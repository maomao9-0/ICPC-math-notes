# Phase 1.5 Final Cross-File Consistency & Bijective Verification Audit

**Audit Scope**:
- [`fps_research/CURRICULUM_ARCHITECTURE.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md) (`CA`)
- [`fps_research/PROBLEM_CURATION.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md) (`PC`)
- [`fps_research/problem_archive.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md) (`PA`)
- Round 2 Benchmark Critiques: [`critic_round2_taxonomy_and_dag.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/phase1_5/critic_round2_taxonomy_and_dag.md) (Critic A) & [`critic_round2_problem_and_ladder_audit.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/phase1_5/critic_round2_problem_and_ladder_audit.md) (Critic B)

---

## 0. Executive Summary & Scorecard

| Audit Dimension | Status | Findings Summary |
| :--- | :--- | :--- |
| **1A. Round 2 Critic A & Critic B Incorporation** | **96% Complete (4 Residual Gaps)** | All 16 Canonical Failure Modes (`CA §2.4`), the 43-problem bijective permutation (`Critic B §6.1–6.2`), and 22 of 24 chapter sub-section fixes are live. Four residual gaps remain: (1) `Ch 13` sub-section split-brain between `CA` and `PC`, (2) `Ch 03` missing `3.5` in `CA`, (3) `Ch 16 [Mas-2] #214` table cell still says `"3D Algebraic Diagonal"`, and (4) 3 problem-identity issues (`#165 Luogu P5268`, `#220/#128` in `Ch 15`, `#216 LOJ 154` in `Ch 24`). |
| **1B. Chapter Title & Sub-Section Alignment (`Ch 01`–`Ch 24`)** | **24/24 Titles Match; Sub-Section Drift in `Ch 03, 06, 10, 11, 13, 16–24`** | Chapter titles (`Ch 01`–`Ch 24`) and Unit headers (`Unit I`–`Unit VI`) match 100%. However, `CA` updated its sub-sections in Round 2 while `PC` kept the Round 1 sub-section headers in `Ch 10, 11, 13, 16–24`, and `CA` dropped `3.5` (Burnside/Pólya) and `13.1–13.3` (Graphical/Bipartite/DAG/SCC EGFs). Additionally, 5 Checkpoint Stage 2 rows contain dangling sub-section numbers (`3.5`, `6.5`, `11.5`, `14.5`). |
| **2A. 254-Slot-to-`#ID` Bijective Mapping** | **PASS (100% Match Across All 5 Tables)** | Across `CA` Main Ladders, `CA §6.2` 4-Column Index, `PC` Main Ladders, `PC §6.1` Master Directory, and `PA §0` Routing Table, every single slot (`Ch 01 [SS-1]` through `Ch 24 [Mas-2]`, `CP-I.1` through `CP-VI.8`, `Syn-01` through `Syn-14`) maps to the **exact same `#ID`** (`#001`–`#254`). Zero missing IDs, zero duplicate `#ID`s. |
| **2B. `#ID`-to-Problem-Title Identity across `CA` vs. `PC`/`PA`** | **FAIL (53 Split-Brain Title Divergences in `CA`)** | While `PC` Main, `PC §6.1`, and `PA §0` agree 100% on all 254 `(Slot, #ID, Problem Title)` triples, **`CA` exhibits a split-brain synchronization bug in 53 un-swapped slots (`51` Chapter Ladder rows + `2` Checkpoint Stage 1 rows)**: `CA` updated the `#ID` column to match `PC` (and used `PC`'s titles in `CA §5.2`), but left `synthesis_v1_curriculum_architecture.md`'s old Round 1 problem titles sitting next to `PC`'s `#ID` numbers! This creates 15 internal duplicate problem titles and 3 quarantined template leaks inside `CA`. |
| **3. Quarantined Templates (`R-01`–`R-67`) & Formatting Integrity** | **PASS (100% Match & 0 Formatting Errors)** | All 67 quarantined templates (`R-01`–`R-67`) match 100% in problem identity and chapter assignment between `CA §6.1` and `PC §5.1`. Across `CA`, `PC`, and `PA`, there are **0** forbidden LaTeX paren/bracket math delimiters and **0** unescaped vertical bars `|` inside `$...$` in Markdown tables. |

---

## 1. Chapter Title & Sub-Section Alignment (`Ch 01`–`Ch 24`)

### 1.1 Verification of Round 2 Critic A (`critic_round2_taxonomy_and_dag.md`) Upgrades
1. **All 16 Canonical Failure Modes Incorporated**: `CA §2.4` (`L121–L142`) now explicitly codifies all 16 failure modes (`#1`–`#16`), including the 6 newly mandated Round 2 additions:
   - `#11`: Missing $x\frac{d}{dx}$ radial derivation before multivariate diagonals (`Ch 16`).
   - `#12`: $F(0) \neq 0$ or $F'(0) = 0$ breakdown in composition/compositional inverse (`Ch 11` / `Ch 21`).
   - `#13`: Non-simple or colliding characteristic roots $\alpha_i = \alpha_j$ in partial fraction expansion (`Ch 04`).
   - `#14`: Chirp Z-Transform base $c=0$ or $c^k \equiv 1 \pmod p$ degeneracy (`Ch 07` / `Ch 20`).
   - `#15`: Off-by-one boundary shifts in bivariate Reflection Principle / Kernel Method (`Ch 15`).
   - `#16`: Forgetting the $\frac{1}{k!}$ symmetry factor in $\exp(F(x))$ or the base-point shift in $\ln(1+F(x))$ (`Ch 02` / `Ch 12` / `Ch 24`).
2. **Round 2 Mathematical & Algorithmic Sub-Section Fixes Incorporated in `CA`**:
   - **`Ch 02` vs `Ch 10` Boundary (`CA L248, L557–558`)**: `Ch 02` derives $O(n \log n)$ Newton lifting exclusively for algebraic/transcendental primitives (`inv`, `sqrt`, `ln`, `exp`, `pow`), while `Ch 10` (`10.1` CDQ Divide-and-Conquer NTT, `10.2` Generalized Newton Iteration $G(F)=0$ for implicit combinatorial equations) owns `10.2`.
   - **`Ch 12.4` vs `Ch 13.4` Symbolic Matrix-Tree Split (`CA L641, L678`)**: `Ch 12.4` is restricted to Weighted Prüfer Sequences & Degree-Constrained Tree Reductions, while Symbolic Matrix-Tree over truncated polynomial rings $R[x]/(x^{k+1})$ is consolidated into `Ch 13.4`.
   - **`Ch 16.3–16.4` Radial Derivation & Lipshitz's Theorem (`CA L799–800`)**: Explicitly separates `16.3` Algebraic Diagonals via Radial Derivation $\mathfrak{D} = x\frac{d}{dx}$ from `16.4` Lipshitz's Theorem & 3D D-Finite Diagonals (`UOJ 596`).
   - **`Ch 17.1–17.4` Bipartite Good–Lagrange & Obstinate Kernel (`CA L836–839`)**: Explicitly includes `17.1` Rank-2 Jacobians & Bipartite Tree/Forest Inversion (`ARC 176 E`) and `17.4` Quadrant Lattice Walks & Obstinate Kernel Method (`Luogu P4494`).
   - **`Ch 18.3` 7 Canonical ODE Archetypes (`CA L879`)**: Explicitly enumerates all 7 non-linear combinatorial ODE archetypes (`Catalan`, `Tree`, `Set`, `Cycle`, `Bell`, `Euler`, `Increasing Tree`).
   - **`Ch 19.2–19.3` WZ Method & `EI 科技` (`CA L916–917`)**: Explicitly names `19.2` Wilf–Zeilberger (WZ) Method & Creative Telescoping and `19.3` ODE-to-Recurrence Extraction & `EI 科技` $\Theta(n)$-Term Reduction (`Luogu P6667`, `LOJ 6728`).
   - **`Ch 20.4` Transposed Chirp Z-Transform (`CA L957`)**: Explicitly adds `20.4` Transposed Chirp Z-Transform ($\text{czt}^\top$) for geometric-progression evaluation and interpolation.
   - **`Ch 21.4` Dual-Route Char-$p$ Inversion (`CA L996`)**: Unifies Route A (Freshman's Dream $F(x)^p = F(x^p)$ elimination) and Route B ($O(n \log^2 n)$ `revert` when $n < p$), plus Artin–Schreier roots (`LOJ 6509`).
   - **`Ch 22.2` 3-Way Weighted Heavy-Light Split & $3c^2$ Fourier Matrix Product (`CA L1033`)**: Explicitly codifies the 3-way split (Heavy Child / Light Children / Subtree Boundary) and the $9 \to 3$ point-value NTT cache optimization.
   - **`Ch 23.2–23.4` $q$-Lucas, Durfee Squares, & 5-Line Krawtchouk Derivation (`CA L1071–1073`)**: All three Critic A requirements are present.
   - **`Ch 24.3–24.4` Pointed Biconnected SPS & $\Omega(n)$-Graded Derivation (`CA L1111–1112`)**: Explicitly adds `Elegia`'s $O(n^2 2^n)$ SPS composition, Pointed Biconnected Graph SPS (`UOJ 910`), and the $\Omega(n)$-graded derivation $D(A)_n = \Omega(n) A_n$ (`UOJ 752`).

### 1.2 Sub-Section Divergences & Split-Brain Issues Between `CA` and `PC`

While `CA` and `PC` have **identical chapter titles** for all 24 chapters, their sub-section lists (`X.1`–`X.4/X.5`) diverged during Round 2 edits:

| Chapter | `CURRICULUM_ARCHITECTURE.md` (`CA`) Sub-Sections | `PROBLEM_CURATION.md` (`PC`) Sub-Sections | Audit Verdict & Required Fix |
| :--- | :--- | :--- | :--- |
| **Ch 03** | `3.1` Partitions & Ferrers; `3.2` Euler's Pentagonal Theorem; `3.3` $O(n\sqrt{n})$ Bounded Knapsack; `3.4` Euler Transform | `3.1` Ferrers & Pentagonal; `3.2` $O(n\sqrt{n})$ Knapsack; `3.3` Euler & **Inverse Euler Transform**; `3.4` Twelvefold Way; `3.5` **Burnside's Lemma & Pólya's Cycle Index Theorem** | **Merge into 5 Sub-Sections in Both Files**: `CA` dropped Inverse Euler Transform (needed by `#223 LOJ 6268`) and `3.5` Burnside/Pólya (needed by `#159 Luogu P4727` and cited by `CA` itself at `L1199` `CP-I.7`!). Standardize both `CA` and `PC` to `3.1`–`3.5`. |
| **Ch 06** | `6.1` $\Delta$ & Newton-Gregory; `6.2` Euler–Maclaurin; `6.3` Consecutive Lagrange Interpolation; `6.4` Falling Factorial Basis & Polynomial Shift | `6.1` $\Delta$, Newton-Gregory & Falling Factorial; `6.2` Falling-Factorial Multiplication; `6.3` Polynomial Shift $F(x+c)$; `6.4` Consecutive Lagrange & Euler–Maclaurin | **Align Sub-Section Order + Fix `CP-II.4`**: Both `CA L1232` and `PC L765` (`CP-II.4 #252`) cite a non-existent `6.5`! Change `6.5` in `CP-II.4` to `6.3/6.4` and align `6.1`–`6.4` headers across both files. |
| **Ch 10** | `10.1` CDQ Divide-and-Conquer NTT; `10.2` Generalized Newton Iteration $G(F)=0$; `10.3` Semi-Online & Fully-Online (`Mivik`) Convolution; `10.4` Multi-Track Mutual CDQ | `10.1` CDQ NTT; `10.2` Semi-Online & Fully-Online (`Mivik`); `10.3` Implicit Newton Iteration; `10.4` Multi-Track Mutual CDQ | **Adopt `CA`'s `10.1`–`10.4` in `PC`**: `CA`'s order matches Critic A's mandate (`10.2` Generalized Newton Iteration). |
| **Ch 11** | `11.1` Formal Laurent Series $K((x))$ & Formal Residue; `11.2` LIF & Characteristic-$p$ Lifting; `11.3` Implicit Tree/Forest Equations & Raney's Lemma | `11.1` $K((x))$ & Residue; `11.2` Classical & Generalized LIF; `11.3` Raney's Lemma & Catalytic Reduction; `11.4` Characteristic-$p$ LIF | **Adopt `PC`'s 4-Sub-Section Structure (`11.1`–`11.4`) + Fix `CP-III.7`**: Separating `11.4` Characteristic-$p$ LIF (`UOJ 751`) is cleaner. Also fix `CA L1271` (`CP-III.7 #205`), which cites a non-existent `11.5` (change to `11.4`). |
| **Ch 13** | `13.1` Kirchhoff's Matrix-Tree; `13.2` BEST Theorem; `13.3` Rank-1 Perturbations; `13.4` Symbolic Matrix-Tree over $R[x]/(x^{k+1})$ | `13.1` Graphical EGFs & Eulerian Graphs ($\ln/\exp$ + $2^{-\binom{n}{2}}$ Twist); `13.2` Bipartite Graphs & Hurwitz EGFs; `13.3` DAGs & Strongly Connected Digraphs; `13.4` Biconnected Components (Block-Cut Trees) | **CRITICAL SPLIT-BRAIN**: `CA` replaced all of `Ch 13` with Matrix-Tree sub-sections, **completely deleting the theoretical text for 5 of the 8 problems in `Ch 13`'s ladder** (`#199 Luogu P7364`, `#053 ARC 105 F`, `#189 Luogu P6295`, `#122 CF 1556F`, `#226 LOJ 6512`)! Conversely, `PC` kept `13.4` as Biconnected Block-Cut Trees (duplicating `Ch 12.3`) and omitted Matrix-Tree/BEST/Symbolic Matrix-Tree (`#055 ARC 118 E`, `#185 Luogu P5807`, `#170 Luogu P5296`, `#136 CF 1906D`)! **Resolution**: Unify both `CA` and `PC` as: `13.1` Graphical Generating Functions & Connected Graphs ($\ln/\exp$ & $2^{-\binom{n}{2}}$ CZT Twist); `13.2` Bipartite Graphs & 2-Colored Hurwitz EGFs; `13.3` Acyclic Digraphs (DAGs) & Strongly Connected Digraphs (Robinson–Stanley Inclusion-Exclusion); `13.4` Kirchhoff's Matrix-Tree, BEST Theorem & Symbolic Matrix-Tree over $R[x]/(x^{k+1})$. |
| **Ch 14** | `14.1` PGFs ($G(1), G'(1), G''(1)$); `14.2` Stopping Times; `14.3` Penney's Game; `14.4` Martingales & Optional Stopping | Identical `14.1`–`14.4` | **Fix Dangling `14.5` in `CP-IV.3` & `CP-IV.4`**: Both `CA L1303–1304, L1425` and `PC L836–837` cite `14.5 Martingale / PGF Stopping Time` for `#099` and `#116`, even though `Ch 14` ends at `14.4`. Change `14.5` to `14.4` in both files. |
| **Ch 16–24** | `CA` includes all Round 2 Critic A sub-section updates (`16.3–16.4`, `17.1/17.4`, `18.3`, `19.2–19.3`, `20.4`, `21.4`, `22.2`, `23.2–23.4`, `24.3–24.4`). | `PC` still displays Round 1 sub-section titles in `Ch 16–24` headers. | **Copy `CA`'s `Ch 16`–`Ch 24` Sub-Section Headers into `PC`**: Ensures 100% sub-section parity across both architectural documents. Also update the table cell in `CA L818`, `PC L482`, and `PA L298` for `Ch 16 [Mas-2] #214` (`UOJ 596`) from `"3D Algebraic Diagonal"` to `"3D D-Finite Diagonal / Radial Derivation \mathfrak{D}"`. |

---

## 2. 254-Problem Slot-by-Slot Identity Check (`CA` vs. `PC` vs. `PA`)

### 2.1 Slot-to-`#ID` Bijective Verification (`100%` Match)
A programmatic cross-check of all 254 problem slots across all 5 master tables:
1. `CA` Main Chapter Ladders (`Ch 01`–`Ch 24`: 192 slots), Blind Checkpoints (`CP-I`–`CP-VI`: 48 slots), and Capstone Synthesis (`Syn-01`–`Syn-14`: 14 slots)
2. `CA §6.2` Compact 4-Column Master Index (`L1579–1647`)
3. `PC` Main Chapter Ladders, Blind Checkpoints, and Capstone Synthesis
4. `PC §6.1` Complete 254-Problem Directory (`L1047–1304`)
5. `PA §0` Master Bidirectional Routing Table (`L144–401`)

confirms **zero slot-to-`#ID` discrepancies (`0 / 254`)**. Every `#ID` from `#001` to `#254` appears **exactly once** in each of the 5 tables, and every single slot (`Ch 01 [SS-1]` through `Syn-14`) is assigned the **exact same `#ID`** across all three files.

### 2.2 The 53 `#ID`-to-Problem-Title Split-Brain Divergences in `CURRICULUM_ARCHITECTURE.md`

Despite 100% agreement on `Slot -> #ID`, **`CA` and `PC`/`PA` disagree on the Problem Title / Judge ID in 53 slots (`51` Chapter Ladder rows + `2` Checkpoint Stage 1 rows)**, plus `1` dual-judge alias (`Ch 22 [Mas-1] #166`) and `19` rows where only the Wave Pointer column differs.

#### Root Cause Diagnosis
During Round 1, `synthesis_v1_curriculum_architecture.md` and `synthesis_v2_problem_curation.md` independently populated several chapter ladders using different problems from the research waves. In Round 2:
1. `PC` (`PROBLEM_CURATION.md`) and `PA` (`problem_archive.md`) established the canonical 1-to-1 bijection `#001`–`#254` (`PC §6.1` and `PA §0` match 100% on all 254 `#ID`s, titles, and slots).
2. When `CA` (`CURRICULUM_ARCHITECTURE.md`) applied Critic B's 43-problem permutation, `CA` updated all 43 swapped slots to `PC`'s exact `#ID` and Problem Title, and updated the `#ID` column in the remaining 211 slots—**but in 53 un-swapped rows across `Ch 01, 03, 05, 06, 07, 14, 15, 20, 22, 24` and `CP-II.8, CP-IV.8`, `CA` left its old Round 1 problem titles sitting next to `PC`'s `#ID` numbers!**
3. **Internal Proof Inside `CA`**:
   - In `CA §5.2` (Revisited Problems Index, `L1419`), `CA` writes: `` `#094` | **CF 923E** — *Perpetual Subtraction* | `Ch 06 [Adv-1]` ``—matching `PC`! Yet in `CA`'s `Ch 06` ladder table (`L421`), `CA` writes: `` `#094` | **CF 891E** — *Lust* ``!
   - In `CA §5.2` (`L1425`), `CA` writes: `` `#156` | **Luogu P4548** — *[CTSC2006] 歌唱王国* | `Ch 14 [Int-1]` ``—matching `PC`! Yet in `CA`'s `Ch 14` ladder table (`L728`), `CA` writes: `` `#156` | **Luogu P3706** — *[SDOI2017] 硬币游戏* ``!
   - In `CA §5.2` (`L1426`), `CA` writes: `` `#220` | **LOJ 6160** | `Ch 15 [Int-1]` ``, whereas in `CA`'s `Ch 15` ladder table (`L765`), `CA` writes: `` `#220` | **AtCoder ABC 205 E / ARC 145 D / Luogu P3266** ``!
4. **Catastrophic Side Effects of `CA`'s Stale Titles**: Because `CA` updated the 43 swapped rows to `PC`'s titles while leaving the 53 un-swapped rows with Round 1 titles, `CA` currently contains **15 duplicate problems** and **3 quarantined template leaks** inside its own tables:
   - **15 Internal Duplicates in `CA`**: `fps_24_f` (`Ch 01 Int-1 #004` & `Ch 11 SS-1 #003`), `CF 451E` (`Ch 01 Int-2 #077` & `CP-II.1 #085`), `Luogu P6078` (`Ch 03 SS-2 #188` & `Ch 05 Int-1 #187`), `LOJ 6089` (`Ch 03 Adv-1 #223` & `Ch 03 SS-2 #188` in `PC`), `CF 891E` (`Ch 06 Adv-1 #094` & `Ch 02 Mas-2 #091`), `CF 923E` (`Ch 06 Adv-2 #096` & `CA §5.2 #094`), `Luogu P5591` (`Ch 07 SS-2 #104` & `Ch 07 Int-1 #183`), `Luogu P3321` (`Ch 07 Int-1 #183` & `Ch 07 Int-2 #141`), `Luogu P5326` (`Ch 14 Adv-1 #148` & `CP-IV.2 #169`), `UOJ 310` (`Ch 14 Adv-2 #209`, `Ch 24 SS-1 #216`, & `CP-VI.6 #206`), `CF 1264D2` (`Ch 15 SS-2 #070` & `CP-V.2 #108`), `UOJ 424` (`Ch 15 Adv-2 #134` & `Ch 15 Mas-2 #210`), `CF 1336E2` (`Ch 15 Mas-1 #076` & `Ch 23 Mas-2 #111`), `CF 1613F` (`Ch 20 Int-1 #127` & `Ch 22 SS-2 #124`), `ABC 281 Ex` (`Ch 20 Int-1 #127` & `Ch 21 SS-1 #036`), `UOJ 604` (`Ch 20 Mas-2 #217` & `CP-V.6 #215`).
   - **3 Quarantined Template Leaks in `CA`**: `fps_24_j` (`R-44` equivalent in `Ch 06 SS-1 #005`), `Luogu P5282` (`R-35` in `Ch 20 Int-2 #167`), `Luogu P5495` (`R-39` in `Ch 24 Adv-2 #207`), plus `ABC 205 E` (`R-63` in `Ch 15 Int-1 #220`).

#### Complete 53-Problem Reconciliation Table (`CA` vs. `PC`/`PA`)

| `#ID` | Assigned Slot | `CA` Line & Stale Title in `CURRICULUM_ARCHITECTURE.md` | `PC` Line & Canonical Title in `PROBLEM_CURATION.md` / `problem_archive.md` | Authoritative Resolution & Prerequisite Audit |
| :--- | :--- | :--- | :--- | :--- |
| `#004` | `Ch 01 [Int-1]` | `L219`: **AtCoder `fps_24_f`** — *Colorful Balls* | `L139`: **AtCoder `fps_24_g`** — *Coin (`1G#2`)* | **Adopt `PC` (`fps_24_g`)**: `fps_24_f` is already `#003` (`Ch 11 SS-1`). `fps_24_g` is 100% forward-reference-free `Ch 01` OGF product modeling. |
| `#077` | `Ch 01 [Int-2]` | `L220`: **Codeforces 451E** — *Devu and Flowers* | `L140`: **CSES 1729 / AtCoder ARC 116 E** — *Stick Game / Spread of Information (`1A#5`)* | **Adopt `PC` (`CSES 1729 / ARC 116 E`)**: `CF 451E` is already `#085` (`CP-II.1`). |
| `#087` | `Ch 01 [Adv-2]` | `L222`: **Codeforces 993E** — *Nikita and Order Statistics* | `L142`: **Codeforces 623E** — *Transforming Sequence (`1B#5`)* (`O(k^2)` Bonus) | **Adopt `PC` (`CF 623E` $O(k^2)$ DP Bonus)**: Note that `CF 993E` (`CA`) is also a clean `Ch 01` cross-correlation problem (`PC` lists `CF 993E` in `R-01` replacements), so either synchronize `CA` to `#087 CF 623E (O(k^2) Bonus)` or keep `CF 623E` as `PC` specifies. |
| `#188` | `Ch 03 [SS-2]` | `L299`: **Luogu P6078** — *[CEOI2004] Sweets* | `L195`: **LOJ 6089** — *小 Y 的背包计数问题 (`2A#2`)* | **Adopt `PC` (`LOJ 6089`)**: `Luogu P6078` is already `#187` (`Ch 05 Int-1`). `LOJ 6089` is the canonical $O(n\sqrt{n})$ bounded knapsack problem (`3.3`). |
| `#223` | `Ch 03 [Adv-1]` | `L302`: **LOJ 6089** — *小 Y 的背包计数问题* | `L198`: **LOJ 6268** — *分拆数 (Inverse Euler Transform) (`2A#5`)* | **Adopt `PC` (`LOJ 6268`)**: Eliminates the `LOJ 6089` duplicate and tests `3.4` Inverse Euler Transform. |
| `#047` | `Ch 03 [Adv-2]` | `L303`: **AtCoder AGC 043 D** — *Merge Triplets* | `L199`: **AtCoder AGC 036 D / CF 1156E** — *Negative Cycle / Partition Bounds (`2A#6`)* | **Adopt `PC` (`AGC 036 D`)**: `AGC 043 D` requires $\exp/\ln$ on bounded cycle blocks (`Ch 02`/`Ch 12`), whereas `AGC 036 D` fits `Ch 03`. |
| `#022` | `Ch 03 [Mas-1]` | `L304`: **AtCoder ABC 221 H** — *Count Multiset* | `L200`: **AtCoder ABC 253 Ex / ARC 145 E** — *We Love Forest / Partition Variants (`2A#7`)* | **Adopt `PC` (`ARC 145 E` Partition Variant)**: Note: ensure the description emphasizes the `ARC 145 E` partition variant (or `ABC 221 H`), not `ABC 253 Ex` (which is Set Power Series `Ch 24`). |
| `#159` | `Ch 03 [Mas-2]` | `L305`: **Luogu P4191** — *[CTSC2010] 性能优化* | `L201`: **Luogu P4727** — *[HNOI2009] 图的同构记数 (`2B#4`)* | **Adopt `PC` (`Luogu P4727`)**: `Luogu P4191` requires Bluestein CZT (`Ch 07`), which is a **forward reference** in `Ch 03`! `Luogu P4727` tests Burnside/Pólya cycle index over partitions (`3.5`). |
| `#008` | `Ch 05 [Adv-1]` | `L382`: **AtCoder ABC 138 F / ARC 116 C** — *Coincidence / Multiple Sequences* | `L254`: **AtCoder ABC 172 F / CF 1260F** — *Unfair Nim / Colored Tree (`1A#10`)* | **Adopt `PC` (`ABC 172 F / CF 1260F`)**: `ARC 116 C` is already `#056` (`Ch 05 SS-1`). |
| `#054` | `Ch 05 [Adv-2]` | `L383`: **AtCoder ARC 110 D** — *Binomial Coefficient is Fun* | `L255`: **AtCoder ARC 116 D** — *I Wanna Win The Game (`1A#11`)* | **Adopt `PC` (`ARC 116 D`)**: `ARC 110 D` is already `#058` (`CP-II.2`). |
| `#005` | `Ch 06 [SS-1]` | `L417`: **AtCoder `fps_24_j`** — *Polynomial Shift* | `L282`: **AtCoder ABC 154 F / CF 622F** — *Many Many Paths / The Sum of the k-th Powers (`2B#6`)* | **Adopt `PC` (`ABC 154 F / CF 622F`)**: `fps_24_j` is a pure shift template, whereas `CF 622F` is the canonical $O(k)$ consecutive Lagrange interpolation problem (`6.3`). |
| `#083` | `Ch 06 [SS-2]` | `L418`: **Codeforces 622F** — *The Sum of the k-th Powers* | `L283`: **Codeforces 280C / CF 711E** — *Birthday Paradox & Finite Difference Warmup (`2B#7`)* | **Adopt `PC` (`CF 711E` Finite Difference Warmup)**: Avoids duplicating `CF 622F` (`#005`). |
| `#109` | `Ch 06 [Int-1]` | `L419`: **Luogu P5395** — *第二类斯特林数·行* | `L284`: **Codeforces 1278F** — *Cards (`2B#8`)* | **Adopt `PC` (`CF 1278F`)**: `Luogu P5395` is quarantined template `R-27`! `CF 1278F` is the classic falling-factorial $E[X^k] = \sum S(k,j) \binom{n}{j} j! p^j$ problem (`6.4`). |
| `#192` | `Ch 06 [Int-2]` | `L420`: **Codeforces 1278F** — *Cards* | `L285`: **Luogu P6620** — *[省选联考 2020 A 卷] 组合数问题 (`2B#9`)* | **Adopt `PC` (`Luogu P6620`)**: Eliminates the `CF 1278F` shift and pairs `CF 1278F` (`Int-1`) with `Luogu P6620` (`Int-2`). |
| `#094` | `Ch 06 [Adv-1]` | `L421`: **Codeforces 891E** — *Lust* | `L286`: **Codeforces 923E** — *Perpetual Subtraction (`1B#9`)* | **Adopt `PC` (`CF 923E`)**: `CA §5.2` (`L1419`) already lists `#094` as `CF 923E`! (`CF 891E` is `#091` in `Ch 02 Mas-2`). |
| `#096` | `Ch 06 [Adv-2]` | `L422`: **Codeforces 923E** — *Perpetual Subtraction* | `L287`: **Codeforces 960G / Luogu P4091** — *[HEOI2016] 求和 (`2B#10`)* | **Adopt `PC` (`Luogu P4091`)**: Eliminates the `CF 923E` duplicate. (Write `Luogu P4091 — [HEOI2016] 求和` without `CF 960G`, since `CF 960G` is `#095` in `Ch 08 Adv-1`). |
| `#046` | `Ch 06 [Mas-1]` | `L423`: **Luogu P6620** — *[省选联考 2020 A 卷] 组合数问题* | `L288`: **AtCoder AGC 034 F / CF 1097G** — *Vladislav and a Great Legend (`2B#11`)* | **Adopt `PC` (`CF 1097G`)**: Eliminates the `Luogu P6620` duplicate and tests falling-factorial $x^k = \sum S(k,j) x^{\underline{j}}$ on trees (`6.4`). |
| `#176` | `Ch 06 [Mas-2]` | `L424`: **Luogu P5401** — *[CTS2019] 珍珠* | `L289`: **Luogu P5396 / LOJ 6059** — *Falling Factorial Polynomial Multiplication (`2B#12`)* | **Adopt `PC` (`LOJ 6059`)**: `Luogu P5401` is already `#175` (`Ch 07 Adv-1`)! |
| `#180` | `Ch 07 [SS-1]` | `L457`: **Codeforces 1054H / Gym 102978C** — *2D Roots of Unity Filter Warmup* | `L312`: **Luogu P5591** — *小猪佩奇学数学 (`1B#10`)* | **Adopt `PC` (`Luogu P5591`)**: `CF 1054H` is already `#104` (`Ch 07 SS-2` in `PC`)! `Luogu P5591` is the cleanest pure Roots of Unity Filter `[k \mid i]` warmup (`7.1`). |
| `#104` | `Ch 07 [SS-2]` | `L458`: **Luogu P5591** — *小猪佩奇学数学* | `L313`: **Codeforces 1054H** — *Epic Convolution (`1B#11`)* | **Adopt `PC` (`CF 1054H`)**: Eliminates the shift between `SS-1` and `SS-2`. |
| `#183` | `Ch 07 [Int-1]` | `L459`: **Luogu P3321** — *[SDOI2015] 序列统计* | `L314`: **Luogu P5643 / HDU 5852** — *Cyclic Convolution mod $(x^k-1)$ (`1B#12`)* | **Adopt `PC` (`HDU 5852` Cyclic Convolution mod $x^k-1$)**: `Luogu P3321` is `#141` (`Ch 07 Int-2` in `PC`). Note: drop the `Luogu P5643` alias here (as `P5643` is `#184` in `Ch 24`) and refer to `#183` as `HDU 5852 / Cyclic Convolution mod (x^k - 1)`. |
| `#141` | `Ch 07 [Int-2]` | `L460`: **Codeforces 901E** — *Periodic* | `L315`: **Luogu P3321** — *[SDOI2015] 序列统计 (`1B#13`)* | **Adopt `PC` (`Luogu P3321`)**: `Luogu P3321` is the canonical primitive-root discrete log $\to$ cyclic NTT (`7.3`) problem. |
| `#114` | `Ch 07 [Mas-1]` | `L463`: **Codeforces 1054H** — *Epic Convolution* | `L318`: **Codeforces 1334G** — *Substring Search (`1B#16`)* | **Adopt `PC` (`CF 1334G`)**: Eliminates the internal `CF 1054H` duplicate in `CA` (`SS-1` & `Mas-1`). |
| `#156` | `Ch 14 [Int-1]` | `L728`: **Luogu P3706** — *[SDOI2017] 硬币游戏* | `L442`: **Luogu P4548** — *[CTSC2006] 歌唱王国 (`4B#3`)* | **Adopt `PC` (`Luogu P4548`)**: `CA §5.2` (`L1425`) already lists `#156` as `Luogu P4548`! Single-string PGF + KMP borders (`14.2`) precedes multi-string Penney's Game (`Int-2 #151 Luogu P3706`). |
| `#151` | `Ch 14 [Int-2]` | `L729`: **Codeforces 1097D** — *Makoto and a Blackboard* | `L443`: **Luogu P3706** — *[SDOI2017] 硬币游戏 (`4B#4`)* | **Adopt `PC` (`Luogu P3706`)**: `Luogu P3706` is the exact $N$-player $O(N^3)$ Penney's Game linear system (`14.3`). |
| `#148` | `Ch 14 [Adv-1]` | `L730`: **Luogu P5326** — *[ZJOI2019] 开关* | `L444`: **Luogu P3343** — *[ZJOI2015] 地震后的幻想乡 (`4B#5`)* | **Adopt `PC` (`Luogu P3343`)**: `Luogu P5326` is already `#169` (`CP-IV.2`). |
| `#209` | `Ch 14 [Adv-2]` | `L731`: **UOJ 310** — *[UNR #2] 黎明前的巧克力* | `L445`: **UOJ 418 / Luogu P4769** — *Stopping Time PGF (`4B#6`)* | **Adopt `PC` (`UOJ 418`)**: `UOJ 310` is already `#206` (`CP-VI.6`), and requires Set Power Series FWT (`Ch 24`), which is a **severe forward reference** in `Ch 14`! |
| `#117` | `Ch 14 [Mas-1]` | `L732`: **Codeforces 1349D** — *Slime and Biscuits* | `L446`: **Codeforces 1479E** — *School Clubs (`4B#7`)* | **Adopt `PC` (`CF 1479E`)**: `CF 1349D` is `#116` (`CP-IV.4`) and `#115` (`Ch 14 Mas-2`). `CF 1479E` pairs with `CF 1349D` for potential-function martingale mastery (`14.4`). |
| `#115` | `Ch 14 [Mas-2]` | `L733`: **Codeforces 1479E** — *School Clubs* | `L447`: **Codeforces 1349D** — *Slime and Biscuits (`4B#8`)* | **Adopt `PC` (`CF 1349D`)**: Swaps `Mas-1` and `Mas-2` to match `PC` and `PA`. |
| `#152` | `Ch 15 [SS-1]` | `L763`: **AtCoder ABC 240 F / CF 1194E** — *Reflection Principle Ballot Warmup* | `L460`: **Luogu P3978** — *[TJOI2015] 概率论 (`4B#9`)* | **Adopt `PC` (`Luogu P3978`)**: Classic Dyck path / Catalan generating function $C(x) = 1 + x C(x)^2$ leaf-expectation warmup (`15.1`). |
| `#070` | `Ch 15 [SS-2]` | `L764`: **Codeforces 1264D2** — *Beautiful Bracket Sequence (Hard Version)* | `L461`: **AtCoder ARC 145 D / CF 1204E** — *Natasha, Spoons and Prefixes (`4B#10`)* | **Adopt `PC` (`CF 1204E`)**: `CF 1264D2` is already `#108` (`CP-V.2`). `CF 1204E` is the canonical Reflection Principle prefix-maxima problem (`15.1`). |
| `#220` | `Ch 15 [Int-1]` | `L765`: **AtCoder ABC 205 E / ARC 145 D / Luogu P3266** — *[JLOI2015] 骗我呢* | `L462`: **LOJ 6077** — *「2017 山东一轮集训 Day7」逆序对 (`4B#11`)* | **UNIFY AS `#220 Luogu P3266 — [JLOI2015] 骗我呢` IN BOTH FILES**: As Critic A (`§3.2`) proved, `LOJ 6077` is bounded inversion generating function $\prod \frac{1-x^i}{1-x}$ (`Ch 03`), NOT a lattice walk, while `ABC 205 E` in `CA` is quarantined template `R-63`! `Luogu P3266 — [JLOI2015] 骗我呢` (`Wave 4B#L747`) is the exact two-wall alternating reflection strip walk (`15.1`) and has zero collisions. Update `#220` to `Luogu P3266 — [JLOI2015] 骗我呢` in `CA`, `PC`, and `PA`. |
| `#098` | `Ch 15 [Int-2]` | `L766`: **Luogu P3978** — *[TJOI2015] 概率论* | `L463`: **Codeforces 1034D / Gym 102586F** — *Slime and Sequences / Lattice Walk (`4B#12`)* | **Adopt `PC` (`Gym 102586F` Lattice Walk)**: Eliminates the `Luogu P3978` duplicate (`#152`). |
| `#128` | `Ch 15 [Adv-1]` | `L767`: **AtCoder ABC 251 Ex / AGC 052 D** — *Fill Triangle / Raney Walk* | `L464`: **Codeforces 1810G** — *The Maximum Prefix (`4B#13`)* | **Adopt `PC` (`CF 1810G` — Prefix-Maximum Walk Kernel / DP) OR Dual-Label `CF 1810G / Raney Cyclic Shift Walk (`4B#13`)`**: Align `CA` with `PC` (`#128`) and explicitly frame the solution via the bivariate prefix-excess kernel $K(t,u) = 1 - t(p u + q u^{-1})$ (`15.3`) so the Kernel Method engine is directly exercised. |
| `#134` | `Ch 15 [Adv-2]` | `L768`: **UOJ 424** — *[集训队作业2018] count* | `L465`: **Codeforces 1842H / Gym 103470K** — *Slime and Sandwiches / Reflection Principle (`4B#14`)* | **Adopt `PC` (`Gym 103470K`)**: `UOJ 424` is already `#210` (`Ch 15 Mas-2`)! |
| `#076` | `Ch 15 [Mas-1]` | `L769`: **Codeforces 1336E2** — *Chiori and Doll Picking* | `L466`: **Catalan-Kernel Synthesis / Gym 102759C** — *Bivariate Kernel Walk (`4B#15`)* | **Adopt `PC` (`Gym 102759C` Bivariate Kernel Walk)**: `CF 1336E2` in `CA` is `#111` (`Ch 23 Mas-2` Krawtchouk coding theory) and has nothing to do with `Ch 15` lattice walks! |
| `#127` | `Ch 20 [Int-1]` | `L964`: **Codeforces 1613F / ABC 281 Ex** — *Tree Coloring / Alchemy* | `L548`: **Codeforces 1770G / Gym 102978H** — *Telleporter / Transposed Vandermonde (`3A#9`)* | **Adopt `PC` (`Gym 102978H` Transposed Vandermonde)**: `CF 1613F` is `#124` (`Ch 22 SS-2`) and `ABC 281 Ex` is `#036` (`Ch 21 SS-1`)! `Gym 102978H` directly tests `20.2` Transposed Vandermonde (`mul_t`). |
| `#167` | `Ch 20 [Int-2]` | `L965`: **Luogu P5282** — *[模板] 快速阶乘算法* | `L549`: **Luogu P5284 / LOJ 6485** — *LJJ 学二项式定理 / Multipoint Eval (`3A#10`)* | **Adopt `PC` (`LOJ 6485` — LJJ 学二项式定理)**: `Luogu P5282` in `CA` is quarantined template `R-35`! (Note: in `PC`/`PA`, drop the `Luogu P5284` prefix since `P5284` is string problem `[十二省联考 2019] 字符串问题`, and keep `LOJ 6485 — LJJ 学二项式定理`). |
| `#217` | `Ch 20 [Mas-2]` | `L969`: **UOJ 604** — *[UR #20] 跳蚤电话* | `L553`: **LOJ 172 / Luogu P5433** — *Polynomial GCD & Half-GCD (`3A#14`)* | **Adopt `PC` (`Luogu P5433` — Polynomial Half-GCD Application)**: `UOJ 604` is already `#215` (`CP-V.6`). |
| `#050` | `Ch 22 [Adv-1]` | `L1044`: **Luogu P4719** — *[模板] 动态 DP* | `L586`: **AtCoder AGC 058 D / CF 1408G** — *Yet Another ABC String / Cluster Counting (`5B#4`)* | **Adopt `PC` (`CF 1408G` / Tree-Cluster Convolution)**: `Luogu P4719` is a pure Dynamic DP template (`【模板】`), violating the Zero-Template Rule! |
| `#204` | `Ch 22 [Adv-2]` | `L1045`: **Luogu P3781** — *[SDOI2017] 切树游戏* | `L587`: **Luogu P8352 / UOJ 748** — *[SDOI/SXOI2022] 小 N 的独立集 (`5B#5`)* | **Adopt `PC` (`Luogu P8352`)**: `Luogu P3781` is `#155` (`Ch 22 Mas-2`). |
| `#166` | `Ch 22 [Mas-1]` | `L1046`: **LOJ 6674** — *链分治 NTT / Chain-Divide Tree FPS* | `L588`: **Luogu P5281** — *[ZJOI2019] Minimax 搜索 (`5B#6`)* | **Adopt `PC` (`Luogu P5281 / LOJ 3044`)**: `LOJ 3044` is `[ZJOI2019] Minimax 搜索` (`CA` wrote `LOJ 6674`). Unify as `Luogu P5281 (LOJ 3044) — [ZJOI2019] Minimax 搜索`. |
| `#155` | `Ch 22 [Mas-2]` | `L1047`: **UOJ 604 / LOJ 3044** — *[ZJOI2019] Minimax 搜索* | `L589`: **Luogu P3781** — *[SDOI2017] 切树游戏 (`5B#7`)* | **Adopt `PC` (`Luogu P3781`)**: Eliminates the swap between `Adv-2`, `Mas-1`, and `Mas-2`. |
| `#216` | `Ch 24 [SS-1]` | `L1118`: **UOJ 310** — *[UNR #2] 黎明前的巧克力* | `L620`: **LOJ 154** — *集合幂级数 exp / ln / 幂 (`5B#8`)* | **UNIFY AS `#216 Codeforces 449D — Jzzhu and Numbers` (or `ABC 212 H — Nim Counting`) IN ALL THREE FILES**: `CA`'s `UOJ 310` duplicates `#206` (`CP-VI.6`), while `PC`'s `LOJ 154` is a bare library template (`R-67` lists `LOJ 154`!). Replacing `#216` with `CF 449D — Jzzhu and Numbers` (`Wave 5B#L2762`, SOS DP / Zeta transform subset-AND warmup) or `ABC 212 H` (`Wave 5B#L2795`, Nim XOR FWT geometric series) eliminates both the `UOJ 310` duplicate and the `LOJ 154` template leak! |
| `#158` | `Ch 24 [SS-2]` | `L1119`: **Luogu P4233** — *[射命丸文的笔记]* | `L621`: **Luogu P4570 / CF 1119H** — *Triple (`5B#9`)* | **Adopt `PC` (`CF 1119H — Triple`)**: `Luogu P4233` is already `#157` (`Ch 12 Adv-2`). `CF 1119H` is the canonical 3-term Walsh–Hadamard FWT system (`24.1`). |
| `#244` | `Ch 24 [Int-1]` | `L1120`: **Codeforces 1119H** — *Triple* | `L622`: **Yukicoder 1211 / ABC 253 Ex** — *We Love Forest (`5B#10`)* | **Adopt `PC` (`ABC 253 Ex — We Love Forest`)**: Eliminates the `CF 1119H` shift and introduces $O(n^2 2^n)$ Subset Convolution (`24.2`) & SPS $\exp$ (`24.3`). |
| `#034` | `Ch 24 [Int-2]` | `L1121`: **AtCoder ABC 253 Ex** — *We Love Forest* | `L623`: **AtCoder ABC 269 Ex / ABC 306 Ex** — *Balance Scale (`5B#11`)* | **Adopt `PC` (`ABC 306 Ex — Balance Scale`)**: Eliminates the `ABC 253 Ex` shift (`Int-1`). (Note: drop `ABC 269 Ex` from the dual title since `ABC 269 Ex` is `#028` in `Ch 22 SS-1`). |
| `#184` | `Ch 24 [Adv-1]` | `L1122`: **AtCoder ABC 306 Ex** — *Balance Scale* | `L624`: **Luogu P5643** — *[PKUWC2018] 随机游走 (`5B#12`)* | **Adopt `PC` (`Luogu P5643`)**: Eliminates the `ABC 306 Ex` shift and tests Min-Max Inclusion-Exclusion + SOS DP (`24.1`). |
| `#207` | `Ch 24 [Adv-2]` | `L1123`: **Luogu P5495** — *[模板] Dirichlet 前缀和* | `L625`: **UOJ 348** — *[WC2018] 州区划分 (`5B#13`)* | **Adopt `PC` (`UOJ 348`)**: `Luogu P5495` in `CA` is quarantined template `R-39`! `UOJ 348` is the landmark $O(n^2 2^n)$ Subset Convolution DP (`24.2`). |
| `#212` | `Ch 24 [Mas-1]` | `L1124`: **UOJ 348** — *[WC2018] 州区划分* | `L626`: **UOJ 752** — *[UNR #6] 小火车 (`5B#14`)* | **Adopt `PC` (`UOJ 752`)**: `UOJ 752` tests the $\Omega(n)$-graded Dirichlet derivation (`24.4`). |
| `#215` | `Ch 24 [Mas-2]` | `L1125`: **UOJ 752** — *[UNR #6] 小火车* | `L627`: **UOJ 910** — *Pointed Biconnected Graph SPS (`5B#15`)* | **Adopt `PC` (`UOJ 910`)**: `UOJ 910` is the ultimate `Elegia` $O(n^2 2^n)$ SPS composition / pointed biconnected graph problem (`24.3`). |
| `#176` | `CP-II.8` (Stage 1) | `L1220`: **Luogu P5401** | `L753`: **Luogu P5396 / LOJ 6059** | **Adopt `PC` (`LOJ 6059`)**: Stage 1 mirrors `Ch 06 [Mas-2] #176`. |
| `#117` | `CP-IV.8` (Stage 1) | `L1292`: **Codeforces 1349D** | `L825`: **Codeforces 1479E** | **Adopt `PC` (`CF 1479E`)**: Stage 1 mirrors `Ch 14 [Mas-1] #117`. |

#### Additional Minor Alias Fix in Both `CA` and `PC`
- **`#165` (`Ch 02 [SS-2]`, `CA L256`, `PC L169`, `PA L251`)**: Currently labeled `Luogu P5268 — Subset Sum via ln/exp`. On Luogu, `P5268` is `[SNOI2017] 一个简单的询问` (Mo's algorithm), and in `Wave 5B#C3` it was a misnumbered entry for $G(x) = W(F(x))$ composition (`Ch 21`). Update the title of `#165` in all three files to **`Luogu P4389 (Warmup Variant) / AtCoder ABC 222 F — 0-1 & Unbounded Subset Sum via $\ln/\exp$ (`1D#4`)`** so readers are not sent to a Mo's algorithm problem.

---

## 3. Formatting, Quarantine (`R-01`–`R-67`), & Bijective Integrity Verification

### 3.1 Bijective Integrity (`#001`–`#254` and `R-01`–`R-67`)
- **`#001`–`#254` Bijection**:
  - `CURRICULUM_ARCHITECTURE.md`: `254` unique IDs (`#001`–`#254`), `0` missing, `0` duplicate `#ID`s.
  - `PROBLEM_CURATION.md`: `254` unique IDs (`#001`–`#254`), `0` missing, `0` duplicate `#ID`s.
  - `problem_archive.md`: `254` unique IDs (`#001`–`#254`), `0` missing, `0` duplicate `#ID`s.
- **`R-01`–`R-67` Quarantine Registry**:
  - `CURRICULUM_ARCHITECTURE.md §6.1` (`L1504–1570`): `67` unique IDs (`R-01`–`R-67`), `0` missing, `0` duplicates.
  - `PROBLEM_CURATION.md §5.1` (`L969–1035`): `67` unique IDs (`R-01`–`R-67`), `0` missing, `0` duplicates.
  - Cross-file identity check between `CA §6.1` and `PC §5.1`: **100% match (`67 / 67`)** on both Problem Identity and Assigned Chapter.

### 3.2 Math Delimiters & Markdown Table Pipe Escaping
Automated regex verification across every line of `CURRICULUM_ARCHITECTURE.md`, `PROBLEM_CURATION.md`, and `problem_archive.md`:
- **Forbidden LaTeX paren/bracket math delimiters**: `0` instances in `CA`, `0` instances in `PC`, `0` instances in `PA`.
- **Unescaped vertical bars `|` inside `$...$` in Markdown table rows**: `0` instances in `CA`, `0` instances in `PC`, `0` instances in `PA`.

---

## 4. Concrete Action Checklist to Reach 100% Cross-File Lock

1. **Synchronize the 53 Stale Problem Titles in `CURRICULUM_ARCHITECTURE.md` (`Ch 01, 03, 05, 06, 07, 14, 15, 20, 22, 24` & `CP-II.8, CP-IV.8`)**:
   - Replace the 53 stale Round 1 problem titles in `CA` (listed in the Section 2.2 table above) with `PC`'s canonical problem titles and Wave Pointers, and synchronize `CA §6.2`'s short problem codes for those 53 `#ID`s.
2. **Apply the 3 Surgical Problem-Identity Fixes Across All 3 Files (`CA`, `PC`, `PA`)**:
   - `#165` (`Ch 02 [SS-2]`): Change `Luogu P5268` (Mo's algorithm typo) to `Luogu P4389 (0-1 Subset Sum Variant) / AtCoder FPS Subset Sum via ln/exp`.
   - `#220` (`Ch 15 [Int-1]`): Use `CA`'s `Luogu P3266 — [JLOI2015] 骗我呢` (2-wall Reflection Principle strip walk) instead of `PC`'s `LOJ 6077` (which is `Ch 03` bounded inversion product $\prod \frac{1-x^i}{1-x}$) or `ABC 205 E` (`R-63`).
   - `#216` (`Ch 24 [SS-1]`): Replace `UOJ 310` (duplicate of `#206` in `CA`) and `LOJ 154` (bare template in `PC`) with `Codeforces 449D — Jzzhu and Numbers` (`Wave 5B#L2762`, SOS DP / Zeta Transform subset-AND warmup).
3. **Unify Sub-Section Headers (`Ch 03, 06, 10, 11, 13, 16–24`) & Fix the 5 Dangling `CP` Stage 2 References**:
   - **Unify `Ch 13` in both `CA` and `PC`**:
     - `13.1` Graphical Generating Functions & Connected Graphs ($\ln/\exp$ & $2^{-\binom{n}{2}}$ CZT Twist)
     - `13.2` Bipartite Graphs & 2-Colored Hurwitz EGFs
     - `13.3` Acyclic Digraphs (DAGs) & Strongly Connected Digraphs (Robinson–Stanley Inclusion-Exclusion)
     - `13.4` Kirchhoff's Matrix-Tree, BEST Theorem & Symbolic Matrix-Tree over $R[x]/(x^{k+1})$
   - **Add `3.5` Burnside's Lemma & Pólya's Cycle Index Theorem to `CA`'s `Ch 03`**, and copy `CA`'s Round 2 sub-section headers for `Ch 10, 16–24` into `PC`.
   - **Fix Dangling Sub-Section Numbers in `CP` Stage 2**:
     - `CP-II.4 (#252)`: `6.5` $\to$ `6.3/6.4` (`CA L1232`, `PC L765`).
     - `CP-III.7 (#205)`: `11.5` $\to$ `11.4` (`CA L1271`).
     - `CP-IV.3 (#099)` & `CP-IV.4 (#116)`: `14.5` $\to$ `14.4` (`CA L1303–1304, L1425`, `PC L836–837`).
   - **Fix `Ch 16 [Mas-2] #214` (`UOJ 596`) Table Cell**: Change `"3D Algebraic Diagonal"` to `"3D D-Finite Diagonal / Radial Derivation \mathfrak{D}"` at `CA L818`, `PC L482`, and `PA L298`.
