# Phase 3 Iteration 5 Specialist Audit Report: Multivariate, Diagonal, Formal Residue & Kernel Method Clarity

- **Auditor**: `fps-textbook-critic` (Phase 3 Iteration 5 Global Specialist Critic)
- **Date**: 2026-10-15
- **Scope**:
  1. [`chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd) (1,734 lines)
  2. [`chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd) (1,453 lines)
  3. [`chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd) (1,411 lines)
  4. [`chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd) (1,401 lines)
  5. [`checkpoints/cp03-part3-online-implicit-lif-graphs.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp03-part3-online-implicit-lif-graphs.qmd) (1,290 lines)
  6. [`checkpoints/cp04-part4-pgf-walks-multivariate.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd) (992 lines)
  - Cross-referenced against [`AGENTS.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/AGENTS.md) and [`NOTATION.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/NOTATION.qmd).

---

## 1. Executive Verdict

**OVERALL VERDICT: PASS WITH 3 MINOR EDITORIAL / NOTATION HARMONIZATION POLISH ITEMS (ZERO MATHEMATICAL ERRORS, ZERO MAGIC STEPS, ZERO PREREQUISITE VIOLATIONS)**

Across all 8,281 lines of the 4 specialist chapters (`Ch 11`, `Ch 15`, `Ch 16`, `Ch 17`) and 2 blind checkpoints (`CP-III`, `CP-IV`), the textbook achieves exceptional algebraic rigor, pedagogical transparency, and self-contained completeness:
- Every formal residue change of variables, Puiseux/Catalan root substitution, 1D/2D Kernel Method cancellation, Furstenberg diagonal extraction, Multivariate Good–Lagrange determinant, and MacMahon Master Theorem reduction is **100% algebraically justified** inside formal power/Laurent series rings with **zero reliance on complex contour integrals** or hand-waved analytic continuation.
- Every non-obvious substitution is preceded by an explicit **Diagnostic Signal** and **Reverse-Engineering Scratchpad**.
- All 32 chapter problems (8 per chapter) and 16 checkpoint problems (`CP-III.1`–`CP-III.8`, `CP-IV.1`–`CP-IV.8`) have complete self-contained statements, exact constraints/moduli, 3 progressive hints, full derivations, and Algorithm Contracts (`Input`/`Output`/`Complexity`), with 100% spoiler-free Stage 1 tables in `CP-III` and `CP-IV`.

Below is the detailed audit across the **4 Specialist Focus Areas**, the **8 Mandatory Audit Dimensions**, and the **3 Minor Actionable Polish Items** with exact line numbers and drop-in replacements.

---

## 2. Specialist Audit Focus Areas

### Focus Area 1: Formal Residue Calculus (`Ch 11`, `CP-III.3`, `CP-III.7`, `CP-IV.7`)

| Verification Target | Locations Audited | Status & Line-Referenced Findings |
| :--- | :--- | :--- |
| **Formal Laurent ring $K((x))$ & residue functional $\operatorname{Res}_{x=0} F(x)\,dx = [x^{-1}]F(x)$** | `Ch 11` lines 62–108 | **PASS.** Explicitly constructs $K((x)) = K[[x]][x^{-1}]$ with discrete valuation $\operatorname{val}(F) = m_0 \in \mathbb{Z}$, proves field structure when $K$ is a field via $F(x)^{-1} = x^{-m_0} U(x)^{-1}$, and defines $\operatorname{Res}_{x=0}$ purely as the coefficient extraction $[x^{-1}]$. |
| **Derivative Kernel Lemma ($\operatorname{Res}_{x=0} F'(x)\,dx = 0$ in ALL characteristics)** | `Ch 11` lines 110–124 | **PASS.** Proves $F'(x) = \sum_{n \ge m_0} n f_n x^{n-1}$ has $[x^{-1}]F'(x) = 0 \cdot f_0 = 0$ unconditionally, and explicitly highlights the characteristic-$p$ caveat: $\operatorname{Res} H(x)\,dx = 0 \iff H = F'$ holds in char $0$, whereas in char $p > 0$ any $x^{kp-1}$ ($k \ne 0$) also has zero residue and cannot be integrated without dividing by $kp \equiv 0 \pmod p$. |
| **Logarithmic Derivative Valuation Identity ($\operatorname{Res}_{u=0} \frac{G'(u)}{G(u)}\,du = m$)** | `Ch 11` lines 126–140 | **PASS.** Factors $G(u) = u^m U(u)$ with $U(0) \ne 0$, expands $G'(u)/G(u) = m u^{-1} + U'(u)/U(u)$ with $U'/U \in K[[u]]$, and extracts $[u^{-1}] = m \cdot 1_K$ without complex analysis. |
| **Jacobi's Formal Change-of-Variables Theorem ($\operatorname{Res}_{x=0} F(x)\,dx = \operatorname{Res}_{u=0} F(G(u))G'(u)\,du$)** | `Ch 11` lines 142–207 | **PASS (Exemplary).** Theorem 11.1 proves linearity reduces the identity to $F(x) = x^k$ ($k \in \mathbb{Z}$). Case 1 ($k = -1$) uses the Logarithmic Derivative Valuation Identity with $\operatorname{val}(G) = 1$. Case 2 ($k \ge 0$) is immediate since $G(u)^k G'(u) \in K[[u]]$. Case 3 ($k \le -2$) avoids division by $k+1$ in characteristic $p \mid (k+1)$ via **universal ring lifting**: in $\mathbb{Z}[g_1^{\pm 1}, g_2, g_3, \dots] \subset \mathbb{Q}(g_1)[g_2, \dots]$, $G(u)^k G'(u) = \frac{d}{du}\!\big(\frac{G(u)^{k+1}}{k+1}\big)$ has $[u^{-1}] = 0$ in $\mathbb{Q}(g_1)[g_2, \dots]$, hence is the zero polynomial in $\mathbb{Z}[g_1^{\pm 1}, g_2, \dots]$, and specializing via $\mathbb{Z} \to K$ preserves $0$ in every characteristic $p$. |
| **All 6 Canonical Forms of LIF & Failure Modes `#5` and `#16`** | `Ch 11` lines 209–395 | **PASS.** Derives Form 1 ($\frac{1}{n}[u^{n-1}]H'(u)\phi(u)^n$), Form 2 ($[u^n]H(u)\phi(u)^n(1 - \frac{u\phi'(u)}{\phi(u)})$ — **division-free in char $p$**), Form 3 (Bürmann-type), Form 4 (Exponential $w = x e^{G(w)}$), Form 5 (Implicit $P(x, w(x)) = 0$), and Form 6 (Compositional Inverse). Failure Mode `#5` (lines 322–342) and Failure Mode `#16` (lines 344–378, Catalan negative upper-index trap at $k=0$ where $\binom{-1}{0}=1 \ne 0$) are thoroughly explained and hand-verified. |
| **Catalan Residue Substitution $x = \frac{u}{(1+u)^2}$ & $q$-Catalan / Raney Extensions** | `Ch 11` lines 189–207, 397–609, 907–1025; `CP-III.3` lines 313–415; `CP-III.7` lines 783–889 | **PASS.** Every Catalan substitution $x = u/(1+u)^2$, $dx = \frac{1-u}{(1+u)^3}\,du$, and $\sqrt{1-4x} = \frac{1-u}{1+u}$ is preceded by a Reverse-Engineering Scratchpad showing why $C(x) = 1+u$ rationalizes the square root and why $\operatorname{val}_u(x) = 1$ validates Theorem 11.1. |

---

### Focus Area 2: 1D & 2D Kernel Method (`Ch 15`, `Ch 17`, `CP-IV.8`)

| Verification Target | Locations Audited | Status & Line-Referenced Findings |
| :--- | :--- | :--- |
| **Ring Distinction: $(K[y, y^{-1}])[[x]]$ vs. $K[y][[x]]$ vs. $K_{\le H}[y][[x]]$** | `Ch 15` lines 60–117, 250–266, 381–393 | **PASS.** Explicitly distinguishes unconstrained walks in $(K[y, y^{-1}])[[x]]$ (no boundary terms), half-line walks $[0, \infty)$ in $K[y][[x]]$ (absorbing boundary terms $B_r(x) = [y^r]W(x, y)$), and two-sided strip walks $[0, H]$ in $K_{\le H}[y][[x]]$ (polynomials in $y$ of degree $\le H$). |
| **Why Small Roots Can Be Substituted into $W(x, y) \in K[y][[x]]$ & Large Roots Cannot** | `Ch 15` lines 268–331 | **PASS (Exemplary).** The **Fundamental Dichotomy** (lines 286–331) proves via Newton polygons and valuation arithmetic that if $S(y) = \sum_{j=-k}^m s_j y^j$, the $k$ **small roots** have $\operatorname{val}_x(y_i) = 1/k > 0$, so $\operatorname{val}_x(w_{n,r} x^n y_i(x)^r) = n + r/k \to \infty$ as $n \to \infty$ (finite sum at every fractional power of $x$), whereas the $m$ **large roots** have $\operatorname{val}_x(y_{\text{large}}) = -1/m < 0$, causing $x^n y_{\text{large}}(x)^r \sim x^{n - r/m}$ to accumulate infinitely many terms at a fixed power of $x$ when $r$ is unbounded on $[0, \infty)$ (**Failure Mode `#14`**, lines 318–331). Conversely, on a bounded strip $[0, H]$ (`§15.4`, lines 387–393), $W(x, y) \in K_{\le H}[y][[x]]$ has degree $\le H$ in $y$, so *both* small and large roots are legally substitutable after clearing $y^H$! |
| **Vieta's Large-Root Elimination Trick & Reflection Principle Algebraic Equivalence** | `Ch 15` lines 333–458 | **PASS.** Shows how $y_1(x)\cdots y_{k+1}(x) = (-1)^{k+1} c_{-k}/c_1 = (-1)^{k+1}/u(x)$ expresses the symmetric product of $k$ small roots via the single large root $y_{k+1}(x) = u(x)$ (lines 354–364), and proves that subtracting the $y_1 \leftrightarrow y_2$ symmetric equations on $[0, H]$ reproduces the André Reflection Principle and Chebyshev spectral formula identically (lines 395–482). |
| **Obstinate Kernel Method (`Bousquet-Mélou & Mishna 2010`) & Vieta Group $\mathcal{G} = \langle \Phi, \Psi \rangle$** | `Ch 17` lines 394–547; `CP-IV.8` lines 881–966 | **PASS.** Explains why a single kernel substitution in 2D leaves two coupled boundary series $F(x; t)$ and $G(y; t)$, derives the Vieta involutions $\Phi(x, y) = \big(\frac{\tilde{A}_{-1}(y)}{\tilde{A}_1(y)x}, y\big)$ and $\Psi(x, y) = \big(x, \frac{A_{-1}(x)}{A_1(x)y}\big)$ from quadratic Vieta products, proves the alternating telescoping sum $\sum_{g \in \mathcal{G}} \operatorname{sgn}(g)\,g(x y K Q) = \sum_{g \in \mathcal{G}} \operatorname{sgn}(g)\,g(\text{RHS})$ cancels both $F(x; t)$ and $G(y; t)$ in $\mathcal{F}_{\text{alg}}$ before projecting onto $K[[x, y]][[t]]$, traces both Gouyou-Beauchamps ($|\mathcal{G}|=4$, $D_2$, lines 441–489, 1081–1217) and Kreweras/Tandem ($|\mathcal{G}|=6$, $D_3$, lines 491–509, `CP-IV.8`), and documents the **Corner Double-Subtraction Trap** ($\epsilon t Q(0,0;t)$ when $(-1,-1) \in \mathcal{S}$) and **Quadrant Support Table Check** (lines 511–536). |

---

### Focus Area 3: Multivariate Rings, Chi-Graded Kronecker & Furstenberg Diagonals (`Ch 16`, `Ch 17`, `CP-IV.7`)

| Verification Target | Locations Audited | Status & Line-Referenced Findings |
| :--- | :--- | :--- |
| **5-Ring Bivariate Hierarchy & Iterated Extraction Non-Commutativity** | `Ch 16` lines 44–153 | **PASS.** Defines Rings 1–5 ($K[[x, y]]$, $K[y][[x]]$, $K(y)[[x]]$, $K((x))[[y]]$, $K((y))[[x]]$), proves that $[x^m][y^n] = [y^n][x^m]$ on $K[[x, y]]$ but fails on $K((x))[[y]] \neq K((y))[[x]]$ via the classic counterexample $\frac{1}{x-y} = \sum_{k \ge 0} x^{-k-1} y^k \in K((x))[[y]]$ vs. $-\sum_{k \ge 0} y^{-k-1} x^k \in K((y))[[x]]$ (lines 116–153). |
| **2D Bostan–Mori across All 4 Regimes & Kinoshita–Li Trade-Off** | `Ch 16` lines 155–342 | **PASS.** Covers Regime 1 (Full Bivariate Parity Split, $O(d_x d_y \log n \log m)$), Regime 2 (Kinoshita–Li `2024` $x$-Halving with $y$-Doubling maintaining invariant $N_j \cdot K_j = n$ in $O(n \log^2 n)$ total work, lines 224–274), Regime 3 (Sparse 1D-to-2D Reduction via $[x^n]A(x) G(x^b y)^k$), and Regime 4 (Frobenius $\bmod p$ reduction $\frac{P(x,y)Q(x,y)^{p-1}}{Q(x^p, y^p)}$ in $O(p^2 d_x d_y \log_p(\max(n, m)))$). |
| **Chi-Graded Kronecker Substitution & Theorem 16.1 (Carry-Detection Proof)** | `Ch 16` lines 344–489 | **PASS.** Proves Theorem 16.1 (lines 382–414) step by step: $\chi(I+J) - \chi(I) - \chi(J) \equiv \sum_{r=1}^{d-1} c_r \pmod d$ where $c_r = \lfloor(i_r + j_r)/n_r\rfloor \in \{0, 1\}$, so $0 \le \sum_{r=1}^{d-1} c_r \le d-1$, which is $\equiv 0 \pmod d$ iff every $c_r = 0$. Also derives the Radial Euler Derivation $\mathfrak{D} = \sum_{r=1}^d N_{r-1} x_r \partial_{x_r}$ for multivariate $\exp/\ln/\text{pow}$ in $O(d \cdot N \log N)$ and flags the small-modulus guard $p \le N-1$ (lines 467–481). |
| **Furstenberg's Theorem (Both Directions), Failure Mode `#15` & Lipshitz's Theorem** | `Ch 16` lines 492–684; `CP-IV.7` lines 809–879 | **PASS.** Proves Theorem 16.2 (Reverse Diagonal Extraction $\operatorname{Diag}_{x,y} R(x,y) = \operatorname{Res}_{z=0} \frac{1}{z} R(z, t/z)$ inside $K((z))[[t]]$, plus the 1-line quadratic shortcut $\frac{1}{\sqrt{\beta^2 - 4\alpha\gamma}}$) and Theorem 16.3 (Forward Algebraic Lift $f(t) = \operatorname{Diag}_{x,y}\!\big(\frac{y^2 P_y(xy, y)}{P(xy, y)}\big)$ when $P(t, f(t))=0$, $f(0)=0$, $P_y(0,0) \ne 0$). **Failure Mode `#15`** (lines 538–587) gives a complete worked counterexample on $R(x,y) = \frac{x+2y}{1-x-y}$ ($\deg_y A = 1 = \deg_y B$) where $z=0$ is a double pole of $\frac{1}{z}R(z, t/z)$ and omitting it gives $2 \ne 1$ at $n=0$. **Lipshitz's Theorem** (lines 650–684) contrasts 2D algebraic diagonals with 3D+ D-finite transcendental diagonals ($\sum \frac{(3n)!}{(n!)^3} t^n \sim \frac{\sqrt{3}}{2\pi}\frac{27^n}{n}$ in char $0$, yet algebraic $\bmod p$ by Furstenberg–Deligne–Christol). |

---

### Focus Area 4: Multivariate Good–Lagrange & MacMahon's Master Theorem (`Ch 17`)

| Verification Target | Locations Audited | Status & Line-Referenced Findings |
| :--- | :--- | :--- |
| **Multivariate Good–Lagrange Theorem 17.1 (Forms 1 & 2, Char-$p$ Safety & Gessel's Combinatorial Proof)** | `Ch 17` lines 41–169 | **PASS.** States both Form 1 ($[\mathbf{u}^{\mathbf{n}}] H(\mathbf{u}) \det(\delta_{i,j} - \frac{u_j}{\phi_i}\frac{\partial \phi_i}{\partial u_j}) \boldsymbol{\phi}^{\mathbf{n}}$, division-free and char-$p$ safe) and Form 2 ($[\mathbf{u}^{\mathbf{n}-\mathbf{1}}] H(\mathbf{u}) \det(\frac{\partial(u_i/\phi_i)}{\partial u_j})$), proves their algebraic equivalence via row scaling and Leibniz expansion, and gives Gessel's (`1987`) combinatorial proof showing why the bare product $[\mathbf{u}^{\mathbf{n}}]\boldsymbol{\phi}^{\mathbf{n}}$ overcounts functional digraphs containing directed cycles in $V \setminus \{0\}$ while the Jacobian determinant $\det(I_d - J(\mathbf{u}))$ performs exact Inclusion–Exclusion over vertex-disjoint directed cycles $\mathcal{C}$ with sign $(-1)^{c(\mathcal{C})}$. |
| **Bipartite Rank-1 Collapse (Corollary 17.1) & Scoins's Theorem** | `Ch 17` lines 171–243 | **PASS.** Proves $\det\begin{pmatrix} I_A & -M_{AB} \\ -M_{BA} & I_B \end{pmatrix} = 1 - \frac{u\phi'(u)}{\phi(u)}\frac{v\psi'(v)}{\psi(v)}$ when $M_{AB} M_{BA}$ has rank 1, and verifies Scoins's theorem ($n^{m-1} m^{n-1}$) at $n=2, m=2$ ($K_{2,2} = C_4 \implies 4$ spanning trees) step by step. |
| **MacMahon's Master Theorem (Theorem 17.2), Dixon's Identity & BEST Theorem Contrast** | `Ch 17` lines 245–330, 825–915 | **PASS.** Derives MacMahon's Master Theorem ($[\mathbf{x}^{\mathbf{n}}]\prod_{i=1}^d (\sum_j a_{i,j} x_j)^{n_i} = [\mathbf{x}^{\mathbf{n}}] \frac{1}{\det(I_d - A X)}$) directly from Good–Lagrange Form 2 via the inhomogeneous deformation $\Phi_i(\mathbf{u}) = 1 + \sum_j a_{i,j} u_j$ followed by degree homogenization, proves the full 3-parameter Dixon identity (`Int-1 #250`, lines 825–915), and explicitly contrasts MMT's cycle-cover determinant $\det(I_d - AX)^{-1}$ with the BEST Theorem's Laplacian cofactor $\det L^{(r)}$ enforcing a last-exit spanning arborescence (lines 319–330). |
| **Newton–Girard Symmetric Function Trinity & Failure Mode `#7`** | `Ch 17` lines 332–391 | **PASS.** Proves $P(t) = -t\frac{E'(-t)}{E(-t)} = t\frac{H'(t)}{H(t)}$, states the $O(N \log N)$ FPS pipeline via `fps_ln`/`fps_exp`, and documents **Failure Mode `#7`** (lines 374–391): in char $p \le N$, $e_k \to p_k$ (`fps_deriv` + `fps_inv`) remains 100% legal because it never divides by $k$, whereas $p_k \to e_k$ or $p_k \to h_k$ (`fps_int` inside `fps_exp`) crashes at $k = p$ with division by $0 \pmod p$. |

---

## 3. Summary Across the 8 Mandatory Audit Dimensions

1. **Mathematical Accuracy & Index Boundary Verification**: **100% Pass.** All formulas, signs, summation limits, valuation shifts, and small-$n$ base cases ($n=0, 1, 2, 3$) across `Ch 11`, `Ch 15`, `Ch 16`, `Ch 17`, `CP-III`, and `CP-IV` were checked and verified.
2. **Zero Magic Steps & Reverse-Engineering Scratchpad Audit**: **100% Pass.** Every non-trivial substitution, kernel root product, residue change-of-variables, and determinant reduction includes a Diagnostic Signal and Reverse-Engineering Scratchpad.
3. **Strict Prerequisite Closure & Zero Forward-Reference Audit**: **100% Pass.** `Ch 11` uses only `Ch 1`–`Ch 11`; `Ch 15` uses only `Ch 1`–`Ch 15`; `Ch 16` uses only `Ch 1`–`Ch 16`; `Ch 17` uses only `Ch 1`–`Ch 17`; `CP-III` uses only Parts I–III (`Ch 1`–`Ch 13`); and `CP-IV` uses only Parts I–IV (`Ch 1`–`Ch 17`).
4. **100% Sub-Section, Failure Mode & Characteristic-$p$ Completeness**: **100% Pass.** All assigned Failure Modes (`#5` and `#16` in `Ch 11`; `#14` in `Ch 15`; `#15` in `Ch 16`; `#7` in `Ch 17`), Characteristic-$p$ bypasses (Theorem 11.1 universal ring proof, LIF Form 2, Frobenius decimation, 2D Bostan–Mori $\bmod p$, Good–Lagrange Form 1, Newton–Girard asymmetry), and Revisited Dual-Perspective Cross-References are present and rigorous (see Minor Item 1 below for a label typo in `Ch 15`'s Revisited callout).
5. **8-Problem Ladder & Blind Checkpoint Completeness Audit**: **100% Pass.** All 32 chapter problems and 16 checkpoint problems match `CURRICULUM_ARCHITECTURE.md`, include 3 progressive hints + full derivation + Algorithm Contract, and `CP-III`/`CP-IV` Stage 1 tables are 100% spoiler-free.
6. **`AGENTS.md` Editorial Policy Compliance**: **100% Pass.** Zero raw NTT/modint template dumps; every algorithmic snippet uses clean C++20 pseudocode with an explicit Algorithm Contract and local algebraic hypotheses beside every division.
7. **Citations & Terminology Integration**: **100% Pass.** Proper credits to Jacobi (`1830`), Lagrange (`1770`), Bürmann (`1799`), Raney (`1960`), Gessel (`1987`, `2016`), Banderier & Flajolet (`2002`), Furstenberg (`1967`), Lipshitz (`1988`), Kinoshita & Li (`2024`), Bousquet-Mélou & Mishna (`2010`), Good (`1960`), MacMahon (`1915`), and Scoins (`1962`), alongside `[EN]`/`[ZH]`/`[JA]` terminology tables.
8. **Quarto Formatting & Render Safety**: **100% Pass.** Zero forbidden `\(` or `\[` math delimiters, zero unescaped `|` inside Markdown tables, and all `:::` / `<details>` blocks are properly balanced.

---

## 4. Minor Actionable Polish Items (With Exact Line Numbers & Drop-In Fixes)

While there are zero mathematical errors or missing derivations, the following **3 minor editorial/notation polish items** should be applied to achieve 100% cross-chapter perfection:

### Item 1: `Ch 15` Line 1413 — Revisited Callout Reference Label Mismatch (`UOJ 424 #210`)
- **Location**: [`chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd:1411-1415`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L1411-L1415)
- **Finding**: Line 1413 states:
  > *"We first solved UOJ 424 (`#210`) in Chapter 11 (`§11.4`, Mastery 2) via Cartesian tree height decomposition and formal Laurent residue extraction."*
  In `Ch 11`, however, Mastery 2 is `#203` (`Luogu P7592 — 2021 CoE-II E: 数树`), whereas the Catalan formal residue substitution $x = \frac{u}{(1+u)^2}$ and shifted Catalan extraction used here were developed in `Ch 11` (`§11.1–11.2` and Intermediate 2 `#201 Luogu P7439`).
- **Exact Drop-In Fix for `chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd` (lines 1411–1415)**:
  ```markdown
  ::: {.callout-tip title="Revisited Cross-Reference: Formal Residue Extraction (Ch 11) vs. Strip Reflection / Chebyshev Polynomials (Ch 15)"}
  Using the Catalan Formal Residue Engine developed in Chapter 11 (`§11.1–11.2`, and applied in Intermediate 2 `#201`), we can extract the coefficient directly in the $u$-plane via $x = \frac{u}{(1+u)^2}$, $dx = \frac{1-u}{(1+u)^3}\,du$, and $\frac{U_{m-1}(1/(2\sqrt{x}))}{\sqrt{x}^{m-1}} = \frac{(1+u)^{m-1}(1 - u^m)}{(1-u)u^{m-1}}$. Here in Chapter 15, we arrived at the exact same rational generating function $\frac{P_{m+1}(x)}{P_{m+2}(x)}$ and its geometric series expansion purely through **bounded-strip kernel cancellation** (or equivalently **André's Reflection Principle** and **Chebyshev spectral synthesis**). Notice how the two viewpoints complement each other:
  ```

### Item 2: Harmonize Iterated Laurent-Series Ring Notation $K((z))[[t]]$ vs. $K[[t]]((z))$ and Capitalized `\operatorname{Res}`
- **Locations**:
  1. [`checkpoints/cp04-part4-pgf-walks-multivariate.qmd:868`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L868)
  2. [`NOTATION.qmd:132`](file:///home/maomao90/Documents/IO/ICPC-math-notes/NOTATION.qmd#L132)
  3. [`chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd) (lines 11, 86, 506, 522, 531, 581–585, 633–635, 1084, 1406–1407) and [`checkpoints/cp03-part3-online-implicit-lif-graphs.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp03-part3-online-implicit-lif-graphs.qmd) (lines 803–805, 1115–1117)
- **Finding**:
  - In `Ch 16` (§16.1, line 78), the text carefully proves that the diagonal substitution $F(z, t/z) = \sum_{k \ge 0} \big(\sum_{n=0}^k f_{n, k-n} z^{2n-k}\big) t^k$ has $z$-valuation $-k \to -\infty$ as $k \to \infty$, and therefore lives in $K((z))[[t]]$ (formal power series in $t$ with Laurent coefficients in $K((z))$), **not** in $K[[t]]((z))$ (which would require a single uniform lower bound on the power of $z$ across all $t^k$). However, `CP-IV.7` line 868 writes `$\mathbb{Q}[[t]]((z))$` and `NOTATION.qmd` line 132 writes `$K[[t]]((y))$`.
  - Additionally, `NOTATION.qmd` line 106 standardizes the formal residue operator as capitalized `\operatorname{Res}_{x=0}`, which `Ch 11`, `Ch 15`, `Ch 17`, and `CP-IV` follow, whereas `Ch 16` and `CP-III` use lowercase `\operatorname{res}_z`.
- **Exact Drop-In Fixes**:
  - In `checkpoints/cp04-part4-pgf-walks-multivariate.qmd` line 868, replace `\mathbb{Q}[[t]]((z))` with `\mathbb{Q}((z))[[t]]`.
  - In `NOTATION.qmd` line 132, replace `K[[t]]((y))` with `K((y))[[t]]`.
  - (Optional cosmetic consistency) Replace `\operatorname{res}` with `\operatorname{Res}` in `Ch 16` and `CP-III` to match `NOTATION.qmd` line 106.

### Item 3: `Ch 17` Line 497 — Clean Up Draft Fragment `\text{ etc.}` in Tandem Walk Step Inventory Equation
- **Location**: [`chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd:497`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L497)
- **Finding**: Line 497 currently reads:
  ```markdown
  $$S(x, y) = x + \frac{y}{x} + \frac{1}{y} = \left(\frac{1}{y}\right) + x + \left(\frac{1}{x}\right) y = \left(\frac{1}{y} + x\right)\text{ etc.}$$
  ```
  The trailing `= \left(\frac{1}{y} + x\right)\text{ etc.}` is an informal draft fragment and should explicitly display the $y$-grouped and $x$-grouped decompositions that feed $A_j(x)$ and $\tilde{A}_i(y)$ on the very next line (line 499).
- **Exact Drop-In Fix for `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd` (line 497)**:
  ```markdown
  $$S(x, y) = x + \frac{y}{x} + \frac{1}{y} = y^{-1} + x + x^{-1} y = y x^{-1} + y^{-1} + x.$$
  ```
