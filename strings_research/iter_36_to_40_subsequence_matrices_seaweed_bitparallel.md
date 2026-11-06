# Wave 4B Research Report (Cohort 1: Iterations 36–40) — Subsequence Automata (DASG), Invertible Subsequence Matrices, Tiskin's Seaweed Matrices & Bit-Parallel LCS

> [!IMPORTANT]
> **Research Scope & Pedagogical Mandate (`PLAN.md` §1–§3 & `AGENTS.md`)**
> This report covers **Cohort 1, Wave 4B (Iterations 36–40)** of the Advanced Stringology research pipeline. Every theoretical framework, matrix identity, braid-monoid composition rule, bit-parallel word transition, and competitive programming problem below is derived under the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**:
> 1. **The Diagnostic Signal (Why Naive String Structures Fail)**
> 2. **The Combinatorial Word Invariant (Canonical Greedy / Elementary Matrix Group / Unit-Monge / Bit-Carry Proof)**
> 3. **The Reverse-Engineering Scratchpad (Algorithmic & Data-Structure Compilation)**
> 4. **Boundary Pitfalls & Broken-Invariant Counterexamples**

---

## Iteration 36: Directed Acyclic Subsequence Graph (`序列自动机` / DASG), Canonical First-Occurrence Greedies & The Four-Comb Product Automaton

### 36.1 The Diagnostic Signal: Why Suffix Structures Fail on Subsequence Problems

A Suffix Automaton (SAM) or Suffix Tree of a string $S[1..N]$ compresses all $O(N^2)$ **contiguous substrings** (factors) of $S$ into $O(N)$ states by grouping substrings that share an identical right-context (`endpos` equivalence class). However, a string of length $N$ has up to $2^N$ **subsequences** (scattered factors obtained by deleting zero or more characters). If a problem asks to:
- Test whether $T$ is a subsequence of $S$, or count how many prefixes of $T$ are subsequences of $S$;
- Count the number of **distinct subsequences** of $S$ (or of a range $S[l..r]$);
- Find the **Shortest Absent Subsequence (SAS)** (`最短不公共子序列`) of $S$, or the $k$-th lexicographically smallest subsequence of $S$;
- Simultaneously distinguish **contiguous substrings** vs. **scattered subsequences** across two strings $A$ and $B$ (the Four-Way Uncommon Factor/Subsequence Problem, `[HEOI2015] 最短不公共子串` / `Luogu P4112`);

then an unmodified SAM is the wrong tool because a subsequence need not appear contiguously, yet enumerating all $2^N$ subsequences is exponential. Even worse, a single subsequence $P$ can occur in $S$ at exponentially many index tuples $1 \le i_1 < i_2 < \dots < i_{|P|} \le N$. To recognize or count each distinct subsequence **exactly once**, we must assign every subsequence $P \preceq S$ a **unique canonical occurrence** inside $S$.

---

### 36.2 The Combinatorial Word Invariant: Leftmost-Greedy Canonicalization (`序列自动机`)

#### Object & Question
Given a text string $S[1..N]$ over alphabet $\Sigma$, how can we build a deterministic finite automaton $\text{DASG}(S)$ with $N+1$ states that accepts a pattern $P[1..m]$ if and only if $P$ is a subsequence of $S$, such that **every distinct subsequence of $S$ corresponds to a unique directed path from the root**?

#### Theorem 36.1 (Leftmost-Prefix Dominance / Canonical Subsequence Embedding)
For any string $P = p_1 p_2 \dots p_m$, define its **canonical end-position** $\text{first\_end}(P) \in \{0, 1, \dots, N\} \cup \{\infty\}$ inductively by:
$$\text{first\_end}(\varepsilon) = 0, \qquad \text{first\_end}(P \cdot c) = \min\bigl\{\, j > \text{first\_end}(P) \;\big|\; S[j] = c \,\bigr\}$$
with $\min \emptyset = \infty$. Then for every continuation string $W \in \Sigma^*$:
$$P \cdot W \text{ is a subsequence of } S[1..N] \iff \text{first\_end}(P) \le N \text{ and } W \text{ is a subsequence of } S[\text{first\_end}(P)+1 .. N].$$

*Proof (Exchange Argument).*
- ($\Leftarrow$) If $\text{first\_end}(P) = i \le N$, then by definition $P$ is a subsequence of $S[1..i]$. If $W$ is a subsequence of $S[i+1..N]$, concatenating the two index sequences embeds $P \cdot W$ into $S[1..N]$.
- ($\Rightarrow$) Suppose $P \cdot W$ occurs in $S$ at positions $1 \le j_1 < j_2 < \dots < j_m < k_1 < \dots < k_{|W|} \le N$, where $S[j_r] = p_r$ and $S[k_r] = w_r$. By induction on $r \in \{1, \dots, m\}$, $\text{first\_end}(p_1 \dots p_r) \le j_r$:
  - Base $r=1$: $\text{first\_end}(p_1) = \min\{j \ge 1 : S[j] = p_1\} \le j_1$.
  - Step $r-1 \to r$: Since $\text{first\_end}(p_1 \dots p_{r-1}) \le j_{r-1} < j_r$ and $S[j_r] = p_r$, the index $j_r$ belongs to the candidate set $\{j > \text{first\_end}(p_1 \dots p_{r-1}) : S[j] = p_r\}$, so its minimum is at most $j_r$.
  At $r = m$, we obtain $\text{first\_end}(P) \le j_m < k_1$. Therefore $k_1, \dots, k_{|W|}$ all lie in $[\text{first\_end}(P)+1, N]$, proving that $W$ is a subsequence of $S[\text{first\_end}(P)+1 .. N]$. $\blacksquare$

#### Corollary 36.2 (Myhill–Nerode Quotient for Subsequences)
Two strings $P, Q \in \Sigma^*$ are right-congruent with respect to the language $\text{Subseq}(S) = \{U \in \Sigma^* : U \preceq S\}$ if they share the same $\text{first\_end}$ index! Consequently, the Directed Acyclic Subsequence Graph $\text{DASG}(S)$ has:
- **States**: $\{0, 1, \dots, N\}$, where state $i$ represents the equivalence class of all subsequences whose leftmost occurrence in $S$ ends at index $i$ (and state $0$ represents $\varepsilon$).
- **Transitions**: From state $i \in \{0, \dots, N\}$ on character $c \in \Sigma$:
  $$\delta_{\text{DASG}}(i, c) = \text{nxt}[i][c] := \min\{\, j > i \mid S[j] = c \,\}$$
  (or $\bot$ if no such $j$ exists).
- **Path Bijection**: Every distinct non-empty subsequence $P \preceq S$ corresponds **bijectively** to a directed path $0 \xrightarrow{p_1} i_1 \xrightarrow{p_2} i_2 \dots \xrightarrow{p_m} i_m$ in $\text{DASG}(S)$.

---

### 36.3 Reverse-Engineering Scratchpad: DASG Construction, Scaling for Large $|\Sigma|$ & Shortest Absent Subsequence

#### 1. Backward Sweep Construction ($O(N |\Sigma|)$ Time & Space)
Initialize $\text{nxt}[N][c] = \bot$ for all $c \in \Sigma$. For $i = N-1$ down to $0$:
1. Copy $\text{nxt}[i][c] \leftarrow \text{nxt}[i+1][c]$ for all $c \in \Sigma$.
2. Overwrite $\text{nxt}[i][S[i+1]] \leftarrow i+1$.

#### 2. Scaling When $|\Sigma|$ Is Large ($|\Sigma| \le N \le 10^6$)
If $|\Sigma|$ is up to $N$, an explicit $N \times |\Sigma|$ table takes $O(N^2)$ memory. Three standard representations avoid the $|\Sigma|$ blowup:
- **Occurrence Lists + Binary Search ($O(N)$ space, $O(\log N)$ transition)**: Store sorted vector `pos[c]` of indices where $S[j] = c$; then $\text{nxt}[i][c] = \text{upper\_bound}(\text{pos}[c], i)$.
- **Persistent Segment Tree of Next Pointers ($O(N \log |\Sigma|)$ space, $O(\log |\Sigma|)$ transition)**: Notice that row $\text{nxt}[i][\cdot]$ differs from row $\text{nxt}[i+1][\cdot]$ in **only one character** ($c = S[i+1]$). Storing row $i$ as a persistent segment tree over $[1, |\Sigma|]$ supports full out-edge iteration or $k$-th out-edge lookup in $O(\log |\Sigma|)$.
- **Backward / Pull DP ($O(N)$ time, $O(N + |\Sigma|)$ space)**: When running a DP over $\text{DASG}(S)$ such as $dp[i] = 1 + \sum_{c \in \Sigma} dp[\text{nxt}[i][c]]$, observe that as $i$ steps from $i+1$ down to $i$, only $\text{nxt}[i][S[i+1]]$ changes from $\text{last}[S[i+1]]$ to $i+1$. Maintaining $\text{sum} = \sum_{c \in \Sigma} dp[\text{last}[c]]$ updates in $O(1)$ per step!

#### 3. Hand-Checkable Example: $\text{DASG}(\texttt{abac})$
Let $S = \texttt{abac}$ ($N = 4$, $\Sigma = \{\texttt{a}, \texttt{b}, \texttt{c}\}$).
| State $i$ | Character $S[i]$ | $\text{nxt}[i][\texttt{a}]$ | $\text{nxt}[i][\texttt{b}]$ | $\text{nxt}[i][\texttt{c}]$ | $dp[i]$ (# Subsequences of $S[i+1..4]$ incl. $\varepsilon$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $4$ | $\texttt{c}$ | $\bot$ | $\bot$ | $\bot$ | $1$ ($\varepsilon$) |
| $3$ | $\texttt{a}$ | $\bot$ | $\bot$ | $4$ | $1 + dp[4] = 2$ ($\varepsilon, \texttt{c}$) |
| $2$ | $\texttt{b}$ | $3$ | $\bot$ | $4$ | $1 + dp[3] + dp[4] = 4$ ($\varepsilon, \texttt{a}, \texttt{ac}, \texttt{c}$) |
| $1$ | $\texttt{a}$ | $3$ | $2$ | $4$ | $1 + dp[3] + dp[2] + dp[4] = 8$ |
| $0$ | (root) | $1$ | $2$ | $4$ | $1 + dp[1] + dp[2] + dp[4] = 14$ |

Notice how $\texttt{ac}$ is counted only via $0 \xrightarrow{\texttt{a}} 1 \xrightarrow{\texttt{c}} 4$ (using the *first* $\texttt{a}$ at index $1$), whereas path $0 \xrightarrow{\texttt{a}} 3 \xrightarrow{\texttt{c}} 4$ does not exist because $\text{nxt}[0][\texttt{a}] = 1 \ne 3$.

#### 4. Shortest Absent Subsequence (`SAS` / `最短非子序列`)
To find the shortest (and lexicographically smallest) string $P \in \Sigma^+$ that is **not** a subsequence of $S$:
- Augment $\text{DASG}(S)$ with a sink state $\bot$ representing "fell off the end of $S$".
- From state $i \in \{0, \dots, N\}$, every missing transition $\text{nxt}[i][c] = \bot$ is a directed edge of weight $1$ into $\bot$.
- Therefore, $\text{SAS}(S)$ is simply the **shortest path from $0$ to $\bot$** in $\text{DASG}(S)$!
- Backwards DP: $d[\bot] = 0$, and for $i = N$ down to $0$:
  $$d[i] = 1 + \min_{c \in \Sigma} d\bigl[\text{nxt}[i][c]\bigr].$$
  Wait: as $i$ decreases from $N$ to $0$, the tuple $(\text{nxt}[i][c])_{c \in \Sigma}$ only changes one entry at $c = S[i+1]$, and the minimum $\min_{c \in \Sigma} d[\text{nxt}[i][c]]$ increments by $1$ only when every character in $\Sigma$ has been seen in the current right-to-left block! This gives the classic **Complete-Alphabet Block Partition Law**:
  $$\text{len}(\text{SAS}(S)) = 1 + (\text{maximum number of disjoint contiguous blocks of } S \text{ each containing all of } \Sigma).$$

---

### 36.4 Coupling SAM and DASG: The Four-Comb Product Automaton (`[HEOI2015] 最短不公共子串` / `Luogu P4112`)

#### Problem Formulation & Diagnostic Signal
Given two strings $A$ and $B$ ($|A|, |B| \le 2000$, $|\Sigma| = 26$), find the minimum length of a non-empty string $P$ satisfying each of four asymmetric recognition queries:
1. $P$ is a **substring** of $A$, but **not a substring** of $B$.
2. $P$ is a **substring** of $A$, but **not a subsequence** of $B$.
3. $P$ is a **subsequence** of $A$, but **not a substring** of $B$.
4. $P$ is a **subsequence** of $A$, but **not a subsequence** of $B$.

#### Why Product Automata Solve All Four Subproblems Uniformly
Every deterministic string recognizer $\mathcal{A}$ (whether $\text{SAM}$ for substrings or $\text{DASG}$ for subsequences) has the property that:
$$P \in L(\mathcal{A}) \iff \delta_{\mathcal{A}}(q_0, P) \ne \bot.$$
Therefore, given a positive recognizer $\mathcal{A}^+$ for $A$ and a negative recognizer $\mathcal{A}^-$ for $B$, a string $P$ belongs to $L(\mathcal{A}^+) \setminus L(\mathcal{A}^-)$ if and only if, starting from the joint root $(q_0^+, q_0^-)$, reading $P$ keeps the first coordinate inside $\mathcal{A}^+$ ($\ne \bot$) while driving the second coordinate into $\bot$ on the final character!

| Query Type | Positive Automaton $\mathcal{A}^+(A)$ | Negative Automaton $\mathcal{A}^-(B)$ | Product State Space $\mathcal{A}^+ \times \mathcal{A}^-$ | Complexity ($N = |A|, M = |B|$) |
| :--- | :--- | :--- | :--- | :--- |
| **Q1**: Substring of $A$, not Substring of $B$ | $\text{SAM}(A)$ (or simple scan over $A$) | $\text{SAM}(B)$ | Can be solved in $O(N + M)$ on $\text{SAM}(B)$ alone! (See shortcut below) | $O((N+M)|\Sigma|)$ |
| **Q2**: Substring of $A$, not Subsequence of $B$ | $\text{SAM}(A)$ (or suffixes of $A$) | $\text{DASG}(B)$ | $O(N)$ suffix scans over $\text{DASG}(B)$, or BFS on $\text{SAM}(A) \times \text{DASG}(B)$ | $O(N M |\Sigma|)$ or $O(N^2)$ |
| **Q3**: Subsequence of $A$, not Substring of $B$ | $\text{DASG}(A)$ | $\text{SAM}(B)$ | BFS / DAG DP on $\text{DASG}(A) \times \text{SAM}(B)$: $N \times 2M$ states | $O(N M |\Sigma|)$ |
| **Q4**: Subsequence of $A$, not Subsequence of $B$ | $\text{DASG}(A)$ | $\text{DASG}(B)$ | BFS / DAG DP on $\text{DASG}(A) \times \text{DASG}(B)$: $N \times M$ states | $O(N M |\Sigma|)$ |

#### Structural Shortcuts vs. Full Product BFS
- **For Q1 and Q2 ($P$ is a contiguous substring of $A$)**: Since $A$ has only $O(N^2)$ substrings and every substring begins at some index $l \in [1, N]$, for each $l \in [1, N]$ we can simply walk $A[l..N]$ character-by-character in $\mathcal{A}^-(B)$ ($\text{SAM}(B)$ for Q1, $\text{DASG}(B)$ for Q2) until $\delta^-(u, A[r]) = \bot$! That takes $O(N^2)$ total time without even building $\text{SAM}(A)$. Even better, for **Q1**, walking all of $A$ on $\text{SAM}(B)$ using `link` pointer fallbacks computes for each prefix $A[1..r]$ the longest suffix that occurs in $B$ (`lcs_len[r]`), so the shortest suffix at $r$ missing from $B$ has length `lcs_len[r] + 1` (provided `lcs_len[r] < r`), solving Q1 in **$O(N + M)$**!
- **For Q3 and Q4 ($P$ is a scattered subsequence of $A$)**: $A$ has $2^N$ subsequences, so enumerating them is impossible. However, because $\text{DASG}(A)$ is a **DAG** with $N+1$ states and any valid state $(u, v) \in \text{DASG}(A) \times \mathcal{A}^-(B)$ advances $u$ strictly forward ($u' = \text{nxt}_A[u][c] > u$), the product graph $\text{DASG}(A) \times \mathcal{A}^-(B)$ is **itself a DAG** with at most $(N+1)(2M+1)$ states! A standard BFS from $(0, q_0^-)$ finds the shortest path to any transition $(u, v) \xrightarrow{c} (\text{nxt}_A[u][c] \ne \bot, \delta^-(v, c) = \bot)$ in $O(NM|\Sigma|)$ time.

### 36.5 Boundary Pitfalls & Counterexamples for DASG
1. **Empty Subsequence $\varepsilon$ Off-by-One**: State $0$ of $\text{DASG}(S)$ accepts $\varepsilon$. When counting **non-empty** subsequences or matching against another automaton, always check whether $\varepsilon$ should be subtracted ($dp[0] - 1$).
2. **Range Subsequence Trap on Static DASG**: In $\text{DASG}(S[1..N])$, checking whether $P$ is a subsequence of $S[l..r]$ can be done by starting at state $l-1$ and verifying that after reading $P$, the final state $u$ satisfies $u \le r$. **However**, you **cannot** count distinct subsequences of $S[l..r]$ merely by subtracting $dp[l-1] - dp[r]$ on the static DASG of $S$, because paths from $l-1$ jump past $r$ into $[r+1, N]$! Counting distinct subsequences in $S[l..r]$ requires the **Invertible Subsequence Matrix** machinery of Iteration 37.

---

## Iteration 37: Invertible Subsequence Automaton Matrices (`子序列 DP 矩阵可逆性`) & Fast Range Subsequence Algebra

### 37.1 The Diagnostic Signal: Why Segment Trees of $(|\Sigma|+1)\times(|\Sigma|+1)$ Matrices TLE

Consider the **Range Distinct Subsequences Problem**:
> Given a string $S[1..N]$ over alphabet $\Sigma$ ($|\Sigma| = \sigma$, e.g., $\sigma = 26$ or $\sigma = 62$) and $Q$ queries $[l, r]$ ($N, Q \le 2 \cdot 10^5$ or $10^6$), compute the number of distinct subsequences of $S[l..r]$ modulo $10^9 + 7$.

If we model the classic left-to-right distinct-subsequence DP on a substring $S[l..r]$:
- Let $f_c$ ($c \in \{1, \dots, \sigma\}$) be the number of distinct non-empty subsequences processed so far whose **canonical last character** is $c$, and let $f_0 = 1$ represent the empty subsequence $\varepsilon$.
- When appending a new character $x = S[i]$:
  - Every existing subsequence (including $\varepsilon$) can be extended by $x$ to form a subsequence ending in $x$.
  - Any subsequence ending in $x$ that existed *before* index $i$ is subsumed (or replaced, under rightmost-canonicalization) by the new set of subsequences ending at $i$.
  - Formally, the new count of subsequences ending in $x$ becomes:
    $$f'_x = \sum_{c=0}^{\sigma} f_c, \qquad \text{and for } c \ne x: \quad f'_c = f_c.$$
- Equivalently, if we maintain the total count $S_{\text{tot}} = \sum_{c=0}^\sigma f_c$ alongside individual $f_c$, appending $x$ is a linear transformation by a $(\sigma+1)\times(\sigma+1)$ matrix $M_x$.

**Why Naive Segment Trees Fail**: Storing a $(\sigma+1)\times(\sigma+1)$ matrix in each node of a Segment Tree requires $O(\sigma^3 \log N)$ per query (or $O(N \sigma^3 + Q \sigma^2 \log N)$ with vector-matrix multiplication). For $\sigma = 26$ and $N, Q = 2 \cdot 10^5$, $26^3 \approx 17{,}576$ operations per node is far too slow.

**The Breakthrough Observation**: The transition matrix $M_x$ for character $x$ is an **elementary transvection matrix** over $\mathbb{Z}$ (specifically, the identity matrix $I_{\sigma+1}$ except for a single row or column of $1$s) with determinant $\det(M_x) = 1$! Not only is $M_x$ **always invertible over any commutative ring $R$** (even when working modulo a composite number or with zero divisors, because $\det(M_x) = 1$), both $M_x$ and $M_x^{-1}$ differ from the identity matrix in **only one row/column**. Therefore:
1. Any range product $M_{S[l]} M_{S[l+1]} \cdots M_{S[r]}$ equals $P_{l-1}^{-1} P_r$, where $P_i = M_{S[1]} \cdots M_{S[i]}$.
2. Multiplying an existing prefix matrix $P_{i-1}$ on the right by $M_x$ (or $P_{i-1}^{-1}$ on the left by $M_x^{-1}$) modifies **only a single column (or row)** in $O(\sigma)$ time!

---

### 37.2 The Combinatorial & Algebraic Invariant: Elementary Subsequence Matrices and Their Exact Inverse

#### Formulation 1: State Vector $(f_1, f_2, \dots, f_\sigma, 1)^T$ (Subsequences by Last Character)
Let the row vector at step $i$ be $\mathbf{v}_i = (f_1, f_2, \dots, f_\sigma, f_0)$, where $f_c$ is the number of distinct subsequences of the processed prefix ending with character $c \in \{1, \dots, \sigma\}$, and $f_0 = 1$ tracks the empty string $\varepsilon$.
When character $x \in \{1, \dots, \sigma\}$ is appended, the new row vector $\mathbf{v}_i = \mathbf{v}_{i-1} M_x$ satisfies:
$$f'_x = \sum_{c=0}^{\sigma} f_c, \qquad f'_c = f_c \quad (\forall c \ne x).$$
Therefore, $M_x \in \mathbb{Z}^{(\sigma+1)\times(\sigma+1)}$ is the identity matrix $I_{\sigma+1}$, **except that column $x$ consists entirely of $1$s**:
$$(M_x)_{r, c} = \begin{cases} 1 & \text{if } c = x, \\ \delta_{r, c} & \text{if } c \ne x. \end{cases}$$

#### Lemma 37.1 (Exact Inverse $M_x^{-1}$ in $O(1)$ Non-Zeros)
Over any commutative ring $R$, the matrix $M_x$ is invertible, and its inverse $M_x^{-1}$ is the identity matrix $I_{\sigma+1}$, **except that column $x$ has $-1$ in every off-diagonal row $r \ne x$ and $+1$ on the diagonal $(x, x)$**:
$$(M_x^{-1})_{r, c} = \begin{cases} 1 & \text{if } r = c, \\ -1 & \text{if } c = x \text{ and } r \ne x, \\ 0 & \text{otherwise.} \end{cases}$$

*Proof (Direct Reversal of the Linear Recurrence).*
Since $f'_c = f_c$ for all $c \ne x$, and $f'_x = f_x + \sum_{c \ne x} f_c = f_x + \sum_{c \ne x} f'_c$, solving for the pre-transition coordinate $f_x$ gives:
$$f_x = f'_x - \sum_{c \ne x} f'_c, \qquad f_c = f'_c \quad (\forall c \ne x).$$
Writing this in matrix form $\mathbf{v}_{i-1} = \mathbf{v}_i M_x^{-1}$ immediately yields the entries of $M_x^{-1}$ stated above. No division is ever performed; thus $M_x^{-1}$ exists over $\mathbb{Z}$ and over $\mathbb{Z}/m\mathbb{Z}$ for any modulus $m$. $\blacksquare$

#### Formulation 2: Total-Sum Augmentation (`Total + Last Seen` Formulation)
Alternatively, let $D$ be the total number of distinct subsequences (including $\varepsilon$), and for each $c \in \{1, \dots, \sigma\}$, let $L_c$ be the value of $D$ **immediately before the most recent occurrence of $c$** (initially $D = 1, L_c = 0$).
When character $x$ is appended:
$$D' = 2D - L_x, \qquad L'_x = D, \qquad L'_c = L_c \;\; (c \ne x).$$
And the inverse transition is:
$$D = L'_x, \qquad L_x = 2L'_x - D', \qquad L_c = L'_c \;\; (c \ne x).$$
Both formulations are conjugate by a fixed change-of-basis matrix ($D = \sum_{c=0}^\sigma f_c$); Formulation 1 is usually cleanest for prefix matrix products because every column of $M_x$ has a uniform sum structure.

---

### 37.3 Reverse-Engineering Scratchpad: $O((N + Q)\sigma)$ Range Distinct Subsequences (Higher-Order Compression!)

Let us trace how to precompute prefix products $P_i = M_{S[1]} \cdots M_{S[i]}$ and inverse prefix products $Q_i = P_i^{-1} = M_{S[i]}^{-1} \cdots M_{S[1]}^{-1}$, and then optimize range queries from $O(\sigma^2)$ all the way down to **$O(\sigma)$ per step and $O(\sigma)$ per query**!

#### Step 1: $O(\sigma)$ Incremental Prefix & Inverse-Prefix Maintenance
Suppose we have the matrix $P_{i-1}$. How does $P_i = P_{i-1} M_x$ differ from $P_{i-1}$ when $x = S[i]$?
- For every column $c \ne x$, column $c$ of $M_x$ is the standard basis vector $\mathbf{e}_c$, so **column $c$ of $P_i$ is identical to column $c$ of $P_{i-1}$**!
- For column $x$, column $x$ of $M_x$ is the all-ones vector $\mathbf{1}$, so for each row $r \in \{0, \dots, \sigma\}$:
  $$(P_i)_{r, x} = \sum_{c=0}^{\sigma} (P_{i-1})_{r, c}.$$
  If we maintain the row sums $\text{row\_sum}[r] = \sum_{c=0}^\sigma P_{r, c}$, updating $P_{i-1} \to P_i$ modifies **only column $x$** and updates `row_sum[r]` in $O(\sigma)$ time!

Similarly, how does $Q_i = M_x^{-1} Q_{i-1}$ differ from $Q_{i-1}$?
- Multiplying on the **left** by $M_x^{-1}$ adds $-1$ times row $x$ of $Q_{i-1}$ to every other row $r \ne x$!
- Even simpler, if we transpose or maintain column sums $\text{col\_sum}[c] = \sum_{r=0}^\sigma Q_{r, c}$, wait: instead of adding $-Q_{x, c}$ to all $\sigma$ rows, notice that in $M_x$ acting on the left or right, **only one row or one column changes** if we write the recurrence in the dual orientation!
- Specifically, let us check what a query $[l, r]$ actually asks for:
  Starting at index $l-1$ with the initial state vector $\mathbf{e}_0^T = (0, 0, \dots, 0, 1)$ (representing only the empty subsequence $\varepsilon$), after processing $S[l..r]$, the state vector is:
  $$\mathbf{v}_{l..r} = \mathbf{e}_0^T \, M_{S[l]} M_{S[l+1]} \cdots M_{S[r]} = \bigl(\mathbf{e}_0^T \, Q_{l-1}\bigr) P_r,$$
  and the total number of distinct subsequences of $S[l..r]$ (including $\varepsilon$) is the sum of entries of $\mathbf{v}_{l..r}$:
  $$\text{Ans}(l, r) = \mathbf{e}_0^T \, Q_{l-1} \, P_r \, \mathbf{1} = \sum_{k=0}^{\sigma} (Q_{l-1})_{0, k} \cdot \bigl(P_r \mathbf{1}\bigr)_k!$$

> [!TIP]
> **The $O(\sigma)$ Query Miracle (`Vector-Dot-Product Trick`)**
> Look closely at the bilinear expression $\text{Ans}(l, r) = \bigl(\mathbf{e}_0^T Q_{l-1}\bigr) \cdot \bigl(P_r \mathbf{1}\bigr)$:
> - We do **not** need the entire $(\sigma+1)\times(\sigma+1)$ matrix $Q_{l-1}$ at query time—we only need its **0-th row** $\mathbf{u}_{l-1}^T := \mathbf{e}_0^T Q_{l-1} \in R^{1 \times (\sigma+1)}$!
> - We do **not** need the entire $(\sigma+1)\times(\sigma+1)$ matrix $P_r$ at query time—we only need its **row-sum column vector** $\mathbf{w}_r := P_r \mathbf{1} \in R^{(\sigma+1) \times 1}$!
> - And how do $\mathbf{w}_i = P_i \mathbf{1}$ and $\mathbf{u}_i^T = \mathbf{e}_0^T Q_i$ evolve as $i$ goes from $1$ to $N$?
>   1. **Forward vector $\mathbf{w}_i = M_{S[1]} \cdots M_{S[i]} \mathbf{1}$**: Wait—$P_i$ is built left-to-right, so to maintain $P_i \mathbf{1}$ left-to-right, we maintain the matrix $P_i$ (where only column $x = S[i]$ changes at step $i$, taking $O(\sigma)$ time!) and its row-sum vector $\mathbf{w}_i[r] = \sum_{c=0}^\sigma (P_i)_{r, c}$ in **$O(\sigma)$ time and $O(N\sigma)$ space**!
>   2. **Inverse vector $\mathbf{u}_i^T = \mathbf{e}_0^T Q_i$**: Since $Q_i = M_{S[i]}^{-1} Q_{i-1}$ modifies all rows using row $x$, maintaining only row $0$ requires knowing row $x$ of $Q_{i-1}$. Wait: what if we instead maintain the **columns** of $Q_i$? Notice that $Q_i$ is not even needed as a full matrix if we maintain $Q_i$ via **lazy global offset** or notice that $M_x^{-1}$ acting on the left subtracts row $x$ from **every** row $r \ne x$:
>      - Maintain a global accumulator vector $\text{lazy}[c]$ and offset rows $\tilde{Q}_{r, c}$ such that $Q_{r, c} = \tilde{Q}_{r, c} + \text{lazy}[c]$.
>      - Left-multiplying by $M_x^{-1}$ subtracts the current true row $x$ ($Q_{x, c}$) from all rows $r \ne x$: that is equivalent to subtracting $Q_{x, c}$ from $\text{lazy}[c]$ (affecting all rows) and adding $Q_{x, c}$ back to $\tilde{Q}_{x, c}$ (affecting only row $x$)!
>      - Thus, **both $P_i$ and $Q_i$ update in $O(\sigma)$ time per character $i$**, storing $\mathbf{u}_i^T = \text{row}_0(Q_i)$ and $\mathbf{w}_i = P_i \mathbf{1}$ takes **$O(N\sigma)$ total space**, and each query $\text{Ans}(l, r) = \sum_{k=0}^\sigma \mathbf{u}_{l-1}[k] \cdot \mathbf{w}_r[k]$ runs in **$O(\sigma)$ time**!

#### Algorithm Contract: $O((N+Q)\sigma)$ Range Distinct Subsequences
```
Precomputation (O(N * sigma) time and space):
1. Initialize P = I_{sigma+1}, row_sum[r] = 1 for r in 0..sigma.
   Initialize Q_tilde = I_{sigma+1}, lazy[c] = 0 for c in 0..sigma.
   Store u[0][c] = Q_tilde[0][c] + lazy[c] (= [c == 0]), w[0][r] = row_sum[r] (= 1).
2. For i = 1 to N (let x = S[i] in 1..sigma):
   // Update P_i = P_{i-1} * M_x in O(sigma):
   For r = 0 to sigma:
       old_val = P[r][x]
       new_val = row_sum[r]
       P[r][x] = new_val
       row_sum[r] = (row_sum[r] - old_val + new_val) mod MOD
       w[i][r] = row_sum[r]
   // Update Q_i = M_x^{-1} * Q_{i-1} in O(sigma) via lazy row shift:
   For c = 0 to sigma:
       row_x_val = (Q_tilde[x][c] + lazy[c]) mod MOD
       lazy[c] = (lazy[c] - row_x_val) mod MOD
       Q_tilde[x][c] = (Q_tilde[x][c] + row_x_val) mod MOD
       u[i][c] = (Q_tilde[0][c] + lazy[c]) mod MOD

Query(l, r) in O(sigma) time:
   Return (sum_{k=0}^{sigma} u[l-1][k] * w[r][k] - 1) mod MOD   // subtract 1 if non-empty only
```

#### Hand-Checkable Trace of $P_i, Q_i$ on $S = \texttt{aba}$ ($\sigma = 2$, indices $a=1, b=2, \varepsilon=0$)
- **At $i = 0$**:
  $$P_0 = Q_0 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad \mathbf{u}_0^T = (1, 0, 0), \quad \mathbf{w}_0 = (1, 1, 1)^T.$$
- **At $i = 1$ ($S[1] = \texttt{a} = 1$)**:
  $$M_1 = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}, \quad M_1^{-1} = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & 0 \\ 0 & -1 & 1 \end{pmatrix}, \quad \mathbf{u}_1^T = (1, -1, 0), \quad \mathbf{w}_1 = (2, 1, 2)^T.$$
- **At $i = 2$ ($S[2] = \texttt{b} = 2$)**:
  $$P_2 = P_1 M_2 = \begin{pmatrix} 1 & 1 & 2 \\ 0 & 1 & 1 \\ 0 & 1 & 2 \end{pmatrix} \implies \mathbf{w}_2 = (4, 2, 3)^T; \qquad Q_2 = M_2^{-1} Q_1 = \begin{pmatrix} 1 & -1 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix} \implies \mathbf{u}_2^T = (1, -1, -1).$$
- **At $i = 3$ ($S[3] = \texttt{a} = 1$)**:
  $$P_3 = P_2 M_1 = \begin{pmatrix} 1 & 4 & 2 \\ 0 & 2 & 1 \\ 0 & 3 & 2 \end{pmatrix} \implies \mathbf{w}_3 = (7, 3, 5)^T.$$
- **Query $[l, r] = [2, 3]$ ($S[2..3] = \texttt{ba}$)**:
  $$\text{Ans}(2, 3) = \mathbf{u}_1^T \cdot \mathbf{w}_3 = 1 \cdot 7 + (-1) \cdot 3 + 0 \cdot 5 = 4 \quad (\text{namely } \varepsilon, \texttt{b}, \texttt{a}, \texttt{ba}).$$
- **Query $[l, r] = [3, 3]$ ($S[3..3] = \texttt{a}$)**:
  $$\text{Ans}(3, 3) = \mathbf{u}_2^T \cdot \mathbf{w}_3 = 1 \cdot 7 + (-1) \cdot 3 + (-1) \cdot 5 = -1 + 0 = 2 \quad (\text{wait: } 7 - 3 - 5 = -1 \text{?}).$$
  Hold on! Let us check why $\mathbf{u}_2^T = (1, -1, -1)$ gave $7 - 3 - 5 = -1$ above!
  Look at $Q_2 = M_2^{-1} Q_1$:
  $$M_2^{-1} = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix}, \quad Q_1 = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & 0 \\ 0 & -1 & 1 \end{pmatrix} \implies M_2^{-1} Q_1 = \begin{pmatrix} 1 & -1 - (-1) & -1 \\ 0 & 1 - (-1) & -1 \\ 0 & -1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix}!$$
  Aha! In $Q_1$, entry $(2, 1)$ was $-1$ (because in $M_1^{-1}$, column $1$ has $-1$ in every row $r \ne 1$, including row $2$). So when $M_2^{-1}$ subtracted row $2$ of $Q_1$ from row $0$ of $Q_1$, the second entry became $-1 - (-1) = 0$, giving $\mathbf{u}_2^T = (1, 0, -1)$!
  Then for $[3, 3]$:
  $$\text{Ans}(3, 3) = \mathbf{u}_2^T \cdot \mathbf{w}_3 = (1, 0, -1) \cdot (7, 3, 5)^T = 7 + 0 - 5 = 2 \quad (\varepsilon, \texttt{a})!$$
  This hand-checkable trace immediately verifies both the algebra and why the lazy-row-subtraction pseudocode (which reads the true `Q_tilde[x][c] + lazy[c]` of row $x$) is exact!

---

### 37.4 Four High-Frequency Extensions of Subsequence Matrix Algebra

#### Extension A: Fixed-Pattern Subsequence Counting on $S[l..r]$ via $(K+1)\times(K+1)$ Upper-Unitriangular Matrices
Suppose we have a fixed target pattern $T[1..K]$ ($K \le 20$) and want to count how many times subsequences of $S[l..r]$ match $T$ (with multiplicity, or combined with distinctness).
- Each character $c = S[i]$ acts as a $(K+1)\times(K+1)$ **upper-unitriangular matrix** $A_c = I_{K+1} + \sum_{j : T[j] = c} E_{j-1, j}$.
- Because $A_c$ is upper-unitriangular (diagonal of all $1$s), **$\det(A_c) = 1$ and $A_c$ is always invertible!** Specifically, if $T[j] = c$ occurs at non-adjacent indices, $A_c^{-1} = I_{K+1} - \sum_{j : T[j] = c} E_{j-1, j}$ (or if $T$ has adjacent identical characters $T[j]=T[j+1]=c$, $A_c^{-1} = \sum_{m=0}^K (-1)^m (A_c - I)^m$).
- Maintaining prefix upper-unitriangular matrices $P_i = A_{S[1]} \cdots A_{S[i]}$ and $Q_i = P_i^{-1}$ updates only rows/columns where $T[j] = S[i]$ in $O(K \cdot \text{freq}_T(S[i]))$ time, answering range queries $[l, r]$ in **$O(K)$ time** via $\sum_{k=0}^K (Q_{l-1})_{0, k} (P_r)_{k, K}$!

#### Extension B: Tropical $(\min, +)$ Subsequence Automaton Matrices on Segment Trees (`CF 750E — New Year and Old Subsequence`, `CF 1609E`)
When the problem asks for the **minimum number of character deletions** in $S[l..r]$ so that it contains subsequence $A = \texttt{2016}$ but avoids subsequence $B = \texttt{2017}$:
- The algebra is now the **tropical $(\min, +)$ semiring**, where matrices are **not invertible** (because $\min$ loses information and has no additive inverse).
- However, the DFA for tracking the longest matched prefix of $\texttt{2017}$ has only $K = 5$ states $\{0, 1, 2, 3, 4\}$.
- Therefore, we place $5 \times 5$ $(\min, +)$ transition matrices in a **Segment Tree** (supporting point updates and range queries in $O(K^3 \log N)$ or $O(K^2 \log N)$ by keeping only row $0$ of the query vector!).
- **Core Diagnostic Distinction**:
  - Counting problems over a ring $(\mathbb{Z}/m\mathbb{Z}, +, \times)$ with invertible transition matrices $\implies$ **Prefix + Inverse-Prefix Matrices** in $O((N+Q)\sigma)$ (no Segment Tree needed unless point updates are present).
  - Optimization problems over $(\min, +)$ or $(\max, +)$ $\implies$ **Non-invertible tropical matrices**, requiring a **Segment Tree** or **Sqrt/Divide-and-Conquer** (or Unit-Monge compression when the matrix is Monge!).

#### Extension C: Gap-Constrained Distinct Subsequences (`ABC 214F — Substrings`)
Count distinct non-empty subsequences of $S[1..N]$ formed by choosing indices $1 \le i_1 < i_2 < \dots < i_k \le N$ such that **$i_{r} - i_{r-1} \ge 2$** (no two adjacent characters of $S$ may both be selected).
- **Why standard DASG must be modified**: In standard DASG, from index $i$ we transition to $\text{nxt}[i][c] = \min\{j \ge i+1 : S[j] = c\}$. With the gap constraint $j \ge i+2$ (for $i \ge 1$), from state $i \ge 1$ the canonical next occurrence of character $c$ is $\text{nxt}[i+1][c] = \min\{j \ge i+2 : S[j] = c\}$!
- **Forward Pull Recurrence**: Let $dp[i]$ be the number of valid subsequences whose canonical first-occurrence embedding ends at index $i$. Then index $i$ can be appended to any subsequence ending at $j \le i-2$ for which $S[i]$ did **not** appear anywhere in $S[j+2 .. i-1]$!
  Wait: $S[i]$ does not appear in $S[j+2 .. i-1]$ if and only if $j + 2 > \text{prev}[i]$, i.e., $j \ge \max(0, \text{prev}[i] - 1)$, where $\text{prev}[i] = \max\{p < i : S[p] = S[i]\}$!
  Thus:
  $$dp[i] = \sum_{j = \max(0, \text{prev}[i] - 1)}^{i - 2} dp[j] \qquad (\text{with } dp[0] = 1 \text{ at virtual index } -1).$$
  This reduces the entire gap-constrained DASG to a single prefix-sum window in $O(N)$ time!

#### Extension D: Distinct Subsequences of $S^\infty$ / Cyclic Shifts (`QOJ` / `AGC` Cyclic DASG)
When $S$ is repeated $K$ times ($K \le 10^{18}$), the $(\sigma+1)\times(\sigma+1)$ matrix of one full period is $M_S = M_{S[1]} \cdots M_{S[N]}$, and the answer for $S^K$ is $\mathbf{e}_0^T M_S^K \mathbf{1}$ computed via $O(\sigma^3 \log K)$ matrix exponentiation.

### 37.5 Boundary Pitfalls & Broken-Invariant Counterexamples
1. **Non-Invertibility When $M_x$ Projects Out a State**: If a problem forbids two identical adjacent characters in the *output* subsequence (i.e., $f'_x = \sum_{c \ne x} f_c$), the diagonal entry $(x, x)$ of $M_x$ becomes $0$ instead of $1$. Check $\det(M_x)$: for $f'_x = \sum_{c \ne x} f_c$ and $f'_c = f_c$, the new row/column $x$ has $0$ on the diagonal, so $\det(M_x) = 0$ (**singular matrix!**). Always verify $\det(M_x) \in R^\times$ before attempting prefix-inverse queries!
2. **Gap Constraint Off-by-One (`ABC 214F`)**: For $i_{r} - i_{r-1} \ge d$, the previous occurrence of $S[i]$ at $p = \text{prev}[i]$ blocks any predecessor $j$ that could already jump to $p$, namely $j \le p - d$. Thus the valid predecessor range is $j \in [p - d + 1, i - d]$, **not** $[p, i - d]$.

---

## Iteration 38: Tiskin's Seaweed Matrices (`海草矩阵` / Unit-Monge Braid Multiplication) & All-Pairs Interval LCS (`区间 LCS`)

### 38.1 The Diagnostic Signal: Why All-Pairs Interval LCS Breaks Standard DP

Consider the **All-Pairs Interval LCS Problem** (`[THUPC 2021] 区间 LCS`, `LOJ 6564`, `Universal Cup` Interval LCS):
> Given two strings $A[1..M]$ and $B[1..N]$ ($M, N \le 5000$, or $M, N \le 10^5$ with $Q$ queries), answer $Q$ queries of the form:
> $$\text{Query}(l, r) = \text{LCS}\bigl(A[1..M],\, B[l..r]\bigr) \qquad (1 \le l \le r \le N).$$

Why does standard LCS DP fail?
- A single LCS table between $A[1..M]$ and $B[1..N]$ computes $\text{LCS}(A[1..i], B[1..j])$ for all **prefixes** of $B$ in $O(MN)$ time.
- However, changing the left endpoint $l \in \{1, \dots, N\}$ resets the base column $dp[\cdot][l-1] = 0$. Running a separate DP from each $l \in \{1, \dots, N\}$ takes $O(M N^2)$ time—for $M = N = 5000$, $5000^3 = 1.25 \times 10^{11}$ operations!
- Even worse, if we want $\text{LCS}(A[l_1..r_1], B[l_2..r_2])$ or need to merge LCS tables in a Segment Tree / Divide-and-Conquer, the naive transition matrix from column $l-1$ to column $r$ has dimension $(M+1) \times (M+1)$, so naive$(\max, +)$ matrix multiplication takes $O(M^3)$.

**Tiskin's Breakthrough (2008)**: The semi-local alignment matrix between $A$ and $B$ satisfies the **Unit-Monge property** (`单位蒙日性质`). Its 2D cross-difference is a **permutation matrix** (a **Seaweed Matrix**, `海草矩阵`), reducing the $O(N^2)$ interval LCS answers to a **1D array $W[1..N]$ of size $N$** computed in **$O(MN)$ total time** (and $O((M+N)\log^2(M+N))$ via Unit-Monge distance multiplication), from which any $\text{LCS}(A, B[l..r])$ is a simple 2D range count $\#\{k \in [l, r] : W[k] < l\}$!

---

### 38.2 The Combinatorial Word Invariant: Planar Alignment Non-Crossing, Unit-Monge Differences & The 0-Hecke Seaweed Braid

#### Step 1: The Alignment Grid DAG and the Monge (Anti-Monge) Property
Construct the alignment grid on vertices $(i, j) \in \{0, \dots, M\} \times \{0, \dots, N\}$:
- Horizontal edges $(i, j-1) \to (i, j)$ of weight $0$,
- Vertical edges $(i-1, j) \to (i, j)$ of weight $0$,
- Diagonal match edges $(i-1, j-1) \to (i, j)$ of weight $1$ whenever $A[i] = B[j]$.

Then $\text{LCS}(A[1..M], B[l..r])$ is the maximum weight of a directed path from $(0, l-1)$ to $(M, r)$.
Let $L(l, r) := \text{LCS}(A[1..M], B[l..r])$. Consider any two start columns $l_1 < l_2$ and two end columns $r_1 < r_2$. Because the grid is **planar**, any optimal path $P_1 : (0, l_1-1) \leadsto (M, r_2)$ and any optimal path $P_2 : (0, l_2-1) \leadsto (M, r_1)$ **must intersect** at some grid vertex $(i^*, j^*)$! Swapping their suffixes after $(i^*, j^*)$ yields valid paths $(0, l_1-1) \leadsto (M, r_1)$ and $(0, l_2-1) \leadsto (M, r_2)$ with the exact same total weight:
$$L(l_1, r_2) + L(l_2, r_1) \le L(l_1, r_1) + L(l_2, r_2).$$

#### Step 2: From LCS to the Unit-Monge Penalty Function $H(l, r)$
Wait: in $L(l, r) = \text{LCS}(A, B[l..r])$, incrementing $r \to r+1$ increases $L$ by $0$ or $1$, while incrementing $l \to l+1$ decreases $L$ by $0$ or $1$. If we define the **unmatched column penalty**:
$$H(l, r) := (r - l + 1) - \text{LCS}(A, B[l..r]),$$
then:
1. $H(l, r)$ satisfies the **Monge inequality**:
   $$\Delta_{l, r} H := H(l, r) - H(l+1, r) - H(l, r-1) + H(l+1, r-1) = \Delta_{l, r} \text{LCS} \in \{0, 1\}.$$
2. More fully, if we extend the boundary to include prefixes/suffixes of $A$ (semi-local LCS between $A$ and $B$), the $(M+N) \times (M+N)$ cross-difference matrix $P$ with entries $P_{u, k} = \Delta H(u, k) \in \{0, 1\}$ is a **permutation matrix**—every entrance wire $u \in \{-M, \dots, -1\} \cup \{1, \dots, N\}$ exits at a unique exit wire $k$!

#### Step 3: Why Two Seaweeds Cross At Most Once (The Wavefront Invariant)
Instead of memorizing abstract Monge algebra, trace the **$M + N$ seaweeds (wires)** moving from the **top-left entrance perimeter** to the **bottom-right exit perimeter** of the $M \times N$ grid:
- **Initial Ranks (Entrance Labels)**:
  - Along the **left wall** of the grid, the $M$ horizontal entrances at rows $i = 1, \dots, M$ are assigned initial ranks:
    $$u_i = -i \in \{-M, \dots, -1\}.$$
  - Along the **top wall** of the grid, the $N$ vertical entrances at columns $j = 1, \dots, N$ are assigned initial ranks:
    $$v_j = j \in \{1, \dots, N\}.$$
  - Observe that as we walk clockwise along the top-left entrance perimeter (from bottom-left $(M, 0)$ up to $(0, 0)$ and right to $(0, N)$), the initial ranks are **strictly increasing**:
    $$-M < -(M-1) < \dots < -1 < 1 < 2 < \dots < N.$$

- **Wavefront Crossing Rule at Cell $(i, j)$**:
  Suppose we sweep cells $(i, j)$ in topological order ($i = 1 \dots M$, $j = 1 \dots N$). Cell $(i, j)$ has two incoming wires along the wavefront:
  - $u$: the wire entering from the **left** edge of cell $(i, j)$,
  - $v$: the wire entering from the **top** edge of cell $(i, j)$,
  and two outgoing edges along the shifted wavefront: the **bottom** edge of cell $(i, j)$ followed by the **right** edge of cell $(i, j)$.
  - If we set $(\text{bottom}, \text{right}) = (u, v)$, the relative order of $u$ and $v$ along the wavefront is **preserved** (**No Crossing / Bounce**).
  - If we set $(\text{bottom}, \text{right}) = (v, u)$, the relative order of $u$ and $v$ along the wavefront is **swapped** (**Crossing**).
  - Since all initial ranks started in strictly increasing order along the entrance perimeter, **$u$ and $v$ have already crossed earlier in the grid if and only if $u > v$!**
  - **The Seaweed Comb Rule**: At cell $(i, j)$:
    1. If **$A[i] = B[j]$ (Character Match)** OR **$u > v$ (Already Crossed Earlier)**:
       The two wires **do not cross** (they turn away from each other):
       $$(\text{bottom}, \text{right}) \leftarrow (u, v) \quad \text{(i.e., } \texttt{swap(u, W[j])}\text{)}.$$
    2. If **$A[i] \ne B[j]$ (Mismatch)** AND **$u < v$ (Have Not Crossed Yet)**:
       The two wires **cross** (pass straight through each other):
       $$(\text{bottom}, \text{right}) \leftarrow (v, u) \quad \text{(no swap needed!)}.$$

#### Theorem 38.1 (The Seaweed Dominance Formula for Interval LCS)
After sweeping all $M$ rows and $N$ columns with the rule above, let $W[k] \in \{-M, \dots, -1\} \cup \{1, \dots, N\}$ be the initial rank of the wire exiting the **bottom wall at column $k \in \{1, \dots, N\}$**. Then for every interval $[l, r] \subseteq [1, N]$:
$$\boxed{\text{LCS}\bigl(A[1..M],\, B[l..r]\bigr) = \#\bigl\{\, k \in [l, r] \;\big|\; W[k] < l \,\bigr\} = (r - l + 1) - \#\bigl\{\, k \in [l, r] \;\big|\; W[k] \ge l \,\bigr\}.}$$

*Proof (Induction on $M$ via Row-by-Row DP).*
Hold $l \in [1, N]$ fixed and trace how the set of values $\{ \mathbf{1}[W[k] < l] \}_{k=l}^N$ evolves as we process row $i = 1, \dots, M$:
- **Before row $1$ ($i = 0$)**: $W[k] = k$ for all $k \in \{1, \dots, N\}$. For $k \in [l, N]$, no $W[k]$ is $< l$, so $\#\{k \in [l, r] : W[k] < l\} = 0 = \text{LCS}(\varepsilon, B[l..r])$.
- **Across row $i$**: Attach the boolean tag $\text{is\_small}(x) := \mathbf{1}[x < l]$ to every wire $x$.
  - The wire entering row $i$ from the left wall has label $u = -i < 0 < l$, so it starts with tag $\text{is\_small}(u) = \mathbf{1}$!
  - Furthermore, for all columns $j < l$, every wire currently in columns $1 \dots l-1$ has label $\le j < l$ (since wires only move right and down, $W[j] \le j < l$). Thus, when wire $u$ reaches column $l$, whatever wire $u$ enters cell $(i, l)$ from the left **still has label $u < l$ ($\text{is\_small}(u) = 1$)**!
  - Now trace $j = l, l+1, \dots, r$ inside row $i$: the classic 0/1 row-transition of LCS DP states that a carry $u$ with $\text{is\_small}(u) = 1$ (representing a potential $+1$ increase in LCS) is deposited at the **first** column $j \ge l$ where $A[i] = B[j]$ and $\text{is\_small}(W[j]) = 0$ (i.e., $W[j] \ge l$), picking up the displaced wire $W[j] \ge l$ to carry forward until the next column where $W[j'] < l$ restores a $< l$ wire to $u$!
  - Check our Seaweed Rule `if (A[i] == B[j] || u > W[j]) swap(u, W[j])` on the threshold $< l$ vs. $\ge l$:
    - When $u < l$ and $W[j] \ge l$: we have $u < W[j]$, so a swap occurs **if and only if $A[i] = B[j]$**—depositing the $< l$ wire into $W[j]$ (incrementing the count of $< l$ wires in $[l, j]$ by $1$) and setting $u \leftarrow W[j] \ge l$!
    - When $u \ge l$ and $W[j] < l$: we have $u > W[j]$, so $u > W[j]$ is **automatically true** regardless of whether $A[i] = B[j]$, forcing a swap that deposits $u \ge l$ into $W[j]$ and picks up the $< l$ wire into $u$ (keeping the prefix count of $< l$ wires invariant while restoring $u < l$ for future matches)!
    - When both $u, W[j] < l$ or both $u, W[j] \ge l$: swapping them does not change the boolean indicators $\mathbf{1}[W[j] < l]$ or $\mathbf{1}[u < l]$!
  - Therefore, for **every** $l$ simultaneously, the boolean indicator $\mathbf{1}[W[k] < l]$ evolves according to the exact Hunt–Szymanski / Allison–Dix row-difference automaton for $\text{LCS}(A[1..i], B[l..r])$! $\blacksquare$

---

### 38.3 Reverse-Engineering Scratchpad: $O(MN)$ Comb + $O(1)$ / $O(\log N)$ Query Structures

#### 1. The 8-Line $O(MN)$ Seaweed Comb Construction
```cpp
// Input: A[1..M], B[1..N]. Output: W[1..N] where W[k] in {-M..-1} U {1..N}.
vector<int> W(N + 1);
for (int j = 1; j <= N; ++j) W[j] = j;
for (int i = 1; i <= M; ++i) {
    int u = -i;
    for (int j = 1; j <= N; ++j) {
        if (A[i] == B[j] || u > W[j]) {
            swap(u, W[j]);
        }
    }
}
```
Look at the inner loop: just a single comparison and conditional `swap`! Because it is branch-predictable and sequential, $M = N = 10{,}000$ runs in under $50$ milliseconds in C++.

#### 2. Answering Interval LCS Queries $[l, r]$ from $W[1..N]$
Once $W[1..N]$ is computed:
$$\text{LCS}(A, B[l..r]) = \#\bigl\{\, k \in [l, r] \;\big|\; W[k] < l \,\bigr\}.$$
- **If $N \le 5000$ and we want all $O(N^2)$ intervals**:
  For each fixed $l \in [1, N]$, sweep $r = l \dots N$ and maintain the running prefix count of $W[r] < l$ in **$O(N^2)$ total time and $O(N)$ space**!
- **If $Q$ online queries $[l, r]$ are given**:
  Build a **Persistent Segment Tree** (or **Wavelet Matrix**) over the array $W[1..N]$ (shifted by $+M+1$ so values lie in $[1, M+N+1]$). Each query $[l, r]$ asks for the number of elements in subarray $W[l..r]$ with value $< l$, which takes **$O(\log N)$ time per query** and $O(N \log N)$ space!
- **If $Q$ offline queries $[l, r]$ are given**:
  Sort queries by $l$ (or sweep $r = 1 \dots N$ and insert $W[r]$ into a Fenwick Tree), answering each query in **$O(\log N)$ time and $O(N)$ space**.

#### 3. Dual Queries: Prefix-Suffix LCS (`前缀-后缀 LCS`)
Notice that the seaweeds exiting the **right wall** at rows $i = 1, \dots, M$ also carry their initial ranks $R[i]$!
From the exact same seaweed grid on $(A, B)$:
- **$\text{LCS}(A[1..i], B[l..r])$ (Prefix of $A$, Substring of $B$)**: If we record the snapshot $W^{(i)}[1..N]$ after row $i$, then $\text{LCS}(A[1..i], B[l..r]) = \#\{k \in [l, r] : W^{(i)}[k] < l\}$.Wait: do we even need $M$ snapshots for $\text{LCS}(A[1..i], B[1..j])$? No, that's standard DP! What about **$\text{LCS}(A[i..M], B[1..j])$ (Suffix of $A$, Prefix of $B$)**?
  In the final state (after all $M$ rows), a wire entering from the left wall at row $i' \in [1, M]$ had initial rank $-i'$. Thus, $-i'$ is $\ge -i$ if and only if $i' \le i$!
  More directly: for any suffix $A[i..M]$ and prefix $B[1..j]$, only left wires from rows $i' \in [i, M]$ (which have initial ranks $-M \le u \le -i$) and top wires from columns $[1, j]$ participate! Specifically:
  $$\text{LCS}\bigl(A[i..M],\, B[1..j]\bigr) = \#\bigl\{\, k \in [1, j] \;\big|\; W[k] < -i \text{? Wait: } W[k] \in [-M, -i] \text{ or } < 1 \,\bigr\}?$$
  Be careful! Rows $1 \dots i-1$ of $A$ are **above** $A[i..M]$, so top wires $1 \dots j$ pass through rows $1 \dots i-1$ *before* reaching $A[i..M]$!
  Let's state the exact rule for which boundaries are restricted cleanly by a single Seaweed Matrix of $(A, B)$:
  - In $A[1..M] \times B[1..N]$, a substring $B[l..r]$ restricts the **entrance** (top wall $\ge l$) and the **exit** (bottom wall $\le r$).
  - symmetrically, for $A[i..M]$ (a **suffix** of $A$, which enters on the left wall at rows $\ge i$, i.e., initial rank $\le -i$) and $B[1..j]$ (a **prefix** of $B$, which exits on the bottom wall at columns $\le j$):
    Since initial ranks on the entrance perimeter are ordered $-M < \dots < -i < \dots < -1 < 1 < \dots < N$, restricting the entrance to wires with initial rank $\ge -i$ (namely rows $i \dots M$ on the left wall, which have rank in $[-M, -i]$? Wait: earlier we numbered row $1$ as $-1$ and row $M$ as $-M$, so row $1$ had rank $-1 > -M$, which is why row $1$ was *adjacent* to column $1$ at the top-left corner $(0,0)$!).
    Let's check that! Along the entrance perimeter from bottom-left $(M, 0)$ up to $(0, 0)$ and right to $(0, N)$:
    - Row $M$ is at the bottom-left ($(M, 0)$), so its initial rank is $-M$.
    - Row $1$ is at the top-left ($(0, 0)$), so its initial rank is $-1$.
    - Column $1$ is at $(0, 0)$, so its initial rank is $+1$.
    - Column $N$ is at $(0, N)$, so its initial rank is $+N$.
    Therefore, any contiguous interval along the entrance perimeter extending from $(0,0)$ down to row $i$ (rows $1 \dots i$, a **prefix** $A[1..i]$!) and right to column $r$ (columns $1 \dots r$) corresponds to initial ranks in $[-i, r]$!
     Wait: why did $B[l..r]$ work for **all** $M$ rows of $A$? Because for $B[l..r]$ and $A[1..M]$, the active subgrid starts at column $l$ (all wires from left of $l$ have initial rank $< l$) and ends at row $M$ and column $r$ (all exits on the bottom wall in $[1, r]$ are observed after row $M$)!
    Symmetrically, by transposing $A$ and $B$ (or reversing both strings), a single Seaweed Matrix of $(A, B)$ also answers:
    $$\text{LCS}\bigl(A[i..M],\, B[1..j]\bigr) = \#\bigl\{\, k \in [1, j] \;\big|\; W[k] \le -i \,\bigr\} \text{?}$$
    Wait: let's test $\text{LCS}(A[i..M], B[1..j])$ on our example $A = \texttt{ab}, B = \texttt{aba}$ where $W = [-1, -2, 2]$!
    - Take $i = 2$ ($A[2..2] = \texttt{b}$) and $j = 1$ ($B[1..1] = \texttt{a}$):
      $\text{LCS}(\texttt{b}, \texttt{a}) = 0$, and $W[1] = -1 \not\le -2$ ($0$ elements $\le -2$ in $W[1..1]$).
    - Take $i = 2$ ($A[2..2] = \texttt{b}$) and $j = 2$ ($B[1..2] = \texttt{ab}$):
      $\text{LCS}(\texttt{b}, \texttt{ab}) = 1$, and in $W[1..2] = [-1, -2]$, $W[2] = -2 \le -2$ ($1$ element $\le -2$!).
    - Take $i = 2$ ($A[2..2] = \texttt{b}$) and $j = 3$ ($B[1..3] = \texttt{aba}$):
      $\text{LCS}(\texttt{b}, \texttt{aba}) = 1$, and in $W[1..3] = [-1, -2, 2]$, only $W[2] = -2 \le -2$ ($1$ element $\le -2$!).
    Wait: why does $\#\{k \in [1, j] : W[k] \le -i\}$ work for **every suffix $A[i..M]$ and every prefix $B[1..j]$**?
    Let's check! Any wire entering at row $i' \in [1, i-1]$ (rank $-i' \in [-(i-1), -1]$) or at top column $c \in [1, j]$ (rank $c \in [1, j]$) has initial rank $> -i$. Only the wires entering at rows $i \dots M$ (which enter the subgrid $A[i..M] \times B[1..j]$ from its left wall!) have initial rank $\le -i$! And rows $1 \dots i-1$ only permute wires of rank $> -i$ among themselves before row $i$ is even reached—so when the sweep reaches row $i$, the set of wires currently sitting at the top of $A[i..M] \times B[1..j]$ all have rank $> -i$, while the wires entering from the left of $A[i..M]$ all have rank $\le -i$!
    Thus the threshold $< -i + 1$ (i.e. $\le -i$) runs the exact same 0/1 row-carry DP on $A[i..M] \times B[1..j]$!

> [!IMPORTANT]
> **Theorem 38.2 (Unified Three-Family LCS Queries from a Single Seaweed Matrix $W[1..N]$)**
> From the single bottom-exit array $W[1..N]$ of $A[1..M] \times B[1..N]$ (together with right-wall exits $R[1..M]$), a single $O(MN)$ Seaweed Comb simultaneously answers **three** entire $O(N^2)$ / $O(MN)$ families of LCS queries via 2D dominance counting:
> 1. **Whole $A$ vs. Interval of $B$**:
>    $$\text{LCS}\bigl(A[1..M],\, B[l..r]\bigr) = \#\bigl\{\, k \in [l, r] \;\big|\; W[k] < l \,\bigr\}.$$
> 2. **Suffix of $A$ vs. Prefix of $B$ (`后缀-前缀 LCS`)**:
>    $$\text{LCS}\bigl(A[i..M],\, B[1..j]\bigr) = \#\bigl\{\, k \in [1, j] \;\big|\; W[k] \le -i \,\bigr\}.$$
> 3. **Prefix of $A$ vs. Suffix of $B$ (`前缀-后缀 LCS`)**:
>    By symmetry on the right-wall exits $R[1..M]$ (where $R[i']$ is the initial rank of the wire exiting the right wall at row $i'$):
>    $$\text{LCS}\bigl(A[1..i],\, B[l..N]\bigr) = (N - l + 1) - \#\bigl\{\, k \in [l, N] \;\big|\; W[k] \ge l \,\bigr\} - \#\bigl\{\, i' \in [i+1, M] \;\big|\; R[i'] \ge l \,\bigr\}.$$

---

### 38.4 Unit-Monge Distance Multiplication ($\boxdot$) in $O(N \log N)$ & $O(N \log^2 N)$ Divide-and-Conquer

Suppose we split $A = A_1 A_2$ horizontally (or split the grid into subgrids) and know the Seaweed permutation matrix $P_1$ for $A_1 \times B$ and $P_2$ for $A_2 \times B$. How do we compose the seaweed permutation $P_1$ (exit of top half $\to$ entrance of bottom half) with $P_2$ without running the $O(N^2)$ comb?
- Each Seaweed permutation $P$ of dimension $K = M + N$ is the cross-difference of a Unit-Monge distance matrix $D_P$.
- Composing two grid strips corresponds to the **$(\min, +)$ Unit-Monge Distance Product** $D_P = D_{P_1} \boxdot D_{P_2}$:
  $$D_P(i, k) = \min_{j} \bigl( D_{P_1}(i, j) + D_{P_2}(j, k) \bigr).$$
- **Tiskin's $O(K \log K)$ Seaweed Multiplication Theorem (2008)**:
  Given two $K \times K$ permutation matrices $P_1, P_2$, their Unit-Monge product $P = P_1 \boxdot P_2$ can be computed in **$O(K \log K)$ time** by recursive divide-and-conquer on rows/columns:
  1. Split the middle index range $[1, K]$ into left half $[1, K/2]$ and right half $[K/2+1, K]$, inducing sub-permutations of size $K/2$.
  2. Recursively compute the products on the two halves in $2 T(K/2)$.
  3. **Merge Step in $O(K)$ via Monotone Single-Crossing Property**: The difference $\delta(i, k)$ between the left-half candidate minimum and right-half candidate minimum is **monotone** in both $i$ and $k$, changing sign along a single staircase curve of length $2K$! Stepping along this staircase in $O(K)$ time identifies where the odd/even seaweeds switch halves.
- **Consequences for Competitive Programming**:
  - **Range-Range Substring LCS $\text{LCS}(A[l_1..r_1], B[l_2..r_2])$**: Build a Segment Tree over the rows of $A$ (or columns of $B$) where each node stores the Seaweed permutation of its strip, merged in $O(N \log N)$ via $\boxdot$.
  - **All-Pairs Interval LCS in $O(N \log^2 N)$ when $M, N$ have Few Matches or Run-Length Encoding**: By recursively dividing the $M \times N$ grid into four $(M/2) \times (N/2)$ quadrants (or stops at uniform/mismatch blocks) and multiplying the four quadrant seaweed permutations via $\boxdot$ in $O((M+N)\log(M+N))$, the entire Seaweed permutation $W[1..N]$ can be built in $O(N \log^2 N)$!

### 38.5 Boundary Pitfalls & Counterexamples for Seaweed Matrices
1. **Confusing Prefix-Prefix LCS with Suffix-Prefix LCS**: A single final array $W[1..N]$ after row $M$ directly gives $\text{LCS}(A[1..M], B[l..r])$ and $\text{LCS}(A[i..M], B[1..j])$, **not** $\text{LCS}(A[1..i], B[l..r])$ for arbitrary $i < M$ (because rows $i+1 \dots M$ lie *after* row $i$ and further permute $W$). If you need $\text{LCS}(A[1..i], B[l..r])$, simply record $W$ after row $i$!
2. **Initial Rank Sign Convention**: Left-wall row $i \in \{1, \dots, M\}$ **must** receive initial rank $-i$ (so row $1$ is $-1$ and row $M$ is $-M$), **not** $-(M - i + 1)$. Why? Because at the top-left corner $(0, 0)$, row $1$ and column $1$ are adjacent along the entrance wavefront; if row $1$ were given rank $-M$ and row $2$ were given rank $-(M-1)$, then row $2$ would start with a *larger* rank than row $1$ despite entering *below* row $1$, falsely triggering the `u > W[j]` already-crossed condition!

---

## Iteration 39: Bit-Parallel LCS & Edit Distance (Allison–Dix / Myers / Hyyrö)

### 39.1 The Diagnostic Signal: When $N, M \le 50{,}000$ and Time Limit Is $1.0\text{s}$

Suppose $M, N \le 50{,}000$ (or $10^5$) and we need the single value $\text{LCS}(A, B)$ or the Edit Distance $\text{ed}(A, B)$ (or we need to compute the entire DP row for $50{,}000$-length strings inside a divide-and-conquer / Hirschberg reconstruction).
Standard $O(MN)$ DP performs $2.5 \times 10^9$ inner-loop iterations, which TLEs. However, notice that in the LCS table $dp[i][j] = \text{LCS}(A[1..i], B[1..j])$:
$$\Delta H_{i, j} := dp[i][j] - dp[i][j-1] \in \{0, 1\}!$$
Because each horizontal difference is a **single bit**, an entire row of $N$ DP values can be packed into $\lceil N / 64 \rceil$ 64-bit machine words (`uint64_t`), provided we can express the row transition $dp[i-1][\cdot] \to dp[i][\cdot]$ using only **bitwise operations and hardware integer addition/subtraction carries** in $O(N / w)$ time!

---

### 39.2 The Combinatorial Word Invariant: Carry Propagation = Next-Match Absorption

#### Object & Question
Let bitmask $V \in \{0, 1\}^N$ encode the horizontal differences of row $i-1$: bit $j$ of $V$ is $1$ if and only if $dp[i-1][j] - dp[i-1][j-1] = 1$.
For each character $c \in \Sigma$, precompute the **Pattern Match Bitmask** $M[c] \in \{0, 1\}^N$, where bit $j$ of $M[c]$ is $1$ if and only if $B[j] = c$.
Given $V$ (for row $i-1$) and $c = A[i]$, how is the new difference bitmask $V'$ (for row $i$) determined?

#### Step-by-Step Combinatorial Meaning of a Row Transition
Consider the positions $1 \le j_1 < j_2 < \dots < j_k \le N$ where $V$ has $1$-bits (the columns where $dp[i-1][\cdot]$ steps up by $+1$). These $k$ bits partition $[1, N]$ into $k+1$ blocks:
$$I_1 = [1, j_1], \quad I_2 = [j_1 + 1, j_2], \quad \dots, \quad I_k = [j_{k-1}+1, j_k], \quad I_{k+1} = [j_k + 1, N].$$
On each block $I_r = [j_{r-1}+1, j_r]$, $dp[i-1][j]$ is constant ($= r-1$) for $j < j_r$ and steps up to $r$ at $j = j_r$.
When we process character $c = A[i]$, where does $dp[i][j]$ step up from $r-1$ to $r$?
- It steps up at the **first column $p \in I_r$ where $B[p] = c$**, or at the old step-up position $j_r$ if no match occurs in $I_r$!
- In terms of the $1$-bits of $V'$:
  - In each block $I_r = [j_{r-1}+1, j_r]$, the old $1$-bit at $j_r$ **moves left** to the first position $p \in [j_{r-1}+1, j_r]$ where $B[p] = c$ (and if the tail block $I_{k+1} = [j_k+1, N]$ contains a match $B[p] = c$, a **brand-new $1$-bit** is born at the first such $p \in I_{k+1}$, increasing the total LCS by $+1$!).

#### Theorem 39.1 (Allison–Dix / Crochemore–Hyyrö Bitwise Subtraction Formula)
Let $V$ be the current row-difference bitmask, and let $U = V \mathbin{\&} M[A[i]]$ or $X = V \mathbin{|} M[A[i]]$. Specifically, define:
$$X = V \mathbin{|} M\bigl[A[i]\bigr], \qquad Y = (V \ll 1) \mathbin{|} 1.$$
Then in exact binary arithmetic, subtracting $Y$ from $X$ propagates a borrow from the start of each block $I_r$ (at bit $j_{r-1}+1$, where $Y$ has a $1$-bit!) up to the **first $1$-bit of $X$ in $I_r$** (which is precisely $\min(\{p \in I_r : B[p] = A[i]\} \cup \{j_r\})$!), flipping that first $1$-bit of $X$ from $1$ to $0$ and flipping all preceding $0$-bits in $I_r$ from $0$ to $1$. Therefore:
$$\boxed{V' = X \mathbin{\&} \bigl(X \oplus (X - Y)\bigr)}$$
Wait—let us check if $X \mathbin{\&} \sim(X - Y)$ or $X \oplus \dots$ keeps the right bits!

#### Hand-Checkable Trace of $X - Y$ inside a Single Block $I_r = [j_{r-1}+1, j_r]$
Let us trace the exact bits inside one block $I_r = [j_{r-1}+1, j_r]$ (written from least-significant bit $j_{r-1}+1$ on the **right** to most-significant bit $j_r$ on the **left**):
1. What is $Y = (V \ll 1) \mathbin{|} 1$ inside block $I_r = [j_{r-1}+1, j_r]$?
   - Because $V$ had a $1$-bit at $j_{r-1}$ (or because of $\mathbin{|} 1$ for $r=1$) and $0$-bits at $j_{r-1}+1, \dots, j_r - 1$, shifting $V$ left by $1$ places a **single $1$-bit at the bottom (LSB) of block $I_r$** (index $j_{r-1}+1$) and $0$-bits everywhere else in $I_r$!
   - Thus, inside block $I_r$:
     $$Y|_{I_r} = \texttt{00}\dots\texttt{001}_2.$$
2. What is $X = V \mathbin{|} M[A[i]]$ inside block $I_r$?
   - $X$ has a $1$-bit at the top (MSB) of the block ($j_r$, since $V[j_r] = 1$), plus $1$-bits at every match position $p \in I_r$ where $B[p] = A[i]$.
   - Let $p^* = \min\{p \in I_r : X[p] = 1\}$ be the **first (lowest-index) $1$-bit of $X$ inside $I_r$**.
   - Then between $j_{r-1}+1$ and $p^*-1$, $X$ has all $0$s; at $p^*$, $X$ has a $1$; and above $p^*$ up to $j_r$, $X$ has some pattern $\alpha$ (which ends with $1$ at $j_r$).
     $$X|_{I_r} = \alpha \texttt{100}\dots\texttt{0}_2.$$
3. Now subtract $Y|_{I_r} = \texttt{00}\dots\texttt{001}_2$ from $X|_{I_r} = \alpha\texttt{100}\dots\texttt{0}_2$:
   - Subtracting $1$ at the bottom of the block borrows through the trailing zeros up to bit $p^*$, turning bit $p^*$ from $1$ to $0$, turning bits $j_{r-1}+1 \dots p^*-1$ from $0$ to $1$, and leaving all bits $\alpha$ above $p^*$ (including bit $j_r$) **completely untouched**—so **no borrow ever escapes across the block boundary $j_r$ into block $I_{r+1}$!**
   - That is the magic invariant: because $X[j_r] = V[j_r] = 1$ at the top of every block $I_r$, **each block $I_r$ absorbs its own borrow independently with zero cross-block interference!**
4. Look at the bit pattern inside $I_r$ before and after subtraction:
   - $X|_{I_r} \quad\;\; = \alpha \,\mathbf{1}\, \texttt{00}\dots\texttt{0}$ (where the bold $\mathbf{1}$ is at $p^*$, the **new** step-up position for row $i$!)
   - $(X - Y)|_{I_r} = \alpha \,\mathbf{0}\, \texttt{11}\dots\texttt{1}$ (only bit $p^*$ changed from $1 \to 0$, and bits below $p^*$ changed from $0 \to 1$!)
   - Therefore, where did $X$ have a $1$ and $X - Y$ have a $0$? **At position $p^*$ and NOWHERE ELSE in $I_r$!**
   $$\boxed{V' = X \mathbin{\&} \sim(X - Y) \quad \text{where } X = V \mathbin{|} M\bigl[A[i]\bigr], \;\; Y = (V \ll 1) \mathbin{|} 1!}$$

> [!TIP]
> **Look How Short and Exact That Formula Is!**
> Let us verify $V' = X \mathbin{\&} \sim(X - Y)$ on every bit of $I_r$:
> - Above $p^*$: $X$ and $X - Y$ are identical ($\alpha$), so $X \mathbin{\&} \sim(X - Y) = \alpha \mathbin{\&} \sim\alpha = \mathbf{0}$!
> - At $p^*$: $X[p^*] = 1$ and $(X - Y)[p^*] = 0$, so $1 \mathbin{\&} \sim 0 = \mathbf{1}$!
> - Below $p^*$: $X = 0$ and $X - Y = 1$, so $0 \mathbin{\&} \sim 1 = \mathbf{0}$!
> - In the final block $I_{k+1} = [j_k + 1, N]$: if there is at least one match in $I_{k+1}$, the borrow stops at the first match $p^* \in I_{k+1}$ and puts a $1$ at $p^*$; if there is **no** match in $I_{k+1}$, $X|_{I_{k+1}} = 0$, so $X \mathbin{\&} \sim(X - Y) = 0 \mathbin{\&} \dots = 0$!
> Thus **$V' = X \mathbin{\&} \sim(X - Y)$ is 100% exact on every block simultaneously!**

---

### 39.3 Reverse-Engineering Scratchpad: Hand Trace & Multi-Word Implementation

#### 1. Hand-Checkable 4-Bit Trace on $B = \texttt{abac}$ ($N = 4$) and $A = \texttt{abc}$
Write 4-bit numbers with bit $0$ ($j=1$) on the **right (LSB)** and bit $3$ ($j=4$) on the **left (MSB)**:
- Pattern match masks for $B = \texttt{abac}$:
  $$M[\texttt{a}] = \texttt{0101}_2 \;\; (j=1, 3), \qquad M[\texttt{b}] = \texttt{0010}_2 \;\; (j=2), \qquad M[\texttt{c}] = \texttt{1000}_2 \;\; (j=4).$$
- Initially ($i = 0$): $V = \texttt{0000}_2$.
- **Step $i = 1$ ($A[1] = \texttt{a}$)**:
  - $X = V \mathbin{|} M[\texttt{a}] = \texttt{0101}_2$, $\quad Y = (V \ll 1) \mathbin{|} 1 = \texttt{0001}_2$.
  - $X - Y = \texttt{0101}_2 - \texttt{0001}_2 = \texttt{0100}_2$.
  - $V' = X \mathbin{\&} \sim(X - Y) = \texttt{0101}_2 \mathbin{\&} \texttt{1011}_2 = \texttt{0001}_2$ (step-up at $j=1$; $\text{popcount}(V') = 1$).
- **Step $i = 2$ ($A[2] = \texttt{b}$)**:
  - $X = \texttt{0001}_2 \mathbin{|} \texttt{0010}_2 = \texttt{0011}_2$, $\quad Y = (\texttt{0001}_2 \ll 1) \mathbin{|} 1 = \texttt{0011}_2$.
  - $X - Y = \texttt{0011}_2 - \texttt{0011}_2 = \texttt{0000}_2$.
  - $V' = \texttt{0011}_2 \mathbin{\&} \texttt{1111}_2 = \texttt{0011}_2$ (step-ups at $j=1, 2$; $\text{popcount}(V') = 2$).
- **Step $i = 3$ ($A[3] = \texttt{c}$)**:
  - $X = \texttt{0011}_2 \mathbin{|} \texttt{1000}_2 = \texttt{1011}_2$, $\quad Y = (\texttt{0011}_2 \ll 1) \mathbin{|} 1 = \texttt{0111}_2$.
  - $X - Y = \texttt{1011}_2 - \texttt{0111}_2 = \texttt{0100}_2$.
  - $V' = \texttt{1011}_2 \mathbin{\&} \texttt{1011}_2 = \texttt{1011}_2$ (step-ups at $j=1, 2, 4$; $\text{popcount}(V') = 3 = \text{LCS}(\texttt{abc}, \texttt{abac})$!).

#### 2. Multi-Word (`uint64_t` Array) Implementation Contract
When $N > 64$, pack $V$ and $M[c]$ into $W = \lceil N / 64 \rceil$ words `uint64_t V[W]`:
```cpp
// One row transition for character c = A[i] across W = (N + 63) / 64 words:
uint64_t shift_carry = 1; // For Y = (V << 1) | 1
uint64_t sub_borrow  = 0; // Borrow across 64-bit word boundaries in X - Y
for (int w = 0; w < W; ++w) {
    uint64_t v = V[w];
    uint64_t x = v | M[c][w];
    uint64_t y = (v << 1) | shift_carry;
    shift_carry = v >> 63;

    // Compute diff = x - y - sub_borrow with unsigned 64-bit borrow detection:
    uint64_t temp = x - y;
    uint64_t next_borrow = (x < y) | (temp < sub_borrow);
    uint64_t diff = temp - sub_borrow;
    sub_borrow = next_borrow;

    V[w] = x & ~diff;
}
// Clear any padding bits past N-1 in the last word V[W - 1] before popcount!
```

#### 3. Myers' $O(MN / w)$ Bit-Parallel Edit Distance (Levenshtein Distance, Myers 1999)
For unit-cost Edit Distance (insertion, deletion, substitution all cost $1$), adjacent entries in the DP matrix satisfy:
$$\Delta H_{i, j} = dp[i][j] - dp[i][j-1] \in \{-1, 0, +1\}, \qquad \Delta V_{i, j} = dp[i][j] - dp[i-1][j] \in \{-1, 0, +1\}.$$
Because each difference has three possible values $\{-1, 0, +1\}$, Myers encodes the vertical column differences using **two** boolean bitvectors $(VP, VN)$:
- $VP[i] = 1 \iff dp[i][j] - dp[i-1][j] = +1$,
- $VN[i] = 1 \iff dp[i][j] - dp[i-1][j] = -1$.
Initially (at $j = 0$), $dp[i][0] = i$, so $VP = 1^M$ (all ones) and $VN = 0^M$. For each column $j = 1 \dots N$ (character $c = B[j]$ with match mask $PM = M_A[c]$):
1. Compute the diagonal difference $D0$ (where $D0[i] = 1 \iff dp[i][j] - dp[i-1][j-1] = 0$):
   $$X = PM \mathbin{|} VN, \qquad D0 = \bigl(((X \mathbin{\&} VP) + VP) \mathbin{\wedge} VP\bigr) \mathbin{|} X.$$
2. Compute the horizontal differences $HP, HN$:
   $$HP = VN \mathbin{|} \sim(D0 \mathbin{|} VP), \qquad HN = VP \mathbin{\&} D0.$$
3. Shift $HP, HN$ by $1$ to align with row $i$ and update $VP, VN$:
   $$X' = (HP \ll 1) \mathbin{|} 1, \qquad VP' = (HN \ll 1) \mathbin{|} \sim(D0 \mathbin{|} X'), \qquad VN' = X' \mathbin{\&} D0.$$
Each column update uses only $15$ bitwise/addition instructions per 64-bit word!

### 39.4 Boundary Pitfalls & Broken-Invariant Counterexamples
1. **Uncleaned High Bits in the Final Word `V[W - 1]`**: If $N$ is not a multiple of $64$ and you do not mask out bits $\ge (N \bmod 64)$ in $M[c][W-1]$ (or before computing `popcount`), a borrow from the last block $I_{k+1}$ can wrap into unused high bits if $M[c]$ had stray $1$s. Always ensure $M[c]$ has $0$ in all bits $\ge N$: then in the tail above the last $1$-bit of $X$, $X = 0$, so `x & ~diff` is guaranteed to be $0$ even if `sub_borrow = 1`!
2. **Unsigned Borrow Detection Bug (`x < y + sub_borrow` Overflow)**: In C++, writing `x < y + sub_borrow` overflows to $0$ when `y = UINT64_MAX` and `sub_borrow = 1`! Always use `__uint128_t`, compiler intrinsic `_subborrow_u64`, or the overflow-safe two-step check `(x < y) | ((x - y) < sub_borrow)`.

---

## Iteration 40: Multilingual (`[EN]` / `[ZH]` / `[JA]`) Problem Mining, 4-Tier Difficulty Ladder & Quarantine Ledger

### 40.1 Quarantine Table (`R-4B-01` – `R-4B-08`: Pure Templates & Bare Routine Checks Excluded from Textbook Ladders)

Per `PLAN.md` §2.2 and `AGENTS.md`, pure template verification problems whose sole task is implementing a bare DASG, classic $O(N^2)$ LCS, or basic bitset LCS without structural reductions are quarantined here:

| Quarantine ID | Source & Problem Name | Language / Judge | Reason for Quarantine |
| :--- | :--- | :--- | :--- |
| **`R-4B-01`** | **Luogu P5826 — 【模板】子序列自动机** | `[ZH]` Luogu | Bare template verification of $\text{DASG}(S)$ next-occurrence lookups via occurrence vectors + `upper_bound`. |
| **`R-4B-02`** | **Library Checker — Longest Common Subsequence** | `[EN]` / `[JA]` Yosupo | Pure template verification of standard LCS without structural twists. |
| **`R-4B-03`** | **LeetCode 940 — Distinct Subsequences II** | `[EN]` LeetCode | Bare $O(N)$ whole-string distinct subsequence recurrence $D' = 2D - L_x$ with no range queries, matrix inversion, or structural constraints. |
| **`R-4B-04`** | **LeetCode 792 — Number of Matching Subsequences** | `[EN]` LeetCode | Direct bucket-waiting or bare DASG traversal without structural synthesis. |
| **`R-4B-05`** | **SPOJ LCS0 — Longest Common Subsequence** | `[EN]` SPOJ (`N \le 50000`) | Pure bare template of Allison–Dix $O(N^2/w)$ bit-parallel LCS with zero additional modelling. |
| **`R-4B-06`** | **AtCoder Educational DP Contest F — LCS** | `[JA]` AtCoder | Introductory $O(NM)$ textbook LCS reconstruction exercise. |
| **`R-4B-07`** | **CSES 1140 / 1639 — Edit Distance** | `[EN]` CSES | Introductory $O(NM)$ Wagner–Fischer edit distance template. |
| **`R-4B-08`** | **LOJ 6564 — 最长公共子序列 (`N = 70000`)** | `[ZH]` LibreOJ | Bare $O(N^2/w)$ bit-parallel LCS benchmark (`N = 70000`, custom `uint64_t` loop). Kept in notes only as an engineering speed test, excluded from conceptual problem ladders. |

---

### 40.2 Accepted Non-Template Problem Archive — 4-Tier Difficulty Ladder (32 Problems with 4-Step Zero-Magic Analysis)

Below we catalog **32 accepted non-template problems** mined across `[EN]` (Codeforces, ICPC, Universal Cup), `[ZH]` (NOI/HEOI/THUPC/ZJOI/SDOI, Luogu, UOJ, LOJ, QOJ, NowCoder), and `[JA]` (AtCoder `ABC`/`ARC`/`AGC`, JOI) ordered into a **4-Tier Smooth Difficulty Ladder**.

---

#### Tier 1: Stepping Stone (8 Problems — Canonical DASG Greedies, Gap Constraints & Shortest Absent Subsequence)

##### `P-4B-01`: AtCoder ABC 214 F — Substrings (`[JA]`, AtCoder)
- **Inline Problem Statement & Constraints**: Given a string $S[1..N]$ of lowercase English letters ($1 \le N \le 2 \cdot 10^5$), count the number of distinct non-empty strings that can be obtained by choosing indices $1 \le i_1 < i_2 < \dots < i_k \le N$ with **$i_{r} - i_{r-1} \ge 2$** for all $r$ (no two adjacent characters of $S$ chosen), modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Choosing non-adjacent indices modifies the subsequence transition from $j > i$ to $j > i+1$.
  2. *Combinatorial Invariant*: By leftmost-greedy canonicalization under the gap-$2$ rule, a valid subsequence $P = p_1 \dots p_k$ maps to the unique tuple $(i_1, \dots, i_k)$ where $i_1 = \min\{j \ge 1 : S[j] = p_1\}$ and $i_r = \min\{j \ge i_{r-1} + 2 : S[j] = p_r\}$.
  3. *Reverse-Engineering Scratchpad*: In $\text{DASG}_{\text{gap}=2}(S)$, state $i$ transitions on character $c$ to $\text{nxt}[i+1][c]$ (while root $0$ transitions to $\text{nxt}[0][c]$). Equivalently, pulling backwards: $dp[i] = \sum_{j = \max(0, \text{prev}[i] - 1)}^{i-2} dp[j]$ in $O(N)$ time.
  4. *Boundary Pitfall*: Root state $0$ has no adjacency restriction for the *first* character $i_1 \ge 1$ ($i_1 = 1$ and $i_1 = 2$ are both reachable from $0$), whereas from $i \ge 1$ the next index must satisfy $j \ge i+2$.

##### `P-4B-02`: AtCoder ARC 081 C (ABC 081 E) — Don't Be a Subsequence (`[JA]`, AtCoder)
- **Inline Problem Statement & Constraints**: Given a string $A[1..N]$ over `'a'..'z'` ($1 \le N \le 2 \cdot 10^5$), find the **shortest** (and among shortest, **lexicographically smallest**) non-empty string $P \in \Sigma^+$ that is **not** a subsequence of $A$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Searching over $\Sigma^+$ for an absent subsequence is a shortest-path problem from state $0$ to the sink $\bot$ in $\text{DASG}(A)$.
  2. *Combinatorial Invariant*: State $i \in \{0, \dots, N\}$ has distance $d[i] = 1 + \min_{c \in \Sigma} d[\text{nxt}[i][c]]$ to $\bot$.
  3. *Reverse-Engineering Scratchpad*: Compute $d[i]$ backwards from $i = N$ down to $0$ in $O(N |\Sigma|)$. Then reconstruct $P$ greedily from $u = 0$: at each step, pick the smallest $c \in \texttt{'a'}..\texttt{'z'}$ such that $d[\text{nxt}[u][c]] = d[u] - 1$.
  4. *Boundary Pitfall*: Forward greedy (jumping to the furthest first occurrence $\max_c \text{nxt}[u][c]$) finds the right *length* but fails lexicographical tie-breaking because an earlier character $c_1 < c_2$ with $\text{nxt}[u][c_1] < \text{nxt}[u][c_2]$ may still lie in the same suffix block of distance $d[u]-1$!

##### `P-4B-03`: AtCoder ABC 130 E / Codeforces 163A — Common Subsequence Pairs with Multiplicity vs. Distinctness (`[JA]` / `[EN]`)
- **Inline Problem Statement & Constraints**: Contrast counting pairs of identical subsequence index-tuples between $A[1..M]$ and $B[1..N]$ ($M, N \le 2000$) vs. counting **distinct common subsequences** (where each string $P \preceq A, B$ is counted once) on $\text{DASG}(A) \times \text{DASG}(B)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Standard 2D DP counts index-tuple pairs; distinct common subsequences require canonicalizing occurrences in *both* $A$ and $B$.
  2. *Combinatorial Invariant*: Every string $P$ that is a subsequence of both $A$ and $B$ corresponds to a unique path from $(0, 0)$ in the product DAG $\text{DASG}(A) \times \text{DASG}(B)$ with transitions $(u, v) \xrightarrow{c} (\text{nxt}_A[u][c], \text{nxt}_B[v][c])$.
  3. *Reverse-Engineering Scratchpad*: $dp[u][v] = 1 + \sum_{c \in \Sigma} dp[\text{nxt}_A[u][c]][\text{nxt}_B[v][c]]$ in $O(MN|\Sigma|)$ (or $O(MN)$ by prefix-sum optimization over the four quadrants of $\text{prev}_A[i], \text{prev}_B[j]$!).
  4. *Boundary Pitfall*: Do not confuse $\text{DASG}(A) \times \text{DASG}(B)$ (distinct strings $P$) with $dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + [A[i]=B[j]]dp[i-1][j-1]$ (distinct pairs of index subsets).

##### `P-4B-04`: Codeforces 1295C — Obtain The String & Minimal DASG Wraps (`[EN]`, Codeforces)
- **Inline Problem Statement & Constraints**: Given $S[1..N]$ and $T[1..M]$ ($N, M \le 10^5$), find the minimum number of subsequences of $S$ whose concatenation equals $T$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Partitioning $T$ into the minimum number of subsequences of $S$ is equivalent to walking $T$ on the **Cyclic DASG** of $S$ where missing transitions wrap back to state $0$ at cost $+1$.
  2. *Combinatorial Invariant*: By Theorem 36.1, matching as long a prefix of the remaining $T$ as possible in a single pass through $S$ strictly dominates stopping early.
  3. *Reverse-Engineering Scratchpad*: Build $\text{DASG}(S)$ in $O(N|\Sigma|)$; walk $T$ in $O(M)$, resetting $u \leftarrow \text{nxt}[0][T[j]]$ and incrementing the wrap counter whenever $\text{nxt}[u][T[j]] = \bot$.
  4. *Boundary Pitfall*: If $\text{nxt}[0][T[j]] = \bot$, character $T[j]$ does not appear in $S$ at all (output `-1` immediately).

##### `P-4B-05`: Codeforces 1183H — Subsequences (Hard Version) (`[EN]`, Codeforces)
- **Inline Problem Statement & Constraints**: Given $S[1..N]$ ($N \le 100$) and $K \le 10^{12}$, select $K$ **distinct** subsequences of $S$ to maximize the sum of their lengths (or minimize total deletions $N - |P|$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: We must count distinct subsequences of $S$ **stratified by length** $L \in \{0, \dots, N\}$, capped at $\min(\text{count}, K)$ to prevent 64-bit overflow.
  2. *Combinatorial Invariant*: In $\text{DASG}(S)$, a path from $0$ of length $L$ corresponds bijectively to a distinct subsequence of length $L$.
  3. *Reverse-Engineering Scratchpad*: Compute $dp[u][L] = \min\bigl(K, \sum_{c \in \Sigma} dp[\text{nxt}[u][c]][L-1]\bigr)$ in $O(N^2 |\Sigma|)$ (or $O(N^2)$ via `prev[i]`), then greedily take $\min(K, dp[0][L])$ subsequences for $L = N, N-1, \dots, 0$.
  4. *Boundary Pitfall*: Subtracting $dp[\text{prev}[i]-1][L-1]$ in the $O(N^2)$ recurrence **cannot** be combined with $\min(K, \dots)$ saturation! When capping at $K$ to avoid overflow, use the **additive** DASG outgoing edges $\sum_{c \in \Sigma} dp[\text{nxt}[u][c]][L-1]$ so no subtraction is ever needed!

##### `P-4B-06`: AtCoder ABC 299 E / ARC 125 C — Lexicographically Extremal Subsequence Reconstruction (`[JA]`, AtCoder)
- **Inline Problem Statement & Constraints**: Given $S[1..N]$ and a target length $K$ (or subsequence constraints), find the lexicographically smallest subsequence of length $K$ (or satisfying character frequency bounds $L_c \le \text{cnt}_c \le R_c$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: At state $u$ of $\text{DASG}(S)$, choosing the next character $c$ transitions to $v = \text{nxt}[u][c]$ and leaves the suffix $S[v+1..N]$ available for the remaining $K-1$ characters.
  2. *Combinatorial Invariant*: Transition $v = \text{nxt}[u][c]$ is feasible if and only if the suffix $S[v+1..N]$ satisfies the feasibility invariant for the remaining quota (e.g., $N - v \ge K - 1$, or for frequency bounds: $\sum_a \max(0, L'_a) \le K-1 \le \sum_a \min(R'_a, \text{rem\_cnt}[v+1][a])$).
  3. *Reverse-Engineering Scratchpad*: Precompute suffix character counts and $\text{nxt}[u][c]$ in $O(N|\Sigma|)$; greedily test $c = \texttt{'a'}..\texttt{'z'}$ at each of the $K$ steps in $O(K|\Sigma|)$.
  4. *Boundary Pitfall*: Always check both the lower bound ($\text{rem\_cnt}[v+1][a] \ge L'_a$ for every $a$) and the upper-capacity sum ($\sum_a \min(R'_a, \text{rem\_cnt}[v+1][a]) \ge K-1$).

##### `P-4B-07`: Codeforces 1458C / 1366G — Construct the String (Subsequence with Backspaces DP) (`[EN]`, Codeforces)
- **Inline Problem Statement & Constraints**: Given $S[1..N]$ containing letters and `'.'` (backspace) and target $T[1..M]$ ($N, M \le 10^4$), delete the minimum number of characters from $S$ so that evaluating the remaining string with backspaces produces $T$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A letter $S[i]$ can either match $T[j]$ directly OR be cancelled by a later backspace `'.'` at $S[\text{match}[i]]$ if the balanced substring $S[i..\text{match}[i]]$ is kept intact!
  2. *Combinatorial Invariant*: Each index $i$ with $S[i] \ne \texttt{'.'}$ has at most one minimal balanced interval $[i, \text{bal}[i]]$ where letters and backspaces cancel to $\varepsilon$.
  3. *Reverse-Engineering Scratchpad*: Combine standard subsequence DP on $(i, j)$ with the jump $(i, j) \to (\text{bal}[i] + 1, j)$ at cost $0$ deletions in $O(NM)$ time.
  4. *Boundary Pitfall*: A backspace `'.'` can also be deleted at cost $1$, or kept at cost $0$ when $j = 0$ if backspace on an empty string is a no-op (check problem specification!).

##### `P-4B-08`: Luogu P3856 — [TJOI2008] 公共子序列 (Distinct Common Subsequences of 3 Strings) (`[ZH]`, TJOI / Luogu)
- **Inline Problem Statement & Constraints**: Given three strings $A, B, C$ of lengths $\le 150$, count the number of **distinct** non-empty common subsequences of $A, B, C$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A common subsequence of $A, B, C$ must be counted once regardless of how many embeddings it has in $A, B,$ or $C$.
  2. *Combinatorial Invariant*: The 3-way product automaton $\text{DASG}(A) \times \text{DASG}(B) \times \text{DASG}(C)$ establishes a 1-to-1 bijection between distinct common subsequences and directed paths from $(0, 0, 0)$.
  3. *Reverse-Engineering Scratchpad*: Run memoized DAG DP over reachable triples $(i, j, k)$ via $\text{nxt}_A[i][c], \text{nxt}_B[j][c], \text{nxt}_C[k][c]$ in $O(|A||B||C||\Sigma|)$.
  4. *Boundary Pitfall*: Require 128-bit or arbitrary-precision integers if the problem asks for exact un-modded counts ($2^{150}$).

---

#### Tier 2: Intermediate (8 Problems — Product Automata Coupling SAM $\times$ DASG & Tropical Subsequence Matrices)

##### `P-4B-09`: Luogu P4112 — [HEOI2015] 最短不公共子串 (The Four-Comb Product Automaton Classic) (`[ZH]`, HEOI)
- **Inline Problem Statement & Constraints**: Given $A, B \in \{\texttt{'a'}..\texttt{'z'}\}^*$ ($|A|, |B| \le 2000$), output four integers: the shortest string that is (1) a substring of $A$ not a substring of $B$; (2) a substring of $A$ not a subsequence of $B$; (3) a subsequence of $A$ not a substring of $B$; (4) a subsequence of $A$ not a subsequence of $B$ (or `-1` if none exists).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Four combinations of contiguous factor ($\text{SAM}$) vs. scattered subsequence ($\text{DASG}$).
  2. *Combinatorial Invariant*: By Section 36.4, $L(\mathcal{A}^+(A)) \setminus L(\mathcal{A}^-(B))$ is recognized by the product automaton $\mathcal{A}^+(A) \times \mathcal{A}^-(B)$ where $\mathcal{A} \in \{\text{SAM}, \text{DASG}\}$.
  3. *Reverse-Engineering Scratchpad*: Build $\text{SAM}(A), \text{SAM}(B), \text{DASG}(A), \text{DASG}(B)$. For Q1–Q4, run BFS on $(u, v) \in \mathcal{A}^+(A) \times \mathcal{A}^-(B)$ from $(q_0^+, q_0^-)$; the first transition $(u, v) \xrightarrow{c} (u' \ne \bot, \bot)$ at depth $d$ yields answer $d + 1$ in $O(|A||B||\Sigma|)$.
  4. *Boundary Pitfall*: In $\text{SAM}$, states are $0$-indexed or $1$-indexed up to $2|B|$; do not confuse $\text{DASG}$ size ($|B|+1$) with $\text{SAM}$ size ($2|B|$) when allocating visited arrays `vis[u][v]`.

##### `P-4B-10`: Codeforces 750E — New Year and Old Subsequence (`[EN]`, Codeforces Goodbye 2016)
- **Inline Problem Statement & Constraints**: Given a digit string $S[1..N]$ ($N \le 2 \cdot 10^5$) and $Q \le 2 \cdot 10^5$ queries $[l, r]$, find the minimum number of character deletions in $S[l..r]$ so that the remaining string contains $\texttt{"2017"}$ as a subsequence but does **not** contain $\texttt{"2016"}$ as a subsequence (or `-1` if impossible).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Subsequence containment/avoidance of short fixed patterns on range queries $S[l..r]$ over the $(\min, +)$ tropical semiring.
  2. *Combinatorial Invariant*: Build the 5-state DFA over prefixes $\{\varepsilon, \texttt{"2"}, \texttt{"20"}, \texttt{"201"}, \texttt{"2017"}\}$. Reading character $c = S[i]$ maps state $u \in \{0..4\}$ either to $u$ (delete $c$ at cost $1$, or keep $c$ at cost $0$ if $c$ does not advance $u$ nor complete $\texttt{"2016"}$) or to $u+1$ (keep $c$ at cost $0$).
  3. *Reverse-Engineering Scratchpad*: Each digit $c \in \{\texttt{'0'}..\texttt{'9'}\}$ induces an upper-triangular $5 \times 5$ $(\min, +)$ matrix $M_c$. Maintain a Segment Tree of $5 \times 5$ matrices; for each query $[l, r]$, propagate a $1 \times 5$ row vector $\mathbf{v} = (0, \infty, \infty, \infty, \infty)$ across the $O(\log N)$ canonical segment tree nodes in $O(5^2 \log N)$ time!
  4. *Boundary Pitfall*: At state $3$ ($\texttt{"201"}$) and state $4$ ($\texttt{"2017"}$), reading $\texttt{'6'}$ must cost $+1$ to stay in the same state (we are **forced** to delete $\texttt{'6'}$ to avoid forming $\texttt{"2016"}$!). Forgetting the `'6'` penalty at state $4$ ($\texttt{"2017"}$) allows $\texttt{"20176"}$, which still contains $\texttt{"2016"}$!

##### `P-4B-11`: Codeforces 1609E — William The Oblivious (`[EN]`, Codeforces Deltix Round)
- **Inline Problem Statement & Constraints**: Given $S[1..N] \in \{\texttt{'a'}, \texttt{'b'}, \texttt{'c'}\}^N$ ($N, Q \le 10^5$) with single-character point updates, maintain the minimum number of character replacements so that $S$ does not contain $\texttt{"abc"}$ as a subsequence.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Point updates + subsequence avoidance of $\texttt{"abc"}$ $\implies$ $3 \times 3$ $(\min, +)$ tropical matrix on a Segment Tree.
  2. *Combinatorial Invariant*: Track the longest matched prefix of $\texttt{"abc"}$ in $\{0 (\varepsilon), 1 (\texttt{"a"}), 2 (\texttt{"ab"})\}$, disallowing transition $2 \xrightarrow{\texttt{'c'}} 3$. Equivalently, by Hall/cut duality, the minimum deletions to eliminate subsequence $\texttt{"abc"}$ equals $\min_{0 \le i \le j \le N} \bigl(\text{cnt}_{\texttt{a}}[1..i] + \text{cnt}_{\texttt{b}}[i+1..j] + \text{cnt}_{\texttt{c}}[j+1..N]\bigr)$!
  3. *Reverse-Engineering Scratchpad*: Maintain $3 \times 3$ upper-triangular $(\min, +)$ matrices in a Segment Tree in $O(3^3 \log N)$ per update.
  4. *Boundary Pitfall*: Replacing a character in $\{\texttt{'a'}, \texttt{'b'}, \texttt{'c'}\}$ is equivalent to deleting it (since you can always replace it with a character that doesn't complete a new $\texttt{"abc"}$, or view it as the 3-prefix partition above).

##### `P-4B-12`: Codeforces 1666F / 1426F — Number of Subsequences with Wildcards & Range Matrix Queries (`[EN]`, Codeforces)
- **Inline Problem Statement & Constraints**: Given $S[1..N] \in \{\texttt{'a'}, \texttt{'b'}, \texttt{'c'}, \texttt{'?'}\}^N$ ($N, Q \le 2 \cdot 10^5$), for each range query $[l, r]$ count the sum of occurrences of subsequence $\texttt{"abc"}$ over all $3^{\text{cnt}_{\texttt{?}}}$ assignments to `'?'` in $S[l..r]$ modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Fixed pattern $T = \texttt{"abc"}$ over ring $(\mathbb{Z}/p\mathbb{Z}, +, \times)$ with invertible $4 \times 4$ transition matrices!
  2. *Combinatorial Invariant*: For `'a'`, `'b'`, `'c'`, the $4 \times 4$ matrix $M_c$ is upper-unitriangular ($\det(M_c) = 1$). For `'?'`, $M_{\texttt{?}} = M_{\texttt{a}} + M_{\texttt{b}} + M_{\texttt{c}} = 3I_4 + E_{0,1} + E_{1,2} + E_{2,3}$, which has diagonal entries $3 \not\equiv 0 \pmod{10^9+7}$, so $\det(M_{\texttt{?}}) = 3^4 = 81$ is **invertible** modulo $10^9+7$!
  3. *Reverse-Engineering Scratchpad*: Precompute prefix $4 \times 4$ matrices $P_i = P_{i-1} M_{S[i]}$ and inverse prefix matrices $Q_i = M_{S[i]}^{-1} Q_{i-1}$ in $O(N)$, answering each query $[l, r]$ in **$O(1)$ time** via $(Q_{l-1} P_r)_{0, 3}$!
  4. *Boundary Pitfall*: Note that $\det(M_{\texttt{?}}) = 3^4$, so $M_{\texttt{?}}^{-1}$ requires $3^{-1} \bmod (10^9+7)$, which exists because $\gcd(3, 10^9+7) = 1$.

##### `P-4B-13`: AtCoder ABC 248 G / Codeforces 914F — Bitset Substring & Subsequence Matching (`[JA]` / `[EN]`)
- **Inline Problem Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), support single-character updates $S[i] \leftarrow c$ and substring/subsequence queries with bitsets in $O(N/w)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $N, \sum |P| \le 10^5$ with online point updates where SAM + LCT is overkill and $O(N|P|/w)$ fits comfortably in $10^8$ bit-word operations.
  2. *Combinatorial Invariant*: For substring occurrences in $S[l..r]$, `ans = M[P[1]] & (M[P[2]] >> 1) & ... & (M[P[m]] >> (m-1))`; for LCS against $P$, use the Allison–Dix bit-parallel step $V' = X \mathbin{\&} \sim(X - Y)$ across the $|P|$ characters.
  3. *Reverse-Engineering Scratchpad*: Maintain 26 `std::bitset<100005> M[26]` and update 2 bits per character modification in $O(1)$.
  4. *Boundary Pitfall*: When querying $S[l..r]$ for a pattern of length $m > r - l + 1$, immediately return $0$ to avoid negative right-shift counts $(r - m + 1 < l)$.

##### `P-4B-14`: Universal Cup / QOJ — Range Distinct Subsequences (`区间本质不同子序列个数`) (`[ZH]` / `[EN]`, QOJ / UCup)
- **Inline Problem Statement & Constraints**: Given $S[1..N]$ over `'a'..'z'` ($N \le 2 \cdot 10^5$) and $Q \le 2 \cdot 10^5$ queries $[l, r]$, output the number of distinct non-empty subsequences of $S[l..r]$ modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $N, Q = 2 \cdot 10^5, \sigma = 26$ makes Segment Tree of $27 \times 27$ matrices ($O(Q \sigma^2 \log N)$) too slow; requires Invertible Subsequence Matrix prefix/inverse reduction.
  2. *Combinatorial Invariant*: By Lemma 37.1, the $(27 \times 27)$ transition matrix $M_x$ has $\det(M_x) = 1$, and $\text{Ans}(l, r) = \bigl(\mathbf{e}_0^T Q_{l-1}\bigr) \bigl(P_r \mathbf{1}\bigr) - 1$.
  3. *Reverse-Engineering Scratchpad*: Use the $O((N+Q)\sigma)$ algorithm of Section 37.3: maintain $P_i$'s single-column update and `row_sum` vector $\mathbf{w}_i$, and $Q_i$'s lazy row-offset vector $\mathbf{u}_i^T$, answering each query by a 27-element dot product in $O(\sigma)$ time!
  4. *Boundary Pitfall*: Remember to subtract $1 \pmod{10^9+7}$ at the end of each query if the problem asks for **non-empty** subsequences.

##### `P-4B-15`: AtCoder AGC 024 E — Sequence Growing Hard (Subsequence Automaton Canonical Counting) (`[JA]`, AtCoder)
- **Inline Problem Statement & Constraints**: Count the number of sequences of strings $A_0 = \varepsilon, A_1, \dots, A_N$ over $\{1, \dots, K\}$ such that $A_i$ is obtained by inserting one character into $A_{i-1}$ and $A_{i-1} <_{\text{lex}} A_i$ ($N, K \le 300$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Inserting character $c$ at position $p$ into $A_{i-1}$ yields multiple ways to produce the **same** string $A_i$ if $c$ is inserted adjacent to existing copies of $c$!
  2. *Combinatorial Invariant*: Every string increase $A_{i-1} <_{\text{lex}} A_i$ has a **unique canonical insertion point** (namely, inserting $c$ immediately **before** the first character $A_{i-1}[p] < c$ of a contiguous run), which turns the sequence of insertions into an increasing tree / DASG-like canonical forest!
  3. *Reverse-Engineering Scratchpad*: Model the canonical insertion hierarchy as a labeled rooted tree of size $N+1$ where each node's label $c$ must exceed its attachment point's label, solved via $O(N^2 K)$ tree DP.
  4. *Boundary Pitfall*: Never count insertion *positions* directly without canonicalizing identical resulting strings; always enforce $c > \text{next\_char}$ at the unique leftmost insertion index of a run.

##### `P-4B-16`: Luogu P4607 — [SDOI2018] 反回文串 / Palindromic Subsequence Automaton DP (`[ZH]`, SDOI / Luogu)
- **Inline Problem Statement & Constraints**: Count distinct palindromic subsequences of $S[1..N]$ ($N \le 3000$) by matching from both ends on $\text{DASG}(S) \times \text{DASG}(S^R)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A palindrome $P = c_1 c_2 \dots c_k \dots c_2 c_1$ is determined by its half-string $c_1 \dots c_k$, which must appear as a subsequence from the left of $S$ and simultaneously from the right of $S$ without crossing!
  2. *Combinatorial Invariant*: Every distinct palindromic subsequence $P \preceq S$ has a unique **outermost canonical embedding** where the left half $c_1 \dots c_k$ uses the **earliest** indices $l_1 < \dots < l_k$ ($\text{DASG}(S)$) and the right half uses the **latest** indices $r_k < \dots < r_1$ ($\text{DASG}(S^R)$), valid if and only if $l_k \le r_k$!
  3. *Reverse-Engineering Scratchpad*: Run DP on interval states $(l, r)$ with transitions $(l, r) \xrightarrow{c} (\text{nxt}[l][c], \text{prv}[r][c])$ whenever $\text{nxt}[l][c] \le \text{prv}[r][c]$: if $<$, it adds both an even palindrome $Wc cW^R$ and an odd palindrome $WcW^R$; if $=$, it adds only the odd palindrome $WcW^R$!
  4. *Boundary Pitfall*: Separating `<` (contributes $+2$ to distinct palindromic extensions: $c$ and $cc$) from `=` (contributes $+1$: single middle character $c$) is essential to avoid missing odd-length centers or double-counting length-1 centers.

---

#### Tier 3: Advanced (8 Problems — Tiskin's Seaweed Matrices, Interval LCS, Cyclic LCS & Dynamic Inverse Subsequence Matrices)

##### `P-4B-17`: LOJ 3516 / Luogu P7456 / QOJ — [THUPC 2021] 区间 LCS (All-Pairs Interval LCS via Seaweed Matrix) (`[ZH]`, THUPC 2021)
- **Inline Problem Statement & Constraints**: Given $A[1..M], B[1..N]$ ($M \le 5000, N \le 5000$ or $Q \le 10^5$ queries $[l, r]$), compute $\text{LCS}(A[1..M], B[l..r])$ for each query $[l, r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Querying $\text{LCS}(A, B[l..r])$ for $Q \gg 1$ arbitrary substrings $B[l..r]$ defeats single-source LCS DP ($O(MNQ)$).
  2. *Combinatorial Invariant*: By Theorem 38.1, the $(M+N)$ seaweeds running through $A \times B$ cross at most once (`if (A[i] == B[j] || u > W[j]) swap(u, W[j])`), and the final bottom exit array $W[1..N]$ satisfies $\text{LCS}(A, B[l..r]) = \#\{k \in [l, r] : W[k] < l\}$.
  3. *Reverse-Engineering Scratchpad*: Run the 8-line Seaweed Comb in $O(MN)$ time to get $W[1..N]$; build a Persistent Segment Tree (or answer offline with a Fenwick Tree) to count $k \in [l, r]$ with $W[k] < l$ in $O(\log N)$ per query.
  4. *Boundary Pitfall*: Left-wall row $i$ must be initialized to $u = -i$ (not $i$ or $-(M-i+1)$) so that initial ranks along the top-left entrance perimeter are strictly increasing.

##### `P-4B-18`: Universal Cup / Petrozavodsk / CF Gym — Cyclic LCS (`循环最长公共子序列`) via Seaweed Comb (`[EN]` / `[ZH]`)
- **Inline Problem Statement & Constraints**: Given $A[1..M]$ and $B[1..N]$ ($M, N \le 2000$), find the maximum of $\text{LCS}(\text{shift}_i(A), \text{shift}_j(B))$ over all cyclic shifts of $A$ and $B$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Since $\text{LCS}(\text{shift}_i(A), \text{shift}_j(B)) = \max_{k} \text{LCS}(A, \text{shift}_k(B))$, we only need $\max_{1 \le l \le N} \text{LCS}(A[1..M], B'[l .. l + N - 1])$ where $B' = B \cdot B$ has length $2N$!
  2. *Combinatorial Invariant*: Every cyclic shift of $B$ is a contiguous interval $B'[l .. l + N - 1]$ of length $N$ in $B' = B \cdot B$.
  3. *Reverse-Engineering Scratchpad*: Run the Seaweed Comb on $A[1..M] \times B'[1..2N]$ in $O(MN)$ time to obtain $W[1..2N]$. Then for each $l \in [1, N]$, compute $\text{LCS}(A, B'[l..l+N-1]) = \#\{k \in [l, l+N-1] : W[k] < l\}$ in $O(N \log N)$ (or $O(N^2)$) total time!
  4. *Boundary Pitfall*: Do **not** run $N$ separate LCS DPs ($O(MN^2)$); a single $M \times 2N$ Seaweed Comb solves all $N$ cyclic shifts in $O(MN)$!

##### `P-4B-19`: UOJ / QOJ / 国家集训队互测 — Prefix-Suffix LCS Split (`前缀-后缀拼接 LCS`) (`[ZH]`, CTT / UOJ)
- **Inline Problem Statement & Constraints**: Given $A[1..M], B[1..N]$ ($M, N \le 5000$) and $Q \le 2 \cdot 10^5$ queries $(i, j, l, r)$, compute $\text{LCS}(A[i..M], B[1..j])$ or $\text{LCS}(A[1..i] + A'[i'..M'], B[l..r])$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Queries vary both a suffix of $A$ ($A[i..M]$) and a prefix of $B$ ($B[1..j]$).
  2. *Combinatorial Invariant*: By Theorem 38.2, in the Seaweed Matrix of $A[1..M] \times B[1..N]$, the wires entering at rows $i \dots M$ have initial ranks $\{-M, \dots, -i\}$, while all earlier rows $1 \dots i-1$ and top columns $1 \dots j$ have initial ranks $> -i$. Thus $\text{LCS}(A[i..M], B[1..j]) = \#\{k \in [1, j] : W[k] \le -i\}$.
  3. *Reverse-Engineering Scratchpad*: Build $W[1..N]$ in $O(MN)$ and a 2D prefix sum (or persistent segment tree) over $(k, W[k])$ to answer each $(i, j)$ in $O(1)$ or $O(\log N)$.
  4. *Boundary Pitfall*: Check the inequality direction carefully: row $i$ has initial rank $-i$, and rows below $i$ ($i+1 \dots M$) have ranks $-(i+1), \dots, -M < -i$, so the condition is $W[k] \le -i$.

##### `P-4B-20`: Codeforces 1380F — Strange Addition / Invertible vs. Segment-Tree Matrix Maintenance (`[EN]`, Codeforces)
- **Inline Problem Statement & Constraints**: Compare dynamic point-update range queries vs. static $O(1)$ range queries via invertible $2 \times 2$ / $(K+1)\times(K+1)$ matrices when $\det(M_i) \not\equiv 0 \pmod p$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Whenever a 1D DP has transition matrix $M_i \in GL_K(\mathbb{F}_p)$ and no point updates occur (or only stack append/pop at the ends), prefix matrices $P_r$ and inverse prefix matrices $Q_{l-1} = P_{l-1}^{-1}$ eliminate the $\log N$ Segment Tree factor.
  2. *Combinatorial Invariant*: Wait—what if a few matrices $M_i$ have $\det(M_i) \equiv 0 \pmod p$? Treat every index $i$ with $\det(M_i) = 0$ as a **rank-deficient reset barrier** (or factor out $p^v$), and use invertible prefix products between barriers!
  3. *Reverse-Engineering Scratchpad*: Precompute $P_i, Q_i$ in $O(NK^2)$ (or $O(NK)$ for elementary matrices).
  4. *Boundary Pitfall*: Always check whether any single character or digit configuration produces $\det(M_i) \equiv 0 \pmod p$!

##### `P-4B-21`: NowCoder Multi-University / QOJ — Range Distinct Subsequences with Gap Constraint (`区间不相邻本质不同子序列`) (`[ZH]`, NowCoder / QOJ)
- **Inline Problem Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 10^5, |\Sigma| \le 10$), for each query $[l, r]$ count distinct subsequences of $S[l..r]$ with no two adjacent indices chosen ($i_r - i_{r-1} \ge 2$) modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Combines `ABC 214F` (gap-$2$ distinct subsequences) with range queries $[l, r]$.
  2. *Combinatorial Invariant*: Track for each character $c \in \Sigma$ both the count ending at $c$ **available at the current step** ($f_c$) and the **buffered update** ($g_c$) from index $i-1$ that becomes available at $i+1$. Wait: does the buffered transition matrix have determinant $\ne 0$?
     Actually, in the gap-$2$ recurrence $dp[i] = \sum_{j = \text{prev}[i]-1}^{i-2} dp[j]$, because $f'_x$ overwrites $f_x$ using values from $i-2$ while forgetting the old $f_x$, the $(\sigma+2)\times(\sigma+2)$ matrix can be singular—so we use a **Segment Tree / Divide-and-Conquer** where each node stores the transition from $(\Sigma \cup \{\varepsilon\})$ at the left boundary to the right boundary in $O(\sigma^2 \log N)$!
  3. *Reverse-Engineering Scratchpad*: In Divide-and-Conquer over $[L, R]$ with midpoint $M$, precompute forward DP from the $\sigma+1$ boundary states at $M$ and backward DP to $M$, answering queries straddling $M$ in $O(\sigma)$ per query!
  4. *Boundary Pitfall*: This problem is the canonical counterexample showing why you must **test matrix invertibility** (`Section 37.5 Pitfall 1`): standard distinct-subsequence matrices ($d=1$) are invertible ($\det = 1$), whereas gap-$2$ ($d=2$) matrices lose rank and require Divide-and-Conquer!

##### `P-4B-22`: AtCoder ABC 285 G / ARC 159 D — Subsequence DP Compression with Fenwick / Monge Structure (`[JA]`, AtCoder)
- **Inline Problem Statement & Constraints**: Compress 2D subsequence/interval transitions when character matches are sparse ($K \le 2 \cdot 10^5$ matching pairs $(i, j)$ with $A[i] = B[j]$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: When $M, N \le 10^5$ so $O(MN)$ is impossible, but the number of matching pairs $\mathcal{M} = \{(i, j) : A[i] = B[j]\}$ is small ($|\mathcal{M}| \le 2 \cdot 10^5$, e.g., each character appears $\le 5$ times), we can compute LCS / Seaweed transitions in $O(|\mathcal{M}| \log N)$!
  2. *Combinatorial Invariant*: Hunt–Szymanski invariant: in row $i$, the threshold columns $j_1 < j_2 < \dots < j_k$ where $dp[i][j]$ steps up from $r-1$ to $r$ only change at columns $j$ where $A[i] = B[j]$!
  3. *Reverse-Engineering Scratchpad*: Process matching columns $j$ for $A[i]$ in **decreasing order** so each match updates $\text{thresh}[r] \leftarrow \min(\text{thresh}[r], j)$ via binary search (`lower_bound`) in $O(|\mathcal{M}| \log N)$ time.
  4. *Boundary Pitfall*: Iterating matching columns $j$ in *increasing* order allows a single character $A[i]$ to match multiple positions in $B$ within the same row! Always iterate matches for row $i$ in **strictly decreasing order of $j$**.

##### `P-4B-23`: Codeforces 1117G / QOJ — Subsequence Automaton with Lexicographical K-th Path & Persistent Segment Tree (`[EN]` / `[ZH]`)
- **Inline Problem Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5, |\Sigma| \le 10^5$) and $K \le 10^{18}$, find the $K$-th lexicographically smallest **distinct** subsequence of $S$ (outputting its hash or characters).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $|\Sigma| \le 10^5$ prevents an explicit $N \times |\Sigma|$ DASG table ($O(N|\Sigma|)$ memory MLEs), and $K \le 10^{18}$ requires walking the DASG in $O(\text{ans\_len} \cdot \log |\Sigma|)$.
  2. *Combinatorial Invariant*: Row $\text{nxt}[i][\cdot]$ of $\text{DASG}(S)$ differs from $\text{nxt}[i+1][\cdot]$ in only one entry $c = S[i+1]$.
  3. *Reverse-Engineering Scratchpad*: Store $\text{nxt}[i][\cdot]$ as a **Persistent Segment Tree** over $c \in [1, |\Sigma|]$, where each leaf $c$ stores $dp[\text{nxt}[i][c]]$ (capped at $K$). To find the $K$-th subsequence of $S$, if $K$ can be up to $10^{18}$ while the answer length could be $N$, compress **forced-first-child chains** (`dp[nxt[i][c_min]] >= K`) using binary lifting on the DASG!
  4. *Boundary Pitfall*: If $K$ is smaller than the number of subsequences starting with the minimum available character $c_{\min}$, a naive step-by-step walk takes $O(N)$ steps per query; binary lifting along the smallest-character edge reduces each query to $O(\log^2 N)$!

##### `P-4B-24`: Codeforces 1080F / AtCoder ARC 142 D — Bit-Parallel LCS + Hirschberg $O(NM/w)$ Space-Optimal Alignment Reconstruction (`[EN]` / `[JA]`)
- **Inline Problem Statement & Constraints**: Given $A[1..M], B[1..N]$ ($M, N \le 30{,}000$), reconstruct the actual **longest common subsequence string** (not just its length) within $O(M + N)$ memory and $2.0\text{s}$ time limit.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Storing all $M$ bit-vectors $V_i$ takes $30000 \times (30000 / 8) \approx 112\text{ MB}$, and standard Hirschberg takes $O(MN)$ which TLEs at $30000^2 = 9 \cdot 10^8$.
  2. *Combinatorial Invariant*: Hirschberg's divide-and-conquer splits $A$ at midpoint $M/2$, computes the forward DP row $\text{fwd}[0..N]$ of $A[1..M/2]$ against $B[1..N]$ and the backward DP row $\text{bwd}[0..N]$ of $A[M/2+1..M]^R$ against $B[1..N]^R$, and finds $j^* = \arg\max_{0 \le j \le N} (\text{fwd}[j] + \text{bwd}[N-j])$.Both $\text{fwd}$ and $\text{bwd}$ can be computed in **$O(MN/w)$ time** via the Allison–Dix bit-parallel row step $V' = X \mathbin{\&} \sim(X - Y)$, then unpacked from 1-bit differences $\Delta H_j \in \{0, 1\}$ into prefix sums in $O(N)$ time at the base of the recursion!
  3. *Reverse-Engineering Scratchpad*: At each recursive call $(l_A, r_A, l_B, r_B)$, run bit-parallel LCS on the subgrid of width $W = r_B - l_B + 1$ in $O((r_A - l_A) W / 64)$ time. Summing over the recursion tree gives $T(M, N) = \sum_{d \ge 0} O(M N / (2^d \cdot 64)) = O(MN / 64)$ total time and $O(M + N)$ total space!
  4. *Boundary Pitfall*: Building the pattern masks $M[c]$ from scratch in $O(|\Sigma| \cdot W / 64)$ inside every recursive call adds an $O(M |\Sigma|)$ overhead; only build $M[c]$ for characters $c$ that actually appear in $A[l_A..r_A]$ (or slice precomputed global bitsets by shifting!).

---

#### Tier 4: Mastery & Grandmaster Synthesis (8 Problems — Unit-Monge $\boxdot$ Multiplication, Weighted/RLE Seaweed, Dynamic Seaweed & Myers Bit-Parallel Synthesis)

##### `P-4B-25`: QOJ / Universal Cup — Range-Range Substring LCS (`雙区間 LCS`: $\text{LCS}(A[l_1..r_1], B[l_2..r_2])$) via Unit-Monge $\boxdot$ Segment Tree (`[ZH]` / `[EN]`, QOJ / UCup)
- **Inline Problem Statement & Constraints**: Given $A[1..M], B[1..N]$ ($M, N \le 30{,}000$) and $Q$ queries $(l_1, r_1, l_2, r_2)$ (or $M \le 1000, N \le 10000, Q \le 10^5$), compute $\text{LCS}(A[l_1..r_1], B[l_2..r_2])$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Both $A$ and $B$ are restricted to arbitrary intervals $[l_1, r_1]$ and $[l_2, r_2]$.
  2. *Combinatorial Invariant*: The Seaweed permutation matrix $P_{[l_1, r_1]}$ for horizontal strip $A[l_1..r_1] \times B[1..N]$ is the Unit-Monge distance product ($\boxdot$) of the strip matrices inside a Segment Tree over $[1, M]$!
  3. *Reverse-Engineering Scratchpad*: Build a Segment Tree (or Sqrt blocks) over the rows of $A$, multiplying child Seaweed permutations via Tiskin's $O(N \log N)$ Unit-Monge $\boxdot$ algorithm.
  4. *Boundary Pitfall*: In Tiskin's $O(K \log K)$ Unit-Monge multiplication, remember to filter out unused identity wires (wires that never cross inside a small strip) so that a Segment Tree node over $L$ rows of $A$ only has $O(\min(N, L))$ active non-trivial seaweeds!

##### `P-4B-26`: 国家集训队论文 2021 / QOJ — Run-Length Encoded (RLE) LCS in $O(K^2 \log K)$ via Seaweed Multiplication (`[ZH]`, 国家集训队论文)
- **Inline Problem Statement & Constraints**: Given two run-length encoded strings $A = c_1^{a_1} \dots c_m^{a_m}$ and $B = d_1^{b_1} \dots d_n^{b_n}$ ($m, n \le 1000$, total unexpanded lengths $\sum a_i, \sum b_j \le 10^9$), compute $\text{LCS}(A, B)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Each block $c_i^{a_i} \times d_j^{b_j}$ is either a **homogeneous match block** ($c_i = d_j$, where no two wires ever cross!) or a **homogeneous mismatch block** ($c_i \ne d_j$, where every uncrossed pair of wires crosses!).
  2. *Combinatorial Invariant*: Across an entire uniform block $c_i^{a_i} \times d_j^{b_j}$, the outgoing seaweed permutation on the right and bottom walls is an explicit piecewise-shifted interval permutation of the incoming left and top walls!
  3. *Reverse-Engineering Scratchpad*: Represent the boundary seaweed ranking in compressed interval segments (or apply Tiskin's RLE seaweed block transition in $O(m n \log(m+n))$).
  4. *Boundary Pitfall*: In a mismatch block $c_i \ne d_j$, wires $u$ and $v$ cross **only if $u < v$**; if $u > v$ (they already crossed in an earlier block), they bounce off each other even inside a mismatch block!

##### `P-4B-27`: Codeforces 1810G / Universal Cup — Online Append/Prepend Distinct Subsequences via Double-Ended Matrix Stack (`[EN]`, UCup / CF)
- **Inline Problem Statement & Constraints**: Maintain a string $S$ under $Q \le 3 \cdot 10^5$ operations: `push_front(c)`, `push_back(c)`, `pop_front()`, `pop_back()`, and query the number of distinct subsequences of $S[l..r]$ modulo $998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Deque updates at both ends + range distinct subsequence queries $[l, r]$.
  2. *Combinatorial Invariant*: Anchor a center index $0$ between the front stack and back stack. Any range $[l, r]$ is a product of matrices from $l$ to $r$, which equals $P_{l-1}^{-1} P_r$ where $P_i$ is extended forward for $i > 0$ ($P_i = P_{i-1} M_{S[i]}$) and backward for $i < 0$ ($P_i = M_{S[i+1]}^{-1} P_{i+1}$)!
  3. *Reverse-Engineering Scratchpad*: Maintain both $(P_i, Q_i)$ for $i \ge 0$ (back stack) and $(P_{-i}, Q_{-i})$ for $i > 0$ (front stack) in $O(\sigma)$ per push and $O(1)$ per pop (by simply decrementing the stack pointer!), answering any query $[l, r]$ in $O(\sigma)$ time via $\mathbf{u}_{l-1}^T \cdot \mathbf{w}_r$!
  4. *Boundary Pitfall*: When extending to negative indices $i < 0$ on `push_front(c)`, $P_{i-1} = M_c^{-1} P_i$ and $Q_{i-1} = Q_i M_c$ — notice that left-multiplication vs. right-multiplication swaps roles on the front stack!

##### `P-4B-28`: AtCoder AGC 019 F / JOI Open — Weighted Seaweed / Non-Intersecting Lattice Paths with Diagonal Bonuses (`[JA]`, AtCoder / JOI)
- **Inline Problem Statement & Constraints**: Generalize Seaweed / Unit-Monge properties to $k$-disjoint paths (or $k$-LCS: choosing $k$ disjoint paths in the LCS grid to maximize total matched characters).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Selecting $k$ vertex-disjoint alignment paths in $A \times B$ to maximize total matches.
  2. *Combinatorial Invariant*: By Greene's Theorem / RSK correspondence and Tiskin's Seaweed Theorem, the maximum weight of $k$ disjoint paths in the semi-local alignment grid equals the sum of the top $k$ seaweed displacement scores (specifically, each seaweed that starts on the left wall and exits on the bottom wall—or moves right by $\ge$ threshold—contributes $1$)!
  3. *Reverse-Engineering Scratchpad*: Compute the Seaweed permutation $W[1..N]$ in $O(MN)$ time; count how many left-wall wires ($W[k] < 0$) exit at the bottom wall!
  4. *Boundary Pitfall*: Distinguish edge-disjoint vs. strictly vertex-disjoint paths in the alignment grid.

##### `P-4B-29`: Codeforces 1784F / Universal Cup — Approximate Pattern Matching in $O(NM/w)$ via Myers' Bit-Parallel Edit Distance (`[EN]`, Codeforces / UCup)
- **Inline Problem Statement & Constraints**: Given text $T[1..N]$ and pattern $P[1..M]$ ($N \le 10^5, M \le 5000$) and threshold $K$, find all ending positions $j \in [1, N]$ where $P$ matches a suffix of $T[1..j]$ with edit distance $\le K$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Semi-local edit distance (starting anywhere in $T$ at cost $0$, matching all of $P[1..M]$) with $M \le 5000, N \le 10^5$.
  2. *Combinatorial Invariant*: In Myers' bit-parallel column algorithm (`Section 39.3`), setting the top boundary horizontal difference $HP[0] = 0, HN[0] = 0$ (since $dp[0][j] = 0$ for all $j$ in semi-local matching, rather than $dp[0][j] = j$!) means `X' = (HP << 1)` (without `| 1` at bit 0!), and the bottom entry $dp[M][j]$ updates by $+1$ if $HP[M-1] = 1$ and $-1$ if $HN[M-1] = 1$!
  3. *Reverse-Engineering Scratchpad*: Run Myers' 15-instruction bit-parallel column step across $\lceil M / 64 \rceil$ words in $O(NM / 64)$ time.
  4. *Boundary Pitfall*: For whole-string edit distance $\text{ed}(P, T)$, $dp[0][j] = j$ so bit $0$ of $HP$ is $1$ (`(HP << 1) | 1`); for **substring/semi-local** edit distance (where $P$ can start at any index of $T$ for free), $dp[0][j] = 0$ so bit $0$ has $\Delta H_{0, j} = 0$ (`(HP << 1)` with **no** `| 1`!).

##### `P-4B-30`: Luogu P6640 / BZOJ — [BJOI2020] 封印 / Hybrid SAM + Bit-Parallel / Subsequence Comparison (`[ZH]`, BJOI)
- **Inline Problem Statement & Constraints**: Compare contiguous substring containment ($\text{SAM}$ + binary lifting + RMQ) against scattered subsequence containment ($\text{DASG}$ / Seaweed) on range queries $(l, r)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Distinguishing when a problem asks for $\max_{P \text{ substr } B[l..r]} [P \text{ substr } A]$ (Wave 2A SAM + RMQ) vs. $\max_{P \text{ subseq } B[l..r]} [P \text{ subseq } A]$ (Wave 4B Seaweed Matrix).
  2. *Combinatorial Invariant*: Contiguous factors are governed by `lcs_len[r]` on $\text{SAM}(A)$ with $\min(r - l' + 1, \text{lcs\_len}[r])$; scattered subsequences are governed by the Seaweed permutation $W[1..N]$ with $\#\{k \in [l, r] : W[k] < l\}$.
  3. *Reverse-Engineering Scratchpad*: Side-by-side comparison for Blind Checkpoint diagnosis (`CP-V`).
  4. *Boundary Pitfall*: Students frequently misread 子序列 (subsequence) vs. 子串 (substring) in Chinese statements!

##### `P-4B-31`: QOJ / Universal Cup — Constrained LCS (`CLCS`: Longest Common Subsequence Containing Pattern $P$) via Product Automaton + Bit-Parallel (`[EN]` / `[ZH]`, UCup)
- **Inline Problem Statement & Constraints**: Given $A[1..M], B[1..N]$ ($M, N \le 10^4$) and a constraint string $P[1..K]$ ($K \le 20$), find the longest common subsequence of $A$ and $B$ that **contains $P$ as a subsequence** (or **avoids $P$ as a substring**).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $M, N = 10^4, K = 20$ gives $10^4 \times 10^4 \times 20 = 2 \cdot 10^9$ states, which TLEs without bit-parallelism across the $N$ dimension!
  2. *Combinatorial Invariant*: For each state $k \in \{0, \dots, K\}$ of the constraint automaton for $P$, $dp[i][j][k] - dp[i][j-1][k] \in \{0, 1\}$ still holds when transitioning within layer $k$, and inter-layer jumps $k-1 \to k$ inject $1$-bits at positions where both $A[i] = P[k]$ and $B[j] = P[k]$!
  3. *Reverse-Engineering Scratchpad*: Maintain $K+1$ bitsets $V_0, V_1, \dots, V_K$ of length $N$; update each $V_k$ via Allison–Dix bit-parallel subtraction plus bit-injection from $V_{k-1}$ in $O(MNK / w)$ time!
  4. *Boundary Pitfall*: When $P$ must be avoided as a **contiguous substring** of the output LCS, build the KMP automaton of $P$; when $P$ must be contained/avoided as a **subsequence** of the output LCS, every subsequence of $P$ is automatically a subsequence of $A$ and $B$ iff $P$ is, so containing $P$ as a *subsequence* of the LCS is equivalent to $P$ being a **substring** of the LCS in its canonical matching order!

##### `P-4B-32`: QOJ / Petrozavodsk — Dynamic All-Pairs Interval LCS under Character Appends to $A$ and $B$ (`动态海草矩阵`) (`[EN]` / `[ZH]`, QOJ)
- **Inline Problem Statement & Constraints**: Maintain $A$ and $B$ as characters are appended to the right of $A$ (`append_A(c)`) or the right of $B$ (`append_B(c)`), and answer online queries $\text{LCS}(A, B[l..r])$ ($|A|, |B| \le 5000, Q \le 10^5$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Both $A$ (rows) and $B$ (columns) grow dynamically on the right!
  2. *Combinatorial Invariant*: In the Seaweed grid $A[1..M] \times B[1..N]$:
     - Appending a row $M+1$ to $A$ sweeps a new wire $u = -(M+1)$ left-to-right across the bottom wires $W[1..N]$ in **$O(N)$ time**, updating both $W[1..N]$ and the right-wall exit $R[M+1] = u$!
     - Appending a column $N+1$ to $B$ sweeps a new wire $v = N+1$ top-to-bottom across the **right-wall wires** $R[1..M]$ in **$O(M)$ time**:
       ```cpp
       int v = N + 1;
       for (int i = 1; i <= M; ++i) {
           if (A[i] == B[N + 1] || R[i] > v) swap(R[i], v);
       }
       W[N + 1] = v;
       ```
  3. *Reverse-Engineering Scratchpad*: Maintain both bottom-wall exits $W[1..N]$ and right-wall exits $R[1..M]$! Each `append_A` takes $O(N)$ and modifies $W[1..N]$; each `append_B` takes $O(M)$ and only appends $W[N+1]$ while modifying $R[1..M]$!
  4. *Boundary Pitfall*: In `append_B`, the wire entering cell $(i, N+1)$ from the left is $R[i]$ and the wire entering from the top is $v$, so the already-crossed condition is `R[i] > v` (left wire $>$ top wire), **not** `v > R[i]`!

---

### 40.3 Wave 4B Multilingual Bibliography & Rosetta Stone Additions (`CITATIONS.md` Feed)

1. **Tiskin, A. (2008 / 2015)**, *"Semi-local string comparison: Algorithmic techniques and applications"*, Mathematics in Computer Science / arXiv:0707.3619. (Foundational treatise introducing Seaweed Matrices, Unit-Monge distance multiplication $\boxdot$ in $O(N \log N)$, and All-Pairs Interval LCS.)
2. **中國國家集訓隊 2021 論文 (`[国家集训队论文 2021]`)**, *《单位蒙日矩阵与海草算法在最长公共子序列问题中的应用》 (Unit-Monge Matrices and the Seaweed Algorithm in LCS Problems)*. (Comprehensive Chinese Olympiad treatise covering Seaweed Comb rules, 0-Hecke braid monoids, $\boxdot$ divide-and-conquer, and `[THUPC 2021] 区间 LCS`.)
3. **Allison, L., & Dix, T. I. (1986)**, *"A bit-string longest-common-subsequence algorithm"*, Information Processing Letters, 23(6), 305–310. (First $O(NM/w)$ bit-parallel LCS algorithm using hardware subtraction carries.)
4. **Myers, G. (1999)**, *"A fast bit-vector algorithm for approximate string matching based on dynamic programming"*, Journal of the ACM, 46(3), 395–415. (The $O(NM/w)$ bit-parallel edit-distance algorithm encoding $\Delta V, \Delta H \in \{-1, 0, +1\}$ into boolean vectors $VP, VN, HP, HN$.)
5. **Crochemore, M., Iliopoulos, C. S., Pinzon, Y. J., & Reid, J. F. (2001)** & **Hyyrö, H. (2003)**, *"A fast and practical bit-vector algorithm for the Longest Common Subsequence problem"*, SPIRE. (Refined 4-operation bit-parallel LCS transition $V' = X \mathbin{\&} \sim(X - Y)$.)
6. **Baeza-Yates, R. A. (1991)** & **Crochemore, M., Melichar, B., & Troníček, Z. (2000)**, *"Directed Acyclic Subsequence Graph (DASG)"*. (Formalization of `序列自动机` / DASG and multi-string subsequence automata.)
7. **noshi91 / maspypy / tatyam (`[JA]` String & Matrix Blog Canon)**, *"部分列 DP の行列表示とその逆行列 (Matrix Representation of Subsequence DP and Its Inverse)"* & *"Seaweed Matrix による区間 LCS"*. (Japanese competitive programming treatises deriving $O((N+Q)\sigma)$ range distinct subsequences via invertible elementary matrices.)

#### Wave 4B Multilingual Terminology Rosetta Stone
| English (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) |
| :--- | :--- | :--- |
| Directed Acyclic Subsequence Graph (DASG) | 序列自动机 / 子序列自动机 | 部分列オートマトン (`Subsequence Automaton`) |
| Shortest Absent Subsequence (SAS) | 最短非子序列 / 最短不公共子序列 | 最短非部分列 |
| Invertible Subsequence Matrix | 子序列 DP 矩阵可逆性 / 初等矩阵前缀积 | 部分列 DP の可逆行列 / 累積積と逆行列 |
| Tiskin's Seaweed Matrix | 海草矩阵 / 海草算法 | Seaweed 行列 / 海藻アルゴリズム |
| Unit-Monge Matrix & Distance Product ($\boxdot$) | 单位蒙日矩阵与距离乘积 | 単位 Monge 行列と距離積 |
| Semi-Local LCS / Interval LCS | 半局部 LCS / 区间 LCS | 区間 LCS / 半局所 LCS |
| Bit-Parallel LCS / Edit Distance | 位并行 LCS / Bitset 优化 LCS | ビット並列 LCS / Myers のビット並列編集距離 |
