# Cohort 3 Reconciled Master Report — Wave 4B (Iteration 112): Subsequence Automata (DASG), Invertible Subsequence Matrices, Tiskin's Seaweed Matrices & Bit-Parallel LCS

> [!IMPORTANT]
> **Cohort 3 Reconciliation & Blind-Spot Audit Mandate (`PLAN.md` §1–§3 & `AGENTS.md`)**
> This master document synthesizes and reconciles the two independent Phase 1 discovery cohorts for **Wave 4B**:
> - **Cohort 1 (`Iterations 36–40`)**: `strings_research/iter_36_to_40_subsequence_matrices_seaweed_bitparallel.md` (921 lines)
> - **Cohort 2 (`Iterations 88–92`)**: `strings_research/cohort2_iter_88_to_92_subsequence_matrices_seaweed_bitparallel.md` (825 lines)
>
> In addition to merging all complementary proofs, algorithmic optimizations, and non-template problems under the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**, this Cohort 3 report conducts an explicit cross-cohort blind-spot audit and fills remaining frontier gaps from `[ZH]` (`国家集训队论文 2021`), `[JA]` (`noshi91` / `maspypy` / `tatyam` treatises), and `[EN]` (Tiskin, Gawrychowski–Kociumaka–Manea) literature—including the **exact $O(K)$ monotone-staircase merge for Unit-Monge $\boxdot$ multiplication**, **Range LIS (`区间 LIS`) as a sparse 1-match-per-row Seaweed reduction in $O(N \log^2 N)$**, and **Simon's Congruence ($\sim_k$) / Arch-Tree Equivalence Testing**.

---

## 0. Cross-Cohort Comparison, Blind-Spot Audit & Reconciliation Ledger

### 0.1 What Cohort 1 Captured That Cohort 2 Missed

1. **Unified Three-Family LCS Dominance from a Single Seaweed Matrix (Cohort 1 Theorem 38.2)**:
   - Cohort 1 proved that a *single* $O(MN)$ Seaweed Comb on $A[1..M] \times B[1..N]$—storing bottom-wall exit labels $W[1..N] \in \{-M, \dots, -1\} \cup \{1, \dots, N\}$ and right-wall exit labels $R[1..M]$—simultaneously answers **three distinct $O(N^2) / O(MN)$ families of LCS queries** via 2D orthogonal range counting without running additional passes or storing $M$ row snapshots:
     1. *Whole $A$ vs. Substring of $B$*: $\text{LCS}(A[1..M], B[l..r]) = \#\{k \in [l, r] \mid W[k] < l\}$.
     2. *Suffix of $A$ vs. Prefix of $B$ (`后缀-前缀 LCS`)*: $\text{LCS}(A[i..M], B[1..j]) = \#\{k \in [1, j] \mid W[k] \le -i\}$.
     3. *Prefix of $A$ vs. Suffix of $B$ (`前缀-后缀 LCS`)*: $\text{LCS}(A[1..i], B[l..N]) = (N - l + 1) - \#\{k \in [l, N] \mid W[k] \ge l\} - \#\{i' \in [i+1, M] \mid R[i'] \ge l\}$.
   - *Cohort 2 Blind Spot*: Cohort 2 only derived Family 1 (via the inverse permutation $p(i) > r$) and suggested taking $M$ explicit row snapshots of `col_wire[1..N]` for prefix-substring queries, missing the fact that Suffix-Prefix and Prefix-Suffix LCS are directly encoded in the final perimeter permutation by initial-rank thresholding at $-i$.

2. **Upper-Unitriangular Fixed-Pattern Subsequence Matrices & Nilpotent Series Inverse (Cohort 1 §37.4A)**:
   - Cohort 1 derived the $(K+1) \times (K+1)$ upper-unitriangular matrix $A_c = I_{K+1} + \sum_{j : T[j] = c} E_{j-1, j}$ for counting occurrences of a fixed pattern $T[1..K]$ in $S[l..r]$ (with multiplicity or wildcards, e.g., `CF 1426F / 1666F`), and showed how to invert $A_c$ via $A_c^{-1} = \sum_{m=0}^K (-1)^m (A_c - I)^m$ even when $T$ has adjacent identical characters ($T[j] = T[j+1] = c$).
   - *Cohort 2 Blind Spot*: Cohort 2 focused exclusively on distinct-subsequence elementary matrices $M_c$ and tropical $5 \times 5$ matrices (`CF 750E`), omitting upper-unitriangular fixed-pattern matrix inversion.

3. **Singular Rank-Loss Counterexample for Gap-2 Range Distinct Subsequences (Cohort 1 §37.5 & `P-4B-21`)**:
   - Cohort 1 explicitly demonstrated why extending `ABC 214F` (non-adjacent distinct subsequences, $i_r - i_{r-1} \ge 2$) to range queries $S[l..r]$ **breaks matrix invertibility**: the buffered transition overwrites the old character state with a delayed sum, yielding $\det = 0$, and therefore requires Divide-and-Conquer / Segment Tree rather than prefix-matrix inversion.
   - *Cohort 2 Blind Spot*: Cohort 2 solved whole-string `ABC 214F` via scalar prefix sums, without analyzing the singular matrix failure mode for range queries.

4. **Double-Ended Deque Subsequence Matrix Stack (`P-4B-27`), RLE Seaweed Block Transitions (`P-4B-26`), Greene's $k$-LCS Theorem (`P-4B-28`), Semi-Local Myers Edit Distance Boundary (`P-4B-29`), and Constrained LCS Bit-Parallel Injection (`P-4B-31`)**:
   - Cohort 1 detailed how `push_front` swaps left/right multiplication roles ($P_{i-1} = M_c^{-1} P_i$) on a two-stack deque; how uniform match/mismatch rectangles in Run-Length Encoded strings act as interval shifts on seaweeds; why Myers' bit-parallel column step drops `| 1` in `(HP << 1)` when switching from global edit distance ($dp[0][j] = j$) to semi-local substring matching ($dp[0][j] = 0$); and how to inject bits between $K+1$ Allison–Dix bitsets for Constrained LCS (`CLCS`).

---

### 0.2 What Cohort 2 Captured That Cohort 1 Missed

1. **Hébrard's Arch Factorization, Universality Index $\iota(S)$ & $O(\log N)$ Range SAS via Binary Lifting (Cohort 2 Theorem 88.2 & Problem 31)**:
   - Cohort 2 formalized $k$-universality (a string containing all $\sigma^k$ words of length $k$ as subsequences), proved **Hébrard's Arch Factorization** $S = A_1 A_2 \dots A_k \cdot R$ (where each arch $A_r$ is a minimal $1$-universal substring), proved $\text{len}(\text{SAS}(S)) = \iota(S) + 1 = k + 1$, and showed how to compute $\iota(S[l..r])$ and reconstruct a Range Shortest Absent Subsequence in **$O(\log N)$ time per query** via binary lifting on the arch jump function $f(l) = \max_{c \in \Sigma} \text{nxt}[l-1][c] + 1$!
   - *Cohort 1 Blind Spot*: Cohort 1 noted the Complete-Alphabet Block Partition Law in 3 lines at the end of §36.3.4, but missed the formal Arch Factorization theorem, the witness construction via arch-final bottlenecks $m_1 \dots m_k m_{k+1}$ (`CF 1925C`), and the $O(\log N)$ binary-lifting range query reduction.

2. **Matrix-Free $O(N\sigma)$ Two-Term Vector Recurrence for Forward Prefix Row Sums (Cohort 2 Theorem 89.3)**:
   - Cohort 2 observed that when $P_i = M_{S[i]} P_{i-1}$ grows on the left, only row $c = S[i]$ of $P_{i-1}$ changes, and it is replaced by the sum of all rows of $P_{i-1}$, which is $\mathbf{u}_{i-1}^T = \mathbf{1}^T P_{i-1}$! Since the old row $c$ of $P_{i-1}$ was set at the previous occurrence $\text{last}[c]$ to $\mathbf{u}_{\text{last}[c]-1}^T$, the vector $\mathbf{u}_i^T = \mathbf{1}^T P_i$ obeys the direct scalar-like recurrence:
     $$\mathbf{u}_i^T = 2 \mathbf{u}_{i-1}^T - \mathbf{u}_{\text{last}[S[i]] - 1}^T!$$
     This eliminates maintaining the forward matrix $P_i$ altogether during precomputation!
   - *Cohort 1 Blind Spot*: Cohort 1 maintained the full $(\sigma+1)\times(\sigma+1)$ matrix $P$ in memory (updating column $x$ in $O(\sigma)$), which also takes $O(N\sigma)$ time but requires maintaining $P$ alongside $\mathbf{w}_i$. Combining Cohort 2's matrix-free $\mathbf{u}_i^T$ recurrence with the lazy-offset $\mathbf{v}_i$ vector yields the cleanest possible $O((N+Q)\sigma)$ implementation.

3. **Weighted Subsequence Matrices & Local Commutative Ring Unit Criterion (Cohort 2 Problem 26)**:
   - Cohort 2 generalized the elementary subsequence matrix to arbitrary multiplicative character weights $\alpha_c$ (or length indeterminate $x$), proving $\det(M_c(\alpha_c)) = \alpha_c$ and explicitly enforcing the `AGENTS.md` local algebraic hypothesis: $M_c(\alpha_c)$ is invertible over a commutative ring $\mathcal{R}$ **if and only if $\alpha_c \in \mathcal{R}^\times$ is a unit** (whereas unweighted $\alpha_c = 1$ is universally invertible over any ring $\mathbb{Z}/m\mathbb{Z}$).

4. **Alphabet-Independent $O(|A||B|)$ Product DASG Path Counting via 2D Difference Arrays (Cohort 2 Problem 28)**:
   - Cohort 2 proved that in $\text{DASG}(A) \times \text{DASG}(B)$, a matched pair $(i', j')$ with $A[i'] = B[j'] = c$ is the canonical transition from $(i, j)$ on character $c$ if and only if:
     $$(i, j) \in \bigl[\text{prev}_A[i'],\, i' - 1\bigr] \times \bigl[\text{prev}_B[j'],\, j' - 1\bigr].$$
     Thus each matching cell $(i', j')$ adds $dp[i'][j']$ to a 2D rectangle of predecessor states, reducing $O(|A||B||\Sigma|)$ to **$O(|A||B|)$ independent of $|\Sigma|$**!

5. **Direct Coupling of Bit-Parallel Allison–Dix LCS with `DP套DP` Automaton Precomputation (Cohort 2 Problem 27)**:
   - Cohort 2 showed that for outer automaton DP (`DP套DP`, Wave 4A) over LCS states of a short pattern $A$ ($|A| \le 20$), the Allison–Dix 4-instruction bitwise step $D' = X \mathbin{\&} \sim(X - S)$ computes the entire DFA transition table `trans[D][c]` directly on bitmasks in $O(2^{|A|}|\Sigma|)$ without ever unpacking bitmasks into DP arrays!

---

### 0.3 Frontier & Obscure Topics Added in Cohort 3 Gap-Hunting

1. **Exact $O(K)$ Monotone-Staircase Merge Algorithm for Unit-Monge Distance Multiplication ($\boxdot$) & $O(K \log K)$ Vector-Matrix Query Propagation (`[国家集训队论文 2021]`)**:
   - Both Cohort 1 and Cohort 2 summarized Tiskin's $O(K \log K)$ divide-and-conquer at a high level. In Section 4.4 below, we derive the **exact $O(K)$ merge invariant** (how the cross-difference permutation $P = P_1 \boxdot P_2$ is stitched together from $Q_L = P_{1,L} \boxdot P_{2,L}$ and $Q_R = P_{1,R} \boxdot P_{2,R}$ via a single $2K$-step staircase walk) and explain how to propagate a query vector across $O(\log M)$ Segment Tree nodes using **SMAWK / Monotone Minima ($O(K \log K)$ vector-matrix $\boxdot$)** instead of full matrix-matrix products!
2. **Range LIS (`区间最长上升子序列`) in $O(N \log^2 N)$ as a Sparse 1-Match-Per-Row Seaweed Reduction (`[国家集训队论文 2021]`, `Universal Cup`)**:
   - Because $\text{LIS}(B[l..r]) = \text{LCS}\bigl((1, 2, \dots, N),\, B[l..r]\bigr)$, computing the Seaweed Matrix of the identity permutation $A = (1, \dots, N)$ against a permutation $B[1..N]$ answers all range LIS queries $[l, r]$ in $O(\log N)$ time! Moreover, since each row of $A$ matches only **one** column of $B$, dividing and conquering over the value range $[1, N]$ using Unit-Monge $\boxdot$ builds the entire Seaweed permutation in **$O(N \log^2 N)$ time** (avoiding the $O(N^2)$ grid sweep!).
3. **Simon's Congruence ($\sim_k$), Piecewise Testable Equivalence & Universal Arch Trees (Barker et al. 2020 / Gawrychowski et al. 2021)**:
   - In Section 1.5, we derive the characterization of **Simon's Congruence $U \sim_k V$** (two strings sharing the exact same set of subsequences of length $\le k$) and show how canonical DASG coordinates and Arch Factorization compute the **Simon Congruence Distance** (the smallest $k$ where $\text{Subseq}_k(U) \ne \text{Subseq}_k(V)$, i.e., the length of the **Shortest Distinguishing Subsequence** between $U$ and $V$).

---

## 1. Directed Acyclic Subsequence Graph (`序列自动机` / DASG), Arch Factorization, Simon's Congruence & Product Automata

### 1.1 Step 1: The Diagnostic Signal (Why Suffix Structures Fail on Subsequences)

A Suffix Automaton (SAM) or Suffix Tree of $S[1..N]$ compresses all $O(N^2)$ **contiguous substrings** into $O(N)$ states because occurrences of a contiguous factor shift rigidly by $+1$ under right-extension. By contrast, $S[1..N]$ contains up to $2^N$ **subsequences** (scattered factors), and a single subsequence $P$ can occur at exponentially many index tuples $1 \le i_1 < i_2 < \dots < i_{|P|} \le N$.
Whenever a problem asks to:
- Recognize whether $P$ is a subsequence of $S[l..r]$, or count prefixes/extensions of $P$ inside $S$;
- Count **distinct** subsequences of $S$ (each string $P \preceq S$ counted once regardless of multiplicity), or find the $K$-th lexicographically smallest subsequence;
- Find the **Shortest Absent Subsequence (`SAS` / `最短缺失子序列`)** or **Universality Index $\iota(S[l..r])$**;
- Compare two strings $A, B$ across **contiguous substrings vs. scattered subsequences** (`[HEOI2015] 最短不公共子串` / `Luogu P4112`);

we must collapse the $2^N$ subset states of the subsequence NFA by assigning every subsequence $P \preceq S$ a **unique canonical occurrence** inside $S$.

---

### 1.2 Step 2: The Combinatorial Word Invariants (Leftmost Greedy Dominance & Hébrard's Arch Factorization)

#### Theorem 1.1 (Leftmost-Prefix Dominance / Canonical Subsequence Embedding)
Given $S[1..N]$ over alphabet $\Sigma$, define the **canonical greedy match position** $\text{first\_end}_S(P) \in \{0, 1, \dots, N\} \cup \{\infty\}$ of a word $P \in \Sigma^*$ inductively by:
$$\text{first\_end}_S(\varepsilon) = 0, \qquad \text{first\_end}_S(P \cdot c) = \min\bigl\{\, j \in [\text{first\_end}_S(P) + 1,\, N] \;\big|\; S[j] = c \,\bigr\}$$
with $\min \emptyset = \infty$. Then for every continuation string $W \in \Sigma^*$:
$$P \cdot W \text{ is a subsequence of } S[1..N] \iff \text{first\_end}_S(P) \le N \text{ and } W \text{ is a subsequence of } S\bigl[\text{first\_end}_S(P)+1 .. N\bigr].$$

*Proof (Exchange Argument).*
- ($\Leftarrow$) If $\text{first\_end}_S(P) = i \le N$, then $P$ embeds into $S[1..i]$. Any embedding of $W$ into $S[i+1..N]$ concatenates with the embedding of $P$ to form a strictly increasing embedding of $P \cdot W$ into $S[1..N]$.
- ($\Rightarrow$) Suppose $P \cdot W$ embeds into $S$ at indices $1 \le j_1 < \dots < j_m < k_1 < \dots < k_{|W|} \le N$, where $S[j_r] = P[r]$ and $S[k_r] = W[r]$. By induction on $r = 1, \dots, m$, we have $\text{first\_end}_S(P[1..r]) \le j_r$:
  - Base $r = 1$: $\text{first\_end}_S(P[1]) = \min\{j \ge 1 \mid S[j] = P[1]\} \le j_1$.
  - Step $r-1 \to r$: Since $\text{first\_end}_S(P[1..r-1]) \le j_{r-1} < j_r$ and $S[j_r] = P[r]$, index $j_r$ belongs to the candidate set $\{j > \text{first\_end}_S(P[1..r-1]) \mid S[j] = P[r]\}$, so the minimum is $\le j_r$.
  At $r = m$, $\text{first\_end}_S(P) \le j_m < k_1$, so $k_1, \dots, k_{|W|} \in [\text{first\_end}_S(P)+1, N]$, proving $W \preceq S[\text{first\_end}_S(P)+1..N]$. $\blacksquare$

#### Corollary 1.2 (Myhill–Nerode Quotient & Bijection of the DASG)
By Theorem 1.1, the Myhill–Nerode right-congruence class of $P \in \Sigma^*$ with respect to $\text{Subseq}(S)$ depends **only** on the single integer $\text{first\_end}_S(P) \in \{0, 1, \dots, N, \infty\}$. Thus the **Directed Acyclic Subsequence Graph ($\text{DASG}(S)$ / `序列自动机`)** has:
- **States**: $\{0, 1, \dots, N\}$ (plus dead sink $\infty$ / $\bot$).
- **Transitions**: For $i \in \{0, \dots, N\}$ and $c \in \Sigma$:
  $$\delta_{\text{DASG}}(i, c) = \text{nxt}[i][c] := \min\{\, j \in [i+1, N] \mid S[j] = c \,\}.$$
- **Path Bijection**: Every distinct subsequence $P \in \text{Subseq}(S)$ corresponds **bijectively** to a directed path $0 \xrightarrow{P[1]} i_1 \xrightarrow{P[2]} \dots \xrightarrow{P[m]} i_m$ in $\text{DASG}(S)$.

#### Theorem 1.3 (Hébrard's Arch Factorization & Shortest Absent Subsequence Duality)
A string $U \in \Sigma^*$ is called **$k$-universal** over $\Sigma$ (where $\sigma = |\Sigma|$) if every word $W \in \Sigma^k$ of length $k$ appears as a subsequence of $U$. The **universality index** $\iota(S)$ is the maximum $k \ge 0$ such that $S$ is $k$-universal, and a **Shortest Absent Subsequence (`SAS`)** of $S$ is a minimum-length string $W \in \Sigma^* \setminus \text{Subseq}(S)$.
Factorize $S$ greedily from left to right into minimal $1$-universal substrings (**arches**):
$$S = A_1 A_2 \dots A_k \cdot R$$
where each $A_r = S[l_r .. r_r]$ ($l_1 = 1, l_{r} = r_{r-1} + 1$) is the **shortest** prefix of $S[l_r .. N]$ containing all $\sigma$ characters of $\Sigma$, and the **rest** $R = S[l_{k+1}..N]$ misses at least one character of $\Sigma$ ($\text{alph}(R) \subsetneq \Sigma$). Then:
1. $\iota(S) = k$, and every Shortest Absent Subsequence of $S$ has length **$\text{len}(\text{SAS}(S)) = k + 1$**.
2. Choosing the bottleneck character $m_r = S[r_r]$ at the end of each arch $A_r$ ($r = 1, \dots, k$) together with any character $m_{k+1} \in \Sigma \setminus \text{alph}(R)$ yields an explicit Shortest Absent Subsequence $M = m_1 m_2 \dots m_k m_{k+1}$ of length $k+1$.

*Proof.*
1. **Any $W \in \Sigma^k$ is a subsequence of $S$**: Since each arch $A_r$ contains every character of $\Sigma$, we can match $W[r]$ inside $A_r$ for $r = 1, \dots, k$. Thus $\iota(S) \ge k$ and $|\text{SAS}(S)| \ge k + 1$.
2. **Explicit absent witness $M = m_1 \dots m_k m_{k+1}$ of length $k+1$**: By minimality of $r_r$, the final character $m_r = S[r_r]$ of arch $A_r = S[l_r .. r_r]$ does **not** occur anywhere in $S[l_r .. r_r - 1]$. By induction on $r = 1, \dots, k$, $\text{first\_end}_S(m_1 \dots m_r) = r_r = l_{r+1} - 1$. Finally, after matching $m_1 \dots m_k$ at $r_k = l_{k+1} - 1$, character $m_{k+1} \notin \text{alph}(R)$ does not occur in $R = S[l_{k+1}..N]$, so $\text{first\_end}_S(M) = \infty$. $\blacksquare$

---

### 1.3 Step 3: Reverse-Engineering Scratchpad (DASG Representations, Range Arch Binary Lifting & Four-Comb Product Automata)

#### 1. Three Canonical DASG Representations by Alphabet Regime
| Alphabet Regime | Representation | Build Time & Space | Transition $\text{nxt}[i][c]$ | Out-Degree Sweep |
| :--- | :--- | :--- | :--- | :--- |
| **Small Alphabet** ($\sigma \le 62$) | Flat 2D array `nxt[N+1][sigma]` swept backwards $i = N-1 \downarrow 0$ | $O(N \sigma)$ time & space | $O(1)$ | $O(\sigma)$ |
| **Large Alphabet, Point Lookups** ($\sigma \le N$) | Per-character sorted occurrence vectors `pos[c]` | $O(N)$ time & space | $O(\log(\text{freq}_c))$ via `upper_bound` | N/A |
| **Large Alphabet, Full Out-Edges** ($\sigma \le N$) | **Persistent Segment Tree** over $[1, \sigma]$ (`rt[i]` updates leaf $S[i+1] \leftarrow i+1$ from `rt[i+1]`) | $O(N \log \sigma)$ time & space | $O(\log \sigma)$ | $O(\log \sigma)$ per subtree aggregate |

#### 2. Hand-Checkable Trace of $\text{DASG}(\texttt{abac})$
Let $S = \texttt{abac}$ ($N = 4, \Sigma = \{\texttt{a}, \texttt{b}, \texttt{c}\}$):
| State $i$ | $S[i]$ | $\text{nxt}[i][\texttt{a}]$ | $\text{nxt}[i][\texttt{b}]$ | $\text{nxt}[i][\texttt{c}]$ | $dp[i]$ (# Subsequences of $S[i+1..4]$ incl. $\varepsilon$) | SAS Distance $d[i]$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $4$ | $\texttt{c}$ | $\infty$ | $\infty$ | $\infty$ | $1$ ($\varepsilon$) | $1$ ($\texttt{a}, \texttt{b}, \texttt{c}$) |
| $3$ | $\texttt{a}$ | $\infty$ | $\infty$ | $4$ | $1 + dp[4] = 2$ | $1$ ($\texttt{a}, \texttt{b}$) |
| $2$ | $\texttt{b}$ | $3$ | $\infty$ | $4$ | $1 + dp[3] + dp[4] = 4$ | $1$ ($\texttt{b}$) |
| $1$ | $\texttt{a}$ | $3$ | $2$ | $4$ | $1 + dp[3] + dp[2] + dp[4] = 8$ | $2$ ($1 + \min(1,1,1)$) |
| $0$ | (root) | $1$ | $2$ | $4$ | $1 + dp[1] + dp[2] + dp[4] = 14$ | $2$ (e.g., $\texttt{bb}$, $\texttt{ca}$) |

Notice how $S = \texttt{abac}$ has **one** complete arch $A_1 = \texttt{abac}$ ($r_1 = 4$) and empty remainder $R = \varepsilon$, so $\iota(S) = 1$ and $\text{len}(\text{SAS}(S)) = 2 = d[0]$.

#### 3. $O(\log N)$ Range Shortest Absent Subsequence (`Range SAS` / `区间最短缺失子序列`) via Binary Lifting
To answer $Q$ queries asking for $\iota(S[l..r])$ or the length/witness of $\text{SAS}(S[l..r])$:
- For every start position $i \in \{0, \dots, N\}$ (corresponding to substring start $l = i + 1$), the first complete arch starting at $i+1$ ends at:
  $$\text{arch\_end}[i] = \max_{c \in \Sigma} \text{nxt}[i][c].$$
- Build a binary-lifting table $\text{up}[k][i]$ ($2^k$-th iterate of $i \mapsto \text{arch\_end}[i]$) in $O(N \log N)$ time.
- For a query $[l, r]$, start at $u = l - 1$ and binary lift across $k = \lfloor \log_2 N \rfloor \downarrow 0$: whenever $\text{up}[k][u] \le r$, advance $u \leftarrow \text{up}[k][u]$ and add $2^k$ to the arch count $\iota$.
- The number of complete arches in $S[l..r]$ is $\iota$, the SAS length is $\iota + 1$, and any character $c$ with $\text{nxt}[u][c] > r$ can serve as the final absent character $m_{\iota+1}$!

#### 4. The Four-Comb Product Automaton (`[HEOI2015] 最短不公共子串` / `Luogu P4112`) & $O(|A||B|)$ Rectangle Optimization
Given strings $A$ and $B$, any combination of **Substring ($\text{SAM}$)** vs. **Subsequence ($\text{DASG}$)** recognition for $L(\mathcal{A}^+(A)) \setminus L(\mathcal{A}^-(B))$ is solved by running unweighted BFS on the product automaton $\mathcal{A}^+(A) \times \mathcal{A}^-(B)$ from $(q_0^+, q_0^-)$:
- Every transition $(u, v) \xrightarrow{c} (\delta^+(u, c), \delta^-(v, c))$ with $\delta^+(u, c) \ne \bot$ and $\delta^-(v, c) = \bot$ at BFS depth $d$ yields an uncommon witness of length $d + 1$.
- **Alphabet-Independent $O(|A||B|)$ Optimization for $\text{DASG}(A) \times \text{DASG}(B)$ Path Counting**:
  When counting paths in $\text{DASG}(A) \times \text{DASG}(B)$ (e.g., distinct common subsequences of $A$ and $B$), a pair $(i', j')$ with $A[i'] = B[j'] = c$ is the canonical transition target $(\text{nxt}_A[i][c], \text{nxt}_B[j][c])$ from state $(i, j)$ **if and only if**:
  $$\text{prev}_A[i'] \le i < i' \quad \text{and} \quad \text{prev}_B[j'] \le j < j',$$
  where $\text{prev}_A[i'] = \max(\{0\} \cup \{p < i' \mid A[p] = A[i']\})$. Thus each matching cell $(i', j')$ contributes $dp[i'][j']$ to the 2D predecessor rectangle $[\text{prev}_A[i'], i'-1] \times [\text{prev}_B[j'], j'-1]$, reducing $O(|A||B||\Sigma|)$ to **$O(|A||B|)$ time** via 2D prefix/difference arrays!

---

### 1.4 Step 4: Frontier Extension — Simon's Congruence ($\sim_k$) & Shortest Distinguishing Subsequence (Gawrychowski et al. 2021)

#### Object & Question
Two strings $U, V \in \Sigma^*$ are **Simon-congruent at level $k$**, written $U \sim_k V$, if they have the **exact same set of subsequences of length $\le k$**:
$$U \sim_k V \iff \text{Subseq}_{\le k}(U) = \text{Subseq}_{\le k}(V).$$
Given $U$ and $V$, what is the **Shortest Distinguishing Subsequence (`SDS`)**—a minimum-length string $W \in \Sigma^*$ that is a subsequence of **exactly one** of $U$ and $V$ (so $|W| = k^* + 1$ where $k^*$ is the maximum $k$ with $U \sim_k V$)?

#### Structural Solution
1. **Quadratic Regime ($|U|, |V| \le 3000$)**: Run BFS on the symmetric difference of $\text{DASG}(U)$ and $\text{DASG}(V)$—namely, on $\text{DASG}(U) \times \text{DASG}(V)$ starting from $(0, 0)$, stop at the first transition $(u, v) \xrightarrow{c} (\text{nxt}_U[u][c], \text{nxt}_V[v][c])$ where **exactly one** of the two target states is $\infty$!
2. **Linear-Time Regime ($|U|, |V| \le 10^6$, Barker et al. 2020 / Gawrychowski–Kociumaka–Kosche–Manea 2021)**:
   - For each index $i$ in $U$, define its **backward universality rank vector** $(r_c(i))_{c \in \Sigma}$ specifying the minimum length of a subsequence ending with $c$ at $i$ that is unique to $U[1..i]$.
   - Using the **Simon-Tree** (hierarchical partitioning of $U$ and $V$ by backwards arch decomposition), $U \sim_k V$ and the exact shortest distinguishing witness $W$ can be computed in **$O(|U| + |V|)$ time** independent of $|\Sigma|$!

---

### 1.5 Step 4 (Cont.): Boundary Pitfalls & Broken-Invariant Counterexamples for DASG

1. **Fatal Bug — Taking `link[v]` in $\text{SAM}(B)$ During Product Automaton BFS (`[HEOI2015] 最短不公共子串`)**:
   - In streaming LCS over $\text{SAM}(B)$, when $\delta_B(v, c) = \bot$ one follows `link[v]` to drop characters from the *front* of the matched string. In the product automaton $\mathcal{A}^+(A) \times \text{SAM}(B)$, following `link[v]` checks whether a *proper suffix* of $W \cdot c$ occurs in $B$, whereas $W \cdot c \in \text{Substr}(B)$ requires the **entire string** $W \cdot c$ to walk from the root of $\text{SAM}(B)$ without ever falling off! Thus $\text{SAM}(B)$ must be treated as a pure forward DAG with zero suffix-link fallbacks during BFS.
2. **Subtraction Overflow Trap in Length-Stratified DASG Counting (`CF 1183H`)**:
   - When clamping subsequence counts at $\min(K, \dots)$ to avoid 64-bit overflow ($K \le 10^{18}$), you **cannot** use the $O(N)$ recurrence $dp[i] = 2 dp[i-1] - dp[\text{prev}[i]-1]$ because subtracting two values both clamped at $K$ yields $2K - K = K$ (or $K - K = 0$), destroying the true count! Whenever clamping at $K$, always sum purely additively over the $\le |\Sigma|$ outgoing DASG transitions $dp[u] = \min\bigl(K, 1 + \sum_{c} dp[\text{nxt}[u][c]]\bigr)$.
3. **Greedy SAS Tie-Breaking Failure (`ARC 081 E`)**:
   - Jumping greedily forward to $\arg\max_{c} \text{nxt}[u][c]$ finds the correct *length* $\iota(S) + 1$ of the SAS, but fails to find the **lexicographically smallest** SAS! For example, on $S = \texttt{bacb}$ ($\Sigma = \{\texttt{a}, \texttt{b}, \texttt{c}\}$), at $u = 0$, $\text{nxt}[0] = (\texttt{a}\to 2, \texttt{b}\to 1, \texttt{c}\to 3)$. Both $\texttt{a}$ (at $2$, missing $\texttt{a}$ afterwards $\implies \texttt{aa}$) and $\texttt{c}$ (at $3$, missing $\texttt{a}$ afterwards $\implies \texttt{ca}$) lead to absent strings of length $2$, so $\texttt{aa} <_{\text{lex}} \texttt{ca}$ wins even though $\text{nxt}[0][\texttt{a}] = 2 < \text{nxt}[0][\texttt{c}] = 3$! Always compute backward distances $d[u]$ first, then step to the **smallest character $c$** with $d[\text{nxt}[u][c]] = d[u] - 1$.

---

## 2. Invertible Subsequence Automaton Matrices (`子序列 DP 矩阵可逆性`) & Fast Range Subsequence Algebra

### 2.1 Step 1: The Diagnostic Signal (Why Segment Trees of $(\sigma+1)\times(\sigma+1)$ Matrices TLE)

Given a string $S[1..N]$ over an alphabet of size $\sigma = |\Sigma|$ (e.g., $\sigma = 26$) and $Q$ range queries $[l, r]$ ($N, Q \le 2 \cdot 10^5$ or $10^6$), we must compute the number of **distinct subsequences** of $S[l..r]$ modulo $M$ (e.g., $10^9 + 7$).
- A Segment Tree storing $(\sigma+1)\times(\sigma+1)$ DP transition matrices takes $O(N \sigma^3 + Q \sigma^2 \log N)$ time—for $\sigma = 26$, $\sigma^3 \approx 1.9 \times 10^4$ operations per node, causing TLE/MLE.
- **Why Naive Intuition Thinks the DP Is Non-Invertible**: In the classic recurrence $w_c \leftarrow 1 + \sum_{a \in \Sigma} w_a$, it looks as though the old value $w_c$ is overwritten and lost.
- **The Algebraic Breakthrough**: The old value $w_c$ is **included inside the sum $\sum_{a \in \Sigma} w_a$ with coefficient $+1$**! Thus the transition matrix $M_c$ is an **elementary row/column addition matrix with determinant $\det(M_c) = 1$**, invertible over **every commutative ring $\mathcal{R}$** in $O(1)$ non-zero off-diagonal entries!

---

### 2.2 Step 2: The Combinatorial & Algebraic Invariant (Elementary Transvection Matrices & Exact Inverses)

#### Theorem 2.1 (Bijective Non-Destructive Partition & Determinant-1 Elementary Matrix)
For any string $T \in \Sigma^*$, let $w_a(T)$ ($a \in \{1, \dots, \sigma\}$) be the number of distinct non-empty subsequences of $T$ whose **last character** is $a$, and let $w_{\sigma+1}(T) = 1$ count the empty string $\varepsilon$. Write the column vector $\mathbf{w}(T) = (w_1(T), \dots, w_\sigma(T), w_{\sigma+1}(T))^T$.
When character $c \in \{1, \dots, \sigma\}$ is appended to $T$:
- Every $u \in \text{Subseq}(T)$ bijectively forms a unique subsequence $u \cdot c$ ending in $c$, so $w_c(T \cdot c) = \sum_{j=1}^{\sigma+1} w_j(T)$, while $w_a(T \cdot c) = w_a(T)$ for all $a \ne c$.
- In matrix form, $\mathbf{w}(T \cdot c) = M_c \mathbf{w}(T)$, where $M_c \in \mathbb{Z}^{(\sigma+1)\times(\sigma+1)}$ is the identity matrix $I_{\sigma+1}$ except that **row $c$ is all $1$s**:
  $$M_c = I_{\sigma+1} + \mathbf{e}_c \sum_{j \ne c} \mathbf{e}_j^T, \qquad (M_c)_{r, j} = \begin{cases} 1 & \text{if } r = c \text{ or } r = j, \\ 0 & \text{otherwise.} \end{cases}$$
- Over **any commutative ring $\mathcal{R}$** (even modulo a composite integer $m$ with zero divisors!), $\det(M_c) = 1$, and its exact inverse $M_c^{-1}$ is $I_{\sigma+1}$ except that **row $c$ has $-1$ in every off-diagonal column $j \ne c$**:
  $$M_c^{-1} = I_{\sigma+1} - \mathbf{e}_c \sum_{j \ne c} \mathbf{e}_j^T, \qquad (M_c^{-1})_{r, j} = \begin{cases} 1 & \text{if } r = j, \\ -1 & \text{if } r = c \text{ and } j \ne c, \\ 0 & \text{otherwise.} \end{cases}$$

*Proof.* Multiplying out $(I + \mathbf{e}_c \sum_{j \ne c} \mathbf{e}_j^T)(I - \mathbf{e}_c \sum_{k \ne c} \mathbf{e}_k^T)$ and using $\mathbf{e}_j^T \mathbf{e}_c = 0$ for $j \ne c$ gives $I + \mathbf{e}_c \sum_{j \ne c} \mathbf{e}_j^T - \mathbf{e}_c \sum_{k \ne c} \mathbf{e}_k^T - 0 = I_{\sigma+1}$. $\blacksquare$

#### Corollary 2.2 (Weighted Generalization & Local Ring Invertibility Hypothesis)
If each character $c \in \Sigma$ carries a multiplicative weight $\alpha_c \in \mathcal{R}$ (so the weight of a subsequence $W$ is $\prod_{k=1}^{|W|} \alpha_{W[k]}$, or $\alpha_c = x$ to track subsequence lengths), then row $c$ of $M_c(\alpha_c)$ is $(\alpha_c, \alpha_c, \dots, \alpha_c, 1 + \dots)$: specifically, under canonical last-occurrence replacement, $w_c(T \cdot c) = \alpha_c \sum_{j=1}^{\sigma+1} w_j(T)$, so row $c$ of $M_c(\alpha_c)$ is filled with $\alpha_c$, giving:
$$\det\bigl(M_c(\alpha_c)\bigr) = \alpha_c.$$
- **Local Algebraic Hypothesis (`AGENTS.md`)**: $M_c(\alpha_c)$ is invertible over the commutative ring $\mathcal{R}$ **if and only if $\alpha_c \in \mathcal{R}^\times$ is a unit** (e.g., $\gcd(\alpha_c, m) = 1$ in $\mathbb{Z}/m\mathbb{Z}$, or $\alpha_c \not\equiv 0 \pmod p$ in a field $\mathbb{F}_p$). When $\alpha_c \in \mathcal{R}^\times$, $M_c(\alpha_c)^{-1}$ has $\alpha_c^{-1}$ at entry $(c, c)$ and $-1$ at entries $(c, j)$ for $j \ne c$.

---

### 2.3 Step 3: Reverse-Engineering Scratchpad (Reconciled Matrix-Free $O((N+Q)\sigma)$ Algorithm)

By combining **Cohort 2's matrix-free forward recurrence** for $\mathbf{u}_i^T = \mathbf{1}^T P_i$ with **Cohort 1 & 2's lazy-offset inverse maintenance** for $\mathbf{v}_i = P_i^{-1} \mathbf{e}_{\sigma+1}$, we obtain an algorithm that **never allocates a $(\sigma+1)\times(\sigma+1)$ matrix at each index $i$** and runs in **$O((N+Q)\sigma)$ time and $O(N\sigma)$ space**:

#### Mathematical Derivation of the Bilinear Dot Product $\text{Ans}(l, r) = \mathbf{u}_r^T \cdot \mathbf{v}_{l-1}$
Define the prefix matrix product:
$$P_i = M_{S[i]} M_{S[i-1]} \cdots M_{S[1]} \qquad (P_0 = I_{\sigma+1}).$$
Then the transition matrix for substring $S[l..r]$ is $M_{S[r]} \cdots M_{S[l]} = P_r P_{l-1}^{-1}$, and the total number of distinct subsequences of $S[l..r]$ (including $\varepsilon$) is:
$$\text{Ans}(l, r) = \mathbf{1}^T \bigl(M_{S[r]} \cdots M_{S[l]}\bigr) \mathbf{e}_{\sigma+1} = \underbrace{\bigl(\mathbf{1}^T P_r\bigr)}_{\mathbf{u}_r^T \in \mathcal{R}^{1 \times (\sigma+1)}} \cdot \underbrace{\bigl(P_{l-1}^{-1} \mathbf{e}_{\sigma+1}\bigr)}_{\mathbf{v}_{l-1} \in \mathcal{R}^{(\sigma+1) \times 1}} = \sum_{k=1}^{\sigma+1} u_r[k] \cdot v_{l-1}[k].$$

1. **How $\mathbf{u}_i^T = \mathbf{1}^T P_i$ Updates in $O(\sigma)$ Time Without Storing $P_i$**:
   - Since $P_i = M_{S[i]} P_{i-1}$, left-multiplying by $M_c$ ($c = S[i]$) leaves all rows $r \ne c$ of $P_{i-1}$ unchanged, and replaces row $c$ with the sum of all rows of $P_{i-1}$, which is $\mathbf{1}^T P_{i-1} = \mathbf{u}_{i-1}^T$!
   - What was row $c$ of $P_{i-1}$ just before step $i$? If $c$ last appeared at index $p = \text{last}[c] \ge 1$, row $c$ was set at step $p$ to $\mathbf{u}_{p-1}^T$; if $c$ never appeared before ($p = 0$), row $c$ is still row $c$ of $P_0 = I_{\sigma+1}$, which is $\mathbf{e}_c^T$!
   - Therefore, for all $i = 1, \dots, N$ (with $c = S[i]$):
     $$\boxed{\mathbf{u}_i^T = 2 \mathbf{u}_{i-1}^T - \begin{cases} \mathbf{u}_{\text{last}[c] - 1}^T & \text{if } \text{last}[c] \ge 1, \\ \mathbf{e}_c^T & \text{if } \text{last}[c] = 0! \end{cases}}$$

2. **How $\mathbf{v}_i = P_i^{-1} \mathbf{e}_{\sigma+1}$ Updates in $O(\sigma)$ Time via Lazy Column Offset**:
   - Since $P_i^{-1} = P_{i-1}^{-1} M_{S[i]}^{-1}$, right-multiplying by $M_c^{-1}$ leaves column $c$ of $P_{i-1}^{-1}$ unchanged, and **subtracts column $c$ from every other column $k \ne c$** (including column $\sigma+1$)!
   - Represent each column $k \in \{1, \dots, \sigma+1\}$ of $P_i^{-1}$ as $\mathbf{c}_k = \tilde{\mathbf{c}}_k + \mathbf{g}$, where $\mathbf{g} \in \mathcal{R}^{\sigma+1}$ is a global lazy offset vector (initially $\mathbf{g} = \mathbf{0}$ and $\tilde{\mathbf{c}}_k = \mathbf{e}_k$).
   - At step $i$ ($c = S[i]$), read the true column $c$: $\mathbf{w} = \tilde{\mathbf{c}}_c + \mathbf{g}$. Subtract $\mathbf{w}$ from all columns via $\mathbf{g} \leftarrow \mathbf{g} - \mathbf{w}$, and restore column $c$ via $\tilde{\mathbf{c}}_c \leftarrow \tilde{\mathbf{c}}_c + \mathbf{w}$.
   - Then the $(\sigma+1)$-th column of $P_i^{-1}$ (since $c \in \{1, \dots, \sigma\}$ never equals $\sigma+1$) is simply:
     $$\boxed{\mathbf{v}_i = \mathbf{c}_{\sigma+1}^{(i)} = \mathbf{e}_{\sigma+1} + \mathbf{g}^{(i)}!}$$

#### Complete Algorithm Contract: $O((N+Q)\sigma)$ Range Distinct Subsequences
```
Precomputation (O(N * sigma) time and space):
1. Initialize u[0][1..sigma+1] = (1, 1, ..., 1), v[0][1..sigma+1] = (0, ..., 0, 1).
   Initialize last[1..sigma] = 0, g[1..sigma+1] = 0, c_tilde[k][r] = [k == r] for k, r in 1..sigma+1.
2. For i = 1 to N (let c = S[i] in 1..sigma):
   // 1. Update u[i] in O(sigma):
   For k = 1 to sigma + 1:
       old_row_c = (last[c] == 0) ? (k == c ? 1 : 0) : u[last[c] - 1][k]
       u[i][k] = (2 * u[i - 1][k] - old_row_c) mod MOD
   last[c] = i
   // 2. Update v[i] in O(sigma) via lazy column offset g:
   For r = 1 to sigma + 1:
       w_r = (c_tilde[c][r] + g[r]) mod MOD
       g[r] = (g[r] - w_r) mod MOD
       c_tilde[c][r] = (c_tilde[c][r] + w_r) mod MOD
       v[i][r] = (g[r] + (r == sigma + 1 ? 1 : 0)) mod MOD

Query(l, r) in O(sigma) time:
   Return (sum_{k=1}^{sigma+1} u[r][k] * v[l - 1][k] - 1) mod MOD   // -1 for non-empty subsequences
```

---

### 2.4 Step 4: Extensions & Broken-Invariant Counterexamples for Subsequence Matrices

| Extension / Problem Setting | Matrix Dimension & Algebraic Structure | Invertible? | Optimal Query Strategy |
| :--- | :--- | :---: | :--- |
| **Range Distinct Subsequences** ($S[l..r]$) | $(\sigma+1)\times(\sigma+1)$ elementary matrix $M_c$ over $\mathbb{Z}/m\mathbb{Z}$ | **Yes** ($\det = 1$) | Prefix vectors $\mathbf{u}_r^T \cdot \mathbf{v}_{l-1}$ in **$O(\sigma)$ per query** |
| **Range Weighted / Length-GF Distinct Subsequences** | $(\sigma+1)\times(\sigma+1)$ matrix $M_c(\alpha_c)$ | **Iff $\alpha_c \in \mathcal{R}^\times$** ($\det = \alpha_c$) | Prefix vectors $\mathbf{u}_r^T \cdot \mathbf{v}_{l-1}$ in **$O(\sigma)$ per query** |
| **Range Fixed-Pattern Multiplicity** ($T[1..K]$ in $S[l..r]$) | $(K+1)\times(K+1)$ upper-unitriangular $A_c = I + \sum_{T[j]=c} E_{j-1,j}$ | **Yes** ($\det = 1$) | Prefix upper-unitriangular $Q_{l-1} P_r$ in **$O(K)$ per query** |
| **Deque Updates (`push/pop_front/back`) + Range $[l, r]$** | Two-stack prefix/inverse products anchored at index $0$ | **Yes** ($\det = 1$) | Front stack $P_{-i} = M_c^{-1} P_{-(i-1)}$, back stack $P_i = P_{i-1} M_c$ in **$O(\sigma)$** |
| **Range Min-Deletions to Avoid/Contain Pattern** (`CF 750E`, `CF 1609E`) | $(K+1)\times(K+1)$ matrix over **Tropical Semiring $(\mathbb{Z}\cup\{\infty\}, \min, +)$** | **No** ($\min$ has no inverse) | **Segment Tree** of $(K+1)\times(K+1)$ tropical matrices, vector propagation in **$O(K^2 \log N)$** |
| **Range Gap-$2$ Distinct Subsequences** ($i_r - i_{r-1} \ge 2$) | Buffered state overwrites old $f_x$ without adding $f_x$ | **No** ($\det = 0$, singular) | **Divide-and-Conquer / Segment Tree** in **$O(\sigma^2 \log N)$** |
| **Adjacent-Distinct Output Subsequences** ($W[r] \ne W[r-1]$) | $f'_c = \sum_{a \ne c} f_a$ sets diagonal $(c, c)$ of $M_c$ to $0$ | **No** ($\det = 0$, singular) | **Segment Tree / Divide-and-Conquer** |

---

## 3. Tiskin's Seaweed Matrices (`海草矩阵` / Unit-Monge Braid Multiplication) & All-Pairs Interval LCS (`区间 LCS`)

### 3.1 Step 1: The Diagnostic Signal (Why $O(N^2)$ DP Cannot Answer All-Pairs Interval LCS)

Given $A[1..M]$ and $B[1..N]$ ($M, N \le 5000$ or $10^5$), the **All-Pairs Interval LCS** problem (`[THUPC 2021] 区间 LCS` / `Luogu P7456` / `LOJ 3399` / `[国家集训队论文 2021 — 单位蒙日矩阵]`) asks for:
$$\text{Query}(l, r) = \text{LCS}\bigl(A[1..M],\, B[l..r]\bigr) \qquad (1 \le l \le r \le N).$$
Running a standard $O(MN)$ LCS DP from each start position $l \in \{1, \dots, N\}$ takes $O(MN^2)$ time. Yet all $\binom{N+1}{2}$ interval LCS answers are completely determined by a **1D permutation array of length $N$** (**Tiskin's Seaweed Matrix**, `海草矩阵`), computable in **$O(MN)$ time** via a 3-line comb loop or in **$O((M+N)\log^2(M+N))$ time** via Unit-Monge distance multiplication!

---

### 3.2 Step 2: The Combinatorial Word Invariants (Planar Uncrossing, Unit-Monge Cross-Differences & Dual Seaweed Conventions)

#### Theorem 3.1 (Planar Alignment Uncrossing & The Unit Cross-Difference Permutation Matrix)
In the $(M+1) \times (N+1)$ alignment DAG of $A[1..M]$ and $B[1..N]$ (horizontal/vertical edges of weight $0$, diagonal match edges $(x-1, y-1) \to (x, y)$ of weight $1$ when $A[x] = B[y]$), let $L(l, r) = \text{LCS}(A[1..M], B[l+1..r])$ for $0 \le l \le r \le N$.
1. **Submodular / Anti-Monge Quadrangle Inequality**: For any $0 \le l < l' \le r < r' \le N$, any optimal path $(0, l) \leadsto (M, r')$ and any optimal path $(0, l') \leadsto (M, r)$ must cross at some grid vertex $(x^*, y^*)$; swapping their suffixes after $(x^*, y^*)$ proves:
   $$L(l, r) + L(l', r') \ge L(l, r') + L(l', r).$$
2. **Unit-Monge Cross-Difference**: For $1 \le i \le j \le N$, define the 2D cross-difference:
   $$\Delta(i, j) := \bigl(L(i-1, j) - L(i, j)\bigr) - \bigl(L(i-1, j-1) - L(i, j-1)\bigr).$$
   By the quadrangle inequality, $\Delta(i, j) \ge 0$. Moreover, summing across row $i$ telescopes to:
   $$\sum_{j=i}^{N} \Delta(i, j) = \bigl(L(i-1, N) - L(i, N)\bigr) - \bigl(L(i-1, i-1) - L(i, i-1)\bigr) = L(i-1, N) - L(i, N) \in \{0, 1\},$$
   and similarly summing down column $j$ gives $\sum_{i=1}^{j} \Delta(i, j) = L(0, j) - L(0, j-1) \in \{0, 1\}$.
   Since a sum of non-negative integers equals $0$ or $1$, **every $\Delta(i, j) \in \{0, 1\}$, and each row $i$ and column $j$ contains at most one $1$**!

#### Reconciling Cohort 1 (`Exit-to-Entrance` $W[k]$) and Cohort 2 (`Entrance-to-Exit` $p[i]$) Seaweed Conventions
To extend $\Delta(i, j)$ to a full $(M+N) \times (M+N)$ permutation matrix, trace $M+N$ **seaweeds (wires)** entering along the **left wall** ($M$ horizontal entrances at rows $x = 1, \dots, M$, assigned initial ranks $u_x = -x \in \{-M, \dots, -1\}$) and the **top wall** ($N$ vertical entrances at columns $y = 1, \dots, N$, assigned initial ranks $v_y = y \in \{1, \dots, N\}$).
Notice that walking clockwise along the top-left entrance perimeter from bottom-left $(M, 0)$ up to $(0, 0)$ and right to $(0, N)$ visits initial ranks in **strictly increasing order**:
$$-M < -(M-1) < \dots < -1 < 1 < 2 < \dots < N.$$
At each cell $(x, y)$ ($x = 1 \dots M, y = 1 \dots N$), a wire $u$ enters from the **left** edge and a wire $v = W[y]$ enters from the **top** edge:
- **Seaweed Comb Cell Rule**:
  $$\text{If } A[x] = B[y] \text{ OR } u > W[y]: \quad \text{wires DO NOT cross (bounce): } \texttt{swap}(u, W[y]).$$
  $$\text{If } A[x] \ne B[y] \text{ AND } u < W[y]: \quad \text{wires CROSS straight through: no swap!}$$
  *(Invariant: Since all wires start sorted along the entrance perimeter, $u > W[y]$ holds if and only if wires $u$ and $W[y]$ have **already crossed** at an earlier mismatch cell; thus no two seaweeds ever cross more than once—the 0-Hecke / sticky braid relation $s_i^2 = s_i$!)*

After sweeping all $M \times N$ cells:
- **Cohort 1 Convention (`Bottom-Exit Array` $W[1..N]$ & `Right-Exit Array` $R[1..M]$)**:
  - $W[k] \in \{-M, \dots, -1\} \cup \{1, \dots, N\}$ is the **initial entrance rank** of the wire exiting the **bottom wall at column $k \in \{1, \dots, N\}$**.
  - $R[x] \in \{-M, \dots, -1\} \cup \{1, \dots, N\}$ is the **initial entrance rank** of the wire exiting the **right wall at row $x \in \{1, \dots, M\}$**.
- **Cohort 2 Convention (`Top-Entrance Exit Map` $p[1..N]$)**:
  - $p[i] \in \{1, \dots, N\} \cup \{\infty\}$ is the **bottom exit column** where the wire that entered at **top column $i \in \{1, \dots, N\}$** exits (or $p[i] = \infty$ if it exited on the right wall).
- **Exact Duality Between the Two Conventions**:
  For any top wire $i \in [1, N]$ and bottom column $k \in [1, N]$:
  $$W[k] = i \iff p[i] = k!$$
  Since wires only move right and down, $W[k] \le k$ and $p[i] \ge i$. Among the $r - l + 1$ bottom exits in $[l, r]$, the wires with $W[k] \ge l$ are **precisely** the top entrances $i \in [l, r]$ that exited at $p[i] \le r$:
  $$\#\bigl\{\, k \in [l, r] \;\big|\; W[k] < l \,\bigr\} = (r - l + 1) - \#\bigl\{\, k \in [l, r] \;\big|\; W[k] \ge l \,\bigr\} = (r - l + 1) - \#\bigl\{\, i \in [l, r] \;\big|\; p[i] \le r \,\bigr\} = \#\bigl\{\, i \in [l, r] \;\big|\; p[i] > r \,\bigr\}!$$

#### Theorem 3.2 (Unified Three-Family LCS Dominance Formulas from $(W[1..N], R[1..M])$)
From a single $O(MN)$ Seaweed Comb on $A[1..M] \times B[1..N]$ producing $(W[1..N], R[1..M])$ (and $p[1..N]$), all three semi-local LCS families are given by 2D orthogonal range counts:
1. **Family 1 — Whole $A$ vs. Substring of $B$ (`区间 LCS`)**:
   $$\text{LCS}\bigl(A[1..M],\, B[l..r]\bigr) = \#\bigl\{\, k \in [l, r] \;\big|\; W[k] < l \,\bigr\} = \#\bigl\{\, i \in [l, r] \;\big|\; p[i] > r \,\bigr\}.$$
2. **Family 2 — Suffix of $A$ vs. Prefix of $B$ (`后缀-前缀 LCS`)**:
   $$\text{LCS}\bigl(A[i..M],\, B[1..j]\bigr) = \#\bigl\{\, k \in [1, j] \;\big|\; W[k] \le -i \,\bigr\}.$$
   *(Why: Wires entering at rows $i \dots M$ have initial ranks $\{-M, \dots, -i\}$, while all wires entering at rows $1 \dots i-1$ or top columns $1 \dots j$ have initial ranks $> -i$. Rows $1 \dots i-1$ only permute wires of rank $> -i$ among themselves before row $i$ is reached!)*
3. **Family 3 — Prefix of $A$ vs. Suffix of $B$ (`前缀-后缀 LCS`)**:
   $$\text{LCS}\bigl(A[1..i],\, B[l..N]\bigr) = \#\bigl\{\, x \in [1, i] \;\big|\; R[x] \ge l \,\bigr\} + \#\bigl\{\, k \in [l, N] \;\big|\; W[k] \in [-i, -1] \,\bigr\}.$$
   *(Or if row snapshots $W^{(i)}[1..N]$ are recorded after each row $i$, $\text{LCS}(A[1..i], B[l..r]) = \#\{k \in [l, r] \mid W^{(i)}[k] < l\}$ for **all** prefix-substring pairs $(i, l, r)$!)*

---

### 3.3 Step 3: Reverse-Engineering Scratchpad (8-Line Comb, Dynamic Appends, Exact $O(K \log K)$ Unit-Monge $\boxdot$ & Range LIS)

#### 1. The 8-Line $O(MN)$ Seaweed Comb Kernel (Simultaneously Recording $W[1..N]$, $R[1..M]$, and $p[1..N]$)
```cpp
vector<int> W(N + 1), R(M + 1), p(N + 1, N + 1);
for (int j = 1; j <= N; ++j) W[j] = j;
for (int i = 1; i <= M; ++i) {
    int u = -i; // Left-wall entrance wire for row i
    for (int j = 1; j <= N; ++j) {
        if (A[i] == B[j] || u > W[j]) {
            std::swap(u, W[j]);
        }
    }
    R[i] = u;   // Right-wall exit wire for row i
}
for (int k = 1; k <= N; ++k) {
    if (W[k] >= 1) p[W[k]] = k;
}
```

#### 2. Dynamic Character Appends to $A$ (`append_A`) and $B$ (`append_B`) in $O(N)$ / $O(M)$ Time
Because $(W[1..N], R[1..M])$ stores the complete bottom and right exit perimeter:
- **`append_A(c)` (add row $M+1$ at bottom)**: Initialize `u = -(M + 1)`, sweep $j = 1 \dots N$ (`if (c == B[j] || u > W[j]) swap(u, W[j]);`), and set `R[M + 1] = u` in **$O(N)$ time**.
- **`append_B(c)` (add column $N+1$ at right)**: Initialize `v = N + 1`, sweep $i = 1 \dots M$ (`if (A[i] == c || R[i] > v) swap(R[i], v);`), and set `W[N + 1] = v` in **$O(M)$ time**!
  Notice that during `append_B(c)`, none of the existing bottom exits $W[1..N]$ change at all—only the new entry $W[N+1]$ is appended and $R[1..M]$ is updated!

#### 3. Frontier Algorithm: Exact $O(K \log K)$ Unit-Monge Permutation Multiplication ($P = P_1 \boxdot P_2$) (`[国家集训队论文 2021]`)
When $M, N \le 10^5$, we cannot afford $O(MN)$. Instead, we compose horizontal strips of the grid using Tiskin's **Unit-Monge Distance Multiplication** $\boxdot$:
- Given two $K \times K$ permutation matrices $P_1, P_2$ (represented as 0-indexed permutations $P_1[0..K-1], P_2[0..K-1]$), define their implicit **Unit-Monge distribution matrices**:
  $$D_P(i, j) := \#\bigl\{\, x \in [i, K-1] \;\big|\; P[x] < j \,\bigr\} \qquad (0 \le i, j \le K).$$
  Note that $D_P$ has cross-differences $D_P(i, j+1) - D_P(i+1, j+1) - D_P(i, j) + D_P(i+1, j) = \mathbf{1}\bigl[P[i] = j\bigr]$.
- The Unit-Monge product $D_P = D_{P_1} \boxdot D_{P_2}$ is defined by:
  $$D_P(i, k) = \min_{0 \le j \le K} \bigl( D_{P_1}(i, j) + D_{P_2}(j, k) \bigr),$$
  and its cross-difference is a unique $K \times K$ permutation $P = P_1 \boxdot P_2$.
- **How the $O(K \log K)$ Divide-and-Conquer Merge Step Works (`The 2K-Step Monotone Staircase`)**:
  1. **Split at $M = \lfloor K / 2 \rfloor$**: Partition the middle index $j \in [0, K]$ into the left half $j \in [0, M]$ and the right half $j \in [M, K]$.
     - Filter $P_1$ into $P_{1, L}$ (rows $i$ with $P_1[i] < M$, compressed to $[0, M-1]$) and $P_{1, R}$ (rows $i$ with $P_1[i] \ge M$, compressed to $[0, K-M-1]$).
     - Filter $P_2$ into $P_{2, L}$ (first $M$ rows of $P_2$, column-compressed) and $P_{2, R}$ (last $K-M$ rows of $P_2$, column-compressed).
  2. **Recurse**: Compute $Q_L = P_{1, L} \boxdot P_{2, L}$ (size $M$) and $Q_R = P_{1, R} \boxdot P_{2, R}$ (size $K - M$) in $2 T(K/2)$ time, and map their row/column indices back to the original $[0, K-1]$ coordinates.
  3. **The $O(K)$ Staircase Merge Invariant**:
     For any $(i, k) \in [0, K] \times [0, K]$, let $F_L(i, k) = \min_{0 \le j \le M} (D_{P_1}(i, j) + D_{P_2}(j, k))$ and $F_R(i, k) = \min_{M \le j \le K} (D_{P_1}(i, j) + D_{P_2}(j, k))$.
     Define the **advantage function** $\delta(i, k) := F_R(i, k) - F_L(i, k)$.
     - Using the compressed results $Q_L$ and $Q_R$, advancing $i \to i+1$ or $k \to k+1$ changes $F_L(i, k)$ and $F_R(i, k)$ in **$O(1)$ time** (because $F_L(i, k) - F_L(i+1, k) = \mathbf{1}[Q_L(i) < k]$ and so on!).
     - By the Monge quadrangle inequality across $j \le M \le j'$, $\delta(i, k)$ is **monotonically non-decreasing in $i$** and **monotonically non-decreasing in $k$** (as $i$ increases from $0 \to K$, $F_L$ drops faster on left rows; as $k$ increases from $0 \to K$, $F_R$ drops faster on right columns).
     - Therefore, the region where $\delta(i, k) < 0$ ($F_R < F_L$) is separated from the region where $\delta(i, k) \ge 0$ ($F_L \le F_R$) by a **single monotone staircase path** from $(i, k) = (0, K)$ to $(K, 0)$ of at most $2K$ steps!
     - Walking $(i, k)$ from $(0, K)$ to $(K, 0)$ in $2K$ steps while maintaining $\delta(i, k)$ in $O(1)$ per step identifies every cell $(i, k)$ where the optimal $j$ switches from $Q_L$ to $Q_R$, assembling the merged permutation $P[0..K-1]$ in **$O(K)$ time**!

#### 4. Frontier Reduction: Range LIS (`区间最长上升子序列`) in $O(N \log^2 N)$ via Sparse Seaweed (`[国家集训队论文 2021]`)
Given a permutation $B[1..N]$ of $\{1, \dots, N\}$ and $Q$ queries $[l, r]$, how do we compute $\text{LIS}(B[l..r])$?
- Observe that a subsequence of $B[l..r]$ is strictly increasing if and only if it is a common subsequence of $A = (1, 2, \dots, N)$ and $B[l..r]$:
  $$\text{LIS}\bigl(B[l..r]\bigr) = \text{LCS}\bigl((1, 2, \dots, N),\, B[l..r]\bigr)!$$
- In the $N \times N$ alignment grid of $A = (1..N)$ and $B[1..N]$, **each row $x \in \{1, \dots, N\}$ has ONLY ONE matching cell**, namely at column $y = \text{pos}_B[x]$ where $B[y] = x$!
- Because the $N \times N$ grid contains only $N$ match cells in total, divide-and-conquer over the rows $x \in [1, N]$:
  - A subproblem of $K$ rows $x \in [L, R]$ only interacts with the $K$ columns of $B$ where values in $[L, R]$ appear (all other $N - K$ columns of $B$ have zero matches in rows $[L, R]$ and act as trivial mismatch pass-through wires!).
  - Compressing to those $K$ active columns and multiplying the top half $[L, M]$ and bottom half $[M+1, R]$ via $O(K \log K)$ Unit-Monge $\boxdot$ gives the recurrence $T(K) = 2 T(K/2) + O(K \log K) = O(K \log^2 K)$!
- Once the bottom-exit Seaweed permutation $W[1..N]$ is computed in **$O(N \log^2 N)$ time**, every Range LIS query $[l, r]$ is answered in **$O(\log N)$ time** via $\text{LIS}(B[l..r]) = \#\{k \in [l, r] \mid W[k] < l\}$!

---

## 4. Bit-Parallel LCS & Edit Distance (Allison–Dix / Hyyrö / Myers)

### 4.1 Step 1 & Step 2: Row-Difference Monotonicity & The Allison–Dix Hardware Borrow Identity

In the LCS DP table $dp[i][j] = \text{LCS}(A[1..i], B[1..j])$, adjacent horizontal entries satisfy:
$$D_i[j] := dp[i][j] - dp[i][j-1] \in \{0, 1\} \qquad (1 \le j \le N).$$
Let $1 \le j_1 < j_2 < \dots < j_k \le N$ be the columns where $D_{i-1}[j] = 1$, partitioning $[1, N]$ into intervals $I_r = [j_{r-1}+1, j_r]$ ($j_0 = 0$) plus tail $I_{k+1} = [j_k+1, N]$.
When transitioning to row $i$ on character $c = A[i]$, within each interval $I_r = [j_{r-1}+1, j_r]$, the step-up bit moves left from $j_r$ to the **earliest match** of $c$ inside $I_r$:
$$j'_r = \min\Bigl(\bigl\{\, p \in [j_{r-1}+1, j_r] \;\big|\; B[p] = A[i] \,\bigr\} \cup \{j_r\}\Bigr).$$

#### Theorem 4.1 (Allison–Dix 1986 / Crochemore–Hyyrö 4-Operation Bitwise Step)
Pack $D_{i-1}[1..N]$ into an $N$-bit integer $V$, and let $M[c]$ be the $N$-bit pattern mask where bit $j-1$ is $1 \iff B[j] = c$. Define:
$$X = V \mathbin{|} M\bigl[A[i]\bigr], \qquad Y = (V \ll 1) \mathbin{|} 1.$$
Then the new row-difference bitmask $V'$ for row $i$ is given by:
$$\boxed{V' = X \mathbin{\&} \sim(X - Y).}$$

*Proof (Interval-Local Borrow Absorption).*
Inside each interval $I_r = [j_{r-1}+1, j_r]$:
1. $Y = (V \ll 1) \mathbin{|} 1$ has a **single $1$-bit at the bottom (LSB) of $I_r$** (at $j_{r-1}+1$) and $0$s everywhere else in $I_r$.
2. $X = V \mathbin{|} M[A[i]]$ has $1$-bits at all match positions in $I_r$ **and** a guaranteed $1$-bit at the top (MSB) of $I_r$ (at $j_r$, since $V \subseteq X$).
3. Therefore, subtracting $Y$ from $X$ generates a borrow starting at $j_{r-1}+1$ that propagates up through the trailing $0$s of $X|_{I_r}$ until it hits the **lowest-indexed $1$-bit $j'_r \in I_r$ of $X$**, flipping bit $j'_r$ from $1 \to 0$, flipping bits $[j_{r-1}+1 .. j'_r - 1]$ from $0 \to 1$, and leaving all bits in $[j'_r + 1 .. j_r]$ **unchanged** (so **no borrow ever crosses $j_r$ into $I_{r+1}$**!).
4. Consequently, inside $I_r$, bit $j'_r$ is the **unique** position where $X$ has $1$ and $X - Y$ has $0$, which is isolated by $X \mathbin{\&} \sim(X - Y)$. $\blacksquare$

---

### 4.2 Step 3 & Step 4: Myers' Bit-Parallel Edit Distance, Hirschberg Space-Optimal Reconstruction & `DP套DP` Coupling

1. **Myers' $O(MN / w)$ Bit-Parallel Levenshtein Edit Distance (Myers 1999)**:
   - Adjacent column/row differences in unit-cost edit distance lie in $\{-1, 0, +1\}$, encoded by bitvector pairs $(VP, VN)$ (vertical $+1$ and $-1$) and $(HP, HN)$ (horizontal $+1$ and $-1$):
     $$X = M_A[B[j]] \mathbin{|} VN, \qquad D0 = \bigl(((X \mathbin{\&} VP) + VP) \oplus VP\bigr) \mathbin{|} X,$$
     $$HP = VN \mathbin{|} \sim(D0 \mathbin{|} VP), \qquad HN = VP \mathbin{\&} D0,$$
     $$X' = (HP \ll 1) \mathbin{|} b_0, \qquad VP' = (HN \ll 1) \mathbin{|} \sim(D0 \mathbin{|} X'), \qquad VN' = X' \mathbin{\&} D0,$$
     where **$b_0 = 1$ for global edit distance** ($dp[0][j] = j \implies \Delta H_{0, j} = +1$) and **$b_0 = 0$ for semi-local substring edit distance** ($dp[0][j] = 0 \implies \Delta H_{0, j} = 0$).
2. **Bit-Parallel LCS + Hirschberg $O(MN / w)$-Time, $O(M+N)$-Space Alignment Reconstruction**:
   - Storing all $M$ bitvectors $V_1, \dots, V_M$ takes $O(MN/8)$ bytes ($> 300\text{ MB}$ at $M, N = 50{,}000$). Running Allison–Dix bit-parallel LCS forward on $A[1..M/2]$ and backward on $A[M/2+1..M]^R$ to find the midpoint split $j^* = \arg\max_j (\text{fwd}[j] + \text{bwd}[N-j])$ reconstructs the actual LCS string in $\sum_{d \ge 0} O(MN / (2^d w)) = O(MN/w)$ time and $O(M+N)$ memory!
   - **Critical Pitfall**: Inside recursive calls on $(A[l_A..r_A], B[l_B..r_B])$, only build/slice pattern masks $M[c]$ for the active width $r_B - l_B + 1$ and active alphabet of $A[l_A..r_A]$, never over the full $1..N$.
3. **Instant `DP套DP` Automaton Precomputation (`trans[D][c]`)**:
   - In LCS `DP套DP` problems (`Wave 4A`, $|A| \le 20$), Theorem 4.1 computes the next mask `trans[D][c]` from mask `D` in 4 bitwise instructions without unpacking `D` into an array of length $|A|$.

---

## 5. Master Quarantine Ledger of Pure-Template Problems (`R-4B-01` – `R-4B-10`)

Per `PLAN.md` §2.2 and `AGENTS.md`, pure template verification problems across Cohort 1 and Cohort 2 are consolidated and quarantined here:

| Quarantine ID | Source & Problem Name | Judge / Language | Reason for Quarantine |
| :--- | :--- | :--- | :--- |
| **`R-4B-01`** | **Luogu P5826 — 【模板】子序列自动机** | `[ZH]` Luogu | Bare template verification of $\text{DASG}(S)$ next-occurrence lookups via occurrence vectors + `upper_bound`. |
| **`R-4B-02`** | **Library Checker — Longest Common Subsequence** | `[EN]` / `[JA]` Yosupo | Pure template verification of standard LCS without structural twists. |
| **`R-4B-03`** | **Library Checker — Prefix-Substring LCS** | `[EN]` / `[JA]` Yosupo | Pure template verification of Tiskin's Seaweed comb construction and 2D dominance counting. |
| **`R-4B-04`** | **LeetCode 940 — Distinct Subsequences II** | `[EN]` LeetCode | Bare $O(N)$ whole-string distinct subsequence recurrence $D' = 2D - L_x$ without range queries or matrix inversion. |
| **`R-4B-05`** | **LeetCode 792 — Number of Matching Subsequences** | `[EN]` LeetCode | Direct bucket-waiting / bare DASG traversal without structural synthesis. |
| **`R-4B-06`** | **SPOJ LCS0 — Longest Common Subsequence ($N \le 50000$)** | `[EN]` SPOJ | Pure bare template of Allison–Dix $O(N^2/w)$ bit-parallel LCS with zero additional modelling. |
| **`R-4B-07`** | **LOJ 6564 — 最长公共子序列 ($N = 70000$)** | `[ZH]` LibreOJ | Bare $O(N^2/w)$ bit-parallel LCS engineering benchmark. |
| **`R-4B-08`** | **AtCoder Educational DP Contest F — LCS** | `[JA]` AtCoder | Introductory $O(NM)$ textbook LCS reconstruction exercise. |
| **`R-4B-09`** | **CSES 1143 / LeetCode 1143 — Longest Common Subsequence** | `[EN]` CSES / LC | Bare textbook Needleman–Wunsch DP exercise. |
| **`R-4B-10`** | **CSES 1639 — Edit Distance** | `[EN]` CSES | Introductory $O(NM)$ Wagner–Fischer edit distance template. |

---

## 6. Master Reconciled Non-Template Problem Archive (`W4B-01` – `W4B-42`, 4-Tier Smooth Difficulty Ladder)

This section synthesizes the complete union of accepted non-template problems from Cohort 1 (`P-4B-01..32`) and Cohort 2 (`1..32`), deduplicated and enriched with Cohort 3 frontier additions into **42 problems (`W4B-01` – `W4B-42`)**, each with a self-contained mathematical statement, constraints, and **4-Step Zero-Magic Analysis**.

---

### Tier 1: Stepping Stone (`W4B-01` – `W4B-10` — Canonical DASG Greedies, Gap Constraints, Arch Factorization & Product DAGs)

#### `W4B-01`: AtCoder ABC 214 F — Substrings (`[JA]`, AtCoder)
- **Statement & Constraints**: Given $S[1..N] \in \{\texttt{'a'}..\texttt{'z'}\}^N$ ($1 \le N \le 2 \cdot 10^5$), count distinct non-empty strings formed by choosing indices $1 \le i_1 < i_2 < \dots < i_k \le N$ with $i_r - i_{r-1} \ge 2$ for all $r$, modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Non-adjacent index selection shifts the subsequence transition from $j \ge i+1$ to $j \ge i+2$.
  2. *Combinatorial Invariant*: By leftmost-greedy canonicalization under gap $2$, every valid output string corresponds bijectively to a path in $\text{DASG}_{\text{gap}=2}(S)$ where root $0$ jumps to $\text{nxt}[0][c]$ and state $i \ge 1$ jumps to $\text{nxt}[i+1][c]$.
  3. *Reverse-Engineering Scratchpad*: Pulling backwards, index $i$ extends any canonical prefix ending at $j \le i-2$ for which $S[i]$ did not appear in $S[j+2..i-1]$, yielding $dp[i] = \sum_{j = \max(0, \text{prev}[i]-1)}^{i-2} dp[j]$ in $O(N)$ time.
  4. *Boundary Pitfall*: Root state $0$ can jump to both $i_1 = 1$ and $i_1 = 2$; only transitions from $i \ge 1$ enforce $j \ge i+2$.

#### `W4B-02`: AtCoder ARC 081 E (ABC 081 / ARC 081 C) — Don't Be a Subsequence (`[JA]`, AtCoder)
- **Statement & Constraints**: Given $A[1..N] \in \{\texttt{'a'}..\texttt{'z'}\}^N$ ($1 \le N \le 2 \cdot 10^5$), find the shortest (and among shortest, lexicographically smallest) string $P \in \Sigma^+$ that is **not** a subsequence of $A$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Finding a shortest absent subsequence is a shortest-path problem from root $0$ to the dead sink $\infty$ in $\text{DASG}(A)$.
  2. *Combinatorial Invariant*: By Theorem 1.1 & 1.3, $d[i] = 1 + \min_{c \in \Sigma} d[\text{nxt}[i][c]]$ with $d[\infty] = 0$.
  3. *Reverse-Engineering Scratchpad*: Compute $d[i]$ for $i = N \downarrow 0$ in $O(N|\Sigma|)$, then reconstruct from $u = 0$ by picking the smallest $c$ with $d[\text{nxt}[u][c]] = d[u] - 1$.
  4. *Boundary Pitfall*: Forward greedy ($\arg\max_c \text{nxt}[u][c]$) finds the minimum length $\iota(A)+1$ but fails lexicographical tie-breaking when an earlier index in the same arch also has distance $d[u]-1$.

#### `W4B-03`: Codeforces 1924A / 1925C — Did We Get Everything Covered? (`[EN]`, Codeforces)
- **Statement & Constraints**: Given $N, K \le 26$ and $S[1..M]$ ($M \le 1000$) over the first $K$ letters, decide if all $K^N$ strings of length $N$ are subsequences of $S$, and if not, output a missing string of length $N$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Testing whether $\iota(S) \ge N$ over alphabet size $K$.
  2. *Combinatorial Invariant*: By Theorem 1.3 (Hébrard's Arch Factorization), $\iota(S) \ge N$ iff $S$ partitions into $\ge N$ disjoint $1$-universal arches $A_1 \dots A_N$.
  3. *Reverse-Engineering Scratchpad*: Sweep $S$ greedily collecting distinct characters until count $= K$; record each arch's last character $m_r = S[r_r]$ and clear the set. If $k < N$ arches form, append any character $m_{k+1} \notin \text{alph}(R)$ and pad to length $N$ in $O(M)$ time.
  4. *Boundary Pitfall*: The character $m_{k+1} \notin \text{alph}(R)$ **must** be placed immediately after $m_1 \dots m_k$ before any arbitrary padding characters.

#### `W4B-04`: Codeforces 1295C — Obtain The String & Cyclic DASG Wraps (`[EN]`, Codeforces)
- **Statement & Constraints**: Given $S[1..N]$ and $T[1..M]$ ($N, M \le 10^5$), find the minimum number of subsequences of $S$ whose concatenation equals $T$ (or `-1`).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Partitioning $T$ into minimum subsequences of $S$ is greedy traversal on $\text{DASG}(S)$ wrapping to $0$ on missing transitions.
  2. *Combinatorial Invariant*: By Theorem 1.1, consuming the longest prefix of $T$ in each pass through $S$ strictly dominates stopping early.
  3. *Reverse-Engineering Scratchpad*: Build $\text{DASG}(S)$ in $O(N|\Sigma|)$; walk $T$ in $O(M)$, wrapping $u \leftarrow \text{nxt}[0][T[j]]$ whenever $\text{nxt}[u][T[j]] = \infty$.
  4. *Boundary Pitfall*: Check $\text{nxt}[0][T[j]] = \infty$ first to detect characters absent from $S$ (`-1`).

#### `W4B-05`: Codeforces 1303E — Erase Subsequences (`[EN]`, Codeforces)
- **Statement & Constraints**: Given $S[1..N]$ and $T[1..M]$ ($N, M \le 400$), determine if $T$ can be split into $T = T_1 \cdot T_2$ such that $S$ contains $T_1$ and $T_2$ as two **disjoint** subsequences? Wait: in `CF 1303E`, we check if $T$ can be formed by concatenating two subsequences of $S$ that use disjoint indices of $S$ (equivalently, $T_1$ and $T_2$ are interleaved inside $S$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Naive 3D DP over $(k_{\text{split}}, i \in S, j_1 \in T_1, j_2 \in T_2)$ takes $O(M^3 N)$.
  2. *Combinatorial Invariant*: Fix the split $T = T_1 \cdot T_2$. For prefixes $T_1[1..a]$ and $T_2[1..b]$, the optimal embedding in $S$ minimizes the ending index $dp[a][b] \in \{0, \dots, N, \infty\}$ in $\text{DASG}(S)$.
  3. *Reverse-Engineering Scratchpad*: Transition $dp[a][b] = \min\bigl(\text{nxt}_S[dp[a-1][b]][T_1[a]],\, \text{nxt}_S[dp[a][b-1]][T_2[b]]\bigr)$ in $O(1)$, giving $O(M^3 + N|\Sigma|)$ total time.
  4. *Boundary Pitfall*: Set $\text{nxt}_S[\infty][c] = \infty$ so unreachable states never jump back into $S$.

#### `W4B-06`: Codeforces 1183H — Subsequences (Hard Version) (`[EN]`, Codeforces)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 100$) and $K \le 10^{12}$, choose $K$ distinct subsequences of $S$ minimizing total deletions $\sum (N - |P|)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Count distinct subsequences of $S$ stratified by length $L \in \{0, \dots, N\}$, clamped at $K$.
  2. *Combinatorial Invariant*: Paths of length $L$ from $0$ in $\text{DASG}(S)$ bijectively match distinct subsequences of length $L$.
  3. *Reverse-Engineering Scratchpad*: Compute $dp[u][L] = \min\bigl(K, \sum_{c \in \Sigma} dp[\text{nxt}[u][c]][L-1]\bigr)$ in $O(N^2|\Sigma|)$, then greedily take $\min(K, dp[0][L])$ for $L = N \downarrow 0$.
  4. *Boundary Pitfall*: Never use the subtractive recurrence $2dp[i-1] - dp[\text{prev}[i]-1]$ when clamping at $K$; use purely additive DASG out-edge summation.

#### `W4B-07`: AtCoder ABC 130 E vs. Product DASG — Multiplicity vs. Distinct Common Subsequences (`[JA]` / `[EN]`)
- **Statement & Constraints**: Given $A[1..M], B[1..N]$ ($M, N \le 2000$), contrast counting equal subsequence index-pair embeddings (`ABC 130 E`) vs. counting **distinct common subsequence strings** on $\text{DASG}(A) \times \text{DASG}(B)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Multiplicity counts index subsets $(I, J)$; distinctness counts unique strings $P \preceq A, B$.
  2. *Combinatorial Invariant*: Unique strings $P \preceq A, B$ correspond bijectively to paths from $(0, 0)$ in $\text{DASG}(A) \times \text{DASG}(B)$.
  3. *Reverse-Engineering Scratchpad*: Use the 2D predecessor rectangle optimization (`§1.3.4`): each matching pair $(i', j')$ with $A[i'] = B[j']$ adds $dp[i'][j']$ to $[\text{prev}_A[i'], i'-1] \times [\text{prev}_B[j'], j'-1]$ in $O(MN)$ time.
  4. *Boundary Pitfall*: Do not conflate 2D prefix-sum inclusion-exclusion ($- dp[i-1][j-1]$) with string deduplication ($\text{prev}_A[i']$).

#### `W4B-08`: Luogu P3856 — [TJOI2008] 公共子串 (Distinct Common Subsequences of 3 Strings) (`[ZH]`, TJOI)
- **Statement & Constraints**: Given $A, B, C$ ($|A|, |B|, |C| \le 150$), count distinct non-empty common subsequences of all three strings.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: 3-way distinct common subsequence counting.
  2. *Combinatorial Invariant*: Bijection with directed paths from $(0, 0, 0)$ in $\text{DASG}(A) \times \text{DASG}(B) \times \text{DASG}(C)$.
  3. *Reverse-Engineering Scratchpad*: Memoized DAG DP over reachable triples $(\text{nxt}_A[i][c], \text{nxt}_B[j][c], \text{nxt}_C[k][c])$ in $O(|A||B||C||\Sigma|)$.
  4. *Boundary Pitfall*: Requires arbitrary-precision arithmetic if un-modded ($2^{150}$).

#### `W4B-09`: AtCoder ABC 299 E / ARC 125 C — Lexicographically Extremal Subsequence Reconstruction (`[JA]`, AtCoder)
- **Statement & Constraints**: Given $S[1..N]$ and length/frequency constraints, reconstruct the lexicographically smallest valid subsequence of length $K$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Lexicographical greedy step-by-step walk on $\text{DASG}(S)$.
  2. *Combinatorial Invariant*: From state $u$, choosing character $c$ jumps to $v = \text{nxt}[u][c]$ and is valid iff $S[v+1..N]$ has enough remaining characters per symbol to satisfy all lower/upper bounds.
  3. *Reverse-Engineering Scratchpad*: Precompute suffix character counts and $\text{nxt}[u][c]$ in $O(N|\Sigma|)$; test $c = \texttt{'a'}..\texttt{'z'}$ greedily at each step in $O(K|\Sigma|)$.
  4. *Boundary Pitfall*: Must verify both individual lower bounds $\text{rem}[v+1][a] \ge L'_a$ and total capped capacity $\sum_a \min(R'_a, \text{rem}[v+1][a]) \ge K - 1$.

#### `W4B-10`: AtCoder ABC 138 E / Codeforces 91A — Cyclic DASG & Binary Lifting on $S^\infty$ (`[JA]` / `[EN]`)
- **Statement & Constraints**: Given $S[1..N]$ and $T[1..M]$ (or compressed $T$ of length $\le 10^{18}$), find the minimum prefix of $S^\infty$ containing $T$ as a subsequence.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Matching against an infinite periodic repetition $S^\infty$.
  2. *Combinatorial Invariant*: In $\text{DASG}(S \cdot S)$, advancing one character from index $i \in [0, N-1]$ lands at $\text{nxt}[i][c] \in [i+1, i+N]$, advancing total length by $\text{nxt}[i][c] - i$ and moving to state $\text{nxt}[i][c] \bmod N$.
  3. *Reverse-Engineering Scratchpad*: Build $\text{DASG}(S \cdot S)$ in $O(N|\Sigma|)$; for repeated blocks of $T$, binary lift the state-transition function $f : \{0..N-1\} \to \{0..N-1\}$ in $O(N \log K)$.
  4. *Boundary Pitfall*: Doubling $S$ to $S \cdot S$ avoids wrap-around branch logic inside `nxt`.

---

### Tier 2: Intermediate (`W4B-11` – `W4B-21` — Four-Comb Product Automata, Dynamic DASG Slices, Bracket/Palindrome DASGs & Tropical Matrices)

#### `W4B-11`: Luogu P4112 / BZOJ 4032 — [HEOI2015] 最短不公共子串 (The Four-Comb Product Automaton Classic) (`[ZH]`, HEOI)
- **Statement & Constraints**: Given $A, B \in \{\texttt{'a'}..\texttt{'z'}\}^*$ ($|A|, |B| \le 2000$), output the minimum length of a non-empty string $W$ that is: (1) Substring of $A$, not Substring of $B$; (2) Substring of $A$, not Subsequence of $B$; (3) Subsequence of $A$, not Substring of $B$; (4) Subsequence of $A$, not Subsequence of $B$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Four combinations of contiguous factor ($\text{SAM}$) vs. scattered subsequence ($\text{DASG}$).
  2. *Combinatorial Invariant*: $L(\mathcal{A}^+(A)) \setminus L(\mathcal{A}^-(B))$ is recognized by the product DFA $\mathcal{A}^+(A) \times \mathcal{A}^-(B)$ where $\mathcal{A} \in \{\text{SAM}, \text{DASG}\}$.
  3. *Reverse-Engineering Scratchpad*: Build $\text{SAM}(A), \text{SAM}(B), \text{DASG}(A), \text{DASG}(B)$. Run BFS on $(u, v) \in \mathcal{A}^+(A) \times \mathcal{A}^-(B)$; the first transition $(u, v) \xrightarrow{c} (\delta^+(u, c) \ne \bot,\, \delta^-(v, c) = \bot)$ at depth $d$ gives $d + 1$ in $O(|A||B||\Sigma|)$ (with Q1 also solvable in $O(|A|+|B|)$ via `lcs_len` on $\text{SAM}(B)$).
  4. *Boundary Pitfall*: Never follow `link[v]` in $\text{SAM}(B)$ when $\delta^-(v, c) = \bot$, and normalize root/dead-state indices between 0-indexed DASG and 1-indexed SAM.

#### `W4B-12`: Codeforces 1149B — Three Religions (`[EN]`, Codeforces Div. 1)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$) and three initially empty strings $W_1, W_2, W_3$ modified by $Q \le 1000$ append/pop operations (with $|W_r| \le 250$ always), determine after each operation whether $S$ contains $W_1, W_2, W_3$ as three **pairwise disjoint** subsequences.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Dynamic append/pop on 3 pattern strings against a static text $S$ of length $10^5$.
  2. *Combinatorial Invariant*: On $\text{DASG}(S)$, let $dp[i][j][k] \in \{0, \dots, N, \infty\}$ be the minimum prefix of $S$ containing $W_1[1..i], W_2[1..j], W_3[1..k]$ disjointly:
     $$dp[i][j][k] = \min_{r \in \{1, 2, 3\}} \text{nxt}_S\bigl[dp[\dots]\bigr]\bigl[W_r[\text{last}]\bigr].$$
  3. *Reverse-Engineering Scratchpad*: Appending to $W_1$ only computes the single 2D slice $i = |W_1|$ of size $|W_2| \times |W_3| \le 250^2$ in $O(L^2)$ time; popping decrements $|W_1|$ in $O(1)$! Total time: $O(N|\Sigma| + Q L^2)$.
  4. *Boundary Pitfall*: Ensure $\text{nxt}_S[\infty][c] = \infty$ for all $c \in \Sigma$.

#### `W4B-13`: Codeforces 750E — New Year and Old Subsequence (`[EN]`, Codeforces Goodbye 2016)
- **Statement & Constraints**: Given digit string $S[1..N]$ ($N, Q \le 2 \cdot 10^5$) and queries $[l, r]$, find the minimum deletions in $S[l..r]$ so that $\texttt{"2017"}$ is a subsequence and $\texttt{"2016"}$ is **not** a subsequence (or `-1`).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Range optimization of subsequence containment/avoidance $\implies$ tropical $(\min, +)$ DFA matrix on a Segment Tree.
  2. *Combinatorial Invariant*: Track the 5 prefix states $\{0 (\varepsilon), 1 (\texttt{"2"}), 2 (\texttt{"20"}), 3 (\texttt{"201"}), 4 (\texttt{"2017"})\}$, where digit $S[i]$ defines an upper-triangular $5 \times 5$ $(\min, +)$ matrix $T_{S[i]}$.
  3. *Reverse-Engineering Scratchpad*: Build a Segment Tree of $5 \times 5$ matrices in $O(5^3 N)$; answer $[l, r]$ by multiplying the $1 \times 5$ row vector $(0, \infty, \infty, \infty, \infty)$ across $O(\log N)$ nodes in $O(5^2 \log N)$ time.
  4. *Boundary Pitfall*: At **both** state $3$ ($\texttt{"201"}$) and state $4$ ($\texttt{"2017"}$), reading $\texttt{'6'}$ must pay cost $+1$ to delete $\texttt{'6'}$ ($T_{\texttt{'6'}}[3][3] = T_{\texttt{'6'}}[4][4] = 1$).

#### `W4B-14`: Codeforces 1609E — William The Oblivious (`[EN]`, Codeforces)
- **Statement & Constraints**: Given $S[1..N] \in \{\texttt{'a'}, \texttt{'b'}, \texttt{'c'}\}^N$ ($N, Q \le 10^5$) with single-character point updates, maintain the minimum character replacements to eliminate $\texttt{"abc"}$ as a subsequence.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Dynamic point updates + subsequence avoidance of $\texttt{"abc"}$.
  2. *Combinatorial Invariant*: $3 \times 3$ $(\min, +)$ tropical matrix over states $\{\varepsilon, \texttt{"a"}, \texttt{"ab"}\}$; equivalently $\min_{0 \le i \le j \le N} (\text{cnt}_{\texttt{a}}[1..i] + \text{cnt}_{\texttt{b}}[i+1..j] + \text{cnt}_{\texttt{c}}[j+1..N])$.
  3. *Reverse-Engineering Scratchpad*: Segment Tree of $3 \times 3$ tropical matrices in $O(3^3 \log N)$ per update.
  4. *Boundary Pitfall*: Tropical matrices have no inverse; always use a Segment Tree.

#### `W4B-15`: Codeforces 1426F / 1666F — Fixed-Pattern Subsequence Multiplicity with Wildcards on Ranges (`[EN]`, Codeforces)
- **Statement & Constraints**: Given $S[1..N] \in \{\texttt{'a'}, \texttt{'b'}, \texttt{'c'}, \texttt{'?'}\}^N$ ($N, Q \le 2 \cdot 10^5$), for each range query $[l, r]$ compute the sum of occurrences of subsequence $\texttt{"abc"}$ over all $3^{\text{cnt}_{\texttt{?}}}$ assignments to `'?'` in $S[l..r]$ modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Fixed-pattern counting over the commutative ring $\mathbb{F}_p$ where transition matrices are upper-triangular with nonzero diagonal!
  2. *Combinatorial Invariant*: For $c \in \{\texttt{'a'}, \texttt{'b'}, \texttt{'c'}\}$, $A_c$ is $4 \times 4$ upper-unitriangular ($\det(A_c) = 1$). For `'?'`, $A_{\texttt{?}} = A_{\texttt{a}} + A_{\texttt{b}} + A_{\texttt{c}} = 3I_4 + E_{0,1} + E_{1,2} + E_{2,3}$ has $\det(A_{\texttt{?}}) = 3^4 \not\equiv 0 \pmod{10^9+7}$, so $A_{\texttt{?}}$ is invertible!
  3. *Reverse-Engineering Scratchpad*: Precompute prefix $4 \times 4$ matrices $P_i = P_{i-1} A_{S[i]}$ and $Q_i = A_{S[i]}^{-1} Q_{i-1}$ in $O(N)$, answering each $[l, r]$ in **$O(1)$ time** via $(Q_{l-1} P_r)_{0, 3}$.
  4. *Boundary Pitfall*: Inverting $A_{\texttt{?}} = 3(I + \frac{1}{3}N)$ uses the nilpotent expansion $A_{\texttt{?}}^{-1} = 3^{-1}(I - 3^{-1}N + 3^{-2}N^2 - 3^{-3}N^3)$.

#### `W4B-16`: Codeforces 1366G — Construct the String (Subsequence Matching with Backspaces) (`[EN]`, Codeforces)
- **Statement & Constraints**: Given $S[1..N]$ (letters and backspace `'.'`) and target $T[1..M]$ ($N, M \le 10^4$), find the minimum deletions from $S$ so that evaluating the remaining string produces $T$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Characters in $S$ can either match $T[j]$ at cost $0$, be deleted at cost $1$, or be cancelled at cost $0$ by a later backspace `'.'`!
  2. *Combinatorial Invariant*: Each letter $S[i] \ne \texttt{'.'}$ has at most one minimal balanced interval $[i, r_i]$ where $S[i..r_i]$ reduces to $\varepsilon$ via backspaces.
  3. *Reverse-Engineering Scratchpad*: Precompute $r_i$ in $O(N^2)$ or $O(N)$; run 2D DP on $(i, j)$ with the cost-$0$ jump $(i, j) \to (r_i + 1, j)$ in $O(NM)$ time.
  4. *Boundary Pitfall*: Do not allow unmatched letters to be skipped at cost $0$ without pairing them with a balanced backspace interval $[i, r_i]$.

#### `W4B-17`: Luogu P4607 / SDOI / JOI — Distinct Palindromic Subsequences on Bidirectional DASG (`[ZH]` / `[JA]`)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3000$), count the number of **distinct** palindromic subsequences of $S$ modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Deduplicating palindromic subsequences $P = W \cdot \text{mid} \cdot W^R$.
  2. *Combinatorial Invariant*: Every distinct palindromic subsequence has a unique **outermost canonical embedding** where the left half $W$ uses the earliest indices ($\text{nxt}[l][c]$ in $\text{DASG}(S)$) and the right half $W^R$ uses the latest indices ($\text{prv}[r][c]$ in $\text{DASG}(S^R)$), valid iff $\text{nxt}[l][c] \le \text{prv}[r][c]$.
  3. *Reverse-Engineering Scratchpad*: 2D DP on interval $(l, r)$ with $S[l] = S[r]$: transition to $(\text{nxt}[l][c], \text{prv}[r][c])$, adding $+2$ when $\text{nxt}[l][c] < \text{prv}[r][c]$ ($WcW^R$ and $WccW^R$) and $+1$ when $\text{nxt}[l][c] = \text{prv}[r][c]$ ($WcW^R$). Optimize to $O(N^2)$ via 2D prefix sums.
  4. *Boundary Pitfall*: Separate strict inequality `<` ($+2$) from equality `=` ($+1$).

#### `W4B-18`: UOJ / LOJ Regional Classic — Bracket-Balanced Distinct Subsequences (`括号序列子序列计数`) (`[ZH]`, UOJ / LOJ)
- **Statement & Constraints**: Given $S[1..N] \in \{\texttt{'('}, \texttt{')'}\}^N$ ($N \le 500$), count distinct non-empty regular bracket sequences (RBS) that occur as subsequences of $S$ modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Intersection of $\text{Subseq}(S)$ with the Dyck language of balanced parentheses.
  2. *Combinatorial Invariant*: Bijection between distinct RBS subsequences of $S$ and paths from $(0, 0)$ to $(i, 0)$ in $\text{DASG}(S) \times \{0, \dots, N/2\}$ (tracking prefix balance $\text{bal} \ge 0$).
  3. *Reverse-Engineering Scratchpad*: From $(i, \text{bal})$, transition to $(\text{nxt}[i][\texttt{'('}], \text{bal}+1)$ and (if $\text{bal} > 0$) to $(\text{nxt}[i][\texttt{')'}], \text{bal}-1)$ in $O(N^2)$ time.
  4. *Boundary Pitfall*: Subtract $1$ for $\varepsilon$ if only non-empty RBS are requested.

#### `W4B-19`: AtCoder AGC 024 E — Sequence Growing Hard (`[JA]`, AtCoder Grand Contest)
- **Statement & Constraints**: Count sequences of strings $A_0 = \varepsilon, A_1, \dots, A_N$ over $\{1, \dots, K\}$ ($N, K \le 300$) where $A_i$ is formed by inserting one character into $A_{i-1}$ and $A_{i-1} <_{\text{lex}} A_i$, modulo $M$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Inserting $c$ anywhere inside an existing contiguous run of $c$'s produces the **same** string $A_i$.
  2. *Combinatorial Invariant*: Canonicalize every insertion by requiring $c$ to be inserted **immediately before a character $x < c$** (or at the very end if $x = 0$), which turns $A_{i-1} <_{\text{lex}} A_i$ into a bijection with labeled increasing rooted trees of size $N+1$!
  3. *Reverse-Engineering Scratchpad*: Tree DP over subtree size $s \in [1, N+1]$ and root label bound $k \in [1, K]$ in $O(N^2 K)$ time.
  4. *Boundary Pitfall*: Failing to canonicalize insertions within equal-character runs overcounts identical string sequences.

#### `W4B-20`: Codeforces 914F / AtCoder ABC 248 G — Dynamic Bitset Pattern & Subsequence Matching (`[EN]` / `[JA]`)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), support point character updates $S[i] \leftarrow c$ and substring/LCS range queries $P$ on $S[l..r]$ ($\sum |P| \le 10^5$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Online point updates + $\sum |P| \le 10^5$ fits $O(N \sum |P| / 64)$ bit-parallel operations in $< 0.2\text{s}$.
  2. *Combinatorial Invariant*: Maintain 26 bitsets `M[26]` of length $N$; point updates flip 2 bits in $O(1)$.
  3. *Reverse-Engineering Scratchpad*: Shift-and-AND `M[P[k]] >> (k-1)` for substring queries, or run Allison–Dix bit-parallel LCS on the sliced bitmask window $[l, r]$.
  4. *Boundary Pitfall*: Guard against $|P| > r - l + 1$ before computing window masks.

#### `W4B-21`: Luogu P4094 / BZOJ — Large-Alphabet DASG via Persistent Segment Tree (`[ZH]`, Luogu / BZOJ)
- **Statement & Constraints**: Given integer array $S[1..N]$ ($N, |\Sigma| \le 10^5$), build $\text{DASG}(S)$ to answer subsequence and SAS queries over large alphabet $\Sigma = \{1, \dots, 10^5\}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $N \times |\Sigma| = 10^{10}$ rules out a flat 2D transition table.
  2. *Combinatorial Invariant*: Row $\text{nxt}[i][\cdot]$ differs from $\text{nxt}[i+1][\cdot]$ in only one entry $c = S[i+1]$.
  3. *Reverse-Engineering Scratchpad*: Build persistent segment tree roots `rt[N] .. rt[0]` in $O(N \log |\Sigma|)$ time and space.
  4. *Boundary Pitfall*: Initialize `rt[N]` with $\infty$ ($d[\infty] = 0$) across all $|\Sigma|$ leaves so unseen characters are detected in $O(1)$ at the root.

---

### Tier 3: Advanced (`W4B-22` – `W4B-32` — Invertible Range Subsequence Matrices, Seaweed All-Pairs Interval LCS, Cyclic LCS & Hirschberg Bitset LCS)

#### `W4B-22`: QOJ / Universal Cup / CodeChef `DISTSUBS` — Range Distinct Subsequences (`区间本质不同子序列个数`) (`[ZH]` / `[EN]`)
- **Statement & Constraints**: Given $S[1..N] \in \{\texttt{'a'}..\texttt{'z'}\}^N$ ($N, Q \le 2 \cdot 10^5$), for each query $[l, r]$ output the number of distinct non-empty subsequences of $S[l..r]$ modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Static range queries for distinct subsequences where Segment Tree of $27 \times 27$ matrices ($O(Q\sigma^2 \log N)$) is too slow.
  2. *Combinatorial Invariant*: By Theorem 2.1, $\det(M_c) = 1$, and $\text{Ans}(l, r) = (\mathbf{1}^T P_r)(P_{l-1}^{-1} \mathbf{e}_{\sigma+1}) - 1 = \mathbf{u}_r^T \cdot \mathbf{v}_{l-1} - 1$.
  3. *Reverse-Engineering Scratchpad*: Precompute $\mathbf{u}_i^T = 2\mathbf{u}_{i-1}^T - \mathbf{u}_{\text{last}[S[i]]-1}^T$ and $\mathbf{v}_i = \mathbf{e}_{\sigma+1} + \mathbf{g}^{(i)}$ via lazy column offset in $O(N\sigma)$ time and space (`§2.3`); answer each query in **$O(\sigma)$ time** via a 27-element dot product!
  4. *Boundary Pitfall*: When $\text{last}[c] = 0$, the subtracted old row $c$ of $P_0 = I_{\sigma+1}$ is $\mathbf{e}_c^T$, not $\mathbf{0}^T$!

#### `W4B-23`: Codeforces 1667E / Universal Cup — Weighted & Length-Generating Range Distinct Subsequences (`[EN]` / `[ZH]`)
- **Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 2 \cdot 10^5$), character weights $\alpha_c \in \mathbb{F}_{998244353}^\times$ (or evaluation point $x \ne 0$), and queries $[l, r]$, compute $\sum_{W \in \text{Subseq}(S[l..r])} \prod_{k=1}^{|W|} \alpha_{W[k]} \pmod{998244353}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Weighted extension of Range Distinct Subsequences.
  2. *Combinatorial Invariant*: By Corollary 2.2, $M_c(\alpha_c)$ has row $c$ filled with $\alpha_c$, so $\det(M_c(\alpha_c)) = \alpha_c \in \mathbb{F}_p^\times$ is invertible with $(M_c(\alpha_c)^{-1})_{c, c} = \alpha_c^{-1}$ and $(M_c(\alpha_c)^{-1})_{c, j} = -1$ for $j \ne c$.
  3. *Reverse-Engineering Scratchpad*: Use the $O((N+Q)\sigma)$ vector dot-product algorithm with $\alpha_c$ in the forward step and $\alpha_c^{-1}$ in the inverse lazy-offset step.
  4. *Boundary Pitfall*: **Local Algebraic Hypothesis (`AGENTS.md`)**: Invertibility requires $\alpha_c \in \mathcal{R}^\times$; if $\alpha_c \equiv 0 \pmod p$, handle $\alpha_c = 0$ characters by deleting them from $S$ before building prefix matrices!

#### `W4B-24`: Codeforces 1810G / Universal Cup — Deque Range Distinct Subsequences (`push/pop_front/back` + $[l, r]$) (`[EN]` / `[ZH]`)
- **Statement & Constraints**: Maintain string $S$ under $Q \le 3 \cdot 10^5$ deque operations (`push_front`, `push_back`, `pop_front`, `pop_back`) and online range distinct subsequence queries $S[l..r]$ modulo $998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Double-ended insertions/deletions + arbitrary range queries $[l, r]$.
  2. *Combinatorial Invariant*: Anchor origin $0$ between front indices $i \le 0$ and back indices $i > 0$. Any range $[l, r]$ has transition product $P_r P_{l-1}^{-1}$ where for $i > 0$, $P_i = M_{S[i]} P_{i-1}$, and for $i \le 0$, $P_{i-1} = P_i M_{S[i]}^{-1}$!
  3. *Reverse-Engineering Scratchpad*: Maintain $\mathbf{u}_i^T = \mathbf{1}^T P_i$ and $\mathbf{v}_i = P_i^{-1} \mathbf{e}_{\sigma+1}$ on both the front stack and back stack in $O(\sigma)$ per push and $O(1)$ per pop, answering $[l, r]$ in $O(\sigma)$ time.
  4. *Boundary Pitfall*: On the front stack ($i \to i-1$), left- and right-multiplication swap roles ($P_{i-1} = P_i M_c^{-1}$ and $P_{i-1}^{-1} = M_c P_i^{-1}$)!

#### `W4B-25`: NowCoder Multi-University / QOJ — Range Gap-$2$ Distinct Subsequences (`区间不相邻本质不同子序列`) (`[ZH]`, NowCoder / QOJ)
- **Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 10^5, |\Sigma| \le 10$), for each query $[l, r]$ count distinct subsequences of $S[l..r]$ with $i_r - i_{r-1} \ge 2$ modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Range queries for `ABC 214F` where the transition matrix is **singular** ($\det = 0$)!
  2. *Combinatorial Invariant*: Because the buffered transition overwrites $f_x$ using delayed states from $i-2$ without adding the current $f_x$, the matrix cannot be inverted (`§2.4`). Instead, any valid subsequence straddling midpoint $M$ either does not use $M$, or jumps from $\le M-1$ to $\ge M+1$.
  3. *Reverse-Engineering Scratchpad*: Offline Divide-and-Conquer over $[L, R]$ (or Segment Tree of $(\sigma+1)\times(\sigma+1)$ boundary transfer matrices) in $O((N + Q)\sigma \log N)$ time.
  4. *Boundary Pitfall*: Canonical lesson in checking $\det(M_c) \ne 0$ before attempting prefix-matrix inversion.

#### `W4B-26`: Luogu P7456 / LOJ 3399 — [THUPC 2021] 区间 LCS (All-Pairs Interval LCS via Seaweed Matrix) (`[ZH]`, THUPC 2021)
- **Statement & Constraints**: Given $A[1..M], B[1..N]$ ($M, N \le 5000$ or $10^5$) and $Q \le 10^6$ queries $(l, r)$, compute $\text{LCS}(A[1..M], B[l..r])$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $Q$ arbitrary interval LCS queries on $B[l..r]$ against $A$.
  2. *Combinatorial Invariant*: By Theorem 3.1 & 3.2, running the Seaweed Comb on $A \times B$ produces $W[1..N]$ (and $p[1..N]$) such that $\text{LCS}(A, B[l..r]) = \#\{k \in [l, r] \mid W[k] < l\} = \#\{i \in [l, r] \mid p[i] > r\}$.
  3. *Reverse-Engineering Scratchpad*: Compute $W[1..N]$ via the 8-line Seaweed Comb in $O(MN)$ time; answer queries in $O(\log N)$ via Persistent Segment Tree / Fenwick Tree (or $O(1)$ via 2D prefix sums for $N \le 5000$).
  4. *Boundary Pitfall*: Initialize left-wall row $i$ to $u = -i$ (strictly increasing towards top-left corner $(0,0)$), and use strict inequality $W[k] < l$ (or $p[i] > r$).

#### `W4B-27`: Universal Cup / Petrozavodsk / Codeforces — Cyclic LCS (`循环最长公共子序列`) via Seaweed Comb (`[EN]` / `[ZH]`)
- **Statement & Constraints**: Given $A[1..M]$ and $B[1..N]$ ($M, N \le 2000$), compute the maximum of $\text{LCS}(\text{shift}_i(A), \text{shift}_j(B))$ over all cyclic rotations of $A$ and $B$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Naive cyclic LCS runs $N$ separate LCS DPs in $O(MN^2)$ time.
  2. *Combinatorial Invariant*: Any non-crossing cyclic matching of size $L$ has at least one cut point in $A$'s standard order $1..M$, which corresponds to a single cut in $B$; thus rotating $B$ alone suffices, and every cyclic shift of $B$ is a length-$N$ window $B'[l..l+N-1]$ of $B' = B \cdot B$!
  3. *Reverse-Engineering Scratchpad*: Run the 8-line Seaweed Comb on $A[1..M] \times B'[1..2N]$ in **$O(MN)$ time** to get $W[1..2N]$; evaluate $\#\{k \in [l, l+N-1] \mid W[k] < l\}$ for $l = 1 \dots N$ in $O(N \log N)$ or $O(N^2)$ time!
  4. *Boundary Pitfall*: Replaces complex $O(MN)$ Schmidt non-crossing shortest-path divide-and-conquer with 10 lines of Seaweed code.

#### `W4B-28`: UOJ / QOJ / 国家集训队互测 — Three-Family Prefix-Suffix & Suffix-Prefix LCS (`前缀-后缀拼接 LCS`) (`[ZH]`, CTT / QOJ)
- **Statement & Constraints**: Given $A[1..M], B[1..N]$ ($M, N \le 5000$) and $Q \le 2 \cdot 10^5$ queries $(i, j)$, compute $\text{LCS}(A[i..M], B[1..j])$ and $\text{LCS}(A[1..i], B[l..N])$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Queries vary a suffix of $A$ against a prefix of $B$ (or prefix of $A$ against suffix of $B$).
  2. *Combinatorial Invariant*: By Theorem 3.2 (Families 2 & 3), a single $O(MN)$ Seaweed Comb on $A \times B$ yields $\text{LCS}(A[i..M], B[1..j]) = \#\{k \in [1, j] \mid W[k] \le -i\}$.
  3. *Reverse-Engineering Scratchpad*: Build 2D prefix sums (or persistent segment tree) over $(k, W[k])$ in $O(MN)$ to answer every query in $O(1)$ or $O(\log N)$ time.
  4. *Boundary Pitfall*: Because row $i$ starts with label $-i$ and rows $i+1..M$ start with $-(i+1)..-M < -i$, the suffix condition on $A[i..M]$ is $W[k] \le -i$.

#### `W4B-29`: Codeforces 1842H / ICPC WF — Optimal Substring Insertion to Maximize LCS (`[EN]`, ICPC / CF)
- **Statement & Constraints**: Given $A[1..M], B[1..N], C[1..K]$ ($M, N, K \le 5000$), insert $C$ into $B$ at the optimal index $k \in [0, N]$ to maximize $\text{LCS}(A, B[1..k] \cdot C \cdot B[k+1..N])$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Inserting $C$ at $B[k]$ partitions $A$ into $A[1..i-1]$ (matched with $B[1..k]$), $A[i..j]$ (matched with $C$), and $A[j+1..M]$ (matched with $B[k+1..N]$).
  2. *Combinatorial Invariant*: All interval values $L_C(i, j) = \text{LCS}(C, A[i..j])$ for $1 \le i \le j \le M$ are given by a single Seaweed Comb of $C$ against $A$ in $O(KM + M^2)$ time!
  3. *Reverse-Engineering Scratchpad*: Precompute prefix LCS $dp_{\text{pref}}[i][k] = \text{LCS}(A[1..i], B[1..k])$, suffix LCS $dp_{\text{suff}}[j][k] = \text{LCS}(A[j..M], B[k..N])$, and $L_C(i, j)$; for each $(i, j)$, combine with $\max_k (dp_{\text{pref}}[i-1][k] + dp_{\text{suff}}[j+1][k+1])$ in $O(MN + KM + M^2)$ total time!
  4. *Boundary Pitfall*: Run the Seaweed Comb with $A$ as the horizontal (interval-queried) string and $C$ as the vertical string.

#### `W4B-30`: Codeforces 1117G / QOJ — $K$-th Lexicographically Smallest Distinct Subsequence on Large Alphabet (`[EN]` / `[ZH]`)
- **Statement & Constraints**: Given $S[1..N]$ ($N, |\Sigma| \le 10^5$) and $K \le 10^{18}$, output the $K$-th lexicographically smallest distinct subsequence of $S$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $|\Sigma| \le 10^5$ requires a persistent-segment-tree DASG, and $K \le 10^{18}$ with answer length up to $N$ requires compressing forced minimum-character chains.
  2. *Combinatorial Invariant*: In $\text{DASG}(S)$, each node $u$ has a persistent segment tree over $c \in [1, |\Sigma|]$ storing subtree sums of $dp[\text{nxt}[u][c]]$ clamped at $K+1$.
  3. *Reverse-Engineering Scratchpad*: Segment-tree binary search finds the next character $c$ in $O(\log |\Sigma|)$; if $c = c_{\min}$ and $K$ is small, binary lift along the $c_{\min}$-chain to skip $O(N)$ unit steps in $O(\log N)$ time.
  4. *Boundary Pitfall*: Remember to decrement $K \leftarrow K - 1$ at each visited state to account for the subsequence terminating at the current node.

#### `W4B-31`: Codeforces 1080F / SPOJ / ICPC — Bit-Parallel LCS + Hirschberg $O(MN/w)$ Space-Optimal Reconstruction (`[EN]` / `[JA]`)
- **Statement & Constraints**: Given $A[1..M], B[1..N]$ ($M, N \le 50{,}000$), reconstruct the actual longest common subsequence string within $256\text{ MB}$ and $2.0\text{s}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $M, N = 50{,}000$ requires $O(MN/w)$ time (bit-parallelism) AND $O(M+N)$ space (Hirschberg divide-and-conquer).
  2. *Combinatorial Invariant*: Combine Theorem 4.1 ($V' = X \mathbin{\&} \sim(X - Y)$) with Hirschberg midpoint splitting at $M/2$.
  3. *Reverse-Engineering Scratchpad*: At each recursive step $(l_A, r_A, l_B, r_B)$, run bit-parallel LCS on the subgrid of width $W = r_B - l_B + 1$ in $O((r_A - l_A)W / 64)$ time; unpack the two midpoint bitvectors into integer prefix sums to locate $j^* \in [l_B-1, r_B]$.
  4. *Boundary Pitfall*: Slice or build pattern masks $M[c]$ only on the active sub-interval $[l_B, r_B]$ so total work across the recursion tree remains $O(MN/w)$.

#### `W4B-32`: AtCoder ABC 285 G / ARC 159 D — Sparse-Match Hunt–Szymanski & Fenwick Seaweed Compression (`[JA]`, AtCoder)
- **Statement & Constraints**: Given $A[1..M], B[1..N]$ ($M, N \le 10^5$) where the total number of matching pairs $\mathcal{M} = \{(i, j) \mid A[i] = B[j]\}$ is at most $2 \cdot 10^5$, compute $\text{LCS}(A, B)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $M, N = 10^5$ with sparse character matches $|\mathcal{M}| \le 2 \cdot 10^5$.
  2. *Combinatorial Invariant*: The step-up threshold columns $j_1 < j_2 < \dots < j_k$ in row $i$ only change at columns $j$ where $A[i] = B[j]$.
  3. *Reverse-Engineering Scratchpad*: For each $i = 1 \dots M$, iterate matching columns $j$ with $B[j] = A[i]$ in **strictly decreasing order**, updating $\text{thresh}[r] \leftarrow \min(\text{thresh}[r], j)$ via binary search in $O(|\mathcal{M}| \log N)$ time.
  4. *Boundary Pitfall*: Iterating $j$ in increasing order allows a single character $A[i]$ to be matched multiple times across the same row!

---

### Tier 4: Mastery & Grandmaster Synthesis (`W4B-33` – `W4B-42` — Unit-Monge $\boxdot$ Divide-and-Conquer, Range LIS via Seaweed, RLE Seaweed, Dynamic Seaweed & Simon's Congruence)

#### `W4B-33`: 国家集训队论文 2021 / QOJ / Universal Cup — Range-Range Substring LCS (`双区间 LCS`: $\text{LCS}(A[l_1..r_1], B[l_2..r_2])$) (`[ZH]` / `[EN]`)
- **Statement & Constraints**: Given $A[1..M], B[1..N]$ ($M, N \le 30{,}000$) and $Q$ queries $(l_1, r_1, l_2, r_2)$, compute $\text{LCS}(A[l_1..r_1], B[l_2..r_2])$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Both $A$ and $B$ are sliced to intervals $[l_1, r_1]$ and $[l_2, r_2]$.
  2. *Combinatorial Invariant*: The Seaweed permutation matrix for horizontal strip $A[l_1..r_1] \times B[1..N]$ is the Unit-Monge distance product ($\boxdot$) of elementary strip permutations inside a Segment Tree over $[1, M]$.
  3. *Reverse-Engineering Scratchpad*: Build a Segment Tree over $A[1..M]$ merging child Seaweed permutations via the $O(K \log K)$ monotone-staircase $\boxdot$ algorithm (`§3.3.3`), compressing out inactive columns of $B$; answer queries by propagating the boundary distribution vector across $O(\log M)$ segment tree nodes via SMAWK monotone minima in $O(\log^2 N)$ per node.
  4. *Boundary Pitfall*: Always compress out identity wires (columns of $B$ with no matches in $A[L..R]$) so a segment tree node of height $L = R - L + 1$ has at most $2L$ active wires instead of $N$.

#### `W4B-34`: 国家集训队论文 2021 / Universal Cup / QOJ — Range LIS (`区间最长上升子序列`) in $O(N \log^2 N)$ via Sparse Seaweed (`[ZH]` / `[EN]`)
- **Statement & Constraints**: Given a permutation $B[1..N]$ of $\{1, \dots, N\}$ ($N, Q \le 10^5$), for each query $[l, r]$ output the length of the Longest Increasing Subsequence $\text{LIS}(B[l..r])$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Range LIS on a permutation of size $10^5$.
  2. *Combinatorial Invariant*: $\text{LIS}(B[l..r]) = \text{LCS}\bigl((1, 2, \dots, N),\, B[l..r]\bigr)$. In the $N \times N$ Seaweed grid of $A = (1..N)$ against $B[1..N]$, each row $x \in [1, N]$ has **exactly one** matching cell $(x, \text{pos}_B[x])$.
  3. *Reverse-Engineering Scratchpad*: Divide-and-conquer over value intervals $[L, R] \subseteq [1, N]$ (`§3.3.4`): restrict to the $K = R - L + 1$ columns of $B$ containing values in $[L, R]$, recurse on $[L, M]$ and $[M+1, R]$, and multiply the two size-$K/2$ Seaweed permutations via $O(K \log K)$ Unit-Monge $\boxdot$ in $O(N \log^2 N)$ total time. Query $\#\{k \in [l, r] \mid W[k] < l\}$ in $O(\log N)$ via Wavelet Matrix / Persistent Segment Tree!
  4. *Boundary Pitfall*: When lifting the two half-permutations of size $K/2$ to size $K$ before calling $\boxdot$, interleave their column coordinates according to the relative order of indices in $B$.

#### `W4B-35`: 国家集训队论文 2021 / QOJ — Run-Length Encoded (RLE) LCS via Seaweed Block Transitions (`[ZH]`, 国家集训队论文)
- **Statement & Constraints**: Given two run-length encoded strings $A = c_1^{a_1} \dots c_m^{a_m}$ and $B = d_1^{b_1} \dots d_n^{b_n}$ ($m, n \le 1000$, unexpanded lengths $\sum a_i, \sum b_j \le 10^9$), compute $\text{LCS}(A, B)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Unexpanded lengths are $10^9$, so we must propagate seaweeds across uniform blocks $c_i^{a_i} \times d_j^{b_j}$ in $O(1)$ or $O(\log(m+n))$ per block.
  2. *Combinatorial Invariant*: Inside a **match block** ($c_i = d_j$), no two wires cross ($(\text{bottom}, \text{right}) = (\text{left}, \text{top})$ shifted diagonally). Inside a **mismatch block** ($c_i \ne d_j$), every pair of wires $(u, v)$ with $u < v$ crosses, while pairs with $u > v$ bounce!
  3. *Reverse-Engineering Scratchpad*: Maintain the compressed seaweed permutation segments across the $m \times n$ blocks (or compose block permutations via $\boxdot$) in $O(mn \log(m+n))$ time.
  4. *Boundary Pitfall*: Even in a mismatch block $c_i \ne d_j$, wires with $u > v$ (already crossed in an earlier block) do **not** cross again!

#### `W4B-36`: QOJ / Petrozavodsk — Dynamic All-Pairs Interval LCS under Character Appends (`动态海草矩阵`) (`[EN]` / `[ZH]`)
- **Statement & Constraints**: Maintain $A$ and $B$ under online right-appends `append_A(c)` and `append_B(c)` and online queries $\text{LCS}(A, B[l..r])$ ($|A|, |B| \le 5000, Q \le 10^5$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Interleaved row appends to $A$, column appends to $B$, and interval LCS queries on $B[l..r]$.
  2. *Combinatorial Invariant*: Maintain both bottom exits $W[1..N]$ and right exits $R[1..M]$ (`§3.3.2`).
  3. *Reverse-Engineering Scratchpad*: `append_A(c)` sweeps $u = -(M+1)$ across $W[1..N]$ in $O(N)$ and sets $R[M+1] = u$; `append_B(c)` sweeps $v = N+1$ down $R[1..M]$ (`if (A[i] == c || R[i] > v) swap(R[i], v);`) in $O(M)$ and appends $W[N+1] = v$.
  4. *Boundary Pitfall*: In `append_B(c)`, $R[i]$ enters cell $(i, N+1)$ from the left and $v$ enters from the top, so the already-crossed condition is `R[i] > v` (never `v > R[i]`).

#### `W4B-37`: AtCoder AGC 055 D / ARC 146 E / JOI Spring Camp — LCS Automaton (`DP套DP`) + Allison–Dix Bit-Parallel Mask Transitions (`[JA]`, AtCoder / JOI)
- **Statement & Constraints**: Given $A[1..K]$ ($K \le 18$) and $M \le 100$, count strings $B \in \Sigma^M$ such that $\text{LCS}(A, B) = L$ for each $0 \le L \le K$ modulo $998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Outer counting DP over the $2^K$ states of the inner LCS DP row.
  2. *Combinatorial Invariant*: By Theorem 4.1, each of the $2^K$ inner DP states is a $K$-bit difference mask $D \in [0, 2^K)$, and its transition on character $c$ is $D' = (D \mathbin{|} M_c) \mathbin{\&} \sim\bigl((D \mathbin{|} M_c) - ((D \ll 1) \mathbin{|} 1)\bigr)$.
  3. *Reverse-Engineering Scratchpad*: Precompute `trans[D][c]` in $O(2^K |\Sigma|)$ using 4 bitwise instructions per entry; run the outer DP in $O(M 2^K |\Sigma|)$ time.
  4. *Boundary Pitfall*: Mask `trans[D][c]` with `(1 << K) - 1` so bit $K$ is never set.

#### `W4B-38`: Codeforces 1784F / Universal Cup — Semi-Local Approximate Matching via Myers' Bit-Parallel Edit Distance (`[EN]`, CF / UCup)
- **Statement & Constraints**: Given text $T[1..N]$ ($N \le 10^5$), pattern $P[1..M]$ ($M \le 5000$), and threshold $K$, find all end positions $j \in [1, N]$ where $P$ matches a suffix of $T[1..j]$ with edit distance $\le K$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Semi-local edit distance at scale $M = 5000, N = 10^5$ requires $O(MN/64)$ bit-parallelism.
  2. *Combinatorial Invariant*: In Myers' bit-parallel column step (`§4.2.1`), free start positions in $T$ correspond to $dp[0][j] = 0 \implies \Delta H_{0, j} = 0$.
  3. *Reverse-Engineering Scratchpad*: Run Myers' 15-instruction column update across $\lceil M/64 \rceil$ words with `X' = (HP << 1)` (no `| 1` at bit $0$ of word $0$), updating current bottom edit distance by $+HP[M-1] - HN[M-1]$.
  4. *Boundary Pitfall*: Including `| 1` in `(HP << 1) | 1` computes global edit distance $\text{ed}(P, T[1..j])$ instead of semi-local substring edit distance!

#### `W4B-39`: QOJ / Universal Cup — Constrained LCS (`CLCS`) via Bit-Parallel Layer Injection (`[EN]` / `[ZH]`, UCup)
- **Statement & Constraints**: Given $A[1..M], B[1..N]$ ($M, N \le 10^4$) and pattern $P[1..K]$ ($K \le 20$), find the longest common subsequence of $A$ and $B$ that contains $P$ as a subsequence.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: 3D DP of size $10^4 \times 10^4 \times 21 \approx 2.1 \times 10^9$ needs bit-parallel compression along $N$.
  2. *Combinatorial Invariant*: Within each prefix match layer $k \in \{0, \dots, K\}$ of $P$, horizontal differences lie in $\{0, 1\}$, and when $A[i] = P[k]$, positions $j$ with $B[j] = P[k]$ transition from layer $k-1$ to layer $k$.
  3. *Reverse-Engineering Scratchpad*: Maintain $K+1$ bitsets $V_0, \dots, V_K$ of width $N$, updating each via Allison–Dix subtraction plus bit-injection from $V_{k-1}$ at match masks $M_B[P[k]]$ in $O(MNK / w)$ time.
  4. *Boundary Pitfall*: Ensure layer $k \ge 1$ is initialized to $-\infty$ (empty/unreachable beyond prefix $0$) until $P[1..k]$ has actually been matched!

#### `W4B-40`: AtCoder ARC 145 E / Universal Cup — Range Universality Index $\iota(S[l..r])$ & Range SAS via Arch Binary Lifting (`[JA]` / `[EN]`)
- **Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 2 \cdot 10^5, |\Sigma| = 26$), for each query $[l, r]$ find the length and lexicographically smallest witness of $\text{SAS}(S[l..r])$ (or $\iota(S[l..r])$) in $O(\log N)$ time.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Range queries for Shortest Absent Subsequence length $\iota(S[l..r]) + 1$.
  2. *Combinatorial Invariant*: By Theorem 1.3 (`§1.3.3`), the first complete arch starting at $i+1$ ends at $\text{arch\_end}[i] = \max_{c \in \Sigma} \text{nxt}[i][c]$.
  3. *Reverse-Engineering Scratchpad*: Precompute binary lifting table $\text{up}[k][i]$ on $i \mapsto \text{arch\_end}[i]$ in $O(N \log N)$ time; for query $[l, r]$, lift from $u = l - 1$ while $\text{up}[k][u] \le r$ in $O(\log N)$ time.
  4. *Boundary Pitfall*: If $\text{arch\_end}[i] = \infty$, set $\text{up}[0][i] = N + 1$ so binary lifting never wraps out of bounds.

#### `W4B-41`: AtCoder AGC 019 F / JOI Open — $k$-Disjoint Alignment Paths & Greene's Seaweed Duality (`[JA]`, AtCoder / JOI)
- **Statement & Constraints**: Given $A[1..M], B[1..N]$, find the maximum total matches collected by $k$ vertex-disjoint alignment paths (or weighted diagonal bonuses).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Generalizing single-path LCS to $k$-disjoint paths ($k$-LCS).
  2. *Combinatorial Invariant*: By Greene's Theorem and Tiskin's Seaweed Duality, the $M+N$ seaweeds decompose the semi-local alignment potential into independent wire displacements.
  3. *Reverse-Engineering Scratchpad*: Compute the Seaweed permutation $W[1..N]$ in $O(MN)$ (or $O(N \log^2 N)$) and aggregate the top $k$ wire displacement contributions.
  4. *Boundary Pitfall*: Carefully distinguish strictly vertex-disjoint grid paths from edge-disjoint paths.

#### `W4B-42`: Universal Cup / Gawrychowski et al. (2021) — Simon's Congruence ($\sim_k$) & Shortest Distinguishing Subsequence (`[EN]` / `[ZH]`)
- **Statement & Constraints**: Given two strings $U[1..M]$ and $V[1..N]$ ($M, N \le 3000$ in quadratic version; $M, N \le 5 \cdot 10^5$ in linear version), find the maximum $k$ such that $U \sim_k V$ (i.e., $U$ and $V$ have the exact same set of subsequences of length $\le k$), and output a shortest distinguishing subsequence $W$ of length $k+1$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Symmetric difference of $\text{Subseq}(U)$ and $\text{Subseq}(V)$ (`§1.4`).
  2. *Combinatorial Invariant*: $W$ distinguishes $U$ and $V$ iff walking $W$ in $\text{DASG}(U) \times \text{DASG}(V)$ reaches a state where $\text{first\_end}_U(W) \le M$ and $\text{first\_end}_V(W) = \infty$ (or vice versa).
  3. *Reverse-Engineering Scratchpad*: For $M, N \le 3000$, run BFS on $\text{DASG}(U) \times \text{DASG}(V)$ from $(0, 0)$ in $O(MN|\Sigma|)$ time; for $M, N \le 5 \cdot 10^5$, construct the Simon-Tree of backward arch universality ranks (Barker et al. 2020 / Gawrychowski et al. 2021) in $O(M + N)$ time.
  4. *Boundary Pitfall*: A distinguishing witness $W$ may exist in $U \setminus V$ OR in $V \setminus U$; test both $(\text{nxt}_U \le M, \text{nxt}_V = \infty)$ and $(\text{nxt}_U = \infty, \text{nxt}_V \le N)$ at every BFS layer.

---

## 7. Consolidated Wave 4B Multilingual Bibliography & Terminology Rosetta Stone (`CITATIONS.md` Master Feed)

### 7.1 Primary Academic, Olympiad & Blog Sources
1. **Tiskin, A. (2008 / 2015)**, *"Semi-local string comparison: Algorithmic techniques and applications"*, Mathematics in Computer Science, 1(4), 571–603 / arXiv:0707.3619. (Introduces Seaweed Matrices, the 0-Hecke sticky braid monoid, $O(N \log N)$ Unit-Monge distance multiplication $\boxdot$, and All-Pairs Interval LCS.)
2. **中国国家集训队 2021 论文 (`[国家集训队论文 2021]`)**, *《单位蒙日矩阵与海草算法在最长公共子序列问题中的应用》 (Unit-Monge Matrices and the Seaweed Algorithm in LCS Problems)*. (Definitive `[ZH]` Olympiad reference on Seaweed combs, $O(K \log K)$ Unit-Monge $\boxdot$ monotone-staircase merge, `[THUPC 2021] 区间 LCS`, and $O(N \log^2 N)$ Range LIS.)
3. **Baeza-Yates, R. A. (1991)**, *"Searching subsequences"*, Theoretical Computer Science, 78(2), 363–376; and **Crochemore, M., Melichar, B., & Troníček, Z. (2000)**, *"Directed Acyclic Subsequence Graph — Overview"*, Journal of Discrete Algorithms. (Foundational papers on `序列自动机` / DASG.)
4. **Simon, I. (1975)**, *"Piecewise testable events"*, Autom. Theor. Form. Lang., LNCS 33, 214–222; **Hébrard, J.-J. (1991)**, *"An algorithm for distinguishing efficiently bit-strings by their subsequences"*, Theoretical Computer Science, 82(1), 35–49. (Introduces Simon's Congruence $\sim_k$, $k$-universality $\iota(S)$, and Arch Factorization $S = A_1 \dots A_k R$.)
5. **Barker, L., Fleischmann, P., Harwardt, K., Manea, F., & Nowotka, D. (2020)** & **Gawrychowski, P., Kociumaka, T., Kosche, M., & Manea, F. (2021)**, *"Optimal algorithms for Simon's congruence"* (STACS 2021). ($O(|U|+|V|)$ Simon-Tree algorithm for testing $U \sim_k V$ and finding the Shortest Distinguishing Subsequence.)
6. **Allison, L., & Dix, T. I. (1986)**, *"A bit-string longest-common-subsequence algorithm"*, Information Processing Letters, 23(6), 305–310; **Crochemore, M., Iliopoulos, C. S., Pinzon, Y. J., & Reid, J. F. (2001)** & **Hyyrö, H. (2003 / 2004)**, *"Bit-parallel LCS-length computation revisited"*. (The 4-operation hardware borrow formula $V' = X \mathbin{\&} \sim(X - Y)$.)
7. **Myers, G. (1999)**, *"A fast bit-vector algorithm for approximate string matching based on dynamic programming"*, Journal of the ACM, 46(3), 395–415. (The $O(MN/w)$ bit-parallel edit distance algorithm using $(VP, VN, HP, HN)$.)
8. **noshi91 / maspypy / tatyam (`[JA]` Competitive Programming Treatises)**, *"部分列 DP の行列表示とその逆行列 (Matrix Representation of Subsequence DP and Its Inverse)"* & *"Seaweed Matrix (Tiskin's Algorithm) による区間 LCS"*. (Japanese competitive programming canon deriving $O((N+Q)\sigma)$ range distinct subsequences via elementary matrix inverses and lazy column offsets.)

### 7.2 Reconciled Multilingual Stringology Rosetta Stone (Wave 4B)
| English (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) |
| :--- | :--- | :--- |
| Directed Acyclic Subsequence Graph (DASG) | 序列自动机 / 子序列自动机 | 部分列オートマトン (`Subsequence Automaton`) |
| Shortest Absent Subsequence (`SAS`) | 最短非子序列 / 最短缺失子序列 | 最短非部分列 (`Shortest Non-Subsequence`) |
| Arch Factorization & Universality Index $\iota(S)$ | 拱分解 / 子序列全集度 | アーチ分解 / 普遍性指数 |
| Simon's Congruence ($U \sim_k V$) | Simon 同余 / $k$-子序列等价 | Simon 合同 |
| Four-Comb Product Automaton ($\text{SAM} \times \text{DASG}$) | 最短不公共子串/子序列乘积自动机 (`[HEOI2015]`) | 直積オートマトン ($\text{SAM} \times \text{DASG}$) |
| Invertible Subsequence Automaton Matrix | 子序列 DP 矩阵可逆性 / 初等矩阵前缀积与逆 | 部分列 DP の可逆行列 / 累積積と逆行列 |
| Tiskin's Seaweed Matrix | 海草矩阵 / 海草算法 | Seaweed 行列 / 海藻アルゴリズム |
| Unit-Monge Matrix & Distance Product ($\boxdot$) | 单位蒙日矩阵与距离乘积 ($\boxdot$) | 単位 Monge 行列と距離積 (`Sticky Braid Product`) |
| All-Pairs Interval LCS / Semi-Local LCS | 区间 LCS / 半局部最长公共子序列 (`[THUPC 2021]`) | 区間 LCS / 半局所 LCS |
| Range Longest Increasing Subsequence (`Range LIS`) | 区间最长上升子序列 (`区间 LIS`) | 区間 LIS (Seaweed 帰着) |
| Bit-Parallel LCS (Allison–Dix / Hyyrö) | 位并行 LCS / Bitset 压位 LCS | ビット並列 LCS (ワード並列 LCS) |
| Myers' Bit-Parallel Edit Distance | Myers 位并行编辑距离 | Myers のビット並列編集距離 |
