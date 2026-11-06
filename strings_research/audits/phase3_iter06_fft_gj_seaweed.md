# Phase 3 Global Audit Report — Iteration 06: FFT String Matching, Goulden–Jackson, Subsequence Matrices, Seaweed Matrices, Word Equations & Combinatorics on Words

- **Audit Scope**: `strings/chapters/ch18-*.qmd` through `strings/chapters/ch30-*.qmd` (Parts V, VI & VII — 13 Chapters, 8,166 Lines)
- **Verification Suite**: `tests/audit_strings_math.py` (Oracles 09, 10, 11, and 12 — **100% PASS**)
- **Audit Status**: **100% MATHEMATICALLY RIGOROUS & COMPLIANT WITH `AGENTS.md`**

---

## 1. Executive Summary & Global Audit Metrics

| Chapter | File | Lines | Callouts | Practice Problems | Forbidden LaTeX / `<details>` | Broken `.qmd` Links | Math / Editorial Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Ch 18** | `ch18-fft-wildcard-involution-matching.qmd` | 570 | 45 | 8 (4 Tiers) | 0 / 0 | 0 | **PASS (Exact)** |
| **Ch 19** | `ch19-kmismatch-wavefront-period-dichotomy.qmd` | 528 | 45 | 8 (4 Tiers) | 0 / 0 | 0 | **PASS (Polished)** |
| **Ch 20** | `ch20-structural-isomorphism-weighted-strings.qmd` | 624 | 46 | 8 (4 Tiers) | 0 / 0 | 0 | **PASS (Exact)** |
| **Ch 21** | `ch21-locally-consistent-parsing-slp-attractors.qmd` | 607 | 45 | 8 (4 Tiers) | 0 / 0 | 0 | **PASS (Polished)** |
| **Ch 22** | `ch22-dasg-arch-simon-invertible-matrices.qmd` | 654 | 46 | 8 (4 Tiers) | 0 / 0 | 0 | **PASS (Exact)** |
| **Ch 23** | `ch23-bit-parallel-lcs-seaweed-matrices.qmd` | 652 | 47 | 8 (4 Tiers) | 0 / 0 | 0 | **PASS (Exact)** |
| **Ch 24** | `ch24-goulden-jackson-moment-shift-fps.qmd` | 627 | 46 | 8 (4 Tiers) | 0 / 0 | 0 | **PASS (Exact)** |
| **Ch 25** | `ch25-martingale-pgfs-automaton-dp-of-dp.qmd` | 613 | 47 | 8 (4 Tiers) | 0 / 0 | 0 | **PASS (Exact)** |
| **Ch 26** | `ch26-word-equations-signed-parallel-dsu.qmd` | 619 | 45 | 9 (4 Tiers) | 0 / 0 | 0 | **PASS (Polished)** |
| **Ch 27** | `ch27-inverse-reconstruction-inequality-dags.qmd` | 576 | 42 | 8 (4 Tiers) | 0 / 0 | 0 | **PASS (Exact)** |
| **Ch 28** | `ch28-debruijn-best-bwt-wheeler-rlbwt.qmd` | 710 | 40 | 8 (4 Tiers) | 0 / 0 | 0 | **PASS (Polished)** |
| **Ch 29** | `ch29-tree-strings-stack-trie-sl2-hashing.qmd` | 789 | 40 | 8 (4 Tiers) | 0 / 0 | 0 | **PASS (Exact)** |
| **Ch 30** | `ch30-sturmian-singular-thue-morse-morphic-2d.qmd` | 646 | 44 | 9 (4 Tiers) | 0 / 0 | 0 | **PASS (Polished)** |

---

## 2. Chapter-by-Chapter Mathematical Rigor Audit (`Ch 18`–`Ch 30`)

### 2.1 Part V: Approximate / FFT Matching, Structural Isomorphism & Compressed Indexing (`Ch 18`–`Ch 21`)

1. **Chapter 18 — `ch18-fft-wildcard-involution-matching.qmd` (`T-3B-01`)**:
   - **Cross-Correlation Reversal Duality (Lemma 18.1)**: Verified the exact index-sum invariant $k + (M - 1 - j) = (i + j) + (M - 1 - j) = i + M - 1$, translating cross-correlation $\sum_{j=0}^{M-1} f(P[j])g(T[i+j])$ into coefficient $[x^{i+M-1}](A\cdot B)$ with $A[M - 1 - j] = f(P[j])$ and $B[k] = g(T[k])$.
   - **Clifford–Clifford Deterministic 3-NTT / 1-NTT Squared Penalty (Theorem 18.2)**: Verified the expansion
     $$D_{\text{ind}}(i) = \sum_{j=0}^{M-1} u_{P_j} u_{T_{i+j}}(v_{P_j} - v_{T_{i+j}})^2 = C_1[i+M-1] - 2C_2[i+M-1] + C_3[i+M-1],$$
     together with the explicit non-vanishing modular guard $\max D_{\text{ind}}(i) \le M(|\Sigma| - 1)^2 < p = 998244353$ (preventing modular wraparound when $M \le 10^6, |\Sigma| \le 26$) and the 1-forward + 1-inverse NTT butterfly reuse saving 4 of 6 transforms.
   - **Kalai's Randomized Projection (Theorem 18.3) & 3-in-2 Complex Hermitian Packing**: Verified the one-sided wildcard 1-NTT reduction ($T$ wildcard-free $\implies \sum r_j v_{T_{i+j}} = [x^{i+M-1}]R\cdot B$) vs. two-sided 2-NTT difference, Schwartz–Zippel error $\le 1/(p-1)$, and complex root-of-unity embedding $e^{2\pi i c/|\Sigma|}$ with 3-in-2 Hermitian symmetry $Z_k = A_k + i B_k$.
   - **`CF 1334G` Involution & Cauchy–Schwarz Affine Matching (Theorem 18.4)**: Verified all four `CF 1334G` methods (degree-4 polynomial, 2-cycle involution sum/product invariants $s_c = c + \pi(c), p_c = c\pi(c)$, 1-NTT random involution weights, and `Shift-And` bitsets) plus Cauchy–Schwarz collinearity $S_2 S_{P^2} - S_1^2 = 0$ with $S_1 \cdot S_P \ge 0$ (`a > 0`) and $\sqrt{M\log M}$ quantile value-bucketing.

2. **Chapter 19 — `ch19-kmismatch-wavefront-period-dichotomy.qmd` (`T-3B-02`)**:
   - **Kangaroo Jumps & 2-Z-Array $k = 1$ Matching (Lemma 19.1)**: Verified the clamped Kangaroo jump `j += min(LCE(j, i + j), M - j)` (preventing out-of-bounds reads past $T[i+M-1]$) and the parameter-free $O(N + M)$ 1-mismatch test $\operatorname{LCP}(P, T[i..]) + \operatorname{LCS}(P, T[..i+M-1]) \ge M - 1$.
   - **Landau–Vishkin Wavefront DP (Theorem 19.2) & Abrahamson Heavy–Light Split (Theorem 19.3)**: Verified the diagonal wavefront transition $p_0(e, d) = \max(L(e-1, d) + 1,\, L(e-1, d+1) + 1,\, L(e-1, d-1))$ and Abrahamson's heavy–light threshold $B = \lceil\sqrt{M\log_2 M}\rceil$ balancing $\le |\Sigma_{\text{heavy}}| < M/B$ per-character indicator NTTs against $\sum_{c \in \Sigma_{\text{light}}} \operatorname{occ}_P(c) \cdot \operatorname{occ}_T(c) \le N B$.
   - **Bringmann–Künnemann–Charalampopoulos–Kociumaka–Wellnitz $2k$-Period Dichotomy (Theorem 19.4)**: Verified both cases in full detail:
     - *Case A ($\operatorname{per}(P) > 2k$)*: Triangle inequality on shift distance $d_H(P[0..M-1-\delta], P[\delta..M-1]) \ge 2k + 1$ proves adjacent $k$-mismatch occurrences are separated by $\delta > k$, bounding Kangaroo jumps to $O(N)$.
     - *Case B ($\operatorname{per}(P) = p \le 2k$)*: Decomposition of $P$ and $T$ into RLE of period-$p$ runs with $\le 2k$ breaks ($3k$ runs), reducing matching to stride-$p$ parallelogram range updates (`diff1`, `diff2` with $O(1)$ 4-point updates) in $O(N + \frac{N}{p}k^2)$ time.

3. **Chapter 20 — `ch20-structural-isomorphism-weighted-strings.qmd` (`T-3B-03`, `T-3B-04`)**:
   - **Parameterized `p-KMP` (`T-3B-03`, Theorems 20.1 & 20.2)**: Verified Baker's context-independent encoding $\operatorname{prev}[i] = i - \operatorname{last}[S[i]]$, the mandatory dynamic window-clipping operator $\operatorname{clip}(x, L) = x \cdot [x \le L]$ re-evaluated *inside* every `while (q > 0)` fallback step, and the Single-Position Mutation Theorem for `prev` under sliding windows (`p = next[i]` updates $\operatorname{prev}[p] \leftarrow 0$) and tree ancestor paths.
   - **Order-Isomorphic `Order-KMP` (Theorem 20.3) & Cartesian-Tree `Cartesian-KMP` (Theorem 20.4)**: Verified Kubica et al.'s predecessor/successor relative indices $(\operatorname{LMax}[i], \operatorname{LMin}[i])$ and Park et al.'s Parent-Distance representation $\operatorname{PD}[i] = i - \max\{j < i : P[j] \le P[i]\}$ with single-stack simulation.
   - **Abelian / Parikh Continuum vs. Ternary Counterexample (Theorem 20.5) & $1/z$ Weighted Suffix Trees (Theorem 20.6)**: Verified the binary Parikh Intermediate Value Theorem (`[min_1[L], max_1[L]]` connectedness) alongside the explicit ternary counterexample $S = \texttt{abbc}$, and Barton et al.'s proof that the product measure generates $\le \lfloor z \rfloor$ disjoint cylinder leaves per node, yielding $O(zN)$-node $1/z$ WST construction.

4. **Chapter 21 — `ch21-locally-consistent-parsing-slp-attractors.qmd` (`T-3B-05`, `T-3B-06`)**:
   - **Locally Consistent Parsing & Cole–Vishkin 6-Coloring (Theorem 21.1)**: Verified alternating `RComp` ($c^\ell \to c_\ell$) and `PComp`, Cole–Vishkin's deterministic bit-differentiation step $c'(i) = 2\ell_i + \operatorname{bit}_{\ell_i}(W[i])$ reducing alphabet size to $6$ in $3$ rounds, and Jeż's directed cut synthesis $\Sigma_L \times \Sigma_R$ guaranteeing $\ge 1/4$ expectation ($\le 3/4$ length shrinkage per phase).
   - **Primary-Seam SLP Pattern Matching (Theorem 21.2)**: Verified that every occurrence of $P$ in $\operatorname{val}(X_r)$ has a unique highest split rule $X_u \to X_L X_R$ spanning the cut in $J_u = \operatorname{suff}_{|P|-1}(\operatorname{val}(X_L)) \cdot \operatorname{pref}_{|P|-1}(\operatorname{val}(X_R))$ and accumulating via DAG DP $\operatorname{occ}[u] = \operatorname{occ}[L] + \operatorname{occ}[R] + \operatorname{seam}[u]$.
   - **String Attractors $\gamma(S)$ (Theorem 21.3), $\tau$-Synchronizing Sets (Theorem 21.4) & 2D Wavelet LZ77 Indexing (Theorem 21.5)**: Verified Kempa–Prezza's SAM hitting-set formulation ($\operatorname{minlen}(q) = \operatorname{len}(\operatorname{link}(q)) + 1$, with universal lower bound $\gamma(S) \ge |\Sigma_S|$), Kempa–Kociumaka's $O(N/\tau)$-sized $\tau$-synchronizing set construction via sliding-window minima of period-free hashes, and Kärkkäinen–Ukkonen's primary-cut 2D Orthogonal Range Counting reduction.

---

### 2.2 Part VI: Subsequence Algebra, Seaweed Matrices, Goulden–Jackson & Automaton DP (`Ch 22`–`Ch 25`)

5. **Chapter 22 — `ch22-dasg-arch-simon-invertible-matrices.qmd` (`T-4B-01`, `T-4B-02`, `T-4B-03`)**:
   - **Subsequence Automaton (`DASG`), Arch Factorization & Simon's Congruence (Theorems 22.1–22.3)**: Verified leftmost-prefix greediness $\delta(i, c) = \operatorname{nxt}[i][c]$, 2D predecessor rectangle summation for common subsequences (`W4B-07`), Hébrard's Arch Factorization $\operatorname{sas}(S) = \iota(S) + 1$ with binary lifting on `arch_end[i]` for $O(\log N)$ range queries, and Barker et al.'s Simon-Tree equivalence for $\sim_k$.
   - **$\det(M_c) = 1$ Invertible Subsequence Matrices & Matrix-Free $O(N\sigma)$ Two-Term Recurrence (Theorems 22.4 & 22.5)**: Verified the transvection decomposition
     $$M_c = I_{\sigma+1} + \mathbf{e}_c \sum_{j \ne c} \mathbf{e}_j^T, \qquad M_c^{-1} = I_{\sigma+1} - \mathbf{e}_c \sum_{j \ne c} \mathbf{e}_j^T, \qquad \det(M_c) = 1,$$
     valid over any commutative ring $\mathcal{R}$ without division, and the exact two-term recurrence for the row-sum vector $\mathbf{u}_i^T = \mathbf{1}^T P_i$:
     $$\mathbf{u}_i^T = 2\mathbf{u}_{i-1}^T - \begin{cases} \mathbf{u}_{\operatorname{last}[c]-1}^T & \text{if } \operatorname{last}[c] \ge 1, \\ \mathbf{e}_c^T & \text{if } \operatorname{last}[c] = 0, \end{cases}$$
     along with lazy offset maintenance $\mathbf{g}^{(i)}$ for $\mathbf{v}_i = P_i^{-1}\mathbf{e}_{\sigma+1}$ reducing range distinct subsequence queries from $O((N+Q)\sigma^2)$ to $O((N+Q)\sigma)$ time and $O(N\sigma)$ space (`CodeChef DISTSUBS`, `Slider`).

6. **Chapter 23 — `ch23-bit-parallel-lcs-seaweed-matrices.qmd` (`T-4B-04`, `T-4B-05`)**:
   - **Allison–Dix Borrow Propagation (Theorem 23.1) & Myers' Edit-Distance Differential Step (Theorem 23.2)**: Verified the 4-instruction two's-complement borrow identity
     $$X = V \mathbin{|} M_c, \qquad Y = (V \ll 1) \mathbin{|} 1, \qquad V' = X \mathbin{\&} \sim(X - Y),$$
     with its complete 3-case bitwise carry/borrow proof and multi-word `adc`/`sbb` carry propagation (`LOJ #6564`), plus Myers' 15-instruction horizontal/vertical difference update $(\Delta H, \Delta V) \in \{-1, 0, +1\}$ with left-boundary increment $b_0 \in \{0, 1\}$.
   - **Tiskin's Seaweed Braid Comb & 3-Family Dominance Identity (Theorems 23.3–23.5)**: Verified the sticky 0-Hecke wiring rule `if (A[i] == B[j] || u > W[j]) swap(u, W[j]);`, the exact 3-family dominance formulas (Prefix–Substring $W^{(i)}[k] < l$, Suffix–Prefix $W[k] \le -i$, and Prefix–Suffix $W[k] > -i$), and Tiskin's $O(K\log K)$ divide-and-conquer Unit-Monge distance-matrix product $\boxdot$ yielding $O(N\log^2 N)$ static and $O(\sqrt{N}\log N)$ dynamic Range LIS (`CF 1810G`, `P9197`).

7. **Chapter 24 — `ch24-goulden-jackson-moment-shift-fps.qmd` (`T-4A-01`, `T-4A-02`)**:
   - **Goulden–Jackson Signed Cluster System & Guibas–Odlyzko Transfer Matrix Duality (Theorems 24.1 & 24.2)**: Verified the signed cluster inclusion-exclusion system $(\Sigma_0 - x\Sigma + \mathbf{1}^T\mathbf{C}(x)\mathbf{1})^{-1}$, the diagonal self-overlap baseline $\mathbf{C}(0) = I_m$ (so $C_{i,i}(0) = 1$), the single-pattern Exact--$k$ OGF
     $$[t^k]F(x, t) = \frac{x^L D_1(x)^{k-1}}{D_0(x)^{k+1}},$$
     and the mandatory valuation-shift protocol $D_1(x) = x^{d_{\min}}\widetilde{D}_1(x)$ ($d_{\min} = \operatorname{per}(P)$) before `poly_ln` / `poly_pow`.
   - **Non-Antichain Embedded Weight Absorption, Cyclic $-xQ'(x)/Q(x)$, & $t = 1 + u$ Binomial Moment Shift (Theorem 24.3)**: Verified how substring containment $P_a \subseteq P_b$ breaks the naive antichain assumption and is repaired by absorbing $\prod (1 + (t_a - 1))^e$ into transition weights, verified the trace identity $\operatorname{tr}(T(x)^n) = [x^n](-xQ'(x)/Q(x))$ for cyclic wrap-around avoidance, and verified the $t = 1 + u$ substitution collapsing the denominator to $(1 - \sigma x)^{j+1}$:
     $$G_j(x) = [u^j]F(x, 1 + u) = \frac{x^L D_1(x)^{j-1}}{(1 - \sigma x)^{j+1}}, \qquad [x^n t^k]F(x, t) = \sum_{j=k}^K (-1)^{j-k}\binom{j}{k}[x^n]G_j(x).$$

8. **Chapter 25 — `ch25-martingale-pgfs-automaton-dp-of-dp.qmd` (`T-4A-03`, `T-4A-04`)**:
   - **Conway's Casino Martingale, Variance & $k$-th Occurrence Renewal (Theorem 25.1)**: Verified the Optional Stopping Theorem derivation of $\mathbb{E}[T_S] = \Phi_S(1)$, the PGF derivative formula $G'_S(1) = \Phi_S(1)$ and variance
     $$\operatorname{Var}(T_S) = \Phi_S(1)^2 + \Phi_S(1) - 2\Phi'_S(1),$$
     and the renewal decomposition $T_{S,k} = T_{S,1} + \sum_{r=2}^k \Delta_r$ where $\mathbb{E}[\Delta_r] = 1/\mathbb{P}(S) = \Sigma^L$ is independent of self-borders of $S$.
   - **Division-Free Pattern Race System $\Phi_{i,j}$ (Theorem 25.2) & 4-Stage `DP套DP` Compiler (Theorem 25.3)**: Verified the $(m+1)\times(m+1)$ linear system for winning probabilities $(p_1, \dots, p_m)$ with seed-prefix offset $\Phi_{S_0, P_j}$ (`[SDOI2017] 硬币游戏`), the 4-stage `DP套DP` compiler (`[TJOI2018] 游园会`, LCS difference vectors $\Delta v_i \in \{0, 1\}^K$, Hopcroft DFA minimization, and Brzozowski's double-reversal minimization), and Bentley–Saxe binary-grouped dynamic Aho–Corasick (`CF 710F`).

---

### 2.3 Part VII: Word Equations, Inverse/Inequality Digraphs, Wheeler/RLBWT, Tree Strings, $SL_2(\mathbb{F}_p)$ & Combinatorics on Words (`Ch 26`–`Ch 30`)

9. **Chapter 26 — `ch26-word-equations-signed-parallel-dsu.qmd` (`T-5A-01`, `T-5A-02`)**:
   - **Lossless Dyadic Block Covering (Theorem 26.1) & Online Potential Amortization (Theorem 26.2)**: Verified the 2-block Sparse-Table covering equivalence for both orientation-preserving ($t = 0$) and orientation-reversing ($t = 1$) substring equations (`[SCOI2016] 萌萌哒`), and the potential bound $\Phi = \sum_{k=0}^K (c_k + p_k) \le 2N(K + 1)$ proving $O((M + N\log N)\alpha(N))$ worst-case online recursion.
   - **Signed Palindrome DSU Root Bit `is_pal[k][r]` (Lemma 26.3), Tree Binary-Lifting DSU & $N \le 10^{18}$ Period Folding**: Verified the two-pass level pushdown (Pass 1 pushing root self-palindromes `is_pal[k][r] == 1` via `unite_block(k - 1, r, r + half, 1)` and Pass 2 cross-swapping offsets on $d = 1$ edges), the $N = 4$ self-loop counterexample when `ru == rv` with `(du ^ dv ^ d) == 1`, the $\le 3$-segment LCA path split for Signed Tree Binary-Lifting DSU, and the 3 contraction engines for $N \le 10^{18}$ word/palindrome equations (Fine–Wilf modulo folding, dihedral $R_2 \circ R_1 = T_\Delta$, and Jeż Recompression).

10. **Chapter 27 — `ch27-inverse-reconstruction-inequality-dags.qmd` (`T-3A-06`, `T-5A-03`)**:
    - **5-Structure Inverse Reconstruction Duality & Chordal Chromatic Product (Theorems 27.1 & 27.2)**: Verified the equality + termination-mismatch decomposition for KMP $\pi$, Z-array, Manacher radii $R$, SA+LCP, and Lyndon arrays, together with the simplicial elimination ordering proof that forbidden predecessors $N_{\text{prev}}(c_r)$ form a clique, yielding the exact chromatic polynomial $\prod_{r=1}^m \max(0, \sigma - \operatorname{deg}_{\text{prev}}(c_r))$.
    - **Mandatory Forward Verification Pass (`Pitfall 27.1`) & Suffix Array Adjacency Theorem (Theorem 27.3)**: Verified the $\pi = [0, 1, 0, 1, 1]$ phantom-equality counterexample ($S = \texttt{aabaa}$ has $\pi[5] = 2 \ne 1$), necessity and backward-induction sufficiency of the SA Adjacency Theorem with empty-suffix sentinel $\operatorname{rk}[N+1] = 0$ (`CF 1526E`, `ARC 044 D`, $\binom{N+K-1-D}{N}$), and the 4-phase Binary-Lifting DSU + $\{0, 1\}$-weighted Tarjan SCC DAG pipeline (`CF 568C` 2-SAT prefix branching).

11. **Chapter 28 — `ch28-debruijn-best-bwt-wheeler-rlbwt.qmd` (`T-5A-04`, `T-5A-05`)**:
    - **De Bruijn Hierholzer & AC-DFA BEST Theorem (Proposition 28.1, Lemma 28.2, Theorem 28.3)**: Verified the post-order Hierholzer lexicographical optimality proof, the Last-Exit Spanning In-Arborescence double-counting bijection for the BEST Theorem (`ABC 336 G`), and the AC-DFA BEST generalization (`UOJ #607`) exposing the **Parallel-Edge Indistinguishability Trap**: dividing by $\prod_{u,c} \operatorname{cnt}(u, c)!$ rather than $\prod_{u,v} A(u, v)!$ whenever distinct characters $c_1 \ne c_2$ transition between the same state pair $(u, v)$.
    - **BWT LF-Mapping (Theorem 28.4), Multi-Cycle Lyndon `BBWT`, Wheeler Graphs (Definition 28.5) & Nishimoto–Tabei $O(1)$ RLBWT Move Structure (Theorem 28.6)**: Verified LF rank preservation, `BBWT` cycle decomposition of $\pi_{FL}$ preserving equal CFL factors $w^d$ as $d$ separate cycles, the Two-Step Vertex–Edge–Vertex interval transition on Wheeler graphs, and Nishimoto–Tabei's $d = 2$ run-splitting construction ($r' \le 2r$) achieving strict $O(1)$ worst-case `MOVE_LF` queries on $N \le 10^{18}$ strings.

12. **Chapter 29 — `ch29-tree-strings-stack-trie-sl2-hashing.qmd` (`T-5A-06`, `T-5B-04`)**:
    - **Dual-Rank Tree Suffix Array $(\operatorname{rk}_k[u], \operatorname{id}_k[u])$ & Tree Kasai Failure (Theorem 29.1, Counterexample 29.1)**: Verified the two-pass stable radix sort ordering by $(\operatorname{rk}_k[u], \operatorname{rk}_k[\operatorname{anc}(u, 2^k)], \operatorname{id}_k[u])$, the 4-vertex sibling counterexample where Kasai's $h[\operatorname{id}[u]] \ge h[\operatorname{id}[\operatorname{fa}(u)]] - 1$ fails, and the $O(\log N)$ binary-lifting `TREE_LCP` replacement (`Luogu P5353`).
    - **Leaf-Rooted Substring Coverage (Theorem 29.2) & Centroid + $\sqrt{M}$ Dual-SAM Split (`[CTSC2010] 珠宝商`)**: Verified the $\le 20$-leaf GSAM coverage theorem (`[ZJOI2015] 诸神眷顾的幻想乡`) and the $\sqrt{M}$ double-thresholding law for `[CTSC2010] 珠宝商` (thresholding both $S_c$ and each subtracted child subtree $|T_{\text{sub}}|$ against $B = \sqrt{M}$ to avoid the $\Theta(NM)$ star-graph blowup).
    - **Deterministic Stack-Trie Path Isomorphism (Theorem 29.3) & $GL_2(\mathbb{F}_p)$ Matrix Involutions (Proposition 29.4)**: Verified that $\operatorname{red}(S[l..r]) = P_{l-1}^{-1}P_r = \operatorname{path}_{\mathcal{T}}(u_{l-1}\uparrow w\downarrow u_r)$ in the Stack-Trie $\mathcal{T}$ with zero junction cancellation (`CF 1223F`), verified Cayley–Hamilton trace-zero $\det = -1$ involutions $M_c^2 = I_2 \in GL_2(\mathbb{F}_p)$, and verified the `([)(])` multi-type directed Dyck counterexample (`Counterexample 29.2`).

13. **Chapter 30 — `ch30-sturmian-singular-thue-morse-morphic-2d.qmd` (`T-5B-01`, `T-5B-02`, `T-5B-03`, `T-5B-07`)**:
    - **Morse–Hedlund Theorem (Theorem 30.1), Sturmian 6-Way Equivalence (Theorem 30.2) & Rytter's Singular Words $w_k$ (`[周任飞 2017]`, Theorem 30.3)**: Verified the right-special factor degree proof of $p_{\mathbf{w}}(n) \ge n + 1$, the irrational circle-rotation partition proof of $p_{\mathbf{w}}(n) = n + 1$, Fibonacci near-commutativity $F_k = \pi_k xy$, and Rytter's singular words $w_k = x\pi_k x$ triggering the longest-repeated-suffix drop from $f_{k-1}$ to $f_{k-2}$ at $m = f_k + f_{k-2}$ in Zhou Renfei's $O(\log n)$ prefix substring counter.
    - **Thue's Overlap-Freeness (Theorem 30.4), Prouhet–Tarry–Escott & Universal `uint64_t` Anti-Hash (Theorem 30.5)**: Verified the parity-decimation proof that $\mathbf{t}$ is overlap-free, the equal-power-sum identity $\sum_{n\in A_k} n^m = \sum_{n\in B_k} n^m$ for $0 \le m < k$, and the Lifting-the-Exponent proof that $v_2(\Phi_k(B)) \ge 1 + \sum_{j=1}^{k-1}(j + 2) \ge k(k+1)/2$, reaching $64$ at $k = 10$ ($N = 1024$) and $76 \ge 66 > 64$ at $k = 11$ ($N = 2048$) for every odd base $B$.
    - **Three-Regime Iterated Morphic Pattern Counting (Theorem 30.6) & 2D Periodicity (`T-5B-07`)**: Verified the $(|\Sigma|+|\Sigma|^2)$ 2-letter junction matrix (Regime 1), $O(m)$ KMP functional composition for mortal/unit-growth morphisms (Regime 2), `CF 1466G` level promotion $r_0$ + Z-border pivot sums (Regime 3), Baker–Bird deduplicated Row-ID AC + vertical KMP, and Amir–Benson 4-class 2D periodicity + Vishkin's $O(1)$ 2D witness duel.

---

## 3. Surgical Fixes Applied During Audit

1. **`strings/chapters/ch19-kmismatch-wavefront-period-dichotomy.qmd` (Line 313)**:
   - Replaced conversational scratchpad phrasing `Wait: if $T[i_1..i_1+M-1]$` with formal textbook exposition `Notice that since $T[i_1..i_1+M-1]$` inside `Problem 19.3 (W3B-20)` Hint 3.
2. **`strings/chapters/ch21-locally-consistent-parsing-slp-attractors.qmd` (Line 406)**:
   - Removed conversational parenthetical `(wait: more simply, let $k^* = \arg\min_{k \in [i+\tau, i+2\tau-1]} R[k]$ or consider the global minimum $k^* \in [i, i + 2\tau - 1]$;` in `Problem 21.3 (W5B-46)` Full Derivation, replacing it with `let $k^* = \arg\min_{k \in [i, i + 2\tau - 1]} R[k]$ be the global minimum on $[i, i + 2\tau - 1]$:`.
3. **`strings/chapters/ch26-word-equations-signed-parallel-dsu.qmd` (Line 587)**:
   - Replaced conversational `—wait: we *must* unite before recursing` in `Problem 26.9 (W5A-49)` Full Derivation with clean formal exposition explaining why uniting at level $k$ before recursing and caching $(r_i, r_j) \in \operatorname{neq}[k]$ on child failure preserves the $O((Q + N\log N)\log^2 N)$ worst-case bound.
4. **`strings/chapters/ch28-debruijn-best-bwt-wheeler-rlbwt.qmd` (Line 660)**:
   - Replaced conversational `wait—if $P_q$ is matched **forward**` in `Problem 28.8 (W5A-50)` Hint 2 with formal exposition.
5. **`strings/chapters/ch30-sturmian-singular-thue-morse-morphic-2d.qmd` (Lines 120–128, 190–192, 417–420, 520–526)**:
   - Inserted missing blank lines after Markdown bullet lists (before `Meanwhile, let us trace...`, `Notice why the ramp jumps...`, `Summing the exponents of $2$...`, and `Precompute the two junction counts...`) to guarantee strict Pandoc list termination, and replaced conversational `wait—for $k \le 10^{18}$` in `Problem 30.6 (W5B-27)` Full Derivation with formal prose.
