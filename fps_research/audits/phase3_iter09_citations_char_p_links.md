# Phase 3 Iteration 9 Audit Report — Full Citation Verification, Reserve Problem Archive, Characteristic-$p$ Audit & Cross-Links

- **Auditor**: `fps-textbook-critic` (Phase 3 Iteration 9 Global Specialist Critic)
- **Date**: 2026-10-15
- **Scope**:
  1. `SOURCES.qmd` vs. `fps_research/CITATIONS.md` + citation and terminology integration across all 24 chapters (`chapters/ch01-*.qmd`–`chapters/ch24-*.qmd`).
  2. `capstones/problem-archive-guide.qmd` vs. `fps_research/problem_archive.md`, `fps_research/CURRICULUM_ARCHITECTURE.md`, all 24 chapters, 6 checkpoints (`checkpoints/cp01-*.qmd`–`checkpoints/cp06-*.qmd`), and `capstones/synthesis-reserve.qmd` (covering all 254 curated problems `#001`–`#254`, 67 quarantined templates `R-01`–`R-67`, and 12 Revisited Dual-Perspective Bridges).
  3. Characteristic-$p$ (`p = 998244353` vs. small/composite $p$) & 16 Canonical Failure Modes (`#1`–`#16`) across `chapters/ch01-*.qmd`–`chapters/ch24-*.qmd`, `STUDY_PLAN.qmd`, `00-prerequisite-audit/chapter.qmd`, and `CONTENT_AUDIT.md`.
  4. Global `.qmd` cross-links, `#anchor` targets, navigation integrity in `_quarto.yml`, `index.qmd`, `STUDY_PLAN.qmd`, `NOTATION.qmd`, `SOURCES.qmd`, and Quarto formatting/render safety.

---

## Executive Summary & Verdict Matrix

| Audit Checklist | Status | Key Findings Summary |
| :--- | :--- | :--- |
| **Checklist 1A: Bibliography & Rosetta Stone (`SOURCES.qmd` vs. `CITATIONS.md`)** | **ACTION REQUIRED (MODERATE)** | `SOURCES.qmd` (`#fps-bibliography`) includes 48 bibliography rows (62 citation codes) vs. 79 rows (85 citation codes) in `fps_research/CITATIONS.md` — **18 bibliography rows (23 citation codes) are omitted**, plus `CITATIONS.md` §2 (Cross-Wave / Chapter-to-Citation Index Matrix) is omitted. All 75 Rosetta Stone rows (`#fps-rosetta-stone`) are present in both files (with minor LaTeX/abbreviation divergences in 13 rows). Chapters credit authors in prose rather than using bracketed `[EN-...]`/`[ZH-...]`/`[JA-...]` citation codes. |
| **Checklist 1B: 67 Quarantined Templates (`R-01`–`R-67`)** | **ACTION REQUIRED (CRITICAL IN CH 02 & CH 07)** | `capstones/problem-archive-guide.qmd` (§1, §4.1, §4.2) and `fps_research/problem_archive.md` are **100% consistent** across all 67 `R-01`–`R-67` entries. However, **`Ch 02` (lines 1358–1375) and `Ch 07` (lines 1635–1636) contain hallucinated/scrambled `R-xx` mappings** in their end-of-chapter Library Verification Footnotes; `Ch 05` omits `R-64, R-65`; and `Ch 11, 13, 14, 15, 16` omit their assigned `R-xx` verification callouts. |
| **Checklist 2: 254 Problem Archive (`#001`–`#254`) & 12 Dual-Perspective Bridges** | **ACTION REQUIRED (CRITICAL IN CH 17 & CH 18)** | `capstones/problem-archive-guide.qmd` (§1 and §2.1) matches `fps_research/problem_archive.md` **100%** across all 254 problems, and all 254 `#pid` tags appear in their exact assigned chapter/checkpoint/capstone `.qmd` files. However: (1) **`Ch 17` replaces the problem statements/titles of `#204` (`[Adv-2]`) and `#138` (`[Mas-1]`)** with different problems (`Luogu P7599: 数树` instead of `[APIO2021] 雨林跳跃`, and `CF Gym 102586J` instead of `CF Gym 102538F`); (2) **`Ch 18` has two wrong `#pid` citations in prose** (`#038` on line 263 and `#236` on line 385); (3) **`Ch 21` line 436 mislabels Revisited #11** as `#201 / #036` instead of `#220`; and (4) `index.qmd` line 177 says `#001–#321` instead of `#001–#254 & R-01–R-67`. |
| **Checklist 3: Characteristic-$p$ & 16 Canonical Failure Modes (`#1`–`#16`)** | **ACTION REQUIRED (MODERATE)** | Every Characteristic-$p$ bypass (`p \le N` nilpotency, Lucas/Frobenius, 2-adic valuation, Bostan–Mori/Lagrange algebraicity, $p$-adic lifting) and all 16 Canonical Failure Modes are substantively taught with zero gaps. However, **`Failure Mode #15` has a 3-way numbering collision** across `Ch 01` (line 502), `Ch 13` (line 394), and `Ch 16` / `CP-IV` / `STUDY_PLAN.qmd` (Improper Rational Diagonal pole at $z=0$); `Ch 08` (line 1248) uses a local `Failure Mode #1 Guard`; and `STUDY_PLAN.qmd` (line 134, 147) omits `Failure Modes #3, #4` in `Ch 02` and `Failure Mode #15` in `Ch 13`. |
| **Checklist 4: Global Cross-Links, Anchors, Navigation & Quarto Safety** | **ACTION REQUIRED (1 BROKEN LINK)** | Across all `.qmd` files in the repository, there is **exactly 1 broken `.qmd` file link** (`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd:L263` $\to$ `../checkpoints/cp03-part3-combinatorial-classes-grammar.qmd`) and **0 broken `#anchor` targets**. `_quarto.yml` navigation and Quarto formatting safety (`\(`, `\[`, table pipes, `<details>`) are **100% clean**. |

---

## Checklist 1: Bibliography, Multilingual Rosetta Stone & Quarantined Template Citations

### 1.1 `SOURCES.qmd` vs. `fps_research/CITATIONS.md` — Omitted Bibliography Entries

- **Location**: [SOURCES.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/SOURCES.qmd#L84-L177) vs. [fps_research/CITATIONS.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L13-L108)
- **Diagnostic**:
  - `fps_research/CITATIONS.md` Section 1 contains **79 bibliography rows (85 citation codes)** across Categories I–V, whereas `SOURCES.qmd` (`#fps-bibliography`) contains **48 bibliography rows (62 citation codes)**.
  - Specifically, **18 bibliography rows** and **4 secondary citation-code aliases** from `CITATIONS.md` are missing from `SOURCES.qmd`:
    1. **Category II (`SOURCES.qmd:L113-L133` — 7 omitted peer-reviewed papers)**:
       - `[EN-Pr-BP00]` — Mireille Bousquet-Mélou & Marko Petkovšek (2000), *"Linear Recurrences with Constant Coefficients: the Multivariate Case"*, Discrete Mathematics 225(1–3), 51–75 (Ch 17).
       - `[EN-Pr-AAK03]` — Michael H. Albert, M. D. Atkinson, & Martin Klazar (2003), *"The Enumeration of Simple Permutations"*, Journal of Integer Sequences 6, Article 03.4.4 (Ch 12, Ch 21).
       - `[EN-Pr-Fo65]` — Dominique Foata (1965), *"Etude algébrique de certains problèmes d'analyse combinatoire et du calcul des probabilités"*, Publ. Inst. Statist. Univ. Paris 14, 81–241 (Ch 15).
       - `[EN-Pr-ASU75]` — Alfred V. Aho, Kenneth Steiglitz, & Jeffrey D. Ullman (1975), *"Evaluating Polynomials at Fixed Sets of Points"*, SIAM Journal on Computing 4(4), 533–539 (Ch 07).
       - `[EN-Pr-HK71]` — M. L. J. Hautus & D. A. Klarner (1971), *"The Diagonal of a Double Power Series"*, Duke Mathematical Journal 38(2), 229–235 (Ch 16).
       - `[EN-Pr-BLS17]` — Alin Bostan, Pierre Lairez, & Bruno Salvy (2017), *"Multiple Binomial Sums"*, Journal of Symbolic Computation 80, 351–386 (Ch 16, Ch 18).
       - `[EN-Pr-St80]` — Richard P. Stanley (1980), *"Differentiably Finite Power Series"*, European Journal of Combinatorics 1(2), 175–188 (Ch 18).
    2. **Category III (`SOURCES.qmd:L137-L157` — 2 omitted rows + 4 dropped secondary codes)**:
       - Omitted row `[ZH-Bg-XYX20]` — `x义x` (`xyx`), *Formal Power Series, EGF/OGF Combinatorial Classes, Relaxed Convolution, and Transposed Multiplication Blog Compendium*, 2019–2022 (Ch 01–Ch 10, Ch 20–Ch 21).
       - Omitted row `[ZH-Bg-OIW]` — OI-Wiki Contributors, *OI-Wiki — Math: Polynomials & Generating Functions*, <https://oi-wiki.org/math/poly/intro/> (Ch 01–Ch 10).
       - Dropped secondary code `[ZH-NT-LBT19]` on line 146 (`SOURCES.qmd` has only `[ZH-Lu-LBT19]`; `CITATIONS.md` line 67 has `[ZH-Lu-LBT19]` / `[ZH-NT-LBT19]`).
       - Dropped secondary code `[ZH-Bl-EI20]` on line 149 (`SOURCES.qmd` has only `[ZH-Bg-EI20]`; `CITATIONS.md` line 70 has `[ZH-Bg-EI20]` / `[ZH-Bl-EI20]`).
       - Dropped secondary code `[ZH-NT-YHX20]` on line 151 (`SOURCES.qmd` has only `[ZH-Bg-YHX20]`; `CITATIONS.md` line 72 has `[ZH-Bg-YHX20]` / `[ZH-NT-YHX20]`).
       - Dropped secondary code `[ZH-Bg-War21]` on line 155 (`SOURCES.qmd` has only `[ZH-So-War21]`; `CITATIONS.md` line 77 has `[ZH-So-War21]` / `[ZH-Bg-War21]`).
    3. **Category IV (`SOURCES.qmd:L161-L168` — 5 omitted Japanese entries)**:
       - `[JA-Bg-Mo21]` — Ryuhei Mori (森立平), *「母関数を使って級数を計算する」「ラグランジュの反転公式」*, 2021 (Ch 05, Ch 11).
       - `[JA-Bg-KK23]` — `KowerKoint` & `@hotman78`, *Formal Power Series Implementation & Competitive Programming Guides*, Qiita / Hatena Blog, 2020–2023 (Ch 01–Ch 08).
       - `[JA-Bg-AC26]` — AtCoder Official Editorials & `traP` (Tokyo Tech Digital Creators Club) Lectures, *FPS in Competitive Programming*, 2020–2026 (Ch 01–Ch 10).
       - `[JA-Bg-Ha21]` — `hamamu`, *「バーレカンプ・マッシー法 (Berlekamp-Massey Algorithm) の解説」*, Hatena Blog (Ch 05).
       - `[JA-ln-De17]` — `DEGwer` (Masataka Yoneda / 米田優峻), *「数え上げPDF (Counting in Competitive Programming)」*, 2017 (Ch 03, Ch 04, Ch 06, Ch 11).
    4. **Category V (`SOURCES.qmd:L172-L177` — 4 omitted English CP tutorial entries)**:
       - `[EN-Tu-CPA]` / `[EN-CP-CPA]` — CP-Algorithms Contributors, *Algebra: Fast Fourier Transform, Operations on Polynomials and Series*, <https://cp-algorithms.com/> (Ch 01, Ch 02, Ch 07).
       - `[EN-CP-Er20]` — Kamil Dębowski (`Errichto`) & `chilli`, *Codeforces Tutorials on Generating Functions, Berlekamp–Massey, and NTT*, 2019–2021 (Ch 05, Ch 07).
       - `[EN-CP-El20]` — Zixiang Zhou (`Elegia`), `Indistinguishable`, & `Egor`, *Codeforces Research Discussions on Algebraic Generating Functions, Nimber Arithmetic, and P-Recursive Series*, 2019–2023 (Ch 16–Ch 24).
       - `[EN-CP-3B23]` — Grant Sanderson (`3Blue1Brown`) & Marko Riedel (MSE), *Olympiad Generating Function & Roots-of-Unity Filter Expositions*, 2018–2023 (Ch 07).
  - Additionally, `CITATIONS.md` Section 2 (**Cross-Wave / Chapter-to-Citation Index Matrix**, lines 111–142) is not included in `SOURCES.qmd`.

#### Drop-in Fix for `SOURCES.qmd` (Lines 133, 146–157, 168, 177)

1. **Insert the 7 missing Category II rows at `SOURCES.qmd:L133`** (after `[EN-Pr-Ges84]`):
```markdown
| **`[EN-Pr-BP00]`** | Mireille Bousquet-Mélou & Marko Petkovšek | *"Linear Recurrences with Constant Coefficients: the Multivariate Case"* | Discrete Mathematics 225(1–3), 51–75, 2000 | **Ch 17**: The Kernel Method for multivariate recurrences, obstinate kernel method, and quarter-plane lattice walks. |
| **`[EN-Pr-AAK03]`** | Michael H. Albert, M. D. Atkinson, & Martin Klazar | *"The Enumeration of Simple Permutations"* | Journal of Integer Sequences, Vol. 6, Article 03.4.4, 2003 | **Ch 12, Ch 21**: Functional inversion of permutation OGFs $\sum n! x^n$, simple permutations, and compositional decomposition trees. |
| **`[EN-Pr-Fo65]`** | Dominique Foata | *"Etude algébrique de certains problèmes d'analyse combinatoire et du calcul des probabilités"* | Publ. Inst. Statist. Univ. Paris 14, 81–241, 1965 | **Ch 15**: The Cartier–Foata commutation monoid and weighted Dyck/Motzkin lattice path decomposition. |
| **`[EN-Pr-ASU75]`** | Alfred V. Aho, Kenneth Steiglitz, & Jeffrey D. Ullman | *"Evaluating Polynomials at Fixed Sets of Points"* | SIAM Journal on Computing 4(4), 533–539, 1975 | **Ch 07**: Chirp Z-Transform (Bluestein's identity) and geometric multipoint evaluation. |
| **`[EN-Pr-HK71]`** | M. L. J. Hautus & D. A. Klarner | *"The Diagonal of a Double Power Series"* | Duke Mathematical Journal 38(2), 229–235, 1971 | **Ch 16**: Algebraic diagonals of bivariate rational functions via residue contour reduction. |
| **`[EN-Pr-BLS17]`** | Alin Bostan, Pierre Lairez, & Bruno Salvy | *"Multiple Binomial Sums"* | Journal of Symbolic Computation 80, 351–386, 2017 | **Ch 16, Ch 18**: Creative telescoping, rational diagonals, and D-finite differential operators. |
| **`[EN-Pr-St80]`** | Richard P. Stanley | *"Differentiably Finite Power Series"* | European Journal of Combinatorics 1(2), 175–188, 1980 | **Ch 18**: Foundational closure properties of D-finite (holonomic) power series and P-recursive sequences. |
```

2. **Restore secondary codes and add the 2 missing Category III rows at `SOURCES.qmd:L146-L157`**:
```markdown
| **`[ZH-Lu-LBT19]`** / **`[ZH-NT-LBT19]`** | 罗煜翔 (`command_block`, Luogu Blog) | *《多项式计数杂谈》 (Miscellaneous Notes on Polynomial Counting) & 《生成函数杂谈》* | Luogu Blog Showcase, 2019–2021 | **Ch 01–Ch 14**: Comprehensive bridge from elementary EGF/OGF modeling to Euler's pentagonal theorem, Lagrange inversion, and tree counting. |
| **`[ZH-Bg-EI20]`** / **`[ZH-Bl-EI20]`** | 虞皓翔 (`Elegia` / `EI`) | *Blog & UOJ Community Articles: D-Finite / ODE Automaton (`ODE自动机`), Transposed Principle, and Half-GCD* | UOJ Blog / GitHub Pages, 2019–2023 | **Ch 02, Ch 06, Ch 16, Ch 18, Ch 19, Ch 21**: Differential method (`微分法`) for $O(n)$ power-of-polynomial, binomial sum reduction, creative telescoping, and fast polynomial GCD. |
| **`[ZH-Bg-YHX20]`** / **`[ZH-NT-YHX20]`** | 严誉 (`yhx-12243`) | *Competitive Programming Notes on Generating Functions, Burnside/Pólya, and Bivariate Kernel Method* | Personal Blog (`yhx-12243.github.io`), 2018–2021 | **Ch 03, Ch 04, Ch 13, Ch 15, Ch 17**: Step-by-step algebraic derivations for high-difficulty Chinese provincial and national team training problems. |
| **`[ZH-So-War21]`** / **`[ZH-Bg-War21]`** | 沃若 (`Waaall` / `War`) | *《多项式全家桶与生成函数》 (The Complete Polynomial Family Bucket & Generating Functions)* | Blog Series, 2020–2022 | **Ch 01, Ch 02, Ch 05, Ch 07, Ch 20**: Engineering implementation of NTT, Newton iteration, Bostan–Mori, multipoint evaluation, and constant-factor optimization. |
| **`[ZH-Bg-XYX20]`** | `x义x` (`xyx`) | *Formal Power Series, EGF/OGF Combinatorial Classes, Relaxed Convolution, and Transposed Multiplication Blog Compendium* | CSDN / Blog Series, 2019–2022 | **Ch 01–Ch 10, Ch 20–Ch 21**: Intuitive expositions of CDQ NTT, semi-online convolution, and the Tellegen transposition principle. |
| **`[ZH-Bg-OIW]`** | OI-Wiki Contributors | *OI-Wiki — Math: Polynomials & Generating Functions (`多项式与生成函数`)* | <https://oi-wiki.org/math/poly/intro/> | **Ch 01–Ch 10**: Standard Chinese competitive programming reference for polynomial templates and terminology. |
```

3. **Insert the 5 missing Category IV rows at `SOURCES.qmd:L168`** (after `[JA-Li-ACL20]`):
```markdown
| **`[JA-Bg-Mo21]`** | Ryuhei Mori (森立平) | *「母関数を使って級数を計算する」「ラグランジュの反転公式」 (Calculating Series Using Generating Functions & Lagrange Inversion)* | Qiita / Personal Technical Notes, 2021 | **Ch 05, Ch 11**: Pedagogical bridge between rational/algebraic generating functions and residue calculus. |
| **`[JA-Bg-KK23]`** | `KowerKoint` & `@hotman78` | *Formal Power Series Implementation & Competitive Programming Guides* | Qiita / Hatena Blog, 2020–2023 | **Ch 01–Ch 08**: Practical guide to translating DP recurrences into FPS operations on AtCoder ABC/ARC/AGC tasks. |
| **`[JA-Bg-AC26]`** | AtCoder Official Editorials & `traP` (Tokyo Tech Digital Creators Club) | *FPS in Competitive Programming (`競技プログラミングにおける形式的べき級数`)* | AtCoder / `trap.jp` Lectures, 2020–2026 | **Ch 01–Ch 10**: Introductory and intermediate problem-solving patterns using `atcoder::convolution`. |
| **`[JA-Bg-Ha21]`** | `hamamu` | *「バーレカンプ・マッシー法 (Berlekamp-Massey Algorithm) の解説」* | Hatena Blog | **Ch 05**: Visual discrepancy-update derivation of the Berlekamp–Massey shortest LFSR algorithm. |
| **`[JA-ln-De17]`** | `DEGwer` (Masataka Yoneda / 米田優峻) | *「数え上げPDF (Counting in Competitive Programming)」* | Comprehensive Lecture Notes, 2017 | **Ch 03, Ch 04, Ch 06, Ch 11**: Canonical Japanese competitive programming reference on combinatorial enumeration, Catalans, trees, and generating functions. |
```

4. **Insert the 4 missing Category V rows at `SOURCES.qmd:L177`** (after `[EN-CP-Ch19]`):
```markdown
| **`[EN-Tu-CPA]`** / **`[EN-CP-CPA]`** | CP-Algorithms Contributors | *Algebra: Fast Fourier Transform, Operations on Polynomials and Series* | <https://cp-algorithms.com/> | **Ch 01, Ch 02, Ch 07**: Standard English competitive programming reference for FFT/NTT and Newton's method. |
| **`[EN-CP-Er20]`** | Kamil Dębowski (`Errichto`) & `chilli` | *Codeforces Tutorials on Generating Functions, Berlekamp–Massey, and NTT* | Codeforces Blogs, 2019–2021 | **Ch 05, Ch 07**: Practical implementation notes and complexity benchmarks for BM + Bostan–Mori. |
| **`[EN-CP-El20]`** | Zixiang Zhou (`Elegia`), `Indistinguishable`, & `Egor` | *Codeforces Research Discussions on Algebraic Generating Functions, Nimber Arithmetic, and P-Recursive Series* | Codeforces Blogs, 2019–2023 | **Ch 16–Ch 24**: High-end algorithmic crossovers between computer algebra and competitive programming. |
| **`[EN-CP-3B23]`** | Grant Sanderson (`3Blue1Brown`) & Marko Riedel (MSE) | *Olympiad Generating Function & Roots-of-Unity Filter Expositions* | YouTube / Mathematics Stack Exchange, 2018–2023 | **Ch 07**: Visual and complex-analytic motivation for the roots-of-unity multisection filter (e.g., IMO 1995 P6). |
```

---

### 1.2 Multilingual Terminology Rosetta Stone (`SOURCES.qmd` vs. `fps_research/CITATIONS.md`)

- **Location**: [SOURCES.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/SOURCES.qmd#L180-L260) vs. [fps_research/CITATIONS.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L145-L224)
- **Diagnostic**:
  - All **75 rows (`1`–`75`)** are present in both `SOURCES.qmd` (`#fps-rosetta-stone`) and `fps_research/CITATIONS.md` §3.
  - Minor textual/notation divergences exist in 13 rows (`Rows 40, 44, 45, 50, 56, 61, 63, 64, 65, 66, 67, 71, 74`):
    - **Row 67 (`SOURCES.qmd:L251` vs. `CITATIONS.md:L216`)**: `SOURCES.qmd` writes `$\operatorname{mul}^T(F, G)$` whereas `CITATIONS.md`, `NOTATION.qmd:L86`, and `Ch 21` write `$\operatorname{mulT}(F, G)$` (or `$\operatorname{mul}^{\top}$`). Align `SOURCES.qmd:L251` to `$\operatorname{mulT}(F, G)$` for notation consistency with `NOTATION.qmd`.
    - **Row 40 (`SOURCES.qmd:L224` vs. `CITATIONS.md:L189`)**: `SOURCES.qmd` drops the explanatory parenthetical `(Matrix-Tree / Prüfer)` in English and `(無向連結グラフ / ケイリーの公式)` in Japanese.
    - **Row 44 (`SOURCES.qmd:L228` vs. `CITATIONS.md:L193`)**: `SOURCES.qmd` abbreviates `Robinson's DAG Recurrence (Layer-by-Layer IE)` to `Robinson's DAG Recurrence`.

---

### 1.3 Quarantined Library Verification Footnotes (`R-01`–`R-67`) Across Chapters vs. `capstones/problem-archive-guide.qmd`

- **Location**:
  - Master Reference: [capstones/problem-archive-guide.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd#L172-L202) and [capstones/problem-archive-guide.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd#L969-L1061) vs. [fps_research/problem_archive.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md#L279-L369).
  - Chapter Footnotes: `chapters/ch01-*.qmd` through `chapters/ch24-*.qmd`.
- **Verification of `capstones/problem-archive-guide.qmd` vs. `fps_research/problem_archive.md`**:
  - **100% PASS**: All 67 quarantined reference templates (`R-01` through `R-67`) match 100% between `capstones/problem-archive-guide.qmd` (§1 table at lines 172–202, §4.1 table at lines 971–1040, and §4.2 table at lines 1046–1061) and `fps_research/problem_archive.md`.
- **CRITICAL Discrepancies in Chapter Footnotes**:
  1. **[CRITICAL] `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd` (lines 1358–1375) — Scrambled/Hallucinated `R-06, R-09–R-19` Table**:
     - In [chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L1358-L1375), the callout titled `Library Verification Footnotes (R-06, R-09–R-19)` includes `R-11` (which actually belongs to **Ch 01**, `Library Checker — product_of_polynomial_sequence`, already cited in `Ch 01` line 848!) and shifts/scrambles the meanings of `R-06` and `R-09` through `R-19`:
       - `Ch 02` claims `R-06` = `cp-algorithms — Operations on polynomials and series` (actual `R-06` = `Library Checker — inv_of_formal_power_series_sparse`).
       - `Ch 02` claims `R-09` = `Library Checker — log_of_formal_power_series` (actual `R-09` = `Library Checker — pow_of_formal_power_series_sparse`).
       - `Ch 02` claims `R-10` = `Library Checker — exp_of_formal_power_series` (actual `R-10` = `Library Checker — sqrt_of_formal_power_series_sparse`).
       - `Ch 02` claims `R-11` = `Library Checker — pow_of_formal_power_series` (actual `R-11` = `Library Checker — product_of_polynomial_sequence` in Ch 01).
       - `Ch 02` claims `R-12` = `Library Checker — sqrt_of_formal_power_series` (actual `R-12` = `Library Checker — log_of_formal_power_series`).
       - `Ch 02` claims `R-13`–`R-17` = the 5 sparse LC tasks (actual `R-13` = `exp`, `R-14` = `pow`, `R-15` = `sqrt`, `R-16` = `Luogu P4725`, `R-17` = `Luogu P4726`).
       - `Ch 02` claims `R-18` = `Luogu P4725 / P4726` and `R-19` = `Luogu P5205 / P5245` (actual `R-18` = `Luogu P5205`, `R-19` = `Luogu P5245`).
  2. **[CRITICAL] `chapters/ch07-roots-of-unity-cyclotomic-czt.qmd` (lines 1635–1636) — Hallucinated `R-02, R-31, R-45` Descriptions**:
     - In [chapters/ch07-roots-of-unity-cyclotomic-czt.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd#L1635-L1636), the callout writes:
       - `**R-02**: Arbitrary-Modulus Polynomial Multiplication (MTT / 3-Prime NTT) — Luogu P4245 / Library Checker convolution_mod_1000000007` (actually **`R-02`** is `Library Checker — convolution_mod_1000000007`, **`R-03`** is `Luogu P4245`, and **`R-04`** is `Library Checker — convolution_mod_2_64`).
       - `**R-31**: Chirp Z-Transform & Geometric Multipoint Evaluation — Luogu P6800 (Chirp Z-Transform) / Luogu P5050 (Multipoint Evaluation)` (actually **`R-31`** is `Luogu P6800 — 【模板】Chirp Z-Transform`, while `Luogu P5050` is **`R-26`** in Ch 20).
       - `**R-45**: Arbitrary-Modulus Polynomial Power & Roots-of-Unity Filter Verification — Luogu P5245 / Garner Reconstruction` (actually **`R-45`** is `Luogu P4721 — 【模板】分治 FFT` in Ch 10! The third quarantined template assigned to Ch 07 in `problem-archive-guide.qmd:L182` is **`R-04`**, not `R-45`).
  3. **[MINOR] `chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd` (line 1871) — Omitted `R-64, R-65`**:
     - `Ch 05` line 1871 lists `R-05, R-39, R-40, R-41`, omitting `R-64` (`QOJ 942 — Find the Determinant` / sparse BM) and `R-65` (`POJ 3762` / linear recurrence acceleration) which are assigned to Ch 05 in `problem-archive-guide.qmd:L180, L1037-L1038`.
  4. **[MODERATE] Missing Quarantined Library Verification Callouts in `Ch 11`, `Ch 13`, `Ch 14`, `Ch 15`, `Ch 16`**:
     - According to `capstones/problem-archive-guide.qmd` (§1 lines 186–191 and §4.2 lines 1046–1061), the following chapters have quarantined reference entries (`R-xx`) that are not yet cited at the end of those chapters:
       - `Ch 11` (`chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd`): `R-61` (`ARC 116 E`), `R-62` (`CF 917D` alternative submission).
       - `Ch 13` (`chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd`): `R-38` (`Library Checker — counting_eulerian_circuits`), `R-59` (`ABC 236 Ex`).
       - `Ch 14` (`chapters/ch14-set-cover-inclusion-exclusion-exp-log.qmd`): `R-53` (`ARC 118 E`), `R-54` (`ABC 266 Ex`), `R-55` (`ABC 242 Ex`), `R-58` (`ARC 105 F`).
       - `Ch 15` (`chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`): `R-63` (`CF 1556F`).
       - `Ch 16` (`chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`): `R-42` (`HackerRank — Sum ofitan`), `R-43` (`POJ 3734 — Blocks`).

#### Drop-in Fix for `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd` (Lines 1358–1375)

Replace lines 1358–1375 of `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd` with:
```markdown
::: {.callout-note}
### Library Verification Footnotes (R-06, R-07–R-10, R-12–R-19)

To benchmark and regression-test your implementations of the dense $O(N \log N)$ Newton iteration pipeline (§2.4) and the $O(N K)$ sparse ODE recurrence pipeline (§2.3), use the following quarantined reference templates from the [Master Problem Archive & Quarantine Ledger](../capstones/problem-archive-guide.qmd#complete-quarantined-template-verification-guide-r-01r-67):

| Archive ID | Judge & Task Identifier | Target Algorithm & Complexity |
| :--- | :--- | :--- |
| **`R-06`** | Library Checker — `inv_of_formal_power_series_sparse` | Sparse reciprocal $1/F(x) \bmod x^N$ in $O(NK)$ (§2.3.1) |
| **`R-07`** | Library Checker — `log_of_formal_power_series_sparse` | Sparse logarithmic derivative + integration $\ln F(x) \bmod x^N$ in $O(NK)$ (§2.3.2) |
| **`R-08`** | Library Checker — `exp_of_formal_power_series_sparse` | Sparse differential equation $E' = F' E \implies \exp F(x) \bmod x^N$ in $O(NK)$ (§2.3.3) |
| **`R-09`** | Library Checker — `pow_of_formal_power_series_sparse` | Sparse ODE $F G' = \alpha F' G \implies F(x)^M \bmod x^N$ in $O(NK)$ with valuation shift (§2.3.5) |
| **`R-10`** | Library Checker — `sqrt_of_formal_power_series_sparse` | Sparse ODE $2 F S' = F' S \implies \sqrt{F(x)} \bmod x^N$ in $O(NK)$ + Tonelli–Shanks (§2.3.4) |
| **`R-12`** | Library Checker — `log_of_formal_power_series` | Dense $\ln F(x) = \int \frac{F'(x)}{F(x)}\,dx \bmod x^N$ in $O(N \log N)$ (§2.4.1) |
| **`R-13`** | Library Checker — `exp_of_formal_power_series` | Dense Newton iteration for $\exp F(x) \bmod x^N$ in $O(N \log N)$ (§2.4.2) |
| **`R-14`** | Library Checker — `pow_of_formal_power_series` | Dense valuation-shifted $\exp(M \ln F_1(x)) \bmod x^N$ in $O(N \log N)$ (§2.4.4) |
| **`R-15`** | Library Checker — `sqrt_of_formal_power_series` | Dense Newton iteration for $\sqrt{F(x)} \bmod x^N$ + Cipolla/Tonelli–Shanks (§2.4.3) |
| **`R-16` / `R-17`** | Luogu P4725 (`【模板】多项式对数函数`) / P4726 (`【模板】多项式指数函数`) | Chinese judge verification for dense $\ln$ and $\exp$ modulo $998244353$ |
| **`R-18` / `R-19`** | Luogu P5205 (`【模板】多项式开根`) / P5245 (`【模板】多项式快速幂`) | Chinese judge verification for dense $\sqrt{F}$ ($[x^0]F=1$) and $F(x)^K$ |
:::
```

#### Drop-in Fix for `chapters/ch07-roots-of-unity-cyclotomic-czt.qmd` (Lines 1632–1638)

Replace lines 1632–1638 of `chapters/ch07-roots-of-unity-cyclotomic-czt.qmd` with:
```markdown
::: {.callout-tip}
### Quarantined Library Verification Footnotes (`R-02`, `R-03`, `R-04`, `R-31`)

To verify your implementation of the foundational transform primitives developed in this chapter before tackling the problem ladder, submit to the following standard library-verification benchmarks (quarantined from the reasoning ladder per the [Master Problem Archive & Quarantine Ledger](../capstones/problem-archive-guide.qmd#complete-quarantined-template-verification-guide-r-01r-67)):

- **`R-02`**: *Arbitrary-Modulus Convolution ($\bmod 10^9+7$)* — Library Checker `convolution_mod_1000000007` (§7.4 Three-Prime NTT + Garner's Algorithm).
- **`R-03`**: *Arbitrary-Modulus Polynomial Multiplication (MTT)* — Luogu P4245 `【模板】任意模数多项式乘法` (§7.4).
- **`R-04`**: *Convolution Modulo $2^{64}$* — Library Checker `convolution_mod_2_64` (§7.4 5-Prime NTT / Karatsuba verification).
- **`R-31`**: *Chirp Z-Transform (Geometric Multipoint Evaluation)* — Luogu P6800 `【模板】Chirp Z-Transform` (§7.3 Bluestein's identity $ij = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$).
:::
```

---

## Checklist 2: Reserve Problem Archive (`#001`–`#254`) & 12 Dual-Perspective Bridges

### 2.1 Master Problem Ledger (`capstones/problem-archive-guide.qmd` vs. `fps_research/problem_archive.md`)

- **Verification Result**:
  - **100% PASS on `capstones/problem-archive-guide.qmd` vs. `fps_research/problem_archive.md`**:
    - Every single problem ID `#001` through `#254` is accounted for in both Section 1 (By-Chapter & By-Part Curriculum Mapping, lines 38–169) and Section 2.1 (Complete Numerical Index `#001`–`#254`, lines 625–891) of `capstones/problem-archive-guide.qmd`.
    - All 192 Chapter Ladder slots (`24 × 8`), 48 Blind Checkpoint slots (`6 × 8`), and 14 Capstone Synthesis Reserve slots (`192 + 48 + 14 = 254`), plus all 67 Quarantined Templates (`R-01`–`R-67`, total `254 + 67 = 321`), match `fps_research/problem_archive.md` and `fps_research/CURRICULUM_ARCHITECTURE.md` 100%.

### 2.2 CRITICAL Problem Statement / Contest-ID Mismatches in `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`

- **Location**:
  1. [chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L953-L1028) (`#204`, `Ch 17 [Adv-2]`)
  2. [chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L1030-L1107) (`#138`, `Ch 17 [Mas-1]`)
- **Diagnostic**:
  1. **`#204` (`Ch 17 [Adv-2]`) Conflict**:
     - In `fps_research/problem_archive.md:L219`, `fps_research/CURRICULUM_ARCHITECTURE.md:L1135`, and `capstones/problem-archive-guide.qmd:L426, L837`, `#204` is **`Luogu P7599 — [APIO2021] 雨林跳跃 (2D Dominance Lattice Walk + Bivariate Kernel Method)`**.
     - However, in `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd:L953`, the problem heading and problem statement are written as **`### Advanced 2 (#204) — Coupled Bipartite Tree Enumeration (Luogu P7599: 数树)`**, which is a 2-variable Good–Lagrange bipartite forest problem (and note that on Luogu, `P7599` is `[APIO2021] 雨林跳跃`, while `[Ynoi2019] 数树` is `Luogu P5285`!).
  2. **`#138` (`Ch 17 [Mas-1]`) Conflict**:
     - In `fps_research/problem_archive.md:L153`, `fps_research/CURRICULUM_ARCHITECTURE.md:L1135`, and `capstones/problem-archive-guide.qmd:L427, L771`, `#138` is **`CF Gym 102538F — 3D Walk / Quarter Plane (3D / Quarter-Plane Walk via Obstinate Kernel + Weyl Group)`**.
     - However, in `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd:L1030`, the heading writes **`### Mastery 1 (#138) — Quarter-Plane Tandem & 3D Ballot Walk (Codeforces Gym 102586J)`**. While the mathematical content IS the 3D / quarter-plane tandem ballot walk via the $\mathfrak{S}_3$ Weyl group / obstinate kernel method (`1/(j-i)` Vandermonde determinant), the contest ID in the heading is written as `Codeforces Gym 102586J` instead of `CF Gym 102538F`.

#### Drop-in Fixes for `#204` and `#138`

- **For `#138` in `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd:L1030`**:
  Replace line 1030:
  ```markdown
  ### Mastery 1 (#138) — Quarter-Plane Tandem & 3D Ballot Walk (CF Gym 102538F: 3D Walk / Quarter Plane)
  ```
- **For `#204` in `capstones/problem-archive-guide.qmd` vs. `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`**:
  - Note: Because `Luogu P7599` (`[APIO2021] 雨林跳跃`) is actually a Cartesian-tree / binary-lifting data structure problem on Luogu and NOT a generating function problem (an artifact from the original raw problem pool), the author of `Ch 17` wisely replaced `#204` with a genuine 2-variable Good–Lagrange coupled bipartite tree problem (`Coupled Bipartite Tree Enumeration`, which exercises §17.3 Good–Lagrange in the problem ladder!).
  - Therefore, to make `Ch 17` and `capstones/problem-archive-guide.qmd` 100% consistent without losing the Good–Lagrange ladder coverage in `Ch 17`:
    1. In `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd:L953`, remove the erroneous `(Luogu P7599: 数树)` subtitle or clarify it as `### Advanced 2 (#204) — Coupled Bipartite Tree Enumeration via 2D Good–Lagrange (Luogu P7599 Variant / Bipartite Forest EGF)`.
    2. In `capstones/problem-archive-guide.qmd:L426` and `L837`, update the title of `#204` to `Luogu P7599 (Variant) — Coupled Bipartite Tree Enumeration (2D Good–Lagrange Jacobian Determinant)` so that the Archive Guide matches `Ch 17 [Adv-2]` 100%.

---

### 2.3 Stale / Erroneous `#pid` References in Prose Across Chapters & `index.qmd`

1. **`index.qmd:L177` — Outdated `#001–#321` numbering**:
   - **Location**: [index.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/index.qmd#L177)
   - **Current Text**:
     `| [Problem Archive & Quarantine Guide](capstones/problem-archive-guide.qmd) | Complete 321-Problem Curated Index & Quarantine Ledger (`#001`–`#321`) |`
   - **Drop-in Fix**:
     `| [Problem Archive & Quarantine Guide](capstones/problem-archive-guide.qmd) | Complete 321-Problem Curated Index & Quarantine Ledger (`#001`–`#254` & `R-01`–`R-67`) |`

2. **`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd:L263` — Broken Link AND Wrong `#pid` (`#038`)**:
   - **Location**: [chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L263)
   - **Current Text**:
     `*Cross-Reference ([CP-III — #038 AtCoder ABC 296 Ex: Unite](../checkpoints/cp03-part3-combinatorial-classes-grammar.qmd))*`
   - **Diagnostic**:
     - The file `../checkpoints/cp03-part3-combinatorial-classes-grammar.qmd` does not exist! The actual Part III checkpoint file is `../checkpoints/cp03-part3-online-implicit-lif-graphs.qmd`.
     - Furthermore, `#038` is `ABC 288 Ex — A Nameless Counting Problem` in `Ch 24 [Mas-2]`, and `ABC 296 Ex` is not in `CP-III`! In `Ch 10` (`chapters/ch10-cdq-relaxed-convolution-implicit-trees.qmd:L1004`), the Catalan / D-finite holonomic preview is `#007` (`ABC 384 G` / `Ch 10 [Ss-2]`) or `#060` (`CF 438E — The Child and Binary Tree`, `Ch 10 [Int-1]`).
   - **Drop-in Fix for `chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd:L263`**:
     ```markdown
     *Cross-Reference ([Ch 10 — #060 CF 438E: The Child and Binary Tree](ch10-cdq-relaxed-convolution-implicit-trees.qmd) & [CP-III](../checkpoints/cp03-part3-online-implicit-lif-graphs.qmd))*: In Part III, we solved algebraic tree ecuaciones such as $T(x) = 1 + x C(x) T(x)^2$ via $O(n \log n)$ Newton square-root extraction or $O(n \log^2 n)$ CDQ divide-and-conquer FFT. Because every algebraic series is D-finite (Theorem 18.2), converting $T(x)$ into a linear ODE with polynomial coefficients reduces the coefficient extraction of $[x^n] T(x)$ to an $O(n)$ P-recursive linear recurrence—eliminating the NTT completely!
     ```

3. **`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd:L385` — Wrong `#pid` (`#236`) for `QOJ #60`**:
   - **Location**: [chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L385)
   - **Current Text**:
     `- **Canonical Problems**: **QOJ #60 (Chinese Chess / Counting 2-Regular Bipartite Graphs)** (#236), **Luogu P4491 / P6667**, and **CF 1842I / UOJ 424**.`
   - **Diagnostic**: `#236` is `yukicoder 963 — 門松列列 2 (Eulerian Numbers)` in `CP-V.1`, whereas `Counting 2-Regular Graphs` in `Ch 18` is `#013` (`ABC 353 G`, `Ch 18 [Int-1]`) and `P-Recursive ODE / Holonomic D-Finite` on UOJ is `#214` (`UOJ 515`, `Ch 18 [Adv-1]`).
   - **Drop-in Fix for `chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd:L385`**:
     ```markdown
     - **Canonical Problems**: **AtCoder ABC 353 G (Counting 2-Regular Graphs)** (#013), **UOJ 515 (P-Recursive ODE / Holonomic D-Finite)** (#214), and **QOJ 5424 (D-Finite / Holonomic Recurrence)** (#227).
     ```

4. **`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd:L436-L438` — Misnumbered Revisited Bridge (`Revisited #11` / `#201`)**:
   - **Location**: [chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd#L436-L438)
   - **Current Text**:
     `#### Dual-Perspective Bridge: Revisited #11 (#201 Luogu P7439 — [Kronecker/Lagrange] vs. Power Projection / #036 ABC 281 Ex)`
     `In **Chapter 11 (Int-1, #201 Luogu P7439)**, we extracted a single coefficient $[x^n] G(x)$ of an implicitly defined series $G(x) = x \Phi(G(x))$ in $O(n \log n)$ time via the Lagrange Inversion Formula $[x^n] G(x) = \frac{1}{n} [u^{n-1}] \Phi(u)^n$.`
   - **Diagnostic**:
     - According to `fps_research/CURRICULUM_ARCHITECTURE.md` §5.2 (line 1259) and `capstones/problem-archive-guide.qmd` §3 (line 953), `Revisited #11` is `#220 Luogu P3266 — [JLOI2015] 骗我呢` (`Ch 15` vs. `Ch 05`), whereas the `Ch 11` $\leftrightarrow$ `Ch 21` bridge is **`Revisited #12` (`#036 ABC 281 Ex — Alchemy`)**, and `#201` (`Luogu P7439`) is **`Ch 11 [Int-2]`** (not `Int-1`).
   - **Drop-in Fix for `chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd:L436-L438`**:
     ```markdown
     #### Dual-Perspective Bridge: Revisited #12 (#036 ABC 281 Ex — Alchemy & #201 Luogu P7439: Lagrange Inversion vs. Power Projection)

     In **Chapter 11 (Adv-1, #036 ABC 281 Ex; Int-2, #201 Luogu P7439)**, we extracted a single coefficient $[x^n] G(x)$ of an implicitly defined series $G(x) = x \Phi(G(x))$ in $O(n \log n)$ time via the Lagrange Inversion Formula $[x^n] G(x) = \frac{1}{n} [u^{n-1}] \Phi(u)^n$.
     ```

5. **`chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd:L1413` — Minor Citation Slip (`#201` instead of `#210`)**:
   - **Location**: [chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L1413)
   - **Current Text**:
     `We first solved UOJ 424 (#210) in Chapter 11 (§11.1–§11.2, alongside #201) using Raney's Lemma and the reflection principle.`
   - **Diagnostic**: In Chapter 11, `#210` (`UOJ 424`) is solved in `Ch 11 [Adv-2]` alongside `#060` (`CF 438E`) and `#036` (`ABC 281 Ex`), whereas `#201` (`Luogu P7439`) is an algebraic degree-3 functional equation (`Ch 11 [Int-2]`), not a Raney/reflection problem.

---

### 2.4 Audit of the 12 Revisited Dual-Perspective Bridges (`capstones/problem-archive-guide.qmd` §3)

- **Location**: [capstones/problem-archive-guide.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd#L938-L959) and [fps_research/CURRICULUM_ARCHITECTURE.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md#L1243-L1260).
- **Verification Matrix Across All 12 Dual-Perspective Problems**:

| Dual # | Problem ID & Name | Perspective A Chapter | Perspective B Chapter | Audit Status |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `#101` (`CF 1096G — Lucky Tickets`) | `Ch 01` / `Ch 07` (`O(N \log N \log K)` binary-exp NTT) | `Ch 02` (`[Int-1]`, lines 849–915: `O(N \log N)` $\exp(K \ln F)$ AND `O(N)` sparse ODE) | Both perspectives are derived in `Ch 02` (`[Int-1]`), and `Ch 07` (`#084 CF 632E`, line 1170) discusses the same pattern, though `#101` is not explicitly cited by ID in `Ch 01` or `Ch 07`. |
| **2** | `#060` (`CF 438E — The Child and Binary Tree`) | `Ch 10` (`[Int-1]`, line 996: CDQ D&C FFT) | `Ch 02` (line 807: Newton $\sqrt{\cdot}$ comparison callout) | **PASS** (explicitly cross-referenced in both `Ch 02` and `Ch 10`). |
| **3** | `#003` (`ABC 399 G — Colorful Spanning Tree`) | `Ch 04` (`[Adv-1]`, line 871: Matrix-Tree determinant of polynomials) | `Ch 05` (line 604) & `Ch 07` (line 977: Lagrange interpolation) | **PASS** (explicitly cross-referenced in `Ch 04`, `Ch 05`, and `Ch 07`). |
| **4** | `#021` (`ABC 333 G — Nearest Fraction`) / `#030` (`ABC 300 Ex — Fibonacci: Revisited`) | `Ch 05` (`[Int-1]` `#030`, line 1277: parity-splitting Bostan–Mori) | `Ch 07` (line 979: DFT root-of-unity coordinates) | **PASS** (`#030` is solved in `Ch 05` and cross-referenced in `Ch 07:L979`). |
| **5** | `#124` (`CF 960G — Bandit Blues`) | `Ch 06` (`[Int-1]`, line 911: D&C rising factorial $x^{\overline{n}}$) | `Ch 08` (line 510: first-element-minimum ODE $F' = 1 + yF^2$) | **PASS** (explicitly cross-referenced in both `Ch 06` and `Ch 08`). |
| **6** | `#028` (`ABC 305 Ex — Shojin`) | `Ch 09` (`[Adv-2]`, line 1261: Monge / Alien DP + `(min,+)` hull) | `Ch 20` (line 262: segment-tree matrix product $2 \times 2$ comparison) | **PASS** (explicitly cross-referenced in both `Ch 09` and `Ch 20`). |
| **7** | `#065` (`CF 623E — Transforming Sequence`) | `Ch 07` (`[Adv-1]`, line 1236: 3-Prime NTT + binary lifting $2^k$) | `Ch 06` (line 451: Stirling transformation into powers) | **PASS** (explicitly cross-referenced in both `Ch 06` and `Ch 07`). |
| **8** | `#085` (`CF 755G — PolandBall and Many Other Balls`) | `Ch 05` (`[Adv-1]`, line 1384: $2 \times 2$ transfer matrix / characteristic roots) | `Ch 15` (line 138: Chebyshev / holistic ODE $O(K)$ recurrence) | **PASS** (explicitly cross-referenced in both `Ch 05` and `Ch 15`). |
| **9** | `#210` (`UOJ 424 — 【集训队作业2018】count`) | `Ch 11` (`[Adv-2]`, line 1170: iterated reflection principle) | `Ch 15` (`[Mas-2]`, line 1378: Chebyshev polynomial transfer) | **PASS** (explicitly cross-referenced in both `Ch 11` and `Ch 15`). |
| **10** | `#156` (`Luogu P4548 — [CTSC2006] 歌唱王国`) | `Ch 08` (`[Int-2]` solves `#154 Luogu P3702`, line 1054, via border equations) | `Ch 14` (`[Ss-2]`, line 683: solves `#156 Luogu P4548` via PGF + border theorem) | Both perspectives are explained in `Ch 14` (`[Ss-2]` lines 683–746), though `Ch 08` does not explicitly cite `#156` by ID. |
| **11** | `#220` (`Luogu P3266 — [JLOI2015] 骗我呢`) | `Ch 15` (`[Adv-1]`, line 1044: two-wall reflection principle) | `Ch 05` (transfer matrix / Bostan–Mori perspective discussed inside `Ch 15:L1044-L1120`) | Both perspectives are compared inside `Ch 15 [Adv-1]`, though `Ch 05` does not explicitly cite `#220` by ID. |
| **12** | `#036` (`ABC 281 Ex — Alchemy`) | `Ch 11` (`[Adv-1]`, line 1068: Lagrange inversion $[x^n] F^{-1}$) | `Ch 21` (line 436: Kinoshita–Li power projection / composition inverse) | **PASS** (explicitly cross-referenced in both `Ch 11` and `Ch 21`). |

---

## Checklist 3: Characteristic-$p$ & 16 Canonical Failure Modes Audit

### 3.1 Characteristic-$p$ Audit (`p = 998244353` vs. Small/Composite $p$)

- **Locations Audited**:
  - `00-prerequisite-audit/chapter.qmd` (§3 Modular Arithmetic & Characteristic-$p$ Readiness, lines 80–125)
  - `STUDY_PLAN.qmd` (§4 The 16 Canonical Failure Modes & Characteristic-$p$ Bypasses, lines 129–162)
  - `CONTENT_AUDIT.md` (§3 Characteristic-$p$ & Failure-Mode Audit Matrix, lines 89–104)
  - Chapters `Ch 01`–`Ch 24` (`chapters/ch01-*.qmd`–`chapters/ch24-*.qmd`).
- **Verification of Characteristic-$p$ Progression (`CURRICULUM_ARCHITECTURE.md` §2.3)**:
  1. **Large Prime ($p > N$) Regime (`Ch 02` §2.1–§2.5, `Ch 03` §3.2)**:
     - Verified in `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd` (lines 72–118, 250–265): Explicitly states and proves that $\int x^k dx = \frac{x^{k+1}}{k+1}$, $\ln F(x) = \int \frac{F'}{F} dx$, and $\exp F(x)$ require $1, 2, \dots, N$ to be invertible in $R$, failing at degree $k = p$ when $p \le N$ because $\partial(x^p) = p x^{p-1} \equiv 0 \pmod p$ has a nontrivial kernel $\mathbb{F}_p[x^p]$ and $\operatorname{im}(\partial)$ misses $x^{p-1}$.
  2. **Small Prime ($p \le N$) & Frobenius Endomorphism Regime (`Ch 02` §2.2, `Ch 06` §6.1, `Ch 16` §16.4)**:
     - Verified in `Ch 02` (§2.2 lines 122–205: Frobenius $(A+B)^p \equiv A^p + B^p \pmod p$, $F(x)^p \equiv F(x^p) \pmod p$, Lucas's Theorem $\binom{n}{k} \equiv \prod \binom{n_i}{k_i} \pmod p$, and `#110 CF 1278F` small-$p$ guard at line 1044), `Ch 06` (§6.1 lines 118–150: `Failure Mode #9` Lucas bypass when $p \le N$), and `Ch 16` (§16.4 lines 520–680: Furstenberg's theorem and Christol's $\Lambda_r$ Cartier operator over $\mathbb{F}_p[[x]]$ for `#199 Luogu P6295` and `#209 UOJ 300`).
  3. **2-Adic Valuation & NTT Primitives Regime (`Ch 07` §7.2–§7.4)**:
     - Verified in `chapters/ch07-roots-of-unity-cyclotomic-czt.qmd` (§7.2 lines 210–310, §7.4 lines 520–675): Explicitly checks $2^k \mid (p-1)$ (`998244353 - 1 = 119 \times 2^{23}$, `Failure Mode #10` at $N > 2^{23}$) and develops 3-Prime NTT + Garner's mixed-radix CRT (`469762049`, `998244353`, `1004535809`) and Bluestein's CZT for arbitrary moduli.
  4. **Division-Free / Differential-Free Bypasses (`Ch 05` §5.2, `Ch 11` §11.2, `Ch 22` §22.4)**:
     - Verified in `Ch 05` (§5.2 lines 380–460: Bostan–Mori requires only $q_0 \not\equiv 0 \pmod p$ with zero divisions by $k!$), `Ch 11` (§11.2 lines 195–270: Raney's Lemma and the alternate derivative-free form of Lagrange Inversion $[x^n] F(x)^k = [u^n](1 - u \Phi'(u)/\Phi(u)) \Phi(u)^n$ avoid dividing by $n$ when $p \mid n$), and `Ch 22` (§22.4 lines 690–810: working over the local ring $\mathbb{F}_p[z]/(z^{c+1})$ to bypass division by zero in FWT/NTT evaluation values).
  5. **P-Recursive Indicial Zero-Divisors (`Ch 18` §18.4)**:
     - Verified in `chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd` (§18.4 lines 470–645): Develops indicial polynomial root analysis ($P_r(n) \equiv 0 \pmod p$ at $n = k p - c$) and the $\mathbb{Z}/p^e\mathbb{Z}[z]/(z^L)$ $p$-adic / symbolic $\varepsilon$-deformation lifting bypass (`Failure Mode #14`).

---

### 3.2 Audit of the 16 Canonical Failure Modes (`#1`–`#16`) & Numbering Collisions

- **Verification Matrix of All 16 Canonical Failure Modes**:

| FM # | Canonical Failure Mode (`CURRICULUM_ARCHITECTURE.md` §2.4) | Assigned Chapter & Section | Status in Chapter `.qmd` | Status in `STUDY_PLAN.qmd` (§4, L133–160) |
| :---: | :--- | :--- | :--- | :--- |
| **#1** | Valuation-Shift Precision Loss ($F(x) = x^v G(x) \bmod x^N$ requires $G \bmod x^{N-v}$) | `Ch 01` (§1.5, L480) & `Ch 02` (§2.4.4, L551) | **PASS** | **PASS** (L133) |
| **#2** | Non-Unit Constant Term in $\ln F$, $\exp F$, $F^\alpha$, $\sqrt{F}$ | `Ch 02` (§2.4, L367, L446, L494) | **PASS** | **PASS** (L134) |
| **#3** | Characteristic-$p$ Breakdown of $\int x^{p-1} dx$ & $\exp(x)$ at $N \ge p$ | `Ch 02` (§2.1, L256) | **PASS** | **OMITTED on L134** (only `#2` listed for Ch 02) |
| **#4** | Branch Selection & Quadratic Residue Existence for $\sqrt{F(x)}$ | `Ch 02` (§2.4.3, L494; §2.5, L648) | **PASS** | **OMITTED on L134** (only `#2` listed for Ch 02) |
| **#5** | Labeled (EGF) vs. Unlabeled (OGF) Universe Confusion | `Ch 03` (§3.4, L570) | **PASS** | **PASS** (L136) |
| **#6** | Burnside vs. Pólya Weight Independence Trap | `Ch 03` (§3.5, L705) | **PASS** | **PASS** (L136) |
| **#7** | Non-Coprime Modulus / Missing $q_0^{-1}$ in Bostan–Mori | `Ch 05` (§5.2, L445) | **PASS** | **PASS** (L139) |
| **#8** | Under-Sampled Berlekamp–Massey Prefix ($M < 2L$) | `Ch 05` (§5.4, L967) | **PASS** | **PASS** (L139) |
| **#9** | Factorial Division by Zero in Binomial Convolutions when $N \ge p$ | `Ch 06` (§6.1, L126) | **PASS** | **PASS** (L140) |
| **#10** | NTT Length Exceeding 2-Adic Valuation ($2^k \nmid (p-1)$) or Coefficient Overflow | `Ch 07` (§7.4, L540) | **PASS** | **PASS** (L141) |
| **#11** | Cyclic Wrap-Around Pollution in CDQ / Relaxed Convolution | `Ch 10` (§10.1, L213) | **PASS** | **PASS** (L144) |
| **#12** | Lagrange Inversion Without Valuation Shift ($\operatorname{val}(F) = 1$ Violation) | `Ch 11` (§11.3, L534) | **PASS** | **PASS** (L145) |
| **#13** | Unlabeled Graph / Tournament Cycle Index Symmetry Factor Omission | `Ch 13` (§13.5, L865) | **PASS** | **PASS** (L147) |
| **#14** | P-Recursive Leading Coefficient Zero-Divisor ($P_r(n) \equiv 0 \pmod p$) | `Ch 18` (§18.4, L490) | **PASS** | **PASS** (L153) |
| **#15** | Robinson's DAG Sign Error $(-1)^{k-1}$ vs. $(-1)^{|V|-k}$ **AND** Improper Rational Diagonal Pole at $z=0$ | `Ch 01` (L502), `Ch 13` (L394), `Ch 16` (L462), `CP-IV` (L423) | **3-WAY COLLISION** (see below) | Lists `#15` on `Ch 16` (L151), omits `#15` on `Ch 13` (L147) |
| **#16** | Prüfer $N=1$ Boundary Trap (`Ch 04`) & Catalan Negative Upper-Index Trap at $k=0$ (`Ch 11`) | `Ch 04` (§4.3, L483) & `Ch 11` (§11.3, L566) | **PASS** (paired as `#16a` / `#16b` in `CURRICULUM_ARCHITECTURE.md:L184`) | **PASS** (listed on both `Ch 04` L137 and `Ch 11` L145) |

- **Detailed Diagnostics & Drop-in Fixes for Failure Mode Numbering Collisions**:
  1. **Collision 1: `Failure Mode #15` is assigned to THREE different failure modes**:
     - **`Ch 01` (`chapters/ch01-ring-valuation-inversion-dc.qmd:L502`)**: Heading says `::: {.callout-warning title="Failure Mode #15: Degree-Bound Explosion & Missing Zero-Trim in D&C Product Trees"}`. Because `#1` is the canonical failure mode for `Ch 01` (and `#15` belongs to `Ch 13` / `Ch 16`), rename `Ch 01:L502` to `Failure Mode #1b: Degree-Bound Explosion & Missing Zero-Trim in D&C Product Trees` (pairing it with `Failure Mode #1` on line 480).
     - **`Ch 13` (`chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd:L394`) vs. `Ch 16` (`chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd:L462`) & `CP-IV` (`checkpoints/cp04-part4-graphs-ie-walks.qmd:L423, L889, L905, L989`)**:
       - Note that `CURRICULUM_ARCHITECTURE.md` itself created this split (`§2.4` line 183 assigns `#15` to `Ch 13` Robinson's DAG sign error, while `§3 Ch 16` line 803 assigns `#15` to `Ch 16` Improper Rational Diagonal pole at $z=0$).
       - Just as `Failure Mode #16` is cleanly shared between `Ch 04` and `Ch 11` in `STUDY_PLAN.qmd` and `CURRICULUM_ARCHITECTURE.md`, update `STUDY_PLAN.qmd:L147` (`Ch 13` row) and `L151` (`Ch 16` row) so both `#15a` (Robinson's DAG Sign Error $(-1)^{k-1}$ in `Ch 13`) and `#15b` (Hidden Pole at $z=0$ in Improper Rational Diagonals in `Ch 16`) are explicitly listed!
  2. **Collision 2: `Ch 08` (`chapters/ch08-symbolic-method-automata-transfer-matrix.qmd:L1248`) uses local `Failure Mode #1 Guard`**:
     - Line 1248 writes `- **Failure Mode #1 Guard (Antichain Reduction)**:` inside `Ch 08 [Adv-1]`, which collides with global `Failure Mode #1` (`Ch 01` Valuation-Shift Precision Loss).
     - **Drop-in Fix for `chapters/ch08-symbolic-method-automata-transfer-matrix.qmd:L1248`**: Change `- **Failure Mode #1 Guard (Antichain Reduction)**:` to `- **Antichain Reduction Guard (Substring Containment Trap)**:`.
  3. **Omission in `STUDY_PLAN.qmd:L134` (`Ch 02` row) and `L147` (`Ch 13` row)**:
     - **Location**: [STUDY_PLAN.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/STUDY_PLAN.qmd#L134) and [STUDY_PLAN.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/STUDY_PLAN.qmd#L147)
     - **Drop-in Fix for `STUDY_PLAN.qmd:L134`**:
       ```markdown
       | **Ch 02** | Calculus, Frobenius, Sparse ODEs & Newton Iteration | **Failure Modes #2, #3, #4**: Non-unit constant terms ($[x^0]F \neq 1$ in $\ln$, $[x^0]F \neq 0$ in $\exp$); Characteristic-$p$ breakdown of $\int x^{p-1}\,dx$ at $N \ge p$ (Frobenius $F(x)^p \equiv F(x^p) \pmod p$ & sparse ODE bypass); and branch selection / quadratic residue check for $\sqrt{F(x)}$. |
       ```
     - **Drop-in Fix for `STUDY_PLAN.qmd:L147`**:
       ```markdown
       | **Ch 13** | Graphical GFs: Eulerian, Bipartite, DAGs, SCCs & Tournaments | **Failure Modes #13 & #15a**: Unlabeled graph/tournament cycle index edge-orbit symmetry factor omission (polynomially scaling $2^{c(\sigma)}$); and Robinson's DAG inclusion–exclusion sign error ($-(-1)^k = (-1)^{k-1}$ on source layers vs. $(-1)^{|V|-k}$). |
       ```

---

## Checklist 4: Global Cross-Link, Anchor, Navigation & Quarto Formatting Audit

### 4.1 Internal `.qmd` Links & `#anchor` Targets Across the Entire Repository

- **Automated Verification Scope**: All 71 `.qmd` files in `/home/maomao90/Documents/IO/ICPC-math-notes` (including all 24 FPS chapters, 6 FPS checkpoints, 2 FPS capstones, `00-prerequisite-audit/chapter.qmd`, `STUDY_PLAN.qmd`, `NOTATION.qmd`, `SOURCES.qmd`, `index.qmd`, and all earlier volume chapters).
- **Broken `.qmd` File Links Found**: **1 total**
  - **Location**: [chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L263)
  - **Broken Target**: `../checkpoints/cp03-part3-combinatorial-classes-grammar.qmd`
  - **Valid Target**: `../checkpoints/cp03-part3-online-implicit-lif-graphs.qmd` (see §2.3 Item 2 above for the exact drop-in fix).
- **Broken `#anchor` Targets Found**: **0 total**
  - All explicit `{#...}` IDs (`#fps-bibliography` and `#fps-rosetta-stone` in `SOURCES.qmd`) and auto-generated Quarto heading slugs (`#complete-quarantined-template-verification-guide-r-01r-67` in `capstones/problem-archive-guide.qmd:L969`, referenced across `Ch 01`–`Ch 24`) resolve 100% cleanly.

### 4.2 `_quarto.yml` Navigation & File Existence Check

- **Location**: [_quarto.yml](file:///home/maomao90/Documents/IO/ICPC-math-notes/_quarto.yml#L1-L97)
- **Verification Result**: **100% PASS**
  - Every file listed in `_quarto.yml` exists on disk.
  - All 24 FPS chapters (`chapters/ch01-*.qmd`–`chapters/ch24-*.qmd`), all 6 Blind Checkpoints (`checkpoints/cp01-*.qmd`–`checkpoints/cp06-*.qmd`), both Capstones (`capstones/synthesis-reserve.qmd` and `capstones/problem-archive-guide.qmd`), `00-prerequisite-audit/chapter.qmd`, `STUDY_PLAN.qmd`, `NOTATION.qmd`, `SOURCES.qmd`, and `index.qmd` are registered in their exact curriculum order under Parts I–VI and Capstone & Reference.

### 4.3 Quarto Formatting & Render Safety Check

- **Automated Verification Scope**: Checked all FPS `.qmd` files (`chapters/ch01-*.qmd`–`chapters/ch24-*.qmd`, `checkpoints/cp01-*.qmd`–`checkpoints/cp06-*.qmd`, `capstones/*.qmd`, `00-prerequisite-audit/chapter.qmd`, `STUDY_PLAN.qmd`, `NOTATION.qmd`, `SOURCES.qmd`, `index.qmd`) for:
  1. Forbidden `\(` or `\[` math delimiters outside code blocks: **0 instances found (100% clean)**.
  2. Unescaped `|` inside `$...$` within Markdown table rows: **0 instances found in all FPS `.qmd` files (100% clean)**.
  3. Unclosed `<details>` or `</details>` mismatches: **0 instances found (100% clean)**.

---

## Prioritized Action Checklist for Final Textbook Polish

1. **[CRITICAL — `Ch 02` & `Ch 07` Quarantined Footnotes]**:
   - Apply the drop-in table replacement in [chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L1358-L1375) to fix the scrambled `R-06` / `R-09`–`R-19` mappings and remove `R-11` (which belongs to Ch 01).
   - Apply the drop-in replacement in [chapters/ch07-roots-of-unity-cyclotomic-czt.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd#L1632-L1638) to fix the misattributed `R-02, R-03, R-04, R-31` descriptions and remove `R-45` (which belongs to Ch 10).
2. **[CRITICAL — `Ch 18` Broken Link & Wrong `#pid` Citations]**:
   - In [chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L263), fix the broken link `../checkpoints/cp03-part3-combinatorial-classes-grammar.qmd` $\to$ `../checkpoints/cp03-part3-online-implicit-lif-graphs.qmd` and fix the `#038` reference.
   - In [chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L385), replace `QOJ #60 ... (#236)` with `AtCoder ABC 353 G ... (#013), UOJ 515 ... (#214), and QOJ 5424 ... (#227)`.
3. **[CRITICAL — `Ch 17` Problem Title Synchronization (`#204` & `#138`)]**:
   - In [chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L1030), fix `(Codeforces Gym 102586J)` $\to$ `(CF Gym 102538F: 3D Walk / Quarter Plane)`.
   - Synchronize the `#204` (`Ch 17 [Adv-2]`) title between `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd:L953` and `capstones/problem-archive-guide.qmd:L426, L837`.
4. **[MODERATE — `SOURCES.qmd` Bibliography Completeness]**:
   - Add the 18 omitted bibliography rows (7 in Category II, 2 in Category III + 4 secondary codes, 5 in Category IV, 4 in Category V) from `fps_research/CITATIONS.md` into `SOURCES.qmd` (`#fps-bibliography`), and align Row 67 of `#fps-rosetta-stone` (`\operatorname{mulT}`).
5. **[MODERATE — Failure Mode Numbering & `Ch 21` / `index.qmd` Minor Fixes]**:
   - Rename `Failure Mode #15` in `Ch 01:L502` to `Failure Mode #1b`, rename `Failure Mode #1 Guard` in `Ch 08:L1248` to `Antichain Reduction Guard`, and update `STUDY_PLAN.qmd:L134, L147` to include `Failure Modes #3, #4` (`Ch 02`) and `#15a` (`Ch 13`).
   - Fix `Revisited #11` $\to$ `Revisited #12` in `Ch 21:L436`, and update `(#001–#321)` $\to$ `(#001–#254 & R-01–R-67)` in `index.qmd:L177`.
