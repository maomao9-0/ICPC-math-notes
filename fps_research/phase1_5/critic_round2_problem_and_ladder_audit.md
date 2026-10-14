# Round 3.5 Verification Critic B: Second-Pass Problem Allocation, Thematic Fit, Forward-Reference & Checkpoint Audit of `synthesis_v1_curriculum.md`

**Auditor Role**: Adversarial Problem Curation Reviewer, Prerequisite DAG Auditor & Difficulty Monotonicity Critic (Round 3.5 — Verification Critic B)  
**Target Audited**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/phase1_5/synthesis_v1_curriculum.md`  
**Cross-Referenced Against**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md`, `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md`, and `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/phase1_5/critic_3_problem_distribution.md`

---

## 1. Executive Summary & Audit Scorecard

`synthesis_v1_curriculum.md` successfully established the **24-chapter architectural spine (`Ch 01`–`Ch 24`)**, enforced the **`254 = 192 + 48 + 14` accepted-problem bijection**, and isolated all **`67` bare templates (`R-01`–`R-67`)** into footnotes.

However, a rigorous **problem-by-problem inspection of the actual mathematical solution mechanisms** of all `254` problem slots in `synthesis_v1_curriculum.md` uncovers **four severe structural bugs** that arose when the `synthesis_v1` script forced `8` problems into every chapter ladder and auto-generated the Blind Checkpoint tables:

1. **Bug Class 1 — 14 Problem-Level Forward-Reference Violations**:
   - Problems requiring **CDQ Divide-and-Conquer FFT (`Ch 09`)**, **Implicit Newton Iteration (`Ch 10`)**, **Lagrange Inversion (`Ch 11`)**, **Bivariate/Trivariate Rational Diagonals (`Ch 16`)**, **Hitting-Time PGFs (`Ch 14`)**, and **Kinoshita–Li $O(N \log^2 N)$ Fast Polynomial Composition / Power Projection (`Ch 21`)** were accidentally placed into early chapters (`Ch 02`, `Ch 08`, `Ch 09`, `Ch 11`, `Ch 12`, `Ch 18`).
   - Most glaringly:
     - `Ch 02 [Adv-2]` (`#206` `UOJ 50 — 链式反应`) solves the non-autonomous nonlinear differential equation $F'(x) = \frac{1}{2}A(x)F(x)^2 + 1$, which requires **CDQ FFT (`Ch 09`)** or **Differential Newton Iteration (`Ch 10`)**, in a chapter that only teaches basic $\ln, \exp, \sqrt{\cdot}$!
     - `Ch 02 [Mas-2]` (`#165` `Luogu P5268`) explicitly lists *"Harmonic $\ln$-$\exp$ (`Ch 03`) + Power Projection / Composition (`Ch 21`)"* in `Ch 02`!
     - `Ch 02 [SS-1]` (`#011` `fps_24_q — Dice`) and `Ch 02 [SS-2]` (`#242` `yukicoder 1939`) require **Exponential Generating Functions (`Ch 04`)**, placed two chapters before EGFs are introduced!
     - `Ch 08 [Mas-2]` (`#074` `AGC 058 D — Yet Another ABC String`) requires **3D Rational Diagonal Extraction (`Ch 16` / `Ch 17`)**, placed in `Ch 08`!
     - `Ch 12 [SS-1]` (`#047` `ABC 387 G — Prime Circuit`) requires **Kinoshita–Li $O(N \log^2 N)$ Fast Polynomial Composition (`Ch 21`)** (because prime cycle lengths have no closed-form EGF), placed as a `Stepping Stone` in `Ch 12`!

2. **Bug Class 2 — 24 Thematic Misplacements ("Quota-Padding Dumps" in `Ch 12`, `Ch 13`, `Ch 16`, `Ch 17`, `Ch 18`, `Ch 19`, `Ch 21`, `Ch 23`)**:
   - To hit `8` problems per chapter, `synthesis_v1` dumped leftover problems from unrelated chapters into `Ch 12`, `Ch 13`, `Ch 16`, `Ch 17`, `Ch 18`, `Ch 19`, `Ch 21`, and `Ch 23`:
     - **`Ch 19` (Coupled Sparse Composition, WZ Creative Telescoping & Truncated Taylor ODEs / `EI 科技`)** is the worst offender: **5 of its 8 problems (`#154`, `#120`, `#108`, `#118`, `#072`) have ZERO connection to WZ pairs, sparse composition ODEs, or `EI 科技`**! Even worse, `Ch 19 [Adv-1]` (`#108` `CF 1264D2`) is a 1-line Vandermonde absorption identity $\sum i\binom{A}{i} = A\binom{A-1}{i-1}$ (`Ch 06`) that was explicitly flagged in `R-46` as a pure Vandermonde identity!
     - **`Ch 21` (Kinoshita–Li Fast Composition, Power Projection & All-$n$ `revert`)** has **its entire first half (`SS-1`, `SS-2`, `Int-1`, `Int-2`: `#238`, `#054`, `#157`, `#091`) filled with problems that do NOT use polynomial composition, power projection, or compositional inverse at all** (they are `Ch 02` Newton–Girard power sums and `Ch 04` EGFs), while actual Kinoshita–Li composition / `revert` problems (`#047` `ABC 387 G`, `#045` `ABC 345 G`, `#061` `ARC 138 F`, `#036` `ABC 281 Ex`) were scattered into `Ch 11`, `Ch 12`, and `CP-V`!
     - **`Ch 12 [Int-2]` (`#164` `Luogu P5219 — 无聊的水题 I`)** is a basic **Prüfer Sequence bounded-degree tree EGF (`Ch 04` `Stepping Stone`)** sitting in the Cactus / Block-Cut / 2-Connected Graph chapter!
     - **`Ch 13 [SS-2]` (`#103` `CF 1109D — Sasha and Interesting Fact`)** is a basic **Cayley Forest formula $k n^{n-k-1}$ (`Ch 04` `Stepping Stone`)** sitting in the Graphical $2^{\binom{n}{2}}$ CZT & DAG/SCC chapter!
     - **`Ch 17 [SS-2]` (`#196` `Luogu P6672 — 你的生命已如风中残烛`)** is the canonical **1D Raney's Lemma Cyclic Shift $\frac{1}{m+1}$ (`Ch 11` `Stepping Stone`)** sitting in the 2D Quarter-Plane Obstinate Kernel & Multivariate Good–Lagrange chapter!
     - **`Ch 23 [Int-1]` (`#172` `Luogu P5366 — [SNOI2017] 遗失的答案`)** is a **Bitwise FWT OR+AND / Prime-Exponent Lattice (`Ch 24`)** problem sitting in the $q$-Analogue chapter, while `#233` (`QOJ 5097 / SOJ 703 — 布尔立方`), a genuine Gaussian $q$-binomial $\begin{bmatrix} n \\ k \end{bmatrix}_2$ problem, was parked in `Syn-11`!

3. **Bug Class 3 — 17 Corrupted / Hallucinated Stage-1 Problem Descriptions in Blind Checkpoints (`CP-II`–`CP-VI`) & 10 Stale Slot IDs in Section 5.2**:
   - In Section 4 of `synthesis_v1_curriculum.md`, `17` rows of the **Stage 1 ("Raw Constraint & Structural Cues")** tables in `CP-II` through `CP-VI` contain **corrupted text that describes a completely different problem (often a quarantined bare template!) than the Problem ID & Title in that row**:
     - For example, `CP-II.3` (`#251` `CF 1264D1 — Beautiful Bracket Sequence (Easy)`) has Stage-1 text *"Given a polynomial $P(x)$ of degree $N \le 2.5\times 10^5$ and shift $c$, output the coefficients of $P(x+c)$"* (the bare Taylor Shift template!), `CP-II.4` (`#252` `CF 622F — The Sum of the k-th Powers`) describes `CF 960G` (prefix/suffix maxima), `CP-V.6` (`#215` `UOJ 604 — 跳蚤电话`) describes the bare `composition_of_formal_power_series` template, `CP-VI.5` (`#068` `AGC 005 F — Many Easy Problems`) describes $q$-binomial matrix rank instead of tree Steiner subtrees, and `CP-VI.8` (`#180` `Luogu P5643 — 随机游走`) describes a Dirichlet series prefix sum instead of random walk on a tree!
   - Additionally, in **Section 5.2 (Revisited Dual-Perspective Cross-Reference Index)**, `10` of the `12` rows list a `Primary Slot (#ID)` where the `#ID` and slot belong to a different problem than the named `Problem ID & Title`.

4. **Bug Class 4 — 1 Cross-Judge Title Conflation in the 254-Problem Pool (`#179` vs `#219`)**:
   - `#179` (`Luogu P5597 — 【XR-4】复读 / 带加强和多项木` in `Ch 10 [Adv-1]`) and `#219` (`LOJ 3398 — 带加强和多项木` in `CP-IV.8`) both reference `带加强和多项木`. While `Luogu P5597` (`【XR-4】复读`) is an unlabeled $k$-ary tree automaton minimization problem and `LOJ 3398` (`带加强和多项木`, `2020 集训队论文`) is the multivariate Good–Lagrange / Newton tree problem, their titles were conflated in `#179` and must be cleanly separated.

### Summary Audit Scorecard (`synthesis_v1` vs. Target `synthesis_v2`)

| Audit Dimension | `synthesis_v1_curriculum.md` Status | Target `synthesis_v2` Status (via Section 6 Patch) |
| :--- | :-: | :-: |
| **1. Forward-Reference Violations Across 192 Ladder + 48 Checkpoint Slots** | **14 violations** (`Ch 02` $\times 4$, `Ch 08` $\times 1$, `Ch 09` $\times 2$, `Ch 11` $\times 2$, `Ch 12` $\times 3$, `Ch 18` $\times 2$) | **0 violations** |
| **2. Thematic Misplacements Across 24 Chapter Ladders** | **24 misplaced slots** (concentrated in `Ch 12, 13, 16, 17, 18, 19, 21, 23`) | **0 misplaced slots** |
| **3. Difficulty Monotonicity (`SS` $\to$ `Int` $\to$ `Adv` $\to$ `Mas`)** | **9 inversions** (e.g., `Luogu P5268` (`SS`) at `Ch 02 Mas-2`, `ABC 387 G` (`Adv`) at `Ch 12 SS-1`, `fps_24_q` (`Adv`) at `Ch 02 SS-1`) | **100% monotone across all 24 chapters** |
| **4. Corrupted Stage-1 Descriptions in Blind Checkpoints (`CP-I`–`CP-VI`)** | **17 corrupted rows** in `CP-II`..`CP-VI` | **0 corrupted rows** (exact replacement text provided in §3.2) |
| **5. Stale Slot/ID References in Revisited Table (§5.2)** | **10 mismatched `#ID`/Slot pairs** in §5.2 | **0 mismatches** (exact corrected table provided in §3.3) |
| **6. 254-Problem Bijection & 67-Template Quarantine** | **Preserved** (`192 + 48 + 14 = 254`, `67` templates) | **Preserved 100%** (exact 43-problem permutation on `#001`–`#254`) |

---

## 2. Investigation 1: Thematic Fit & Solution-Mechanism Audit of All 192 Chapter Ladder Problems (`Ch 01`–`Ch 24`)

Below is the chapter-by-chapter audit of the `192` ladder problems in `synthesis_v1_curriculum.md`. Chapters with zero thematic or prerequisite defects (`Ch 01`, `Ch 03`, `Ch 04`, `Ch 05`, `Ch 06`, `Ch 07`, `Ch 10`, `Ch 14`, `Ch 15`, `Ch 20`, `Ch 22`, `Ch 24`) are summarized first, followed by deep-dive tables on every chapter containing a thematic misplacement or forward-reference violation (`Ch 02`, `Ch 08`, `Ch 09`, `Ch 11`, `Ch 12`, `Ch 13`, `Ch 16`, `Ch 17`, `Ch 18`, `Ch 19`, `Ch 21`, `Ch 23`).

### 2.1 Chapters with Clean Thematic Fit (`Ch 01, 03, 04, 05, 06, 07, 10, 14, 15, 20, 22, 24`)

- **`Ch 01` (Formal Ring $K[[x]]$, Cauchy Convolution & $O(N \log N)$ Newton Inversion)**: All 8 problems (`#019`, `#043`, `#004`, `#077`, `#049`, `#097`, `#066`, `#107`) genuinely test 1D OGF convolution, reverse-indexing cross-correlation, D&C product trees, and 1D series inversion $1/F(x)$ using only `Ch 01` tools.
- **`Ch 03` (Multiset Construction, Partitions, Euler Transform, Ferrers/Durfee & Pólya)**: All 8 problems (`#001`, `#188`, `#153`, `#009`, `#223`, `#221`, `#150`, `#159`) genuinely test partition OGFs, bounded subset products, harmonic $\ln/\exp$, Durfee squares, and Burnside/Pólya cycle indices.
- **`Ch 04` (Labeled Species, EGFs, $\exp/\ln$ Bridge & Prüfer Trees)**: All 8 problems (`#002`, `#007`, `#161`, `#008`, `#083`, `#141`, `#041`, `#174`) are 100% thematic labeled EGF / Prüfer / tree-component problems.
- **`Ch 05` (Rational GFs, Bostan–Mori & Berlekamp–Massey)**: All 8 problems (`#104`, `#040`, `#187`, `#069`, `#034`, `#081`, `#177`, `#073`) genuinely use rational OGFs, polynomial division, Bostan–Mori parity splitting, and Berlekamp–Massey LFSR synthesis. *(Only a 2-slot difficulty swap `#034 <-> #040` is needed; see §4.)*
- **`Ch 06` (Binomial Sums, Vandermonde, Stirling Numbers, Taylor Shift & Consecutive Lagrange)**: All 8 problems (`#005`, `#055`, `#193`, `#080`, `#094`, `#096`, `#098`, `#109`) are 100% thematic.
- **`Ch 07` (Roots of Unity Filter, Circulant Matrices, Bluestein CZT & Cyclic Convolutions)**: All 8 problems (`#224`, `#248`, `#178`, `#143`, `#147`, `#012`, `#092`, `#168`) are 100% thematic.
- **`Ch 10` (Implicit Functional Equations, Coupled Fréchet Newton Iteration & Otter's Dissimilarity)**: All 8 problems (`#186`, `#226`, `#244`, `#013`, `#179`, `#126`, `#191`, `#192`) genuinely solve implicit functional equations via 1D/coupled/Pólya Newton iteration or Otter's dissimilarity theorem.
- **`Ch 14` (Probability Generating Functions, Renewal, Stopping Times, Min–Max IE & Martingales)**: All 8 problems (`#115`, `#026`, `#156`, `#071`, `#148`, `#209`, `#039`, `#113`) are 100% thematic stochastic/PGF problems.
- **`Ch 15` (1D Bounded Lattice Walks, Reflection Principle, Small-Steps Kernel Method & Denominator-Gcd)**: All 8 problems (`#105`, `#070`, `#220`, `#140`, `#128`, `#134`, `#076`, `#210`) are 100% thematic 1D lattice-walk / reflection / kernel-method problems.
- **`Ch 20` (Tellegen's Transposition Principle `mulT`, Multipoint Evaluation, Fast Interpolation & Sampling Shift)**: All 8 problems (`#050`, `#197`, `#127`, `#167`, `#208`, `#202`, `#181`, `#217`) are 100% thematic interpolation / multipoint evaluation / transposed convolution / sampling-shift problems.
- **`Ch 22` (Tree DP with Generating Functions: HLD Chain Merging, Static Top Trees & Zero-Divisor Pairs)**: All 8 problems (`#031`, `#124`, `#046`, `#198`, `#149`, `#136`, `#166`, `#145`) are 100% thematic Tree DP + FPS problems.
- **`Ch 24` (Bitwise Algebras FWT/SOS, Set Power Series $\mathcal{R}_n$ & Dirichlet GFs)**: All 8 problems (`#216`, `#020`, `#027`, `#042`, `#110`, `#207`, `#231`, `#038`) are 100% thematic FWT/SPS/Dirichlet problems.

---

### 2.2 Deep-Dive Audit of Defective Chapter Ladders (`Ch 02, 08, 09, 11, 12, 13, 16, 17, 18, 19, 21, 23`)

#### 1. `Ch 02` (Formal Calculus, Newton $\ln/\exp/\sqrt{\cdot}/P^\alpha$, $O(NK)$ Sparse Power ODEs & Newton–Girard Sums)
**4 of 8 slots have forward-reference or difficulty-inversion defects**:

| Slot | Current Problem (`synthesis_v1`) | Actual Mathematical Solution Mechanism | Defect Type | Required Action for `synthesis_v2` |
| :-: | :--- | :--- | :--- | :--- |
| **SS-1** | `#011` `fps_24_q — Dice` (`1B#18`) | Computes $\sum_{i=1}^N A_i^k$ via $-\ln\prod(1-A_i x)$ (`Ch 02`) **AND** combines with **EGF** moment extraction $\sum \binom{M}{k}\dots$ (`Ch 04`). Rated `Intermediate/Advanced` in `problem_archive.md`. | **Forward Ref (`Ch 04` EGF) + Difficulty Inversion** | Move `#011` to `Ch 04 [Adv-2]`; replace with `#238` **`yukicoder 1145 — Sum of Powers`** (currently misplaced at `Ch 21 SS-1`), which is the pure `Ch 02` Newton–Girard $-\sum \frac{-a_i x}{1-a_i x}$ `Stepping Stone`! |
| **SS-2** | `#242` `yukicoder 1939 — Numbered Colorful Balls` (`5A#2`) | Labeled balls of $C$ colors with $O(NK)$ sparse recurrence on **Exponential Generating Functions** (`Ch 04` + `Ch 19`). | **Forward Ref (`Ch 04` EGF)** | Move `#242` to `Ch 19 [SS-1]`; replace with `#165` **`Luogu P5268`** (rated `Stepping Stone` in `problem_archive.md` `5B#C3` for basic subset-sum product $\ln/\exp$). |
| **Adv-2** | `#206` `UOJ 50 — [UR #3] 链式反应` (`2A#46`) | Solves the non-autonomous nonlinear differential equation $F'(x) = \frac{1}{2}A(x)F(x)^2 + 1$ for binary tree cascades via **CDQ Divide-and-Conquer FFT (`Ch 09`)** or **Implicit Differential Newton Iteration (`Ch 10`)**! | **Severe Forward Ref (`Ch 09`/`Ch 10`)** | Move `#206` to **`Ch 09 [Mas-1]`**; bring `#157` **`Luogu P4705 — 玩游戏`** (currently misplaced in `Ch 21 Int-1`, testing Newton–Girard power sums $\ln\prod(1-a_i x)$ + convolution) into `Ch 02 [Adv-1]`. |
| **Mas-2** | `#165` `Luogu P5268` (`5B#C3`) | Listed as *"Harmonic $\ln$-$\exp$ + Power Projection / Composition"*, while `problem_archive.md` rates `#165` as a **`Stepping Stone`**! | **Difficulty Inversion + Forward Ref** | Demote `#165` to `Ch 02 [SS-2]` (scoped strictly to basic $\ln$-$\exp$ subset product) and place `#091` **`CF 891E — Lust`** (polynomial product $\prod(a_i-x)$ + formal derivative, moved from `Ch 21 Int-2`) at `Ch 02 [Mas-2]`. |

#### 2. `Ch 08` (Combinatorial Sieves, Binomial Inversion, Connected-Component IE & Goulden–Jackson Cluster Method)
**1 slot has a severe forward-reference defect**:

| Slot | Current Problem (`synthesis_v1`) | Actual Mathematical Solution Mechanism | Defect Type | Required Action for `synthesis_v2` |
| :-: | :--- | :--- | :--- | :--- |
| **Mas-2** | `#074` `AGC 058 D — Yet Another ABC String` (`2B#D7`) | Avoids cyclic substrings `ABC, BCA, CAB`; the cluster OGF is the **trivariate rational function** $\frac{1-xyz}{1-(x+y+z)+2xyz}$, and extracting $[x^A y^B z^C]$ requires **Multivariate Diagonal / Binomial Coefficient Extraction (`Ch 16`)**! | **Severe Forward Ref (`Ch 16`)** | Move `#074` to **`Ch 16 [Adv-2]`** (where it is a premier trivariate rational diagonal + cluster showcase); move `#137` **`CF Gym 102331J — Forbidden Strings`** (Multi-Pattern Aho–Corasick Goulden–Jackson Cluster Matrix) into `Ch 08 [Mas-2]`. |

#### 3. `Ch 09` (Causal Recurrences: CDQ Divide-and-Conquer FFT & Online Relaxed Convolution)
**2 slots have forward-reference & thematic defects**:

| Slot | Current Problem (`synthesis_v1`) | Actual Mathematical Solution Mechanism | Defect Type | Required Action for `synthesis_v2` |
| :-: | :--- | :--- | :--- | :--- |
| **SS-1** | `#003` `fps_24_f — Colored Paper` (`1A#2`) | Part 1 is $(e^x)^k \sinh^m x$ (`Ch 04`); Part 2 ("Colored Tree") solves the implicit equation $F(x) = x \cosh F(x)$ via **Implicit Newton Iteration (`Ch 10`)** or **Lagrange Inversion (`Ch 11`)**. It does **not** use CDQ FFT or Online Relaxed Convolution! | **Forward Ref (`Ch 10`/`Ch 11`) + Thematic Misfit** | Move `#003` to **`Ch 11 [SS-1]`**; move `#060` **`ARC 138 E — Decreasing Subsequence`** (semi-online block CDQ convolution) into `Ch 09 [SS-1]`. |
| **Mas-1** | `#059` `ARC 137 F — Overlaps` (`3B#22`) | Solves an **implicit algebraic equation via Newton Iteration (`Ch 10`) / Form-4 Derivative-Free LIF (`Ch 11`) / Riccati ODE + Kinoshita–Li Composition (`Ch 21`)**. Zero CDQ / Relaxed Convolution! | **Severe Forward Ref (`Ch 10`/`Ch 11`/`Ch 21`)** | Move `#059` to **`Ch 21 [Int-2]`**; replace in `Ch 09 [Mas-1]` with `#206` **`UOJ 50 — 链式反应`** (CDQ FFT on $F' = \frac{1}{2}A F^2 + 1$). |

#### 4. `Ch 11` (Formal Laurent Series $K((x))$, Formal Residues, Raney's Lemma & Lagrange–Bürmann Inversion)
**1 slot has a severe forward-reference defect**:

| Slot | Current Problem (`synthesis_v1`) | Actual Mathematical Solution Mechanism | Defect Type | Required Action for `synthesis_v2` |
| :-: | :--- | :--- | :--- | :--- |
| **Int-2** | `#045` `ABC 345 G — Sugoroku 5` (`5B#B2`) | Computes hitting-time distribution on $[0, N]$ by factoring into **Hitting-Time PGF (`Ch 14`) + Kinoshita–Li $O(N \log^2 N)$ Fast Polynomial Composition $F(G(x))$ (`Ch 21`)**! Its wave tag `5B#B2` literally comes from Wave 5B Section 2 (Fast Composition)! | **Severe Forward Ref (`Ch 14` & `Ch 21`)** | Move `#045` to **`Ch 21 [SS-2]`**; replace in `Ch 11` with `#196` **`Luogu P6672 — 你的生命已如风中残烛`** (currently misplaced in `Ch 17 SS-2`, which is pure 1D Raney's Lemma Cyclic Shift $\frac{1}{m+1}$!). |

#### 5. `Ch 12` (Pointed Species $\vartheta=xD$: Cacti, Deserts, Block-Cut Trees & 2-Connected Graphs)
**2 slots have severe thematic / forward-reference defects, plus 3 slots require single-$n$ vs all-$n$ scoping notes**:

| Slot | Current Problem (`synthesis_v1`) | Actual Mathematical Solution Mechanism | Defect Type | Required Action for `synthesis_v2` |
| :-: | :--- | :--- | :--- | :--- |
| **SS-1** | `#047` `ABC 387 G — Prime Circuit` (`4A#P25`) | Counts connected graphs where every cycle has prime length ($N \le 2.5 \times 10^5$). Because prime cycles have no closed-form EGF, computing $C(T(x)) \bmod x^{N+1}$ requires **Kinoshita–Li $O(N \log^2 N)$ Fast Polynomial Composition (`Ch 21`)**! Moreover, `problem_archive.md` rates `#047` as `Advanced`! | **Severe Forward Ref (`Ch 21`) + Difficulty Inversion** | Move `#047` to **`Ch 21 [Int-1]`**; promote `#176` (`Luogu P5434 — 有标号荒漠计数`) to `Ch 12 [SS-1]`. |
| **Int-2** | `#164` `Luogu P5219 — 无聊的水题 I` (`3A#3`) | Counts labeled trees on $n$ vertices with maximum degree $m$ via **Prüfer sequence bounded-degree EGF** $[x^{n-2}](\sum_{i=0}^{m-1} \frac{x^i}{i!})^n$. Rated `Stepping Stone` in `problem_archive.md`. Has **zero** cactus, desert, or biconnected graph structure! | **Blatant Thematic Misfit (Pure Prüfer Tree)** | Move `#164` to **`Ch 13 [SS-1]`** (spanning tree warmup); bring `#245` **`51Nod 1728 — 不动点`** (functional graphs = cycles of rooted trees) into `Ch 12 [SS-2]` and `#146` **`Luogu P3684 — 大朋友和多叉树`** into `Ch 12 [Int-1]`. |
| **Adv-2, Mas-1, Mas-2** | `#016` (`fps_24_w`), `#183` (`Luogu P5827`), `#184` (`Luogu P5828`) | Pointed Block-Cut Tree $\ln(R(x)/x) = B'(R(x))$. For a **single $n$**, $[x^n]B(x)$ is extracted in $O(n \log n)$ via `Ch 11` Lagrange Inversion; for **all $1 \le k \le n$**, it requires `Ch 21` `compositional_inverse`. | **Pedagogical Scoping Note Needed** | Explicitly annotate in `Ch 12` that `Ch 12` solves the **single-$n$ $O(n \log n)$ Lagrange Inversion formulation** (and $O(n^2)$ / Newton subtasks), while simultaneous all-$n$ `revert` is revisited in `Ch 21.4` (and `Section 5.2` Row 9). |

#### 6. `Ch 13` (Graphical GFs $2^{\binom{n}{2}}$ CZT, Eulerian/Bipartite, DAGs, SCCs & Matrix-Tree over FPS)
**1 slot (`SS-1`) is a functional-graph problem belonging in `Ch 12`**:

| Slot | Current Problem (`synthesis_v1`) | Actual Mathematical Solution Mechanism | Defect Type | Required Action for `synthesis_v2` |
| :-: | :--- | :--- | :--- | :--- |
| **SS-1** | `#245` `51Nod 1728 — 不动点` (`3A#19`) | Counts endofunctions $f^k(x) = f^{k+1}(x)$, i.e., cycles of rooted trees of height $\le k$, via iterated $F_j(x) = x \exp(F_{j-1}(x))$. Uses **zero** $2^{\binom{n}{2}}$ CZT, DAG IE, or Matrix-Tree! | **Thematic Misfit (Belongs in `Ch 12` Functional Graphs)** | Move `#245` to **`Ch 12 [SS-2]`** (where functional graphs = cycles of rooted trees live), and place `#164` (`Luogu P5219`) at `Ch 13 [SS-1]` as the degree-constrained spanning-tree warmup before `13.4` Matrix-Tree! |

#### 7. `Ch 16` (5-Ring Bivariate Hierarchy, 2D Bostan–Mori & Furstenberg Diagonals)
**1 slot is a pure 1D OGF problem with zero bivariate/diagonal content**:

| Slot | Current Problem (`synthesis_v1`) | Actual Mathematical Solution Mechanism | Defect Type | Required Action for `synthesis_v2` |
| :-: | :--- | :--- | :--- | :--- |
| **Int-1** | `#035` `ABC 279 Ex — Sum of Prod of Min` (`4A#P4`) | Evaluates $[x^M] \prod_{i=1}^N \frac{1-(i+1)x^i+ix^{i+1}}{(1-x)^2}$ in $O(N\sqrt{N})$ via sparse 1D polynomial multiplication (`Ch 03` Pentagonal/sparse product). Has **zero** bivariate variables, zero 2D Bostan–Mori, and zero diagonal extraction! | **Blatant Thematic Misfit (1D OGF)** | Move `#035` to `CP-III.6`; replace in `Ch 16 [Int-1]` with **`#025` `ABC 240 G — Teleporting Takahashi`** (3D walk decoupled into 1D $\times$ rotated 2D $(x+y, x-y)$ bivariate binomials), and move **`#074` `AGC 058 D`** (trivariate rational diagonal $[x^A y^B z^C] P/Q$) into `Ch 16 [Adv-2]`. |

#### 8. `Ch 17` (2D Quarter-Plane Obstinate Kernel, Multivariate Good–Lagrange & MacMahon's Master Theorem)
**2 of 8 slots (`SS-1` and `SS-2`) do NOT belong in `Ch 17`**:

| Slot | Current Problem (`synthesis_v1`) | Actual Mathematical Solution Mechanism | Defect Type | Required Action for `synthesis_v2` |
| :-: | :--- | :--- | :--- | :--- |
| **SS-1** | `#025` `ABC 240 G — Teleporting Takahashi` (`4A#P9`) | Unbounded 3D Manhattan walk decoupled into 1D walk $\times$ rotated 2D $(x+y, x-y)$ walk. Has **no quadrant boundary** and **no obstinate kernel or Good–Lagrange**! | **Thematic Misfit (Belongs in `Ch 16` Bivariate Decoupling)** | Move `#025` to **`Ch 16 [Int-1]`**; place **`#154` `Luogu P4456 — [CQOI2018] 交错序列`** (2D constrained step walk moment extraction $\sum i^a j^b$) at `Ch 17 [SS-1]`. |
| **SS-2** | `#196` `Luogu P6672 — [清华集训2016] 你的生命已如风中残烛` (`4B#5`) | Pure **1D Raney's Lemma Cyclic Shift $\frac{1}{m+1}$** (`Wave 4B#5`, rated `Stepping Stone`)! Has **zero** 2D lattice walk, zero quarter-plane kernel, and zero multivariate Good–Lagrange! | **Blatant Thematic Misfit (Pure `Ch 11` 1D Raney's Lemma)** | Move `#196` to **`Ch 11 [Int-1]`**; bring **`#219` `LOJ 3398 — 带加强和多项木`** (Multivariate Implicit Tree System + Good–Lagrange Jacobian $\det(I - J_G(u))$, currently in `CP-IV.8`) into `Ch 17 [Int-2]`. |

#### 9. `Ch 18` (Holonomic D-Finite Theory, Weyl Algebra, Algebraic-to-ODE Compilation & $O(N)$ P-Recursive Unrolling)
**3 slots have thematic or forward-reference defects**:

| Slot | Current Problem (`synthesis_v1`) | Actual Mathematical Solution Mechanism | Defect Type | Required Action for `synthesis_v2` |
| :-: | :--- | :--- | :--- | :--- |
| **SS-2** | `#236` `yukicoder 963 — 門松列列 2` (`2B#F4`) | Counts alternating sequences via Eulerian secant/tangent EGF $\sec x + \tan x$ and coupled Riccati ODE $S'=1+S^2, C'=SC$. | **Thematic Shift** | Swap `#236` into **`CP-V.1` ($\to$ `Ch 19.2` Coupled Riccati ODE)** and bring **`#064` `ARC 153 D — Sum of Sum of Digits`** (carry-propagation D-Finite recurrence) into `Ch 18 [SS-2]`. |
| **Adv-1** | `#090` `CF 848E — Days of Floral Colours` (`2A#47`) | Solved by $4 \times 4$ matrix rational OGF denominator + CDQ NTT (`Ch 05` / `Ch 09`), **not** D-Finite non-constant-coefficient P-recursive ODE! | **Thematic Misfit (`Ch 05`/`Ch 09`)** | Move `#090` to **`CP-III.1` ($\to$ `Ch 09` CDQ NTT)**; replace in `Ch 18 [Adv-1]` with **`#125` `CF 1667E — Centroid Probabilities`** (D-Finite tree centroid differential recurrence). |
| **Mas-2** | `#230` `LOJ 6728 — U 群把妹王` (`3A#12`) | Description lists *"Power Projection / Kinoshita–Li (`Ch 21`) / Algebraic-to-ODE $O(n)$ Extraction (`Ch 18`)"*. | **Forward-Ref Mention (`Ch 21`)** | Scope the `Ch 18 [Mas-2]` description strictly to **Algebraic-to-D-Finite ODE Compilation & $O(n)$ P-Recursive Extraction**. |

#### 10. `Ch 19` (Coupled Sparse Composition, WZ Creative Telescoping & Truncated Taylor ODEs / `EI 科技`)
**CRITICAL AUDIT FINDING — 5 of the 8 slots in `Ch 19` were unrelated quota-padding dumps or missing their ODE pullback framing**:

| Slot | Current Problem (`synthesis_v1`) | Actual Mathematical Solution Mechanism | Defect Type | Required Action for `synthesis_v2` |
| :-: | :--- | :--- | :--- | :--- |
| **SS-1** | `#154` `Luogu P4456 — [CQOI2018] 交错序列` (`5A#7`) | Bivariate 2D walk automaton $(1+y, x)$ + $2 \times 2$ matrix binary exponentiation in $O(k^3 \log n)$. Uses **zero** ODEs, zero WZ, and zero `EI 科技`! | **Blatant Thematic Misfit** | Move `#154` to `Ch 17 [SS-1]`; replace with **`#242` `yukicoder 1939 — Numbered Colorful Balls`** ($O(NK)$ sparse EGF differential recurrence pullback, moved from `Ch 02 SS-2`). |
| **SS-2** | `#120` `CF 1548C — The Three Little Pigs` (`2A#7`) | Divides $(1+x)^{3N+3}-1$ by $(1+x)^3-1 = x^3+3x^2+3x$ in $O(N)$. | **Missing ODE Pullback Framing** | Reframe `#120` explicitly as the **19.1 Stepping Stone for Chain-Rule Sparse Composition Pullback** $H(x) = \frac{u^{N+1}-1}{u-1}\big\rvert_{u=(1+x)^3}$. |
| **Adv-1** | `#108` `CF 1264D2 — Beautiful Bracket Sequence (Hard)` (`4A#P12`) | **1-line Vandermonde absorption identity** $i\binom{A}{i} = A\binom{A-1}{i-1}$ + prefix sums (`Ch 06`)! Even `R-46` in Section 6.1 admits `CF 1264D2` collapses to a 1-line Vandermonde sum! | **Egregious Thematic Misfit (Pure `Ch 06` Vandermonde)** | Evict `#108` from `Ch 19 [Adv-1]` to `CP-V.2`; replace with **`#028` `ABC 260 Ex — Colorfulness`** (Coupled D&C NTT + Truncated Taylor Shift). |
| **Adv-2** | `#118` `CF 1515E — Phoenix and Computers` (`2B#B1`) | Bivariate EGF $\frac{1}{1-x(e^y-1)}$ + $O(N^2)$ D-Finite recurrence. | **Needs Explicit 19.1 Framing** | Frame explicitly under **19.1 Sparse Composition Pullback** $F(G(y)) = (1 - x(e^y-1))^{-1}$ + Row ODE. |
| **Mas-1** | `#072` `AGC 043 D — Merge Triplets` (`2B#C3`) | Counts permutations with $1,2,3$-cycles via $\exp(xy + \frac{x^2}{2}y^{-1} + \frac{x^3}{3})$ by differentiating to get a **coupled sparse differential recurrence** $\partial_x F = (y + xy^{-1} + x^2)F$ in $O(N^2)$! | **Needs Explicit 19.1 ODE Rewrite** | Rewrite the `Core Mathematical Mechanism` column of `#072` to **"Sparse Composition ODE Pullback $F(x,y) = \exp(xy + \frac{x^2}{2}y^{-1} + \frac{x^3}{3}) \implies \partial_x F = (y + xy^{-1} + x^2)F$ (`19.1`)"**. |

#### 11. `Ch 21` (Kinoshita–Li $O(N \log^2 N)$ Fast Composition, Power Projection & All-$n$ `revert`)
**CRITICAL AUDIT FINDING — Slots `SS-1`, `SS-2`, `Int-1`, `Int-2` of `Ch 21` did NOT use polynomial composition, power projection, or compositional inverse at all**:

| Slot | Current Problem (`synthesis_v1`) | Actual Mathematical Solution Mechanism | Defect Type | Required Action for `synthesis_v2` |
| :-: | :--- | :--- | :--- | :--- |
| **SS-1** | `#238` `yukicoder 1145 — Sum of Powers` (`2A#35`) | Computes $\sum_{i=1}^n a_i^k$ via $-\sum \frac{-a_i x}{1-a_i x} = -x \frac{d}{dx}\ln\prod(1-a_i x)$ (`Ch 02`). Zero composition, zero power projection, zero `revert`! | **Blatant Thematic Misfit (Pure `Ch 02` Newton–Girard)** | Move `#238` to **`Ch 02 [SS-1]`**; replace `Ch 21 [SS-1]` with **`#036` `ABC 281 Ex — Alchemy`** (all-$n$ `compositional_inverse` / falling-factorial EGF, from `CP-V.8`). |
| **SS-2** | `#054` `ARC 106 E — Medals` (`2A#35`) | Binary search + Hall's Marriage Theorem + Zeta Transform (`Ch 24`). Zero polynomial composition, zero power projection, zero `revert`! | **Blatant Thematic Misfit (`Ch 24` Hall + SOS)** | Move `#054` to **`CP-VI.5` ($\to$ `Ch 24.1`)**; replace `Ch 21 [SS-2]` with **`#045` `ABC 345 G — Sugoroku 5`** (Hitting-time PGF + Fast Polynomial Composition $F(G(x))$, moved from `Ch 11 Int-2`). |
| **Int-1** | `#157` `Luogu P4705 — 玩游戏` (`1A#24`) | Computes $\frac{1}{nm}\sum (a_i+b_j)^k$ via Newton–Girard $\ln\prod(1-a_i x)$ (`Ch 02`) + 1D convolution. Zero composition or power projection! | **Blatant Thematic Misfit (`Ch 02`)** | Move `#157` to **`Ch 02 [Adv-1]`**; replace `Ch 21 [Int-1]` with **`#047` `ABC 387 G — Prime Circuit`** (Cactus Prime-Cycle EGF requiring $O(N \log^2 N)$ Fast Composition $C(T(x))$, moved from `Ch 12 SS-1`). |
| **Int-2** | `#091` `CF 891E — Lust` (`1A#16`) | Computes $\prod_{i=1}^n (a_i - x)$ in $O(n^2)$ ($n \le 5000$) + derivative extraction (`Ch 02`). Zero composition or power projection! | **Blatant Thematic Misfit (`Ch 02`)** | Move `#091` to **`Ch 02 [Mas-2]`**; replace `Ch 21 [Int-2]` with **`#059` `ARC 137 F — Overlaps`** (Implicit algebraic equation + Riccati ODE + Fast Composition, moved from `Ch 09 Mas-1`). |

#### 12. `Ch 23` ($q$-Analogues, Gaussian Binomials, $q$-Pentagonal, $q$-Lucas & MacWilliams / Krawtchouk)
**1 slot is a Bitwise FWT / Number-Theoretic Lattice problem with zero $q$-analogue content**:

| Slot | Current Problem (`synthesis_v1`) | Actual Mathematical Solution Mechanism | Defect Type | Required Action for `synthesis_v2` |
| :-: | :--- | :--- | :--- | :--- |
| **Int-1** | `#172` `Luogu P5366 — [SNOI2017] 遗失的答案` (`5B#E5`) | Encodes prime-power exponents between $\gcd=G$ and $\operatorname{lcm}=L$ as bitmasks ($\le 8$ primes) and runs **Bitwise FWT OR + AND Subset Convolution (`Ch 24`)**! Has **zero** $q$-binomial or $\mathbb{F}_q$ subspace content! | **Blatant Thematic Misfit (`Ch 24` Bitwise FWT)** | Swap `#172` (`Luogu P5366`) with **`#233` `QOJ 5097 / SOJ 703 — 布尔立方 (Boolean Cube)`** (currently in `Syn-11`), which is a genuine **Gaussian $q$-binomial $\begin{bmatrix} n \\ k \end{bmatrix}_2$ subspace problem (`Wave 5B#E7`)**! Place `#172` in `Syn-11` (bridging `Ch 08` Divisor IE $\times$ `Ch 24` Bitwise FWT OR/AND + Prime Lattice). |

---

## 3. Investigation 2: Complete Problem-Level Forward-Reference Audit & Blind Checkpoint (`CP-I`–`CP-VI`) Corruption Audit

### 3.1 Complete Ledger of All 14 Forward-Reference Violations in `synthesis_v1_curriculum.md`

| # | Current Slot (`synthesis_v1`) | Problem ID & Title | Unmet Prerequisite Required by Solution | Taught In | Fix in `synthesis_v2` |
| :-: | :--- | :--- | :--- | :-: | :--- |
| 1 | `Ch 02 [SS-1]` | `#011` `fps_24_q — Dice` | Exponential Generating Function (EGF) moment convolution | **Ch 04** | Move `#011` to `Ch 04 [Adv-2]`; put `#238` (`yukicoder 1145`) at `Ch 02 [SS-1]` |
| 2 | `Ch 02 [SS-2]` | `#242` `yukicoder 1939 — Numbered Colorful Balls` | Exponential Generating Functions (EGF) + $O(NK)$ sparse recurrence | **Ch 04 / Ch 19** | Move `#242` to `Ch 19 [SS-1]`; put `#165` (`Luogu P5268`) at `Ch 02 [SS-2]` |
| 3 | `Ch 02 [Adv-2]` | `#206` `UOJ 50 — [UR #3] 链式反应` | Non-autonomous ODE $F' = \frac{1}{2}A F^2 + 1$ via CDQ FFT or Differential Newton | **Ch 09 / Ch 10** | Move `#206` to `Ch 09 [Mas-1]`; put `#157` (`Luogu P4705`) at `Ch 02 [Adv-1]` |
| 4 | `Ch 02 [Mas-2]` | `#165` `Luogu P5268 — Subset-Sum Product` | Listed as *"Harmonic $\ln$-$\exp$ (`Ch 03`) + Power Projection (`Ch 21`)"* | **Ch 03 / Ch 21** | Demote `#165` to `Ch 02 [SS-2]` (basic $\ln$-$\exp$); put `#091` (`CF 891E`) at `Ch 02 [Mas-2]` |
| 5 | `Ch 08 [Mas-2]` | `#074` `AGC 058 D — Yet Another ABC String` | Trivariate rational diagonal extraction $[x^A y^B z^C] \frac{1-xyz}{1-(x+y+z)+2xyz}$ | **Ch 16** | Move `#074` to `Ch 16 [Adv-2]`; put `#137` (`CF Gym 102331J`) at `Ch 08 [Mas-2]` |
| 6 | `Ch 09 [SS-1]` | `#003` `fps_24_f — Colored Paper` | Part 2 solves $F = x \cosh F$ via Implicit Newton (`Ch 10`) or LIF (`Ch 11`) | **Ch 10 / Ch 11** | Move `#003` to `Ch 11 [SS-1]`; put `#060` (`ARC 138 E`) at `Ch 09 [SS-1]` |
| 7 | `Ch 09 [Mas-1]` | `#059` `ARC 137 F — Overlaps` | Implicit Algebraic Newton (`Ch 10`) / Form-4 LIF (`Ch 11`) / Composition (`Ch 21`) | **Ch 10 / 11 / 21** | Move `#059` to `Ch 21 [Int-2]`; put `#206` (`UOJ 50`) at `Ch 09 [Mas-1]` |
| 8 | `Ch 11 [Int-2]` | `#045` `ABC 345 G — Sugoroku 5` | Hitting-Time PGF (`Ch 14`) + Kinoshita–Li Fast Composition $F(G(x))$ (`Ch 21`) | **Ch 14 & Ch 21** | Move `#045` to `Ch 21 [SS-2]`; put `#196` (`Luogu P6672`) at `Ch 11 [Int-1]` |
| 9 | `Ch 12 [SS-1]` | `#047` `ABC 387 G — Prime Circuit` | Kinoshita–Li $O(N \log^2 N)$ Fast Composition $C(T(x))$ on prime-cycle EGF | **Ch 21** | Move `#047` to `Ch 21 [Int-1]`; put `#176` (`Luogu P5434`) at `Ch 12 [SS-1]` |
| 10 | `Ch 12 [Adv-2]` | `#016` `fps_24_w — Biconnected Graphs` | All-$n$ extraction of pointed block-cut $\ln(R/x) = B'(R)$ requires `revert` | **Ch 21** | Scope `Ch 12` to single-$n$ $O(n \log n)$ LIF (`Ch 11`) & $O(n^2)$ DP; cross-ref `Ch 21` for all-$n$ |
| 11 | `Ch 12 [Mas-1]` | `#183` `Luogu P5827 — 点双连通图计数` | Single-$n$ uses `Ch 11` LIF; all-$n$ note mentions `Ch 21` | **Ch 11 (OK)** | Clarify single-$n$ $O(n \log n)$ LIF in `Ch 12` table (`Ch 21` revisited in §5.2) |
| 12 | `Ch 12 [Mas-2]` | `#184` `Luogu P5828 — 边双连通图计数` | Single-$n$ uses `Ch 11` LIF; all-$n$ note mentions `Ch 21` | **Ch 11 (OK)** | Clarify single-$n$ $O(n \log n)$ LIF in `Ch 12` table |
| 13 | `Ch 18 [Mas-2]` | `#230` `LOJ 6728 — U 群把妹王` | Table mentions *"Power Projection / Kinoshita–Li (`Ch 21`)"* in `Ch 18` | **Ch 21** | Scope `Ch 18 [Mas-2]` strictly to Algebraic-to-ODE $O(n)$ P-Recursive Extraction |
| 14 | `CP-IV.8` | `#219` `LOJ 3398 — 带加强和多项木` | Duplicate/variant title overlap with `#179` (`Luogu P5597` in `Ch 10 [Adv-1]`) | **Alias Clash** | Clarify `#179` as `Luogu P5597 — 【XR-4】复读` ($k$-ary tree automaton) and `#219` as `LOJ 3398 — 带加强和多项木` (Good–Lagrange) |

---

### 3.2 Complete Audit of the 17 Corrupted Stage-1 Descriptions in Blind Checkpoints (`CP-II`–`CP-VI`)

In Section 4 of `synthesis_v1_curriculum.md`, Stage 2 (the collapsible answer key) has the **correct** problem reductions, but **17 rows of Stage 1 ("Raw Constraint & Structural Cues") have hallucinated/corrupted text copied from bare templates or unrelated problems**. Every single corrupted row must be replaced in `synthesis_v2` using the exact verified text below:

| Slot | Pool ID & Problem Title | Corrupted Stage-1 Text in `synthesis_v1` (WRONG) | Exact Corrected Stage-1 Text for `synthesis_v2` (VERIFIED) |
| :-: | :--- | :--- | :--- |
| **CP-II.2** | `#152` **Luogu P4091 — [HEOI2016] 求和** | *"Given $N, M \le 2.5\times 10^5$, compute $\sum_k \binom{N}{k}\binom{M}{k}\dots$ with three coupled index constraints."* | **Given $n \le 10^5$, evaluate the double sum $\sum_{i=0}^n \sum_{j=0}^i \left\{\begin{smallmatrix} i \\ j \end{smallmatrix}\right\} 2^j j! \pmod{998244353}$.** |
| **CP-II.3** | `#251` **CF 1264D1 — Beautiful Bracket Sequence (Easy)** | *"Given a polynomial $P(x)$ of degree $N \le 2.5\times 10^5$ and shift $c$, output the coefficients of $P(x+c)$."* *(Bare Taylor Shift template!)* | **Given a bracket string of `(`, `)`, and `?` of length $n \le 2000$, sum the maximum matched nested depth over all $2^q$ completions.** |
| **CP-II.4** | `#252` **CF 622F — The Sum of the k-th Powers** | *"For all $k=1,\dots,n$ ($n \le 2.5\times 10^5$), count permutations of $n$ with $k$ prefix maxima and $b$ suffix maxima."* *(That is `CF 960G`!)* | **Given $n \le 10^9$ and $k \le 10^6$, evaluate $\sum_{i=1}^n i^k \pmod{10^9+7}$ in $O(k)$ time.** |
| **CP-II.5** | `#100` **CF 1054H — Epic Convolution** | *"Evaluate $\sum_{k=0}^n f(k) \binom{n}{k} p^k (1-p)^{n-k}$ for degree-$d$ polynomial $f$."* *(That is `Luogu P6667`!)* | **Given arrays $a_i, b_j$ ($n, m \le 10^5$) and $c$, evaluate $\sum_{i,j} a_i b_j c^{i^2 j^3 \bmod 490018} \pmod{490019}$.** |
| **CP-II.8** | `#137` **CF Gym 102331J — Forbidden Strings** | *"Arrange $n$ colored balls ($\sum c_i \le 10^5$) on a circle so no two adjacent balls share the same color."* *(That is `ABC 232 G` / `LOJ 6503`!)* | **Count strings of length $n$ over an alphabet that avoid a given dictionary of forbidden patterns $P_1, \dots, P_m$.** *(Note: `#137` moves to `Ch 08 [Mas-2]` and `#141` `LOJ 6222` takes `CP-II.8` in §6)* |
| **CP-III.1** | `#060` **ARC 138 E — Decreasing Subsequence** | *"Given transition weights $g_1, \dots, g_n$ ($n \le 10^5$), solve $f_i = \sum_{j=1}^i f_{i-j} g_j$ online."* *(Bare `Luogu P4721` template!)* | **Count sequences $A_1, \dots, A_N$ with $0 \le A_i \le i$ ($N \le 2.5\times 10^5$) containing a decreasing subsequence of length $K$.** *(Note: `#060` moves to `Ch 09 [SS-1]` and `#090` `CF 848E` takes `CP-III.1` in §6)* |
| **CP-III.4** | `#160` **Luogu P4747 — [CERC2017] Intrinsic Interval** | *"Given $f(x)$ of degree $n \le 10^5$, solve a nonlinear functional equation $G(x) = \dots$ to degree $n$."* | **Count simple permutations (interval-indecomposable permutations) and decompose permutation intervals up to $n \le 10^5$.** |
| **CP-III.7** | `#205` **Luogu P8555 — 密码学第三次小作业** | *"Extract $[x^n]$ from a compositional functional equation $F(x) = x \phi(F(x))$ for $n \le 2\times 10^5$."* *(Wrong constraint!)* | **Extract $[x^n]$ from a scale-invariant algebraic generating function for $n \le 10^{18}$ modulo a small prime $p \le 10^5$.** |
| **CP-III.8** | `#163` **Luogu P5206 — [WC2019] 数树** | *"Count labeled biconnected / block-structured graphs on $n \le 10^5$ vertices with cycle-weight constraints."* *(Wrong problem!)* | **Given $n \le 10^5$ and $y$, evaluate $\sum_{T_1, T_2} y^{n - \lvert E(T_1) \cap E(T_2) \rvert}$ across 3 subtasks: (0) both fixed, (1) $T_1$ fixed, (2) both variable.** |
| **CP-IV.7** | `#243` **yukicoder 2104 — Fuss–Catalan Diagonal** | *"Count lattice walks of length $n \le 2\times 10^5$ confined to $[0, H]$ with step set $\{-1, 0, +1\}$."* *(Wrong problem!)* | **Extract the asymmetric $(p, q)$-diagonal coefficient $[x^{pn} y^{qn}] F(x, y)$ of a bivariate algebraic/rational series ($n \le 2\times 10^5$).** |
| **CP-IV.8** | `#219` **LOJ 3398 — 带加强和多项木** | *"Count 2D lattice paths in the first quadrant $(x,y \ge 0)$ of length $n \le 10^5$ with asymmetric steps."* *(Wrong problem!)* | **Given a multi-type colored rooted tree specification on $n \le 10^5$ vertices, extract the multivariate coefficient via Jacobian $\det(I - J_G)$.** *(Note: `#219` moves to `Ch 17 [Int-2]` and `#082` `BZOJ 4899` takes `CP-IV.8` in §6)* |
| **CP-V.1** | `#028` **ABC 260 Ex — Colorfulness** | *"Given a rational/algebraic bivariate diagonal of degree $n \le 10^7$, compute the $n$-th term in $O(n)$ time."* *(Wrong problem!)* | **Given $N$ balls with color multiplicities $c_i$ ($\sum c_i = N \le 2.5\times 10^5$), count permutations for every $K=0..N-1$ adjacent equal-color pairs.** *(Note: `#028` moves to `Ch 19 [Adv-1]` and `#236` `yukicoder 963` takes `CP-V.1` in §6)* |
| **CP-V.4** | `#135` **CF 1988F — Heartbeat** | *"Given $f(0), f(1), \dots, f(d)$ ($d \le 1.6\times 10^5$), evaluate $f(c), f(c+1), \dots, f(c+m)$ in $O(d \log d)$ time."* *(Bare `Luogu P5667` template!)* | **For all $n \le 700$, count permutations weighted by prefix-maximum count, suffix-maximum count, and adjacent ascent count.** |
| **CP-V.6** | `#215` **UOJ 604 — [UR #20] 跳蚤电话** | *"Given polynomials $F(x), G(x)$ of degree $N \le 1.3\times 10^5$, compute $F(G(x)) \bmod x^{N+1}$ in $O(N \log^2 N)$."* *(Bare `composition` template!)* | **Given a tree on $n \le 10^5$ vertices constructed by adding leaves/splitting edges, count valid construction histories.** |
| **CP-V.8** | `#036` **ABC 281 Ex — Alchemy** | *"Given $F(x)$ with $[x^0]F=0, [x^1]F \neq 0$ ($N \le 1.3\times 10^5$), compute all coefficients of $F^{\langle -1 \rangle}(x) \bmod x^{N+1}$."* *(Bare `revert` template!)* | **Count reachable subset states in an alchemy merging process of size $N \le 2\times 10^5$ via falling-factorial EGF and compositional inverse.** *(Note: `#036` moves to `Ch 21 [SS-1]` and `#068` `AGC 005 F` takes `CP-V.8` in §6)* |
| **CP-VI.5** | `#068` **AGC 005 F — Many Easy Problems** | *"Count $n \times m$ matrices over $\mathbb{F}_q$ ($n, m \le 2\times 10^5$) of each rank $r$ via $q$-binomials."* *(Wrong problem!)* | **Given a tree $T$ on $N \le 2\times 10^5$ vertices, for every $K=1,\dots,N$, compute the sum of minimal Steiner subtree sizes over all $\binom{N}{K}$ vertex subsets.** *(Note: `#068` swaps with `#054` `ARC 106 E` into `CP-V.8` in §6)* |
| **CP-VI.8** | `#180` **Luogu P5643 — [PKUWC2018] 随机游走** | *"Given a multiplicative arithmetic function on $n \le 10^{10}$, evaluate prefix sums via Dirichlet series convolution."* *(Wrong problem!)* | **Given a tree on $n \le 18$ vertices and root $x$, answer $Q \le 5000$ queries asking for the expected steps of a random walk to visit all vertices in $S \subseteq V$.** |

---

### 3.3 Complete Audit of the 10 Mismatched Slot/ID References in Section 5.2 (Revisited Dual-Perspective Index)

In `synthesis_v1_curriculum.md` Section 5.2 (Lines 1028–1039), `10` of the `12` rows have stale `Primary Slot (#ID)` entries that do not match the `Problem ID & Title` in Column 3. Here is the exact audit and correction table:

| Row | `Primary Slot` Written in `synthesis_v1` (STALE) | Named Problem in Column 3 | Actual Pool `#ID` & Slot of Named Problem (after §6 `synthesis_v2` Swap) |
| :-: | :--- | :--- | :--- |
| 1 | `Ch 02 [Int-1]` (`#101`) | **CF 1096G — Lucky Tickets** | **`Ch 02 [Int-1]` (`#101`)** *(Matches)* |
| 2 | `Ch 04 [Mas-1]` (`#041`) *(Wrong: `#041` is `ABC 303 Ex`!)* | **CF 438E — The Child and Binary Tree** | **`Ch 02 [Adv-2]` (`#084`)** |
| 3 | `Ch 05 [Adv-1]` (`#034`) *(Wrong: `#034` is `ABC 279 G`!)* | **ABC 300 Ex — Fibonacci: Revisited** | **`Ch 05 [Adv-1]` (`#040`)** |
| 4 | `Ch 06 [Adv-2]` (`#096`) *(Wrong: `#096` is `CF 960G`!)* | **CF 923E — Perpetual Subtraction** | **`Ch 06 [Adv-1]` (`#094`)** |
| 5 | `Ch 08 [Int-1]` (`#155`) *(Wrong: `#155` is `Luogu P4491`!)* | **CF 840C — On the Bench** | **`Ch 08 [Int-2]` (`#089`)** |
| 6 | `Ch 09 [Adv-2]` (`#225`) *(Wrong: `#225` is `LOJ 6503`!)* | **ABC 230 Ex — Bullion** | **`Ch 09 [Int-2]` (`#023`)** |
| 7 | `Ch 10 [Adv-1]` (`#179`) *(Wrong: `#179` is `Luogu P5597`!)* | **yukicoder 3029 — Cactus Weight** | **`Ch 10 [Int-1]` (`#244`)** |
| 8 | `Ch 11 [Int-1]` (`#201`) *(Wrong: `#201` is `Luogu P7439`!)* | **Luogu P7438 — [AGM 2021] 恐龙** | **`Ch 11 [SS-2]` (`#200`)** |
| 9 | `Ch 12 [Adv-1]` (`#190`) *(Wrong: `#190` is `Luogu P6596`!)* | **Luogu P5827 — 点双连通图计数** | **`Ch 12 [Mas-1]` (`#183`)** |
| 10 | `Ch 14 [SS-1]` (`#115`) *(Wrong: `#115` is `CF 1392H`!)* | **Luogu P4548 — [CTSC2006] 歌唱王国** | **`Ch 14 [Int-1]` (`#156`)** |
| 11 | `Ch 15 [Int-1]` (`#220`) | **ABC 205 E / ARC 145 D / LOJ 6160** | **`Ch 15 [Int-1]` (`#220`)** *(Clarify title as `LOJ 6160 — 2D Matrix Walk Reflection`)* |
| 12 | `Ch 16 [Adv-2]` (`#125`) *(Wrong: `#125` is `CF 1667E`!)* | **ARC 136 F / Luogu P4456 — Diagonal & ODE** | **`CP-IV.6` (`#058` `ARC 136 F — Flip Cells`)** |

---

## 4. Investigation 3: Difficulty Monotonicity Audit (`SS-1..2` $\to$ `Int-1..2` $\to$ `Adv-1..2` $\to$ `Mas-1..2`)

We audited the difficulty progression within each of the 24 chapters against the official difficulty ratings in `problem_archive.md` and actual mathematical depth. Nine monotonicity inversions were identified in `synthesis_v1_curriculum.md`:

| # | Chapter & Slot | Problem ID & Title | Rating in `problem_archive.md` | Why It Violates Difficulty Monotonicity | Resolution in `synthesis_v2` (§6) |
| :-: | :--- | :--- | :-: | :--- | :--- |
| 1 | `Ch 02 [SS-1]` | `#011` `fps_24_q — Dice` | `Int / Adv` | Requires Newton–Girard power sums $-\ln\prod(1-A_i x)$ **plus** EGF moment expansion; much harder than `Ch 02 [Int-1]` (`CF 1096G`) and `[Mas-2]` (`Luogu P5268`). | Move `#011` to `Ch 04 [Adv-2]`; place `#238` (`yukicoder 1145`, pure Newton–Girard `SS`) at `Ch 02 [SS-1]`. |
| 2 | `Ch 02 [Mas-2]` | `#165` `Luogu P5268` | `Stepping Stone` | Rated `Stepping Stone` (`Wave 5B #C3`) in `problem_archive.md`; placed above `CF 438E` (`#084`) and `ABC 267 Ex` (`#030`)! | Demote `#165` to `Ch 02 [SS-2]`; place `#091` (`CF 891E`) at `Ch 02 [Mas-2]`. |
| 3 | `Ch 05 [SS-2]` vs `[Adv-1]` | `#040` `ABC 300 Ex` vs `#034` `ABC 279 G` | `Int` vs `SS` | `#040` (`ABC 300 Ex — Fibonacci: Revisited`, degree-$K$ Bostan–Mori at $N \le 10^{18}$) is harder than `#034` (`ABC 279 G — At Most 2 Colors`, basic $O(N)$ rational OGF). | Swap `#034` (`ABC 279 G`) into `Ch 05 [SS-2]` and `#040` (`ABC 300 Ex`) into `Ch 05 [Adv-1]` (which also aligns §5.2 Row 3!). |
| 4 | `Ch 09 [SS-1]` | `#003` `fps_24_f — Colored Paper` | `Int / Adv` | Part 2 requires solving $F = x \cosh F$ via Newton iteration or LIF, harder than `Ch 09 [Int-1]` (`CF 553E`). | Move `#003` to `Ch 11 [SS-1]`; place `#060` (`ARC 138 E`) at `Ch 09 [SS-1]`. |
| 5 | `Ch 11 [SS-1]` | `#010` `fps_24_p — Ball` | `Advanced` | Requires bivariate root shift + formal residue extraction, whereas `#003` (`fps_24_f` Part 2: $[x^n] F(x)$ for $F = x \cosh F$) is the cleanest 1-line LIF Stepping Stone. | Place `#003` (`fps_24_f`) at `Ch 11 [SS-1]`, `#200` (`Luogu P7438`) at `[SS-2]`, `#196` (`Luogu P6672`, Raney) at `[Int-1]`, `#201` (`Luogu P7439`) at `[Int-2]`, and `#010` (`fps_24_p`) at `[Adv-1]`. |
| 6 | `Ch 12 [SS-1]` | `#047` `ABC 387 G — Prime Circuit` | `Advanced` | Requires $O(N \log^2 N)$ Kinoshita–Li fast polynomial composition $C(T(x))$; far harder than `#176` (`Luogu P5434 — 有标号荒漠计数`, rated `Stepping Stone`!). | Move `#047` to `Ch 21 [Int-1]`; promote `#176` (`Luogu P5434 — 有标号荒漠计数`) to `Ch 12 [SS-1]`. |
| 7 | `Ch 17 [SS-2]` | `#196` `Luogu P6672` | `Stepping Stone` (1D) | Pure 1D Raney's Lemma problem placed in 2D Quarter-Plane / Good–Lagrange chapter. | Move `#196` to `Ch 11 [Int-1]`; place `#154` (`Luogu P4456`) and `#044` (`ABC 336 G`) at `Ch 17 [SS-1..2]`. |
| 8 | `Ch 19 [Adv-1]` | `#108` `CF 1264D2` | `Stepping Stone / Int` | 1-line Vandermonde absorption identity placed as `Adv-1` above `CF 932E` (`#095`) and `Luogu P6667` (`#195`)! | Move `#108` to `CP-V.2`; place `#028` (`ABC 260 Ex`) at `Ch 19 [Adv-1]`. |
| 9 | `Ch 21 [SS-1..Int-2]` | `#238, #054, #157, #091` | `SS / Int` (`Ch 02/04`) | None of these 4 problems use composition or power projection, creating a cliff jump from `Int-2` (`O(n^2)` EGF) to `Adv-1` (`ARC 154 F`, Coupon Collector + Fast Composition). | Populate `Ch 21 [SS-1..Int-2]` with `#036` (`ABC 281 Ex`), `#045` (`ABC 345 G`), `#047` (`ABC 387 G`), and `#059` (`ARC 137 F`). |

---

## 5. Investigation 4: Alignment with `PROBLEM_CURATION.md` & Blueprint for Re-Indexing `problem_archive.md`

### 5.1 Accounting Reconciliation (`PROBLEM_CURATION.md` vs. `problem_archive.md` vs. `synthesis_v2`)

1. **Exact Pool Bijection (`254 + 67 = 321`)**:
   - `PROBLEM_CURATION.md` defines the canonical deduplicated pool of **`254` accepted problems (`#001`–`#254`)** and **`67` quarantined bare templates (`R-01`–`R-67`)** (`321` total).
   - Every single ID `#001`–`#254` is accounted for in `synthesis_v1_curriculum.md` (`192` Chapter Ladder slots + `48` Blind Checkpoint slots + `14` Synthesis Reserve slots = `254`).
   - Our `synthesis_v2` swap list in **Section 6** is a **strict mathematical permutation on `#001`–`#254`**: zero problems are added, dropped, or duplicated.

2. **Resolving Cross-Wave Duplicate Entries in `problem_archive.md`**:
   - As documented in `PROBLEM_CURATION.md`, `problem_archive.md` was originally concatenated across `14` research wave reports (`Wave 1A` through `Wave 5B`) and therefore contains ~`31` cross-wave duplicate entries (where the same problem was analyzed from two different wave perspectives, e.g., `CF 438E` in `Wave 1A` and `Wave 3A`, `Luogu P4548` in `Wave 2B` and `Wave 4B`, `ABC 230 Ex` in `Wave 1A` and `Wave 3A`, `Luogu P5827` in `Wave 3A` and `Wave 5B`).
   - Also, `#179` (`Luogu P5597 — 【XR-4】复读`) and `#219` (`LOJ 3398 — 带加强和多项木`) must have their titles disambiguated so `#179` is exclusively `Luogu P5597 — 【XR-4】复读` ($k$-ary tree automaton minimization + Newton iteration, `Ch 10 [Adv-1]`) and `#219` is exclusively `LOJ 3398 — 带加强和多项木` (Multivariate Good–Lagrange tree specification, `Ch 17 [Int-2]`).

### 5.2 Blueprint for Re-Indexing `problem_archive.md` by the 24 Canonical Chapters (`Ch 01`–`Ch 24`)

When `problem_archive.md` is updated to match `synthesis_v2`, its structure should be upgraded as follows without losing any of its rich wave writeups:
1. **Section 1 (Judge-by-Judge Quick Lookup Index)**:
   - Add a **Column 2 (`Canonical Pool ID #001–#254 / R-01–R-67`)** and **Column 6 (`Canonical Curriculum Slot`: `Ch XX [Tier]`, `CP-P.k -> Ch XX`, `Syn-XX`, or `Quarantined Template R-XX (Ch XX)`)** to every row of the AtCoder, Codeforces, Luogu, UOJ/LOJ/QOJ, and Other Judge lookup tables.
2. **New Section 1.8 (24-Chapter Master Index `Ch 01`–`Ch 24`)**:
   - Insert a compact 24-chapter lookup table right after Section 1.7 that lists for each chapter `Ch 01`–`Ch 24`:
     - Its `8` Ladder Problems (`SS-1..Mas-2`) with clickable anchor links to their full writeups in Sections 2–15,
     - Its routed Blind Checkpoint problems (`CP-I`–`CP-VI`),
     - Its Synthesis Reserve bridges (`Syn-01`–`Syn-14`), and
     - Its Quarantined Template footnotes (`R-01`–`R-67`).
3. **Cross-Wave Multi-Perspective Consolidation**:
   - Where a problem appears in two waves of `problem_archive.md` (the 12 flagship dual-perspective problems in §5.2 plus ~19 wave overlaps), cross-link both wave writeups under its canonical `#ID` so chapter authors in Phase 2 automatically inherit both perspectives.

---

## 6. Investigation 5: Exact Slot-by-Slot Bijective Swap List for `synthesis_v2`

To achieve **0 forward references, 0 thematic misplacements, 0 difficulty inversions, and 100% preservation of the 254-problem bijection**, apply the following **43-problem bijective permutation** across the 254 slots of `synthesis_v1_curriculum.md`.

### 6.1 Exact Corrected Chapter Ladder Tables for the Affected Chapters (`synthesis_v2` Drop-In Replacement)

Below are the exact, ready-to-paste `8`-problem ladder tables for every modified chapter (`Ch 02`, `Ch 04`, `Ch 05`, `Ch 08`, `Ch 09`, `Ch 11`, `Ch 12`, `Ch 13`, `Ch 16`, `Ch 17`, `Ch 18`, `Ch 19`, `Ch 21`, `Ch 23`), followed by the complete 43-row bijective permutation ledger in Section 6.2.

#### Corrected `Ch 02` Ladder (`Prereqs <= Ch 02`, 0 EGF / CDQ / Composition Forward Refs)
| Tier | ID | Problem | Wave | Core Mathematical Mechanism & Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#238` | **yukicoder 1145 — Sum of Powers** | `2A#35` | Newton–Girard Power Sums $-\sum_{i=1}^n \frac{-a_i x}{1 - a_i x} = -x \frac{d}{dx}\ln\prod(1 - a_i x)$ |
| **SS-2** | `#165` | **Luogu P5268 — Subset-Sum Product & Exp-Ln Bridge** | `5B#C3` | Subset-Sum Product $\prod(1 + x^{a_i})$ via Logarithmic Derivative & $\exp$ |
| **Int-1** | `#101` | **CF 1096G — Lucky Tickets** | `1B#8` | $O(NK)$ Sparse Power ODE $(1-x)(1-x^{10})G' = k P' G$ (Zero NTTs) |
| **Int-2** | `#222` | **LOJ 6261 — 一个人的高三 (Lonely Senior Year)** | `1A#10` | Series Power $F(x)^k$ & Binomial Series Expansion $(1-x)^{-\alpha}$ |
| **Adv-1** | `#157` | **Luogu P4705 — 玩游戏** | `1A#24` | Newton–Girard Power Sums $\ln\prod(1 - a_i x)$ + Binomial Convolution |
| **Adv-2** | `#084` | **CF 438E — The Child and Binary Tree** | `1A#7` | Quadratic Radical $F(x) = \frac{2}{1 + \sqrt{1 - 4C(x)}}$ via Newton `sqrt` + `inv` |
| **Mas-1** | `#030` | **ABC 267 Ex — Odd Sum** | `1B#7` | Parity Split $\frac{P(x)-P(-x)}{2}$ + Logarithmic Derivative $\ln/\exp$ |
| **Mas-2** | `#091` | **CF 891E — Lust** | `1A#16` | Polynomial Product $\prod_{i=1}^n (a_i - x)$ + Formal Derivative / Coefficient Extraction |

#### Corrected `Ch 04` Ladder (`Prereqs <= Ch 04`)
| Tier | ID | Problem | Wave | Core Mathematical Mechanism & Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#002` | **`fps_24_e` — Sequence 2** | `1A#15` | Labeled Multiset Permutation EGF $\prod_{m=1}^M \sum_{j=0}^m \frac{x^j}{j!}$ |
| **SS-2** | `#007` | **`fps_24_m` — Value of Permutation** | `1A#20` | Cycle Decomposition EGF $\ln\frac{1}{1-x}$ & Pointer Tracking |
| **Int-1** | `#161` | **Luogu P4841 — [集训队作业2013] 城市规划** | `1A#14` | Labeled Connected Graphs $C(x) = \ln G(x)$ via EGF Logarithm |
| **Int-2** | `#008` | **`fps_24_n` — Tree** | `3A#2` | Prüfer Sequence Degree-Distribution EGF $n![x^{n-2}]\prod E_{d_i}(x)$ |
| **Adv-1** | `#083` | **CF 407E / Gym — k-Cycle** | `1A#21` | Constrained Cycle-Length Permutation EGF $\exp(\sum_{k \in S} \frac{x^k}{k})$ |
| **Adv-2** | `#011` | **`fps_24_q` — Dice** | `1B#18` | Newton–Girard Power Sums $-\ln\prod(1 - A_i x)$ + EGF Moment Expansion |
| **Mas-1** | `#041` | **ABC 303 Ex — Constrained Tree Degree** | `3A#5` | Prüfer Sequence + Sparse $\ln/\exp$ for Vertex-Degree Constraints |
| **Mas-2** | `#174` | **Luogu P5401 — [CTS2019] 珍珠** | `1B#14` | Parity EGF $\left(\frac{e^x+e^{-x}}{2}\right)^k$ + Binomial Inversion |

#### Corrected `Ch 05` Ladder (`Prereqs <= Ch 05`)
- Swap `SS-2` (`#040` `ABC 300 Ex`) and `Adv-1` (`#034` `ABC 279 G`):
  - `SS-1`: `#104` (`CF 1117D`), `SS-2`: `#034` (`ABC 279 G`), `Int-1`: `#187` (`Luogu P6122`), `Int-2`: `#069` (`AGC 013 E`), `Adv-1`: `#040` (`ABC 300 Ex`), `Adv-2`: `#081` (`CF 148E / Gym 102978F`), `Mas-1`: `#177` (`Luogu P5487`), `Mas-2`: `#073` (`AGC 049 D`).

#### Corrected `Ch 08` Ladder (`Prereqs <= Ch 08`, 0 Trivariate Diagonal Forward Refs)
- Replace `Mas-2` (`#074` `AGC 058 D`, moved to `Ch 16 [Adv-2]`) with `#137` (**`CF Gym 102331J — Forbidden Strings`**, Multi-Pattern Aho–Corasick Goulden–Jackson Cluster Matrix $(I + C(x))^{-1}$), and place `#141` (**`LOJ 6222 — Powers of k in Permutations`**) into `CP-II.8`.

#### Corrected `Ch 09` Ladder (`Prereqs <= Ch 09`, 0 Implicit Newton / LIF Forward Refs)
| Tier | ID | Problem | Wave | Core Mathematical Mechanism & Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#060` | **ARC 138 E — Decreasing Subsequence** | `5A#22` | RSK / Greene Theorem Semi-Online Block CDQ Convolution |
| **SS-2** | `#021` | **ABC 222 H — Beautiful Binary Tree** | `3B#1` | Causal Binary Tree Recurrence via CDQ / Semi-Online Convolution |
| **Int-1** | `#086` | **CF 553E — Kyoya and Train** | `1B#13` | Time-Window Shortest Path DP via CDQ Divide-and-Conquer FFT |
| **Int-2** | `#023` | **ABC 230 Ex — Bullion** | `1A#27` | Unlabeled Knapsack / Weighings via Online Relaxed Convolution |
| **Adv-1** | `#056` | **ARC 123 F — Arithmetic Progression** | `4B#32` | Non-Homogeneous Causal Recurrence via CDQ / Relaxed Convolution |
| **Adv-2** | `#225` | **LOJ 6503 — Magic (魔术)** | `2B#B6` | Adjacent-Color Run Avoidance + Divide-and-Conquer NTT |
| **Mas-1** | `#206` | **UOJ 50 — [UR #3] 链式反应** | `2A#46` | Non-Autonomous Differential Equation $F' = \frac{1}{2}A(x)F^2 + 1$ via CDQ FFT |
| **Mas-2** | `#075` | **AGC 060 D — Same Generating Function** | `1B#25` | Coupled Eulerian Permutation Ascent CDQ Divide-and-Conquer FFT |

#### Corrected `Ch 11` Ladder (`Prereqs <= Ch 11`, 0 Fast Composition Forward Refs)
| Tier | ID | Problem | Wave | Core Mathematical Mechanism & Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#003` | **`fps_24_f` — Colored Paper / Colored Tree** | `1A#2` | Implicit Tree Equation $F = x \cosh F$ Solved via $[x^n]F = \frac{1}{n}[u^{n-1}]\cosh^n u$ |
| **SS-2** | `#200` | **Luogu P7438 — [AGM 2021] 恐龙** | `3B#28` | Composite Power Extraction $[x^N] F(x)^k = \frac{k}{N}[u^{N-k}]\phi(u)^N$ |
| **Int-1** | `#196` | **Luogu P6672 — [清华集训2016] 你的生命已如风中残烛** | `4B#5` | 1D Raney's Lemma Cyclic Shift $\frac{1}{m+1}$ on Degree Sequences |
| **Int-2** | `#201` | **Luogu P7439 — [KrOI2021] 蕾切尔** | `3B#29` | Formal Residue Change of Variables $\operatorname{Res}_x G(x) = \operatorname{Res}_u G(F(u))F'(u)$ |
| **Adv-1** | `#010` | **`fps_24_p` — Ball** | `1A#29` | Bivariate Root Shift + Formal Residue / Lagrange Inversion |
| **Adv-2** | `#229` | **LOJ 6703 — 小 Q 的序列** | `3B#27` | Derivative-Free Form 4 LIF $[x^n] H(F(x)) = [u^n] H(u)(1 - u\phi'/\phi)\phi(u)^n$ |
| **Mas-1** | `#114` | **CF 1349F2 — Slime and Sequences (Hard Version)** | `1A#30` | Eulerian Bivariate EGF $\to$ Lambert-$W$ Substitution + Lagrange Inversion |
| **Mas-2** | `#203` | **Luogu P7592 — 2021 CoE-II E (数树)** | `3B#11` | 4-Subtask Synthesis (2D Rational, Bivariate LIF, Lucas Char-$p$ LIF) |

#### Corrected `Ch 12` Ladder (`Prereqs <= Ch 12`, 0 Fast Composition Forward Refs)
| Tier | ID | Problem | Wave | Core Mathematical Mechanism & Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#176` | **Luogu P5434 — 有标号荒漠计数** | `3A#9` | Labeled Desert EGF $\exp(C_{\text{cactus}}(x))$ via Cactus $\exp$ |
| **SS-2** | `#245` | **51Nod 1728 — 不动点** | `3A#19` | Endofunction Cycles of Height-$\le k$ Rooted Trees $F_j(x) = x \exp(F_{j-1}(x))$ |
| **Int-1** | `#146` | **Luogu P3684 / BZOJ 3684 — 大朋友和多叉树** | `3B#25` | Degree-Constrained Multi-Way Rooted Tree Species + Lagrange Inversion |
| **Int-2** | `#227` | **LOJ 6569 — 仙人掌计数 (Cactus Counting)** | `3A#7` | Labeled Cactus Pointed Equation $C^\bullet = x \exp\left(C^\bullet + \frac{(C^\bullet)^2}{2(1 - C^\bullet)}\right)$ |
| **Adv-1** | `#190` | **Luogu P6596 — How Many of Them** | `3A#14` | Labeled Connected Graphs with $\le k$ Bridges via Tree-of-2-ECCs EGF |
| **Adv-2** | `#016` | **`fps_24_w` — Biconnected Graphs** | `3A#11` | Pointed Block-Cut Tree $\ln(R(x)/x) = B'(R(x))$ (Single-$n$ LIF / $O(n^2)$ DP; all-$n$ in Ch 21) |
| **Mas-1** | `#183` | **Luogu P5827 — 点双连通图计数** | `3A#10` | Single-Degree $N$ Vertex-Biconnected Graph Count via Block-Cut LIF in $O(N \log N)$ |
| **Mas-2** | `#184` | **Luogu P5828 — 边双连通图计数** | `3A#13` | Single-Degree $N$ Edge-Biconnected Graph Count via $T^\bullet = x e^{B'(T^\bullet)}$ + LIF |

#### Corrected `Ch 13` Ladder (`Prereqs <= Ch 13`)
- `SS-1`: `#164` (`Luogu P5219 — 无聊的水题 I`, Bounded-Degree Spanning Tree Prüfer / Kirchhoff Warmup)
- `SS-2`: `#103` (`CF 1109D — Sasha and Interesting Fact`, Generalized Cayley Forest Formula $k n^{n-k-1}$)
- `Int-1`: `#093` (`CF 896E / Gym 102129D — Chirp-Z Graphical GF`)
- `Int-2`: `#189` (`Luogu P6295 — 有标号 DAG 计数`)
- `Adv-1`: `#199` (`Luogu P7364 — 有标号二分图计数`)
- `Adv-2`: `#053` (`ARC 105 F / LOJ 6539 — Lights Out on Connected Graph`)
- `Mas-1`: `#122` (`CF 1580E / CF 1392G — Strongly Connected Tournaments`)
- `Mas-2`: `#212` (`UOJ 498 — 新年的追逐战`)

#### Corrected `Ch 16` Ladder (`Prereqs <= Ch 16`)
- `SS-1`: `#048` (`ABC 399 G — Colorful Graph`, 2D Bivariate GF)
- `SS-2`: `#129` (`CF 1810G — The Maximum Prefix`, Bivariate Prefix Max GF)
- `Int-1`: `#025` (`ABC 240 G — Teleporting Takahashi`, 3D Walk Decoupled into 1D $\times$ Rotated 2D $(x+y, x-y)$ Bivariate Binomials)
- `Int-2`: `#232` (`QOJ 4895 — Bivariate Rational Coefficient`, 2D Bostan–Mori)
- `Adv-1`: `#237` (`yukicoder 1080 — Diagonal / Bostan–Mori`)
- `Adv-2`: `#074` (`AGC 058 D — Yet Another ABC String`, Trivariate Rational Cluster Diagonal $[x^A y^B z^C] \frac{1-xyz}{1-(x+y+z)+2xyz}$)
- `Mas-1`: `#240` (`yukicoder 1751 — Bivariate Diagonal`)
- `Mas-2`: `#214` (`UOJ 592 — 新年的聚会`, Bivariate Symmetric/Antisymmetric Determinant Extraction)

#### Corrected `Ch 17` Ladder (`Prereqs <= Ch 17`)
| Tier | ID | Problem | Wave | Core Mathematical Mechanism & Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#154` | **Luogu P4456 — [CQOI2018] 交错序列** | `5A#7` | 2D Constrained Step Walk $(x, y)$ Moment Extraction $\sum i^a j^b$ |
| **SS-2** | `#044` | **ABC 336 G — 16 Integers** | `3A#33` | De Bruijn Eulerian Graph + MacMahon Master Theorem $\det(I - X A)^{-1}$ |
| **Int-1** | `#228` | **LOJ 6671 — Unlabeled Phylogenetic Trees** | `3B#17` | Multivariate Burnside Cycle Index + Good–Lagrange |
| **Int-2** | `#219` | **LOJ 3398 — 带加强和多项木** | `3B#9` | Multivariate Implicit Tree System + Good–Lagrange Jacobian $\det(I - J_G(u))$ |
| **Adv-1** | `#015` | **`fps_24_v` — 12 Directions** | `1A#33` | 2D Laurent Step-Polynomial Factorization & Boundary Reduction |
| **Adv-2** | `#204` | **Luogu P7599 — [APIO2021] 雨林跳跃** | `4B#16` | 2D Dominance Lattice Walk + Bivariate Kernel Method |
| **Mas-1** | `#138` | **CF Gym 102538F — 3D Walk / Quarter Plane** | `4B#31` | Quarter-Plane Obstinate Kernel / Algebraic Group Involution |
| **Mas-2** | `#234` | **QOJ 8048 — Good–Lagrange Multivariate** | `4B#30` | Multivariate Good–Lagrange Jacobian $\det(I - J_G(u))$ + Newton |

#### Corrected `Ch 18` Ladder (`Prereqs <= Ch 18`)
| Tier | ID | Problem | Wave | Core Mathematical Mechanism & Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#151` | **Luogu P4002 — [清华集训2017] 生成树计数** | `3A#27` | Algebraic / Prüfer Tree Block Sum $\to$ D-Finite Differential Reduction |
| **SS-2** | `#064` | **ARC 153 D — Sum of Sum of Digits** | `5B#D9` | Carry-Propagation Polynomial Shift & D-Finite Recurrence |
| **Int-1** | `#022` | **ABC 226 H — Random K-th Max** | `2B#E2` | Order-Statistic Integral $\int_0^1 t^k(1-t)^{n-k} dt$ & Holonomic Recurrence |
| **Int-2** | `#239` | **yukicoder 1504 — Holonomic Walk** | `5A#25` | Algebraic-to-D-Finite ODE Compilation for $O(N)$ Walk Extraction |
| **Adv-1** | `#125` | **CF 1667E — Centroid Probabilities** | `3A#8` | Tree Centroid Differential Recurrence + Reverse Convolution |
| **Adv-2** | `#088` | **CF 755G — PolandBall and Many Other Balls** | `2B#D4` | Continuant Matrix GF + Hyperbola Residue + $O(K)$ 2nd-Order D-Finite ODE |
| **Mas-1** | `#211` | **UOJ 450 — [集训队作业2018] 复读机** | `1A#28` | Mod-$d$ Roots-of-Unity Filter $(e^x + e^{\omega x} + e^{\omega^2 x})^k$ + 2D PDE |
| **Mas-2** | `#230` | **LOJ 6728 — U 群把妹王** | `3A#12` | Algebraic-to-D-Finite ODE Compilation & $O(N)$ P-Recursive Extraction |

#### Corrected `Ch 19` Ladder (`Prereqs <= Ch 19`)
| Tier | ID | Problem | Wave | Core Mathematical Mechanism & Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#242` | **yukicoder 1939 — Numbered Colorful Balls** | `5A#2` | $O(NK)$ Sparse EGF Differential Recurrence Pullback |
| **SS-2** | `#120` | **CF 1548C — The Three Little Pigs** | `2A#7` | Sparse Composition Pullback $H(x) = \frac{u^{N+1}-1}{u-1}\big\rvert_{u=(1+x)^3}$ in $O(N)$ |
| **Int-1** | `#095` | **CF 932E — Team Work** | `1B#10` | Stirling S2 Expansion $\sum S(K,j)\binom{N}{j}j! 2^{N-j}$ + $O(K)$ `EI 科技` ODE |
| **Int-2** | `#195` | **Luogu P6667 — [清华集训2016] 如何优雅地求和** | `2A#25` | Binomial Sum $\sum \binom{n}{k} x^k (1-x)^{n-k} f(k)$ via Falling Factorials / $O(m)$ ODE |
| **Adv-1** | `#028` | **ABC 260 Ex — Colorfulness** | `2B#B7` | Adjacent-Color IE + Coupled Divide-and-Conquer NTT + Truncated Taylor Shift |
| **Adv-2** | `#118` | **CF 1515E — Phoenix and Computers** | `2B#B1` | Sparse Composition Pullback $F(x,y) = (1 - x(e^y-1))^{-1}$ + Row ODE |
| **Mas-1** | `#072` | **AGC 043 D — Merge Triplets** | `2B#C3` | Sparse Composition ODE $\partial_x F = (y + xy^{-1} + x^2)F$ on $\exp(xy + \frac{x^2}{2}y^{-1} + \frac{x^3}{3})$ |
| **Mas-2** | `#213` | **UOJ 514 — [UR #19] 通用测评号** | `5A#24` | `EI 科技` Truncated Exponential Derivative $\frac{d}{dx}(e^{-x} S_{<a}(x)) = -e^{-x} \frac{x^{a-1}}{(a-1)!}$ |

#### Corrected `Ch 21` Ladder (`Prereqs <= Ch 21`, 100% Fast Composition / Power Projection / `revert`)
| Tier | ID | Problem | Wave | Core Mathematical Mechanism & Role |
| :-: | :-: | :--- | :-: | :--- |
| **SS-1** | `#036` | **ABC 281 Ex — Alchemy** | `2B#B12` | Falling-Factorial EGF + Simultaneous All-$n$ `compositional_inverse` |
| **SS-2** | `#045` | **ABC 345 G — Sugoroku 5** | `5B#B2` | Hitting-Time PGF + Kinoshita–Li $O(N \log^2 N)$ Fast Polynomial Composition $F(G(x))$ |
| **Int-1** | `#047` | **ABC 387 G — Prime Circuit** | `4A#P25` | Prime-Cycle Cactus EGF via $O(N \log^2 N)$ Fast Composition $C(T(x))$ |
| **Int-2** | `#059` | **ARC 137 F — Overlaps** | `3B#22` | Implicit Algebraic Equation + Riccati ODE + Fast Polynomial Composition |
| **Adv-1** | `#065` | **ARC 154 F — Dice Game** | `4A#P23` | Coupon Collector Moment EGF + Fast Polynomial Composition |
| **Adv-2** | `#218` | **LOJ 171 / QOJ 6504 — 幂投影 (Power Projection)** | `5B#B16` | Kinoshita–Li Transposed Composition $\sum_i w_i [x^i] F(x)^k$ |
| **Mas-1** | `#235` | **QOJ 8528 — FPS Composition / Power Projection** | `4A#P26` | Kinoshita–Li $O(N \log^2 N)$ Bivariate Parity Splitting Algorithm |
| **Mas-2** | `#017` | **`fps_24_x` — Functional Square Root** | `1A#31` | Iterated Composition $F(F(x)) = G(x)$ in $\mathbb{F}_p[[x]]/(x^N)$ |

#### Corrected `Ch 23` Ladder (`Prereqs <= Ch 23`, 100% $q$-Analogues & Krawtchouk)
- Swap `Ch 23 [Int-1]` (`#172` `Luogu P5366 — [SNOI2017] 遗失的答案`) with `Syn-11` (`#233` `QOJ 5097 / SOJ 703 — 布尔立方 (Boolean Cube)`):
  - `SS-1`: `#123` (`CF 1603F`), `SS-2`: `#033` (`ABC 278 Ex`), `Int-1`: `#233` (`QOJ 5097 / SOJ 703 — 布尔立方`, Gaussian $q$-Binomial $\begin{bmatrix} n \\ k \end{bmatrix}_2$ Subspace Enumeration), `Int-2`: `#057` (`ARC 134 E`), `Adv-1`: `#062` (`ARC 139 F`), `Adv-2`: `#132` (`CF 1916F`), `Mas-1`: `#063` (`ARC 145 F`), `Mas-2`: `#111` (`CF 1336E2`).

---

### 6.2 Master Verification of the 43-Problem Bijective Permutation (`synthesis_v1` $\to$ `synthesis_v2`)

Every single moved problem `#ID` below appears **exactly once in the "Leaves Slot (`v1`)" column** and **exactly once in the "Enters Slot (`v2`)" column**, proving that the `254`-problem bijection is 100% preserved:

| # | Pool ID | Problem ID & Title | Leaves Slot (`v1`) | Enters Slot (`v2`) | New Home Chapter / Routing |
| :-: | :-: | :--- | :--- | :--- | :--- |
| 1 | `#003` | `fps_24_f` — Colored Paper / Colored Tree | `Ch 09 [SS-1]` | **`Ch 11 [SS-1]`** | Ch 11 (Lagrange Inversion $F = x \cosh F$) |
| 2 | `#010` | `fps_24_p` — Ball | `Ch 11 [SS-1]` | **`Ch 11 [Adv-1]`** | Ch 11 (Bivariate Root Shift + Residue) |
| 3 | `#011` | `fps_24_q` — Dice | `Ch 02 [SS-1]` | **`Ch 04 [Adv-2]`** | Ch 04 (Newton–Girard $\ln$ + EGF Moments) |
| 4 | `#025` | ABC 240 G — Teleporting Takahashi | `Ch 17 [SS-1]` | **`Ch 16 [Int-1]`** | Ch 16 (3D $\to$ 1D $\times$ Rotated 2D $(x+y,x-y)$) |
| 5 | `#028` | ABC 260 Ex — Colorfulness | `CP-V.1` | **`Ch 19 [Adv-1]`** | Ch 19 (Coupled D&C NTT + Truncated Taylor Shift) |
| 6 | `#034` | ABC 279 G — At Most 2 Colors | `Ch 05 [Adv-1]` | **`Ch 05 [SS-2]`** | Ch 05 ($O(N)$ Rational Transfer Stepping Stone) |
| 7 | `#035` | ABC 279 Ex — Sum of Prod of Min | `Ch 16 [Int-1]` | **`CP-III.6`** | CP-III $\to$ Ch 03 / Ch 09 (Sparse Product D&C) |
| 8 | `#036` | ABC 281 Ex — Alchemy | `CP-V.8` | **`Ch 21 [SS-1]`** | Ch 21 (Falling-Factorial EGF + All-$n$ `revert`) |
| 9 | `#040` | ABC 300 Ex — Fibonacci: Revisited | `Ch 05 [SS-2]` | **`Ch 05 [Adv-1]`** | Ch 05 (Bostan–Mori + $(1-x)$ Sparse Trick) |
| 10 | `#044` | ABC 336 G — 16 Integers | `Ch 17 [Int-2]` | **`Ch 17 [SS-2]`** | Ch 17 (De Bruijn Eulerian + MacMahon Master Theorem) |
| 11 | `#045` | ABC 345 G — Sugoroku 5 | `Ch 11 [Int-2]` | **`Ch 21 [SS-2]`** | Ch 21 (Hitting-Time PGF + Fast Composition $F(G)$) |
| 12 | `#047` | ABC 387 G — Prime Circuit | `Ch 12 [SS-1]` | **`Ch 21 [Int-1]`** | Ch 21 (Prime-Cycle Cactus Fast Composition $C(T)$) |
| 13 | `#054` | ARC 106 E — Medals | `Ch 21 [SS-2]` | **`CP-VI.5`** | CP-VI $\to$ Ch 24 (Hall's Theorem + SOS Zeta Transform) |
| 14 | `#059` | ARC 137 F — Overlaps | `Ch 09 [Mas-1]` | **`Ch 21 [Int-2]`** | Ch 21 (Implicit Algebraic + Riccati + Composition) |
| 15 | `#060` | ARC 138 E — Decreasing Subsequence | `CP-III.1` | **`Ch 09 [SS-1]`** | Ch 09 (Semi-Online Block CDQ Convolution) |
| 16 | `#064` | ARC 153 D — Sum of Sum of Digits | `CP-V.2` | **`Ch 18 [SS-2]`** | Ch 18 (Carry-Propagation D-Finite Recurrence) |
| 17 | `#068` | AGC 005 F — Many Easy Problems | `CP-VI.5` | **`CP-V.8`** | CP-V $\to$ Ch 20 (Subtree Size Rerooting `mulT`) |
| 18 | `#074` | AGC 058 D — Yet Another ABC String | `Ch 08 [Mas-2]` | **`Ch 16 [Adv-2]`** | Ch 16 (3D Rational Cluster Diagonal $[x^A y^B z^C]$) |
| 19 | `#082` | CF 240F / BZOJ 4899 — 记忆的轮廓 | `Ch 11 [Adv-1]` | **`CP-IV.8`** | CP-IV $\to$ Ch 14 (Tree DP + PGF Stopping Distribution) |
| 20 | `#084` | CF 438E — The Child and Binary Tree | `Ch 02 [Adv-1]` | **`Ch 02 [Adv-2]`** | Ch 02 (Quadratic Radical $2/(1+\sqrt{1-4C})$) |
| 21 | `#090` | CF 848E — Days of Floral Colours | `Ch 18 [Adv-1]` | **`CP-III.1`** | CP-III $\to$ Ch 09 ($4 \times 4$ Rational System + CDQ NTT) |
| 22 | `#091` | CF 891E — Lust | `Ch 21 [Int-2]` | **`Ch 02 [Mas-2]`** | Ch 02 (Product $\prod(a_i - x)$ + Formal Derivative) |
| 23 | `#108` | CF 1264D2 — Beautiful Bracket Sequence (Hard) | `Ch 19 [Adv-1]` | **`CP-V.2`** | CP-V $\to$ Ch 06 / Ch 19 (Hypergeometric Absorption / WZ) |
| 24 | `#125` | CF 1667E — Centroid Probabilities | `Ch 16 [Adv-2]` | **`Ch 18 [Adv-1]`** | Ch 18 (D-Finite Differential Recurrence + Convolution) |
| 25 | `#137` | CF Gym 102331J — Forbidden Strings | `CP-II.8` | **`Ch 08 [Mas-2]`** | Ch 08 (Multi-Pattern Goulden–Jackson Cluster Matrix) |
| 26 | `#141` | LOJ 6222 — Powers of $k$ in Permutations | `Ch 04 [Adv-2]` | **`CP-II.8`** | CP-II $\to$ Ch 04 / Ch 08 (Cycle-Length Sieve $\exp$) |
| 27 | `#146` | Luogu P3684 — 大朋友和多叉树 | `CP-III.6` | **`Ch 12 [Int-1]`** | Ch 12 (Degree-Constrained Rooted Tree Species + LIF) |
| 28 | `#154` | Luogu P4456 — [CQOI2018] 交错序列 | `Ch 19 [SS-1]` | **`Ch 17 [SS-1]`** | Ch 17 (2D Lattice Walk Moment Extraction $\sum i^a j^b$) |
| 29 | `#157` | Luogu P4705 — 玩游戏 | `Ch 21 [Int-1]` | **`Ch 02 [Adv-1]`** | Ch 02 (Newton–Girard Power Sums $\ln\prod(1-a_i x)$) |
| 30 | `#164` | Luogu P5219 — 无聊的水题 I | `Ch 12 [Int-2]` | **`Ch 13 [SS-1]`** | Ch 13 (Bounded-Degree Spanning Tree Warmup) |
| 31 | `#165` | Luogu P5268 — Subset-Sum Product | `Ch 02 [Mas-2]` | **`Ch 02 [SS-2]`** | Ch 02 (Subset-Sum Product $\ln/\exp$ Stepping Stone) |
| 32 | `#172` | Luogu P5366 — [SNOI2017] 遗失的答案 | `Ch 23 [Int-1]` | **`Syn-11`** | Syn-11 (Ch 08 Divisor IE $\times$ Ch 24 FWT OR/AND) |
| 33 | `#176` | Luogu P5434 — 有标号荒漠计数 | `Ch 12 [SS-2]` | **`Ch 12 [SS-1]`** | Ch 12 (Labeled Desert $\exp(C_{\text{cactus}})$ Stepping Stone) |
| 34 | `#196` | Luogu P6672 — 你的生命已如风中残烛 | `Ch 17 [SS-2]` | **`Ch 11 [Int-1]`** | Ch 11 (1D Raney's Lemma Cyclic Shift $\frac{1}{m+1}$) |
| 35 | `#201` | Luogu P7439 — [KrOI2021] 蕾切尔 | `Ch 11 [Int-1]` | **`Ch 11 [Int-2]`** | Ch 11 (Formal Residue Change of Variables) |
| 36 | `#206` | UOJ 50 — [UR #3] 链式反应 | `Ch 02 [Adv-2]` | **`Ch 09 [Mas-1]`** | Ch 09 (Non-Autonomous ODE $F'=\frac{1}{2}AF^2+1$ via CDQ) |
| 37 | `#219` | LOJ 3398 — 带加强和多项木 | `CP-IV.8` | **`Ch 17 [Int-2]`** | Ch 17 (Multivariate Implicit Tree + Good–Lagrange) |
| 38 | `#227` | LOJ 6569 — 仙人掌计数 | `Ch 12 [Int-1]` | **`Ch 12 [Int-2]`** | Ch 12 (Pointed Cactus Functional Equation) |
| 39 | `#233` | QOJ 5097 / SOJ 703 — 布尔立方 | `Syn-11` | **`Ch 23 [Int-1]`** | Ch 23 (Gaussian $q$-Binomial $\begin{bmatrix} n \\ k \end{bmatrix}_2$ Subspaces) |
| 40 | `#236` | yukicoder 963 — 門松列列 2 | `Ch 18 [SS-2]` | **`CP-V.1`** | CP-V $\to$ Ch 19 (Coupled ODE $S'=1+S^2, C'=SC$) |
| 41 | `#238` | yukicoder 1145 — Sum of Powers | `Ch 21 [SS-1]` | **`Ch 02 [SS-1]`** | Ch 02 (Newton–Girard Power Sums $-\sum \frac{-a_i x}{1-a_i x}$) |
| 42 | `#242` | yukicoder 1939 — Numbered Colorful Balls | `Ch 02 [SS-2]` | **`Ch 19 [SS-1]`** | Ch 19 ($O(NK)$ Sparse EGF Differential Recurrence) |
| 43 | `#245` | 51Nod 1728 — 不动点 | `Ch 13 [SS-1]` | **`Ch 12 [SS-2]`** | Ch 12 (Endofunction Cycles of Height-$\le k$ Trees) |

*(Bijection Proof: The multiset of 43 "Leaves Slot (`v1`)" positions and the multiset of 43 "Enters Slot (`v2`)" positions are **100% identical**! Every single chapter `Ch 01`–`Ch 24` retains `8` disjoint problems, every Blind Checkpoint `CP-I`–`CP-VI` retains `8` disjoint problems, and the Synthesis Reserve retains `14` disjoint problems.)*
