# Wave 5A Master Reconciled Treatise & Problem Archive (Cohort 3, Iteration 113): Word Equations, Parallel DSU (`倍增并查集`), String Inequalities, Wheeler/De Bruijn Graphs & Strings on Trees

> [!IMPORTANT]
> **Cohort 3 Cross-Agent Reconciliation & Blind-Spot Audit (Iteration 113)**
> This master synthesis reconciles **Cohort 1 (`strings_research/iter_41_to_45_word_equations_dsu_bwt_tree_strings.md`)** and **Cohort 2 (`strings_research/cohort2_iter_93_to_97_word_equations_dsu_bwt_tree_strings.md`)** across **Wave 5A**. It executes:
> 1. **A Granular Cross-Cohort Blind-Spot Audit (§0)**: Exposing every structural invariant, edge-case pitfall, complexity bound, and multilingual problem captured by one cohort and missed by the other.
> 2. **An Obscure & Frontier Stringology Gap Hunt (§0.4)**: Adding deep theoretical and competitive bridges missed or only sketched in single cohorts—including **Tree Binary-Lifting DSU** on branched ancestor paths, **Move-Structure $O(1)$ RLBWT Interval Jumping** (Nishimoto–Tabei 2021), **Mantaci–Restivo–Rosone Bijective BWT (`BBWT`) & Lyndon Multiset Inversion**, and **Alanko–Gagie–Navarro–Benkiki Deterministic Wheeler DFA Interval Partitioning**.
> 3. **The Unified 4-Step Master Theory Treatise (§1–§4)**: Synthesizing the sharpest proofs, worked traces, broken-invariant counterexamples, and non-standard algorithmic contracts.
> 4. **The Deduplicated Master Problem Archive (§5–§6)**: **48 unique accepted non-template problems (`W5A-01..W5A-48`)** across 4 difficulty tiers with full 4-Step Zero-Magic Analysis, plus **12 quarantined templates (`R-5A-01..R-5A-12`)** and a unified **Multilingual Rosetta Stone & Bibliography (§7)**.

---

## 0. Cross-Cohort Comparison & Blind-Spot Audit (Cohort 1 vs. Cohort 2)

### 0.1 What Cohort 1 (`Iter 41–45`) Captured That Cohort 2 (`Iter 93–97`) Missed or Under-Specified

| Topic Area | Cohort 1 Unique Discovery / Superior Formulation | Cohort 2 Blind Spot or Gap | Reconciled Action in Cohort 3 Master |
| :--- | :--- | :--- | :--- |
| **Signed / Parity DSU for Palindrome Equations** | Explicitly identified the **Self-Reversal Root Loop Bug** (`Pitfall 1`, `Iter 41.2` & `Contract A.1`): when a merge induces a parity-$1$ self-loop on a DSU root $r$ at level $k$ ($B(k, r) = B(k, r)^R$), a standard parity DSU sees `find(u) == find(v)` and returns early, completely dropping the palindrome constraint on $B(k, r)$! Cohort 1 introduced the explicit root flag `is_pal[k][r]` pushed down via `UNITE(k-1, r, r + 2^{k-1}, 1)` **before** non-root edges. | Cohort 2 (`Iter 93.3.2`) gave both the $S \cdot S^R$ concatenation reduction and the signed-edge DSU pushdown `(i, r + 2^{k-1}, 1)`, and even traced a self-reversal in `Trace A`, but **never stated the `is_pal[k][r]` root boolean invariant** needed when `find(u) == find(v)` in code! | Adopt Cohort 1's `is_pal[k][r]` root self-palindrome bit AND Cohort 2's $S \cdot S^R$ concatenation duality + `Trace A` ($N=6$) worked walkthrough. |
| **Huge-$N$ ($10^{18}$) Word Equations & Palindrome Reflection Groups** | Explicitly separated **three regimes** (`Iter 41.4`): (A) Fine–Wilf periodic folding, (B) **Palindromic Reflection Group on $[1..N]$** where two overlapping palindrome involutions $\sigma_1(x) = l_1 + r_1 - x$ and $\sigma_2(x) = l_2 + r_2 - x$ compose to a translation $\sigma_2(\sigma_1(x)) = x + (l_2 + r_2 - l_1 - r_1)$, and (C) **Artur Jeż's Recompression (JACM 2016)** via alternating run-length block compression $c^k \to c_k$ and locally consistent pair compression $ab \to c$ on SLPs in $O(M \log N)$ phases. | Cohort 2 (`Iter 93.3.3`) covered Plandowski (1994/1999) and Euclidean modulo period folding, and noted single-palindrome midpoint folding, but omitted the composition of two reflections into a translation shift and omitted Jeż's Recompression (2016). | Unify Plandowski/Euclidean interval modulo folding, the Dihedral Reflection-to-Translation Group reduction, and Jeż's SLP Recompression in `§1.4`. |
| **Wheeler Graph Recognition Obstruction** | Formulated the **forbidden interval-interleaving obstruction** (`P-5A-29`): when edges are sorted by $(a, u)$, target vertices $v$ must be non-decreasing, so $u_1 < u_2 < u_3$ with $v_1 = v_3 \neq v_2$ is the exact convexity violation of $\text{pre}_c(v)$. | Cohort 2 stated the 3 Wheeler axioms and the 2-step vertex-to-edge-to-vertex rank lookup (`Iter 97 #20`), but did not state the interval convexity recognition test. | Combine Cohort 1's convexity recognition test with Cohort 2's two-step edge-rank transition formula in `§3.3`. |
| **Unique Cohort 1 Problems** | Cataloged `CF 827A` (DSU next-uncovered jump), `BZOJ 4974 / [SDOI2017]` (`per[i] = i - pi[i]` reconstruction), `CF 1051E` (Z-LCE big-integer substring inequality DP), `CF 291E` (KMP DFA vs. amortized KMP tree hazard), `ABC 272 F` (cyclic shift SA separator tie-breaking), `CF 535D` (Z-array overlap consistency), `ABC 197 F` (product-graph bidirectional palindrome BFS), `CF 1152F2` (De Bruijn window matrix DP), `[USACO12DEC] First! G` (Trie 26-vertex alphabet DAG), `[PKUSC2018] 神仙的游戏` (NTT border conflict sieve), `AtCoder ABC 336 G` (`16 Integers` 4-mer BEST theorem), `AGC 047 B` (reversed Trie prefix mask), `[HNOI2019] JOJO` (persistent KMP on version tree with RLE `slink`), `CF 1310C — Au Pont Rouge` (LCP threshold binary search DP), and `ARC 050 D` (suffix concatenation comparator via 2 LCP queries). | Missed or replaced these 15 specific problems with other problems. | Preserve all 15 unique Cohort 1 problems in the master 48-problem archive (`§5`). |

---

### 0.2 What Cohort 2 (`Iter 93–97`) Captured That Cohort 1 (`Iter 41–45`) Missed or Under-Specified

| Topic Area | Cohort 2 Unique Discovery / Superior Formulation | Cohort 1 Blind Spot or Gap | Reconciled Action in Cohort 3 Master |
| :--- | :--- | :--- | :--- |
| **Potential-Function Proof of Online Binary-Lifting DSU** | Provided a formal potential function proof (`Theorem 93.1`): $\Phi = \sum_{k=0}^K c_k \le N(K+1)$, dividing recursive `merge(k, i, j)` calls into **Productive Calls** ($\Delta \Phi = -1$, at most $N(K+1)$) and **Unproductive (Short-Circuited) Calls** (at most $2M + 2 \times \text{productive}$), plus **Online Conflict Rollback** via small-to-large `neq[r]` sets (`Iter 97 #18`). | Cohort 1 (`Iter 41.2 Step 3.2`) gave the correct edge-counting argument ($\le N-1$ successful unions per level), but did not formalize the potential $\Phi$ or online conflict-rejection with rollback (`neq[r]`). | Adopt Cohort 2's formal potential proof (`Theorem 1.2`) and online conflict-checking DSU contract in `§1.2–§1.3`. |
| **Complete Sufficiency Proof & `banana` Trace of SA Adjacency Theorem** | Proved **both necessity and backward-induction sufficiency** of the Suffix Array Adjacency Theorem (`Iter 94.2.3`), compiled a comprehensive **5-Row Inverse Reconstruction Duality Table** (Z-array, KMP $\pi$, Manacher $R$, SA alone, and SA + `height`), highlighted the **Phantom Equality / Chromatic Number Trap** (why forward verification is mandatory when $|\Sigma|$ is bounded), and gave a hand-checkable trace on `S = "banana"` (`Trace B`). | Cohort 1 (`Theorem 42.1`) proved the step-by-step rank reduction $S[u..N] < S[v..N] \iff S[u+1..N] < S[v+1..N]$ when $S[u]=S[v]$, but did not include the 5-row comparative table, the chromatic number triangle counterexample on $|\Sigma|=2$, or the `"banana"` trace. | Include Cohort 2's 5-row duality table, sufficiency proof, chromatic counterexample, and `"banana"` trace in `§2`. |
| **Lex-Smallest Hierholzer Proof & AC-DFA BEST Generalization** | Explained *why* post-order reversal in Hierholzer's algorithm with sorted outgoing lists yields the lexicographically smallest Eulerian string (`Iter 95.3.2`), and generalized the BEST theorem from fixed-$k$ De Bruijn graphs to **Aho–Corasick DFAs avoiding forbidden substrings** (`Iter 97 #30`), pointing out the critical pitfall that two edges $u \xrightarrow{c} v$ and $u \xrightarrow{c'} v$ with $c \neq c'$ can land in the same AC state $v$, so the denominator divides by $\prod_{u, c} \text{count}(u, c)!$ rather than $\prod_{u, v} A(u, v)!$! | Cohort 1 covered the De Bruijn BEST theorem (`Theorem 43.1`) and `ABC 336 G`, but did not include the Aho–Corasick DFA BEST theorem generalization or the $(u, c)$ vs. $(u, v)$ parallel-edge pitfall. | Elevate Cohort 2's AC-DFA BEST theorem and $(u, c)$ vs. $(u, v)$ pitfall into `§3.2`. |
| **RLBWT Piecewise-Translation Intervals** | Formulated **Run-Length Burrows–Wheeler Transform (`RLBWT`)** interval jumping (`Iter 97 #29`) for $N \le 10^{12}$ with $R \le 10^5$ BWT runs, showing that $\text{LF}$ is a piecewise-translation bijection with $R$ intervals. | Cohort 1 covered standard FM-index backward search and cyclic BWT without sentinel, but omitted RLBWT for $N \le 10^{12}$. | Integrate RLBWT + Nishimoto–Tabei $O(1)$ Move-Structure jumping into `§3.3`. |
| **Tree SA Kasai Fallacy, Tree LCP Binary Lifting & `[CTSC2010] 珠宝商` Child-Subtree Subtraction Pitfall** | Exposed two subtle tree-string bugs: (1) **Why Kasai's $O(N)$ algorithm (`h[rk[u]] >= h[rk[fa[u]]] - 1`) fails on branched trees** (`Iter 96.4.2`) and how to compute `height[i]` in $O(\log N)$ using the saved $\text{rk}_k[u]$ layers; (2) In **`[CTSC2010] 珠宝商`** (`Iter 97 #25`), when subtracting same-subtree pairs for a large centroid $S_c > \sqrt{M}$, **you must also threshold each child subtree $|T_{\text{sub}}|$ against $B = \sqrt{M}$**, otherwise a star-like centroid with $O(S_c)$ leaf children of size $1$ runs $O(M)$ Link-Tree pushdown $O(S_c)$ times and TLEs in $O(NM)$! Also introduced **Tree Binary-Lifting DSU** (`Iter 97 #32`) on $(u, k)$ ancestor blocks. | Cohort 1 (`P-5A-26`) derived the $\sqrt{M}$ centroid split and dual-SAM Link-Tree pushdown for `[CTSC2010] 珠宝商`, but missed the **child-subtree threshold pitfall** during inclusion-exclusion subtraction! Cohort 1 also did not state the Kasai fallacy on trees or Tree Binary-Lifting DSU. | Incorporate Cohort 2's child-subtree thresholding fix for `[CTSC2010] 珠宝商`, the Kasai fallacy proof, and Tree Binary-Lifting DSU into `§4`. |
| **Unique Cohort 2 Problems & Quarantine Entries** | Cataloged `ARC 044 D` (Inverse SA string construction), `[POI 2000] 公共串` (multi-string LCS via BFS GSAM), `[JSOI2015] 串分割` (circular digit splitting), `Tree Path Substring Comparison via rk_k` (`Iter 97 #15`), `UOJ 607 / General k-mer BEST`, `Online Word Equations with Conflict Rollback` (`Iter 97 #18`), `Tree SA + Height RMQ for Distinct Upward Prefixes` (`Iter 97 #19`), `[ZJOI2019] 语言 / Tree Path AC Avoidance`, `CF 1063F — String Journey`, `AGC 055 D — ABC Ultimatum`, `Partially Filled Z-Array Reconstruction`, `Tree Path 1-Mismatch Pattern Counting via Centroid + LCE Hash`, `RLBWT Pattern Matching`, `AC Automaton + BEST Theorem`, `[BJOI2020] 树上子串`, and `Tree Binary-Lifting DSU + Inequality Graph`. Also quarantined `Luogu P5353` (when treated as a bare template without queries) and `SPOJ BWTINV`. | Cohort 1 placed `Luogu P5353` in Tier 2 (`P-5A-12`) to teach Dual-Rank Tree SA, whereas Cohort 2 quarantined bare `Luogu P5353` (`R-5A-01`) and instead placed **Tree SA coupled with LCP/Chairman Tree/Substring Queries** in the ladder. | Reconcile cleanly: per `AGENTS.md`, quarantine bare `Luogu P5353` (`R-5A-09`) while teaching its exact Dual-Rank Doubling Contract in `§4.2` and testing it via query-coupled problems (`W5A-18`, `W5A-31`, `W5A-45`, `W5A-48`). |

---

### 0.3 Obscure & Frontier Stringology Gap Hunt (Added in Cohort 3)

To ensure zero blind spots across `[EN]`, `[ZH]`, and `[JA]` sources, Cohort 3 adds four frontier techniques to Wave 5A:

1. **Tree Binary-Lifting DSU (`树上倍增并查集`) for Path Word Equations (`§1.5` & `W5A-48`)**:
   - When equality constraints $S(u_1, L) = S(u_2, L)$ are imposed on **upward ancestor paths** (or decomposed general simple paths via HLD / LCA splitting $u \rightsquigarrow \text{lca}(u, v) \rightsquigarrow v$) of a tree $T$, we replace 1D intervals $[i, i+2^k-1]$ with tree binary-lifting states $(k, u)$ representing the upward path from $u$ of length $2^k$. Pushing down $(k, u) \equiv (k, v)$ merges $(k-1, u) \equiv (k-1, v)$ and $(k-1, \text{anc}(u, 2^{k-1})) \equiv (k-1, \text{anc}(v, 2^{k-1}))$. For arbitrary undirected tree paths $u_1 \rightsquigarrow v_1$ and $u_2 \rightsquigarrow v_2$ of length $L$, split each path at its LCA into an upward segment and a downward segment (which is a reversed upward segment!), splitting at most twice so every segment reduces to **Signed Tree Binary-Lifting DSU** in $O((M + N \log N)\alpha(N))$ time!
2. **Nishimoto–Tabei (2021) Move Structure for $O(1)$-Time RLBWT LF-Stepping (`§3.3` & `W5A-43`)**:
   - In Run-Length BWT (`RLBWT`) with $R$ runs over a string of length $N \le 10^{18}$, binary searching the $R$ intervals takes $O(\log R)$ per LF-step. By splitting output intervals so that each input run interval maps into a sub-interval spanning **at most $2$ output run intervals** (the **Move Data Structure** of Nishimoto & Tabei, ICALP 2021 / `r-index`), LF-mapping transitions $(idx, \text{offset}) \mapsto (idx', \text{offset}')$ run in **strictly $O(1)$ worst-case time** and $O(R)$ space!
3. **Bijective Burrows–Wheeler Transform (`BBWT`, Mantaci–Restivo–Rosone 2007) & Lyndon Necklace Decomposition (`§3.2`)**:
   - Standard BWT requires appending a sentinel `$` (increasing alphabet/length). The **Bijective BWT** factors $S = w_1 w_2 \dots w_m$ into its unique non-increasing Chen–Fox–Lyndon factorization (Wave 1B) and sorts all cyclic shifts of all $w_j$ under the **$\omega$-order** ($u \prec_\omega v \iff u^\infty < v^\infty$). Then LF-mapping decomposes into $m$ disjoint cycles whose lengths equal $|w_1|, \dots, |w_m|$, establishing a bijection between $\Sigma^N$ and $\Sigma^N$ with **no sentinel character**!
4. **Deterministic Wheeler Graph Partitioning & Co-Lexicographical Interval Refinement (`§3.3`)**:
   - Given an acyclic or general DFA $G = (V, E, \Sigma)$, we can decide whether $G$ is a Wheeler Graph and construct its Wheeler ordering $\prec$ in $O(|E| \log |V|)$ time (Alanko, Gagie, Navarro, Benkiki 2020) via Hopcroft-style **co-lexicographical interval refinement** tracking $[\min\text{colex}(v), \max\text{colex}(v)]$.

---

## 1. Word Equations, Signed Binary-Lifting DSU (`倍增并查集`), Tree Path Equations & Huge-Length Contractions

### 1.1 Concrete Objects & Fundamental Question

Let $S[1..N]$ be an unknown string over an alphabet $\Sigma$. We are given $M$ **bulk word equation constraints** of two canonical types:
1. **Orientation-Preserving Substring Equality ($t = 0$)**: $S[l_1 .. l_1 + L - 1] = S[l_2 .. l_2 + L - 1]$, asserting that $\forall d \in [0, L-1],\; S[l_1 + d] = S[l_2 + d]$.
2. **Orientation-Reversing / Palindromic Substring Equality ($t = 1$)**: $S[l_1 .. l_1 + L - 1] = (S[l_2 .. l_2 + L - 1])^R$, asserting that $\forall d \in [0, L-1],\; S[l_1 + d] = S[l_2 + L - 1 - d]$. (Setting $l_1 = l_2$ forces $S[l_1 .. l_1 + L - 1]$ to be a palindrome.)

Let $\sim$ be the smallest equivalence relation on $\{1, 2, \dots, N\}$ generated by these $M$ equations, and let $C$ be the number of connected components of $(\{1, \dots, N\}, \sim)$. How do we compute the exact equivalence classes of $\sim$ in $O((M + N \log N)\alpha(N))$ time when $N \le 5 \cdot 10^5$, on a **tree** when paths are equated, and when $N \le 10^{18}$?

---

### 1.2 The 4-Step "Zero Magic Invariants & Structural Decompositions" Derivation

#### Step 1: The Diagnostic Signal (Why Pointwise DSU, Segment Trees & Treaps Fail)
- **Pointwise DSU ($O(NM \alpha(N))$)**: A single constraint of length $L = \Theta(N)$ performs $L$ individual merges `unite(l1 + d, l2 + d)`, taking $10^{10}$ operations for $N, M = 10^5$.
- **Canonical Segment Tree Range-Graph Failure**: A segment tree partitions $[l_1, r_1]$ and $[l_2, r_2]$ into $O(\log N)$ dyadic blocks aligned to multiples of $2^k$. Whenever $l_1 \not\equiv l_2 \pmod{2^k}$, the dyadic blocks of $[l_1, r_1]$ and $[l_2, r_2]$ have **different lengths and misaligned split offsets**, so you cannot equate segment tree nodes!
- **Huge-Length Regime ($N \le 10^{18}$)**: Even $O(N \log N)$ states cannot be allocated in memory, and an overlapping shift $S[l..l+L-1] = S[l+p..l+p+L-1]$ with $p \ll L$ slices naive coordinate-compressed intervals into $O(L/p) = O(N)$ fragments.

#### Step 2: The Combinatorial Word Invariant (Dyadic Block Covering & Potential Amortization)

Instead of disjoint dyadic partitions, we use **overlapping power-of-two blocks** (Sparse-Table / ST-table geometry). For each level $k \in \{0, 1, \dots, \lfloor \log_2 N \rfloor\}$ and start index $i \in [1, N - 2^k + 1]$, let $B_k(i) := S[i .. i + 2^k - 1]$ denote the block of length $2^k$ starting at $i$.

> [!IMPORTANT]
> **Theorem 1.1 (Lossless Dyadic Block Covering Equivalence)**
> Let $L \ge 1$ and $k = \lfloor \log_2 L \rfloor$, so $2^k \le L < 2^{k+1}$.
> 1. **Forward Equality ($t = 0$)**: $S[l_1 .. l_1 + L - 1] = S[l_2 .. l_2 + L - 1]$ holds **if and only if**:
>    $$B_k(l_1) = B_k(l_2) \quad \text{and} \quad B_k(l_1 + L - 2^k) = B_k(l_2 + L - 2^k).$$
> 2. **Reversed Equality ($t = 1$)**: $S[l_1 .. l_1 + L - 1] = (S[l_2 .. l_2 + L - 1])^R$ holds **if and only if**:
>    $$B_k(l_1) = B_k(l_2 + L - 2^k)^R \quad \text{and} \quad B_k(l_1 + L - 2^k) = B_k(l_2)^R.$$

**Proof by Double-Inclusion of Offsets**:
Let $I = \{0, 1, \dots, L-1\}$, $A = \{0, \dots, 2^k - 1\}$, and $B = \{L - 2^k, \dots, L - 1\}$. Because $2^k \le L < 2 \cdot 2^k$, we have $0 \le L - 2^k \le 2^k$, so $A \cup B = I$.
- In the forward case ($t = 0$), $B_k(l_1) = B_k(l_2)$ enforces $S[l_1 + d] = S[l_2 + d]$ for all $d \in A$, and $B_k(l_1 + L - 2^k) = B_k(l_2 + L - 2^k)$ enforces $S[l_1 + d] = S[l_2 + d]$ for all $d \in B$. For any offset $d \in A \cap B = \{L - 2^k, \dots, 2^k - 1\}$ in the overlap, both block equations assert the **exact same character equality** $S[l_1 + d] = S[l_2 + d]$.
- In the reversed case ($t = 1$), the prefix $S[l_1 .. l_1 + 2^k - 1]$ of the first interval must equal the reversal of the **suffix** $S[l_2 + L - 2^k .. l_2 + L - 1]$ of the second interval, which for $d \in A$ gives $S[l_1 + d] = S[(l_2 + L - 2^k) + (2^k - 1 - d)] = S[l_2 + L - 1 - d]$. Symmetrically, the second block equation enforces $S[l_1 + d] = S[l_2 + L - 1 - d]$ for all $d \in B$. Thus no index is omitted and no contradictory constraint is introduced. $\blacksquare$

Now consider a single level $k > 0$. Any block equality $B_k(i) = B_k(r)$ of length $2^k$ splits into **two half-block equalities** of length $2^{k-1}$ at level $k-1$:
$$B_k(i) = B_k(r) \iff B_{k-1}(i) = B_{k-1}(r) \;\wedge\; B_{k-1}(i + 2^{k-1}) = B_{k-1}(r + 2^{k-1}),$$
and any reversed block equality $B_k(i) = B_k(r)^R$ splits with **cross-swapped half-offsets**:
$$B_k(i) = B_k(r)^R \iff B_{k-1}(i) = B_{k-1}(r + 2^{k-1})^R \;\wedge\; B_{k-1}(i + 2^{k-1}) = B_{k-1}(r)^R.$$

```
Level k (rev = 1):   [---- B_k(i) ----]   === (reversed) ===   [---- B_k(r) ----]^R
                      /              \                          /              \
Level k-1:     [ B_{k-1}(i) ]  [ B_{k-1}(i+h) ]          [ B_{k-1}(r) ]  [ B_{k-1}(r+h) ]
                     |                \________________________/                |
                     \__________________________________________________________/
               B_{k-1}(i) == B_{k-1}(r+h)^R       AND      B_{k-1}(i+h) == B_{k-1}(r)^R
```

> [!IMPORTANT]
> **Theorem 1.2 (Potential Function Bound for Online Recursive Binary-Lifting DSU)**
> Suppose queries arrive **online** and we execute `merge_block(k, i, j, d)` recursively: if `find(k, i) == find(k, j)` (and no new self-palindrome bit `is_pal[k][r]` is set), return immediately; otherwise unite at level $k$ and recurse on the two half-block equations at level $k-1$. Across any sequence of $M$ queries on a string of length $N$, the total number of `merge_block` calls is at most $2M + 6N(\lfloor \log_2 N \rfloor + 1) = O(M + N \log N)$, running in $O((M + N \log N)\alpha(N))$ time.

**Proof**: Define the potential function
$$\Phi = \sum_{k=0}^{\lfloor \log_2 N \rfloor} \big( c_k + p_k \big),$$
where $c_k \le N$ is the number of connected components in $\text{DSU}_k$ and $p_k \le c_k \le N$ is the number of components at level $k$ with `is_pal[k][r] == 0`. Initially $\Phi \le 2N(\lfloor \log_2 N \rfloor + 1)$, and always $\Phi \ge 0$.
Every call to `merge_block(k, i, j, d)` is either:
- **Productive**: Either $\text{find}_k(i) \neq \text{find}_k(j)$ (merging two components so $c_k$ drops by $1$, and $p_k$ does not increase) or $\text{find}_k(i) = \text{find}_k(j) = r$ with a new self-palindrome parity $d_{\text{net}} = 1$ when `is_pal[k][r]` was $0$ (flipping `is_pal[k][r]` from $0 \to 1$ so $p_k$ drops by $1$). In both cases $\Delta \Phi \le -1$, and the call spawns at most $2$ child calls at level $k-1$.
- **Unproductive (Short-Circuited)**: $\text{find}_k(i) = \text{find}_k(j)$ and no new `is_pal` bit is flipped. It terminates in $O(\alpha(N))$ time with zero recursive calls.
Since $\Phi$ can decrease at most $2N(\lfloor \log_2 N \rfloor + 1)$ times across the entire execution, there are at most $2N(\lfloor \log_2 N \rfloor + 1)$ productive calls, and every unproductive call is either one of the $2M$ top-level query calls or a direct child of a productive call. $\blacksquare$

---

#### Step 3: The Reverse-Engineering Scratchpad (Offline Pushdown, Signed DSU & Online Conflict Rollback)

1. **Offline Top-Down Level Pushdown (`[SCOI2016] 萌萌哒`)**:
   - Insert each query $(t, l_1, l_2, L)$ into level $k = \lfloor \log_2 L \rfloor$ via two `UNITE(k, ...)` calls.
   - Sweep $k$ from $\lfloor \log_2 N \rfloor$ down to $1$ with $h = 2^{k-1}$:
     - **Pass 1 (Root Self-Palindromes)**: For each root $r$ at level $k$ (`fa[k][r] == r`) with `is_pal[k][r] == 1`, call `UNITE(k - 1, r, r + h, 1)`.
     - **Pass 2 (Component Spanning Edges)**: For each $i \in [1, N - 2^k + 1]$ with $(r, d) = \text{FIND}(k, i)$ and $r \neq i$:
       - If $d = 0$: `UNITE(k - 1, i, r, 0)` and `UNITE(k - 1, i + h, r + h, 0)`.
       - If $d = 1$: `UNITE(k - 1, i, r + h, 1)` and `UNITE(k - 1, i + h, r, 1)`.
2. **Isomorphic $S' = S \cdot S^R$ Concatenation Trick (Alternative to Signed DSU)**:
   - If you want to avoid writing signed DSU parity bits and `is_pal[k][r]`, construct a virtual string $S' = S \cdot S^R$ of length $2N$. Pre-unite `UNITE(0, i, 2N + 1 - i)` for all $1 \le i \le N$ at level $0$. Then any reversed equality $S[l_1..r_1] = S[l_2..r_2]^R$ is simply the **orientation-preserving** equality $S'[l_1..r_1] = S'[2N + 1 - r_2 .. 2N + 1 - l_2]$ on $[1..2N]$! (Trades $2\times$ memory for zero parity logic.)
3. **Online Queries with Point Inequality Conflicts ($S[u] \neq S[v]$)**:
   - Maintain at each level-$0$ DSU root $r$ a hash set `neq[r]` of roots forbidden from merging with $r$. When uniting $r_u$ and $r_v$ at level $0$, check if $r_v \in \text{neq}[r_u]$; if no conflict occurs, merge their `neq` sets small-to-large in $O(\log^2 N)$. If a query must be rejected atomically upon conflict, record level-$k$ DSU changes on a rollback stack during the query's `merge_block` calls and unwind if a conflict is hit at level $0$.

---

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples

- **Pitfall 1 (Dropping Parity-1 Self-Loops on DSU Roots)**:
  - *Counterexample*: Let $N = 4$ and impose a single palindrome query $S[1..4] = S[1..4]^R$. Here $L = 4, k = 2$, so we call `UNITE(2, 1, 1, rev=1)`. Since `find(2, 1) == find(2, 1)`, a naive DSU that returns whenever `ru == rv` does **nothing**, leaving $C = 4$ instead of $C = 2$! Maintaining `is_pal[k][ru] = 1` when `ru == rv` and `(du ^ dv ^ d) == 1` is mandatory in Signed DSU.
- **Pitfall 2 (Not Swapping Half-Offsets on `rev = 1` Pushdown)**:
  - *Counterexample*: If $B_1(1) = S[1..2]$ and $B_1(3) = S[3..4]$ have `rev = 1`, then $S[1..2] = (S[3..4])^R \implies S[1]=S[4], S[2]=S[3]$. Pushing down `(1, 3, 1)` and `(2, 4, 1)` without swapping the second operand's half-offset forces $S[1]=S[3]$ and $S[2]=S[4]$ (a translation instead of a reversal!).

---

### 1.3 Worked Trace: Signed Binary-Lifting DSU on Overlapping Translation + Palindrome ($N = 6$)

Suppose $S[1..6]$ satisfies:
1. $S[1..4] = S[3..6]$ (forward translation, $L = 4 = 2^2, t = 0$), and
2. $S[1..4] = (S[1..4])^R$ (palindrome of length $4 = 2^2, t = 1$).

- **At level $k = 2$ ($2^2 = 4$)**:
  - Query 1 calls `UNITE(2, 1, 3, 0)` $\implies \text{fa}[2][1] = 3, \text{rev}[2][1] = 0$.
  - Query 2 calls `UNITE(2, 1, 1, 1)` $\implies \text{find}(2, 1) = (3, 0)$, so $(0 \oplus 0 \oplus 1) = 1 \implies \text{is\_pal}[2][3] = 1$.
- **Pushdown $k = 2 \to 1$ ($h = 2^1 = 2$)**:
  - Pass 1 (Root self-palindrome on $r = 3$): `UNITE(1, 3, 3 + 2, 1)` = `UNITE(1, 3, 5, 1)`.
  - Pass 2 (Edge $i = 1 \to r = 3, d = 0$): `UNITE(1, 1, 3, 0)` and `UNITE(1, 3, 5, 0)`.
  - Notice that combining `(3, 5, 1)` and `(3, 5, 0)` at level $1$ sets $\text{is\_pal}[1][\text{root}(3)] = 1$!
- **Pushdown $k = 1 \to 0$ ($h = 2^0 = 1$)**:
  - Pass 1 (Root self-palindrome at level $1$): unites $(3, 4)$ (and by transitivity $(1, 2)$ and $(5, 6)$).
  - Pass 2 (Edges at level $1$): $(1, 3, 0) \implies S[1]=S[3], S[2]=S[4]$; $(3, 5, 0) \implies S[3]=S[5], S[4]=S[6]$.
  - All $6$ positions collapse into **one single component** $\{1, 2, 3, 4, 5, 6\}$ ($C = 1$), matching the hand check!

---

### 1.4 Huge-Length Word Equations ($N \le 10^{18}, M \le 10^5$) via Fine–Wilf Contractions & Jeż's Recompression

When $N \le 10^{18}$, three structural engines replace $O(N \log N)$ arrays:
1. **Plandowski / Fine–Wilf Euclidean Period Folding**:
   - An overlapping translation equation $S[l_1..r_1] = S[l_2..r_2]$ with $l_1 < l_2 \le r_1$ and shift $p = l_2 - l_1$ makes the union $[l_1, r_2]$ periodic with period $p$: every index $x \in [l_2, r_2]$ folds canonically into $[l_1, l_1 + p - 1]$ via $x \mapsto l_1 + ((x - l_1) \bmod p)$, splitting any query sub-interval $[a, b] \subseteq [l_2, r_2]$ into at most **two** contiguous sub-intervals in $[l_1, l_1 + p - 1]$.
   - If two periodic intervals of periods $p$ and $q$ overlap by $\ge p + q - \gcd(p, q)$, the **Fine–Wilf Theorem** contracts their union into a single period $g = \gcd(p, q)$; on shorter overlaps, replacing $(q, p)$ by $(p, q \bmod p)$ mimics the Euclidean algorithm in $O(\log N)$ steps.
2. **Dihedral Reflection-to-Translation Reduction for Huge Palindromes**:
   - Each palindrome constraint on $[l_i, r_i]$ acts as an affine reflection $\sigma_i(x) = l_i + r_i - x$. Any single palindrome folds $[ \lfloor (l_i+r_i)/2 \rfloor + 1, r_i ]$ onto $[l_i, \lceil (l_i+r_i)/2 \rceil ]$, halving the interval length; two overlapping reflections $\sigma_1, \sigma_2$ compose to a pure translation $\sigma_2(\sigma_1(x)) = x + (l_2 + r_2 - l_1 - r_1)$, reducing to Case 1.
3. **Artur Jeż's Recompression (JACM 2016) on Straight-Line Programs (SLPs)**:
   - For completely general word equations of description size $M$ over $N \le 10^{18}$, represent intervals implicitly and alternate two local contractions: (a) **Run-Length Block Compression** replacing maximal blocks $c^k \to c_k$, and (b) **Locally Consistent Pair Compression** partitioning $\Sigma = \Sigma_L \sqcup \Sigma_R$ (deterministically or via 2-coloring active adjacency edges) and compressing $ab \to c$ for $(a, b) \in \Sigma_L \times \Sigma_R$. Each phase shrinks block lengths by a constant factor, terminating in $O(M \log N)$ phases!

---

### 1.5 Frontier Extension: Tree Binary-Lifting DSU (`树上倍增并查集`) for Path Word Equations

Suppose characters sit on the vertices of a tree $T$ ($N \le 2 \cdot 10^5$), and we are given $M$ path-equality constraints asserting $\text{str}(u_1 \rightsquigarrow v_1) = \text{str}(u_2 \rightsquigarrow v_2)$ of length $L$:
1. **Upward Ancestor Paths**: Define block $B_k(u)$ to be the upward vertical path of $2^k$ vertices starting at $u$: $u \to \text{fa}(u) \to \dots \to \text{anc}(u, 2^k - 1)$.
   - An upward path equality $\text{str}(u_1 \uparrow L) = \text{str}(u_2 \uparrow L)$ decomposes via $k = \lfloor \log_2 L \rfloor$ into:
     $$B_k(u_1) = B_k(u_2) \quad \text{and} \quad B_k(\text{anc}(u_1, L - 2^k)) = B_k(\text{anc}(u_2, L - 2^k)).$$
2. **General Simple Paths $u \rightsquigarrow v$ via LCA Splitting + Signed Tree DSU**:
   - Every simple path $u \rightsquigarrow v$ in $T$ splits at $w = \text{lca}(u, v)$ into an **upward prefix** $u \uparrow w$ of length $d_1 = \text{depth}(u) - \text{depth}(w) + 1$ and a **downward suffix** $\text{child}(w, v) \downarrow v$ of length $d_2 = \text{depth}(v) - \text{depth}(w)$, which is the **exact reversal** of the upward path $v \uparrow \text{child}(w, v)$!
   - Thus equating $\text{str}(u_1 \rightsquigarrow v_1) = \text{str}(u_2 \rightsquigarrow v_2)$ splits at both LCAs into at most **3 pairs of upward ancestor path equations** (some orientation-preserving $t=0$, some orientation-reversing $t=1$)!
   - Pushing $(k, u) \equiv_{d} (k, r)$ down from level $k$ to $k-1$ with $h = 2^{k-1}$ calls:
     - If $d = 0$: `UNITE(k-1, u, r, 0)` and `UNITE(k-1, anc(u, h), anc(r, h), 0)`.
     - If $d = 1$: `UNITE(k-1, u, anc(r, h), 1)` and `UNITE(k-1, anc(u, h), r, 1)`.
   - Total complexity across the entire tree: $O((M + N \log N)\alpha(N))$ time!

---

## 2. String Inequality Graphs, Lexicographical Constraints & Inverse String Reconstruction

### 2.1 Concrete Objects & Fundamental Question

Suppose an unknown string $S[1..N]$ over an ordered alphabet $(\Sigma, <)$ is constrained by:
- **Lexicographical Substring Inequalities**: $S[l_1..r_1] < S[l_2..r_2]$ or $S[l_1..r_1] \le S[l_2..r_2]$, or
- **Inverse String Structure Specifications**: a target **Suffix Array** $\text{SA}[1..N]$ (with or without `height`), **KMP prefix function** $\pi[1..N]$, **Z-array** $Z[1..N]$, or **Manacher radii** $R[1..2N-1]$.

We must decide feasibility, compute the **minimum alphabet size** $|\Sigma|_{\min}$, reconstruct the **lexicographically smallest valid string** $S$, or **count** all valid strings $S \in \Sigma^N$.

---

### 2.2 The 4-Step "Zero Magic Invariants & Structural Decompositions" Derivation

#### Step 1: The Diagnostic Signal (Why Inequalities Cannot Be Pushed Down Like Equalities)
Unlike equality ($AB = CD \iff A = C \wedge B = D$), lexicographical order is a **disjunction over the Longest Common Prefix (LCP)** $t = \text{LCP}(U, V)$:
$$U < V \iff \Big( \exists t \in [0, \min(|U|, |V|) - 1] : U[1..t] = V[1..t] \;\wedge\; U[t+1] < V[t+1] \Big) \;\lor\; \Big( |U| < |V| \;\wedge\; U = V[1..|U|] \Big).$$
Because $t$ is unknown in an arbitrary unanchored inequality system (in fact, general unanchored substring inequality feasibility is NP-hard!), polynomial-time algorithms rely on one of three structural anchors:
1. **LCP Witness Decomposition**: $t = \text{LCP}(S[l_1..r_1], S[l_2..r_2])$ is given or fixed by equality constraints, splitting each inequality into **one bulk prefix equality of length $t$** (fed to `§1` Binary-Lifting DSU) + **one point character inequality** $S[l_1+t] < S[l_2+t]$.
2. **Inverse String Structures (SA / KMP / Z / Manacher)**: The structure itself fixes the exact equality prefix and mismatch index for every comparison.
3. **2-SAT / Small-Alphabet Prefix Branching (`CF 568C`)**: A single global inequality $S \ge S_0$ has only $N+1$ candidate LCP lengths $t \in [0, N]$.

#### Step 2: The Combinatorial Word Invariant (SA Adjacency Theorem & Inverse Duality Table)

> [!IMPORTANT]
> **Theorem 2.1 (Nong–Zhang–Chan / Burrows–Wheeler Suffix Array Adjacency Theorem)**
> Let $\text{SA}[1..N]$ be a permutation of $\{1, \dots, N\}$, and let $\text{rk}[1..N+1]$ be its inverse rank array with $\text{rk}[\text{SA}[i]] = i$ and empty-suffix sentinel $\text{rk}[N+1] = 0$. A string $S[1..N]$ has suffix array $\text{SA}$ **if and only if** for every $i \in \{1, \dots, N-1\}$ with $u = \text{SA}[i]$ and $v = \text{SA}[i+1]$:
> 1. **Permissive Step ($\le$)**: If $\text{rk}[u+1] < \text{rk}[v+1]$, then $S[u] \le S[v]$.
> 2. **Forced Strict Step ($<$)**: If $\text{rk}[u+1] > \text{rk}[v+1]$, then $S[u] < S[v]$.

**Proof (Necessity & Sufficiency)**:
- **Necessity ($\implies$)**: Since $S[u..N] < S[v..N]$, their first characters satisfy $S[u] \le S[v]$. If $S[u] = S[v]$, stripping the shared first character reduces the comparison of $S[u..N]$ vs. $S[v..N]$ to $S[u+1..N]$ vs. $S[v+1..N]$. Thus $S[u] = S[v]$ is legal **only** when $S[u+1..N] < S[v+1..N]$, i.e., $\text{rk}[u+1] < \text{rk}[v+1]$. Whenever $\text{rk}[u+1] > \text{rk}[v+1]$, equality $S[u] = S[v]$ would force $S[u..N] > S[v..N]$, so we **must** have $S[u] < S[v]$.
- **Sufficiency ($\impliedby$)**: Suppose $S$ satisfies (1) and (2) for all $i \in [1, N-1]$, yet some adjacent pair $(u, v) = (\text{SA}[i], \text{SA}[i+1])$ violates $S[u..N] < S[v..N]$. Choose the violating adjacent pair $(u, v)$ that **minimizes the remaining suffix length** $\min(N - u + 1, N - v + 1)$ (or equivalently maximizes $\max(u, v)$). Since $S[u] \le S[v]$ holds by (1)–(2), $S[u..N] \ge S[v..N]$ forces $S[u] = S[v]$ and $S[u+1..N] \ge S[v+1..N]$ (note $u, v \le N$ cannot have $u = N$ and $S[u]=S[v]$ because $\text{rk}[N+1] = 0 < \text{rk}[v+1]$ gives $S[N..N] = S[v] < S[v] S[v+1..N]$ strictly!). Because $S[u] = S[v]$ was permitted by (1)–(2), we must have $\text{rk}[u+1] < \text{rk}[v+1]$. Therefore, in the target $\text{SA}$ ordering between $\text{rk}[u+1]$ and $\text{rk}[v+1]$, the suffixes starts at $S[u+1..N]$ and ends at $S[v+1..N] \le S[u+1..N]$, so by transitivity **at least one adjacent pair $(\text{SA}[j], \text{SA}[j+1])$ in that interval must also be inverted**, and since first characters are non-decreasing along $\text{SA}$, all suffixes in $[\text{rk}[u+1], \text{rk}[v+1]]$ share the same first character, giving a shorter inverted adjacent pair—contradicting the minimality of $(u, v)$! $\blacksquare$

**Corollaries of Theorem 2.1**:
- Let $D = \sum_{i=1}^{N-1} [\text{rk}[\text{SA}[i]+1] > \text{rk}[\text{SA}[i+1]+1]]$ be the number of **forced strict jumps**.
- The **minimum alphabet size** to realize $\text{SA}$ is $|\Sigma|_{\min} = D + 1$.
- The number of valid strings over an alphabet of size $K$ is $\binom{N + K - 1 - D}{N}$ (`CF 1526E`).

##### Complete 5-Structure Inverse Reconstruction Duality Table

| Target Structure | Implied Equality Constraints (DSU / Copy) | Implied Mismatch ($\neq$) or Order ($<, \le$) Constraints | Structural Validity & Verification Rule |
| :--- | :--- | :--- | :--- |
| **Z-Array** $Z[2..N]$ | $S[1 .. Z[i]] = S[i .. i + Z[i] - 1]$ | If $i + Z[i] \le N$: $S[1 + Z[i]] \neq S[i + Z[i]]$ | $0 \le Z[i] \le N - i + 1$; re-run forward Z-algorithm on $S$ to verify. |
| **KMP Array** $\pi[1..N]$ | If $\pi[i] > 0$: $S[i] = S[\pi[i]]$ | $\forall q \in \text{FailChain}(\pi[i-1])$ with $q + 1 > \pi[i]$: $S[i] \neq S[q+1]$; if $\pi[i]=0$: $S[i] \neq S[1]$ | $\pi[1]=0, \pi[i] \le \pi[i-1]+1$. At most $2N$ total fail-chain mismatch edges by KMP potential! |
| **Manacher** $R[1..2N-1]$ | Center $c$, radius $R[c]$: $S[l..r] = S[l..r]^R$ | If $l > 1$ and $r < N$: $S[l-1] \neq S[r+1]$ | Linear sweep merges only new right boundaries $r > r_{\max}$ in $O(N)$; re-run Manacher to verify. |
| **Suffix Array** $\text{SA}[1..N]$ | None mandatory | For $u = \text{SA}[i], v = \text{SA}[i+1]$:<br>• $\text{rk}[u+1] < \text{rk}[v+1] \implies S[u] \le S[v]$<br>• $\text{rk}[u+1] > \text{rk}[v+1] \implies S[u] < S[v]$ | With $\text{rk}[N+1] = 0$, necessary and sufficient (Theorem 2.1). |
| **SA + LCP** ($\text{SA}, \text{height}$) | $\forall i \in [2, N]$: $S[\text{SA}[i-1] .. +h_i-1] = S[\text{SA}[i] .. +h_i-1]$ | Let $u = \text{SA}[i-1], v = \text{SA}[i]$. If $u+h_i \le N$ and $v+h_i \le N$: $S[u+h_i] < S[v+h_i]$ | If $v + h_i > N$, **impossible** ($S[u..N]$ cannot be a prefix of $S[v..N]$ with $u \neq v$ and $S[u..N] < S[v..N]$ unless $u + h_i > N$!). |

---

#### Step 3: The Reverse-Engineering Scratchpad (Tarjan SCC + Condensation DAG Longest Path)

To solve a combined system of substring equalities $S[a..b] = S[c..d]$, weak character inequalities $S[u] \le S[v]$, and strict character inequalities $S[u] < S[v]$:
1. **Equality Contraction**: Push all interval equalities down the Binary-Lifting DSU (`§1`) to level $0$. Let $V_0 = \{ \text{find}_0(i) : 1 \le i \le N \}$.
2. **Weighted Inequality Digraph $G = (V_0, E_0 \cup E_1)$**:
   - Each $S[u] \le S[v]$ adds a weight-$0$ directed edge $\text{find}_0(u) \xrightarrow{0} \text{find}_0(v)$.
   - Each $S[u] < S[v]$ adds a weight-$1$ directed edge $\text{find}_0(u) \xrightarrow{1} \text{find}_0(v)$.
3. **Tarjan SCC Positive-Cycle Check**:
   - Compute Strongly Connected Components of $G$. Every cycle of $\le$ edges forces all vertices in the same SCC $C_a$ to take the **exact same character**.
   - Therefore, the system is **feasible** over an unbounded alphabet if and only if **no edge of weight $1$ ($<$) has both endpoints inside the same SCC $C_a$**!
4. **Condensation DAG Longest Path**:
   - On the condensation DAG $\mathcal{D}$, compute in topological order:
     $$\text{dist}[X] = \max\Big( \{0\} \cup \{ \text{dist}[Y] + w(Y \to X) : (Y \to X) \in \mathcal{D} \} \Big).$$
   - Then $K_{\min} = 1 + \max_X \text{dist}[X]$ is the minimum required alphabet size, and assigning `'a' + dist[SCC(find_0(i))]` produces the **pointwise lexicographically smallest valid string** $S$!

---

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples

- **Pitfall 1 (The Phantom Equality & Chromatic Number Trap in Z / KMP / Manacher Reconstruction)**:
  - *Counterexample 1 (Unreachable KMP Border)*: Let $N = 3$ and $\pi = [0, 0, 2]$. Simply setting $S[3] = S[\pi[3]] = S[2]$ and $S[2] \neq S[1]$ produces $S = \text{"abb"}$, whose actual KMP array is $[0, 0, 0] \neq [0, 0, 2]$ because $\pi[3] = 2 > \pi[2] + 1 = 1$ violates KMP border extension!
  - *Counterexample 2 (Chromatic Conflict on Small Alphabet)*: Suppose $|\Sigma| = 2$ (`{'a', 'b'}`) and the Z-array or Manacher array induces three pairwise non-equalities $S[1] \neq S[2], S[2] \neq S[3], S[1] \neq S[3]$ (a $K_3$ triangle of $\neq$ edges) with zero equality edges. DSU sees no self-loop $S[i] \neq S[i]$, yet no 2-coloring of $K_3$ exists!
  - **Universal Safeguard**: After constructing the candidate string $S$, **always run the forward KMP / Z / Manacher algorithm on $S$ in $O(N)$ time** and check that the resulting array matches the input entry-for-entry!
- **Pitfall 2 (Forgetting $\text{rk}[N+1] = 0$ in Inverse SA)**:
  - See Cohort 2 `Trace B` on $S = \text{"banana"}$ ($N = 6$, $\text{SA} = [6, 4, 2, 1, 5, 3]$): at $i = 1$ ($u = 6, v = 4$), $u + 1 = 7$ is the empty suffix with $\text{rk}[7] = 0 < \text{rk}[5] = 5$, allowing $S[6] = S[4] = \text{'a'}$. The only two forced strict jumps are $i = 3$ ($u = 2, v = 1 \implies \text{rk}[3]=6 > \text{rk}[2]=3 \implies S[2] < S[1]$) and $i = 4$ ($u = 1, v = 5 \implies \text{rk}[2]=3 > \text{rk}[6]=1 \implies S[1] < S[5]$), giving $D = 2$ and $|\Sigma|_{\min} = 3$.

---

## 3. De Bruijn Graphs, the BEST Theorem, Burrows–Wheeler Transform (BWT) & Wheeler Graphs

### 3.1 Concrete Objects & Fundamental Question

1. **$k$-Mer / Automaton Spectrum Counting & Reconstruction**: Given prescribed multiplicities $c(w)$ for each $k$-mer $w \in \Sigma^k$ (or transition counts on an Aho–Corasick DFA avoiding forbidden patterns), reconstruct the lexicographically smallest valid string $S$ or count the exact number of valid strings $S$ when $N = \sum c(w) + k - 1 \le 10^{18}$.
2. **BWT, RLBWT & Wheeler Graphs**: Given $\text{BWT}(S)$ (or a run-length compressed $\text{RLBWT}$ with $R$ runs for $N \le 10^{18}$, or an edge-labeled graph $G = (V, E, \Sigma)$), invert $\text{BWT}(S) \mapsto S$, count occurrences of $P[1..M]$ in $O(M)$ steps, and characterize when a DFA admits a 1D co-lexicographical interval ordering (**Wheeler Graph**).

---

### 3.2 The 4-Step "Zero Magic Invariants & Structural Decompositions" Derivation

#### Step 1: The Diagnostic Signal (Why Bitmask DP and Explicit Suffix Structures Fail)
- Counting strings of length $N \le 10^7$ or $10^{18}$ with exact $k$-mer multiplicities $c(w)$ cannot track the remaining frequency vector in DP ($\prod (c(w)+1)$ states).
- On a labeled graph or compressed text of length $N \le 10^{12}$, building an explicit Suffix Array takes $\Omega(N \log N)$ bits, whereas BWT / RLBWT / Wheeler DFAs maintain the active state set of any pattern $P$ as a **single 1D interval $[L_P, R_P]$**.

#### Step 2: The Combinatorial Word Invariant (De Bruijn Duality, BEST Bijection & Wheeler Monotonicity)

##### Invariant 3A: De Bruijn Subword-to-Edge Bijection & The BEST Theorem
In the **$(k-1)$-dimensional De Bruijn multigraph** $\mathcal{B}(\Sigma, k)$:
- **Vertices**: $V = \Sigma^{k-1}$ (words of length $k-1$).
- **Directed Edges**: Each $k$-mer $w = c_1 c_2 \dots c_k$ with count $c(w)$ contributes $c(w)$ parallel edges $w[1..k-1] \xrightarrow{w[k]} w[2..k]$.
- **Bijection**: Strings $S$ of length $N \ge k-1$ with $k$-mer spectrum $c(\cdot)$ correspond bijectively to **Eulerian trails** of length $N - k + 1$ in $\mathcal{B}(\Sigma, k)$.

> [!IMPORTANT]
> **Theorem 3.1 (The BEST Theorem — de Bruijn, van Aardenne-Ehrenfest, Smith, Tutte)**
> Let $G = (V_{\text{act}}, E)$ be a weakly connected balanced directed Eulerian multigraph where every active vertex $v \in V_{\text{act}}$ has $\text{in}(v) = \text{out}(v) = d(v) \ge 1$. Fix a root $r \in V_{\text{act}}$ and a reference outgoing edge $e_0$ from $r$.
> 1. **Edge-Labeled Eulerian Circuits**: The number of Eulerian circuits starting with $e_0$ (treating parallel edges as distinct) is:
>    $$\mathcal{E}_{\text{edge}}(G, e_0) = t_{\text{in}}(G, r) \cdot \prod_{v \in V_{\text{act}}} \big(d(v) - 1\big)!,$$
>    where $t_{\text{in}}(G, r) = \det L^{(r)}_{\text{out}}$ is the number of **directed spanning in-arborescences rooted at $r$** (oriented toward $r$), equal to the $(r, r)$-cofactor of the out-degree Laplacian $L_{\text{out}}(u, u) = d(u) - A(u, u)$ and $L_{\text{out}}(u, v) = -A(u, v)$ ($u \neq v$).
> 2. **Indistinguishable $k$-Mer / AC-DFA String Counting**: Because permuting the $c(w)$ parallel copies of the same $k$-mer $w$ (or the $\text{count}(u, c)$ copies of transition $u \xrightarrow{c} \delta(u, c)$ in a deterministic Aho–Corasick DFA) yields the **exact same string**, the number of distinct strings induced by open Eulerian trails from $u_{\text{start}}$ to $u_{\text{end}}$ (via virtual return edge $e_{\text{virt}} : u_{\text{end}} \to u_{\text{start}}$ at $r = u_{\text{end}}$) is:
>    $$\mathcal{E}_{\text{string}}(G) = \frac{t_{\text{in}}(G, r) \cdot \prod_{v \in V_{\text{act}}} \big(d(v) - 1\big)!}{\prod_{w \in \Sigma^k} c(w)!}.$$
>    *(If $u_{\text{start}} = u_{\text{end}} = r$ is already balanced without adding $e_{\text{virt}}$, multiply the numerator by $d(r)$ so the factor at $r$ is $d(r)!$ instead of $(d(r)-1)!$.)*

**Double-Count Proof of the BEST Bijection**:
- Given an Eulerian circuit starting with $e_0$ at $r$, record for each $v \neq r$ the **last outgoing edge $e_{\text{last}}(v)$** used to exit $v$, and for every $v \in V_{\text{act}}$ record the order $\pi_v$ in which its other $d(v)-1$ outgoing edges are traversed.
- **No Cycles in $\{e_{\text{last}}(v) : v \neq r\}$**: Suppose $v_1 \to v_2 \to \dots \to v_m \to v_1$ were a directed cycle of last-exit edges ($r$ has no edge in this set). Let $v_i$ be the vertex on the cycle whose final exit $e_{\text{last}}(v_i) = (v_i \to v_{i+1})$ occurs **last in time** along the circuit. Traversing $(v_i \to v_{i+1})$ enters $v_{i+1} \neq r$ *after* $v_{i+1}$ has already used its final exit $e_{\text{last}}(v_{i+1})$, contradicting $\text{in}(v_{i+1}) = \text{out}(v_{i+1})$! Thus $\{e_{\text{last}}(v)\}$ is a spanning in-arborescence $T$ rooted at $r$.
- **Unique Reconstruction**: Conversely, given any in-arborescence $T$ rooted at $r$ and local permutations $\{\pi_v\}$ of the $d(v)-1$ non-tree edges at each $v$, a walk starting with $e_0$ that always takes the next unused edge in $\pi_v$ and saves $e_{\text{last}}(v) \in T$ for last can never get stuck at $v \neq r$ (by degree balance) and cannot get stuck at $r$ while any edge remains untraversed (as any unvisited vertex $u$ would have a directed path in $T$ to $r$ whose tree edges were never used!). $\blacksquare$

##### Invariant 3B: BWT LF-Mapping Rank Preservation & Bijective BWT (`BBWT`)
For a string $S[1..N]$ ending with unique sentinel `$` (or decomposed into Lyndon words $w_1 \ge_{\text{lex}} \dots \ge_{\text{lex}} w_m$ under $\omega$-order in the **Mantaci–Restivo–Rosone Bijective BWT**):

> [!IMPORTANT]
> **Theorem 3.2 (The LF-Mapping Rank-Preservation Invariant)**
> In the sorted cyclic-shift matrix $\mathcal{M}$ with First column $F[1..N]$ and Last column $L[1..N] = \text{BWT}(S)$, for every character $c$ and every $k \ge 1$, the **$k$-th occurrence of $c$ in $L$** and the **$k$-th occurrence of $c$ in $F$** represent the **exact same character index in $S$**:
> $$\text{LF}(i) = C[L[i]] + \text{Occ}(L[i], i).$$

**Proof**: Any two rows $i < j$ in $\mathcal{M}$ with $L[i] = L[j] = c$ represent cyclic shifts $u_i c < u_j c \iff u_i < u_j$. Rotating the trailing $c$ to the front gives rows $i', j'$ in $F$ representing $c u_i$ and $c u_j$. Because prepending the *same* character $c$ preserves lexicographical order ($u_i < u_j \iff c u_i < c u_j$), we have $i' < j'$. $\blacksquare$

---

### 3.3 Wheeler Graphs & Run-Length BWT (`RLBWT`) Move Structures

A directed edge-labeled graph $G = (V, E, \Sigma)$ is a **Wheeler Graph** (Gagie–Manzini–Sirén 2017) iff there exists a total order $\prec$ on $V$ such that for all edges $(u_1 \xrightarrow{a_1} v_1)$ and $(u_2 \xrightarrow{a_2} v_2)$:
1. **Zero-Indegree First**: $\text{in}(v_1) = 0 < \text{in}(v_2) \implies v_1 \prec v_2$.
2. **Input-Label Homogeneity & Monotonicity**: $a_1 < a_2 \implies v_1 \prec v_2$ (every $v$ has a unique incoming character label $\lambda(v)$, and vertices are grouped contiguously by $\lambda(v)$).
3. **Co-Lexicographical Path Monotonicity**: $(a_1 = a_2 \;\wedge\; u_1 \prec u_2) \implies v_1 \preceq v_2$.

**Algorithmic Consequences & Pitfalls**:
- **Two-Step Interval Transition on General Wheeler DFAs**: In a linear BWT, each row has in-degree $1$ and out-degree $1$. In a general Wheeler DFA, vertices can have multiple incoming or outgoing edges of label $c$. To update the reachable vertex interval $[l_V, r_V]$ upon reading character $c$:
  1. Find the contiguous interval of **outgoing $c$-edges** $[l_E, r_E] = [\text{rank}_{\text{out}, c}(l_V - 1) + 1,\; \text{rank}_{\text{out}, c}(r_V)]$ leaving $[l_V, r_V]$.
  2. By Axiom 3, these edges land on a contiguous interval of target vertices $[l'_V, r'_V] = [\text{target}(c, l_E),\; \text{target}(c, r_E)]$!
- **Recognition Obstruction**: When edges of label $c$ are sorted by source vertex $u$, the target vertices $v$ must be non-decreasing. In particular, $u_1 \prec u_2 \prec u_3$ with $v_1 = v_3 \neq v_2$ is the exact forbidden interval-interleaving pattern.
- **RLBWT & Nishimoto–Tabei $O(1)$ Move Structure**: When $\text{BWT}(S)$ consists of $R$ equal-character runs ($N \le 10^{18}, R \le 10^5$), each run $L[l..r] = c^k$ maps by Theorem 3.2 to a single contiguous interval $[C[c] + \text{Occ}(c, l),\; C[c] + \text{Occ}(c, r)]$ of length $k$ in $F$. Binary searching the $R$ run boundaries gives $O(\log R)$ per LF-step; splitting runs so no mapped interval crosses more than $2$ run boundaries in $L$ (**Nishimoto–Tabei 2021 Move Structure**) gives **$O(1)$ worst-case LF-steps** in $O(R)$ space!
- **BEST Theorem Pitfalls**:
  1. **Isolated Vertices**: Always restrict the Laplacian $L_{\text{out}}$ to $V_{\text{act}} = \{v : d(v) > 0\}$ and verify that $V_{\text{act}}$ forms a single weakly connected component!
  2. **AC-DFA vs. De Bruijn Parallel Edges**: In an Aho–Corasick DFA, two edges $u \xrightarrow{c_1} v$ and $u \xrightarrow{c_2} v$ with **different characters $c_1 \neq c_2$** can enter the same state $v$ (e.g., via failure transitions back to root). They represent *distinct* characters and must **not** be treated as indistinguishable parallel edges: divide by $\prod_{u, c} \text{count}(u, c)!$, never by $\prod_{u, v} A(u, v)!$!

---

## 4. Strings on Trees — Tree Suffix Array, Tree Generalized SAM & Centroid Decomposition with Automata

### 4.1 Concrete Objects & Fundamental Question

Given a tree $T = (V, E)$ with $N$ vertices (or edges) labeled over $\Sigma$:
1. **Tree Suffix Array (`Luogu P5353`)**: Root $T$ at $1$ and sort all $N$ upward ancestor strings $S(u) = c(u) c(\text{fa}(u)) \dots c(1)$ lexicographically in $O(N \log N)$ time, plus answer LCP queries $\text{LCP}(S(u), S(v))$ and path-substring comparisons.
2. **Low-Leaf Undirected Path Substring Census (`[ZJOI2015] 诸神眷顾的幻想乡`)**: Given an unrooted tree $T$ ($N \le 10^5$) with **at most $L \le 20$ leaves**, count all distinct strings formed by simple paths $u \rightsquigarrow v$.
3. **General Undirected Tree-Path Pattern & Palindrome Counting (`CF 914E`, `[CTSC2010] 珠宝商`)**: On an arbitrary tree $T$ ($N \le 2 \cdot 10^5$), count simple paths $u \rightsquigarrow v$ that form a palindrome or match substrings of a pattern/text $S[1..M]$.

---

### 4.2 The 4-Step "Zero Magic Invariants & Structural Decompositions" Derivation

#### Step 1: The Diagnostic Signal (Why Linear SA, Kasai's Algorithm & Single-Rooted GSAM Fail on Trees)
1. **The Rank-Tie Collapse Paradox in Tree SA**:
   On a linear string, all suffixes have distinct lengths, so ranks become strictly distinct. On a tree, two distinct nodes $u \neq v$ can have the **exact same upward string** $S(u) = S(v)$!
   - If you break ties between $u$ and $v$ at step $k$ using vertex IDs so every node gets a unique rank $\text{id}_k[u]$, then at step $k+1$, two children $x, y$ with $\text{fa}(x)=u, \text{fa}(y)=v$ and $c(x)=c(y)$ will see $\text{id}_k[u] \neq \text{id}_k[v]$ in their first half and **falsely declare $S(x)[1..2^{k+1}] \neq S(y)[1..2^{k+1}]$** without comparing their second halves!
   - Conversely, if you only maintain tied ranks $\text{rk}_k[u]$, $O(N)$ nodes can fall into the same bucket, breaking deterministic tie-breaking and $O(N)$ bucket radix sort.
2. **The Kasai $O(N)$ LCP Fallacy on Branched Trees**:
   In a linear string, $\text{height}[\text{rk}[i]] \ge \text{height}[\text{rk}[i-1]] - 1$ holds because stepping from $i$ to $i+1$ moves to a unique next suffix. On a branched tree, multiple nodes $u, w$ can share the same parent $p = \text{fa}(u) = \text{fa}(w)$ and the same character $c(u) = c(w)$! Then the predecessor of $u$ in $\text{SA}$ may be $w$ (with $\text{fa}(w) = \text{fa}(u)$), while the predecessor of $\text{fa}(u)$ in $\text{SA}$ is some completely unrelated node $z$, destroying Kasai's lower bound!
3. **The $O(N^2)$ Simple-Path Explosion**:
   An unrooted tree has $\binom{N}{2}$ simple paths; a single rooting only turns vertical ancestor-descendant paths into prefixes, missing $\Lambda$-shaped paths $u \rightsquigarrow \text{lca}(u, v) \rightsquigarrow v$.

---

#### Step 2: The Combinatorial Word Invariant (Dual-Rank Splitting, Leaf-Rooted Cover & Centroid Stitching)

##### Invariant 4A: Dual-Rank Tree Suffix Array (`rk` for True String Equality vs. `id` for Total Order)
At each doubling step $k \in \{0, \dots, \lceil \log_2 N \rceil\}$, maintain **two distinct arrays**:
1. **True String Equivalence Rank $\text{rk}_k[u]$**:
   $$\text{rk}_k[u] = \text{rk}_k[v] \iff S(u)[1..2^k] = S(v)[1..2^k] \iff \big(\text{rk}_{k-1}[u], \text{rk}_{k-1}[\text{anc}(u, 2^{k-1})]\big) = \big(\text{rk}_{k-1}[v], \text{rk}_{k-1}[\text{anc}(v, 2^{k-1})]\big).$$
2. **Tie-Broken Permutation Rank $\text{id}_k[u] \in \{1, \dots, N\}$**: The inverse of the sorted array $\text{sa}_k[1..N]$ ($\text{id}_k[\text{sa}_k[i]] = i$).
- **Sorting at Step $k \to k+1$**: Order vertices by the **4-tuple**
  $$\big(\text{rk}_k[u],\; \text{rk}_k[\text{anc}(u, 2^k)],\; \text{id}_k[u],\; \text{id}_k[\text{anc}(u, 2^k)]\big),$$
  which is executed in **two stable $O(N)$ counting sorts**: first order by the second half using the already-distinct $\text{id}_k[\text{anc}(u, 2^k)]$ (with $\text{id}_k[0] = 0$), then stable-sort by $\text{rk}_k[u]$ (or $(\text{rk}_k[u], \text{id}_k[u])$).
- **$O(\log N)$ Tree LCP via Saved $\text{rk}_k$ Layers**: Storing $\text{rk}_k[u]$ for all $k = 0 \dots \lfloor \log_2 N \rfloor$ allows computing $\text{LCP}(S(u), S(v))$ for **any** two tree nodes $u, v$ in $O(\log N)$ time by binary lifting: for $k = \lfloor \log_2 N \rfloor$ down to $0$, if $\text{rk}_k[u] == \text{rk}_k[v]$, add $2^k$ to LCP and jump $u \leftarrow \text{anc}(u, 2^k),\; v \leftarrow \text{anc}(v, 2^k)$!

##### Invariant 4B: Leaf-Rooted Substring Cover (`[ZJOI2015] 诸神眷顾的幻想乡`)

> [!IMPORTANT]
> **Theorem 4.1 (Leaf-Rooted Substring Cover of Unrooted Trees)**
> Let $T$ be an unrooted tree with $|V| \ge 2$ and leaf set $\mathcal{L} = \{\ell \in V : \deg(\ell) = 1\}$. Every directed simple path $u \rightsquigarrow v$ in $T$ is a **contiguous substring** of a root-to-node path $\ell \rightsquigarrow v$ in the tree $T_\ell$ rooted at some leaf $\ell \in \mathcal{L}$.

**Proof**: Root $T$ at $v$. Walk from $u$ strictly deeper into $u$'s subtree (away from $v$) until reaching a node $\ell$ with no children. Then $\deg_T(\ell) = 1$ ($\ell \in \mathcal{L}$), and the unique simple path $\ell \rightsquigarrow v$ passes through $u$, so $\text{str}(u \rightsquigarrow v)$ is a suffix of $\text{str}(\ell \rightsquigarrow v)$. $\blacksquare$

Hence when $|\mathcal{L}| \le 20$, inserting all $|\mathcal{L}|$ leaf-rooted trees into a single **Generalized SAM (GSAM)** captures all $\binom{N}{2}$ path strings in at most $2 |\mathcal{L}| N \le 4 \cdot 10^6$ states!

##### Invariant 4C: Centroid Decomposition + Dual-SAM Split Convolution (`[CTSC2010] 珠宝商`)
When $|\mathcal{L}| = \Theta(N)$ and we want to sum the number of occurrences of $\text{str}(u \rightsquigarrow v)$ inside a text $S[1..M]$ over all $N^2$ pairs $(u, v)$:
- Build $\text{SAM}_S$ (for $S$) and $\text{SAM}_{S^R}$ (for $S^R$).
- At a centroid $c$ of component size $S_c$, every path $u \rightsquigarrow c \rightsquigarrow v$ splits at $c$. Set threshold $B = \sqrt{M}$:
  1. **Light Component ($S_c \le B$)**: Enumerate all $O(S_c^2)$ pairs $(u, v)$ directly by walking from $u$ through $c$ to $v$ in $\text{SAM}_S$ and adding $|\text{endpos}_S(q)|$ in $O(S_c^2)$ time.
  2. **Heavy Component ($S_c > B$)**: Walk downward from $c$ to all nodes in $c$'s component to count how many upward paths $u \rightsquigarrow c$ reach state $y \in \text{SAM}_{S^R}$ and how many downward paths $\text{next}(c, v) \rightsquigarrow v$ reach state $x \in \text{SAM}_S$. Push these node counts down the Link Trees of $\text{SAM}_{S^R}$ and $\text{SAM}_S$ to the prefix/suffix indices $i \in [1..M]$ of $S$, and sum $\text{up}[i] \cdot \text{down}[i+1]$ in $O(S_c + M)$ time!

---

#### Step 3 & Step 4: Algorithmic Contracts & Critical Tree-String Pitfalls

1. **Zero-Length Clone Avoidance in Tree GSAM (`[ZJOI2015]`)**:
   - Either traverse each rooted tree $T_\ell$ in **BFS order** (increasing depth), or at the very top of `extend(p, c)` check `if (ch[p][c])`: if `len[q] == len[p] + 1`, return `q` immediately; if `len[q] > len[p] + 1`, split `q` into `clone` with `len[clone] = len[p] + 1` and return `clone` **without allocating a new node `cur`**!
2. **The Child-Subtree Subtraction Threshold Bug in `[CTSC2010] 珠宝商` (Cohort 2 Discovery)**:
   - When $S_c > B = \sqrt{M}$, the all-pairs sum $\sum_{i=1}^M \text{up}[i] \cdot \text{down}[i+1]$ over $c$'s component includes invalid non-simple paths where $u$ and $v$ lie in the **same child subtree $T_{\text{sub}}$** of $c$.
   - **Fatal Bug**: If you subtract each child subtree $T_{\text{sub}}$ by running the $O(|T_{\text{sub}}| + M)$ Link-Tree pushdown on *every* child subtree of $c$, then a star-like centroid $c$ with $S_c = N$ and $N-1$ leaf children of size $1$ will execute $O(M)$ Link-Tree sweeps $N-1$ times, **blowing up to $O(NM)$ TLE**!
   - **Fix**: Apply the exact same threshold $B = \sqrt{M}$ to each child subtree $T_{\text{sub}}$ during subtraction: if $|T_{\text{sub}}| \le B$, subtract its internal pairs via the $O(|T_{\text{sub}}|^2)$ direct walk; only run the $O(|T_{\text{sub}}| + M)$ Link-Tree sweep when $|T_{\text{sub}}| > B$! Since $\sum_{|T_{\text{sub}}| > B} 1 < \frac{N \log N}{B}$, total time across the entire centroid tree is strictly bounded by $O(N \sqrt{M} + M \sqrt{N} \log N)$.
3. **Amortized KMP Failure-Link Hazard on Branched Trees (`CF 291E`)**:
   - Running standard `while (q && P[q+1] != c) q = pi[q]` during a tree DFS is **not** amortized $O(1)$ per edge: a node $u$ with $q = |P| - 1$ can have $N/2$ leaf children that each force $O(|P|)$ fallback steps, degrading to $O(N |P|)$! Always precompute the deterministic KMP automaton $\delta(q, c)$ (or use `slink` jumping in $O(\log |P|)$ when $|\Sigma|$ is huge or RLE-compressed as in `[HNOI2019] JOJO`).

---

### 4.3 Master Algorithmic Contracts (Signed Binary-Lifting DSU & Dual-Rank Tree SA)

#### Contract 4.1: Signed Binary-Lifting DSU with Root Self-Palindrome Bit (`is_pal[k][r]`)
```text
// State: fa[0..K][1..N], rev[0..K][1..N] in {0, 1}, is_pal[0..K][1..N] in {0, 1}
procedure FIND(k, u):
    if fa[k][u] == u: return (u, 0)
    (r, d) <- FIND(k, fa[k][u])
    fa[k][u] <- r
    rev[k][u] <- rev[k][u] xor d
    return (r, rev[k][u])

procedure UNITE(k, u, v, d):
    (ru, du) <- FIND(k, u)
    (rv, dv) <- FIND(k, v)
    if ru == rv:
        if (du xor dv xor d) == 1:
            is_pal[k][ru] <- 1   // Self-reversal loop on root ru!
        return
    fa[k][ru] <- rv
    rev[k][ru] <- du xor dv xor d
    is_pal[k][rv] <- is_pal[k][rv] or is_pal[k][ru]

procedure PUSHDOWN_ALL(N, K):
    for k = K down to 1:
        half <- 2^(k - 1)
        // Pass 1: Push down root self-palindrome constraints first
        for r = 1 to N - 2^k + 1:
            if fa[k][r] == r and is_pal[k][r] == 1:
                UNITE(k - 1, r, r + half, 1)
        // Pass 2: Push down spanning-forest edges
        for i = 1 to N - 2^k + 1:
            (r, d) <- FIND(k, i)
            if r != i:
                if d == 0:
                    UNITE(k - 1, i, r, 0)
                    UNITE(k - 1, i + half, r + half, 0)
                else:
                    UNITE(k - 1, i, r + half, 1)
                    UNITE(k - 1, i + half, r, 1)
```

#### Contract 4.2: Dual-Rank Tree Suffix Array + $O(\log N)$ Tree LCP
```text
// Input: Rooted tree T (1..N), parent anc[0][u], character c[u]
// Output: sa[1..N], saved equivalence ranks rk[0..K][1..N], and adjacent height[2..N]
procedure BUILD_TREE_SA(N, K):
    // Step 0: Counting sort by c[u]; set rk[0][u] = rank of c[u] (equal iff c[u] == c[v]), id[sa[i]] = i
    for k = 0 to K - 1:
        // 1. Bucket vertices by second-half tie-broken rank id[anc[k][u]] (0 if anc[k][u] == 0)
        // 2. Stable counting sort by primary first-half key rk[k][u] (breaking ties by id[u]) -> sa[1..N]
        rk[k + 1][sa[1]] <- 1
        for i = 2 to N:
            u <- sa[i - 1]; v <- sa[i]
            same_1 <- (rk[k][u] == rk[k][v])
            same_2 <- (rk[k][anc[k][u]] == rk[k][anc[k][v]])
            rk[k + 1][v] <- rk[k + 1][u] + (0 if (same_1 and same_2) else 1)
        for i = 1 to N: id[sa[i]] <- i

function TREE_LCP(u, v, K):
    lcp <- 0
    for k = K down to 0:
        if u != 0 and v != 0 and rk[k][u] == rk[k][v]:
            lcp <- lcp + 2^k
            u <- anc[k][u]; v <- anc[k][v]
    return lcp
```

---

## 5. Master Reconciled Non-Template Problem Archive (`W5A-01` to `W5A-48`)

All accepted non-template problems from Cohort 1 (`P-5A-01..32`) and Cohort 2 (`Iter 97 #1..32`) have been deduplicated, cross-verified, and unified into a **48-problem 4-Tier Smooth Difficulty Ladder** (`Tier 1: Stepping Stone` $\to$ `Tier 2: Intermediate` $\to$ `Tier 3: Advanced` $\to$ `Tier 4: Mastery`), each with its full **4-Step Zero-Magic Analysis**.

---

### Tier 1: Stepping Stones (`W5A-01` to `W5A-12` — Foundational Reductions & Inverse Array Dualities)

#### W5A-01. `[ZH]` `[SCOI2016] 萌萌哒` (`Luogu P3295` / `BZOJ 4567`) — *[Cohort 1 P-5A-01 + Cohort 2 #1]*
- **Topic**: Binary-Lifting DSU (`倍增并查集`) for Substring Equality Constraints.
- **Statement & Constraints**: Given string length $N \le 10^5$ and $M \le 10^5$ substring equality constraints $S[l_1..r_1] = S[l_2..r_2]$ ($r_1 - l_1 = r_2 - l_2$), count the number of valid decimal strings $S \in \{0..9\}^N$ with $S[1] \neq 0$ modulo $10^9+7$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $M$ range equalities of length up to $N$ make naive $O(NM \alpha(N))$ pointwise DSU TLE.
  2. *Combinatorial Invariant*: By Theorem 1.1, each equality of length $L$ splits losslessly into two overlapping ST-table blocks of length $2^k$ ($k = \lfloor \log_2 L \rfloor$) at level $k$.
  3. *Compilation*: Unite endpoints at level $k$; sweep $k = \lfloor \log_2 N \rfloor$ down to $1$ calling `unite(k-1, i, r)` and `unite(k-1, i + 2^{k-1}, r + 2^{k-1})`. With $C$ connected components at level $0$, output $9 \cdot 10^{C-1} \bmod (10^9+7)$.
  4. *Pitfall*: Pushing down all pairs in a component instead of only $(i, \text{find}_k(i))$ degrades back to $O(N^2)$.

#### W5A-02. `[EN]` `CF 1526E — Oolimry and Suffix Array` — *[Cohort 1 P-5A-02 + Cohort 2 #2]*
- **Topic**: Inverse Suffix Array Characterization & Stars-and-Bars Counting.
- **Statement & Constraints**: Given the Suffix Array $\text{SA}[0..N-1]$ of length $N \le 2 \cdot 10^5$ and alphabet size $K \le 2 \cdot 10^5$, count how many strings $S \in \Sigma^N$ have suffix array $\text{SA}$ modulo $998244353$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Counting valid character assignments along SA order without LCP values.
  2. *Combinatorial Invariant*: By Theorem 2.1 (SA Adjacency Theorem), $S[\text{SA}[i]] = S[\text{SA}[i+1]]$ is permitted iff $\text{rk}[\text{SA}[i]+1] < \text{rk}[\text{SA}[i+1]+1]$ (with $\text{rk}[N] = -1$).
  3. *Compilation*: Count forced strict steps $D = \sum_{i=0}^{N-2} [\text{rk}[\text{SA}[i]+1] > \text{rk}[\text{SA}[i+1]+1]]$. By stars-and-bars, the number of valid strings is $\binom{N + K - 1 - D}{N}$ in $O(N)$ time.
  4. *Pitfall*: Forgetting the empty-suffix sentinel $\text{rk}[N] = -1$, which corrupts the transition at $\text{SA}[i] = N-1$.

#### W5A-03. `[JA]` `AtCoder ARC 044 D — 文字列と辞書順 (String and Lexicographical Order)` — *[Cohort 2 #5]*
- **Topic**: Pointwise Minimal Inverse Suffix Array Reconstruction.
- **Statement & Constraints**: Given a permutation $\text{SA}[1..N]$ ($N \le 10^6$), construct the lexicographically smallest uppercase string $S$ whose suffix array is $\text{SA}$, or output `-1` if $> 26$ letters are required.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Direct constructive counterpart to `W5A-02`.
  2. *Combinatorial Invariant*: By Theorem 2.1, setting $S[\text{SA}[i+1]] = S[\text{SA}[i]] + [\text{rk}[\text{SA}[i]+1] > \text{rk}[\text{SA}[i+1]+1]]$ achieves the minimum alphabet size and lexicographically smallest string simultaneously.
  3. *Compilation*: Compute $\text{rk}[1..N+1]$ with $\text{rk}[N+1] = 0$, accumulate mandatory $+1$ jumps in $O(N)$, and place characters back into $S[\text{SA}[i]]$.
  4. *Pitfall*: Printing characters in SA order $i = 1..N$ instead of original string order $S[1..N]$.

#### W5A-04. `[EN]` `CF 508D — Tanya and Password` — *[Cohort 1 P-5A-03 + Cohort 2 #4]*
- **Topic**: De Bruijn Graph Eulerian Trail Reconstruction ($k = 3$).
- **Statement & Constraints**: Given $N \le 2 \cdot 10^5$ substrings of length $3$ over `[a-zA-Z0-9]` ($|\Sigma| = 62$), reconstruct a string of length $N+2$ whose $3$-mers match the input multiset, or report `NO`.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Exact $3$-mer spectrum reconstruction.
  2. *Combinatorial Invariant*: Each $3$-mer $c_1 c_2 c_3$ is a directed edge $c_1 c_2 \to c_2 c_3$ in $\mathcal{B}(\Sigma, 3)$ on $62^2 = 3844$ vertices. Valid strings correspond bijectively to Eulerian trails.
  3. *Compilation*: Check Eulerian trail degree conditions ($\text{out}(v) - \text{in}(v) \in \{-1, 0, 1\}$, at most one $+1$ start vertex) and run Hierholzer's algorithm in $O(N)$.
  4. *Pitfall*: Disconnected Eulerian components when the graph has both a valid trail component and an isolated cycle; must verify $|E_{\text{walk}}| == N$.

#### W5A-05. `[ZH]` `[SDOI2017] 字符串 / Inverse KMP Reconstruction` (`BZOJ 4974` / `LOJ 2143` / `Luogu P4998`) — *[Cohort 1 P-5A-05 + Cohort 2 #3]*
- **Topic**: Inverse KMP Prefix-Function String Reconstruction (`per[i] = i - pi[i]`).
- **Statement & Constraints**: Given the shortest prefix period array $\text{per}[1..N]$ (or KMP array $\pi[1..N] = i - \text{per}[i]$, $N \le 2 \cdot 10^5$), construct the lexicographically smallest lowercase string $S$ realizing $\pi$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $\pi[i]$ encodes both character equalities and ancestor mismatch inequalities.
  2. *Combinatorial Invariant*: If $\pi[i] > 0$, $S[i] = S[\pi[i]]$ is forced. If $\pi[i] = 0$, $S[i]$ must differ from $S[q + 1]$ for all $q \in \text{FailChain}(\pi[i-1])$ and from $S[1]$.
  3. *Compilation*: Sweep $i = 1..N$; when $\pi[i] = 0$, walk $q \leftarrow \pi[q]$ from $\pi[i-1]$, mark $S[q+1]$ in a 26-bit forbidden mask, and assign the smallest free letter. Total work is $O(N)$ by KMP potential analysis.
  4. *Pitfall*: If input validity is not guaranteed, run forward KMP on the reconstructed $S$ to verify $\pi_{\text{actual}}(S) == \pi_{\text{input}}$.

#### W5A-06. `[EN]` `CF 827A — String Reconstruction` — *[Cohort 1 P-5A-04]*
- **Topic**: Pointwise Substring Placement via DSU Next-Uncovered Jump.
- **Statement & Constraints**: Given $N \le 10^5$ strings $t_i$ and positions $x_{i, j}$ where $t_i$ occurs in $S$ ($\sum |t_i|, \max x \le 2 \cdot 10^6$), reconstruct the lexicographically smallest valid $S$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Overlapping placements of $t_i$ copy ranges into $S$; naive range copying takes $O(L^2)$.
  2. *Combinatorial Invariant*: Each index $p \in [1, L]$ only needs to be written **once**; a DSU `find_next(p)` jumps over already-assigned contiguous intervals in $O(\alpha(L))$.
  3. *Compilation*: For each placement $[x, x + |t_i| - 1]$, iterate $p = \text{find}(x)$ while $p < x + |t_i|$, set $S[p] = t_i[p - x + 1]$, and unite $p \to p + 1$.
  4. *Pitfall*: Unassigned indices must be filled with `'a'`, not left as `'\0'`.

#### W5A-07. `[EN]` `CF 1051E — Vasya and Big Integers` — *[Cohort 1 P-5A-06]*
- **Topic**: Substring Lexicographical Inequality $L \le S[l..r] \le R$ via Z-Algorithm LCE + DP.
- **Statement & Constraints**: Partition digit string $A[1..N]$ ($N \le 10^6$) into substrings each satisfying $L \le A[l..r] \le R$ as big integers without leading zeros, modulo $998244353$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Comparing $A[l..l+|L|-1]$ against $L$ and $R$ naively takes $O(|L|)$ per DP state.
  2. *Combinatorial Invariant*: By the LCP Witness Decomposition (`§2.2`), $A[l..l+|L|-1] \ge L$ is decided in $O(1)$ at the first mismatch $t = Z_L(l)$ via $A[l+t] > L[1+t]$.
  3. *Compilation*: Precompute Z-arrays of $L \# A$ and $R \# A$; transition DP via prefix sums over valid lengths $[|L|, |R|]$ in $O(N)$ time.
  4. *Pitfall*: Single-digit `"0"` is valid if $L = \text{"0"}$, whereas multi-digit substrings starting with `'0'` are always forbidden.

#### W5A-08. `[EN]` `CF 291E — Tree-String Problem` — *[Cohort 1 P-5A-07]*
- **Topic**: Deterministic KMP Automaton on Rooted Tree Paths.
- **Statement & Constraints**: Given a rooted tree with strings on edges ($\sum |s_e| \le 3 \cdot 10^5$) and pattern $P$, count occurrences of $P$ along root-to-node downward paths.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Amortized KMP fail-link traversal (`while (q && P[q+1] != c) q = pi[q]`) degrades to $O(|P|)$ per branching child on a tree!
  2. *Combinatorial Invariant*: Precomputing the KMP DFA $\delta(q, c)$ makes every character transition worst-case $O(1)$, eliminating branching rollback cost.
  3. *Compilation*: Build $\delta[0..|P|][0..25]$ in $O(|P| |\Sigma|)$; DFS the tree passing state $q$ in $O(\sum |s_e|)$.
  4. *Pitfall*: Using amortized `while` loops without $\delta(q, c)$ TLEs on a broom tree where a node with $q = |P|-1$ has $10^5$ leaf children.

#### W5A-09. `[JA]` `AtCoder ABC 272 F — Two Strings` — *[Cohort 1 P-5A-08]*
- **Topic**: Suffix Array Lexicographical Comparison of All Cyclic Shifts (`BWT` / Doubled SA).
- **Statement & Constraints**: Given strings $S, T$ of length $N \le 2 \cdot 10^5$, count pairs $(i, j) \in [1..N]^2$ such that the $i$-th cyclic shift $S_i$ satisfies $S_i \le T_j$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Comparing $N^2$ pairs of length-$N$ cyclic shifts directly is $O(N^3)$.
  2. *Combinatorial Invariant*: Concatenating $S \cdot S \cdot \text{\texttt{a}} \cdot T \cdot T \cdot \text{\texttt{z}}$ orders all cyclic shifts of $S$ and $T$ simultaneously in one SA of length $4N+2$.
  3. *Compilation*: Sweep the SA and count how many valid $S$-shift starts ($1..N$) precede each valid $T$-shift start ($2N+2..3N+1$).
  4. *Pitfall*: Tie-breaking when $S_i == T_j$: placing `'a'` after $S \cdot S$ and `'z'` after $T \cdot T$ guarantees $S_i$ sorts before $T_j$ on exact length-$N$ ties!

#### W5A-10. `[EN]` `BOI 2004 REPEATS / CSES 1113 — String Transform (Inverse BWT)` — *[Cohort 1 P-5A-13 + Cohort 2 #6]*
- **Topic**: Inverse Burrows–Wheeler Transform via LF-Mapping Cycle Reconstruction.
- **Statement & Constraints**: Given the BWT string $L[1..N]$ ($N \le 10^6$) containing sentinel `#` (or row index $I$), reconstruct the original string $S$ in $O(N)$ time.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Rebuilding the $N \times N$ cyclic shift matrix takes $O(N^2)$ time and memory.
  2. *Combinatorial Invariant*: By Theorem 3.2 (LF-Mapping), the $k$-th occurrence of $c$ in $L$ is the exact same character in $S$ as the $k$-th occurrence of $c$ in $F$, so $\text{LF}(i) = C[L[i]] + \text{Occ}(L[i], i)$ steps backward by $1$ position in $S$ (and its inverse stable-sort permutation $\text{FL}(i)$ steps forward by $1$).
  3. *Compilation*: Compute stable counting-sort mapping in $O(N)$ and follow the cycle from `#` for $N-1$ steps.
  4. *Pitfall*: Non-stable sorting on ties splits the Hamiltonian cycle of $S$ into disjoint sub-cycles!

#### W5A-11. `[ZH]` `[POI 2000] 公共串` (`Luogu P5546`) — *[Cohort 2 #8]*
- **Topic**: Multi-String Longest Common Substring via BFS Generalized SAM.
- **Statement & Constraints**: Find the longest common substring of $K \le 5$ strings (scalable to $\sum |S_i| \le 5 \cdot 10^5$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Foundation for Tree GSAM (`W5A-25`).
  2. *Combinatorial Invariant*: In the BFS Generalized SAM of $\{S_1, \dots, S_K\}$, state $u$ occurs in $S_j$ iff its Link-Tree subtree contains a prefix node of $S_j$.
  3. *Compilation*: Build BFS GSAM, propagate a $K$-bit occurrence mask up the Link Tree in topological order, and take $\max \{\text{len}(u) : \text{mask}[u] = 2^K - 1\}$.
  4. *Pitfall*: Online DFS GSAM without checking existing transitions creates zero-length clones that corrupt $\text{len}(u)$.

#### W5A-12. `[EN]` `CF 535D — Tavas and Malekas` — *[Cohort 1 P-5A-11a]*
- **Topic**: Self-Overlap Consistency via Z-Array + Unconstrained Component Counting.
- **Statement & Constraints**: Given string length $N \le 10^6$, pattern $P[1..M]$, and positions $y_1 < y_2 < \dots < y_k$ where $P$ must occur in $S$, count valid strings $S \in \{\text{'a'}..\text{'z'}\}^N$ modulo $10^9+7$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Consecutive placements $y_i, y_{i+1}$ with $y_i + M - 1 \ge y_{i+1}$ force $P$ to match a shifted copy of itself on an overlap of length $L = y_i + M - y_{i+1}$.
  2. *Combinatorial Invariant*: $P[1..M]$ agrees with itself at shift $d = y_{i+1} - y_i$ iff $Z_P[d + 1] \ge M - d$.
  3. *Compilation*: Precompute $Z_P[1..M]$ in $O(M)$, check all adjacent overlaps $y_{i+1} - y_i < M$ in $O(1)$ each, count uncovered positions $C$, and output $26^C \bmod (10^9+7)$.
  4. *Pitfall*: Only checking adjacent placements $y_i, y_{i+1}$ suffices because if $y_i$ overlaps $y_{i+2}$, it also overlaps $y_{i+1}$ and transitivity of equality handles $y_i \cap y_{i+2}$!

---

### Tier 2: Intermediate (`W5A-13` to `W5A-24` — Signed DSU, 2-SAT Inequalities, De Bruijn DP & Tree SA Queries)

#### W5A-13. `[EN]` `CF 568C — New Language` — *[Cohort 1 P-5A-09 + Cohort 2 #10]*
- **Topic**: Lexicographical Lower Bound $S \ge S_0$ + 2-SAT Alphabet Implication Graph.
- **Statement & Constraints**: Alphabet $\Sigma$ ($|\Sigma| \le 26$) is partitioned into Vowels (`V`) and Consonants (`C`). Given $M \le 400^2$ implication rules $(i, t_1) \implies (j, t_2)$ and reference string $S_0$ ($N \le 200$), find the lexicographically smallest valid string $S \ge S_0$, or report `-1`.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $S \ge S_0$ couples a non-local lexicographical comparison with $O(N^2)$ 2-SAT implications.
  2. *Combinatorial Invariant*: Branch on the exact LCP length $d \in [0, N]$ where $S[1..d] = S_0[1..d]$ and $S[d+1] > S_0[d+1]$. Since 2-SAT only cares about the binary type (`V` vs. `C`) of each position, at $d+1$ we only need to test at most **two** candidate characters: the smallest `V` $> S_0[d+1]$ and the smallest `C` $> S_0[d+1]$!
  3. *Compilation*: Iterate $d = N$ down to $0$; test 2-SAT feasibility in $O(N + M)$, and once a valid $d$ is found, greedily fill $i = d+2..N$ left-to-right.
  4. *Pitfall*: If the entire alphabet $\Sigma$ contains only Vowels (zero Consonants), then type `C` is unconditionally false: you **must** add unary clauses $x_i \to \neg x_i$ for the empty class!

#### W5A-14. `[EN]` `[ZH]` `[JA]` `Signed Palindrome & Substring Equations` (`AtCoder ABC 259 Ex` / `CF Gym 102900K` / `LOJ 6073`) — *[Cohort 1 P-5A-10 + Cohort 2 #11]*
- **Topic**: Signed Binary-Lifting DSU (`带权倍增并查集`) for Simultaneous Translation & Palindrome Constraints.
- **Statement & Constraints**: Given $N \le 2 \cdot 10^5$, $M_1$ substring equalities $S[l_1..r_1] = S[l_2..r_2]$, and $M_2$ palindrome/reversal constraints $S[l_1..r_1] = S[l_2..r_2]^R$, count valid strings over $\Sigma$ modulo $998244353$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Simultaneous forward and reversed block equalities require relative orientation tracking.
  2. *Combinatorial Invariant*: By Theorem 1.1 and Contract 4.1, each level-$k$ DSU edge carries parity $d \in \{0, 1\}$ and each root $r$ carries a self-palindrome bit `is_pal[k][r]`. Pushing down $d = 1$ swaps the half-block offsets: $(i, r + 2^{k-1}, 1)$ and $(i + 2^{k-1}, r, 1)$.
  3. *Compilation*: Run Contract 4.1 from $k = 17$ down to $1$ in $O((M + N \log N)\alpha(N))$ time; output $|\Sigma|^C$.
  4. *Pitfall*: Failing to record `is_pal[k][ru] = 1` when `ru == rv` and `(du ^ dv ^ d) == 1` drops palindrome constraints on root blocks (see `§1.2 Pitfall 1`).

#### W5A-15. `[EN]` `Inverse Z-Array + Manacher Joint Reconstruction` (`CF Gym 102001` / `Gym 101981I`) — *[Cohort 1 P-5A-11b + Cohort 2 #7]*
- **Topic**: Signed Binary-Lifting DSU + Conflict Graph Verification for Joint Z & Manacher Arrays.
- **Statement & Constraints**: Given $Z[1..N]$ and/or Manacher radii $R[1..2N-1]$ ($N \le 10^5$), construct the lexicographically smallest string $S$ matching the given arrays or report impossible.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $O(N)$ prefix-equality blocks and palindrome-reversal blocks coexist with $O(N)$ boundary mismatch constraints $S[u] \neq S[v]$.
  2. *Combinatorial Invariant*: Every $Z[i]$ induces forward equality $S[1..Z[i]] = S[i..i+Z[i]-1]$ and mismatch $S[1+Z[i]] \neq S[i+Z[i]]$; every Manacher radius $R[c]$ induces palindrome $S[l..r] = S[l..r]^R$ and mismatch $S[l-1] \neq S[r+1]$ (and for Manacher alone, linear sweep of $r_{\max}$ merges only $O(N)$ new pairs!).
  3. *Compilation*: Contract equalities via Signed DSU (or linear sweep), greedily assign smallest valid letters avoiding conflict neighbors, and **re-run forward Z and Manacher** in $O(N)$ to verify exact equality.
  4. *Pitfall*: Skipping the forward Z/Manacher verification step falls prey to the Phantom Equality & Chromatic Number Trap (`§2.2 Pitfall 1`).

#### W5A-16. `[JA]` `AtCoder ABC 197 F — Construct a Palindrome` — *[Cohort 1 P-5A-14]*
- **Topic**: Bidirectional Palindrome Walk on Edge-Labeled Graphs.
- **Statement & Constraints**: Given an undirected graph with $N \le 1000$ vertices and $M \le 1000$ character-labeled edges, find the shortest walk from $1$ to $N$ whose edge labels form a palindrome, or output `-1`.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Palindrome symmetry couples the $k$-th step from $1$ with the $k$-th step backward from $N$.
  2. *Combinatorial Invariant*: A palindromic walk in $G$ corresponds to a shortest path in the product graph $V \times V$ starting at $(1, N)$ along identically labeled edge pairs $(u \xrightarrow{c} u', v \xrightarrow{c} v')$, terminating at $(u, u)$ (even length $2d$) or $(u, v) \in E$ (odd length $2d+1$).
  3. *Compilation*: BFS on $N^2$ states $(u, v)$ in $O(N^2 + M^2)$ time.
  4. *Pitfall*: Must check both even-length meeting $(u, u)$ and odd-length edge meeting $(u, v) \in E$ across all states.

#### W5A-17. `[EN]` `CF 1152F2 — Neko Rules the Catniverse (Large Version)` — *[Cohort 1 P-5A-15]*
- **Topic**: De Bruijn Window State Compression + Matrix Exponentiation.
- **Statement & Constraints**: Count sequences of length $K \le 12$ of distinct integers from $\{1..N\}$ ($N \le 10^9$) where $a_{i+1} \le a_i + m$ ($m \le 4$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Inserting elements in increasing value order $x = 1..N$ only depends on which of the last $m$ integers $[x-m .. x-1]$ are present in the sequence.
  2. *Combinatorial Invariant*: Maintain the $m$-bit De Bruijn vertex $\text{mask} \in \mathcal{B}(\{0,1\}, m)$ of active elements in $[x-m..x-1]$. Element $x$ can either be placed at the very start of the sequence or immediately after any of the $\text{popcount}(\text{mask})$ active elements in $[x-m..x-1]$, giving $1 + \text{popcount}(\text{mask})$ ways!
  3. *Compilation*: Build a $(K+1) \cdot 2^m \le 208$ state transition matrix and exponentiate to power $N$ in $O((K 2^m)^3 \log N)$.
  4. *Pitfall*: The window mask shifts `(mask << 1) & ((1 << m) - 1)` at **every** step $x \to x+1$, even when $x$ is not chosen.

#### W5A-18. `[JA]` `Tree Upward Substring Lexicographical Queries` (`ARC 116 E` / `Luogu P5353` Query Extension) — *[Cohort 1 P-5A-12 + Cohort 2 #15]*
- **Topic**: Dual-Rank Tree Suffix Array + $O(\log N)$ Binary-Lifting LCP for Tree Substring Comparisons.
- **Statement & Constraints**: Given a rooted tree $T$ ($N \le 2 \cdot 10^5$) with character-labeled vertices, answer $Q \le 2 \cdot 10^5$ queries comparing upward path substrings $\text{str}(u_1 \uparrow L_1)$ and $\text{str}(u_2 \uparrow L_2)$ lexicographically.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Whole-path Tree SA ranks cannot compare truncated upward substrings of lengths $L_1, L_2$ directly if their LCP is shorter or longer than $\min(L_1, L_2)$.
  2. *Combinatorial Invariant*: By Contract 4.2, storing all $\lfloor \log_2 N \rfloor + 1$ layers of the **true string equivalence rank** $\text{rk}_k[u]$ during Tree SA construction allows computing $d = \text{LCP}(S(u_1), S(u_2))$ in $O(\log N)$ via binary lifting!
  3. *Compilation*: Build Dual-Rank Tree SA saving `rk[0..K][1..N]`. For each query, compute $d = \text{TREE\_LCP}(u_1, u_2, K)$; if $d \ge \min(L_1, L_2)$, compare lengths $L_1$ vs. $L_2$; otherwise compare $c(\text{anc}(u_1, d))$ vs. $c(\text{anc}(u_2, d))$.
  4. *Pitfall*: Using tie-broken `id[u]` instead of `rk[k][u]` during binary lifting stops prematurely when two distinct nodes have identical $2^k$-prefixes!

#### W5A-19. `[ZH]` `[USACO12DEC] First! G` (`Luogu P3065`) — *[Cohort 1 P-5A-16]*
- **Topic**: Lexicographical Constraint Graph on a Trie (Alphabet Permutation Feasibility).
- **Statement & Constraints**: Given $N \le 3 \cdot 10^4$ strings of total length $\le 3 \cdot 10^5$, determine which strings $S_i$ can become strictly lexicographically smallest among all $N$ strings under some permutation of `a-z`.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Comparing $S_i$ against all $N-1$ strings individually takes $O(N^2)$.
  2. *Combinatorial Invariant*: On the Trie of $\{S_1, \dots, S_N\}$, every string $S_j \neq S_i$ diverges from $S_i$ at their exact LCA on thepath of $S_i$! Thus walking $S_i$ down the Trie and adding directed edges $S_i[d] \to c'$ for all existing sibling transitions $c' \neq S_i[d]$ captures **all** $N-1$ comparisons in $O(|S_i| \cdot |\Sigma|)$!
  3. *Compilation*: For each $S_i$, build its $26$-vertex alphabet graph along its Trie path and test for cycles (plus reject if any shorter string $S_j$ ends at a proper ancestor of $S_i$).
  4. *Pitfall*: If $S_j$ is a proper prefix of $S_i$, $S_j < S_i$ under **every** alphabet permutation!

#### W5A-20. `[EN]` `CF 1361C — Johnny and Megan's Necklace` — *[Cohort 1 P-5A-23 + Cohort 2 #13]*
- **Topic**: Binary Search on $k$-Bit Overlap + Eulerian Circuit in Induced De Bruijn Graph.
- **Statement & Constraints**: Given $N \le 5 \cdot 10^5$ pairs of integers $(a_i, b_i)$, arrange them into a cycle maximizing the number of shared trailing binary bits $k \in [0, 20]$ between adjacent pairs.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Sharing $k$ trailing bits means $u \equiv v \pmod{2^k}$.
  2. *Combinatorial Invariant*: Modulo $2^k$, each pair $(a_i, b_i)$ is an undirected edge between $(a_i \bmod 2^k)$ and $(b_i \bmod 2^k)$ on $2^k$ vertices. A valid cycle exists iff all active vertices have even degree and form a single connected component.
  3. *Compilation*: Binary search $k \in [0, 20]$ and reconstruct the Eulerian circuit via Hierholzer's algorithm in $O(N + 2^k)$.
  4. *Pitfall*: Outputting the $2N$ endpoints in the exact traversal orientation $(2i-1, 2i)$ vs. $(2i, 2i-1)$ along the Eulerian circuit.

#### W5A-21. `[ZH]` `[JSOI2015] 串分割` (`Luogu P6095`) — *[Cohort 2 #14]*
- **Topic**: Circular String Partition Minimizing Maximum Lexicographical Piece via SA.
- **Statement & Constraints**: Partition a circular digit string of length $N \le 2 \cdot 10^5$ into $K$ pieces minimizing the lexicographically largest piece.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: By length dominance (no leading zeros/equal digit lengths), the maximum piece must have length $L = \lceil N/K \rceil$.
  2. *Combinatorial Invariant*: Sort all $N$ cyclic substrings of length $L$ via SA of $S \cdot S$. Binary search the threshold rank $R$: for a fixed $R$, every starting position $i$ can advance by $L$ if $\text{rk}[i] \le R$, or by $L-1$ otherwise.
  3. *Compilation*: Since the first piece has length $\le L$, try all $L$ starting offsets in $[1, L]$ and greedily take steps of $L$ or $L-1$ for $K$ pieces; total time $O(K \cdot L) = O(N)$ per binary search step!
  4. *Pitfall*: Using $\text{rk}[i] \le R$ instead of comparing the length-$L$ LCP when two suffixes share the same length-$L$ prefix: must compare $\text{LCP}(\text{SA}[R], i) \ge L$ or $\text{rk}[i] \le R$!

#### W5A-22. `[JA]` `AtCoder AGC 047 B — First Second` — *[Cohort 1 P-5A-24]*
- **Topic**: Reversed Trie (Co-Lexicographical Suffix Tree) + Prefix Character Mask Counting.
- **Statement & Constraints**: Given $N \le 2 \cdot 10^5$ strings ($\sum |S_i| \le 10^6$), an operation replaces the first two characters of a string by either one of them. Count pairs $(i, j)$ such that $S_i$ can be reduced to $S_j$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Repeatedly deleting the 1st or 2nd character keeps the suffix $S_i[|S_i| - |S_j| + 2 .. |S_i|]$ intact and replaces the prefix $S_i[1 .. |S_i| - |S_j| + 1]$ by any single character appearing in that prefix!
  2. *Combinatorial Invariant*: $S_i \to^* S_j$ iff $S_j[2..|S_j|]$ is a suffix of $S_i$ and $S_j[1] \in \text{set}(S_i[1 .. |S_i| - |S_j| + 1])$.
  3. *Compilation*: Insert all $S_i^R$ into a Trie; at the exact step $k$ where $c = S_i[k]$ makes its *first* appearance in $S_i[1..k]$, increment `cnt[node_at_k+1][c]`. Query `cnt[node(S_j[2..]^R)][S_j[1]]` in $O(\sum |S_i|)$.
  4. *Pitfall*: Updating all $26$ bits at every node takes $26 \sum |S_i|$; only increment `cnt[node][c]` when `mask` changes or at the suffix boundary!

#### W5A-23. `[EN]` `CSAcademy — Substring Restrictions` (`CF Gym 102059`) — *[Cohort 1 P-5A-21]*
- **Topic**: Online Recursive Binary-Lifting DSU (`merge_block(k, i, j)`) with Early-Exit Potential.
- **Statement & Constraints**: Given $N \le 10^5$ and $M \le 10^5$ online queries asserting $S[l_1..l_1+L-1] = S[l_2..l_2+L-1]$, output $26^C \bmod (10^9+7)$ after **every** query.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Offline top-down pushdown cannot report intermediate component counts $C$ after each query.
  2. *Combinatorial Invariant*: By Theorem 1.2, recursive `merge_block(k, i, j)` short-circuits whenever `find(k, i) == find(k, j)`, bounding total productive calls across all $M$ queries by $N(\lfloor \log_2 N \rfloor + 1)$.
  3. *Compilation*: Split each online query into two $2^k$-blocks and invoke `merge_block(k, i, j)`; at $k = 0$, decrement $C$. Total time $O((M + N \log N)\alpha(N))$.
  4. *Pitfall*: Splitting into non-power-of-two lengths breaks level alignment; always split into $2^k$-blocks at level $k = \lfloor \log_2 L \rfloor$.

#### W5A-24. `[JA]` `AtCoder ARC 050 D — Suffix Concatenation` — *[Cohort 1 P-5A-32]*
- **Topic**: Lexicographical Concatenation Ordering of Suffixes ($S_i + S_j < S_j + S_i$) via 2-Step LCP.
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), arrange all $N$ suffixes $S_i = S[i..N]$ to minimize their concatenation $S_{p_1} S_{p_2} \dots S_{p_N}$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Comparing $S_i + S_j$ vs. $S_j + S_i$ naively takes $O(N)$ per comparison in `std::sort`.
  2. *Combinatorial Invariant*: For $i < j$ ($|S_i| > |S_j|$, $L_1 = N - j + 1$): first check $t_1 = \text{LCP}(i, j)$. If $t_1 < L_1$, order by $\text{rk}[i]$ vs. $\text{rk}[j]$. If $t_1 \ge L_1$, compare the remaining aligned segment $S[i + L_1 .. N]$ against $S[i .. N - L_1]$ via $t_2 = \text{LCP}(i + L_1, i)$!
  3. *Compilation*: Build SA + RMQ on `height`; sort $\{1..N\}$ with the $O(1)$ comparator in $O(N \log N)$ time.
  4. *Pitfall*: In the second step, if $\text{LCP}(i + L_1, i) \ge j - i$, then $S_i + S_j == S_j + S_i$ are strictly equal (since the final $L_1$ characters of both are $S[j..N]$!), so the comparator **must** return `false` to satisfy strict weak ordering!

---

### Tier 3: Advanced (`W5A-25` to `W5A-36` — Tree GSAM, Centroid + Palindrome/AC, BEST Theorem & Inequality SCCs)

#### W5A-25. `[ZH]` `[ZJOI2015] 诸神眷顾的幻想乡` (`Luogu P3346` / `BZOJ 3926`) — *[Cohort 1 P-5A-17 + Cohort 2 #9]*
- **Topic**: Tree Generalized Suffix Automaton (`广义 SAM`) via Leaf-Rooted Substring Cover.
- **Statement & Constraints**: Given an unrooted tree $T$ with $N \le 10^5$ vertices colored from $\{0..9\}$ and **at most $L \le 20$ leaves**, count the number of distinct strings formed by all simple paths in $T$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $\binom{N}{2}$ simple paths include $\Lambda$-shaped paths missed by any single rooting.
  2. *Combinatorial Invariant*: By Theorem 4.1 (Leaf-Rooted Substring Cover), every simple path $u \rightsquigarrow v$ extends backward from $u$ to some leaf $\ell \in \mathcal{L}$, making it a vertical substring in $T_\ell$!
  3. *Compilation*: For each of the $\le 20$ leaves $\ell$, root $T$ at $\ell$ and insert all $N$ nodes into a single BFS Generalized SAM ($\le 4 \cdot 10^6$ states). Output $\sum_{x \in \text{GSAM}} (\text{len}(x) - \text{len}(\text{link}(x)))$.
  4. *Pitfall*: Naive single-string `extend` without checking `if (ch[p][c])` before allocating `cur` creates zero-length clones that corrupt the GSAM (`§4.2 Step 3`).

#### W5A-26. `[EN]` `CF 914E — Palindromes in a Tree` — *[Cohort 1 P-5A-18 + Cohort 2 #16]*
- **Topic**: Centroid Decomposition + Parikh Parity Bitmasks + Tree Difference Array.
- **Statement & Constraints**: Given a tree $T$ with $N \le 2 \cdot 10^5$ vertices labeled `'a'..'t'` ($|\Sigma| = 20$), for **each vertex $v$**, count simple paths passing through $v$ whose character multiset can be rearranged into a palindrome.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Each valid path $u \rightsquigarrow w$ increments **every** intermediate vertex on $u \rightsquigarrow w$, not just its endpoints.
  2. *Combinatorial Invariant*: A path is rearrangeable into a palindrome iff its xor-mask $M(u \rightsquigarrow w) \in [0, 2^{20})$ has popcount $\le 1$. At centroid $c$, crediting $+1$ to `diff[u]` for each valid partner $w$ in other child subtrees of $c$ and summing `diff` bottom-up toward $c$ credits every node on $u \rightsquigarrow c$ in $O(1)$!
  3. *Compilation*: Two-pass subtree sweep (left-to-right and right-to-left) at each centroid $c$ using `cnt[1 << 20]` in $O(N |\Sigma| \log N)$ total time.
  4. *Pitfall*: Paths $u \rightsquigarrow c \rightsquigarrow w$ get pushed up to $c$ from **both** $u$'s subtree and $w$'s subtree: divide the cross-subtree sum at $c$ by $2$, and ensure $c$'s character bit is included on only one side of the XOR!

#### W5A-27. `[JA]` `AtCoder ABC 336 G — 16 Integers` — *[Cohort 1 P-5A-20]*
- **Topic**: De Bruijn Graph $\mathcal{B}(\{0,1\}, 4)$ + BEST Theorem + Matrix-Tree Cofactor.
- **Statement & Constraints**: Given exact occurrence counts $X_{b_1 b_2 b_3 b_4} \le 10^6$ of all $16$ binary $4$-mers in a binary string $S$, count valid binary strings $S$ modulo $998244353$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: String length $\sum X_w + 3 \le 1.6 \cdot 10^7$ rules out DP, while $|V| = 2^3 = 8$ is tiny.
  2. *Combinatorial Invariant*: By Theorem 3.1 (BEST Theorem), valid strings with $4$-mer counts $X_w$ correspond to open Eulerian trails in the $8$-vertex De Bruijn multigraph $\mathcal{B}(\{0,1\}, 4)$, divided by $\prod_{w \in \{0,1\}^4} X_w!$.
  3. *Compilation*: Restrict to active vertices $V_{\text{act}} = \{v : d(v) > 0\}$, verify weak connectivity and degree balance, add virtual return edge $u_{\text{end}} \to u_{\text{start}}$, compute the $(r, r)$-cofactor of $L_{\text{out}}$ in $O(8^3)$, and multiply by $\prod_{v \in V_{\text{act}}} (\text{out}(v)-1)! / \prod X_w!$.
  4. *Pitfall*: Including isolated vertices ($d(v) = 0$) in the $8 \times 8$ Laplacian forces the determinant to $0$!

#### W5A-28. `[ZH]` `General $k$-Mer Spectrum Eulerian String Counting` (`UOJ 607` / `QOJ` / `NOI-WC`) — *[Cohort 2 #17]*
- **Topic**: Arbitrary-Alphabet De Bruijn Graph + BEST Theorem with Balanced vs. Open-Trail Dispatch.
- **Statement & Constraints**: Given $|\Sigma|^{k-1} \le 300$ and $k$-mer multiplicities $c(w)$ with $\sum c(w) \le 10^7$ (or $10^{18}$ with Lucas/mod factorials), count distinct strings $S$ realizing spectrum $c(\cdot)$ modulo $998244353$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Generalization of `W5A-27` to $|V| \le 300$ where the graph may be either strictly balanced ($\forall v, \text{in}(v) = \text{out}(v)$) or semi-Eulerian ($\text{out}(u_s) - \text{in}(u_s) = 1$).
  2. *Combinatorial Invariant*: When strictly balanced, any active vertex $r$ can serve as $u_{\text{start}} = u_{\text{end}}$, and there are $\sum_{r \in V_{\text{act}}} d(r) = \sum c(w)$ choices for the first edge $e_0$, giving $\big(\sum c(w)\big) \cdot t_{\text{in}}(G, r_0) \cdot \prod_{v \in V_{\text{act}}} (d(v)-1)! / \prod c(w)!$ (since $t_{\text{in}}(G, r)$ is independent of $r$ in a balanced Eulerian graph!).
  3. *Compilation*: $O(|V|^3 + \sum c(w))$ Gaussian elimination + factorial division.
  4. *Pitfall*: In a balanced Eulerian graph, $t_{\text{in}}(G, r)$ is **identical for all $r \in V_{\text{act}}$**, so you only need **one** determinant computation multiplied by $\sum_{v \in V_{\text{act}}} d(v) = |E|$, not $|V|$ separate determinants!

#### W5A-29. `[EN]` `[ZH]` `LCP-Anchored Substring Equalities & Inequalities` (`QOJ 5421` / `CF Gym 104077`) — *[Cohort 1 P-5A-22 + Cohort 2 #12, #24]*
- **Topic**: Binary-Lifting DSU + Tarjan SCC + Condensation DAG Longest Path.
- **Statement & Constraints**: Given $N \le 10^5$ and $M \le 10^5$ constraints specifying $\text{LCP}(S[l_1..r_1], S[l_2..r_2]) = d$ and $S[l_1..r_1] \le S[l_2..r_2]$ (or $<$, $=$), find the minimum alphabet size $K_{\min}$ and lexicographically smallest valid string $S$, or report `-1`.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Combines bulk prefix equalities of length $d$ with mismatch character inequalities at offset $d$.
  2. *Combinatorial Invariant*: Push $S[l_1..l_1+d-1] = S[l_2..l_2+d-1]$ into Binary-Lifting DSU (`§1`). At offset $d$: if $d < \min(L_1, L_2)$, add directed edge $\text{rep}(l_1+d) \xrightarrow{1} \text{rep}(l_2+d)$; if $d = \min(L_1, L_2)$, check directly whether length comparison $L_1$ vs. $L_2$ satisfies the requested relation!
  3. *Compilation*: Run Binary-Lifting DSU pushdown, build $\{0, 1\}$-weighted digraph on $\text{DSU}_0$ roots, check no SCC contains a weight-$1$ edge via Tarjan SCC, and compute DAG longest paths $\text{dist}[X]$.
  4. *Pitfall*: Failing to reject when $d = L_2 < L_1$ and $S[l_1..r_1] \le S[l_2..r_2]$ (a string cannot be $\le$ its own proper prefix!).

#### W5A-30. `[EN]` `Online Word Equations with Inequality Conflict Rejection` (`QOJ` / `CF 1286D` Variant) — *[Cohort 2 #18]*
- **Topic**: Online Recursive Binary-Lifting DSU + Small-to-Large Conflict Sets + Rollback Stack.
- **Statement & Constraints**: Maintain $S[1..N]$ ($N \le 2 \cdot 10^5$) under $Q \le 2 \cdot 10^5$ online operations: (1) assert $S[l_1..r_1] = S[l_2..r_2]$, (2) assert $S[i] \neq S[j]$, or (3) query $26^C \bmod (10^9+7)$, rejecting and ignoring any operation that contradicts accepted assertions.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Contradictory queries must be rejected atomically online without corrupting $\text{DSU}_0..\text{DSU}_K$.
  2. *Combinatorial Invariant*: By Theorem 1.2, each accepted query performs only amortized $O(1)$ productive merges across all $K+1$ DSU levels. Maintain `std::set<int> neq[r]` on $\text{DSU}_0$ roots merged small-to-large.
  3. *Compilation*: During `merge_block(k, i, j)`, push all DSU modifications onto a rollback log; if any level-$0$ merge hits $r_v \in \text{neq}[r_u]$, unwind the rollback log and ignore the query!
  4. *Pitfall*: Even if a query is rejected and rolled back, without recording already-tested pairs at level $k$ inside the *same* query, an adversarial query could recurse on the same conflict twice—keep changes until the end of the query or abort on the very first conflict!

#### W5A-31. `[ZH]` `Distinct Upward Path Prefixes & K-th Tree String via Tree SA + Height` (`Luogu P4094` Tree Variant) — *[Cohort 2 #19]*
- **Topic**: Dual-Rank Tree Suffix Array + $O(\log N)$ Tree LCP `height` Array + Binary Search.
- **Statement & Constraints**: Given a rooted tree $T$ ($N \le 2 \cdot 10^5$, $|\Sigma| \le N$) with characters on vertices, count total distinct upward path substrings (prefixes of $S(u)$) and find the $K$-th lexicographically smallest distinct upward string.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Large alphabet $|\Sigma| \le N$ and lexicographical $K$-th query make GSAM transition tables slow/un-ordered, whereas Tree SA orders all $N$ upward strings directly.
  2. *Combinatorial Invariant*: By Contract 4.2, $\text{height}[i] = \text{min}\big(\text{depth}(\text{SA}[i-1]), \text{depth}(\text{SA}[i]), \text{TREE\_LCP}(\text{SA}[i-1], \text{SA}[i])\big)$. Node $\text{SA}[i]$ contributes $\text{depth}(\text{SA}[i]) - \text{height}[i]$ new distinct upward prefix strings!
  3. *Compilation*: Build Tree SA and `height[2..N]` in $O(N \log N)$, build prefix sums of $\text{depth}(\text{SA}[i]) - \text{height}[i]$, and binary search for the $K$-th string in $O(\log N)$.
  4. *Pitfall*: Do not use Kasai's algorithm on trees (`§4.2 Step 1.2`); compute `height[i]` via binary lifting on `rk[k]` and cap at $\min(\text{depth}(u), \text{depth}(v))$.

#### W5A-32. `[EN]` `[JA]` `Wheeler Graph Recognition & Interval Pattern Matching` (`QOJ` / `JOI Spring Camp` / Gagie–Manzini–Sirén) — *[Cohort 1 P-5A-29 + Cohort 2 #20]*
- **Topic**: Wheeler DFA Co-Lexicographical Interval Maintenance & Convexity Recognition.
- **Statement & Constraints**: Given an edge-labeled DFA $G = (V, E, \Sigma)$ ($|V|, |E| \le 2 \cdot 10^5$), verify whether a vertex ordering $\prec$ is a valid Wheeler order, and answer $Q$ queries counting vertices reachable by pattern $P_q$ ($\sum |P_q| \le 5 \cdot 10^5$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Simulating $P_q$ from all $|V|$ vertices takes $O(|V| \cdot |P_q|)$.
  2. *Combinatorial Invariant*: By the Wheeler Axioms (`§3.3`), the reachable vertex set for any $P_q$ is a single contiguous interval $[l_V, r_V]$ updated in two $O(1)$ rank steps: vertex interval $[l_V, r_V] \to$ outgoing $c$-edge interval $[l_E, r_E] \to$ target vertex interval $[l'_V, r'_V]$.
  3. *Compilation*: Check Wheeler validity by sorting edges by $(c, u)$ and verifying target vertices $v$ are non-decreasing (`v[i] <= v[i+1]`) and partitioned by incoming label $c$; answer queries via prefix rank arrays in $O(|P_q|)$.
  4. *Pitfall*: Assuming in-degree $1$ like linear BWT fails when a vertex $v$ has multiple incoming $c$-edges: you must map vertex range $\to$ edge range $\to$ target vertex range.

#### W5A-33. `[ZH]` `[PKUSC2018] 神仙的游戏` (`LOJ 6436`) — *[Cohort 1 P-5A-19]*
- **Topic**: Wildcard Border Periodicity Equations + NTT Difference Convolution + Harmonic Sieve.
- **Statement & Constraints**: Given $S \in \{\text{'0'}, \text{'1'}, \text{'?'}\}^N$ ($N \le 5 \cdot 10^5$), a length $k$ is a valid border iff `'?'` can be filled so $S[1..k] = S[N-k+1..N]$. Compute the XOR sum of $k^2$ over all valid border lengths $k$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $S[1..k] = S[N-k+1..N]$ is a system of $k$ character equations $S[i] = S[i + N - k]$ on a single string $S$, which forces $d = N - k$ to be a global period of $S$!
  2. *Combinatorial Invariant*: Period $d$ is realizable by filling `'?'` iff no `'0'` and `'1'` lie in the same congruence class $\bmod d$, i.e., there are no indices $i, j$ with $S[i] = \text{'0'}, S[j] = \text{'1'}$ and $d \mid |i - j|$.
  3. *Compilation*: Convolve `[S[i] == '0']` with `[S[N - j] == '1']` via NTT in $O(N \log N)$ to find all forbidden differences $\Delta = |i - j|$; mark period $d$ invalid iff any multiple $m \cdot d$ is a forbidden difference.
  4. *Pitfall*: Treating `'?'` as a non-transitive wildcard (only checking $|i - j| = d$ instead of all multiples $m \cdot d$) fails when $S[1] = \text{'0'}, S[1+d] = \text{'?'}, S[1+2d] = \text{'1'}$!

#### W5A-34. `[ZH]` `Tree Path Multi-Pattern Avoidance via Centroid + AC Automaton` (`Luogu P5327` / `[ZJOI2019]` Variant) — *[Cohort 2 #21]*
- **Topic**: Centroid Decomposition + Aho–Corasick Automaton & Fail-Tree Subtree Queries.
- **Statement & Constraints**: Given a character-labeled tree $T$ ($N \le 10^5$) and a dictionary $\{P_1, \dots, P_m\}$ ($\sum |P_i| \le 10^5$), count simple paths $(u, v)$ in $T$ that contain at least one $P_i$ as a substring.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Multi-pattern matching across $\binom{N}{2}$ undirected tree paths.
  2. *Combinatorial Invariant*: Complement-count paths avoiding all $P_i$. Mark terminal states in the AC automaton $\mathcal{A}$ (and $\mathcal{A}^R$) as absorbing (`bad[u] |= bad[fail[u]]`). At centroid $c$, combine non-absorbing upward states $q_1 \in \mathcal{A}^R$ and downward states $q_2 \in \mathcal{A}$ that do not form a straddling match across $c$.
  3. *Compilation*: Centroid Decomposition + AC Fail-Tree DFS order updates.
  4. *Pitfall*: Forgetting to propagate absorbing flags down the AC failure tree before walking tree edges.

#### W5A-35. `[EN]` `CF 1063F — String Journey` — *[Cohort 2 #22]*
- **Topic**: Substring Containment DAG Longest Path + SAM Link-Tree RMQ.
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \cdot 10^5$), find the maximum $k$ such that there exist disjoint substrings $t_1, \dots, t_k$ from left to right with $|t_i| = k - i + 1$ and $t_{i+1}$ a substring of $t_i$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Substring containment chain $t_k \subset t_{k-1} \subset \dots \subset t_1$ on $S$.
  2. *Combinatorial Invariant*: Since $|t_i| = |t_{i+1}| + 1$, $t_{i+1}$ is either the prefix $S[l_i .. r_i - 1]$ or the suffix $S[l_i + 1 .. r_i]$ of $t_i$. Moreover, $\text{dp}[l]$ (max chain length starting at $l$) satisfies $\text{dp}[l] \le \text{dp}[l+1] + 1$, giving a monotone two-pointer bound!
  3. *Compilation*: Sweep $l$ from $N$ down to $1$ with monotone pointer $r$, checking in $O(\log N)$ via SAM Link-Tree binary lifting + Segment Tree RMQ whether $S[l..l+L-2]$ or $S[l+1..l+L-1]$ has a prior state with $\text{dp} \ge L - 1$.
  4. *Pitfall*: Only inserting $\text{dp}[r]$ into the segment tree once $r \ge l + \text{dp}[l]$ to enforce disjointness of $t_1$ and $t_2$.

#### W5A-36. `[JA]` `AtCoder AGC 055 D — ABC Ultimatum` — *[Cohort 2 #23]*
- **Topic**: Cyclic 3-Cycle De Bruijn Subsequence Decomposition DP.
- **Statement & Constraints**: Count strings of length $3N$ ($N \le 15$) over $\{\text{'A'}, \text{'B'}, \text{'C'}\}$ decomposable into $N$ disjoint subsequences each equal to `"ABC"`, `"BCA"`, or `"CAB"`.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Cyclic shift symmetry on 3-letter subsequence transitions.
  2. *Combinatorial Invariant*: For a fixed decomposition count $(x, y, z)$ with $x + y + z = N$, Hall's condition reduces to bounding the maximum prefix excess of `'A'`, `'B'`, `'C'` along the 3-cycle De Bruijn graph; canonicalizing the minimal excess avoids fixed-$(x, y, z)$ double counting.
  3. *Compilation*: Prefix-excess DP in $O(N^5)$ time.
  4. *Pitfall*: Overcounting strings that admit multiple valid triples $(x, y, z)$.

---

### Tier 4: Mastery (`W5A-37` to `W5A-48` — `[CTSC2010] 珠宝商`, $10^{18}$ Word Equations, RLBWT Move Structures & Tree Syntheses)

#### W5A-37. `[ZH]` `[CTSC2010] 珠宝商` (`Luogu P4218` / `P4248`Tree Variant) — *[Cohort 1 P-5A-26 + Cohort 2 #25]*
- **Topic**: Undirected Tree-Path Pattern Counting in $S[1..M]$ via Centroid Decomposition + Dual SAM + $\sqrt{M}$ Double Thresholding.
- **Statement & Constraints**: Given an unrooted tree $T$ with $N \le 5 \cdot 10^4$ character-labeled vertices and a text string $S[1..M]$ ($M \le 5 \cdot 10^4$), compute the total number of occurrences of $\text{str}(u \rightsquigarrow v)$ in $S$ summed over all $N^2$ ordered pairs $(u, v)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Both $N, M \le 5 \cdot 10^4$: enumerating $N^2$ paths is $O(N^2)$, while doing an $O(M)$ split-point convolution at every centroid is $O(NM)$.
  2. *Combinatorial Invariant*: Build $\text{SAM}_S$ and $\text{SAM}_{S^R}$. At centroid $c$ of size $S_c$ with threshold $B = \sqrt{M}$:
     - **Light Regime ($S_c \le B$)**: Walk all $O(S_c^2)$ pairs $(u, v)$ directly in $\text{SAM}_S$ and add $|\text{endpos}_S(q)|$ in $O(S_c^2)$ time.
     - **Heavy Regime ($S_c > B$)**: Map upward paths $u \rightsquigarrow c$ into $\text{SAM}_{S^R}$ and downward paths $\text{next}(c, v) \rightsquigarrow v$ into $\text{SAM}_S$, push path counts down both Link Trees to the prefix/suffix indices $i \in [1..M]$ of $S$, and sum $\text{up}[i] \cdot \text{down}[i+1]$ in $O(S_c + M)$ time!
  3. *Compilation*: Set $B \approx \sqrt{M} \approx 250$; total time $O(N \sqrt{M} + M \sqrt{N} \log N)$.
  4. *Pitfall (Cohort 2 Critical Fix)*: When $S_c > B$ and you subtract same-child-subtree pairs $(u, v) \in T_{\text{sub}}^2$, **you must also threshold $|T_{\text{sub}}|$ against $B$** ($O(|T_{\text{sub}}|^2)$ walk if $|T_{\text{sub}}| \le B$, and $O(|T_{\text{sub}}| + M)$ Link-Tree sweep only if $|T_{\text{sub}}| > B$)! Otherwise a centroid with $O(N)$ leaf children of size $1$ runs $O(M)$ work $O(N)$ times and TLEs!

#### W5A-38. `[EN]` `[JA]` `Huge-Length Word & Palindrome Equations ($N \le 10^{18}$)` (`QOJ 6504` / `Universal Cup` / `Yukicoder`) — *[Cohort 1 P-5A-27 + Cohort 2 #26]*
- **Topic**: Huge-Length ($N \le 10^{18}$) Word Equations via Fine–Wilf Euclidean Period Contraction & Reflection Folding.
- **Statement & Constraints**: Given $N \le 10^{18}$ and $M \le 1000$ constraints $S[l_1..r_1] = S[l_2..r_2]$ (or palindrome equations $S[l..r] = S[l..r]^R$), compute the number of independent character components $C$ and output $|\Sigma|^C \bmod 998244353$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $N \le 10^{18}$ prohibits materializing $O(N \log N)$ binary-lifting blocks.
  2. *Combinatorial Invariant*: By `§1.4`, an overlapping equation $S[l..l+L-1] = S[l+p..l+p+L-1]$ ($p > 0$) makes $[l, l+p+L-1]$ periodic with period $p$, folding $[l+p, l+p+L-1]$ onto $[l, l+p-1]$ via $x \mapsto l + ((x - l) \bmod p)$ (splitting any interval into at most $2$ pieces). Overlapping periods $p, q$ reduce via $(q, p) \mapsto (p, q \bmod p)$ and Fine–Wilf $\gcd(p, q)$ in $O(\log N)$ Euclidean steps!
  3. *Compilation*: Maintain dynamic elementary intervals with affine shift/reflection DSU edges; recursively fold overlapping intervals in $O(M \log^2 N)$ operations.
  4. *Pitfall*: When folding $[x, y]$ modulo $p$ into $[l, l+p-1]$, whenever $(x - l) \bmod p > (y - l) \bmod p$, the image wraps around the period boundary and must be split into **two** contiguous intervals $[l + (x-l)\bmod p,\; l+p-1]$ and $[l,\; l + (y-l)\bmod p]$.

#### W5A-39. `[ZH]` `[HNOI2019] JOJO` (`Luogu P5287`) — *[Cohort 1 P-5A-28]*
- **Topic**: Persistent KMP Automaton on a Version Tree with Run-Length Compressed Blocks (`slink` Period Jumping).
- **Statement & Constraints**: Starting from an empty string, support $N \le 10^5$ operations on a version tree: (1) append $x \le 10^4$ copies of character $c$, or (2) revert to version $v$. After each operation, output $\sum_{i=1}^{|S|} \pi[i] \bmod 998244353$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Combines version-tree branching (which defeats amortized KMP) with RLE blocks $(c, x)$ of length $10^4$ (which defeat single-character DFA transitions).
  2. *Combinatorial Invariant*: Represent the string as a sequence of RLE blocks $(c_k, x_k)$. When appending $(c, x)$ at block index $k$, walk the KMP failure chain of RLE blocks using **`slink` (series-link) periodic jumps** in $O(\log k)$ steps: a border block $(c_j, x_j)$ with $c_j = c$ and $x_j \le x$ contributes an arithmetic progression of border lengths for the prefix of $(c, x)$ of length $x_j$, and only the **longest** match with $x_j = x$ can extend further as the full block border!
  3. *Compilation*: DFS the version tree; at each node, jump `slink` on the RLE KMP chain in $O(\log N)$ steps to sum the arithmetic progressions of $\pi$.
  4. *Pitfall*: When matching against the very first RLE block $(c_1, x_1)$ with $c_1 = c$ and $x > x_1$, the remaining $x - x_1$ characters of the new block all receive constant border length $x_1$ (not $0$!).

#### W5A-40. `[EN]` `CF 1098F — Ж-function` — *[Cohort 1 P-5A-25]*
- **Topic**: Link-Tree Centroid Decomposition + 2D Range Queries for Substring Z-Sums.
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \cdot 10^5$) and $Q \le 2 \cdot 10^5$ queries $[l, r]$, compute $\sum_{i=l}^r \text{LCP}(S[l..r], S[i..r])$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $\text{LCP}(S[l..r], S[i..r]) = \min\big(r - i + 1,\; \text{len}(\text{lca}_{\text{LinkTree}}(\text{state}(i), \text{state}(l)))\big)$.
  2. *Combinatorial Invariant*: Build the SAM of $S^R$ so suffix $S[i..N]$ corresponds to prefix node $v_i$ in the Link Tree $\mathcal{T}$, and $\text{LCE}(l, i) = \text{len}(\text{lca}_{\mathcal{T}}(v_l, v_i))$. Decompose $\mathcal{T}$ via **Centroid Decomposition** (or HLD) so $\text{lca}(v_l, v_i)$ is captured at the highest centroid on their path, reducing the query $i \in [l, r]$ with clamp $r - i + 1 \le \text{len}(w)$ to 2D Fenwick Tree range sums!
  3. *Compilation*: SAM of $S^R$ + Link-Tree Centroid Decomposition / HLD + offline Fenwick Tree in $O((N + Q) \log^2 N)$.
  4. *Pitfall*: Splitting the $\min(r - i + 1, L)$ clamp cleanly into $i \le r - L + 1$ (contributes $L$) and $r - L + 1 < i \le r$ (contributes $r - i + 1$).

#### W5A-41. `[JA]` `Partially Filled Z-Array Reconstruction & Counting` (`AtCoder AGC 059 D` / Grandmaster Inverse Z) — *[Cohort 2 #27]*
- **Topic**: Z-Box Inheritance Constraints + Dynamic Equality/Inequality Graph Feasibility.
- **Statement & Constraints**: Given a partially filled Z-array $Z[1..N]$ (with `-1` wildcards, $N \le 3000$), decide whether a valid string $S$ exists (or count valid strings).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Unknown entries $Z[j] = -1$ mean the set of equality/inequality edges is not fixed upfront.
  2. *Combinatorial Invariant*: Inside any active Z-box $[i, i + Z[i] - 1]$, index $j$ mirrors $k = j - i + 1$:
     - If $k + Z[k] - 1 < Z[i]$, then $Z[j] = Z[k]$ is **forced**.
     - If $k + Z[k] - 1 > Z[i]$, then $Z[j] = i + Z[i] - j$ is **forced**.
     - If $k + Z[k] - 1 = Z[i]$, then $Z[j] \ge i + Z[i] - j$ is required, and $Z[j] > i + Z[i] - j$ holds iff the mismatch characters of $i$ and $k$ are equal!
  3. *Compilation*: Sweep $i = 2..N$ propagating forced Z-box relations and checking DSU equality vs. mismatch consistency.
  4. *Pitfall*: If a known $Z[j] > i + Z[i] - j$ occurs when $k + Z[k] - 1 < Z[i]$, it forces $S[1+Z[i]] = S[i+Z[i]]$ (violating $i$'s mismatch!).

#### W5A-42. `[EN]` `Tree Path 1-Mismatch & Wildcard Pattern Counting` (`CF 1781F` / `ICPC` Variant) — *[Cohort 2 #28]*
- **Topic**: Centroid Decomposition + Binary-Lifting Tree Hash LCE for Approximate Tree Path Matching.
- **Statement & Constraints**: Given a character-labeled tree $T$ ($N \le 5 \cdot 10^4$) and pattern $P[1..L]$, count directed paths $u \rightsquigarrow v$ of length $L$ that have Hamming distance $\le 1$ to $P$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Exact SAM/AC transitions break when $1$ mismatch is allowed along a tree path.
  2. *Combinatorial Invariant*: At centroid $c$, a path $u \rightsquigarrow c \rightsquigarrow v$ of length $L$ has $\le 1$ mismatch with $P$ iff either (a) $u \rightsquigarrow c$ has $0$ mismatches with $P[1..d]$ and $c \rightsquigarrow v$ has $\le 1$ mismatch with $P[d..L]$, or (b) $u \rightsquigarrow c$ has $1$ mismatch with $P[1..d]$ and $c \rightsquigarrow v$ has $0$ mismatches with $P[d..L]$. For any node $u$, its first mismatch against $P$ is found in $O(\log N)$ via binary lifting + tree rolling hash LCE, and its second mismatch checks whether the remainder has $0$ more mismatches!
  3. *Compilation*: Centroid Decomposition + Binary-Lifting Tree Hash LCE in $O(N \log^2 N)$.
  4. *Pitfall*: Paths where the single mismatch occurs **at the centroid $c$ itself** are counted in both (a) and (b) unless $c$ is assigned strictly to the downward half $\text{next}(c, v) \rightsquigarrow v$!

#### W5A-43. `[ZH]` `[JA]` `Run-Length Compressed BWT (`RLBWT`) Pattern Matching & Move Structure` (`UOJ` / `LOJ` / Nishimoto–Tabei) — *[Cohort 2 #29 + Cohort 3 Frontier]*
- **Topic**: RLBWT Piecewise-Affine LF-Mapping & $O(1)$ Move Data Structure.
- **Statement & Constraints**: Given the run-length encoded BWT of a string $S$ of length $N \le 10^{12}$ consisting of $R \le 10^5$ equal-character runs $(c_j, \ell_j)$, extract $S[K .. K + L - 1]$ ($L \le 10^5$) and count occurrences of pattern $P[1..M]$ ($M \le 10^5$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $N \le 10^{12}$ forbids $O(N)$ arrays, while $R \le 10^5$ runs are small.
  2. *Combinatorial Invariant*: By Theorem 3.2, the $j$-th run $L[l_j .. r_j] = c^{\ell_j}$ maps under $\text{LF}$ to a contiguous interval $[C[c] + \text{Occ}(c, l_j),\; C[c] + \text{Occ}(c, r_j)]$ of length $\ell_j$ in $F$ with slope $+1$! Thus $\text{LF}$ is a piecewise-translation bijection with $R$ intervals.
  3. *Compilation*: Store prefix lengths by character to evaluate $\text{Occ}(c, x)$ in $O(\log R)$ via binary search (or split runs into $\le 2R$ intervals via the **Nishimoto–Tabei Move Structure** so every LF-step is a direct pointer + offset jump in $O(1)$ time!).
  4. *Pitfall*: When updating $[l, r]$ on character $c$, if run $j$ at boundary $l$ has $c_j \neq c$, advance $l$ to the first run of character $c$ inside $[l, r]$.

#### W5A-44. `[EN]` `Eulerian String Counting Avoiding Forbidden Substrings (AC Automaton + BEST Theorem)` (`Universal Cup` / `QOJ`) — *[Cohort 2 #30]*
- **Topic**: Aho–Corasick DFA + BEST Theorem for Variable-Length Transition Spectra.
- **Statement & Constraints**: Given forbidden patterns $\mathcal{F}$ ($\sum |P| \le 500$) and exact transition counts $\text{cnt}(u, c)$ for each state $u$ and character $c \in \Sigma$ in the Aho–Corasick DFA of $\mathcal{F}$, count valid strings $S$ starting at state $0$, avoiding $\mathcal{F}$, and realizing $\text{cnt}(u, c)$ modulo $998244353$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Generalizes De Bruijn $k$-mer Eulerian counting (`W5A-27`) to an arbitrary deterministic AC automaton.
  2. *Combinatorial Invariant*: Because the AC DFA has at most one outgoing transition per $(u, c)$, two distinct sequences of $(u, c)$ transitions from state $0$ produce distinct strings $S$! Thus valid strings biject with open Eulerian trails from $u_{\text{start}} = 0$ in the AC transition multigraph.
  3. *Compilation*: Check no active state has `bad[u] == 1`; run the BEST Theorem (Theorem 3.1) on active AC states $V_{\text{act}}$, dividing by $\prod_{u \in V_{\text{act}}, c \in \Sigma} \text{cnt}(u, c)!$.
  4. *Pitfall (Cohort 2 Critical Discovery)*: Unlike De Bruijn graphs, in an AC DFA two transitions $u \xrightarrow{c_1} v$ and $u \xrightarrow{c_2} v$ with **different characters $c_1 \neq c_2$** can land in the same target state $v$! You must divide by $\prod_{u, c} \text{cnt}(u, c)!$, **never** by $\prod_{u, v} A(u, v)!$!

#### W5A-45. `[ZH]` `Tree Path K-th Lexicographical String via Tree SA + Persistent Segment Tree` (`Luogu P6096` / `QOJ`) — *[Cohort 1 P-5A-30]*
- **Topic**: Dual-Rank Tree Suffix Array + Tree-Path Persistent Segment Tree (Chairman Tree).
- **Statement & Constraints**: Given a rooted tree $T$ ($N \le 10^5$) with character-labeled nodes, answer $Q \le 10^5$ queries: among all ancestors $w$ of $u$ at depth $\in [d_L, d_R]$ (or on path $u \rightsquigarrow v$), find the $k$-th lexicographically smallest upward string $S(w)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Requires range $k$-th rank queries along tree paths over the global ordering of upward tree strings.
  2. *Combinatorial Invariant*: Once Contract 4.2 computes the Tree SA rank $\text{id}[w] \in [1..N]$ for every node $w$, the set of upward strings on the vertical segment $\text{anc}(u, \text{depth}(u)-d_L) \rightsquigarrow \text{anc}(u, \text{depth}(u)-d_R)$ is the difference of two root-to-node Persistent Segment Trees!
  3. *Compilation*: Build Tree SA in $O(N \log N)$, build a Persistent Segment Tree along $T$ inserting $\text{id}[w]$ at node $w$ from its parent's version, and binary search the difference of two versions in $O(\log N)$ per query.
  4. *Pitfall*: Ensure tie-breaking in $\text{id}[w]$ matches the problem's tie-breaker when two ancestors have identical upward strings $S(w_1) = S(w_2)$.

#### W5A-46. `[ZH]` `[BJOI2020] 树上子串` (`Luogu P6640` + Subtree Depth Extension) — *[Cohort 2 #31]*
- **Topic**: Tree Generalized SAM + Link-Tree Segment Tree Merging + Binary Lifting.
- **Statement & Constraints**: Given a rooted tree $T$ ($N \le 10^5$) where each root-to-node path forms a string, answer $Q \le 10^5$ queries $(u, d_1, d_2, P_q)$ ($\sum |P_q| \le 2 \cdot 10^5$): find the longest substring of $P_q$ that appears as a suffix of some node $v$ in $u$'s subtree with depth $\in [d_1, d_2]$ (or entirely inside the subtree depth window).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Restricting occurrences in a Tree GSAM to a subtree + depth interval.
  2. *Combinatorial Invariant*: Build the BFS Generalized SAM of $T$. Each tree node $v$ is an $\text{endpos}$ point indexed by its DFS tin $\text{dfn}[v]$. Walk $P_q$ on the GSAM to find the longest matched length at each prefix of $P_q$, and use Link-Tree binary lifting + Segment Tree Merging on $\text{dfn}[v]$ to check whether a state's $\text{endpos}$ set intersects $\text{subtree}(u)$.
  3. *Compilation*: BFS GSAM + Segment Tree Merging on Link Tree in $O((N + \sum |P_q|) \log N)$.
  4. *Pitfall*: Clipping the depth window to $[d_1 + L - 1, d_2]$ so a matched substring of length $L$ ending at $v$ does not start above depth $d_1$!

#### W5A-47. `[EN]` `CF 1310C — Au Pont Rouge` — *[Cohort 1 P-5A-31]*
- **Topic**: Lexicographical Substring Inequality Binary Search ($S[l..r] \ge P$) + LCP Table + Suffix-Sum DP.
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 1000$), partition $S$ into $M$ substrings maximizing the lexicographically smallest piece, and find the $K$-th largest such minimum piece ($K \le 10^{18}$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Binary searching over all $\binom{N+1}{2}$ candidate substrings $P$ requires counting partitions where every piece satisfies $S[i..j] \ge P$ in $O(N^2)$ time.
  2. *Combinatorial Invariant*: For a fixed threshold $P = S[a..b]$, a piece starting at $i$ satisfies $S[i..j] \ge P$ iff $j \ge r_{\min}(i)$, where $r_{\min}(i)$ is found in $O(1)$ from $t = \text{LCP}(i, a)$: if $t < |P|$ and $S[i+t] > S[a+t]$, then $r_{\min}(i) = i + t$; if $t < |P|$ and $S[i+t] < S[a+t]$, then $r_{\min}(i) = \infty$; if $t \ge |P|$, then $r_{\min}(i) = i + |P| - 1$.
  3. *Compilation*: Precompute $\text{LCP}[i][j]$ in $O(N^2)$, sort all substrings in $O(N^2 \log N)$, and binary search with an $O(NM)$ suffix-sum DP capped at $\min(\text{dp}, K + 1)$.
  4. *Pitfall*: DP values must be capped at $K + 1$ at every addition to avoid `int64` overflow.

#### W5A-48. `[EN]` `Grandmaster Tree Synthesis: Tree Binary-Lifting DSU + Inequality SCC + Tree SA` (`CF 1817D` / `Universal Cup` Synthesis) — *[Cohort 2 #32 + Cohort 3 Frontier]*
- **Topic**: Signed Tree Binary-Lifting DSU (`树上倍增并查集`) + Tarjan SCC Condensation DAG + Dual-Rank Tree Suffix Array.
- **Statement & Constraints**: Given a rooted tree $T$ ($N \le 10^5$) with unknown characters on vertices and $M \le 10^5$ constraints specifying $\text{LCP}(\text{str}(u_1 \uparrow L_1), \text{str}(u_2 \uparrow L_2)) = d$ and $\text{str}(u_1 \uparrow L_1) \le \text{str}(u_2 \uparrow L_2)$, construct the pointwise lexicographically smallest valid vertex labeling (ordered by vertex $1..N$) and compute its Tree Suffix Array, or report `-1`.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Grandmaster synthesis combining all three pillars of Wave 5A on a tree: Tree Word Equations (`§1.5`), String Inequality SCCs (`§2.2`), and Dual-Rank Tree SA (`§4.2`).
  2. *Combinatorial Invariant*: Each LCP $d$ imposes an upward tree-path equality $\text{str}(u_1 \uparrow d) = \text{str}(u_2 \uparrow d)$, which splits into two tree binary-lifting blocks $B_k(u_1) = B_k(u_2)$ and $B_k(\text{anc}(u_1, d-2^k)) = B_k(\text{anc}(u_2, d-2^k))$ ($k = \lfloor \log_2 d \rfloor$). At depth $d$, if $d < \min(L_1, L_2)$, it adds the strict character inequality $c(\text{anc}(u_1, d)) < c(\text{anc}(u_2, d))$.
  3. *Compilation*: Push down Tree Binary-Lifting DSU from $k = 17 \to 0$ via `UNITE(k-1, u, r)` and `UNITE(k-1, anc(u, 2^{k-1}), anc(r, 2^{k-1}))`, run Tarjan SCC + DAG longest path on $\text{DSU}_0$ roots to assign `'a' + dist[SCC(find_0(u))]`, and finally run Contract 4.2 to output the Tree SA in $O((N \log N + M)\alpha(N))$.
  4. *Pitfall*: Locating the mismatch character at offset $d$ on a tree requires binary lifting to $\text{anc}(u_1, d)$ and $\text{anc}(u_2, d)$ in $O(\log N)$ time rather than $u_1 + d$!

---

## 6. Consolidated Quarantine Ledger (`R-5A-01` to `R-5A-12` — Excluded Pure Templates)

Per `AGENTS.md` and `PLAN.md §2.2`, all bare implementation verification templates from Cohort 1 and Cohort 2 are strictly quarantined from the textbook practice ladders:

| Quarantine ID | Problem Source & Title | Language | Cohort Origin | Reason for Quarantine |
| :--- | :--- | :--- | :--- | :--- |
| **`R-5A-01`** | `Luogu P3367 — 【模板】并查集` / `Library Checker — Unionfind` | `[ZH]`/`[EN]` | Cohort 1 `R-5A-01` | Bare DSU template without ST-table binary-lifting decomposition. |
| **`R-5A-02`** | `Luogu P4782 — 【模板】2-SAT` / `Library Checker — Two Sat` | `[ZH]`/`[EN]` | Cohort 1 `R-5A-02` | Bare 2-SAT solver verification without lexicographical string inequality compilation. |
| **`R-5A-03`** | `Luogu P7771 — 【模板】欧拉路径` / `CSES 1693 — Teleporters Path` | `[ZH]`/`[EN]` | Cohort 1 & 2 `R-5A-03` | Standard Hierholzer Eulerian path template without De Bruijn $k$-mer or BEST modeling. |
| **`R-5A-04`** | `CSES 1692 — De Bruijn Sequence` | `[EN]` | Cohort 1 & 2 `R-5A-04` | Bare textbook generation of a binary De Bruijn cycle of order $n \le 15$. |
| **`R-5A-05`** | `Luogu P6139 — 【模板】广义后缀自动机 (广义 SAM)` | `[ZH]` | Cohort 1 `R-5A-05` & Cohort 2 `R-5A-02` | Pure Generalized SAM template asking only for distinct substring count of an explicit input Trie. |
| **`R-5A-06`** | `Luogu P3806 — 【模板】点分治 1` | `[ZH]` | Cohort 1 `R-5A-06` | Bare Centroid Decomposition distance query template without string automata or bitmasks. |
| **`R-5A-07`** | `Luogu P6178 — 【模板】Matrix-Tree 定理` | `[ZH]` | Cohort 1 `R-5A-07` & Cohort 2 `R-5A-05` | Pure directed/undirected Laplacian determinant template without De Bruijn / BEST coupling. |
| **`R-5A-08`** | `Library Checker — Suffix Array` / `Luogu P3809 — 【模板】后缀排序` | `[EN]`/`[ZH]` | Cohort 1 `R-5A-08` | Standard 1D Suffix Array construction template. |
| **`R-5A-09`** | `Luogu P5353 — 【模板】树上后缀排序` (Bare Template Version) | `[ZH]` | Cohort 2 `R-5A-01` | Bare Tree Suffix Sorting template; its Dual-Rank Doubling Contract is taught directly in `§4.2–§4.3` and tested via query-coupled problems (`W5A-18`, `W5A-31`, `W5A-45`, `W5A-48`). |
| **`R-5A-10`** | `Library Checker — Directed Eulerian Trail` | `[EN]`/`[JA]` | Cohort 2 `R-5A-06` | Pure library verification problem for Eulerian trails. |
| **`R-5A-11`** | `SPOJ BWT / BWTINV — Burrows–Wheeler Transform Inversion` | `[EN]` | Cohort 2 `R-5A-07` | Bare implementation check of BWT forward/backward transform without structural twists. |
| **`R-5A-12`** | `Luogu P3375 / P5410 — 【模板】KMP / 扩展 KMP (Z-Function)` | `[ZH]` | Cohort 2 `R-5A-08` | Forward KMP and Z-array computation templates. |

---

## 7. Reconciled Multilingual Stringology Rosetta Stone & Master Bibliography

### 7.1 Multilingual Terminology Table (`[EN]` $\leftrightarrow$ `[ZH]` $\leftrightarrow$ `[JA]`)

| Concept (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) | Canonical Theorems & Archetypes |
| :--- | :--- | :--- | :--- |
| **Binary-Lifting / Parallel DSU** | 倍增并查集 / ST表并查集 | ダブリング Union-Find / 区間等価 UF | Theorem 1.1 & 1.2; `[SCOI2016] 萌萌哒` (`W5A-01`). |
| **Signed / Palindrome Binary-Lifting DSU** | 带权倍增并查集 (回文/翻转方程) | 重み付き (反転) ダブリング UF | Contract 4.1 (`is_pal[k][r]`); `W5A-14`. |
| **Tree Binary-Lifting DSU** | 树上倍增并查集 | 木上のダブリング Union-Find | `§1.5`; `W5A-48`. |
| **Huge-Length Word Equations & Recompression** | 超长字方程 / 局部一致性重压缩 | 巨大文字列の語の方程式 / 再圧縮法 | Jeż (2016); Plandowski (1994); `W5A-38`. |
| **Inverse SA / KMP / Z / Manacher Reconstruction** | 逆后缀数组 / KMP・Z・Manacher 还原 | 接尾辞配列・KMP・Z・Manacher の逆問題 | Theorem 2.1; Bannai et al. (2003); `W5A-02..05`, `W5A-15`. |
| **De Bruijn Graph & BEST Theorem** | De Bruijn 图与 BEST 定理 | ド・ブラン・グラフと BEST 定理 | Theorem 3.1; `AtCoder ABC 336 G` (`W5A-27`), `W5A-28`, `W5A-44`. |
| **Burrows–Wheeler Transform & LF-Mapping** | BWT 变换与 LF 映射 / FM-Index | Burrows–Wheeler 変換 / LF-マッピング | Theorem 3.2; Burrows & Wheeler (1994); Ferragina & Manzini (2000). |
| **Run-Length BWT (`RLBWT`) & Move Structure** | 游程压缩 BWT 与 Move 结构 | ランレングス圧縮 BWT (`RLBWT`) | Nishimoto & Tabei (2021); `W5A-43`. |
| **Wheeler Graphs (Prefix-Sorted DFAs)** | Wheeler 图 (前缀有序自动机) | Wheeler グラフ | Gagie, Manzini & Sirén (2017); `W5A-32`. |
| **Dual-Rank Tree Suffix Array** | 树上后缀排序 (双秩并列消歧) | 木上の接尾辞配列 (Tree Suffix Array) | Contract 4.2; `Luogu P5353`, `W5A-18`, `W5A-31`, `W5A-45`. |
| **Tree Generalized SAM (`Tree GSAM`)** | 树上广义后缀自动机 (叶根覆盖) | 木上の広義接尾辞オートマトン | Theorem 4.1; `[ZJOI2015] 诸神眷顾的幻想乡` (`W5A-25`). |
| **Centroid Decomposition + Dual SAM / Bitmask** | 点分治 + 双 SAM 根号分治 / 树上路径匹配 | 重心分解 + 接尾辞オートマトン | `[CTSC2010] 珠宝商` (`W5A-37`), `CF 914E` (`W5A-26`). |

---

### 7.2 Consolidated Master Bibliography (Academic, `[ZH]` National Team & `[JA]` Treatises)

1. **`[EN]` Academic Stringology & Graph Theory Canon**:
   - **de Bruijn, N. G. & van Aardenne-Ehrenfest, T. (1951)** — *Circuits and trees in oriented linear graphs*, Simon Stevin, 28, 203–217; **Smith, C. A. B. & Tutte, W. T. (1941)** — *On unicursal paths in a network of degree 4*, Amer. Math. Monthly: foundational proofs of the **BEST Theorem**.
   - **Burrows, M. & Wheeler, D. J. (1994)** — *A block-sorting lossless data compression algorithm*, Digital SRC Research Report 124.
   - **Ferragina, P. & Manzini, G. (2000)** — *Opportunistic data structures with applications*, FOCS 2000, 390–398: introduces the **FM-Index** and backward search via `LF-mapping`.
   - **Mantaci, S., Restivo, A., Rosone, G., & Sciortino, M. (2007)** — *An extension of the Burrows–Wheeler Transform*, Theoretical Computer Science, 387(3), 298–312: introduces the **Bijective BWT (`BBWT`)** via Chen–Fox–Lyndon factorization.
   - **Gagie, T., Manzini, G., & Sirén, J. (2017)** — *Wheeler graphs: A framework for BWT-based data structures*, Theoretical Computer Science, 698, 67–78; **Alanko, J., Gagie, T., Navarro, G., & Benkiki, O. (2020)** — *Tunneling on Wheeler graphs* / deterministic Wheeler recognition.
   - **Nishimoto, T. & Tabei, Y. (2021)** — *Optimal-time queries on BWT-runs compressed indexes*, ICALP 2021: introduces the **$O(1)$ Move Data Structure** for `RLBWT` LF-mapping.
   - **Plandowski, W. (1994, 1999)** — *Testing equivalence of morphisms on context-free languages* (ESA 1994) & *Satisfiability of word equations with constants is in PSPACE* (FOCS 1999).
   - **Jeż, A. (2016)** — *Recompression: A simple and powerful technique for word equations*, Journal of the ACM, 63(1), Article 4: $O(M \log N)$ locally consistent block/pair recompression for huge-length word equations.
   - **Bannai, H., Inenaga, S., Shinohara, A., & Takeda, M. (2003)** — *Inferring strings from graphs and arrays*, MFCS 2003, LNCS 2747, 208–217: unified theory of inverse KMP, Z, Suffix Array, and Manacher reconstruction via equality/inequality graphs.
2. **`[ZH]` Chinese National Team Papers (`国家集训队论文`) & Olympiad Editorials**:
   - **刘研绎 (Liu Yanyi, 2015)** — *《广义后缀自动机及其应用》 (Generalized Suffix Automaton and Its Applications)*, 2015 国家集训队论文: formalizes BFS vs. online DFS Tree GSAM construction, zero-length clone avoidance, and `[ZJOI2015] 诸神眷顾的幻想乡`.
   - **徐毅 (Xu Yi, 2014) & 金策 (Jin Ce, 2019)** — 国家集训队论文 on palindromic automata, string periodicity, Fine–Wilf contractions, and border series-link (`slink`) jumping on trees (`[HNOI2019] JOJO`).
   - **SCOI 2016 Official Editorial (`[SCOI2016] 萌萌哒`) & CTSC 2010 Official Editorial (`[CTSC2010] 珠宝商`)**: canonical references for `倍增并查集` and $\sqrt{M}$ heavy/light Centroid Decomposition + Dual-SAM Link-Tree stitching.
3. **`[JA]` Japanese Competitive Stringology Treatises**:
   - **`noshi91` / `maspypy` / `henkoku` / `tatyam`** — Algorithmic treatises on potential-amortized online doubling Union-Find (`ダブリング Union-Find`, $O(N \log N \alpha(N))$), Inverse Suffix Array combinatorics (`ARC 044 D`, `CF 1526E`), De Bruijn BEST Theorem (`ABC 336 G`), and `RLBWT` interval indexing.
