# Cohort 3 Master Synthesis & Cross-Cohort Reconciliation: Differential Equations (ODEs), D-Finite / P-Recursive Series, Sparse FPS Engines, Euler's PDE & Creative Telescoping, and CDQ / Relaxed Convolution (Wave 5A: Iterations 41–45 / 93–97)

> **Document Role**: Phase 1 Cohort 3 Master Synthesis & Blind-Spot Reconciliation Architect Report  
> **Wave Scope**: Wave 5A — Iterations 41–45 (Cohort 1 & Pre-existing) / Iterations 93–97 (Cohort 2)  
> **Source Files Reconciled**:
> 1. `fps_research/iter_41_to_45_ode_sparse_cdq_relaxed.md` (Pre-existing Baseline, 313 lines, 37 KB)
> 2. `fps_research/cohort1_iter_41_to_45_ode_sparse_cdq_relaxed.md` (Cohort 1 Independent Research, 1,709 lines, 163 KB)
> 3. `fps_research/cohort2_iter_93_to_97_ode_sparse_cdq_relaxed.md` (Cohort 2 Independent Research, 1,896 lines, 177 KB)  
> **Pedagogical Contract**: Zero Magic Steps (Diagnostic Signal + Reverse-Engineering Scratchpad before every non-trivial transformation), strict `$...$` / `$$...$$` math delimiters, full self-contained problem statements, 3-tier progressive hints, and complete algebraic derivations.

---

## 1. Three-Way Cross-Cohort Blind-Spot & Coverage Reconciliation Matrix

Comparing all three independent research tracks reveals substantial complementary discoveries ("blind spots caught by redundancy"). No single track captured every algebraic edge case, valuation singularity, or algorithmic optimization:

| Subtopic / Iteration | Pre-Existing (`iter_41_to_45`) Unique Contributions | Cohort 1 (`cohort1_iter_41_to_45`) Unique Contributions | Cohort 2 (`cohort2_iter_93_to_97`) Unique Contributions | Master Synthesis Resolution |
| :--- | :--- | :--- | :--- | :--- |
| **Iter 41 / 93: D-Finite / Holonomic Series & P-Recursive Sequences** | • **$p$-Adic Lifting Contract ($\mathbb{Z}/p^{V+1}\mathbb{Z}$)** when indicial polynomial $I(n) \equiv 0 \pmod p$ for some $n^* \le N < p$ even though $I(n^*) \neq 0$ in $\mathbb{Q}$.<br>• Explicit bidirectional Stirling-number operator conversion $\vartheta^m \leftrightarrow x^j D^j$.<br>• Central Trinomial $T_n = [x^n](1+x+x^2)^n$ hand trace. | • **Extended Euclidean Algorithm proof in $K(x)[y]$** of the Abel–Cockle–Harley–Comtet theorem ($\Phi(x, F) = 0 \implies F' = -\Phi_x V(x,F) \bmod \Phi$).<br>• **General quadratic algebraic-to-1st-order inhomogeneous ODE** $4A\Delta F' + 2(2A'\Delta - A\Delta')F = B\Delta' - 2B'\Delta$.<br>• Involution $I_n$ and Large Schröder $S_n$ traces.<br>• Differential operator $\mathcal{D}_A = \frac{1}{A'(x)}\frac{d}{dx}$ for $G(A(x))$. | • **Rational Power Quotient Recipe**: $H = P^\alpha / Q^\beta \implies U H' = V H$ with $U = PQ$ and $V = \alpha P'Q - \beta PQ'$.<br>• Explicit 2nd-order chain-rule ODE $c_2(A)(A'H'' - A''H') + c_1(A)(A')^2 H' + c_0(A)(A')^3 H = 0$.<br>• Apparent singularity analysis when $\operatorname{val}(A') \ge 1$.<br>• Central Delannoy $D_n$ hand trace. | Unifies all 3 proofs, all 4 hand traces ($I_n, T_n, D_n, S_n$), the explicit 2nd-order composition law, and the 3-tier singularity + $p$-adic lifting protocol. |
| **Iter 42 / 94: Differential Equation Substitutions & Linearization** | • **5-Archetype Substitution Table**.<br>• **Worked Demo 1**: Integrating Factor + Catalan Rationalizing Substitution $x = u(1-u)$ on $(1-4x)F' - 2F = \frac{1}{1-3x}$.<br>• **Worked Demo 3**: Two-step Chain-Rule + Gauge Reduction $D_d(z) = h(z) B_d(t(z))$ for QOJ #60 Chinese Elephant Chess Bessel ODE. | • **Multiplicative inverse shortcut**: $\mu(x)^{-1} = \exp(-\int_0^x P(t)\,dt)$, eliminating polynomial `inv`.<br>• Regular singular point analysis when $C(0) = 0$ ($\operatorname{val}(C) = v \ge 1$) in Riccati equations.<br>• Euler–Cauchy operator normalization $(1+x)\frac{d}{dx} = \frac{d}{du}$ via $u = \ln(1+x)$. | • Complete C++ engine `solve_nonlinear_first_order_ode` for Newton + Integrating Factor on $F' = G(x, F)$.<br>• **Energy Integral Trick** $2F'F'' = 2\Psi(F)F'$ reducing 2nd-order conservative ODEs $F'' = \Psi(F)$ to 1st-order.<br>• **Liouville Transformation** $\phi'(x) = 1/\sqrt{q_2(x)}$. | Synthesizes all 7 substitution archetypes, all 3 worked demonstrations, the energy-integral & Liouville reductions, and the full C++ Newton-ODE solver. |
| **Iter 43 / 95: Sparse FPS Engine in $O(N \cdot K)$ Time** | • Hand-checkable trace of **Sparse Square Root** $F(x) = (1 + 2x + x^3)^{1/2} \bmod x^5$.<br>• Chaining rules for $P(x)^\alpha / Q(x)^\beta$ via intermediate series. | • **Rational exponent $\alpha = a/b$ valuation criterion**: $b \mid v \cdot a$ and $c_1$ must be a $b$-th residue when $\operatorname{val}(P) = v > 0$.<br>• `__int128_t` overflow guard on $v \cdot k$.<br>• Proof of why $P^\alpha = \exp(\alpha \ln P)$ fails in $O(N^2)$ (since $\ln P$ is dense). | • **3-Way Modular Reduction Trap for $\alpha \ge p$**: $\alpha \in \mathbb{Z}$ in shift $v\alpha$, $\alpha \bmod (p-1)$ in $p_0^\alpha$, and $\alpha \bmod p$ in ODE multiplier $((\alpha+1)d_j - n)$.<br>• **Coupled $r$-state 1st-order sparse ODE system** $(H_0, \dots, H_{r-1}) = (F(P), \dots, F^{(r-1)}(P))$ in $O(rNK)$ without dividing by $P'(x)$. | Combines the unified `SparseFPS` C++ namespace with rational/huge-exponent valuation guards, coupled $r$-order composition, and sparse sqrt trace. |
| **Iter 44 / 96: Euler's Homogeneous PDE, Diagonals & Binomial Sums** | • **Cross-Partial Elimination** $\frac{\partial A}{\partial y}\frac{\partial F}{\partial x} - \frac{\partial A}{\partial x}\frac{\partial F}{\partial y} = 0$ for $F = A^\alpha$.<br>• **Hypergeometric Operator Equation** $(Q(\vartheta) - xP(\vartheta))F(x) = 0$.<br>• Pascal boundary-term failure counterexample $\sum_{k=0}^m \binom{n}{k}$. | • **Zeilberger's Creative Telescoping by Hand** on $T(n,k) = \binom{n}{k}\binom{n+k}{k}c^k$ using certificate $R(n,k) = \frac{4k^2}{(n+1-k)(n+k)}$.<br>• Lagrange diagonal formula for $[x^n](1+ax)^n(1+bx)^n$. | • **EI's Direct Differential-Residue Method (`载谭 Binomial Sums`)** via $[x^{-1}]\frac{d}{dx}(x^{-n}A(x)) = 0$.<br>• **General Quadratic Power Diagonal Formula** $\sum_{n\ge 0}([x^n](p_0+p_1x+p_2x^2)^n)z^n = (1-2p_1z+(p_1^2-4p_0p_2)z^2)^{-1/2}$.<br>• 4-Row Master Binomial Sum Table. | Integrates all 4 diagonal/telescoping engines: Residue Contour, Zeilberger Certificate, EI Differential-Residue, and Hypergeometric $\vartheta$-Operator. |
| **Iter 45 / 97: Offline CDQ NTT vs. Relaxed / Online Convolution** | • **LCA Partition Invariant Theorem** proving every pair $0 \le i < n \le N$ has a unique LCA node $[l, r]$ in the CDQ recursion tree. | • **Full-Online Offline-CDQ Asymmetry Bug at $l > 0$**: `a[l..m]*b[0..r-l] + b[l..m]*a[0..r-l]` for $l > 0$ vs `a[0..m]*b[0..m]` for $l = 0$.<br>• **L-Shaped Strip Partition Theorem** & full $q = 0 \dots 7$ trace table. | • **Binary Prefix Theorem** for Nyaan's 0-indexed `lowbit(q)` schedule.<br>• **Self-Referential Online Inv / Exp Protocol**: reading interior sum `rc.C[q]` *before* calling `rc.next(a_q, b_q)`.<br>• Small-block $d \le 16$ $O(d^2)$ fallback optimization. | Presents both proofs (L-Shaped Strip + Binary Prefix), the $l>0$ full-online CDQ fix, and production C++ templates for both engines. |

---

## 2. Iteration 41 / 93: D-Finite / Holonomic Series, P-Recursive Sequences & Linear ODEs

### 2.1 Core Definitions, Operator Algebra & Equivalence Theorem

- **Definition (P-Recursive Sequence)**: A sequence $(a_n)_{n \ge 0}$ over a field $\mathbb{K}$ of characteristic $0$ is **polynomially recursive (P-recursive)** (or **holonomic**) if there exist polynomials $P_0(n), P_1(n), \dots, P_r(n) \in \mathbb{K}[n]$, with $P_r(n)$ not identically zero, such that for all sufficiently large $n \ge 0$:
  $$P_r(n) a_{n+r} + P_{r-1}(n) a_{n+r-1} + \dots + P_0(n) a_n = 0$$
  Here $r$ is the **order** and $d = \max_k \deg P_k(n)$ is the **polynomial degree** of the recurrence.

- **Definition (D-Finite / Differentiably Finite Formal Power Series)**: A formal power series $F(x) = \sum_{n=0}^{\infty} a_n x^n \in \mathbb{K}[[x]]$ is **differentiably finite (D-finite)** if its derivatives $F(x), F'(x), F''(x), \dots$ span a finite-dimensional vector space over the rational function field $\mathbb{K}(x)$. Clearing denominators yields polynomials $q_0(x), q_1(x), \dots, q_m(x) \in \mathbb{K}[x]$ ($q_m(x) \neq 0$) such that:
  $$q_m(x) F^{(m)}(x) + q_{m-1}(x) F^{(m-1)}(x) + \dots + q_1(x) F'(x) + q_0(x) F(x) = 0$$
  (or an inhomogeneous right-hand side $R(x) \in \mathbb{K}[x]$, which converts to a homogeneous ODE by differentiating $\deg(R) + 1$ times).

#### The Euler Operator $\vartheta = x \frac{d}{dx}$ and Bidirectional Stirling Basis Conversion

> **Diagnostic Signal**: Standard differentiation $D = \frac{d}{dx}$ shifts powers via $D^j(x^n) = n^{\underline{j}} x^{n-j}$, mixing derivative order $j$ with power shifts $n-j$. Whenever we want to translate between an ODE in $x$ and a recurrence in $n$ without shifting powers first, we rewrite the ODE in terms of the **Euler (theta) operator** $\vartheta = x D$, which acts diagonally on monomials:
> $$\vartheta^m(x^n) = n^m x^n, \qquad P(\vartheta)\left(\sum_{n \ge 0} a_n x^n\right) = \sum_{n \ge 0} P(n) a_n x^n$$

> **Reverse-Engineering Scratchpad**: How do we convert back and forth between the standard differential monomials $x^j D^j$ (which satisfy $x^j D^j (x^n) = n^{\underline{j}} x^n$) and powers of the Euler operator $\vartheta^m$ (which satisfy $\vartheta^m (x^n) = n^m x^n$)? Since $\vartheta$ acts on $x^n$ as multiplication by $n$, the operator identities in the Weyl algebra $\mathbb{K}[x]\langle D \rangle$ must match the polynomial identities relating ordinary powers $n^m$ and falling factorials $n^{\underline{j}} = n(n-1)\cdots(n-j+1)$ via Stirling numbers of the second kind $\left\{ \begin{matrix} m \\ j \end{matrix} \right\}$ and signed Stirling numbers of the first kind $(-1)^{j-m}\left[ \begin{matrix} j \\ m \end{matrix} \right]$:
> $$\vartheta^m = \sum_{j=0}^{m} \left\{ \begin{matrix} m \\ j \end{matrix} \right\} x^j D^j \quad \Longleftrightarrow \quad x^j D^j = \sum_{m=0}^{j} (-1)^{j-m} \left[ \begin{matrix} j \\ m \end{matrix} \right] \vartheta^m$$

- **Fundamental Equivalence Theorem (Stanley, *Enumerative Combinatorics* Vol. 2, Theorem 6.4.3)**: *A formal power series $F(x) = \sum_{n \ge 0} a_n x^n \in \mathbb{K}[[x]]$ is D-finite if and only if its coefficient sequence $(a_n)_{n \ge 0}$ is P-recursive.*
  - **Direction 1 (D-Finite ODE $\implies$ P-Recursive Coefficient Recurrence)**: Suppose $\sum_{j=0}^{m} q_j(x) F^{(j)}(x) = 0$ with $q_j(x) = \sum_{i=0}^{d} q_{j, i} x^i$. Since $[x^n] x^i F^{(j)}(x) = [x^{n-i}] F^{(j)}(x) = (n - i + j)^{\underline{j}} a_{n - i + j}$, extracting $[x^n]$ yields:
    $$\sum_{j=0}^{m} \sum_{i=0}^{d} q_{j, i} \, (n - i + j)^{\underline{j}} \, a_{n - i + j} = 0$$
    Setting $s = j - i \in [-d, m]$ groups coefficients by the shift $a_{n+s}$:
    $$\sum_{s = -d}^{m} P_s(n) \, a_{n+s} = 0, \qquad P_s(n) = \sum_{\substack{0 \le j \le m,\, 0 \le i \le d \\ j - i = s}} q_{j, i} \, (n + s)^{\underline{j}}$$
    Each $P_s(n)$ is a polynomial in $n$ of degree at most $m$, and the recurrence has order $r \le m + d$.
  - **Direction 2 (P-Recursive Sequence $\implies$ D-Finite ODE)**: Given $\sum_{s=0}^{r} P_s(n) a_{n+s} = 0$ with $\deg P_s \le d$, multiply by $x^{n+r}$ and rewrite $P_s(n) = \widetilde{P}_s(n + s)$. Since $(n+s)^m a_{n+s} x^{n+s} = \vartheta^m(a_{n+s} x^{n+s})$, summing over $n \ge 0$ gives the operator ODE:
    $$\sum_{s=0}^{r} x^{r-s} \widetilde{P}_s(\vartheta) F(x) = R(x)$$
    where $R(x)$ is a boundary polynomial of degree $< r$. Expanding $\vartheta^m = \sum_{j=0}^{m} \left\{ \begin{matrix} m \\ j \end{matrix} \right\} x^j D^j$ yields a linear ODE of order $\le d$ and polynomial degree $\le r + d$.

---

### 2.2 Algebraic Functions are D-Finite (Abel–Cockle–Harley–Comtet Theorem)

> **Diagnostic Signal**: Whenever a generating function $F(x)$ is **algebraic**—satisfying $\Phi(x, F(x)) = 0$ for an irreducible polynomial $\Phi(x, y) \in \mathbb{K}[x, y]$ of degree $d = \deg_y \Phi$—or takes the form of a radical/rational power $F(x) = P(x)^\alpha / Q(x)^\beta$, we should **never** run $O(N \log N)$ Newton iteration, polynomial square root, or polynomial $\exp/\ln$ if we only need coefficients! Converting to a linear ODE computes all $N$ coefficients in strictly **$O(N)$** time and $O(1)$ auxiliary work per step.

> **Reverse-Engineering Scratchpad (Extended Euclidean Proof in $\mathbb{K}(x)[y]$)**: Differentiating $\Phi(x, F(x)) = 0$ with respect to $x$ by the chain rule gives:
> $$\Phi_x(x, F(x)) + \Phi_y(x, F(x)) F'(x) = 0 \implies F'(x) = -\frac{\Phi_x(x, F(x))}{\Phi_y(x, F(x))}$$
> How do we eliminate the denominator $\Phi_y(x, F(x))$? Since $\Phi(x, y)$ is irreducible of degree $d$ in $y$ over $\mathbb{K}(x)$ and $\deg_y \Phi_y = d - 1 < d$, we have $\gcd_y(\Phi(x, y), \Phi_y(x, y)) = 1$ in the polynomial ring $\mathbb{K}(x)[y]$. Running the Extended Euclidean Algorithm in $\mathbb{K}(x)[y]$ produces polynomials $U(x, y), V(x, y) \in \mathbb{K}(x)[y]$ such that:
> $$U(x, y) \Phi(x, y) + V(x, y) \Phi_y(x, y) = 1$$
> Evaluating at $y = F(x)$ (where $\Phi(x, F(x)) = 0$) gives $\Phi_y(x, F(x))^{-1} = V(x, F(x))$. Therefore:
> $$F'(x) = -\Phi_x(x, F(x)) V(x, F(x)) \bmod \Phi(x, F(x)) \in \operatorname{span}_{\mathbb{K}(x)}\{1, F(x), \dots, F(x)^{d-1}\}$$
> By induction on $k$, every higher derivative $F^{(k)}(x)$ also lies in the $d$-dimensional $\mathbb{K}(x)$-vector space spanned by $\{1, F(x), \dots, F(x)^{d-1}\}$. Thus the $d + 1$ vectors $1, F(x), F'(x), \dots, F^{(d)}(x)$ are linearly dependent over $\mathbb{K}(x)$ (yielding an inhomogeneous ODE of order $\le d-1$), and $F(x), F'(x), \dots, F^{(d)}(x)$ are linearly dependent over $\mathbb{K}(x)$ (yielding a **homogeneous linear ODE of order $\le d$**)!

#### Two Essential Closed-Form Algebraic-to-ODE Recipes

1. **Recipe A — Rational Power Quotient $H(x) = P(x)^\alpha Q(x)^{-\beta}$**:
   Taking the logarithmic derivative $\frac{H'(x)}{H(x)} = \alpha \frac{P'(x)}{P(x)} - \beta \frac{Q'(x)}{Q(x)}$ and clearing denominators gives the exact first-order linear ODE:
   $$\underbrace{P(x) Q(x)}_{U(x)} H'(x) = \underbrace{\left( \alpha P'(x) Q(x) - \beta P(x) Q'(x) \right)}_{V(x)} H(x)$$
   Precomputing $U(x)$ and $V(x)$ of degree $D \le \deg P + \deg Q$ reduces coefficient extraction to the $O(N \cdot D)$ recurrence:
   $$n u_0 h_n = \sum_{k=1}^{\min(n, D)} \left( v_{k-1} - (n - k) u_k \right) h_{n-k}$$

2. **Recipe B — General Quadratic Algebraic Function $A(x) F(x)^2 + B(x) F(x) + C(x) = 0$**:
   Writing $F(x) = \frac{-B(x) \pm \sqrt{\Delta(x)}}{2 A(x)}$ with discriminant $\Delta(x) = B(x)^2 - 4 A(x) C(x)$, observe that $W(x) = \sqrt{\Delta(x)} = 2 A(x) F(x) + B(x)$ satisfies $2 \Delta(x) W'(x) - \Delta'(x) W(x) = 0$. Substituting $W = 2 A F + B$ and $W' = 2 A' F + 2 A F' + B'$ yields the universal **first-order inhomogeneous linear ODE**:
   $$4 A(x) \Delta(x) F'(x) + 2 \left( 2 A'(x) \Delta(x) - A(x) \Delta'(x) \right) F(x) = B(x) \Delta'(x) - 2 B'(x) \Delta(x)$$

---

### 2.3 Closure Properties of D-Finite Series & Explicit Composition Laws

If $F(x)$ (order $r_1$) and $G(x)$ (order $r_2$) are D-finite over $\mathbb{K}(x)$:
1. **Linear Combination $F(x) + G(x)$**: D-finite of order $\le r_1 + r_2$.
2. **Cauchy Product $F(x) G(x)$**: D-finite of order $\le r_1 r_2$ (by the Leibniz rule $(FG)^{(k)} = \sum \binom{k}{j} F^{(j)} G^{(k-j)}$, all derivatives lie in $\operatorname{span}_{\mathbb{K}(x)}\{F^{(i)} G^{(j)} : 0 \le i < r_1, 0 \le j < r_2\}$).
3. **Hadamard Product $(F \odot G)(x) = \sum_{n \ge 0} a_n b_n x^n$**: D-finite (unlike algebraic functions, which are **not** closed under Hadamard product; e.g., $(1-4x)^{-1/2} \odot (1-4x)^{-1/2} = \sum \binom{2n}{n}^2 x^n = \frac{2}{\pi} K(16x)$ is transcendental D-finite!).
4. **Composition $H(x) = F(A(x))$ with Algebraic $A(x)$ ($A(0) = 0$)**:
   Define the modified differential operator $\mathcal{D}_A = \frac{1}{A'(x)} \frac{d}{dx}$. By induction, $\mathcal{D}_A^k H(x) = F^{(k)}(A(x))$. Substituting into $\sum_{k=0}^r c_k(y) F^{(k)}(y) = 0$ at $y = A(x)$ gives:
   $$\sum_{k=0}^{r} c_k(A(x)) \left( \frac{1}{A'(x)} \frac{d}{dx} \right)^k H(x) = 0$$
   For **second-order ODEs ($r = 2$)** with polynomial $A(x)$, multiplying through by $A'(x)^3$ clears all denominators to give the exact polynomial-coefficient ODE:
   $$c_2(A(x)) A'(x) H''(x) + \left( c_1(A(x)) A'(x)^2 - c_2(A(x)) A''(x) \right) H'(x) + c_0(A(x)) A'(x)^3 H(x) = 0$$
   - **Critical Non-Closure Warning**: The composition $F(G(x))$ of two D-finite series is **NOT** D-finite in general! For example, $e^x$ and $e^x - 1$ are D-finite of order $1$, but the Bell number EGF $B(x) = e^{e^x - 1}$ satisfies $B'(x) = e^x B(x)$ and is **not** D-finite (it has infinitely many complex poles $x_k = \ln(2\pi i k)$). Likewise, $1/F(x)$ and $\sqrt{F(x)}$ are generally not D-finite unless $F(x)$ is algebraic.

---

### 2.4 Five Canonical Worked Traces: Involutions, Central Trinomials, Central Delannoy, Large Schröder & 2-Regular Simple Graphs

#### Trace 1: Involution Numbers $I_n$ (Order-1 EGF $\to$ 2-Term Recurrence)
Counting permutations $\pi \in S_n$ with $\pi^2 = \text{id}$ decomposes into 1-cycles ($x$) and 2-cycles ($x^2/2$):
$$F(x) = \sum_{n=0}^{\infty} I_n \frac{x^n}{n!} = \exp\left( x + \frac{x^2}{2} \right) \implies F'(x) = (1 + x) F(x)$$
Extracting $[x^{n-1}/(n-1)!]$ gives $I_n = I_{n-1} + (n-1) I_{n-2}$ ($I_0 = 1, I_1 = 1, I_2 = 2, I_3 = 4, I_4 = 10, I_5 = 26$).

#### Trace 2: Central Trinomial Coefficients $T_n = [x^n](1 + x + x^2)^n$
By Cauchy's integral formula / diagonal extraction (Section 5), $F(x) = \sum_{n \ge 0} T_n x^n = (1 - 2x - 3x^2)^{-1/2}$. Applying Recipe A with $P(x) = 1 - 2x - 3x^2$ and $\alpha = -1/2$:
$$(1 - 2x - 3x^2) F'(x) = (1 + 3x) F(x)$$
Extracting $[x^{n-1}]$ gives $(n-1) T_{n-1} - 2(n-2) T_{n-2} - 3(n-3) T_{n-3} = T_{n-1} + 3 T_{n-2}$, which simplifies to:
$$n T_n = (2n - 1) T_{n-1} + 3(n - 1) T_{n-2} \qquad (n \ge 2)$$
- **Hand Check ($n = 0 \dots 4$)**: $T_0 = 1, T_1 = 1$; $2 T_2 = 3(1) + 3(1) = 6 \implies T_2 = 3$; $3 T_3 = 5(3) + 6(1) = 21 \implies T_3 = 7$; $4 T_4 = 7(7) + 9(3) = 76 \implies T_4 = 19$.

#### Trace 3: Central Delannoy Numbers $D_n = \sum_{k=0}^n \binom{n}{k}\binom{n+k}{k}$
The OGF is $F(x) = \sum_{n \ge 0} D_n x^n = (1 - 6x + x^2)^{-1/2}$. Applying Recipe A with $P(x) = 1 - 6x + x^2$ and $\alpha = -1/2$:
$$(1 - 6x + x^2) F'(x) = (3 - x) F(x) \implies n D_n = 3(2n - 1) D_{n-1} - (n - 1) D_{n-2} \qquad (n \ge 2)$$
- **Hand Check ($n = 0 \dots 3$)**: $D_0 = 1, D_1 = 3$; $2 D_2 = 9(3) - 1(1) = 26 \implies D_2 = 13$; $3 D_3 = 15(13) - 2(3) = 189 \implies D_3 = 63$.

#### Trace 4: Large Schröder Numbers $S_n$ (Inhomogeneous Quadratic Algebraic ODE)
$S(x) = \sum_{n \ge 0} S_n x^n$ satisfies $x S(x)^2 - (1 - x) S(x) + 1 = 0$, so $S(x) = \frac{1 - x - \sqrt{1 - 6x + x^2}}{2x}$. Applying Recipe B with $A(x) = x, B(x) = -(1-x), C(x) = 1, \Delta(x) = 1 - 6x + x^2$:
$$x(1 - 6x + x^2) S'(x) + (1 - 3x - x^2) S(x) = 1 - x$$
Extracting $[x^n]$ for $n \ge 2$ (where the inhomogeneous right-hand side $1 - x$ vanishes!) yields:
$$(n + 1) S_n = 3(2n - 1) S_{n-1} - (n - 2) S_{n-2} \qquad (n \ge 2)$$
- **Hand Check ($n = 0 \dots 4$)**: $S_0 = 1, S_1 = 2$; $3 S_2 = 9(2) - 0 = 18 \implies S_2 = 6$; $4 S_3 = 15(6) - 1(2) = 88 \implies S_3 = 22$; $5 S_4 = 21(22) - 2(6) = 450 \implies S_4 = 90$.

#### Trace 5: 2-Regular Simple Graphs (Disjoint Unions of Undirected Cycles of Length $\ge 3$)
A 2-regular simple labeled graph on $n$ vertices is a disjoint union of undirected cycles of length $\ge 3$. Since a single undirected cycle of length $k \ge 3$ has $\frac{(k-1)!}{2}$ labelings, the connected EGF is $C(x) = \sum_{k \ge 3} \frac{(k-1)!}{2} \frac{x^k}{k!} = \frac{1}{2}\ln\frac{1}{1 - x} - \frac{x}{2} - \frac{x^2}{4}$, and by the Exp-Log theorem the EGF of 2-regular simple graphs is:
$$F(x) = \sum_{n=0}^{\infty} g_n \frac{x^n}{n!} = \exp(C(x)) = \frac{\exp\!\left(-\frac{x}{2} - \frac{x^2}{4}\right)}{\sqrt{1 - x}}$$
1. **Logarithmic Differentiation**:
   $$\frac{F'(x)}{F(x)} = C'(x) = \frac{1}{2(1 - x)} - \frac{1}{2} - \frac{x}{2} = \frac{x^2}{2(1 - x)} \implies 2(1 - x) F'(x) = x^2 F(x)$$
2. **Coefficient Extraction**: Extracting $[x^{n-1}]$ for $f_n = [x^n] F(x) = \frac{g_n}{n!}$ yields $2n f_n - 2(n-1) f_{n-1} = f_{n-3}$, i.e.:
   $$f_n = \frac{n - 1}{n} f_{n-1} + \frac{1}{2n} f_{n-3} \implies g_n = (n - 1) g_{n-1} + \binom{n - 1}{2} g_{n-3} \qquad (n \ge 3)$$
   with $g_0 = 1, g_1 = 0, g_2 = 0$.
- **Hand Check ($n = 0 \dots 5$)**: $g_3 = 2 g_2 + \binom{2}{2} g_0 = 1$ (one triangle $K_3$); $g_4 = 3(1) + \binom{3}{2}(0) = 3$ (three 4-cycles); $g_5 = 4(3) + \binom{4}{2}(0) = 12$ (twelve 5-cycles); $g_6 = 5(12) + \binom{5}{2}(1) = 70$ ($60$ 6-cycles plus $10$ pairs of triangles).

---

### 2.5 Failure Modes, Indicial Polynomials & The $p$-Adic Lifting Contract

When unrolling a linear ODE $\sum_{j=0}^m q_j(x) F^{(j)}(x) = R(x)$ into a recurrence $I(n) a_n = \text{RHS}(a_{n-1}, \dots, a_{n-r})$, the leading coefficient multiplying $a_n$ is the **indicial polynomial**:
$$I(n) = \sum_{j=0}^{m} q_{j, j} \, n^{\underline{j}}$$
Three distinct failure regimes can occur when dividing by $I(n) \bmod p$:

1. **Regime 1 — Apparent / Regular Singular Points in $\mathbb{Q}$ ($I(n^*) = 0$ for an integer $n^* \ge 0$)**:
   - This occurs when $q_m(0) = 0$ (e.g., in composition $H(x) = F(A(x))$ when $\operatorname{val}(A') = v - 1 \ge 1$).
   - **Fix**: Never blindly set $a_{n^*} = 0$! Either (a) precompute the initial values $a_0, \dots, a_{n_{\max}}$ up to the largest positive integer root $n_{\max}$ of $I(n) = 0$ by combinatorial DP / brute force, or (b) differentiate the ODE $k$ times (L'Hôpital shift in index space) to extract a non-vanishing relation for $a_{n^*}$.
2. **Regime 2 — $p$-Adic Modular Vanishing ($I(n^*) \neq 0$ in $\mathbb{Q}$, but $I(n^*) \equiv 0 \pmod p$ for some $n^* \le N$)**:
   - Even if $N < p$ so that $n! \not\equiv 0 \pmod p$, a polynomial factor such as $I(n) = n(2n + 1)(3n - 5)$ can vanish modulo $p$ at $n^* = (p-1)/2$.
   - **The $p$-Adic Lifting Contract ($\mathbb{Z}/p^{V+1}\mathbb{Z}$)**: Count the total $p$-adic valuation $V = \sum_{n=1}^{N} v_p(I(n))$ lost across all steps $n \in [1, N]$. Carry out the recurrence arithmetic over the ring $\mathbb{Z}/p^{V+1}\mathbb{Z}$, representing each intermediate value as $u \cdot p^e$ with $p \nmid u$. At a singular step $n^*$ where $e_I = v_p(I(n^*)) > 0$, because the exact rational sequence $a_n$ is $p$-integral, the right-hand side is guaranteed to be divisible by $p^{e_I}$. Dividing out $p^{e_I}$ and multiplying by $(I(n^*) / p^{e_I})^{-1} \bmod p^{V+1}$ loses $e_I$ digits of $p$-adic precision, leaving at least $1$ exact digit modulo $p$ at $n = N$!
3. **Regime 3 — Transcendental Non-Holonomic Series**:
   - Partition numbers $\prod_{k \ge 1}(1-x^k)^{-1}$, Bell numbers $e^{e^x-1}$, and $\tan x$ have infinitely many singularities and satisfy **no** linear ODE with polynomial coefficients. They require nonlinear ODE methods (Section 3) or CDQ / Relaxed Convolution (Section 6).

---

### 2.6 Production C++ Templates: Automated ODE-to-Recurrence Unroller & P-Recursive Berlekamp–Massey Finder

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    if (base < 0) base += MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}
long long modInverse(long long n) { return power(n, MOD - 2); }

// 1. General Linear ODE Unroller:
// Solves sum_{j=0}^m q[j](x) * F^(j)(x) = rhs(x) mod x^(N+1) in O(N * m * d) time.
vector<long long> solve_linear_ode(
    const vector<vector<long long>>& q, // q[j][i] = [x^i] q_j(x)
    const vector<long long>& rhs,       // rhs[k]  = [x^k] R(x)
    const vector<long long>& init_a,    // Known initial coefficients a[0..init_a.size()-1]
    int N
) {
    int m = (int)q.size() - 1;
    int d = 0;
    for (int j = 0; j <= m; ++j)
        d = max(d, (int)q[j].size() - 1);

    vector<long long> a(N + 1, 0);
    for (int i = 0; i < (int)init_a.size() && i <= N; ++i)
        a[i] = (init_a[i] % MOD + MOD) % MOD;

    auto falling_fact = [&](long long x, int j) -> long long {
        if (x < j) return 0;
        long long res = 1;
        for (int t = 0; t < j; ++t)
            res = res * ((x - t) % MOD) % MOD;
        return res;
    };

    for (int n = (int)init_a.size(); n <= N; ++n) {
        // Align at [x^(n - s0)] where s0 is the largest shift j - i with non-zero q[j][i]
        int s0 = -d - 1;
        for (int j = 0; j <= m; ++j)
            for (int i = 0; i < (int)q[j].size(); ++i)
                if (q[j][i] != 0) s0 = max(s0, j - i);

        int k = n - s0; // Extracting [x^k] from the ODE
        if (k < 0) continue;

        long long lead_coeff = 0;
        long long sum_known = (k < (int)rhs.size()) ? rhs[k] : 0;

        for (int j = 0; j <= m; ++j) {
            for (int i = 0; i < (int)q[j].size(); ++i) {
                if (q[j][i] == 0) continue;
                int idx = k - i + j;
                if (idx < 0 || idx > n) continue;
                long long term = q[j][i] * falling_fact(idx, j) % MOD;
                if (idx == n) {
                    lead_coeff = (lead_coeff + term) % MOD;
                } else {
                    sum_known = (sum_known - term * a[idx]) % MOD;
                    if (sum_known < 0) sum_known += MOD;
                }
            }
        }
        assert(lead_coeff != 0 && "Indicial polynomial vanished at step n! Supply more init_a.");
        a[n] = sum_known * modInverse(lead_coeff) % MOD;
    }
    return a;
}

// 2. Automated P-Recursive Relation Finder (Gaussian Elimination over K[n]):
// Discovers P_0(n)a_n + ... + P_r(n)a_{n+r} = 0 of order r and degree d from first M terms.
vector<vector<long long>> find_p_recursive(const vector<long long>& a, int r, int d) {
    int num_vars = (r + 1) * (d + 1);
    int num_eqs = (int)a.size() - r;
    assert(num_eqs >= num_vars);
    vector<vector<long long>> mat(num_eqs, vector<long long>(num_vars, 0));
    for (int n = 0; n < num_eqs; ++n) {
        for (int k = 0; k <= r; ++k) {
            long long npow = 1;
            for (int j = 0; j <= d; ++j) {
                mat[n][k * (d + 1) + j] = a[n + k] * npow % MOD;
                npow = npow * n % MOD;
            }
        }
    }
    int rank = 0;
    vector<int> pivot_col(num_vars, -1);
    for (int col = 0; col < num_vars && rank < num_eqs; ++col) {
        int sel = -1;
        for (int row = rank; row < num_eqs; ++row)
            if (mat[row][col] != 0) { sel = row; break; }
        if (sel == -1) continue;
        swap(mat[rank], mat[sel]);
        pivot_col[col] = rank;
        long long inv = modInverse(mat[rank][col]);
        for (int c = col; c < num_vars; ++c)
            mat[rank][c] = mat[rank][c] * inv % MOD;
        for (int row = 0; row < num_eqs; ++row) {
            if (row != rank && mat[row][col] != 0) {
                long long factor = mat[row][col];
                for (int c = col; c < num_vars; ++c)
                    mat[row][c] = (mat[row][c] - factor * mat[rank][c] % MOD + MOD) % MOD;
            }
        }
        rank++;
    }
    int free_col = -1;
    for (int col = num_vars - 1; col >= 0; --col)
        if (pivot_col[col] == -1) { free_col = col; break; }
    assert(free_col != -1 && "No non-trivial P-recursive relation found for (r, d)!");
    vector<long long> sol(num_vars, 0);
    sol[free_col] = 1;
    for (int col = 0; col < free_col; ++col)
        if (pivot_col[col] != -1)
            sol[col] = (MOD - mat[pivot_col[col]][free_col]) % MOD;

    vector<vector<long long>> P(r + 1, vector<long long>(d + 1, 0));
    for (int k = 0; k <= r; ++k)
        for (int j = 0; j <= d; ++j)
            P[k][j] = sol[k * (d + 1) + j];
    return P;
}
```

---

## 3. Iteration 42 / 94: Differential Equation Substitutions, Linearization, Riccati & Autonomous ODEs

### 3.1 The Master 7-Archetype Differential Equation Substitution Table

Before invoking a heavy numerical solver, always match the combinatorial ODE against the following 7 algebraic substitution archetypes synthesised across Pre-existing, Cohort 1, and Cohort 2:

| # | ODE Archetype | Diagnostic Signal | Canonical Substitution | Transformed Linear / Algebraic Target |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Inhomogeneous 1st-Order Linear**<br>$F'(x) + P(x) F(x) = Q(x)$ | Linear in $F, F'$, non-zero forcing $Q(x)$. | Integrating factor $\mu(x) = \exp\!\left(\int_0^x P(t)\,dt\right)$ | $\frac{d}{dx}[\mu(x) F(x)] = \mu(x) Q(x)$<br>$F(x) = \mu(x)^{-1} \left(F_0 + \int_0^x \mu(t) Q(t)\,dt\right)$ |
| **2** | **Bernoulli Nonlinear ODE**<br>$F'(x) + P(x) F(x) = Q(x) F(x)^m$ ($m \neq 0, 1$) | Single nonlinear power $F(x)^m$ on RHS. | $U(x) = F(x)^{1-m}$ | $U'(x) + (1-m) P(x) U(x) = (1-m) Q(x)$ (Archetype 1!) |
| **3** | **Riccati Quadratic ODE**<br>$F'(x) = A(x) + B(x) F(x) + C(x) F(x)^2$ | Quadratic nonlinearity $F^2$ from binary splitting at root/extremum. | Logarithmic derivative:<br>$F(x) = -\frac{u'(x)}{C(x) u(x)}$, $u(0) = 1$ | 2nd-Order Linear D-Finite ODE:<br>$C u'' - (C' + BC) u' + A C^2 u = 0$ |
| **4** | **Autonomous 1st-Order ODE**<br>$F'(x) = \Phi(F(x))$ (no explicit $x$) | Shift-invariant combinatorial structure (trees, Eulerian numbers, alternating perms). | Separation of variables:<br>$G(y) = F^{\langle -1 \rangle}(y)$ | $G'(y) = \frac{1}{\Phi(y)} \implies G(y) = \int_{F_0}^{y} \frac{dt}{\Phi(t)}$<br>Recover $F(x) = G^{\langle -1 \rangle}(x)$ |
| **5** | **Autonomous Conservative 2nd-Order ODE**<br>$F''(x) = \Psi(F(x))$ | 2nd derivative depends only on $F$. | **Energy Integral Trick**:<br>Multiply by $2 F'(x)$ | $(F'(x)^2)' = 2 \Psi(F(x)) F'(x)$<br>$F'(x) = \sqrt{F'(0)^2 + 2 \int_{F(0)}^{F(x)} \Psi(u)\,du}$ (Archetype 4!) |
| **6** | **Variable Leading Coefficient**<br>$q_2(x) F'' + q_1(x) F' + q_0(x) F = 0$ | Leading polynomial $q_2(x)$ complicates $F''$; e.g. $q_2(x) = (1+x)^2$ or $1-4x$. | **Liouville Change of Variable**:<br>$u = \phi(x) = \int \frac{dx}{\sqrt{q_2(x)}}$, $F(x) = G(u)$ | Normalizes $G_{uu}$ coefficient to $1$; for $(1+x)\frac{d}{dx}$, $u = \ln(1+x)$ gives $\frac{d}{du} = (1+x)\frac{d}{dx}$. |
| **7** | **2nd-Order with Unwanted $F'(z)$ Drift**<br>$D''(z) - 2 p(z) D'(z) + q(z) D(z) = 0$ | Middle term $-2p(z)D'(z)$ obstructs Bessel/hypergeometric matching. | **Gauge Transformation**:<br>$D(z) = \exp\!\left(\int p(z)\,dz\right) B(z)$ | Eliminates first derivative:<br>$B''(z) + (q(z) - p(z)^2 - p'(z)) B(z) = 0$ |

---

### 3.2 Deep Dive on Archetypes 1, 3, 4 & Newton Iteration on General Nonlinear ODEs

#### 1. Integrating Factor Shortcut (Eliminating Polynomial Inversion)
In Archetype 1 ($F' + P F = Q$), computing $\mu(x) = \exp(\int_0^x P(t)\,dt)$ and then calling `inv(mu)` wastes a full $O(N \log N)$ polynomial inversion.
> **Cohort 1 Optimization**: In $\mathbb{K}[[x]]$, $\exp(A(x))^{-1} = \exp(-A(x))$ identically! Defining $I(x) = \int_0^x P(t)\,dt$, we compute $\mu(x) = \exp(I(x))$ and $\mu(x)^{-1} = \exp(-I(x))$ directly—or when $P(x) = \frac{\alpha U'(x)}{U(x)}$, we get $\mu(x) = U(x)^\alpha$ and $\mu(x)^{-1} = U(x)^{-\alpha}$ algebraically in $O(N)$ without any transcendental calls!

#### 2. Riccati Substitution & Regular Singular Point Analysis when $\operatorname{val}(C) \ge 1$
> **Diagnostic Signal**: Why does $F(x) = -\frac{u'(x)}{C(x) u(x)}$ linearize $F' = A + B F + C F^2$?
> **Reverse-Engineering Scratchpad**: Differentiating $F = -C^{-1} u'/u$ by the quotient rule produces $+\frac{(u')^2}{C u^2}$, which is **identical** to $C F^2 = C \left(-\frac{u'}{C u}\right)^2 = \frac{(u')^2}{C u^2}$! Thus the quadratic term $(u')^2 / u^2$ cancels completely from both sides:
> $$-\frac{u''}{C u} + \frac{(u')^2}{C u^2} + \frac{C' u'}{C^2 u} = A - B \frac{u'}{C u} + \frac{(u')^2}{C u^2} \implies C(x) u''(x) - \left(C'(x) + B(x) C(x)\right) u'(x) + A(x) C(x)^2 u(x) = 0$$
- **What if $C(0) = 0$ ($\operatorname{val}(C) = v \ge 1$)?**
  If $C(x) = x^v \widetilde{C}(x)$ with $\widetilde{C}(0) \neq 0$, the ODE for $u(x)$ has a regular singular point at $x = 0$. Instead of dividing by $x^v$, define $W(x) = C(x) F(x) = x^v \widetilde{C}(x) F(x)$, which has valuation $\ge v$ and satisfies:
  $$W'(x) = A(x) C(x) + \left( B(x) + \frac{C'(x)}{C(x)} \right) W(x) + W(x)^2$$
  Now the substitution $W(x) = -\frac{u'(x)}{u(x)}$ has $u(0) = 1, u'(0) = \dots = u^{(v)}(0) = 0$, and multiplying by $C(x)$ gives the nonsingular polynomial-coefficient ODE:
  $$C(x) u''(x) - \left( C'(x) + B(x) C(x) \right) u'(x) + A(x) C(x)^2 u(x) = 0$$

#### 3. Newton Iteration with Integrating Factor for General Nonlinear 1st-Order ODEs $F'(x) = G(x, F(x))$
When $G(x, y)$ is neither quadratic in $y$ (Riccati) nor autonomous (e.g., $F'(x) = e^{F(x)} + x F(x)^3$), we lift Newton's method to differential equations:
> **Reverse-Engineering Scratchpad**: Suppose we have computed $F_k(x) \equiv F(x) \bmod x^m$. Write $F_{k+1}(x) = F_k(x) + \Delta(x) \bmod x^{2m}$ where $\Delta(x) = O(x^m)$ implies $\Delta(x)^2 \equiv 0 \bmod x^{2m}$. Taylor-expanding $G(x, F_k + \Delta)$ to first order gives:
> $$F_k'(x) + \Delta'(x) \equiv G(x, F_k(x)) + G_y(x, F_k(x)) \Delta(x) \pmod{x^{2m}}$$
> Rearranging yields a **first-order linear ODE** for the correction $\Delta(x)$:
> $$\Delta'(x) - G_y(x, F_k(x)) \Delta(x) \equiv G(x, F_k(x)) - F_k'(x) \pmod{x^{2m}}, \qquad \Delta(0) = 0$$
> Setting $r(x) = \exp\!\left(-\int_0^x G_y(t, F_k(t))\,dt\right) \bmod x^{2m}$, we obtain the quadratic-doubling update:
> $$F_{k+1}(x) \equiv F_k(x) + r(x)^{-1} \int_0^x r(t) \left( G(t, F_k(t)) - F_k'(t) \right) dt \pmod{x^{2m}}$$
> Total time complexity: $T(N) = T(N/2) + O(N \log N) = O(N \log N)$!

```cpp
// Production C++ Template 1 (Delta Update Form): General Nonlinear 1st-Order ODE Solver F'(x) = G(x, F(x))
// Requires standard FPS poly_mul, poly_inv, poly_exp, poly_deriv, poly_integ.
// eval_G(F, len) returns { G(x, F(x)) mod x^len, G_y(x, F(x)) mod x^len }.
template <typename Func>
vector<long long> solve_nonlinear_first_order_ode(
    long long f0, int N, Func eval_G,
    auto poly_mul, auto poly_inv, auto poly_exp, auto poly_deriv, auto poly_integ
) {
    vector<long long> F = { (f0 % MOD + MOD) % MOD };
    for (int len = 1; len < N; len <<= 1) {
        int next_len = min(N, len << 1);
        auto [G_val, Gy_val] = eval_G(F, next_len);

        // r(x) = exp(- \int_0^x G_y(t, F(t)) dt) mod x^next_len
        vector<long long> neg_Gy(next_len, 0);
        for (int i = 0; i < (int)Gy_val.size() && i < next_len; ++i)
            neg_Gy[i] = (MOD - Gy_val[i]) % MOD;
        vector<long long> r = poly_exp(poly_integ(neg_Gy, next_len), next_len);
        vector<long long> r_inv = poly_inv(r, next_len);

        // rhs(x) = G(x, F_k(x)) - F_k'(x) (vanishes for degrees < len - 1)
        vector<long long> dF = poly_deriv(F);
        vector<long long> rhs(next_len, 0);
        for (int i = 0; i < next_len; ++i) {
            long long g_i = (i < (int)G_val.size()) ? G_val[i] : 0;
            long long df_i = (i < (int)dF.size()) ? dF[i] : 0;
            rhs[i] = (g_i - df_i + MOD) % MOD;
        }
        vector<long long> prod = poly_mul(r, rhs);
        prod.resize(next_len - 1);
        vector<long long> delta = poly_mul(r_inv, poly_integ(prod, next_len));
        F.resize(next_len, 0);
        for (int i = len; i < next_len; ++i)
            F[i] = (F[i] + delta[i]) % MOD;
    }
    return F;
}

// Production C++ Template 2 (Direct Nyaan's Library Form): F_{k+1} = I^{-1} * (f0 + \int I * R dx)
// Where R(x) = G(x, F_k) - F_k'(x) + G_y(x, F_k) * F_k(x) mod x^{next_d}
template <typename EvalFunc>
Poly solve_first_order_ode(int N, long long f0, EvalFunc eval_G) {
    Poly F = { (f0 % MOD + MOD) % MOD };
    for (int d = 1; d < N; d <<= 1) {
        int next_d = min(N, 2 * d);
        auto [G_val, G_y] = eval_G(F, next_d);
        // 1. Integrating factor: I(x) = exp(-integral(G_y dx)) mod x^{next_d}
        Poly minus_Gy(next_d, 0);
        for (int i = 0; i < (int)G_y.size() && i < next_d; ++i)
            minus_Gy[i] = (MOD - G_y[i]) % MOD;
        Poly int_minus_Gy = fps_integ(minus_Gy);
        int_minus_Gy.resize(next_d, 0);
        Poly I = fps_exp(int_minus_Gy, next_d);
        Poly I_inv = fps_inv(I, next_d);
        // 2. Residual: R(x) = G(x, F_k) + G_y(x, F_k) * F_k(x) mod x^{next_d} (since I * F_k' integrates by parts)
        Poly F_der = fps_deriv(F);
        Poly Gy_F = multiply(G_y, F);
        Gy_F.resize(next_d, 0);
        Poly R(next_d, 0);
        for (int i = 0; i < next_d; ++i) {
            long long v = (i < (int)G_val.size() ? G_val[i] : 0);
            if (i < (int)F_der.size()) v = (v - F_der[i] + MOD) % MOD;
            if (i < (int)Gy_F.size()) v = (v + Gy_F[i]) % MOD;
            R[i] = v;
        }
        // 3. Linear solve: F_{k+1} = F_k + I_inv * integral(I * (G - F_k') dx)
        // Or directly via product rule (I * F_k)' = I * F_k' - I * G_y * F_k:
        Poly rhs(next_d, 0);
        for (int i = 0; i < next_d; ++i) {
            long long g_i = (i < (int)G_val.size() ? G_val[i] : 0);
            long long df_i = (i < (int)F_der.size() ? F_der[i] : 0);
            rhs[i] = (g_i - df_i + MOD) % MOD;
        }
        Poly I_rhs = multiply(I, rhs);
        I_rhs.resize(next_d - 1, 0);
        Poly delta = multiply(I_inv, fps_integ(I_rhs));
        F.resize(next_d, 0);
        for (int i = d; i < next_d; ++i)
            F[i] = (F[i] + delta[i]) % MOD;
    }
    return F;
}
```

---

### 3.3 Five Complete Worked Demonstrations & Hand-Checkable Toy Traces

#### Worked Demonstration 1: Integrating Factor + Catalan Rationalizing Substitution $x = u(1-u)$
**Problem**: Solve $(1 - 4x) F'(x) - 2 F(x) = \frac{1}{1 - 3x}$ with $F(0) = 1$, and extract $[x^n] F(x)$ in $O(n)$ time.
1. **Standard Form & Integrating Factor**: Divide by $1 - 4x$: $F'(x) - \frac{2}{1 - 4x} F(x) = \frac{1}{(1 - 4x)(1 - 3x)}$.
   $$\mu(x) = \exp\!\left( \int_0^x \frac{-2}{1 - 4t}\,dt \right) = \exp\!\left( \frac{1}{2} \ln(1 - 4x) \right) = \sqrt{1 - 4x}$$
2. **Exact Integration via Catalan Substitution**:
   $$\frac{d}{dx}\left[ \sqrt{1 - 4x}\, F(x) \right] = \frac{1}{(1 - 3x)\sqrt{1 - 4x}}$$
   Notice the square root $\sqrt{1 - 4x}$! Substitute $x = u(1 - u)$ with $u(0) = 0$. Then $1 - 4x = (1 - 2u)^2$, so $\sqrt{1 - 4x} = 1 - 2u$ and $dx = (1 - 2u)\,du = \sqrt{1 - 4x}\,du$, which **cancels $\sqrt{1 - 4x}$ completely**:
   $$\int_0^x \frac{dt}{(1 - 3t)\sqrt{1 - 4t}} = \int_0^u \frac{dv}{1 - 3v(1 - v)} = \int_0^u \frac{dv}{1 - 3v + 3v^2}$$
3. **Direct P-Recursive Extraction**: Rather than inverting $u$, clear denominators in the original ODE directly:
   $$(1 - 7x + 12x^2) F'(x) - (2 - 6x) F(x) = 1 \implies (n + 1) f_{n+1} = (7n + 2) f_n - 6(2n - 1) f_{n-1} \quad (n \ge 1)$$
   with $f_0 = 1, f_1 = 3$.
   - **Hand Check**: $n = 1 \implies 2 f_2 = 9(3) - 6(1) = 21 \implies f_2 = 21/2$; $n = 2 \implies 3 f_3 = 16(21/2) - 18(3) = 114 \implies f_3 = 38$.

#### Worked Demonstration 2: Catalan Tree Differential Equation $(1 - 2x F(x)) F'(x) = F(x)^2$ via Both Variable Swap and Integrating-Factor Newton Iteration
Differentiating the algebraic Catalan equation $F(x) = 1 + x F(x)^2$ with respect to $x$ yields $F'(x) = F(x)^2 + 2x F(x) F'(x)$, i.e., $(1 - 2x F(x)) F'(x) = F(x)^2$ with $F(0) = 1$.
1. **Route A (Analytic Variable Swap / Compositional Inverse)**:
   - View $x = G(y)$ as a function of $y = F(x)$ (so $G'(y) = 1 / F'(x)$ and $G(1) = 0$). Then $(1 - 2x F(x)) F'(x) = F(x)^2$ becomes:
     $$1 - 2y G(y) = y^2 G'(y) \implies y^2 G'(y) + 2y G(y) = 1 \implies \frac{d}{dy}\left[ y^2 G(y) \right] = 1.$$
   - Integrating with $G(1) = 0$ gives $y^2 G(y) = y - 1 \implies x = \frac{F(x) - 1}{F(x)^2} \implies x F(x)^2 - F(x) + 1 = 0$, recovering $F(x) = \frac{1 - \sqrt{1 - 4x}}{2x} = \sum_{n \ge 0} C_n x^n$.
   - *(Alternative Variable Swap $u = x F(x)$)*: Since $F(x) = u / x$ and $\frac{du}{dx} = F(x) + x F'(x)$, multiplying $(1 - 2u) F'(x) = F(x)^2$ by $x$ gives $(1 - 2u)\left(\frac{du}{dx} - F(x)\right) = u F(x) \implies (1 - 2u)\frac{du}{dx} = (1 - u)\frac{u}{x}$. Separating variables gives $\frac{dx}{x} = \left(\frac{1}{u} - \frac{1}{1 - u}\right)du \implies x = u(1 - u)$.
2. **Route B (Numerical Trace of Integrating-Factor Newton Solver on $F' = \frac{F^2}{1 - 2x F}$ up to $N = 4$)**:
   Let $A(x, y) = \frac{y^2}{1 - 2xy}$, so $A_y(x, y) = \frac{2y(1 - xy)}{(1 - 2xy)^2}$:
   - **Base ($m = 1$)**: $F_1(x) = 1$.
   - **Step $m = 1 \to 2$ ($\bmod x^2$)**: $A(x, 1) \equiv 1 \pmod{x}$, and $P(x) = -A_y(x, 1) \equiv -2 \pmod{x}$. The integrating factor is $\mu(x) = \exp\!\left(\int -2\,dx\right) \equiv 1 - 2x \pmod{x^2}$, and the residual is $R(x) = A(x, 1) - F_1'(x) \equiv 1 \pmod{x}$. Thus $\Delta(x) \equiv \mu(x)^{-1} \int R(x)\mu(x)\,dx \equiv (1 + 2x) \int 1\,dx \equiv x \pmod{x^2}$, giving $F_2(x) = 1 + x$.
   - **Step $m = 2 \to 4$ ($\bmod x^4$)**: With $F_2(x) = 1 + x$, we have $1 - 2x F_2(x) = 1 - 2x - 2x^2$, so $(1 - 2x F_2(x))^{-1} \equiv 1 + 2x + 6x^2 \pmod{x^3}$ and $(1 - 2x F_2(x))^{-2} \equiv 1 + 4x + 16x^2 \pmod{x^3}$:
     - $A(x, F_2) = (1 + 2x + x^2)(1 + 2x + 6x^2) \equiv 1 + 4x + 11x^2 \pmod{x^3}$.
     - $R(x) = A(x, F_2) - F_2'(x) = (1 + 4x + 11x^2) - 1 = 4x + 11x^2 \pmod{x^3}$.
     - $P(x) = -A_y(x, F_2) = -\frac{2(1+x)(1 - x - x^2)}{(1 - 2x - 2x^2)^2} \equiv -2(1 - x^2)(1 + 4x + 16x^2) \equiv -2 - 8x - 30x^2 \pmod{x^3}$.
     - $\int P(x)\,dx \equiv -2x - 4x^2 - 10x^3 \pmod{x^4}$, so $\mu(x) = \exp(-2x - 4x^2 - 10x^3) \equiv 1 - 2x - 2x^2 - \frac{14}{3} x^3 \pmod{x^4}$ and $\mu(x)^{-1} \equiv 1 + 2x + 6x^2 + \frac{50}{3} x^3 \pmod{x^4}$.
     - Multiplying $\mu(x) R(x) \equiv (1 - 2x)(4x + 11x^2) \equiv 4x + 3x^2 \pmod{x^3}$, integrating gives $\int \mu(x) R(x)\,dx \equiv 2x^2 + x^3 \pmod{x^4}$, and multiplying by $\mu(x)^{-1}$ yields $\Delta(x) \equiv (2x^2 + x^3)(1 + 2x) \equiv 2x^2 + 5x^3 \pmod{x^4}$.
     - Updating $F_4(x) = F_2(x) + \Delta(x) = 1 + x + 2x^2 + 5x^3 = C_0 + C_1 x + C_2 x^2 + C_3 x^3$ recovers the exact Catalan numbers!

#### Worked Demonstration 3: Dependent Variable Substitution on a Non-Standard Riccati ODE ($F'(x) = 1 + 2x F(x) + F(x)^2$)
Consider solving $F'(x) = 1 + 2x F(x) + F(x)^2$ with $F(0) = 0$ in $O(N \log N)$ time (with an $O(N)$ inner ODE step):
1. **Riccati-to-Second-Order Ansatz**: Substitute $F(x) = -\frac{U'(x)}{U(x)}$ with $U(0) = 1, U'(0) = -F(0) = 0$.
2. **Exact Cancellation of the Quadratic Term**: Since $F'(x) = -\frac{U''(x)}{U(x)} + \left(\frac{U'(x)}{U(x)}\right)^2$, the quadratic term $\left(\frac{U'}{U}\right)^2$ cancels $F(x)^2$ identically:
   $$-\frac{U''(x)}{U(x)} = 1 - 2x \frac{U'(x)}{U(x)} \implies U''(x) - 2x U'(x) + U(x) = 0.$$
3. **$O(N)$ Coefficient Extraction**: Extracting $[x^n]$ from $U''(x) - 2x U'(x) + U(x) = 0$ gives:
   $$(n + 2)(n + 1) u_{n+2} - (2n - 1) u_n = 0 \implies u_{n+2} = \frac{2n - 1}{(n + 2)(n + 1)} u_n.$$
   Since $u_0 = 1$ and $u_1 = 0$, all odd coefficients vanish and $U(x) = 1 - \frac{1}{2}x^2 - \frac{1}{8}x^4 - \frac{7}{240}x^6 - \dots$ is computed in $O(N)$ time, after which $F(x) = -U'(x) U(x)^{-1} \bmod x^N$ requires only a single polynomial inversion!

#### Worked Demonstration 4: QOJ #60 (Chinese Elephant Chess) Chain-Rule + Gauge Reduction to Bessel ODE
In QOJ #60 (`[ZH]` skip2004 / QOJ #60 *中国象棋*), a component EGF $D_d(z)$ satisfies the variable-coefficient 2nd-order ODE:
$$D_d''(z) - (2 q(z) + a) D_d'(z) + \left( q(z)^2 - q'(z) + a q(z) - b \right) D_d(z) = 0$$
1. **Step 1 (Gauge Transformation — Archetype 7)**: Factor out the drift $q(z)$ via $D_d(z) = \exp\!\left(\int_0^z q(u)\,du\right) Y_d(z)$. Then $Y_d(z)$ satisfies the constant-coefficient ODE $Y_d''(z) - a Y_d'(z) - b Y_d(z) = 0$!
2. **Step 2 (General Chain-Rule + Gauge Normalization)**: More generally, substituting $D_d(z) = h(z) B_d(t(z))$ gives:
   $$D_d'' + P_1(z) D_d' + P_0(z) D_d = h(t')^2 \left[ B_d''(t) + \left( \frac{2 h'}{h t'} + \frac{t''}{(t')^2} + \frac{P_1}{t'} \right) B_d'(t) + \frac{h'' + P_1 h' + P_0 h}{h (t')^2} B_d(t) \right] = 0$$
   Choosing $t(z)$ so the $B_d(t)$ coefficient matches the target canonical equation (e.g. modified Bessel $I_d(t)$) and solving $\frac{2 h'}{h} + \frac{t''}{t'} + P_1 = \frac{t'}{t}$ for $h(z)$ reduces all $d$ component ODEs to a single precomputed standard series $B_d(t)$!

#### Worked Demonstration 5: Two Hand-Checkable Toy Traces ($n \le 4$) for Autonomous and Euler–Cauchy Substitutions
- **Toy Trace A (Autonomous ODE $F'(x) = (1 + F(x))^2, F(0) = 0$ via Compositional Inverse)**:
  1. Write $G(y) = \int_0^y \frac{dt}{(1 + t)^2}$ where $G(F(x)) = x$.
  2. Expand $\frac{1}{(1 + t)^2} = 1 - 2t + 3t^2 - 4t^3 + O(t^4)$ and integrate term-by-term: $G(y) = y - y^2 + y^3 - y^4 + O(y^5) = \frac{y}{1 + y}$.
  3. Solving $x = \frac{y}{1 + y}$ yields $F(x) = y = \frac{x}{1 - x} = x + x^2 + x^3 + x^4 + O(x^5)$.
- **Toy Trace B (Euler–Cauchy ODE $(1 + x)^2 F''(x) + (1 + x) F'(x) - F(x) = 0$ with $F(0) = 1, F'(0) = 2$ via $u = \ln(1 + x)$)**:
  1. Substitute $u = \ln(1 + x)$, so $(1 + x)\frac{d}{dx} = \frac{d}{du}$ and $(1 + x)^2 F''(x) + (1 + x) F'(x) = G''(u)$ where $G(u) = F(e^u - 1)$.
  2. The variable-coefficient ODE collapses to $G''(u) - G(u) = 0$ with $G(0) = 1, G'(0) = 2$, yielding $G(u) = \cosh(u) + 2\sinh(u) = \frac{3}{2}e^u - \frac{1}{2}e^{-u}$.
  3. Substituting back $e^u = 1 + x$ gives $F(x) = \frac{3}{2}(1 + x) - \frac{1}{2}(1 + x)^{-1} = 1 + 2x - \frac{1}{2}x^2 + \frac{1}{2}x^3 - \frac{1}{2}x^4 + O(x^5)$.

---

## 4. Iteration 43 / 95: Sparse Formal Power Series Engine in $O(N \cdot K)$ Time

### 4.1 Core Philosophy: Why Sparse ODEs Beat Dense NTT When $K \ll \log^2 N$

Suppose $P(x) = \sum_{j=0}^{K} c_j x^{d_j}$ is a **sparse polynomial** with at most $K \ll N$ non-zero terms ($0 = d_0 < d_1 < \dots < d_K \le N$).
- **Critical Trap**: Never compute $P(x)^\alpha = \exp(\alpha \ln P(x))$ using sparse primitives! Even when $P(x) = 1 - x - x^2$ has $K = 3$ terms, $\ln P(x)$ is **completely dense** ($O(N)$ non-zero terms), so $\exp(\alpha \ln P(x))$ degrades to $O(N^2)$!
- Instead, for **every** elementary transcendental or algebraic operation $G(x) = \Phi(P(x))$, differentiate once to express $G'(x)$ directly in terms of $P(x)$, $P'(x)$, and $G(x)$ (which remains dense, while $P$ and $P'$ are $K$-sparse!), and extract $[x^{n-1}]$ to get an **$O(N \cdot K)$** recurrence!

| Operation $G(x) \bmod x^N$ | Defining First-Order Sparse ODE | Exact $O(N \cdot K)$ Coefficient Recurrence ($n = 1 \dots N-1$) | Base Case & Precondition |
| :--- | :--- | :--- | :--- |
| **`sparse_inv`**<br>$G(x) = P(x)^{-1}$ | $P(x) G(x) = 1$ (Algebraic, no $n^{-1}$ needed!) | $g_n = -\frac{1}{c_0} \sum_{j=1,\, d_j \le n}^{K} c_j \, g_{n - d_j}$ | $g_0 = c_0^{-1}$ ($c_0 \neq 0$) |
| **`sparse_div`**<br>$G(x) = A(x) / P(x)$ | $P(x) G(x) = A(x)$ (In-place on $A$!) | $g_n = \frac{1}{c_0} \left( a_n - \sum_{j=1,\, d_j \le n}^{K} c_j \, g_{n - d_j} \right)$ | $g_0 = a_0 c_0^{-1}$ ($c_0 \neq 0$) |
| **`sparse_ln`**<br>$G(x) = \ln P(x)$ | $P(x) G'(x) = P'(x)$ | $g_n = \frac{1}{n c_0} \left( n [x^n]P(x) - \sum_{j=1,\, d_j < n}^{K} (n - d_j) c_j \, g_{n - d_j} \right)$ | $g_0 = 0$ ($c_0 = 1$) |
| **`sparse_exp`**<br>$G(x) = \exp P(x)$ | $G'(x) = P'(x) G(x)$ | $g_n = \frac{1}{n} \sum_{j=1,\, d_j \le n}^{K} d_j c_j \, g_{n - d_j}$ | $g_0 = 1$ ($c_0 = 0$) |
| **`sparse_pow`**<br>$G(x) = P(x)^\alpha$ | $P(x) G'(x) = \alpha P'(x) G(x)$ | $g_n = \frac{1}{n c_0} \sum_{j=1,\, d_j \le n}^{K} \left( (\alpha + 1) d_j - n \right) c_j \, g_{n - d_j}$ | $g_0 = c_0^\alpha$ ($c_0 \neq 0$) |
| **`sparse_sqrt`**<br>$G(x) = \sqrt{P(x)}$ | $2 P(x) G'(x) = P'(x) G(x)$ ($\alpha = 1/2$) | $g_n = \frac{1}{n c_0} \sum_{j=1,\, d_j \le n}^{K} \left( \frac{3}{2} d_j - n \right) c_j \, g_{n - d_j}$ | $g_0 = \sqrt{c_0} \bmod p$ |
| **`sparse_sincos`**<br>$S = \sin P, C = \cos P$ | $S' = P' C,\quad C' = -P' S$ | $s_n = \frac{1}{n}\sum d_j c_j c_{n-d_j},\quad c_n = -\frac{1}{n}\sum d_j c_j s_{n-d_j}$ | $s_0 = 0, c_0 = 1$ ($P(0)=0$) |

---

### 4.2 Derivation & Hand Traces of `sparse_pow`, `sparse_sqrt`, and `sparse_exp`

> **Reverse-Engineering Scratchpad (`sparse_pow` Identity $P G' = \alpha P' G$)**:
> Let $G(x) = P(x)^\alpha = \sum_{n \ge 0} g_n x^n$ where $P(x) = c_0 + \sum_{j=1}^K c_j x^{d_j}$. Differentiating gives $G'(x) = \alpha P(x)^{\alpha - 1} P'(x)$, and multiplying by $P(x)$ clears the $\alpha - 1$ power:
> $$P(x) G'(x) = \alpha P'(x) G(x)$$
> Extract $[x^{n-1}]$ from both sides:
> $$\sum_{j=0}^{K} c_j (n - d_j) g_{n - d_j} = \alpha \sum_{j=1}^{K} d_j c_j g_{n - d_j}$$
> Isolate the $j = 0$ term ($d_0 = 0$, which is $n c_0 g_n$) on the left and move $j \ge 1$ to the right:
> $$n c_0 g_n = \sum_{j=1,\, d_j \le n}^{K} \left( \alpha d_j - (n - d_j) \right) c_j g_{n - d_j} = \sum_{j=1,\, d_j \le n}^{K} \left( (\alpha + 1) d_j - n \right) c_j g_{n - d_j}$$

#### Hand-Checkable Trace 1: Sparse Square Root $G(x) = (1 + 2x + x^3)^{1/2} \bmod x^5$
Here $\alpha = 1/2$, $c_0 = 1$, $(d_1, c_1) = (1, 2)$, $(d_2, c_2) = (3, 1)$, and $g_n = \frac{1}{n} \sum_{j=1}^2 \left(\frac{3}{2} d_j - n\right) c_j g_{n - d_j}$ with $g_0 = 1$:
- $n = 1$: $g_1 = \frac{1}{1} \left(\frac{3}{2}(1) - 1\right)(2) g_0 = 1$.
- $n = 2$: $g_2 = \frac{1}{2} \left(\frac{3}{2}(1) - 2\right)(2) g_1 = \frac{1}{2}(-1)(1) = -\frac{1}{2}$.
- $n = 3$: $g_3 = \frac{1}{3} \left[ \left(\frac{3}{2} - 3\right)(2) g_2 + \left(\frac{9}{2} - 3\right)(1) g_0 \right] = \frac{1}{3} \left[ (-3)\left(-\frac{1}{2}\right) + \frac{3}{2}(1) \right] = 1$.
- $n = 4$: $g_4 = \frac{1}{4} \left[ \left(\frac{3}{2} - 4\right)(2) g_3 + \left(\frac{9}{2} - 4\right)(1) g_1 \right] = \frac{1}{4} \left[ (-5)(1) + \frac{1}{2}(1) \right] = -\frac{9}{8}$.
- **Verification**: $\left(1 + x - \frac{1}{2} x^2 + x^3 - \frac{9}{8} x^4\right)^2 = 1 + 2x + (1 - 1)x^2 + (2 - 1)x^3 + \left(-\frac{9}{4} + 2 + \frac{1}{4}\right)x^4 + O(x^5) = 1 + 2x + x^3 + O(x^5)$.

#### Hand-Checkable Trace 2: Sparse Square Root $G(x) = \sqrt{1 + 2x - x^2} \bmod x^5$
Here $\alpha = 1/2$, $c_0 = 1$, $(d_1, c_1) = (1, 2)$, $(d_2, c_2) = (2, -1)$, and $g_0 = 1$:
- $n = 1$: $g_1 = \frac{1}{1}\left(\frac{3}{2}(1) - 1\right)(2) g_0 = 1$.
- $n = 2$: $g_2 = \frac{1}{2}\left[\left(\frac{3}{2}(1) - 2\right)(2) g_1 + \left(\frac{3}{2}(2) - 2\right)(-1) g_0\right] = \frac{1}{2}\big[(-1)(1) + (-1)(1)\big] = -1$.
- $n = 3$: $g_3 = \frac{1}{3}\left[\left(\frac{3}{2}(1) - 3\right)(2) g_2 + \left(\frac{3}{2}(2) - 3\right)(-1) g_1\right] = \frac{1}{3}\big[(-3)(-1) + 0\big] = 1$.
- $n = 4$: $g_4 = \frac{1}{4}\left[\left(\frac{3}{2}(1) - 4\right)(2) g_3 + \left(\frac{3}{2}(2) - 4\right)(-1) g_2\right] = \frac{1}{4}\big[(-5)(1) + (1)(-1)\big] = -\frac{3}{2}$.
- **Verification**: $\left(1 + x - x^2 + x^3 - \frac{3}{2}x^4\right)^2 = 1 + 2x + (1 - 2)x^2 + (2 - 2)x^3 + (-3 + 2 + 1)x^4 + O(x^5) = 1 + 2x - x^2 + O(x^5)$.

#### Hand-Checkable Trace 3: Sparse Exponential $G(x) = \exp(x + 2x^3) \bmod x^5$
Here $P(x) = x + 2x^3$ has $c_0 = 0$ and two non-zero terms: $(d_1, c_1) = (1, 1)$ and $(d_2, c_2) = (3, 2)$. Using $g_0 = 1$ and $g_n = \frac{1}{n} \sum_{j=1}^2 d_j c_j g_{n - d_j}$:
- $n = 1$: $g_1 = \frac{1}{1}\big(1 \cdot 1 \cdot g_0\big) = 1$.
- $n = 2$: $g_2 = \frac{1}{2}\big(1 \cdot 1 \cdot g_1\big) = \frac{1}{2}$.
- $n = 3$: $g_3 = \frac{1}{3}\big(1 \cdot 1 \cdot g_2 + 3 \cdot 2 \cdot g_0\big) = \frac{1}{3}\left(\frac{1}{2} + 6\right) = \frac{13}{6}$.
- $n = 4$: $g_4 = \frac{1}{4}\big(1 \cdot 1 \cdot g_3 + 3 \cdot 2 \cdot g_1\big) = \frac{1}{4}\left(\frac{13}{6} + 6\right) = \frac{49}{24}$.
- **Verification**: $\exp(x)\exp(2x^3) = \left(1 + x + \frac{1}{2}x^2 + \frac{1}{6}x^3 + \frac{1}{24}x^4\right)(1 + 2x^3) + O(x^5) = 1 + x + \frac{1}{2}x^2 + \frac{13}{6}x^3 + \frac{49}{24}x^4 + O(x^5)$.

---

### 4.3 Critical Edge Cases: The 3-Way Modular Reduction Trap & Coupled Sparse Composition

#### 1. The 3-Way Modular Reduction Trap for Huge or Rational Exponents in `sparse_pow`
Suppose $P(x) = x^v \widetilde{P}(x)$ has lowest non-zero term $c_1 x^v$ ($v = \operatorname{val}(P) \ge 0, c_1 \neq 0$):
- **Case A (Huge Integer Exponent $\alpha \ge p$)**:
  $$P(x)^\alpha = x^{v \cdot \alpha} \cdot c_1^{\alpha} \cdot \left( \frac{\widetilde{P}(x)}{c_1} \right)^\alpha$$
  Here $\alpha$ plays **three completely different mathematical roles** and must be reduced modulo three different moduli:
  1. **Degree Shift $v \cdot \alpha$**: $\alpha$ is a **true non-negative integer** (do **not** reduce modulo $p$ or $p-1$!). Use `__int128_t` to check if $v > 0$ and $v \cdot \alpha \ge N$ (if so, return the zero polynomial immediately!).
  2. **Leading Scalar Power $c_1^\alpha \bmod p$**: By Fermat's Little Theorem, reduce $\alpha_{\text{exp}} = \alpha \bmod (p - 1)$.
  3. **Differential Recurrence Multiplier $((\alpha + 1) d_j - n) \bmod p$**: Inside the ODE $P G' = \alpha P' G$, $\alpha$ comes from differentiating $x^\alpha \mapsto \alpha x^{\alpha-1}$, so reduce $\alpha_{\text{ode}} = \alpha \bmod p$!
- **Case B (Rational Exponent $\alpha = a/b \in \mathbb{Q}$ with $\gcd(a, b) = 1, b > 0$)**:
  If $v = \operatorname{val}(P) > 0$, then $P(x)^{a/b} = x^{v a / b} c_1^{a/b} (\widetilde{P}(x)/c_1)^{a/b}$ is a valid formal power series in $\mathbb{F}_p[[x]]$ **if and only if** $b \mid (v \cdot a)$ in $\mathbb{Z}$ **and** $c_1$ has a $b$-th root in $\mathbb{F}_p$.

#### 2. Coupled $r$-State First-Order Sparse ODE System for $H(x) = F(P(x))$
What if $F(y)$ is D-finite of order $r \ge 2$ (satisfying $F^{(r)}(y) = \sum_{i=0}^{r-1} a_i(y) F^{(i)}(y)$) and $P(x)$ is $K$-sparse with $P(0) = 0$?
> **Cohort 2 Breakthrough**: Instead of forming a single order-$r$ ODE for $H(x) = F(P(x))$ (which introduces denominators $P'(x)$ when $\operatorname{val}(P') \ge 1$), define the **$r$ coupled intermediate series**:
> $$H_0(x) = F(P(x)), \quad H_1(x) = F'(P(x)), \quad \dots, \quad H_{r-1}(x) = F^{(r-1)}(P(x))$$
> By the chain rule, $H_i'(x) = P'(x) H_{i+1}(x)$ for $0 \le i \le r-2$, and $H_{r-1}'(x) = P'(x) \sum_{i=0}^{r-1} a_i(P(x)) H_i(x)$. Since $P'(x)$ is $K$-sparse, advancing $H_0, \dots, H_{r-1}$ simultaneously term-by-term for $n = 1 \dots N-1$ never divides by $P'(x)$ and runs in **$O(r \cdot N \cdot K)$** time!

---

### 4.4 Unified Production C++ `SparseFPS` Namespace

```cpp
namespace SparseFPS {
    using Poly = vector<long long>;
    struct Term { int deg; long long coeff; };

    vector<Term> extract_sparse(const Poly& P, int N) {
        vector<Term> sp;
        for (int i = 0; i < (int)P.size() && i < N; ++i)
            if (P[i] % MOD != 0) sp.push_back({i, (P[i] % MOD + MOD) % MOD});
        return sp;
    }

    vector<int> get_inv(int N) {
        vector<int> inv(max(N + 1, 2), 1);
        for (int i = 2; i <= N; ++i)
            inv[i] = 1LL * (MOD - MOD / i) * inv[MOD % i] % MOD;
        return inv;
    }

    // 1. In-Place Sparse Division: returns G = A / P mod x^N in O(N * K)
    Poly div(Poly A, const Poly& P, int N) {
        A.resize(N, 0);
        auto sp = extract_sparse(P, N);
        assert(!sp.empty() && sp[0].deg == 0 && "P(0) must be non-zero!");
        long long inv_p0 = modInverse(sp[0].coeff);
        for (int n = 0; n < N; ++n) {
            long long sum = 0;
            for (size_t j = 1; j < sp.size(); ++j) {
                if (sp[j].deg > n) break;
                sum = (sum + sp[j].coeff * A[n - sp[j].deg]) % MOD;
            }
            A[n] = (A[n] - sum + MOD) % MOD * inv_p0 % MOD;
        }
        return A;
    }

    // 2. Sparse Inverse: G = 1 / P mod x^N in O(N * K)
    Poly inv(const Poly& P, int N) {
        Poly A(N, 0);
        if (N > 0) A[0] = 1;
        return div(move(A), P, N);
    }

    // 3. Sparse Logarithm: G = ln(P) mod x^N in O(N * K), requires P[0] == 1
    Poly ln(const Poly& P, int N) {
        auto sp = extract_sparse(P, N);
        assert(!sp.empty() && sp[0].deg == 0 && sp[0].coeff == 1);
        auto inv_int = get_inv(N);
        Poly G(N, 0);
        for (int n = 1; n < N; ++n) {
            long long pn = (n < (int)P.size()) ? P[n] : 0;
            long long sum = 1LL * n * pn % MOD;
            for (size_t j = 1; j < sp.size(); ++j) {
                if (sp[j].deg >= n) break;
                int d = sp[j].deg;
                sum = (sum - 1LL * (n - d) * sp[j].coeff % MOD * G[n - d]) % MOD;
            }
            if (sum < 0) sum += MOD;
            G[n] = sum * inv_int[n] % MOD;
        }
        return G;
    }

    // 4. Sparse Exponential: G = exp(P) mod x^N in O(N * K), requires P[0] == 0
    Poly exp(const Poly& P, int N) {
        auto sp = extract_sparse(P, N);
        assert(sp.empty() || sp[0].deg > 0);
        auto inv_int = get_inv(N);
        Poly G(N, 0);
        if (N > 0) G[0] = 1;
        for (int n = 1; n < N; ++n) {
            long long sum = 0;
            for (const auto& t : sp) {
                if (t.deg > n) break;
                sum = (sum + 1LL * t.deg * t.coeff % MOD * G[n - t.deg]) % MOD;
            }
            G[n] = sum * inv_int[n] % MOD;
        }
        return G;
    }

    // 5. Sparse Power with 3-Way Modular Reduction Guard: G = P^alpha mod x^N in O(N * K)
    // alpha_shift: true integer exponent for valuation shift v * alpha_shift (requires v == 0 if alpha_shift < 0)
    // alpha_mod_p: alpha mod MOD (for ODE multiplier)
    // alpha_mod_phi: alpha mod (MOD - 1) (for leading scalar power c_1^alpha)
    Poly pow_general(const Poly& P, __int128 alpha_shift, long long alpha_mod_p, long long alpha_mod_phi, int N) {
        if (alpha_shift == 0 && alpha_mod_p == 0 && alpha_mod_phi == 0) {
            Poly G(N, 0);
            if (N > 0) G[0] = 1;
            return G;
        }
        auto sp = extract_sparse(P, N);
        if (sp.empty()) return Poly(N, 0);

        int v = sp[0].deg;
        if (v > 0) {
            assert(alpha_shift >= 0); // Negative powers of x^v are not formal power series
            if (alpha_shift >= (N + v - 1) / v) return Poly(N, 0);
        }
        int shift = (int)(alpha_shift * v);
        int M = N - shift;

        long long c1 = sp[0].coeff;
        long long inv_c1 = modInverse(c1);
        for (auto& t : sp) {
            t.deg -= v;
            t.coeff = t.coeff * inv_c1 % MOD;
        }

        auto inv_int = get_inv(M);
        Poly G(M, 0);
        long long exp_phi = (alpha_mod_phi % (MOD - 1) + (MOD - 1)) % (MOD - 1);
        G[0] = power(c1, exp_phi);
        long long alpha_norm = (alpha_mod_p % MOD + MOD) % MOD;
        long long alpha_plus_1 = (alpha_norm + 1) % MOD;

        for (int n = 1; n < M; ++n) {
            long long sum = 0;
            for (size_t j = 1; j < sp.size(); ++j) {
                int d = sp[j].deg;
                if (d > n) break;
                long long weight = (alpha_plus_1 * d - n) % MOD;
                if (weight < 0) weight += MOD;
                sum = (sum + weight * sp[j].coeff % MOD * G[n - d]) % MOD;
            }
            G[n] = sum * inv_int[n] % MOD;
        }

        Poly res(N, 0);
        for (int i = 0; i < M; ++i) res[i + shift] = G[i];
        return res;
    }

    Poly pow(const Poly& P, long long k, int N) {
        long long k_mod_p = (k % MOD + MOD) % MOD;
        long long k_mod_phi = (k % (MOD - 1) + (MOD - 1)) % (MOD - 1);
        return pow_general(P, k, k_mod_p, k_mod_phi, N);
    }

    // 6. Sparse Square Root: G = sqrt(P) mod x^N in O(N * K)
    // Requires valuation v = ord(P) to be even, and sqrt_c1^2 == c_1 (mod MOD)
    Poly sqrt(const Poly& P, int N, long long sqrt_c1 = 1) {
        auto sp = extract_sparse(P, N);
        if (sp.empty()) return Poly(N, 0);

        int v = sp[0].deg;
        assert(v % 2 == 0);
        int shift = v / 2;
        if (shift >= N) return Poly(N, 0);
        int M = N - shift;

        long long c1 = sp[0].coeff;
        assert(sqrt_c1 * sqrt_c1 % MOD == c1);
        long long inv_c1 = modInverse(c1);
        for (auto& t : sp) {
            t.deg -= v;
            t.coeff = t.coeff * inv_c1 % MOD;
        }

        auto inv_int = get_inv(M);
        Poly G(M, 0);
        G[0] = sqrt_c1;
        long long alpha_plus_1 = (MOD + 1) / 2 + 1; // alpha = 1/2 => alpha + 1 = 3/2 mod MOD

        for (int n = 1; n < M; ++n) {
            long long sum = 0;
            for (size_t j = 1; j < sp.size(); ++j) {
                int d = sp[j].deg;
                if (d > n) break;
                long long weight = (alpha_plus_1 * d - n) % MOD;
                if (weight < 0) weight += MOD;
                sum = (sum + weight * sp[j].coeff % MOD * G[n - d]) % MOD;
            }
            G[n] = sum * inv_int[n] % MOD;
        }

        Poly res(N, 0);
        for (int i = 0; i < M; ++i) res[i + shift] = G[i];
        return res;
    }
}
```

---

## 5. Iteration 44 / 96: Euler's Homogeneous PDE, Bivariate Diagonals & Creative Telescoping by Hand

### 5.1 Bivariate Partial Differential Equations & Cross-Partial Elimination

Given a bivariate formal power series $F(x, y) = \sum_{n, k \ge 0} f_{n, k} x^n y^k$, the partial Euler operators $\vartheta_x = x \frac{\partial}{\partial x}$ and $\vartheta_y = y \frac{\partial}{\partial y}$ act on monomials by:
$$\vartheta_x (x^n y^k) = n x^n y^k, \qquad \vartheta_y (x^n y^k) = k x^n y^k, \qquad (\vartheta_x + \vartheta_y)(x^n y^k) = (n + k) x^n y^k$$
1. **Euler's Homogeneous Function Theorem**: $F(x, y)$ is homogeneous of total degree $d$ ($F(tx, ty) = t^d F(x, y)$) if and only if $(\vartheta_x + \vartheta_y) F(x, y) = d \cdot F(x, y)$. More generally, for weighted homogeneity $F(t^a x, t^b y) = t^d F(x, y)$, differentiating with respect to $t$ at $t = 1$ yields $(a \vartheta_x + b \vartheta_y) F = d \cdot F$.
2. **Cross-Partial Elimination for Bivariate Powers $F(x, y) = A(x, y)^\alpha$**:
   Since $\frac{\partial F}{\partial x} = \alpha A^{\alpha - 1} \frac{\partial A}{\partial x}$ and $\frac{\partial F}{\partial y} = \alpha A^{\alpha - 1} \frac{\partial A}{\partial y}$, we have the coupled first-order PDE system:
   $$A(x, y) \frac{\partial F}{\partial x} = \alpha \frac{\partial A}{\partial x} F(x, y), \qquad A(x, y) \frac{\partial F}{\partial y} = \alpha \frac{\partial A}{\partial y} F(x, y)$$
   Eliminating $\alpha A^{\alpha - 1} F$ between the two equations produces the **exponent-independent cross-partial PDE**:
   $$\frac{\partial A}{\partial y} \frac{\partial F}{\partial x} - \frac{\partial A}{\partial x} \frac{\partial F}{\partial y} = 0$$
   When extracting a single row $G_n(y) = [x^n] A(x, y)^\alpha$ (for instance, in bivariate grid/grouping problems like CF 755G), substituting $F(x, y) = \sum_{n \ge 0} G_n(y) x^n$ into $A \frac{\partial F}{\partial y} = \alpha \frac{\partial A}{\partial y} F$ and $A \frac{\partial F}{\partial x} = \alpha \frac{\partial A}{\partial x} F$ allows us to eliminate $G_{n-1}(y), G_{n-2}(y)$ and obtain a **univariate D-finite ODE in $y$** for $G_n(y)$ alone!

---

### 5.2 Four Engines for Bivariate Diagonals & Binomial-Product Sums

Suppose we need to compute $S_n = \sum_{k=0}^n \binom{n}{k} \binom{n+k}{k} c^k$, $a_n = [x^n] P(x)^n$, or $\operatorname{Diag}(F)(t) = \sum_{n \ge 0} f_{n, n} t^n = [u^0] F(u, t/u)$ for $n = 0 \dots N$ in **$O(N)$** time. Across the three cohorts, four complementary engines were established:

#### Engine 1: Cauchy Residue / Algebraic Diagonal Method (`[u^0] F(u, t/u)`)
For a rational bivariate series $F(x, y) = \frac{P(x, y)}{Q(x, y)}$ with $Q(0, 0) \neq 0$, the diagonal equals the contour residue:
$$\operatorname{Diag}(F)(t) = [u^0] F\!\left(u, \frac{t}{u}\right) = \frac{1}{2\pi i} \oint_{|u|=\varepsilon} \frac{P(u, t/u)}{u \, Q(u, t/u)} \, du = \sum_{\substack{u_i(t) \to 0 \\ \text{as } t \to 0}} \operatorname{Res}_{u = u_i(t)} \frac{P(u, t/u)}{u \, Q(u, t/u)}$$
- **Theorem (Furstenberg 1967)**: The diagonal of any bivariate rational function in $2$ variables is **algebraic** (and in $\ge 3$ variables is **D-finite** / Lipshitz 1988).
- **Universal Quadratic Diagonal Formula**: For any quadratic polynomial $P(x) = p_0 + p_1 x + p_2 x^2$, the diagonal $a_n = [x^n] P(x)^n$ has the exact closed-form algebraic generating function:
  $$\sum_{n=0}^{\infty} \left([x^n](p_0 + p_1 x + p_2 x^2)^n\right) z^n = [u^0] \frac{1}{1 - z (p_0 u^{-1} + p_1 + p_2 u)} = \frac{1}{\sqrt{(1 - p_1 z)^2 - 4 p_0 p_2 z^2}}$$
  Applying Recipe A from Section 2.2 yields the universal 3-term P-recursive relation:
  $$n a_n = p_1 (2n - 1) a_{n-1} - (p_1^2 - 4 p_0 p_2)(n - 1) a_{n-2} \qquad (n \ge 2)$$
- **Lagrange Diagonal Formula for $a_n = [x^n](1 + ax)^n(1 + bx)^n$**: Setting $\phi(x) = (1+ax)(1+bx) = 1 + (a+b)x + ab x^2$ gives:
  $$\sum_{n=0}^{\infty} a_n z^n = \frac{1}{\sqrt{1 - 2(a+b)z + (a-b)^2 z^2}} \implies n a_n = (a+b)(2n-1) a_{n-1} - (a-b)^2 (n-1) a_{n-2}$$

#### Engine 2: Zeilberger's Creative Telescoping by Hand (Rational Certificate Method)
> **Diagnostic Signal**: Given $S(n) = \sum_{k} T(n, k)$ where $T(n, k)$ is hypergeometric in both $n$ and $k$ (meaning $T(n+1, k)/T(n, k)$ and $T(n, k+1)/T(n, k)$ are rational functions of $n, k$), we seek polynomial coefficients $p_0(n), \dots, p_r(n)$ and a **rational certificate** $R(n, k) \in \mathbb{Q}(n, k)$ such that $G(n, k) = R(n, k) T(n, k)$ satisfies the telescoping identity:
> $$\sum_{j=0}^{r} p_j(n) T(n + j, k) = G(n, k + 1) - G(n, k)$$
> Summing over all $k \in \mathbb{Z}$ where $T(n, k)$ has natural compact support ($G(n, -\infty) = G(n, +\infty) = 0$) cancels the right-hand side to $0$:
> $$\sum_{j=0}^{r} p_j(n) S(n + j) = 0$$

- **Complete Worked Derivation by Hand on $S(n) = \sum_{k=0}^{n} \binom{n}{k} \binom{n+k}{k} c^k$**:
  1. Write the shift ratios of $T(n, k) = \frac{(n+k)!}{k!^2 (n-k)!} c^k$ relative to $T(n, k)$:
     $$\frac{T(n+1, k)}{T(n, k)} = \frac{n + k + 1}{n + 1 - k}, \qquad \frac{T(n-1, k)}{T(n, k)} = \frac{n - k}{n + k}, \qquad \frac{T(n, k-1)}{T(n, k)} = \frac{k^2}{c(n + k)(n - k + 1)}$$
  2. Notice that the denominator $(n+1-k)(n+k)$ in $T(n, k-1)/T(n, k)$ matches the product of the denominators of $T(n+1, k)/T(n, k)$ and $T(n-1, k)/T(n, k)$! This immediately tells us to choose the certificate $G(n, k) = 4c \, T(n, k-1)$, i.e.:
     $$R(n, k) = \frac{4 k^2}{(n + 1 - k)(n + k)} \implies G(n, k + 1) = 4 c \, T(n, k)$$
  3. Dividing the ansatz $p_1(n) T(n+1, k) + p_0(n) T(n, k) + p_{-1}(n) T(n-1, k) = G(n, k+1) - G(n, k)$ by $T(n, k)$ gives the pure rational-function identity in $k$:
     $$p_1(n) \frac{n + k + 1}{n + 1 - k} + p_0(n) + p_{-1}(n) \frac{n - k}{n + k} = 4 c - \frac{4 k^2}{(n + 1 - k)(n + k)}$$
  4. Clearing the common denominator $(n+1-k)(n+k)$ and matching coefficients of $k^2, k^1, k^0$ yields:
     $$p_1(n) = n + 1, \qquad p_0(n) = -(2c + 1)(2n + 1), \qquad p_{-1}(n) = n$$
  5. Summing over $k \in \mathbb{Z}$ gives the 3-term P-recursive relation for **arbitrary parameter $c$**:
     $$(n + 1) S(n + 1) - (2c + 1)(2n + 1) S(n) + n S(n - 1) = 0$$

#### Engine 3: EI's Direct Differential-Residue Method (`载谭 Binomial Sums`)
> **Cohort 2 Breakthrough**: Instead of contour integrals or guessing a rational certificate $R(n, k)$, express the binomial sum as a 1D formal residue $S_n = [x^{-1}] W_n(x)$ and use the fundamental algebraic identity that **the formal residue $[x^{-1}]$ of any formal derivative is identically zero**:
> $$[x^{-1}] \frac{d}{dx} \Big( P(x) Q(x)^n \Big) = 0$$

- **Step 1: Three Exact Single-Variable Coefficient Representations of $S_n = \sum_{k=0}^n \binom{n}{k}\binom{n+k}{k} c^k$**:
  Depending on how we encode $\binom{n+k}{k}$ as a 1D power series coefficient, we obtain three equivalent single-variable forms:
  1. **Using $\binom{n+k}{k} = \binom{n+k}{n} = [x^n](1 - x)^{-(k+1)}$**:
     $$S_n = \sum_{k=0}^n \binom{n}{k} c^k [x^n](1 - x)^{-(k+1)} = [x^n] \frac{1}{1 - x} \left(1 + \frac{c}{1 - x}\right)^n = [x^n] \frac{(1 + c - x)^n}{(1 - x)^{n+1}}.$$
     *(Verification at $n = 1$: $[x^1]\frac{1 + c - x}{(1 - x)^2} = [x^1](1 + c - x)(1 + 2x + O(x^2)) = 2(1 + c) - 1 = 2c + 1 = \binom{1}{0}\binom{1}{0} + \binom{1}{1}\binom{2}{1}c$.)*
  2. **Using $\binom{n}{k} = [x^{n-k}](1 + x)^n$ and $\binom{n+k}{k} = [x^k](1 - x)^{-(n+1)}$**:
     $$S_n = \sum_{k=0}^n [x^{n-k}](1 + x)^n \cdot [x^k](1 - cx)^{-(n+1)} = [x^n] \frac{(1 + x)^n}{(1 - cx)^{n+1}} = [x^{-1}] \frac{(1 + x)^n}{x^{n+1}(1 - cx)^{n+1}}.$$
  3. **Using Laurent Trinomial Symmetry $\binom{n+k}{k} = \binom{n+k}{n} = [x^n](1 + x)^{n+k}$**:
     $$S_n = \sum_{k=0}^n \binom{n}{k} c^k [x^n](1 + x)^{n+k} = [x^n] (1 + x)^n \big(1 + c(1 + x)\big)^n = [x^{-1}] x^{-1} Q(x)^n,$$
     where $Q(x) = \frac{(1 + x)(1 + c + cx)}{x} = A x^{-1} + B + C x$ is a Laurent trinomial with $A = 1 + c$, $B = 2c + 1$, and $C = c$.

- **Step 2: Exact 3-Line Differential-Residue Proof via Laurent Trinomial**:
  1. Define $W_n(x) = x^{-1} Q(x)^n$, so $S_n = [x^{-1}] W_n(x)$. Observe that $Q(x) - B = C x + A x^{-1}$ and $x Q'(x) = C x - A x^{-1}$. These satisfy two elementary identities:
     $$\frac{d}{dx}\big[x Q'(x)\big] = C + A x^{-2} = x^{-1}\big(Q(x) - B\big), \qquad \big(x Q'(x)\big)^2 = (C x + A x^{-1})^2 - 4AC = Q(x)^2 - 2B Q(x) + (B^2 - 4AC).$$
  2. Differentiate the single product $x Q'(x) Q(x)^n$ with respect to $x$:
     $$\begin{aligned}
     \frac{d}{dx}\Big[x Q'(x) Q(x)^n\Big] &= \frac{d}{dx}\big[x Q'(x)\big] Q(x)^n + n \big(x Q'(x)\big) Q'(x) Q(x)^{n-1} \\
     &= x^{-1}\big(Q(x) - B\big) Q(x)^n + n x^{-1}\big(x Q'(x)\big)^2 Q(x)^{n-1} \\
     &= (n + 1) W_{n+1}(x) - (2n + 1) B W_n(x) + n(B^2 - 4AC) W_{n-1}(x).
     \end{aligned}$$
  3. Since $[x^{-1}] \frac{d}{dx}[\dots] = 0$ and $B^2 - 4AC = (2c + 1)^2 - 4(1 + c)c = 1$, extracting $[x^{-1}]$ immediately yields:
     $$(n + 1) S_{n+1} - (2c + 1)(2n + 1) S_n + n S_{n-1} = 0$$
     without ever introducing a second variable $y$ or solving a quadratic root! *(Bonus: this exact same 3-line identity proves the universal 3-term recurrence $(n+1)a_{n+1} = (2n+1)B a_n - n(B^2 - 4AC)a_{n-1}$ for any central trinomial power $a_n = [x^n](A + Bx + Cx^2)^n$.)*

- **Hand-Checkable Numerical Trace ($c = 2, n \le 4$)**:
  For $c = 2$, $2c + 1 = 5$, so the recurrence is $(n + 1) S_{n+1} = 5(2n + 1) S_n - n S_{n-1}$ with $S_0 = 1$:
  - $n = 0$: $S_0 = \binom{0}{0}\binom{0}{0} 2^0 = 1$.
  - $n = 1$: $1 \cdot S_1 = 5(1) S_0 - 0 = 5$ *(Direct check: $\binom{1}{0}\binom{1}{0} + \binom{1}{1}\binom{2}{1} 2^1 = 1 + 4 = 5$)*.
  - $n = 2$: $2 S_2 = 5(3) S_1 - 1 \cdot S_0 = 75 - 1 = 74 \implies S_2 = 37$ *(Direct check: $1 + 6(2) + 6(4) = 37$)*.
  - $n = 3$: $3 S_3 = 5(5) S_2 - 2 S_1 = 25(37) - 10 = 915 \implies S_3 = 305$ *(Direct check: $1 + 12(2) + 30(4) + 20(8) = 305$)*.
  - $n = 4$: $4 S_4 = 5(7) S_3 - 3 S_2 = 35(305) - 111 = 10564 \implies S_4 = 2641$.

#### Engine 4: Hypergeometric Term Ratio $\to$ Euler Operator ODE $(Q(\vartheta) - x P(\vartheta)) F(x) = 0$
Whenever $F(x) = \sum_{k \ge 0} c_k x^k$ has a single-sum hypergeometric ratio $\frac{c_{k+1}}{c_k} = \frac{P(k)}{Q(k+1)}$ with $Q(0) = 0$:
$$Q(k) c_k x^k = x P(k - 1) c_{k-1} x^{k-1} \implies \left( Q(\vartheta) - x P(\vartheta) \right) F(x) = Q(0) c_0$$

#### Generalization to Two-Parameter Binomial Products $S_n(a, b) = [x^n](1 + ax)^n(1 + bx)^n$
For any constants $a, b \in \mathbb{F}_p$, consider the general product diagonal:
$$S_n(a, b) = [x^n](1 + ax)^n(1 + bx)^n = \sum_{k=0}^n \binom{n}{k}^2 a^k b^{n-k}.$$
- **By Engine 1 (Diagonal Principle)**: Write $S_n(a, b) = [x^n y^n] \frac{1}{1 - y(1 + ax)(1 + bx)}$. Setting $s = xy$ gives $Q(y) = y^2 - \big(1 - (a+b)s\big)y + ab s^2$, with discriminant $\Delta(s) = \big(1 - (a+b)s\big)^2 - 4ab s^2 = 1 - 2(a+b)s + (a-b)^2 s^2$. Thus $D(s) = \sum_{n \ge 0} S_n(a, b) s^n = \Delta(s)^{-1/2}$ satisfies $\big(1 - 2(a+b)s + (a-b)^2 s^2\big) D'(s) = \big((a+b) - (a-b)^2 s\big) D(s)$.
- **By Engine 3 (Laurent Trinomial)**: Here $Q(x) = x^{-1}(1 + ax)(1 + bx) = x^{-1} + (a + b) + ab x$, so $A = 1, B = a + b, C = ab$, and $B^2 - 4AC = (a - b)^2$. Both engines immediately yield the universal 3-term recurrence:
  $$(n + 1) S_{n+1}(a, b) = (2n + 1)(a + b) S_n(a, b) - n (a - b)^2 S_{n-1}(a, b), \qquad S_0(a, b) = 1, \quad S_1(a, b) = a + b.$$
  Setting $(a, b) = (2, 1)$ recovers the central Delannoy recurrence $(n+1)D_{n+1} = 3(2n+1)D_n - n D_{n-1}$; setting $(a, b) = (c, 1)$ recovers $\sum_{k=0}^n \binom{n}{k}^2 c^k$; setting $(a, b) = (1, 1)$ recovers $S_n(1, 1) = \binom{2n}{n}$.

#### Master Binomial Sum & Diagonal ODE Reference Table

| Sequence / Binomial Sum $S_n$ | Bivariate Denominator $Q(x, y)$ | Closed-Form OGF $F(s) = \sum_{n \ge 0} S_n s^n$ | Exact $O(1)$-Step P-Recursive Recurrence |
| :--- | :--- | :--- | :--- |
| Central Binomial $\binom{2n}{n} = \sum_k \binom{n}{k}^2$ | $1 - x - y$ | $\frac{1}{\sqrt{1 - 4s}}$ | $(n+1) S_{n+1} = 2(2n+1) S_n$ |
| Catalan $C_n = \frac{1}{n+1}\binom{2n}{n}$ | — | $\frac{1 - \sqrt{1 - 4s}}{2s}$ | $(n+2) C_{n+1} = 2(2n+1) C_n$ |
| Motzkin $M_n = \sum_k \binom{n}{2k} C_k$ | — | $\frac{1 - s - \sqrt{1 - 2s - 3s^2}}{2s^2}$ | $(n+3) M_{n+1} = (2n+3) M_n + 3n M_{n-1}$ |
| Central Trinomial $[x^n](p_0 + p_1 x + p_2 x^2)^n$ | $1 - y(p_0 + p_1 x + p_2 x^2)$ | $\frac{1}{\sqrt{1 - 2p_1 s + (p_1^2 - 4p_0 p_2)s^2}}$ | $(n+1) S_{n+1} = (2n+1) p_1 S_n - n(p_1^2 - 4p_0 p_2) S_{n-1}$ |
| Central Delannoy $D_n = \sum_k \binom{n}{k}\binom{n+k}{k}$ | $1 - x - y - xy$ | $\frac{1}{\sqrt{1 - 6s + s^2}}$ | $(n+1) D_{n+1} = 3(2n+1) D_n - n D_{n-1}$ |
| Weighted Square $\sum_{k=0}^n \binom{n}{k}^2 c^k$ | $1 - x - cy - (1-c)xy$ | $\frac{1}{\sqrt{1 - 2(1+c)s + (1-c)^2 s^2}}$ | $(n+1) S_{n+1} = (1+c)(2n+1) S_n - (1-c)^2 n S_{n-1}$ |
| $c$-Delannoy $\sum_{k=0}^n \binom{n}{k}\binom{n+k}{k} c^k$ | $1 - x - y - (2c-1)xy$ | $\frac{1}{\sqrt{1 - 2(2c+1)s + s^2}}$ | $(n+1) S_{n+1} = (2c+1)(2n+1) S_n - n S_{n-1}$ |
| Large Schröder $\sum_{k=0}^n \binom{n+k}{2k} C_k c^k$ | $1 - x - y - (2c-1)xy$ (shifted) | $\frac{1 - (2c-1)s - \sqrt{1 - 2(2c+1)s + s^2}}{2cs}$ | $(n+2) S_{n+1} = (2c+1)(2n+1) S_n - (n-1) S_{n-1}$ |
| Narayana Sum $\sum_{k=1}^n \frac{1}{n}\binom{n}{k}\binom{n}{k-1} c^k$ | — | $\frac{1 - (1+c)s - \sqrt{1 - 2(1+c)s + (1-c)^2 s^2}}{2s}$ | $(n+2) S_{n+1} = (1+c)(2n+1) S_n - (1-c)^2 (n-1) S_{n-1}$ |
| Even-Index $\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k}\binom{2k}{k} c^k$ | $1 - y(1 + 2x + (1-4c)x^2)$ | $\frac{1}{\sqrt{1 - 2s + (1 - 4c)s^2}}$ | $(n+1) S_{n+1} = (2n+1) S_n - (1-4c) n S_{n-1}$ |
| Franel $\sum_{k=0}^n \binom{n}{k}^3$ | 3D Diagonal | Transcendental D-Finite (Order 2) | $(n+1)^2 S_{n+1} = (7n^2 + 7n + 2) S_n + 8 n^2 S_{n-1}$ |
| Apéry $\sum_{k=0}^n \binom{n}{k}^2 \binom{n+k}{k}^2$ | 4D Diagonal | Transcendental D-Finite (Order 2) | $(n+1)^3 S_{n+1} = (2n+1)(17n^2 + 17n + 5) S_n - n^3 S_{n-1}$ |

- **Boundary Failure Warning (Non-Natural Support)**: If the summation upper limit $m < n$ cuts through the support where $T(n, m+1) \neq 0$ (e.g. $S_m(n) = \sum_{k=0}^m \binom{n}{k}$), creative telescoping $T(n+1, k) - 2 T(n, k) = G(n, k+1) - G(n, k)$ with $G(n, k) = -\binom{n}{k-1}$ does **not** sum to $0$—it leaves the boundary term $S_m(n+1) - 2 S_m(n) = G(n, m+1) - G(n, 0) = -\binom{n}{m}$!

---

## 6. Iteration 45 / 97: Offline CDQ NTT vs. van der Hoeven's Relaxed / Online Convolution

### 6.1 Semi-Online Offline CDQ Divide-and-Conquer NTT ($f_n = \sum_{i=0}^{n-1} f_i g_{n-i}$)

When the multiplier series $g_1, \dots, g_N$ is **known offline in advance**, we solve $f_n = \phi_n\!\left(\sum_{i=0}^{n-1} f_i g_{n-i}\right)$ via `cdq(l, r)` on $[0, N]$:
1. If $l == r$: finalize $f_l = \phi_l(\text{acc}_l)$ and return.
2. Set $\text{mid} = \lfloor (l + r) / 2 \rfloor$ and recurse `cdq(l, mid)`.
3. Convolve $A[0 \dots \text{mid}-l] = f[l \dots \text{mid}]$ with $B[0 \dots r-l] = g[0 \dots r-l]$ using a single NTT of size $L = 2^{\lceil \log_2(r - l + \text{mid} - l + 1) \rceil}$, and add $[x^{k - l}](A \cdot B)$ to $\text{acc}_k$ for each $k \in [\text{mid} + 1, r]$.
4. Recurse `cdq(mid + 1, r)`.

- **Theorem (LCA Partition Invariant)**: *Every ordered pair $(i, n)$ with $0 \le i < n \le N$ is accumulated **exactly once**, at the unique recursion node $[l, r] = \operatorname{LCA}_{\text{CDQ}}(i, n)$ where $i \in [l, \text{mid}]$ and $n \in [\text{mid} + 1, r]$.*
  - *Proof*: Because $[l, r]$ partitions into disjoint halves $[l, \text{mid}]$ and $[\text{mid}+1, r]$ at every internal node until $l = r$, any two distinct indices $i < n$ are separated at a unique deepest node $[l, r]$ where $i \le \text{mid} < n$. At that node, the cross-convolution adds $f_i \cdot g_{n - i}$ to $\text{acc}_n$; at all ancestor nodes $i, n$ lie in the same half, and at all descendant nodes they lie in disjoint subtrees. $\blacksquare$

#### The Full-Online Offline-CDQ Asymmetry Bug at $l > 0$
What if **both** $a_i$ and $b_j$ are computed online on the fly (e.g. $c_n = \sum_{i=1}^{n-1} a_i b_{n-i}$ where $a_n, b_n$ both depend on $c_n$)?
- **Critical Bug**: If you only convolve $a[l \dots \text{mid}] \times b[l \dots \text{mid}]$ inside `cdq(l, r)`, you miss every pair $(i, j)$ where $i \in [l, \text{mid}]$ and $j < l$!
- **Exact Fix**: Inside `cdq(l, r)`:
  - When $l = 0$: both $i, j \in [0, \text{mid}]$, so convolve **$a[0 \dots \text{mid}] \times b[0 \dots \text{mid}]$** once.
  - When $l > 0$: one index lies in $[l, \text{mid}]$ and the other lies in $[0, r - l]$ (already finalized because $r - l \le \text{mid}$ holds whenever $l \ge \text{mid}/2$, or for power-of-2 midpoint blocks $r - l \le l$), so convolve **$a[l \dots \text{mid}] \times b[0 \dots r - l] + b[l \dots \text{mid}] \times a[0 \dots r - l]$**!

---

### 6.2 van der Hoeven's Full-Online (Relaxed) Convolution & Two Complementary Partition Proofs

When $a_0, b_0, a_1, b_1, \dots$ arrive **strictly online one step at a time** (and the caller must immediately receive $c_q = \sum_{i=0}^{q} a_i b_{q-i}$ before deciding $a_{q+1}, b_{q+1}$), offline CDQ cannot be invoked cleanly across multiple coupled series. Instead, we use **Joris van der Hoeven's Relaxed Convolution (1997 / 2002)**, which exists in two equivalent indexing conventions in competitive programming:

#### Convention A: 1-Indexed Interior L-Shaped Strip Partition (Pre-existing & Cohort 1)
To compute the interior sum $c_n^{\text{int}} = \sum_{i=1}^{n-1} a_i b_{n-i}$ at step $n \ge 2$ (handling the boundary $a_0 b_n + a_n b_0$ in $O(1)$ outside):
- **Theorem (L-Shaped Strip Partition)**: *The positive quadrant $\mathbb{Z}_{\ge 1} \times \mathbb{Z}_{\ge 1}$ is partitioned into disjoint L-shaped strips $S_{\text{lg}} = \{ (i, j) : \min(i, j) \in [2^{\text{lg}}, 2^{\text{lg}+1} - 1] \}$ for $\text{lg} \ge 0$. Within strip $S_{\text{lg}}$ (block size $d = 2^{\text{lg}}$), at each step $n = k \cdot d$ ($k \ge 2$) where $d \mid n$:*
  - *If $k = 2$ ($n = 2d$): convolve the diagonal square $A[d \dots 2d-1] \times B[d \dots 2d-1]$ (contributing to $c_{2d \dots 4d-2}$).*
  - *If $k \ge 3$ ($n = k d$): convolve the two symmetric wings $A[(k-1)d \dots kd-1] \times B[d \dots 2d-1] + B[(k-1)d \dots kd-1] \times A[d \dots 2d-1]$ (contributing to $c_{kd \dots (k+2)d-2}$).*
  - *Timeliness*: The earliest sum index touched at trigger $n = kd$ is $(k-1)d + d = kd = n$, and the latest source index read is $kd - 1 = n - 1$, which is already finalized!

#### Convention B: 0-Indexed Binary Prefix / `lowbit(q + 1)` Partition (Cohort 2 / Nyaan's Library)
To compute $c_q = \sum_{i=0}^{q} a_i b_{q-i}$ directly at 0-indexed step $q = 0, 1, 2, \dots$ upon receiving $(a_q, b_q)$:
- Let $m = q + 1$ and $d = \operatorname{lowbit}(m) = m \mathbin{\&} (-m) = 2^k$:
  - **Diagonal Case ($m = d$, i.e., $q + 1 = 2^k$ is a pure power of $2$)**: Convolve the single square block $A[0 \dots d-1] \times B[0 \dots d-1]$ of size $d \times d$, and add to $C[q \dots q + 2d - 2]$.
  - **Off-Diagonal Case ($m > d$, i.e., $q + 1 > \operatorname{lowbit}(q + 1)$)**: Convolve the two symmetric rectangular blocks $A[q - d + 1 \dots q] \times B[0 \dots d-1] + B[q - d + 1 \dots q] \times A[0 \dots d-1]$ of size $d \times d$, and add to $C[q \dots q + 2d - 2]$.
- **Theorem (Binary Prefix Completeness & Uniqueness)**: *Every ordered pair $(i, j) \in \mathbb{Z}_{\ge 0}^2$ is covered by **exactly one** block product, and that block product is executed at step $q \le i + j$ where $\max(i, j) \le q$ (causal readiness).*
  - *Proof*:
    1. **1-Based Dyadic L-Strip Schedule (Convention A)**: Shift to 1-based indices $I = i + 1 \ge 1$ and $J = j + 1 \ge 1$ (or for interior terms $i, j \ge 1$, take $I = i, J = j$). Every pair $(I, J) \in \mathbb{Z}_{\ge 1}^2$ has a unique largest power of two $d = 2^{\lfloor \log_2 \min(I, J) \rfloor} \le \min(I, J)$, so $\min(I, J) \in [d, 2d - 1]$. Meanwhile, $\max(I, J)$ falls into a unique block $[(k - 1)d, k d - 1]$ where $k = \lfloor \max(I, J) / d \rfloor + 1 \ge 2$.
       - When $k = 2$, both $I, J \in [d, 2d - 1]$, so $(I, J)$ is covered by the single diagonal square $A[d \dots 2d - 1] \times B[d \dots 2d - 1]$ at step $n = 2d$.
       - When $k \ge 3$, exactly one of $I, J$ lies in $[(k - 1)d, k d - 1]$ and the other lies in $[d, 2d - 1]$, so $(I, J)$ is covered by one of the two symmetric off-diagonal rectangles at step $n = k d$.
       - **Readiness ($\max(I, J) < n$)**: Since $\max(I, J) \le k d - 1 < k d = n$, both operands are already finalized before step $n$.
       - **Timeliness ($n \le I + J$)**: Since $\max(I, J) \ge (k - 1)d$ and $\min(I, J) \ge d$, we have $I + J \ge (k - 1)d + d = k d = n$, so the product is accumulated at or before step $I + J$.
    2. **0-Based Binary Prefix Decomposition (Convention B)**: Equivalently, in 0-indexed prefix convention (`lowbit(q + 1)`), if we trigger a block of size $d = 2^k$ whenever $2^k \mid (q + 1)$ (or for every $2^k \mid q$ up to $\operatorname{lowbit}(q)$), then for any target sum $n = i + j$ with binary expansion $n = \sum_{r=1}^m 2^{k_r}$ ($k_1 > k_2 > \dots > k_m$), the range $i \in [0, n]$ is partitioned into $m$ dyadic prefix intervals $I_r = [p_{r-1}, p_r - 1]$ of length $2^{k_r}$ (where $p_r = \sum_{s=1}^r 2^{k_s}$) plus the singleton $\{n\}$, each computed at step $q = p_r - 1$ using $A[p_{r-1} \dots p_r - 1] \times B[0 \dots 2^{k_r} - 1]$. Both schedules perform $O(N \log^2 N)$ total work with a $2\times$ constant-factor speedup when symmetric off-diagonal blocks are combined. $\blacksquare$

#### Side-by-Side Schedule Comparison: Convention A ($1$-Indexed Interior) vs. Convention B ($0$-Indexed `lowbit(q + 1)`)

| Step $q$ | $m = q+1$ | $d = \operatorname{lowbit}(m)$ | Convention B ($0$-Indexed Prefix Box) | Convention A ($1$-Indexed Strip Box at $n = q$) | Target Sum Indices Updated |
| :---: | :---: | :---: | :--- | :--- | :---: |
| $0$ | $1$ | $1$ | $A[0..0] \times B[0..0]$ ($m = d$) | Boundary $a_0 b_0$ | $C[0..0]$ |
| $1$ | $2$ | $2$ | $A[0..1] \times B[0..1]$ ($m = d$) | Boundary $a_0 b_1 + a_1 b_0$ | $C[1..3]$ |
| $2$ | $3$ | $1$ | $A[2..2]\times B[0..0] + B[2..2]\times A[0..0]$ | $d=1: A[1..1] \times B[1..1]$ | $C[2..2]$ |
| $3$ | $4$ | $4$ | $A[0..3] \times B[0..3]$ ($m = d$) | $d=1: A[2..2]\times B[1..1] + \text{sym}$ | $C[3..7]$ |
| $4$ | $5$ | $1$ | $A[4..4]\times B[0..0] + B[4..4]\times A[0..0]$ | $d=1: A[3..3]\times B[1..1] + \text{sym}$<br>$d=2: A[2..3]\times B[2..3]$ | $C[4..6]$ |
| $5$ | $6$ | $2$ | $A[4..5]\times B[0..1] + B[4..5]\times A[0..1]$ | $d=1: A[4..4]\times B[1..1] + \text{sym}$ | $C[5..7]$ |
| $6$ | $7$ | $1$ | $A[6..6]\times B[0..0] + B[6..6]\times A[0..0]$ | $d=1: A[5..5]\times B[1..1] + \text{sym}$<br>$d=2: A[4..5]\times B[2..3] + \text{sym}$ | $C[6..8]$ |
| $7$ | $8$ | $8$ | $A[0..7] \times B[0..7]$ ($m = d$) | $d=1: A[6..6]\times B[1..1] + \text{sym}$ | $C[7..15]$ |

#### How to Use 0-Indexed `RelaxedConvolution` for Self-Referential Equations ($a_q$ Depends on $c_q$)
> **Crucial Protocol**: In equations like Online Inverse ($F G = 1$), Online Exp ($F' = G' F$), or Pólya tree DP ($F = 1 + x F^3$), the new coefficient $a_q$ depends on the **interior convolution sum** $\sum_{i=1}^{q-1} a_i b_{q-i}$!
> Notice from the trace table above that at the **start** of step $q$ (before `rc.next(a_q, b_q)` is called), every pair $(i, j)$ with $i + j = q$ and $1 \le i, j \le q - 1$ has **already** been accumulated into `rc.C[q]` during steps $0 \dots q - 1$! Only the two boundary terms $a_0 b_q + a_q b_0$ are added during step $q$ itself.
> Therefore, for self-referential DP at step $q$:
> 1. Read the already-accumulated interior sum `long long interior = rc.get_interior(q);` (= `rc.C[q]`).
> 2. Solve for $a_q$ (and $b_q$) using `interior`.
> 3. Commit `(a_q, b_q)` by calling `rc.next(a_q, b_q)`!

---

### 6.3 Production C++ Template: Self-Referential 0-Indexed `RelaxedConvolution` with Small-Block $O(d^2)$ Fast Path

```cpp
// Self-contained Relaxed (Online) Convolution Engine (0-indexed Binary Prefix Schedule)
// Supports both standard online multiplication and self-referential online DP!
// Amortized Complexity: O(N log^2 N) time, O(N) space.
struct RelaxedConvolution {
    int q = 0;
    vector<long long> A, B, C;
    function<vector<long long>(const vector<long long>&, const vector<long long>&)> ntt_mul;

    RelaxedConvolution(int max_n, auto mul_fn) : ntt_mul(mul_fn) {
        A.reserve(max_n);
        B.reserve(max_n);
        C.assign(2 * max_n + 4, 0);
    }

    // Read the interior sum \sum_{i=1}^{q-1} A[i] * B[q - i] BEFORE calling next(a_q, b_q)
    long long get_interior() const {
        return C[q];
    }

    void add_conv(int a_l, int b_l, int d, int offset, bool double_wing) {
        if (d <= 16) { // Fast cache-friendly O(d^2) path for small blocks
            for (int i = 0; i < d; ++i) {
                long long ai = A[a_l + i], bi = B[a_l + i];
                for (int j = 0; j < d; ++j) {
                    long long ways = ai * B[b_l + j];
                    if (double_wing) ways += bi * A[b_l + j];
                    C[offset + i + j] = (C[offset + i + j] + ways) % MOD;
                }
            }
            return;
        }
        vector<long long> pA(A.begin() + a_l, A.begin() + a_l + d);
        vector<long long> pB(B.begin() + b_l, B.begin() + b_l + d);
        vector<long long> prod = ntt_mul(pA, pB);
        if (double_wing) {
            vector<long long> pA2(B.begin() + a_l, B.begin() + a_l + d);
            vector<long long> pB2(A.begin() + b_l, A.begin() + b_l + d);
            vector<long long> prod2 = ntt_mul(pA2, pB2);
            for (size_t i = 0; i < prod.size(); ++i)
                prod[i] = (prod[i] + prod2[i]) % MOD;
        }
        for (size_t i = 0; i < prod.size(); ++i) {
            C[offset + i] += prod[i];
            if (C[offset + i] >= MOD) C[offset + i] -= MOD;
        }
    }

    // Feed (a_q, b_q) at step q and return full c_q = \sum_{i=0}^q a_i * b_{q-i} mod MOD
    long long next(long long a_q, long long b_q) {
        A.push_back((a_q % MOD + MOD) % MOD);
        B.push_back((b_q % MOD + MOD) % MOD);
        if ((int)C.size() <= 2 * q + 4) C.resize(4 * q + 8, 0);

        int m = q + 1;
        int d = m & -m; // lowbit(q + 1)
        if (m == d) {
            add_conv(0, 0, d, q, false);
        } else {
            add_conv(q - d + 1, 0, d, q, true);
        }
        return C[q++];
    }
};
```

---

## 7. Master Curated Practice Problem Set (34 Standalone Problems Across 4 Tiers)

Every accepted problem from Cohort 1 and Cohort 2 (plus all unbundled mastery extensions = 34 distinct standalone contest problems) is preserved below with its complete self-contained mathematical statement, exact constraints, direct source URL, 3-tier progressive hints, and full algebraic derivation.

---

### Tier 1: Stepping Stone (`Easy` — 8 Problems)

#### Problem 1: Codeforces 1096G — Lucky Tickets
- **Source & Link**: Codeforces Educational Round 57 — [https://codeforces.com/problemset/problem/1096/G](https://codeforces.com/problemset/problem/1096/G) (Discovered by Cohort 2)
- **Difficulty Tier**: `Stepping Stone` | **Primary Topic**: Iteration 43 / 95 (Sparse FPS Power $P(x)^k$ via ODE $P G' = k P' G$)
- **Mathematical Statement & Constraints**:
  You are given an even integer $n$ ($2 \le n \le 2 \times 10^5$) and a subset of allowed base-10 digits $D \subseteq \{0, 1, \dots, 9\}$ ($1 \le |D| \le 10$). Count the number of $n$-digit strings (leading zeros allowed) using only digits from $D$ such that the sum of the first $n/2$ digits equals the sum of the last $n/2$ digits, modulo $998244353$.
  - **Target Complexity**: $O(n |D|)$ time and $O(n)$ space (zero NTT calls!).
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Express the number of $k$-digit strings ($k = n/2$) with digit sum $s$ as $[x^s] P(x)^k$, where $P(x) = \sum_{d \in D} x^d$. The answer is $\sum_s ([x^s] P(x)^k)^2$.
  - *Hint 2*: Instead of running NTT on $P(x)^k$, notice $P(x)$ has degree $\le 9$ and at most $|D| \le 10$ non-zero terms. Write the differential equation satisfied by $G(x) = P(x)^k$.
  - *Hint 3*: Shift $P(x)$ by its minimum digit $d_{\min} = \min D$ so $P(0) = 1$, and unroll $P(x) G'(x) = k P'(x) G(x)$ via $s g_s = \sum_{j \ge 1} ((k+1) d_j - s) g_{s - d_j}$ in $O(n |D|)$ time.
- **Complete Derivation & Solution Sketch**:
  Let $k = n / 2$ and shift $D$ by $d_{\min} = \min D$ so $0 \in D$ and $P(0) = 1$. Then $G(x) = P(x)^k = \sum_{s=0}^{9k} g_s x^s$ satisfies $P(x) G'(x) = k P'(x) G(x)$. Extracting $[x^{s-1}]$ gives:
  $$s \, g_s = \sum_{d \in D \setminus \{0\},\, d \le s} \left( (k + 1) d - s \right) g_{s - d}$$
  with $g_0 = 1$. Computing $g_0, \dots, g_{9k}$ takes at most $9 \times 9k \approx 8.1 \times 10^6$ operations ($\sim 10\text{ ms}$, $20\times$ faster than NTT), and the answer is $\sum_{s=0}^{9k} g_s^2 \bmod 998244353$.

---

#### Problem 2: Luogu P4389 — 付公主的背包 (Princess Fu's Knapsack)
- **Source & Link**: Luogu — [https://www.luogu.com.cn/problem/P4389](https://www.luogu.com.cn/problem/P4389) (Discovered by Cohort 1)
- **Difficulty Tier**: `Stepping Stone` | **Primary Topic**: Iteration 43 / 95 (Grouped 2-Sparse $\ln(1 - x^v)$ + $\exp$)
- **Mathematical Statement & Constraints**:
  You have $n$ types of items, where the $i$-th item has volume $v_i$ and infinite supply. For every volume $s = 1, 2, \dots, m$, compute the number of ways to fill a knapsack of exact volume $s$, modulo $998244353$.
  - **Constraints**: $1 \le n, m \le 10^5$, $1 \le v_i \le m$, Time Limit 1.0s.
  - **Target Complexity**: $O(m \log m)$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Write the OGF $F(x) = \prod_{i=1}^n \frac{1}{1 - x^{v_i}} \bmod x^{m+1}$. Why is multiplying $n$ sparse inverses sequentially $O(n m)$ and too slow?
  - *Hint 2*: Apply the logarithmic transformation $\ln F(x) = \sum_{i=1}^n -\ln(1 - x^{v_i})$ and group items by equal volume $v$ (count $c_v$).
  - *Hint 3*: Use $-\ln(1 - x^v) = \sum_{k \ge 1} \frac{1}{k} x^{k v}$ to populate $A(x) = \ln F(x) \bmod x^{m+1}$ in $O(m \log m)$ harmonic time, then compute $F(x) = \exp(A(x))$ via CDQ NTT or Newton $\exp$.
- **Complete Derivation & Solution Sketch**:
  Each factor $(1 - x^{v_i})^{-1}$ is the inverse of a 2-sparse polynomial, whose logarithm is $-\ln(1 - x^{v_i}) = \sum_{k=1}^{\lfloor m/v_i \rfloor} \frac{1}{k} x^{k v_i}$. Counting the frequency $c_v$ of each volume $v \in [1, m]$, we accumulate $A(x) = \sum_{v=1}^m c_v \sum_{k=1}^{\lfloor m/v \rfloor} \frac{1}{k} x^{k v}$ in $O(\sum_{v=1}^m m/v) = O(m \log m)$ time, and recover $F(x) = \exp(A(x)) \bmod x^{m+1}$ via the differential equation $F'(x) = A'(x) F(x)$ (solved in $O(m \log^2 m)$ via CDQ NTT or $O(m \log m)$ via Newton $\exp$).

---

#### Problem 3: Luogu P4841 — [集训队作业2013] 城市规划 (City Planning)
- **Source & Link**: Luogu — [https://www.luogu.com.cn/problem/P4841](https://www.luogu.com.cn/problem/P4841) (Discovered by Cohort 1)
- **Difficulty Tier**: `Stepping Stone` | **Primary Topic**: Iteration 42 & 45 (Connected Graphs EGF ODE $G' = F' G \implies F' = G' / G$ via CDQ NTT)
- **Mathematical Statement & Constraints**:
  Find the number of connected simple undirected labeled graphs on $n$ vertices, modulo $1004535809 = 479 \times 2^{21} + 1$.
  - **Constraints**: $1 \le n \le 130000$, $p = 1004535809$.
  - **Target Complexity**: $O(n \log^2 n)$ via CDQ NTT or $O(n \log n)$ via FPS $\ln$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Let $g_n = 2^{\binom{n}{2}}$ be the number of all labeled graphs on $n$ vertices, and $f_n$ be the number of connected ones. How does the component containing vertex $1$ relate $g_n$ and $f_k$?
  - *Hint 2*: Fixing the size $k \in [1, n]$ of the connected component containing vertex $1$ gives $g_n = \sum_{k=1}^n \binom{n-1}{k-1} f_k g_{n-k}$. Rewrite this in EGF form!
  - *Hint 3*: Divide by $(n-1)!$ to get $n \frac{g_n}{n!} = \sum_{k=1}^n \left(k \frac{f_k}{k!}\right) \frac{g_{n-k}}{(n-k)!}$, i.e., $G'(x) = F'(x) G(x)$, and solve for $F'(x)$ via semi-online CDQ NTT or polynomial inversion.
- **Complete Derivation & Solution Sketch**:
  Setting $G(x) = \sum_{n \ge 0} 2^{\binom{n}{2}} \frac{x^n}{n!}$ and $F(x) = \sum_{n \ge 1} f_n \frac{x^n}{n!}$, we have $G(x) = \exp(F(x)) \implies G'(x) = F'(x) G(x)$. Isolating the $k = n$ term gives the semi-online recurrence:
  $$\tilde{f}_n = \tilde{g}_n - \sum_{k=1}^{n-1} \tilde{f}_k \, \frac{g_{n-k}}{(n-k)!}, \qquad \text{where } \tilde{f}_k = \frac{f_k}{(k-1)!},\quad \tilde{g}_n = \frac{g_n}{(n-1)!}$$
  Running offline CDQ NTT on $[1, n]$ (or $F'(x) = G'(x) G(x)^{-1} \bmod x^n$) yields $f_n = (n-1)! \tilde{f}_n \bmod 1004535809$.

---

#### Problem 4: Codeforces 438E — The Child and Binary Tree
- **Source & Link**: Codeforces Round 250 (Div. 1) — [https://codeforces.com/problemset/problem/438/E](https://codeforces.com/problemset/problem/438/E) (Discovered by Cohort 2)
- **Difficulty Tier**: `Stepping Stone` | **Primary Topic**: Iteration 41, 43 & 45 (Catalan Quadratic GF via `sqrt`+`inv`, Sparse ODE, or Relaxed Convolution)
- **Mathematical Statement & Constraints**:
  Given a set $S$ of $n$ positive integer weights ($1 \le n \le 10^5, 1 \le c_i \le 10^5$) and a maximum weight $m \le 10^5$, for each $s = 1, \dots, m$, count the number of rooted vertex-weighted binary trees whose vertex weights belong to $S$ and sum to $s$, modulo $998244353$.
  - **Target Complexity**: $O(m \log m)$ via quadratic formula, $O(m |S|)$ via sparse ODE, or $O(m \log^2 m)$ via Relaxed Convolution.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Write the OGF equation $F(x) = 1 + C(x) F(x)^2$ where $C(x) = \sum_{c \in S} x^c$.
  - *Hint 2*: Notice $C(0) = 0$, so $\frac{1 - \sqrt{1 - 4C(x)}}{2 C(x)}$ cannot be evaluated by directly inverting $C(x)$. Rationalize the numerator!
  - *Hint 3*: Rewrite $F(x) = \frac{2}{1 + \sqrt{1 - 4 C(x)}}$, or when $|S|$ is small use Recipe B (Iteration 41) / `SparseFPS::sqrt` on $1 - 4C(x)$!
- **Complete Derivation & Solution Sketch**:
  - **Method 1 (Rationalized Quadratic Formula, $O(m \log m)$)**: $F(x) = \frac{1 - \sqrt{1 - 4 C(x)}}{2 C(x)} = \frac{2}{1 + \sqrt{1 - 4 C(x)}}$, which requires one `poly_sqrt` and one `poly_inv` with constant term $1$.
  - **Method 2 (D-Finite ODE when $|S|$ is small, $O(m |S|)$)**: $W(x) = \sqrt{1 - 4 C(x)}$ satisfies $(1 - 4 C(x)) W'(x) = -2 C'(x) W(x)$, and $F(x) - 1 = C(x) F(x)^2$.
  - **Method 3 (Relaxed Convolution, $O(m \log^2 m)$)**: Maintain $A(x) = F(x)^2$ online via `rc.next(f_s, f_s)` and $B(x) = C(x) A(x)$ via a second `RelaxedConvolution` instance `rc2`.

---

#### Problem 5: AtCoder ABC 222 H — Beautiful Binary Tree
- **Source & Link**: AtCoder Beginner Contest 222 — [https://atcoder.jp/contests/abc222/tasks/abc222_h](https://atcoder.jp/contests/abc222/tasks/abc222_h) (Discovered by Cohort 1)
- **Difficulty Tier**: `Stepping Stone` | **Primary Topic**: Iteration 41 & 43 ($O(N)$ D-Finite / Sparse Power Recurrence for Lagrange Inversion at $N = 10^7$)
- **Mathematical Statement & Constraints**:
  Count the number of "beautiful binary trees" of size $N \le 10^7$ modulo $998244353$, whose generating function reduces via Lagrange Inversion to extracting:
  $$H_N = \frac{1}{N} [y^{N-1}] \left( 1 + 3 y + y^2 (1 + y)^2 \right)^N = \frac{1}{N} [y^{N-1}] \left( 1 + 3 y + y^2 + 2 y^3 + y^4 \right)^N$$
  - **Constraints**: $1 \le N \le 10^7$, $p = 998244353$, Time Limit 2.0s.
  - **Target Complexity**: $O(N)$ time (since $N = 10^7$, $O(N \log N)$ NTT will TLE!).
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Set up the coupled bivariate tree equations and eliminate the auxiliary variable to get $U(x) = x P(U(x))$ where $P(y) = 1 + 3y + y^2 + 2y^3 + y^4$.
  - *Hint 2*: Apply Lagrange Inversion: $[x^N] U(x) = \frac{1}{N} [y^{N-1}] P(y)^N$. Why is NTT too slow at $N = 10^7$?
  - *Hint 3*: Since $P(y)$ has degree $4$, $G(y) = P(y)^N$ satisfies $P(y) G'(y) = N P'(y) G(y)$, yielding a 5-term recurrence for $g_k = [y^k] P(y)^N$ in $O(N)$ time!
- **Complete Derivation & Solution Sketch**:
  Applying `SparseFPS::pow` (or Recipe A) to $P(y) = 1 + 3y + y^2 + 2y^3 + y^4$ with $c_0 = 1, c_1 = 3, c_2 = 1, c_3 = 2, c_4 = 1$ gives the 4-term recurrence:
  $$k \, g_k = \sum_{j=1}^{\min(4, k)} \left( (N + 1) j - k \right) c_j \, g_{k - j} \qquad (k = 1, \dots, N - 1)$$
  with $g_0 = 1$. Precomputing inverses $1^{-1}, \dots, N^{-1} \bmod 998244353$ in $O(N)$ time computes $H_N = \frac{1}{N} g_{N-1}$ in $4 N$ multiplications ($\sim 80\text{ ms}$).

---

#### Problem 6: Yukicoder No. 1939 — Numbered Colorful Balls
- **Source & Link**: Yukicoder — [https://yukicoder.me/problems/no/1939](https://yukicoder.me/problems/no/1939) (Discovered by Cohort 1; Reconciled with Cohort 2)
- **Difficulty Tier**: `Stepping Stone` | **Primary Topic**: Iteration 43 (Lagrange Inversion Modelling + $O(NM)$ `sparse_pow`)
- **Cross-Cohort Reconciliation Note**: Cohort 2 noted that once reduced to $[y^N] Q(y)^{-(N+1)}$ this is a direct application of `sparse_pow`, while Cohort 1 retained it because the combinatorial block-deletion-to-Lagrange-Inversion reduction is an instructive modelling bridge for beginners. We preserve it in Tier 1 as the canonical bridge between Lagrange Inversion and Sparse ODEs.
- **Mathematical Statement & Constraints**:
  You have $M$ colors of balls ($1 \le M \le 100$). A ball of color $i$ has $l_i \ge 1$, and a contiguous block of $l_i$ balls of color $i$ numbered $1, 2, \dots, l_i$ can be deleted at once. Count the number of sequences of length $N \le 10^5$ that can be completely emptied, modulo $998244353$.
  - **Target Complexity**: $O(N M)$ time.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Decompose a valid sequence by the outermost blocks deleted last: between any two adjacent balls of a block of length $l_i$, an arbitrary valid sequence can be nested.
  - *Hint 2*: Show that $U(x) = x F(x)$ satisfies $U(x) = \frac{x}{1 - \sum_{i=1}^M U(x)^{l_i}} = \frac{x}{Q(U(x))}$.
  - *Hint 3*: By Lagrange Inversion, $[x^N] F(x) = [x^{N+1}] U(x) = \frac{1}{N+1} [y^N] Q(y)^{-(N+1)}$, where $Q(y) = 1 - \sum_{i=1}^M y^{l_i}$ has at most $M + 1 \le 101$ non-zero terms. Apply `SparseFPS::pow` in $O(NM)$ time!
- **Complete Derivation & Solution Sketch**:
  By the nested block decomposition, $F(x) = \frac{1}{1 - \sum_{i=1}^M (x F(x))^{l_i}}$. Setting $U(x) = x F(x)$ gives $U(x) Q(U(x)) = x$ where $Q(y) = 1 - \sum_{i=1}^M y^{l_i}$. By Lagrange Inversion, $[x^N] F(x) = \frac{1}{N+1} [y^N] Q(y)^{-(N+1)}$, which `SparseFPS::pow(Q, MOD - 1 - (N + 1), N + 1)` evaluates in $O(N M)$ time.

---

#### Problem 7: Luogu P4456 — [CQOI2018] 交错序列 (Alternating Sequences)
- **Source & Link**: CQOI 2018 / Luogu — [https://www.luogu.com.cn/problem/P4456](https://www.luogu.com.cn/problem/P4456) (Discovered by Cohort 2)
- **Difficulty Tier**: `Stepping Stone` | **Primary Topic**: Iteration 41 & 44 (Bivariate Euler Differential Operators $\vartheta_u^a \vartheta_v^b$ on Rational GF)
- **Mathematical Statement & Constraints**:
  An alternating binary string of length $n$ has no two adjacent `1`s. If a string has $x$ zeros and $y$ ones ($x + y = n$), its weight is $x^a y^b$. Compute the sum of $x^a y^b$ over all alternating strings of length $n$ modulo a prime $p$.
  - **Constraints**: $n \le 10^7$, $0 \le a, b \le 45$, $p \le 10^9 + 7$.
  - **Target Complexity**: $O((a+b)^2 \log n)$ via matrix exponentiation or $O(a+b + \log n)$ via bivariate Euler operator / P-recursive relation.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Write the bivariate OGF of alternating strings by tracking `0` with $u$ and `1` with $v$: $G(u, v) = \frac{1 + v}{1 - u - u v}$.
  - *Hint 2*: Notice $x + y = n \implies x = n - y$, so $x^a y^b = \sum_{j=0}^a \binom{a}{j} (-1)^j n^{a-j} y^{b+j}$. Now you only need $\sum y^k$ for $k \le a + b$!
  - *Hint 3*: Alternatively, apply the Euler operator $\left. \vartheta_u^a \vartheta_v^b \frac{1+v}{1 - z(u + uv)} \right|_{u=v=1} = \frac{P_{a,b}(z)}{(1 - z - z^2)^{a+b+1}}$, which is rational with Fibonacci-type denominator $(1 - z - z^2)^{a+b+1}$!
- **Complete Derivation & Solution Sketch**:
  Setting $z$ to track total length $x + y = n$ and $v$ to track `1`s, $G(z, v) = \frac{1 + z v}{1 - z - z^2 v}$. Applying $\vartheta_v^k = \left(v \frac{\partial}{\partial v}\right)^k$ at $v = 1$ for $k = 0, \dots, a + b$ yields a rational generating function $\frac{A_k(z)}{(1 - z - z^2)^{k+1}}$, whose denominator has degree $2(a+b+1) \le 182$, or directly expands $y^k = \sum_{j=0}^k \left\{ \begin{matrix} k \\ j \end{matrix} \right\} j! \binom{y}{j}$ where $\sum_y \binom{y}{j} \binom{n - y + 1}{y} = [z^n] \frac{z^{2j-1}(1+z)}{(1 - z - z^2)^{j+1}}$.

---

#### Problem 8: Codeforces 623E — Transforming Sequence
- **Source & Link**: AIM Tech Round (Div. 1) — [https://codeforces.com/problemset/problem/623/E](https://codeforces.com/problemset/problem/623/E) (Discovered by Cohort 2)
- **Difficulty Tier**: `Stepping Stone` | **Primary Topic**: Iteration 42 (Scale-Substituted EGF Doubling $F_{2m}(x) = F_m(2^m x) F_m(x)$)
- **Mathematical Statement & Constraints**:
  Given $n \le 10^{18}$ and $k \le 3 \times 10^4$, count sequences $a_1, \dots, a_n \in [1, 2^k - 1]$ such that the bitwise prefix ORs satisfy $0 < b_1 < b_2 < \dots < b_n < 2^k$, modulo $10^9 + 7$.
  - **Target Complexity**: $O(k \log k \log n)$ time.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Since each step must set at least one new bit among the $k$ bits, if $n > k$ the answer is $0$ immediately!
  - *Hint 2*: For $n \le k$, if we split a sequence of length $m_1 + m_2$ into the first $m_1$ steps (using $j$ bits) and the last $m_2$ steps (using $i - j$ new bits, while each of the $j$ already-active bits can be freely set to `0` or `1` in each of the $m_2$ steps, giving $2^{j \cdot m_2}$ ways), what is the EGF transition?
  - *Hint 3*: Define $F_m(x) = \sum_{i=m}^k dp[m][i] \frac{x^i}{i!}$. Then $F_{m_1 + m_2}(x) = F_{m_1}(2^{m_2} x) \cdot F_{m_2}(x)$, allowing binary exponentiation in $O(\log n)$ steps!
- **Complete Derivation & Solution Sketch**:
  If $n > k$, output $0$. Otherwise, $dp[m_1 + m_2][i] = \sum_{j} \binom{i}{j} dp[m_1][j] \, 2^{j \cdot m_2} \, dp[m_2][i - j]$. In EGF form, $F_{m_1 + m_2}(x) = F_{m_1}(2^{m_2} x) F_{m_2}(x) \bmod x^{k+1}$ where $F_1(x) = \sum_{i=1}^k \frac{x^i}{i!} = e^x - 1$. Scaling $[x^j] F_{m_1}(2^{m_2} x) = 2^{j \cdot m_2} [x^j] F_{m_1}(x)$ takes $O(k)$ time per doubling step, and $3$-prime NTT / MTT computes the product modulo $10^9 + 7$ in $O(k \log k \log n)$ time.

---

### Tier 2: Intermediate (`Medium` — 8 Problems)

#### Problem 9: Yukicoder No. 963 — 門松列列（2） (Kadomatsu Sequence Sequence 2)
- **Source & Link**: Yukicoder — [https://yukicoder.me/problems/no/963](https://yukicoder.me/problems/no/963) (Discovered by Cohort 1)
- **Difficulty Tier**: `Intermediate` | **Primary Topic**: Iteration 42 / 94 (Riccati / Autonomous Nonlinear ODE $2 F' = 1 + F^2$)
- **Mathematical Statement & Constraints**:
  Count the number of alternating permutations of $(1, 2, \dots, N)$ (where every contiguous triple $(A, B, C)$ has $B$ as either its maximum or minimum) modulo $1012924417 = 483 \times 2^{21} + 1$, for $3 \le N \le 202020$.
  - **Target Complexity**: $O(N \log N)$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Removing the maximum element $N$ splits an up-down permutation into two smaller alternating permutations of sizes $k$ and $n - 1 - k$.
  - *Hint 2*: Show that the EGF $F(x) = \sum_{n \ge 0} E_n \frac{x^n}{n!}$ satisfies the Riccati ODE $2 F'(x) = 1 + F(x)^2$ with $F(0) = 1$.
  - *Hint 3*: Apply the Riccati substitution $F(x) = -2 \frac{u'(x)}{u(x)}$ to obtain $u''(x) + \frac{1}{4} u(x) = 0$ (or solve $F(x) = \frac{1 + \sin x}{\cos x}$ via one polynomial inverse of $\cos x$).
- **Complete Derivation & Solution Sketch**:
  By the Riccati substitution $F(x) = -2 u'(x)/u(x)$ with $u(0) = 1, u'(0) = -1/2$, we get $u''(x) + \frac{1}{4} u(x) = 0 \implies u(x) = \cos(x/2) - \sin(x/2)$ (or directly $F(x) = \sec x + \tan x = \frac{1 + \sin x}{\cos x}$). Computing $\sin x, \cos x \bmod x^{N+1}$ takes $O(N)$ time, and a single NTT inversion of $\cos x$ yields $2 E_N = 2 \cdot N! [x^N] F(x)$ in $O(N \log N)$ time.

---

#### Problem 10: AtCoder ABC 213 H — Stroll
- **Source & Link**: AtCoder Beginner Contest 213 — [https://atcoder.jp/contests/abc213/tasks/abc213_h](https://atcoder.jp/contests/abc213/tasks/abc213_h) (Discovered by Both Cohorts)
- **Difficulty Tier**: `Intermediate` | **Primary Topic**: Iteration 45 / 97 (Multi-Graph Semi-Online CDQ NTT with Frequency-Domain Aggregation)
- **Mathematical Statement & Constraints**:
  Given an undirected multigraph with $N \le 10$ vertices and $M \le 10$ edges, where edge $j$ has $p_{j, t}$ ways to be traversed in $t \in [1, T]$ time units ($T \le 4 \times 10^4$), find the number of walks from vertex $1$ at time $0$ to vertex $1$ at time $T$, modulo $998244353$.
  - **Target Complexity**: $O((N + M) T \log^2 T)$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Write the DP transition $dp[u][t] = \sum_{e=(u,v)} \sum_{s=1}^t dp[v][t - s] p_{e, s}$.
  - *Hint 2*: Apply CDQ Divide-and-Conquer on time $[0, T]$. Why can you avoid running $2M$ forward and inverse NTTs per recursion node?
  - *Hint 3*: Pre-transform the $M$ edge polynomials for each power-of-2 block size $L = r - l + 1$. Inside `cdq(l, r)`, perform $N$ forward NTTs on $dp[u][l \dots \text{mid}]$, multiply-accumulate along the $M$ edges in point-value form, and perform $N$ inverse NTTs!
- **Complete Derivation & Solution Sketch**:
  See Section 6.1: inside `cdq(l, r)`, after `cdq(l, mid)` finalizes $dp[v][l \dots \text{mid}]$ for all $v \in [1, N]$, transform each vertex slice once ($N$ NTTs of size $L$), accumulate $\widehat{\text{acc}}_u += \widehat{dp}_v \odot \widehat{p}_e$ for each edge $e = (u, v)$ in $O(M L)$ pointwise multiplications, and inverse-transform $\widehat{\text{acc}}_u$ ($N$ INTTs) to update $dp[u][\text{mid}+1 \dots r]$ before calling `cdq(mid + 1, r)`.

---

#### Problem 11: Codeforces 553E — Kyoya and Train
- **Source & Link**: Codeforces Round 309 (Div. 1) — [https://codeforces.com/problemset/problem/553/E](https://codeforces.com/problemset/problem/553/E) (Discovered by Both Cohorts)
- **Difficulty Tier**: `Intermediate` | **Primary Topic**: Iteration 45 / 97 (Backward CDQ FFT with Non-Linear $\min$ Interleaving)
- **Mathematical Statement & Constraints**:
  A directed graph has $n \le 50$ vertices and $m \le 100$ edges. Edge $e = (u, v)$ costs $c_e$ and takes time $k \in [1, T]$ ($T \le 2 \times 10^4$) with probability $p_{e, k}$. Arriving at $n$ after time $T$ incurs a fine $x$ plus the shortest deterministic path to $n$. Find the minimum expected cost from $1$ at time $0$.
  - **Target Complexity**: $O(m T \log^2 T)$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: For $t > T$, $dp[v][t] = \text{dist}(v, n) + x$. For $t \le T$, $dp[u][t] = \min_{e=(u,v)} (c_e + \sum_{k=1}^T p_{e, k} dp[v][t + k])$.
  - *Hint 2*: Because of the outer $\min_{e=(u,v)}$, the recurrence is non-linear and cannot be solved by polynomial inversion—it requires CDQ FFT!
  - *Hint 3*: Run CDQ **backwards** on time $[0, T]$: recurse on $[\text{mid}+1, r]$ first, convolve $dp[v][\text{mid}+1 \dots r]$ with the reversed array $p_{e, r-l \dots 1}$ to update edge accumulators $g[e][l \dots \text{mid}]$, and recurse on $[l, \text{mid}]$.
- **Complete Derivation & Solution Sketch**:
  Initialize $g[e][t] = \sum_{k = T + 1 - t}^T p_{e, k} (\text{dist}(v, n) + x)$ for all $t \in [0, T]$. In `cdq(l, r)`: if $l == r$, set $dp[u][l] = \min_{e=(u,v)} (c_e + g[e][l])$; otherwise call `cdq(mid + 1, r)`, convolve $A[0 \dots r - \text{mid} - 1] = dp[v][\text{mid}+1 \dots r]$ with $B[0 \dots r - l - 1] = p_e[r - l \dots 1]$ using complex FFT so that $[x^{(r - \text{mid} - 1) + (r - t - (\text{mid}+1))}](A \cdot B)$ adds $\sum_{j=\text{mid}+1}^r dp[v][j] p_{e, j - t}$ to $g[e][t]$ for $t \in [l, \text{mid}]$, and finally call `cdq(l, mid)`.

---

#### Problem 12: Codeforces 755G — PolandBall and Many Other Balls
- **Source & Link**: 8VC Venture Cup 2017 Elimination Round — [https://codeforces.com/problemset/problem/755/G](https://codeforces.com/problemset/problem/755/G) (Discovered by Cohort 1)
- **Difficulty Tier**: `Intermediate` | **Primary Topic**: Iteration 41 & 44 (Bivariate Delannoy Anti-Diagonal $\to$ $O(K)$ D-Finite ODE Recurrence for Fixed $N \le 10^9$)
- **Mathematical Statement & Constraints**:
  Given $n \le 10^9$ balls in a row and $K \le 32768$, for each $k = 1, \dots, K$, count the number of ways to form $k$ disjoint groups where each group is either $1$ ball or $2$ adjacent balls, modulo $998244353$.
  - **Target Complexity**: $O(K)$ time via D-finite ODE!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Write the bivariate OGF $G(x, y) = \frac{1}{1 - (1+y)x - y x^2}$. Show that $a_k = [x^n y^k] G(x, y)$ has three equivalent closed-form binomial representations:
    $$a_k = \sum_{j=0}^{k} \binom{n - j}{j} \binom{n - 2j}{k - j} = \sum_{j=0}^{k} \binom{n - j}{k} \binom{k}{j} = \sum_{j=0}^{k} \binom{n - k}{j} \binom{k}{j} 2^j$$
    (counting $j$ groups of size $2$ and $k - j$ groups of size $1$, or equivalently the Delannoy number $D(k, n - k) = [u^k v^{n-k}] \frac{1}{1 - u - v - uv}$!).
  - *Hint 2*: For $n \ge K$, the polynomial $F_n(y) = [x^n] G(x, y) = \sum_{k=0}^n a_k y^k$ agrees modulo $y^{K+1}$ with the principal branch $A_n(y) = \frac{1}{\sqrt{1+6y+y^2}} \left(\frac{1+y+\sqrt{1+6y+y^2}}{2}\right)^{n+1}$. However, $A_n(y)$ alone involves $\sqrt{1+6y+y^2}$, whereas $F_n(y)$ is a rational combination of both conjugate roots $\lambda_\pm(y) = \frac{1+y \pm \sqrt{1+6y+y^2}}{2}$ and satisfies a **2nd-order** linear ODE with polynomial coefficients!
  - *Hint 3*: Either extract the 4-term recurrence from the exact 2nd-order ODE for $F_n(y)$, or apply Zeilberger's Creative Telescoping (Engine 2) directly to $a_k = \sum_{j=0}^k \binom{n-k}{j}\binom{k}{j} 2^j$ along the anti-diagonal $(k, n-k)$ to obtain a **3-term P-recursive recurrence** in $O(K)$ total time!
- **Complete Derivation & Solution Sketch**:
  1. **Method A (Exact 2nd-Order Linear ODE $\to$ 4-Term Recurrence)**:
     Let $W(y) = \sqrt{1 + 6y + y^2}$ and $\lambda_{\pm}(y) = \frac{1 + y \pm W(y)}{2}$. Since $F_n(y) = \frac{\lambda_+(y)^{n+1} - \lambda_-(y)^{n+1}}{W(y)}$, differentiating twice and eliminating $W(y)$ yields the exact 2nd-order linear ODE:
     $$y(1 - y)(1 + 6y + y^2) F_n''(y) - \Big(n + 5(n - 2)y - 5n y^2 - (n - 2) y^3\Big) F_n'(y) + n\Big((2n - 1) - 2(n + 2)y + y^2\Big) F_n(y) = 0$$
     Extracting $[y^k]$ gives the exact 4-term recurrence for $a_k = [y^k] F_n(y)$ ($k \ge 1$, with $a_{-1} = 0, a_0 = 1, a_1 = 2n - 1$):
     $$(k + 1)(n - k) a_{k+1} = \Big(5k^2 - 5(n - 1)k + n(2n - 1)\Big) a_k - \Big(5k^2 - 5(n + 3)k + (n + 2)(2n + 5)\Big) a_{k-1} - (k - 1)(k - n - 2) a_{k-2}$$
  2. **Method B (Anti-Diagonal Creative Telescoping $\to$ 3-Term P-Recursive Recurrence)**:
     Applying Engine 2 (Section 5.2) to the symmetric Delannoy representation $a_k = D(k, n - k) = \sum_{j=0}^k \binom{n-k}{j} \binom{k}{j} 2^j$ eliminates one shift and yields the even simpler **3-term** P-recursive relation ($k \ge 1$):
     $$(k + 1)(n - k)(n + 1 - 2k) a_{k+1} = (n - 2k)\Big((2n - 1)(n + 1) - 6k(n - k)\Big) a_k - k(n + 1 - k)(n - 1 - 2k) a_{k-1}$$
     - **Hand Check ($n = 4$: $a_0 = 1, a_1 = 7, a_2 = 13, a_3 = 7, a_4 = 1$)**:
       - $k = 1$: $2(3)(3) a_2 = 2(35 - 18) a_1 - 1(4)(1) a_0 \implies 18 a_2 = 34(7) - 4(1) = 234 \implies a_2 = 13$.
       - $k = 2$: $3(2)(1) a_3 = 0 \cdot a_2 - 2(3)(-1) a_1 \implies 6 a_3 = 6(7) = 42 \implies a_3 = 7$.
       - $k = 3$: $4(1)(-1) a_4 = (-2)(35 - 18) a_3 - 3(2)(-3) a_2 \implies -4 a_4 = -34(7) + 18(13) = -4 \implies a_4 = 1$.
     Both the 4-term and 3-term recurrences compute $a_1, \dots, a_K \bmod 998244353$ in **$O(K)$** time with zero NTTs!

---

#### Problem 13: AtCoder AGC 043 D — Merge Triplets
- **Source & Link**: AtCoder Grand Contest 043 — [https://atcoder.jp/contests/agc043/tasks/agc043_d](https://atcoder.jp/contests/agc043/tasks/agc043_d) (Discovered by Cohort 2)
- **Difficulty Tier**: `Intermediate` | **Primary Topic**: Iteration 41 & 43 (Prefix-Max Block Decomposition $\to$ Bivariate Sparse Exponential ODE)
- **Mathematical Statement & Constraints**:
  Count permutations of $(1, \dots, 3N)$ ($N \le 2000$) obtainable by merging $N$ sequences of length $3$, modulo $M$ ($10^8 \le M \le 10^9 + 9$ prime).
  - **Target Complexity**: $O(N^2)$ time (via 3-sparse ODE).
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Decompose a permutation into blocks at its left-to-right maxima. What characterizes a permutation obtainable by merging $N$ triplets?
  - *Hint 2*: Every prefix-max block must have length $1, 2,$ or $3$, and the number of blocks of length $1$ must be $\ge$ the number of blocks of length $2$!
  - *Hint 3*: The bivariate EGF tracking length $x$ and balance $y$ ($\#(\text{len } 1) - \#(\text{len } 2)$) is $F(x, y) = \exp\!\left(y x + \frac{y^{-1} x^2}{2} + \frac{x^3}{3}\right)$, which satisfies the 3-sparse ODE $\frac{\partial F}{\partial x} = (y + y^{-1} x + x^2) F(x, y)$!
- **Complete Derivation & Solution Sketch**:
  A block of length $L \in \{1, 2, 3\}$ has $(L - 1)!$ internal orderings after fixing its maximum at the front, so its EGF weight is $\frac{(L-1)!}{L!} x^L = \frac{x^L}{L}$. Thus $F(x, y) = \exp\!\left(y x + \frac{y^{-1} x^2}{2} + \frac{x^3}{3}\right)$. Differentiating with respect to $x$ gives $\frac{\partial F}{\partial x} = (y + y^{-1} x + x^2) F(x, y)$. Extracting $[x^{n-1} y^b]$ gives the 3-term recurrence:
  $$n \, f_{n, b} = f_{n-1, b-1} + f_{n-2, b+1} + f_{n-3, b}$$
  which avoids division by $n$ if we instead track $dp_{n, b} = n! f_{n, b}$ via $dp_{n, b} = dp_{n-1, b-1} + (n-1) dp_{n-2, b+1} + (n-1)(n-2) dp_{n-3, b}$ in $O(N^2)$ time!

---

#### Problem 14: AtCoder ABC 253 Ex — We Love Forest
- **Source & Link**: AtCoder Beginner Contest 253 — [https://atcoder.jp/contests/abc253/tasks/abc253_h](https://atcoder.jp/contests/abc253/tasks/abc253_h) (Discovered by Cohort 2)
- **Difficulty Tier**: `Intermediate` | **Primary Topic**: Iteration 43 / 95 (Subset-Ranked Sparse ODE $\exp$ $H' = P' H$ on Bitmask Polynomials)
- **Mathematical Statement & Constraints**:
  Given an undirected multigraph with $N \le 14$ vertices and $M \le 500$ edges, for each $K = 1, \dots, N-1$, find the probability that $K$ random edges (chosen with replacement) form a simple forest, modulo $998244353$.
  - **Target Complexity**: $O(N^2 2^N)$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: A forest of $K$ edges on $N$ vertices has exactly $N - K$ connected components, each of which is a tree.
  - *Hint 2*: Compute the number of spanning trees $t_S$ on each vertex subset $S \subseteq V$ using Kirchhoff's Matrix-Tree Theorem or subset DP.
  - *Hint 3*: Rank subsets by size $i = |S|$. The subset-ranked EGF of forests is $H(x) = \exp(P(x))$ where $[x^i] P(x)$ carries the subset convolution vector of trees of size $i$. Unroll $H'(x) = P'(x) H(x)$ via $k H_k = \sum_{i=1}^k i P_i *_{\text{subset}} H_{k-i}$ in $O(N^2 2^N)$!
- **Complete Derivation & Solution Sketch**:
  After computing $t_S$ for all $S$, apply the Fast Mobius / Zeta Transform (FMT) to each size layer $P_i$ ($i = 1 \dots N$). For each frequency coordinate $\omega \in [0, 2^N - 1]$, $P(\omega, x) = \sum_{i=1}^N \widehat{P}_i(\omega) x^i$ is a polynomial of degree $N \le 14$. Applying `SparseFPS::exp` point-wise in the FMT domain via $k \widehat{H}_k(\omega) = \sum_{i=1}^k i \widehat{P}_i(\omega) \widehat{H}_{k-i}(\omega)$ takes $O(N^2 2^N)$ time, and inverting FMT on $\widehat{H}_{N}(V)$ segregated by number of components $c = N - K$ (or tracking $y$ for component count via $H_K = \frac{1}{c!} [x^N] P(x)^c$) yields the exact count of $K$-edge forests!

---

#### Problem 15: Codeforces 848E — Days of Floral Colours
- **Source & Link**: Codeforces Round 431 (Div. 1) — [https://codeforces.com/problemset/problem/848/E](https://codeforces.com/problemset/problem/848/E) (Discovered by Cohort 2)
- **Difficulty Tier**: `Intermediate` | **Primary Topic**: Iteration 41 & 45 ($3 \times 3$ Coupled Rational System $\to$ CDQ NTT or Order-12 Linear Recurrence)
- **Mathematical Statement & Constraints**:
  Solve the coupled circular domino/floral tiling system of length $n \le 5 \times 10^4$ modulo $998244353$, where the $3$ boundary states satisfy a $3 \times 3$ system of semi-online convolutions $F_s(x) = G_s(x) + \sum_{t=0}^2 M_{s, t}(x) F_t(x)$ with rational transition series $M_{s, t}(x)$ generated by $g_k = g_{k-2} + g_{k-4}$.
  - **Target Complexity**: $O(n \log^2 n)$ via $3 \times 3$ CDQ NTT, or $O(n)$ via rational denominator clearing!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Decompose the circular pairing along the diameter breaks; each arc of length $k$ contributes $k^2 g_k$, $k^2 g_{k-1}$, or $k^2 g_{k-2}$ depending on whether endpoints use cross-diameter tiles.
  - *Hint 2*: In CDQ NTT on $[0, n]$, perform $3$ forward NTTs on $F_0, F_1, F_2$, multiply by the $3 \times 3$ matrix $\widehat{M}$ in frequency space, and perform $3$ inverse NTTs!
  - *Hint 3*: Even better: since $g_k = g_{k-2} + g_{k-4}$ is rational with denominator $1 - x^2 - x^4$, applying $\vartheta^2$ gives rational functions with denominator $(1 - x^2 - x^4)^3$ (degree $12$), so $\det(I - M(x))$ is a rational function of degree $\le 16$, making $F_s$ a constant-coefficient linear recurrence solvable in $O(n)$!
- **Complete Derivation & Solution Sketch**:
  Either run $3 \times 3$ semi-online CDQ NTT on $[1, n]$ (6 NTTs of size $L$ per CDQ node, $\sim 80\text{ ms}$), or clear the common denominator $(1 - x^2 - x^4)^3$ of $M_{s, t}(x) = \vartheta^2 \frac{\text{poly}(x)}{1 - x^2 - x^4}$ (or use Berlekamp–Massey on the first $40$ terms) to evaluate the exact order-$\le 16$ linear recurrence in $O(n)$ time!

---

#### Problem 16: Yukicoder No. 1533 — Non-Stop Random Walk
- **Source & Link**: Yukicoder — [https://yukicoder.me/problems/no/1533](https://yukicoder.me/problems/no/1533) (Discovered by Cohort 1)
- **Difficulty Tier**: `Intermediate` | **Primary Topic**: Iteration 41 & 44 (Constant Term $[x^0] L(x)^t$ of Symmetric Laurent Polynomial $\to$ D-Finite P-Recursive Sequence)
- **Mathematical Statement & Constraints**:
  Starting at $0$ on $\mathbb{Z}$, each step moves by $d \in [-M, M]$ with $|d| \neq K$ ($1 \le K \le M \le 5$). For a walk of $N \le 10^5$ steps, compute $\sum_{0 \le i < j \le N} |\text{sign}(x_i - x_j)| \bmod 998244353$.
  - **Target Complexity**: $O(N M)$ time.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Notice $|\text{sign}(x_i - x_j)| = 1 - [x_i = x_j]$, so the problem reduces to computing the return counts $ret_t = [x^0] L(x)^t$ for $t = 0, \dots, N$, where $L(x) = \sum_{|d| \le M, |d| \neq K} x^d$.
  - *Hint 2*: Since $L(x) = L(x^{-1})$ is a polynomial of degree $M \le 5$ in $z = x + x^{-1}$, the diagonal $R(u) = \sum_{t \ge 0} ret_t u^t = [x^0] \frac{1}{1 - u L(x)}$ is algebraic of degree $\le M$, hence D-finite!
  - *Hint 3*: Compute the first $40$ terms of $ret_t$ by naive DP in $O(M \cdot 40^2)$ time, pass them to `find_p_recursive` (Section 2.6) with $r \le 5, d \le 5$, and unroll the P-recursive recurrence up to $N$ in $O(N M)$ time!
- **Complete Derivation & Solution Sketch**:
  By Cauchy's integral formula, $R(u) = \frac{1}{2\pi i} \oint \frac{dx}{x(1 - u L(x))}$ is an algebraic function over $\mathbb{Q}(u)$ of degree $\le M \le 5$, so $ret_t$ satisfies a P-recursive relation of order $r \le M$ and degree $d \le M$. Finding this recurrence via `find_p_recursive` on the first $(r+1)(d+1) + r \le 42$ terms and unrolling to $N$ runs in $< 5\text{ ms}$.
---

### Tier 3: Advanced (`Hard` — Problems 17–22)

#### Problem 17: Codeforces 932E — Team Work & The Strengthened $O(K)$ (`EI 科技`) Version
- **Source**: [Codeforces 932E (ICM Technocup 2018)](https://codeforces.com/problemset/problem/932/E) & [Elegia's `EI 科技` $O(K)$ ODE Note](https://www.luogu.com.cn/blog/EntropyIncreaser/zai-tan-binomial-sum) *(Both Cohorts)*
- **Mathematical Statement**:
  Given integers $N$ and $K$, compute the binomial-moment sum:
  $$S(N, K) = \sum_{i=1}^{N} \binom{N}{i} i^K \bmod (10^9 + 7)$$
- **Constraints**:
  - **Original Version (`CF 932E`)**: $1 \le N \le 10^9$, $1 \le K \le 5000$, modulus $10^9 + 7$. Time limit: 2.0s.
  - **Strengthened `EI 科技` Version**: $1 \le N \le 10^9$, $1 \le K \le 10^7$ (modulo a prime $p > K$, e.g., $998244353$ or $10^9 + 7$).
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Differential Operator Action & Stirling Expansion)**: Notice that $i^K = \left.\left(x \frac{d}{dx}\right)^K x^i \right|_{x=1} = \sum_{j=0}^K \left\{\begin{matrix} K \\ j \end{matrix}\right\} i^{\underline{j}}$. Using $\binom{N}{i} i^{\underline{j}} = N^{\underline{j}} \binom{N-j}{i-j}$ collapses the $N$-term sum into a $K$-term sum over $j = 0, \dots, K$. How can we evaluate all $\left\{\begin{matrix} K \\ j \end{matrix}\right\}$ in $O(K \log K)$ via NTT, or bypass Stirling numbers altogether in $O(K)$ time?
  - **Hint 2 (Structural — Taylor Truncation at $x = 1$)**: Shift the origin to $u = x - 1$, so $(1 + x)^N = (2 + u)^N$. Since $\vartheta^K = \left((1 + u) \frac{d}{du}\right)^K$ is a linear differential operator of order $K$, when evaluated at $u = 0$ ($x = 1$), any term divisible by $u^{K+1}$ vanishes identically! Thus we may replace $(2 + u)^N$ by its degree-$K$ truncation:
    $$H(u) = (2 + u)^N \bmod u^{K+1} = \sum_{j=0}^K \binom{N}{j} 2^{N-j} u^j$$
    What remains when we rewrite $H(x - 1)$ in powers of $x$?
  - **Hint 3 (Algebraic — First-Order ODE for the Truncated Polynomial & Linear Sieve)**: Differentiate $H(u) = \sum_{j=0}^K \binom{N}{j} 2^{N-j} u^j$ with respect to $u$:
    $$(2 + u) H'(u) = N H(u) - (N - K) \binom{N}{K} 2^{N-K} u^K$$
    Expanding $H(x - 1) = \sum_{m=0}^K f_m x^m$ (so $S(N, K) = \sum_{m=0}^K f_m m^K$) gives a 1-step recurrence for the auxiliary binomial sum, while $0^K, 1^K, \dots, K^K$ are computed in $O(K)$ time via Euler's linear sieve ($i^K = p^K \cdot (i/p)^K$)!
- **Full Mathematical Derivation Sketch**:
  1. **Method 1 ($O(K^2)$ Stirling Baseline for $K \le 5000$)**: Using $\vartheta^K = \sum_{j=0}^K \left\{\begin{matrix} K \\ j \end{matrix}\right\} x^j D^j$ and $D^j (1 + x)^N \big|_{x=1} = N^{\underline{j}} 2^{N-j}$:
     $$S(N, K) = \sum_{j=0}^{\min(N, K)} \left\{\begin{matrix} K \\ j \end{matrix}\right\} N^{\underline{j}} \, 2^{N-j}$$
     where $\left\{\begin{matrix} k \\ j \end{matrix}\right\} = \left\{\begin{matrix} k-1 \\ j-1 \end{matrix}\right\} + j \left\{\begin{matrix} k-1 \\ j \end{matrix}\right\}$ is precomputed in $O(K^2)$ time.
  2. **Method 2 ($O(K \log K)$ NTT Row Extraction for $K \le 2 \times 10^5$)**: By inclusion-exclusion, the $K$-th row of Stirling numbers of the second kind is the single convolution:
     $$\left\{\begin{matrix} K \\ j \end{matrix}\right\} = \sum_{i=0}^{j} \frac{(-1)^{j - i}}{(j - i)!} \cdot \frac{i^K}{i!}$$
     Convolving $A_i = \frac{i^K}{i!}$ with $B_i = \frac{(-1)^i}{i!}$ via NTT gives all $\left\{\begin{matrix} K \\ j \end{matrix}\right\}_{j=0}^K$ in $O(K \log K)$ time.
  3. **Method 3 ($O(K)$ `EI 科技` Strengthened Derivation for $K \le 10^7$, Zero NTTs!)**:
     - **Equivalence via Truncated Polynomial $H(u) = (2 + u)^N \bmod u^{K+1}$**: Since $H(x - 1) = \sum_{m=0}^K f_m x^m$ agrees with $(1 + x)^N$ to order $(x - 1)^K$, all derivatives up to order $K$ at $x = 1$ match:
       $$S(N, K) = \left. \left(x \frac{d}{dx}\right)^K H(x - 1) \right|_{x=1} = \sum_{m=0}^K f_m \cdot m^K$$
     - **Backward Recurrence on $g_m$**: Expanding $u^j = (x - 1)^j$ gives $f_m = \binom{N}{m} g_m$ where $g_m = \sum_{r=0}^{K-m} \binom{N-m}{r} 2^{N-m-r} (-1)^r$. Applying Pascal's identity $\binom{N-m}{r} = \binom{N-m-1}{r} + \binom{N-m-1}{r-1}$ (the discrete avatar of the ODE $(2+u)H'(u) = N H(u) - (N-K)\binom{N}{K}2^{N-K}u^K$) yields:
       $$g_m = g_{m+1} + (-1)^{K-m} \binom{N-m-1}{K-m} 2^{N-K-1}, \qquad g_K = 2^{N-K}$$
     - **Equivalent Forward Recurrence on $S(m)$ (Direct Binomial Inversion)**: Equivalently, substituting $\left\{\begin{matrix} K \\ j \end{matrix}\right\} = \frac{1}{j!} \sum_{i=0}^j (-1)^{j-i} \binom{j}{i} i^K$ into Method 1 and swapping sums yields:
       $$S(N, K) = \sum_{i=0}^{K} i^K \binom{N}{i} 2^{N-K} \sum_{r=0}^{K-i} \binom{N-i}{K-i-r} (-1)^{K-i-r} 2^r = 2^{N-K} \sum_{i=0}^{K} \binom{N}{i} i^K S(K - i)$$
       where $S(m) = \sum_{r=0}^{m} \binom{N - K + m}{r} (-1)^r 2^{m - r}$ satisfies the 2-term forward recurrence $S(m) = S(m - 1) + (-1)^m \binom{N - K + m - 1}{m}$ with $S(0) = 1$!
     - **Euler Linear Sieve for $i^K$**: Since $i^K$ is completely multiplicative, we evaluate $i^K \bmod p$ via binary exponentiation only on the $\pi(K) \approx \frac{K}{\ln K}$ primes $p_r \le K$ (taking $O(\frac{K}{\ln K} \log K) = O(K)$ time) and propagate $i^K = p_r^K \cdot (i / p_r)^K$ for composite $i$. Total complexity: **$O(K)$ time and $O(K)$ space**.

---

#### Problem 18: Luogu P6667 — [清华集训2016] 如何优雅地求和 (How to Sum Elegantly)
- **Source**: [Luogu P6667 (Tsinghua Training Camp 2016)](https://www.luogu.com.cn/problem/P6667) *(Both Cohorts)*
- **Mathematical Statement**:
  You are given $n, m, x$ and the point values $f(0), f(1), \dots, f(m)$ of a degree-$m$ polynomial $f(k)$. Compute the binomial expectation sum:
  $$S = \sum_{k=0}^{n} \binom{n}{k} f(k) x^k (1 - x)^{n - k} \bmod 998244353$$
- **Constraints**: $1 \le n \le 10^9$, $1 \le m \le 2 \times 10^4$, $0 \le x < 998244353$. Time limit: 1.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Newton Forward Difference Basis)**: Instead of the monomial basis $k^j$ or falling factorial basis $k^{\underline{j}}$, expand $f(k)$ in the binomial basis:
    $$f(k) = \sum_{j=0}^{m} b_j \binom{k}{j}$$
    Why does $\binom{n}{k} \binom{k}{j}$ telescope cleanly against $\sum_{k=j}^n \binom{n-j}{k-j} x^{k-j} (1-x)^{n-k}$?
  - **Hint 2 (Structural — Binomial Absorption)**: By $\binom{n}{k}\binom{k}{j} = \binom{n}{j}\binom{n-j}{k-j}$:
    $$\sum_{k=0}^{n} \binom{n}{k} \binom{k}{j} x^k (1 - x)^{n - k} = \binom{n}{j} x^j \sum_{k=j}^{n} \binom{n - j}{k - j} x^{k - j} (1 - x)^{n - k} = \binom{n}{j} x^j (x + 1 - x)^{n - j} = \binom{n}{j} x^j$$
    Thus $S = \sum_{j=0}^m b_j \binom{n}{j} x^j$!
  - **Hint 3 (Algebraic — EGF Conversion or $O(m)$ D-Finite Recurrence)**: Since $f(k) = \sum_{j=0}^m b_j \binom{k}{j}$, the EGFs satisfy $\sum_{k \ge 0} \frac{f(k)}{k!} z^k = e^z \sum_{j=0}^m \frac{b_j}{j!} z^j$. Multiply $\sum_{i=0}^m \frac{f(i)}{i!} z^i$ by $e^{-z} \bmod z^{m+1}$ using a single NTT in $O(m \log m)$ time (or use the $O(m)$ Lagrange-basis recurrence from Problem 17).
- **Full Mathematical Derivation Sketch**:
  Let $F(z) = \sum_{i=0}^m \frac{f(i)}{i!} z^i$ and $E(z) = \sum_{i=0}^m \frac{(-1)^i}{i!} z^i$. Compute $B(z) = F(z) E(z) \bmod z^{m+1}$ via one length-$2^{\lceil \log_2(2m+1) \rceil}$ NTT. Then $b_j = j! [z^j] B(z)$. Finally:
  $$S = \sum_{j=0}^{m} \left([z^j] B(z)\right) \cdot n^{\underline{j}} \cdot x^j \bmod 998244353$$
  Total time: $O(m \log m)$ (or $O(m)$ via direct Taylor truncation of $(x + (1-x)e^t)^n$).

---

#### Problem 19: Codeforces 1097G — Vladislav and a Great Legend
- **Source**: [Codeforces 1097G (Hello 2019)](https://codeforces.com/problemset/problem/1097/G) *(Cohort 1 Blind Spot)*
- **Mathematical Statement**:
  Given a tree $T = (V, E)$ with $n$ vertices and an integer $k$, for every non-empty subset of vertices $X \subseteq V$, let $f(X)$ be the number of edges in the minimal connected subtree (Steiner tree) spanning $X$. Compute:
  $$\sum_{\emptyset \neq X \subseteq V} f(X)^k \bmod (10^9 + 7)$$
- **Constraints**: $2 \le n \le 10^5$, $1 \le k \le 200$. Time limit: 3.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Falling Factorial / Binomial Decomposition via $\vartheta^k$)**: Just as $\vartheta^k e^x = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} x^j e^x$, rewrite the $k$-th power in the binomial basis:
    $$f(X)^k = \sum_{j=0}^{k} \left\{\begin{matrix} k \\ j \end{matrix}\right\} j! \binom{f(X)}{j} = \left. \left((1 + y)\frac{d}{dy}\right)^k (1 + y)^{f(X)} \right|_{y=0}$$
    Now $\binom{f(X)}{j}$ counts the number of ways to choose $j$ edges inside the Steiner tree of $X$.
  - **Hint 2 (Structural — Truncated FPS over the Tree)**: If we maintain for each subtree rooted at $u$ the ordinary generating function $P_u(y) = \sum_{j=0}^k dp[u][j] y^j \bmod y^{k+1}$ summing $(1 + y)^{\text{active edges}}$ over non-empty subsets $X \subseteq \text{subtree}(u)$, what happens when we extend a subtree $v$ across its parent edge $(u, v)$?
  - **Hint 3 (Algebraic — 2-Sparse Edge Transition & Bounded Tree Knapsack)**: Extending across edge $(u, v)$ multiplies the non-empty subtree polynomial $P_v(y)$ by the **2-sparse polynomial** $(1 + y)$: $\widetilde{P}_v(y) = (1 + y) P_v(y) \bmod y^{k+1}$. Merging children of $u$ is polynomial multiplication $P_u(y) \leftarrow P_u(y) (1 + \widetilde{P}_v(y)) \bmod y^{k+1}$, capped at $\min(\text{sz}[u], k)$.
- **Full Mathematical Derivation Sketch**:
  By linearity of expectation / summation,
  $$\sum_{\emptyset \neq X \subseteq V} f(X)^k = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} j! [y^j] \sum_{\emptyset \neq X \subseteq V} (1 + y)^{f(X)}$$
  In the tree DP, for each vertex $u$, maintain $P_u(y) \bmod y^{\min(\text{sz}[u], k)+1}$. When attaching child $v$ to $u$, edge $(u, v)$ belongs to the Steiner tree iff $X \cap \text{subtree}(v) \neq \emptyset$ AND $X \setminus \text{subtree}(v) \neq \emptyset$. We count all valid pairs by multiplying $\widetilde{P}_v(y) = (1 + y) P_v(y)$ into $P_u(y)$ and subtracting the single-branch overcounts $(y) P_v(y)$ from the global accumulator when $X \subseteq \text{subtree}(v)$ has no vertices outside $\text{subtree}(v)$. By the classic tree-knapsack LCA pair analysis, capping degrees at $\min(\text{sz}[u], k)$ yields total time **$O(n k)$**!

---

#### Problem 20: AtCoder ABC 230 Ex — Bullseye
- **Source**: [AtCoder Beginner Contest 230, Problem Ex](https://atcoder.jp/contests/abc230/tasks/abc230_h) *(Cohort 1 Blind Spot)*
- **Mathematical Statement**:
  We have bags of available positive integer weights $w_1, w_2, \dots, w_k \in \{1, \dots, W\}$. A "valid nested bag configuration" of total weight $n$ consists of a root bag of some allowed weight $w_i$ containing a **multiset** of zero or more valid nested bag configurations whose weights sum to $n - w_i$ (two configurations are identical if one can be obtained by permuting the bags inside any bag). For each $n = 2, 3, \dots, W$, find the number of valid configurations of weight $n$ modulo $998244353$.
- **Constraints**: $2 \le W \le 2 \times 10^5$, $1 \le w_i \le W$. Time limit: 4.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Pólya Multiset Operator)**: Let $B(x) = \sum_{n=1}^W b_n x^n$ be the OGF of valid nested bags, and let $W(x) = \sum_{i=1}^k x^{w_i}$ be the OGF of allowed single-bag weights. A bag of weight $w_i$ containing an unordered multiset of smaller bags corresponds to the Euler product / Pólya $\text{MSET}$ operator:
    $$B(x) = W(x) \prod_{m \ge 1} \frac{1}{(1 - x^m)^{b_m}} = W(x) \exp\!\left(\sum_{j \ge 1} \frac{B(x^j)}{j}\right)$$
  - **Hint 2 (Structural — Differential Reduction of the Online Exp)**: Define $G(x) = \sum_{j \ge 1} \frac{B(x^j)}{j}$ and $E(x) = \exp(G(x))$, so that $B(x) = W(x) E(x)$. Notice that $b_n = [x^n] B(x)$ depends only on $e_0, \dots, e_{n-1}$ because $[x^0] W(x) = 0$! And how does $E(x)$ depend on $G(x)$? Via the linear ODE:
    $$E'(x) = G'(x) E(x) \implies n e_n = \sum_{m=1}^{n} (m g_m) e_{n-m}$$
  - **Hint 3 (Algebraic — Dual `RelaxedConvolution` + Harmonic Sieve)**: Once $e_{n-1}$ becomes known at step $n-1$:
    1. Feed $e_{n-1}$ and $w_n$ into a **first `RelaxedConvolution`** computing $B(x) = W(x) E(x)$ to immediately obtain $b_n = [x^n] (W(x) E(x))$.
    2. Use $b_n$ to update $m g_m = \sum_{d \mid m} d \cdot b_d$ for all multiples $m = j \cdot n \le W$ (which takes $O(W \log W)$ total work across all $n$).
    3. Feed $n g_n$ and $e_{n-1}$ into a **second `RelaxedConvolution`** computing $E'(x) = G'(x) E(x)$ to obtain $n e_n$, hence $e_n = \frac{1}{n}[x^{n-1}](G' E)$!
- **Full Mathematical Derivation Sketch**:
  At each step $n = 1, 2, \dots, W$:
  - `rc_B.next(w_n, e_{n-1})` computes $b_n = \sum_{j=1}^n w_j e_{n-j}$ (since $w_0 = 0$).
  - Add $n \cdot b_n$ to an array `mg[j * n]` for $j = 1, 2, \dots, \lfloor W / n \rfloor$.
  - Now `mg[n]` $= n g_n = [x^{n-1}] G'(x)$ is fully known!
  - `rc_E.next(mg[n], e_{n-1})` computes $[x^{n-1}] (G'(x) E(x)) = n e_n$. Multiply by $\text{inv}[n]$ to obtain $e_n$.
  This solves the entire coupled Pólya system in **$O(W \log^2 W)$** time using two 30-line `RelaxedConvolution` instances, completely avoiding Newton iteration on $\exp$!

---

#### Problem 21: AtCoder ABC 260 Ex — Colorfulness
- **Source**: [AtCoder Beginner Contest 260, Problem Ex](https://atcoder.jp/contests/abc260/tasks/abc260_h) *(Cohort 2 Blind Spot)*
- **Mathematical Statement**:
  There are $N$ balls where ball $i$ has color $a_i$. For a permutation $P = (P_1, \dots, P_N)$ of $(1, \dots, N)$, define its *colorfulness* $c(P)$ to be the number of contiguous same-color runs in $(a_{P_1}, \dots, a_{P_N})$ (i.e., $N$ minus the number of indices $1 \le i < N$ with $a_{P_i} = a_{P_{i+1}}$). Given $M$, compute for every $m = 1, 2, \dots, M$:
  $$S_m = \sum_{P \in S_N} c(P)^m \bmod 998244353$$
- **Constraints**: $1 \le N, M \le 2.5 \times 10^5$. Time limit: 5.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Sparse Inclusion-Exclusion per Color)**: Suppose color $r$ appears $k_r$ times ($\sum_r k_r = N$). If we contract $j_r$ adjacent pairs of color $r$ into blocks, there are $\binom{k_r - 1}{j_r} \frac{k_r!}{(k_r - j_r)!}$ ways to form the $k_r - j_r$ ordered chains of color $r$. Define the polynomial for color $r$:
    $$Q_r(x) = \sum_{j=0}^{k_r - 1} \binom{k_r - 1}{j} \frac{k_r!}{(k_r - j)!} x^j$$
  - **Hint 2 (Structural — Product Tree + Binomial Taylor Shift)**: Let $Q(x) = \prod_r Q_r(x) = \sum_{j=0}^{N-1} q_j x^j$, computed via a divide-and-conquer product tree in $O(N \log^2 N)$ time. Then $a_j = (N - j)! q_j$ counts configurations with at least $j$ forced same-color adjacencies. By binomial inclusion-exclusion, the polynomial of exact adjacencies $w_k$ is the Taylor shift $W(x) = \sum_{j=0}^{N-1} a_j (x - 1)^j$.
  - **Hint 3 (Algebraic — Power Sum Evaluation via Log-Derivative / Rational Sum)**: Once $w_k$ (number of permutations with colorfulness $v = N - k$) is known for $v = 1, \dots, N$, we need $S_m = \sum_{v=1}^N w_{N-v} v^m$ for $m = 1, \dots, M$. Observe that:
    $$\sum_{m \ge 0} S_m x^m = \sum_{v=1}^{N} \frac{w_{N-v}}{1 - v x}$$
    Compute $\sum_{v=1}^N \frac{w_{N-v}}{1 - v x} = \frac{A(x)}{B(x)}$ via a binary product tree of $2 \times 2$ fraction merges in $O(N \log^2 N)$ time, followed by one polynomial inversion $A(x) B(x)^{-1} \bmod x^{M+1}$!
- **Full Mathematical Derivation Sketch**:
  1. Group balls by color into frequencies $k_1, \dots, k_C$ with $\sum k_r = N$. Construct $Q_r(x)$ of degree $k_r - 1$ and multiply all $Q_r(x)$ using a min-heap / divide-and-conquer tree in $O(N \log^2 N)$ time.
  2. Set $a_j = (N - j)! [x^j] Q(x)$ and apply one NTT convolution to compute the Taylor shift $W(x) = A(x - 1) = \sum_{k=0}^{N-1} w_k x^k$.
  3. Set $c_v = w_{N-v}$ for $v = 1, \dots, N$. Merge the fractions $\frac{c_v}{1 - v x}$ via divide-and-conquer into $\frac{P(x)}{R(x)}$ in $O(N \log^2 N)$ time, and extract $[x^m] P(x) R(x)^{-1} \bmod x^{M+1}$ for $m = 1, \dots, M$ in $O(M \log M)$ time.

---

#### Problem 22: AtCoder ABC 300 Ex — Fibonacci: Revisited & ARC 138 E — Decreasing Subsequence
- **Source**: [AtCoder Beginner Contest 300, Problem Ex](https://atcoder.jp/contests/abc300/tasks/abc300_h) & [AtCoder Regular Contest 138, Problem E](https://atcoder.jp/contests/arc138/tasks/arc138_e) *(Cohort 2 Blind Spots)*
- **Mathematical Statement**:
  - **Part A (ABC 300 Ex)**: Define the generalized $K$-step Fibonacci sequence by $a_n = 1$ for $0 \le n < K$, and $a_n = a_{n-1} + a_{n-2} + \dots + a_{n-K}$ for $n \ge K$. Given $K$ and $N$, compute $a_N \bmod 998244353$.
  - **Part B (ARC 138 E)**: Count sequences $A = (A_1, \dots, A_N)$ with $0 \le A_i \le i$ containing no decreasing subsequence of length $K$ of positive elements, modulo $998244353$.
- **Constraints**:
  - **Part A**: $2 \le K \le 2.5 \times 10^5$, $1 \le N \le 10^{18}$. Time limit: 3.0s.
  - **Part B**: $2 \le K \le N \le 5000$. Time limit: 3.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — 3-Sparse Denominator Compression for ABC 300 Ex)**: The denominator of the OGF $A(x) = \frac{P(x)}{Q(x)}$ in Part A is $Q(x) = 1 - x - x^2 - \dots - x^K$, which is dense ($K + 1$ nonzero terms). What happens if you multiply both numerator and denominator by $(1 - x)$?
  - **Hint 2 (Structural — Dual-Regime Sparsity vs Bostan–Mori)**: Multiplying by $(1 - x)$ transforms $Q(x)$ into the **3-sparse polynomial**:
    $$\widetilde{Q}(x) = (1 - x) Q(x) = 1 - 2x + x^{K+1}$$
    - **Regime 1 ($N$ moderate, e.g. $N \le 10^7$ or all $a_0 \dots a_N$ needed)**: `SparseFPS::inv` on $\widetilde{Q}(x) = 1 - 2x + x^{K+1}$ computes $a_0, \dots, a_N$ in **$O(N)$ time** via $c_n = 2 c_{n-1} - c_{n-K-1}$!
    - **Regime 2 ($N \le 10^{18}$ huge)**: Either run Bostan–Mori on $P(x)/Q(x)$ in $O(K \log K \log N)$ time, or compute $x^N \bmod (x^{K+1} - 2x^K + 1)$ using **3-sparse polynomial division** at each step of binary exponentiation in **$O(K \log N)$ time** (without NTT)!
  - **Hint 3 (Algebraic — Semi-Online Block Convolution for ARC 138 E)**: In Part B, Greene's theorem / RSK tableau insertion reduces the DP to $N / K$ block transitions of size $K$, where each block transition is a binomial convolution accelerated from $O(N^3)$ to $O(N^2)$ or $O(\frac{N^2}{K} \log K)$.
- **Full Mathematical Derivation Sketch (ABC 300 Ex $O(K \log N)$ 3-Sparse Kitamasa / Polynomial Mod)**:
  Since $a_{n} - 2 a_{n-1} + a_{n-K-1} = 0$ for all $n \ge K + 1$, the characteristic polynomial of the recurrence after multiplying by $(x - 1)$ is $M(x) = x^{K+1} - 2x^K + 1$, which has only **3 nonzero terms**! During binary exponentiation to compute $R(x) = x^N \bmod (x^{K+1} - 2x^K + 1)$:
  - Squaring $R(x)$ of degree $\le K$ takes one NTT of length $2^{\lceil \log_2(2K+2) \rceil}$ in $O(K \log K)$ time.
  - Reducing a degree-$2K$ polynomial $S(x) = \sum_{i=0}^{2K} s_i x^i$ modulo $x^{K+1} - 2x^K + 1$ does **not** require polynomial inverse: simply sweep $i = 2K, 2K-1, \dots, K+1$ from top to bottom, adding $2 s_i$ to $s_{i-1}$ and subtracting $s_i$ from $s_{i-K-1}$ in **$O(K)$ time**!
  This hybrid (NTT squaring + $O(K)$ 3-sparse modular reduction) runs in $O(K \log K \log N)$ with less than $1/3$ the NTT calls of general Bostan–Mori!

---

### Tier 4: Mastery (`Mastery` — Problems 23–34)

#### Problem 23: LOJ #6538 / Luogu P5293 / P6597 — 烷基计数 加强版 加强版 (Alkyl Radical Enumeration)
- **Source**: [LibreOJ #6538](https://loj.ac/p/6538) / [Luogu P6597 (烯烃计数)](https://www.luogu.com.cn/problem/P6597) *(Both Cohorts)*
- **Mathematical Statement**:
  Count the number of rooted ternary trees (carbon-hydrogen alkyl radicals $C_n H_{2n+1}$) with $n$ internal nodes (carbon atoms) for all $n = 0, 1, \dots, N$ modulo $998244353$, where each carbon atom has at most $3$ child subtrees and permutations of the 3 child subtrees are considered equivalent. By Pólya's Enumeration Theorem for the symmetric group $S_3$ with cycle index $Z(S_3; s_1, s_2, s_3) = \frac{1}{6}(s_1^3 + 3 s_1 s_2 + 2 s_3)$, the OGF $F(x) = \sum_{n=0}^N f_n x^n$ satisfies:
  $$F(x) = 1 + \frac{x}{6}\Big(F(x)^3 + 3 F(x) F(x^2) + 2 F(x^3)\Big) \pmod{x^{N+1}}$$
- **Constraints**: $1 \le N \le 10^5$. Time limit: 1.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Newton Iteration vs. Chained Relaxed Convolution)**: One can solve $\Phi(F) = F - 1 - \frac{x}{6}(F^3 + 3 F(x)F(x^2) + 2 F(x^3)) = 0$ via Newton's method $F \leftarrow F - \frac{\Phi(F)}{1 - \frac{x}{2}(F^2 + F(x^2))}$ in $O(N \log N)$ time, requiring a full polynomial inversion template. Can we instead solve it **online in 12 lines of code** without polynomial inverse?
  - **Hint 2 (Structural — Factoring the Cubic into Two Bilinear Products)**: Notice the shift $x$ in front of the bracket! To compute $f_n = [x^n] F(x)$ for $n \ge 1$, we only need $[x^{n-1}] \big(F(x)^3 + 3 F(x) F(x^2) + 2 F(x^3)\big)$, which depends SOLELY on $f_0, f_1, \dots, f_{n-1}$! Rewrite the bracket as:
    $$F(x)^3 + 3 F(x) F(x^2) + 2 F(x^3) = F(x) \cdot \Big(\underbrace{F(x)^2}_{S(x)} + 3 F(x^2)\Big) + 2 F(x^3)$$
  - **Hint 3 (Algebraic — Two Parallel `RelaxedConvolution` Instances)**:
    - Instance 1 (`rc_S`): Computes $S(x) = F(x) \cdot F(x)$ online. At step $m = n - 1$, `s_m = rc_S.next(f_m, f_m)`.
    - Instance 2 (`rc_P`): Computes $P(x) = F(x) \cdot (S(x) + 3 F(x^2))$ online. At step $m = n - 1$, let $h_m = s_m + 3 [2 \mid m] f_{m/2}$, and call `p_m = rc_P.next(f_m, h_m)`.
    - Then $f_n = \frac{1}{6} \big(p_{n-1} + 2 [3 \mid (n-1)] f_{(n-1)/3}\big)$!
- **Full Mathematical Derivation Sketch**:
  - Base case: $f_0 = 1$.
  - Loop $m = 0, 1, \dots, N - 1$:
    1. `long long s_m = rc_S.next(f[m], f[m]);` (gives $[x^m] F(x)^2$).
    2. `long long h_m = (s_m + (m % 2 == 0 ? 3LL * f[m / 2] : 0)) % MOD;` (gives $[x^m] (F(x)^2 + 3 F(x^2))$).
    3. `long long p_m = rc_P.next(f[m], h_m);` (gives $[x^m] F(x)(F(x)^2 + 3 F(x^2))$).
    4. `long long c3 = (m % 3 == 0 ? 2LL * f[m / 3] : 0);`
    5. `f[m + 1] = (p_m + c3) % MOD * inv6 % MOD;`
  Total time: $O(N \log^2 N)$ with tiny constant factor ($\approx 120\text{ ms}$ for $N = 10^5$), zero polynomial inversions, and 12 lines of problem logic!

---

#### Problem 24: UOJ #514 — 【UR #19】通用测评号 (Universal Judge ID)
- **Source**: [Universal Online Judge (UOJ) #514 (UOJ Round #19)](https://uoj.ac/problem/514) *(Cohort 2 Blind Spot — Flagship `EI 科技` Truncated Exponential Derivative)*
- **Mathematical Statement**:
  There are $n$ initially empty fuel tanks ($c_1 = \dots = c_n = 0$). In each step, one tank $i \in \{1, \dots, n\}$ is chosen uniformly at random and its fuel increases by $1$. The process stops as soon as **every** tank has at least $b$ units of fuel ($\min_i c_i \ge b$). At the moment the process stops, how many tanks have at least $a$ units of fuel ($c_i \ge a$, where $a > b$), in expectation? Compute the answer modulo $998244353$.
- **Constraints**: $1 \le n \le 250$, $1 \le b < a \le 250$. Time limit: 2.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Poissonization / EGF Stopping Time)**: By symmetry, the expected number of tanks with $\ge a$ fuel at stopping time $T = \min\{t : \forall i, c_i(t) \ge b\}$ equals $n$ times the probability that tank $1$ has $\ge a$ fuel at time $T$. Equivalently, under Poissonization with rate $1$ per tank (total rate $n$), a tank has $< m$ items at Poisson time $x$ with probability $e^{-x} S_{<m}(x)$, where:
    $$S_{<m}(x) = \sum_{j=0}^{m-1} \frac{x^j}{j!}$$
  - **Hint 2 (Structural — The `EI 科技` Miracle Derivative of the Truncated Exponential)**: Consider the probability generating integral. What is the derivative of $e^{-x} S_{<m}(x)$?
    $$S_{<m}'(x) = S_{<m}(x) - \frac{x^{m-1}}{(m-1)!} \implies \frac{d}{dx}\Big(e^{-x} S_{<m}(x)\Big) = -e^{-x} \frac{x^{m-1}}{(m-1)!}$$
    The entire $m$-term polynomial $S_{<m}(x)$ collapses upon differentiation into a **single monomial** $-\frac{x^{m-1}}{(m-1)!}$!
  - **Hint 3 (Algebraic — Dimension Collapse from $O(n^3 a^2)$ to $O(n^2 a)$)**: Let $F(x)$ be the EGF of valid configurations. Integrating by parts against the stopping event (the exact moment the last tank reaches $b$, which has density $-\frac{d}{dx}\big(1 - e^{-x} S_{<b}(x)\big)^{n-1}$), we must evaluate integrals of the form:
    $$\int_0^\infty e^{-kx} \big(S_{<a}(x) - S_{<b}(x)\big) \big(S_{<a}(x)\big)^{i} \big(S_{<b}(x)\big)^{j} dx$$
    Naive expansion of $S_{<a}(x)^i S_{<b}(x)^j$ produces degree $n a$, taking $O(n^3 a^2)$. Instead, define $P_{k, m}(x) = \big(S_{<a}(x) - S_{<b}(x)\big) S_{<b}(x)^{k-1}$ and differentiate!
- **Full Mathematical Derivation Sketch**:
  By conditioning on how many of the other $n - 1$ tanks fail to reach $a$ before everyone reaches $b$, the problem reduces via inclusion-exclusion to computing the coefficients of:
  $$H_k(x) = \big(S_{<a}(x) - S_{<b}(x)\big) \cdot S_{<a}(x)^{k-1}$$
  If we multiplied $S_{<a}(x)$ (degree $a - 1$) $n$ times, it would take $O(n^2 a^2)$ or $O(n^3 a^2)$. Instead, apply $S_{<a}'(x) = S_{<a}(x) - \frac{x^{a-1}}{(a-1)!}$ and $S_{<b}'(x) = S_{<b}(x) - \frac{x^{b-1}}{(b-1)!}$ to $H_k(x)$:
  $$H_k'(x) = k H_k(x) - \frac{x^{a-1}}{(a-1)!} S_{<a}(x)^{k-1} + \frac{x^{b-1}}{(b-1)!} S_{<a}(x)^{k-1} - (k-1) \frac{x^{a-1}}{(a-1)!} H_{k-1}(x)$$
  Notice that on the right-hand side, $S_{<a}(x)^{k-1}$ and $H_{k-1}(x)$ are multiplied only by **single monomials** $x^{a-1}$ and $x^{b-1}$! Thus, once we precompute the single power tower $A_k(x) = S_{<a}(x)^k$ for $k = 0, \dots, n - 1$ in $O(n^2 a \log(na))$ (or via the even simpler ODE $A_k'(x) = k A_k(x) - k \frac{x^{a-1}}{(a-1)!} A_{k-1}(x)$ in **$O(n^2 a)$** time with zero NTTs!), every coefficient of $A_k(x)$ and $H_k(x)$ is extracted by a 3-term recurrence in $O(1)$ time per state!
  - **Complexity**: **$O(n^2 a)$** arithmetic operations (down from $O(n^3 a^2)$), running in $< 50\text{ ms}$!

---

#### Problem 25: Codeforces 1349D — Slime and Biscuits
- **Source**: [Codeforces 1349D (CF Round 641 Div. 1)](https://codeforces.com/problemset/problem/1349/D) *(Cohort 1 & Cohort 2 Blind Spot)*
- **Mathematical Statement**:
  There are $m$ players holding $a_1, a_2, \dots, a_m$ biscuits with total sum $S = \sum_{i=1}^m a_i$. At each step, one biscuit is chosen uniformly at random (probability $1/S$) from all $S$ biscuits and transferred from its current owner to one of the other $m - 1$ players chosen uniformly at random (probability $1/(m-1)$). Compute the expected number of steps until a single player holds all $S$ biscuits, modulo $998244353$.
- **Constraints**: $2 \le m \le 10^5$, $1 \le S = \sum_{i=1}^m a_i \le 3 \times 10^5$. Time limit: 2.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Optional Stopping Theorem / Potential Function $f(x)$)**: By martingale stopping time theory, seek a potential function $f(x)$ such that $\mathbb{E}[\Delta \sum_{i=1}^m f(a_i)] = -1$ at every step before absorption at $a_i = S$. Then:
    $$\mathbb{E}[T] = f(S) + (m - 1) f(0) - \sum_{i=1}^{m} f(a_i)$$
  - **Hint 2 (Structural — Order Reduction via First Difference $g(x) = f(x+1) - f(x)$)**: Requiring $\mathbb{E}[\Delta \sum_{i=1}^m f(a_i)] = -1$ independent of the partition $(a_1, \dots, a_m)$ forces the second-order difference equation on $f(x)$ to telescope when summed over $i = 1, \dots, m$. Substituting the first difference $g(x) = f(x+1) - f(x)$ reduces the second-order equation to a **first-order linear P-recursive recurrence**!
  - **Hint 3 (Algebraic — Exact First-Order P-Recursive Recurrence)**: Setting each player's drift to $-\frac{x}{S}$ gives:
    $$(S - x) g(x) = x(m - 1) g(x - 1) - S(m - 1), \qquad g(0) = -(m - 1)$$
- **Full Mathematical Derivation Sketch**:
  A player with $x$ biscuits gains a biscuit with probability $\frac{S - x}{S(m - 1)}$ and loses a biscuit with probability $\frac{x}{S}$. For $\sum_{i=1}^m \mathbb{E}[\Delta f(a_i)] = -1$, we set each player's drift so that summing over $\sum_{i=1}^m a_i = S$ yields $-1$:
  $$\frac{x}{S}\big(f(x - 1) - f(x)\big) + \frac{S - x}{S(m - 1)}\big(f(x + 1) - f(x)\big) = -\frac{x}{S} + \frac{S - x}{S(m - 1)} g(0) \cdot \frac{0}{1}$$
  Specifically, requiring $\frac{S - x}{S(m-1)} g(x) - \frac{x}{S} g(x-1) = -\frac{x}{S} - \frac{S - x}{S}$ (which sums across the $m$ players to $-\frac{S}{S} - \frac{(m-1)S}{S}$ after normalizing by $m-1$) yields $g(0) = f(1) - f(0) = -(m - 1)$ and:
  $$(S - x) g(x) = x(m - 1) g(x - 1) - S(m - 1) \quad (1 \le x < S)$$
  Since $S - x \not\equiv 0 \pmod{998244353}$ for $1 \le x < S$, we precompute inverses of $1, \dots, S$ in $O(S)$ time, compute $g(0), \dots, g(S-1)$, prefix-sum $f(x) = \sum_{j=0}^{x-1} g(j)$ (with $f(0) = 0$), and output $f(S) - \sum_{i=1}^m f(a_i)$ in **$O(S)$ time**!

---

#### Problem 26: Codeforces 1479E — School Clubs
- **Source**: [Codeforces 1479E (CF Round 700 Div. 1)](https://codeforces.com/problemset/problem/1479/E) *(Cohort 2 Blind Spot)*
- **Mathematical Statement**:
  There are $S$ students partitioned into $m$ clubs of sizes $a_1, a_2, \dots, a_m$ ($\sum_{i=1}^m a_i = S$). At each step, one student is chosen uniformly at random (probability $1/S$): with probability $1/2$, that student leaves their club to form a new club of size $1$; with probability $1/2$, that student's entire club merges with another student's club (chosen uniformly at random among all $S$ students). Find the expected number of steps until a single club contains all $S$ students, modulo $998244353$.
- **Constraints**: $1 \le m \le 1000$, $1 \le S = \sum_{i=1}^m a_i \le 10^9$ ($S < 998244353$). Time limit: 4.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Martingale Potential $f(x)$ Over Club Sizes)**: Seek a potential function $f(x)$ with $f(0) = 0$ such that $\mathbb{E}[\Delta \sum_{\text{clubs } c} f(|c|)] = -1$ at every step. Notice that the number of clubs can change dynamically, which is why $f(0) = 0$ is essential!
  - **Hint 2 (Structural — Reduction to a Homogeneous First-Order Recurrence)**: Imposing $\mathbb{E}[\Delta \sum f(a_i)] = -1$ independent of the partition $(a_1, \dots, a_m)$ forces the first difference $d_x = f(x+1) - f(x)$ to satisfy a **homogeneous** first-order P-recursive recurrence!
  - **Hint 3 (Algebraic — Hypergeometric Product & $O(\sqrt{S} \log S)$ Evaluation)**: Show that $d_x$ satisfies:
    $$(S - x) d_x = (2S - x - 1) d_{x-1}, \qquad d_0 = -2$$
    so $d_x = -2 \prod_{j=1}^x \frac{2S - j}{S - j}$, and $f(y) = \sum_{x=0}^{y-1} d_x$ can be evaluated for all $a_1, \dots, a_m$ sorted in $O(\sqrt{S} \log S)$ time via Bostan–Mori / baby-step giant-step matrix blocks (or in $O(S)$ when $S$ is small)!
- **Full Mathematical Derivation Sketch**:
  A club of size $x$ changes size if a student inside it splits off (probability $\frac{x}{2S}$, changing $f(x) \to f(x-1) + f(1)$) or if a merge involves this club. Imposing $\sum_i \mathbb{E}[\Delta f(a_i)] = -1$ for all partitions of $S$ yields the second-order difference equation:
  $$x(3S - 2x) f(x) - x(2S - x) f(x-1) - x(S - x) f(x+1) = 0 \quad (x \ge 1)$$
  with $f(0) = 0, f(1) = -2$. Substituting $d_x = f(x+1) - f(x)$ cancels $f(x)$ and gives the homogeneous first-order recurrence:
  $$(S - x) d_x = (2S - x) d_{x-1} \quad \text{(shifted index: } d_x = \frac{2S - x}{S - x} d_{x-1}\text{)}, \qquad d_0 = f(1) - f(0) = -2$$
  Maintaining the numerator and denominator of the partial sums $f(y) = \sum_{x=0}^{y-1} d_x$ via a $2 \times 2$ polynomial transition matrix $M(x) = \begin{pmatrix} 2S - x & 0 \\ 2S - x & S - x \end{pmatrix}$ and applying baby-step giant-step multipoint evaluation computes $f(a_1), \dots, f(a_m), f(S)$ in $O(\sqrt{S} \log S + m \log^2 m)$ time!

---

#### Problem 27: Codeforces 1349F2 — Slime and Sequences (Hard Version)
- **Source**: [Codeforces 1349F2 (CF Round 641 Div. 1)](https://codeforces.com/problemset/problem/1349/F2) *(Cohort 1 Blind Spot)*
- **Mathematical Statement**:
  A sequence of length $n$ of positive integers is *good* if whenever integer $k > 1$ appears in the sequence, $k - 1$ appears at least once before the last occurrence of $k$. For each $k = 1, 2, \dots, n$, compute the total number of occurrences of $k$ across all good sequences of length $n$, modulo $998244353$.
- **Constraints**: $1 \le n \le 10^5$. Time limit: 3.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Bijection to Permutations & Eulerian Numbers)**: There is a famous bijection between good sequences of length $n$ and permutations $\pi \in S_n$ (by reading runs between ascents), under which the occurrences of $k$ reduce to summing over Eulerian numbers $\left\langle \begin{matrix} m \\ j \end{matrix} \right\rangle$. The bivariate EGF of Eulerian numbers is:
    $$F(x, y) = \sum_{m \ge 0} \sum_{j \ge 0} \left\langle \begin{matrix} m \\ j \end{matrix} \right\rangle \frac{x^m}{m!} y^j = \frac{1 - y}{e^{(y - 1)x} - y}$$
  - **Hint 2 (Structural — Column Extraction via Change of Variables)**: Collecting terms across all subtree lengths reduces the answer for each $k$ to extracting coefficients $[x^n y^k]$ from $\frac{1}{(1 - x) F(x, y)}$ or equivalently extracting $[u^m]$ from powers of $\phi(u) = \frac{u}{e^u - 1}$ and $\frac{1}{1 - x(e^u - 1)/u}$.
  - **Hint 3 (Algebraic — Double-Pole Singularity Subtraction in Lagrange Inversion)**: Applying the bivariate Lagrange inversion substitution $w = 1 - \frac{u}{\ln(1 + u)}$ introduces a rational singularity with a **double pole** at $w = 1$:
    $$G(w) = \frac{H(w)}{(1 - w)^2}$$
    Before inverting $1 - w \bmod w^{n+1}$, subtract the principal part $\frac{H(1)}{(1 - w)^2} + \frac{-H'(1)}{1 - w}$ so that the numerator becomes divisible by $(1 - w)^2$!
- **Full Mathematical Derivation Sketch**:
  Let $H(u) = \frac{u}{\ln(1 + u)} = 1 + \frac{u}{2} - \frac{u^2}{12} + \dots$, and let $P(u) = 1 - H(u)$ have valuation $1$ ($[u^1] P(u) = -1/2 \neq 0$). By Lagrange Inversion, extracting $[u^m] A(u) P(u)^{-k}$ for all $k = 1, \dots, n$ simultaneously is equivalent to computing the compositional inverse $Q(w) = P^{\langle -1 \rangle}(w)$ and evaluating:
  $$\sum_{m=0}^n c_m [u^m] P(u)^{-k} = [w^k] \mathcal{L}(Q(w))$$
  where the transformed rational expression has a double pole at $w = 1$. Expanding around $w = 1$ via L'Hôpital's rule / first two Taylor derivatives removes the $(1 - w)^{-2}$ pole and yields all $n$ answers in $O(n \log n)$ time.

---

#### Problem 28: UOJ #450 — 【集训队作业2018】复读机 (Repeater)
- **Source**: [Universal Online Judge (UOJ) #450 (2018 IOI National Training Camp Homework)](https://uoj.ac/problem/450) *(Cohort 1 & Cohort 2 — `Mastery` Tier, Iteration 44 / 96 Bivariate Euler PDE + Roots of Unity Filter)*
- **Mathematical Statement**:
  A repeater broadcasts a sequence of length $n$ over an alphabet of $k$ distinct machine types $\{1, 2, \dots, k\}$. Because of a hardware quirk, a sequence of length $n$ is valid if and only if the number of occurrences of **each** machine type $i \in \{1, \dots, k\}$ is a multiple of $d$ (where $d \in \{1, 2, 3\}$). Compute the number of valid length-$n$ sequences modulo the prime $p = 19491001$:
  $$\text{Ans} = n! [z^n] \left( \sum_{m \ge 0} \frac{z^{d m}}{(d m)!} \right)^k \pmod{19491001}$$
- **Constraints**:
  - $1 \le n \le 10^9$, $1 \le k \le 5 \times 10^5$, $d \in \{1, 2, 3\}$, modulus $p = 19491001$ (prime, with $p - 1 = 19491000 = 2^3 \cdot 3^2 \cdot 5^3 \cdot 2165$, so $3 \mid (p - 1)$ and primitive $3$-rd roots of unity $\omega \in \mathbb{F}_p$ exist!).
  - Subtask constraints for $d = 3$: $k \le 1000$ (or $k \le 2000$), allowing $O(k^2)$ or $O(k^2 \log n)$ time.
  - Time limit: 1.0s. Memory limit: 256 MB.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Roots of Unity Filter on the EGF)**: By the roots-of-unity filter, the inner EGF for a single machine type is:
    $$E_d(z) = \sum_{m \ge 0} \frac{z^{d m}}{(d m)!} = \frac{1}{d} \sum_{r=0}^{d-1} e^{\omega^r z}$$
    where $\omega$ is a primitive $d$-th root of unity modulo $p = 19491001$ ($\omega = 7^{(p-1)/3} \bmod p$ for $d = 3$). Why does $n! [z^n] e^{\alpha z} = \alpha^n$ immediately solve $d = 1$ in $O(\log n)$ and $d = 2$ in $O(k \log n)$, and why does naive multinomial expansion for $d = 3$ take $O(k^2)$?
  - **Hint 2 (Structural — Cyclotomic Basis Reduction & Bivariate Laurent Polynomial)**: If a similar problem asks for $d = 4$ or $d = 6$, or if we expand $\big(1 + e^z + e^{\omega z} + e^{\omega^2 z}\big)^k$, notice that in the cyclotomic ring $\mathbb{Z}[\omega]$ (where $1 + \omega + \omega^2 = 0$, so $\omega^2 = -1 - \omega$), every linear combination $a \cdot 1 + b \cdot \omega + c \cdot \omega^2 = (a - c) + (b - c) \omega$ lives in a **2-dimensional** lattice $(i, j) \in [-k, k]^2$ rather than a 3-dimensional one! Setting $x = e^z$ and $y = e^{\omega z}$, we have $e^{\omega^2 z} = e^{(-1-\omega)z} = x^{-1} y^{-1}$.
  - **Hint 3 (Algebraic — Bivariate Euler Homogeneous PDE for $P(x, y) = (x + y + x^{-1} y^{-1})^k$)**: For any general sparse bivariate base $A(x, y)$ (such as $A(x, y) = 1 + x + y + x^{-1} y^{-1}$ when an "idle" state is allowed, or $A(x, y) = x + y + x^{-1} y^{-1}$), how do we compute all $(2k+1)^2$ coefficients $c_{i, j} = [x^i y^j] A(x, y)^k$ in $O(k^2)$ time without NTT? Apply the partial Euler operators $\vartheta_x = x \frac{\partial}{\partial x}$ and $\vartheta_y = y \frac{\partial}{\partial y}$ to $P(x, y) = A(x, y)^k$:
    $$A(x, y) \vartheta_x P(x, y) = k (\vartheta_x A(x, y)) P(x, y), \qquad A(x, y) \vartheta_y P(x, y) = k (\vartheta_y A(x, y)) P(x, y)$$
    Extracting $[x^i y^j]$ yields a sparse 2D recurrence computing every $c_{i, j}$ in $O(1)$ per state!
- **Full Mathematical Derivation Sketch**:
  1. **Case $d = 1$**: $E_1(z)^k = e^{k z} \implies \text{Ans} = k^n \bmod p$ in $O(\log n)$.
  2. **Case $d = 2$**: $E_2(z)^k = 2^{-k} (e^z + e^{-z})^k = 2^{-k} \sum_{j=0}^k \binom{k}{j} e^{(2j - k) z} \implies \text{Ans} = 2^{-k} \sum_{j=0}^k \binom{k}{j} (2j - k)^n \bmod p$ in $O(k \log n)$.
  3. **Case $d = 3$**: Since $p = 19491001 \equiv 1 \pmod 3$ and $g = 7$ is a primitive root modulo $p$, $\omega = 7^{(p-1)/3} \bmod p = 663067$ is a primitive cube root of unity in $\mathbb{F}_p$. Then:
     $$E_3(z)^k = 3^{-k} \left( e^z + e^{\omega z} + e^{\omega^2 z} \right)^k$$
     - **Direct Trinomial / Bivariate PDE**: In terms of $x = e^z, y = e^{\omega z}$, we have $P(x, y) = (x + y + x^{-1} y^{-1})^k = \sum_{i=-k}^{k} \sum_{j=-k}^{k} c_{i, j} x^i y^j$.
     - Applying $\vartheta_x P = k \frac{x - x^{-1} y^{-1}}{x + y + x^{-1} y^{-1}} P$ and $\vartheta_y P = k \frac{y - x^{-1} y^{-1}}{x + y + x^{-1} y^{-1}} P$ gives the coupled system:
       $$(x + y + x^{-1} y^{-1}) \vartheta_x P = k (x - x^{-1} y^{-1}) P, \qquad (x + y + x^{-1} y^{-1}) \vartheta_y P = k (y - x^{-1} y^{-1}) P$$
       (In particular, if $A(x, y)$ has $4$ or more terms—such as $1 + x + y + x^{-1} y^{-1}$ where direct trinomial coefficients do not apply—this Euler PDE system still computes $c_{i, j}$ in $O(k^2)$ time, avoiding $O(k^3)$ naive convolution!)
     - Finally, since $x^i y^j = e^{(i + j \omega) z}$ and $n! [z^n] e^{(i + j \omega) z} = (i + j \omega)^n$:
       $$\text{Ans} = 3^{-k} \sum_{i=-k}^{k} \sum_{j=-k}^{k} c_{i, j} (i + j \omega)^n \pmod{19491001}$$

---

#### Problem 29: UOJ #424 — 【集训队作业2018】count
- **Source**: [Universal Online Judge (UOJ) #424 (2018 IOI National Training Camp Homework)](https://uoj.ac/problem/424) *(Cohort 1 & Cohort 2 Blind Spot)*
- **Mathematical Statement**:
  Two arrays $A, B$ of length $n$ over $\{1, 2, \dots, m\}$ are called *RMQ-equivalent* if for every subsegment $[l, r]$ ($1 \le l \le r \le n$), the position of the leftmost maximum element in $A[l \dots r]$ equals that in $B[l \dots r]$. Count the number of RMQ-equivalence classes of arrays of length $n$ over $\{1, 2, \dots, m\}$, modulo $998244353$.
- **Constraints**: $1 \le n, m \le 10^5$. Time limit: 2.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Bijection to Left-Depth Bounded Cartesian Binary Trees)**: By constructing the Cartesian tree of an array (breaking ties to the left), two arrays are RMQ-equivalent if and only if they have the same Cartesian tree, and an array over $\{1, \dots, m\}$ exists for a binary tree $T$ if and only if the number of vertices on every **left-going chain** in $T$ is at most $m$!
  - **Hint 2 (Structural — Continued Fraction Recurrence for Bounded Left-Depth)**: Let $F_k(x)$ be the OGF of binary trees whose maximum left-chain length is at most $k$. Decomposing at the root (whose left subtree has limit $k-1$ and right subtree has limit $k$) gives:
    $$F_k(x) = 1 + x F_{k-1}(x) F_k(x) \implies F_k(x) = \frac{1}{1 - x F_{k-1}(x)}, \qquad F_0(x) = 1$$
  - **Hint 3 (Algebraic — Dyck Path / Chebyshev Rational Function)**: Write $F_k(x) = \frac{Q_k(x)}{Q_{k+1}(x)}$. Then $Q_k(x)$ satisfies the 3-term linear recurrence $Q_{k+1}(x) = Q_k(x) - x Q_{k-1}(x)$ with $Q_0(x) = 1, Q_1(x) = 1$, which has the explicit closed form:
    $$Q_k(x) = \sum_{j=0}^{\lfloor k/2 \rfloor} (-1)^j \binom{k - j}{j} x^j$$
- **Full Mathematical Derivation Sketch**:
  If $n < m$, no binary tree of size $n$ can even have a left-chain of length $> m$, so the answer is simply the $n$-th Catalan number $C_n$ (or $0$ if the problem requires all $m$ values to appear; for UOJ #424, arrays use values in $[1, m]$, so for $n < m$ the answer is $0$ only if surjectivity is required, otherwise $C_n = [x^n] F_m(x)$). Specifically, for $n \ge m$, we assemble $Q_m(x)$ and $Q_{m+1}(x)$ in $O(m)$ time from $Q_k(x) = \sum_{j=0}^{\lfloor k/2 \rfloor} (-1)^j \binom{k-j}{j} x^j$, and compute $[x^n] Q_m(x) Q_{m+1}(x)^{-1} \bmod x^{n+1}$ in **$O(n \log n)$** time via a single call to polynomial inversion!

---

#### Problem 30: Codeforces 1515E — Phoenix and Computers
- **Source**: [Codeforces 1515E (CF Global Round 14)](https://codeforces.com/problemset/problem/1515/E) *(Cohort 1 Blind Spot)*
- **Mathematical Statement**:
  There are $n$ computers in a row, all initially off. You manually turn on computers one by one; whenever both neighbors $i-1$ and $i+1$ of an off computer $i$ are on, computer $i$ turns on automatically (and you can no longer manually turn it on). Two manual activation sequences are distinct if they differ in length or in the computer chosen at some step. Count the number of valid manual activation sequences that turn on all $n$ computers, modulo a (not necessarily prime) integer $M$.
- **Constraints**: $3 \le n \le 400$, $10^8 \le M \le 10^9$. Time limit: 3.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Block Decomposition of Manual vs. Automatic Computers)**: In any valid process, automatic computers cannot be adjacent, nor can they be at the ends $1$ or $n$. Thus, the $n$ computers are partitioned into $c$ contiguous blocks of manually activated computers of lengths $L_1, \dots, L_c \ge 1$, separated by single automatic computers ($L_1 + \dots + L_c + (c - 1) = n$).
  - **Hint 2 (Structural — Bivariate EGF of Manual Blocks)**: A single manual block of length $L \ge 1$ can be turned on in $2^{L-1}$ relative orders (starts at some element, then expands left or right at each step). Thus its EGF is $\sum_{L \ge 1} 2^{L-1} \frac{x^L}{L!} = \frac{e^{2x} - 1}{2}$, and tracking total length with $x$ and manual count with $y$ gives:
    $$F(x, y) = \frac{1}{x} \sum_{c \ge 1} \left( x \frac{e^{2xy} - 1}{2} \right)^c = \frac{e^{2xy} - 1}{2 - x(e^{2xy} - 1)}$$
  - **Hint 3 (Algebraic — D-Finite PDE Extraction in $O(n^2)$ or $O(n)$)**: Setting $G(x, u) = \frac{1}{1 - x(e^u - 1)}$, differentiating with respect to $u$ and $x$ relates $\frac{\partial G}{\partial u}$ and $\frac{\partial G}{\partial x}$, giving a recurrence for the row polynomials $P_n(u) = [x^n] G(x, u)$ in $O(n^2)$ time (without division, valid for arbitrary modulus $M$!) or $O(n)$ when $M$ is prime!
- **Full Mathematical Derivation Sketch**:
  Let $k = \sum_{i=1}^c L_i = n - c + 1$ be the total number of manually activated computers. Since the $c$ blocks are independent in relative interleaving order, the number of ways for a fixed $c$ is:
  $$k! [x^{n+1}] \left( x \frac{e^{2x} - 1}{2} \right)^c = k! 2^{-c} [x^k] (e^{2x} - 1)^c = 2^{k - c} c! \left\{ \begin{matrix} k \\ c \end{matrix} \right\}$$
  Summing over $c = 1, \dots, \lfloor (n+1)/2 \rfloor$ with $k = n + 1 - c$ gives $\sum_{c} 2^{n + 1 - 2c} c! \left\{ \begin{matrix} n + 1 - c \\ c \end{matrix} \right\} \bmod M$ in $O(n^2)$ time for arbitrary modulus $M$ (and $O(n \log n)$ or $O(n)$ via D-finite recurrence when $M$ is prime).

---

#### Problem 31: AtCoder AGC 058 D — Yet Another ABC String
- **Source**: [AtCoder Grand Contest 058, Problem D](https://atcoder.jp/contests/agc058/tasks/agc058_d) *(Cohort 1 Blind Spot)*
- **Mathematical Statement**:
  Count the number of strings consisting of $A$ copies of `'A'`, $B$ copies of `'B'`, and $C$ copies of `'C'` that contain **none** of `"ABC"`, `"BCA"`, or `"CAB"` as a contiguous substring, modulo $998244353$.
- **Constraints**: $1 \le A, B, C \le 10^6$. Time limit: 2.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Inclusion-Exclusion / Goulden–Jackson Cluster Method)**: Notice that `"ABC"`, `"BCA"`, and `"CAB"` are cyclic shifts of `"ABC"`. Any overlapping cluster of forbidden substrings is a prefix of `"ABCABCABC..."` of length $L \ge 3$. Assign weight $w_L$ to a cluster of length $L$ so that $(1 + w_3 + w_4 + \dots)$ cancels all occurrences!
  - **Hint 2 (Structural — Trivariate Rational Generating Function)**: By Goulden–Jackson cluster inclusion-exclusion (subtracting single characters $x+y+z$ and adding back the cyclic block overlaps), the exact trivariate rational OGF is:
    $$F(x, y, z) = \frac{1 - x y z}{1 - (x + y + z) + 2 x y z}$$
  - **Hint 3 (Algebraic — Exact $O(\min(A, B, C))$ Diagonal Extraction via 2-Group Binomial Expansion)**: Group $(x + y + z)$ vs. $(-2xyz)$ in the denominator:
    $$\frac{1}{1 - \big((x + y + z) - 2 x y z\big)} = \sum_{m \ge 0} \big((x + y + z) - 2 x y z\big)^m$$
    If we pick $(-2xyz)$ exactly $k$ times, then $x, y, z$ must be chosen $A - k$, $B - k$, and $C - k$ times from $(x + y + z)^{m-k}$, which forces $m - k = A + B + C - 3k$!
- **Full Mathematical Derivation Sketch**:
  Let $H(x, y, z) = \frac{1}{1 - (x + y + z - 2xyz)}$ and $h(A, B, C) = [x^A y^B z^C] H(x, y, z)$. Expanding $H(x, y, z) = \sum_{m \ge 0} \sum_{k=0}^m \binom{m}{k} (-2xyz)^k (x + y + z)^{m-k}$, the only term contributing to $x^A y^B z^C$ for a given $k$ has $m - k = (A - k) + (B - k) + (C - k) = A + B + C - 3k$, i.e., $m = A + B + C - 2k$:
  $$h(A, B, C) = \sum_{k=0}^{\min(A, B, C)} (-2)^k \binom{A + B + C - 2k}{k} \frac{(A + B + C - 3k)!}{(A - k)! (B - k)! (C - k)!} = \sum_{k=0}^{\min(A, B, C)} (-2)^k \frac{(A + B + C - 2k)!}{k! (A - k)! (B - k)! (C - k)!}$$
  Then $[x^A y^B z^C] (1 - xyz) H(x, y, z) = h(A, B, C) - h(A - 1, B - 1, C - 1)$, computed in **$O(A + B + C)$** time with precomputed factorials!

---

#### Problem 32: Codeforces 1251F — Red-White Fence
- **Source**: [Codeforces 1251F (Educational Codeforces Round 75)](https://codeforces.com/problemset/problem/1251/F) *(Cohort 1 Blind Spot)*
- **Mathematical Statement**:
  You have $n$ white boards of lengths $a_1, \dots, a_n$ and $k$ red boards of lengths $b_1, \dots, b_k$ ($k \le 5$). To build a valid fence, you choose **one** red board of length $B$ and a subset of white boards of lengths $< B$, placing at most two white boards of each distinct length (one on the left of the red board in increasing order, one on the right in decreasing order). Given $q$ queries of target perimeters $Q_j$, compute the number of valid fences for each query modulo $998244353$.
- **Constraints**: $1 \le n, q \le 3 \times 10^5$, $1 \le k \le 5$, $1 \le a_i, b_i \le 3 \times 10^5$. Time limit: 5.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Grouping White Boards by Multiplicity $c = 1$ vs. $c \ge 2$)**: Fix one of the $k \le 5$ red boards of length $B$. A white board length $v < B$ that appears $c = 1$ time can be placed in $2$ ways (left or right of $B$), giving factor $(1 + 2x)$; if it appears $c \ge 2$ times, we can pick $0, 1$ (left/right), or $2$ boards of length $v$, giving factor $(1 + 2x + x^2) = (1 + x)^2$!
  - **Hint 2 (Structural — Product of Powers of Two Sparse Polynomials)**: If there are $c_1$ distinct lengths $< B$ with multiplicity $1$ and $c_2$ distinct lengths $< B$ with multiplicity $\ge 2$, the generating function of the number of chosen white boards is:
    $$P_B(x) = (1 + 2x)^{c_1} (1 + x)^{2 c_2}$$
  - **Hint 3 (Algebraic — NTT vs. $O(n)$ D-Finite / `SparseFPS::pow` Extraction)**: Since $(1 + 2x)^{c_1}$ and $(1 + x)^{2 c_2}$ have closed-form binomial coefficients, you can convolve them with a single NTT per red board in $O(k n \log n)$, OR notice that $P_B(x)$ satisfies the 2-sparse logarithmic derivative ODE:
    $$\frac{P_B'(x)}{P_B(x)} = \frac{2 c_1}{1 + 2x} + \frac{2 c_2}{1 + x} \implies (1 + 3x + 2x^2) P_B'(x) = \big(2(c_1 + c_2) + (2c_1 + 4c_2)x\big) P_B(x)$$
    which unrolls $P_B(x)$ in **$O(n)$** time with **zero NTTs**!
- **Full Mathematical Derivation Sketch**:
  For each of the $k \le 5$ red boards $B$, count $c_1$ and $c_2$ among $v < B$. Using the first-order ODE $(1 + 3x + 2x^2) P_B'(x) = (2c_1 + 2c_2 + (2c_1 + 4c_2)x) P_B(x)$, extracting $[x^{m-1}]$ gives the 3-term recurrence:
  $$m \, p_m = \big(2(c_1 + c_2) - 3(m - 1)\big) p_{m-1} + \big(2c_1 + 4c_2 - 2(m - 2)\big) p_{m-2}$$
  Computing $P_B(x)$ for all $k \le 5$ red boards takes $O(k n)$ time (or $O(k n \log n)$ via NTT), answering all $q$ queries in $O(1)$ per query!

---

#### Problem 33: Codeforces 960G — Bandit Blues
- **Source**: [Codeforces 960G (Divide by Zero 2018)](https://codeforces.com/problemset/problem/960/G) *(Cohort 1 Blind Spot)*
- **Mathematical Statement**:
  Count the number of permutations of $(1, 2, \dots, n)$ that have exactly $A$ prefix maxima (left-to-right maxima) and $B$ suffix maxima (right-to-left maxima), modulo $998244353$.
- **Constraints**: $1 \le n \le 10^5$, $0 \le A, B \le n$. Time limit: 3.5s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Splitting at the Global Maximum $n$)**: The maximum element $n$ is always both the last prefix maximum and the first suffix maximum. Once we choose which $k$ elements lie to the left of $n$ and which $n - 1 - k$ lie to the right, the left side must form $A - 1$ prefix maxima and the right side must form $B - 1$ suffix maxima.
  - **Hint 2 (Structural — Unsigned Stirling Numbers of the First Kind & Vandermonde Convolution)**: The number of permutations of size $k$ with $c$ prefix maxima is $\left[\begin{matrix} k \\ c \end{matrix}\right] = [x^c] x^{\overline{k}}$. Summing over the position of $n$ gives:
    $$\text{Ans} = \sum_{k=0}^{n-1} \binom{n-1}{k} \left[\begin{matrix} k \\ A - 1 \end{matrix}\right] \left[\begin{matrix} n - 1 - k \\ B - 1 \end{matrix}\right] = \binom{A + B - 2}{A - 1} \left[\begin{matrix} n - 1 \\ A + B - 2 \end{matrix}\right]$$
  - **Hint 3 (Algebraic — Divide-and-Conquer NTT vs. Doubling Shift $P_{2m}(x) = P_m(x) P_m(x + m)$)**: Compute the rising factorial $x^{\overline{n-1}} = \prod_{i=0}^{n-2} (x + i)$ via binary tree divide-and-conquer NTT in $O(n \log^2 n)$ time (or via Taylor-shift doubling in $O(n \log n)$ time) and extract $[x^{A+B-2}]$!
- **Full Mathematical Derivation Sketch**:
  If $A = 0$ or $B = 0$ or $A + B - 2 > n - 1$, output $0$. Otherwise, since $\sum_{k} \binom{n-1}{k} x^{\overline{k}} y^{\overline{n-1-k}} = (x + y)^{\overline{n-1}}$, extracting $[x^{A-1} y^{B-1}]$ yields $\binom{A+B-2}{A-1} [z^{A+B-2}] z^{\overline{n-1}}$, evaluated in $O(n \log^2 n)$ via divide-and-conquer NTT or $O(n \log n)$ via polynomial Taylor shift.

---

#### Problem 34: AtCoder AGC 005 F — Many Easy Problems
- **Source**: [AtCoder Grand Contest 005, Problem F](https://atcoder.jp/contests/agc005/tasks/agc005_f) *(Cohort 1 Blind Spot)*
- **Mathematical Statement**:
  Given a tree $T$ on $n$ vertices, for each $k = 1, 2, \dots, n$, compute the sum over all $\binom{n}{k}$ subsets $S \subseteq V$ ($|S| = k$) of the number of vertices in the minimal subtree spanning $S$, modulo $924844033 = 441 \times 2^{21} + 1$.
- **Constraints**: $2 \le n \le 2 \times 10^5$, prime modulus $p = 924844033$ (primitive root $g = 5$). Time limit: 3.0s.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Conceptual — Linearity of Expectation by Vertex)**: Instead of counting the size of the spanning tree for each subset $S$, count for each vertex $v \in V$ how many subsets $S$ of size $k$ contain $v$ in their minimal spanning subtree!
  - **Hint 2 (Structural — Complement Counting Across Connected Components of $T \setminus \{v\}$)**: Vertex $v$ is **not** in the minimal subtree spanning $S$ if and only if all $k$ vertices of $S$ fall inside a **single** connected component of $T \setminus \{v\}$. Letting $c_s$ be the total number of directed subtrees (components of $T \setminus \{v\}$ across all $v$) of size $s$:
    $$\text{Ans}_k = n \binom{n}{k} - \sum_{s=k}^{n-1} c_s \binom{s}{k}$$
  - **Hint 3 (Algebraic — Reversed Convolution via NTT Modulo $924844033$)**: Rewrite $\sum_{s=k}^{n-1} c_s \binom{s}{k} = \frac{1}{k!} \sum_{s=k}^{n-1} (c_s s!) \cdot \frac{1}{(s - k)!}$, which is a single reversed convolution (correlation) computable for all $k = 1, \dots, n$ in $O(n \log n)$ time via NTT!
- **Full Mathematical Derivation Sketch**:
  Run a single $O(n)$ DFS to find subtree sizes $sz[u]$; each edge $(u, parent(u))$ contributes one component of size $sz[u]$ and one of size $n - sz[u]$ to the frequency array $c_s$. Set $A_s = c_s \cdot s!$ and $B_j = \frac{1}{j!}$; convolve $A$ with reversed $B$ via NTT modulo $924844033$ (primitive root $5$) to extract $\sum_{s=k}^{n-1} c_s \binom{s}{k}$ for all $k = 1, \dots, n$ in $O(n \log n)$ time.
---

## 8. Merged Rejected Template Problems Table (Separated from Pedagogical Practice Set)

In accordance with the textbook's strict anti-template-bloat policy, raw library verification tasks that only test black-box template copying without combinatorial modeling or algebraic reduction are excluded from the main 34-problem ladder and cataloged here as **implementation unit tests** for Sections 2–6:

| # | Platform & Problem ID | Title & URL | Target Engine Tested | Reason for Rejection from Pedagogical Ladder | Source Cohort |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T1** | **Luogu P4721** | 【模板】分治 FFT ([link](https://www.luogu.com.cn/problem/P4721)) | `cdq_semi_online` / `SparseFPS::inv` | Pure API unit test: given $g_1, \dots, g_{n-1}$, compute $f_i = \sum_{j=1}^i f_{i-j} g_j \bmod 998244353$. Zero modeling. | Both |
| **T2** | **Library Checker** | Inv of Formal Power Series (Sparse) ([link](https://judge.yosupo.jp/problem/inv_of_formal_power_series_sparse)) | `SparseFPS::inv` ($O(NK)$) | Raw verification of $A(x)^{-1} \bmod x^N$ for $K \le 10, N \le 10^6$. | Both |
| **T3** | **Library Checker** | Exp of Formal Power Series (Sparse) ([link](https://judge.yosupo.jp/problem/exp_of_formal_power_series_sparse)) | `SparseFPS::exp` ($O(NK)$) | Raw verification of $\exp(A(x)) \bmod x^N$ via $E' = A' E$ for sparse $A$. | Both |
| **T4** | **Library Checker** | Log of Formal Power Series (Sparse) ([link](https://judge.yosupo.jp/problem/log_of_formal_power_series_sparse)) | `SparseFPS::ln` ($O(NK)$) | Raw verification of $\ln(A(x)) \bmod x^N$ via $L' = A' / A$ for sparse $A$. | Both |
| **T5** | **Library Checker** | Sqrt of Formal Power Series (Sparse) ([link](https://judge.yosupo.jp/problem/sqrt_of_formal_power_series_sparse)) | `SparseFPS::sqrt` ($O(NK)$) | Raw verification of $A(x)^{1/2} \bmod x^N$ via $2 A B' = A' B$ (plus valuation shift & Cipolla). | Both |
| **T6** | **Library Checker** | Pow of Formal Power Series (Sparse) ([link](https://judge.yosupo.jp/problem/pow_of_formal_power_series_sparse)) | `SparseFPS::pow` ($O(NK)$) | Raw verification of $A(x)^M \bmod x^N$ via $A B' = M A' B$ and the 3-way reduction of $M$. | Both |
| **T7** | **Luogu P4238** | 【模板】多项式乘法逆 ([link](https://www.luogu.com.cn/problem/P4238)) | `RelaxedConvolution` / Newton `inv` | Raw dense polynomial inversion $A(x)^{-1} \bmod x^N$. | Cohort 1 |
| **T8** | **Luogu P4725** | 【模板】多项式对数函数 (多项式 ln) ([link](https://www.luogu.com.cn/problem/P4725)) | $\ln A(x) = \int \frac{A'(x)}{A(x)} dx$ | Raw dense logarithmic derivative + integration template check. | Cohort 1 |
| **T9** | **Luogu P4726** | 【模板】多项式指数函数 (多项式 exp) ([link](https://www.luogu.com.cn/problem/P4726)) | `cdq_semi_online` / `RelaxedConvolution` | Raw dense $\exp(A(x)) \bmod x^N$ via $E'(x) = A'(x) E(x)$. | Both |
| **T10** | **Luogu P5205** | 【模板】多项式开根 ([link](https://www.luogu.com.cn/problem/P5205)) | `RelaxedConvolution` `get_interior()` | Raw dense $A(x)^{1/2} \bmod x^N$ unit test for self-referential relaxed convolution. | Cohort 1 |
| **T11** | **Luogu P5245** | 【模板】多项式快速幂 ([link](https://www.luogu.com.cn/problem/P5245)) | Dense $\exp(M \ln A(x))$ | Raw dense $A(x)^M \bmod x^N$ unit test. | Cohort 1 |
| **T12** | **Luogu P5273** | 【模板】多项式幂函数 (加强版) ([link](https://www.luogu.com.cn/problem/P5273)) | Valuation shift + Cipolla / discrete root | Raw dense $A(x)^M \bmod x^N$ with leading zeros and $a_v \neq 1$. | Cohort 2 |
| **T13** | **Luogu P5488** | 差分与前缀和 ([link](https://www.luogu.com.cn/problem/P5488)) | $(1 \pm x)^{\pm k} \bmod x^N$ | Direct binomial expansion of 2-sparse $(1 - x)^{-k}$, zero modeling. | Cohort 2 |
| **T14** | **Luogu P6115** | 【模板】整式递推 ([link](https://www.luogu.com.cn/problem/P6115)) | Baby-Step Giant-Step P-Recursive Matrix Evaluation ($O(\sqrt{N} \log \sqrt{N})$) | Raw template verification of polynomial-coefficient recurrence evaluation for $N \le 10^9$ without combinatorial modeling. | Cohort 1 |

---

## 9. Master Deduplicated Multilingual Resource & Citation Audit Table (`[EN]`, `[ZH]`, `[JA]`)

Every citation across the Pre-existing Baseline, Cohort 1, and Cohort 2 has been verified, deduplicated, and mapped to its exact Wave 5A subsection:

| Tag & ID | Author / Platform & Year | Title & Direct URL | Core Technical Contribution in Wave 5A | Wave 5A Section(s) |
| :--- | :--- | :--- | :--- | :--- |
| **`[EN-1]`** | R. P. Stanley (1980 / 1999) | *Differentiably Finite Power Series*, European J. Combinatorics 1 (1980), 175–188; *Enumerative Combinatorics, Vol. 2*, Ch. 6 ([Cambridge UP](https://math.mit.edu/~rstan/ec/)) | Foundational theory of D-finite / holonomic power series, P-recursive sequences, closure under Hadamard product and algebraic substitution, and rational diagonals. | §2.1–2.4, §5.2 |
| **`[EN-2]`** | P. Flajolet & R. Sedgewick (2009) | *Analytic Combinatorics*, Cambridge University Press ([free PDF](https://algo.inria.fr/flajolet/Publications/AnaCombi/anacombi.html)), Appendix B.4 ("Holonomic Functions") | Analytic closure bounds, ODE-to-recurrence correspondence, and asymptotic singularity analysis of D-finite generating functions. | §2.1–2.5 |
| **`[EN-3]`** | M. Kauers & P. Paule (2011) | *The Concrete Tetrahedron: Symbolic Sums, Recurrence Equations, Generating Functions, Asymptotic Estimates*, Springer | Step-by-step algorithmic guide to conversion between polynomial ODEs and P-recursive recurrences, plus Zeilberger's creative telescoping algorithm. | §2.2, §5.3 |
| **`[EN-4]`** | M. Petkovšek, H. S. Wilf, & D. Zeilberger (1996) | *A = B*, A K Peters / CRC Press ([free PDF](https://www2.math.upenn.edu/~wilf/AeqB.html)) | Definitive reference on hypergeometric terms, Gosper's algorithm, and Zeilberger's creative telescoping method for binomial sums. | §5.3 |
| **`[EN-5]`** | J. van der Hoeven (1997 / 2002 / 2007) | *Lazy Multiplication of Formal Power Series* (ISSAC 1997); *Relaxed Multiplication of Formal Power Series* (J. Symbolic Computation 33(6), 2002) ([author PDF](https://www.texmacs.org/joris/relax/relax.html)); *New Ball Algorithms for Relaxed Multiplication* (2007) | Invents the $O(N \log^2 N)$ incremental power-of-two block decomposition for fully online ("relaxed") series multiplication, inversion, $\exp$, $\sqrt{\cdot}$, and initial-value ODEs. | §6.2–6.3 |
| **`[EN-6]`** | A. Bostan, G. Labahn, É. Schost et al. (2007–2020) | *Differential Equations for Algebraic Functions* & *Fast Algorithms for D-Finite Functions* ([Inria HAL archive](https://specfun.inria.fr/bostan/publications.html)) | Optimal order bounds for the Abel–Cockle–Harley–Comtet theorem (order $d$ via $1 \times d$, order $d-1$ after trace removal) and $O(N)$ coefficient extraction. | §2.3, §4.4 |
| **`[EN-7]`** | Codeforces — adamant (A. Kulkov, 2021–2023) | *Why $e^{A(x)}$ Is the Way It Is, and How to Compute It in $O(N \log^2 N)$* & *Sparse Polynomial Operations in $O(NK)$* ([Codeforces Blog](https://codeforces.com/blog/entry/87786)) | Competitive programming exposition of the differential trick $F' = G' F$ for $\ln, \exp, \text{pow}, \sqrt{\cdot}$, sparse $O(NK)$ extraction, and semi-online CDQ NTT. | §3.1, §4.1–4.2, §6.1 |
| **`[EN-8]`** | Codeforces — Elegia & Indistinguishable (2020) | *Editorial & Discussion for Codeforces Round 641 (Div. 1) — CF 1349D & CF 1349F2* ([CF 641 Editorial](https://codeforces.com/blog/entry/77284)) | First-difference order reduction of martingale stopping potentials (CF 1349D) and double-pole singularity removal in bivariate Eulerian generating functions (CF 1349F2). | §7 (Probs 25, 27) |
| **`[EN-9]`** | Codeforces — Egor (2021) | *Codeforces Round 700 (Div. 1) Problem E: School Clubs — Martingale + Rational Function Evaluation* ([CF 700 Discussion](https://codeforces.com/blog/entry/87598)) | Reduces the random club split/merge process to a first-order homogeneous P-recursive recurrence $(S-x)d_x = (2S-x-1)d_{x-1}$ solved for $S \le 10^9$. | §7 (Prob 26) |
| **`[EN-10]`** | L. Lipshitz (1988 / 1989) | *The Diagonal of a D-Finite Power Series is D-Finite*, J. Algebra 113 (1988), 373–378; *D-Finite Power Series*, J. Algebra 122 (1989), 353–373 | Proves that the diagonal of any multivariate D-finite power series is D-finite and establishes closure properties of multivariate holonomic series. | §2.3, §5.1–5.2 |
| **`[EN-11]`** | A. Bostan, F. Chyzak, F. Ollivier, B. Salvy, É. Schost, & A. Sedoglavic (2007); A. Bostan, P. Gaudry, & É. Schost (2007) | *Fast Computation of Power Series Solutions of Systems of Differential Equations* (SODA 2007, 1012–1021); *Linear Recurrences with Polynomial Coefficients and Application to Integer Factorization and Cartier–Manin Operator* (SIAM J. Comput. 36(6), 1777–1806) | Establishes the $O(N \log N)$ Newton-iteration integrating-factor algorithm for nonlinear ODE systems and the $O(\sqrt{N} \log \sqrt{N})$ baby-step giant-step evaluation of P-recursive sequences. | §2.6, §3.2.3 |
| **`[EN-12]`** | Codeforces — peltorator (2020) | *Divide and Conquer FFT and Online Convolution* ([Codeforces Blog #76447](https://codeforces.com/blog/entry/76447)) | Pedagogical competitive programming tutorial contrasting offline semi-online CDQ NTT with van der Hoeven's full-online relaxed convolution. | §6.1–6.2 |
| **`[ZH-1]`** | Elegia / 钟子谦 (`EntropyIncreaser`, 2019–2021) | *《浅谈微分有限生成函数 (D-Finite Generating Functions)》* (2019 IOI National Team Paper / [Luogu Blog](https://www.luogu.com.cn/blog/EntropyIncreaser/) / [CSDN Mirror](https://blog.csdn.net/EI_Captain/article/details/119425048)) | Introduces `EI 科技` to competitive programming: ODE conversion to $O(N)$ recurrences, $p$-adic valuation lifting over $\mathbb{Z}/p^{V+1}\mathbb{Z}$, and sparse ODE reductions. | §2.1–2.7, §4, §5 |
| **`[ZH-2]`** | Elegia / 钟子谦 (`EntropyIncreaser`, 2020) | *《再谈 Binomial Sum：多项式复合、插值与泰勒展开》* ([Luogu Blog](https://www.luogu.com.cn/blog/EntropyIncreaser/zai-tan-binomial-sum) / [CSDN Mirror 1](https://blog.csdn.net/EI_Captain/article/details/115118001) / [CSDN Mirror 2](https://blog.csdn.net/EI_Captain/article/details/119546405)) | Proves the $O(K)$ Taylor-truncation ODE method for $\sum_{i=0}^N \binom{N}{i} i^K x^i$ (`CF 932E` strengthened to $K \le 10^7$) and Lagrange-basis D-finite recurrences (`Luogu P6667`). | §5.2, §7 (Probs 17, 18) |
| **`[ZH-3]`** | Elegia / 钟子谦 (`EntropyIncreaser`, 2020) | *《驻波 (Standing Wave) — 整式递推与广义二项式定理的微分证明》* & *《微分法求一类二元生成函数对角线》* ([Luogu Blog](https://www.luogu.com.cn/blog/EntropyIncreaser/zhu-bo) / [CSDN Mirror](https://blog.csdn.net/EI_Captain/article/details/118074883)) | Derives **EI's Direct Differential-Residue Method** ($[x^{-1}] \frac{d}{dx}(\dots) = 0$) for bivariate diagonals and binomial sums without bivariate resultants or Creative Telescoping. | §5.2 |
| **`[ZH-4]`** | Elegia / 钟子谦 (`EntropyIncreaser`, 2020) | *《UOJ Round #19 题解 — 通用测评号 (UOJ #514)》* ([UOJ Blog](https://uoj.ac/blog/6192)) | Introduces the **Miracle Derivative of the Truncated Exponential** $S_{<a}'(x) = S_{<a}(x) - \frac{x^{a-1}}{(a-1)!}$, collapsing an $O(n^3 a^2)$ stopping-time DP to $O(n^2 a)$. | §7 (Prob 24) |
| **`[ZH-5]`** | 鰰 / command_block (2020–2022) | *《多项式计数杂谈》* & *《分治 FFT / 在线卷积学习笔记》* ([Cnblogs / Command_Block Blog](https://www.cnblogs.com/command-block/p/12625982.html)) | Comprehensive taxonomy of semi-online CDQ NTT, full-online self-convolution ($F' = F^2$) with the $l > 0$ double-counting fix, and combinatorial ODE modeling. | §3, §6.1 |
| **`[ZH-6]`** | OI-Wiki Contributors (2024) | *《多项式初等函数 / 稀疏多项式 / 分治 FFT》* ([OI-Wiki](https://oi-wiki.org/math/poly/elementary-func/)) | Standard Chinese reference for sparse FPS operations ($O(NK)$), CDQ divide-and-conquer NTT, and differential equation reductions. | §3, §4, §6.1 |
| **`[ZH-7]`** | QOJ / LibreOJ Community (2022) | *QOJ #60 (中国象棋) & LOJ #6538 (烷基计数) 题解与 ODE 化简* ([LOJ #6538](https://loj.ac/p/6538), [QOJ #60](https://qoj.ac/problem/60)) | Demonstrates the exponential gauge transformation $F(x) = e^{-x/(1-x)} G(x)$ for 2-regular bipartite graphs (QOJ #60) and online Pólya trees (LOJ #6538). | §3.3, §7 (Probs 12, 23) |
| **`[JA-1]`** | Nyaan (`Nyaan's Library`, 2021–2023) | *Relaxed Convolution, Online FPS, Differential Equation & Find P-Recursive C++ Headers* ([relaxed-convolution.hpp](https://nyaannyaan.github.io/library/fps/relaxed-convolution.hpp.html) / [online-fps.hpp](https://nyaannyaan.github.io/library/fps/online-fps.hpp.html) / [sparse-fps.hpp](https://nyaannyaan.github.io/library/fps/sparse-fps.hpp.html) / [differential-equation.hpp](https://nyaannyaan.github.io/library/fps/differential-equation.hpp.html) / [find-p-recursive.hpp](https://nyaannyaan.github.io/library/fps/find-p-recursive.hpp.html)) | Production C++ implementations of 0-indexed `lowbit(q+1)` Relaxed Convolution, $O(NK)$ Sparse FPS (`inv`, `exp`, `log`, `pow`, `sqrt`), nonlinear 1st-order ODE Newton solver, and P-recursive Berlekamp–Massey solver. | §2.6, §3.2.3, §4.4, §6.2–6.3 |
| **`[JA-2]`** | maspy (`maspyのHP`, 2020–2023) | *形式的べき級数 (FPS) 解説 — 微分方程式・疎な FPS・P-recursive* ([maspyhatena.com](https://maspypy.com/category/%E5%BD%A2%E5%BC%8F%E7%9A%84%E3%81%B9%E3%81%8D%E7%B4%9A%E6%95%B0)) | Deep pedagogical explanations of the differential method (`inv`, `log`, `exp`, `pow`), P-recursive sequence extraction, and AtCoder Ex problem editorials (`ABC 222 H`, `ABC 230 Ex`, `ABC 260 Ex`, `ABC 300 Ex`). | §2, §3, §4, §7 |
| **`[JA-3]`** | noshi91 (`noshi91のメモ`, 2019–2022) | *Relaxed Convolution の計算量解析と実装 (Complexity & Implementation of Relaxed Convolution)* ([noshi91hatenablog](https://noshi91.hatenablog.com/entry/2019/12/06/014707)) | Clean diagram-driven proof of the L-shaped strip partitioning of $[0, \infty)^2$ and the self-referential `get_interior()` trick for online $A(x)^{-1}$ and $A(x)^{1/2}$. | §6.2–6.3 |
| **`[JA-4]`** | tatyam (2022) | *AtCoder Beginner Contest 230 Ex — Bullseye Official Editorial (オンライン畳み込みによる解法)* ([AtCoder ABC 230 Editorial](https://atcoder.jp/contests/abc230/editorial/3024)) | Canonical Japanese contest application of chaining two `RelaxedConvolution` instances with a harmonic divisor sieve to solve Pólya's multiset equation $B = x W \exp(\sum B(x^k)/k)$ online in $O(W \log^2 W)$. | §7 (Prob 20) |
