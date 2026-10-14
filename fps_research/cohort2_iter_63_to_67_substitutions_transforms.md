# Cohort 2, Iterations 63–67: Rational & Radical Substitutions, Falling-Factorial Basis Transforms, Power-Sum Logarithmic Derivatives, and Roots of Unity Filters

---

## Iteration 63: Polynomial Taylor Shift & Rational Linear Substitutions ($GL_2$ Möbius Action, Krawtchouk Transform, and Euler Transform)

### 1. Concrete Counting Models & The Two Regimes of Linear Substitution

Before writing down a transformation matrix, we must distinguish two fundamentally different algebraic objects on which a rational linear substitution acts:

1. **Finite-Degree Polynomials (Projective $GL_2(K)$ Action)**:
   Suppose we have a polynomial $F(x) = \sum_{k=0}^n f_k x^k \in K[x]$ of fixed degree at most $n$, where $f_k$ counts configurations of weight $k$ inside a bounded universe of size $n$ (for example, $f_k$ is the number of subsets of size $k$, or the coefficient of $x^k$ in a probability generating function of $n$ coins). When each item's weight generator $x$ is replaced by a rational linear combination of two states — such as replacing $x$ by $\frac{1-x}{1+x}$ during a parity-flip transition on an $n$-bit hypercube, or computing $\sum_{k=0}^n f_k (a x + b)^k (c x + d)^{n-k}$ — clearing the denominator $(cx+d)^n$ yields a new polynomial of degree at most $n$:
   $$G(x) = (\mathcal{M}_g F)(x) := (cx+d)^n F\!\left(\frac{ax+b}{cx+d}\right) = \sum_{k=0}^n f_k (ax+b)^k (cx+d)^{n-k}.$$
   Here the degree $n$ is fixed in advance, and the substitution is an exact linear operator on the $(n+1)$-dimensional vector space $K[x]_{\le n}$.

2. **Truncated Formal Power Series (Infinite-Series Euler Transform)**:
   Suppose instead that $F(x) = \sum_{k \ge 0} f_k x^k \in K[[x]]$ is an infinite formal power series truncated at $x^N$, and we wish to compute the first $N$ terms of
   $$H(x) = (1 - cx)^{-\alpha} F\!\left(\frac{ax}{1 - cx}\right) \bmod x^N = \sum_{k=0}^{N-1} f_k a^k x^k (1 - cx)^{-(k+\alpha)} \bmod x^N.$$
   Crucially, the constant term of the numerator $ax$ is **zero**, so $\frac{ax}{1-cx} \in x K[[x]]$ has positive $x$-adic valuation. Therefore $(ax)^k$ vanishes modulo $x^N$ for all $k \ge N$, and the infinite sum truncates to a finite degree-$(N-1)$ operator!

Recognizing whether a problem lives in the projective degree-$n$ regime (where $b$ may be nonzero, as in $\frac{1-x}{1+x}$) or the $x$-adic Euler regime (where $b=0$) determines the exact reduction to Taylor shifts.

---

### 2. Elementary Generators and the $O(n \log n)$ Taylor Shift

Let $K$ be a commutative ring in which $n!$ is a unit (for NTT primes $p$, this requires $n < p$). The group $GL_2(K)$ of invertible $2 \times 2$ matrices
$$g = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \qquad \det(g) = ad - bc \in K^\times,$$
acts on $V_n = K[x]_{\le n}$ from the right via
$$(\mathcal{M}_g F)(x) = (cx+d)^n F\!\left(\frac{ax+b}{cx+d}\right).$$
Let us verify that this is a genuine group action by homogenizing $F(x)$ to the degree-$n$ bivariate polynomial $\widetilde{F}(X, Y) = Y^n F(X/Y) = \sum_{k=0}^n f_k X^k Y^{n-k}$. Then
$$(\mathcal{M}_g F)(x) = \widetilde{F}(ax+b, cx+d) = \widetilde{F}\!\left((x, 1) \begin{pmatrix} a & c \\ b & d \end{pmatrix}\right).$$
Because matrix multiplication is associative, applying $g_1$ followed by $g_2$ corresponds to multiplying their matrices: $\mathcal{M}_{g_1 g_2}(F) = \mathcal{M}_{g_2}(\mathcal{M}_{g_1}(F))$.

Every matrix in $GL_2(K)$ can be factored into three types of elementary transformations, each of which acts on the coefficient array $[f_0, f_1, \dots, f_n]$ in $O(n)$ or $O(n \log n)$ time:

1. **Diagonal Scaling ($D_{\lambda, \mu} = \begin{pmatrix} \lambda & 0 \\ 0 & \mu \end{pmatrix}$)**:
   $$(\mathcal{M}_{D_{\lambda,\mu}} F)(x) = \sum_{k=0}^n f_k (\lambda x)^k \mu^{n-k} = \sum_{k=0}^n \left(f_k \lambda^k \mu^{n-k}\right) x^k.$$
   **Cost**: $O(n)$ point-wise scalar multiplications.

2. **Polynomial Reversal ($J = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$)**:
   $$(\mathcal{M}_J F)(x) = x^n F(1/x) = \sum_{k=0}^n f_k x^{n-k} = \sum_{j=0}^n f_{n-j} x^j.$$
   **Cost**: $O(n)$ in-place array reversal `reverse(f.begin(), f.end())`.

3. **Affine Translation / Taylor Shift ($T_s = \begin{pmatrix} 1 & s \\ 0 & 1 \end{pmatrix}$)**:
   $$(\mathcal{M}_{T_s} F)(x) = F(x + s) = \sum_{k=0}^n f_k (x + s)^k.$$
   Expanding $(x+s)^k = \sum_{j=0}^k \binom{k}{j} s^{k-j} x^j$ and exchanging summation order gives:
   $$\begin{aligned}
   [x^j] F(x+s) &= \sum_{k=j}^n f_k \binom{k}{j} s^{k-j} \\
   &= \frac{1}{j!} \sum_{k=j}^n \bigl(k! f_k\bigr) \cdot \left(\frac{s^{k-j}}{(k-j)!}\right).
   \end{aligned}$$
   In words: each degree-$k$ term $f_k x^k$ chooses $j$ factors of $x$ and $k-j$ factors of $s$ in $\binom{k}{j}$ ways. If we define the factorial-scaled vector $A_k = k! f_k$ for $0 \le k \le n$ and the exponential weight vector $B_i = \frac{s^i}{i!}$ for $0 \le i \le n$, then the sum is a **difference-index (cross-correlation) convolution**: the indices $(k, k-j)$ have difference $k - (k-j) = j$. Reversing $A$ via $A^{\text{rev}}_u = A_{n-u} = (n-u)! f_{n-u}$ converts this into a standard sum-index polynomial multiplication:
   $$[x^j] F(x+s) = \frac{1}{j!} [u^{n-j}] \left(\sum_{u=0}^n A_{n-u} u^u\right) \left(\sum_{i=0}^n \frac{s^i}{i!} u^i\right).$$
   **Cost**: **1 multiplication** of length-$(n+1)$ polynomials, running in $O(n \log n)$ time.

---

### 3. Bruhat Decomposition of the General $GL_2(K)$ Action

Now consider an arbitrary matrix $g = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ over a field $K$. How many polynomial multiplications are needed to compute $(\mathcal{M}_g F)(x) = (cx+d)^n F\bigl(\frac{ax+b}{cx+d}\bigr)$?

- **Case 1: $c = 0$ (Affine Transformation, $d \neq 0$)**.
  Since $c = 0$, the denominator is a constant $d^n$:
  $$(cx+d)^n F\!\left(\frac{ax+b}{cx+d}\right) = d^n F\!\left(\frac{a}{d} x + \frac{b}{d}\right).$$
  First perform a Taylor shift by $s = b/d$ to obtain $F_1(y) = F(y + b/d)$ (1 convolution), then scale $[y^k] F_1(y)$ by $d^{n-k} a^k$ ($O(n)$ time).
  **Total cost**: **1 Taylor shift** ($O(n \log n)$).

- **Case 2: $c \neq 0$ (Genuine Fractional Linear / Möbius Transformation)**.
  Perform polynomial long division on the rational argument $\frac{ax+b}{cx+d}$:
  $$\frac{ax+b}{cx+d} = \frac{a}{c} + \frac{bc - ad}{c(cx+d)} = \alpha + \frac{\beta}{cx+d}, \qquad \text{where } \alpha = \frac{a}{c}, \quad \beta = \frac{bc - ad}{c} = -\frac{\det(g)}{c}.$$
  In matrix form, this is the **Bruhat decomposition** $g = T_\alpha \cdot D_{\beta, 1} \cdot J \cdot D_{c, 1} \cdot T_{d/c}$ (when $c \neq 0$), or step by step on polynomials:
  1. **Inner Taylor shift by $\alpha = a/c$**: Compute $F_1(y) = F(y + \alpha) = \sum_{k=0}^n f^{(1)}_k y^k$ using 1 Taylor shift. Now
     $$F\!\left(\alpha + \frac{\beta}{cx+d}\right) = F_1\!\left(\frac{\beta}{cx+d}\right) = \sum_{k=0}^n f^{(1)}_k \beta^k (cx+d)^{-k}.$$
  2. **Scale and Reverse**: Multiply the exterior factor $(cx+d)^n$ into the sum:
     $$(cx+d)^n F_1\!\left(\frac{\beta}{cx+d}\right) = \sum_{k=0}^n \bigl(f^{(1)}_k \beta^k\bigr) (cx+d)^{n-k} = \sum_{j=0}^n \bigl(f^{(1)}_{n-j} \beta^{n-j}\bigr) (cx+d)^j.$$
     Define $F_2(z) = \sum_{j=0}^n f^{(2)}_j z^j$ with $f^{(2)}_j = f^{(1)}_{n-j} \beta^{n-j}$ in $O(n)$ time.
  3. **Outer Substitution $z = cx + d$**: Evaluate $F_2(cx + d)$. First shift $F_3(w) = F_2(w + d)$ via a second Taylor shift (1 convolution), then scale the $k$-th coefficient by $c^k$ in $O(n)$ time.
  **Total cost**: **At most 2 Taylor shifts** (2 NTT convolutions of length $2n$).

---

### 4. The Krawtchouk / Hadamard Transform: $\sum_{k=0}^n f_k (1-x)^k (1+x)^{n-k}$

One of the most frequent bottlenecks in competitive programming combinatorics (e.g., hypercube random walks, XOR convolutions with fixed popcount, Ising/spin parity flips) is computing the polynomial
$$K_F(x) = \sum_{k=0}^n f_k (1 - x)^k (1 + x)^{n-k}.$$
If we expand $(1-x)^k (1+x)^{n-k} = \sum_{j=0}^n K_j(k; n) x^j$, the transition coefficients
$$K_j(k; n) = [x^j] (1-x)^k (1+x)^{n-k} = \sum_{r=0}^j (-1)^r \binom{k}{r} \binom{n-k}{j-r}$$
are the **Krawtchouk polynomials**, which are the eigenvalues of the Hamming association scheme (equivalently, the action of the $2^n \times 2^n$ Walsh-Hadamard transform restricted to bitstrings of Hamming weight $k$).

Rather than computing $K_j(k; n)$ term-by-term in $O(n^2)$, observe that $K_F(x)$ is the $GL_2$ Möbius transform for $g = \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix}$:
$$K_F(x) = (1+x)^n F\!\left(\frac{1-x}{1+x}\right).$$
Using $\frac{1-x}{1+x} = -1 + \frac{2}{1+x}$, we obtain an immediate **two-shift pipeline**:
1. **Step 1 (Shift by $-1$)**: Compute $G(y) = F(y - 1) = \sum_{k=0}^n g_k y^k$ via a Taylor shift of $F$ by $s = -1$.
2. **Step 2 (Scale and Reverse)**: Since $F\!\left(-1 + \frac{2}{1+x}\right) = G\!\left(\frac{2}{1+x}\right)$, multiplying by $(1+x)^n$ gives
   $$K_F(x) = (1+x)^n \sum_{k=0}^n g_k 2^k (1+x)^{-k} = \sum_{j=0}^n \bigl(g_{n-j} 2^{n-j}\bigr) (1+x)^j.$$
   Define $H(z) = \sum_{j=0}^n h_j z^j$ where $h_j = 2^{n-j} g_{n-j}$.
3. **Step 3 (Shift by $+1$)**: Finally, $K_F(x) = H(x + 1)$, which is a Taylor shift of $H(z)$ by $s = +1$.

Notice the symmetry: the involutory property $(1+x)^n K_F\bigl(\frac{1-x}{1+x}\bigr) = 2^n F(x)$ holds immediately because $\begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix}^2 = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = 2I$.

---

### 5. Hand-Checkable Trace ($n = 2$)

Let $F(x) = 1 + 2x + 3x^2$ ($f = [1, 2, 3]$, $n = 2$). We wish to compute
$$K_F(x) = 1 \cdot (1+x)^2 + 2 \cdot (1-x)(1+x) + 3 \cdot (1-x)^2.$$
- **Direct expansion (Ground Truth)**:
  - $1(1 + 2x + x^2) = 1 + 2x + x^2$
  - $2(1 - x^2) = 2 - 2x^2$
  - $3(1 - 2x + x^2) = 3 - 6x + 3x^2$
  - Sum: $K_F(x) = (1+2+3) + (2+0-6)x + (1-2+3)x^2 = 6 - 4x + 2x^2$.
- **Algorithmic Pipeline Trace**:
  1. **Shift $F$ by $s = -1$**: $G(y) = F(y-1) = 1 + 2(y-1) + 3(y-1)^2 = (1 - 2 + 3) + (2 - 6)y + 3y^2 = 2 - 4y + 3y^2$. Thus $g = [2, -4, 3]$.
  2. **Scale and Reverse**: $h_j = 2^{2-j} g_{2-j}$:
     - $h_0 = 2^2 g_2 = 4 \cdot 3 = 12$
     - $h_1 = 2^1 g_1 = 2 \cdot (-4) = -8$
     - $h_2 = 2^0 g_0 = 1 \cdot 2 = 2$
     So $H(z) = 12 - 8z + 2z^2$.
  3. **Shift $H$ by $s = +1$**: $K_F(x) = H(x+1) = 12 - 8(x+1) + 2(x+1)^2 = (12 - 8 + 2) + (-8 + 4)x + 2x^2 = 6 - 4x + 2x^2$.
  The trace matches the ground truth $6 - 4x + 2x^2$ identically.

---

### 6. Infinite-Series Euler Transform: $(1 - cx)^{-\alpha} F\!\left(\frac{ax}{1 - cx}\right) \bmod x^N$

Suppose $F(x) = \sum_{k=0}^{N-1} f_k x^k$ and we need the first $N$ coefficients of
$$E(x) = (1 - cx)^{-\alpha} F\!\left(\frac{ax}{1 - cx}\right) \bmod x^N.$$
Using rising factorials $\alpha^{\overline{m}} = \alpha(\alpha+1)\cdots(\alpha+m-1)$ (with $\alpha^{\overline{0}} = 1$), note the identity:
$$\binom{m + \alpha - 1}{m - k} = \frac{(k+\alpha)^{\overline{m-k}}}{(m-k)!} = \frac{\alpha^{\overline{m}}}{\alpha^{\overline{k}} (m-k)!},$$
provided $\alpha^{\overline{k}}$ does not vanish in $K$ for $0 \le k < N$ (for the standard Euler transform $\alpha = 1$, $\alpha^{\overline{k}} = k!$, which is always invertible when $N \le p$). Then:
$$[x^m] E(x) = c^m \alpha^{\overline{m}} \sum_{k=0}^m \left(\frac{f_k (a/c)^k}{\alpha^{\overline{k}}}\right) \cdot \left(\frac{1}{(m-k)!}\right).$$
This is a **single standard sum-index convolution** of length $N$!
- **What if $\alpha \in \{0, -1, \dots, -(N-2)\}$ so $\alpha^{\overline{k}}$ hits zero?**
  When $\alpha = -n$ for an integer $0 \le n < N$, the factor $(1-cx)^{-\alpha} = (1-cx)^n$ turns $E(x)$ back into the finite-degree $GL_2$ polynomial action $(1-cx)^n F\bigl(\frac{ax}{1-cx}\bigr)$ on degree $n$ (plus high-degree terms $k > n$ which have $(1-cx)^{-(k-n)}$ with positive denominator exponent $k-n \ge 1$). Splitting $F(x) = F_{\le n}(x) + x^{n+1} F_{>n}(x)$ avoids division by zero completely.

---

### 7. Algorithmic Contract & Failure Modes

| Operator | Formula | Preconditions in $K = \mathbb{F}_p$ | NTT Convolutions (length $2n$) |
| :--- | :--- | :--- | :--- |
| **Taylor Shift** | $F(x + s)$ | $n < p$ | $1$ |
| **General $GL_2$ Action** | $(cx+d)^n F\bigl(\frac{ax+b}{cx+d}\bigr)$ | $n < p$, $ad - bc \not\equiv 0$ | $1$ (if $c=0$) or $2$ (if $c \neq 0$) |
| **Krawtchouk Transform** | $\sum_{k=0}^n f_k (1-x)^k (1+x)^{n-k}$ | $n < p$, $2 \not\equiv 0$ | $2$ |
| **Euler Transform ($\alpha = 1$)** | $\frac{1}{1-cx} F\bigl(\frac{ax}{1-cx}\bigr) \bmod x^N$ | $N \le p$ | $1$ |

**Failure Modes**:
1. **Characteristic Overflow ($n \ge p$)**: Both Taylor shift and Euler transform divide by $k!$ for $k \le n$. If $n \ge p$, factorial division fails and one must use Lucas's theorem or $p$-adic lifting.
2. **Degenerate Determinant ($ad - bc \equiv 0 \pmod p$)**: If $ad - bc = 0$, the rational function $\frac{ax+b}{cx+d}$ is constant ($\frac{a}{c}$), so $(cx+d)^n F(a/c)$ collapses to a scalar multiple of $(cx+d)^n$. Attempting the Bruhat step $\beta = (bc-ad)/c = 0$ would zero out all $k \ge 1$ terms unless $F(a/c)$ is evaluated directly in $O(n)$ time.

---

## Iteration 64: Radical Generating Functions & Universal Euler Substitutions ($\sqrt{1-4x}$, $\sqrt{1-2x-3x^2}$, $\sqrt{1-6x+x^2}$, and Chebyshev $\sqrt{1-4x^2}$)

### 1. Concrete Lattice-Path Models & The Universal Quadratic Radical $\sqrt{1 - 2ax + bx^2}$

Why do so many 2D lattice walk, tree enumeration, and secondary structure problems collapse to a generating function containing the square root of a quadratic polynomial
$$\Delta(x) := 1 - 2ax + bx^2 \quad ?$$
Consider a directed walk in the $(t, y)$-plane starting at $(0, 0)$, where each step advances horizontal weight by $1$ or $2$ and changes height $y$ by $+1, 0,$ or $-1$:
- Allowed steps going **up** ($\Delta y = +1$) have weight generator $U(x) = x$.
- Allowed **level** steps ($\Delta y = 0$) have weight generator $L(x) = \ell_1 x + \ell_2 x^2$.
- Allowed steps going **down** ($\Delta y = -1$) have weight generator $D(x) = d_1 x + d_2 x^2$.

Let $M(x)$ be the ordinary generating function of **excursions** (walks from height $0$ to height $0$ that never dip below $y = 0$). By decomposing any non-empty excursion at its first step (either a level step followed by an excursion, or an up-step followed by an excursion on $[1, \infty)$ that hits height $0$ for the first time, followed by another excursion), we obtain the fundamental quadratic functional equation:
$$M(x) = 1 + L(x) M(x) + U(x) D(x) M(x)^2 \iff U(x) D(x) M(x)^2 - \bigl(1 - L(x)\bigr) M(x) + 1 = 0.$$
Solving this quadratic equation for the branch with $M(0) = 1$ yields
$$M(x) = \frac{1 - L(x) - \sqrt{(1 - L(x))^2 - 4 U(x) D(x)}}{2 U(x) D(x)}.$$
Simultaneously, if we consider **unconstrained bridges** (walks from $(0,0)$ to $(n,0)$ allowed to go negative), their generating function is $[y^0] \frac{1}{1 - (L(x) + U(x)y + D(x)y^{-1})}$. Extracting the residue at the pole inside the unit circle $|y| \le 1$ gives the reciprocal radical:
$$B(x) = \frac{1}{\sqrt{(1 - L(x))^2 - 4 U(x) D(x)}} = \frac{1}{\sqrt{1 - 2ax + bx^2}}.$$

Four classic families arise immediately as special cases of $\Delta(x) = 1 - 2ax + bx^2$:

| Combinatorial Family | Step Set $(\Delta t, \Delta y)$ | $a$ | $b$ | $c = \frac{a^2-b}{4}$ | Radical $\sqrt{1 - 2ax + bx^2}$ | Excursion OGF $M(x)$ | Bridge OGF $B(x)$ |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **Catalan / Dyck** | $(1,+1), (1,-1)$ (counted by semi-length) | $2$ | $0$ | $1$ | $\sqrt{1 - 4x}$ | $C(x) = \frac{1-\sqrt{1-4x}}{2x}$ | $\frac{1}{\sqrt{1-4x}} = \sum \binom{2n}{n} x^n$ |
| **Motzkin** | $(1,+1), (1,0), (1,-1)$ | $1$ | $-3$ | $1$ | $\sqrt{1 - 2x - 3x^2}$ | $M(x) = \frac{1-x-\sqrt{1-2x-3x^2}}{2x^2}$ | $\frac{1}{\sqrt{1-2x-3x^2}}$ (Central Trinomial) |
| **Schröder / Delannoy** | $(1,+1), (1,0), (1,-1)$ or $(1,0)_{\text{weight }2}$ | $3$ | $1$ | $2$ | $\sqrt{1 - 6x + x^2}$ | $S(x) = \frac{1-x-\sqrt{1-6x+x^2}}{2x}$ | $\frac{1}{\sqrt{1-6x+x^2}}$ (Central Delannoy) |
| **Chebyshev / Aerated Dyck** | $(1,+1), (1,-1)$ (counted by total length) | $0$ | $-4$ | $1$ | $\sqrt{1 - 4x^2}$ | $C(x^2) = \frac{1-\sqrt{1-4x^2}}{2x^2}$ | $\frac{1}{\sqrt{1-4x^2}}$ |

---

### 2. Reverse-Engineering the Universal Rationalizing Substitution

Suppose we face a complicated generating function $G(x) = R\!\left(x, \sqrt{1 - 2ax + bx^2}\right)$, where $R(x, w)$ is a rational function or formal power series, and we want to extract $[x^n] G(x)$ in $O(n)$ or $O(n \log n)$ time without doing costly square-root / Newton iterations. How do we find a substitution $x = \phi(u)$ that turns $\sqrt{1 - 2ax + bx^2}$ into a rational function of $u$ while keeping $x(u) = u + O(u^2)$ convenient for Lagrange inversion?

Let us set
$$x(u) = \frac{u}{D(u)}, \qquad \text{where } D(u) = 1 + au + cu^2,$$
and determine the constant $c$ so that $\Delta(x(u)) = 1 - 2a x(u) + b x(u)^2$ becomes a perfect square! Compute the numerator of $\Delta(x(u))$ over the common denominator $D(u)^2$:
$$\begin{aligned}
D(u)^2 \Delta(x(u)) &= (1 + au + cu^2)^2 - 2au(1 + au + cu^2) + bu^2 \\
&= \bigl(1 + 2au + (a^2 + 2c)u^2 + 2acu^3 + c^2 u^4\bigr) - \bigl(2au + 2a^2 u^2 + 2acu^3\bigr) + bu^2 \\
&= 1 + \bigl(2c - a^2 + b\bigr) u^2 + c^2 u^4.
\end{aligned}$$
Notice how the $u^1$ and $u^3$ terms cancel automatically! To make $1 + (2c - a^2 + b)u^2 + c^2 u^4$ equal to the perfect square $(1 - cu^2)^2 = 1 - 2cu^2 + c^2 u^4$, we simply equate the $u^2$ coefficients:
$$2c - a^2 + b = -2c \iff 4c = a^2 - b \iff c = \frac{a^2 - b}{4}.$$

This single equation yields the **Universal Quadratic Radical Substitution**:
$$\boxed{
x(u) = \frac{u}{1 + au + cu^2}, \qquad c = \frac{a^2 - b}{4} \quad \Longrightarrow \quad \sqrt{1 - 2ax + bx^2} = \frac{1 - cu^2}{1 + au + cu^2}.
}$$

Let us also compute the differential $\frac{dx}{du}$ using the quotient rule:
$$\frac{dx}{du} = \frac{(1 + au + cu^2) - u(a + 2cu)}{(1 + au + cu^2)^2} = \frac{1 - cu^2}{(1 + au + cu^2)^2} = \frac{\sqrt{1 - 2ax + bx^2}}{1 + au + cu^2}.$$
Look at the miraculous cancellation when we divide $\frac{dx}{x}$ by $\frac{du}{u}$:
$$\frac{dx}{x(u)} = \frac{1 - cu^2}{u(1 + au + cu^2)} du \implies \frac{1}{\sqrt{1 - 2ax + bx^2}} \frac{dx}{x} = \frac{1 + au + cu^2}{1 - cu^2} \cdot \frac{1 - cu^2}{u(1 + au + cu^2)} du = \frac{du}{u}.$$
Rewriting this identity in derivative form explains **why differentiating radical generating functions always eliminates the numerator**:
$$\boxed{
\frac{1}{\sqrt{1 - 2ax + bx^2}} = \frac{x}{u} \frac{du}{dx} = x \frac{d}{dx} \ln u(x).
}$$
Moreover, solving $c u^2 + (a - 1/x)u + 1 = 0$ for the formal power series branch $u(x) = x + O(x^2)$ gives the explicit inverse:
$$u(x) = \frac{1 - ax - \sqrt{1 - 2ax + bx^2}}{2cx} = \frac{2x}{1 - ax + \sqrt{1 - 2ax + bx^2}}.$$

---

### 3. The Two Master Coefficient Extraction Formulas (Formal Residue Change of Variables)

Using the formal residue theorem $[x^n] F(x) = \operatorname{Res}_{x=0} \frac{F(x)}{x^{n+1}} dx = \operatorname{Res}_{u=0} \frac{F(x(u))}{x(u)^{n+1}} \frac{dx}{du} du$, we obtain two universal coefficient extraction formulas for any power series $H(x)$:

1. **Formula A (With $\frac{1}{\sqrt{1-2ax+bx^2}}$ present — No $(1-cu^2)$ factor!)**:
   Because $\frac{1}{\sqrt{1-2ax+bx^2}} \frac{dx}{x} = \frac{du}{u}$ and $x(u)^{-n} = u^{-n}(1 + au + cu^2)^n$:
   $$\boxed{
   [x^n] \frac{H(x)}{\sqrt{1 - 2ax + bx^2}} = [u^n] H\!\left(\frac{u}{1 + au + cu^2}\right) (1 + au + cu^2)^n.
   }$$
   In particular, when $H(x) = u(x)^k$ (representing $k$ independent excursion components convoluted with a bridge), $H(x(u)) = u^k$, so:
   $$[x^n] \frac{u(x)^k}{\sqrt{1 - 2ax + bx^2}} = [u^{n-k}] (1 + au + cu^2)^n.$$

2. **Formula B (Without $\frac{1}{\sqrt{1-2ax+bx^2}}$ — Includes the factor $(1 - cu^2)$)**:
   Since $F(x) = F(x) \sqrt{\Delta(x)} \cdot \frac{1}{\sqrt{\Delta(x)}}$ and $\sqrt{\Delta(x(u))} = \frac{1-cu^2}{1+au+cu^2}$:
   $$\boxed{
   [x^n] F(x) = [u^n] F\!\left(\frac{u}{1 + au + cu^2}\right) (1 - cu^2) (1 + au + cu^2)^{n-1}.
   }$$
   In particular, for $F(x) = u(x)^k$ (the $k$-th power of the excursion generating function):
   $$[x^n] u(x)^k = [u^{n-k}] (1 - cu^2)(1 + au + cu^2)^{n-1} = \frac{k}{n} [u^{n-k}] (1 + au + cu^2)^n.$$

Let us check how the four classic families specialize under Formula A and Formula B:
- **Catalan ($a=2, b=0 \implies c=1$)**:
  $1 + au + cu^2 = 1 + 2u + u^2 = (1+u)^2$ and $u(x) = \frac{1-\sqrt{1-4x}}{2} = x C(x)$.
  By Formula A, $[x^n] \frac{C(x)^k}{\sqrt{1-4x}} = [x^{n+k}] \frac{u(x)^k}{\sqrt{1-4x}} = [u^n] (1+u)^{2(n+k)} = \binom{2n+2k}{n}$.
  By Formula B, $[x^n] C(x)^k = [x^{n+k}] u(x)^k = [u^n] (1-u^2)(1+u)^{2n+2k-2} = \frac{k}{n+k}\binom{2n+2k}{n}$.
- **Motzkin ($a=1, b=-3 \implies c=1$)**:
  $1 + au + cu^2 = 1 + u + u^2$, $x(u) = \frac{u}{1+u+u^2}$, and $u(x) = \frac{1-x-\sqrt{1-2x-3x^2}}{2x} = x M(x)$.
  By Formula B, $[x^n] M(x)^k = \frac{k}{n+k} [u^n] (1 + u + u^2)^{n+k}$ (a single trinomial coefficient!).
- **Central Delannoy & Large Schröder ($a=3, b=1 \implies c=2$)**:
  $1 + au + cu^2 = 1 + 3u + 2u^2 = (1+u)(1+2u)$ — **it factors into linear terms!**
  Therefore, by Formula A with $H(x) = 1$, the Central Delannoy number is:
  $$D_n = [x^n] \frac{1}{\sqrt{1 - 6x + x^2}} = [u^n] (1+u)^n (1+2u)^n = \sum_{j=0}^n \binom{n}{j}^2 2^j.$$
  And the Large Schröder number $S_n = [x^n] \frac{1-x-\sqrt{1-6x+x^2}}{2x}$ satisfies $u(x) = \frac{1-3x-\sqrt{1-6x+x^2}}{4x} = \frac{S(x)-1}{2}$ (which already has $x$ divided out: $u(x) = x + 3x^2 + 11x^3 + 45x^4 + \dots$). Therefore $[x^n] u(x) = \frac{1}{2} S_n$ for all $n \ge 1$, giving:
  $$S_n = 2 [x^n] u(x) = \frac{2}{n} [u^{n-1}] (1+u)^n (1+2u)^n = 2 [u^{n-1}] (1 - 2u^2)(1+u)^{n-2}(1+2u)^{n-2},$$
  or equivalently, using $v(x) = x S(x) = \frac{u}{1+u}$, $S_n = [x^{n+1}] v(x) = [u^n](1-2u^2)(1+u)^{n-1}(1+2u)^{n-1}$.

---

### 4. Hand-Checkable Trace: Central Delannoy $D_2$, Large Schröder $S_2$, and Motzkin $M_3$

1. **Central Delannoy $D_2 = [x^2] (1 - 6x + x^2)^{-1/2}$**:
   - **Direct Taylor expansion**: $(1 - (6x - x^2))^{-1/2} = 1 + \frac{1}{2}(6x - x^2) + \frac{3}{8}(6x - x^2)^2 + O(x^3) = 1 + 3x + \left(-\frac{1}{2} + \frac{3}{8}\cdot 36\right)x^2 = 1 + 3x + 13x^2$. So $D_2 = 13$.
   - **Formula A Trace ($a=3, b=1, c=2, n=2$)**:
     $$D_2 = [u^2] (1+u)^2 (1+2u)^2 = [u^2] (1 + 2u + u^2)(1 + 4u + 4u^2) = 1\cdot 4 + 2\cdot 4 + 1\cdot 1 = 13.$$
2. **Large Schröder $S_2 = 6$ and $S_3 = 22$**:
   - **Corrected Formula Trace**: For $n=2$, $S_2 = \frac{2}{2}[u^1](1+u)^2(1+2u)^2 = [u^1](1+6u+\dots) = 6$. For $n=3$, $S_3 = \frac{2}{3}[u^2](1+3u+2u^2)^3 = \frac{2}{3}(3 + 27 + 3) = 22$.
3. **Motzkin $M_3 = [x^3] \frac{1-x-\sqrt{1-2x-3x^2}}{2x^2} = [x^4] u(x)$**:
   - **Direct combinatorics**: For $n=3$, the 4 Motzkin paths of length $3$ are $LLL, LUD, ULD, UDL$. So $M_3 = 4$.
   - **Formula B Trace ($a=1, b=-3, c=1, n=4, k=1$)**:
     $$M_3 = [u^3] (1 - u^2)(1 + u + u^2)^3.$$
     Since $(1+u+u^2)^3 = 1 + 3u + 6u^2 + 7u^3 + 6u^4 + 3u^5 + u^6$, we get $[u^3](1-u^2)(1+u+u^2)^3 = 7 - 3 = 4$.

---

### 5. Chebyshev Polynomials & Bounded-Height Lattice Walks on $[0, H]$ (Two Models)

When a Dyck or Motzkin walk is restricted to stay inside a **bounded horizontal strip** $0 \le y \le H$, its transfer matrix is an $(H+1) \times (H+1)$ tridiagonal Toeplitz matrix. Equivalently, let $F_h(x) = \frac{P_h(x)}{P_{h+1}(x)}$ be the generating function of walks from height $0$ to height $0$ inside $[0, h]$, where the denominator polynomials satisfy the three-term Chebyshev recurrence:
$$P_{h+1}(x) = (1 - L(x)) P_h(x) - U(x) D(x) P_{h-1}(x), \qquad P_0(x) = 1, \quad P_1(x) = 1 - L(x).$$
Crucially, **two distinct parameterizations** arise in competitive programming depending on whether $x$ indexes matched Up-Down pairs (semi-length) or individual steps:

1. **Model I: Semi-Length / Up-Down Pair Weight $x$ (Dyck Paths of Length $2n$ Indexed by $n$ Pairs)**:
   Here horizontal steps do not exist ($L(x) = 0$) and each matched Up-Down pair carries weight $U(x)D(x) = x$, so $P_{h+1}(x) = P_h(x) - x P_{h-1}(x)$. Under the Catalan substitution $x = \frac{u}{(1+u)^2}$, the characteristic roots of $\lambda^2 - \lambda + \frac{u}{(1+u)^2} = 0$ are $\lambda_1 = \frac{1}{1+u}$ and $\lambda_2 = \frac{u}{1+u}$ (first-power $u$, **not** $u^2$):
   $$P_h(x(u)) = \frac{1 - u^{h+1}}{(1 - u)(1 + u)^h}, \qquad F_h(x(u)) = \frac{P_h(x(u))}{P_{h+1}(x(u))} = (1 + u)\frac{1 - u^{h+1}}{1 - u^{h+2}}.$$

2. **Model II: Step-Length Tridiagonal Walk ($L(x) = ax, U(x)D(x) = cx^2$, e.g. Motzkin Paths of Length $n$)**:
   Here each step carries weight $x$, so $1 - L(x) = \frac{1+cu^2}{1+au+cu^2}$ and $U(x)D(x) = \frac{cu^2}{(1+au+cu^2)^2}$ under $x = \frac{u}{1+au+cu^2}$. The characteristic roots are $\lambda_1 = \frac{1}{1+au+cu^2}$ and $\lambda_2 = \frac{cu^2}{1+au+cu^2}$, giving even powers $(cu^2)$:
   $$P_{h+1}(x(u)) = \frac{1}{(1 + au + cu^2)^{h+1}} \cdot \frac{1 - (cu^2)^{h+2}}{1 - cu^2}, \qquad F_h(x(u)) = (1 + au + cu^2) \frac{1 - (cu^2)^{h+1}}{1 - (cu^2)^{h+2}}.$$

- **Combinatorial Meaning (Reflection Principle)**: Expanding $\frac{1 - u^{h+1}}{1 - u^{h+2}}$ (in Model I) or $\frac{1 - (cu^2)^{h+1}}{1 - (cu^2)^{h+2}}$ (in Model II) as a geometric series via Formula A/B immediately reproduces the **André reflection principle** in the $u$-domain, extracting the exact $n$-th coefficient of a bounded-strip walk in $O\!\left(\frac{n}{H}\right)$ terms!

---

## Iteration 65: Falling-Factorial Polynomials (`下降幂多项式`), Point-Value EGFs, and Stirling Basis Conversions

### 1. Concrete Algebraic Model: Why Falling Factorials Diagonalize Evaluation at $0, 1, 2, \dots$

For any integer $k \ge 0$, the **falling factorial** (`下降幂`) and **rising factorial** (`上升幂`) are defined by
$$x^{\underline{k}} := x(x-1)\cdots(x-k+1) = \prod_{j=0}^{k-1} (x - j), \qquad x^{\overline{k}} := x(x+1)\cdots(x+k-1) = \prod_{j=0}^{k-1} (x + j),$$
with $x^{\underline{0}} = x^{\overline{0}} = 1$. Since $\deg(x^{\underline{k}}) = k$, the set $\{x^{\underline{0}}, x^{\underline{1}}, \dots, x^{\underline{n}}\}$ is a basis of $K[x]_{\le n}$. Any polynomial $F(x)$ of degree at most $n$ has a unique representation as a **falling-factorial polynomial**:
$$F(x) = \sum_{k=0}^n a_k x^{\underline{k}}.$$

Why is this basis so much better behaved than the monomial basis $\sum_{k=0}^n c_k x^k$ when evaluating $F(m)$ at non-negative integers $m = 0, 1, 2, \dots$?
Look at what happens when we divide $m^{\underline{k}}$ by $m!$:
$$\frac{m^{\underline{k}}}{m!} = \begin{cases} \dfrac{m(m-1)\cdots(m-k+1)}{m!} = \dfrac{1}{(m-k)!} & \text{if } m \ge k, \\[8pt] 0 & \text{if } 0 \le m < k. \end{cases}$$
The dependence on $m$ and $k$ splits into a pure difference index $m - k$! Let us form the **Point-Value Exponential Generating Function (Point-Value EGF)** of the sequence $(F(0), F(1), F(2), \dots)$:
$$\widehat{F}(t) := \sum_{m=0}^\infty F(m) \frac{t^m}{m!}.$$
Substitute $F(m) = \sum_{k=0}^n a_k m^{\underline{k}}$ and exchange the sums:
$$\begin{aligned}
\widehat{F}(t) &= \sum_{m=0}^\infty \left(\sum_{k=0}^n a_k m^{\underline{k}}\right) \frac{t^m}{m!} \\
&= \sum_{k=0}^n a_k t^k \sum_{m=k}^\infty \frac{t^{m-k}}{(m-k)!} \\
&= \left(\sum_{k=0}^n a_k t^k\right) e^t.
\end{aligned}$$

This proves the **Fundamental Theorem of Falling-Factorial Polynomials**:
$$\boxed{
F(x) = \sum_{k=0}^n a_k x^{\underline{k}} \quad \Longleftrightarrow \quad \widehat{F}(t) = \sum_{m=0}^\infty F(m) \frac{t^m}{m!} = A(t) e^t, \qquad \text{where } A(t) = \sum_{k=0}^n a_k t^k.
}$$
And by multiplying both sides by $e^{-t} = \sum_{j \ge 0} \frac{(-1)^j}{j!} t^j$, we recover the falling-factorial coefficient generating function $A(t)$ directly from the point values:
$$\boxed{
A(t) = \widehat{F}(t) e^{-t} \quad \Longleftrightarrow \quad a_k = \sum_{m=0}^k \frac{(-1)^{k-m}}{(k-m)!} \frac{F(m)}{m!}.
}$$

---

### 2. $O(n \log n)$ Operations in the Falling-Factorial Basis

Because pointwise multiplication of values $H(m) = F(m) G(m)$ corresponds to the **Hadamard (coefficient-wise) product** of their Point-Value EGFs $\widehat{H}(t) = \widehat{F}(t) \odot \widehat{G}(t)$:
$$\left[t^m\right] \widehat{H}(t) = \frac{F(m)G(m)}{m!} = m! \cdot \left(\frac{F(m)}{m!}\right) \left(\frac{G(m)}{m!}\right),$$
we obtain a fast transform between falling-factorial coefficients and integer point values that plays the exact same role as the FFT between ordinary coefficients and roots of unity!

#### Operation 1: Falling-Factorial Polynomial Multiplication (`P5393`) in $O(n \log n)$
Given $F(x) = \sum_{k=0}^n a_k x^{\underline{k}}$ and $G(x) = \sum_{k=0}^m b_k x^{\underline{k}}$, their product $H(x) = F(x)G(x) = \sum_{k=0}^{n+m} c_k x^{\underline{k}}$ has degree $N = n + m$. To find $c_0, \dots, c_N$:
1. **FWT / Evaluation via $e^t$ (2 convolutions of length $N+1$)**:
   Compute $\widehat{F}(t) = A(t) e^t \bmod t^{N+1}$ and $\widehat{G}(t) = B(t) e^t \bmod t^{N+1}$. Now $[t^i]\widehat{F}(t) = \frac{F(i)}{i!}$ and $[t^i]\widehat{G}(t) = \frac{G(i)}{i!}$ for $0 \le i \le N$.
2. **Pointwise Multiplication ($O(N)$ time)**:
   For $0 \le i \le N$, set $\widehat{H}_i = i! \cdot \widehat{F}_i \cdot \widehat{G}_i = \frac{F(i)G(i)}{i!}$.
3. **IFWT / Interpolation via $e^{-t}$ (1 convolution of length $N+1$)**:
   Compute $C(t) = \widehat{H}(t) e^{-t} \bmod t^{N+1}$. The coefficients of $C(t)$ are $c_0, \dots, c_N$.
- **Total cost**: **3 NTT convolutions** of length $n+m+1$, running in $O((n+m)\log(n+m))$ time.

#### Operation 2: Binomial Moment Sums $\sum_{i=0}^M \binom{M}{i} p^i q^{M-i} F(i)$ in $O(n)$ (Once $a_k$ Are Known)
Suppose $M$ can be huge ($M \le 10^9$), while $\deg(F) = n \le 2 \cdot 10^5$, and we want to evaluate the binomial expectation sum
$$S = \sum_{i=0}^M \binom{M}{i} p^i q^{M-i} F(i).$$
Notice the identity $\binom{M}{i} i^{\underline{k}} = \frac{M!}{i!(M-i)!} \frac{i!}{(i-k)!} = \frac{M^{\underline{k}} (M-k)!}{(i-k)!(M-i)!} = M^{\underline{k}} \binom{M-k}{i-k}$ for $i \ge k$. Substituting $F(i) = \sum_{k=0}^n a_k i^{\underline{k}}$ and swapping sums:
$$\begin{aligned}
\sum_{i=0}^M \binom{M}{i} p^i q^{M-i} F(i) &= \sum_{k=0}^n a_k \sum_{i=k}^M \binom{M}{i} i^{\underline{k}} p^i q^{M-i} \\
&= \sum_{k=0}^n a_k M^{\underline{k}} p^k \sum_{i=k}^M \binom{M-k}{i-k} p^{i-k} q^{M-i} \\
&= \sum_{k=0}^n a_k M^{\underline{k}} p^k (p + q)^{M-k}.
\end{aligned}$$
The upper limit $M \le 10^9$ drops to $\min(n, M) \le 2 \cdot 10^5$! Once $F(x)$ is converted into the falling-factorial basis $a_0, \dots, a_n$, the entire sum evaluates in **$O(n)$ time**.

---

### 3. Basis Conversion Triangle: Ordinary Powers $x^k$, Falling Factorials $x^{\underline{k}}$, and Rising Factorials $x^{\overline{k}}$

The transition matrices between the three canonical polynomial bases — monomials $\{x^k\}$, falling factorials $\{x^{\underline{k}}\}$, and rising factorials $\{x^{\overline{k}}\}$ — are governed by the **Stirling numbers of the first kind** $\left[\begin{matrix} n \\ k \end{matrix}\right]$, **Stirling numbers of the second kind** $\left\{\begin{matrix} n \\ k \end{matrix}\right\}$, and **Lah numbers** $L(n, k) = \binom{n-1}{k-1}\frac{n!}{k!}$:

$$\begin{aligned}
x^n &= \sum_{k=0}^n \left\{\begin{matrix} n \\ k \end{matrix}\right\} x^{\underline{k}} = \sum_{k=0}^n (-1)^{n-k} \left\{\begin{matrix} n \\ k \end{matrix}\right\} x^{\overline{k}}, \\
x^{\underline{n}} &= \sum_{k=0}^n (-1)^{n-k} \left[\begin{matrix} n \\ k \end{matrix}\right] x^k, \qquad x^{\overline{n}} = \sum_{k=0}^n \left[\begin{matrix} n \\ k \end{matrix}\right] x^k, \\
x^{\overline{n}} &= \sum_{k=0}^n L(n, k) x^{\underline{k}}, \qquad x^{\underline{n}} = \sum_{k=0}^n (-1)^{n-k} L(n, k) x^{\overline{k}}.
\end{aligned}$$

Let us carefully distinguish the algorithmic complexity of converting **a single row ($x^n$)** versus **an arbitrary polynomial ($\sum_{j=0}^n c_j x^j$)**:

| Conversion Task | Algebraic Reduction | Time Complexity | Why? |
| :--- | :--- | :--- | :--- |
| **1. Single Monomial $x^n \to \sum_{k=0}^n \left\{\begin{matrix} n \\ k \end{matrix}\right\} x^{\underline{k}}$** | $A(t) = \widehat{F}(t) e^{-t}$ with $F(m) = m^n$ | **$O(n \log n)$** | Since $F(m) = m^n$ is completely multiplicative, $0^n, 1^n, \dots, n^n$ are computed in $O(n)$ time via a linear prime sieve, followed by 1 convolution with $e^{-t}$. |
| **2. Single Falling Factorial $x^{\underline{n}} \to \sum_{k=0}^n (-1)^{n-k}\left[\begin{matrix} n \\ k \end{matrix}\right] x^k$** | Doubling: $x^{\underline{2m}} = x^{\underline{m}} (x-m)^{\underline{m}}$ | **$O(n \log n)$** | Given $P_m(x) = x^{\underline{m}}$, compute $P_m(x-m)$ by 1 Taylor shift and multiply $P_m(x) P_m(x-m)$ ($T(n) = T(n/2) + O(n \log n) = O(n \log n)$). |
| **3. Arbitrary Polynomial $\sum_{j=0}^n c_j x^j \to \sum_{k=0}^n a_k x^{\underline{k}}$ (`P5394`)** | Evaluate $F(0), \dots, F(n)$ or D&C on $x^{\underline{m}}$ | **$O(n \log^2 n)$** | Unlike $m^n$, an arbitrary $F(x)$ is not multiplicative! Either use Multipoint Evaluation on $0, 1, \dots, n$ ($O(n \log^2 n)$) + $e^{-t}$ convolution, or D&C polynomial division by $x^{\underline{m}}$. |
| **4. Arbitrary Falling Factorial $\sum_{k=0}^n a_k x^{\underline{k}} \to \sum_{j=0}^n c_j x^j$** | D&C tree on $x(x-1)\cdots(x-k+1)$ or Interpolation | **$O(n \log^2 n)$** | Build the subproduct tree over $\{x - i\}_{i=0}^{n-1}$ and accumulate bottom-up: $F_{L,R}(x) = F_{L,M}(x) + (x-L)\cdots(x-M) F_{M+1,R}(x)$ in $O(n \log^2 n)$. |
| **5. Arbitrary Falling $\leftrightarrow$ Rising ($\sum a_k x^{\underline{k}} \leftrightarrow \sum b_k x^{\overline{k}}$)** | Lah transform: $b_k = \frac{1}{k!} \sum_{j=k}^n (j! a_j) \binom{j-1}{k-1}$ or $F(-x)$ | **$O(n \log n)$** | Notice $(-x)^{\underline{k}} = (-1)^k x^{\overline{k}}$! Or use the difference-index convolution of $j! a_j$ with $\binom{j-1}{k-1}$ in **1 NTT convolution** ($O(n \log n)$)! |

Notice **Row 5**: Even though converting between ordinary powers $x^k$ and falling/rising factorials for a general polynomial takes $O(n \log^2 n)$, converting **directly between falling factorials and rising factorials** takes only **$O(n \log n)$** (1 convolution) via the Lah transform or via the identity $F(-x) = \sum_{k=0}^n (-1)^k a_k x^{\overline{k}}$ (which evaluates $F(-m)$ via $A(t)e^{-t}$)!

---

### 4. Hand-Checkable Trace ($n = 3$)

Convert $F(x) = x^3$ into the falling-factorial basis $F(x) = \sum_{k=0}^3 a_k x^{\underline{k}}$:
1. **Point values of $F(x) = x^3$ at $m = 0, 1, 2, 3$**:
   $F(0) = 0, F(1) = 1, F(2) = 8, F(3) = 27$.
   Point-Value EGF: $\widehat{F}(t) = 0 + 1 \cdot t + \frac{8}{2!} t^2 + \frac{27}{3!} t^3 + \dots = t + 4t^2 + \frac{9}{2}t^3 + O(t^4)$.
2. **Convolve with $e^{-t} = 1 - t + \frac{1}{2}t^2 - \frac{1}{6}t^3 + O(t^4)$**:
   $$\begin{aligned}
   A(t) = \widehat{F}(t) e^{-t} &= \left(t + 4t^2 + \frac{9}{2}t^3\right)\left(1 - t + \frac{1}{2}t^2 - \frac{1}{6}t^3\right) \bmod t^4 \\
   &= t + (4 - 1)t^2 + \left(\frac{9}{2} - 4 + \frac{1}{2}\right)t^3 \\
   &= t + 3t^2 + t^3.
   \end{aligned}$$
   Thus $a_0 = 0, a_1 = 1, a_2 = 3, a_3 = 1$, matching $\left\{\begin{matrix} 3 \\ 0 \end{matrix}\right\}=0, \left\{\begin{matrix} 3 \\ 1 \end{matrix}\right\}=1, \left\{\begin{matrix} 3 \\ 2 \end{matrix}\right\}=3, \left\{\begin{matrix} 3 \\ 3 \end{matrix}\right\}=1$:
   $$x^3 = 1 \cdot x + 3 \cdot x(x-1) + 1 \cdot x(x-1)(x-2).$$

---

## Iteration 66: Power-Sum / Subset-Product Logarithmic Derivatives & Newton's Identities (`ln / exp Trick`)

### 1. The Two Regimes of Product Generating Functions

Whenever a problem asks us to multiply together $m$ factors — such as subset sums $\prod_{i=1}^m (1 + x^{w_i})$, unbounded knapsack $\prod_{i=1}^m (1 - x^{w_i})^{-1}$, or elementary symmetric polynomials $\prod_{i=1}^m (1 + a_i x)$ — multiplying the factors one by one takes $O(m n)$. Taking the formal logarithm $\ln P(x)$ turns the product into a sum, and differentiating via the **logarithmic derivative** $\frac{P'(x)}{P(x)} = \frac{d}{dx} \ln P(x)$ removes even the harmonic denominators $\frac{1}{k}$.

However, there are **two distinct regimes** depending on where the variable $x$ sits inside each factor, and confusing them leads to wrong time complexities:

| Feature | **Regime A: Exponent-Weighted (Euler / Knapsack Products)** | **Regime B: Scalar-Weighted (Power Sums & Newton's Identities)** |
| :--- | :--- | :--- |
| **Canonical Product $P(x)$** | $\displaystyle \prod_{k=1}^{N} (1 - x^k)^{-c_k}$ or $\displaystyle \prod_{k=1}^{N} (1 + x^k)^{c_k}$ | $\displaystyle \prod_{i=1}^{m} (1 - a_i x)^{-c_i}$ or $\displaystyle \prod_{i=1}^{m} (1 + a_i x)^{c_i}$ |
| **What varies per item?** | The **degree / exponent** $w_i \in \{1, \dots, N\}$ of $x^{w_i}$ | The **scalar coefficient** $a_i \in K$ of $a_i x$ |
| **Log-Derivative $x \frac{P'(x)}{P(x)}$** | $\displaystyle \sum_{n=1}^{N} x^n \sum_{k \mid n} k c_k$ (Divisor sum!) | $\displaystyle \sum_{k=1}^{N} x^k \left(\sum_{i=1}^m c_i a_i^k\right) = \sum_{k=1}^{N} p_k x^k$ (Power sums!) |
| **How is $\ln P(x)$ built?** | **Harmonic Sieve** (`for k=1..N: for j=1..N/k`) | **Subproduct Tree** $Q(x) = \prod_{i=1}^m (1 - a_i x)$ + FPS $\ln / \text{inv}$ |
| **Time Complexity** | **$O(N \log N)$** | **$O(m \log^2 m + N \log N)$** |
| **Representative Problem** | Luogu P4389 (`付公主的背包`) | Luogu P4705 (`玩游戏`) |

---

### 2. Regime A: Exponent-Weighted Euler Products via the Harmonic Sieve

Suppose we have $m$ items with integer weights $w_1, \dots, w_m \in \{1, \dots, N\}$. Step 1 is **frequency compression**: group identical weights by counting $c_k = \#\{i : w_i = k\}$ for each $1 \le k \le N$.
Now consider the unbounded knapsack generating function (or 0/1 subset-sum generating function):
$$P_{\text{unb}}(x) = \prod_{k=1}^N (1 - x^k)^{-c_k} \bmod x^{N+1}, \qquad P_{0/1}(x) = \prod_{k=1}^N (1 + x^k)^{c_k} \bmod x^{N+1}.$$
Using the formal logarithm series $-\ln(1 - z) = \sum_{j=1}^\infty \frac{z^j}{j}$ and $\ln(1 + z) = \sum_{j=1}^\infty \frac{(-1)^{j-1} z^j}{j}$:
$$\begin{aligned}
\ln P_{\text{unb}}(x) &= \sum_{k=1}^N c_k \sum_{j=1}^{\lfloor N/k \rfloor} \frac{x^{jk}}{j} \bmod x^{N+1}, \\
\ln P_{0/1}(x) &= \sum_{k=1}^N c_k \sum_{j=1}^{\lfloor N/k \rfloor} \frac{(-1)^{j-1}}{j} x^{jk} \bmod x^{N+1}.
\end{aligned}$$
Why is the double loop over $(k, j)$ with $jk \le N$ so fast? Because for each $k \in \{1, \dots, N\}$, the inner loop runs $\lfloor N/k \rfloor$ times, so the total number of operations to build the array $L(x) = \ln P(x) \bmod x^{N+1}$ is the harmonic series
$$\sum_{k=1}^N \left\lfloor \frac{N}{k} \right\rfloor = N H_N = O(N \log N).$$
Once $L(x) \bmod x^{N+1}$ is accumulated in $O(N \log N)$ additions, a **single call to FPS $\exp(L(x)) \bmod x^{N+1}$** recovers $P(x) \bmod x^{N+1}$ in $O(N \log N)$ time!

---

### 3. Regime B: Scalar Power Sums $p_k = \sum_{i=1}^m a_i^k$ and Newton's Identities

Now suppose we are given $m$ arbitrary field elements $a_1, a_2, \dots, a_m \in \mathbb{F}_p$ ($m \le 10^5$), and we need the **power sums**
$$p_k := \sum_{i=1}^m a_i^k \qquad \text{for all } 0 \le k \le N.$$
Naively computing $p_k$ for each $k$ takes $O(m N)$ time. Instead, form the generating function of the sequence $(p_0, p_1, p_2, \dots)$:
$$\begin{aligned}
P(x) := \sum_{k=0}^\infty p_k x^k &= \sum_{k=0}^\infty \left(\sum_{i=1}^m a_i^k\right) x^k \\
&= \sum_{i=1}^m \sum_{k=0}^\infty (a_i x)^k \\
&= \sum_{i=1}^m \frac{1}{1 - a_i x}.
\end{aligned}$$
Now compare each summand $\frac{1}{1 - a_i x}$ with the logarithmic derivative of $1 - a_i x$:
$$\frac{d}{dx} \ln(1 - a_i x) = \frac{-a_i}{1 - a_i x} \implies 1 - x \frac{d}{dx} \ln(1 - a_i x) = 1 + \frac{a_i x}{1 - a_i x} = \frac{1}{1 - a_i x}.$$
Summing over $i = 1, \dots, m$ and defining the master polynomial $Q(x) := \prod_{i=1}^m (1 - a_i x)$ gives the **Power-Sum Logarithmic Derivative Identity**:
$$\boxed{
P(x) = \sum_{k=0}^\infty p_k x^k = \sum_{i=1}^m \frac{1}{1 - a_i x} = m - x \frac{Q'(x)}{Q(x)} = m - x \frac{d}{dx} \ln Q(x), \qquad \text{where } Q(x) = \prod_{i=1}^m (1 - a_i x).
}$$

More generally, if each element $a_i$ carries an arbitrary multiplicity or weight $c_i \in K$, so $p_k = \sum_{i=1}^m c_i a_i^k$, then
$$\sum_{k=0}^\infty p_k x^k = \sum_{i=1}^m \frac{c_i}{1 - a_i x} = \frac{N(x)}{Q(x)},$$
which is computed in $O(m \log^2 m)$ time by divide-and-conquer fraction addition $\frac{N_L}{Q_L} + \frac{N_R}{Q_R} = \frac{N_L Q_R + N_R Q_L}{Q_L Q_R}$ on the subproduct tree, followed by **1 FPS inversion** $N(x) Q(x)^{-1} \bmod x^{N+1}$ in $O(N \log N)$ time!

#### Bidirectional Equivalence with Elementary ($e_k$) and Complete Homogeneous ($h_k$) Symmetric Polynomials
Notice what $Q(x)$ and $Q(x)^{-1}$ represent in symmetric function theory:
- **Elementary Symmetric Polynomials $e_k = \sum_{1 \le i_1 < \dots < i_k \le m} a_{i_1}\cdots a_{i_k}$**:
  $$E(x) := \sum_{k=0}^m e_k x^k = \prod_{i=1}^m (1 + a_i x) = Q(-x).$$
- **Complete Homogeneous Symmetric Polynomials $h_k = \sum_{1 \le i_1 \le \dots \le i_k \le m} a_{i_1}\cdots a_{i_k}$**:
  $$H(x) := \sum_{k=0}^\infty h_k x^k = \prod_{i=1}^m \frac{1}{1 - a_i x} = \frac{1}{Q(x)} = \frac{1}{E(-x)}.$$
- **Newton's Identities as an $\exp / \ln$ Bridge**:
  Since $\ln H(x) = -\ln Q(x) = \sum_{k=1}^\infty \frac{p_k}{k} x^k$ and $\ln E(x) = \ln Q(-x) = \sum_{k=1}^\infty (-1)^{k-1} \frac{p_k}{k} x^k$:
  $$\boxed{
  H(x) = \exp\!\left(\sum_{k=1}^\infty \frac{p_k}{k} x^k\right), \qquad E(x) = \exp\!\left(\sum_{k=1}^\infty (-1)^{k-1} \frac{p_k}{k} x^k\right).
  }$$
  Differentiating $\ln E(x)$ gives $E'(x) = E(x) \sum_{k \ge 1} (-1)^{k-1} p_k x^{k-1}$, which upon extracting $[x^{k-1}]$ is the classic **Newton-Girard recurrence** $k e_k = \sum_{j=1}^k (-1)^{j-1} e_{k-j} p_j$. In FPS algorithms, we never run the $O(N^2)$ recurrence: we convert between $\{p_k\}_{k=1}^N$, $\{e_k\}_{k=1}^N$, and $\{h_k\}_{k=1}^N$ in **$O(N \log N)$ time** using $\ln$, $\exp$, and polynomial inversion!

---

### 4. Application: Moments of Pairwise Sums $\sum_{i=1}^n \sum_{j=1}^m (a_i + b_j)^k$ (Luogu P4705 `玩游戏`)

Suppose we are given two arrays $a_1, \dots, a_n$ and $b_1, \dots, b_m$, and for every $t = 1, 2, \dots, K$ we must compute the expected $t$-th power of a random sum:
$$S_t = \frac{1}{nm} \sum_{i=1}^n \sum_{j=1}^m (a_i + b_j)^t.$$
Expand $(a_i + b_j)^t = \sum_{r=0}^t \binom{t}{r} a_i^r b_j^{t-r}$ and push the sums over $i$ and $j$ inside:
$$\begin{aligned}
\sum_{i=1}^n \sum_{j=1}^m (a_i + b_j)^t &= \sum_{r=0}^t \binom{t}{r} \left(\sum_{i=1}^n a_i^r\right) \left(\sum_{j=1}^m b_j^{t-r}\right) \\
&= t! \sum_{r=0}^t \left(\frac{p_r(A)}{r!}\right) \left(\frac{p_{t-r}(B)}{(t-r)!}\right).
\end{aligned}$$
Look at the structure:
1. Compute the power sums $p_r(A) = \sum_{i=1}^n a_i^r$ for $0 \le r \le K$ via subproduct tree $Q_A(x) = \prod_{i=1}^n (1 - a_i x)$ and $-x Q_A'(x)/Q_A(x) \bmod x^{K+1}$ in $O(n \log^2 n + K \log K)$ time.
2. Compute the power sums $p_s(B) = \sum_{j=1}^m b_j^s$ for $0 \le s \le K$ via $Q_B(x) = \prod_{j=1}^m (1 - b_j x)$ in $O(m \log^2 m + K \log K)$ time.
3. Convolve the EGFs $\sum_{r=0}^K \frac{p_r(A)}{r!} x^r$ and $\sum_{s=0}^K \frac{p_s(B)}{s!} x^s$ in **1 NTT convolution** of length $K+1$!

---

### 5. Hand-Checkable Trace ($m = 2$, $a = [2, 3]$, $N = 3$)

Let $A = [2, 3]$ ($m = 2$).
- **Ground Truth Power Sums**:
  - $p_0 = 2^0 + 3^0 = 2$
  - $p_1 = 2^1 + 3^1 = 5$
  - $p_2 = 2^2 + 3^2 = 13$
  - $p_3 = 2^3 + 3^3 = 35$
- **Logarithmic Derivative Trace**:
  1. Subproduct tree product: $Q(x) = (1 - 2x)(1 - 3x) = 1 - 5x + 6x^2$.
  2. Derivative: $Q'(x) = -5 + 12x$, so $-x Q'(x) = 5x - 12x^2$.
  3. Series inversion: $Q(x)^{-1} = (1 - (5x - 6x^2))^{-1} = 1 + (5x - 6x^2) + (5x - 6x^2)^2 + (5x - 6x^2)^3 + O(x^4) = 1 + 5x + 19x^2 + 65x^3 + O(x^4)$ (note that $[1, 5, 19, 65]$ are the complete homogeneous symmetric polynomials $h_0, h_1, h_2, h_3$!).
  4. Multiply $m - x Q'(x) Q(x)^{-1} \bmod x^4$:
     $$2 + (5x - 12x^2)(1 + 5x + 19x^2) = 2 + 5x + (25 - 12)x^2 + (95 - 60)x^3 + O(x^4) = 2 + 5x + 13x^2 + 35x^3 + O(x^4).$$
  The coefficients $[2, 5, 13, 35]$ match $p_0, p_1, p_2, p_3$ exactly.

---

## Iteration 67: Roots of Unity Filter (`单位根反演`), Floor Sums, and Cyclic Quotient Rings $K[x]/(x^k - 1)$

### 1. Concrete Counting Problem: Extracting Periodic Subsequences & Cyclic Remainder Sums

Given a formal power series or high-degree polynomial $F(x) = \sum_{n \ge 0} f_n x^n$ (such as $F(x) = (1 + x)^N$ or $F(x) = e^x$), suppose we want to sum every $k$-th coefficient belonging to a fixed residue class $r \pmod k$:
$$S_{r, k}(F) := \sum_{\substack{n \ge 0 \\ n \equiv r \pmod k}} f_n = \sum_{m=0}^\infty f_{mk + r}.$$
There are **two dual algebraic ways** to compute $S_{r, k}(F)$, and understanding their equivalence clarifies both when the Roots of Unity Filter works and what to do when the prime modulus $p$ does not have a primitive $k$-th root of unity!

#### Viewpoint 1: The Quotient Ring $K[x]/(x^k - 1)$ (Valid over ANY Commutative Ring $K$)
In the quotient ring $R_k = K[x]/(x^k - 1)$, we enforce the relation $x^k \equiv 1$. Therefore, for every integer $n \ge 0$, $x^n \equiv x^{n \bmod k}$, and the canonical projection of $F(x)$ into $K[x]/(x^k - 1)$ groups coefficients by residue class modulo $k$:
$$F(x) \bmod (x^k - 1) = \sum_{r=0}^{k-1} \left(\sum_{n \equiv r \pmod k} f_n\right) x^r = \sum_{r=0}^{k-1} S_{r, k}(F) x^r.$$
Notice that this requires **no division by $k$ and no roots of unity**! If $F(x) = P(x)^N$ for a small polynomial $P(x)$, we can compute $P(x)^N \bmod (x^k - 1)$ directly by binary exponentiation with cyclic convolutions of length $k$.

#### Viewpoint 2: The Roots of Unity Filter (`单位根反演`) (Diagonalizing $K[x]/(x^k - 1)$ via CRT)
Suppose $k$ is invertible in $K$ and $K$ contains a **primitive $k$-th root of unity** $\omega_k$ (for a prime field $\mathbb{F}_p$, this holds if and only if $k \mid (p - 1)$, where $\omega_k \equiv g^{(p-1)/k} \pmod p$ for a primitive root $g$ of $\mathbb{F}_p^\times$). Then $x^k - 1 = \prod_{j=0}^{k-1} (x - \omega_k^j)$ splits into distinct linear factors, and the Chinese Remainder Theorem isomorphically diagonalizes the cyclic quotient ring into $k$ independent scalar fields:
$$K[x]/(x^k - 1) \xrightarrow{\;\sim\;} \prod_{j=0}^{k-1} K[x]/(x - \omega_k^j) \cong K^k, \qquad F(x) \longmapsto \bigl(F(\omega_k^0), F(\omega_k^1), \dots, F(\omega_k^{k-1})\bigr).$$
Algebraically, the character orthogonality identity for any integer $m$:
$$\frac{1}{k} \sum_{j=0}^{k-1} \omega_k^{j m} = \begin{cases} 1 & \text{if } k \mid m, \\[6pt] \dfrac{\omega_k^{km} - 1}{k(\omega_k^m - 1)} = 0 & \text{if } k \nmid m, \end{cases} = [k \mid m],$$
allows us to insert the indicator $[n \equiv r \pmod k] = [k \mid (n - r)]$ directly into $\sum_{n \ge 0} f_n$:
$$\begin{aligned}
S_{r, k}(F) = \sum_{n \ge 0} f_n [k \mid (n - r)] &= \sum_{n \ge 0} f_n \left(\frac{1}{k} \sum_{j=0}^{k-1} \omega_k^{j(n - r)}\right) \\
&= \frac{1}{k} \sum_{j=0}^{k-1} \omega_k^{-jr} \sum_{n \ge 0} f_n \bigl(\omega_k^j\bigr)^n \\
&= \frac{1}{k} \sum_{j=0}^{k-1} \omega_k^{-jr} F(\omega_k^j).
\end{aligned}$$
Even more generally, keeping $x$ inside gives the decimated series:
$$\boxed{
\sum_{n \equiv r \pmod k} f_n x^n = \frac{1}{k} \sum_{j=0}^{k-1} \omega_k^{-jr} F(\omega_k^j x), \qquad S_{r, k}(F) = \frac{1}{k} \sum_{j=0}^{k-1} \omega_k^{-jr} F(\omega_k^j).
}$$

---

### 2. Decision Criterion: Roots of Unity Filter vs. Cyclic Quotient Ring $K[x]/(x^k - 1)$

Why is the Roots of Unity Filter so much faster when $F(x)$ has a closed form (like $(1 + ax)^N$ or $e^x$), and when must we fall back to $K[x]/(x^k - 1)$ or cyclotomic extensions?

| Scenario | Roots of Unity Filter (`单位根反演`) | Quotient Ring $K[x]/(x^k - 1)$ |
| :--- | :--- | :--- |
| **Requirement on Modulus $p$** | Requires $k \mid (p - 1)$ so $\omega_k \in \mathbb{F}_p$ exists | Works for **ANY** modulus $p$ (even composite $M$ or $p \mid k$) |
| **Evaluating $(1+x)^N \bmod (x^k-1)$ for single $r$** | **$O(k \log N)$** ($k$ scalar binary exponentiations $(1+\omega_k^j)^N$) | **$O(k \log k \log N)$** (polynomial binary exponentiation) or $O(k^2 \log N)$ |
| **Evaluating $(1+x)^N \bmod (x^k-1)$ for ALL $0 \le r < k$** | **$O(k \log N + k \log k)$** (evaluate $F(\omega_k^j)$, then 1 IDFT of size $k$) | **$O(k \log k \log N)$** |
| **Combining with Binomial / Taylor Sums $\sum_{i=0}^N \binom{N}{i} i^m [k \mid i]$** | Reduces immediately to $\frac{1}{k}\sum_{j=0}^{k-1} [t^m/m!] (1 + \omega_k^j e^t)^N$ | Requires tracking polynomial coefficients in $K[x]/(x^k-1)$ |
| **What if $k \nmid (p - 1)$?** | Work in the cyclotomic quotient ring $\mathbb{F}_p[\zeta]/(\Phi_k(\zeta))$ or use Bluestein's chirp-Z transform if $\omega_k$ exists for non-power-of-2 $k$ | Directly compute in $\mathbb{F}_p[x]/(x^k - 1)$! |

**Subtlety — Non-Power-of-2 $k$ When $k \mid (p - 1)$**:
For the standard NTT prime $p = 998244353 = 119 \times 2^{23} + 1$, a primitive $k$-th root of unity $\omega_k = 3^{(p-1)/k} \bmod p$ exists in $\mathbb{F}_p$ not only for powers of $2$ up to $2^{23}$, but also for any divisor of $p - 1 = 2^{23} \times 7 \times 17$. If we need all residue classes $r = 0, \dots, k-1$ simultaneously for a general $k \mid (p-1)$, we compute $y_j = F(\omega_k^j)$ for $0 \le j < k$ and apply **Bluestein's Chirp-Z Transform** $\omega_k^{-jr} = \omega_{2k}^{r^2 + j^2 - (r-j)^2}$ to compute all $S_{r, k}(F)$ in $O(k \log k)$ time via a single power-of-2 NTT!

---

### 3. The Floor-Sum Trick: Handling $\left\lfloor \frac{i}{k} \right\rfloor$ in Binomial Sums (Luogu P5591 `小猪佩奇学数学`)

A classic disguise of the Roots of Unity Filter is a sum containing the floor function $\lfloor i / k \rfloor$, such as Luogu P5591 (`小猪佩奇学数学`):
$$S = \sum_{i=0}^n \binom{n}{i} p^i \left\lfloor \frac{i}{k} \right\rfloor \pmod{998244353}, \qquad n \le 10^9, \quad k \mid (p-1), \quad k \le 2^{20}.$$
At first glance, $\lfloor i/k \rfloor$ is not periodic with period $k$ — it grows linearly with $i$! How do we make it periodic?
Use the division algorithm identity:
$$\boxed{
\left\lfloor \frac{i}{k} \right\rfloor = \frac{i - (i \bmod k)}{k}.
}$$
Substituting this splits $S$ into two completely decoupled sums:
$$S = \frac{1}{k} \underbrace{\sum_{i=0}^n i \binom{n}{i} p^i}_{S_{\text{linear}}} - \frac{1}{k} \underbrace{\sum_{i=0}^n (i \bmod k) \binom{n}{i} p^i}_{S_{\text{periodic}}}.$$
1. **The Linear Part $S_{\text{linear}}$**: Using $i \binom{n}{i} = n \binom{n-1}{i-1}$,
   $$S_{\text{linear}} = n p (1 + p)^{n-1}.$$
2. **The Periodic Part $S_{\text{periodic}}$**: Now $(i \bmod k)$ depends only on $r = i \bmod k \in \{0, 1, \dots, k-1\}$! Applying the Roots of Unity Filter:
   $$\begin{aligned}
   S_{\text{periodic}} &= \sum_{r=0}^{k-1} r \sum_{i \equiv r \pmod k} \binom{n}{i} p^i \\
   &= \sum_{r=0}^{k-1} r \left(\frac{1}{k} \sum_{j=0}^{k-1} \omega_k^{-jr} (1 + p \omega_k^j)^n\right) \\
   &= \frac{1}{k} \sum_{j=0}^{k-1} (1 + p \omega_k^j)^n \left(\sum_{r=0}^{k-1} r \omega_k^{-jr}\right).
   \end{aligned}$$
3. **Closed Form for the Inner Geometric-Arithmetic Weight $\sum_{r=0}^{k-1} r z^r$**:
   For $z = \omega_k^{-j}$:
   - When $j = 0$ ($z = 1$): $\sum_{r=0}^{k-1} r = \frac{k(k-1)}{2}$.
   - When $1 \le j < k$ ($z = \omega_k^{-j} \neq 1$, with $z^k = 1$): differentiating or multiplying $G(z) = \sum_{r=0}^{k-1} r z^r$ by $(1 - z)$ gives $(1 - z)G(z) = \sum_{r=1}^{k-1} z^r - (k-1)z^k = -1 - (k-1) = -k$, so:
     $$\boxed{
     \sum_{r=0}^{k-1} r \omega_k^{-jr} = \begin{cases} \dfrac{k(k-1)}{2} & \text{if } j = 0, \\[8pt] \dfrac{k}{\omega_k^{-j} - 1} & \text{if } 1 \le j < k. \end{cases}
     }$$
   The entire sum $S$ therefore reduces to a single loop over $j = 0, \dots, k-1$ running in **$O(k \log n)$ time**!

---

### 4. Multidimensional Root-of-Unity Filters & EGFs (UOJ #450 `复读机`)

Suppose we count length-$n$ sequences over an alphabet of $m$ types (an EGF problem where the count of each type $c_i$ is weighted by $\frac{x^{c_i}}{c_i!}$), subject to the constraint that **each type $i \in \{1, \dots, m\}$ appears a number of times $c_i$ satisfying a congruence condition modulo $d$** (for example, $d \mid c_i$, or at least $m - K$ types satisfy $d \mid c_i$).

For a single type $i$, the filtered EGF for $c_i \equiv r \pmod d$ is:
$$E_{r, d}(x) := \sum_{\substack{c \ge 0 \\ c \equiv r \pmod d}} \frac{x^c}{c!} = \frac{1}{d} \sum_{j=0}^{d-1} \omega_d^{-jr} e^{\omega_d^j x}.$$
Notice the algebraic miracle: $E_{r, d}(x)$ is a **linear combination of $d$ pure exponentials $e^{\omega_d^j x}$**!
When we multiply $E_{r, d}(x)$ across all $m$ independent types:
$$\left(E_{0, d}(x)\right)^m = \frac{1}{d^m} \left(\sum_{j=0}^{d-1} e^{\omega_d^j x}\right)^m.$$
Instead of $d^m$ distinct exponentials, any product $e^{\omega_d^{j_1} x} \cdots e^{\omega_d^{j_m} x} = \exp\!\left(\bigl(\sum_{t=0}^{d-1} a_t \omega_d^t\bigr) x\right)$ depends **only on the composition tuple $(a_0, a_1, \dots, a_{d-1})$** of how many types chose each root $\omega_d^t$, where $a_0 + \dots + a_{d-1} = m$!
- For $d = 2$ ($\omega_2 = -1$): there are only $m + 1$ tuples $(a_0, m - a_0)$.
- For $d = 3$: there are only $\binom{m+2}{2} = O(m^2)$ tuples $(a_0, a_1, a_2)$, reducing $3^m$ states to $O(m^2)$ exponential evaluations $\left(\sum_{t=0}^{d-1} a_t \omega_d^t\right)^n$!

---

### 5. Hand-Checkable Trace ($k = 3$, $n = 4$, $r = 1$)

Let us verify $S_{1, 3}((1+x)^4) = \binom{4}{1} + \binom{4}{4} = 4 + 1 = 5$ over $\mathbb{C}$ (or $\mathbb{F}_7$ where $\omega_3 = 2$ since $2^3 = 8 \equiv 1 \pmod 7$).
- **Trace in $\mathbb{F}_7$ ($\omega_3 = 2, \omega_3^2 = 4, 3^{-1} \equiv 5 \pmod 7, n = 4, r = 1$)**:
  - $j = 0$: $\omega_3^0 = 1$, $\omega_3^{-0\cdot 1} (1 + 1)^4 = 1 \cdot 16 \equiv 2 \pmod 7$.
  - $j = 1$: $\omega_3^1 = 2$, $\omega_3^{-1} (1 + 2)^4 = 4 \cdot 3^4 = 4 \cdot 81 \equiv 4 \cdot 4 = 16 \equiv 2 \pmod 7$.
  - $j = 2$: $\omega_3^2 = 4$, $\omega_3^{-2} (1 + 4)^4 = 2 \cdot 5^4 = 2 \cdot 625 \equiv 2 \cdot 2 = 4 \pmod 7$.
  - Sum divided by $3$: $3^{-1}(2 + 2 + 4) \equiv 5 \cdot 8 \equiv 40 \equiv 5 \pmod 7$.
  Matches $\binom{4}{1} + \binom{4}{4} = 5$ identically!

---

## Multilingual Bibliographic & Pedagogical Citations (Iterations 63–67)

1. **`[EN]` Aho, A. V., Steiglitz, K., & Ullman, J. D. (1975). "Evaluating polynomials at fixed sets of points." *SIAM Journal on Computing*, 4(4), 533–539.**
   - Establishes the $O(n \log n)$ convolution reduction for the polynomial Taylor shift $F(x+c)$ and proves that any rational linear (Möbius) substitution $(cx+d)^n F\bigl(\frac{ax+b}{cx+d}\bigr)$ factors into at most two Taylor shifts plus $O(n)$ diagonal scalings and reversals.
2. **`[EN]` Bostan, A., Chyzak, F., Giusti, M., Lebreton, R., Lecerf, G., Salvy, B., & Schost, É. (2017). *Algorithmes Efficaces en Calcul Formel*. Chapter 6 ("Changement de base et translation") & Chapter 15 ("Séries algébriques").**
   - Comprehensive mathematical treatment of basis conversions between monomials $x^k$, falling factorials $x^{\underline{k}}$, and shifted bases, alongside Newton's identities and quadratic algebraic generating functions.
3. **`[EN]` Flajolet, P., & Sedgewick, R. (2009). *Analytic Combinatorics*. Cambridge University Press. Chapter V.2 ("Lattice paths and walks") & Appendix B.4 ("Lagrange Inversion").**
   - Derives the continued-fraction Chebyshev polynomials for bounded-height lattice paths and the formal residue change-of-variables method for Motzkin and Schröder walks.
4. **`[EN]` Stanley, R. P. (1999). *Enumerative Combinatorics, Volume 2*. Cambridge University Press. Chapter 6.3 ("Diagonal of rational functions and Central Delannoy numbers") & Chapter 7 ("Symmetric Functions").**
   - Proves the equivalence between Central Delannoy / Large Schröder generating functions $\frac{1}{\sqrt{1-6x+x^2}}$ and symmetric function identities $\ln H(x) = \sum_{k \ge 1} \frac{p_k}{k} x^k$.
5. **`[EN]` Codeforces Blog — adamant (2019–2022). "Polynomial shift in $O(n \log n)$", "Krawtchouk polynomials in CP", and "Symmetric polynomials and Newton's identities".**
   - Synthesizes the competitive-programming pipeline for $(1+x)^n F\bigl(\frac{1-x}{1+x}\bigr)$ via two Taylor shifts and the subproduct-tree logarithmic derivative $\sum_{i=1}^m \frac{1}{1-a_i x} = m - x \frac{Q'(x)}{Q(x)}$.
6. **`[ZH]` 钟子谦 (Zhong Ziqian, 2019). 《浅谈下降幂多项式》 (*IOI 2019 国家集训队论文集 / Chinese National Team Papers 2019*).**
   - The foundational Chinese OI paper introducing the Point-Value EGF theorem $\widehat{F}(t) = A(t)e^t$ for falling-factorial polynomials (`下降幂多项式`), proving $O(n \log n)$ multiplication (`P5393`), $O(n \log^2 n)$ monomial-to-falling conversion (`P5394`), and $O(n)$ evaluation of binomial moment sums $\sum_{i=0}^M \binom{M}{i} p^i q^{M-i} F(i)$.
7. **`[ZH]` 付公主 / 杜教 (2017–2018). 《生成函数与多项式对数导数技巧》 & OI-Wiki ("多项式平移、斯特林数与单位根反演").**
   - Standardizes the Chinese OI terminology `ln / exp Trick` contrasting the $O(n \log n)$ harmonic-sieve Euler product (`P4389 付公主的背包`) with the $O(m \log^2 m + n \log n)$ subproduct-tree power-sum logarithmic derivative (`P4705 玩游戏`), as well as `单位根反演` (Roots of Unity Filter) for floor sums (`P5591`) and multidimensional cyclic EGFs (`UOJ #450 复读机`).
8. **`[JA]` Maspy (2021–2023). 「多項式の平行移動 (Taylor Shift) と一次分数変換」「ウォルシュ・アダマール変換とクラウチュク多項式」 (*maspyのHP*).**
   - Derives the $GL_2(\mathbb{F}_p)$ group action on degree-$n$ polynomials, the two-shift Krawtchouk reduction used in AtCoder ARC136 F (`Flip Cells`), and the rationalizing substitution for quadratic radicals $\sqrt{1 - 2ax + bx^2}$.
9. **`[JA]` Noshi91 & Editorial Team (2020–2024). AtCoder ABC/ARC/AGC Editorials (ABC267 Ex, ARC136 F, AGC038 E).**
   - Explains parity/mod-$k$ root-of-unity filters in $\mathbb{F}_{998244353}$ and falling-factorial basis reductions in Japanese competitive programming.

---

## Problem Harvesting, Rejections, and Pedagogical Bridges (Iterations 63–67)

### Rejected Library-Checker & Pure Template Problems (Excluded per Repository Policy)

Per `AGENTS.md`, pure verification and template implementation problems are excluded from the main problem bank and recorded here so future contributors do not re-add them:

| # | Platform & ID | Title | Reason for Rejection |
| :- | :--- | :--- | :--- |
| R1 | Library Checker | `polynomial_taylor_shift` | Pure verification of $F(x+c)$ in $O(n \log n)$ with zero combinatorial modelling. |
| R2 | Luogu P5393 | `下降幂多项式乘法` (Falling-Factorial Polynomial Multiplication) | Direct template verification of $\widehat{F}(t) = A(t)e^t$, pointwise multiplication, and $\widehat{H}(t)e^{-t}$. |
| R3 | Luogu P5394 | `【模板】下降幂多项式` | Pure template conversion of an ordinary polynomial to falling-factorial basis. |
| R4 | Library Checker | `stirling_number_of_the_first_kind` / `stirling_number_of_the_second_kind` | Pure row computation of $\left[\begin{matrix} n \\ k \end{matrix}\right]$ and $\left\{\begin{matrix} n \\ k \end{matrix}\right\}$. |
| R5 | Luogu P5383 / P5395 | `第二类斯特林数·行` / `第一类斯特林数·行` | Direct row convolution templates without problem reduction. |
| R6 | Library Checker | `kth_term_of_linearly_recurrent_sequence` | Pure Bostan-Mori template without modelling. |

---

### Accepted Problems: Summary Table (24 Problems Across Clusters A–E)

| # | Cluster | Problem ID & Title | Platform | Difficulty | Core Technique |
| :- | :--- | :--- | :--- | :---: | :--- |
| **A1** | Iter 63 ($GL_2$ / Krawtchouk) | **ARC136 F** — *Flip Cells* | AtCoder | 2800 | EGF parity product + Krawtchouk $(1-x)^k(1+x)^{n-k}$ via 2 Taylor shifts |
| **A2** | Iter 63 ($GL_2$ / Shift) | **CF 1349D** — *Slime and Biscuits* | Codeforces | 2900 | Potential EGF + $GL_2$ rational linear substitution on hypercube transitions |
| **A3** | Iter 63 ($GL_2$ / Shift) | **AGC005 F** — *Many Easy Problems* | AtCoder | 2200 | Binomial upper-index convolution reduced to reversed Taylor shift |
| **A4** | Iter 63 ($GL_2$ / Shift) | **CF 923E** — *Perpetual Subtraction* | Codeforces | 2600 | Forward Taylor shift + diagonal eigenbasis diagonalization + inverse Taylor shift |
| **A5** | Iter 63 ($GL_2$ / Euler) | **CF 1548C** — *The Three Little Pigs* | Codeforces | 2100 | Affine polynomial shift $(1+x)^{3n}$ and root/shift reduction |
| **B1** | Iter 64 (Radical Subst.) | **LOJ #6261 / CF 438E-variant** — *Catalan Radical Convolution* | LibreOJ / CF | 2500 | Quadratic radical $\frac{H(x)}{\sqrt{1 - 4x}}$ via Catalan substitution $x = \frac{u}{(1+u)^2}$ |
| **B2** | Iter 64 (Radical Subst.) | **GYM 102978 H** — *Motzkin Paths with Colored Peaks* | CF Gym | 2700 | Motzkin radical $\sqrt{1-2x-3x^2}$ cleared via $x = \frac{u}{1+u+u^2}$ |
| **B3** | Iter 64 (Radical Subst.) | **UOJ #424** — *「集训队作业 2018」count* | UOJ | 2700 | Bounded-height Dyck/Catalan walks on $[0, K]$ via Chebyshev $P_K(x)$ & reflection in $u$ |
| **B4** | Iter 64 (Radical Subst.) | **LOJ #6077 / P4491-variant** — *Schröder & Delannoy Path Convolution* | LibreOJ | 2600 | Large Schröder / Central Delannoy $\frac{1}{\sqrt{1-6x+x^2}}$ via $x = \frac{u}{(1+u)(1+2u)}$ |
| **B5** | Iter 64 (Radical Subst.) | **AGC021 E** — *Ball Eat Chameleons* | AtCoder | 2600 | Bounded-strip Dyck path reflection equivalent to Chebyshev quotient $\frac{U_{H-1}}{U_H}$ |
| **C1** | Iter 65 (Falling Fact.) | **Luogu P6620** — *[省选联考 2020 A 卷] 组合数问题* | Luogu | 2300 | Convert $F(k)$ to $\sum a_j k^{\underline{j}}$ to collapse $\sum_{k=0}^n f(k) x^k \binom{n}{k}$ to $O(m^2)$ or $O(m \log m)$ |
| **C2** | Iter 65 (Falling Fact.) | **CF 932E** — *Team Work* | Codeforces | 2200 | Convert $i^k = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} i^{\underline{j}}$ to evaluate $\sum_{i=1}^n \binom{n}{i} i^k$ in $O(k \log k)$ |
| **C3** | Iter 65 (Falling Fact.) | **CF 1097G** — *Vladislav and a Great Legend* | Codeforces | 2600 | Edge-subset power $(|E(S)|)^k = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} j! \binom{|E(S)|}{j}$ DP on trees |
| **C4** | Iter 65 (Falling Fact.) | **CF 1278F** — *Cards* | Codeforces | 2400 | Binomial moment $\mathbb{E}[X^k] = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} n^{\underline{j}} p^j$ via $O(k \log k)$ Stirling row |
| **C5** | Iter 65 (Falling Fact.) | **Luogu P6667** — *如何优雅地求和* | Luogu | 2500 | Point-values $F(0)\dots F(m) \xrightarrow{e^{-t}} a_k \xrightarrow{O(m)} \sum_{k=0}^n F(k)\binom{n}{k} x^k (1-x)^{n-k}$ |
| **D1** | Iter 66 (Power-Sum $\ln'$) | **Luogu P4705** — *玩游戏* | Luogu | 2500 | Expected $(a_i + b_j)^t$ via Regime B subproduct tree $-x \frac{Q'(x)}{Q(x)}$ + EGF convolution |
| **D2** | Iter 66 (Harmonic $\ln$) | **Luogu P4389** — *付公主的背包* | Luogu | 2400 | Regime A unbounded knapsack $\prod_{i=1}^n (1 - x^{v_i})^{-1}$ via $O(m \log m)$ harmonic $\ln + \exp$ |
| **D3** | Iter 66 (Newton / $\ln'$) | **LOJ #6503** — *「雅礼集训 2018 Day4」Magic* | LibreOJ | 2500 | Subproduct tree + $\ln / \exp$ to extract symmetric / block polynomials |
| **D4** | Iter 66 (Harmonic $\ln$) | **LOJ #6089** — *小 Y 的背包计数问题* | LibreOJ | 2400 | Bounded knapsack $\prod_{i=1}^n \frac{1-x^{i(i+1)}}{1-x^i}$ via $O(n\sqrt{n})$ DP vs. $O(n \log n)$ harmonic $\ln/\exp$ |
| **D5** | Iter 66 (Power-Sum $\ln'$) | **CF 1613F** — *Tree Coloring* | Codeforces | 2500 | Subproduct tree $\prod_{u} (1 + d_u x)$ vs. frequency grouping + $\ln/\exp$ |
| **E1** | Iter 67 (Roots of Unity) | **Luogu P5591** — *小猪佩奇学数学* | Luogu | 2500 | Floor sum $\sum_{i=0}^n \binom{n}{i} p^i \lfloor i/k \rfloor$ via $\lfloor i/k \rfloor = \frac{i - (i \bmod k)}{k}$ and size-$k$ root filter |
| **E2** | Iter 67 (Roots of Unity) | **LOJ #6485** — *LJJ 学二项式定理* | LibreOJ | 2200 | 4-residue weighted binomial sum $\sum_{i=0}^n \binom{n}{i} s^i a_{i \bmod 4}$ via $\omega_4 \in \mathbb{F}_{998244353}$ |
| **E3** | Iter 67 (Roots of Unity) | **UOJ #450** — *「UNR #3」复读机* | UOJ | 2600 | Multidimensional mod-$d$ EGF $\left(\frac{1}{d}\sum_{j=0}^{d-1} e^{\omega_d^j x}\right)^k$ compressed to $\binom{k+d-1}{d-1}$ states |
| **E4** | Iter 67 (Roots of Unity) | **AtCoder ABC267 Ex** — *Odd Sum* | AtCoder | 2400 | 2D generating function $[x^M] \frac{1}{2}\bigl(P(x, 1) - P(x, -1)\bigr)$ with $\omega_2 = -1$ parity filter |

---

### Detailed Problem Specifications & Two-Stage Pedagogical Bridges

#### Cluster A: Iteration 63 ($GL_2$ Möbius Action, Taylor Shift, and Krawtchouk Transform)

##### Problem A1: AtCoder ARC136 F — Flip Cells
- **Metadata**: Platform: AtCoder | ID: `arc136_f` | Title: *Flip Cells* | Difficulty: 2800 (4 Yellow) | Tags: `EGF`, `Krawtchouk Transform`, `Taylor Shift`, `Absorbing Markov Chain`.
- **Inline Problem Statement**: You are given an $H \times W$ grid of binary cells ($H \le 50, W \le 50$, so $N = HW \le 2500$; the polynomial step scales to $N \le 2.5 \times 10^5$) and target row popcounts $A_1, \dots, A_H$. At each step you uniformly at random pick one of the $N$ cells and flip its state ($0 \leftrightarrow 1$). Find the expected number of flips until, for every row $i$, the number of $1$s in row $i$ equals $A_i$, modulo $998244353$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  Let $F(t)$ be the EGF of transitioning from the initial grid to a valid target grid in $m$ flips, and $G(t)$ be the EGF of transitioning from any valid target grid to any valid target grid in $m$ flips (by symmetry, $G(t)$ is independent of which valid target grid we start at!). If a valid target grid has $k$ cells that differ from the initial grid, then in $m$ flips those $k$ cells must be flipped an odd number of times ($\sinh(t/N)$) and the remaining $N-k$ cells an even number of times ($\cosh(t/N)$). Summing over all valid target configurations with $f_k$ configurations at Hamming distance $k$ from the start gives:
  $$F(t) = \sum_{k=0}^N f_k \left(\frac{e^{t/N} - e^{-t/N}}{2}\right)^k \left(\frac{e^{t/N} + e^{-t/N}}{2}\right)^{N-k} = e^{t} 2^{-N} \sum_{k=0}^N f_k \bigl(1 - e^{-2t/N}\bigr)^k \bigl(1 + e^{-2t/N}\bigr)^{N-k}.$$
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Setting $x = e^{-2t/N}$, the sum $\sum_{k=0}^N f_k (1-x)^k (1+x)^{N-k}$ is precisely the **Krawtchouk transform** $(1+x)^N P\bigl(\frac{1-x}{1+x}\bigr)$ of $P(x) = \sum_{k=0}^N f_k x^k$ (and similarly for $G(t)$ where $g_k$ counts valid target pairs at distance $k$). Applying the 2-Taylor-shift Krawtchouk reduction expresses both $F(t)$ and $G(t)$ as linear combinations $\sum_{j=0}^N c_j e^{\frac{N - 2j}{N} t}$, from which the expected hitting time $\left.\frac{d}{ds}\left(\frac{\mathcal{L}F(s)}{\mathcal{L}G(s)}\right)\right|_{s=0}$ is extracted in $O(N \log N)$ time for the polynomial step.

##### Problem A2: Codeforces 1349D — Slime and Biscuits
- **Metadata**: Platform: Codeforces | ID: `1349D` | Title: *Slime and Biscuits* | Difficulty: 2900 | Tags: `Potential Function`, `Generating Functions`, `Linear Recurrence / Shift`.
- **Inline Problem Statement**: There are $n$ players ($n \le 10^5$) holding $a_1, a_2, \dots, a_n$ biscuits ($\sum a_i = S \le 3 \times 10^5$). Each second, one biscuit is chosen uniformly at random among all $S$ biscuits and transferred to a uniformly chosen player among the other $n-1$ players. Find the expected time until one player holds all $S$ biscuits, modulo $998244353$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  From an EGF viewpoint (dual to potential functions), if we track the state of each biscuit as either belonging to target player $i$ (state $+1$) or one of the $n-1$ other players (weight $n-1$), the EGF for $k$ biscuits initially not with player $i$ all ending up with player $i$ after $m$ steps is $\left(\frac{e^{t/S} - e^{-t/((n-1)S)}}{n}\right)^k \left(\frac{e^{t/S} + (n-1)e^{-t/((n-1)S)}}{n}\right)^{S-k}$.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  With $x = e^{-\frac{n}{(n-1)S} t}$, the transition polynomial across all $n$ players is $\sum_{k=0}^S f_k (1 - x)^k (1 + (n-1)x)^{S-k}$, which is the **$GL_2(\mathbb{F}_p)$ Möbius action** for $g = \begin{pmatrix} -1 & 1 \\ n-1 & 1 \end{pmatrix}$! This evaluates in $O(S \log S)$ via two Taylor shifts (or directly in $O(S)$ via the three-term tridiagonal differential recurrence induced by $\Delta(x)$).

##### Problem A3: AtCoder AGC005 F — Many Easy Problems
- **Metadata**: Platform: AtCoder | ID: `agc005_f` | Title: *Many Easy Problems* | Difficulty: 2200 | Tags: `Trees`, `Binomial Convolution`, `Taylor Shift`.
- **Inline Problem Statement**: Given a tree $T$ on $n$ vertices ($n \le 2 \times 10^5$), for every $k = 1, 2, \dots, n$, compute the sum of sizes of the minimal subtree spanning $S$ over all $\binom{n}{k}$ subsets $S \subseteq V(T)$ of size $k$, modulo $924844033$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  By linearity of expectation, a vertex $v$ belongs to the minimal subtree spanning $S$ unless $S$ is contained entirely inside a single connected component of $T \setminus \{v\}$. Letting $c_m$ be the number of directed subtrees of size $m$ across all $2(n-1)$ oriented edges, the answer for $k$ is $n\binom{n}{k} - \sum_{m=k}^n c_m \binom{m}{k}$.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Notice that $\sum_{m=k}^n c_m \binom{m}{k} = [x^k] \sum_{m=0}^n c_m (x + 1)^m = [x^k] C(x + 1)$, where $C(x) = \sum_{m=0}^n c_m x^m$! Thus computing the answer for all $k = 1, \dots, n$ simultaneously is literally **a single Taylor shift $C(x + 1)$** by $s = 1$, solved in $O(n \log n)$ time with 1 NTT convolution.

##### Problem A4: Codeforces 923E — Perpetual Subtraction
- **Metadata**: Platform: Codeforces | ID: `923E` | Title: *Perpetual Subtraction* | Difficulty: 2600 | Tags: `Linear Algebra`, `Eigenbasis`, `Taylor Shift`.
- **Inline Problem Statement**: You start with a random integer $X_0 \in \{0, 1, \dots, n\}$ ($n \le 10^5$) with given probability distribution $p_0, p_1, \dots, p_n$. In each of $M$ steps ($M \le 10^{18}$), you replace $X$ with a uniformly random integer in $\{0, 1, \dots, X\}$. Find the final probability distribution after $M$ steps, modulo $998244353$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  In polynomial form, if $P^{(t)}(x) = \sum_{k=0}^n p_k^{(t)} x^k$, then one step sends $x^k \mapsto \frac{1}{k+1} \sum_{j=0}^k x^j = \frac{x^{k+1} - 1}{(k+1)(x - 1)}$. In the shifted basis $(x - 1)^k$, $\sum_{j=0}^n \binom{j}{k} \frac{1}{j+1} = \frac{1}{k+1} \binom{n+1}{k+1}$, which means the transition operator $T$ is **diagonal in the shifted basis $(x - 1)^k$** with eigenvalue $\lambda_k = \frac{1}{k+1}$!
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  1. Perform a **Taylor shift by $+1$**: compute $Q(y) = P^{(0)}(y + 1) = \sum_{k=0}^n q_k y^k$ in $O(n \log n)$ time.
  2. Apply $M$ steps in the eigenbasis in $O(n)$ time: $q_k^{(M)} = q_k \cdot (k + 1)^{-M} \bmod p$.
  3. Perform an **inverse Taylor shift by $-1$**: compute $P^{(M)}(x) = Q^{(M)}(x - 1)$ in $O(n \log n)$ time.
  Total time: $O(n \log n + n \log M)$ using 2 Taylor shifts!

##### Problem A5: Codeforces 1548C — The Three Little Pigs
- **Metadata**: Platform: Codeforces | ID: `1548C` | Title: *The Three Little Pigs* | Difficulty: 2100 | Tags: `Polynomial Shift`, `Generating Functions`.
- **Inline Problem Statement**: Given $n \le 10^6$ and $q \le 2 \times 10^5$ queries $x \in \{1, \dots, 3n\}$, compute $\sum_{i=1}^n \binom{3i}{x} \bmod 10^9+7$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  Form the polynomial $F(z) = \sum_{i=1}^n (1 + z)^{3i} = (1+z)^3 \frac{(1+z)^{3n} - 1}{(1+z)^3 - 1}$. We need $[z^x] F(z)$ for all $1 \le x \le 3n$.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Instead of shifting $(1+z)^{3n}$, notice that $(1+z)^3 - 1 = z(z^2 + 3z + 3)$, and the numerator $(1+z)^{3n+3} - (1+z)^3$ has known binomial coefficients in the $z$-basis directly! Dividing a degree-$(3n+3)$ polynomial by the quadratic $z^2 + 3z + 3$ in $O(n)$ time gives all $3n$ answers in linear time.

---

#### Cluster B: Iteration 64 (Radical Generating Functions & Universal Euler Substitutions)

##### Problem B1: LibreOJ #6261 / CF-Style Catalan Radical Power Sum
- **Metadata**: Platform: LibreOJ / Codeforces | ID: `LOJ 6261` / `CF 438E-variant` | Title: *Catalan Radical Convolution* | Difficulty: 2500 | Tags: `Catalan Substitution`, `Radical Generating Functions`, `Lagrange Inversion`.
- **Inline Problem Statement**: Given a polynomial $H(x) = \sum_{k=0}^n h_k x^k$ of degree $n \le 2 \cdot 10^5$ and an integer $m \le n$, compute $[x^m] \frac{H(x)}{\sqrt{1 - 4x}} \bmod 998244353$ and $[x^m] H\bigl(\frac{1-\sqrt{1-4x}}{2}\bigr) \bmod 998244353$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  The series $\frac{1}{\sqrt{1-4x}} = \sum_{r \ge 0} \binom{2r}{r} x^r$ counts unconstrained central binomial bridges, while $u(x) = \frac{1-\sqrt{1-4x}}{2} = x C(x)$ is the shifted Catalan generating function.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Applying the universal Euler substitution with $a = 2, b = 0, c = 1$ gives $x = \frac{u}{(1+u)^2}$ and $\sqrt{1-4x} = \frac{1-u}{1+u}$. By Formula B, $[x^m] H(u(x)) = [u^m] H(u) \frac{1-u}{1+u} (1+u)^{2m} = [u^m] H(u)(1-u)(1+u)^{2m-1}$, which evaluates in **$O(m)$ time** (a single dot product of the coefficients of $H(u)$ with binomial coefficients $\binom{2m-1}{m-k} - \binom{2m-1}{m-k-1}$)!

##### Problem B2: GYM 102978 H / Motzkin Excursion Composition
- **Metadata**: Platform: Codeforces Gym (Petrozavodsk / XIX Open Cup) | ID: `102978H` | Title: *Motzkin Paths with Colored Peaks* | Difficulty: 2700 | Tags: `Motzkin Generating Function`, `Euler Substitution`, `Lagrange Inversion`.
- **Inline Problem Statement**: Count the number of Motzkin paths of length $n \le 2 \cdot 10^5$ from $(0,0)$ to $(n,0)$ whose $k$ returns to the $x$-axis are weighted by a given polynomial sequence $w_k$, and where bridges are allowed after the last return, modulo $998244353$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  A Motzkin excursion between consecutive returns has OGF $u(x) = x M(x) = \frac{1 - x - \sqrt{1 - 2x - 3x^2}}{2x}$, and the trailing Motzkin bridge has OGF $\frac{1}{\sqrt{1 - 2x - 3x^2}}$. Thus the total OGF is $\frac{W(u(x))}{\sqrt{1 - 2x - 3x^2}}$ where $W(u) = \sum_{k=0}^n w_k u^k$.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Rather than computing $\sqrt{1 - 2x - 3x^2}$ and composing $W(u(x))$ in $O(n \log^2 n)$, apply **Formula A** with $a = 1, b = -3, c = \frac{1^2 - (-3)}{4} = 1$:
  $$[x^n] \frac{W(u(x))}{\sqrt{1 - 2x - 3x^2}} = [u^n] W(u) (1 + u + u^2)^n.$$
  Compute $(1 + u + u^2)^n \bmod u^{n+1}$ in $O(n)$ time via the D-finite three-term recurrence of central trinomial coefficients (or 1 NTT), then take the inner product with $w_k$ in $O(n)$ time!

##### Problem B3: UOJ #424 — 「集训队作业 2018」count (Cartesian Trees of Bounded Left-Depth)
- **Metadata**: Platform: UOJ | ID: `424` | Title: *「集训队作业 2018」count* | Difficulty: 2700 | Tags: `Cartesian Tree`, `Bounded Dyck Paths`, `Chebyshev Polynomials`, `Reflection Principle`.
- **Inline Problem Statement**: Two sequences of length $n$ are equivalent if their Cartesian trees have the same shape (breaking ties to the left). Find the number of equivalence classes of sequences of length $n$ over $\{1, \dots, m\}$ ($n, m \le 2 \cdot 10^5$), modulo $998244353$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  A sequence of length $n$ can be realized using alphabet $\{1, \dots, m\}$ if and only if its Cartesian tree has **maximum left-chain depth at most $m$**. Under the standard bijection between binary trees of size $n$ and Dyck paths of semi-length $n$, this is equivalent to counting Dyck paths of semi-length $n$ whose height never exceeds $m$. The OGF is $F_m(x) = \frac{P_m(x)}{P_{m+1}(x)}$ where $P_{k+1}(x) = P_k(x) - x P_{k-1}(x)$.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Applying the Catalan substitution $x = \frac{u}{(1+u)^2}$ ($a=2, b=0, c=1$) transforms $P_k(x(u))$ into $\frac{1 - u^{k+1}}{(1-u)(1+u)^k}$. By Formula B,
  $$[x^n] \frac{P_m(x)}{P_{m+1}(x)} = [u^n] (1 - u^2)(1+u)^{2n} \frac{1 - u^{m+1}}{1 - u^{m+2}}.$$
  Expanding $\frac{1}{1 - u^{m+2}} = \sum_{r \ge 0} u^{r(m+2)}$ has at most $\lfloor \frac{n}{m+2} \rfloor$ non-zero terms, so the answer is a simple alternating sum of $O(n/m)$ binomial coefficients $\binom{2n}{n - r(m+2)}$, computed in **$O(n)$ total time** without a single FFT!

##### Problem B4: LibreOJ #6077 / Luogu P4491 — Large Schröder & Central Delannoy Lattice Paths
- **Metadata**: Platform: LibreOJ | ID: `6077` (Radical Variant) | Title: *Schröder & Delannoy Path Convolution* | Difficulty: 2600 | Tags: `Schröder Numbers`, `Central Delannoy`, `Euler Substitution`.
- **Inline Problem Statement**: Given weights $c_0, \dots, c_n$ ($n \le 2 \cdot 10^5$), compute $\sum_{k=0}^n c_k [x^n] \frac{S(x)^k}{\sqrt{1 - 6x + x^2}} \bmod 998244353$, where $S(x) = \frac{1 - x - \sqrt{1 - 6x + x^2}}{2x}$ is the Large Schröder generating function.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  Here $\Delta(x) = 1 - 6x + x^2$ has $a = 3, b = 1, c = \frac{9-1}{4} = 2$, and $u(x) = \frac{1 - 3x - \sqrt{1 - 6x + x^2}}{4x}$ satisfies $S(x(u)) = 1 + 2u$ under $x = \frac{u}{(1+u)(1+2u)}$!
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Let us verify $x S(x)$ at $x = \frac{u}{(1+u)(1+2u)}$: since $\sqrt{1-6x+x^2} = \frac{1-2u^2}{(1+u)(1+2u)}$, we have
  $$x S(x) = \frac{1 - x - \sqrt{1-6x+x^2}}{2} = \frac{(1+3u+2u^2) - u - (1-2u^2)}{2(1+u)(1+2u)} = \frac{2u(1+2u)}{2(1+u)(1+2u)} = \frac{u}{1+u}, \qquad S(x(u)) = 1 + 2u!$$
  Notice how $S(x(u)) = 1 + 2u$ is **linear in $u$**! Therefore, by Formula A:
  $$[x^n] \frac{\sum_{k=0}^n c_k S(x)^k}{\sqrt{1 - 6x + x^2}} = [u^n] (1+u)^n (1+2u)^n \sum_{k=0}^n c_k (1 + 2u)^k.$$
  All we need is a **single Taylor shift** of $C(z) = \sum_{k=0}^n c_k z^k$ at $z = 1 + 2u$, followed by multiplying with $(1+u)^n (1+2u)^n$ in $O(n \log n)$ time!

##### Problem B5: AtCoder AGC021 E — Ball Eat Chameleons
- **Metadata**: Platform: AtCoder | ID: `agc021_e` | Title: *Ball Eat Chameleons* | Difficulty: 2600 | Tags: `Lattice Paths`, `Reflection Principle`, `Catalan / Chebyshev`.
- **Inline Problem Statement**: There are $n$ chameleons, initially all blue. You feed $k$ balls ($n, k \le 5 \times 10^5$), each painted red or blue, to the chameleons. A chameleon turns red when it has eaten strictly more red balls than blue balls, and turns blue when it has eaten strictly more blue balls than red balls. Count the number of color sequences of $k$ balls that can make all $n$ chameleons red at the end, modulo $998244353$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  For a fixed number of red balls $R$ and blue balls $B = k - R$ (with $R \ge B$), all $n$ chameleons can end up red if and only if the lattice path of $(R, B)$ never dips below the line $y = x - (R - B + n - 1)$ (with a boundary adjustment when $R = B$).
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  In generating-function terms, the reflection against a single line corresponds to the $r = 1$ term of the $u$-domain Catalan reflection formula $[u^B] (1 - u^{R-B+n})(1+u)^{R+B}$, reducing the count for each $(R, B)$ to $\binom{R+B}{R} - \binom{R+B}{B - (R - B + n)}$ in $O(1)$ per pair and $O(k)$ overall.

---

#### Cluster C: Iteration 65 (Falling-Factorial Polynomials & Stirling Basis Conversions)

##### Problem C1: Luogu P6620 — [省选联考 2020 A 卷] 组合数问题
- **Metadata**: Platform: Luogu | ID: `P6620` | Title: *[省选联考 2020 A 卷] 组合数问题* | Difficulty: 2300 (省选/NOI-) | Tags: `Falling-Factorial Polynomial`, `Stirling Numbers of the Second Kind`, `Binomial Moment`.
- **Inline Problem Statement**: Given integers $n, x, p$ ($n \le 10^9$, $p \le 10^9$ not necessarily prime!) and a polynomial $f(k) = \sum_{i=0}^m a_i k^i$ of degree $m \le 1000$, compute
  $$\sum_{k=0}^n f(k) x^k \binom{n}{k} \pmod p.$$
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  Because $n \le 10^9$ is huge while $m = \deg(f) \le 1000$ is small, we must absorb $f(k)$ into $\binom{n}{k}$ using $\binom{n}{k} k^{\underline{j}} = n^{\underline{j}} \binom{n-j}{k-j}$. Expanding $f(k) = \sum_{j=0}^m b_j k^{\underline{j}}$ in the falling-factorial basis transforms the sum into:
  $$\sum_{k=0}^n f(k) x^k \binom{n}{k} = \sum_{j=0}^m b_j n^{\underline{j}} x^j \sum_{k=j}^n \binom{n-j}{k-j} x^{k-j} = \sum_{j=0}^m b_j n^{\underline{j}} x^j (1 + x)^{n-j}.$$
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Notice that $p$ is **not necessarily prime**, so we cannot divide by $j!$ in $\widehat{F}(t)e^{-t}$. Instead, since $k^i = \sum_{j=0}^i \left\{\begin{matrix} i \\ j \end{matrix}\right\} k^{\underline{j}}$, we precompute the Stirling numbers of the second kind $\left\{\begin{matrix} i \\ j \end{matrix}\right\} \bmod p$ in $O(m^2)$ using the additive recurrence $\left\{\begin{matrix} i \\ j \end{matrix}\right\} = \left\{\begin{matrix} i-1 \\ j-1 \end{matrix}\right\} + j \left\{\begin{matrix} i-1 \\ j \end{matrix}\right\}$ (zero divisions!), compute $b_j = \sum_{i=j}^m a_i \left\{\begin{matrix} i \\ j \end{matrix}\right\} \bmod p$, and evaluate the final sum in $O(m^2 + m \log n)$ time. (When $p = 998244353$ and $m \le 2 \cdot 10^5$, converting $f(k)$ via multipoint evaluation + $e^{-t}$ solves it in $O(m \log^2 m)$.)

##### Problem C2: Codeforces 932E — Team Work
- **Metadata**: Platform: Codeforces | ID: `932E` | Title: *Team Work* | Difficulty: 2200 | Tags: `Falling Factorials`, `Stirling Numbers`, `NTT`.
- **Inline Problem Statement**: Given $n \le 10^9$ and $k \le 5000$ (or $k \le 2 \cdot 10^5$ in the NTT generalization), compute $\sum_{i=1}^n \binom{n}{i} i^k \pmod{10^9+7}$ (or $\bmod 998244353$).
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  Here $F(i) = i^k$ is a single monomial. Converting $i^k = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} i^{\underline{j}}$ collapses the sum of length $n \le 10^9$ to length $k$:
  $$\sum_{i=1}^n \binom{n}{i} i^k = \sum_{j=0}^{\min(n, k)} \left\{\begin{matrix} k \\ j \end{matrix}\right\} n^{\underline{j}} 2^{n-j}.$$
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Using the Point-Value EGF of $F(x) = x^k$, the coefficients $a_j = \left\{\begin{matrix} k \\ j \end{matrix}\right\}$ are extracted in **$O(k \log k)$ time** via $A(t) = \left(\sum_{m=0}^k \frac{m^k}{m!} t^m\right) e^{-t} \bmod t^{k+1}$ (with $m^k$ sieved in $O(k)$ time), followed by an $O(k)$ accumulation of $\sum_{j=0}^k a_j n^{\underline{j}} 2^{n-j}$.

##### Problem C3: Codeforces 1097G — Vladislav and a Great Legend
- **Metadata**: Platform: Codeforces | ID: `1097G` | Title: *Vladislav and a Great Legend* | Difficulty: 2600 | Tags: `Tree DP`, `Falling Factorials`, `Stirling Numbers`.
- **Inline Problem Statement**: Given a tree $T$ on $n \le 10^5$ vertices and an integer $k \le 200$, for every non-empty subset $X \subseteq V(T)$, let $f(X)$ be the number of edges in the minimal subtree spanning $X$. Compute $\sum_{\emptyset \neq X \subseteq V(T)} f(X)^k \bmod 10^9+7$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  Tracking $f(X)^k$ directly in a tree DP would require maintaining degree-$k$ ordinary polynomials where combining two subtrees costs $O(k^2)$ without size pruning. Instead, expand $f(X)^k$ in the falling-factorial basis:
  $$f(X)^k = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} j! \binom{f(X)}{j}.$$
  Now $\binom{f(X)}{j}$ has a direct **combinatorial interpretation**: it is the number of ways to choose a subset of $j$ edges from the minimal subtree spanning $X$!
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Maintain $dp[u][j]$ = number of pairs $(X_u, E_u)$ in the subtree of $u$ with $|E_u| = j \le \min(sz[u], k)$. By bounding $j \le \min(sz[u], k)$ at every merge step, pairs of vertices are LCA-merged at most once, dropping the tree DP complexity from $O(n k^2)$ to **$O(n k)$**!

##### Problem C4: Codeforces 1278F — Cards
- **Metadata**: Platform: Codeforces | ID: `1278F` | Title: *Cards* | Difficulty: 2400 | Tags: `Probabilities`, `Falling Factorials`, `Binomial Moments`.
- **Inline Problem Statement**: A deck has $m$ cards, one of which is a Joker. You shuffle the deck and look at the top card $n$ times ($n, m < 998244353$, $k \le 5000$ or $k \le 2 \cdot 10^5$). Let $X \sim \text{Binomial}(n, 1/m)$ be the number of times you see the Joker. Compute $\mathbb{E}[X^k] \bmod 998244353$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  The $j$-th **factorial moment** of $X = \sum_{r=1}^n I_r \sim \text{Binomial}(n, p)$ (with $p = 1/m$) is simply $\mathbb{E}[X^{\underline{j}}] = n^{\underline{j}} p^j$ because $X^{\underline{j}} = j! \sum_{|S|=j} \prod_{r \in S} I_r$!
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Writing $X^k = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} X^{\underline{j}}$ and taking expectation immediately gives:
  $$\mathbb{E}[X^k] = \sum_{j=0}^{\min(n, k)} \left\{\begin{matrix} k \\ j \end{matrix}\right\} n^{\underline{j}} m^{-j}.$$
  Computing the $k$-th row of Stirling numbers via $A(t) = \widehat{F}(t) e^{-t}$ takes $O(k \log k)$ time.

##### Problem C5: Luogu P6667 — 如何优雅地求和
- **Metadata**: Platform: Luogu | ID: `P6667` | Title: *如何优雅地求和* | Difficulty: 2500 (省选/NOI-) | Tags: `Point-Value EGF`, `Falling-Factorial Polynomial`.
- **Inline Problem Statement**: You are given $n \le 10^9$, $m \le 2 \times 10^4$, $x \in \mathbb{F}_{998244353}$, and the point values $F(0), F(1), \dots, F(m)$ of a degree-$m$ polynomial $F$. Compute
  $$\sum_{k=0}^n F(k) \binom{n}{k} x^k (1 - x)^{n-k} \pmod{998244353}.$$
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  Notice that we are **already given the point values $F(0), \dots, F(m)$** at $0, 1, \dots, m$! We do NOT need Lagrange interpolation to the monomial basis $x^j$ — we should go directly from point values to the falling-factorial basis $F(k) = \sum_{j=0}^m a_j k^{\underline{j}}$!
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  By the Fundamental Theorem of Falling-Factorial Polynomials, $A(t) = \widehat{F}(t) e^{-t} \bmod t^{m+1}$ where $\widehat{F}(t) = \sum_{i=0}^m \frac{F(i)}{i!} t^i$. A **single NTT convolution** of length $m+1$ produces $a_0, \dots, a_m$ in $O(m \log m)$ time, and since $(x + (1-x))^{n-j} = 1^{n-j} = 1$, the binomial sum simplifies to $\sum_{j=0}^m a_j n^{\underline{j}} x^j$ in $O(m)$ time!

---

#### Cluster D: Iteration 66 (Power-Sum / Subset-Product Logarithmic Derivatives & Newton's Identities)

##### Problem D1: Luogu P4705 — 玩游戏
- **Metadata**: Platform: Luogu | ID: `P4705` | Title: *玩游戏* | Difficulty: 2500 (省选/NOI-) | Tags: `Logarithmic Derivative`, `Power Sums`, `Subproduct Tree`, `EGF Convolution`.
- **Inline Problem Statement**: Given two integer arrays $a_1, \dots, a_n$ and $b_1, \dots, b_m$ ($n, m \le 10^5$) and an integer $t \le 10^5$, for every $k = 1, 2, \dots, t$, compute the expected value of $(a_i + b_j)^k$ when $i \in \{1, \dots, n\}$ and $j \in \{1, \dots, m\}$ are chosen uniformly and independently at random, modulo $998244353$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  By binomial expansion, $\sum_{i=1}^n \sum_{j=1}^m (a_i + b_j)^k = k! \sum_{r=0}^k \frac{p_r(A)}{r!} \frac{p_{k-r}(B)}{(k-r)!}$, where $p_r(A) = \sum_{i=1}^n a_i^r$ and $p_s(B) = \sum_{j=1}^m b_j^s$ are the **scalar power sums** of $A$ and $B$.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  This is the canonical **Regime B** logarithmic derivative problem: build $Q_A(x) = \prod_{i=1}^n (1 - a_i x)$ and $Q_B(x) = \prod_{j=1}^m (1 - b_j x)$ via divide-and-conquer subproduct trees in $O((n+m)\log^2(n+m))$ time, compute $P_A(x) = n - x \frac{Q_A'(x)}{Q_A(x)} \bmod x^{t+1}$ and $P_B(x) = m - x \frac{Q_B'(x)}{Q_B(x)} \bmod x^{t+1}$ in $O(t \log t)$ time, divide the $r$-th coefficient by $r!$, and multiply the two EGFs in $O(t \log t)$ time.

##### Problem D2: Luogu P4389 — 付公主的背包
- **Metadata**: Platform: Luogu | ID: `P4389` | Title: *付公主的背包* | Difficulty: 2400 (省选/NOI-) | Tags: `Euler Product`, `Harmonic Sieve`, `FPS ln / exp`.
- **Inline Problem Statement**: There are $n$ types of items ($n \le 10^5$) with volumes $v_1, v_2, \dots, v_n$ ($1 \le v_i \le m \le 10^5$), each available in infinite supply. For every target volume $s = 1, 2, \dots, m$, find the number of ways to fill a knapsack of volume $s$, modulo $998244353$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  Let $c_k = \#\{i : v_i = k\}$ be the multiplicity of volume $k$. The ordinary generating function is the Euler product $P(x) = \prod_{k=1}^m (1 - x^k)^{-c_k} \bmod x^{m+1}$.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  This is the canonical **Regime A** logarithmic derivative problem: taking $\ln P(x) = \sum_{k=1}^m c_k \sum_{j=1}^{\lfloor m/k \rfloor} \frac{x^{jk}}{j} \bmod x^{m+1}$ accumulates the logarithm array in $O(m \log m)$ time via the harmonic sieve, and a single call to $\exp(\ln P(x)) \bmod x^{m+1}$ outputs all $m$ answers in $O(m \log m)$ time.

##### Problem D3: LibreOJ #6503 — 「雅礼集训 2018 Day4」Magic
- **Metadata**: Platform: LibreOJ | ID: `6503` | Title: *「雅礼集训 2018 Day4」Magic* | Difficulty: 2500 | Tags: `Subproduct Tree`, `Symmetric Polynomials`, `Inclusion-Exclusion`.
- **Inline Problem Statement**: There are $m$ colors of cards with counts $a_1, a_2, \dots, a_m$ ($\sum_{i=1}^m a_i = n \le 10^5$) and a threshold $k$. Compute the number of permutations of all $n$ cards such that the total number of adjacent same-color pairs is at most $k$, modulo $998244353$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  By inclusion-exclusion (or EGF block decomposition) within each color $i$, splitting $a_i$ cards of color $i$ into $b_i$ monochromatic blocks gives a polynomial $P_i(x)$ of degree $a_i - 1$ describing the number of merged adjacent pairs. The total generating function is $\prod_{i=1}^m P_i(x)$ where $\sum_{i=1}^m \deg(P_i) = n - m \le 10^5$.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Combining all $m$ polynomials via a priority-queue Huffman/divide-and-conquer product tree runs in $O(n \log^2 n)$ time. Moreover, if all $a_i$ are grouped by distinct sizes (at most $O(\sqrt{n})$ distinct values since $\sum a_i = n$), raising each distinct $P_s(x)$ to its multiplicity $c_s$ via $\exp(c_s \ln P_s(x))$ reduces the work even further.

##### Problem D4: LibreOJ #6089 — 「2017 山东一轮集训 Day1」小 Y 的背包计数问题
- **Metadata**: Platform: LibreOJ | ID: `6089` | Title: *小 Y 的背包计数问题* | Difficulty: 2400 | Tags: `Bounded Knapsack`, `Euler Product`, `Harmonic Sieve`.
- **Inline Problem Statement**: You have a knapsack of capacity $n \le 10^5$ and $n$ types of items. The $i$-th type ($1 \le i \le n$) has weight $i$ and can be used at most $i$ times. For every total weight $1 \le s \le n$, count the number of valid multisets of weight $s$ modulo $23333333$ (or $998244353$ in the NTT version).
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  The generating function is $P(x) = \prod_{i=1}^n (1 + x^i + x^{2i} + \dots + x^{i^2}) = \prod_{i=1}^n \frac{1 - x^{i(i+1)}}{1 - x^i} \bmod x^{n+1}$.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Notice that $\frac{1 - x^{i(i+1)}}{1 - x^i}$ is a ratio of two Regime A factors! Taking the logarithm:
  $$\ln P(x) = \sum_{i=1}^n \ln(1 - x^{i(i+1)}) - \sum_{i=1}^n \ln(1 - x^i) \bmod x^{n+1}.$$
  Collecting the coefficients of $x^k$ in both products via the harmonic sieve and exponentiating solves the NTT-prime version in $O(n \log n)$ time (and for non-NTT prime $23333333$, splitting at $\sqrt{n}$ solves it in $O(n \sqrt{n})$).

##### Problem D5: Codeforces 1613F — Tree Coloring
- **Metadata**: Platform: Codeforces | ID: `1613F` | Title: *Tree Coloring* | Difficulty: 2500 | Tags: `Inclusion-Exclusion`, `Subproduct Tree / ln-exp`.
- **Inline Problem Statement**: Given a rooted tree on $n \le 2.5 \times 10^5$ vertices and $n$ colors, count the number of bijective vertex colorings $c: V \to \{1, \dots, n\}$ such that for every vertex $u$ except the root, $c(u) \neq c(\text{parent}(u)) - 1$, modulo $998244353$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  A violation at vertex $v$ links $c(\text{parent}(v)) \to c(v)$. Since each vertex $u$ can have at most one child $v$ violating the rule with $u$, choosing $k$ violations across the tree corresponds to picking at most one child at each vertex $u$ (in $deg_{\text{child}}(u)$ ways), which merges $n$ elements into $n - k$ chains:
  $$E(x) = \prod_{u=1}^n (1 + d_u x), \qquad \text{Answer} = \sum_{k=0}^{n-1} (-1)^k (n - k)! [x^k] E(x).$$
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Notice that $\sum_{u=1}^n d_u = n - 1$! We can either compute $\prod_{u=1}^n (1 + d_u x)$ via a subproduct tree in $O(n \log^2 n)$ time, OR group vertices by their distinct child degrees $d_u$ (there are at most $O(\sqrt{n})$ distinct values of $d_u$ since $\sum d_u = n - 1$) and accumulate $\ln E(x) = \sum_{d \ge 1} m_d \ln(1 + dx)$ to run in $O(n \log n)$ time!

---

#### Cluster E: Iteration 67 (Roots of Unity Filter, Floor Sums, and Cyclic Quotient Rings)

##### Problem E1: Luogu P5591 — 小猪佩奇学数学
- **Metadata**: Platform: Luogu | ID: `P5591` | Title: *小猪佩奇学数学* | Difficulty: 2500 (省选/NOI-) | Tags: `Roots of Unity Filter`, `Floor Sum`, `Binomial Theorem`.
- **Inline Problem Statement**: Given $n, p, k$ ($1 \le n, p < 998244353$, $k \in \{2^0, 2^1, \dots, 2^{20}\}$), compute
  $$\sum_{i=0}^n \binom{n}{i} p^i \left\lfloor \frac{i}{k} \right\rfloor \pmod{998244353}.$$
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  Rewrite $\left\lfloor \frac{i}{k} \right\rfloor = \frac{i - (i \bmod k)}{k}$. The first part $\frac{1}{k}\sum_{i=0}^n i \binom{n}{i} p^i = \frac{n p (1+p)^{n-1}}{k}$ is immediate. The second part requires evaluating $\sum_{r=0}^{k-1} r \sum_{i \equiv r \pmod k} \binom{n}{i} p^i$.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Applying the Roots of Unity Filter with $\omega_k = 3^{(998244353-1)/k} \bmod 998244353$ gives $\frac{1}{k}\sum_{j=0}^{k-1} (1 + p \omega_k^j)^n \sum_{r=0}^{k-1} r \omega_k^{-jr}$. Substituting the closed form $\sum_{r=0}^{k-1} r \omega_k^{-jr} = \frac{k}{\omega_k^{-j} - 1}$ for $j \neq 0$ (and $\frac{k(k-1)}{2}$ for $j = 0$) reduces the entire problem to $k$ modular exponentiations in **$O(k \log n)$ time**.

##### Problem E2: LibreOJ #6485 — LJJ 学二项式定理
- **Metadata**: Platform: LibreOJ | ID: `6485` | Title: *LJJ 学二项式定理* | Difficulty: 2200 | Tags: `Roots of Unity Filter`, `Mod-4 Filter`.
- **Inline Problem Statement**: Given $T \le 10^5$ test cases, each with $n \le 10^{18}$, $s \in \mathbb{F}_{998244353}$, and four weights $a_0, a_1, a_2, a_3$, compute
  $$\sum_{i=0}^n \binom{n}{i} s^i a_{i \bmod 4} \pmod{998244353}.$$
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  The sum decomposes into $\sum_{r=0}^3 a_r S_{r, 4}\bigl((1 + sx)^n\bigr)$.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Since $4 \mid (998244353 - 1)$, let $\omega_4 = 3^{(998244353-1)/4} \equiv 911660635 \pmod{998244353}$ be the primitive $4$-th root of unity. Then
  $$S_{r, 4} = \frac{1}{4} \sum_{j=0}^3 \omega_4^{-jr} (1 + s \omega_4^j)^n.$$
  Evaluating $(1 + s \omega_4^j)^n$ for $j = 0, 1, 2, 3$ takes $4$ binary exponentiations ($O(\log n)$ per query).

##### Problem E3: UOJ #450 — 「UNR #3」复读机
- **Metadata**: Platform: UOJ | ID: `450` | Title: *「UNR #3」复读机* | Difficulty: 2600 | Tags: `EGF`, `Roots of Unity Filter`, `Symmetry Compression`.
- **Inline Problem Statement**: Find the number of sequences of length $n \le 10^{18}$ over an alphabet of size $k \le 5 \times 10^5$ ($d \in \{1, 2, 3\}$) such that the multiplicity of **every** character is divisible by $d$, modulo $19491001$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  Note that the prime modulus is $p = 19491001$, and $p - 1 = 19491000$ is divisible by $3$ (so $\omega_3 = 7^{(p-1)/3} \bmod p$ exists in $\mathbb{F}_p$). The EGF for a single character having multiplicity divisible by $d$ is $E_{0, d}(x) = \frac{1}{d}\sum_{j=0}^{d-1} e^{\omega_d^j x}$, so the answer is $n! [x^n] E_{0, d}(x)^k$.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  For $d = 3$, expanding $\left(e^x + e^{\omega_3 x} + e^{\omega_3^2 x}\right)^k$ by the multinomial theorem gives:
  $$n! [x^n] E_{0, 3}(x)^k = \frac{1}{3^k} \sum_{a + b + c = k} \frac{k!}{a! b! c!} \bigl(a + b \omega_3 + c \omega_3^2\bigr)^n.$$
  Since $k \le 5 \times 10^5$, there are $\binom{k+2}{2} = O(k^2)$ triples $(a, b, c)$ if $d = 3$ and $k \le 2000$ (which matches the problem's subtask constraints: $k \le 5 \times 10^5$ for $d = 2$ and $k \le 2000$ for $d = 3$), solved in $O(k \log n)$ for $d=2$ and $O(k^2 \log n)$ for $d=3$!

##### Problem E4: AtCoder ABC267 Ex — Odd Sum
- **Metadata**: Platform: AtCoder | ID: `abc267_h` | Title: *Odd Sum* | Difficulty: 2400 | Tags: `Roots of Unity Filter`, `Parity Generating Function`, `Subproduct Tree`.
- **Inline Problem Statement**: Given $N \le 10^5$ integers $A_1, \dots, A_N \in \{1, \dots, 10\}$ and a target sum $M \le 10^6$, count the number of subsets of $\{1, \dots, N\}$ of **odd cardinality** whose elements sum to $M$, modulo $998244353$.
- **Bridge 1 (Combinatorial Modelling $\to$ Generating Function)**:
  Form the bivariate generating function $P(x, y) = \prod_{i=1}^N (1 + y x^{A_i})$, where $x$ tracks the subset sum and $y$ tracks the subset cardinality. We want $\sum_{k \equiv 1 \pmod 2} [x^M y^k] P(x, y)$.
- **Bridge 2 (Algebraic Reduction $\to$ Complexity)**:
  Apply the Roots of Unity Filter in $y$ with $k = 2$ and $\omega_2 = -1$:
  $$\sum_{k \text{ odd}} [x^M y^k] P(x, y) = [x^M] \frac{P(x, 1) - P(x, -1)}{2}.$$
  Grouping the $N$ items by their values $v \in \{1, \dots, 10\}$ (or multiplying via subproduct tree) computes $P(x, 1) = \prod_{v=1}^{10} (1 + x^v)^{c_v}$ and $P(x, -1) = \prod_{v=1}^{10} (1 - x^v)^{c_v}$ in $O(M \log M)$ time!
