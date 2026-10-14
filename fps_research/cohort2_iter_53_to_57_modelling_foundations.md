# Cohort 2 — Wave 1A (Iterations 53–57): Foundational Algebra, Unlabelled OGFs, Labelled EGFs, and Multilingual (`[EN]`/`[ZH]`/`[JA]`) Combinatorial Modelling

> **Research Cohort**: Cohort 2 (Independent Redundant Discovery)  
> **Wave Scope**: Wave 1A — Iterations 53, 54, 55, 56, 57  
> **Target File**: `fps_research/cohort2_iter_53_to_57_modelling_foundations.md`  
> **Pedagogical Standard**: Zero Magic Steps — Concrete Object, Diagnostic Signal, Reverse-Engineering Scratchpad, Annotated Algebraic Derivation, Hand-Checkable Toy Trace ($n \le 4$), Failure Modes & Prime Characteristic Obstructions.

---

## Executive Architecture of Wave 1A

Generating functions and formal power series (FPS) are often taught in competitive programming as two disconnected worlds: either as a collection of ad-hoc algebraic tricks ("multiply by $x$, differentiate, guess a closed form") or as a black-box polynomial library (`inv`, `ln`, `exp`, `sqrt` in $O(N \log N)$). Both perspectives fail on modern contest problems unless the solver masters **the bridge between combinatorial specifications and formal algebraic operators**.

This five-iteration treatise builds that bridge from first principles across English (`[EN]`), Chinese (`[ZH]`), and Japanese (`[JA]`) competitive programming and analytic combinatorics literature:

1. **Iteration 53 — Foundational Algebra of Formal Power Series ($R[[x]]$, $K[[x]]$, $K((x))$)**: Establishes the purely algebraic and $x$-adic topological foundation of formal series without analytic convergence; characterizes invertible series ($[x^0]F \in R^\times$), formal composition ($\operatorname{val}(G) \ge 1$), and the differential/integral operator calculus ($D = \frac{d}{dx}$, $\vartheta = x\frac{d}{dx}$, $\int_0^x$), including prime characteristic $p > 0$ obstructions and reverse-engineering scratchpads for eliminating polynomial weights in recurrences.
2. **Iteration 54 — Unlabelled Symbolic Method & Ordinary Generating Functions (OGFs)**: Develops the Flajolet–Sedgewick unlabelled dictionary ($+, \times, \operatorname{SEQ}, \operatorname{MSET}, \operatorname{PSET}, \operatorname{CYC}$), the **Euler Transform** $\prod_{k \ge 1}(1-x^k)^{-a_k} = \exp\!\left(\sum_{j \ge 1} \frac{A(x^j)}{j}\right)$, two distinct $O(N \log N)$ algorithms for Euler and Inverse Euler transforms (via $\ln/\exp$ harmonic sieve and via logarithmic derivative $xF'/F$ + Möbius inversion), Ferrers diagrams, Durfee squares, Euler's Pentagonal Number Theorem, and Pólya/Burnside cycle index substitution.
3. **Iteration 55 — Labelled Symbolic Method & Exponential Generating Functions (EGFs)**: Develops binomial convolution, labelled operators ($\operatorname{SEQ}$, $\operatorname{SET}(A) = \exp(A)$, $\operatorname{CYC}(A) = \ln\frac{1}{1-A}$), the Pointing operator $\Theta A = xA'(x)$, and the **Boxed Product** $A^{\square} \star B = \int_0^x A'(t)B(t)\,dt$ (tracking the minimum/maximum label to break symmetry without overcounting), alongside a complete structural catalog of classical EGFs (derangements, restricted cycles, involutions, connected graphs, bipartite graphs, alternating permutations, Bell and Stirling numbers).
4. **Iteration 56 — `[ZH]` Combinatorial Modelling Deep-Dive**: Synthesizes the Chinese OI/ICPC literature (`国家集训队论文` by Jin Ce 2015, Yang Maolong 2018, Zhong Ziqian 2019; Lu Xin / Elegia's operator framework; OI-Wiki; Luogu/UOJ/LOJ tutorials), focusing on `多项式 exp/ln 的组合意义` (combinatorial meaning of polynomial $\exp/\ln$), `付公主的背包` (Euler transform knapsack trick), and `有标号定根技巧` (labelled root-fixing / pivot-label differential equations).
5. **Iteration 57 — `[JA]` Combinatorial Modelling Deep-Dive & Rigorous Wave 1A Problem Audit**: Synthesizes the Japanese FPS school (`maspypy.com`, `noshi91`, `Nyaan`, `tatyam`, `opt-cp`, AtCoder/yukicoder FPS 24), followed by a comprehensive audit of **20 non-template Accepted Problems** across four difficulty tiers (`Stepping Stone`, `Intermediate`, `Advanced`, `Mastery`) with full mathematical statements, constraints, diagnostic bridges, complete derivations, progressive 3-tier hints, a **Rejected Template Problems Table**, and a **Master Multilingual Bibliography**.

---

## Iteration 53: Foundational Algebra of Formal Power Series ($R[[x]]$, $K[[x]]$, $K((x))$)

### 53.1 Why "Formal"? Dispensing with Analytic Convergence

In classical real or complex analysis, a power series $\sum_{n=0}^{\infty} a_n x^n$ is a function of a numerical variable $x \in \mathbb{C}$, well-defined only inside its radius of convergence $R = (\limsup_{n\to\infty} |a_n|^{1/n})^{-1}$. In combinatorics and competitive programming, however, sequences such as $a_n = n!$ (counting permutations of $n$ elements) or $a_n = 2^{\binom{n}{2}}$ (counting labelled graphs on $n$ vertices) grow hyper-exponentially. Their analytic radius of convergence is $R = 0$: the series $\sum_{n=0}^{\infty} n! x^n$ diverges for every $x \ne 0$ in $\mathbb{C}$. Moreover, in competitive programming we routinely work over finite fields $\mathbb{F}_p$ (such as $p = 998244353$), where the usual Archimedean absolute value $|\cdot|$ and complex analytic radius of convergence do not even exist!

To manipulate generating functions legally over arbitrary commutative rings $R$ (such as $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{C}$, $\mathbb{F}_p$, or polynomial rings $K[y]$), we treat a formal power series strictly as an **infinite sequence of coefficients** equipped with algebraic operations that require only **finitely many ring operations per coefficient**.

#### Concrete Algebraic Object: The Ring $R[[x]]$ and Field $K((x))$

Let $R$ be a commutative ring with identity $1_R \ne 0_R$. A **formal power series** over $R$ is an infinite sequence $(a_0, a_1, a_2, \dots)$ with $a_n \in R$, written symbolically as:
$$F(x) = \sum_{n=0}^{\infty} a_n x^n.$$
Here $x$ is never instantiated to a number; $x^n$ is simply a formal placeholder marking the $n$-th slot of the sequence. We denote the coefficient of $x^n$ in $F(x)$ by the **coefficient extraction operator**:
$$[x^n] F(x) := a_n.$$

1. **Equality**: Two formal power series $F(x) = \sum_{n\ge 0} a_n x^n$ and $G(x) = \sum_{n\ge 0} b_n x^n$ are equal ($F = G$) if and only if $[x^n]F(x) = [x^n]G(x)$ for every integer $n \ge 0$.
2. **Addition and Scalar Multiplication**: Defined term-by-term:
   $$[x^n]\big(\alpha F(x) + \beta G(x)\big) := \alpha [x^n]F(x) + \beta [x^n]G(x) \quad (\alpha, \beta \in R).$$
3. **Cauchy Multiplication (Convolution)**:
   $$[x^n]\big(F(x) \cdot G(x)\big) := \sum_{k=0}^{n} \big([x^k]F(x)\big)\big([x^{n-k}]G(x)\big) = \sum_{k=0}^{n} a_k b_{n-k}.$$
   Notice why this requires no convergence: for each fixed $n \ge 0$, the sum $\sum_{k=0}^n a_k b_{n-k}$ contains exactly $n+1$ terms. It is a finite sum in $R$!

With these operations, $(R[[x]], +, \cdot)$ is a commutative ring with additive identity $0 = \sum_{n\ge 0} 0 x^n$ and multiplicative identity $1 = 1 + 0x + 0x^2 + \dots$. Furthermore, if $R$ is an integral domain (has no zero divisors), then $R[[x]]$ is also an integral domain.

---

### 53.2 Valuation, the $x$-adic Topology, and Formal Summability

Even though we reject analytic convergence on $\mathbb{C}$, we constantly write infinite sums and infinite products of formal power series, such as:
$$\exp(G(x)) = \sum_{k=0}^{\infty} \frac{G(x)^k}{k!} \quad \text{or} \quad \prod_{k=1}^{\infty} \frac{1}{1 - x^k}.$$
When is an infinite sum $\sum_{k=0}^{\infty} F_k(x)$ or infinite product $\prod_{k=1}^{\infty} (1 + H_k(x))$ mathematically well-defined in $R[[x]]$?

#### Concrete Algebraic Object: Valuation $\operatorname{val}(F)$ and Formal Convergence

For a non-zero series $F(x) = \sum_{n=0}^{\infty} a_n x^n \in R[[x]]$, its **valuation** (or **order**, denoted $\operatorname{val}(F)$ or $\operatorname{ord}(F)$) is the smallest index $n \ge 0$ for which $[x^n]F(x) \ne 0$:
$$\operatorname{val}(F) := \min\{n \in \mathbb{Z}_{\ge 0} : [x^n]F(x) \ne 0\}.$$
By convention, the zero series has $\operatorname{val}(0) = +\infty$.

The valuation satisfies three fundamental properties for all $F, G \in R[[x]]$:
1. $\operatorname{val}(F) = +\infty \iff F = 0$.
2. **Strong Triangle Inequality (Ultrametric Property)**:
   $$\operatorname{val}(F \pm G) \ge \min\big(\operatorname{val}(F), \operatorname{val}(G)\big),$$
   with equality whenever $\operatorname{val}(F) \ne \operatorname{val}(G)$.
3. **Multiplicativity** (when $R$ is an integral domain):
   $$\operatorname{val}(F \cdot G) = \operatorname{val}(F) + \operatorname{val}(G)$$
   (and $\ge$ in general rings with zero divisors).

If we fix a constant $0 < c < 1$ (say $c = 2^{-1}$) and define the **ultrametric norm** $\|F\|_x := c^{\operatorname{val}(F)}$ (with $\|0\|_x = 0$), then $d(F, G) := \|F - G\|_x$ is an ultrametric distance on $R[[x]]$, and $R[[x]]$ is a **complete metric space** under $d$. Intuitively, two series $F$ and $G$ are "close" in the $x$-adic topology if their coefficients agree up to a high power of $x$, i.e., $F(x) \equiv G(x) \pmod{x^N}$ for large $N$.

> [!IMPORTANT]
> **Criterion for Formal Summability and Multiplicability**:
> 1. **Infinite Sum $\sum_{k=0}^{\infty} F_k(x)$**: A family of formal power series $\{F_k(x)\}_{k \ge 0}$ is **formally summable** in $R[[x]]$ if and only if
>    $$\lim_{k \to \infty} \operatorname{val}(F_k) = +\infty.$$
>    Why? Because for any fixed target exponent $n \ge 0$, there exists an index $K(n)$ such that $\operatorname{val}(F_k) > n$ for all $k > K(n)$. Thus $[x^n]F_k(x) = 0$ for all $k > K(n)$, reducing the $n$-th coefficient of the infinite sum to a **finite sum**:
>    $$[x^n] \sum_{k=0}^{\infty} F_k(x) := \sum_{k=0}^{K(n)} [x^n] F_k(x).$$
> 2. **Infinite Product $\prod_{k=1}^{\infty} (1 + H_k(x))$**: The infinite product is well-defined in $R[[x]]$ if and only if $\operatorname{val}(H_k) \ge 1$ for all $k$ (or after finitely many $k$) and
>    $$\lim_{k \to \infty} \operatorname{val}(H_k) = +\infty.$$
>    For instance, in the partition product $\prod_{k=1}^{\infty} (1 + x^k + x^{2k} + \dots)$, the $k$-th factor has $H_k(x) = x^k + x^{2k} + \dots$ with $\operatorname{val}(H_k) = k \to \infty$. To compute $[x^n]$, any factor with $k > n$ contributes only $1$, so $[x^n]\prod_{k=1}^{\infty}(1-x^k)^{-1} = [x^n]\prod_{k=1}^{n}(1-x^k)^{-1}$.

---

### 53.3 Multiplicative Inverses and Formal Laurent Series $K((x))$

#### Concrete Algebraic Object: Units $R[[x]]^\times$ vs. Formal Laurent Series $K((x))$

When can we divide by a formal power series $F(x) = \sum_{n=0}^{\infty} a_n x^n$?

##### Diagnostic Signal
You have an equation $F(x) G(x) = H(x)$ and want to write $G(x) = H(x) F(x)^{-1}$, or you need to invert $1 - A(x)$ in a recurrence or $\operatorname{SEQ}(A)$ construction. Before writing $F(x)^{-1}$, you must check the constant term $[x^0]F(x) = a_0$.

##### Reverse-Engineering Scratchpad (Deriving the Invertibility Condition)
Suppose $G(x) = \sum_{n=0}^{\infty} b_n x^n \in R[[x]]$ satisfies $F(x) G(x) = 1$. Let us extract coefficients on both sides starting from $n = 0$:
- At $n = 0$: $[x^0](F \cdot G) = a_0 b_0 = [x^0]1 = 1$.
  This single equation immediately forces $a_0$ to have a multiplicative inverse $b_0 = a_0^{-1}$ in the base ring $R$! If $a_0 = 0$ (or if $R = \mathbb{Z}$ and $a_0 = 2$), no $b_0 \in R$ can satisfy $a_0 b_0 = 1$.
- At $n \ge 1$: $[x^n](F \cdot G) = \sum_{k=0}^{n} a_k b_{n-k} = a_0 b_n + \sum_{k=1}^{n} a_k b_{n-k} = 0$.
  Since $a_0 \in R^\times$ is already invertible, we can uniquely isolate $b_n$ in terms of $b_0, \dots, b_{n-1}$:
  $$b_n = -a_0^{-1} \sum_{k=1}^{n} a_k b_{n-k}.$$

##### Theorem (Characterization of Invertible FPS)
A formal power series $F(x) \in R[[x]]$ has a multiplicative inverse $F(x)^{-1} \in R[[x]]$ if and only if its constant term is a unit in $R$:
$$F(x) \in R[[x]]^\times \iff [x^0]F(x) \in R^\times.$$
When $R = K$ is a field (e.g., $\mathbb{Q}$, $\mathbb{C}$, or $\mathbb{F}_p$), $K^\times = K \setminus \{0\}$, so $F(x)$ is invertible in $K[[x]]$ if and only if $[x^0]F(x) \ne 0$ (equivalently, $\operatorname{val}(F) = 0$).

##### What if $[x^0]F(x) = 0$? The Field of Formal Laurent Series $K((x))$
In many problems (for example, inverting $F(x) = x^2 - x^3$ or applying Lagrange Inversion), we must divide by a non-zero series $F(x) \in K[[x]]$ whose valuation is $v = \operatorname{val}(F) \ge 1$.
We can factor out $x^v$ uniquely:
$$F(x) = x^v \tilde{F}(x), \quad \text{where } \tilde{F}(x) = \sum_{n=0}^{\infty} a_{n+v} x^n \text{ has } [x^0]\tilde{F}(x) = a_v \ne 0.$$
Since $[x^0]\tilde{F}(x) \ne 0$ in the field $K$, $\tilde{F}(x)$ has a genuine inverse $\tilde{F}(x)^{-1} \in K[[x]]$. Therefore, the inverse of $F(x)$ lives in the **field of formal Laurent series** $K((x))$:
$$F(x)^{-1} = x^{-v} \tilde{F}(x)^{-1} = \sum_{n=-v}^{\infty} c_n x^n \in K((x)).$$
Formally, $K((x)) = K[[x]][x^{-1}]$ consists of series of the form $\sum_{n=N}^{\infty} c_n x^n$ with $N \in \mathbb{Z}$ (allowing **finitely many** negative powers of $x$, but infinitely many positive powers). It is the field of fractions of the integral domain $K[[x]]$.

> [!WARNING]
> **Why doubly-infinite series $\sum_{n=-\infty}^{\infty} c_n x^n$ DO NOT form a ring**:
> If you allow infinitely many negative powers AND infinitely many positive powers simultaneously, multiplication breaks down! For example, multiplying $\left(\sum_{n=-\infty}^{\infty} x^n\right)$ by itself would require computing $[x^0] = \sum_{k=-\infty}^{\infty} 1 \cdot 1$, an infinite sum of $1$s that does not converge in the formal topology. Always keep Laurent series bounded below ($n \ge N > -\infty$).

---

### 53.4 Formal Composition $F(G(x))$ and Compositional Inverses

#### Concrete Algebraic Object: Substituting $G(x)$ into $F(x)$

Given $F(x) = \sum_{k=0}^{\infty} f_k x^k \in R[[x]]$ and $G(x) = \sum_{m=0}^{\infty} g_m x^m \in R[[x]]$, we define the **formal composition** $(F \circ G)(x) = F(G(x))$ as the infinite sum:
$$F(G(x)) := \sum_{k=0}^{\infty} f_k \big(G(x)\big)^k.$$

##### Diagnostic Signal
You want to evaluate $\exp(G(x))$, $\ln(1 + G(x))$, $(1 - G(x))^{-1}$, or substitute a sub-structure generating function $G(x)$ into an outer structure $F(x)$.

##### Reverse-Engineering Scratchpad (Why $[x^0]G(x) = 0$ is Mandatory)
When is the infinite sum $\sum_{k=0}^{\infty} f_k G(x)^k$ formally summable for *arbitrary* $F \in R[[x]]$?
By our formal summability criterion (Section 53.2), we need $\operatorname{val}\big(f_k G(x)^k\big) \to \infty$ as $k \to \infty$ for every choice of coefficients $f_k$ (for instance, $f_k = 1$ for all $k$).
- Suppose $[x^0]G(x) = g_0 \ne 0$, so $\operatorname{val}(G) = 0$. Then $[x^0]\big(G(x)^k\big) = g_0^k$. Consequently, computing the constant term $[x^0]F(G(x))$ alone would require evaluating the infinite sum $\sum_{k=0}^{\infty} f_k g_0^k$ in $R$, which is meaningless in $R[[x]]$ unless $F$ is a finite polynomial!
- Conversely, suppose $[x^0]G(x) = 0$, meaning $\operatorname{val}(G) \ge 1$. Then $G(x) = x \tilde{G}(x)$, so $G(x)^k = x^k \tilde{G}(x)^k$, which implies:
  $$\operatorname{val}\big(G(x)^k\big) \ge k.$$
  Therefore, for any target degree $n \ge 0$, every term $f_k G(x)^k$ with $k > n$ has valuation at least $n + 1$, so $[x^n]\big(G(x)^k\big) = 0$ for all $k > n$!

##### Explicit Coefficient Formula for Formal Composition
Whenever $\operatorname{val}(G) \ge 1$ (i.e., $[x^0]G(x) = 0$), $F(G(x))$ is well-defined for all $F \in R[[x]]$, and its $n$-th coefficient is the **finite** sum:
$$[x^n] F(G(x)) = \sum_{k=0}^{n} f_k [x^n] \big(G(x)^k\big).$$

##### Compositional Inverse $F^{\langle -1 \rangle}(x)$
When does $F(x) \in R[[x]]$ have a **compositional inverse** $H(x) \in R[[x]]$ satisfying $F(H(x)) = x$ and $H(F(x)) = x$?
1. First, for $F(H(x))$ and $H(F(x))$ to be well-defined, we must have $[x^0]F(x) = 0$ and $[x^0]H(x) = 0$.
2. Second, write $F(x) = f_1 x + f_2 x^2 + \dots$ and $H(x) = h_1 x + h_2 x^2 + \dots$. Extracting $[x^1]F(H(x)) = [x^1]x = 1$ gives:
   $$f_1 h_1 = 1.$$
   Thus $F$ has a compositional inverse in $R[[x]]$ if and only if **$[x^0]F(x) = 0$ and $[x^1]F(x) \in R^\times$** (i.e., $\operatorname{val}(F) = 1$ when $R = K$ is a field).

---

### 53.5 The Formal Operator Calculus: $D = \frac{d}{dx}$, $\vartheta = x\frac{d}{dx}$, and $\int_0^x$

In competitive programming, recurrence relations and combinatorial sums frequently contain polynomial weights in the index $n$, such as $n a_n$, $n^2 a_n$, $\binom{n}{k} a_n$, or $\frac{a_n}{n+1}$. The key to translating these index weights into algebra on $F(x) = \sum_{n=0}^{\infty} a_n x^n$ is the **formal operator calculus**.

#### Concrete Algebraic Objects: Three Linear Operators on $R[[x]]$

1. **Formal Derivative $D = \frac{d}{dx}$**:
   $$D F(x) = F'(x) := \sum_{n=1}^{\infty} n a_n x^{n-1} = \sum_{n=0}^{\infty} (n+1) a_{n+1} x^n.$$
   That is, $[x^n] F'(x) = (n+1) [x^{n+1}] F(x)$. Notice that $D$ combines two effects: it multiplies each coefficient $a_n$ by its index $n$, and it **shifts the exponent down by $1$** ($x^n \mapsto x^{n-1}$).
2. **Pointing / Theta / Euler Operator $\vartheta = x D = x\frac{d}{dx}$**:
   $$\vartheta F(x) = x F'(x) := \sum_{n=0}^{\infty} n a_n x^n.$$
   That is, $[x^n] (\vartheta F)(x) = n [x^n] F(x)$. Unlike $D$, the operator $\vartheta$ **preserves the exponent $x^n$**! Iterating $\vartheta$ $k$ times produces pure power weights:
   $$[x^n] (\vartheta^k F)(x) = n^k [x^n] F(x).$$
3. **Formal Integration $\int_0^x$**:
   Assuming $1, 2, \dots, n+1$ are invertible in $R$ (e.g., $R = \mathbb{Q}$ or $R = \mathbb{F}_p$ for $n + 1 < p$), the formal integral with zero constant term is:
   $$\int_0^x F(t)\,dt := \sum_{n=0}^{\infty} \frac{a_n}{n+1} x^{n+1} = \sum_{n=1}^{\infty} \frac{a_{n-1}}{n} x^n.$$
   That is, $[x^0]\int_0^x F(t)\,dt = 0$ and $[x^n]\int_0^x F(t)\,dt = \frac{1}{n}[x^{n-1}]F(x)$ for $n \ge 1$.

#### Algebraic Rules of $D$ and $\vartheta$ (Verified Purely via Coefficients)

All standard rules of differential calculus hold in $R[[x]]$ without limits:
- **Linearity**: $D(\alpha F + \beta G) = \alpha DF + \beta DG$.
- **Leibniz Product Rule**: $D(F \cdot G) = (DF)G + F(DG)$, and $\vartheta(F \cdot G) = (\vartheta F)G + F(\vartheta G)$.
- **Quotient Rule**: When $G \in R[[x]]^\times$, $D(F/G) = \frac{(DF)G - F(DG)}{G^2}$.
- **Chain Rule**: When $\operatorname{val}(G) \ge 1$,
  $$D\big(F(G(x))\big) = F'(G(x)) \cdot G'(x), \qquad \vartheta\big(F(G(x))\big) = F'(G(x)) \cdot \vartheta G(x).$$
- **Higher Derivatives and Rising/Falling Factorials**:
  $$D^k F(x) = \sum_{n=k}^{\infty} n^{\underline{k}} a_n x^{n-k} = \sum_{n=0}^{\infty} (n+k)^{\underline{k}} a_{n+k} x^n, \qquad x^k D^k F(x) = \sum_{n=0}^{\infty} n^{\underline{k}} a_n x^n,$$
  where $n^{\underline{k}} = n(n-1)\cdots(n-k+1) = k!\binom{n}{k}$ is the falling factorial.

---

### 53.6 How to Discover Operator Manipulations: Diagnostic Signals & Reverse-Engineering Scratchpads

#### Diagnostic Signal Table for Index Weights in Recurrences and Sums

| Term in Recurrence / Sum | What You Want on $x^n$ | Operator Translation on $F(x) = \sum_{n\ge 0} a_n x^n$ | Shift / Alignment Notes |
| :--- | :--- | :--- | :--- |
| $a_{n-k}$ | Shift index by $+k$ | $x^k F(x)$ | Zero-pads $[x^0], \dots, [x^{k-1}]$ |
| $a_{n+1}$ | Shift index by $-1$ | $\frac{F(x) - a_0}{x}$ | Must subtract boundary term $a_0$ before dividing by $x$ |
| $n a_n$ | Multiply $a_n$ by $n$ in-place | $\vartheta F(x) = x F'(x)$ | Preserves degree $x^n$ |
| $(n+1) a_{n+1}$ | Multiply by index and shift $-1$ | $D F(x) = F'(x)$ | Shifts $x^{n+1} \mapsto x^n$ |
| $(n-1) a_{n-1}$ | Multiply shifted index | $x^2 F'(x)$ | Since $\sum (n-1)a_{n-1}x^n = x \sum m a_m x^m = x(xF'(x))$ |
| $n^2 a_n$ | Multiply $a_n$ by $n^2$ | $\vartheta^2 F(x) = x(xF'(x))' = x^2 F''(x) + x F'(x)$ | Expand via Stirling numbers $n^k = \sum_{j=0}^k \left\{ \begin{matrix} k \\ j \end{matrix} \right\} n^{\underline{j}}$ |
| $\binom{n}{k} a_n$ | Multiply $a_n$ by $\binom{n}{k}$ | $\frac{x^k}{k!} D^k F(x) = \frac{x^k}{k!} F^{(k)}(x)$ | Preserves degree $x^n$ |
| $\frac{a_n}{n+1}$ | Divide $a_n$ by $n+1$ | $\frac{1}{x} \int_0^x F(t)\,dt$ | Requires $1, \dots, n+1 \in R^\times$ |
| $\frac{a_n}{n}$ ($n \ge 1$) | Divide $a_n$ by $n$ | $\int_0^x \frac{F(t) - a_0}{t}\,dt$ | Requires $a_0$ subtracted first |

#### Reverse-Engineering Scratchpad 1: Converting a Polynomial-Coefficient Recurrence into an ODE

Suppose a contest problem gives the recurrence:
$$(n + 2) a_{n+1} = (2n + 1) a_n + 3n a_{n-1} \quad (n \ge 1), \quad a_0 = 1, a_1 = 2.$$
How does a solver systematically turn this into a differential equation for $F(x) = \sum_{n=0}^{\infty} a_n x^n$ **without guessing**?

1. **Step 1 (Align every term's coefficient multiplier with its own subscript!)**:
   Look at the three terms: $(n+2)a_{n+1}$, $(2n+1)a_n$, and $3n a_{n-1}$.
   The operators $D$ and $\vartheta = xD$ multiply $a_m$ by its **own** subscript $m$! Therefore, we rewrite every polynomial multiplier in terms of the subscript of the $a_\bullet$ it multiplies:
   - Left-hand side has $a_{n+1}$, so rewrite $n+2$ in terms of $(n+1)$:
     $$(n+2) a_{n+1} = (n+1) a_{n+1} + 1 \cdot a_{n+1}.$$
   - First right-hand term has $a_n$, which is already in terms of $n$:
     $$(2n+1) a_n = 2(n a_n) + 1 \cdot a_n.$$
   - Second right-hand term has $a_{n-1}$, so rewrite $3n$ in terms of $(n-1)$:
     $$3n a_{n-1} = 3(n-1) a_{n-1} + 3 a_{n-1}.$$
2. **Step 2 (Multiply by $x^n$ and sum over the valid range $n \ge 1$)**:
   $$\sum_{n=1}^{\infty} (n+1)a_{n+1} x^n + \sum_{n=1}^{\infty} a_{n+1} x^n = 2 \sum_{n=1}^{\infty} n a_n x^n + \sum_{n=1}^{\infty} a_n x^n + 3 \sum_{n=1}^{\infty} (n-1)a_{n-1} x^n + 3 \sum_{n=1}^{\infty} a_{n-1} x^n.$$
3. **Step 3 (Translate each sum using the dictionary, carefully restoring missing $n=0$ boundary terms)**:
   - $\sum_{n=1}^{\infty} (n+1)a_{n+1}x^n = F'(x) - a_1$.
   - $\sum_{n=1}^{\infty} a_{n+1}x^n = \frac{F(x) - a_0 - a_1 x}{x}$.
   - $2\sum_{n=1}^{\infty} n a_n x^n = 2 x F'(x)$ (since the $n=0$ term $0\cdot a_0$ is zero anyway).
   - $\sum_{n=1}^{\infty} a_n x^n = F(x) - a_0$.
   - $3\sum_{n=1}^{\infty} (n-1)a_{n-1} x^n = 3x \sum_{m=0}^{\infty} m a_m x^m = 3 x^2 F'(x)$.
   - $3\sum_{n=1}^{\infty} a_{n-1} x^n = 3x \sum_{m=0}^{\infty} a_m x^m = 3x F(x)$.
4. **Step 4 (Assemble the ODE)**:
   Substituting $a_0 = 1, a_1 = 2$ yields a linear first-order ODE in $F'(x)$ and $F(x)$:
   $$F'(x) - 2 + \frac{F(x) - 1 - 2x}{x} = (2x + 3x^2) F'(x) + (1 + 3x) F(x) - 1.$$

> [!TIP]
> **The Golden Rule of Index-Multiplier Alignment**:
> Before summing $\sum_{n} P(n) a_{n+s} x^n$, ALWAYS expand $P(n)$ as a polynomial (or falling factorial) in the shifted index $m = n + s$. Once every term has the form $m^k a_m x^{m-s} = x^{-s} (m^k a_m x^m)$, it translates immediately to $x^{-s} (\vartheta^k F)(x)$ minus finite boundary terms!

#### Reverse-Engineering Scratchpad 2: Using $D$ and $\ln$ to Linearize Powers and Products

Suppose we want to compute $H(x) = \big(F(x)\big)^k \bmod x^n$ where $F(0) = 1$, or solve $G(x) = \exp(F(x)) \bmod x^n$, without paying $O(\log k)$ polynomial multiplications.
How do we discover the differential equation trick?
1. Look at $H(x) = F(x)^k$. Powering is non-linear, but differentiation brings the exponent $k$ down as a linear scalar multiplier:
   $$H'(x) = k F(x)^{k-1} F'(x).$$
2. We do not want $F(x)^{k-1}$—we want $H(x) = F(x)^k$! Multiply both sides by $F(x)$:
   $$F(x) H'(x) = k F'(x) H(x).$$
3. Now extract $[x^m]$ on both sides for $m \ge 0$:
   $$\sum_{j=0}^{m} [x^{m-j}]F(x) \cdot (j+1) h_{j+1} = k \sum_{j=0}^{m} (j+1) f_{j+1} \cdot h_{m-j}.$$
   If $F(x)$ has at least $S$ non-zero coefficients (sparse polynomial!), this gives an **$O(n S)$ recurrence** for $h_{m+1}$!

---

### 53.7 Prime Characteristic $p > 0$ Obstructions (Crucial for Modular Arithmetic)

In competitive programming, almost all polynomial arithmetic is performed over $\mathbb{F}_p$ where $p$ is a prime (such as $p = 998244353$ or a small prime $p \le N$). While ring addition, Cauchy multiplication, and multiplicative inversion ($[x^0]F \not\equiv 0 \pmod p$) work identically over $\mathbb{F}_p[[x]]$, **differential and integral calculus suffer severe obstructions when the degree $n$ reaches or exceeds $p$**.

#### Obstruction 1: Non-Trivial Kernel of $D$ in Characteristic $p$
Over a field of characteristic $0$ (like $\mathbb{Q}$ or $\mathbb{C}$), $D F(x) = 0 \iff F(x) = a_0$ is a constant series.
Over $\mathbb{F}_p[[x]]$, however, for any multiple of $p$, $n = kp$, we have $n \equiv 0 \pmod p$, so:
$$D(x^{kp}) = kp x^{kp-1} = 0 \pmod p!$$
Therefore, the kernel of the formal derivative over $\mathbb{F}_p[[x]]$ is an infinite-dimensional subring:
$$\ker\big(D : \mathbb{F}_p[[x]] \to \mathbb{F}_p[[x]]\big) = \mathbb{F}_p[[x^p]] = \left\{\sum_{k=0}^{\infty} c_k x^{kp} : c_k \in \mathbb{F}_p\right\}.$$
Consequently, knowing $F'(x)$ and $F(0)$ in $\mathbb{F}_p[[x]]$ uniquely determines $[x^n]F(x)$ **only for $1 \le n < p$**! At $n = p$, $[x^{p-1}]F'(x) = p \cdot a_p \equiv 0 \pmod p$ destroys all information about $a_p$.

#### Obstruction 2: Failure of Formal Integration $\int_0^x$, $\ln$, and $\exp$ for $n \ge p$
Because $[x^n] \int_0^x F(t)\,dt = \frac{1}{n} [x^{n-1}]F(x)$, computing the $n$-th coefficient of the formal integral requires dividing by $n$ in the base ring $R$.
- Over $\mathbb{F}_p$, $n$ is invertible if and only if $p \nmid n$.
- Specifically, $\int_0^x x^{p-1}\,dt = \frac{x^p}{p}$ **does not exist** in $\mathbb{F}_p[[x]]$!
- Because $\ln(1 + G(x)) = \int_0^x \frac{G'(t)}{1 + G(t)}\,dt$ and $\exp(G(x)) = \sum_{k=0}^{\infty} \frac{G(x)^k}{k!}$ both divide by $1, 2, \dots, n$, **formal $\ln(F(x)) \bmod x^{N}$ and $\exp(G(x)) \bmod x^{N}$ are defined over $\mathbb{F}_p$ only when $N \le p$** (i.e., up to degree $n \le p - 1$).

---

### 53.8 Hand-Checkable Toy Trace ($n \le 4$) & Failure Modes

#### Worked Toy Trace: Computing $F(x) = (1 - x - x^2)^{-1}$ and $\vartheta F(x)$ up to $x^4$
Let $P(x) = 1 - x - x^2 \in \mathbb{Q}[[x]]$. Since $[x^0]P(x) = 1 \in \mathbb{Q}^\times$, $F(x) = P(x)^{-1} = \sum_{n\ge 0} f_n x^n$ exists in $\mathbb{Q}[[x]]$.
Using $f_0 = 1$ and $f_n = -\sum_{k=1}^n p_k f_{n-k} = f_{n-1} + f_{n-2}$:
- $n = 0$: $f_0 = 1$
- $n = 1$: $f_1 = f_0 = 1$
- $n = 2$: $f_2 = f_1 + f_0 = 2$
- $n = 3$: $f_3 = f_2 + f_1 = 3$
- $n = 4$: $f_4 = f_3 + f_2 = 5$
So $F(x) = 1 + x + 2x^2 + 3x^3 + 5x^4 + O(x^5)$.
Now let us verify $\vartheta F(x) = x F'(x) = \sum_{n\ge 0} n f_n x^n$ via the quotient rule:
$$\vartheta F(x) = x \frac{d}{dx}(1 - x - x^2)^{-1} = \frac{x(1 + 2x)}{(1 - x - x^2)^2} = (x + 2x^2) F(x)^2.$$
Let us check up to $x^4$:
- $F(x)^2 = (1 + x + 2x^2 + 3x^3 + 5x^4)^2 = 1 + 2x + 5x^2 + 10x^3 + 20x^4 + O(x^5)$.
- Multiply by $(x + 2x^2)$:
  $$(x + 2x^2)(1 + 2x + 5x^2 + 10x^3 + \dots) = x + (2+2)x^2 + (5+4)x^3 + (10+10)x^4 + O(x^5) = 1x + 4x^2 + 9x^3 + 20x^4 + O(x^5).$$
Comparing coefficients with $n f_n$:
- $n = 1$: $1 \cdot f_1 = 1 \cdot 1 = 1$ (matches $1x$)
- $n = 2$: $2 \cdot f_2 = 2 \cdot 2 = 4$ (matches $4x^2$)
- $n = 3$: $3 \cdot f_3 = 3 \cdot 3 = 9$ (matches $9x^3$)
- $n = 4$: $4 \cdot f_4 = 4 \cdot 5 = 20$ (matches $20x^4$). Exact match!

#### Summary of Failure Modes & Edge Cases in Iteration 53
1. **Boundary Term Omission when Shifting**: Writing $\sum_{n=0}^{\infty} a_{n+1} x^n = \frac{F(x)}{x}$ instead of $\frac{F(x) - a_0}{x}$. Always verify at $x = 0$ (constant term)!
2. **Non-Zero Constant Term in Composition / $\exp$ / $\ln$**: Calling `exp(G)` when $[x^0]G \ne 0$, or `ln(F)` when $[x^0]F \ne 1$. In $\mathbb{F}_p[[x]]$, $\exp(c + \tilde{G})$ does not even have a natural meaning in $\mathbb{F}_p$ unless $e^c$ is defined externally.
3. **Characteristic $p \le N$ Division by Zero**: Using polynomial $\ln$, $\exp$, or ODE integration when the modulus $p$ is smaller than the required degree $N$ (e.g., $p = 10007$ and $N = 50000$).
4. **Conflating $D = \frac{d}{dx}$ and $\vartheta = x\frac{d}{dx}$**: Iterating $D^k$ produces falling factorials $n^{\underline{k}}$ and shifts degree by $-k$, whereas iterating $\vartheta^k$ produces pure powers $n^k$ and preserves degree.

---

## Iteration 54: Unlabelled Symbolic Method & Ordinary Generating Functions (OGFs)

### 54.1 The Unlabelled Combinatorial Universe and Flajolet–Sedgewick Operators

#### Concrete Combinatorial Object: Unlabelled Combinatorial Class $(\mathcal{A}, |\cdot|)$

Following Flajolet and Sedgewick (*Analytic Combinatorics*, Part A), an **unlabelled combinatorial class** is a set $\mathcal{A}$ of discrete objects equipped with a size function $|\cdot| : \mathcal{A} \to \mathbb{Z}_{\ge 0}$ such that for every integer $n \ge 0$, the subset $\mathcal{A}_n := \{\alpha \in \mathcal{A} : |\alpha| = n\}$ is finite.
Because the atoms making up an object carry **no distinguishing labels** (two objects are identical if they are isomorphic), we associate to $\mathcal{A}$ its **Ordinary Generating Function (OGF)** in $\mathbb{Q}[[x]]$:
$$A(x) = \sum_{\alpha \in \mathcal{A}} x^{|\alpha|} = \sum_{n=0}^{\infty} a_n x^n, \qquad \text{where } a_n = |\mathcal{A}_n|.$$

Two elementary atomic classes form the building blocks of all specifications:
- **Neutral class $\mathcal{E} = \{\epsilon\}$**: Contains a single empty/neutral object of size $|\epsilon| = 0$. Its OGF is $E(x) = x^0 = 1$.
- **Atomic class $\mathcal{Z} = \{\bullet\}$**: Contains a single unlabelled atom of size $|\bullet| = 1$. Its OGF is $Z(x) = x^1 = x$.

#### The Fundamental Unlabelled Operator Dictionary

| Combinatorial Construction | Notation | Meaning on Objects $\gamma$ | Size Law $|\gamma|$ | OGF Translation $C(x)$ | Validity Condition |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Disjoint Union** | $\mathcal{C} = \mathcal{A} + \mathcal{B}$ | Choose $\gamma \in \mathcal{A}$ OR $\gamma \in \mathcal{B}$ ($\mathcal{A} \cap \mathcal{B} = \emptyset$) | $\|\gamma\|_{\mathcal{A}}$ or $\|\gamma\|_{\mathcal{B}}$ | $A(x) + B(x)$ | Always valid |
| **Cartesian Product** | $\mathcal{C} = \mathcal{A} \times \mathcal{B}$ | Ordered pair $\gamma = (\alpha, \beta)$ with $\alpha \in \mathcal{A}, \beta \in \mathcal{B}$ | $\|\alpha\| + \|\beta\|$ | $A(x) \cdot B(x)$ | Always valid |
| **Sequence** | $\mathcal{C} = \operatorname{SEQ}(\mathcal{A})$ | Ordered tuple $(\alpha_1, \dots, \alpha_k)$ of any length $k \ge 0$ | $\sum_{i=1}^k \|\alpha_i\|$ | $\frac{1}{1 - A(x)}$ | $[x^0]A(x) = 0$ ($\mathcal{A}_0 = \emptyset$) |
| **Length-$k$ Sequence** | $\mathcal{C} = \operatorname{SEQ}_k(\mathcal{A})$ | Ordered $k$-tuple $(\alpha_1, \dots, \alpha_k)$ | $\sum_{i=1}^k \|\alpha_i\|$ | $A(x)^k$ | Always valid |
| **Powerset (Subset)** | $\mathcal{C} = \operatorname{PSET}(\mathcal{A})$ | Unordered subset of **distinct** elements from $\mathcal{A}$ | $\sum_{\alpha \in S} \|\alpha\|$ | $\prod_{k=1}^{\infty} (1 + x^k)^{a_k} = \exp\!\left(\sum_{j=1}^{\infty} \frac{(-1)^{j-1}}{j} A(x^j)\right)$ | $[x^0]A(x) = 0$ |
| **Multiset** | $\mathcal{C} = \operatorname{MSET}(\mathcal{A})$ | Unordered multiset (repetitions allowed) from $\mathcal{A}$ | $\sum_{\alpha \in M} m(\alpha)\|\alpha\|$ | $\prod_{k=1}^{\infty} \frac{1}{(1 - x^k)^{a_k}} = \exp\!\left(\sum_{j=1}^{\infty} \frac{A(x^j)}{j}\right)$ | $[x^0]A(x) = 0$ |
| **Directed Cycle** | $\mathcal{C} = \operatorname{CYC}(\mathcal{A})$ | Necklace / directed cycle of $\ge 1$ objects from $\mathcal{A}$ up to rotation | $\sum_{i=1}^k \|\alpha_i\|$ | $\sum_{d=1}^{\infty} \frac{\varphi(d)}{d} \ln\frac{1}{1 - A(x^d)}$ | $[x^0]A(x) = 0$ |

> [!CAUTION]
> **Why $[x^0]A(x) = 0$ is Mandatory for $\operatorname{SEQ}(\mathcal{A})$, $\operatorname{MSET}(\mathcal{A})$, and $\operatorname{CYC}(\mathcal{A})$**:
> Combinatorially, if $\mathcal{A}$ contained an object $\epsilon$ of size $0$, we could insert arbitrarily many copies of $\epsilon$ into a sequence or multiset without changing its total size $n$, producing **infinitely many** objects of size $n$ ($c_n = \infty$). Algebraically, $[x^0]A(x) = 0 \iff \operatorname{val}(A) \ge 1$, which is the exact condition from Section 53.4 required for $(1 - A(x))^{-1} = \sum_{k\ge 0} A(x)^k$ to be formally summable!

---

### 54.2 The Multiset Operator $\operatorname{MSET}(\mathcal{A})$ and the Euler Transform

#### 1. Concrete Combinatorial Object
Let $\mathcal{A}$ be an unlabelled class with $a_0 = 0$ and $a_k = |\mathcal{A}_k|$ distinct objects of size $k$ for each $k \ge 1$. We want to count $\mathcal{C} = \operatorname{MSET}(\mathcal{A})$, the class of **unordered multisets** of objects chosen from $\mathcal{A}$, where:
- The order in which objects are chosen does **not** matter;
- Any individual object $\alpha \in \mathcal{A}_k$ can be chosen $0, 1, 2, \dots$ times;
- Total size is the sum of sizes of the chosen objects (with multiplicity).

Classic examples:
1. **Unlabelled Rooted Trees & Forests**: Removing the root of an unlabelled non-plane rooted tree of size $n$ leaves an **unordered multiset** (forest) of unlabelled rooted subtrees of total size $n-1$: $\mathcal{T} = \mathcal{Z} \times \operatorname{MSET}(\mathcal{T})$.
2. **Colored Integer Partitions / Unbounded Knapsack Ways**: We have $a_k$ distinct item types of weight $k$, each in infinite supply, and want the number of ways $f_n$ to form total weight $n$.

#### 2. Diagnostic Signal
Reach for the **Euler Transform** whenever you see:
- "Unlabelled", "up to isomorphism", or "unordered collection of components where identical components cannot be distinguished from one another."
- A product of the form $\prod_{k=1}^{N} (1 - x^k)^{-a_k}$ or $\prod_{i=1}^{M} (1 - x^{w_i})^{-1}$ or $\prod_{i=1}^{M} (1 + x^{w_i})$ that must be expanded up to $x^N$ in $O(N \log N)$ time.

#### 3. Reverse-Engineering Scratchpad (Deriving the Euler Transform & Its $\exp$ Form)

**Step A: From Combinatorial Choice to the Infinite Product**.
Consider a single fixed object $\alpha \in \mathcal{A}_k$ of size $k$. In any multiset $M \in \operatorname{MSET}(\mathcal{A})$, how many times can $\alpha$ appear?
It can appear $m = 0, 1, 2, \dots$ times, contributing $0, k, 2k, \dots$ to the total size. Thus the OGF for the choices of multiplicity of this **single** object $\alpha$ is:
$$1 + x^k + x^{2k} + x^{3k} + \dots = \frac{1}{1 - x^k}.$$
Since there are $a_k$ distinct objects in $\mathcal{A}_k$, and the multiplicity of each distinct object $\alpha \in \mathcal{A}$ is chosen **independently**, the Cartesian product rule over all objects $\alpha \in \bigcup_{k\ge 1} \mathcal{A}_k$ gives:
$$F(x) = \prod_{\alpha \in \mathcal{A}} \frac{1}{1 - x^{|\alpha|}} = \prod_{k=1}^{\infty} \left(\frac{1}{1 - x^k}\right)^{a_k} = \prod_{k=1}^{\infty} (1 - x^k)^{-a_k}.$$

**Step B: Why the Product Form is Computationally Stuck, and How $\ln / \exp$ Unlocks It**.
If we try to multiply $(1 - x^k)^{-a_k}$ one $k$ at a time up to $x^N$, it takes $O(N^2)$ time. How can we convert an infinite product into an infinite sum, and collapse the inner sum in $O(N \log N)$?
Take the formal logarithm $\ln F(x)$! Since $[x^0]F(x) = 1$, $\ln F(x)$ is well-defined:
$$\ln F(x) = \ln \prod_{k=1}^{\infty} (1 - x^k)^{-a_k} = \sum_{k=1}^{\infty} -a_k \ln(1 - x^k).$$
Now substitute the expansion $-\ln(1 - u) = \sum_{j=1}^{\infty} \frac{u^j}{j}$ with $u = x^k$:
$$\ln F(x) = \sum_{k=1}^{\infty} a_k \sum_{j=1}^{\infty} \frac{x^{jk}}{j}.$$
Now look closely at the double sum: if we interchange the summation order (valid because $\operatorname{val}(x^{jk}) = jk \to \infty$), grouping by $j$ first:
$$\ln F(x) = \sum_{j=1}^{\infty} \frac{1}{j} \left(\sum_{k=1}^{\infty} a_k (x^j)^k\right) = \sum_{j=1}^{\infty} \frac{A(x^j)}{j}!$$
Exponentiating both sides yields Pólya's / Flajolet–Sedgewick's **Exponential Form of the Euler Transform**:
$$F(x) = \operatorname{MSET}(\mathcal{A})(x) = \prod_{k=1}^{\infty} \frac{1}{(1 - x^k)^{a_k}} = \exp\!\left(\sum_{j=1}^{\infty} \frac{A(x^j)}{j}\right).$$

Similarly, for the **Powerset Operator** $\operatorname{PSET}(\mathcal{A})$, each object $\alpha \in \mathcal{A}_k$ can be chosen at most once ($1 + x^k$), giving:
$$\operatorname{PSET}(\mathcal{A})(x) = \prod_{k=1}^{\infty} (1 + x^k)^{a_k} = \exp\!\left(\sum_{k=1}^{\infty} a_k \ln(1 + x^k)\right) = \exp\!\left(\sum_{j=1}^{\infty} \frac{(-1)^{j-1}}{j} A(x^j)\right).$$

---

### 54.3 Two $O(N \log N)$ Algorithms for Euler Transform & Inverse Euler Transform

Let $A(x) = \sum_{k=1}^{N} a_k x^k$ and $F(x) = \prod_{k=1}^{N} (1 - x^k)^{-a_k} \bmod x^{N+1}$. In contest problems, we need both:
- **Forward Euler Transform**: Given $a_1, \dots, a_N$, compute $f_0, \dots, f_N$ in $O(N \log N)$.
- **Inverse Euler Transform**: Given $f_0 = 1, f_1, \dots, f_N$, recover the underlying prime/component counts $a_1, \dots, a_N$ in $O(N \log N)$.

#### Method A: Harmonic Sieve + Polynomial $\exp / \ln$ (The "Fu Princess Knapsack" Trick)

Equating $[x^n] \ln F(x)$ in $\ln F(x) = \sum_{k=1}^{\infty} a_k \sum_{j=1}^{\infty} \frac{x^{jk}}{j}$ by setting $n = j k$ (so $k = d$ runs over all divisors of $n$, and $j = n / d$) gives:
$$g_n := [x^n] \ln F(x) = \sum_{d \mid n} \frac{a_d}{n/d} = \frac{1}{n} \sum_{d \mid n} d \cdot a_d \qquad (n \ge 1).$$

1. **Forward Euler Transform ($A \mapsto F$) in $O(N \log N)$**:
   - Initialize an array $g[0 \dots N] = 0$.
   - For $k = 1, 2, \dots, N$ (whenever $a_k \ne 0$):
     - For $j = 1, 2, \dots, \lfloor N / k \rfloor$:
       - Add $a_k \cdot j^{-1} \bmod p$ to $g[j \cdot k]$.
   - Total work for building $G(x) = \sum_{n=1}^{N} g_n x^n$ is $\sum_{k=1}^N \lfloor N/k \rfloor = O(N \log N)$ operations!
   - Finally, compute $F(x) = \exp(G(x)) \bmod x^{N+1}$ in $O(N \log N)$ time.

2. **Inverse Euler Transform ($F \mapsto A$) in $O(N \log N)$**:
   - Compute $G(x) = \ln F(x) \bmod x^{N+1}$ in $O(N \log N)$ time.
   - For each $n = 1, \dots, N$, set $b_n := n \cdot g_n = \sum_{d \mid n} d \cdot a_d$.
   - Invert the divisor sum in-place in $O(N \log N)$ time (either via Möbius inversion $n a_n = \sum_{d \mid n} \mu(n/d) b_d$, or even simpler by subtracting multiples):
     - For $d = 1, 2, \dots, N$:
       - At this moment $b_d$ equals $d \cdot a_d$, so $a_d = b_d \cdot d^{-1} \bmod p$.
       - For $m = 2d, 3d, \dots \le N$: subtract $b_d$ from $b_m$.

#### Method B: Logarithmic Derivative $\vartheta \ln F = \frac{x F'(x)}{F(x)}$ (Recurrence & Inverse Transform Without $\ln$)

What if we apply the theta operator $\vartheta = x\frac{d}{dx}$ directly to $\ln F(x)$?
$$\vartheta \ln F(x) = \frac{x F'(x)}{F(x)} = \sum_{k=1}^{\infty} a_k \frac{k x^k}{1 - x^k} = \sum_{n=1}^{\infty} \left(\sum_{d \mid n} d \cdot a_d\right) x^n.$$
Let $c_n := \sum_{d \mid n} d \cdot a_d$ and $C(x) = \sum_{n=1}^{\infty} c_n x^n$. Then:
$$x F'(x) = C(x) \cdot F(x) \iff n f_n = \sum_{m=1}^{n} c_m f_{n-m} \quad (n \ge 1, f_0 = 1).$$

Why is Method B essential to know alongside Method A?
1. **When $N \le 5000$ ($O(N^2)$ DP Required)**: You do not need NTT or `exp` at all! Precompute $c_m = \sum_{d \mid m} d a_d$ in $O(N \log N)$, and run $f_n = \frac{1}{n} \sum_{m=1}^n c_m f_{n-m}$ in $O(N^2)$ time with a 5-line loop.
2. **Self-Referential Equations (e.g., Unlabelled Rooted Trees $\mathcal{T} = \mathcal{Z} \times \operatorname{MSET}(\mathcal{T})$)**: Here $a_n = t_n$ is not known in advance—it depends on $f_{n-1} = t_n$! Since $c_m = \sum_{d \mid m} d t_d$ can be updated on the fly as soon as $t_d$ is computed, the recurrence $t_{n+1} = \frac{1}{n} \sum_{m=1}^{n} c_m t_{n+1-m}$ solves unlabelled rooted trees in $O(N^2)$ or $O(N \log^2 N)$ via CDQ divide-and-conquer FFT.

#### Hand-Checkable Toy Trace ($n \le 4$): Counting Unlabelled Non-Plane Rooted Trees
An unlabelled rooted tree of size $n \ge 1$ consists of a root atom of size $1$ attached to an unordered multiset of unlabelled rooted subtrees:
$$\mathcal{T} = \mathcal{Z} \times \operatorname{MSET}(\mathcal{T}) \implies T(x) = x \exp\!\left(\sum_{j=1}^{\infty} \frac{T(x^j)}{j}\right).$$
Let $F(x) = T(x)/x = \sum_{n=0}^{\infty} t_{n+1} x^n$, so $f_n = t_{n+1}$ and $c_m = \sum_{d \mid m} d t_d$. Using $t_1 = f_0 = 1$ and $f_n = \frac{1}{n} \sum_{m=1}^n c_m f_{n-m}$:
- $n = 1$: $c_1 = 1 \cdot t_1 = 1$. Then $t_2 = f_1 = \frac{1}{1}(c_1 f_0) = 1$. (1 tree on 2 vertices: a single edge).
- $n = 2$: $c_2 = 1 \cdot t_1 + 2 \cdot t_2 = 1 + 2 = 3$. Then $t_3 = f_2 = \frac{1}{2}(c_1 f_1 + c_2 f_0) = \frac{1}{2}(1\cdot 1 + 3\cdot 1) = 2$. (2 trees on 3 vertices: path $P_3$ and cherry $K_{1,2}$).
- $n = 3$: $c_3 = 1 \cdot t_1 + 3 \cdot t_3 = 1 + 6 = 7$. Then $t_4 = f_3 = \frac{1}{3}(c_1 f_2 + c_2 f_1 + c_3 f_0) = \frac{1}{3}(1\cdot 2 + 3\cdot 1 + 7\cdot 1) = \frac{12}{3} = 4$. (4 unlabelled rooted trees on 4 vertices).
- $n = 4$: $c_4 = 1\cdot t_1 + 2\cdot t_2 + 4\cdot t_4 = 1 + 2 + 16 = 19$. Then $t_5 = f_4 = \frac{1}{4}(c_1 f_3 + c_2 f_2 + c_3 f_1 + c_4 f_0) = \frac{1}{4}(1\cdot 4 + 3\cdot 2 + 7\cdot 1 + 19\cdot 1) = \frac{36}{4} = 9$.
Sequence $t_1, \dots, t_5 = 1, 1, 2, 4, 9$ (OEIS A000081). Verified!

---

### 54.4 Integer Partitions, Ferrers Diagrams, Durfee Squares, and Euler's Pentagonal Number Theorem

#### 1. Unlabelled Partitions as $\operatorname{MSET}(\mathbb{Z}_{\ge 1})$
An integer partition of $n$ is a non-increasing sequence of positive integers $\lambda = (\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_\ell \ge 1)$ summing to $n$. Equivalently, it is a multiset of positive integers where there is $a_k = 1$ integer of size $k$ for each $k \ge 1$. Thus:
$$P(x) = \sum_{n=0}^{\infty} p_n x^n = \prod_{k=1}^{\infty} \frac{1}{1 - x^k}.$$

#### 2. Ferrers Diagrams and Conjugate Partitions
Representing $\lambda = (\lambda_1, \dots, \lambda_\ell)$ as a left-justified grid of unit boxes with $\lambda_i$ boxes in row $i$ gives its **Ferrers diagram** (or Young diagram). Reflecting the diagram across its main diagonal transposes rows and columns, yielding the **conjugate partition** $\lambda'$.
This geometric bijection immediately equates two seemingly different restrictions:
- Number of partitions of $n$ into **at most $K$ parts** ($\ell(\lambda) \le K$) $\iff$ Number of partitions of $n$ into **parts of size at most $K$** ($\lambda_1 \le K$), with OGF:
  $$P_{\le K}(x) = \prod_{k=1}^{K} \frac{1}{1 - x^k}.$$
- Number of partitions of $n$ into **exactly $K$ parts** $\iff$ Number of partitions of $n$ with **largest part equal to $K$**, with OGF:
  $$P_{=K}(x) = \frac{x^K}{\prod_{k=1}^{K} (1 - x^k)}.$$

#### 3. The Durfee Square Identity ($O(N \sqrt{N})$ Partition Decomposition)

##### Diagnostic Signal
You need to compute $\prod_{k=1}^{\infty}(1 - x^k)^{-1}$ or $\prod_{k=1}^{\infty}(1 + y x^k)$ or constrained partition sums where $K$ varies, or you want an $O(N \sqrt{N})$ DP without using $\ln/\exp$ or NTT.

##### Reverse-Engineering Scratchpad (Geometric Decomposition of the Ferrers Diagram)
In any Ferrers diagram $\lambda$, let $k \ge 0$ be the largest integer such that the diagram contains a $k \times k$ square of boxes in its top-left corner (i.e., $\lambda_k \ge k$, while $\lambda_{k+1} \le k$). This maximal $k \times k$ square is called the **Durfee square** of $\lambda$.
Once the Durfee square of size $k^2$ is removed, the remaining boxes of $\lambda$ split cleanly into two independent pieces:
1. **To the right of the $k \times k$ square**: A Ferrers diagram with **at most $k$ rows**, whose OGF is $\prod_{i=1}^{k} \frac{1}{1 - x^i}$.
2. **Below the $k \times k$ square**: A Ferrers diagram whose rows have **width at most $k$** (parts $\le k$), whose OGF is also $\prod_{i=1}^{k} \frac{1}{1 - x^i}$.

Summing over all possible Durfee square side lengths $k \ge 0$ (where $k^2 \le N$, so $k \le \lfloor\sqrt{N}\rfloor$) gives the **Durfee Square Identity**:
$$\prod_{i=1}^{\infty} \frac{1}{1 - x^i} = \sum_{k=0}^{\infty} \frac{x^{k^2}}{\prod_{i=1}^{k} (1 - x^i)^2}.$$
Because $k \le \sqrt{N}$, we can maintain the denominator $\prod_{i=1}^{k} (1 - x^i)^{-2} \bmod x^{N+1}$ incrementally as $k$ increases from $0$ to $\lfloor\sqrt{N}\rfloor$, performing $2\sqrt{N}$ simple knapsack passes of length $N$ in **$O(N \sqrt{N})$ time and $O(N)$ space**!

Similarly, for **distinct-part partitions** $\lambda_1 > \lambda_2 > \dots > \lambda_k \ge 1$ into $k$ parts, subtracting the staircase $(k, k-1, \dots, 1)$ of size $\binom{k+1}{2} = \frac{k(k+1)}{2}$ leaves a partition into at most $k$ parts:
$$\prod_{i=1}^{\infty} (1 + y x^i) = \sum_{k=0}^{\infty} y^k \frac{x^{k(k+1)/2}}{\prod_{i=1}^{k} (1 - x^i)}.$$

#### 4. Euler's Pentagonal Number Theorem

What is the reciprocal of the partition generating function, $\prod_{k=1}^{\infty} (1 - x^k)$?
Expanding $\prod_{k=1}^{\infty} (1 - x^k) = \sum_{n=0}^{\infty} \big(p_{\text{even}}(n) - p_{\text{odd}}(n)\big) x^n$, where $p_{\text{even}}(n)$ and $p_{\text{odd}}(n)$ count partitions of $n$ into an even or odd number of **distinct** parts, **Franklin's involution (1881)** pairs up almost all distinct-part partitions of $n$ of opposite parity by comparing two segments of the Ferrers diagram:
- $s = \lambda_\ell$: the smallest part (bottom row).
- $d$: the length of the rightmost $45^\circ$ diagonal slope starting from the top-right corner ($\lambda_1, \lambda_2 = \lambda_1 - 1, \dots$).
Moving the bottom row to the rightmost diagonal (when $s \le d$) or moving the rightmost diagonal to a new bottom row (when $s > d$) changes the number of parts by $\pm 1$, flipping the sign $(-1)^\ell$!
This involution fails **if and only if** the bottom row and the rightmost diagonal intersect and block the move, which happens in exactly two cases when there are $m \ge 1$ parts:
1. $s = d = m$: the parts are $(2m-1, 2m-2, \dots, m)$, summing to $\omega(m) = \frac{m(3m-1)}{2}$ with sign $(-1)^m$.
2. $s = d + 1 = m + 1$: the parts are $(2m, 2m-1, \dots, m+1)$, summing to $\omega(-m) = \frac{m(3m+1)}{2}$ with sign $(-1)^m$.

##### Theorem (Euler's Pentagonal Number Theorem)
$$\prod_{k=1}^{\infty} (1 - x^k) = 1 + \sum_{m=1}^{\infty} (-1)^m \left(x^{\frac{m(3m-1)}{2}} + x^{\frac{m(3m+1)}{2}}\right) = \sum_{m=-\infty}^{\infty} (-1)^m x^{\frac{m(3m-1)}{2}}.$$
Consequently:
- Using $\prod_{k=1}^{\infty}(1-x^k) \cdot P(x) = 1$, we get the **$O(N\sqrt{N})$ recurrence**:
  $$p_n = \sum_{m=1}^{\infty} (-1)^{m-1} \left(p_{n - \frac{m(3m-1)}{2}} + p_{n - \frac{m(3m+1)}{2}}\right) = p_{n-1} + p_{n-2} - p_{n-5} - p_{n-7} + p_{n-12} + p_{n-15} - \dots$$
- Or we construct the sparse polynomial $Q(x) = \sum_{\omega(\pm m) \le N} (-1)^m x^{\omega(\pm m)}$ in $O(\sqrt{N})$ time and compute $P(x) = Q(x)^{-1} \bmod x^{N+1}$ via polynomial inversion in **$O(N \log N)$ time** (avoiding $\ln/\exp$ completely!).

---

### 54.5 Unlabelled Cycles $\operatorname{CYC}(\mathcal{A})$ and Pólya / Burnside Cycle Index GFs

#### Diagnostic Signal
You are counting unlabelled **necklaces**, **directed cycles of sub-structures**, or **unlabelled unicyclic graphs** where two cycles are equivalent if one can be rotated into the other.

#### Reverse-Engineering Scratchpad (Why Unlabelled $\operatorname{CYC}$ Needs $\varphi(d)$)
In the labelled world (Iteration 55), a cycle of $k$ distinct labelled objects has $k$ distinct rotations, so we simply divide $A(x)^k$ by $k$.
In the **unlabelled** world, however, a tuple $(\alpha_1, \dots, \alpha_k) \in \mathcal{A}^k$ might be periodic! For instance, if $\alpha_1 = \alpha_2 = \dots = \alpha_k$, rotating the tuple gives the **exact same** tuple, so dividing by $k$ would produce the fraction $1/k$ instead of $1$!
Instead, we apply **Burnside's Lemma** to the cyclic group $C_k = \{r^0, r^1, \dots, r^{k-1}\}$ acting on $\mathcal{A}^k$:
$$\operatorname{CYC}_k(\mathcal{A})(x) = \frac{1}{k} \sum_{j=0}^{k-1} \sum_{\substack{\vec{\alpha} \in \mathcal{A}^k \\ r^j \cdot \vec{\alpha} = \vec{\alpha}}} x^{|\vec{\alpha}|}.$$
When is $\vec{\alpha} = (\alpha_1, \dots, \alpha_k)$ invariant under rotation by $j$ steps?
Rotation by $j$ decomposes the $k$ positions into $g = \gcd(k, j)$ cycles, each of length $d = k / g$. For $\vec{\alpha}$ to be fixed by $r^j$, the objects in each of the $g$ cycles must be identical, so we choose $g = k/d$ objects freely from $\mathcal{A}$, and each chosen object is repeated $d$ times (contributing $d |\alpha|$ to the total size, hence $A(x^d)$ per cycle!).
Since there are $\varphi(d)$ values of $j \in \{0, \dots, k-1\}$ with $k / \gcd(k, j) = d$, we obtain:
$$\operatorname{CYC}_k(\mathcal{A})(x) = \frac{1}{k} \sum_{d \mid k} \varphi(d) \big(A(x^d)\big)^{k/d}.$$
Summing over all cycle lengths $k \ge 1$ and setting $k = d m$:
$$\operatorname{CYC}(\mathcal{A})(x) = \sum_{d=1}^{\infty} \frac{\varphi(d)}{d} \sum_{m=1}^{\infty} \frac{A(x^d)^m}{m} = \sum_{d=1}^{\infty} \frac{\varphi(d)}{d} \ln \frac{1}{1 - A(x^d)}.$$
More generally, for any permutation group $G \le S_k$ with **cycle index polynomial** $Z_G(s_1, s_2, \dots, s_k) = \frac{1}{|G|} \sum_{g \in G} \prod_{i=1}^k s_i^{c_i(g)}$, **Pólya's Enumeration Theorem** states that the OGF of $G$-orbits of configurations $\mathcal{A}^k$ is obtained by substituting $s_i \leftarrow A(x^i)$:
$$\mathcal{C}(x) = Z_G\big(A(x), A(x^2), \dots, A(x^k)\big).$$

---

## Iteration 55: Labelled Symbolic Method & Exponential Generating Functions (EGFs)

### 55.1 Labelled Classes and Why EGFs Normalize by $n!$

#### Concrete Combinatorial Object: Labelled Combinatorial Class $(\mathcal{A}, |\cdot|)$

A **labelled combinatorial class** $\mathcal{A}$ consists of finite structures whose $n = |\alpha|$ atoms bear **distinct canonical labels** $\{1, 2, \dots, n\}$. For instance, a labelled graph on $n$ vertices has vertex set $\{1, 2, \dots, n\}$; a permutation of length $n$ is a collection of disjoint directed cycles on $\{1, 2, \dots, n\}$.
To a labelled class $\mathcal{A}$ with $a_n = |\mathcal{A}_n|$ objects of size $n$, we associate its **Exponential Generating Function (EGF)**:
$$\widehat{A}(x) = \sum_{\alpha \in \mathcal{A}} \frac{x^{|\alpha|}}{|\alpha|!} = \sum_{n=0}^{\infty} a_n \frac{x^n}{n!}.$$
To extract the combinatorial count $a_n$ from $\widehat{A}(x)$, we multiply the $x^n$ coefficient by $n!$:
$$a_n = n! [x^n] \widehat{A}(x).$$

#### Reverse-Engineering Scratchpad (Why Labelled Product $\mathcal{A} \star \mathcal{B}$ Produces Binomial Convolution)

Suppose we want to form an ordered pair $\gamma = (\alpha, \beta)$ of total size $n$ from a labelled class $\mathcal{A}$ and a labelled class $\mathcal{B}$.
Why can we NOT simply pick $\alpha \in \mathcal{A}_k$ and $\beta \in \mathcal{B}_{n-k}$ directly?
Because $\alpha \in \mathcal{A}_k$ is canonically labelled with $\{1, \dots, k\}$ and $\beta \in \mathcal{B}_{n-k}$ is canonically labelled with $\{1, \dots, n-k\}$—their labels collide!
To build a valid labelled object $\gamma$ on $\{1, 2, \dots, n\}$, we must perform a **two-stage relabelling procedure**:
1. **Partition the label set $\{1, 2, \dots, n\}$** into a subset $S \subseteq \{1, \dots, n\}$ of size $k$ (assigned to the first component) and its complement $\overline{S} = \{1, \dots, n\} \setminus S$ of size $n - k$ (assigned to the second component). There are $\binom{n}{k}$ ways to choose $S$.
2. **Choose canonical structures** $\alpha_0 \in \mathcal{A}_k$ ($a_k$ ways) and $\beta_0 \in \mathcal{B}_{n-k}$ ($b_{n-k}$ ways), and relabel $\alpha_0$ with $S$ and $\beta_0$ with $\overline{S}$ via the unique order-preserving bijection.

Summing over $k = 0, 1, \dots, n$ gives the **Binomial Convolution**:
$$c_n = \sum_{k=0}^{n} \binom{n}{k} a_k b_{n-k} = \sum_{k=0}^{n} \frac{n!}{k!(n-k)!} a_k b_{n-k}.$$
Dividing both sides by $n!$ immediately decouples the factorials:
$$\frac{c_n}{n!} = \sum_{k=0}^{n} \left(\frac{a_k}{k!}\right) \left(\frac{b_{n-k}}{(n-k)!}\right) \iff \widehat{C}(x) = \widehat{A}(x) \cdot \widehat{B}(x)!$$
This is why EGFs divide by $n!$: **Cauchy multiplication of EGFs automatically executes the $\binom{n}{k}$ label-distribution step!**

---

### 55.2 The Labelled Operator Dictionary: $\operatorname{SEQ}$, $\operatorname{SET} = \exp$, and $\operatorname{CYC} = \ln\frac{1}{1-\cdot}$

| Labelled Construction | Notation | Combinatorial Meaning | Count $c_n$ Formula | EGF Translation $\widehat{C}(x)$ | Validity Condition |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Disjoint Union** | $\mathcal{C} = \mathcal{A} + \mathcal{B}$ | Choose from $\mathcal{A}$ OR $\mathcal{B}$ | $a_n + b_n$ | $\widehat{A}(x) + \widehat{B}(x)$ | Always valid |
| **Labelled Product** | $\mathcal{C} = \mathcal{A} \star \mathcal{B}$ | Ordered pair $(\alpha, \beta)$ with relabelling | $\sum_{k=0}^n \binom{n}{k} a_k b_{n-k}$ | $\widehat{A}(x) \cdot \widehat{B}(x)$ | Always valid |
| **Length-$k$ Sequence** | $\mathcal{C} = \operatorname{SEQ}_k(\mathcal{A})$ | Ordered $k$-tuple $(\alpha_1, \dots, \alpha_k)$ | $\sum_{n_1+\dots+n_k=n} \binom{n}{n_1,\dots,n_k} \prod a_{n_i}$ | $\widehat{A}(x)^k$ | Always valid |
| **Sequence** | $\mathcal{C} = \operatorname{SEQ}(\mathcal{A})$ | Ordered tuple of any length $k \ge 0$ | $\sum_{k=0}^n [\operatorname{SEQ}_k(\mathcal{A})]_n$ | $\frac{1}{1 - \widehat{A}(x)}$ | $[x^0]\widehat{A}(x) = 0$ |
| **Size-$k$ Set** | $\mathcal{C} = \operatorname{SET}_k(\mathcal{A})$ | Unordered set $\{\alpha_1, \dots, \alpha_k\}$ of $k$ components | $\frac{1}{k!} [\operatorname{SEQ}_k(\mathcal{A})]_n$ | $\frac{\widehat{A}(x)^k}{k!}$ | $[x^0]\widehat{A}(x) = 0$ |
| **Set (Exp Formula)** | $\mathcal{C} = \operatorname{SET}(\mathcal{A})$ | Unordered set of any number $k \ge 0$ of components | $\sum_{k=0}^n \frac{1}{k!} [\operatorname{SEQ}_k(\mathcal{A})]_n$ | $\exp\!\big(\widehat{A}(x)\big)$ | $[x^0]\widehat{A}(x) = 0$ |
| **Directed Cycle** | $\mathcal{C} = \operatorname{CYC}(\mathcal{A})$ | Directed cycle of $k \ge 1$ components up to rotation | $\sum_{k=1}^n \frac{1}{k} [\operatorname{SEQ}_k(\mathcal{A})]_n$ | $\ln \frac{1}{1 - \widehat{A}(x)}$ | $[x^0]\widehat{A}(x) = 0$ |
| **Pointing** | $\mathcal{C} = \Theta \mathcal{A}$ | Distinguish 1 atom among the $n$ atoms of $\alpha$ | $n a_n$ | $x \widehat{A}'(x) = \vartheta \widehat{A}(x)$ | Always valid |
| **Boxed Product** | $\mathcal{C} = \mathcal{A}^{\square} \star \mathcal{B}$ | Pair $(\alpha, \beta)$ where min-label $1 \in \alpha$ | $\sum_{k=1}^n \binom{n-1}{k-1} a_k b_{n-k}$ | $\int_0^x \widehat{A}'(t)\widehat{B}(t)\,dt$ | $[x^0]\widehat{A}(x) = 0$ |

#### Deep-Dive: Why Labelled $\operatorname{SET}(\mathcal{A}) = \exp(\widehat{A}(x))$ and $\operatorname{CYC}(\mathcal{A}) = \ln\frac{1}{1-\widehat{A}(x)}$ Are Simpler Than Unlabelled $\operatorname{MSET}$ and $\operatorname{CYC}$!

In Iteration 54, unlabelled multisets required the Euler transform $\exp\sum_{j\ge 1} \frac{A(x^j)}{j}$ and unlabelled cycles required $\sum_{d\ge 1} \frac{\varphi(d)}{d}\ln\frac{1}{1-A(x^d)}$ because an unlabelled tuple $(\alpha_1, \dots, \alpha_k)$ can have repeated or periodic components.
Why do all the $j \ge 2$ and $d \ge 2$ terms **vanish** in the labelled world?
Because every non-empty component $\alpha_i$ ($|\alpha_i| \ge 1$) receives a **disjoint, non-empty subset of labels** $S_i \subseteq \{1, \dots, n\}$!
1. Since $S_1, S_2, \dots, S_k$ are pairwise disjoint and non-empty, **the $k$ relabelled components $\alpha_1, \dots, \alpha_k$ are always pairwise distinct**!
2. Therefore, permuting $(\alpha_1, \dots, \alpha_k)$ in all $k!$ ways always produces $k!$ **distinct** ordered tuples—so dividing by $k!$ is exact:
   $$|\operatorname{SET}_k(\mathcal{A})_n| = \frac{1}{k!} |\operatorname{SEQ}_k(\mathcal{A})_n| \implies \widehat{\operatorname{SET}}(\mathcal{A})(x) = \sum_{k=0}^{\infty} \frac{\widehat{A}(x)^k}{k!} = \exp\!\big(\widehat{A}(x)\big).$$
3. Similarly, rotating $(\alpha_1, \dots, \alpha_k)$ by $0, 1, \dots, k-1$ steps always produces $k$ **distinct** ordered tuples (where can label $1$ sit? In any of the $k$ positions!), so dividing by $k$ is exact:
   $$|\operatorname{CYC}_k(\mathcal{A})_n| = \frac{1}{k} |\operatorname{SEQ}_k(\mathcal{A})_n| \implies \widehat{\operatorname{CYC}}(\mathcal{A})(x) = \sum_{k=1}^{\infty} \frac{\widehat{A}(x)^k}{k} = \ln\frac{1}{1 - \widehat{A}(x)}.$$

---

### 55.3 Pointing $\Theta \mathcal{A}$ and the Boxed Product $\mathcal{A}^{\square} \star \mathcal{B}$ (Min-Label / Max-Label Tracking)

#### 1. The Pointing Operator $\Theta \mathcal{A}$ (Rooting a Structure)
Given a labelled class $\mathcal{A}$, the **pointed class** $\Theta \mathcal{A}$ consists of pairs $(\alpha, v)$ where $\alpha \in \mathcal{A}_n$ and $v \in \{1, 2, \dots, n\}$ is a distinguished atom ("root" or "marked vertex").
Since each $\alpha \in \mathcal{A}_n$ has $n$ choices for $v$, $(\Theta \mathcal{A})_n$ has $n a_n$ objects, and its EGF is:
$$\widehat{\Theta \mathcal{A}}(x) = \sum_{n=1}^{\infty} n a_n \frac{x^n}{n!} = x \sum_{n=1}^{\infty} a_n \frac{x^{n-1}}{(n-1)!} = x \widehat{A}'(x) = \vartheta \widehat{A}(x).$$
For example, if $\mathcal{U}$ is the class of **unrooted** labelled trees ($u_n = n^{n-2}$ by Cayley's formula), then pointing a vertex turns an unrooted tree into a **rooted** labelled tree $\mathcal{T} = \Theta \mathcal{U}$ ($t_n = n u_n = n^{n-1}$).
Every rooted labelled tree consists of its root atom $\mathcal{Z}$ attached to an unordered set of rooted labelled subtrees $\operatorname{SET}(\mathcal{T})$:
$$\mathcal{T} = \mathcal{Z} \star \operatorname{SET}(\mathcal{T}) \implies \widehat{T}(x) = x \exp\!\big(\widehat{T}(x)\big).$$

#### 2. The Boxed Product $\mathcal{A}^{\square} \star \mathcal{B}$ (Tracking the Component with Label $1$ or Label $n$)

##### Concrete Combinatorial Object
Let $\mathcal{A}$ and $\mathcal{B}$ be labelled classes with $a_0 = 0$ ($\mathcal{A}$ has no empty objects). The **boxed product** $\mathcal{C} = \mathcal{A}^{\square} \star \mathcal{B}$ (also written $\mathcal{A}^{\min} \star \mathcal{B}$ or $\mathcal{A}^{\max} \star \mathcal{B}$) is the subset of ordered pairs $(\alpha, \beta) \in \mathcal{A} \star \mathcal{B}$ subject to the constraint that **the smallest label $1$ (or equivalently the largest label $n$) must lie in the $\mathcal{A}$-component $\alpha$**.

##### Diagnostic Signal
Reach for the **Boxed Product** $\mathcal{A}^{\square} \star \mathcal{B}$ whenever:
1. You want to decompose a composite structure into **(the component containing vertex $1$)** and **(everything else)**—this breaks symmetry between components without needing $\exp$, allowing you to handle constraints where the component containing vertex $1$ is special!
2. You are counting permutations, increasing trees, Cartesian trees, or insertion processes by **splitting at the minimum or maximum element** (where the pivot label $1$ or $n$ is fixed in a specific slot).

##### Reverse-Engineering Scratchpad & Step-by-Step Algebraic Derivation
Suppose we build an object $\gamma = (\alpha, \beta) \in (\mathcal{A}^{\square} \star \mathcal{B})_n$ of total size $n \ge 1$, where $|\alpha| = k \ge 1$ and $|\beta| = n - k \ge 0$.
1. **Label distribution with label $1$ locked into $\alpha$**:
   Since label $1$ is already assigned to $\alpha$, we only need to choose the remaining $k - 1$ labels for $\alpha$ from the remaining $n - 1$ labels $\{2, 3, \dots, n\}$.
   How many ways? Exactly $\binom{n-1}{k-1}$ ways!
2. **Recurrence for $c_n$**:
   Summing over $k = 1, 2, \dots, n$ gives:
   $$c_n = \sum_{k=1}^{n} \binom{n-1}{k-1} a_k b_{n-k} = \sum_{k=1}^{n} \frac{(n-1)!}{(k-1)!(n-k)!} a_k b_{n-k} \qquad (n \ge 1, \; c_0 = 0).$$
3. **Convert to EGFs by dividing by $(n-1)!$**:
   Notice that the numerator on the right is $(n-1)!$, not $n!$! Divide both sides by $(n-1)!$:
   $$\frac{c_n}{(n-1)!} = \sum_{k=1}^{n} \left(\frac{a_k}{(k-1)!}\right) \left(\frac{b_{n-k}}{(n-k)!}\right).$$
4. **Recognize the derivative series**:
   Multiply by $x^{n-1}$ and sum over $n \ge 1$. Since $\widehat{C}'(x) = \sum_{n=1}^{\infty} c_n \frac{x^{n-1}}{(n-1)!}$ and $\widehat{A}'(x) = \sum_{k=1}^{\infty} a_k \frac{x^{k-1}}{(k-1)!}$, the right-hand side is the Cauchy product of $\widehat{A}'(x)$ and $\widehat{B}(x)$!
   $$\widehat{C}'(x) = \widehat{A}'(x) \cdot \widehat{B}(x) \iff \widehat{C}(x) = \int_0^x \widehat{A}'(t) \widehat{B}(t)\,dt.$$

> [!IMPORTANT]
> **One-Line Combinatorial Proof of the Exponential Formula via Boxed Product**:
> Let $\mathcal{F} = \operatorname{SET}(\mathcal{A})$ be the class of sets of components from $\mathcal{A}$ ($a_0 = 0$). Any non-empty set of components in $\mathcal{F}$ has a unique component that contains the minimum label $1$, and the remaining components form an arbitrary set in $\mathcal{F}$! Thus:
> $$\mathcal{F} = \mathcal{E} + \mathcal{A}^{\square} \star \mathcal{F} \implies \widehat{F}'(x) = 0 + \widehat{A}'(x) \widehat{F}(x) \implies \frac{\widehat{F}'(x)}{\widehat{F}(x)} = \widehat{A}'(x) \implies \widehat{F}(x) = \exp\!\big(\widehat{A}(x)\big).$$
> In Chinese competitive programming literature, this decomposition ($\mathcal{F} = \mathcal{E} + \mathcal{A}^{\square} \star \mathcal{F}$, or $f_n = \sum_{k=1}^n \binom{n-1}{k-1} a_k f_{n-k}$) is famously known as **`有标号定根技巧` ( the Labelled Root/Pivot-Fixing Trick)**!

---

### 55.4 Complete Structural Catalog of Classical Labelled EGFs

#### 1. Permutations, Derangements, Restricted Cycle Lengths, and Involutions
By decomposing a permutation $\pi \in S_n$ into its disjoint directed cycles, the class of all permutations $\mathcal{P}$ is a set of directed cycles of atoms:
$$\mathcal{P} = \operatorname{SET}\big(\operatorname{CYC}(\mathcal{Z})\big) \implies \widehat{P}(x) = \exp\!\left(\ln\frac{1}{1-x}\right) = \frac{1}{1-x} = \sum_{n=0}^{\infty} n! \frac{x^n}{n!}.$$
What if every cycle length is restricted to lie in a subset $S \subseteq \mathbb{Z}_{\ge 1}$?
Then a single valid cycle has EGF $\widehat{C}_S(x) = \sum_{k \in S} \frac{x^k}{k}$, so permutations whose cycle lengths all belong to $S$ have EGF:
$$\widehat{P}_S(x) = \exp\!\left(\sum_{k \in S} \frac{x^k}{k}\right).$$
- **Derangements ($\pi(i) \ne i$, so $S = \{2, 3, 4, \dots\}$)**:
  $$\widehat{D}(x) = \exp\!\left(\sum_{k=2}^{\infty} \frac{x^k}{k}\right) = \exp\!\left(\ln\frac{1}{1-x} - x\right) = \frac{e^{-x}}{1 - x} \implies d_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}.$$
- **Involutions ($\pi^2 = \mathrm{id}$, so $S = \{1, 2\}$; also counts Standard Young Tableaux of size $n$ by RSK)**:
  $$\widehat{I}(x) = \exp\!\left(x + \frac{x^2}{2}\right) \implies i_n = n! [x^n] \exp\!\left(x + \frac{x^2}{2}\right), \quad i_n = i_{n-1} + (n-1) i_{n-2}.$$
- **2-Regular Simple Graphs (Disjoint Unions of Undirected Cycles of Length $\ge 3$)**:
  An undirected cycle of length $k \ge 3$ has $(k-1)!/2$ orientations on $k$ vertices, so $\widehat{C}_{\ge 3}(x) = \sum_{k=3}^{\infty} \frac{x^k}{2k} = \frac{1}{2}\ln\frac{1}{1-x} - \frac{x}{2} - \frac{x^2}{4}$, and:
  $$\widehat{G}_{2\text{-reg}}(x) = \exp\!\left(\frac{1}{2}\ln\frac{1}{1-x} - \frac{x}{2} - \frac{x^2}{4}\right) = \frac{e^{-x/2 - x^2/4}}{\sqrt{1 - x}}.$$

#### 2. Set Partitions (Bell Numbers) and Stirling Numbers of Both Kinds
- **Non-Empty Labelled Set $\operatorname{SET}_{\ge 1}(\mathcal{Z})$**: For each $n \ge 1$, there is $1$ way to form a single set $\{1, \dots, n\}$, so its EGF is $e^x - 1$.
- **Set Partitions into Exactly $k$ Non-Empty Blocks (Stirling Numbers of the Second Kind $\left\{ \begin{matrix} n \\ k \end{matrix} \right\}$)**:
  $$\mathcal{S}_k = \operatorname{SET}_k\big(\operatorname{SET}_{\ge 1}(\mathcal{Z})\big) \implies \sum_{n=k}^{\infty} \left\{ \begin{matrix} n \\ k \end{matrix} \right\} \frac{x^n}{n!} = \frac{(e^x - 1)^k}{k!}.$$
- **All Set Partitions (Bell Numbers $B_n = \sum_{k=0}^n \left\{ \begin{matrix} n \\ k \end{matrix} \right\}$)**:
  $$\mathcal{B} = \operatorname{SET}\big(\operatorname{SET}_{\ge 1}(\mathcal{Z})\big) \implies \widehat{B}(x) = \sum_{n=0}^{\infty} B_n \frac{x^n}{n!} = \exp(e^x - 1).$$
- **Permutations with Exactly $k$ Disjoint Cycles (Unsigned Stirling Numbers of the First Kind $\left[ \begin{matrix} n \\ k \end{matrix} \right]$)**:
  $$\mathcal{C}_k = \operatorname{SET}_k\big(\operatorname{CYC}(\mathcal{Z})\big) \implies \sum_{n=k}^{\infty} \left[ \begin{matrix} n \\ k \end{matrix} \right] \frac{x^n}{n!} = \frac{1}{k!} \left(\ln \frac{1}{1 - x}\right)^k.$$

#### 3. Connected Labelled Graphs, Eulerian Graphs, and Bipartite Graphs via $\ln$, $\exp$, and $\sqrt{\cdot}$
- **Connected Simple Undirected Graphs**:
  On $n$ labelled vertices, there are $\binom{n}{2}$ potential edges, so there are $g_n = 2^{\binom{n}{2}}$ simple graphs in total. Since every simple graph is uniquely a $\operatorname{SET}$ of its connected components:
  $$\widehat{G}(x) = \sum_{n=0}^{\infty} 2^{\binom{n}{2}} \frac{x^n}{n!} = \exp\!\big(\widehat{C}(x)\big) \implies \widehat{C}(x) = \ln \widehat{G}(x).$$
  Thus $c_n = n! [x^n] \ln \widehat{G}(x)$ counts connected labelled graphs on $n$ vertices in $O(N \log N)$ time!
- **Connected Eulerian Graphs (All Degrees Even)**:
  How many graphs on $n$ labelled vertices have **every vertex degree even**?
  Isolate vertex $n$: we can choose all edges among $\{1, \dots, n-1\}$ freely in $2^{\binom{n-1}{2}}$ ways, and then for each $v \in \{1, \dots, n-1\}$, the edge $\{v, n\}$ is uniquely forced by the parity of $v$'s current degree (which automatically leaves vertex $n$ with even degree since the sum of degrees is even!). Thus $e_n = 2^{\binom{n-1}{2}}$, and taking $\ln \sum_{n\ge 0} 2^{\binom{n-1}{2}} \frac{x^n}{n!}$ (with $e_0 = 1$) gives **connected Eulerian graphs**!
- **Labelled Bipartite Graphs and Connected Bipartite Graphs**:
  How do we count labelled bipartite graphs when a bipartite graph does not come with a unique 2-coloring?
  **Reverse-Engineering Scratchpad**:
  1. First, count **properly 2-colored** (black/white) labelled graphs $b_n^{(2)}$: choose $k$ black vertices and $n-k$ white vertices in $\binom{n}{k}$ ways, and choose a subset of the $k(n-k)$ cross-edges in $2^{k(n-k)}$ ways:
     $$b_n^{(2)} = \sum_{k=0}^{n} \binom{n}{k} 2^{k(n-k)}.$$
  2. How do we compute $b_0^{(2)}, \dots, b_N^{(2)}$ in $O(N \log N)$? Rewrite the cross-product $k(n-k)$ using the **Chirp-Z / Square-Completion Identity** $k(n-k) = \binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}$:
     $$\frac{b_n^{(2)}}{n! 2^{\binom{n}{2}}} = \sum_{k=0}^{n} \left(\frac{2^{-\binom{k}{2}}}{k!}\right) \left(\frac{2^{-\binom{n-k}{2}}}{(n-k)!}\right),$$
     which is a single NTT convolution!
  3. Let $\widehat{B}_2(x) = \sum_{n=0}^{\infty} b_n^{(2)} \frac{x^n}{n!}$. Then $\ln \widehat{B}_2(x)$ is the EGF of **connected 2-colored graphs**.
  4. Now, every connected bipartite graph has **exactly 2** proper 2-colorings (swap black and white!). Therefore, the EGF of **connected uncolored bipartite graphs** is:
     $$\widehat{C}_{\text{bip}}(x) = \frac{1}{2} \ln \widehat{B}_2(x).$$
  5. Finally, an arbitrary labelled bipartite graph is a $\operatorname{SET}$ of connected uncolored bipartite graphs:
     $$\widehat{G}_{\text{bip}}(x) = \exp\!\big(\widehat{C}_{\text{bip}}(x)\big) = \exp\!\left(\frac{1}{2} \ln \widehat{B}_2(x)\right) = \sqrt{\widehat{B}_2(x)}!$$

#### 4. Alternating (Up-Down / André) Permutations via the Boxed Product
An **alternating (up-down) permutation** of $\{1, \dots, n\}$ satisfies $\pi_1 < \pi_2 > \pi_3 < \pi_4 > \dots$.
How do we derive its EGF $\widehat{E}(x) = \sum_{n=0}^{\infty} E_n \frac{x^n}{n!}$?
Split $\pi$ at the position of the **largest label $n$** (using the Boxed Product!):
- Because $\pi_{i-1} < \pi_i > \pi_{i+1}$ at every peak, for $n \ge 2$ the largest element $n$ **must sit at an even index** $2k$ ($1 \le 2k \le n$), except when $n = 1$.
- More symmetrically, in the class of all alternating permutations (or by splitting into odd-length $E_{\text{odd}}(x)$ and even-length $E_{\text{even}}(x)$), removing the maximum element splits a size-$n$ alternating permutation into two independent alternating permutations, yielding André's differential equation:
  $$2 \widehat{E}'(x) = 1 + \widehat{E}(x)^2, \quad \widehat{E}(0) = 1 \implies \widehat{E}(x) = \sec x + \tan x.$$

#### Hand-Checkable Toy Trace ($n \le 4$): Connected Labelled Graphs via $\widehat{C}(x) = \ln \widehat{G}(x)$
We have $g_0 = 1, g_1 = 1, g_2 = 2, g_3 = 8, g_4 = 64$, so:
$$\widehat{G}(x) = 1 + x + \frac{2}{2!}x^2 + \frac{8}{3!}x^3 + \frac{64}{4!}x^4 + O(x^5) = 1 + x + x^2 + \frac{4}{3}x^3 + \frac{8}{3}x^4 + O(x^5).$$
Using $n c_n = n g_n - \sum_{k=1}^{n-1} \binom{n}{k} k c_k g_{n-k}$ (i.e., $c_n = g_n - \sum_{k=1}^{n-1} \binom{n-1}{k-1} c_k g_{n-k}$, the Boxed Product recurrence!):
- $n = 1$: $c_1 = g_1 = 1$.
- $n = 2$: $c_2 = g_2 - \binom{1}{0} c_1 g_1 = 2 - 1 = 1$. (1 connected graph on 2 vertices: $K_2$).
- $n = 3$: $c_3 = g_3 - \binom{2}{0} c_1 g_2 - \binom{2}{1} c_2 g_1 = 8 - 1\cdot 1\cdot 2 - 2\cdot 1\cdot 1 = 4$. (3 trees $P_3$ + 1 triangle $K_3 = 4$).
- $n = 4$: $c_4 = g_4 - \binom{3}{0} c_1 g_3 - \binom{3}{1} c_2 g_2 - \binom{3}{2} c_3 g_1 = 64 - 1(1)(8) - 3(1)(2) - 3(4)(1) = 64 - 8 - 6 - 12 = 38$. (16 trees + 15 graphs with 4 edges + 6 graphs with 5 edges + 1 $K_4 = 38$). Exact match!

---

## Iteration 56: `[ZH]` Combinatorial Modelling Deep-Dive (Chinese OI / ICPC School)

The Chinese competitive programming community (`国家集训队论文`, OI-Wiki, Luogu `洛谷日报`, UOJ/LOJ/QOJ) developed a remarkably systematic pedagogy for connecting polynomial algorithms (`inv`, `ln`, `exp`, `sqrt`, ODEs) to combinatorial enumeration. This iteration synthesizes the core literature and extracts the four signature modelling paradigms of the `[ZH]` school.

### 56.1 Foundational `[ZH]` Literature Survey

1. **`[ZH]` Jin Ce (金策, Tsinghua University), *《生成函数的运算与组合计数问题》* (*Operations on Generating Functions and Combinatorial Counting Problems*), 2015 Chinese National Team Paper (`国家集训队2015论文集`)**:
   - **Historical & Technical Significance**: The watershed paper that brought Flajolet–Sedgewick's Symbolic Method and Newton's method on formal power series into mainstream Chinese OI. Jin Ce systematically showed that polynomial `inv`, `sqrt`, `ln`, and `exp` are not merely algebraic curiosities, but direct translations of combinatorial $\operatorname{SEQ}$, binary tree quadratic equations (CF 438E), connected-to-general $\operatorname{SET}$ inversion (POJ 1737 / BZOJ 3456), and differential equations for labelled trees (UOJ #50).
2. **`[ZH]` Lu Xin (吕欣 / Elegia, Peking University), *《生成函数在组合计数中的应用》* & Luogu/UOJ Lectures on Operator Calculus and Euler Transform (2018–2021)**:
   - **Technical Significance**: Unified OGFs and EGFs through formal differential operators ($\vartheta = x\frac{d}{dx}$), logarithmic derivatives, and the algebraic equivalence between the Euler transform $\prod(1-x^k)^{-a_k}$ and the harmonic-sieved exponential $\exp\sum_{j\ge 1} \frac{A(x^j)}{j}$.
3. **`[ZH]` Yang Maolong (杨懋龙), *《浅谈生成函数在掷骰子问题上的应用》* (*Applications of Generating Functions in Dice-Rolling Problems*), 2018 Chinese National Team Paper (`国家集训队2018论文集`)**:
   - **Technical Significance**: Established the standard `[ZH]` framework for **Probability Generating Functions (PGFs)** $F(x) = \sum_{n\ge 0} \Pr[X = n] x^n$. By replacing ad-hoc expectation recurrences with the formal derivative at $x = 1$:
     $$\mathbb{E}[X] = F'(1) = (\vartheta F)(1), \qquad \operatorname{Var}(X) = F''(1) + F'(1) - \big(F'(1)\big)^2,$$
     stopping-time problems (such as first occurrence of a string pattern in dice/coin rolls, CTSC 2006 `歌唱王国`) reduce to differentiating rational OGF equations $(1 - x)F(x) + \dots = 1$ at $x = 1$.
4. **`[ZH]` OI-Wiki (`docs/math/poly/ogf.md`, `egf.md`, `elementary-func.md`, `partition.md`) & Classic Luogu Blogs (`command_block` *《多项式计数杂谈》*, `rqy` *《多项式 exp 的组合意义》*)**:
   - **Technical Significance**: Standardized the terminology `多项式 exp/ln 的组合意义` (Combinatorial Meaning of Polynomial $\exp/\ln$), `付公主的背包` (Harmonic-Sieve Euler Transform Knapsack), and `有标号定根技巧` (Labelled Root-Fixing / Boxed Product).

---

### 56.2 Paradigm ZH-1: `多项式 exp/ln 的组合意义` (Combinatorial Meaning of Polynomial $\exp$ and $\ln$)

In Chinese editorials, whenever a problem asks to count structures on $n$ labelled vertices with multiplicative weight over connected components, solvers immediately invoke **`多项式 exp 的组合意义`**:

#### The General Weighted Block-Decomposition Principle
Suppose a composite labelled structure $\gamma$ on $\{1, \dots, n\}$ is an unordered set of $k \ge 0$ disjoint connected components $\{\alpha_1, \dots, \alpha_k\}$, and the weight (or number of ways to configure) $\gamma$ factors as the product of weights of its components:
$$W(\gamma) = \prod_{i=1}^{k} w(\alpha_i).$$
If $c_m = \sum_{|\alpha|=m} w(\alpha)$ is the total weight of single connected components on $m$ labelled vertices ($c_0 = 0$), and $f_n = \sum_{|\gamma|=n} W(\gamma)$ is the total weight of composite structures on $n$ labelled vertices ($f_0 = 1$), then:
$$\widehat{F}(x) = \sum_{n=0}^{\infty} f_n \frac{x^n}{n!} = \exp\!\left(\sum_{m=1}^{\infty} c_m \frac{x^m}{m!}\right) = \exp\!\big(\widehat{C}(x)\big), \qquad \widehat{C}(x) = \ln \widehat{F}(x).$$

#### Three High-Frequency Twists in `[ZH]` Contests
1. **Twist 1 — Counting Connected Structures by Inverting Easy Total Counts ($\widehat{C} = \ln \widehat{F}$)**:
   Counting connected graphs, connected Eulerian graphs, or connected bipartite graphs directly by DP is hard because connectivity is a global property. Counting **all** (possibly disconnected) graphs $\widehat{F}(x)$ is easy ($2^{\binom{n}{2}}$). Taking $\ln \widehat{F}(x)$ strips away disconnected configurations automatically in $O(N \log N)$!
2. **Twist 2 — Counting $k$-Component Structures or Cycle-of-Components**:
   Once $\widehat{C}(x) = \ln \widehat{F}(x)$ is extracted, we are NOT limited to single connected components!
   - Exactly $k$ connected components: $\frac{\widehat{C}(x)^k}{k!}$.
   - A directed cycle of connected components: $\ln\frac{1}{1 - \widehat{C}(x)}$.
   - Connected components with size restricted to $S \subseteq \mathbb{Z}_{\ge 1}$: zero out $[x^m]\widehat{C}(x)$ for $m \notin S$, then re-exponentiate $\exp(\widehat{C}_{\in S}(x))$!
3. **Twist 3 — Iterated $\exp$ for Rooted Trees, Cactus Graphs, and Block-Cut Trees**:
   In a rooted labelled tree where each vertex $u$ with $d$ children carries a local weight $w_d$ (for example, $w_d = \binom{d+1}{2}$ or $w_d = 1$ for $d \in D$), the EGF of rooted trees satisfies:
   $$\widehat{T}(x) = x \sum_{d=0}^{\infty} w_d \frac{\widehat{T}(x)^d}{d!}.$$
   When $w_d = 1$ for all $d \ge 0$, this is $\widehat{T}(x) = x \exp(\widehat{T}(x))$. In rooted cactus graphs (where edges and simple cycles share vertices), a vertex is attached to a $\operatorname{SET}$ of edges (each leading to a rooted cactus $\widehat{T}$) and simple cycles of length $\ge 3$ (each carrying a sequence of $\ge 2$ other rooted cacti $\frac{1}{2}\widehat{T}^k$ for $k \ge 2$):
   $$\widehat{T}(x) = x \exp\!\left(\widehat{T}(x) + \sum_{k=2}^{\infty} \frac{\widehat{T}(x)^k}{2}\right) = x \exp\!\left(\frac{2\widehat{T}(x) - \widehat{T}(x)^2}{2(1 - \widehat{T}(x))}\right).$$

---

### 56.3 Paradigm ZH-2: `付公主的背包` (The Harmonic-Sieve Euler Transform Knapsack Trick)

Named after the iconic Luogu problem **P4389 `付公主的背包` (Fu Princess's Knapsack)**, this paradigm solves unbounded or 0-1 knapsack counting problems when the number of items $M$ and maximum capacity $N$ are both up to $10^5$—where standard $O(NM)$ knapsack DP TLEs!

#### Diagnostic Signal
You are asked to compute $[x^s] \prod_{i=1}^{M} \frac{1}{1 - x^{v_i}}$ (unbounded knapsack), $[x^s] \prod_{i=1}^{M} (1 + x^{v_i})$ (0-1 subset sum ways), or $[x^s] \prod_{i=1}^{M} \frac{1 - x^{(b_i + 1)v_i}}{1 - x^{v_i}}$ (bounded knapsack, since the numerator splits into $\prod (1 - x^{w_i})$) for all $s = 0, 1, \dots, N$, with $M, N \le 10^5$ and $v_i \ge 1$.

#### Reverse-Engineering Scratchpad
1. **Why naive divide-and-conquer NTT is suboptimal here**:
   Multiplying $M$ polynomials of degree $v_i$ via a binary tree works when $\sum_{i=1}^M v_i \le N$, but here each $v_i$ can be up to $N$, so $\sum v_i$ can be $MN = 10^{10}$! Even if we truncate at $x^{N+1}$, divide-and-conquer NTT still struggles.
2. **Group items by weight $k$**:
   Instead of iterating over the $M$ items, count how many items have weight $k$:
   $$a_k := \big|\{i \in \{1, \dots, M\} : v_i = k\}\big| \qquad (1 \le k \le N).$$
   Then the generating function is the exact **Euler Transform** of $(a_1, \dots, a_N)$:
   $$F(x) = \prod_{k=1}^{N} \left(\frac{1}{1 - x^k}\right)^{a_k}.$$
3. **Apply $\ln$, sieve harmonically in $O(N \log N)$, and apply $\exp$ once**:
   $$\ln F(x) = \sum_{k=1}^{N} a_k \ln\frac{1}{1 - x^k} = \sum_{k=1}^{N} a_k \sum_{j=1}^{\lfloor N/k \rfloor} \frac{x^{jk}}{j} \pmod{x^{N+1}}.$$
   Because $\sum_{k=1}^N \lfloor N/k \rfloor = O(N \log N)$, we accumulate all coefficients of $\ln F(x) \bmod x^{N+1}$ in a simple $O(N \log N)$ harmonic loop, and then invoke polynomial `exp` **once**!

---

### 56.4 Paradigm ZH-3: `有标号定根技巧` (Labelled Pivot-Label / Root-Fixing Trick & ODEs)

#### Diagnostic Signal
You are counting a recursive labelled structure on $n$ vertices (such as UOJ #50 `链式反应`, increasing trees, or connected graphs with root-dependent transitions), and you write a recurrence by **isolating vertex $1$ (the vertex with the smallest label)**:
$$f_n = \sum_{k} \binom{n-1}{k-1} (\dots).$$
Whenever $\binom{n-1}{k-1}$ appears in a labelled recurrence instead of $\binom{n}{k}$, it is the **Boxed Product** $\mathcal{A}^{\square} \star \mathcal{B}$ in disguise!

#### Reverse-Engineering Scratchpad (From $\binom{n-1}{k-1}$ to $\widehat{F}'(x)$)
Suppose a labelled problem has the recurrence (as in UOJ #50 `链式反应`):
$$f_n = \frac{1}{2} \sum_{\substack{i + j + k = n - 1 \\ i, j \ge 1, k \ge 0}} a_k \binom{n-1}{i, j, k} f_i f_j \quad (n \ge 2), \quad f_1 = 1, f_0 = 0.$$
Here, vertex $1$ is the root of a cascading reaction: it triggers two sub-trees of sizes $i$ and $j$ ($f_i$ and $f_j$, divided by $2$ because the two sub-trees are unordered) plus $k$ specification vertices from a given set ($a_k$), partitioning the remaining $n-1$ labels into $(i, j, k)$ via the multinomial coefficient $\binom{n-1}{i, j, k} = \frac{(n-1)!}{i! j! k!}$.
How do we convert this to an EGF equation?
1. Divide both sides by $(n-1)!$:
   $$\frac{f_n}{(n-1)!} = \frac{1}{2} \sum_{i + j + k = n - 1} \left(\frac{a_k}{k!}\right) \left(\frac{f_i}{i!}\right) \left(\frac{f_j}{j!}\right) \qquad (n \ge 2).$$
2. Multiply by $x^{n-1}$ and sum over $n \ge 1$ (adding $+1$ for the base case $n = 1$, where $\frac{f_1}{0!} x^0 = 1$):
   $$\widehat{F}'(x) = \sum_{n=1}^{\infty} f_n \frac{x^{n-1}}{(n-1)!} = \frac{1}{2} \widehat{A}(x) \big(\widehat{F}(x)\big)^2 + 1!$$
3. We have reduced a 3-way multinomial DP to a **first-order non-linear ODE** $\widehat{F}'(x) = \frac{1}{2}\widehat{A}(x)\widehat{F}(x)^2 + 1$, solvable in $O(N \log N)$ via Newton's method on FPS or $O(N \log^2 N)$ via CDQ divide-and-conquer FFT!

---

### 56.5 Paradigm ZH-4: Differential Operators & EGFs for Sequential Modifications (CF 891E *Lust*)

Highlighted in OI-Wiki `math/poly/egf.md`, **Codeforces 891E (Lust)** illustrates how EGFs and formal operators solve sequential random modification problems on products.
Suppose we start with an array $a_1, \dots, a_n$ and perform $k$ operations; in each operation we uniformly pick an index $i \in \{1, \dots, n\}$ and decrement $a_i \leftarrow a_i - 1$. We want the expected value of the final product $\prod_{i=1}^n (a_i - c_i)$, where $c_i \ge 0$ is the number of times index $i$ was chosen ($\sum_{i=1}^n c_i = k$).
- The number of operation sequences producing tuple $(c_1, \dots, c_n)$ is the multinomial coefficient $\frac{k!}{c_1! \cdots c_n!}$.
- Thus we need to compute:
  $$S = \sum_{c_1 + \dots + c_n = k} \frac{k!}{c_1! \cdots c_n!} \prod_{i=1}^{n} (a_i - c_i) = k! [x^k] \prod_{i=1}^{n} \left(\sum_{c=0}^{\infty} (a_i - c) \frac{x^c}{c!}\right).$$
- Look at the inner EGF for a single element $a_i$:
  $$\sum_{c=0}^{\infty} (a_i - c) \frac{x^c}{c!} = a_i \sum_{c=0}^{\infty} \frac{x^c}{c!} - x \sum_{c=1}^{\infty} \frac{x^{c-1}}{(c-1)!} = (a_i - x) e^x!$$
- Multiplying across $i = 1, \dots, n$ factors out $e^{nx}$ completely:
  $$\prod_{i=1}^{n} (a_i - x) e^x = e^{nx} \prod_{i=1}^{n} (a_i - x)!$$
  Since $P(x) = \prod_{i=1}^n (a_i - x)$ is a degree-$n$ polynomial computable in $O(n^2)$, extracting $k! [x^k] e^{nx} P(x) = \sum_{j=0}^{\min(n,k)} k^{\underline{j}} n^{k-j} [x^j]P(x)$ solves the problem in $O(n^2)$ even for $k = 10^9$!

---

## Iteration 57 (Part 1): `[JA]` Combinatorial Modelling Deep-Dive (Japanese FPS School)

In the Japanese competitive programming ecosystem (`maspypy.com`, `noshi91.hatenablog.com`, `Nyaan`'s `nyaannyaan.github.io/library`, `tatyam`, `opt-cp.com`, AtCoder ABC/ARC/AGC, and the **FPS 24** educational problem set), Formal Power Series is treated as a **first-class modelling language** that replaces dynamic programming rather than merely accelerating it.

### 57.1 Foundational `[JA]` Literature & Philosophy (`DP を立てずに母関数を直接書く`)

1. **`[JA]` maspy (`maspypy.com`), *形式的べき級数解説 (Formal Power Series Commentary)* & *分割数の母関数と五角数定理 (Generating Functions of Partition Numbers and Pentagonal Number Theorem)* (2019–2023)**:
   - **Core Philosophy**: `maspy` emphasizes **"Write the generating function directly without setting up a DP table"** (`DP を立てずに母関数を直接書く`). When a beginner sets up a DP $dp[i][j]$, they artificially impose a sequential order on the choices. By writing the choice for each independent element or slot as a polynomial factor $f_i(x)$ and taking the product $\prod f_i(x)$ (or composition $F(G(x))$), algebraic symmetries become visible immediately.
2. **`[JA]` Nyaan (`nyaannyaan.github.io/library`), *Formal Power Series & Famous Series Library* (`fps/formal-power-series.hpp`, `fps/fps-famous-series.hpp`, `fps/differential-equation.hpp`)**:
   - **Technical Significance**: Codifies a production-grade C++20 FPS DSL where `inv`, `exp`, `log`, `pow`, `sqrt`, `TaylorShift`, `Stirling1st`, `Stirling2nd`, `Bell`, `Bernoulli`, and `Partition` are composable primitives, verified against Library Checker (`judge.yosupo.jp`).
3. **`[JA]` noshi91 (`noshi91.hatenablog.com`), tatyam, and `opt-cp.com` (*競技プログラミングにおける形式的べき級数*)**:
   - **Technical Significance**: Pioneered relaxed/online convolution, fast subset-sum/multiset-sum reductions via $\exp(\ln)$, and inclusion-exclusion over FPS for AtCoder ABC/ARC/AGC problems.

---

### 57.2 Four Signature `[JA]` FPS Modelling Idioms

#### Idiom JA-1: Independent Choice Product $\to$ Log-Sum-Exp Bucketing
In AtCoder problems, whenever $M$ independent choices have polynomial generating functions $(1 + c_i x^{a_i})$ or $(1 - c_i x^{a_i})^{-1}$ or $(1 + x^{a_i} + x^{2a_i} + \dots + x^{b_i a_i})$ with $\max a_i \le N$:
1. First, convert any finite geometric series $1 + x^a + \dots + x^{b a} = \frac{1 - x^{(b+1)a}}{1 - x^a}$ into the ratio of a numerator factor $(1 - x^{(b+1)a})$ and a denominator factor $(1 - x^a)$.
2. Second, bucket factors of identical degree and coefficient $(a, c)$ and use the harmonic expansion $\ln(1 - c x^a) = -\sum_{j=1}^{\lfloor N/a \rfloor} \frac{c^j}{j} x^{ja}$ to sum all logs in $O(N \log N)$ before a single `.exp()`.

#### Idiom JA-2: Inclusion-Exclusion (PIE) Directly Inside $\operatorname{SEQ}$ or $\operatorname{SET}$
Suppose we want to count sequences or circular arrangements of objects where **adjacent identical/forbidden transitions are disallowed** (e.g., AtCoder ABC 236 Ex *Distinct Multiples*, or counting arrangements with no two adjacent elements from the same group).
In the `[JA]` paradigm:
- Instead of inclusion-exclusion over all $2^{n-1}$ subsets of Violated Adjacencies globally, we group maximal contiguous chains of violated adjacencies into **connected blocks (clusters)**.
- A cluster of $k \ge 1$ elements forced to be equal (or connected by forbidden edges) carries an inclusion-exclusion weight $(-1)^{k-1}$ (for linear chains) or $\sum_{\text{connected graphs on } k} (-1)^{|E|} = (-1)^{k-1}(k-1)!$ (for pairwise distinctness on complete graphs $K_k$!).
- Why does $\sum_{G \text{ connected on } k \text{ vertices}} (-1)^{|E|} = (-1)^{k-1}(k-1)!$ hold?
  **Proof via FPS $\ln$!**:
  Consider the EGF of **all** graphs on $k$ vertices weighted by $(-1)^{|E|}$. For $k = 1$, there is $1$ graph with $0$ edges ($(-1)^0 = 1$). For $k \ge 2$, there are $\binom{k}{2} \ge 1$ potential edges, so $\sum_{E} (-1)^{|E|} = (1 - 1)^{\binom{k}{2}} = 0$!
  Thus the total weighted EGF is simply $\widehat{F}(x) = 1 + x$!
  By the Exponential Formula, the EGF of **connected** graphs weighted by $(-1)^{|E|}$ is:
  $$\widehat{C}(x) = \ln \widehat{F}(x) = \ln(1 + x) = \sum_{k=1}^{\infty} (-1)^{k-1} (k-1)! \frac{x^k}{k!}!$$
  Therefore, the sum of $(-1)^{|E|}$ over all connected graphs on $k$ labelled vertices is **always $(-1)^{k-1}(k-1)!$**! This single FPS identity (famously used in **AtCoder ABC 236 Ex**) collapses chromatic-polynomial / distinct-tuple inclusion-exclusion into an EGF $\exp$ or DP immediately!

#### Idiom JA-3: Unified FPS View of the Twelvefold Way (Stirling, Bell, Partition)
As implemented in `Nyaan/library/fps/fps-famous-series.hpp`:
- **Fixed $K$, Varying $N$ ($n = 0 \dots N$)**:
  - Unsigned Stirling 1st kind $\left[\begin{matrix} n \\ K \end{matrix}\right]$: $n! [x^n] \frac{1}{K!}\left(\ln\frac{1}{1-x}\right)^K$.
  - Stirling 2nd kind $\left\{\begin{matrix} n \\ K \end{matrix}\right\}$: $n! [x^n] \frac{1}{K!}(e^x - 1)^K$.
- **Fixed $N$, Varying $K$ ($k = 0 \dots N$)**:
  - Unsigned Stirling 1st kind $\left[\begin{matrix} N \\ k \end{matrix}\right]$: $[x^k] x^{\overline{N}} = [x^k] x(x+1)\cdots(x+N-1)$, computed in $O(N \log N)$ via doubling + `TaylorShift` ($P(x) \mapsto P(x) P(x + m)$).
  - Stirling 2nd kind $\left\{\begin{matrix} N \\ k \end{matrix}\right\}$: By binomial inversion, $\left\{\begin{matrix} N \\ k \end{matrix}\right\} = \frac{1}{k!} \sum_{j=0}^{k} (-1)^{k-j} \binom{k}{j} j^N = \sum_{j=0}^{k} \frac{(-1)^{k-j}}{(k-j)!} \cdot \frac{j^N}{j!}$, which is a **single convolution** of $\frac{(-1)^i}{i!}$ and $\frac{j^N}{j!}$!

#### Idiom JA-4: Bipartite / 2-Colored Graph Square-Root Trick (`ARC 105 F` / `AGC` style)
When counting connected graphs on $N$ labelled vertices equipped with a bipartite 2-coloring (or vertex-subset assignment with cross-edge weights $2^{k(n-k)}$):
1. Use $k(n-k) = \binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}$ to express the 2-colored graph EGF $\widehat{B}_2(x)$ as the square of an EGF $\widehat{H}(x) = \sum_{k\ge 0} 2^{-\binom{k}{2}} \frac{x^k}{k!}$ (after scaling $[x^n]$ by $2^{\binom{n}{2}}$).
2. Take $\ln \widehat{B}_2(x)$ to isolate connected 2-colored components, divide by $2$ if the two color classes are interchangeable, and apply $\exp$ to reassemble!

---

## Iteration 57 (Part 2): Rigorous Wave 1A Competitive Programming Problem Audit

In accordance with the Wave 1A audit mandate, all bare polynomial implementation templates (e.g., Library Checker `inv_of_formal_power_series`, Luogu P4725 `【模板】多项式对数函数`) are strictly excluded from the accepted curriculum and logged in the **Rejected Template Problems Table** (Section 57.5). Below we present **20 carefully curated, non-template contest problems** spanning four difficulty tiers (`Stepping Stone`, `Intermediate`, `Advanced`, `Mastery`) across Codeforces, AtCoder, Luogu, UOJ, LOJ, POJ, 51nod, and yukicoder.

---

### 57.3 Tier 1 & Tier 2 Accepted Problems (`Stepping Stone` & `Intermediate`)

#### Problem 1: Luogu P4389 — 付公主的背包 (Fu Princess's Knapsack)
- **Judge & URL**: Luogu P4389 (`https://www.luogu.com.cn/problem/P4389`)
- **Difficulty Tier**: `Stepping Stone` (Unlabelled $\operatorname{MSET}$ / Forward Euler Transform via Harmonic Sieve + $\exp$)
- **Mathematical Statement & Constraints**:
  You are given $n$ types of items; the $i$-th item has volume $v_i$ ($1 \le v_i \le m$) and is available in infinite supply. For every capacity $s = 1, 2, \dots, m$, compute the number of ways to fill a knapsack of exact volume $s$ (order of items does not matter) modulo $998244353$.
  - **Constraints**: $1 \le n, m \le 10^5$, $1 \le v_i \le m$.
  - **Target Complexity**: $O((n + m) \log m)$ time, $O(m)$ space.
- **Diagnostic Signal & Modelling Bridge**:
  Each item $i$ contributes an unlabelled sequence of copies $1 + x^{v_i} + x^{2v_i} + \dots = (1 - x^{v_i})^{-1}$. Because both $n$ and $m$ are $10^5$, an $O(nm)$ knapsack DP times out. Grouping items by identical volume $k$ turns the product into the Euler transform $\prod_{k=1}^m (1 - x^k)^{-a_k}$.
- **Complete Derivation & Solution Sketch**:
  1. Let $a_k = |\{i \in \{1, \dots, n\} : v_i = k\}|$ be the multiplicity of items of volume $k$. The desired OGF is:
     $$F(x) = \prod_{k=1}^{m} (1 - x^k)^{-a_k} \pmod{x^{m+1}}.$$
  2. Taking the formal logarithm gives:
     $$G(x) := \ln F(x) = \sum_{k=1}^{m} -a_k \ln(1 - x^k) = \sum_{k=1}^{m} a_k \sum_{j=1}^{\lfloor m/k \rfloor} \frac{x^{jk}}{j} \pmod{x^{m+1}}.$$
  3. Populate the coefficients of $G(x)$ in $O(m \log m)$ time using the harmonic loop over $(k, j)$, then compute $F(x) = \exp(G(x)) \bmod x^{m+1}$ in $O(m \log m)$ time.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Write the answer as the coefficient $[x^s]$ of a product of $n$ geometric series. Why can you group items that have the exact same volume $v_i = k$?
  - *Hint 2*: How do you turn a product $\prod_{k=1}^m (1 - x^k)^{-a_k}$ into a sum? Consider taking the formal logarithm $\ln F(x)$ and expanding $-\ln(1 - x^k)$.
  - *Hint 3*: Accumulate $[x^{jk}] \ln F(x) \mathrel{+}= a_k / j$ for all $1 \le k \le m$ and $1 \le j \le \lfloor m/k \rfloor$ in $O(m \log m)$ total steps, then apply polynomial $\exp$ mod $x^{m+1}$.

---

#### Problem 2: Luogu P4841 — [集训队作业2013] 城市规划 (Urban Planning)
- **Judge & URL**: Luogu P4841 (`https://www.luogu.com.cn/problem/P4841`) — also classic BZOJ 3456 / POJ 1737 (for small $n$)
- **Difficulty Tier**: `Stepping Stone` (Labelled $\operatorname{SET}$ Inversion via EGF $\ln$)
- **Mathematical Statement & Constraints**:
  Find the number of **connected** simple undirected graphs on $n$ labelled vertices $\{1, 2, \dots, n\}$ modulo $1004535809$ ($= 479 \times 2^{21} + 1$, a prime with primitive root $3$).
  - **Constraints**: $1 \le n \le 1.3 \times 10^5$.
  - **Target Complexity**: $O(n \log n)$ time, $O(n)$ space.
- **Diagnostic Signal & Modelling Bridge**:
  The vertices are labelled $\{1, \dots, n\}$, and any simple graph is uniquely a disjoint union ($\operatorname{SET}$) of its connected components. Counting all simple graphs is trivial ($g_n = 2^{\binom{n}{2}}$), which signals inverting $\widehat{G}(x) = \exp(\widehat{C}(x))$ via $\widehat{C}(x) = \ln \widehat{G}(x)$.
- **Complete Derivation & Solution Sketch**:
  1. Let $g_n = 2^{\binom{n}{2}}$ (with $g_0 = 1$) be the total number of simple undirected graphs on $n$ labelled vertices, with EGF $\widehat{G}(x) = \sum_{n=0}^{\infty} 2^{\binom{n}{2}} \frac{x^n}{n!}$.
  2. Let $c_n$ be the number of connected simple graphs on $n$ labelled vertices ($c_0 = 0$), with EGF $\widehat{C}(x) = \sum_{n=1}^{\infty} c_n \frac{x^n}{n!}$.
  3. By the Exponential Formula ($\mathcal{G} = \operatorname{SET}(\mathcal{C})$), $\widehat{G}(x) = \exp(\widehat{C}(x))$, so $\widehat{C}(x) = \ln \widehat{G}(x) \bmod x^{n+1}$.
  4. Compute $\ln \widehat{G}(x) = \int_0^x \widehat{G}'(t) \widehat{G}(t)^{-1}\,dt \bmod x^{n+1}$ using NTT modulo $1004535809$, and output $c_n = n! [x^n] \widehat{C}(x) \bmod 1004535809$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Instead of counting connected graphs directly, how many total simple graphs exist on $n$ labelled vertices, and how does any simple graph decompose into connected components?
  - *Hint 2*: Express the relationship between the EGF $\widehat{G}(x)$ of all graphs and the EGF $\widehat{C}(x)$ of connected graphs using the $\operatorname{SET}$ operator (or isolate the component containing vertex $1$).
  - *Hint 3*: Since $\widehat{G}(x) = \exp(\widehat{C}(x))$, compute $\widehat{C}(x) = \ln \widehat{G}(x) \bmod x^{n+1}$ in $O(n \log n)$ time and multiply $[x^n]\widehat{C}(x)$ by $n!$.

---

#### Problem 3: 51nod 1728 — 不动点 (Fixed Point / Iterated Rooted Forests)
- **Judge & URL**: 51nod 1728 (`https://www.51nod.com/Challenge/Problem.html#problemId=1728`) — Featured in OI-Wiki `math/poly/egf.md`
- **Difficulty Tier**: `Stepping Stone` (Labelled $\operatorname{SET}$ & Rooted Bounded-Height Trees via Iterated $\exp$)
- **Mathematical Statement & Constraints**:
  Given integers $n$ and $k$, count the number of functions $f : \{1, 2, \dots, n\} \to \{1, 2, \dots, n\}$ such that $f^{(k)}(x) = f^{(k-1)}(x)$ for every $x \in \{1, \dots, n\}$, where $f^{(m)}$ denotes the $m$-fold composition of $f$ with itself (and $f^{(0)}(x) = x$). Output the answer modulo $998244353$ for $T$ test cases.
  - **Constraints**: $T \le 500$, $1 \le n, k \le 2 \times 10^3$ (or $n \le 10^5$ for single fixed $k$).
  - **Target Complexity**: $O(n k \log n)$ via polynomial $\exp$ or $O(n^2)$ precomputation via logarithmic derivative.
- **Diagnostic Signal & Modelling Bridge**:
  A functional graph $x \to f(x)$ is a set of connected components, each consisting of a directed cycle with rooted trees attached. The condition $f^{(k)}(x) = f^{(k-1)}(x)$ means every walk stabilizes after at most $k-1$ steps: therefore every cycle must have length $1$ (a fixed point $r$ with $f(r) = r$), and every vertex has distance at most $k-1$ to the root $r$!
- **Complete Derivation & Solution Sketch**:
  1. Each connected component is a rooted labelled tree of **height at most $k-1$** (where a single root vertex has height $0$). And the whole function $f$ is an unordered $\operatorname{SET}$ of such components, which is equivalent to adding a virtual super-root of height $k$!
  2. Let $\widehat{F}_m(x)$ be the EGF of a single rooted labelled tree of height at most $m-1$ (for $m \ge 1$). A root atom $\mathcal{Z}$ (EGF $x$) has an unordered $\operatorname{SET}$ of child subtrees each of height at most $m-2$:
     $$\widehat{F}_1(x) = x, \qquad \widehat{F}_m(x) = x \exp\!\big(\widehat{F}_{m-1}(x)\big) \quad (m \ge 2).$$
  3. The EGF of valid functions $f$ on $n$ elements is $\operatorname{SET}(\mathcal{F}_k)$, which has EGF $\exp(\widehat{F}_k(x)) = \frac{\widehat{F}_{k+1}(x)}{x}$.
  4. Using $\widehat{F}_m'(x) = \widehat{F}_m(x)\big(\frac{1}{x} + \widehat{F}_{m-1}'(x)\big)$, we can compute all $\widehat{F}_m(x) \bmod x^{N+1}$ in $O(N^2)$ total time across all $k$, or $O(N k \log N)$ via iterated `exp`.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Draw the directed graph with edges $u \to f(u)$. What does $f^{(k)}(u) = f^{(k-1)}(u)$ imply about the cycles of this graph and the maximum distance of any vertex to a cycle?
  - *Hint 2*: Every cycle must be a self-loop $r \to r$, and each connected component is a rooted tree of height $\le k-1$. How do you build a rooted labelled tree of height $\le m$ from subtrees of height $\le m-1$?
  - *Hint 3*: Define the EGF $\widehat{F}_1(x) = x$ and $\widehat{F}_m(x) = x \exp(\widehat{F}_{m-1}(x))$. The answer for $(n, k)$ is $n! [x^n] \exp(\widehat{F}_k(x))$.

---

#### Problem 4: Luogu P6189 — [NOI Online #1 入门组] 跑步 (Running / Partition Numbers)
- **Judge & URL**: Luogu P6189 (`https://www.luogu.com.cn/problem/P6189`)
- **Difficulty Tier**: `Stepping Stone` (Unlabelled Partitions via Durfee Square / Square-Root Split or Pentagonal Number Theorem)
- **Mathematical Statement & Constraints**:
  Calculate the number of integer partitions $p_n$ of $n$ modulo $P$ (where $P$ is an arbitrary integer $10^8 \le P \le 10^9 + 9$, not necessarily prime!).
  - **Constraints**: $1 \le n \le 10^5$, arbitrary modulus $P$.
  - **Target Complexity**: $O(n \sqrt{n})$ time, $O(n)$ space.
- **Diagnostic Signal & Modelling Bridge**:
  We need $[x^n] \prod_{k=1}^n (1 - x^k)^{-1} \bmod P$. Because the modulus $P$ is arbitrary (not NTT-friendly, and $1/j \bmod P$ may not exist for Euler transform $\ln/\exp$), we need a purely additive/subtractive $O(n\sqrt{n})$ method: either **Euler's Pentagonal Number Theorem** or the **Durfee Square / $\sqrt{n}$ Knapsack Split**!
- **Complete Derivation & Solution Sketch**:
  - **Method 1 (Euler's Pentagonal Number Recurrence)**:
    Since $\prod_{k=1}^{\infty}(1 - x^k) \cdot \sum_{n=0}^{\infty} p_n x^n = 1$, expanding the left-hand side via Euler's Pentagonal Number Theorem $\sum_{m=-\infty}^{\infty} (-1)^m x^{m(3m-1)/2}$ gives:
    $$p_n = \sum_{m=1}^{\infty} (-1)^{m-1} \left(p_{n - \frac{m(3m-1)}{2}} + p_{n - \frac{m(3m+1)}{2}}\right) \pmod P.$$
    Since $\frac{m(3m-1)}{2} \le n \implies m = O(\sqrt{n})$, this uses only additions and subtractions modulo $P$ in $O(n\sqrt{n})$ time!
  - **Method 2 (Durfee Square Identity)**:
    $$P(x) = \sum_{k=0}^{\lfloor\sqrt{n}\rfloor} \frac{x^{k^2}}{\prod_{i=1}^{k} (1 - x^i)^2},$$
    which also uses only additions modulo $P$ in $O(n\sqrt{n})$ time.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Notice that the modulus $P$ is not necessarily prime, so division is forbidden. How can you compute $\prod_{k=1}^n (1 - x^k)^{-1}$ using only additions and subtractions?
  - *Hint 2*: Either split the Ferrers diagram using its largest top-left $k \times k$ Durfee square ($k \le \sqrt{n}$), or consider the reciprocal product $\prod_{k=1}^{\infty} (1 - x^k)$.
  - *Hint 3*: By Euler's Pentagonal Number Theorem, $\prod_{k=1}^{\infty}(1-x^k) = 1 + \sum_{m\ge 1}(-1)^m (x^{m(3m-1)/2} + x^{m(3m+1)/2})$, giving a direct $O(n\sqrt{n})$ recurrence for $p_n$.

---

#### Problem 5: Codeforces 438E — The Child and Binary Tree
- **Judge & URL**: Codeforces 438E (`https://codeforces.com/problemset/problem/438/E`)
- **Difficulty Tier**: `Intermediate` (Unlabelled Symbolic Method $\mathcal{T} = \mathcal{E} + \mathcal{C} \times \mathcal{T}^2$ + Polynomial `sqrt` & `inv`)
- **Mathematical Statement & Constraints**:
  You are given a set $C = \{c_1, c_2, \dots, c_n\}$ of allowed positive integer vertex weights. A rooted binary tree (where left and right children are distinguished) is valid if every vertex has its weight in $C$. For each total weight $s = 1, 2, \dots, m$, find the number of valid rooted binary trees of total weight $s$ modulo $998244353$.
  - **Constraints**: $1 \le n, m \le 10^5$, $1 \le c_i \le 10^5$.
  - **Target Complexity**: $O(m \log m)$ time, $O(m)$ space.
- **Diagnostic Signal & Modelling Bridge**:
  A rooted plane binary tree is either empty (weight $0$) or consists of a root vertex with weight in $C$, an ordered left subtree, and an ordered right subtree. In the unlabelled Symbolic Method:
  $$\mathcal{T} = \mathcal{E} + \mathcal{C} \times \mathcal{T} \times \mathcal{T} \implies T(x) = 1 + C(x) T(x)^2.$$
- **Complete Derivation & Solution Sketch**:
  1. Let $C(x) = \sum_{i=1}^{n} x^{c_i}$ (truncated at $x^{m+1}$, with $[x^0]C(x) = 0$).
  2. Solving the quadratic equation $C(x) T(x)^2 - T(x) + 1 = 0$ via the quadratic formula appears to give $T(x) = \frac{1 \pm \sqrt{1 - 4C(x)}}{2C(x)}$, which has two issues: we must pick the sign, and $C(x)$ has $[x^0]C(x) = 0$ so $2C(x)$ is not invertible in $\mathbb{F}_p[[x]]$!
  3. **Zero-Magic Resolution**:
     - First, check $x = 0$: we need $[x^0]T(x) = 1$. Since $\sqrt{1 - 4C(0)} = 1$, choosing the $+$ sign would give $\frac{2}{0}$ (a Laurent pole!), whereas choosing the $-$ sign gives $1 - \sqrt{1 - 4C(x)} = 2C(x) + \dots$ which vanishes at $x = 0$.
     - Second, rationalize the numerator to eliminate the division by non-unit $C(x)$:
       $$T(x) = \frac{1 - \sqrt{1 - 4C(x)}}{2C(x)} = \frac{2}{1 + \sqrt{1 - 4C(x)}}!$$
     - Now the denominator $1 + \sqrt{1 - 4C(x)}$ has constant term $1 + 1 = 2 \in \mathbb{F}_p^\times$, so we compute $\sqrt{1 - 4C(x)} \bmod x^{m+1}$ and invert $1 + \sqrt{1 - 4C(x)} \bmod x^{m+1}$ in $O(m \log m)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Express the class of valid binary trees $\mathcal{T}$ recursively in terms of the empty tree $\mathcal{E}$, the root weight polynomial $C(x)$, and the left and right subtrees.
  - *Hint 2*: Solve $C(x) T(x)^2 - T(x) + 1 = 0$ for $T(x)$. Why can you NOT directly call polynomial `inv` on $2C(x)$?
  - *Hint 3*: Multiply numerator and denominator of $\frac{1 - \sqrt{1 - 4C(x)}}{2C(x)}$ by $1 + \sqrt{1 - 4C(x)}$ to obtain $T(x) = \frac{2}{1 + \sqrt{1 - 4C(x)}}$, whose denominator has constant term $2 \ne 0$.

---

#### Problem 6: Codeforces 891E — Lust
- **Judge & URL**: Codeforces 891E (`https://codeforces.com/problemset/problem/891/E`) — Featured in OI-Wiki `math/poly/egf.md`
- **Difficulty Tier**: `Intermediate` (Labelled EGF Binomial Convolution & Operator Algebra)
- **Mathematical Statement & Constraints**:
  Given an array $a_1, a_2, \dots, a_n$ and an integer $k$, in each of $k$ steps you uniformly at random choose an index $i \in \{1, \dots, n\}$ and decrement $a_i$ by $1$. Compute the expected value of $a_1 a_2 \dots a_n$ minus the final product $a'_1 a'_2 \dots a'_n$, modulo $10^9 + 7$.
  - **Constraints**: $1 \le n \le 5000$, $1 \le k \le 10^9$, $0 \le a_i \le 10^9$.
  - **Target Complexity**: $O(n^2)$ time, $O(n)$ space.
- **Diagnostic Signal & Modelling Bridge**:
  Although $k \le 10^9$ is huge, $n \le 5000$ is small. Distributing $k$ labelled time-steps among $n$ buckets so bucket $i$ receives $c_i$ decrements carries the multinomial weight $\frac{k!}{c_1!\cdots c_n!}$, which is the exact coefficient $k![x^k]$ of an $n$-fold **EGF product**!
- **Complete Derivation & Solution Sketch**:
  1. Let $c_i$ be the number of times index $i$ is decremented ($\sum_{i=1}^n c_i = k$). The expected final product is:
     $$\mathbb{E}\left[\prod_{i=1}^n (a_i - c_i)\right] = \frac{1}{n^k} \sum_{c_1 + \dots + c_n = k} \frac{k!}{c_1! \cdots c_n!} \prod_{i=1}^{n} (a_i - c_i) = \frac{k!}{n^k} [x^k] \prod_{i=1}^{n} \left(\sum_{c=0}^{\infty} (a_i - c) \frac{x^c}{c!}\right).$$
  2. Using $\sum_{c=0}^{\infty} c \frac{x^c}{c!} = x e^x$, each factor simplifies to:
     $$\sum_{c=0}^{\infty} (a_i - c) \frac{x^c}{c!} = (a_i - x) e^x.$$
  3. Therefore, the product over $i = 1, \dots, n$ is $e^{nx} \prod_{i=1}^{n} (a_i - x)$.
  4. Expand the degree-$n$ polynomial $P(x) = \prod_{i=1}^{n} (a_i - x) = \sum_{j=0}^{n} p_j x^j$ in $O(n^2)$ time. Then:
     $$\frac{k!}{n^k} [x^k] \big(e^{nx} P(x)\big) = \frac{k!}{n^k} \sum_{j=0}^{\min(n, k)} p_j \frac{n^{k-j}}{(k-j)!} = \sum_{j=0}^{\min(n, k)} p_j \frac{k^{\underline{j}}}{n^j}.$$
     Subtract this from $\prod_{i=1}^n a_i \bmod (10^9+7)$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: If index $i$ is chosen $c_i$ times ($\sum c_i = k$), how many sequences of choices produce $(c_1, \dots, c_n)$? Why does $\frac{k!}{c_1!\cdots c_n!}$ suggest an Exponential Generating Function?
  - *Hint 2*: Write the single-element EGF $\sum_{c=0}^{\infty} (a_i - c) \frac{x^c}{c!}$ in closed form using $e^x$.
  - *Hint 3*: Factor $\prod_{i=1}^n (a_i - x)e^x = e^{nx} \prod_{i=1}^n (a_i - x)$. Since $\prod_{i=1}^n (a_i - x)$ has degree $n \le 5000$, expand it in $O(n^2)$ and extract $[x^k]$ analytically!

---

#### Problem 7: LOJ #6538 — 烷基计数 加强版 加强版 (Alkyl Radical Enumeration / Unlabelled Rooted Ternary Trees)
- **Judge & URL**: LibreOJ #6538 (`https://loj.ac/p/6538`) / Luogu P6597 (`https://www.luogu.com.cn/problem/P6597`)
- **Difficulty Tier**: `Intermediate` (Unlabelled Pólya / Cycle Index $\operatorname{MSET}_3(\mathcal{A})$ + Newton's Method)
- **Mathematical Statement & Constraints**:
  An alkyl radical with $n$ carbon atoms is an unlabelled rooted tree on $n$ vertices in which the root has degree at most $3$ and every non-root vertex has degree at most $4$ (so every vertex has at most $3$ children, and the order of children does not matter). Compute the number of alkyl radicals of size $1, 2, \dots, n$ modulo $998244353$.
  - **Constraints**: $1 \le n \le 10^5$.
  - **Target Complexity**: $O(n \log n)$ time, $O(n)$ space.
- **Diagnostic Signal & Modelling Bridge**:
  Each carbon atom (weight $x$) has an **unordered multiset of size $3$** of subtrees drawn from $\mathcal{A}$ (where $\mathcal{A}$ includes the empty subtree $\epsilon$ of size $0$). Since $k = 3$ is fixed and small, we use the cycle index of the symmetric group $S_3$ from Pólya's theorem:
  $$Z_{S_3}(s_1, s_2, s_3) = \frac{1}{6}\big(s_1^3 + 3 s_1 s_2 + 2 s_3\big).$$
- **Complete Derivation & Solution Sketch**:
  1. Let $A(x) = \sum_{k=0}^{\infty} a_k x^k$ with $a_0 = 1$ (representing an empty hydrogen branch).
  2. A non-empty tree consists of a root carbon atom $x$ and an unordered 3-multiset of branches from $A(x)$:
     $$A(x) = 1 + x \cdot Z_{S_3}\big(A(x), A(x^2), A(x^3)\big) = 1 + \frac{x}{6}\Big(A(x)^3 + 3 A(x) A(x^2) + 2 A(x^3)\Big).$$
  3. When solving up to $x^N$ by doubling ($n \to 2n$), notice that $A(x^2) \bmod x^{2n}$ and $A(x^3) \bmod x^{2n}$ only depend on coefficients of $A(x)$ of degree $< n$, which are **already known** from the previous doubling step!
  4. Thus, treating $A(x^2)$ and $A(x^3)$ as known constants at step $2n$, we apply one step of Newton's method $A \leftarrow A - \frac{\Phi(A)}{\Phi'(A)}$ where $\Phi(A) = \frac{x}{6}(A(x)^3 + 3A(x)A(x^2) + 2A(x^3)) - A(x) + 1$ and $\Phi'(A) = \frac{x}{2}(A(x)^2 + A(x^2)) - 1$ in $O(n \log n)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: View an empty child slot as a size-$0$ tree ($a_0 = 1$), so every vertex has an unordered multiset of **exactly 3** subtrees. How do you express $\operatorname{MSET}_3(\mathcal{A})$ in terms of $A(x)$, $A(x^2)$, and $A(x^3)$?
  - *Hint 2*: Apply Burnside's Lemma to $S_3$ acting on $\mathcal{A}^3$: the cycle types in $S_3$ are $(1,1,1)$ (1 element), $(2,1)$ (3 transpositions), and $(3)$ (2 3-cycles).
  - *Hint 3*: Solve $A(x) = 1 + \frac{x}{6}(A(x)^3 + 3A(x)A(x^2) + 2A(x^3))$ via Newton's method: when lifting precision from $x^m$ to $x^{2m}$, $A(x^2)$ and $A(x^3)$ are already fully determined!

---

#### Problem 8: AtCoder ABC 222 H — Beautiful Binary Tree
- **Judge & URL**: AtCoder Beginner Contest 222 Problem H (`https://atcoder.jp/contests/abc222/tasks/abc222_h`)
- **Difficulty Tier**: `Intermediate` (Unlabelled Symbolic Method $\operatorname{SEQ}$ + Formal Calculus / Rational Power Extraction)
- **Mathematical Statement & Constraints**:
  Find the number of "beautiful binary trees" with $N$ vertices modulo $998244353$, which reduces via the problem's combinatorics to extracting the coefficient:
  $$a_N = \frac{1}{N} [x^{N-1}] \left(1 + 3x + x(1 + x)^2\right)^N = \frac{1}{N} [x^{N-1}] \big((1 + x)(1 + 3x + x^2)\big)^N.$$
  - **Constraints**: $1 \le N \le 10^7$.
  - **Target Complexity**: $O(N)$ time via D-finite ODE recurrence (or $O(N \log N)$ via FPS).
- **Diagnostic Signal & Modelling Bridge**:
  We need $[x^{N-1}] P(x)^N$ where $P(x) = (1+x)(1+3x+x^2)$ is a fixed sparse polynomial of degree $3$, and $N = 10^7$ is too large for $O(N \log N)$ NTT within the time limit! By Iteration 53.6 (Reverse-Engineering Scratchpad 2), $H(x) = P(x)^N$ satisfies the linear first-order ODE:
  $$P(x) H'(x) = N P'(x) H(x),$$
  which yields a 4-term linear recurrence for $[x^k]H(x)$ in $O(N)$ time!
- **Complete Derivation & Solution Sketch**:
  1. Let $H(x) = \sum_{k=0}^{3N} h_k x^k = \big(1 + 4x + 4x^2 + x^3\big)^N$, so $P(x) = 1 + 4x + 4x^2 + x^3$ and $P'(x) = 4 + 8x + 3x^2$.
  2. Differentiating $H(x) = P(x)^N$ gives $P(x) H'(x) = N P'(x) H(x)$.
  3. Extracting $[x^k]$ on both sides for $k = 0, 1, \dots, N-2$:
     $$(k+1)h_{k+1} + 4k h_k + 4(k-1)h_{k-1} + (k-2)h_{k-2} = N\big(4h_k + 8h_{k-1} + 3h_{k-2}\big).$$
  4. Solving for $h_{k+1}$ gives an $O(1)$-per-step recurrence using precomputed modular inverses of $1, \dots, N$, computing $h_{N-1}$ in $O(N)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Write the generating function of the tree construction (or via Lagrange inversion) to reduce the answer to $\frac{1}{N}[x^{N-1}] (1 + 4x + 4x^2 + x^3)^N$.
  - *Hint 2*: Since $N = 10^7$, NTT is slow, but $P(x) = 1 + 4x + 4x^2 + x^3$ has only 4 terms! What differential equation does $H(x) = P(x)^N$ satisfy?
  - *Hint 3*: Compare $[x^k]$ on both sides of $P(x) H'(x) = N P'(x) H(x)$ to compute $h_0, h_1, \dots, h_{N-1}$ in $O(N)$ time.

---

#### Problem 9: UOJ #50 — [UR #3] 链式反应 (Chain Reaction)
- **Judge & URL**: UOJ #50 (`https://uoj.ac/problem/50`)
- **Difficulty Tier**: `Intermediate` (Labelled Boxed Product / `有标号定根技巧` ODE $\widehat{F}' = \frac{1}{2}\widehat{A}\widehat{F}^2 + 1$)
- **Mathematical Statement & Constraints**:
  Given a binary string $a_1 a_2 \dots a_n$ specifying allowed non-cascading bombardment sizes ($a_k \in \{0, 1\}$), a valid rooted reaction tree on $m$ labelled atoms has vertex $1$ as the root, and each cascading atom triggers two unordered sub-cascades of sizes $i, j \ge 1$ plus $k \ge 0$ leaf atoms ($a_k = 1$). Compute the number of valid structures for all $m = 1, 2, \dots, n$ modulo $998244353$.
  - **Constraints**: $1 \le n \le 2 \times 10^5$.
  - **Target Complexity**: $O(n \log n)$ via Newton's method on ODE or $O(n \log^2 n)$ via CDQ divide-and-conquer FFT.
- **Diagnostic Signal & Modelling Bridge**:
  The root atom must have the smallest label among all atoms in its subtree (an increasing tree structure!). Isolating the root (label $1$) partitions the remaining $m-1$ labels into $(i, j, k)$, producing the multinomial factor $\binom{m-1}{i, j, k}$—the exact signature of the **Boxed Product / `有标号定根技巧`**!
- **Complete Derivation & Solution Sketch**:
  1. As derived in Section 56.4, the recurrence is:
     $$f_m = \frac{1}{2} \sum_{i + j + k = m - 1} \frac{(m-1)!}{i! j! k!} a_k f_i f_j \quad (m \ge 2), \quad f_1 = 1.$$
  2. Dividing by $(m-1)!$ and summing against $x^{m-1}$ yields the first-order non-linear ODE for the EGF $\widehat{F}(x) = \sum_{m=1}^{\infty} f_m \frac{x^m}{m!}$:
     $$\widehat{F}'(x) = \frac{1}{2} \widehat{A}(x) \widehat{F}(x)^2 + 1, \qquad \widehat{F}(0) = 0.$$
  3. To solve this up to $x^{n+1}$:
     - **Via CDQ Divide-and-Conquer FFT ($O(n \log^2 n)$)**: First let $\widehat{G}(x) = \widehat{A}(x) \widehat{F}(x)$ and solve simultaneously when advancing the mid-point $[l, r]$.
     - **Via Newton's Method on ODE ($O(n \log n)$)**: Given $\widehat{F}_0 \equiv \widehat{F} \pmod{x^m}$, linearizing $\widehat{F}' - \frac{1}{2}\widehat{A}\widehat{F}^2 - 1 = 0$ gives the linear first-order ODE for $\widehat{F}$:
       $$\widehat{F}' - (\widehat{A}\widehat{F}_0) \widehat{F} \equiv 1 - \frac{1}{2}\widehat{A}\widehat{F}_0^2 \pmod{x^{2m}},$$
       solved via the integrating factor $\mu(x) = \exp\!\left(-\int_0^x \widehat{A}(t)\widehat{F}_0(t)\,dt\right)$!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Since every parent has a smaller label than all vertices in its subtree, the root of the entire structure must carry label $1$. Write the recurrence by partitioning the remaining $m-1$ labels.
  - *Hint 2*: Divide your recurrence for $f_m$ by $(m-1)!$ instead of $m!$. What differential equation does the EGF $\widehat{F}(x)$ satisfy?
  - *Hint 3*: Solve $\widehat{F}'(x) = \frac{1}{2}\widehat{A}(x)\widehat{F}(x)^2 + 1$ using CDQ divide-and-conquer FFT in $O(n \log^2 n)$ or Newton's method with integrating factor in $O(n \log n)$.

---

#### Problem 10: yukicoder No. 899 — 逆オイラー変換 (Inverse Euler Transform / Graph Component Recovery)
- **Judge & URL**: yukicoder / AtCoder / LOJ #6268 (`https://loj.ac/p/6268` — 分拆数 / Inverse Euler Transform applications)
- **Difficulty Tier**: `Intermediate` (Inverse Euler Transform via $\ln$ + Möbius Inversion)
- **Mathematical Statement & Constraints**:
  You are given the sequence $f_0 = 1, f_1, f_2, \dots, f_N \pmod{998244353}$, which is the OGF of multisets $\operatorname{MSET}(\mathcal{A})$ formed from an unknown unlabelled class $\mathcal{A}$:
  $$F(x) = \sum_{n=0}^{N} f_n x^n \equiv \prod_{k=1}^{N} (1 - x^k)^{-a_k} \pmod{x^{N+1}}.$$
  Recover the sequence $a_1, a_2, \dots, a_N \pmod{998244353}$.
  - **Constraints**: $1 \le N \le 10^5$.
  - **Target Complexity**: $O(N \log N)$ time, $O(N)$ space.
- **Diagnostic Signal & Modelling Bridge**:
  Whenever we know the total count of unlabelled composite objects $f_n$ (e.g., unlabelled forests or total knapsack combinations) and need to recover the number of **connected unlabelled components** or **available coin denominations** $a_k$, we apply the **Inverse Euler Transform** (Section 54.3).
- **Complete Derivation & Solution Sketch**:
  1. Compute $G(x) = \ln F(x) \bmod x^{N+1}$ (or directly $C(x) = x F'(x) F(x)^{-1} \bmod x^{N+1}$) in $O(N \log N)$ time.
  2. By Section 54.3, the $n$-th coefficient of $C(x) = x G'(x)$ satisfies:
     $$c_n = n [x^n] \ln F(x) = \sum_{d \mid n} d \cdot a_d \qquad (1 \le n \le N).$$
  3. Apply Dirichlet / Möbius inversion in $O(N \log N)$ time:
     $$a_n = \frac{1}{n} \sum_{d \mid n} \mu\!\left(\frac{n}{d}\right) c_d \pmod{998244353}.$$
- **Progressive 3-Tier Hints**:
  - *Hint 1*: How is $\ln F(x)$ related to the unknown exponents $a_1, \dots, a_N$ in $\prod_{k=1}^N (1 - x^k)^{-a_k}$?
  - *Hint 2*: Expand $x \frac{d}{dx} \ln F(x) = \frac{x F'(x)}{F(x)}$ as a power series and collect the coefficient of $x^n$ in terms of the divisors $d \mid n$.
  - *Hint 3*: Since $[x^n]\frac{xF'(x)}{F(x)} = \sum_{d \mid n} d a_d$, compute $xF'(x)F(x)^{-1} \bmod x^{N+1}$ via polynomial inversion and invert the divisor sum in $O(N \log N)$ time.

---

### 57.4 Tier 3 & Tier 4 Accepted Problems (`Advanced` & `Mastery`)

#### Problem 11: AtCoder ABC 236 Ex — Distinct Multiples
- **Judge & URL**: AtCoder Beginner Contest 236 Problem Ex (`https://atcoder.jp/contests/abc236/tasks/abc236_h`)
- **Difficulty Tier**: `Advanced` (Inclusion-Exclusion on Connected Components via $\ln(1+x)$ + EGF $\exp$)
- **Mathematical Statement & Constraints**:
  Given $N$ positive integers $D_1, D_2, \dots, D_N$ and an upper bound $M$, count the number of tuples $(A_1, A_2, \dots, A_N)$ of positive integers such that:
  1. $1 \le A_i \le M$ and $D_i \mid A_i$ for all $i = 1, \dots, N$;
  2. $A_i \ne A_j$ for all $1 \le i < j \le N$ (all elements are pairwise distinct).
  Output the answer modulo $998244353$.
  - **Constraints**: $1 \le N \le 16$, $1 \le M, D_i \le 10^{18}$.
  - **Target Complexity**: $O(3^N)$ via subset-convolution $\exp$, or $O(N^2 2^N)$ via ranked Möbius transform / FPS $\exp$ on Set Power Series.
- **Diagnostic Signal & Modelling Bridge**:
  The pairwise distinctness condition $A_i \ne A_j$ over $\binom{N}{2}$ pairs is a graph-coloring / inclusion-exclusion problem on $K_N$. For any subset of edges $E \subseteq \binom{[N]}{2}$ representing violated constraints ($A_i = A_j$), each connected component $S \subseteq [N]$ forces all $A_i$ ($i \in S$) to be equal, giving $\lfloor M / \operatorname{lcm}_{i \in S}(D_i) \rfloor$ choices!
  What is the sum of $(-1)^{|E|}$ over all edge sets $E$ that make a subset $S$ of size $k = |S|$ connected? By Idiom JA-2 (Section 57.2, $\ln(1 + x) = \sum_{k\ge 1} (-1)^{k-1}(k-1)! \frac{x^k}{k!}$), it is **exactly $(-1)^{k-1}(k-1)!$**!
- **Complete Derivation & Solution Sketch**:
  1. Let $c(G)$ be the number of connected components of a spanning subgraph $G = ([N], E)$. By PIE:
     $$\text{Ans} = \sum_{E \subseteq \binom{[N]}{2}} (-1)^{|E|} \prod_{S \in \text{comp}(G)} \left\lfloor \frac{M}{\operatorname{lcm}_{i \in S} D_i} \right\rfloor.$$
  2. Group the sum by the partition of $[N]$ into connected components $\{S_1, \dots, S_r\}$. For each component $S$ of size $k = |S|$, the sum of $(-1)^{|E_S|}$ over all connected graphs on $S$ is the $k$-th coefficient of $k! [x^k] \ln(1 + x) = (-1)^{k-1}(k-1)!$.
  3. Define the single-component weight for each non-empty subset $S \subseteq [N]$:
     $$w(S) := (-1)^{|S|-1} (|S| - 1)! \left\lfloor \frac{M}{\operatorname{lcm}_{i \in S} D_i} \right\rfloor \pmod{998244353}.$$
  4. Then the answer is the Set-Partition Exponential ($\operatorname{SET}$) of $w(S)$, computed via Boxed-Product DP (fixing the minimum element $\min(T)$ of each subset $T \subseteq [N]$):
     $$dp[T] = \sum_{\substack{S \subseteq T \\ \min(T) \in S}} w(S) \cdot dp[T \setminus S], \qquad dp[\emptyset] = 1.$$
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Apply inclusion-exclusion to the $\binom{N}{2}$ conditions $A_i \ne A_j$. If you pick a subset of equalities $E$, what must be true about all $A_i$ in the same connected component $S$ of $E$?
  - *Hint 2*: Instead of summing over all $2^{\binom{N}{2}}$ edge sets, fix a connected component $S$ of size $k$. What is $\sum_{G \text{ connected on } k \text{ vertices}} (-1)^{|E(G)|}$? Use the EGF $\widehat{F}(x) = \sum_{k\ge 0} (1 - 1)^{\binom{k}{2}} \frac{x^k}{k!} = 1 + x$ and take $\ln \widehat{F}(x)$!
  - *Hint 3*: Each connected component $S$ has weight $w(S) = (-1)^{|S|-1}(|S|-1)! \lfloor M / \operatorname{lcm}_{i\in S} D_i \rfloor$. Combine components into a partition of $[N]$ using the Boxed-Product subset DP fixing $\min(T) \in S$.

---

#### Problem 12: AtCoder ARC 105 F — Lights Out on Connected Graph
- **Judge & URL**: AtCoder Regular Contest 105 Problem F (`https://atcoder.jp/contests/arc105/tasks/arc105_f`) — Also generalized to $N \le 10^5$ via FPS `ln`/`sqrt` on Library Checker / yukicoder
- **Difficulty Tier**: `Advanced` (Labelled Connected Bipartite Graphs via $\frac{1}{2}\ln \widehat{B}_2(x)$)
- **Mathematical Statement & Constraints**:
  As shown in the game analysis of Lights Out on a connected undirected graph $G$, the game is winnable from all initial states if and only if $G$ is **connected and bipartite**. Count the number of connected bipartite simple graphs on $N$ labelled vertices (in ARC 105 F on a given edge set $M$ for $N \le 17$, and in the standard FPS version on $K_N$ for $N \le 10^5$ modulo $998244353$).
  - **Constraints**: $1 \le N \le 10^5$ (FPS version) / $N \le 17$ (subgraph version).
  - **Target Complexity**: $O(N \log N)$ time for the complete graph version via FPS.
- **Diagnostic Signal & Modelling Bridge**:
  A bipartite graph is a graph that admits a 2-coloring, and each **connected** bipartite graph admits **exactly $2$** proper 2-colorings. This signals:
  1. Count all 2-colored graphs $b_n^{(2)} = \sum_{k=0}^n \binom{n}{k} 2^{k(n-k)}$ via Chirp-Z square completion;
  2. Take $\ln$ to isolate connected 2-colored graphs;
  3. Divide by $2$ to get connected uncolored bipartite graphs!
- **Complete Derivation & Solution Sketch**:
  1. Using $k(n-k) = \binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}$, define $\widehat{H}(x) = \sum_{k=0}^{N} 2^{-\binom{k}{2}} \frac{x^k}{k!}$.
  2. Compute $\widehat{H}(x)^2 \bmod x^{N+1}$ via a single NTT multiplication. Then the EGF of 2-colored graphs is:
     $$\widehat{B}_2(x) = \sum_{n=0}^{N} 2^{\binom{n}{2}} \big([x^n] \widehat{H}(x)^2\big) x^n.$$
  3. Compute $\widehat{C}_{\text{bip}}(x) = \frac{1}{2} \ln \widehat{B}_2(x) \bmod x^{N+1}$. The number of connected bipartite graphs on $n$ labelled vertices is $n! [x^n] \widehat{C}_{\text{bip}}(x)$! (And the number of all bipartite graphs is $n! [x^n] \exp(\widehat{C}_{\text{bip}}(x)) = n! [x^n] \sqrt{\widehat{B}_2(x)}$).
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Why is it easier to count graphs equipped with a explicit black/white 2-coloring of the vertices than uncolored bipartite graphs?
  - *Hint 2*: Use $k(n-k) = \binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}$ to compute $b_n^{(2)} = \sum_{k=0}^n \binom{n}{k} 2^{k(n-k)}$ for all $n \le N$ using a single polynomial squaring.
  - *Hint 3*: If $\widehat{B}_2(x)$ is the EGF of 2-colored graphs, what does $\ln \widehat{B}_2(x)$ count, and how many 2-colorings does a single connected bipartite graph have?

---

#### Problem 13: Luogu P5824 — 十二重计数法 (The Twelvefold Way)
- **Judge & URL**: Luogu P5824 (`https://www.luogu.com.cn/problem/P5824`)
- **Difficulty Tier**: `Advanced` (Complete OGF/EGF Synthesis of Stanley's Twelvefold Way)
- **Mathematical Statement & Constraints**:
  Given $n$ balls and $m$ boxes, output the number of ways to place the $n$ balls into the $m$ boxes modulo $998244353$ under all **12 combinations** of:
  - Balls: Labelled (`L`) vs. Unlabelled (`U`);
  - Boxes: Labelled (`L`) vs. Unlabelled (`U`);
  - Capacity constraint: Arbitrary (`—`), Injective / at most 1 ball per box ($\le 1$), Surjective / at least 1 ball per box ($\ge 1$).
  - **Constraints**: $1 \le n, m \le 2 \times 10^5$.
  - **Target Complexity**: $O((n + m) \log(n + m))$ time, $O(n + m)$ space.
- **Diagnostic Signal & Modelling Bridge**:
  This problem is the ultimate test of distinguishing **Labelled ($\operatorname{SEQ}_m / \operatorname{SET}_m$ of EGFs)** from **Unlabelled ($\operatorname{SEQ}_m / \operatorname{MSET}_m$ of OGFs)**:
  - **Labelled Balls (`L`) $\implies$ EGF**: Each box holds a subset of labels, with EGF $e^x$ (arbitrary), $1 + x$ ($\le 1$), or $e^x - 1$ ($\ge 1$).
    - Labelled Boxes (`L`): $\operatorname{SEQ}_m$ of boxes $\implies$ raise box EGF to the $m$-th power!
    - Unlabelled Boxes (`U`): $\operatorname{SET}_m$ of boxes $\implies$ divide by $m!$ for non-empty boxes!
  - **Unlabelled Balls (`U`) $\implies$ OGF**: Balls only have count, no labels.
    - Labelled Boxes (`L`): $\operatorname{SEQ}_m$ of box OGFs $(1-x)^{-1}$, $(1+x)$, or $x(1-x)^{-1}$ $\implies$ stars and bars!
    - Unlabelled Boxes (`U`): Partition numbers $p_{\le m}(n)$ and $p_{=m}(n) = p_{\le m}(n - m)$ via Euler's Pentagonal Number Theorem / Euler Transform!
- **Complete Derivation & Solution Sketch**:
  Let us tabulate all 12 formulas and their fast FPS evaluation:
  1. **(L, L, —)**: $n! [x^n] (e^x)^m = m^n$.
  2. **(L, L, $\le 1$)**: $n! [x^n] (1 + x)^m = m^{\underline{n}} = \binom{m}{n} n!$.
  3. **(L, L, $\ge 1$)**: $n! [x^n] (e^x - 1)^m = m! \left\{\begin{matrix} n \\ m \end{matrix}\right\} = \sum_{j=0}^{m} (-1)^{m-j} \binom{m}{j} j^n$ (computed in $O(m \log m)$ or $O(m)$ via linear sieve of $j^n$).
  4. **(L, U, —)**: $\sum_{k=0}^{m} \left\{\begin{matrix} n \\ k \end{matrix}\right\}$ (compute row $n$ of Stirling 2nd kind $\left\{\begin{matrix} n \\ k \end{matrix}\right\} = \sum_{j=0}^k \frac{(-1)^{k-j}}{(k-j)!} \frac{j^n}{j!}$ via NTT convolution in $O(n \log n)$ and sum for $k \le m$).
  5. **(L, U, $\le 1$)**: $[n \le m]$.
  6. **(L, U, $\ge 1$)**: $\left\{\begin{matrix} n \\ m \end{matrix}\right\} = n! [x^n] \frac{(e^x - 1)^m}{m!}$.
  7. **(U, L, —)**: $[x^n] (1 - x)^{-m} = \binom{n + m - 1}{n}$.
  8. **(U, L, $\le 1$)**: $[x^n] (1 + x)^m = \binom{m}{n}$.
  9. **(U, L, $\ge 1$)**: $[x^n] x^m (1 - x)^{-m} = \binom{n - 1}{m - 1}$.
  10. **(U, U, —)**: Partitions of $n$ into $\le m$ parts = $[x^n] \prod_{k=1}^{m} (1 - x^k)^{-1}$, computed in $O(n \log n)$ via Euler Transform (`ln`/`exp` harmonic sieve) or Pentagonal Number `inv`!
  11. **(U, U, $\le 1$)**: $[n \le m]$.
  12. **(U, U, $\ge 1$)**: Partitions of $n$ into exactly $m$ parts = $[x^{n-m}] \prod_{k=1}^{m} (1 - x^k)^{-1}$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Classify the 12 cases by whether balls are labelled (EGF) or unlabelled (OGF), and whether boxes are ordered ($\operatorname{SEQ}_m$) or unordered ($\operatorname{SET}_m$ / $\operatorname{MSET}_m$).
  - *Hint 2*: For Cases 3, 4, 6 (Stirling numbers of the second kind $\left\{\begin{matrix} n \\ k \end{matrix}\right\}$ for fixed $n$ and all $k \le m$), write $\left\{\begin{matrix} n \\ k \end{matrix}\right\} = \sum_{j=0}^k \frac{(-1)^{k-j}}{(k-j)!} \cdot \frac{j^n}{j!}$ as a single convolution.
  - *Hint 3*: For Cases 10 and 12 (unlabelled balls and unlabelled boxes), use Ferrers conjugation to equate $\le m$ boxes with parts of size $\le m$, and evaluate $\prod_{k=1}^m (1 - x^k)^{-1} \bmod x^{n+1}$ via the harmonic-sieve Euler transform.

---

#### Problem 14: Codeforces 1251F — Red-White Fence
- **Judge & URL**: Codeforces 1251F (`https://codeforces.com/problemset/problem/1251/F`)
- **Difficulty Tier**: `Intermediate` (Unlabelled OGF Independent Choice Product $\prod (1 + 2x)(1 + x)^2$)
- **Mathematical Statement & Constraints**:
  You have $n$ white boards of lengths $a_1, \dots, a_n$ and $k$ red boards of lengths $b_1, \dots, b_k$ ($k \le 5$). To build a valid fence around a single red board of length $B$, you may choose any subset of white boards of lengths strictly less than $B$ and place each white board either to the left or to the right of the red board, such that white board lengths strictly increase up to $B$ and strictly decrease after $B$ (so at most 2 white boards of any given length $L < B$ can be used). Answer $q$ queries for the number of valid fences of perimeter $Q_j$ modulo $998244353$.
  - **Constraints**: $1 \le n, q \le 3 \times 10^5$, $1 \le k \le 5$, $a_i, b_i \le 3 \times 10^5$.
  - **Target Complexity**: $O(k n \log n + q)$ time, $O(n)$ space.
- **Diagnostic Signal & Modelling Bridge**:
  For a fixed red board of height $B$, consider each distinct white board height $L < B$ independently:
  - If there is **only $1$** white board of height $L$ available, we can either omit it ($1$), place it on the left ($x$), or place it on the right ($x$): OGF is **$1 + 2x$**.
  - If there are **$\ge 2$** white boards of height $L$ available (say $m \ge 2$ identical boards, treated as distinguishable by index in the problem), we can choose $0$ boards ($1$ way), $1$ board and place it left or right ($2$ ways), or $2$ boards (one left, one right: $1$ way): OGF is **$1 + 2x + x^2 = (1 + x)^2$**!
- **Complete Derivation & Solution Sketch**:
  1. For each of the $k \le 5$ red boards $B$, count the number $c_1$ of lengths $L < B$ that appear **exactly once** among the white boards, and the number $c_2$ of lengths $L < B$ that appear **at least twice**.
  2. Since choices across different lengths $L$ are independent, the OGF of the number of chosen white boards is:
     $$F_B(x) = (1 + 2x)^{c_1} (1 + x)^{2 c_2}.$$
  3. Because the binomial expansions of $(1 + 2x)^{c_1}$ and $(1 + x)^{2 c_2}$ are known in $O(n)$ closed form:
     $$[x^i](1 + 2x)^{c_1} = \binom{c_1}{i} 2^i, \qquad [x^j](1 + x)^{2c_2} = \binom{2c_2}{j},$$
     we compute $F_B(x)$ in **a single NTT convolution** per red board ($k \le 5$ convolutions total)!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Fix one of the $k \le 5$ red boards of height $B$. Once you choose which white board heights appear on the left and which appear on the right, is their left-to-right ordering already uniquely forced?
  - *Hint 2*: Write the OGF for a single distinct height $L < B$ depending on whether its frequency is $1$ or $\ge 2$.
  - *Hint 3*: Multiply $(1 + 2x)^{c_1}$ and $(1 + x)^{2c_2}$ using a single NTT per red board.

---

#### Problem 15: Codeforces 960G — Bandit Blues
- **Judge & URL**: Codeforces 960G (`https://codeforces.com/problemset/problem/960/G`)
- **Difficulty Tier**: `Advanced` (Labelled Boxed Product / Pivot-Label Decomposition & Stirling Numbers of the 1st Kind)
- **Mathematical Statement & Constraints**:
  Find the number of permutations of $\{1, 2, \dots, n\}$ that have **exactly $A$ prefix maxima** (left-to-right maxima) and **exactly $B$ suffix maxima** (right-to-left maxima), modulo $998244353$.
  - **Constraints**: $1 \le n \le 10^5$, $0 \le A, B \le n$.
  - **Target Complexity**: $O(n \log n)$ via doubling + Taylor shift, or $O(n \log^2 n)$ via divide-and-conquer NTT.
- **Diagnostic Signal & Modelling Bridge**:
  Apply the **Boxed Product / Pivot-Label Split** at the global maximum element $n$:
  - Every prefix maximum (except $n$ itself) lies strictly to the left of $n$;
  - Every suffix maximum (except $n$ itself) lies strictly to the right of $n$;
  - Within the elements to the left of $n$, each record-to-next-record block is a directed cycle with its maximum element fixed at the front! Thus a permutation of $k$ elements with $c$ prefix maxima corresponds bijectively to a permutation of $k$ elements with $c$ disjoint cycles, counted by the unsigned Stirling number of the first kind $\left[\begin{matrix} k \\ c \end{matrix}\right]$!
- **Complete Derivation & Solution Sketch**:
  1. If $A = 0$ or $B = 0$ or $A + B - 2 > n - 1$, the answer is $0$.
  2. Split the permutation at the global maximum $n$: choose $k$ elements from $\{1, \dots, n-1\}$ to go to the left of $n$ (forming $A - 1$ prefix maxima) and $n - 1 - k$ elements to go to the right of $n$ (forming $B - 1$ suffix maxima).
  3. Even simpler: before deciding whether each of the $A + B - 2$ cycle-blocks goes to the left of $n$ or to the right of $n$, partition $\{1, \dots, n-1\}$ into $A + B - 2$ cycles in $\left[\begin{matrix} n - 1 \\ A + B - 2 \end{matrix}\right]$ ways, and then choose which $A - 1$ of those cycles go to the left of $n$ (where their internal order is uniquely sorted by their cycle maxima!) in $\binom{A + B - 2}{A - 1}$ ways!
  4. Therefore:
     $$\text{Ans} = \left[\begin{matrix} n - 1 \\ A + B - 2 \end{matrix}\right] \binom{A + B - 2}{A - 1} = \binom{A + B - 2}{A - 1} \cdot [x^{A+B-2}] \prod_{i=0}^{n-2} (x + i).$$
  5. Compute $P_{n-1}(x) = x^{\overline{n-1}} = \prod_{i=0}^{n-2}(x + i)$ in $O(n \log n)$ via doubling $P_{2m}(x) = P_m(x) P_m(x + m)$ (`TaylorShift`) or $O(n \log^2 n)$ via divide-and-conquer NTT.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Locate the global maximum $n$ in the permutation. How does $n$ separate the remaining $A - 1$ prefix maxima from the remaining $B - 1$ suffix maxima?
  - *Hint 2*: Look at the blocks starting at each prefix maximum to the left of $n$. Why is a block headed by its maximum element equivalent to a directed cycle, and why is the left-to-right order of blocks uniquely determined by their headers?
  - *Hint 3*: Partition $\{1, \dots, n-1\}$ into $A + B - 2$ cycles ($\left[\begin{matrix} n-1 \\ A+B-2 \end{matrix}\right]$ ways) and assign $A - 1$ cycles to the left of $n$ ($\binom{A+B-2}{A-1}$ ways). Compute $\left[\begin{matrix} n-1 \\ A+B-2 \end{matrix}\right] = [x^{A+B-2}] x^{\overline{n-1}}$ via FPS.

---

#### Problem 16: AtCoder AGC 005 F — Many Easy Problems
- **Judge & URL**: AtCoder Grand Contest 005 Problem F (`https://atcoder.jp/contests/agc005/tasks/agc005_f`)
- **Difficulty Tier**: `Intermediate` (Contribution to the Sum + Binomial Convolution via Reversed FPS)
- **Mathematical Statement & Constraints**:
  Given a tree $T$ on $N$ vertices, for each $K = 1, 2, \dots, N$, compute the sum over all $\binom{N}{K}$ vertex subsets $S$ of size $K$ of the size of the minimal subtree spanning $S$, modulo $924844033$ ($= 441 \times 2^{21} + 1$, primitive root $5$).
  - **Constraints**: $2 \le N \le 2 \times 10^5$.
  - **Target Complexity**: $O(N \log N)$ time, $O(N)$ space.
- **Diagnostic Signal & Modelling Bridge**:
  By linearity of expectation / contribution to the sum, a vertex $v$ does **not** belong to the minimal subtree spanning $S$ if and only if $S$ is entirely contained within a single connected component of $T \setminus \{v\}$. Letting $c_s$ be the total number of subtrees of size $s$ obtained across all $v$ when deleting $v$, we must evaluate:
  $$\text{Ans}_K = N \binom{N}{K} - \sum_{s=K}^{N-1} c_s \binom{s}{K} = N\binom{N}{K} - \frac{1}{K!} \sum_{s=K}^{N-1} (c_s s!) \frac{1}{(s - K)!}$$
  for all $K = 1, \dots, N$ simultaneously!
- **Complete Derivation & Solution Sketch**:
  1. Root the tree arbitrarily and run a single $O(N)$ DFS. Each edge $e = (u, p)$ splits the tree into two components of sizes $sz[u]$ and $N - sz[u]$. Increment $c_{sz[u]}$ and $c_{N - sz[u]}$ by $1$.
  2. We need $R_K = \sum_{s=K}^{N-1} (c_s s!) \cdot \frac{1}{(s - K)!}$ for all $K = 1, \dots, N$.
  3. Notice that the indices $(s)$ and $(s - K)$ have a **constant difference** $s - (s - K) = K$! By reversing the first array $A_{N - s} := c_s s!$ and setting $B_d := \frac{1}{d!}$, we get a standard Cauchy convolution:
     $$R_K = \sum_{s=K}^{N-1} A_{N - s} B_{s - K} = [x^{N - K}] \big(A(x) B(x)\big),$$
     computable in a single NTT multiplication modulo $924844033$!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Instead of finding the minimal spanning tree for each subset $S$, count for each vertex $v$ how many subsets $S$ of size $K$ do **not** include $v$ in their spanning subtree.
  - *Hint 2*: Expand $\sum_{s=K}^{N-1} c_s \binom{s}{K} = \frac{1}{K!} \sum_{s=K}^{N-1} (c_s s!) \frac{1}{(s-K)!}$. Why is this a difference-convolution in $s$ and $K$?
  - *Hint 3*: Reverse the polynomial $A(x) = \sum_{s=1}^{N-1} (c_s s!) x^{N-s}$ and multiply by $B(x) = \sum_{d=0}^{N-1} \frac{x^d}{d!}$ via NTT.

---

#### Problem 17: Luogu P4705 — 玩游戏 (Playing Games)
- **Judge & URL**: Luogu P4705 (`https://www.luogu.com.cn/problem/P4705`)
- **Difficulty Tier**: `Advanced` (EGF Binomial Expansion + Power Sums $\sum a_i^k$ via Logarithmic Derivative $\vartheta \ln$)
- **Mathematical Statement & Constraints**:
  Given two sequences $a_1, \dots, a_n$ and $b_1, \dots, b_m$, for every $t = 1, 2, \dots, K$, compute the expected value of $(a_i + b_j)^t$ when $i \in \{1, \dots, n\}$ and $j \in \{1, \dots, m\}$ are chosen uniformly at random, modulo $998244353$.
  - **Constraints**: $1 \le n, m, K \le 10^5$.
  - **Target Complexity**: $O((n + m + K) \log^2(n + m + K))$ time.
- **Diagnostic Signal & Modelling Bridge**:
  First, expand $(a_i + b_j)^t = t! \sum_{r=0}^t \frac{a_i^r}{r!} \cdot \frac{b_j^{t-r}}{(t-r)!}$ via the Binomial Theorem! Summing over all $(i, j)$ decouples $a$ and $b$ into the EGF product of their **power sums** $S_A(r) = \sum_{i=1}^n a_i^r$ and $S_B(s) = \sum_{j=1}^m b_j^s$!
  How do we compute the power sums $S_A(r) = \sum_{i=1}^n a_i^r$ for all $r = 1, \dots, K$ in $O(n \log^2 n + K \log K)$ time? Via the **logarithmic derivative** (Section 54.3):
  $$\sum_{r=1}^{\infty} \left(\sum_{i=1}^{n} a_i^r\right) x^r = \sum_{i=1}^{n} \frac{a_i x}{1 - a_i x} = -x \frac{d}{dx} \ln \prod_{i=1}^{n} (1 - a_i x)!$$
- **Complete Derivation & Solution Sketch**:
  1. Compute $P_A(x) = \prod_{i=1}^{n} (1 - a_i x)$ and $P_B(x) = \prod_{j=1}^{m} (1 - b_j x)$ in $O(n \log^2 n + m \log^2 m)$ time using divide-and-conquer NTT.
  2. Compute the power-sum OGFs via logarithmic differentiation:
     $$F_A(x) = n - \frac{x P_A'(x)}{P_A(x)} \pmod{x^{K+1}}, \qquad F_B(x) = m - \frac{x P_B'(x)}{P_B(x)} \pmod{x^{K+1}},$$
     so $[x^r]F_A(x) = \sum_{i=1}^n a_i^r$ and $[x^s]F_B(x) = \sum_{j=1}^m b_j^s$.
  3. Convert $F_A$ and $F_B$ into EGFs by dividing the $r$-th coefficient by $r!$:
     $$\widehat{F}_A(x) = \sum_{r=0}^{K} \frac{[x^r]F_A(x)}{r!} x^r, \qquad \widehat{F}_B(x) = \sum_{s=0}^{K} \frac{[x^s]F_B(x)}{s!} x^s.$$
  4. Multiply $\widehat{F}_A(x) \cdot \widehat{F}_B(x) \bmod x^{K+1}$, and for each $t = 1, \dots, K$, output $\frac{t!}{nm} [x^t] \big(\widehat{F}_A(x) \widehat{F}_B(x)\big) \bmod 998244353$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Use the binomial expansion of $(a_i + b_j)^t$ to rewrite $\sum_{i,j} (a_i + b_j)^t$ as an EGF convolution of power sums $S_A(r) = \sum_{i=1}^n a_i^r$ and $S_B(s) = \sum_{j=1}^m b_j^s$.
  - *Hint 2*: Observe that $\sum_{r=1}^{\infty} a_i^r x^r = \frac{a_i x}{1 - a_i x} = -x \frac{d}{dx} \ln(1 - a_i x)$. How can you sum this over all $i = 1, \dots, n$ simultaneously?
  - *Hint 3*: Compute $P_A(x) = \prod_{i=1}^n (1 - a_i x)$ via divide-and-conquer NTT, then extract $-x P_A'(x) P_A(x)^{-1} \bmod x^{K+1}$!

---

#### Problem 18: HDU 5279 — YJC plays minecraft
- **Judge & URL**: HDU 5279 (`https://acm.hdu.edu.cn/showproblem.php?pid=5279`)
- **Difficulty Tier**: `Advanced` (Labelled Cycle-of-Blocks Decomposition + EGF $\exp$ & $\operatorname{SEQ}$)
- **Mathematical Statement & Constraints**:
  You are given $N$ islands of sizes $a_1, a_2, \dots, a_N$ (where island $i$ has $a_i$ labelled vertices). Within each island $i$, you already have a connected graph; now you want to add edges between consecutive islands in a ring $1 - 2 - \dots - N - 1$ (at most 1 edge per adjacent pair of islands, and each chosen edge can connect any of the $a_i a_{i+1}$ vertex pairs) AND count the number of internal connected structures such that no cycle crosses islands except possibly the whole ring, modulo $998244353$.
  - **Constraints**: $\sum a_i \le 10^5$.
  - **Target Complexity**: $O((\sum a_i) \log(\sum a_i))$ time.
- **Diagnostic Signal & Modelling Bridge**:
  Contains two classic sub-problems:
  1. For each island of size $m = a_i$, count the number of connected simple graphs on $m$ labelled vertices via $\widehat{C}(x) = \ln \sum_{m\ge 0} 2^{\binom{m}{2}} \frac{x^m}{m!}$.
  2. For the ring of islands $1, \dots, N$, either every adjacent pair $(i, i+1)$ is connected (weighted by $\prod a_i^2$, minus overcounted trees), or we break the ring into a sequence of connected chains via $\operatorname{SEQ}$!
- **Complete Derivation & Solution Sketch**:
  1. Precompute the number of connected simple graphs $c_m$ for all $m \le \max(a_i)$ in $O(M \log M)$ time using $\widehat{C}(x) = \ln \widehat{G}(x)$.
  2. Within each island $i$, the internal configuration multiplier is $c_{a_i}$. Factor out $\prod_{i=1}^N c_{a_i}$.
  3. For the inter-island bridges on the cycle of length $N$, apply the transfer matrix / OGF over the chain to count valid edge selections where removing at least one bridge leaves a forest of chains.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Decouple the internal edges inside each island $i$ (of size $a_i$) from the bridges between adjacent islands.
  - *Hint 2*: Use $\widehat{C}(x) = \ln \sum_{m\ge 0} 2^{\binom{m}{2}} \frac{x^m}{m!}$ to precompute the number of connected simple graphs $c_{a_i}$ for each island.
  - *Hint 3*: Combine the inter-island choices around the cycle of length $N$ by conditioning on whether all $N$ bridges are present.

---

#### Problem 19: UOJ #450 / Luogu P5401 — [CTS2019] 珍珠 (Pearls)
- **Judge & URL**: Luogu P5401 (`https://www.luogu.com.cn/problem/P5401`) / UOJ #450 (`https://uoj.ac/problem/450`)
- **Difficulty Tier**: `Mastery` (Labelled EGF Parity Filtering $\frac{e^x - e^{-x}}{2}$ + Binomial Inversion + NTT Convolution)
- **Mathematical Statement & Constraints**:
  There are $n$ pearls to be chosen in sequence, where each pearl can be given one of $D$ distinct colors $\{1, 2, \dots, D\}$. A color sequence of length $n$ is valid if we can pair up pearls of the same color to form **at least $m$ pairs** (equivalently, if the number of colors that appear an **odd** number of times is at most $n - 2m$). Compute the number of valid color sequences of length $n$ modulo $998244353$.
  - **Constraints**: $1 \le n \le 10^9$, $1 \le m \le 10^9$, $1 \le D \le 10^5$.
  - **Target Complexity**: $O(D \log D)$ time, $O(D)$ space.
- **Diagnostic Signal & Modelling Bridge**:
  If $c_i$ is the number of times color $i$ appears ($\sum_{i=1}^D c_i = n$), the number of unpaired pearls is the number of colors with $c_i \equiv 1 \pmod 2$. Thus we need **at most $K := n - 2m$ colors to have odd frequency**!
  In the EGF world:
  - A color with **arbitrary** frequency has EGF $\sum_{c\ge 0} \frac{x^c}{c!} = e^x$.
  - A color forced to have **odd** frequency has EGF $\sum_{c \text{ odd}} \frac{x^c}{c!} = \sinh x = \frac{e^x - e^{-x}}{2}$!
  Because $n \le 10^9$ is huge while $D \le 10^5$ is small, expanding $(e^x - e^{-x})^k e^{(D-k)x}$ as a linear combination of $e^{a x}$ allows extracting $n! [x^n] e^{a x} = a^n$ in $O(1)$ per exponent!
- **Complete Derivation & Solution Sketch**:
  1. If $2m > n$, all $D^n$ sequences fail ($0$ ways); if $n - 2m \ge D$, all $D^n$ sequences succeed! Assume $0 \le K = n - 2m < D$.
  2. Define $g_k$ as the binomial-Counting sum where we distinguish $k$ colors and force them to have odd frequency, leaving the other $D - k$ colors arbitrary:
     $$g_k = \binom{D}{k} n! [x^n] \left(\frac{e^x - e^{-x}}{2}\right)^k e^{(D - k)x}.$$
  3. Expand $(e^x - e^{-x})^k e^{(D-k)x} = \sum_{j=0}^{k} (-1)^{k-j} \binom{k}{j} e^{(D - 2k + 2j)x}$. Since $n! [x^n] e^{a x} = a^n$:
     $$g_k = \frac{D!}{(D - k)! 2^k} \sum_{j=0}^{k} \frac{(-1)^{k-j}}{(k - j)!} \cdot \frac{(D - 2k + 2j)^n}{j!}?$$
     Look closely: $(D - 2k + 2j)^n$ depends only on $k - j$! Let $i = k - j$:
     $$g_k = \frac{D!}{(D - k)! 2^k} \sum_{i=0}^{k} \left(\frac{(-1)^i (D - 2i)^n}{i!}\right) \left(\frac{1}{(k - i)!}\right),$$
     which is a **single NTT convolution** to compute $g_0, g_1, \dots, g_D$ in $O(D \log D)$ time!
  4. Finally, let $f_r$ be the number of sequences with **exactly $r$** odd-frequency colors. Since $g_k = \sum_{r=k}^{D} \binom{r}{k} f_r$, **Binomial Inversion** gives $f_r = \sum_{k=r}^{D} (-1)^{k-r} \binom{k}{r} g_k$ (a second NTT convolution!), and we output $\sum_{r=0}^{K} f_r \bmod 998244353$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Translate "at least $m$ pairs can be formed" into an upper bound $K = n - 2m$ on the number of colors that appear an **odd** number of times.
  - *Hint 2*: What is the EGF of a color whose frequency is odd? How do you extract $n! [x^n] \left(\frac{e^x - e^{-x}}{2}\right)^k e^{(D-k)x}$ when $n = 10^9$?
  - *Hint 3*: Expand $(e^x - e^{-x})^k e^{(D-k)x}$ using the binomial theorem, substitute $i = k - j$ so $(D - 2i)^n$ depends only on $i$, compute all $g_k$ via NTT, and apply binomial inversion to recover $f_r$ for $r \le n - 2m$.

---

#### Problem 20: Luogu P5900 — 无标号无根树计数 (Unlabelled Unrooted Tree Enumeration)
- **Judge & URL**: Luogu P5900 (`https://www.luogu.com.cn/problem/P5900`) — Also Library Checker `counting_unlabeled_trees` / `maspy` FPS tutorial
- **Difficulty Tier**: `Mastery` (Self-Referential Euler Transform $T(x) = x \exp\sum \frac{T(x^j)}{j}$ + Otter's Dissimilarity Theorem)
- **Mathematical Statement & Constraints**:
  Find the number of **unlabelled unrooted trees** on $n$ vertices (up to graph isomorphism) modulo $998244353$.
  - **Constraints**: $1 \le n \le 2 \times 10^5$.
  - **Target Complexity**: $O(n \log n)$ via Newton's method on Euler transform or $O(n \log^2 n)$ via CDQ divide-and-conquer FFT.
- **Diagnostic Signal & Modelling Bridge**:
  Counting unlabelled **rooted** trees $T(x) = \sum_{n\ge 1} t_n x^n$ uses the self-referential Euler Transform $\mathcal{T} = \mathcal{Z} \times \operatorname{MSET}(\mathcal{T})$ (Section 54.3). How do we go from unlabelled **rooted** trees $T(x)$ to unlabelled **unrooted** trees $U(x)$ without overcounting symmetry orbits of vertices?
  By **Otter's Dissimilarity Characteristic Theorem (1948)**: in any unrooted tree $\tau$, the number of isomorphism orbits of vertices ($p^*$) minus the number of isomorphism orbits of undirected edges ($q^*$) plus the number of symmetric edges whose two endpoints are interchangeable ($s \in \{0, 1\}$) always equals $1$:
  $$p^* - q^* + s = 1!$$
- **Complete Derivation & Solution Sketch**:
  1. **Step 1 (Unlabelled Rooted Trees $T(x)$)**:
     Solve $T(x) = x \exp\!\left(\sum_{j=1}^{\infty} \frac{T(x^j)}{j}\right) \bmod x^{n+1}$.
     - Using Newton's method: when lifting precision from $m$ to $2m$, the higher-harmony sum $S_{\ge 2}(x) = \sum_{j=2}^{2m} \frac{T(x^j)}{j} \bmod x^{2m+1}$ depends only on coefficients of $T$ up to index $m$ (already known!). Thus we solve $T(x) = x e^{S_{\ge 2}(x)} e^{T(x)} \bmod x^{2m+1}$ via one step of Newton's method:
       $$T \leftarrow T - \frac{T - x e^{S_{\ge 2}(x) + T(x)}}{1 - T} \pmod{x^{2m+1}}$$
       in $O(n \log n)$ total time!
  2. **Step 2 (Otter's Dissimilarity Theorem for Unrooted Trees $U(x)$)**:
     Sum the identity $1 = p^*(\tau) - q^*(\tau) + s(\tau)$ over all unlabelled unrooted trees $\tau$ of size $n$:
     - $\sum_{\tau} p^*(\tau)$ counts unrooted trees with a distinguished vertex orbit = **unlabelled rooted trees** $T(x)$.
     - $\sum_{\tau} (q^*(\tau) - s(\tau))$ counts unrooted trees with a distinguished **asymmetric** edge (an unordered pair of **distinct** non-isomorphic rooted subtrees $\{\tau_1, \tau_2\}$), which has OGF $\frac{1}{2}\big(T(x)^2 - T(x^2)\big)$!
     - Therefore, the OGF of unlabelled unrooted trees is:
       $$U(x) = T(x) - \frac{1}{2}\Big(T(x)^2 - T(x^2)\Big)!$$
     Extracting $[x^n]U(x)$ after computing $T(x)$ takes $O(n \log n)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: First count unlabelled **rooted** trees $T(x) = x \operatorname{MSET}(\mathcal{T})(x) = x \exp\left(\sum_{j\ge 1} \frac{T(x^j)}{j}\right)$ using Newton's method or CDQ divide-and-conquer FFT.
  - *Hint 2*: In any unrooted tree $\tau$, compare the number of vertex isomorphism orbits $p^*(\tau)$ (ways to root $\tau$ at a vertex) with the number of edge isomorphism orbits $q^*(\tau)$ (ways to orient/bisect $\tau$ at an edge).
  - *Hint 3*: By Otter's Dissimilarity Theorem, $U(x) = T(x) - \frac{1}{2}(T(x)^2 - T(x^2))$. Evaluate $[x^n]U(x)$ directly from $T(x)$.

---

### 57.5 Rejected Template Problems Table (Strict Audit Exclusion Log)

In compliance with the Wave 1A Problem Audit standards, the following pure polynomial library verification problems were encountered during discovery and **explicitly rejected** from the pedagogical problem set:

| Judge & Problem ID | Title | Underlying Operation | Reason for Rejection |
| :--- | :--- | :--- | :--- |
| Library Checker `inv_of_formal_power_series` | Inv of Formal Power Series | $F(x)^{-1} \bmod x^N$ | Pure algebraic implementation template with zero combinatorial modelling. |
| Library Checker `log_of_formal_power_series` | Log of Formal Power Series | $\ln F(x) \bmod x^N$ | Pure algebraic implementation template; replaced by Luogu P4841 & ARC 105 F. |
| Library Checker `exp_of_formal_power_series` | Exp of Formal Power Series | $\exp F(x) \bmod x^N$ | Pure algebraic implementation template; replaced by Luogu P4389 & 51nod 1728. |
| Library Checker `sqrt_of_formal_power_series` | Sqrt of Formal Power Series | $\sqrt{F(x)} \bmod x^N$ | Pure algebraic implementation template; replaced by CF 438E & ARC 105 F. |
| Luogu P4238 | `【模板】多项式乘法逆` | $F(x)^{-1} \bmod x^N$ | Bare Luogu template problem asking directly for coefficients of $F^{-1}$. |
| Luogu P4725 | `【模板】多项式对数函数（多项式 ln）` | $\ln F(x) \bmod x^N$ | Bare Luogu template problem asking directly for coefficients of $\ln F$. |
| Luogu P4726 | `【模板】多项式指数函数（多项式 exp）` | $\exp F(x) \bmod x^N$ | Bare Luogu template problem asking directly for coefficients of $\exp F$. |
| Luogu P5205 | `【模板】多项式开根` | $\sqrt{F(x)} \bmod x^N$ | Bare Luogu template problem asking directly for coefficients of $\sqrt{F}$. |
| Library Checker `partition_function` | Partition Function | $\prod (1-x^k)^{-1} \bmod x^N$ | Pure sequence table output; replaced by Luogu P6189 (arbitrary modulus) & P5824. |

---

### 57.6 Master Wave 1A Multilingual Bibliography (`[EN]`, `[ZH]`, `[JA]`)

#### English (`[EN]`) Foundational Textbooks & Research Papers
1. **`[EN]` Philippe Flajolet and Robert Sedgewick**, *Analytic Combinatorics*, Cambridge University Press (2009). URL: `https://algo.inria.fr/flajolet/Publications/AnaCombi/anacombi.html`.
   - *Unique Insight*: Definitive treatise on the Unlabelled Symbolic Method ($\operatorname{SEQ}, \operatorname{MSET}, \operatorname{PSET}, \operatorname{CYC}$, Chapter I) and Labelled Symbolic Method ($\operatorname{SET} = \exp$, $\operatorname{CYC} = \ln\frac{1}{1-\cdot}$, Pointing $\Theta$, and the Boxed Product $\mathcal{A}^{\square} \star \mathcal{B}$, Chapter II).
2. **`[EN]` Herbert S. Wilf**, *generatingfunctionology* (3rd Edition), A K Peters / CRC Press (2006). URL: `https://www2.math.upenn.edu/~wilf/DownldGF.html`.
   - *Unique Insight*: Develops the formal operator rules (Rule 1–Rule 5 for shifting and $\vartheta = xD$), the Exponential Formula, and deck/hand card-modelling for $\exp/\ln$.
3. **`[EN]` Richard P. Stanley**, *Enumerative Combinatorics, Volume 1 & Volume 2*, Cambridge University Press (2011, 1999).
   - *Unique Insight*: Rigorous algebraic structure of $R[[x]]$ and $K((x))$, the Twelvefold Way (Vol. 1, Section 1.9), symmetric functions, and exponential structures (Vol. 2, Chapter 5).
4. **`[EN]` Ronald L. Graham, Donald E. Knuth, and Oren Patashnik**, *Concrete Mathematics: A Foundation for Computer Science* (2nd Edition), Addison-Wesley (1994).
   - *Unique Insight*: Chapter 7 provides concrete operator manipulations, binomial convolutions, and generating function scratchpads for recurrence solving.
5. **`[EN]` Richard Otter**, *"The Number of Trees"*, Annals of Mathematics, Vol. 49, No. 3, pp. 583–599 (1948).
   - *Unique Insight*: Proves the dissimilarity characteristic theorem $p^* - q^* + s = 1$ yielding $U(x) = T(x) - \frac{1}{2}(T(x)^2 - T(x^2))$ for unlabelled unrooted trees.

#### Chinese (`[ZH]`) National Team Papers (`国家集训队论文`), Wikis & Blogs
6. **`[ZH]` Jin Ce (金策)**, *《生成函数的运算与组合计数问题》* (*Operations on Generating Functions and Combinatorial Counting Problems*), 2015 Chinese IOI National Team Paper (`国家集训队2015论文集`), pp. 1–18 (2015).
   - *Unique Insight*: Connects Flajolet–Sedgewick's OGF/EGF operators to $O(N \log N)$ polynomial `inv`, `sqrt`, `ln`, `exp`, and ODE solvers in competitive programming.
7. **`[ZH]` Yang Maolong (杨懋龙)**, *《浅谈生成函数在掷骰子问题上的应用》* (*Applications of Generating Functions in Dice-Rolling Problems*), 2018 Chinese IOI National Team Paper (`国家集训队2018论文集`) (2018).
   - *Unique Insight*: Systematic derivation of expectation $F'(1)$ and variance $F''(1) + F'(1) - (F'(1))^2$ for stopping-time probability generating functions.
8. **`[ZH]` Lu Xin (吕欣 / Elegia)**, *《生成函数在组合计数中的应用》* & Luogu Blog Series on Operator Algebra and Polynomial Counting (2018–2021). URL: `https://www.luogu.com.cn/blog/Elegia/`.
   - *Unique Insight*: Develops the logarithmic-derivative Euler transform, harmonic sieve techniques, and ODE reductions for sparse power series.
9. **`[ZH]` OI-Wiki Collective**, *多项式与生成函数章节 (`math/poly/intro.md`, `ogf.md`, `egf.md`, `elementary-func.md`, `math/combinatorics/partition.md`)*. URL: `https://oi-wiki.org/math/poly/intro/`.
   - *Unique Insight*: Curates Chinese competitive programming terminology (`多项式 exp/ln 的组合意义`, `有标号定根技巧`) and worked derivations for 51nod 1728, CF 891E, and partition Durfee squares.
10. **`[ZH]` command_block**, *《多项式计数杂谈》* (*Miscellaneous Notes on Polynomial Counting*), Luogu Blog (2020). URL: `https://www.luogu.com.cn/blog/command-block/duo-xiang-shi-ji-shuo-za-tan`.
    - *Unique Insight*: Comprehensive problem-solving guide covering Euler transform (`付公主的背包`), Inverse Euler transform, Pólya tree counting (`烷基计数`), and EGF parity tricks (`CTS2019 珍珠`).

#### Japanese (`[JA]`) Competitive Programming Blogs & Libraries
11. **`[JA]` maspy (ますぴー)**, *形式的べき級数解説 (Formal Power Series Commentary)* & *分割数の母関数と五角数定理 (Generating Functions of Partition Numbers and Pentagonal Number Theorem)*, `maspypy.com` (2019–2023). URL: `https://maspypy.com/category/%e5%bd%a2%e5%bc%8f%e7%9a%84%e3%81%b9%e3%81%8d%e7%b4%9a%e6%95%b0`.
    - *Unique Insight*: Articulates the Japanese "FPS-First" philosophy (`DP を立てずに母関数を直接書く`), Pentagonal Number `inv` partition tables, and Durfee square decompositions.
12. **`[JA]` Nyaan**, *Competitive Programming Library — Formal Power Series & Famous Series (`fps/formal-power-series.hpp`, `fps/fps-famous-series.hpp`, `fps/differential-equation.hpp`)*, `nyaannyaan.github.io` (2020–2024). URL: `https://nyaannyaan.github.io/library/`.
    - *Unique Insight*: Unified C++ implementation of FPS operations, ODE solvers, and the Twelvefold Way (Stirling 1st/2nd kind, Bell, Bernoulli, Partition numbers).
13. **`[JA]` noshi91, tatyam, and opt (`opt-cp.com`)**, *競技プログラミングにおける形式的べき級数 (Formal Power Series in Competitive Programming)* & AtCoder ABC/ARC/AGC Editorials (2019–2024). URL: `https://opt-cp.com/fps-implementation/`.
    - *Unique Insight*: Documents log-sum-exp product bucketing, connected bipartite graph enumeration (`ARC 105 F`), and inclusion-exclusion via $\ln(1+x)$ (`ABC 236 Ex`).
