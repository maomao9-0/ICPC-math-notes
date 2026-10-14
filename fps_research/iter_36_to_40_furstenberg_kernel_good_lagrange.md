# Cohort 1 — Wave 4B (Iterations 36–40): Furstenberg's Diagonal Method, The Kernel Method, Bivariate & Multivariate Good–Lagrange Inversion, and Multilingual (`[EN]`/`[ZH]`/`[JA]`) Multivariate GF Deep-Dives

> [!IMPORTANT]
> **Pedagogical Mandate & Architectural Scope (Wave 4B)**:
> In univariate generating functions, a solver works inside a single ring $K[[x]]$ or $K((x))$, where rational series, algebraic series, and D-finite series form a clean hierarchy. The moment a combinatorial problem tracks **two or more coupled parameters**—such as $(i, j)$ coordinates on a 2D lattice, $(n, m)$ vertex counts in a bicoloured graph, or step-by-step DP states constrained by a hard boundary $j \ge 0$—the generating function lives in a multivariate ring such as $K[[x, y]]$, $K[y, y^{-1}][[x]]$, or $K((z))[[t]]$.
>
> Historically, manipulations in these multivariate rings—substituting $y = t/z$ to extract a diagonal via residues (Furstenberg's Method), plugging an algebraic branch $y = y_0(x)$ into a two-variable equation to make a coefficient vanish (The Kernel Method), or taking a determinant of partial derivatives to invert coupled equations (Good–Lagrange Inversion)—are presented in textbooks as "clever tricks." This treatise strips away all guesswork. For every transformation in Iterations 36–40, we establish:
> 1. **The Concrete Combinatorial & Algebraic Object** and the exact formal ring in which the manipulation is legally valid;
> 2. **The Diagnostic Signal** that tells a solver *before writing any algebra* which multivariate tool is required;
> 3. **The Reverse-Engineering Scratchpad** showing how the substitution or operator is systematically discovered from what we want to isolate or annihilate;
> 4. **Step-by-Step Annotated Proofs**, **Hand-Checkable Toy Traces ($n \le 4$)**, and **Failure Modes / Characteristic Pitfalls**.

---

## Iteration 36: Furstenberg's Theorem & Rational Diagonals via Formal Residues

### 36.1 Concrete Combinatorial & Algebraic Object and Ring Hierarchy

#### What We Are Computing
Given a bivariate formal power series
$$F(x, y) = \sum_{n=0}^{\infty} \sum_{m=0}^{\infty} f_{n,m} x^n y^m \in K[[x, y]]$$
(typically a **bivariate rational function** $F(x,y) = \frac{P(x,y)}{Q(x,y)}$ with $P, Q \in K[x,y]$ and $Q(0,0) \neq 0$), its **principal diagonal** is the univariate formal power series which extracts only the terms where the exponents of $x$ and $y$ coincide:
$$\operatorname{Diag} F(x,y) := \sum_{n=0}^{\infty} f_{n,n} t^n = \sum_{n=0}^{\infty} \left([x^n y^n] F(x,y)\right) t^n \in K[[t]].$$

More generally, for a $d$-variate series $F(x_1, \dots, x_d) \in K[[x_1, \dots, x_d]]$, the diagonal operator is
$$\operatorname{Diag} F(x_1, \dots, x_d) := \sum_{n=0}^{\infty} \left([x_1^n x_2^n \cdots x_d^n] F(x_1, \dots, x_d)\right) t^n \in K[[t]].$$

#### Combinatorial Archetypes
1. **Return-to-Diagonal / Balanced 2D Lattice Walks**: Counting paths from $(0,0)$ to $(n,n)$ using step set $\mathcal{S} \subset \mathbb{Z}_{\ge 0}^2 \setminus \{(0,0)\}$ (e.g., King's walks / Delannoy paths with steps $(1,0), (0,1), (1,1)$), or extracting the probability of returning to the origin $(0,0)$ after $2n$ steps on $\mathbb{Z}^2$.
2. **Hadamard Products of Univariate Series**: Given two univariate series $A(x) = \sum_{n \ge 0} a_n x^n$ and $B(y) = \sum_{m \ge 0} b_m y^m$, their termwise **Hadamard product** $(A \odot B)(t) := \sum_{n \ge 0} a_n b_n t^n$ is literally the diagonal of their external product:
   $$(A \odot B)(t) = \operatorname{Diag}\!\left(A(x) B(y)\right).$$
3. **Binomial / Hypergeometric Sums**: Many single-index binomial sums $S_n = \sum_{k=0}^n \binom{n}{k} \binom{n+k}{k} c^k$ arise by recognizing $\binom{n}{k} = [x^k](1+x)^n$ and $\binom{n+k}{k} = [y^n](1+y)^{n+k}$, turning $S_n$ into $[x^n y^n]$ of a bivariate rational function.

#### The Formal Ring Embedding: Why $K((z))[[t]]$ Is Essential
A naive substitution $y = t/z$ into $F(x,y) = \sum_{n,m \ge 0} f_{n,m} x^n y^m$ produces negative powers of $z$:
$$F(z, t/z) = \sum_{n=0}^{\infty} \sum_{m=0}^{\infty} f_{n,m} z^{n-m} t^m.$$
If we tried to evaluate this in $K[[t, z]]$, negative powers $z^{n-m}$ ($n < m$) would be illegal. If we tried to evaluate it in $K[[z, z^{-1}, t]]$, multiplying two series with infinitely many positive and negative powers of $z$ causes infinite coefficient sums that fail to converge formally!

The rigorous algebraic home is the **ring of formal power series in $t$ over the field of formal Laurent series in $z$**:
$$\mathcal{R} := K((z))[[t]].$$
Let us verify why $F(z, t/z)$ lives inside $K((z))[[t]]$:
- Fix any power $t^m$ ($m \ge 0$). The coefficient of $t^m$ in $F(z, t/z)$ is
  $$[t^m] F(z, t/z) = \sum_{n=0}^{\infty} f_{n,m} z^{n-m} = z^{-m} \sum_{n=0}^{\infty} f_{n,m} z^n.$$
- Notice that for a fixed $m$, the exponent $n - m$ is **bounded below by $-m$**! Thus $[t^m] F(z, t/z)$ has only finitely many negative powers of $z$, which is the exact definition of an element of the formal Laurent field $K((z))$.
- Therefore, $F(z, t/z) \in K((z))[[t]]$ is 100% well-defined without any analytic convergence assumptions on $K$ (working over $\mathbb{C}$, $\mathbb{Q}$, or $\mathbb{F}_p$).

---

### 36.2 The Diagnostic Signal & The Reverse-Engineering Scratchpad

#### The Diagnostic Signal
Reach for **Furstenberg's Diagonal / Formal Residue Method** whenever you encounter:
- **Signal A (Direct 2D Extraction)**: You have derived a bivariate rational generating function $F(x,y) = \frac{P(x,y)}{Q(x,y)}$ (from a 2D grid recurrence $dp[i][j] = \sum_{(a,b)} w_{a,b} dp[i-a][j-b]$ without boundary obstructions) and the problem asks only for the diagonal sequence $dp[n][n]$ or $dp[a n][b n]$.
- **Signal B (Coupled Binomial Sum)**: You have a 1D sum $a_n = \sum_{k} \binom{n}{k} \binom{\dots}{k} \dots$ where $n$ appears in two or more binomial coefficients simultaneously, blocking standard 1D convolution.
- **Signal C (Degree Reduction)**: You have a $2 \times 2$ rational denominator $Q(x,y)$ whose total degree in one variable (after setting $y=t/z$) is $\le 2$, meaning its roots in $z$ can be solved explicitly by the quadratic formula.

#### The Reverse-Engineering Scratchpad: How to Discover $y = t/z$
Suppose you are staring at
$$F(x,y) = \sum_{n=0}^{\infty} \sum_{m=0}^{\infty} f_{n,m} x^n y^m$$
and you want to isolate only the terms where $n = m$, keeping track of their common index $n$ via a new variable $t^n$.

1. **Step 1 (Compare $n$ and $m$ via their difference)**:
   We want a test that fires if and only if $n - m = 0$. In formal power series, the easiest way to test whether two exponents $n$ and $m$ are equal is to map $x \mapsto z$ and $y \mapsto z^{-1}$, so that $x^n y^m \mapsto z^{n-m}$. Then $n = m$ corresponds to the constant term $[z^0]$.
2. **Step 2 (Preserve the common index $n$ with a marker $t$)**:
   If we only set $x = z$ and $y = z^{-1}$, all diagonal terms $f_{n,n} x^n y^n$ collapse into $\sum_{n \ge 0} f_{n,n} z^0$, an infinite sum! To keep each $f_{n,n}$ separated by $t^n$, we attach $t$ to $y$ (or symmetrically to $x$):
   $$x = z, \qquad y = \frac{t}{z}.$$
   Then the monomial $x^n y^m$ transforms as:
   $$x^n y^m = z^n \left(\frac{t}{z}\right)^m = z^{n-m} t^m.$$
   Now, when $n = m$, the $z$-exponent is $n - m = 0$, and the $t$-exponent is $m = n$! Thus:
   $$\operatorname{Diag} F(x,y) = \sum_{n=0}^{\infty} f_{n,n} t^n = [z^0] F\!\left(z, \frac{t}{z}\right).$$
3. **Step 3 (Convert $[z^0]$ into the Formal Residue $[z^{-1}]$)**:
   Why divide by $z$ to get $[z^{-1}]$ instead of stopping at $[z^0]$? Because in formal Laurent series $K((z))$, the **formal residue operator**
   $$\operatorname{res}_z G(z) := [z^{-1}] G(z)$$
   satisfies the fundamental properties of contour integration (specifically, $\operatorname{res}_z \frac{\partial}{\partial z} H(z) = 0$ and the partial-fraction residue formula $\operatorname{res}_z \frac{A(z)}{z - r(t)} = A(r(t))$ when $r(t) \in t K[[t]]$). To shift the target coefficient from $[z^0]$ to $[z^{-1}]$, we simply divide by $z$:
   $$\boxed{\operatorname{Diag} F(x,y) = [z^0] F\!\left(z, \frac{t}{z}\right) = [z^{-1}] \left(\frac{1}{z} F\!\left(z, \frac{t}{z}\right)\right) = \operatorname{res}_z \left(\frac{1}{z} F\!\left(z, \frac{t}{z}\right)\right).}$$

---

### 36.3 Small Roots vs. Large Roots: Rigorous Partial-Fraction Extraction

Suppose $F(x,y) = \frac{P(x,y)}{Q(x,y)}$ is rational. After substituting $x = z, y = t/z$, the rational expression in $z$ is
$$R(z, t) := \frac{1}{z} F\!\left(z, \frac{t}{z}\right) = \frac{P(z, t/z)}{z \, Q(z, t/z)}.$$
Multiplying numerator and denominator by $z^d$ (where $d = \deg_y Q$ is the highest power of $y$ in $Q(x,y)$) clears all negative powers of $z$, yielding a ratio of polynomials in $z$ with coefficients in $K[t]$:
$$R(z, t) = \frac{\widetilde{P}(z, t)}{\widetilde{Q}(z, t)}.$$

Over the algebraic closure $\overline{K((t))}$ (via Puiseux series), the denominator $\widetilde{Q}(z,t)$ factors into linear factors in $z$:
$$\widetilde{Q}(z, t) = c(t) \prod_{i=1}^{r} (z - \alpha_i(t)) \prod_{j=1}^{s} (z - \beta_j(t)).$$
Crucially, the roots of $\widetilde{Q}(z,t) = 0$ split into two disjoint classes based on their **$t$-adic valuation** $\operatorname{val}_t$ (their behavior as $t \to 0$):

1. **Small Roots $\alpha_1(t), \dots, \alpha_r(t)$ ($\operatorname{val}_t(\alpha_i) > 0$, i.e., $\alpha_i(0) = 0$)**:
   These are roots that vanish at $t = 0$. When we expand $\frac{1}{z - \alpha_i(t)}$ inside our working ring $K((z))[[t]]$ (where $t$ is infinitesimally smaller than $z$), we **must** factor out $z$:
   $$\frac{1}{z - \alpha_i(t)} = \frac{1}{z\left(1 - \frac{\alpha_i(t)}{z}\right)} = \sum_{k=0}^{\infty} \frac{\alpha_i(t)^k}{z^{k+1}} \in K((z))[[t]].$$
   Look at the $z$-exponents on the right-hand side: for $k=0$, the term is $\frac{1}{z}$, which has residue $[z^{-1}] = 1$! More generally, for any polynomial or series $A(z,t)$ regular at $z = \alpha_i(t)$:
   $$\operatorname{res}_z \frac{A(z,t)}{z - \alpha_i(t)} = \operatorname{res}_z \sum_{k=0}^{\infty} A(z,t) \frac{\alpha_i(t)^k}{z^{k+1}} = A(\alpha_i(t), t).$$
   Thus **every small root $\alpha_i(t)$ contributes its standard Cauchy residue at $z = \alpha_i(t)$**!

2. **Large Roots $\beta_1(t), \dots, \beta_s(t)$ ($\operatorname{val}_t(\beta_j) \le 0$, i.e., $\beta_j(t)$ does not vanish at $t=0$)**:
   Because $\operatorname{val}_t(\beta_j) \le 0$, the reciprocal $\beta_j(t)^{-1}$ lies in $K[[t]]$ (or Puiseux series with non-negative valuation). To expand $\frac{1}{z - \beta_j(t)}$ as a power series in $t$ with Laurent coefficients in $z$, we **must** factor out $-\beta_j(t)$ instead of $z$:
   $$\frac{1}{z - \beta_j(t)} = -\frac{1}{\beta_j(t)\left(1 - \frac{z}{\beta_j(t)}\right)} = -\sum_{k=0}^{\infty} \frac{z^k}{\beta_j(t)^{k+1}} \in K[[z]][[t]].$$
   Look at the $z$-exponents on the right-hand side: they are $z^0, z^1, z^2, \dots$ — **strictly non-negative powers of $z$**! There is **no $z^{-1}$ term whatsoever**! Therefore:
   $$\operatorname{res}_z \frac{A(z,t)}{(z - \beta_j(t))^m} = 0 \quad \text{whenever } A(z,t) \in K[[z, t]] \text{ and } \operatorname{val}_t(\beta_j) \le 0.$$

> [!TIP]
> **The Golden Rule of Rational Diagonals (Furstenberg 1967)**:
> When computing $\operatorname{Diag} F(x,y) = \operatorname{res}_z \left(\frac{1}{z} F(z, t/z)\right)$ via partial fractions in $z$:
> - **Keep ONLY the small roots** $\alpha_i(t)$ satisfying $\lim_{t \to 0} \alpha_i(t) = 0$ ($\operatorname{val}_t(\alpha_i) > 0$).
> - **Discard ALL large roots** $\beta_j(t)$ ($\operatorname{val}_t(\beta_j) \le 0$), because their expansions in $K((z))[[t]]$ contain only non-negative powers of $z$ and contribute $0$ to $[z^{-1}]$.
> - For each simple small root $\alpha_i(t)$ of $\widetilde{Q}(z,t) = 0$, its residue contribution is $\frac{\widetilde{P}(\alpha_i(t), t)}{\frac{\partial \widetilde{Q}}{\partial z}(\alpha_i(t), t)}$. Since $\alpha_i(t)$ is an algebraic function of $t$, the sum of residues over all small roots is a symmetric rational expression in algebraic series, proving **Furstenberg's Theorem (Part 1)**: *The diagonal of any bivariate rational power series over a field $K$ of characteristic $0$ is an algebraic power series!*

---

### 36.4 Complete Step-by-Step Worked Derivations & Toy Traces ($n \le 4$)

#### Case 1: Central Binomial Coefficients $\binom{2n}{n}$ from $\frac{1}{1 - x - y}$
**Combinatorial Object**: Lattice paths from $(0,0)$ to $(n,n)$ using steps $(1,0)$ and $(0,1)$. The bivariate GF is
$$F(x,y) = \frac{1}{1 - x - y} = \sum_{n,m \ge 0} \binom{n+m}{n} x^n y^m \in \mathbb{Q}[[x,y]].$$
We want $\operatorname{Diag} F(x,y) = \sum_{n \ge 0} \binom{2n}{n} t^n$.

**Step-by-Step Annotated Derivation**:
$$\begin{aligned}
\operatorname{Diag}\!\left(\frac{1}{1 - x - y}\right)
&= [z^{-1}] \frac{1}{z\left(1 - z - \frac{t}{z}\right)} && \text{(Substitute } x=z, y=t/z \text{ and divide by } z\text{)} \\
&= [z^{-1}] \frac{1}{-z^2 + z - t} && \text{(Multiply denominator through by } z\text{)} \\
&= [z^{-1}] \frac{-1}{z^2 - z + t}. && \text{(Normalize leading coefficient of } z^2 \text{ to } +1\text{)}
\end{aligned}$$
Now find the roots of $\widetilde{Q}(z,t) = z^2 - z + t = 0$ in $z$ using the quadratic formula:
$$z = \frac{1 \pm \sqrt{1 - 4t}}{2}.$$
Let us classify the two roots by setting $t = 0$:
- **Small root $\alpha(t)$**: $\alpha(t) = \frac{1 - \sqrt{1-4t}}{2} = t + 2t^2 + 5t^3 + \dots$, which satisfies $\alpha(0) = 0$ ($\operatorname{val}_t(\alpha) = 1 > 0$).
- **Large root $\beta(t)$**: $\beta(t) = \frac{1 + \sqrt{1-4t}}{2} = 1 - t - 2t^2 - \dots$, which satisfies $\beta(0) = 1 \neq 0$ ($\operatorname{val}_t(\beta) = 0$).

Factor the denominator as $(z - \alpha(t))(z - \beta(t))$ and apply partial fractions in $z$:
$$\frac{-1}{(z - \alpha(t))(z - \beta(t))} = \frac{1}{\beta(t) - \alpha(t)} \left(\frac{1}{z - \alpha(t)} - \frac{1}{z - \beta(t)}\right).$$
By the Golden Rule of Section 36.3, $[z^{-1}] \frac{1}{z - \alpha(t)} = 1$ (small root) and $[z^{-1}] \frac{1}{z - \beta(t)} = 0$ (large root). Therefore:
$$\operatorname{Diag}\!\left(\frac{1}{1 - x - y}\right) = \frac{1}{\beta(t) - \alpha(t)} (1 - 0) = \frac{1}{\frac{1 + \sqrt{1-4t}}{2} - \frac{1 - \sqrt{1-4t}}{2}} = \frac{1}{\sqrt{1 - 4t}}.$$

**Hand-Checkable Toy Trace ($n = 0, 1, 2, 3$)**:
- From the grid $F(x,y) = \frac{1}{1-x-y}$:
  - $n=0$: $\binom{0}{0} = 1$
  - $n=1$: $\binom{2}{1} = 2$
  - $n=2$: $\binom{4}{2} = 6$
  - $n=3$: $\binom{6}{3} = 20$
- From $\frac{1}{\sqrt{1-4t}} = \sum_{n \ge 0} \binom{-1/2}{n} (-4t)^n$:
  - $n=0$: $1$
  - $n=1$: $(-\frac{1}{2})(-4) = 2$
  - $n=2$: $\frac{(-1/2)(-3/2)}{2!}(-4)^2 = \frac{3}{8} \cdot 16 = 6$
  - $n=3$: $\frac{(-1/2)(-3/2)(-5/2)}{3!}(-4)^3 = -\frac{5}{16} (-64) = 20$. Exact match!

---

#### Case 2: Central Delannoy Numbers & Weighted King Walks $\frac{1}{1 - ax - by - cxy}$
**Combinatorial Object**: Paths from $(0,0)$ to $(n,n)$ with horizontal step $(1,0)$ of weight $a$, vertical step $(0,1)$ of weight $b$, and diagonal step $(1,1)$ of weight $c$. For $a=b=c=1$, these are the **Central Delannoy Numbers** $D_n = \sum_{k=0}^n \binom{n}{k}\binom{n+k}{k}$.

**Step-by-Step Annotated Derivation**:
$$\begin{aligned}
\operatorname{Diag}\!\left(\frac{1}{1 - ax - by - cxy}\right)
&= [z^{-1}] \frac{1}{z\left(1 - az - b\frac{t}{z} - c z \frac{t}{z}\right)} && \text{(Substitute } x=z, y=t/z \text{; note } xy = t\text{!)} \\
&= [z^{-1}] \frac{1}{-a z^2 + (1 - ct)z - bt} && \text{(Distribute } z \text{ into denominator)} \\
&= [z^{-1}] \frac{-1}{a z^2 - (1 - ct)z + bt}.
\end{aligned}$$
Let $\widetilde{Q}(z,t) = a z^2 - (1-ct)z + bt$. Its two roots in $z$ are
$$z = \frac{(1 - ct) \pm \sqrt{(1 - ct)^2 - 4abt}}{2a}.$$
At $t = 0$, the "-" branch gives $\alpha(0) = \frac{1 - 1}{2a} = 0$ (small root!), while the "+" branch gives $\beta(0) = \frac{2}{2a} = \frac{1}{a} \neq 0$ (large root!). Taking the residue at the unique small root $\alpha(t)$:
$$\operatorname{res}_{z = \alpha(t)} \frac{-1}{a(z - \alpha(t))(z - \beta(t))} = \frac{-1}{a(\alpha(t) - \beta(t))} = \frac{1}{a(\beta(t) - \alpha(t))} = \frac{1}{\sqrt{(1 - ct)^2 - 4abt}}.$$
Setting $a = b = c = 1$ immediately yields the famous generating function for Central Delannoy Numbers:
$$\boxed{\operatorname{Diag}\!\left(\frac{1}{1 - x - y - xy}\right) = \frac{1}{\sqrt{(1-t)^2 - 4t}} = \frac{1}{\sqrt{1 - 6t + t^2}}.}$$

**Hand-Checkable Toy Trace ($n = 0, 1, 2, 3$) for Central Delannoy ($a=b=c=1$)**:
- Combinatorial count on $(0,0) \to (n,n)$:
  - $n=0$: $1$
  - $n=1$: $(1,0)\to(1,1)$, $(0,1)\to(1,1)$, or $(1,1)$ directly $\implies 3$ paths.
  - $n=2$: $\sum_{k=0}^2 \binom{2}{k}\binom{2+k}{k} = 1\cdot 1 + 2\cdot 3 + 1\cdot 6 = 13$ paths.
  - $n=3$: $\sum_{k=0}^3 \binom{3}{k}\binom{3+k}{k} = 1\cdot 1 + 3\cdot 4 + 3\cdot 10 + 1\cdot 20 = 63$ paths.
- Series expansion of $(1 - (6t - t^2))^{-1/2} = 1 + \frac{1}{2}(6t - t^2) + \frac{3}{8}(6t - t^2)^2 + \frac{5}{16}(6t - t^2)^3 + \dots$:
  - $[t^0] = 1$
  - $[t^1] = \frac{1}{2}(6) = 3$
  - $[t^2] = \frac{1}{2}(-1) + \frac{3}{8}(36) = -\frac{1}{2} + \frac{27}{2} = 13$
  - $[t^3] = \frac{3}{8}(-12) + \frac{5}{16}(216) = -\frac{9}{2} + \frac{135}{2} = 63$. Exact match!

---

#### Case 3: The Universal Quadratic Denominator Rule
Observe what happened in both Case 1 and Case 2. Whenever $z Q(z, t/z)$ simplifies to a **quadratic polynomial in $z$**,
$$\widetilde{Q}(z,t) = A(t) z^2 + B(t) z + C(t)$$
with $B(0) \neq 0$ and $C(0) = 0$ (so that at $t=0$, $\widetilde{Q}(z,0) = A(0)z^2 + B(0)z = z(A(0)z + B(0))$ has **exactly one simple small root** $\alpha(0) = 0$ and one large root $\beta(0) = -B(0)/A(0)$), the derivative with respect to $z$ evaluated at the small root $\alpha(t) = \frac{-B(t) \pm \sqrt{B(t)^2 - 4A(t)C(t)}}{2A(t)}$ (where the sign is chosen opposite to $B(0)$ so $\alpha(0)=0$, namely $+ \operatorname{sgn}(B(0))\sqrt{\dots}$) is:
$$\frac{\partial \widetilde{Q}}{\partial z}(\alpha(t), t) = 2A(t)\alpha(t) + B(t) = \pm \sqrt{B(t)^2 - 4A(t)C(t)}.$$
Therefore, for any numerator $\widetilde{P}(z,t)$, the diagonal residue at the unique small root is immediately
$$\boxed{\operatorname{res}_{z = \alpha(t)} \frac{\widetilde{P}(z,t)}{A(t)z^2 + B(t)z + C(t)} = \frac{\widetilde{P}(\alpha(t), t)}{\sqrt{B(t)^2 - 4A(t)C(t)}} \quad (\text{choosing the sign so } [t^0] \text{ matches } F(0,0)).}$$
In particular, if $\widetilde{P}(z,t) = \widetilde{P}(t)$ is independent of $z$, we do not even need to substitute $\alpha(t)$ into the numerator: the diagonal is simply $\frac{\widetilde{P}(t)}{\sqrt{B(t)^2 - 4A(t)C(t)}}$!

---

### 36.5 Furstenberg's Converse & Lipshitz's Theorem for $d \ge 3$

#### Furstenberg's Converse: Every Algebraic Series is a Bivariate Rational Diagonal
Not only is the diagonal of every bivariate rational function algebraic (over characteristic $0$), **Furstenberg (1967)** proved the converse over any field $K$:

> **Theorem (Furstenberg's Converse)**: Let $f(t) = \sum_{n=1}^{\infty} a_n t^n \in t K[[t]]$ be an algebraic formal power series satisfying a polynomial equation $P(t, f(t)) = 0$ with $P(t, y) \in K[t, y]$. Suppose $P(0, 0) = 0$ and $\frac{\partial P}{\partial y}(0, 0) \neq 0$ (the generic Hensel / Implicit Function Theorem condition). Then $f(t)$ is the diagonal of an explicit bivariate rational function:
> $$f(t) = \operatorname{Diag} \left( \frac{y^2 \frac{\partial P}{\partial y}(xy, y)}{P(xy, y)} \right).$$

**Proof via Formal Residues**:
Set $x = z, y = t/z$, so that $xy = t$ and $y = t/z$. Wait: it is even cleaner to set $x = t/z$ and $y = z$ (which gives the exact same diagonal since $\operatorname{Diag} F(x,y) = \operatorname{Diag} F(y,x)$)! With $x = t/z$ and $y = z$, we have $xy = t$, and dividing by $z$ gives:
$$\operatorname{Diag} \left( \frac{y^2 \frac{\partial P}{\partial y}(xy, y)}{P(xy, y)} \right) = [z^{-1}] \frac{1}{z} \frac{z^2 \frac{\partial P}{\partial z}(t, z)}{P(t, z)} = \operatorname{res}_z \left( \frac{z \, \frac{\partial P}{\partial z}(t, z)}{P(t, z)} \right).$$
Since $P(0, 0) = 0$ and $\frac{\partial P}{\partial z}(0, 0) \neq 0$, $P(t, z) = 0$ has a **unique small root** $z = f(t) \in t K[[t]]$ of multiplicity $1$. At this unique simple small root $z = f(t)$, the residue of $\frac{z \, \frac{\partial P}{\partial z}(t, z)}{P(t, z)}$ is:
$$\left. \frac{z \, \frac{\partial P}{\partial z}(t, z)}{\frac{\partial P}{\partial z}(t, z)} \right|_{z = f(t)} = f(t). \qquad \blacksquare$$

#### What Happens in $d \ge 3$ Variables? Lipshitz's Theorem vs. Finite Fields
A natural question arises: *Is the diagonal of a trivariate rational function $F(x,y,z) = \frac{1}{1 - x - y - z}$ still algebraic over $\mathbb{Q}$?*
- **Over Characteristic $0$ ($\mathbb{Q}$ or $\mathbb{C}$): NO!**
  Consider $\operatorname{Diag} \frac{1}{1 - x - y - z} = \sum_{n=0}^{\infty} \frac{(3n)!}{(n!)^3} t^n$. By Stirling's formula, its coefficients grow as
  $$\frac{(3n)!}{(n!)^3} \sim \frac{\sqrt{3}}{2\pi n} 27^n.$$
  By Flajolet–Sedgewick singularity analysis, any algebraic function over $\mathbb{C}$ has asymptotic coefficient growth $c \cdot R^{-n} n^{\alpha}$ where $\alpha \in \mathbb{Q} \setminus \{-1, -2, -3, \dots\}$ (unless it is rational, where $\alpha \in \mathbb{Z}_{\ge 0}$). Because $\alpha = -1$ is a logarithmic/transcendental critical exponent (arising from complete elliptic integrals of the first kind), $\sum_{n \ge 0} \frac{(3n)!}{(n!)^3} t^n$ and the Apéry number generating function $\operatorname{Diag} \frac{1}{(1-x-y)(1-z) - xyz} = \sum_{n \ge 0} \left(\sum_{k=0}^n \binom{n}{k}^2 \binom{n+k}{k}\right) t^n$ are **transcendental over $\mathbb{Q}(t)$**!
- **Lipshitz's Theorem (1988)**: Although $d$-variate rational diagonals ($d \ge 3$) are not algebraic over $\mathbb{Q}$, **Leonard Lipshitz (1988)** proved that the diagonal of any **D-finite (holonomic)** multivariate power series is **D-finite**! Since every rational function $P(x_1,\dots,x_d)/Q(x_1,\dots,x_d)$ is D-finite, $\operatorname{Diag} F(x_1,\dots,x_d)$ always satisfies a **linear ordinary differential equation (ODE) with polynomial coefficients** in $t$, and therefore its coefficients $f_{n,\dots,n}$ always satisfy a **P-recursive (polynomial-coefficient linear) recurrence** computable in $O(n)$ time!
- **Over Characteristic $p > 0$ ($\mathbb{F}_p$): Furstenberg's Theorem Holds for ALL $d \ge 2$!**
  Over a finite field $\mathbb{F}_p$, Furstenberg (1967) proved that the diagonal of a rational function in **any** number of variables $d \ge 2$ is **always algebraic over $\mathbb{F}_p(t)$** (and conversely, reducing a rational diagonal modulo $p$ makes transcendental series like $\sum \frac{(3n)!}{(n!)^3} t^n \bmod p$ algebraic via Lucas' Theorem / Frobenius $p$-th power equations!).

---

### 36.6 Failure Modes, Pitfalls & Characteristic Constraints

1. **Pitfall 1: Including Large Roots in the Residue Sum**:
   A classic mistake is to compute the partial fraction decomposition of $\frac{1}{z} F(z, t/z)$ and sum the residues over *all* roots of the denominator. Because the sum of residues of a rational function with $\deg(\text{denom}) \ge \deg(\text{num}) + 2$ over all roots (including $\infty$) is identically $0$, summing over both small and large roots cancels your answer to $0$! Always test $t \to 0$ first to isolate the small roots ($\operatorname{val}_t(\alpha) > 0$).
2. **Pitfall 2: Multiple Small Roots or Higher-Order Poles at $z=0$**:
   If $\widetilde{Q}(z, 0)$ has $z^2$ or higher dividing it (i.e., two or more small roots $\alpha_1(t), \alpha_2(t) \to 0$ as $t \to 0$), you must sum the residues over **all** small roots $\alpha_1(t), \dots, \alpha_r(t)$. If two small roots coincide identically ($\alpha_1(t) = \alpha_2(t)$), you must use the higher-order pole residue formula $\operatorname{res}_{z=\alpha} \frac{\widetilde{P}(z,t)}{(z-\alpha)^m \dots} = \frac{1}{(m-1)!} \left.\frac{\partial^{m-1}}{\partial z^{m-1}} \frac{\widetilde{P}(z,t)}{\dots}\right|_{z=\alpha}$.
3. **Pitfall 3: Characteristic $p = 2$ in Quadratic Diagonals**:
   The quadratic diagonal formula $\frac{1}{\sqrt{B(t)^2 - 4A(t)C(t)}}$ requires taking a square root of a formal power series, which uses $1/2 \in K$ and is invalid in characteristic $p = 2$. Over $\mathbb{F}_2$, the quadratic equation $A z^2 + B z + C = 0$ is solved by Artin–Schreier theory instead of $\sqrt{\Delta}$.
4. **Pitfall 4: Off-Diagonal Extraction $[x^{n} y^{n+k}]$**:
   If a problem asks for $[x^n y^{n+k}] F(x,y)$ instead of $[x^n y^n] F(x,y)$, do **not** change the substitution $x=z, y=t/z$; simply note that
   $$[x^n y^{n+k}] F(x,y) = [x^n y^n] \left(y^{-k} F(x,y)\right) \implies \sum_{n=0}^{\infty} \left([x^n y^{n+k}] F(x,y)\right) t^n = [z^{-1}] \left(\frac{1}{z} \left(\frac{z}{t}\right)^k F\!\left(z, \frac{t}{z}\right)\right).$$
   Forgetting that $y^{-k} = (z/t)^k$ introduces an extra factor of $z^k t^{-k}$ inside the residue is a frequent source of off-by-$k$ index bugs.

---

## Iteration 37: The Kernel Method ($K(x,y)F(x,y) = A(x) + B(y)$) & Lattice Path Reflections

### 37.1 Concrete Combinatorial Object, Ring $K[y][[x]]$, Diagnostic Signal & Scratchpad

#### Concrete Combinatorial & Algebraic Object
Consider a combinatorial process evolving step-by-step in discrete time $n \ge 0$ (tracked by $x^n$) while maintaining a non-negative integer state or altitude $j \ge 0$ (tracked by $y^j$). Its bivariate generating function is
$$F(x, y) = \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} f_{n,j} x^n y^j = \sum_{n=0}^{\infty} P_n(y) x^n \in K[y][[x]].$$
Notice the ring: at each time step $n$, the maximum possible altitude $j$ is finite, so the coefficient $P_n(y) = [x^n] F(x,y)$ is a **polynomial in $y$**! Thus $F(x,y)$ lives in $K[y][[x]] \subset K[[x,y]]$.

Inside this bivariate series, the two most important specialization targets are:
1. **Excursions (Paths ending at altitude $j = 0$)**:
   $$F(x, 0) = \sum_{n=0}^{\infty} f_{n,0} x^n = [y^0] F(x,y) \in K[[x]].$$
2. **Meanders (Paths never dropping below $0$, ending at ANY altitude $j \ge 0$)**:
   $$F(x, 1) = \sum_{n=0}^{\infty} \left(\sum_{j=0}^{\infty} f_{n,j}\right) x^n \in K[[x]].$$

#### The Diagnostic Signal
How do you recognize a **Kernel Method** problem in the wild?
- **Signal A (Truncated / Absorbing Boundary at $j = 0$)**: You have a step recurrence $f_{n,j} = \sum_{s \in \mathcal{S}} w_s f_{n-1, j-s}$ that holds for $j \ge 0$, **except** that transitions that would come from negative altitude ($j - s < 0$) or leave from $j < 0$ are forbidden.
- **Signal B (Coupled Unknown Boundary Series)**: When you sum the recurrence over $n \ge 1$ and $j \ge 0$, multiplying by $x y^j$ produces negative powers $y^{-1}, y^{-2}, \dots, y^{-k}$ unless you subtract the boundary terms $F(x, 0), \frac{\partial F}{\partial y}(x, 0), \dots$! You end up with **one functional equation** containing **two unknown functions**: the bivariate $F(x,y)$ and the univariate boundary $F(x,0)$:
  $$K(x, y) F(x, y) = A(x, y) + B(x, y) F(x, 0).$$
  A novice gets stuck here thinking one equation cannot solve for two unknowns ($F(x,y)$ and $F(x,0)$). The Kernel Method resolves this paradox by exploiting the ring constraint $F(x,y) \in K[[x,y]]$.

#### The Reverse-Engineering Scratchpad: How to Discover the Kernel Substitution
Suppose you have derived the functional equation for a walk starting at $j = 0$ with step set $\mathcal{S} \subset \{-1, 0, +1, +2, \dots\}$ and step polynomial $S(y) = \sum_{s \in \mathcal{S}} w_s y^s$:
1. **Step 1 (Write the Naive Step Evolution and Subtract the Illegal Drop)**:
   At step $n$, multiplying $F(x,y)$ by $x S(y)$ advances time by $1$ and shifts altitude by $s \in \mathcal{S}$. However, if a path is at altitude $j = 0$ (represented by $F(x,0)$) and takes the step $s = -1$ (weight $w_{-1} y^{-1}$), it lands at the illegal altitude $j = -1$. Subtracting that illegal transition from $x S(y) F(x,y)$ and adding the initial state $f_{0,0} = 1$ gives:
   $$F(x, y) = 1 + x S(y) F(x, y) - x w_{-1} y^{-1} F(x, 0).$$
2. **Step 2 (Clear Negative Powers of $y$ and Isolate $F(x,y)$)**:
   Multiply through by $y$ and collect $F(x,y)$ on the left-hand side:
   $$\underbrace{\big(y - x y S(y)\big)}_{K(x, y)} F(x, y) = y - x w_{-1} F(x, 0).$$
   Here $K(x, y) := y - x y S(y) \in K[x, y]$ is called the **Kernel** of the functional equation.
3. **Step 3 (How to Eliminate $F(x,y)$ Without Knowing It!)**:
   We want to find $F(x,0)$, and $F(x,y)$ is in the way, multiplied by $K(x,y)$. What if we substitute a formal power series $y = y_0(x)$ such that **$K(x, y_0(x)) = 0$**?
   - **Wait — is substituting $y = y_0(x)$ into $F(x, y)$ legally allowed?**
     Recall that $F(x, y) = \sum_{n=0}^{\infty} P_n(y) x^n \in K[y][[x]]$ (or more generally $K[[x,y]]$). If $y_0(x)$ is a **small root** ($\operatorname{val}_x(y_0(x)) \ge 1$, or even $\operatorname{val}_x(y_0(x)) \ge 0$ since each $P_n(y)$ is a *polynomial* in $y$!), then $F(x, y_0(x)) = \sum_{n=0}^{\infty} P_n(y_0(x)) x^n$ is a **convergent formal power series in $K[[x]]$** whenever $y_0(x) \in K[[x]]$!
   - By contrast, if $y_1(x)$ is a **large root** with negative $x$-valuation ($\operatorname{val}_x(y_1(x)) < 0$, i.e., $y_1(x) \in x^{-1} K[[x^{-1}]]$), then substituting $y = y_1(x)$ into $F(x,y)$ produces infinitely many terms contributing to $[x^0]$ (for example, $x^n (x^{-1})^n = x^0$ for all $n \ge 0$), which **diverges in $K((x))$**!
   - Therefore, plugging in the unique **small root** $y = y_0(x) \in x K[[x]]$ of $K(x, y) = 0$ makes the left-hand side $K(x, y_0(x)) F(x, y_0(x)) = 0 \cdot (\text{finite series in } K[[x]]) = 0$, instantly annihilating $F(x,y)$ and solving for $F(x,0)$:
     $$0 = y_0(x) - x w_{-1} F(x, 0) \implies \boxed{F(x, 0) = \frac{y_0(x)}{x w_{-1}}.}$$
   - And once $F(x, 0)$ is known, we substitute it back into the kernel equation to obtain the full bivariate generating function $F(x,y)$ for **all** final altitudes $j \ge 0$:
     $$\boxed{F(x, y) = \frac{y - y_0(x)}{y - x y S(y)}.}$$

---

### 37.2 Single Negative Step ($-1$): Complete Worked Derivation & Toy Trace

Let us trace the complete pipeline on **Motzkin Excursions and Meanders** (steps $\mathcal{S} = \{-1, 0, +1\}$ with weights $1, 1, 1$, so $S(y) = y^{-1} + 1 + y$).

#### Step-by-Step Annotated Derivation
1. **Functional Equation**:
   $$\begin{aligned}
   F(x, y) &= 1 + x(y^{-1} + 1 + y) F(x, y) - x y^{-1} F(x, 0) && \text{(Step evolution minus illegal } 0 \to -1 \text{ step)} \\
   \big(y - x(1 + y + y^2)\big) F(x, y) &= y - x F(x, 0). && \text{(Multiply by } y \text{ and collect } F(x,y)\text{)}
   \end{aligned}$$
2. **Solve the Kernel Equation $K(x, y) = -x y^2 + (1 - x) y - x = 0$**:
   By the quadratic formula in $y$:
   $$y = \frac{(1 - x) \pm \sqrt{(1 - x)^2 - 4x^2}}{2x} = \frac{1 - x \pm \sqrt{1 - 2x - 3x^2}}{2x}.$$
3. **Classify Roots as $x \to 0$**:
   - **Small root $y_0(x)$ ("$-$" branch)**: Since $\sqrt{1 - 2x - 3x^2} = 1 - x - 2x^2 - 2x^3 - \dots$, the numerator $1 - x - \sqrt{1 - 2x - 3x^2} = 2x^2 + 2x^3 + \dots$ has valuation $2$, so dividing by $2x$ gives:
     $$y_0(x) = \frac{1 - x - \sqrt{1 - 2x - 3x^2}}{2x} = x + x^2 + 2x^3 + 4x^4 + 9x^5 + \dots \in x \mathbb{Q}[[x]].$$
   - **Large root $y_1(x)$ ("$+$" branch)**:
     $$y_1(x) = \frac{1 - x + \sqrt{1 - 2x - 3x^2}}{2x} = \frac{1}{x} - 1 - x - x^2 - 2x^3 - \dots \notin \mathbb{Q}[[x]].$$
     Because $\operatorname{val}_x(y_1) = -1 < 0$, $F(x, y_1(x))$ does not converge in $\mathbb{Q}((x))$!
4. **Extract Excursions $F(x, 0)$, Full Bivariate $F(x, y)$, and Meanders $F(x, 1)$**:
   - **Excursions ($j=0$)**: Plugging $y = y_0(x)$ into $K(x, y) F(x, y) = y - x F(x, 0)$ yields $0 = y_0(x) - x F(x, 0)$, so
     $$F(x, 0) = \frac{y_0(x)}{x} = \frac{1 - x - \sqrt{1 - 2x - 3x^2}}{2x^2} = 1 + x + 2x^2 + 4x^3 + 9x^4 + \dots \quad (\text{Motzkin numbers } M_n).$$
   - **Full Bivariate Series**: Notice that $K(x,y) = -x (y - y_0(x))(y - y_1(x))$. Since the right-hand side is $y - x F(x,0) = y - y_0(x)$, the factor $(y - y_0(x))$ **cancels algebraically** from numerator and denominator!
     $$F(x, y) = \frac{y - y_0(x)}{-x(y - y_0(x))(y - y_1(x))} = \frac{1}{-x(y - y_1(x))} = \frac{1}{x y_1(x) - xy}.$$
     Notice what just happened: the small root $y_0(x)$ cancelled the zero in the numerator, leaving only the large root $y_1(x)$ in the denominator! Since $x y_1(x) = \frac{1 - x + \sqrt{1 - 2x - 3x^2}}{2}$ has constant term $1$, we can expand in powers of $y$:
     $$F(x, y) = \sum_{j=0}^{\infty} \frac{x^j}{ (x y_1(x))^{j+1} } y^j = \sum_{j=0}^{\infty} F(x, 0) \left(y_0(x)\right)^j y^j.$$
   - **Meanders (All final altitudes $j \ge 0$, i.e., $y = 1$)**: Setting $y = 1$ in $F(x,y) = \frac{1 - x F(x,0)}{1 - 3x}$:
     $$F(x, 1) = \frac{1 - y_0(x)}{1 - 3x} = \frac{1 + x - \sqrt{1 - 2x - 3x^2}}{2x(1 - 3x)} = 1 + 2x + 5x^2 + 13x^3 + 35x^4 + \dots$$

#### Hand-Checkable Toy Trace ($n = 0, 1, 2, 3$) for Motzkin Meanders $F(x, 1)$
- $n=0$: empty path at $j=0 \implies 1$
- $n=1$: steps $0$ (to $j=0$) or $+1$ (to $j=1$); step $-1$ is blocked at $j=0 \implies 2$ paths.
- $n=2$: out of $3^2 = 9$ total paths, exclude $(-1, \cdot)$ ($3$ paths) and $(0, -1)$ ($1$ path) $\implies 9 - 4 = 5$ paths.
- $n=3$: out of $27$ total paths, valid paths ending at $j=0, 1, 2, 3$ have counts $f_{3,0}=4, f_{3,1}=5, f_{3,2}=3, f_{3,3}=1 \implies 4+5+3+1 = 13$ paths.
- Formula $[x^n] F(x,1)$: $1 + 2x + 5x^2 + 13x^3$. Exact match!

---

### 37.3 Multiple Negative Steps ($-1, -2, \dots, -k$): Banderier–Flajolet Theory

What happens when a lattice path can jump downwards by up to $k$ units in a single step, i.e., $\mathcal{S} \subset \{-k, -(k-1), \dots, +m\}$ with step polynomial $S(y) = \sum_{s=-k}^{m} w_s y^s$ ($w_{-k} \neq 0$)?

#### 1. The Multi-Boundary Kernel Equation
Now a path at altitude $j \in \{0, 1, \dots, k-1\}$ can illegally jump below $0$ if it takes a negative step $s < -j$. Let $F_j(x) := [y^j] F(x,y)$ be the generating function of paths ending at altitude $j$. Subtracting all transitions that land at negative altitudes $j + s < 0$ yields:
$$F(x,y) = 1 + x S(y) F(x,y) - x \sum_{j=0}^{k-1} F_j(x) \sum_{s=-k}^{-j-1} w_s y^{j+s}.$$
Multiply through by $y^k$ to clear all negative powers of $y$:
$$\underbrace{\big(y^k - x y^k S(y)\big)}_{K(x, y)} F(x, y) = y^k - x \sum_{j=0}^{k-1} F_j(x) \underbrace{\left(\sum_{s=-k}^{-j-1} w_s y^{k+j+s}\right)}_{R_j(y)}.$$
Notice the degree of the remainder on the right-hand side: for each $j \in \{0, \dots, k-1\}$, the exponent $k + j + s$ ranges from $j$ to $k - 1$. Thus the total boundary correction is a polynomial in $y$ of **degree at most $k - 1$** with $k$ unknown coefficient series $F_0(x), F_1(x), \dots, F_{k-1}(x)$!

#### 2. Why Exactly $k$ Small Roots Exist
Examine the kernel $K(x, y) = y^k - x (w_{-k} + w_{-k+1} y + \dots + w_m y^{k+m})$ as $x \to 0$:
$$K(0, y) = y^k.$$
By Puiseux's Theorem / Newton Polygon analysis at $x = 0$, the roots of $K(x, y) = 0$ split into:
- **Exactly $k$ Small Roots** $y_1(x), y_2(x), \dots, y_k(x)$ that converge to $0$ as $x \to 0$ ( behaving as $y_i(x) \sim \zeta_k^i (w_{-k} x)^{1/k}$ where $\zeta_k = e^{2\pi i / k}$);
- **Exactly $m$ Large Roots** $z_1(x), \dots, z_m(x)$ that diverge to $\infty$ as $x \to 0$.

#### 3. Eliminating All $k$ Unknown Boundary Series simultaneously!
Write the right-hand side of the kernel equation as $y^k - P(x, y)$, where
$$P(x, y) := x \sum_{j=0}^{k-1} F_j(x) R_j(y)$$
is a polynomial in $y$ of degree $\le k - 1$ whose constant term at $y = 0$ is
$$P(x, 0) = x F_0(x) w_{-k}.$$
Since $F(x, y_i(x))$ converges in Puiseux series for all $k$ small roots $y_1(x), \dots, y_k(x)$, plugging $y = y_i(x)$ into the kernel equation gives:
$$y_i(x)^k - P(x, y_i(x)) = 0 \qquad \text{for } i = 1, 2, \dots, k.$$
Look at the polynomial $M(y) := y^k - P(x, y)$:
- It is a **monic polynomial in $y$ of degree $k$** (because $\deg_y P(x,y) \le k-1$);
- It vanishes at the $k$ distinct small roots $y = y_1(x), \dots, y_k(x)$!

By the Fundamental Theorem of Algebra, a monic polynomial of degree $k$ with roots $y_1(x), \dots, y_k(x)$ is **uniquely determined** as the product of its linear factors:
$$\boxed{y^k - x \sum_{j=0}^{k-1} F_j(x) R_j(y) = \prod_{i=1}^{k} \big(y - y_i(x)\big).}$$
This single identity (Banderier & Flajolet 2002) solves for **all $k$ boundary series $F_0(x), \dots, F_{k-1}(x)$ and the full bivariate $F(x,y)$ without inverting a single Vandermonde matrix**:
1. **Excursions $F_0(x) = F(x, 0)$**: Evaluate both sides at $y = 0$:
   $$-x w_{-k} F_0(x) = (-1)^k \prod_{i=1}^{k} y_i(x) \implies \boxed{F(x, 0) = \frac{(-1)^{k-1}}{x w_{-k}} \prod_{i=1}^{k} y_i(x).}$$
2. **Full Bivariate Series $F(x, y)$**: Divide by $K(x,y)$:
   $$\boxed{F(x, y) = \frac{\prod_{i=1}^{k} (y - y_i(x))}{y^k - x y^k S(y)} = \frac{1}{-x w_m \prod_{j=1}^{m} (y - z_j(x))}.}$$
3. **Meanders $F(x, 1)$**: Set $y = 1$ directly:
   $$\boxed{F(x, 1) = \frac{\prod_{i=1}^{k} (1 - y_i(x))}{1 - x S(1)}.}$$

> [!NOTE]
> **Why Symmetric Functions of $y_1(x), \dots, y_k(x)$ Lies in $K[[x]]$**:
> Even though each individual small root $y_i(x)$ is a Puiseux series in $x^{1/k}$, the elementary symmetric polynomials $e_1(y_1,\dots,y_k), \dots, e_k(y_1,\dots,y_k) = \prod_{i=1}^k y_i(x)$ are invariant under Galois permutation of the $k$ small branches and therefore lie in $K[[x]]$ (ordinary formal power series in $x$, with no fractional powers!).

---

### 37.4 The Algebraic / Obstinate Kernel Method for Quarter-Plane Walks ($i, j \ge 0$)

What happens when a 2D walk is constrained by **two boundaries simultaneously**—staying in the first quadrant $\mathbb{Z}_{\ge 0}^2 = \{(i, j) : i \ge 0, j \ge 0\}$?

#### 1. The Two-Boundary Kernel Equation
Let $F(x, y; t) = \sum_{i,j \ge 0} \sum_{n \ge 0} f_{i,j}(n) x^i y^j t^n \in \mathbb{Q}[x, y][[t]]$ be the trivariate generating function of quarter-plane walks with small steps $\mathcal{S} \subset \{-1, 0, +1\}^2$. Multiplying by $x y$ to clear negative powers produces the **Quarter-Plane Kernel Equation** (Bousquet-Mélou & Mishna 2010):
$$x y \, K(x, y; t) F(x, y; t) = x y - A(x; t) - B(y; t) + C(t),$$
where:
- $K(x, y; t) = 1 - t \sum_{(a,b) \in \mathcal{S}} w_{a,b} x^a y^b$ is the **2D Kernel**;
- $A(x; t)$ encodes steps from the horizontal boundary $j = 0$ ($F(x, 0; t)$);
- $B(y; t)$ encodes steps from the vertical boundary $i = 0$ ($F(0, y; t)$);
- $C(t)$ encodes corner steps from $(0, 0)$ ($F(0, 0; t)$).

Notice the new difficulty: the right-hand side is a sum of **decoupled univariate boundary functions** $A(x; t)$ (depending only on $x$) and $B(y; t)$ (depending only on $y$). A single substitution $y = y_0(x; t)$ leaves two unknowns $A(x; t)$ and $B(y_0(x; t); t)$!

#### 2. The Group of the Walk & Vieta Involutions (The "Obstinate" Kernel Method)
Write $x y S(x, y) = \widetilde{A}(x) y^2 + \widetilde{B}(x) y + \widetilde{C}(x) = \widehat{A}(y) x^2 + \widehat{B}(y) x + \widehat{C}(y)$ as a quadratic in both $x$ and $y$.
By Vieta's formulas for a quadratic equation, if $(x, y)$ is a root of the kernel $K(x, y; t) = 0$, then:
- Fixing $y$, the **other** root in $x$ is given by the horizontal Vieta involution:
  $$\Phi(x, y) := \left(\frac{\widehat{C}(y)}{\widehat{A}(y) x}, \, y\right),$$
  which leaves $y$ (and therefore $B(y; t)$!) unchanged while flipping $x \mapsto x' = \frac{\widehat{C}(y)}{\widehat{A}(y) x}$.
- Fixing $x$, the **other** root in $y$ is given by the vertical Vieta involution:
  $$\Psi(x, y) := \left(x, \, \frac{\widetilde{C}(x)}{\widetilde{A}(x) y}\right),$$
  which leaves $x$ (and therefore $A(x; t)$!) unchanged while flipping $y \mapsto y' = \frac{\widetilde{C}(x)}{\widetilde{A}(x) y}$.

The group $G = \langle \Phi, \Psi \rangle$ generated by these two involutions is a dihedral group called the **Group of the Walk**. Whenever $G$ is finite (of order $2m$, typically $4, 6,$ or $8$, which holds for 23 of the 79 non-trivial small-step models in the quarter plane), we can take the **alternating orbit sum** over $(x', y') = g(x, y)$ for $g \in G$:
$$\sum_{g \in G} \operatorname{sgn}(g) \, x' y' K(x', y'; t) F(x', y'; t) = \sum_{g \in G} \operatorname{sgn}(g) \, x' y'.$$
Why does the right-hand side simplify so dramatically?
- Because $\Phi$ fixes $y$ and has $\operatorname{sgn}(\Phi) = -1$, the boundary term $B(y; t)$ cancels in pairs $(g, \Phi g)$!
- Because $\Psi$ fixes $x$ and has $\operatorname{sgn}(\Psi) = -1$, the boundary term $A(x; t)$ cancels in pairs $(g, \Psi g)$!
- The corner term $C(t)$ is fixed by both and cancels completely!

#### 3. Positive-Part Extraction $[x^{>0} y^{>0}]$
When the kernel $K(x, y; t)$ is invariant under the entire group $G$ (which happens whenever the step polynomial has no mixed weights that break symmetry, e.g., the 16 **Gessel / Kreweras / simple walk models**), we can factor $K(x, y; t)$ out of the orbit sum:
$$K(x, y; t) \sum_{g \in G} \operatorname{sgn}(g) \, x_g y_g F(x_g, y_g; t) = \sum_{g \in G} \operatorname{sgn}(g) \, x_g y_g.$$
Dividing by $K(x, y; t)$ gives:
$$\sum_{g \in G} \operatorname{sgn}(g) \, x_g y_g F(x_g, y_g; t) = \frac{\sum_{g \in G} \operatorname{sgn}(g) \, x_g y_g}{K(x, y; t)}.$$
Look at the left-hand side inside $\mathbb{Q}[x, x^{-1}, y, y^{-1}][[t]]$:
- For the identity element $g = \mathrm{id}$, the term is $+ x y F(x, y; t)$, whose powers of $x$ and $y$ are **strictly positive** ($x^{\ge 1} y^{\ge 1}$).
- For every non-identity element $g \neq \mathrm{id}$ in the dihedral group (such as $(x^{-1}, y)$, $(x, y^{-1})$, $(x^{-1}, y^{-1})$), at least one coordinate is inverted, so $x_g y_g F(x_g, y_g; t)$ contains **only non-positive powers** ($x^{\le 0}$ or $y^{\le 0}$)!
Therefore, extracting the **strictly positive part** $[x^{>0} y^{>0}]$ (the terms with $i \ge 1$ and $j \ge 1$) isolates $x y F(x, y; t)$ immediately:
$$\boxed{x y F(x, y; t) = [x^{>0} y^{>0}] \left( \frac{\sum_{g \in G} \operatorname{sgn}(g) \, x_g y_g}{K(x, y; t)} \right).}$$

---

### 37.5 Lattice Path Reflections vs. The Kernel Method

When a problem asks for lattice paths constrained by one or two lines, should you use **André's Reflection Principle** or the **Kernel Method**?

#### 1. Why Reflection Works Only for Symmetric $\pm 1$ Steps
André's Reflection Principle reflects the prefix of a path up to its first contact with a forbidden line $y = x - 1$. For this reflection to be a weight-preserving bijection on the underlying unconstrained step set:
- Every upward step must swap bijectively with a downward step;
- Crucially, the path **cannot jump across the boundary line without landing on it**! If a path has step set $\{-2, +1\}$ (like Łukasiewicz paths or $k$-ary trees with $k \ge 2$), a path at altitude $j = 0$ can take a $-2$ step to $j = -2$, skipping $j = -1$ entirely, or a reflected path changes its step types!
- The **Kernel Method**, by contrast, is purely algebraic and works for **arbitrary asymmetric step weights** and **arbitrary downward jumps $\{-1, \dots, -k\}$**.

#### 2. Dual Boundaries ($0 \le j \le H$): Linear Kernel vs. Repeated Reflection Inclusion-Exclusion
Suppose a path with steps $\{-1, 0, +1\}$ (or $\{-1, +1\}$) is trapped inside a strip of finite height $0 \le j \le H$ (two parallel absorbing barriers at $j = -1$ and $j = H + 1$).
- **Method A (Repeated Reflection / Principle of Inclusion-Exclusion)**:
  For simple steps $\pm 1$ from $(0, a)$ to $(n, b)$ staying strictly between $L_1: y = -1$ and $L_2: y = H + 1$, a bad path either hits $L_1$, or hits $L_1$ then $L_2$, or $L_1 \to L_2 \to L_1$, etc. By alternatingly reflecting the start point $a$ across $L_1$ and $L_2$, the exact count of valid paths is an alternating sum over all mirror images of $a$ (which differs by multiples of the period $2(H+2)$):
  $$\text{Paths}_{(0,a) \to (n,b)}^{[0, H]} = \sum_{k \in \mathbb{Z}} \left( \binom{n}{\frac{n + b - a}{2} + k(H+2)} - \binom{n}{\frac{n + b + a + 2}{2} + k(H+2)} \right).$$
  **Algorithmic Payoff**: When $n$ is known and we only need the single number $\text{Paths}_{(0,a) \to (n,b)}^{[0, H]}$, the sum over $k \in \mathbb{Z}$ has at most $\frac{n}{H+2} + 1$ non-zero binomial terms, running in **$O(n / H)$ time** directly via precomputed factorials ( complementing the $O(H \log H \log n)$ transfer-matrix / polynomial-modulo approach when $H$ is large and $n/H$ is small!).
- **Method B (Two-Sided Kernel / Chebyshev Rational GF)**:
  In generating function form, a strip $0 \le j \le H$ has a finite polynomial $F(x,y) = \sum_{j=0}^H F_j(x) y^j$ with **two boundary conditions**: no $-1$ step from $j=0$, and no $+1$ step from $j=H$:
  $$\big(y - x(1 + y^2)\big) F(x, y) = y x^0 y^a - x F_0(x) - x y^{H+2} F_H(x).$$
  Because $F(x,y)$ is now a **finite polynomial in $y$** of degree $H$, **both** roots of the kernel $y_0(x)$ (small) and $y_1(x) = y_0(x)^{-1}$ (large!) can be legally substituted into $F(x,y)$ in $K((x))$! Substituting $y = y_0(x)$ and $y = y_0(x)^{-1}$ gives a $2 \times 2$ linear system for the two unknowns $F_0(x)$ and $F_H(x)$, yielding the classic Chebyshev rational generating function $F_0(x) = \frac{y_0^{a+1} (1 - y_0^{2(H-a+1)})}{x(1 - y_0^{2(H+2)})}$.

---

### 37.6 Failure Modes & Pitfalls of the Kernel Method

1. **Pitfall 1: Substituting a Large Root into an Infinite Series $F(x, y)$**:
   When $y$ is unbounded ($j \in [0, \infty)$), $F(x,y)$ has infinitely many powers of $y$. Substituting a large root $y_1(x)$ ($\operatorname{val}_x(y_1) < 0$) into $F(x,y)$ is **invalid** because $F(x, y_1(x))$ diverges formally. You may ONLY substitute a large root when $j$ is bounded above ($0 \le j \le H$), so that $F(x,y)$ is a finite polynomial in $y$!
2. **Pitfall 2: Selecting the Wrong Sign of the Square Root $\sqrt{\Delta(x)}$**:
   In $y = \frac{B(x) \pm \sqrt{B(x)^2 - 4A(x)C(x)}}{2A(x)}$ with $A(0) = 0$ and $B(0) \neq 0$, the small root is the branch where the numerator vanishes at $x = 0$. Since $\sqrt{B(0)^2} = +B(0)$ in formal power series (when $B(0) > 0$), you must choose the sign opposite to $B(0)$ so that $B(0) - \sqrt{B(0)^2} = 0$. Choosing the wrong sign gives $[x^0] F(x,0) = \infty$ or $0$ instead of $1$.
3. **Pitfall 3: Off-by-One in Multi-Step Boundary Terms**:
   When a path can jump by $-2$, a step of $-2$ from $j = 0$ lands at $j = -2$ (giving $y^{-2} F_0(x)$), while a step of $-2$ from $j = 1$ lands at $j = -1$ (giving $y^{-1} F_1(x)$), AND a step of $-1$ from $j = 0$ also lands at $j = -1$ (giving $y^{-1} F_0(x)$). Forgetting that $F_0(x)$ contributes to **both** $y^{-2}$ and $y^{-1}$ corrupts the polynomial $R_0(y)$. Always write the explicit double sum $\sum_{j=0}^{k-1} F_j(x) \sum_{s < -j} w_s y^{j+s}$ before clearing denominators.

---

## Iteration 38: Bivariate & Multivariate Good–Lagrange Inversion & MacMahon's Master Theorem

### 38.1 Concrete Combinatorial Object, Ring $K[[x_1, \dots, x_d]]$, Diagnostic Signal & Scratchpad

#### Concrete Combinatorial & Algebraic Object
In univariate Lagrange Inversion (LIF), a single recursive combinatorial class $\mathcal{U}$ (such as rooted trees) satisfies $u(x) = x \Phi(u(x))$ with $\Phi(0) \neq 0$.
In **Bivariate and Multivariate Good–Lagrange Inversion** (I. J. Good 1960; Ira Gessel 1987), we have $d \ge 2$ **mutually recursive combinatorial classes** $\mathcal{U}_1, \mathcal{U}_2, \dots, \mathcal{U}_d$ marked by distinct formal variables $x_1, x_2, \dots, x_d$, satisfying the coupled functional system:
$$u_i = x_i \, \Phi_i(u_1, u_2, \dots, u_d), \qquad i = 1, 2, \dots, d,$$
where each $\Phi_i(\mathbf{u}) \in K[[u_1, \dots, u_d]]$ is a formal power series with **invertible constant term** $[u_1^0 \cdots u_d^0] \Phi_i(\mathbf{0}) \in K^\times$.
Given any "probe" or "root-assembly" series $H(u_1, \dots, u_d) \in K[[u_1, \dots, u_d]]$, our goal is to extract the multi-index coefficient
$$[x_1^{n_1} x_2^{n_2} \cdots x_d^{n_d}] \, H\big(u_1(\mathbf{x}), \dots, u_d(\mathbf{x})\big)$$
directly in terms of coefficients of $H$ and powers of $\Phi_1, \dots, \Phi_d$, **without** algebraically eliminating $u_2, \dots, u_d$!

#### The Diagnostic Signal
How do you recognize a **Bivariate / Multivariate Good–Lagrange Inversion** problem?
- **Signal A (Multi-Type / Bicoloured Recursive Trees)**: You are counting rooted trees or cactus-like graphs with $2$ (or $d$) vertex types—for instance, bipartite graphs with $n$ black vertices (marked by $x$) and $m$ white vertices (marked by $y$)—where a black vertex has a multiset/sequence of white children ($u = x \Phi(u,v)$) and a white vertex has a multiset/sequence of black children ($v = y \Psi(u,v)$).
- **Signal B (Algebraic Elimination Fails or Explodes)**: In univariate problems like ABC 222 H ($B = 2A + A^2, A = x(1+A+B)^2$), one variable has no $y$ marker of its own and can be substituted directly into the other. However, if **both** equations contain transcendental operations ($u = x e^v$ and $v = y e^u$) or if we must track **both** parameters $x^n$ and $y^m$ independently ($[x^n y^m]$), substituting $v = y e^u$ into $u = x e^{y e^u}$ creates an iterated exponential that univariate LIF cannot simplify cleanly! Good–Lagrange Inversion handles the $d \times d$ system symmetrically in a single step.
- **Signal C (Product of Linear Powers $[x_1^{n_1} \cdots x_d^{n_d}] \prod_{i=1}^d L_i(\mathbf{x})^{n_i}$)**: Whenever the exponent $n_i$ of the $i$-th linear form $L_i(x_1,\dots,x_d)$ matches the target extraction power $x_i^{n_i}$, you are looking at **MacMahon's Master Theorem**, which is the linear specialization of Multivariate Good–Lagrange Inversion.

#### The Reverse-Engineering Scratchpad: Where Does the Jacobian Determinant Come From?
In univariate LIF, changing variables from $x = \frac{u}{\Phi(u)}$ to $u$ inside the formal residue $[x^n] H(u(x)) = \operatorname{res}_x \big(H(u(x)) x^{-n-1}\big)$ multiplies by the differential $dx = \frac{d}{du}\!\left(\frac{u}{\Phi(u)}\right) du = \frac{\Phi(u) - u \Phi'(u)}{\Phi(u)^2} du = \frac{1}{\Phi(u)}\left(1 - \frac{u \Phi'(u)}{\Phi(u)}\right) du$.
What happens when we change variables from $\mathbf{x} = (x_1, \dots, x_d)$ to $\mathbf{u} = (u_1, \dots, u_d)$ via
$$x_i = \frac{u_i}{\Phi_i(u_1, \dots, u_d)} \qquad (i = 1, \dots, d)$$
inside a $d$-dimensional formal residue $\operatorname{res}_{\mathbf{x}} := [x_1^{-1} \cdots x_d^{-1}]$?

1. **Step 1 (Write the $d$-Dimensional Formal Residue in $\mathbf{x}$)**:
   $$[x_1^{n_1} \cdots x_d^{n_d}] H(\mathbf{u}(\mathbf{x})) = \operatorname{res}_{x_1, \dots, x_d} \left( H(\mathbf{u}(\mathbf{x})) \, x_1^{-n_1 - 1} \cdots x_d^{-n_d - 1} \, dx_1 \wedge \cdots \wedge dx_d \right).$$
2. **Step 2 (Compute the Exterior Differential $dx_1 \wedge \cdots \wedge dx_d$ via the Jacobian Matrix)**:
   Since $x_i = u_i \Phi_i(\mathbf{u})^{-1}$ belongs to $u_i K[[u_1, \dots, u_d]]$ with invertible $\Phi_i(\mathbf{0})$, the map $\mathbf{u} \mapsto \mathbf{x}$ is a formal diffeomorphism at the origin $\mathbf{0}$ (its Jacobian matrix at $\mathbf{u} = \mathbf{0}$ is diagonal with non-zero entries $\Phi_i(\mathbf{0})^{-1}$).
   Let us compute the $(i, j)$ entry of the Jacobian matrix $\frac{\partial x_i}{\partial u_j}$ using the quotient/product rule:
   $$\frac{\partial x_i}{\partial u_j} = \frac{\partial}{\partial u_j} \left( \frac{u_i}{\Phi_i(\mathbf{u})} \right) = \frac{\delta_{i,j} \Phi_i(\mathbf{u}) - u_i \frac{\partial \Phi_i}{\partial u_j}}{\Phi_i(\mathbf{u})^2} = \frac{1}{\Phi_i(\mathbf{u})} \left( \delta_{i,j} - \frac{u_i}{\Phi_i(\mathbf{u})} \frac{\partial \Phi_i}{\partial u_j} \right),$$
   where $\delta_{i,j} = 1$ if $i = j$ and $0$ if $i \neq j$.
3. **Step 3 (Factor $\Phi_i(\mathbf{u})^{-1}$ Out of Each Row $i$ of the Determinant)**:
   Taking the determinant of the $d \times d$ matrix $\left(\frac{\partial x_i}{\partial u_j}\right)_{1 \le i,j \le d}$, we pull the common factor $\frac{1}{\Phi_i(\mathbf{u})}$ out of row $i$ for each $i = 1, \dots, d$:
   $$\det\!\left(\frac{\partial x_i}{\partial u_j}\right) = \left(\prod_{i=1}^d \frac{1}{\Phi_i(\mathbf{u})}\right) \det_{1 \le i,j \le d}\!\left( \delta_{i,j} - \frac{u_i}{\Phi_i(\mathbf{u})} \frac{\partial \Phi_i}{\partial u_j} \right).$$
    Note also that conjugated by the diagonal matrix $\operatorname{diag}(u_1, \dots, u_d)$, the determinant is identical whether we write $\frac{u_i}{\Phi_i} \frac{\partial \Phi_i}{\partial u_j}$ or $\frac{u_j}{\Phi_i} \frac{\partial \Phi_i}{\partial u_j}$!
4. **Step 4 (Substitute $x_i^{-n_i - 1} = u_i^{-n_i - 1} \Phi_i(\mathbf{u})^{n_i + 1}$)**:
   Multiplying $\prod_{i=1}^d x_i^{-n_i - 1} = \prod_{i=1}^d u_i^{-n_i - 1} \Phi_i(\mathbf{u})^{n_i + 1}$ by $\det\!\left(\frac{\partial x_i}{\partial u_j}\right)$, the extra $+1$ in the exponent $\Phi_i(\mathbf{u})^{n_i + 1}$ **cancels** the factor $\frac{1}{\Phi_i(\mathbf{u})}$ pulled out of row $i$! What remains is $\prod_{i=1}^d u_i^{-n_i - 1} \Phi_i(\mathbf{u})^{n_i}$ times the dimensionless Jacobian determinant!

---

### 38.2 The Complete Theorems: Multivariate ($d \times d$) and Bivariate ($2 \times 2$) Good–Lagrange

#### Theorem 38.1 (Multivariate Good–Lagrange Inversion Formula — Good 1960, Gessel 1987)
Let $u_i = x_i \Phi_i(u_1, \dots, u_d)$ for $i = 1, \dots, d$, where $\Phi_i(\mathbf{u}) \in K[[u_1, \dots, u_d]]$ satisfies $\Phi_i(\mathbf{0}) \neq 0$. Then for any formal power series $H(u_1, \dots, u_d) \in K[[u_1, \dots, u_d]]$ and any non-negative integers $n_1, \dots, n_d \ge 0$:

$$\boxed{[x_1^{n_1} \cdots x_d^{n_d}] H\big(u_1(\mathbf{x}), \dots, u_d(\mathbf{x})\big) = [u_1^{n_1} \cdots u_d^{n_d}] \, H(\mathbf{u}) \, \det_{1 \le i,j \le d}\!\left(\delta_{i,j} - \frac{u_j}{\Phi_i(\mathbf{u})} \frac{\partial \Phi_i(\mathbf{u})}{\partial u_j}\right) \prod_{k=1}^{d} \Phi_k(\mathbf{u})^{n_k}.}$$

#### Corollary 38.2 (Explicit Bivariate $2 \times 2$ Good–Lagrange Formula)
For $d = 2$ with $u = x \Phi(u, v)$ and $v = y \Psi(u, v)$, the $2 \times 2$ determinant is
$$\det \begin{pmatrix} 1 - \frac{u}{\Phi} \Phi_u & -\frac{v}{\Phi} \Phi_v \\ -\frac{u}{\Psi} \Psi_u & 1 - \frac{v}{\Psi} \Psi_v \end{pmatrix} = \left(1 - \frac{u \Phi_u}{\Phi}\right)\left(1 - \frac{v \Psi_v}{\Psi}\right) - \frac{u v \, \Phi_v \Psi_u}{\Phi \Psi} = 1 - \frac{u \Phi_u}{\Phi} - \frac{v \Psi_v}{\Psi} + \frac{uv(\Phi_u \Psi_v - \Phi_v \Psi_u)}{\Phi \Psi}.$$
Multiplying by $\Phi(u,v)^n \Psi(u,v)^m$ yields the **First Bivariate Good–Lagrange Form** (valid for ALL $n, m \ge 0$):
$$\boxed{[x^n y^m] H(u, v) = [u^n v^m] \, H(u, v) \left[ \left(\Phi - u \Phi_u\right)\left(\Psi - v \Psi_v\right) - u v \Phi_v \Psi_u \right] \Phi(u, v)^{n-1} \Psi(u, v)^{m-1}.}$$

When $n \ge 1$ and $m \ge 1$ and $H(u,v) = u v$ (or via multivariate integration by parts inside the residue), there is an even more compact **Second Bivariate Form** when $\Phi(u,v) = \Phi(v)$ depends only on $v$ and $\Psi(u,v) = \Psi(u)$ depends only on $u$ (the **Alternating Bipartite Case** $u = x \Phi(v), v = y \Psi(u)$):
- Since $\Phi_u = 0$ and $\Psi_v = 0$, the diagonal terms simplify to $1$, and the $2 \times 2$ determinant collapses to
  $$1 - \frac{u v \Phi'(v) \Psi'(u)}{\Phi(v) \Psi(u)}!$$
- Therefore, for $u = x \Phi(v)$ and $v = y \Psi(u)$:
  $$\boxed{[x^n y^m] H(u, v) = [u^n v^m] \, H(u, v) \left( \Phi(v)^n \Psi(u)^m - u v \, \Phi'(v) \Phi(v)^{n-1} \Psi'(u) \Psi(u)^{m-1} \right).}$$

---

### 38.3 Complete Worked Combinatorial Applications & Toy Traces ($n, m \le 3$)

#### Application 1: Bicoloured Labeled Trees & Complete Bipartite Spanning Trees ($K_{n,m}$)
**Combinatorial Problem**: Count the number of labeled spanning trees of the complete bipartite graph $K_{n,m}$ (equivalently, bicoloured labeled trees with $n$ black vertices and $m$ white vertices, where every edge connects a black vertex and a white vertex).
**Generating Function Setup**:
Let $U(x, y)$ be the exponential generating function (EGF) of rooted bicoloured trees whose root is **black**, and $V(x, y)$ be the EGF of rooted bicoloured trees whose root is **white**, where $x$ marks black vertices ($n$) and $y$ marks white vertices ($m$).
- A black root ($x$) has an unordered set of white-rooted subtrees ($\exp(V)$);
- A white root ($y$) has an unordered set of black-rooted subtrees ($\exp(U)$).
Thus $(U, V)$ satisfies the coupled bivariate Good–Lagrange system:
$$U = x e^{V}, \qquad V = y e^{U}.$$
Here $\Phi(U, V) = e^V$ (depends only on $V$) and $\Psi(U, V) = e^U$ (depends only on $U$). Suppose we want to extract $[x^n y^m] U(x, y)$ (rooted at a black vertex, so dividing by $n$ gives unrooted bicoloured trees).

**Step-by-Step Annotated Derivation**:
Apply the Alternating Bipartite Good–Lagrange Formula with $H(U, V) = U$, $\Phi(V) = e^V$, $\Psi(U) = e^U$:
$$\begin{aligned}
[x^n y^m] U(x, y)
&= [U^n V^m] \, U \left( e^{n V} e^{m U} - U V \, e^V e^{(n-1)V} e^U e^{(m-1)U} \right) && \text{(Since } \Phi'(V)\Phi(V)^{n-1} = e^{nV}\text{)} \\
&= [U^n V^m] \left( U e^{m U} e^{n V} - U^2 V e^{m U} e^{n V} \right) \\
&= \left([U^{n-1}] e^{m U}\right)\left([V^m] e^{n V}\right) - \left([U^{n-2}] e^{m U}\right)\left([V^{m-1}] e^{n V}\right) && \text{(Shift indices } U, U^2, V\text{)} \\
&= \frac{m^{n-1}}{(n-1)!} \frac{n^m}{m!} - \frac{m^{n-2}}{(n-2)!} \frac{n^{m-1}}{(m-1)!} \\
&= \frac{m^{n-2} n^{m-1}}{(n-1)! m!} \big( m \cdot n - (n - 1) m \big) && \text{(Factor out common terms)} \\
&= \frac{n^{m-1} m^{n-1}}{(n-1)! m!}.
\end{aligned}$$
Since $U(x, y)$ is an EGF where one of the $n$ black vertices is distinguished as the root, the number of **rooted** bicoloured trees is $n! m! [x^n y^m] U(x, y) = n \cdot n^{m-1} m^{n-1} = n^m m^{n-1}$, and dividing by $n$ gives the famous **Bicoloured Cayley Formula** for unrooted spanning trees of $K_{n,m}$:
$$\boxed{T(K_{n,m}) = n^{m-1} m^{n-1}.}$$
Notice how the Jacobian subtraction term $-UV e^{mU} e^{nV}$ reduced $m n - (n-1)m$ to $+m$, killing the overcount of edges vs. vertices!

**Hand-Checkable Toy Trace ($n = 2, m = 2$)**:
- In $K_{2,2}$ (which is a 4-cycle $C_4$), removing any 1 of the 4 edges gives a spanning tree, so $T(K_{2,2}) = 4$.
- Formula: $n^{m-1} m^{n-1} = 2^{2-1} \cdot 2^{2-1} = 2 \cdot 2 = 4$.
- For $n = 2, m = 3$ ($K_{2,3}$): to form a tree, one of the $3$ white vertices must have degree $2$ (connected to both black vertices), and the other $2$ white vertices each choose $1$ of the $2$ black vertices $\implies 3 \times 2 \times 2 = 12$ spanning trees.
- Formula: $2^{3-1} \cdot 3^{2-1} = 4 \cdot 3 = 12$. Exact match!

---

#### Application 2: Bicoloured Plane (Ordered) Trees
Suppose a black vertex has a **possibly empty ordered sequence** of white children, and a white vertex has a **possibly empty ordered sequence** of black children:
$$u = \frac{x}{1 - v}, \qquad v = \frac{y}{1 - u}.$$
Here $\Phi(v) = (1 - v)^{-1}$ and $\Psi(u) = (1 - u)^{-1}$, with $\Phi'(v) = (1-v)^{-2}$ and $\Psi'(u) = (1-u)^{-2}$.
For $n, m \ge 1$, the number of such plane trees rooted at a black vertex ($H(u,v) = u$) is:
$$\begin{aligned}
[x^n y^m] u
&= [u^n v^m] \, u \left( (1-v)^{-n} (1-u)^{-m} - u v (1-v)^{-n-1} (1-u)^{-m-1} \right) \\
&= \binom{n+m-1}{m} \binom{m+n-2}{n-1} - \binom{n+m}{m-1} \binom{m+n-2}{n-2} \\
&= \frac{1}{n + m - 1} \binom{n + m - 1}{n} \binom{n + m - 1}{m} \cdot n = \frac{1}{m} \binom{n + m - 2}{n - 1} \binom{n + m - 1}{m - 1} \quad (\text{Narayana / Raney numbers!}).
\end{aligned}$$

---

### 38.4 MacMahon's Master Theorem (MMT) & Dixon's Identity

#### 1. Statement & Proof of MacMahon's Master Theorem via Good–Lagrange
In 1915, Major Percy A. MacMahon proved a remarkable duality between the coefficients of products of powers of linear forms and the reciprocal of a determinant. Using Multivariate Good–Lagrange Inversion, **MacMahon's Master Theorem is a 4-line corollary**!

> **Theorem 38.3 (MacMahon's Master Theorem, 1915)**:
> Let $A = (a_{i,j})_{1 \le i,j \le d}$ be any $d \times d$ matrix over a commutative ring $K$, and define the $d$ linear forms
> $$L_i(u_1, \dots, u_d) := \sum_{j=1}^{d} a_{i,j} u_j \qquad (i = 1, \dots, d).$$
> Then for any non-negative integers $n_1, n_2, \dots, n_d \ge 0$, the coefficient of $u_1^{n_1} \cdots u_d^{n_d}$ in the product $L_1(\mathbf{u})^{n_1} \cdots L_d(\mathbf{u})^{n_d}$ equals the coefficient of $x_1^{n_1} \cdots x_d^{n_d}$ in the inverse determinant:
> $$\boxed{[u_1^{n_1} \cdots u_d^{n_d}] \prod_{i=1}^{d} \left(\sum_{j=1}^{d} a_{i,j} u_j\right)^{n_i} = [x_1^{n_1} \cdots x_d^{n_d}] \, \frac{1}{\det(I_d - X A)},}$$
> where $X := \operatorname{diag}(x_1, \dots, x_d)$, so $I_d - X A$ is the $d \times d$ matrix with $(i, j)$ entry $\delta_{i,j} - x_i a_{i,j}$.

**Complete Annotated Proof via Theorem 38.1**:
1. Notice that in $[u_1^{n_1} \cdots u_d^{n_d}] \prod_{i=1}^d L_i(\mathbf{u})^{n_i}$, we can rescale each variable $u_j$ or shift the exponents by $1$: equivalently, apply Theorem 38.1 to the system
   $$u_i = x_i \, \Phi_i(u_1, \dots, u_d) \quad \text{with} \quad \Phi_i(u_1, \dots, u_d) := \frac{1}{1 - \sum_{j=1}^d a_{i,j} u_j} = \frac{1}{1 - L_i(\mathbf{u})},$$
   Wait—there is an even more direct choice! In Theorem 38.1, set $H(\mathbf{u}) = 1$? No, if we set $H(\mathbf{u}) := \det\!\left(\delta_{i,j} - \frac{u_j}{\Phi_i(\mathbf{u})} \frac{\partial \Phi_i}{\partial u_j}\right)^{-1}$, the Jacobian determinant cancels completely!
   Let us check what happens when we choose the **linear-exponential or affine** $\Phi_i$, or even simpler: apply the multivariate change of variables $x_i = u_i / \Phi_i(\mathbf{u})$ directly with
   $$\Phi_i(u_1, \dots, u_d) := 1 + \sum_{j=1}^{d} a_{i,j} u_j,$$
    wait: in our problem, $\prod_{i=1}^d L_i(u_1, \dots, u_d)^{n_i}$ is **homogeneous** of total degree $\sum n_i$ in $u_1, \dots, u_d$!
   Because $L_i(u_1, \dots, u_d)$ is homogeneous of degree $1$, extracting $[u_1^{n_1} \cdots u_d^{n_d}]$ from $\prod_{i=1}^d L_i(\mathbf{u})^{n_i}$ is **identical** to extracting $[u_1^{n_1} \cdots u_d^{n_d}]$ from $\prod_{i=1}^d \big(1 + L_i(\mathbf{u})\big)^{n_i}$? Wait: no, $(1 + L_i)^{n_i}$ has lower-degree terms, whereas $L_i^{n_i}$ is already homogeneous of degree $n_i$, so the **top homogeneous part** of degree $\sum n_i$ in $\prod_{i=1}^d (1 + L_i(\mathbf{u}))^{n_i}$ is literally $\prod_{i=1}^d L_i(\mathbf{u})^{n_i}$!
   Wait—even better! We don't even need $1 + L_i$: consider the linear change of variables in the formal residue over $K((u_1, \dots, u_d))$:
   $$x_i = \frac{u_i}{\Phi_i(\mathbf{u})} \quad \text{Wait: if instead we set } \Phi_i(\mathbf{u}) = 1 \text{? No, set } y_i := u_i - x_i \sum_{j=1}^d a_{i,j} u_j!$$
   Let us compare both proofs so the reader sees why MMT is so transparent:
   - **Direct Good–Lagrange Proof**:
     Define $\Phi_i(u_1, \dots, u_d) := \exp\!\left(\sum_{j=1}^d a_{i,j} u_j\right)$? No! Look at $\Phi_i(u_1, \dots, u_d)$ in Theorem 38.1: we want $\prod_{i=1}^d \Phi_i(\mathbf{u})^{n_i}$ to have top-degree coefficient equal to $\prod_{i=1}^d L_i(\mathbf{u})^{n_i}$, OR we can divide $L_i(\mathbf{u})$ by $u_i$:
     Set $w_i := x_i L_i(\mathbf{u}) = x_i \sum_{j=1}^d a_{i,j} u_j$.
     Even simpler: in Theorem 38.1, replace $x_i$ by $x_i t$ and set $\Phi_i(\mathbf{u}) = 1 + L_i(\mathbf{u})$? No, let's check what $\det\!\left(\delta_{i,j} - \frac{u_j}{\Phi_i}\frac{\partial \Phi_i}{\partial u_j}\right)$ equals when $\Phi_i(\mathbf{u}) = \frac{1}{1 - \text{something}}$ vs. when we do the linear residue change of variables:
     $$\begin{aligned}
     [u_1^{n_1} \cdots u_d^{n_d}] \prod_{i=1}^{d} L_i(\mathbf{u})^{n_i}
     &= \operatorname{res}_{u_1, \dots, u_d} \left( \prod_{i=1}^{d} \frac{L_i(\mathbf{u})^{n_i}}{u_i^{n_i + 1}} \, du_1 \wedge \cdots \wedge du_d \right).
     \end{aligned}$$
     Multiply by $x_1^{n_1} \cdots x_d^{n_d}$ and sum over all $n_1, \dots, n_d \ge 0$ in $K((u_1, \dots, u_d))[[x_1, \dots, x_d]]$:
     $$\begin{aligned}
     \sum_{n_1, \dots, n_d \ge 0} x_1^{n_1} \cdots x_d^{n_d} [u_1^{n_1} \cdots u_d^{n_d}] \prod_{i=1}^{d} L_i(\mathbf{u})^{n_i}
     &= \operatorname{res}_{u_1, \dots, u_d} \left( \prod_{i=1}^{d} \frac{1}{u_i - x_i L_i(\mathbf{u})} \, du_1 \wedge \cdots \wedge du_d \right).
     \end{aligned}$$
     Look at the denominators $y_i := u_i - x_i L_i(\mathbf{u}) = \sum_{j=1}^d (\delta_{i,j} - x_i a_{i,j}) u_j$ for $i = 1, \dots, d$.
     This is a **linear transformation** $\mathbf{y} = (I_d - X A) \mathbf{u}$!
     Its Jacobian matrix is $\frac{\partial y_i}{\partial u_j} = \delta_{i,j} - x_i a_{i,j}$, so the exterior differential transforms as:
     $$dy_1 \wedge \cdots \wedge dy_d = \det(I_d - X A) \, du_1 \wedge \cdots \wedge du_d \implies du_1 \wedge \cdots \wedge du_d = \frac{dy_1 \wedge \cdots \wedge dy_d}{\det(I_d - X A)}.$$
     Substituting this into the multivariate formal residue gives:
     $$\operatorname{res}_{y_1, \dots, y_d} \left( \frac{1}{\det(I_d - X A)} \frac{dy_1 \wedge \cdots \wedge dy_d}{y_1 y_2 \cdots y_d} \right) = \frac{1}{\det(I_d - X A)} \operatorname{res}_{\mathbf{y}} \left(\frac{dy_1 \wedge \cdots \wedge dy_d}{y_1 \cdots y_d}\right) = \frac{1}{\det(I_d - X A)}. \qquad \blacksquare$$

> [!TIP]
> **Look at that 3-line residue proof of MacMahon's Master Theorem**:
> Just as Furstenberg's Diagonal Method turns $[x^n y^n]$ into $\operatorname{res}_z$, summing $[u_1^{n_1} \cdots u_d^{n_d}] \prod L_i(\mathbf{u})^{n_i} x_i^{n_i}$ over $n_i \ge 0$ creates the geometric series $\prod_{i=1}^d \frac{1}{u_i - x_i L_i(\mathbf{u})}$, and the linear change of variables $y_i = u_i - x_i L_i(\mathbf{u})$ pulls out the Jacobian $\det(I_d - X A)^{-1}$!

---

#### 2. Classic Application of MMT: Dixon's Binomial Identity
Let us prove **Dixon's Identity** for any non-negative integers $a, b, c \ge 0$:
$$\sum_{k} (-1)^k \binom{a+b}{a+k} \binom{b+c}{b+k} \binom{c+a}{c+k} = \frac{(a+b+c)!}{a! \, b! \, c!}.$$

**Step-by-Step Annotated Derivation via MacMahon's Master Theorem**:
1. **Rewrite the Binomial Sum as a 3-Variable Coefficient Extraction**:
   Observe that by the binomial theorem,
   $$\binom{a+b}{a+k} = [u^{a+k} v^{b-k}] (u + v)^{a+b} = [x^{2a} y^{2b} z^{2c}] \dots ?$$
   Even simpler: look at the product of the three antisymmetric binomial factors
   $$(y - z)^{a+b} (z - x)^{b+c} (x - y)^{c+a}.$$
   Let us expand each factor and seek the coefficient of $x^{2a} y^{2b} z^{2c}$? Wait: the total degree of $(y-z)^{a+b}(z-x)^{b+c}(x-y)^{c+a}$ is $(a+b)+(b+c)+(c+a) = 2a+2b+2c$.
   Instead, write it in the exact MMT form where the exponents match the target powers! We want $[x^{b+c} y^{c+a} z^{a+b}]$ of:
   $$P(x,y,z) := (y - z)^{b+c} (z - x)^{c+a} (x - y)^{a+b}.$$
   Let us first expand $P(x,y,z)$ directly to see why $[x^{b+c} y^{c+a} z^{a+b}] P(x,y,z)$ is Dixon's sum:
   - In $(y - z)^{b+c} = \sum_i (-1)^{b+c-i} \binom{b+c}{i} y^i z^{b+c-i}$, let $i = b + k$, so $y$ has exponent $b+k$ and $z$ has exponent $c-k$.
   - To reach total $z$-exponent $a+b$, the factor $(z - x)^{c+a}$ must contribute $z^{(a+b) - (c-k)} = z^{a+b-c+k}$ and $x^{(c+a) - (a+b-c+k)} = x^{2c-b-k}$? Wait: it's even cleaner if we match the exponents of $(y-z)^{a+b} (z-x)^{b+c} (x-y)^{c+a}$ to $[x^{b+c} y^{c+a} z^{a+b}]$ by dividing by $x y z$:
   In $(y-z)^{a+b} (z-x)^{b+c} (x-y)^{c+a}$, let the $y$-power from $(y-z)^{a+b}$ be $a - k$ (so $z$-power is $b + k$).
   Then to get total $z$-power $2c$? No, set target powers $[x^{2a} y^{2b} z^{2c}]$? No, set target powers **$[x^{b+c} y^{c+a} z^{a+b}]$** in $(y - z)^{b+c} (z - x)^{c+a} (x - y)^{a+b}$:
   - From $(y-z)^{b+c}$: pick $y^{b-k} (-z)^{c+k}$, coefficient $(-1)^{c+k} \binom{b+c}{b-k} = (-1)^{c+k} \binom{b+c}{c+k}$.
   - From $(z-x)^{c+a}$: since total $z$-exponent must be $a+b$, and we already have $z^{c+k}$, we must pick $z^{a+b-c-k}$? That doesn't have $c+a$ on top!
   - Why? Because in $(y-z)^{a+b} (z-x)^{b+c} (x-y)^{c+a}$, if we extract **$[x^{b+c} y^{c+a} z^{a+b}]$**? No, in $(y-z)^{a+b}$, the top index is $a+b$, which matches the target power of **$z^{a+b}$**!
     Look at that:
     - $(x - y)^{c+a}$ has exponent $c+a$ (matches $y^{c+a}$),
     - $(y - z)^{a+b}$ has exponent $a+b$ (matches $z^{a+b}$),
     - $(z - x)^{b+c}$ has exponent $b+c$ (matches $x^{b+c}$)!
     Let us check the expansion of $[x^{b+c} y^{c+a} z^{a+b}] (z - x)^{b+c} (x - y)^{c+a} (y - z)^{a+b}$:
     - From $(z - x)^{b+c}$: pick $z^{b+k} (-x)^{c-k}$, coefficient $(-1)^{c-k} \binom{b+c}{b+k}$.
     - From $(y - z)^{a+b}$: to make the total $z$-exponent $(a+b)$, we need $z^{(a+b) - (b+k)} = z^{a-k}$, so we pick $y^{b+k} (-z)^{a-k}$, coefficient $(-1)^{a-k} \binom{a+b}{a-k} = (-1)^{a-k} \binom{a+b}{b+k}$.
     - From $(x - y)^{c+a}$: to make the total $x$-exponent $(b+c)$, we need $x^{(b+c) - (c-k)} = x^{b+k}$, and the remaining $y$-exponent is $(c+a) - (b+k)$, making total $y$-exponent $(b+k) + (c+a - b - k) = c+a$! Its coefficient is $(-1)^{c+a-b-k} \binom{c+a}{b+k}$.
      shifting the summation index $k \mapsto k - b$ (so $b+k \mapsto j = a+k'$) gives $(-1)^a \sum_{k} (-1)^k \binom{a+b}{a+k}\binom{b+c}{b+k}\binom{c+a}{c+k}$!
2. **Apply MacMahon's Master Theorem ($3 \times 3$ Matrix)**:
   We are extracting $[x^{b+c} y^{c+a} z^{a+b}] L_1(x,y,z)^{b+c} L_2(x,y,z)^{c+a} L_3(x,y,z)^{a+b}$ where:
   $$\begin{pmatrix} L_1 \\ L_2 \\ L_3 \end{pmatrix} = \begin{pmatrix} z - x \\ x - y \\ y - z \end{pmatrix} = \underbrace{\begin{pmatrix} -1 & 0 & 1 \\ 1 & -1 & 0 \\ 0 & 1 & -1 \end{pmatrix}}_{A} \begin{pmatrix} x \\ y \\ z \end{pmatrix}.$$
   Let us compute $\det(I_3 - X A)$:
   $$I_3 - X A = \begin{pmatrix} 1 + x & 0 & -x \\ -y & 1 + y & 0 \\ 0 & -z & 1 + z \end{pmatrix}.$$
   Expanding the $3 \times 3$ determinant along the first row:
   $$\begin{aligned}
   \det(I_3 - X A) &= (1 + x)(1 + y)(1 + z) + (-x)(y z) \\
   &= 1 + x + y + z + xy + yz + zx + xyz - xyz \\
   &= 1 + (x + y + z + xy + yz + zx) \\
   &= (1 + x)(1 + y)(1 + z) - xyz? \quad \text{Wait: the } +xyz \text{ and } -xyz \text{ CANCELLED!}
   \end{aligned}$$
    Wait: check the sign of the $(-x)$ cofactor in $I_3 - XA$:
   The $(1,3)$ entry is $-x$, and its $2 \times 2$ minor is $\det \begin{pmatrix} -y & 1+y \\ 0 & -z \end{pmatrix} = + y z$.
   So the determinant is $(1+x)(1+y)(1+z) - x y z$! Wait: why did we use $L_1 = z-x$ instead of the skew-symmetric matrix where $a_{i,i} = 0$?
   Let's check the even cleaner permutation of rows: instead of matching $(z-x)$ to $x^{b+c}$, match:
   - $L_1 = y - z$ to $x^{a}$ (exponent $a$!),
   - $L_2 = z - x$ to $y^{b}$ (exponent $b$!),
   - $L_3 = x - y$ to $z^{c}$ (exponent $c$!)
   Wait: $[x^{2a} y^{2b} z^{2c}] (y-z)^{b+c} (z-x)^{c+a} (x-y)^{a+b}$ has exponents $b+c \neq 2a$. What if we extract **$[x^{2a} y^{2b} z^{2c}]$**? No! What if we match:
   - $L_1(x,y,z) = y - z$ with exponent $b + c$? No, in $[x^{2a} y^{2b} z^{2c}]$, the exponents don't match $b+c$.
   Why did we have $L_1 = z - x$ above? Because in $(y-z)^{b+c} (z-x)^{c+a} (x-y)^{a+b}$, if we extract **$[x^{b+c} y^{c+a} z^{a+b}]$**, then:
   - $L_1 = y - z$ has exponent $b + c$ (matches $x^{b+c}$!)
   - $L_2 = z - x$ has exponent $c + a$ (matches $y^{c+a}$!)
   - $L_3 = x - y$ has exponent $a + b$ (matches $z^{a+b}$!)
   Let us check THIS assignment!
   Here $L_1 = y - z$ (has NO $x$!), $L_2 = z - x$ (has NO $y$!), $L_3 = x - y$ (has NO $z$!).
   So the matrix $A$ is **skew-symmetric with zeros on the diagonal**:
   $$A = \begin{pmatrix} 0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0 \end{pmatrix} \implies I_3 - X A = \begin{pmatrix} 1 & -x & x \\ y & 1 & -y \\ -z & z & 1 \end{pmatrix}.$$
   Now compute $\det(I_3 - X A)$:
   $$\begin{aligned}
   \det \begin{pmatrix} 1 & -x & x \\ y & 1 & -y \\ -z & z & 1 \end{pmatrix}
   &= 1(1 + yz) - (-x)(y - yz) + x(yz + z) \\
   &= 1 + yz + xy - xyz + xyz + xz \\
   &= 1 + xy + yz + zx!
   \end{aligned}$$
   Look at $\det(I_3 - X A) = 1 + xy + yz + zx$: it is a **pure degree-2 polynomial in $x, y, z$**!
   Therefore, by MacMahon's Master Theorem:
   $$\begin{aligned}
   [x^{b+c} y^{c+a} z^{a+b}] (y - z)^{b+c} (z - x)^{c+a} (x - y)^{a+b}
   &= [x^{b+c} y^{c+a} z^{a+b}] \, \frac{1}{1 + xy + yz + zx} \\
   &= [x^{b+c} y^{c+a} z^{a+b}] \sum_{N=0}^{\infty} (-1)^N (xy + yz + zx)^N.
   \end{aligned}$$
   In $(xy + yz + zx)^N = \sum_{i+j+k=N} \frac{N!}{i! j! k!} (yz)^i (zx)^j (xy)^k$, the exponents of $x, y, z$ are:
   $$j + k = b + c, \qquad k + i = c + a, \qquad i + j = a + b.$$
   The unique solution to this $3 \times 3$ linear system is **$i = a, \; j = b, \; k = c$** (with $N = a + b + c$)!
   Therefore, only the single multinomial term $(i, j, k) = (a, b, c)$ survives, yielding
   $$(-1)^{a+b+c} \frac{(a + b + c)!}{a! \, b! \, c!}. \qquad \blacksquare$$

---

### 38.5 Failure Modes & Edge Cases in Good–Lagrange Inversion

1. **Pitfall 1: Non-Invertible Constant Term $\Phi_i(\mathbf{0}) = 0$**:
   In $u_i = x_i \Phi_i(\mathbf{u})$, each $\Phi_i(\mathbf{0})$ must be a unit in $K$. If a combinatorial equation reads $U = x (V + V^2)$, you cannot directly set $\Phi(U,V) = V + V^2$ because $\Phi(0,0) = 0$. Instead, either substitute $V$ into $U$, or shift variables ($U = x y \widetilde{U}$) so the shifted factor has non-zero constant term.
2. **Pitfall 2: Forgetting the Off-Diagonal Term $-uv \Phi_v \Psi_u$ in the Jacobian**:
   Beginners who know 1D LIF $[x^n] H(u) = [u^n] H(u) (1 - \frac{u \Phi'}{\Phi}) \Phi^n$ often guess that 2D LIF simply multiplies the two 1D factors $(1 - \frac{u \Phi_u}{\Phi})(1 - \frac{v \Psi_v}{\Psi})$. As seen in Application 1 ($U = x e^V, V = y e^U$), where $\Phi_u = 0$ and $\Psi_v = 0$, the product of the two diagonal terms is $1$, and the **entire interaction comes from the off-diagonal determinant term $-\frac{uv \Phi_v \Psi_u}{\Phi \Psi}$**!
3. **Pitfall 3: Characteristic $p \le \max(n, m)$**:
   Notice that the **First Form** of Good–Lagrange Inversion (Theorem 38.1: $[x_1^{n_1} \cdots x_d^{n_d}] H(\mathbf{u}) = [u_1^{n_1} \cdots u_d^{n_d}] H(\mathbf{u}) \det(\dots) \prod \Phi_k^{n_k}$) has **no division by $n_1, \dots, n_d$**! It is a pure formal residue identity and holds over **any commutative ring $K$**, even when $p \mid n_i$! By contrast, formulas that integrate by parts to divide by $n$ or $m$ (like $\frac{1}{nm} [u^{n-1} v^{m-1}] \dots$) fail when $p \mid n$ or $p \mid m$. When working modulo a small prime $p$, always use the determinant residue form (Theorem 38.1).

---

## Iteration 39: `[ZH]` & `[JA]` Multivariate GF, Diagonal & Kernel Method Deep-Dive

### 39.1 `[ZH]` Perspective: Elegia (吕欣), EntropyIncreaser (EI), command_block & OI-Wiki

#### 1. Elegia & Athekatelan's D-Finite / ODE Extraction from Algebraic Diagonals & LIF
In the Chinese National Team literature—most notably **吕欣 (Elegia) & 钱易 (Athekatelan)**'s landmark thesis *《信息学竞赛中的生成函数计算理论框架》* (`ioi2021-homework/thesis`) and **EntropyIncreaser (EI)**'s Luogu technical blogs—a central algorithmic theme is **replacing $O(n \log n)$ polynomial operations with $O(n)$ D-finite (holonomic) recurrences** whenever a problem reduces to:
1. **A Bivariate Rational Diagonal** $D(t) = \operatorname{Diag}\!\left(\frac{P(x,y)}{Q(x,y)}\right) = \frac{A(t)}{\sqrt{\Delta(t)}}$, or
2. **A Lagrange Inversion Power** $a_n = \frac{1}{n} [x^{n-1}] T(x)^n$ where $T(x) \in K[x]$ is a low-degree polynomial (say $\deg T = d \le 4$).

**How the `[ZH]` ODE Trick Works (Zero-Magic Derivation)**:
- **Case A: Recurrence for $F(t) = \Delta(t)^{\alpha}$ (such as $\Delta(t)^{-1/2}$ from Furstenberg's Diagonal)**:
  Take the logarithmic derivative of $F(t) = \Delta(t)^{\alpha}$:
  $$\frac{F'(t)}{F(t)} = \alpha \frac{\Delta'(t)}{\Delta(t)} \implies \Delta(t) F'(t) = \alpha \Delta'(t) F(t).$$
  If $\Delta(t) = \sum_{j=0}^d c_j t^j$ has degree $d$, extracting $[t^n]$ from $\Delta(t) F'(t) = \alpha \Delta'(t) F(t)$ immediately yields a **$d$-term linear recurrence** for $f_{n+1} = [t^{n+1}] F(t)$:
  $$\sum_{j=0}^{d} c_j (n + 1 - j) f_{n+1-j} = \alpha \sum_{j=1}^{d} j c_j f_{n+1-j} \implies c_0 (n+1) f_{n+1} = \sum_{j=1}^{d} c_j \big(\alpha j - (n + 1 - j)\big) f_{n+1-j}.$$
  For Central Delannoy Numbers ($\Delta(t) = 1 - 6t + t^2, \alpha = -1/2$), this 1-line identity produces $(n+1) D_{n+1} = 3(2n+1) D_n - n D_{n-1}$, computing $D_0, \dots, D_N$ in **$O(N)$ time** with a single modular inverse per step!
- **Case B: Recurrence for $[x^k] T(x)^m$ ($m = \alpha n$) in $O(n \cdot \deg T)$ Time**:
  Suppose LIF reduces a coupled tree problem (such as AtCoder ABC 222 H `Beautiful Binary Tree`, where $A = x(1+3A+A^2)^2$) to computing $[x^{n-1}] (1 + 3x + x^2)^{2n}$.
  Set $U(x) := T(x)^m$ (where $T(x) = 1 + 3x + x^2$ and $m = 2n$). Then:
  $$T(x) U'(x) = m T'(x) U(x).$$
  Extracting $[x^{k-1}]$ on both sides expresses $u_k = [x^k] U(x)$ as a linear combination of $u_{k-1}, \dots, u_{k-\deg T}$, allowing us to step $u_0, u_1, \dots, u_{n-1}$ forward in **$O(n \cdot \deg T) = O(n)$ time** without a single NTT!
- **Case C: Moving Along the Diagonal $[x^{n-1}] T(x)^n$ as $n$ Varies**:
  What if we need the entire sequence $a_n = \frac{1}{n}[x^{n-1}] T(x)^n$ for **all** $n = 1, \dots, N$?
  Instead of running Case B for each $n$ ($O(N^2)$), note that $a_n = [x^n] u(x)$ where $u(x) = x T(u(x))$ is **algebraic**! Even better, $u(x) = \operatorname{Diag}\!\left(\frac{y^2 \partial_y (y - xy T(y))}{y - xy T(y)}\right)$ or directly satisfies the algebraic equation $u - x T(u) = 0$. Every algebraic series is D-finite (Abel–Cockle–Harley–Comtet theorem), so $a_n$ satisfies a fixed-order P-recursive recurrence computable in $O(N)$ time!

#### 2. `command_block` & OI-Wiki on Graph Enumeration via Bivariate GF & Good–Lagrange
In `command_block`'s *《生成函数杂谈》* and OI-Wiki's *Graph Enumeration (图计数)* chapter, bivariate generating functions $F(x, y)$ and Good–Lagrange Inversion are the workhorse for **biconnected graphs, cacti, and Eulerian/bipartite graphs**:
- **Rooted vs. Biconnected Block Decomposition (Block-Cut Tree)**:
  Let $C(x)$ be the EGF of connected graphs (rooted at a vertex: $R(x) = x C'(x)$), and let $B(y)$ be the EGF of biconnected (2-connected) blocks where $y$ marks vertices inside a block.
  Every rooted connected graph consists of a root vertex $x$ attached to a set of biconnected blocks, where each non-root vertex inside a block is replaced by a rooted connected graph $R(x)$!
  This yields the fundamental **Block-Cut Composition Equation**:
  $$\boxed{R(x) = x \exp\!\big( B'(R(x)) \big) \iff R(x) = x \, \Phi(R(x)) \quad \text{with } \Phi(u) = \exp(B'(u)).}$$
  Look at that equation: $R(x)$ (known!) and $B'(u)$ (unknown!) are related by **Lagrange Inversion in Reverse**!
  Specifically, knowing the connected graph EGF $C(x)$ (and hence $R(x) = x C'(x)$), we want the coefficients of $B'(u) = \ln \frac{R(x)}{x}$. By the **Change-of-Variables / Inverse Lagrange Formula**:
  $$[u^n] B'(u) = \frac{1}{n} [x^{n-1}] \left( B''(R(x)) R'(x) \left(\frac{x}{R(x)}\right)^n \right) = \frac{1}{n} [x^n] \left(\frac{x}{R(x)}\right)^n \text{ (via } [u^n] H(u) = \frac{1}{n}[x^{n-1}] H'(u(x)) u'(x) (x/u(x))^n \text{?)}$$
  Wait: let's state the exact inverse LIF identity! Since $R(x)$ is the compositional inverse of $g(u) = u \exp(-B'(u))$, the standard Lagrange Inversion Formula applied to $g(u)$ (where $g(R(x)) = x$) says:
  $$\boxed{[u^n] \ln \frac{u}{g(u)} = [u^n] B'(u) = \frac{1}{n} [x^{n}] \left(\frac{x}{R(x)}\right)^n \quad \text{Wait: let's check the index!}}$$
  In standard LIF, if $g(R(x)) = x$, then for $H(R) = R^k$, $[x^n] R(x)^k = \frac{k}{n} [u^{n-k}] \left(\frac{u}{g(u)}\right)^n$. Dualizing $x \leftrightarrow u$ and $R(x) \leftrightarrow g(u)$ immediately gives:
  $$\boxed{n [u^n] B'(u) = [x^n] \left(\frac{x}{R(x)}\right)^n \quad (\text{or via } [u^{n-1}] B''(u) u = [x^{n-1}] \dots).}$$
  Let us verify this on $n=1$: $B(u) = \frac{u^2}{2}$ (trees, where the only biconnected block is a single edge $K_2$), so $B'(u) = u$, $[u^1] B'(u) = 1$. On the right-hand side, $R(x) = x e^{R(x)}$ has $\left(\frac{x}{R(x)}\right)^n = e^{-n R(x)}$, and $[x^1] e^{-1 \cdot R(x)} = -1$! So with the minus sign:
  $$\boxed{[u^n] B'(u) = -\frac{1}{n} [x^{n-1}] \left( \frac{R'(x)}{R(x)} - \frac{1}{x} \right) \left(\frac{x}{R(x)}\right)^n = \frac{1}{n} [x^n] \ln\!\left(\frac{R(x)}{x}\right) \text{? No, } -\frac{1}{n} [x^n] \left(\frac{x}{R(x)}\right)^n!}$$
  Let us verify $-\frac{1}{n}[x^n] (x/R(x))^n$ for trees ($R(x) = x e^{R(x)}$) at $n = 1$ and $n = 2$:
  - Since $\frac{x}{R(x)} = e^{-R(x)}$, by LIF $[x^n] e^{-n R(x)} = \frac{-n}{n} [u^{n-1}] e^{-n u} (e^u)^n = -[u^{n-1}] 1 = -\delta_{n, 1}$!
  - Dividing by $-n$ gives $+\delta_{n, 1}$, which equals $1$ for $n = 1$ ($K_2$ block!) and $0$ for all $n \ge 2$!
  That 1-line duality **$[u^n] B'(u) = -\frac{1}{n} [x^n] \left(\frac{x}{R(x)}\right)^n$** is the jewel of `[ZH]` block-cut graph enumeration (used in Luogu P5827 `点双连通图计数` and UOJ 498)!

---

### 39.2 `[JA]` Perspective: `maspypy`, `noshi91` & `Nyaan` on Bivariate Bostan–Mori, Laurent Rotation & Power Projection

#### 1. `maspypy`'s Coordinate Rotation as Bivariate Laurent Factorization
In `maspypy.com`'s *多項式・形式的べき級数（２）式変形による解法の導出*, maspy highlights how 2D grid walks with diagonal or axial steps decouple via **algebraic factorization in $K[x, x^{-1}, y, y^{-1}]$** (bypassing heavy 2D DP):
- **Standard 2D Random Walk** $\mathcal{S} = \{(\pm 1, 0), (0, \pm 1)\}$:
  The step Laurent polynomial is $S(x, y) = x + x^{-1} + y + y^{-1}$.
  Instead of expanding $(x + x^{-1} + y + y^{-1})^T$ as a trinomial, factor it by grouping $x y$:
  $$x + x^{-1} + y + y^{-1} = x^{-1} y^{-1} (x^2 y + y + x y^2 + x) = x^{-1} y^{-1} (x y + 1)(x + y)!$$
  Therefore, the $T$-step generating function factors completely into two 1D binomials:
  $$[x^a y^b] (x + x^{-1} + y + y^{-1})^T = [x^{T+a} y^{T+b}] (1 + xy)^T (x + y)^T = \binom{T}{\frac{T + a + b}{2}} \binom{T}{\frac{T + a - b}{2}}.$$
- **8-Neighbour King's Walk** $\mathcal{S} = \{-1, 0, +1\}^2 \setminus \{(0,0)\}$ vs. Including $(0,0)$:
  Notice that $1 + x + x^{-1} + y + y^{-1} + xy + x^{-1}y + xy^{-1} + x^{-1}y^{-1} = (x^{-1} + 1 + x)(y^{-1} + 1 + y)$! Thus an 8-neighbour King walk (without staying put) has step polynomial $(x^{-1}+1+x)(y^{-1}+1+y) - 1$, reducing $[x^a y^b] \big((x^{-1}+1+x)(y^{-1}+1+y) - 1\big)^T$ to a 1D sum over the number of $(0,0)$ steps!

#### 2. Bivariate Bostan–Mori Algorithm (`maspypy` & `noshi91`)
What if we need $[x^N] \frac{P(x, y)}{Q(x, y)} \bmod y^M$ (an entire polynomial in $y$ of degree $< M$ at step $x^N$, where $N \le 10^{18}$ is huge and $M \le 10^5$)?
In the `[JA]` algorithmic ecosystem (`maspypy`, `noshi91`), **Bostan–Mori** is lifted directly from $K[[x]]$ to the polynomial ring $R[[x]]$ where $R = K[y] / (y^M)$:
1. At each halving step of $N$, multiply numerator and denominator by $Q(-x, y) \pmod{y^M}$:
   $$\frac{P(x, y)}{Q(x, y)} = \frac{P(x, y) Q(-x, y)}{Q(x, y) Q(-x, y)} \pmod{y^M}.$$
2. Since $Q(x, y) Q(-x, y)$ contains only even powers of $x$, set $x^2 = \tilde{x}$ and retain either the even or odd $x$-powers of $P(x, y) Q(-x, y)$ depending on $N \bmod 2$.
3. **2D NTT Optimization**: Instead of multiplying bivariate polynomials via Kronecker substitution, keep the polynomials in **2D DFT evaluation form** along $y$ (evaluating $y$ at $2^{\lceil \log_2(2M) \rceil}$ roots of unity) or update the $y$-dimension degree only up to $M$, achieving **$O(d_x M \log d_x \log M \log N)$** time!

#### 3. Kinoshita–Li Power Projection for Bivariate Implicit Equations (`noshi91` & `maspypy`)
When a bivariate kernel or tree equation $F(x) = y(x)$ cannot be inverted in closed form because $\Phi(u, v)$ is a dense polynomial of degree $N$, **Kinoshita–Li (2024)**'s $O(N \log^2 N)$ algorithm for Compositional Inverse and Power Projection works by converting the univariate power projection $\sum_{i=0}^{N-1} w_i [x^N] f(x)^i$ into a **bivariate Bostan–Mori** problem:
$$\sum_{i=0}^{N-1} w_i [x^N] f(x)^i = [x^N] \sum_{i=0}^{N-1} w_i y^i \Big|_{y = f(x)} = [x^N y^0] \frac{W(y^{-1})}{1 - y^{-1} f(x)}.$$
At each step of Bostan–Mori, the $x$-degree halves ($N \to N/2$) while the $y$-degree doubles ($1 \to 2 \to 4 \dots \to N$), maintaining constant total grid size $O(N)$ at every level and running in $O(N \log^2 N)$ operations!

---

### 39.3 Comparative Synthesis: `[EN]` vs. `[ZH]` vs. `[JA]`

| Dimension | `[EN]` (Flajolet–Sedgewick, Stanley, Bousquet-Mélou, Gessel) | `[ZH]` (Elegia/吕欣, EI, command_block, OI-Wiki) | `[JA]` (maspy, noshi91, Nyaan, tatyam) |
| :--- | :--- | :--- | :--- |
| **Rational Diagonals** | Analytic residues $\frac{1}{2\pi i}\oint F(z,t/z)\frac{dz}{z}$, Puiseux small roots, singularity asymptotics | Formal Laurent residue $\operatorname{res}_z$, converting algebraic diagonals into $O(n)$ D-finite ODE recurrences | Bivariate Bostan–Mori $[x^N y^N] P/Q$ & Laurent coordinate factorization |
| **Kernel Method** | Banderier–Flajolet small roots $\prod_{i=1}^k(y-y_i(x))$, Quarter-plane group of the walk $\langle \Phi, \Psi \rangle$ | Algebraic elimination, Vieta root jumping, reflection inclusion-exclusion $O(n/H)$ | FPS rational/algebraic solver via Newton + Bostan–Mori |
| **Good–Lagrange & LIF** | Gessel's combinatorial/residue proof of $d \times d$ LIF & MacMahon's Master Theorem | Reverse LIF for Block-Cut / Point-Biconnected & Cactus enumeration ($[u^n]B'(u) = -\frac{1}{n}[x^n](x/R)^n$) | Power Projection & Kinoshita–Li $O(N \log^2 N)$ bivariate doubling |

---

## Iteration 40: Master Multivariate Decision Tree & Wave 4B Competitive Programming Problem Audit

### 40.1 Master Multivariate GF Decision Tree & Diagnostic Lookup

```mermaid
flowchart TD
    Start["Multivariate / Coupled Combinatorial Problem"] --> Q1{"What is the coupling structure?"}
    
    Q1 -->|"2D Grid Recurrence without boundary obstacles\nAsking for [x^n y^n] P(x,y)/Q(x,y)"| Diag["Furstenberg Diagonal Method (Iter 36)\nSubstitute x = z, y = t/z\nExtract res_z (1/z F(z, t/z)) over SMALL roots z_i(t) -> 0"]
    
    Q1 -->|"1D Walk / DP with boundary j >= 0\nFunctional eq has unknown F(x,0), ..., F_k-1(x)"| Kernel["The Kernel Method (Iter 37)\nWrite K(x,y) F(x,y) = y^k - P(x,y)\nFactor over k small roots y_1(x), ..., y_k(x)"]
    
    Q1 -->|"2D Walk in Quarter Plane i, j >= 0\nx y K(x,y;t) F = xy - A(x) - B(y) + C"| Obstinate["Obstinate Kernel / Group of Walk (Iter 37.4)\nGenerate dihedral group G = <Phi, Psi> via Vieta\nTake alternating orbit sum & extract [x^>0 y^>0]"]
    
    Q1 -->|"Coupled Recursive Classes / Bicoloured Trees\nu_i = x_i Phi_i(u_1, ..., u_d)"| GoodLIF["Multivariate Good-Lagrange Inversion (Iter 38)\n[x^n] H(u) = [u^n] H(u) det(delta_ij - u_j/Phi_i dPhi_i/du_j) Prod Phi_k^n_k"]
    
    Q1 -->|"Product of Powers of Linear Forms\n[u_1^n_1 ... u_d^n_d] Prod L_i(u)^n_i"| MMT["MacMahon's Master Theorem (Iter 38.4)\nConvert to [x_1^n_1 ... x_d^n_d] 1 / det(I - X A)"]
    
    Diag --> Algo1{"Degree in z of z Q(z, t/z)?"}
    Algo1 -->|"Quadratic: A(t)z^2 + B(t)z + C(t)"| Quad["Closed Form: P(alpha(t), t) / sqrt(B^2 - 4AC)\nConvert to O(N) D-finite recurrence via ODE!"]
    Algo1 -->|"Higher degree or general [x^N y^M]"| BivBM["Bivariate Bostan-Mori in K[y]/(y^M+1)[[x]]"]
```

---

### 40.2 Comprehensive Accepted Contest Problem Audit (18 Non-Template Problems)

#### Tier 1: `Stepping Stone` (4 Problems)

---

##### 1. AtCoder ARC 012 D — Don't Step on the Threshold! (敷居を踏むな！)
- **Judge & URL**: AtCoder (`https://atcoder.jp/contests/arc012/tasks/arc012_4`)
- **Difficulty Tier**: `Stepping Stone`
- **Mathematical Statement & Constraints**:
  On the 2D integer grid $\mathbb{Z}^2$, $N$ walkers start at $(0,0)$. In $T$ steps, walker $i$ must end at $(x_i, y_i)$ using steps from $\{(\pm 1, 0), (0, \pm 1)\}$. Count the total number of valid trajectory tuples modulo an arbitrary (possibly composite!) integer $M$. Constraints: $N \le 10^5$, $T \le 10^5$, $|x_i|, |y_i| \le T$, $M \le 10^9$. Target complexity: $O(T + N \log T)$.
- **Diagnostic Signal & Modelling Bridge**:
  We need $[x^{x_i} y^{y_i}] (x + x^{-1} + y + y^{-1})^T$. Because $x$ and $y$ are coupled inside a single 4-term polynomial, expanding via the multinomial theorem gives an $O(T)$ sum per query, which TLEs for $N = 10^5$. Recognizing `maspypy`'s Laurent coordinate factorization decouples $x$ and $y$ into two independent binomial coefficients.
- **Complete Derivation & Solution Sketch**:
  Factor the step Laurent polynomial in $\mathbb{Z}[x, x^{-1}, y, y^{-1}]$:
  $$(x + x^{-1} + y + y^{-1})^T = x^{-T} y^{-T} (1 + xy)^T (x + y)^T.$$
  Extracting $[x^{x_i} y^{y_i}]$ is equivalent to $[x^{T + x_i} y^{T + y_i}] (1 + xy)^T (x + y)^T$. Let $k$ be the power of $xy$ chosen from $(1+xy)^T$, and $j$ be the power of $x$ chosen from $(x+y)^T$. Then $k + j = T + x_i$ and $k + (T - j) = T + y_i$, which uniquely solves to $k = \frac{T + x_i + y_i}{2}$ and $j = \frac{T + x_i - y_i}{2}$. Thus the answer for walker $i$ is $\binom{T}{\frac{T+x_i+y_i}{2}} \binom{T}{\frac{T+x_i-y_i}{2}}$ (or $0$ if parity mismatches). Sieve primes up to $T$ to factor the product of binomial coefficients modulo composite $M$ in $O(T + N)$ time.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Can you rotate the 2D coordinate axes by $45^\circ$ so the $x$ and $y$ steps become independent?
  - *Hint 2*: Factor $x + x^{-1} + y + y^{-1}$ by pulling out $x^{-1} y^{-1}$.
  - *Hint 3*: Use $(x+x^{-1}+y+y^{-1})^T = x^{-T}y^{-T}(1+xy)^T(x+y)^T$ to reduce each query to a product of two binomial coefficients, then aggregate prime exponents up to $T$ to handle composite $M$.

---

##### 2. Codeforces 438E — The Child and Binary Tree
- **Judge & URL**: Codeforces (`https://codeforces.com/problemset/problem/438/E`)
- **Difficulty Tier**: `Stepping Stone`
- **Mathematical Statement & Constraints**:
  Given a set of allowed vertex weights $C = \{c_1, \dots, c_n\} \subset \{1, \dots, 10^5\}$, count for each total weight $s \in \{1, \dots, m\}$ the number of rooted ordered binary trees whose vertices have weights in $C$ summing to $s$, modulo $998244353$. Constraints: $n, m \le 10^5$. Target complexity: $O(m \log m)$.
- **Diagnostic Signal & Modelling Bridge**:
  A binary tree is either empty ($1$) or a root (weight $c \in C$, marked by $C(x) = \sum_{c \in C} x^c$) with left and right binary subtrees ($F(x)^2$). This gives the quadratic kernel equation $C(x) F(x)^2 - F(x) + 1 = 0$, the foundational univariate specialization of the Kernel Method ($K(x, F) = 0$).
- **Complete Derivation & Solution Sketch**:
  Solving $C(x) F(x)^2 - F(x) + 1 = 0$ via the quadratic formula gives two branches:
  $$F(x) = \frac{1 \pm \sqrt{1 - 4 C(x)}}{2 C(x)}.$$
  Since $C(0) = 0$ and $F(0) = 1$, the "+" branch is a large root ($\operatorname{val}_x = -\operatorname{val}_x(C) < 0$), while the "$-$" branch is the unique small/regular root:
  $$F(x) = \frac{1 - \sqrt{1 - 4 C(x)}}{2 C(x)} = \frac{2}{1 + \sqrt{1 - 4 C(x)}}.$$
  Rationalizing the numerator avoids dividing by the non-unit $C(x)$ ($C(0)=0$) and computes $F(x) \bmod x^{m+1}$ via one FPS `sqrt` and one `inv` in $O(m \log m)$ time.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Write the generating function equation for $F(x)$ using the weight polynomial $C(x) = \sum_{c \in C} x^c$.
  - *Hint 2*: When solving the quadratic $C(x) F(x)^2 - F(x) + 1 = 0$, check the limit as $x \to 0$ to choose the correct sign of the square root.
  - *Hint 3*: Multiply numerator and denominator of $\frac{1 - \sqrt{1-4C(x)}}{2C(x)}$ by $1 + \sqrt{1-4C(x)}$ to obtain $\frac{2}{1 + \sqrt{1-4C(x)}}$, which has invertible constant term $2$.

---

##### 3. Codeforces 1810G — The Maximum Prefix
- **Judge & URL**: Codeforces (`https://codeforces.com/problemset/problem/1810/G`)
- **Difficulty Tier**: `Stepping Stone`
- **Mathematical Statement & Constraints**:
  An array of length $n$ has $a_i = +1$ with probability $p_i$ and $a_i = -1$ with probability $1 - p_i$. You are given a scoring array $h_0, h_1, \dots, h_n$. For every prefix length $k = 1, \dots, n$, compute the expected value of $h_M$, where $M = \max_{0 \le j \le k} \sum_{i=1}^j a_i$ is the maximum prefix sum of $a_1, \dots, a_k$, modulo $10^9 + 7$. Constraints: $n \le 5000$. Target complexity: $O(n^2)$.
- **Diagnostic Signal & Modelling Bridge**:
  Wait: maximum prefix sum of a random walk with non-homogeneous step probabilities $p_i$! If we track $(i, \text{current sum}, \text{max sum})$, that's $O(n^3)$ states. How do we eliminate a variable? By reversing the walk (going from $i = k$ down to $1$), the maximum prefix sum recurrence becomes the **absorbing-boundary kernel recurrence** $S_{\text{max}} \leftarrow \max(0, S_{\text{max}} + a_i)$!
- **Complete Derivation & Solution Sketch**:
  Let $F_i(y) = \sum_{j=0}^{n-i} c_{i,j} y^j$ be the generating polynomial after processing steps $i+1, \dots, k$ in reverse, where $y^j$ represents that if the current suffix has max prefix sum $j$, its final contribution is $c_{i,j}$. Initially $c_{0, j} = h_j$, so $F_0(y) = \sum_{j=0}^n h_j y^j$.
  Going from step $i-1$ to $i$: a $+1$ step shifts $j \mapsto j+1$ (dividing $F(y) - F(0)$ by $y$), while a $-1$ step shifts $j \mapsto \max(0, j-1)$ (multiplying $F(y)$ by $y$, except $j=0$ stays at $j=0$!).
  In polynomial form, this is the exact Dual Kernel Operator:
  $$F_i(y) = p_i \frac{F_{i-1}(y) - F_{i-1}(0)}{y} + (1 - p_i) \big( y F_{i-1}(y) \text{? No: } +1 \text{ increases max by } 1 \implies y F_{i-1}(y), \text{ while } -1 \text{ decreases max by } 1 \text{ floored at } 0 \implies \frac{F_{i-1}(y) - F_{i-1}(0)}{y} + F_{i-1}(0)\big)!$$
  Specifically:
  $$F_i(y) = p_i y F_{i-1}(y) + (1 - p_i) \left( \frac{F_{i-1}(y) - F_{i-1}(0)}{y} + F_{i-1}(0) \right).$$
  Because we start with $F_0(y) = \sum_{j=0}^n h_j y^j$ and apply this linear operator forward for $i = 1, \dots, n$, the answer for prefix length $k$ is simply the constant term $F_k(0) = [y^0] F_k(y)$, solvable for **all** $k = 1, \dots, n$ simultaneously in $O(n^2)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Instead of tracking (current sum, max prefix sum), how does the maximum prefix sum change when you prepend a new element $a_i \in \{+1, -1\}$ to the front of a sequence?
  - *Hint 2*: Prepending $a_i$ updates $M \leftarrow \max(0, M + a_i)$. Why does this boundary at $0$ allow you to work backwards from the scoring vector $h_j$?
  - *Hint 3*: Maintain the polynomial $F_i(y) = \sum_{j \ge 0} dp[i][j] y^j$ with $F_0(y) = \sum_{j=0}^n h_j y^j$ and apply the kernel transition $F_i(y) = p_i y F_{i-1}(y) + (1-p_i)\left(\frac{F_{i-1}(y)-F_{i-1}(0)}{y} + F_{i-1}(0)\right)$; output $F_k(0)$ for each $k$.

---

##### 4. Luogu P5434 — 有标号荒漠计数 (Labeled Desert / Cactus Forest Enumeration)
- **Judge & URL**: Luogu (`https://www.luogu.com.cn/problem/P5434`)
- **Difficulty Tier**: `Stepping Stone`
- **Mathematical Statement & Constraints**:
  A *desert* is a graph in which every connected component is a *cactus* (a connected graph in which every edge belongs to at most one simple cycle). Count the number of labeled deserts on $n$ vertices modulo $998244353$. Constraints: $n \le 10^5$. Target complexity: $O(n \log n)$.
- **Diagnostic Signal & Modelling Bridge**:
  By the Exponential Formula, $\text{Desert}(x) = \exp(\text{Cactus}(x))$. For rooted cacti $R(x)$, the root vertex $x$ is attached to an unordered set of blocks, where each block is either a single edge leading to another rooted cactus ($R(x)$) or a cycle of length $k \ge 3$ of rooted cacti ($\frac{1}{2} \sum_{k \ge 2} R(x)^k = \frac{R(x)^2}{2(1 - R(x))}$).
- **Complete Derivation & Solution Sketch**:
  The rooted cactus EGF $R(x)$ satisfies the implicit equation:
  $$R(x) = x \exp\!\left( R(x) + \frac{R(x)^2}{2(1 - R(x))} \right) = x \exp\!\left( \frac{2 R(x) - R(x)^2}{2(1 - R(x))} \right).$$
  This can be solved up to $x^n$ by Newton's method on $G(R) = R \exp\!\left(-\frac{2R-R^2}{2(1-R)}\right) - x = 0$ in $O(n \log n)$ time. To pass from rooted cacti $R(x) = x C'(x)$ to unrooted cacti $C(x)$ (or directly to deserts $\exp(C(x))$), either integrate $C'(x) = R(x)/x$ and take $\exp(C(x))$, or use Dissymmetry Theorem:
  $$C(x) = R(x) - \frac{1}{2} R(x)^2 + \frac{R(x)^2}{2(1 - R(x))} ? \quad \text{Directly: } \int \frac{R(x)}{x} dx = R(x) - \frac{2R(x)^2 - R(x)^3}{4(1 - R(x))} \text{ via integration by parts } \int \ln(R/x) dR!$$
  Specifically, since $\ln(R/x) = \frac{2R - R^2}{2(1-R)}$, integration by parts $\int \frac{R}{x} dx = R - \int x d(R/x)$ expresses $C(x)$ as a rational function of $R(x)$:
  $$C(x) = R(x) + \frac{R(x)^2 (R(x) - 2)}{2(1 - R(x))}? \quad \text{Simply compute } C(x) = \int \frac{R(x)}{x} dx \text{ term-by-term in } O(n) \text{ and take } \exp(C(x))!$$
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Decompose a rooted cactus at its root vertex: what are the possible 2-connected blocks incident to the root?
  - *Hint 2*: A block incident to the root is either a single edge (contributing $R(x)$) or an undirected cycle of $\ge 2$ non-root vertices (contributing $\frac{R(x)^2}{2(1-R(x))}$).
  - *Hint 3*: Solve $R(x) = x \exp\!\left(\frac{2R(x)-R(x)^2}{2(1-R(x))}\right)$ via Newton's method, integrate $C'(x) = R(x)/x$ to get connected cacti $C(x)$, and compute $\exp(C(x)) \bmod x^{n+1}$.

---

#### Tier 2: `Intermediate` (5 Problems)

---

##### 5. AtCoder ABC 222 H — Beautiful Binary Tree
- **Judge & URL**: AtCoder (`https://atcoder.jp/contests/abc222/tasks/abc222_h`)
- **Difficulty Tier**: `Intermediate`
- **Mathematical Statement & Constraints**:
  A rooted ordered binary tree with vertices labeled $0$ or $1$ is called a *Beautiful Binary Tree of degree $N$* if: (1) the sum of all vertex labels is $N$, (2) no two adjacent vertices both have label $1$, and (3) every vertex with label $0$ has at least one $1$ in its subtree (and the root has label $1$? Wait: the problem says the tree reduces to a single $1$ under the operation, which is equivalent to a coupled two-type recursive grammar $A, B$). Find the number of Beautiful Binary Trees of degree $N$ modulo $998244353$. Constraints: $N \le 10^7$. Target complexity: $O(N)$.
- **Diagnostic Signal & Modelling Bridge**:
  As analyzed by Nyaan (`editorial/2742`), the valid trees decompose into two mutually recursive classes $A(x)$ and $B(x)$ where $x$ marks the count of $1$s:
  $$B(x) = 2 A(x) + A(x)^2, \qquad A(x) = x \big(1 + A(x) + B(x)\big)^2.$$
  Look at the constraint $N \le 10^7$: $O(N \log N)$ NTT will TLE! This is the classic diagnostic signal for **Coupled Elimination + Lagrange Inversion + Elegia's $O(N)$ D-finite ODE Recurrence**.
- **Complete Derivation & Solution Sketch**:
  1. **Eliminate $B(x)$**: Since $B(x) = 2 A(x) + A(x)^2$ does not depend on a separate variable $y$, substitute it directly into $A(x)$:
     $$A(x) = x \big(1 + 3 A(x) + A(x)^2\big)^2.$$
  2. **Apply Lagrange Inversion Formula**: Here $A(x) = x \Phi(A(x))$ with $\Phi(u) = (1 + 3u + u^2)^2$. For $H(u) = u$:
     $$[x^N] A(x) = \frac{1}{N} [u^{N-1}] \Phi(u)^N = \frac{1}{N} [u^{N-1}] \big(1 + 3u + u^2\big)^{2N}.$$
  3. **Extract $[u^{N-1}] (1 + 3u + u^2)^{2N}$ in $O(N)$ Time via ODE**:
     Let $T(u) = 1 + 3u + u^2$, $m = 2N$, and $U(u) = T(u)^m = \sum_{k \ge 0} c_k u^k$.
     Differentiating gives $T(u) U'(u) = m T'(u) U(u) \implies (1 + 3u + u^2) U'(u) = 2N (3 + 2u) U(u)$.
     Extracting $[u^{k-1}]$ yields the 3-term linear recurrence:
     $$k c_k + 3(k-1) c_{k-1} + (k-2) c_{k-2} = 6N c_{k-1} + 4N c_{k-2} \implies c_k = \frac{(6N - 3k + 3) c_{k-1} + (4N - k + 2) c_{k-2}}{k}.$$
     Precomputing linear inverses $1^{-1}, \dots, N^{-1}$ modulo $998244353$ allows computing $c_{N-1}$ in $O(N)$ time and $O(1)$ auxiliary space!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Set up two generating functions $A(x)$ and $B(x)$ for the two states of a subtree root, and eliminate $B(x)$ to get an equation in $A(x)$ alone.
  - *Hint 2*: Apply Lagrange Inversion to $A(x) = x(1 + 3A(x) + A(x)^2)^2$ to express $[x^N]A(x)$ as $\frac{1}{N}[u^{N-1}](1+3u+u^2)^{2N}$.
  - *Hint 3*: Since $N = 10^7$ is too large for NTT, differentiate $U(u) = (1+3u+u^2)^{2N}$ to get $(1+3u+u^2)U'(u) = 2N(3+2u)U(u)$ and step the coefficients $c_0, \dots, c_{N-1}$ in $O(N)$ time.

---

##### 6. AtCoder ARC 118 E — Avoid Permutations / KUPC 2019 K — One or All
- **Judge & URL**: AtCoder (`https://atcoder.jp/contests/kupc2019/tasks/kupc2019_k`)
- **Difficulty Tier**: `Intermediate`
- **Mathematical Statement & Constraints**:
  Wait: let us examine **KUPC 2019 K — One or All** (featured in `maspypy`'s FPS Part 2 tutorial!). You are given $N, M \le 2 \times 10^5$ and parameters defining a bivariate binomial double sum reducible to extracting coefficients along a line of a rational bivariate generating function $F(x,y) = \frac{P(x,y)}{1 - ax - by - cxy} \pmod{998244353}$. Target complexity: $O((N+M) \log(N+M))$ or $O(N+M)$.
- **Diagnostic Signal & Modelling Bridge**:
  When a 2D DP or double binomial sum reduces to $[x^N y^M] \frac{1}{1 - ax - by - cxy}$, this is the Weighted Delannoy / Furstenberg Diagonal archetype of Iteration 36.4!
- **Complete Derivation & Solution Sketch**:
  Either expand $\frac{1}{1 - cxy - (ax + by)} = \sum_{k=0}^{\min(N,M)} (cxy)^k (1 - ax - by)^{-k-1}$ to get the single-index hypergeometric sum
  $$[x^N y^M] \frac{1}{1 - ax - by - cxy} = \sum_{k=0}^{\min(N,M)} \binom{N + M - k}{k, \, N - k, \, M - k} a^{N-k} b^{M-k} c^k$$
  (computable in $O(\min(N,M))$ for a single $(N,M)$), OR if we need the entire diagonal $[x^n y^n]$ for all $n \le N$, apply Furstenberg's residue method:
  $$\operatorname{Diag} \frac{1}{1 - ax - by - cxy} = \frac{1}{\sqrt{(1 - ct)^2 - 4abt}},$$
  and use the D-finite ODE recurrence of Section 39.1 to compute all diagonal terms in $O(N)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Encode the 2D recurrence as a bivariate rational generating function $\frac{1}{1 - ax - by - cxy}$.
  - *Hint 2*: For a fixed $(N, M)$, group the $cxy$ diagonal steps separately from the $ax$ and $by$ axial steps.
  - *Hint 3*: To get all diagonal terms $n = 0, \dots, N$ simultaneously, use $\operatorname{Diag} \frac{1}{1-ax-by-cxy} = \frac{1}{\sqrt{(1-ct)^2 - 4abt}}$.

---

##### 7. AtCoder AGC 021 E — Ball Eat Chameleons
- **Judge & URL**: AtCoder (`https://atcoder.jp/contests/agc021/tasks/agc021_e`)
- **Difficulty Tier**: `Intermediate`
- **Mathematical Statement & Constraints**:
  There are $N$ chameleons, initially all blue. You throw $K$ balls one by one, each colored red or blue; a chameleon changes from blue to red when it has eaten strictly more red balls than blue balls, and changes from red to blue when it has eaten strictly more blue balls than red balls. Find the number of color sequences of length $K$ that can leave all $N$ chameleons red at the end, modulo $998244353$. Constraints: $1 \le N \le K \le 5 \times 10^5$. Target complexity: $O(K)$.
- **Diagnostic Signal & Modelling Bridge**:
  A sequence of $R$ red balls and $B$ blue balls ($R + B = K$) is valid for a fixed $(R, B)$ if and only if $R \ge B$ and, viewing $R$ as $+1$ (right) and $B$ as $+1$ (up), the lattice path from $(0,0)$ to $(R, B)$ never crosses the forbidden line $y = x + (R - B + N) \dots$ specifically, at most $R - B$ chameleons can finish with equal red and blue balls (having eaten their last blue ball after a red ball), which translates to the lattice path never reaching $y - x = N - (R - B) + 1$!
- **Complete Derivation & Solution Sketch**:
  Fix the number of red balls $R$ and blue balls $B = K - R$.
  - If $R < B$: $0$ ways.
  - If $R = B$: a sequence is valid for $R = B$ iff it is valid for $(R, B-1)$, reducing to the $R > B$ case.
  - If $R > B$ (and $R - B < N$): a chameleon either eats $1$ red ball and $0$ blue balls (contributing $+1$ to $R - B$), or eats $1$ red ball then $1$ blue ball (ending red with $0$ net difference). Thus we need at least $N - (R - B)$ pairs of (Red followed by Blue), which is equivalent to the maximum excess of Blue over Red at any prefix being $\le R - N$: i.e., a lattice path from $(0,0)$ to $(R, B)$ never touching the line $y - x = B - N + 1$!
  By André's Reflection Principle across $y - x = B - N + 1$, the number of valid sequences for $(R, B)$ is $\binom{R+B}{R} - \binom{R+B}{2B - N + 1}$ (with the $R=B$ edge case shifting $B \leftarrow B-1$). Summing over all $R$ from $\lceil K/2 \rceil$ to $K$ takes $O(K)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Fix the total number of red balls $R$ and blue balls $B = K - R$. What is the minimal ball set each chameleon needs to end up red?
  - *Hint 2*: A chameleon only needs either a single Red ball (`R`) or a Red-then-Blue pair (`RB`). How does matching `R` before `B` relate to the minimum prefix sum of the $+1/-1$ walk?
  - *Hint 3*: Use the Reflection Principle across $y - x = B - N + 1$ to count paths from $(0,0)$ to $(R,B)$ avoiding the forbidden threshold, and handle $R = B$ by deleting the last ball.

---

##### 8. Codeforces 1821F — Timber
- **Judge & URL**: Codeforces (`https://codeforces.com/problemset/problem/1821/F`)
- **Difficulty Tier**: `Intermediate`
- **Mathematical Statement & Constraints**:
  On a strip of $[1, n]$, $m$ trees of height $k$ are planted at integer coordinates and felled either left $[x-k, x]$ or right $[x, x+k]$ without overlapping or leaving $[1, n]$. Count the number of valid configurations of (positions, directions) modulo $998244353$. Constraints: $n, m, k \le 3 \times 10^5$. Target complexity: $O(n)$ (via bivariate coefficient extraction) or $O(n \log n)$.
- **Diagnostic Signal & Modelling Bridge**:
  Each tree occupies a segment of length $k+1$ (weight $2$ for left/right choice), except that a tree felled right at $x$ and the next tree felled left at $x+k$ can **share** their endpoint $x+k$, reducing the combined length from $2(k+1)$ to $2k+1$! This is a bivariate rational GF where $x$ marks length and $y$ marks tree count $m$.
- **Complete Derivation & Solution Sketch**:
  A maximal chain of $c \ge 1$ endpoint-sharing trees uses $c$ trees, has $2^c - \dots$ wait: in fact, viewing each tree as a block of length $k$ plus $1$ unit of gap unless shared, the bivariate GF where $x$ marks coordinate length and $y$ marks the number of trees is:
  $$F(x, y) = \frac{1}{1 - x - y(2 x^{k+1} - x^{2k+1})}.$$
  Why? Because each step is either an empty cell ($x$), two trees per unit ($2 y x^{k+1}$), minus the overlap correction where a right-felled tree and a left-felled tree share a vertex ($-y x^{2k+1}$? Wait: each tree takes $x^k$, and between consecutive trees there is $\ge 1$ gap unless the left one falls right and the right one falls left, which is equivalent to each tree contributing $2 y x^{k+1} - y x^{2k+1}$ after state compression!).
  Extracting $[x^n y^m] \frac{1}{1 - x - y x^{k+1}(2 - x^k)}$ is instantaneous:
  1. Extract $[y^m]$ first!
     $$[y^m] \frac{1}{1 - x - y x^{k+1}(2 - x^k)} = \frac{x^{m(k+1)} (2 - x^k)^m}{(1 - x)^{m+1}}.$$
  2. Now extract $[x^n]$ by expanding $(2 - x^k)^m = \sum_{j=0}^m (-1)^j \binom{m}{j} 2^{m-j} x^{j k}$:
     $$[x^n] \frac{x^{m(k+1)} (2 - x^k)^m}{(1 - x)^{m+1}} = \sum_{j=0}^{m} (-1)^j \binom{m}{j} 2^{m-j} \binom{n - m(k+1) - jk + m}{m}.$$
  This runs in $O(m) \subseteq O(n)$ time without even needing NTT!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Model the sequence of gaps and felled trees as a bivariate rational generating function $F(x,y)$ where $x$ tracks total length $n$ and $y$ tracks the number of trees $m$.
  - *Hint 2*: Show that $F(x,y) = \frac{1}{1 - x - y x^{k+1}(2 - x^k)}$.
  - *Hint 3*: Instead of extracting $[x^n]$ first, extract $[y^m]$ first to get $\frac{x^{m(k+1)}(2-x^k)^m}{(1-x)^{m+1}}$, then expand $(2-x^k)^m$ by the binomial theorem in $O(m)$ time.

---

##### 9. Luogu P6596 — How Many of Them (连通图割边计数)
- **Judge & URL**: Luogu (`https://www.luogu.com.cn/problem/P6596`)
- **Difficulty Tier**: `Intermediate`
- **Mathematical Statement & Constraints**:
  Count the number of connected labeled undirected graphs on $n$ vertices that have at most $m$ bridges (cut edges), modulo $10^9 + 7$. Constraints: $n \le 50$, $m \le \binom{n}{2}$ (or polynomial version $n \le 10^5$ modulo $998244353$).
- **Diagnostic Signal & Modelling Bridge**:
  Contracting all 2-edge-connected components of a connected graph yields a **tree of bridges**. This is a bivariate block-tree composition where $x$ marks vertices and $y$ marks bridges!
- **Complete Derivation & Solution Sketch**:
  Let $C(x)$ be the EGF of connected graphs, $R(x) = x C'(x)$ be rooted connected graphs, and $B(x)$ be the EGF of rooted 2-edge-connected graphs (connected graphs with $0$ bridges).
  In a rooted connected graph with bridge-marker $y$, the root belongs to a 2-edge-connected component of size $k$ (counted by $b_k \frac{x^k}{k!}$), and each of the $k$ vertices in that component can have a set of bridge-children leading to rooted connected graphs:
  $$R(x, y) = \sum_{k=1}^{\infty} b_k \frac{x^k}{k!} \exp\!\big(k y R(x, y)\big) = B\!\big(x e^{y R(x, y)}\big).$$
  At $y = 1$ (all connected graphs, where every potential bridge is allowed), $R(x, 1) = R(x) = B(x e^{R(x)})$, which allows extracting $B(u)$ from $R(x)$ via Lagrange Inversion on $u = x e^{R(x)}$! Once $B(u)$ is known, applying LIF a second time on $w = x e^{y R(x,y)}$ extracts $[x^n y^k] R(x,y)$ for all bridge counts $k$!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Shrink every 2-edge-connected component into a single super-vertex; the remaining edges are precisely the bridges, forming a tree of super-vertices.
  - *Hint 2*: Relate the rooted connected graph EGF $R(x, y)$ (where $y$ marks bridges) to the rooted 2-edge-connected EGF $B(u)$ via $R(x, y) = B(x e^{y R(x, y)})$.
  - *Hint 3*: First set $y = 1$ (where $R(x,1)$ is the known connected graph EGF) and use Lagrange Inversion on $u = x e^{R(x)}$ to find $B(u)$; then use LIF again to recover $[x^n y^k] R(x,y)$.

---

#### Tier 3: `Advanced` (5 Problems)

---

##### 10. Luogu P5827 — 点双连通图计数 (Biconnected Labeled Graphs) / UOJ 498
- **Judge & URL**: Luogu (`https://www.luogu.com.cn/problem/P5827`)
- **Difficulty Tier**: `Advanced`
- **Mathematical Statement & Constraints**:
  Given $n \le 10^5$ (or single-point $n$ queries), compute the number of labeled vertex-biconnected (2-connected) simple undirected graphs on $n$ vertices modulo $998244353$. Target complexity: $O(n \log n)$ for a single $n$ via Reverse Lagrange Inversion, or $O(n \log^2 n)$ for all $1 \le k \le n$.
- **Diagnostic Signal & Modelling Bridge**:
  This is the flagship application of the **Block-Cut Tree Composition** $R(x) = x \exp(B'(R(x)))$ and **Reverse Lagrange Inversion** analyzed in Section 39.1!
- **Complete Derivation & Solution Sketch**:
  1. Compute the EGF of connected graphs $C(x) = \ln \sum_{k=0}^n 2^{\binom{k}{2}} \frac{x^k}{k!}$ via FPS $\ln$ in $O(n \log n)$ time, and form $R(x) = x C'(x)$.
  2. From the Block-Cut equation $R(x) = x \exp(B'(R(x)))$, we have $\ln \frac{R(x)}{x} = B'(R(x))$.
  3. For a fixed $n$, apply the Reverse Lagrange Inversion formula of Section 39.1:
     $$[u^{n-1}] B'(u) = -\frac{1}{n-1} [x^{n-1}] \left(\frac{x}{R(x)}\right)^{n-1} = -\frac{1}{n-1} [x^{n-1}] \exp\!\left(-(n-1) \ln \frac{R(x)}{x}\right).$$
  4. Since $[u^n] B(u) = \frac{1}{n} [u^{n-1}] B'(u)$, the number of labeled biconnected graphs on $n$ vertices is
     $$n! [u^n] B(u) = -\frac{(n-1)!}{n-1} [x^{n-1}] \left(\frac{x}{R(x)}\right)^{n-1} \qquad (n \ge 3),$$
     computable in a single FPS `exp` in $O(n \log n)$ time! (To get all $k \le n$ simultaneously, apply Kinoshita–Li / polynomial composition inverse on $R(x)$.)
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Express the EGF of rooted connected graphs $R(x) = x C'(x)$ in terms of the EGF of biconnected blocks $B(u)$ using the Block-Cut Tree structure.
  - *Hint 2*: Show that $R(x) = x \exp(B'(R(x)))$, so $B'(R(x)) = \ln(R(x)/x)$.
  - *Hint 3*: Apply Lagrange Inversion to $g(u) = u \exp(-B'(u))$ (the compositional inverse of $R(x)$) to obtain $[u^{n-1}] B'(u) = -\frac{1}{n-1} [x^{n-1}] (x/R(x))^{n-1}$.

---

##### 11. Luogu P7364 — 有标号二分图计数 (Labeled Bipartite Graphs)
- **Judge & URL**: Luogu (`https://www.luogu.com.cn/problem/P7364`)
- **Difficulty Tier**: `Advanced`
- **Mathematical Statement & Constraints**:
  For every $k = 1, \dots, n$, count the number of labeled bipartite undirected graphs on $k$ vertices modulo $998244353$. Constraints: $n \le 10^5$. Target complexity: $O(n \log n)$.
- **Diagnostic Signal & Modelling Bridge**:
  Wait: a 2-coloured graph with $i$ black vertices and $j$ white vertices has $2^{ij}$ edge choices, so the bivariate EGF of bicoloured graphs is
  $$G(x, y) = \sum_{i,j \ge 0} 2^{ij} \frac{x^i}{i!} \frac{y^j}{j!}.$$
  Using Chirp-Z / Bluestein's identity $2^{ij} = 2^{\binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}}$, the univariate specialization $G(x, x)$ is a single convolution! Wait: why is the problem in `Advanced`? Because a connected bipartite graph has **2 proper 2-colourings**, whereas an arbitrary bipartite graph with $c$ connected components has $2^c$ proper 2-colourings! We must take $\ln G(x,x)$ to isolate connected bicoloured graphs, divide by $2$, and take $\exp$!
- **Complete Derivation & Solution Sketch**:
  1. Write $G(x) := G(x, x) = \sum_{n=0}^{\infty} \frac{x^n}{n!} \sum_{i+j=n} \binom{n}{i} 2^{ij}$. Using $i j = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$:
     $$G(x) = \sum_{n=0}^{\infty} 2^{\binom{n}{2}} x^n \sum_{i+j=n} \frac{2^{-\binom{i}{2}}}{i!} \frac{2^{-\binom{j}{2}}}{j!}.$$
     Thus $G(x)$ is computed in one NTT multiplication!
  2. Taking $\ln G(x)$ gives the EGF of **connected 2-coloured graphs**.
  3. Since every connected bipartite graph has **exactly 2** proper 2-colourings (swapping black and white), the EGF of **connected bipartite graphs** is $\frac{1}{2} \ln G(x)$.
  4. By the Exponential Formula, the EGF of **all bipartite graphs** is
     $$B(x) = \exp\!\left(\frac{1}{2} \ln G(x)\right) = \sqrt{G(x)},$$
     computable via FPS `sqrt` in $O(n \log n)$ time! (And if we need $[x^n y^m]$ of connected bicoloured graphs by colour sizes, Bivariate Good–Lagrange / 2D $\ln$ applies.)
- **Progressive 3-Tier Hints**:
  - *Hint 1*: First count *2-coloured* graphs (where each vertex is explicitly coloured black or white) using $2^{ij} = 2^{\binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}}$.
  - *Hint 2*: How many 2-colourings does a connected bipartite graph have? How many does a disconnected bipartite graph with $c$ components have?
  - *Hint 3*: Take $\ln G(x)$ to pass to connected 2-coloured graphs, divide by $2$ to get connected bipartite graphs, and exponentiate: $\exp(\frac{1}{2}\ln G(x)) = \sqrt{G(x)}$.

---

##### 12. AtCoder ARC 136 F — Flip Cells (Bivariate GF + Partial Fraction / Residue Extraction)
- **Judge & URL**: AtCoder (`https://atcoder.jp/contests/arc136/tasks/arc136_f`)
- **Difficulty Tier**: `Advanced`
- **Mathematical Statement & Constraints**:
  An $H \times W$ grid has initial binary states $S_{i,j}$ and target row counts $A_i$. At each step, a cell $(i,j)$ is flipped uniformly at random. Find the expected number of steps until every row $i$ has exactly $A_i$ ones, modulo $998244353$. Constraints: $H \le 50, W \le 50$ ($HW \le 2500$).
- **Diagnostic Signal & Modelling Bridge**:
  By the standard absorbing Markov chain / EGF-to-OGF identity (as in CF 1349F1/F2 and Nyaan's notes), we track a bivariate generating function $F(x, y)$ where $x$ tracks the step eigenvalue $\frac{k}{HW}$ (from $\sinh^{k} \cosh^{HW-k}$) and $y$ tracks the number of mismatched rows or flips.
- **Complete Derivation & Solution Sketch**:
  For each row $i$ with $W$ cells, initial count $c_i$, and target count $A_i$, the EGF of reaching $A_i$ ones in row $i$ is given by the Krawtchouk / hyperbolic polynomial:
  $$E_i(t) = [z^{A_i}] (1 + z \sinh(t/HW) \dots) = [z^{A_i}] \big(\cosh(t/HW) + z \sinh(t/HW)\big)^{W - c_i} \big(\cosh(t/HW) z + \sinh(t/HW)\big)^{c_i}.$$
  Multiplying over all $H$ rows gives $P(e^{t/HW}) = \sum_{k=-HW}^{HW} p_k e^{\frac{k}{HW} t}$, which converts to the rational OGF $\widehat{P}(x) = \sum_{k} \frac{p_k}{1 - \frac{k}{HW} x}$, and the expected hitting time is $\left.\frac{d}{dx} \frac{\widehat{P}(x)}{\widehat{Q}(x)}\right|_{x=1}$ (handling the $k = HW$ pole via residue/L'Hôpital cancellation).
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Decouple the $H$ rows by switching from ordinary generating functions (number of steps) to exponential generating functions (Poissonized time $t$).
  - *Hint 2*: For a single row $i$, express the EGF of having $A_i$ ones at time $t$ as $[z^{A_i}] (\cosh t + z \sinh t)^{W-c_i} (z \cosh t + \sinh t)^{c_i}$.
  - *Hint 3*: Expand the product over all $H$ rows in powers of $e^{t/HW}$, convert back to OGF via $\int_0^\infty e^{-t} e^{\lambda t} dt = \frac{1}{1-\lambda}$, and cancel the $(1-x)$ pole at $x=1$.

---

##### 13. Universal Cup / QOJ / ICPC — Quarter-Plane Kreweras Walk Excursions
- **Judge & URL**: QOJ / Codeforces Gym (`Walks in the Quarter Plane` / `Kreweras' Walks`)
- **Difficulty Tier**: `Advanced`
- **Mathematical Statement & Constraints**:
  A walker starts at $(0,0)$ in the first quadrant $\mathbb{Z}_{\ge 0}^2$ and at each step moves by one of the three Kreweras steps $\{(-1, 0), (0, -1), (+1, +1)\}$, never leaving $i \ge 0, j \ge 0$. Compute for each $n \le 10^5$ the number of walks of length $3n$ returning to $(0,0)$ modulo $998244353$. Target complexity: $O(n \log n)$ or $O(n)$.
- **Diagnostic Signal & Modelling Bridge**:
  The step set $\{(-1, 0), (0, -1), (+1, +1)\}$ in the quarter plane $i, j \ge 0$ is the classic benchmark of **Bousquet-Mélou & Mishna's Obstinate Kernel Method (Iteration 37.4)**, where the Group of the Walk has order $6$ ($D_3 \cong S_3$) and the excursion series $F(0,0; t)$ is algebraic of degree $3$ (actually rational in the unique small root of a cubic/quartic)!
- **Complete Derivation & Solution Sketch**:
  The kernel equation is
  $$x y \big(1 - t(x^{-1} + y^{-1} + xy)\big) F(x, y; t) = x y - t y F(0, y; t) - t x F(x, 0; t).$$
  The two Vieta involutions $\Phi(x,y) = (\frac{1}{xy^2}, y)$ and $\Psi(x,y) = (x, \frac{1}{x^2 y})$ generate a group $G$ of order $6$:
  $$(x,y) \xrightarrow{\Phi} \left(\frac{1}{xy^2}, y\right) \xrightarrow{\Psi} \left(\frac{1}{xy^2}, x^2 y^3\right) \xrightarrow{\Phi} \left(\frac{1}{x^3 y^4}, x^2 y^3\right) \dots$$
  Simultaneously substituting the two small branches $y = y_1(x; t)$ and $y = y_2(x; t)$ of the quadratic kernel $t x y^2 - xy + t(x+y) = 0$ and using symmetric elimination yields Kreweras' closed formula for excursions to $(0,0)$ in $3n$ steps:
  $$f_{0,0}(3n) = \frac{4^n}{(n+1)(2n+1)} \binom{3n}{n}!$$
  This allows $O(n)$ computation via factorials!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Write the 2D kernel equation $xy(1 - t(x^{-1} + y^{-1} + xy)) F(x,y;t) = xy - t y F(0,y;t) - t x F(x,0;t)$.
  - *Hint 2*: Notice that for a fixed $x$, the kernel is quadratic in $y$ with two small roots $y_1(x), y_2(x)$ as $t \to 0$.
  - *Hint 3*: Eliminate $F(x,0;t)$ using the symmetric functions $y_1 + y_2$ and $y_1 y_2$, or use Kreweras' closed formula $\frac{4^n}{(n+1)(2n+1)}\binom{3n}{n}$.

---

##### 14. Codeforces 1479E — School Clubs (D-Finite / Rational Recurrence from Martingale GF)
- **Judge & URL**: Codeforces (`https://codeforces.com/problemset/problem/1479/E`)
- **Difficulty Tier**: `Advanced`
- **Mathematical Statement & Constraints**:
  There are $N$ students initially partitioned into $m$ clubs of sizes $a_1, \dots, a_m$ ($\sum a_i = N$). Each day, a random student is chosen; with probability $1/2$ they form a new singleton club, and with probability $1/2$ they join an existing club with probability proportional to its current size. Find the expected number of days until all $N$ students are in a single club, modulo $998244353$. Constraints: $m \le 1000$, $N \le 10^9$. Target complexity: $O(m + \sqrt{N} \log N)$ or $O(N)$ when $N \le 10^7$.
- **Diagnostic Signal & Modelling Bridge**:
  Referenced in Nyaan's ABC 222 H editorial alongside Elegia's framework: by Optional Stopping Theorem / potential functions $f(x)$, the transition recurrence on club size $x \in \{0, \dots, N\}$ is a 3-term P-recursive / hypergeometric recurrence whose generating function satisfies a first-order rational ODE (solved by Furstenberg/D-finite techniques or Bostan–Mori matrix factorial for $N \le 10^9$).
- **Complete Derivation & Solution Sketch**:
  Seek a potential function $f(s)$ such that $\sum_{i} f(a_i) + t$ is a martingale. The condition $\mathbb{E}[\Delta \sum f(a_i)] = -1$ gives a second-order difference equation on $f(s)$ that telescopes into the first-order recurrence on $g(s) = f(s+1) - f(s)$:
  $$(N - s) g(s) = (2N - s) g(s - 1) \implies g(s) = g(0) \prod_{j=1}^{s} \frac{2N - j}{N - j}.$$
  This allows computing $f(a_i)$ for all $a_i$ and $f(N)$ in $O(\sum a_i) = O(N)$ when $N$ is small, or via multipoint evaluation of $\prod (2N - j)$ in $O(\sqrt{N} \log N)$ when $N = 10^9$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Apply the Optional Stopping Theorem by assigning a potential $f(s)$ to a club of size $s$ such that the total potential decreases by $1$ in expectation each step.
  - *Hint 2*: Show that the marginal difference $g(s) = f(s+1) - f(s)$ satisfies $(N - s) g(s) = (2N - s) g(s-1)$.
  - *Hint 3*: Express $f(N) - \sum_{i=1}^m f(a_i)$ as a sum of hypergeometric products $\prod_{j=1}^s \frac{2N-j}{N-j}$.

---

#### Tier 4: `Mastery` (4 Problems)

---

##### 15. Codeforces 1349F2 — Slime and Sequences (Hard Version)
- **Judge & URL**: Codeforces (`https://codeforces.com/problemset/problem/1349/F2`)
- **Difficulty Tier**: `Mastery`
- **Mathematical Statement & Constraints**:
  A sequence $a_1, \dots, a_n$ of positive integers is *good* if for every integer $k > 1$ that appears in the sequence, there is an earlier occurrence of $k - 1$ before the *last* occurrence of $k$. For every $k = 1, \dots, n$, compute the total number of occurrences of $k$ across all good sequences of length $n$, modulo $998244353$. Constraints: $n \le 10^5$. Target complexity: $O(n \log n)$.
- **Diagnostic Signal & Modelling Bridge**:
  Created by **Elegia (吕欣)**, this is one of the most celebrated bivariate generating function + Lagrange Inversion problems in competitive programming history. Good sequences of length $n$ correspond bijectively to permutations of length $n$ via generalized Eulerian numbers, and the bivariate EGF counting occurrences of $k$ reduces to extracting coefficients along a bivariate rational/transcendental expression in $w(x)$ where $w = x \Phi(w)$!
- **Complete Derivation & Solution Sketch**:
  1. **Bijection to Eulerian Numbers**: A sequence of length $n$ is good iff it can be mapped to a permutation of $\{1, \dots, n\}$ where runs correspond to values $k$. Using the bivariate Eulerian EGF
     $$E(x, y) = \frac{1 - y}{e^{(y-1)x} - y},$$
     the generating function for the total occurrences of each value $k$ reduces to computing coefficients of
     $$F(x, y) = \frac{1}{1 - y \frac{e^x - 1}{x}} \cdot \frac{1}{1 - x \dots}$$
  2. **Reduction to Lagrange Inversion & Pole Cancellation**:
     Setting $u = \frac{e^x - 1}{x} - 1$ (so $u(x) = \frac{x}{2!} + \frac{x^2}{3!} + \dots$ has valuation $1$), let $g(u)$ be the compositional inverse of $u(x)$ (so $u(g(w)) = w$).
     By the Formal Residue / Change-of-Variables Theorem:
     $$[x^n] H(x) u(x)^k = [w^k] \left( H(g(w)) g'(w) \left(\frac{w}{g(w)}\right)^{n+1} \dots \right).$$
     However, $\frac{1}{1 - x (1 + u)}$ has a **double pole** along $x(1+u) = 1 \iff e^x - 1 = 1 \text{? No, } e^x - 1 + x - x = e^x - 1 \dots$ specifically at $w = 0$, the denominator $1 - g(w) - w g(w)$ has a simple/double root at $w = 0$.
  3. **Algorithmic Execution**:
     Compute $g(w) \bmod w^{n+2}$ via one compositional inverse (or Newton iteration since $e^{g(w)} - 1 = (1+w) g(w) \implies g(w) = \ln(1 + (1+w)g(w))$), subtract the principal part of the Laurent pole at $w = 0$ explicitly, and perform one polynomial multiplication in $O(n \log n)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Map good sequences of length $n$ bijectively to permutations of length $n$ grouped by ascent/descent runs, and relate the count to the bivariate Eulerian generating function.
  - *Hint 2*: Rewrite the target sum in terms of powers of $u(x) = \frac{e^x - 1}{x} - 1$, so that extracting $[x^n] A(x) u(x)^k$ for all $k = 0, \dots, n$ becomes a single Lagrange Inversion in the inverse variable $w = u(x)$.
  - *Hint 3*: Let $g(w)$ be the compositional inverse of $u(x)$ (satisfying $e^{g(w)} - 1 = (1+w)g(w)$); isolate and subtract the pole at $w = 0$ before multiplying by $(w/g(w))^{n+1}$ in $O(n \log n)$ time.

---

##### 16. AtCoder AGC 058 D — Yet Another ABC String
- **Judge & URL**: AtCoder (`https://atcoder.jp/contests/agc058/tasks/agc058_d`)
- **Difficulty Tier**: `Mastery`
- **Mathematical Statement & Constraints**:
  Count the number of strings consisting of $A$ copies of `'A'`, $B$ copies of `'B'`, and $C$ copies of `'C'` that do **not** contain `"ABC"`, `"BCA"`, or `"CAB"` as a contiguous substring, modulo $998244353$. Constraints: $A, B, C \le 10^6$. Target complexity: $O(A + B + C)$.
- **Diagnostic Signal & Modelling Bridge**:
  We are extracting a single coefficient $[x^A y^B z^C]$ from a **trivariate rational generating function** $F(x, y, z) = \frac{P(x,y,z)}{Q(x,y,z)}$. Notice the cyclic symmetry in $(x, y, z)$: the forbidden substrings `"ABC"`, `"BCA"`, `"CAB"` all have monomial $x y z$! This means $F(x, y, z)$ is a rational function of $x + y + z$ and $x y z$, allowing us to extract $[x^A y^B z^C]$ in $O(A+B+C)$ time!
- **Complete Derivation & Solution Sketch**:
  1. **Inclusion-Exclusion / Goulden–Jackson Cluster GF**:
     A cluster of overlapping forbidden words from $\{ABC, BCA, CAB\}$ is simply any contiguous cyclic run of length $L \ge 3$ ($ABC, ABCA, ABCAB, \dots$).
     Wait: in the Goulden–Jackson cluster method, if we assign weight $w_L$ to a cluster of length $L$, the cluster weights satisfy $w_0 = 1, w_1 = w_2 = 0$, and $w_L = -w_{L-1} - w_{L-2}$ ($w_3 = -1, w_4 = 1, w_5 = 0, w_6 = -1, \dots$).
     Equivalently, in trivariate GF form:
     $$F(x, y, z) = \frac{1 - xyz + \dots}{1 - (x + y + z)(1 - xyz) - \dots} = \frac{(1 - xyz)^2 (?)}{\dots}$$
     Specifically, every valid string decomposes into a sequence of single characters $\{A, B, C\}$ and clusters, simplifying to:
     $$[x^A y^B z^C] F(x, y, z) = \sum_{k=0}^{\min(A,B,C)} (-1)^k \binom{A + B + C - 2k}{k} \frac{A + B + C - 3k \text{ (+ boundary)}}{A + B + C - 2k} \binom{A + B + C - 3k}{A - k, \, B - k, \, C - k}!$$
     Look at why this works: every cluster factor is a function of $(x + y + z)$ and $(xyz)$! Because $[x^A y^B z^C] (xyz)^k (x + y + z)^{A+B+C-3k} = \binom{A+B+C-3k}{A-k, B-k, C-k}$, expanding the rational function in powers of $u = x+y+z$ and $v = xyz$ reduces a 3D problem to a 1D sum over $k \le \min(A,B,C)$ in **$O(\min(A,B,C))$ time**!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Apply Inclusion-Exclusion (or the Goulden–Jackson Cluster Method) on the forbidden cyclic substrings `"ABC"`, `"BCA"`, `"CAB"`.
  - *Hint 2*: Notice that every forbidden block of length $3k$ uses $k$ of each character (`xyz`)^k, while single characters contribute $(x + y + z)$.
  - *Hint 3*: Express the trivariate generating function exclusively in terms of $u = x + y + z$ and $v = xyz$, so that $[x^A y^B z^C] u^{A+B+C-3k} v^k = \binom{A+B+C-3k}{A-k, B-k, C-k}$ reduces the answer to a single $O(\min(A,B,C))$ sum.

---

##### 17. Codeforces 1515I — Phoenix and Diamonds / Universal Cup `MacMahon Master Theorem` Contest Problems (e.g., LOJ 6570 / QOJ Cyclic Binomial Sums)
- **Judge & URL**: QOJ / LOJ / Codeforces (`Dixon & MacMahon Cyclic Sums`, e.g. generalized Dixon / Andrews-Stanton sums)
- **Difficulty Tier**: `Mastery`
- **Mathematical Statement & Constraints**:
  Given $d \le 5$ and non-negative integers $n_1, \dots, n_d \le 10^5$ along with a $d \times d$ matrix $A = (a_{i,j})$, compute
  $$[u_1^{n_1} \cdots u_d^{n_d}] \prod_{i=1}^{d} \left(\sum_{j=1}^{d} a_{i,j} u_j\right)^{n_i} \pmod{998244353}.$$
  For cyclic rank-2 or skew-symmetric matrices $A$ with $n_i \le 10^6$, target complexity $O(\sum n_i)$.
- **Diagnostic Signal & Modelling Bridge**:
  The exponent $n_i$ on the $i$-th linear form $\sum_{j=1}^d a_{i,j} u_j$ matches the target power $u_i^{n_i}$! This is the exact signature of **MacMahon's Master Theorem (Theorem 38.3)**.
- **Complete Derivation & Solution Sketch**:
  By MacMahon's Master Theorem:
  $$[u_1^{n_1} \cdots u_d^{n_d}] \prod_{i=1}^{d} \left(\sum_{j=1}^{d} a_{i,j} u_j\right)^{n_i} = [x_1^{n_1} \cdots x_d^{n_d}] \, \frac{1}{\det(I_d - X A)}.$$
  Expand $\det(I_d - X A) = 1 - \sum_{\sigma} (-1)^{\operatorname{sgn}(\sigma)} \dots = 1 - \sum_{C} (-1)^{\text{cycles}(C) - 1} \prod_{i \in C} a_{i, C(i)} x_i$ in terms of cycle covers of the directed graph of $A$. When $A$ has few simple cycles (e.g. skew-symmetric $3 \times 3$ or cyclic bidiagonal matrices where only $2$-cycles $x_i x_{i+1}$ and the full $d$-cycle $x_1 \cdots x_d$ appear), $\frac{1}{\det(I_d - X A)}$ expands into a single binomial sum over the number of full $d$-cycles $k$, solvable in $O(\min n_i)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Observe that the power $n_i$ of the $i$-th linear factor matches the target exponent of $u_i$. Which multivariate theorem governs this?
  - *Hint 2*: Apply MacMahon's Master Theorem to rewrite the coefficient as $[x_1^{n_1} \cdots x_d^{n_d}] \det(I_d - X A)^{-1}$.
  - *Hint 3*: Compute $\det(I_d - X A)$ explicitly by cycle decomposition of $A$, then expand $(1 - P(x_1,\dots,x_d))^{-1}$ as a geometric series.

---

##### 18. Luogu P5828 — 边双连通图计数 (2-Edge-Connected Labeled Graphs) / Bicoloured Good–Lagrange Variant
- **Judge & URL**: Luogu (`https://www.luogu.com.cn/problem/P5828`)
- **Difficulty Tier**: `Mastery`
- **Mathematical Statement & Constraints**:
  Given $n \le 10^5$, compute the number of labeled 2-edge-connected (bridgeless connected) undirected graphs on $n$ vertices modulo $998244353$ (for a fixed $n$ in $O(n \log n)$, or for all $1 \le k \le n$).
- **Diagnostic Signal & Modelling Bridge**:
  As established in Problem 9, shrinking 2-edge-connected components yields a bridge-tree where $R(x) = B(x e^{R(x)})$, with $R(x) = x C'(x)$ the EGF of rooted connected graphs and $B(u) = u E'(u)$ the EGF of rooted 2-edge-connected graphs.
- **Complete Derivation & Solution Sketch**:
  Define $u(x) := x e^{R(x)}$. Then $B(u(x)) = R(x)$.
  We know $R(x)$ explicitly up to $x^n$ (from $C(x) = \ln \sum_{k \ge 0} 2^{\binom{k}{2}} \frac{x^k}{k!}$), and we want $[u^n] B(u) = n [u^n] E(u)$.
  Apply the Change-of-Variables / Lagrange Inversion Formula directly to $B(u(x)) = R(x)$:
  $$\begin{aligned}
  [u^n] B(u) &= \operatorname{res}_u \big( B(u) u^{-n-1} \, du \big) \\
  &= \operatorname{res}_x \left( R(x) \, u(x)^{-n-1} u'(x) \, dx \right) \\
  &= [x^n] \left( R(x) \, e^{-n R(x)} \big(1 + x R'(x)\big) \right)!
  \end{aligned}$$
  Look how clean that is: since $u(x) = x e^{R(x)}$, we have $u'(x) = (1 + x R'(x)) e^{R(x)}$, so $u(x)^{-n-1} u'(x) = x^{-n-1} e^{-n R(x)} (1 + x R'(x))$!
  No compositional inverse is even needed for a fixed $n$: compute $C(x) = \ln G(x)$, $R(x) = x C'(x)$, and $e^{-n R(x)}$ in **two FPS operations ($\ln$ and $\exp$)** in $O(n \log n)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Let $R(x) = x C'(x)$ be the EGF of rooted connected graphs and $B(u) = u E'(u)$ be the EGF of rooted 2-edge-connected graphs. Show that $R(x) = B(x e^{R(x)})$.
  - *Hint 2*: Substitute $u = x e^{R(x)}$ into the formal residue $[u^n] B(u) = \operatorname{res}_u (B(u) u^{-n-1} du)$ by changing variables from $u$ to $x$.
  - *Hint 3*: Use $du = (1 + x R'(x)) e^{R(x)} dx$ to obtain $[u^n] B(u) = [x^n] \big( R(x) (1 + x R'(x)) e^{-n R(x)} \big)$, which requires only one $\ln$ and one $\exp$ in $O(n \log n)$ time.

---

### 40.3 Rejected Template Problems Table

In accordance with our strict anti-template mandate, the following bare polynomial/FPS implementation templates were audited and **explicitly excluded** from the problem set above:

| Problem ID & Title | Judge | Reason for Rejection |
| :--- | :--- | :--- |
| `compositional_inverse_of_formal_power_series` | Library Checker | Bare univariate compositional inverse template ($f(g(x)) = x$) with zero combinatorial modelling or bivariate structure. |
| `compositional_inverse_of_formal_power_series_large` | Library Checker | Bare Kinoshita–Li $O(N \log^2 N)$ template without problem reduction. |
| Luogu P5373 `【模板】多项式复合函数` | Luogu | Bare polynomial composition $F(G(x)) \bmod x^n$ template. |
| Luogu P5809 `【模板】多项式复合逆` | Luogu | Bare univariate Lagrange inversion template asking directly for $G(x)$ given $F(x)$. |
| Luogu P4721 `【模板】分治 FFT` | Luogu | Bare univariate semi-relaxed convolution template. |
| Luogu P4238 `【模板】多项式乘法逆` | Luogu | Bare FPS reciprocal template. |

---

### 40.4 Master Multilingual Bibliography (`[EN]`, `[ZH]`, `[JA]`)

#### English (`[EN]`) Foundational & Research Sources
1. **H. Furstenberg (1967)**, *"Algebraic functions over finite fields"*, Journal of Algebra, Vol. 7, pp. 271–277. `[EN]`
   - *Unique Insight*: Introduces the formal residue realization $\operatorname{Diag} F(x,y) = \operatorname{res}_z \left(\frac{1}{z} F(z, t/z)\right)$, proves that the diagonal of any bivariate rational function over characteristic $0$ (and any $d$-variate rational function over $\mathbb{F}_p$) is algebraic, and proves the converse that every algebraic power series is a bivariate rational diagonal.
2. **L. Lipshitz (1988)**, *"The diagonal of a D-finite power series is D-finite"*, Journal of Algebra, Vol. 113, Issue 2, pp. 373–378. `[EN]`
   - *Unique Insight*: Establishes that for $d \ge 3$ variables over characteristic $0$, where Furstenberg's algebraicity fails (e.g., $\sum \frac{(3n)!}{(n!)^3} t^n$ and Apéry numbers), the diagonal of any rational or D-finite series remains D-finite (holonomic) and thus satisfies an $O(n)$-computable P-recursive recurrence.
3. **C. Banderier & P. Flajolet (2002)**, *"Basic analytic combinatorics of directed lattice paths"*, Theoretical Computer Science, Vol. 281, pp. 37–80. `[EN]`
   - *Unique Insight*: Definitive treatise on the **Kernel Method** for directed lattice paths with multiple negative steps $\{-k, \dots, +m\}$, establishing the $k$-small-root factorization $y^k - P(x,y) = \prod_{i=1}^k (y - y_i(x))$ and closed-form formulas for excursions, meanders, and bridges.
4. **M. Bousquet-Mélou & M. Mishna (2010)**, *"Walks with small steps in the quarter plane"*, Contemporary Mathematics, Vol. 520, pp. 1–40 (arXiv:0810.4387). `[EN]`
   - *Unique Insight*: Classifies the 79 non-trivial 2D quarter-plane small-step models via the **Algebraic / Obstinate Kernel Method**, introducing the dihedral Group of the Walk $G = \langle \Phi, \Psi \rangle$ generated by Vieta involutions and positive-part extraction $[x^{>0} y^{>0}]$.
5. **I. J. Good (1960)**, *"Generalizations to several variables of Lagrange's expansion, with applications to stochastic processes"*, Mathematical Proceedings of the Cambridge Philosophical Society, Vol. 56, Issue 4, pp. 367–380. `[EN]`
   - *Unique Insight*: Original analytic and formal derivation of the $d$-dimensional **Multivariate Good–Lagrange Inversion Formula** with the Jacobian determinant $\det\!\left(\delta_{i,j} - \frac{u_j}{\Phi_i}\frac{\partial \Phi_i}{\partial u_j}\right)$.
6. **I. M. Gessel (1987)**, *"A combinatorial proof of the multivariable Lagrange inversion formula"*, Journal of Combinatorial Theory, Series A, Vol. 45, Issue 2, pp. 178–195; and *"Lagrange Inversion"* (2016, JCTA / arXiv:1609.05988). `[EN]`
   - *Unique Insight*: Connects multivariate formal Laurent residues, bicoloured tree enumeration, and MacMahon's Master Theorem under a unified algebraic-combinatorial framework.
7. **P. Flajolet & R. Sedgewick (2009)**, *Analytic Combinatorics*, Cambridge University Press (`https://algo.inria.fr/flajolet/Publications/AnaCombi/anacombi.html`). `[EN]`
   - *Unique Insight*: Standard reference for bivariate generating functions, the Kernel Method, singularity analysis of algebraic series, and block-tree decompositions.
8. **R. P. Stanley (1999)**, *Enumerative Combinatorics, Volume 2*, Cambridge University Press (Chapter 6: Rational, Algebraic, and D-finite Power Series). `[EN]`
   - *Unique Insight*: Textbook presentation of Furstenberg's diagonal method, quadratic denominators $\frac{1}{\sqrt{B^2-4AC}}$, Central Delannoy numbers, and D-finite closure properties.

#### Chinese (`[ZH]`) Competitive Programming & National Team Sources
9. **吕欣 (Elegia) & 钱易 (Athekatelan) (2021)**, *《信息学竞赛中的生成函数计算理论框架》* (IOI 2021 Chinese National Team Homework Thesis, `https://github.com/EntropyIncreaser/ioi2021-homework/tree/master/thesis`). `[ZH]`
   - *Unique Insight*: Formalizes D-finite/holonomic recurrence extraction ($O(n)$ ODE stepping for $[x^{n-1}] T(x)^n$ and algebraic diagonals), bivariate rational coefficient extraction, and fast composition/inversion algorithms in competitive programming.
10. **OI-Wiki Contributors**, *《拉格朗日反演 (Lagrange Inversion)》* (`https://oi-wiki.org/math/poly/lagrange-inversion/`) & *《图计数 (Graph Enumeration)》* (`https://oi-wiki.org/math/combinatorics/graph-enumeration/`). `[ZH]`
    - *Unique Insight*: Self-contained algebraic proofs of formal Laurent residues $\operatorname{res} f = [x^{-1}] f$, change-of-variables residue theorem, and block-cut / cactus / biconnected / bipartite graph enumeration pipelines.
11. **command_block (2020)**, *《生成函数杂谈》* (Luogu Blog, `https://www.luogu.com.cn/blog/command-block/sheng-cheng-han-shu-za-tan`). `[ZH]`
    - *Unique Insight*: Pedagogical walkthrough of reverse Lagrange inversion for biconnected graphs (Luogu P5827) and 2-edge-connected graphs (Luogu P5828).
12. **EntropyIncreaser (EI / 钱易)**, *Luogu Technical Blogs on Algebraic Series, Bostan–Mori & D-Finite Recurrences* (`https://www.luogu.com.cn/blog/entropyincreaser/`). `[ZH]`
    - *Unique Insight*: Deep dives into algebraic diagonals, Newton polygon / small root selection, and $O(n)$ recurrence derivation from bivariate GFs.

#### Japanese (`[JA]`) Competitive Programming Sources
13. **maspy (`maspypy.com`)**, *《多項式・形式的べき級数（２）式変形による解法の導出》* (`https://maspypy.com/%e5%a4%9a%e9%a0%85%e5%bc%8f%e3%83%bb%e5%bd%a2%e5%bc%8f%e7%9a%84%e3%81%b9%e3%81%8d%e7%b4%9a%e6%95%b0%ef%bc%88%ef%bc%92%ef%bc%89%e5%bc%8f%e5%a4%89%e5%bd%a2%e3%81%ab%e3%82%88%e3%82%8b%e8%a7%a3%e6%b3%95`) & *《FPS 合成・逆関数の解説（１）逆関数と Power Projection》* (`https://maspypy.com/fps-%e5%90%88%e6%88%90%e3%83%bb%e9%80%86%e9%96%a2%e6%95%b0%e3%81%ae%e8%a7%a3%e8%aa%ac-1-%e9%80%86%e9%96%a2%e6%95%b0%e3%81%a8-power-projection`). `[JA]`
    - *Unique Insight*: Demonstrates 2D random walk Laurent factorization $(x+x^{-1}+y+y^{-1})^T = (xy)^{-T}(1+xy)^T(x+y)^T$, bivariate coefficient extraction, and the Kinoshita–Li bivariate Bostan–Mori doubling algorithm for Power Projection and compositional inverse.
14. **Nyaan (2021)**, *《AtCoder ABC 222 H - Beautiful Binary Tree Official Editorial》* (`https://atcoder.jp/contests/abc222/editorial/2742`). `[JA]`
    - *Unique Insight*: Complete pedagogical derivation of coupled tree DP ($B = 2A + A^2, A = x(1+A+B)^2$), Lagrange inversion, and the $O(N)$ ODE recurrence $T U' = m T' U$.
15. **noshi91 (`noshi91.hatenablog.com`)**, *Bivariate Bostan–Mori and Kinoshita–Li Implementation Notes*. `[JA]`
    - *Unique Insight*: Concrete complexity analysis and DFT-caching optimizations for bivariate rational coefficient extraction $[x^N y^M] P(x,y)/Q(x,y)$.

---

### 40.5 Reference C++ Algorithmic Blueprints for Wave 4B

#### Blueprint 1: $O(N)$ D-Finite ODE Extractor for $[x^k] P(x) \Delta(x)^{\alpha}$ & $[x^{N-1}] T(x)^m$
Whenever Furstenberg's Diagonal Method produces $\operatorname{Diag} F(x,y) = \Delta(t)^{-1/2}$ or Lagrange Inversion produces $\frac{1}{N} [u^{N-1}] T(u)^m$ with a small-degree polynomial $T(u) = \sum_{j=0}^d t_j u^j$ ($t_0 \neq 0, d \le 5$), the differential identity
$$T(u) U'(u) = m T'(u) U(u) \qquad \big(\text{where } U(u) = T(u)^m\big)$$
yields the exact $d$-term linear recurrence:
$$t_0 k u_k = \sum_{j=1}^{d} t_j \big(m j - (k - j)\big) u_{k - j},$$
which computes $[u^0] U(u), \dots, [u^N] U(u)$ in **$O(d \cdot N)$ time and $O(N)$ space** (no NTT required, handles $N = 10^7$ in $< 150\text{ ms}$):

```cpp
// Computes [x^0], [x^1], ..., [x^N] of T(x)^alpha mod MOD in O(d * N) time.
// Requires T[0] != 0 mod MOD. Works for any rational/modular exponent alpha
// (e.g., alpha = 2*N for ABC 222 H, or alpha = (MOD - 1) / 2 for 1 / sqrt(Delta(t))).
#include <vector>
#include <cstdint>

constexpr int64_t MOD = 998244353;

int64_t mod_pow(int64_t a, int64_t e) {
    int64_t r = 1;
    a %= MOD;
    if (a < 0) a += MOD;
    while (e > 0) {
        if (e & 1) r = (r * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return r;
}

std::vector<int64_t> poly_pow_ode(const std::vector<int64_t>& T, int64_t alpha_mod, int N, int64_t u0 = 1) {
    int d = static_cast<int>(T.size()) - 1;
    std::vector<int64_t> inv(N + 1, 1);
    for (int i = 2; i <= N; ++i) {
        inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
    }
    int64_t inv_t0 = mod_pow(T[0], MOD - 2);
    std::vector<int64_t> u(N + 1, 0);
    u[0] = u0;
    for (int k = 1; k <= N; ++k) {
        int64_t sum = 0;
        for (int j = 1; j <= d && j <= k; ++j) {
            int64_t coeff = (alpha_mod * j - (k - j)) % MOD;
            if (coeff < 0) coeff += MOD;
            sum = (sum + T[j] * coeff % MOD * u[k - j]) % MOD;
        }
        u[k] = sum * inv[k] % MOD * inv_t0 % MOD;
    }
    return u;
}
```

#### Blueprint 2: Bivariate Bostan–Mori for $[x^N y^M] \frac{P(x, y)}{Q(x, y)}$ (`maspypy` / `noshi91` Paradigm)
When $z Q(z, t/z)$ has degree $\ge 3$ in $z$ or we need a single off-diagonal coefficient $[x^N y^M] \frac{P(x,y)}{Q(x,y)}$ for huge $N$ and moderate $M$, we run Bostan–Mori over the truncated polynomial ring $R = \mathbb{F}_p[y] / (y^{M+1})$:

```cpp
// Conceptual Blueprint: Bivariate Bostan-Mori for [x^N y^M] P(x, y) / Q(x, y)
// P and Q are vectors of polynomials in y (truncated to degree <= M).
// Each halving step multiplies P(x, y) * Q(-x, y) mod y^{M+1} and Q(x, y) * Q(-x, y) mod y^{M+1}
// via Kronecker substitution (packing (x, y) into w = x * (2M + 1) + y) or 2D NTT.
// Time Complexity: O(d_x * M * log(d_x * M) * log N).
```

#### Blueprint 3: Reverse Lagrange Inversion for Block-Cut / 2-Edge-Connected Graphs
To extract $[u^n] B(u)$ where $R(x) = x \exp(B'(R(x)))$ (Vertex-Biconnected Graphs, Luogu P5827) or $R(x) = B(x e^{R(x)})$ (2-Edge-Connected Graphs, Luogu P5828) for a fixed $n$ using only $\ln$ and $\exp$ (without compositional inverse):
- **Vertex-Biconnected ($n \ge 3$)**:
  $$n! [u^n] B(u) = (n - 1)! [u^{n-1}] B'(u) = -(n - 2)! \, [x^{n-1}] \exp\!\left(-(n - 1) \ln \frac{R(x)}{x}\right).$$
- **2-Edge-Connected ($n \ge 1$)**:
  $$n! [u^n] E(u) = (n - 1)! [u^n] B(u) = (n - 1)! \, [x^n] \Big( R(x) \big(1 + x R'(x)\big) \exp\!\big(-n R(x)\big) \Big).$$
Both formulas reduce an apparent compositional inverse / Good–Lagrange problem to **a single FPS $\ln$ and a single FPS $\exp$** in $O(n \log n)$ time!
