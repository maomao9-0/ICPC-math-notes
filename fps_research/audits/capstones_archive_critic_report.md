# Capstones & Problem Archive Comprehensive Audit Report (`capstones_archive_critic_report.md`)

**Auditor**: FPS Textbook Critic & Mathematical Auditor (`fps-textbook-critic`)  
**Audited Files**:
1. [`capstones/synthesis-reserve.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/synthesis-reserve.qmd) (`2,005` lines)
2. [`capstones/problem-archive-guide.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd) (`1,077` lines)
3. [`fps_research/problem_archive.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md) (Section 0 & Section 1, lines `1–470`)

**Reference Authorities Cross-Examined**:
- [`AGENTS.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/AGENTS.md)
- [`fps_research/CURRICULUM_ARCHITECTURE.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md) (§4 Blind Checkpoints, §5.1–§5.4 Synthesis Reserve & 43-Problem Permutation, §6.1–§6.2 67 Quarantined Templates & 254 Canonical Pool Directory)

---

## Executive Summary & Verdict

| Audit Target | Mathematical Rigor & Completeness | Bijective Synchronization (`254 + 67`) | Quarto Render & Editorial Hygiene | Verdict |
| :--- | :---: | :---: | :---: | :---: |
| [`capstones/synthesis-reserve.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/synthesis-reserve.qmd) | **100% Pass** (All `Syn-01`–`Syn-14` & `Revisited #1`–`#12` complete) | **100% Pass** matches `CURRICULUM_ARCHITECTURE.md` §5.1–§5.2 | **3 Minor Prose Fixes** (2 `"Let check"` typos, 1 conversational `"Careful:"` in sample trace) | **PASS WITH MINOR PROSE FIXES** |
| [`capstones/problem-archive-guide.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd) | **Needs Sync** (16 stale `CP-*` descriptions in §2.1, 2 wrong problem names in §2.2, 4 truncated `2.` items in §1) | **99.6% Slot Match** (`#082` `CP-IV.8` routed to `Ch 11` instead of `Ch 14` in 3 places) | **100% Pass** on math delimiters, pipes, `<details>`, and `.qmd` links; 2 empty `()` in §4.1 | **REQUIRES TARGETED TABLE SYNC** |
| [`fps_research/problem_archive.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md) (`L1–470`) | **Needs Sync** (3 stale technique cells `#054`, `#251`, `#252` in §1.2–§1.3) | **99.6% Slot Match** (`#082` `CP-IV.8` routed to `Ch 11` instead of `Ch 14` at `L150`, `L450`) | **100% Pass** | **REQUIRES 5-LINE SYNC** |

---

## Part 1: Audit of `capstones/synthesis-reserve.qmd`

### 1.1 Note on Canonical `Syn-01`–`Syn-14` IDs vs. Chapter/Checkpoint IDs
* **Canonical Verification**: In [`CURRICULUM_ARCHITECTURE.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md) (§5.1, lines `1400–1418`; §6.2, lines `1585–1650`) and [`fps_research/problem_archive.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md) (lines `49` & `465`), the 14 Grandmaster Multi-Chapter Synthesis Reserve problems are:
  - `Syn-01`: `#006` (`fps_24_k — Permutation`)
  - `Syn-02`: `#014` (`fps_24_t — Tree 2`)
  - `Syn-03`: `#051` (`ARC 093 F — Dark Horse`)
  - `Syn-04`: `#087` (`CF 623E — Transforming Sequence`)
  - `Syn-05`: `#106` (`CF 1228E — Another Filling the Grid`)
  - `Syn-06`: `#112` (`CF 1342E — Placing Rooks`)
  - `Syn-07`: `#142` (`Luogu P3311 — [SDOI2014] 数数`)
  - `Syn-08`: `#171` (`Luogu P5339 — [TJOI2019] 唱、跳、rap和篮球`)
  - `Syn-09`: `#173` (`Luogu P5400 — [CTS2019] 随机立方体`)
  - `Syn-10`: `#182` (`Luogu P5824 — 十二重计数法`)
  - `Syn-11`: `#172` (`Luogu P5366 — [SNOI2017] 遗失的答案`)
  - `Syn-12`: `#247` (`HDU 5855 — Less Time, More Profit`)
  - `Syn-13`: `#249` (`CSES 1112 — Required Substring`)
  - `Syn-14`: `#253` (`CF 961G — Partitions`)
  *(Note: The alternative list `#040, #052, #053, #079, #092, #106, #113, #129, #152, #223, #239, #241, #242, #252` consists of Chapter Ladder / Checkpoint problems such as `Ch 05 Adv-1` (`#040`), `Ch 08 Mas-1` (`#052`), `Ch 13 Adv-2` (`#053`), `CP-I.5` (`#079`), `Ch 07 Mas-1` (`#092`), `Ch 14 Mas-2` (`#113`), `Ch 16 SS-2` (`#129`), `CP-II.2` (`#152`), `Ch 03 Adv-1` (`#223`), `Ch 18 Int-2` (`#239`), `Ch 08 SS-2` (`#241`), `Ch 19 SS-1` (`#242`), and `CP-II.4` (`#252`), many of which are also covered in Section 3 of `synthesis-reserve.qmd` as Flagship Revisited Dual-Perspective problems.)*

### 1.2 8-Dimension Audit of `Syn-01`–`Syn-14` & `Revisited #1`–`#12`
1. **Concrete, Self-Contained Inline Problem Statements & Constraints**:
   - Every single problem `Syn-01` through `Syn-14` has an explicit, unhedged `#### Problem Statement`, `#### Constraints` (with exact bounds, modulus, and required complexity), and a hand-checkable `#### Sample Trace ($N \le 4$)` verified against the closed-form formulas.
   - All 3 progressive collapsible hints (`Hint 1 — Diagnostic Signal & Combinatorial Model`, `Hint 2 — Perspective 1 vs. Perspective 2 Setup`, `Hint 3 — Key Equations & Extraction Contract`) and the `Complete Dual-Perspective Derivation & Comparative Analysis` block are present and mathematically rigorous for all 14 problems.
   - Every problem includes a `::: {.callout-warning}` Failure Mode & Remedy block and a 5-item `#### Algorithm Contract` (`Input`, `Output`, `Algebraic Preconditions`, `Complexity`, `Correctness Invariant`).
2. **Section 3 (12 Flagship Revisited Dual-Perspective Problems `Revisited #1`–`#12`)**:
   - Lines `1957–2005` cover all 12 Flagship Dual-Perspective problems (`#084`, `#021`, `#113`, `#074`, `#153`, `#161`, `#226`, `#230`, `#025`, `#040`, `#036`, `#068`) matching [`CURRICULUM_ARCHITECTURE.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md) §5.2 100%, with valid relative `.qmd` links.
3. **Quarto Hygiene Check on `capstones/synthesis-reserve.qmd`**:
   - `\(` or `\[` delimiters: **0 instances**
   - `!$$` factorial collisions: **0 instances**
   - Unescaped `|` inside `$...$` in tables: **0 instances**
   - `<details>` / `<summary>` / `</details>` balance & blank-line padding: **56/56 balanced, 0 missing blank lines**
   - Broken `.qmd` links: **0 broken links**

### 1.3 Required Prose & Typo Fixes in `capstones/synthesis-reserve.qmd`

#### Issue SR-1: Grammatical Typo `"Let check"` at Lines 129 and 272
- **Location 1**: [`capstones/synthesis-reserve.qmd:129`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/synthesis-reserve.qmd#L129)
  - **Current Text**:
    ```markdown
    Let $D(x) = \sum_{s=0}^N \frac{(-1)^s}{(s!)^2} x^s \bmod x^{N+1}$. Since $[x^0] D(x) = 1 \neq 0$, $D(x)$ is invertible in $\mathbb{F}_p[[x]] / (x^{N+1})$. Let check $N = 3$:
    ```
  - **Drop-In Replacement**:
    ```markdown
    Let $D(x) = \sum_{s=0}^N \frac{(-1)^s}{(s!)^2} x^s \bmod x^{N+1}$. Since $[x^0] D(x) = 1 \neq 0$, $D(x)$ is invertible in $\mathbb{F}_p[[x]] / (x^{N+1})$. Evaluating at $N = 3$:
    ```
- **Location 2**: [`capstones/synthesis-reserve.qmd:272`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/synthesis-reserve.qmd#L272)
  - **Current Text**:
    ```markdown
    Let check our sample trace $N = 3, A = (1, 2, 1), T = 3$:
    ```
  - **Drop-In Replacement**:
    ```markdown
    Verifying on our sample trace $N = 3, A = (1, 2, 1), T = 3$:
    ```

#### Issue SR-2: Conversational Self-Correction `"= 1/7? Careful:"` in `Syn-09` Sample Trace at Line 1155
- **Location**: [`capstones/synthesis-reserve.qmd:1155`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/synthesis-reserve.qmd#L1155)
  - **Current Text**:
    ```markdown
      * For $j = 1$ chosen cell: probability it is great is $\frac{1}{8 - 1} = \frac{1}{7}$? Careful: the union of $1$ cell's slice-mates has size $8 - (2-1)(2-1)(2-1) = 7$, so probability is $\frac{1}{7}$, and across $8$ cells $f_1 = 8 \cdot \frac{1}{7} = \frac{8}{7}$.
    ```
  - **Drop-In Replacement**:
    ```markdown
      * For $j = 1$ chosen cell: the union of $1$ cell's slice neighborhood has size $U_1 = 8 - (2-1)(2-1)(2-1) = 7$, so the probability it is great is $\frac{1}{7}$, and across all $8$ cells $f_1 = 8 \cdot \frac{1}{7} = \frac{8}{7}$.
    ```

---

## Part 2: Audit of `capstones/problem-archive-guide.qmd`

### 2.1 Issue PAG-1: Routing Mismatch for `#082` (`Toyota 2023 Spring Final E`, `CP-IV.8`) — Routed to `Ch 11` Instead of `Ch 14`
In [`CURRICULUM_ARCHITECTURE.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md) (§4.4 line `1313` and §6.2 line `1604`), `#082` (`Toyota 2023 Spring Final E — Replace Digits / Tree Constraint`) is assigned to **`CP-IV.8 ($\to$ Ch 14)`** (since `CP-IV` tests Part IV: Chapters 14–18, whereas `Ch 11` is in Part III). However, in `capstones/problem-archive-guide.qmd`, `#082` is routed to `Ch 11` in three places:
1. **Lines 304 vs. 364** (Section 1 Chapter-by-Chapter Routing):
   - In [`capstones/problem-archive-guide.qmd:304`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd#L304) (`Ch 11`), remove ``[`CP-IV.8`](../checkpoints/cp04-part4-blind-checkpoint.qmd): `#082` (Toyota 2023 Spring Final E), ``:
     ```markdown
     * **Routed Blind Checkpoints (2)**: [`CP-III.5`](../checkpoints/cp03-part3-blind-checkpoint.qmd): `#119` (CF 1528F), [`CP-III.7`](../checkpoints/cp03-part3-blind-checkpoint.qmd): `#205` (Luogu P8555).
     ```
   - In [`capstones/problem-archive-guide.qmd:364`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd#L364) (`Ch 14`), add ``[`CP-IV.8`](../checkpoints/cp04-part4-blind-checkpoint.qmd): `#082` (Toyota 2023 Spring Final E)``:
     ```markdown
     * **Routed Blind Checkpoints (6)**: [`CP-IV.1`](../checkpoints/cp04-part4-blind-checkpoint.qmd): `#158` (Luogu P4707), [`CP-IV.2`](../checkpoints/cp04-part4-blind-checkpoint.qmd): `#169` (Luogu P5326), [`CP-IV.3`](../checkpoints/cp04-part4-blind-checkpoint.qmd): `#099` (CF 1025G), [`CP-IV.4`](../checkpoints/cp04-part4-blind-checkpoint.qmd): `#116` (CF 1479E), [`CP-IV.5`](../checkpoints/cp04-part4-blind-checkpoint.qmd): `#194` (Luogu P6633), [`CP-IV.8`](../checkpoints/cp04-part4-blind-checkpoint.qmd): `#082` (Toyota 2023 Spring Final E).
     ```
2. **Line 592** (Section 1.2 Blind Checkpoints Summary Table, row `CP-IV`):
   - **Current Text** ([`capstones/problem-archive-guide.qmd:592`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd#L592)):
     ```markdown
     | [**`CP-IV`**](../checkpoints/cp04-part4-blind-checkpoint.qmd) | Part IV (Ch 14–18) | **`.1`**: `#158` Luogu P4707 ($\to$ Ch 14)<br>**`.2`**: `#169` Luogu P5326 ($\to$ Ch 14) | **`.3`**: `#099` CF 1025G ($\to$ Ch 14)<br>**`.4`**: `#116` CF 1479E ($\to$ Ch 14) | **`.5`**: `#194` Luogu P6633 ($\to$ Ch 14)<br>**`.6`**: `#058` ARC 136 F ($\to$ Ch 16) | **`.7`**: `#243` yukicoder 2104 ($\to$ Ch 16)<br>**`.8`**: `#082` Toyota 2023 Spring Final E ($\to$ Ch 11) |
     ```
   - **Drop-In Replacement**:
     ```markdown
     | [**`CP-IV`**](../checkpoints/cp04-part4-blind-checkpoint.qmd) | Part IV (Ch 14–18) | **`.1`**: `#158` Luogu P4707 ($\to$ Ch 14)<br>**`.2`**: `#169` Luogu P5326 ($\to$ Ch 14) | **`.3`**: `#099` CF 1025G ($\to$ Ch 14)<br>**`.4`**: `#116` CF 1479E ($\to$ Ch 14) | **`.5`**: `#194` Luogu P6633 ($\to$ Ch 14)<br>**`.6`**: `#058` ARC 136 F ($\to$ Ch 16) | **`.7`**: `#243` yukicoder 2104 ($\to$ Ch 16)<br>**`.8`**: `#082` Toyota 2023 Spring Final E ($\to$ Ch 14) |
     ```
3. **Line 715** (Section 2.1 Master Numerical Directory, row `#082`):
   - **Current Text** ([`capstones/problem-archive-guide.qmd:715`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd#L715)):
     ```markdown
     | `#082` | **Toyota 2023 Spring Final E — Replace Digits / Tree Constraint** (AtCoder) | `3A#16` | [`CP-IV.8`](../checkpoints/cp04-part4-blind-checkpoint.qmd) ($\to$ [`Ch 11`](../chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd)) | [`Ch 11`](../chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd) | Implicit Tree Degree Constraint + Lagrange Inversion |
     ```
   - **Drop-In Replacement**:
     ```markdown
     | `#082` | **Toyota 2023 Spring Final E — Replace Digits / Tree Constraint** (AtCoder) | `3A#16` | [`CP-IV.8`](../checkpoints/cp04-part4-blind-checkpoint.qmd) ($\to$ [`Ch 14`](../chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd)) | [`Ch 14`](../chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd) | Expected Value of Random Digit Replacement / Implicit Tree Constraint via PGF & Lagrange Inversion |
     ```

---

### 2.2 Issue PAG-2: 16 Blind Checkpoint Rows in Section 2.1 (`L687–L885`) Have Stale / Wrong Problem Descriptions in Column 6
During the 43-problem permutation from `synthesis_v1` to `CURRICULUM_ARCHITECTURE.md`, the `Canonical Curriculum Slot` column in Section 2.1 was updated, but 16 `CP-*` rows retained the `Surface Problem Statement` of the **old** problem that used to occupy that checkpoint slot!

Below is the complete line-by-line list of all 16 mismatched rows in [`capstones/problem-archive-guide.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd) (`L687–L885`) and their exact drop-in replacements:

1. **Line 687 (`#054`, `ARC 106 E — Medals`, `CP-VI.5`)** — *Currently has the description of `ARC 106 D — Powers` (`Newton Identities / Power-Sum OGF`)*:
   ```markdown
   | `#054` | **[ARC 106 E — Medals](https://atcoder.jp/contests/arc106/tasks/arc106_e)** (AtCoder) | `5B#F3` | [`CP-VI.5`](../checkpoints/cp06-part6-blind-checkpoint.qmd) ($\to$ [`Ch 24`](../chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd)) | [`Ch 24`](../chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd) | Fast Zeta / SOS Transform + Hall's Marriage Theorem on Bipartite Medal Schedules ($N \le 18, K \le 10^5$) |
   ```
2. **Line 701 (`#068`, `AGC 005 F — Many Easy Problems`, `CP-V.8`)** — *Currently has the description of `#233` (`Count n x m matrices over F_q of each rank r via q-binomials`)*:
   ```markdown
   | `#068` | **[AGC 005 F — Many Easy Problems](https://atcoder.jp/contests/agc005/tasks/agc005_f)** (AtCoder) | `1B#15` | [`CP-V.8`](../checkpoints/cp05-part5-blind-checkpoint.qmd) ($\to$ [`Ch 20`](../chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd)) | [`Ch 20`](../chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd) | Subtree Size Frequency + Reverse-Indexed Vandermonde / Transposed Convolution (`mulT`) for Steiner Subtrees |
   ```
3. **Line 733 (`#100`, `CF 1054H — Epic Convolution`, `CP-II.5`)** — *Currently has the description of `#193` (`Luogu P6620`)*:
   ```markdown
   | `#100` | **[CF 1054H — Epic Convolution](https://codeforces.com/problemset/problem/1054/H)** (CF) | `2A#21` | [`CP-II.5`](../checkpoints/cp02-part2-blind-checkpoint.qmd) ($\to$ [`Ch 07`](../chapters/ch07-roots-of-unity-cyclotomic-czt.qmd)) | [`Ch 07`](../chapters/ch07-roots-of-unity-cyclotomic-czt.qmd) | 2D Index-Calculus & Mixed-Radix Chirp-$Z$ Transform for $\sum_{i,j} a_i b_j c^{i^2 j^3 \bmod 490018} \pmod{490019}$ |
   ```
4. **Line 752 (`#119`, `CF 1528F — AmShZ Farm`, `CP-III.5`)** — *Currently describes planted trees with out-degree in $\{0\}\cup S$ instead of cyclic parking functions*:
   ```markdown
   | `#119` | **[CF 1528F — AmShZ Farm](https://codeforces.com/problemset/problem/1528/F)** (CF) | `1A#24` | [`CP-III.5`](../checkpoints/cp03-part3-blind-checkpoint.qmd) ($\to$ [`Ch 11`](../chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd)) | [`Ch 11`](../chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd) | Cyclic Parking Function Raney Orbit $\binom{n}{j} (n+1)^{n-j-1}$ + Stirling $S_2$ Power Expansion |
   ```
5. **Line 764 (`#131`, `CF 1906J — Count BFS Graphs`, `CP-III.2`)** — *Currently describes tournament structures (`#132`)*:
   ```markdown
   | `#131` | **[CF 1906J — Count BFS Graphs](https://codeforces.com/problemset/problem/1906/J)** (CF) | `5B#A2` | [`CP-III.2`](../checkpoints/cp03-part3-blind-checkpoint.qmd) ($\to$ [`Ch 09`](../chapters/ch09-cdq-fft-online-relaxed-convolution.qmd)) | [`Ch 09`](../chapters/ch09-cdq-fft-online-relaxed-convolution.qmd) | BFS Queue-Layer Interval Transition DP + Generating Function Prefix Convolution |
   ```
6. **Line 768 (`#135`, `CF 1988F — Heartbeat`, `CP-V.4`)** — *Currently describes Shift of Sampling Points (`R-30`)*:
   ```markdown
   | `#135` | **[CF 1988F — Heartbeat](https://codeforces.com/problemset/problem/1988/F)** (CF) | `5B#B6` | [`CP-V.4`](../checkpoints/cp05-part5-blind-checkpoint.qmd) ($\to$ [`Ch 20`](../chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd)) | [`Ch 20`](../chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd) | Prefix-Suffix Maximum & Ascent Permutation DP via Tellegen Transposed Convolution (`mulT`) |
   ```
7. **Line 785 (`#152`, `Luogu P4091 — [HEOI2016] 求和`, `CP-II.2`)** — *Currently describes a 3-index binomial sum (`#080`)*:
   ```markdown
   | `#152` | **[Luogu P4091 — [HEOI2016] 求和](https://www.luogu.com.cn/problem/P4091)** (Luogu) | `2A#23` | [`CP-II.2`](../checkpoints/cp02-part2-blind-checkpoint.qmd) ($\to$ [`Ch 06`](../chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd)) | [`Ch 06`](../chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd) | Row-Sum of Stirling Numbers of the Second Kind $\sum_{i=0}^n \sum_{j=0}^i \left\{\begin{smallmatrix} i \\ j \end{smallmatrix}\right\} 2^j j!$ via NTT |
   ```
8. **Line 793 (`#160`, `Luogu P4747 — [CERC2017] Intrinsic Interval`, `CP-III.4`)** — *Currently describes generic nonlinear functional equation*:
   ```markdown
   | `#160` | **[Luogu P4747 — [CERC2017] Intrinsic Interval](https://www.luogu.com.cn/problem/P4747)** (Luogu) | `3A#12` | [`CP-III.4`](../checkpoints/cp03-part3-blind-checkpoint.qmd) ($\to$ [`Ch 10`](../chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd)) | [`Ch 10`](../chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd) | Simple (Interval-Indecomposable) Permutations via Compositional Substitution Inversion |
   ```
9. **Line 796 (`#163`, `Luogu P5206 — [WC2019] 数树`, `CP-III.8`)** — *Currently describes biconnected graphs*:
   ```markdown
   | `#163` | **[Luogu P5206 — [WC2019] 数树](https://www.luogu.com.cn/problem/P5206)** (Luogu) | `1B#17` | [`CP-III.8`](../checkpoints/cp03-part3-blind-checkpoint.qmd) ($\to$ [`Ch 13`](../chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd)) | [`Ch 13`](../chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd) | 3-Subtask Tree Intersection $\sum_{T_1, T_2} y^{n - \lvert E_1 \cap E_2 \rvert}$ via Tree DP & EGF $\exp\!\left(\frac{n^2 y}{1-y} T(x)\right)$ |
   ```
10. **Line 808 (`#175`, `Luogu P5406 — [THUPC2019] 找树`, `CP-VI.7`)** — *Currently describes hypergraph edge weights (`#207` `UOJ 94`)*:
    ```markdown
    | `#175` | **[Luogu P5406 — [THUPC2019] 找树](https://www.luogu.com.cn/problem/P5406)** (Luogu) | `5B#F8` | [`CP-VI.7`](../checkpoints/cp06-part6-blind-checkpoint.qmd) ($\to$ [`Ch 24`](../chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd)) | [`Ch 24`](../chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd) | Mixed Bitwise FWT (AND/OR/XOR per Bit) Inside Symbolic Matrix-Tree Determinant |
    ```
11. **Line 813 (`#180`, `Luogu P5643 — [PKUWC2018] 随机游走`, `CP-VI.8`)** — *Currently describes Dirichlet series prefix sums (`#231` `LOJ 6729`)*:
    ```markdown
    | `#180` | **[Luogu P5643 — [PKUWC2018] 随机游走](https://www.luogu.com.cn/problem/P5643)** (Luogu) | `2B#C1` | [`CP-VI.8`](../checkpoints/cp06-part6-blind-checkpoint.qmd) ($\to$ [`Ch 24`](../chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd)) | [`Ch 24`](../chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd) | Tree Random Walk Gaussian Elimination + Min–Max Inclusion–Exclusion + Fast Zeta (SOS) Transform |
    ```
12. **Line 818 (`#185`, `Luogu P5853 — Stirling & Falling Factorial Transpose`, `CP-V.5`)** — *Currently describes subproduct tree multipoint evaluation*:
    ```markdown
    | `#185` | **[Luogu P5853 — Stirling & Falling Factorial Transpose](https://www.luogu.com.cn/problem/P5853)** (Luogu) | `5B#B14` | [`CP-V.5`](../checkpoints/cp05-part5-blind-checkpoint.qmd) ($\to$ [`Ch 20`](../chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd)) | [`Ch 20`](../chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd) | Transposed Vandermonde & Stirling Basis Conversion via Tellegen's Principle (`mulT`) |
    ```
13. **Line 838 (`#205`, `Luogu P8555 — 密码学第三次小作业`, `CP-III.7`)** — *Currently describes $n \le 2\times 10^5$ LIF instead of $n \le 10^{18}$ mod small prime $p \le 10^5$*:
    ```markdown
    | `#205` | **[Luogu P8555 — 密码学第三次小作业](https://www.luogu.com.cn/problem/P8555)** (Luogu) | `4B#31` | [`CP-III.7`](../checkpoints/cp03-part3-blind-checkpoint.qmd) ($\to$ [`Ch 11`](../chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd)) | [`Ch 11`](../chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd) | Scale-Invariant Algebraic Generating Function $[x^n]$ Extraction for $n \le 10^{18}$ Modulo Small Prime $p \le 10^5$ |
    ```
14. **Line 848 (`#215`, `UOJ 604 — [UR #20] 跳蚤电话`, `CP-V.6`)** — *Currently describes polynomial composition $F(G(x))$ (`#235` `QOJ 8528`)*:
    ```markdown
    | `#215` | **[UOJ 604 — [UR #20] 跳蚤电话](https://uoj.ac/problem/604)** (UOJ) | `4B#8` | [`CP-V.6`](../checkpoints/cp05-part5-blind-checkpoint.qmd) ($\to$ [`Ch 20`](../chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd)) | [`Ch 20`](../chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd) | Tree Construction History Enumeration via Transposed Multipoint Evaluation / D&C NTT |
    ```
15. **Line 876 (`#243`, `yukicoder 2104 — Fuss–Catalan Diagonal`, `CP-IV.7`)** — *Currently describes bounded strip Motzkin walks*:
    ```markdown
    | `#243` | **[yukicoder 2104 — Fuss–Catalan Diagonal](https://yukicoder.me/problems/no/2104)** (yuki) | `4B#14` | [`CP-IV.7`](../checkpoints/cp04-part4-blind-checkpoint.qmd) ($\to$ [`Ch 16`](../chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd)) | [`Ch 16`](../chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd) | Asymmetric $(p, q)$-Diagonal Extraction $[x^{pn} y^{qn}] F(x, y)$ via Furstenberg Residue & Lagrange Inversion |
    ```
16. **Lines 884 & 885 (`#251` `CF 1264D1`, `CP-II.3` and `#252` `CF 622F`, `CP-II.4`)** — *Currently describe Taylor Shift (`R-28`) and Prefix-Suffix Maxima (`#096` `CF 960G`)*:
    ```markdown
    | `#251` | **[CF 1264D1 — Beautiful Bracket Sequence (Easy)](https://codeforces.com/problemset/problem/1264/D1)** (CF) | `2A#3` | [`CP-II.3`](../checkpoints/cp02-part2-blind-checkpoint.qmd) ($\to$ [`Ch 06`](../chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd)) | [`Ch 06`](../chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd) | Bracket Depth Contribution Sum + Vandermonde Convolution Identity $\sum_i i \binom{a}{i} \binom{b}{c-i}$ |
    | `#252` | **[CF 622F — The Sum of the k-th Powers](https://codeforces.com/problemset/problem/622/F)** (CF) | `2A#26` | [`CP-II.4`](../checkpoints/cp02-part2-blind-checkpoint.qmd) ($\to$ [`Ch 06`](../chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd)) | [`Ch 06`](../chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd) | $O(k)$ Prefix-Suffix Factorial Lagrange Interpolation on Consecutive Points $x = 1, \dots, k+2$ for $\sum_{i=1}^n i^k$ |
    ```

---

### 2.3 Issue PAG-3: Two Wrong Problem Titles in Section 2.2 (43-Problem Bijective Permutation Table, `L916` & `L923`)
In [`capstones/problem-archive-guide.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd) Section 2.2:
1. **Line 916 (`#082`)**: Labeled `CF 240F / BZOJ 4899 — 记忆的轮廓` (and routed to `Ch 11`), whereas `#082` is **`Toyota 2023 Spring Final E — Replace Digits / Tree Constraint`** routed to `CP-IV.8` ($\to$ `Ch 14`).
   - **Drop-In Replacement for Line 916**:
     ```markdown
     | `#082` | **Toyota 2023 Spring Final E — Replace Digits / Tree Constraint** | `Ch 11 [Int-1]` | [`CP-IV.8`](../checkpoints/cp04-part4-blind-checkpoint.qmd) ($\to$ [`Ch 14`](../chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd)) | Shifted to Part IV Blind Checkpoint (`CP-IV.8`); `Ch 11 [Int-1]` filled by Clean 1D Raney `#196`. |
     ```
2. **Line 923 (`#141`)**: Labeled `LOJ 6222 — Powers of $k$ in Permutations`, whereas `#141` is **`Luogu P2290 / P4430 — 树的计数 / 猴猴吃香蕉`**.
   - **Drop-In Replacement for Line 923**:
     ```markdown
     | `#141` | **Luogu P2290 / P4430 — 树的计数 / 猴猴吃香蕉** | `Ch 06 [SS-2]` | [`CP-II.8`](../checkpoints/cp02-part2-blind-checkpoint.qmd) ($\to$ [`Ch 04`](../chapters/ch04-egf-set-cyc-boxed-prufer.qmd)) | Shifted to Part II Blind Checkpoint (`CP-II.8`); `Ch 06 [SS-2]` filled by Vandermonde `#055`. |
     ```

---

### 2.4 Issue PAG-4: 4 Truncated `"2."` Reverse-Engineering Scratchpad Lines in Section 1 (`L185`, `L250`, `L270`, `L290`) & 2 Empty `()` in Section 4.1 (`L986`, `L1003`)
In [`capstones/problem-archive-guide.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd), four `Reverse-Engineering Scratchpad` bullets in Section 1 end abruptly with a dangling `2.`:
1. **Line 185 (`Ch 06`)**:
   - **Current**: `* **Reverse-Engineering Scratchpad**: 1. Replace $\binom{n}{k}$ by $[x^k](1+x)^n$ (or $\binom{n+k-1}{k} = [x^k](1-x)^{-n}$), exchange the order of summation, and collapse the inner geometric/binomial series. 2. For $\sum_k k^m \binom{n}{k} p^k (1-p)^{n-k}$, substitute $k^m = \sum_{j=0}^m \left\{\begin{smallmatrix} m \\ j \end{smallmatrix}\right\} k^{\underline{j}}$ so $k^{\underline{j}} \binom{n}{k} = n^{\underline{j}} \binom{n-j}{k-j}$ pulls $k$ out of the polynomial! 2.`
   - **Fix**: Remove the trailing ` 2.` at the end of line 185.
2. **Line 250 (`Ch 09`)**:
   - **Current**: `* **Reverse-Engineering Scratchpad**: 1. If $f_n = \sum_{i=1}^n f_{n-i} g_i$ where $g_1, \dots, g_N$ are already known, use standard CDQ D&C FFT (\`solve(L, R)\`). 2.`
   - **Fix**: Replace trailing `2.` with `2. If $g_i$ also depends on $f_i$ (e.g., $f_n = \sum_{i=1}^{n-1} f_i f_{n-i}$), use Semi-Online / Relaxed Convolution splitting $(i < mid, j < mid)$ vs. symmetric cross-terms.`
3. **Line 270 (`Ch 10`)**:
   - **Current**: `* **Reverse-Engineering Scratchpad**: 1. Express the rooted structure $R(x)$ via $\operatorname{SEQ}$, $\operatorname{MSET}$, or $\operatorname{CYC}$ of subtrees to obtain a fixed-point equation $R(x) = x \Phi(R(x), R(x^2), \dots)$. 2.`
   - **Fix**: Replace trailing `2.` with `2. Treat higher-order Pólya terms $R(x^2), R(x^3), \dots$ as known constants at precision $x^{2m}$ during the Newton step $R \gets R - \frac{P(R)}{P'(R)} \bmod x^{2m}$, then subtract the edge-rooted symmetry orbit to count unrooted trees.`
4. **Line 290 (`Ch 11`)**:
   - **Current**: `* **Reverse-Engineering Scratchpad**: 1. Rewrite $T(x) = x \phi(T(x))$ as $\frac{T(x)}{\phi(T(x))} = x$; then $[x^n] H(T(x)) = \frac{1}{n} [u^{n-1}] H'(u) \phi(u)^n$ (one polynomial power)! 2.`
   - **Fix**: Replace trailing `2.` with `2. When the relation is not in standard $x = u/\phi(u)$ form, set $x = g(u)$ so the inner function linearizes and apply the formal residue change of variables $\operatorname{Res}_x F(x) dx = \operatorname{Res}_u F(g(u)) g'(u) du$.`
5. **Lines 986 & 1003 (Empty `()` in Section 4.1)**:
   - **Line 986 (`R-46`)**: Change `**Codeforces 1264D2 (When Used as 1-Line Vandermonde Identity in Wave 4B)** ()` to `**Codeforces 1264D2 (When Used as 1-Line Vandermonde Identity in Wave 4B)** (CF)`.
   - **Line 1003 (`R-49`)**: Change `**Luogu P6198 / Pure $(q;q)_n$ Exp/Ln Template** ()` to `**Luogu P6198 / Pure $(q;q)_n$ Exp/Ln Template** (Luogu)`.

---

## Part 3: Audit of `fps_research/problem_archive.md` (Lines 1–470)

All 254 problems (`#001`–`#254`) are present in Section 0 and Section 1 (`1.1`–`1.6`) of [`fps_research/problem_archive.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md). Five lines in `L1–470` require synchronization with `CURRICULUM_ARCHITECTURE.md`:

1. **Line 122 (`#054`, `ARC 106 E — Medals`)** — *Stale technique & wave pointer from `ARC 106 D`*:
   - **Current**: `| **ARC 106 E** | \`#054\` | Medals | Newton Identities / Power-Sum OGF | Wave 2A (#35) | **\`CP-VI.5\`** ($\to$ \`Ch 24\`) |`
   - **Drop-In Replacement**:
     ```markdown
     | **ARC 106 E** | `#054` | Medals | Fast Zeta / SOS Transform + Hall's Marriage Theorem | Wave 5B (#F3) | **`CP-VI.5`** ($\to$ `Ch 24`) |
     ```
2. **Line 150 (`#082`, `Toyota 2023 Spring Final E`)** — *Routed to `Ch 11` instead of `Ch 14`*:
   - **Current**: `| **Toyota 2023 Spring Final E** | \`#082\` | Replace Digits / Tree Constraint | Implicit Tree Degree Constraint + Lagrange Inversion | Wave 3A (#16) | **\`CP-IV.8\`** ($\to$ \`Ch 11\`) |`
   - **Drop-In Replacement**:
     ```markdown
     | **Toyota 2023 Spring Final E** | `#082` | Replace Digits / Tree Constraint | Expected Value of Random Digit Replacement / Implicit Tree Constraint | Wave 3A (#16) | **`CP-IV.8`** ($\to$ `Ch 14`) |
     ```
3. **Lines 214 & 215 (`#251` `CF 1264D1` and `#252` `CF 622F`)** — *Wrong technique descriptions in Column 4*:
   - **Current**:
     ```markdown
     | **CF 1264D1** | `#251` | Beautiful Bracket Sequence (Easy) | Given a polynomial $P(x)$ of degree $N \le 2.5\times 10^5$ and shift $c$, output the coefficients of $P(x+c)$. | `2A#3` | **`CP-II.3`** ($\to$ `Ch 06`) |
     | **CF 622F** | `#252` | The Sum of the k-th Powers | For all $k=1,\dots,n$ ($n \le 2.5\times 10^5$), count permutations of $n$ with $k$ prefix maxima and $b$ suffix maxima. | `2A#26` | **`CP-II.4`** ($\to$ `Ch 06`) |
     ```
   - **Drop-In Replacement**:
     ```markdown
     | **CF 1264D1** | `#251` | Beautiful Bracket Sequence (Easy) | Bracket Depth Contribution Sum + Vandermonde Convolution Identity $\sum_i i \binom{a}{i} \binom{b}{c-i}$ | `2A#3` | **`CP-II.3`** ($\to$ `Ch 06`) |
     | **CF 622F** | `#252` | The Sum of the k-th Powers | $O(k)$ Consecutive-Point Lagrange Interpolation for $\sum_{i=1}^n i^k$ | `2A#26` | **`CP-II.4`** ($\to$ `Ch 06`) |
     ```
4. **Lines 450 & 453 (Section 1.6 Inverse Chapter-to-Problem Bijection for `Ch 11` and `Ch 14`)** — *Move `**CP-IV.8**: #082 (Toyota 2023 Spring Final E)` from `Ch 11` (`L450`) to `Ch 14` (`L453`)*:
   - **Drop-In Replacement for Line 450 (`Ch 11`)**:
     ```markdown
     | **Ch 11** | **SS-1**: `#003` (`fps_24_f`, `1A#2`); **SS-2**: `#200` (Luogu P7438, `3B#28`); **Int-1**: `#196` (Luogu P6672, `4B#5`); **Int-2**: `#201` (Luogu P7439, `3B#29`); **Adv-1**: `#010` (`fps_24_p`, `1A#29`); **Adv-2**: `#229` (LOJ 6703, `3B#27`); **Mas-1**: `#114` (CF 1349F2, `1A#30`); **Mas-2**: `#203` (Luogu P7592, `3B#11`) | **CP-III.5**: `#119` (CF 1528F), **CP-III.7**: `#205` (Luogu P8555) | `R-61`, `R-62` |
     ```
   - **Drop-In Replacement for Line 453 (`Ch 14`)**:
     ```markdown
     | **Ch 14** | **SS-1**: `#115` (CF 1392H, `2B#E3`); **SS-2**: `#026` (ABC 242 Ex, `2B#E8`); **Int-1**: `#156` (Luogu P4548, `2B#E9`); **Int-2**: `#071` (AGC 038 E, `2B#E10`); **Adv-1**: `#148` (Luogu P3706, `2B#D2`); **Adv-2**: `#209` (UOJ 390, `2B#E6`); **Mas-1**: `#039` (ABC 289 Ex, `2B#E12`); **Mas-2**: `#113` (CF 1349D, `2B#E5`) | **CP-IV.1**: `#158` (Luogu P4707), **CP-IV.2**: `#169` (Luogu P5326), **CP-IV.3**: `#099` (CF 1025G), **CP-IV.4**: `#116` (CF 1479E), **CP-IV.5**: `#194` (Luogu P6633), **CP-IV.8**: `#082` (Toyota 2023 Spring Final E) | `R-53`, `R-54`, `R-55`, `R-58` |
     ```
