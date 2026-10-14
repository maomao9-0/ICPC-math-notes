# Phase 3 Iteration 1 Global Specialist Audit: Abstract Math & Notation Clarity

**Auditor**: `fps-textbook-critic` (Global Specialist #4 — Abstract Math & Notation Clarity)  
**Scope**: `NOTATION.qmd` and all 24 chapters (`chapters/ch01-*.qmd` through `chapters/ch24-*.qmd`)  
**Audit Dimensions**:
1. Abstract Mathematical Foundations Explained from First Principles
2. Local Algebraic Hypotheses & Characteristic-$p$ Limits
3. Global Notation Synchronization with `NOTATION.qmd`
4. Quarto Formatting & Hygiene Sweep

---

## Executive Summary

Across all 24 chapters and `NOTATION.qmd`, the textbook exhibits an exceptionally high level of mathematical rigor and pedagogical clarity:
- **First-Principles Strengths**: `Ch 11` (§11.1, lines 55–143) gives a crystal-clear, division-free motivation for why doubly-infinite series fail to form a ring and how the formal Laurent field $K((x))$ and formal residue $\operatorname{Res}_{x=0}$ resolve this; `Ch 16` (§16.1, lines 44–88) clearly motivates the 5-level bivariate ring hierarchy $K[[x,y]] \subset K((x))[[y]]$ and $\operatorname{Diag}_{x,y}$; `Ch 18` (§18.1, lines 50–109) and `Ch 19` (§19.1, lines 28–96) build the Weyl algebra $K[x]\langle D_x \rangle$, Euler operator $\vartheta = xD_x$, and Ore shift algebra $K[n]\langle E_n \rangle$ from first principles; `Ch 23` (§23.1, lines 30–97) introduces Gaussian $q$-binomials $\begin{bmatrix} n \\ k \end{bmatrix}_q$ via three concrete combinatorial models; and `Ch 24` (§24.1–24.2, lines 33–187) constructs monoid algebras and the set power series ring $K[x_0,\dots,x_{n-1}]/(x_0^2,\dots,x_{n-1}^2)$ from scratch.
- **Quarto Hygiene Baseline**: Across all 25 inspected `.qmd` files, there are **0** forbidden `\(` or `\[` delimiters, **0** unescaped `|` inside `$...$` in Markdown tables, and **100%** balanced `<details>`/`</details>` and `:::` fenced blocks.

However, our line-by-line audit surfaced **29 actionable findings** across the 4 dimensions that should be patched to achieve 100% first-principles accessibility, local hypothesis completeness, global notation synchronization, and Quarto render safety:
- **Dimension 1 (First-Principles Definitions)**: **4 findings** (`Ch 01` early ring/ideal/valuation/Cauchy convergence terminology before definition; `Ch 06` umbral evaluation functional; `Ch 17` missing Schur basis $s_\lambda$ alongside $e_k, h_k, p_k$; `Ch 20` explicit definition of the transposed dual space $K[x]_{<n}^*$).
- **Dimension 2 (Local Algebraic Hypotheses & Char-$p$ Limits)**: **3 findings** (`Ch 02` Proposition 2.4 missing inline $p > N$ hypothesis inside the theorem box; `Ch 04` §4.1–4.2 $\operatorname{SET}/\operatorname{CYC}$ formulas missing inline $p > N$ annotation; `Ch 16` Theorem 16.2 Furstenberg quadratic shortcut missing explicit $\operatorname{char}(K) \neq 2, p > N$ hypothesis).
- **Dimension 3 (Global Notation Synchronization with `NOTATION.qmd`)**: **8 findings** (5 missing/incomplete operator rows in `NOTATION.qmd`, plus lowercase `\operatorname{res}` in `Ch 16` & `Ch 21`, capitalized `*_{\text{XOR}}` in `Ch 24`, and lowercase `\operatorname{diag}` for series diagonal in `Ch 18`).
- **Dimension 4 (Quarto Formatting & Hygiene Sweep)**: **14 findings** (1 display-math factorial collision `!$$` in `Ch 08`, 14 inline `![` factorial-bracket collisions across 7 chapters, 4 raw `"Wait"` draft self-corrections in `Ch 02`, `Ch 03`, `Ch 07`, and 3 broken internal `.qmd` links in `Ch 16` and `Ch 18`).

---

## Dimension 1: Abstract Mathematical Foundations Explained from First Principles

### Finding 1.1 — `Ch 01`: Unexplained Ring, Ideal, Quotient Ring, $\mathfrak{m}$-adic Valuation Alias $\operatorname{ord}_x$, and Cauchy Convergence at First Introduction
- **File**: `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd`
- **Lines**: `27–38` and `158–194`
- **Issue**:
  1. Line 27 states *"Let $K$ be a commutative ring..."* and lines 146–148 use *"ideal $(x^N)$"*, *"quotient ring $K[[x]]/(x^N)$"*, and *"integral domain"* before explaining what a commutative ring, unit group $K^\times$, field, ideal, or quotient ring mean in plain competitive programming terms (the Ring vs. Field box currently appears much later at line 237).
  2. Lines 158–194 define $\nu(F) = \operatorname{val}(F)$, but do not mention the standard alias $\operatorname{ord}_x(F)$ (or why it is called the $\mathfrak{m}$-adic valuation for the maximal ideal $\mathfrak{m} = (x)$), nor do they explicitly define **Cauchy convergence in the valuation metric** ($\operatorname{val}(S_{k+1} - S_k) \to \infty \iff$ every coefficient $[x^n]S_k$ freezes after finitely many steps, which is the exact reason Newton iteration $G_{k+1}$ converges in §1.4 without knowing the limit series $G$ beforehand).
- **Drop-in Fix 1 (Insert right after Line 38 of `chapters/ch01-ring-convolutions-newton-inv.qmd`)**:
```markdown
::: {.callout-note title="First Principles: Commutative Rings $R$, Units $R^\times$, and Fields $K$"}
Throughout this book, our coefficient system is either a **commutative ring** $R$ or a **field** $K$:

- **Commutative Ring ($R$)**: A set equipped with addition ($+$), subtraction ($-$), and commutative multiplication ($\cdot$) with an additive identity $0$ and multiplicative identity $1$ (for example, the integers $\mathbb{Z}$, modular integers $\mathbb{Z}/m\mathbb{Z}$ for composite $m$, or polynomials $K[y]$). Division is **not** guaranteed in a general ring.
- **Unit ($u \in R^\times$)**: An element $u \in R$ that possesses a multiplicative inverse $u^{-1} \in R$ satisfying $u \cdot u^{-1} = 1$. In $\mathbb{Z}/m\mathbb{Z}$, $u$ is a unit if and only if $\gcd(u, m) = 1$. The set of all units forms the **unit group** $R^\times$.
- **Integral Domain**: A commutative ring with no nonzero **zero divisors** ($a \cdot b = 0 \implies a = 0$ or $b = 0$).
- **Field ($K$)**: A commutative ring in which **every nonzero element is a unit** ($K^\times = K \setminus \{0\}$), such as $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ for a prime $p$.
:::
```
- **Drop-in Fix 2 (Replace Lines 145–194 of `chapters/ch01-ring-convolutions-newton-inv.qmd`)**:
```markdown
Instead, we replace analytic convergence with **algebraic truncation** (the **formal topology** or **$\mathfrak{m}$-adic topology**). For each integer $N \ge 1$, the set of series whose first $N$ coefficients vanish ($f_0 = f_1 = \dots = f_{N-1} = 0$) is closed under addition and under multiplication by *any* series in $K[[x]]$; in algebra, such a "multiples-absorbing" subset is called an **ideal**, denoted $(x^N) = x^N K[[x]]$. Identifying two series whenever their difference lies in $(x^N)$ yields the **quotient ring** $K[[x]] / (x^N) \cong K[x] / (x^N)$: concretely, arithmetic in $K[[x]] / (x^N)$ is simply ordinary polynomial arithmetic where every term of degree $\ge N$ is discarded ($\bmod\; x^N$).

To measure how many leading coefficients of a series vanish, we define its **valuation** (also called the **order** $\operatorname{ord}_x(F)$ or **$\mathfrak{m}$-adic valuation** with respect to the ideal $\mathfrak{m} = (x)$):

::: {#def-valuation}
### Definition 1.1 (Formal Valuation $\nu(F) = \operatorname{val}(F) = \operatorname{ord}_x(F)$)
For a nonzero formal power series $F(x) = \sum_{n=0}^{\infty} f_n x^n \in K[[x]]$, its **valuation** (denoted interchangeably by $\nu(F)$, $\operatorname{val}(F)$, or $\operatorname{ord}_x(F)$) is the smallest index $n \ge 0$ such that $[x^n] F(x) \neq 0$:
$$
\nu(F) = \operatorname{val}(F) = \operatorname{ord}_x(F) := \min \{ n \ge 0 : f_n \neq 0 \}.
$$
By convention, the zero series has valuation $\nu(0) = +\infty$. Over an integral domain $K$, valuation satisfies:

1. $\nu(F \cdot G) = \nu(F) + \nu(G)$ (in particular, $\nu(F^k) = k \cdot \nu(F)$), and
2. $\nu(F \pm G) \ge \min(\nu(F), \nu(G))$ (the **strong triangle inequality**).
:::

The valuation induces a formal distance $d(F, G) := 2^{-\operatorname{val}(F - G)}$ between power series: two series are "close" not when their numerical values are small, but when they agree on a long prefix of coefficients ($F \equiv G \pmod{x^N} \iff \operatorname{val}(F - G) \ge N$). A sequence of series $(S_k)_{k \ge 0}$ is **Cauchy in the valuation metric** if $\operatorname{val}(S_{k+1} - S_k) \to \infty$ as $k \to \infty$. Because $K[[x]]$ is **complete** under this metric, every Cauchy sequence converges to a unique limit series $S(x) \in K[[x]]$—for each target degree $n$, once $\operatorname{val}(S_{k+1} - S_k) > n$ for all $k \ge K(n)$, the coefficient $[x^n] S_k$ is permanently frozen! This Cauchy completeness is why Newton iteration ($G_{k+1} \equiv G_k \pmod{x^{2^k}}$) can construct an unknown series $G(x)$ purely from prefix agreements.

Consequently, an infinite sum $\sum_{k=0}^{\infty} A_k(x)$ or infinite product $\prod_{k=1}^{\infty} (1 + B_k(x))$ is **formally summable** (or **formally convergent**) in $K[[x]]$ if and only if the valuations of the perturbations grow to infinity:
$$
\lim_{k \to \infty} \nu(A_k) = +\infty \qquad \text{or} \qquad \lim_{k \to \infty} \nu(B_k) = +\infty.
$$
```

---

### Finding 1.2 — `Ch 06`: Explicit First-Principles Definition of Umbral Evaluation as a Linear Functional
- **File**: `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd`
- **Lines**: `420–455` (§6.4 Stirling Numbers & Basis Conversion)
- **Issue**: While `Ch 06` derives the shift algebra $\Delta = E - I$ (§6.3) and conversions between ordinary powers $x^n$ and falling factorials $x^{\underline{k}}$ (§6.4), it does not explicitly define **umbral evaluation** from first principles as a $K$-linear functional $L : K[x] \to K$ (replacing symbolic powers $u^k$ or falling factorials $x^{\underline{k}}$ by sequence elements $a_k$ via linearity), which is referenced in the curriculum architecture and connects basis change to linear functionals.
- **Drop-in Fix (Insert after Line 442 of `chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd`)**:
```markdown
::: {.callout-note title="First Principles: Umbral Calculus as a Linear Functional on $K[x]$"}
In classical combinatorics, **umbral calculus** (`[EN]` umbral evaluation / `[ZH]` 阴算子 / 符号幂代换) is often written via the shorthand $(a + b)^n \mapsto \sum_{k=0}^n \binom{n}{k} a_k b^{n-k}$, where exponents $a^k$ are "lowered to subscripts" $a_k$ after expansion. There is zero mystery in this notation: it is simply the application of a **$K$-linear functional** $L_a : K[u] \to K$ defined on the basis of monomials by $L_a(u^k) := a_k$ (or on the falling-factorial basis by $L(x^{\underline{k}}) := y^k$). Because $L_a$ is linear, applying $L_a$ to any polynomial identity in $u$—such as $(u + 1)^n = \sum_{k=0}^n \binom{n}{k} u^k$ or $x^n = \sum_{k=0}^n \left\{ \begin{matrix} n \\ k \end{matrix} \right\} x^{\underline{k}}$—immediately produces a valid scalar identity $L_a((u+1)^n) = \sum_{k=0}^n \binom{n}{k} a_k$ without any hand-waving.
:::
```

---

### Finding 1.3 — `Ch 17`: Complete the Four Canonical Symmetric Function Bases by Defining Schur Functions $s_\lambda$ alongside $e_k, h_k, p_k$
- **File**: `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`
- **Lines**: `325–359` (§17.3 Symmetric Functions, Newton's Identities & MacMahon Master Theorem)
- **Issue**: §17.3 introduces the ring of symmetric functions $\Lambda = K[x_1, \dots, x_m]^{\mathfrak{S}_m}$ and defines three of the four classical bases ($e_k$, $h_k$, $p_k$) on lines 331–346, but omits the fourth canonical basis—the **Schur functions $s_\lambda$**—specified in the curriculum's abstract math foundations.
- **Drop-in Fix (Insert item 4 right after Line 346 of `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`)**:
```markdown
4. **Schur Symmetric Functions ($s_\lambda$, indexed by integer partitions $\lambda = (\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_\ell > 0)$)**:
   $$
   s_\lambda(x_1, \dots, x_m) := \frac{\det_{1 \le i, j \le m}\!\left(x_i^{\lambda_j + m - j}\right)}{\det_{1 \le i, j \le m}\!\left(x_i^{m - j}\right)} = \det_{1 \le i, j \le \ell}\!\left( h_{\lambda_i - i + j} \right) \quad \text{(Jacobi–Trudi identity)},
   $$
   where $h_0 = 1$ and $h_r = 0$ for $r < 0$. Combinatorially, $s_\lambda$ is the generating function of **semistandard Young tableaux (SSYT)** of shape $\lambda$ (equivalently, non-intersecting lattice path systems via the Lindström–Gessel–Viennot lemma of Chapter 13). While $e_k$, $h_k$, and $p_k$ generate $\Lambda$ multiplicatively as polynomials, the Schur functions $\{s_\lambda\}$ form an orthonormal $K$-linear basis of $\Lambda$.
```

---

### Finding 1.4 — `Ch 20`: Explicit First-Principles Definition of the Transposed Dual Space $K[x]_{<n}^*$
- **File**: `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd`
- **Lines**: `55–78` and `172–207` (§20.1–20.2)
- **Issue**: §20.1–20.2 speaks of "covectors $\mathbf{w}$" and transposed Toeplitz multiplication $T_B^\top \mathbf{c}$, and `Ch 21` (lines 71, 223, 273) later refers to *"the dual space $K[x]_{<n}^*$"* as a concept established in `Ch 20`, but `Ch 20` never explicitly writes down the notation $K[x]_{<n}^*$ or defines from first principles what an element of $K[x]_{<n}^*$ is.
- **Drop-in Fix (Insert after Line 195 of `chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd`)**:
```markdown
::: {.callout-note title="First Principles: The Transposed Dual Space $K[x]_{<n}^*$ and Formal Laurent Covectors"}
In linear algebra, given the $n$-dimensional vector space of polynomials $V_n = K[x]_{<n} = \operatorname{span}_K\{1, x, \dots, x^{n-1}\}$, its **dual space**—denoted $K[x]_{<n}^* := \operatorname{Hom}_K(K[x]_{<n}, K)$—is the space of all $K$-linear functionals $\ell : K[x]_{<n} \to K$.

A linear functional $\ell \in K[x]_{<n}^*$ is uniquely determined by the $n$-tuple of numbers $c_j := \ell(x^j)$ for $0 \le j < n$: for any polynomial $A(x) = \sum_{j=0}^{n-1} a_j x^j \in K[x]_{<n}$, linearity gives $\ell(A) = \sum_{j=0}^{n-1} c_j a_j = \langle \mathbf{c}, \mathbf{a} \rangle$. Equivalently, if we encode $\ell$ as the formal series $C(x) = \sum_{j=0}^{n-1} c_j x^j$, then $\ell(A) = [x^0]\big(C(x) A(x^{-1})\big)$.

Under this duality, the forward multiplication map $M_B : K[x]_{<n} \to K[x]_{<n+m-1}$ defined by $A(x) \mapsto A(x)B(x)$ induces a dual map $M_B^\top : K[x]_{<n+m-1}^* \to K[x]_{<n}^*$ given by $\ell \mapsto (\ell \circ M_B)$. Evaluating $(\ell \circ M_B)(x^i) = \ell(x^i B(x)) = \sum_{j=0}^{m-1} b_j \ell(x^{i+j}) = \sum_{j=0}^{m-1} b_j c_{i+j}$ recovers our exact **transposed multiplication (middle product)** $\operatorname{mulT}(C, B)$! Thus, $\operatorname{mulT}(C, B)$ is simply the natural action of $B(x)$ on the dual space $K[x]_{<n+m-1}^* \to K[x]_{<n}^*$.
:::
```

---

## Dimension 2: Local Algebraic Hypotheses & Characteristic-$p$ Limits

### Finding 2.1 — `Ch 02`: State the Characteristic Hypothesis $1, 2, \dots, N \in K^\times$ Inside Proposition 2.4 (`\exp` ODE Equivalence)
- **File**: `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd`
- **Line**: `163–177`
- **Issue**: Proposition 2.4 (`### Proposition 2.4 (ODE Characterization of Formal Exp and Log)`) states $F(x) = \exp(B(x)) \iff F'(x) = B'(x) F(x)$ with $[x^0]F(x) = 1$, but defers the hypothesis that $1, 2, \dots, N$ must be units in $K$ ($\operatorname{char}(K) = 0$ or $p > N$) to the prose below the box (line 179). Placing the local algebraic hypothesis right inside the Proposition header/statement ensures compliance with the `AGENTS.md` local-hypothesis policy.
- **Drop-in Fix (Replace Lines 163–167 of `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd`)**:
```markdown
::: {#prp-exp-log-ode}
### Proposition 2.4 (ODE Characterization of Formal Exp and Log)
Let $K$ be a commutative ring in which $1, 2, \dots, N \in K^\times$ (in particular, $\operatorname{char}(K) = 0$ or $K = \mathbb{F}_p$ with prime $p > N$). For any series $A(x) \in K[[x]] / (x^{N+1})$ with $[x^0]A(x) = 1$, and any series $B(x) \in K[[x]] / (x^{N+1})$ with $[x^0]B(x) = 0$:
```

---

### Finding 2.2 — `Ch 04`: Annotate the Local Hypothesis $p > N$ Beside the $\operatorname{SET} \implies \exp$ and $\operatorname{CYC} \implies \ln\frac{1}{1-A}$ EGF Formulas in §4.1–4.2
- **File**: `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd`
- **Lines**: `148–160` and `235–245`
- **Issue**: In §4.2, the EGF identities $B(x) = \exp(A(x))$ for $\mathcal{B} = \operatorname{SET}(\mathcal{A})$ and $C(x) = \ln\frac{1}{1-A(x)}$ for $\mathcal{C} = \operatorname{CYC}(\mathcal{A})$ state the valuation precondition $a_0 = [x^0]A(x) = 0$, but defer the characteristic precondition $p > N$ (needed because $k! \in K^\times$ for $1 \le k \le N$) to the Failure Mode callout box later in §4.2. Adding a brief inline parenthetical $(\text{requiring } a_0 = 0 \text{ and } 1, 2, \dots, N \in K^\times \text{ modulo } x^{N+1})$ right next to the boxed $\operatorname{SET}$ and $\operatorname{CYC}$ equations makes the local hypothesis immediately visible at every division by $k!$.
- **Drop-in Fix (In `chapters/ch04-egf-set-cyc-boxed-prufer.qmd`, Line 157 and Line 242)**:
  - At Line 157, after `$$C(x) = \sum_{k=1}^{\infty} \frac{A(x)^k}{k} = \ln \frac{1}{1 - A(x)}.$$`, append:
    `*(Local Algebraic Hypothesis: Requires $[x^0]A(x) = 0$ for formal convergence and $1, 2, \dots, N \in K^\times$—i.e., $p > N$ over $\mathbb{F}_p$—when computing modulo $x^{N+1}$.)*`
  - At Line 242, after `$$B(x) = \sum_{k=0}^{\infty} \frac{A(x)^k}{k!} = \exp(A(x)).$$`, append:
    `*(Local Algebraic Hypothesis: Requires $[x^0]A(x) = 0$ and $1, 2, \dots, N \in K^\times$, i.e., $p > N$ over $\mathbb{F}_p$, when computing modulo $x^{N+1}$.)*`

---

### Finding 2.3 — `Ch 16`: Explicitly State $\operatorname{char}(K) \neq 2$ and $p > N$ in Theorem 16.2 (Furstenberg's Rational Diagonal Quadratic Shortcut)
- **File**: `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`
- **Lines**: `516–536`
- **Issue**: Theorem 16.2 (`### Theorem 16.2 (Furstenberg's Rational Diagonal Residue Formula & 1-Line Quadratic Shortcut)`) writes the inverse square root $\frac{1}{\sqrt{\beta(t)^2 - 4\alpha(t)\gamma(t)}}$ assuming $\beta(0) = 1$, without stating inside the theorem box that extracting the square root and D-finite recurrence up to degree $N$ requires $\operatorname{char}(K) \neq 2$ (and $p > N$ for D-finite ODE unrolling / Newton `sqrt`, whereas $p \le N$ uses the Regime 4 Frobenius bypass of §16.3).
- **Drop-in Fix (Replace Lines 529–535 of `chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`)**:
```markdown
In particular, if $Q_t(z) = \alpha(t) z^2 + \beta(t) z + \gamma(t)$ is **quadratic** in $z$ with $\gamma(0) = 0$ and $\beta(0) = 1$, then over any field $K$ with $\operatorname{char}(K) \neq 2$ (and $p > N$ when evaluating up to $t^N$ via Newton `sqrt` or D-finite ODE unrolling), $Q_t(z)$ has a unique small root $z_1(t) \in t K[[t]]$ and:
$$
\operatorname{Diag}_{x,y} F(x, y) = \operatorname{Res}_{z=z_1(t)} \frac{P(z, t/z)}{\alpha(t) z^2 + \beta(t) z + \gamma(t)} \, dz = \left. \frac{P(z, t/z)}{\sqrt{\beta(t)^2 - 4\alpha(t)\gamma(t)}} \right|_{z = z_1(t)}.
$$
*(If $P(x, y) = 1$, this simplifies directly to $\operatorname{Diag}_{x,y} \frac{1}{H(x,y)} = \frac{1}{\sqrt{\beta(t)^2 - 4\alpha(t)\gamma(t)}}$. When $p \le N$, replace the square-root ODE with the Frobenius reduction of §16.3.)*
```

---

## Dimension 3: Global Notation Synchronization with `NOTATION.qmd`

### Finding 3.1 — `NOTATION.qmd`: Add Missing Canonical Entries and Aliases Used Across `Ch 01`–`Ch 24`
- **File**: `/home/maomao90/Documents/IO/ICPC-math-notes/NOTATION.qmd`
- **Lines**: `114–126`
- **Issue**: Several standard symbols and aliases used heavily across the 24 chapters are either omitted from the `NOTATION.qmd` Master Operator Table or listed without their chapter aliases:
  1. Line 114 lists $[x^n] F(x)$ but omits bivariate/multivariate extraction $[x^k y^m] F(x,y)$ and iterated extraction $[x^k]([y^m] F(x,y))$.
  2. Line 118 lists $\nu(F) = \operatorname{val}(F)$ but omits the standard aliases $\operatorname{ord}_x(F)$ and $\operatorname{val}_x(F)$ used in `Ch 11`, `Ch 16`, and `Ch 23`.
  3. Line 122 lists $\vartheta = x D$ but omits the multivariate/subscripted variants $\vartheta_x = x D_x$ and $\Theta_x = x \partial_x$ used in `Ch 16`–`Ch 19`.
  4. Line 124 lists $\operatorname{Res}_{x=0} F(x)$ but omits the shorthand $\operatorname{Res}_x F(x)$ and differential notation $\operatorname{Res}_{x=0} F(x)\,dx$ used in `Ch 11`, `Ch 17`, `Ch 19`, and `Ch 21`.
  5. Falling/rising factorials ($x^{\underline{k}}, x^{\overline{k}}$), Karamata Stirling/Eulerian brackets ($\left\{\begin{matrix} n \\ k \end{matrix}\right\}, \left[\begin{matrix} n \\ k \end{matrix}\right], \left\langle\begin{matrix} n \\ k \end{matrix}\right\rangle$), shift/difference operators ($E, \Delta$), multivariate diagonal ($\operatorname{Diag}_{x,y}$), transposed multiplication ($\operatorname{mulT}(C, B)$), and bitwise/subset convolutions ($*_{\text{or}}, *_{\text{and}}, *_{\text{xor}}, *_{\text{sub}}$) are missing from the `NOTATION.qmd` table.
- **Drop-in Fix (Replace Lines 114–126 of `/home/maomao90/Documents/IO/ICPC-math-notes/NOTATION.qmd`)**:
```markdown
| $[x^n] F(x)$, $[x^k y^m] F(x,y)$ | Coefficient extraction: $[x^n] \sum f_k x^k := f_n$; multivariate $[x^k y^m] F(x,y) := [x^k]\big([y^m] F(x,y)\big) = f_{k,m}$ |None (pure $K$-linear functional) |
| $F(x) \bmod x^N$ | Degree truncation: projection onto $R[x]/(x^N)$, keeping terms $x^0, \dots, x^{N-1}$ |None |
| $\deg(P)$ | Degree of a polynomial $P \in R[x]$, with $\deg(0) := -\infty$ | $P$ is a finite polynomial |
| $\nu(F) = \operatorname{val}(F) = \operatorname{ord}_x(F)$ | Formal ($\mathfrak{m}$-adic) valuation: $\min\{n \in \mathbb{Z} : [x^n]F(x) \neq 0\}$, with $\nu(0) := +\infty$ (written $\operatorname{val}_x(F)$ or $\operatorname{ord}_x(F)$ when the variable is emphasized) |None |
| $D F(x) = F'(x)$ | Formal derivative: $\sum_{n \ge 1} n f_n x^{n-1}$ |None |
| $\int F(x)\,dx$ | Formal integral: $\sum_{n \ge 0} \frac{f_n}{n+1} x^{n+1}$ (constant term $0$) | $1, 2, \dots, N \in R^\times$ ($\operatorname{char}(K) = 0$ or $p > N$) |
| $\vartheta = x D$ (or $\vartheta_x = x D_x$, $\Theta_x = x \partial_x$) | Theta / Euler pointing operator: $\vartheta F(x) = x F'(x) = \sum_{n \ge 0} n f_n x^n$ |None |
| $E$ (or $E_n$) and $\Delta = E - I$ | Forward shift operator ($E f_n = f_{n+1}$) and forward difference operator ($\Delta f_n = f_{n+1} - f_n$) |None |
| $\operatorname{Res}_{x=0} F(x) = \operatorname{Res}_x F(x)$ | Formal residue (also written $\operatorname{Res}_{x=0} F(x)\,dx$): $[x^{-1}] F(x)$ for $F(x) \in K((x))$ | $F(x) \in K((x))$ is a formal Laurent series |
| $\operatorname{Diag}_{x,y} F(x,y)$ | Bivariate diagonal operator: $\sum_{n \ge 0} ([x^n y^n] F(x,y)) t^n$ | $F(x,y) \in K[[x,y]]$ (or diagonally summableLaurent series) |
| $\operatorname{mulT}(C, B) = T_B^\top \mathbf{c}$ | Transposed multiplication (middle product) on the dual space $K[x]_{<n+m-1}^* \to K[x]_{<n}^*$: $[x^i]\operatorname{mulT}(C, B) := \sum_{j=0}^{m-1} b_j c_{i+j}$ |None |
| $x^{\underline{k}}$, $x^{\overline{k}}$ | Falling factorial $x(x-1)\cdots(x-k+1)$ and rising factorial $x(x+1)\cdots(x+k-1)$ |None |
| $\left\{ \begin{matrix} n \\ k \end{matrix} \right\}$, $\left[ \begin{matrix} n \\ k \end{matrix} \right]$, $\left\langle \begin{matrix} n \\ k \end{matrix} \right\rangle$ | Stirling numbers of the second kind, unsigned Stirling numbers of the first kind, and Eulerian numbers (Karamata notation) |None |
| $\begin{bmatrix} n \\ k \end{bmatrix}_q$, $(a; q)_n$ | Gaussian $q$-binomial coefficient $\frac{(q;q)_n}{(q;q)_k (q;q)_{n-k}}$ and $q$-Pochhammer symbol $\prod_{j=0}^{n-1}(1 - a q^j)$ |None (polynomial in $q$) |
| $*_{\text{or}}$, $*_{\text{and}}$, $*_{\text{xor}}$, $*_{\text{sub}}$ | Bitwise OR, AND, XOR convolutions on $K^{2^n}$ and subset convolution on $K[x_0,\dots,x_{n-1}]/(x_0^2,\dots,x_{n-1}^2)$ | $*_{\text{xor}}$ inversion requires $2 \in K^\times$ ($\operatorname{char}(K) \neq 2$) |
```

---

### Finding 3.2 — `Ch 16` & `Ch 21`: Synchronize Lowercase `\operatorname{res}` to Capitalized `\operatorname{Res}`
- **Files & Lines**:
  1. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`: Lines `11, 506, 509, 522, 531, 581, 582, 585, 621, 633, 635, 643`
  2. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd`: Lines `8, 285, 293, 300, 302, 304, 315, 341`
- **Issue**: `NOTATION.qmd` (line 124) and `Ch 11`, `Ch 17`, `Ch 19` standardize the formal residue operator as capitalized `\operatorname{Res}` ($\operatorname{Res}_{x=0}$ or $\operatorname{Res}_x$), whereas `Ch 16` and `Ch 21` use lowercase `\operatorname{res}_z` and `\operatorname{res}_u`.
- **Drop-in Fix**: Replace all occurrences of `\operatorname{res}` with `\operatorname{Res}` on the listed lines in `chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd` and `chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd`.

---

### Finding 3.3 — `Ch 18`: Synchronize Lowercase `\operatorname{diag} R(x, y)` to `\operatorname{Diag}_{x,y} R(x, y)`
- **File**: `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd`
- **Lines**: `28` and `251`
- **Issue**: Lines 28 and 251 of `Ch 18` write `\operatorname{diag} R(x, y)` for the bivariate series diagonal, whereas `Ch 16` (§16.1–16.4) and `NOTATION.qmd` use capitalized `\operatorname{Diag}_{x,y}` to distinguish the series diagonal operator from the diagonal matrix constructor `\operatorname{diag}(x_1, \dots, x_d)` in `Ch 17`.
- **Drop-in Fix**:
  - Line 28: Change `\operatorname{diag} R(x, y)` $\to$ `\operatorname{Diag}_{x,y} R(x, y)`.
  - Line 251: Change `\operatorname{diag} R(x, y)` $\to$ `\operatorname{Diag}_{x,y} R(x, y)`.

---

### Finding 3.4 — `Ch 24`: Synchronize `*_{\text{XOR}}` to Lowercase `*_{\text{xor}}`
- **File**: `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd`
- **Line**: `87`
- **Issue**: Line 87 writes `*_{\text{XOR}}`, whereas the curriculum specification and `NOTATION.qmd` standardize on lowercase `*_{\text{or}}, *_{\text{and}}, *_{\text{xor}}, *_{\text{sub}}`.
- **Drop-in Fix (Line 87 of `chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd`)**:
  - Change `*_{\text{XOR}}` $\to$ `*_{\text{xor}}`.

---

## Dimension 4: Quarto Formatting & Hygiene Sweep

### Finding 4.1 — `Ch 08`: Display-Math Factorial Collision `!$$`
- **File**: `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd`
- **Line**: `118`
- **Issue**: Line 118 ends an inline display-math block with `(n - j)!$$`, which collides `!` with `$$` and violates the `AGENTS.md` Quarto Math Hygiene Policy (`never place ! immediately before $ or $$`).
- **Drop-in Fix (Line 118 of `chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd`)**:
  - Replace:
    `$$\text{Valid placements of } j \text{ rooks, with the remaining } n - j \text{ rooks placed arbitrarily: } r_j(B) \cdot (n - j)!$$`
  - With:
    `$$\text{Valid placements of } j \text{ rooks, with the remaining } n - j \text{ rooks placed arbitrarily: } r_j(B) \cdot (n - j)! $$`

---

### Finding 4.2 — 7 Chapters: 14 Inline `n![x^n]` Factorial-Bracket Collisions (`![` Inside Math)
- **Files & Lines**:
  1. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd`: Lines `172` (twice: `n![x^n]` and `k![x^k]`), `190` (`k![x^k]`), `661` (`n![x^n]`), `917` (`n![x^n]`), `1127` (`n![x^n]`)
  2. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd`: Line `842` (`n![x^n]`)
  3. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`: Lines `129` (`n![x^n]`), `242` (`n![x^n]`), `268` (`n![x^n]`)
  4. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd`: Line `1573` (`n![x^n]`)
  5. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd`: Line `3` (`n![x^n]`)
  6. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd`: Lines `1226` (`(n-2)![x^n]`), `1248` (`(n-2)![x^n]`)
  7. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd`: Line `841` (`(n-1)![x^n]`)
- **Issue**: Writing `![` without a space (`n![x^n]`) both risks Markdown image parser interference in edge cases and cramps the factorial symbol against the bracket `[x^n]`.
- **Drop-in Fix**: Insert a LaTeX thin space `\,` between `!` and `[` in all 14 occurrences (`n!\,[x^n]`, `k!\,[x^k]`, `(n-1)!\,[x^n]`, `(n-2)!\,[x^n]`).

---

### Finding 4.3 — `Ch 02`, `Ch 03`, `Ch 07`: 4 Raw `"Wait"` Stream-of-Consciousness Self-Corrections
- **Files & Lines**:
  1. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd`, Line `290`:
     - Current: `Wait: for $\Phi'(G_0) = 2 g_0$ to be a unit in $K$, we need **both** $g_0 \in K^\times$ **and** $2 \in K^\times$!`
     - Drop-in Fix: `Crucial algebraic check: for $\Phi'(G_0) = 2 g_0$ to be a unit in $K$, we need **both** $g_0 \in K^\times$ **and** $2 \in K^\times$!`
  2. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd`, Line `1206`:
     - Current: `Wait: can we simplify even further for coding speed? Notice that since $1 - x - x^2$ is quadratic...`
     - Drop-in Fix: `**Implementation shortcut**: Because $1 - x - x^2$ is quadratic...`
  3. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd`, Line `1277`:
     - Current: `Wait: the modulus is $23333333$, which is a prime, and $n \le 10^5 < 23333333$, so every integer $1, 2, \dots, n$ is invertible modulo $p$!`
     - Drop-in Fix: `**Modulus check**: Because $p = 23333333$ is prime and $n \le 10^5 < p$, every integer $1, 2, \dots, n$ is a unit in $\mathbb{F}_p$!`
  4. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd`, Line `328`:
     - Current: `4. **Wait—test this over a finite field $\mathbb{F}_p$!** Suppose $p = 998244353$ and $m = 5$.`
     - Drop-in Fix: `4. **Finite-field stress test over $\mathbb{F}_p$**: Suppose $p = 998244353$ and $m = 5$.`

---

### Finding 4.4 — `Ch 16` & `Ch 18`: 3 Broken Internal `.qmd` Cross-Reference Links
- **Files & Lines**:
  1. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`, Line `1113`:
     - Current: `[Chapter 18: Algebraic Series, D-Finite Functions & P-Recursions](ch18-algebraic-series-d-finite-p-recursions.qmd)`
     - Drop-in Fix: `[Chapter 18: D-Finite Series, the Weyl Algebra, P-Recursive Sequences & Indicial Lifting](ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd)`
  2. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`, Line `1210`:
     - Current: `[Chapter 8: Inclusion-Exclusion, Möbius Inversion, Euler Transform & Burnside](../part2-combinatorial-translation/ch08-PIE-mobius-euler-transform-burnside.qmd)`
     - Drop-in Fix: `[Chapter 8: Connected-Component Inclusion-Exclusion, Rook Polynomials & Goulden-Jackson](ch08-connected-component-ie-rook-goulden-jackson.qmd)`
  3. `/home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd`, Line `263`:
     - Current: `[Part IV Synthesis Checkpoint](../checkpoints/cp4-part4-synthesis-checkpoint.qmd)`
     - Drop-in Fix: `[Part IV Synthesis Checkpoint](../checkpoints/cp04-part4-pgf-walks-multivariate.qmd)`
