# Wave 2B (Cohort 2 — Iterations 68–72): Advanced Suffix Structures — SA-IS, Virtual Suffix Trees, Internal Pattern Matching (IPM) & Bi-Directional Structures

> **Cohort 2 Independent Discovery & Structural Audit Report**
> **Scope**: Iterations 68–72 (`Wave 2B` redundant discovery pass).
> **Mandate**: 100% independent derivation of the structural invariants, failure modes, and data-structure couplings for Linear-Time Induced Sorting (SA-IS), Virtual Suffix Trees (`后缀树虚树`) & Cartesian Trees on `height`, Internal Pattern Matching (IPM) & The Basic Substring Dictionary (Kociumaka et al.), and Bi-Directional Suffix Structures (SCDAWG, Affix Automata, Suffix Balanced Trees `后缀平衡树`, Online Double-Ended Suffix Trees).

---

## Iteration 68: Linear-Time Induced Sorting (SA-IS) as a Structural Reduction

### 68.1 The Diagnostic Signal: Why $O(N \log N)$ Doubling Fails at Scale or on Non-Standard Domains

Standard prefix-doubling suffix array construction runs in $O(N \log N)$ time with radix sort or $O(N \log^2 N)$ with comparison sort. While sufficient for $N \le 2 \times 10^5$, three concrete competitive programming regimes break doubling or expose its structural rigidity:

1. **Extreme Scale and Tight Time Limits ($N \in [10^6, 10^7]$)**: In modern ICPC/IOI/NOI tasks with $N \ge 2 \times 10^6$ (or multi-string concatenations reaching $5 \times 10^6$), $O(N \log N)$ cache-unfriendly random bucket accesses during 20 doubling passes exceed 1.0s–1.5s limits.
2. **Recursive / Non-Power-of-Two Alphabet Compression**: When inducing suffix order on modified string spaces (such as Lyndon-word factorizations, BWT over cyclic strings, or run-length encoded inputs), doubling performs redundant work over identical type runs.
3. **Lack of Prefix-Free Sentinel or Cyclic/Generalized Domains**: Standard SA-IS relies critically on a unique lexicographically smallest sentinel `$` at the end of the string. When adapting induced sorting to cyclic shifts (`BWT`), generalized multi-string sets without distinct sentinels, or trees, blindly applying a textbook SA-IS template produces silent bucket overwrites or wrong tie-breaking.

---

### 68.2 The Combinatorial Word Invariant: L/S Classification, LMS Substrings, and the Two-Pass Induction Proof

Let $S[1..n]$ be a string over an ordered alphabet $\Sigma$, terminated by a unique sentinel $S[n] = \texttt{\$}$ strictly smaller than every character in $\Sigma$. Denote by $\text{suf}(i) = S[i..n]$ the suffix starting at index $i$.

#### 1. L-Type and S-Type Suffix Classification

Every position $i \in [1..n]$ is classified by comparing $\text{suf}(i)$ with its immediate right neighbor $\text{suf}(i+1)$:
- **S-type (Smaller)**: $i$ is S-type if $\text{suf}(i) < \text{suf}(i+1)$. By convention, $n$ (the sentinel `$`) is S-type.
- **L-type (Larger)**: $i$ is L-type if $\text{suf}(i) > \text{suf}(i+1)$.

Because all suffixes have distinct lengths and end with the unique minimum sentinel `$`, $\text{suf}(i) \ne \text{suf}(i+1)$ always holds. This yields a backward $O(n)$ recurrence for `type[i]`:
$$
\text{type}[i] = \begin{cases}
\text{S} & \text{if } i = n \text{ or } S[i] < S[i+1] \text{ or } (S[i] = S[i+1] \text{ and } \text{type}[i+1] = \text{S}), \\
\text{L} & \text{if } S[i] > S[i+1] \text{ or } (S[i] = S[i+1] \text{ and } \text{type}[i+1] = \text{L}).
\end{cases}
$$

#### 2. The Bucket Partition Invariant (Why L Precedes S Within Every Character Bucket)

Consider the bucket $B_c = \{ i \mid S[i] = c \}$ of all suffixes starting with character $c \in \Sigma$.

> **Lemma 68.1 (Intra-Bucket L/S Separation)**: For any $i \in B_c$:
> - If $\text{type}[i] = \text{L}$, then the first character after the run of $c$'s at $i$ is some $c' < c$ (or $\texttt{\$}$), so $\text{suf}(i) < c^\infty$.
> - If $\text{type}[i] = \text{S}$, then the first character after the run of $c$'s at $i$ is some $c'' > c$, so $\text{suf}(i) > c^\infty$.
>
> Consequently, inside every character bucket $B_c$, **every L-type suffix is strictly lexicographically smaller than every S-type suffix**:
> $$
> B_c = B_{c,\text{L}} \sqcup B_{c,\text{S}}, \quad \text{where } \forall i \in B_{c,\text{L}}, \, \forall j \in B_{c,\text{S}}, \quad \text{suf}(i) < \text{suf}(j).
> $$

This single inequality is the engine of induced sorting: L-type suffixes occupy a contiguous prefix of $B_c$, and S-type suffixes occupy the remaining contiguous suffix of $B_c$.

#### 3. Leftmost S-Type (LMS) Positions and LMS Substrings

A position $i \in [2..n]$ is a **Leftmost S-type (LMS)** position (often denoted $\text{S}^*$) if:
$$
\text{type}[i] = \text{S} \quad \text{and} \quad \text{type}[i-1] = \text{L}.
$$
Let $1 < i_1 < i_2 < \dots < i_m = n$ be all LMS positions in $S$.
- Because $i=1$ has no left neighbor and no two LMS positions can be adjacent ($\text{type}[i-1] = \text{L}$ requires at least one L-type position between consecutive S-runs), the number of LMS positions satisfies:
  $$
  m \le \left\lfloor \frac{n}{2} \right\rfloor.
  $$
- An **LMS substring** is either a segment $S[i_k .. i_{k+1}]$ between two consecutive LMS positions ($1 \le k < m$), or the singleton sentinel $S[n..n]$ for $k = m$.

#### 4. Canonical Ordering of LMS Substrings & Equality Testing

How do we compare two LMS substrings $S[i_a..i_{a+1}]$ and $S[i_b..i_{b+1}]$ so that their relative order is consistent with the relative order of the full LMS suffixes $\text{suf}(i_a)$ and $\text{suf}(i_b)$?
We compare LMS substrings simultaneously by **character and L/S type** at each offset $d = 0, 1, \dots$:
- At offset $d$, compare $(S[i_a+d], \text{type}[i_a+d])$ vs. $(S[i_b+d], \text{type}[i_b+d])$, where inside the same character $c$, $\text{L} < \text{S}$.
- Two LMS substrings are **canonically identical** if and only if they have the exact same length $\ell = i_{a+1} - i_a + 1 = i_{b+1} - i_b + 1$, and for all $0 \le d < \ell$:
  $$
  S[i_a + d] = S[i_b + d] \quad \text{and} \quad \text{type}[i_a + d] = \text{type}[i_b + d].
  $$

```
Index:   1   2   3   4   5   6   7   8   9  10  11  12
Char:    m   i   s   s   i   s   s   i   p   p   i   $
Type:    L   S   L   L   S   L   L   S   L   L   L   S
LMS:         *           *           *               *
LMS substrings:
  i_1=2..5: "issi" (S,L,L,S)
  i_2=5..8: "issi" (S,L,L,S)  <-- Identical char & type!
  i_3=8..12: "ippi$" (S,L,L,L,S)
  i_4=12..12: "$" (S)
```

> **Theorem 68.2 (LMS Prefix Sufficiency)**: Suppose we place all LMS positions into the tails of their respective character buckets $B_{c,\text{S}}$ (not necessarily sorted by full suffix, even arbitrary order within each bucket tail) and run the two-pass Induced Sort (Pass 1: left-to-right L-induction; Pass 2: right-to-left S-induction). Then:
> 1. All **LMS substrings** are sorted into exact canonical order (with ties between identical LMS substrings broken arbitrarily).
> 2. If instead the LMS positions were initially placed into the tails of $B_{c,\text{S}}$ in the **exact sorted order of their full LMS suffixes** $\text{suf}(i_k)$, then the same two-pass Induced Sort places **all $n$ suffixes** of $S$ into exact sorted order!

*Proof of why Pass 1 and Pass 2 never read an uninitialized dependency (Strict Pointer Monotonicity)*:
- **Pass 1 (Left-to-Right L-Induction)**: Maintain a head pointer `head[c]` at the beginning of each bucket $B_c$. Scan the array `SA[1..n]` from $p = 1$ to $n$. Whenever `SA[p] = j > 1` and $\text{type}[j-1] = \text{L}$, place $j-1$ at `SA[head[S[j-1]]++]`.
  - *Why is $j$ always placed before $j-1$ is needed?* Because $j-1$ is L-type, we have $\text{suf}(j-1) > \text{suf}(j)$. Thus in the final sorted order, index $j$ sits strictly to the left of $j-1$ (`rk[j] < rk[j-1]`). Furthermore, all L-type suffixes starting with $c = S[j-1]$ are induced strictly in increasing order of their stripped suffix $\text{suf}(j)$. And where do the very first triggers come from? Every maximal contiguous block of L-type indices $j-k, \dots, j-1$ is immediately followed by an S-type index $j$ with $\text{type}[j-1]=\text{L}$—which is by definition an **LMS position**! Since all LMS positions are pre-seeded in `SA` before Pass 1 begins, induction starts at the LMS seeds and propagates leftward across every L-run without ever starving.
- **Pass 2 (Right-to-Left S-Induction)**: Clear the old LMS seeds (or overwrite them), reset a tail pointer `tail[c]` to the end of each bucket $B_c$, and scan `SA[1..n]` from $p = n$ down to $1$. Whenever `SA[p] = j > 1` and $\text{type}[j-1] = \text{S}$, place $j-1$ at `SA[tail[S[j-1]]--]`.
  - *Why is $j$ always scanned before $j-1$ is needed?* Because $j-1$ is S-type, $\text{suf}(j-1) < \text{suf}(j)$, so in `SA`, $j$ sits strictly to the **right** of $j-1$ (`rk[j] > rk[j-1]`). Scanning right-to-left visits $j$ before $j-1$'s target slot is reached, filling $B_{c,\text{S}}$ from largest to smallest! And every maximal contiguous block of S-type indices is bordered on its right by an L-type index (already sorted in Pass 1!), except the block containing $n$, which starts at $n = \texttt{\$}$ (placed at `SA[1]` at the end of Pass 1 or seeded).

---

### 68.3 The Reverse-Engineering Scratchpad: 5-Stage Recursive Reduction Contract

Because $m \le \lfloor n/2 \rfloor$, SA-IS satisfies the recurrence $T(n) = T(\lfloor n/2 \rfloor) + O(n) = O(n)$ time and $O(n)$ space:

1. **Stage 1 (Type & LMS Extraction)**: Scan $i = n-1 \dots 1$ to compute `type[i]` and collect LMS indices $i_1 < i_2 < \dots < i_m$. Compute bucket boundaries `bkt_start[c]` and `bkt_end[c]`.
2. **Stage 2 (LMS Substring Sorting via Preliminary Induction)**:
   - Seed `SA` with $-1$, place LMS indices $i_1, \dots, i_m$ into the tails of their character buckets.
   - Run Pass 1 (left-to-right L-induction) and Pass 2 (right-to-left S-induction).
3. **Stage 3 (LMS Substring Naming & Reduced String $S_1$)**:
   - Extract the LMS indices from `SA` in their newly induced order.
   - Compare each adjacent pair of LMS substrings in $O(\text{length of LMS substring})$ time (Checking both character and `type`!). Because $\sum_{k=1}^{m-1} (i_{k+1} - i_k + 1) = (n - i_1) + m - 1 \le 2n$, total comparison work across all adjacent LMS substrings is strictly $O(n)$!
   - Assign integer rank names $1, \dots, \sigma_1$ to the LMS positions in their original left-to-right string order $i_1, \dots, i_m$ to form reduced string $S_1[1..m]$.
4. **Stage 4 (Recursion or Direct Inversion)**:
   - If $\sigma_1 < m$ (at least two LMS substrings were identical), recursively call $\text{SA-IS}(S_1, \sigma_1)$ to get $\text{SA}_1[1..m]$.
   - If $\sigma_1 = m$ (all LMS substrings are distinct), $\text{SA}_1[S_1[k]] = k$ directly in $O(m)$ time without recursion.
5. **Stage 5 (Final Full-Suffix Induction)**:
   - Map $\text{SA}_1[1..m]$ back to the true LMS positions $i_{\text{SA}_1[1]}, \dots, i_{\text{SA}_1[m]}$.
   - Clear `SA`, place the sorted LMS positions into the **tails** of their character buckets in exact order, and run Pass 1 (L-induction) and Pass 2 (S-induction) one final time.

---

### 68.4 Extending SA-IS to Non-Standard Domains & Boundary Pitfalls

| Domain Adaptation | Why Naive SA-IS Fails | Structural Modification |
| :--- | :--- | :--- |
| **Generalized SA on $k$ Strings $S_1, \dots, S_k$** | Concatenating with a **single shared separator** `#` violates the unique-sentinel rule: if $S_a = S_b$, two LMS substrings ending at `#` can be identical even at the separator, or suffixes leak across `#`. Using $k$ distinct separators $\texttt{\$_1 < \dots < \$_k}$ blows up the alphabet by $k$. | Define virtual sentinel positions at the end of each string $S_r$. Mark every virtual sentinel position as **S-type (and LMS)**, with the tie-breaking rule that virtual sentinels are strictly smaller than any real character, and among sentinels, the sentinel of $S_a$ is smaller than $S_b$ iff $a < b$. Never compare characters past a sentinel! |
| **Cyclic Suffix Array / Burrows–Wheeler Transform (BWT)** | A cyclic string $S^\infty$ has no sentinel `$`, and if $S = w^d$ is a power of a primitive root $w$, cyclic shifts at period multiples are identical. | First find the lexicographically smallest cyclic shift (or Lyndon conjugate) in $O(n)$ via Duval's algorithm (`Wave 1B`), rotate $S$ so it starts with a Lyndon word $w$ (or $w^d$), or define cyclic L/S types where a completely periodic tie defaults to S-type at period boundaries. |
| **Tree Suffix Array (All Root-to-Leaf or Node-to-Root Paths)** | SA-IS requires each suffix $j$ to have a **unique** predecessor $j-1$ for induction, which holds if paths go **from node $u$ to the root** (each $u$ has a unique parent $p(u)$, so $\text{suf}(u) = c(u) + \text{suf}(p(u))$), provided branching children can be seeded. | Induction works on **upward tree paths** ($\text{suf}(u) = S[u] \cdot \text{suf}(\text{parent}(u))$): when scanning `SA[p] = v`, iterate over all children $u \in \text{children}(v)$ of matching L/S type! However, two distinct nodes $u_1, u_2$ can have **identical upward strings**, so ranks are no longer a permutation—requiring bucket-grouped tie propagation. |

#### Broken-Invariant Counterexamples
1. **Comparing Only Characters (Ignoring L/S Types) During LMS Substring Naming**:
   - Consider $S = \texttt{babab\$}$ ($n=6$):
     - Indices: $1:\texttt{b(L)}, 2:\texttt{a(S*)}, 3:\texttt{b(L)}, 4:\texttt{a(S*)}, 5:\texttt{b(L)}, 6:\texttt{\$(S*)}$.
     - Suppose in another string we have two LMS substrings $S[i_1..i_2] = \texttt{aba}$ where the second `a` is followed by `c` (so the second `a` is S-type), vs. $S[j_1..j_2] = \texttt{aba}$ where the second `a` is followed by `a` then `c` (still S-type) vs. where an internal character has different L/S type at the boundary. Specifically, if an LMS substring $A = \texttt{ab}$ ends at `b(S*)` (because `b` is followed by `c`) and another prefix has `ab` where `b` is `L`-type (followed by `a`, so the LMS substring is actually `aba`), failing to check the exact LMS endpoint or type merges unequal substrings!
2. **Stale LMS Seeds Not Cleared Before Pass 2**:
   - In Stage 2, LMS indices are placed at the **ends** of $B_{c,\text{S}}$ only as an approximate seed. During Pass 1, L-type suffixes are induced using these seeds. Before Pass 2 runs, if you leave the approximate LMS seeds sitting in $B_{c,\text{S}}$ instead of overwriting/clearing the S-type suffix slots (keeping only $n = \texttt{\$}$), Pass 2 will read the **unsorted** initial LMS seeds when scanning right-to-left, corrupting the induced S-order!

---

## Iteration 69: Virtual Suffix Trees (`后缀树虚树`), Cartesian Tree on `height` & DSU-on-Tree

### 69.1 The Diagnostic Signal: From Whole-String LCP to Subset & Multi-Scale LCP Aggregations

Suppose a problem gives a string $S$ of length $N$ and asks either:
1. **All-Pairs LCP Function over the Whole String**: Compute $\sum_{1 \le i < j \le N} f(\text{LCP}(\text{suf}(i), \text{suf}(j)))$ or $\max_{\text{LCP}(i, j) \ge r} w_i \cdot w_j$ (`[AHOI2013] 差异`, `[NOI2015] 品酒大会`).
2. **Subset Query LCP Aggregation**: Across $Q$ queries ($\sum (|A_q| + |B_q|) \le 4 \times 10^5$), each giving subsets of suffixes or substrings $A_q, B_q$, compute $\sum_{u \in A_q} \sum_{v \in B_q} \text{LCP}(u, v)$ (`CF 1073G — Yet Another LCP Problem`).
3. **Substring Weight $\times$ Frequency Statistics**: Compute $\sum_{t \in \text{Sub}(S)} g(|t|, \text{occ}(t))$ where $g$ is non-linear in $\text{occ}(t)$ (e.g., $\text{occ}(t)^2$ in `CF 802I`, or forbidden-endpoint filtered occurrences in `CF 873F`).

A naive approach iterating over pairs $(i, j)$ takes $O(N^2)$ or $O(|A_q||B_q|)$ time. What converts pairwise LCP into linear-time tree DP?

---

### 69.2 The Combinatorial Word Invariant: LCP Range-Minimum Identity & Suffix Tree $\leftrightarrow$ `height` Cartesian Tree Duality

Let $\text{SA}[1..N]$ be the suffix array of $S$, $\text{rk}[1..N]$ be its inverse permutation, and $H[k] = \text{height}[k] = \text{LCP}(\text{suf}(\text{SA}[k-1]), \text{suf}(\text{SA}[k]))$ for $2 \le k \le N$.

#### 1. The LCP Range-Minimum Theorem

For any two suffixes at SA positions $1 \le x < y \le N$:
$$
\text{LCP}(\text{suf}(\text{SA}[x]), \text{suf}(\text{SA}[y])) = \min_{x < k \le y} H[k].
$$
*Why is this true?* Sort any three strings $A < B < C$ lexicographically. Every common prefix of $A$ and $C$ must also be a prefix of $B$ (since $A_d \le B_d \le C_d$ at the first differing position), so $\text{LCP}(A, C) = \min(\text{LCP}(A, B), \text{LCP}(B, C))$. Induction over the adjacent steps $x, x+1, \dots, y$ yields the minimum over $H[x+1..y]$.

#### 2. Isomorphism Between the Suffix Tree of $S$ and the Min-Cartesian Tree of $H[2..N]$

Every internal node $u$ of the **Suffix Tree** of $S$ represents a maximal right-branching substring (or left-branching in the reverse view) whose occurrences correspond to a contiguous interval $[L_u, R_u]$ in $\text{SA}$ where all suffixes share a common prefix of length $\ell_u$, and any extension to $L_u - 1$ or $R_u + 1$ drops the LCP strictly below $\ell_u$:
$$
\min_{L_u < k \le R_u} H[k] = \ell_u, \quad H[L_u] < \ell_u, \quad H[R_u + 1] < \ell_u.
$$
This is **literally the definition of a node in the Min-Cartesian Tree of the array $H[2..N]$** (or equivalently, the Kruskalian Reachability Tree when merging adjacent SA positions $k-1$ and $k$ in decreasing order of $H[k]$)!

```
Suffix Array positions:  SA[1]     SA[2]     SA[3]     SA[4]
Adjacent LCPs:               H[2]=3    H[3]=1    H[4]=4
Cartesian Tree on H:
             [H[3] = 1]  <-- LCA of (SA[1..2]) and (SA[3..4]), interval [1..4]
              /      \
       [H[2] = 3]   [H[4] = 4]
        /      \     /      \
     SA[1]   SA[2] SA[3]   SA[4]
```

> **Theorem 69.1 (Three Equivalent Representations of the Suffix Tree)**:
> For any string $S$ of length $N$:
> 1. The **Min-Cartesian Tree** built on $\text{height}[2..N]$ (with $N$ external leaves $\text{SA}[1..N]$ and $N-1$ internal nodes $H[2..N]$, collapsing equal-value parent-child edges),
> 2. The **Kruskal Reconstruction Tree (DSU Merging)** formed by sorting $k \in [2..N]$ in descending order of $H[k]$ and uniting DSU components of $k-1$ and $k$, and
> 3. The **Parent Link Tree of the Suffix Automaton (SAM) built on the reversed string $S^R$** (where $\text{len}(u)$ is the string depth $\ell_u$),
> are **canonically isomorphic** as edge-weighted rooted trees!

---

### 69.3 The Reverse-Engineering Scratchpad: Monotonic Stack, DSU Sweeping, and Virtual Suffix Trees (`后缀树虚树`)

Depending on the problem query type, we compile Theorem 69.1 into one of four algorithmic engines:

#### Engine A: Monotonic Stack Contribution over $H[2..N]$ (`[AHOI2013] 差异`, `CF 802I`, `CF 873F`)
When the problem asks for $\sum_{1 \le x < y \le N} \min_{x < k \le y} H[k]$ or a function of the maximal rectangle of height $H[k]$:
- Find for each $k \in [2..N]$ the largest interval $[L_k, R_k]$ of $H$-indices such that:
  - For $j \in [L_k, k-1]$, $H[j] > H[k]$ (strict inequality on the left),
  - For $j \in [k+1, R_k]$, $H[j] \ge H[k]$ (non-strict inequality on the right, to avoid double-counting ties!).
- Then $H[k]$ is the unique tie-broken minimum for exactly $(k - L_k + 1)(R_k - k + 1)$ pairs of suffixes $(x, y)$ with $L_k - 1 \le x < k \le y \le R_k$.
- Furthermore, if we collapse equal heights into maximal rectangles $[l, r]$ where $\min_{l < j \le r} H[j] = h$ and $p = \max(H[l], H[r+1])$ is the parent's string depth, then this node represents **$h - p$ distinct substrings** (of lengths $p+1, p+2, \dots, h$), each occurring **exactly $r - l + 1$ times** in $S$!
- Therefore, for any function $g(\text{len}, \text{occ})$:
  $$
  \sum_{t \in \text{Sub}(S)} g(|t|, \text{occ}(t)) = \sum_{\text{internal node } u} \sum_{\ell = \text{len}(p(u)) + 1}^{\text{len}(u)} g(\ell, \text{sz}(u)).
  $$

#### Engine B: Offline DSU Sweep in Decreasing Order of $H[k]$ (`[NOI2015] 品酒大会`)
When the problem asks, for every threshold $r \in [0..N-1]$, to aggregate pairs $(i, j)$ with $\text{LCP}(i, j) \ge r$ (including non-linear extremal queries like $\max_{\text{LCP}(i,j) \ge r} a_i a_j$ where $a_i$ can be negative!):
- Maintain a DSU over SA indices $1..N$. Initially each index $k$ is a singleton component with $\text{sz}[k] = 1$, $\max_1[k] = \min_1[k] = a_{\text{SA}[k]}$.
- Sort the adjacent edges $e_k = (k-1, k)$ in decreasing order of weight $H[k]$ from $N-1$ down to $0$.
- When merging component $U$ and component $V$ at height $r = H[k]$:
  - New pairs with exact LCP $= r$ equals $\text{sz}[U] \cdot \text{sz}[V]$.
  - Candidate maximum product at threshold $r$ is $\max(\max_1[U] \cdot \max_1[V], \min_1[U] \cdot \min_1[V])$.
- Finally, take a suffix sum (for counts) and suffix maximum (for products) from $r = N-1$ down to $0$.

#### Engine C: Virtual Suffix Tree (`后缀树虚树`) for Subset Queries (`CF 1073G`, `[SDOI2016] 生成魔咒` variants)
Given a query with $k$ specified substrings $\{ S[l_1..r_1], \dots, S[l_k..r_k] \}$:
1. **Locate each substring $S[l_i..r_i]$ in the Suffix Tree**:
   - Either use the explicit Suffix Tree (SAM of $S^R$) and binary-lift from the leaf of $\text{suf}(l_i)$ to the highest ancestor $u_i$ with $\text{len}(u_i) \ge r_i - l_i + 1$,
   - Or operate directly on the Suffix Array: represent each substring $S[l_i..r_i]$ by its SA rank $\text{rk}[l_i]$ capped at length $\ell_i = r_i - l_i + 1$.
2. **Build the Virtual Suffix Tree in $O(k \log k)$**:
   - Sort the query terminals by their SA rank $\text{rk}$ (which is already the DFS order of the Suffix Tree!).
   - For each adjacent pair of sorted terminals $u_j, u_{j+1}$, compute their LCA in the Suffix Tree, whose string depth is $\min(\ell_j, \ell_{j+1}, \text{RMQ}_H(\text{rk}[u_j]+1 .. \text{rk}[u_{j+1}]))$.
   - Use the standard monotonic-stack Virtual Tree (`虚树`) construction to obtain a compressed tree of at most $2k - 1$ nodes, and run $O(k)$ tree DP on the virtual tree!

#### Engine D: DSU-on-Tree (`树上启发式合并`) over the Suffix Tree / Cartesian Tree
When merging pair contributions across two subtrees where the pair condition mixes **SA rank proximity** and **original string index proximity** $i, j$ (e.g., $\max_{|i - j| \le D} \text{LCP}(i, j)$ or $\sum_{i < j} f(\text{LCP}(i, j), |i - j|)$):
- Traverse the Cartesian Tree of $H$ (or SAM Link Tree). Keep the heavy child's ordered set `std::set<int>` of original string indices $i$, and insert each light child's indices one by one.
- Whenever a light index $i$ is inserted into the heavy set, only its **immediate predecessor $i^-$ and successor $i^+$** in the set can minimize $|i - j|$ at the current LCA string depth $\ell_u$, generating at most $O(N \log N)$ candidate dominant pairs $(i, i^-)$ and $(i, i^+)$ across the entire tree! This is the canonical **Dominant Pair (`支配对`)** reduction on Suffix Trees.

---

### 69.4 Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Symmetric Strict vs. Non-Strict Monotonic Stack Bounds**:
   - If you use strict inequality `$H[j] > H[k]$` on **both** the left and right when finding $[L_k, R_k]$, then for $S = \texttt{aaaa}$ where $H = [3, 2, 1]$, duplicate values in $H$ (e.g. $S = \texttt{ababab}$, $H$ has two `2`s) will cause pairs spanning both `2`s to be **omitted completely**! Conversely, using $\ge$ on both sides **double-counts** those pairs. Always use `>` on one side and `>=` on the other.
2. **Forgetting Length-1 Single-Suffix Nodes in Substring Aggregations (`CF 802I`, `CF 873F`)**:
   - The Cartesian tree on $H[2..N]$ only groups substrings shared by **at least two** suffixes ($\text{occ}(t) \ge 2$). Substrings that occur **only once** ($\text{occ}(t) = 1$) reside on the leaf edges below the deepest internal node! Specifically, for each suffix $\text{SA}[k]$ of total length $n - \text{SA}[k] + 1$, let $h_{\max}(k) = \max(H[k], H[k+1])$. All prefixes of $\text{suf}(\text{SA}[k])$ of lengths $\ell \in [h_{\max}(k) + 1 .. n - \text{SA}[k] + 1]$ occur **exactly once** in $S$. Omitting these leaf edges loses all $\text{occ}(t) = 1$ contributions!
3. **Negative Weights in `[NOI2015] 品酒大会` (`r = 0` Base Case & Minimum Tracking)**:
   - Two negative deliciousness values $a_i, a_j < 0$ can multiply to a huge positive product. Tracking only component maximums misses $\min_1[U] \cdot \min_1[V]$. Also, even if $H[k] = 0$ for some adjacent suffixes, they still merge at $r = 0$!

---

## Iteration 70: Internal Pattern Matching (IPM) & The Basic Substring Dictionary (Kociumaka et al.)

### 70.1 The Diagnostic Signal: Treating Substrings $S[l..r]$ as First-Class Atomic Objects

In classical string algorithms, a pattern $P$ is given externally and matched against a text $T$ in $O(|P| + |T|)$ time. In **Internal Pattern Matching (IPM)**—systematized in the landmark dissertation and STOC/SODA papers of Tomasz Kociumaka, Jakub Radoszewski, Wojciech Rytter, and Tomasz Waleń—both the pattern and the text are **substrings of the same static string $S[1..N]$**, specified only by their endpoints $(l_1, r_1)$ and $(l_2, r_2)$, and queries must be answered in **$O(1)$ or $O(\text{polylog } N)$ time per query**!

When a problem asks $Q \le 5 \times 10^5$ queries on $S[1..N]$ of the form:
- *"Compare $S[a..b] \cdot S[c..d]$ vs. $S[e..f]$ lexicographically"*,
- *"Find the $k$-th occurrence of $S[l_1..r_1]$ inside $S[l_2..r_2]$"*,
- *"Find the longest border (or smallest period) of $S[l..r]$"* (`[BJWC2018] Border 的四种求法`), or
- *"Count how many substrings in a dictionary occur inside $S[l..r]$ or tie-break splits across prefix/suffix pairs"*,

any algorithm whose query time scales with the substring length $|S[l..r]| = r - l + 1$ immediately TLEs in $O(NQ)$.

---

### 70.2 The Combinatorial Word Invariant: Basic Substring Dictionary Primitives & The Periodicity of Internal Occurrences

#### Primitive 1: $O(1)$ Longest Common Extension ($\text{LCE}(i, j)$) & Substring Lexicographical Comparison
Given two starting positions $i, j \in [1..N]$ with $\text{rk}[i] < \text{rk}[j]$:
$$
\text{LCE}(i, j) = \min_{\text{rk}[i] < k \le \text{rk}[j]} H[k].
$$
With an $O(N \log N)$-space (or $O(N)$ Method of Four Russians) RMQ table over $H[2..N]$, $\text{LCE}(i, j)$ is answered in $O(1)$ time.
From $\text{LCE}$, comparing two arbitrary substrings $U = S[l_1..r_1]$ and $V = S[l_2..r_2]$ takes $O(1)$ time:
1. Let $\ell = \min(|U|, |V|, \text{LCE}(l_1, l_2))$.
2. If $\ell = |U|$ and $\ell = |V|$, then $U = V$.
3. If $\ell = |U| < |V|$, then $U < V$; if $\ell = |V| < |U|$, then $U > V$.
4. Otherwise $\ell < \min(|U|, |V|)$, and the comparison reduces to $S[l_1 + \ell] \lessgtr S[l_2 + \ell]$ (or $\text{rk}[l_1] \lessgtr \text{rk}[l_2]$).

**Concatenation Comparison ($A_1 A_2 \dots A_k$ vs. $B_1 B_2 \dots B_m$)**:
Given two virtual strings formed by concatenating $k$ substrings of $S$, we maintain two pointers into the pieces $(p_A, \text{offset}_A)$ and $(p_B, \text{offset}_B)$. At each step, we compute $\ell = \text{LCE}$ of the current suffixes of piece $p_A$ and piece $p_B$:
- If $\ell$ is strictly smaller than the remaining length of both current pieces, we find the exact mismatch character in $O(1)$ and terminate!
- Otherwise, at least one piece is completely exhausted, so we advance $p_A$ or $p_B$ in $O(1)$. Total time: $O(k + m)$!

#### Primitive 2: Internal Pattern Matching Theorem (Why Occurrences of $U$ in $V$ Form $O(1)$ Arithmetic Progressions when $|V| \le 2|U|$)

Suppose we want to find **all occurrences** of a substring $U = S[l_1..r_1]$ inside another substring $V = S[l_2..r_2]$ where $|U| \le |V| < 2|U|$ (a **2-approximate length ratio**).

> **Theorem 70.1 (The IPM Arithmetic Progression Lemma)**:
> Let $U$ and $V$ be strings with $|U| \le |V| < 2|U|$. Let $\text{Occ}(U, V) = \{ i_1 < i_2 < \dots < i_k \}$ be the starting positions of all occurrences of $U$ in $V$. Then:
> 1. If $k \le 2$, $\text{Occ}(U, V)$ has at most 2 elements.
> 2. If $k \ge 3$, then $\text{Occ}(U, V)$ forms a **single arithmetic progression** with common difference $d = i_2 - i_1 = \text{per}(U)$, the shortest period of $U$!

*Proof (Double-Overlap Alignment)*:
Since $i_1$ and $i_k$ are occurrences of $U$ inside $V$ and $|V| < 2|U|$, we have $i_k + |U| - 1 \le |V| < 2|U|$, which forces $i_k - i_1 < |U|$. Thus **even the first occurrence $i_1$ and the last occurrence $i_k$ overlap by at least $2|U| - |V| \ge 1$ character**!
In particular, any two consecutive occurrences $i_r, i_{r+1}$ overlap by $|U| - (i_{r+1} - i_r) > |U|/2$, so $d_r = i_{r+1} - i_r < |U|/2$ is a period of $U$. If $d_r \ne \text{per}(U)$, then by the Weak Periodicity Lemma ($\gcd(d_r, \text{per}(U))$ is also a period of $U$ since $d_r + \text{per}(U) < |U|$), $d_r$ must be a multiple of $\text{per}(U)$, and the periodic block extending from $i_1$ to $i_k + |U| - 1$ cannot skip an intermediate shift of $\text{per}(U)$! Thus $i_1, i_2, \dots, i_k$ is an arithmetic progression with step $d = \text{per}(U)$. $\blacksquare$

---

### 70.3 The Reverse-Engineering Scratchpad: `[BJWC2018] Border 的四种求法` (The Four Canonical Methods for Internal Border Queries)

Given $S[1..N]$ and $Q$ queries $(l, r)$ ($N, Q \le 2 \times 10^5$), find the **longest border** of $S[l..r]$—i.e., the maximum $k \in [1 .. r-l]$ such that $S[l .. l+k-1] = S[r-k+1 .. r]$.

Let us derive all four distinct structural methodologies enshrined in `[BJWC2018] Border 的四种求法` (authored by Jin Ce / 金策):

#### Method 1: SAM / Suffix Tree Link-Tree + Segment Tree Merging + Heavy-Light Decomposition ($O(N \log^2 N + Q \log^2 N)$)
A length $k = i - l + 1$ ($l \le i < r$) is a border of $S[l..r]$ iff the prefix $S[1..i]$ and the prefix $S[1..r]$ share a common suffix of length at least $i - l + 1$:
$$
\text{LCSuf}(S[1..i], S[1..r]) \ge i - l + 1 \iff i - \text{len}(\text{LCA}_{\text{SAM}}(\text{pos}(i), \text{pos}(r))) < l.
$$
Let $u_r = \text{pos}(r)$ be the SAM node of prefix $S[1..r]$. Walk the heavy-light decomposition (HLD) chains from $u_r$ up to the root of the SAM Link Tree. For each ancestor $w$ on the path from $u_r$ to the root:
- Case A ($i$ is in a light subtree of $w$, so $\text{LCA}(i, r) = w$ has fixed $\text{len}(w)$): We need the largest $i \in [l, r-1]$ in the $\text{endpos}$ set of $w$ such that $i - \text{len}(w) < l \iff i \le l + \text{len}(w) - 1$. That is simply a **predecessor query** for $\min(r-1, l + \text{len}(w) - 1)$ inside the merged $\text{endpos}$ Segment Tree of node $w$!
- Case B ($w = \text{LCA}(i, r)$ lies on the heavy chain, and $i$ enters from a light child of $w$): Pre-store for each light child index $i$ its value $v(i) = i - \text{len}(w)$ in a Segment Tree over the heavy chain; query the heavy chain segment for the largest $i < r$ with $v(i) < l$.

#### Method 2: SA Rank Neighborhood + Persistent Segment Tree + $\sqrt{N}$ Decomposition ($O((N+Q)\sqrt{N \log N})$ or $O(N \sqrt{N})$)
Split candidate border lengths $k$ at threshold $B = \sqrt{N}$:
- **Short Borders ($k \le B$)**: A border of length $k$ exists iff $S[l..l+k-1] = S[r-k+1..r] \iff \text{LCE}(l, r-k+1) \ge k$. Instead of checking all $k \le B$, observe that any $j = r-k+1$ with $\text{LCE}(l, j) \ge 1$ and small difference in SA rank is close to $\text{rk}[l]$, OR we can directly test $k$ via string hashing / SA rank window! Even simpler: for **Long Borders ($k > B$)**, the starting position $j = r-k+1$ of the suffix must satisfy $\text{LCE}(l, j) \ge k > B$. In the Suffix Array, all suffixes sharing an LCP $> B$ with $\text{suf}(l)$ form a contiguous SA interval $[L_B, R_B]$ around $\text{rk}[l]$. Wait: instead of $k > B$, use the dual split:
  - **Small SA-Rank Distance ($|\text{rk}[j] - \text{rk}[l]| \le B$)**: There are only $2B$ suffixes $j$ within SA-rank distance $B$ of $\text{rk}[l]$. Check each one in $O(1)$ if $j \in [l+1, r]$ and $\text{LCE}(l, j) \ge r - j + 1$.
  - **Large SA-Rank Distance ($|\text{rk}[j] - \text{rk}[l]| > B$)**: Since there are $> B$ suffixes between $\text{rk}[l]$ and $\text{rk}[j]$ in SA, and all of them share prefix $S[l .. l+k-1]$, the substring $S[l .. l+k-1]$ occurs $> B$ times in $S$, which implies if we instead split by **border length $k \le B$ vs. $k > B$**:
    - Check $k = 1 \dots B$ directly in $O(B)$ via $O(1)$ $\text{LCE}(l, r-k+1) \ge k$.
    - For $k > B$: the border $S[l..l+k-1]$ has length $> B$, so we only care about suffixes $j \in [l+1, r-B]$ inside the SA interval $[L, R]$ of $S[l..l+B-1]$ that satisfy $j + \text{LCE}(l, j) > r$. Because $\text{LCE}(l, j)$ is unimodal around $\text{rk}[l]$, or via $O(N/B)$ periodic steps, this bridges directly to Method 4!

#### Method 3: Offline 2D Sweep-Line over Periodic Runs (`Runs Theorem`, $O(N \log N + Q \log N)$)
Every border $S[l..l+k-1] = S[r-k+1..r]$ with $k \ge \lceil (r-l+1)/2 \rceil$ (a **long border**, $\ge$ half the substring length) implies that $S[l..r]$ has period $p = (r - l + 1) - k \le (r - l + 1)/2$. Therefore, $S[l..r]$ is a tandem repeat of period $p$ and length $\ge 2p$, so it is contained inside a **unique maximal periodic run** $R = [l_R, r_R, p]$ of $S$ (`Wave 1B`)!
- Thus all borders of length $\ge |S[l..r]|/2$ can be found by checking the runs covering $[l, r]$.

#### Method 4: Kociumaka's $O(\log N)$ Dyadic IPM Decomposition (Pure $O(N \log N + Q \log N)$ Online!)
Partition all possible border lengths $k \in [1 .. r-l]$ into $\lceil \log_2(r-l+1) \rceil$ dyadic intervals $I_m = [2^m, \min(r-l, 2^{m+1}-1)]$ for $m = 0, 1, \dots, \lfloor \log_2(r-l) \rfloor$:
- A border of length $k \in [2^m, 2^{m+1}-1]$ must share the prefix $P_m = S[l .. l + 2^m - 1]$ of length $2^m$, AND share the suffix $Q_m = S[r - 2^m + 1 .. r]$ of length $2^m$!
- More precisely:
  1. Look for occurrences of the prefix $P_m = S[l .. l + 2^m - 1]$ inside the tail window $S[r - 2^{m+1} + 2 .. r]$. This tail window has length $2^{m+1} - 1 < 2 |P_m|$!
  2. By **Theorem 70.1 (The IPM Arithmetic Progression Lemma)**, all occurrences of $P_m$ inside $S[r - 2^{m+1} + 2 .. r]$ can be found by querying a **Persistent Segment Tree over SA** (in the SA interval of $P_m$, find the minimum, second minimum, and maximum starting positions in $[r - 2^{m+1} + 2, r - 2^m + 1]$)—at most 3 Persistent Segment Tree queries per scale $m$!
  3. Symmetrically, all occurrences of the suffix $Q_m = S[r - 2^m + 1 .. r]$ inside the head window $S[l .. l + 2^{m+1} - 2]$ form a single arithmetic progression of starting positions!
  4. A shift $k \in [2^m, 2^{m+1}-1]$ is a valid border of $S[l..r]$ **if and only if** $r - k + 1$ is an occurrence of $P_m$ in the tail window **and** $l + k - 2^m$ is an occurrence of $Q_m$ in the head window!
  5. Intersecting two 1D arithmetic progressions (after normalizing to the border length $k$) in $O(1)$ time (since if both have size $\ge 3$, they have the **exact same common difference** $d = \text{per}(P_m) = \text{per}(Q_m)$ whenever their overlap is non-empty!) yields all borders in $[2^m, 2^{m+1}-1]$ as a single arithmetic progression in $O(\log N)$ time per scale $m$!

```
Substring S[l..r], testing border length k in [2^m, 2^{m+1}-1]:

  S[l .................... l+k-1]        (candidate prefix border of length k)
  |-- P_m (2^m) --|
          |---- Q_m (2^m) ----|  <-- must occur in head window S[l .. l+2^{m+1}-2]

  S[r-k+1 .................... r]        (candidate suffix border of length k)
  |-- P_m (2^m) --|              <-- must occur in tail window S[r-2^{m+1}+2 .. r]
          |---- Q_m (2^m) ----|
```

---

### 70.4 Bi-Directional 2D Orthogonal Range Queries on $(\text{SA}, \text{SA}^R)$

Suppose we are given a string $S[1..N]$ and a query asks for split occurrences $P = P_1 \cdot P_2$ (or $P_1 \cdot ? \cdot P_2$ with a wildcard at position $k$), or asks how many split points $i$ have $S[1..i]$ ending with $P_1$ and $S[i+1..N]$ starting with $P_2$:
- $S[1..i]$ ends with $P_1 \iff$ in the Suffix Array $\text{SA}^R$ of the reversed string $S^R$, $\text{rk}^R[N - i + 1] \in [L^R(P_1^R), R^R(P_1^R)]$.
- $S[i+1..N]$ starts with $P_2 \iff$ in the Suffix Array $\text{SA}$ of $S$, $\text{rk}[i+1] \in [L(P_2), R(P_2)]$.
- By creating a 2D point $(x_i, y_i) = (\text{rk}^R[N - i + 1], \text{rk}[i + 1])$ for each split index $i \in [1..N-1]$, every bi-directional prefix/suffix constraint becomes a **2D orthogonal rectangle query** $[L^R, R^R] \times [L, R]$, solvable in $O(\log N)$ time per query via a **Wavelet Matrix** or **Persistent Segment Tree**!

---

### 70.5 Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Allowing the Trivial Full-String Border $k = r - l + 1$**:
   - By definition, a border of $S[l..r]$ must be a **proper** prefix/suffix ($1 \le k \le r - l$). In Method 1 (SAM + Segment Tree Merge), querying the $\text{endpos}$ set in $[l, r]$ instead of $[l, r-1]$ will always return $i = r$, yielding the trivial length $r - l + 1$.
2. **Intersection of APs with Different Periods in Dyadic IPM**:
   - When intersecting the AP of $P_m$-occurrences in the tail window and the AP of $Q_m$-occurrences in the head window, it is tempting to assume both APs always have the same common difference $d$. That is only true when both APs have **at least 2 elements that overlap**! If one AP has size $\le 2$, you must explicitly test its $\le 2$ individual elements against the other AP rather than assuming equal step sizes.

---

## Iteration 71: Bi-Directional / Double-Ended Suffix Structures — Suffix Balanced Trees (`后缀平衡树`), SCDAWG & Online Prepend/Append Automata

### 71.1 The Diagnostic Signal: Dynamic Prepend/Append & Bi-Directional Context Equivalence

Standard Suffix Arrays are completely static, while Ukkonen's Suffix Tree and Blumer's Suffix Automaton (SAM) are **strictly uni-directional**: they are designed to append characters to the **right** end of $S$ in $O(1)$ amortized time. Why does prepending a character $c$ to the **left** end of $S$ ($S \leftarrow c \cdot S$) break a standard SAM?
- **Appending $c$ to the right** adds a new prefix $S \cdot c$, creating $O(1)$ new $\text{endpos}$ equivalence classes (at most 2 new SAM states: the new full-string state and at most one clone state along the suffix link chain).
- **Prepending $c$ to the left** adds a single new **suffix** $c \cdot S$ to the string! In the Suffix Tree of $S$ (which is the Link Tree of the SAM of $S^R$), adding a single new suffix $c \cdot S$ splits at most **one** edge in the Suffix Tree (creating one new leaf and at most one new internal branching node), **provided we know where $c \cdot S$ ranks among existing suffixes or where its longest repeated prefix branches**!
- However, in the **forward SAM** of $S$, prepending $c$ can modify the $\text{endpos}$ sets of every prefix of $c \cdot S$, while in a dynamic problem (`[JSOI2016] 独特的树叶` / dynamic suffix rank queries with front/back insertion and deletion, `[BZOJ 3682] Phorni`, `[BZOJ 4768] wxh loves substring`), we must maintain the **online sorted order of all suffixes** under dynamic left-prepend (and left-delete) operations, OR maintain both forward and backward transitions simultaneously (Symmetric Compact DAWG / Affix Automaton).

---

### 71.2 The Combinatorial Word Invariant: Tag-Based $O(1)$ Suffix Comparison & Bi-Directional Context Equivalence

#### 1. Suffix Balanced Tree (`后缀平衡树`) & Dietz–Sleator Order-Maintenance Tags

Suppose we maintain a string $S$ under **left-prepending** ($S \leftarrow c \cdot S$, or equivalently right-appending if we reverse the string so each step adds a new prefix $P_i = P_{i-1} \cdot c_i$ and we sort reversed prefixes). Let $\text{suf}(i)$ be the already-inserted suffixes for $i = 1, \dots, n-1$, stored in a Binary Search Tree (BST) in exact lexicographical order.
Now we prepend a new character $c$ at the front to form the new suffix $\text{suf}(n) = c \cdot \text{suf}(n-1)$.
How can we insert $\text{suf}(n)$ into the BST in $O(\log n)$ time?
When walking down the BST from the root, at each visited BST node $u$ (representing some existing suffix $\text{suf}(u) = S[u] \cdot \text{suf}(u-1)$), we must compare $\text{suf}(n)$ against $\text{suf}(u)$:
$$
\text{suf}(n) \lessgtr \text{suf}(u) \iff \big(c,\, \text{suf}(n-1)\big) \lessgtr \big(S[u],\, \text{suf}(u-1)\big).
$$
- If $c \ne S[u]$, the comparison is decided immediately in $O(1)$ by $c \lessgtr S[u]$!
- If $c = S[u]$, the comparison reduces to comparing two **already-existing suffixes**: $\text{suf}(n-1) \lessgtr \text{suf}(u-1)$!

How do we compare two existing BST nodes $\text{suf}(n-1)$ and $\text{suf}(u-1)$ in **$O(1)$ time** instead of $O(\log n)$?
> **Theorem 71.1 (Weight-Balanced BST Dyadic Tag Invariant / `后缀平衡树`)**:
> Maintain the suffixes in a **Weight-Balanced Tree (Scapegoat Tree / $\alpha$-Weight-Balanced Tree)** or Treap where every node $x$ is assigned a real/64-bit integer interval $[L_x, R_x] \subseteq [0, 2^{62}]$ and a midpoint tag:
> $$
> \text{tag}[x] = \frac{L_x + R_x}{2},
> $$
> with left child assigned $[L_x, \text{tag}[x]]$ and right child assigned $[\text{tag}[x], R_x]$.
> Because the tree height is strictly bounded by $O(\log_{1/\alpha} n)$ (for $\alpha \in [0.7, 0.75]$, depth $< 55$ for $n \le 10^6$), the 64-bit integer tags never underflow, and for any two existing suffixes $i, j$:
> $$
> \text{suf}(i) < \text{suf}(j) \iff \text{tag}[i] < \text{tag}[j] \quad \text{in } O(1) \text{ time!}
> $$
> Whenever a subtree of size $s$ is rebuilt (or rotated in a Treap), recomputing the tags of the $s$ nodes in the subtree takes $O(s)$ amortized time ($O(\log n)$ per insertion), yielding **$O(\log n)$ worst-case/amortized time per prepend (or delete)**!

#### 2. Maintaining Dynamic `height` / LCP in a Suffix Balanced Tree
When $\text{suf}(n)$ is inserted into the Suffix Balanced Tree between its BST predecessor $u^-$ and successor $u^+$:
- How do we compute $\text{LCP}(\text{suf}(n), u^-)$ and $\text{LCP}(\text{suf}(n), u^+)$?
  - Either use $O(\log n)$ binary search + polynomial hash (if hashing is collision-safe), or
  - Use **pure combinatorial LCP bootstrapping**:
    - If $S[n] \ne S[u^-]$, then $\text{LCP}(\text{suf}(n), u^-) = 0$.
    - If $S[n] = S[u^-]$, then $\text{LCP}(\text{suf}(n), u^-) = 1 + \text{LCP}(\text{suf}(n-1), u^- - 1)$, where $\text{LCP}(\text{suf}(n-1), u^- - 1)$ is a range-minimum query between two existing nodes in the BST! Because the BST itself maintains subtree minimums of adjacent `height` values, any $\text{LCP}(x, y)$ between two existing suffixes is answered in $O(\log n)$ time by querying the BST interval between $x$ and $y$—requiring **zero hashing and zero RMQ tables**!
- Consequently, the **number of distinct substrings** of $S$ under dynamic front-insertions and front-deletions is maintained online in $O(\log n)$ per operation as:
  $$
  \Delta \text{Distinct}(n) = |S[n..]| - \max\big(\text{LCP}(\text{suf}(n), u^-),\, \text{LCP}(\text{suf}(n), u^+)\big).
  $$

#### 3. Symmetric Compact DAWG (SCDAWG) / Affix Automaton (Blumer, Inenaga et al.)

What if a problem allows **both** left-prepend ($S \leftarrow c \cdot S$) and right-append ($S \leftarrow S \cdot c$) dynamically online?
Let $\text{endpos}(w)$ be the set of right endpoints of occurrences of $w$ in $S$, and $\text{startpos}(w)$ be the set of left endpoints of occurrences of $w$ in $S$.
- In the forward SAM, states are equivalence classes of $\equiv_L$ (same $\text{endpos}$, closed under taking suffixes up to the shortest length; each equivalence class is an interval of suffixes of its longest member $\vec{w}$, where $\vec{w}$ is the **left-extension closure** of $w$).
- In the reverse SAM (SAM of $S^R$, or Suffix Tree of $S$), states are equivalence classes of $\equiv_R$ (same $\text{startpos}$, corresponding to **right-extension closure** $\overleftarrow{w}$).
- In the **Symmetric Compact DAWG (SCDAWG)** (Inenaga et al. 2001–2005), each canonical vertex represents a **bi-maximal factor (prime factor / closed substring)** $\overleftrightarrow{w}$ that cannot be extended either to the left or to the right without losing occurrences in $S$:
  $$
  \forall c \in \Sigma, \quad \text{occ}(c \cdot \overleftrightarrow{w}) < \text{occ}(\overleftrightarrow{w}) \quad \text{and} \quad \text{occ}(\overleftrightarrow{w} \cdot c) < \text{occ}(\overleftrightarrow{w}).
  $$

```
                   Right-extension (forward SAM transitions)
              w  -------------------------------------------->  w * c
              |                                                   |
Left-ext      |                                                   |  Suffix / Prefix
(reverse SAM  v                                                   v  links
 transitions) a * w -----------------------------------------> a * w * c
```

> **Theorem 71.2 (Linear Bound on Bi-Maximal Nodes in SCDAWG)**:
> Every bi-maximal substring $\overleftrightarrow{w}$ of $S$ is simultaneously the longest string in its forward SAM state and the longest string in its reverse SAM state (hence an explicit internal node of both the Suffix Tree of $S$ and the Suffix Tree of $S^R$). Therefore, a string of length $n$ has at most **$n - 1$ internal bi-maximal nodes** and $O(n)$ forward and backward compact transitions, and the SCDAWG supports **online left-prepend and right-append** in $O(n \log |\Sigma|)$ total time!

---

### 71.3 The Reverse-Engineering Scratchpad: Practical Competitive Programming Compilations for Bi-Directional Suffix Queries

In contest settings, implementing a full pointer-based SCDAWG is rarely needed because one of two cleaner reductions applies:

1. **Reduction 1: Suffix Balanced Tree (`后缀平衡树`) + Tree Path / Persistent Queries (`[BZOJ 3682] Phorni`, `[BZOJ 4768]`)**:
   - When characters are appended at one end (or tree-branched across versions) and queries ask for the lexicographical rank of a new suffix or the $k$-th lexicographically smallest suffix in a range, flip the orientation so additions become **left-prepends** and maintain the Suffix Balanced Tree with 64-bit `double` or `uint64_t` tags.
2. **Reduction 2: Offline Deque Construction + SAM/SA on the Full Trajectory**:
   - If the sequence of left-prepends and right-appends is known (or queries do not depend on encrypted answers that change which character is prepended/appended), the active string at every time $t$ is a **contiguous substring $S[l_t .. r_t]$ of the final double-ended string $S[1..N]$**!
   - Then every query on the dynamic deque string at time $t$ reduces immediately to an **Internal Pattern Matching (IPM) / Substring Range Query on the static final string $S[1..N]$** (`Iter 70` or `Wave 2A` SAM + Segment Tree Merge / LCT)!
3. **Reduction 3: Online Double-Ended Distinct Substrings via Dual-SAM + LCT / Suffix Balanced Tree**:
   - If online encryption forces true online left-prepend and right-append:
     - Maintain a **Suffix Balanced Tree** for left-prepends AND a **Prefix Balanced Tree** (Suffix Balanced Tree on $S^R$) for right-appends, or use the **Online Double-Ended Suffix Tree** (Inenaga / Breslauer–Italiano), where appending at the right uses Ukkonen's active point and prepending at the left inserts a single suffix via the Prefix Balanced Tree!

---

### 71.4 Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Floating-Point Tag Precision Loss in Unbalanced BSTs (`后缀平衡树`)**:
   - If you use `double` (53-bit mantissa) for `tag[u] = (L + R) / 2` in a Treap without rebuilding or with an unlucky random seed where depth exceeds $53$, two distinct nodes receive `tag[u] == tag[v]`, causing **catastrophic BST comparison failure**! Always use a **Scapegoat Tree** with $\alpha = 0.75$ (strictly bounding depth $\le \log_{4/3}(10^6) \approx 48$) and 64-bit unsigned integer tags $[0, 2^{62}]$.
2. **Confusing Prefix Append with Suffix Prepend in `后缀平衡树`**:
   - The $O(1)$ tag comparison $\text{suf}(n) \lessgtr \text{suf}(u) \iff (S[n], \text{tag}[n-1]) \lessgtr (S[u], \text{tag}[u-1])$ **only works when adding a character at the front of the compared strings**! If the problem appends characters to the **back** of $S$ ($S \leftarrow S \cdot c$) and asks to compare **suffixes** of $S$, appending $c$ to the back changes **every** existing suffix simultaneously! To use a Suffix Balanced Tree when appending to the back, you must maintain the sorted order of **reversed prefixes** $S[1..i]^R$ (since appending $c$ to $S[1..i-1]$ prepends $c$ to $S[1..i-1]^R$).

---

## Iteration 72: Multilingual Problem Mining (`[EN]`/`[ZH]`/`[JA]`), 4-Tier Difficulty Ladder & Quarantine Ledger

### 72.1 Quarantine Table (`R-2B-01` to `R-2B-08`) — Excluded Template & Verification Problems

Per `AGENTS.md` and `PLAN.md`, bare library verification problems are quarantined from the pedagogical ladder:

| Quarantine ID | Judge & Problem | Reason for Quarantine |
| :--- | :--- | :--- |
| **`R-2B-01`** | **Library Checker — Suffix Array** | Pure SA construction verification ($N = 5 \times 10^5$); zero modeling beyond SA-IS / doubling template. |
| **`R-2B-02`** | **Library Checker — Number of Substrings** | Pure formula $\binom{N+1}{2} - \sum_{k=2}^N H[k]$ verification. |
| **`R-2B-03`** | **Luogu P3809 — 【模板】后缀排序** | Standard Chinese template verification for Suffix Array ($N = 10^6$). |
| **`R-2B-04`** | **UOJ #35 — 后缀排序** | Standard SA + `height` array template verification. |
| **`R-2B-05`** | **POJ 2774 — Long Long Message** | Bare two-string LCS via $S_1 \texttt{\#} S_2$ SA + `height` scan. |
| **`R-2B-06`** | **POJ 1743 — Musical Theme** | Bare binary search on answer + `height` block min/max check. |
| **`R-2B-07`** | **LOJ #111 — 后缀排序** | Bare Suffix Array template verification. |
| **`R-2B-08`** | **AtCoder Practice2 I — Number of Substrings** | Bare ACL `suffix_array` + `lcp_array` template verification. |

---

### 72.2 Curated Non-Template Problem Corpus (30 Problems Across 4 Difficulty Tiers)

We organize **30 non-template problems** mined across `[EN]` (Codeforces, ICPC, POI, SPOJ), `[ZH]` (NOI, AHOI, BJWC, HEOI/TJOI, SDOI, ZJOI, JSOI, BZOJ, Luogu, UOJ, QOJ), and `[JA]` (AtCoder AGC/ARC/ABC, JOI) into a 4-Tier Difficulty Ladder.

---

#### Tier 1: Stepping Stone (8 Problems — Core Structural Reductions on `height` Cartesian Trees & Basic IPM)

##### 1. `[ZH]` `[AHOI2013] 差异` (Luogu P4248)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), compute $\sum_{1 \le i < j \le N} \big(|\text{suf}(i)| + |\text{suf}(j)| - 2\,\text{LCP}(\text{suf}(i), \text{suf}(j))\big)$.
- **4-Step Analysis**:
  1. *Signal*: Naive $O(N^2)$ pair enumeration TLEs; sum separates into $\frac{N(N-1)(N+1)}{2} - 2 \sum_{1 \le x < y \le N} \min_{x < k \le y} H[k]$.
  2. *Invariant*: By Theorem 69.1, each $H[k]$ is the unique tie-broken minimum on its Cartesian-tree rectangle $[L_k, R_k]$.
  3. *Compilation*: Run a single monotonic stack pass over $H[2..N]$ with strict `<` on the left and `<=` on the right; subtract $2 \sum_{k=2}^N H[k] (k - L_k + 1)(R_k - k + 1)$.
  4. *Pitfall*: Using strict `<` on both sides drops pairs when $H$ has equal entries; requires 64-bit integer arithmetic (`__int128` or `long long`).

##### 2. `[EN]` `CF 873F — Forbidden Indices`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and a binary mask $B[1..N]$ marking forbidden starting indices (or ending indices after reversal), maximize $|t| \cdot \text{occ}_{\text{valid}}(t)$ over all substrings $t$.
- **4-Step Analysis**:
  1. *Signal*: Substring occurrences must exclude forbidden indices; checking every substring takes $O(N^2)$.
  2. *Invariant*: Every valid equivalence class of substrings with $>1$ occurrence is a contiguous interval $[L_k, R_k]$ in SA with string depth $H[k]$, containing $\text{pref\_valid}[R_k] - \text{pref\_valid}[L_k - 1]$ valid suffixes.
  3. *Compilation*: Build SA + $H$, compute prefix sums of $(1 - B[\text{SA}[i]])$ over SA order, and evaluate $\max_k H[k] \cdot (\text{cnt}(R_k) - \text{cnt}(L_k - 1))$ via Cartesian tree / monotonic stack, plus the single-occurrence case $\max_{B[i]=0} (N - i + 1)$.
  4. *Pitfall*: Forgetting the single-occurrence leaf case ($\text{occ}_{\text{valid}}(t) = 1$) when the longest valid suffix never shares an LCP with another valid suffix!

##### 3. `[EN]` `CF 802I — Fake News (hard)`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), compute $\sum_{t \in \text{Sub}(S)} \text{occ}(t)^2$.
- **4-Step Analysis**:
  1. *Signal*: Squaring $\text{occ}(t)$ means we cannot simply count pairs of suffixes independently without grouping identical substrings by length intervals.
  2. *Invariant*: In the Cartesian tree of $H[2..N]$, node $u$ with interval $[L_u, R_u]$, height $h_u$, and parent height $h_{p(u)}$ represents exactly $h_u - h_{p(u)}$ distinct substrings, each occurring $R_u - L_u + 1$ times.
  3. *Compilation*: Build the Min-Cartesian tree on $H[2..N]$ (plus $N$ leaves of height $N - \text{SA}[k] + 1$); sum $(h_u - h_{p(u)}) \cdot \text{sz}(u)^2$ over all nodes $u$.
  4. *Pitfall*: Omitting leaf nodes (where $\text{sz}(u) = 1$ and $h_u = N - \text{SA}[k] + 1$) misses all substrings occurring once.

##### 4. `[ZH]` `[NOI2015] 品酒大会` (Luogu P2178 / UOJ #131)
- **Statement & Constraints**: Given $S[1..N]$ and integer weights $a_1, \dots, a_N \in [-10^9, 10^9]$ ($N \le 3 \times 10^5$), for every $r \in [0..N-1]$, find (1) the number of pairs $(i, j)$ with $\text{LCP}(i, j) \ge r$, and (2) the maximum product $a_i a_j$ among such pairs.
- **4-Step Analysis**:
  1. *Signal*: Threshold $r$ varies over all $[0..N-1]$ and weights $a_i$ can be negative, so monotonic stack rectangles alone don't easily track component-wide min/max products at every threshold.
  2. *Invariant*: Decreasing threshold $r$ from $N-1$ down to $0$ corresponds to Kruskal DSU merging of adjacent SA positions $k-1$ and $k$ when $H[k] = r$.
  3. *Compilation*: Sort edges $H[k]$ descending; maintain DSU with $\text{sz}, \max_1, \min_1$; on uniting $U, V$ at $r = H[k]$, add $\text{sz}[U]\text{sz}[V]$ to `cnt[r]` and update `ans[r]` with $\max(\max_1[U]\max_1[V], \min_1[U]\min_1[V])$; take suffix sums/maxima from $N-1 \to 0$.
  4. *Pitfall*: Failing to track $\min_1$ misses the product of two negative numbers; initializing `ans[r] = 0` instead of $-\infty$ corrupts negative-only maximums.

##### 5. `[ZH]` `[JSOI2007] 字符加密` (Luogu P4051)
- **Statement & Constraints**: Given a string $S$ ($N \le 10^5$), sort all $N$ cyclic shifts of $S$ and output the last character of each sorted cyclic shift (the Burrows–Wheeler Transform $L$-column).
- **4-Step Analysis**:
  1. *Signal*: Suffixes must wrap around the end of $S$ cyclically.
  2. *Invariant*: Concatenating $S' = S \cdot S[1..N-1] \cdot \texttt{\$}$ turns cyclic shift comparison of length $N$ into suffix comparison on $S'$ provided identical cyclic shifts (when $S$ is periodic) preserve relative index order.
  3. *Compilation*: Run SA-IS on $S \cdot S[1..N-1] \cdot \texttt{\$}$ and filter $\text{SA}[k] \le N$.
  4. *Pitfall*: Appending only $S$ without a sentinel allows suffixes starting at $i < j$ with identical length-$N$ cyclic shifts to be inverted if $S[N]$ is larger than the next character.

##### 6. `[ZH]` `[HAOI2016] 找相同字符` (Luogu P3181)
- **Statement & Constraints**: Given two strings $S_1, S_2$ ($|S_1|, |S_2| \le 2 \times 10^5$), count the number of equal substring pairs $(S_1[l_1..r_1], S_2[l_2..r_2])$ with $S_1[l_1..r_1] = S_2[l_2..r_2]$.
- **4-Step Analysis**:
  1. *Signal*: Cross-string pairwise LCP sum $\sum_{i \in S_1} \sum_{j \in S_2} \text{LCP}(\text{suf}_1(i), \text{suf}_2(j))$.
  2. *Invariant*: By inclusion-exclusion, $\text{Cross}(S_1, S_2) = \text{All}(S_1 \texttt{\#} S_2) - \text{All}(S_1) - \text{All}(S_2)$, or directly $\sum_{\text{Cartesian node } u} (h_u - h_{p(u)}) \cdot \text{cnt}_1(u) \cdot \text{cnt}_2(u)$.
  3. *Compilation*: Build SA + $H$ on $S_1 \texttt{\#} S_2$ and evaluate on the Cartesian tree of $H$.
  4. *Pitfall*: Letting $\text{LCP}$ cross the separator `#` if the separator character already appears in $S_1$ or $S_2$.

##### 7. `[EN]` `CF 123D — String`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), compute $\sum_{t \in \text{Sub}(S)} \frac{\text{occ}(t)(\text{occ}(t)+1)}{2}$.
- **4-Step Analysis**:
  1. *Signal*: Identical to `CF 802I` with $g(|t|, k) = k(k+1)/2$, or notice $\sum_{t} \binom{\text{occ}(t)+1}{2} = \binom{N+1}{2} + \sum_{1 \le i < j \le N} \text{LCP}(i, j)$!
  2. *Invariant*: Choosing 2 occurrences of the same substring $t$ of length $\ell$ is in bijection with choosing two suffixes $(i, j)$ with $\text{LCP}(i, j) \ge \ell$.
  3. *Compilation*: Compute $\frac{N(N+1)}{2} + \sum_{k=2}^N H[k](k - L_k + 1)(R_k - k + 1)$ in $O(N)$.
  4. *Pitfall*: Off-by-one on single occurrences ($\binom{1+1}{2} = 1$, which sums to $\binom{N+1}{2}$ over all substrings $(l, r)$).

##### 8. `[JA]` `AtCoder ABC 272 F — Two Strings`
- **Statement & Constraints**: Given $S, T$ of length $N \le 2 \times 10^5$, count pairs $(i, j) \in [0..N-1]^2$ such that cyclic shift $S^{(i)} \le T^{(j)}$ lexicographically.
- **4-Step Analysis**:
  1. *Signal*: Comparing all $N^2$ pairs of cyclic shifts requires global cyclic rank ordering with exact tie-breaking when $S^{(i)} = T^{(j)}$.
  2. *Invariant*: In the concatenation $U = S \cdot S \cdot \texttt{a} \cdot T \cdot T \cdot \texttt{z}$ (where $\texttt{a} < \Sigma < \texttt{z}$), for any $i, j \in [1..N]$, $\text{suf}_U(i) < \text{suf}_U(2N+1+j) \iff S^{(i)} \le T^{(j)}$!
  3. *Compilation*: Build SA-IS on $U$ of length $4N+2$ and count inversion pairs between $i \in [1..N]$ and $j \in [2N+2..3N+1]$ in linear scan.
  4. *Pitfall*: If $S^{(i)} = T^{(j)}$, the characters after length $N$ in $S \cdot S$ and $T \cdot T$ are still equal up to length $2N$! Placing $\texttt{a}$ after $S \cdot S$ and $\texttt{z}$ after $T \cdot T$ guarantees that at offset $\le 2N$, $S^{(i)}$ breaks ties strictly smaller than $T^{(j)}$.

---

#### Tier 2: Intermediate (8 Problems — Virtual Suffix Trees `后缀树虚树`, Substring Rank & Concatenation IPM)

##### 9. `[EN]` `CF 1073G — Yet Another LCP Problem`
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ queries ($N, Q \le 2 \times 10^5$, $\sum (|A_q| + |B_q|) \le 2 \times 10^5$), compute $\sum_{i \in A_q} \sum_{j \in B_q} \text{LCP}(\text{suf}(i), \text{suf}(j))$.
- **4-Step Analysis**:
  1. *Signal*: Query subsets $A_q, B_q$ vary dynamically per query, with $\sum (|A_q| + |B_q|) = O(N)$, demanding an $O(k \log k)$ query engine where $k = |A_q| + |B_q|$.
  2. *Invariant*: Sorting the $k$ query suffixes by $\text{rk}[i]$ and taking adjacent RMQs on $H$ compresses the induced Suffix Tree into a Virtual Suffix Tree (`后缀树虚树`) of size $\le 2k-1$ (or directly a weighted monotonic stack over the $k-1$ adjacent interval minimums).
  3. *Compilation*: Sort $A_q \cup B_q$ by SA rank; compute adjacent LCPs $h_r = \text{RMQ}_H(\text{rk}[p_r]+1 .. \text{rk}[p_{r+1}])$; run a monotonic stack over $h_1, \dots, h_{k-1}$ accumulating $\text{cnt}_A \cdot \text{cnt}_B \cdot h_r$ (plus $N - i + 1$ when $i \in A_q \cap B_q$).
  4. *Pitfall*: Forgetting $i \in A_q \cap B_q$ (same suffix in both sets, where $\text{LCP}(i, i) = N - i + 1$ cannot be read from $H$).

##### 10. `[ZH]` `[HEOI2016 / TJOI2016] 字符串` (Luogu P4094)
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ queries $(a, b, c, d)$ ($N, Q \le 10^5$), find $\max_{l=c}^{d} \min\big(d - l + 1,\, \text{LCP}(\text{suf}(l), S[a..b])\big)$—the longest prefix of $S[c..d]$'s suffixes that is a substring of $S[c..d]$ and a prefix of $S[a..b]$.
- **4-Step Analysis**:
  1. *Signal*: A prefix of $S[a..b]$ of length $k$ occurs inside $S[c..d]$ iff there is a starting index $l \in [c, d - k + 1]$ with $\text{LCE}(a, l) \ge k$.
  2. *Invariant*: $\text{LCE}(a, l) \ge k$ holds iff $\text{rk}[l]$ lies in the contiguous SA interval $[L(a, k), R(a, k)]$ around $\text{rk}[a]$ where $\min H \ge k$. Moreover, this predicate is monotonic in $k$!
  3. *Compilation*: Binary search on $k \in [1 .. \min(b-a+1, d-c+1)]$. For a candidate $k$, find $[L(a, k), R(a, k)]$ via binary search on the RMQ table of $H$, then check if the Persistent Segment Tree over SA contains any starting index $l \in [c, d - k + 1]$ inside SA range $[L(a, k), R(a, k)]$. Time: $O(Q \log^2 N)$.
  4. *Pitfall*: Checking $l \in [c, d]$ instead of $l \in [c, d - k + 1]$ allows the match to overflow past $d$!

##### 11. `[EN]` `CF 504E — Misha and LCP on Tree`
- **Statement & Constraints**: Given a tree of $N \le 3 \times 10^5$ nodes with a character on each node, and $Q \le 10^6$ queries asking for the LCP of the string on the simple path $(u_1 \to v_1)$ and the path $(u_2 \to v_2)$.
- **4-Step Analysis**:
  1. *Signal*: Each tree path decomposes via Heavy-Light Decomposition (HLD) into $O(\log N)$ contiguous segments of the Euler/HLD string $S$ (forward on going down, reversed on going up).
  2. *Invariant*: Concatenating the HLD heavy-chain string $S$ and its reversal $S^R$ turns every tree path $(u \to v)$ into a concatenation of $O(\log N)$ substrings of $S \cdot S^R$!
  3. *Compilation*: Build SA + $O(1)$ RMQ on $S \cdot S^R$ in $O(N)$. For each query, decompose both paths into $\le 2 \log_2 N$ intervals in $S \cdot S^R$ and run the Two-Pointer Concatenation LCE algorithm (`Iter 70.2`), advancing one interval per $O(1)$ LCE query. Total time: $O(N + Q \log N)$.
  4. *Pitfall*: With $Q = 10^6$, binary search + hash per segment ($O(Q \log^2 N)$) TLEs; $O(1)$ RMQ LCE with two-pointer piece exhaustion is mandatory.

##### 12. `[ZH]` `[SDOI2016] 生成魔咒` (Luogu P4070)
- **Statement & Constraints**: Characters are appended one by one ($N \le 10^5$, $|\Sigma| \le 10^9$); after each append, print the number of distinct substrings.
- **4-Step Analysis**:
  1. *Signal*: Online distinct substring count over a large alphabet $|\Sigma| \le 10^9$.
  2. *Invariant*: Reversing the string (or processing offline via SA on the reversed string $S^R$) turns each prefix append $S[1..i]$ into inserting a new suffix $\text{suf}_{S^R}(N - i + 1)$ into the Suffix Balanced Tree (or deleting suffixes in reverse order on static SA).
  3. *Compilation*: Either maintain a Suffix Balanced Tree online (adding $|S[1..i]| - \max(\text{LCP}(u, u^-), \text{LCP}(u, u^+))$), or offline build SA on $S^R$ and maintain active suffixes in a doubly linked list.
  4. *Pitfall*: Standard array-transition SAM MLEs when $|\Sigma| = 10^9$ unless transitions use hash/map or Suffix Balanced Tree / offline SA.

##### 13. `[EN]` `CF 616F — Expensive Strings`
- **Statement & Constraints**: Given $M$ strings $S_1, \dots, S_M$ ($\sum |S_i| \le 5 \times 10^5$) with costs $c_1, \dots, c_M \in [-10^7, 10^7]$, maximize $|t| \cdot \sum_{i=1}^M c_i \cdot \text{occ}_{S_i}(t)$ over all nonempty strings $t$.
- **4-Step Analysis**:
  1. *Signal*: Multi-string weighted occurrence sum times length $|t|$.
  2. *Invariant*: On the Generalized Suffix Array of $S_1 \texttt{\$_1} \dots S_M \texttt{\$_M}$ (with LCP capped at the remaining length of each individual string $S_i$), every multi-occurrence equivalence class is a Cartesian tree node $[L_k, R_k]$ with height $h_k = \min(H[k], \text{rem\_len})$.
  3. *Compilation*: Cap each suffix's max valid length at the distance to the end of its string $S_i$; compute prefix sums of $c_{\text{str}(\text{SA}[j])}$ over SA; run Cartesian tree / monotonic stack over capped $H[k]$, and check single-occurrence full suffixes of each $S_i$.
  4. *Pitfall*: Failing to cap $H[k]$ by the end of $S_i$ allows substrings to span across separators and falsely merge occurrences from adjacent strings.

##### 14. `[JA]` `AtCoder ARC 151 E — Keep Being Substring`
- **Statement & Constraints**: Given array $A[1..N]$ and two subsegments $X = A[l_1..r_1], Y = A[l_2..r_2]$ ($N \le 2 \times 10^5$), at each step you can either append/prepend an element to the current sequence or delete an end element, provided the current sequence is always a contiguous nonempty subarray of $A$. Find the minimum steps from $X$ to $Y$.
- **4-Step Analysis**:
  1. *Signal*: If $X$ and $Y$ share a common subarray of length $L = \text{LCS}(X, Y) \ge 1$, we can shrink $X$ to the common subarray of length $L$ and expand to $Y$ in $|X| + |Y| - 2L$ steps! If $\text{LCS}(X, Y) = 0$ (disjoint characters), we must walk on a graph of adjacent characters in $A$.
  2. *Invariant*: The Longest Common Substring of $X = A[l_1..r_1]$ and $Y = A[l_2..r_2]$ is $\max_{i \in [l_1..r_1], j \in [l_2..r_2]} \min(r_1 - i + 1, r_2 - j + 1, \text{LCE}_A(i, j))$, or found on the Suffix Array / SAM of $X \texttt{\#} Y$ in $O(|X| + |Y|)$ time!
  3. *Compilation*: Build SA + $H$ on $X \texttt{\#} Y$ to find $L = \text{LCS}(X, Y)$ in $O(|X| + |Y|)$. If $L > 0$, answer is $|X| + |Y| - 2L$; if $L = 0$, shrinks to length 1 and runs BFS on the adjacency graph of $A[k] \leftrightarrow A[k+1]$ in $O(N)$.
  4. *Pitfall*: Assuming $L = 0$ is impossible or forgetting that shrinking to an empty string is forbidden (`nonempty subarray`), which forces the length-1 character transition graph when $L = 0$.

##### 15. `[EN]` `CF 427D — Match & Catch`
- **Statement & Constraints**: Given $S_1, S_2$ ($N \le 5000$ or scalable to $5 \times 10^5$), find the shortest substring $t$ that occurs **uniquely** ($\text{occ}_{S_1}(t) = 1$ and $\text{occ}_{S_2}(t) = 1$) in both $S_1$ and $S_2$.
- **4-Step Analysis**:
  1. *Signal*: Exact occurrence count $= 1$ in both strings, minimizing length $|t|$.
  2. *Invariant*: In the Cartesian tree of $H$ on $S_1 \texttt{\#} S_2$, a node $u$ with interval $[L_u, R_u]$ has $\text{cnt}_1(u) = 1$ and $\text{cnt}_2(u) = 1$ iff $R_u - L_u + 1 = 2$ (an adjacent pair of suffixes $\text{SA}[k-1], \text{SA}[k]$ from different strings!) and its parent height $h_{p(u)} = \max(H[k-1], H[k+1])$ is strictly smaller than $H[k]$. The shortest valid substring in this equivalence class has length $h_{p(u)} + 1$!
  3. *Compilation*: Check every adjacent pair $(k-1, k)$ in SA from opposite strings: if $H[k] > \max(H[k-1], H[k+1])$, update answer with $\max(H[k-1], H[k+1]) + 1$.
  4. *Pitfall*: Taking $H[k]$ (the longest length in the class) instead of $\max(H[k-1], H[k+1]) + 1$ (the **shortest** length in the class!).

##### 16. `[ZH]` `[SCOI2012] 喵星球上的点名` (Luogu P2336)
- **Statement & Constraints**: Given $N$ cats (each with a first and last name string) and $M$ query patterns ($\sum \text{len} \le 10^5$), find (1) for each pattern, how many cats contain it in either name, and (2) for each cat, how many patterns it matched.
- **4-Step Analysis**:
  1. *Signal*: Multi-pattern substring containment with distinct-color (cat ID) counting in SA intervals and point-in-range reverse accumulation.
  2. *Invariant*: Each pattern $P_q$ corresponds to a contiguous SA interval $[L_q, R_q]$ in the Generalized SA of all cat names. Question (1) is the number of distinct cat IDs in $[L_q, R_q]$; Question (2) is the number of intervals $[L_q, R_q]$ covering at least one occurrence of cat $c$.
  3. *Compilation*: Sort intervals $[L_q, R_q]$ by right endpoint $R_q$ and sweep a Fenwick tree tracking the **last seen position** `last[c]` of each cat $c$: when `last[c]` moves from $p_{\text{old}} \to p_{\text{new}}$, any query interval $[L_q, R_q]$ with $p_{\text{old}} < L_q \le p_{\text{new}}$ and $R_q \ge p_{\text{new}}$ covers cat $c$ for the first time!
  4. *Pitfall*: A cat has **two** names, so both names receive the same color ID $c$.

---

#### Tier 3: Advanced (8 Problems — 2D Bi-Directional SA Range Queries, Suffix Balanced Trees `后缀平衡树`, DSU-on-Tree Dominant Pairs)

##### 17. `[ZH]` `[BZOJ 3682] Phorni`
- **Statement & Constraints**: Maintain a string $S$ online under character additions (encrypted queries!), and also maintain an array $P[1..M]$ of indices into $S$'s suffixes under single-element updates $P[x] \leftarrow v$ and range queries asking for the index $x \in [l, r]$ that minimizes the suffix $\text{suf}(P[x])$.
- **4-Step Analysis**:
  1. *Signal*: Encrypted online character insertions + $O(1)$ lexicographical comparison of dynamic suffixes inside a Segment Tree over $P[1..M]$.
  2. *Invariant*: Reversing the string orientation makes each character append a **left-prepend** of a new suffix $\text{suf}(n) = c \cdot \text{suf}(n-1)$. By Theorem 71.1, a **Suffix Balanced Tree (`后缀平衡树`)** maintains real/64-bit integer tags $\text{tag}[i]$ for all existing suffixes such that $\text{suf}(i) < \text{suf}(j) \iff \text{tag}[i] < \text{tag}[j]$ in $O(1)$ time!
  3. *Compilation*: Maintain a Scapegoat-based Suffix Balanced Tree with $\alpha = 0.75$ and 64-bit integer tags $[0, 2^{62}]$. Maintain a standard Segment Tree over $P[1..M]$ comparing two suffixes $P[x], P[y]$ in $O(1)$ via `tag[P[x]] < tag[P[y]]` (breaking ties by smaller index $x$).
  4. *Pitfall*: When a Scapegoat subtree is rebuilt, the integer tags of nodes inside that subtree change, but their **relative order** is invariant, so the Segment Tree over $P[1..M]$ never needs to be rebuilt—only queried using the current `tag` array!

##### 18. `[ZH]` `[JSOI2016] 独特的树叶` / Dynamic Front/Back Distinct Substrings & Suffix Balanced Tree (`[BZOJ 4768] wxh loves substring`)
- **Statement & Constraints**: Maintain a string $S$ online under encrypted front-prepend and front-delete operations ($Q \le 2 \times 10^5$), and query how many substrings of $S$ match a given query pattern $T$ (or query the total distinct substrings).
- **4-Step Analysis**:
  1. *Signal*: Online encrypted front-insertions AND front-deletions invalidate static SA and append-only SAM (which cannot delete characters cleanly if states are cloned).
  2. *Invariant*: Prepending $c$ adds a single suffix $\text{suf}(n)$ to the Suffix Balanced Tree; deleting the front character removes $\text{suf}(n)$ from the Suffix Balanced Tree! A pattern $T$ occurs as a prefix of $\text{suf}(u)$ iff $\text{suf}(u) \in [T, T \cdot \infty)$, which is a contiguous BST range query in the Suffix Balanced Tree!
  3. *Compilation*: Insert/lazy-delete $\text{suf}(n)$ in a Scapegoat Suffix Balanced Tree in $O(\log N)$ time. To count occurrences of pattern $T$, walk down the Suffix Balanced Tree comparing $T$ character-by-character against node $u$ in $O(|T| + \log N)$ time to find the rank of $T$ and $T \cdot \texttt{\{}$.
  4. *Pitfall*: Using true structural deletion in a Scapegoat tree can shift tags prematurely; use lazy deletion flags and rebuild when deleted count exceeds $(1-\alpha)\text{sz}$.

##### 19. `[EN]` `CF 1098F — Ж-function`
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ queries $(l, r)$ ($N, Q \le 2 \times 10^5$), compute $\sum_{i=l}^{r} \min\big(r - i + 1,\, \text{LCE}(l, i)\big)$—the sum of the Z-function of the substring $S[l..r]$!
- **4-Step Analysis**:
  1. *Signal*: For each query $(l, r)$, we sum $\min(r - i + 1, \text{LCE}(l, i))$ over $i \in [l, r]$. Notice this combines **SA / Suffix Tree LCA** ($\text{LCE}(l, i)$) with **2D linear constraints** ($i \in [l, r]$ and $i + \text{LCE}(l, i) - 1 \le r$ vs. $> r$).
  2. *Invariant*: On the Suffix Tree (Cartesian Tree of $H$ or SAM of $S^R$), $\text{LCE}(l, i) = \text{len}(\text{LCA}(l, i))$. Using **Heavy-Light Decomposition (HLD) / Centroid Decomposition on the Suffix Tree**, each query $(l, r)$ walks $O(\log N)$ ancestors $w$ of leaf $l$, where $\text{len}(w)$ is fixed on light subtrees, reducing the sum over $i \in [l, r]$ to two 2D range sum queries ($i \le r - \text{len}(w) + 1$ contributing $\text{len}(w)$, and $i > r - \text{len}(w) + 1$ contributing $r - i + 1$)!
  3. *Compilation*: Decompose the Suffix Tree via HLD or Centroid Decomposition; sweep over heavy chains and light subtrees with a Fenwick tree keyed by $i + \text{len}(w)$ in $O((N + Q) \log^2 N)$ time.
  4. *Pitfall*: When $i$ and $l$ diverge along a heavy edge (rather than at a light child of $w$), $\text{LCE}(l, i)$ depends on the shallower of the two heavy-chain positions ($\min(\text{len}(w_l), \text{len}(w_i))$), requiring two separate offline sweeps along each heavy chain (once for $w_i$ above $w_l$, once for $w_i$ below $w_l$).

##### 20. `[EN]` `ICPC WF 2019 — First of Her Name` (`GYM / WF 2019 D`)
- **Statement & Constraints**: Given a rooted tree of $N \le 10^6$ nodes where each node adds a character at the **front** of its parent's name, and $Q$ query strings ($\sum |P_q| \le 10^6$), count for each query $P_q$ how many tree nodes have a name starting with $P_q$.
- **4-Step Analysis**:
  1. *Signal*: Names are formed by walking **from node $u$ up to the root**, so every node $u$ has a unique successor $\text{parent}(u)$!
  2. *Invariant*: Sorting all $N$ upward tree paths is the **Tree Suffix Array** (`Iter 68.4`). Every query string $P_q$ is a prefix of a contiguous interval $[L_q, R_q]$ in the Tree Suffix Array!
  3. *Compilation*: Build the Tree Suffix Array by rank-pair doubling (or induced sorting on upward paths); for each query $P_q$, binary search the Tree SA in $O(|P_q| \log N)$ time by jumping along tree ancestors of $\text{SA}[m]$ (or character-by-character refined SA interval shrinking in $O(|P_q| \log N)$).
  4. *Pitfall*: Distinct tree nodes can have **identical** upward strings to the root! During Tree SA construction, ties must be given the **exact same rank** before the final enumeration, or binary search must find the full tie range.

##### 21. `[ZH]` `[NOI2016] 优秀的拆分` (Luogu P1117 / UOJ #219)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^4$, multi-test), count the number of quadruples $(i, j, k)$ such that $S[i..j] = AA$ and $S[j+1..k] = BB$ are both non-empty squares ($AABB$ decompositions).
- **4-Step Analysis**:
  1. *Signal*: Counting $AA$ ending at each $j$ ($\text{pre}[j]$) and $BB$ starting at each $j+1$ ($\text{suf}[j+1]$) in $O(N^2)$ TLEs; we need $O(N \log N)$ via harmonic-series LCE checkpoints!
  2. *Invariant*: Fix half-length $L \in [1 .. \lfloor N/2 \rfloor]$ and place checkpoints at multiples $p_m = m \cdot L$. Any square $AA$ of length $2L$ MUST cover **exactly two consecutive checkpoints** $p_m$ and $p_{m+1}$! Let $l_{\text{ext}} = \min(L, \text{LCSuf}(p_m, p_{m+1}))$ and $r_{\text{ext}} = \min(L, \text{LCE}(p_m, p_{m+1}))$. If $l_{\text{ext}} + r_{\text{ext}} - 1 \ge L$, then every starting position in $[p_m - l_{\text{ext}} + 1,\, p_m + r_{\text{ext}} - L]$ begins a square of length $2L$, which is a contiguous range update on $\text{suf}$ and $\text{pre}$!
  3. *Compilation*: Build SA + $O(1)$ RMQ on $S$ (for $\text{LCE}$) and on $S^R$ (for $\text{LCSuf}$). Loop $L = 1 \dots N/2$ and $m = 1 \dots \lfloor N/L \rfloor - 1$ ($\sum N/L = O(N \log N)$ steps), applying difference-array range increments to $\text{pre}$ and $\text{suf}$.
  4. *Pitfall*: Without capping $l_{\text{ext}} \le L$ and $r_{\text{ext}} \le L$, a periodic run of length $\ge 3L$ will be counted by multiple adjacent checkpoint pairs $(p_m, p_{m+1})$ and $(p_{m+1}, p_{m+2})$! Specifically, cap the left extension at $l_{\text{ext}} \le L$ and right extension at $r_{\text{ext}} \le L - 1$ (including $p_m$ on one side only) so each starting position belongs to a unique checkpoint $p_m$.

##### 22. `[EN]` `POI 2010 — Beads (Korale)` / `SPOJ SUBLEX` / `[ZJOI2015] 诸神眷顾的幻想乡`
- **Statement & Constraints**: Given a string $S[1..N]$ and $Q$ queries for the $k$-th lexicographically smallest distinct substring (or substring with multiplicity, `[TJOI2015] 弦论` Luogu P3975, $N \le 5 \times 10^5, k \le 10^{18}$), output its endpoints $(l, r)$ in $O(\log N)$ per query.
- **4-Step Analysis**:
  1. *Signal*: Outputting the string itself takes $O(N)$ per query if $Q$ is large; IPM demands returning $(l, r)$ in $O(\log N)$.
  2. *Invariant*: In SA order, suffix $\text{SA}[i]$ contributes $(N - \text{SA}[i] + 1) - H[i]$ new distinct substrings of lengths $H[i]+1, \dots, N - \text{SA}[i] + 1$.
  3. *Compilation*: Compute prefix sums of $(N - \text{SA}[i] + 1 - H[i])$; binary search for the first $i$ exceeding $k$, and return $l = \text{SA}[i]$, $r = l + H[i] + (k - \text{pref}[i-1]) - 1$.
  4. *Pitfall*: When counting with multiplicity (`TJOI2015 弦论` $t=1$), the lengths $H[i]+1 \dots$ have decreasing multiplicities determined by the right boundaries $R_k$ on the Cartesian tree of $H$ (or SAM DAG path counts).

##### 23. `[EN]` `CF 666E — Forensic Examination` (SA + Cartesian Tree + Segment Tree Merge formulation)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), $M$ dictionary strings $T_1, \dots, T_M$ ($\sum |T_i| \le 5 \times 10^4$), and $Q \le 5 \times 10^5$ queries $(l, r, p_l, p_r)$, find which $T_k$ ($k \in [p_l, p_r]$) maximizes $\text{occ}_{T_k}(S[l..r])$.
- **4-Step Analysis**:
  1. *Signal*: Query substring $S[l..r]$ is given by endpoints; we must find its equivalence class in $S \texttt{\#} T_1 \texttt{\#} \dots \texttt{\#} T_M$ and query the frequency mode over $k \in [p_l, p_r]$.
  2. *Invariant*: In the Generalized SA of $S$ and $T_1 \dots T_M$, the suffixes sharing prefix $S[l..r]$ form a contiguous SA interval $[L(l, r), R(l, r)]$ (which is a single node in the Cartesian tree of $H$).
  3. *Compilation*: Locate $[L(l, r), R(l, r)]$ in $O(\log N)$ via binary search on RMQ of $H$ around $\text{rk}[l]$; use Mo's algorithm, Wavelet Matrix, or Segment Tree Merging on the Cartesian tree of $H$ to query the maximum count in dictionary index range $[p_l, p_r]$.
  4. *Pitfall*: If $\max_{k \in [p_l, p_r]} \text{occ}_{T_k}(S[l..r]) = 0$, the problem requires outputting the **smallest index $p_l$** with count `0`, not index `0`!

##### 24. `[JA]` `JOI 2018 Spring Camp — Bitaro's Party / Wildcard Split Matching` (2D Orthogonal Range Query on $(\text{SA}, \text{SA}^R)$)
- **Statement & Constraints**: Given a text $S[1..N]$ and $Q$ queries $(P_1, P_2)$ (or single-wildcard pattern $P_1 \cdot \texttt{?} \cdot P_2$, $\sum (|P_1| + |P_2|) \le 2 \times 10^5$), count how many occurrences of $P_1 \cdot \texttt{?} \cdot P_2$ appear in $S$.
- **4-Step Analysis**:
  1. *Signal*: Naive intersection of occurrences of $P_1$ and occurrences of $P_2$ takes $O(\text{occ}(P_1) + \text{occ}(P_2)) = O(N)$ per query.
  2. *Invariant*: Position $i$ is the wildcard center iff $S[1..i-1]$ ends with $P_1$ ($\text{rk}_{S^R}[N-(i-1)+1] \in [L^R(P_1^R), R^R(P_1^R)]$) and $S[i+1..N]$ starts with $P_2$ ($\text{rk}_S[i+1] \in [L(P_2), R(P_2)]$).
  3. *Compilation*: Plot $N-2$ points $p_i = (\text{rk}_{S^R}[N-i+2],\, \text{rk}_S[i+1])$ in 2D; answer each query as a 2D rectangle count $[L^R, R^R] \times [L, R]$ via a Wavelet Matrix or offline Fenwick sweep in $O((N + Q)\log N + \sum (|P_1|+|P_2|))$.
  4. *Pitfall*: Off-by-one in the reversal index mapping: prefix $S[1..i-1]$ reversed starts at index $N - (i - 1) + 1 = N - i + 2$ in $S^R$, while suffix $S[i+1..N]$ starts at $i+1$ in $S$.

---

#### Tier 4: Mastery (6 Problems — Internal Border Queries, Dyadic IPM, Dominant Pairs & Bi-Directional Grandmasters)

##### 25. `[ZH]` `[BJWC2018] Border 的四种求法` (Luogu P4482)
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ queries $(l, r)$ ($N, Q \le 2 \times 10^5$), find the length of the longest proper border of $S[l..r]$.
- **4-Step Analysis**:
  1. *Signal*: Arbitrary substring $S[l..r]$ has no precomputed KMP table; a border $k \in [1..r-l]$ requires $S[l..l+k-1] = S[r-k+1..r]$.
  2. *Invariant*: Either (a) via **SAM Link-Tree HLD + Segment Tree Merging**, $i \in [l, r-1]$ ends a border iff $i - \text{len}(\text{LCA}_{\text{SAM}}(i, r)) < l$, or (b) via **Kociumaka's Dyadic IPM Decomposition (`Iter 70.3`)**, for each scale $m \in [0..\lfloor \log_2(r-l) \rfloor]$, occurrences of $P_m = S[l..l+2^m-1]$ in $S[r-2^{m+1}+2..r]$ and occurrences of $Q_m = S[r-2^m+1..r]$ in $S[l..l+2^{m+1}-2]$ each form a **single arithmetic progression**!
  3. *Compilation*: Implement either Method 1 (SAM Link-Tree HLD + Segment Tree Merge predecessor query + heavy-chain Segment Tree in $O((N+Q)\log^2 N)$) or Method 4 (Dyadic IPM + Persistent Segment Tree over SA + 1D AP intersection in $O((N+Q)\log^2 N)$).
  4. *Pitfall*: Querying $i \in [l, r]$ instead of $i \in [l, r-1]$ returns the improper border $k = r - l + 1$; in AP intersection, when an AP has $\le 2$ elements, its step $d$ is not constrained by $\text{per}(P_m)$ and must be checked point-by-point.

##### 26. `[EN]` `CF 1043G — Speckled Band`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $(l, r)$, find the minimum number of distinct block types needed to partition $S[l..r]$ so that no two adjacent blocks are identical (equiv. minimum $k$-coloring of repeats, which turns out to be $\le 4$!).
- **4-Step Analysis**:
  1. *Signal*: The answer for $S[l..r]$ is always in $\{-1, 1, 2, 3, 4\}$! Specifically:
     - `-1` iff all characters in $S[l..r]$ are distinct (checkable in $O(1)$ via character prefix sums since $|\Sigma| = 26$).
     - `1` iff $S[l..r]$ is a periodic repetition $w^d$ ($d \ge 2$), i.e., has a period $p \mid (r-l+1)$ with $p < r-l+1$.
     - `2` iff $S[l..r]$ has a **non-empty border** ($S[l..l+k-1] = S[r-k+1..r]$ for some $k$, giving $A \cdot B \cdot A$), OR begins with a square $AA$, OR ends with a square $AA$.
     - `3` iff $S[l..r]$ contains any square $AA$ strictly inside $[l, r]$, OR $S[l]$ repeats in $S[l+1..r]$, OR $S[r]$ repeats in $S[l..r-1]$.
     - `4` otherwise!
  2. *Invariant*: Testing whether $S[l..r]$ has **any** border reduces to testing if the **shortest border** of $S[l..r]$ exists, which by IPM / Runs / $\sqrt{N}$ SA-neighborhood (`Iter 70.3`) can be checked in $O(\sqrt{N})$ or $O(\log N)$ per query; squares starting at $i$ or ending at $j$ are precomputed in $O(N \log N)$ via Lyndon Runs (`[NOI2016] 优秀的拆分` checkpoints).
  3. *Compilation*: Precompute shortest square starting at $l$ ($\text{min\_sq\_L}[l]$) and ending at $r$ ($\text{min\_sq\_R}[r]$) via $O(N \log N)$ LCE checkpoints + DSU/Segment Tree; check `1` via divisors of $r-l+1$ and $O(1)$ LCE; check `2` (border existence) via $\sqrt{N}$ split ($k \le \sqrt{N}$ checked by LCE, $k > \sqrt{N}$ checked by $|\text{rk}[j] - \text{rk}[l]| \le \sqrt{N}$).
  4. *Pitfall*: Checking only $A \cdot B \cdot A$ for answer `2` and forgetting $A \cdot A \cdot B$ (square prefix) or $B \cdot A \cdot A$ (square suffix)!

##### 27. `[ZH]` `[WC2018] 即时战略` / Dominant Pairs on Suffix Tree (`[UOJ / LOJ / QOJ] 支配对 LCP`: $\max_{l \le i < j \le r} \text{LCP}(\text{suf}(i), \text{suf}(j))$ or `CF 765F` on Suffixes)
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ queries $(l, r)$ ($N, Q \le 2 \times 10^5$), find $\max_{l \le i < j \le r} \min\big(r - j + 1,\, \text{LCP}(\text{suf}(i), \text{suf}(j))\big)$—the longest repeated substring inside $S[l..r]$.
- **4-Step Analysis**:
  1. *Signal*: Naive check of all pairs $(i, j) \in [l, r]^2$ takes $O((r-l)^2)$.
  2. *Invariant*: By **Engine D (`Iter 69.3`, DSU-on-Tree Dominant Pairs)**, in the Cartesian Tree of $H$ (or SAM Link Tree), at internal node $u$ with string depth $\ell_u$, when merging light child indices into the heavy child's `std::set<int>`, an index $x$ only needs to pair with its **immediate predecessor $x^-$ and successor $x^+$** in original string index order! Why? Because if $x^- < y < x$ belonged to the opposite subtree, $y$ would contradict $x^-$ being the immediate predecessor; and for any $z < x^-$, $[z, x] \supset [x^-, x]$ while both pairs have the exact same $\text{LCP} = \ell_u$, so $(x^-, x)$ strictly dominates $(z, x)$ for every query $[l, r]$!
  3. *Compilation*: Run DSU-on-Tree on the Cartesian tree of $H$ to extract at most $2N \log_2 N$ dominant triples $(i, j, \ell_u)$ ($i < j$). For a query $(l, r)$ with $l \le i < j \le r$, each triple contributes $\min(r - j + 1, \ell_u)$. Split at $j + \ell_u - 1 \le r$ vs. $> r$ and answer offline via 2D Fenwick tree sweep by decreasing $l$ in $O(N \log^2 N + Q \log N)$!
  4. *Pitfall*: Forgetting to cap $\ell_u$ by $r - j + 1$ allows the repeated substring starting at $j$ to extend past the right query boundary $r$!

##### 28. `[EN]` `Universal Cup / QOJ — Substring Rank & Lexicographical Range Queries` (`[ZJOI2017] 字符串` / IPM + Significant Suffixes Bridge)
- **Statement & Constraints**: Given $S[1..N]$ (under range alphabet shifts or static queries) and $Q$ queries $(l, r)$, find the lexicographically largest or $k$-th suffix of $S[l..r]$.
- **4-Step Analysis**:
  1. *Signal*: The relative order of two suffixes $S[i..r]$ and $S[j..r]$ of $S[l..r]$ differs from the global suffix order $\text{rk}[i] \lessgtr \text{rk}[j]$ **only when one is a prefix of the other** ($\text{LCE}(i, j) \ge r - \max(i, j) + 1$)!
  2. *Invariant*: If we look for the lexicographically **minimal** suffix of $S[l..r]$, all suffixes $S[i..r]$ that are not prefixes of the best candidate preserve their global SA rank $\text{rk}[i]$; the only tie-breaking overrides occur along the $O(\log N)$ **Significant Suffixes** / dyadic prefix-border chain (`Wave 1B` + `Wave 2B` IPM).
  3. *Compilation*: Use Persistent Segment Tree over SA to find the suffix $i_0 \in [l, r]$ with minimum global $\text{rk}[i_0]$ (which maximizes $S[i_0..r]$ when no prefix containment occurs, or is the longest prefix among tied candidates), then walk the $O(\log N)$ border chain of $S[i_0..r]$ via IPM / Significant Suffixes.
  4. *Pitfall*: Assuming the suffix $i \in [l, r]$ with minimum $\text{rk}[i]$ in global SA is always the minimum suffix of $S[l..r]$! Counterexample: $S = \texttt{abac}$, query $[1, 3] = \texttt{aba}$. Global suffixes: $\text{suf}(3) = \texttt{ac} < \text{suf}(1) = \texttt{abac}$, so $\text{rk}[3] < \text{rk}[1]$, EXCEPT if $S = \texttt{abad}$, $\text{suf}(1) = \texttt{abad} < \text{suf}(3) = \texttt{ad}$ ($\text{rk}[1] < \text{rk}[3]$), yet inside $S[1..3] = \texttt{aba}$, $S[3..3] = \texttt{a} < S[1..3] = \texttt{aba}$ because truncation at $r=3$ turns $S[3..3]$ into a proper prefix of $S[1..3]$!

##### 29. `[JA]` `AtCoder AGC 047 B — First Second` (Bi-Directional Trie + Suffix Equivalence)
- **Statement & Constraints**: Given $N$ strings $S_1, \dots, S_N$ ($\sum |S_i| \le 10^6$), in one operation you can delete either the first character or the second character of a string. Count pairs $(i, j)$ such that $S_i$ can be reduced to $S_j$.
- **4-Step Analysis**:
  1. *Signal*: Deleting the 1st or 2nd character repeatedly from $S_i$ allows keeping **any** single character $c \in S_i[1 .. |S_i|-|S_j|+1]$ as the first character, followed by the exact suffix $S_i[|S_i|-|S_j|+2 .. |S_i|] = S_j[2 .. |S_j|]$!
  2. *Invariant*: $S_i$ reduces to $S_j$ iff $S_j[2..|S_j|]$ is a suffix of $S_i$, and the character $S_j[1]$ appears at least once in the prefix $S_i[1 .. |S_i| - |S_j| + 1]$.
  3. *Compilation*: Insert all reversed strings $S_i^R$ into a Trie (or Suffix Tree / SA of reversed strings), maintaining at each prefix depth a 26-bit mask of characters present in the remaining prefix of $S_i$; query for each $S_j$ the node of $S_j[2..]^R$ and bit-count $S_j[1]$.
  4. *Pitfall*: Subtracting $i = j$ self-pairs.

##### 30. `[EN]` `POI 2012 — Prefixuffix (Prefiksufiks)` / Generalized Bi-Directional Cyclic Border (`CF / QOJ` Cyclic Border Queries)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6$) and/or substring queries $S[l..r]$, find the longest **cyclic border** (a prefix $S[l..l+k-1]$ and suffix $S[r-k+1..r]$ with $k \le (r-l+1)/2$ that are **cyclic shifts** of one another: $S[l..l+k-1] = U \cdot V$ and $S[r-k+1..r] = V \cdot U$).
- **4-Step Analysis**:
  1. *Signal*: $U$ is already a border of $S[l..r]$, and $V$ is a border of the stripped interior $S[l+|U| .. r-|U|]$!
  2. *Invariant*: For every shrink step from $(l', r') \to (l'+1, r'-1)$, the maximum inner border length $f(l', r')$ decreases by **at most 2**: $f(l'+1, r'-1) \ge f(l', r') - 2$! Why? Because removing the first and last character of $S[l'..r']$ removes at most 2 characters from its longest border.
  3. *Compilation*: Compute $f(i, N-i+1)$ from the center $i = \lfloor N/2 \rfloor$ outward to $i = 1$: initialize $len = f(i+1, N-i) + 2$, and decrement $len$ while $\text{LCE}(i, N - i + 1 - len + 1) < len$ in $O(1)$ per step ($O(N)$ total time!). Combine with longest exact border of $S[1..N]$.
  4. *Pitfall*: Allowing $k + f(k+1, N-k) > \lfloor N/2 \rfloor$ overlaps the prefix and suffix in the middle; always cap at $\lfloor N/2 \rfloor - k$.

---

## 72.3 Multilingual Terminology Rosetta Stone & Academic/Contest Bibliography (`Wave 2B`)

| English (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) | Canonical Papers & Treatises |
| :--- | :--- | :--- | :--- |
| **Induced Sorting (SA-IS)** | 诱导排序 (`SA-IS`) | 誘導ソート (`SA-IS`) | Nong, Zhang, Chan (DCC 2009), *"Linear Suffix Array Construction by Almost Pure Induced-Sorting"* |
| **LMS (Leftmost S-type) Substring** | LMS 子串 / 最左 S 型子串 | LMS 部分文字列 | Nong–Zhang–Chan (2009); Ko–Aluru (2003) |
| **Cartesian Tree on LCP (`height`)** | `height` 数组的笛卡尔树 | LCP 配列上の Cartesian Tree | Kasai et al. (2001); Abouelhoda et al. (2004, *Enhanced Suffix Array*) |
| **Virtual Suffix Tree** | 后缀树虚树 | 圧縮接尾辞木 (Auxiliary Suffix Tree) | `[CF 1073G]`, `[SDOI2011] 消耗战` + Suffix Tree LCA |
| **Dominant Pairs on Suffix Tree** | 后缀树支配对 (`启发式合并支配对`) | 接尾辞木上の支配ペア (Dominant Pairs) | Chinese National Team Papers (`国家集训队论文 — 支配对理论`) |
| **Internal Pattern Matching (IPM)** | 内部模式匹配 / 基本子串字典 | 内部パターンマッチング (IPM) | Kociumaka, Radoszewski, Rytter, Waleń (SODA 2015 / PhD Thesis 2018), *"Internal Pattern Matching Queries in a Text and Applications"* |
| **Internal Border Query** | 区间 Border 查询 (`Border 的四种求法`) | 部分文字列の最大 Border クエリ | Jin Ce (`金策`, *国家集训队论文 2019* & `[BJWC2018] Border 的四种求法`); Kociumaka et al. |
| **Suffix Balanced Tree** | 后缀平衡树 | 接尾辞平衡二分探索木 | Dietz–Sleator (STOC 1987, *Order Maintenance*); Chen Lijie (`陈立杰`, WC / 集训队讲座) |
| **Symmetric Compact DAWG (SCDAWG)** | 对称压缩有向无环词图 / 双向后缀自动机 | 対称コンパクト DAWG (SCDAWG) | Blumer et al. (1987); Inenaga, Hoshino, Shinohara, Takeda, Arikawa (2001–2005), *"On-Line Construction of Symmetric Compact Directed Acyclic Word Graphs"* |

---

## 72.4 Frontier & Obscure Extensions Discovered in Wave 2B (`[EN]`/`[ZH]`/`[JA]` Deep Audit)

To ensure Phase 1.5 curriculum design captures frontier developments beyond standard Suffix Arrays and Virtual Suffix Trees, we document three advanced reductions connecting `Wave 2B` to modern stringology:

### 1. Kempa–Kociumaka String Synchronizing Sets ($\tau$-Synchronizing Sets) as a Deterministic Sublinear-Space LCE & IPM Engine
While SA-IS (`Iter 68`) selects **LMS positions** (local minima of suffix order at distance $1$, which can be sparse or dense depending on runs and only compress by a guaranteed factor of $2$), Kempa and Kociumaka (STOC 2019) introduced **$\tau$-Synchronizing Sets**:
- Given a parameter $\tau \ge 1$, a subset of positions $\mathsf{S} \subseteq [1 .. n - 2\tau + 1]$ is a $\tau$-synchronizing set if:
  1. **Local Consistency**: Whether $i \in \mathsf{S}$ depends **only** on the length-$2\tau$ substring $S[i .. i + 2\tau - 1]$ (for instance, picking $i$ if the minimum Lyndon rank or Karp–Rabin / Birenbaum–Ukkonen rank among $[i .. i+\tau]$ occurs at one of the endpoints).
  2. **Density Bound**: No two synchronizing positions in any non-periodic region are closer than $\Omega(\tau)$, so $|\mathsf{S}| = O(n / \tau)$.
  3. **Covering Guarantee**: Every window $[i .. i + \tau - 1]$ whose underlying length-$3\tau-1$ substring does not have period $\le \tau/3$ contains **at least one** synchronizing position $s \in \mathsf{S}$!
- **Why this matters for Competitive Programming & Textbook Synthesis**:
  - $\tau$-Synchronizing Sets generalize both the **Difference Cover ($DC_3$)** of Kärkkäinen–Sanders (which is position-dependent rather than content-dependent) and **SA-IS LMS positions** (which have $\tau = 1$ but no $O(n/\tau)$ density guarantee).
  - For $\tau = \Theta(\log_\sigma n)$, they allow constructing Suffix Arrays and answering $O(1)$ LCE and Internal Pattern Matching queries in $O(n / \log_\sigma n)$ packed words!

### 2. Substring Rank (`Rank(S[l..r])`) & Range Distinct Substring Counting via Persistent Segment Tree on `height` Cartesian Tree
How do we assign a **canonical global lexicographical rank** $\text{SubRank}(S[l..r]) \in [1 .. |\text{Sub}(S)|]$ to any query substring $S[l..r]$ in $O(\log N)$ time?
1. Locate the highest ancestor $u$ of leaf $\text{rk}[l]$ in the Suffix Tree (or Cartesian tree of $H$) whose string depth satisfies $\text{len}(u) \ge r - l + 1$ (via binary lifting on the Suffix Tree or binary search on RMQ of $H$).
2. Precompute a DFS traversal over the Suffix Tree accumulating the number of distinct substrings $\text{len}(v) - \text{len}(p(v))$ on each edge $(p(v), v)$ in lexicographical order of outgoing characters.
3. Then:
   $$
   \text{SubRank}(S[l..r]) = \text{pref\_substrings}(u) - \big(\text{len}(u) - (r - l + 1)\big),
   $$
   computable in **$O(1)$ time** once $u$ is found in $O(\log N)$ (or $O(1)$ with level-ancestor / micro-macro tree)!

### 3. Additional Bonus Problems for Reserve / Synthesis (`#31`–`#33`)

##### 31. `[ZH]` `[THUPC 2019 / QOJ] 双向后缀平衡树 / Deque Distinct Substrings Online`
- **Statement & Constraints**: Start with an empty string; support $Q \le 2 \times 10^5$ online **encrypted** operations: (1) prepend character $c$ to front, (2) append character $c$ to back, and output the total number of distinct substrings after each operation.
- **4-Step Analysis**:
  1. *Signal*: Online encrypted front-prepend and back-append simultaneously.
  2. *Invariant*: Maintain two coupled **Suffix Balanced Trees (`后缀平衡树`)**: $\mathcal{T}_{\text{suf}}$ maintaining all suffixes of $S$ (supporting $O(\log N)$ front-prepend directly!), and $\mathcal{T}_{\text{pref}}$ maintaining all reversed prefixes of $S$ (supporting $O(\log N)$ back-append directly!). Wait—when we prepend $c$ to the front of $S$, how do we also update $\mathcal{T}_{\text{pref}}$? We don't need to insert into $\mathcal{T}_{\text{pref}}$ if each step only counts the **new** substrings created at the active end ($\Delta = |S| - \max(\text{LCP}(u, u^-), \text{LCP}(u, u^+))$), PROVIDED $\mathcal{T}_{\text{suf}}$ has all current suffixes and $\mathcal{T}_{\text{pref}}$ has all current prefixes! And how does a front-prepend add a new prefix of length $1$ to $\mathcal{T}_{\text{pref}}$ (or back-append add a length-1 suffix to $\mathcal{T}_{\text{suf}}$)? A back-append changes the last character of all suffixes, which only affects suffixes within LCP $\ge$ their total length—meaning the only tie-breaks that change in $\mathcal{T}_{\text{suf}}$ are suffixes that were previously **prefixes of another suffix** (i.e., borders of $S$)!
  3. *Compilation*: Alternatively, use the **Online Symmetric Compact DAWG (SCDAWG)** (`Iter 71.2`) or maintain the Suffix Balanced Tree of suffixes paired with the longest border of $S$ to update the $O(1)$ new equivalence class at the opposite end.
  4. *Pitfall*: Assuming $\mathcal{T}_{\text{suf}}$ and $\mathcal{T}_{\text{pref}}$ are completely independent without transferring the newly created 1-character prefix/suffix between them.

##### 32. `[EN]` `CF 1063F — String Journey` (Cartesian Tree on `height` + Persistent Segment Tree DP)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), find the maximum $k$ such that there is a sequence of disjoint substrings $t_1, t_2, \dots, t_k$ from left to right where $|t_i| = k - i + 1$ and $t_{i+1}$ is a proper substring of $t_i$.
- **4-Step Analysis**:
  1. *Signal*: By greedy truncation, we may assume $|t_i| = k - i + 1$ and $t_{i+1}$ is either the prefix $t_i[1..|t_i|-1]$ or the suffix $t_i[2..|t_i|]$!
  2. *Invariant*: Let $dp[i]$ be the maximum valid length of a chain starting at index $i$. Then $dp[i] \le dp[i+1] + 1$! As we decrement $i$ from $N$ down to $1$, a candidate length $L = dp[i]$ is valid iff there exists $j \ge i + L$ such that $dp[j] \ge L - 1$ and either $\text{LCE}(i, j) \ge L - 1$ or $\text{LCE}(i + 1, j) \ge L - 1$!
  3. *Compilation*: Because $dp[i] \le dp[i+1] + 1$, the pointer $ptr = i + dp[i]$ advances monotonically from $N$ down to $1$ ($O(N)$ total pointer steps!). Each check asks whether the SA interval $[L(i, \ell-1), R(i, \ell-1)]$ (or for $i+1$) has $\max dp[j] \ge \ell - 1$ among already-inserted $j \ge i + \ell$, answered in $O(\log N)$ via a Segment Tree over SA positions! Total time: $O(N \log N)$.
  4. *Pitfall*: Inserting $j$ into the Segment Tree before $i + dp[i]$ reaches $j$ allows overlapping substrings $t_i$ and $t_{i+1}$.

##### 33. `[JA]` `AtCoder AGC 060 D — Same Descent Set` / Suffix-Rank Permutation Inversion Dualities (Bridge to `Wave 5A`)
- **Statement & Constraints**: Explores the characterization of suffix rank permutations `rk[1..N]` induced by L/S-type descent patterns: a position $i$ is L-type iff $\text{rk}[i] > \text{rk}[i+1]$ (a descent in the inverse suffix array `rk`!), directly linking SA-IS L/S types (`Iter 68`) to permutation descent combinatorics.
