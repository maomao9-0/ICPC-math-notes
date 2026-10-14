# Wave 5A Research & Audit Record (Iterations 41–45): D-Finite Series & Linear ODEs, Differential Equation Substitutions, Sparse FPS in $O(N \cdot K)$, Euler Homogeneous PDEs, CDQ NTT, and Online / Relaxed Convolution

> **Scope of Wave 5A**: This document records Iterations 41–45 of the multilingual (`[EN]`, `[ZH]`, `[JA]`) Formal Power Series (FPS) and Generating Functions research and audit loop. It establishes the bidirectional dictionary between D-finite (holonomic) generating functions and P-recursive sequences, provides a zero-magic reverse-engineering guide for simplifying differential equations via variable and gauge substitutions, formalizes the $O(N \cdot K)$ sparse FPS engine (`inv`, `div`, `exp`, `ln`, `pow`, $\sqrt{\cdot}$, $F(P(x))$), develops Euler homogeneous PDEs and creative telescoping for binomial sums, and proves the exact index invariants for both Semi-Online Divide-and-Conquer FFT (CDQ NTT) and Fully Online / Relaxed Convolution (van der Hoeven's dyadic square tiling).

---

## Iteration 41: D-Finite Series, P-Recursive Sequences & Turning GFs into Linear ODEs ($P(x)F' + Q(x)F = R(x)$)

### 41.1 Concrete Definitions: D-Finite Series and P-Recursive Sequences
In earlier waves, rational generating functions $F(x) = \frac{P(x)}{Q(x)}$ corresponded to **constant-coefficient** linear recurrences $f_n = c_1 f_{n-1} + \dots + c_d f_{n-d}$. However, most sequences involving factorials, Catalan/Delannoy/Motzkin paths, involutions, derangements, or powers of binomial coefficients grow too fast or decay too irregularly to satisfy any constant-coefficient recurrence. Their natural home is the wider class of **polynomial-coefficient** recurrences and linear differential equations:

1. **P-Recursive (Polynomially Recursive / Holonomic) Sequence (`整式递推数列`)**:
   A sequence $(f_n)_{n \ge 0}$ over a field $K$ is **P-recursive** of order $r$ and polynomial degree $d$ if there exist polynomials $Q_0(n), Q_1(n), \dots, Q_r(n) \in K[n]$ of degree at most $d$ (with $Q_0(n) \neq 0$) and a finite-support/polynomial sequence $c_n$ such that for all $n \ge n_0$:
   $$Q_0(n) f_n + Q_1(n) f_{n-1} + \dots + Q_r(n) f_{n-r} = c_n.$$
   Once the initial window $f_0, \dots, f_{n_0-1}$ is known and provided the leading coefficient $Q_0(n) \in K^\times$ is invertible for every $n \in [n_0, N]$, each term $f_n$ is computed from the previous $r$ terms in $O(r)$ operations (after evaluating $Q_k(n)$), yielding all $f_0, \dots, f_N$ in **$O(r N)$ time and $O(r)$ working space**—completely bypassing $O(N \log N)$ NTT!

2. **D-Finite (Differentiably Finite / Holonomic) Series (`微分有限生成函数`)**:
   A formal power series $F(x) = \sum_{n \ge 0} f_n x^n \in K[[x]]$ is **D-finite** of order $s$ if there exist polynomials $P_0(x), P_1(x), \dots, P_s(x) \in K[x]$ (with $P_s(x) \neq 0$) and an inhomogeneous polynomial $R(x) \in K[x]$ such that:
   $$P_s(x) F^{(s)}(x) + P_{s-1}(x) F^{(s-1)}(x) + \dots + P_1(x) F'(x) + P_0(x) F(x) = R(x).$$
   *(Note: Differentiating both sides $\deg R + 1$ times produces a strictly homogeneous linear ODE of order $s + \deg R + 1$, so the homogeneous and polynomial-inhomogeneous definitions define the exact same class of series in characteristic zero.)* Equivalently, the derivatives $F(x), F'(x), F''(x), \dots$ span a finite-dimensional vector space over the rational function field $K(x)$.

---

### 41.2 The Bidirectional Translation Dictionary ($x^i D^j \leftrightarrow$ Shift & Falling Factorial)
Let $D = \frac{d}{dx}$ be the formal derivative and $\vartheta = x \frac{d}{dx}$ be the Euler homogeneity operator ($[x^n] \vartheta^m F(x) = n^m f_n$).

#### Direction 1: Differential Equation $\to$ Sequence Recurrence
Every monomial differential term $x^i F^{(j)}(x)$ translates mechanically into a single shifted coefficient of $F(x)$:
$$[x^n] \bigl(x^i F^{(j)}(x)\bigr) = [x^{n-i}] F^{(j)}(x) = \begin{cases} (n - i + j)^{\underline{j}} \, f_{n - i + j} = \dfrac{(n - i + j)!}{(n - i)!} f_{n - i + j}, & \text{if } n \ge i, \\ 0, & \text{if } n < i, \end{cases}$$
where $m^{\underline{j}} = m(m-1)\cdots(m-j+1)$ is a falling factorial (a polynomial in $n$ with integer coefficients, requiring no division).

Notice the **index shift $s = j - i$**:
- A term $x^i F^{(j)}(x)$ accesses the sequence at index **$n + (j - i)$**!
- In particular, for a **first-order linear ODE** $P(x) F'(x) + Q(x) F(x) = R(x)$ where $P(x) = \sum_{i=0}^{d_P} p_i x^i$ and $Q(x) = \sum_{i=0}^{d_Q} q_i x^i$, let $r = \max(d_P, d_Q + 1)$ (setting $p_i = 0$ for $i > d_P$ and $q_i = 0$ for $i > d_Q$). Extracting $[x^{n-1}]$ for $n \ge 1$ aligns the highest accessed index at $f_n$:
  $$\underbrace{n p_0}_{\text{coeff of } f_n} f_n + \sum_{k=1}^{r} \bigl((n - k) p_k + q_{k-1}\bigr) f_{n-k} = [x^{n-1}] R(x).$$
- More generally, for an **order-$s$ linear ODE** $\sum_{j=0}^s \left(\sum_{i} p_{j, i} x^i\right) F^{(j)}(x) = R(x)$, let $s_{\max} = \max \{ j - i : p_{j, i} \neq 0 \}$ be the maximum shift. Extracting $[x^{n - s_{\max}}]$ places the highest accessed term at $f_n$ with leading polynomial coefficient:
  $$I(n) = \sum_{j - i = s_{\max}} p_{j, i} \, (n)^{\underline{j}}.$$

#### Direction 2: Sequence Recurrence $\to$ Differential Equation
Conversely, given a P-recursive recurrence $\sum_{k=0}^r Q_k(n) f_{n-k} = c_n$ (valid for $n \ge n_0$), how do we construct the linear ODE for $F(x) = \sum_{n \ge 0} f_n x^n$?
1. Observe how $\vartheta = x D$ interacts with a shift $x^k F(x) = \sum_{n \ge k} f_{n-k} x^n$:
   $$[x^n] \Bigl( Q_k(\vartheta) \bigl(x^k F(x)\bigr) \Bigr) = Q_k(n) f_{n-k} \qquad (n \ge k).$$
   Equivalently, using the commutation rule $\vartheta (x^k G) = x^k (\vartheta + k) G$, we can pull $x^k$ to the left:
   $$Q_k(\vartheta) \bigl(x^k F(x)\bigr) = x^k Q_k(\vartheta + k) F(x).$$
2. Summing over $n \ge n_0$ shows that $\sum_{k=0}^r x^k Q_k(\vartheta + k) F(x) = R(x)$, where $R(x)$ is a polynomial of degree $< n_0$ (plus any finite support of $c_n$) determined by the initial values $f_0, \dots, f_{n_0 - 1}$.
3. Finally, to rewrite powers of $\vartheta = x D$ in terms of ordinary derivatives $x^j D^j = x^j \frac{d^j}{dx^j}$ (or vice versa), use the **Stirling Number Operator Identities**:
   $$\vartheta^m = \sum_{j=0}^m \left\{ \begin{matrix} m \\ j \end{matrix} \right\} x^j D^j, \qquad x^j D^j = \vartheta(\vartheta - 1)\cdots(\vartheta - j + 1) = \sum_{m=0}^j (-1)^{j-m} \left[ \begin{matrix} j \\ m \end{matrix} \right] \vartheta^m.$$

---

### 41.3 How to Turn Closed-Form GFs into Linear ODEs: The 4 Canonical Recipes
Whenever a problem reduces to a generating function built from algebraic powers, radicals, exponentials, or logarithms of low-degree polynomials, we do **not** need $O(N \log N)$ FPS operations (`inv`, `sqrt`, `ln`, `exp`, `pow`). Instead, we convert $F(x)$ into a linear ODE with polynomial coefficients using four mechanical rules:

| Closed-Form GF Pattern | Diagnostic Step | Resulting Linear ODE with Polynomial Coefficients | Order & Recurrence Width |
| :--- | :--- | :--- | :--- |
| **1. Power of Rational Function** $F(x) = \left(\frac{A(x)}{B(x)}\right)^\alpha$ | Take logarithmic derivative $\frac{F'}{F} = \alpha \left(\frac{A'}{A} - \frac{B'}{B}\right)$ | $A(x)B(x) F'(x) - \alpha \bigl(A'(x)B(x) - A(x)B'(x)\bigr) F(x) = 0$ | Order $1$; width $\le \deg A + \deg B$ |
| **2. Exponential of Rational Function** $F(x) = \exp\!\left(\frac{A(x)}{B(x)}\right)$ | Differentiate $\ln F(x) = \frac{A(x)}{B(x)}$ | $B(x)^2 F'(x) - \bigl(A'(x)B(x) - A(x)B'(x)\bigr) F(x) = 0$ | Order $1$; width $\le \max(2\deg B, \deg A + \deg B - 1)$ |
| **3. Product of Power & Exponential** $F(x) = A(x)^\alpha \exp\!\left(\frac{B(x)}{C(x)}\right)$ | Take $\frac{F'}{F} = \alpha \frac{A'}{A} + \left(\frac{B}{C}\right)'$ and clear denominators | $A(x) C(x)^2 F'(x) - \bigl(\alpha A'(x) C(x)^2 + A(x)(B'C - BC')\bigr) F(x) = 0$ | Order $1$; width $\le \deg A + 2\deg C$ |
| **4. Logarithmic / Integral Form** $F(x) = A(x) \ln B(x)$ or $\int A(x)^\alpha dx$ | Differentiate once to eliminate $\ln$ or $\int$, then apply Rule 1 | For $F = \int A^\alpha dx$: $A(x) F''(x) - \alpha A'(x) F'(x) = 0$ | Order $2$ (or Order $1$ in $G = F'$) |

---

### 41.4 Small Hand-Checkable Example: Central Trinomial Coefficients
Let $T_n = [x^n](1 + x + x^2)^n$ be the number of king paths of $n$ steps from $(0, 0)$ to $(n, 0)$ using steps $(1, -1), (1, 0), (1, 1)$. By the constant-term / diagonal identity (Iteration 35), its OGF is:
$$F(x) = \sum_{n \ge 0} T_n x^n = \frac{1}{\sqrt{1 - 2x - 3x^2}} = (1 - 2x - 3x^2)^{-1/2}.$$
1. **Apply Recipe 1** ($A(x) = 1 - 2x - 3x^2$, $B(x) = 1$, $\alpha = -1/2$):
   $$\frac{F'(x)}{F(x)} = -\frac{1}{2} \frac{-2 - 6x}{1 - 2x - 3x^2} = \frac{1 + 3x}{1 - 2x - 3x^2}.$$
2. **Clear the denominator**:
   $$(1 - 2x - 3x^2) F'(x) - (1 + 3x) F(x) = 0.$$
3. **Extract $[x^{n-1}]$ for $n \ge 1$**:
   - $[x^{n-1}] F'(x) = n T_n$,
   - $[x^{n-1}] (-2x F'(x)) = -2(n-1) T_{n-1}$,
   - $[x^{n-1}] (-3x^2 F'(x)) = -3(n-2) T_{n-2}$,
   - $[x^{n-1}] (-F(x)) = -T_{n-1}$,
   - $[x^{n-1}] (-3x F(x)) = -3 T_{n-2}$.
   Summing these five terms gives the 3-term recurrence:
   $$n T_n = (2n - 1) T_{n-1} + 3(n - 1) T_{n-2} \qquad (n \ge 1, \; T_0 = 1, \; T_{-1} = 0).$$
4. **Hand Check**:
   - $n = 1$: $1 \cdot T_1 = 1 \cdot 1 + 0 = 1 \implies T_1 = 1$.
   - $n = 2$: $2 \cdot T_2 = 3 \cdot 1 + 3 \cdot 1 = 6 \implies T_2 = 3$ (matching $[x^2](1+x+x^2)^2 = 3$).
   - $n = 3$: $3 \cdot T_3 = 5 \cdot 3 + 6 \cdot 1 = 21 \implies T_3 = 7$ (matching $[x^3](1+x+x^2)^3 = 7$).
   - $n = 4$: $4 \cdot T_4 = 7 \cdot 7 + 9 \cdot 3 = 76 \implies T_4 = 19$ (matching $[x^4](1+x+x^2)^4 = 19$).

---

### 41.5 Failure Modes: Singular Points of the Indicial Polynomial & Modular Division Traps
When extracting a recurrence from $P(x) F'(x) + Q(x) F(x) = R(x)$, two distinct failure modes can cause the leading coefficient of $f_n$ to vanish:

1. **Failure Mode A (Regular Singular Point at $x = 0$ & Indicial Roots in Characteristic $0$)**:
   Suppose $p_0 = [x^0] P(x) = 0$, while $p_1 = [x^1] P(x) \neq 0$ (so $x = 0$ is a *regular singular point* of the ODE). Then extracting $[x^n]$ instead of $[x^{n-1}]$ yields:
   $$\underbrace{(n p_1 + q_0)}_{I(n)} f_n + \sum_{k \ge 1} \bigl((n - k) p_{k+1} + q_k\bigr) f_{n-k} = [x^n] R(x).$$
   The polynomial $I(n) = n p_1 + q_0$ is the **indicial polynomial**. If $I(n^*) = 0$ for some positive integer $n^* = -q_0 / p_1 \in \mathbb{Z}_{\ge 1}$, the recurrence **cannot determine $f_{n^*}$** from $f_0, \dots, f_{n^*-1}$!
   - **Concrete Counterexample**: Let $F(x) = 1 + x + \frac{3x^2}{1 - x} = 1 + x + 3x^2 + 3x^3 + \dots$, which satisfies $(x - x^2) F'(x) - 2 F(x) = -2 - x + 2x^2$. Here $p_1 = 1, q_0 = -2$, so $I(n) = n - 2$ vanishes at $n^* = 2$. At $n = 2$, the recurrence says $0 \cdot f_2 - 1 \cdot f_1 = -1$, which only verifies $f_1 = 1$ and leaves $f_2 = 3$ undetermined!
   - **Resolution**: Precompute or initialize $f_0, f_1, \dots, f_{n^*}$ up to the largest positive integer root $n^*$ of $I(n)$ directly from the combinatorial definition or small-degree series expansion before running the linear recurrence for $n > n^*$.

2. **Failure Mode B (Small Prime Characteristic $p \le N$ or $I(n) \equiv 0 \pmod p$ & The $p$-Adic Precision Loss Contract)**:
   Over $\mathbb{F}_p$, even when $x = 0$ is an ordinary point ($p_0 \neq 0$), the leading coefficient $n p_0$ vanishes at every multiple of $p$ ($n = p, 2p, \dots$). Worse yet, even when $N < p$, a shifted indicial polynomial $I(n) = a n + b$ with **no positive integer root in $\mathbb{Q}$** can vanish modulo $p$ at $n^* = (-b a^{-1}) \bmod p \in [1, N]$!
   - **Concrete Example**: If $I(n) = 2n - p$ or $I(n) = (N-1)n + 1$, then $I(n)$ never vanishes in $\mathbb{Q}$ for $n \in [1, N]$, but modulo $p = 998244353$, $I(n^*) \equiv 0 \pmod p$ at $n^* = (-b a^{-1}) \bmod p$.
   - **Why Naive $\bmod p$ Fails and How $p$-Adic Lifting ($\mathbb{Z}/p^{V+1}\mathbb{Z}$) Fixes It**:
     Suppose the true sequence $f_n \in \mathbb{Z}_{(p)}$ is $p$-integral for all $n \le N$, and let $V = \sum_{n=n_0}^N v_p\bigl(I(n)\bigr)$ be the total $p$-adic valuation of the leading polynomial across the target range $[n_0, N]$. (When $N < p$ and $\deg I = 1$, $I(n)$ has at most one root $n^* \in [n_0, N]$ modulo $p$, so typically $V = v_p(I(n^*)) = 1$.)
     If we run the recurrence over $\mathbb{Z}/p^{V+1}\mathbb{Z}$, each time we hit an index $n^*$ where $p^v \parallel I(n^*)$, the right-hand side $\text{RHS}_{n^*}$ is guaranteed to be divisible by $p^v$ (since $f_{n^*}$ is $p$-integral). Dividing $\text{RHS}_{n^*}$ by $p^v$ **loses $v$ digits of $p$-adic precision**:
     $$\frac{\text{RHS}_{n^*} \bmod p^{k}}{p^v} \quad \text{is well-defined modulo } p^{k - v}, \text{ NOT modulo } p^k!$$
     Because the total number of $p$-divisions across all $n \in [n_0, N]$ is $V$, starting with initial terms modulo $p^{V+1}$ ensures that after losing $V$ digits of $p$-adic precision across the singular steps, at least $p^{(V+1) - V} = p^1$ precision survives at every index, recovering the exact value of $f_n \bmod p$ for all $n \le N$!

---

## Iteration 42: Simplifying Differential Equations via Substitution & Sparse FPS Operations in $O(N \cdot K)$

### 42.1 Demystifying Differential Equation Substitutions ("How Would I Think of This Substitution?")
A recurring frustration when reading generating function editorials is seeing an ugly differential equation—such as $(1 - 4x) F'(x) - 2 F(x) = G(x)$, or $F'(x) = \frac{1}{2} A(x) F(x)^2 + 1$, or $D''(z) - a(z) D'(z) + b(z) D(z) = 0$—and watching the author pull a magic substitution out of thin air that collapses the ODE into a closed form.

In reality, **there are only five structural substitution archetypes for differential equations in combinatorics**, and each one can be reverse-engineered mechanically from a diagnostic clue in the equation:

| Archetype | Diagnostic Clue in the Ugly ODE | What Makes It Hard as Written? | Mechanical Reverse-Engineering Scratchpad (How to Derive the Substitution) |
| :--- | :--- | :--- | :--- |
| **1. Gauge / Integrating Factor Substitution** $F(x) = \mu(x) G(x)$ | Inhomogeneous first-order linear ODE: $F'(x) + a(x) F(x) = b(x)$ (or shifting away a first-derivative term in a 2nd-order ODE). | Both $F'(x)$ and $a(x)F(x)$ appear on the LHS, preventing direct integration of $b(x)$. | Write $F(x) = \mu(x) G(x)$. Then $F' + a F = \mu G' + (\mu' + a \mu) G$. To kill the $G$ term, set $\mu' + a \mu = 0 \implies \mu(x) = \exp(-\int a(x) dx)$. Then $G'(x) = \mu(x)^{-1} b(x) \implies F(x) = \mu(x) \left(F(0) + \int_0^x \mu(t)^{-1} b(t) dt\right)$! |
| **2. Independent-Variable Operator Normalization** $x = \psi(u)$ | Derivative $\frac{d}{dx}$ is multiplied by a recurrent weight $W(x) \frac{d}{dx}$ (e.g., $(1+x)\frac{d}{dx}$ or $\sqrt{1-4x}\frac{d}{dx}$). | $W(x)$ shifts degrees or introduces a square root $\sqrt{\Delta(x)}$. | By the Chain Rule, $\frac{d}{du} = \frac{dx}{du} \frac{d}{dx}$. To turn $W(x)\frac{d}{dx}$ into a pure derivative $\frac{d}{du}$, solve $\frac{dx}{du} = W(x)$! <br>• If $W(x) = 1+x$: $x = e^u - 1 \implies (1+x)\frac{d}{dx} = \frac{d}{du}$.<br>• If $W(x) = \sqrt{1-4x}$: set $\sqrt{1-4x} = 1 - 2u \implies x = u(1-u)$, and miraculously $\frac{dx}{du} = 1 - 2u = \sqrt{1-4x}$, so $\sqrt{1-4x}\frac{d}{dx} = \frac{d}{du}$! |
| **3. Autonomous / Separable Inversion** $x = \int \frac{dF}{\Psi(F)}$ | Removing the root vertex in an EGF gives $F'(x) = \Psi(F(x))$ or $F'(x) = A'(x) \Psi(F(x))$. | Non-linear in $F(x)$, so coefficient extraction has an $m$-fold convolution $\Psi(F)$. | Swap roles of independent and dependent variables! Since $\frac{dF}{dA} = \Psi(F)$, separate variables: $\int_{F(0)}^{F(x)} \frac{du}{\Psi(u)} = A(x) - A(0)$. Integrate the rational/elementary function $\frac{1}{\Psi(u)}$ in closed form $H(F(x)) = A(x)$, then invert $H$ analytically or via `revert`! |
| **4. Riccati Logarithmic-Derivative Linearization** $F(x) = -\frac{1}{a(x)} \frac{U'(x)}{U(x)}$ | Quadratic non-linearity $F'(x) = a(x) F(x)^2 + b(x) F(x) + c(x)$. | The $F(x)^2$ term causes naive coefficient extraction to cost $O(N^2)$ or $O(N \log^2 N)$. | Recall how differentiating a log-derivative produces a square: $\left(\frac{U'}{U}\right)' = \frac{U''}{U} - \left(\frac{U'}{U}\right)^2$. Substitute $F = -\frac{1}{a} \frac{U'}{U}$: the $-\frac{1}{a}\left(\frac{U'}{U}\right)^2$ in $F'$ **cancels $a F^2$ identically**, leaving the **linear** 2nd-order D-finite ODE $a U'' - (a' + ab) U' + a^2 c U = 0$! |
| **5. Composite D-Finite Chain-Rule + Gauge Reduction** $D(z) = h(z) B(t(z))$ | A simple hypergeometric/Bessel series $B(t)$ is composed with a rational $t(z)$ and scaled by $h(z)$. | Computing $B(t(z))$ via polynomial composition takes $O(N \log^2 N)$ and misses the $O(N)$ recurrence. | Split into two simple steps: (1) Let $U(z) = B(t(z))$ and use $B''(t) + \alpha(t) B'(t) + \beta(t) B(t) = 0$ + Chain Rule to get a 2nd-order ODE for $U(z)$; (2) Substitute $U(z) = h(z)^{-1} D(z)$ via $q(z) = \frac{h'(z)}{h(z)}$! |

#### Worked Demonstration 1: Archetype 1 + Archetype 2 (Catalan Substitution Inside an ODE)
Suppose a counting problem yields the inhomogeneous differential equation:
$$(1 - 4x) F'(x) - 2 F(x) = \frac{1}{1 - 3x}, \qquad F(0) = 1.$$
1. **Diagnose**: The homogeneous part $(1 - 4x) F' - 2 F = 0$ has integrating factor $\mu(x) = (1 - 4x)^{-1/2}$, which involves the Catalan radical $\sqrt{1 - 4x}$.
2. **Apply Archetype 1 + Archetype 2**:
   - First apply **Archetype 1 (Integrating Factor)**: Since $\bigl(\sqrt{1 - 4x} F(x)\bigr)' = \frac{(1 - 4x) F'(x) - 2 F(x)}{\sqrt{1 - 4x}}$, divide the ODE by $\sqrt{1 - 4x}$:
     $$\frac{d}{dx} \Bigl(\sqrt{1 - 4x} F(x)\Bigr) = \frac{1}{(1 - 3x)\sqrt{1 - 4x}}.$$
   - Next apply **Archetype 2 (Rationalizing Substitution $x = u(1-u)$)**: Set $\sqrt{1 - 4x} = 1 - 2u$, so $x = u(1 - u)$ and $dx = (1 - 2u)\,du = \sqrt{1 - 4x}\,du$!
   - Notice the exact cancellation: $\frac{dx}{\sqrt{1 - 4x}} = du$! Thus, in the $u$-variable, the differential equation becomes a pure rational derivative with **no square roots**:
     $$\frac{d}{du} \Bigl((1 - 2u) F(u(1-u))\Bigr) = \frac{1}{1 - 3u(1-u)} = \frac{1}{1 - 3u + 3u^2}!$$

#### Worked Demonstration 2: Archetype 3 (Autonomous ODE $F'(x) = \Psi(F(x))$ in Alternating Permutations)
Suppose we want the EGF $F(x) = \sum_{n \ge 0} E_n \frac{x^n}{n!}$ of **alternating permutations** $\pi_1 < \pi_2 > \pi_3 < \pi_4 > \dots$ of $\{1, \dots, n\}$.
1. **Combinatorial Root-Removal (Differentiation)**:
   In any alternating permutation of $n + 1$ elements, removing the minimum element $1$ splits the permutation into two independent alternating permutations of sizes $i$ and $n - i$ (with $i$ odd). Summing over both up-down and down-up orientations for $n \ge 1$ gives the autonomous non-linear ODE:
   $$F'(x) = \frac{1 + F(x)^2}{2}, \qquad F(0) = 1.$$
2. **Mechanical Separation of Variables**:
   Instead of expanding $F(x)^2$ term-by-term, write $\frac{dF}{1 + F^2} = \frac{1}{2} dx$ and integrate from $x = 0$ ($F(0) = 1$):
   $$\arctan(F(x)) - \frac{\pi}{4} = \frac{x}{2} \implies F(x) = \tan\!\left(\frac{x}{2} + \frac{\pi}{4}\right) = \sec x + \tan x = \frac{1 + \sin x}{\cos x}!$$

#### Worked Demonstration 3: Archetype 5 (Two-Step Derivation of the QOJ #60 Bessel ODE in Chapter 19)
In [`19-frontier-capstones/chapter.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/19-frontier-capstones/chapter.qmd#L130-L152) (`#rectangular-components`, **QOJ #60 Chinese Elephant Chess**), counting $n \times (n+d)$ binary matrices with row/column sums $\le 2$ reduces to extracting $[z^n] D_d(z)$, where:
$$D_d(z) = h(z) B_d\bigl(t(z)\bigr), \qquad B_d(t) = \sum_{r \ge 0} \frac{t^r}{r!(r+d)!}, \qquad t(z) = z J(z)^2, \qquad h(z) = H(z) J(z)^d.$$
How do we derive the second-order linear ODE for $D_d(z)$ without guesswork?
1. **Base Hypergeometric ODE for $B_d(t)$**:
   The term ratio of $B_d(t)$ is $\frac{c_r}{c_{r-1}} = \frac{1}{r(r+d)}$, so $\vartheta_t(\vartheta_t + d) B_d(t) = t B_d(t)$. Since $\vartheta_t^2 = t^2 \frac{d^2}{dt^2} + t \frac{d}{dt}$, dividing by $t$ gives the Bessel ODE:
   $$t B_d''(t) + (d + 1) B_d'(t) - B_d(t) = 0 \iff B_d''(t) = -\frac{d+1}{t} B_d'(t) + \frac{1}{t} B_d(t).$$
2. **Step 1 (Chain-Rule Substitution $U(z) = B_d(t(z))$)**:
   Differentiate $U(z) = B_d(t(z))$ twice with respect to $z$:
   $$U'(z) = t'(z) B_d'(t(z)) \implies B_d'(t(z)) = \frac{U'(z)}{t'(z)},$$
   $$U''(z) = t''(z) B_d'(t(z)) + \bigl(t'(z)\bigr)^2 B_d''(t(z)).$$
   Substitute $B_d''(t)$ and $B_d'(t)$ into $U''(z)$:
   $$U''(z) = \underbrace{\left(\frac{t''(z)}{t'(z)} - (d+1)\frac{t'(z)}{t(z)}\right)}_{a(z)} U'(z) + \underbrace{\frac{(t'(z))^2}{t(z)}}_{b(z)} U(z) \iff U''(z) - a(z) U'(z) - b(z) U(z) = 0.$$
3. **Step 2 (Archetype 1 Gauge Substitution $D_d(z) = h(z) U(z)$)**:
   Let $q(z) = \frac{h'(z)}{h(z)}$ (which is a known rational function of $z$). Since $U = h^{-1} D_d$:
   - $\frac{D_d'}{h} = U' + q U \implies U' = \frac{D_d'}{h} - q U$,
   - $\frac{D_d''}{h} = U'' + 2q U' + (q^2 + q') U = U'' + 2q\left(\frac{D_d'}{h} - q U\right) + (q^2 + q')U \implies U'' = \frac{D_d''}{h} - 2q \frac{D_d'}{h} + (q^2 - q') U$.
   Plugging $U, U', U''$ into $U'' - a U' - b U = 0$ and multiplying by $h(z)$ yields the exact ODE verified in [`tests/audit_frontier_math.py`](file:///home/maomao90/Documents/IO/ICPC-math-notes/tests/audit_frontier_math.py#L183-L186):
   $$D_d''(z) - \bigl(2q(z) + a(z)\bigr) D_d'(z) + \bigl(q(z)^2 - q'(z) + a(z) q(z) - b(z)\bigr) D_d(z) = 0!$$

---

### 42.2 The $O(N \cdot K)$ Sparse FPS Engine (`inv`, `div`, `exp`, `ln`, `pow`, $\sqrt{\cdot}$, $F(P(x))$)
When the input polynomial $A(x) = \sum_{j \in S} a_j x^j$ is **sparse**—having at most $K = |S| \ll N$ non-zero coefficients (for instance, $A(x) = 1 - x^c$, or $1 + x + x^2$, or Euler's pentagonal series $\sum_{k} (-1)^k x^{k(3k-1)/2}$ where $K = O(\sqrt{N})$)—calling dense $O(N \log N)$ NTT routines wastes time and memory. Instead, we convert each transcendental FPS operation into a first-order linear ODE and extract $[x^n]$ directly in **$O(N \cdot K)$ time**!

#### Precomputation Contract for Division-Free Inner Loops
To avoid an $O(\log p)$ modular exponentiation inside the $n = 1 \dots N$ loop, always precompute the linear modular inverses $\text{inv}[1 \dots N]$ in $O(N)$ time via:
$$\text{inv}[1] = 1, \qquad \text{inv}[n] = (p - \lfloor p / n \rfloor) \cdot \text{inv}[p \bmod n] \bmod p \qquad (2 \le n \le N < p).$$

#### Complete Table of $O(N \cdot K)$ Sparse FPS Recurrences
Let $S = \{j \in [1, N] : a_j \neq 0\}$ be the set of positive non-zero indices of $A(x)$, with $|S| \le K$.

| Operation | Defining ODE Identity | Exact $O(N \cdot K)$ Coefficient Recurrence ($n = 1, 2, \dots, N$) | Required Algebraic Preconditions |
| :--- | :--- | :--- | :--- |
| **1. Sparse Inversion** $F = A^{-1}$ | $A(x) F(x) = 1$ | $f_0 = a_0^{-1}$, <br>$f_n = -a_0^{-1} \sum_{\substack{j \in S \\ j \le n}} a_j f_{n-j}$ | $a_0 \in R^\times$ is a unit (no division by $n$ needed; works in **any** characteristic!). |
| **2. Sparse Division** $F = B / A$ ($A$ sparse) | $A(x) F(x) = B(x)$ | $f_0 = b_0 a_0^{-1}$, <br>$f_n = a_0^{-1} \Bigl(b_n - \sum_{\substack{j \in S \\ j \le n}} a_j f_{n-j}\Bigr)$ | $a_0 \in R^\times$ is a unit ($B$ can be completely dense!). |
| **3. Sparse Exponential** $F = \exp(A)$ | $F'(x) = A'(x) F(x)$ | $f_0 = 1$, <br>$f_n = \frac{1}{n} \sum_{\substack{j \in S \\ j \le n}} j \, a_j \, f_{n-j}$ | $a_0 = 0$; $1, 2, \dots, N \in R^\times$ are units ($N < p$). |
| **4. Sparse Logarithm** $F = \ln(A)$ | $A(x) F'(x) = A'(x)$ | Let $g_n = n f_n$ ($n \ge 1$): <br>$g_n = a_0^{-1} \Bigl(n a_n - \sum_{\substack{j \in S \\ 1 \le j < n}} a_j g_{n-j}\Bigr)$, then $f_n = \frac{g_n}{n}$ | $a_0 = 1$ (or $a_0 \in R^\times$ for normalized $\ln(A/a_0)$); $1, \dots, N \in R^\times$. |
| **5. Sparse Power** $F = A(x)^\alpha$ ($\alpha \in K$) | $A(x) F'(x) = \alpha A'(x) F(x)$ | Strip valuation $v = v(A)$ first so $a_0 \in K^\times$. Set $f_0 = a_0^\alpha$, and for $n \ge 1$: <br>$f_n = \frac{1}{n a_0} \sum_{\substack{j \in S \\ j \le n}} \bigl((\alpha + 1) j - n\bigr) a_j f_{n-j}$ | After shifting by $v(A)$, $a_0 \in K^\times$ and $1, \dots, N \in K^\times$. Covers **Sparse Sqrt** ($\alpha = \frac{1}{2}$) and **Sparse Inverse Power** ($\alpha = -m$)! |
| **6. Sparse Composition & Chaining** $H(x) = F(P(x))$ ($P$ sparse) | • If $F \in \{\exp, \ln, (\cdot)^\alpha, \text{inv}\}$: apply Rows 1–5 directly to $P(x)$ in **$O(N \cdot K)$**!<br>• If $F(y)$ satisfies $A(y)F'(y) + B(y)F(y) = C(y)$: $A(P(x)) H'(x) + B(P(x)) P'(x) H(x) = C(P(x)) P'(x)$ | • For $H(x) = \frac{P(x)^\alpha}{Q(x)^\beta}$ ($P, Q$ sparse): first compute $U = P(x)^\alpha$ in $O(NK)$ via Row 5, then if $\beta = 1$ apply Row 2 ($H = U / Q$) in $O(NK)$, or convolve $P^\alpha$ and $Q^{-\beta}$!<br>• For general order-$1$ ODE, keep auxiliary powers as coupled $O(NK)$ recurrences or expand $A(P(x))$ in $O(N \cdot K^{\deg A})$. | $P(0) = 0$ (or $F(P(0))$ known); leading coefficient invertible. |

#### Derivation of the Sparse Power Recurrence (Row 5)
Why does $A(x) F'(x) = \alpha A'(x) F(x)$ yield the single-sum formula above?
Extract $[x^{n-1}]$ from both sides of $A(x) F'(x) = \alpha A'(x) F(x)$:
- LHS: $[x^{n-1}] \bigl(A(x) F'(x)\bigr) = n a_0 f_n + \sum_{j \in S, j \le n} (n - j) a_j f_{n-j}$.
- RHS: $[x^{n-1}] \bigl(\alpha A'(x) F(x)\bigr) = \sum_{j \in S, j \le n} \alpha j a_j f_{n-j}$.
Move the $j \ge 1$ sum from the LHS to the RHS:
$$n a_0 f_n = \sum_{\substack{j \in S \\ j \le n}} \bigl(\alpha j - (n - j)\bigr) a_j f_{n-j} = \sum_{\substack{j \in S \\ j \le n}} \bigl((\alpha + 1)j - n\bigr) a_j f_{n-j}!$$

#### Small Hand-Checkable Example: Sparse Square Root $F(x) = (1 + 2x + x^3)^{1/2} \bmod x^5$
Here $a_0 = 1$, $\alpha = 1/2$ (so $\alpha + 1 = 3/2$), and the sparse support is $S = \{1, 3\}$ with $a_1 = 2, a_3 = 1$.
- $f_0 = 1^{1/2} = 1$.
- $n = 1$: $f_1 = \frac{1}{1} \bigl((\frac{3}{2}\cdot 1 - 1) a_1 f_0\bigr) = \frac{1}{2} \cdot 2 \cdot 1 = 1$.
- $n = 2$: $f_2 = \frac{1}{2} \bigl((\frac{3}{2}\cdot 1 - 2) a_1 f_1\bigr) = \frac{1}{2} \bigl(-\frac{1}{2} \cdot 2 \cdot 1\bigr) = -\frac{1}{2}$.
- $n = 3$: $f_3 = \frac{1}{3} \bigl((\frac{3}{2}\cdot 1 - 3) a_1 f_2 + (\frac{3}{2}\cdot 3 - 3) a_3 f_0\bigr) = \frac{1}{3} \bigl(-\frac{3}{2} \cdot 2 \cdot (-\frac{1}{2}) + \frac{3}{2} \cdot 1 \cdot 1\bigr) = \frac{1}{3}\bigl(\frac{3}{2} + \frac{3}{2}\bigr) = 1$.
- $n = 4$: $f_4 = \frac{1}{4} \bigl((\frac{3}{2}\cdot 1 - 4) a_1 f_3 + (\frac{3}{2}\cdot 3 - 4) a_3 f_1\bigr) = \frac{1}{4} \bigl(-\frac{5}{2} \cdot 2 \cdot 1 + \frac{1}{2} \cdot 1 \cdot 1\bigr) = -\frac{9}{8}$.
**Verification**: Squaring $1 + x - \frac{1}{2}x^2 + x^3 - \frac{9}{8}x^4 \bmod x^5$:
- $[x^0] = 1$,
- $[x^1] = 2$,
- $[x^2] = 2(-1/2) + 1^2 = 0$,
- $[x^3] = 2(1) + 2(1)(-1/2) = 1$,
- $[x^4] = 2(-9/8) + 2(1)(1) + (-1/2)^2 = -\frac{9}{4} + 2 + \frac{1}{4} = 0$.
Matches $1 + 2x + x^3 \bmod x^5$ identically!

---

## Iteration 43: Euler Homogeneous PDEs for Multivariate Series & Holonomic Reductions of Binomial Sums

### 43.1 Euler's Homogeneous PDE & Cross-Partial Elimination for Bivariate Series
When a bivariate generating function $F(x, y) = \sum_{n, m \ge 0} f_{n,m} x^n y^m$ is given by a power or exponential of a sparse bivariate polynomial $A(x, y)$, we have **two** partial derivatives $\frac{\partial F}{\partial x}$ and $\frac{\partial F}{\partial y}$:
1. **Weighted Euler Homogeneity**:
   If a combinatorial class satisfies $a \cdot (\text{exponent of } x) + b \cdot (\text{exponent of } y) = c$ on a graded component, then:
   $$\left(a x \frac{\partial}{\partial x} + b y \frac{\partial}{\partial y}\right) F(x, y) = c F(x, y).$$
2. **Cross-Partial Elimination for $F(x, y) = A(x, y)^\alpha$**:
   Taking partial logarithmic derivatives with respect to $x$ and $y$ gives two coupled PDEs:
   $$A(x, y) \frac{\partial F}{\partial x} = \alpha \frac{\partial A}{\partial x} F(x, y), \qquad A(x, y) \frac{\partial F}{\partial y} = \alpha \frac{\partial A}{\partial y} F(x, y).$$
   Furthermore, multiplying the first by $\frac{\partial A}{\partial y}$ and the second by $\frac{\partial A}{\partial x}$ eliminates $\alpha F(x, y)$ completely:
   $$\frac{\partial A}{\partial y} \frac{\partial F}{\partial x} - \frac{\partial A}{\partial x} \frac{\partial F}{\partial y} = 0!$$
   When we only want a single row $R_n(y) = [x^n] F(x, y)$ as a polynomial in $y$ (for fixed huge $n \le 10^9$ and $m = 0 \dots K$), extracting $[x^n]$ from a linear combination of the $x$-PDE and $y$-PDE eliminates shifts in $n$ and produces a **pure ODE in $y$** for $R_n(y)$!

---

### 43.2 Three Systematic Pipelines for Reducing Binomial Sums to $O(N)$ P-Recursive Recurrences
Suppose we need to compute $S_n = \sum_{k=0}^n T(n, k)$ for $n = 0, 1, \dots, N$ (where $N \le 10^7$), and $T(n, k)$ is a product of binomial coefficients and powers such as $\binom{n}{k}^2 x^k$, $\binom{n}{k}\binom{n+k}{k}$, or $\binom{2k}{k}\binom{2(n-k)}{n-k}$. How do we find the $O(N)$ P-recursive recurrence for $S_n$ **by hand** during a contest?

#### Pipeline A: Bivariate OGF $\to$ Algebraic Diagonal $\to$ First-Order Linear ODE
Whenever $S_n = \sum_{k=0}^n \binom{n}{k} \binom{a n + b k + c}{d n + e k} x^k$ is a convolution or diagonal of two binomials:
1. Form the OGF $G(t) = \sum_{n \ge 0} S_n t^n$ by swapping the sum over $n$ and $k$, or express $S_n = [t^n z^0] F(t, z)$ as a constant term in $z$ and extract the formal residue (Furstenberg's method, Iteration 36) to obtain an **algebraic closed form** $G(t) = \Delta(t)^{-1/2}$.
2. Apply **Recipe 1 of Iteration 41** ($\Delta(t) G'(t) + \frac{1}{2}\Delta'(t) G(t) = 0$) and extract $[t^{n-1}]$!

- **Worked Derivation for the Narayana / Legendre Sum $S_n(x) = \sum_{k=0}^n \binom{n}{k}^2 x^k$**:
  1. Write $\binom{n}{k}^2 x^k = \binom{n}{k} [z^{n-k}] (1 + xz)^n$, so by the Binomial Theorem:
     $$S_n(x) = [z^n] \bigl((1 + z)(1 + xz)\bigr)^n.$$
  2. By the Diagonal / Lagrange Change-of-Variables Formula ($w = \frac{z}{(1+z)(1+xz)}$), the OGF $G(t) = \sum_{n \ge 0} S_n(x) t^n$ is:
     $$G(t) = \frac{1}{\sqrt{1 - 2(1+x)t + (1-x)^2 t^2}}.$$
  3. Take the logarithmic derivative with respect to $t$:
     $$\bigl(1 - 2(1+x)t + (1-x)^2 t^2\bigr) G'(t) - \bigl((1+x) - (1-x)^2 t\bigr) G(t) = 0.$$
  4. Extract $[t^n]$ to get the 3-term P-recursive recurrence valid for any parameter $x \in K$:
     $$(n + 1) S_{n+1}(x) = (2n + 1)(1 + x) S_n(x) - n(1 - x)^2 S_{n-1}(x)!$$

#### Pipeline B: Direct Hypergeometric Differential Operator ($\vartheta = x \frac{d}{dx}$)
Suppose $F(x) = \sum_{k \ge 0} c_k x^k$ is a hypergeometric series whose consecutive term ratio is a rational function of $k$:
$$\frac{c_{k+1}}{c_k} = \frac{P(k)}{Q(k+1)}, \qquad Q(0) = 0.$$
Since $\vartheta x^k = k x^k$, applying the operator $Q(\vartheta)$ to $F(x)$ gives:
$$Q(\vartheta) F(x) = \sum_{k \ge 1} Q(k) c_k x^k = x \sum_{k \ge 0} Q(k+1) c_{k+1} x^k = x \sum_{k \ge 0} P(k) c_k x^k = x P(\vartheta) F(x)!$$
Thus $F(x)$ immediately satisfies the differential equation:
$$\bigl(Q(\vartheta) - x P(\vartheta)\bigr) F(x) = 0!$$
- **Example**: For $S_n(x) = \sum_{k=0}^n \binom{n}{k}^2 x^k$, the term ratio in $k$ is $\frac{c_{k+1}}{c_k} = \frac{(n-k)^2}{(k+1)^2}$, so $Q(k) = k^2$ and $P(k) = (n-k)^2$. Instantly, $\bigl(\vartheta^2 - x(n - \vartheta)^2\bigr) S_n(x) = 0$, which is a second-order linear ODE in $x$!

#### Pipeline C: Hand-Driven Creative Telescoping (Zeilberger's Method) & Boundary Trap
To find a recurrence in $n$ for $S_n = \sum_k F(n, k)$ directly from the summand $F(n, k)$:
1. Divide $\sum_{i=0}^r q_i(n) F(n+i, k)$ by $F(n, k)$ so every term is a rational function of $(n, k)$ with common denominator, and match the numerator against $\Delta_k \bigl(R(n, k) F(n, k)\bigr) = G(n, k+1) - G(n, k)$.
2. **Failure Mode (Non-Zero Boundary Terms when the Upper Limit Truncates Non-Zero Summands)**:
   If the sum is truncated at $k = m$ (e.g., $S_n = \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{k}$) where $\binom{n}{k}$ does **not** vanish at $k = \lfloor n/2 \rfloor + 1$, summing $G(n, k+1) - G(n, k)$ from $k = 0$ to $m$ does **not** telescope to $0$! Instead, it telescopes to the explicit boundary term $G(n, m+1) - G(n, 0)$. For example, with $H(n, k) = -\binom{n}{k-1}$, Pascal's identity gives $\binom{n+1}{k} - 2\binom{n}{k} = H(n, k+1) - H(n, k)$, so summing $k = 0 \dots m$ yields $S_{n+1, m} - 2 S_{n, m} = -\binom{n}{m}$ rather than $0$!

---

## Iteration 44: Divide-and-Conquer FFT (CDQ NTT) & Semi-Online Convolutions

### 44.1 Semi-Online Recurrences & Why Direct FPS Inversion Fails when $\psi_n$ Varies with $n$
Consider a recurrence of the form:
$$f_n = \psi_n\!\left( c_n + \sum_{i=0}^{n-1} f_i \, g_{n-i} \right) \qquad (1 \le n \le N),$$
where:
- The sequence $g_1, g_2, \dots, g_N$ (and $c_1, \dots, c_N$) is **completely known in advance (offline)**,
- The sequence $f_0, f_1, \dots, f_N$ is **unknown**, and at step $n$, after accumulating the convolution sum $\text{acc}_n = \sum_{i=0}^{n-1} f_i g_{n-i}$, we apply an index-dependent transformation $\psi_n(\text{acc}_n)$ to obtain $f_n$ before moving to $n+1$.

**When can we avoid CDQ NTT, and when is CDQ NTT mandatory?**
- **Case 1 ($\psi_n$ is the identity, $f_n = c_n + \sum_{i=0}^{n-1} f_i g_{n-i}$)**:
  This is a pure linear convolution $F(x) = C(x) + F(x) G(x) \implies F(x) = \frac{C(x)}{1 - G(x)} \bmod x^{N+1}$. Solve it in **$O(N \log N)$ via a single FPS `inv`** (Newton iteration), which is $3\times$–$5\times$ faster than CDQ NTT!
- **Case 2 ($\psi_n$ depends on $n$ or is non-linear)**:
  - **Example A (FPS $\exp$ / Connected Graph EGFs)**: $f_n = \frac{1}{n} \sum_{i=0}^{n-1} f_i \bigl((n-i) a_{n-i}\bigr)$. Here $\psi_n(s) = \frac{s}{n}$ divides by $n$ at each step!
  - **Example B (DP with Position-Dependent Multipliers)**: $f_n = w_n \sum_{i=0}^{n-1} f_i g_{n-i}$, where $w_n$ is an arbitrary input array (so $w_n f_n$ is not a polynomial differential operator $P(\vartheta)$).
  - **Example C ($\min / \max$ + Convolution in Expected-Value Graph DP, e.g., CF 553E)**: At time $t$, a vertex chooses the minimum over outgoing edges of expected future cost $\sum_{k \ge 1} p_{e, k} dp[v][t - k]$.
  In all three subcases of Case 2, $f_n$ cannot be finalized until $\text{acc}_n = \sum_{i=0}^{n-1} f_i g_{n-i}$ has been fully accumulated, and no future $f_m$ ($m > n$) can use $f_n$ until $\psi_n$ has been applied!

---

### 44.2 The CDQ Divide-and-Conquer NTT Algorithm (`分治 NTT`)
Initialize $\text{acc}[0 \dots N] \gets 0$ and $f_0$ to the base case. Define the recursive procedure $\text{CDQ}(l, r)$ over the index interval $[l, r]$:
1. **Base Case ($l = r$)**:
   If $l > 0$, finalize $f_l \gets \psi_l(c_l + \text{acc}[l])$. Return.
2. **Divide**:
   Let $\text{mid} = \lfloor (l + r) / 2 \rfloor$.
3. **Conquer Left Half**:
   Call $\text{CDQ}(l, \text{mid})$. Upon return, all values $f_l, f_{l+1}, \dots, f_{\text{mid}}$ are **100% finalized**!
4. **Cross-Contribution via NTT (Left $\to$ Right)**:
   Form the polynomial slice $A(x) = \sum_{i=l}^{\text{mid}} f_i x^{i - l}$ (of degree $\text{mid} - l$) and the known kernel slice $B(x) = \sum_{j=1}^{r - l} g_j x^j$ (of degree $r - l$).
   Multiply $C(x) = A(x) B(x)$ via NTT of length $2^{\lceil \log_2(r - l + \text{mid} - l + 1) \rceil}$, and for each target index $n \in [\text{mid} + 1, r]$, accumulate:
   $$\text{acc}[n] \gets \text{acc}[n] + [x^{n - l}] C(x) = \text{acc}[n] + \sum_{i=l}^{\text{mid}} f_i \, g_{n - i}.$$
5. **Conquer Right Half**:
   Call $\text{CDQ}(\text{mid} + 1, r)$.

```
CDQ Interval [l, r] with midpoint mid = (l + r) // 2:
  [ l ............ mid ]  (1) Recursively solved first -> f[l..mid] finalized!
            |
            +--- (2) Convolve f[l..mid] with g[1..r-l] via NTT ---> Accumulate into:
                                                                    [ mid+1 ........ r ]
                                                                    (3) Recursively solve right half!
```

---

### 44.3 Rigorous Disjointness & Completeness Invariant
**Theorem (LCA Partition Invariant)**: For every pair of indices $(i, n)$ satisfying $0 \le i < n \le N$, the product $f_i g_{n-i}$ is added to $\text{acc}[n]$ **exactly once**, and this addition occurs **before** the base case $\text{CDQ}(n, n)$ finalizes $f_n$.

*Proof*: Consider the binary recursion tree over $[0, N]$. Since $0 \le i < n \le N$, the leaves $[i, i]$ and $[n, n]$ are distinct, so they have a **unique Lowest Common Ancestor (LCA)** interval $[l, r]$ in the recursion tree where $i$ falls into the left child $[l, \text{mid}]$ ($l \le i \le \text{mid}$) and $n$ falls into the right child $[\text{mid}+1, r]$ ($\text{mid}+1 \le n \le r$).
- **Existence & Uniqueness**: At this unique LCA node $[l, r]$, $1 \le n - i \le r - l$, so the cross-convolution in Step 4 includes the exact term $f_i g_{n-i}$ in $[x^{n-l}] C(x)$ and adds it to $\text{acc}[n]$. No other node in the recursion tree ever pairs $i \in [l', \text{mid}']$ with $n \in [\text{mid}'+1, r']$.
- **Causality**: By structural induction on the pre-order traversal of the recursion tree, every ancestor $[l, r]$ of $[i, i]$ and $[n, n]$ finishes its left subtree $\text{CDQ}(l, \text{mid})$ (which contains $[i, i]$) *before* executing Step 4, and executes Step 4 *before* entering its right subtree $\text{CDQ}(\text{mid}+1, r)$ (which contains $[n, n]$). Thus $f_i$ is already finalized when Step 4 runs, and all cross-contributions for $0 \le i < n$ have been added to $\text{acc}[n]$ before $\text{CDQ}(n, n)$ is reached! $\blacksquare$

**Complexity**: At depth $d$ of the recursion tree, there are $2^d$ intervals of length $L = N / 2^d$, and each performs an NTT of size $\le \frac{3}{2} L$ in $O(L \log L)$ time. Summing across $\lceil \log_2 N \rceil$ levels gives $O(N \log^2 N)$ time and $O(N)$ auxiliary space.
