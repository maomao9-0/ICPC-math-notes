# Part V Critic C Audit Report: Algorithm Contracts, Failure Modes, Code Snippets & Quarto Syntax/Layout (`Ch 18`–`Ch 21` + `CP-V`)

**Auditor**: Critic C (`fps-textbook-critic` — Algorithm Contracts, Failure Modes, Code Snippets & Quarto Syntax/Layout)  
**Target Files**:
1. [`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd) (`1,148` lines)
2. [`chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd) (`1,123` lines)
3. [`chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd) (`1,215` lines)
4. [`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd) (`1,089` lines)
5. [`checkpoints/cp05-part5-dfinite-transposition-composition.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp05-part5-dfinite-transposition-composition.qmd) (`1,196` lines)

---

## Executive Summary

| Audit Dimension | Status | Summary of Findings |
| :--- | :---: | :--- |
| **1A. Problem Ladder & Checkpoint 5-Part Algorithm Contracts (`40/40` Problems)** | **PASS (with minor field-label harmonization note)** | All `40` problems (`32` chapter ladder problems + `8` `CP-V` checkpoint problems) include an explicit 5-part `#### Algorithm Contract` block inside their collapsible solutions. `Ch 18`, `Ch 20`, and `CP-V` use the canonical 5 labels (`Input & Exact Index Boundaries`, `Preconditions`, `Postconditions (Output)`, `Time & Space Complexity`, `Loop / Algebraic Invariant`), while `Ch 19` and `Ch 21` use slightly abbreviated labels (`Input(s)`, `Output`, `Algebraic Preconditions`/`Preconditions`, `Complexity`, `Correctness Invariant`/`Invariant`). |
| **1B. Main-Text Core Engine Algorithm Contracts (`Ch 18`–`Ch 21`)** | **NEEDS 6 ADDITIONS** | `11` main-text Algorithm Contracts are present (`2` in `Ch 18`, `3` in `Ch 19`, `3` in `Ch 20`, `3` in `Ch 21`), but **6 core engines in the main text** lack a formal 5-part `Algorithm Contract` callout box (`§18.2`, `§18.3`, `§19.1`, `§20.4 Part A`, `§20.4 Part C`, `§21.3`). Drop-in replacements are provided in Section 1. |
| **1C. Mandatory `.callout-warning` Failure-Mode Callouts** | **NEEDS 2 CALLOUT UPGRADES** | `8` `.callout-warning` boxes are present and exemplary (`Ch 18`: Indicial Singularity `I(n^*) ≡ 0 (mod p)`; `Ch 19`: WZ Non-Natural Boundaries, `$1/P'(x)$` Sparsity-Destruction Trap, Shifted Taylor Unrolling Direction; `Ch 20`: `mulT` Cyclic Wrap-Around Window `[m-1, n+m-2]`, Overlap Singularity `c+k ∈ [0, d]`; `Ch 21`: `f_0 ≠ 0` Power Projection trap, `Route A` LIF trap when `p ≤ N`). However, **2 mandatory failure modes** (`Ch 18` §18.3 Archetype 1 Integrating-Factor Trap when $p \le N$, and `Ch 21` §21.4 Degree $p+2$ Artin–Schreier Obstruction) are currently plain `####` headings instead of `.callout-warning` boxes. |
| **2. Code Block Policy & Length Audit ($\le 15$ Lines, Zero Boilerplate)** | **NEEDS 3 COMPRESSIONS** | Zero standard library boilerplate dumps (`NTT`, `modint`, `inv`, `ln`, `exp`) appear anywhere in Part V, and 100% of code blocks carry explicit language tags (`cpp` or `{mermaid}`). However, **3 C++ snippets exceed the strict $\le 15$-line limit** (`ch18` lines `478–496` at `17` lines; `ch21` lines `252–269` at `16` lines; `ch21` lines `410–429` at `18` lines). Drop-in $\le 14$-line replacements are provided in Section 2. |
| **3. Strict Quarto Syntax & Hygiene Audit** | **NEEDS 3 TARGETED FIXES + DISPLAY-MATH SPACING PASS** | Zero `!$$` collisions, zero `\(` or `\[` delimiters, zero unescaped `|` inside `$...$` in Markdown tables, 100% balanced `<details>`/`</summary>`/`</details>` and `:::` blocks with proper surrounding blank lines, and 100% spoiler-free `CP-V` Stage 1. **3 targeted fixes required**: (1) broken internal `.qmd` link in `ch21` line `444` (`ch12-prufer-cayley-block-cut-cactus-graphs.qmd` $\to$ `ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`), (2) raw conversational `"Let's check"` in `cp05` line `739`, (3) missing space after `!` in `ch20` line `167`, plus a blank-line spacing pass around single-line `$$...$$` display math blocks in `ch18`, `ch19`, `ch21`, and `cp05`. |

---

## Area 1: Algorithm Contracts & Failure-Mode Callout Audit (`Ch 18`–`Ch 21` + `CP-V`)

### 1.1 Main-Text Core Engine Algorithm Contracts Inventory

| Chapter & Section | Core Engine / Template | Current Status | Line Numbers | Action Required |
| :--- | :--- | :---: | :---: | :--- |
| **Ch 18 §18.1** | Weyl-Algebra Holonomic Unrolling | Present (`.callout-note`) | `171–181` | None |
| **Ch 18 §18.2** | Abel–Cockle–Harley–Comtet Radical-to-ODE Compiler (Recipes A & B) | **MISSING** | After `278` | **Add Contract 1A below** |
| **Ch 18 §18.3** | Riccati-to-Second-Order Holonomic Linearization | **MISSING** | After `403` | **Add Contract 1B below** |
| **Ch 18 §18.4** | Indicial Singularity Bypass via $p$-Adic Valuation Tracking | Present (`.callout-note`) | `498–506` | None |
| **Ch 19 §19.1** | Coupled ODE-to-P-Recursive Unrolling | **MISSING** | After `113` | **Add Contract 1C below** |
| **Ch 19 §19.2** | Rational-Power & Sparse Composition Unrolling ($P(x)^\alpha$, $\exp(P)$, $\ln(P)$) | Present (`.callout-note`) | `194–201` | None |
| **Ch 19 §19.3A** | Differentiate-Divide-Integrate via Half-GCD (Non-Monic Divisor) | Present (`.callout-note`) | `268–275` | None |
| **Ch 19 §19.3B** | Shifted Truncated Taylor ODE Unrolling for $\sum f_n (P(x)-c)^n$ | Present (`.callout-note`) | `339–346` | None |
| **Ch 20 §20.2** | Transposed Truncated Convolution (`mulT`) | Present (`.callout-note`) | `303–318` | None |
| **Ch 20 §20.3A** | Tellegen Top-Down Multipoint Evaluation (`eval`) | Present (`.callout-note`) | `460–475` | None |
| **Ch 20 §20.3B** | Fast Lagrange Interpolation (`interp`) | Present (`.callout-note`) | `516–530` | None |
| **Ch 20 §20.4A** | Transposed Chirp Z-Transform ($\operatorname{czt}^\top$) | **MISSING** | After `556` | **Add Contract 1D below** |
| **Ch 20 §20.4B** | Shift of Sampling Points (`shift_of_sampling_points`) | Present (`.callout-note`) | `673–688` | None |
| **Ch 20 §20.4C** | BSGS Block Polynomial Doubling ($N! \bmod P$ & P-Recursive Matrices) | **MISSING** | After `740` | **Add Contract 1E below** |
| **Ch 21 §21.1** | Kinoshita–Li Bivariate Power Projection (`power_projection`) | Present (`.callout-important`) | `121–129` | None |
| **Ch 21 §21.2** | Kinoshita–Li Transposed FPS Composition (`fps_compose`) | Present (`.callout-important`) | `242–250` | None |
| **Ch 21 §21.3** | Elegia's All-$n$ Coupled Binomial Sum Linearization | **MISSING** | After `335` | **Add Contract 1F below** |
| **Ch 21 §21.4** | Compositional Inverse (`fps_revert`, Routes A & B) | Present (`.callout-important`) | `398–408` | None |

---

### 1.2 Drop-In Replacements for Missing Main-Text Algorithm Contracts

#### Issue 1A: Add Main-Text Algorithm Contract in `Ch 18` §18.2 (Line `278`)
- **File**: [`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L276-L280)
- **Target Lines**: `276–280`
- **Drop-In Replacement**:
```markdown
Both sides are explicit polynomials of degree $\le \max(2d-1, d + \deg A, d-1 + \deg B)$! Extracting $[x^n]$ compiles $F(x)$ directly into a bounded-order P-recursive recurrence without ever calling a square-root or division routine on power series.

::: {.callout-note}
## Algorithm Contract: Abel–Cockle–Harley–Comtet Radical-to-ODE Compiler (Recipes A & B)
- **Input & Exact Index Boundaries**: Polynomials $P(x)$ of degree $d \ge 1$ with $P(0) \neq 0$, exponent $\alpha = r/s \in \mathbb{Q}$ (Recipe A) or polynomial numerator/radical pair $(A(x), B(x))$ of degrees $d_A, d_B$ (Recipe B), target length $N \ge 0$, and prime modulus $p$.
- **Preconditions**: $P(0)$ is a unit in $\mathbb{F}_p$, $s \not\equiv 0 \pmod p$, and the indicial polynomial $I(m) = s P_0 m$ is non-zero modulo $p$ for $1 \le m \le N$ (otherwise dispatch to §18.4 $p$-adic valuation lifting).
- **Postconditions (Output)**: Exact coefficient array $f[0 \dots N]$ of $F(x) = P(x)^{r/s} \bmod x^{N+1}$ (Recipe A) or $F(x) = A(x) + B(x)\sqrt{P(x)} \bmod x^{N+1}$ (Recipe B).
- **Time & Space Complexity**: $\mathcal{O}(dN)$ time and $\mathcal{O}(N)$ space for Recipe A; $\mathcal{O}((d + d_A + d_B)N)$ time and $\mathcal{O}(N)$ space for Recipe B.
- **Loop / Algebraic Invariant**: At step $m \in [1, N]$, the cleared polynomial ODE identity holds identically at coefficient $[x^{m-1}]$, determining $f_m$ uniquely from $\{f_{m-j}\}_{j=1}^{K}$ using only ring multiplications and a single scalar inversion $(s P_0 m)^{-1} \bmod p$.
:::

---
```

#### Issue 1B: Add Main-Text Algorithm Contract in `Ch 18` §18.3 (Line `403`)
- **File**: [`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L401-L405)
- **Target Lines**: `401–405`
- **Drop-In Replacement**:
```markdown
Notice how every non-linear convolution $y(x)^2$ has vanished! We have traded a quadratic $O(N \log N)$ Newton-iteration problem for a linear second-order ODE whose coefficients are small polynomials, which unrolls in $O(N)$ time via §18.1.

::: {.callout-note}
## Algorithm Contract: Riccati-to-Second-Order Holonomic Linearization
- **Input & Exact Index Boundaries**: Polynomials $A(x), B(x), C(x), D(x) \in \mathbb{F}_p[x]$ of maximum degree $d$ defining the quadratic Riccati ODE $A(x) y'(x) = B(x) + C(x) y(x) + D(x) y(x)^2$, initial value $y(0) = y_0$, and target degree $N \ge 0$.
- **Preconditions**: $A(0) D(0) \not\equiv 0 \pmod p$ (or known valuation shift), and the linearized indicial polynomial for $u(x) = \exp(-\int \frac{D(x)}{A(x)} y(x)\,dx)$ has no roots in $[1, N] \bmod p$ (if $p \le N$, use $p$-adic valuation lifting on $u_n$ before recovering $y_n$).
- **Postconditions (Output)**: Auxiliary holonomic sequence $u[0 \dots N+1]$ satisfying the cleared second-order linear ODE $(A^2 D) u'' + (A(A'D - AD' - CD)) u' + (BD^2) u = 0$, and recovered Riccati sequence $y[0 \dots N]$ via $D(x) y(x) u(x) = -A(x) u'(x) \bmod x^{N+1}$.
- **Time & Space Complexity**: $\mathcal{O}(d^2 + dN)$ time and $\mathcal{O}(N)$ auxiliary space.
- **Loop / Algebraic Invariant**: After step $m$, $u[0 \dots m+1]$ satisfies $[x^{m-1}]$ of the cleared second-order linear ODE and $y[0 \dots m]$ satisfies $\sum_{j=0}^m (D \ast y)_j u_{m-j} = -(m+1) A_0 u_{m+1} - \sum_{k \ge 1} (m+1-k) A_k u_{m+1-k}$.
:::

---
```

#### Issue 1C: Add Main-Text Algorithm Contract in `Ch 19` §19.1 (Line `113`)
- **File**: [`chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd#L110-L115)
- **Target Lines**: `110–115`
- **Drop-In Replacement**:
```markdown
- $n = 2$: $3 f_3 = 9 f_2 - 7 f_1 + f_0 = 9(2) - 7(1) + 1 = 12 \implies f_3 = 4$.
- $n = 3$: $4 f_4 = 12 f_3 - 10 f_2 + 2 f_1 = 12(4) - 10(2) + 2(1) = 30 \implies f_4 \text{ wait—why is } 4 f_4 = 30$? Because in Step 1, $(1 - x) F(x)$ differentiated is $-F(x) + (1 - x) F'(x)$, and we substituted $(1 - x) G(x) = x F(x) \implies -x(1 - x) G'(x) = -x^2 F'(x) - \dots$ Always verify whether you cleared denominators before differentiating! In fact, unrolling the **coupled pair** $(f_n, g_n)$ directly from $(1 - x) F' = F + G$ and $(1 - x) G' = x F + x F'$ gives $n f_n - (n - 1) f_{n-1} = f_{n-1} + g_{n-1} \implies n f_n = n f_{n-1} + g_{n-1}$ and $n g_n = (n - 1) g_{n-1} + n f_{n-1}$, which requires **zero divisions** ($f_n = f_{n-1} + \frac{1}{n} g_{n-1}$—or notice $g_{n-1}$ is always divisible by $n$!).

::: {.callout-note}
## Algorithm Contract: Coupled ODE-to-P-Recursive Unrolling
- **Input & Exact Index Boundaries**: A $k \times k$ polynomial matrix $M(x) \in \mathbb{F}_p[x]^{k \times k}$ of maximum entry degree $d$, scalar denominator polynomial $Q(x) = \sum_{j=0}^d q_j x^j$ with $q_0 \neq 0$, initial vector $\mathbf{F}_0 = [x^0]\mathbf{F}(x) \in \mathbb{F}_p^k$, and target degree $N \ge 0$.
- **Preconditions**: $q_0 \not\equiv 0 \pmod p$ and $N < p$ (so $q_0^{-1}$ and $(n+1)^{-1} \bmod p$ exist for all $0 \le n < N$).
- **Postconditions (Output)**: Vector sequence $\mathbf{F}_0, \mathbf{F}_1, \dots, \mathbf{F}_N \in \mathbb{F}_p^k$ satisfying $Q(x)\mathbf{F}'(x) = M(x)\mathbf{F}(x) \bmod x^N$.
- **Time & Space Complexity**: $\mathcal{O}(k^2 d N)$ time and $\mathcal{O}(kN)$ space (or $\mathcal{O}(k^2 d)$ rolling space).
- **Loop / Algebraic Invariant**: At the end of iteration $n \in [0, N-1]$, the vectors $\mathbf{F}_0, \dots, \mathbf{F}_{n+1}$ satisfy $q_0(m+1)\mathbf{F}_{m+1} = \sum_{j=0}^{\min(d,m)} M_j \mathbf{F}_{m-j} - \sum_{j=1}^{\min(d,m)} q_j (m+1-j)\mathbf{F}_{m+1-j} \pmod p$ for all $0 \le m \le n$.
:::

---
```

#### Issue 1D: Add Main-Text Algorithm Contract in `Ch 20` §20.4 Part A (Line `556`)
- **File**: [`chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd#L552-L558)
- **Target Lines**: `552–558`
- **Drop-In Replacement**:
```markdown
Since $b_j = [x^j] F(x)$ is extracted from a shifted middle window of $A(x)$ against the reversed sequence $w_{\binom{k}{2}}$, **$\operatorname{czt}^\top$ has the exact same complexity and algebraic structure as forward $\operatorname{czt}$**: one diagonal scaling by $w^{-\binom{j}{2}}$, one `mulT` against $G(x) = \sum_{k=0}^{n+m-2} w^{\binom{k}{2}} x^k$, and one final diagonal scaling by $w^{-\binom{i}{2}}$.

::: {.callout-note}
## Algorithm Contract: Transposed Chirp Z-Transform ($\operatorname{czt}^\top$)
- **Input & Exact Index Boundaries**: Weight vector $y[0 \dots m-1] \in \mathbb{F}_p^m$, geometric base $w \in \mathbb{F}_p^\times$, and target output length $n \ge 1$.
- **Preconditions**: $w \not\equiv 0 \pmod p$ (so $w^{-1} \bmod p$ exists).
- **Postconditions (Output)**: Vector $b[0 \dots n-1] \in \mathbb{F}_p^n$ where $b_i = \sum_{j=0}^{m-1} y_j w^{ij} \bmod p$ for $0 \le i < n$.
- **Time & Space Complexity**: $\mathcal{O}((n + m) \log(n + m))$ time (1 NTT call via `mulT` of length $2^{\lceil \log_2(n+m-1) \rceil}$) and $\mathcal{O}(n + m)$ space.
- **Loop / Algebraic Invariant**: After diagonal scaling $\tilde{y}_j = y_j w^{-\binom{j}{2}}$ and transposed convolution $c = \operatorname{mulT}(G, \tilde{y}, n)$ against $G(x) = \sum_{k=0}^{n+m-2} w^{\binom{k}{2}} x^k$, each entry satisfies $c_i = w^{\binom{i}{2}} \sum_{j=0}^{m-1} y_j w^{ij} \pmod p$.
:::

### Part B: Shift of Sampling Points (`shift_of_sampling_points`)
```

#### Issue 1E: Add Main-Text Algorithm Contract in `Ch 20` §20.4 Part C (Line `740`)
- **File**: [`chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd#L738-L743)
- **Target Lines**: `738–743`
- **Drop-In Replacement**:
```markdown
Since we perform $\log_2 B$ doubling steps on degree-$B$ polynomials (or $k \times k$ matrices of degree-$B$ polynomials), the total runtime is $\mathcal{O}(\sqrt{N} \log N)$ (or $\mathcal{O}(k^2 \sqrt{N} \log N + k^3 \sqrt{N})$ for order-$k$ P-recursive recurrences), unlocking $N \le 10^9$ in under a second!

::: {.callout-note}
## Algorithm Contract: BSGS Block Polynomial Doubling ($N! \bmod P$ & P-Recursive Matrices)
- **Input & Exact Index Boundaries**: Target index $N \ge 0$, prime modulus $P > B = \lfloor \sqrt{N} \rfloor$, and $k \times k$ degree-$r$ polynomial transition matrix $M(x) \in \mathbb{F}_P[x]^{k \times k}$ (with $k=1, r=1, M(x) = [x+1]$ for $N! \bmod P$).
- **Preconditions**: $B+1$ consecutive grid points are invertible modulo $P$ so `shift_of_sampling_points` can evaluate shifted block products without overlap singularities.
- **Postconditions (Output)**: Exact matrix product $\mathcal{M}_N = M(N-1) M(N-2) \cdots M(0) \bmod P$ (or scalar $N! \bmod P$).
- **Time & Space Complexity**: $\mathcal{O}(k^2 r \sqrt{N} \log N + k^3 r \sqrt{N})$ time and $\mathcal{O}(k^2 r \sqrt{N})$ space.
- **Loop / Algebraic Invariant**: After doubling phase $t$ with block size $d = 2^t$, the array stores the point values of $\mathcal{M}_d(x) = \prod_{j=0}^{d-1} M(x+j)$ at the $r d + 1$ sample points $x \in \{0, d, 2d, \dots, r d^2\}$.
:::

---
```

#### Issue 1F: Add Main-Text Algorithm Contract in `Ch 21` §21.3 (Line `335`)
- **File**: [`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd#L332-L337)
- **Target Lines**: `332–337`
- **Drop-In Replacement**:
```markdown
By setting $H(y) = F(y) \cdot G(y)^{-n_0}$ (or in coupled dynamic programming where $m$ varies with $n$, separating the $n$-dependence via compositional inverse $W(x)$ of $x / G(x)^\alpha$), Theorem 21.1 reduces an entire table of $N$ distinct Lagrange inversions to a single FPS composition or compositional inverse!

::: {.callout-important}
## Algorithm Contract: Elegia's All-$n$ Coupled Binomial Sum Linearization
- **Input & Exact Index Boundaries**: Formal power series $F(y), G(y) \in \mathbb{F}_p[[y]] \bmod y^{N+1}$ with $[y^0]G(y) = 1$, linear exponent slope $\alpha \in \mathbb{F}_p$, and target range $0 \le k \le N$.
- **Preconditions**: $N < p$ and $[y^0]G(y) = 1 \not\equiv 0 \pmod p$ (so $W(x) = (x / G(x)^\alpha)^{\langle -1 \rangle}$ is well-defined up to $x^{N+1}$).
- **Postconditions (Output)**: Exact sequence $S_k = [y^k] F(y) G(y)^{\alpha k}$ for all $0 \le k \le N$ simultaneously, computed as $[x^k]\left(\frac{F(W(x))}{1 - \alpha x G'(W(x)) / G(W(x))}\right)$.
- **Time & Space Complexity**: $\mathcal{O}(N \log^2 N)$ time and $\mathcal{O}(N \log N)$ space via one call to `fps_revert` and two calls to `fps_compose`.
- **Loop / Algebraic Invariant**: Under the formal change of variables $x = y G(y)^{-\alpha} \iff y = W(x)$, the logarithmic derivative $\frac{x W'(x)}{W(x)} = \frac{1}{1 - \alpha y G'(y)/G(y)}$ preserves residues across all degrees $0 \le k \le N$ simultaneously.
:::

---
```

---

### 1.3 Mandatory `.callout-warning` Failure-Mode Upgrades (`Ch 18` & `Ch 21`)

#### Issue 1G: Upgrade `Ch 18` §18.3 Archetype 1 Integrating-Factor Trap (`p <= N`) to `.callout-warning`
- **File**: [`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L343-L351)
- **Target Lines**: `343–351`
- **Drop-In Replacement**:
```markdown
::: {.callout-warning}
## Failure Mode: Archetype 1 — First-Order Linear ODEs ($a(x) F'(x) + b(x) F(x) = c(x)$) When $p \le N$
In calculus over $\mathbb{R}$, one solves $a(x) F'(x) + b(x) F(x) = c(x)$ using an integrating factor $\mu(x) = \exp\!\left(\int \frac{b(x)}{a(x)}\,dx\right)$. In competitive programming over $\mathbb{F}_p[[x]]$:

1. Computing $\int (b/a)\,dx$ and $\exp(\cdot)$ requires $O(N \log N)$ polynomial operations and **fails completely** if $p \le N$ (because $\int x^{p-1}\,dx = x^p / p$ divides by zero!).
2. Even worse, if $a(0) = 0$ (a regular singular point), $b(x)/a(x)$ has a pole at $x = 0$, so its formal integral does not even exist in $\mathbb{F}_p[[x]]$.

**The Holonomic Cure**: Never compute the integrating factor! Read off $[x^n]$ directly from $a(x) F'(x) + b(x) F(x) = c(x)$ in $O(d N)$ time.
:::
```

#### Issue 1H: Upgrade `Ch 21` §21.4 Degree $p+2$ Artin–Schreier Obstruction to `.callout-warning`
- **File**: [`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd#L477-L487)
- **Target Lines**: `477–487`
- **Drop-In Replacement**:
```markdown
::: {.callout-warning}
## Failure Mode: The Degree $p + 2$ Artin–Schreier Obstruction for Functional Square Roots ($G(G(x)) = F(x)$)
Suppose we want to solve $G(G(x)) = F(x) \bmod x^{N+1}$ when $F(x) = x + f_2 x^2 + \cdots$ with $f_2 \neq 0 \pmod p$ (a parabolic tangent series). Over $\mathbb{Q}$, a unique formal solution $G(x) = x + \frac{f_2}{2} x^2 + \cdots$ always exists because at each degree $k \ge 2$, the linear equation for $g_k = [x^k]G(x)$ has leading coefficient $2 g_1^k + \cdots = 2$.
In characteristic $p > 2$, something shocking happens at degree $k = p + 1$: because $G(x)$ is tangent to the time-$1/2$ flow of a formal vector field, the $p$-th iterate $F^{\circ p}(x) = G^{\circ 2p}(x)$ must satisfy $F^{\circ p}(x) \equiv x \pmod{x^{p+1}}$, and its $[x^{p+2}]$ coefficient is an invariant! Specifically, when $G(x) = x + g_2 x^2 + \cdots$ is iterated twice, the unknown coefficient $g_{p+1}$ enters $[x^{p+1}] G(G(x))$ with coefficient $2$, which determines $g_{p+1}$, **but at degree $k = p + 2$, the coefficient of $g_{p+1}$ in $[x^{p+2}]G(G(x))$ receives a contribution $(p+1) g_2 g_{p+1} + g_2 g_{p+1} = (p+2) g_2 g_{p+1}$ while the Artin–Schreier derivation annihilates the $p$-th power term**, creating a rigid polynomial compatibility condition on $(f_2, \dots, f_{p+2})$ modulo $p$ when reducing via Abelian / Écalle–Voronin conjugacy! (We will derive and solve this exact characteristic-$p$ obstruction in **Mas-2, #326 QOJ 5094**.)
:::
```

---

## Area 2: Code Block Policy & Length Audit ($\le 15$ Lines, Zero Boilerplate, Explicit Language Tags)

### 2.1 Complete Code Block Inventory Across Part V

| File | Lines (Inclusive of Fences) | Language Tag | Inner Lines | Boilerplate Check | Length Status ($\le 15$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ch18` | `51–56` | `{mermaid}` | `4` | Clean | PASS |
| `ch18` | `158–169` | `cpp` | `10` | Clean | PASS |
| `ch18` | `478–496` | `cpp` | **`17`** | Clean | **FAIL ($17 > 15$)** |
| `ch19` | `30–40` | `{mermaid}` | `9` | Clean | PASS |
| `ch19` | `181–192` | `cpp` | `10` | Clean | PASS |
| `ch19` | `252–266` | `cpp` | `13` | Clean | PASS |
| `ch19` | `313–327` | `cpp` | `13` | Clean | PASS |
| `ch20` | `78–92` | `{mermaid}` | `13` | Clean | PASS |
| `ch20` | `288–301` | `cpp` | `12` | Clean | PASS |
| `ch20` | `450–458` | `cpp` | `7` | Clean | PASS |
| `ch20` | `656–671` | `cpp` | `14` | Clean | PASS |
| `ch21` | `73–86` | `{mermaid}` | `12` | Clean | PASS |
| `ch21` | `131–145` | `cpp` | `13` | Clean | PASS |
| `ch21` | `252–269` | `cpp` | **`16`** | Clean | **FAIL ($16 > 15$)** |
| `ch21` | `410–429` | `cpp` | **`18`** | Clean | **FAIL ($18 > 15$)** |

---

### 2.2 Drop-In Replacements for the 3 Code Blocks Exceeding 15 Lines

#### Issue 2A: Compress `ch18` `struct PAdicVal` (`17` lines $\to$ `13` lines)
- **File**: [`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L478-L496)
- **Target Lines**: `478–496`
- **Drop-In Replacement** (`13` inner lines):
````markdown
```cpp
struct PAdicVal {
    long long v = 0; mint u = 0; // Represents u * p^v (0 is v = INF, u = 0)
    static PAdicVal from_int(long long x, long long p) {
        if (x == 0) return {1LL << 60, 0};
        long long v = 0; while (x % p == 0) { x /= p; ++v; }
        return {v, mint(x)};
    }
    friend PAdicVal operator+(const PAdicVal& a, const PAdicVal& b) {
        if (a.v < b.v) return a;
        if (b.v < a.v) return b;
        return {a.v, a.u + b.u}; // Safe when min_v >= 0 and u != -b.u mod p
    }
};
```
````

#### Issue 2B: Compress `ch21` `fps_compose` (`16` lines $\to$ `14` lines)
- **File**: [`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd#L252-L269)
- **Target Lines**: `252–269`
- **Drop-In Replacement** (`14` inner lines):
````markdown
```cpp
Poly fps_compose(Poly g, Poly f, int n, int k = 1) { // returns G(F(x)) mod x^{n+1}
    if (n == 0) return g;
    Poly q(2 * (n + 1) * k, 0);
    for (int i = 0; i <= n; ++i) for (int j = 0; j < k; ++j)
        q[(i << 1 | 1) * k + j] = -f[i * k + j]; // Q(x,y) = 1 - y F(x)
    auto Q_prod = bivar_conv_neg(q, n, k);        // Q(x,y) * Q(-x,y)
    Poly q_next((n / 2 + 1) * 2 * k, 0);
    for (int i = 0; i <= n / 2; ++i) for (int j = 0; j < 2 * k; ++j)
        q_next[i * 2 * k + j] = Q_prod[2 * i * 2 * k + j];
    Poly u = fps_compose(g, q_next, n / 2, 2 * k); // Recurse on (n/2, 2k)
    Poly u_up((n + 1) * 2 * k, 0);
    for (int i = 0; i <= n / 2; ++i) for (int j = 0; j < 2 * k; ++j)
        u_up[2 * i * 2 * k + j] = u[i * 2 * k + j];
    return bivar_mulT_x(u_up, q_minus_x(q), n, k); // P(x,y) = mulT(U(x^2,y), Q(-x,y))
}
```
````

#### Issue 2C: Compress `ch21` `fps_revert_routeA` & `fps_revert_routeB` (`18` lines $\to$ `14` lines)
- **File**: [`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd#L410-L429)
- **Target Lines**: `410–429`
- **Drop-In Replacement** (`14` inner lines):
````markdown
```cpp
Poly fps_revert_routeA(Poly f, int n) { // Requires p > n, f[0]=0, f[1]!=0
    Poly w(n + 1, 0); w[n] = 1;         // Linear form w_k = [k == n]
    Poly p = power_projection(w, f, n); // p_k = [x^n] F(x)^k
    for (int k = 1; k <= n; ++k) p[k] = p[k] * n * inv_int(k) % MOD;
    return shift_and_pow_neg_inv(p, n); // G(x) = x * (p_n(x)/x)^{-1/n}
}
Poly fps_revert_routeB(Poly f, int n) { // Characteristic-free (requires only f[1] != 0)
    Poly g = {0, inv_mod(f[1])};
    for (int m = 2; m <= n; m <<= 1) {
        Poly fg = fps_compose(f, g, m); fg[1] = (fg[1] + MOD - 1) % MOD;
        Poly dfg = fps_compose(deriv(f), g, m - 1);
        g = g - trunc(fg * inv_series(dfg, m), m + 1);
    }
    return trunc(g, n + 1);
}
```
````

---

## Area 3: Strict Quarto Syntax & Hygiene Audit

### 3.1 Summary of Automated Quarto Hygiene Checks

1. **`!$$` Factorial-Math Collisions**: **0 instances** across all 5 files (`PASS`).
2. **Forbidden `\(` or `\[` Math Delimiters**: **0 instances** across all 5 files (`PASS`).
3. **Unescaped `|` Inside `$...$` in Markdown Tables**: **0 instances** across all 5 files (`PASS` — `cp05` properly uses `\lvert s \rvert` and `\lvert S \rvert`).
4. **`<details>` / `<summary>` / `</details>` Balance & Blank Lines**: **100% balanced** across all 5 files (`ch18`: `32`, `ch19`: `32`, `ch20`: `32`, `ch21`: `32`, `cp05`: `32`), with a blank line after every `</summary>` and before every `</details>` (`PASS`).
5. **`:::` Callout Balance & Surrounding Blank Lines**: **100% balanced** across all 5 files, with blank lines before every opening `::: {.callout-...}` and after every closing `:::` (`PASS`).
6. **`CP-V` Stage 1 Spoiler-Free Audit (`lines 27–489`)**: The overview table (`lines 27–36`), all 8 problem statements, and all 8 `Hint 1 (Diagnostic Signal)` blocks in `cp05-part5-dfinite-transposition-composition.qmd` contain **zero chapter references or technique spoilers** (`PASS`).

---

### 3.2 Targeted Link, Prose & Typography Fixes (With Exact Drop-In Replacements)

#### Issue 3A (CRITICAL): Broken Internal `.qmd` Link in `ch21` Line `444`
- **File**: [`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd#L442-L446)
- **Target Line**: `444`
- **Bug**: Links to `ch12-prufer-cayley-block-cut-cactus-graphs.qmd`, which does not exist in `chapters/`. The actual file in `chapters/` is `ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`.
- **Drop-In Replacement for Line `444`**:
```markdown
1. **Block-Cut Tree Biconnected Graph Dissymmetry ([Chapter 12 (Mas-2, #183 Luogu P5827)](ch12-cacti-deserts-block-cut-biconnected-graphs.qmd))**:
```

#### Issue 3B: Forbidden `"Let's check"` Conversational Phrasing in `cp05` Line `739`
- **File**: [`checkpoints/cp05-part5-dfinite-transposition-composition.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp05-part5-dfinite-transposition-composition.qmd#L738-L742)
- **Target Line**: `739`
- **Bug**: Contains raw conversational phrasing `Let's check the Sample Trace ($n = 4$):`.
- **Drop-In Replacement for Line `739`**:
```markdown
**Verification on the Sample Trace ($n = 4$)**:
```

#### Issue 3C: Missing Space After `!` in `ch20` Line `167`
- **File**: [`chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd#L166-L169)
- **Target Line**: `167`
- **Bug**: Missing space after exclamation mark (`without a single polynomial division!Notice what happened`).
- **Drop-In Replacement for Line `167`**:
```markdown
  3. At the leaves $u_i$, read off the length-$1$ remainder $r_i = P(x_i)$ directly—**without a single polynomial division!** Notice what happened: in forward interpolation, we build $\prod (x - x_j)$ bottom-up and then evaluate $M'(x_i)$ top-down using polynomial modulo. In transposed multipoint evaluation, the bottom-up phase builds the *exact same subproduct tree* $M_u(x)$, and the top-down phase replaces every polynomial division with a transposed convolution `mulT`!
```

---

### 3.3 Single-Line `$$...$$` Display-Math Surrounding Blank-Line Hygiene

- **Observation**: In `ch20`, display-math blocks are written as multi-line `$$\n...\n$$` blocks with blank lines before and after (only 2 minor adjacencies at lines `948` and `1124`). In `ch18` (`203` single-line `$$...$$` blocks), `ch19` (`128` blocks), `ch21` (`159` blocks), and `cp05` (`113` blocks), single-line `$$...$$` display math equations are placed directly on lines immediately following or preceding prose/list items without a blank line separating them.
- **Why It Matters**: In Pandoc/Quarto Markdown, a `$$...$$` line that immediately follows a non-blank text line (without an intervening blank line) is parsed as inline display math attached to the preceding paragraph rather than a standalone display block, which can cause cramped vertical spacing or inconsistent HTML/PDF block rendering.
- **One-Command Automated Fix**: Run the following idempotent Python script from `/home/maomao90/Documents/IO/ICPC-math-notes` to ensure every standalone `$$...$$` display-math line in `ch18`–`ch21` and `cp05` is preceded and followed by a blank line:

```python
import pathlib, re

files = [
    "chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd",
    "chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd",
    "chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd",
    "chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd",
    "checkpoints/cp05-part5-dfinite-transposition-composition.qmd",
]
for fp in files:
    lines = pathlib.Path(fp).read_text().splitlines()
    out, in_math = [], False
    for line in lines:
        s = line.strip()
        is_single = s.startswith("$$") and s.endswith("$$") and len(s) > 4
        if is_single or (s == "$$" and not in_math):
            if out and out[-1].strip() != "":
                out.append("")
        out.append(line)
        if is_single or (s == "$$" and in_math):
            out.append("")
        if s == "$$":
            in_math = not in_math
    cleaned = re.sub(r"\n{3,}", "\n\n", "\n".join(out)) + "\n"
    pathlib.Path(fp).write_text(cleaned)
```
