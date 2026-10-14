# Phase 1.5 Canonical Master Problem Curation & 24-Chapter Problem Architecture (`PROBLEM_CURATION.md`)

> **Phase 1.5 Round 4 Canonical Curriculum & Problem Curation Blueprint**
> **Source Authority**: Synthesized and audited across all 10 Phase 1 Cohort 3 Wave Reports ([`cohort3_wave_1a`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md) through [`cohort3_wave_5b`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md)), [`problem_archive.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md), [`synthesis_v1_curriculum.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/phase1_5/synthesis_v1_curriculum.md), and the Round 2 Independent Audits ([`critic_round2_taxonomy_and_dag.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/phase1_5/critic_round2_taxonomy_and_dag.md) and [`critic_round2_problem_and_ladder_audit.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/phase1_5/critic_round2_problem_and_ladder_audit.md)).
> **Exact Corpus Accounting (`321` Total Cataloged Problems)**:
> $$\underbrace{\mathbf{192}}_{\text{24 Ch Ladders }(24 \times 8)} + \underbrace{\mathbf{48}}_{\text{6 Blind Checkpoints }(6 \times 8)} + \underbrace{\mathbf{14}}_{\text{Grandmaster Synthesis Reserve}} = \mathbf{254\text{ Unique Accepted Non-Template Problems}}, \qquad \mathbf{254} + \underbrace{\mathbf{67}}_{\text{Quarantined Templates }(R\text{-01..}R\text{-67})} = \mathbf{321\text{ Total Problems}}.$$

---

## 1. Executive Summary & Phase 1.5 Curriculum Accounting

### 1.1 From 10 Phase 1 Research Waves to the 6-Part, 24-Chapter Zero-Forward-Reference Curriculum

During Phase 1 (`Cohort 1` $\to$ `Cohort 2` $\to$ `Cohort 3`), `408` raw problem appearances across 16 online judges were deduplicated into **254 unique non-template competitive programming problems** (`#001`–`#254`) and **67 quarantined bare-template verification problems** (`R-01`–`R-67`). In Phase 1.5, the 10 research collection waves (`Wave 1A` through `Wave 5B`) and all regional (`[ZH]` / `[JA]`) audit buckets have been completely dissolved into a **6-Part, 24-Chapter Zero-Forward-Reference Curriculum Architecture**:

1. **Exact Bijection Over All `254` Accepted Problems**:
   - **Primary Chapter Ladders (`192` Problems = `24 Chapters × 8 Problems`)**: Every chapter `Ch 01` through `Ch 24` features an 8-problem 4-tier smooth difficulty ladder (`2 Stepping Stone [SS-1, SS-2]`, `2 Intermediate [Int-1, Int-2]`, `2 Advanced [Adv-1, Adv-2]`, `2 Mastery [Mas-1, Mas-2]`).
   - **Part-End Blind Topic-Group Checkpoints (`48` Problems = `6 Checkpoints × 8 Problems`)**: `CP-I` through `CP-VI` test unassisted diagnostic routing at the end of each Part using a two-stage spoiler-free format (Stage 1: Raw Constraint & Structural Cues; Stage 2: Collapsible Diagnostic Routing & Algebraic Solution Key).
   - **Grandmaster Multi-Chapter Synthesis Reserve (`14` Problems = `Syn-01`–`Syn-14`)**: Reserved for end-of-book multi-pillar synthesis and cross-part capstones.
   - **Multi-Resolution "Revisited" Index (`12` Cross-References)**: Landmark problems (`CF 438E`, `ABC 222 H`, `Luogu P4389`, `Luogu P4841`, `LOJ 6538`, `LOJ 6728`, `CF 1349D`, `AGC 058 D`, `ABC 240 G`, `ABC 300 Ex`, `ABC 281 Ex`, `AGC 005 F`) are assigned a single primary home slot (`100%` bijection preserved) and explicitly cross-indexed across later chapters that attack the same problem with higher-powered operators.
2. **Strict Prerequisite Ordering (`0` Forward-Reference Violations)**:
   - Every problem assigned to `Ch XX` or `CP-K` is solvable using **only** algebraic rings, formal operators, and algorithms introduced in `Ch 01..Ch XX` (Verified in Round 2 by Critic A and Critic B after applying the 43-problem bijective swap ledger in Section 6.2).
   - All `67` bare library-verification templates (`R-01`–`R-67`) remain strictly quarantined from pedagogical ladders and checkpoints, and are linked as **Implementation Verification Footnotes** at the bottom of the exact chapter that derives their underlying algorithm.

### 1.2 Master 6-Part, 24-Chapter Curriculum & Problem Allocation Matrix

| Part | Ch | Chapter Title & Core Algebraic / Operator Theme | Prereq DAG | Source Waves Dissolved | Ladder (`8`) | Quarantined Templates (`67`) |
| :-: | :-: | :--- | :--- | :--- | :-: | :--- |
| **I** | **01** | The Ring $K[[x]]$, Valuation, Cauchy Convolutions, D&C Product Trees & Newton Inversion (`inv`) | — | `1A (§1), 1B (§1–§4)` | `8` (`2/2/2/2`) | `R-01, R-02, R-03, R-04, R-11, R-44, R-47, R-60` |
| **I** | **02** | Formal Calculus ($D, \vartheta=xD, \int$), Frobenius, $O(NK)$ Sparse Log-Derivative Trick & 1D Newton ($\ln, \exp, \sqrt{\cdot}, P^\alpha$) | Ch 01 | `1A (§2–§3), 2A (§5), 5A (§1)` | `8` (`2/2/2/2`) | `R-06, R-09, R-10, R-12..R-19` |
| **I** | **03** | Unlabeled Multisets (`MSET`), Partition OGFs, Durfee/Pentagonal Splits, Harmonic Euler Transform & Pólya Cycle Index | Ch 01–02 | `1A (§4, §6), 1B (§5), 2A (§6)` | `8` (`2/2/2/2`) | `R-25` |
| **I** | **04** | Exponential Generating Functions (EGFs), Labelled `SET`/`CYC` Assemblies, Boxed Product ($C' = A'B$) & Prüfer/Cayley Trees | Ch 01–02 | `1A (§5, §7), 1B (§3), 3A (§5), 3B (§1)` | `8` (`2/2/2/2`) | `R-24, R-37` |
| **II** | **05** | Rational OGFs $P(x)/Q(x)$, Partial Fractions, Bostan–Mori $[x^N]$ Parity Splitting & Berlekamp–Massey | Ch 01–02 | `1B (§2), 2A (§1), 2B (§4), 4A (§1)` | `8` (`2/2/2/2`) | `R-05, R-39, R-40, R-41, R-64, R-65` |
| **II** | **06** | Binomial Sums, Vandermonde, Falling-Factorial EGF, Taylor Shift $F(x+c)$, Stirling Numbers & $O(d)$ Lagrange | Ch 01–04 | `1B (§4), 2A (§1,§3), 5B (§4)` | `8` (`2/2/2/2`) | `R-20..R-23, R-28, R-29, R-46` |
| **II** | **07** | Affine/Monomial Substitutions, Parity Split, Roots of Unity Filter & Chirp-$Z$ Transform (Bluestein CZT) | Ch 01–06 | `1B (§5), 2A (§1,§5), 5B (§4)` | `8` (`2/2/2/2`) | `R-31` |
| **II** | **08** | Inclusion–Exclusion Sieves: Binomial Inversion, Rook Polynomials, Cluster Method & Goulden–Jackson Matrix | Ch 04–06 | `2B (§1–§4)` | `8` (`2/2/2/2`) | `R-56, R-57` |
| **III** | **09** | Causal Recurrences: CDQ Divide-and-Conquer NTT (`solve(l,r)`) & Hoeven's Online Relaxed Convolution | Ch 01–05 | `1B (§3), 2B (§2), 5A (§3–§4)` | `8` (`2/2/2/2`) | `R-45` |
| **III** | **10** | Implicit Functional Equations $\Phi(x,F)=0$, Coupled Multicolor Newton Iteration & Otter's Unrooted Trees | Ch 02–04, 09 | `2A (§2), 3A (§2–3), 3B (§1–4)` | `8` (`2/2/2/2`) | `R-36` |
| **III** | **11** | Formal Laurent Series $K((x))$, Formal Residue Theorem $\operatorname{Res}_x$, Raney's Lemma & Lagrange Inversion (LIF) | Ch 02–04, 10 | `1A (§7), 3A (§1–2), 3B (§2–4)` | `8` (`2/2/2/2`) | `R-61, R-62` |
| **III** | **12** | Functional Digraphs, Pointed Operator $\vartheta=x\partial_x$, Cactus EGF & Single-$n$ Block-Cut Biconnected Graphs | Ch 04, 10–11 | `3A (§3–§4)` | `8` (`2/2/2/2`) | *(Uses Ch 04/10/11 primitives)* |
| **III** | **13** | Graphical Generating Functions ($2^{\binom{n}{2}}$ CZT), Bipartite/Eulerian/DAG/Tournament Sieves & Matrix-Tree / BEST | Ch 04, 06–08, 12 | `3A (§4)` | `8` (`2/2/2/2`) | `R-38, R-59` |
| **IV** | **14** | Probability Generating Functions (PGFs), $x=1+t$ Moments, Renewal Pole Cancellation, Min–Max IE & Martingales | Ch 04–06, 08 | `2B (§5)` | `8` (`2/2/2/2`) | `R-53, R-54, R-55, R-58` |
| **IV** | **15** | 1D Bounded Lattice Walks: Reflection Principle, Catalan/Motzkin/Schröder Paths, Continuum Limit & Kernel Method | Ch 02, 05, 10–11 | `2A (§2), 3A (§2), 4B (§2)` | `8` (`2/2/2/2`) | `R-63` |
| **IV** | **16** | Multivariate FPS $K[[x_1,\dots,x_d]]$, Twisted $\chi$-Grading, 2D Bostan–Mori & Rational Diagonal Extraction | Ch 03, 05, 07 | `2A (§5), 4A (§1–§3)` | `8` (`2/2/2/2`) | `R-42, R-43` |
| **IV** | **17** | Furstenberg's Diagonal Theorem, 2D Quarter-Plane Obstinate Kernel Method & Multivariate Good–Lagrange | Ch 11, 13, 15–16 | `4B (§1–§4)` | `8` (`2/2/2/2`) | *(Uses Ch 11/15/16 primitives)* |
| **V** | **18** | D-Finite (Holonomic) Series, P-Recursive Sequences, Weyl Closure Properties & Algebraic-to-ODE Compilation | Ch 02, 05, 10–11, 16–17 | `5A (§1–§2)` | `8` (`2/2/2/2`) | `R-66` |
| **V** | **19** | Advanced ODE Techniques: Truncated Taylor Shift (`EI 科技`), Coupled ODEs, WZ Pairs & $O(\sqrt{N}\log N)$ BSGS | Ch 06, 09, 18 | `4A (§3), 5A (§1–§3)` | `8` (`2/2/2/2`) | *(Uses Ch 06/09/18 primitives)* |
| **V** | **20** | Tellegen's Transposition Principle (`mulT`), Subproduct Multipoint Eval, Interpolation & Sampling Shift | Ch 01, 05–07 | `4C (§1–2), 5B (§2,§4)` | `8` (`2/2/2/2`) | `R-26, R-27, R-30` |
| **V** | **21** | Kinoshita–Li $O(N\log^2 N)$ Fast Composition, Power Projection & All-$n$ Compositional Inverse (`revert`) | Ch 11–12, 16, 20 | `4A (§4), 4C (§1), 5B (§2–3)` | `8` (`2/2/2/2`) | `R-32, R-33, R-34, R-35` |
| **VI** | **22** | Tree DP with FPS: Heavy-Light Chain D&C, Static Top Trees, $2\times 2$ Polynomial Matrices & Zero-Divisor Pairs | Ch 01, 06, 09, 20 | `5B (§1)` | `8` (`2/2/2/2`) | `R-67` |
| **VI** | **23** | $q$-Analogues, Gaussian Binomials $\begin{bmatrix}n\\k\end{bmatrix}_q$, $q$-Pentagonal, $q$-Difference Equations, $q$-Lucas & Krawtchouk | Ch 03, 06, 11 | `4A (§3), 5B (§5)` | `8` (`2/2/2/2`) | `R-48, R-49` |
| **VI** | **24** | Bitwise Algebras (FWT/SOS), Set Power Series $\mathcal{R}_n = K[x_1,\dots,x_n]/(x_i^2)$ & Dirichlet Generating Functions $\mathcal{D}_f$ | Ch 02, 04, 12–13, 22 | `1B (§5), 4A (§2), 5B (§6)` | `8` (`2/2/2/2`) | `R-07, R-08, R-50, R-51, R-52` |
| **—** | **CP / Syn** | **6 Part-End Blind Checkpoints (`CP-I`..`CP-VI`: `48`) + Grandmaster Synthesis Reserve (`Syn-01`..`Syn-14`: `14`)** | All Parts | All 10 Waves | **`48 + 14`** | **Total: `254` Accepted + `67` Quarantined = `321`** |

### 1.3 Phase 1 Cohort 3 Wave Source Directory

All wave tags (`1A#...` through `5B#...`) in Sections 2–6 index directly into the 10 Phase 1 Cohort 3 Wave Reports and the Master Encyclopedia:
- **Wave 1A**: [`cohort3_wave_1a_modelling_foundations.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md) — Algebraic Rings, Valuation, Newton Iteration, Symbolic Method, Partitions & Pólya
- **Wave 1B**: [`cohort3_wave_1b_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md) — 1D/2D Convolutions, Reversible Knapsack DP, Binomial Sums & Vandermonde
- **Wave 2A**: [`cohort3_wave_2a_substitutions_transforms.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_2a_substitutions_transforms.md) — Substitutions, Roots of Unity Filter, Taylor Shift, Stirling & Borel/Laplace Bridge
- **Wave 2B**: [`cohort3_wave_2b_ie_pgf_zh_ja_audit.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_2b_ie_pgf_zh_ja_audit.md) — Inclusion–Exclusion, Rook Polynomials, Goulden–Jackson Cluster Method & PGFs
- **Wave 3A**: [`cohort3_wave_3a_lagrange_residues_trees_graphs.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3a_lagrange_residues_trees_graphs.md) — Formal Laurent Series, Formal Residues, Lagrange Inversion, Trees & Graphical Enumeration
- **Wave 3B**: [`cohort3_wave_3b_implicit_zh_ja_audit.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md) — Implicit Functional Equations, Coupled Multicolor Newton Iteration & Otter Dissymmetry
- **Wave 4A**: [`cohort3_wave_4a_multivariate_bostan_mori_diag.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4a_multivariate_bostan_mori_diag.md) — Bostan–Mori, Multivariate FPS, Twisted $\chi$-Grading & Rational Diagonals
- **Wave 4B**: [`cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4b_furstenberg_kernel_good_lagrange.md) — Furstenberg Diagonal Theorem, Lattice Walks, Kernel Method & Good–Lagrange
- **Wave 5A**: [`cohort3_wave_5a_ode_sparse_cdq_relaxed.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md) — D-Finite ODEs, Truncated Taylor Shift (`EI 科技`), CDQ NTT & Relaxed Convolution
- **Wave 5B**: [`cohort3_wave_5b_tree_fps_transposition_compose_q.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md) — Tellegen Transposition (`mulT`), Kinoshita–Li Composition, Tree DP + FPS, $q$-Series & Bitwise/Dirichlet SPS
- **Master Encyclopedia**: [`problem_archive.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md)

---

## 2. Per-Chapter 4-Tier Smooth Difficulty Ladders (`Ch 01`–`Ch 24`, 192 Problems)


### Part I: The Algebraic Engine & Symbolic Translators (Chapters 01–04)

#### Chapter 01: The Ring $K[[x]]$, Valuation, Cauchy Convolutions, Divide-and-Conquer Product Trees & Newton Inversion (`ch01_ring_convolutions_newton_inv.qmd`)
- **Ring / Operator**: $K[x]$, $K[[x]]$, $K[[x]]/(x^N)$, $(K[[x]])^\times$ $\mid$ **Prereqs**: None (Entry Point; assumes black-box `NTT`) $\mid$ **Waves**: `1A (§1), 1B (§1–§4)`
- **Sub-sections & Core Derivations**:
  - **1.1** Formal Power Series vs. Analytic Functions: Sequences $A = (a_0, a_1, \dots) \in K^{\mathbb{N}}$ with indeterminate $x$ as a positional shift symbol.
  - **1.2** The Unit Theorem & Quotient Arithmetic in $K[[x]]/(x^N)$: Proof that $A(x) \in (K[[x]])^\times \iff [x^0]A(x) \in K^\times$.
  - **1.3** The 4 Fundamental Convolution Paradigms; *Additive Cauchy Convolution*: $c_k = \sum_{i+j=k} a_i b_j$.
- **Diagnostic Signal & Scratchpad**: $1\text{D}$ or $2\text{D}$ sums with $i+j=k$ (constant sum) or $i-j=d$ (constant difference, e.g., $1/(i-j)^2$ forces or substring gaps), dynamic knapsack queries with deletions, or independent factors $\prod_{i=1}^M P_i(x)$ with $\sum \deg P_i \le 3 \times 10^5$. $\mid$ *Scratchpad*: 1. Isolate the index invariant: if $i+j=k$, multiply $A(x)B(x)$; if $i-j=d$, reverse $B$ to $B^R(x) = x^{N-1}B(x^{-1})$ so $(i) + (N-1-j) = N-1+d$.
- **Flagship Worked Example (`CF 993E` — Nikita and Order Statistics)**: *Problem*: Given $a_1, \dots, a_N$ and threshold $X$, count subarrays $[l, r]$ containing $k$ elements $< X$ for every $k = 0, \dots, N$. *Derivation*: Let $s_r = \sum_{m=1}^r [a_m < X]$ be the prefix count ($0 \le r \le N$), and let $cnt[v]$ be the frequency of prefix sum $v$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 01`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#019` | **ABC 178 D — Redistribution** | `1B#4` | Restricted Composition $x^3/(1-x)$ |
| **SS-2** | `#043` | **ABC 321 F — #(subset sum = K) with Add/Erase** | `1B#3` | Reversible $O(K)$ DP Division by $(1+x^v)$ |
| **Int-1** | `#004` | **`fps_24_g` — Coin** | `1A#2` | Dynamic Sliding-Window Partition $\prod_{j=k}^{k+L-1}(1-x^j)^{-1}$ & Reversible Coin DP |
| **Int-2** | `#077` | **EDPC M — Candies** | `1B#2` | Prefix-Sum Optimization of $\prod \frac{1-x^{a_i+1}}{1-x}$ |
| **Adv-1** | `#049` | **ARC 028 D — 注文の多い高橋商店** | `1B#6` | Reversible Bounded Knapsack Divide-by-$\frac{1-x^{a_i+1}}{1-x}$ |
| **Adv-2** | `#097` | **CF 993E — Nikita and Order Statistics** | `1B#17` | Prefix-Count Reverse Indexing Difference Convolution |
| **Mas-1** | `#066` | **AGC 001 E — BBQ Hard** | `1B#9` | Offset Lattice-Path Vandermonde Shift $\binom{a_i+a_j+b_i+b_j}{a_i+a_j}$ |
| **Mas-2** | `#107` | **CF 1251F — Red-White Fence** | `1A#11` | $2x(1+2x)^{c_1}(1+x)^{2c_2}$ Frequency Grouping |

> **Ch 01 Quarantined Library Verification Footnote (§5)**: `R-01`, `R-02`, `R-03`, `R-04`, `R-11`, `R-44`, `R-47`, `R-60`.

#### Chapter 02: Formal Calculus ($D, \vartheta=xD, \int$), Characteristic-$p$ Frobenius, the $O(NK)$ Sparse Logarithmic-Derivative Trick & 1D Newton ($\ln, \exp, \sqrt{\cdot}, P^\alpha$) (`ch02_calculus_frobenius_sparse_ode_newton.qmd`)
- **Ring / Operator**: $D: K[[x]] \to K[[x]]$, $\vartheta = xD$, $\int: K[[x]]_{<p-1} \to xK[[x]]$, Frobenius $A(x)^p \equiv A(x^p) \pmod p$, $1 + xK[[x]]$ $\mid$ **Prereqs**: Ch 01 ($K[[x]]$, Valuation, Newton `inv`) $\mid$ **Waves**: `1A (§2–§3), 2A (§5), 5A (§1)`
- **Sub-sections & Core Derivations**:
  - **2.1** Formal Differentiation $D$, Pointing Operator $\vartheta = xD$ & Formal Integration $\int$: Linear maps $D(\sum a_n x^n) = \sum (n+1)a_{n+1}x^n$ and $\vartheta(\sum a_n x^n) = \sum n a_n x^n$.
  - **2.2** Characteristic-$p$ Frobenius Endomorphism: Proof that in $\mathbb{F}_p[[x]]$, $\binom{p}{k} \equiv 0 \pmod p$ for $0 < k < p$, so $A(x)^p = A(x^p)$ and $D(A(x)^p) = 0$.
  - **2.3** Formal Logarithm $\ln$, Exponential $\exp$, and the 3-Way Modular Reduction Trap for $A(x)^\alpha \bmod x^N$.
  - **2.4** 1D Newton Square Root $\sqrt{A(x)}$ & The $O(NK)$ Sparse Logarithmic-Derivative Trick.
- **Diagnostic Signal & Scratchpad**: Computing $(P(x))^M \bmod x^N$ where $P(x)$ has $K \le 20$ non-zero terms (`CF 1096G`), extracting power sums $S_k = \sum a_i^k$ via $-\vartheta \ln(1 - a_i x)$ (`AtCoder fps_24_q`), or solving quadratic Catalan equations $C = 1 + x C^2$ via $\sqrt{1-4x}$. $\mid$ *Scratchpad*: Differentiate $G = P^\alpha$ logarithmically to obtain $P G' = \alpha P' G$ and extract $[x^n]$ in $O(NK)$ time.
- **Flagship Worked Example (`CF 1096G` — Lucky Tickets)**: *Problem*: Compute $[x^S] (1 + x + x^2 + \dots + x^9)^k \pmod{998244353}$ for $k = N/2 \le 10^5, S \le 9k$. *Derivation*: Write $P(x) = \frac{1 - x^{10}}{1 - x}$. Instead of NTT or $\ln/\exp$, note $G(x) = (1 - x^{10})^k (1 - x)^{-k}$ or apply the 2-sparse relation $(1 - x)(1 - x^{10}) G'(x) = k(1 - 10x^9 + 9x^{10}) G(x)$, unrolling $g_n$ in $O(S)$ time (or $O(10 \cdot S)$ via sparse power recurrence).

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 02`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#238` | **yukicoder 1145 — Sum of Powers** | `2A#35` | Newton–Girard Power Sums $-\sum_{i=1}^n \frac{-a_i x}{1 - a_i x} = -x \frac{d}{dx}\ln\prod(1 - a_i x)$ |
| **SS-2** | `#165` | **Luogu P4389 (0-1 Subset Sum Variant) / AtCoder FPS Subset Sum via ln/exp** | `1D#4` | Subset-Sum Product $\prod(1 + x^{a_i})$ via Logarithmic Derivative & $\exp$ |
| **Int-1** | `#101` | **CF 1096G — Lucky Tickets** | `1B#8` | $O(NK)$ Sparse Power ODE $(1-x)(1-x^{10})G' = k P' G$ (Zero NTTs) |
| **Int-2** | `#222` | **LOJ 6261 — 一个人的高三 (Lonely Senior Year)** | `1A#10` | Series Power $F(x)^k$ & Binomial Series Expansion $(1-x)^{-\alpha}$ |
| **Adv-1** | `#157` | **Luogu P4705 — 玩游戏** | `1A#24` | Newton–Girard Power Sums $\ln\prod(1 - a_i x)$ + Binomial Convolution |
| **Adv-2** | `#084` | **CF 438E — The Child and Binary Tree** | `1A#7` | Explicit Quadratic Radical $F(x) = \frac{2}{1 + \sqrt{1 - 4x C(x)}}$ via `poly_sqrt` + `poly_inv` (revisited via CDQ in Ch 09 & Newton in Ch 10) |
| **Mas-1** | `#030` | **ABC 267 Ex — Odd Sum** | `1B#7` | Parity Split $\frac{P(x)-P(-x)}{2}$ + Logarithmic Derivative $\ln/\exp$ |
| **Mas-2** | `#091` | **CF 891E — Lust** | `1A#16` | Polynomial Product $\prod_{i=1}^n (a_i - x)$ + Formal Derivative / Coefficient Extraction |

> **Ch 02 Quarantined Library Verification Footnote (§5)**: `R-06`, `R-09`, `R-10`, `R-12`, `R-13`, `R-14`, `R-15`, `R-16`, `R-17`, `R-18`, `R-19`.

#### Chapter 03: Unlabeled Multisets (`MSET`), Partition OGFs, Durfee/Pentagonal Splits, Harmonic Euler Transform & Pólya Cycle Index (`ch03_mset_partitions_euler_polya.qmd`)
- **Ring / Operator**: $\operatorname{SEQ}, \operatorname{PSET}, \operatorname{MSET}: xK[[x]] \to K[[x]]$, Cycle Index Polynomial $Z_G(s_1, \dots, s_m) \in \mathbb{Q}[s_1, \dots, s_m]$ $\mid$ **Prereqs**: Ch 01–02 ($K[[x]]$, $\ln$, $\exp$, $O(NK)$ sparse recurrences) $\mid$ **Waves**: `1A (§4, §6), 1B (§5), 2A (§6)`
- **Sub-sections & Core Derivations**:
  - **3.1** Flajolet–Sedgewick Unlabeled Combinatorial Operators: Disjoint union $+$, Cartesian product $\times$, sequence $\operatorname{SEQ}(\mathcal{A}) = (1 - A(x))^{-1}$, powerset $\operatorname{PSET}(\mathcal{A}) = \prod_{n \ge 1}(1 + x^n)^{a_n}$, and multiset $\operatorname{MSET}(\mathcal{A}) = \prod_{n \ge 1}(1 - x^n)^{-a_n}$.
  - **3.2** The Euler Transform & $O(N \log N)$ Harmonic $\ln$-$\exp$ Compression; $$\ln \operatorname{MSET}(\mathcal{A})(x) = \sum_{n \ge 1} a_n \ln\left(\frac{1}{1-x^n}\right) = \sum_{k \ge 1} \frac{A(x^k)}{k} = \sum_{m=1}^N x^m \sum_{d \mid m} \frac{d \cdot a_d}{m}$$.
  - **3.3** The Inverse Euler Transform: Given $F(x) = \operatorname{MSET}(\mathcal{A})(x)$, recover the generator sequence $a_n$ by taking $L(x) = \ln F(x)$, setting $b_n = n [x^n] L(x) = \sum_{d \mid n} d a_d$, and applying number-theoretic Möbius inversion $n a_n = \sum_{d \mid n} \mu(n/d) b_d$ (`yukicoder 899 / LOJ 6268`, `Luogu P3784`).
  - **3.4** Integer Partitions, Durfee Squares & Euler's Pentagonal Number Theorem; Partition OGF $P(x) = \prod_{k \ge 1}(1 - x^k)^{-1}$.
  - **3.5** Burnside's Lemma & Pólya's Cycle Index Theorem: Group actions $G \curvearrowright X$, cycle index polynomial $Z_G(s_1, \dots, s_n) = \frac{1}{\lvert G \rvert} \sum_{g \in G} \prod_{k=1}^n s_k^{c_k(g)}$, Pólya substitution $s_k \gets A(x^k)$, and enumerating non-isomorphic graphs via $Z_{S_n}^{(2)}$ over partitions of $n \le 60$ (`Luogu P4727`).
- **Diagnostic Signal & Scratchpad**: Unlabeled multisets, knapsack items with identical weights $w_i \le N$, partition counts with bounded part sizes/multiplicities, or counting objects up to symmetry group $C_n, D_n, S_n$. $\mid$ *Scratchpad*: 1. Group items by weight into frequency buckets $cnt[w]$. 2. Replace $\prod_w (1 - x^w)^{-cnt[w]}$ (or $\prod_w \frac{1 - x^{w(c_w+1)}}{1 - x^w}$) by $\exp\left(\sum_{w} cnt[w] \sum_{k=1}^{\lfloor N/w \rfloor} \frac{x^{wk}}{k}\right)$.
- **Flagship Worked Example (`Luogu P4389` — 付公主的背包)**: *Problem*: Given $N \le 10^5$ item types of volume $v_i \le M \le 10^5$ (each with infinite supply), compute the number of ways to fill volume $s$ for all $1 \le s \le M \pmod{998244353}$. *Derivation*: Count $cnt[v] = \#\{i : v_i = v\}$. Then $F(x) = \prod_{v=1}^M (1 - x^v)^{-cnt[v]}$. Compute $L(x) = \ln F(x) \bmod x^{M+1}$ in $O(M \log M)$ time via a harmonic loop `for v=1..M: if cnt[v]: for k=1..M/v: L[v*k] += cnt[v] * inv[k]`, then return $\exp(L(x)) \bmod x^{M+1}$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 03`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#001` | **`fps_24_a` — Snack / Snacks** | `1A#1` | OGF Product & Polynomial Power $P(x)^D$ / Subset-Sum $\ln$-$\exp$ |
| **SS-2** | `#188` | **Luogu P6189 — [NOI Online #1] 跑步** | `1A#6` | Integer Partition $O(N\sqrt{N})$ Durfee Square / Pentagonal Number Theorem |
| **Int-1** | `#153` | **Luogu P4389 — 付公主的背包** | `1A#7a` | Harmonic $\ln$-$\exp$ Subset-Sum Compression ($O(M \log M)$) |
| **Int-2** | `#009` | **`fps_24_n` — Coin 2 / Coins 2** | `1A#7b` | Harmonic $\ln$-$\exp$ Compression $\prod(1+x^{A_i})$ & Bounded Numerator $\prod(1-x^{A_i+1})$ |
| **Adv-1** | `#223` | **yukicoder 899 / LOJ 6268 — 逆オイラー変換 (Inverse Euler)** | `1A#8` | Möbius Inversion on $\ln A(x)$ to Recover Generator Sequence |
| **Adv-2** | `#221` | **LOJ 6089 — 小 Y 的背包计数问题** | `2A#37` | $\sqrt{N}$ Split: Small Items DP + Large Items Partition Pentagonal Number |
| **Mas-1** | `#150` | **Luogu P3784 — [SDOI2017] 遗忘的集合** | `1B#25` | Inverse Euler Transform (Recovering Item Set from Subset Sums) |
| **Mas-2** | `#159` | **Luogu P4727 — [HNOI2009] 图的同构记数** | `2A#39` | Burnside's Lemma + Partition Cycle Index $Z(S_n)$ |

> **Ch 03 Quarantined Library Verification Footnote (§5)**: `R-25`.

#### Chapter 04: Exponential Generating Functions (EGFs), Labelled `SET`/`CYC` Assemblies, Boxed Product ($C' = A'B$) & Prüfer/Cayley Tree Enumeration (`ch04_egf_set_cyc_boxed_prufer.qmd`)
- **Ring / Operator**: $K_{\text{EGF}}[[x]]$ under Binomial Convolution $\binom{n}{k}$, $\operatorname{SET}(A)=\exp(A)$, $\operatorname{CYC}(A)=\ln(1-A)^{-1}$, Boxed Product $A^{\square} * B = \int A'(x)B(x)dx$, Prüfer Multinomial Ring $\mid$ **Prereqs**: Ch 01–02 ($K[[x]]$, Formal Calculus $D/\int$, $\ln$, $\exp$) $\mid$ **Waves**: `1A (§5, §7), 1B (§3), 3A (§5), 3B (§1)`
- **Sub-sections & Core Derivations**:
  - **4.1** Exponential Generating Functions (EGFs) & Binomial Convolution: Encoding labeled structures $A(x) = \sum_{n \ge 0} a_n \frac{x^n}{n!}$ so $C(x) = A(x)B(x) \iff c_n = \sum_{k=0}^n \binom{n}{k} a_k b_{n-k}$ corresponds to relabeling disjoint unions.
  - **4.2** The Labeled Symbolic Dictionary (`SEQ`, `SET`, `CYC`, Boxed Product); Ordered tuple $\operatorname{SEQ}_k(\mathcal{A}) = A(x)^k$, unordered set $\operatorname{SET}(\mathcal{A}) = \exp(A(x))$, directed cycle $\operatorname{CYC}(\mathcal{A}) = \ln\left(\frac{1}{1-A(x)}\right)$, undirected cycle $\frac{1}{2}\left(\ln\frac{1}{1-A(x)} - A(x) - \frac{A(x)^2}{2}\right)$.
  - **4.3** The Exp–Log Connected Component Bridge: For any labeled graph/object class where an object is a disjoint union of connected components ($\mathcal{G} = \operatorname{SET}(\mathcal{C})$), $G(x) = \exp(C(x)) \iff C(x) = \ln G(x)$ (`Luogu P4841`, `AtCoder fps_24_m`).
  - **4.4** Hyperbolic Parity Filters ($\sinh x, \cosh x$) & Roots-of-Unity EGF Sieves: Using $\cosh x = \frac{e^x + e^{-x}}{2}$ (even multiplicities) and $\sinh x = \frac{e^x - e^{-x}}{2}$ (odd multiplicities) to count colorings with parity constraints (`Luogu P5401`).
  - **4.5** Prüfer Sequences & Degree-Constrained Labeled Trees; Bijection between labeled trees on $n$ vertices with degrees $(d_1, \dots, d_n)$ and sequences in $[n]^{n-2}$ where vertex $i$ appears $d_i - 1$ times.
- **Diagnostic Signal & Scratchpad**: Labeled vertices/positions, permutations decomposed into cycles, connected labeled graphs on $n$ vertices, or tree counting where vertex degrees $d_i \in D_i$ are constrained independently. $\mid$ *Scratchpad*: 1. If elements are distinguishable, divide by $n!$ at the start and multiply by $n!$ at the end.
- **Flagship Worked Example (`ABC 303 Ex` — Constrained Tree Degree)**: *Problem*: Given a set of allowed vertex degrees $S \subseteq \{1, \dots, N-1\}$, count labeled trees on $N \le 2 \times 10^5$ vertices whose degrees all lie in $S \pmod{998244353}$. *Derivation*: By Prüfer's bijection, each vertex $i \in [1, N]$ independently contributes a Prüfer multiplicity $d_i - 1 \in \{s - 1 : s \in S\}$ summing to $N - 2$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 04`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#002` | **`fps_24_e` — Sequence 2** | `1A#15` | Labeled Multiset Permutation EGF $\prod_{m=1}^M \sum_{j=0}^m \frac{x^j}{j!}$ |
| **SS-2** | `#007` | **`fps_24_m` — Value of Permutation** | `1A#20` | Cycle Decomposition EGF $\ln\frac{1}{1-x}$ & Pointer Tracking |
| **Int-1** | `#161` | **Luogu P4841 — [集训队作业2013] 城市规划** | `1A#14` | Labeled Connected Graphs $C(x) = \ln G(x)$ via EGF Logarithm |
| **Int-2** | `#008` | **`fps_24_n` — Tree** | `3A#2` | Prüfer Sequence Degree-Distribution EGF $n![x^{n-2}]\prod E_{d_i}(x)$ |
| **Adv-1** | `#083` | **CF 407E / Gym — k-Cycle** | `1A#21` | Constrained Cycle-Length Permutation EGF $\exp(\sum_{k \in S} \frac{x^k}{k})$ |
| **Adv-2** | `#011` | **`fps_24_q` — Dice** | `1B#18` | Newton–Girard Power Sums $-\ln\prod(1 - A_i x)$ + EGF Moment Expansion |
| **Mas-1** | `#041` | **ABC 303 Ex — Constrained Tree Degree** | `3A#5` | Prüfer Sequence Degree-Constrained EGF $[x^{N-2}] P(x)^N$ via Dense $\exp(N \ln P(x))$ in $O(N \log N)$ |
| **Mas-2** | `#174` | **Luogu P5401 — [CTS2019] 珍珠** | `1B#14` | Parity EGF $\left(\frac{e^x+e^{-x}}{2}\right)^k$ + Binomial Inversion |

> **Ch 04 Quarantined Library Verification Footnote (§5)**: `R-24`, `R-37`.


### Part II: Rational Recurrences, Binomial Sums, Sieves & Pattern Inclusion-Exclusion (Chapters 05–08)

#### Chapter 05: Rational Generating Functions $K(x)$, Partial Fractions, 1D Bostan–Mori & Berlekamp–Massey (`ch05_rational_bostan_mori_berlekamp_massey.qmd`)
- **Ring / Operator**: Rational Subring $K(x)_0 = \{P(x)/Q(x) : Q(0) \neq 0\} \subset K[[x]]$, Shift-Invariant Recurrence Space $\mid$ **Prereqs**: Ch 01 ($K[[x]]$, Polynomial Multiplication & Inversion) $\mid$ **Waves**: `1B (§2), 2A (§2), 4A (§1–§2)`
- **Sub-sections & Core Derivations**:
  - **5.1** The Fundamental Theorem of Rational Generating Functions: Equivalence between constant-coefficient linear recurrences $a_n = \sum_{i=1}^d c_i a_{n-i}$ ($n \ge d$) and rational functions $F(x) = \frac{P(x)}{Q(x)}$ with $Q(x) = 1 - \sum_{i=1}^d c_i x^i$ and $P(x) = (F(x) Q(x)) \bmod x^d$.
  - **5.2** Partial Fraction Decomposition & Heaviside Cover-Up: Distinct-root residue formula $c_i = \frac{P(r_i^{-1})}{\prod_{j \neq i}(1 - \lambda_j / \lambda_i)}$.
  - **5.3** 1D Bostan–Mori Algorithm ($O(d \log d \log N)$); Exploiting $Q(x)Q(-x) = \widetilde{Q}(x^2)$ to write $[x^N] \frac{P(x)}{Q(x)} = [x^{\lfloor N/2 \rfloor}] \frac{\mathcal{E}_{N \bmod 2}(P(x)Q(-x))}{\widetilde{Q}(x)}$, reducing $N \le 10^{18}$ in $\lfloor \log_2 N \rfloor$ steps.
  - **5.4** Berlekamp–Massey Algorithm ($O(d^2)$) & Minimum-Polynomial Discovery: Finding the shortest linear recurrence $Q(x)$ generating $a_0, \dots, a_{2d-1}$ over $\mathbb{F}_p$, and pairing BM + Bostan–Mori as an automated black-box solver when a sequence is provably rational of degree $d \le 5000$.
- **Diagnostic Signal & Scratchpad**: Huge index $N \le 10^{18}$ with state space / window width $d \le 5 \times 10^4$ (too large for $O(d^3 \log N)$ matrix exponentiation, right in the sweet spot for $O(d \log d \log N)$ Bostan–Mori!). $\mid$ *Scratchpad*: 1. Check if the denominator $Q(x)$ can be written explicitly (e.g., $1 - x - x^M$ or transfer-matrix characteristic polynomial) or discovered from the first $2d$ terms via Berlekamp–Massey.
- **Flagship Worked Example (`ABC 300 Ex` — Fibonacci: Revisited)**: *Problem*: Given $a_n = a_{n-1} + a_{n-2} + \dots + a_{n-K}$, compute $a_N \bmod 998244353$ for $N \le 10^{18}, K \le 2.5 \times 10^5$. *Derivation*: $Q(x) = 1 - x - x^2 - \dots - x^K$. Running Bostan–Mori directly on $Q(x)$ takes $O(K \log K \log N)$ time.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 05`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#104` | **CF 1117D — Magic Gems** | `4A#P4` | Sparse Denominator $1/(1-x-x^M)$ + Bostan–Mori |
| **SS-2** | `#034` | **ABC 279 G — At Most 2 Colors** | `2B#B3` | Sliding-Window Transfer-Matrix Rational OGF $P(x)/Q(x)$ |
| **Int-1** | `#187` | **Luogu P6078 — [CEOI2004] Sweet** | `1B#8` | Sparse Denominator $(1-x)^{-n} \prod (1-x^{m_i+1})$ |
| **Int-2** | `#069` | **AGC 013 E — Placing Squares** | `2B#D5` | Combinatorial Split-or-Pass $3 \times 3$ Matrix / Rational OGF |
| **Adv-1** | `#040` | **ABC 300 Ex — Fibonacci: Revisited** | `2A#8` | 3-Sparse Denominator $(1-x)Q(x) = 1-2x+x^{K+1}$ + Bostan–Mori at $N \le 10^{18}$ |
| **Adv-2** | `#081` | **AISing 2020 F — Two Snuke** | `1B#22` | 10-Tuple Difference Weight OGF $F(z) = \frac{z^5(1+z)^{11}}{(1-z^2)^{16}}$ + Parity Extraction |
| **Mas-1** | `#177` | **Luogu P5487 — [BJOI2019] 勘破神机** | `4A#P18` | Berlekamp–Massey + Bostan–Mori + Stirling S1 Power Sums |
| **Mas-2** | `#073` | **AGC 054 E — ZigZag Break** | `2A#21` | Difference Cancellation / Telescoping Rational Series |

> **Ch 05 Quarantined Library Verification Footnote (§5)**: `R-05`, `R-39`, `R-40`, `R-41`, `R-64`, `R-65`.

#### Chapter 06: Binomial Sums, Vandermonde, Snake Oil, Taylor Shift, Falling Factorials, Stirling/Eulerian Duality & $O(d)$ Consecutive Lagrange Interpolation (`ch06_binomial_snake_oil_taylor_shift_stirling.qmd`)
- **Ring / Operator**: Shift Automorphism $\tau_c: A(x) \mapsto A(x+c)$, Falling-Factorial Basis $\{x^{\underline{k}}\}$, Exponential Generating Kernel $e^x$, Stirling/Eulerian Transition Matrices $\mid$ **Prereqs**: Ch 01–02, Ch 04 (Cauchy/Binomial Convolution, EGFs $e^x$) $\mid$ **Waves**: `1A (§8), 1B (§4), 2A (§1, §3–§4)`
- **Sub-sections & Core Derivations**:
  - **6.1** The Golden Rule of Index Alignment & Vandermonde Convolution: Decoupling $\sum_k \alpha(n)\beta(k)\gamma(n-k) a_k b_{n-k}$ into Cauchy/reverse-indexed convolutions and upper-index negation $\binom{-r}{k} = (-1)^k \binom{r+k-1}{k}$.
  - **6.2** The First Two Binomial Sum Engines (Snake Oil & Egorychev Polynomial Extraction) & The Falling-Factorial Basis $\{x^{\underline{k}}\}$.
  - **6.3** Polynomial Taylor Shift $A(x + c)$, Generalized $\alpha$-Euler Transform $(1 - cx)^{-\alpha} F\!\left(\frac{ax}{1 - cx}\right)$ (Failure Mode #14), & Projective Möbius Transforms.
  - **6.4** Stirling Numbers $\left[\begin{smallmatrix} n \\ k \end{smallmatrix}\right], \left\{\begin{smallmatrix} n \\ k \end{smallmatrix}\right\}$, Eulerian Numbers $\left\langle\begin{smallmatrix} n \\ k \end{smallmatrix}\right\rangle$ & $O(d)$ Consecutive Lagrange Interpolation.
- **Diagnostic Signal & Scratchpad**: Sums of the form $\sum_k \binom{n}{k} k^m x^k$ ($n \le 10^9, m \le 2 \times 10^5$), tree/grid DPs whose state values are polynomials of degree $d \le N$ evaluated at huge $X \le 10^9$, or permutation statistics by cycles/prefix maxima/ascents. $\mid$ *Scratchpad*: 1. Whenever $k^m$ multiplies $\binom{n}{k}$, immediately expand $k^m = \sum_{j=0}^m \left\{\begin{smallmatrix} m \\ j \end{smallmatrix}\right\} k^{\underline{j}}$ so $k^{\underline{j}} \binom{n}{k} = n^{\underline{j}} \binom{n-j}{k-j}$ pulls $k$ out of the polynomial! 2.
- **Flagship Worked Example (`CF 923E` — Perpetual Subtraction)**: *Problem*: An integer $x \in [0, N]$ is repeatedly replaced by a uniform random integer in $[0, x]$ for $M \le 10^{18}$ steps. *Derivation*: One step maps $P(x) = \sum_{i=0}^N p_i x^i \mapsto \sum_{i=0}^N \frac{p_i}{i+1} \frac{1-x^{i+1}}{1-x}$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 06`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#005` | **`fps_24_h` — Jump** | `2A#1` | Bivariate Rational Substitution $\frac{1-y}{1-2y-x}$ & Taylor Shift |
| **SS-2** | `#055` | **ARC 110 D — Binomial Coefficient is Fun** | `1B#16` | Vandermonde Convolution $\prod (1-x)^{-(A_i+1)}$ |
| **Int-1** | `#193` | **Luogu P6620 — [省选联考2020 A卷] 组合数问题** | `2A#24` | Polynomial-Weighted Binomial Sum via Falling Factorials $k^{\underline{j}}\binom{n}{k} = n^{\underline{j}}\binom{n-j}{k-j}$ |
| **Int-2** | `#080` | **KUPC 2019 K — One or All** | `2A#4` | Projective Möbius Substitution $(1-x)^N A(\frac{1+x}{1-x})$ |
| **Adv-1** | `#094` | **CF 923E — Perpetual Subtraction** | `2A#2` | Diagonalization of Pascal / Shift Operator via Taylor Shift |
| **Adv-2** | `#096` | **CF 960G — Bandit Blues** | `1A#23` | Unsigned Stirling S1 $\left[\begin{smallmatrix} n-1 \\ A+B-2 \end{smallmatrix}\right] \binom{A+B-2}{A-1}$ via Doubling Shift |
| **Mas-1** | `#098` | **CF 995F — Cowmpany Cowmpensation** | `5B#D6` | Tree DP Polynomial Degree Bound + $O(N)$ Lagrange Interpolation |
| **Mas-2** | `#109` | **CF 1278F — Cards** | `2A#29` | Expected $K$-th Moment of Binomial via Falling Factorials |

> **Ch 06 Quarantined Library Verification Footnote (§5)**: `R-20`, `R-21`, `R-22`, `R-23`, `R-28`, `R-29`, `R-46`.

#### Chapter 07: Roots of Unity Filter, Cyclotomic Quotient Rings $\mathbb{F}_p[\omega]/(\Phi_m(\omega))$ & Bluestein's Chirp Z-Transform (CZT) (`ch07_roots_of_unity_cyclotomic_czt.qmd`)
- **Ring / Operator**: Cyclic Group Algebra $K[C_m] \cong K[x]/(x^m - 1)$, Cyclotomic Quotient Ring $\mathbb{F}_p[\omega]/(\Phi_m(\omega))$, Bluestein Identity $ij = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$ $\mid$ **Prereqs**: Ch 01, Ch 05 (Cauchy Convolution, Rational Series) $\mid$ **Waves**: `2A (§7), 5B (§4)`
- **Sub-sections & Core Derivations**:
  - **7.1** The Roots of Unity Filter (`单位根反演`) & Cyclic Convolution $\bmod (x^m - 1)$.
  - **7.2** Cyclotomic Quotient Rings $\mathbb{F}_p[\omega]/(\Phi_m(\omega))$ When $m \nmid (p-1)$.
  - **7.3** Bluestein's Chirp Z-Transform (CZT, $O((N+M)\log(N+M))$); Using the identity $ij = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$ (or $2ij = (i+j)^2 - i^2 - j^2$) to rewrite geometric-progression evaluation $y_j = A(c \cdot q^j) = q^{-\binom{j}{2}} \sum_{i=0}^{N-1} \left(a_i c^i q^{-\binom{i}{2}}\right) q^{\binom{i+j}{2}}$ as a single reverse-indexed Cauchy convolution!.
- **Diagnostic Signal & Scratchpad**: Summing $\binom{N}{k}$ over $k \equiv r \pmod m$ or involving $\lfloor k/m \rfloor = \frac{k - (k \bmod m)}{m}$, cyclic walks on $C_m$, multiplicative convolutions $i \cdot j \bmod P$, or evaluating $A(q^0), A(q^1), \dots, A(q^{M-1})$. $\mid$ *Scratchpad*: 1. If $m \mid (p-1)$ and $m \le 10^6$, compute $\omega_m = g^{(p-1)/m} \bmod p$ and evaluate $F(\omega_m^j)$ directly (or via CZT if $F$ is a polynomial rather than a closed form).
- **Flagship Worked Example (`Luogu P5591` — 小猪佩奇学数学)**: *Problem*: Compute $\sum_{k=0}^n \binom{n}{k} p^k \lfloor k/w \rfloor \pmod{998244353}$ for $n \le 10^9, w \in \{2^0, \dots, 2^{20}\}$. *Derivation*: Write $\lfloor k/w \rfloor = \frac{k - (k \bmod w)}{w}$. The first part is $\frac{1}{w} \sum_{k=0}^n k \binom{n}{k} p^k = \frac{np(1+p)^{n-1}}{w}$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 07`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#224` | **LOJ 6485 — LJJ 学二项式定理** | `2A#40` | Mod-4 Roots-of-Unity Filter $(1 \pm x)^n, (1 \pm ix)^n$ |
| **SS-2** | `#248` | **BZOJ 3328 — PYXFIB** | `2A#41` | Matrix Fibonacci + Bluestein / Roots-of-Unity Filter |
| **Int-1** | `#178` | **Luogu P5591 — 小猪佩奇学数学** | `2A#46` | Floor-Sum Roots-of-Unity Filter $\sum_{k=0}^n \binom{n}{k} p^k \lfloor k/w \rfloor$ |
| **Int-2** | `#143` | **Luogu P3321 — [SDOI2015] 序列统计** | `5B#D3` | Primitive Root Discrete Log + Cyclic Convolution $\bmod (x^{p-1}-1)$ |
| **Adv-1** | `#147` | **Luogu P3702 — [SDOI2017] 序列计数** | `1B#14` | Prime Complementary Sieve + Cyclic Convolution $\bmod (x^p - 1)$ |
| **Adv-2** | `#012` | **`fps_24_r` — Random Walk** | `2A#47` | Cyclic Convolution $\bmod (x^M - 1)$ via Roots of Unity & Catalan Kernel |
| **Mas-1** | `#092` | **CF 901E — Periodicovsky** | `5B#D10` | Cyclic Chirp-$Z$ Transform (Bluestein's Algorithm) |
| **Mas-2** | `#168` | **Luogu P5293 — [HNOI2019] 白兔之舞** | `2A#48` | $k \times k$ Matrix Walk Modulo $x^L - 1$ + Bluestein Chirp-$Z$ |

> **Ch 07 Quarantined Library Verification Footnote (§5)**: `R-31`.

#### Chapter 08: Connected-Component Inclusion-Exclusion (`连续段容斥`), Rook Polynomials, Smirnov Words & Goulden–Jackson Cluster Method (`ch08_connected_component_ie_rook_goulden_jackson.qmd`)
- **Ring / Operator**: Incidence Poset Valuation, Hit/Rook Polynomials, Smirnov Word Substitution $x_i \mapsto \frac{x_i}{1+x_i}$, Overlap Matrix $(I + C(x))^{-1}$ over $K[[x]]^m$ $\mid$ **Prereqs**: Ch 01, Ch 04, Ch 05, Ch 06 (OGFs, EGFs, Rational Series, Binomial Inversion / Taylor Shift) $\mid$ **Waves**: `2B (§A–§D)`
- **Sub-sections & Core Derivations**:
  - **8.1** Binomial Inversion ("At Least $k$" $\iff$ "Exact $k$") via Reverse NTT; If $g_j = \sum_{k=j}^n \binom{k}{j} f_k$ counts configurations with at least $j$ chosen violations, then $f_k = \sum_{j=k}^n (-1)^{j-k} \binom{j}{k} g_j \iff F(x) = G(x-1)$, evaluated for all $k=0 \dots n$ in one Taylor shift (`Luogu P4491`, `ABC 172 E`).
  - **8.2** Rook Polynomials, Hit Polynomials & Forbidden Bipartite Matchings; For any board $B \subseteq [n] \times [n]$ with rook numbers $r_j(B)$, the number of permutations avoiding $B$ is $\sum_{j=0}^n (-1)^j r_j(B) (n-j)!$.
  - **8.3** Connected-Component Inclusion–Exclusion (`连续段容斥`) & Smirnov Words; Replacing "no two adjacent elements share a color/property" by partitioning each color class of size $c_i$ into $b$ maximal contiguous blocks with signed weight $(-1)^{c_i - b}$, yielding the per-color block EGF $\sum_{b=1}^{c_i} (-1)^{c_i-b} \binom{c_i-1}{b-1} \frac{x^b}{b!}$ (`CF 840C`) and the Smirnov word substitution $A_{\text{Smirnov}}(x_1, \dots, x_m) = \left(1 - \sum_{i=1}^m \frac{x_i}{1+x_i}\right)^{-1}$.
  - **8.4** The Goulden–Jackson Cluster Method & The 3-Regime String Avoidance Hierarchy.
- **Diagnostic Signal & Scratchpad**: "Exact $k$ occurrences of a local violation", "no two adjacent items are equal/compatible", or "strings avoiding forbidden substring(s) $P_1, \dots, P_m$". $\mid$ *Scratchpad*: 1. Never try to track "which positions are NOT violated" directly: assign formal weight $y-1$ to each violation (or merge violated adjacent pairs into connected clusters), compute $g_j$ ("$j$ forced edges/overlaps"), and invert!
- **Flagship Worked Example (`CF 840C` — On the Bench)**: *Problem*: Given $a_1, \dots, a_N$ ($N \le 300$, or $N \le 2.5 \times 10^5$ in `ABC 260 Ex`), count permutations where no two adjacent elements have $a_{p_i} a_{p_{i+1}}$ equal to a perfect square. *Derivation*: Square-free cores partition the array into color classes of sizes $c_1, \dots, c_m$. In any valid arrangement, elements of color $i$ have no adjacent equal neighbors.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 08`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#018` | **ABC 172 E — NEQ** | `2B#A2` | Binomial Inversion & Rook-Style EGF |
| **SS-2** | `#241` | **yukicoder 1810 — Substring Avoidance** | `2B#D1` | Single-Pattern Guibas–Odlyzko Denominator |
| **Int-1** | `#155` | **Luogu P4491 — [HAOI2018] 染色** | `2B#A7` | Exact-$k$ Color Frequency Binomial Inversion Convolution |
| **Int-2** | `#089` | **CF 840C — On the Bench** | `2B#B4` | Adjacent-Block Inclusion-Exclusion via Falling-Factorial EGF |
| **Adv-1** | `#067` | **AGC 005 D — ~K Perm Counting** | `2B#B2` | Disjoint Rook Paths + Inclusion-Exclusion Convolution |
| **Adv-2** | `#139` | **CF Gym 102978H — Harsh Comments / Motzkin** | `2A#16` | Motzkin Trinomial Radical + Multi-Pattern Goulden–Jackson |
| **Mas-1** | `#052` | **ARC 100 F / LOJ 3395 — Colorful Sequences** | `2B#B8` | Forbidden Rainbow Window Automaton / IE OGF |
| **Mas-2** | `#137` | **CF Gym 102331J — Forbidden Strings** | `2B#D3` | Multi-Pattern Aho–Corasick Goulden–Jackson Cluster Matrix $(I + C(x))^{-1}$ |

> **Ch 08 Quarantined Library Verification Footnote (§5)**: `R-56`, `R-57`.


### Part III: Online Convolutions, Implicit Equations, Formal Residues & Graph Enumeration (Chapters 09–13)

#### Chapter 09: Causal Dynamic Programming: Semi-Online CDQ Divide-and-Conquer FFT & Online Relaxed Convolution (`ch09_cdq_fft_online_relaxed_convolution.qmd`)
- **Ring / Operator**: Contractive Causal Operators on $K[[x]]$ ($\operatorname{val}(\Phi(F)-\Phi(G)) > \operatorname{val}(F-G)$), Dyadic Lowbit Block Decomposition $\mid$ **Prereqs**: Ch 01–04, Ch 08 (Convolutions, Calculus, $\ln/\exp$, Connected-Component IE) $\mid$ **Waves**: `4B (§1), 5A (§2), 5B (§3)`
- **Sub-sections & Core Derivations**:
  - **9.1** Causal Contractive Operators on $K[[x]]$: When a sequence $f_n$ depends on $f_0, \dots, f_{n-1}$ through a non-linear wrapper $f_n = \psi_n\left(\sum_{i=1}^{n-1} f_i g_{n-i}\right)$, why standard offline inversion fails (or requires complicated ODEs) whereas causal divide-and-conquer succeeds in $O(N \log^2 N)$.
  - **9.2** Semi-Online CDQ Divide-and-Conquer FFT ($O(N \log^2 N)$); Recursive procedure `solve(L, R)`: first recurse `solve(L, M)`, then convolve known $f[L.M]$ with $g[1.R-L]$ to accumulate contributions into $f[M+1.R]$, then recurse `solve(M+1, R)`.
  - **9.3** Fully Online 0-Indexed Relaxed Convolution (van der Hoeven / Nyaan, $O(N \log^2 N)$).
  - **9.4** 10-Line Online Replacements for `inv`, `ln`, `exp`, and Pólya Euler Transforms: How $F'(x) = A'(x) F(x) \iff n f_n = \sum_{i=1}^n (i a_i) f_{n-i}$ becomes a 5-line loop calling `relaxed.next(i * a[i], f[i-1]) / i`, including online Euler transforms where $A(x^k)$ updates harmonic multiples on the fly (`ABC 230 Ex`).
- **Diagnostic Signal & Scratchpad**: DP transitions $dp[u][t] = \min/\max/+ \sum_{s < t} dp[v][s] \cdot w_{e}(t-s)$ on graphs (`CF 553E`, `ABC 213 Ex`), or self-referential recurrences $f_n = \psi_n(\sum_{i+j=n} \alpha_i f_i \beta_j f_j)$ (`yukicoder 3029`, `AGC 060 D`). $\mid$ *Scratchpad*: 1. If one factor $g$ is fully known in advance ($f = f * g + h$), use standard CDQ D&C FFT (`solve(L, R)`). 2.
- **Flagship Worked Example (`ABC 230 Ex` — Bullion)**: *Problem*: Given valid bag weights, a bag of weight $w$ can hold any multiset of smaller bags (with at least 2 items) whose weights sum to $w - 1$. *Derivation*: $F(x) = x \left(\prod_{w \ge 1} (1 - x^w)^{-f_w} - F(x)\right)$. Taking derivatives gives $x F'(x) = F(x) + F(x) \sum_{m \ge 1} x^m \sum_{d \mid m} d f_d$ (after adjusting for singletons).

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 09`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#060` | **ARC 138 E — Decreasing Subsequence** | `5A#22` | RSK / Greene Theorem Semi-Online Block CDQ Convolution |
| **SS-2** | `#021` | **ABC 222 H — Beautiful Binary Tree** | `3B#1` | Explicit Causal Binary-Tree Recurrence $f_n = \sum c_{i,j} f_i f_j$ via CDQ / Relaxed Convolution (revisited via LIF in Ch 11 & ODE in Ch 18) |
| **Int-1** | `#086` | **CF 553E — Kyoya and Train** | `1B#13` | Time-Window Shortest Path DP via CDQ Divide-and-Conquer FFT |
| **Int-2** | `#023` | **ABC 230 Ex — Bullion** | `1A#27` | Unlabeled Knapsack / Weighings via Online Relaxed Convolution |
| **Adv-1** | `#056` | **ARC 123 F — Arithmetic Progression** | `4B#32` | Non-Homogeneous Causal Recurrence via CDQ / Relaxed Convolution |
| **Adv-2** | `#225` | **LOJ 6503 — Magic (魔术)** | `2B#B6` | Adjacent-Color Run Avoidance + Divide-and-Conquer NTT |
| **Mas-1** | `#206` | **UOJ 50 — [UR #3] 链式反应** | `2A#46` | Non-Autonomous Differential Equation $F' = \frac{1}{2}A(x)F^2 + 1$ via CDQ FFT |
| **Mas-2** | `#075` | **AGC 060 D — Same Generating Function** | `1B#25` | Coupled Eulerian Permutation Ascent CDQ Divide-and-Conquer FFT |

> **Ch 09 Quarantined Library Verification Footnote (§5)**: `R-45`.

#### Chapter 10: General Implicit Functional Equations, Coupled/Multivariate Newton Iteration, Unlabeled Trees & Otter's Dissimilarity Theorem (`ch10_implicit_equations_newton_unlabeled_trees_otter.qmd`)
- **Ring / Operator**: Implicit Operator $\Phi: (xK[[x]])^r \to (xK[[x]])^r$, Fréchet / Jacobian Derivative $J_\Phi(F) \in \operatorname{Mat}_r(K[[x]]/(x^d))$, Otter Dissymmetry Ring $\mid$ **Prereqs**: Ch 02–04, Ch 09 (1D Newton, Pólya Cycle Index, EGFs, Online Relaxed Convolution) $\mid$ **Waves**: `1A (§6), 3A (§6), 3B (§2–§3), 4B (§2)`
- **Sub-sections & Core Derivations**:
  - **10.1** Contractive Implicit Functional Equations $\Phi(x, F(x)) = 0$ in $(xK[[x]], d_{\operatorname{val}})$.
  - **10.2** General 1D & Coupled $r \times r$ Jacobian Newton Iteration ($O(N \log N)$).
  - **10.3** Unlabeled Rooted Trees, Pólya Substitution $R(x^k)$ & The Key Trick for Newton Iteration.
  - **10.4** Otter's Dissimilarity Theorem for Unrooted Unlabeled Trees & Chemical Isomers (Alkanes/Alkenes).
- **Diagnostic Signal & Scratchpad**: Recursive tree/graph/string grammars $F(x) = \Psi(x, F(x), F(x^2), F(x^3))$ up to $N \le 2.5 \times 10^5$, or counting unrooted unlabeled trees / chemical isomers. $\mid$ *Scratchpad*: 1. Root the structure first to obtain a fixed-point equation $R(x) = x \Phi(R(x), R(x^2), \dots)$. 2.
- **Flagship Worked Example (`Luogu P5900` — 无标号无根树计数)**: *Problem*: Count unrooted unlabeled trees on $N \le 2 \times 10^5$ vertices $\pmod{998244353}$. *Derivation*: First solve $R(x) = x \exp\left(R(x) + \sum_{k \ge 2} \frac{R(x^k)}{k}\right) \pmod{x^{N+1}}$. In the Newton step $d \to 2d$, let $S_{\ge 2}(x) = \sum_{k=2}^{2d-1} \frac{R_d(x^k)}{k} \bmod x^{2d}$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 10`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#186` | **Luogu P5900 — 无标号无根树计数** | `1A#29` | Otter's Dissymmetry Theorem $U(x) = R(x) - \frac{1}{2}(R(x)^2 - R(x^2))$ |
| **SS-2** | `#226` | **LOJ 6538 — 烷基计数 加强版 加强版** | `1A#14` | Pólya $S_3$ Ternary Tree via Newton or 12-Line Chained Relaxed Convolution |
| **Int-1** | `#244` | **yukicoder 3029 — Colored Tree (FPS 24)** | `3B#5` | $2 \times 2$ Jacobian Newton / Substitution Elimination |
| **Int-2** | `#013` | **`fps_24_s` — Game** | `1A#30` | Tree Normal-Play Game $L = x\exp(x e^x - L)$ via Newton / Lambert $W$ |
| **Adv-1** | `#179` | **Luogu P5597 — 【XR-4】复读** | `3B#18` | Unlabeled $k$-ary Tree Automaton Minimization + Coupled Implicit Newton Iteration |
| **Adv-2** | `#126` | **CF 1687F — Koishi's Unconscious Permutation** | `3B#20` | Implicit Bivariate / Cycle-Rise Permutation Equations |
| **Mas-1** | `#191` | **Luogu P6598 — 烷烃计数 (Alkanes)** | `1A#14` | Pólya $S_3, S_4$ Cycle Index + Otter Dissimilarity |
| **Mas-2** | `#192` | **Luogu P6597 — 烯烃计数 (Alkenes)** | `1A#14` | Double-Bond Unrooted Carbon Trees via Cycle Index |

> **Ch 10 Quarantined Library Verification Footnote (§5)**: `R-36`.

#### Chapter 11: The Laurent Field $K((x))$, Formal Residue Calculus ($\operatorname{Res}_{x=0}$, Change-of-Variables / `EI 留数法`), Raney's Lemma, the 6 Forms of Lagrange Inversion (LIF) & Characteristic-$p$ LIF (`ch11_laurent_residues_raney_lagrange_inversion.qmd`)
- **Ring / Operator**: Formal Laurent Field $K((x)) = K[[x]][x^{-1}]$, Formal Residue Functional $\operatorname{Res}_{x=0}: K((x))dx \to K$, Compositional Group $(xK[[x]]_{\operatorname{val}=1}, \circ)$ $\mid$ **Prereqs**: Ch 01–02, Ch 04, Ch 10 ($K[[x]]$, Formal Calculus, Frobenius, Implicit Equations) $\mid$ **Waves**: `3A (§1–§4), 3B (§1–§2), 4B (§3)`
- **Sub-sections & Core Derivations**:
  - **11.1** The Field of Formal Laurent Series $K((x)) = K[[x]][x^{-1}]$ & The Formal Residue Functional.
  - **11.2** Algebraic Proof of all 6 Forms of Lagrange–Bürmann Inversion (LIF); **Proof via Formal Residues**: For $u = x / \phi(u)$ (or $F(G(x)) = x$), $[x^n] H(G(x)) = \operatorname{Res}_{x=0} H(G(x)) x^{-n-1} dx = \operatorname{Res}_{u=0} H(u) F(u)^{-n-1} F'(u) du$.
  - **11.3** Raney's Cycle Lemma: Combinatorial counterpart of Form 1—among the $m$ cyclic shifts of an integer sequence $(s_1, \dots, s_m)$ summing to $+1$, **exactly $1$** shift has all proper prefix sums strictly positive (`AtCoder fps_24_o`, `Luogu P6672`).
  - **11.4** Characteristic-$p$ Lagrange Inversion ($n \ge p$): Why $\frac{1}{n} [u^{n-k}] \phi(u)^n$ fails when $p \mid n$, why Form 3 ($[u^n] H(u)(1 - u \phi'(u)/\phi(u))\phi(u)^n$) has **no $1/n$ division**, and how Frobenius splitting $\phi(u)^n = \phi(u^{p^k})^q \phi(u)^r$ extracts $[x^n] G(x) \bmod p$ for $n \le 10^{18}$ and small prime $p \le 10^5$ (`Luogu P7592`, `Luogu P8555`).
- **Diagnostic Signal & Scratchpad**: Need a **single coefficient** $[x^N] H(F(x))$ where $F(x) = x \phi(F(x))$ (or an algebraic/Catalan equation that can be rewritten via $u = x \phi(u)$), or a binomial sum $\sum_k \binom{n + \alpha k}{k} c_k$ with $k$ coupled inside the upper index. $\mid$ *Scratchpad*: 1. When $N$ is fixed and you only need $[x^N] H(F(x))$, **do not run Newton Iteration**: apply LIF to reduce $[x^N] H(F(x))$ to $\frac{1}{N}[u^{N-1}] H'(u) \phi(u)^N$ (one polynomial power)! 2.
- **Flagship Worked Example (`Luogu P7438` — [AGM 2021] 恐龙 / Implicit Tree LIF)**: *Problem*: Given an implicit tree equation $F(x) = x \phi(F(x))$, extract $[x^N] F(x)^k \pmod{998244353}$ for $N \le 2 \times 10^5$. *Derivation*: Instead of $O(N \log N)$ Newton iteration to find all coefficients of $F(x)$ followed by $F(x)^k$, apply LIF Form 1 directly: $[x^N] F(x)^k = \frac{k}{N} [u^{N-k}] \phi(u)^N$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 11`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#003` | **`fps_24_f` — Colored Paper / Colored Tree** | `1A#2` | Implicit Tree Equation $F = x \cosh F$ Solved via $[x^n]F = \frac{1}{n}[u^{n-1}]\cosh^n u$ |
| **SS-2** | `#200` | **Luogu P7438 — [AGM 2021] 恐龙** | `3B#28` | Composite Power Extraction $[x^N] F(x)^k = \frac{k}{N}[u^{N-k}]\phi(u)^N$ |
| **Int-1** | `#196` | **Luogu P6672 — [清华集训2016] 你的生命已如风中残烛** | `4B#5` | 1D Raney's Lemma Cyclic Shift $\frac{1}{m+1}$ on Degree Sequences |
| **Int-2** | `#201` | **Luogu P7439 — [KrOI2021] 蕾切尔** | `3B#29` | Formal Residue Change of Variables $\operatorname{Res}_x G(x) = \operatorname{Res}_u G(F(u))F'(u)$ |
| **Adv-1** | `#010` | **`fps_24_p` — Ball** | `1A#29` | Bivariate Root Shift + Formal Residue / Lagrange Inversion |
| **Adv-2** | `#229` | **LOJ 6703 — 小 Q 的序列** | `3B#27` | Derivative-Free Form 4 LIF $[x^n] H(F(x)) = [u^n] H(u)(1 - u\phi'/\phi)\phi(u)^n$ |
| **Mas-1** | `#114` | **CF 1349F2 — Slime and Sequences (Hard Version)** | `1A#30` | Eulerian Bivariate EGF $\to$ Lambert-$W$ Substitution + Lagrange Inversion |
| **Mas-2** | `#203` | **Luogu P7592 — 2021 CoE-II E (数树)** | `3B#11` | 4-Subtask Synthesis (2D Rational, Bivariate LIF, Lucas Char-$p$ LIF) |

> **Ch 11 Quarantined Library Verification Footnote (§5)**: `R-61`, `R-62`.

#### Chapter 12: Cacti, Desert Graphs, Block-Cut Trees & 2-Vertex / 2-Edge-Connected Graph Enumeration (Combining Newton Iteration & Compositional Inverse / LIF) (`ch12_cacti_deserts_block_cut_biconnected_graphs.qmd`)
- **Ring / Operator**: Pointed Operator $\vartheta = xD$, Block-Cut Substitution $Z(x) = x e^{B'(Z(x))}$, Bridge-Block Substitution $W(x) = x e^{B'(W(x))}$ $\mid$ **Prereqs**: Ch 04, Ch 10, Ch 11 (EGFs, Pointing $\vartheta$, Coupled Newton, Lagrange Inversion) $\mid$ **Waves**: `3A (§7), 3B (§3), 4B (§3), 5B (§3)`
- **Sub-sections & Core Derivations**:
  - **12.1** Pointing Operator $\vartheta = xD$ & Rooted-to-Unrooted Labelled Transitions.
  - **12.2** Labeled Cactus Graphs & Desert Graphs (Edge-Disjoint Cycle Forests); In a rooted labeled cactus $T(x)$, the root $r$ is incident to an unordered set (`exp`) of attachments, each of which is either a single bridge edge to another rooted cactus ($T(x)$) or a simple cycle of length $k \ge 3$ of rooted cacti ($\frac{1}{2} \sum_{k \ge 2} T(x)^k = \frac{T(x)^2}{2(1-T(x))}$).
  - **12.3** Block-Cut Trees & 2-Vertex-Connected (Biconnected) Labeled Graphs (`Luogu P5827`, `AtCoder fps_24_w`).
  - **12.4** Bridge-Block Trees & 2-Edge-Connected Labeled Graphs (`Luogu P5828`, `Luogu P6596`).
- **Diagnostic Signal & Scratchpad**: Counting graphs where every cycle is edge-disjoint (cacti/deserts), counting graphs with $k$ bridges, or counting 2-vertex / 2-edge-connected graphs on $N$ labeled vertices. $\mid$ *Scratchpad*: 1. Always start from the **rooted connected EGF** $R(x) = x C'(x)$! 2. Express $R(x)$ in terms of the derivative $B'(\cdot)$ of the 2-connected block EGF via block-cut or bridge-block substitution, then invert the substitution using Lagrange Inversion!
- **Flagship Worked Example (`Luogu P5827` — 点双连通图计数)**: *Problem*: Compute the number of labeled 2-vertex-connected (biconnected) graphs on $N$ vertices $\pmod{998244353}$ for $N \le 10^5$. *Derivation*: First compute $G(x) = \sum_{k \ge 0} 2^{\binom{k}{2}} \frac{x^k}{k!}$, $C(x) = \ln G(x)$, and $R(x) = x C'(x)$. Since $\ln(R(x)/x) = B'(R(x))$, let $H(x) = \ln(R(x)/x)$ and extract single-$N$ via Ch 11.2 Lagrange Inversion $[x^{N-1}]B'(x) = \frac{1}{N-1}[x^{N-1}] H'(x)\left(\frac{x}{R(x)}\right)^{N-1}$ in $O(N \log N)$ (simultaneous all-$n$ `revert` deferred to Ch 21.4).

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 12`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#176` | **Luogu P5434 — 有标号荒漠计数** | `3A#9` | Labeled Desert EGF $\exp(C_{\text{cactus}}(x))$ via Cactus $\exp$ |
| **SS-2** | `#245` | **51Nod 1728 — 不动点** | `3A#19` | Endofunction Cycles of Height-$\le k$ Rooted Trees $F_j(x) = x \exp(F_{j-1}(x))$ |
| **Int-1** | `#146` | **Luogu P3684 / BZOJ 3684 — 大朋友和多叉树** | `3B#25` | Degree-Constrained Multi-Way Rooted Tree Species + Lagrange Inversion |
| **Int-2** | `#227` | **LOJ 6569 — 仙人掌计数 (Cactus Counting)** | `3A#7` | Labeled Cactus Pointed Equation $C^\bullet = x \exp\left(C^\bullet + \frac{(C^\bullet)^2}{2(1 - C^\bullet)}\right)$ |
| **Adv-1** | `#190` | **Luogu P6596 — How Many of Them** | `3A#14` | Labeled Connected Graphs with $\le k$ Bridges via Tree-of-2-ECCs EGF |
| **Adv-2** | `#016` | **`fps_24_w` — Biconnected Graphs** | `3A#11` | Pointed Block-Cut Tree $\ln(R(x)/x) = B'(R(x))$ + Single-$n$ $O(n \log n)$ Lagrange Inversion Extraction (all-$n$ `revert` deferred to Ch 21.4) |
| **Mas-1** | `#183` | **Luogu P5827 — 点双连通图计数** | `3A#10` | Single-Degree $N$ Vertex-Biconnected Graphs via Pointed Block-Cut Equation & $O(N \log N)$ Lagrange Inversion (all-$n$ `revert` in Ch 21.4) |
| **Mas-2** | `#184` | **Luogu P5828 — 边双连通图计数** | `3A#13` | Single-Degree $N$ Edge-Biconnected Graphs via $C'(x) = B'(C(x)e^{C'(x)})$ & $O(N \log N)$ Lagrange Inversion (all-$n$ `revert` in Ch 21.4) |

> **Ch 12 Quarantined Library Verification Footnote (§5)**: Uses prerequisite chapter primitives (`0` new bare templates).

#### Chapter 13: Graphical Generating Functions ($2^{\binom{n}{2}}$ CZT Convolution), Eulerian & Bipartite Graphs, Robinson's DAGs, Strongly Connected Digraphs & Matrix-Tree over FPS (`ch13_graphical_gf_eulerian_bipartite_dags_sccs.qmd`)
- **Ring / Operator**: Graphical EGF Ring (twisted by $2^{-\binom{n}{2}}$ via CZT), Determinants $\det L(x) \in K[[x]]/(x^d)$ $\mid$ **Prereqs**: Ch 04, Ch 07, Ch 09, Ch 12 (EGFs, Bluestein CZT, CDQ/Newton, Block-Cut Decompositions) $\mid$ **Waves**: `3A (§8), 3B (§4), 4A (§3), 4B (§3)`
- **Sub-sections & Core Derivations**:
  - **13.1**: Graphical Generating Functions, Edge-Indicator Reweighting $2^{\binom{n}{2}} \to (1+w)^{\binom{n}{2}}$, and Connected Simple & Eulerian Graphs via $\ln G(x)$ and $2^{-\binom{n}{2}}$ Chirp-$z$ Convolution
  - **13.2**: Bipartite Graphs, 2-Colored Hurwitz EGFs $\sum 2^{ab} \frac{x^a}{a!} \frac{y^b}{b!}$, and Chirp-$z$ / Bluestein Reduction ($2ab = (a+b)^2 - a^2 - b^2$)
  - **13.3**: Acyclic Digraphs (DAGs), Out-Degree Layering DP, Robinson–Stanley Zero-Indegree Inclusion–Exclusion ($\sum_{n \ge 0} (-1)^n 2^{-\binom{n}{2}} \frac{x^n}{n!}$), and Strongly Connected Digraphs (SCCs)
  - **13.4**: Kirchhoff's Matrix-Tree Theorem, The BEST Theorem for Directed Eulerian Circuits, Rank-1 Determinant Perturbations, and Symbolic Matrix-Tree $\det L(x) \bmod x^{k+1}$ over Commutative Rings
- **Diagnostic Signal & Scratchpad**: Counting labeled graphs ($n \le 10^5$ or $n \le 500$) with connectivity, bipartiteness, acyclicity (DAG), strong connectivity (SCC), or spanning-tree weight constraints. $\mid$ *Scratchpad*: Write the quadratic edge factor $2^{\binom{n}{2}}$ as $\exp(\frac{1}{2} n^2 \ln 2 - \frac{1}{2} n \ln 2)$ or apply Bluestein's identity $\binom{n+m}{2} = \binom{n}{2} + \binom{m}{2} + nm$ to reduce 2D graph convolutions to 1D NTT.
- **Flagship Worked Example (`Luogu P7364` / `CF 1951I` / Connected Simple, Eulerian, and DAG Enumeration via Chirp-$z$ + $\ln/\exp$)**: *Problem*: Count connected simple graphs, connected Eulerian graphs, and DAGs on $N \le 10^5$ labeled vertices. *Derivation*: Express $G(x) = \sum_{n \ge 0} 2^{\binom{n}{2}} \frac{x^n}{n!}$ and $D(x) = \left(\sum_{n \ge 0} (-1)^n 2^{-\binom{n}{2}} \frac{x^n}{n!}\right)^{-1}$ via Chirp-$z$ transform and truncated $\ln / \text{inv}$ in $O(N \log N)$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 13`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#164` | **Luogu P5219 — 无聊的水题 I** | `3A#3` | Bounded-Degree Labeled Spanning Trees via Prüfer EGF $\prod_{i=1}^n \left(\sum_{j=0}^{D-2} \frac{x^j}{j!}\right)$ |
| **SS-2** | `#103` | **CF 1109D — Sasha and Interesting Fact** | `4B#8` | Generalized Cayley Forest Formula $k n^{n-k-1}$ |
| **Int-1** | `#093` | **CF 917D — Stranger Trees** | `3A#36` | Weighted Matrix-Tree Determinant Interpolation / Prüfer |
| **Int-2** | `#189` | **Luogu P6295 — 有标号 DAG 计数** | `3A#34` | Robinson–Stanley EGF $\sum (-1)^{k-1} \frac{x^k}{k! 2^{\binom{k}{2}}}$ Inversion + $\ln$ |
| **Adv-1** | `#199` | **Luogu P7364 — 有标号二分图计数** | `3A#33` | 2-Colored Graph EGF $B_2(x) \implies \text{Connected } \frac{1}{2}\ln B_2(x) \implies \text{Total } \sqrt{B_2(x)}$ |
| **Adv-2** | `#053` | **ARC 105 F / LOJ 6539 — Lights Out on Connected Graph** | `1A#20` | Connected Bipartite Graph $\ln$ of Sqrt-Scaled Sum |
| **Mas-1** | `#122` | **CF 1556F — Sports Betting (Strongly Connected Variant)** | `3A#37` | Strongly Connected Digraphs via Semiring/FPS Inversion |
| **Mas-2** | `#212` | **UOJ 498 — 新年的追逐** | `3A#39` | Game on Random Graphs via Connected Component EGF |

> **Ch 13 Quarantined Library Verification Footnote (§5)**: `R-38`, `R-59`.


### Part IV: Stochastic Processes, Lattice Walks, Multivariate Diagonals & Kernel Method (Chapters 14–17)

#### Chapter 14: Probability Generating Functions (PGFs), Taylor Expansion at $x=1+t \bmod t^3$, Stopping Times, Renewal Equations, Poissonization & Martingales (`ch14_pgf_stopping_times_renewal_poisson_martingales.qmd`)
- **Ring / Operator**: Jet Ring $K[t]/(t^3)$ via $x = 1+t$, Renewal Equation $F(x) = U(x)/R(x)$, Optional Stopping Martingale Space $\mid$ **Prereqs**: Ch 04–06, Ch 08 (EGFs, Rational GFs, Falling Factorials, Guibas–Odlyzko String Overlap) $\mid$ **Waves**: `2B (§E), 2C (§A–§C)`
- **Sub-sections & Core Derivations**:
  - **14.1**: Probability Generating Functions $P(x) = \sum_{n \ge 0} \Pr[X=n] x^n$ and the Factorial Moment Calculus ($\mathbb{E}[X] = P'(1)$, $\text{Var}(X) = P''(1) + P'(1) - P'(1)^2$)
  - **14.2**: First-Passage / Stopping-Time Renewal Equation $F(x) = \frac{G(x)}{1 - H(x)}$ and Tail-Probability GF $Q(x) = \frac{1 - P(x)}{1 - x}$ ($\mathbb{E}[T] = Q(1)$)
  - **14.3**: String Pattern Matching, Prefix-Suffix Autocorrelation Polynomials $C_{A,B}(x)$, Conway's Game of Penney, and Optional Stopping / Martingale Bridges
  - **14.4**: Exponential Poissonization (Coupon Collector / Balls-in-Bins EGF $\prod_i (e^{p_i x} - 1)$) and Potential Function $\sum_i \phi(a_i)$ Linearization
- **Diagnostic Signal & Scratchpad**: Expected hitting times, stopping times for string/coin patterns, random walks on hypercubes/urns, or coupon-collector variants where DP states have cycles. $\mid$ *Scratchpad*: Form either the first-passage OGF $F(x)$ and differentiate at $x=1$ (using L'Hôpital's rule when denominator vanishes at $x=1$), or Poissonize discrete steps into continuous time $t$ via EGFs $\sum c_k e^{\lambda_k t}$ and integrate $\int_0^\infty (1 - E(t)) e^{-t} dt$.
- **Flagship Worked Example (`Luogu P4548` — [CTSC2006] 歌唱王国 & Non-Uniform Coupon Collector)**: *Problem*: Compute the expected waiting time until a target string $S$ appears in i.i.d. random characters, and generalize to $m$-urn occupancy. *Derivation*: Construct the coupled OGF system $(1 - x) Q(x) + x^{|S|} P(x) = 1$, use KMP border autocorrelation $C_{S,S}(x)$ to relate $Q(x)$ and $P(x)$, and evaluate at $x=1$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 14`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#115` | **CF 1392H — ZS Shuffles Cards** | `2B#E1` | Memoryless Geometric Stopping PGF + Harmonic Expectation |
| **SS-2** | `#026` | **ABC 242 Ex — Random Painting** | `2B#E8` | Continuous-Time Min-Max Stopping PGF $F'(1)$ |
| **Int-1** | `#156` | **Luogu P4548 — [CTSC2006] 歌唱王国** | `1A#15` | KMP Border Polynomial / Guibas–Odlyzko $F'(1) = \sum_{\text{border } L} m^L$ |
| **Int-2** | `#071` | **AGC 038 E — Gachapon** | `2B#E6` | Multivariate Min-Max Stopping Time EGF $F'(1)$ |
| **Adv-1** | `#148` | **Luogu P3706 — [SDOI2017] 硬币游戏** | `2B#E3` | Multi-Player Guibas–Odlyzko Correlation Linear System |
| **Adv-2** | `#209` | **UOJ 390 — [UNR #3] 百鸽笼** | `2B#E7` | Bounded-Capacity Stopping Time EGF $\prod \sum_{j < a_i} \frac{x^j}{j!}$ |
| **Mas-1** | `#039` | **ABC 289 Ex — Trio** | `2B#E12` | 3-Walker Return-to-Origin Absorbing PGF $(P^3) \oslash Q$ |
| **Mas-2** | `#113` | **CF 1349D — Slime and Biscuits** | `2A#12` | Martingale Stopping Potential + First-Difference Order Reduction |

> **Ch 14 Quarantined Library Verification Footnote (§5)**: `R-53`, `R-54`, `R-55`, `R-58`.

#### Chapter 15: 1D Bounded Lattice Walks, Radical Substitutions, Chebyshev Strip Continuants & the 1D Kernel Method (with Laurent Kernel Cancellation) (`ch15_1d_lattice_walks_chebyshev_kernel_method.qmd`)
- **Ring / Operator**: Bivariate Walk Ring $K[u, u^{-1}][[t]]$, Radical Extension $K[[x]][\sqrt{\Delta(x)}]$, Chebyshev Continuant Polynomials $U_m(x)$ $\mid$ **Prereqs**: Ch 05, Ch 11, Ch 14 (Rational GFs, Laurent Field $K((x))$ & Residue Change-of-Variables, PGFs) $\mid$ **Waves**: `2A (§4), 3A (§2), 3C (§1), 4B (§2)`
- **Sub-sections & Core Derivations**:
  - **15.1**: Unbounded and Single-Boundary 1D Lattice Walks (Ballot Numbers, Dyck Paths, Motzkin Paths, and the Quadratic Radical $C(x) = \frac{1 - \sqrt{1 - 4x}}{2x}$)
  - **15.2**: Bounded-Height Dyck Paths in $[0, H]$ via Linear Transfer Matrices and Chebyshev Continuant Polynomials $U_H(\frac{1}{2x})$
  - **15.3**: The 1D Kernel Method for General Bounded-Below Walks with Negative Steps $-k$: Characteristic Equation $1 - x S(u) = 0$ and Small-Root Substitution $u = u_1(x), \dots, u_k(x)$
  - **15.4**: Reflection Principle vs. Algebraic Kernel Cancellation, Absorbing Barriers, and Cyclic Random Walks mod $K$
- **Diagnostic Signal & Scratchpad**: 1D walks or prefix-sum processes constrained to stay $\ge 0$ or within $[0, H]$, where step sizes include $-1, 0, +1$ or general bounded negative steps. $\mid$ *Scratchpad*: Introduce the height variable $u$, write $(1 - x S(u)) W(x,u) = W_0(x) - x \sum_{j=0}^{k-1} R_j(x,u)$, and plug in the $k$ power-series roots $u_i(x)$ of the kernel $1 - x S(u) = 0$ that vanish at $x=0$ to eliminate $W(x,u)$ and solve for the boundary series $R_j(x)$.
- **Flagship Worked Example (`Gym 104053J` / Bounded-Height Dyck Paths via Chebyshev Continuants & 1D Kernel Method)**: *Problem*: Count 1D walks of length $N$ staying in $[0, H]$ or $[0, \infty)$ with step set $\{-1, 0, +1\}$. *Derivation*: Solve the tridiagonal transfer recurrence in $K(x)$ to obtain $W_{\le H}(x) = \frac{U_H(1/2x)}{x U_{H+1}(1/2x)}$ in $O(H \log H + \log N)$, and verify the $H \to \infty$ limit via the small root $u_1(x)$ of $1 - x(u^{-1} + 1 + u) = 0$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 15`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#105` | **CF 1204E — Natasha, Sasha and the Prefix Sums** | `3A#1` | Reflection Principle on Exceedance Thresholds |
| **SS-2** | `#070` | **AGC 021 E — Ball Eat Chameleons** | `2A#18` | Reflection Principle / Raney's Lemma Weak Ballot Bound |
| **Int-1** | `#220` | **Luogu P3266 — [JLOI2015] 骗我呢** | `4B#3` | Two-Wall Alternating Reflection Principle Strip Walk |
| **Int-2** | `#140` | **CF Gym 103415K / yukicoder 1341 — Gambler's Walk** | `4B#14` | Asymmetric $+1, -2$ Walk via Small-Root Kernel Factoring |
| **Adv-1** | `#128` | **CF 1810G — The Maximum Prefix** | `3A#9` | Backward DP / Kernel Method on Prefix Maxima |
| **Adv-2** | `#134` | **CF 1967E2 — Again Counting Arrays (Hard)** | `3A#4` | Bounded-Wall Reflection Principle ($\pm 1$ Walk between $0$ and $M$) |
| **Mas-1** | `#076` | **AGC 070 C — No Clar** | `3A#20` | Bivariate Ballot / Catalan Path Pair Extraction |
| **Mas-2** | `#210` | **UOJ 424 — count (Cartesian / Left-Depth Trees)** | `2A#20` | Chebyshev Rational Function $Q_m(x)/Q_{m+1}(x)$ + Reflection |

> **Ch 15 Quarantined Library Verification Footnote (§5)**: `R-63`.

#### Chapter 16: The 5-Ring Bivariate Hierarchy, 2D Bostan–Mori, Twisted Kronecker Substitution & Furstenberg's Algebraic Diagonal Reduction in $K[[t]]((y))$ (`ch16_bivariate_hierarchy_2d_bostan_mori_furstenberg.qmd`)
- **Ring / Operator**: 5-Ring Hierarchy: $K[x,y] \subset K[x][[y]] \subset K[[x,y]] \subset K((x))[[y]] \subset K[[t]]((y))$, Diagonal Operator $\operatorname{Diag}: K[[x,y]] \to K[[t]]$, Twisted Kronecker Quotient $K[z]/(z^{ND})$ $\mid$ **Prereqs**: Ch 05, Ch 11, Ch 15 (1D Bostan–Mori, Formal Residues in $K((y))$, Algebraic Radicals) $\mid$ **Waves**: `3C (§2), 4A (§4), 4B (§4)`
- **Sub-sections & Core Derivations**:
  - **16.1**: The 5-Ring Bivariate Hierarchy ($K[x,y] \subset K[y][[x]] \subset K[[x,y]] \subset K((x))[[y]] \subset K((x))((y))$) & Where Each Series Lives ($\frac{1}{x-y}$ Iterated Laurent Asymmetry)
  - **16.2**: The 4 Regimes of Bivariate Bostan–Mori $[x^N]\frac{P(x,y)}{Q(x,y)}$ (`TECHNIQUE_TAXONOMY.md` §3.5.A)
  - **16.3**: Twisted Kronecker Substitution for $d$-Dimensional FPS ($\text{mul}, \text{inv}, \ln, \exp$) in $K[x_1,\dots,x_d]/(x_1^{n_1},\dots,x_d^{n_d})$
  - **16.4**: Furstenberg's Diagonal Theorem ($\operatorname{Diag}(R) \leftrightarrow$ Algebraic via $[u^0]F(t/u, u)$), Radial Total-Degree Derivation $\mathfrak{D} = \sum x_i \partial_{x_i}$ for 3D D-Finite Diagonals, & Failure Mode #15
- **Diagnostic Signal & Scratchpad**: 2D recurrences with constant coefficients, $[x^n y^m] P(x,y)/Q(x,y)$ where $n$ is huge ($10^{18}$) and $m$ is moderate ($\le 10^4$), or extracting $[x^n y^n] R(x,y)$. $\mid$ *Scratchpad*: For asymmetric $(n, m)$, treat $K[y]/(y^{m+1})$ as the coefficient ring and run Bostan-Mori in $x$ using 2D NTT/Kronecker multiplication. For $[x^n y^n] R(x,y)$, substitute $x = t/u, y = u$, expand in the iterated Laurent ring $K((t))((u))$, and sum the residues of the small poles $u = u_i(t) \in t K[[t]]$.
- **Flagship Worked Example (`AGC 058 D` / `UOJ 596` — Rational Diagonal Extraction & Twisted $\chi$-Graded Bivariate Bostan–Mori)**: *Problem*: Extract $[x^n y^n] \frac{1}{1 - x - y - xy}$ and $[x^n y^m] \frac{P(x,y)}{Q(x,y)}$. *Derivation*: Substitute $x = t/u, y = u$ to write $\text{Diag}(F)(t) = [u^0] \frac{-u}{u^2 - (1-t)u + t}$, factor the denominator in $K((t))[u]$, and take the residue at the unique small root $u_1(t) = \frac{1 - t - \sqrt{1 - 6t + t^2}}{2}$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 16`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#048` | **ARC 012 D — Don't Step on the Mines!** | `1B#11` | 2D Walk Factoring + Prime-Power Kummer/Lucas Valuation |
| **SS-2** | `#129` | **CF 1821F — Timber** | `4B#12` | Inclusion-Exclusion on Domino Fall Directions $\frac{1}{1-x-yx^{k+1}(2-x^k)}$ |
| **Int-1** | `#025` | **ABC 240 G — Teleporting Takahashi** | `2A#43` | 3D Walk Decoupled into 1D $\times$ Rotated 2D $(u,v) = (x+y, x-y)$ Bivariate Binomials |
| **Int-2** | `#232` | **QOJ 4815 — 2D Bostan–Mori / Implicit Tree** | `3A#11` | 2D Rational Bostan–Mori $[x^n y^m] P(x,y)/Q(x,y)$ & Small-Prime Implicit Tree |
| **Adv-1** | `#237` | **yukicoder 1080 — Delannoy / Chebyshev Sum** | `4A#P22` | Rational Bivariate Diagonal |
| **Adv-2** | `#074` | **AGC 058 D — Yet Another ABC String** | `2B#A8` | Trivariate Rational Cluster Diagonal $[x^A y^B z^C] \frac{1-xyz}{1-(x+y+z)+2xyz}$ |
| **Mas-1** | `#240` | **yukicoder 1783 — Digits-Sum-Mod-10 Convolution** | `4A#P25` | Radix-10 Multivariate DFT + Twisted Kronecker Truncated Power $F(x)^K$ |
| **Mas-2** | `#214` | **UOJ 596 — [集训队互测2021] 三维立体混元劲** | `4A#P28` | 3D Connected Hypergraphs via Twisted Kronecker $\chi$-Graded $\ln G(x,y,z)$ & Radial Derivation $\mathfrak{D} = x\partial_x + y\partial_y + z\partial_z$ in $O(ABC \log(ABC))$ |

> **Ch 16 Quarantined Library Verification Footnote (§5)**: `R-42`, `R-43`.

#### Chapter 17: 2D Quarter-Plane Obstinate Kernel Method, Multivariate Good–Lagrange Inversion & MacMahon's Master Theorem (`ch17_quarter_plane_obstinate_kernel_good_lagrange_macmahon.qmd`)
- **Ring / Operator**: Iterated Laurent Ring $K((x))((y))$, Dihydral Birational Group $\mathcal{G} = \langle \Phi, \Psi \rangle$, Multivariate Jacobian $\det(I - J_G(u))$ $\mid$ **Prereqs**: Ch 10, Ch 11, Ch 13, Ch 15, Ch 16 (Multivariate Systems, LIF, Matrix-Tree, Kernel Method, Bivariate Hierarchy) $\mid$ **Waves**: `3C (§3), 4B (§4)`
- **Sub-sections & Core Derivations**:
  - **17.1**: Multivariate Good–Lagrange Inversion (Forms 1 & 2 and Bipartite Rank-1 Matrix Determinant Collapse)
  - **17.2**: MacMahon's Master Theorem $[x_1^{n_1} \cdots x_m^{n_m}] \prod_{i=1}^m (\sum_{j=1}^m a_{i,j} x_j)^{n_i} = [x_1^{n_1} \cdots x_m^{n_m}] \frac{1}{\det(I - X A)}$
  - **17.3**: The Ring of Symmetric Functions $\Lambda$, Newton–Girard Power-Sum Duality $P(t) = \frac{d}{dt}\ln H(t)$, & Failure Mode #7
  - **17.4**: 2D Quarter-Plane Lattice Walks ($i, j \ge 0$), The Obstinate Kernel Method (Dihedral Orbit Elimination), & Bivariate PDE Companion Matrices
- **Diagnostic Signal & Scratchpad**: 2D walks restricted to the first quadrant $\mathbb{Z}_{\ge 0}^2$ (such as Kreweras, Tandem, or Gessel walks), coupled multivariate tree/functional equations $F_i = x_i \phi_i(F_1, \dots, F_m)$, or permanent/cycle-cover sums over $m$ variables. $\mid$ *Scratchpad*: Check if the step-set inventory $S(x,y)$ admits birational involutions $\iota_1, \iota_2$ generating a finite dihedral group $D_{2k}$, or for coupled functional equations apply the Jacobian determinant factor of Multivariate Good-Lagrange.
- **Flagship Worked Example (`UOJ 424` / Obstinate Kernel Method on Tandem Walk & MacMahon's Master Theorem)**: *Problem*: Count 2D walks in $\mathbb{Z}_{\ge 0}^2$ with step set $\{(+1,0), (-1,+1), (0,-1)\}$ and derive MacMahon's Master Theorem from Good-Lagrange. *Derivation*: Apply the $D_6$ group orbit of $(x,y) \mapsto (y/x, y)$ and $(x, x/y)$ to eliminate boundary series $A(x,t), B(y,t)$ and extract $[x^0 y^0]$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 17`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#154` | **Luogu P4456 — [CQOI2018] 交错序列** | `5A#7` | 2D Constrained Step Walk $(x, y)$ Moment Extraction $\sum i^a j^b$ |
| **SS-2** | `#044` | **ABC 336 G — 16 Integers** | `3A#33` | De Bruijn Eulerian Graph + MacMahon Master Theorem $\det(I - X A)^{-1}$ |
| **Int-1** | `#228` | **LOJ 6671 — Unlabeled Phylogenetic Trees** | `3B#17` | Multivariate Burnside Cycle Index + Good–Lagrange |
| **Int-2** | `#219` | **LOJ 3398 — 带加强和多项木** | `3B#9` | Multivariate Implicit Tree System + Good–Lagrange Jacobian $\det(I - J_G(u))$ |
| **Adv-1** | `#015` | **`fps_24_v` — 12 Directions** | `1A#33` | 2D Laurent Step-Polynomial Factorization & Boundary Reduction |
| **Adv-2** | `#204` | **Luogu P7599 — [APIO2021] 雨林跳跃** | `4B#16` | 2D Dominance Lattice Walk + Bivariate Kernel Method |
| **Mas-1** | `#138` | **CF Gym 102538F — 3D Walk / Quarter Plane** | `4B#31` | Quarter-Plane Obstinate Kernel / Algebraic Group Involution |
| **Mas-2** | `#234` | **QOJ 8048 — Good–Lagrange Multivariate** | `4B#30` | Multivariate Good–Lagrange Jacobian $\det(I - J_G(u))$ + Newton |

> **Ch 17 Quarantined Library Verification Footnote (§5)**: Uses prerequisite chapter primitives (`0` new bare templates).


### Part V: D-Finite ODEs, Transposition Principle (`mulT`) & Fast Composition (`Kinoshita–Li`) (Chapters 18–21)

#### Chapter 18: D-Finite (Holonomic) Series, Weyl Algebra $K[x]\langle D \rangle$, Algebraic-to-ODE Compilation, $O(N)$ P-Recursive Unrolling, 3D Rational Diagonals & Mod-$p$ Indicial Lifting (`ch18_d_finite_weyl_algebra_p_recursive_indicial_lifting.qmd`)
- **Ring / Operator**: Non-Commutative Weyl Algebra $K[x]\langle D \rangle / (Dx - xD - 1)$, Shift Algebra $K[n]\langle S_n \rangle$, Jet Ring $\mathbb{F}_p[\epsilon]/(\epsilon^r)$ for Mod-$p$ Indicial Root Lifting $\mid$ **Prereqs**: Ch 02, Ch 05, Ch 07, Ch 11, Ch 16 (Formal Calculus, Rational GFs, Roots-of-Unity Filters, Algebraic Series, Diagonals) $\mid$ **Waves**: `5A (§1, §3)`
- **Sub-sections & Core Derivations**:
  - **18.1**: D-Finite (Holonomic) Series $\leftrightarrow$ P-Recursive Sequences & The Euler Operator Dictionary ($\vartheta = x D_x$, $x^a D_x^b \leftrightarrow$ Shift Operators)
  - **18.2**: The Abel–Cockle–Harley–Comtet Theorem (Algebraic $\implies$ D-Finite) & Recipes A / B
  - **18.3**: The Complete 7-Archetype Differential Equation Substitution Table (`TECHNIQUE_TAXONOMY.md` §3.6.B)
  - **18.4**: Closure Properties of D-Finite Series & Failure Mode #8 ($p$-Adic Indicial Lifting over $\mathbb{Z}/p^{V+1}\mathbb{Z}$ Across $p_r(n) \equiv 0 \pmod p$ Singularities)
- **Diagnostic Signal & Scratchpad**: A sequence whose GF is algebraic (contains $\sqrt{\Delta(x)}$), is a diagonal of a rational function, or is a product of low-order D-finite series (like Bessel/Catalan/Motzkin products), requiring $[x^n] F(x)$ in $O(n)$ time or $O(\sqrt{n} \log n)$ time instead of $O(n \log n)$ NTT. $\mid$ *Scratchpad*: Differentiate the algebraic equation $F(x) = A(x)^{1/2}$ log-linearly to get $2 A(x) F'(x) = A'(x) F(x)$, extract $[x^n]$ to obtain a short P-recurrence, and guard against $p_r(n) \equiv 0 \pmod p$ by maintaining $(a_n + a_n^{(1)} \epsilon) \pmod{\epsilon^2}$.
- **Flagship Worked Example (`LOJ 6728` / `ABC 240 G` — From Algebraic Radical GF to $O(N)$ P-Recurrence & Mod-$p$ Singularity Lifting)**: *Problem*: Convert $F(x) = (1 - 2(a+b)x + (a-b)^2 x^2)^{-1/2}$ into a 3-term P-recurrence and evaluate across $n+1 \equiv 0 \pmod p$. *Derivation*: Differentiate $\ln F(x)$ to obtain $(1 - 2(a+b)x + (a-b)^2 x^2) F'(x) = (a+b - (a-b)^2 x) F(x)$, extract $[x^n]$, and trace $\epsilon$-lifting at $n = p-1$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 18`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#151` | **Luogu P4002 — [清华集训2017] 生成树计数** | `3A#27` | Algebraic / Prüfer Tree Block Sum $\to$ D-Finite Differential Reduction |
| **SS-2** | `#064` | **ARC 153 D — Sum of Sum of Digits** | `5B#D9` | Carry-Propagation Polynomial Shift & D-Finite Recurrence |
| **Int-1** | `#022` | **ABC 226 H — Random K-th Max** | `2B#E2` | Order-Statistic Integral $\int_0^1 t^k(1-t)^{n-k} dt$ & Holonomic Recurrence |
| **Int-2** | `#239` | **yukicoder 1504 — Holonomic Walk** | `5A#25` | Algebraic-to-D-Finite ODE Compilation for $O(N)$ Walk Extraction |
| **Adv-1** | `#125` | **CF 1667E — Centroid Probabilities** | `3A#8` | Tree Centroid Differential Recurrence + Reverse Convolution |
| **Adv-2** | `#088` | **CF 755G — PolandBall and Many Other Balls** | `2B#D4` | Continuant Matrix GF + Hyperbola Residue + $O(K)$ 2nd-Order D-Finite ODE |
| **Mas-1** | `#211` | **UOJ 450 — [集训队作业2018] 复读机** | `1A#28` | Mod-$d$ Roots-of-Unity Filter $(e^x + e^{\omega x} + e^{\omega^2 x})^k$ + 2D PDE |
| **Mas-2** | `#230` | **LOJ 6728 — U 群把妹王** | `3A#12` | Algebraic-to-D-Finite ODE Compilation & Single-Pass $O(N)$ P-Recursive Unrolling for Biconnected / Connected Graphs |

> **Ch 18 Quarantined Library Verification Footnote (§5)**: `R-66`.

#### Chapter 19: Coupled Sparse Composition, WZ Creative Telescoping & Truncated Taylor ODEs (`EI 科技` for $f(P(x)) \bmod x^n$) (`ch19_coupled_sparse_composition_wz_truncated_taylor_ode.qmd`)
- **Ring / Operator**: Quotient Differential Module $K[x]/(x^n)$, WZ Certificate Pair $(F(n,k), G(n,k))$ with $\Delta_n F = \Delta_k G$, Truncated Holonomic Remainder Equation $\mid$ **Prereqs**: Ch 02, Ch 06, Ch 08, Ch 18 (Sparse ODEs, Falling Factorials, Inclusion-Exclusion, D-Finite Weyl Algebra) $\mid$ **Waves**: `2A (§4), 5A (§4)`
- **Sub-sections & Core Derivations**:
  - **19.1**: Non-Commutative Weyl & Shift Operator Algebras ($K[x]\langle D_x \rangle$ and $K[n]\langle E_n \rangle$)
  - **19.2**: Zeilberger's Creative Telescoping, WZ Pairs & `EI`'s Differential-Residue Binomial Sum Engine (Engine 3)
  - **19.3**: Coupled $r$-State Sparse Composition $F(P(x))$ in $O(rNK)$ & `EI 科技` Truncated Taylor ODEs ($A(x)F_{<N}' + B(x)F_{<N} = C(x) - R_N(x)$)
  - **19.4**: Motivating Sub-Section: Singularity Analysis Intuition ($[x^n]F(x) \sim \frac{C}{\Gamma(\alpha)} R^{-n} n^{\alpha-1}$) & $O(\sqrt{N}\log N)$ Bostan–Chudnovsky–Chudnovsky Holonomic BSGS
- **Diagnostic Signal & Scratchpad**: Definite hypergeometric sums $\sum_k \binom{n}{k}^a \binom{n+k}{k}^b x^k$ that resist snake-oil OGF swaps, or compositions $F(P(x))$ where $P(x)$ has degree $\le 5$ and $N = 10^7$ (so $O(N \log N)$ NTT TLEs while $O(N)$ recurrence passes). $\mid$ *Scratchpad*: Construct the ODE for $F(u)$, substitute $u = P(x)$ and $du = P'(x) dx$ to obtain a linear ODE for $H(x) = F(P(x))$, and read off the $O(N \deg P)$ coefficient recurrence.
- **Flagship Worked Example (`LOJ 6538` / `Luogu P7435` / Sparse Composition ODE Pullback & WZ Creative Telescoping)**: *Problem*: Compute $[x^n] F(P(x))$ for $\deg P \le 4$ up to $N = 5 \cdot 10^6$ in $O(N)$ time, and telescope $\sum_k \binom{n}{k}^2 \binom{n+k}{k}^2$. *Derivation*: Pull back the first-order ODE $u F'(u) = \alpha F(u)$ along $u = P(x)$ to get $P(x) H'(x) = \alpha P'(x) H(x)$.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 19`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#242` | **yukicoder 1939 — Numbered Colorful Balls** | `5A#2` | $O(NK)$ Sparse EGF Differential Recurrence Pullback |
| **SS-2** | `#120` | **CF 1548C — The Three Little Pigs** | `2A#7` | Sparse Composition Pullback $H(x) = \frac{u^{N+1}-1}{u-1}\big\rvert_{u=(1+x)^3}$ in $O(N)$ |
| **Int-1** | `#095` | **CF 932E — Team Work** | `1B#10` | Stirling S2 Expansion $\sum S(K,j)\binom{N}{j}j! 2^{N-j}$ + $O(K)$ `EI 科技` ODE |
| **Int-2** | `#195` | **Luogu P6667 — [清华集训2016] 如何优雅地求和** | `2A#25` | Binomial Sum $\sum \binom{n}{k} x^k (1-x)^{n-k} f(k)$ via Falling Factorials / $O(m)$ ODE |
| **Adv-1** | `#028` | **ABC 260 Ex — Colorfulness** | `2B#B7` | Adjacent-Color IE + Coupled Divide-and-Conquer NTT + Truncated Taylor Shift |
| **Adv-2** | `#118` | **CF 1515E — Phoenix and Computers** | `2B#B1` | Sparse Composition Pullback $F(x,y) = (1 - x(e^y-1))^{-1}$ + Row ODE |
| **Mas-1** | `#072` | **AGC 043 D — Merge Triplets** | `2B#C3` | Sparse Composition ODE $\partial_x F = (y + xy^{-1} + x^2)F$ on $\exp(xy + \frac{x^2}{2}y^{-1} + \frac{x^3}{3})$ |
| **Mas-2** | `#213` | **UOJ 514 — [UR #19] 通用测评号** | `5A#24` | `EI 科技` Truncated Exponential Derivative $\frac{d}{dx}(e^{-x} S_{<a}(x)) = -e^{-x} \frac{x^{a-1}}{(a-1)!}$ |

> **Ch 19 Quarantined Library Verification Footnote (§5)**: Uses prerequisite chapter primitives (`0` new bare templates).

#### Chapter 20: Tellegen's Transposition Principle (`mulT`), Subproduct Tree Multipoint Evaluation, Fast Interpolation, Sampling Point Shift & $O(\sqrt{P}\log P)$ Factorial (`ch20_tellegen_transposition_multipoint_sampling_shift.qmd`)
- **Ring / Operator**: Dual Space $(K[x]_{<n})^* \cong K[x^{-1}]_{>-n}$, Middle Product $\operatorname{mulT}(A, B)_k = \sum_i a_i b_{i+k}$, Subproduct Tree over $K[x]$ $\mid$ **Prereqs**: Ch 01, Ch 05, Ch 06, Ch 07 (Convolutions, Partial Fractions, Consecutive Lagrange Interpolation, CZT) $\mid$ **Waves**: `4C (§1–§2), 5B (§2, §4)`
- **Sub-sections & Core Derivations**:
  - **20.1**: Tellegen's Transposition Principle (`转置原理`) & Straight-Line Linear Circuits in $(K[x]/(x^n))^*$
  - **20.2**: The Middle Product (`mulT`) $\text{mulT}(A, B)_k = \sum_{i \ge 0} a_i b_{i+k}$ & $2\times$ FFT / Bit-Reversal Optimizations (`TECHNIQUE_TAXONOMY.md` §3.7.C)
  - **20.3**: Division-Free Multipoint Evaluation (`eval`) & Fast Lagrange Interpolation (`interp`) via Subproduct Trees in $O(N \log^2 N)$
  - **20.4**: Transposed Chirp Z-Transform ($\text{czt}^\top$), Shift of Sampling Points (`连续点值平移` $f(0..d) \mapsto f(c..c+d)$), & $O(\sqrt{P}\log P)$ Block Factorial ($N! \bmod P$)
- **Diagnostic Signal & Scratchpad**: Evaluating a degree-$N$ polynomial at $M$ arbitrary points $x_1, \dots, x_M$, recovering $P(x)$ from values, shifting evaluations on an arithmetic progression $f(0), \dots, f(d)$ to $f(c), \dots, f(c+d)$, or computing products $\prod_{i=1}^N (x + i)$ at $N = 10^9$. $\mid$ *Scratchpad*: Express evaluation $P(x_i) = [x^0] \text{mulT}(P(x), \frac{1}{1 - x_i x})$ via middle products descending the subproduct tree $T_{u} = T_{2u} T_{2u+1}$ in $O(N \log^2 N)$ without polynomial division.
- **Flagship Worked Example (`Luogu P5667` — Lagrange Interpolation on Arithmetic Progression & Tellegen `mulT` Multipoint Eval)**: *Problem*: Given $f(0), f(1), \dots, f(n)$, compute $f(m), f(m+1), \dots, f(m+n)$ in $O(n \log n)$ time. *Derivation*: Rewrite the Lagrange basis as $f(m+k) = \prod_{j=0}^n (m+k-j) \sum_{i=0}^n \frac{(-1)^{n-i} f(i)}{i!(n-i)! (m+k-i)}$, which is a single 1D convolution.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 20`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#050` | **ARC 033 D — 多項式 (Polynomial)** | `5B#D1` | $O(N)$ Sequential Prefix/Suffix Lagrange Interpolation |
| **SS-2** | `#197` | **Luogu P7116 — [NOIP2020] 微信步数** | `5B#D7` | High-Dimensional Walk Volume Sum via Bernoulli / Lagrange Interpolation |
| **Int-1** | `#127` | **CF 1770G — Koxia and Bracket** | `5B#B8` | Transposed Divide-and-Conquer NTT on Bracket Prefixes |
| **Int-2** | `#167` | **Luogu P5284 — [十二省联考2019] 字符串问题** | `5B#B5` | Suffix Automaton DAG Path via Segment-Tree / Transposed Optimization |
| **Adv-1** | `#208` | **UOJ 182 — a^-1 + b problem** | `5B#B12` | Alternating Fractional Linear Möbius Transforms + Multipoint Eval |
| **Adv-2** | `#202` | **Luogu P7440 — [KrOI2021] Feux Follets** | `5B#B13` | Multipoint Evaluation + Transposed Polynomial Divide-and-Conquer |
| **Mas-1** | `#181` | **Luogu P5668 — N-Step Shift** | `5B#D8` | Sequential Lagrange Shift + Multipoint Evaluation |
| **Mas-2** | `#217` | **LOJ 161 — 快速阶乘算法** | `5B#D11` | $O(\sqrt{P} \log P)$ Sampling Shift Evaluation |

> **Ch 20 Quarantined Library Verification Footnote (§5)**: `R-26`, `R-27`, `R-30`.

#### Chapter 21: Kinoshita–Li $O(N \log^2 N)$ Fast Composition, Power Projection & All-$n$ Compositional Inverse (`revert` & $G(G(x))=F(x)$) (`ch21_kinoshita_li_composition_power_projection_revert.qmd`)
- **Ring / Operator**: Bivariate Laurent Dual $(K[[x]][y])^*$, Composition Operator $C_F(G) = G \circ F \bmod x^N$, Adjoint Power Projection $C_F^\top(w)_k = \langle w, F^k \rangle$ $\mid$ **Prereqs**: Ch 11, Ch 12, Ch 16, Ch 20 (Lagrange Inversion, Block-Cut Inversion, 2D Bostan–Mori, Tellegen Transposition `mulT`) $\mid$ **Waves**: `4A (§4), 4C (§1), 5B (§2–§3)`
- **Sub-sections & Core Derivations**:
  - **21.1**: Power Projection ($\text{proj}_k = \sum_{i=0}^{N-1} w_i [x^i]F(x)^k$) via Kinoshita–Li 2D Bostan–Mori in $O(N \log^2 N)$
  - **21.2**: Kinoshita–Li FPS Composition ($H(x) = G(F(x)) \bmod x^N$) via Tellegen Transposition of Power Projection
  - **21.3**: `Elegia`'s All-$n$ Coupled Binomial Sum Linearization (Form 6 Case B via `compose` / `power_projection`)
  - **21.4**: Dual-Route Compositional Inverse (`revert`), Failure Mode #6, & Functional Square Roots $G(G(x)) = F(x)$ (Degree $p+2$ Artin–Schreier Obstruction)
- **Diagnostic Signal & Scratchpad**: Computing the entire series $F(G(x)) \bmod x^N$ for arbitrary dense $F, G$, computing $[x^{N-1}] H(x) G(x)^k$ for all $k=0..N-1$ simultaneously, or computing all $N$ coefficients of the compositional inverse $G^{\langle -1 \rangle}(x)$ when $N \le 2 \cdot 10^5$. $\mid$ *Scratchpad*: Never run $N$ separate Lagrange inversions! Use Power Projection (`PowerProj(H, G)`) to obtain $c_k = [x^{N-1}] (G(x)/x)^{-k}$ for all $k$, then recover $[x^k] G^{\langle -1 \rangle}(x) = \frac{1}{N-1} [x^{N-1-k}] (G(x)/x)^{-(N-1)}$ or via logarithmic derivative.
- **Flagship Worked Example (`ARC 138 F` / `ABC 281 Ex` / Kinoshita-Li $O(N \log^2 N)$ Composition, Power Projection & All-$n$ `revert`)**: *Problem*: Compute all coefficients of $F(G(x)) \bmod x^N$ and $G^{\langle -1 \rangle}(x) \bmod x^N$ for $N = 131072$. *Derivation*: Trace the bivariate parity reduction $(d_x, d_y) = (n/2^k, 2^k)$ for Power Projection and invert via Tellegen transposition.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 21`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#036` | **ABC 281 Ex — Alchemy** | `2B#B12` | Falling-Factorial EGF + Simultaneous All-$n$ `compositional_inverse` |
| **SS-2** | `#045` | **ABC 345 G — Sugoroku 5** | `5B#B2` | Hitting-Time PGF + Kinoshita–Li $O(N \log^2 N)$ Fast Polynomial Composition $F(G(x))$ |
| **Int-1** | `#047` | **ABC 387 G — Prime Circuit** | `4A#P25` | Prime-Cycle Cactus EGF via $O(N \log^2 N)$ Fast Composition $C(T(x))$ |
| **Int-2** | `#059` | **ARC 137 F — Overlaps** | `3B#22` | Implicit Algebraic Equation + Riccati ODE + Fast Polynomial Composition |
| **Adv-1** | `#065` | **ARC 154 F — Dice Game** | `4A#P23` | Coupon Collector Moment EGF + Fast Polynomial Composition |
| **Adv-2** | `#218` | **LOJ 171 / QOJ 6504 — 幂投影 (Power Projection)** | `5B#B16` | Kinoshita–Li Transposed Composition $\sum_i w_i [x^i] F(x)^k$ |
| **Mas-1** | `#235` | **QOJ 8528 — FPS Composition / Power Projection** | `4A#P26` | Kinoshita–Li $O(N \log^2 N)$ Bivariate Parity Splitting Algorithm |
| **Mas-2** | `#017` | **`fps_24_x` — Functional Square Root** | `1A#31` | Iterated Composition $F(F(x)) = G(x)$ in $\mathbb{F}_p[[x]]/(x^N)$ |

> **Ch 21 Quarantined Library Verification Footnote (§5)**: `R-32`, `R-33`, `R-34`, `R-35`.


### Part VI: Structural Extensions: Tree DP + FPS, $q$-Series & Bitwise / Dirichlet Algebras (Chapters 22–24)

#### Chapter 22: Tree DP with Generating Functions: Heavy-Light Chain Merging, Weight-Balanced Static Top Trees, $2 \times 2$ Polynomial Transfer Matrices, Dynamic FWT Zero-Divisor Pairs $(a,c)=a\cdot 0^c$ & Rerooting `mulT` (`ch22_tree_dp_fps_hld_static_top_tree_zero_divisor.qmd`)
- **Ring / Operator**: Matrix Semigroup $\operatorname{Mat}_2(K[x])$, Rake/Compress Cluster Algebra, Zero-Divisor Valuation Monoid $K^\times \times \mathbb{Z}_{\ge 0}$ ($a \cdot 0^c$) $\mid$ **Prereqs**: Ch 01, Ch 06, Ch 09, Ch 20 (Product Trees, Stirling/Taylor Shift, D&C NTT, Tellegen `mulT`) $\mid$ **Waves**: `5B (§1)`
- **Sub-sections & Core Derivations**:
  - **22.1**: Subtree Size Convolution Bounds ($O(N^2)$) vs. Arbitrary-Degree Polynomial Merging ($O(N \log^2 N)$) & HLD Transfer Matrices
  - **22.2**: HLD + Weight-Balanced Static Top Tree (`全局平衡二叉树`): `Rake` & 3-Way Weighted-Midpoint `Compress` (`TECHNIQUE_TAXONOMY.md` §3.7.B)
  - **22.3**: Dynamic DP with Polynomials / FWT & Failure Mode #10 (Zero-Divisor Pairs $(a, c) \equiv a \cdot 0^c \in \mathbb{F}_p^\times \times \mathbb{Z}_{\ge 0}$)
  - **22.4**: Subtree Frequency Rerooting, Centroid FFT Edge-Length Convolutions, & Vandermonde `mulT` on Trees
- **Diagnostic Signal & Scratchpad**: Counting subtrees, independent sets, matchings, or $k$-component cuts on an arbitrary tree $T$ ($N \le 10^5$) for all sizes $k=1..N$, or maintaining DP over a tree with point updates and FWT/NTT transitions. $\mid$ *Scratchpad*: Decompose $T$ into heavy paths. At each node $u$, first merge all light-child polynomial vectors using a min-heap by degree ($O(S_u \log^2 S_u)$), then multiply the resulting $2 \times 2$ polynomial transition matrices along each heavy path using weighted midpoint divide-and-conquer.
- **Flagship Worked Example (`Luogu P4719` / `Luogu P4581` — HLD + Divide-and-Conquer Tree Independent Set Polynomial & Dynamic FWT Zero-Divisor Pairs)**: *Problem*: Given a tree of size $N \le 10^5$, compute the number of independent sets of size $k$ for all $0 \le k \le N$ in $O(N \log^2 N)$, and maintain dynamic subtree XOR counts. *Derivation*: Formulate the heavy-chain matrix product $\prod_{u \in \text{chain}} \begin{pmatrix} L_{u,0}(x) & L_{u,0}(x) \\ x L_{u,1}(x) & 0 \end{pmatrix}$ and evaluate via balanced divide-and-conquer.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 22`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#031` | **ABC 269 Ex — Antichain** | `5B#A1` | Heavy-Light Decomposition + D&C Tree FPS |
| **SS-2** | `#124` | **CF 1613F — Tree Coloring** | `2A#36` | Derangement-Style Tree Degree Inclusion-Exclusion $\prod(1 + c_u x)$ |
| **Int-1** | `#046` | **ABC 355 G — Baseball** | `5B#A3` | Laminar Containment Tree + Tree-DP Convolution |
| **Int-2** | `#198` | **Luogu P7279 — 光棱碎片 (Prism Shards)** | `5B#A4` | $2 \times 2$ Polynomial Matrix Heavy-Light Decomposition |
| **Adv-1** | `#149` | **Luogu P3781 / LOJ 2269 — [SDOI2017] 切树游戏** | `5B#A8` | FWT + Heavy-Light Decomposition + Zero-Count $(\text{val}, \text{cnt})$ Ring |
| **Adv-2** | `#136` | **CF 2006E — Iris's Full Binary Tree** | `5B#A15` | Centroid / Heavy-Light Tree Convolution |
| **Mas-1** | `#166` | **Luogu P5281 / LOJ 3044 — [ZJOI2019] Minimax 搜索** | `5B#A11` | Dynamic Tree DP + HLD Rational / Polynomial Chain Product |
| **Mas-2** | `#145` | **Luogu P3348 — [ZJOI2016] 大森林** | `5B#A19` | Offline Tree Modification + HLD Polynomial Chain Product |

> **Ch 22 Quarantined Library Verification Footnote (§5)**: `R-67`.

#### Chapter 23: $q$-Analogues, Gaussian Binomials, $q$-Pentagonal / Durfee Identities, $q$-Difference Equations, $q$-Lucas & MacWilliams / Krawtchouk Duality (`ch23_q_analogues_gaussian_binomials_q_lucas_macwilliams.qmd`)
- **Ring / Operator**: $q$-Deformed Ring $K(q)[[x]]$, $q$-Shift Operator $T_q f(x) = f(qx)$, Grassmannian Subspace Lattice $\mathcal{L}(\mathbb{F}_q^n)$, Krawtchouk Group Ring $K[\mathbb{F}_2^m]$ $\mid$ **Prereqs**: Ch 03, Ch 06, Ch 11 (Partitions/Pentagonal/Durfee, Binomial Identities, Formal Residues) $\mid$ **Waves**: `4A (§3), 5B (§5)`
- **Sub-sections & Core Derivations**:
  - **23.1**: $q$-Pochhammer Symbols $(a; q)_n$, Gaussian $q$-Binomials $\begin{bmatrix} n \\ k \end{bmatrix}_q$, & The $q$-Difference Equation Engine $A(x) = P(x)A(qx) + Q(x)$
  - **23.2**: Characteristic-$p$ Hazards: Failure Mode #9 ($q$-Lucas Theorem at Roots of Unity $q^d = 1$) & Chirp-Z $q$-Convolution
  - **23.3**: Euler's Pentagonal Number Theorem, Jacobi's Triple Product & Durfee Square Decomposition (`TECHNIQUE_TAXONOMY.md` §3.8.2)
  - **23.4**: Vector Spaces over $\mathbb{F}_q$, Grassmannian Subspace Inversion & Self-Contained 5-Line Krawtchouk / MacWilliams Duality
- **Diagnostic Signal & Scratchpad**: Counting full-rank matrices or subspaces over $\mathbb{F}_q$, subsets with prescribed modular sum $\sum_{s \in S} s \equiv r \pmod d$, or inversion/area statistics $q^{\text{inv}(\pi)}$. $\mid$ *Scratchpad*: Replace $(1+x)^n$ with $\prod_{k=0}^{n-1} (1 + q^k x)$, apply the $q$-shift $x \mapsto qx$ to obtain the $q$-difference equation $(1 - x) F(x) = (1 - q^n x) F(qx)$, and extract $[x^k]$ to compute all coefficients in $O(N)$ time; if $q = \zeta_d$ is a $d$-th root of unity, apply the $q$-Lucas reduction.
- **Flagship Worked Example (`ARC 145 F` / `ARC 139 F` — $q$-Binomial Subspace Enumeration & $q$-Lucas Root-of-Unity Reduction)**: *Problem*: Extract coefficients of $F(x) = \prod_{k=0}^{n-1} (1 + q^k x)$ in $O(n)$ time and evaluate $\begin{bmatrix} n \\ k \end{bmatrix}_{\zeta_d}$ at a primitive $d$-th root of unity. *Derivation*: Use $(1 + q^n x) F(x) = (1 + x) F(qx)$ to compare $[x^k]$ on both sides.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 23`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#123` | **CF 1603F — October 18, 2017** | `5B#E1` | $q$-Binomial Rank Enumeration in $\mathbb{F}_2^k$ |
| **SS-2** | `#033` | **ABC 278 Ex — make 1** | `5B#E2` | Basis / XOR Space $q$-Binomial & $q$-Pochhammer |
| **Int-1** | `#233` | **QOJ 5097 / SOJ 703 — 布尔立方 (Boolean Cube)** | `5B#E7` | Gaussian $q$-Binomial $\begin{bmatrix} n \\ k \end{bmatrix}_2$ Subspace Lattice Enumeration over $\mathbb{F}_2^n$ |
| **Int-2** | `#057` | **ARC 134 E — Modulo Nim** | `5B#E9` | $q$-Analogue / Subset Modulo Game Reduction |
| **Adv-1** | `#062` | **ARC 139 F — Many Xor Optimization Problems** | `5B#E4` | $q$-Binomial Gaussian Elimination Basis Enumeration |
| **Adv-2** | `#132` | **CF 1916F — Group Division** | `5B#E6` | Bipolar Orientation / Biconnected $q$-Analogue |
| **Mas-1** | `#063` | **ARC 145 F — Modulo Sum of Increasing Sequences** | `4B#33` | $q$-Pentagonal / Cyclic Orbit Sum + Good–Lagrange |
| **Mas-2** | `#111` | **CF 1336E2 — Chiori and Doll Picking (Hard)** | `4A#P17` | MacWilliams Dual-Code Krawtchouk Transform ($O(2^{m-r})$) |

> **Ch 23 Quarantined Library Verification Footnote (§5)**: `R-48`, `R-49`.

#### Chapter 24: Bitwise Algebras (FWT/SOS), Set Power Series $\mathcal{R}_n = K[x_1,\dots,x_n]/(x_i^2)$ ($\exp, \ln$, `Elegia` Composition, Pointed Biconnected SPS) & Dirichlet Generating Functions $\mathcal{D}_f$ ($\Omega(n)$-Derivations & Multiplicative Sieves) (`ch24_bitwise_fwt_set_power_series_dirichlet_gf.qmd`)
- **Ring / Operator**: Truncated Boolean Ring $\mathcal{R}_n = K[x_1, \dots, x_n]/(x_1^2, \dots, x_n^2) \cong K[z]/(z^{n+1})^{2^n}$, Dirichlet Ring $(\mathcal{D}, +, *_{\text{Dir}})$ with Derivation $\partial_\Omega(n^{-s}) = \Omega(n)n^{-s}$ $\mid$ **Prereqs**: Ch 02, Ch 04, Ch 12, Ch 13, Ch 22 (Formal Calculus, $\ln/\exp$, Pointed Block-Cut Biconnected Graphs, Matrix-Tree, FWT Zero-Divisor Pairs) $\mid$ **Waves**: `1B (§5), 4A (§2), 5B (§6)`
- **Sub-sections & Core Derivations**:
  - **24.1**: Bitwise Group Algebras (OR, AND, XOR Fast Walsh–Hadamard / Zeta / Möbius Transforms in $O(n 2^n)$)
  - **24.2**: The Set Power Series Ring $\mathcal{R}_n = K[x_1, \dots, x_n]/(x_1^2, \dots, x_n^2)$ & Ranked Fast Zeta Transform in $O(n^2 2^n)$
  - **24.3**: Transcendental Operations on $\mathcal{R}_n$ ($\text{inv}, \ln, \exp, P^\alpha$), Division-Free MSB Split, `Elegia`'s $O(n^2 2^n)$ General SPS Composition, & Pointed Biconnected Graph SPS (`#215 UOJ 910`)
  - **24.4**: The Ring of Dirichlet Series $\mathcal{D}_f$, Bell Series & The Prime-Multiplicity $\Omega(n)$-Derivation $\partial_\Omega(n^{-s}) = \Omega(n) n^{-s}$ (`#212 UOJ 752`)
- **Diagnostic Signal & Scratchpad**: For $n \le 21$: counting connected/biconnected/DAG/Eulerian induced subgraphs on a given $n$-vertex graph $G$, or set-partition problems over $2^V$. For $N \le 10^{11}$: prefix sums of multiplicative arithmetic functions $\sum_{i=1}^N (f * g)(i)$. $\mid$ *Scratchpad*: For subgraph counting on $2^V$, lift indicator weights $f(S)$ to ranked SPS $\hat{f}(S, u) = f(S) u^{|S|}$, apply Fast Zeta Transform in $O(n^2 2^n)$, run the exact Chapter 05/13 truncated FPS operation (`ln`, `exp`, `inv`) of length $n+1$ independently at each mask $S$, and invert via Fast Möbius Transform.
- **Flagship Worked Example (`CF 449D` / `ABC 213 G` — Connected & Bipartite Induced Subgraphs in $O(n^2 2^n)$ via Ranked SPS $\ln/\exp$ & Du Jiao Dirichlet Sieve)**: *Problem*: Given a graph $G=(V,E)$ with $|V| \le 20$, count connected spanning subgraphs for every subset $S \subseteq V$ in $O(|V|^2 2^{|V|})$. *Derivation*: Define $F(x) = \sum_{S \subseteq V} 2^{|E(S)|} x^S \in \mathcal{R}_n$ and compute $C(x) = \ln F(x)$ in $\mathcal{R}_n$ via Ranked Zeta Transform + pointwise $O(n^2)$ polynomial logarithm.

- **4-Tier Practice Ladder (`8` Disjoint Problems, Verified `Prereqs <= Ch 24`)**:

| Tier | Pool ID | Problem ID & Title | Source Wave | Core Mathematical Mechanism & Pedagogical Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#216` | **CF 449D — Jzzhu and Numbers** | `5B#F1` | Superset SOS DP / Fast Zeta Transform + Inclusion-Exclusion |
| **SS-2** | `#020` | **ABC 213 G — Connectivity 2** | `1B#24` | Connected Subgraph Subset Convolution ($\ln$) |
| **Int-1** | `#027` | **ABC 253 Ex — We Love Forest** | `5A#14` | Set Power Series $\exp$ on Spanning Trees |
| **Int-2** | `#042` | **ABC 306 Ex — Balance Scale** | `5B#F5` | DAG Orientation Set Power Series / Subset Inversion |
| **Adv-1** | `#110` | **CF 1326F2 — Wise Men (Hard Version)** | `2B#C4` | Partition Subset Convolution + SOS / Möbius Inversion |
| **Adv-2** | `#207` | **UOJ 94 — [集训队互测2015] 胡策的统计** | `5B#F7` | Biconnected Subgraphs via Vertex-by-Vertex Set Power Series $\ln$ |
| **Mas-1** | `#231` | **LOJ 6729 — 幂数 (Powerful Numbers)** | `5B#F9` | Prime-Power Bell Series Division & Dirichlet $\exp/\ln$ |
| **Mas-2** | `#038` | **ABC 288 Ex — A Nameless Counting Problem** | `5B#F10` | Dirichlet / Multiplicative Bell Series & XOR DP |

> **Ch 24 Quarantined Library Verification Footnote (§5)**: `R-07`, `R-08`, `R-50`, `R-51`, `R-52`.

---

## 3. Part-End Blind Topic-Group Checkpoints (`CP-I`–`CP-VI`, 48 Disjoint Problems)

> **Two-Stage Spoiler-Free Diagnostic Protocol**:
> 1. **Zero Overlap & Zero Forward References**: All `48` problems (`6 × 8`) are strictly disjoint from the `192` chapter ladder problems and the `14` Grandmaster Synthesis Reserve problems. Every problem in `CP-K` requires only tools taught up to the end of Part `K`.
> 2. **Stage 1 (Blind Diagnostic Arena)**: Presents the raw problem statement constraints and structural regime cues **without** chapter numbers or operator spoilers.
> 3. **Stage 2 (Collapsible Diagnostic Routing & Algebraic Solution Key)**: Hidden inside a `<details>` block so the reader can self-test diagnostic recognition before revealing the target chapter and algebraic reduction.


### CP-I: Blind Checkpoint for Part I — *The Algebraic Engine & Symbolic Translators* (Ch 01–04)

**Diagnostic Brief**: Diagnose whether each problem lives in the unlabeled OGF ring $K[[x]]$ (requiring reverse-indexed correlation, quotient inversion $1/F(x)$, $O(NK)$ sparse power ODEs, or harmonic Euler $\ln/\exp$ and Pólya cycle indices) or the labeled EGF ring (requiring $\exp/\ln$ component extraction, boxed products, or Prüfer degree sequences).

#### Stage 1: Spoiler-Free Blind Problem Arena (`8` Disjoint Problems)

| Slot | Pool ID | Problem ID & Title | Source Wave | Raw Constraint & Structural Cues (Spoiler-Free) |
| :-: | :-: | :--- | :-: | :--- |
| **CP-I.1** | `#078` | **Typical90 #065 — RGB Balls 2** | `4A#P1` | Pick $K$ balls from $R$ red, $G$ green, $B$ blue ($R,G,B,K \le 2\times 10^5$) subject to pairwise sum bounds $r+g \le X, g+b \le Y, b+r \le Z$. |
| **CP-I.2** | `#144` | **Luogu P3338 — [ZJOI2014] 力** | `1B#5` | Given $q_1, \dots, q_n$ ($n \le 10^5$), compute $E_i = \sum_{j < i} \frac{q_j}{(i-j)^2} - \sum_{j > i} \frac{q_j}{(i-j)^2}$ for all $i$. |
| **CP-I.3** | `#246` | **HDU 5279 — YJC plays minecraft** | `1A#26` | Count configurations of $n \le 10^5$ circularly arranged blocks into valid intervals modulo $998244353$. |
| **CP-I.4** | `#032` | **ABC 276 G — Count Sequences** | `1B#19` | Count sequences $a_1, \dots, a_N \in [0, M]$ ($N, M \le 10^7$) with $a_i \not\equiv a_{i+1} \pmod 3$. |
| **CP-I.5** | `#079` | **JSC 2019 Qual F — Candy Retribution** | `1B#15` | Distribute $S$ candies to $N$ children ($N, M, S \le 3\times 10^5$) so the top $M$ children each receive in $[a, b]$. |
| **CP-I.6** | `#250` | **Project Euler 755 — Not Zeckendorf** | `2A#10` | Count ways to express $n \le 10^{13}$ as a sum of distinct Fibonacci numbers. |
| **CP-I.7** | `#037` | **ABC 284 Ex — Count Unlabeled Graphs** | `3A#38` | Count unlabeled simple graphs on $N \le 60$ vertices modulo $p$. |
| **CP-I.8** | `#024` | **ABC 236 Ex — Distinct Multiples** | `1A#19` | Given $D_1, \dots, D_N$ ($N \le 16$), count tuples $(A_1, \dots, A_N)$ of distinct integers in $[1, M]$ with $D_i \mid A_i$. |

#### Stage 2: Diagnostic Routing & Algebraic Solution Key (Collapsible)

<details>
<summary><strong>Click to Reveal CP-I Diagnostic Routing & Algebraic Reduction Key (Verified Prereqs &le; Ch 04)</strong></summary>

| Slot | Pool ID | Target Home Chapter & Section | Diagnostic Trigger & Algebraic Reduction |
| :-: | :-: | :--- | :--- |
| **CP-I.1** | `#078` | **Ch 01 (1.3 2-Way Split Convolution & Filtering)** | Rewrite pairwise upper bounds as single-color lower bounds $K-Y \le r \le R$, split into $(R,G)$ convolved with $(B)$, and extract $[x^K]$ in a single NTT. |
| **CP-I.2** | `#144` | **Ch 01 (1.3 Reverse-Indexing Difference Convolution)** | Recognize the difference index $(i-j)$ as a cross-correlation and reverse $b_k = q_{n-k}$ to compute all $E_i$ via two 1D FFT convolutions. |
| **CP-I.3** | `#246` | **Ch 01 (1.2 Quotient Inversion $1/F(x)$)** | Reduce circular interval block configurations to linear sequence inversion $(1 - G(x))^{-1}$ via `poly_inv`. |
| **CP-I.4** | `#032` | **Ch 01 (1.1 Mod-3 Step OGF $(1+x+x^2)^m$)** | Encode step differences $d_i = a_i - a_{i-1}$ via $\frac{x+x^2}{1-x^3}$ and extract $[x^S]$ in $O(M)$ time via binomial expansion. |
| **CP-I.5** | `#079` | **Ch 03 (3.1 Bounded-Range Composition OGF)** | Sum over the $M$-th largest threshold $v$ and evaluate $[x^{S-Mv}]\frac{(1-x^{b+1})^{N-M}}{(1-x)^{N+1}}$ in $O(S \log S)$ harmonic time. |
| **CP-I.6** | `#250` | **Ch 03 (3.2 Subset-Sum Product $\prod(1 + x^{F_k})$)** | Exploit the sparse gap growth of Fibonacci numbers in $\prod_{k \ge 2}(1 + x^{F_k})$ via recursive range splitting. |
| **CP-I.7** | `#037` | **Ch 03 (3.5 Burnside's Lemma & Partition Cycle Index)** | Enumerate cycle-type partitions $\lambda \vdash N$ and weight each by $2^{\sum_i \lfloor l_i/2 \rfloor + \sum_{i<j} \gcd(l_i, l_j)}$ divided by centralizer size $z_\lambda$. |
| **CP-I.8** | `#024` | **Ch 04 (4.2 Set-Partition $\exp/\ln$ Sieve)** | Weight each connected block $S$ of equal elements by $(-1)^{\lvert S\rvert - 1}(\lvert S\rvert - 1)! \lfloor M / \operatorname{lcm}(S) \rfloor$ and apply set-partition $\exp$. |

</details>


### CP-II: Blind Checkpoint for Part II — *Rational Recurrences, Binomial Sums, Sieves & Pattern Inclusion-Exclusion* (Ch 05–08)

**Diagnostic Brief**: Diagnose whether each problem reduces to a constant-coefficient rational OGF $P(x)/Q(x)$ solved by Bostan–Mori ($N \le 10^{18}$), a binomial/Stirling/Taylor-shift basis transform or $O(d)$ consecutive Lagrange interpolation, a Roots of Unity / Chirp-$Z$ filter on exponents, or a structural Inclusion–Exclusion sieve (Binomial Inversion, Rook polynomials, or Prüfer degree EGF).

#### Stage 1: Spoiler-Free Blind Problem Arena (`8` Disjoint Problems)

| Slot | Pool ID | Problem ID & Title | Source Wave | Raw Constraint & Structural Cues (Spoiler-Free) |
| :-: | :-: | :--- | :-: | :--- |
| **CP-II.1** | `#085` | **CF 451E — Devu and Flowers** | `2B#A1` | Pick $s \le 10^{14}$ flowers from $n \le 20$ boxes where box $i$ has $f_i$ flowers. |
| **CP-II.2** | `#152` | **Luogu P4091 — [HEOI2016] 求和** | `2A#23` | Given $n \le 10^5$, compute $\sum_{i=0}^n \sum_{j=0}^i \left\{\begin{smallmatrix} i \\ j \end{smallmatrix}\right\} 2^j j!$ modulo $998244353$. |
| **CP-II.3** | `#251` | **CF 1264D1 — Beautiful Bracket Sequence (Easy)** | `2A#3` | Given a string $s$ of `(`, `)`, and `?` ($\lvert s\rvert \le 2000$), sum the maximum matched nested parenthesis depth over all $2^q$ completions. |
| **CP-II.4** | `#252` | **CF 622F — The Sum of the k-th Powers** | `2A#26` | Given $n \le 10^9$ and $k \le 10^6$, compute $\sum_{i=1}^n i^k \pmod{10^9+7}$ in $O(k)$ time. |
| **CP-II.5** | `#100` | **CF 1054H — Epic Convolution** | `2A#49` | Given arrays $a_i, b_j$ of length $\le 10^5$ and primitive $c \pmod{490019}$, compute $\sum_{i,j} a_i b_j c^{i^2 j^3} \pmod{490019}$. |
| **CP-II.6** | `#029` | **ABC 266 G — Yet Another RGB Sequence** | `2B#A5` | Count strings of $R$ `R`s, $G$ `G`s, $B$ `B`s ($\le 10^6$) containing exactly $K$ occurrences of substring `RG`. |
| **CP-II.7** | `#162` | **Luogu P4859 — 已经没有什么好害怕的了** | `2B#A9` | Given two arrays $A, B$ of length $n \le 2000$, count pairings with exactly $k$ pairs satisfying $A_i > B_{\pi(i)}$. |
| **CP-II.8** | `#141` | **Luogu P2290 / P4430 — 树的计数 / 猴猴吃香蕉** | `1B#7` | Given prescribed vertex degrees $d_1, \dots, d_n$ on $n \le 10^5$ labeled vertices, count the number of distinct labeled trees. |

#### Stage 2: Diagnostic Routing & Algebraic Solution Key (Collapsible)

<details>
<summary><strong>Click to Reveal CP-II Diagnostic Routing & Algebraic Reduction Key (Verified Prereqs &le; Ch 08)</strong></summary>

| Slot | Pool ID | Target Home Chapter & Section | Diagnostic Trigger & Algebraic Reduction |
| :-: | :-: | :--- | :--- |
| **CP-II.1** | `#085` | **Ch 06 (6.1 Bounded Composition $\prod(1-x^{f_i+1})(1-x)^{-n}$)** | Expand the $2^n$ numerator terms of $\prod_{i=1}^n (1 - x^{f_i+1})$ and pair each with $[x^{s-d}](1-x)^{-n} = \binom{s-d+n-1}{n-1}$ in $O(n 2^n)$. |
| **CP-II.2** | `#152` | **Ch 06 (6.4 Stirling Numbers of the Second Kind Row-Sum via NTT)** | Substitute $j! \left\{\begin{smallmatrix} i \\ j \end{smallmatrix}\right\} = \sum_{k=0}^j (-1)^{j-k}\binom{j}{k} k^i$, swap sums over $i$, and evaluate the resulting Cauchy convolution via a single NTT. |
| **CP-II.3** | `#251` | **Ch 06 (6.1 Unique Split-Point Vandermonde Convolution Identity)** | Count completions around the unique split index where prefix '(' count equals suffix ')' count and collapse via Vandermonde $\sum_k \binom{a}{k}\binom{b}{c-k} = \binom{a+b}{c}$. |
| **CP-II.4** | `#252` | **Ch 06 (6.3/6.4 $O(k)$ Consecutive Lagrange Interpolation)** | Sieve $i^k$ on $0, 1, \dots, k+1$ in $O(k)$ time and evaluate the degree-$(k+1)$ polynomial $S_k(n)$ at $n$ using prefix/suffix factorial products. |
| **CP-II.5** | `#100` | **Ch 07 (7.3 2D Index-Calculus & Mixed-Radix Chirp-$Z$ Transform)** | Reduce exponents $i^2 j^3 \bmod (p-1)$ via CRT over $490018 = 2 \times 491 \times 499$ and apply Bluestein's identity $u v = \binom{u+v}{2} - \binom{u}{2} - \binom{v}{2}$. |
| **CP-II.6** | `#029` | **Ch 08 (8.1 Non-Overlapping Substring Inclusion–Exclusion)** | Contract $j \ge K$ chosen `RG` pairs into atomic tokens and apply Binomial Inversion $f_K = \sum_{j \ge K} (-1)^{j-K}\binom{j}{K} g_j$. |
| **CP-II.7** | `#162` | **Ch 08 (8.1 Sort-and-DP Rook Polynomial + Binomial Inversion)** | Sort $A, B$ so domination thresholds are monotone, compute the rook polynomial $g_j$ in $O(n^2)$, and recover $f_k$ via Binomial Inversion. |
| **CP-II.8** | `#141` | **Ch 04 (4.4 Prüfer Sequence Degree-Distribution EGF)** | Map each vertex $v$ of degree $d_v$ to Prüfer multiplicity $d_v - 1$, yielding $[x^{n-2}] (n-2)! \prod_{i=1}^n \frac{x^{d_i-1}}{(d_i-1)!} = \frac{(n-2)!}{\prod (d_i-1)!}$. |

</details>


### CP-III: Blind Checkpoint for Part III — *Online Convolutions, Implicit Equations, Formal Residues & Graph Enumeration* (Ch 09–13)

**Diagnostic Brief**: Diagnose whether each functional equation is causal/self-referential (solved by $O(N \log^2 N)$ CDQ Divide-and-Conquer NTT or Online Relaxed Convolution), contractive for all coefficients up to $N$ (solved by $O(N \log N)$ Coupled Newton Iteration), asks for a single coefficient $[x^N] H(G(x))$ or mod-$p$ algebraic term (solved by Formal Residues / Lagrange Inversion / Char-$p$ LIF), or counts labeled graphs/trees via $2^{\binom{n}{2}}$ CZT and Matrix-Tree over FPS.

#### Stage 1: Spoiler-Free Blind Problem Arena (`8` Disjoint Problems)

| Slot | Pool ID | Problem ID & Title | Source Wave | Raw Constraint & Structural Cues (Spoiler-Free) |
| :-: | :-: | :--- | :-: | :--- |
| **CP-III.1** | `#090` | **CF 848E — Days of Floral Colours** | `5A#15` | Place dominoes of 3 types around a circle of $2n$ vertices ($n \le 5 \times 10^4$) and sum the product of segment lengths between symmetric pairs. |
| **CP-III.2** | `#131` | **CF 1906J — Count BFS Graphs** | `5B#A10` | Given a permutation $a_1, \dots, a_n$ ($n \le 5000$), count simple undirected graphs on $n$ vertices whose lexicographically smallest BFS order starting at $1$ is $a$. |
| **CP-III.3** | `#133` | **CF 1930I — Counting Is Fun** | `3B#24` | Given a binary string $p$ of length $n \le 10^5$, count binary strings $q$ such that every interval $[l,r]$ having a majority of $1$s in $q$ contains at least one $1$ in $p$. |
| **CP-III.4** | `#160` | **Luogu P4747 — [CERC2017] Intrinsic Interval** | `2B#B11` | Count simple (interval-indecomposable) permutations of length $k$ for all $k \le n \le 10^5$. |
| **CP-III.5** | `#119` | **CF 1528F — AmShZ Farm** | `3A#17` | Given $n \le 10^9$ and $k \le 10^5$, sum $(\text{score of } a)^k$ over all valid parking sequences $a_1, \dots, a_n \in [1, n]$. |
| **CP-III.6** | `#035` | **ABC 279 Ex — Sum of Prod of Min** | `4A#P10` | Given $N \le 2 \times 10^5$ and $M \le 2N$, compute $\sum_{A_1 + \dots + A_N = M, A_i \ge 1} \prod_{i=1}^N \min(i, A_i) \pmod{200003}$. |
| **CP-III.7** | `#205` | **Luogu P8555 — 密码学第三次小作业** | `3B#21` | Given huge $n \le 10^{18}$ and small prime modulus $p \le 10^5$, extract $[x^n]$ of a scale-invariant algebraic tree series $F(x) \pmod p$. |
| **CP-III.8** | `#163` | **Luogu P5206 — [WC2019] 数树** | `2B#B9` | Given $n \le 10^5$, $y$, and mode $op \in \{0,1,2\}$ (two given trees, one given tree, or zero given trees), compute $\sum_{T_1, T_2} y^{n - \lvert E(T_1) \cap E(T_2) \rvert}$. |

#### Stage 2: Diagnostic Routing & Algebraic Solution Key (Collapsible)

<details>
<summary><strong>Click to Reveal CP-III Diagnostic Routing & Algebraic Reduction Key (Verified Prereqs &le; Ch 13)</strong></summary>

| Slot | Pool ID | Target Home Chapter & Section | Diagnostic Trigger & Algebraic Reduction |
| :-: | :-: | :--- | :--- |
| **CP-III.1** | `#090` | **Ch 09 (9.1 Coupled $4 \times 4$ Matrix Divide-and-Conquer NTT / Rational System)** | Formulate the $4 \times 4$ parity/endpoint transfer matrix for symmetric domino segments and solve to degree $n$ via CDQ Divide-and-Conquer NTT. |
| **CP-III.2** | `#131` | **Ch 09 (9.1 Queue Interval Convolution) & Ch 13 (13.1 Graphical Factor)** | Track the BFS queue interval $[l, r]$ where $a_i < a_{i+1}$ forces monotone parent attachments and weight unconstrained edges by $2^{\text{free}}$. |
| **CP-III.3** | `#133` | **Ch 10 (10.2 Implicit Functional Equation & Newton Iteration)** | Decompose $0$-runs of $p$ via Dyck/Catalan prefix sums and solve the resulting implicit functional equation via Newton / CDQ convolution. |
| **CP-III.4** | `#160` | **Ch 10 (10.2 Substitution Inversion for Simple Permutations)** | Write the substitution decomposition of all permutations in terms of simple permutations and invert via implicit Newton iteration. |
| **CP-III.5** | `#119` | **Ch 11 (11.3 Raney's Cycle Lemma & Circular Parking Orbit)** | Lift linear parking sequences to a circle of size $n+1$ (Raney's Lemma probability $1/(n+1)$) and expand $x^k$ in the Stirling / falling-factorial basis. |
| **CP-III.6** | `#035` | **Ch 03 (3.2 Sparse Product Decomposition) & Ch 09 (9.1 Product Tree)** | Rewrite each factor as $\frac{1 - (i+1)x^i + i x^{i+1}}{(1-x)^2}$, multiply the degree-bounded trinomials via divide-and-conquer, and extract $[x^{M-N}]$. |
| **CP-III.7** | `#205` | **Ch 11 (11.4 Algebraic Series Mod Small Prime $p$ via Char-$p$ LIF)** | Use Frobenius linearity $(A(x))^p \equiv A(x^p) \pmod p$ and base-$p$ digit extraction (Lucas/Frobenius system) to compute $[x^n] F(x)$ in $O(p \log p \log_p n)$. |
| **CP-III.8** | `#163` | **Ch 13 (13.4 Tree Intersection EGF $\exp(\frac{n^2 y}{1-y}T(x))$ & Matrix-Tree)** | Expand edge intersection via subset inclusion–exclusion $(1 + (y^{-1}-1))^k$, weight each component of size $s$ by $s$ or $s^2$, and apply $\exp$ on the rooted tree series. |

</details>


### CP-IV: Blind Checkpoint for Part IV — *Stochastic Processes, Lattice Walks, Multivariate Diagonals & Kernel Method* (Ch 14–17)

**Diagnostic Brief**: Diagnose whether a stochastic or multivariate problem calls for PGF stopping-time / renewal / martingale expansion at $x=1+t$, 1D bounded lattice walks & the Kernel Method $K(t, u_0(t)) = 0$, bivariate rational diagonals $[x^n y^n] P/Q$ via 2D Bostan–Mori or Furstenberg's algebraic residue reduction, or implicit tree / kernel root elimination via Lagrange Inversion.

#### Stage 1: Spoiler-Free Blind Problem Arena (`8` Disjoint Problems)

| Slot | Pool ID | Problem ID & Title | Source Wave | Raw Constraint & Structural Cues (Spoiler-Free) |
| :-: | :-: | :--- | :-: | :--- |
| **CP-IV.1** | `#158` | **Luogu P4707 — 重返现世** | `2B#E5` | Given $n \le 1000$ items with probabilities $p_i/M$ ($\sum p_i = M \le 10^4$), find the expected time until at least $k$ distinct items appear. |
| **CP-IV.2** | `#169` | **Luogu P5326 — [ZJOI2019] 开关** | `2B#E10` | Given $n$ switches ($\sum p_i \le 5\times 10^4$), find the expected number of toggles to reach target states $s_i \in \{0,1\}$. |
| **CP-IV.3** | `#099` | **CF 1025G — Company Acquisitions** | `2B#E14` | Given $n \le 500$ companies in an active/vassal forest where each step randomly pairs two active roots and resets the loser's vassals, find the expected steps until $1$ root remains. |
| **CP-IV.4** | `#116` | **CF 1479E — School Clubs** | `2B#E15` | Given $m \le 1000$ club sizes $a_i$ ($\sum a_i = n \le 10^9$) where each day a random student either switches to a club with probability $a_j/n$ or forms a new club, find the expected days until all students are in one club. |
| **CP-IV.5** | `#194` | **Luogu P6633 — [ZJOI2020] 抽卡** | `3B#8` | Given a set $S$ of $n \le 2 \times 10^5$ integers and uniform random draws with replacement from $S$, find the expected draws until $k$ consecutive integers have been collected. |
| **CP-IV.6** | `#058` | **ARC 136 F — Flip Cells** | `2A#11` | Flip $H \times W$ ($HW \le 50$) grid cells to reach target row parity states and transition count; extract the exact multi-parameter expectation. |
| **CP-IV.7** | `#243` | **yukicoder 2104 — Fuss–Catalan Diagonal** | `4B#25` | Given an asymmetric rational bivariate series $P(x,y)/Q(x,y)$ and $(p,q)$, extract the asymmetric diagonal $[x^{pn} y^{qn}] \frac{P(x,y)}{Q(x,y)}$ for $n \le 10^5$. |
| **CP-IV.8** | `#082` | **Toyota 2023 Spring Final E — Replace Digits / Tree Constraint** | `3A#16` | Given a constrained digit-replacement / tree-structured operation process of size $n \le 2 \times 10^5$, extract the target configuration count via implicit root elimination. |

#### Stage 2: Diagnostic Routing & Algebraic Solution Key (Collapsible)

<details>
<summary><strong>Click to Reveal CP-IV Diagnostic Routing & Algebraic Reduction Key (Verified Prereqs &le; Ch 17)</strong></summary>

| Slot | Pool ID | Target Home Chapter & Section | Diagnostic Trigger & Algebraic Reduction |
| :-: | :-: | :--- | :--- |
| **CP-IV.1** | `#158` | **Ch 14 (14.4 $k$-th Min–Max Identity & Compressed Knapsack DP)** | Apply $\min_k(S) = \sum_{T} (-1)^{\lvert T\rvert - (n-k+1)}\binom{\lvert T\rvert - 1}{n-k}\min(T)$ and compress $\sum_{i \in T} p_i = s$ via $O(M(n-k))$ DP. |
| **CP-IV.2** | `#169` | **Ch 14 (14.2 Switching-Walk Renewal Equation $F = G / H$)** | Write the exponential parity walk $G(x)$ and return series $H(x)$, convert to ordinary PGFs via $[x^k/k!] \mapsto z^k$, and evaluate $\frac{d}{dz}(G/H)\big\rvert_{z=1}$ after clearing $(1-z)$. |
| **CP-IV.3** | `#099` | **Ch 14 (14.4 Optional Stopping Theorem & Martingale Potential)** | Construct the potential $\Phi = \sum_{\text{active } u} (2^{\text{vassals}(u)} - 1)$ whose expected increment per step is $+1$, yielding $E[T] = (2^{n-1}-1) - \Phi_0$. |
| **CP-IV.4** | `#116` | **Ch 14 (14.4 First-Order Homogeneous Martingale Difference Recurrence)** | Seek an additive potential $\sum f(a_i)$ satisfying $\mathbb{E}[\Delta \Phi] = -1$, which reduces to a homogeneous two-term recurrence for $\Delta f(s) = f(s+1)-f(s)$. |
| **CP-IV.5** | `#194` | **Ch 14 (14.3 Coupon Collector of Contiguous Runs via EGF + NTT)** | Decompose $S$ into maximal contiguous intervals, write the survival EGF for avoiding $k$ consecutive picks via $O(\ell/k)$ inclusion–exclusion, and multiply across intervals via NTT. |
| **CP-IV.6** | `#058` | **Ch 16 (16.3 Exponential Parity Walk & Bivariate Residue Extraction)** | Track parity transitions via bivariate EGF $\sinh/\cosh$ factors combined with switching-PGF pole extraction. |
| **CP-IV.7** | `#243` | **Ch 16 (16.4 Asymmetric $(p, q)$-Diagonal via Furstenberg Residue)** | Represent $[x^{pn} y^{qn}] F(x,y) = [t^n] \operatorname{Res}_x \frac{1}{x} F(x, t x^{-p/q})$ and extract the algebraic root residues. |
| **CP-IV.8** | `#082` | **Ch 11 (11.2 Lagrange Inversion) & Ch 15 (15.3 Kernel Root Substitution)** | Formulate the implicit functional equation for valid replacement trees and extract $[x^n]$ via single-coefficient Lagrange Inversion. |

</details>


### CP-V: Blind Checkpoint for Part V — *D-Finite ODEs, Transposition Principle (`mulT`) & Fast Composition (`Kinoshita–Li`)* (Ch 18–21)

**Diagnostic Brief**: Diagnose whether a problem requires compiling an algebraic/combinatorial specification into an $O(N)$ P-recursive recurrence or coupled ODE, applying WZ / hypergeometric absorption, reversing a linear signal-flow graph via Tellegen's `mulT` (transposed subproduct trees, Monge/tree history D&C, or subtree size rerooting), or running Kinoshita–Li $O(N \log^2 N)$ fast composition / power projection.

#### Stage 1: Spoiler-Free Blind Problem Arena (`8` Disjoint Problems)

| Slot | Pool ID | Problem ID & Title | Source Wave | Raw Constraint & Structural Cues (Spoiler-Free) |
| :-: | :-: | :--- | :-: | :--- |
| **CP-V.1** | `#236` | **yukicoder 963 — 門松列列 2** | `5A#9` | Count permutations of length $N \le 10^5$ (or kadomatsu-constrained alternating sequences) satisfying coupled local up/down step relations. |
| **CP-V.2** | `#108` | **CF 1264D2 — Beautiful Bracket Sequence (Hard)** | `4A#P12` | Given a bracket string $s$ of `(`, `)`, and `?` of length $\lvert s \rvert \le 10^6$, sum the maximum matched nested depth over all completions in $O(\lvert s \rvert)$ time. |
| **CP-V.3** | `#130` | **CF 1842I — Tenzing and Necklace** | `5B#B17` | Cut a circular necklace of $n \le 5 \times 10^5$ beads into $k$ intervals of length $\le m$ to minimize cut cost using circular Monge D&C + transposed convolution. |
| **CP-V.4** | `#135` | **CF 1988F — Heartbeat** | `5B#B15` | For every length $1 \le k \le n \le 700$ (or $5 \times 10^4$), sum the product of prefix-maximum count, suffix-maximum count, and adjacent-ascent weight over all permutations of length $k$. |
| **CP-V.5** | `#185` | **Luogu P5853 — Stirling & Falling Factorial Transpose** | `5B#B14` | Convert between falling-factorial, Stirling, and Vandermonde-evaluated polynomial bases of degree $n \le 10^5$ using transposed subproduct trees. |
| **CP-V.6** | `#215` | **UOJ 604 — [UR #20] 跳蚤电话** | `4A#P27` | Given a rooted tree on $n \le 10^5$ vertices generated by sequentially attaching nodes or subdividing edges, count valid construction histories via tree-structured transposed multipoint evaluation. |
| **CP-V.7** | `#061` | **ARC 138 F — KD-Tree** | `4A#P26` | Count valid interval-split / KD-tree sequences of length $n \le 2.5\times 10^5$ via power projection / compositional inverse. |
| **CP-V.8** | `#068` | **AGC 005 F — Many Easy Problems** | `1A#12` | Given a tree $T$ on $N \le 2 \times 10^5$ vertices, for every $k = 1, \dots, N$ compute the sum over all $\binom{N}{k}$ vertex subsets $S$ of the size of the minimal subtree spanning $S$. |

#### Stage 2: Diagnostic Routing & Algebraic Solution Key (Collapsible)

<details>
<summary><strong>Click to Reveal CP-V Diagnostic Routing & Algebraic Reduction Key (Verified Prereqs &le; Ch 21)</strong></summary>

| Slot | Pool ID | Target Home Chapter & Section | Diagnostic Trigger & Algebraic Reduction |
| :-: | :-: | :--- | :--- |
| **CP-V.1** | `#236` | **Ch 19 (19.2 Coupled First-Order / Riccati ODE Systems)** | Translate alternating permutation transitions into the coupled Riccati ODE system $S'(x) = 1 + S(x)^2, C'(x) = S(x)C(x)$ ($\sec x + \tan x$) and solve in $O(N \log N)$. |
| **CP-V.2** | `#108` | **Ch 06 (6.1 Vandermonde Absorption) & Ch 19 (19.3 Hypergeometric Summation)** | Apply the absorption identity $i \binom{A}{i} = A \binom{A-1}{i-1}$ to collapse the inner Vandermonde sum into two closed-form binomials evaluated in $O(\lvert s \rvert)$. |
| **CP-V.3** | `#130` | **Ch 20 (20.1 Tellegen Transposition `mulT` inside Circular Cut D&C)** | Combine randomized circular cut reduction and WQS / Monge divide-and-conquer with transposed convolution `mulT`. |
| **CP-V.4** | `#135` | **Ch 20 (20.1 Prefix-Suffix Maximum DP via Transposed Convolution `mulT`)** | Recognize the reverse-indexed binomial merge around the maximum element $k$ as an exact middle product $\operatorname{mulT}$. |
| **CP-V.5** | `#185` | **Ch 20 (20.2 Transposed Vandermonde & Stirling Basis Conversion)** | Run Tellegen's transposed remainder tree (`mulT` descending the subproduct tree) to convert between power and falling-factorial bases in $O(n \log^2 n)$. |
| **CP-V.6** | `#215` | **Ch 20 (20.2 Tree History DP via Transposed Multipoint Evaluation)** | Model subtree growth histories as rational fractions and evaluate via transposed subproduct tree divide-and-conquer. |
| **CP-V.7** | `#061` | **Ch 21 (21.1 Kinoshita–Li $O(N \log^2 N)$ Fast Composition & Power Projection)** | Reduce the recursion to dense polynomial composition $G(F(x)) \bmod x^N$ and solve via Kinoshita–Li 2D Bostan–Mori transposition. |
| **CP-V.8** | `#068` | **Ch 20 (20.1 Tellegen Transposition Principle & Reverse-Indexed `mulT`)** | By linearity of expectation over edges, express $\text{ans}_k = N\binom{N}{k} - \sum_{s=1}^{N-1} \text{cnt}_s \binom{s}{k}$ and evaluate for all $k$ in a single middle product `mulT`. |

</details>


### CP-VI: Blind Checkpoint for Part VI — *Structural Extensions: Tree DP + FPS, $q$-Series & Bitwise / Dirichlet Algebras* (Ch 22–24)

**Diagnostic Brief**: Diagnose across Heavy-Light Spine D&C / Static Top Trees / dynamic FWT zero-divisor pairs $(a,c)=a\cdot 0^c$ on trees, Gaussian $q$-binomials $\begin{bmatrix} n \\ k \end{bmatrix}_q$ & $q$-difference equations over $\mathbb{F}_q$, Bitwise FWT/SOS, Set Power Series $\mathcal{R}_n = K[x_1,\dots,x_n]/(x_i^2)$ ($O(n^2 2^n)$ $\ln/\exp$), and Dirichlet Generating Functions $\mathcal{D}_f(s)$.

#### Stage 1: Spoiler-Free Blind Problem Arena (`8` Disjoint Problems)

| Slot | Pool ID | Problem ID & Title | Source Wave | Raw Constraint & Structural Cues (Spoiler-Free) |
| :-: | :-: | :--- | :-: | :--- |
| **CP-VI.1** | `#102` | **CF 1097G — Vladislav and a Great Legend** | `2A#28` | Given a tree on $n \le 10^5$ vertices and exponent $k \le 200$, compute $\sum_{\emptyset \neq S \subseteq V} (\text{steiner}(S))^k$. |
| **CP-VI.2** | `#121` | **CF 1553I — Stairs** | `4A#P16` | Given stair-length constraints on a sequence of length $n \le 10^5$, count valid stair partitions via $2 \times 2$ polynomial matrix divide-and-conquer. |
| **CP-VI.3** | `#117` | **CF 1510H — Hard Optimization** | `5B#A12` | Given a tree on $n \le 2000$ vertices with interval weights, merge heavy-path polynomial DP states. |
| **CP-VI.4** | `#170` | **Luogu P5327 — [ZJOI2019] 语言** | `5B#A18` | Given $m \le 10^5$ paths on a tree of size $n \le 10^5$, count connected path unions via tree DP + HLD decomposition. |
| **CP-VI.5** | `#054` | **ARC 106 E — Medals** | `2A#35` | Given $N \le 18$ employees with work/rest schedules and $K \le 10^5$ medals required per employee, find the minimum total days $D$ needed to award all $NK$ medals. |
| **CP-VI.6** | `#254` | **UOJ 310 — [UNR #2] 黎明前的巧克力** | `5B#F2` | Given $n \le 10^6$ integers $a_i < 2^{20}$, count pairs of disjoint subsets with equal XOR sum. |
| **CP-VI.7** | `#175` | **Luogu P5406 — [THUPC2019] 找树** | `4A#P8` | Given a graph on $n \le 70$ vertices where each edge has a $w \le 12$-bit integer weight and each bit uses AND, OR, or XOR, find the maximum bitwise weight of a spanning tree. |
| **CP-VI.8** | `#180` | **Luogu P5643 — [PKUWC2018] 随机游走** | `2B#E16` | Given a tree on $n \le 18$ vertices and $Q \le 5000$ queries of vertex subsets $S$, find the expected steps for a random walk from $x$ to visit every vertex in $S$. |

#### Stage 2: Diagnostic Routing & Algebraic Solution Key (Collapsible)

<details>
<summary><strong>Click to Reveal CP-VI Diagnostic Routing & Algebraic Reduction Key (Verified Prereqs &le; Ch 24)</strong></summary>

| Slot | Pool ID | Target Home Chapter & Section | Diagnostic Trigger & Algebraic Reduction |
| :-: | :-: | :--- | :--- |
| **CP-VI.1** | `#102` | **Ch 22 (22.1 Edge-Subset Stirling Expansion $x^k = \sum S(k,j)\binom{x}{j}j!$ on Trees)** | Expand $x^k = \sum_{j=0}^k \left\{\begin{smallmatrix} k \\ j \end{smallmatrix}\right\} j! \binom{x}{j}$ to convert the $k$-th power of induced Steiner size into a degree-$k$ polynomial tree DP. |
| **CP-VI.2** | `#121` | **Ch 22 (22.2 $2 \times 2$ Polynomial Matrix Block-Merging D&C)** | Compress contiguous stair runs into blocks and multiply $2 \times 2$ boundary-state polynomial transition matrices along a balanced divide-and-conquer tree. |
| **CP-VI.3** | `#117` | **Ch 22 (22.1 Tree Interval Covering DP + Minkowskian / FPS Merge)** | Combine heavy-light chain decomposition with convex/polynomial state merging across subtrees. |
| **CP-VI.4** | `#170` | **Ch 22 (22.2 Tree Path Union Maintenance + HLD Decomposition)** | Maintain connected spanning subtrees of active paths along heavy-light chains via divide-and-conquer merge. |
| **CP-VI.5** | `#054` | **Ch 24 (24.1 Fast Zeta / SOS Subset Transform & Hall's Marriage Theorem)** | Binary search on $D$ and verify Hall's condition $\lvert U(S) \rvert \ge K \lvert S \rvert$ for all $2^N$ subsets $S$ using $O(N 2^N)$ Fast Zeta Transform (SOS DP). |
| **CP-VI.6** | `#254` | **Ch 24 (24.1 Small-Support Bitwise XOR FWT Eigenvalue Trick $\prod(1 + 2x^{a_i})$)** | In the XOR group ring, each factor $(1 + 2x^{a_i})$ has Walsh eigenvalues $1 + 2(-1)^{\operatorname{popcount}(k \ \& \ a_i)} \in \{-1, 3\}$; count frequencies via forward FWT, take powers of $3$ and $-1$, and apply IFWT in $O(b 2^b)$. |
| **CP-VI.7** | `#175` | **Ch 24 (24.1 Mixed Bitwise FWT (AND/OR/XOR) inside Matrix-Tree Determinant)** | Apply the mixed $2^w$-point FWT to every entry of the $(n-1)\times(n-1)$ Laplacian, compute $2^w$ scalar determinants in $O(2^w n^3)$, and apply IFWT. |
| **CP-VI.8** | `#180` | **Ch 24 (24.1 Tree Random Walk Elimination + SOS Subset Sum + Min–Max IE)** | For each mask $T \subseteq V$, compute first-hit time $\min(T)$ in $O(n)$ via tree Gaussian elimination $E_u = A_u E_{fa(u)} + B_u$, then apply Min–Max IE via SOS Zeta transform. |

</details>

---

## 4. Grandmaster Multi-Chapter Synthesis Reserve (`Syn-01`–`Syn-14`) & Multi-Resolution "Revisited" Index

### 4.1 Disjoint Grandmaster Multi-Chapter Synthesis Reserve (`14` Problems)

> **Purpose**: These `14` problems (`Syn-01`–`Syn-14`) are 100% disjoint from the `192` chapter ladder problems and the `48` Part-end Checkpoint problems (`192 + 48 + 14 = 254`). Each problem bridges 3 or more distinct chapters across multiple Parts and serves as an end-of-book Grandmaster Capstone exercise.

| Reserve Slot | Pool ID | Problem ID & Title | Source Wave | Multi-Chapter Synthesis Architecture & Algebraic Pipeline |
| :-: | :-: | :--- | :-: | :--- |
| **Syn-01** | `#006` | **`fps_24_k` — Permutation** | `1A#4` | Ch 01 (Newton `inv`) $\times$ Ch 04 (Derangement EGF) $\times$ Ch 08 (Cluster IE) |
| **Syn-02** | `#014` | **`fps_24_t` — Colorful** | `1A#22` | Ch 03 (Cycle Index) $\times$ Ch 04 (Cycle-Parity EGF) $\times$ Ch 08 (Smirnov Word IE) |
| **Syn-03** | `#051` | **ARC 093 F — Dark Horse** | `2B#C2` | Ch 08 (Poset IE) $\times$ Ch 22 (Tree/Subtree Merging) $\times$ Ch 24 (SOS Subset Convolution) |
| **Syn-04** | `#087` | **CF 623E — Transforming Sequence** | `1B#23` | Ch 04 (Binomial EGF) $\times$ Ch 06 (Geometric Taylor Shift) $\times$ Ch 23 ($q$-Binomial Doubling) |
| **Syn-05** | `#106` | **CF 1228E — Another Filling the Grid** | `2B#A8` | Ch 06 (Binomial Sums) $\times$ Ch 08 (2D Bipartite IE) $\times$ Ch 16 (Bivariate Series) |
| **Syn-06** | `#112` | **CF 1342E — Placing Rooks** | `2A#22` | Ch 04 (Set Partition EGF $\exp$) $\times$ Ch 06 (Stirling S2 Row Extraction) $\times$ Ch 08 (Rook Polynomials) |
| **Syn-07** | `#142` | **Luogu P3311 — [SDOI2014] 数数** | `2B#D3` | Ch 05 (Rational Transfer Matrix) $\times$ Ch 08 (Goulden–Jackson Multi-Pattern Avoidance) |
| **Syn-08** | `#171` | **Luogu P5339 — [TJOI2019] 唱、跳、rap和篮球** | `2B#B5` | Ch 01 (D&C Convolution) $\times$ Ch 04 (Bounded EGF) $\times$ Ch 08 (Forbidden Block IE) |
| **Syn-09** | `#173` | **Luogu P5400 — [CTS2019] 随机立方体** | `2B#A10` | Ch 06 (Binomial Inversion) $\times$ Ch 08 (3D Poset IE) $\times$ Ch 14 (Probabilistic Stopping) |
| **Syn-10** | `#182` | **Luogu P5824 — 十二重计数法** | `1A#25` | Ch 01 (Polynomial `inv`) $\times$ Ch 03 (Partitions & Pentagonal OGF) $\times$ Ch 04 (EGF $\exp$) $\times$ Ch 06 (Stirling $S_2$) |
| **Syn-11** | `#172` | **Luogu P5366 — [SNOI2017] 遗失的答案** | `5B#E5` | Ch 08 (GCD/LCM Boundary Inclusion–Exclusion) $\times$ Ch 23 (Prime-Exponent Divisor Lattice) $\times$ Ch 24 (Bitwise OR FWT / SOS Transform) |
| **Syn-12** | `#247` | **HDU 5855 — Less Time, More Profit** | `2A#9` | Ch 05 (Rational GF Optimization) $\times$ Ch 13 (Network Matrix / Graph Algebraic Reduction) |
| **Syn-13** | `#249` | **CSES 1112 — Required Substring** | `2B#D1` | Ch 05 (KMP Automaton OGF) $\times$ Ch 08 (Goulden–Jackson Avoidance) $\times$ Ch 14 (Stopping-Time PGF) |
| **Syn-14** | `#253` | **CF 961G — Partitions** | `2A#25` | Ch 04 (EGF $\exp$) $\times$ Ch 06 (Stirling S2 Linear Decomposition) $\times$ Ch 14 (Linearity of Expectation) |

### 4.2 Multi-Resolution "Revisited" Index (`12` Landmark Cross-Chapter Threads)

> **Pedagogical Design**: Each of the `12` landmark problems below occupies **exactly one** primary slot in the `254`-problem bijection (shown in the *Primary Home Slot* column) and is explicitly revisited in later chapters to demonstrate how escalating the algebraic operator (e.g., Quadratic Radical $\to$ CDQ NTT $\to$ Implicit Newton, or Lagrange Inversion $\to$ D-Finite ODE $\to$ All-$n$ `revert`) transforms the asymptotic runtime or structural generality.

| # | Pool ID | Problem ID & Title | Primary Home Slot | Later "Revisited" Chapters & Comparative Pedagogical Payoff |
| :-: | :-: | :--- | :--- | :--- |
| **1** | `#084` | **CF 438E — The Child and Binary Tree** | **Ch 02 `Adv-2`** | **Ch 02** (Closed-form quadratic radical $\frac{2}{1+\sqrt{1-4xC(x)}}$ via `poly_sqrt` + `poly_inv`) $\to$ **Ch 09** (Causal $O(N \log^2 N)$ CDQ Divide-and-Conquer NTT without square roots) $\to$ **Ch 10** (General implicit Newton iteration $F_{k+1} = F_k - G(F_k)/G'(F_k)$). |
| **2** | `#021` | **ABC 222 H — Beautiful Binary Tree** | **Ch 09 `SS-2`** | **Ch 09** (Causal binary-tree recurrence via CDQ / Relaxed Convolution) $\to$ **Ch 11** (Single-coefficient $O(N \log N)$ Lagrange Inversion $[u^{n-1}]$) $\to$ **Ch 18** (Algebraic-to-D-Finite ODE compilation into an $O(N)$ 3-term P-recursive recurrence). |
| **3** | `#161` | **Luogu P4841 — [集训队作业2013] 城市规划** | **Ch 04 `Int-1`** | **Ch 04** (Labeled connected graphs $C(x) = \ln G(x)$ via EGF logarithm) $\to$ **Ch 07 / Ch 13** (Replacing $O(N)$ binomial precomputation with $2^{\binom{n}{2}}$ Bluestein Chirp-$Z$ Transform) $\to$ **Ch 09** (Semi-online CDQ / Relaxed Logarithm). |
| **4** | `#153` | **Luogu P4389 — 付公主的背包** | **Ch 03 `Int-1`** | **Ch 03** (Harmonic $O(M \log M)$ Euler Transform $\exp\left(\sum_v c_v \sum_k \frac{x^{kv}}{k}\right)$) $\to$ **Ch 09** (Online item arrival via Hoeven's Relaxed Exp). |
| **5** | `#226` | **LOJ 6538 — 烷基计数 加强版 加强版** | **Ch 10 `SS-2`** | **Ch 03** ($O(N^2)$ Pólya cycle index DP) $\to$ **Ch 09** ($O(N \log^2 N)$ Relaxed / CDQ Convolution with $A(x^2), A(x^3)$) $\to$ **Ch 10** ($O(N \log N)$ Burnside $S_3$ Newton iteration). |
| **6** | `#230` | **LOJ 6728 — U 群把妹王** | **Ch 18 `Mas-2`** | **Ch 12** (Single-$n$ $O(n \log n)$ Lagrange Inversion on pointed Block-Cut equation) $\to$ **Ch 18** (Algebraic-to-D-Finite ODE compilation & $O(N)$ P-recursive unrolling) $\to$ **Ch 21** (Simultaneous all-$n$ $O(N \log^2 N)$ Kinoshita–Li `revert`). |
| **7** | `#113` | **CF 1349D — Slime and Biscuits** | **Ch 14 `Mas-2`** | **Ch 05** (Rational OGF deconvolution) $\to$ **Ch 14** (PGF pole cancellation at $x=1$ & tridiagonal martingale potential recurrence). |
| **8** | `#074` | **AGC 058 D — Yet Another ABC String** | **Ch 16 `Adv-2`** | **Ch 08** (Goulden–Jackson forbidden-cluster inclusion–exclusion) $\to$ **Ch 16** (Trivariate rational diagonal $[x^A y^B z^C] \frac{1-xyz}{1-(x+y+z)+2xyz}$). |
| **9** | `#025` | **ABC 240 G — Teleporting Takahashi** | **Ch 16 `Int-1`** | **Ch 07** (Coordinate rotation $(u,v) = (x+y, x-y)$ decoupling 2D steps) $\to$ **Ch 16** (3D-to-1D $\times$ 2D decoupled multivariate coefficient extraction) $\to$ **Ch 18** (D-finite holonomic walk recurrence). |
| **10** | `#040` | **ABC 300 Ex — Fibonacci: Revisited** | **Ch 05 `Adv-1`** | **Ch 05** (3-sparse denominator $(1-x)Q(x) = 1-2x+x^{K+1}$ & $O(K \log K \log N)$ Bostan–Mori) $\to$ **Ch 07** (Roots of Unity Filter step inside parity splitting). |
| **11** | `#036` | **ABC 281 Ex — Alchemy** | **Ch 21 `SS-1`** | **Ch 06** (Falling-factorial EGF basis) $\to$ **Ch 11** (Single-$n$ Lagrange Inversion) $\to$ **Ch 21** (Simultaneous all-$n$ extraction via $O(N \log^2 N)$ Kinoshita–Li `compositional_inverse`). |
| **12** | `#068` | **AGC 005 F — Many Easy Problems** | **CP-V.8 ($\to$ Ch 20)** | **Ch 06** (Subtree size Vandermonde binomial sum) $\to$ **Ch 20** (Reverse-indexed Tellegen middle product `mulT`) $\to$ **Ch 22** (Tree rerooting & subtree frequency aggregation). |

---

## 5. Consolidated Quarantined Template Problems Table (`R-01`–`R-67`, 67 Rejected Templates)

> **Strict Anti-Template Quarantine Policy**: Every bare library-verification problem (e.g., Library Checker `inv`/`exp`/`log`/`sqrt`/`pow`, Luogu `【模板】` polynomial primitives, or trivial 1-line DP/ballot exercises) is excluded from all `192` Chapter Ladder slots, `48` Checkpoint slots, and `14` Synthesis Reserve slots. Instead, each of the `67` quarantined templates below is linked as an **Implementation Verification Footnote** in its corresponding Target Chapter (`Ch 01`–`Ch 24`) so readers can unit-test their library black boxes before tackling the combinatorial ladder.

| ID | Quarantined Template Problem ID, Title & Judge Link | Waves Quarantining It & Source Links | Target Ch | Pedagogical Quarantine Rationale | Recommended Non-Template Replacements in Accepted Corpus |
| :-: | :--- | :--- | :-: | :--- | :--- |
| **`R-01`** | **Luogu P3803** — *【模板】多项式乘法 (FFT)* ([Luogu](https://www.luogu.com.cn/problem/P3803)) | `1B#L1289`, `5B#L3067` | **Ch 01** | Pure polynomial multiplication $A(x)B(x)$ with zero combinatorial modeling or index transformation. | `CF 993E` (Prefix-sum difference cross-correlation), `Luogu P3338` ([ZJOI2014] 力) |
| **`R-02`** | **Library Checker** — *`convolution_mod` (Convolution $\bmod 998244353$)* ([LC](https://judge.yosupo.jp/problem/convolution_mod)) | `1B#L1289` | **Ch 01** | Raw NTT unit test; gives away that convolution is required without testing the 3-Question Convolution Litmus Test. | `Luogu P3338` ([ZJOI2014] 力), `CF 993E` (Nikita and Order Statistics), `AGC 001 E` (BBQ Hard) |
| **`R-03`** | **Library Checker / Luogu P4245** — *`convolution_mod_1000000007` / 【模板】任意模数多项式乘法 (MTT)* ([Luogu](https://www.luogu.com.cn/problem/P4245)) | `1B#L1289` | **Ch 01** | Tests 3-prime CRT / split-radix FFT precision mechanics in isolation without any generating function derivation. | `CF 623E` (Transforming Sequence $\pmod{10^9+7}$), `Luogu P5282` (快速阶乘算法) |
| **`R-04`** | **Luogu P4238 / Library Checker** — *【模板】多项式乘法逆 / `inv_of_formal_power_series`* ([Luogu](https://www.luogu.com.cn/problem/P4238)) | `1A#L1594`, `1A#L1601`, `1B#L1290`, `2B#L1461`, `4B#L1886`, `5A#L1684` | **Ch 01** | Directly asks for $F(x)^{-1} \pmod{x^n}$; skips the crucial `SEQ` operator modeling $F(x) = (1 - A(x))^{-1}$. | `AtCoder fps_24_k` (Indecomposable Permutations), `AGC 060 D` (Same Descent Set), `Luogu P6295` (Labeled DAGs) |
| **`R-05`** | **Luogu P4512 / Library Checker** — *【模板】多项式除法 / `division_of_polynomials`* ([Luogu](https://www.luogu.com.cn/problem/P4512)) | `1B#L1290` | **Ch 05** | Pure Euclidean quotient/remainder $A(x) = Q(x)B(x) + R(x)$ via reversal $x^n A(1/x)$ with no problem context. | `CF 1548C` (The Three Little Pigs), `QOJ #4815` (Bounded Strip Walk) |
| **`R-06`** | **Luogu P5205 / P5277 / Library Checker** — *【模板】多项式开根 / `sqrt_of_formal_power_series`* ([Luogu](https://www.luogu.com.cn/problem/P5205)) | `1A#L1597`, `1A#L1601`, `1B#L1293`, `5A#L1687` | **Ch 02** | Directly asks for $F(x)^{1/2} \pmod{x^n}$; completely hides the quadratic branch selection and $x \to 0$ pole cancellation pitfalls! | `CF 438E` (The Child and Binary Tree), `yukicoder 1080` (Generalized Delannoy Diagonal) |
| **`R-07`** | **Luogu P4717 / Library Checker** — *【模板】快速莫比乌斯/沃尔什变换 (FMT/FWT) / `bitwise_and_convolution`, `bitwise_xor_convolution`* ([Luogu](https://www.luogu.com.cn/problem/P4717)) | `1B#L1289`, `5B#L3064` | **Ch 24** | Explicitly names OR, AND, and XOR convolutions on given arrays $A, B$. | `Luogu P5406` ([THUPC2019] 找树), `CF 1336E2` (Chiori and Doll Picking), `ARC 139 F` |
| **`R-08`** | **Luogu P6097 / Library Checker** — *【模板】子集卷积 / `subset_convolution`* ([Luogu](https://www.luogu.com.cn/problem/P6097)) | `5B#L3064` | **Ch 24** | Raw ranked Zeta/Möbius transform verification without graph/hypergraph connectivity interpretation. | `ABC 213 G` (Connectivity 2), `CF 1326F2` (Wise Men), `UOJ #94` (胡策的统计) |
| **`R-09`** | **LOJ #150** — *挑战多项式 (Polynomial Challenge All-in-One Template)* ([LOJ #150](https://loj.ac/p/150)) | `3B#L1536` | **Ch 02** | Chains 8 arbitrary polynomial operations ($\sqrt{\cdot}, \exp, \ln, \arcsin$, power, derivative) in a synthetic expression. | `Luogu P5434` (有标号荒漠计数), `LOJ #6538` (烷基计数 加强版 加强版) |
| **`R-10`** | **Luogu P5264 / P5265** — *多项式三角函数 / 多项式反三角函数 ($\sin, \cos, \arcsin, \arctan$)* ([Luogu](https://www.luogu.com.cn/problem/P5264)) | `3B#L1536` | **Ch 02** | Artificial template testing $\frac{e^{iF} \pm e^{-iF}}{2}$ and $\int \frac{F'}{\sqrt{1-F^2}}$ without combinatorial meaning (unlike André's alternating permutations). | `yukicoder 963` (Kadomatsu Sequence 2 / André's ODE), `Luogu P5326` ([ZJOI2019] 开关) |
| **`R-11`** | **Library Checker** — *`product_of_polynomial_sequence`* ([LC](https://judge.yosupo.jp/problem/product_of_polynomial_sequence)) | `1B#L1289` | **Ch 01** | Directly asks for $\prod_{i=1}^n P_i(x)$ given the list of polynomials $P_i(x)$. | `CF 1613F` (Tree Coloring), `CF 1251F` (Red-White Fence), `ABC 260 Ex` (Colorfulness) |
| **`R-12`** | **Luogu P4725 / Library Checker** — *【模板】多项式对数函数 (多项式 ln) / `log_of_formal_power_series`* ([Luogu](https://www.luogu.com.cn/problem/P4725)) | `1A#L1596`, `1B#L1291`, `2B#L1462`, `3A#L1491`, `3B#L1536`, `5A#L1685`, `5B#L3068` | **Ch 02** | Computes $\int \frac{F'(x)}{F(x)}dx$ on a given array without teaching connected-component extraction $C(x) = \ln G(x)$ or Newton power sums. | `AtCoder fps_24_m` (Connected Labeled Graphs), `Luogu P7364` (Labeled Eulerian/Bipartite Graphs), `Luogu P4705` (玩游戏) |
| **`R-13`** | **Luogu P4726 / Library Checker** — *【模板】多项式指数函数 (多项式 exp) / `exp_of_formal_power_series`* ([Luogu](https://www.luogu.com.cn/problem/P4726)) | `1A#L1595`, `1B#L1291`, `2B#L1462`, `3A#L1491`, `3B#L1536`, `5A#L1686` | **Ch 02** | Computes $\exp(F(x))$ on raw input; omits the `SET` construction and the Euler Transform harmonic sieve $\exp(\sum \frac{A(x^k)}{k})$. | `AtCoder fps_24_l` (Permutation 2), `Luogu P4389` (付公主的背包), `LOJ #6503` (Magic) |
| **`R-14`** | **Luogu P5245 / P5273 / Library Checker** — *【模板】多项式快速幂 / `pow_of_formal_power_series`* ([Luogu](https://www.luogu.com.cn/problem/P5245)) | `1A#L1598`, `1B#L1292`, `3B#L1536`, `5A#L1688`, `5A#L1689` | **Ch 02** | Directly asks for $F(x)^k \pmod{x^n}$; spoils that the problem reduces to a polynomial power (such as via LIF or Prüfer codes). | `Luogu P5219` (Bounded Degree Trees), `ABC 303 Ex` (Constrained Tree Degree), `AtCoder fps_24_o` |
| **`R-15`** | **Library Checker** — *`inv_of_formal_power_series_sparse`* ([LC](https://judge.yosupo.jp/problem/inv_of_formal_power_series_sparse)) | `2B#L1473`, `5A#L1679` | **Ch 02** | Explicitly hands the coder a sparse polynomial with $K$ non-zero entries and asks for $F^{-1}$ in $O(NK)$. | `yukicoder 1939` (Numbered Colorful Balls), `AtCoder fps_24_g` (Coin) |
| **`R-16`** | **Library Checker** — *`sqrt_of_formal_power_series_sparse`* ([LC](https://judge.yosupo.jp/problem/sqrt_of_formal_power_series_sparse)) | `5A#L1682` | **Ch 02** | Explicitly hands a sparse polynomial for $O(NK)$ ODE square root without testing radical diagonal extraction. | `yukicoder 1080` (Generalized Delannoy Diagonal), `CF 755G` (PolandBall and Many Other Balls) |
| **`R-17`** | **Library Checker** — *`log_of_formal_power_series_sparse`* ([LC](https://judge.yosupo.jp/problem/log_of_formal_power_series_sparse)) | `5A#L1681` | **Ch 02** | Raw $O(NK)$ ODE logarithmic derivative check. | `yukicoder 1939` (Numbered Colorful Balls) |
| **`R-18`** | **Library Checker** — *`exp_of_formal_power_series_sparse`* ([LC](https://judge.yosupo.jp/problem/exp_of_formal_power_series_sparse)) | `5A#L1680` | **Ch 02** | Raw $O(NK)$ ODE exponential check $F' = P' F$. | `AGC 043 D` (Merge Triplets), `AtCoder fps_24_l` (Permutation 2) |
| **`R-19`** | **Library Checker** — *`pow_of_formal_power_series_sparse`* ([LC](https://judge.yosupo.jp/problem/pow_of_formal_power_series_sparse)) | `5A#L1683` | **Ch 02** | Raw $O(NK)$ ODE power recurrence $P G' = M P' G$. | `CF 1096G` (Lucky Tickets), `ABC 222 H` (Beautiful Binary Tree via trinomial power ODE) |
| **`R-20`** | **Luogu P5395 / Library Checker** — *第二类斯特林数·行 / `stirling_number_of_the_second_kind`* ([Luogu](https://www.luogu.com.cn/problem/P5395)) | `1B#L1296`, `2A#L748`, `2A#L749`, `2B#L1465` | **Ch 06** | Directly asks for row $n$ of $\left\{ \begin{matrix} n \\ k \end{matrix} \right\}$; doesn't test recognizing when to convert $i^n$ to falling factorials. | `CF 932E` (Team Work), `CF 1278F` (Cards), `CF 1097G` (Vladislav and a Great Legend) |
| **`R-21`** | **Luogu P5396 / Library Checker** — *第二类斯特林数·列 / `stirling_number_of_the_second_kind_fixed_k`* ([Luogu](https://www.luogu.com.cn/problem/P5396)) | `2A#L750`, `2A#L751`, `2B#L1466` | **Ch 06** | Directly asks for column $k$ of $\left\{ \begin{matrix} n \\ k \end{matrix} \right\} = \frac{n!}{k!}[x^n](e^x - 1)^k$. | `CF 623E` (Transforming Sequence), `Luogu P4859` (已经没有什么好害怕的了) |
| **`R-22`** | **Luogu P5408 / Library Checker** — *第一类斯特林数·行 / `stirling_number_of_the_first_kind`* ([Luogu](https://www.luogu.com.cn/problem/P5408)) | `2A#L744`, `2A#L745`, `2B#L1465` | **Ch 06** | Directly asks for $x^{\overline{n}} = \prod_{k=0}^{n-1}(x+k)$; spoils the Rényi–Foata record-to-cycle bijection! | `CF 960G` (Bandit Blues), `CF 1528F` (AmShZ Farm) |
| **`R-23`** | **Luogu P5409 / Library Checker** — *第一类斯特林数·列 / `stirling_number_of_the_first_kind_fixed_k`* ([Luogu](https://www.luogu.com.cn/problem/P5409)) | `2A#L746`, `2A#L747`, `2B#L1466` | **Ch 06** | Directly asks for $\frac{n!}{k!}[x^n]\left(\ln\frac{1}{1-x}\right)^k$. | `AtCoder fps_24_l` (Permutation 2) |
| **`R-24`** | **Luogu P5748 / Library Checker** — *集合划分计数 (Bell Numbers) / `bell_number`* ([Luogu](https://www.luogu.com.cn/problem/P5748)) | `5B#L3058` | **Ch 04** | Directly asks for $\exp(e^x - 1) \pmod{x^{n+1}}$ without modeling equivalence relations. | `AtCoder fps_24_d` (Sequence 2), `CF 840C` (On the Bench) |
| **`R-25`** | **Library Checker** — *`partition_function` (Pure Unrestricted Partition Template)* ([LC](https://judge.yosupo.jp/problem/partition_function)) | `1A#L1602` | **Ch 03** | Directly asks for $\prod_{k \ge 1}(1-x^k)^{-1}$ via Pentagonal Number Theorem with no modeling. | `Luogu P6189` ([NOI Online #1] 跑步 — Durfee Square / $\sqrt{N}$ Split), `LOJ #6089` (小 Y 的背包计数问题), `ABC 279 Ex` |
| **`R-26`** | **Luogu P5050 / Library Checker** — *【模板】多项式多点求值 / `multipoint_evaluation`* ([Luogu](https://www.luogu.com.cn/problem/P5050)) | `5B#L3052`, `5B#L3053` | **Ch 20** | Raw subproduct tree remainder evaluation $P(x_i)$ with no transposition or combinatorial context. | `UOJ #182` (`a^-1 + b` problem), `Luogu P5282` (快速阶乘算法) |
| **`R-27`** | **Luogu P5158 / Library Checker** — *【模板】多项式快速插值 / `polynomial_interpolation`* ([Luogu](https://www.luogu.com.cn/problem/P5158)) | `5B#L3052` | **Ch 20** | Raw Lagrange interpolation from arbitrary $(x_i, y_i)$. | `CF 995F` (Cowmpany Cowmpensation), `Luogu P7116` ([NOIP2020] 微信步数) |
| **`R-28`** | **Luogu P5393 / P5394** — *下降幂多项式乘法 / 【模板】下降幂多项式乘法* ([Luogu](https://www.luogu.com.cn/problem/P5393)) | `2A#L742`, `2A#L743` | **Ch 06** | Explicitly asks to multiply polynomials in the $x^{\underline{k}}$ basis via EGF $e^x$. | `Luogu P4491` ([HAOI2018] 染色), `CF 932E` (Team Work) |
| **`R-29`** | **Library Checker** — *`polynomial_taylor_shift` ($F(x+c)$)* ([LC](https://judge.yosupo.jp/problem/polynomial_taylor_shift)) | `1B#L1295`, `2A#L741`, `2B#L1460`, `4A#L1375`, `4B#L1885` | **Ch 06** | Directly asks for $F(x+c)$; spoils that exact-$k$ Inclusion-Exclusion is simply $A(x) = G(x-1)$ and eigen-basis diagonalization is $P(x \pm 1)$! | `Luogu P4491` ([HAOI2018] 染色), `ABC 260 Ex` (Colorfulness), `CF 923E` (Perpetual Subtraction) |
| **`R-30`** | **Luogu P5667 / Library Checker** — *拉格朗日插值2 (连续点值平移) / `shift_of_sampling_points_of_polynomial`* ([Luogu](https://www.luogu.com.cn/problem/P5667)) | `4A#L1376`, `5B#L3061`, `5B#L3062` | **Ch 20** | Directly gives $f(0), \dots, f(d)$ and asks for $f(c), \dots, f(c+d)$. | `Luogu P5282 / LOJ #161` (快速阶乘算法), `ARC 033 D` |
| **`R-31`** | **Luogu P6800 / Library Checker** — *【模板】Chirp Z-Transform / `multipoint_evaluation_on_geometric_sequence`* ([Luogu](https://www.luogu.com.cn/problem/P6800)) | `1B#L1297`, `5B#L3059`, `5B#L3060` | **Ch 07** | Directly asks for $P(a c^k)$ via Bluestein's identity $ij = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$. | `Luogu P5293` ([HNOI2019] 白兔之舞), `CF 1054H` (Epic Convolution), `Luogu P6295` (Labeled DAGs) |
| **`R-32`** | **Luogu P5808 / P5809 / Library Checker** — *【模板】多项式复合逆 / `compositional_inverse_of_formal_power_series`* ([Luogu](https://www.luogu.com.cn/problem/P5809)) | `1A#L1600`, `2B#L1463`, `3A#L1488`, `3A#L1489`, `3B#L1533`, `3B#L1535`, `4B#L1875`, `4B#L1876`, `5B#L3057` | **Ch 21** | Directly asks for $G(x)$ such that $F(G(x)) = x$; hides how tree grammars, block-cut decompositions, or simple permutations reduce to compositional inversion. | `Luogu P4747` (Simple Permutations), `Luogu P5827` (Biconnected Graphs), `Luogu P5828` (2-Edge-Connected Graphs) |
| **`R-33`** | **Luogu P5373 / Library Checker** — *【模板】多项式复合函数 / `composition_of_formal_power_series`* ([Luogu](https://www.luogu.com.cn/problem/P5373)) | `1A#L1599`, `2B#L1463`, `3A#L1487`, `3B#L1534`, `3B#L1535`, `4B#L1877`, `4B#L1884`, `5B#L3056` | **Ch 21** | Directly asks for $G(F(x)) \pmod{x^N}$; skips the component-substitution modeling step. | `ABC 387 G` (Prime Cycles), `CF 1349F2` (Slime and Sequences Hard) |
| **`R-34`** | **Library Checker** — *`composition_of_formal_power_series_large`* ([LC](https://judge.yosupo.jp/problem/composition_of_formal_power_series_large)) | `2B#L1457`, `3B#L1534`, `4A#L1372`, `5B#L3054` | **Ch 21** | Benchmark for Kinoshita–Li $O(N \log^2 N)$ `compose` at $N = 2\cdot 10^5$. | `ABC 387 G` (Prime Cycles), `QOJ #8528 / ARC 138 F` |
| **`R-35`** | **Library Checker** — *`compositional_inverse_of_formal_power_series_large` & `power_projection_of_formal_power_series`* ([LC](https://judge.yosupo.jp/problem/compositional_inverse_of_formal_power_series_large)) | `2B#L1458`, `2B#L1459`, `3A#L1489`, `3B#L1533`, `4A#L1371`, `4A#L1373`, `4B#L1874`, `5B#L3055` | **Ch 21** | Benchmark for Power Projection + LIF `revert` at $N = 2\cdot 10^5$. | `Luogu P5827` (点双连通图计数), `Luogu P5828` (边双连通图计数), `ARC 154 F` (Dice Game) |
| **`R-36`** | **Luogu P5900 / P4841** — *Template-Only Usage of 无标号树计数 / 城市规划 in Higher Waves* ([Luogu](https://www.luogu.com.cn/problem/P5900)) | `3A#L1492`, `3B#L1541` | **Ch 10** | When treated as a bare 1-line $\ln G(x)$ or Euler transform call in Wave 3 without Otter's dissimilarity or degree constraints (covered in Wave 1A/1B/3B). | `Luogu P6598` (烷烃计数), `Luogu P5434` (有标号荒漠计数), `ABC 284 Ex` |
| **`R-37`** | **Luogu P6086** — *【模板】Prufer 序列* ([Luogu](https://www.luogu.com.cn/problem/P6086)) | `3A#L1490` | **Ch 04** | Pure constructive bijection between tree parent array and Prüfer array. | `Luogu P5219` (Bounded Max-Degree Labeled Trees), `CF 917D` (Stranger Trees) |
| **`R-38`** | **Luogu P6178 / Library Checker** — *【模板】Matrix-Tree 定理 / `counting_spanning_trees_directed`, `counting_spanning_trees_undirected`* ([Luogu](https://www.luogu.com.cn/problem/P6178)) | `3A#L1493` | **Ch 13** | Direct Laplacian determinant computation without multivariate polynomial edge weights or BEST Eulerian reduction. | `Luogu P5406` ([THUPC2019] 找树), `ABC 336 G` (16 Integers), `CF 917D` (Stranger Trees) |
| **`R-39`** | **Luogu P4723 / Library Checker** — *【模板】常系数齐次线性递推 / `kth_term_of_linearly_recurrent_sequence`* ([Luogu](https://www.luogu.com.cn/problem/P4723)) | `1B#L1294`, `2A#L752`, `2B#L1473`, `4A#L1367`, `4A#L1368` | **Ch 05** | Hands the coder the linear recurrence coefficients $c_1, \dots, c_k$ and asks for $a_N$; doesn't test deriving rational generating functions $P(x)/Q(x)$ from combinatorial walks or IE. | `CF 1117D` (Magic Gems), `ABC 300 Ex` (Fibonacci: Revisited), `AGC 013 E` (Placing Squares) |
| **`R-40`** | **Luogu P5487 (Pure BM Template Usage) / Library Checker** — *【模板】Berlekamp–Massey 算法 / `find_linear_recurrence`* ([LC](https://judge.yosupo.jp/problem/find_linear_recurrence)) | `2A#L752`, `4A#L1368` | **Ch 05** | Pure shortest LFSR synthesis on a given sequence $a_0, \dots, a_{2d}$. *(Note: `Luogu P5487` is accepted in Wave 4A ONLY for its second part — binomial moment sum $\sum \binom{f_n}{k}$ and bivariate diagonal extraction!)* | `Luogu P5487` (Part 2: Binomial Moment Sum $\sum \binom{f_n}{k}$), `UOJ #182` |
| **`R-41`** | **Luogu P7439 (Pure Recurrence Template) / Library Checker** — *【模板】常系数齐次线性递推 (加强版) / `consecutive_terms_of_linear_recurrent_sequence`* ([Luogu](https://www.luogu.com.cn/problem/P7439)) | `4A#L1369` | **Ch 05** | Directly asks for $a_M, a_{M+1}, \dots, a_{M+N-1}$ of a given linear recurrence via transposed Bostan–Mori. | `ABC 300 Ex` (Fibonacci: Revisited), `CF 755G` (PolandBall and Many Other Balls) |
| **`R-42`** | **Library Checker** — *`multivariate_convolution`* ([LC](https://judge.yosupo.jp/problem/multivariate_convolution)) | `4A#L1374` | **Ch 16** | Raw multidimensional truncated convolution $\pmod{(x_1^{n_1}, \dots, x_k^{n_k})}$ via radix-mixed grading $\chi(\mathbf{i})$. | `ABC 240 G` (Teleporting Takahashi), `AGC 058 D` (Yet Another ABC String) |
| **`R-43`** | **Library Checker** — *`multivariate_convolution_cyclic`* ([LC](https://judge.yosupo.jp/problem/multivariate_convolution_cyclic)) | `4A#L1374` | **Ch 16** | Raw multidimensional cyclic DFT $\pmod{(x_1^{n_1}-1, \dots, x_k^{n_k}-1)}$. | `CF 1054H` (Epic Convolution), `Luogu P3702` ([SDOI2017] 序列计数) |
| **`R-44`** | **Codeforces 632E / Pure Subset-Sum Power Template** — *Thief in a Shop* ([CF 632E](https://codeforces.com/problemset/problem/632/E)) | `3B#L1540`, `4A#L1377` | **Ch 01** | Unweighted boolean knapsack $P(x)^k$ solvable by $O(NK)$ BFS or basic binary-exponentiation FFT without bivariate or implicit structure. | `CF 1096G` (Lucky Tickets — in Wave 5A), `ABC 222 H` (Beautiful Binary Tree) |
| **`R-45`** | **Luogu P4721** — *【模板】分治 FFT (CDQ Divide-and-Conquer FFT)* ([Luogu](https://www.luogu.com.cn/problem/P4721)) | `2B#L1464`, `3B#L1536`, `5A#L1678` | **Ch 09** | Explicitly gives $f_n = \sum_{i=1}^n f_{n-i} g_i$ (which is actually solvable in $O(N \log N)$ via $(1-G(x))^{-1}$!) and asks for CDQ FFT. Fails to show *when* CDQ FFT is genuinely needed over Newton inversion! | `CF 553E` (Kyoya and Train — outer $\min$ prevents $(1-G)^{-1}$!), `ARC 138 E` (Non-autonomous scaling), `ABC 213 Ex` (Stroll) |
| **`R-46`** | **Codeforces 1264D2 (When Used as 1-Line Vandermonde Identity in Wave 4B)** | `4B#L1883` | **Ch 06** | In Wave 4B (Kernel Method), `CF 1264D2` is rejected because it collapses to a 1-line Vandermonde sum without boundary reflections (it is placed in Wave 4A/5B instead). | `Luogu P6672` (你的生命已如风中残烛), `CF 1810G` (The Maximum Prefix) |
| **`R-47`** | **AtCoder Educational DP Contest M (When Used in Wave 2B IE/PGF)** — *Candies* | `2B#L1468` | **Ch 01** | Basic sliding-window prefix sum DP (appropriate as a Stepping Stone in Wave 1B, but rejected in Wave 2B where $O(N/s)$ harmonic or multivariate IE is required). | `CF 451E` (Devu and Flowers), `ARC 028 D` (Busy Takahashi Store) |
| **`R-48`** | **Library Checker** — *`q_binomial_coefficient_prime_mod` (Pure Gaussian Binomial $\binom{n}{k}_q$ Verification)* ([LC](https://judge.yosupo.jp/problem/q_binomial_coefficient_prime_mod)) | `5B#L3063` | **Ch 23** | Directly asks for $\binom{n}{k}_q \pmod P$; skips linear-algebraic subspace counting over $\mathbb{F}_q$ and $q$-Pochhammer pentagonal inversion. | `CF 1603F` (October 18, 2017), `ABC 278 Ex` (make 1), `ARC 145 F` |
| **`R-49`** | **Luogu P6198 / Pure $(q;q)_n$ Exp/Ln Template** | `5B#L3063` | **Ch 23** | Raw $\exp\left(-\sum \frac{x^k}{k(1-q^k)}\right)$ template without graph or matrix rank modeling. | `ABC 278 Ex` (make 1), `ARC 139 F` (Many Xor Optimization Problems) |
| **`R-50`** | **Library Checker** — *`exp_of_set_power_series`* ([LC](https://judge.yosupo.jp/problem/exp_of_set_power_series)) | `5B#L3065` | **Ch 24** | Directly asks for $\exp_{\text{SPS}}(F)$ on a $2^N$ array; skips connected-to-general subgraph decomposition. | `ABC 213 G` (Connectivity 2), `LOJ #154` (集合划分计数), `ABC 253 Ex` (We Love Forest) |
| **`R-51`** | **Library Checker** — *`log_of_set_power_series` / `power_projection_of_set_power_series`* ([LC](https://judge.yosupo.jp/problem/power_projection_of_set_power_series)) | `5B#L3065` | **Ch 24** | Raw $O(N^2 2^N)$ ranked FMT logarithm / transposed composition check without graph orientation or biconnectivity context. | `ABC 306 Ex` (Balance Scale / DAG orientations), `UOJ #94` (胡策的统计) |
| **`R-52`** | **Luogu P5325** — *【模板】Min_25 筛 (Pure Multiplicative Prefix Sum Template)* ([Luogu](https://www.luogu.com.cn/problem/P5325)) | `5B#L2989` | **Ch 24** | Synthetic multiplicative function $f(p^k) = p^k(p^k - 1)$ designed purely to test Min_25 sieve mechanics. *(Note: Included in Wave 5B Cluster F only when paired with Bell series / Dirichlet $\exp_{\text{Dir}}$ and `ABC 288 Ex`!)* | `ABC 288 Ex` (A Nameless Counting Problem — Dirichlet / Euler Transform Bridge), `LOJ #6729` (幂数) |
| **`R-53`** | **CSES 1729 & CSES 1725** — *Stick Game & Dice Probability* ([CSES](https://cses.fi/problemset/task/1725)) | `2B#L1467` | **Ch 14** | Elementary $O(NK)$ game/probability DP requiring zero generating function algebra or PGF stopping-time analysis. | `AtCoder fps_24_q` (Dice), `ARC 154 F` (Dice Game) |
| **`R-54`** | **Codeforces 280C & Luogu P1291** — *Game on Tree & `[SHOI2002]` 百事世界杯之旅* ([CF 280C](https://codeforces.com/problemset/problem/280/C)) | `2B#L1469` | **Ch 14** | Introductory Linearity of Expectation $\sum 1/\text{depth}(u)$ and coupon collector $\sum n/i$ exercises requiring no PGF or Min-Max IE. | `CF 1392H` (ZS Shuffles Cards), `AGC 038 E` (Gachapon) |
| **`R-55`** | **UVa 10759 & HDU 4336** — *Dice Throwing & Card Collector* ([HDU 4336](https://acm.hdu.edu.cn/showproblem.php?pid=4336)) | `2B#L1470` | **Ch 14** | Naive $O(n^2)$ dice DP and $O(2^n)$ bitmask Min-Max IE; completely superseded by polynomial PGF knapsack DP. | `Luogu P4707` (重返现世), `UOJ #390` (百鸽笼) |
| **`R-56`** | **Luogu P3375 & SPOJ `SUBLEX`** — *`【模板】KMP` & Lexicographical Substring Search* ([Luogu](https://www.luogu.com.cn/problem/P3375)) | `2B#L1471` | **Ch 08** | Pure string-matching / suffix-automaton data structure templates with no Goulden–Jackson cluster GF or PGF renewal system. | `CSES 1112 / yukicoder 1810` (Goulden–Jackson Cluster OGF), `Luogu P4548` (歌唱王国) |
| **`R-57`** | **Standard Montmort Derangement Templates** — *$D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$* | `2B#L1472` | **Ch 08** | Single-constraint textbook derangement formula with no bivariate shift or cycle-length constraint. | `ABC 172 E` (NEQ), `AtCoder fps_24_l` (Permutation 2), `AGC 005 D` (~K Permutations) |
| **`R-58`** | **Standard Absorbing Markov Chain Gaussian Elimination Templates** — *$E_u = 1 + \sum P_{uv} E_v$* | `2B#L1474` | **Ch 14** | Generic $O(V^3)$ dense Gaussian elimination without tridiagonal potential deconvolution or PGF pole cancellation. | `CF 1349D` (Slime and Biscuits), `CF 1479E` (School Clubs), `Luogu P5643` (随机游走) |
| **`R-59`** | **Library Checker** — *`counting_eulerian_circuits`* ([LC](https://judge.yosupo.jp/problem/counting_eulerian_circuits)) | `3A#L1493` | **Ch 13** | Bare directed BEST Theorem determinant template on a given small graph without sequence/walk modeling. | `ABC 336 G` (16 Integers — De Bruijn Eulerian Tour + Good–Lagrange) |
| **`R-60`** | **CSES 1095** — *Exponentiation ($a^b \bmod 10^9+7$)* ([CSES](https://cses.fi/problemset/task/1095)) | `3A#L1494` | **Ch 01** | Trivial scalar modular binary exponentiation with zero FPS content. | `CF 156D` (Clues), `Luogu P5219` (无聊的水题 I) |
| **`R-61`** | **Luogu P7591** — *2021 CoE-II D (Bare LIF Verification)* ([Luogu](https://www.luogu.com.cn/problem/P7591)) | `3B#L1537` | **Ch 11** | Strictly dominated by its 4-subtask sequel `Luogu P7592` (`2021 CoE-II E: 数树`). | `Luogu P7592` (2021 CoE-II E: 数树), `Luogu P7438` ([AGM 2021] Tree) |
| **`R-62`** | **SPOJ `LARMY` / CSES 2064 / CSES 2187 / Luogu P1044** — *Bracket Sequences I & II / 栈* ([CSES](https://cses.fi/problemset/task/2064)) | `3B#L1538`, `3B#L1539`, `4B#L1878`, `4B#L1879` | **Ch 11** | Elementary 1-line Catalan number $\frac{1}{n+1}\binom{2n}{n}$ or 1-mirror reflection $\binom{2n-k}{n} - \binom{2n-k}{n-1}$ requiring no Kernel Method or Newton iteration. | `CF 1204E` (Natasha, Sasha and the Prefix Sums), `AGC 021 E` (Ball Eat Chameleons), `CF 1821F` (Timber) |
| **`R-63`** | **Codeforces 896D / AtCoder ABC 205 E / Luogu P1641** — *Nephren Runs a Cinema / White and Black Balls / `[SCOI2010]` 生成字符串* ([CF 896D](https://codeforces.com/problemset/problem/896/D)) | `4B#L1880`, `4B#L1881`, `4B#L1882` | **Ch 15** | Standard 1-mirror ballot reflection $\binom{n+m}{n} - \binom{n+m}{n+k+1}$ or direct Motzkin trinomial expansion without small-branch kernel elimination. | `AGC 021 E` (Ball Eat Chameleons), `Luogu P6672` (你的生命已如风中残烛), `yukicoder 1341` |
| **`R-64`** | **Yukicoder No. 2677 & SPOJ `FIBOSUM`** — *Simple Linear Recurrence & Matrix Exponentiation Templates* ([yukicoder](https://yukicoder.me/problems/no/2677)) | `4A#L1370`, `4A#L1379` | **Ch 05** | Fixed $2\times 2$ / $3\times 3$ matrix exponentiation exercises that do not exercise $O(d \log d \log N)$ Bostan–Mori parity splitting. | `ABC 300 Ex` (Fibonacci: Revisited), `CF 1117D` (Magic Gems) |
| **`R-65`** | **AtCoder ABC 130 E** — *Common Subsequence* ([AtCoder](https://atcoder.jp/contests/abc130/tasks/abc130_e)) | `4A#L1378` | **Ch 05** | Basic $O(NM)$ 2D prefix-sum DP where the inputs $S, T$ are arbitrary strings rather than translation-invariant lattice step sets. | `yukicoder 1080` (Generalized Delannoy Diagonal), `ABC 240 G` (Teleporting Takahashi) |
| **`R-66`** | **Luogu P5488 & Luogu P6115** — *差分与前缀和 & `【模板】整式递推`* ([Luogu](https://www.luogu.com.cn/problem/P5488)) | `5A#L1690`, `5A#L1691` | **Ch 18** | Direct $(1 \pm x)^{\pm k} \bmod x^n$ template and bare BSGS P-recursive matrix product template without combinatorial D-finite ODE derivation. | `UOJ #514` ([UR #19] 通用测评号), `CF 755G` (PolandBall and Many Other Balls) |
| **`R-67`** | **Library Checker** — *`static_top_tree` / `point_set_tree_path_composite_sum` & `polynomial_composite_set_power_series`* ([LC](https://judge.yosupo.jp/problem/static_top_tree)) | `5B#L3051`, `5B#L3066` | **Ch 22** | Pure data-structure / Set Power Series black-box verification templates without combinatorial tree or subgraph modeling. | `ABC 269 Ex` (Antichain), `ABC 355 G` (Baseball), `LOJ #154` (集合划分计数) |
---

## 6. Complete 254-Problem Bijective Master Lookup Table (`#001`–`#254`) & Audit Ledger

### 6.1 Bijective Master Directory (`#001`–`#254`: `192` Ladder + `48` Checkpoint + `14` Synthesis = `254`)

> **Automated Bijection Guarantee**: Every accepted problem `#001` through `#254` appears **exactly once** in the table below (`0` duplicates, `0` omissions, `0` forward-reference violations).

| Pool ID | Problem ID & Title | Source Wave | Canonical Phase 1.5 Slot | Core Mathematical Mechanism & Role |
| :-: | :--- | :-: | :--- | :--- |
| `#001` | **`fps_24_a` — Snack / Snacks** | `1A#1` | **`Ch 03 [SS-1]`** | OGF Product & Polynomial Power $P(x)^D$ / Subset-Sum $\ln$-$\exp$ |
| `#002` | **`fps_24_e` — Sequence 2** | `1A#15` | **`Ch 04 [SS-1]`** | Labeled Multiset Permutation EGF $\prod_{m=1}^M \sum_{j=0}^m \frac{x^j}{j!}$ |
| `#003` | **`fps_24_f` — Colored Paper / Colored Tree** | `1A#2` | **`Ch 11 [SS-1]`** | Implicit Tree Equation $F = x \cosh F$ Solved via $[x^n]F = \frac{1}{n}[u^{n-1}]\cosh^n u$ |
| `#004` | **`fps_24_g` — Coin** | `1A#2` | **`Ch 01 [Int-1]`** | Dynamic Sliding-Window Partition $\prod_{j=k}^{k+L-1}(1-x^j)^{-1}$ & Reversible Coin DP |
| `#005` | **`fps_24_h` — Jump** | `2A#1` | **`Ch 06 [SS-1]`** | Bivariate Rational Substitution $\frac{1-y}{1-2y-x}$ & Taylor Shift |
| `#006` | **`fps_24_k` — Permutation** | `1A#4` | **`Syn-01`** | Ch 01 (Newton `inv`) $\times$ Ch 04 (Derangement EGF) $\times$ Ch 08 (Cluster IE) |
| `#007` | **`fps_24_m` — Value of Permutation** | `1A#20` | **`Ch 04 [SS-2]`** | Cycle Decomposition EGF $\ln\frac{1}{1-x}$ & Pointer Tracking |
| `#008` | **`fps_24_n` — Tree** | `3A#2` | **`Ch 04 [Int-2]`** | Prüfer Sequence Degree-Distribution EGF $n![x^{n-2}]\prod E_{d_i}(x)$ |
| `#009` | **`fps_24_n` — Coin 2 / Coins 2** | `1A#7b` | **`Ch 03 [Int-2]`** | Harmonic $\ln$-$\exp$ Compression $\prod(1+x^{A_i})$ & Bounded Numerator $\prod(1-x^{A_i+1})$ |
| `#010` | **`fps_24_p` — Ball** | `1A#29` | **`Ch 11 [Adv-1]`** | Bivariate Root Shift + Formal Residue / Lagrange Inversion |
| `#011` | **`fps_24_q` — Dice** | `1B#18` | **`Ch 04 [Adv-2]`** | Newton–Girard Power Sums $-\ln\prod(1 - A_i x)$ + EGF Moment Expansion |
| `#012` | **`fps_24_r` — Random Walk** | `2A#47` | **`Ch 07 [Adv-2]`** | Cyclic Convolution $\bmod (x^M - 1)$ via Roots of Unity & Catalan Kernel |
| `#013` | **`fps_24_s` — Game** | `1A#30` | **`Ch 10 [Int-2]`** | Tree Normal-Play Game $L = x\exp(x e^x - L)$ via Newton / Lambert $W$ |
| `#014` | **`fps_24_t` — Colorful** | `1A#22` | **`Syn-02`** | Ch 03 (Cycle Index) $\times$ Ch 04 (Cycle-Parity EGF) $\times$ Ch 08 (Smirnov Word IE) |
| `#015` | **`fps_24_v` — 12 Directions** | `1A#33` | **`Ch 17 [Adv-1]`** | 2D Laurent Step-Polynomial Factorization & Boundary Reduction |
| `#016` | **`fps_24_w` — Biconnected Graphs** | `3A#11` | **`Ch 12 [Adv-2]`** | Pointed Block-Cut Tree $\ln(R(x)/x) = B'(R(x))$ + Single-$n$ $O(n \log n)$ Lagrange Inversion Extraction (all-$n$ `revert` deferred to Ch 21.4) |
| `#017` | **`fps_24_x` — Functional Square Root** | `1A#31` | **`Ch 21 [Mas-2]`** | Iterated Composition $F(F(x)) = G(x)$ in $\mathbb{F}_p[[x]]/(x^N)$ |
| `#018` | **ABC 172 E — NEQ** | `2B#A2` | **`Ch 08 [SS-1]`** | Binomial Inversion & Rook-Style EGF |
| `#019` | **ABC 178 D — Redistribution** | `1B#4` | **`Ch 01 [SS-1]`** | Restricted Composition $x^3/(1-x)$ |
| `#020` | **ABC 213 G — Connectivity 2** | `1B#24` | **`Ch 24 [SS-2]`** | Connected Subgraph Subset Convolution ($\ln$) |
| `#021` | **ABC 222 H — Beautiful Binary Tree** | `3B#1` | **`Ch 09 [SS-2]`** | Explicit Causal Binary-Tree Recurrence $f_n = \sum c_{i,j} f_i f_j$ via CDQ / Relaxed Convolution (revisited via LIF in Ch 11 & ODE in Ch 18) |
| `#022` | **ABC 226 H — Random K-th Max** | `2B#E2` | **`Ch 18 [Int-1]`** | Order-Statistic Integral $\int_0^1 t^k(1-t)^{n-k} dt$ & Holonomic Recurrence |
| `#023` | **ABC 230 Ex — Bullion** | `1A#27` | **`Ch 09 [Int-2]`** | Unlabeled Knapsack / Weighings via Online Relaxed Convolution |
| `#024` | **ABC 236 Ex — Distinct Multiples** | `1A#19` | **`CP-I.8`** | Given $D_1, \dots, D_N$ ($N \le 16$), count tuples $(A_1, \dots, A_N)$ of distinct integers in $[1, M]$ with $D_i \mid A_i$. |
| `#025` | **ABC 240 G — Teleporting Takahashi** | `2A#43` | **`Ch 16 [Int-1]`** | 3D Walk Decoupled into 1D $\times$ Rotated 2D $(u,v) = (x+y, x-y)$ Bivariate Binomials |
| `#026` | **ABC 242 Ex — Random Painting** | `2B#E8` | **`Ch 14 [SS-2]`** | Continuous-Time Min-Max Stopping PGF $F'(1)$ |
| `#027` | **ABC 253 Ex — We Love Forest** | `5A#14` | **`Ch 24 [Int-1]`** | Set Power Series $\exp$ on Spanning Trees |
| `#028` | **ABC 260 Ex — Colorfulness** | `2B#B7` | **`Ch 19 [Adv-1]`** | Adjacent-Color IE + Coupled Divide-and-Conquer NTT + Truncated Taylor Shift |
| `#029` | **ABC 266 G — Yet Another RGB Sequence** | `2B#A5` | **`CP-II.6`** | Count strings of $R$ `R`s, $G$ `G`s, $B$ `B`s ($\le 10^6$) containing exactly $K$ occurrences of substring `RG`. |
| `#030` | **ABC 267 Ex — Odd Sum** | `1B#7` | **`Ch 02 [Mas-1]`** | Parity Split $\frac{P(x)-P(-x)}{2}$ + Logarithmic Derivative $\ln/\exp$ |
| `#031` | **ABC 269 Ex — Antichain** | `5B#A1` | **`Ch 22 [SS-1]`** | Heavy-Light Decomposition + D&C Tree FPS |
| `#032` | **ABC 276 G — Count Sequences** | `1B#19` | **`CP-I.4`** | Count sequences $a_1, \dots, a_N \in [0, M]$ ($N, M \le 10^7$) with $a_i \not\equiv a_{i+1} \pmod 3$. |
| `#033` | **ABC 278 Ex — make 1** | `5B#E2` | **`Ch 23 [SS-2]`** | Basis / XOR Space $q$-Binomial & $q$-Pochhammer |
| `#034` | **ABC 279 G — At Most 2 Colors** | `2B#B3` | **`Ch 05 [SS-2]`** | Sliding-Window Transfer-Matrix Rational OGF $P(x)/Q(x)$ |
| `#035` | **ABC 279 Ex — Sum of Prod of Min** | `4A#P10` | **`CP-III.6`** | Infinite Product $\prod_{i=1}^N \min(i, A_i) \implies [x^{M-N}]\prod_{i=1}^N \frac{1-(i+1)x^i+ix^{i+1}}{(1-x)^2}$ |
| `#036` | **ABC 281 Ex — Alchemy** | `2B#B12` | **`Ch 21 [SS-1]`** | Falling-Factorial EGF + Simultaneous All-$n$ `compositional_inverse` |
| `#037` | **ABC 284 Ex — Count Unlabeled Graphs** | `3A#38` | **`CP-I.7`** | Count unlabeled simple graphs on $N \le 60$ vertices modulo $p$. |
| `#038` | **ABC 288 Ex — A Nameless Counting Problem** | `5B#F10` | **`Ch 24 [Mas-2]`** | Dirichlet / Multiplicative Bell Series & XOR DP |
| `#039` | **ABC 289 Ex — Trio** | `2B#E12` | **`Ch 14 [Mas-1]`** | 3-Walker Return-to-Origin Absorbing PGF $(P^3) \oslash Q$ |
| `#040` | **ABC 300 Ex — Fibonacci: Revisited** | `2A#8` | **`Ch 05 [Adv-1]`** | 3-Sparse Denominator $(1-x)Q(x) = 1-2x+x^{K+1}$ + Bostan–Mori at $N \le 10^{18}$ |
| `#041` | **ABC 303 Ex — Constrained Tree Degree** | `3A#5` | **`Ch 04 [Mas-1]`** | Prüfer Sequence Degree-Constrained EGF $[x^{N-2}] P(x)^N$ via Dense $\exp(N \ln P(x))$ in $O(N \log N)$ |
| `#042` | **ABC 306 Ex — Balance Scale** | `5B#F5` | **`Ch 24 [Int-2]`** | DAG Orientation Set Power Series / Subset Inversion |
| `#043` | **ABC 321 F — #(subset sum = K) with Add/Erase** | `1B#3` | **`Ch 01 [SS-2]`** | Reversible $O(K)$ DP Division by $(1+x^v)$ |
| `#044` | **ABC 336 G — 16 Integers** | `3A#33` | **`Ch 17 [SS-2]`** | De Bruijn Eulerian Graph + MacMahon Master Theorem $\det(I - X A)^{-1}$ |
| `#045` | **ABC 345 G — Sugoroku 5** | `5B#B2` | **`Ch 21 [SS-2]`** | Hitting-Time PGF + Kinoshita–Li $O(N \log^2 N)$ Fast Polynomial Composition $F(G(x))$ |
| `#046` | **ABC 355 G — Baseball** | `5B#A3` | **`Ch 22 [Int-1]`** | Laminar Containment Tree + Tree-DP Convolution |
| `#047` | **ABC 387 G — Prime Circuit** | `4A#P25` | **`Ch 21 [Int-1]`** | Prime-Cycle Cactus EGF via $O(N \log^2 N)$ Fast Composition $C(T(x))$ |
| `#048` | **ARC 012 D — Don't Step on the Mines!** | `1B#11` | **`Ch 16 [SS-1]`** | 2D Walk Factoring + Prime-Power Kummer/Lucas Valuation |
| `#049` | **ARC 028 D — 注文の多い高橋商店** | `1B#6` | **`Ch 01 [Adv-1]`** | Reversible Bounded Knapsack Divide-by-$\frac{1-x^{a_i+1}}{1-x}$ |
| `#050` | **ARC 033 D — 多項式 (Polynomial)** | `5B#D1` | **`Ch 20 [SS-1]`** | $O(N)$ Sequential Prefix/Suffix Lagrange Interpolation |
| `#051` | **ARC 093 F — Dark Horse** | `2B#C2` | **`Syn-03`** | Ch 08 (Poset IE) $\times$ Ch 22 (Tree/Subtree Merging) $\times$ Ch 24 (SOS Subset Convolution) |
| `#052` | **ARC 100 F / LOJ 3395 — Colorful Sequences** | `2B#B8` | **`Ch 08 [Mas-1]`** | Forbidden Rainbow Window Automaton / IE OGF |
| `#053` | **ARC 105 F / LOJ 6539 — Lights Out on Connected Graph** | `1A#20` | **`Ch 13 [Adv-2]`** | Connected Bipartite Graph $\ln$ of Sqrt-Scaled Sum |
| `#054` | **ARC 106 E — Medals** | `2A#35` | **`CP-VI.5`** | Newton Identities / Power-Sum OGF |
| `#055` | **ARC 110 D — Binomial Coefficient is Fun** | `1B#16` | **`Ch 06 [SS-2]`** | Vandermonde Convolution $\prod (1-x)^{-(A_i+1)}$ |
| `#056` | **ARC 123 F — Arithmetic Progression** | `4B#32` | **`Ch 09 [Adv-1]`** | Non-Homogeneous Causal Recurrence via CDQ / Relaxed Convolution |
| `#057` | **ARC 134 E — Modulo Nim** | `5B#E9` | **`Ch 23 [Int-2]`** | $q$-Analogue / Subset Modulo Game Reduction |
| `#058` | **ARC 136 F — Flip Cells** | `2A#11` | **`CP-IV.6`** | Flip $N \le 50$ coins with target parity state and transition count $T$; extract the exact multi-parameter coefficient. |
| `#059` | **ARC 137 F — Overlaps** | `3B#22` | **`Ch 21 [Int-2]`** | Implicit Algebraic Equation + Riccati ODE + Fast Polynomial Composition |
| `#060` | **ARC 138 E — Decreasing Subsequence** | `5A#22` | **`Ch 09 [SS-1]`** | RSK / Greene Theorem Semi-Online Block CDQ Convolution |
| `#061` | **ARC 138 F — KD-Tree** | `4A#P26` | **`CP-V.7`** | Count valid interval-split sequences of length $n \le 2.5\times 10^5$ via power projection / compositional inverse. |
| `#062` | **ARC 139 F — Many Xor Optimization Problems** | `5B#E4` | **`Ch 23 [Adv-1]`** | $q$-Binomial Gaussian Elimination Basis Enumeration |
| `#063` | **ARC 145 F — Modulo Sum of Increasing Sequences** | `4B#33` | **`Ch 23 [Mas-1]`** | $q$-Pentagonal / Cyclic Orbit Sum + Good–Lagrange |
| `#064` | **ARC 153 D — Sum of Sum of Digits** | `5B#D9` | **`Ch 18 [SS-2]`** | Carry-Propagation Polynomial Shift & D-Finite Recurrence |
| `#065` | **ARC 154 F — Dice Game** | `4A#P23` | **`Ch 21 [Adv-1]`** | Coupon Collector Moment EGF + Fast Polynomial Composition |
| `#066` | **AGC 001 E — BBQ Hard** | `1B#9` | **`Ch 01 [Mas-1]`** | Offset Lattice-Path Vandermonde Shift $\binom{a_i+a_j+b_i+b_j}{a_i+a_j}$ |
| `#067` | **AGC 005 D — ~K Perm Counting** | `2B#B2` | **`Ch 08 [Adv-1]`** | Disjoint Rook Paths + Inclusion-Exclusion Convolution |
| `#068` | **AGC 005 F — Many Easy Problems** | `1A#12` | **`CP-V.8`** | Count $n \times m$ matrices over $\mathbb{F}_q$ ($n, m \le 2\times 10^5$) of each rank $r$ via $q$-binomials. |
| `#069` | **AGC 013 E — Placing Squares** | `2B#D5` | **`Ch 05 [Int-2]`** | Combinatorial Split-or-Pass $3 \times 3$ Matrix / Rational OGF |
| `#070` | **AGC 021 E — Ball Eat Chameleons** | `2A#18` | **`Ch 15 [SS-2]`** | Reflection Principle / Raney's Lemma Weak Ballot Bound |
| `#071` | **AGC 038 E — Gachapon** | `2B#E6` | **`Ch 14 [Int-2]`** | Multivariate Min-Max Stopping Time EGF $F'(1)$ |
| `#072` | **AGC 043 D — Merge Triplets** | `2B#C3` | **`Ch 19 [Mas-1]`** | Sparse Composition ODE $\partial_x F = (y + xy^{-1} + x^2)F$ on $\exp(xy + \frac{x^2}{2}y^{-1} + \frac{x^3}{3})$ |
| `#073` | **AGC 054 E — ZigZag Break** | `2A#21` | **`Ch 05 [Mas-2]`** | Difference Cancellation / Telescoping Rational Series |
| `#074` | **AGC 058 D — Yet Another ABC String** | `2B#A8` | **`Ch 16 [Adv-2]`** | Trivariate Rational Cluster Diagonal $[x^A y^B z^C] \frac{1-xyz}{1-(x+y+z)+2xyz}$ |
| `#075` | **AGC 060 D — Same Generating Function** | `1B#25` | **`Ch 09 [Mas-2]`** | Coupled Eulerian Permutation Ascent CDQ Divide-and-Conquer FFT |
| `#076` | **AGC 070 C — No Clar** | `3A#20` | **`Ch 15 [Mas-1]`** | Bivariate Ballot / Catalan Path Pair Extraction |
| `#077` | **EDPC M — Candies** | `1B#2` | **`Ch 01 [Int-2]`** | Prefix-Sum Optimization of $\prod \frac{1-x^{a_i+1}}{1-x}$ |
| `#078` | **Typical90 #065 — RGB Balls 2** | `4A#P1` | **`CP-I.1`** | Pick $K$ balls from $R$ red, $G$ green, $B$ blue ($R,G,B,K \le 2\times 10^5$) subject to pairwise sum bounds $r+g \le X, g+b \le Y, b+r \le Z$. |
| `#079` | **JSC 2019 Qual F — Candy Retribution** | `1B#15` | **`CP-I.5`** | Distribute $S$ candies to $N$ children ($N, M, S \le 3\times 10^5$) so the top $M$ children each receive in $[a, b]$. |
| `#080` | **KUPC 2019 K — One or All** | `2A#4` | **`Ch 06 [Int-2]`** | Projective Möbius Substitution $(1-x)^N A(\frac{1+x}{1-x})$ |
| `#081` | **AISing 2020 F — Two Snuke** | `1B#22` | **`Ch 05 [Adv-2]`** | 10-Tuple Difference Weight OGF $F(z) = \frac{z^5(1+z)^{11}}{(1-z^2)^{16}}$ + Parity Extraction |
| `#082` | **Toyota 2023 Spring Final E — Replace Digits / Tree Constraint** | `3A#16` | **`CP-IV.8`** | Implicit Tree Degree Constraint + Lagrange Inversion |
| `#083` | **CF 407E / Gym — k-Cycle** | `1A#21` | **`Ch 04 [Adv-1]`** | Constrained Cycle-Length Permutation EGF $\exp(\sum_{k \in S} \frac{x^k}{k})$ |
| `#084` | **CF 438E — The Child and Binary Tree** | `1A#7` | **`Ch 02 [Adv-2]`** | Explicit Quadratic Radical $F(x) = \frac{2}{1 + \sqrt{1 - 4x C(x)}}$ via `poly_sqrt` + `poly_inv` (revisited via CDQ in Ch 09 & Newton in Ch 10) |
| `#085` | **CF 451E — Devu and Flowers** | `2B#A1` | **`CP-II.1`** | Pick $s \le 10^{14}$ flowers from $n \le 20$ boxes where box $i$ has $f_i$ flowers. |
| `#086` | **CF 553E — Kyoya and Train** | `1B#13` | **`Ch 09 [Int-1]`** | Time-Window Shortest Path DP via CDQ Divide-and-Conquer FFT |
| `#087` | **CF 623E — Transforming Sequence** | `1B#23` | **`Syn-04`** | Ch 04 (Binomial EGF) $\times$ Ch 06 (Geometric Taylor Shift) $\times$ Ch 23 ($q$-Binomial Doubling) |
| `#088` | **CF 755G — PolandBall and Many Other Balls** | `2B#D4` | **`Ch 18 [Adv-2]`** | Continuant Matrix GF + Hyperbola Residue + $O(K)$ 2nd-Order D-Finite ODE |
| `#089` | **CF 840C — On the Bench** | `2B#B4` | **`Ch 08 [Int-2]`** | Adjacent-Block Inclusion-Exclusion via Falling-Factorial EGF |
| `#090` | **CF 848E — Days of Floral Colours** | `5A#15` | **`CP-III.1`** | $4 \times 4$ Matrix Rational Denominator + CDQ NTT |
| `#091` | **CF 891E — Lust** | `1A#16` | **`Ch 02 [Mas-2]`** | Polynomial Product $\prod_{i=1}^n (a_i - x)$ + Formal Derivative / Coefficient Extraction |
| `#092` | **CF 901E — Periodicovsky** | `5B#D10` | **`Ch 07 [Mas-1]`** | Cyclic Chirp-$Z$ Transform (Bluestein's Algorithm) |
| `#093` | **CF 917D — Stranger Trees** | `3A#36` | **`Ch 13 [Int-1]`** | Weighted Matrix-Tree Determinant Interpolation / Prüfer |
| `#094` | **CF 923E — Perpetual Subtraction** | `2A#2` | **`Ch 06 [Adv-1]`** | Diagonalization of Pascal / Shift Operator via Taylor Shift |
| `#095` | **CF 932E — Team Work** | `1B#10` | **`Ch 19 [Int-1]`** | Stirling S2 Expansion $\sum S(K,j)\binom{N}{j}j! 2^{N-j}$ + $O(K)$ `EI 科技` ODE |
| `#096` | **CF 960G — Bandit Blues** | `1A#23` | **`Ch 06 [Adv-2]`** | Unsigned Stirling S1 $\left[\begin{smallmatrix} n-1 \\ A+B-2 \end{smallmatrix}\right] \binom{A+B-2}{A-1}$ via Doubling Shift |
| `#097` | **CF 993E — Nikita and Order Statistics** | `1B#17` | **`Ch 01 [Adv-2]`** | Prefix-Count Reverse Indexing Difference Convolution |
| `#098` | **CF 995F — Cowmpany Cowmpensation** | `5B#D6` | **`Ch 06 [Mas-1]`** | Tree DP Polynomial Degree Bound + $O(N)$ Lagrange Interpolation |
| `#099` | **CF 1025G — Company Acquisitions** | `2B#E14` | **`CP-IV.3`** | Simulate a random process on $n \le 2\times 10^5$ piles and compute the expected stopping time modulo $998244353$. |
| `#100` | **CF 1054H — Epic Convolution** | `2A#49` | **`CP-II.5`** | Evaluate $\sum_{k=0}^n f(k) \binom{n}{k} p^k (1-p)^{n-k}$ for degree-$d$ polynomial $f$ ($n \le 10^9, d \le 5\times 10^5$). |
| `#101` | **CF 1096G — Lucky Tickets** | `1B#8` | **`Ch 02 [Int-1]`** | $O(NK)$ Sparse Power ODE $(1-x)(1-x^{10})G' = k P' G$ (Zero NTTs) |
| `#102` | **CF 1097G — Vladislav and a Great Legend** | `2A#28` | **`CP-VI.1`** | Given a tree on $n \le 10^5$ vertices and exponent $k \le 200$, compute $\sum_{S} (\text{steiner}(S))^k$. |
| `#103` | **CF 1109D — Sasha and Interesting Fact** | `4B#8` | **`Ch 13 [SS-2]`** | Generalized Cayley Forest Formula $k n^{n-k-1}$ |
| `#104` | **CF 1117D — Magic Gems** | `4A#P4` | **`Ch 05 [SS-1]`** | Sparse Denominator $1/(1-x-x^M)$ + Bostan–Mori |
| `#105` | **CF 1204E — Natasha, Sasha and the Prefix Sums** | `3A#1` | **`Ch 15 [SS-1]`** | Reflection Principle on Exceedance Thresholds |
| `#106` | **CF 1228E — Another Filling the Grid** | `2B#A8` | **`Syn-05`** | Ch 06 (Binomial Sums) $\times$ Ch 08 (2D Bipartite IE) $\times$ Ch 16 (Bivariate Series) |
| `#107` | **CF 1251F — Red-White Fence** | `1A#11` | **`Ch 01 [Mas-2]`** | $2x(1+2x)^{c_1}(1+x)^{2c_2}$ Frequency Grouping |
| `#108` | **CF 1264D2 — Beautiful Bracket Sequence (Hard)** | `4A#P12` | **`CP-V.2`** | Vandermonde Absorption Identity $i \binom{A}{i} = A \binom{A-1}{i-1}$ |
| `#109` | **CF 1278F — Cards** | `2A#29` | **`Ch 06 [Mas-2]`** | Expected $K$-th Moment of Binomial via Falling Factorials |
| `#110` | **CF 1326F2 — Wise Men (Hard Version)** | `2B#C4` | **`Ch 24 [Adv-1]`** | Partition Subset Convolution + SOS / Möbius Inversion |
| `#111` | **CF 1336E2 — Chiori and Doll Picking (Hard)** | `4A#P17` | **`Ch 23 [Mas-2]`** | MacWilliams Dual-Code Krawtchouk Transform ($O(2^{m-r})$) |
| `#112` | **CF 1342E — Placing Rooks** | `2A#22` | **`Syn-06`** | Ch 04 (Set Partition EGF $\exp$) $\times$ Ch 06 (Stirling S2 Row Extraction) $\times$ Ch 08 (Rook Polynomials) |
| `#113` | **CF 1349D — Slime and Biscuits** | `2A#12` | **`Ch 14 [Mas-2]`** | Martingale Stopping Potential + First-Difference Order Reduction |
| `#114` | **CF 1349F2 — Slime and Sequences (Hard Version)** | `1A#30` | **`Ch 11 [Mas-1]`** | Eulerian Bivariate EGF $\to$ Lambert-$W$ Substitution + Lagrange Inversion |
| `#115` | **CF 1392H — ZS Shuffles Cards** | `2B#E1` | **`Ch 14 [SS-1]`** | Memoryless Geometric Stopping PGF + Harmonic Expectation |
| `#116` | **CF 1479E — School Clubs** | `2B#E15` | **`CP-IV.4`** | Given $n \le 500$ targets on a random walk, compute the expected hitting time via first-passage decomposition. |
| `#117` | **CF 1510H — Hard Optimization** | `5B#A12` | **`CP-VI.3`** | Given a tree on $n \le 2000$ vertices with interval weights, merge heavy-path polynomial DP states. |
| `#118` | **CF 1515E — Phoenix and Computers** | `2B#B1` | **`Ch 19 [Adv-2]`** | Sparse Composition Pullback $F(x,y) = (1 - x(e^y-1))^{-1}$ + Row ODE |
| `#119` | **CF 1528F — AmShZ Farm** | `3A#17` | **`CP-III.5`** | Count planted trees on $n \le 10^5$ vertices where every internal node has out-degree in $\{0\} \cup S$. |
| `#120` | **CF 1548C — The Three Little Pigs** | `2A#7` | **`Ch 19 [SS-2]`** | Sparse Composition Pullback $H(x) = \frac{u^{N+1}-1}{u-1}\big\rvert_{u=(1+x)^3}$ in $O(N)$ |
| `#121` | **CF 1553I — Stairs** | `4A#P16` | **`CP-VI.2`** | Given stair-length constraints on a sequence/tree of length $n \le 10^5$, merge interval DP states via D&C. |
| `#122` | **CF 1556F — Sports Betting (Strongly Connected Variant)** | `3A#37` | **`Ch 13 [Mas-1]`** | Strongly Connected Digraphs via Semiring/FPS Inversion |
| `#123` | **CF 1603F — October 18, 2017** | `5B#E1` | **`Ch 23 [SS-1]`** | $q$-Binomial Rank Enumeration in $\mathbb{F}_2^k$ |
| `#124` | **CF 1613F — Tree Coloring** | `2A#36` | **`Ch 22 [SS-2]`** | Derangement-Style Tree Degree Inclusion-Exclusion $\prod(1 + c_u x)$ |
| `#125` | **CF 1667E — Centroid Probabilities** | `3A#8` | **`Ch 18 [Adv-1]`** | Tree Centroid Differential Recurrence + Reverse Convolution |
| `#126` | **CF 1687F — Koishi's Unconscious Permutation** | `3B#20` | **`Ch 10 [Adv-2]`** | Implicit Bivariate / Cycle-Rise Permutation Equations |
| `#127` | **CF 1770G — Koxia and Bracket** | `5B#B8` | **`Ch 20 [Int-1]`** | Transposed Divide-and-Conquer NTT on Bracket Prefixes |
| `#128` | **CF 1810G — The Maximum Prefix** | `3A#9` | **`Ch 15 [Adv-1]`** | Backward DP / Kernel Method on Prefix Maxima |
| `#129` | **CF 1821F — Timber** | `4B#12` | **`Ch 16 [SS-2]`** | Inclusion-Exclusion on Domino Fall Directions $\frac{1}{1-x-yx^{k+1}(2-x^k)}$ |
| `#130` | **CF 1842I — Tenzing and Necklace** | `5B#B17` | **`CP-V.3`** | Given a tree/array of size $n \le 10^5$, compute a shifted multi-parameter convolution using transposed multiplication. |
| `#131` | **CF 1906J — Count BFS Graphs** | `5B#A10` | **`CP-III.2`** | Count labeled tournament structures / intervals on $n \le 10^5$ vertices via recursive complement subtraction. |
| `#132` | **CF 1916F — Group Division** | `5B#E6` | **`Ch 23 [Adv-2]`** | Bipolar Orientation / Biconnected $q$-Analogue |
| `#133` | **CF 1930I — Counting Is Fun** | `3B#24` | **`CP-III.3`** | For each $k$, count binary strings of length $n \le 2\times 10^5$ whose self-overlapping blocks satisfy a prefix-recursive rule. |
| `#134` | **CF 1967E2 — Again Counting Arrays (Hard)** | `3A#4` | **`Ch 15 [Adv-2]`** | Bounded-Wall Reflection Principle ($\pm 1$ Walk between $0$ and $M$) |
| `#135` | **CF 1988F — Heartbeat** | `5B#B15` | **`CP-V.4`** | Given $f(0), f(1), \dots, f(d)$ ($d \le 1.6\times 10^5$), evaluate $f(c), f(c+1), \dots, f(c+m)$ in $O(d \log d)$ time. |
| `#136` | **CF 2006E — Iris's Full Binary Tree** | `5B#A15` | **`Ch 22 [Adv-2]`** | Centroid / Heavy-Light Tree Convolution |
| `#137` | **CF Gym 102331J — Forbidden Strings** | `2B#D3` | **`Ch 08 [Mas-2]`** | Multi-Pattern Aho–Corasick Goulden–Jackson Cluster Matrix $(I + C(x))^{-1}$ |
| `#138` | **CF Gym 102538F — 3D Walk / Quarter Plane** | `4B#31` | **`Ch 17 [Mas-1]`** | Quarter-Plane Obstinate Kernel / Algebraic Group Involution |
| `#139` | **CF Gym 102978H — Harsh Comments / Motzkin** | `2A#16` | **`Ch 08 [Adv-2]`** | Motzkin Trinomial Radical + Multi-Pattern Goulden–Jackson |
| `#140` | **CF Gym 103415K / yukicoder 1341 — Gambler's Walk** | `4B#14` | **`Ch 15 [Int-2]`** | Asymmetric $+1, -2$ Walk via Small-Root Kernel Factoring |
| `#141` | **Luogu P2290 / P4430 — 树的计数 / 猴猴吃香蕉** | `1B#7` | **`CP-II.8`** | Prüfer Sequence Multinomial Coefficient $\frac{(n-2)!}{\prod (d_i-1)!}$ |
| `#142` | **Luogu P3311 — [SDOI2014] 数数** | `2B#D3` | **`Syn-07`** | Ch 05 (Rational Transfer Matrix) $\times$ Ch 08 (Goulden–Jackson Multi-Pattern Avoidance) |
| `#143` | **Luogu P3321 — [SDOI2015] 序列统计** | `5B#D3` | **`Ch 07 [Int-2]`** | Primitive Root Discrete Log + Cyclic Convolution $\bmod (x^{p-1}-1)$ |
| `#144` | **Luogu P3338 — [ZJOI2014] 力** | `1B#5` | **`CP-I.2`** | Given $q_1, \dots, q_n$ ($n \le 10^5$), compute $E_i = \sum_{j < i} \frac{q_j}{(i-j)^2} - \sum_{j > i} \frac{q_j}{(i-j)^2}$ for all $i$. |
| `#145` | **Luogu P3348 — [ZJOI2016] 大森林** | `5B#A19` | **`Ch 22 [Mas-2]`** | Offline Tree Modification + HLD Polynomial Chain Product |
| `#146` | **Luogu P3684 / BZOJ 3684 — 大朋友和多叉树** | `3B#25` | **`Ch 12 [Int-1]`** | Degree-Constrained Multi-Way Rooted Tree Species + Lagrange Inversion |
| `#147` | **Luogu P3702 — [SDOI2017] 序列计数** | `1B#14` | **`Ch 07 [Adv-1]`** | Prime Complementary Sieve + Cyclic Convolution $\bmod (x^p - 1)$ |
| `#148` | **Luogu P3706 — [SDOI2017] 硬币游戏** | `2B#E3` | **`Ch 14 [Adv-1]`** | Multi-Player Guibas–Odlyzko Correlation Linear System |
| `#149` | **Luogu P3781 / LOJ 2269 — [SDOI2017] 切树游戏** | `5B#A8` | **`Ch 22 [Adv-1]`** | FWT + Heavy-Light Decomposition + Zero-Count $(\text{val}, \text{cnt})$ Ring |
| `#150` | **Luogu P3784 — [SDOI2017] 遗忘的集合** | `1B#25` | **`Ch 03 [Mas-1]`** | Inverse Euler Transform (Recovering Item Set from Subset Sums) |
| `#151` | **Luogu P4002 — [清华集训2017] 生成树计数** | `3A#27` | **`Ch 18 [SS-1]`** | Algebraic / Prüfer Tree Block Sum $\to$ D-Finite Differential Reduction |
| `#152` | **Luogu P4091 — [HEOI2016] 求和** | `2A#23` | **`CP-II.2`** | Given $N, M \le 2.5\times 10^5$, compute $\sum_{k} \binom{N}{k}\binom{M}{k}\dots$ with three coupled index constraints. |
| `#153` | **Luogu P4389 — 付公主的背包** | `1A#7a` | **`Ch 03 [Int-1]`** | Harmonic $\ln$-$\exp$ Subset-Sum Compression ($O(M \log M)$) |
| `#154` | **Luogu P4456 — [CQOI2018] 交错序列** | `5A#7` | **`Ch 17 [SS-1]`** | 2D Constrained Step Walk $(x, y)$ Moment Extraction $\sum i^a j^b$ |
| `#155` | **Luogu P4491 — [HAOI2018] 染色** | `2B#A7` | **`Ch 08 [Int-1]`** | Exact-$k$ Color Frequency Binomial Inversion Convolution |
| `#156` | **Luogu P4548 — [CTSC2006] 歌唱王国** | `1A#15` | **`Ch 14 [Int-1]`** | KMP Border Polynomial / Guibas–Odlyzko $F'(1) = \sum_{\text{border } L} m^L$ |
| `#157` | **Luogu P4705 — 玩游戏** | `1A#24` | **`Ch 02 [Adv-1]`** | Newton–Girard Power Sums $\ln\prod(1 - a_i x)$ + Binomial Convolution |
| `#158` | **Luogu P4707 — 重返现世** | `2B#E5` | **`CP-IV.1`** | Given $n \le 1000$ items with probabilities $p_i$ ($\sum p_i \le 10^4$), find the expected time until at least $k$ items appear. |
| `#159` | **Luogu P4727 — [HNOI2009] 图的同构记数** | `2A#39` | **`Ch 03 [Mas-2]`** | Burnside's Lemma + Partition Cycle Index $Z(S_n)$ |
| `#160` | **Luogu P4747 — [CERC2017] Intrinsic Interval** | `2B#B11` | **`CP-III.4`** | Given $f(x)$ of degree $n \le 10^5$, solve a nonlinear functional equation $G(x) = \dots$ to degree $n$. |
| `#161` | **Luogu P4841 — [集训队作业2013] 城市规划** | `1A#14` | **`Ch 04 [Int-1]`** | Labeled Connected Graphs $C(x) = \ln G(x)$ via EGF Logarithm |
| `#162` | **Luogu P4859 — 已经没有什么好害怕的了** | `2B#A9` | **`CP-II.7`** | Given two arrays $A, B$ of length $n \le 2000$, count pairings with exactly $k$ pairs satisfying $A_i > B_{\pi(i)}$. |
| `#163` | **Luogu P5206 — [WC2019] 数树** | `2B#B9` | **`CP-III.8`** | Count labeled biconnected / block-structured graphs on $n \le 10^5$ vertices with cycle-weight constraints. |
| `#164` | **Luogu P5219 — 无聊的水题 I** | `3A#3` | **`Ch 13 [SS-1]`** | Bounded-Degree Labeled Spanning Trees via Prüfer EGF $\prod_{i=1}^n \left(\sum_{j=0}^{D-2} \frac{x^j}{j!}\right)$ |
| `#165` | **Luogu P4389 (0-1 Subset Sum Variant) / AtCoder FPS Subset Sum via ln/exp** | `1D#4` | **`Ch 02 [SS-2]`** | Subset-Sum Product $\prod(1 + x^{a_i})$ via Logarithmic Derivative & $\exp$ |
| `#166` | **Luogu P5281 / LOJ 3044 — [ZJOI2019] Minimax 搜索** | `5B#A11` | **`Ch 22 [Mas-1]`** | Dynamic Tree DP + HLD Rational / Polynomial Chain Product |
| `#167` | **Luogu P5284 — [十二省联考2019] 字符串问题** | `5B#B5` | **`Ch 20 [Int-2]`** | Suffix Automaton DAG Path via Segment-Tree / Transposed Optimization |
| `#168` | **Luogu P5293 — [HNOI2019] 白兔之舞** | `2A#48` | **`Ch 07 [Mas-2]`** | $k \times k$ Matrix Walk Modulo $x^L - 1$ + Bluestein Chirp-$Z$ |
| `#169` | **Luogu P5326 — [ZJOI2019] 开关** | `2B#E10` | **`CP-IV.2`** | Given $n$ switches ($\sum p_i \le 5\times 10^4$), find the expected number of toggles to reach target states $s_i \in \{0,1\}$. |
| `#170` | **Luogu P5327 — [ZJOI2019] 语言** | `5B#A18` | **`CP-VI.4`** | Given $m \le 10^5$ paths on a tree of size $n \le 10^5$, count connected path unions via tree DP + FPS. |
| `#171` | **Luogu P5339 — [TJOI2019] 唱、跳、rap和篮球** | `2B#B5` | **`Syn-08`** | Ch 01 (D&C Convolution) $\times$ Ch 04 (Bounded EGF) $\times$ Ch 08 (Forbidden Block IE) |
| `#172` | **Luogu P5366 — [SNOI2017] 遗失的答案** | `5B#E5` | **`Syn-11`** | Ch 08 (GCD/LCM Boundary Inclusion–Exclusion) $\times$ Ch 23 (Prime-Exponent Divisor Lattice) $\times$ Ch 24 (Bitwise OR FWT / SOS Transform) |
| `#173` | **Luogu P5400 — [CTS2019] 随机立方体** | `2B#A10` | **`Syn-09`** | Ch 06 (Binomial Inversion) $\times$ Ch 08 (3D Poset IE) $\times$ Ch 14 (Probabilistic Stopping) |
| `#174` | **Luogu P5401 — [CTS2019] 珍珠** | `1B#14` | **`Ch 04 [Mas-2]`** | Parity EGF $\left(\frac{e^x+e^{-x}}{2}\right)^k$ + Binomial Inversion |
| `#175` | **Luogu P5406 — [THUPC2019] 找树** | `4A#P8` | **`CP-VI.7`** | Given hypergraph edge weights on $n \le 20$ vertices, count connected spanning sub-hypergraphs via Set Power Series. |
| `#176` | **Luogu P5434 — 有标号荒漠计数** | `3A#9` | **`Ch 12 [SS-1]`** | Labeled Desert EGF $\exp(C_{\text{cactus}}(x))$ via Cactus $\exp$ |
| `#177` | **Luogu P5487 — [BJOI2019] 勘破神机** | `4A#P18` | **`Ch 05 [Mas-1]`** | Berlekamp–Massey + Bostan–Mori + Stirling S1 Power Sums |
| `#178` | **Luogu P5591 — 小猪佩奇学数学** | `2A#46` | **`Ch 07 [Int-1]`** | Floor-Sum Roots-of-Unity Filter $\sum_{k=0}^n \binom{n}{k} p^k \lfloor k/w \rfloor$ |
| `#179` | **Luogu P5597 — 【XR-4】复读** | `3B#18` | **`Ch 10 [Adv-1]`** | Unlabeled $k$-ary Tree Automaton Minimization + Coupled Implicit Newton Iteration |
| `#180` | **Luogu P5643 — [PKUWC2018] 随机游走** | `2B#E16` | **`CP-VI.8`** | Given a multiplicative arithmetic function on $n \le 10^{10}$, evaluate prefix sums via Dirichlet series convolution. |
| `#181` | **Luogu P5668 — N-Step Shift** | `5B#D8` | **`Ch 20 [Mas-1]`** | Sequential Lagrange Shift + Multipoint Evaluation |
| `#182` | **Luogu P5824 — 十二重计数法** | `1A#25` | **`Syn-10`** | Ch 01 (Polynomial `inv`) $\times$ Ch 03 (Partitions & Pentagonal OGF) $\times$ Ch 04 (EGF $\exp$) $\times$ Ch 06 (Stirling $S_2$) |
| `#183` | **Luogu P5827 — 点双连通图计数** | `3A#10` | **`Ch 12 [Mas-1]`** | Single-Degree $N$ Vertex-Biconnected Graphs via Pointed Block-Cut Equation & $O(N \log N)$ Lagrange Inversion (all-$n$ `revert` in Ch 21.4) |
| `#184` | **Luogu P5828 — 边双连通图计数** | `3A#13` | **`Ch 12 [Mas-2]`** | Single-Degree $N$ Edge-Biconnected Graphs via $C'(x) = B'(C(x)e^{C'(x)})$ & $O(N \log N)$ Lagrange Inversion (all-$n$ `revert` in Ch 21.4) |
| `#185` | **Luogu P5853 — Stirling & Falling Factorial Transpose** | `5B#B14` | **`CP-V.5`** | Evaluate a tree-structured polynomial recurrence at $n \le 10^5$ query points using subproduct tree evaluation. |
| `#186` | **Luogu P5900 — 无标号无根树计数** | `1A#29` | **`Ch 10 [SS-1]`** | Otter's Dissymmetry Theorem $U(x) = R(x) - \frac{1}{2}(R(x)^2 - R(x^2))$ |
| `#187` | **Luogu P6078 — [CEOI2004] Sweet** | `1B#8` | **`Ch 05 [Int-1]`** | Sparse Denominator $(1-x)^{-n} \prod (1-x^{m_i+1})$ |
| `#188` | **Luogu P6189 — [NOI Online #1] 跑步** | `1A#6` | **`Ch 03 [SS-2]`** | Integer Partition $O(N\sqrt{N})$ Durfee Square / Pentagonal Number Theorem |
| `#189` | **Luogu P6295 — 有标号 DAG 计数** | `3A#34` | **`Ch 13 [Int-2]`** | Robinson–Stanley EGF $\sum (-1)^{k-1} \frac{x^k}{k! 2^{\binom{k}{2}}}$ Inversion + $\ln$ |
| `#190` | **Luogu P6596 — How Many of Them** | `3A#14` | **`Ch 12 [Adv-1]`** | Labeled Connected Graphs with $\le k$ Bridges via Tree-of-2-ECCs EGF |
| `#191` | **Luogu P6598 — 烷烃计数 (Alkanes)** | `1A#14` | **`Ch 10 [Mas-1]`** | Pólya $S_3, S_4$ Cycle Index + Otter Dissimilarity |
| `#192` | **Luogu P6597 — 烯烃计数 (Alkenes)** | `1A#14` | **`Ch 10 [Mas-2]`** | Double-Bond Unrooted Carbon Trees via Cycle Index |
| `#193` | **Luogu P6620 — [省选联考2020 A卷] 组合数问题** | `2A#24` | **`Ch 06 [Int-1]`** | Polynomial-Weighted Binomial Sum via Falling Factorials $k^{\underline{j}}\binom{n}{k} = n^{\underline{j}}\binom{n-j}{k-j}$ |
| `#194` | **Luogu P6633 — [ZJOI2020] 抽卡** | `3B#8` | **`CP-IV.5`** | Draw items without replacement from weighted pools ($N \le 2\times 10^5$); compute the expected stopping steps. |
| `#195` | **Luogu P6667 — [清华集训2016] 如何优雅地求和** | `2A#25` | **`Ch 19 [Int-2]`** | Binomial Sum $\sum \binom{n}{k} x^k (1-x)^{n-k} f(k)$ via Falling Factorials / $O(m)$ ODE |
| `#196` | **Luogu P6672 — [清华集训2016] 你的生命已如风中残烛** | `4B#5` | **`Ch 11 [Int-1]`** | 1D Raney's Lemma Cyclic Shift $\frac{1}{m+1}$ on Degree Sequences |
| `#197` | **Luogu P7116 — [NOIP2020] 微信步数** | `5B#D7` | **`Ch 20 [SS-2]`** | High-Dimensional Walk Volume Sum via Bernoulli / Lagrange Interpolation |
| `#198` | **Luogu P7279 — 光棱碎片 (Prism Shards)** | `5B#A4` | **`Ch 22 [Int-2]`** | $2 \times 2$ Polynomial Matrix Heavy-Light Decomposition |
| `#199` | **Luogu P7364 — 有标号二分图计数** | `3A#33` | **`Ch 13 [Adv-1]`** | 2-Colored Graph EGF $B_2(x) \implies \text{Connected } \frac{1}{2}\ln B_2(x) \implies \text{Total } \sqrt{B_2(x)}$ |
| `#200` | **Luogu P7438 — [AGM 2021] 恐龙** | `3B#28` | **`Ch 11 [SS-2]`** | Composite Power Extraction $[x^N] F(x)^k = \frac{k}{N}[u^{N-k}]\phi(u)^N$ |
| `#201` | **Luogu P7439 — [KrOI2021] 蕾切尔** | `3B#29` | **`Ch 11 [Int-2]`** | Formal Residue Change of Variables $\operatorname{Res}_x G(x) = \operatorname{Res}_u G(F(u))F'(u)$ |
| `#202` | **Luogu P7440 — [KrOI2021] Feux Follets** | `5B#B13` | **`Ch 20 [Adv-2]`** | Multipoint Evaluation + Transposed Polynomial Divide-and-Conquer |
| `#203` | **Luogu P7592 — 2021 CoE-II E (数树)** | `3B#11` | **`Ch 11 [Mas-2]`** | 4-Subtask Synthesis (2D Rational, Bivariate LIF, Lucas Char-$p$ LIF) |
| `#204` | **Luogu P7599 — [APIO2021] 雨林跳跃** | `4B#16` | **`Ch 17 [Adv-2]`** | 2D Dominance Lattice Walk + Bivariate Kernel Method |
| `#205` | **Luogu P8555 — 密码学第三次小作业** | `3B#21` | **`CP-III.7`** | Extract $[x^n]$ from a compositional functional equation $F(x) = x \phi(F(x))$ for $n \le 2\times 10^5$. |
| `#206` | **UOJ 50 — [UR #3] 链式反应** | `2A#46` | **`Ch 09 [Mas-1]`** | Non-Autonomous Differential Equation $F' = \frac{1}{2}A(x)F^2 + 1$ via CDQ FFT |
| `#207` | **UOJ 94 — [集训队互测2015] 胡策的统计** | `5B#F7` | **`Ch 24 [Adv-2]`** | Biconnected Subgraphs via Vertex-by-Vertex Set Power Series $\ln$ |
| `#208` | **UOJ 182 — a^-1 + b problem** | `5B#B12` | **`Ch 20 [Adv-1]`** | Alternating Fractional Linear Möbius Transforms + Multipoint Eval |
| `#209` | **UOJ 390 — [UNR #3] 百鸽笼** | `2B#E7` | **`Ch 14 [Adv-2]`** | Bounded-Capacity Stopping Time EGF $\prod \sum_{j < a_i} \frac{x^j}{j!}$ |
| `#210` | **UOJ 424 — count (Cartesian / Left-Depth Trees)** | `2A#20` | **`Ch 15 [Mas-2]`** | Chebyshev Rational Function $Q_m(x)/Q_{m+1}(x)$ + Reflection |
| `#211` | **UOJ 450 — [集训队作业2018] 复读机** | `1A#28` | **`Ch 18 [Mas-1]`** | Mod-$d$ Roots-of-Unity Filter $(e^x + e^{\omega x} + e^{\omega^2 x})^k$ + 2D PDE |
| `#212` | **UOJ 498 — 新年的追逐** | `3A#39` | **`Ch 13 [Mas-2]`** | Game on Random Graphs via Connected Component EGF |
| `#213` | **UOJ 514 — [UR #19] 通用测评号** | `5A#24` | **`Ch 19 [Mas-2]`** | `EI 科技` Truncated Exponential Derivative $\frac{d}{dx}(e^{-x} S_{<a}(x)) = -e^{-x} \frac{x^{a-1}}{(a-1)!}$ |
| `#214` | **UOJ 596 — [集训队互测2021] 三维立体混元劲** | `4A#P28` | **`Ch 16 [Mas-2]`** | 3D Connected Hypergraphs via Twisted Kronecker $\chi$-Graded $\ln G(x,y,z)$ & Radial Derivation $\mathfrak{D} = x\partial_x + y\partial_y + z\partial_z$ in $O(ABC \log(ABC))$ |
| `#215` | **UOJ 604 — [UR #20] 跳蚤电话** | `4A#P27` | **`CP-V.6`** | Given polynomials $F(x), G(x)$ of degree $N \le 1.3\times 10^5$, compute $F(G(x)) \bmod x^{N+1}$ in $O(N \log^2 N)$. |
| `#216` | **CF 449D — Jzzhu and Numbers** | `5B#F1` | **`Ch 24 [SS-1]`** | Superset SOS DP / Fast Zeta Transform + Inclusion-Exclusion |
| `#217` | **LOJ 161 — 快速阶乘算法** | `5B#D11` | **`Ch 20 [Mas-2]`** | $O(\sqrt{P} \log P)$ Sampling Shift Evaluation |
| `#218` | **LOJ 171 / QOJ 6504 — 幂投影 (Power Projection)** | `5B#B16` | **`Ch 21 [Adv-2]`** | Kinoshita–Li Transposed Composition $\sum_i w_i [x^i] F(x)^k$ |
| `#219` | **LOJ 3398 — 带加强和多项木** | `3B#9` | **`Ch 17 [Int-2]`** | Multivariate Implicit Tree System + Good–Lagrange Jacobian $\det(I - J_G(u))$ |
| `#220` | **Luogu P3266 — [JLOI2015] 骗我呢** | `4B#3` | **`Ch 15 [Int-1]`** | Two-Wall Alternating Reflection Principle Strip Walk |
| `#221` | **LOJ 6089 — 小 Y 的背包计数问题** | `2A#37` | **`Ch 03 [Adv-2]`** | $\sqrt{N}$ Split: Small Items DP + Large Items Partition Pentagonal Number |
| `#222` | **LOJ 6261 — 一个人的高三 (Lonely Senior Year)** | `1A#10` | **`Ch 02 [Int-2]`** | Series Power $F(x)^k$ & Binomial Series Expansion $(1-x)^{-\alpha}$ |
| `#223` | **yukicoder 899 / LOJ 6268 — 逆オイラー変換 (Inverse Euler)** | `1A#8` | **`Ch 03 [Adv-1]`** | Möbius Inversion on $\ln A(x)$ to Recover Generator Sequence |
| `#224` | **LOJ 6485 — LJJ 学二项式定理** | `2A#40` | **`Ch 07 [SS-1]`** | Mod-4 Roots-of-Unity Filter $(1 \pm x)^n, (1 \pm ix)^n$ |
| `#225` | **LOJ 6503 — Magic (魔术)** | `2B#B6` | **`Ch 09 [Adv-2]`** | Adjacent-Color Run Avoidance + Divide-and-Conquer NTT |
| `#226` | **LOJ 6538 — 烷基计数 加强版 加强版** | `1A#14` | **`Ch 10 [SS-2]`** | Pólya $S_3$ Ternary Tree via Newton or 12-Line Chained Relaxed Convolution |
| `#227` | **LOJ 6569 — 仙人掌计数 (Cactus Counting)** | `3A#7` | **`Ch 12 [Int-2]`** | Labeled Cactus Pointed Equation $C^\bullet = x \exp\left(C^\bullet + \frac{(C^\bullet)^2}{2(1 - C^\bullet)}\right)$ |
| `#228` | **LOJ 6671 — Unlabeled Phylogenetic Trees** | `3B#17` | **`Ch 17 [Int-1]`** | Multivariate Burnside Cycle Index + Good–Lagrange |
| `#229` | **LOJ 6703 — 小 Q 的序列** | `3B#27` | **`Ch 11 [Adv-2]`** | Derivative-Free Form 4 LIF $[x^n] H(F(x)) = [u^n] H(u)(1 - u\phi'/\phi)\phi(u)^n$ |
| `#230` | **LOJ 6728 — U 群把妹王** | `3A#12` | **`Ch 18 [Mas-2]`** | Algebraic-to-D-Finite ODE Compilation & Single-Pass $O(N)$ P-Recursive Unrolling for Biconnected / Connected Graphs |
| `#231` | **LOJ 6729 — 幂数 (Powerful Numbers)** | `5B#F9` | **`Ch 24 [Mas-1]`** | Prime-Power Bell Series Division & Dirichlet $\exp/\ln$ |
| `#232` | **QOJ 4815 — 2D Bostan–Mori / Implicit Tree** | `3A#11` | **`Ch 16 [Int-2]`** | 2D Rational Bostan–Mori $[x^n y^m] P(x,y)/Q(x,y)$ & Small-Prime Implicit Tree |
| `#233` | **QOJ 5097 / SOJ 703 — 布尔立方 (Boolean Cube)** | `5B#E7` | **`Ch 23 [Int-1]`** | Gaussian $q$-Binomial $\begin{bmatrix} n \\ k \end{bmatrix}_2$ Subspace Lattice Enumeration over $\mathbb{F}_2^n$ |
| `#234` | **QOJ 8048 — Good–Lagrange Multivariate** | `4B#30` | **`Ch 17 [Mas-2]`** | Multivariate Good–Lagrange Jacobian $\det(I - J_G(u))$ + Newton |
| `#235` | **QOJ 8528 — FPS Composition / Power Projection** | `4A#P26` | **`Ch 21 [Mas-1]`** | Kinoshita–Li $O(N \log^2 N)$ Bivariate Parity Splitting Algorithm |
| `#236` | **yukicoder 963 — 門松列列 2** | `5A#9` | **`CP-V.1`** | Alternating Permutations $\sec x + \tan x$ via ODE / CDQ |
| `#237` | **yukicoder 1080 — Delannoy / Chebyshev Sum** | `4A#P22` | **`Ch 16 [Adv-1]`** | Rational Bivariate Diagonal |
| `#238` | **yukicoder 1145 — Sum of Powers** | `2A#35` | **`Ch 02 [SS-1]`** | Newton–Girard Power Sums $-\sum_{i=1}^n \frac{-a_i x}{1 - a_i x} = -x \frac{d}{dx}\ln\prod(1 - a_i x)$ |
| `#239` | **yukicoder 1504 — Holonomic Walk** | `5A#25` | **`Ch 18 [Int-2]`** | Algebraic-to-D-Finite ODE Compilation for $O(N)$ Walk Extraction |
| `#240` | **yukicoder 1783 — Digits-Sum-Mod-10 Convolution** | `4A#P25` | **`Ch 16 [Mas-1]`** | Radix-10 Multivariate DFT + Twisted Kronecker Truncated Power $F(x)^K$ |
| `#241` | **yukicoder 1810 — Substring Avoidance** | `2B#D1` | **`Ch 08 [SS-2]`** | Single-Pattern Guibas–Odlyzko Denominator |
| `#242` | **yukicoder 1939 — Numbered Colorful Balls** | `5A#2` | **`Ch 19 [SS-1]`** | $O(NK)$ Sparse EGF Differential Recurrence Pullback |
| `#243` | **yukicoder 2104 — Fuss–Catalan Diagonal** | `4B#25` | **`CP-IV.7`** | Count lattice walks of length $n \le 2\times 10^5$ confined to $[0, H]$ with step set $\{-1, 0, +1\}$. |
| `#244` | **yukicoder 3029 — Colored Tree (FPS 24)** | `3B#5` | **`Ch 10 [Int-1]`** | $2 \times 2$ Jacobian Newton / Substitution Elimination |
| `#245` | **51Nod 1728 — 不动点** | `3A#19` | **`Ch 12 [SS-2]`** | Endofunction Cycles of Height-$\le k$ Rooted Trees $F_j(x) = x \exp(F_{j-1}(x))$ |
| `#246` | **HDU 5279 — YJC plays minecraft** | `1A#26` | **`CP-I.3`** | Count configurations of $n \le 10^5$ circularly arranged blocks into valid intervals modulo $998244353$. |
| `#247` | **HDU 5855 — Less Time, More Profit** | `2A#9` | **`Syn-12`** | Ch 05 (Rational GF Optimization) $\times$ Ch 13 (Network Matrix / Graph Algebraic Reduction) |
| `#248` | **BZOJ 3328 — PYXFIB** | `2A#41` | **`Ch 07 [SS-2]`** | Matrix Fibonacci + Bluestein / Roots-of-Unity Filter |
| `#249` | **CSES 1112 — Required Substring** | `2B#D1` | **`Syn-13`** | Ch 05 (KMP Automaton OGF) $\times$ Ch 08 (Goulden–Jackson Avoidance) $\times$ Ch 14 (Stopping-Time PGF) |
| `#250` | **Project Euler 755 — Not Zeckendorf** | `2A#10` | **`CP-I.6`** | Count ways to express $n \le 10^{13}$ as a sum of distinct Fibonacci numbers. |
| `#251` | **CF 1264D1 — Beautiful Bracket Sequence (Easy)** | `2A#3` | **`CP-II.3`** | Given a polynomial $P(x)$ of degree $N \le 2.5\times 10^5$ and shift $c$, output the coefficients of $P(x+c)$. |
| `#252` | **CF 622F — The Sum of the k-th Powers** | `2A#26` | **`CP-II.4`** | For all $k=1,\dots,n$ ($n \le 2.5\times 10^5$), count permutations of $n$ with $k$ prefix maxima and $b$ suffix maxima. |
| `#253` | **CF 961G — Partitions** | `2A#25` | **`Syn-14`** | Ch 04 (EGF $\exp$) $\times$ Ch 06 (Stirling S2 Linear Decomposition) $\times$ Ch 14 (Linearity of Expectation) |
| `#254` | **UOJ 310 — [UNR #2] 黎明前的巧克力** | `5B#F2` | **`CP-VI.6`** | Given $n \le 10^6$ integers $a_i < 2^{20}$, count pairs of disjoint subsets with equal XOR sum. |

### 6.2 Round 2 Audit Resolution Ledger (`43`-Problem Bijective Permutation from `synthesis_v1` to Canonical `Phase 1.5`)

> **Traceability Note**: The `43`-row bijective permutation below records every slot update from `synthesis_v1_curriculum.md` to the canonical Phase 1.5 curation (`critic_round2_problem_and_ladder_audit.md` §6.2), resolving all `14` hard forward-reference violations, `16` off-theme misfits, and `11` difficulty inversion pairs while preserving the exact `254`-problem bijection.

| Pool ID | Problem ID & Title | `synthesis_v1` Slot | Canonical Phase 1.5 Slot | Pedagogical & Prerequisite Resolution Rationale |
| :-: | :--- | :--- | :--- | :--- |
| `#003` | `fps_24_f` — Colored Paper / Colored Tree | `Ch 09 [SS-1]` | **`Ch 11 [SS-1]`** | Ch 11 (Lagrange Inversion $F = x \cosh F$) |
| `#010` | `fps_24_p` — Ball | `Ch 11 [SS-1]` | **`Ch 11 [Adv-1]`** | Ch 11 (Bivariate Root Shift + Residue) |
| `#011` | `fps_24_q` — Dice | `Ch 02 [SS-1]` | **`Ch 04 [Adv-2]`** | Ch 04 (Newton–Girard $\ln$ + EGF Moments) |
| `#025` | ABC 240 G — Teleporting Takahashi | `Ch 17 [SS-1]` | **`Ch 16 [Int-1]`** | Ch 16 (3D $\to$ 1D $\times$ Rotated 2D $(x+y,x-y)$) |
| `#028` | ABC 260 Ex — Colorfulness | `CP-V.1` | **`Ch 19 [Adv-1]`** | Ch 19 (Coupled D&C NTT + Truncated Taylor Shift) |
| `#034` | ABC 279 G — At Most 2 Colors | `Ch 05 [Adv-1]` | **`Ch 05 [SS-2]`** | Ch 05 ($O(N)$ Rational Transfer Stepping Stone) |
| `#035` | ABC 279 Ex — Sum of Prod of Min | `Ch 16 [Int-1]` | **`CP-III.6`** | CP-III $\to$ Ch 03 / Ch 09 (Sparse Product D&C) |
| `#036` | ABC 281 Ex — Alchemy | `CP-V.8` | **`Ch 21 [SS-1]`** | Ch 21 (Falling-Factorial EGF + All-$n$ `revert`) |
| `#040` | ABC 300 Ex — Fibonacci: Revisited | `Ch 05 [SS-2]` | **`Ch 05 [Adv-1]`** | Ch 05 (Bostan–Mori + $(1-x)$ Sparse Trick) |
| `#044` | ABC 336 G — 16 Integers | `Ch 17 [Int-2]` | **`Ch 17 [SS-2]`** | Ch 17 (De Bruijn Eulerian + MacMahon Master Theorem) |
| `#045` | ABC 345 G — Sugoroku 5 | `Ch 11 [Int-2]` | **`Ch 21 [SS-2]`** | Ch 21 (Hitting-Time PGF + Fast Composition $F(G)$) |
| `#047` | ABC 387 G — Prime Circuit | `Ch 12 [SS-1]` | **`Ch 21 [Int-1]`** | Ch 21 (Prime-Cycle Cactus Fast Composition $C(T)$) |
| `#054` | ARC 106 E — Medals | `Ch 21 [SS-2]` | **`CP-VI.5`** | CP-VI $\to$ Ch 24 (Hall's Theorem + SOS Zeta Transform) |
| `#059` | ARC 137 F — Overlaps | `Ch 09 [Mas-1]` | **`Ch 21 [Int-2]`** | Ch 21 (Implicit Algebraic + Riccati + Composition) |
| `#060` | ARC 138 E — Decreasing Subsequence | `CP-III.1` | **`Ch 09 [SS-1]`** | Ch 09 (Semi-Online Block CDQ Convolution) |
| `#064` | ARC 153 D — Sum of Sum of Digits | `CP-V.2` | **`Ch 18 [SS-2]`** | Ch 18 (Carry-Propagation D-Finite Recurrence) |
| `#068` | AGC 005 F — Many Easy Problems | `CP-VI.5` | **`CP-V.8`** | CP-V $\to$ Ch 20 (Subtree Size Rerooting `mulT`) |
| `#074` | AGC 058 D — Yet Another ABC String | `Ch 08 [Mas-2]` | **`Ch 16 [Adv-2]`** | Ch 16 (3D Rational Cluster Diagonal $[x^A y^B z^C]$) |
| `#082` | CF 240F / BZOJ 4899 — 记忆的轮廓 | `Ch 11 [Adv-1]` | **`CP-IV.8`** | CP-IV $\to$ Ch 14 (Tree DP + PGF Stopping Distribution) |
| `#084` | CF 438E — The Child and Binary Tree | `Ch 02 [Adv-1]` | **`Ch 02 [Adv-2]`** | Ch 02 (Quadratic Radical $2/(1+\sqrt{1-4C})$) |
| `#090` | CF 848E — Days of Floral Colours | `Ch 18 [Adv-1]` | **`CP-III.1`** | CP-III $\to$ Ch 09 ($4 \times 4$ Rational System + CDQ NTT) |
| `#091` | CF 891E — Lust | `Ch 21 [Int-2]` | **`Ch 02 [Mas-2]`** | Ch 02 (Product $\prod(a_i - x)$ + Formal Derivative) |
| `#108` | CF 1264D2 — Beautiful Bracket Sequence (Hard) | `Ch 19 [Adv-1]` | **`CP-V.2`** | CP-V $\to$ Ch 06 / Ch 19 (Hypergeometric Absorption / WZ) |
| `#125` | CF 1667E — Centroid Probabilities | `Ch 16 [Adv-2]` | **`Ch 18 [Adv-1]`** | Ch 18 (D-Finite Differential Recurrence + Convolution) |
| `#137` | CF Gym 102331J — Forbidden Strings | `CP-II.8` | **`Ch 08 [Mas-2]`** | Ch 08 (Multi-Pattern Goulden–Jackson Cluster Matrix) |
| `#141` | LOJ 6222 — Powers of $k$ in Permutations | `Ch 04 [Adv-2]` | **`CP-II.8`** | CP-II $\to$ Ch 04 / Ch 08 (Cycle-Length Sieve $\exp$) |
| `#146` | Luogu P3684 — 大朋友和多叉树 | `CP-III.6` | **`Ch 12 [Int-1]`** | Ch 12 (Degree-Constrained Rooted Tree Species + LIF) |
| `#154` | Luogu P4456 — [CQOI2018] 交错序列 | `Ch 19 [SS-1]` | **`Ch 17 [SS-1]`** | Ch 17 (2D Lattice Walk Moment Extraction $\sum i^a j^b$) |
| `#157` | Luogu P4705 — 玩游戏 | `Ch 21 [Int-1]` | **`Ch 02 [Adv-1]`** | Ch 02 (Newton–Girard Power Sums $\ln\prod(1-a_i x)$) |
| `#164` | Luogu P5219 — 无聊的水题 I | `Ch 12 [Int-2]` | **`Ch 13 [SS-1]`** | Ch 13 (Bounded-Degree Spanning Tree Warmup) |
| `#165` | Luogu P4389 (0-1 Subset Sum Variant) / AtCoder FPS Subset Sum via ln/exp | `Ch 02 [Mas-2]` | **`Ch 02 [SS-2]`** | Ch 02 (Subset-Sum Product $\ln/\exp$ Stepping Stone) |
| `#172` | Luogu P5366 — [SNOI2017] 遗失的答案 | `Ch 23 [Int-1]` | **`Syn-11`** | Syn-11 (Ch 08 Divisor IE $\times$ Ch 24 FWT OR/AND) |
| `#176` | Luogu P5434 — 有标号荒漠计数 | `Ch 12 [SS-2]` | **`Ch 12 [SS-1]`** | Ch 12 (Labeled Desert $\exp(C_{\text{cactus}})$ Stepping Stone) |
| `#196` | Luogu P6672 — 你的生命已如风中残烛 | `Ch 17 [SS-2]` | **`Ch 11 [Int-1]`** | Ch 11 (1D Raney's Lemma Cyclic Shift $\frac{1}{m+1}$) |
| `#201` | Luogu P7439 — [KrOI2021] 蕾切尔 | `Ch 11 [Int-1]` | **`Ch 11 [Int-2]`** | Ch 11 (Formal Residue Change of Variables) |
| `#206` | UOJ 50 — [UR #3] 链式反应 | `Ch 02 [Adv-2]` | **`Ch 09 [Mas-1]`** | Ch 09 (Non-Autonomous ODE $F'=\frac{1}{2}AF^2+1$ via CDQ) |
| `#219` | LOJ 3398 — 带加强和多项木 | `CP-IV.8` | **`Ch 17 [Int-2]`** | Ch 17 (Multivariate Implicit Tree + Good–Lagrange) |
| `#227` | LOJ 6569 — 仙人掌计数 | `Ch 12 [Int-1]` | **`Ch 12 [Int-2]`** | Ch 12 (Pointed Cactus Functional Equation) |
| `#233` | QOJ 5097 / SOJ 703 — 布尔立方 | `Syn-11` | **`Ch 23 [Int-1]`** | Ch 23 (Gaussian $q$-Binomial $\begin{bmatrix} n \\ k \end{bmatrix}_2$ Subspaces) |
| `#236` | yukicoder 963 — 門松列列 2 | `Ch 18 [SS-2]` | **`CP-V.1`** | CP-V $\to$ Ch 19 (Coupled ODE $S'=1+S^2, C'=SC$) |
| `#238` | yukicoder 1145 — Sum of Powers | `Ch 21 [SS-1]` | **`Ch 02 [SS-1]`** | Ch 02 (Newton–Girard Power Sums $-\sum \frac{-a_i x}{1-a_i x}$) |
| `#242` | yukicoder 1939 — Numbered Colorful Balls | `Ch 02 [SS-2]` | **`Ch 19 [SS-1]`** | Ch 19 ($O(NK)$ Sparse EGF Differential Recurrence) |
| `#245` | 51Nod 1728 — 不动点 | `Ch 13 [SS-1]` | **`Ch 12 [SS-2]`** | Ch 12 (Endofunction Cycles of Height-$\le k$ Trees) |
