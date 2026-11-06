# Wave 4B (Cohort 2 Independent Research — Iterations 88–92): Subsequence Automata (DASG), Invertible Subsequence Matrices, Tiskin's Seaweed Matrices & Bit-Parallel LCS

> **Cohort 2 Independence Record**: This document is the 100% independent redundant discovery and structural derivation pass for **Wave 4B (Iterations 88–92)**, written without reading Cohort 1's `iter_36_to_40_subsequence_matrices_seaweed_bitparallel.md`. Every combinatorial invariant, matrix factorization, Unit-Monge braid multiplication proof, bitwise carry identity, and multilingual problem analysis below is derived from first principles following the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard** (`PLAN.md §2`).

---

## Iteration 88: Direct Acyclic Subsequence Graph (`序列自动机` / DASG), Shortest Absent Subsequence (`SAS`), Arch Factorization & Four-Comb Product Automata

### 88.1 The 4-Step Structural Derivation of the Subsequence Automaton (DASG)

#### Step 1: The Diagnostic Signal (Why Naive Subsequence Matching & Whole-String Suffix Structures Fail)
Suppose we are given a text $S[1..N]$ over an alphabet $\Sigma$ of size $\sigma = |\Sigma|$ and must answer:
1. Whether a pattern $P[1..M]$ is a subsequence of $S$ (or of a substring $S[l..r]$),
2. How many distinct subsequences $S$ possesses, or what the **Shortest Absent Subsequence (SAS)** (`最短缺失子序列`) of $S$ is, or
3. What the shortest string $W$ is that appears as a **subsequence** of $A$ but **not** as a **substring** (or subsequence) of $B$ (`[HEOI2015] 最短不公共子串` / `Luogu P4112`).

Why do standard substring structures (KMP, AC, SA, SAM) fail on subsequences?
- A Suffix Automaton (SAM) compresses substrings into $O(N)$ equivalence classes of $\text{endpos}$ sets because contiguous occurrences of a factor $u$ shift rigidly by $+1$ when extended by one character. Subsequences have $2^N$ possible index subsets; the set of ending positions of a subsequence $P$ in $S$ does not obey contiguous shift invariance.
- Conversely, building an explicit deterministic finite automaton (DFA) by subset construction on the NFA that allows $\epsilon$-skips over every character would ostensibly create $2^N$ subset states. Yet the minimal deterministic automaton accepting all subsequences of $S$ has **at most $N + 1$ states**! Why does subset construction collapse from $2^N$ states to $N+1$ singleton states?

#### Step 2: The Combinatorial Word Invariant (Canonical Earliest-Match Dominance & Simon's Arch Factorization)

##### Theorem 88.1 (Canonical Greedy Prefix Dominance)
Let $S[1..N]$ be a string. For any sequence $P = c_1 c_2 \dots c_m$, define its **canonical greedy match index** $\text{pos}_S(P) \in \{0, 1, \dots, N, \infty\}$ inductively by:
$$\text{pos}_S(\epsilon) = 0, \qquad \text{pos}_S(P' \cdot c) = \min \bigl\{ j \in \{\text{pos}_S(P') + 1, \dots, N\} \;\big|\; S[j] = c \bigr\}$$
with $\min \emptyset = \infty$. Then for every right extension $Q \in \Sigma^*$:
$$P \cdot Q \text{ is a subsequence of } S \iff Q \text{ is a subsequence of the suffix } S[\text{pos}_S(P) + 1 .. N].$$
Consequently, the Nerode right-congruence class of $P$ with respect to the language $\text{Subseq}(S)$ is completely determined by the single integer $\text{pos}_S(P) \in \{0, 1, \dots, N, \infty\}$.

*Proof (Exchange Argument on Occurrence Monotonicity).*
($\Leftarrow$) If $P$ matches inside $S[1..\text{pos}_S(P)]$ and $Q$ matches inside $S[\text{pos}_S(P)+1..N]$, concatenating their index sequences gives a valid strictly increasing embedding of $P \cdot Q$ in $S$.
($\Rightarrow$) Suppose $P \cdot Q$ has *any* valid embedding $1 \le i_1 < i_2 < \dots < i_m < j_1 < \dots < j_{|Q|} \le N$ where $S[i_k] = P[k]$ and $S[j_r] = Q[r]$. We prove by induction on $k = 1, \dots, m$ that $\text{pos}_S(P[1..k]) \le i_k$:
- Base case $k = 0$: $\text{pos}_S(\epsilon) = 0 \le i_0 := 0$.
- Inductive step: By the induction hypothesis, $\text{pos}_S(P[1..k-1]) \le i_{k-1} < i_k$. Since $i_k \ge \text{pos}_S(P[1..k-1]) + 1$ and $S[i_k] = P[k]$, the index $i_k$ belongs to the candidate set $\{j > \text{pos}_S(P[1..k-1]) \mid S[j] = P[k]\}$. Since $\text{pos}_S(P[1..k])$ is the minimum of this set, $\text{pos}_S(P[1..k]) \le i_k$.

At $k = m$, we have $\text{pos}_S(P) \le i_m < j_1$. Thus $j_1 < j_2 < \dots < j_{|Q|}$ all lie in $[\text{pos}_S(P) + 1, N]$, proving $Q$ is a subsequence of $S[\text{pos}_S(P) + 1 .. N]$. $\blacksquare$

##### Theorem 88.2 (Hébrard's Arch Factorization & Shortest Absent Subsequence Duality)
Define a string $U$ to be **$1$-universal** (or a **full arch**) over $\Sigma$ if every character $c \in \Sigma$ appears at least once in $U$; let $\iota(S)$ (the **universality index** of $S$) be the maximum $k \ge 0$ such that every string in $\Sigma^k$ is a subsequence of $S$.
Factorize $S$ greedily from left to right into minimal $1$-universal blocks (**arches**):
$$S = A_1 A_2 \dots A_k \cdot R$$
where each $A_r = S[l_r .. r_r]$ is the shortest prefix of $S[l_r .. N]$ containing all $\sigma$ characters of $\Sigma$, and the **rest** $R = S[l_{k+1}..N]$ lacks at least one character of $\Sigma$. Then:
1. The length of the **Shortest Absent Subsequence (SAS)** of $S$ is exactly $k + 1$ (so $\iota(S) = k$).
2. Every SAS of $S$ of length $k + 1$ is obtained by picking in each arch $A_r$ a character that occurs **only at the very last position** $r_r$ of $A_r$ (or at least forces the canonical match past previous arches), and ending with a character $c \notin \text{alph}(R)$.

*Proof.*
1. **Lower bound ($> k$ is impossible for length $\le k$)**: Any word $W = c_1 c_2 \dots c_k \in \Sigma^k$ of length $k$ has $c_1 \in A_1$ (since $A_1$ contains all of $\Sigma$), $c_2 \in A_2$, ..., $c_k \in A_k$. Thus $\text{pos}_S(W) \le r_k \le N$, so every $W \in \Sigma^k$ is a subsequence of $S$.
2. **Upper bound ($\exists W \in \Sigma^{k+1}$ absent from $S$)**: For each arch $A_r = S[l_r..r_r]$, by minimality of $r_r$, the last character $m_r = S[r_r]$ does **not** appear anywhere in $S[l_r .. r_r - 1]$. Choose $m_{k+1} \in \Sigma \setminus \text{alph}(R)$. Consider the word $M = m_1 m_2 \dots m_k m_{k+1}$ of length $k + 1$. By definition of $m_1$, the earliest occurrence of $m_1$ in $S[1..N]$ is at index $r_1$. Inductively, after matching $m_1 \dots m_{r-1}$ at index $r_{r-1} = l_r - 1$, the earliest occurrence of $m_r$ in $S[l_r .. N]$ is at index $r_r$. Finally, after reaching $r_k = l_{k+1} - 1$, the character $m_{k+1}$ does not occur in $R = S[l_{k+1}..N]$, so $\text{pos}_S(M) = \infty$. $\blacksquare$

#### Step 3: The Reverse-Engineering Scratchpad (DASG Construction, Persistence & Four-Comb Product Automata)

##### 1. Backward Scan vs. Persistent Functional DASG
The **Direct Acyclic Subsequence Graph (DASG / `序列自动机`)** of $S[1..N]$ has states $i \in \{0, 1, \dots, N\}$ (plus dead sink $\infty$ or $-1$), with transition table:
$$\text{nxt}[i][c] = \min \{ j \in [i+1, N] \mid S[j] = c \}.$$
Scanning backwards from $i = N - 1$ down to $0$:
$$\text{nxt}[i][c] = \begin{cases} i + 1 & \text{if } S[i+1] = c, \\ \text{nxt}[i+1][c] & \text{if } S[i+1] \ne c. \end{cases}$$
- **Time/Space Contract (Dense Table)**: $O(N |\Sigma|)$ time and space.
- **Persistent / Large-Alphabet Contract ($|\Sigma| \le N$)**: Observe that row $\text{nxt}[i][\cdot]$ differs from row $\text{nxt}[i+1][\cdot]$ in **exactly one entry**, namely $c = S[i+1]$! Replacing the flat array of size $|\Sigma|$ with a **Persistent Segment Tree** (or persistent balanced tree) over $[1, |\Sigma|]$ constructs the entire DASG in $O(N \log |\Sigma|)$ time and space, while supporting transitions $\text{nxt}[i][c]$ in $O(\log |\Sigma|)$ time.
- **Range Subsequence Check on $S[l..r]$**: By Theorem 88.1 applied to the suffix $S[l..N]$, a pattern $P[1..M]$ is a subsequence of $S[l..r]$ if and only if starting at state $u_0 = l - 1$ and transitioning $u_k = \text{nxt}[u_{k-1}][P[k]]$ yields $u_M \le r$.

##### 2. Backward DP on DASG for SAS and Lexicographically $K$-th Subsequence
To compute the shortest absent subsequence (and its lexicographically smallest witness, or count of SAS):
- Define $d[i]$ for $i \in \{0, \dots, N\}$ as the minimum length of a string $W \in \Sigma^+$ that is **not** a subsequence of $S[i+1..N]$:
  $$d[i] = 1 + \min_{c \in \Sigma} \begin{cases} 0 & \text{if } \text{nxt}[i][c] = \infty, \\ d[\text{nxt}[i][c]] & \text{if } \text{nxt}[i][c] \le N. \end{cases}$$
- Similarly, to find the lexicographically $K$-th distinct subsequence of $S$, define $dp[i] = 1 + \sum_{c \in \Sigma, \text{nxt}[i][c] \le N} dp[\text{nxt}[i][c]]$ (capped at $\min(\text{val}, K+1)$ to prevent 64-bit integer overflow!). Every path from state $0$ in the DASG corresponds bijectively to a distinct subsequence via its canonical greedy embedding.

##### 3. The Four-Comb Product Automaton (`[HEOI2015] 最短不公共子串` / `Luogu P4112`)
Given two strings $A, B$ with $|A|, |B| \le 2000$ over $\Sigma = \{\text{`a'}, \dots, \text{`z'}\}$, we must find the minimum length of a string $W \in \Sigma^+$ across **four combinations** of recognizers:

| Subproblem | Condition on $W$ in $A$ | Condition on $W$ in $B$ | Automaton $\mathcal{M}_A$ for $A$ | Automaton $\mathcal{M}_B$ for $B$ |
| :--- | :--- | :--- | :--- | :--- |
| **(1)** | **Substring** of $A$ | Not a **Substring** of $B$ | $\text{SAM}(A)$ | $\text{SAM}(B)$ |
| **(2)** | **Substring** of $A$ | Not a **Subsequence** of $B$ | $\text{SAM}(A)$ | $\text{DASG}(B)$ |
| **(3)** | **Subsequence** of $A$ | Not a **Substring** of $B$ | $\text{DASG}(A)$ | $\text{SAM}(B)$ |
| **(4)** | **Subsequence** of $A$ | Not a **Subsequence** of $B$ | $\text{DASG}(A)$ | $\text{DASG}(B)$ |

**Unified Product-Automaton Formulation**:
Both $\text{SAM}(X)$ and $\text{DASG}(X)$ are deterministic incomplete DFAs $\mathcal{M}_X = (Q_X, \Sigma, \delta_X, q_{X, 0})$ with $|Q_X| \le 2|X| + 1$ such that:
$$\mathcal{L}(\mathcal{M}_X) = \{ W \in \Sigma^* \mid \delta_X^*(q_{X,0}, W) \ne \perp \}$$
is the exact set of all substrings (for SAM) or all subsequences (for DASG) of $X$.
Therefore, a word $W \in \Sigma^+$ belongs to $\mathcal{L}(\mathcal{M}_A) \setminus \mathcal{L}(\mathcal{M}_B)$ if and only if in the product automaton $\mathcal{M}_A \times \mathcal{M}_B$:
1. Starting from $(q_{A,0}, q_{B,0})$, there is a path $W = c_1 \dots c_{L-1}$ of length $L - 1$ to a reachable product state $(u, v) \in Q_A \times Q_B$ (meaning $W \in \mathcal{L}(\mathcal{M}_A) \cap \mathcal{L}(\mathcal{M}_B)$), and
2. From $(u, v)$, there exists a character $c \in \Sigma$ such that $\delta_A(u, c) \ne \perp$ (so $W \cdot c \in \mathcal{L}(\mathcal{M}_A)$) while $\delta_B(v, c) = \perp$ (so $W \cdot c \notin \mathcal{L}(\mathcal{M}_B)$)!

Running a single unweighted **BFS** over product states $(u, v) \in Q_A \times Q_B$ solves each of the four subproblems in $O(|Q_A| \cdot |Q_B| \cdot |\Sigma|) = O(|A| \cdot |B| \cdot |\Sigma|)$ time!
*(Bonus Structural Shortcut for Subproblem (1) & (3)*: For Subproblem (1), we do not even need product BFS—for every node $u \in \text{SAM}(A)$, all strings in $u$ of length $> \text{max\_match}_B(u)$ are absent in $B$; however, the unified product BFS handles all 4 tasks with identical 20-line logic when $|A|, |B| \le 2000$.)

##### Hand-Checkable Example: Product Automaton on $A = \text{"aba"}$, $B = \text{"ab"}$ over $\Sigma = \{\text{a, b}\}$
- $\text{DASG}(A)$ has states $\{0, 1, 2, 3\}$ with $\text{nxt}_A[0] = (\text{a}\to 1, \text{b}\to 2)$, $\text{nxt}_A[1] = (\text{a}\to 3, \text{b}\to 2)$, $\text{nxt}_A[2] = (\text{a}\to 3, \text{b}\to \perp)$, $\text{nxt}_A[3] = (\perp, \perp)$.
- $\text{DASG}(B)$ has states $\{0, 1, 2\}$ with $\text{nxt}_B[0] = (\text{a}\to 1, \text{b}\to 2)$, $\text{nxt}_B[1] = (\text{a}\to \perp, \text{b}\to 2)$, $\text{nxt}_B[2] = (\perp, \perp)$.
- Starting at $(0, 0)$ at distance $0$:
  - On `'a'`: transitions to $(1, 1)$ at distance $1$. From $(1, 1)$, reading `'a'` gives $\text{nxt}_A[1][\text{a}] = 3 \ne \perp$ while $\text{nxt}_B[1][\text{a}] = \perp$! Thus $W = \text{"aa"}$ of length $2$ is a subsequence of $A$ (`a_a`) and not a subsequence of $B$.

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples
1. **Confusing SAM Match-Link Resets with Product-Automaton Transitions**: When checking if a string is a substring of $B$ via $\text{SAM}(B)$, a naive coder might try to take suffix links `link[v]` when $\delta_B(v, c) = \perp$ (as in LCS streaming). **Fatal bug**: Taking `link[v]` drops a prefix of $W$, checking whether a *suffix* of $W \cdot c$ is in $B$, whereas we require the **entire** candidate string $W \cdot c$ to be a substring of $B$! In the product automaton, $\delta_B$ must use **pure forward DAG transitions** (never suffix links).
2. **Off-by-One Indexing Between 1-Indexed SAM Root (`root = 1`) and 0-Indexed DASG Root (`root = 0`)**: In standard implementations, SAM uses `1` as root and `0` as dead state $\perp$, whereas DASG often uses `0` as root (before index $1$) and $N+1$ or $-1$ as dead state $\perp$. Mixing the dead-state sentinel `0` across SAM and DASG causes state $0$ of DASG to be treated as $\perp$ and immediately terminates BFS at step $0$. Always normalize both automata to 1-indexed states `1 .. tot` with `0` strictly reserved for $\perp$.
3. **Exponential Overflow in $K$-th Subsequence Counting**: On DASG, $dp[i]$ can reach $2^N$. In $K$-th subsequence problems ($K \le 10^{18}$), failing to clamp $dp[i] = \min(K + 1, \sum dp[\text{nxt}[i][c]])$ causes 64-bit signed/unsigned wrap-around, corrupting the comparison $K > dp[\text{nxt}[i][c]]$.

---

## Iteration 89: Invertible Subsequence Automaton Matrices (`子序列 DP 矩阵可逆性`) & Range Subsequence Algebra

### 89.1 The 4-Step Derivation of Invertible Subsequence DP Matrices

#### Step 1: The Diagnostic Signal (Why Segment Trees of $(|\Sigma|+1)\times(|\Sigma|+1)$ Matrices TLE)
Suppose we are given a static string $S[1..N]$ over alphabet $\Sigma$ of size $\sigma = |\Sigma|$ (e.g., $\sigma = 26$ or $\sigma = 10$) and $Q$ range queries $[l, r]$ ($N, Q \le 2 \cdot 10^5$ or $10^6$), each asking for:
- The number of **distinct subsequences** of the substring $S[l..r]$ modulo $10^9 + 7$, or
- The count of subsequences of $S[l..r]$ weighted by character values or subject to forbidden/target subsequence structures.

Why do standard approaches fail?
- Running the $O(N)$ distinct subsequence DP from scratch per query takes $O(NQ)$ time.
- Building a Segment Tree over $[1, N]$ where each node stores a $(\sigma + 1) \times (\sigma + 1)$ transition matrix requires $O(N \sigma^3)$ preprocessing and $O(Q \sigma^2 \log N)$ (using vector-matrix multiplication down the segment tree) or $O(Q \sigma^3 \log N)$ time—for $\sigma = 26, N, Q = 2 \cdot 10^5$, $26^3 \approx 17{,}576$, which is far too slow and memory-heavy!
- **The Key Question**: Can we eliminate the Segment Tree entirely and answer each range query $[l, r]$ in $O(\sigma)$ or $O(\sigma^2)$ time using **prefix matrix products** $P_r = M_{S[1]} \cdots M_{S[r]}$ and their **exact matrix inverses** $P_{l-1}^{-1}$?

#### Step 2: The Combinatorial Word Invariant (Why the Distinct-Subsequence Transition Matrix Has Determinant $1$)

At first glance, many programmers believe the distinct-subsequence DP transition is **not invertible** because in the recurrence:
$$\text{Way 1 (Naive overwrite)}: \quad dp_{new}[c] \leftarrow 1 + \sum_{a \in \Sigma} dp_{old}[a]$$
it looks as if $dp_{old}[c]$ is overwritten!
**Look closer at the sum on the right-hand side**: the term $dp_{old}[c]$ is **included** inside $\sum_{a \in \Sigma} dp_{old}[a]$!
Let us verify this both combinatorially and algebraically.

##### Theorem 89.1 (Bijective Non-Destructive Partition of Distinct Subsequences)
For any string $T \in \Sigma^*$, partition the set $\text{Subseq}(T)$ of all distinct subsequences of $T$ into $\sigma + 1$ disjoint buckets:
- For each $a \in \Sigma$, let $W_a(T)$ be the set of distinct non-empty subsequences of $T$ whose **last character** is $a$, with size $w_a(T) = |W_a(T)|$.
- Let $W_\epsilon(T) = \{\epsilon\}$ be the singleton set containing the empty subsequence, with size $w_\epsilon(T) = 1$.

When a single character $c \in \Sigma$ is appended to $T$ to form $T \cdot c$:
1. For every $a \ne c$, no new subsequence ending in $a$ can be formed, so $W_a(T \cdot c) = W_a(T)$ and $w_a(T \cdot c) = w_a(T)$.
2. Every non-empty subsequence of $T \cdot c$ ending in $c$ is of the form $u \cdot c$ where $u \in \text{Subseq}(T) = \{\epsilon\} \sqcup \bigsqcup_{a \in \Sigma} W_a(T)$. Because stripping the final character $c$ from $u \cdot c$ recovers $u$ uniquely, the map $u \mapsto u \cdot c$ is a **bijection** from $\text{Subseq}(T)$ onto $W_c(T \cdot c)$!

Therefore:
$$w_c(T \cdot c) = w_\epsilon(T) + \sum_{a \in \Sigma} w_a(T) = \mathbf{1 \cdot w_c(T)} + w_\epsilon(T) + \sum_{a \in \Sigma \setminus \{c\}} w_a(T).$$

*Proof of Invertibility & Elementary Matrix Factorization.*
Let the state vector be the column vector $\mathbf{w}(T) = \bigl(w_1(T), w_2(T), \dots, w_\sigma(T), w_\epsilon(T)\bigr)^T \in \mathbb{Z}^{\sigma + 1}$, initialized at $\mathbf{w}(\epsilon) = (0, 0, \dots, 0, 1)^T$.
Appending $c \in \{1, \dots, \sigma\}$ multiplies $\mathbf{w}(T)$ on the left by the $(\sigma + 1) \times (\sigma + 1)$ matrix:
$$M_c = I_{\sigma+1} + \mathbf{e}_c \sum_{j \in \{1, \dots, \sigma+1\} \setminus \{c\}} \mathbf{e}_j^T$$
where $\mathbf{e}_j$ is the $j$-th standard basis vector.
In plain language, $M_c$ is the identity matrix $I_{\sigma+1}$ except that **row $c$ is filled entirely with $1$s**:
$$M_c = \begin{pmatrix}
1 & \cdots & 0 & \cdots & 0 & 0 \\
\vdots & \ddots & \vdots & & \vdots & \vdots \\
1 & \cdots & \mathbf{1} & \cdots & 1 & 1 \\
\vdots & & \vdots & \ddots & \vdots & \vdots \\
0 & \cdots & 0 & \cdots & 1 & 0 \\
0 & \cdots & 0 & \cdots & 0 & 1
\end{pmatrix} \leftarrow \text{row } c.$$

Because $M_c$ is obtained from $I_{\sigma+1}$ by adding every row $j \ne c$ to row $c$, it is a product of $\sigma$ elementary row-addition matrices, so:
1. $\det(M_c) = 1$ over **any commutative ring $\mathcal{R}$** (no field division is ever required to invert $M_c$!).
2. Its exact inverse $M_c^{-1}$ simply **subtracts** every row $j \ne c$ from row $c$:
   $$M_c^{-1} = I_{\sigma+1} - \mathbf{e}_c \sum_{j \in \{1, \dots, \sigma+1\} \setminus \{c\}} \mathbf{e}_j^T,$$
   which has $1$ on all diagonal entries, $-1$ on all off-diagonal entries of row $c$, and $0$ everywhere else! $\blacksquare$

##### Corollary 89.2 (The Dual Basis: Marginal New-Subsequence Potential $d_a$)
What if we multiply on the **right** instead of the left (or consider the transpose $M_c^T$)?
Let $\mathbf{d}(T) = \mathbf{1}_{\sigma+1}^T M_{T[1]} M_{T[2]} \cdots M_{T[|T|]}$ (or take the coordinate change $d_a = \sum_{b} w_b + 1 - w_a$).
Initially $\mathbf{d}(\epsilon) = (1, 1, \dots, 1, 1)^T$ (or with last coordinate $0$ for non-empty count). When character $c$ is read, multiplying by $M_c$ on the right adds **column $c$ to every other column $j \ne c$**:
$$d_{c, \text{new}} = d_{c, \text{old}}, \qquad d_{j, \text{new}} = d_{j, \text{old}} + d_{c, \text{old}} \quad (\forall j \ne c).$$
Combinatorially, $d_a(T)$ is the number of distinct subsequences of $T$ formed **since the last occurrence of $a$**—i.e., the exact marginal increase in total distinct subsequences if character $a$ were appended next!

#### Step 3: The Reverse-Engineering Scratchpad ($O(N \sigma + Q \sigma)$ Range Distinct Subsequences)

Suppose we want to compute the number of distinct subsequences of $S[l..r]$ for $Q$ queries $[l, r]$.
Let us assemble the prefix matrix product and its inverse so that **neither preprocessing nor querying ever touches an explicit $(\sigma+1)\times(\sigma+1)$ matrix in $O(\sigma^2)$ time per step**!

##### 1. Matrix Associativity Equation for $S[l..r]$
For a substring $S[l..r]$, the state vector produced by feeding $S[l..r]$ into an initially empty automaton is:
$$\mathbf{w}(S[l..r]) = M_{S[r]} M_{S[r-1]} \cdots M_{S[l]} \mathbf{e}_{\sigma+1}$$
and the total number of distinct subsequences of $S[l..r]$ (including $\epsilon$) is:
$$\text{Ans}(l, r) = \mathbf{1}^T \cdot \bigl(M_{S[r]} \cdots M_{S[l]}\bigr) \cdot \mathbf{e}_{\sigma+1}.$$
Define the prefix product from the right:
$$P_i = M_{S[i]} M_{S[i-1]} \cdots M_{S[1]} \qquad (P_0 = I_{\sigma+1}).$$
Then:
$$M_{S[r]} \cdots M_{S[l]} = P_r P_{l-1}^{-1}, \qquad P_{l-1}^{-1} = M_{S[1]}^{-1} M_{S[2]}^{-1} \cdots M_{S[l-1]}^{-1}.$$
Thus:
$$\text{Ans}(l, r) = \underbrace{\bigl(\mathbf{1}^T P_r\bigr)}_{\text{row vector } \mathbf{u}_r^T \in \mathcal{R}^{1 \times (\sigma+1)}} \cdot \underbrace{\bigl(P_{l-1}^{-1} \mathbf{e}_{\sigma+1}\bigr)}_{\text{column vector } \mathbf{v}_{l-1} \in \mathcal{R}^{(\sigma+1) \times 1}} = \sum_{k=1}^{\sigma+1} u_r[k] \cdot v_{l-1}[k]!$$

Look at what just happened:
- Instead of storing the full $(\sigma+1)\times(\sigma+1)$ matrices $P_r$ and $P_{l-1}^{-1}$ (which would take $O(N \sigma^2)$ space and $O(\sigma^2)$ per query if we wanted arbitrary entries), **the query only needs the row vector $\mathbf{u}_r^T = \mathbf{1}^T P_r$ at the right endpoint $r$ and the single column vector $\mathbf{v}_{l-1} = P_{l-1}^{-1} \mathbf{e}_{\sigma+1}$ at the left endpoint $l - 1$**!
- Can we maintain $\mathbf{u}_i^T = \mathbf{u}_{i-1}^T \dots$? Wait: $P_i = M_{S[i]} P_{i-1}$ multiplies $M_{S[i]}$ on the **left** of $P_{i-1}$, whereas $P_i^{-1} = P_{i-1}^{-1} M_{S[i]}^{-1}$ multiplies $M_{S[i]}^{-1}$ on the **right** of $P_{i-1}^{-1}$!
  Wait—if we reverse the multiplication order by defining:
  $$\widetilde{P}_i = M_{S[1]} M_{S[2]} \cdots M_{S[i]}, \qquad \widetilde{P}_i^{-1} = M_{S[i]}^{-1} \cdots M_{S[1]}^{-1},$$
  let us check whether we should index left-to-right or right-to-left:
  In Theorem 89.1, reading $S[l]$, then $S[l+1]$, ..., then $S[r]$ applies $M_{S[l]}$ first, then $M_{S[l+1]}$, ..., and finally $M_{S[r]}$ on the left:
  $$\mathbf{w}(S[l..r]) = M_{S[r]} \cdots M_{S[l]} \mathbf{e}_{\sigma+1}.$$
  If instead we use the transpose (or read $S[l..r]$ into row vectors from left to right: $\mathbf{x}_{new}^T = \mathbf{x}_{old}^T M_{S[i]}^T$), then:
  $$\text{Ans}(l, r) = \mathbf{e}_{\sigma+1}^T \cdot \bigl(M_{S[l]}^T M_{S[l+1]}^T \cdots M_{S[r]}^T\bigr) \cdot \mathbf{1} = \mathbf{e}_{\sigma+1}^T \widetilde{P}_{l-1}^{-1} \widetilde{P}_r \mathbf{1}.$$
  Let us track **how fast** we can maintain the full matrices $\widetilde{P}_i = \widetilde{P}_{i-1} M_{S[i]}^T$ and $\widetilde{P}_i^{-1} = (M_{S[i]}^T)^{-1} \widetilde{P}_{i-1}^{-1}$ as $i$ goes from $1$ to $N$:
  1. Multiplying $\widetilde{P}_{i-1}$ on the right by $M_c^T$ only modifies **column $c$** of $\widetilde{P}$ (setting column $c$ to the sum of all columns of $\widetilde{P}_{i-1}$)! Maintaining the row sums of $\widetilde{P}$ allows updating column $c$ in $O(\sigma)$ time!
  2. Multiplying $\widetilde{P}_{i-1}^{-1}$ on the left by $(M_c^T)^{-1} = (M_c^{-1})^T$ adds $(-1) \times (\text{row } c)$ to **every other row** $j \ne c$ of $\widetilde{P}_{i-1}^{-1}$! By maintaining a lazy global row-offset or simply noting that only row $c$ is read and subtracted from other rows, even a direct update takes $O(\sigma^2)$ time per step (or $O(\sigma)$ with a global lazy offset vector!).
  3. And at query time $[l, r]$:
     - If we want the **entire state vector** $\mathbf{w}(S[l..r]) = P_r P_{l-1}^{-1} \mathbf{e}_{\sigma+1}$, we first extract the column vector $\mathbf{v} = P_{l-1}^{-1} \mathbf{e}_{\sigma+1}$ in $O(\sigma)$ time, and then multiply $P_r \cdot \mathbf{v}$ in $O(\sigma^2)$ time—or if we only need the scalar $\mathbf{1}^T P_r P_{l-1}^{-1} \mathbf{e}_{\sigma+1}$, we take the dot product of the precomputed row vector $\mathbf{u}_r^T = \mathbf{1}^T P_r$ with the precomputed column vector $\mathbf{v}_{l-1} = P_{l-1}^{-1} \mathbf{e}_{\sigma+1}$ in **$O(\sigma)$ time per query**!

Let us verify this $O(N\sigma + Q\sigma)$ bound!
Wait: can we really precompute both $\mathbf{u}_r^T = \mathbf{1}^T P_r$ AND $\mathbf{v}_{l-1} = P_{l-1}^{-1} \mathbf{e}_{\sigma+1}$ for all $0 \le i \le N$ in $O(N \sigma)$ total time and space?!
Let's check!
- Remember $P_i = M_{S[i]} M_{S[i-1]} \cdots M_{S[1]}$, so $P_i$ grows on the **left** ($P_i = M_{S[i]} P_{i-1}$), whereas $P_i^{-1} = M_{S[1]}^{-1} \cdots M_{S[i]}^{-1}$ grows on the **right** ($P_i^{-1} = P_{i-1}^{-1} M_{S[i]}^{-1}$)!
- Because $P_i = M_{S[i]} P_{i-1}$, the matrix $P_i$ differs from $P_{i-1}$ **only in row $c = S[i]$**: specifically, row $c$ of $P_i$ becomes the column-wise sum of all rows of $P_{i-1}$, which is literally $\mathbf{u}_{i-1}^T = \mathbf{1}^T P_{i-1}$!
  Wait: Look at that identity:
  $$\text{Row } c \text{ of } P_i = \mathbf{1}^T P_{i-1} = \mathbf{u}_{i-1}^T!$$
  And therefore, the new sum of all rows of $P_i$ is:
  $$\mathbf{u}_i^T = \mathbf{u}_{i-1}^T - (\text{Row } c \text{ of } P_{i-1}) + \mathbf{u}_{i-1}^T = 2 \mathbf{u}_{i-1}^T - \mathbf{u}_{\text{last}[c] - 1}^T!$$
  **WHAT A MIRACLE!** Let's double check that!
  Because Row $c$ of $P_{i-1}$ was last updated at the previous occurrence $\text{last}[c]$ of character $c$, at which time it was set to $\mathbf{u}_{\text{last}[c]-1}^T$!
  So $\mathbf{u}_i^T = \mathbf{1}^T P_i$ satisfies the exact vector recurrence:
  $$\mathbf{u}_i^T = 2 \mathbf{u}_{i-1}^T - \mathbf{u}_{\text{last}[S[i]] - 1}^T!$$
  Wait: we don't even need the $(\sigma+1)$-dimensional vector if we track the scalar sequence! Wait—even better: what about $\mathbf{v}_i = P_i^{-1} \mathbf{e}_{\sigma+1}$?
  Let's check how $P_i^{-1}$ updates! Since $P_i^{-1} = P_{i-1}^{-1} M_{S[i]}^{-1}$, multiplying on the right by $M_c^{-1}$ replaces every column $j \ne c$ of $P_{i-1}^{-1}$ by $(\text{col } j) - (\text{col } c)$, while keeping column $c$ unchanged!
  Wait: That means the columns of $P_i^{-1}$ update just like Corollary 89.2 in reverse:
  Let $\mathbf{c}_j^{(i)}$ be column $j$ of $P_i^{-1}$. Wait: each column of $P_i^{-1}$ is a $(\sigma+1)$-vector, OR notice that in $\text{Ans}(l, r) = \mathbf{1}^T P_r P_{l-1}^{-1} \mathbf{e}_{\sigma+1}$:
  Instead of expanding $\mathbf{u}_r^T$ as a $(\sigma+1)$-vector, write:
  $$\text{Ans}(l, r) = \underbrace{\bigl(\mathbf{1}^T P_r\bigr)}_{1 \times (\sigma+1)} \cdot \underbrace{\bigl(P_{l-1}^{-1} \mathbf{e}_{\sigma+1}\bigr)}_{(\sigma+1) \times 1}.$$
  Since $\mathbf{u}_r^T = \mathbf{1}^T P_r$ is a single $1 \times (\sigma+1)$ row vector that satisfies $\mathbf{u}_i^T = 2\mathbf{u}_{i-1}^T - \mathbf{u}_{\text{last}[S[i]]-1}^T$ (taking $O(\sigma)$ time and space per step $i$), what about $\mathbf{v}_i = P_i^{-1} \mathbf{e}_{\sigma+1}$?
  Wait: to know column $\sigma+1$ of $P_i^{-1}$, since $P_i^{-1} = P_{i-1}^{-1} M_c^{-1}$ subtracts column $c$ from all other columns (including column $\sigma+1$), we only need to know **what column $c$ of $P_{i-1}^{-1}$ is**? No, wait: instead of tracking whole columns of $P_i^{-1}$, look at $P_i^{-1}$ acting on the row vector $\mathbf{e}_{\sigma+1}^T$ or column vector $\mathbf{e}_{\sigma+1}$:
  In $P_i = M_{S[i]} P_{i-1}$, we only modified **row $c$** of $P_{i-1}$.
  What about $P_i^{-1} = P_{i-1}^{-1} M_{S[i]}^{-1}$?
  If we track the single column vector $\mathbf{v}_i = P_i^{-1} \mathbf{e}_{\sigma+1}$? No, $M_{S[i]}^{-1}$ is on the **right** of $P_{i-1}^{-1}$, right in front of $\mathbf{e}_{\sigma+1}$!
  Because $M_{S[i]}^{-1}$ is on the right of $P_{i-1}^{-1}$, we can't just apply $M_{S[i]}^{-1}$ to $\mathbf{v}_{i-1} = P_{i-1}^{-1} \mathbf{e}_{\sigma+1}$.
  Instead, which vector CAN we update by left-multiplication by $M_{S[i]}^{-1}$, or right-multiplication by $M_{S[i]}^{-1}$?
  **Any row vector $\mathbf{r}_{i}^T = \mathbf{r}_{i-1}^T M_{S[i]}^{-1}$**!
  Because for ANY row vector $\mathbf{r}^T = (r_1, \dots, r_\sigma, r_{\sigma+1})$, multiplying on the right by $M_c^{-1}$ only changes **all coordinates $j \ne c$ by subtracting $r_c$**:
  $$\bigl(\mathbf{r}^T M_c^{-1}\bigr)_j = \begin{cases} r_c & \text{if } j = c, \\ r_j - r_c & \text{if } j \ne c! \end{cases}$$
  AND simultaneously, for ANY column vector $\mathbf{w}_i = M_{S[i]} \mathbf{w}_{i-1}$, multiplying on the left by $M_c$ only changes **coordinate $c$** by setting it to $\sum_{j=1}^{\sigma+1} w_j$:
  $$\bigl(M_c \mathbf{w}\bigr)_j = \begin{cases} \sum_{k=1}^{\sigma+1} w_k & \text{if } j = c, \\ w_j & \text{if } j \ne c! \end{cases}$$

Let us pause and admire the symmetry we just uncovered:
- **Left-multiplying a column vector by $M_c$** ($M_c \mathbf{w}$) takes $O(\sigma)$ time (or $O(1)$ time if we maintain the sum of coordinates!).
- **Right-multiplying a row vector by $M_c^{-1}$** ($\mathbf{r}^T M_c^{-1}$) ALSO takes $O(\sigma)$ time (or $O(1)$ time with a global lazy offset)!
- Wait: in $\text{Ans}(l, r) = \mathbf{1}^T P_r P_{l-1}^{-1} \mathbf{e}_{\sigma+1}$, the matrix $P_r$ is on the **left** and $P_{l-1}^{-1}$ is on the **right**!
- What if we instead write the identity in reverse order by reading the string or transposing?
  Wait: why is $P_r$ on the left of $P_{l-1}^{-1}$? Because $M_{S[r]} \cdots M_{S[l]} = (M_{S[r]} \cdots M_{S[1]}) (M_{S[l-1]} \cdots M_{S[1]})^{-1} = P_r P_{l-1}^{-1}$.
  Can we ALSO write $M_{S[r]} \cdots M_{S[l]}$ using **suffix products** or **left-to-right products**?
  Suppose we read $S[l..r]$ from right to left vs left to right: the number of distinct subsequences of $S[l..r]$ is equal to the number of distinct subsequences of $(S[l..r])^R$, or even directly without reversing:
  In Theorem 89.1, if we partition distinct subsequences of $S[l..r]$ by their **first** character instead of their **last** character, then:
  $$\text{Ans}(l, r) = \mathbf{e}_{\sigma+1}^T \cdot \bigl(M_{S[l]}^T M_{S[l+1]}^T \cdots M_{S[r]}^T\bigr) \cdot \mathbf{1}.$$
  Here, let $Q_i = M_{S[1]}^T M_{S[2]}^T \cdots M_{S[i]}^T$. Then:
  $$M_{S[l]}^T \cdots M_{S[r]}^T = Q_{l-1}^{-1} Q_r!$$
  Now substitute $Q_{l-1}^{-1} Q_r$ into $\text{Ans}(l, r)$:
  $$\text{Ans}(l, r) = \underbrace{\bigl(\mathbf{e}_{\sigma+1}^T Q_{l-1}^{-1}\bigr)}_{\text{row vector } \mathbf{a}_{l-1}^T} \cdot \underbrace{\bigl(Q_r \mathbf{1}\bigr)}_{\text{column vector } \mathbf{b}_r}!$$
  Wait: how does $\mathbf{a}_i^T = \mathbf{e}_{\sigma+1}^T Q_i^{-1}$ evolve when $i \to i+1$?
  Since $Q_i^{-1} = (M_{S[i]}^T)^{-1} Q_{i-1}^{-1}$, $Q_i^{-1}$ grows on the **left**, whereas $Q_i = Q_{i-1} M_{S[i]}^T$ grows on the **right**!
  In BOTH cases, one side is a $1 \times (\sigma+1)$ row vector and the other is a $(\sigma+1) \times 1$ column vector, and how fast can we compute $\mathbf{u}_i^T = \mathbf{1}^T P_i$ and $\mathbf{v}_i = P_i^{-1} \mathbf{e}_{\sigma+1}$ for all $i = 0, \dots, N$?
  Let's check BOTH $\mathbf{u}_i^T = \mathbf{1}^T P_i$ and $\mathbf{v}_i = P_i^{-1} \mathbf{e}_{\sigma+1}$!
  1. Earlier we proved that because $P_i = M_{S[i]} P_{i-1}$ replaces row $c = S[i]$ of $P_{i-1}$ with $\mathbf{1}^T P_{i-1} = \mathbf{u}_{i-1}^T$, the row vector $\mathbf{u}_i^T = \mathbf{1}^T P_i$ satisfies:
     $$\mathbf{u}_i^T = 2 \mathbf{u}_{i-1}^T - \mathbf{u}_{\text{last}[S[i]] - 1}^T.$$
     Wait: how long does it take to compute $\mathbf{u}_i^T$ from $\mathbf{u}_{i-1}^T$ and $\mathbf{u}_{\text{last}[S[i]] - 1}^T$?
     Just **$O(\sigma)$ time** (subtracting two vectors of length $\sigma + 1$)! We don't need to maintain $P_i$ at all!
  2. Now what about $\mathbf{v}_i = P_i^{-1} \mathbf{e}_{\sigma+1}$?
     Since $P_i^{-1} = P_{i-1}^{-1} M_{S[i]}^{-1}$, let $\mathbf{c}_k^{(i)}$ denote the $k$-th column of $P_i^{-1}$.
     When $M_c^{-1}$ is multiplied on the right of $P_{i-1}^{-1}$, what happens to the columns of $P_{i-1}^{-1}$?
     - Column $c$ is unchanged: $\mathbf{c}_c^{(i)} = \mathbf{c}_c^{(i-1)}$.
     - Every other column $k \ne c$ has column $c$ subtracted from it: $\mathbf{c}_k^{(i)} = \mathbf{c}_k^{(i-1)} - \mathbf{c}_c^{(i-1)}$!
     Wait: notice that **every single column $k \ne c$ receives the exact same subtraction $-\mathbf{c}_c^{(i-1)}$**!
     Let us verify that!
     If you have $\sigma + 1$ columns $\mathbf{c}_1, \dots, \mathbf{c}_{\sigma+1}$, and at step $i$ (with $c = S[i]$) you subtract $\mathbf{c}_c$ from **all other $\sigma$ columns**, that is equivalent to:
     - Subtracting $\mathbf{c}_c$ from a **single global offset vector** $\mathbf{g}$ (so $\mathbf{g} \leftarrow \mathbf{g} - \mathbf{c}_c^{\text{actual}}$), and
     - Adding $\mathbf{c}_c^{\text{actual}}$ to stored column $c$ so that column $c$'s actual value remains unchanged!
     Specifically, write each column $k$ as $\mathbf{c}_k^{(i)} = \tilde{\mathbf{c}}_k^{(i)} + \mathbf{g}^{(i)}$.
     At $i = 0$, $P_0^{-1} = I_{\sigma+1}$, so $\mathbf{g}^{(0)} = \mathbf{0}$ and $\tilde{\mathbf{c}}_k^{(0)} = \mathbf{e}_k$.
     At step $i$ with character $c = S[i]$:
     - Read the actual column $c$: $\mathbf{w} = \tilde{\mathbf{c}}_c^{(i-1)} + \mathbf{g}^{(i-1)}$ in $O(\sigma)$ time.
     - Subtract $\mathbf{w}$ from all columns by setting $\mathbf{g}^{(i)} = \mathbf{g}^{(i-1)} - \mathbf{w}$ in $O(\sigma)$ time.
     - Restore column $c$ by setting $\tilde{\mathbf{c}}_c^{(i)} = \tilde{\mathbf{c}}_c^{(i-1)} + \mathbf{w} = 2\tilde{\mathbf{c}}_c^{(i-1)} + \mathbf{g}^{(i-1)}$ in $O(\sigma)$ time!
     - And the vector we want to record for left-endpoints is simply the $(\sigma+1)$-th column:
       $$\mathbf{v}_i = \mathbf{c}_{\sigma+1}^{(i)} = \mathbf{e}_{\sigma+1} + \mathbf{g}^{(i)}!$$

##### Theorem 89.3 (The Complete $O((N + Q)\sigma)$ Prefix-Matrix Algorithm for Range Distinct Subsequences)
For any string $S[1..N]$ over an alphabet of size $\sigma$, we can precompute both:
1. $\mathbf{u}_i^T = \mathbf{1}^T P_i \in \mathcal{R}^{1 \times (\sigma+1)}$ for all $0 \le i \le N$, and
2. $\mathbf{v}_i = P_i^{-1} \mathbf{e}_{\sigma+1} \in \mathcal{R}^{(\sigma+1) \times 1}$ for all $0 \le i \le N$

in **$O(N \sigma)$ total time and $O(N \sigma)$ space** (not $O(N\sigma^2)$!), and answer every range distinct subsequence query $[l, r]$ in **$O(\sigma)$ time** via the single dot product:
$$\text{Ans}(l, r) = \mathbf{u}_r^T \cdot \mathbf{v}_{l-1} = \sum_{k=1}^{\sigma+1} u_r[k] \cdot v_{l-1}[k].$$

##### Hand-Checkable Example: $S = \text{"aba"}$ over $\Sigma = \{\text{a}=1, \text{b}=2\}$ ($\sigma = 2$, dimension $3$)
Let us trace $\mathbf{u}_i^T$ and $\mathbf{v}_i$ by hand for $S = \text{"aba"}$:
- **Initialization ($i = 0$)**:
  - $P_0 = I_3 \implies \mathbf{u}_0^T = (1, 1, 1)$.
  - $P_0^{-1} = I_3 \implies \mathbf{c}_1^{(0)} = (1,0,0)^T, \mathbf{c}_2^{(0)} = (0,1,0)^T, \mathbf{c}_3^{(0)} = (0,0,1)^T$, so $\mathbf{v}_0 = (0, 0, 1)^T$.
- **Step $i = 1$ ($S[1] = \text{'a'} = 1$)**:
  - Row $1$ of $P_1$ becomes $\mathbf{u}_0^T = (1, 1, 1)$, so $\mathbf{u}_1^T = 2\mathbf{u}_0^T - (\text{row } 1 \text{ of } P_0) = 2(1,1,1) - (1,0,0) = (1, 2, 2)$.
  - In $P_1^{-1}$, subtract $\mathbf{c}_1^{(0)} = (1,0,0)^T$ from columns $2$ and $3$:
    $\mathbf{c}_1^{(1)} = (1,0,0)^T$, $\mathbf{c}_2^{(1)} = (-1,1,0)^T$, $\mathbf{c}_3^{(1)} = (-1,0,1)^T \implies \mathbf{v}_1 = (-1, 0, 1)^T$.
- **Step $i = 2$ ($S[2] = \text{'b'} = 2$)**:
  - Row $2$ of $P_2$ becomes $\mathbf{u}_1^T = (1, 2, 2)$, so $\mathbf{u}_2^T = 2\mathbf{u}_1^T - (\text{row } 2 \text{ of } P_1) = 2(1,2,2) - (0,1,0) = (2, 3, 4)$.
  - In $P_2^{-1}$, subtract $\mathbf{c}_2^{(1)} = (-1,1,0)^T$ from columns $1$ and $3$:
    $\mathbf{c}_1^{(2)} = (2,-1,0)^T$, $\mathbf{c}_2^{(2)} = (-1,1,0)^T$, $\mathbf{c}_3^{(2)} = (0,-1,1)^T \implies \mathbf{v}_2 = (0, -1, 1)^T$.
- **Step $i = 3$ ($S[3] = \text{'a'} = 1$)**:
  - Row $1$ of $P_3$ becomes $\mathbf{u}_2^T = (2, 3, 4)$, replacing row $1$ of $P_2$ which was $\mathbf{u}_0^T = (1, 1, 1)$:
    $\mathbf{u}_3^T = 2\mathbf{u}_2^T - \mathbf{u}_0^T = 2(2,3,4) - (1,1,1) = (3, 5, 7)$.
- **Query Check**:
  1. $S[1..3] = \text{"aba"}$: $\mathbf{u}_3^T \cdot \mathbf{v}_0 = (3, 5, 7) \cdot (0, 0, 1)^T = 7$ (subsequences: $\epsilon, \text{a}, \text{b}, \text{ab}, \text{ba}, \text{aa}, \text{aba}$ — indeed $7$!).
  2. $S[2..3] = \text{"ba"}$: $\mathbf{u}_3^T \cdot \mathbf{v}_1 = (3, 5, 7) \cdot (-1, 0, 1)^T = -3 + 0 + 7 = 4$ (subsequences: $\epsilon, \text{b}, \text{a}, \text{ba}$ — indeed $4$!).
  3. $S[3..3] = \text{"a"}$: $\mathbf{u}_3^T \cdot \mathbf{v}_2 = (3, 5, 7) \cdot (0, -1, 1)^T = 0 - 5 + 7 = 2$ (subsequences: $\epsilon, \text{a}$ — indeed $2$!).

#### Step 4: Boundary Pitfalls, Non-Adjacent Extensions (`ABC 214F`), and Broken-Invariant Counterexamples
1. **When the Matrix Is Only Invertible Over a Ring vs. Singular (`CF 750E`)**:
   - For **counting** subsequences modulo $M$, $M_c$ is over the commutative ring $(\mathbb{Z}/M\mathbb{Z}, +, \times)$ and has $\det(M_c) = 1$, so $M_c^{-1}$ always exists.
   - For **min-plus / tropical DP** (such as `CF 750E — New Year and Old Subsequence`, where we find the minimum characters to delete so `"2017"` is a subsequence and `"2016"` is not), the tropical semiring $(\mathbb{Z} \cup \{\infty\}, \min, +)$ has **no additive inverses**! You **cannot** invert a tropical matrix; `CF 750E` must use a Segment Tree of $5 \times 5$ tropical matrices in $O((N + Q \log N) \cdot 5^3)$ time. Never attempt prefix-matrix inversion on $(\min, +)$ or $(\max, +)$ semirings!
2. **Non-Adjacent Distinct Subsequences (`AtCoder ABC 214 F — Substrings`)**:
   What if two chosen indices in $S$ cannot be adjacent ($i_{k+1} \ge i_k + 2$)?
   - Let $S_i$ be the total number of valid non-adjacent subsequences chosen from $S[1..i]$ (with $S_0 = 1$ for $\epsilon$, $S_{-1} = 0$).
   - When considering $c = S[i]$, any new subsequence ending at $c$ must extend a valid subsequence from $S[1..i-2]$ (counted by $S_{i-2}$), minus those already formed at the previous occurrence $\text{last}[c]$ (which extended $S[1..\text{last}[c]-2]$):
     $$dp[i] = S_{i-2} \quad \text{and} \quad S_i = S_{i-1} + S_{i-2} - S_{\text{last}[c]-2}$$
     (where if $\text{last}[c] = 0$, the subtracted term is $0$, and if $\text{last}[c] = 1$, we subtract $1$ for the single-character subsequence `"c"` already created at index $1$!).
   - **Pitfall**: At $\text{last}[c] = 1$, index $\text{last}[c] - 2 = -1$, where $S_{-1}$ would be $0$ if unadjusted, forgetting that index $1$ already created the single-character subsequence $c$ (from $\epsilon$)! Fixing $S_{-1} = 1$ ONLY for the single-character creation at $i = 1$ (or tracking $dp[i]$ as the number of *newly* created subsequences at $i$, so $dp[i] = \sum_{j=\max(0, \text{last}[c]-1)}^{i-2} dp[j]$) prevents this classic off-by-one bug.

---

## Iteration 90: Tiskin's Seaweed Matrices (`海草矩阵` / Unit-Monge Braid Multiplication) & All-Pairs Interval LCS (`区间 LCS`)

### 90.1 The 4-Step Derivation of Tiskin's Seaweed Matrices & Unit-Monge Algebra

#### Step 1: The Diagnostic Signal (Why $O(N^2)$ DP Cannot Answer All-Pairs Interval LCS)
Given two strings $A[1..M]$ and $B[1..N]$, the **All-Pairs Interval LCS** problem (`Semi-Local LCS` / `[THUPC 2021] 区间 LCS` / `[国家集训队论文 2021 — 单位蒙日矩阵]`) asks:
- Answer $Q$ queries $(l, r)$ ($1 \le l \le r \le N$), each requesting $\text{LCS}(A[1..M], B[l..r])$, where $M, N \le 5000$ and $Q \le 10^6$ (or $M, N, Q \le 10^5$ over small/general alphabets).
- Or even more generally: compute $\text{LCS}(A, B[l..r])$ for **all $\binom{N+1}{2}$ intervals $[l, r] \subseteq [1, N]$ simultaneously** in $O(MN + N^2)$ time (instead of $O(MN^2)$)!

Why does standard LCS DP fail?
- Running Needleman–Wunsch DP from each starting point $l \in \{1, \dots, N\}$ takes $O(MN)$ per start point $l$, totaling $O(MN^2)$ time.
- Why is there only $O(N)$ (rather than $O(N^2)$) actual information in the $(N+1) \times (N+1)$ matrix of all interval answers $L(l, r) = \text{LCS}(A, B[l+1..r])$ for $0 \le l \le r \le N$?

#### Step 2: The Combinatorial Word Invariant (Planar Path Crossing, Monge Property & Permutation Cross-Differences)

##### 1. The Alignment Grid DAG
Construct the $(M+1) \times (N+1)$ alignment grid with vertices $(x, y)$ for $0 \le x \le M$ (rows, top-to-bottom) and $0 \le y \le N$ (columns, left-to-right):
- Horizontal edges $(x, y-1) \to (x, y)$ of weight $0$ (skipping $B[y]$).
- Vertical edges $(x-1, y) \to (x, y)$ of weight $0$ (skipping $A[x]$).
- Diagonal match edges $(x-1, y-1) \to (x, y)$ of weight $1$ whenever $A[x] = B[y]$.
Then for any $0 \le l \le r \le N$, the Longest Common Subsequence $\text{LCS}(A[1..M], B[l+1..r])$ is the maximum weight of a directed path from the top boundary vertex $(0, l)$ to the bottom boundary vertex $(M, r)$.

It is mathematically cleaner (following Tiskin 2008) to convert this **maximum-weight match** problem into a **minimum-weight non-match / dual grid** or directly state the **Submodular (Anti-Monge) Inequality** on $L(l, r) = \text{LCS}(A[1..M], B[l+1..r])$.

##### Theorem 90.1 (Planar Crossing / Quadrangle Inequality for Interval LCS)
For all $0 \le l < l' \le r < r' \le N$:
$$L(l, r) + L(l', r') \ge L(l, r') + L(l', r).$$
More strongly, defining the **2D unit cross-difference**:
$$\Delta(i, j) = L(i-1, j) - L(i, j) - L(i-1, j-1) + L(i, j-1) \qquad (1 \le i \le j \le N),$$
we have $\Delta(i, j) \in \{0, 1\}$ for every $1 \le i \le j \le N$, and in each row $i$ and each column $j$, there is **at most one** entry with $\Delta(i, j) = 1$!

*Proof (Planar Path Uncrossing).*
Let $P_1$ be an optimal path from $(0, l)$ to $(M, r')$ of weight $L(l, r')$, and let $P_2$ be an optimal path from $(0, l')$ to $(M, r)$ of weight $L(l', r)$.
Because $(0, l)$ lies to the left of $(0, l')$ on the top boundary $x = 0$, while $(M, r')$ lies to the right of $(M, r)$ on the bottom boundary $x = M$, and all edges move by $(\Delta x, \Delta y) \in \{(1,0), (0,1), (1,1)\}$ (no edge can jump across another path without sharing a grid vertex), by planar topology the paths $P_1$ and $P_2$ **must intersect at some grid vertex** $v = (x^*, y^*)$.
Swap the suffixes of $P_1$ and $P_2$ after $v$:
- The prefix of $P_1$ from $(0, l)$ to $v$ followed by the suffix of $P_2$ from $v$ to $(M, r)$ is a valid path from $(0, l)$ to $(M, r)$, so its weight is at most $L(l, r)$.
- The prefix of $P_2$ from $(0, l')$ to $v$ followed by the suffix of $P_1$ from $v$ to $(M, r')$ is a valid path from $(0, l')$ to $(M, r')$, so its weight is at most $L(l', r')$.
Summing these two weights preserves the exact multiset of edges of $P_1$ and $P_2$, yielding:
$$L(l, r) + L(l', r') \ge \text{wt}(P_1) + \text{wt}(P_2) = L(l, r') + L(l', r).$$
In particular, $\Delta(i, j) = \bigl(L(i-1, j) + L(i, j-1)\bigr) - \bigl(L(i, j) + L(i-1, j-1)\bigr) \ge 0$.
Furthermore, extending a substring $B[l+1..r]$ by one character changes its LCS with $A$ by at most $1$:
$$0 \le L(i-1, j) - L(i, j) \le 1 \quad \text{and} \quad 0 \le L(i, j) - L(i, j-1) \le 1.$$
Summing $\Delta(i, j)$ over $j = i, \dots, N$:
$$\sum_{j=i}^N \Delta(i, j) = \bigl(L(i-1, N) - L(i, N)\bigr) - \bigl(L(i-1, i-1) - L(i, i-1)\bigr) = \bigl(L(i-1, N) - L(i, N)\bigr) - (0 - 0) \in \{0, 1\}!$$
Since every term $\Delta(i, j) \ge 0$ is an integer and their sum across row $i$ (and similarly across column $j$) belongs to $\{0, 1\}$, we conclude that $\Delta(i, j) \in \{0, 1\}$ and every row $i$ and column $j$ contains **at most one $1$**! $\blacksquare$

##### Theorem 90.2 (Tiskin's Seaweed Comb Wiring & The $(M+N) \times (M+N)$ Permutation Matrix)
To make every row and column contain **exactly one $1$** (turning $\Delta$ into a full permutation matrix), we include the **left boundary** ($M$ horizontal entrances on the left side of the $M \times N$ cell grid, indexed $-M, -M+1, \dots, -1$) and the **top boundary** ($N$ vertical entrances at the top of the $M \times N$ cell grid, indexed $1, 2, \dots, N$), together with the $N$ bottom exits ($1, \dots, N$) and $M$ right exits ($N+1, \dots, N+M$).
Trace $M + N$ **seaweeds** (wires) through the $M \times N$ cells $(x, y) \in \{1, \dots, M\} \times \{1, \dots, N\}$ in any topological order (e.g., row by row $x = 1 \dots M$, column by column $y = 1 \dots N$). Each cell $(x, y)$ has one wire $u_{\text{left}}$ entering from its left edge and one wire $u_{\text{top}}$ entering from its top edge:

$$\text{\textbf{Tiskin's Seaweed Cell Rule at }} (x, y): \quad \begin{cases}
\text{\textbf{Avoid (Do Not Cross)}}: \text{if } A[x] = B[y] \text{ OR } u_{\text{left}} \text{ and } u_{\text{top}} \text{ have ALREADY crossed earlier}, \\
\quad \implies u_{\text{left}} \text{ exits through the BOTTOM edge, and } u_{\text{top}} \text{ exits through the RIGHT edge.} \\[6pt]
\text{\textbf{Cross}}: \text{if } A[x] \ne B[y] \text{ AND } u_{\text{left}} \text{ and } u_{\text{top}} \text{ have NOT crossed earlier}, \\
\quad \implies u_{\text{left}} \text{ exits through the RIGHT edge, and } u_{\text{top}} \text{ exits through the BOTTOM edge.}
\end{cases}$$

Since wires start in sorted order along the left-then-top boundary (left entrances have smaller initial labels than top entrances), the condition "$u_{\text{left}}$ and $u_{\text{top}}$ have NOT crossed earlier" is simply the numerical comparison **$u_{\text{left}} < u_{\text{top}}$**!
When all $M \times N$ cells are processed, each top entrance $i \in \{1, \dots, N\}$ exits either at some bottom column $p(i) \in \{1, \dots, N\}$ or at some right row $p(i) \in \{N+1, \dots, N+M\}$. Then for every interval $[l, r] \subseteq [1, N]$ ($1$-indexed substring $B[l..r]$):
$$\boxed{\text{LCS}(A[1..M], B[l..r]) = (r - l + 1) - \bigl|\bigl\{ i \in [l, r] \;\big|\; p(i) \le r \bigr\}\bigr| = \bigl|\bigl\{ i \in [l, r] \;\big|\; p(i) > r \bigr\}\bigr|!}$$

*Why does this formula hold?*
Let us verify it from Theorem 90.1!
By summing the cross-differences $\Delta(i, j)$ over the triangle $l \le i \le j \le r$:
$$L(l-1, r) = \sum_{i=l}^r \bigl(L(i-1, r) - L(i, r)\bigr).$$
Wait: in the standard comb convention where a match $A[x] = B[y]$ prevents crossing (so matched top wires are deflected to the right boundary $> N$, or equivalently in the dual formulation where unmatched wires go straight to the bottom $\le r$):
- If $A$ has no characters in common with $B[l..r]$ ($A[x] \ne B[y]$ everywhere), every top wire $i \in [l, r]$ crosses every horizontal wire and goes **straight down** to bottom exit $p(i) = i \le r$. Then $|\{i \in [l, r] \mid p(i) > r\}| = 0 = \text{LCS}$!
- Whenever a top wire $i \in [l, r]$ participates in the critical jump $L(i-1, r) - L(i, r) = 1$, it is deflected to the right of column $r$ (either exiting the bottom at some column $p(i) \in (r, N]$ or exiting the right boundary at $p(i) > N$).
- Therefore, $\Delta(i, j) = 1 \iff p(i) = j$ for $j \in (r, N]$, and $L(i-1, N) - L(i, N) = 1 \iff p(i) > N$. In both cases, **$L(i-1, r) - L(i, r) = 1 \iff p(i) > r$**!
Summing over $i = l, \dots, r$ immediately gives:
$$\text{LCS}(A[1..M], B[l..r]) = \sum_{i=l}^r [p(i) > r]! \quad \blacksquare$$

#### Step 3: The Reverse-Engineering Scratchpad ($O(MN)$ Comb Simulation, 2D Dominance Queries & $O(N \log^2 N)$ Unit-Monge Braid Multiplication)

##### 1. The $O(MN)$ Seaweed Comb Algorithm + $O(Q \log N)$ (or $O(N^2)$) Interval LCS Queries
Given $A[1..M]$ and $B[1..N]$:
1. Initialize wire labels:
   - Left boundary wires for rows $x = 1 \dots M$: `left_wire[x] = -M + x - 1` (or `x`, while top wires get `M + y` so that every left wire starts strictly smaller than every top wire!). Let us use positive integers $1 \dots M+N$:
     $$\text{row\_wire}[x] = x \quad (1 \le x \le M), \qquad \text{col\_wire}[y] = M + y \quad (1 \le y \le N).$$
     Notice that $\text{row\_wire}[x] < \text{col\_wire}[y]$ holds initially for all $x, y$!
2. Sweep $x = 1 \dots M$:
   Let $u = \text{row\_wire}[x]$ (the wire currently travelling horizontally along row $x$).
   Sweep $y = 1 \dots N$:
   Let $v = \text{col\_wire}[y]$ (the wire entering cell $(x, y)$ from the top).
   - If $A[x] \ne B[y]$ AND $u < v$: **Cross**! Wire $u$ goes to the right (so $u$ stays $u$), and wire $v$ goes down (so $\text{col\_wire}[y]$ stays $v$). Nothing changes in memory!
   - If $A[x] = B[y]$ OR $u > v$: **Avoid (Swap)**! Wire $u$ exits the bottom ($\text{col\_wire}[y] \leftarrow u$) and wire $v$ exits the right ($u \leftarrow v$):
     $$\text{if } (A[x] == B[y] \text{ or } u > v): \quad \text{swap}(u, \text{col\_wire}[y]).$$
3. After the $O(MN)$ double loop finishes, where did each original top wire $M + i$ ($i \in \{1, \dots, N\}$) end up?
   - If wire $M + i$ is currently in $\text{col\_wire}[j]$ for some $j \in \{1, \dots, N\}$, its exit column is $p(i) = j$.
   - Otherwise, wire $M + i$ exited on the right boundary, so we set $p(i) = N + 1$ (since $p(i) > r$ holds for all $r \le N$).
4. **Querying $\text{LCS}(A, B[l..r])$**:
   By Theorem 90.2, $\text{LCS}(A, B[l..r]) = |\{i \in [l, r] \mid p(i) > r\}|$.
   - For $Q$ online queries: Build a **Persistent Segment Tree** (or Wavelet Matrix) over the array $p[1..N]$ in $O(N \log N)$ time, answering each 2D dominance query $(l \le i \le r, \; p(i) > r)$ in $O(\log N)$ time!
   - For offline queries: Sweep $r = 1 \dots N$ with a **Fenwick Tree** in $O((N + Q) \log N)$ time.
   - For all $O(N^2)$ pairs $(l, r)$: For each fixed $r$, compute suffix counts of $i \le r$ with $p(i) > r$ in $O(N^2)$ total time!

Look at the sheer simplicity of Step 2 above: the entire $O(MN)$ Seaweed Comb construction is a **3-line inner loop**:
```cpp
for (int x = 1; x <= M; ++x) {
    int u = x; // left entrance wire for row x
    for (int y = 1; y <= N; ++y) {
        if (A[x] == B[y] || u > col_wire[y]) {
            std::swap(u, col_wire[y]);
        }
    }
}
```
Let us double check that 3-line loop!
- Why is `if (A[x] != B[y] && u < col_wire[y])` a no-op?
  Because in our variable assignment, `u` holds the wire moving **right** (from left entrance to right exit of cell $(x,y)$), and `col_wire[y]` holds the wire moving **down** (from top entrance to bottom exit of cell $(x,y)$)!
  When wires **cross**, the left entrance wire `u` goes **straight right** (staying in `u`!), and the top entrance wire `col_wire[y]` goes **straight down** (staying in `col_wire[y]`!).
  When wires **avoid / bounce**, the left entrance wire `u` turns **down** (into `col_wire[y]`), and the top entrance wire `col_wire[y]` turns **right** (into `u`), which is `std::swap(u, col_wire[y])`!

##### Hand-Checkable Example: $A = \text{"ab"}$, $B = \text{"aba"}$ ($M = 2, N = 3$)
- Initially: `col_wire[1..3] = [3, 4, 5]` (representing top wires for $B[1], B[2], B[3]$, i.e., $2 + i$).
- **Row $x = 1$ ($A[1] = \text{'a'}$), starts with $u = 1$**:
  - $y = 1$ ($B[1] = \text{'a'}$): Match $A[1] == B[1]$ $\implies$ swap! `col_wire[1] = 1`, $u = 3$.
  - $y = 2$ ($B[2] = \text{'b'}$): Mismatch and $u = 3 < \text{col\_wire}[2] = 4$ $\implies$ cross (no swap). `col_wire[2] = 4`, $u = 3$.
  - $y = 3$ ($B[3] = \text{'a'}$): Match $A[1] == B[3]$ $\implies$ swap! `col_wire[3] = 3`, $u = 5$ (wire $5$ exits right!).
  - After Row $1$: `col_wire = [1, 4, 3]`.
- **Row $x = 2$ ($A[2] = \text{'b'}$), starts with $u = 2$**:
  - $y = 1$ ($B[1] = \text{'a'}$): Mismatch, but $u = 2 > \text{col\_wire}[1] = 1$! They already crossed in column $1$ of row $1$, so swap! `col_wire[1] = 2`, $u = 1$.
  - $y = 2$ ($B[2] = \text{'b'}$): Match $A[2] == B[2]$ $\implies$ swap! `col_wire[2] = 1`, $u = 4$ (wire $4$ exits right!).
  - $y = 3$ ($B[3] = \text{'a'}$): Mismatch, but $u = 4 > \text{col\_wire}[3] = 3$! Already crossed $\implies$ swap! `col_wire[3] = 4`, $u = 3$ (wire $3$ exits right!).
  - After Row $2$: `col_wire = [2, 1, 4]`.
- **Extract $p(1..3)$ for top wires $2+1=3, 2+2=4, 2+3=5$**:
  - Top wire $3$ ($i = 1$): not in `col_wire`, exited right $\implies p(1) = \infty$.
  - Top wire $4$ ($i = 2$): ends at `col_wire[3]` $\implies p(2) = 3$.
  - Top wire $5$ ($i = 3$): not in `col_wire`, exited right $\implies p(3) = \infty$.
- **Verify All $6$ Substring LCS Values of $B = \text{"aba"}$ with $A = \text{"ab"}$ via $|\{i \in [l, r] \mid p(i) > r\}|$**:
  - $[1, 1]$ (`"a"`): $i \in \{1\}$, $p(1) = \infty > 1 \implies \text{LCS} = 1$.
  - $[2, 2]$ (`"b"`): $i \in \{2\}$, $p(2) = 3 > 2 \implies \text{LCS} = 1$.
  - $[3, 3]$ (`"a"`): $i \in \{3\}$, $p(3) = \infty > 3 \implies \text{LCS} = 1$.
  - $[1, 2]$ (`"ab"`): $i \in \{1, 2\}$, $p(1)=\infty > 2, p(2)=3 > 2 \implies \text{LCS} = 2$.
  - $[2, 3]$ (`"ba"`): $i \in \{2, 3\}$, $p(2)=3 \not> 3, p(3)=\infty > 3 \implies \text{LCS} = 1$ (`LCS("ab", "ba") = 1`!).
  - $[1, 3]$ (`"aba"`): $i \in \{1, 2, 3\}$, $p(1)=\infty > 3, p(2)=3 \not> 3, p(3)=\infty > 3 \implies \text{LCS} = 2$.
  Every single interval $[l, r]$ matches $\text{LCS}(A, B[l..r])$!

##### 2. Unit-Monge Distance Multiplication ($\boxdot$) in $O(N \log N)$ and $O(N \log^2 N)$ Divide-and-Conquer
What if we need to compose two Seaweed combs vertically (e.g., splitting $A = A_1 A_2$ in a Divide-and-Conquer tree or Segment Tree over $A$, where $M, N \le 10^5$)?
Stacking the comb of $A_1$ on top of the comb of $A_2$ corresponds to composing their permutation matrices under the **Sticky Braid / Demazure / Unit-Monge Product** $P = P_1 \boxdot P_2$:
- Convert permutation matrices $P_1, P_2$ into their implicit Unit-Monge distribution matrices $D_{P}(i, j) = \sum_{x < i, y \ge j} P(x, y)$.
- Composing $A_1$ and $A_2$ computes the tropical $(\min, +)$ matrix product:
  $$(D_{P_1} \odot D_{P_2})(i, k) = \min_{j} \bigl(D_{P_1}(i, j) + D_{P_2}(j, k)\bigr),$$
  whose cross-difference is again a $K \times K$ permutation matrix $P = P_1 \boxdot P_2$.
- **Tiskin's Recursive Divide-and-Conquer Product ($O(K \log K)$)**:
  Given two $K \times K$ permutation matrices $P_1, P_2$:
  1. Split the middle index range $[1, K]$ of $P_1$'s columns / $P_2$'s rows into lower/upper halves of size $K/2$, extracting the sub-permutations $P_{1, L}, P_{1, R}$ and $P_{2, L}, P_{2, R}$.
  2. Recursively compute $Q_L = P_{1, L} \boxdot P_{2, L}$ and $Q_R = P_{1, R} \boxdot P_{2, R}$ (two subproblems of size $K/2$).
  3. **Merge in $O(K)$ time**: The difference $\delta(i, k)$ between the contribution of the left half and right half is monotonic in both $i$ and $k$ with step $\pm 1$, so the boundary curve separating where the left half beats the right half is a monotone staircase path from $(0, K)$ to $(K, 0)$ of length $2K$, traceable in $O(K)$ time via incremental cross-difference updates (`[国家集训队论文 2021 — 单位蒙日矩阵]`).
  4. Recurrence: $T(K) = 2 T(K/2) + O(K) = O(K \log K)$!
- By matching non-zero cells $(x, y)$ where $A[x] = B[y]$ or dividing $A$ into halves, computing the Seaweed matrix of two strings (or composing $O(\log N)$ segments of $A$) takes $O(N \log^2 N)$ time!

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples
1. **Strict Inequality $p(i) > r$ vs. Weak Inequality $p(i) \ge r$**:
   In the $1$-indexed formula $\text{LCS}(A, B[l..r]) = |\{i \in [l, r] \mid p(i) > r\}|$, notice that when $B[i]$ never matches anything in $A$, wire $M + i$ goes straight down column $i$ and exits at bottom column $p(i) = i$. For $r = i$, we must have $\text{LCS}(A, B[i..i]) = 0$, which requires $p(i) = i$ to **not** be counted! Thus the condition is strictly **$p(i) > r$**, never $p(i) \ge r$.
2. **Forgetting the Historical Crossing Condition (`u > col_wire[y]`)**:
   If you only swap when $A[x] == B[y]$ and forget `|| u > col_wire[y]`, two wires that already crossed at an earlier mismatch can cross a **second time** at a later mismatch, undoing their crossing and violating the braid monoid property ($s_i^2 = s_i$ instead of $s_i^2 = 1$). Both conditions `A[x] == B[y]` AND `u > col_wire[y]` must trigger `swap(u, col_wire[y])`.

---

## Iteration 91: Bit-Parallel LCS & Edit Distance (Allison–Dix / Crochemore–Iliopoulos–Pinzon / Myers)

### 91.1 The 4-Step Derivation of Bit-Parallel LCS (`Bitset LCS` in $O(MN / w)$)

#### Step 1: The Diagnostic Signal (When $N, M \le 5 \cdot 10^4$ or $10^5$ Beats $O(N^2)$ DP)
Suppose we must compute $\text{LCS}(A[1..M], B[1..N])$ (or Edit Distance / Cyclic LCS) for $M, N \le 60{,}000$ within a 1–2 second time limit:
- Naive $O(MN)$ DP performs $3.6 \times 10^9$ inner-loop branches and memory writes, exceeding the time limit by $5\times$–$10\times$.
- Hunt–Szymanski (`O((R + N) \log N)` where $R$ is the number of matching pairs $(x, y)$ with $A[x] = B[y]$) degenerates to $O(MN \log N)$ when $|\Sigma|$ is small (e.g., binary or DNA alphabet $\Sigma = \{\text{A, C, G, T}\}$ where $R \approx MN/4$).
- However, every adjacent horizontal step in the LCS table satisfies:
  $$dp[x][y] - dp[x][y-1] \in \{0, 1\}!$$
  Because each row $dp[x][1..N]$ is encoded completely by $N$ bits $D_x[y] = dp[x][y] - dp[x][y-1] \in \{0, 1\}$, we can pack $w = 64$ columns into a single machine word `uint64_t`!
  **The Central Question**: Why does replacing $\max(dp[x-1][y], dp[x][y-1])$ with a single hardware integer subtraction (`X - ((D << 1) | 1)`) propagate the exact monotonic staircase step across 64 columns in $O(1)$ clock cycles?

#### Step 2: The Combinatorial Word Invariant (K-Contour Step Propagation & Hardware Borrow Chains)

##### Theorem 91.1 (Row-Difference Monotonicity & Segment Capture Invariant)
Fix row $x-1$ and let $D[y] = dp[x-1][y] - dp[x-1][y-1] \in \{0, 1\}$ for $1 \le y \le N$.
The indices $y$ where $D[y] = 1$ partition $[1, N]$ into contour intervals: if $1 \le y_1 < y_2 < \dots < y_k \le N$ are the positions where $D[y_r] = 1$ (and we set $y_0 = 0, y_{k+1} = N+1$), then for every $y \in [y_r, y_{r+1} - 1]$, we have $dp[x-1][y] = r$.
When we process character $c = A[x]$ to compute the new row $dp[x][\cdot]$ and its difference bitvector $D'[y] = dp[x][y] - dp[x][y-1]$:
- On each interval $[y_r + 1, y_{r+1}]$, the value of $dp[x][y]$ can increase from $r$ to $r+1$ **if and only if** either:
  1. $y = y_{r+1}$ (inheriting $dp[x-1][y_{r+1}] = r+1$ from above, i.e., $D[y_{r+1}] = 1$), OR
  2. There is at least one match position $m \in [y_r + 1, y]$ where $B[m] = A[x]$ (since at the earliest such $m$, $dp[x][m] = dp[x-1][m-1] + 1 = r + 1$, which then propagates horizontally to all $y \in [m, y_{r+1}]$ via $dp[x][y] \ge dp[x][y-1]$).
- Therefore, within each interval $(y_r, y_{r+1}]$, the **new** step position $y'_{r+1}$ where $D'[y] = 1$ is simply the **minimum** (leftmost) index in $(y_r, y_{r+1}]$ that either has $B[m] = A[x]$ or equals the old step $y_{r+1}$:
  $$y'_{r+1} = \min \bigl( \{ m \in (y_r, y_{r+1}] \mid B[m] = A[x] \} \cup \{y_{r+1}\} \bigr)!$$

*Proof of the Bitwise Borrow Identity (Allison–Dix 1986 / Hyyrö 2004).*
Represent subsets of $\{0, 1, \dots, N-1\}$ ($0$-indexed columns) as $N$-bit integers:
- Let $D$ be the bitmask of current $1$-steps ($D_j = 1 \iff dp[x-1][j+1] - dp[x-1][j] = 1$).
- Let $M_c$ be the precomputed match bitmask for character $c = A[x]$ ($M_{c, j} = 1 \iff B[j+1] = c$).
- Define the candidate bitmask:
  $$X = D \;\mid\; M_c.$$
  Notice that within every interval $(y_r, y_{r+1}]$, the bits where $X = 1$ are precisely $\{m \in (y_r, y_{r+1}] \mid B[m] = c\} \cup \{y_{r+1}\}$, so our goal is to **keep only the lowest-indexed $1$-bit of $X$ inside each interval $(y_r, y_{r+1}]$**, and clear all higher $1$-bits of $X$ in that interval!
- Look at the shifted bitmask denoting the **starts** of each interval $(y_r, y_{r+1}]$:
  $$S = (D \ll 1) \;\mid\; 1.$$
  The $1$-bits of $S$ sit at the exact left endpoints $y_r + 1$ of each interval $(y_r, y_{r+1}]$.
- Now consider the integer subtraction:
  $$X - S = (D \mid M_c) - \bigl((D \ll 1) \mid 1\bigr).$$
  What happens when we subtract $1$ at the left endpoint $y_r + 1$ of interval $(y_r, y_{r+1}]$ from $X$?
  - Since every interval $(y_r, y_{r+1}]$ has $X = 1$ at its right endpoint $y_{r+1}$ (because $D \subseteq X$), **a borrow out of the top of interval $(y_r, y_{r+1}]$ into the next interval $(y_{r+1}, y_{r+2}]$ NEVER occurs**! Every interval $(y_r, y_{r+1}]$ absorbs its own borrow independently!
  - Within interval $(y_r, y_{r+1}]$, subtracting $1$ at $y_r + 1$ propagates a borrow across all $0$-bits of $X$ until it hits the **first (lowest-indexed) $1$-bit** $y'_{r+1}$ of $X$ in $(y_r, y_{r+1}]$, flipping that bit from $1 \to 0$ (and flipping the preceding $0$-bits from $0 \to 1$), while leaving **all higher bits in $(y'_{r+1}, y_{r+1}]$ completely untouched**!
  - Consequently, in $X \oplus (X - S)$, the bits that changed are $[y_r + 1 .. y'_{r+1}]$, and taking:
    $$D' = X \;\ \& \;\ \sim(X - S) \qquad \bigl(\text{where } X = D \mid M_{A[x]}, \;\; S = (D \ll 1) \mid 1\bigr)$$
    isolates **exclusively** the bit $y'_{r+1}$ (the unique bit where $X = 1$ and $X - S = 0$) in every single interval $(y_r, y_{r+1}]$ simultaneously! $\blacksquare$

#### Step 3: The Reverse-Engineering Scratchpad (Multi-Word Carry Propagation & Myers's Edit Distance)

##### 1. Exact Multi-Word 64-Bit Loop for Allison–Dix Bit-Parallel LCS
When $N > 64$, we store $D$ and each $M_c$ as an array of $W = \lceil N / 64 \rceil$ unsigned 64-bit integers (`uint64_t`).
For each character $c = A[x]$ ($x = 1 \dots M$), we sweep word index $k = 0 \dots W-1$ maintaining two 1-bit carries across word boundaries:
- `shift_carry` $\in \{0, 1\}$: the highest bit (`D[k] >> 63`) shifted out of `D[k] << 1` into bit $0$ of word $k+1$ (initialized to `1` at $k = 0$ for the `| 1` in $(D \ll 1) \mid 1$).
- `sub_borrow` $\in \{0, 1\}$: the unsigned subtraction borrow out of `X - S` from word $k$ into word $k+1$ (initialized to `0` at $k = 0$).

```cpp
// Non-standard core kernel: Allison-Dix 64-bit word-parallel LCS step
uint64_t shift_carry = 1; // represents the '| 1' at bit 0 of word 0
uint64_t sub_borrow = 0;
for (int k = 0; k < W; ++k) {
    uint64_t X = D[k] | Match[c][k];
    uint64_t S = (D[k] << 1) | shift_carry;
    shift_carry = D[k] >> 63;
    // Compute Y = X - S - sub_borrow with unsigned 64-bit borrow detection:
    uint64_t Y = X - S;
    uint64_t next_borrow = (Y > X);
    uint64_t Z = Y - sub_borrow;
    next_borrow |= (Z > Y);
    sub_borrow = next_borrow;
    D[k] = X & ~Z;
}
```
After $x = 1 \dots M$, $\text{LCS}(A, B) = \sum_{k=0}^{W-1} \text{popcount}(D[k])$ (after masking off any unused bits beyond $N$ in the last word $W-1$).
- **Complexity**: $O(|\Sigma| \frac{N}{w} + \frac{MN}{w})$ time and $O(|\Sigma| \frac{N}{w})$ space. For $M = N = 50{,}000$, $\frac{MN}{64} \approx 3.9 \times 10^7$ simple bitwise operations, executing in **$< 40$ milliseconds** in C++!

##### Hand-Checkable Example: $B = \text{"abac"}$ ($N = 4$), $A = \text{"ba"}$ ($M = 2$)
Write 4-bit integers in binary from MSB (index 4) to LSB (index 1):
- Match masks: $M_{\text{a}} = 0101_2$ (pos 1, 3), $M_{\text{b}} = 0010_2$ (pos 2), $M_{\text{c}} = 1000_2$ (pos 4).
- Initially: $D = 0000_2$.
- **Step $x = 1$ ($A[1] = \text{'b'}$)**:
  - $X = D \mid M_{\text{b}} = 0010_2$.
  - $S = (D \ll 1) \mid 1 = 0001_2$.
  - $X - S = 0010_2 - 0001_2 = 0001_2$.
  - $D' = X \ \& \ \sim(X - S) = 0010_2 \ \& \ 1110_2 = 0010_2$ (representing row $dp[1] = [0, 1, 1, 1]$).
- **Step $x = 2$ ($A[2] = \text{'a'}$)**:
  - $X = D \mid M_{\text{a}} = 0010_2 \mid 0101_2 = 0111_2$.
  - $S = (D \ll 1) \mid 1 = 0100_2 \mid 0001_2 = 0101_2$.
  - $X - S = 0111_2 - 0101_2 = 0010_2$.
  - $D' = X \ \& \ \sim(X - S) = 0111_2 \ \& \ 1101_2 = 0101_2$ (representing row $dp[2] = [1, 1, 2, 2]$).
- Total LCS $= \text{popcount}(0101_2) = 2$. Hand check confirms $\text{LCS}(\text{"ba"}, \text{"abac"}) = |\text{"ba"}| = 2$!

##### 2. Myers's Bit-Parallel Levenshtein Edit Distance ($O(MN / w)$)
For unit-cost Edit Distance (insertion, deletion, substitution all cost $1$), adjacent horizontal and vertical differences satisfy $\Delta H, \Delta V \in \{-1, 0, +1\}$.
Myers (1999) encodes each column step by two bitvectors $VP$ (where $\Delta V = +1$, initialized to $1^N$) and $VN$ (where $\Delta V = -1$, initialized to $0^N$), updating in $O(1)$ bitwise operations per 64-bit word via:
1. $D0 = (((M_c \ \& \ VP) + VP) \oplus VP) \mid M_c \mid VN$ (diagonal zero-difference propagation via addition carry),
2. $HP = VN \mid \sim(D0 \mid VP)$ and $HN = D0 \ \& \ VP$,
3. $VP' = (HN \ll 1) \mid \sim(D0 \mid ((HP \ll 1) \mid 1))$ and $VN' = D0 \ \& \ ((HP \ll 1) \mid 1)$.

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples
1. **Unclean Trailing Bits in the Last Word $W - 1$**:
   When $N$ is not a multiple of $64$, `D[W-1]` can acquire $1$-bits at positions $\ge (N \bmod 64)$ if `Match[c][W-1]` is not zero-padded or if `popcount(D[W-1])` is called without masking `D[W-1] &= ((1ULL << (N % 64)) - 1)`. Because `Match[c][W-1]` has $0$s at positions $\ge (N \bmod 64)$, $X = D \mid M_c$ is $0$ above bit $(N \bmod 64) - 1$, so $D' = X \ \& \ \sim Z$ automatically keeps those upper bits $0$ **provided** `D[W-1]` and `Match[c][W-1]` start with $0$s in those upper bits!
2. **Signed Shift / Undefined Behavior on `1 << 64`**:
   Using `1UL` (32-bit on Windows LLP64) instead of `1ULL`, or computing `(1ULL << (N % 64))` when `N % 64 == 0` vs `64`, causes UB. Always mask only when `N % 64 != 0`.
3. **Reconstructing the Actual LCS String in $O(MN/w)$ Time and $O(N)$ Space**:
   Storing all $M$ bitvectors $D_1, \dots, D_M$ for backtracking takes $\frac{MN}{8}$ bytes ($\approx 312\text{ MB}$ for $M = N = 50{,}000$), which can MLE on 256 MB limits. Instead, combine **Hirschberg's Divide-and-Conquer** with Bit-Parallel LCS: run forward bitset LCS on $A[1..M/2]$ and backward bitset LCS on $A[M/2+1..M]^R$, find the split point $y^* = \arg\max_y (dp_{\text{pref}}[y] + dp_{\text{suff}}[N-y])$, and recurse! The total bit-parallel work is $\sum_{k \ge 0} 2^k \frac{(M/2^k) N}{w} = O(\frac{MN}{w})$ with only **$O(N/w)$ auxiliary DP memory**!

---

## Iteration 92: Multilingual Problem Mining (`[EN]` / `[ZH]` / `[JA]`), 4-Tier Difficulty Ladder & Quarantine Ledger

### 92.1 Quarantine Table of Excluded Pure-Template Problems (`R-4B-01` – `R-4B-06`)

Per `AGENTS.md` and `PLAN.md §2.2`, bare template verification problems are strictly quarantined from the textbook chapters:

| Quarantine ID | Source & Problem Name | Reason for Quarantine |
| :--- | :--- | :--- |
| **`R-4B-01`** | **Luogu P5826** — `【模板】子序列自动机` (`[ZH]`) | Pure template verification of persistent-array / binary-search DASG subsequence queries without structural coupling or DP optimization. |
| **`R-4B-02`** | **Library Checker** — `Longest Common Subsequence` (`[EN]`/`[JA]`) | Pure template verification of standard / bitset LCS reconstruction without structural modeling. |
| **`R-4B-03`** | **CSES 1143 / LeetCode 1143** — `Longest Common Subsequence` | Bare textbook Needleman–Wunsch DP exercise. |
| **`R-4B-04`** | **LeetCode 940** — `Distinct Subsequences II` | Bare whole-string $dp[c] = \sum dp + 1$ template without range queries, matrix inversion, or structural constraints. |
| **`R-4B-05`** | **SPOJ LCS0** — `Longest Common Subsequence` ($N \le 50000$) | Bare Allison–Dix bitset LCS speed test with zero modeling beyond packing bits. |
| **`R-4B-06`** | **Library Checker** — `Prefix-Substring LCS` | Pure template verification of Seaweed comb array $p[1..N]$ construction and dominance counting. |

---

### 92.2 Curated 32-Problem 4-Tier Difficulty Ladder with 4-Step Zero-Magic Analysis

#### Tier 1: Stepping Stone (Core Invariants of DASG, Non-Adjacent Subsequence DP & Arch Factorization)

1. **`[JA]` AtCoder ARC 081 E (ABC 081 / ARC 081 C) — Don't Be a Subsequence** ($N \le 2 \cdot 10^5, |\Sigma| = 26$)
   - *1. Diagnostic Signal*: Find the shortest (and lexicographically smallest among shortest) string $W \in \Sigma^+$ that is **not** a subsequence of $A$. Naive enumeration over $\Sigma^k$ is exponential.
   - *2. Combinatorial Invariant*: By Theorem 88.1 & Theorem 88.2 (Arch Factorization), $W$ is absent from $A[i+1..N]$ iff its first character $c$ transitions to $\text{nxt}[i][c]$ from which the remaining suffix of $W$ is absent.
   - *3. Algorithmic Compilation*: Build $\text{nxt}[i][c]$ backwards for $i = N \dots 0$, compute $d[i] = 1 + \min_{c} d[\text{nxt}[i][c]]$ (with $d[\infty] = 0$), and greedily reconstruct from $i = 0$ by picking the smallest $c$ achieving $d[i] = 1 + d[\text{nxt}[i][c]]$. Time: $O(N |\Sigma|)$.
   - *4. Pitfall*: Stopping reconstruction at $i = N$ instead of $\infty$ omits the final character $c \notin \text{alph}(R)$ that pushes the match out of bounds.

2. **`[JA]` AtCoder ABC 214 F — Substrings** ($N \le 2 \cdot 10^5, |\Sigma| = 26$)
   - *1. Diagnostic Signal*: Count distinct non-empty subsequences of $S$ formed by choosing non-adjacent indices ($i_{k+1} \ge i_k + 2$) modulo $10^9 + 7$.
   - *2. Combinatorial Invariant*: Canonical greedy non-adjacent matching: every valid string $W$ has a unique earliest non-adjacent embedding where $W[1]$ is at the first occurrence of $W[1]$, and $W[k]$ is at the earliest occurrence of $W[k]$ at index $\ge \text{pos}(W[1..k-1]) + 2$.
   - *3. Algorithmic Compilation*: On the modified DASG where state $i$ transitions to $\text{nxt}[i + 1][c]$ (for $i \ge 1$) and state $0$ transitions to $\text{nxt}[0][c]$, count DAG paths: $dp[i] = \sum_{j = \text{last}[S[i]]}^{i-2} dp[j]$ (with special base at $i = 0$). Time: $O(N)$.
   - *4. Pitfall*: From the root $i = 0$, the first character can be chosen at index $1$ ($\text{nxt}[0][c]$), whereas from any matched index $i \ge 1$, the next character must be at $\ge i + 2$ ($\text{nxt}[i+1][c]$). Treating $i = 0$ like $i \ge 1$ forbids picking $S[1]$!

3. **`[EN]` Codeforces 1458 C / 1303 E — Erase Subsequences** ($|S|, |T| \le 400$)
   - *1. Diagnostic Signal*: Decide whether $T$ can be partitioned into two disjoint subsequences $T_1, T_2$ that appear sequentially as a subsequence $T_1$ and $T_2$ in $S$ (so $T$ is formed by two passes over $S$). Naive 3D DP is $O(|S| \cdot |T|^2)$ per split point $= O(|S| \cdot |T|^3)$.
   - *2. Combinatorial Invariant*: Fix the split point $k$ where $T_1 = T[1..k]$ and $T_2 = T[k+1..|T|]$. Among all ways to match $T_1[1..i]$ and $T_2[1..j]$ inside a prefix of $S$, it is always optimal to **minimize** the prefix length of $S$ consumed (or equivalently, fixing $i$ and prefix of $S$, **maximize** $j$).
   - *3. Algorithmic Compilation*: Use $\text{DASG}(S)$: let $dp[i][j]$ be the minimum index in $S$ needed to match $T_1[1..i]$ and $T_2[1..j]$ simultaneously. Transition via $\text{nxt}_S[dp[i][j]][c]$ in $O(1)$ time! Total time across all $k$: $O(|T|^3 + |S||\Sigma|)$.
   - *4. Pitfall*: Rebuilding $\text{DASG}(S)$ inside the loop over $k$ adds an unnecessary factor of $|T|$.

4. **`[EN]` Codeforces 1295 C — Obtain The String** ($|S|, |T| \le 10^5$)
   - *1. Diagnostic Signal*: Minimum number of subsequences of $S$ needed to concatenate into $T$.
   - *2. Combinatorial Invariant*: Greedy canonical consumption on $\text{DASG}(S)$: each pass should match the longest possible prefix of the remaining suffix of $T$.
   - *3. Algorithmic Compilation*: Walk $\text{nxt}_S[u][T[i]]$; whenever $\text{nxt}_S[u][T[i]] = \infty$, increment pass count and reset $u = 0$. Time: $O((|S| + |T|)|\Sigma|)$.
   - *4. Pitfall*: If $\text{nxt}_S[0][T[i]] = \infty$, the character $T[i]$ does not exist in $S$ at all—must immediately return `-1` instead of looping infinitely.

5. **`[EN]` Codeforces 1924 C / 1925 C — Did We Get Everything Covered?** ($N, K \le 26, M \le 1000$)
   - *1. Diagnostic Signal*: Determine if all $K^N$ strings of length $N$ over $\{a_1, \dots, a_K\}$ are subsequences of $S[1..M]$, and if not, output a missing witness of length $N$.
   - *2. Combinatorial Invariant*: Direct application of Theorem 88.2 (Hébrard's Arch Factorization): $\iota(S) \ge N \iff S$ contains at least $N$ disjoint $1$-universal arches.
   - *3. Algorithmic Compilation*: Sweep $S$, collecting unique characters until size reaches $K$; record the final character $m_r$ of each arch and reset the set. If $< N$ arches are formed, append a character missing from the remainder $R$ and pad to length $N$. Time: $O(M)$.
   - *4. Pitfall*: Padding with an arbitrary character *before* appending the character missing from $R$ breaks the greedy forced-jump invariant! The character absent from $R$ must come **immediately** after the arch bottlenecks $m_1 \dots m_k$.

6. **`[ZH]` Luogu P3856 — `[TJOI2008] 公共子串` (Distinct Common Subsequences of 3 Strings)** ($|A|, |B|, |C| \le 150$)
   - *1. Diagnostic Signal*: Count distinct non-empty strings $W$ that are subsequences of all three strings $A, B, C$.
   - *2. Combinatorial Invariant*: A string $W$ has a unique canonical state $(u_A, u_B, u_C)$ in the 3-way product automaton $\text{DASG}(A) \times \text{DASG}(B) \times \text{DASG}(C)$.
   - *3. Algorithmic Compilation*: DAG path counting on reachable product states $(\text{nxt}_A[i][c], \text{nxt}_B[j][c], \text{nxt}_C[k][c])$ in $O(|A||B||C||\Sigma|)$ time using big integers.
   - *4. Pitfall*: Counting paths without canonical earliest-match transitions (`nxt[i][c]`) overcounts subsequences with multiple embeddings.

7. **`[JA]` AtCoder ABC 130 E / ARC-style Extension — Subsequence Path Counting vs Distinct**
   - *1. Diagnostic Signal*: Distinguishing multiplicity-weighted common subsequences from distinct common subsequences on $\text{DASG}(A) \times \text{DASG}(B)$.
   - *2. Combinatorial Invariant*: Canonical matches biject distinct subsequences to paths in $\text{DASG}$, whereas index-pair DP counts embedding pairs.
   - *3. Algorithmic Compilation*: Contrast standard 2D prefix-sum DP with product-DASG DAG DP.
   - *4. Pitfall*: Subtracting $dp[i-1][j-1]$ handles 2D grid inclusion-exclusion, not distinct string deduplication.

---

#### Tier 2: Intermediate (Four-Comb Product Automata, Bracket Subsequences, Matrix Semiring DP & Bitset LCS)

8. **`[ZH]` Luogu P4112 — `[HEOI2015] 最短不公共子串` (Shortest Uncommon Substring / Subsequence Four-Comb)** ($|A|, |B| \le 2000$)
   - *1. Diagnostic Signal*: Solve all 4 combinations of shortest $W$ that is a (substring / subsequence) of $A$ and NOT a (substring / subsequence) of $B$.
   - *2. Combinatorial Invariant*: Product automaton $\mathcal{M}_A \times \mathcal{M}_B$ where $\mathcal{M}_X \in \{\text{SAM}(X), \text{DASG}(X)\}$ is a deterministic incomplete DFA accepting $\text{Substr}(X)$ or $\text{Subseq}(X)$.
   - *3. Algorithmic Compilation*: Build $\text{SAM}(A), \text{SAM}(B), \text{DASG}(A), \text{DASG}(B)$ in $O((|A|+|B|)|\Sigma|)$ time. For each of the 4 pairs, run BFS on $(u, v) \in Q_A \times Q_B$ from $(\text{root}_A, \text{root}_B)$; the first state $(u, v)$ at depth $d$ that has a transition $c$ with $\delta_A(u, c) \ne \perp$ and $\delta_B(v, c) = \perp$ gives answer $d + 1$. Time: $O(|A||B||\Sigma|)$.
   - *4. Pitfall*: Using suffix links in $\text{SAM}(B)$ when $\delta_B(v, c) = \perp$ turns substring recognition into suffix-of-prefix matching, completely invalidating Subproblems (1) and (3).

9. **`[EN]` Codeforces 750 E — New Year and Old Subsequence** ($N, Q \le 2 \cdot 10^5$)
   - *1. Diagnostic Signal*: Given digit string $S[1..N]$ and $Q$ range queries $[l, r]$, find the minimum deletions in $S[l..r]$ so that `"2017"` is a subsequence and `"2016"` is NOT a subsequence.
   - *2. Combinatorial Invariant*: Construct the 5-state DFA tracking the longest prefix of `"2017"` matched so far: states $0$ ($\epsilon$), $1$ (`"2"`), $2$ (`"20"`), $3$ (`"201"`), $4$ (`"2017"`), while forbidding transition from state $3$ or $4$ on `'6'` (requiring `'6'` to be deleted at cost $1$).
   - *3. Algorithmic Compilation*: Each character $S[i]$ defines a $5 \times 5$ $(\min, +)$ tropical matrix $T_{S[i]}$. Build a Segment Tree over $[1, N]$ storing $5 \times 5$ matrices; for each query $[l, r]$, multiply the row vector $(0, \infty, \infty, \infty, \infty)$ through the $O(\log N)$ segment tree nodes in $O(5^2 \log N)$ time!
   - *4. Pitfall*: Even after reaching state $4$ (`"2017"`), any subsequent `'6'` in $S[l..r]$ still forms `"2016"` using the `"201"` prefix! Thus state $4$ MUST also pay cost $1$ to delete every `'6'` ($T_{\text{'6'}}[4][4] = 1$, not $0$).

10. **`[JA]` AtCoder ABC 299 E / ARC 159 D /JOI-style — Palindromic Distinct Subsequences on DASG** ($N \le 3000$)
    - *1. Diagnostic Signal*: Count distinct palindromic subsequences of $S[1..N]$ modulo $998244353$.
    - *2. Combinatorial Invariant*: Every distinct palindrome $P = c_1 \dots c_k (\text{mid}) c_k \dots c_1$ is uniquely represented by matching $c_1 \dots c_k$ at the **earliest** possible prefix positions in $S$ (forward DASG $\text{nxt}[l][c]$) and matching the mirrored $c_1 \dots c_k$ at the **latest** possible suffix positions in $S$ (backward DASG $\text{prv}[r][c]$), requiring $\text{nxt}[l][c] < \text{prv}[r][c]$.
    - *3. Algorithmic Compilation*: 2D DP over outer matched pair $(l, r)$ with $l < r$ and $S[l] = S[r]$: from $(l, r)$, transition to $(\text{nxt}[l][c], \text{prv}[r][c])$ for each $c \in \Sigma$ whenever $\text{nxt}[l][c] < \text{prv}[r][c]$, plus $1$ for the even palindrome without center, plus $|\text{alph}(S[l+1..r-1])|$ for odd centers! Notice that for fixed $(l, r)$, the target $(\text{nxt}[l][c], \text{prv}[r][c])$ is a single cell, so each state has $|\Sigma|$ transitions—or summing via prefix sums takes $O(N^2)$ time!
    - *4. Pitfall*: If $\text{nxt}[l][c] == \text{prv}[r][c]$, that single character $c$ adds an odd-length palindrome (length $+1$), NOT an outer pair transition (length $+2$).

11. **`[ZH]` Luogu P3763 / BZOJ 4032 — `[HEOI2015] 最短不公共子串` Memory-Optimized Variant & Witness Reconstruction**
    - *1. Diagnostic Signal*: Reconstruct the lexicographically smallest witness string $W$ in all 4 combinations of SAM/DASG product automata.
    - *2. Combinatorial Invariant*: Visiting transitions $c = \text{'a'} \dots \text{'z'}$ in alphabetical order during BFS from $(\text{root}_A, \text{root}_B)$ guarantees the first discovered witness is both shortest and lexicographically smallest.
    - *3. Algorithmic Compilation*: Store parent pointer `(prev_u, prev_v, char_c)` on the product grid and backtrack from the first accepting transition.
    - *4. Pitfall*: Checking acceptance when popping from the queue vs pushing into the queue must still scan $c = \text{'a'} \dots \text{'z'}$ in increasing order.

12. **`[EN]` Codeforces 1149 B — Three Religions** ($N \le 10^5, |W_1|, |W_2|, |W_3| \le 250, Q \le 1000$)
    - *1. Diagnostic Signal*: Maintain three dynamic strings $W_1, W_2, W_3$ (each up to length $250$) under character append/pop, checking after each operation whether $S[1..N]$ can be partitioned into three disjoint subsequences equal to $W_1, W_2, W_3$.
    - *2. Combinatorial Invariant*: On $\text{DASG}(S)$, let $dp[i][j][k]$ be the minimum prefix of $S$ containing $W_1[1..i], W_2[1..j], W_3[1..k]$ as disjoint subsequences:
      $$dp[i][j][k] = \min \bigl(\text{nxt}[dp[i-1][j][k]][W_1[i]], \; \text{nxt}[dp[i][j-1][k]][W_2[j]], \; \text{nxt}[dp[i][j][k-1]][W_3[k]]\bigr).$$
    - *3. Algorithmic Compilation*: Appending a character to $W_1$ only computes the single slice $i = |W_1|$ of size $|W_2| \times |W_3| \le 250^2$ in $O(L^2)$ time! Popping requires $O(1)$ work. Total time: $O(N|\Sigma| + Q L^2)$.
    - *4. Pitfall*: Defining $\text{nxt}[\infty][c] = \infty$ is essential so unreachable states do not wrap around to $\text{nxt}[0][c]$.

13. **`[EN]` AtCoder ABC 138 E / Codeforces 91 A — Newspaper Headline & Cyclic DASG Binary Lifting** ($|S| \le 10^5, |T| \le 10^6$)
    - *1. Diagnostic Signal*: When $T$ is matched against $S^\infty$ (or when $Q$ queries ask how many copies of $S$ are needed to contain $S[l..r]$ repeated $k$ times), step-by-step character walking is too slow if $T$ is compressed.
    - *2. Combinatorial Invariant*: On $\text{DASG}(S \cdot S)$, jumping from one occurrence of pattern block to the next is a deterministic functional graph transition $f(i)$, amenable to binary lifting $f^{2^k}(i)$.
    - *3. Algorithmic Compilation*: Precompute jump pointers in $O(N \log K)$ time.
    - *4. Pitfall*: Doubling $S$ to $S \cdot S$ is required before building `nxt` so cyclic wrap-around transitions do not need modular branches inside the inner loop.

14. **`[ZH]` UOJ / LOJ / Regional Classic — Bracket-Balanced Distinct Subsequences (`括号序列子序列计数`)** ($N \le 500$)
    - *1. Diagnostic Signal*: Count distinct regular bracket sequences (RBS) that appear as subsequences of $S[1..N]$.
    - *2. Combinatorial Invariant*: Every distinct RBS has a unique canonical greedy embedding in $\text{DASG}(S)$ tracked by $(i, \text{bal})$ where $i \in \{0, \dots, N\}$ is the DASG node and $\text{bal} \in \{0, \dots, N/2\}$ is the open-minus-close balance.
    - *3. Algorithmic Compilation*: From $(i, \text{bal})$, transition to $(\text{nxt}[i][\text{'('}], \text{bal} + 1)$ and (if $\text{bal} > 0$) to $(\text{nxt}[i][\text{')'}], \text{bal} - 1)$ in $O(N^2)$ time.
    - *4. Pitfall*: Counting empty string $\epsilon$ when the problem asks for non-empty RBS, or allowing $\text{bal} < 0$.

15. **`[EN]` Codeforces / SPOJ / ICPC Regional — Bit-Parallel LCS with $K$-Length Substring Reconstruction & Hirschberg** ($M, N \le 50{,}000$)
    - *1. Diagnostic Signal*: Compute and reconstruct the actual LCS string of $A[1..M]$ and $B[1..N]$ for $M, N = 50{,}000$ in 256 MB memory.
    - *2. Combinatorial Invariant*: Combining Theorem 91.1 (Allison–Dix $O(MN/w)$ bit-parallel row difference DP) with Hirschberg's bidirectional midpoint split $M/2$.
    - *3. Algorithmic Compilation*: Run bitset LCS forward on $A[1..M/2]$ vs $B$ and backward on $A[M/2+1..M]^R$ vs $B^R$; unpack the two final $N$-bit difference vectors into prefix sums in $O(N)$ time, find $y^* = \arg\max_y (L_1[y] + L_2[N-y])$, and recurse on $(A[1..M/2], B[1..y^*])$ and $(A[M/2+1..M], B[y^*+1..N])$. Total time: $O(MN/w)$, space: $O((M+N)|\Sigma|/w + N)$.
    - *4. Pitfall*: During the recursive subcalls on $B[l_B .. r_B]$, rebuilding the match bitmasks $M_c$ over the entire string $B$ instead of just the active subsegment $[l_B, r_B]$ blows up the time complexity from $O(MN/w)$ to $O(MN \log M / w)$! Always slice or build $M_c$ locally in $O((r_B - l_B + 1)|\Sigma|/w)$ time per recursive call.

---

#### Tier 3: Advanced (Invertible Subsequence Matrices, Range Distinct Subsequences, Cyclic Bitset LCS & Seaweed Interval LCS)

16. **`[ZH]` / `[EN]` Range Distinct Subsequences (`区间本质不同子序列计数` — QOJ / Universal Cup / HDU 6599-style / CodeChef `DISTSUBS`)** ($N, Q \le 2 \cdot 10^5, |\Sigma| \le 26$)
    - *1. Diagnostic Signal*: Given $S[1..N]$ and $Q$ queries $[l, r]$, output the number of distinct subsequences of $S[l..r]$ modulo $10^9 + 7$. Segment tree of $27 \times 27$ matrices takes $O(N\sigma^3 + Q\sigma^2 \log N)$ and TLEs.
    - *2. Combinatorial Invariant*: By Theorem 89.1 & Theorem 89.3, the transition matrix $M_c = I_{\sigma+1} + \mathbf{e}_c \sum_{j \ne c} \mathbf{e}_j^T$ has determinant $1$ and inverse $M_c^{-1} = I_{\sigma+1} - \mathbf{e}_c \sum_{j \ne c} \mathbf{e}_j^T$. Moreover, $\text{Ans}(l, r) = (\mathbf{1}^T P_r)(P_{l-1}^{-1} \mathbf{e}_{\sigma+1}) = \mathbf{u}_r^T \cdot \mathbf{v}_{l-1}$.
    - *3. Algorithmic Compilation*: Precompute $\mathbf{u}_i^T = 2\mathbf{u}_{i-1}^T - \mathbf{u}_{\text{last}[S[i]]-1}^T$ and $\mathbf{v}_i = P_i^{-1} \mathbf{e}_{\sigma+1}$ (via lazy global offset vector $\mathbf{g}^{(i)}$ on the columns of $P_i^{-1}$) in $O(N\sigma)$ time and space; answer each query $[l, r]$ in $O(\sigma)$ time via dot product $\mathbf{u}_r^T \cdot \mathbf{v}_{l-1}$!
    - *4. Pitfall*: Subtracting $1$ at the end if the problem specifies **non-empty** distinct subsequences ($\text{Ans}(l, r) - 1 \pmod{10^9+7}$).

17. **`[EN]` Codeforces 1609 E — William The Oblivious (Dynamic `"abc"`-Free Subsequence Maintenance)** ($N, Q \le 10^5$)
    - *1. Diagnostic Signal*: Given a string of `'a'`, `'b'`, `'c'` under single-character point updates, maintain the minimum deletions so `"abc"` is NOT a subsequence.
    - *2. Combinatorial Invariant*: By Menger's / Dilworth's duality on the 3-character subsequence `"abc"`, any valid deletion leaves a string where all remaining `'a'`s precede some split $i$, all remaining `'c'`s follow some split $j \ge i$, and no `'b'` lies between $i$ and $j$. Equivalently, track the $3 \times 3$ $(\min, +)$ automaton matrix avoiding `"abc"`.
    - *3. Algorithmic Compilation*: Segment tree of $3 \times 3$ tropical matrices over $[1, N]$, $O(3^3 \log N)$ per update.
    - *4. Pitfall*: Confusing `"abc"` as a contiguous substring with `"abc"` as a subsequence.

18. **`[ZH]` Luogu P7456 / LOJ 3399 — `[THUPC 2021] 区间 LCS` (All-Pairs / Range Query Interval LCS)** ($|A| \le 5000, |B| \le 5000$ or $10^5, Q \le 10^6$)
    - *1. Diagnostic Signal*: Given $A[1..M], B[1..N]$ and $Q$ queries $(l, r)$, compute $\text{LCS}(A, B[l..r])$.
    - *2. Combinatorial Invariant*: By Theorem 90.1 & Theorem 90.2, the 2D cross-difference of $\text{LCS}(A, B[l..r])$ is Tiskin's Seaweed permutation $p[1..N]$, and $\text{LCS}(A, B[l..r]) = |\{i \in [l, r] \mid p(i) > r\}|$.
    - *3. Algorithmic Compilation*: Run the 3-line Seaweed comb loop in $O(MN)$ time (or $O((M+N)\log^2(M+N))$ via Unit-Monge divide-and-conquer when $M, N \le 10^5$) to extract $p[1..N]$. Answer $Q$ queries in $O(Q \log N)$ via Persistent Segment Tree / Fenwick sweep (or $O(1)$ per query after $O(N^2)$ 2D prefix sums when $N \le 5000$).
    - *4. Pitfall*: Using $p(i) \ge r$ instead of $p(i) > r$ overcounts unmatched characters exiting at $p(i) = r$.

19. **`[JA]` AtCoder ABC 331 F / Universal Cup — Range Binary Subsequence Count with Point Updates** ($N, Q \le 2 \cdot 10^5, |\Sigma| = 2$)
    - *1. Diagnostic Signal*: Maintain distinct subsequences of $S[l..r]$ under **point character updates** $S[p] \leftarrow c$ when $|\Sigma|$ is small ($\sigma \le 6$).
    - *2. Combinatorial Invariant*: When point updates are present, prefix inverses cannot be maintained statically in $O(1)$, so we store the $(\sigma+1)\times(\sigma+1)$ matrix $M_{S[i]}$ in a Segment Tree—or exploit the sparse structure $M_c$ to multiply two segment tree nodes in $O(\sigma^3)$ time and evaluate queries via vector-matrix products in $O(\sigma^2 \log N)$ time.
    - *3. Algorithmic Compilation*: Segment tree of $(\sigma+1)\times(\sigma+1)$ matrices.
    - *4. Pitfall*: Multiplying full matrices during `query(l, r)` takes $O(\sigma^3 \log N)$, whereas passing the $1 \times (\sigma+1)$ vector $\mathbf{w}$ through the $O(\log N)$ canonical segment tree nodes takes only $O(\sigma^2 \log N)$!

20. **`[EN]` Codeforces 1814 F / 1614-style / ICPC WF — Cyclic LCS (`循环最长公共子序列`) via Seaweed Matrices or Andy Nguyen's Bitset Method** ($M, N \le 2000$)
    - *1. Diagnostic Signal*: Given $A[1..M]$ and $B[1..N]$, find the maximum LCS between $A$ (or any cyclic shift of $A$) and any cyclic shift of $B$: $\max_{0 \le k < N} \text{LCS}(A, B[k+1..N] B[1..k])$.
    - *2. Combinatorial Invariant*: Doubling $B$ to $B' = B \cdot B$ of length $2N$ reduces every cyclic shift $B[k+1..N] B[1..k]$ to the contiguous interval $B'[k+1 .. k+N]$ of length $N$!
    - *3. Algorithmic Compilation*: Run Tiskin's Seaweed comb on $A[1..M]$ and $B'[1..2N]$ in $O(MN)$ time to obtain $p[1..2N]$. Then for each $k \in \{0, \dots, N-1\}$, $\text{LCS}(A, B'[k+1..k+N]) = |\{i \in [k+1, k+N] \mid p(i) > k + N\}|$, which can be swept across $k = 0 \dots N-1$ in $O(N)$ time! Total time: **$O(MN)$** (replacing the classical $O(MN)$ non-crossing shortest path divide-and-conquer of Schmidt 1998 with a 10-line Seaweed loop!).
    - *4. Pitfall*: Wait—what if we may rotate **both** $A$ and $B$? Rotating $B$ covers all alignments where the optimal cyclic LCS does not wrap around BOTH $A$ and $B$ simultaneously; in fact, any non-crossing cyclic matching of size $L \ge 1$ has at least one matched pair $(x, y)$, and cutting the circle no longer needs both strings rotated if we fix the cut between matched pairs of $B$! Wait: does rotating only $B$ always achieve the maximum cyclic LCS of $A$ and $B$?
      **Careful Counterexample Check**: Suppose $A = \text{"ba"}$ and $B = \text{"ab"}$. Rotating $B$ gives `"ab"` ($\text{LCS}(\text{"ba"}, \text{"ab"}) = 1$) and `"ba"` ($\text{LCS}(\text{"ba"}, \text{"ba"}) = 2$). What if $A = \text{"cab"}$ and $B = \text{"abc"}$? Rotating $B$ gives `"cab"`, matching all 3! In general, for any cyclic common subsequence $c_1 \dots c_L$, its indices in $A$ are cyclic only up to the cut of $A$, so if we keep $A$ fixed (cut at $M|1$), the indices in $A$ are $1 \le i_1 < \dots < i_L \le M$, which cuts $B$ at **one** corresponding place, meaning **rotating $B$ alone suffices to find the maximum Cyclic LCS of $A$ and $B$**!

21. **`[ZH]` QOJ / Universal Cup — Prefix-Suffix & Substring-Prefix LCS Matrix (`全前缀-全子串 LCS`)** ($M, N \le 2000$)
    - *1. Diagnostic Signal*: Compute $\text{LCS}(A[1..i], B[l..r])$ for all $1 \le i \le M$ and $1 \le l \le r \le N$.
    - *2. Combinatorial Invariant*: In the $O(MN)$ Seaweed comb algorithm, the state of `col_wire[1..N]` immediately after finishing row $x = i$ is the **exact** Seaweed permutation for $A[1..i]$ vs $B[1..N]$!
    - *3. Algorithmic Compilation*: After each row $x = i$ of the Seaweed loop, read off `col_wire[1..N]` to answer all interval queries against $A[1..i]$.
    - *4. Pitfall*: Modifying `col_wire` destructively without recording row snapshots if queries across different $i$ are not sorted by $i$.

22. **`[JA]` AtCoder AGC 024 E — Sequence Growing Hard** ($N, K \le 300$)
    - *1. Diagnostic Signal*: Count sequences of strings $A_0 = \epsilon, A_1, \dots, A_N$ over $\{1, \dots, K\}$ where $A_i$ is obtained by inserting one character into $A_{i-1}$ such that $A_{i-1} <_{\text{lex}} A_i$ (where $A_{i-1}$ is a subsequence of $A_i$).
    - *2. Combinatorial Invariant*: Inserting character $c$ immediately before some position $p$ with $A_{i-1}[p] = c$ duplicates a run of $c$'s; to avoid overcounting identical resulting strings $A_i$, canonicalize by inserting $c$ **only at the end of a contiguous block of $c$'s** (so $c > A_{i-1}[p]$ holds strictly!).
    - *3. Algorithmic Compilation*: Tree / Cartesian insertion DP in $O(N^3)$ time.
    - *4. Pitfall*: Inserting $c$ before $c$ produces the exact same string as inserting $c$ after $c$; failing to canonicalize the insertion position within equal-character runs overcounts valid string trajectories.

23. **`[EN]` Codeforces 1366 G — Construct the String** ($|S|, |T| \le 10^4$)
    - *1. Diagnostic Signal*: $S$ contains letters and `'.'` (backspace). Delete the minimum number of characters from $S$ so that evaluating the remaining string produces $T$.
    - *2. Combinatorial Invariant*: Subsequence matching coupled with stack-cancellation segments: for each character $S[i] \ne \text{'.'}$, precompute the shortest balanced prefix $S[i..r_i]$ where $S[i]$ is deleted by a matching `'.'` at $r_i$.
    - *3. Algorithmic Compilation*: 2D DP over $(i \in [0, |S|], j \in [0, |T|])$ with jump transition $i \to r_i + 1$ (cost $0$ deletions!). Time: $O(|S||T|)$.
    - *4. Pitfall*: Allowing arbitrary unmatched letters to be skipped at cost $0$ without pairing them with a balanced `'.'` interval.

24. **`[ZH]` Luogu P4094 / SDOI / BZOJ — Subsequence Automaton + Persistent Segment Tree on Large Alphabet** ($N, |\Sigma| \le 10^5$)
    - *1. Diagnostic Signal*: Build $\text{DASG}(S)$ when the alphabet size is $\sigma = 10^5$ (integer array elements), and answer subsequence / absent-subsequence queries.
    - *2. Combinatorial Invariant*: Since $\text{nxt}[i][\cdot]$ differs from $\text{nxt}[i+1][\cdot]$ in only one entry $c = S[i+1]$, the $N+1$ transition rows share $O(N \log \sigma)$ persistent segment tree nodes.
    - *3. Algorithmic Compilation*: Build persistent segment tree roots `rt[N] .. rt[0]` backwards; each point update sets leaf $S[i+1]$ to $i+1$, and maintain segment-tree minimum of $d[\text{nxt}[i][c]]$ at internal nodes to query $\min_{c \in \Sigma} d[\text{nxt}[i][c]]$ in $O(1)$ time at the root!
    - *4. Pitfall*: If some $c \in \{1, \dots, \sigma\}$ has never appeared in $S[i+1..N]$, its leaf holds $\infty$ (with $d[\infty] = 0$), so the segment tree must initialize all $\sigma$ leaves at `rt[N]` to $d[\infty] = 0$.

---

#### Tier 4: Mastery (Unit-Monge Braid Divide-and-Conquer, Range Subsequence Matrix Inverses with Constraints, Bit-Parallel Cyclic LCS & Weighted Seaweeds)

25. **`[ZH]` 国家集训队论文 2021 / QOJ — Substring-Substring LCS Queries (`双区间 LCS`: $\text{LCS}(A[l_1..r_1], B[l_2..r_2])$)** ($M, N \le 10^5$ or $3 \cdot 10^4, Q \le 10^5$)
    - *1. Diagnostic Signal*: Query $\text{LCS}(A[l_1..r_1], B[l_2..r_2])$ where **both** $A$ and $B$ are sliced to intervals!
    - *2. Combinatorial Invariant*: Build a Segment Tree over $A[1..M]$ where each node $[L, R]$ stores the Seaweed permutation matrix of $A[L..R]$ against $B[1..N]$ (restricted to the active matching columns of $B$, of size $\le R - L + 1$), merged via $O(K \log K)$ **Unit-Monge Braid Multiplication ($\boxdot$)**.
    - *3. Algorithmic Compilation*: Precompute the segment tree over $A$ in $O(M \log^2 M)$ time; for a query $(l_1, r_1, l_2, r_2)$, propagate the boundary distribution vector across the $O(\log M)$ canonical segment tree nodes of $A[l_1..r_1]$ using Tiskin's Monge vector-matrix multiplication in $O(\log^2 N)$ per node.
    - *4. Pitfall*: Storing dense $N \times N$ Seaweed permutations in every segment tree node of $A$ uses $O(MN \log M)$ space; you must compress out identity wires (columns $y$ where no character in $A[L..R]$ matches $B[y]$) so a node of length $K = R - L + 1$ only touches $\le 2K$ active wires!

26. **`[EN]` Codeforces 1667 E / 1707 D / UCup Grandmaster — Range Distinct Subsequences Modulo $P$ with Forbidden Substrings or Length Weights** ($N, Q \le 2 \cdot 10^5, |\Sigma| = 26$)
    - *1. Diagnostic Signal*: For each query $[l, r]$, compute $\sum_{W \in \text{Subseq}(S[l..r])} x^{|W|} \pmod{998244353}$ (the length-generating polynomial evaluated at $x$, or distinct subsequence count weighted by $\prod_{k} \text{val}(W[k])$).
    - *2. Combinatorial Invariant*: Generalize Theorem 89.1 to weighted elementary matrices! When character $c$ with weight $\alpha_c$ is appended, every existing subsequence $u \in \text{Subseq}(T)$ gets extended to $u \cdot c$ of weight $\alpha_c \cdot \text{wt}(u)$, while $w_c(T)$ is replaced by $\alpha_c \bigl(w_\epsilon(T) + \sum_{a \in \Sigma} w_a(T)\bigr)$!
      Wait: let us check the diagonal entry $(c, c)$ of the weighted matrix $M_c(\alpha_c)$:
      $$w_c(T \cdot c) = \alpha_c w_c(T) + \alpha_c w_\epsilon(T) + \sum_{a \ne c} \alpha_c w_a(T)!$$
      So row $c$ of $M_c(\alpha_c)$ is $(\alpha_c, \alpha_c, \dots, \alpha_c)$, and its determinant is **$\det(M_c(\alpha_c)) = \alpha_c$**!
      As long as $\alpha_c \in \mathcal{R}^\times$ is a **unit** in the ring (e.g., $\alpha_c \not\equiv 0 \pmod{998244353}$), $M_c(\alpha_c)$ is **still invertible** with:
      $$M_c(\alpha_c)^{-1}: \quad \text{row } c \text{ has } \alpha_c^{-1} \text{ on the diagonal and } -1 \text{ on all off-diagonal entries } j \ne c!$$
    - *3. Algorithmic Compilation*: Apply the exact same $O((N + Q)\sigma)$ prefix-matrix algorithm of Theorem 89.3 with $\alpha_c^{-1}$ in the inverse update!
    - *4. Pitfall*: **Local Algebraic Hypothesis (`AGENTS.md`)**: When $\alpha_c = 1$ (unweighted count), $\det(M_c) = 1$, which is a unit over **every** commutative ring $\mathbb{Z}/M\mathbb{Z}$. When $\alpha_c \ne 1$, $M_c(\alpha_c)$ is invertible **if and only if** $\gcd(\alpha_c, M) = 1$! If $\alpha_c \equiv 0 \pmod M$, row $c$ becomes all zeros and $M_c(0)$ is singular.

27. **`[JA]` AtCoder AGC 055 D / ARC 146 E / JOI Spring Camp — LCS Automaton (`DP套DP`) Meets Bit-Parallel State Compression** ($N \le 15, M \le 100$)
    - *1. Diagnostic Signal*: Count strings $B \in \Sigma^M$ such that $\text{LCS}(A, B) = k$ for each $0 \le k \le |A|$ ($|A| \le 15$).
    - *2. Combinatorial Invariant*: By Theorem 91.1, the entire LCS DP row $dp[x][1..|A|]$ is bijectively encoded by the $|A|$-bit difference mask $D \in \{0, \dots, 2^{|A|}-1\}$, and its transition on character $c \in \Sigma$ is given in $O(1)$ time by the Allison–Dix formula $D' = (D \mid M_c) \ \& \ \sim\bigl((D \mid M_c) - ((D \ll 1) \mid 1)\bigr)$!
    - *3. Algorithmic Compilation*: Precompute the transition table `trans[D][c]` for all $2^{|A|}$ masks $D$ in $O(2^{|A|} |\Sigma|)$ time using the 1-line bitwise formula (no array unpacking needed!), then run outer DP over $(x \in [0, M], D \in [0, 2^{|A|}))$ in $O(M 2^{|A|} |\Sigma|)$ time!
    - *4. Pitfall*: Unpacking and repacking the DP array inside the transition loop adds an $O(|A|)$ factor; the Allison–Dix bitwise transition computes `trans[D][c]` in **4 CPU instructions**!

28. **`[EN]` Universal Cup / Petrozavodsk — $K$-th Lexicographically Smallest Common Subsequence of $A$ and $B$** ($|A|, |B| \le 3000, K \le 10^{18}$)
    - *1. Diagnostic Signal*: Find the $K$-th lexicographically smallest **distinct common subsequence** (or common **longest** subsequence) of $A$ and $B$.
    - *2. Combinatorial Invariant*: On the product automaton $\text{DASG}(A) \times \text{DASG}(B)$, every distinct common subsequence corresponds to a unique path from $(0, 0)$ where step $c$ transitions $(i, j) \to (\text{nxt}_A[i][c], \text{nxt}_B[j][c])$.
    - *3. Algorithmic Compilation*: Compute $dp[i][j] = 1 + \sum_{c \in \Sigma} dp[\text{nxt}_A[i][c]][\text{nxt}_B[j][c]]$ (clamped at $K+1$) in $O(|A||B||\Sigma|)$ time (or $O(|A||B|)$ via 2D suffix sums since $\text{nxt}_A[i][c]$ is the first occurrence of $c$ after $i$!), then walk greedily from $(0, 0)$.
    - *4. Pitfall*: To optimize $O(|A||B||\Sigma|) \to O(|A||B|)$, observe that $(i', j')$ with $A[i'] = B[j'] = c$ is the canonical transition from $(i, j)$ on $c$ iff $i < i' \le \text{prev}_A[i']$... wait: $\text{nxt}_A[i][c] = i' \iff \text{prev}_A[i'] \le i < i'$! Thus each matched pair $(i', j')$ with $A[i'] = B[j']$ contributes $dp[i'][j']$ to the 2D rectangle $[\text{prev}_A[i'], i'-1] \times [\text{prev}_B[j'], j'-1]$, reducing $O(|A||B||\Sigma|)$ to **$O(|A||B|)$ alphabet-independent time** via 2D difference arrays!

29. **`[ZH]` UOJ / LOJ / NOI-style — Dynamic Range Subsequence Matching via Sqrt / Wavelet + DASG** ($N, Q \le 10^5, \sum |P| \le 10^5$)
    - *1. Diagnostic Signal*: Given $S[1..N]$ and queries $(l, r, P)$ asking for the longest prefix of $P$ that is a subsequence of $S[l..r]$ when $|\Sigma| \le 10^5$.
    - *2. Combinatorial Invariant*: Each step in $P$ sets $cur \leftarrow \text{nxt}[cur][P[k]]$ and stops if $cur > r$.
    - *3. Algorithmic Compilation*: Maintain per-character sorted occurrence lists with finger search / persistent segment tree in $O(\sum |P| \log N)$.
    - *4. Pitfall*: Binary searching from index $0$ instead of using cache-friendly small-vector or persistent DASG when $|\Sigma|$ is small.

30. **`[EN]` Codeforces 1842 H / 1776-style / ICPC WF — Semi-Local LCS & Longest Common Subsequence with Substring Insertion** ($M, N \le 5000$)
    - *1. Diagnostic Signal*: Insert string $C$ into $B$ at the optimal position $k \in [0, N]$ to maximize $\text{LCS}(A, B[1..k] \cdot C \cdot B[k+1..N])$.
    - *2. Combinatorial Invariant*: Splitting $A$ at some index $i \in [0, M]$ and $C$ or $B$ requires knowing $\text{LCS}(A[i+1..M], B[k+1..N])$ for all $(i, k)$, or using Seaweed comb composition $P_{B[1..k]} \boxdot P_C \boxdot P_{B[k+1..N]}$.
    - *3. Algorithmic Compilation*: When $A$ is split into prefix/suffix and $C$ is matched against middle intervals of $A$, use Seaweed matrix on $C$ vs $A$ to get all interval LCS values $\text{LCS}(A[i..j], C)$ in $O(|A||C| + |A|^2)$ time, then combine with prefix LCS $dp_{\text{pref}}[i-1][k]$ and suffix LCS $dp_{\text{suff}}[j+1][k+1]$!
    - *4. Pitfall*: Trying to run Seaweed on $B$ instead of $A$ when $A$ is the string being partitioned into three contiguous segments $A[1..i-1], A[i..j], A[j+1..M]$.

31. **`[JA]` AtCoder ARC 145 E / AGC-style — Universal Subsequence Augmentation (Minimizing Additions to Increase $\iota(S)$)** ($N \le 2 \cdot 10^5, |\Sigma| = 26$)
    - *1. Diagnostic Signal*: Given $S[1..N]$ and $Q$ queries $(l, r)$, find the universality index $\iota(S[l..r])$ (the length of the Shortest Absent Subsequence of $S[l..r]$ minus $1$) in $O(\log N)$ time per query!
    - *2. Combinatorial Invariant*: By Theorem 88.2 (Hébrard's Arch Factorization), $\iota(S[l..r])$ is the maximum number of disjoint $1$-universal arches inside $[l, r]$. Starting from any $l$, the first arch ends at $f(l) = \max_{c \in \Sigma} \text{nxt}[l-1][c]$.
    - *3. Algorithmic Compilation*: Compute $f(l) = \max_{c \in \Sigma} \text{nxt}[l-1][c]$ for all $1 \le l \le N$ in $O(N|\Sigma|)$ time; then build a binary-lifting table $f^{2^k}(l)$ in $O(N \log N)$ time! For any query $[l, r]$, binary lift from $l$ while $f(cur) \le r$ in **$O(\log N)$ time per query** to get the exact number of arches $k = \iota(S[l..r])$, and read the remainder $R = S[cur .. r]$ to find a missing character for the SAS!
    - *4. Pitfall*: Off-by-one when transitioning from arch $A_1 = S[l .. f(l)]$ to the next arch start $f(l) + 1$ (the binary lifting table must jump $l \mapsto f(l) + 1$, and we count jumps where $f(l) \le r$).

32. **`[EN]` / `[ZH]` Universal Cup / QOJ — Dynamic All-Pairs Interval LCS under Appends & Prepends (`双端海草矩阵维护`)** ($N, Q \le 10^5$)
    - *1. Diagnostic Signal*: Maintain $B$ under character appends (and/or prepends) against a fixed small $A$ (or maintain Seaweed wires dynamically) while querying $\text{LCS}(A, B[l..r])$.
    - *2. Combinatorial Invariant*: Appending a character $B[N+1]$ adds one new vertical column $y = N+1$ to the right of the $M \times N$ Seaweed comb, requiring only $O(M)$ swaps down column $N+1$ using the current right-boundary exit wires `right_wire[1..M]`!
    - *3. Algorithmic Compilation*: Maintain the $M$ right-exit wire labels `right_wire[1..M]`. When $B[N+1] = c$ is appended, initialize a new top wire `v = M + N + 1` and push it down rows $x = 1 \dots M$: if $A[x] == c$ or `right_wire[x] > v`, `swap(right_wire[x], v)`. Record the bottom exit of `v` in a dynamic Fenwick / wavelet structure in $O(M + \log N)$ time per append!
    - *4. Pitfall*: Note that when `right_wire[x]` and `v` swap, the wire previously exiting on the right of row $x$ (which had $p(i) = \infty$) now exits at the **bottom of column $N+1$**, so its exit position changes from $p(i) = \infty$ to **$p(i) = N + 1$**! Updating $p(i) \leftarrow N+1$ makes online queries for $r < N+1$ unchanged (since $N+1 > r$ still holds!), while for $r \ge N+1$ we just count how many wires in $[l, r]$ still have $p(i) > r$ (i.e., either exited at column $\in (r, N_{\text{cur}}]$ or are currently in `right_wire[1..M]`)!

---

### 92.3 Cohort 2 Synthesis & Verification Checklist for Wave 4B

1. **DASG & Arch Factorization (`Iter 88`)**:
   - Derived canonical greedy match optimality ($\text{pos}_S(P)$) by exchange argument.
   - Connected Shortest Absent Subsequence (`SAS`) to Hébrard's Arch Factorization ($S = A_1 \dots A_k R$) and $O(\log N)$ range SAS queries via binary lifting on $f(l) = \max_{c \in \Sigma} \text{nxt}[l-1][c] + 1$.
   - Derived the unified Product Automaton $\mathcal{M}_A \times \mathcal{M}_B$ for `[HEOI2015] 最短不公共子串` (`Luogu P4112`), plus the 2D difference-array $O(|A||B|)$ alphabet-independent optimization for product DASG DP.
2. **Invertible Subsequence Automaton Matrices (`Iter 89`)**:
   - Resolved the apparent paradox of why $dp[c] \leftarrow 1 + \sum_{a \in \Sigma} dp[a]$ is invertible: $dp[c]$ is **included** in the right-hand sum, making the diagonal entry $(c, c)$ equal to $1$ and $\det(M_c) = 1$ over every commutative ring.
   - Derived the $O((N+Q)\sigma)$ prefix-matrix algorithm $\text{Ans}(l, r) = \mathbf{u}_r^T \cdot \mathbf{v}_{l-1}$ using $\mathbf{u}_i^T = 2\mathbf{u}_{i-1}^T - \mathbf{u}_{\text{last}[S[i]]-1}^T$ and a lazy global column offset $\mathbf{g}^{(i)}$ for $P_i^{-1}$, avoiding both Segment Trees and $O(N\sigma^2)$ matrix copies.
3. **Tiskin's Seaweed Matrices & Unit-Monge Algebra (`Iter 90`)**:
   - Proved the Planar Crossing Quadrangle Inequality and why the 2D cross-difference $\Delta(i, j)$ has row/column sums in $\{0, 1\}$.
   - Formulated the 3-line $O(MN)$ Seaweed Comb kernel (`if (A[x] == B[y] || u > col_wire[y]) swap(u, col_wire[y]);`), hand-checked on all 6 intervals of $B = \text{"aba"}$ vs $A = \text{"ab"}$, and explained $O(K \log K)$ Unit-Monge Braid Multiplication ($\boxdot$) and online character append maintenance.
4. **Bit-Parallel LCS & Edit Distance (`Iter 91`)**:
   - Proved the Allison–Dix / Hyyrö hardware borrow identity $D' = X \ \& \ \sim(X - S)$ from interval minimum-match capture, gave the exact 64-bit multi-word carry/borrow kernel, and coupled it with Hirschberg's linear-space divide-and-conquer and `DP套DP` mask transitions.
