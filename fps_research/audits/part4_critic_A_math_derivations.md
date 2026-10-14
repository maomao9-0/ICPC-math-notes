# Part IV Critic A Audit Report — Mathematical Rigor, Single-Step Derivations & Zero-Magic Scratchpads (Chapters 14–17 & Checkpoint IV)

- **Auditor**: Part IV Critic A (Mathematical Rigor, Single-Step Derivations & Zero-Magic Scratchpad Auditor)
- **Audited Files**:
  1. [`chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd) (1,305 lines)
  2. [`chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd) (1,376 lines)
  3. [`chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd) (1,374 lines)
  4. [`chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd) (1,259 lines)
  5. [`checkpoints/cp04-part4-pgf-walks-multivariate.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd) (902 lines)
- **Reference Standards**: `AGENTS.md`, `fps_research/CURRICULUM_ARCHITECTURE.md`, `fps_research/PROBLEM_CURATION.md`, `fps_research/TECHNIQUE_TAXONOMY.md`, `fps_research/problem_archive.md`.

---

## Executive Summary & Audit Verdict

Across the 6,216 lines of Part IV (`Chapters 14–17` and `Checkpoint IV`), the core mathematical exposition, single-step derivations, reverse-engineering scratchpads, hand-checkable numerical walkthroughs, and 40 problem solutions (`32` chapter ladder problems + `8` blind checkpoint problems) are at a remarkably high standard. Every single-step derivation in the main text and collapsible solutions was checked line by line and verified numerically.

At the same time, our line-by-line mathematical audit uncovered **6 genuine mathematical / boundary formula bugs**, **2 raw `"Wait:"` self-correction monologues**, **5 missing Revisited Dual-Perspective Cross-References (`CURRICULUM_ARCHITECTURE.md` §5.2)**, and **several stale chapter numbers / broken `.qmd` cross-links** from earlier curriculum drafts. Every single defect is cataloged below with exact line numbers and drop-in replacement blocks.

| File | Mathematical & Boundary Bugs | `"Wait:"` Monologues | Missing Revisited Cross-Refs (§5.2) | Stale Ch. Numbers / Broken `.qmd` Links |
| :--- | :-: | :-: | :-: | :-: |
| **`ch14-pgf-stopping-times-renewal-poisson-martingales.qmd`** | **0** | **0** | **1** (`#3`/`#10`: `Ch 08 §8.4` Goulden–Jackson $\leftrightarrow$ `Ch 14 §14.4` Guibas–Odlyzko) | **1** (Line 1298 broken link to `ch15`) |
| **`ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`** | **1** (Line 1296: $F_{-1}(z)=0$ instead of $F_{-1}(z)=1$ in `Mas-2 #210` Hint 2) | **0** | **1** (`#9`: `Mas-2 #210` $\leftrightarrow$ `Ch 11 §11.4` Catalytic Tree Shift & `Ch 05`) | **2** (Lines 8–9, 385, 392–393 stale Ch 5 / Ch 10 refs) |
| **`ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`** | **2** (Line 386 & Lines 1269, 1304–1305: false second expression for $\chi(I)$ when $n_r \not\equiv 1 \pmod d$; Line 672: wrong coefficients $3t(27t-1)D_3'' + (108t-1)D_3'$ instead of $t(27t-1)D_3'' + (54t-1)D_3'$ in ODE for $D_3(t)$) | **0** | **2** (`#4`: `Adv-2 #074` $\leftrightarrow$ `Ch 08 §8.2/§8.4`; `#10`: `Adv-1 #237` $\leftrightarrow$ `Ch 18 §18.2`) | **1** (Lines 8–11 stale Ch 7 / Ch 15 refs & broken `.qmd` links) |
| **`ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`** | **2** (Line 681: binary index $v = 2j + 2k + l$ instead of $v = 4j + 2k + l$ in `SS-2 #044`; Lines 1203 & 1231: wrong carry-grading formula $\chi = (e_1+e_2+e_3) \bmod 3$ in `Mas-2 #234`) | **1** (Line 686: `(Wait: if all u initially...)`) | **0** (`#5` and `#11` are present and verified) | **2** (Lines 11–14, 200, 1172, 1203, 1231 stale Ch 13 / Ch 15 refs & broken `.qmd` links) |
| **`cp04-part4-pgf-walks-multivariate.qmd`** | **1** (Line 79 & Line 555: wrong sign $dp[0][0] = -1$ instead of $dp[0][0] = 1$ in `CP-IV.1 #158`) | **1** (Line 557: `-1 - 0 = -1? Wait: we want +1...`) | **1** (`#12`: `CP-IV.6 #058` $\leftrightarrow$ `Ch 18 §18.2` $O(N)$ D-Finite Krawtchouk) | **0** |

---

## Chapter 14 Audit: `ch14-pgf-stopping-times-renewal-poisson-martingales.qmd`

### 1. Mathematical & Pedagogical Verification Summary
- **§14.1 (`PGF Fundamentals, Tail-Sum Identity & Factorial Moments`)**:
  - Verified $F(z) + (1-z)G(z) = 1$, $\mathbb{E}[T] = F'(1) = G(1)$, $\mathbb{E}[T^{\underline{k}}] = F^{(k)}(1) = k G^{(k-1)}(1)$, and $\operatorname{Var}(T) = F''(1) + F'(1) - (F'(1))^2 = 2G'(1) + G(1) - G(1)^2$.
  - Verified the formal algebraic justification of $F(z) + (1-z)G(z) = 1$ via coefficient extraction $[z^n]$ for $n=0$ and $n \ge 1$ (lines 61–69).
- **§14.2 (`Evaluating Rational PGFs at z = 1 via Formal Taylor Shift`)**:
  - Verified the substitution $z = 1 + t \bmod t^3$, the pole-cancellation valuation shift $\widetilde{P}(t) = P(1+t)/t^v$, $\widetilde{Q}(t) = Q(1+t)/t^v$, and the explicit $O(1)$ truncated division formulas for $\mathbb{E}[T] = p_1 - q_1$ and $\operatorname{Var}(T) = 2(p_2 - q_2 - q_1(p_1 - q_1)) + (p_1 - q_1) - (p_1 - q_1)^2$ (lines 171–208).
  - Verified **Canonical Failure Mode #13** (lines 136–154) and the worked trace on $T \sim \operatorname{Geom}(p)$ (lines 212–233).
- **§14.3 (`Renewal Equations, First-Passage Deconvolution & Poissonization`)**:
  - Verified the renewal decomposition $H_{u \to v}(z) = F_{u \to v}(z) H_{v \to v}(z)$, the $(1-z)$ pole-cancellation identity $F_{u \to v}(z) = \frac{(1-z)H_{u \to v}(z)}{(1-z)H_{v \to v}(z)}$, and the hypercube parity EGF + Borel transform derivation (lines 240–337).
- **§14.4 (`Pattern Waiting Times, Optional Stopping & Martingale Potentials`)**:
  - Verified Li's gambling martingale potential $\Phi_{\text{Li}}(S) = \sum_{j=1}^{|S|} [S_{1..j} = S_{|S|-j+1..|S|}] \sigma^j$, the Single-Pattern KMP Border Theorem $\mathbb{E}[T_S] = \Phi_{\text{Li}}(S)$, the Multi-Pattern Guibas–Odlyzko system $C(1)\mathbf{p} = G(1)\mathbf{1}$ & $\sum_{j=1}^k p_j = 1$, and the Additively Separable Martingale Potential $\Phi(X) = \sum f(a_i)$ with gauge-fixing $f(1)$ and first-difference order reduction $g(s) = f(s+1) - f(s)$ (lines 341–566).
- **8-Problem Ladder (`SS-1 #155`, `SS-2 #176`, `Int-1 #156`, `Int-2 #170`, `Adv-1 #148`, `Adv-2 #212`, `Mas-1 #091`, `Mas-2 #112`)**:
  - All 8 problems match `CURRICULUM_ARCHITECTURE.md` 100%, and every hand trace and derivation step is mathematically sound.

### 2. Required Fixes in `ch14-pgf-stopping-times-renewal-poisson-martingales.qmd`

#### Defect Ch14-1: Missing Revisited Dual-Perspective Cross-Reference (`#3` / `#10` in `CURRICULUM_ARCHITECTURE.md` §5.2) Connecting `Ch 08 (§8.4)` Goulden–Jackson Cluster Method to `Ch 14 (§14.4)` Guibas–Odlyzko Waiting Times
- **Location**: [`chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd#L455-L463) (end of §14.4 Part B, and echoed in `Int-1 #156` / `Adv-1 #148`).
- **Issue**: `CURRICULUM_ARCHITECTURE.md` §5.2 mandates an explicit Revisited Dual-Perspective Cross-Reference showing how the deterministic Goulden–Jackson forbidden-substring cluster matrix $(I + C(x))$ from Chapter 08 (§8.4) becomes the stochastic Guibas–Odlyzko stopping-time system $C(1)\mathbf{p} = G(1)\mathbf{1}$ upon substituting $x = z/\sigma$ and evaluating at $z = 1$.
- **Drop-In Fix (Lines 455–463)**:
```markdown
   This gives $k + 1$ linear equations in the $k + 1$ unknowns $(p_1, \dots, p_k, G(1))$:
   $$\begin{cases}
   \displaystyle \sum_{j=1}^{k} C_{j, i}(1)\, p_j = G(1) & \text{for } i = 1, 2, \dots, k, \\[8pt]
   \displaystyle \sum_{j=1}^{k} p_j = 1.
   \end{cases}$$
   Solving this $(k + 1) \times (k + 1)$ linear system in $O(k^3)$ time simultaneously determines every pattern's winning probability $p_j$ and the expected stopping time $\mathbb{E}[T] = G(1)$!

::: {.callout-note}
## Revisited Dual-Perspective Cross-Reference — From Goulden–Jackson Clusters (`Ch 08 §8.4`) to Guibas–Odlyzko Martingales (`Ch 14 §14.4`)
In **[Chapter 08 (§8.4: The Goulden–Jackson Cluster Method)](ch08-connected-component-ie-rook-goulden-jackson.qmd)**, we counted deterministic $n$-letter strings over an alphabet of size $\sigma$ avoiding a reduced pattern set $\{S_1, \dots, S_k\}$ via the cluster matrix $I + C_{\text{GJ}}(x)$, where the overlap polynomial was weighted by $x^{|S_i| - r}$.

How does that deterministic counting matrix become the stochastic system above? Dividing every $n$-letter string count by $\sigma^n$ corresponds to the **probabilistic scaling substitution $x \leftarrow z / \sigma$**! Under $x = z / \sigma$:
1. The deterministic unstopped word enumerator becomes the survival PGF $G(z) = \sum_{n \ge 0} \mathbb{P}(T > n) z^n$.
2. The Goulden–Jackson overlap polynomial between $S_j$ and $S_i$ becomes $(z/\sigma)^{|S_i|} C_{j, i}(z)$, where $C_{j, i}(z) = \sum_{r \in \operatorname{Border}(S_j, S_i)} \sigma^r z^{-r}$.
3. Evaluating at $z = 1$ (so $x = 1/\sigma$) turns the deterministic cluster inversion into the stochastic Guibas–Odlyzko linear system $\sum_{j=1}^k C_{j, i}(1) p_j = G(1)$ for both `Int-1 (#156 — SDOI2017 硬币游戏)` and `Adv-1 (#148 — JSOI2009 有趣的游戏)`!
:::
```

#### Defect Ch14-2: Broken Internal `.qmd` Link to Chapter 15 at Line 1298
- **Location**: [`chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd#L1298)
- **Issue**: Line 1298 links to `(ch15-lattice-walks-reflection-kernel-method.qmd)`, whereas the actual file in `chapters/` is `ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`.
- **Drop-In Fix (Line 1298)**:
```markdown
Before moving to [Chapter 15: 1D Lattice Walks, Reflection Principle & Small-Root Kernel Method](ch15-1d-lattice-walks-chebyshev-kernel-method.qmd), verify that you can execute each of the following without hesitation:
```

---

## Chapter 15 Audit: `ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`

### 1. Mathematical & Pedagogical Verification Summary
- **§15.1 (`Unconstrained vs. Constrained 1D Lattice Walks & André's Reflection Principle`)**:
  - Verified the formal step-set OGF $W(x, y) = \frac{1}{1 - x S(y)} \in \mathbb{Q}[y, y^{-1}][[x]]$, the first-hitting reflection bijection, the general ballot theorem $[x^n] y^{\Delta} \mathcal{C}(x) = \frac{\Delta + 1}{k + \Delta + 1}\binom{2k + \Delta}{k}$, and **Canonical Failure Mode #14** (asymmetric step sets break reflection; lines 113–129).
- **§15.2 (`Two Absorbing Boundaries, Method of Images & Chebyshev Polynomials`)**:
  - Verified the dihedral reflection group $D_\infty = \langle r_1, r_2 \rangle$ on $[-1, H+1]$ with period $L = H+2$, the signed Method of Images orbit sum (Theorem 15.1), the tridiagonal Chebyshev transfer determinant $U_k\!\left(\frac{1}{2x}\right) x^k$, and the discrete Fourier diagonalization (Theorem 15.2).
- **§15.3 (`The 1D Kernel Method: Small vs. Large Roots & Multi-Root Symmetric Elimination`)**:
  - Verified the Formal Laurent Ring Substitution Theorem (Theorem 15.3: $y = y_0(x)$ is valid in $K[y][[x]]$ when $\operatorname{val}_x(y_0) \ge 1$, and invalid in $K[[y, y^{-1}]][[x]]$), Regimes A ($k=1$), B ($k \ge 2$ small roots via Newton–Girard), and C ($m=1$ positive step via Vieta's product at the single large root $y_L(x)$), and the Formal Residue Change-of-Variables derivation of $[x^n] C(x)^r$ via $x = u/(1+u)^2$ (lines 397–441).
- **§15.4 (`Łukasiewicz Walks & Raney's Cycle Lemma`)**:
  - Verified Theorem 15.4 (Raney's Cycle Lemma), the algebraic equivalence with Form 2 of Lagrange Inversion, and all 8 ladder problems (`SS-1 #178`, `SS-2 #104`, `Int-1 #129`, `Int-2 #188`, `Adv-1 #165`, `Adv-2 #069`, `Mas-1 #202`, `Mas-2 #210`).

### 2. Required Fixes in `ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`

#### Defect Ch15-1: Mathematical Base-Case Error ($F_{-1}(z) = 0$ Instead of $F_{-1}(z) = 1$) in `Mas-2 #210` Hint 2
- **Location**: [`chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L1294-L1299)
- **Issue**: Line 1296 in Hint 2 writes:
  $$F_k(z) = 1 + z F_{k-1}(z) F_k(z) \quad \Longrightarrow \quad F_k(z) = \frac{1}{1 - z F_{k-1}(z)} \qquad (k \ge 0,\ F_{-1}(z) = 0).$$
  If $F_{-1}(z) = 0$, then $F_0(z) = \frac{1}{1 - 0} = 1$, which counts only the empty tree instead of right-comb trees of height $0$ ($F_0(z) = \frac{1}{1-z}$), shifting all Chebyshev continuant indices $Q_m(z) / Q_{m+1}(z)$ by $1$! As the full derivation on line 1326 rightly explains, the empty tree is always valid ($[z^0] F_{-1}(z) = 1$), so **$F_{-1}(z) = 1$** (giving $F_0(z) = \frac{1}{1-z} = \frac{Q_1(z)}{Q_2(z)}$).
- **Drop-In Fix (Lines 1294–1299)**:
```markdown
Let $F_k(z)$ be the OGF of valid binary trees (including the empty tree $1$) whose maximum left-step depth is at most $k$ (equivalently, Dyck paths starting at height $0$ and staying in $[0, k+1]$). Since the root's left subtree has left-depth budget $k - 1$ and its right subtree keeps budget $k$:
$$F_k(z) = 1 + z F_{k-1}(z) F_k(z) \quad \Longrightarrow \quad F_k(z) = \frac{1}{1 - z F_{k-1}(z)} \qquad (k \ge 0,\ F_{-1}(z) = 1).$$
For $L(T) \le m$ on $n$ non-empty vertices, the root itself sits at $d_L(\text{root}) = 1$, so the non-empty tree has OGF $F_{m-1}(z) - 1$, and we want $[z^n] F_{m-1}(z)$!
```

#### Defect Ch15-2: Missing Revisited Dual-Perspective Cross-Reference (`#9` in `CURRICULUM_ARCHITECTURE.md` §5.2) in `Mas-2 #210` (`UOJ 424 — count`)
- **Location**: [`chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L1342-L1353)
- **Issue**: `CURRICULUM_ARCHITECTURE.md` §5.2 (`#9`) specifies that `#210 (UOJ 424 — count)` must cross-reference its dual perspective from `Ch 11 (§11.4)` (Catalytic Tree Shift $F_k = 1 + x F_{k-1} F_k$ & `Ch 05` Bostan–Mori) alongside the `Ch 15 (§15.2)` Two-Boundary Reflection / Chebyshev Transfer $U_m$.
- **Drop-In Fix (Lines 1342–1353)**:
```markdown
4. **Regime Dispatch (`fps_inv` vs. Bostan–Mori)**:
   - **Regime 1 ($n \le 10^5$, arbitrary $m$)**: Compute $Q_{m+1}(z) \bmod z^{n+1}$ by reading its $\lfloor (m+1)/2 \rfloor$ nonzero binomial coefficients up to degree $\min(m + 1, n)$, invert $Q_{m+1}(z) \bmod z^{n+1}$ in $O(n \log n)$ time via `fps_inv`, and take the inner product with $Q_m(z)$! (Even simpler: when $m > n$, the ceiling $m + 1$ can never be reached in $n$ steps, so the answer is simply the unconstrained Catalan number $C_n = \frac{1}{n+1}\binom{2n}{n}$ in $O(n)$ time!)
   - **Regime 2 ($m \le 10^5$, huge $n \le 10^{18}$)**: Construct the explicit polynomials $Q_m(z)$ and $Q_{m+1}(z)$ of degree $\le \lceil m/2 \rceil$ in $O(m)$ time, and extract $[z^n] \frac{Q_m(z)}{Q_{m+1}(z)}$ via **Bostan–Mori** in $O(m \log m \log n)$ time!

::: {.callout-note}
## Revisited Dual-Perspective Cross-Reference — Catalytic Tree Shift (`Ch 11 §11.4`) vs. Two-Boundary Walk Reflection (`Ch 15 §15.2`)
In **[Chapter 11 (§11.4)](ch11-laurent-residues-raney-lagrange-inversion.qmd)**, we viewed $F_k(z) = 1 + z F_{k-1}(z) F_k(z)$ through the lens of **root-subtree catalytic decomposition**,linearizing the fractional linear Möbius map $F_k = \frac{1}{1 - z F_{k-1}}$ via $2 \times 2$ matrices. Here in **Chapter 15 (§15.2)**, the exact same rational function $F_{m-1}(z) = \frac{Q_m(z)}{Q_{m+1}(z)}$ emerges geometrically from the **Two-Boundary Method of Images (Theorem 15.1)** and **Chebyshev Transfer Determinant (Theorem 15.2)** on Dyck paths in $[0, m]$. Whenever a tree depth constraint and a bounded-strip lattice walk share the same Chebyshev continuant $Q_{m+1}(z) = \sum_{j \ge 0} (-1)^j \binom{m+1-j}{j} z^j$, you can freely switch between the Method of Images orbit sum ($O(n/m)$ binomial evaluations) and rational coefficient extraction (`Ch 01` `fps_inv` or `Ch 05` Bostan–Mori)!
:::

- **Complexity**: $O(\min(n, m) \log \min(n, m))$ time (or $O(n)$ via the Method of Images sum of $\lfloor n/(m+2) \rfloor$ binomial terms) and $O(n)$ space.
```

#### Defect Ch15-3: Stale Chapter References (`Chapter 5` for `fps_inv`/`fps_sqrt`/`fps_exp` and `Chapter 10` for `Bostan–Mori`)
- **Location**: [`chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L6-L10) and [lines 385–393](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L385-L393).
- **Issue**:
  - Lines 8–9 refer to `Chapter 5 (fps_inv, fps_sqrt, fps_exp)` (actually **Chapters 1–2**) and `Chapter 10 (Bostan–Mori & Linear Recurrences)` (actually **Chapter 5**).
  - Lines 385, 392, 393 in the §15.3B table refer to `fps_inv (Ch 05)` and `Bostan–Mori (Ch 10)`.
- **Drop-In Fix (Lines 6–11)**:
```markdown
## Prerequisites & Core Toolkit from Earlier Chapters
- **[Chapters 01–02 (Ring Convolutions, `fps_inv`, `fps_sqrt`, `fps_exp`)](ch01-ring-convolutions-newton-inv.qmd)**: Polynomial inversion, square roots, and logarithmic/exponential operations modulo $x^N$.
- **[Chapter 05 (Rational GFs, Bostan–Mori & Linear Recurrences)](ch05-rational-bostan-mori-berlekamp-massey.qmd)**: Extracting $[x^N] P(x)/Q(x)$ in $O(d \log d \log N)$ time.
- **[Chapter 07 (Roots of Unity Filter & Bluestein's CZT)](ch07-roots-of-unity-cyclotomic-czt.qmd)**: Extracting arithmetic progressions of exponents modulo $L$.
- **[Chapter 11 (Formal Laurent Series, Formal Residues & Lagrange Inversion)](ch11-laurent-residues-raney-lagrange-inversion.qmd)**: The residue operator $[u^{-1}]$, the formal change-of-variables law, and Lagrange Inversion Forms 1 & 2.
```
- **Drop-In Fix (Lines 383–394)**:
```markdown
| Step Set Bounds $(k, m)$ | Unknowns & Small Roots | Elimination Strategy | Extraction Engine for $[x^n]$ |
| :--- | :--- | :--- | :--- |
| **$k = 1, m = 1$** (Motzkin / Dyck) | $1$ boundary $F_0(x)$; $1$ small root $y_0(x)$ | Quadratic formula for $y_0(x)$; $F_0(x) = y_0(x) / (x w_{-1})$ | Closed-form binomial sum or `fps_sqrt` (`Ch 02`) in $O(n \log n)$ |
| **$k = 1, m \ge 2$** (Łukasiewicz) | $1$ boundary $F_0(x)$; $1$ small root $y_0(x)$ | $y_0(x) = x \Phi(y_0(x))$; $F_0(x) = y_0(x) / (x w_{-1})$ | Lagrange Inversion (`Ch 11`) in $O(n \log n)$ |
| **$k \ge 2, m \ge 2$** (General Bounded) | $k$ boundaries $F_0, \dots, F_{k-1}$; $k$ small roots $y_1, \dots, y_k$ |Symmetric elimination or $k \times k$ Vandermonde system | Coupled Newton / D-Finite ODE (`Ch 10` / `Ch 18`) |
| **$k \ge 2, m = 1$** ($1$ Positive Step) | $k$ boundaries, **Eliminate via $1$ Large Root $y_L(x)$** | Substitute $y = y_L(x)$ into $[y^{\le k-1}] K(x, y) F(x, y)$ | Lagrange Inversion at $y_L(x)$ (`Ch 11`) in $O(n \log n)$ |
| **Bounded Strip $[0, H]$**, $k=m=1$ | $2$ boundaries $F_0(x), F_H(x)$ | Method of Images / Chebyshev $U_H$ rational fraction | `fps_inv` (`Ch 01`) for $n \le 10^5$; Bostan–Mori (`Ch 05`) for $n \le 10^{18}$ |
| **Bounded Strip $[0, H]$**, general $k, m$ | $k + m$ boundaries | $H \times H$ Transfer Matrix / Companion Polynomial | Bostan–Mori (`Ch 05`) in $O(H \log H \log n)$ |
```

---

## Chapter 16 Audit: `ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`

### 1. Mathematical & Pedagogical Verification Summary
- **§16.1 (`The Five-Ring Multivariate Hierarchy & Pivot Variable Method`)**:
  - Verified the distinct algebraic properties of $K[x,y]$, $K[y][[x]]$, $K[[x]][y]$, $K[[x,y]]$, and $K((x))((y)) \neq K((y))((x))$ (Example 16.1: $\frac{1}{x-y}$ has $[x^0 y^0]=0$ in both, but opposite signs on $x^{-k} y^{k-1}$).
  - Verified the Pivot Variable Method (`主元法`) and all 3 steps of `Bivariate Exp` via `Ch 09` CDQ-FFT (lines 97–156).
- **§16.2 (`2D Bostan–Mori & All 4 Regimes of [x^N y^K] P(x,y)/Q(x,y)`)**:
  - Verified the degree growth analysis ($d_y^{(t)} = 2^t d_y$, $d_x^{(t)} \le d_x$), the $O(d_x K \log(d_x K) + K \log K \log N)$ complexity of `bivariate_bostan_mori`, all 4 regimes (A, B, C, D), and the sparse partial-step elimination $x = \text{poly}(y)$ (lines 160–345).
- **§16.3 (`Multivariate Truncated Convolutions: Chi-Twisted Kronecker FFT`)**:
  - Verified the proof of Theorem 16.1 using $\chi(I) = \left(\sum_{r=1}^{d-1} \lfloor I / N_r \rfloor\right) \bmod d$ (lines 393–408), the worked trace on $(1 + x + y)^2 \bmod (x^2, y^2)$ (lines 410–426), and the C++ implementation `multivariate_truncated_mul` (lines 433–489). *(See Defect Ch16-1 below for the false second equality on line 386 and in `Mas-2 #214`.)*
- **§16.4 (`Bivariate Diagonals, Furstenberg's Theorem & Lipshitz's Theorem`)**:
  - Verified Furstenberg's Diagonal Theorem (Theorem 16.2, Direction 1 & Direction 2), the 1-Line Quadratic Denominator Shortcut (Corollary 16.1), **Canonical Failure Mode #15** (forgetting the $z=0$ pole when $a \ge p$, lines 572–593), and Lipshitz's Theorem (Theorem 16.3, lines 639–693). *(See Defect Ch16-2 below for the coefficient error in the differential equation for $D_3(t)$ at line 672.)*
- **8-Problem Ladder (`SS-1 #128`, `SS-2 #191`, `Int-1 #050`, `Int-2 #126`, `Adv-1 #237`, `Adv-2 #074`, `Mas-1 #215`, `Mas-2 #214`)**:
  - Verified all 8 problems against `CURRICULUM_ARCHITECTURE.md`.

### 2. Required Fixes in `ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`

#### Defect Ch16-1 (CRITICAL MATH BUG): False Second Formula for the Carry-Grading Function $\chi(I)$ in Theorem 16.1 (Line 386) and `Mas-2 #214` (Lines 1269, 1304–1305)
- **Location**: [`chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L384-L388) and [lines 1268–1271, 1303–1307](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L1268-L1307).
- **Mathematical Proof of Bug**:
  - Line 386 writes:
    $$\chi(I) := \left( \sum_{r=1}^{d-1} \left\lfloor \frac{I}{N_r} \right\rfloor \right) \bmod d = \left( \sum_{r=2}^{d} (r - 1) \, i_r \right) \bmod d.$$
  - The **first expression** $\chi(I) := \left( \sum_{r=1}^{d-1} \left\lfloor \frac{I}{N_r} \right\rfloor \right) \bmod d$ (which is what the proof on lines 393–408 and the C++ implementations on lines 449 and 1328 actually use!) is **100% mathematically true** for all radix bases $n_1, \dots, n_d$.
  - However, the **second equality** $= \left(\sum_{r=2}^d (r-1) i_r\right) \bmod d$ is **MATHEMATICALLY FALSE** whenever $n_r \not\equiv 1 \pmod d$!
  - Why? Because for $I = i_1 + i_2 N_1 + i_3 N_2 + \dots + i_d N_{d-1}$, the quotient $\lfloor I / N_r \rfloor$ is:
    $$\left\lfloor \frac{I}{N_r} \right\rfloor = i_{r+1} + i_{r+2} n_{r+1} + i_{r+3} n_{r+1} n_{r+2} + \dots + i_d \prod_{s=r+1}^{d-1} n_s,$$
    which equals $\sum_{s=r+1}^d i_s$ ONLY if $n_{r+1} = n_{r+2} = \dots = 1$!
  - **Concrete Counterexample ($d = 3, A = B = C = 1 \implies n_1 = n_2 = n_3 = 2, N_1 = 2, N_2 = 4$, the exact walkthrough of `Mas-2 #214`)**:
    - True formula: $\chi(I) = \big(\lfloor I/2 \rfloor + \lfloor I/4 \rfloor\big) \bmod 3 = \big((b + 2c) + c\big) \bmod 3 = (b + 3c) \bmod 3 = b \bmod 3$.
    - Consider multiplying $y \cdot y = y^2$, i.e., $(a, b, c) = (0, 1, 0)$ with $(a', b', c') = (0, 1, 0)$:
      Here $I = 2$ and $I' = 2$, so $I + I' = 4$, which decodes in base $(2, 2, 2)$ to $(a'', b'', c'') = (0, 0, 1)$ (a spurious carry from $y^2$ into $z^1$!).
      - Under the **true** $\chi(I) = (\lfloor I/2 \rfloor + \lfloor I/4 \rfloor) \bmod 3$: $\chi(2) + \chi(2) = 1 + 1 = 2 \not\equiv \chi(4) = 2$? Wait: $\lfloor 2/2 \rfloor + \lfloor 2/4 \rfloor = 1 + 0 = 1$, so $\chi(2) + \chi(2) = 2$, whereas $\lfloor 4/2 \rfloor + \lfloor 4/4 \rfloor = 2 + 1 = 3 \equiv 0 \pmod 3 \neq 2$! The true $\chi(I)$ **successfully detects the carry** ($2 \not\equiv 0 \pmod 3$)!
      - Under the **false** formula $\tilde{\chi}(a, b, c) = (b + 2c) \bmod 3$ (line 386 and line 1304): $\tilde{\chi}(0, 1, 0) + \tilde{\chi}(0, 1, 0) = 1 + 1 = 2$, and for the carried result $(0, 0, 1)$, $\tilde{\chi}(0, 0, 1) = 0 + 2(1) = 2$! So $\tilde{\chi}(I) + \tilde{\chi}(I') \equiv \tilde{\chi}(I + I') \pmod 3$, **failing to reject the spurious carry $y^2 \mapsto z$**!
      - And under the **false** formula $\hat{\chi}(a, b, c) = (b + c) \bmod 3$ (written in Hint 2 at line 1269): multiplying $xy \cdot x$ has $(1, 1, 0) + (1, 0, 0) = 3 + 1 = 4 \mapsto (0, 0, 1)$, where $\hat{\chi}(1, 1, 0) + \hat{\chi}(1, 0, 0) = 1 + 0 = 1 = \hat{\chi}(0, 0, 1)$, **failing to reject the spurious carry $x^2 y \mapsto z$**!
- **Drop-In Fix 1 (Theorem 16.1, Lines 383–390)**:
```markdown
**Theorem 16.1 ($\chi$-Twisted Kronecker Multiplication).** *Define the **carry-grading function** $\chi : \{0, 1, \dots, N - 1\} \to \mathbb{Z}_d$ by:*

$$\chi(I) := \left( \sum_{r=1}^{d-1} \left\lfloor \frac{I}{N_r} \right\rfloor \right) \bmod d = \left( \sum_{s=2}^{d} i_s \sum_{r=1}^{s-1} \frac{N_{s-1}}{N_r} \right) \bmod d.$$

*For any two multi-indices $\mathbf{i} = \operatorname{dec}(I)$ and $\mathbf{j} = \operatorname{dec}(J)$ with $I + J < N$:*
```
- **Drop-In Fix 2 (`Mas-2 #214` Hint 2, Lines 1268–1271)**:
```markdown
Pack $(a, b, c)$ into $I = a + b(A+1) + c(A+1)(B+1) \in [0, V)$, where $N_1 = A + 1$ and $N_2 = (A + 1)(B + 1)$. By Theorem 16.1, for $I + J < V$, the 1D addition $I + J$ is carry-free if and only if the carry-grading function $\chi(I) = \big(\lfloor I / N_1 \rfloor + \lfloor I / N_2 \rfloor\big) \bmod 3 = \big(b + (B + 2)c\big) \bmod 3$ satisfies:
$$\chi(I + J) \equiv \chi(I) + \chi(J) \pmod 3.$$
```
- **Drop-In Fix 3 (`Mas-2 #214` Step 1, Lines 1303–1307)**:
```markdown
1. **3D-to-1D Kronecker Packing & Carry Grading**:
   Let $n_1 = A + 1, n_2 = B + 1, n_3 = C + 1$, with prefix products $N_1 = n_1$, $N_2 = n_1 n_2$, and $V = n_1 n_2 n_3$. Every valid exponent triple $(a, b, c) \in [0, A] \times [0, B] \times [0, C]$ maps bijectively to $I = a + b N_1 + c N_2 \in [0, V)$ with carry-grading tag $\chi(I) = \big(\lfloor I / N_1 \rfloor + \lfloor I / N_2 \rfloor\big) \bmod 3 = \big(b + (n_2 + 1)c\big) \bmod 3$.
```

#### Defect Ch16-2 (CRITICAL MATH BUG): Wrong Coefficients in the Differential Equation for the 3D Diagonal $D_3(t)$ at Line 672
- **Location**: [`chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L669-L674)
- **Mathematical Proof of Bug**:
  - Line 672 writes:
    $$n^2 u_n - 3(3n - 1)(3n - 2) u_{n-1} = 0 \iff 3t(27t - 1) D_3''(t) + (108t - 1) D_3'(t) + 6 D_3(t) = 0,$$
  - Let us check $[t^{n-1}]$ of $t(27t - 1) D_3''(t) + (54t - 1) D_3'(t) + 6 D_3(t) = 0$:
    - From $-t D_3''(t) - D_3'(t)$: $[t^{n-1}]$ is $-n(n-1) u_n - n u_n = -n^2 u_n$.
    - From $27t^2 D_3''(t) + 54t D_3'(t) + 6 D_3(t)$: $[t^{n-1}]$ is $\big(27(n-1)(n-2) + 54(n-1) + 6\big) u_{n-1} = (27n^2 - 27n + 6) u_{n-1} = 3(3n-1)(3n-2) u_{n-1}$.
  - Thus the true ODE equivalent to $n^2 u_n - 3(3n-1)(3n-2) u_{n-1} = 0$ is:
    $$t(27t - 1) D_3''(t) + (54t - 1) D_3'(t) + 6 D_3(t) = 0,$$
    whereas $3t(27t - 1) D_3''(t) + (108t - 1) D_3'(t) + 6 D_3(t)$ gives $[t^{n-1}] = -(3n^2 - 2n) u_n + (81n^2 - 135n + 60) u_{n-1} \neq 0$ for all $n \ge 2$!
- **Drop-In Fix (Lines 669–674)**:
```markdown
   $$\frac{u_n}{u_{n-1}} = \frac{(3n)! / (n!)^3}{(3n - 3)! / ((n - 1)!)^3} = \frac{3n(3n - 1)(3n - 2)}{n^3} = \frac{3(3n - 1)(3n - 2)}{n^2}.$$
   Therefore, $u_n$ satisfies the **first-order P-recursive relation** (and corresponding second-order Fuchsian linear ODE):
   $$n^2 u_n - 3(3n - 1)(3n - 2) u_{n-1} = 0 \iff t(27t - 1) D_3''(t) + (54t - 1) D_3'(t) + 6 D_3(t) = 0,$$
   allowing $u_0, u_1, \dots, u_N \bmod p$ to be computed in $O(N)$ time!
```

#### Defect Ch16-3: Missing Revisited Dual-Perspective Cross-References (`#4` and `#10` in `CURRICULUM_ARCHITECTURE.md` §5.2)
- **Location 1 (`#10` — `Adv-1 #237 yukicoder 1080`)**: [`chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L1083-L1092).
- **Drop-In Fix 1 (Insert before `</details>` at Line 1091)**:
```markdown
::: {.callout-note}
## Revisited Dual-Perspective Cross-Reference — Algebraic Diagonal (`Ch 16 §16.4`) vs. D-Finite P-Recursion (`Ch 18 §18.2`)
Because $C(t) = \frac{1}{\sqrt{(1 - 2t)^2 + 4t^2}} = \frac{1}{\sqrt{1 - 4t + 8t^2}}$ is algebraic (`Ch 16 §16.4`), it is automatically **D-finite (`Ch 18 §18.2`)**! Differentiating $(1 - 4t + 8t^2) C'(t) = (2 - 8t) C(t)$ and extracting $[t^{n-1}]$ yields the three-term P-recursion $n c_n = 2(2n - 1) c_{n-1} - 8(n - 1) c_{n-2}$. In **Chapter 18 (§18.2)**, we will see how this P-recursion computes $c_0, \dots, c_N$ in $O(N)$ linear time, replacing the $O(N \log N)$ `fps_inv_sqrt` call!
:::
```
- **Location 2 (`#4` — `Adv-2 #074 AtCoder AGC 058 D`)**: [`chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L1173-L1181).
- **Drop-In Fix 2 (Insert before `</details>` at Line 1180)**:
```markdown
::: {.callout-note}
## Revisited Dual-Perspective Cross-Reference — Smirnov & Goulden–Jackson (`Ch 08 §8.2, §8.4`) vs. 3D Rational Diagonal (`Ch 16 §16.4`)
In **[Chapter 08 (§8.2 & §8.4)](ch08-connected-component-ie-rook-goulden-jackson.qmd)**, we saw two general word-enumeration frameworks: the **Smirnov word transfer reduction** $W_i \mapsto \frac{w_i x}{1 + w_i x}$ (for runs of identical letters) and the **Goulden–Jackson Cluster Method** (for avoiding forbidden substrings `ABC`, `BCA`, `CAB`). Here in `Adv-2 (#074)`, because the three cyclic forbidden triples have symmetric overlaps, the cluster denominator collapses to the single rational function $\frac{1 - x y z}{1 - (x + y + z) + 2 x y z}$, turning a multivariate Goulden–Jackson sieve into a clean $O(A + B + C)$ rational diagonal extraction!
:::
```

#### Defect Ch16-4: Stale Chapter Numbers & Broken `.qmd` Links in Prerequisites (Lines 8–11)
- **Location**: [`chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L7-L12)
- **Issue**: Line 8 links to `ch05-rational-recurrences-bostan-mori.qmd` (actual: `ch05-rational-bostan-mori-berlekamp-massey.qmd`); Line 9 refers to `Chapter 7 (ch07-newton-transcendental-fps.qmd)` (actual: **Chapter 2**, `ch02-calculus-frobenius-sparse-ode-newton.qmd`); Line 11 refers to `Chapter 15 (ch15-binomial-sums-egorychev.qmd)` (actual: **Chapter 6**, `ch06-binomial-snake-oil-taylor-shift-stirling.qmd`, and **Chapter 15**, `ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`).
- **Drop-In Fix (Lines 7–12)**:
```markdown
Before diving into multivariate generating functions, ensure you are comfortable with the following univariate tools:
- **Chapter 2** ([Formal Calculus, Sparse Differential Equations & Newton's Method](ch02-calculus-frobenius-sparse-ode-newton.qmd)): Univariate FPS inversion, logarithmic derivative $\ln G = \int (G'/G)\,dx$, and exponential $\exp F$.
- **Chapter 5** ([Rational GFs, Euclidean Division & The Bostan–Mori Engine](ch05-rational-bostan-mori-berlekamp-massey.qmd)): Univariate Bostan–Mori parity splitting $[x^N] P(x)/Q(x)$ and Graeffe root-squaring $Q(x)Q(-x) = V(x^2)$.
- **Chapter 6** ([Binomial Sums, Snake Oil, Taylor Shift & Stirling Numbers](ch06-binomial-snake-oil-taylor-shift-stirling.qmd)): Coefficient extraction identities and binomial double sums.
- **Chapter 11** ([Formal Laurent Series, Formal Residues, Raney's Lemma & Lagrange Inversion](ch11-laurent-residues-raney-lagrange-inversion.qmd)): The formal Laurent field $K((z))$, valuation $\operatorname{val}_z$, and formal residue operator $\operatorname{res}_z = [z^{-1}]$.
```

---

## Chapter 17 Audit: `ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`

### 1. Mathematical & Pedagogical Verification Summary
- **§17.1 (`Multivariate Good–Lagrange Inversion & Coupled Tree Systems`)**:
  - Verified Theorem 17.1 (Form 1 & Form 2), the formal residue proof via $x_i = u_i / \Phi_i(\mathbf{u})$ and logarithmic Jacobian $I_d - J(\mathbf{u})$, Gessel's combinatorial cycle-cancellation proof on functional digraphs (lines 116–137), and Corollary 17.1 (Bipartite Rank-1 Collapse, verified on Scoins's theorem $n^{m-1} m^{n-1}$).
- **§17.2 (`MacMahon's Master Theorem & The BEST Theorem`)**:
  - Verified Theorem 17.2 (MacMahon's Master Theorem), the 3-parameter Dixon identity derivation $\binom{a+b}{a}\binom{b+c}{b}\binom{c+a}{c} = \frac{(a+b+c)!}{a!b!c!}$ (lines 213–248), and Theorem 17.3 (BEST Theorem vs. MacMahon cycle covers).
- **§17.3 (`The Symmetric Function Trinity: e_k, h_k, p_k & Newton–Girard`)**:
  - Verified $E(t) H(t) = 1$, $P(t) = \frac{t H'(t)}{H(t)} = \frac{-t E'(-t)}{E(-t)}$, and **Canonical Failure Mode #7** (division by $k$ fails in characteristic $p \le N$, with all 3 characteristic-$p$ remedies on lines 328–359).
- **§17.4 (`2D Quarter-Plane Lattice Walks: The Obstinate Kernel Method & Bivariate PDEs`)**:
  - Verified the 4-boundary quarter-plane functional equation (lines 384–393), the Vieta involutions $\Phi, \Psi$, the $D_2$ (order 4) decouple trace on $S(x,y) = x + x^{-1} + y + y^{-1}$, the $D_3$ (order 6) trace on the Tandem Walk $S(x,y) = x + y/x + y^{-1}$ (Theorem 17.4), and the Bivariate PDE Companion Matrix method (§17.4E).
  - Verified that Revisited Dual-Perspective Cross-References `#5` (`Int-1 #228` $\leftrightarrow$ `Ch 13 §13.2`) and `#11` (`Int-2 #219` $\leftrightarrow$ `Ch 20 §20.1`) are already present in the text!

### 2. Required Fixes in `ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`

#### Defect Ch17-1: Binary Indexing Typo ($v = 2j + 2k + l$ Instead of $v = 4j + 2k + l$) + Raw `"Wait:"` Monologue in `SS-2 #044` (`ABC 336 G`)
- **Location**: [`chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L680-L689)
- **Issue**:
  1. Line 681 writes: `from $u = 4i + 2j + k$ to $v = 2j + 2k + l$.` For the 3-bit vertex $(j, k, l) \in \{0, 1\}^3$, its binary integer index is **$v = 4j + 2k + l$**, NOT $2j + 2k + l$!
  2. Line 686 contains a raw editorial monologue `(Wait: if all $u$ initially have $d^+(u) = d^-(u)$...)`.
- **Drop-In Fix (Lines 680–689)**:
```markdown
1. **De Bruijn Graph Construction & Degree Balance Check**:
   Construct the $8$-vertex directed multigraph $G = (V, E)$ where $V = \{0, 1, \dots, 7\}$ and each 4-tuple $(i, j, k, l)$ gives $X_{i,j,k,l}$ parallel directed edges from $u = 4i + 2j + k$ to $v = 4j + 2k + l$. Let $V_{\text{active}} \subseteq V$ be the set of vertices incident to at least one edge. Check via BFS/DFS that all vertices in $V_{\text{active}}$ lie in a single weakly connected component; if not, output $0$.

2. **Enumerating Valid Start/End Pairs $(s, t)$ via the Sentinel Edge $t \to s$**:
   For each candidate pair of start vertex $s \in V_{\text{active}}$ and end vertex $t \in V_{\text{active}}$, adding one distinguishable sentinel edge $e^* = (t \to s)$ increments $d^+(t)$ and $d^-(s)$ by $1$.
   A pair $(s, t) \in V_{\text{active}}^2$ can support an Eulerian trail if and only if $d^+_{\text{aug}}(u) = d^-_{\text{aug}}(u)$ for all $u \in V$: specifically, if all $u$ initially satisfy $d^+(u) = d^-(u)$, then $s = t$ can be any vertex in $V_{\text{active}}$; if exactly one vertex has $d^+ - d^- = +1$ and one has $d^+ - d^- = -1$, then $s$ and $t$ are uniquely forced; otherwise the answer is $0$.
```

#### Defect Ch17-2 (CRITICAL MATH BUG): False Carry-Grading Formula $\chi(i_1, i_2, i_3) = (i_1 + i_2 + i_3) \bmod 3$ in `Mas-2 #234` (Lines 1203 & 1231) + Stale Chapter 15 Reference
- **Location**: [`chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L1203) and [line 1231](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L1231) (plus line 1172).
- **Mathematical Proof of Bug**:
  - Lines 1203 and 1231 state that for 3D $\chi$-twisted Kronecker FFT on $R = \mathbb{F}_p[u_1, u_2, u_3]/(u_1^{k_1+1}, u_2^{k_2+1}, u_3^{k_3+1})$, the carry-grading function is $\chi(e_1, e_2, e_3) = (e_1 + e_2 + e_3) \bmod 3$.
  - This is **mathematically false** whenever $k_1 \not\equiv 0 \pmod 3$ or $k_2 \not\equiv 0 \pmod 3$! For example, if $k_1 = 1$, adding $(1, 0, 0) + (1, 0, 0)$ produces a carry into the second coordinate $(0, 1, 0)$, where $(1+0+0) + (1+0+0) = 2 \neq (0+1+0) = 1 \pmod 3$, which happens to differ only because $k_1 = 1 \not\equiv 0 \pmod 3$; if $k_1 = 2$, $(2, 0, 0) + (1, 0, 0)$ carries into $(0, 1, 0)$, and $(2+0+0) + (1+0+0) = 3 \equiv 0 \neq 1$, whereas if $k_1 = 1$ and we add $(1, 1, 0) + (1, 0, 0) \mapsto (0, 0, 1)$ when $k_2 = 1$, $(1+1+0) + (1+0+0) = 3 \equiv 0 \neq 1$, AND if $k_1 = 2, k_2 = 1$, $(2, 1, 0) + (1, 0, 0) \mapsto (0, 0, 1)$ has $(2+1+0) + (1+0+0) = 4 \equiv 1 = (0+0+1) \pmod 3$, **failing to detect the double carry**!
  - By Chapter 16 (Theorem 16.1), the true carry-grading function for $I = e_1 + e_2 N_1 + e_3 N_2$ (with $N_1 = k_1 + 1$, $N_2 = (k_1 + 1)(k_2 + 1)$) is:
    $$\chi(I) = \left(\left\lfloor \frac{I}{N_1} \right\rfloor + \left\lfloor \frac{I}{N_2} \right\rfloor\right) \bmod 3 = \big(e_2 + (k_2 + 2) e_3\big) \bmod 3.$$
  - In addition, lines 1172, 1203, and 1231 cite `(Chapter 15)` instead of `(Chapter 16)` for $\chi$-twisted Kronecker FFT.
- **Drop-In Fix 1 (Line 1172)**:
```markdown
- **Required Complexity**: $O(V \log V)$ time and $O(V)$ space via 3D Multivariate Good–Lagrange Form 1 and $\chi$-twisted Kronecker FFT (Chapter 16).
```
- **Drop-In Fix 2 (Line 1203)**:
```markdown
Let $k_i = n_i - r_i$. We work in the truncated 3D polynomial ring $R = \mathbb{F}_p[u_1, u_2, u_3]/(u_1^{k_1+1}, u_2^{k_2+1}, u_3^{k_3+1})$ using the $\chi$-twisted Kronecker FFT from Chapter 16 (where $\chi(I) = \big(\lfloor I/N_1 \rfloor + \lfloor I/N_2 \rfloor\big) \bmod 3 = \big(i_2 + (k_2 + 2) i_3\big) \bmod 3$ with $N_1 = k_1 + 1, N_2 = (k_1 + 1)(k_2 + 1)$):
```
- **Drop-In Fix 3 (Line 1231)**:
```markdown
   Using $\chi$-twisted Kronecker multiplication ($\chi(I) = \big(\lfloor I/N_1 \rfloor + \lfloor I/N_2 \rfloor\big) \bmod 3 = \big(e_2 + (k_2 + 2) e_3\big) \bmod 3$, Chapter 16), we transform all 9 polynomials $M_{i,j}(\mathbf{u})$ once and evaluate the $2 \times 2$ minors and final outer product in $O(3^2 V \log V)$ operations.
```

#### Defect Ch17-3: Stale Chapter Numbers & Broken `.qmd` Links in Prerequisites (Lines 11–14 & Line 200)
- **Location**: [`chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L10-L15) and [line 200](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L200).
- **Issue**: Lines 11–14 link to non-existent filenames (`ch11-lagrange-inversion-formal-residues.qmd`, `ch13-implicit-equations-newton-functional-iteration.qmd`, `ch15-multivariate-fps-kronecker-bostan-mori.qmd`, `ch16-rational-diagonals-furstenberg.qmd`) and assign Implicit Equations to Chapter 13 (actually **Chapter 10**) and Multivariate FPS / Kronecker / Bostan–Mori to Chapter 15 (actually **Chapter 16**; also on line 200).
- **Drop-In Fix (Lines 10–15)**:
```markdown
Before diving into this chapter, ensure you are fluent with the following tools from earlier chapters:
- **[Chapter 10 — Implicit Equations, Multivariate Newton & Unlabeled Trees](ch10-implicit-equations-newton-unlabeled-trees-otter.qmd)**: Coupled implicit systems of formal power series and multivariate Jacobian matrices.
- **[Chapter 11 — Formal Laurent Series, Formal Residues, Raney's Lemma & Lagrange Inversion](ch11-laurent-residues-raney-lagrange-inversion.qmd)**: Univariate formal Laurent series $K((x))$, the formal residue operator $\operatorname{Res}_x$, the change-of-variables law $\operatorname{Res}_x F(x) = \operatorname{Res}_u F(g(u))g'(u)$, and univariate Lagrange Inversion.
- **[Chapter 15 — 1D Lattice Walks, Reflection Principle & The Kernel Method](ch15-1d-lattice-walks-chebyshev-kernel-method.qmd)**: Boundary kernel equations, small vs. large roots, and Vieta root-jumping involutions.
- **[Chapter 16 — The Multivariate Hierarchy, 2D Bostan–Mori, $\chi$-Twisted Kronecker & Furstenberg Diagonals](ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd)**: Multivariate rings $K[[x_1, \dots, x_d]]$, $\chi$-twisted Kronecker multiplication, 2D Bostan–Mori, and iterated multivariate formal residues.
```
- **Drop-In Fix (Line 200)**:
```markdown
  Extract $[x_1^{m_1} \cdots x_d^{m_d}] \det(I_d - X A)^{-1}$ via multivariate Bostan–Mori or $\chi$-twisted Kronecker inversion (Chapter 16) in $O(2^d + V \log V)$ time where $V = \prod_{i=1}^d (m_i + 1)$.
```

---

## Checkpoint IV Audit: `cp04-part4-pgf-walks-multivariate.qmd`

### 1. Mathematical, Structural & Spoiler-Free Verification Summary
- **100% Spoiler-Free Stage 1 Verified**:
  - All 8 problems (`CP-IV.1 #158`, `CP-IV.2 #169`, `CP-IV.3 #099`, `CP-IV.4 #116`, `CP-IV.5 #194`, `CP-IV.6 #058`, `CP-IV.7 #243`, `CP-IV.8 #082`) match `CURRICULUM_ARCHITECTURE.md` 100%.
  - In Stage 1, no visible heading, problem statement, small-instance walkthrough, or Hint 1 (`Spoiler-Free`) reveals the target chapter number or paradigm name.
- **Stage 2 Derivations Verified**:
  - `CP-IV.1 (#158)`: Extended $K$-th Min–Max IE and Pascal DP state compression verified *(see Defect CP4-1 for the $dp[0][0] = -1$ sign bug in Hint 3 line 79 and the `"Wait:"` monologue at lines 555–558)*.
  - `CP-IV.2 (#169)`: Parity EGF factorization, Borel transform to OGF, and $(1-x)$ pole cancellation at $x = 1+t \bmod t^2$ verified.
  - `CP-IV.3 (#099)`: Pairwise martingale potential $\Phi = \sum (2^{a_i} - 1)$ verified.
  - `CP-IV.4 (#116)`: Martingale potential with conservation-law gauge fixing $f(1) = 2$ and first-difference reduction $(N-s)g(s) = (2N-s)g(s-1)$ verified.
  - `CP-IV.5 (#194)`: Uniform subset coupon-collector conditioning, interval run-length generating function, formal residue change of variables $w = x/(1+x)^{k+1}$, and D&C NTT verified.
  - `CP-IV.6 (#058)`: Column-symmetric set-hitting renewal deconvolution and Krawtchouk basis transform verified *(see Defect CP4-2 for the missing Revisited cross-reference `#12` to `Ch 18 §18.2`)*.
  - `CP-IV.7 (#243)`: Furstenberg $(p, 1)$-diagonal substitution $x = z, y = t/z^p$, Global Residue Theorem on $\mathbb{P}^1$ at the unique large pole $z_{\text{large}}(t) = 1 - w(t)$ (resolving Failure Mode #15), and Form 1 LIF extraction verified.
  - `CP-IV.8 (#082)`: Both fixed-multiplicity Raney Cycle Lemma (plus $2 \times 2$ affine decimal tracking) and 1-small-root Kernel Method $y_0(x) = x\Phi(y_0(x))$ verified.

### 2. Required Fixes in `cp04-part4-pgf-walks-multivariate.qmd`

#### Defect CP4-1: Wrong Sign ($dp[0][0] = -1$ Instead of $dp[0][0] = 1$) in `CP-IV.1` Hint 3 (Line 79) + Raw `"Wait:"` Monologue in Stage 2 (Lines 555–558)
- **Location**: [`checkpoints/cp04-part4-pgf-walks-multivariate.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L77-L80) and [lines 552–560](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L552-L560).
- **Issue**:
  1. For the transition $dp_{\text{new}}[j + p_i][r] = dp[j + p_i][r] + dp[j][r - 1] - dp[j][r]$, a singleton subset $S = \{i\}$ ($s = 1$) at $r = 1$ must receive $(-1)^{1-1}\binom{0}{0} = +1 = dp[0][0] - dp[0][1]$, which requires **$dp[0][0] = +1$** (and $dp[j][0] = 0$ for all $j \ge 1$). Hint 3 on line 79 erroneously writes `with base convention $dp[0][0] = -1$`.
  2. In Stage 2 (lines 555–558), the text starts with `dp[0][0] = -1`, notices it gives `-1`, and leaves a raw self-correction monologue: `- For $r = 1$: $dp[0][0] - dp[0][1] = -1 - 0 = -1$? Wait: we want $+1$ for $r = 1, s = 1$!`.
- **Drop-In Fix 1 (Hint 3, Lines 77–80)**:
```markdown
Define $dp[j][r]$ (for $0 \le j \le m$ and $1 \le r \le K$) as the sum of $(-1)^{|S| - r} \binom{|S| - 1}{r - 1}$ over all subsets $S$ of the items processed so far with $\sum_{i \in S} p_i = j$. When adding item $i$ with weight $p_i$:
$$dp_{\text{new}}[j + p_i][r] = dp[j + p_i][r] + dp[j][r - 1] - dp[j][r],$$
with base seed $dp[0][0] = 1$ and $dp[j][0] = 0$ for all $j \ge 1$ (so when $S = \{i\}$ is a singleton of weight $p_i$ and $r = 1$, it receives $+dp[0][0] - dp[0][1] = +1 = (-1)^{1-1}\binom{0}{0}$). Finally, $\mathbb{E}[T] = \sum_{j=1}^m dp[j][K] \cdot \frac{m}{j} \bmod 998244353$ in $O(n m K)$ time and $O(m K)$ space.
```
- **Drop-In Fix 2 (Stage 2 Solution, Lines 552–560)**:
```markdown
Let us check the base case when $S$ transitions from the empty set ($s = 0$) to a singleton ($s = 1$):
For $s = 1$, we want $f(1, r) = (-1)^{1 - r} \binom{0}{r - 1} = [r = 1]$.
If we set the empty-set state ($j = 0$) to have:
$$dp[0][0] = 1, \qquad dp[0][r] = 0 \quad (1 \le r \le K),$$
and keep $dp[j][0] = 0$ for all $j \ge 1$ while applying the transition $dp_{\text{new}}[j + p_i][r] = dp[j + p_i][r] + dp[j][r - 1] - dp[j][r]$ for $r = 1, \dots, K$, let us verify the first two insertions:
- Adding 1st element (weight $p_1$): for $r = 1$, $dp[p_1][1] \gets dp[0][0] - dp[0][1] = 1 - 0 = +1 = (-1)^{1-1}\binom{0}{0}$. For $r \ge 2$, $dp[p_1][r] \gets dp[0][r-1] - dp[0][r] = 0$.
```

#### Defect CP4-2: Missing Revisited Dual-Perspective Cross-Reference (`#12` in `CURRICULUM_ARCHITECTURE.md` §5.2) in `CP-IV.6` (`#058` — `ARC 136 F Flip Cells`)
- **Location**: [`checkpoints/cp04-part4-pgf-walks-multivariate.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L784-L791)
- **Issue**: `CURRICULUM_ARCHITECTURE.md` §5.2 (`#12`) mandates a forward/dual-perspective note in `CP-IV.6 (#058)` explaining how the $O(N^2)$ Krawtchouk basis expansion $\sum_{m=0}^N u_m (1 - z)^m (1 + z)^{N - m}$ is accelerated to $O(N)$ time in **Chapter 18 (§18.2)** via D-Finite / P-Recursive evaluation of the Krawtchouk basis polynomials.
- **Drop-In Fix (Lines 784–791)**:
```markdown
##### 3. Algorithm Contract (`CP-IV.6`)

- **Input**: $H, W \le 50$ ($N = HW \le 2500$), initial grid $S$, target row sums $A_1, \dots, A_H$.
- **Step 1**: Construct $p_i(y)$ and $q_i(y)$ of degree $W$ for each row $i$, and multiply them iteratively in $O(H^2 W^2) = O(N^2)$ time to obtain $U(y)$ and $V(y)$.
- **Step 2**: Compute $A_{\text{raw}}(z) = \sum_{m=0}^N u_m (1 - z)^m (1 + z)^{N - m}$ and $B_{\text{raw}}(z) = \sum_{m=0}^N v_m (1 - z)^m (1 + z)^{N - m}$ in $O(N^2)$ time, where $[z^r]$ corresponds to $k = N - 2r \in \{-N, \dots, N\}$.
- **Step 3**: Return $\frac{1}{B_{\text{raw}}[0]} \sum_{r=1}^N \big(B_{\text{raw}}[r] - A_{\text{raw}}[r]\big) \frac{N}{2r} \bmod 998244353$.
- **Complexity**: $O(H^2 W^2)$ time and $O(H W)$ space.

::: {.callout-note}
## Revisited Dual-Perspective Preview — From $O(N^2)$ Krawtchouk Expansion to $O(N)$ D-Finite Recurrence (`Ch 18 §18.2`)
In Step 2 above, converting $U(y) = \sum_{m=0}^N u_m y^m$ into $A_{\text{raw}}(z) = (1 + z)^N U\!\left(\frac{1 - z}{1 + z}\right) = \sum_{m=0}^N u_m (1 - z)^m (1 + z)^{N - m}$ by naive polynomial accumulation takes $O(N^2)$ time. In **Chapter 18 (§18.2: D-Finite Power Series & P-Recursive Sequences)**, we will revisit `#058 (ARC 136 F)` and show that the Krawtchouk basis polynomials $K_r(m) = [z^r] (1 - z)^m (1 + z)^{N - m}$ satisfy a three-term linear recurrence (and a first-order rational ODE under the Möbius substitution $y = \frac{1 - z}{1 + z}$), allowing Step 2 to be evaluated in **$O(N)$ time** (or $O(N \log N)$ across all $r$)!
:::
```
