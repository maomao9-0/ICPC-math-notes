# Site Integration & Reference Pages Audit Report (`site_reference_critic_report.md`)

**Auditor**: `fps-textbook-critic` (Site Integration & Reference Pages Critic)  
**Target Files Audited (7 files)**:
1. [`_quarto.yml`](file:///home/maomao90/Documents/IO/ICPC-math-notes/_quarto.yml) (Lines 1–169)
2. [`index.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/index.qmd) (Lines 1–194)
3. [`00-prerequisite-audit/chapter.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/00-prerequisite-audit/chapter.qmd) (Lines 1–283)
4. [`STUDY_PLAN.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/STUDY_PLAN.qmd) (Lines 1–186)
5. [`NOTATION.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/NOTATION.qmd) (Lines 1–180)
6. [`SOURCES.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/SOURCES.qmd) (Lines 1–258)
7. [`CONTENT_AUDIT.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/CONTENT_AUDIT.md) (Lines 1–503)

**Cross-Referenced Master Specifications**:
- [`AGENTS.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/AGENTS.md)
- [`fps_research/CURRICULUM_ARCHITECTURE.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md)
- [`fps_research/CITATIONS.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md)
- [`capstones/synthesis-reserve.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/synthesis-reserve.qmd)
- [`capstones/problem-archive-guide.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd)

---

## Executive Scorecard Across the 4 Mandatory Audit Dimensions

| Audit Dimension | Target File(s) | Status | Summary of Findings |
| :--- | :--- | :-: | :--- |
| **1. `_quarto.yml` Navigation Completeness** | [`_quarto.yml`](file:///home/maomao90/Documents/IO/ICPC-math-notes/_quarto.yml#L1-L169) | **PASS (100%)** | All **61** `.qmd` files in the repository are registered in `_quarto.yml` (`missing = []`, `not_in_nav = []`), including all 24 FPS chapters (`chapters/ch01`–`ch24`), all 6 blind checkpoints (`checkpoints/cp01`–`cp06`), both capstones (`capstones/synthesis-reserve.qmd`, `capstones/problem-archive-guide.qmd`), all 24 baseline chapters/exercise sets, and all 5 reference pages. |
| **2. `00-prerequisite-audit/chapter.qmd` Integration** | [`00-prerequisite-audit/chapter.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/00-prerequisite-audit/chapter.qmd#L1-L283) | **ACTION REQUIRED** | Currently only routes readers at lines 278–282 to `01-modular-algebra`, `04-combinatorics`, `10-linear-algebra`, and `11-probability`. Has **zero** mention of or link to the 24-Chapter FPS & Generating Functions Track (`Ch 01`–`Ch 24`) or its entry library/algebraic contracts (`NTT` black-box, `mint`, formal sequence vs. analytic function, ring unit $f_0 \in K^\times$ vs. field division). Ready-to-apply drop-in section provided in **Section 2** below. |
| **3. Reference Pages & `CONTENT_AUDIT.md` Synchronization** | [`index.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/index.qmd), [`STUDY_PLAN.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/STUDY_PLAN.qmd), [`NOTATION.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/NOTATION.qmd), [`SOURCES.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/SOURCES.qmd), [`CONTENT_AUDIT.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/CONTENT_AUDIT.md) | **CRITICAL FIX IN `CONTENT_AUDIT.md` + 4 MINOR POLISHES** | `STUDY_PLAN.qmd` is 100% synchronized. **`CONTENT_AUDIT.md` (lines 401–503) is severely out of date**: it documents an obsolete **262-problem** draft (`192 + 20 + 50`, `0` checkpoint problems) and completely wrong Failure Mode numbers (`#1`–`#16` scrambled across chapters) instead of the canonical **321-problem architecture** (`254 = 192 + 48 + 14` accepted + `67` quarantined). Minor 1-line fixes also identified in `index.qmd` (line 176), `NOTATION.qmd` (lines 127–131 & 163), and `SOURCES.qmd` (line 149). Complete drop-in replacements provided in **Section 3** below. |
| **4. Strict Quarto Hygiene** | All 7 target files | **PASS (100%)** | Automated scan confirms **0** occurrences of `\(` or `\[`, **0** occurrences of `!$$` display-math factorial collisions, **0** unescaped `|` inside `$...$` in Markdown tables, **0** broken internal `.qmd` links, and **100%** valid `mermaid` `flowchart TD` syntax with quoted node labels. |

---

## 1. Audit Dimension 1: `_quarto.yml` Navigation Completeness

### 1.1 Automated Verification of All 61 `.qmd` Routes
Every `.qmd` path in [`_quarto.yml`](file:///home/maomao90/Documents/IO/ICPC-math-notes/_quarto.yml#L12-L132) was cross-checked against the filesystem (`chapters/`, `checkpoints/`, `capstones/`, `00-prerequisite-audit/` through `19-frontier-capstones/`, and root `.qmd` pages):

- **Start Here (Lines 14–19)**:
  - `index.qmd`, `00-prerequisite-audit/chapter.qmd`, `NOTATION.qmd`, `STUDY_PLAN.qmd` — **4/4 exist**.
- **Foundations, Combinatorics & Polynomials, Number Theory, Linear Algebra & Probability, Advanced Synthesis (Lines 21–70)**:
  - All 19 baseline `chapter.qmd` files (`01` through `19`) and all 5 companion `exercises.qmd` files (`01`, `03`, `06`, `09`, `10`) — **24/24 exist**.
- **FPS & Generating Functions Track — Parts I–VI & Capstones (Lines 72–128)**:
  - **Part I (`Ch 01`–`Ch 04` + `CP-I`, lines 75–80)**:
    - `chapters/ch01-ring-convolutions-newton-inv.qmd`
    - `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd`
    - `chapters/ch03-mset-partitions-euler-polya.qmd`
    - `chapters/ch04-egf-set-cyc-boxed-prufer.qmd`
    - `checkpoints/cp01-part1-foundations.qmd`
  - **Part II (`Ch 05`–`Ch 08` + `CP-II`, lines 84–89)**:
    - `chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd`
    - `chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd`
    - `chapters/ch07-roots-of-unity-cyclotomic-czt.qmd`
    - `chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd`
    - `checkpoints/cp02-part2-rational-transforms-ie.qmd`
  - **Part III (`Ch 09`–`Ch 13` + `CP-III`, lines 93–99)**:
    - `chapters/ch09-cdq-fft-online-relaxed-convolution.qmd`
    - `chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd`
    - `chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd`
    - `chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`
    - `chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd`
    - `checkpoints/cp03-part3-online-implicit-lif-graphs.qmd`
  - **Part IV (`Ch 14`–`Ch 17` + `CP-IV`, lines 103–108)**:
    - `chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd`
    - `chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`
    - `chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`
    - `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`
    - `checkpoints/cp04-part4-pgf-walks-multivariate.qmd`
  - **Part V (`Ch 18`–`Ch 21` + `CP-V`, lines 112–117)**:
    - `chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd`
    - `chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd`
    - `chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd`
    - `chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd`
    - `checkpoints/cp05-part5-dfinite-transposition-composition.qmd`
  - **Part VI & Capstones (`Ch 22`–`Ch 24` + `CP-VI` + 2 Capstones, lines 121–128)**:
    - `chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd`
    - `chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd`
    - `chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd`
    - `checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd`
    - `capstones/synthesis-reserve.qmd`
    - `capstones/problem-archive-guide.qmd`
- **Reference (Lines 130–132)**:
  - `SOURCES.qmd` — **1/1 exists**.

**Result**: `61/61` files mapped bijectively (`0` broken links, `0` orphaned `.qmd` files).

---

## 2. Audit Dimension 2: `00-prerequisite-audit/chapter.qmd` Integration

### 2.1 Issue Found
- **Location**: [`00-prerequisite-audit/chapter.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/00-prerequisite-audit/chapter.qmd#L261-L283)
- **Severity**: **Medium-High (Missing Curriculum Bridge & Entry Contract)**
- **Description**:
  - `00-prerequisite-audit/chapter.qmd` serves as the universal entry gate from `index.qmd` (linked at `index.qmd` line 11 and `STUDY_PLAN.qmd` line 19).
  - However, lines 278–282 (`Where to Go Next`) only route the reader to `01-modular-algebra`, `04-combinatorics`, `10-linear-algebra`, and `11-probability`.
  - There is **no mention** of the **24-Chapter Formal Power Series & Generating Functions Track (`Ch 01`–`Ch 24`)**, nor does it state the **Black-Box Library & Algebraic Entry Contract** required by [`AGENTS.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/AGENTS.md#L76-L86) and [`CURRICULUM_ARCHITECTURE.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md#L10-L18) when jumping into [`chapters/ch01-ring-convolutions-newton-inv.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd).

### 2.2 Ready-to-Apply Drop-In Fix for `00-prerequisite-audit/chapter.qmd` (Lines 276–283)

Replace lines 276–283 of [`00-prerequisite-audit/chapter.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/00-prerequisite-audit/chapter.qmd#L276-L283) with the following expanded routing and entry-contract section:

```markdown
## Where to Go Next

- If modular inverse or CRT felt shaky, start cleanly at [Chapter 1: Modular Arithmetic as a Ring and a Field](../01-modular-algebra/chapter.qmd).
- If the EGF and Vandermonde checks felt shaky, keep [Chapter 4: Combinatorial Enumeration](../04-combinatorics/chapter.qmd) and [Chapter 6: Polynomials and Convolution](../06-polynomials/chapter.qmd) slow and deliberate.
- If the rank and expectation checks felt shaky, pay extra attention when entering [Chapter 10: Linear Algebra over Finite Fields](../10-linear-algebra/chapter.qmd) and [Chapter 11: Discrete Probability and Expectation](../11-probability/chapter.qmd).
- If all four areas felt comfortable, you are ready to enter either the **Foundations Track** at [Chapter 1](../01-modular-algebra/chapter.qmd) or the **24-Chapter Formal Power Series & Generating Functions Track** at [FPS Chapter 01: The Ring $K[[x]]$, Valuation, Cauchy Convolutions & Newton Inversion](../chapters/ch01-ring-convolutions-newton-inv.qmd).

::: {.callout-important}
## Entry Contract for the 24-Chapter FPS & Generating Functions Track (`Ch 01`–`Ch 24`)

The 24-chapter FPS & Generating Functions curriculum ([`Ch 01`](../chapters/ch01-ring-convolutions-newton-inv.qmd)–[`Ch 24`](../chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd)) is a self-contained algebraic engine built on four explicit entry assumptions:

1. **Formal Power Series vs. Analytic Functions**: An element $F(x) = \sum_{n \ge 0} f_n x^n \in K[[x]]$ is an infinite sequence $(f_0, f_1, f_2, \dots)$ over a commutative ring $K$, never an analytic function of a complex variable. Infinite sums $\sum_{k \ge 0} G_k(x)$ are governed purely by the **$x$-adic valuation** $\operatorname{val}(G_k) \to \infty$ (finitely many non-zero contributions to $[x^n]$ for each fixed $n$), not radius of convergence.
2. **Ring Units vs. Field Division**: Division in $K[[x]]$ is checked locally before every step: $F(x)$ is invertible in $K[[x]]$ if and only if its constant term is a unit $[x^0]F(x) = f_0 \in K^\times$. Operators that integrate $\int x^{n-1}\,dx = x^n / n$ (`ln`, `exp`, `pow`, classical Lagrange inversion) additionally require $\operatorname{char}(K) = 0$ or prime $p > N$.
3. **Black-Box `mint` & `NTT` Primitive Contract**: In accordance with editorial policy, the FPS chapters never dump boilerplate modular integer (`mint`), factorial sieve, or raw Cooley–Tukey Butterfly `NTT` templates. You are assumed to have a working black-box polynomial multiplication primitive `mul(A, B)` running in $O(N \log N)$ over NTT-friendly primes such as $p = 998244353 = 119 \cdot 2^{23} + 1$ (constructed from scratch in [Baseline Chapter 6: Polynomials and Convolution](../06-polynomials/chapter.qmd)).
4. **Notation & Study Roadmap**: Keep the [Notation & Operator Cheat Sheet](../NOTATION.qmd) open for the 16 Canonical Failure Modes (`#1`–`#16`) and operator contracts, and use the [Study Plan & Diagnostic Guide](../STUDY_PLAN.qmd) to navigate the 24 chapters, 6 Two-Stage Blind Checkpoints ([`CP-I`](../checkpoints/cp01-part1-foundations.qmd)–[`CP-VI`](../checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd)), and [Multi-Perspective Synthesis Reserve](../capstones/synthesis-reserve.qmd).
:::
```

---

## 3. Audit Dimension 3: Reference Pages (`index.qmd`, `STUDY_PLAN.qmd`, `NOTATION.qmd`, `SOURCES.qmd`) & `CONTENT_AUDIT.md`

### 3.1 CRITICAL ISSUE: `CONTENT_AUDIT.md` Lines 401–503 Reflect an Obsolete 262-Problem Draft
- **Location**: [`CONTENT_AUDIT.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/CONTENT_AUDIT.md#L401-L503)
- **Severity**: **Critical (Contradicts Canonical 321-Problem Architecture & Failure Mode Registry)**
- **Detailed Line-by-Line Discrepancies**:
  1. **Stale Problem Pool Accounting (Lines 411–414, 421–452, 499–502)**:
     - `CONTENT_AUDIT.md` line 414 & lines 451–452 claim a **`262`-problem curation** (`192` chapter problems `#001`–`#192` + `20` Synthesis Reserve `#193`–`#212` + `50` Categorized Archive `#213`–`#262`, with `0` problems in `CP-I`–`CP-VI`).
     - In reality, [`CURRICULUM_ARCHITECTURE.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md#L33-L41), [`index.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/index.qmd#L25-L34), [`STUDY_PLAN.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/STUDY_PLAN.qmd#L168-L185), [`capstones/synthesis-reserve.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/synthesis-reserve.qmd#L8-L16), and [`capstones/problem-archive-guide.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd#L6-L29) implement the **321-Problem Bijective Architecture**:
       - **`254` Accepted Non-Template Problems (`#001`–`#254`)** = **`192`** Chapter Ladder Problems (`24 × 8`) + **`48`** Part-End Blind Checkpoint Problems (`6 × 8`, `CP-I`–`CP-VI`) + **`14`** Multi-Perspective Synthesis Reserve Problems (`Syn-01`–`Syn-14`),
       - Plus **`67` Quarantined Bare-Template Unit Tests (`R-01`–`R-67`)**, and
       - **`12` Revisited Dual-Perspective Flagship Problems**.
  2. **Scrambled Failure Mode Numbers `#1`–`#16` (Lines 421–450)**:
     - The "Failure Modes Audited" column in `CONTENT_AUDIT.md` lines 421–450 assigns completely wrong Failure Mode numbers compared to [`CURRICULUM_ARCHITECTURE.md` §2.4](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md#L201-L219), [`STUDY_PLAN.qmd` lines 131–160](file:///home/maomao90/Documents/IO/ICPC-math-notes/STUDY_PLAN.qmd#L131-L160), and [`NOTATION.qmd` lines 155–172](file:///home/maomao90/Documents/IO/ICPC-math-notes/NOTATION.qmd#L155-L172):
       - E.g., `CONTENT_AUDIT.md` assigns `#1, #2, #4` to `Ch 01` and `#3, #5, #6` to `Ch 02`, whereas canonical §2.4 assigns **`#1`** to `Ch 01.4`, **`#2, #3, #4`** to `Ch 02.2–2.3`, **`#5`** to `Ch 11.2`, **`#6`** to `Ch 21.4`, **`#7`** to `Ch 17.3`, **`#8`** to `Ch 18.4`, **`#9`** to `Ch 23.2`, **`#10`** to `Ch 22.3`, **`#11, #12`** to `Ch 07.3–7.4`, **`#13`** to `Ch 09.2`, **`#14`** to `Ch 06.3`, **`#15`** to `Ch 16.4`, and **`#16`** to `Ch 04.4 & Ch 11.3`.
  3. **Inaccurate Chapter Descriptions in Detailed Inventory (Lines 457–497)**:
     - Line 457 (`ch01`) claims `sqrt` and quadratic residues are in `Ch 01`, whereas `sqrt` is in `Ch 02.3`.
     - Line 475 (`ch13`) omits Kirchhoff's Matrix-Tree Theorem, BEST Theorem, Wright's sparse connected-graph kernel decomposition, symbolic determinants over $\mathbb{F}_p[x]/(x^{k+1})$, and $O(V^3)$ Hessenberg reduction.
     - Line 493 (`ch22`) claims `Ch 22` uses $p$-adic lifting $(c, \alpha) \equiv c p^\alpha \pmod{p^K}$, whereas `Ch 22.3` uses the **Zero-Divisor Monoid $(a, c) \equiv a \cdot 0^c$ over $\mathbb{F}_p$** (and $p$-adic valuation lifting is `Ch 18.4`, Failure Mode `#8`).

#### Ready-to-Apply Drop-In Replacement for `CONTENT_AUDIT.md` (Lines 401–503)

Replace lines 401–503 of [`CONTENT_AUDIT.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/CONTENT_AUDIT.md#L401-L503) with the following canonical, fully verified inventory:

```markdown
---

## 24-Chapter Formal Power Series (FPS) & Generating Functions Track Audit (`Ch 01`–`Ch 24`, `CP-I`–`CP-VI`, Capstones)

In addition to the 19-chapter core competitive programming mathematics sequence audited above, the repository includes the complete **32-page Formal Power Series & Generating Functions Textbook Track** (`24` Chapters + `6` Two-Stage Blind Checkpoints + `2` Capstone Compendia), governed by [`fps_research/CURRICULUM_ARCHITECTURE.md`](fps_research/CURRICULUM_ARCHITECTURE.md) and [`AGENTS.md`](AGENTS.md).

### Architectural & Editorial Invariants Verified Across All 32 FPS Pages

1. **Zero Boilerplate Template Dumps**: Raw `NTT`, `mint`, and linear sieve boilerplate are strictly omitted in favor of algebraic operator derivations and explicit **5-Part Algorithm Contracts** (`Input`, `Output`, `Algebraic / Ring Hypotheses`, `Complexity & NTT Count`, and `Failure Modes`).
2. **Local Algebraic Hypotheses Beside Every Division**: Every division checks unit invertibility ($[x^0]F \in K^\times$), characteristic bounds ($\operatorname{char}(K) = 0$ or $p > N$ for $\int x^{n-1}\,dx = x^n/n$), and $x$-adic valuation shifts ($\operatorname{val}(F) = v$).
3. **All 16 Canonical Failure Modes (`#1`–`#16`) & Characteristic-$p$ Bypasses Covered**: Every failure mode and small-prime $p \le N$ bypass in `CURRICULUM_ARCHITECTURE.md` §2.3–§2.4 is proved and illustrated in its assigned chapter.
4. **321-Problem Bijective Curation (`254 Accepted + 67 Quarantined`, Zero Duplicates, Zero Forward-Reference Violations)**:
   - **`192` Chapter Ladder Problems (`24 Chapters × 8 Problems`)**: Every chapter concludes with a 4-tier progressive ladder (`SS-1`, `SS-2`, `Int-1`, `Int-2`, `Adv-1`, `Adv-2`, `Mas-1`, `Mas-2`) with inline statements, exact constraints, 3 progressive hints, and complete derivations using only techniques from Chapters $1 \dots k$.
   - **`48` Two-Stage Blind Checkpoint Problems (`6 Checkpoints × 8 Problems`, `CP-I`–`CP-VI`)**: Placed at the end of Parts I–VI with a 100% spoiler-free Stage 1 arena and collapsible Stage 2 diagnostic routing and full solutions.
   - **`14` Grandmaster Multi-Perspective Synthesis Reserve Problems (`Syn-01`–`Syn-14`)** + **`12` Revisited Dual-Perspective Flagship Bridges** in [`capstones/synthesis-reserve.qmd`](capstones/synthesis-reserve.qmd).
   - **`67` Quarantined Bare-Template Unit Tests (`R-01`–`R-67`)** + **Complete 254-Problem Bijective Lookup Index (`#001`–`#254`)** in [`capstones/problem-archive-guide.qmd`](capstones/problem-archive-guide.qmd).

### Master Status Table: 24 FPS Chapters, 6 Blind Checkpoints & 2 Capstones

| Unit | File Path | Core Mathematical & Algorithmic Scope | Failure Modes (`#1`–`#16`) & Char-$p$ Bypasses | Curated Problems | Status |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Ch 01** | `chapters/ch01-ring-convolutions-newton-inv.qmd` | Ring $K[[x]]$, $x$-adic valuation, Cauchy/reverse convolution, Min-Heap D&C product trees, Newton `inv` ($10/3\,\mathsf{E}(n)$), $O(NK)$ `sparse_div` | `#1` (NTT Aliasing) | `8` (`#019, #043, #004, #077, #049, #097, #066, #107`) | Complete |
| **Ch 02** | `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd` | Formal $D_x, \int$, `ln`, Newton `exp`, `sqrt` (Cipolla/Tonelli–Shanks), `pow` valuation shift, $O(NK)$ sparse ODEs, Newton–Girard | `#2` (`ln/exp` Valuation), `#3` (Zero-Divisor `pow`), `#4` (`sqrt` Parity/Residue); Frobenius $F(x)^p \equiv F(x^p)$ | `8` (`#238, #165, #101, #222, #157, #084, #030, #091`) | Complete |
| **Ch 03** | `chapters/ch03-mset-partitions-euler-polya.qmd` | Unlabeled Symbolic Method ($\operatorname{SEQ}, \operatorname{MSET}, \operatorname{PSET}$), harmonic $O(N \log N)$ Euler transform & Mobius inverse, Ferrers/Pentagonal $O(N\sqrt{N})$, Burnside/Polya $Z_G$ | Char-$p$ $O(N\sqrt{N})$ Durfee / Pentagonal bypass for `MSET` when $p \le N$ | `8` (`#001, #188, #153, #009, #223, #221, #150, #159`) | Complete |
| **Ch 04** | `chapters/ch04-egf-set-cyc-boxed-prufer.qmd` | Labeled EGFs, binomial convolution, $\operatorname{SET}/\exp$, $\operatorname{CYC}/\ln$, connected $\leftrightarrow$ all, Greene–Wilf Boxed Product $\mathcal{A}^{\square} \star \mathcal{B}$, Prufer sequences | `#16` (Prufer $N=1$ Boundary Trap); Boxed-Product $G' = C'G \iff C' = G'G^{-1}$ Char-$p$ bypass | `8` (`#002, #007, #161, #008, #083, #011, #041, #174`) | Complete |
| **CP-I** | `checkpoints/cp01-part1-foundations.qmd` | Part I Two-Stage Blind Diagnostic: OGF vs. EGF, $\operatorname{MSET}$ vs. $\operatorname{SET}$, sparse ODE vs. dense `ln/exp` | Audits `#1`–`#4`, `#16` | `8` (`CP-I.1`–`CP-I.8`: `#078, #144, #246, #032, #079, #250, #037, #024`) | Complete |
| **Ch 05** | `chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd` | Rational series $P(x)/Q(x)$, reversal `divmod`, Bostan–Mori parity splitting + NTT half-spectrum trick, partial fractions, Berlekamp–Massey LFSR | Frobenius Bostan–Mori $[x^N]P(x)Q(x)^{p-1}/Q(x^p)$ over small $\operatorname{char}(K) = p$ | `8` (`#104, #034, #187, #069, #040, #081, #177, #073`) | Complete |
| **Ch 06** | `chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd` | Index alignment, Snake Oil, Egorychev extraction, Taylor shift $F(x+c)$, generalized $\alpha$-Euler transform, Stirling $S_1/S_2$, Eulerian, FFP, $O(d)$ Lagrange | `#14` (Negative-Integer $\alpha = -d$ Pole Trap in $(1-cx)^{-\alpha}F(ax/(1-cx))$) | `8` (`#005, #055, #193, #080, #094, #096, #098, #109`) | Complete |
| **Ch 07** | `chapters/ch07-roots-of-unity-cyclotomic-czt.qmd` | DFT Vandermonde duality, 3-Prime Garner `MTT`, Bluestein Chirp-$Z$ Transform (`czt`), Root-of-Unity Filters (`单位根反演`), discrete-log cyclic convolution | `#11` (Cyclotomic Quotient Ring $\mathbb{F}_p[\omega]/(\Phi_m(\omega))$ when $m \nmid (p-1)$), `#12` (Bluestein $\binom{i+j}{2}$ & $c=0$) | `8` (`#224, #248, #178, #143, #147, #012, #092, #168`) | Complete |
| **Ch 08** | `chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd` | Binomial inversion $G(x, y-1)$, Run-Length IE $F = W/(1+W)$, Smirnov words, `ez_lcw` $O(n \log^2 n)$ sparsity, rook/path IE, 4-regime Goulden–Jackson | Order-of-operations trap: OGF transfer $W/(1+W)$ before dividing $[x^s]$ by $s!$ | `8` (`#018, #241, #155, #089, #067, #139, #052, #137`) | Complete |
| **CP-II** | `checkpoints/cp02-part2-rational-transforms-ie.qmd` | Part II Two-Stage Blind Diagnostic: Bostan–Mori vs. Taylor Shift vs. CZT/Roots of Unity vs. Cluster IE | Audits `#11`, `#12`, `#14` | `8` (`CP-II.1`–`CP-II.8`: `#085, #152, #251, #252, #100, #029, #162, #141`) | Complete |
| **Ch 09** | `chapters/ch09-cdq-fft-online-relaxed-convolution.qmd` | Causal recurrences, semi-online CDQ NTT (`cdq(l,r)`), full-online `RelaxedConvolution` (`lowbit(q+1)`), online `exp` & harmonic Pólya updates | `#13` (CDQ Self-Convolution Asymmetry Bug: factor $2$ at $l > 0$) | `8` (`#060, #021, #086, #023, #056, #225, #206, #075`) | Complete |
| **Ch 10** | `chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd` | Implicit Functional Equations $A(x,F)=0$, Fréchet derivative, $d\times d$ Jacobian Newton, integrating-factor ODE Newton, Pólya $T(x^k)$ trick, Otter's theorem | Jacobian singularity & Pólya $k \ge 2$ constant-in-step-$s$ optimization | `8` (`#186, #226, #244, #013, #179, #126, #191, #192`) | Complete |
| **Ch 11** | `chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd` | Laurent field $K((x))$, formal residue $\operatorname{Res}_{x=0}$, change-of-variables, 6 Canonical Forms of LIF, `ABC 345 G` trick, Raney/Lambert/Catalan | `#5` (Char-$p$ Division by $n$ in LIF $\to$ Form 2/3 & Base-$p$ Frobenius Decimation), `#16` (Catalan $k=0$ Trap) | `8` (`#003, #200, #196, #201, #010, #229, #114, #203`) | Complete |
| **Ch 12** | `chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd` | Pointing $\Theta = xD_x$, Cayley trees $T = xe^T$, Husimi cactus EGF, Tutte's Block-Cut equation $\ln(R/x) = B'(R)$, 2-ECC ($G = x\exp(B'(Ge^{-G^2/2}))$) | Single-$N$ LIF (`Ch 12.3`) vs. all-$n$ composition/inversion (`Ch 21.3`) | `8` (`#176, #245, #146, #227, #190, #016, #183, #184`) | Complete |
| **Ch 13** | `chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd` | Graphical GF $\mathcal{G}(A)$, Bluestein edge convolution, Wright's sparse connected graphs, bipartite/Eulerian/DAG/SCCs, Matrix-Tree, BEST, $O(V^3)$ Hessenberg | `#12` (Bluestein $\binom{i+j}{2}$ for $2^{-\binom{n}{2}}$); graphic Robinson–Foulds $(-1)^n$ sign | `8` (`#164, #103, #093, #189, #199, #053, #122, #212`) | Complete |
| **CP-III** | `checkpoints/cp03-part3-online-implicit-lif-graphs.qmd` | Part III Two-Stage Blind Diagnostic: CDQ/Relaxed vs. Implicit Newton vs. LIF vs. Cactus/Block-Cut/DAG EGFs | Audits `#5`, `#13`, `#16` | `8` (`CP-III.1`–`CP-III.8`: `#090, #131, #133, #160, #119, #035, #205, #163`) | Complete |
| **Ch 14** | `chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd` | PGF factorial moments at $x = 1+t$, renewal $F(x)(1-x) + (1-p x^L)G(x) = 1$, KMP border OGF, Poissonization, $k$-th Min–Max IE, Martingales | Clearing removable $(1-x)^k$ poles before substituting $x=1$ (`#169`, `#209`) | `8` (`#115, #026, #156, #071, #148, #209, #039, #113`) | Complete |
| **Ch 15** | `chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd` | Reflection principle, Kelvin's alternating images across two walls, Chebyshev $U_H(x/2)$ transfer, 1D Kernel Method & Puiseux small-branch elimination | Selecting strictly the small branches $\operatorname{val}_t(u_i(t)) > 0$ inside the kernel | `8` (`#105, #070, #220, #140, #128, #134, #076, #210`) | Complete |
| **Ch 16** | `chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd` | 5-Ring Bivariate Hierarchy, Kronecker packing $\chi$, 3-regime 2D Bostan–Mori, diagonal $[x^n y^n]$ of rational series, Furstenberg's residue theorem | `#15` (Kronecker Packing Wrap-Around Collision $\to$ pad $B_k \ge \deg_{x_k} F + \deg_{x_k} G + 1$) | `8` (`#048, #129, #025, #232, #237, #074, #240, #214`) | Complete |
| **Ch 17** | `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd` | 2D Quarter-Plane walks, biharmonic group $\mathcal{G}$, Obstinate Kernel Method, Multivariate Good–Lagrange $\det(I - J_G)$, MacMahon's Master Theorem | `#7` (2D Obstinate Kernel Over-Subtraction of $[x^0 y^0]F$ & Newton–Girard Sign Trap) | `8` (`#154, #044, #228, #219, #015, #204, #138, #234`) | Complete |
| **CP-IV** | `checkpoints/cp04-part4-pgf-walks-multivariate.qmd` | Part IV Two-Stage Blind Diagnostic: PGF Stopping/Martingales vs. 1D Kernel vs. 2D Bostan–Mori/Furstenberg vs. Good–Lagrange | Audits `#7`, `#15` | `8` (`CP-IV.1`–`CP-IV.8`: `#158, #169, #099, #116, #194, #058, #243, #082`) | Complete |
| **Ch 18** | `chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd` | Weyl algebra $K[x]\langle D_x \rangle$, Euler operator $\vartheta = xD_x$, D-finite closure, 7 ODE Archetypes $\to$ $O(N)$ P-recursive, indicial roots & $p$-adic lifting | `#8` (P-Recursive Singularity $P_0(n_0) \equiv 0 \pmod p$ $\to$ Indicial / $p$-Adic Valuation Lifting) | `8` (`#151, #064, #022, #239, #125, #088, #211, #230`) | Complete |
| **Ch 19** | `chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd` | Coupled nonlinear ODEs (`sec/tan`), `EI` Differential-Residue Method for $\sum_k f_k [x^{n-k}]A(x)B(x)^k$, WZ pairs, `EI` Truncated Taylor Shift (`#118`, `#213`) | Truncating $(x+c)^n \bmod x^m$ so the differentiated ODE RHS stays $O(1)$-sparse! | `8` (`#242, #120, #095, #195, #028, #118, #072, #213`) | Complete |
| **Ch 20** | `chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd` | Tellegen's Principle, Middle Product `mulT`, subproduct trees, $O(N \log^2 N)$ multipoint evaluation & interpolation, sampling shift, $O(\sqrt{N}\log N)$ factorial | Explicit `mulT(A, B, out_len)` indexing alignment $c_j = \sum_i a_i b_{i+j}$ | `8` (`#050, #197, #127, #167, #208, #202, #181, #217`) | Complete |
| **Ch 21** | `chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd` | Power Projection via 2D Bostan–Mori + Nachia half-swap, Kinoshita–Li `compose` via Tellegen transposition, Dual-Route `revert`, $k$-th functional root | `#6` (Compositional Inverse Valuation/Derivative Trap: $f_0 = 0, f_1 \in K^\times$) | `8` (`#036, #045, #047, #059, #065, #218, #235, #017`) | Complete |
| **CP-V** | `checkpoints/cp05-part5-dfinite-transposition-composition.qmd` | Part V Two-Stage Blind Diagnostic: D-Finite $O(N)$ ODE vs. `EI` Truncated Taylor vs. Tellegen `mulT` vs. Kinoshita–Li `compose`/`revert` | Audits `#6`, `#8` | `8` (`CP-V.1`–`CP-V.8`: `#236, #108, #130, #135, #185, #215, #061, #068`) | Complete |
| **Ch 22** | `chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd` | $O(NK)$ bounded tree knapsack, HLD Spine D&C + weighted balanced midpoint, Static Top Trees (`Compress`/`Rake`), Zero-Divisor Monoid $(a,c) = a\cdot 0^c$ | `#10` (Dynamic Tree DP / FWT Division-by-Zero Trap $\to$ Zero-Divisor Monoid $(a, c)$) | `8` (`#031, #124, #046, #198, #149, #136, #166, #145`) | Complete |
| **Ch 23** | `chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd` | $q$-Pochhammer $(a;q)_n$, Gaussian $\begin{bmatrix}n\\k\end{bmatrix}_q$, RREF subspaces, $q$-Binomial/Cauchy/Pentagonal/Durfee, $q$-D-finite ODEs, $q$-Lucas, MacWilliams | `#9` (Root-of-Unity Pole $(q;q)_n \equiv 0 \pmod p$ when $\operatorname{ord}_p(q) \le n$ $\to$ $q$-Lucas) | `8` (`#123, #033, #233, #057, #062, #132, #063, #111`) | Complete |
| **Ch 24** | `chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd` | Bitwise FWT (OR/AND/XOR), $O(n^2 2^n)$ Subset Convolution & Set Power Series $\mathcal{R}_n$ (`inv/ln/exp`, Pointed SPS), Dirichlet GF $\mathcal{D}_f(s)$ (`inv/ln/exp` via $\Omega(n)$) | XOR-FWT $2^{-n}$ division & Pointed SPS $\Theta_v$ bypassing divisions by $1 \dots n$ in $\operatorname{char} p$ | `8` (`#216, #020, #027, #042, #110, #207, #231, #038`) | Complete |
| **CP-VI** | `checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd` | Part VI Two-Stage Blind Diagnostic: HLD/Top-Tree FPS vs. $q$-Series vs. FWT/SPS $\mathcal{R}_n$ vs. Dirichlet GF $\mathcal{D}_f(s)$ | Audits `#9`, `#10` | `8` (`CP-VI.1`–`CP-VI.8`: `#102, #121, #117, #170, #054, #254, #175, #180`) | Complete |
| **Cap 1** | `capstones/synthesis-reserve.qmd` | Grandmaster Multi-Perspective Synthesis Reserve (`Syn-01`–`Syn-14` Dual-Derivation Writeups) & Master Index of the `12` Revisited Dual-Perspective Flagship Problems | Cross-Part comparative trade-offs (`Ch 01`–`Ch 24`) | `14` Disjoint Reserve (`Syn-01`–`Syn-14`) + `12` Revisited Bridges | Complete |
| **Cap 2** | `capstones/problem-archive-guide.qmd` | Master Problem Archive, 24-Chapter Curriculum Index, `67` Quarantined Template Unit Tests (`R-01`–`R-67`), & Complete `254`-Problem Bijective Verification Table | Enforces strict template quarantine (`R-01`–`R-67`) | Full `321`-Problem Index (`254` Accepted + `67` Quarantined) | Complete |
```

---

### 3.2 Minor Polish Items in `index.qmd`, `NOTATION.qmd`, and `SOURCES.qmd`

#### Item 3.2.1: `index.qmd` Line 176 (`28-entry` vs `12-entry` Revisited Dual-Perspective Cross-Index)
- **Location**: [`index.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/index.qmd#L176)
- **Severity**: **Low (Count Typo in Description)**
- **Description**: Line 176 states `"and the complete 28-entry Revisited Dual-Perspective Cross-Index"`, whereas [`CURRICULUM_ARCHITECTURE.md` §5.2](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md#L1415-L1433) and [`capstones/synthesis-reserve.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/synthesis-reserve.qmd#L3-L16) have **12** Revisited Dual-Perspective Flagship Problems (alongside the **14** Synthesis Reserve problems `Syn-01`–`Syn-14`).
- **Ready-to-Apply Drop-In Fix (`index.qmd` Line 176)**:
  ```markdown
  | **Capstone 1** | [Multi-Perspective Synthesis Reserve](capstones/synthesis-reserve.qmd) | Full dual-perspective derivations of the **14 Grandmaster Synthesis Reserve problems (`Syn-01`–`Syn-14`)** and the complete **12-entry Revisited Dual-Perspective Cross-Index**. |
  ```

#### Item 3.2.2: `NOTATION.qmd` Lines 127–131 & Line 163 (5-Ring Hierarchy Numbering & Failure Mode `#7` Sign Convention)
- **Location**: [`NOTATION.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/NOTATION.qmd#L127-L131) and [`NOTATION.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/NOTATION.qmd#L163)
- **Severity**: **Low (Clarity & Sign Convention Polish)**
- **Description**:
  1. Lines 127–131 title the list **"The 5-Ring Bivariate Hierarchy (`Ch 15`–`Ch 17`)"**, but use a 4-item numbered list (`1.`–`4.`) where item `4.` combines two rings (`K((x))[[y]]` and `K[[t]]((y))`). Splitting `4.` and `5.` makes the 5-ring count visually immediate.
  2. Line 163 (`Failure Mode #7`) writes `use $P(t) = -t E'(-t)/E(-t)$` without stating whether $E(t) = \sum_{k \ge 0} e_k t^k$ (unsigned) or $\sum_{k \ge 0} (-1)^k e_k t^k$ (signed), whereas `CURRICULUM_ARCHITECTURE.md` line 209 writes `use $P(t) = -t \frac{d}{dt}\ln E(-t)$ where $E(t) = \sum_{k \ge 0} e_k t^k$ = 1 + e_1 t + e_2 t^2 + \dots$`. Explicitly stating $E(t) = \sum_{k \ge 0} e_k t^k$ eliminates any sign ambiguity.
- **Ready-to-Apply Drop-In Fix (`NOTATION.qmd` Lines 127–131)**:
  ```markdown
  ### The 5-Ring Bivariate Hierarchy (`Ch 15`–`Ch 17`)
  1. **$K[x, y]$**: Bivariate polynomials (finitely many non-zero terms).
  2. **$K[y][[x]]$**: Power series in $x$ with **polynomial** coefficients in $y$ ($\deg_y f_n(y) < \infty$ for each $n$; natural home of lattice walks where $x = t$ marks time steps).
  3. **$K[[x, y]]$**: Formal bivariate power series (supports arbitrary $(n, m) \in \mathbb{Z}_{\ge 0}^2$).
  4. **$K((x))[[y]]$**: Formal power series in $y$ over the Laurent field $K((x))$ (bounded below in $x$ for each fixed $y^m$).
  5. **$K[[t]]((y))$**: Formal Laurent series in $y$ over $K[[t]]$ (the **Furstenberg Diagonal Ring**, where $x y = t \implies x = t y^{-1}$ converts $[x^n y^n]F(x, y)$ into the 1D residue $[t^n]\operatorname{Res}_{y=0}\big(y^{-1}F(t y^{-1}, y)\big)$!).
  ```
- **Ready-to-Apply Drop-In Fix (`NOTATION.qmd` Line 163)**:
  ```markdown
  | **`#7`** | **2D Obstinate Kernel Over-Subtraction & Newton–Girard Sign Trap** | [`Ch 17.3`](chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd) | Subtracting $F(x,0)+F(0,y)$ double-counts $F(0,0)$ ($\to +F(0,0)$); for $E(t) = \sum_{k \ge 0} e_k t^k$, use $P(t) = -t E'(-t)/E(-t)$. |
  ```

#### Item 3.2.3: `SOURCES.qmd` Line 149 (Missing Space After `&`)
- **Location**: [`SOURCES.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/SOURCES.qmd#L149)
- **Severity**: **Trivial Typo**
- **Description**: Line 149 reads `14. **Alin Bostan &Ryuhei Mori (2020/2021)**` (missing space between `&` and `Ryuhei`).
- **Ready-to-Apply Drop-In Fix (`SOURCES.qmd` Line 149)**:
  ```markdown
  14. **Alin Bostan & Ryuhei Mori (2020/2021)** — *"A Simple and Fast Algorithm for Computing the $N$-th Term of a Linearly Recurrent Sequence"* (SOSA 2021, `arXiv:2008.08822`) — Parity-splitting rational coefficient extraction $[x^N] P(x)/Q(x)$ in $O(d \log d \log N)$ (`Ch 05.3`, `Ch 16.2`, `Ch 21.1`).
  ```

#### Item 3.2.4: Optional Frontmatter Polish on 3 Chapter/Checkpoint Files (`ch21`, `ch23`, `cp03`)
- **Observation**: During our automated cross-check of all 32 FPS `.qmd` targets referenced by `_quarto.yml`, `index.qmd`, and `STUDY_PLAN.qmd`, we noticed that 29 of the 32 FPS `.qmd` files use YAML `title:` frontmatter (`---\ntitle: "..."\n---`), whereas 3 files (`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd` line 1, `chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd` line 1, and `checkpoints/cp03-part3-online-implicit-lif-graphs.qmd` line 1) start directly with `# Title` H1 headings. Quarto supports both `# Title` H1 and YAML `title:`, so this renders safely, but we note it here for cross-chapter consistency awareness.

---

## 4. Audit Dimension 4: Strict Quarto Hygiene Verification Across All 7 Target Files

An automated regex and AST parser was executed across all 7 target files to check every Quarto rendering hazard specified in [`AGENTS.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/AGENTS.md):

| File | Total Lines | Forbidden `\(` or `\[` | Factorial `!$$` Collisions | Unescaped `|` inside `$...$` in Tables | Broken Local Links | Unclosed `:::` / `<details>` / `mermaid` | Hygiene Verdict |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [`_quarto.yml`](file:///home/maomao90/Documents/IO/ICPC-math-notes/_quarto.yml) | 169 | `0` | `0` | `0` | `0` (`61/61` valid) | `0` | **PASS** |
| [`index.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/index.qmd) | 194 | `0` | `0` | `0` | `0` (`34/34` valid) | `0` (`2/2` `mermaid` valid) | **PASS** |
| [`00-prerequisite-audit/chapter.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/00-prerequisite-audit/chapter.qmd) | 283 | `0` | `0` | `0` | `0` (`4/4` valid) | `0` | **PASS** |
| [`STUDY_PLAN.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/STUDY_PLAN.qmd) | 186 | `0` | `0` | `0` | `0` (`36/36` valid) | `0` | **PASS** |
| [`NOTATION.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/NOTATION.qmd) | 180 | `0` | `0` | `0` | `0` (`28/28` valid) | `0` | **PASS** |
| [`SOURCES.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/SOURCES.qmd) | 258 | `0` | `0` | `0` | `0` (`7/7` valid) | `0` | **PASS** |
| [`CONTENT_AUDIT.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/CONTENT_AUDIT.md) | 503 | `0` | `0` | `0` | `0` | `0` | **PASS** |
