# Phase 3 Iteration 7 Specialist Audit Report: Per-Topic Smooth Difficulty Ladders & Inline Problem Statements, Constraints, Hints & Solutions (`Ch 01`–`Ch 24`, `192` Problems)

- **Auditor**: `fps-textbook-critic` (Phase 3 Iteration 7 Specialist — Per-Topic Smooth Difficulty Ladders & Inline Problem Statements/Constraints/Solutions)
- **Scope**: All 24 main chapters (`chapters/ch01-ring-convolutions-newton-inv.qmd` through `chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd`), comprising $24 \times 8 = 192$ inline practice ladder problems (`SS-1`, `SS-2`, `Int-1`, `Int-2`, `Adv-1`, `Adv-2`, `Mas-1`, `Mas-2`), cross-examined against `capstones/problem-archive-guide.qmd`, `fps_research/PROBLEM_CURATION.md`, `fps_research/CURRICULUM_ARCHITECTURE.md`, `AGENTS.md`, and `fps_research/PLAN.md`.
- **Audit Date**: 2026-10-15

---

## 1. Executive Summary & Global Compliance Scorecard

| Audit Checklist Dimension | Total Audited | Strictly Compliant | Action Required | Compliance Rate | Key Audit Finding |
| :--- | :-: | :-: | :-: | :-: | :--- |
| **1. Smooth 4-Tier Difficulty Progression (`SS -> Int -> Adv -> Mas`), Canonical ID Bijection & Prerequisite Closure** | `192` problems (`24` chapters) | `191 / 192` (`100%` ID match) | `1` problem (`Ch 10 Int-1` `#244`) | **99.5%** (`100%` ID bijection) | **100% (`192/192`) canonical ID match** against `capstones/problem-archive-guide.qmd` with zero duplicates or drift. One problem (`Ch 10 Int-1`, `#244` `yukicoder 3029: Colored Tree`, `L805–L886`) places *cycle-weighted labeled cacti* (a `Ch 12` topic) as its primary statement (`Part 1`) and relegates the actual `yukicoder 3029` 2-Colored Tree coupled system to `Part 2`. |
| **2A. 100% Self-Contained Inline Problem Statements & Exact Constraints/Moduli (Zero `"refer to OJ"`)** | `192` problems | `179 / 192` | `13` problems (split / hedged variants) | **93.2%** (`100%` zero `"refer to OJ"`) | Zero problems say `"refer to OJ"`; all 192 state constraints, moduli, and target complexities inline. However, **13 problems** split their visible statement into `Variant A / Variant B`, `Part A / Part B`, `Task 1 / Task 2`, or parenthetical ambiguity instead of presenting a single canonical problem statement first. |
| **2B. Visible Hand-Checkable Sample Trace ($N \le 4$) Outside `<details>`** | `192` problems | `160 / 192` (`Ch 05`–`Ch 24`) | `32` problems (`Ch 01`–`Ch 04`) | **83.3%** | **100% (`160/160`)** of problems in Parts II–VI (`Ch 05`–`Ch 24`) have a visible hand-checkable sample trace ($N \le 4$) outside `<details>`. By contrast, **0% (`0/32`)** of problems in Part I (`Ch 01`–`Ch 04`) have a visible sample trace outside `<details>` (`17/32` bury a trace inside the 4th `<details>` solution block; `15/32` omit a small-$N$ trace altogether). |
| **3. 3 Progressive `<details>` Hints (Diagnostic Signal $\to$ Algebraic Setup $\to$ Extraction & Complexity)** | `192` problems (`576` hints) | `184 / 192` | `8` problems (`Ch 22` `<summary>` labels) | **95.8%** (`100%` have 3 hints) | **100% (`192/192`)** of problems have exactly 3 progressive `<details>` hints before the solution block. In `Ch 22` (`8/8` problems), the `<summary>` titles deviate from the textbook-wide `Hint 1 — Diagnostic Signal... / Hint 2 — Algebraic Setup... / Hint 3 — Coefficient Extraction...` convention. |
| **4. Complete Step-by-Step `<details>` Derivation & 5-Part `Algorithm Contract`** | `192` problems | `56 / 192` full 5-part; `88 / 192` 4-of-5; `48 / 192` partial | `48` priority upgrades (`Ch 01, 03, 04, 06, 07, 08`) + `88` 5th-bullet additions | **100%** full derivations; **29.2%** strict 5-part contracts | **100% (`192/192`)** of problems contain complete, multi-step mathematical derivations inside the 4th `<details>` block with zero raw template dumps. For the `Algorithm Contract` block: `Ch 02, 05, 10, 11, 22, 23, 24` (`56` problems) include all 5 required contract components; `Ch 09` and `Ch 12`–`Ch 21` (`88` problems) have 5-bullet callouts that split `Input` and `Preconditions` into two bullets and omit `Failure Modes & Edge Cases` (or `Invariant` in `Ch 17 P3–P8`); `Ch 01, 03, 04, 06, 07, 08` (`48` problems) have abbreviated 1–4 bullet contracts. |

---

## 2. 24-Chapter Master Audit Matrix (`192` Ladder Problems)

| Chapter | Canonical 8-Problem Ladder IDs (`SS-1..Mas-2`) | Problem Line Ranges (`L_start–L_end`) | ID Match & Prereq Closure | Inline Statement Quality | Visible Trace ($N \le 4$) Outside `<details>` | 3 Progressive `<details>` Hints | 4th `<details>` Derivation & 5-Part Contract |
| :--- | :--- | :--- | :-: | :-: | :-: | :-: | :-: |
| **[Ch 01](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd)** | `#019, #043, #004, #077, #049, #097, #066, #107` | `L517–L1229` | PASS (`8/8`) | PASS (`8/8`) | **FAIL (`0/8`)** — Missing outside `<details>` | PASS (`8/8`) | **WARN (`0/8` 5-part)** — Only 1-line `Complexity Contract` |
| **[Ch 02](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd)** | `#238, #165, #101, #222, #157, #084, #030, #091` | `L695–L1352` | PASS (`8/8`) | **WARN (`7/8`)** — `SS-2 (#165)` split (`1. Unbounded` vs `2. 0-1`) | **FAIL (`0/8`)** — Missing outside `<details>` | PASS (`8/8`) | PASS (`8/8` full 5-part callout) |
| **[Ch 03](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd)** | `#001, #188, #153, #009, #223, #221, #150, #159` | `L907–L1500` | PASS (`8/8`) | **WARN (`6/8`)** — `SS-1 (#001)` & `Mas-2 (#159)` split (`Variant A/B`, `Part A/B`) | **FAIL (`0/8`)** — Missing outside `<details>` | PASS (`8/8`) | **WARN (`0/8` 5-part)** — Only 1-line `- **Complexity**:` bullet |
| **[Ch 04](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd)** | `#002, #007, #161, #008, #083, #011, #041, #174` | `L425–L1107` | PASS (`8/8`) | **WARN (`5/8`)** — `SS-2 (#007)`, `Int-2 (#008)`, `Adv-2 (#011)` split/hedged | **FAIL (`0/8`)** — Missing outside `<details>` | PASS (`8/8`) | **WARN (`0/8` 5-part)** — Missing `Invariant` & `Failure Modes` |
| **[Ch 05](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd)** | `#104, #034, #187, #069, #040, #081, #177, #073` | `L785–L1837` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8` — 4 bullets covering all 5 parts) |
| **[Ch 06](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd)** | `#005, #055, #193, #080, #094, #096, #098, #109` | `L792–L1391` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | **WARN (`0/8` 5-part)** — Only `Trace`, `Boundary Cases`, `Complexity` |
| **[Ch 07](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd)** | `#224, #248, #178, #143, #147, #012, #092, #168` | `L690–L1612` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | **WARN (`0/8` 5-part)** — Missing `Invariant` & `Failure Modes` |
| **[Ch 08](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd)** | `#018, #241, #155, #089, #067, #139, #052, #137` | `L590–L1297` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | **WARN (`0/8` 5-part)** — Missing `Failure Modes` bullet in §5 |
| **[Ch 09](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch09-cdq-fft-online-relaxed-convolution.qmd)** | `#060, #021, #086, #023, #056, #225, #206, #075` | `L527–L1332` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | **MINOR (`8/8` 4-of-5)** — Add `Failure Modes & Edge Cases` bullet |
| **[Ch 10](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd)** | `#186, #226, #244, #013, #179, #126, #191, #192` | `L624–L1390` | **FAIL (`7/8`)** — `Int-1 (#244)` uses `Ch 12` Cactus as `Part 1` | **WARN (`6/8`)** — `Int-1 (#244)` inverted; `Adv-2 (#126)` hedged | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8` full 6-bullet contract) |
| **[Ch 11](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd)** | `#003, #200, #196, #201, #010, #229, #114, #203` | `L817–L1733` | PASS (`8/8`) | **WARN (`7/8`)** — `SS-2 (#200)` split into `Task 1 / Task 2` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8` full 5-bullet contract) |
| **[Ch 12](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd)** | `#176, #245, #146, #227, #190, #016, #183, #184` | `L568–L1296` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | **MINOR (`8/8` 4-of-5)** — Add `Failure Modes & Edge Cases` bullet |
| **[Ch 13](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd)** | `#164, #103, #093, #189, #199, #053, #122, #212` | `L794–L1680` | PASS (`8/8`) | **WARN (`6/8`)** — `Adv-2 (#053)` & `Mas-1 (#122)` split (`1/2`, `Part A/B`) | PASS (`8/8`) | PASS (`8/8`) | **MINOR (`8/8` 4-of-5)** — Add `Failure Modes & Edge Cases` bullet |
| **[Ch 14](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd)** | `#115, #026, #156, #071, #148, #209, #039, #113` | `L601–L1340` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | **MINOR (`8/8` 4-of-5)** — Add `Failure Modes & Edge Cases` bullet |
| **[Ch 15](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd)** | `#105, #070, #220, #140, #128, #134, #076, #210` | `L531–L1430` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | **MINOR (`8/8` 4-of-5)** — Add `Failure Modes & Edge Cases` bullet |
| **[Ch 16](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd)** | `#048, #129, #025, #232, #237, #074, #240, #214` | `L692–L1386` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | **MINOR (`8/8` 4-of-5)** — Add `Failure Modes & Edge Cases` bullet |
| **[Ch 17](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd)** | `#154, #044, #228, #219, #015, #204, #138, #234` | `L614–L1400` | PASS (`8/8`) | **WARN (`7/8`)** — `Adv-1 (#015)` has `\dots` in step set $\mathcal{S}_{12}$ | PASS (`8/8`) | PASS (`8/8`) | **MINOR (`8/8` 4-of-5)** — `P1–P2` need `Failure Modes`; `P3–P8` need `Invariant` |
| **[Ch 18](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd)** | `#151, #064, #022, #239, #125, #088, #211, #230` | `L558–L1387` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | **MINOR (`8/8` 4-of-5)** — Add `Failure Modes & Edge Cases` bullet |
| **[Ch 19](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd)** | `#242, #120, #095, #195, #028, #118, #072, #213` | `L418–L1100` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | **MINOR (`8/8` 4-of-5)** — Add `Failure Modes & Edge Cases` bullet |
| **[Ch 20](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd)** | `#050, #197, #127, #167, #208, #202, #181, #217` | `L768–L1529` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | **MINOR (`8/8` 4-of-5)** — Add `Failure Modes & Edge Cases` bullet |
| **[Ch 21](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd)** | `#036, #045, #047, #059, #065, #218, #235, #017` | `L500–L1065` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | **MINOR (`8/8` 4-of-5)** — Add `Failure Modes & Edge Cases` bullet |
| **[Ch 22](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd)** | `#031, #124, #046, #198, #149, #136, #166, #145` | `L591–L1297` | PASS (`8/8`) | **WARN (`7/8`)** — `Int-1 (#046)` parenthetically hedged | PASS (`8/8`) | **WARN (`8/8` labels)** — Non-standard `<summary>` titles | PASS (`8/8` full 5-part contract) |
| **[Ch 23](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd)** | `#123, #033, #233, #057, #062, #132, #063, #111` | `L484–L1222` | PASS (`8/8`) | **WARN (`7/8`)** — `Int-1 (#233)` parenthetically hedged | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8` full 5-part contract) |
| **[Ch 24](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd)** | `#216, #020, #027, #042, #110, #207, #231, #038` | `L556–L1410` | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8`) | PASS (`8/8` full 6-bullet contract) |

---

## 3. Dimension 1 Audit: Smooth 4-Tier Difficulty Progression, Canonical ID Bijection & Prerequisite Closure

### 3.1 100% (`192/192`) Canonical ID Bijective Alignment Verified
Every single one of the 192 ladder problems across `Ch 01`–`Ch 24` matches the canonical problem pool IDs (`#001`–`#254`) and tier slots (`SS-1`, `SS-2`, `Int-1`, `Int-2`, `Adv-1`, `Adv-2`, `Mas-1`, `Mas-2`) in [problem-archive-guide.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/problem-archive-guide.qmd) and [PROBLEM_CURATION.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md) with **zero missing problems, zero duplicates, and zero tier inversions**.

### 3.2 Action Item 1.1 (CRITICAL — Prerequisite Closure & Inverted Problem Statement in `Ch 10 Int-1`, `#244` `yukicoder 3029: Colored Tree`)

- **File & Lines**: [ch10-implicit-equations-newton-unlabeled-trees-otter.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd#L805-L886)
- **Diagnostic Issue**:
  1. According to `PROBLEM_CURATION.md` (`L324`, `L1289`), `problem_archive.md` (`L1483–L1494`), and `cohort3_wave_3b_implicit_zh_ja_audit.md` (`L886–L902`), `#244` (`yukicoder 3029: Colored Tree`) is the **2-Colored Red/Blue Rooted Tree Coupled Implicit System** ($\Phi_1(x, R, B) = R - x \exp(B) = 0, \Phi_2(x, R, B) = B - x \sum_{j=0}^K \frac{R^j}{j!} = 0$), which teaches how to solve a $2 \times 2$ coupled tree system in `Ch 10 §10.2` via substitution elimination + Logarithmic Newton Iteration (or $2 \times 2$ Jacobian Newton).
  2. However, in `ch10-implicit-equations-newton-unlabeled-trees-otter.qmd` (`L805–L886`), the visible problem statement (`L812`) and `Part 1` (`L850–L864`) instead define **Cycle-Weighted Labeled Cacti** (using Block-Cut Tree decomposition around cycles of length $L \ge 3$ and bridges, which is a **forward-reference to Chapter 12** and duplicates `#227 LOJ 6569 — Cactus Counting` in `Ch 12 Int-2`), while relegating the actual `yukicoder 3029` 2-Colored Tree problem to a brief note in `Part 2` (`L866–L873`)!
- **Exact Drop-In Fix for `L805–L886` of `chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd`**:
  Replace lines `805–886` with the unified 2-Colored Rooted Tree specification:

```markdown
### Intermediate 1 (`#244`) — yukicoder 3029: Colored Tree

- **Source**: [yukicoder No. 3029 — Colored Tree](https://yukicoder.me/problems/no/3029)
- **Prerequisite Tags**: `[Coupled-2x2-Implicit-System]`, `[Substitution-Elimination]`, `[2x2-Jacobian-Newton]`, `[Logarithmic-Newton-Speedup]`

#### Problem Statement & Exact Constraints

Consider rooted labeled trees on $n$ vertices $\{1, 2, \dots, n\}$ in which every vertex is colored either **Red** or **Blue** subject to the following two-layer branching rules:

1. The root of the tree is colored **Red**.
2. Every **Red** vertex has an arbitrary number of children, all of which must be colored **Blue**.
3. Every **Blue** vertex has **at most $K$** children ($0 \le \text{children} \le K$), all of which must be colored **Red**.

Given $N$ and the degree cap $K$, compute for every $n = 1, 2, \dots, N$ the number of valid 2-colored rooted labeled trees on $n$ vertices modulo $998244353$.

- **Constraints**: $1 \le K \le N \le 2.5 \times 10^5$, modulus $p = 998244353$.
- **Required Complexity**: $O(N \log N)$ time and $O(N)$ space.
- **Sample Trace ($N = 3, K = 1$)**:
  - $n = 1$: Only the Red root ($1$ tree: $r_1 = 1$).
  - $n = 2$: The Red root has $1$ Blue child, which is a leaf ($2! \cdot [x^2] R(x) = 2$ labeled trees: $1_R \to 2_B$ or $2_R \to 1_B$).
  - $n = 3$: Either the Red root has $2$ Blue leaf children ($3$ ways to choose the Red root $\times 1$ unordered pair of Blue leaves $= 3$ trees), or the Red root has $1$ Blue child which in turn has $1$ Red child ($3! = 6$ labeled paths $u_R \to v_B \to w_R$), giving $r_3 = 3 + 6 = 9$.

<details>
<summary>Hint 1 — Diagnostic Signal & Combinatorial Model</summary>

Let $R(x) = \sum_{n=1}^\infty \frac{r_n}{n!} x^n$ be the EGF of valid trees rooted at a **Red** vertex, and let $B(x) = \sum_{n=1}^\infty \frac{b_n}{n!} x^n$ be the EGF of valid subtrees rooted at a **Blue** vertex.
- Removing a Red root leaves an arbitrary unordered $\operatorname{SET}$ of Blue-rooted subtrees: $R(x) = x \exp(B(x))$.
- Removing a Blue root leaves an unordered $\operatorname{SET}_{\le K}$ of at most $K$ Red-rooted subtrees: $B(x) = x P_K(R(x))$, where $P_K(y) = \sum_{j=0}^K \frac{y^j}{j!}$.

</details>

<details>
<summary>Hint 2 — Algebraic Setup & Reverse-Engineering Scratchpad</summary>

1. Notice that $B(x) = x P_K(R(x))$ is already explicit in $R(x)$! By the Substitution Principle of Section 10.2, substitute $B(x)$ directly into $R(x) = x \exp(B(x))$ to obtain the single univariate implicit equation:
   $$R(x) = x \exp\!\big(x P_K(R(x))\big), \qquad P_K(y) = \sum_{j=0}^{K} \frac{y^j}{j!}.$$
2. Apply the **Logarithmic Newton Speedup** from Section 10.1 to $\Psi(R) = \ln(R(x)/x) - x P_K(R(x)) = 0$ so that you never call `exp` inside the Newton loop!

</details>

<details>
<summary>Hint 3 — Coefficient Extraction & Complexity Contract</summary>

Since $P_K'(y) = P_{K-1}(y) = \sum_{j=0}^{K-1} \frac{y^j}{j!}$ (with $P_{-1}(y) = 0$), the Logarithmic Newton derivative is $\Psi'(R) = \frac{1}{R} - x P_{K-1}(R)$. Multiplying through by $R_d(x)$ yields the doubling update:
$$R_{2d}(x) \equiv R_d(x) \left( 1 - \frac{\ln(R_d(x)/x) - x P_K(R_d(x))}{1 - x R_d(x) P_{K-1}(R_d(x))} \right) \pmod{x^{2d}},$$
requiring only polynomial evaluation of $P_K(R_d)$ (or `exp` when $K \ge N$), 1 `ln`, and 1 `inv` per doubling step!

</details>

<details>
<summary>Complete Derivation & Solution</summary>

#### Step 1: Coupled $2 \times 2$ Species System & Substitution Elimination

1. **Setting Up the Coupled System**:
   By theLabeled `SET` construction (Chapter 4), a Red root (EGF $x$) attached to an arbitrary set of Blue subtrees and a Blue root (EGF $x$) attached to at most $K$ Red subtrees satisfy the $2 \times 2$ implicit system:
   $$\Phi_1(x, R, B) = R(x) - x \exp\!\big(B(x)\big) = 0, \qquad \Phi_2(x, R, B) = B(x) - x P_K\big(R(x)\big) = 0,$$
   where $P_K(y) = \sum_{j=0}^{K} \frac{y^j}{j!}$.
2. **Equivalence of Substitution Elimination and $2 \times 2$ Jacobian Inversion (§10.2)**:
   - **Via Substitution**: Substituting $B(x) = x P_K(R(x))$ into $\Phi_1 = 0$ gives $R(x) = x \exp\!\big(x P_K(R(x))\big)$, or equivalently $\Psi(R) := \ln(R(x)/x) - x P_K(R(x)) = 0$.
   - **Via $2 \times 2$ Jacobian Matrix**: Even if we kept $(R, B)$ un-eliminated, the $2 \times 2$ Jacobian of $(\Phi_1, \Phi_2)$ is
     $$J_{\mathbf{\Phi}}(R, B) = \begin{pmatrix} 1 & -x e^{B} \\ -x P_{K-1}(R) & 1 \end{pmatrix}, \qquad \det J_{\mathbf{\Phi}} = 1 - x^2 e^{B} P_{K-1}(R) = 1 - x R P_{K-1}(R),$$
     producing the exact same Newton denominator $1 - x R_d(x) P_{K-1}(R_d(x))$!

#### Step 2: Logarithmic Newton Iteration & Hand-Check Verification ($N = 3, K = 1$)

For $K = 1$, $P_1(y) = 1 + y$ and $P_0(y) = 1$, so $\ln(R(x)/x) = x(1 + R(x))$. Expanding up to $x^3$:
$$\frac{R(x)}{x} = \exp\!\big(x + x R(x)\big) = 1 + (x + x R(x)) + \frac{1}{2}(x + x R(x))^2 + \dots$$
- $[x^1] R(x) = 1 \implies r_1 = 1! \cdot 1 = 1$.
- $[x^2] R(x) = [x^1]\big(x + x R(x)\big) = 1 \implies r_2 = 2! \cdot 1 = 2$.
- $[x^3] R(x) = [x^2]\left(x R(x) + \frac{1}{2} x^2\right) = [x^1]R(x) + \frac{1}{2} = \frac{3}{2} \implies r_3 = 3! \cdot \frac{3}{2} = 9$, matching our hand trace!

*(Note on Plane/Ordered Variant)*: When the problem instead specifies **ordered (plane)** 2-colored trees with $a$ Red vertices and $b$ Blue vertices where $R(x, y) = x \frac{1 - B^{K+1}}{1 - B}$ and $B(x, y) = \frac{y}{1 - R}$, the exact same substitution $B = \frac{y}{1 - R}$ eliminates $B$ in one line!

::: {.callout-important}
## Algorithm Contract (`#244 yukicoder 3029`)

- **Input**: Integers $N, K$ ($1 \le K \le N \le 2.5 \times 10^5$).
- **Preconditions**: Prime modulus $p = 998244353 > N$.
- **Index & Truncation Boundaries**: Base case $R_1(x) = x \pmod{x^2}$; at doubling step $d \to 2d$, shift $U_d(x) = R_d(x)/x \bmod x^{2d-1}$ with $U_d(0) = 1$ before calling `ln(U_d, 2d-1)`, evaluate $x P_K(R_d(x)) \bmod x^{2d-1}$ and $x R_d(x) P_{K-1}(R_d(x)) \bmod x^{2d-1}$, and multiply the fractional correction by $R_d(x) \bmod x^{2d}$.
- **1-Sentence Loop Invariant**: After doubling step $d$, $R_d(x) \equiv x \exp\!\big(x P_K(R_d(x))\big) \pmod{x^d}$ holds with exact 2-colored tree EGF coefficients $[x^1 \dots x^{d-1}]R(x)$.
- **Output**: Sequence $r_n = n! [x^n] R(x) \bmod 998244353$ for $1 \le n \le N$.
- **Complexity**: $O(N \log N)$ time, $O(N)$ space.
:::

</details>
```

---

## 4. Dimension 2 Audit: Self-Contained Inline Problem Statements, Exact Constraints/Moduli, and Visible Sample Traces ($N \le 4$)

### 4.1 Action Item 2.1 — Add Visible Hand-Checkable Sample Traces ($N \le 4$) Outside `<details>` for All 32 Problems in Part I (`Ch 01`–`Ch 04`)

In Parts II–VI (`Ch 05`–`Ch 24`), **all 160 problems (`100%`)** display a visible **Sample Trace ($N \le 4$)** outside `<details>` right below the problem statement and constraints so the reader can verify their understanding of the combinatorial rules before opening Hint 1.
In Part I (`Ch 01`–`Ch 04`), **none of the 32 problems (`0%`)** have a visible sample trace outside `<details>` (`17` place a trace inside the 4th `<details>` solution block, while `15` omit a concrete small-$N$ trace entirely).

Below are the exact insertion lines (immediately before the first `<details>` tag of each problem) and ready-to-insert visible sample traces for all 32 problems in `Ch 01`–`Ch 04`:

#### Chapter 01 (`chapters/ch01-ring-convolutions-newton-inv.qmd`)
1. **`Ch 01 SS-1` (`#019` AtCoder ABC 178 D — Redistribution, insert before `L530`)**:
   ```markdown
   - **Sample Trace ($S = 7$)**: The ordered tuples of integers $\ge 3$ summing to $7$ are $(7)$, $(3, 4)$, and $(4, 3)$, giving **3** valid sequences.
   ```
2. **`Ch 01 SS-2` (`#043` AtCoder ABC 331 G — Collect Them All, insert before `L626`)**:
   ```markdown
   - **Sample Trace ($N = 3, M = 2, C = (1, 2)$)**: The subset sums are $S_\varnothing = 0$, $S_{\{1\}} = 1$, $S_{\{2\}} = 2$, $S_{\{1,2\}} = 3$. By Inclusion–Exclusion, $\mathbb{E}[T] = 3\left(\frac{1}{1} + \frac{1}{2} - \frac{1}{3}\right) = \frac{7}{2} \equiv 499122180 \pmod{998244353}$.
   ```
3. **`Ch 01 Int-1` (`#004` AtCoder `fps_24_h` — Snack 2, insert before `L713`)**:
   ```markdown
   - **Sample Trace ($N = 2, M = 1$)**: For $k = 0$: $\binom{1}{0} 2^0 = 1$; for $k = 1$: $\binom{1}{1} 2^1 = 2$ ($S_1 = 3$). For the second sum: $(3^2 - 2^2)\left(\binom{1}{0}2^0 + \binom{2}{1}2^1\right) = 5 \times 5 = 25$. Total $= 3 + 25 = 28$.
   ```
4. **`Ch 01 Int-2` (`#077` AtCoder JSC 2019 Final E —ashi's Move, insert before `L791`)**:
   ```markdown
   - **Sample Trace ($N = 2, K = 1, A = [1, 2]$)**: We extract $[x^0 \dots x^2]$ of $\big((1-x)^{-1}(1 + x + 2x^2)\big)^{-1} = (1 - x)(1 + x + 2x^2)^{-1} = 1 - 2x + 0x^2 + \dots$, giving $(1, -2, 0) \equiv (1, 998244351, 0) \pmod{998244353}$.
   ```
5. **`Ch 01 Adv-1` (`#049` AtCoder ARC 028 D — 注文の多い高橋商店, insert before `L865`)**:
   ```markdown
   - **Sample Trace ($N = 3, M = 2, a = (1, 2, 1), Q$: $k = 2, x = 1$)**: Removing item $2$ leaves items $1$ and $3$ with polynomial $(1+t)^2 = 1 + 2t + t^2$. To reach total $M = 2$ when item $2$ contributes $x = 1$, the remaining items must contribute $M - x = 1$, giving $[t^1](1+t)^2 = 2$.
   ```
6. **`Ch 01 Adv-2` (`#097` CF 993E — Nikita and Order Statistics, insert before `L946`)**:
   ```markdown
   - **Sample Trace ($n = 3, x = 2, A = [1, 2, 1]$)**: Prefix counts of elements $< 2$ are $(c_0, c_1, c_2, c_3) = (0, 1, 1, 2)$, so frequency array is $f = (1, 2, 1)$. Subarray counts for $k = 0, 1, 2, 3$ are $(1, 3, 2, 0)$.
   ```
7. **`Ch 01 Mas-1` (`#066` AtCoder AGC 001 E — BBQ Hard, insert before `L1031`)**:
   ```markdown
   - **Sample Trace ($N = 2, (A_1, B_1) = (1, 1), (A_2, B_2) = (1, 2)$)**: The single pair $(1, 2)$ has $\binom{1+1+1+2}{1+1} = \binom{5}{2} = 10$ paths, which equals $\frac{1}{2}\big([x^1 y^2]\text{DP} + [x^1 y^1]\text{DP} - \binom{2}{1} - \binom{3}{1}\big) = 10$.
   ```
8. **`Ch 01 Mas-2` (`#107` CF 1218D — Xor Spanning Tree, insert before `L1137`)**:
   ```markdown
   - **Sample Trace (Triangle $C_3$ with edge weights $1, 2, 3$)**: Total XOR of all edges is $1 \oplus 2 \oplus 3 = 0$. Deleting one edge from the 3-cycle leaves spanning tree XORs $\{0 \oplus 1, 0 \oplus 2, 0 \oplus 3\} = \{1, 2, 3\}$, so minimum XOR is **1** with multiplicity **1**.
   ```

#### Chapter 02 (`chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd`)
1. **`Ch 02 SS-1` (`#238` yukicoder 1145 — Sum of Powers, insert before `L706`)**:
   ```markdown
   - **Sample Trace ($N = 2, M = 3, A = [1, 2]$)**: $Q(x) = (1 - x)(1 - 2x) = 1 - 3x + 2x^2$, and $-x Q'(x)/Q(x) = 3x + 5x^2 + 9x^3 + \dots$, matching $S_1 = 1+2 = 3, S_2 = 1+4 = 5, S_3 = 1+8 = 9$.
   ```
2. **`Ch 02 SS-2` (`#165` 0-1 Subset Sum via Pólya-Logarithm, insert before `L783`)**:
   ```markdown
   - **Sample Trace ($N = 3, M = 3, w = [1, 1, 2]$)**: $\prod_{i=1}^3 (1 + x^{w_i}) = (1 + x)^2(1 + x^2) = 1 + 2x + 2x^2 + 2x^3 + x^4$, so subset counts for $s = 1, 2, 3$ are $(2, 2, 2)$.
   ```
3. **`Ch 02 Int-1` (`#101` CF 1096G — Lucky Tickets, insert before `L857`)**:
   ```markdown
   - **Sample Trace ($n = 2, D = \{0, 1\}$)**: Here $k = n/2 = 1$ and $P(x) = 1 + x$. The sum of squares of coefficients of $P(x)^1$ is $1^2 + 1^2 = 2$ (tickets `00` and `11`). For $n = 4$ ($k = 2$), $P(x)^2 = 1 + 2x + x^2$, giving $1^2 + 2^2 + 1^2 = 6$.
   ```
4. **`Ch 02 Int-2` (`#222` LOJ 6261 — Lonely Senior Year, insert before `L941`)**:
   ```markdown
   - **Sample Trace ($n = 3, k = 2, A = [1, 1, 1]$)**: Since $A(x) = (1 - x)^{-1} \bmod x^3$, $B(x) = A(x) \cdot (1 - x)^{-2} = (1 - x)^{-3} = 1 + 3x + 6x^2 + \dots$, giving $(1, 3, 6)$.
   ```
5. **`Ch 02 Adv-1` (`#157` Luogu P4705 — 玩游戏, insert before `L1021`)**:
   ```markdown
   - **Sample Trace ($n = 1, m = 1, a = [1], b = [2], K = 2$)**: There is $n m = 1$ pair with sum $a_1 + b_1 = 3$, so expected values for $t = 1, 2$ are $(3^1, 3^2) = (3, 9)$.
   ```
6. **`Ch 02 Adv-2` (`#084` CF 438E — The Child and Binary Tree, insert before `L1108`)**:
   ```markdown
   - **Sample Trace ($n = 1, m = 3, C = \{1\}$)**: Here $C(x) = x$, so $T(x) = \frac{1 - \sqrt{1 - 4x}}{2x} - 1 = x + 2x^2 + 5x^3 + \dots$ (Catalan numbers $C_1 = 1, C_2 = 2, C_3 = 5$).
   ```
7. **`Ch 02 Mas-1` (`#030` AtCoder ABC 267 Ex — Odd Sum, insert before `L1189`)**:
   ```markdown
   - **Sample Trace ($N = 3, M = 3, A = [1, 1, 2]$)**: Odd-sized subsets summing to $3$ must have size $1$ (none, since $3 \notin A$) or size $3$ ($\{1, 1, 2\}$ sums to $4 \ne 3$). For $M = 4$, the size-$3$ subset $\{1, 1, 2\}$ sums to $4$, giving answer **1**.
   ```
8. **`Ch 02 Mas-2` (`#091` CF 891E — Lust, insert before `L1274`)**:
   ```markdown
   - **Sample Trace ($n = 2, k = 1, a = [2, 3]$)**: With $k = 1$ decrement, we either decrement $a_1$ ($2 \to 1$, gain $3$) or $a_2$ ($3 \to 2$, gain $2$), so expected gain is $\frac{3 + 2}{2} = \frac{5}{2} \equiv 499122179 \pmod{10^9 + 7}$.
   ```

#### Chapter 03 (`chapters/ch03-mset-partitions-euler-polya.qmd`)
1. **`Ch 03 SS-1` (`#001` AtCoder `fps_24_a` — Snack, insert before `L923`)**:
   ```markdown
   - **Sample Trace ($D = 1, N = 3$)**: With $1$ snack chosen from $(1\text{ of }1\text{-yen}, 2\text{ of }3\text{-yen}, 1\text{ of }4\text{-yen}, 3\text{ of }6\text{-yen})$, the number of ways to spend $N = 3$ yen is $[x^3](x + 2x^3 + x^4 + 3x^6)^1 = 2$.
   ```
2. **`Ch 03 SS-2` (`#188` Luogu P6189 — Running, insert before `L1004`)**:
   ```markdown
   - **Sample Trace ($N = 4$)**: The integer partitions of $4$ are $(4), (3,1), (2,2), (2,1,1), (1,1,1,1)$, giving $p(4) = 5$.
   ```
3. **`Ch 03 Int-1` (`#153` Luogu P4389 — 付公主的背包, insert before `L1077`)**:
   ```markdown
   - **Sample Trace ($n = 2, m = 3, v = [1, 2]$)**: Unbounded multisets from $\{1, 2\}$ have OGF $\frac{1}{(1-x)(1-x^2)} = 1 + x + 2x^2 + 2x^3 + \dots$, giving $(1, 2, 2)$ for $s = 1, 2, 3$.
   ```
4. **`Ch 03 Int-2` (`#009` AtCoder `fps_24_o` — Rooted Trees, insert before `L1142`)**:
   ```markdown
   - **Sample Trace ($N = 4$)**: The numbers of unlabeled rooted trees on $n = 1, 2, 3, 4$ vertices are $T_1 = 1, T_2 = 1, T_3 = 2$ (path $P_3$ and cherry $K_{1,2}$), and $T_4 = 4$.
   ```
5. **`Ch 03 Adv-1` (`#223` yukicoder 899 / LOJ 6268 — Inverse Euler Transform, insert before `L1217`)**:
   ```markdown
   - **Sample Trace ($N = 3, b = [1, 1, 2, 2]$)**: Since $B(x) = 1 + x + 2x^2 + 2x^3 \equiv \frac{1}{(1-x)(1-x^2)} \pmod{x^4}$, the inverse Euler transform recovers generator multiplicities $(a_1, a_2, a_3) = (1, 1, 0)$.
   ```
6. **`Ch 03 Adv-2` (`#221` LOJ 6089 — 小 Y 的背包计数问题, insert before `L1276`)**:
   ```markdown
   - **Sample Trace ($N = 3$)**: Item $1$ has size $1$ and cap $1$; item $2$ has size $2$ and cap $2$; item $3$ has size $3$ and cap $3$. Expanding $(1+x)(1+x^2+x^4)(1+x^3+x^6+x^9) \bmod x^4 = 1 + x + x^2 + 2x^3$, giving $(1, 1, 2)$ for $s = 1, 2, 3$.
   ```
7. **`Ch 03 Mas-1` (`#150` Luogu P3784 — 遗忘的集合, insert before `L1354`)**:
   ```markdown
   - **Sample Trace ($n = 3, f = [1, 1, 2]$ for $1 + f_1 x + f_2 x^2 + f_3 x^3 = 1 + x + x^2 + 2x^3$)**: Factoring $1 + x + x^2 + 2x^3 \equiv (1+x)(1+x^2)(1+x^3) \pmod{x^4}$ recovers the 0-1 item set $S = \{1, 2, 3\}$.
   ```
8. **`Ch 03 Mas-2` (`#159` Luogu P4727 — 图的同构记数, insert before `L1428`)**:
   ```markdown
   - **Sample Trace ($n = 3$)**: The partitions of $3$ are $(1,1,1)$ ($1$ perm, $3$ edge orbits $\implies 2^3 = 8$), $(2,1)$ ($3$ perms, $2$ edge orbits $\implies 3 \times 2^2 = 12$), and $(3)$ ($2$ perms, $1$ edge orbit $\implies 2 \times 2^1 = 4$). Burnside average: $\frac{8 + 12 + 4}{6} = 4$ unlabeled graphs on $3$ vertices ($0, 1, 2, 3$ edges).
   ```

#### Chapter 04 (`chapters/ch04-egf-set-cyc-boxed-prufer.qmd`)
1. **`Ch 04 SS-1` (`#002` AtCoder `fps_24_e` — Sequence, insert before `L438`)**:
   ```markdown
   - **Sample Trace ($N = 2, M = 2$)**: Symbol $1$ can appear $\le 1$ time and symbol $2$ can appear $\le 2$ times. Valid length-$2$ sequences over $\{1, 2\}$ are $(1, 2), (2, 1), (2, 2)$, giving $2! [x^2](1 + x)\left(1 + x + \frac{x^2}{2}\right) = 3$.
   ```
2. **`Ch 04 SS-2` (`#007` AtCoder `fps_24_m` — Value of Permutation, insert before `L514`)**:
   ```markdown
   - **Sample Trace ($N = 2, a = (a_1, a_2)$)**: Of the $2! = 2$ permutations of $\{1, 2\}$, the identity $(1)(2)$ has two $1$-cycles and the transposition $(1\,2)$ has one $2$-cycle, so the additive total is $2 a_1 + a_2$ and the multiplicative total is $a_1^2 + a_2$.
   ```
3. **`Ch 04 Int-1` (`#161` Luogu P4841 — 城市规划, insert before `L592`)**:
   ```markdown
   - **Sample Trace ($n = 3$)**: Total labeled graphs on $3$ vertices is $2^{\binom{3}{2}} = 8$. Disconnected graphs have $0$ edges ($1$ graph) or $1$ edge ($3$ graphs), leaving $8 - 4 = 4$ connected labeled graphs ($3$ paths of length $2$ and $1$ triangle $K_3$).
   ```
4. **`Ch 04 Int-2` (`#008` AtCoder `fps_24_n` — Tree, insert before `L671`)**:
   ```markdown
   - **Sample Trace ($N = 4, D = \{1, 3\}$)**: A tree on $4$ vertices with all degrees in $\{1, 3\}$ must have Prüfer multiplicities in $\{0, 2\}$, so one vertex has multiplicity $2$ (degree $3$, the center of $K_{1,3}$) and three vertices have multiplicity $0$ (leaves), giving $2! [x^2] \left(1 + \frac{x^2}{2!}\right)^4 = 4$ labeled stars.
   ```
5. **`Ch 04 Adv-1` (`#083` CF 438D / BZOJ 3456 — 城市规划 Boxed Pivot, insert before `L746`)**:
   ```markdown
   - **Sample Trace ($n = 3$)**: Using the boxed-component recurrence $c_n = 2^{\binom{n}{2}} - \sum_{k=1}^{n-1} \binom{n-1}{k-1} c_k 2^{\binom{n-k}{2}}$ with $c_1 = 1, c_2 = 1$ gives $c_3 = 8 - \big(\binom{2}{0}(1)(2^1) + \binom{2}{1}(1)(2^0)\big) = 8 - (2 + 2) = 4$.
   ```
6. **`Ch 04 Adv-2` (`#011` AtCoder `fps_24_q` — Dice, insert before `L831`)**:
   ```markdown
   - **Sample Trace ($N = 2, M = 2, K = 2, A = [1, 2]$)**: The $2^2 = 4$ ordered pairs have sums $\{2, 3, 3, 4\}$. For $k = 1$, the sum is $2 + 3 + 3 + 4 = 12$; for $k = 2$, the sum of squares is $2^2 + 3^2 + 3^2 + 4^2 = 38$.
   ```
7. **`Ch 04 Mas-1` (`#041` AtCoder ABC 306 Ex — Balance Scale, insert before `L927`)**:
   ```markdown
   - **Sample Trace ($N = 2, M = 1$, single comparison $1\text{ vs }2$)**: There are $3$ outcomes (`<`, `>`, `=`). Both `<` and `>` produce $2$-vertex DAGs ($1$ edge), whereas `=` contracts $\{1, 2\}$ into a single $1$-vertex component ($0$ edges). All $3$ outcomes are acyclic, so the answer is **3**.
   ```
8. **`Ch 04 Mas-2` (`#174` Luogu P5401 — 珍珠, insert before `L1010`)**:
   ```markdown
   - **Sample Trace ($D = 2, n = 2, m = 1$)**: We need at least $m = 1$ pair of matching colors among $n = 2$ pearls of $D = 2$ colors. Only $(1, 1)$ and $(2, 2)$ have a pair (whereas $(1, 2)$ and $(2, 1)$ have $2$ odd color counts, exceeding $n - 2m = 0$), giving **2** valid sequences.
   ```

---

### 4.2 Action Item 2.2 — Unify Split / Hedged Problem Statements (`13` Problems)

To comply with `AGENTS.md` and `fps_research/PLAN.md` (*"Problem statements must be 100% self-contained, stating exact inputs, outputs, constraints, and moduli without hedging or 'refer to OJ'"*), each of the following 13 problems should state a **single canonical problem statement** outside `<details>`, moving secondary variants or companion problems into a remark inside the 4th `<details>` solution block:

1. **[Ch 02 SS-2 (`#165`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L770-L782)**:
   - **Issue**: Splits into `1. Unbounded Knapsack (Luogu P4389)` and `2. 0-1 Subset Sum Variant`. Since `Luogu P4389` (Unbounded Knapsack) is already the canonical problem `#153` in `Ch 03 Int-1`, `#165` should state the **0-1 Subset Sum via Pólya-Logarithm** ($\prod_{i=1}^N (1 + x^{w_i}) \bmod x^{M+1}$) as its single primary statement, and mention the sign change for $(1 - x^{w_i})^{-1}$ inside the solution block.
2. **[Ch 03 SS-1 (`#001`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L907-L922)**:
   - **Issue**: Splits into `Variant A (Factored Menu)` and `Variant B (Multiplicity Menu — fps_24_a)`.
   - **Fix**: Make `Variant B` (the actual AtCoder `fps_24_a — Snack` problem: $1$ snack of $1$ yen, $2$ snacks of $3$ yen, $1$ snack of $4$ yen, $3$ snacks of $6$ yen; $D$ snacks totaling $N$ yen with $N - D \le 5 \times 10^5$) the sole visible problem statement, and present `Variant A` inside Hint 2 / Solution Step 1 as the warm-up motivation.
3. **[Ch 03 Mas-2 (`#159`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L1416-L1427)**:
   - **Issue**: Splits into `Part A (Luogu P4727, n <= 60 unlabeled graphs)` and `Part B (Pólya–Redfield Cycle Index Synthesis for necklaces, N <= 10^5)`.
   - **Fix**: Make `Part A` (`Luogu P4727 — 图的同构记数`: count unlabeled simple undirected graphs on $n \le 60$ vertices modulo $997$) the sole visible problem statement, and keep `Part B` as `#### Bonus Extension: Pólya–Redfield Cycle Index for Cyclic Necklaces` inside the 4th `<details>` solution block.
4. **[Ch 04 SS-2 (`#007`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L499-L513)**:
   - **Issue**: Splits into `1. additive cycle weight` and `2. multiplicative cycle weight`.
   - **Fix**: State the multiplicative cycle-weight product $\prod_{c \in \mathcal{C}(\pi)} a_{|c|}$ (`[x^N] \exp(\sum_{L=1}^N a_L \frac{x^L}{L})`, the primary `SET(CYC)` identity of `fps_24_m`) as the primary problem statement, and derive the $O(N)$ additive cycle-weight formula $N! \sum_{L=1}^N \frac{a_L}{L}$ as Step 1 of the solution.
5. **[Ch 04 Int-2 (`#008`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L660-L670)**:
   - **Issue**: Hedged parenthetical wording (`"Each vertex i has a prescribed degree constraint or degree weight function w_i(d) (for instance, in fps_24_n ... while in Luogu P2290 ...)"`).
   - **Fix**: State `AtCoder fps_24_n — Tree` directly: given $N \le 2.5 \times 10^5$ and a subset of allowed vertex degrees $S \subseteq \{1, 2, \dots, N-1\}$, count the number of labeled trees on $N$ vertices in which every vertex $v \in \{1, \dots, N\}$ has degree $\deg(v) \in S$, modulo $998244353$. Mention the general vertex-weight product $(N-2)! [x^{N-2}] \prod_{i=1}^N \sum_{d \ge 1} w_i(d) \frac{x^{d-1}}{(d-1)!}$ inside the solution block.
6. **[Ch 04 Adv-2 (`#011`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L817-L830)**:
   - **Issue**: Splits into `1. Two-Array Sum of k-th Powers` and `2. M-Fold Roll Sum of k-th Powers (fps_24_q)`.
   - **Fix**: State `AtCoder fps_24_q — Dice` ($M$-fold roll sum of $k$-th powers $\sum_{(i_1,\dots,i_M)} (A_{i_1} + \dots + A_{i_M})^k \bmod 998244353$ for all $1 \le k \le K$) as the sole primary statement, and present the $M = 2$ two-array case as a warm-up inside the solution block.
7. **[Ch 10 Adv-2 (`#126`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd#L1070-L1079)**:
   - **Issue**: Line `1076` hedges with `"we decompose p into s minimal contiguous interval blocks (or cycle components via Foata's bijection) and count its ascents k..."`.
   - **Fix**: State the exact `Codeforces 1687F — Koishi's Unconscious Permutation` problem definition cleanly without parenthetical hedging, and present the equivalence inside Hint 1 / Solution Step 1.
8. **[Ch 11 SS-2 (`#200`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd#L905-L924)**:
   - **Issue**: Splits into `1. Task 1 (Single Power Coefficient)` and `2. Task 2 (Composite Sequence Extraction)`.
   - **Fix**: State the composite forest extraction $[x^N] \frac{1}{1 - F(x)}$ (or $[x^N] F(x)^k$ for given $N, k$) as the primary statement and treat the companion formula in the solution block.
9. **[Ch 13 Adv-2 (`#053`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd#L1307-L1328)**:
   - **Issue**: Splits into `1. Full Labeled Complete Graph Version (LOJ 6539, N <= 10^5)` and `2. Arbitrary Host Graph Version (ARC 105 F, N <= 17)` and introduces the problem via the parity invariant before stating the concrete monochromatic-edge-flip operation of `ARC 105 F / LOJ 6539`.
   - **Fix**: State the concrete monochromatic-edge-flip game on connected labeled graphs on $n \le 10^5$ vertices (`LOJ 6539`) as the primary problem statement outside `<details>`, derive the bipartite realization in Hint 1, and keep the $N \le 17$ arbitrary host graph version (`ARC 105 F`) as Part 2 of the solution block.
10. **[Ch 13 Mas-1 (`#122`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd#L1412-L1437)**:
    - **Issue**: Splits into `Part A (Symmetric Tournament & General Digraph Enumeration, N <= 10^5)` and `Part B (CF 1556F Non-Uniform Bradley–Terry Tournament, N <= 14)`.
    - **Fix**: State `Codeforces 1556F — Sports Betting` (the Bradley–Terry tournament expected winner count for $N \le 14$) as the primary statement, and present the $N \le 10^5$ symmetric tournament EGF $T(x) = 1/\Phi(-x)$ as the FPS scaling extension inside the solution block.
11. **[Ch 17 Adv-1 (`#015`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L1004-L1022)**:
    - **Issue**: Line `1012` writes `\mathcal{S}_{12} = \{ (\pm 1, 0), (0, \pm 1), (+2, +1), (+1, +2), (-2, -1), (-1, -2), (0, +1)\text{ [with multiplicity]}, \dots \}` with an ellipsis `\dots`.
    - **Fix**: Replace `L1010–L1016` with the exact, ellipsis-free 12-direction compound step specification: in each step, the walker takes one cardinal step $(dx_1, dy_1) \in \{(+1, 0), (-1, 0), (0, +1), (0, -1)\}$ followed by one diagonal-or-stay step $(dx_2, dy_2) \in \{(+1, +1), (0, 0), (-1, -1)\}$ ($4 \times 3 = 12$ transitions: $(+2, +1), (+1, +2), (-2, -1), (-1, -2)$ each with weight $1$, and $(+1, 0), (-1, 0), (0, +1), (0, -1)$ each with weight $2$), corresponding to $S(x, y) = (x + x^{-1} + y + y^{-1})(xy + 1 + x^{-1}y^{-1})$.
12. **[Ch 22 Int-1 (`#046`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd#L758-L782)**:
    - **Issue**: Lines `765–768` contain parenthetical hedging (`"scores a run with probability p_u (or chooses a subset of games...) ... or in the dual counting version..."`).
    - **Fix**: State the exact weighted tree DP polynomial problem cleanly: each vertex $u \in \{1, \dots, N\}$ has weight $w_u \in \mathbb{Z}_{\ge 1}$, local factor $(1 + p_u x^{w_u})$, and full-subtree bonus $c_u x^{\text{sz}_w[u]}$, defining $F_u(x) = c_u x^{\text{sz}_w[u]} + (1 + p_u x^{w_u}) \prod_{v \in \text{ch}(u)} F_v(x)$; compute $[x^0 \dots x^W] F_1(x) \bmod 998244353$.
13. **[Ch 23 Int-1 (`#233`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L652-L667)**:
    - **Issue**: Lines `658–660` hedge with `"(with r_3 = n or summed over r_3 when a 1-axis/slice-sum constraint...)"`.
    - **Fix**: State the exact 3D rank-product problem over $\mathbb{F}_2^n$ cleanly, and place the $r_3 = n$ specialization note inside Hint 1 / Solution Step 1.

---

## 5. Dimension 3 Audit: 3 Progressive `<details>` Hints & `<summary>` Standardization

### 5.1 Action Item 3.1 — Standardize `<summary>` Titles in `Ch 22` (`L613–L1247`)
- **File**: [ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd#L613-L1247)
- **Diagnostic Issue**: Across `Ch 01`–`Ch 21` and `Ch 23`–`Ch 24` (`184/192` problems), the 3 progressive `<details>` hints use the uniform textbook-wide `<summary>` labels:
  - `<summary>Hint 1 — Diagnostic Signal & Combinatorial Model</summary>`
  - `<summary>Hint 2 — Algebraic Setup & Reverse-Engineering Scratchpad</summary>`
  - `<summary>Hint 3 — Coefficient Extraction & Complexity Contract</summary>`
  - `<summary>Complete Derivation & Solution</summary>`
  In `Ch 22` (`8/8` problems, at lines `613, 619, 625`, `696, 702, 708`, `778, 784, 790`, `855, 861, 867`, `952, 958, 964`, `1049, 1055, 1061`, `1129, 1135, 1141`, `1235, 1241, 1247`), the `<summary>` tags use custom titles (`Hint 1 — Spoiler-Free Structural Observation`, `Hint 2 — Diagnostic Signal & Technique Selection`, `Hint 3 — Key Algebraic Equation...`).
- **Fix**: Replace those 24 `<summary>` lines in `chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd` with the standard 3-tier `<summary>` labels above.

---

## 6. Dimension 4 Audit: Complete Step-by-Step `<details>` Solutions & 5-Part `Algorithm Contract` Blocks

All `192/192` problems provide complete, multi-step derivations inside their 4th `<details>` block with zero hand-waving and zero raw template dumps. However, the `Algorithm Contract` block at the end of the 4th `<details>` solution block exhibits three distinct levels of completeness across the 24 chapters:

1. **Tier A — Strictly Compliant 5-Part `Algorithm Contract` (`56` problems in `Ch 02, 05, 10, 11, 22, 23, 24`)**:
   - Explicitly states all 5 required parts: (1) `Input & Preconditions`, (2) `Postconditions (Output)`, (3) `Time & Space Complexity`, (4) `Loop / Algebraic Invariant`, and (5) `Failure Modes & Edge Cases` (or `Index & Truncation Boundaries`).
2. **Tier B — Abbreviated / Partial Contract (`48` problems in `Ch 01, 03, 04, 06, 07, 08` — HIGH PRIORITY ACTION)**:
   - **`Ch 01`** (`8` problems: `L605–L608`, `L690–L694`, `L774–L778`, `L847–L851`, `L928–L932`, `L1008–L1012`, `L1112–L1116`, `L1224–L1228`): Contains only a 1-sentence `#### 5. Complexity Contract` (missing `Input & Preconditions`, `Postconditions (Output)`, `Loop / Algebraic Invariant`, and `Failure Modes & Edge Cases`).
   - **`Ch 03`** (`8` problems: `L987`, `L1060`, `L1125`, `L1196`, `L1259`, `L1335`, `L1410`, `L1498`): Contains only a single `- **Complexity**: ...` bullet at the end of the solution (missing `Input & Preconditions`, `Postconditions (Output)`, `Loop / Algebraic Invariant`, and `Failure Modes & Edge Cases`).
   - **`Ch 04`** (`8` problems: `L480–L494`, `L562–L576`, `L642–L655`, `L716–L729`, `L799–L812`, `L898–L911`, `L979–L992`, `L1093–L1106`): Contains `Preconditions`, `Postcondition`, `Algorithm Steps`, `Time Complexity`, `Space Complexity`, but omits `Loop / Algebraic Invariant` and `Failure Modes & Edge Cases`.
   - **`Ch 06`** (`8` problems: `L838–L846`, `L909–L917`, `L984–L992`, `L1066–L1074`, `L1147–L1155`, `L1220–L1228`, `L1305–L1313`, `L1382–L1390`): Contains `Hand-Checkable Trace`, `Boundary Cases`, `Complexity`, but omits `Input & Preconditions`, `Postconditions (Output)`, and `Loop / Algebraic Invariant`.
   - **`Ch 07`** (`8` problems: `L773–L784`, `L888–L899`, `L991–L1002`, `L1090–L1101`, `L1203–L1214`, `L1327–L1338`, `L1463–L1474`, `L1600–L1611`): Contains `Hand-Checkable Trace`, `Preconditions`, `Postconditions`, `Complexity`, but omits `Loop / Algebraic Invariant` and `Failure Modes & Edge Cases`.
   - **`Ch 08`** (`8` problems: `L655–L663`, `L735–L743`, `L822–L830`, `L899–L907`, `L995–L1003`, `L1080–L1088`, `L1188–L1196`, `L1288–L1296`): Contains `Preconditions`, `Postconditions`, `Core Invariant`, `Time Complexity`, `Space Complexity`, omitting an explicit `Failure Modes & Edge Cases` bullet inside `#### 5. Algorithm & Complexity Contract`.
3. **Tier C — 5-Bullet Callouts Missing 5th Conceptual Part (`88` problems in `Ch 09` and `Ch 12`–`Ch 21` — MEDIUM PRIORITY ACTION)**:
   - In `Ch 09`, `Ch 12`, `Ch 13`, `Ch 14`, `Ch 15`, `Ch 16`, `Ch 17 (P1–P2)`, `Ch 18`, `Ch 19`, `Ch 20`, and `Ch 21`, the `Algorithm Contract` block has 5 bullets because `Input` and `Preconditions` were split into 2 separate bullets (`Input`, `Preconditions`, `Postconditions (Output)`, `Time & Space Complexity`, `Loop / Algebraic Invariant`), leaving out an explicit `Failure Modes & Edge Cases` bullet inside the contract block.
   - Conversely, in `Ch 17 (P3–P8)` (`L897–L906`, `L990–L999`, `L1096–L1105`, `L1178–L1187`, `L1284–L1293`, `L1390–L1399`), the 5 bullets are `Input`, `Preconditions`, `Postconditions`, `Complexity`, and `Failure Modes & Edge Cases`, omitting `Loop / Algebraic Invariant`.
   - **Fix**: Add `- **Failure Modes & Edge Cases**: ...` to the contract blocks in `Ch 09`, `Ch 12`–`Ch 16`, `Ch 17 (P1–P2)`, and `Ch 18`–`Ch 21`, and add `- **Loop / Algebraic Invariant**: ...` to `Ch 17 (P3–P8)`.

---

## 7. Prioritized Action Plan for Remediation

1. **Priority 1 (Prerequisite Closure & Canonical Problem Match — `1` problem)**:
   - Apply **Action Item 1.1** to `chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd` (`L805–L886`, `#244 yukicoder 3029: Colored Tree`) so that the 2-Colored Rooted Tree coupled system is the primary statement and the `Ch 12` Cactus forward-reference is removed.
2. **Priority 2 (Visible Hand-Checkable Sample Traces Outside `<details>` in Part I — `32` problems)**:
   - Apply **Action Item 2.1** across `Ch 01` (`8` problems), `Ch 02` (`8` problems), `Ch 03` (`8` problems), and `Ch 04` (`8` problems) so that 100% (`192/192`) of ladder problems in the textbook have a visible sample trace ($N \le 4$) before the first `<details>` tag.
3. **Priority 3 (Unify Split / Hedged Problem Statements — `13` problems)**:
   - Apply **Action Item 2.2** to unify the `13` split/hedged problem statements in `Ch 02 SS-2`, `Ch 03 SS-1`, `Ch 03 Mas-2`, `Ch 04 SS-2`, `Ch 04 Int-2`, `Ch 04 Adv-2`, `Ch 10 Adv-2`, `Ch 11 SS-2`, `Ch 13 Adv-2`, `Ch 13 Mas-1`, `Ch 17 Adv-1`, `Ch 22 Int-1`, and `Ch 23 Int-1`.
4. **Priority 4 (Upgrade Abbreviated Algorithm Contracts & Standardize `Ch 22` Hint Summaries)**:
   - Apply **Action Item 3.1** to standardize the 24 hint `<summary>` headers in `Ch 22`.
   - Apply **Action Item 4.1** to upgrade the abbreviated contracts in `Ch 01, 03, 04, 06, 07, 08` (`48` problems) and **Action Item 4.2** to append the 5th conceptual bullet (`Failure Modes & Edge Cases` / `Invariant`) in `Ch 09` and `Ch 12`–`Ch 21`.
