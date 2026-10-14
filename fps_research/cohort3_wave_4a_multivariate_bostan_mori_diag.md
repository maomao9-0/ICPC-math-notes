# Wave 4A Master Synthesis (Cohort 3 Reconciliation — Iterations 31–35 / 83–87): Multivariate Formal Power Series, Mixed OGF/EGF, Variable Decoupling & $\chi$-Graded Truncation, 1D/2D Bostan–Mori, Rational Diagonals, and MacMahon's Master Theorem

> **Cohort 3 Role**: Cross-Cohort Reconciliation, Blind-Spot Audit, Gap-Hunting, and Definitive Master Archive
> **Compiled Sources**:
> 1. Cohort 1 (`fps_research/iter_31_to_35_multivariate_bostan_mori_diag.md`, 1,474 lines)
> 2. Cohort 2 (`fps_research/cohort2_iter_83_to_87_multivariate_bostan_mori_diag.md`, 1,650 lines)
> 3. Cohort 3 Gap-Hunting Additions (Mixed OGF/EGF Symbolic Calculus & PDE Bridge; MacMahon's Master Theorem, Foata's Bijection, Permanent–Determinant Duality, and I. J. Good's Proof of Dixon's Identity)
> **Pedagogical Standard**: **Zero Magic Steps** — Every ring inclusion, primary-variable flip, monomial decoupling, $\chi$-graded Kronecker carry filter, parity halving, small-root residue separation, and determinant extraction is preceded by a **Diagnostic Signal** and a **Reverse-Engineering Scratchpad**, followed by step-by-step verbally annotated derivations, hand-checkable $n \le 4$ traces, and explicit failure modes.

---

## Section 1: Cross-Cohort Blind-Spot & Coverage Reconciliation Matrix

### 1.1 High-Level Architectural Comparison: Cohort 1 vs. Cohort 2 vs. Cohort 3

Both Cohort 1 and Cohort 2 independently produced high-rigor monographs (~140 KB each), but each cohort uncovered critical algebraic nuances, algorithmic optimizations, failure modes, and contest problems that the other missed. Furthermore, cross-referencing both cohorts against the Wave 4A specification revealed two theoretical pillars (**Mixed OGF/EGF Calculus** and **MacMahon's Master Theorem**) that neither cohort treated in a dedicated theoretical section.

```mermaid
flowchart TD
    subgraph C1["Cohort 1 Unique Strengths (Iter 31–35)"]
        C1A["Explicit Homomorphism Validity of ev_{y=y_0}<br/>& Shifted Root-of-Unity Fix y_r = c * omega^r"]
        C1B["Characteristic p = 2 Collapse Analysis<br/>in 1D Bostan-Mori (Freshman's Dream vs. /2 Failure)"]
        C1C["9 Unique Contest Problems:<br/>ARC154F, CF1553I, CF1336E2, P5406,<br/>yuki1783, ABC279Ex, P5487, ABC240G, CF1264D2"]
    end

    subgraph C2["Cohort 2 Unique Strengths (Iter 83–87)"]
        C2A["Exact Intersection K[x,y] ⊂≠ K[y][[x]] ∩ K[x][[y]]<br/>& Non-Associativity Disaster in K[[z, z^{-1}]]"]
        C2B["MSB-First Graeffe Bostan-Mori, maspypy Monic y-Reversal,<br/>& Regime D Bostan-Christol-Dumas mod p"]
        C2C["Full Reverse Furstenberg Proof (Algebraic -> Rational Diag),<br/>Two-Boundary Kernel Method & Full C++20 Blueprints"]
        C2D["9 Unique Contest Problems:<br/>Typical90 #065, CF1117D, CF960G, P5339,<br/>AGC013E, ABC387G, CF1349F2, QOJ4815, BCD mod p"]
    end

    subgraph C3["Cohort 3 Gap-Hunting Additions"]
        C3A["Mixed OGF/EGF ('Exponential-Ordinary') Calculus:<br/>SET_y, SEQ_y, CYC_y & Stirling/Eulerian Triad"]
        C3B["MacMahon's Master Theorem (MMT):<br/>[x^m] prod (Ax)_i^{m_i} = [x^m] det(I - XA)^{-1},<br/>Foata Bijection, Permanent Duality & Dixon's Identity"]
    end

    C1 --> M["Cohort 3 Unified Master Archive<br/>(Zero Magic Steps + 28 Curated Problems)"]
    C2 --> M
    C3 --> M
```

### 1.2 Detailed Blind-Spot & Discrepancy Audit Table

| Sub-Topic / Iteration | Found by Cohort 1 ONLY (Missed by Cohort 2) | Found by Cohort 2 ONLY (Missed by Cohort 1) | Subtle Discrepancies Resolved & Cohort 3 Gap-Hunting Additions |
| :--- | :--- | :--- | :--- |
| **Iter 31 / 83: Multivariate FPS Rings & Mixed OGF/EGF** | • **Shifted Evaluation Fix**: Proved that $\operatorname{ev}_{y=y_0}: K[y][[x]] \to K[[x]]$ fails in $K[[y]][[x]]$, and showed how to fix vanishing denominators $Q(0, \omega^r) = 0$ via scalar shift $y_r = c \cdot \omega^r$.<br/>• Full $4 \times 4$ row-vs-column trace of trinomial GF $\frac{1}{1-x(1+y+y^2)}$ comparing $K[y][[x]]$ vs. $K[[x]][[y]]$. | • **Iterated Laurent Ring $K((z))[[t]]$ in the Ring Hierarchy**: Proved unit theorem $C_0(z) \neq 0$ in $K((z))[[t]]$ and showed $K((x))[[y]] \neq K((y))[[x]]$ via disjoint supports of $\frac{1}{x-y}$.<br/>• Proved the **Secondary-Variable Degree Growth Lemma** $\deg_y F_n(y) \le c n$ by induction. | • **Algebraic Discrepancy Fixed**: Cohort 1 wrote $K[y][[x]] \cap K[x][[y]] = K[x,y]$ in passing; Cohort 2 proved $K[x,y] \subsetneq K[y][[x]] \cap K[x][[y]]$ using the counterexample $D(x,y) = \frac{1}{1-xy} = \sum_{n \ge 0} x^n y^n$ (where $[x^n]D = y^n \in K[y]$ and $[y^k]D = x^k \in K[x]$, yet $D \notin K[x,y]$).<br/>• **Cohort 3 Addition**: Full section on **Mixed OGF/EGF ("Exponential-Ordinary" GFs)** $\sum_{n,k} f_{n,k} \frac{x^n}{n!} y^k$, bivariate $\mathsf{SET}_y / \mathsf{SEQ}_y / \mathsf{CYC}_y$, Stirling/Eulerian GFs, and PDE bridges. |
| **Iter 32 / 84: Variable Decoupling, 2D FFT, Twisted Kronecker & Graeffe** | • **Hybrid Cyclic + Truncated Multivariate Convolution**: Demonstrated combining radix-$10$ multidimensional DFT on cyclic variables $\bmod (z_r^{10}-1)$ with twisted Kronecker FPS $\operatorname{pow}$ on truncated variables $\bmod z_r^{10}$ (via `yukicoder 1783`). | • **Partial-Derivative + 1D Boundary Method**: Derived $\partial_x \ln F = (\partial_x F) F^{-1}$ with integration constant $[x^0]\ln F(x,y) = \ln F(0,y) \bmod y^M$, which works even when $p \le N = n_1 n_2$ as long as $\max(n_1,n_2) < p$.<br/>• Complete C++20 `MultivariateFPS` struct implementing $\chi(i)$ and $\mathfrak{D}$. | • Unified both cohorts' derivations of van der Hoeven (2002) / Elegia / EntropyIncreaser's $\chi(I) = \sum_{r=1}^{d-1} \lfloor I / (n_1 \cdots n_r) \rfloor \bmod d$ carry-detector and the total-index radial Euler derivation $\mathfrak{D} = \sum_{r=1}^d (n_1 \cdots n_{r-1}) x_r \partial_{x_r}$. |
| **Iter 33 / 85: 1D & 2D Bostan–Mori & Graeffe Root-Squaring** | • **Characteristic $p = 2$ Edge Case**: Analyzed how $Q(-x) = Q(x)$ in $\mathbb{F}_2[x]$ satisfies $Q(x)^2 = Q(x^2)$ automatically, while NTT-domain formulas dividing by $2$ fail.<br/>• Explicit Taylor-shift preprocessing $F(y) \gets F(y + g_0)$ when composing $F(G(x))$ with $[x^0]G(x) = g_0 \neq 0$. | • **MSB-First Bostan–Mori & Graeffe Root-Squaring**: Connected $V_t(x) = \mathcal{E}(V_{t-1}(x)V_{t-1}(-x))$ to Graeffe's method (squaring roots at each step) and Schönhage's partial fraction identity.<br/>• **`maspypy`'s $y$-Reversed Monic Formulation**: $Q_0(x,y) = y - f(x)$ keeps $Q_t(x,y) = y^{2^t} + \tilde{Q}_t(x,y)$ with $\deg_y \tilde{Q}_t < 2^t$, avoiding $2^t+1$ FFT length doubling.<br/>• **Regime D (Bostan–Christol–Dumas $\bmod p$)**: Frobenius reduction $Q(x,y)^p \equiv Q(x^p, y^p) \pmod p$.<br/>• Full C++20 implementations of `bostan_mori_ntt`, `power_projection`, and `fps_composition`. | • Synthesized all **4 Regimes of 2D Bostan–Mori** (Regime A: Truncated $K[y]/(y^{K+1})$; Regime B: Root-of-unity $y$-Evaluation–Interpolation; Regime C: Kinoshita–Li $x$-halving / $y$-doubling; Regime D: Bostan–Christol–Dumas Frobenius $\bmod p$) alongside complete C++20 code and small-$N$ traces. |
| **Iter 34 / 86: Constant Term $\operatorname{CT}_z$, Rational Diagonals & MMT** | • **Shifted Diagonal Theorem**: Proved $[z^s] F(z, t/z) = \operatorname{CT}_z(z^{-s} F(z, t/z)) = \operatorname{res}_z(z^{-s-1} F(z, t/z))$ for general off-diagonal shifts $s \in \mathbb{Z}$.<br/>• Derived the explicit 3-term P-recursion for generalized Delannoy walks $n h_n = (2n-1)(c+2ab) h_{n-1} - (n-1)c^2 h_{n-2}$.<br/>• Discussed Lipshitz's theorem for $d \ge 3$ variables (transcendental but D-finite). | • **Non-Associativity Trap in $K[[z, z^{-1}]]$**: Proved why $(1-z)\sum_{k \in \mathbb{Z}} z^k = 0$ breaks associativity and why expanding across the unit circle corrupts $[z^0]$.<br/>• **Reverse Furstenberg Theorem**: Proved $A(t) = \operatorname{Diag}_{x,y}\left(\frac{y^2 \partial_y E(xy,y)}{E(xy,y)}\right)$ for any algebraic series.<br/>• **Two-Boundary Kernel Method** in $K((u))[[t]]$ and **Formal Residue Integration by Parts** for CF 755G. | • **Cohort 3 Addition**: Complete section on **MacMahon's Master Theorem (MMT)** $[x_1^{m_1} \cdots x_d^{m_d}] \prod_{i=1}^d (A \mathbf{x})_i^{m_i} = [x_1^{m_1} \cdots x_d^{m_d}] \frac{1}{\det(I - X A)}$, proved both algebraically (via multivariate Jacobi residue change of variables) and bijectively (Foata's cycle-decomposition), plus Permanent vs. Determinant complexity duality and I. J. Good's MMT proof of **Dixon's Identity**. |
| **Iter 35 / 87: Curated Problem Bank, Rejected Templates & `[EN]`/`[ZH]`/`[JA]` Audit** | • 18 problems (9 unique to Cohort 1).<br/>• Rejected `Luogu P7439` and `multivariate_convolution`.<br/>• Cited `noshi91` Hatena blog on Power Projection. | • 18 problems (9 unique to Cohort 2).<br/>• Rejected `multipoint_evaluation` and `Yukicoder 2677`.<br/>• Cited `ryuhe1` (Ryuhei Mori) Qiita article, `Bostan-Christol-Dumas (2016)`, `Furstenberg (1967)`, and `NaCly_Fish` / `zzq`. | • Merged and deduplicated all **27 unique contest problems** from Cohorts 1 & 2 + **1 new MMT/Dixon problem** = **28 fully derived non-template problems**, 8 rejected templates, and 16 multilingual citations (`[EN]`, `[ZH]`, `[JA]`). |

---

## Section 2 (Iteration 31 / 83): Multivariate Formal Power Series Rings, Primary-Variable Selection, and Mixed OGF/EGF Calculus

### 2.1 The Five-Ring Bivariate Hierarchy & Strict Inclusions

Let $K$ be a commutative ring with identity (in competitive programming, typically a prime field $\mathbb{F}_p$ such as $\mathbb{F}_{998244353}$ or $\mathbb{Q}$). When a two-parameter sequence $(f_{n,k})$ is encoded into a formal series in two indeterminates $(x, y)$, the expression $\sum_{n,k} f_{n,k} x^n y^k$ is **algebraically ambiguous until we specify the ambient ring**. Unlike univariate series—which form a single linear chain $K[x] \subsetneq K[[x]] \subsetneq K((x))$—bivariate series inhabit five distinct rings with fundamentally different finiteness and invertibility rules:

```mermaid
flowchart BT
    P["K[x, y] ≅ K[y][x] ≅ K[x][y]<br/>Bivariate Polynomials<br/>(Finite support in both x and y)"] --> INT["K[y][[x]] ∩ K[x][[y]]<br/>Bi-Finite Slice Series<br/>(e.g., 1/(1 - xy) = sum x^n y^n)"]
    INT --> YX["K[y][[x]]<br/>FPS in x over Polynomial Ring K[y]<br/>(Every [x^n]F(x,y) is a finite polynomial in K[y])"]
    INT --> XY["K[x][[y]]<br/>FPS in y over Polynomial Ring K[x]<br/>(Every [y^k]F(x,y) is a finite polynomial in K[x])"]
    YX --> XXYY["K[[x, y]] ≅ K[[y]][[x]] ≅ K[[x]][[y]]<br/>Full First-Quadrant Bivariate FPS<br/>(Arbitrary infinite support in n >= 0, k >= 0)"]
    XY --> XXYY
    XXYY --> LAUR["K((z))[[t]]<br/>Iterated Formal Laurent Series<br/>(For each t^n, z-exponents are bounded below: k >= v_n)"]
```

| Ring Notation | Element Structure $F(x,y)$ | Support Constraint on $(n,k)$ with $f_{n,k} \neq 0$ | Unit Condition $F \in R^\times$ (for domain/field $K$) | Typical Competitive Programming Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **$K[x,y]$** | $\sum_{n=0}^N \sum_{k=0}^M f_{n,k} x^n y^k$ | $n \ge 0, k \ge 0$; **finitely many** $(n,k)$ in total | $F(x,y) = f_{0,0} \in K^\times$ | Finite 2D knapsack, polynomial numerators & denominators |
| **$K[y][[x]]$** | $\sum_{n=0}^\infty P_n(y) x^n,\; P_n(y) \in K[y]$ | $n \ge 0, k \ge 0$; **for each fixed $n$, only finitely many $k$** ($\deg_y P_n < \infty$) | $P_0(y) \in K[y]^\times \iff P_0(y) = f_{0,0} \in K^\times$ (constant in $y$!) | DP over size $n$ where auxiliary statistic $k \le c \cdot n$; allows exact un-truncated evaluation $y = y_0$ |
| **$K[x][[y]]$** | $\sum_{k=0}^\infty Q_k(x) y^k,\; Q_k(x) \in K[x]$ | $n \ge 0, k \ge 0$; **for each fixed $k$, only finitely many $n$** ($\deg_x Q_k < \infty$) | $Q_0(x) \in K[x]^\times \iff Q_0(x) = f_{0,0} \in K^\times$ (constant in $x$!) | Counting structures with a fixed number $k$ of special components where size $n$ is bounded by $k$ |
| **$K[[x,y]]$** | $\sum_{n=0}^\infty \sum_{k=0}^\infty f_{n,k} x^n y^k$ | $n \ge 0, k \ge 0$ (arbitrary infinite support in first quadrant) | $f_{0,0} = F(0,0) \in K^\times$ | General bivariate OGF/EGF; canonically isomorphic to $K[[y]][[x]]$ and $K[[x]][[y]]$ |
| **$(K[y]/(y^{K+1}))[[x]]$** | $\sum_{n=0}^\infty \bar{P}_n(y) x^n,\; \deg_y \bar{P}_n \le K$ | $n \ge 0, 0 \le k \le K$ | $[y^0] \bar{P}_0(y) = f_{0,0} \in K^\times$ (since $y^{K+1} = 0$ is nilpotent) | Truncated bivariate Bostan–Mori when $N \le 10^{18}, K \le 10^5$ |
| **$K((z))[[t]]$** | $\sum_{n=0}^\infty L_n(z) t^n,\; L_n(z) \in K((z))$ | $n \ge 0$; **for each fixed $n$, $k \ge v_n > -\infty$ is bounded below** | $L_0(z) \in K((z))^\times \iff L_0(z) \neq 0$ (when $K$ is a field) | 1D random walks in time $t$ and position $z \in \mathbb{Z}$; diagonal extraction $\operatorname{Diag}_{x,y} F = \operatorname{CT}_z F(z, t/z)$ |

#### Strictness of the Ring Inclusions (Reconciling Cohort 1 & Cohort 2)
1. **$K[x,y] \subsetneq K[y][[x]] \cap K[x][[y]]$**:
   Consider the diagonal geometric series
   $$D(x,y) = \frac{1}{1 - xy} = \sum_{n=0}^{\infty} x^n y^n.$$
   For each fixed $n$, $[x^n] D(x,y) = y^n \in K[y]$ has finite degree $n$; for each fixed $k$, $[y^k] D(x,y) = x^k \in K[x]$ has finite degree $k$. Thus $D(x,y) \in K[y][[x]] \cap K[x][[y]]$, yet $D(x,y) \notin K[x,y]$. (However, if a series $F(x,y)$ has uniformly bounded $y$-degree $\deg_y([x^n]F) \le M$ for all $n$ AND uniformly bounded $x$-degree $\deg_x([y^k]F) \le N$ for all $k$, then $F \in K[x,y]$.)
2. **$K[y][[x]] \setminus K[x][[y]]$ vs. $K[x][[y]] \setminus K[y][[x]]$**:
   - $F_1(x,y) = \frac{1}{1 - x(1+y)} = \sum_{n=0}^\infty (1+y)^n x^n$ lies in $K[y][[x]]$, but $[y^0] F_1(x,y) = \sum_{n=0}^\infty x^n = \frac{1}{1-x} \notin K[x]$, so $F_1 \notin K[x][[y]]$.
   - Symmetrically, $F_2(x,y) = \frac{1}{1 - y(1+x)} \in K[x][[y]] \setminus K[y][[x]]$.
   - Finally, $F_3(x,y) = \frac{1}{1 - x - y} = \sum_{n,k \ge 0} \binom{n+k}{n} x^n y^k$ has $[x^0] F_3 = \frac{1}{1-y} \notin K[y]$ and $[y^0] F_3 = \frac{1}{1-x} \notin K[x]$, so $F_3 \in K[[x,y]] \setminus (K[y][[x]] \cup K[x][[y]])$.

---

### 2.2 Theorem on Units, Rational Membership & Secondary-Variable Degree Growth

#### Theorem 2.1 (Characterization of Units & Rational Ring Membership)
Let $K$ be an integral domain (or field $\mathbb{F}_p$).
1. **In $K[[x,y]]$**: $F(x,y) = \sum_{n,k \ge 0} f_{n,k} x^n y^k$ is a unit in $K[[x,y]]$ if and only if $f_{0,0} \in K^\times$.
2. **In $K[y][[x]]$**: $F(x,y) = \sum_{n=0}^\infty P_n(y) x^n$ is a unit in $K[y][[x]]$ if and only if $P_0(y) \in K[y]^\times \iff P_0(y) = f_{0,0} \in K^\times$ is a **non-zero constant polynomial** independent of $y$.
   - *Rational Criterion*: For $P, Q \in K[x,y]$ with $Q(0,0) \in K^\times$, the rational series $\frac{P(x,y)}{Q(x,y)}$ belongs to $K[y][[x]]$ (when coprime) **if and only if** $Q(0, y) \in K^\times$ (setting $x = 0$ eliminates all occurrences of $y$ in the denominator).
3. **In $(K[y]/(y^{K+1}))[[x]]$**: $F(x,y) = \sum_{n=0}^\infty \bar{P}_n(y) x^n$ is a unit if and only if $[y^0] \bar{P}_0(y) = f_{0,0} \in K^\times$.
4. **In $K((z))[[t]]$**: Over a field $K$, $F(z,t) = \sum_{n=0}^\infty L_n(z) t^n$ is a unit in $K((z))[[t]]$ if and only if the leading $t^0$-coefficient $L_0(z)$ is not the zero Laurent series ($L_0(z) \neq 0$).
5. **Secondary-Variable Degree Growth Lemma**: If $Q(x,y) = 1 - \sum_{n=1}^\infty Q_n(y) x^n \in K[y][[x]]$ satisfies $\deg_y Q_n(y) \le c \cdot n$ for all $n \ge 1$, then $F(x,y) = Q(x,y)^{-1} = \sum_{n=0}^\infty F_n(y) x^n \in K[y][[x]]$ satisfies $\deg_y F_n(y) \le c \cdot n$ for all $n \ge 0$.

#### Proof with Verbal Annotations
- **Why (1)–(3) hold**: For any commutative ring $R$, a formal power series $\sum_{n \ge 0} r_n x^n \in R[[x]]$ is invertible iff $r_0 \in R^\times$ (by recursive extraction $g_n = -r_0^{-1} \sum_{i=1}^n r_i g_{n-i}$).
  - For $R = K[[y]]$, $P_0(y) \in K[[y]]^\times \iff f_{0,0} \in K^\times$.
  - For $R = K[y]$ (over an integral domain $K$), $\deg(A B) = \deg A + \deg B$ forces the only units of $K[y]$ to be degree-$0$ constants $K^\times$. Thus $1 - y$ is **not** invertible in $K[y]$, so $(1 - y - x)^{-1} \notin K[y][[x]]$.
  - Passing to the quotient ring $R = K[y]/(y^{K+1})$ makes $y$ nilpotent ($y^{K+1} = 0$), so any $P_0(y) = f_{0,0}(1 - y A(y))$ with $f_{0,0} \in K^\times$ has the finite polynomial inverse $f_{0,0}^{-1} \sum_{m=0}^K y^m A(y)^m \bmod y^{K+1}$.
- **Why (4) holds**: When $K$ is a field, $R = K((z))$ is itself a field: any non-zero $L_0(z) = c_v z^v (1 + d_1 z + \cdots)$ with $c_v \neq 0$ and $v \in \mathbb{Z}$ has inverse $c_v^{-1} z^{-v} (1 + d_1 z + \cdots)^{-1} \in K((z))$.
- **Why (5) holds**: By induction on $n$ in $F_n(y) = \sum_{i=1}^n Q_i(y) F_{n-i}(y)$, each summand has $y$-degree at most $c i + c(n - i) = c n$. $\blacksquare$

---

### 2.3 The Primary-Variable Selection Rule (`主元法`, Zhǔyuánfǎ)

#### Diagnostic Signals
When confronted with a bivariate problem in $(x, y)$, use these three diagnostic signals to choose which variable sits on the outside of the ring brackets:
1. **Combinatorial / Algebraic Finiteness Signal**: If an object of $x$-size $n$ has $y$-statistic bounded by $0 \le k \le c \cdot n$, then $F(x,y) \in K[y][[x]]$. You may safely evaluate $y$ at arbitrary field elements $y_0 \in K$ because $\operatorname{ev}_{y=y_0}: K[y][[x]] \to K[[x]]$ only sums finitely many terms per $x^n$.
2. **Differential / Algebraic ODE Signal**: If the functional equation differentiates or shifts with respect to $x$ while $y$ acts as a passive scalar marker, make $x$ the outer variable (or flip roles if solving a quadratic in $x$ yields a clean D-finite ODE in $y$, as in **CF 755G**!).
3. **Constraint Asymmetry Signal ($N$ vs. $K$)**:
   - **Regime $N \le 10^{18}, K \le 10^5$**: Either work in $(K[y]/(y^{K+1}))[[x]]$ via $O(\log N)$ binary exponentiation / Bostan–Mori in $x$, **or** flip to $K[[x]][[y]]$ if $[y^k] F(x,y)$ is a compact rational function of $x$ whose $[x^N]$ coefficient can be extracted at the very end in $O(K)$ time!
   - **Regime $N \le 10^5, K \le 10$**: View $F \in (K[[x]]/(x^{N+1}))[y]/(y^{K+1})$, requiring only $O(K^2)$ 1D FPS operations of length $N$.

#### Reverse-Engineering Scratchpad: Discovering the Ring Flip on Trinomial Walks
Consider $F(x, y) = \frac{1}{1 - x(1 + y + y^2)}$, counting $n$-step walks from $(0,0)$ to $(n,k)$ with steps $(1,0), (1,1), (1,2)$.

```
[Scratchpad: Comparing K[y][[x]] vs. K[[x]][[y]] for F(x, y) = 1 / (1 - x(1 + y + y^2))]

Attempt 1 (Primary Variable x, working in K[y][[x]]):
- Denominator Q(x,y) = 1 - (1 + y + y^2) x has [x^0] Q(0,y) = 1 \in K[y]^\times.
- Geometric expansion in x stays inside K[y][[x]]:
    F(x, y) = \sum_{n=0}^{\infty} (1 + y + y^2)^n x^n.
- Best when n is small or we want all y^k for a fixed n.

Attempt 2 (Primary Variable y, hoping for K[x][[y]]):
- Group denominator by powers of y:
    Q(x, y) = (1 - x) - x y(1 + y).
- Constant term in y is [y^0] Q(x, 0) = 1 - x \notin K[x]^\times!
- However, 1 - x IS a unit in K[[x]]! Factoring out (1 - x) in K[[x]][[y]] gives:
    F(x, y) = \frac{1}{1 - x} \cdot \frac{1}{1 - \frac{x}{1 - x} y(1 + y)}
            = \sum_{j=0}^{\infty} \frac{x^j}{(1 - x)^{j+1}} y^j (1 + y)^j
            = \sum_{k=0}^{\infty} y^k \left( \sum_{j=\lceil k/2 \rceil}^{k} \binom{j}{k - j} \frac{x^j}{(1 - x)^{j+1}} \right).
- Look at the payoff: even though [y^k] F(x,y) \in K[[x]] is an infinite series in x,
  extracting [x^N] from x^j / (1 - x)^{j+1} is just \binom{N}{j}!
  So if N = 10^{18} and k = 10^5, the K[[x]][[y]] expansion gives [x^N y^k] F(x,y) in O(k) time:
    [x^N y^k] F(x, y) = \sum_{j=\lceil k/2 \rceil}^{\min(N, k)} \binom{j}{k - j} \binom{N}{j}!
```

#### Hand-Checkable $4 \times 4$ Trace ($n, k \le 3$)

| $n \backslash k$ | $y^0$ | $y^1$ | $y^2$ | $y^3$ | Row Polynomial $[x^n] F(x,y) \in K[y]$ |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **$x^0$** | $1$ | $0$ | $0$ | $0$ | $1$ (deg $0$) |
| **$x^1$** | $1$ | $1$ | $1$ | $0$ | $1 + y + y^2$ (deg $2$) |
| **$x^2$** | $1$ | $2$ | $3$ | $2$ | $1 + 2y + 3y^2 + 2y^3 + y^4$ (deg $4$) |
| **$x^3$** | $1$ | $3$ | $6$ | $7$ | $1 + 3y + 6y^2 + 7y^3 + 6y^4 + 3y^5 + y^6$ (deg $6$) |
| **Col Series $[y^k]F \in K[[x]]$** | $\frac{1}{1-x}$ | $\frac{x}{(1-x)^2}$ | $\frac{x}{(1-x)^3}$ | $\frac{2x^2-x^3}{(1-x)^4}$ | *Rational in $x$, infinite series in $K[[x]]$!* |

---

### 2.4 Mixed OGF/EGF ("Exponential-Ordinary" Generating Functions) & Bivariate Symbolic Calculus (Cohort 3 Gap-Hunting Addition)

#### 1. Concrete Combinatorial / Algebraic Object
In labeled combinatorial enumeration, we frequently count structures of **labeled size $n$** (atoms $\{1, 2, \dots, n\}$) refined by an **unlabeled auxiliary statistic $k$** (such as number of connected components, cycles, blocks, ascents, or leaves). The natural algebraic object encoding $(f_{n,k})_{n,k \ge 0}$ is a **Mixed Exponential-Ordinary Generating Function (EOGF)**:
$$F(x, y) = \sum_{n=0}^{\infty} \sum_{k=0}^{\infty} f_{n,k} \frac{x^n}{n!} y^k = \sum_{n=0}^{\infty} P_n(y) \frac{x^n}{n!} \in K[y][[x]],$$
where $x$ is **exponential** (dividing by $n!$ to handle relabeling in $\binom{n}{i}$ ways) and $y$ is **ordinary** (multiplying $y^{k_1} \cdot y^{k_2} = y^{k_1 + k_2}$ to add additive statistics).

#### 2. The Diagnostic Signal
Use a Mixed OGF/EGF $F(x,y) = \sum_{n,k} f_{n,k} \frac{x^n}{n!} y^k$ whenever:
- Combining two substructures of sizes $(n_1, n_2)$ and statistics $(k_1, k_2)$ requires **binomial relabeling** $\binom{n_1 + n_2}{n_1}$ on the $x$-index and **ordinary addition** $k_1 + k_2$ on the $y$-index:
  $$h_{n, k} = \sum_{n_1 + n_2 = n} \binom{n}{n_1} \sum_{k_1 + k_2 = k} f_{n_1, k_1} g_{n_2, k_2} \iff H(x, y) = F(x, y) \cdot G(x, y).$$

#### 3. Reverse-Engineering Scratchpad: Marking Components in the Symbolic Method

```
[Scratchpad: How Marking With y Transforms 1D EGF Constructors into 2D Mixed GFs]

Suppose A(x) = \sum_{n=1}^\infty a_n \frac{x^n}{n!} (with a_0 = 0) is the EGF of a connected labeled building block \mathcal{A}.
We want to build composite objects \mathcal{B} out of k building blocks from \mathcal{A}, and track k with y^k!
In a single assembly of k blocks:
- Each block contributes A(x) * y (since it adds +1 to the block count tracked by y).
- Therefore, replacing A(x) by y * A(x) inside any 1D labeled constructor immediately gives the Mixed EOGF!
  1. Ordered sequence of k blocks (\mathsf{SEQ}):
       \sum_{k=0}^\infty k! \frac{(y A(x))^k}{k!} = \frac{1}{1 - y A(x)}.
  2. Unordered set of k blocks (\mathsf{SET}):
       \sum_{k=0}^\infty \frac{(y A(x))^k}{k!} = \exp\big(y A(x)\big).
  3. Directed cycle of k blocks (\mathsf{CYC}):
       \sum_{k=1}^\infty \frac{(k-1)!}{k!} (y A(x))^k = \ln\left(\frac{1}{1 - y A(x)}\right).
```

#### 4. Step-by-Step Derivation of the Canonical Mixed OGF/EGF Triad & PDE Operators

1. **Differential-Algebraic Dictionary on $F(x, y) = \sum_{n,k} f_{n,k} \frac{x^n}{n!} y^k$**:
   $$\begin{aligned}
   \frac{\partial}{\partial x} F(x, y) &= \sum_{n, k \ge 0} f_{n+1, k} \frac{x^n}{n!} y^k && \text{(Shifts labeled size } n+1 \to n\text{)}, \\
   x \frac{\partial}{\partial x} F(x, y) &= \sum_{n, k \ge 0} n \, f_{n, k} \frac{x^n}{n!} y^k && \text{(Multiplies by labeled size } n\text{)}, \\
   y \frac{\partial}{\partial y} F(x, y) &= \sum_{n, k \ge 0} k \, f_{n, k} \frac{x^n}{n!} y^k && \text{(Multiplies by statistic } k\text{; sets } k=1 \implies \text{expected value }\mathbb{E}[k]\text{!)}.
   \end{aligned}$$

2. **The Canonical Triad of Mixed Bivariate Generating Functions**:

| Combinatorial Numbers $T_{n,k}$ | Recurrence Relation | Building Block $\mathcal{A}$ & Constructor | Closed-Form Mixed OGF/EGF $\sum_{n,k \ge 0} T_{n,k} \frac{x^n}{n!} y^k$ |
| :--- | :--- | :--- | :--- |
| **Unsigned Stirling 1st Kind $\left[\begin{smallmatrix} n \\ k \end{smallmatrix}\right]$**<br/>($n$ elements into $k$ disjoint cycles) | $\left[\begin{smallmatrix} n \\ k \end{smallmatrix}\right] = (n-1)\left[\begin{smallmatrix} n-1 \\ k \end{smallmatrix}\right] + \left[\begin{smallmatrix} n-1 \\ k-1 \end{smallmatrix}\right]$ | $\mathcal{A} = \mathsf{CYC}_{\ge 1}(\mathcal{Z})$ has $A(x) = \ln\frac{1}{1-x}$;<br/>$\mathcal{B} = \mathsf{SET}_y(\mathcal{A})$ | $\exp\left(y \ln\frac{1}{1-x}\right) = (1 - x)^{-y} = \sum_{n=0}^\infty y^{\overline{n}} \frac{x^n}{n!}$ |
| **Stirling 2nd Kind $\left\{\begin{smallmatrix} n \\ k \end{smallmatrix}\right\}$**<br/>($n$ elements into $k$ non-empty sets) | $\left\{\begin{smallmatrix} n \\ k \end{smallmatrix}\right\} = k\left\{\begin{smallmatrix} n-1 \\ k \end{smallmatrix}\right\} + \left\{\begin{smallmatrix} n-1 \\ k-1 \end{smallmatrix}\right\}$ | $\mathcal{A} = \mathsf{SET}_{\ge 1}(\mathcal{Z})$ has $A(x) = e^x - 1$;<br/>$\mathcal{B} = \mathsf{SET}_y(\mathcal{A})$ | $\exp\big(y(e^x - 1)\big)$ |
| **Eulerian Numbers $\left\langle\begin{smallmatrix} n \\ k \end{smallmatrix}\right\rangle$**<br/>(Permutations of $n$ with $k$ ascents) | $\left\langle\begin{smallmatrix} n \\ k \end{smallmatrix}\right\rangle = (k+1)\left\langle\begin{smallmatrix} n-1 \\ k \end{smallmatrix}\right\rangle + (n-k)\left\langle\begin{smallmatrix} n-1 \\ k-1 \end{smallmatrix}\right\rangle$ | PDE $\partial_x E = (1 + y \partial_y)E + y(x\partial_x - y\partial_y)E$<br/>or inclusion-exclusion on runs | $\dfrac{1 - y}{\exp((y - 1)x) - y} = \dfrac{(1 - y)\exp((1 - y)x)}{1 - y\exp((1 - y)x)}$ |

3. **Step-by-Step Derivation of the Eulerian Mixed EOGF via Variable Decoupling**:
   Let us derive both the **run-indexed** ($m = k+1$ ascending runs) and **ascent-indexed** ($k$ ascents, $\left\langle\begin{smallmatrix} 0 \\ 0 \end{smallmatrix}\right\rangle = 1$) forms of $E(x, y) = \sum_{n=0}^\infty \sum_{k=0}^n \left\langle\begin{smallmatrix} n \\ k \end{smallmatrix}\right\rangle y^k \frac{x^n}{n!}$ with zero magic steps:
   - **Form A (Run-Indexed Form $\widetilde{E}(x, y) = 1 + y(E(x,y) - 1)$)**:
     A permutation is a sequence of $m \ge 0$ non-empty strictly increasing runs, where a run of length $r \ge 2$ can be formed by merging two adjacent runs (tracked by inclusion-exclusion weight $(y-1)$ per merge). Hence each connected run block has weight $\frac{e^{(y-1)x} - 1}{y - 1}$, and taking $\mathsf{SEQ}$ of $y$-marked blocks gives:
     $$\begin{aligned}
     \widetilde{E}(x, y) := 1 + \sum_{n=1}^{\infty} \sum_{k=0}^{n-1} \left\langle\begin{matrix} n \\ k \end{matrix}\right\rangle y^{k+1} \frac{x^n}{n!}
     &= \sum_{m=0}^{\infty} y^m \left( \frac{e^{(y-1)x} - 1}{y - 1} \right)^m && \text{(Geometric series in } v = y \frac{e^{(y-1)x} - 1}{y - 1}\text{, }\operatorname{val}_x(v) = 1\text{)} \\
     &= \frac{1}{1 - y \frac{e^{(y-1)x} - 1}{y - 1}} = \frac{y - 1}{y e^{(y-1)x} - 1} = \frac{1 - y}{1 - y \exp((y - 1)x)}.
     \end{aligned}$$
   - **Form B (Ascent-Indexed Form $E(x, y)$)**:
     Since $\widetilde{E}(x, y) = 1 + y(E(x, y) - 1)$, solving for $E(x, y) = 1 + \frac{\widetilde{E}(x, y) - 1}{y}$ yields:
     $$\begin{aligned}
     E(x, y) &= 1 + \frac{1}{y}\left(\frac{1 - y}{1 - y e^{(y-1)x}} - 1\right) = 1 + \frac{1 - y - 1 + y e^{(y-1)x}}{y\big(1 - y e^{(y-1)x}\big)} \\
     &= \frac{1 - y e^{(y-1)x} + e^{(y-1)x} - 1}{1 - y e^{(y-1)x}} = \frac{(1 - y) e^{(1-y)x}}{1 - y e^{(1-y)x}} = \frac{1 - y}{\exp((y - 1)x) - y}.
     \end{aligned}$$
   - **Form C (Power-Series Substitution Form for `CF 1349F2`)**:
     Dividing numerator and denominator of $E(x, y) = \frac{y - 1}{y - \exp((y - 1)x)}$ by $(y - 1)$ and setting the composite variable $u := (y - 1)x$ (so $y = 1 + u/x$) gives:
     $$E(x, y) = \frac{1}{1 - \frac{e^{(y-1)x} - 1}{y - 1}} = \frac{1}{1 - x \left(\frac{e^u - 1}{u}\right)} = \sum_{m=0}^{\infty} x^m H(u)^m, \qquad H(u) := \frac{e^u - 1}{u} = \sum_{j=0}^{\infty} \frac{u^j}{(j+1)!}.$$
     Notice how $u = (y - 1)x$ completely **decouples** $y - 1$ and $x$: extracting $[x^n/n!] E(x, y)$ reduces to $n! \sum_{m=0}^n (y-1)^{n-m} [u^{n-m}] H(u)^m$, immediately proving $[x^n/n!] E(x,y)$ is a polynomial in $y$ of degree $\le n$ and unlocking the $O(n \log n)$ Lagrange / residue extraction in **CF 1349F2 — Slime and Sequences**!

---

### 2.5 Failure Modes, Pitfalls & Edge Cases for Ring Selection

1. **Attempting Un-Truncated Inversion When $Q(0, y) \notin K^\times$**:
   In $Q(x,y) = 1 - x - y$, $[x^0] Q(x,y) = 1 - y$ is **not** a unit in $K[y]$. Running 1D Newton iteration over $K[y][[x]]$ fails at step $0$; you must work in $(K[y]/(y^{K+1}))[[x]]$ or homogenize via $(x, y) \mapsto (x t, y t)$.
2. **Evaluating an Infinite Series in $K[[y]][[x]]$ at $y = y_0 \neq 0$**:
   The evaluation map $\operatorname{ev}_{y=y_0}$ is well-defined on $K[y][[x]]$, **not** on $K[[y]][[x]]$ (where it produces infinite sums $\sum_{k=0}^\infty f_{n,k} y_0^k$ in $K$). Before evaluating $y = \omega^r$, verify either that $F \in K[y][[x]]$ or that you are evaluating a rational expression $P(x,y)/Q(x,y)$ where $Q(0, \omega^r) \neq 0$ for every $r$.
3. **Equating $K((x))[[y]]$ and $K((y))[[x]]$**:
   For $G(x,y) = \frac{1}{x - y}$, expanding in $K((y))[[x]]$ gives $-\sum_{n=0}^\infty x^n y^{-n-1}$ (supported on $n \ge 0, k \le -1$), whereas expanding in $K((x))[[y]]$ gives $\sum_{k=0}^\infty x^{-k-1} y^k$ (supported on $n \le -1, k \ge 0$). Never swap expansion order when negative Laurent powers are present!
---

## 3. Iteration 32 / 84: Variable Decoupling, Evaluation–Interpolation, Twisted Kronecker Substitution, and Multivariate FPS Operations

### 3.1 Diagnostic Signals & Reverse-Engineering Scratchpad

#### A. Diagnostic Signals
1. **Linear-Exponent / Shear Decoupling Signal**:
   - **Signal**: Every monomial $x^i y^j$ in a bivariate generator $H(x, y)$ satisfies a linear relation $j = a i + b$, or $H(x, y)$ is built from terms like $(1 + y x^a)$ or $\frac{1}{1 - x - y x^2}$.
   - **Action**: Substitute the shear variable $u = x y^a$ so $[x^n y^k] H(x, y) = [u^n y^{k - a n}] \widetilde{H}(u, y)$.
2. **Symmetric-Sum / Diagonal Monomial Decoupling Signal**:
   - **Signal**: A multivariate expression depends on subsets of variables only through an elementary symmetric block ($z = x+y$ in **CF 960G**, $u = xyz$ in **AGC 058 D**, $u = x_1 x_2 x_3 x_4$ in **Luogu P5339**).
   - **Action**: Factor out the composite variable $u$, extract $[u^m]$ first, and multiply by the free multinomial/Vandermonde convolution of the remaining variables.
3. **Evaluation–Interpolation vs. Kronecker / 2D FFT Signal**:
   - **Signal**: Need $[x^N y^k] \mathcal{F}(A(x,y))$ where $N$ is large ($N \le 10^{18}$ via Bostan–Mori or $N \le 10^5$ via 1D ODE) and the $y$-degree is bounded by $D_y \le 2^m$, OR variables are coupled through a bitwise/cyclic group constraint ($\pmod{z_r^{10}-1}$ in **yukicoder 1783**, XOR/AND/OR in **Luogu P5406**).
   - **Action**: Evaluate $y$ at $L = 2^{\lceil \log_2(D_y + 1) \rceil}$ roots of unity $y_r = c \omega^r$ (or perform FWT on $y$), solve $L$ independent 1D problems in $x$, and run IDFT/IFWT on $y$.
4. **Twisted Kronecker ($\chi$-Graded) Multivariate FPS Signal**:
   - **Signal**: General dense $d$-variate truncated operations ($\times, \operatorname{inv}, \ln, \exp, \operatorname{pow}$) modulo $(x_1^{n_1}, \dots, x_d^{n_d})$ where total state volume $N = \prod_{i=1}^d n_i \le 3 \times 10^5$ (**UOJ #596** with $A, B, C \le 50$).
   - **Action**: Map $\mathbb{F}_p[x_1, \dots, x_d]/(x_1^{n_1}, \dots, x_d^{n_d})$ into $\mathbb{F}_p[t]/(t^N)[z]/(z^d)$ using the carry-tracking $\chi$-statistic and the radial Euler derivation $\mathfrak{D} = \sum_{j=1}^d w_j x_j \partial_{x_j}$.

#### B. Reverse-Engineering Scratchpad
```
Given F(x_1, ..., x_d) mod (x_1^{n_1}, ..., x_d^{n_d}):
 ├─ Can F be written in terms of composite variables u_1, ..., u_r (r < d)?
 │   ├─ Shear u = x y^a:       [x^n y^k] F(x, y) = [u^n y^{k - an}] F(u y^{-a}, y)
 │   ├─ Homogenization x -> xt, y -> yt: collects total degree n + k as [t^m]
 │   └─ Symmetric block z = x+y or u = xyz: extract [z^m] or [u^m] in O(1)/1D NTT first!
 ├─ Is F a sequence of 1D operations parameterized by auxiliary y of known degree D_y?
 │   └─ Check Q(0, \omega^r) != 0. If zero at some root, shift y_r = c * \omega^r (c != 0)!
 │      Evaluate y = y_0, ..., y_{L-1} -> Solve L independent 1D problems -> IDFT in y.
 └─ Is F a full dense d-variate FPS needing inv / ln / exp / pow mod (x_1^{n_1}, ..., x_d^{n_d})?
     ├─ Packing: Twisted Kronecker \chi(I) = (\sum_{r=1}^{d-1} \lfloor I / N_r \rfloor) mod d
     │           Costs O(d N \log N) vs. Naive zero-padding O(2^d N \log N).
     └─ Transcendental Ops:
         ├─ Approach 1 (Cohort 2): Partial Derivative \partial_{x_1} + 1D boundary at x_1 = 0
         └─ Approach 2 (Cohorts 1 & 2): Radial Euler Operator \mathfrak{D} = t \frac{d}{dt} on Kronecker index!
```

---

### 3.2 Variable Decoupling & Monomial Change of Variables

#### Theorem 3.1 (Shear Automorphism & Monomial Decoupling)
Let $F(x, y) \in K[[x, y]]$ and let $a \in \mathbb{Z}_{>0}$. Under the substitution $u = x y^a$ (so $x = u y^{-a}$), if $\widetilde{F}(u, y) := F(u y^{-a}, y)$ belongs to $K[[u, y]]$ (which holds whenever $f_{n, k} = 0$ for all $k < a n$), then:
$$\begin{aligned}
[x^n y^k] F(x, y)
&= [x^n y^k] \sum_{i \ge 0} \sum_{j \ge 0} \tilde{f}_{i, j} (x y^a)^i y^j && \text{(Substitute } u = x y^a \text{ into } \widetilde{F}(u, y)\text{)} \\
&= [x^n y^k] \sum_{i \ge 0} \sum_{j \ge 0} \tilde{f}_{i, j} x^i y^{a i + j} && \text{(Combine powers of } y\text{)} \\
&= \tilde{f}_{n, k - a n} = [u^n y^{k - a n}] \widetilde{F}(u, y) && \text{(Match } i = n \text{ and } a n + j = k\text{)}.
\end{aligned}$$

#### Canonical Worked Examples of Variable Decoupling
1. **Sheared Rational Denominator (`CF 755G`)**:
   In $F(x, y) = \frac{1}{1 - (1+y)x - y x^2}$, the denominator mixes $x$, $xy$, and $x^2 y$. Substituting $x$ by $x$ and grouping powers of $y$:
   $$\frac{1}{1 - x - xy(1 + x)} = \sum_{k=0}^{\infty} y^k x^k \frac{(1+x)^k}{(1-x)^{k+1}} \implies [x^n y^k] F(x,y) = [x^{n-k}] \frac{(1+x)^k}{(1-x)^{k+1}}.$$
   Every $y^k$ slice is now an explicit 1D rational function of $x$!
2. **Linear Sum Grouping (`CF 960G`)**:
   To extract $[x^A y^B] \prod_{i=0}^{n-2} (i + x + y)$, observe that $x$ and $y$ appear *exclusively* through $z = x + y$:
   $$\begin{aligned}
   [x^A y^B] \prod_{i=0}^{n-2} (i + x + y)
   &= [x^A y^B] \sum_{m=0}^{n-1} \left[\begin{matrix} n-1 \\ m \end{matrix}\right] (x + y)^m && \text{(Expand rising factorial in } z = x+y\text{)} \\
   &= \binom{A+B}{A} \left[\begin{matrix} n-1 \\ A+B \end{matrix}\right] && \text{(Extract } [x^A y^B] (x+y)^m \text{ at } m = A+B\text{)}.
   \end{aligned}$$
3. **3-Variable Diagonal Monomial Grouping (`AtCoder AGC 058 D`)**:
   In the Goulden–Jackson rational generating function $F(x,y,z) = \frac{1 - xyz}{1 - (x+y+z) + 2xyz}$, the variables $x, y, z$ interact only via $s = x+y+z$ and $u = xyz$:
   $$\begin{aligned}
   [x^A y^B z^C] \frac{1 - u}{1 - s + 2u}
   &= [x^A y^B z^C] (1 - u) \sum_{m=0}^{\infty} \frac{(-2u)^m}{(1 - s)^{m+1}} && \text{(Geometric series in } \frac{-2u}{1-s}\text{)} \\
   &= \sum_{m \ge 0} (-2)^m \big( [x^{A-m} y^{B-m} z^{C-m}] (1-s)^{-m-1} \\
   &\qquad\qquad\qquad - [x^{A-m-1} y^{B-m-1} z^{C-m-1}] (1-s)^{-m-1} \big) && \text{(Since } [x^a y^b z^c] u^m G = [x^{a-m} y^{b-m} z^{c-m}] G\text{)},
   \end{aligned}$$
   reducing a 3D coefficient extraction to a 1D sum of multinomials in $O(\min(A,B,C))$.

---

### 3.3 Evaluation–Interpolation on Auxiliary Variables & The Shifted-Root Fix

When a bivariate problem asks for $[x^N y^k] F(x, y)$ where $[x^N] F(x, y)$ is a polynomial in $y$ of degree $D_y < L = 2^m$, we can bypass symbolic $y$-polynomial arithmetic by **evaluating $y$ at $L$ points in $\mathbb{F}_p$**:

1. **Choose $L = 2^{\lceil \log_2(D_y + 1) \rceil}$ evaluation points**:
   Ordinarily we pick $y_r = \omega^r$ ($0 \le r < L$), where $\omega = g^{(p-1)/L} \bmod p$ is a primitive $L$-th root of unity.
2. **Cohort 1 Blind-Spot Catch — The Shifted Root-of-Unity Fix ($y_r = c \omega^r$)**:
   > [!WARNING]
   > When extracting $[x^N] \frac{P(x, y_r)}{Q(x, y_r)}$ via 1D Bostan–Mori or 1D FPS inversion, we require the constant term $Q(0, y_r) \not\equiv 0 \pmod p$ for all $0 \le r < L$. If $Q(0, y) = 1 - y$, then at $r = 0$ we have $y_0 = \omega^0 = 1$, causing a **division-by-zero crash** $Q(0, 1) = 0$!
   >
   > **The Fix**: Pick a non-zero shift scalar $c \in \mathbb{F}_p^\times$ such that $Q(0, c \omega^r) \neq 0$ for all $0 \le r < L$ (since $\deg_y Q(0, y) \le D_y \ll p$, a random $c \in \mathbb{F}_p^\times$ succeeds with probability $\ge 1 - \frac{L \cdot \deg_y Q(0,y)}{p-1}$).
   > - **Shifted Forward DFT**: Evaluate $y$ on the coset $y_r = c \omega^r$ by scaling the input coefficients $a_j \mapsto a_j c^j$ before running standard NTT of length $L$.
   > - **Solve $L$ Independent 1D Subproblems**: Compute $v_r = [x^N] F(x, c \omega^r) \in \mathbb{F}_p$ for each $0 \le r < L$.
   > - **Shifted Inverse DFT**: Run standard INTT of length $L$ on $(v_0, \dots, v_{L-1})$ to recover $\tilde{f}_{N, j} = c^j f_{N, j}$, then multiply by $c^{-j} \bmod p$ to obtain $f_{N, j} = [x^N y^j] F(x, y)$!

---

### 3.4 Multivariate Convolution: 2D FFT vs. Naive Kronecker vs. Twisted Kronecker ($\chi$-Grading)

Suppose we want to compute the truncated multivariate product
$$C(x_1, \dots, x_d) = A(x_1, \dots, x_d) B(x_1, \dots, x_d) \bmod (x_1^{n_1}, \dots, x_d^{n_d}), \qquad N := \prod_{r=1}^d n_r.$$

#### Method 1: Row-Column Multidimensional FFT / NTT
Viewing $\mathbb{F}_p[x_1, \dots, x_d]/(x_1^{L_1}, \dots, x_d^{L_d})$ where $L_r = 2^{\lceil \log_2(2 n_r - 1) \rceil}$, apply 1D NTT along axis $1$, then axis $2$, ..., up to axis $d$, multiply pointwise, and apply 1D INTT along each axis.
- **Blowup flaw**: Each dimension pads to at least $2 n_r - 1$, inflating the array size from $N = \prod n_r$ to $\prod L_r \ge 2^d N$ (and up to $4^d N$ when $n_r = 2^{k_r} + 1$).

#### Method 2: Naive Zero-Padded Kronecker Substitution
Map $x_1 \mapsto t$, $x_2 \mapsto t^{2 n_1 - 1}$, ..., $x_d \mapsto t^{\prod_{r < d}(2 n_r - 1)}$. Since $i_r + j_r \le 2 n_r - 2 < 2 n_r - 1$, no base-$(2n_r - 1)$ carry occurs between dimensions during 1D multiplication.
- **Blowup flaw**: Still inflates the 1D polynomial length to $\prod_{r=1}^d (2 n_r - 1) \approx 2^d N$.

#### Method 3: Twisted Kronecker Substitution ($\chi$-Graded Truncation — van der Hoeven 2002 / Elegia / EntropyIncreaser)
How can we pack $\mathbb{F}_p[x_1, \dots, x_d]/(x_1^{n_1}, \dots, x_d^{n_d})$ into a 1D array of exact size $N = \prod_{r=1}^d n_r$ **with zero internal padding** while preventing cross-dimension carries?

1. **Tight Mixed-Radix Packing**:
   Define stride products $N_0 = 1$ and $N_r = \prod_{j=1}^r n_j$ for $1 \le r \le d$ (so $N_d = N$). Biject each multi-index $\mathbf{i} = (i_1, \dots, i_d) \in \prod_{r=1}^d [0, n_r - 1]$ to the integer
   $$I(\mathbf{i}) = \sum_{r=1}^d i_r N_{r-1} \in [0, N - 1], \qquad i_r = \left\lfloor \frac{I}{N_{r-1}} \right\rfloor \bmod n_r.$$
2. **Exact Carry Equation and the $\chi$-Statistic**:
   When we multiply $t^{I(\mathbf{i})}$ and $t^{I(\mathbf{j})}$, their 1D exponent is $I(\mathbf{i}) + I(\mathbf{j}) = \sum_{r=1}^d (i_r + j_r) N_{r-1}$.
   Suppose the true $d$-variate monomial $x_1^{i_1+j_1} \cdots x_d^{i_d+j_d}$ survives modulo $(x_1^{n_1}, \dots, x_d^{n_d})$, meaning $0 \le i_r + j_r < n_r$ for every $r \in \{1, \dots, d\}$.
   Why isn't $I(\mathbf{i}) + I(\mathbf{j})$ automatically equal to $I(\mathbf{i}+\mathbf{j})$? It **is** when $i_r + j_r < n_r$ for all $r$—however, what about a **spurious pair** $(\mathbf{i}', \mathbf{j}')$ where $i'_r + j'_r \ge n_r$ for some $r$, whose carry into $N_r$ causes $I(\mathbf{i}') + I(\mathbf{j}') = I(\mathbf{k})$ for a valid multi-index $\mathbf{k}$?
   Let $c_r = \lfloor (i_r + j_r) / n_r \rfloor \in \{0, 1\}$ be the carry out of digit $r$, and set $k_r = (i_r + j_r) - c_r n_r \in [0, n_r - 1]$ for $1 \le r \le d$ (with $c_0 = 0$). Since $n_r N_{r-1} = N_r$, we have:
   $$\begin{aligned}
   \left\lfloor \frac{I(\mathbf{i}) + I(\mathbf{j})}{N_r} \right\rfloor
   &= \left\lfloor \frac{I(\mathbf{i})}{N_r} \right\rfloor + \left\lfloor \frac{I(\mathbf{j})}{N_r} \right\rfloor + c_r, \qquad (1 \le r \le d-1).
   \end{aligned}$$
   Define the **carry-tracking grading** $\chi : [0, N-1] \to \mathbb{Z}_d$ by
   $$\chi(I) := \left( \sum_{r=1}^{d-1} \left\lfloor \frac{I}{N_r} \right\rfloor \right) \bmod d = \left( \sum_{r=2}^d i_r (r - 1) \right) \bmod d.$$
   Summing the carry identity over $r = 1, \dots, d-1$ yields:
   $$\chi\big(I(\mathbf{i}) + I(\mathbf{j})\big) - \chi\big(I(\mathbf{i})\big) - \chi\big(I(\mathbf{j})\big) \equiv \sum_{r=1}^{d-1} c_r \pmod d.$$
   Since $I(\mathbf{i}) + I(\mathbf{j}) < N = N_d$ forces $c_d = 0$, the remaining carries $c_1, \dots, c_{d-1} \in \{0, 1\}$ are **non-negative** and there are only $d - 1$ of them:
   $$0 \le \sum_{r=1}^{d-1} c_r \le d - 1.$$
   Therefore,
   $$\sum_{r=1}^{d-1} c_r \equiv 0 \pmod d \iff c_1 = c_2 = \cdots = c_{d-1} = 0 \iff i_r + j_r < n_r \text{ for all } 1 \le r \le d!$$
3. **Algorithm (Twisted Kronecker Multiplication in $O(d N \log N)$)**:
   - Decompose $A$ into $d$ sparse 1D polynomials $A_0(t), \dots, A_{d-1}(t)$ of length $N$, where $[t^I] A_u(t) = a_I \cdot [\chi(I) = u]$ (and similarly $B_0(t), \dots, B_{d-1}(t)$).
   - Apply forward 1D NTT of length $L = 2^{\lceil \log_2(2N - 1) \rceil}$ to $A_0, \dots, A_{d-1}$ and $B_0, \dots, B_{d-1}$ ($2d$ NTTs).
   - For each target residue $w \in \{0, \dots, d-1\}$, accumulate pointwise in the frequency domain:
     $$\widehat{C}_w(\omega^k) = \sum_{u + v \equiv w \pmod d} \widehat{A}_u(\omega^k) \widehat{B}_v(\omega^k).$$
   - Apply inverse 1D NTT to $\widehat{C}_0, \dots, \widehat{C}_{d-1}$ ($d$ INTTs) and extract, for each $I \in [0, N-1]$, the carry-free coefficient
     $$c_I = [t^I] C_{\chi(I)}(t).$$

#### Concrete Hand-Checkable Trace ($d = 2$, $n_1 = 2, n_2 = 2$, $N = 4$)
Let $A(x_1, x_2) = 1 + 2 x_1 + 3 x_2 + 4 x_1 x_2$ and $B(x_1, x_2) = 1 + 5 x_1 + 6 x_2 + 7 x_1 x_2 \bmod (x_1^2, x_2^2)$.
- **True Product $\bmod (x_1^2, x_2^2)$**:
  $$A \cdot B \equiv 1 + (2+5)x_1 + (3+6)x_2 + (4 + 2\cdot 6 + 3\cdot 5 + 7)x_1 x_2 = 1 + 7 x_1 + 9 x_2 + 38 x_1 x_2.$$
- **Kronecker Index & $\chi(I) = \lfloor I / 2 \rfloor \bmod 2$**:
  - $(0,0) \mapsto I=0, \chi(0)=0$; $(1,0) \mapsto I=1, \chi(1)=0$; $(0,1) \mapsto I=2, \chi(2)=1$; $(1,1) \mapsto I=3, \chi(3)=1$.
  - Notice why untwisted 1D multiplication fails at $I = 2$: $x_1 \cdot x_1$ corresponds to $I(1,0) + I(1,0) = 1 + 1 = 2 = I(0,1)$, so the illegal carry term $2 x_1 \cdot 5 x_1 = 10 x_1^2$ leaks into $I=2$ ($x_2$)!
- **Twisted Filtering**:
  - $A_0(t) = 1 + 2t$, $A_1(t) = 3t^2 + 4t^3$; $B_0(t) = 1 + 5t$, $B_1(t) = 6t^2 + 7t^3$.
  - $C_0(t) = A_0 B_0 + A_1 B_1 = (1 + 7t + 10t^2) + (18t^4 + 45t^5 + 28t^6)$.
  - $C_1(t) = A_0 B_1 + A_1 B_0 = (6t^2 + 19t^3 + 14t^4) + (3t^2 + 19t^3 + 20t^4) = 9t^2 + 38t^3 + 34t^4$.
  - Extracting $c_I = [t^I] C_{\chi(I)}(t)$:
    - $I=0 (\chi=0): [t^0] C_0 = 1$
    - $I=1 (\chi=0): [t^1] C_0 = 7$
    - $I=2 (\chi=1): [t^2] C_1 = 9$ (the illegal carry $10t^2$ sits harmlessly in $C_0$, **not** $C_1$!)
    - $I=3 (\chi=1): [t^3] C_1 = 38$.
  - Result: $1 + 7 x_1 + 9 x_2 + 38 x_1 x_2$, matching the true product with zero padding!

---

### 3.5 Multivariate FPS `inv`, `ln`, `exp`, and `pow`: Two Equivalent Perspectives

Let $\mathcal{R}_{\mathbf{n}} = K[x_1, \dots, x_d]/(x_1^{n_1}, \dots, x_d^{n_d})$. How do we compute $F^{-1}, \ln F, \exp F, F^\alpha \in \mathcal{R}_{\mathbf{n}}$?

#### Perspective A (Cohort 1 & 2 Synthesis): The Radial Euler Derivation $\mathfrak{D}$ in the Twisted Kronecker Ring
Define the radial Euler derivation $\mathfrak{D} : \mathcal{R}_{\mathbf{n}} \to \mathcal{R}_{\mathbf{n}}$ using the Kronecker weights $w_r = N_{r-1}$:
$$\mathfrak{D} := \sum_{r=1}^d N_{r-1} x_r \frac{\partial}{\partial x_r} \implies \mathfrak{D}\left( \sum_{\mathbf{i}} f_{\mathbf{i}} \mathbf{x}^{\mathbf{i}} \right) = \sum_{I=0}^{N-1} I \cdot f_I \mathbf{x}^{\mathbf{i}(I)}.$$
Because $\mathfrak{D}$ is a **derivation** ($\mathfrak{D}(FG) = \mathfrak{D}(F)G + F\mathfrak{D}(G)$ and $\mathfrak{D}(\phi(F)) = \phi'(F)\mathfrak{D}(F)$) that acts on the 1D Kronecker index $I \in [0, N-1]$ simply as **multiplication by $I$** (identical to $t \frac{d}{dt}$ on 1D polynomials!) and preserves $\chi(I)$, all four multivariate transcendental operations reduce directly to 1D Newton iteration / radial ODEs with **Multivariate Twisted Kronecker multiplication** replacing 1D multiplication:

1. **Multivariate Inversion ($G = F^{-1}$ for $f_{\mathbf{0}} \neq 0$)**:
   Lift precision on the 1D Kronecker index $I \bmod t^m \to t^{2m}$ for $m = 1, 2, 4, \dots, N$:
   $$G_{2m} \equiv G_m \big(2 - F \cdot_{\chi} G_m\big) \pmod{t^{2m}}.$$
2. **Multivariate Logarithm ($L = \ln F$ for $f_{\mathbf{0}} = 1$)**:
   Apply $\mathfrak{D}$ to $L = \ln F$:
   $$\mathfrak{D}(L) = \mathfrak{D}(F) \cdot_{\chi} F^{-1} \implies l_I = \frac{1}{I} [t^I]\big(\mathfrak{D}(F) \cdot_{\chi} F^{-1}\big) \quad (1 \le I < N), \qquad l_0 = 0.$$
3. **Multivariate Exponential ($E = \exp F$ for $f_{\mathbf{0}} = 0$)**:
   Either run Newton iteration $E_{2m} \equiv E_m \cdot_{\chi} (1 - \ln E_m + F) \pmod{t^{2m}}$, or use CDQ D&C on $\mathfrak{D}(E) = \mathfrak{D}(F) \cdot_{\chi} E$.
4. **Multivariate Power ($P = F^\alpha$ for $f_{\mathbf{0}} = 1$)**:
   Compute $F^\alpha = \exp(\alpha \ln F)$. (Warning: if $f_{\mathbf{0}} = 0$, shift rules $F = x_1^k \widetilde{F}$ DO NOT work in $d \ge 2$ if the lowest degree homogeneous part is not a single monomial, e.g., $F = x_1 + x_2$!)

#### Perspective B (Cohort 2 Synthesis): Partial Derivative $\partial_{x_1}$ + Lower-Dimensional Boundary at $x_1 = 0$
Equivalently, differentiating with respect to $x_1$ alone gives $\partial_{x_1} \ln F = F^{-1} \partial_{x_1} F$, which determines all coefficients $[x_1^{i_1} \cdots x_d^{i_d}] \ln F$ with $i_1 \ge 1$ via $\int dx_1$, while the $i_1 = 0$ slice is the $(d-1)$-variate boundary $(\ln F)(0, x_2, \dots, x_d) = \ln\big(F(0, x_2, \dots, x_d)\big)$. Notice that the Radial Euler Derivation $\mathfrak{D}$ automatically unifies all $d$ partial derivatives into a single pass without needing recursive boundary calls!

#### Complexity Comparison Table
| Operation on $\mathbb{F}_p[x_1, \dots, x_d]/(x_1^{n_1}, \dots, x_d^{n_d})$ ($N = \prod n_r$) | 2D / $d$-D Row-Column FFT | Naive Kronecker | Twisted Kronecker ($\chi$-Graded + $\mathfrak{D}$) |
| :--- | :--- | :--- | :--- |
| **Truncated Multiplication $A \cdot B$** | $O(2^d d N \log N)$ | $O(2^d N \log N)$ | **$O(d N \log N)$** ($3d$ NTTs + $d^2$ pointwise) |
| **Multivariate Inversion $F^{-1}$** | $O(2^d d N \log N)$ | $O(2^d N \log N)$ | **$O(d N \log N)$** |
| **Multivariate $\ln F, \exp F, F^\alpha$** | $O(2^d d N \log N)$ | $O(2^d N \log N)$ | **$O(d N \log N)$** |

---

### 3.6 Failure Modes, Pitfalls & Edge Cases for Iteration 32/84

1. **Modulus $p \le N$ in the Radial Euler Operator $\mathfrak{D}$**:
   Because $\mathfrak{D}^{-1}$ divides the $I$-th Kronecker coefficient by $I \in [1, N-1]$, if the prime modulus $p \le N - 1$, then $I \equiv 0 \pmod p$ is **not invertible** even when every individual exponent satisfies $i_r < n_r < p$! In that small-prime regime, you must switch to **Perspective B** (integrating $\partial_{x_1}$ with $i_1 < n_1 < p$ and recursing on $x_1 = 0$) instead of $\mathfrak{D}$.
2. **Non-Monomial Leading Forms in Multivariate $F^\alpha$**:
   In 1D, if $F(0) = 0$, we factor $F(x) = x^v \widetilde{F}(x)$ with $\widetilde{F}(0) \neq 0$ and compute $F(x)^K = x^{vK} \widetilde{F}(x)^K$. In $d \ge 2$ variables, if $F(0, 0) = 0$, $F(x, y)$ need not factor as $x^a y^b \widetilde{F}(x, y)$ with $\widetilde{F}(0,0) \neq 0$ (for example, $F(x, y) = x + y$). Never apply the 1D valuation shift rule to $F(x, y)^K$ unless $F$ is a monomial multiple of a unit!

---

## 4. Iteration 33 / 85: Rational Generating Functions, 1D & 2D Bostan–Mori, Graeffe Root-Squaring, and Kinoshita–Li $x$-Halving / $y$-Doubling

### 4.1 Diagnostic Signals & Reverse-Engineering Scratchpad

#### A. Diagnostic Signals
1. **1D Bostan–Mori Signal**:
   - **Signal**: Linear recurrence of order $d \le 10^5$ at a huge index $N \le 10^{18}$, or a rational generating function $[x^N] \frac{P(x)}{Q(x)}$ obtained from transfer matrices / continued fractions (**ABC 300 Ex**, **CF 1117D**, **UOJ #424**).
   - **Action**: Run 1D Bostan–Mori in $\frac{2}{3}\mathsf{M}(d)\log_2 N = O(d \log d \log N)$ time.
2. **2D Bostan–Mori Regime A (Truncated $y$-Ring) Signal**:
   - **Signal**: Need $[x^N y^k] \frac{P(x, y)}{Q(x, y)}$ for a huge $N \le 10^{18}$ and small $k \le K$ where $d_x K \le 2 \times 10^5$ (**QOJ #4815**, **CF 755G**).
   - **Action**: Run Bostan–Mori on $x$ with coefficients in $R = \mathbb{F}_p[y]/(y^{K+1})$ in $O(d_x K \log(d_x K) \log N)$.
3. **2D Bostan–Mori Regime B ($y$-Evaluation & Interpolation) Signal**:
   - **Signal**: Same as Regime A, OR $[x^N] \frac{P(x, y)}{Q(x, y)}$ is known to be a polynomial in $y$ of degree $D_y \le 2 \times 10^5$ (e.g., $Q(x, y)$ has $x$-degree $d_x$ and $y$ only appears with degree $\le c$ per $x$).
   - **Action**: Evaluate $y = c \omega^r$ at $L > D_y$ points, run $L$ decoupled 1D Bostan–Mori calls of degree $d_x$, and interpolate in $O(L d_x \log d_x \log N + L \log L)$.
4. **2D Bostan–Mori Regime C (Kinoshita–Li $x$-Halving / $y$-Doubling) Signal**:
   - **Signal**: Need $[x^n] g(x) f(x)^k$ for all $0 \le k < n$ (**Power Projection** / Lagrange Inversion), or $g(f(x)) \bmod x^n$ (**FPS Composition**), or $f^{\langle -1 \rangle}(x) \bmod x^n$ (**Compositional Inverse**) for $n \le 2 \times 10^5$ (**ARC 138 F**, **ABC 387 G**, **QOJ #8528**).
   - **Action**: Form the bivariate rational function $\frac{g(x)}{1 - y f(x)} \bmod x^n$. At each step of Bostan–Mori on $x$, degree in $x$ halves ($N \to \lfloor N/2 \rfloor$) while degree in $y$ doubles ($K \to 2K$), maintaining invariant product $N \cdot K = n$ across $\log_2 n$ levels for $O(n \log^2 n)$ total time!
5. **2D Bostan–Mori Regime D (Bostan–Christol–Dumas Frobenius Reduction) Signal**:
   - **Signal**: Need $[x^N y^M] \frac{P(x, y)}{Q(x, y)} \bmod p$ where **both** $N, M \le 10^{18}$ are huge, and the prime modulus $p$ is small ($p \le 500$).
   - **Action**: Multiply by $Q(x,y)^{p-1}$ and use $Q(x,y)^p \equiv Q(x^p, y^p) \pmod p$ to divide both $N$ and $M$ by $p$ in $O((p d_x d_y) \log(p d_x d_y) \log_p(\max(N,M)))$.

#### B. Reverse-Engineering Scratchpad
```
Need [x^N y^M] P(x, y) / Q(x, y):
 ├─ M = 0 (Univariate 1D):
 │   └─ 1D Bostan-Mori: P(x)Q(-x) parity split -> 4 NTTs of size 2d per bit of N.
 ├─ N <= 10^18, M = K <= 10^5, d_x <= 20:
 │   ├─ Regime A: Truncated ring (K[y]/(y^{K+1}))[[x]] -> O(d_x K \log(d_x K) \log N)
 │   └─ Regime B: Evaluate y = c \omega^r (r = 0..L-1) -> L runs of 1D BM -> IDFT.
 ├─ N = n <= 2*10^5, Q(x, y) = 1 - y f(x), need [x^{n-1} y^k] for ALL 0 <= k < n:
 │   └─ Regime C (Kinoshita-Li 2024):
 │      ├─ Power Projection: forward 2D BM (x-degree N/2, y-degree 2K) -> O(n \log^2 n)
 │      └─ FPS Composition: Tellegen transpose of Power Projection -> O(n \log^2 n)
 └─ N, M <= 10^18 BOTH huge, modulus p small prime:
     └─ Regime D (Frobenius): P * Q^{p-1} / Q(x^p, y^p) mod p -> base-p digit extraction!
```

---

### 4.2 1D Bostan–Mori Algorithm, Graeffe Root-Squaring, and Bit-Reversed NTT Doubling

#### Theorem 4.1 (Rational Parity Splitting & Bostan–Mori Step)
Let $P(x), Q(x) \in K[x]$ with $\deg P < \deg Q = d$ and $Q(0) = 1$. Since $Q(x) Q(-x)$ is invariant under $x \mapsto -x$, there exists a unique polynomial $V(x) \in K[x]$ of degree $d$ with $V(0) = 1$ such that
$$Q(x) Q(-x) = V(x^2).$$
Splitting the numerator $U(x) := P(x) Q(-x)$ into its even and odd parts $U(x) = U_{\text{even}}(x^2) + x U_{\text{odd}}(x^2)$ gives:
$$\frac{P(x)}{Q(x)} = \frac{P(x) Q(-x)}{Q(x) Q(-x)} = \frac{U_{\text{even}}(x^2)}{V(x^2)} + x \frac{U_{\text{odd}}(x^2)}{V(x^2)} \implies [x^N] \frac{P(x)}{Q(x)} = \begin{cases} [x^{N/2}] \dfrac{U_{\text{even}}(x)}{V(x)}, & N \equiv 0 \pmod 2, \\ [x^{(N-1)/2}] \dfrac{U_{\text{odd}}(x)}{V(x)}, & N \equiv 1 \pmod 2. \end{cases}$$

#### Connection to Graeffe's Root-Squaring Method & MSB-First Bostan–Mori (Cohort 2 / Ryuhei Mori 2021)
1. **Graeffe Interpretation**:
   If $Q(x) = \prod_{i=1}^d (1 - \alpha_i x)$ where $\alpha_1, \dots, \alpha_d$ are the characteristic roots of the recurrence, then:
   $$V(x^2) = Q(x) Q(-x) = \prod_{i=1}^d (1 - \alpha_i x)(1 + \alpha_i x) = \prod_{i=1}^d (1 - \alpha_i^2 x^2) \implies V(z) = \prod_{i=1}^d (1 - \alpha_i^2 z).$$
   Thus, one iteration of Bostan–Mori on the denominator $Q \mapsto V$ is **Graeffe's root-squaring iteration**, which squares every recurrence eigenvalue $\alpha_i \mapsto \alpha_i^2$ simultaneously without factoring $Q(x)$!
2. **MSB-First (Top-Down) Bostan–Mori & Why LSB-First Wins**:
   Standard Bostan–Mori processes the bits of $N$ from **least significant bit (LSB)** to **most significant bit (MSB)**. Can it be run **MSB-first** like repeated squaring $x^N \bmod Q^{\text{rev}}(x)$?
   Yes (Mori 2021): precompute the chain of $\ell = \lfloor \log_2 N \rfloor$ Graeffe denominators $Q^{(0)}(x) = Q(x)$, $Q^{(j+1)}(x^2) = Q^{(j)}(x) Q^{(j)}(-x)$ from bottom to top, and then walk down from $j = \ell - 1$ to $0$ using transposed parity projection. However, MSB-first requires storing all $\log_2 N$ denominators $Q^{(j)}$, whereas LSB-first discards each denominator immediately, running in $O(d)$ space!

#### Bit-Reversed NTT-Domain Doubling Trick ($\frac{2}{3}\mathsf{M}(d) \log_2 N$)
Let $L = 2^{\lceil \log_2(2d + 1) \rceil}$ and let $\omega$ be a primitive $L$-th root of unity. Since $-1 = \omega^{L/2}$, the values of $Q(-x)$ at the $L$-th roots of unity are already present in $\widehat{Q}$! Specifically, in bit-reversed NTT order, $(\omega^{2k}, -\omega^{2k})$ occupy adjacent indices $(2k, 2k+1)$:
1. Compute $\widehat{P} = \operatorname{NTT}_L(P)$ and $\widehat{Q} = \operatorname{NTT}_L(Q)$ (**2 NTTs of size $L$**, or 1 NTT via doubling if $\widehat{P}, \widehat{Q}$ of size $L/2$ are carried over from the previous step!).
2. In $O(L)$ pointwise operations, compute for each pair $(y, -y)$:
   $$\widehat{V}(y^2) = \widehat{Q}(y)\widehat{Q}(-y), \qquad \widehat{U}_{\text{even/odd}}(y^2) = \begin{cases} \dfrac{\widehat{P}(y)\widehat{Q}(-y) + \widehat{P}(-y)\widehat{Q}(y)}{2}, & N \text{ even}, \\ \dfrac{\widehat{P}(y)\widehat{Q}(-y) - \widehat{P}(-y)\widehat{Q}(y)}{2y}, & N \text{ odd}. \end{cases}$$
3. Apply $\operatorname{INTT}_{L/2}$ to $\widehat{U}_{\text{even/odd}}$ and $\widehat{V}$ (**2 INTTs of size $L/2$**), then **NTT-double** each of size $L/2 \to L$ at cost $2 \times \frac{1}{2}\mathsf{M}(d)$.
- **Total work per bit of $N$**: $4 \text{ NTTs of size } L/2 = 2 \text{ NTTs of size } L = \frac{2}{3}\mathsf{M}(d)$ (since one standard multiplication uses $3$ NTTs of size $L$).

---

### 4.3 The Four Regimes of 2D Bostan–Mori

#### Regime A: Truncated Auxiliary Ring $(K[y]/(y^{K+1}))[[x]]$
When $N \le 10^{18}$ is huge and we want $[x^N y^k] \frac{P(x,y)}{Q(x,y)}$ for $0 \le k \le K$ with $Q(0,0) \neq 0$:
- Work inside $R[[x]]$ where $R = K[y]/(y^{K+1})$.
- Every step of 1D Bostan–Mori on $x$ computes $P(x, y) Q(-x, y) \bmod y^{K+1}$ and $Q(x, y) Q(-x, y) \bmod y^{K+1}$ while keeping $\deg_x P < \deg_x Q = d_x$ and $\deg_y < K + 1$.
- Using 2D NTT or Kronecker substitution of size $O(d_x K)$, each of the $\log_2 N$ steps takes $O(d_x K \log(d_x K))$, for a total complexity of **$O(d_x K \log(d_x K) \log N)$**.

#### Regime B: Auxiliary Evaluation & Interpolation ($y_r = c \omega^r$)
When $[x^N] \frac{P(x, y)}{Q(x, y)}$ is an exact polynomial in $y$ of degree $D_y$ (for instance, when $Q(x, y) = 1 - x A(y)$ or $Q(0, y) = 1$), evaluate $y$ at $L = 2^{\lceil \log_2(D_y + 1) \rceil}$ shifted roots of unity $y_r = c \omega^r$, run $L$ independent 1D Bostan–Mori calls of degree $d_x$, and apply 1D INTT of length $L$:
- **Complexity**: **$O(L d_x \log d_x \log N + L \log L)$** time and **$O(L + d_x)$** space.

#### Regime C: Kinoshita–Li (2024) $x$-Halving / $y$-Doubling for Power Projection & FPS Composition in $O(n \log^2 n)$
This is the modern competitive programming breakthrough (Yasunori Kinoshita & Baitian Li, ISSAC 2024) that unified **Power Projection**, **Lagrange Inversion**, **FPS Composition**, and **Compositional Inverse** into a single $O(n \log^2 n)$ algorithm with tiny NTT constant factor.

##### 1. Problem 1: Power Projection (Transposed Composition)
Given $f(x), g(x) \in K[[x]] / (x^n)$ with **zero constant term $f(0) = 0$**, compute the linear form projections:
$$w_k = [x^{n-1}] g(x) f(x)^k \qquad \text{for all } 0 \le k < n.$$
Observe that $w_k$ is the coefficient of $x^{n-1} y^k$ in the bivariate rational generating function:
$$\sum_{k=0}^{\infty} g(x) f(x)^k y^k = \frac{g(x)}{1 - y f(x)} \pmod{x^n}.$$
Let us apply Bostan–Mori with respect to $x$ at target exponent $N_0 = n - 1$:
- At recursion level $j = 0$, we have $P_0(x, y) = g(x)$ and $Q_0(x, y) = 1 - y f(x)$, where:
  $$\deg_x P_0, \deg_x Q_0 < N_0 = n, \qquad \deg_y P_0 = 0, \quad \deg_y Q_0 = K_0 = 1.$$
- At recursion level $j$, we maintain $P_j(x, y)$ and $Q_j(x, y)$ with:
  $$\deg_x P_j, \deg_x Q_j < N_j = \left\lceil \frac{n}{2^j} \right\rceil, \qquad \deg_y P_j < K_j = 2^j, \quad \deg_y Q_j \le K_j = 2^j.$$
- **One Step ($j \to j+1$)**:
  Multiply $U_j(x, y) = P_j(x, y) Q_j(-x, y)$ and $V_j(x^2, y) = Q_j(x, y) Q_j(-x, y) \bmod x^{2 N_j}$.
  - The $x$-degree we need after extracting the parity of $N_j$ is **halved**: $N_{j+1} = \lfloor N_j / 2 \rfloor$.
  - The $y$-degree is **doubled**: $\deg_y U_j < 2 K_j = 2^{j+1}$ and $\deg_y V_j \le 2 K_j = 2^{j+1}$.
- **Why Total Complexity is $O(n \log^2 n)$**:
  At every level $j \in \{0, 1, \dots, \lceil \log_2 n \rceil\}$, the total number of coefficients in the 2D polynomial is:
  $$\text{Volume}_j = N_j \cdot K_j \approx \frac{n}{2^j} \cdot 2^j = n!$$
  Thus, every 2D multiplication at level $j$ operates on a 2D grid of total size $O(n)$, costing $O(n \log n)$ via 2D NTT / Kronecker substitution. Across $\log_2 n$ levels, the total time is:
  $$\sum_{j=0}^{\lceil \log_2 n \rceil} O(n \log n) = O(n \log^2 n)!$$
- At the final level $j = \lceil \log_2 n \rceil$, $N_j = 0$, so $x$ has vanished completely: $P_j(0, y)$ and $Q_j(0, y) = 1$ (since $f(0) = 0 \implies Q_0(0, y) = 1 \implies Q_j(0, y) = 1$!) immediately give the answer polynomial $\sum_{k=0}^{n-1} w_k y^k = P_j(0, y) \bmod y^n$!

##### 2. Cohort 1 Blind-Spot Catch: `maspypy`'s Monic $y$-Reversal & Handling $f(0) \neq 0$
- **Why $f(0) = 0$ is crucial**: Since $f(0) = 0$, $[x^0] Q_0(x, y) = 1 - y f(0) = 1$, which implies $[x^0] Q_j(x, y) = 1$ at every level $j$, so **no polynomial inversion is needed at the base case $N_j = 0$**!
- **What if $f(0) = c \neq 0$?**: Write $f(x) = c + \tilde{f}(x)$ with $\tilde{f}(0) = 0$. Compute $\tilde{w}_k = [x^{n-1}] g(x) \tilde{f}(x)^k$ for $0 \le k < n$ using Power Projection on $\tilde{f}$, and then apply a single 1D **Taylor Shift** $W(y) = \widetilde{W}(y + c) \bmod y^n$ in $O(n \log n)$:
  $$w_k = [x^{n-1}] g(x) (c + \tilde{f}(x))^k = \sum_{j=0}^k \binom{k}{j} c^{k-j} \tilde{w}_j.$$
- **`maspypy` Monic $y$-Reversal Optimization**: Instead of storing $Q_j(x, y) = 1 + q_{j,1}(x) y + \cdots + q_{j, K_j}(x) y^{K_j}$ with $K_j + 1$ coefficients in $y$, reverse the $y$-variable by maintaining the monic polynomial $\widetilde{Q}_j(x, y) = y^{K_j} Q_j(x, y^{-1}) = y^{K_j} + \sum_{r=0}^{K_j - 1} \tilde{q}_{j, r}(x) y^r$. Because the leading coefficient $[y^{K_j}] \widetilde{Q}_j(x, y) = 1$ is constant ($1$ at $x=0$ and $0$ for $x^i, i \ge 1$), we only store the lower $K_j = 2^j$ terms in $y$, fitting into an exact power-of-two array of size $2^j$ with zero wasted slots!

##### 3. Problem 2: FPS Composition $h(x) = g(f(x)) \bmod x^n$ via Tellegen's Transposition Principle
Fix $f(x)$ with $f(0) = 0$. Consider the linear map $\mathcal{L}_f : K^n \to K^n$:
$$\mathcal{L}_f(g)_i = [x^i] \sum_{k=0}^{n-1} g_k f(x)^k \quad (\text{FPS Composition}) \quad \Longleftrightarrow \quad \mathcal{L}_f^\top(u)_k = \sum_{i=0}^{n-1} u_i [x^i] f(x)^k = [x^{n-1}] u^{\text{rev}}(x) f(x)^k \quad (\text{Power Projection})!$$
Their shared $n \times n$ matrix has entry $M_{i, k} = [x^i] f(x)^k$. By **Tellegen's Transposition Principle**, transposing the linear dataflow graph of Power Projection reverses the recursion order:
1. **Forward Phase (Compute Denominators $Q_j$)**: Run the exact same denominator squaring $Q_{j+1}(x^2, y) = Q_j(x, y) Q_j(-x, y) \bmod x^{2 N_{j+1}}$ from $j = 0$ up to $L = \lceil \log_2 n \rceil$, storing $Q_0, Q_1, \dots, Q_{L-1}$.
2. **Base Case ($j = L$)**: Load $P_L(0, y) = \sum_{k=0}^{n-1} g_k y^k$.
3. **Backward Transposed Phase ($j = L - 1$ down to $0$)**:
   Given $P_{j+1}(x, y)$ of $x$-degree $< N_{j+1}$ and $y$-degree $< 2 K_j$, spread its coefficients into even/odd $x$-powers according to the parity of $N_j$, and compute the **middle product (transposed multiplication)** with $Q_j(-x, y)$, projecting $\deg_y$ from $2 K_j$ down to $K_j$:
   $$P_j(x, y) = \operatorname{MiddleProd}_y\big( P_{j+1}^{\text{spread}}(x, y),\; Q_j(-x, y) \big).$$
4. **Output ($j = 0$)**: $P_0(x, y)$ has $\deg_y P_0 = 0$ and $\deg_x P_0 < n$; reversing its $x$-coefficients outputs $g(f(x)) \bmod x^n$ in **$O(n \log^2 n)$**!

#### Regime D: Bostan–Christol–Dumas Frobenius Reduction Over Small Prime $\mathbb{F}_p$
When **both** $N, M \le 10^{18}$ are huge and we work over $\mathbb{F}_p$ for a small prime $p$:
- By Freshman's Dream in $\mathbb{F}_p[x, y]$, $Q(x, y)^p = Q(x^p, y^p)$.
- Multiply numerator and denominator by $Q(x, y)^{p-1}$:
  $$\frac{P(x, y)}{Q(x, y)} = \frac{P(x, y) Q(x, y)^{p-1}}{Q(x, y)^p} = \frac{U(x, y)}{Q(x^p, y^p)}, \qquad U(x, y) := P(x, y) Q(x, y)^{p-1} \bmod p.$$
- Let $N = p N' + r_x$ and $M = p M' + r_y$ with $r_x, r_y \in \{0, \dots, p-1\}$. Because $Q(x^p, y^p)$ only contains exponents divisible by $p$, only terms in $U(x, y)$ with $(i, j) \equiv (r_x, r_y) \pmod p$ can contribute to $[x^N y^M]$:
  $$[x^N y^M] \frac{P(x, y)}{Q(x, y)} = [x^{N'} y^{M'}] \frac{U_{r_x, r_y}(x, y)}{Q(x, y)}, \qquad U_{r_x, r_y}(x, y) := \sum_{i, j \ge 0} [x^{p i + r_x} y^{p j + r_y}] U(x, y) \cdot x^i y^j.$$
- Note that $\deg_x U_{r_x, r_y} \le \lfloor \frac{\deg_x P + (p-1)d_x}{p} \rfloor < d_x$ holds as an invariant once $\deg_x P < d_x$ and $\deg_y P < d_y$, running in $\log_p(\max(N, M))$ steps of cost $O(p d_x d_y \log(p d_x d_y))$.

---

### 4.4 Concrete Hand-Checkable Trace of 2D Bostan–Mori ($n = 4$)

Let us trace **Regime C (Power Projection)** by hand for $n = 4$, $g(x) = 1 + x + x^2 + x^3$, and $f(x) = x + 2x^2$, where we want $w_k = [x^3] g(x) f(x)^k$ for $k = 0, 1, 2, 3$:
- **Direct Verification**:
  - $k = 0$: $[x^3] (1 + x + x^2 + x^3) = 1$.
  - $k = 1$: $[x^3] (1 + x + x^2 + x^3)(x + 2x^2) = [x^3](x + 3x^2 + 3x^3 + 3x^4 + 2x^5) = 3$.
  - $k = 2$: $[x^3] (1 + x + x^2 + x^3)(x^2 + 4x^3 + 4x^4) = 1 \cdot 4 + 1 \cdot 1 = 5$.
  - $k = 3$: $[x^3] (1 + x + x^2 + x^3)(x^3 + 6x^4 + \cdots) = 1$.
  - Expected output polynomial: $W(y) = 1 + 3y + 5y^2 + y^3$.
- **Level $j = 0$ ($N_0 = 3$, odd)**:
  - $P_0(x, y) = 1 + x + x^2 + x^3$, $\quad Q_0(x, y) = 1 - y(x + 2x^2) = 1 - xy - 2x^2 y$.
  - $Q_0(-x, y) = 1 + xy - 2x^2 y$.
  - Numerator product $U_0(x, y) = P_0(x, y) Q_0(-x, y) \bmod x^4$:
    $$\begin{aligned}
    U_0(x, y) &= (1 + x + x^2 + x^3)(1 + xy - 2x^2 y) \bmod x^4 \\
    &= 1 + x(1 + y) + x^2(1 - y) + x^3(1 - y).
    \end{aligned}$$
  - Since $N_0 = 3$ is **odd**, extract odd $x$-powers $U_{0,\text{odd}}(x, y)$:
    $$P_1(x, y) = (1 + y) + x(1 - y) \qquad (\deg_x P_1 = 1, \deg_y P_1 = 1).$$
  - Denominator product $V_0(x^2, y) = Q_0(x, y) Q_0(-x, y) = (1 - 2x^2 y)^2 - x^2 y^2 = 1 - x^2(4y + y^2) + 4x^4 y^2$:
    $$Q_1(x, y) = 1 - x(4y + y^2) \pmod{x^2}.$$
- **Level $j = 1$ ($N_1 = \lfloor 3/2 \rfloor = 1$, odd)**:
  - $Q_1(-x, y) = 1 + x(4y + y^2)$.
  - Numerator product $U_1(x, y) = P_1(x, y) Q_1(-x, y) \bmod x^2$:
    $$U_1(x, y) = \big((1 + y) + x(1 - y)\big)\big(1 + x(4y + y^2)\big) \equiv (1 + y) + x\big((1 - y) + (1 + y)(4y + y^2)\big) \pmod{x^2}.$$
  - Since $N_1 = 1$ is **odd**, extract the coefficient of $x^1$:
    $$P_2(0, y) = (1 - y) + (4y + 5y^2 + y^3) = 1 + 3y + 5y^2 + y^3!$$
- **Level $j = 2$ ($N_2 = 0$)**:
  - $W(y) = P_2(0, y) = 1 + 3y + 5y^2 + y^3 \implies (w_0, w_1, w_2, w_3) = (1, 3, 5, 1)$, matching our direct calculation!

---

### 4.5 Failure Modes, Pitfalls & Edge Cases for Iteration 33/85

1. **Passing $\deg_x P \ge \deg_x Q$ into Bostan–Mori**:
   If $\deg_x P \ge \deg_x Q = d$, the invariant $\deg_x P_j < d$ fails on step 1! Always reduce $P = A \bmod Q$ and add $[x^N](A \div Q)$ before starting Bostan–Mori (or in 2D, ensure $\deg_x P < N + 1$ when truncating $\bmod x^{N+1}$).
2. **Calling Kinoshita–Li Power Projection / Composition Without Stripping $f(0) \neq 0$**:
   If $f(0) = c \neq 0$, then $Q_0(0, y) = 1 - c y \neq 1$, so $Q_j(0, y) = (1 - cy)^{2^j} \neq 1$ and the base case requires dividing by $(1 - cy)^{2^L}$. Always decompose $f(x) = c + \tilde{f}(x)$ and apply a 1D Taylor shift of $g(x)$ (for composition: $\tilde{g}(y) = g(y + c)$) or $W(y)$ (for power projection: $W(y) = \widetilde{W}(y + c)$) first!
3. **Truncating $Q_j(x, y)$ Too Aggressively in $x$**:
   When computing $[x^{N_j}] P_j(x, y) / Q_j(x, y)$, both $P_j(x, y)$ and $Q_j(x, y)$ must be kept modulo $x^{N_j + 1}$, and the products $P_j(x, y) Q_j(-x, y)$ and $Q_j(x, y) Q_j(-x, y)$ must be computed modulo $x^{2 N_{j+1} + 2}$ before halving exponents!
---

## 5. Iteration 34 / 86: Constant-Term Extraction $\operatorname{CT}_z$, Diagonal Operator $\operatorname{Diag}_{x,y}$, Furstenberg's Theorem, Kernel Method, and MacMahon's Master Theorem

### 5.1 Diagnostic Signals & Reverse-Engineering Scratchpad

#### A. Diagnostic Signals
1. **Constant-Term / Balanced Step Signal ($\operatorname{CT}_z$)**:
   - **Signal**: A process takes $+1$ and $-1$ steps on a 1D/2D/3D grid and must return to the origin or end at displacement $s$ (**ABC 240 G**, **CF 1264D2**, **LOJ #6728**).
   - **Action**: Encode step displacement as Laurent powers of $z$ and extract $[z^s] S(z)^n = \operatorname{CT}_z\big(z^{-s} S(z)^n\big) = \operatorname{res}_z\big(z^{-s-1} S(z)^n\big)$. In 2D $\ell_1$ walks, rotate coordinates $x + x^{-1} + y + y^{-1} = (u + u^{-1})(v + v^{-1})$ to decouple axes!
2. **Rational Diagonal / Furstenberg Signal ($\operatorname{Diag}_{x,y}$)**:
   - **Signal**: Need $[x^n y^n] \frac{P(x,y)}{Q(x,y)}$ (or $[x^n y^{n+s}]$) for a bivariate rational function whose denominator has $\deg_z(z^d Q(z, t/z)) = 2$ (**Central Binomial**, **Delannoy**, **Yukicoder 1080**, **CF 755G**).
   - **Action**: Substitute $(x, y) \mapsto (z, t/z)$ inside $K((z))[[t]]$, factor the quadratic denominator $-A(t)(z - z_1(t))(z - z_2(t))$ into its unique **small root** $z_1(t) \in t K[[t]]$ and **large root** $z_2(t) \in K((t))$ ($\operatorname{val}_t(z_2) \le 0$), and evaluate the formal residue at $z = z_1(t)$ to obtain an algebraic generating function (D-finite with an $O(N)$ P-recursion!).
3. **Boundary Reflection / Kernel Method Signal**:
   - **Signal**: A walk or queue cannot drop below $0$, producing a functional equation $K(t, u) F(t, u) = A(t, u) + B(t) u^0$ where both $F(t, u)$ and boundary $B(t)$ are unknown.
   - **Action**: Substitute the unique small root $u = u_1(t) \in t K[[t]]$ where the kernel $K(t, u_1(t)) = 0$. Since $F(t, u_1(t))$ converges in $K[[t]]$, the LHS vanishes identically, solving $B(t) = -A(t, u_1(t))$!
4. **MacMahon's Master Theorem (MMT) / Cyclic Product Signal**:
   - **Signal**: Need the diagonal or multi-index coefficient $[x_1^{m_1} \cdots x_d^{m_d}] \prod_{i=1}^d \left(\sum_{j=1}^d a_{ij} x_j\right)^{m_i}$ where the outer exponent $m_i$ of the $i$-th linear form equals the target exponent of $x_i$ (**Dixon's Binomial Identity**, **Permanent vs. Determinant Duality**, **Multi-type Permutation Flow Conservation**).
   - **Action**: Apply MacMahon's Master Theorem to rewrite the coefficient as $[x_1^{m_1} \cdots x_d^{m_d}] \frac{1}{\det(I - X A)}$ where $X = \operatorname{diag}(x_1, \dots, x_d)$, reducing a product of $d$ coupled powers to the inverse of a single $d \times d$ determinant!

#### B. Reverse-Engineering Scratchpad
```
Given [x^n y^k] F(x, y) or [x_1^{m_1} ... x_d^{m_d}] G(x):
 ├─ Is k = n + s (Diagonal or Shifted Diagonal of Rational P(x,y)/Q(x,y))?
 │   └─ Substitute (x, y) -> (z, t/z) in K((z))[[t]]:
 │      [x^n y^{n+s}] F(x,y) = [t^{n+s}] CT_z(z^s F(z, t/z)) = [t^{n+s}] res_z(z^{s-1} F(z, t/z)).
 │      Factor z-denominator -> keep ONLY small roots z_i(t) with val_t(z_i) > 0!
 ├─ Does F(t, u) satisfy K(t, u) F(t, u) = A(t, u) + B(t) (Non-negative prefix constraint)?
 │   └─ Kernel Method: solve K(t, u_1(t)) = 0 for small root u_1(t) in t K[[t]] -> B(t) = -A(t, u_1(t)).
 └─ Is the target [x_1^{m_1} ... x_d^{m_d}] \prod_{i=1}^d (\sum_j a_{ij} x_j)^{m_i}?
     └─ MacMahon's Master Theorem: equals [x_1^{m_1} ... x_d^{m_d}] \det(I - diag(x_1,...,x_d) A)^{-1}!
```

---

### 5.2 Constant-Term Operator $\operatorname{CT}_z$ and Diagonal Operator $\operatorname{Diag}_{x,y}$ in $K((z))[[t]]$

#### Definition 5.1 (Constant-Term, Residue, and Shifted Diagonal Operators)
1. For any formal Laurent series $L(z) = \sum_{k \in \mathbb{Z}} c_k z^k \in K((z))$ (or $K((z))[[t]]$), the **constant-term operator** $\operatorname{CT}_z$ and **formal residue operator** $\operatorname{res}_z$ are:
   $$\operatorname{CT}_z L(z) := [z^0] L(z) = c_0, \qquad \operatorname{res}_z L(z) := [z^{-1}] L(z) = c_{-1} \implies \operatorname{CT}_z L(z) = \operatorname{res}_z\big(z^{-1} L(z)\big).$$
2. For a bivariate formal power series $F(x, y) = \sum_{n, k \ge 0} f_{n, k} x^n y^k \in K[[x, y]]$ and an integer shift $s \in \mathbb{Z}$, the **$s$-shifted diagonal** is:
   $$\operatorname{Diag}_{x, y}^{(s)} F(x, y) := \sum_{n = \max(0, -s)}^{\infty} f_{n, n+s} t^n \in K[[t]] \qquad \big(\text{with } \operatorname{Diag}_{x,y} := \operatorname{Diag}_{x,y}^{(0)}\big).$$

#### Theorem 5.2 (Diagonal-to-Constant-Term & Residue Reduction in $K((z))[[t]]$)
Under the substitution $x = z$ and $y = t / z$, the image of $F(x, y) \in K[[x, y]]$ is
$$F(z, t / z) = \sum_{k=0}^{\infty} \left( \sum_{n=0}^{\infty} f_{n, k} z^{n - k} \right) t^k.$$
Does $F(z, t/z)$ belong to $K((z))[[t]]$?
- **Verification**: For each fixed $k \ge 0$, the coefficient of $t^k$ is $\sum_{n=0}^{\infty} f_{n, k} z^{n - k}$, whose lowest power of $z$ is at least $z^{-k} > -\infty$. Thus $[t^k] F(z, t/z) \in z^{-k} K[[z]] \subset K((z))$, so $F(z, t/z)$ is a **rigorously well-defined element of $K((z))[[t]]$** (whereas it does **not** belong to $K((t))[[z]]$!).
- Extracting $[z^{-s}]$ (or $[z^0]$ after multiplying by $z^s$) inside $K((z))[[t]]$ selects $n - k = -s \iff k = n + s$:
  $$\begin{aligned}
  \operatorname{CT}_z\big( z^s F(z, t/z) \big)
  &= \operatorname{res}_z\big( z^{s-1} F(z, t/z) \big) \\
  &= \sum_{n = \max(0, -s)}^{\infty} f_{n, n+s} t^{n+s} = t^s \operatorname{Diag}_{x, y}^{(s)} F(x, y).
  \end{aligned}$$

---

### 5.3 Small-Root vs. Large-Root Separation & Furstenberg's Theorem (Both Directions)

#### 1. Why Only Small Roots Contribute to $\operatorname{res}_z$ in $K((z))[[t]]$
Suppose we want $\operatorname{Diag}_{x,y} \frac{P(x, y)}{Q(x, y)} = \operatorname{res}_z \frac{P(z, t/z)}{z Q(z, t/z)}$. Over the algebraic closure $\overline{K((t))}$, factor the denominator $z Q(z, t/z)$ into roots $z_i(t)$:
- **Small Roots ($\operatorname{val}_t(z_i(t)) > 0$, i.e., $z_i(t) \in t \overline{K[[t]]}$)**:
  In $K((z))[[t]]$, $t$ is infinitesimal relative to $z$, so $\frac{1}{z - z_i(t)}$ expands as:
  $$\frac{1}{z - z_i(t)} = \frac{1}{z} \cdot \frac{1}{1 - z_i(t)/z} = \sum_{m=0}^{\infty} z_i(t)^m z^{-m-1} \in K((z))[[t]],$$
  which has formal residue $\operatorname{res}_z \frac{1}{z - z_i(t)} = [z^{-1}] \frac{1}{z - z_i(t)} = 1$! More generally, for any simple small root $z_1(t)$ of $D(z, t) := z Q(z, t/z)$:
  $$\operatorname{res}_{z = z_1(t)} \frac{N(z, t)}{D(z, t)} = \frac{N(z_1(t), t)}{(\partial_z D)(z_1(t), t)}.$$
- **Large Roots ($\operatorname{val}_t(z_j(t)) \le 0$ and $z_j(0) \neq 0$)**:
  Because $\operatorname{val}_t(1 / z_j(t)) \ge 0$, the factor $\frac{1}{z - z_j(t)}$ expands in $K((z))[[t]]$ as a pure Taylor series in $z \ge 0$:
  $$\frac{1}{z - z_j(t)} = -\frac{1}{z_j(t)} \cdot \frac{1}{1 - z / z_j(t)} = -\sum_{m=0}^{\infty} \frac{z^m}{z_j(t)^{m+1}} \in K[[z, t]],$$
  which contains **no negative powers of $z$** ($[z^{-1}] = 0$) and therefore contributes **$0$** to the formal residue!

#### Theorem 5.3 (Furstenberg's Theorem — Forward & Converse Directions)
1. **Forward Direction (Bivariate Rational Diagonal $\implies$ Univariate Algebraic)**:
   For the general quadratic rational generating function $F(x, y) = \frac{1}{1 - ax - by - cxy}$, substituting $(x, y) \mapsto (z, t/z)$ inside $K((z))[[t]]$ yields:
   $$\begin{aligned}
   \operatorname{Diag}_{x,y} \frac{1}{1 - ax - by - cxy}
   &= \operatorname{res}_z \frac{1}{z\big(1 - az - b(t/z) - ct\big)} && \text{(Apply Theorem 5.2 with } s = 0\text{)} \\
   &= \operatorname{res}_z \frac{1}{-a z^2 + (1 - ct)z - bt} && \text{(Multiply denominator through by } z\text{)} \\
   &= \operatorname{res}_z \frac{1}{-a \big(z - z_1(t)\big)\big(z - z_2(t)\big)},
   \end{aligned}$$
   where the two roots of $-a z^2 + (1 - ct)z - bt = 0$ are:
   $$z_1(t) = \frac{(1 - ct) - \sqrt{(1 - ct)^2 - 4abt}}{2a} = bt + O(t^2) \quad (\text{small root, } \operatorname{val}_t(z_1) = 1 > 0),$$
   $$z_2(t) = \frac{(1 - ct) + \sqrt{(1 - ct)^2 - 4abt}}{2a} = \frac{1}{a} + O(t) \quad (\text{large root, } \operatorname{val}_t(z_2) = 0 \le 0).$$
   Extracting the residue at the unique small root $z = z_1(t)$ gives:
   $$\operatorname{Diag}_{x,y} \frac{1}{1 - ax - by - cxy} = \frac{1}{-a\big(z_1(t) - z_2(t)\big)} = \frac{1}{\sqrt{(1 - ct)^2 - 4abt}}!$$
   - **Special Case 1 (Central Binomial Coefficients, $a = b = 1, c = 0$)**:
     $$\operatorname{Diag}_{x,y} \frac{1}{1 - x - y} = \sum_{n=0}^{\infty} \binom{2n}{n} t^n = \frac{1}{\sqrt{1 - 4t}}, \qquad (n+1) d_{n+1} = 2(2n+1) d_n.$$
   - **Special Case 2 (Central Delannoy Numbers, $a = b = c = 1$)**:
     $$\operatorname{Diag}_{x,y} \frac{1}{1 - x - y - xy} = \sum_{n=0}^{\infty} D_n t^n = \frac{1}{\sqrt{1 - 6t + t^2}}, \qquad (n+1) D_{n+1} = 3(2n+1) D_n - n D_{n-1}.$$

2. **Converse Direction (Every Algebraic Series is a Rational Diagonal — Furstenberg 1967, Cohort 2 Catch)**:
   Conversely, let $A(t) \in K[[t]]$ be **any** algebraic formal power series with $A(0) = 0$, satisfying a polynomial equation $E(t, A(t)) = 0$ where $E(0, 0) = 0$ and $(\partial_y E)(0, 0) \neq 0$.
   By the Implicit Function Theorem, $y = A(t)$ is the **unique small root** ($\operatorname{val}_t(A(t)) \ge 1$) of $y \mapsto E(t, y)$. Therefore, inside $K((y))[[t]]$, the formal residue of $\frac{y (\partial_y E)(t, y)}{E(t, y)}$ at $y = A(t)$ is $A(t) \cdot 1 = A(t)$!
   Setting $t = xy$ and converting $\operatorname{res}_y \mapsto \operatorname{Diag}_{x, y}$ gives **Furstenberg's Converse Formula**:
   $$A(t) = \operatorname{res}_y \frac{y (\partial_y E)(t, y)}{E(t, y)} = \operatorname{Diag}_{x, y}\left( \frac{y^2 (\partial_y E)(xy, y)}{E(xy, y)} \right)!$$

#### 3. Formal Residue Integration by Parts & D-Finite Horizontal ODE (Cohort 1 Catch — CF 755G)
Because the formal residue of any exact derivative is zero ($\operatorname{res}_z \partial_z G(z) = [z^{-1}] \sum k g_k z^{k-1} = 0$), formal residues satisfy **integration by parts**:
$$\operatorname{res}_z\big( U'(z) V(z) \big) = -\operatorname{res}_z\big( U(z) V'(z) \big).$$
In **CF 755G**, $f_{n, k} = [x^n y^k] \frac{1}{1 - (1+y)x - y x^2}$. By Furstenberg's quadratic root extraction in $x$, the generating function of the $n$-th row $R_n(y) := \sum_{k=0}^n f_{n, k} y^k$ is the coefficient $[x^n] \frac{1}{1 - x - xy(1+x)}$, which satisfies the exact **second-order D-finite differential equation** with polynomial coefficients of degree $2$ in $y$:
$$y(1 - 6y + y^2) R_n''(y) + \big(1 - 3(n+2)y + (n+2)y^2\big) R_n'(y) + \frac{n(n+1)}{2}(1 - y) R_n(y) = 0.$$
Extracting $[y^{k-1}]$ from this ODE immediately yields a **4-term horizontal recurrence of polynomial degree 2** ($O(k)$ total time for fixed $n$):
$$k^2 f_{n, k} = \left(6(k-1)^2 + 3(n+2)(k-1) - \frac{n(n+1)}{2}\right) f_{n, k-1} - \left((k-2)(k+n-1) + \frac{n(n+1)}{2}\right) f_{n, k-2} + (k-3)(k-2) f_{n, k-3}.$$
Equivalently, eliminating $f_{n, k-3}$ via creative telescoping / residue integration by parts on $f_{n,k} = \operatorname{res}_x \frac{x^{-n-1}(x + x^2)^k}{(1-x)^{k+1}}$ yields the compact **3-term horizontal recurrence of polynomial degree 3**:
$$k(n + 2 - k)(2n + 3 - 2k) f_{n, k} = (2n + 1 - 2k)\big(3k(n + 1 - k) + n(n + 1)\big) f_{n, k-1} + (k - 1)(n + k)(2n + 3 - 2k) f_{n, k-2}!$$

---

### 5.4 The Kernel Method in $K((u))[[t]]$ (One- and Two-Boundary Regimes)

1. **One-Boundary Kernel Method**:
   Consider a step polynomial $S(u) = \sum_{j = -b}^{a} s_j u^j \in K[u, u^{-1}]$ with $b \ge 1$ and $s_{-b} \neq 0$, counting non-negative walks where negative steps past $0$ are forbidden. Multiplying by $u^b$ gives the kernel equation in $K[u][[t]]$:
   $$K(t, u) F(t, u) = u^b - t \sum_{r=0}^{b-1} F_r(t) U_r(u), \qquad K(t, u) := u^b - t u^b S(u).$$
   By Newton–Puiseux / Hensel's Lemma, since $K(0, u) = u^b$ has a root of multiplicity $b$ at $u = 0$, the equation $K(t, u) = 0$ has **exactly $b$ small roots** $u_1(t), \dots, u_b(t)$ in $\overline{K}[[t^{1/b}]]$ with $\operatorname{val}_t(u_i(t)) = 1/b > 0$ (and $a$ large roots with $\operatorname{val}_t < 0$).
   Substituting the $b$ small roots $u = u_1(t), \dots, u_b(t)$ makes the LHS $K(t, u_i(t)) F(t, u_i(t)) = 0$, giving a system of $b$ independent linear equations that uniquely determine all $b$ boundary series $F_0(t), \dots, F_{b-1}(t)$!
2. **Two-Boundary Kernel Method (Walks in a Bounded Strip $[0, H]$) & Rigorous Convergence Proof**:
   If walks are confined to $0 \le k \le H$ with step polynomial $S(u) = u^{-1} + c + u$, the kernel $K(t, u) = u - t(1 + cu + u^2)$ has one small root $u_1(t) = t + c t^2 + \dots \in t K[[t]]$ ($\operatorname{val}_t(u_1) = 1 > 0$) and one large root $u_2(t) = 1/u_1(t) = t^{-1} - c + \dots \in t^{-1} K[[t]]$ ($\operatorname{val}_t(u_2) = -1 < 0$), swapped by the **Vieta involution** $u \mapsto u^{-1}$.
   - **Why substituting the large root $u_2(t)$ is illegal in One-Boundary walks but 100% rigorous in Two-Boundary walks**:
     In the One-Boundary regime, $F(t, u) = \sum_{n=0}^{\infty} t^n \left(\sum_{k=0}^{n} f_{n,k} u^k\right)$ has unbounded $u$-degree $\deg_u([t^n] F) = n$, so substituting $u_2(t) = t^{-1} + O(1)$ produces terms $f_{n,k} t^{n-k}$ where $n - k = 0$ occurs for **infinitely many** pairs $(n, n)$, causing $\sum_{n=0}^\infty f_{n,n}$ to diverge in the $(t)$-adic topology!
     In the **Two-Boundary regime**, however, the height of every walk is strictly bounded by $H$, so $F(t, u) = \sum_{k=0}^{H} F_k(t) u^k \in K[u][[t]]$ is a **polynomial in $u$ of fixed degree $H$** with coefficients $F_k(t) \in K[[t]]$. Therefore, substituting any Laurent series $u(t) \in K((t))$ (even with $\operatorname{val}_t(u(t)) = -1$) involves only the **finite sum** $\sum_{k=0}^H F_k(t) u(t)^k \in t^{-H} K[[t]] \subset K((t))$, which converges trivially term-by-term in $K((t))$! Substituting both $u_1(t)$ and $u_2(t) = u_1(t)^{-1}$ into the two-boundary kernel equation
     $$(1 - t S(u)) F(t, u) = 1 - t u^{-1} F_0(t) - t u^{H+1} F_H(t)$$
     gives a $2 \times 2$ linear system in $K((t))$ for the bottom boundary $F_0(t)$ and top boundary $F_H(t)$, recovering the rational generating function $\frac{U_H((1-ct)/(2t))}{U_{H+1}((1-ct)/(2t))}$ (**UOJ #424**)!
3. **Quarter-Plane Kernel Method & Dihedral Group of the Walk (Kreweras Walks Trace — Bousquet-Mélou & Mishna 2010)**:
   Consider **Kreweras walks** in the quarter plane $\mathbb{Z}_{\ge 0}^2$ starting at $(0, 0)$ with step set $\mathcal{S} = \{(-1, 0), (0, -1), (1, 1)\}$ and inventory $S(x, y) = \bar{x} + \bar{y} + xy$. Multiplying the functional equation by $xy$ gives the **Quarter-Plane Kernel Equation** in $K[x, y][[t]]$:
   $$K(x, y; t) Q(x, y; t) = xy - t y Q(0, y; t) - t x Q(x, 0; t), \qquad K(x, y; t) := xy\big(1 - t(\bar{x} + \bar{y} + xy)\big) = xy - t(x + y + x^2 y^2).$$
   - **Dihedral Group $G(\mathcal{S}) \cong D_6$ of the Kernel**:
     The step polynomial $S(x, y) = \bar{x} + \bar{y} + xy$ is invariant under two birational involutions:
     $$\Phi(x, y) := (\bar{x} \bar{y}, y), \qquad \Psi(x, y) := (x, \bar{x} \bar{y}),$$
     which generate the **dihedral group of order 6** ($D_6 \cong \mathfrak{S}_3$) acting on the orbit of $(x, y)$:
     $$(x, y) \xrightarrow{\Phi} (\bar{x}\bar{y}, y) \xrightarrow{\Psi} (\bar{x}\bar{y}, x) \xrightarrow{\Phi} (y, x) \xrightarrow{\Psi} (y, \bar{x}\bar{y}) \xrightarrow{\Phi} (x, \bar{x}\bar{y}) \xrightarrow{\Psi} (x, y).$$
   - **Orbit-Sum Elimination & Positive-Part Extraction**:
     Notice that in the kernel equation $K(x, y; t) Q(x, y; t) / (xy) = 1 - t \bar{x} Q(0, y; t) - t \bar{y} Q(x, 0; t)$, each boundary term $-t \bar{x} Q(0, y; t)$ or $-t \bar{y} Q(x, 0; t)$ is decoupled along one coordinate. Substituting the small algebraic root $y = Y_0(x; t) = t + t x + O(t^2)$ of $K(x, y; t) = 0$ (and its $\Phi$-conjugate) eliminates $Q(x, y; t)$ and produces an algebraic equation for $Q(x, 0; t)$, proving Kreweras's theorem (1965):
     $$[t^{3m}] Q(0, 0; t) = \frac{4^m}{(m+1)(2m+1)} \binom{3m}{m}!$$

---

### 5.5 MacMahon's Master Theorem (MMT), Permanent/Determinant Duality, and Dixon's Identity (Cohort 3 Gap-Hunting Addition)

Both Cohort 1 and Cohort 2 omitted **MacMahon's Master Theorem (1915)**—the crown jewel of multivariate diagonal coefficient extraction that bridges products of linear forms, matrix permanents, matrix determinants, and hypergeometric binomial identities.

#### Theorem 5.4 (MacMahon's Master Theorem — Percy Alexander MacMahon, 1915)
Let $A = (a_{ij})_{1 \le i, j \le d}$ be a $d \times d$ matrix over a commutative ring $K$, let $x_1, \dots, x_d$ be formal indeterminates, and let $X = \operatorname{diag}(x_1, \dots, x_d)$. For each $1 \le i \le d$, define the linear form
$$L_i(x_1, \dots, x_d) := \sum_{j=1}^d a_{ij} x_j.$$
Then for every tuple of non-negative integers $(m_1, \dots, m_d) \in \mathbb{Z}_{\ge 0}^d$, the coefficient of $x_1^{m_1} \cdots x_d^{m_d}$ in the product $\prod_{i=1}^d L_i(x_1, \dots, x_d)^{m_i}$ equals the coefficient of $x_1^{m_1} \cdots x_d^{m_d}$ in the reciprocal determinant $\det(I_d - X A)^{-1}$:
$$[x_1^{m_1} \cdots x_d^{m_d}] \prod_{i=1}^d \left( \sum_{j=1}^d a_{ij} x_j \right)^{m_i} = [x_1^{m_1} \cdots x_d^{m_d}] \frac{1}{\det(I_d - X A)}.$$

#### Proof 1: Algebraic Proof via the Multivariate Jacobi Residue Formula (Multivariate Lagrange–Good Inversion)
Consider the change of variables $u_i = x_i - t_i L_i(x_1, \dots, x_d)$ where we want the diagonal coefficient where $t_i$ matches $m_i$. Even more directly, write the target coefficient as an iterated formal residue in $x_1, \dots, x_d$:
$$\begin{aligned}
[x_1^{m_1} \cdots x_d^{m_d}] \prod_{i=1}^d L_i(\mathbf{x})^{m_i}
&= \operatorname{res}_{x_1, \dots, x_d} \left( \prod_{i=1}^d \frac{L_i(\mathbf{x})^{m_i}}{x_i^{m_i + 1}} \right) \\
&= [t_1^{m_1} \cdots t_d^{m_d}] \operatorname{res}_{x_1, \dots, x_d} \left( \prod_{i=1}^d \frac{1}{x_i - t_i L_i(\mathbf{x})} \right) && \text{(Since } \frac{1}{x_i - t_i L_i} = \sum_{m_i \ge 0} t_i^{m_i} \frac{L_i(\mathbf{x})^{m_i}}{x_i^{m_i+1}}\text{)}.
\end{aligned}$$
Now apply the linear change of variables $y_i = x_i - t_i L_i(\mathbf{x}) = \sum_{j=1}^d (\delta_{ij} - t_i a_{ij}) x_j$, i.e., $\mathbf{y} = (I_d - T A) \mathbf{x}$ where $T = \operatorname{diag}(t_1, \dots, t_d)$.
Its Jacobian matrix is $\frac{\partial(y_1, \dots, y_d)}{\partial(x_1, \dots, x_d)} = I_d - T A$, whose determinant is $\det(I_d - T A)$ (a constant with respect to $\mathbf{x}$!). By the **Multivariate Formal Jacobi Residue Formula** ($\operatorname{res}_{\mathbf{y}} \prod_{i=1}^d y_i^{-1} dy_1 \wedge \cdots \wedge dy_d = 1$):
$$\operatorname{res}_{x_1, \dots, x_d} \left( \det(I_d - T A) \prod_{i=1}^d \frac{1}{y_i(\mathbf{x})} \right) = 1 \implies \operatorname{res}_{x_1, \dots, x_d} \left( \prod_{i=1}^d \frac{1}{x_i - t_i L_i(\mathbf{x})} \right) = \frac{1}{\det(I_d - T A)}!$$
Extracting $[t_1^{m_1} \cdots t_d^{m_d}]$ and renaming $t_i \mapsto x_i$ yields MacMahon's Master Theorem!

#### Proof 2: Combinatorial Proof via Foata's Cycle-Decomposition Bijection (Why Permanents and Determinants Are Dual!)
- **Left-Hand Side**: Expanding $\prod_{i=1}^d \left(\sum_{j=1}^d a_{ij} x_j\right)^{m_i}$, the coefficient $[x_1^{m_1} \cdots x_d^{m_d}]$ is the sum of weights of all directed multigraphs (or **balanced flows**) on vertices $\{1, \dots, d\}$ where vertex $i$ has **out-degree $m_i$** and **in-degree $m_i$**, with ordered outgoing edges from each vertex $i$.
- **Right-Hand Side**: By the Cycle-Collection expansion of a determinant, $\det(I_d - X A) = \sum_{\sigma \in S_d} \operatorname{sgn}(\sigma) \prod_{i=1}^d (I - X A)_{i, \sigma(i)} = \sum_{\mathcal{C}} (-1)^{|\mathcal{C}|} w(\mathcal{C})$, where $\mathcal{C}$ ranges over collections of **vertex-disjoint directed cycles** in the weighted digraph $X A$.
- By the Inclusion–Exclusion / Viennot heaps of pieces / Foata bijection (treating directed cycles as Lyndon words), the reciprocal $\frac{1}{\det(I_d - X A)} = \exp\left(\sum_{C \text{ directed cycle}} \frac{w(C)}{|\operatorname{Aut}(C)|}\right)$ generates multisets of directed cycles, which biject onto balanced directed Eulerian flows with out-degree = in-degree = $m_i$ at every vertex $i$!

#### Corollary 5.5 (Permanent vs. Determinant Duality)
Setting $m_1 = m_2 = \cdots = m_d = 1$ in MacMahon's Master Theorem:
$$\operatorname{perm}(A) := \sum_{\sigma \in S_d} \prod_{i=1}^d a_{i, \sigma(i)} = [x_1 x_2 \cdots x_d] \prod_{i=1}^d \left( \sum_{j=1}^d a_{ij} x_j \right) = [x_1 x_2 \cdots x_d] \frac{1}{\det(I_d - X A)}!$$
In the language of quantum physics and combinatorics:
- **Fermions (Antisymmetric / Exterior Algebra)**: $[x_1 \cdots x_d] \det(I_d + X A) = \det(A)$.
- **Bosons (Symmetric Algebra)**: $[x_1 \cdots x_d] \det(I_d - X A)^{-1} = \operatorname{perm}(A)$.

#### Concrete Hand-Checkable $2 \times 2$ Trace of MacMahon's Master Theorem
Let $d = 2$ and $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Let us verify MMT for $(m_1, m_2) = (2, 1)$:
- **LHS (Direct Binomial Expansion)**:
  $$[x_1^2 x_2^1] (a x_1 + b x_2)^2 (c x_1 + d x_2)^1 = [x_1^2 x_2^1] (a^2 x_1^2 + 2ab x_1 x_2 + b^2 x_2^2)(c x_1 + d x_2) = a^2 d + 2ab c.$$
- **RHS (Reciprocal Determinant)**:
  $$\det(I_2 - X A) = \det\begin{pmatrix} 1 - a x_1 & -b x_1 \\ -c x_2 & 1 - d x_2 \end{pmatrix} = (1 - a x_1)(1 - d x_2) - bc x_1 x_2 = 1 - a x_1 - d x_2 + (ad - bc) x_1 x_2.$$
  Expanding $\frac{1}{\det(I_2 - X A)} = \frac{1}{(1 - a x_1)(1 - d x_2) - bc x_1 x_2}$ as a geometric series in $bc x_1 x_2$:
  $$\frac{1}{(1 - a x_1)(1 - d x_2)} + \frac{bc x_1 x_2}{(1 - a x_1)^2 (1 - d x_2)^2} + O(x_1^2 x_2^2).$$
  Extracting $[x_1^2 x_2^1]$ gives:
  $$a^2 d + bc \cdot ([x_1^1](1 - a x_1)^{-2}) \cdot ([x_2^0](1 - d x_2)^{-2}) = a^2 d + bc (2a)(1) = a^2 d + 2abc,$$
  which matches the LHS term-for-term!

#### Canonical Application: I. J. Good's 3-Variable MMT Proof of Dixon's Binomial Identity
**Theorem (Dixon's Identity, 1891 / I. J. Good, 1962)**: For every integer $n \ge 0$,
$$\sum_{k=0}^{2n} (-1)^k \binom{2n}{k}^3 = (-1)^n \frac{(3n)!}{(n!)^3}.$$
**Zero-Magic-Steps Proof via MacMahon's Master Theorem**:
1. Observe that $\sum_{k=0}^{2n} (-1)^k \binom{2n}{k}^3$ is the diagonal coefficient $[x^{2n} y^{2n} z^{2n}]$ of the product of three differences:
   $$\begin{aligned}
   (y - z)^{2n} (z - x)^{2n} (x - y)^{2n}
   &= \sum_{i=0}^{2n} (-1)^{2n-i} \binom{2n}{i} y^i z^{2n-i} \sum_{j=0}^{2n} (-1)^{2n-j} \binom{2n}{j} z^j x^{2n-j} \sum_{k=0}^{2n} (-1)^{2n-k} \binom{2n}{k} x^k y^{2n-k}.
   \end{aligned}$$
   In this product, to get $x^{2n} y^{2n} z^{2n}$, we must have:
   - Exponent of $x$: $(2n - j) + k = 2n \implies j = k$.
   - Exponent of $y$: $i + (2n - k) = 2n \implies i = k$.
   - Exponent of $z$: $(2n - i) + j = 2n - k + k = 2n$ (automatically satisfied!).
   - Sign: $(-1)^{(2n-k) + (2n-k) + (2n-k)} = (-1)^{6n - 3k} = (-1)^k$.
   Therefore:
   $$\sum_{k=0}^{2n} (-1)^k \binom{2n}{k}^3 = [x^{2n} y^{2n} z^{2n}] (y - z)^{2n} (z - x)^{2n} (x - y)^{2n}!$$
2. Now apply **MacMahon's Master Theorem** with $d = 3$, $(m_1, m_2, m_3) = (2n, 2n, 2n)$, and the skew-symmetric matrix
   $$A = \begin{pmatrix} 0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0 \end{pmatrix} \implies \begin{pmatrix} L_1 \\ L_2 \\ L_3 \end{pmatrix} = A \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} y - z \\ z - x \\ x - y \end{pmatrix}.$$
3. Compute the $3 \times 3$ determinant $\det(I_3 - X A)$:
   $$\det(I_3 - X A) = \det\begin{pmatrix} 1 & -x & x \\ y & 1 & -y \\ -z & z & 1 \end{pmatrix} = 1 + (xy + yz + zx)!$$
   Notice that all linear terms and the cubic term $xyz \det(A)$ vanish because $A$ is skew-symmetric with zero diagonal and rank $2$ ($\det A = 0$)!
4. By MacMahon's Master Theorem:
   $$\begin{aligned}
   \sum_{k=0}^{2n} (-1)^k \binom{2n}{k}^3
   &= [x^{2n} y^{2n} z^{2n}] \frac{1}{1 + xy + yz + zx} \\
   &= [x^{2n} y^{2n} z^{2n}] \sum_{m=0}^{\infty} (-1)^m (xy + yz + zx)^m.
   \end{aligned}$$
   Since $xy + yz + zx$ is homogeneous of degree $2$, only $m = 3n$ can produce total degree $6n$, and in $(xy + yz + zx)^{3n} = \sum_{a+b+c=3n} \frac{(3n)!}{a! b! c!} x^{a+c} y^{a+b} z^{b+c}$, matching $x^{2n} y^{2n} z^{2n}$ requires $a + c = a + b = b + c = 2n \iff a = b = c = n$!
   Hence:
   $$\sum_{k=0}^{2n} (-1)^k \binom{2n}{k}^3 = (-1)^{3n} \frac{(3n)!}{n! n! n!} = (-1)^n \frac{(3n)!}{(n!)^3}. \quad \blacksquare$$

---

### 5.6 Failure Modes, Pitfalls & Edge Cases for Iteration 34/86

1. **The Doubly-Infinite Laurent Space $K[[z, z^{-1}]]$ Associativity Disaster**:
   The space $K[[z, z^{-1}]]$ of doubly-infinite formal series $\sum_{n \in \mathbb{Z}} a_n z^n$ is a $K[z, z^{-1}]$-module, **not a ring**! Even when pairwise products are individually well-defined, multiplication fails to be associative: let
   $$A(z) = \sum_{n=-\infty}^{\infty} z^n \in K[[z, z^{-1}]], \qquad B(z) = 1 - z \in K[z], \qquad C_+(z) = \sum_{n=0}^{\infty} z^n \in K[[z]].$$
   Each adjacent product has only finitely many terms contributing to each power of $z$, yet:
   $$\big(A(z) \cdot B(z)\big) \cdot C_+(z) = \left(\sum_{n \in \mathbb{Z}} (1 - 1) z^n\right) \cdot C_+(z) = 0 \cdot C_+(z) = 0,$$
   whereas
   $$A(z) \cdot \big(B(z) \cdot C_+(z)\big) = A(z) \cdot 1 = \sum_{n=-\infty}^{\infty} z^n \neq 0!$$
   Even worse, $B(z) = 1 - z$ has *two distinct inverses* depending on the chosen ring: $C_+(z) = \sum_{n \ge 0} z^n \in K[[z]]$ and $C_-(z) = -\sum_{n \le -1} z^n \in K((z^{-1}))$, whose difference is the zero-divisor $C_+(z) - C_-(z) = A(z)$ annihilated by $1 - z$. All constant-term and residue manipulations **must** take place inside $K((z))[[t]]$, where every coefficient of $t^k$ is a formal Laurent series with bounded negative degree in $z$.
2. **Including Large Roots in Formal Residue Extraction**:
   When computing $\operatorname{res}_z \frac{N(z,t)}{D(z,t)}$ in $K((z))[[t]]$, summing over *all* roots of $D(\cdot, t)$ gives $0$ (or $-\operatorname{res}_{z=\infty}$) by the global residue theorem! You must sum **strictly over the small roots** $z_i(t)$ satisfying $\operatorname{val}_t(z_i(t)) > 0$ ($\lim_{t \to 0} z_i(t) = 0$).
3. **Applying MacMahon's Master Theorem with Mismatched Exponents**:
   MMT applies to $[x_1^{m_1} \cdots x_d^{m_d}] \prod_{i=1}^d L_i(\mathbf{x})^{k_i}$ **only when $k_i = m_i$ for every $i$**! If $k_i = m_i + s_i$ has small constant offsets $s_i \in \mathbb{Z}$, split $\prod L_i^{m_i + s_i} = \left(\prod L_i^{s_i}\right) \prod L_i^{m_i}$ (if $s_i \ge 0$) or apply the Multivariate Jacobi Residue Formula directly to $\operatorname{res}_{\mathbf{x}} \prod_i \frac{L_i(\mathbf{x})^{k_i}}{x_i^{m_i+1}}$.
---

## 6. Iteration 35 / 87: Master Curated Problem Bank (28 Reconciled Problems Across 4 Tiers)

Every unique non-template problem discovered by Cohort 1 (18 problems) and Cohort 2 (18 problems) has been preserved and cross-reconciled below (9 overlapping problems merged with dual insights + 9 Cohort-1-only + 9 Cohort-2-only + 1 Cohort-3 MMT/Frobenius addition = **28 curated problems**).

### Master Problem Overview Matrix

| # | Tier | Problem & Source | Cohort Origin | Primary Wave 4A Technique | Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P1** | `Stepping Stone` | **AtCoder Typical 90 #065 — RGB Balls 2** | Cohort 2 | 3-Variable Sum Constraint Decoupling ($r+g+b=K$) | $O(K \log K)$ |
| **P2** | `Stepping Stone` | **AtCoder ABC 276 G — Count Strictly Increasing Sequences** | Cohort 1 & 2 | Difference Variables + Primary-Variable Swap | $O(N + M)$ |
| **P3** | `Stepping Stone` | **AtCoder ABC 300 Ex — Fibonacci: Revisited** | Cohort 1 & 2 | Submask-Sum 1D Bostan–Mori ($\mathcal{E}$ vs. $\mathcal{E}+\mathcal{O}$) | $O(K \log K \log N)$ |
| **P4** | `Stepping Stone` | **Codeforces 1117D — Magic Gems (Large $M$ Regime)** | Cohort 2 | 1D Bostan–Mori on $[x^N] \frac{1}{1 - x - x^M}$ | $O(M \log M \log N)$ |
| **P5** | `Stepping Stone` | **AtCoder ABC 240 G — Teleporting Takahashi** | Cohort 1 | 3D $\operatorname{CT}_{x,y,z}$ + 2D $\ell_1$ Walk Rotation $(u+u^{-1})(v+v^{-1})$ | $O(N)$ |
| **P6** | `Stepping Stone` | **Codeforces 623E — Transforming Sequence** | Cohort 1 & 2 | Bivariate EGF Twisted Doubling $F_{a+b}(x) = F_a(2^b x) F_b(x)$ | $O(k \log k \log n)$ |
| **P7** | `Intermediate` | **Codeforces 960G — Bandit Blues** | Cohort 2 | Bivariate Stirling GF Decoupled via $z = x+y$ | $O(n \log^2 n)$ |
| **P8** | `Intermediate` | **Luogu P5406 — [THUPC2019] 找树** | Cohort 1 | $w$-Variate Bitwise FWT Evaluation–Interpolation + Matrix-Tree | $O(2^w n^3)$ |
| **P9** | `Intermediate` | **Luogu P5339 — [TJOI2019] 唱、跳、rap和篮球** | Cohort 2 | 4-Variate EGF Diagonal Inclusion–Exclusion on $u = x_1 x_2 x_3 x_4$ | $O(N^2 \log N)$ |
| **P10** | `Intermediate` | **AtCoder ABC 279 Ex — Sum of Prod of Min** | Cohort 1 | Rational Product + Euler Pentagonal Theorem + Lucas | $O(P + \sqrt{M-N} \log_P M)$ |
| **P11** | `Intermediate` | **AtCoder AGC 013 E — Placing Squares ($K$-Moment Generalization)** | Cohort 2 | Eulerian Polynomial Rational OGF + 1D Bostan–Mori | $O(K \log K \log N)$ |
| **P12** | `Intermediate` | **Codeforces 1264D2 — Beautiful Bracket Sequence (hard)** | Cohort 1 | Balanced Split-Point Depth via $\operatorname{CT}_z$ Vandermonde Identity | $O(n)$ |
| **P13** | `Intermediate` | **UOJ #424 — 【集训队作业2018】count** | Cohort 1 & 2 | Bounded-Height Dyck Paths + Two-Boundary Kernel / Bostan–Mori | $O(m \log m \log n)$ |
| **P14** | `Intermediate` | **Codeforces 755G — PolandBall and Many Other Balls** | Cohort 1 & 2 | Bivariate Rational GF: Polynomial Doubling vs. D-Finite ODE | $O(k \log k \log n)$ or $O(k)$ |
| **P15** | `Advanced` | **AtCoder AGC 058 D — Yet Another ABC String** | Cohort 1 & 2 | 3-Variate Goulden–Jackson GF Decoupled via $u = xyz$ | $O(A+B+C)$ |
| **P16** | `Advanced` | **Codeforces 1553I — Stairs** | Cohort 1 | Bivariate D&C Matrix Contraction in $K[y][[x]]$ | $O(n \log^2 n)$ |
| **P17** | `Advanced` | **Codeforces 1336E2 — Chiori and Doll Picking (hard)** | Cohort 1 | MacWilliams / Walsh–Hadamard Duality via Krawtchouk Decoupling | $O(2^{\min(k, m-k)} + m^3)$ |
| **P18** | `Advanced` | **Luogu P5487 — [BJOI2019] 勘破神机** | Cohort 1 | Stirling Power Expansion + $\mathbb{F}_p[\sqrt{d}]$ Rational Sum | $O(k^2 \log R)$ |
| **P19** | `Advanced` | **Codeforces 1349F1/F2 — Slime and Sequences** | Cohort 2 | Bivariate Eulerian Mixed EOGF $u=(y-1)x$ + Residue Substitution | $O(n \log n)$ |
| **P20** | `Advanced` | **QOJ #4815 — Bivariate Walk with Bounded Height & Weight** | Cohort 2 | Regime A/B 2D Bostan–Mori in $(K[y]/(y^{K+1}))[[x]]$ | $O(d K \log(dK) \log N)$ |
| **P21** | `Advanced` | **AtCoder ABC 387 G — Prime Circuit** | Cohort 2 | Prime-Cycle Cactus EGF + Kinoshita–Li 2D Bostan–Mori Inverse | $O(N \log N)$ / $O(N \log^2 N)$ |
| **P22** | `Advanced` | **Yukicoder No. 1080 / Luogu P6667 — Generalized Delannoy Diagonal** | Cohort 1 & 2 | Furstenberg Diagonal $\operatorname{CT}_z F(z, t/z)$ + 3-Term P-Recursion | $O(N)$ |
| **P23** | `Mastery` | **AtCoder ARC 154 F — Dice Game** | Cohort 1 | Coupon Collector Rational OGF + D&C Evaluation $P(e^z) \bmod z^{M+1}$ | $O((N+M)\log^2(N+M))$ |
| **P24** | `Mastery` | **UOJ #596 — 【集训队互测2021】三维立体混元劲** | Cohort 1 & 2 | 3D Twisted Kronecker $\chi$-Graded FPS $\ln G(x,y,z)$ + Radial $\mathfrak{D}$ | $O(3 ABC \log(ABC))$ |
| **P25** | `Mastery` | **yukicoder No. 1783 — Remix Sum** | Cohort 1 | Hybrid $(K-T)$-D Radix-10 DFT ($\bmod 120586241$) + $T$-D Kronecker $\operatorname{pow}$ | $O(10^K K^2 \log K)$ |
| **P26** | `Mastery` | **AtCoder ARC 138 F / QOJ #8528 — FPS Composition & Power Projection** | Cohort 1 | Kinoshita–Li 2D Bostan–Mori $x$-Halving/$y$-Doubling & Transpose | $O(n \log^2 n)$ |
| **P27** | `Mastery` | **LOJ #6728 / UOJ #604 — 2D Lattice Walk Return to Origin** | Cohort 2 | Iterated Double Constant Term $\operatorname{CT}_{x,y}$ + First-Return Inversion | $O(N \log N)$ |
| **P28** | `Mastery` | **Frobenius Bivariate Diagonal & MacMahon Master Theorem / Dixon Cubes** | Cohort 2 & 3 | Frobenius $Q(x,y)^p \equiv Q(x^p,y^p)$ + MMT $\det(I - XA)^{-1}$ | $O(p d_x d_y \log_p N)$ / $O(N)$ |

---

### Tier 1: `Stepping Stone` (Problems 1–6)

#### Problem 1: AtCoder Typical 90 #065 — RGB Balls 2 (★7)
- **Source**: [AtCoder Typical 90 #065](https://atcoder.jp/contests/typical90/tasks/typical90_bm) *(Cohort 2)*
- **Mathematical Statement**: Given $R$ red, $G$ green, and $B$ blue distinguishable balls, choose $K$ balls such that the numbers $(r, g, b)$ of chosen red, green, and blue balls satisfy $r + g \le X$, $g + b \le Y$, $b + r \le Z$, and $r + g + b = K$. Output the number of valid selections modulo $998244353$.
- **Constraints**: $1 \le R, G, B, K \le 2 \times 10^5$; $0 \le X, Y, Z \le 4 \times 10^5$.
- **Diagnostic Bridge**: The 3-variable generating function $[x^r y^g z^b] (1+x)^R (1+y)^G (1+z)^B$ has pairwise coupled upper bounds $r+g \le X$, $g+b \le Y$, $b+r \le Z$. Subtracting each from $r+g+b = K$ decouples them into independent lower bounds $b \ge K - X$, $r \ge K - Y$, $g \ge K - Z$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Express the three pairwise upper bounds in terms of single variables using $r + g + b = K$.
  - *Hint 2*: Once $r \ge K-Y$, $g \ge K-Z$, $b \ge K-X$ are independent box constraints on $(r, g, b)$, define truncated polynomials $P_R(t), P_G(t), P_B(t)$.
  - *Hint 3*: Compute $[t^K] \big(P_R(t) P_G(t) P_B(t)\big)$ via a single 1D NTT convolution of $P_R \cdot P_G$ followed by an $O(K)$ dot product with $P_B$.
- **Full Derivation Sketch**:
  In the unreduced formulation, we seek $\sum_{r+g+b=K} [r+g \le X][g+b \le Y][b+r \le Z] \binom{R}{r}\binom{G}{g}\binom{B}{b}$. Substituting the hyperplane invariant $r + g + b = K$ into each pairwise inequality decouples the three variables completely:
  $$\begin{aligned}
  r + g \le X &\iff K - b \le X \iff b \ge K - X, \\
  g + b \le Y &\iff K - r \le Y \iff r \ge K - Y, \\
  b + r \le Z &\iff K - g \le Z \iff g \ge K - Z.
  \end{aligned}$$
  Define the three truncated univariate polynomials
  $$P_R(t) = \sum_{r=\max(0, K-Y)}^R \binom{R}{r} t^r, \qquad P_G(t) = \sum_{g=\max(0, K-Z)}^G \binom{G}{g} t^g, \qquad P_B(t) = \sum_{b=\max(0, K-X)}^B \binom{B}{b} t^b.$$
  Then the valid selections are enumerated by $[t^K] \big(P_R(t) P_G(t) P_B(t)\big)$. Computing $C(t) = P_R(t) P_G(t)$ via a single 1D NTT and evaluating $\sum_{b=\max(0, K-X)}^{\min(B, K)} \binom{B}{b} [t^{K-b}] C(t) \pmod{998244353}$ solves the problem in **$O(K \log K)$** time and $O(K)$ space.

---

#### Problem 2: AtCoder ABC 276 G — Count Strictly Increasing Sequences
- **Source**: [AtCoder ABC 276 G](https://atcoder.jp/contests/abc276/tasks/abc276_g) *(Cohorts 1 & 2)*
- **Mathematical Statement**: Count integer sequences $0 \le A_1 < A_2 < \cdots < A_N \le M$ such that $A_{i+1} - A_i \not\equiv 0 \pmod 3$ for all $1 \le i \le N-1$, modulo $998244353$.
- **Constraints**: $1 \le N \le 10^7$, $1 \le M \le 10^7$, time limit 2.0s.
- **Diagnostic Bridge**: Switch to difference variables $d_0 = A_1 \ge 0$, $d_N = M - A_N \ge 0$, and $d_i = A_{i+1} - A_i \in \{1, 2\} + 3\mathbb{Z}_{\ge 0}$ ($1 \le i < N$). The bivariate generator has a product of $N-1$ identical steps; expanding in $y$ (sum of differences) makes every factor sparse in $y$ and $y^3$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Write each valid difference $d_i$ ($1 \le i < N$) as $d_i = r_i + 3 q_i$ with $r_i \in \{1, 2\}$ and $q_i \ge 0$.
  - *Hint 2*: What is the generating function in $y$ for a single step $d_i$? Factor it as $\frac{y + y^2}{1 - y^3} = \frac{y(1+y)}{1 - y^3}$.
  - *Hint 3*: Combine with $\frac{1}{(1-y)^2}$ for $(d_0, d_N)$ to get $[y^{M-N+1}] \frac{(1+y)^{N-1}}{(1-y)^2(1-y^3)^{N-1}}$, and expand $(1+y)^{N-1}$ against the precomputed prefix sums of $\frac{1}{(1-y)^2(1-y^3)^{N-1}}$.
- **Full Derivation Sketch**:
  Under the difference bijection $d_0 = A_1 \in \mathbb{Z}_{\ge 0}$, $d_i = A_{i+1} - A_i \in \mathbb{Z}_{\ge 1} \setminus 3\mathbb{Z}$ ($1 \le i \le N-1$), and $d_N = M - A_N \in \mathbb{Z}_{\ge 0}$, we have $\sum_{i=0}^N d_i = M$. The OGF for $(d_0, d_N)$ is $(1-y)^{-2}$, and the OGF for each internal step $d_i$ is $(y + y^2)(1 + y^3 + y^6 + \cdots) = \frac{y(1+y)}{1 - y^3}$. Hence:
  $$\begin{aligned}
  \text{Ans}
  &= [y^M] \frac{1}{(1-y)^2} \left( \frac{y + y^2}{1 - y^3} \right)^{N-1} = [y^{M - N + 1}] (1+y)^{N-1} \cdot \frac{1}{(1-y)^2 (1-y^3)^{N-1}}.
  \end{aligned}$$
  Let $S = M - N + 1$. If $S < 0$, the answer is $0$. Otherwise, define $G(y) = (1-y)^{-2}(1-y^3)^{-(N-1)} \bmod y^{S+1}$. Since $[y^{3q}] (1 - y^3)^{-(N-1)} = \binom{q + N - 2}{N - 2}$, we initialize an array $g[3q] = \binom{q+N-2}{N-2}$ for $0 \le 3q \le S$ and apply two in-place prefix sums (`for (int i = 1; i <= S; ++i) g[i] += g[i-1]`) to multiply by $(1-y)^{-2}$. Finally, $\text{Ans} = \sum_{j=0}^{\min(N-1, S)} \binom{N-1}{j} g[S - j] \pmod{998244353}$, running in **$O(N + M)$** time with zero NTTs!

---

#### Problem 3: AtCoder ABC 300 Ex — Fibonacci: Revisited
- **Source**: [AtCoder ABC 300 Ex](https://atcoder.jp/contests/abc300/tasks/abc300_h) *(Cohorts 1 & 2)*
- **Mathematical Statement**: Given $1 \le K \le 5 \times 10^4$ and $0 \le N \le 10^{18}$, let $a_n = 1$ for $0 \le n < K$ and $a_n = \sum_{i=1}^K a_{n-i}$ for $n \ge K$. Compute the **bitwise submask sum** $\sum_{m \text{ AND } N = m} a_m \bmod 998244353$.
- **Constraints**: $1 \le K \le 5 \times 10^4$, $0 \le N \le 10^{18}$.
- **Diagnostic Bridge**: Instead of extracting a single coefficient $[x^N] \frac{P(x)}{Q(x)}$, we must sum $[x^m] \frac{P(x)}{Q(x)}$ over all bitwise submasks $m \subseteq N$. In Bostan–Mori's bit-by-bit parity halving, if the lowest bit of $N$ is $0$, then $m$ must be even (keep $\mathcal{E}$); if the lowest bit of $N$ is $1$, then $m$ can be either even or odd (keep $\mathcal{E} + \mathcal{O}$)!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Set $Q_0(x) = 1 - x - x^2 - \cdots - x^K$ and compute $P_0(x) = A(x) Q_0(x) \bmod x^K = 1 - \sum_{j=2}^{K-1}(j-1)x^j$.
  - *Hint 2*: Define the submask sum functional $\mathcal{S}_M(F(x)) := \sum_{m \text{ AND } M = m} [x^m] F(x)$. Split $m = 2m' + b$ with $b \in \{0, 1\}$ to relate $\mathcal{S}_M(F)$ to $\mathcal{S}_{\lfloor M/2 \rfloor}$.
  - *Hint 3*: Write $\frac{P_t(x) Q_t(-x)}{Q_t(x) Q_t(-x)} = \frac{U_t(x^2) + x W_t(x^2)}{V_t(x^2)}$. Update $Q_{t+1}(x) = V_t(x)$ and $P_{t+1}(x) = U_t(x)$ if $(N \gg t)\ \&\ 1 = 0$, or $P_{t+1}(x) = U_t(x) + W_t(x)$ if $(N \gg t)\ \&\ 1 = 1$.
- **Full Derivation Sketch**:
  The OGF of $(a_n)_{n \ge 0}$ is $\frac{P_0(x)}{Q_0(x)}$ where $Q_0(x) = 1 - \sum_{i=1}^K x^i$ and $P_0(x) = (1 + x + \cdots + x^{K-1})Q_0(x) \bmod x^K = 1 - \sum_{j=2}^{K-1}(j-1)x^j$. For any $M \ge 0$, splitting submasks $m \subseteq M$ by their least significant bit $b \in \{0, 1\}$ gives:
  $$\mathcal{S}_M\left(\frac{P(x)}{Q(x)}\right) = \begin{cases} \mathcal{S}_{M/2}\left(\frac{U(x)}{V(x)}\right) & \text{if } M \equiv 0 \pmod 2, \\ \mathcal{S}_{(M-1)/2}\left(\frac{U(x) + W(x)}{V(x)}\right) & \text{if } M \equiv 1 \pmod 2, \end{cases}$$
  where $P(x)Q(-x) = U(x^2) + x W(x^2)$ and $Q(x)Q(-x) = V(x^2)$. Because $U(x)$ and $W(x)$ both have degree $< K$, their sum $U(x) + W(x)$ also has degree $< K$! Iterating this transition for $t = 0, 1, \dots, \lfloor \log_2 N \rfloor$ and returning $P_{\text{final}}(0) / Q_{\text{final}}(0) \pmod{998244353}$ solves the problem in **$O(K \log K \log N)$** time.

---

#### Problem 4: Codeforces 1117D — Magic Gems (Large-$M$ Regime)
- **Source**: [Codeforces 1117D](https://codeforces.com/problemset/problem/1117/D) *(Cohort 2)*
- **Mathematical Statement**: Compute the number of ways to tile a $1 \times N$ board using $1 \times 1$ tiles and $1 \times M$ tiles: $[x^N] \frac{1}{1 - x - x^M} \bmod p$. (In the original problem $M \le 100$, which allows $O(M^3 \log N)$ matrix exponentiation; we analyze both $M \le 100$ and the generalized $M \le 10^5, N \le 10^{18}$ regime.)
- **Constraints**: $1 \le N \le 10^{18}$, $2 \le M \le 10^5$.
- **Diagnostic Bridge**: Rational generating function $\frac{1}{1 - x - x^M}$ of degree $M \le 10^5$ at $N \le 10^{18}$ where $O(M^3 \log N)$ matrix exponentiation TLEs.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Express the tiling count as $[x^N] \frac{1}{1 - x - x^M}$.
  - *Hint 2*: Apply 1D Bostan–Mori with $P_0(x) = 1$ and $Q_0(x) = 1 - x - x^M$.
  - *Hint 3*: Alternatively, for very large $M$, expand $\frac{1}{1-x-x^M} = \sum_{k=0}^{\lfloor N/M \rfloor} \frac{x^{kM}}{(1-x)^{k+1}} = \sum_{k=0}^{\lfloor N/M \rfloor} \binom{N - k(M-1)}{k}$.
- **Full Derivation Sketch**:
  Every valid configuration is a sequence of gems of size $1$ (weight $x$) and split gems of size $M$ (weight $x^M$), giving the rational OGF
  $$F(x) = \sum_{j=0}^\infty (x + x^M)^j = \frac{1}{1 - x - x^M}.$$
  Initializing $P_0(x) = 1$ and $Q_0(x) = 1 - x - x^M$, 1D Bostan–Mori extracts $[x^N] \frac{P_0(x)}{Q_0(x)}$ in $\lfloor \log_2 N \rfloor + 1$ steps in **$O(M \log M \log N)$** time (or $O(M^2 \log N)$ with schoolbook multiplication for $M \le 100$). Moreover, when $N / M \le 10^6$, decoupling $u = x^M$ yields the closed-form binomial sum $[x^N] \sum_{k \ge 0} u^k (1-x)^{-(k+1)} = \sum_{k=0}^{\lfloor N/M \rfloor} \binom{N - k(M-1)}{k}$ in **$O(N/M)$** time.

---

#### Problem 5: AtCoder ABC 240 G — Teleporting Takahashi
- **Source**: [AtCoder ABC 240 G](https://atcoder.jp/contests/abc240/tasks/abc240_g) *(Cohort 1)*
- **Mathematical Statement**: Count paths of length $N \le 10^7$ in $\mathbb{Z}^3$ from $(0,0,0)$ to $(X,Y,Z)$ using the 6 unit steps $(\pm 1, 0, 0), (0, \pm 1, 0), (0, 0, \pm 1)$ modulo $998244353$.
- **Constraints**: $1 \le N \le 10^7$, $|X|, |Y|, |Z| \le 10^7$.
- **Diagnostic Bridge**: Need $[x^X y^Y z^Z] (x + x^{-1} + y + y^{-1} + z + z^{-1})^N$. Once $N-m$ steps are assigned to the $Z$-axis, the remaining $m$ steps lie in the 2D plane, where the 4-step Laurent polynomial $x + x^{-1} + y + y^{-1}$ factors into two independent 1D walks via the $45^\circ$ rotation $u = xy, v = x y^{-1}$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Fix the number of $z$-steps $N - m$; there are $\binom{N}{m} \binom{N-m}{(N-m-Z)/2}$ ways to choose and orient the $z$-steps.
  - *Hint 2*: Factor the 2D step polynomial: $x + x^{-1} + y + y^{-1} = (u + u^{-1})(v + v^{-1})$ where $x = uv$ and $y = u v^{-1}$ (or $u = x^{1/2} y^{1/2}, v = x^{1/2} y^{-1/2}$).
  - *Hint 3*: $[x^X y^Y] (x + x^{-1} + y + y^{-1})^m = \binom{m}{(m+X+Y)/2}\binom{m}{(m+X-Y)/2}$.
- **Full Derivation Sketch**:
  The 3D step Laurent polynomial is $S(x,y,z) = (x + x^{-1} + y + y^{-1}) + (z + z^{-1})$. Under the rotated coordinates $x = u v, y = u v^{-1}$, the 2D step polynomial factors completely:
  $$u v + u^{-1} v^{-1} + u v^{-1} + u^{-1} v = (u + u^{-1})(v + v^{-1}).$$
  Consequently, the number of $m$-step 2D walks from $(0,0)$ to $(X,Y)$ is $[u^{X+Y} v^{X-Y}](u+u^{-1})^m(v+v^{-1})^m = \binom{m}{(m+X+Y)/2}\binom{m}{(m+X-Y)/2}$. Expanding $S(x,y,z)^N = \sum_{m=0}^N \binom{N}{m} (x+x^{-1}+y+y^{-1})^m (z+z^{-1})^{N-m}$ and extracting $[x^X y^Y z^Z]$ yields
  $$\text{Ans} = \sum_{\substack{m = |X|+|Y| \\ m \equiv N - |Z| \pmod 2}}^{N - |Z|} \binom{N}{m} \binom{N-m}{\frac{N-m-Z}{2}} \binom{m}{\frac{m+X+Y}{2}} \binom{m}{\frac{m+X-Y}{2}} \pmod{998244353},$$
  evaluated in **$O(N)$** time and $O(N)$ space.

---

#### Problem 6: Codeforces 623E — Transforming Sequence
- **Source**: [Codeforces 623E](https://codeforces.com/problemset/problem/623/E) *(Cohorts 1 & 2)*
- **Mathematical Statement**: Count sequences $1 \le a_1, \dots, a_n < 2^k$ such that the bitwise OR prefix sums are strictly increasing ($b_1 < b_2 < \cdots < b_n$ where $b_i = b_{i-1} \mathbin{|} a_i$), modulo $10^9 + 7$.
- **Constraints**: $1 \le n \le 10^{18}$, $1 \le k \le 30000$.
- **Diagnostic Bridge**: If $n > k$, the answer is $0$ (each step must set at least one new bit among $k$ bits). For $n \le k$, track the set of bits activated at each step using an EGF in $x$: when concatenating a block of $a$ steps and a block of $b$ steps, each of the $i$ bits already active in the first block can be freely set or unset in all $b$ steps of the second block ($2^b$ choices per active bit), scaling $x \mapsto 2^b x$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: If $n > k$, output $0$. Otherwise let $f_{m, r}$ be the number of valid $m$-step sequences on a fixed universe of $r$ bits where every bit is set at least once, and form the EGF $F_m(x) = \sum_{r=0}^k f_{m, r} \frac{x^r}{r!}$.
  - *Hint 2*: For a single step, $F_1(x) = \sum_{r=1}^k \frac{x^r}{r!} = e^x - 1 \bmod x^{k+1}$.
  - *Hint 3*: Prove the twisted doubling identity $F_{a+b}(x) = F_a(2^b x) F_b(x) \bmod x^{k+1}$ and apply binary exponentiation on $n \le k$.
- **Full Derivation Sketch**:
  Since each of the $n$ steps must activate at least one new bit from $\{0, \dots, k-1\}$, $n > k \implies \text{Ans} = 0$. For $n \le k$, splitting $a+b$ steps into the first $a$ steps (activating $i$ bits) and last $b$ steps (activating $j = r - i$ new bits) gives $(2^i)^b = (2^b)^i$ choices for the $i$ already-active bits during the last $b$ steps:
  $$f_{a+b, r} = \sum_{i+j=r} \binom{r}{i} f_{a, i} (2^b)^i f_{b, j} \iff F_{a+b}(x) = F_a(2^b x) F_b(x) \pmod{x^{k+1}}.$$
  Starting from $F_1(x) = \sum_{r=1}^k \frac{x^r}{r!}$, we compute $F_n(x) \bmod x^{k+1}$ in $\lceil \log_2 n \rceil$ doubling steps using 3-prime NTT (MTT) modulo $10^9 + 7$, and return $\sum_{r=n}^k \binom{k}{r} r! [x^r] F_n(x) \pmod{10^9 + 7}$ in **$O(k \log k \log n)$** time.

---

### Tier 2: `Intermediate` (Problems 7–14)

#### Problem 7: Codeforces 960G — Bandit Blues
- **Source**: [Codeforces 960G](https://codeforces.com/problemset/problem/960/G) *(Cohort 2)*
- **Mathematical Statement**: Count permutations of $\{1, \dots, n\}$ with exactly $A$ prefix maxima (left-to-right records) and $B$ suffix maxima (right-to-left records), modulo $998244353$.
- **Constraints**: $1 \le n \le 10^5$, $0 \le A, B \le n$.
- **Diagnostic Bridge**: Placing the global maximum $n$ splits the permutation into $L$ elements on the left (forming $A-1$ cycles/records) and $R$ elements on the right (forming $B-1$ cycles/records). The bivariate EGF in $(x, y)$ has $x$ and $y$ appearing only through $z = x+y$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: By Rényi–Foata cycle-to-record bijection, the number of permutations of size $m$ with $k$ prefix maxima is the unsigned Stirling number $\left[\begin{smallmatrix} m \\ k \end{smallmatrix}\right] = [x^k] x^{\overline{m}}$.
  - *Hint 2*: Summing over the position of $n$ gives $\sum_{L+R=n-1} \binom{n-1}{L} \left[\begin{smallmatrix} L \\ A-1 \end{smallmatrix}\right] \left[\begin{smallmatrix} R \\ B-1 \end{smallmatrix}\right] = [x^{A-1} y^{B-1}] (x + y)^{\overline{n-1}}$.
  - *Hint 3*: Decouple via $z = x + y$: $[x^{A-1} y^{B-1}] \sum_{m} \left[\begin{smallmatrix} n-1 \\ m \end{smallmatrix}\right] (x+y)^m = \binom{A+B-2}{A-1} \left[\begin{smallmatrix} n-1 \\ A+B-2 \end{smallmatrix}\right]$.
- **Full Derivation Sketch**:
  The global maximum $n$ is simultaneously the last prefix maximum and the first suffix maximum. Conditioning on $L$ elements to the left of $n$ and $R = n - 1 - L$ elements to the right of $n$, and using the unsigned Stirling Mixed EOGF $\sum_{m, c \ge 0} \left[\begin{smallmatrix} m \\ c \end{smallmatrix}\right] y^c \frac{t^m}{m!} = (1 - t)^{-y}$:
  $$\begin{aligned}
  \text{Ans}
  &= \sum_{L+R=n-1} \binom{n-1}{L} \left[\begin{matrix} L \\ A-1 \end{matrix}\right] \left[\begin{matrix} R \\ B-1 \end{matrix}\right]
  = (n-1)! [t^{n-1} x^{A-1} y^{B-1}] (1 - t)^{-x} (1 - t)^{-y} \\
  &= [x^{A-1} y^{B-1}] \prod_{k=0}^{n-2} (k + x + y) = \binom{A+B-2}{A-1} [z^{A+B-2}] \prod_{k=0}^{n-2} (k + z) = \binom{A+B-2}{A-1} \left[\begin{matrix} n-1 \\ A+B-2 \end{matrix}\right],
  \end{aligned}$$
  computed in **$O(n \log^2 n)$** via D&C NTT product (or **$O(n \log n)$** via Taylor-shift doubling of $z^{\overline{n-1}}$).

---

#### Problem 8: Luogu P5406 — [THUPC2019] 找树
- **Source**: [Luogu P5406](https://www.luogu.com.cn/problem/P5406) *(Cohort 1)*
- **Mathematical Statement**: Given an undirected multigraph on $n \le 70$ vertices where each edge $e$ has a $w$-bit integer weight $v_e \in [0, 2^w - 1]$ ($w \le 12$) and each bit position $r \in \{0, \dots, w-1\}$ specifies a bitwise operation $\oplus_r \in \{\text{AND}, \text{OR}, \text{XOR}\}$, find the maximum bitwise weight of a spanning tree.
- **Constraints**: $1 \le n \le 70$, $m \le 5000$, $w \le 12$.
- **Diagnostic Bridge**: A spanning tree's weight is a $w$-variate monomial $z_0^{b_0} \cdots z_{w-1}^{b_{w-1}}$ in the mixed group ring $\mathcal{A} = \bigotimes_{r=0}^{w-1} \mathbb{F}_p[z_r]/I_r$. By applying the $w$-dimensional Fast Walsh–Hadamard Transform (FWT) to every entry of the Laplacian matrix $L(z_0, \dots, z_{w-1})$, the multivariate determinant decouples into $2^w$ independent scalar determinants!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Represent each edge weight $v_e$ as a basis element in the $2^w$-dimensional algebra $\mathcal{A}$ where bit $r$ multiplies via $\oplus_r \in \{\text{AND}, \text{OR}, \text{XOR}\}$.
  - *Hint 2*: Apply the $w$-dimensional forward FWT (matching AND/OR/XOR per bit) to each $(i, j)$ entry of the $(n-1) \times (n-1)$ Laplacian minor.
  - *Hint 3*: Compute $\det \widehat{L}^{(mask)} \in \mathbb{F}_p$ in $O(n^3)$ for each of the $2^w$ masks, apply inverse FWT, and return the largest $mask$ with a non-zero coefficient.
- **Full Derivation Sketch**:
  By Kirchhoff's Matrix-Tree Theorem over the commutative ring $\mathcal{A} = \bigotimes_{r=0}^{w-1} \mathbb{F}_p[z_r]/I_r$, the $(n-1) \times (n-1)$ reduced Laplacian $L(\mathbf{z})$ satisfies $\det L(\mathbf{z}) = \sum_{T} \mathbf{z}^{\text{weight}(T)}$. For each bit $r$, apply the corresponding $2 \times 2$ FWT transform ($\begin{psmallmatrix} 1 & 1 \\ 1 & -1 \end{psmallmatrix}$ for XOR, $\begin{psmallmatrix} 0 & 1 \\ 1 & 1 \end{psmallmatrix}$ for AND, $\begin{psmallmatrix} 1 & 1 \\ 1 & 0 \end{psmallmatrix}$ for OR) to every entry of $L$. Since FWT is an algebra isomorphism $\mathcal{A} \xrightarrow{\sim} \mathbb{F}_p^{2^w}$ with pointwise multiplication, $\widehat{\det L}(mask) = \det\big(\widehat{L}(mask)\big)$ for each $mask \in [0, 2^w - 1]$. Running $O(n^2 w 2^w)$ FWTs, $2^w$ scalar Gaussian eliminations of size $(n-1) \times (n-1)$, and one IFWT of size $2^w$ achieves **$O(2^w n^3 + 2^w w n^2)$** time.

---

#### Problem 9: Luogu P5339 — [TJOI2019] 唱、跳、rap和篮球
- **Source**: [Luogu P5339](https://www.luogu.com.cn/problem/P5339) *(Cohort 2)*
- **Mathematical Statement**: Count sequences of length $N \le 1000$ over $\{1, 2, 3, 4\}$ containing at most $A, B, C, D$ occurrences of $1, 2, 3, 4$ respectively and no contiguous substring `1234`, modulo $998244353$.
- **Constraints**: $N \le 1000$, $0 \le A, B, C, D \le 500$.
- **Diagnostic Bridge**: In the 4-variate EGF over $(x_1, x_2, x_3, x_4)$, the forbidden pattern `1234` only couples the 4 variables through the **diagonal monomial $u = x_1 x_2 x_3 x_4$**! Conditioning on $k$ occurrences of `1234` reduces the remaining $N - 4k$ positions to a standard 4-factor EGF convolution.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Apply inclusion–exclusion on the number $k$ ($0 \le k \le \min(N/4, A, B, C, D)$) of chosen occurrences of the block `1234`.
  - *Hint 2*: With $k$ blocks of `1234` contracted into single tokens, there are $\binom{N - 3k}{k}$ ways to place the $k$ blocks among the remaining $N - 4k$ letters.
  - *Hint 3*: The remaining $N - 4k$ letters are chosen with counts $a \le A-k, b \le B-k, c \le C-k, d \le D-k$ summing to $N - 4k$, which is $(N-4k)! [t^{N-4k}] E_{A-k}(t) E_{B-k}(t) E_{C-k}(t) E_{D-k}(t)$ where $E_M(t) = \sum_{i=0}^M \frac{t^i}{i!}$.
- **Full Derivation Sketch**:
  Because the pattern `1234` has no non-trivial self-overlap, choosing $k$ occurrences of `1234` consumes $k$ copies of each letter in $\{1, 2, 3, 4\}$ and leaves $N - 4k$ free positions, giving $\binom{(N-4k)+k}{k} = \binom{N-3k}{k}$ placements for the $k$ blocks. The remaining $N - 4k$ positions are filled by bounded counts $a \le A-k, b \le B-k, c \le C-k, d \le D-k$, enumerated by the product of truncated EGFs $E_M(t) = \sum_{i=0}^M \frac{t^i}{i!}$:
  $$\text{Ans} = \sum_{k=0}^{\min(\lfloor N/4 \rfloor, A, B, C, D)} (-1)^k \binom{N - 3k}{k} (N - 4k)! [t^{N-4k}] \left( E_{A-k}(t) E_{B-k}(t) E_{C-k}(t) E_{D-k}(t) \right),$$
  evaluated in **$O(N^2 \log N)$** time via NTT (or $O(N^2)$ by maintaining $E_{A-k} E_{B-k}$ and $E_{C-k} E_{D-k}$ incrementally).

---

#### Problem 10: AtCoder ABC 279 Ex — Sum of Prod of Min
- **Source**: [AtCoder ABC 279 Ex](https://atcoder.jp/contests/abc279/tasks/abc279_h) *(Cohort 1)*
- **Mathematical Statement**: Given $1 \le N \le 10^{12}$ and $N \le M \le 2N$, compute $\sum_{A_1 + \cdots + A_N = M, \, A_i \ge 1} \prod_{i=1}^N \min(i, A_i) \bmod 200003$.
- **Constraints**: $1 \le N \le 10^{12}$, $N \le M \le 2N$, prime modulus $P = 200003$.
- **Diagnostic Bridge**: The 1D OGF of $c_{i, a} = \min(i, a)$ ($a \ge 1$) is $\sum_{a=1}^\infty \min(i, a) x^a = \frac{x(1 - x^i)}{(1 - x)^2}$. Multiplying over $i = 1, \dots, N$ yields $\frac{x^N \prod_{i=1}^N (1 - x^i)}{(1 - x)^{2N}}$. Because $M \le 2N \implies K := M - N \le N$, the finite product $\prod_{i=1}^N (1 - x^i)$ agrees with $\prod_{i=1}^\infty (1 - x^i)$ up to degree $K$, which is sparse by **Euler's Pentagonal Number Theorem**!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Verify $\sum_{a=1}^\infty \min(i, a) x^a = \frac{x(1 - x^i)}{(1 - x)^2}$, so the answer is $[x^{M-N}] \frac{\prod_{i=1}^N (1 - x^i)}{(1 - x)^{2N}}$.
  - *Hint 2*: Since $N \le M \le 2N$, the target degree $K = M - N$ satisfies $0 \le K \le N$. Thus any factor $(1 - x^i)$ with $i > N$ is $\equiv 1 \pmod{x^{K+1}}$, allowing us to replace $\prod_{i=1}^N (1 - x^i)$ by $\prod_{i=1}^\infty (1 - x^i) = \sum_{k \in \mathbb{Z}} (-1)^k x^{k(3k-1)/2}$.
  - *Hint 3*: Extract $[x^K]$ against $(1 - x)^{-2N} = \sum_{j \ge 0} \binom{2N - 1 + j}{2N - 1} x^j$ over the $O(\sqrt{K})$ pentagonal numbers $\omega_k = \frac{k(3k-1)}{2} \le K$, evaluating each binomial coefficient via Lucas's Theorem mod $P = 200003$.
- **Full Derivation Sketch**:
  For each $i \in \{1, \dots, N\}$, $\sum_{a=1}^\infty \min(i, a) x^a = x + 2x^2 + \cdots + i x^i + i x^{i+1} + \cdots = \frac{x(1-x^i)}{(1-x)^2}$. Multiplying over $1 \le i \le N$ and setting $K = M - N \le N$:
  $$\text{Ans} = [x^M] \prod_{i=1}^N \frac{x(1-x^i)}{(1-x)^2} = [x^K] (1 - x)^{-2N} \prod_{i=1}^\infty (1 - x^i) = [x^K] (1 - x)^{-2N} \sum_{k \in \mathbb{Z}} (-1)^k x^{k(3k-1)/2}.$$
  Expanding $(1-x)^{-2N}$ gives the sparse summation over $\omega_k = \frac{k(3k-1)}{2} \le M - N$:
  $$\text{Ans} = \sum_{\frac{k(3k-1)}{2} \le M - N} (-1)^k \binom{M + N - 1 - \frac{k(3k-1)}{2}}{2N - 1} \pmod{200003},$$
  which has at most $2\sqrt{2(M-N)/3} + 1 \le 1.64 \times 10^6$ terms, each evaluated in $O(\log_P M)$ time via Lucas's Theorem after $O(P)$ factorial precomputation, for a total time of **$O(P + \sqrt{M - N} \log_P M)$**.

---

#### Problem 11: AtCoder AGC 013 E — Placing Squares (Generalized $K$-Moment Version)
- **Source**: [AtCoder AGC 013 E](https://atcoder.jp/contests/agc013/tasks/agc013_e) *(Cohort 2)*
- **Mathematical Statement**: Partition a $1 \times N$ board ($N \le 10^{18}$) into contiguous segments of lengths $s_1 + \cdots + s_m = N$ and weight each partition by $\prod_{i=1}^m s_i^K \bmod 10^9 + 7$. (Original problem has $K = 2$ with $M$ forbidden cut points; the un-blocked $K \le 10^5$ generalization requires 1D Bostan–Mori.)
- **Constraints**: $1 \le N \le 10^{18}$, $1 \le K \le 10^5$ (or $K = 2, M \le 10^5$ forbidden cuts).
- **Diagnostic Bridge**: The single-block weight generator $W_K(x) = \sum_{s=1}^\infty s^K x^s = \frac{A_K(x)}{(1 - x)^{K+1}}$ is a rational function of degree $K+1$ where $A_K(x)$ is the $K$-th Eulerian polynomial. Thus $\frac{W_K(x)}{1 - W_K(x)} = \frac{A_K(x)}{(1-x)^{K+1} - A_K(x)}$ is a rational function of degree $K+1$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Use the identity $\sum_{s=1}^\infty s^K x^s = \frac{A_K(x)}{(1 - x)^{K+1}}$ where $[x^j] A_K(x) = \left\langle\begin{smallmatrix} K \\ j-1 \end{smallmatrix}\right\rangle$.
  - *Hint 2*: Compute the Eulerian polynomial $A_K(x)$ in $O(K \log K)$ via $A_K(x) = (1 - x)^{K+1} \cdot \left(\sum_{s=0}^K s^K x^s\right) \bmod x^{K+1}$.
  - *Hint 3*: Extract $[x^N] \frac{A_K(x)}{(1-x)^{K+1} - A_K(x)}$ using 1D Bostan–Mori in $O(K \log K \log N)$ (and for $K=2$ with $M$ forbidden cuts $X_1 < \dots < X_M$, multiply $3 \times 3$ transfer matrices $M_{\text{forbid}} M_{\text{allow}}^{\Delta X - 1}$ in $O(3^3 M \log N)$).
- **Full Derivation Sketch**:
  Summing over all $m \ge 1$ segments of positive lengths $s_1 + \cdots + s_m = N$, the OGF of total weight $\prod_{i=1}^m s_i^K$ is
  $$F_K(x) = \sum_{m=1}^\infty W_K(x)^m = \frac{W_K(x)}{1 - W_K(x)} = \frac{A_K(x)}{(1 - x)^{K+1} - A_K(x)},$$
  where $A_K(x) = \sum_{j=1}^K \left\langle\begin{smallmatrix} K \\ j-1 \end{smallmatrix}\right\rangle x^j$ has degree $K$ and $Q_K(x) = (1-x)^{K+1} - A_K(x)$ has degree $K+1$ with $Q_K(0) = 1$. Applying 1D Bostan–Mori extracts $[x^N] F_K(x)$ in **$O(K \log K \log N)$** time (and for the original $K = 2$ version with $M$ forbidden cut coordinates, $Q_2(x) = (1-x)^3 - (x + x^2) = 1 - 4x + 2x^2 - x^3$ corresponds to a 3-state DP over $\{0, 1, 2\}$ placed balls with $3 \times 3$ transition matrices $M_{\text{allow}} = \begin{psmallmatrix} 2 & 2 & 1 \\ 1 & 1 & 0 \\ 1 & 2 & 1 \end{psmallmatrix}$ and $M_{\text{forbid}} = \begin{psmallmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 2 & 1 \end{psmallmatrix}$ in **$O(M \log N)$** time).

---

#### Problem 12: Codeforces 1264D2 — Beautiful Bracket Sequence (hard version)
- **Source**: [Codeforces 1264D2](https://codeforces.com/problemset/problem/1264/D2) *(Cohort 1)*
- **Mathematical Statement**: Given a string $s$ of length $n \le 10^6$ over `(`, `)`, `?`, find the sum of maximum nested bracket depths over all $2^{\#?}$ replacements of `?`, modulo $998244353$.
- **Constraints**: $1 \le n \le 10^6$.
- **Diagnostic Bridge**: Every non-empty matched bracket sequence has a **unique split point** $i$ where the number of `(` in $s[1..i]$ equals the number of `)` in $s[i+1..n]$, and that common count equals the maximum depth! Counting how many ways `(` in $s[1..i]$ equals `)` in $s[i+1..n]$ is a constant-term extraction $\operatorname{CT}_z$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Prove that for any string of `(` and `)`, $\max_{0 \le i \le n} \min(\text{open}(1..i), \text{close}(i+1..n))$ is achieved at the unique split point where $\text{open}(1..i) = \text{close}(i+1..n)$, and cutting each matched pair across the split contributes $+1$.
  - *Hint 2*: If $s[1..i]$ has $a_i$ fixed `(` and $c_i$ `?`'s, and $s[i+1..n]$ has $b_i$ fixed `)` and $d_i$ `?`'s, write the contribution of split $i$ as $\operatorname{CT}_z \big( \text{weight} \cdot z^{a_i} (1+z)^{c_i} \cdot z^{-b_i}(1+z^{-1})^{d_i} \big)$.
  - *Hint 3*: Simplify $\operatorname{CT}_z\big(a_i z^{a_i-b_i}(1+z)^{c_i}(1+z^{-1})^{d_i} + c_i z^{a_i+1-b_i}(1+z)^{c_i-1}(1+z^{-1})^{d_i}\big) = a_i \binom{c_i+d_i}{b_i+d_i-a_i} + c_i \binom{c_i+d_i-1}{b_i+d_i-a_i-1}$.
- **Full Derivation Sketch**:
  Let $a_i, c_i$ be the counts of `(` and `?` in $s[1..i]$, and $b_i, d_i$ be the counts of `)` and `?` in $s[i+1..n]$. At split $i$, choosing $u$ of the $c_i$ left `?`'s to be `(` and $v$ of the $d_i$ right `?`'s to be `)` achieves balanced depth $a_i + u$ when $a_i + u = b_i + v$. Expressing the condition $u - v = b_i - a_i$ as $\operatorname{CT}_z \big(z^{(a_i+u)-(b_i+v)}\big)$:
  $$\begin{aligned}
  \text{Ans}
  &= \sum_{i=1}^{n-1} \operatorname{CT}_z \left[ \left.\frac{\partial}{\partial w}\right|_{w=1} (w z)^{a_i} (1 + w z)^{c_i} z^{-b_i} (1 + z^{-1})^{d_i} \right] \\
  &= \sum_{i=1}^{n-1} \left( a_i \binom{c_i + d_i}{b_i + d_i - a_i} + c_i \binom{c_i + d_i - 1}{b_i + d_i - a_i - 1} \right) \pmod{998244353},
  \end{aligned}$$
  evaluated in **$O(n)$** time and $O(n)$ space.

---

#### Problem 13: UOJ #424 — 【集训队作业2018】count
- **Source**: [UOJ #424](https://uoj.ac/problem/424) *(Cohorts 1 & 2)*
- **Mathematical Statement**: Count equivalence classes of arrays of length $n \le 10^9$ over $\{1, \dots, m\}$ having identical range-minimum Cartesian trees (with ties broken to the left), modulo $998244353$.
- **Constraints**: $1 \le n, m \le 10^9$ with $\min(n, m) \le 2 \times 10^5$.
- **Diagnostic Bridge**: Under leftmost-minimum tie-breaking, a Cartesian tree on $\{1, \dots, m\}$ is realizable if and only if every root-to-node path takes $< m$ left-child steps (since each left-child step strictly increases the minimum value needed in $\{1, \dots, m\}$). By the Two-Boundary Kernel Method (Section 5.6), the OGF of binary trees with left-depth $< m$ is the rational Chebyshev ratio $\frac{Q_m(x)}{Q_{m+1}(x)}$ where $Q_{k+1}(x) = Q_k(x) - x Q_{k-1}(x)$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Show that a binary tree of size $n$ is the leftmost-minimum Cartesian tree of at least one array in $\{1, \dots, m\}^n$ iff the number of left-child edges on any root-to-node path is $\le m - 1$.
  - *Hint 2*: Let $T_k(x)$ be the OGF of binary trees with left-depth $< k$; then $T_0(x) = 1$ and $T_k(x) = \frac{1}{1 - x T_{k-1}(x)} = \frac{Q_k(x)}{Q_{k+1}(x)}$ where $Q_0 = 1, Q_1 = 1$, and $Q_{k+1}(x) = Q_k(x) - x Q_{k-1}(x)$.
  - *Hint 3*: Explicitly, $[x^j] Q_k(x) = (-1)^j \binom{k - j}{j}$. Extract $[x^n] \frac{Q_m(x)}{Q_{m+1}(x)}$ via 1D Bostan–Mori in $O(m \log m \log n)$ (or 1D FPS inversion in $O(n \log n)$ when $n \le 2 \times 10^5$).
- **Full Derivation Sketch**:
  If $n < m$, the left-depth constraint $< m$ is vacuous and the answer is the Catalan number $C_n = \frac{1}{n+1}\binom{2n}{n}$. If $n \ge m$, solving the Two-Boundary Kernel equation $(u - t(1 + u^2)) F(u, t) = u - t A(t) - t u^{m+2} B(t)$ (or the continued fraction $T_k(x) = \frac{1}{1 - x T_{k-1}(x)}$) gives $T_m(x) = \frac{Q_m(x)}{Q_{m+1}(x)}$ with
  $$Q_k(x) = \sum_{j=0}^{\lfloor k/2 \rfloor} (-1)^j \binom{k - j}{j} x^j.$$
  Constructing $Q_m(x)$ and $Q_{m+1}(x)$ in $O(m)$ time and applying 1D Bostan–Mori extracts $[x^n] \frac{Q_m(x)}{Q_{m+1}(x)}$ in **$O(m \log m \log n)$** time.

---

#### Problem 14: Codeforces 755G — PolandBall and Many Other Balls
- **Source**: [Codeforces 755G](https://codeforces.com/problemset/problem/755/G) *(Cohorts 1 & 2)*
- **Mathematical Statement**: Given $n \le 10^9$ and $k < 2^{15}$, for every $1 \le m \le k$ compute the number of ways to choose $m$ disjoint subsets of $\{1, \dots, n\}$ where each subset is either a singleton $\{i\}$ or an adjacent pair $\{i, i+1\}$, modulo $998244353$.
- **Constraints**: $1 \le n \le 10^9$, $1 \le k < 2^{15}$.
- **Diagnostic Bridge**: The bivariate rational generating function is $F(x, y) = \frac{1}{1 - (1+y)x - y x^2}$, so $f_{n,m} = [x^n y^m] F(x, y) = \sum_{j=0}^m \binom{m}{j}\binom{n-j}{m} = D(n-m, m)$ is a diagonal slice of the Delannoy numbers. This single problem unites **all four methods** of Wave 4A:
  1. **2D Bostan–Mori Regime A/B**: $O(k \log k \log n)$.
  2. **Polynomial Fibonacci Doubling $\bmod y^{k+1}$**: $O(k \log k \log n)$.
  3. **Primary-Variable Flip & Quadratic Irrational $\exp((n+1) \ln \alpha(y))$**: $O(k \log k)$.
  4. **D-Finite 2nd-Order ODE (4-Term & 3-Term Recurrences)**: **$O(k)$**!
- **3-Tier Progressive Hints**:
  - *Hint 1* (*Bivariate OGF & Polynomial Fibonacci Doubling*): From $F_n(y) = (1+y) F_{n-1}(y) + y F_{n-2}(y)$, use the companion matrix power $\begin{psmallmatrix} 1+y & y \\ 1 & 0 \end{psmallmatrix}^m = \begin{psmallmatrix} F_m(y) & y F_{m-1}(y) \\ F_{m-1}(y) & y F_{m-2}(y) \end{psmallmatrix}$ to derive the $O(k \log k \log n)$ polynomial doubling identities $F_{2m}(y) = F_m(y)^2 + y F_{m-1}(y)^2$ and $F_{2m+1}(y) = F_{m+1}(y) F_m(y) + y F_m(y) F_{m-1}(y) \bmod y^{k+1}$.
  - *Hint 2* (*$O(k \log k)$ Quadratic Root*): Solve $1 - (1+y)x - y x^2 = 0$ for $x$ with $\Delta = \sqrt{1 + 6y + y^2}$ to write $F_n(y) = \frac{(1+y+\Delta)^{n+1} - (1+y-\Delta)^{n+1}}{2^{n+1}\Delta} \equiv \frac{1}{\Delta}\left(\frac{1 + y + \Delta}{2}\right)^{n+1} \pmod{y^{k+1}}$.
  - *Hint 3* (*$O(k)$ D-Finite ODE Recurrence*): Verify that $F_n(y)$ satisfies the exact 2nd-order linear ODE $y(1 + 6y + y^2) F_n''(y) + (1 + 9y + 2y^2) F_n'(y) - n(n+2)(1 + y) F_n(y) = 0$, and extract $[y^{m-1}]$ to obtain the $O(k)$ recurrence!
- **Full Derivation Sketch**:
  - **Method 1 ($O(k \log k \log n)$ Polynomial Fibonacci Doubling)**: Maintain the pair $(F_m(y), F_{m-1}(y)) \bmod y^{k+1}$ across the binary bits of $n$ from MSB to LSB using $F_{2m}(y) = F_m(y)^2 + y F_{m-1}(y)^2$, $F_{2m+1}(y) = F_{m+1}(y) F_m(y) + y F_m(y) F_{m-1}(y)$, and $F_{m+1}(y) = (1+y) F_m(y) + y F_{m-1}(y)$ with 3 NTTs of size $2^{16}$ per bit.
  - **Method 2 (Optimal $O(k)$ D-Finite ODE Recurrence)**: Since $U_n(y) = 2^{n+1}\Delta F_n(y) = (1+y+\Delta)^{n+1} - (1+y-\Delta)^{n+1}$ with $\Delta = \sqrt{1 + 6y + y^2}$ satisfies $(1+6y+y^2) U_n''(y) + (3+y) U_n'(y) - (n+1)^2 U_n(y) = 0$, substituting $U_n = 2^{n+1}\Delta F_n$ yields the exact 2nd-order ODE for $F_n(y)$:
    $$y(1 + 6y + y^2) F_n''(y) + (1 + 9y + 2y^2) F_n'(y) - n(n+2)(1 + y) F_n(y) = 0.$$
    Extracting $[y^{m-1}]$ and setting $a_m := m(n - m + 1)$ gives the **4-term $O(k)$ recurrence** for all $1 \le m \le \min(n, k)$ (with $f_{n,0} = 1, f_{n,<0} = 0$):
    $$a_m f_{n,m} = \big(2n(n+2) - 5a_m\big) f_{n,m-1} + \big(5a_{m-2} - 2n(n+2)\big) f_{n,m-2} + a_{m-2} f_{n,m-3}.$$
    Eliminating $f_{n,m-3}$ gives the **3-term $O(k)$ recurrence** for $2 \le m \le \min(n, k)$ (with $f_{n,0} = 1, f_{n,1} = 2n - 1$):
    $$m(n-m+1)(n-2m+3) f_{n,m} = \big(2n^3 + n^2(11-10m) + n(18m^2-38m+19) - 12m^3 + 36m^2 - 34m + 10\big) f_{n,m-1} - (m-1)\big(n^2 - 3n(m-1) + (m-2)(2m-1)\big) f_{n,m-2},$$
    which computes all $f_{n,1}, \dots, f_{n,k}$ in **$O(k)$** time!

---

### Tier 3: `Advanced` (Problems 15–22)

#### Problem 15: AtCoder AGC 058 D — Yet Another ABC String
- **Source**: [AtCoder AGC 058 D](https://atcoder.jp/contests/agc058/tasks/agc058_d) *(Cohorts 1 & 2)*
- **Mathematical Statement**: Count strings containing $A$ `'A'`s, $B$ `'B'`s, and $C$ `'C'`s with no contiguous substring `'ABC'`, `'BCA'`, or `'CAB'`, modulo $998244353$.
- **Constraints**: $1 \le A, B, C \le 10^6$.
- **Diagnostic Bridge**: By the Goulden–Jackson cluster method, any maximal overlapping cluster of `{ABC, BCA, CAB}` has length $L \ge 3$ and net inclusion–exclusion weight $(-1)$ when $L \equiv 0 \pmod 3$, $(+1)$ when $L \equiv 1 \pmod 3$, and $0$ when $L \equiv 2 \pmod 3$. Summing over clusters yields the 3-variate rational generating function $\frac{1 - xyz}{1 - (x+y+z) + 2xyz}$, which decouples via $u = xyz$ and $s = x+y+z$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Show that if $w$ is a cluster of overlapping forbidden cyclic triples, its cluster weight sum depends only on $|w| \bmod 3$, yielding the cluster generator $\frac{-3xyz + (x+y+z)xyz}{1 - xyz}$.
  - *Hint 2*: Substitute the cluster generator into the Goulden–Jackson formula $\frac{1}{1 - (x+y+z) - \text{Cluster}(x,y,z)}$ to get $F(x, y, z) = \frac{1 - xyz}{1 - (x+y+z) + 2xyz}$.
  - *Hint 3*: Expand $\frac{1 - u}{1 - s + 2u} = (1 - u) \sum_{k \ge 0} (-2u)^k (1 - s)^{-k-1}$ where $u = xyz$ and $s = x+y+z$, and extract $[x^A y^B z^C]$ in $O(\min(A, B, C))$.
- **Full Derivation Sketch**:
  In the Goulden–Jackson Cluster Method for $\mathcal{F} = \{\text{`ABC`}, \text{`BCA`}, \text{`CAB`}\}$, the cyclic overlaps of length $3k$ have weight $-3(xyz)^k$ and those of length $3k+1$ have weight $+(x+y+z)(xyz)^k$, so the cluster generating function is $C(x,y,z) = \frac{-3xyz + (x+y+z)xyz}{1 - xyz}$. Therefore:
  $$F(x, y, z) = \frac{1}{1 - (x+y+z) - \frac{-3xyz + (x+y+z)xyz}{1 - xyz}} = \frac{1 - xyz}{1 - (x+y+z) + 2xyz}.$$
  Let $M(a, b, c, k) = [x^a y^b z^c] (1 - x - y - z)^{-k-1} = \binom{a+b+c+k}{k} \frac{(a+b+c)!}{a! b! c!}$. Expanding in powers of $u = xyz$ gives:
  $$\text{Ans} = \sum_{k=0}^{\min(A,B,C)} (-2)^k \Big( M(A-k, B-k, C-k, k) - M(A-k-1, B-k-1, C-k-1, k) \Big) \pmod{998244353},$$
  evaluated in **$O(A + B + C)$** time and $O(A + B + C)$ space.

---

#### Problem 16: Codeforces 1553I — Stairs
- **Source**: [Codeforces 1553I](https://codeforces.com/problemset/problem/1553/I) *(Cohort 1)*
- **Mathematical Statement**: Given desired stair lengths $a_1, \dots, a_n$ ($n \le 10^5$), count permutations where each maximal block of consecutive values covering position $i$ has length $a_i$, modulo $998244353$.
- **Constraints**: $1 \le n \le 10^5$.
- **Diagnostic Bridge**: Partition the array into $m$ base blocks of lengths $L_1, \dots, L_m$. Merging adjacent blocks $(L_i, L_{i+1}) \mapsto L_i + L_{i+1}$ corresponds to inclusion–exclusion in a bivariate polynomial $P(x, y)$ where $x$ tracks original blocks and $y$ tracks merged components—and the boundary states of any interval depend only on whether the leftmost/rightmost block has length $1$ or $>1$ ($2 \times 2$ matrix of 1D polynomials)!
- **3-Tier Progressive Hints**:
  - *Hint 1*: First verify that the array cleanly partitions into $m$ contiguous blocks of sizes $L_1, \dots, L_m$ where the $j$-th block consists of $L_j$ copies of $L_j$; if not, output $0$.
  - *Hint 2*: A merged component of $r \ge 1$ original blocks has $2$ orientations (increasing or decreasing) if its total size $> 1$ (i.e., $r \ge 2$ or $L_j > 1$), and $1$ orientation if $r = 1$ and $L_j = 1$.
  - *Hint 3*: Run D&C NTT over $1 \le j \le m$, maintaining a $2 \times 2$ matrix of 1D polynomials in $y$ (number of merged components) indexed by whether the left/right endpoint is an unmerged block of size $1$ or a block of size $>1$.
- **Full Derivation Sketch**:
  By inclusion–exclusion on the $m - 1$ boundaries between the $m$ base blocks, merging $r \ge 1$ consecutive blocks into a single component contributes $(-1)^{r-1} y$ times the orientation factor ($1$ if $r = 1, L_j = 1$; $2$ otherwise). Representing each base block $j$ by a $2 \times 2$ transfer matrix $M_j(y) \in \mathbb{F}_p[y]^{2 \times 2}$ (where state $0$ indicates an active component of size $1$ and state $1$ indicates an active component of size $\ge 2$) and multiplying $M_1(y) \cdots M_m(y)$ via a binary tree of 1D NTTs computes $P(y) = \sum_{k=1}^m c_k y^k$ in **$O(n \log^2 n)$** time. Finally, $\text{Ans} = \sum_{k=1}^m k! c_k \pmod{998244353}$.

---

#### Problem 17: Codeforces 1336E2 — Chiori and Doll Picking (hard version)
- **Source**: [Codeforces 1336E2](https://codeforces.com/problemset/problem/1336/E2) *(Cohort 1)*
- **Mathematical Statement**: Given $n$ integers of $m \le 53$ bits, for each $0 \le c \le m$ compute the number of subsets whose XOR sum has popcount $c$, modulo $998244353$.
- **Constraints**: $1 \le n \le 2 \times 10^5$, $0 \le m \le 53$.
- **Diagnostic Bridge**: Let $k = \dim V \le m$ be the XOR linear basis dimension. When $k \le 26$, enumerate $V$ in $O(2^k)$. When $k > 26$, $\dim V^\perp = m - k \le 26$! By the $m$-variate Walsh–Hadamard / MacWilliams identity, a vector $y \in V^\perp$ with $\operatorname{popcount}(y) = j$ contributes $[z^c] (1 - z)^j (1 + z)^{m - j}$ to popcount $c$, decoupling the $m$ variables into the single scalar $j = \operatorname{popcount}(y)$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Reduce the input to a systematic XOR basis $V$ of dimension $k \le m$ in RREF form $G = [I_k \mid A]$; each element of $V$ is hit $2^{n-k}$ times.
  - *Hint 2*: Construct the orthogonal complement basis $V^\perp$ of dimension $m - k$ in $O(m^2)$ via $H = [A^T \mid I_{m-k}]$.
  - *Hint 3*: If $k > m/2$, enumerate all $2^{m-k}$ vectors $y \in V^\perp$ to count $cnt_{V^\perp}[j] = \#\{y \in V^\perp : \operatorname{popcount}(y) = j\}$, then multiply by the Krawtchouk matrix $K_{c, j} = [z^c](1-z)^j(1+z)^{m-j}$.
- **Full Derivation Sketch**:
  In the $m$-variate group algebra $\mathbb{F}_p[x_0, \dots, x_{m-1}] / (x_r^2 - 1)$, the indicator of the subspace $V$ is $F(\mathbf{x}) = 2^{n-k} \sum_{v \in V} \mathbf{x}^v$. Applying the $m$-dimensional Walsh–Hadamard transform maps $V$ to $2^k$ times the indicator of $V^\perp$. Grouping the inverse transform by Hamming weight $c = \operatorname{popcount}(v)$ and $j = \operatorname{popcount}(y)$ via $[z^c] \prod_{r=0}^{m-1} (1 + (-1)^{y_r} z) = [z^c] (1 - z)^j (1 + z)^{m - j}$ gives MacWilliams' identity:
  $$\text{Ans}[c] = 2^{n - m} \sum_{j=0}^m cnt_{V^\perp}[j] \cdot [z^c] \Big((1 - z)^j (1 + z)^{m - j}\Big) \pmod{998244353},$$
  running in **$O(n m + 2^{\min(k, m-k)} + m^3)$** time.

---

#### Problem 18: Luogu P5487 — [BJOI2019] 勘破神机
- **Source**: [Luogu P5487](https://www.luogu.com.cn/problem/P5487) *(Cohort 1)*
- **Mathematical Statement**: Compute $\sum_{n=L}^R \binom{f_n}{k} \bmod 998244353$ for $L, R \le 10^{18}$ and $k \le 501$, where $f_n$ is either the shifted Fibonacci sequence ($m=2$, $f_n = F_{n+1}$) or the even-indexed sequence ($m=3$, $f_n = \frac{(2+\sqrt{3})^n + (2-\sqrt{3})^n}{2}$).
- **Constraints**: $T \le 10$, $1 \le L \le R \le 10^{18}$, $1 \le k \le 501$.
- **Diagnostic Bridge**: Expand $\binom{f_n}{k} = \frac{1}{k!} \sum_{j=0}^k (-1)^{k-j} \left[\begin{smallmatrix} k \\ j \end{smallmatrix}\right] f_n^j$. Since $f_n = c_1 \alpha^n + c_2 \beta^n$ in the quadratic extension $\mathbb{F}_p[\sqrt{d}]$ ($d = 5$ for $m=2$, $d = 3$ for $m=3$), the binomial expansion of $f_n^j$ decouples $n$ into pure geometric progressions $(\alpha^a \beta^{j-a})^n$, each of which has a degree-1 rational generating function $\frac{1}{1 - \alpha^a \beta^{j-a} x}$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Expand the falling factorial $x^{\underline{k}} = \sum_{j=0}^k (-1)^{k-j} \left[\begin{smallmatrix} k \\ j \end{smallmatrix}\right] x^j$ in $O(k^2)$ time.
  - *Hint 2*: Write $f_n = c_1 \alpha^n + c_2 \beta^n \in \mathbb{F}_p[\sqrt{d}]$ and expand $f_n^j = \sum_{a=0}^j \binom{j}{a} c_1^a c_2^{j-a} (\alpha^a \beta^{j-a})^n$.
  - *Hint 3*: Sum the geometric series $\sum_{n=L}^R r^n$ with $r = \alpha^a \beta^{j-a} \in \mathbb{F}_p[\sqrt{d}]$ in $O(\log R)$ time per pair $(j, a)$ (handling $r = 1$ as $R - L + 1$).
- **Full Derivation Sketch**:
  Working in the quadratic field extension $\mathbb{F}_p[\sqrt{d}]$ (where neither $5$ nor $3$ is a quadratic residue mod $998244353$), we precompute unsigned Stirling numbers $\left[\begin{smallmatrix} k \\ j \end{smallmatrix}\right]$ and binomial coefficients $\binom{j}{a}$ up to $k \le 501$. Interchanging the sums over $n, j, a$ decouples $n$:
  $$\sum_{n=L}^R \binom{f_n}{k} = \frac{1}{k!} \sum_{j=0}^k (-1)^{k-j} \left[\begin{matrix} k \\ j \end{matrix}\right] \sum_{a=0}^j \binom{j}{a} c_1^a c_2^{j-a} \sum_{n=L}^R (\alpha^a \beta^{j-a})^n \pmod{998244353},$$
  evaluated in **$O(k^2 \log R)$** time per testcase.

---

#### Problem 19: Codeforces 1349F1 / 1349F2 — Slime and Sequences (Hard Version)
- **Source**: [Codeforces 1349F2](https://codeforces.com/problemset/problem/1349/F2) *(Cohort 2)*
- **Mathematical Statement**: A sequence $a_1, \dots, a_n$ is *good* if whenever $k > 1$ appears in $a$, the last occurrence of $k-1$ appears strictly before the first occurrence of $k$. For each $1 \le k \le n \le 10^5$, compute the total number of occurrences of $k$ across all good sequences of length $n$, modulo $998244353$.
- **Constraints**: $1 \le n \le 10^5$ (F2), $1 \le n \le 5000$ (F1).
- **Diagnostic Bridge**: By the standardization bijection to permutations $\pi \in S_n$ (listing indices of $1$ in decreasing order, then indices of $2$ in decreasing order, etc.), there are $n!$ good sequences of length $n$, and the occurrences of $k$ are governed by the **Eulerian numbers** $\left\langle\begin{smallmatrix} m \\ k-1 \end{smallmatrix}\right\rangle$ via the **Bivariate Eulerian Mixed EOGF** $E(x, y) = \frac{1 - y}{\exp((y-1)x) - y}$. Applying the power-series substitution $u = (y - 1)x$ (Section 2.4) transforms $E(x, y)$ into $\frac{1}{1 - x H(u)}$ with $H(u) = \frac{e^u - 1}{u}$, and Lagrange–Bürmann residue substitution reduces the entire table to 1D FPS operations in $O(n \log n)$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Biject good sequences of length $n$ to permutations $\pi \in S_n$ to show that the total occurrences of $k$ equal $n! \sum_{m=k}^n \frac{1}{m!} \left\langle\begin{smallmatrix} m \\ k-1 \end{smallmatrix}\right\rangle$ (or equivalently $n! [x^n y^{k-1}]$ of the boundary-adjusted Eulerian Mixed EOGF).
  - *Hint 2*: Use the Eulerian Mixed EOGF $E(x, y) = \sum_{m \ge 0} \sum_{j=0}^m \left\langle\begin{smallmatrix} m \\ j \end{smallmatrix}\right\rangle y^j \frac{x^m}{m!} = \frac{1 - y}{\exp((y-1)x) - y}$. Substitute $u = (y - 1)x$ so $E(x, y) = \frac{1}{1 - x H(u)}$ where $H(u) = \frac{e^u - 1}{u}$, giving $[x^m] E(x, y) = \sum_{j=0}^{m-1} (y-1)^j [u^j] H(u)^m$.
  - *Hint 3*: To compute $c_j = \sum_{m=1}^n [u^j] H(u)^m$ for all $0 \le j < n$ simultaneously, apply the formal residue change of variables $t = G(u) = \frac{u}{H(u)}$ (or $H(u)^{-(n+1)}$ via Lagrange Inversion) in $O(n \log n)$ time, followed by a single Taylor shift from $w = y - 1$ to $y$!
- **Full Derivation Sketch**:
  Under the standardization bijection, the total number of occurrences of $k$ across all $n!$ good sequences is $n! \sum_{m=k}^n \frac{1}{m!} \left\langle\begin{smallmatrix} m \\ k-1 \end{smallmatrix}\right\rangle$. By Section 2.4 (Form C of the Eulerian Mixed EOGF), substituting $u = (y-1)x$ into $E(x, y) = \frac{1-y}{\exp((y-1)x)-y}$ yields
  $$E(x, y) = \frac{1}{1 - x H(u)}, \qquad H(u) = \frac{e^u - 1}{u} = \sum_{j=0}^\infty \frac{u^j}{(j+1)!},$$
  so $\frac{1}{m!} \sum_{k=1}^m \left\langle\begin{smallmatrix} m \\ k-1 \end{smallmatrix}\right\rangle y^{k-1} = [x^m] E(x, y) = \sum_{j=0}^{m-1} (y - 1)^j [u^j] H(u)^m$. Summing over $m$ reduces to extracting $[u^j] \frac{1 - w^{n+1} H(u)^{n+1}}{1 - w H(u)}$ along the diagonal $w^j u^j$. By the Lagrange–Bürmann residue substitution $v = \frac{u}{H(u)}$ (with $\phi(u) = H(u) = \frac{e^u - 1}{u}$), all diagonal coefficients $[u^j] H(u)^{j+r}$ reduce to a single 1D FPS power $H(u)^{-(n+1)} \bmod u^{n+2}$, one 1D FPS inversion $(1 - H(u) + u H'(u))^{-1}$, and one Taylor shift $w = y - 1 \mapsto y$, running in **$O(n \log n)$** time and $O(n)$ space.

---

#### Problem 20: QOJ #4815 — Bivariate Walk with Bounded Height & Weight
- **Source**: [QOJ #4815](https://qoj.ac/problem/4815) *(Cohort 2)*
- **Mathematical Statement**: Given a directed graph on $d \le 15$ vertices where each edge $(u, v)$ has weight $w \in \{0, 1, \dots, c\}$, count walks of length $N \le 10^{18}$ from vertex $1$ to vertex $d$ with total weight $0 \le k \le K$ ($K \le 10^4$), modulo $998244353$.
- **Constraints**: $d \le 15$, $N \le 10^{18}$, $K \le 10^4$.
- **Diagnostic Bridge**: By the transfer-matrix formula, the walk generating function is $[x^N y^k] \frac{P(x, y)}{Q(x, y)}$ where $Q(x, y) = \det(I - x A(y))$ has $\deg_x Q \le d$ and $\deg_y Q \le c d$. Since $N \le 10^{18}$ and $d K \le 1.5 \times 10^5$, this is the canonical **Regime A / B 2D Bostan–Mori** application!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Compute the characteristic polynomial $Q(x, y) = \det(I - x A(y)) \bmod y^{K+1}$ and numerator $P(x, y)$ by evaluating $y$ at $L > K$ roots of unity and running Faddeev–LeVerrier / Gaussian elimination in $O(L d^3)$.
  - *Hint 2*: Apply **Regime B**: for each of the $L$ roots of unity $y_r = \omega^r$, run 1D Bostan–Mori of degree $d$ in $x$ to extract $[x^N] \frac{P(x, \omega^r)}{Q(x, \omega^r)}$ in $O(d \log d \log N)$ (or **Regime A**: run 2D Bostan–Mori directly in $(\mathbb{F}_p[y]/(y^{K+1}))[[x]]$).
  - *Hint 3*: Run a single 1D INTT of length $L$ on the $L$ scalar answers to recover $[x^N y^k]$ for all $0 \le k \le K$!
- **Full Derivation Sketch**:
  Let $A(y) \in \mathbb{F}_p[y]^{d \times d}$ be the weighted adjacency matrix. By Cramer's rule, the walk generating function from $1$ to $d$ is $\frac{P(x,y)}{Q(x,y)} \bmod y^{K+1}$ where $Q(x, y) = \det(I - x A(y))$ has $\deg_x Q \le d$. In **Regime A**, we pack $(x, y) \bmod y^{K+1}$ via Kronecker substitution $x \mapsto z^{2K+1}, y \mapsto z$ and run $\lfloor \log_2 N \rfloor + 1$ steps of 2D Bostan–Mori (truncating $\bmod y^{K+1}$ after each step) in **$O(d K \log(dK) \log N)$** time; in **Regime B** (when $\deg_y A^N \le K$ or after polynomial division $\bmod y^{K+1}$), evaluating at $y = \omega^r$ ($0 \le r < L$), running $L$ scalar 1D Bostan–Mori calls of degree $d$, and interpolating takes **$O(K d \log d \log N + K d^3)$** time.

---

#### Problem 21: AtCoder ABC 387 G — Prime Circuit
- **Source**: [AtCoder ABC 387 G](https://atcoder.jp/contests/abc387/tasks/abc387_g) *(Cohort 2)*
- **Mathematical Statement**: Count connected labeled graphs on $N \le 2.5 \times 10^5$ vertices in which every simple cycle has prime length $p \ge 3$ (a prime-cycle cactus graph), modulo $998244353$.
- **Constraints**: $1 \le N \le 2.5 \times 10^5$.
- **Diagnostic Bridge**: Two cycles sharing an edge would create a third simple cycle whose length makes at least one of the three cycle lengths composite ($a+b, b+c, c+a$ cannot all be odd primes since their sum $2(a+b+c)$ is even!). Thus every valid graph is a **cactus** whose blocks are bridges ($K_2$) and odd prime cycles ($C_p$). Its rooted EGF $T(x)$ satisfies $T(x) = x G(T(x))$ with $G(u) = \exp\left(u + \sum_{p \ge 3 \text{ prime}} \frac{u^{p-1}}{2}\right)$, solved in $O(N \log N)$ for a single $N$ via 1D Lagrange Inversion or $O(N \log^2 N)$ for all $1 \le n \le N$ via **Kinoshita–Li 2D Bostan–Mori**!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Prove that any two cycles sharing an edge in a graph create three paths of lengths $a, b, c \ge 1$ between two branch vertices, and $a+b, b+c, c+a$ cannot all be odd primes. Hence every block is either a bridge ($u$) or a prime cycle $C_p$ ($\frac{u^{p-1}}{2}$ rooted at a vertex), giving $T(x) = x G(T(x))$.
  - *Hint 2*: Compute $G(u) = \exp\left(u + \sum_{3 \le p \le N \text{ prime}} \frac{u^{p-1}}{2}\right) \bmod u^{N+1}$ in $O(N \log N)$.
  - *Hint 3*: To extract the single coefficient $[x^N] T(x)$, apply 1D Lagrange Inversion $[x^N] T(x) = \frac{1}{N} [u^{N-1}] G(u)^N$ in $O(N \log N)$; to compute the entire series $T(x) \bmod x^{N+1}$, apply Kinoshita–Li 2D Bostan–Mori compositional inverse to $f(u) = u / G(u)$ in $O(N \log^2 N)$.
- **Full Derivation Sketch**:
  Let $B(u) = u + \frac{1}{2} \sum_{3 \le p \le N \text{ prime}} u^{p-1}$ be the EGF of blocks rooted at a vertex. By the Block-Tree Theorem, the vertex-rooted connected graph EGF $T(x)$ satisfies $T(x) = x \exp(B(T(x)))$. Unrooting divides $[x^N] T(x)$ by $N$, and applying 1D Lagrange Inversion to $T(x) / \exp(B(T(x))) = x$ gives
  $$\text{Ans} = N! \cdot \frac{1}{N} [x^N] T(x) = (N-1)! \cdot \frac{1}{N} [u^{N-1}] \exp\big(N \cdot B(u)\big) \pmod{998244353},$$
  computed with a single univariate FPS `exp` in **$O(N \log N)$** time (and for all $1 \le n \le N$ simultaneously, Kinoshita–Li 2D Bostan–Mori computes $T(x) \bmod x^{N+1}$ in **$O(N \log^2 N)$** time).

---

#### Problem 22: Yukicoder No. 1080 / Luogu P6667 — Generalized Delannoy & Algebraic Diagonal Walks
- **Source**: [Yukicoder No. 1080](https://yukicoder.me/problems/no/1080) / [Luogu P6667](https://www.luogu.com.cn/problem/P6667) *(Cohorts 1 & 2)*
- **Mathematical Statement**: Compute the diagonal coefficients $d_n = [x^n y^n] \frac{1}{1 - a x - b y - c x y} \bmod 998244353$ for all $0 \le n \le N$ ($N \le 10^6$).
- **Constraints**: $1 \le N \le 10^6$, $a, b, c \in \mathbb{F}_p$.
- **Diagnostic Bridge**: By **Furstenberg's Theorem (Theorem 5.3)**, substituting $(x, y) \mapsto (z, t/z)$ in $K((z))[[t]]$ and taking the residue at the unique small root $z_1(t)$ converts the 2D rational diagonal into the 1D algebraic function $D(t) = \big((1 - ct)^2 - 4abt\big)^{-1/2}$, which satisfies a 3-term linear P-recursion in $O(N)$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Apply $\operatorname{Diag}_{x,y} \frac{1}{1 - ax - by - cxy} = \operatorname{res}_z \frac{1}{-a z^2 + (1-ct)z - bt} = \big((1 - ct)^2 - 4abt\big)^{-1/2}$.
  - *Hint 2*: Set $\Delta(t) = 1 - 2(c + 2ab)t + c^2 t^2$ so $D(t) = \Delta(t)^{-1/2}$, and differentiate logarithmically: $2 \Delta(t) D'(t) + \Delta'(t) D(t) = 0$.
  - *Hint 3*: Extract $[t^n]$ to obtain the 3-term recurrence $(n+1) d_{n+1} = (2n+1)(c + 2ab) d_n - n c^2 d_{n-1}$.
- **Full Derivation Sketch**:
  By Theorem 5.3, $D(t) = \sum_{n=0}^\infty d_n t^n = \operatorname{CT}_z \frac{1}{1 - az - b(t/z) - ct} = \operatorname{res}_z \frac{1}{z(1 - ct) - az^2 - bt}$. The denominator has a unique small root $z_1(t) = \frac{(1-ct) - \sqrt{(1-ct)^2 - 4abt}}{2a} \in t K[[t]]$, at which the residue is
  $$D(t) = \frac{1}{\sqrt{(1 - ct)^2 - 4abt}} = \big(1 - 2(c + 2ab)t + c^2 t^2\big)^{-1/2}.$$
  Differentiating $\Delta(t) D(t)^2 = 1$ yields $2\big(1 - 2(c+2ab)t + c^2 t^2\big) D'(t) + \big(-2(c+2ab) + 2c^2 t\big) D(t) = 0$. Extracting $[t^n]$ gives $d_0 = 1$, $d_1 = c + 2ab$, and
  $$d_{n+1} = \frac{(2n+1)(c + 2ab) d_n - n c^2 d_{n-1}}{n + 1} \pmod{998244353},$$
  computing all $d_0, \dots, d_N$ in **$O(N)$** time and $O(1)$ auxiliary space!

---

### Tier 4: `Mastery` (Problems 23–28)

#### Problem 23: AtCoder ARC 154 F — Dice Game
- **Source**: [AtCoder ARC 154 F](https://atcoder.jp/contests/arc154/tasks/arc154_f) *(Cohort 1)*
- **Mathematical Statement**: Roll a fair $N$-sided die until all $N$ faces appear at least once ($T$ rolls). Compute $\mathbb{E}[T^k] \bmod 998244353$ for all $1 \le k \le M$ ($N, M \le 2 \times 10^5$).
- **Constraints**: $1 \le N, M \le 2 \times 10^5$.
- **Diagnostic Bridge**: The PGF of the coupon collector waiting time is $P(x) = \sum_{t=0}^\infty \mathbb{P}(T = t) x^t = \prod_{i=0}^{N-1} \frac{\frac{N-i}{N} x}{1 - \frac{i}{N} x}$. The moment generating function is $P(e^z) = \sum_{k=0}^M \mathbb{E}[T^k] \frac{z^k}{k!} \bmod z^{M+1}$. Instead of expanding $P(x)$ in $x$, multiply out $P(x) = \frac{A(x)}{B(x)}$ as a degree-$N$ rational function in $O(N \log^2 N)$ and compose $A(e^z)$ and $B(e^z) \bmod z^{M+1}$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Write $P(x) = \frac{N!}{N^N} x^N \prod_{i=1}^{N-1} \frac{1}{1 - \frac{i}{N} x} = \frac{A(x)}{B(x)}$ where $B(x) = \prod_{i=1}^{N-1} (1 - \frac{i}{N} x)$ is computed via a D&C NTT product tree in $O(N \log^2 N)$.
  - *Hint 2*: Notice that for any polynomial $R(x) = \sum_{j=0}^N r_j x^j$, its composition with $e^z$ satisfies $R(e^z) = \sum_{j=0}^N r_j e^{jz} = \sum_{k=0}^\infty \left(\sum_{j=0}^N r_j j^k\right) \frac{z^k}{k!}$.
  - *Hint 3*: Compute the power sums $s_k = \sum_{j=0}^N r_j j^k = [z^k] \sum_{j=0}^N \frac{r_j}{1 - j z}$ up to $k = M$ via D&C NTT on the fractions $\frac{r_j}{1 - j z}$, divide $[z^k]$ by $k!$ to get $A(e^z)$ and $B(e^z) \bmod z^{M+1}$, and compute $A(e^z) B(e^z)^{-1} \bmod z^{M+1}$!
- **Full Derivation Sketch**:
  Waiting times $T = \sum_{i=0}^{N-1} T_i$ of independent geometric random variables have PGF $P(x) = \frac{A(x)}{B(x)}$ where $A(x) = \frac{N!}{N^N} x^N$ and $B(x) = \prod_{i=1}^{N-1} (1 - \frac{i}{N} x)$. Using a binary D&C NTT tree, we first expand $B(x) = \sum_{j=0}^{N-1} b_j x^j$ in $O(N \log^2 N)$ time. Next, to evaluate $B(e^z) \bmod z^{M+1}$, we apply the Laplace-to-OGF identity:
  $$k! [z^k] B(e^z) = \sum_{j=0}^{N-1} b_j j^k = [z^k] \sum_{j=0}^{N-1} \frac{b_j}{1 - j z},$$
  summing the $N$ fractions $\frac{b_j}{1 - j z}$ via a second D&C NTT tree and one 1D FPS inversion up to $z^{M+1}$. Finally, $P(e^z) = A(e^z) B(e^z)^{-1} \bmod z^{M+1}$ yields all $\mathbb{E}[T^k] = k! [z^k] P(e^z)$ ($1 \le k \le M$) in **$O((N + M) \log^2(N + M))$** time!

---

#### Problem 24: UOJ #596 — 【集训队互测2021】三维立体混元劲
- **Source**: [UOJ #596](https://uoj.ac/problem/596) *(Cohorts 1 & 2)*
- **Mathematical Statement**: Count connected labeled 3-colored graphs with $a \le A$ red, $b \le B$ green, and $c \le C$ blue vertices ($A, B, C \le 50$) weighted by edge fugacities, modulo $998244353$.
- **Constraints**: $1 \le A, B, C \le 50$ ($N = (A+1)(B+1)(C+1) \le 132,651$).
- **Diagnostic Bridge**: By the Multivariate Exponential Formula (Theorem 2.2), the connected 3-colored graph EGF is $F(x, y, z) = \ln G(x, y, z) \bmod (x^{A+1}, y^{B+1}, z^{C+1})$. Naive 3D zero-padded FFT pads $51 \times 51 \times 51$ to $128^3 = 2,097,152$ ($16\times$ blowup and TLE), whereas **Twisted Kronecker ($\chi$-Graded) 3D FPS $\ln$** with the radial Euler operator $\mathfrak{D}$ uses FFT length $2^{18} = 262,144$ ($8\times$ smaller)!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Build the disconnected 3-colored graph EGF $G(x, y, z) = \sum_{a,b,c} \frac{\alpha^{\binom{a}{2}}\beta^{\binom{b}{2}}\gamma^{\binom{c}{2}} \lambda_{rg}^{ab}\lambda_{gb}^{bc}\lambda_{br}^{ca}}{a! b! c!} x^a y^b z^c$ in $O(ABC)$ using $i j = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$.
  - *Hint 2*: Pack $(a, b, c) \in [0, A] \times [0, B] \times [0, C]$ into $I = a + b(A+1) + c(A+1)(B+1) \in [0, N-1]$ with carry-tracking residue $\chi(I) = (b + c) \bmod 3$ (Section 3.3).
  - *Hint 3*: Compute $G^{-1}$ via 1D Kronecker-index Newton doubling using 3-graded multiplication $\cdot_\chi$, then extract $\ln G = \mathfrak{D}^{-1}\big(\mathfrak{D}(G) \cdot_\chi G^{-1}\big)$.
- **Full Derivation Sketch**:
  Let $N = (A+1)(B+1)(C+1) \le 132,651$. Under the Kronecker bijection $\phi(a, b, c) = a + b(A+1) + c(A+1)(B+1)$ and grading $\chi(a, b, c) = (b + c) \bmod 3$, Theorem 3.1 guarantees that for $I_1 + I_2 = I < N$, componentwise addition holds if and only if $\chi(I_1) + \chi(I_2) \equiv \chi(I) \pmod 3$. Using the `MultivariateFPS` template (Appendix A.2) with $d = 3$ and dimensions $(A+1, B+1, C+1)$, we compute $G^{-1}$ via Newton doubling and $\ln G(x, y, z) = \mathfrak{D}^{-1}(\mathfrak{D}(G) \cdot_\chi G^{-1})$ in **$O(3 ABC \log(ABC))$** time (~180 ms).

---

#### Problem 25: yukicoder No. 1783 — Remix Sum
- **Source**: [yukicoder No. 1783](https://yukicoder.me/problems/no/1783) *(Cohort 1)*
- **Mathematical Statement**: Given $N$ $K$-digit base-10 integers ($10^K \le 10^5$) where each digit position $r \in \{1, \dots, K\}$ adds either cyclically $\pmod{10}$ ($\text{Carry}=0$, i.e. modulo $z_r^{10}-1$) or with truncation $< 10$ ($\text{Carry}=1$, discarding sums $\ge 10$, i.e. modulo $z_r^{10}$), compute for every target $v \in [0, 10^K - 1]$ the number of $M$-tuples summing to $v$, modulo the prime **$P = 120586241$**.
- **Constraints**: $K \le 5$, $10^K \le 10^5$, $M \le 10^{18}$, prime modulus **$P = 120586241 = 2^{20} \cdot 115 + 1$** (specifically chosen so that $10 \mid (P - 1)$ and $2^{20} \mid (P - 1)$).
- **Diagnostic Bridge**: We need $F(z_1, \dots, z_K)^M$ in the hybrid tensor ring $\bigotimes_{r \notin \mathcal{T}} \frac{\mathbb{F}_P[z_r]}{(z_r^{10}-1)} \otimes \bigotimes_{r \in \mathcal{T}} \frac{\mathbb{F}_P[z_r]}{(z_r^{10})}$. Notice why the modulus is $P = 120586241$ instead of $998244353$: $998244353 - 1$ is not divisible by $10$, whereas $P - 1 = 120586240$ is divisible by $10$, so $\mathbb{F}_P^\times$ has a primitive $10$-th root of unity $\omega_{10} = g^{(P-1)/10} \bmod P$! First apply a $(K - T)$-dimensional radix-10 DFT along the cyclic dimensions, decoupling the problem into $10^{K-T}$ independent **$T$-variate truncated FPS power** instances of size $10^T$, each solved via Twisted Kronecker $\exp(M \ln F)$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Find a primitive root $g$ of $P = 120586241$, set $\omega_{10} = g^{(P-1)/10} \bmod P$, and run radix-10 forward DFT along all $K - T$ cyclic dimensions ($r \notin \mathcal{T}$) in $O((K - T) \cdot 10 \cdot 10^K)$ time.
  - *Hint 2*: For each of the $10^{K-T}$ frequency slices, we have a $T$-variate truncated polynomial in $\mathbb{F}_P[z_{r_1}, \dots, z_{r_T}] / (z_{r_1}^{10}, \dots, z_{r_T}^{10})$ of volume $10^T$.
  - *Hint 3*: Compute $F^M$ on each $T$-variate slice using $\chi$-graded Twisted Kronecker multiplication (`MultivariateFPS` in Appendix A.2, handling $f_{\mathbf{0}} = 0$ via binary exponentiation or lowest-monomial shift), then run the $(K - T)$-dimensional radix-10 IDFT.
- **Full Derivation Sketch**:
  Let $\mathcal{T} \subseteq \{1, \dots, K\}$ be the $T = |\mathcal{T}|$ truncated digit positions. Since $10 \mid (P - 1) = 120586240$, the $(K-T)$-dimensional radix-10 DFT yields an algebra isomorphism
  $$\bigotimes_{r \notin \mathcal{T}} \frac{\mathbb{F}_P[z_r]}{(z_r^{10}-1)} \otimes \bigotimes_{r \in \mathcal{T}} \frac{\mathbb{F}_P[z_r]}{(z_r^{10})} \xrightarrow{\sim} \prod_{\omega \in \mu_{10}^{K-T}} \frac{\mathbb{F}_P[z_{r_1}, \dots, z_{r_T}]}{(z_{r_1}^{10}, \dots, z_{r_T}^{10})}.$$
  On each of the $10^{K-T}$ independent $T$-variate fibers of volume $10^T$, we compute $F_\omega^M \bmod (z_{r_1}^{10}, \dots, z_{r_T}^{10})$ via Twisted Kronecker FPS $\exp(M \ln F_\omega)$ (Section 3.3) in $O(T \cdot 10^T \log(10^T))$ time, and apply the radix-10 IDFT, achieving **$O(10^K T^2 \log 10 + 10^{K+1}(K - T))$** total time.

---

#### Problem 26: AtCoder ARC 138 F / QOJ #8528 — General Dense FPS Composition & Power Projection
- **Source**: [QOJ #8528 (Polynomial Composition)](https://qoj.ac/problem/8528) / [Library Checker — Composition of Formal Power Series (Large)](https://judge.yosupo.jp/problem/composition_of_formal_power_series_large) *(Cohort 1)*
- **Mathematical Statement**: Given $f(x), g(x) \in \mathbb{F}_{998244353}[[x]] / (x^n)$ with $n \le 2 \times 10^5$, compute $g(f(x)) \bmod x^n$ and the power projections $w_k = [x^{n-1}] g(x) f(x)^k$ ($0 \le k < n$).
- **Constraints**: $1 \le n \le 2 \times 10^5$, time limit 5.0s.
- **Diagnostic Bridge**: Brent–Kung baby-step giant-step costs $O((n \log n)^{3/2} + n^2)$ and TLEs for $n = 2 \times 10^5$. **Kinoshita–Li (2024) Regime C 2D Bostan–Mori** solves Power Projection via forward $x$-halving / $y$-doubling on $\frac{g(x)}{1 - y f(x)} \bmod x^n$ and FPS Composition via its Tellegen transpose in **$O(n \log^2 n)$**!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Strip $c = f(0)$ by replacing $g(y) \gets g(y + c)$ via a 1D Taylor shift so that $f(0) = 0$.
  - *Hint 2*: In the forward loop $j = 0, \dots, L-1$, compute $Q_{j+1}(x, y)$ from $Q_j(x, y) Q_j(-x, y)$ where $\deg_x Q_j < \lceil n / 2^j \rceil$ and $\deg_y Q_j \le 2^j$, keeping the total coefficient volume $N_j K_j = \Theta(n)$ invariant at every level!
  - *Hint 3*: For Power Projection, transform $P_j \mapsto P_{j+1}$ top-down; for FPS Composition, initialize $P_L(0, y) = \sum_{k=0}^{n-1} g_k y^{n-1-k}$ at the bottom and apply the transposed middle product $P_{j+1} \mapsto P_j$ bottom-up!
- **Full Derivation Sketch**:
  By Section 4.3 (Regime C), the power projection generating function $\sum_{k=0}^{n-1} w_k y^k = [x^{n-1}] \frac{g(x)}{1 - y f(x)} \bmod y^n$ starts with $P_0(x, y) = g(x), Q_0(x, y) = 1 - y f(x)$ of bidegree $(n-1, 1)$. At each step $j$, multiplying by $Q_j(-x, y)$, extracting the parity of $(n-1) \gg j$ in $x$, and truncating $\bmod y^{2^{j+1}}$ halves the $x$-degree while doubling the $y$-degree via 1D Kronecker-packed NTTs of size $O(n)$. Reversing the linear dataflow graph via Tellegen's Transposition Principle (Section 4.3.2) computes $g(f(x)) \bmod x^n$ in the exact same number of FFTs. Full production-grade C++20 implementations of both `power_projection` and `fps_composition` are given in **Appendix A.3**. Total time: **$O(n \log^2 n)$** (~350 ms for $n = 2 \times 10^5$).

---

#### Problem 27: LOJ #6728 / UOJ #604 — 2D Lattice Walk Return to Origin
- **Source**: [UOJ #604](https://uoj.ac/problem/604) *(Cohort 2)*
- **Mathematical Statement**: Given a 2D step generator $S(x, y) = \sum_{i, j \in \{-1, 0, 1\}} w_{i, j} x^i y^j \in \mathbb{F}_p[x, x^{-1}, y, y^{-1}]$, compute for all $1 \le n \le N$ ($N \le 10^5$) the number of $n$-step walks returning to $(0, 0)$ for the **first time** at step $n$, modulo $998244353$.
- **Constraints**: $1 \le N \le 10^5$.
- **Diagnostic Bridge**: Total returns to $(0, 0)$ have OGF $R(t) = \operatorname{CT}_{x, y} \frac{1}{1 - t S(x, y)}$, and first returns have OGF $F(t) = 1 - \frac{1}{R(t)} \bmod t^{N+1}$. Since $S(x, y)$ has degree $\le 1$ in $x$ and $x^{-1}$, extracting $\operatorname{CT}_x$ first is a quadratic residue in $x$, leaving a 1D algebraic residue in $y$ that is D-finite of bounded order!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Write $S(x, y) = A(y) x + B(y) + C(y) x^{-1}$ where $A, B, C \in \mathbb{F}_p[y, y^{-1}]$ are Laurent polynomials of degree $\le 1$.
  - *Hint 2*: Extract $\operatorname{CT}_x \frac{1}{1 - t S(x, y)} = \frac{1}{\sqrt{(1 - t B(y))^2 - 4 t^2 A(y) C(y)}}$ using Furstenberg's quadratic root formula in $x$.
  - *Hint 3*: Extract $\operatorname{CT}_y$ of the resulting 1D algebraic Laurent series via its D-finite P-recursion (or 1D NTT doubling) to get $R(t) \bmod t^{N+1}$, then compute $F(t) = 1 - R(t)^{-1} \bmod t^{N+1}$.
- **Full Derivation Sketch**:
  Any unconstrained 2D walk returning to $(0,0)$ decomposes uniquely as a sequence of first-return excursions, so $R(t) = \frac{1}{1 - F(t)} \iff F(t) = 1 - \frac{1}{R(t)}$. Writing $1 - t S(x, y) = -t A(y) x + (1 - t B(y)) - t C(y) x^{-1}$ and applying Theorem 5.3 with respect to $x$ eliminates $x$ in closed form:
  $$R(t) = \operatorname{CT}_y \operatorname{CT}_x \frac{1}{1 - t S(x, y)} = \operatorname{CT}_y \frac{1}{\sqrt{(1 - t B(y))^2 - 4 t^2 A(y) C(y)}}.$$
  Because $\Delta(y, t) = (1 - t B(y))^2 - 4 t^2 A(y) C(y)$ is a Laurent polynomial of degree $\le 2$ in $y$, $R(t) = \operatorname{CT}_y \Delta(y, t)^{-1/2}$ is D-finite of order $\le 4$. Computing $R(t) \bmod t^{N+1}$ via its P-recursion in $O(N)$ time and inverting $1 - R(t)^{-1} \bmod t^{N+1}$ via 1D Newton iteration takes **$O(N \log N)$** time.

---

#### Problem 28: Frobenius Bivariate Diagonal & MacMahon's Master Theorem / Generalized Dixon Cubes
- **Source**: Bostan–Christol–Dumas (2016) / I. J. Good (1962) / Contest Synthesis *(Cohorts 2 & 3)*
- **Mathematical Statement**:
  1. **(Part A — Cyclic Linear-Form Diagonal via MMT)**: Given a $3 \times 3$ matrix $A = (a_{ij}) \in \mathbb{F}_p^{3 \times 3}$ and $N \le 10^6$, compute $D_n = [x^{n} y^{n} z^{n}] \prod_{i=1}^3 (a_{i1} x + a_{i2} y + a_{i3} z)^n \bmod 998244353$ for all $0 \le n \le N$.
  2. **(Part B — Huge-$N$ Modulo Small Prime $p$)**: Given $N \le 10^{18}$ and a small prime $p \le 101$, compute $[x^N y^N z^N] \frac{1}{\det(I_3 - \operatorname{diag}(x,y,z) A)} \bmod p$.
- **Constraints**: Part A: $N \le 10^6, p = 998244353$; Part B: $N \le 10^{18}, p \le 101$.
- **Diagnostic Bridge**:
  - In **Part A**, expanding $\prod_{i=1}^3 L_i(x,y,z)^n$ directly for each $n$ is impossible, but **MacMahon's Master Theorem (Theorem 5.4)** collapses $D_n$ for *all* $n$ simultaneously into the diagonal $[x^n y^n z^n] \frac{1}{\det(I_3 - X A)}$ of a single fixed rational function! Furthermore, when $A$ is skew-symmetric ($a_{ij} = -a_{ji}, a_{ii} = 0$), $\det(I_3 - X A) = 1 + a_{12}^2 xy + a_{23}^2 yz + a_{31}^2 zx$, reducing to Dixon's identity!
  - In **Part B**, **Regime D (Bostan–Christol–Dumas Frobenius Reduction)** uses $Q(x,y,z)^p \equiv Q(x^p, y^p, z^p) \pmod p$ to extract $[x^N y^N z^N]$ in $O(\log_p N)$ steps!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Apply MacMahon's Master Theorem to rewrite $D_n = [x^n y^n z^n] \frac{1}{\det(I_3 - \operatorname{diag}(x,y,z) A)}$.
  - *Hint 2*: Expand $Q(x,y,z) = \det(I_3 - X A) = 1 - (\alpha x + \beta y + \gamma z) + (\delta xy + \epsilon yz + \zeta zx) - \eta xyz$. Eliminate $z$ via $\operatorname{CT}_z$ to reduce $\sum_{n \ge 0} D_n t^n$ to a 1D algebraic diagonal with a bounded-order P-recursion in $O(N)$!
  - *Hint 3*: For $N \le 10^{18}$ modulo a small prime $p$ (where the P-recursion divides by multiples of $p$), iterate $P_{k+1}(x,y,z) = \mathcal{S}_{N_k \bmod p}\big(P_k(x,y,z) Q(x,y,z)^{p-1}\big) \bmod p$ where $\mathcal{S}_r$ extracts exponents $\equiv (r, r, r) \pmod p$.
- **Full Derivation Sketch**:
  - **Part A ($O(N)$ via MMT + Furstenberg)**: By Theorem 5.4, $\sum_{n=0}^\infty D_n t^n = \operatorname{Diag}_{x,y,z} Q(x,y,z)^{-1}$ where $Q(x,y,z) = \det(I_3 - \operatorname{diag}(x,y,z) A)$ has multidegree $\le (1, 1, 1)$. Substituting $z \mapsto t / (xy)$ makes $Q(x, y, t/(xy))$ quadratic in $y$, so extracting $\operatorname{CT}_y$ via Furstenberg's residue formula yields $\operatorname{CT}_x \Delta(x, t)^{-1/2}$ where $\Delta(x, t)$ is quartic in $x$, which satisfies a linear P-recursion of order $\le 4$ computable in **$O(N)$** time.
  - **Part B ($O(p^3 \log_p N)$ via Frobenius Sectioning)**: Over $\mathbb{F}_p$, $Q(x,y,z)^p = Q(x^p, y^p, z^p)$, so
    $$[x^N y^N z^N] \frac{P_k(x,y,z)}{Q(x,y,z)} = [x^{\lfloor N/p \rfloor} y^{\lfloor N/p \rfloor} z^{\lfloor N/p \rfloor}] \frac{\mathcal{S}_{N \bmod p}\big(P_k(x,y,z) Q(x,y,z)^{p-1}\big)}{Q(x,y,z)},$$
    where $\deg P_k < (1, 1, 1)$ is preserved at every step! Iterating across the $\lfloor \log_p N \rfloor + 1$ base-$p$ digits of $N$ solves Part B in **$O(p^3 \log_p N)$** time.

---

## 7. Merged Rejected Template Problems Table (Pedagogical Filtering Log)

Both Cohort 1 and Cohort 2 enforced strict pedagogical filtering: problems that merely test black-box template copying without multivariate decoupling, rational parity insight, or diagonal residue transformation were rejected from the main problem bank and are cataloged here for completeness.

| # | Rejected Problem & Source | Judge URL | Flagged By | Reason for Rejection | Superior Pedagogical Replacement |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **R1** | **Library Checker — Kth Term of Linearly Recurrent Sequence** | [Judge](https://judge.yosupo.jp/problem/kth_term_of_linearly_recurrent_sequence) | Cohort 1 & 2 | Pure 1D black-box template verification of `[x^N] P(x)/Q(x)` with zero combinatorial modeling. | **P3 (AtCoder ABC 300 Ex)**, **P11 (AGC 013 E)**, **P13 (UOJ #424)** |
| **R2** | **Luogu P4723 — 【模板】常系数齐次线性递推** | [Luogu](https://www.luogu.com.cn/problem/P4723) | Cohort 1 & 2 | Exact duplicate of R1 in Chinese OJ format; zero generating-function modeling required. | **P13 (UOJ #424)** & **P14 (Codeforces 755G)** |
| **R3** | **Luogu P7439 — 【模板】常系数齐次线性递推 (加强版)** | [Luogu](https://www.luogu.com.cn/problem/P7439) | Cohort 2 | Constant-factor speed test for bit-reversed NTT-domain Bostan–Mori (covered as infrastructure in Section 4.2 & Appendix A.1). | **P3 (AtCoder ABC 300 Ex)** & **P20 (QOJ #4815)** |
| **R4** | **Yukicoder No. 2677 — Simple Linear Recurrence** | [yukicoder](https://yukicoder.me/problems/no/2677) | Cohort 2 | Bare verification problem for $O(d \log d \log N)$ Bostan–Mori without combinatorial disguise. | **P4 (Codeforces 1117D)** & **P11 (AGC 013 E)** |
| **R5** | **Library Checker — Power Projection of Formal Power Series** | [Judge](https://judge.yosupo.jp/problem/power_projection_of_formal_power_series) | Cohort 1 & 2 | Pure verification template for Regime C 2D Bostan–Mori (covered as infrastructure in Section 4.3.2 & Appendix A.3). | **P21 (AtCoder ABC 387 G)** & **P26 (ARC 138 F / QOJ #8528)** |
| **R6** | **Library Checker — Composition of Formal Power Series (Large)** | [Judge](https://judge.yosupo.jp/problem/composition_of_formal_power_series_large) | Cohort 1 & 2 | Pure verification template for Kinoshita–Li $O(n \log^2 n)$ FPS composition (covered in Section 4.3.2 & Appendix A.3). | **P26 (ARC 138 F / QOJ #8528)** |
| **R7** | **Library Checker — Compositional Inverse of Formal Power Series (Large)** | [Judge](https://judge.yosupo.jp/problem/compositional_inverse_of_formal_power_series_large) | Cohort 1 & 2 | Pure verification template for Power Projection + Lagrange Inversion (covered in Section 4.3.3). | **P21 (AtCoder ABC 387 G)** & **P26 (ARC 138 F)** |
| **R8** | **Library Checker — Multivariate Convolution** | [Judge](https://judge.yosupo.jp/problem/multivariate_convolution) | Cohort 1 & 2 | Pure verification template for Section 3.3 Twisted Kronecker $\chi$-graded convolution; zero problem-specific modeling. | **P24 (UOJ #596)** & **P25 (yukicoder No. 1783)** |
| **R9** | **Library Checker — Polynomial Taylor Shift** | [Judge](https://judge.yosupo.jp/problem/polynomial_taylor_shift) | Cohort 1 | Pure 1D convolution identity $\tilde{f}_k k! = \sum_{i \ge k} f_i i! \frac{c^{i-k}}{(i-k)!}$; belongs to Wave 2A, not Wave 4A. | **P19 (Codeforces 1349F2)** & **P26 (ARC 138 F)** |
| **R10** | **Library Checker — Shift of Sampling Points of Polynomial** | [Judge](https://judge.yosupo.jp/problem/shift_of_sampling_points_of_polynomial) | Cohort 1 | Pure 1D Lagrange interpolation on arithmetic progressions; no multivariate coupling or rational diagonal. | **P8 (Luogu P5406)** & **P20 (QOJ #4815)** |
| **R11** | **Codeforces 632E — Thief in a Shop** | [Codeforces](https://codeforces.com/problemset/problem/632/E) | Cohort 2 | 1D boolean subset-sum $[x^w] (\sum x^{a_i})^k$; solved by 1D FFT after shifting by $\min a_i$, no genuine 2D structure. | **P2 (AtCoder ABC 276 G)** & **P6 (Codeforces 623E)** |
| **R12** | **AtCoder ABC 130 E — Common Subsequence** | [AtCoder](https://atcoder.jp/contests/abc130/tasks/abc130_e) | Cohort 2 | Elementary $O(NM)$ 2D prefix-sum DP where $N, M \le 2000$; no FPS speedups or diagonal extraction needed. | **P22 (Yukicoder 1080 / Generalized Delannoy)** |
| **R13** | **SPOJ — FIBOSUM / Matrix Exponentiation Templates** | [SPOJ](https://www.spoj.com/problems/FIBOSUM/) | Cohort 2 | Degree $d = 2$ recurrence; solved in $O(\log N)$ by $2 \times 2$ matrices without polynomial arithmetic. | **P18 (Luogu P5487 — [BJOI2019] 勘破神机)** |

---

## 8. Master Multilingual Bibliography (`[EN]`, `[ZH]`, `[JA]`)

1. **`[EN]` Bostan, A., & Mori, R. (2021).** *A Simple and Fast Algorithm for Computing the $N$-th Term of a Linearly Recurrent Sequence.* SIAM Symposium on Simplicity in Algorithms (SOSA 2021), pp. 118–132. [arXiv:2008.08822](https://arxiv.org/abs/2008.08822). *(Definitive reference for 1D Bostan–Mori, Graeffe root-squaring duality, and the bit-reversed NTT-domain $\frac{2}{3}\mathsf{M}(d)\log_2 N$ optimization.)*
2. **`[EN]` Kinoshita, Y., & Li, B. (2024).** *Power Projection and Composition of Formal Power Series in $O(n \log^2 n)$ Time via Bivariate Bostan–Mori.* Proceedings of ISSAC 2024. [arXiv:2404.05177](https://arxiv.org/abs/2404.05177). *(Introduces Regime C 2D Bostan–Mori $x$-halving / $y$-doubling and its Tellegen transpose for FPS composition and compositional inverse.)*
3. **`[EN]` van der Hoeven, J. (2002).** *Relax, but Don't Be Too Lazy.* Journal of Symbolic Computation, 34(6), 479–542. *(Originates the $\chi$-graded twisted Kronecker substitution for truncated multivariate power series multiplication without zero-padding blowup.)*
4. **`[EN]` Furstenberg, H. (1967).** *Algebraic Functions Over Finite Fields.* Journal of Algebra, 7(2), 271–277. *(Proves both directions of Theorem 5.3: diagonals of bivariate rational functions are algebraic, and every univariate algebraic series is the diagonal of an explicit bivariate rational function.)*
5. **`[EN]` Bousquet-Mélou, M., & Petkovšek, M. (2000).** *Linear Recurrences with Constant Coefficients: the Multivariate Case.* Discrete Mathematics, 225(1–3), 51–75. *(Rigorous foundation of the One- and Two-Boundary Kernel Method in $K((u))[[t]]$ via smallPuiseux roots.)*
6. **`[EN]` Bostan, A., Christol, G., & Dumas, P. (2016).** *Fast Computation of the $N$-th Term of an Algebraic Series Over a Finite Prime Field.* [HAL-01311960](https://hal.science/hal-01311960). *(Establishes Regime D Frobenius reduction $Q(x,y)^p \equiv Q(x^p, y^p) \pmod p$ for huge bivariate diagonals over $\mathbb{F}_p$.)*
7. **`[EN]` MacMahon, P. A. (1915).** *Combinatory Analysis, Vol. 1.* Cambridge University Press, §III, pp. 93–123; and **Good, I. J. (1962)**, *A Short Proof of MacMahon's 'Master Theorem'*, Proc. Cambridge Philos. Soc. 58, 160–161. *(Proves MacMahon's Master Theorem via multivariate contour/formal residues and derives Dixon's binomial identity in 3 lines.)*
8. **`[EN]` Foata, D. (1965).** *Etude algébrique de certains problèmes d'analyse combinatoire et du calcul des probabilités.* Publ. Inst. Statist. Univ. Paris 14, 81–241. *(Combinatorial cycle-decomposition proof of MacMahon's Master Theorem via Lyndon words and Cartier–Foata monoids.)*
9. **`[EN]` Stanley, R. P. (1999).** *Enumerative Combinatorics, Vol. 2.* Cambridge University Press, Chapter 6 (Rational, Algebraic, and D-Finite Generating Functions & Diagonals).
10. **`[EN]` Flajolet, P., & Sedgewick, R. (2009).** *Analytic Combinatorics.* Cambridge University Press, Chapter III (Multivariate Generating Functions & Mixed OGF/EGF Constructors).
11. **`[ZH]` Elegia (2020) & EntropyIncreaser (2021).** *多元形式幂级数的基础操作 / 集合幂级数与多元多项式浅谈.* [EntropyIncreaser Blog](https://entropyincreaser.com/) & UOJ Community Notes. *(Popularized van der Hoeven's $\chi$-graded twisted Kronecker substitution and the radial Euler derivation $\mathfrak{D}$ in Chinese competitive programming, including UOJ #596.)*
12. **`[ZH]` EI / Elegia (2021).** *UOJ #596 【集训队互测2021】三维立体混元劲 题解.* China National Team Training Notes. *(Canonical benchmark for 3-variate truncated FPS $\ln$ via $\chi(I) \bmod 3$.)*
13. **`[ZH]` OI-Wiki Contributors.** *形式幂级数 & 常系数齐次线性递推 (Bostan–Mori) & 复合与拉格朗日反演.* [OI-Wiki](https://oi-wiki.org/math/poly/lagrange/).
14. **`[JA]` Mori, R. (2021).** *線形漸化式の第 $N$ 項を計算するアルゴリズム (Algorithms for Computing the $N$-th Term of a Linear Recurrence).* [Qiita (@ryuhe1)](https://qiita.com/ryuhe1/items/da5acbcce4ac1911f47a). *(Co-author Ryuhei Mori's Japanese exposition of Bostan–Mori, Graeffe's method, MSB-first vs. LSB-first, and bit-reversed NTT doubling.)*
15. **`[JA]` maspy (2024).** *FPS 合成・逆関数の解説 (1) 逆関数と Power Projection / 二変数 Bostan–Mori.* [maspypy.com](https://maspypy.com/fps-%e5%90%88%e6%88%90%e3%83%bb%e9%80%86%e9%96%a2%e6%95%b0%e3%81%ae%e8%a7%a3%e8%aa%ac-1-%e9%80%86%e9%96%a2%e6%95%b0%e3%81%a8-power-projection). *(Details the monic $y$-reversal representation $\widetilde{Q}_j(x,y) = y^{2^j} Q_j(x, y^{-1})$ and $O(n \log^2 n)$ implementation of Kinoshita–Li.)*
16. **`[JA]` noshi91 (2024) & Nyaan.** *Library: Formal Power Series, Bostan–Mori, and Multivariate Polynomials.* [Nyaan's Library](https://nyaannyaan.github.io/library/).

---

## Appendix A: Complete C++20 Reference Implementations

### A.1 Bit-Reversed NTT-Domain 1D Bostan–Mori ($\frac{2}{3}\mathsf{M}(d) \log_2 N$)

```cpp
// Bit-reversed NTT doubling: given hat_A = NTT_L(A) of length L (power of 2) in bit-reversed layout,
// appends NTT_L(A(g^(1/(2L)) x)) to form hat_A of length 2L in bit-reversed layout using 2 NTTs of size L.
void ntt_doubling(vector<mint>& hat_a) {
    int L = (int)hat_a.size();
    vector<mint> a = hat_a;
    ntt(a, true); // INTT of size L
    mint w = mint(PRIMITIVE_ROOT).pow((MOD - 1) / (2 * L)), cur = 1;
    for (int i = 0; i < L; ++i) {
        a[i] *= cur;
        cur *= w;
    }
    ntt(a, false); // NTT of size L
    hat_a.resize(2 * L);
    for (int i = L - 1; i >= 0; --i) {
        hat_a[2 * i]     = hat_a[i];
        hat_a[2 * i + 1] = a[i];
    }
}

// Extracts [x^N] P(x) / Q(x) mod 998244353 in (2/3) M(d) log2(N) via Bit-Reversed NTT-Domain Bostan-Mori
// Assumes deg(P) < deg(Q) = d and Q[0] != 0.
mint bostan_mori(vector<mint> P, vector<mint> Q, uint64_t N) {
    int d = (int)max(P.size(), Q.size()) - 1;
    int half = 1;
    while (half <= d) half <<= 1;
    int L = half << 1;

    P.resize(L, 0);
    Q.resize(L, 0);
    ntt(P, false);
    ntt(Q, false);

    // Precompute bit-reversed inverse twiddle factors for odd/even extraction in bit-reversed order
    vector<mint> inv_w(half);
    inv_w[0] = 1;
    mint w_base = mint(PRIMITIVE_ROOT).pow(MOD - 1 - (MOD - 1) / L);
    for (int k = 1; k < half; k <<= 1) {
        mint step = w_base.pow(half / (2 * k));
        for (int j = 0; j < k; ++j) inv_w[k + j] = inv_w[j] * step;
    }
    mint inv2 = mint(2).inv();

    while (N > 0) {
        vector<mint> U(half), V(half);
        // In bit-reversed layout, (w_i, -w_i) are adjacent at (2*i, 2*i + 1)
        for (int i = 0; i < half; ++i) {
            mint t0 = P[2 * i] * Q[2 * i + 1];
            mint t1 = P[2 * i + 1] * Q[2 * i];
            if ((N & 1) == 0) {
                U[i] = (t0 + t1) * inv2;
            } else {
                U[i] = (t0 - t1) * inv2 * inv_w[i];
            }
            V[i] = Q[2 * i] * Q[2 * i + 1];
        }
        N >>= 1;
        if (N == 0) {
            ntt(U, true);
            ntt(V, true);
            return U[0] * V[0].inv();
        }
        // Extend U and V from size L/2 to size L using only 4 NTTs of size L/2 total!
        ntt_doubling(U);
        ntt_doubling(V);
        P = move(U);
        Q = move(V);
    }
    ntt(P, true);
    ntt(Q, true);
    return P[0] * Q[0].inv();
}
```

---

### A.2 Twisted Kronecker ($\chi$-Graded) Multivariate FPS (`mul`, `inv_prefix`, `inv`, `ln`, `exp`)

```cpp
// Multivariate FPS in F_p[x_1, ..., x_d] / (x_1^{n_1}, ..., x_d^{n_d})
// Complexity: O(d * N * log N) where N = n_1 * n_2 * ... * n_d
struct MultivariateFPS {
    int d, N;
    vector<int> dims, stride, chi;

    MultivariateFPS(const vector<int>& dims_) : d(dims_.size()), dims(dims_), stride(d + 1, 1) {
        for (int r = 0; r < d; ++r) stride[r + 1] = stride[r] * dims[r];
        N = stride[d];
        chi.assign(N, 0);
        for (int I = 0; I < N; ++I) {
            int sum = 0;
            for (int r = 1; r < d; ++r) sum += I / stride[r];
            chi[I] = sum % d;
        }
    }

    // Truncated product mod (x_1^{n_1}, ..., x_d^{n_d}) up to 1D prefix M in O(d M log M)
    vector<mint> mul_prefix(const vector<mint>& A, const vector<mint>& B, int M) const {
        int L = 1;
        while (L < 2 * M - 1) L <<= 1;
        vector<vector<mint>> fA(d, vector<mint>(L, 0)), fB(d, vector<mint>(L, 0));
        for (int I = 0; I < M; ++I) {
            if (I < (int)A.size()) fA[chi[I]][I] = A[I];
            if (I < (int)B.size()) fB[chi[I]][I] = B[I];
        }
        for (int u = 0; u < d; ++u) {
            ntt(fA[u], false);
            ntt(fB[u], false);
        }
        vector<vector<mint>> fC(d, vector<mint>(L, 0));
        for (int u = 0; u < d; ++u) {
            for (int v = 0; v < d; ++v) {
                int w = (u + v >= d ? u + v - d : u + v);
                for (int k = 0; k < L; ++k) fC[w][k] += fA[u][k] * fB[v][k];
            }
        }
        for (int w = 0; w < d; ++w) ntt(fC[w], true);
        vector<mint> C(M, 0);
        for (int I = 0; I < M; ++I) C[I] = fC[chi[I]][I];
        return C;
    }

    vector<mint> mul(const vector<mint>& A, const vector<mint>& B) const {
        return mul_prefix(A, B, N);
    }

    // Prefix Multivariate Inverse up to 1D Kronecker index lim in O(d lim log lim)
    vector<mint> inv_prefix(const vector<mint>& F, int lim) const {
        vector<mint> G(lim, 0);
        G[0] = F[0].inv();
        for (int m = 1; m < lim; m <<= 1) {
            int cur = min(lim, 2 * m);
            auto FG = mul_prefix(F, G, cur);
            for (int I = 0; I < cur; ++I) FG[I] = (I == 0 ? mint(2) - FG[0] : -FG[I]);
            auto nxt = mul_prefix(G, FG, cur);
            for (int I = m; I < cur; ++I) G[I] = nxt[I];
        }
        return G;
    }

    vector<mint> inv(const vector<mint>& F) const {
        return inv_prefix(F, N);
    }

    // Multivariate Logarithm via Radial Euler Derivation D(F)_I = I * F_I (requires F[0] == 1)
    vector<mint> ln(const vector<mint>& F) const {
        vector<mint> DF(N, 0);
        for (int I = 1; I < N; ++I) DF[I] = F[I] * mint(I);
        auto Q = mul(DF, inv(F));
        vector<mint> L(N, 0);
        for (int I = 1; I < N; ++I) L[I] = Q[I] * mint(I).inv();
        return L;
    }

    // Multivariate Exponential in true O(d N log N) via inv_prefix(E, cur) (requires F[0] == 0)
    vector<mint> exp(const vector<mint>& F) const {
        vector<mint> E(N, 0);
        E[0] = 1;
        for (int m = 1; m < N; m <<= 1) {
            int cur = min(N, 2 * m);
            vector<mint> DE(cur, 0);
            for (int I = 1; I < m; ++I) DE[I] = E[I] * mint(I);
            vector<mint> E_cur(E.begin(), E.begin() + cur);
            auto lnE = mul_prefix(DE, inv_prefix(E, cur), cur);
            vector<mint> rhs(cur, 0);
            rhs[0] = 1;
            for (int I = 1; I < cur; ++I) rhs[I] = F[I] - lnE[I] * mint(I).inv();
            auto nxt = mul_prefix(E_cur, rhs, cur);
            for (int I = m; I < cur; ++I) E[I] = nxt[I];
        }
        return E;
    }
};
```

---

### A.3 Kinoshita–Li 2D Bostan–Mori Power Projection & FPS Composition ($O(n \log^2 n)$)

```cpp
// Computes w_k = [x^{n-1}] g(x) f(x)^k for all 0 <= k < n, assuming f[0] == 0.
// Complexity: O(n log^2 n) time, O(n) space.
vector<mint> power_projection(vector<mint> g, vector<mint> f, int n) {
    int N = n, K = 1;
    // Represent 2D polynomials P(x, y) and Q(x, y) as flat arrays
    // where coefficient of x^i y^r is stored at i * stride + r.
    vector<mint> P(N, 0), Q(N * 2, 0);
    for (int i = 0; i < n; ++i) P[i] = (i < (int)g.size() ? g[i] : 0);
    Q[0] = 1;
    for (int i = 1; i < n; ++i) Q[2 * i + 1] = (i < (int)f.size() ? -f[i] : 0);

    int target_x = n - 1;
    while (N > 1) {
        int next_N = (N + 1) >> 1;
        int next_K = K << 1;
        int stride_y = 2 * K + 1;
        // Pack x^i y^r into 1D Kronecker index I = i * stride_y + r
        int M = N * stride_y;
        vector<mint> A(M, 0), B(M, 0), Bm(M, 0);
        for (int i = 0; i < N; ++i) {
            mint sgn = (i & 1) ? mint(-1) : mint(1);
            for (int r = 0; r < K; ++r) A[i * stride_y + r] = P[i * K + r];
            for (int r = 0; r <= K; ++r) {
                mint val = Q[i * (K + 1) + r];
                B[i * stride_y + r] = val;
                Bm[i * stride_y + r] = val * sgn;
            }
        }
        auto U = convolve_1d(A, Bm);
        auto V = convolve_1d(B, Bm);

        int parity = target_x & 1;
        vector<mint> nP(next_N * next_K, 0), nQ(next_N * (next_K + 1), 0);
        for (int i = 0; i < next_N; ++i) {
            int src_x = 2 * i + parity;
            if (src_x < 2 * N - 1) {
                for (int r = 0; r < next_K; ++r) {
                    int idx = src_x * stride_y + r;
                    if (idx < (int)U.size()) nP[i * next_K + r] = U[idx];
                }
            }
            int src_qx = 2 * i;
            if (src_qx < 2 * N - 1) {
                for (int r = 0; r <= next_K; ++r) {
                    int idx = src_qx * stride_y + r;
                    if (idx < (int)V.size()) nQ[i * (next_K + 1) + r] = V[idx];
                }
            }
        }
        P.swap(nP);
        Q.swap(nQ);
        N = next_N;
        K = next_K;
        target_x >>= 1;
    }
    P.resize(n, 0);
    return P;
}

// Computes H(x) = G(F(x)) mod x^n in O(n log^2 n) time (assuming F[0] == 0)
// via the Kinoshita-Li (2024) forward-recursion + Tellegen-transposed 2D Bostan-Mori reduction.
vector<mint> fps_composition(vector<mint> G, vector<mint> F, int n) {
    G.resize(n, 0);
    F.resize(n, 0);

    auto rec = [&](auto& self, const vector<mint>& Q, int deg_y, int deg_x) -> vector<mint> {
        if (deg_x == 1) {
            // Base case: at deg_x = 1, Q(x, y) = 1, and P(0, y) = sum_{j=0}^{n-1} G_j y^{n-1-j}
            vector<mint> P(deg_y + 1, 0);
            for (int j = 0; j < n && n - 1 - j <= deg_y; ++j) {
                P[n - 1 - j] = G[j];
            }
            return P;
        }
        int K = 2 * deg_x;
        int next_deg_y = 2 * deg_y;
        int next_deg_x = (deg_x + 1) / 2;
        int L = 1;
        while (L <= 2 * deg_y * K + 2 * deg_x) L <<= 1;

        vector<mint> A(L, 0), B(L, 0);
        for (int j = 0; j <= deg_y; ++j) {
            for (int i = 0; i < deg_x; ++i) {
                mint v = Q[j * deg_x + i];
                A[j * K + i] = v;
                B[j * K + i] = (i & 1) ? -v : v;
            }
        }
        ntt(A, false);
        ntt(B, false);
        for (int i = 0; i < L; ++i) A[i] *= B[i];
        ntt(A, true);

        vector<mint> next_Q((next_deg_y + 1) * next_deg_x, 0);
        for (int j = 0; j <= next_deg_y; ++j) {
            for (int i = 0; i < next_deg_x; ++i) {
                next_Q[j * next_deg_x + i] = A[j * K + 2 * i];
            }
        }

        // Recursively obtain P_next of bidegree (next_deg_y, next_deg_x - 1)
        vector<mint> P_next = self(self, next_Q, next_deg_y, next_deg_x);

        // Transpose step: spread P_next onto even x-powers and multiply by Q(-x, y) reversed in y
        fill(A.begin(), A.end(), 0);
        for (int j = 0; j <= next_deg_y; ++j) {
            for (int i = 0; i < next_deg_x; ++i) {
                A[j * K + 2 * i] = P_next[j * next_deg_x + i];
            }
        }
        fill(B.begin(), B.end(), 0);
        for (int j = 0; j <= deg_y; ++j) {
            for (int i = 0; i < deg_x; ++i) {
                mint v = Q[j * deg_x + i];
                B[(deg_y - j) * K + i] = (i & 1) ? -v : v;
            }
        }
        ntt(A, false);
        ntt(B, false);
        for (int i = 0; i < L; ++i) A[i] *= B[i];
        ntt(A, true);

        vector<mint> P((deg_y + 1) * deg_x, 0);
        for (int j = 0; j <= deg_y; ++j) {
            for (int i = 0; i < deg_x; ++i) {
                P[j * deg_x + i] = A[(j + deg_y) * K + i];
            }
        }
        return P;
    };

    // Initial denominator Q(x, y) = 1 - y * (F(x) / x) of bidegree (1, n - 1)
    vector<mint> Q0(2 * n, 0);
    Q0[0] = 1;
    for (int i = 1; i < n; ++i) Q0[n + i - 1] = -F[i];

    vector<mint> P0 = rec(rec, Q0, 1, n);
    vector<mint> H(n, 0);
    H[0] = G[0];
    for (int i = 1; i < n; ++i) H[i] = P0[n + i - 1];
    return H;
}
```

