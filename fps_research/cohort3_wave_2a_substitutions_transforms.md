# Wave 2A (Iterations 11–15 / 63–67) Cohort 3 Master Synthesis: Non-Linear Substitutions & Sequence Transforms

**Cohort 3 Cross-Comparison, Blind-Spot Reconciliation & Definitive Reference**  
**Synthesized Sources**:
- **Cohort 1 (`C1`)**: `fps_research/iter_11_to_15_substitutions_transforms.md` (1,760 lines)
- **Cohort 2 New (`C2-New`)**: `fps_research/cohort2_new_iter_63_to_67_substitutions_transforms.md` (1,567 lines)
- **Pre-Existing Cohort 2 (`C2-Pre`)**: `fps_research/cohort2_iter_63_to_67_substitutions_transforms.md` (912 lines)

---

## 1. Three-Way Cross-Cohort Blind-Spot & Coverage Reconciliation Matrix

To eliminate every single-cohort blind spot across our three independent research streams (`C1`, `C2-New`, and `C2-Pre`), we begin with an explicit audit of unique mathematical discoveries, reverse-engineering heuristics, edge-case traps, and contest problems captured by only a subset of the cohorts.

### 1.1 Theoretical & Algorithmic Blind-Spot Matrix

| Iteration / Topic | Cohort 1 (`C1`) Unique Contributions | Cohort 2 New (`C2-New`) Unique Contributions | Pre-Existing Cohort 2 (`C2-Pre`) Unique Contributions | Cohort 3 Unified Resolution |
| :--- | :--- | :--- | :--- | :--- |
| **Algebraic Foundations** | Explicit 3-regime validity classification for $F(G(x))$: (i) $R[[x]]$ ($[x^0]G=0$), (ii) $R[x]$ degree $\le n$, (iii) projective $\mathrm{GL}_2(K)$ action; formal residue proof of Change of Variables $[x^n]F(x) = [u^n]\frac{u}{x(u)}x'(u)F(x(u))$ without Lagrange Inversion. | Focus on matrix factorization of binomial transform and non-vanishing constant-term evaluation traps. | Formal algebraic vs. finite-degree operational boundary table across all five transform families. | Unified in **Section 2** with both the 3-regime validity theorem and the Residue Change-of-Variables Engine. |
| **Iter 11 / 63: Euler, Binomial, Taylor Shift & Möbius** | Formal Borel ($\mathcal{B}$) and Formal Laplace ($\mathcal{L}(\widehat{A})(x) = \int_0^\infty e^{-t}\widehat{A}(xt)dt$) integral operator bridge proving why $\widehat{B}(z) = e^{cz}\widehat{A}(z)$ becomes $B(x) = \frac{1}{1-cx}A(\frac{x}{1-cx})$; idle-step decoupling $G = c + F_{\text{step}}$ for 1D/2D random walks. | Base-$p$ Lucas Theorem + SOS DP fallback when $p \le n$ breaks Taylor Shift division by $k!$; explicit $2\times 2$ matrix factorization $\left(\begin{smallmatrix} 1 & b \\ 0 & 1 \end{smallmatrix}\right)$ of Möbius substitutions. | Rigorous **Bruhat decomposition** of the right projective action $(\mathcal{M}_g F)(x) = (cx+d)^n F(\frac{ax+b}{cx+d})$; explicit reduction of the **Krawtchouk Transform** $K_F(x) = (1+x)^n F(\frac{1-x}{1+x})$ (Hamming scheme eigenvalues) to 2 Taylor shifts; **Generalized Infinite-Series Euler Transform** $E(x) = (1-cx)^{-\alpha}F(\frac{ax}{1-cx}) \bmod x^N$ in 1 NTT via rising factorials $\alpha^{\overline{m}}$ + negative-integer $\alpha=-n$ splitting fix. | Fully merged in **Section 3**, preserving Laplace/Borel bridges, Bruhat $\mathrm{GL}_2(K)$ factorization, Krawtchouk transforms, generalized $\alpha$-Euler transform, and characteristic $p \le n$ Lucas fallbacks. |
| **Iter 12 / 64: Quadratic Radicals, Catalan, Motzkin, Delannoy, Schröder, Narayana & Chebyshev** | Explicit 2D Chebyshev / hexagonal step decoupling via $\mathbb{Q}(\zeta_{12})$ (`FPS-24 V 12 Directions`: $2 + F(x,y) = (x^{1/2}+x^{-1/2})(y^{1/2}+y^{-1/2})((xy)^{1/2}+(xy)^{-1/2})$); cycle-reflection transfer matrix determinant $\det(I - xA) = 1 - Lx^2$. | Side-by-side comparison of the **two Catalan substitutions** ($u = xC(x) \implies x = u(1-u)$ vs. $u = C(x)-1 \implies x = \frac{u}{(1+u)^2}$) explaining negative vs. positive binomial indices; **Characteristic $p=2$ Artin–Schreier** analysis of Catalan series ($C(x) = 1 + xC(x)^2 \implies C_n \equiv 1 \pmod 2 \iff n = 2^k-1$). | Differential logarithmic identity $\frac{1}{\sqrt{1-2ax+bx^2}} = x\frac{d}{dx}\ln u(x)$; **Master Extraction Formulas A & B** (with and without $\frac{1}{\sqrt{\Delta}}$); explicit linear factorization for **Central Delannoy** & **Large Schröder** ($1+3u+2u^2 = (1+u)(1+2u)$); **Model I vs. Model II** Chebyshev bounded-height lattice walk table ($u^{h+1}$ vs. $(cu^2)^{h+1}$). | Merged in **Section 4**, plus an explicit synthesis of **Narayana numbers** $N(n,k) = \frac{1}{n}\binom{n}{k}\binom{n}{k-1}$ via the quadratic peak-tracking substitution $x = \frac{u}{(1+u)(1+tu)}$. |
| **Iter 13 / 65: Transcendental $e^x-1, \ln(1+x)$, Stirling, Lah & Falling Factorials** | Complete side-by-side blueprint and C++ implementations for all 4 $O(n \log n)$ Stirling & Lah regimes (1st/2nd kind $\times$ Fixed Row/Column) and `ffp_from_values`. | Nyaan's `fps/composite-exp.hpp` Borel/Laplace rational sum $\mathcal{L}\{P(e^{cz})\} = \sum_{k=0}^n \frac{p_k}{1-kcz}$ for $O(n \log^2 n)$ monomial-to-FFP transpose conversion; signed vs. unsigned Lah involution matrices. | Complete **5-row complexity table** for conversions between $\{x^k\}$, $\{x^{\underline{k}}\}$, and $\{x^{\overline{k}}\}$, highlighting that Falling $\leftrightarrow$ Rising takes only $O(n \log n)$ (1 convolution) whereas Monomial $\leftrightarrow$ Falling takes $O(n \log^2 n)$; $O(n)$ Binomial Moment Collapse $\sum_{i=0}^m \binom{m}{i} p^i q^{m-i} i^{\underline{k}} = m^{\underline{k}} p^k (p+q)^{m-k}$. | Unified in **Section 5**, including the **Exponential Transform ($\exp/\ln$)** connecting disconnected labeled structures and connected components alongside the EGF-OGF Borel/Laplace bridges. |
| **Iter 14 / 66: Log Derivatives $F'/F$, Euler/Multiset $\operatorname{MSET}/\operatorname{PSET}$, Lyndon/Pólya & Power Sums** | Detailed derivation of $\ln$ vs. $F'/F$ across product-to-sum transforms and elementary-to-power-sum conversion `elementary_to_power_sums`. | **Characteristic $p \le N$ asymmetry**: recovering $e_k$ from $p_k$ fails when $p \le N$ ($p_p = e_1^p$ loses information), whereas computing $p_k$ from $e_k$ via $-xQ'(x)Q(x)^{-1}$ works in *any* characteristic without division by $k$! | Explicit architectural split between **Regime A** (Exponent-Weighted Euler/Multiset $\operatorname{MSET}$ & $\operatorname{PSET}$ Products $\prod(1\pm x^{w_i})^{\pm c_i}$ in $O(N \log N)$ via Frequency Bucketing + Harmonic Sieve) and **Regime B** (Scalar Power Sums $p_k = \sum a_i^k$ in $O(m \log^2 m + N \log N)$ via Subproduct Tree); **Inverse Euler Transform** via Möbius inversion for Lyndon words & unlabeled necklaces. | Unified in **Section 6**, synthesizing Regime A ($\operatorname{MSET}/\operatorname{PSET}$), Inverse Euler Transform (Lyndon words, necklaces, and **Pólya–Redfield Cycle Index**), and Regime B (Newton–Girard + characteristic $p$ asymmetry). |
| **Iter 15 / 67: Roots of Unity Filter (`单位根反演`), Chirp-Z & Cyclotomic Rings** | Explicit `Ext3` C++ struct for $\mathbb{F}_p[\omega]/(\omega^2+\omega+1)$ solving the famous $m=3, p=998244353$ trap ($3 \nmid 998244352$); **Floor-Sum Trick** $\lfloor i/k \rfloor = \frac{i - (i \bmod k)}{k}$ (`CF 891E Lust`). | Parity / mod-4 closed-form specialization table ($m=1,2,4$) and multidimensional roots-of-unity filter reductions (`ABC 240 G`). | Detailed diagnosis of why Chirp-Z must use $\binom{k}{2} = \frac{k(k-1)}{2}$ rather than $\frac{k^2}{2}$ (to avoid nonexistent $\sqrt{\omega_m} \bmod p$ when $m$ is even) and the negative-index shift $M = m-1$ for $i-j < 0$. | Unified in **Section 7**, combining Chirp-Z $\binom{k}{2}$, the Floor-Sum Trick, Multidimensional EGF Cyclic Filters, Quotient Ring $K[x]/(x^m-1)$, and Cyclotomic Extension $\mathbb{F}_p[\omega]/(\Phi_m(\omega))$. |

---

## 2. Algebraic Preliminaries & Master Architecture

Every technique in Wave 2A is an instance of **Formal Composition & Change of Basis**: replacing the indeterminate $x$ in a generating function $F(x) = \sum_{n \ge 0} f_n x^n \in R[[x]]$ with a formal series $G(x)$ or rational expression $G(x) = \frac{P(x)}{Q(x)}$, or applying a differential-logarithmic operator $\frac{d}{dx}\ln F(x)$ to linearize multiplicative structure.

### 2.1 The Three Algebraic Validity Regimes for Composition $F(G(x))$

Before manipulating a substitution, we must verify which algebraic ring makes the infinite sum $\sum_{n \ge 0} f_n G(x)^n$ well-defined:

1. **Regime I: Formal Power Series Ring $R[[x]]$ ($[x^0]G(x) = 0$)**  
   If $G(x) \in xR[[x]]$ has zero constant term ($\operatorname{val}_x(G) \ge 1$), then $\operatorname{val}_x(G(x)^n) \ge n$. For every target degree $k \ge 0$, only finitely many terms $0 \le n \le k$ contribute to $[x^k]F(G(x))$. Examples: $G(x) = \frac{x}{1-cx}$, $G(x) = \frac{x}{1+ax+cx^2}$, $G(x) = e^x - 1$, $G(x) = \ln(1+x)$.
2. **Regime II: Finite-Degree Polynomial Ring $R[x]$ ($\deg F \le n$, $[x^0]G(x) \ne 0$)**  
   If $G(0) \ne 0$ (such as the Taylor shift $G(x) = x + c$ with $c \ne 0$), then $F(G(x))$ does **not** converge in the $(x)$-adic topology of $R[[x]]$ for an infinite series $F$, because $[x^0]F(x+c) = \sum_{n=0}^\infty f_n c^n$ is an infinite sum in $R$. However, if $F(x) \in R[x]$ is a polynomial of degree $\le n$, the sum is finite and exact in $R[x]$.
3. **Regime III: Projective / Möbius Clearing of Denominators ($\mathrm{GL}_2(K)$ Action on $K[x]_{\le n}$)**  
   If $G(x) = \frac{ax+b}{cx+d}$ is a rational function with $b \ne 0$ and $d \ne 0$, we clear denominators on the finite-degree space $K[x]_{\le n}$ via the homogenized operator
   $$(\mathcal{M}_g F)(x) := (cx+d)^n F\!\left(\frac{ax+b}{cx+d}\right) = \sum_{k=0}^n f_k (ax+b)^k (cx+d)^{n-k} \in K[x]_{\le n}$$
   Note that if $b = 0$ and $d \ne 0$, then $G(x) = \frac{ax}{cx+d}$ satisfies $G(0) = 0$, so Regime I applies! Even for an infinite series $F(x) \in K[[x]]$, the generalized Euler transform $E(x) = (1-cx)^{-\alpha} F\!\left(\frac{ax}{1-cx}\right) \bmod x^N$ is well-defined because terms of degree $\ge N$ in $F$ have valuation $\ge N$ after substituting $\frac{ax}{1-cx}$.

### 2.2 The Formal Residue Change-of-Variables Engine

Whenever a nonlinear equation defines $x = \phi(u)$ with $\phi(0) = 0$ and $\phi'(0) \ne 0$ (so $x$ and $u$ are mutually inverse formal parameters of valuation $1$), how do we extract $[x^n]F(x)$ after rewriting $F(x)$ cleanly in terms of $u$?

Rather than memorizing disparate forms of Lagrange Inversion, use the **Formal Residue Change-of-Variables Theorem**: for any formal Laurent series $H(x) \in K((x))$, the formal residue $\operatorname{Res}_x H(x) dx := [x^{-1}]H(x)$ is invariant under any formal change of parameter $x = \phi(u)$ ($\phi(0)=0, \phi'(0)\ne 0$):
$$[x^{-1}]H(x) = [u^{-1}] H(\phi(u))\, \phi'(u)$$

> **Proof in 3 Lines**: By linearity and $(x)$-adic continuity, it suffices to check $H(x) = x^k$ for $k \in \mathbb{Z}$.
> - If $k \ne -1$, then $\phi(u)^k \phi'(u) = \frac{1}{k+1} \frac{d}{du}\!\left(\phi(u)^{k+1}\right)$, and the formal derivative of any Laurent series has zero $[u^{-1}]$ coefficient.
> - If $k = -1$, writing $\phi(u) = c_1 u (1 + \tilde{\phi}(u))$ with $c_1 \ne 0$ gives $\frac{\phi'(u)}{\phi(u)} = \frac{1}{u} + \frac{d}{du}\ln(1 + \tilde{\phi}(u))$, whose $[u^{-1}]$ coefficient is $1$. $\blacksquare$

Setting $H(x) = \frac{F(x)}{x^{n+1}}$ and using $[u^{-1}]\frac{A(u)}{u^{n+1}} = [u^n]A(u)$ yields the two master extraction formulas used throughout Wave 2A:

$$\boxed{[x^n] F(x) = [u^{-1}] \frac{F(x(u))}{x(u)^{n+1}} \frac{dx}{du} = [u^n] \left( F(x(u)) \cdot \left(\frac{u}{x(u)}\right)^{n+1} \frac{dx}{du} \right)} \quad \text{(Differential Form)}$$

$$\boxed{[x^n] F(x) = \frac{1}{n} [u^{n-1}] \left( F'(x(u)) \cdot \left(\frac{u}{x(u)}\right)^n \right) \quad (n \ge 1)} \quad \text{(Integration-by-Parts / Lagrange Form)}$$

---

## 3. Iteration 11 / 63: Rational, Linear & Möbius Substitutions

### 3.1 Diagnostic Signals & Reverse-Engineering Scratchpad

| Raw Coefficient Recurrence / Sum | Diagnostic Features | Target FPS Substitution |
| :--- | :--- | :--- |
| $b_n = \sum_{k=0}^n \binom{n}{k} c^{n-k} a_k$ | Binomial sum over all subsets; powers $c^{n-k}$ pad unselected elements; index $n$ is in the upper index of $\binom{n}{k}$. | **Euler's Series Transform (OGF)** $B(x) = \frac{1}{1-cx} A\!\left(\frac{x}{1-cx}\right)$ or **EGF Product** $\widehat{B}(z) = e^{cz}\widehat{A}(z)$ |
| $b_k = \sum_{n=k}^N \binom{n}{k} c^{n-k} a_n$ | Index $k$ is in the **lower** index of $\binom{n}{k}$; summation runs upward from $k$ to $N$. | **Polynomial Taylor Shift** $B(x) = A(x+c)$ |
| $e_n = \sum_{k=0}^n \binom{n+\alpha-1}{n-k} a^k c^{n-k} f_k$ | Generalized upper-negated binomial coefficient $\binom{-k-\alpha}{n-k}(-1)^{n-k} = \binom{n+\alpha-1}{n-k}$. | **Generalized $\alpha$-Euler Transform** $E(x) = (1-cx)^{-\alpha} F\!\left(\frac{ax}{1-cx}\right)$ |
| $g_j = [x^j] \sum_{k=0}^n f_k (ax+b)^k (cx+d)^{n-k}$ | Homogeneous polynomial weight of total degree $n$ mixing $(ax+b)$ and $(cx+d)$. | **Projective Möbius Action** $(\mathcal{M}_g F)(x) = (cx+d)^n F\!\left(\frac{ax+b}{cx+d}\right)$ |
| $b_m = \sum_{k=0}^n f_k \sum_{j} (-1)^j \binom{k}{j}\binom{n-k}{m-j}$ | Alternating Krawtchouk / Hamming distance sum or $\pm 1$ spin-flip Markov chain. | **Krawtchouk Transform** $K_F(x) = (1+x)^n F\!\left(\frac{1-x}{1+x}\right)$ |

#### Reverse-Engineering Scratchpad (Deriving Euler's Transform from the Sum)
Suppose a problem asks for $b_n = \sum_{k=0}^n \binom{n}{k} c^{n-k} a_k$ for all $0 \le n \le N$, where $a_k$ is defined by an OGF $A(x)$ (or we want to transform the OGF $B(x) = \sum_{n \ge 0} b_n x^n$ directly):
1. **Route 1 (Direct OGF Swap of Summation)**: Multiply by $x^n$, sum over $n \ge 0$, and swap the sums over $n$ and $k$:
   $$B(x) = \sum_{n=0}^\infty x^n \sum_{k=0}^n \binom{n}{k} c^{n-k} a_k = \sum_{k=0}^\infty a_k x^k \sum_{m=0}^\infty \binom{k+m}{k} (cx)^m$$
   Since $\sum_{m=0}^\infty \binom{k+m}{k} (cx)^m = \frac{1}{(1-cx)^{k+1}}$, this collapses immediately to
   $$\boxed{B(x) = \frac{1}{1-cx} \sum_{k=0}^\infty a_k \left(\frac{x}{1-cx}\right)^k = \frac{1}{1-cx} A\!\left(\frac{x}{1-cx}\right)}$$
2. **Route 2 (Formal Borel / Laplace Integral Bridge)**: Dividing $b_n$ by $n!$ gives $\frac{b_n}{n!} = \sum_{k=0}^n \frac{c^{n-k}}{(n-k)!} \frac{a_k}{k!}$, so in the EGF world $\widehat{B}(z) = e^{cz}\widehat{A}(z)$. Applying the **Formal Laplace Transform** $\mathcal{L}(\widehat{F})(x) := \int_0^\infty e^{-t} \widehat{F}(xt)\, dt$ (which maps $\frac{z^n}{n!} \mapsto x^n$ because $\int_0^\infty e^{-t} t^n dt = n!$) gives:
   $$B(x) = \int_0^\infty e^{-t} e^{cxt} \widehat{A}(xt)\, dt = \int_0^\infty e^{-t(1-cx)} \widehat{A}(xt)\, dt \xrightarrow{u = t(1-cx)} \frac{1}{1-cx} \int_0^\infty e^{-u} \widehat{A}\!\left(\frac{xu}{1-cx}\right) du = \frac{1}{1-cx} A\!\left(\frac{x}{1-cx}\right)$$
   This explains *why* the prefactor $\frac{1}{1-cx}$ is mandatory: it is the Jacobian $\frac{dt}{du} = \frac{1}{1-cx}$ of the Laplace scaling!

### 3.2 Generalized Infinite-Series $\alpha$-Euler Transform in 1 NTT Convolution

What if we need the first $N$ coefficients of
$$E(x) = (1-cx)^{-\alpha} F\!\left(\frac{ax}{1-cx}\right) \bmod x^N$$
for an arbitrary parameter $\alpha \in K$ and an infinite series $F(x) = \sum_{k=0}^\infty f_k x^k$?
Expanding $(1-cx)^{-(k+\alpha)} = \sum_{m=0}^\infty \binom{k+\alpha+m-1}{m} c^m x^m$ and setting $n = k + m$ yields:
$$[x^n] E(x) = \sum_{k=0}^n f_k a^k c^{n-k} \binom{n+\alpha-1}{n-k} = \frac{c^n \alpha^{\overline{n}}}{n!} \sum_{k=0}^n \left(\frac{f_k (a/c)^k k!}{\alpha^{\overline{k}}}\right) \frac{n!}{k!(n-k)!}$$
Here, in the last step we factored the rising factorial $\alpha^{\overline{n}} = \alpha(\alpha+1)\cdots(\alpha+n-1)$ using $\binom{n+\alpha-1}{n-k} = \frac{\alpha^{\overline{n}}}{\alpha^{\overline{k}} (n-k)!}$!
- **Case 1 ($\alpha \notin \{0, -1, -2, \dots, -(N-1)\}$)**: Every $\alpha^{\overline{k}}$ is invertible for $0 \le k < N$, so $[x^n]E(x) = c^n \alpha^{\overline{n}} \sum_{k=0}^n \left(\frac{f_k (a/c)^k}{\alpha^{\overline{k}}}\right) \frac{1}{(n-k)!}$, which is **1 single NTT convolution** of length $N$!
- **Case 2 ($\alpha = -d$ is a non-positive integer with $0 \le d < N$)**: Then $\alpha^{\overline{k}}$ hits zero at $k = d+1$. We simply split $F(x) = F_{\le d}(x) + x^{d+1} F_{>d}(x)$:
  1. The finite polynomial piece $(1-cx)^d F_{\le d}\!\left(\frac{ax}{1-cx}\right) = \sum_{k=0}^d f_k (ax)^k (1-cx)^{d-k}$ is computed by the standard homogenized Möbius transform (Section 3.4).
  2. The tail piece is $(1-cx)^d \left(\frac{ax}{1-cx}\right)^{d+1} F_{>d}\!\left(\frac{ax}{1-cx}\right) = (ax)^{d+1} (1-cx)^{-1} F_{>d}\!\left(\frac{ax}{1-cx}\right)$, which has $\tilde{\alpha} = 1 \notin \mathbb{Z}_{\le 0}$ and reduces to Case 1!

### 3.3 Polynomial Taylor Shift $B(x) = A(x+c)$ in $O(n \log n)$

Given $A(x) = \sum_{n=0}^N a_n x^n$, expand $(x+c)^n = \sum_{k=0}^n \binom{n}{k} c^{n-k} x^k$:
$$b_k = [x^k] A(x+c) = \sum_{n=k}^N \binom{n}{k} c^{n-k} a_n = \frac{1}{k!} \sum_{n=k}^N (n!\, a_n) \cdot \frac{c^{n-k}}{(n-k)!}$$
This is a **cross-correlation (difference-index convolution)**. Reversing $u_n = n!\, a_n$ via $\tilde{U}(x) = \sum_{i=0}^N u_{N-i} x^i$ and multiplying by $V(x) = \sum_{j=0}^N \frac{c^j}{j!} x^j$ gives $b_k = \frac{1}{k!} [x^{N-k}](\tilde{U}(x)V(x))$ in **1 NTT multiplication** of size $2N$.

> [!WARNING]
> **Failure Mode: Small Prime Characteristic $p \le N$**  
> If the modulus $p \le N$, then $k!$ is not invertible for $k \ge p$, so the factorial-scaling NTT fails. Instead, use **Lucas's Theorem** $\binom{n}{k} \equiv \prod_i \binom{n_i}{k_i} \pmod p$ in base $p$: view each index $n \in [0, p^L)$ as an $L$-digit base-$p$ vector and apply an $L$-dimensional digit-by-digit transition (generalized SOS DP) in $O(p N \log_p N)$ time (or $O(N \log_2 N)$ when $p = 2$).

### 3.4 General Projective $\mathrm{GL}_2(K)$ Action via Bruhat Decomposition & Krawtchouk Transform

For $g = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathrm{GL}_2(K)$ with $\det(g) = ad - bc \ne 0$, the homogenized operator $(\mathcal{M}_g F)(x) := (cx+d)^n F\!\left(\frac{ax+b}{cx+d}\right)$ defines a right group action $\mathcal{M}_{g_1 g_2} = \mathcal{M}_{g_2} \circ \mathcal{M}_{g_1}$ generated by three elementary $O(n)$ or $O(n \log n)$ primitives:
1. **Reversal** $J = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$: $(\mathcal{M}_J F)(x) = x^n F(1/x) = \sum_{k=0}^n f_{n-k} x^k$ ($O(n)$ array reversal).
2. **Diagonal Scaling** $D(\lambda, \mu) = \begin{pmatrix} \lambda & 0 \\ 0 & \mu \end{pmatrix}$: $(\mathcal{M}_D F)(x) = \sum_{k=0}^n f_k \lambda^k \mu^{n-k} x^k$ ($O(n)$ point-wise scaling).
3. **Unipotent Translation** $T(t) = \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}$: $(\mathcal{M}_{T(t)} F)(x) = F(x+t)$ ($O(n \log n)$ Taylor shift, 1 NTT).

- **Case 1 ($c = 0$)**: Here $(\mathcal{M}_g F)(x) = \sum_{k=0}^n f_k d^{n-k} (ax+b)^k$. To avoid dividing by $d$ (which would fail if $d = 0$ in a degenerate call), pre-scale $F_1(y) = \sum_{k=0}^n (f_k d^{n-k}) y^k$ in $O(n)$ time using a downward prefix product of powers of $d$, then compute $F_2(y) = F_1(y + b)$ via **at most 1 Taylor shift** ($O(n \log n)$), and finally scale $[x^k](\mathcal{M}_g F)(x) = [y^k]F_2(y) \cdot a^k$ in $O(n)$ time.
- **Case 2 ($c \ne 0$, 4-Step Bruhat Decomposition — Safe Even When $d = 0$)**: Using the algebraic identity
  $$\frac{ax+b}{cx+d} = \frac{a}{c} + \frac{bc - ad}{c(cx+d)}$$
  we factor $\mathcal{M}_g$ into **at most 2 Taylor shifts**, 1 reversal, and 2 linear scalings without ever dividing by $d$:
  1. **First Taylor Shift** ($\alpha = a/c$): $F_1(y) = F(y + \alpha)$ ($O(n \log n)$).
  2. **Scale by $\beta = \frac{bc-ad}{c}$ and Reverse**: $F_2(y) = y^n F_1(\beta / y) = \sum_{k=0}^n [y^k]F_1 \cdot \beta^k y^{n-k}$ ($O(n)$).
  3. **Second Taylor Shift by $d$**: $F_3(y) = F_2(y + d)$ ($O(n \log n)$, completely safe when $d = 0$).
  4. **Final Monomial Scaling by $c$**: $(\mathcal{M}_g F)(x) = F_3(cx) = \sum_{j=0}^n [y^j]F_3 \cdot c^j x^j$ ($O(n)$).

#### Specialization: The Krawtchouk Transform (1-Shift vs. 2-Shift Shortcuts)
In spin-flip Markov chains (`ARC136 F`, `KUPC 2019 K`) and coding theory, the **Krawtchouk Transform** is
$$K_F(x) = \sum_{k=0}^n f_k (1-x)^k (1+x)^{n-k} = (1+x)^n F\!\left(\frac{1-x}{1+x}\right)$$
Since $\frac{1-x}{1+x} = -1 + \frac{2}{1+x}$, the Bruhat chain computes $K_F(x)$ in **2 Taylor shifts**:
$$F(y) \xrightarrow{\text{Shift }-1} F_1(y) = F(y-1) \xrightarrow{\text{Scale }2\text{ \& Reverse}} F_2(y) = y^n F_1(2/y) \xrightarrow{\text{Shift }+1} K_F(x) = F_2(x+1)$$
**1-Shift Shortcut when $F_1(y) = F(y-1)$ is Already Known**: Often in contest problems we build $F(y) = \prod (1 \pm y)^{c_i}$ directly in the shifted basis $u = \frac{1-x}{1+x} + 1 = \frac{2}{1+x}$, where $1+x = \frac{2}{u}$ and $1-x = \frac{2(u-1)}{u}$. Then $\prod (1-x)^k (1+x)^{n-k} = 2^n u^{-n} (u-1)^k$, so recovering the $x$-coefficients requires **only 1 Taylor shift** ($u \mapsto x+1$ after reversing)!

#### Small-$n$ Handwritten Trace ($n = 2$, $F(x) = 1 + 2x + 3x^2$, $K_F(x) = (1+x)^2 F(\frac{1-x}{1+x})$)
1. **Direct Expansion**: $K_F(x) = 1(1+x)^2 + 2(1-x)(1+x) + 3(1-x)^2 = (1+2x+x^2) + (2-2x^2) + (3-6x+3x^2) = 6 - 4x + 2x^2$.
2. **Bruhat 2-Shift Trace**:
   - Step 1: $F_1(x) = F(x-1) = 1 + 2(x-1) + 3(x-1)^2 = 2 - 4x + 3x^2$.
   - Step 2: $F_2(x) = x^2 F_1(2/x) = 2x^2 - 4(2)x + 3(4) = 12 - 8x + 2x^2$.
   - Step 3: $K_F(x) = F_2(x+1) = 12 - 8(x+1) + 2(x+1)^2 = 6 - 4x + 2x^2$. Matches!

---

## 4. Iteration 12 / 64: Quadratic Radicals, Catalan, Motzkin, Delannoy, Schröder, Narayana & Chebyshev Substitutions

### 4.1 Diagnostic Signals & Reverse-Engineering Scratchpad

| Combinatorial / Algebraic Signal | Underlying Quadratic Equation | Rational Uniformizing Substitution $x = \phi(u)$ |
| :--- | :--- | :--- |
| $\sqrt{1-4x}$, Catalan $C(x) = \frac{1-\sqrt{1-4x}}{2x}$, or $\binom{2n+k}{n}$ | $U = 1 + xU^2$ or $u = x(1+u)^2$ | **Catalan Type I**: $x = u(1-u)$ ($\sqrt{1-4x} = 1-2u$)<br>**Catalan Type II**: $x = \frac{u}{(1+u)^2}$ ($\sqrt{1-4x} = \frac{1-u}{1+u}$) |
| $\sqrt{1-2x-3x^2}$, Motzkin paths $(+1, 0, -1)$ | $M(x) = 1 + xM(x) + x^2 M(x)^2$ | **Motzkin Substitution**: $x = \frac{u}{1+u+u^2}$ ($\sqrt{1-2x-3x^2} = \frac{1-u^2}{1+u+u^2}$) |
| $\sqrt{1-6x+x^2}$, Central Delannoy $D(x) = \frac{1}{\sqrt{1-6x+x^2}}$ or Large Schröder $S(x) = \frac{1-x-\sqrt{1-6x+x^2}}{2x}$ | $u = x(1+3u+2u^2) = x(1+u)(1+2u)$ | **Delannoy / Schröder Substitution**: $x = \frac{u}{(1+u)(1+2u)}$ ($\sqrt{1-6x+x^2} = \frac{1-2u^2}{1+3u+2u^2}$, $S(x) = 1+2u$) |
| $\sqrt{(1-(1+t)x)^2 - 4tx^2}$, Dyck paths by peaks (**Narayana numbers** $N(n,k)$) | $F(x,t) = 1 + x F(x,t) (t + F(x,t) - 1)$ | **Narayana Substitution**: $x = \frac{u}{(1+u)(1+tu)}$ |
| General radical $\sqrt{1 - 2ax + bx^2}$ | $u = x(1 + au + cu^2)$ with $c = \frac{a^2-b}{4}$ | **Universal Quadratic Substitution**: $x = \frac{u}{1+au+cu^2}$ ($\sqrt{1-2ax+bx^2} = \frac{1-cu^2}{1+au+cu^2}$) |
| Bounded-height Dyck/lattice walks on $[0, H]$, continued fractions $\frac{1}{1-\frac{x^2}{1-\dots}}$, Chebyshev $U_H$ | Transfer matrix $T_H$ with eigenvalues $2\cos\theta$ | **Chebyshev Substitution**: $x = \frac{u}{1+u^2}$ ($\sqrt{1-4x^2} = \frac{1-u^2}{1+u^2}$, killing $\sqrt{\cdot}$ so $U_k(\frac{1}{2x}) = x^{-k}\frac{u^k(1-u^{2k+2})}{(1+u^2)^k(1-u^2)}$) |

#### Reverse-Engineering Scratchpad: How to Rationalize Any $\sqrt{1 - 2ax + bx^2}$ (Euler's Method)
Suppose a problem yields an OGF containing $R(x) = \sqrt{1 - 2ax + bx^2}$ with $a^2 \ne b$:
1. **Force a Rational Square**: Set $1 - 2ax + bx^2 = (1 - ux)^2 = 1 - 2ux + u^2 x^2$? No, that gives $x = \frac{2(u-a)}{u^2-b}$, which has $x(0) \ne 0$. To preserve $x(0) = 0$ and $x'(0) = 1$ (so $x$ and $u$ have the same formal valuation $1$), set:
   $$x = \frac{u}{1 + au + cu^2}$$
2. **Complete the Square in the Numerator**: Substitute $x$ into $1 - 2ax + bx^2$:
   $$1 - 2ax + bx^2 = \frac{(1 + au + cu^2)^2 - 2au(1 + au + cu^2) + bu^2}{(1 + au + cu^2)^2} = \frac{1 + (2c - a^2 + b)u^2 + c^2 u^4}{(1 + au + cu^2)^2}$$
3. **Choose $c$ to Make the Numerator $(1 - cu^2)^2$**: We need $2c - a^2 + b = -2c \iff \boxed{c = \frac{a^2 - b}{4}}$. With this choice of $c$, the radical collapses into a purely rational function of $u$:
   $$\boxed{\sqrt{1 - 2ax + bx^2} = \frac{1 - cu^2}{1 + au + cu^2}, \qquad \frac{dx}{du} = \frac{1 - cu^2}{(1 + au + cu^2)^2}}$$
   Notice the miracle: **the numerator $1 - cu^2$ of $\sqrt{1 - 2ax + bx^2}$ is identical to the numerator of the Jacobian $\frac{dx}{du}$!** In fact, dividing the two immediately proves the **Differential Logarithmic Identity**:
   $$\boxed{\frac{1}{\sqrt{1 - 2ax + bx^2}} = \frac{u'(x) x}{u(x)} = x \frac{d}{dx} \ln u(x)}$$

### 4.2 Side-by-Side Comparison of the Two Catalan Substitutions ($x = u(1-u)$ vs. $x = \frac{u}{(1+u)^2}$)

Why do some references substitute $x = u(1-u)$ while others substitute $x = \frac{u}{(1+u)^2}$ for $\sqrt{1-4x}$? Both correspond to $a = 2, b = 0$, but they parameterize different shifts of $C(x) = \frac{1-\sqrt{1-4x}}{2x}$:

| Feature | **Catalan Substitution I**: $x = u(1-u)$ | **Catalan Substitution II**: $x = \frac{u}{(1+u)^2}$ |
| :--- | :--- | :--- |
| **Relation to $C(x)$** | $u = xC(x) = \frac{1-\sqrt{1-4x}}{2}$, $C(x) = \frac{1}{1-u}$ | $u = C(x) - 1 = \frac{1-2x-\sqrt{1-4x}}{2x}$, $C(x) = 1+u$ |
| **Radical $\sqrt{1-4x}$** | $1 - 2u$ | $\frac{1-u}{1+u}$ |
| **Jacobian $\frac{dx}{du}$ & $\frac{u}{x(u)}$** | $\frac{dx}{du} = 1 - 2u$, $\frac{u}{x(u)} = \frac{1}{1-u}$ | $\frac{dx}{du} = \frac{1-u}{(1+u)^3}$, $\frac{u}{x(u)} = (1+u)^2$ |
| **Residue Extraction of $[x^n]F(x)$** | $[u^n] F(u(1-u)) (1-2u) (1-u)^{-(n+1)}$ (**negative** binomial power) | $[u^n] F\!\left(\frac{u}{(1+u)^2}\right) (1-u) (1+u)^{2n-1}$ (**positive** polynomial power!) |
| **Best Use Case** | Extracting $[x^n] C(x)^k = [x^n] (1-u)^{-k}$, since $(1-u)^{-k}$ merges cleanly with $(1-u)^{-(n+1)}$ into $(1-u)^{-(n+k+1)}$. | Extracting $[x^n] P(C(x))$ for a polynomial $P$, or Chebyshev / ballot reflections where $\frac{u}{(1+u)^2}$ is symmetric under $u \leftrightarrow u^{-1}$. |

#### Classic Raney / Ballot Identity via Catalan Substitution II
Using $C(x) = 1+u$ under $x = \frac{u}{(1+u)^2}$:
$$[x^n] C(x)^k = [u^n] (1+u)^k (1-u) (1+u)^{2n-1} = [u^n](1-u)(1+u)^{2n+k-1} = \binom{2n+k-1}{n} - \binom{2n+k-1}{n-1} = \frac{k}{2n+k}\binom{2n+k}{n}$$
And with the radical in the denominator, $\frac{C(x)^k}{\sqrt{1-4x}} = \frac{(1+u)^{k+1}}{1-u}$ cancels the $(1-u)$ factor from the Jacobian:
$$[x^n] \frac{C(x)^k}{\sqrt{1-4x}} = [u^n] \frac{(1+u)^{k+1}}{1-u} (1-u)(1+u)^{2n-1} = [u^n] (1+u)^{2n+k} = \binom{2n+k}{n}$$

> [!NOTE]
> **Characteristic $p = 2$ Artin–Schreier Behavior of Catalan Numbers**  
> If a problem asks for Catalan or quadratic-radical coefficients modulo $2$ (where $2^{-1}$ does not exist so $\frac{1-\sqrt{1-4x}}{2x}$ is undefined), go back to the ring equation $C(x) = 1 + x C(x)^2 \in \mathbb{F}_2[[x]]$. Since squaring is a Frobenius homomorphism $(A+B)^2 = A^2 + B^2$ in $\mathbb{F}_2[[x]]$, iterating $C(x) = 1 + x(1 + x^2 C(x)^4) = \dots$ immediately gives:
> $$C(x) \equiv \sum_{k=0}^\infty x^{2^k - 1} \pmod 2 \implies C_n \equiv 1 \pmod 2 \iff n = 2^k - 1$$

### 4.3 Two Master Coefficient Extraction Formulas for General $\sqrt{1-2ax+bx^2}$

Applying the Formal Residue Engine (Section 2.2) to $x = \frac{u}{1+au+cu^2}$ ($c = \frac{a^2-b}{4}$, $\Delta = 1 - 2ax + bx^2$) yields two complementary extraction formulas:

- **Master Formula A (With $\frac{1}{\sqrt{\Delta}}$ — Cleanest when $\frac{1}{\sqrt{\Delta}}$ is Present)**:  
  Since $\frac{1}{\sqrt{\Delta}} \frac{dx}{du} = \frac{1}{1+au+cu^2}$, the $(1-cu^2)$ factors cancel completely! For any series $G(x) = H(u(x))$:
  $$\boxed{[x^n] \frac{G(x)}{\sqrt{1-2ax+bx^2}} = [u^n] \Big( H(u) \cdot (1 + au + cu^2)^n \Big)}$$
- **Master Formula B (Without $\frac{1}{\sqrt{\Delta}}$)**:
  $$\boxed{[x^n] G(x) = [u^n] \Big( H(u) \cdot (1 - cu^2) (1 + au + cu^2)^{n-1} \Big)}$$

#### Important Specializations of Master Formulas A & B
1. **Motzkin Numbers $M_n$ ($a = 1, b = -3 \implies c = \frac{1-(-3)}{4} = 1$)**:  
   Here $x = \frac{u}{1+u+u^2}$ and $M(x) = \frac{1-x-\sqrt{1-2x-3x^2}}{2x^2} = 1 + u + u^2 = \frac{u}{x}$. By Formula B (or Lagrange form):
   $$M_n = [x^n] M(x) = \frac{1}{n+1} [u^n] (1 + u + u^2)^{n+1} = \sum_{k=0}^{\lfloor n/2 \rfloor} \frac{1}{n+1} \binom{n+1}{n-2k, k, k+1} = \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} C_k$$
2. **Central Delannoy $D_n$ & Large Schröder $S_n$ ($a = 3, b = 1 \implies c = \frac{9-1}{4} = 2$)**:  
   Here $x = \frac{u}{1+3u+2u^2} = \frac{u}{(1+u)(1+2u)}$—the quadratic trinomial **splits into two linear factors**!
   - By Formula A with $H(u) = 1$, Central Delannoy numbers satisfy:
     $$D_n = [x^n] \frac{1}{\sqrt{1-6x+x^2}} = [u^n] (1+u)^n (1+2u)^n = \sum_{j=0}^n \binom{n}{j}\binom{n}{n-j} 2^j = \sum_{j=0}^n \binom{n}{j}^2 2^j$$
   - For Large Schröder numbers $S(x) = \frac{1-x-\sqrt{1-6x+x^2}}{2x}$, substituting $x = \frac{u}{(1+u)(1+2u)}$ simplifies $S(x(u)) = 1 + 2u$. By Formula B:
     $$S_n = [u^n] (1+2u)(1-2u^2)(1+u)^{n-1}(1+2u)^{n-1} = [u^n] (1-2u^2)(1+u)^{n-1}(1+2u)^n$$
3. **Narayana Numbers $N(n, k)$ (Dyck Paths of Semilength $n$ with $k$ Peaks)**:  
   Counting non-empty Dyck paths by semilength $x$ and peaks $t$ yields $F(x,t) = x t + x F(x,t) + x F(x,t) \frac{F(x,t)}{1 - \dots} \iff u(x,t) = x(1+u)(1+tu)$ where $u = \frac{F(x,t)}{t}$ (or directly setting $x = \frac{u}{(1+u)(1+tu)}$). By the Lagrange form of our Residue Engine:
   $$[x^n] u(x,t) = \frac{1}{n} [u^{n-1}] (1+u)^n (1+tu)^n = \sum_{k=1}^n \frac{1}{n}\binom{n}{k}\binom{n}{k-1} t^k \implies \boxed{N(n,k) = \frac{1}{n}\binom{n}{k}\binom{n}{k-1}}$$

### 4.4 Chebyshev Rational Substitutions ($x = \frac{u}{1+u^2}$) for Bounded-Height Walks

When lattice paths are restricted to a finite strip $0 \le y \le H$, step-by-step DP takes $O(n H)$ time, and transfer-matrix exponentiation takes $O(H^3 \log n)$. Instead, write the generating function as a rational quotient of Chebyshev polynomials via Cramer's rule on the tridiagonal transfer matrix, and apply the rationalizing substitution that diagonalizes the recurrence into powers of $u$!

There are **two distinct contest models** that must never be conflated:

| Model | Combinatorial Walk Type | Substitution $x = \phi(u)$ | Start $(0,0) \to$ End $(N,0)$ OGF in $u$ | Extreme Excursions $(0,0) \to (N,H)$ OGF in $u$ | Sieve / Extraction Method |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Model I (Catalan / Semi-Length Weight)** | Dyck paths of length $2N$ ($N$ up-steps) in $0 \le y \le H$, or Cartesian trees of left-depth $\le H$ (`UOJ #424`). | $x = \frac{u}{(1+u)^2}$ | $[u^N] (1-u) (1+u)^{2N} \frac{1 - u^{H+1}}{1 - u^{H+2}}$ | $[u^N] (1-u) (1+u)^{2N} \frac{u^H (1-u)}{1 - u^{H+2}}$ (**Note**: first-power $u^{H+2}$ in denominator!) | Expand $\frac{1}{1-u^{H+2}} = \sum_{j \ge 0} u^{j(H+2)}$ in $O(N/H)$ terms (harmonic $O(N \log N)$ across all $H$). |
| **Model II (Chebyshev / Step Weight)** | General lattice paths of $N$ steps ($+1$ weight $1$, $0$ weight $a$, $-1$ weight $c$) in $0 \le y \le H$. | $x = \frac{u}{1 + au + cu^2}$ | $[u^N] (1 - cu^2)(1 + au + cu^2)^N \frac{1 - (cu^2)^{H+1}}{1 - (cu^2)^{H+2}}$ | $[u^N] (1 - cu^2)(1 + au + cu^2)^N \frac{u^H (1 - cu^2)}{1 - (cu^2)^{H+2}}$ (**Note**: even-power $(cu^2)^{H+2}$!) | Expand $\frac{1}{1 - (cu^2)^{H+2}} = \sum_{j \ge 0} c^{j(H+2)} u^{2j(H+2)}$ against $(1+au+cu^2)^N$. |

#### Derivation of the Chebyshev Collapse (Model II with $a=0, c=1 \implies x = \frac{u}{1+u^2}$)
The Chebyshev polynomial of the second kind satisfies $U_k(\cos\theta) = \frac{\sin((k+1)\theta)}{\sin\theta}$ and $U_k(z) = 2z U_{k-1}(z) - U_{k-2}(z)$. Setting $2\cos\theta = \frac{1}{x}$ via $e^{i\theta} = u^{-1}$ gives $x = \frac{1}{u + u^{-1}} = \frac{u}{1+u^2}$, so:
$$U_k\!\left(\frac{1}{2x}\right) = \frac{u^{-(k+1)} - u^{k+1}}{u^{-1} - u} = \frac{1 - u^{2k+2}}{u^k (1 - u^2)}$$
In the strip $0 \le y \le H$, the OGF of walks from $y=0$ to $y=0$ is $F_H(x) = \frac{U_H(1/(2x))}{x\, U_{H+1}(1/(2x))} = (1+u^2) \frac{1 - u^{2H+2}}{1 - u^{2H+4}}$. Applying Master Formula B ($a=0, c=1 \implies \frac{dx}{du} = \frac{1-u^2}{(1+u^2)^2}$, $\frac{u}{x} = 1+u^2$) gives:
$$[x^N] F_H(x) = [u^N] (1-u^2)(1+u^2)^N \frac{1 - u^{2H+2}}{1 - u^{2H+4}} = \sum_{j \in \mathbb{Z}} \left( \binom{N}{\frac{N - 2j(H+2)}{2}} - \binom{N}{\frac{N - 2 - 2j(H+2)}{2}} \right)$$
recovering the **André Reflection Principle** purely algebraically!

#### Multi-Dimensional Walk Decoupling (`FPS-24 H Jump`, `FPS-24 V 12 Directions`, `ABC 240 G`)
Whenever a 2D/3D walk has entangled steps $S(x,y)$:
1. **45° Rotation ($u = xy, v = x/y$)**: Converts $( \pm 1, 0 ), ( 0, \pm 1 )$ steps $(x + x^{-1} + y + y^{-1}) = (u^{1/2} + u^{-1/2})(v^{1/2} + v^{-1/2})$ into two **independent** 1D walks!
2. **Idle-Step Shifting ($G = c + S(x,y)$)**: In `FPS-24 V (12 Directions)`, adding a constant $2$ to the 12-direction step polynomial $S(x,y)$ factors it into three decoupled 1D steps:
   $$2 + S(x,y) = (x^{1/2} + x^{-1/2})(y^{1/2} + y^{-1/2})((xy)^{1/2} + (xy)^{-1/2})$$
   We compute $g_k = [x^0 y^0](2 + S(x,y))^k$ in $O(k)$ per $k$, then invert the binomial shift $g_k = \sum_{j=0}^k \binom{k}{j} 2^{k-j} f_j \iff f_n = \sum_{k=0}^n \binom{n}{k} (-2)^{n-k} g_k$ via **Euler's Series Transform** (Iteration 11)!

---

## 5. Iteration 13 / 65: Transcendental Substitutions ($e^x-1, \ln(1+x)$), Stirling, Lah & Falling-Factorial Polynomials (`下降幂多项式`)

### 5.1 Diagnostic Signals & Reverse-Engineering Scratchpad

| Combinatorial / Algebraic Signal | Underlying Transcendental Identity | Target FPS / Basis Method |
| :--- | :--- | :--- |
| Surjections $k!\, {n \brace k}$, ordered Bell numbers, or $b_n = \sum_{k=0}^n {n \brace k} a_k$ | $\frac{(e^x-1)^k}{k!} = \sum_{n=k}^\infty {n \brace k} \frac{x^n}{n!}$ | **EGF Substitution** $\widehat{B}(x) = A(e^x-1)$ |
| Signed/unsigned cycle counts ${n \brack k}$, or $b_n = \sum_{k=0}^n (-1)^{n-k} {n \brack k} a_k$ | $\frac{(\ln(1+x))^k}{k!} = \sum_{n=k}^\infty (-1)^{n-k} {n \brack k} \frac{x^n}{n!}$ | **Logarithmic Substitution** $\widehat{B}(x) = A(\ln(1+x))$ |
| Disconnected labeled graphs $\widehat{G}(x)$ vs. connected labeled graphs $\widehat{C}(x)$ | $\widehat{G}(x) = \exp(\widehat{C}(x)) \iff \widehat{C}(x) = \ln \widehat{G}(x)$ | **Exponential Transform ($\exp/\ln$)** in $O(n \log n)$ |
| Ordered partitions into $k$ lists (Lah numbers $L(n,k) = \binom{n-1}{k-1}\frac{n!}{k!}$) | $\frac{1}{k!}\left(\frac{x}{1-x}\right)^k = \sum_{n=k}^\infty L(n,k) \frac{x^n}{n!}$ | **Lah Rational EGF Substitution** $\widehat{B}(x) = \widehat{A}\!\left(\frac{x}{1-x}\right)$ |
| Sum with polynomial index weight $\sum_{i=0}^m \binom{m}{i} p^i q^{m-i} P(i)$ ($m \le 10^{18}, \deg P \le 10^5$) | $\binom{m}{i} i^{\underline{k}} = m^{\underline{k}} \binom{m-k}{i-k}$ | **Falling-Factorial Polynomial (`下降幂多项式`) Binomial Moment Collapse** in $O(\deg P \log(\deg P))$ |

#### Reverse-Engineering Scratchpad (Deriving the Exponential Substitution & Binomial Moment Collapse from Scratch)
1. **Why $\widehat{B}(x) = A(e^x - 1)$ Encodes Stirling Partition Transforms**:  
   Suppose a problem asks for $b_n = \sum_{k=0}^n {n \brace k} a_k$ (or $\sum_{k=0}^n k!\, {n \brace k} \tilde{a}_k$, where $k!\, {n \brace k}$ counts surjections from $n$ labeled elements to $k$ distinguishable non-empty boxes). Since a single non-empty labeled box has EGF $e^x - 1 = \sum_{m=1}^\infty \frac{x^m}{m!}$, a collection of $k$ unordered non-empty boxes has EGF $\frac{(e^x-1)^k}{k!} = \sum_{n=k}^\infty {n \brace k} \frac{x^n}{n!}$. Multiplying by $a_k$ and summing over $k \ge 0$ gives the EGF composition:
   $$\widehat{B}(x) = \sum_{n=0}^\infty b_n \frac{x^n}{n!} = \sum_{k=0}^\infty a_k \frac{(e^x-1)^k}{k!} = \widehat{A}(e^x - 1)$$
2. **Why $i^K$ Inside $\sum_{i=0}^n \binom{n}{i} p^i q^{n-i} i^K$ Demands Falling Factorials**:  
   In $\binom{n}{i} = \frac{n!}{i!(n-i)!}$, the index $i$ sits in the denominator as $i!$. Multiplying by a monomial $i^K$ does not cancel $i!$, leaving $\frac{i^K}{i!}$. However, multiplying by a **falling factorial** $i^{\underline{k}} = \frac{i!}{(i-k)!}$ cancels $i!$ into $(i-k)!$:
   $$\binom{n}{i} i^{\underline{k}} = \frac{n!}{i!(n-i)!} \frac{i!}{(i-k)!} = \frac{n!}{(n-k)!} \frac{(n-k)!}{(i-k)!(n-i)!} = n^{\underline{k}} \binom{n-k}{i-k}$$
   Summing over $i$ immediately collapses $\sum_{i=k}^n \binom{n-k}{i-k} p^i q^{n-i} = p^k (p+q)^{n-k}$ in $O(1)$ per basis term!

### 5.2 Complete $O(n \log n)$ Blueprint for All 4 Stirling Regimes & Both Lah Regimes

Because $(e^x-1) \circ \ln(1+x) = x$, the Stirling numbers of the first and second kinds form mutually inverse triangular basis matrices:
$$x^n = \sum_{k=0}^n {n \brace k} x^{\underline{k}}, \qquad x^{\underline{n}} = \sum_{k=0}^n (-1)^{n-k} {n \brack k} x^k, \qquad x^{\overline{n}} = \sum_{k=0}^n {n \brack k} x^k$$

| Regime | Target Sequence ($0 \le i \le n$) | Generating Function Identity | Optimal $O(n \log n)$ Algorithm |
| :--- | :--- | :--- | :--- |
| **1. Second Kind — Fixed Row $n$** | ${n \brace k}$ for $0 \le k \le n$ | ${n \brace k} = \frac{1}{k!} \sum_{j=0}^k (-1)^{k-j} \binom{k}{j} j^n$ | **1 Single NTT Convolution**: Convolve $A_j = \frac{j^n}{j!}$ with $B_j = \frac{(-1)^j}{j!}$. |
| **2. Second Kind — Fixed Column $k$** | ${i \brace k}$ for $0 \le i \le n$ | $\sum_{i=k}^\infty {i \brace k} \frac{x^i}{i!} = \frac{(e^x-1)^k}{k!}$ (EGF)<br>$\sum_{i=k}^\infty {i \brace k} x^i = \frac{x^k}{(1-x)(1-2x)\cdots(1-kx)}$ (OGF) | **1 FPS $\ln$ + 1 FPS $\exp$**: Shift $G(x) = \frac{e^x-1}{x} = \sum_{j \ge 0} \frac{x^j}{(j+1)!}$ so $G(0)=1$, compute $\exp(k \ln G(x)) \bmod x^{n-k+1}$, multiply by $\frac{x^k}{k!}$. |
| **3. First Kind — Fixed Row $n$** | ${n \brack k}$ for $0 \le k \le n$ | $\sum_{k=0}^n {n \brack k} x^k = x^{\overline{n}} = x(x+1)\cdots(x+n-1)$ | **Doubling via Taylor Shift**: Write $x^{\overline{2m}} = x^{\overline{m}} \cdot (x+m)^{\overline{m}}$. Compute $(x+m)^{\overline{m}}$ from $x^{\overline{m}}$ in 1 Taylor shift ($O(m \log m)$) + 1 multiplication. Total: $T(n) = T(n/2) + O(n \log n) = O(n \log n)$! |
| **4. First Kind — Fixed Column $k$** | ${i \brack k}$ for $0 \le i \le n$ | $\sum_{i=k}^\infty {i \brack k} \frac{x^i}{i!} = \frac{(-\ln(1-x))^k}{k!}$ | **1 FPS $\ln$ + 1 FPS $\exp$**: Set $H(x) = \frac{-\ln(1-x)}{x} = \sum_{j \ge 0} \frac{x^j}{j+1}$ ($H(0)=1$), compute $\exp(k \ln H(x)) \bmod x^{n-k+1}$, multiply by $\frac{x^k}{k!}$. |
| **5. Lah Numbers — Fixed Row $n$** | $L(n, k) = \binom{n-1}{k-1}\frac{n!}{k!}$ for $1 \le k \le n$ | $x^{\overline{n}} = \sum_{k=0}^n L(n,k) x^{\underline{k}}$ | **$O(n)$ Closed Form** directly from factorials! Moreover, converting $A(x) = \sum a_k x^{\overline{k}} \leftrightarrow \sum b_k x^{\underline{k}}$ is **1 single NTT convolution** via Euler's Transform! |
| **6. Lah Numbers — Fixed Column $k$** | $L(i, k)$ for $k \le i \le n$ | $\sum_{i=k}^\infty L(i,k) \frac{x^i}{i!} = \frac{1}{k!}\left(\frac{x}{1-x}\right)^k$ | **$O(n)$ Closed Form** from factorials, or $O(n \log n)$ via Binomial Transform. |

> [!CAUTION]
> **Critical Implementation Trap in Fixed-Column Stirling (`ln` / `exp` Valuation Shift)**  
> Never pass $e^x - 1$ or $-\ln(1-x)$ directly into `poly_pow` or `poly_ln`, because their constant term $[x^0]$ is $0$! Always divide out $x$ first so the series starts with $1 + c_1 x + \dots$, raise to the $k$-th power modulo $x^{n-k+1}$, and shift back by $x^k / k!$.

### 5.3 Falling-Factorial Polynomials (`下降幂多项式` / FFP) & The Point-Value EGF

A polynomial $P(x)$ of degree $\le n$ written in the falling-factorial basis $P(x) = \sum_{k=0}^n c_k x^{\underline{k}}$ has a remarkable property when evaluated on non-negative integers $m \in \mathbb{Z}_{\ge 0}$: since $\frac{m^{\underline{k}}}{k!} = \binom{m}{k}$, we have
$$\frac{P(m)}{m!} = \sum_{k=0}^m \left(c_k\right) \cdot \frac{1}{(m-k)!}$$
In other words, defining the **Coefficient OGF** $C(t) = \sum_{k=0}^n c_k t^k$ and the **Point-Value EGF** $\widehat{P}(t) = \sum_{m=0}^\infty P(m) \frac{t^m}{m!}$, we obtain the **Fundamental Theorem of Falling-Factorial Polynomials**:
$$\boxed{\widehat{P}(t) = C(t)\, e^t \iff C(t) = \widehat{P}(t)\, e^{-t} \bmod t^{n+1}}$$

1. **FFP Basis $\leftrightarrow$ Point Values $P(0), \dots, P(n)$ in $O(n \log n)$ (1 NTT)**:
   - Given $c_0, \dots, c_n$, multiply $C(t)$ by $e^t \bmod t^{n+1}$ and scale by $m!$ to get $P(0), \dots, P(n)$ in **1 NTT**.
   - Given $P(0), \dots, P(n)$, form $\widehat{P}(t) = \sum_{m=0}^n \frac{P(m)}{m!} t^m$ and multiply by $e^{-t} = \sum_{j=0}^n \frac{(-1)^j}{j!} t^j \bmod t^{n+1}$ to recover $c_0, \dots, c_n$ in **1 NTT**!
2. **FFP Multiplication in $O(n \log n)$ (3 NTTs)**:  
   To multiply $A(x) = \sum_{k=0}^n a_k x^{\underline{k}}$ and $B(x) = \sum_{k=0}^m b_k x^{\underline{k}}$ in the falling-factorial basis up to degree $N = n+m$:
   - Convolve $A_{\text{coef}}(t)$ with $e^t \bmod t^{N+1}$ and $B_{\text{coef}}(t)$ with $e^t \bmod t^{N+1}$ to obtain $\frac{A(i)}{i!}$ and $\frac{B(i)}{i!}$ for $0 \le i \le N$.
   - Multiply point-wise: $\frac{(AB)(i)}{i!} = i! \cdot \frac{A(i)}{i!} \cdot \frac{B(i)}{i!}$.
   - Convolve with $e^{-t} \bmod t^{N+1}$ to get the falling-factorial coefficients of $A(x)B(x)$!

#### Complete 5-Row Basis Conversion Complexity Table ($\{x^k\} \leftrightarrow \{x^{\underline{k}}\} \leftrightarrow \{x^{\overline{k}}\}$)

| Conversion Direction | Mathematical Operator | Time Complexity | Algorithmic Mechanism |
| :--- | :--- | :--- | :--- |
| **1. FFP $\{x^{\underline{k}}\} \leftrightarrow$ Point Values $\{P(0),\dots,P(n)\}$** | $\widehat{P}(t) = C(t)e^t \bmod t^{n+1}$ | **$O(n \log n)$** (1 NTT) | Convolve with $e^t$ or $e^{-t}$. |
| **2. Rising $\{x^{\overline{k}}\} \leftrightarrow$ Falling $\{x^{\underline{k}}\}$** | $x^{\overline{k}} = (-1)^k (-x)^{\underline{k}}$ or Lah transform | **$O(n \log n)$** (1 NTT) | Substitute $x \mapsto -x$ on point values, or apply Euler's Transform $B(t) = \frac{1}{1-t} A\!\left(\frac{t}{1-t}\right)$ to the scaled coefficients $\frac{c_k}{k!}$! |
| **3. Monomial $\{x^k\} \to$ Falling $\{x^{\underline{k}}\}$** | $c_k = [t^k] e^{-t} \sum_{m=0}^n \frac{P(m)}{m!} t^m$ or $\mathcal{L}\{P(e^z)\}$ | **$O(n \log^2 n)$** | Multipoint evaluation of $P(x)$ on $0, 1, \dots, n$ + 1 NTT with $e^{-t}$, **or** D&C rational sum $\sum_{j=0}^n \frac{p_j}{1 - jz}$ (`composite-exp`). |
| **4. Falling $\{x^{\underline{k}}\} \to$ Monomial $\{x^k\}$** | $P(x) = \sum_{k=0}^n c_k x^{\underline{k}}$ | **$O(n \log^2 n)$** | D&C tree over $x^{\underline{k}}$ (using $O(m \log m)$ Taylor shift at each node) or Lagrange interpolation from $P(0), \dots, P(n)$. |
| **5. Binomial Moment Collapse $\sum_{i=0}^m \binom{m}{i} p^i q^{m-i} P(i)$** | $\sum_{i=0}^m \binom{m}{i} p^i q^{m-i} i^{\underline{k}} = m^{\underline{k}} p^k (p+q)^{m-k}$ | **$O(d \log d)$** ($d = \deg P$) | Convert $P$ from $\{P(0),\dots,P(d)\}$ to $c_k$ in **1 NTT** ($O(d \log d)$), then evaluate $\sum_{k=0}^d c_k m^{\underline{k}} p^k (p+q)^{m-k}$ in **$O(d)$**! |

#### The Borel–Laplace Rational Sum (`fps/composite-exp.hpp`) for $P(e^{cz})$ and $A(e^z - 1)$
Whenever we are given a polynomial $P(y) = \sum_{k=0}^M p_k y^k$ and need the first $N+1$ EGF coefficients of $\widehat{B}(z) = P(e^{cz}) = \sum_{k=0}^M p_k e^{kcz}$ (or $\widehat{B}(z) = A(e^z - 1)$ after a Taylor shift $P(y) = A(y-1)$), applying the **Formal Laplace Transform** $\mathcal{L}\{e^{kcz}\} = \frac{1}{1 - kcx}$ converts the transcendental EGF directly into a rational OGF sum:
$$\boxed{B(x) = \sum_{n=0}^\infty b_n x^n = \mathcal{L}\{P(e^{cz})\}(x) = \sum_{k=0}^M \frac{p_k}{1 - kcx}}$$
We sum the $M+1$ fractions $\frac{p_k}{1 - kcx}$ into a single rational function $\frac{U(x)}{V(x)}$ via a binary Divide-and-Conquer product tree in $O(M \log^2 M)$ time, followed by a single polynomial inversion $U(x) V(x)^{-1} \bmod x^{N+1}$ in $O(N \log N)$ time!

---

## 6. Iteration 14 / 66: Logarithmic Derivatives ($F'/F$), Euler / Multiset Transform ($\operatorname{MSET}/\operatorname{PSET}$), Lyndon Words / Pólya & Newton–Girard Power Sums

### 6.1 Architectural Split: Regime A (Exponent-Weighted Euler Products) vs. Regime B (Scalar Power Sums)

The operator $\frac{d}{dx} \ln F(x) = \frac{F'(x)}{F(x)}$ converts arbitrary products $F(x) = \prod_i f_i(x)$ into sums $\sum_i \frac{f_i'(x)}{f_i(x)}$. Across competitive programming, it governs **two fundamentally different regimes** that must be distinguished immediately:

| Feature | **Regime A: Exponent-Weighted Euler / Knapsack Products** | **Regime B: Scalar Root / Power Sum Products** |
| :--- | :--- | :--- |
| **Product Form** | $F(x) = \prod_{w=1}^N (1 \pm x^w)^{\pm c_w} \bmod x^{N+1}$ | $Q(x) = \prod_{i=1}^m (1 - a_i x) \bmod x^{N+1}$ |
| **Where is the variable $i$?** | Inside the **exponent** $x^w$ (each weight $w \in [1, N]$ is an integer). | Inside the **coefficient** $a_i x$ (each $a_i \in \mathbb{F}_p$ is an arbitrary scalar). |
| **Logarithmic Derivative** | $\ln F(x) = \sum_{w=1}^N c_w \sum_{k=1}^{\lfloor N/w \rfloor} \frac{(\pm 1)^k}{k} x^{kw}$ | $-x \frac{Q'(x)}{Q(x)} = \sum_{k=1}^\infty \left(\sum_{i=1}^m a_i^k\right) x^k = \sum_{k=1}^\infty p_k x^k$ |
| **Optimal Algorithm** | **Frequency Bucketing + Harmonic Sieve** in $O(N \log N)$ arithmetic + **1 FPS $\exp$** ($O(N \log N)$). | **Subproduct Tree** $\prod_{i=1}^m (1 - a_i x)$ in $O(m \log^2 m)$ + **1 FPS Inverse / $\ln$** ($O(N \log N)$). |

#### Reverse-Engineering Scratchpad (Deriving the Harmonic Sieve & Newton–Girard Bridge from Scratch)
1. **Why Frequency Bucketing + $\ln/\exp$ Beats $O(N^2)$ Knapsack DP (Regime A)**:  
   Given $n \le 10^5$ items of weights $v_1, \dots, v_n \in [1, N]$ ($N \le 10^5$), naive DP multiplies $F(x)$ by $(1 - x^{v_i})^{-1}$ one item at a time in $O(nN)$ time. Even if all $v_i = 1$, there are $n$ factors! However, at most $N$ distinct weights exist. Grouping identical weights into counts $c_w = \#\{i : v_i = w\}$ gives $F(x) = \prod_{w=1}^N (1 - x^w)^{-c_w}$. Taking $\ln F(x)$ turns the exponent $c_w$ into a scalar multiplier:
   $$\ln F(x) = \sum_{w=1}^N c_w \ln\frac{1}{1 - x^w} = \sum_{w=1}^N c_w \sum_{k=1}^{\lfloor N/w \rfloor} \frac{1}{k} x^{kw}$$
   Since the inner loop runs only $\lfloor N/w \rfloor$ times for each weight $w$, the total work across all $w \in [1, N]$ is $\sum_{w=1}^N \lfloor N/w \rfloor = O(N \log N)$!
2. **Why $-x\frac{Q'(x)}{Q(x)}$ Extracts Scalar Power Sums $p_k = \sum_{i=1}^m a_i^k$ (Regime B)**:  
   When the parameters $a_i$ are arbitrary scalars in $\mathbb{F}_p$ rather than integer exponents, each factor $(1 - a_i x)$ has degree $1$, so we can multiply all $m$ factors into $Q(x) = \prod_{i=1}^m (1 - a_i x)$ via a binary subproduct tree in $O(m \log^2 m)$ time. Then applying the operator $-x \frac{d}{dx} \ln$ linearizes the product into geometric series:
   $$-x \frac{Q'(x)}{Q(x)} = \sum_{i=1}^m \frac{a_i x}{1 - a_i x} = \sum_{i=1}^m \sum_{k=1}^\infty a_i^k x^k = \sum_{k=1}^\infty \left(\sum_{i=1}^m a_i^k\right) x^k$$

### 6.2 Regime A: Multiset ($\operatorname{MSET}$), Powerset ($\operatorname{PSET}$), and Inverse Euler Transform (Lyndon Words, Necklaces & Pólya Cycle Index)

#### 1. Forward Euler / Multiset ($\operatorname{MSET}$) & Powerset ($\operatorname{PSET}$) Transforms in $O(N \log N)$
Suppose a combinatorial class $\mathcal{A}$ has $a_w$ objects of weight $w \ge 1$.
- **Unlabeled Multisets ($\operatorname{MSET}(\mathcal{A})$ / 0-1 Unlimited Knapsack / Unrooted Trees)**:
  $$F_{\operatorname{MSET}}(x) = \prod_{w=1}^\infty \frac{1}{(1 - x^w)^{a_w}} \implies \boxed{\ln F_{\operatorname{MSET}}(x) = \sum_{w=1}^\infty a_w \sum_{k=1}^\infty \frac{x^{kw}}{k} = \sum_{n=1}^\infty \left(\frac{1}{n} \sum_{d \mid n} d\, a_d\right) x^n = \sum_{k=1}^\infty \frac{A(x^k)}{k}}$$
- **Unlabeled Powersets ($\operatorname{PSET}(\mathcal{A})$ / 0-1 Subset-Sum Knapsack)**:
  $$F_{\operatorname{PSET}}(x) = \prod_{w=1}^\infty (1 + x^w)^{a_w} \implies \boxed{\ln F_{\operatorname{PSET}}(x) = \sum_{w=1}^\infty a_w \sum_{k=1}^\infty \frac{(-1)^{k-1}}{k} x^{kw} = \sum_{k=1}^\infty \frac{(-1)^{k-1}}{k} A(x^k)}$$

**The $O(N \log N)$ Harmonic Sieve Algorithm**:
1. Bucket all items by integer weight $w \in [1, N]$ to form the frequency array $a_w$.
2. Initialize array $L[0 \dots N] = 0$. For each $w = 1 \dots N$ with $a_w \ne 0$, iterate over $k = 1, 2, \dots, \lfloor N/w \rfloor$ and add $a_w \cdot \text{inv}[k]$ (or $(-1)^{k-1} a_w \cdot \text{inv}[k]$) to $L[kw]$. By the harmonic series $\sum_{w=1}^N \frac{N}{w} = O(N \log N)$, this takes **$O(N \log N)$ additions** with tiny constant factor!
3. Return $\exp(L(x)) \bmod x^{N+1}$ in $O(N \log N)$.

#### 2. Inverse Euler Transform via Möbius Inversion (Recovering Connected Components & Lyndon Words)
What if we are given the multiset generating function $F(x) = \prod_{w=1}^\infty (1 - x^w)^{-a_w}$ and need to recover the primitive component counts $a_w$?
1. Compute $L(x) = \ln F(x) \bmod x^{N+1}$ in $O(N \log N)$.
2. Since $n [x^n] L(x) = \sum_{d \mid n} d\, a_d$, apply **Möbius Inversion** in $O(N \log N)$ via a divisor sieve:
   $$\boxed{a_n = \frac{1}{n} \sum_{d \mid n} \mu\!\left(\frac{n}{d}\right) d\, [x^d] \ln F(x)}$$
- **Lyndon Words (Aperiodic Prime Necklaces)**: Every word of length $n$ over an alphabet of size $\Sigma$ decomposes uniquely into a non-increasing concatenation of Lyndon words, so $\frac{1}{1 - \Sigma x} = \prod_{w=1}^\infty (1 - x^w)^{-\ell_w}$. Since $\ln\frac{1}{1-\Sigma x} = \sum_{d \ge 1} \frac{\Sigma^d}{d} x^d$, the Inverse Euler Transform immediately yields Witt's formula $\ell_n = \frac{1}{n} \sum_{d \mid n} \mu(n/d) \Sigma^d$!
- **Pólya–Redfield Cycle Index for Cyclic Necklaces ($\mathbb{Z}_n$)**: While Lyndon words count *aperiodic* prime cycles, counting all cyclic necklaces (cycles of $\mathbb{Z}_n$ acting on $A(x)^n$) uses the **Pólya Cycle Index**:
  $$Z_{\text{cycle}}(\mathcal{A})(x) = \sum_{k=1}^\infty \frac{\varphi(k)}{k} \ln \frac{1}{1 - A(x^k)}$$

### 6.3 Regime B: Newton–Girard Identities, Symmetric Polynomials & Characteristic $p$ Asymmetry

Given $m$ scalars $a_1, \dots, a_m \in K$, define the characteristic polynomial $Q(x) = \prod_{i=1}^m (1 - a_i x) = \sum_{k=0}^m (-1)^k e_k x^k$, complete homogeneous symmetric polynomials $H(x) = \frac{1}{Q(x)} = \sum_{k=0}^\infty h_k x^k$, and power sums $p_k = \sum_{i=1}^m a_i^k$ ($p_0 = m$).
Taking the logarithmic derivative of $Q(x)$ yields the **Newton–Girard Generating Function Bridge**:
$$\boxed{P(x) := \sum_{k=1}^\infty p_k x^k = \sum_{i=1}^m \frac{a_i x}{1 - a_i x} = -x \frac{Q'(x)}{Q(x)} = -x \frac{d}{dx} \ln Q(x) \iff Q(x) = \exp\!\left(-\sum_{k=1}^\infty \frac{p_k}{k} x^k\right)}$$

> [!IMPORTANT]
> **Critical Asymmetry When Characteristic $p \le N$ (`C2-New` Discovery)**
> - **Direction 1 ($e_k \to p_k$ via $P(x) = -x Q'(x) Q(x)^{-1}$)**: Works in **ANY characteristic $p$** (even when $p \le N$)! Why? Because $Q(0) = 1$ is invertible in $\mathbb{F}_p[[x]]$, and formal derivative $Q'(x)$ plus polynomial inversion $Q(x)^{-1}$ require **zero divisions by $k$**!
> - **Direction 2 ($p_k \to e_k$ via $Q(x) = \exp(-\sum \frac{p_k}{k} x^k)$)**: **Fails irrevocably when $p \le N$**! Algebraically, in characteristic $p$, Frobenius gives $p_p = \sum a_i^p = (\sum a_i)^p = p_1^p$, so the power sums $p_1, \dots, p_N$ do not even uniquely determine $e_p$!

---

## 7. Iteration 15 / 67: Roots of Unity Filter (`单位根反演`), Bluestein's Chirp-Z Transform & Cyclotomic Rings

### 7.1 Diagnostic Signals & Core Filter Identity

Whenever a problem requires extracting every $m$-th coefficient in a residue class $n \equiv r \pmod m$ from $F(x) = \sum_{n \ge 0} f_n x^n$, use the orthogonality of $m$-th roots of unity $\frac{1}{m}\sum_{j=0}^{m-1} \omega_m^{jk} = [m \mid k]$:
$$\boxed{F_{r \bmod m}(x) := \sum_{\substack{n \ge 0 \\ n \equiv r \pmod m}} f_n x^n = \frac{1}{m} \sum_{j=0}^{m-1} \omega_m^{-jr} F(\omega_m^j x)}$$
For small $m \in \{2, 4\}$, this specializes to the familiar parity and mod-4 filters:
- **$m = 2$**: $F_{\text{even}}(x) = \frac{F(x) + F(-x)}{2}$, $F_{\text{odd}}(x) = \frac{F(x) - F(-x)}{2}$.
- **$m = 4$**: $F_{r \bmod 4}(x) = \frac{1}{4}\left(F(x) + i^{-r}F(ix) + (-1)^r F(-x) + i^r F(-ix)\right)$, where $i = g^{(p-1)/4} \bmod p$ ($p = 998244353 \implies i = 86583718$).

#### Reverse-Engineering Scratchpad (Deriving the Roots of Unity Filter from Scratch)
Suppose we want to isolate $\sum_{n \equiv r \pmod m} f_n x^n$ from a closed-form generating function $F(x) = \sum_{n \ge 0} f_n x^n$ (such as $F(x) = (1 + sx)^N$ with $N \le 10^{18}$):
1. **Replace the Congruence Condition by an Indicator Sum**: Since $n \equiv r \pmod m \iff m \mid (n - r)$, we need an algebraic indicator for $[m \mid k]$. For a primitive $m$-th root of unity $\omega_m$, the geometric series $\sum_{j=0}^{m-1} (\omega_m^k)^j$ equals $m$ when $\omega_m^k = 1$ ($m \mid k$), and $\frac{\omega_m^{mk} - 1}{\omega_m^k - 1} = 0$ when $m \nmid k$.
2. **Push the Root Evaluation Inside $F(x)$**:
   $$\sum_{n \equiv r \pmod m} f_n x^n = \sum_{n=0}^\infty f_n x^n \left(\frac{1}{m} \sum_{j=0}^{m-1} \omega_m^{j(n-r)}\right) = \frac{1}{m} \sum_{j=0}^{m-1} \omega_m^{-jr} \sum_{n=0}^\infty f_n (\omega_m^j x)^n = \frac{1}{m} \sum_{j=0}^{m-1} \omega_m^{-jr} F(\omega_m^j x)$$
   This collapses an $O(N)$ summation over $n \le 10^{18}$ into $m$ point evaluations $F(\omega_m^j x)$, each computable in $O(\log N)$ time!

### 7.2 Bluestein's Chirp-Z Transform (Evaluating $F(\omega_m^j)$ for All $j$ in $O(m \log m)$)

Suppose $y_j = F(\omega_m^j x_0)$ has already been evaluated for each $j = 0, \dots, m-1$ (e.g., via binary exponentiation $(1 + \omega_m^j)^N$), and we need the filtered answers $c_r = \frac{1}{m} \sum_{j=0}^{m-1} y_j \omega_m^{-jr}$ for **all** $r = 0, \dots, m-1$ simultaneously when $m$ is not a power of $2$.
Using **Bluestein's Triangular Number Identity**
$$\boxed{-jr = \binom{j}{2} + \binom{r}{2} - \binom{j+r}{2}}$$
(since $\binom{j}{2} + \binom{r}{2} - \binom{j+r}{2} = \frac{j(j-1) + r(r-1) - (j+r)(j+r-1)}{2} = \frac{-2jr}{2} = -jr$ identically), we rewrite the Inverse Discrete Fourier Transform as a single linear convolution:
$$\boxed{c_r = \frac{\omega_m^{\binom{r}{2}}}{m} \sum_{j=0}^{m-1} \left(y_j\, \omega_m^{\binom{j}{2}}\right) \cdot \omega_m^{-\binom{j+r}{2}} = \frac{\omega_m^{\binom{r}{2}}}{m} \sum_{j=0}^{m-1} A^{\text{rev}}_{m-1-j}\, B_{j+r}}$$
where $A^{\text{rev}}_{m-1-j} = y_j \omega_m^{\binom{j}{2}}$ for $0 \le j < m$ and $B_k = \omega_m^{-\binom{k}{2}}$ for $0 \le k \le 2m-2$, so the sum is the exact coefficient at index $(m - 1 - j) + (j + r) = m - 1 + r$ of the polynomial product $A^{\text{rev}} \ast B$!

> [!CAUTION]
> **Two Classic Pitfalls in Bluestein's Chirp-Z Transform**
> 1. **Why You Must Use $\binom{k}{2} = \frac{k(k-1)}{2}$ Instead of $\frac{k^2}{2}$**: If $m$ is even (and especially when $m$ shares the maximal $2$-adic valuation of $p-1$), $\omega_m^{1/2}$ **does not exist** in $\mathbb{F}_p$, so $\omega_m^{k^2/2}$ is undefined for odd $k$! By contrast, $\binom{k}{2} = \frac{k(k-1)}{2}$ is **always an integer** for all $k \in \mathbb{Z}$.
> 2. **Sign Asymmetry of $\binom{j-r}{2}$ vs. $\binom{j+r}{2}$**: Because $\binom{k}{2} = \frac{k^2 - k}{2}$ contains a linear term $-\frac{k}{2}$, $\binom{j-r}{2} - \binom{j}{2} - \binom{r}{2} = -jr + r \ne -jr$! Always use $-jr = \binom{j}{2} + \binom{r}{2} - \binom{j+r}{2}$ (where the linear terms $\frac{j+r}{2}$ cancel identically) and reverse $A$ so that $(m - 1 - j) + (j + r) = m - 1 + r$.

### 7.3 Two Complete Fallbacks When $m \nmid (p - 1)$

What if $\mathbb{F}_p$ does not contain a primitive $m$-th root of unity (for instance, $m = 3$ or $m = 5$ modulo $p = 998244353$, since $998244352 = 2^{23} \times 7 \times 17$ is not divisible by $3$ or $5$)?

| Fallback Method | Algebraic Ring | Complexity to Compute $[x^{r \bmod m}] A(x)^N$ | Best Use Case |
| :--- | :--- | :--- | :--- |
| **Method A: Cyclic Quotient Ring** | $K[x] / (x^m - 1)$ | $O(m \log m \log N)$ via Chirp-Z/NTT + $\log N$ squarings, or $O(m^2 \log N)$ for small $m$. | Arbitrary $m \le 10^5$: tracks all $m$ residue buckets simultaneously without ever needing $\omega_m \in \mathbb{F}_p$! |
| **Method B: Cyclotomic Extension Ring** | $\mathbb{F}_p[\omega] / (\Phi_m(\omega))$ | $O(\varphi(m)^2 \cdot m \log N)$ (e.g., $O(\log N)$ in $\mathbb{F}_p[\omega]/(\omega^2+\omega+1)$ for $m=3$). | Small $m \in \{3, 5, 6\}$ or when $F(\omega^j)$ is evaluated by a closed-form formula rather than polynomial multiplication. |

> [!WARNING]
> **Why Adjoining $x^m - 1 = 0$ Directly Fails for Root Evaluation**  
> In $\mathbb{F}_p[\omega]/(\omega^m - 1)$, $1 + \omega + \dots + \omega^{m-1} \ne 0$ (since $(\omega - 1)(1 + \dots + \omega^{m-1}) = \omega^m - 1 = 0$ and $\omega - 1$ is a zero divisor!). To force the orthogonality identity $\sum_{j=0}^{m-1} \omega^{jk} = 0$ for $m \nmid k$, you **must** quotient by the $m$-th cyclotomic polynomial $\Phi_m(\omega)$ (for prime $m$, $\Phi_m(\omega) = 1 + \omega + \dots + \omega^{m-1} = 0$).

### 7.4 Binomial Floor Sums & Bivariate Generating Functions ($\lfloor i/m \rfloor$ Decomposition)

What if a problem asks for a weighted sum involving the floor function $\lfloor i / m \rfloor$ (or powers $\lfloor i / m \rfloor^d$), such as
$$S = \sum_{i=0}^n f_i \left\lfloor \frac{i}{m} \right\rfloor \quad \text{or} \quad \sum_{i=0}^n \binom{n}{i} s^i \left\lfloor \frac{i}{m} \right\rfloor$$
where $F(x) = \sum_{i=0}^n f_i x^i$ is a known generating function?

1. **Method 1: Division-Algorithm Linear + Periodic Split (`Floor-Sum Trick`)**  
   Substitute the exact division identity
   $$\boxed{\left\lfloor \frac{i}{m} \right\rfloor = \frac{i - (i \bmod m)}{m} = \frac{i}{m} - \frac{1}{m} \sum_{r=1}^{m-1} r\, [i \equiv r \pmod m]}$$
   - The **linear part** $\frac{1}{m} \sum_{i=0}^n i f_i = \frac{1}{m} F'(1)$ is extracted immediately by formal differentiation $\vartheta F(x) = x F'(x)$ at $x = 1$.
   - The **periodic remainder** is evaluated by the Roots of Unity Filter:
     $$\sum_{r=1}^{m-1} r \sum_{i \equiv r \pmod m} f_i = \frac{1}{m} \sum_{j=0}^{m-1} F(\omega_m^j) \sum_{r=1}^{m-1} r\, \omega_m^{-jr}$$
     Moreover, for every $j \in \{1, \dots, m-1\}$ ($\omega_m^{-j} \ne 1$), the inner geometric-arithmetic sum collapses in $O(1)$ to:
     $$\sum_{r=1}^{m-1} r\, \omega_m^{-jr} = \frac{m}{\omega_m^{-j} - 1}$$
     giving the closed-form **Master Floor-Sum Identity**:
     $$\boxed{\sum_{i=0}^n f_i \left\lfloor \frac{i}{m} \right\rfloor = \frac{F'(1)}{m} - \frac{m-1}{2m} F(1) - \frac{1}{m} \sum_{j=1}^{m-1} \frac{F(\omega_m^j)}{\omega_m^{-j} - 1}}$$
2. **Method 2: Bivariate Generating Function in $K[x, y] / (x^m - y)$**  
   Write $i = qm + r$ with $q = \lfloor i / m \rfloor$ and $r = i \bmod m \in \{0, \dots, m-1\}$. Working in the quotient ring $K[y][x] / (x^m - y)$ (where every carry $x^m$ is replaced by $y$) rewrites $F(x)$ as $\tilde{F}(x, y) = \sum_{r=0}^{m-1} x^r \sum_{q \ge 0} f_{qm+r} y^q$. Differentiating with respect to $y$ ($\left.\frac{\partial}{\partial y}\right|_{y=1}$, or maintaining a 1st-order jet $a + b\varepsilon$ with $y = 1 + \varepsilon, \varepsilon^2 = 0$) extracts $\sum_i f_i \lfloor i / m \rfloor$ even when $m \nmid (p - 1)$!

---

## 8. Unified Master Lookup Table & Complete Production C++20 Library

### 8.1 Master 18-Row Substitution & Sequence Transform Reference Table

| # | Transform / Substitution | Coefficient Formula for $b_n = [x^n]B(x)$ | Generating Function Identity | Optimal Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Euler's Series Transform** | $\sum_{k=0}^n \binom{n}{k} c^{n-k} a_k$ | $B(x) = \frac{1}{1-cx} A\!\left(\frac{x}{1-cx}\right) \iff \widehat{B}(z) = e^{cz}\widehat{A}(z)$ | $O(n \log n)$ (1 NTT) |
| **2** | **Generalized $\alpha$-Euler Transform** | $\sum_{k=0}^n \binom{n+\alpha-1}{n-k} a^k c^{n-k} f_k$ | $E(x) = (1-cx)^{-\alpha} F\!\left(\frac{ax}{1-cx}\right)$ | $O(n \log n)$ (1 NTT) |
| **3** | **Polynomial Taylor Shift** | $b_k = \sum_{n=k}^N \binom{n}{k} c^{n-k} a_n$ | $B(x) = A(x+c)$ ($\deg A = N$) | $O(N \log N)$ (1 NTT) |
| **4** | **Projective $\mathrm{GL}_2(K)$ Action** | $[x^n] \sum_{k=0}^N a_k (ax+b)^k (cx+d)^{N-k}$ | $(\mathcal{M}_g A)(x) = (cx+d)^N A\!\left(\frac{a}{c} + \frac{bc-ad}{c(cx+d)}\right)$ | $O(N \log N)$ ($\le 2$ NTTs) |
| **5** | **Krawtchouk Transform** | $\sum_{k=0}^N a_k \sum_j (-1)^j \binom{k}{j}\binom{N-k}{n-j}$ | $K_A(x) = (1+x)^N A\!\left(\frac{1-x}{1+x}\right)$ | $O(N \log N)$ (1–2 NTTs) |
| **6** | **Catalan Substitution I & II** | $[x^n] F(C(x))$ | $x = u(1-u)$ ($C=\frac{1}{1-u}$) or $x = \frac{u}{(1+u)^2}$ ($C=1+u$) | $O(n \log n)$ |
| **7** | **Universal Quadratic Radical** | $[x^n] \frac{G(x)}{\sqrt{1-2ax+bx^2}}$ | $x = \frac{u}{1+au+cu^2}$ ($c=\frac{a^2-b}{4}$): $[u^n] H(u)(1+au+cu^2)^n$ | $O(n \log n)$ |
| **8** | **Motzkin Substitution** | $M_n = \sum_{k} \binom{n}{2k} C_k$ | $x = \frac{u}{1+u+u^2} \implies \sqrt{1-2x-3x^2} = \frac{1-u^2}{1+u+u^2}$ | $O(n)$ / $O(n \log n)$ |
| **9** | **Delannoy & Large Schröder** | $D_n = \sum_{j=0}^n \binom{n}{j}^2 2^j$ | $x = \frac{u}{(1+u)(1+2u)} \implies \sqrt{1-6x+x^2} = \frac{1-2u^2}{(1+u)(1+2u)}$ | $O(n)$ / $O(n \log n)$ |
| **10** | **Narayana Peak Transform** | $N(n,k) = \frac{1}{n}\binom{n}{k}\binom{n}{k-1}$ | $x = \frac{u}{(1+u)(1+tu)} \implies [x^n]u = \frac{1}{n}[u^{n-1}](1+u)^n(1+tu)^n$ | $O(n)$ |
| **11** | **Chebyshev Bounded Walk** | Walks of length $N$ in $0 \le y \le H$ | $x = \frac{u}{1+u^2} \implies [u^N](1-u^2)(1+u^2)^N \frac{1-u^{2H+2}}{1-u^{2H+4}}$ | $O(N / H)$ per $H$ |
| **12** | **Stirling 2nd Kind (Row / Col)** | ${n \brace k}$ (Row $n$ or Col $k$) | Row: $\frac{1}{k!}\sum (-1)^{k-j}\binom{k}{j}j^n$; Col: $\frac{(e^x-1)^k}{k!}$ | $O(n \log n)$ |
| **13** | **Stirling 1st Kind (Row / Col)** | ${n \brack k}$ (Row $n$ or Col $k$) | Row: $x^{\overline{n}} = x^{\overline{m}}(x+m)^{\overline{m}}$; Col: $\frac{(-\ln(1-x))^k}{k!}$ | $O(n \log n)$ |
| **14** | **Lah Transform** | $\sum_{k=0}^n \binom{n-1}{k-1}\frac{n!}{k!} a_k$ | $\widehat{B}(x) = \widehat{A}\!\left(\frac{x}{1-x}\right)$ | $O(n \log n)$ (1 NTT) |
| **15** | **Falling-Factorial (`下降幂`)** | $P(x) = \sum_{k=0}^n c_k x^{\underline{k}}$ | $\widehat{P}(t) = \sum_{m \ge 0} P(m)\frac{t^m}{m!} = C(t)e^t$ | $O(n \log n)$ (1 NTT) |
| **16** | **Euler / Multiset ($\operatorname{MSET}/\operatorname{PSET}$)** | $[x^n]\prod_{w=1}^N (1 \mp x^w)^{\mp a_w}$ | $\ln F(x) = \sum_{w=1}^N a_w \sum_{k=1}^{\lfloor N/w \rfloor} \frac{(\pm 1)^{k-1}}{k} x^{kw}$ | $O(N \log N)$ Sieve + $\exp$ |
| **17** | **Newton–Girard Power Sums** | $p_k = \sum_{i=1}^m a_i^k \leftrightarrow e_k$ | $\sum_{k \ge 1} p_k x^k = -x \frac{Q'(x)}{Q(x)}$, $Q(x) = \prod_{i=1}^m (1 - a_i x)$ | $O(m \log^2 m + N \log N)$ |
| **18** | **Roots of Unity Filter & Chirp-Z** | $\sum_{n \equiv r \pmod m} f_n x^n$ | $\frac{1}{m}\sum_{j=0}^{m-1} \omega_m^{-jr} F(\omega_m^j x)$ via $-jr = \binom{j}{2}+\binom{r}{2}-\binom{j+r}{2}$ | $O(m \log m)$ (1 NTT) |

### 8.2 Complete Production C++20 Reference Implementations

```cpp
#include <bits/stdc++.h>
using namespace std;

constexpr int MOD = 998244353;
constexpr int G_ROOT = 3;

long long qpow(long long a, long long b) {
    long long res = 1;
    a %= MOD;
    if (a < 0) a += MOD;
    while (b > 0) {
        if (b & 1) res = res * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return res;
}

// Assume standard Poly library primitives:
// vector<int> multiply(vector<int> a, vector<int> b);
// vector<int> poly_inv(vector<int> a, int n);
// vector<int> poly_ln(vector<int> a, int n);
// vector<int> poly_exp(vector<int> a, int n);
// and precomputed fact[], inv_fact[], inv[].

// 1. Polynomial Taylor Shift B(x) = A(x + c) in O(N log N) (1 NTT)
vector<int> taylor_shift(const vector<int>& a, int c,
                         const vector<int>& fact, const vector<int>& inv_fact) {
    int n = (int)a.size() - 1;
    if (n < 0) return {};
    c = (c % MOD + MOD) % MOD;
    if (c == 0) return a;
    vector<int> u(n + 1), v(n + 1);
    long long cp = 1;
    for (int i = 0; i <= n; ++i) {
        u[n - i] = 1LL * a[i] * fact[i] % MOD;
        v[i] = cp * inv_fact[i] % MOD;
        cp = cp * c % MOD;
    }
    vector<int> w = multiply(u, v);
    vector<int> b(n + 1);
    for (int k = 0; k <= n; ++k)
        b[k] = 1LL * w[n - k] * inv_fact[k] % MOD;
    return b;
}

// 2. General Projective Mobius Action (cx + d)^n A((ax + b)/(cx + d)) in O(N log N) (<= 2 NTTs)
// Division-free wrt d (handles d = 0 and c = 0 cleanly without any division by zero)
vector<int> mobius_transform(vector<int> a_poly, long long a, long long b,
                             long long c, long long d,
                             const vector<int>& fact, const vector<int>& inv_fact) {
    int n = (int)a_poly.size() - 1;
    if (n < 0) return {};
    a = (a % MOD + MOD) % MOD; b = (b % MOD + MOD) % MOD;
    c = (c % MOD + MOD) % MOD; d = (d % MOD + MOD) % MOD;
    if (c == 0) {
        // G(x) = sum_{k=0}^n a_poly[k] * d^(n-k) * (ax + b)^k
        vector<int> f1(n + 1);
        long long dp = 1;
        for (int k = n; k >= 0; --k) {
            f1[k] = 1LL * a_poly[k] * dp % MOD;
            dp = dp * d % MOD;
        }
        auto f2 = taylor_shift(f1, b, fact, inv_fact);
        long long ap = 1;
        for (int k = 0; k <= n; ++k) {
            f2[k] = 1LL * f2[k] * ap % MOD;
            ap = ap * a % MOD;
        }
        return f2;
    }
    // Bruhat 4-step decomposition for c != 0: (ax+b)/(cx+d) = a/c + (bc-ad)/(c*(cx+d))
    long long inv_c = qpow(c, MOD - 2);
    long long alpha = a * inv_c % MOD;
    long long beta = ((b * c - a * d) % MOD + MOD) % MOD * inv_c % MOD;

    // Step 1: F1(y) = A(y + alpha)
    auto f1 = taylor_shift(a_poly, alpha, fact, inv_fact);

    // Step 2: F2(y) = y^n F1(beta / y)
    vector<int> f2(n + 1);
    long long bp = 1;
    for (int k = 0; k <= n; ++k) {
        f2[n - k] = 1LL * f1[k] * bp % MOD;
        bp = bp * beta % MOD;
    }

    // Step 3: F3(y) = F2(y + d)
    auto f3 = taylor_shift(f2, d, fact, inv_fact);

    // Step 4: G(x) = F3(c * x)
    long long cp = 1;
    for (int j = 0; j <= n; ++j) {
        f3[j] = 1LL * f3[j] * cp % MOD;
        cp = cp * c % MOD;
    }
    return f3;
}

// 3. Stirling Numbers of 2nd Kind (Fixed Row n): S(n, 0..n) in O(n log n) (1 NTT)
vector<int> stirling_second_kind_row(int n, const vector<int>& inv_fact) {
    vector<int> A(n + 1), B(n + 1);
    for (int i = 0; i <= n; ++i) {
        A[i] = qpow(i, n) * inv_fact[i] % MOD;
        B[i] = (i & 1) ? (MOD - inv_fact[i]) : inv_fact[i];
    }
    auto C = multiply(A, B);
    C.resize(n + 1);
    return C;
}

// 4. Stirling Numbers of 2nd Kind (Fixed Column k): S(0..n, k) in O(n log n)
vector<int> stirling_second_kind_column(int n, int k,
                                        const vector<int>& fact, const vector<int>& inv_fact) {
    if (k > n) return vector<int>(n + 1, 0);
    if (k == 0) {
        vector<int> res(n + 1, 0);
        res[0] = 1;
        return res;
    }
    int len = n - k + 1;
    vector<int> G(len); // G(x) = (e^x - 1) / x = sum_{i>=0} x^i / (i+1)!
    for (int i = 0; i < len; ++i) G[i] = inv_fact[i + 1];
    auto lnG = poly_ln(G, len);
    for (int i = 0; i < len; ++i) lnG[i] = 1LL * lnG[i] * k % MOD;
    auto expG = poly_exp(lnG, len);
    vector<int> res(n + 1, 0);
    for (int i = k; i <= n; ++i) {
        res[i] = 1LL * expG[i - k] * fact[i] % MOD * inv_fact[k] % MOD;
    }
    return res;
}

// 5. Unsigned Stirling Numbers of 1st Kind (Fixed Row n): x^{\overline{n}} in O(n log n) via Doubling
vector<int> stirling_1st_row(int n, const vector<int>& fact, const vector<int>& inv_fact) {
    if (n == 0) return {1};
    auto solve = [&](auto& self, int m) -> vector<int> {
        if (m == 1) return {0, 1};
        int half = m / 2;
        auto f = self(self, half);
        auto f_shift = taylor_shift(f, half, fact, inv_fact);
        auto res = multiply(f, f_shift);
        if (m & 1) {
            res.push_back(0);
            for (int i = m; i >= 1; --i)
                res[i] = (res[i - 1] + 1LL * (m - 1) * res[i]) % MOD;
            res[0] = 1LL * (m - 1) * res[0] % MOD;
        }
        return res;
    };
    return solve(solve, n);
}

// 6. Unsigned Lah Numbers (Fixed Row n): L(n, 0..n) in O(n)
vector<int> lah_numbers_row(int n, const vector<int>& fact, const vector<int>& inv_fact) {
    vector<int> L(n + 1, 0);
    if (n == 0) { L[0] = 1; return L; }
    for (int k = 1; k <= n; ++k) {
        long long c_n1_k1 = 1LL * fact[n - 1] * inv_fact[k - 1] % MOD * inv_fact[n - k] % MOD;
        L[k] = c_n1_k1 * fact[n] % MOD * inv_fact[k] % MOD;
    }
    return L;
}

// 7. Falling-Factorial Polynomial Basis Coefficients from Point Values P(0..n) in O(n log n)
vector<int> ffp_from_values(const vector<int>& val, const vector<int>& inv_fact) {
    int n = (int)val.size() - 1;
    vector<int> p_hat(n + 1), exp_neg(n + 1);
    for (int i = 0; i <= n; ++i) {
        p_hat[i] = 1LL * val[i] * inv_fact[i] % MOD;
        exp_neg[i] = (i & 1) ? (MOD - inv_fact[i]) : inv_fact[i];
    }
    auto c = multiply(p_hat, exp_neg);
    c.resize(n + 1);
    return c;
}

// 8. Regime A: Multiset / Euler Transform prod_{w=1}^N (1 - x^w)^{-a_w} mod x^{N+1} in O(N log N)
vector<int> euler_multiset_transform(const vector<int>& a_weight, int N, const vector<int>& inv) {
    vector<int> ln_F(N + 1, 0);
    for (int w = 1; w <= N; ++w) {
        if (!a_weight[w]) continue;
        for (int k = 1; k * w <= N; ++k) {
            ln_F[k * w] = (ln_F[k * w] + 1LL * a_weight[w] * inv[k]) % MOD;
        }
    }
    return poly_exp(ln_F, N + 1);
}

// 9. Regime B: Newton-Girard Elementary Symmetric e[1..n] -> Power Sums p[1..K] in O(K log K)
// Works in ANY characteristic p since Q'(x) * Q(x)^{-1} requires zero divisions by k!
vector<int> elementary_to_power_sums(const vector<int>& e, int K) {
    int n = (int)e.size() - 1;
    vector<int> Q(min(n, K) + 1, 0);
    Q[0] = 1;
    for (int k = 1; k <= min(n, K); ++k) {
        Q[k] = (k & 1) ? (MOD - e[k]) % MOD : e[k] % MOD;
    }
    vector<int> dQ(max(1, (int)Q.size() - 1), 0);
    for (int k = 1; k < (int)Q.size(); ++k) {
        dQ[k - 1] = 1LL * k * Q[k] % MOD;
    }
    auto invQ = poly_inv(Q, K + 1);
    auto prod = multiply(dQ, invQ);
    vector<int> p(K + 1, 0);
    for (int k = 1; k <= K && k - 1 < (int)prod.size(); ++k) {
        p[k] = (MOD - prod[k - 1]) % MOD; // P(x) = -x Q'(x) / Q(x)
    }
    return p;
}

// 10. Bluestein's Chirp-Z Transform for Roots of Unity Filter in O(m log m)
// Given y[j] = F(w_m^j), returns c[r] = (1/m) * sum_{j=0}^{m-1} y[j] * w_m^{-j*r}
// Uses the verified identity: -j*r = C(j, 2) + C(r, 2) - C(j+r, 2)
vector<int> bluestein_roots_filter(const vector<int>& y, int m, int wm) {
    int inv_wm = qpow(wm, MOD - 2), inv_m = qpow(m, MOD - 2);
    auto C2 = [](long long k) -> long long { return k * (k - 1) / 2; };
    vector<int> A_rev(m), B(2 * m - 1);
    for (int j = 0; j < m; ++j) {
        A_rev[m - 1 - j] = 1LL * y[j] * qpow(wm, C2(j) % m) % MOD;
    }
    for (int k = 0; k <= 2 * m - 2; ++k) {
        B[k] = qpow(inv_wm, C2(k) % m);
    }
    auto conv = multiply(A_rev, B);
    vector<int> c(m);
    for (int r = 0; r < m; ++r) {
        long long factor = 1LL * inv_m * qpow(wm, C2(r) % m) % MOD;
        c[r] = 1LL * conv[m - 1 + r] * factor % MOD;
    }
    return c;
}

// 11. Cyclotomic Extension Ring F_p[w] / (w^2 + w + 1) for m = 3 when 3 \nmid (p - 1)
struct Ext3 {
    long long a, b; // represents a + b * w, where w^2 = -1 - w
    Ext3(long long _a = 0, long long _b = 0) : a((_a % MOD + MOD) % MOD), b((_b % MOD + MOD) % MOD) {}
    Ext3 operator+(const Ext3& o) const { return Ext3(a + o.a, b + o.b); }
    Ext3 operator-(const Ext3& o) const { return Ext3(a - o.a, b - o.b); }
    Ext3 operator*(const Ext3& o) const {
        long long c0 = a * o.a % MOD;
        long long c1 = (a * o.b + b * o.a) % MOD;
        long long c2 = b * o.b % MOD;
        return Ext3(c0 - c2, c1 - c2);
    }
};
```

---

## 9. Master Multilingual Resource & Citation Audit Table (`[EN]`, `[ZH]`, `[JA]`)

| Tag | Source / Author / Title | URL / Reference | Primary Iterations & Unique Pedagogical Value |
| :--- | :--- | :--- | :--- |
| `[EN]` | **Philippe Flajolet & Robert Sedgewick**, *Analytic Combinatorics* (Cambridge Univ. Press, 2009), Ch. I–III & Appendix B | <https://algo.inria.fr/flajolet/Publications/AnaCombi/anacombi.html> | **Iter 11–15**: Symbolic method ($\operatorname{SEQ}, \operatorname{SET}, \operatorname{CYC}, \operatorname{MSET}, \operatorname{PSET}$), Pólya–Redfield cycle index, Chebyshev continued fractions for bounded-height Dyck walks, and Borel/Laplace bridges. |
| `[EN]` | **Herbert S. Wilf**, *generatingfunctionology* (3rd ed., A K Peters, 2006), Ch. 2 & 4 | <https://www2.math.upenn.edu/~wilf/DownldGF.html> | **Iter 11, 13, 14**: Exponential formula $\exp/\ln$ for connected components, Stirling/Bell EGFs, and snake-oil summation. |
| `[EN]` | **Donald E. Knuth**, *The Art of Computer Programming, Vol. 4A*, §7.2.1.6 | Standard Print Reference | **Iter 12**: Definitive derivation of why rational substitutions $x = \frac{u}{1+au+cu^2}$ diagonalize Catalan, Motzkin, and Schröder radicals. |
| `[EN]` | **Leo I. Bluestein**, *"A linear filtering approach to the computation of discrete Fourier transform"*, IEEE Transactions on Audio and Electroacoustics, 18(4):451–455, 1970 | <https://doi.org/10.1109/TAU.1970.1162132> | **Iter 15**: Original paper introducing the Chirp-Z transform reducing arbitrary-length $m$-point DFT/IDFT to linear convolution. |
| `[EN]` | **Alfred V. Aho, Kenneth Steiglitz & Jeffrey D. Ullman**, *"Evaluating polynomials at fixed sets of points"*, SIAM Journal on Computing, 4(4):533–539, 1975 | <https://doi.org/10.1137/0204045> | **Iter 11, 13**: Foundational complexity paper proving $O(n \log n)$ Taylor shift $A(x+c)$ via reversal convolution and fast basis conversions between monomial and factorial bases. |
| `[EN]` | **Alin Bostan, Frédéric Chyzak, Giancarlo Lecerf, Bruno Salvy & Éric Schost**, *"Differential equations for algebraic functions"*, ISSAC 2007 / Journal of Complexity, 2017 | <https://specfun.inria.fr/bostan/publications/BoChLeSaSc07.pdf> | **Iter 12**: Rigorous computer-algebra foundation for converting quadratic/algebraic generating functions into D-finite linear differential recurrences solvable in $O(n)$ time. |
| `[EN]` | **3Blue1Brown (Grant Sanderson)**, *Olympiad level counting (Generating functions & roots of unity)* | <https://www.3blue1brown.com/lessons/olympiad-counting> | **Iter 15**: Visual geometric intuition for the roots-of-unity filter $\frac{1}{m}\sum_{j=0}^{m-1} \omega_m^{-jr} F(\omega_m^j x)$. |
| `[EN]` | **Codeforces — adamant**, *Polya enumeration theorem and Burnside's lemma* & *Chirp Z-transform* | <https://codeforces.com/blog/entry/89228> | **Iter 14, 15**: Connecting $\ln/\exp$ multiset transforms to cycle indices and Bluestein's identity $-jr = \binom{j}{2}+\binom{r}{2}-\binom{j+r}{2}$. |
| `[ZH]` | **OI-Wiki**, *多项式平移 / 斯特林数 / 下降幂多项式 / 单位根反演* | <https://oi-wiki.org/math/poly/lagrange/> & <https://oi-wiki.org/math/combinatorics/stirling/> | **Iter 11, 13, 15**: Complete Chinese competitive programming encyclopedia entries for Taylor shift, all 4 fast Stirling algorithms, falling-factorial polynomials, and `单位根反演`. |
| `[ZH]` | **鐘子謙 (Zhong Ziqian, NOI 2018 National Team Paper)**, *《两类递推数列的性质和应用》 (Properties and Applications of Two Classes of Recurrent Sequences)* | *NOI 2018 国家集训队论文集* | **Iter 13**: Seminal Chinese Olympiad monograph introducing Falling-Factorial Polynomials (`下降幂多项式`) and the Point-Value EGF multiplication $\widehat{P}(t) = C(t)e^t$. |
| `[ZH]` | **command_block (洛谷博客)**, *《多项式计数杂谈》 & 《单位根反演小记》* | <https://www.luogu.com.cn/blog/command-block/duo-xiang-shi-ji-shu-za-tan> | **Iter 11–15**: High-level Olympiad synthesis of Euler/Möbius substitutions, $\ln/\exp$ knapsack bucketing, and roots-of-unity filters. |
| `[JA]` | **maspy (Maspy's HP)**, *形式的べき級数解説 (Formal Power Series Commentary) & AtCoder / FPS-24 Editorials* | <https://maspypy.com/> | **Iter 11–15**: Systematic FPS substitution philosophy: solving problems by changing variables $x = \phi(u)$ and extracting residues rather than recurrence guessing. |
| `[JA]` | **Nyaan's Library**, *FPS Taylor Shift / Stirling Number / Rational & Exponential Composition (`fps/taylor-shift.hpp`, `fps/composite-exp.hpp`)* | <https://nyaannyaan.github.io/library/> | **Iter 11, 13, 14**: Production C++ implementations of Taylor shift, $\mathcal{L}\{P(e^{cz})\}$ rational D&C sum, and Stirling generators. |
| `[JA]` | **noshi91**, *FPS の合成と逆関数 / 固有値とチェビシェフ多項式* | <https://noshi91.hatenablog.com/> | **Iter 12, 14**: Algebraic analysis of Chebyshev rational substitutions for bounded walks and subproduct-tree power-sum algorithms. |

---

## 10. Deduplicated Template Rejections & Master Curated Practice Problem Bank

### 10.1 Rejected Pure Template Problems (12 Problems Excluded from Practice Bank)

To maintain strict pedagogical quality, the following **12 pure library-verification / bare-formula problems** across `C1`, `C2-New`, and `C2-Pre` are cataloged here for algorithmic testing only and excluded from the curated problem bank:

| # | Problem ID & Title | Judge / URL | Iteration | Reason for Rejection |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Library Checker — `polynomial_taylor_shift`** | <https://judge.yosupo.jp/problem/polynomial_taylor_shift> | Iter 11 | Bare verification of $A(x+c)$ with zero combinatorial modeling. |
| 2 | **Luogu P5393 — 下降幂多项式乘法** | <https://www.luogu.com.cn/problem/P5393> | Iter 13 | Direct black-box call to FFP multiplication via $\widehat{P}(t) = C(t)e^t$. |
| 3 | **Luogu P5394 — 【模板】下降幂多项式乘法** | <https://www.luogu.com.cn/problem/P5394> | Iter 13 | Duplicate bare template for FFP multiplication. |
| 4 | **Library Checker — `stirling_number_of_the_first_kind`** | <https://judge.yosupo.jp/problem/stirling_number_of_the_first_kind> | Iter 13 | Direct output of signed ${n \brack k}$ for fixed $n$. |
| 5 | **Luogu P5408 / P5383 — 第一类斯特林数·行** | <https://www.luogu.com.cn/problem/P5408> | Iter 13 | Bare template for unsigned ${n \brack k}$ (fixed row $n$). |
| 6 | **Library Checker — `stirling_number_of_the_first_kind_fixed_k`** | <https://judge.yosupo.jp/problem/stirling_number_of_the_first_kind_fixed_k> | Iter 13 | Direct output of $\frac{(\ln(1+x))^k}{k!}$. |
| 7 | **Luogu P5409 — 第一类斯特林数·列** | <https://www.luogu.com.cn/problem/P5409> | Iter 13 | Bare template for $\frac{(-\ln(1-x))^k}{k!}$. |
| 8 | **Library Checker — `stirling_number_of_the_second_kind`** | <https://judge.yosupo.jp/problem/stirling_number_of_the_second_kind> | Iter 13 | Direct output of ${n \brace k}$ for fixed $n$. |
| 9 | **Luogu P5395 — 第二类斯特林数·行** | <https://www.luogu.com.cn/problem/P5395> | Iter 13 | Bare template for ${n \brace k}$ (fixed row $n$). |
| 10 | **Library Checker — `stirling_number_of_the_second_kind_fixed_k`** | <https://judge.yosupo.jp/problem/stirling_number_of_the_second_kind_fixed_k> | Iter 13 | Direct output of $\frac{(e^x-1)^k}{k!}$. |
| 11 | **Luogu P5396 — 第二类斯特林数·列** | <https://www.luogu.com.cn/problem/P5396> | Iter 13 | Bare template for $\frac{(e^x-1)^k}{k!}$. |
| 12 | **Library Checker — `find_linear_recurrence` / `kth_term_of_linearly_recurrent_sequence`** | <https://judge.yosupo.jp/problem/kth_term_of_linearly_recurrent_sequence> | Iter 15 | Pure Berlekamp–Massey + Bostan–Mori template without a substitution wrapper (covered in Wave 1B). |

---

### 10.2 Master Curated Practice Problem Bank (All 49 Accepted Problems Across Iterations 11–15)

Every accepted problem from `C1`, `C2-New`, and `C2-Pre` is preserved below in full pedagogical detail, organized by Iteration and progressed across all 4 difficulty tiers (`Stepping Stone` $\to$ `Intermediate` $\to$ `Advanced` $\to$ `Mastery`).

---

#### Module A: Iteration 11 / 63 — Rational, Linear & Möbius Substitutions (Problems 1–13)

##### Problem 1 (`Stepping Stone` — Iter 11): AtCoder FPS-24 H — Jump (`C1`)
- **Link**: <https://atcoder.jp/contests/fps-24/tasks/fps_24_h>
- **Mathematical Statement**: On a 2D coordinate plane, a piece starts at $(0, 0)$. You may perform the following operation any number of times (including zero): choose an integer pair $(a, b)$ such that $0 \le a \le 1$, $b \ge 0$, and $(a, b) \neq (0, 0)$, and move the piece from $(x, y)$ to $(x + a, y + b)$. Find the number of operation sequences that end at $(N, M)$ modulo $998244353$, where $1 \le N, M \le 2 \times 10^5$.
- **Diagnostic Signal**: The bivariate OGF of a single move is $S(x, y) = \sum_{b \ge 1} y^b + x \sum_{b \ge 0} y^b = \frac{x + y}{1 - y}$; adding the idle move $1$ separates variables into $1 + S(x, y) = \frac{1 + x}{1 - y}$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Write the bivariate OGF of a single valid move: $S(x, y) = \sum_{a=0}^1 \sum_{b=0}^\infty x^a y^b - 1 = \frac{1 + x}{1 - y} - 1 = \frac{x + y}{1 - y}$.
  - *Hint 2*: Summing over all step counts $k \ge 0$ gives the total bivariate OGF $F(x, y) = \frac{1}{1 - S(x, y)} = \frac{1 - y}{1 - 2y - x}$. Alternatively, include the $(0, 0)$ step by setting $G(x, y) = 1 + S(x, y) = \frac{1 + x}{1 - y}$, which separates variables into $x$ and $y$!
  - *Hint 3*: Extract $[x^N]$ first from $\frac{1 - y}{(1 - 2y) - x}$, then extract $[y^M]$ using the negative binomial series.
- **Full Algebraic Derivation**:
  - **Method 1 (Direct Bivariate Substitution & Coefficient Extraction in $O(N + M)$ Time)**:
    Summing $S(x, y) = \frac{x + y}{1 - y}$ over all operation sequence lengths $k \ge 0$ yields:
    $$F(x, y) = \sum_{k=0}^\infty S(x, y)^k = \frac{1}{1 - \frac{x + y}{1 - y}} = \frac{1 - y}{(1 - 2y) - x} = \frac{1 - y}{1 - 2y} \cdot \frac{1}{1 - \frac{x}{1 - 2y}}$$
    Extracting $[x^N]$ first gives $[x^N] F(x, y) = \frac{1 - y}{(1 - 2y)^{N+1}}$. Extracting $[y^M]$ via $[y^m] (1 - 2y)^{-(N+1)} = 2^m \binom{N + m}{m}$ gives the closed-form solution:
    $$\text{Ans} = [y^M] (1 - y)(1 - 2y)^{-(N+1)} = 2^M \binom{N + M}{M} - 2^{M-1} \binom{N + M - 1}{M - 1} \bmod 998244353$$
  - **Method 2 (Fixed-$k$ Step Enumeration via Shift Substitution $G = 1 + S$)**:
    If we instead need the number of $k$-step walks $a_k = [x^N y^M] S(x, y)^k$ for each $1 \le k \le N + M$, notice that $G(x, y) = 1 + S(x, y) = (1 + x)(1 - y)^{-1}$ factors along the $x$- and $y$-axes, so $b_k = [x^N y^M] G(x, y)^k = \binom{k}{N} \binom{k + M - 1}{M}$. Since $S = G - 1$, binomial inversion (an EGF shift by $e^{-t}$) recovers $a_k = \sum_{j=0}^k (-1)^{k-j} \binom{k}{j} b_j$ for all $k$ via a single NTT convolution in $O((N + M) \log(N + M))$ time. Similarly, for Delannoy-step walks $(x + y + xy)^N = ((1+x)(1+y) - 1)^N$, Euler's substitution $u = \frac{t}{1+t}$ decouples $(1+x)(1+y)$ in $O(N)$ time.

##### Problem 2 (`Stepping Stone` — Iter 11): Codeforces 923E — Perpetual Subtraction (`C2-Pre`)
- **Link**: <https://codeforces.com/problemset/problem/923/E>
- **Mathematical Statement**: Initially a number $x \in \{0, 1, \dots, N\}$ is chosen with probability $p_x$. In each of $M$ rounds ($N \le 10^5$, $M \le 10^{18}$), if the current number is $k$, it is replaced by an integer chosen uniformly at random from $\{0, 1, \dots, k\}$. Find the final probability distribution $p^{(M)}_0, \dots, p^{(M)}_N$ modulo $998244353$.
- **Diagnostic Signal**: One transition step maps $p^{(t)}_j = \sum_{k=j}^N \frac{p^{(t-1)}_k}{k+1}$. How does this upper-triangular operator act on $P(x) = \sum_{k=0}^N p_k x^k$?
- **3-Tier Progressive Hints**:
  - *Hint 1*: In the standard monomial basis $P(x) = \sum_{k=0}^N p_k x^k$, one transition maps $x^k \mapsto \frac{1}{k+1}\sum_{j=0}^k x^j = \frac{x^{k+1}-1}{(k+1)(x-1)}$. The denominator $x-1$ suggests shifting the polynomial center to $x = 1$ via a **Taylor shift** $Q(y) = P(y+1)$!
  - *Hint 2*: Expand $P(x)$ in the shifted basis $y = x - 1$: $Q(y) = P(y+1) = \sum_{m=0}^N q_m y^m$, where $q_m = \sum_{k=m}^N \binom{k}{m} p_k$ is the $m$-th binomial moment.
  - *Hint 3*: By Pascal's hockey-stick identity, $\sum_{j=m}^k \binom{j}{m} = \binom{k+1}{m+1} = \frac{k+1}{m+1} \binom{k}{m}$! Therefore, in the Taylor-shifted polynomial $Q(y) = P(y+1) = \sum_{m=0}^N q_m y^m$, a single transition simply divides $q_m$ by $m+1$!
- **Full Algebraic Derivation**:
  Let $Q^{(t)}(y) = P^{(t)}(y+1) = \sum_{m=0}^N q^{(t)}_m y^m$, where $q^{(t)}_m = \sum_{j=m}^N \binom{j}{m} p^{(t)}_j$. After one step:
  $$q^{(t+1)}_m = \sum_{j=m}^N \binom{j}{m} \sum_{k=j}^N \frac{p^{(t)}_k}{k+1} = \sum_{k=m}^N \frac{p^{(t)}_k}{k+1} \sum_{j=m}^k \binom{j}{m} = \sum_{k=m}^N \frac{p^{(t)}_k}{k+1} \binom{k+1}{m+1} = \frac{1}{m+1} \sum_{k=m}^N \binom{k}{m} p^{(t)}_k = \frac{q^{(t)}_m}{m+1}$$
  Thus $M$ transitions act diagonally in the Taylor-shifted basis! The entire algorithm is:
  1. Compute $Q^{(0)}(y) = P^{(0)}(y+1)$ via **1 Taylor shift** by $+1$ ($O(N \log N)$).
  2. Multiply each coefficient $q_m$ by $(m+1)^{-M} \bmod 998244353$ ($O(N \log M)$).
  3. Recover $P^{(M)}(x) = Q^{(M)}(x-1)$ via **1 Taylor shift** by $-1$ ($O(N \log N)$). Total time: $O(N \log N)$.

##### Problem 3 (`Stepping Stone` — Iter 11): Codeforces 993E — Nikita and Order Statistics (`C1` / `C2-New`)
- **Link**: <https://codeforces.com/problemset/problem/993/E>
- **Mathematical Statement**: Given an array $a_1, a_2, \dots, a_n$ ($1 \le n \le 2 \times 10^5$) and a threshold $x$, for every integer $k \in \{0, 1, \dots, n\}$, count the number of contiguous subarrays $a[l..r]$ ($1 \le l \le r \le n$) that contain **strictly fewer** than $x$ elements exactly $k$ times.
- **Diagnostic Signal**: Prefix-sum difference enumeration $S_r - S_{l-1} = k$ reduces to the exact reversed-index cross-correlation $\sum_{v=0}^{n-k} c_{v+k} c_v$ used in the Taylor shift kernel!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Replace each $a_i$ by $b_i = [a_i < x] \in \{0, 1\}$ and form the prefix sums $S_0, S_1, \dots, S_n$ where $S_r = \sum_{i=1}^r b_i$. A subarray $a[l..r]$ has $k$ elements $< x$ iff $S_r - S_{l-1} = k$.
  - *Hint 2*: Let $c_v$ be the frequency of value $v$ among $S_0, S_1, \dots, S_n$. For $k = 0$, the answer is $\sum_{v=0}^n \binom{c_v}{2}$; for $k \ge 1$, the answer is the cross-correlation $\sum_{v=0}^{n-k} c_{v+k} c_v$.
  - *Hint 3*: Reverse the second copy into $\tilde{c}_{n-v} = c_v$ so that $\sum_{v=0}^{n-k} c_{v+k} \tilde{c}_{n-v} = [z^{n+k}]\left(\sum_u c_u z^u\right)\left(\sum_w \tilde{c}_w z^w\right)$, and compute all $k \ge 1$ in one FFT of length $2n$ over $\mathbb{C}$ (or 64-bit 2-prime NTT).
- **Full Algebraic Derivation**:
  Let $S_0 = 0$ and $S_r = \sum_{i=1}^r [a_i < x]$ for $1 \le r \le n$, and let $c_v = |\{r \in \{0, \dots, n\} : S_r = v\}|$ for $0 \le v \le n$.
  - For $k = 0$: a pair $(l-1, r)$ with $0 \le l-1 < r \le n$ has $S_r - S_{l-1} = 0$ iff $S_r = S_{l-1} = v$, giving $\text{Ans}_0 = \sum_{v=0}^n \binom{c_v}{2}$.
  - For $1 \le k \le n$: since $S_r$ is non-decreasing, $S_r - S_{l-1} = k > 0$ automatically implies $l - 1 < r$. Define $P(z) = \sum_{u=0}^n c_u z^u$ and the reversed polynomial $Q(z) = z^n P(z^{-1}) = \sum_{v=0}^n c_v z^{n-v}$. Multiplying $P(z)$ and $Q(z)$ via FFT / 2-prime NTT gives $\text{Ans}_k = [z^{n+k}] \bigl(P(z) Q(z)\bigr)$ for all $1 \le k \le n$ in $O(n \log n)$ time.

##### Problem 4 (`Intermediate` — Iter 11): KUPC 2019 K — One or All (`C1`)
- **Link**: <https://atcoder.jp/contests/kupc2019/tasks/kupc2019_k>
- **Mathematical Statement**: Given integers $N, M$ ($N \le 2\times 10^5$) and conditions on subsets/operations that generate a polynomial $A(x)$ of degree $N$, evaluate all coefficients of $B(x) = \sum_{k=0}^N a_k (1+x)^k (1-x)^{N-k} \bmod 998244353$.
- **Diagnostic Signal**: Homogeneous weight $(1+x)^k (1-x)^{N-k}$ of total degree $N$ is the exact Krawtchouk / Projective Möbius Transform $(\mathcal{M}_g A)(x) = (1-x)^N A\!\left(\frac{1+x}{1-x}\right)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Factor the rational substitution $\frac{1+x}{1-x} = -1 + \frac{2}{1-x}$.
  - *Hint 2*: Apply the Bruhat decomposition: shift $A_1(y) = A(y-1)$, scale and reverse $A_2(y) = y^N A_1(2/y)$, and shift $B(x) = A_2(1-x)$.
  - *Hint 3*: Each Taylor shift takes 1 NTT multiplication of size $2N$.
- **Full Algebraic Derivation**:
  Write $(1-x)^N A\!\left(\frac{1+x}{1-x}\right) = (1-x)^N A_1\!\left(\frac{2}{1-x}\right)$ where $A_1(y) = A(y-1)$. Letting $A_2(z) = \sum_{k=0}^N [y^k]A_1(y) \cdot 2^k z^{N-k}$, we have $B(x) = A_2(1-x) = \tilde{A}_2(x-1)$ where $\tilde{A}_2(w) = A_2(-w)$. Total complexity: 2 Taylor shifts = $O(N \log N)$.

##### Problem 5 (`Intermediate` — Iter 11): Codeforces 1251F — Red-White Fence (`C1` / `C2-New`)
- **Link**: <https://codeforces.com/problemset/problem/1251/F>
- **Mathematical Statement**: You have $n$ white boards of lengths $a_1, \dots, a_n$ ($1 \le n \le 3 \times 10^5$, $1 \le a_i \le 3 \times 10^5$) and $k$ red boards of distinct lengths $b_1, \dots, b_k$ ($1 \le k \le 5$). To build a valid fence, you choose exactly one red board $b_j$ and a subset of white boards of lengths strictly less than $b_j$, arrange them in strictly increasing then strictly decreasing order around $b_j$, and color boards of the same length on the same side identically. Given $q \le 3 \times 10^5$ queries of perimeter $Q_i$, find the number of valid fences for each query modulo $998244353$.
- **Diagnostic Signal**: Product of shifted linear binomials $(1 + 2x)^{c_1} (1 + x)^{2c_2}$ where $(1 + 2x + x^2) = (1+x)^2$ collapses quadratic factors into linear powers!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Fix one of the $k \le 5$ red boards of length $B$. Only white boards of length $v < B$ can be used, and at most $2$ boards of each length $v$ can be placed (at most one on the left of $B$, at most one on the right of $B$).
  - *Hint 2*: If length $v < B$ appears $\text{cnt}[v] = 1$ time, its contribution to the number of boards chosen is $1 + 2x$. If $\text{cnt}[v] \ge 2$, its contribution is $1 + 2x + x^2 = (1 + x)^2$.
  - *Hint 3*: For each of the $k \le 5$ red boards, count $c_1 = |\{v < B : \text{cnt}[v] = 1\}|$ and $c_2 = |\{v < B : \text{cnt}[v] \ge 2\}|$, expand $(1 + 2x)^{c_1}$ and $(1 + x)^{2c_2}$ via the binomial theorem, multiply them via NTT in $O(n \log n)$ time, and answer each perimeter query $Q_i = 2(B + m + 1)$ in $O(k)$ time.
- **Full Algebraic Derivation**:
  Adding $m$ white boards to a red board of height $B$ creates a fence of perimeter $2(B + m + 1)$. For a fixed red board $B$, let $c_1 = |\{v < B : \text{cnt}[v] = 1\}|$ and $c_2 = |\{v < B : \text{cnt}[v] \ge 2\}|$. The generating function for choosing $m$ white boards around red board $B$ is:
  $$F_B(x) = (1 + 2x)^{c_1} (1 + x)^{2c_2} = \left(\sum_{i=0}^{c_1} \binom{c_1}{i} 2^i x^i\right) \left(\sum_{j=0}^{2c_2} \binom{2c_2}{j} x^j\right)$$
  Since $k \le 5$, we compute $F_B(x)$ for each of the $k$ red boards using a single NTT multiplication of degree $\le 2n$. For each query perimeter $Q$, if $Q$ is even, we sum $[x^{Q/2 - B - 1}] F_B(x)$ over all $k$ red boards $B$ in $O(k n \log n + q k)$ total time.

##### Problem 6 (`Intermediate` — Iter 11): AtCoder AGC 005 F — Many Easy Problems (`C2-New` / `C2-Pre`)
- **Link**: <https://atcoder.jp/contests/agc005/tasks/agc005_f>
- **Mathematical Statement**: Given a tree $T$ with $n$ vertices ($2 \le n \le 2 \times 10^5$), for a subset $S \subseteq V(T)$ of size $k$, let $f(S)$ be the number of vertices in the minimal connected subtree of $T$ spanning $S$. For every $k = 1, 2, \dots, n$, compute the sum of $f(S)$ over all $\binom{n}{k}$ subsets $S$ of size $k$, modulo $924844033$ ($= 2^{21} \times 441 + 1$, primitive root $g = 5$).
- **Diagnostic Signal**: Counting subsets per vertex reduces to $\text{Ans}_k = n\binom{n}{k} - \sum_{m=k}^{n-1} c_m \binom{m}{k} = n\binom{n}{k} - [x^k] \sum_{m=0}^{n-1} c_m (1+x)^m$, which is a Taylor shift $\sum_{m=0}^{n-1} c_m (1+x)^m$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: By linearity of expectation/counting, count how many subsets $S$ of size $k$ include a given vertex $v$ in their minimal spanning subtree.
  - *Hint 2*: Vertex $v$ is **not** in the minimal subtree spanning $S$ iff $S$ is entirely contained within one of the connected components formed when $v$ is deleted from $T$. Across all $v \in V(T)$, the component sizes of $T \setminus \{v\}$ are precisely $s_u$ and $n - s_u$ for each of the $n - 1$ non-root vertices $u$.
  - *Hint 3*: Let $c_m$ be the frequency of component size $m$. Then $\text{Ans}_k = n \binom{n}{k} - \sum_{m=k}^{n-1} c_m \binom{m}{k} = n \binom{n}{k} - \frac{1}{k!} \sum_{m=k}^{n-1} \frac{(c_m m!)}{(m - k)!}$, which is a single reversed Taylor-shift convolution modulo $924844033$.
- **Full Algebraic Derivation**:
  Root the tree arbitrarily and compute subtree sizes $s_u$ for all $u \neq \text{root}$ in $O(n)$ time. Let $c_m$ ($1 \le m < n$) be the frequency of size $m$ in the multiset $\{s_u, n - s_u : u \neq \text{root}\}$. Summing over all $v \in V(T)$:
  $$\text{Ans}_k = n \binom{n}{k} - \sum_{m=k}^{n-1} c_m \binom{m}{k} = n \binom{n}{k} - \frac{1}{k!} \sum_{m=k}^{n-1} (c_m m!) \cdot \frac{1}{(m - k)!}$$
  Define $A_m = c_m m!$ (with $A_n = 0$), reverse $A$ into $\tilde{A}_{n-m} = A_m$, and let $B_j = \frac{1}{j!}$. Convolving $\tilde{A}$ and $B$ via NTT modulo $924844033$ gives $\sum_{m=k}^{n-1} A_m B_{m-k} = [x^{n-k}](\tilde{A}(x) B(x))$ for all $1 \le k \le n$ in $O(n \log n)$ time.

##### Problem 7 (`Intermediate` — Iter 11): Codeforces 1548C — The Three Little Pigs (`C2-New` / `C2-Pre`)
- **Link**: <https://codeforces.com/problemset/problem/1548/C>
- **Mathematical Statement**: Given $n \le 10^6$ and $q \le 2 \times 10^5$ queries $x$ ($1 \le x \le 3n$), compute $\sum_{i=1}^n \binom{3i}{x} \bmod (10^9 + 7)$ for each query $x$.
- **Diagnostic Signal**: Extracting $[t^x] \sum_{i=1}^n (1+t)^{3i}$ via the shifted geometric series $\frac{(1+t)^{3n+3} - 1}{(1+t)^3 - 1}$ and $O(n)$ synthetic polynomial division!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Notice that $\binom{3i}{x} = [t^x] (1 + t)^{3i}$, so the query asks for $[t^x] \sum_{i=1}^n (1 + t)^{3i}$.
  - *Hint 2*: Sum the finite geometric series in powers of $(1 + t)^3$: $\sum_{i=0}^n (1 + t)^{3i} = \frac{(1 + t)^{3n + 3} - 1}{(1 + t)^3 - 1}$.
  - *Hint 3*: Expand the denominator $(1 + t)^3 - 1 = t(t^2 + 3t + 3)$ and perform synthetic polynomial long division on the numerator $(1 + t)^{3n+3} - 1$ in $O(n)$ time!
- **Full Algebraic Derivation**:
  Include $i = 0$ (which adds $[x = 0]$) and sum the geometric progression:
  $$P(t) = \sum_{i=0}^n (1 + t)^{3i} = \frac{(1 + t)^{3n+3} - 1}{(1 + t)^3 - 1} = \frac{\sum_{k=1}^{3n+3} \binom{3n+3}{k} t^k}{t^3 + 3t^2 + 3t} = \frac{\sum_{k=0}^{3n+2} \binom{3n+3}{k+1} t^k}{t^2 + 3t + 3}$$
  Comparing coefficients of $(t^2 + 3t + 3) \sum_{x=0}^{3n} p_x t^x = \sum_{k=0}^{3n+2} \binom{3n+3}{k+1} t^k$ from lowest degree gives the $O(1)$-per-step linear recurrence:
  $$p_0 = n + 1, \qquad p_1 = \frac{\binom{3n+3}{2} - 3 p_0}{3}, \qquad p_x = \frac{\binom{3n+3}{x+1} - 3 p_{x-1} - p_{x-2}}{3} \quad (2 \le x \le 3n)$$
  Precomputing $p_0, \dots, p_{3n}$ takes $O(n)$ time and answers each query $x \ge 1$ in $O(1)$ time.

##### Problem 8 (`Intermediate` — Iter 11): AtCoder ABC 300 Ex — Fibonacci: Revisited (`C2-New`)
- **Link**: <https://atcoder.jp/contests/abc300/tasks/abc300_h>
- **Mathematical Statement**: Define $a_n = 1$ for $0 \le n < K$ and $a_n = \sum_{i=1}^K a_{n-i}$ for $n \ge K$. Given $K \le 5 \times 10^4$ and $N \le 10^{18}$, compute $\sum_{m \text{ AND } N = m} a_m \bmod 998244353$ (the sum of $a_m$ over all non-negative integers $m$ whose binary representation is a submask of $N$), as well as the single term $a_N \bmod 998244353$.
- **Diagnostic Signal**: Rational OGF $F(x) = \frac{P(x)}{Q(x)}$ with $Q(x) = 1 - x - \dots - x^K = \frac{1 - 2x + x^{K+1}}{1 - x}$ combined with a **Submask-Sum Bostan–Mori** even/odd substitution $x^2 \mapsto y$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: The OGF of $(a_n)$ is $F(x) = \frac{P(x)}{Q(x)}$ where $Q(x) = 1 - x - x^2 - \dots - x^K = \frac{1 - 2x + x^{K+1}}{1 - x}$ and $P(x) = \left(Q(x) \sum_{n=0}^{K-1} x^n\right) \bmod x^K = 1 - \sum_{n=1}^{K-1}(n-1)x^n$ (or $\frac{1 - x^K}{1 - 2x + x^{K+1}}$ after clearing $1 - x$).
  - *Hint 2*: Consider the Bostan–Mori step $F(x) = \frac{P(x)Q(-x)}{Q(x)Q(-x)} = \frac{U_0(x^2) + x U_1(x^2)}{V(x^2)}$. Whereas standard Bostan–Mori keeps only the parity bit $N \bmod 2$, summing over all submasks $m \subseteq N$ means that if the lowest bit of $N$ is $0$, we must take the even part $U_0(y)$, whereas if the lowest bit of $N$ is $1$, we can choose *either* bit $0$ or bit $1$ for $m$, which sums $U_0(y) + U_1(y)$!
  - *Hint 3*: Thus at each of the $\lceil \log_2 N \rceil$ halving steps, update $P \leftarrow U_0$ if $N$ is even, or $P \leftarrow U_0 + U_1$ if $N$ is odd, and $Q \leftarrow V$.
- **Full Algebraic Derivation**:
  1. **Rational Generating Function**:
     Since $a_n = 1$ ($0 \le n < K$) and $a_n = \sum_{i=1}^K a_{n-i}$ ($n \ge K$), we have $Q(x) = 1 - \sum_{i=1}^K x^i$ and $P(x) = 1 - \sum_{n=1}^{K-1} (n - 1) x^n$. (Also note that multiplying top and bottom by $1 - x$ compresses $F(x) = \frac{1 - x^K}{1 - 2x + x^{K+1}}$, so for $N$ up to $O(K^2)$ one can even expand $(1 - 2x + x^{K+1})^{-1} = \sum_{j \ge 0} (-1)^j \frac{x^{j(K+1)}}{(1-2x)^{j+1}}$ in $O(N/K)$ terms!)
  2. **Submask-Sum Bostan–Mori Recursion**:
     Let $S(N) = \{m \ge 0 : (m \text{ AND } N) = m\}$ be the set of submasks of $N$. If $N = 2N'$ is even, every $m \in S(N)$ is $2m'$ ($m' \in S(N')$); if $N = 2N' + 1$ is odd, every $m \in S(N)$ is either $2m'$ or $2m' + 1$ ($m' \in S(N')$). Writing $P(x)Q(-x) = U_0(x^2) + x U_1(x^2)$ and $V(x^2) = Q(x)Q(-x)$ gives:
     $$\sum_{m \in S(N)} [x^m] \frac{P(x)}{Q(x)} = \sum_{m' \in S(\lfloor N/2 \rfloor)} [y^{m'}] \frac{\widetilde{P}(y)}{V(y)}, \quad \text{where } \widetilde{P}(y) = \begin{cases} U_0(y) & \text{if } N \equiv 0 \pmod 2, \\ U_0(y) + U_1(y) & \text{if } N \equiv 1 \pmod 2. \end{cases}$$
     When $N = 0$, the answer is $P(0) / Q(0) \bmod 998244353$. Total time complexity: $O(K \log K \log N)$ with only 2 NTTs per bit!

##### Problem 9 (`Intermediate` — Iter 11): HDU 5855 — Less Time, More Profit (`C2-New`)
- **Link**: <https://acm.hdu.edu.cn/showproblem.php?pid=5855>
- **Mathematical Statement**: A project has $N$ plants (with build times $t_i$ and costs $c_i$) and $M$ shops (each yielding profit $p_j$ when a specified subset of plants is built). Find the minimum time $T$ such that a net profit of at least $L$ can be achieved within time $T$, and maximize the net profit for that minimum time ($N, M \le 200$).
- **Diagnostic Signal**: Binary search on the time threshold $T$ combined with minimum-cut closure (and in parametric polynomial-weight variants, Taylor shift $P_i(x + \delta_i)$ aggregation).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Binary search on the time threshold $T$; for a fixed $T$, only plants with $t_i \le T$ are available, reducing the problem to Maximum Weight Closure (minimum cut).
  - *Hint 2*: In parametric / polynomial-weight variants where plant weights are shifted polynomials $P_i(x + \delta_i)$, aggregate the shifted polynomials via Taylor shift before evaluating the cut capacity.
  - *Hint 3*: Run Dinic's algorithm on the bipartite closure network for each binary search midpoint.
- **Full Algebraic Derivation**:
  Sort the plants by build time $t_i$ and binary search on the index of the maximum build time $T$. For a fixed threshold $T$, construct a flow network where the source $S$ connects to each satisfied shop $j$ (all of whose required plants have $t_i \le T$) with capacity $p_j$, each shop $j$ connects to its required plants with capacity $\infty$, and each available plant $i$ connects to the sink $K$ with capacity $c_i$. By the Picard–Queyranne closure theorem, the maximum net profit achievable within time $T$ is $\sum_{j \text{ valid}} p_j - \text{MinCut}(S, K)$, evaluated in $O(\log N \cdot \text{MaxFlow}(N+M, NM))$ time.

##### Problem 10 (`Intermediate` — Iter 11): Project Euler 755 — Not Zeckendorf (`C2-New`)
- **Link**: <https://projecteuler.net/problem=755>
- **Mathematical Statement**: Let $f(n)$ be the number of ways to write $n$ as a sum of distinct Fibonacci numbers $F_1 = 1, F_2 = 2, F_3 = 3, F_4 = 5, \dots$. Compute $S(N) = \sum_{n=0}^N f(n)$ for $N = 10^{13}$.
- **Diagnostic Signal**: Prefix sum of subset-sum polynomial $S(N) = [x \le N] \prod_{k=1}^m (1 + x^{F_k})$ where the exponential growth of $F_k$ collapses branches whenever $R \ge \sum_{i=1}^k F_i = F_{k+2} - 2$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: In generating function terms, $S(N) = \sum_{n=0}^N [x^n] \prod_{k=1}^m (1 + x^{F_k})$.
  - *Hint 2*: Use the identity $\sum_{i=1}^k F_i = F_{k+2} - 2$. If $F_{k+2} - 2 \le R$, then *every* subset of $\{F_1, \dots, F_k\}$ has sum $\le R$, contributing $2^k$ immediately!
  - *Hint 3*: Recurse from the largest Fibonacci number $F_k \le N$ downward, pruning whenever the remaining maximum possible sum $F_{k+2} - 2$ is at most the remaining capacity $R$.
- **Full Algebraic Derivation**:
  Define $G(k, R) = \sum_{n=0}^R [x^n] \prod_{i=1}^k (1 + x^{F_i})$. We have three cases:
  1. If $R < 0$, then $G(k, R) = 0$.
  2. If $R \ge \sum_{i=1}^k F_i = F_{k+2} - 2$, then every subset of $\{F_1, \dots, F_k\}$ sums to at most $R$, so $G(k, R) = 2^k$ in $O(1)$ time!
  3. Otherwise, branch on whether $F_k$ is included: $G(k, R) = G(k-1, R) + G(k-1, R - F_k)$.
  Because $F_k + (F_{k+1} - 2) = F_{k+2} - 2$, in Case 3 where $F_k \le R < F_{k+2} - 2$, at least one of the two recursive branches ($R$ or $R - F_k$) is guaranteed to trigger the $2^{k-1}$ pruning within at most two steps. For $N = 10^{13}$ ($m = 62$), memoized recursion visits fewer than $10^4$ states and finishes in under $1\text{ ms}$.

##### Problem 11 (`Advanced` — Iter 11): AtCoder ARC 136 F — Flip Cells (`C2-Pre`)
- **Link**: <https://atcoder.jp/contests/arc136/tasks/arc136_f>
- **Mathematical Statement**: Given an $H \times W$ binary grid ($H \le 50, W \le 50$, total cells $N = HW \le 2500$ or general $N \le 2.5\times 10^5$ in 1D spin-flip variants) with initial row-sum and state constraints, at each step one cell is chosen uniformly at random and flipped. Find the expected number of steps until a target condition is met modulo $998244353$.
- **Diagnostic Signal**: Uniformly flipping 1 of $N$ bits acts on the EGF $\sum_k c_k (e^{z/N} - e^{-z/N})^k (e^{z/N} + e^{-z/N})^{N-k}$, whose coefficient extraction is the **Krawtchouk Transform** $(1+x)^N F\!\left(\frac{1-x}{1+x}\right)$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: A single random bit flip multiplies the eigenfunction $(-1)^{\langle v, s \rangle}$ (where $|v| = k$) by the eigenvalue $\lambda_k = \frac{N - 2k}{N}$.
  - *Hint 2*: Passing between the Hamming-weight generating function $F(x) = \sum_{k=0}^N f_k x^k$ and the eigenvalue generating function $G(x) = \sum_{m=0}^N g_m x^m$ (where $g_m$ collects coefficients of $(1-x)^k(1+x)^{N-k}$) is the Krawtchouk Transform $G(x) = (1+x)^N F\!\left(\frac{1-x}{1+x}\right)$.
  - *Hint 3*: Once $g_m$ is obtained via 2 Taylor shifts, the expected waiting time from the Markov chain fundamental matrix is $\sum_{m < N} \frac{g_m}{1 - \lambda_m}$, using the standard Stopping-Time Lemma $E[T] = \frac{H'(1) - G'(1)}{G(1)}$.
- **Full Algebraic Derivation**:
  Let $F(x) = \sum_{k=0}^N f_k x^k$ count valid configurations at Hamming distance $k$. The EGF of $t$-step transitions is $\widehat{A}(z) = \sum_{k=0}^N f_k \left(\frac{e^{z/N}-e^{-z/N}}{2}\right)^k \left(\frac{e^{z/N}+e^{-z/N}}{2}\right)^{N-k} = 2^{-N} e^{-z} \sum_{m=0}^N g_m e^{2mz/N}$, where $\sum_{m=0}^N g_m x^m = (1+x)^N F\!\left(\frac{x-1}{x+1}\right)$ is computed in $O(N \log N)$ via Bruhat decomposition. Applying the formal Laplace transform maps $e^{(2m/N - 1)z} \mapsto \frac{1}{1 - \frac{2m-N}{N} t}$, from which $E[T]$ is extracted in $O(N)$.

##### Problem 12 (`Advanced` — Iter 11): Codeforces 1349D — Slime and Biscuits (`C2-Pre`)
- **Link**: <https://codeforces.com/problemset/problem/1349/D>
- **Mathematical Statement**: There are $n$ players ($n \le 10^5$) holding $a_1, \dots, a_n$ biscuits ($\sum a_i = S \le 3\times 10^5$). At each step, one biscuit is chosen uniformly at random among all $S$ biscuits and transferred to one of the other $n-1$ players chosen uniformly at random. Find the expected number of steps until a single player holds all $S$ biscuits, modulo $998244353$.
- **Diagnostic Signal**: In the EGF/Krawtchouk approach to this multi-urn Ehrenfest chain, the transition generates products of $(1 + (n-1)x)^{a_i} (1-x)^{S-a_i}$, which is a generalized Möbius transform $(1-x)^S F\!\left(\frac{1+(n-1)x}{1-x}\right)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Either construct a potential function $\phi(a_1, \dots, a_n)$ where $\sum_{i=1}^n (\phi(a_i^{(t+1)}) - \phi(a_i^{(t)})) = -1$ via a tridiagonal recurrence on $0 \le k \le S$, **or** diagonalize the Ehrenfest transition operator via the generalized Krawtchouk basis $(1 + (n-1)x)^k (1-x)^{S-k}$.
  - *Hint 2*: In the Möbius / Krawtchouk view, let $F(y) = \sum_{i=1}^n y^{a_i}$. The eigenvalue projection polynomial is $(1-x)^S F\!\left(\frac{1+(n-1)x}{1-x}\right)$.
  - *Hint 3*: Applying the Bruhat decomposition $\frac{1+(n-1)x}{1-x} = -(n-1) + \frac{n}{1-x}$ computes all eigenvalue weights in $O(S \log S)$ time (or $O(S)$ via the tridiagonal potential recurrence).
- **Full Algebraic Derivation**:
  In the Krawtchouk eigenbasis $K_m(k; S, n) = [x^m](1+(n-1)x)^k (1-x)^{S-k}$, each step multiplies $K_m$ by the eigenvalue $\lambda_m = 1 - \frac{mn}{S(n-1)}$. Summing over all $n$ players gives the generating function $G(x) = \sum_{i=1}^n (1+(n-1)x)^{a_i}(1-x)^{S-a_i} = (1-x)^S F\!\left(\frac{1+(n-1)x}{1-x}\right)$ where $F(y) = \sum_{i=1}^n y^{a_i}$. By Bruhat decomposition, $G(x)$ is computed in 2 Taylor shifts in $O(S \log S)$ time, and summing $\frac{[x^m](G(x) - G_{\text{target}}(x))}{1 - \lambda_m}$ for $m \ge 1$ yields the exact expected stopping time.

##### Problem 13 (`Mastery` — Iter 11): AtCoder ABC 222 H — Beautiful Binary Tree (`C1`)
- **Link**: <https://atcoder.jp/contests/abc222/tasks/abc222_h>
- **Mathematical Statement**: Count the number of labeled rooted trees or valid "beautiful binary trees" of size $N$ ($N \le 10^7$) whose generating function satisfies $F(x) = x(1 + F(x) + F(x)^2)^2$ (or equivalent polynomial functional equation $F = x \phi(F)$ where $\phi(u) = (1 + 3u + u^2)^2$), and extract $[x^N] F(x) \bmod 998244353$.
- **Diagnostic Signal**: Non-linear composition $F(x) = x \phi(F(x))$ where $\phi(u) = (1 + 3u + u^2)^2$: apply the Lagrange form of our Residue Engine $[x^N] F(x) = \frac{1}{N} [u^{N-1}] (1 + 3u + u^2)^{2N}$, then reduce the trinomial power via a **rational / binomial substitution**!
- **3-Tier Progressive Hints**:
  - *Hint 1*: By the Residue Change-of-Variables Engine ($u = F(x) \implies x = \frac{u}{\phi(u)}$), we need $\frac{1}{N} [u^{N-1}] (1 + 3u + u^2)^{2N}$.
  - *Hint 2*: How do we compute $[u^{N-1}] (1 + 3u + u^2)^{2N}$ in $O(N)$ time when $N = 10^7$? Rewrite the trinomial by completing the square: $1 + 3u + u^2 = (1+u)^2 + u$!
  - *Hint 3*: Expand $((1+u)^2 + u)^{2N} = \sum_{k=0}^{2N} \binom{2N}{k} u^k (1+u)^{2(2N-k)}$. Now extracting $[u^{N-1}]$ is a single $O(N)$ summation $\sum_{k=0}^{N-1} \binom{2N}{k} \binom{4N-2k}{N-1-k}$!
- **Full Algebraic Derivation**:
  The tree grammar yields $F(x) = x(1 + 3F(x) + F(x)^2)^2$ (after substituting the two node states). Setting $u = F(x)$, the Residue Engine gives:
  $$[x^N] F(x) = \frac{1}{N} [u^{N-1}] (1 + 3u + u^2)^{2N} = \frac{1}{N} [u^{N-1}] \big((1+u)^2 + u\big)^{2N} = \frac{1}{N} \sum_{k=0}^{N-1} \binom{2N}{k} [u^{N-1-k}] (1+u)^{4N-2k} = \frac{1}{N} \sum_{k=0}^{N-1} \binom{2N}{k} \binom{4N-2k}{N-1-k}$$
  This runs in $O(N)$ time and $O(1)$ extra space beyond factorials up to $4N$, easily passing for $N = 10^7$!

---

#### Module B: Iteration 12 / 64 — Quadratic Radicals, Catalan, Motzkin, Delannoy, Schröder & Chebyshev (Problems 14–21)

##### Problem 14 (`Stepping Stone` — Iter 12): Codeforces 438E — The Child and Binary Tree (`C1` / `C2-New`)
- **Link**: <https://codeforces.com/problemset/problem/438/E>
- **Mathematical Statement**: You are given a set of allowed vertex weights $c_1, c_2, \dots, c_n$ ($1 \le c_i \le 10^5$) and a maximum weight $m \le 10^5$. A rooted binary tree is good if every vertex's weight belongs to $\{c_1, \dots, c_n\}$. For each $s = 1, 2, \dots, m$, find the number of good rooted binary trees of total weight $s$, modulo $998244353$.
- **Diagnostic Signal**: Catalan-type quadratic equation $C(x) T(x)^2 - T(x) + 1 = 0$ where $[x^0] C(x) = 0$ prevents direct division by $2C(x)$, requiring **conjugate radical rationalization** $T(x) = \frac{2}{1 + \sqrt{1 - 4C(x)}}$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Let $C(x) = \sum_{i=1}^n x^{c_i}$ be the weight polynomial and $T(x) = \sum_{s \ge 0} t_s x^s$ be the generating function of good binary trees. A non-empty binary tree consists of a root in $C$ and two (possibly empty) subtrees, giving $T(x) = 1 + C(x) T(x)^2$.
  - *Hint 2*: Solving the quadratic equation $C(x) T(x)^2 - T(x) + 1 = 0$ gives $T(x) = \frac{1 - \sqrt{1 - 4C(x)}}{2C(x)}$, which cannot be divided directly because $[x^0] C(x) = 0$.
  - *Hint 3*: Rationalize the numerator by multiplying top and bottom by $1 + \sqrt{1 - 4C(x)}$ to obtain $T(x) = \frac{2}{1 + \sqrt{1 - 4C(x)}}$, whose denominator has constant term $2 \not\equiv 0 \pmod{998244353}$!
- **Full Algebraic Derivation**:
  From the structural specification $\mathcal{T} = \{\epsilon\} + \mathcal{C} \times \mathcal{T} \times \mathcal{T}$, the OGF $T(x)$ satisfies $C(x) T(x)^2 - T(x) + 1 = 0$. Selecting the minus branch ($T(0) = 1$) and rationalizing the numerator:
  $$T(x) = \frac{1 - \sqrt{1 - 4C(x)}}{2C(x)} = \frac{(1 - \sqrt{1 - 4C(x)})(1 + \sqrt{1 - 4C(x)})}{2C(x)(1 + \sqrt{1 - 4C(x)})} = \frac{2}{1 + \sqrt{1 - 4C(x)}}$$
  Since $[x^0]\sqrt{1 - 4C(x)} = 1$, we compute $S(x) = \sqrt{1 - 4C(x)} \bmod x^{m+1}$ via polynomial square root (`poly_sqrt`) and then $T(x) = 2 (1 + S(x))^{-1} \bmod x^{m+1}$ via `poly_inv` in $O(m \log m)$ total time.

##### Problem 15 (`Stepping Stone` — Iter 12): LibreOJ #6261 — Catalan Radical Convolution (`C2-Pre`)
- **Link**: <https://loj.ac/p/6261>
- **Mathematical Statement**: Given a polynomial $A(x) = \sum_{k=0}^n a_k x^k$ of degree $n \le 10^5$, compute the first $n+1$ coefficients of $G_1(x) = A\!\left(\frac{1 - 2x - \sqrt{1 - 4x}}{2x}\right)$, $G_2(x) = A\!\left(\frac{1 - \sqrt{1 - 4x}}{2}\right)$, or $G_3(x) = \frac{A(C(x) - 1)}{\sqrt{1-4x}} \bmod 998244353$, where $C(x) = \frac{1-\sqrt{1-4x}}{2x}$ is the Catalan generating function.
- **Diagnostic Signal**: Explicit occurrence of $C(x) - 1 = \frac{1-2x-\sqrt{1-4x}}{2x}$, $xC(x) = \frac{1-\sqrt{1-4x}}{2}$, and $\frac{1}{\sqrt{1-4x}}$—the exact setups of **Catalan Substitution I & II** and **Master Formulas A & B**!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Notice that $u(x) = C(x) - 1 = \frac{1 - 2x - \sqrt{1 - 4x}}{2x}$ satisfies $x = \frac{u}{(1+u)^2}$ and $\sqrt{1-4x} = \frac{1-u}{1+u}$, while $v(x) = xC(x) = \frac{1 - \sqrt{1 - 4x}}{2}$ satisfies $x = v(1-v)$.
  - *Hint 2*: Apply Lagrange Inversion (Master Formula A for $G_3(x)$, Master Formula B for $G_1(x)$, or $\phi(v) = (1-v)^{-1}$ for $G_2(x)$) to express $[x^m]$ in closed binomial form.
  - *Hint 3*: To compute $[x^m]$ for all $0 \le m \le n$ simultaneously, compute $u(x)$ or $v(x) \bmod x^{n+1}$ via a single `poly_sqrt` in $O(n \log n)$ and apply polynomial composition $A(u(x)) \bmod x^{n+1}$ in $O(n \log^2 n)$ time!
- **Full Algebraic Derivation**:
  - **Variant 1 ($u(x) = C(x) - 1 = \frac{1 - 2x - \sqrt{1 - 4x}}{2x}$, where $x = \frac{u}{(1+u)^2}$)**:
    By Master Formula B (Section 4.1), for each $1 \le m \le n$:
    $$[x^m] A(u(x)) = [u^m] A(u)(1 - u^2)(1 + u)^{2m-2} = \sum_{k=1}^m a_k \frac{k}{m} \binom{2m}{m - k}, \qquad [x^0] A(u(x)) = a_0$$
    And with the radical weight $\frac{1}{\sqrt{1-4x}}$, Master Formula A gives $[x^m] \frac{A(u(x))}{\sqrt{1-4x}} = [u^m] A(u)(1+u)^{2m} = \sum_{k=0}^m a_k \binom{2m}{m-k}$.
  - **Variant 2 ($v(x) = xC(x) = \frac{1 - \sqrt{1 - 4x}}{2}$, where $x = v(1-v)$)**:
    By Lagrange Inversion with $\phi(v) = (1 - v)^{-1}$, $[x^m] v(x)^k = \frac{k}{m} [v^{m-k}] (1 - v)^{-m} = \frac{k}{m} \binom{2m - k - 1}{m - k}$, so for $m \ge 1$:
    $$[x^m] A(v(x)) = \sum_{k=1}^m a_k \frac{k}{m} \binom{2m - k - 1}{m - k}, \qquad [x^0] A(v(x)) = a_0$$
  - **Computing All Coefficients $0 \le m \le n$**:
    For a single target $m = n$, either formula above runs in $O(n)$ time. To compute $[x^m]$ for *all* $0 \le m \le n$ simultaneously, compute $u(x) \bmod x^{n+1}$ via `poly_sqrt` in $O(n \log n)$ and apply Kinoshita–Li Bostan–Mori composition (or D&C binary splitting on $x = \frac{u}{(1+u)^2}$) in $O(n \log^2 n)$ time.

##### Problem 16 (`Intermediate` — Iter 12): Codeforces GYM 102978 H — Motzkin Paths with Colored Peaks (`C2-Pre`)
- **Link**: <https://codeforces.com/gym/102978/problem/H>
- **Mathematical Statement**: Count generalized Motzkin paths of length $n$ ($n \le 2\times 10^5$) where up-steps $(1,1)$, level-steps $(1,0)$, and down-steps $(1,-1)$ have weights $1, a, b$, and the path may be concatenated with a given boundary polynomial $P(M(x))$ of degree $\le n$. Output the answer modulo $998244353$.
- **Diagnostic Signal**: Weighted Motzkin functional equation $M(x) = 1 + ax M(x) + bx^2 M(x)^2$, which rationalizes under $u = x M(x) \implies x = \frac{u}{1 + au + bu^2}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Set $u = x M(x)$, so $u = x(1 + au + bu^2) \iff x = \frac{u}{1 + au + bu^2}$ and $M(x) = \frac{u}{x} = 1 + au + bu^2$.
  - *Hint 2*: Apply Master Formula B to extract $[x^n] P(M(x))$ or $[x^n] H(u)$: $[x^n] H(u(x)) = [u^n] H(u) (1 - bu^2) (1 + au + bu^2)^{n-1}$.
  - *Hint 3*: Compute $(1 + au + bu^2)^{n-1} \bmod u^{n+1}$ in $O(n \log n)$ (or in $O(n)$ via the differential recurrence of $(1+au+bu^2)^{n-1}$!) and take the inner product with $H(u)(1-bu^2)$.
- **Full Algebraic Derivation**:
  Under $x = \frac{u}{1+au+bu^2}$, we have $\frac{dx}{du} = \frac{1-bu^2}{(1+au+bu^2)^2}$ and $\frac{u}{x} = 1 + au + bu^2$. For any boundary series $G(x) = H(u)$:
  $$[x^n] G(x) = [u^n] H(u) (1 - bu^2) (1 + au + bu^2)^{n-1}$$
  Since $T(u) = (1 + au + bu^2)^{n-1}$ satisfies $(1 + au + bu^2) T'(u) = (n-1)(a + 2bu) T(u)$, all coefficients $[u^k]T(u)$ for $0 \le k \le n$ can be computed in **$O(n)$ time** via a 3-term linear recurrence, after which $[u^n] H(u)(1-bu^2)T(u)$ is a single $O(n)$ dot product!

##### Problem 17 (`Intermediate` — Iter 12): LibreOJ #6077 — Schröder & Delannoy Path Convolution (`C2-Pre`)
- **Link**: <https://loj.ac/p/6077>
- **Mathematical Statement**: Given $n, k \le 10^5$, compute the number of $k$-tuples of Large Schröder paths of total semilength $n$, i.e., $[x^n] S(x)^k \bmod 998244353$, where $S(x) = \frac{1 - x - \sqrt{1 - 6x + x^2}}{2x}$.
- **Diagnostic Signal**: Radical $\sqrt{1 - 6x + x^2}$ ($a = 3, b = 1 \implies c = \frac{9-1}{4} = 2$), which factors linearly under $x = \frac{u}{(1+u)(1+2u)}$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Substitute $x = \frac{u}{1 + 3u + 2u^2} = \frac{u}{(1+u)(1+2u)}$.
  - *Hint 2*: Verify that $\sqrt{1 - 6x + x^2} = \frac{1 - 2u^2}{(1+u)(1+2u)}$ and therefore $S(x(u)) = 1 + 2u$.
  - *Hint 3*: Apply Master Formula B to $G(x) = S(x)^k = (1+2u)^k$: $[x^n] S(x)^k = [u^n] (1 - 2u^2)(1+u)^{n-1}(1+2u)^{n+k-1}$, which is evaluated in $O(n)$ time!
- **Full Algebraic Derivation**:
  By Master Formula B with $H(u) = (1+2u)^k$ and $c = 2$:
  $$[x^n] S(x)^k = [u^n] (1+2u)^k (1 - 2u^2) (1+u)^{n-1} (1+2u)^{n-1} = [u^n] (1 - 2u^2) (1+u)^{n-1} (1+2u)^{n+k-1}$$
  Since $[u^m] (1+u)^{n-1}(1+2u)^{n+k-1} = \sum_{j=0}^m \binom{n-1}{m-j} \binom{n+k-1}{j} 2^j$, evaluating at $m = n$ and $m = n-2$ takes $O(n)$ time!

##### Problem 18 (`Intermediate` — Iter 12): AtCoder AGC 021 E — Ball Eat Chameleons (`C2-Pre`)
- **Link**: <https://atcoder.jp/contests/agc021/tasks/agc021_e>
- **Mathematical Statement**: There are $N$ chameleons, initially all blue. You throw $K$ balls ($N, K \le 5\times 10^5$), each painted either red or blue. A chameleon turns red when it has eaten strictly more red balls than blue balls, and turns blue when it has eaten strictly more blue balls than red balls. Count the number of color sequences of length $K$ such that it is possible to distribute the $K$ balls so all $N$ chameleons end up red, modulo $998244353$.
- **Diagnostic Signal**: For a fixed number of red balls $R$ and blue balls $B = K - R$, the feasibility condition reduces to a lattice path from $(0,0)$ to $(R, B)$ staying strictly below a line $y - x \le R - N$ (or $y - x \le R - N - 1$ when $R = B$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: A chameleon can end up red with $(r, b) = (1, 0)$ (1 red ball) or with $r = b \ge 1$ if its **last** ball eaten is blue (so it turned red at $(r, r-1)$ and ate 1 extra blue ball without turning back to blue!).
  - *Hint 2*: If the total sequence has $R$ red and $B$ blue balls ($R \ge B$, and if $R = B$ the very last ball must be blue, so reduce to $(R, B-1)$), the sequence is valid iff every prefix has $b - r \le R - N$, i.e., a lattice path bounded by a single wall!
  - *Hint 3*: By the Catalan / Chebyshev reflection principle ($x = \frac{u}{(1+u)^2}$), the number of paths from $(0,0)$ to $(R, B)$ avoiding $y - x = R - N + 1$ is $\binom{R+B}{R} - \binom{R+B}{2R - N + 1}$.
- **Full Algebraic Derivation**:
  For each $R \in [\max(N, \lceil K/2 \rceil), K]$, let $B = K - R$ (if $R = B$, the last ball must be blue so we decrement $B \leftarrow B - 1$). In the Chebyshev variable $x = \frac{u}{(1+u)^2}$, the single-wall ballot OGF is $(1-u)(1+u)^{R+B}(1 - u^{R-N+1})$, whose coefficient is $\binom{R+B}{B} - \binom{R+B}{B - (R - N + 1)} = \binom{R+B}{R} - \binom{R+B}{2R - N + 1}$. Summing over all valid $R$ takes $O(K)$ time.

##### Problem 19 (`Advanced` — Iter 12): AtCoder FPS-24 V — 12 Directions (`C1` / `C2-New`)
- **Link**: <https://atcoder.jp/contests/fps-24/tasks/fps_24_v>
- **Mathematical Statement**: A piece starts at $(0, 0)$ on the 2D plane. In each of $N$ steps ($1 \le N \le 2.5 \times 10^5$), you choose an integer $i \in \{0, 1, \dots, 11\}$ and move from $(x, y)$ to $(x + \cos(30i^\circ), y + \sin(30i^\circ))$. Count the number of operation sequences that end at integer coordinates $(H, W)$ after $N$ steps ($-N \le H, W \le N$), modulo $998244353$.
- **Diagnostic Signal**: The 12 unit vectors on the clock face split into 6 **even** steps in $\frac{1}{2}\mathbb{Z} \times \frac{\sqrt{3}}{2}\mathbb{Z}$ and 6 **odd** steps in $\frac{\sqrt{3}}{2}\mathbb{Z} \times \frac{1}{2}\mathbb{Z}$. Since $1$ and $\sqrt{3}$ are linearly independent over $\mathbb{Q}$, the even and odd walks decouple completely, and adding $+2$ to the 6-step Laurent polynomial $P(x, w)$ factors it into three 1D steps under $x = pq, w = p/q$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Split the 12 step vectors into the 6 **even** directions ($i \in \{0, 2, 4, 6, 8, 10\}$) and the 6 **odd** directions ($i \in \{1, 3, 5, 7, 9, 11\}$). Since $(H, W) \in \mathbb{Z}^2$ has zero $\sqrt{3}$ component on both axes, the even steps must sum to $(H, 0)$ and the odd steps must sum to $(0, W)$ independently!
  - *Hint 2*: For the 6 even steps $P(x, w) = x^2 + x^{-2} + (x + x^{-1})(w + w^{-1})$, add $+2$ and substitute $x = pq, w = p/q$ to factor $Q(pq, p/q) = P(pq, p/q) + 2 = (pq + p^{-1}q^{-1})(p + p^{-1})(q + q^{-1})$.
  - *Hint 3*: Extracting $[p^{2H} q^{2H}] Q(pq, p/q)^n$ gives $f_n(H) = \sum_{b=0}^{n-|H|} \binom{n}{b+|H|} \binom{n}{b}^2$ (which for $H = 0$ is the Franel number $\sum_{b=0}^n \binom{n}{b}^3$!). Expand the binomial coefficients into factorials to evaluate $f_n(H)$ for all $0 \le n \le N$ via a single NTT convolution, then invert the $+2$ shift via an EGF multiplication by $e^{-2t}$!
- **Full Algebraic Derivation**:
  1. **Decoupling Even and Odd Directions over $\mathbb{Q}(\sqrt{3})$**:
     Because $1, \sqrt{3}$ are linearly independent over $\mathbb{Q}$ and $(H, W) \in \mathbb{Z}^2$, the even steps must have net displacement $(H, 0)$ and the odd steps must have net displacement $(0, W)$. By $90^\circ$ rotational symmetry, an $m$-step odd walk to $(0, W)$ is bijective to an $m$-step even walk to $(W, 0)$. Thus, if $g_n(H)$ is the number of $n$-step even walks from $(0, 0)$ to $(H, 0)$, the answer is:
     $$\text{Ans} = \sum_{n=0}^N \binom{N}{n} g_n(H) g_{N-n}(W)$$
  2. **Rotated Monomial Substitution for $g_n(H)$**:
     Representing $(\frac{a}{2}, \frac{b\sqrt{3}}{2})$ by $x^a w^b$, one even step has Laurent polynomial $P(x, w) = x^2 + x^{-2} + (x + x^{-1})(w + w^{-1}) = (x + x^{-1})(x + x^{-1} + w + w^{-1}) - 2$. Let $Q(x, w) = P(x, w) + 2$ and $f_n(H) = [x^{2H} w^0] Q(x, w)^n$. Under $x = pq, w = p/q$ ($x^{2H} w^0 = p^{2H} q^{2H}$):
     $$Q(pq, p/q) = (pq + p^{-1}q^{-1})(pq + p^{-1}q^{-1} + pq^{-1} + p^{-1}q) = (pq + p^{-1}q^{-1})(p + p^{-1})(q + q^{-1})$$
     Choosing $p^{-1}q^{-1}$ a total of $b$ times from $(pq + p^{-1}q^{-1})^n$ requires choosing $p$ and $q$ each $b + |H|$ times from $(p + p^{-1})^n$ and $(q + q^{-1})^n$, giving $f_n(H) = \sum_{b=0}^{n - |H|} \binom{n}{b + |H|} \binom{n}{b}^2$.
  3. **All-$n$ Evaluation via Factorial-Split Convolution**:
     Expanding the binomial coefficients into factorials separates $b$ and $c = n - b$:
     $$f_n(H) = \sum_{b=0}^{n - |H|} \frac{(n!)^3}{(b!)^2 (b + |H|)! \cdot ((n-b)!)^2 (n - b - |H|)!} = (n!)^3 \sum_{b + c = n} A[b] B[c]$$
     where $A[b] = \frac{1}{(b!)^2 (b + |H|)!}$ ($0 \le b \le N - |H|$) and $B[c] = \frac{1}{(c!)^2 (c - |H|)!}$ ($|H| \le c \le N$). One NTT computes $f_n(H)$ for all $0 \le n \le N$, and since $P = Q - 2$, one EGF convolution $\frac{g_n(H)}{n!} = \sum_{k=0}^n \frac{f_k(H)}{k!} \frac{(-2)^{n-k}}{(n-k)!}$ recovers all $g_n(H)$ in $O(N \log N)$ total time.

##### Problem 20 (`Advanced` — Iter 12): UOJ #424 — count (Cartesian Trees of Bounded Left-Depth) (`C2-Pre`)
- **Link**: <https://uoj.ac/problem/424>
- **Mathematical Statement**: Two arrays of length $N$ ($N \le 2\times 10^5$) with elements in $\{1, \dots, M\}$ ($1 \le M \le N \le 2\times 10^5$) are called isomorphic if all their subsegments $[l, r]$ have the same leftmost minimum index. Count the number of equivalence classes of arrays of length $N$ over $\{1, \dots, M\}$ modulo $998244353$.
- **Diagnostic Signal**: Two arrays over $\{1, \dots, M\}$ share the same leftmost-minimum Cartesian tree iff the Cartesian tree has **at most $M - 1$ left-child edges** on any root-to-node path (since each left-child step strictly increases the minimum value). Under the standard bijection to Dyck paths (where the root starts at height $1$ and each left-child edge increases height by $1$), this is **Model I Chebyshev Bounded-Height Dyck Paths** with maximum height $H = M$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: A binary tree of $N$ nodes with at most $M-1$ left-child steps on any root-to-node path bijects to a Dyck path of semilength $N$ (length $2N$) with maximum height $H = M$, whose OGF satisfies $A_0(x) = 1$ and $A_h(x) = \frac{1}{1 - x A_{h-1}(x)}$ for $1 \le h \le M$.
  - *Hint 2*: Apply **Model I (Catalan Substitution II)**: $x = \frac{u}{(1+u)^2}$. Then $A_M(x(u)) = (1+u) \frac{1 - u^{M+1}}{1 - u^{M+2}}$.
  - *Hint 3*: By Master Formula B ($[x^N] H(u(x)) = [u^N] H(u)(1 - u^2)(1 + u)^{2N-2}$), we have $[x^N] A_M(x) = [u^N] (1-u)(1+u)^{2N} \frac{1 - u^{M+1}}{1 - u^{M+2}}$. Expand $\frac{1 - u^{M+1}}{1 - u^{M+2}} = \sum_{k \ge 0} (u^{k(M+2)} - u^{k(M+2) + M + 1})$ to compute the answer in **$O(N / M)$ time**!
- **Full Algebraic Derivation**:
  With $H = M$, substituting $x = \frac{u}{(1+u)^2}$ into $A_h(x) = \frac{1}{1 - x A_{h-1}(x)}$ yields $A_M(x(u)) = (1+u) \frac{1 - u^{M+1}}{1 - u^{M+2}}$. Extracting $[x^N] A_M(x)$ via the Differential Form of the Residue Engine ($\frac{dx}{du} = \frac{1-u}{(1+u)^3}, \frac{u}{x} = (1+u)^2$):
  $$[x^N] A_M(x) = [u^N] (1+u) \frac{1-u^{M+1}}{1-u^{M+2}} \cdot (1+u)^{2N+2} \frac{1-u}{(1+u)^3} = [u^N] (1-u)(1+u)^{2N} (1 - u^{M+1}) \sum_{k=0}^\infty u^{k(M+2)}$$
  Since $[u^m] (1-u)(1+u)^{2N} = \binom{2N}{m} - \binom{2N}{m-1}$, extracting $[u^N]$ yields the exact 4-term reflection sum:
  $$\text{Ans} = \sum_{k \ge 0} \left[ \binom{2N}{N - k(M+2)} - \binom{2N}{N - k(M+2) - 1} - \binom{2N}{N - k(M+2) - M - 1} + \binom{2N}{N - k(M+2) - M - 2} \right]$$
  which has only $O(N/M)$ non-zero terms and runs in $O(N/M)$ time after $O(N)$ factorial precomputation!

##### Problem 21 (`Mastery` — Iter 12): AtCoder AGC 054 E — ZigZag Break (`C1`)
- **Link**: <https://atcoder.jp/contests/agc054/tasks/agc054_e>
- **Mathematical Statement**: You are given integers $N$ and $A$. Count the number of permutations $P = (P_1, P_2, \dots, P_N)$ of $(1, 2, \dots, N)$ with $P_1 = A$ that can be reduced to length $2$ by repeatedly choosing three consecutive elements $(x, y, z)$ such that $y < \min(x, z)$ or $y > \max(x, z)$ and deleting $y$. Output the answer modulo $998244353$ for $T \le 5 \times 10^5$ test cases with $3 \le N \le 10^6$ and $1 \le A \le N$.
- **Diagnostic Signal**: Every operation removes a local extremum $y$, so $P_1$ and $P_N$ are never deleted; characterizing irreducible ("bad") permutations for fixed $P_1 = A < P_N = B$ reduces to a negative-binomial generating function extraction from $(1 - x)^{-A}$ in $O(1)$ per query!
- **3-Tier Progressive Hints**:
  - *Hint 1*: The final two remaining elements must be $P_1$ and $P_N$. By symmetry ($P_i \mapsto N + 1 - P_i$), split into the disjoint cases $P_1 < P_N$ and $P_1 > P_N$.
  - *Hint 2*: When $P_1 = A < P_N = B$, induction shows that $P$ can be reduced to $(P_1, P_N)$ if and only if there exists at least one index $1 \le i \le N-1$ such that $P_i \le A$ and $P_{i+1} \ge B$.
  - *Hint 3*: Count the *bad* permutations (where no such adjacent pair exists) by fixing $B = A + k$ ($2 \le k \le N - A$), inserting the middle elements $(A+1, \dots, A+k-1)$ first, and then inserting the small ($< A$) and large ($> B$) elements. Express the resulting sum over $k$ as a coefficient extraction from $(1 - x)^{-A}$!
- **Full Algebraic Derivation**:
  1. **Characterization of Valid Permutations**:
     Assume $P_1 = A < P_N = B$ (the case $P_1 > P_N$ is identical after replacing $A \leftarrow N + 1 - A$). Call elements $\le A$ of type $L$, elements $\ge B$ of type $R$, and elements in $(A, B)$ of type $M$. A permutation can be reduced to $(P_1, P_N)$ if and only if there is at least one adjacent pair $(P_i, P_{i+1})$ of type $(L, R)$.
  2. **Counting Bad Permutations for Fixed $B = A + k$ ($2 \le k \le N - A$)**:
     We construct a bad permutation (containing **no** adjacent $LR$ pair) in three stages:
     - **Stage 1**: Start with $(A, B) = (L, R)$ and insert the $k - 1$ middle elements $A+1, \dots, A+k-1$ between $A$ and $B$ in $(k - 1)!$ ways. Since $k \ge 2$, at least one $M$ separates $A$ and $B$, destroying the initial $LR$ pair.
     - **Stage 2**: Insert the $A - 1$ remaining elements of type $L$ ($1, \dots, A-1$) one by one. Because $P_1$ is already $L$, $P_N$ is $R$, and no $LR$ pair currently exists, when the $i$-th element of type $L$ ($1 \le i \le A - 1$) is inserted into the current sequence of length $k + i$, it can be placed anywhere except before $P_1$, after $P_N$, or immediately before the single $R$, leaving $(k + i - 1) - 1 = k - 2 + i$ valid slots.
     - **Stage 3**: Insert the $N - A - k$ remaining elements of type $R$ ($B+1, \dots, N$) one by one. Symmetrically, the $j$-th element of type $R$ ($1 \le j \le N - A - k$) has $k - 2 + j$ valid slots.
     Multiplying these choices together gives:
     $$\text{Bad}(k) = (k - 1)! \prod_{i=1}^{A-1} (k - 2 + i) \prod_{j=1}^{N-A-k} (k - 2 + j) = (A - 1)! (N - A - 2)! \binom{A + k - 3}{k - 2} (k - 1)$$
  3. **Generating Function Extraction in $O(1)$ Per Query**:
     Shifting the index via $m = k - 2$ ($0 \le m \le M$, where $M = N - A - 2$) and using $\sum_{m \ge 0} \binom{A + m - 1}{m} x^m = (1 - x)^{-A}$:
     $$\sum_{m=0}^M \binom{A + m - 1}{m}(m + 1) = [x^M] \left(\frac{1}{(1 - x)^{A+1}} + \frac{Ax}{(1 - x)^{A+2}}\right) = \binom{A + M}{M} + A \binom{A + M}{M - 1}$$
     Thus $\text{Bad}_{<}(N, A) = 0$ if $N - A - 2 < 0$, and otherwise:
     $$\text{Bad}_{<}(N, A) = (A - 1)! (N - A - 2)! \left(\binom{N - 2}{N - A - 2} + A \binom{N - 2}{N - A - 3}\right)$$
     Subtracting both $\text{Bad}_{<}(N, A)$ and $\text{Bad}_{<}(N, N + 1 - A)$ from $(N - 1)!$ answers each query in $O(1)$ time!

---

#### Module C: Iteration 13 / 65 — Transcendental Substitutions ($e^x-1, \ln(1+x)$), Stirling, Lah & Falling Factorials (Problems 22–29)

##### Problem 22 (`Stepping Stone` — Iter 13): Codeforces 1342E — Placing Rooks (`C2-New`)
- **Link**: <https://codeforces.com/problemset/problem/1342/E>
- **Mathematical Statement**: Place $n$ rooks on an $n \times n$ chessboard ($1 \le n \le 2\times 10^5$) such that every cell is attacked by at least one rook and exactly $k$ pairs of rooks attack each other ($0 \le k < \frac{n(n-1)}{2}$). Output the number of ways modulo $998244353$.
- **Diagnostic Signal**: Every cell is attacked iff either every row or every column contains at least one rook. If every row has $1$ rook and $c = n - k$ columns are non-empty, we are counting **surjections** from $n$ rows onto $c$ chosen columns!
- **3-Tier Progressive Hints**:
  - *Hint 1*: For every row to have 1 rook, a column with $m \ge 1$ rooks contributes $m - 1$ mutually attacking pairs in that column. Thus $\sum (m_j - 1) = n - c = k \iff c = n - k$ non-empty columns.
  - *Hint 2*: Choose which $c = n - k$ columns are non-empty in $\binom{n}{c}$ ways, and distribute $n$ distinct row rooks surjectively onto those $c$ columns in $c!\, {n \brace c} = [x^n/n!] (e^x - 1)^c$ ways.
  - *Hint 3*: Multiply by $2$ if $1 \le k < n$ (since either all rows or all columns are covered; for $k = 0$ both hold simultaneously and the answer is $n!$, and for $k \ge n$ the answer is $0$).
- **Full Algebraic Derivation**:
  For $k \ge n$, the answer is $0$; for $k = 0$, the answer is $n!$. For $1 \le k < n$, let $c = n - k$. By the EGF $[x^n/n!] (e^x - 1)^c = c!\, {n \brace c} = \sum_{j=0}^c (-1)^{c-j} \binom{c}{j} j^n$, the total number of valid placements is:
  $$\text{Ans} = 2 \binom{n}{n-k} \sum_{j=0}^{n-k} (-1)^{n-k-j} \binom{n-k}{j} j^n \bmod 998244353$$
  evaluated in $O(n \log p)$ (or $O(n)$ with a linear sieve of $j^n$).

##### Problem 23 (`Intermediate` — Iter 13): Luogu P4091 — [HEOI2016 / TJOI2016] 求和 (`C2-New`)
- **Link**: <https://www.luogu.com.cn/problem/P4091>
- **Mathematical Statement**: Given $n \le 10^5$, compute
  $$S = \sum_{i=0}^n \sum_{j=0}^i {i \brace j} 2^j (j!) \bmod 998244353$$
- **Diagnostic Signal**: Summing ${i \brace j}$ down **columns** $0 \le i \le n$ while weighting by $2^j j!$: swap the sums and substitute the explicit formula for $j!\, {i \brace j}$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Substitute $j!\, {i \brace j} = \sum_{k=0}^j (-1)^{j-k} \binom{j}{k} k^i$ (note that for $j > i$, ${i \brace j} = 0$, so we can extend the upper limit of $j$ from $i$ to $n$!).
  - *Hint 2*: Swap the summation over $i$ and $j$: $G(k) = \sum_{i=0}^n k^i = \frac{k^{n+1}-1}{k-1}$ (for $k=0$, $0^0 = 1$; for $k=1$, the sum is $n+1$).
  - *Hint 3*: Then $S = \sum_{j=0}^n 2^j j! \sum_{k=0}^j \frac{(-1)^{j-k}}{(j-k)!} \frac{G(k)}{k!}$, which is **1 single NTT convolution**!
- **Full Algebraic Derivation**:
  Since ${i \brace j} = 0$ for $j > i$, we extend the inner sum to $j = 0 \dots n$:
  $$S = \sum_{j=0}^n 2^j j! \sum_{k=0}^j \frac{(-1)^{j-k}}{(j-k)!} \frac{\sum_{i=0}^n k^i}{k!} = \sum_{j=0}^n 2^j j! [x^j] \left( A(x) B(x) \right)$$
  where $A(x) = \sum_{k=0}^n \frac{\sum_{i=0}^n k^i}{k!} x^k$ and $B(x) = \sum_{m=0}^n \frac{(-1)^m}{m!} x^m$. One NTT of size $2n$ computes all $[x^j](A(x)B(x))$ in $O(n \log n)$ time!

##### Problem 24 (`Intermediate` — Iter 13): Luogu P6620 — [省选联考 2020 A 卷] 组合数问题 (`C1` / `C2-New` / `C2-Pre`)
- **Link**: <https://www.luogu.com.cn/problem/P6620>
- **Mathematical Statement**: Given integers $n, x, p$ and a degree-$m$ polynomial $f(k) = \sum_{i=0}^m a_i k^i$ ($1 \le n, x, p \le 10^9$, $1 \le m \le 10^3$, where $p$ is **not necessarily prime**), compute:
  $$\left(\sum_{k=0}^n f(k) x^k \binom{n}{k}\right) \bmod p$$
- **Diagnostic Signal**: Polynomial weight $f(k)$ inside a binomial sum $\sum_{k=0}^n f(k) x^k \binom{n}{k}$ under a **non-prime modulus $p$** where division by $j!$ is illegal! Converting $f(k) = \sum_{j=0}^m b_j k^{\underline{j}}$ into the falling-factorial basis via Stirling numbers ${i \brace j}$ requires **zero divisions**!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Convert the ordinary polynomial $f(k) = \sum_{i=0}^m a_i k^i$ into the falling-factorial basis $f(k) = \sum_{j=0}^m b_j k^{\underline{j}}$ using Stirling numbers of the second kind: $b_j = \sum_{i=j}^m a_i {i \brace j}$.
  - *Hint 2*: Use the absorption identity $k^{\underline{j}} \binom{n}{k} = n^{\underline{j}} \binom{n - j}{k - j}$, which never requires division by $j!$ (crucial since $p$ is arbitrary and $\gcd(j!, p)$ may be $> 1$!).
  - *Hint 3*: Collapse the inner sum over $k$ via the binomial theorem $\sum_{k=j}^n \binom{n-j}{k-j} x^k = x^j (1 + x)^{n - j}$ in $O(m^2)$ total time.
- **Full Algebraic Derivation**:
  Precompute the Stirling triangle ${i \brace j} \bmod p$ for $0 \le j \le i \le m$ in $O(m^2)$ time via ${i \brace j} = {i-1 \brace j-1} + j {i-1 \brace j} \bmod p$, and compute $b_j = \sum_{i=j}^m a_i {i \brace j} \bmod p$. Substituting $f(k) = \sum_{j=0}^m b_j k^{\underline{j}}$ and applying $k^{\underline{j}} \binom{n}{k} = n^{\underline{j}} \binom{n-j}{k-j}$:
  $$\sum_{k=0}^n f(k) x^k \binom{n}{k} = \sum_{j=0}^{\min(n, m)} b_j n^{\underline{j}} x^j \sum_{k=j}^n \binom{n - j}{k - j} x^{k - j} = \sum_{j=0}^{\min(n, m)} b_j n^{\underline{j}} x^j (1 + x)^{n - j} \bmod p$$
  Since $n^{\underline{j}} = n(n-1)\cdots(n-j+1)$ is a product of $j$ integers, no modular inverses are ever needed! Total time: $O(m^2 + m \log n)$.

##### Problem 25 (`Intermediate` — Iter 13): Luogu P6667 — [清华集训2016] 如何优雅地求和 (`C2-Pre`)
- **Link**: <https://www.luogu.com.cn/problem/P6667>
- **Mathematical Statement**: Given $n \le 10^9$, degree $m \le 2\times 10^4$, probability parameter $x \in \mathbb{F}_{998244353}$, and point values $f(0), f(1), \dots, f(m)$ of a degree-$m$ polynomial $f$, compute:
  $$\sum_{k=0}^n \binom{n}{k} x^k (1-x)^{n-k} f(k) \bmod 998244353$$
- **Diagnostic Signal**: Binomial sum $\sum_{k=0}^n \binom{n}{k} x^k (1-x)^{n-k} f(k)$ with huge $n \le 10^9$ and small degree $m \le 2\times 10^4$ given by point values $f(0 \dots m)$: this is the canonical **Falling-Factorial Polynomial (`下降幂多项式`) Binomial Moment Collapse**!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Do **not** interpolate $f(k)$ into the standard monomial basis $k^j$! Instead, express $f(k) = \sum_{j=0}^m c_j k^{\underline{j}}$ in the falling-factorial basis.
  - *Hint 2*: Use the Point-Value EGF theorem $C(t) = \widehat{f}(t) e^{-t} \bmod t^{m+1}$ to compute $c_0, \dots, c_m$ from $f(0), \dots, f(m)$ in **1 single NTT** ($O(m \log m)$).
  - *Hint 3*: Substitute $\binom{n}{k} k^{\underline{j}} = n^{\underline{j}} \binom{n-j}{k-j}$; the inner sum over $k$ collapses by the Binomial Theorem $\sum_{k=j}^n \binom{n-j}{k-j} x^{k-j}(1-x)^{n-k} = (x + 1 - x)^{n-j} = 1$!
- **Full Algebraic Derivation**:
  Step 1: Compute $c_j = \sum_{i=0}^j \frac{f(i)}{i!} \frac{(-1)^{j-i}}{(j-i)!}$ for $0 \le j \le m$ via 1 NTT (`ffp_from_values`).
  Step 2: Swap the summation and apply the absorption identity $\binom{n}{k} k^{\underline{j}} = n^{\underline{j}} \binom{n-j}{k-j}$:
  $$\sum_{k=0}^n \binom{n}{k} x^k (1-x)^{n-k} \sum_{j=0}^m c_j k^{\underline{j}} = \sum_{j=0}^m c_j n^{\underline{j}} x^j \sum_{k=j}^n \binom{n-j}{k-j} x^{k-j} (1-x)^{n-k} = \sum_{j=0}^m c_j n^{\underline{j}} x^j$$
  Total time: $O(m \log m)$ for the single NTT + $O(m)$ linear scan, completely independent of $n \le 10^9$!

##### Problem 26 (`Intermediate` — Iter 13): Codeforces 932E — Team Work (`C1` / `C2-New`)
- **Link**: <https://codeforces.com/problemset/problem/932/E>
- **Mathematical Statement**: Given $N \le 10^9$ and $K \le 5000$ (or $K \le 2\times 10^5$ in the NTT generalization), compute $\sum_{i=1}^N \binom{N}{i} i^K \bmod (10^9+7)$ (or $\bmod 998244353$).
- **Diagnostic Signal**: Monomial weight $i^K$ inside a binomial sum $\sum_{i=0}^N \binom{N}{i} i^K$: convert $i^K = \sum_{j=0}^K {K \brace j} i^{\underline{j}}$ into the falling-factorial basis!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Expand $i^K = \sum_{j=0}^K {K \brace j} i^{\underline{j}}$ using Row $K$ of the Stirling numbers of the second kind.
  - *Hint 2*: Apply $\binom{N}{i} i^{\underline{j}} = N^{\underline{j}} \binom{N-j}{i-j}$ and sum over $i$: $\sum_{i=j}^N \binom{N-j}{i-j} = 2^{N-j}$.
  - *Hint 3*: Compute ${K \brace j}$ for $0 \le j \le K$ in $O(K^2)$ DP (for $K=5000, p=10^9+7$) or $O(K \log K)$ NTT (for $K=2\times 10^5$), then sum $\sum_{j=0}^{\min(N,K)} {K \brace j} N^{\underline{j}} 2^{N-j}$.
- **Full Algebraic Derivation**:
  $$\sum_{i=0}^N \binom{N}{i} i^K = \sum_{j=0}^{\min(N,K)} {K \brace j} N^{\underline{j}} \sum_{i=j}^N \binom{N-j}{i-j} = \sum_{j=0}^{\min(N,K)} {K \brace j} N^{\underline{j}} 2^{N-j}$$

##### Problem 27 (`Advanced` — Iter 13): Codeforces 960G — Bandit Blues (`C1` / `C2-Pre`)
- **Link**: <https://codeforces.com/problemset/problem/960/G>
- **Mathematical Statement**: Count the number of permutations of $(1, 2, \dots, n)$ ($n \le 10^5$) with exactly $A$ prefix maxima and $B$ suffix maxima, modulo $998244353$.
- **Diagnostic Signal**: The global maximum $n$ splits the permutation into $A-1$ left prefix-maximum cycles and $B-1$ right suffix-maximum cycles. By the Fundamental Foata Bijection, the number of permutations of $m$ elements with $k$ prefix maxima equals the unsigned Stirling number of the first kind ${m \brack k}$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Fix the position of $n$: there are $A-1$ prefix maxima to its left and $B-1$ suffix maxima to its right.
  - *Hint 2*: Instead of summing over the position of $n$, partition the remaining $n-1$ elements into $A + B - 2$ cycles first (${n-1 \brack A+B-2}$ ways), then choose which $A-1$ cycles go to the left of $n$ in $\binom{A+B-2}{A-1}$ ways!
  - *Hint 3*: Compute ${n-1 \brack A+B-2}$ by extracting $[x^{A+B-2}] x^{\overline{n-1}}$ in $O(n \log n)$ via `stirling_1st_row` (Doubling + Taylor Shift)!
- **Full Algebraic Derivation**:
  $$\text{Ans} = \sum_{i=0}^{n-1} \binom{n-1}{i} {i \brack A-1} {n-1-i \brack B-1} = \binom{A+B-2}{A-1} {n-1 \brack A+B-2}$$
  Why does the convolution identity hold? Because the EGF of unsigned Stirling numbers of the first kind is $\sum_{m \ge k} {m \brack k} \frac{x^m}{m!} = \frac{(-\ln(1-x))^k}{k!}$, and multiplying $\frac{(-\ln(1-x))^{A-1}}{(A-1)!} \cdot \frac{(-\ln(1-x))^{B-1}}{(B-1)!} = \binom{A+B-2}{A-1} \frac{(-\ln(1-x))^{A+B-2}}{(A+B-2)!}$ proves the identity in one line! Then ${n-1 \brack A+B-2} = [x^{A+B-2}] x^{\overline{n-1}}$ is computed in $O(n \log n)$ time via Taylor-shift doubling.

##### Problem 28 (`Mastery` — Iter 13): Codeforces 1097G — Vladislav and a Great Legend (`C2-New` / `C2-Pre`)
- **Link**: <https://codeforces.com/problemset/problem/1097/G>
- **Mathematical Statement**: Given a tree $T$ with $n$ vertices ($2 \le n \le 10^5$) and an integer $k$ ($1 \le k \le 200$), for a non-empty subset $X \subseteq V(T)$, let $f(X)$ be the number of edges in the minimal connected subtree spanning $X$. Compute $\sum_{\emptyset \neq X \subseteq V(T)} f(X)^k \bmod (10^9 + 7)$.
- **Diagnostic Signal**: Converting $f(X)^k = \sum_{j=0}^k {k \brace j} j! \binom{f(X)}{j}$ into the falling-factorial / binomial basis replaces an intractable $k$-th power with choosing $j \le k$ edges from the minimal Steiner subtree of $X$, which is solved by an $O(nk)$ tree-knapsack DP!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Decompose $f(X)^k$ into the falling-factorial basis via Stirling numbers of the second kind: $f(X)^k = \sum_{j=0}^k {k \brace j} j! \binom{f(X)}{j}$.
  - *Hint 2*: Observe that $\binom{f(X)}{j}$ counts the number of ways to choose $j$ edges that all belong to the minimal subtree spanning $X$.
  - *Hint 3*: Perform a knapsack-style tree DP $\text{dp}[u][j]$ tracking the number of pairs $(X, E')$ in the subtree of $u$ with $|E'| = j$; by the standard tree-knapsack bound $\min(\text{sz}[u], k)$, merging subtrees takes $O(nk)$ total time!
- **Full Algebraic Derivation**:
  Using $m^k = \sum_{j=0}^k {k \brace j} j! \binom{m}{j}$, we swap the order of summation:
  $$\sum_{\emptyset \neq X \subseteq V(T)} f(X)^k = \sum_{j=0}^k {k \brace j} j! \sum_{\emptyset \neq X \subseteq V(T)} \binom{f(X)}{j}$$
  Now $\sum_{\emptyset \neq X} \binom{f(X)}{j}$ equals the number of pairs $(X, E')$ where $E' \subseteq E(T)$ has $|E'| = j$ and every edge $e \in E'$ separates $X$. In a rooted tree DP, let $\text{dp}[u][j]$ be the number of pairs $(X_u, E'_u)$ in the subtree of $u$ with $X_u \neq \emptyset$, $|E'_u| = j$, such that every edge in $E'_u$ has at least one vertex of $X_u$ in its lower subtree. When extending a child $v$'s subtree along the parent edge $(u, v)$, the polynomial $P_v(x) = \sum_{j=0}^k \text{dp}[v][j] x^j$ transitions to $P_v(x)(1 + x) + x$ (or $P_v(x)(1 + x) - x$ depending on whether the empty set is included in $P_v$). Bounding each convolution by $\min(\text{sz}[u], k)$ yields $O(nk)$ total time and $O(nk)$ space.

##### Problem 29 (`Mastery` — Iter 13): Codeforces 1278F — Cards (`C1` / `C2-New` / `C2-Pre`)
- **Link**: <https://codeforces.com/problemset/problem/1278/F>
- **Mathematical Statement**: A deck of $m$ cards contains $1$ Joker. In each of $n$ independent rounds ($n, m \le 998244352$), you shuffle the deck and look at the top card; let $X$ be the number of times you see the Joker. Given $k \le 5000$ (or $k \le 2\times 10^5$ in the NTT version), compute $E[X^k] \bmod 998244353$.
- **Diagnostic Signal**: $X \sim \operatorname{Binomial}(n, p)$ with $p = \frac{1}{m}$. Computing the $k$-th raw moment $E[X^k] = \sum_{i=0}^n \binom{n}{i} p^i (1-p)^{n-i} i^k$ for huge $n \le 10^9$ is the exact **Falling-Factorial Binomial Moment Collapse**!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Decompose $i^k = \sum_{j=0}^k {k \brace j} i^{\underline{j}}$ into the falling-factorial basis.
  - *Hint 2*: Notice that $E[X^{\underline{j}}] = \sum_{i=0}^n \binom{n}{i} p^i (1-p)^{n-i} i^{\underline{j}} = n^{\underline{j}} p^j (p + 1 - p)^{n-j} = n^{\underline{j}} m^{-j}$!
  - *Hint 3*: Compute Row $k$ of the Stirling numbers of the second kind ${k \brace j}$ in $O(k \log k)$ via 1 NTT (`stirling_2nd_row`), then sum $\sum_{j=0}^{\min(n,k)} {k \brace j} n^{\underline{j}} m^{-j}$ in $O(k)$!
- **Full Algebraic Derivation**:
  $$E[X^k] = E\!\left[\sum_{j=0}^k {k \brace j} X^{\underline{j}}\right] = \sum_{j=0}^{\min(n,k)} {k \brace j} n^{\underline{j}} \left(\frac{1}{m}\right)^j \bmod 998244353$$
  Using 1 NTT to compute ${k \brace 0}, \dots, {k \brace k}$ solves even the $k = 2\times 10^5$ version in $O(k \log k)$ time.

---

#### Module D: Iteration 14 / 66 — Logarithmic Derivatives ($F'/F$), Euler / Multiset ($\operatorname{MSET}/\operatorname{PSET}$) & Power Sums (Problems 30–39)

##### Problem 30 (`Stepping Stone` — Iter 14): Luogu P4389 — 付公主的背包 (`C1` / `C2-New` / `C2-Pre`)
- **Link**: <https://www.luogu.com.cn/problem/P4389>
- **Mathematical Statement**: There are $n$ types of items ($n \le 10^5$), each with volume $v_i \in [1, m]$ ($m \le 10^5$) and infinite supply. For every target capacity $s = 1, 2, \dots, m$, count the number of ways to fill a knapsack of volume $s$ modulo $998244353$.
- **Diagnostic Signal**: Unbounded knapsack OGF $F(x) = \prod_{i=1}^n \frac{1}{1 - x^{v_i}} \bmod x^{m+1}$ where $v_i$ sits in the **exponent**—this is the canonical **Regime A Euler / Multiset ($\operatorname{MSET}$) Transform**!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Never multiply $\frac{1}{1-x^{v_i}}$ one by one ($O(nm)$). First bucket the items by volume: let $c_w$ be the number of item types with volume $w$.
  - *Hint 2*: Take the formal logarithm: $\ln F(x) = \sum_{w=1}^m c_w \ln\frac{1}{1-x^w} = \sum_{w=1}^m c_w \sum_{k=1}^{\lfloor m/w \rfloor} \frac{x^{kw}}{k}$.
  - *Hint 3*: Populate the coefficients of $\ln F(x)$ in $O(m \log m)$ via the Harmonic Sieve, then call `poly_exp` once in $O(m \log m)$!
- **Full Algebraic Derivation**:
  See `euler_multiset_transform` in Section 8.2: bucketing $c_w = \#\{i : v_i = w\}$ and accumulating $[x^{kw}]\ln F(x) \mathrel{+}= \frac{c_w}{k}$ for all $1 \le w \le m, 1 \le k \le \lfloor m/w \rfloor$ takes $O(m \log m)$ additions, followed by a single $O(m \log m)$ polynomial exponential $F(x) = \exp(\ln F(x)) \bmod x^{m+1}$.

##### Problem 31 (`Stepping Stone` — Iter 14): AtCoder FPS-24 N — Coin 2 (`C1`)
- **Link**: <https://atcoder.jp/contests/fps-24/tasks/fps_24_n>
- **Mathematical Statement**: You are given $A_i$ coins of denomination $i$ yen for each $1 \le i \le N$ ($N \le 2.5 \times 10^5$, $0 \le A_i \le N$). Count the number of ways to select a multiset of coins whose values sum to $S$ for each $S = 1, 2, \dots, N$ (or $S = N$) modulo $998244353$.
- **Diagnostic Signal**: Bounded knapsack where item $i$ has weight $i$ and copy bound $A_i$: the OGF is $P(x) = \prod_{i=1}^N (1 + x^i + x^{2i} + \dots + x^{i A_i}) = \prod_{i=1}^N \frac{1 - x^{i(A_i+1)}}{1 - x^i} \bmod x^{N+1}$, which reduces directly to the **Regime A Harmonic Sieve ($\ln/\exp$)**!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Rewrite the finite geometric series $1 + x^i + \dots + x^{i A_i}$ as the quotient $\frac{1 - x^{i(A_i+1)}}{1 - x^i}$.
  - *Hint 2*: Take the formal logarithm modulo $x^{N+1}$: $\ln P(x) = \sum_{i=1}^N \ln\frac{1}{1 - x^i} - \sum_{i=1}^N \ln\frac{1}{1 - x^{i(A_i+1)}}$. Notice that terms with $i(A_i+1) > N$ vanish modulo $x^{N+1}$!
  - *Hint 3*: Accumulate a net weight array $c_w$ where $c_i \mathrel{+}= 1$ for each $1 \le i \le N$ and $c_{i(A_i+1)} \mathrel{-}= 1$ whenever $i(A_i+1) \le N$. Build $\ln P(x) = \sum_{w=1}^N c_w \sum_{k=1}^{\lfloor N/w \rfloor} \frac{x^{kw}}{k}$ in $O(N \log N)$ via the Harmonic Sieve, then exponentiate via `poly_exp`!
- **Full Algebraic Derivation**:
  $$P(x) = \prod_{i=1}^N \frac{1 - x^{i(A_i+1)}}{1 - x^i} \equiv \exp\!\left(\sum_{i=1}^N \sum_{k=1}^{\lfloor N/i \rfloor} \frac{x^{ki}}{k} - \sum_{\substack{1 \le i \le N \\ i(A_i+1) \le N}} \sum_{k=1}^{\lfloor N / (i(A_i+1)) \rfloor} \frac{x^{k i (A_i+1)}}{k}\right) \pmod{x^{N+1}}$$
  Populating the logarithm array via the harmonic loop takes $O(N \log N)$ time, and a single `poly_exp` recovers all answers up to $N$ in $O(N \log N)$ time.

##### Problem 32 (`Stepping Stone` — Iter 14): AtCoder ABC 267 Ex — Odd Sum (`C2-Pre`)
- **Link**: <https://atcoder.jp/contests/abc267/tasks/abc267_h>
- **Mathematical Statement**: Given $N$ integers $A_1, \dots, A_N \in [1, 10]$ ($N \le 10^5$) and target sum $M \le 10^6$, find the number of subsequences containing an **odd** number of elements whose sum is $M$, modulo $998244353$.
- **Diagnostic Signal**: Bivariate 0-1 subset-sum product $\prod_{i=1}^N (1 + y x^{A_i})$ combined with the parity filter $\frac{F(x, 1) - F(x, -1)}{2}$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Apply the $m=2$ roots-of-unity filter on the count variable $y$: the OGF of odd-sized subsets is $\frac{1}{2}\left(\prod_{i=1}^N (1 + x^{A_i}) - \prod_{i=1}^N (1 - x^{A_i})\right)$.
  - *Hint 2*: Bucket $c_w = \#\{i : A_i = w\}$. Since $A_i \le 10$ (or even if $A_i \le M$), both products $\prod_w (1 + x^w)^{c_w}$ and $\prod_w (1 - x^w)^{c_w}$ can be computed up to $x^M$ via the Regime A $\ln/\exp$ Harmonic Sieve (or D&C product tree).
  - *Hint 3*: Subtract the $[x^M]$ coefficients of the two products and multiply by $2^{-1} \bmod 998244353$.
- **Full Algebraic Derivation**:
  Let $F_+(x) = \prod_{w=1}^{10} (1 + x^w)^{c_w}$ and $F_-(x) = \prod_{w=1}^{10} (1 - x^w)^{c_w}$. Using $\ln F_\pm(x) = \sum_{w} c_w \sum_{k \ge 1} \frac{(\pm 1)^k (-1)^{k-1}}{k} x^{kw}$ and `poly_exp` (or direct D&C multiplication), we extract $\frac{1}{2}([x^M]F_+(x) - [x^M]F_-(x))$ in $O(M \log M)$ time.

##### Problem 33 (`Intermediate` — Iter 14): Luogu P4705 — 玩游戏 (`C2-Pre`)
- **Link**: <https://www.luogu.com.cn/problem/P4705>
- **Mathematical Statement**: Given two arrays $a_1, \dots, a_n$ and $b_1, \dots, b_m$ ($n, m \le 10^5$), for every $k = 1, 2, \dots, t$ ($t \le 10^5$), compute the expected value of $(a_i + b_j)^k$ for uniformly chosen $i \in [1, n], j \in [1, m]$, modulo $998244353$.
- **Diagnostic Signal**: Expanding $(a_i + b_j)^k = k! \sum_{r=0}^k \frac{a_i^r}{r!} \frac{b_j^{k-r}}{(k-r)!}$ reduces the problem to computing all **Scalar Power Sums** $p_r(A) = \sum_{i=1}^n a_i^r$ and $p_r(B) = \sum_{j=1}^m b_j^r$ for $0 \le r \le t$—the exact **Regime B Newton–Girard Logarithmic Derivative**!
- **3-Tier Progressive Hints**:
  - *Hint 1*: By binomial expansion, $\sum_{i,j} (a_i + b_j)^k = k! \sum_{r=0}^k \left(\frac{\sum_{i=1}^n a_i^r}{r!}\right) \left(\frac{\sum_{j=1}^m b_j^{k-r}}{(k-r)!}\right)$, which is 1 EGF convolution once we know the power sums $p_r(A)$ and $p_r(B)$!
  - *Hint 2*: To compute $p_r(A) = \sum_{i=1}^n a_i^r$ for all $1 \le r \le t$ simultaneously, build $Q_A(x) = \prod_{i=1}^n (1 - a_i x)$ via a subproduct tree in $O(n \log^2 n)$ time.
  - *Hint 3*: Compute $-x \frac{Q_A'(x)}{Q_A(x)} = -x \frac{d}{dx} \ln Q_A(x) \bmod x^{t+1}$ in $O(t \log t)$ time to get all $p_r(A)$ at once!
- **Full Algebraic Derivation**:
  1. Build $Q_A(x) = \prod_{i=1}^n (1 - a_i x)$ and $Q_B(x) = \prod_{j=1}^m (1 - b_j x)$ via D&C binary multiplication trees in $O((n+m)\log^2(n+m))$.
  2. Compute $P_A(x) = n - x \frac{Q_A'(x)}{Q_A(x)} \bmod x^{t+1}$ and $P_B(x) = m - x \frac{Q_B'(x)}{Q_B(x)} \bmod x^{t+1}$ in $O(t \log t)$.
  3. Scale $[x^r]P_A(x)$ and $[x^r]P_B(x)$ by $\frac{1}{r!}$, convolve them in 1 NTT, and multiply $[x^k]$ by $\frac{k!}{nm} \bmod 998244353$.

##### Problem 34 (`Intermediate` — Iter 14): AtCoder FPS-24 Q — Dice (`C1`)
- **Link**: <https://atcoder.jp/contests/fps-24/tasks/fps_24_q>
- **Mathematical Statement**: You have an $N$-sided die with faces $A_1 < A_2 < \dots < A_N$ and an $M$-sided die with faces $B_1 < B_2 < \dots < B_M$ ($N, M, K \le 10^5$). Each face is rolled with uniform probability $1/N$ and $1/M$ respectively. For every $k = 1, 2, \dots, K$, compute the $k$-th moment of their sum, $\mathbb{E}[(X + Y)^k] = \frac{1}{NM} \sum_{i=1}^N \sum_{j=1}^M (A_i + B_j)^k \bmod 998244353$.
- **Diagnostic Signal**: Identical in structure to Luogu P4705: binomial expansion decouples $(A_i + B_j)^k$ into an EGF convolution of power sums $S_r(A) = \sum_{i=1}^N A_i^r$ and $S_r(B) = \sum_{j=1}^M B_j^r$, which are extracted in bulk via **Subproduct Tree + Logarithmic Derivative** (or, when $A_i, B_j$ are small integer weights, via the **Borel–Laplace exponential substitution** $\sum_{i=1}^N e^{A_i x}$)!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Write $\mathbb{E}[(X + Y)^k] = \frac{k!}{NM} \sum_{r=0}^k \left(\frac{S_r(A)}{r!}\right) \left(\frac{S_{k-r}(B)}{(k-r)!}\right)$ where $S_r(A) = \sum_{i=1}^N A_i^r$.
  - *Hint 2*: Build $Q_A(x) = \prod_{i=1}^N (1 - A_i x)$ and $Q_B(x) = \prod_{j=1}^M (1 - B_j x)$ via D&C subproduct trees in $O((N+M)\log^2(N+M))$ time.
  - *Hint 3*: Compute the logarithmic derivatives $P_A(x) = N - \frac{x Q_A'(x)}{Q_A(x)} \bmod x^{K+1}$ and $P_B(x) = M - \frac{x Q_B'(x)}{Q_B(x)} \bmod x^{K+1}$ in $O(K \log K)$, scale by $1/r!$, and convolve! *(Companion Borel–Laplace Note: If a problem instead asks to extract $[z^K] k! \mathcal{L}\{P(e^z)\}$ where $P(x) = \sum_{j=0}^d c_j x^j$, applying the formal Laplace transform $\mathcal{L}\{e^{jz}\} = \frac{1}{1 - jz}$ reduces the problem to the partial-fraction sum $\sum_{j=0}^d \frac{c_j}{1 - jz}$ of Section 5.3!)*
- **Full Algebraic Derivation**:
  $$P_A(x) = \sum_{r=0}^K S_r(A) x^r \equiv N - x \frac{Q_A'(x)}{Q_A(x)} \pmod{x^{K+1}}, \qquad Q_A(x) = \prod_{i=1}^N (1 - A_i x)$$
  Scaling $\widehat{P}_A(x) = \sum_{r=0}^K \frac{S_r(A)}{r!} x^r$ and $\widehat{P}_B(x) = \sum_{r=0}^K \frac{S_r(B)}{r!} x^r$, we obtain $\mathbb{E}[(X+Y)^k] = \frac{k!}{NM} [x^k]\left(\widehat{P}_A(x)\widehat{P}_B(x)\right)$ in $O((N+M)\log^2(N+M) + K \log K)$ time.

##### Problem 35 (`Intermediate` — Iter 14): AtCoder ARC 106 E / Yukicoder 1145 — Sum of Powers & Medals (`C2-New`)
- **Link**: <https://yukicoder.me/problems/no/1145>
- **Mathematical Statement**: Given $N$ integers $A_1, \dots, A_N$ ($N \le 10^5$) and $K \le 10^5$, output $S_k = \sum_{i=1}^N A_i^k \bmod 998244353$ for all $k = 1, 2, \dots, K$, or conversely recover the elementary symmetric polynomials $e_1, \dots, e_N$ from the power sums $S_1, \dots, S_N$.
- **Diagnostic Signal**: Direct forward and inverse **Regime B Newton–Girard Bridge** $P(x) = -x \frac{Q'(x)}{Q(x)} \iff Q(x) = \exp\!\left(-\int \frac{P(x)}{x} dx\right)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: For $A_i \to S_k$, build $Q(x) = \prod_{i=1}^N (1 - A_i x)$ by subproduct tree in $O(N \log^2 N)$.
  - *Hint 2*: Compute $P(x) = -x Q'(x) Q(x)^{-1} \bmod x^{K+1}$ in $O(K \log K)$.
  - *Hint 3*: For the inverse problem ($S_k \to e_k$ when $p > N$), form $L(x) = -\sum_{k=1}^N \frac{S_k}{k} x^k$ and compute $Q(x) = \exp(L(x)) \bmod x^{N+1}$, where $e_k = (-1)^k [x^k] Q(x)$.
- **Full Algebraic Derivation**:
  Since $\ln(1 - A_i x) = -\sum_{k=1}^\infty \frac{A_i^k}{k} x^k$, summing over $i = 1 \dots N$ gives $\ln Q(x) = -\sum_{k=1}^\infty \frac{S_k}{k} x^k$, and differentiating gives $-x \frac{Q'(x)}{Q(x)} = \sum_{k=1}^\infty S_k x^k$. Total time: $O(N \log^2 N + K \log K)$.

##### Problem 36 (`Intermediate` — Iter 14): Codeforces 1613F — Tree Coloring (`C2-New`)
- **Link**: <https://codeforces.com/problemset/problem/1613/F>
- **Mathematical Statement**: Given a rooted tree of $n$ vertices ($n \le 2.5 \times 10^5$, rooted at $1$), count the number of permutations $p_1, p_2, \dots, p_n$ of $\{1, 2, \dots, n\}$ such that for every vertex $u$ and every child $v$ of $u$, $p_u \neq p_v - 1$. Output the answer modulo $998244353$.
- **Diagnostic Signal**: Inclusion-Exclusion over forbidden parent-child adjacency relations $(u, v)$ where each vertex $u$ with $c_u$ children can be matched to at most one child $v$, producing the **Rook / Matching Polynomial** $\prod_{u=1}^n (1 + c_u x)$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Apply the Principle of Inclusion-Exclusion (PIE) on the set of violated tree edges $E' \subseteq E(T)$ where $p_u = p_v - 1$.
  - *Hint 2*: A subset of $k$ violated directed parent-to-child edges $(u \to v)$ can occur simultaneously if and only if no two chosen edges share the same parent $u$ (each $u$ can precede at most one child $v$ in the permutation), and since $T$ is a tree, no cycles can form! Thus every parent $u$ independently contributes a factor of $(1 + c_u x)$, where $c_u$ is the number of children of $u$.
  - *Hint 3*: Compute $P(x) = \prod_{u=1}^n (1 + c_u x) = \sum_{k=0}^{n-1} a_k x^k$ via a D&C subproduct tree in $O(n \log^2 n)$ (or frequency-bucketed $\ln/\exp$ in $O(n \log n)$), then evaluate $\sum_{k=0}^{n-1} (-1)^k a_k (n - k)! \bmod 998244353$!
- **Full Algebraic Derivation**:
  If $k$ valid parent-child pairs are forced to satisfy $p_u = p_v - 1$, they fuse $n$ elements into $n - k$ disjoint chains, which can be permuted in $(n - k)!$ ways. Because each vertex $u$ can choose at most one of its $c_u$ children to immediately follow it, the number of ways to choose $k$ compatible edges is $a_k = [x^k] \prod_{u=1}^n (1 + c_u x)$. By Inclusion-Exclusion:
  $$\text{Ans} = \sum_{k=0}^{n-1} (-1)^k (n - k)! \, [x^k] \prod_{u=1}^n (1 + c_u x) \bmod 998244353$$
  Notice the diagnostic contrast between Regime B and Regime A here: since $c_u$ is a **scalar coefficient** in $(1 + c_u x)$ rather than an exponent in $(1 + x^{c_u})$, D&C subproduct tree computes $\prod_{u=1}^n (1 + c_u x)$ in $O(n \log^2 n)$ time (or, because $\sum_{u=1}^n c_u = n - 1$, there are at most $O(\sqrt{n})$ distinct values of $c_u$, so grouping equal $c_u$'s via binary exponentiation also runs in $O(n \log n)$).

##### Problem 37 (`Advanced` — Iter 14): LibreOJ #6089 — 小 Y 的背包计数问题 (`C2-Pre`)
- **Link**: <https://loj.ac/p/6089>
- **Mathematical Statement**: You have $n$ types of items ($n \le 10^5$). The $i$-th item has weight $i$ and stock limit $i$ (at most $i$ copies can be chosen). For every total weight $1 \le s \le n$, find the number of ways to fill a knapsack of weight $s$ modulo $23333333$ (or $998244353$).
- **Diagnostic Signal**: The generating function is $F(x) = \prod_{i=1}^n \frac{1 - x^{i(i+1)}}{1 - x^i} \bmod x^{n+1}$! Notice that the numerator factors $1 - x^{i(i+1)}$ only matter for $i(i+1) \le n \iff i \le \sqrt{n}$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Write each bounded geometric sum $1 + x^i + x^{2i} + \dots + x^{i^2} = \frac{1 - x^{i(i+1)}}{1 - x^i}$.
  - *Hint 2*: Under modulo $x^{n+1}$, whenever $i(i+1) > n$, we have $x^{i(i+1)} \equiv 0 \pmod{x^{n+1}}$, so the numerator simplifies! Thus $F(x) \equiv \frac{\prod_{i=1}^{\lfloor\sqrt{n}\rfloor} (1 - x^{i(i+1)})}{\prod_{i=1}^n (1 - x^i)} \pmod{x^{n+1}}$.
  - *Hint 3*: When the modulus is NTT-friendly ($998244353$), compute $\ln F(x) = \sum_{i=1}^n \sum_{k \ge 1} \frac{x^{ki}}{k} - \sum_{i=1}^{\lfloor\sqrt{n}\rfloor} \sum_{k \ge 1} \frac{x^{ki(i+1)}}{k}$ in $O(n \log n)$ via the Harmonic Sieve + `poly_exp`! (When the modulus is non-NTT $23333333$, split at $B = \sqrt{n}$: bounded DP for $i < B$ and partition Ferrers-diagram DP for $i \ge B$ in $O(n\sqrt{n})$.)
- **Full Algebraic Derivation**:
  In the FPS $\ln/\exp$ formulation, $F(x) = \prod_{i=1}^n (1 - x^i)^{-1} \prod_{i=1}^{\lfloor\sqrt{n}\rfloor} (1 - x^{i(i+1)}) \bmod x^{n+1}$ is a pure **Regime A** product with $c_w = 1$ for $w \in [1, n]$ and an extra $-1$ for $w = i(i+1) \le n$. The Harmonic Sieve builds $\ln F(x) \bmod x^{n+1}$ in $O(n \log n)$ time, and a single `poly_exp` finishes the problem in $O(n \log n)$.

##### Problem 38 (`Advanced` — Iter 14): LibreOJ #6503 — Magic (`C2-Pre`)
- **Link**: <https://loj.ac/p/6503>
- **Mathematical Statement**: There are $m$ colors of cards ($m \le 10^5$) with counts $a_1, \dots, a_m$ ($\sum a_i = n \le 10^5$). Arrange all $n$ cards in a row; a "magic pair" is an adjacent pair of cards of the same color. Count the number of distinguishable arrangements with **exactly $k$** magic pairs modulo $998244353$.
- **Diagnostic Signal**: If color $i$ is split into $c_i$ maximal monochromatic blocks, it contributes $a_i - c_i$ adjacent same-color pairs. By Inclusion-Exclusion or the **Lah / Laguerre EGF substitution** combined with a subproduct tree / $\ln$-$\exp$ frequency bucket, the EGF per color is $P_i(x, t) = \sum_{c=1}^{a_i} \binom{a_i-1}{c-1} \frac{(x(1-t))^c}{c!} t^{a_i - c}$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: For a single color with $a_i$ identical cards, splitting it into $c$ blocks gives $\binom{a_i-1}{c-1}$ ways and $a_i - c$ magic pairs, with EGF $\frac{x^c}{c!}$ for placing the $c$ blocks into the permutation of blocks.
  - *Hint 2*: Multiply the EGFs over all $m$ colors (using frequency bucketing + $\ln/\exp$ or D&C multiplication in $O(n \log^2 n)$) to obtain the EGF of total blocks $C = \sum c_i$.
  - *Hint 3*: Notice that substituting $y = x(1-t)$ turns the per-color polynomial into $t^{a_i} G_{a_i}\!\left(\frac{x(1-t)}{t}\right)$, so we only need a single-variable polynomial product in $u = \frac{1-t}{t}$, followed by an **Euler / Möbius Transform** $u = \frac{1-t}{t}$ to recover $[t^k]$!
- **Full Algebraic Derivation**:
  For color $i$, choosing $j = a_i - c$ magic pairs (so $c = a_i - j$ blocks remain) has Inclusion-Exclusion / EGF weight $\sum_{j=0}^{a_i-1} \binom{a_i-1}{j} \frac{x^{a_i-j}}{(a_i-j)!} (t-1)^j$. Extracting $[x^C]$ and multiplying by $C!$ gives $\sum_{C=1}^n C! [x^C] \prod_{i=1}^m \left(\sum_{c=1}^{a_i} \binom{a_i-1}{c-1} \frac{x^c}{c!} (t-1)^{a_i-c}\right)$. We compute the product in the variable $w = t-1$ in $O(n \log^2 n)$ via D&C multiplication, then apply **1 Taylor Shift** $w = t - 1$ to extract $[t^k]$ in $O(n \log n)$!

##### Problem 39 (`Mastery` — Iter 14): Lyndon Words, Necklaces & Pólya–Redfield Cycle Index (`Inverse Euler Transform`) (`C1` / `C2-Pre`)
- **Link**: Classic Olympiad / AtCoder / Luogu P4727 & Necklace Synthesis
- **Mathematical Statement**: Given a weight sequence $a_1, \dots, a_N$ counting primitive components of weight $w$ (or conversely given the multiset generating function $F(x) = \prod_{w=1}^N (1 - x^w)^{-a_w} \bmod x^{N+1}$), (1) recover the primitive counts $a_1, \dots, a_N$ in $O(N \log N)$ time, and (2) compute the generating function of unlabeled cyclic necklaces $Z_{\text{cycle}}(x)$ of total weight $\le N$ modulo $998244353$.
- **Diagnostic Signal**: Recovering exponents $a_w$ from an Euler product $\prod (1-x^w)^{-a_w}$ requires **FPS Logarithm + Möbius Inversion** (**Inverse Euler Transform**); counting cyclic necklaces requires the **Pólya–Redfield Cycle Index** $\sum_{k \ge 1} \frac{\varphi(k)}{k} \ln\frac{1}{1 - A(x^k)}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Take $L(x) = \ln F(x) \bmod x^{N+1}$ in $O(N \log N)$. Then $n [x^n] L(x) = \sum_{d \mid n} d\, a_d$.
  - *Hint 2*: Apply Möbius inversion via an $O(N \log N)$ divisor loop: $n\, a_n = \sum_{d \mid n} \mu(n/d) \cdot d [x^d] L(x)$.
  - *Hint 3*: For cyclic necklaces of beads from class $\mathcal{A}$ with OGF $A(x)$ ($A(0)=0$), compute $B(x) = -\ln(1 - A(x)) \bmod x^{N+1}$ once in $O(N \log N)$, and then apply the Harmonic Sieve $Z_{\text{cycle}}(x) = \sum_{k=1}^N \frac{\varphi(k)}{k} B(x^k) \bmod x^{N+1}$ in $O(N \log N)$!
- **Full Algebraic Derivation**:
  Because $B(x) = \ln\frac{1}{1 - A(x)}$ is computed **once** in $O(N \log N)$, evaluating $Z_{\text{cycle}}(x) = \sum_{k=1}^N \frac{\varphi(k)}{k} B(x^k) \bmod x^{N+1}$ only touches $\lfloor N/k \rfloor$ coefficients for each $k$:
  $$[x^n] Z_{\text{cycle}}(x) = \sum_{k \mid n} \frac{\varphi(k)}{k} [x^{n/k}] \ln\frac{1}{1 - A(x)}$$
  which runs in $O(N \log N)$ total time!

---

#### Module E: Iteration 15 / 67 — Roots of Unity Filter, Bluestein's Chirp-Z & Cyclotomic Rings (Problems 40–49)

##### Problem 40 (`Stepping Stone` — Iter 15): LibreOJ #6485 — LJJ 学二项式定理 (`C1` / `C2-New` / `C2-Pre`)
- **Link**: <https://loj.ac/p/6485>
- **Mathematical Statement**: Given $T$ test cases ($T \le 10^5$), where each test case specifies $n \le 10^{18}$, $s \le 10^9$, and four weights $a_0, a_1, a_2, a_3 \in \mathbb{F}_{998244353}$, compute:
  $$S = \left(\sum_{i=0}^n \binom{n}{i} s^i a_{i \bmod 4}\right) \bmod 998244353$$
- **Diagnostic Signal**: Huge binomial index $n \le 10^{18}$ with periodic weight $a_{i \bmod 4}$ of period $m = 4 \mid (998244353 - 1) = 2^{23} \times 7 \times 17$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Split the sum by the residue $r = i \bmod 4 \in \{0, 1, 2, 3\}$ so that $S = \sum_{r=0}^3 a_r \sum_{i \equiv r \pmod 4} \binom{n}{i} s^i$.
  - *Hint 2*: Find a primitive $4$-th root of unity $\omega_4 \equiv 3^{(p-1)/4} \equiv 86583718 \pmod{998244353}$ and apply the Roots of Unity Filter to $F(x) = (1 + sx)^n$.
  - *Hint 3*: Swap the summation order over $r$ and $j$: $\sum_{r=0}^3 a_r \left(\frac{1}{4}\sum_{j=0}^3 \omega_4^{-jr} (1 + s\omega_4^j)^n\right) = \frac{1}{4}\sum_{j=0}^3 (1 + s\omega_4^j)^n \left(\sum_{r=0}^3 a_r \omega_4^{-jr}\right)$.
- **Full Algebraic Derivation**:
  Let $F(x) = \sum_{i=0}^n \binom{n}{i} (sx)^i = (1 + sx)^n$. By the $m=4$ Roots of Unity Filter:
  $$S_r = \sum_{i \equiv r \pmod 4} \binom{n}{i} s^i = \frac{1}{4} \sum_{j=0}^3 \omega_4^{-jr} (1 + s \omega_4^j)^n$$
  where $\omega_4 = 3^{(998244353-1)/4} \bmod 998244353 = 86583718$ (satisfying $\omega_4^2 \equiv -1 \pmod p$). Thus each test case requires only $4$ modular exponentiations $(1 + s\omega_4^j)^{n \bmod (p-1)} \bmod p$, running in $O(T \log p)$ time.

##### Problem 41 (`Stepping Stone` — Iter 15): BZOJ 3328 — PYXFIB (`C2-New`)
- **Link**: <https://darkbzoj.cc/problem/3328>
- **Mathematical Statement**: Given $T$ test cases, where each test case specifies $n \le 10^{18}$, $k \le 2 \times 10^4$, and a prime modulus $p \le 10^9$ guaranteed to satisfy $k \mid (p - 1)$, let $F_0 = 1, F_1 = 1, F_i = F_{i-1} + F_{i-2}$ be the Fibonacci numbers. Compute:
  $$S = \sum_{i=0}^n \binom{n}{i} F_i [k \mid i] \bmod p$$
- **Diagnostic Signal**: A binomial-weighted linear recurrence $\sum_{i=0}^n \binom{n}{i} F_i [k \mid i]$ where the index $i$ is filtered by $k \mid i$ and $k \mid (p-1)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Replace the scalar Fibonacci number $F_i$ with the entry $[M^i]_{0,0}$ of the $2 \times 2$ Fibonacci transition matrix $M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.
  - *Hint 2*: By the binomial theorem in the matrix ring $\operatorname{Mat}_2(\mathbb{F}_p)[x]$, the matrix generating function is $\sum_{i=0}^n \binom{n}{i} M^i x^i = (I + xM)^n$.
  - *Hint 3*: Apply the $k$-th Roots of Unity Filter to $F(x) = (I + xM)^n$: $\sum_{k \mid i} \binom{n}{i} M^i = \frac{1}{k}\sum_{j=0}^{k-1} (I + \omega_k^j M)^n$. Optional speedup: if $5$ is a quadratic residue modulo $p$, diagonalize $M$ first to replace $2 \times 2$ matrix exponentiation with scalar exponentiation!
- **Full Algebraic Derivation**:
  Let $\omega_k = g^{(p-1)/k} \bmod p$ be a primitive $k$-th root of unity in $\mathbb{F}_p$. Applying the Roots of Unity Filter to the matrix polynomial $P(x) = (I + xM)^n = \sum_{i=0}^n \binom{n}{i} M^i x^i$ yields:
  $$S = \left[ \frac{1}{k} \sum_{j=0}^{k-1} \left(I + \omega_k^j \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}\right)^n \right]_{0,0} \bmod p$$
  Computing $(I + \omega_k^j M)^n$ for each $j \in [0, k-1]$ via $2 \times 2$ binary matrix exponentiation takes $O(k \log n)$ per testcase.

##### Problem 42 (`Intermediate` — Iter 15): Luogu P3702 — [SDOI2017] 序列计数 (`C2-New`)
- **Link**: <https://www.luogu.com.cn/problem/P3702>
- **Mathematical Statement**: Count the number of sequences $(a_1, a_2, \dots, a_n)$ of length $n$ ($1 \le n \le 10^7$) with elements in $\{1, 2, \dots, m\}$ ($1 \le m \le 2 \times 10^7$) such that:
  1. At least one $a_i$ is a prime number;
  2. $a_1 + a_2 + \dots + a_n \equiv 0 \pmod p$ ($1 \le p \le 100$).
  Output the answer modulo $20170408$.
- **Diagnostic Signal**: Sum modulo $p \le 100$ under an unnatural modulus $M = 20170408 = 2^3 \times 2521301$ where $p \nmid \varphi(M)$ (and $M$ is not even prime!). This triggers **Fallback 1 (Cyclic Quotient Ring $R[x]/(x^p - 1)$)**.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Handle "at least one prime" by complementary counting: $(\text{All valid sequences}) - (\text{Valid sequences using only non-primes})$.
  - *Hint 2*: Since $20170408$ does not admit $p$-th roots of unity, work directly in the quotient ring $\mathbb{Z}_{20170408}[x]/(x^p - 1)$. What is the single-step generating polynomial $A(x) \bmod (x^p - 1)$?
  - *Hint 3*: Sieve primes up to $m$ in $O(m)$ using a linear Euler sieve. Form $A_{\text{all}}(x) = \sum_{v=1}^m x^{v \bmod p}$ and $A_{\text{comp}}(x) = \sum_{v \in [1,m]\setminus \mathbb{P}} x^{v \bmod p}$, and compute $[x^0]\big(A_{\text{all}}(x)^n - A_{\text{comp}}(x)^n\big) \bmod (x^p - 1)$ via binary exponentiation with naive $O(p^2)$ cyclic convolution.
- **Full Algebraic Derivation**:
  1. **Linear Sieve**: Run a linear sieve up to $m \le 2 \times 10^7$ in $O(m)$ time to classify each $v \in [1, m]$ as prime or non-prime ($1$ is non-prime).
  2. **Quotient Ring Construction**: Accumulate degree-$<p$ polynomials $A_{\text{all}}(x) = \sum_{r=0}^{p-1} c_r x^r$ and $A_{\text{comp}}(x) = \sum_{r=0}^{p-1} d_r x^r$, where $c_r = |\{v \in [1, m] : v \equiv r \pmod p\}|$ and $d_r = |\{v \in [1, m] \setminus \mathbb{P} : v \equiv r \pmod p\}|$.
  3. **Cyclic Binary Exponentiation**: In $\mathbb{Z}_{20170408}[x]/(x^p - 1)$, multiplication of two polynomials $U, V$ of degree $< p$ is $(U \circledast V)_k = \sum_{i=0}^{p-1} U_i V_{(k - i) \bmod p} \bmod 20170408$ in $O(p^2)$ time. Raising $A_{\text{all}}(x)$ and $A_{\text{comp}}(x)$ to the $n$-th power takes $O(p^2 \log n)$ operations. Total complexity: $O(m + p^2 \log n)$, well within the $1.0\text{ s}$ limit.

##### Problem 43 (`Intermediate` — Iter 15): AtCoder ABC 240 G — Teleporting Takahashi (`C2-New`)
- **Link**: <https://atcoder.jp/contests/abc240/tasks/abc240_g>
- **Mathematical Statement**: Starting at $(0, 0, 0) \in \mathbb{Z}^3$, in each of $N$ steps ($N \le 10^7$) you move by one of the $6$ unit vectors $\{\pm e_1, \pm e_2, \pm e_3\}$. Find the number of $N$-step walks ending at $(X, Y, Z)$ ($|X|, |Y|, |Z| \le 10^7$) modulo $998244353$.
- **Diagnostic Signal**: 3D lattice walk with $N \le 10^7$: 3D does not decouple into 3 independent 1D walks, so we decouple 2D via the Chebyshev $45^\circ$ rotation $(x \pm y)$ and sum over the remaining 1D coordinate $z$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: For a 2D walk of $M$ steps along $\{\pm e_1, \pm e_2\}$ ending at $(X, Y)$, apply the substitution $u = x + y, v = x - y$: $(x + x^{-1} + y + y^{-1})^M = (x^{1/2}y^{1/2} + x^{-1/2}y^{-1/2})^M (x^{1/2}y^{-1/2} + x^{-1/2}y^{1/2})^M$.
  - *Hint 2*: This proves that the number of $M$-step 2D walks to $(X, Y)$ is $\binom{M}{\frac{M + X + Y}{2}} \binom{M}{\frac{M + X - Y}{2}}$ whenever $M \equiv X + Y \pmod 2$ and $|X| + |Y| \le M$.
  - *Hint 3*: Fix the number of $Z$-axis steps $k = a + b$ ($|Z| \le k \le N$, $k \equiv |Z| \pmod 2$), where $a = \frac{k+Z}{2}$ steps are $+e_3$ and $b = \frac{k-Z}{2}$ steps are $-e_3$. The remaining $M = N - k$ steps form a 2D walk to $(X, Y)$.
- **Full Algebraic Derivation**:
  The 3D step polynomial is $(x + x^{-1} + y + y^{-1} + z + z^{-1})^N$. Separating $(z + z^{-1})$ from $(x + x^{-1} + y + y^{-1})$ via the binomial theorem:
  $$[x^X y^Y z^Z](x + x^{-1} + y + y^{-1} + z + z^{-1})^N = \sum_{k=0}^N \binom{N}{k} [z^Z](z + z^{-1})^k \cdot [x^X y^Y](x + x^{-1} + y + y^{-1})^{N-k}$$
  Using the 2D $45^\circ$ diagonal decoupling $[x^X y^Y](x + x^{-1} + y + y^{-1})^M = \binom{M}{\frac{M+X+Y}{2}}\binom{M}{\frac{M+X-Y}{2}}$ and $[z^Z](z + z^{-1})^k = \binom{k}{\frac{k+Z}{2}}$, we obtain the single-sum $O(N)$ formula:
  $$\text{Ans} = \sum_{\substack{k = |Z| \\ k \equiv Z \pmod 2}}^{N - |X| - |Y|} \binom{N}{k} \binom{k}{\frac{k+Z}{2}} \binom{N-k}{\frac{N-k+X+Y}{2}} \binom{N-k}{\frac{N-k+X-Y}{2}} \bmod 998244353$$

##### Problem 44 (`Intermediate` — Iter 15): UOJ #450 — [集训队作业2018 / UNR #3] 复读机 (Repeater) (`C2-Pre`)
- **Link**: <https://uoj.ac/problem/450>
- **Mathematical Statement**: Count the number of sequences of length $n$ ($n \le 10^9$) over an alphabet of $k$ distinct characters ($k \le 5 \times 10^5$) such that the multiplicity of every character is divisible by $d$ ($d \in \{1, 2, 3\}$), modulo the prime $p = 19491001$.
- **Diagnostic Signal**: Labeled sequence counting (EGF) where each of the $k$ alphabet symbols has multiplicity $\equiv 0 \pmod d$, and the prime modulus $p = 19491001$ satisfies $p - 1 = 19491000 = 2^3 \times 3^4 \times 5^3 \times 241$ so $3 \mid (p - 1)$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: By the Roots of Unity Filter applied to $e^x$, the EGF for a single character whose count is divisible by $d$ is $G_d(x) = \frac{1}{d}\sum_{j=0}^{d-1} e^{\omega_d^j x}$, so the answer for $k$ characters is $n! [x^n] G_d(x)^k$.
  - *Hint 2*: For $d = 1$, $G_1(x)^k = e^{kx} \implies \text{Ans} = k^n \bmod p$. For $d = 2$, $G_2(x)^k = 2^{-k} (e^x + e^{-x})^k = 2^{-k} \sum_{i=0}^k \binom{k}{i} e^{(2i - k)x}$, which takes $O(k \log n)$ time!
  - *Hint 3*: For $d = 3$, find a primitive cube root of unity $\omega = 7^{(p-1)/3} \bmod 19491001 = 6630404$. Since $G_3(x)^k = 3^{-k} (e^x + e^{\omega x} + e^{\omega^2 x})^k$, expand the trinomial in $O(k^2 \log n)$ for the $k \le 1000$ subtask, or use the D-finite / P-recursive differential equation of $e^x + e^{\omega x} + e^{\omega^2 x}$ to compute all trinomial coefficients in $O(k \log n)$ for $k \le 5 \times 10^5$!
- **Full Algebraic Derivation**:
  1. **Primitive Root of Unity in $\mathbb{F}_{19491001}$**: Since $19491001 - 1 = 19491000$ is divisible by $3$ and $7$ is a primitive root modulo $19491001$, $\omega = 7^{19491000/3} \equiv 6630404 \pmod{19491001}$ is a primitive $3$-rd root of unity.
  2. **Case $d = 2$ ($k \le 5 \times 10^5$)**:
     $$\text{Ans} = n! [x^n] \left(\frac{e^x + e^{-x}}{2}\right)^k = 2^{-k} \sum_{i=0}^k \binom{k}{i} (2i - k)^n \bmod p$$
     which is evaluated in $O(k \log n)$ time.
  3. **Case $d = 3$ ($k \le 1000$ via Trinomial Expansion, or $k \le 5 \times 10^5$ via ODE)**:
     $$\text{Ans} = n! [x^n] \left(\frac{e^x + e^{\omega x} + e^{\omega^2 x}}{3}\right)^k = 3^{-k} \sum_{i=0}^k \sum_{j=0}^{k-i} \frac{k!}{i!\, j!\, (k - i - j)!} \left(i + j\omega + (k - i - j)\omega^2\right)^n \bmod p$$
     which runs in $O(k^2 \log n)$ time directly (or $O(k \log n)$ by projecting $j\omega + (k-i-j)\omega^2 \equiv (j - k + i + j)\omega - (k - i - j) \pmod{1 + \omega + \omega^2 = 0}$ into the 2D basis $A + B\omega$ and using the ODE of $(1 + y + y^2)^k$).

##### Problem 45 (`Advanced` — Iter 15): Codeforces 891E — Lust (and the Floor-Sum Variant) (`C1`)
- **Link**: <https://codeforces.com/problemset/problem/891/E>
- **Mathematical Statement**: Given an array $a_1, a_2, \dots, a_n$ ($n \le 5000, a_i \le 10^9$) and $k \le 10^9$ operations, in each operation an index $i \in \{1, \dots, n\}$ is chosen uniformly at random and $a_i$ is decremented by $1$. Compute the expected value of $\prod_{i=1}^n a_i^{\text{init}} - \prod_{i=1}^n a_i^{\text{final}}$ modulo $10^9 + 7$. Furthermore, show how the **Floor-Sum Trick** generalizes this to sums of the form $\sum_{i=0}^k \binom{k}{i} \lfloor i/m \rfloor s^i$.
- **Diagnostic Signal**: Expected product after $k$ multinomial decrements ($k \le 10^9, n \le 5000$) requiring EGF product collapse + the Floor-Sum identity $\lfloor i/m \rfloor = \frac{i - (i \bmod m)}{m}$ when floor weights appear.
- **3-Tier Progressive Hints**:
  - *Hint 1*: If element $i$ is decremented $c_i$ times ($\sum c_i = k$), the final product is $\prod_{i=1}^n (a_i - c_i)$ with multinomial probability $\frac{k!}{n^k \prod c_i!}$.
  - *Hint 2*: Form the EGF of each factor: $\sum_{c \ge 0} (a_i - c) \frac{x^c}{c!} = (a_i - x) e^x$. Thus the EGF of the total product over all $n$ elements is $e^{nx} \prod_{i=1}^n (a_i - x)$.
  - *Hint 3*: Expand $P(x) = \prod_{i=1}^n (a_i - x) = \sum_{j=0}^n b_j x^j$ in $O(n^2)$. Then $\mathbb{E}[\prod a_i^{\text{final}}] = \frac{k!}{n^k} [x^k] e^{nx} P(x) = \sum_{j=0}^{\min(n,k)} b_j \frac{k^{\underline{j}}}{n^j}$. For the floor-sum variant $\sum_{i=0}^k \lfloor i/m \rfloor [x^i] F(x)$, substitute $\lfloor i/m \rfloor = \frac{i - \sum_{r=0}^{m-1} r [i \equiv r \pmod m]}{m}$ to reduce to $xF'(x)$ plus a Roots of Unity Filter!
- **Full Algebraic Derivation**:
  1. **EGF Product Collapse**:
     $$\mathbb{E}\left[\prod_{i=1}^n (a_i - c_i)\right] = \frac{k!}{n^k} [x^k] \prod_{i=1}^n \left(\sum_{c_i \ge 0} (a_i - c_i) \frac{x^{c_i}}{c_i!}\right) = \frac{k!}{n^k} [x^k] \left(e^{nx} \prod_{i=1}^n (a_i - x)\right)$$
     Computing $P(x) = \prod_{i=1}^n (a_i - x) = \sum_{j=0}^n b_j x^j$ takes $O(n^2)$ time. Extracting $[x^k]$ from $e^{nx} x^j$ gives $\frac{n^{k-j}}{(k-j)!}$, so $\mathbb{E}[\prod a_i^{\text{final}}] = \sum_{j=0}^n b_j \frac{k^{\underline{j}}}{n^j}$ in $O(n^2)$ total time.
  2. **Floor-Sum Generalization**: Whenever a problem asks for $\sum_{i=0}^k \lfloor i/m \rfloor f_i$, write $\lfloor i/m \rfloor = \frac{i - (i \bmod m)}{m}$. The first term $\frac{1}{m}\sum i f_i = \frac{1}{m}\vartheta F(1)$ is handled by the differential operator $\vartheta = x\frac{d}{dx}$, and the second term $-\frac{1}{m}\sum_{r=1}^{m-1} r \sum_{i \equiv r \pmod m} f_i$ is handled by an $m$-th Roots of Unity Filter (as executed in Problem 46 below).

##### Problem 46 (`Advanced` — Iter 15): Luogu P5591 — 小猪佩奇学数学 (Peppa Pig Learns Math) (`C1`)
- **Link**: <https://www.luogu.com.cn/problem/P5591>
- **Mathematical Statement**: Given $n, p \in [1, 998244352]$ and $k = 2^m$ ($0 \le m \le 20$, so $k \le 2^{20}$ and $k \mid 998244352$), compute:
  $$S = \sum_{i=0}^n \binom{n}{i} p^i \left\lfloor \frac{i}{k} \right\rfloor \bmod 998244353$$
- **Diagnostic Signal**: Binomial sum weighted by $\lfloor i/k \rfloor$ where $k = 2^m \le 2^{20}$: decomposing $\lfloor i/k \rfloor = \frac{i - (i \bmod k)}{k}$ and exchanging the summation order in the Roots of Unity Filter collapses a naive $O(k^2)$ double sum into an $O(k \log n)$ closed-form sum via the **Geometric Derivative Trick** of Section 7.4!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Substitute $\left\lfloor \frac{i}{k} \right\rfloor = \frac{i - (i \bmod k)}{k}$ to split $S = \frac{1}{k}\left(\sum_{i=0}^n i \binom{n}{i} p^i - \sum_{r=1}^{k-1} r \sum_{i \equiv r \pmod k} \binom{n}{i} p^i\right)$.
  - *Hint 2*: The first sum is $n p (1 + p)^{n-1}$. In the second sum, expand $\sum_{i \equiv r \pmod k} \binom{n}{i} p^i = \frac{1}{k}\sum_{j=0}^{k-1} \omega_k^{-jr} (1 + p\omega_k^j)^n$ and **swap the summation order** of $r$ and $j$!
  - *Hint 3*: For $j = 0$, $\sum_{r=1}^{k-1} r = \frac{k(k-1)}{2}$. For $1 \le j \le k-1$, since $\omega_k^{-j} \neq 1$ and $\omega_k^{-jk} = 1$, the inner sum $\sum_{r=1}^{k-1} r \omega_k^{-jr}$ collapses to $\frac{k}{\omega_k^{-j} - 1}$!
- **Full Algebraic Derivation**:
  Using the identity $\sum_{r=1}^{k-1} r q^r = \frac{k}{q - 1}$ for any $k$-th root of unity $q = \omega_k^{-j} \neq 1$:
  $$\sum_{r=1}^{k-1} r \sum_{i \equiv r \pmod k} \binom{n}{i} p^i = \frac{1}{k}\sum_{j=0}^{k-1} (1 + p\omega_k^j)^n \sum_{r=1}^{k-1} r \omega_k^{-jr} = \frac{k-1}{2}(1 + p)^n + \sum_{j=1}^{k-1} \frac{(1 + p\omega_k^j)^n}{\omega_k^{-j} - 1}$$
  Substituting this back into $S = \frac{1}{k}\left(np(1+p)^{n-1} - \sum_{r=1}^{k-1} r S_r\right)$ yields the single-loop $O(k \log n)$ formula:
  $$S = \frac{1}{k}\left(n p (1 + p)^{n-1} - \frac{k-1}{2}(1 + p)^n - \sum_{j=1}^{k-1} \frac{(1 + p\omega_k^j)^n}{\omega_k^{-j} - 1}\right) \bmod 998244353$$

##### Problem 47 (`Advanced` — Iter 15): AtCoder FPS-24 R — Random Walk (`C1`)
- **Link**: <https://atcoder.jp/contests/fps-24/tasks/fps_24_r>
- **Mathematical Statement**: Consider a path graph with $2^N + 1$ vertices numbered $0, 1, \dots, 2^N$ ($N \le 20$). A particle starts at vertex $X$ and takes $T$ steps ($T \le 10^{18}$): at an internal vertex $0 < v < 2^N$, it moves to $v - 1$ or $v + 1$ each with probability $1/2$; at the boundary endpoints $v = 0$ and $v = 2^N$, it deterministically reflects to $1$ and $2^N - 1$ respectively. Compute the probability of ending at vertex $Y$ after $T$ steps modulo $998244353$, and also analyze the general cyclic random walk on $\mathbb{Z}_m$ when $m \mid (p-1)$ vs. $m \nmid (p-1)$.
- **Diagnostic Signal**: Reflecting boundaries at $0$ and $2^N$ unfold via the **Method of Images / Quotient Projection** $\pi : \mathbb{Z}_{2^{N+1}} \to \{0, 1, \dots, 2^N\}$, $\pi(y) = \min(y, 2^{N+1} - y)$, reducing the walk on a reflecting path of length $2^N$ to a standard symmetric random walk on the cycle $\mathbb{Z}_{2^{N+1}}$ of length $M = 2^{N+1} \mid (998244353 - 1)$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Unfold the path $\{0, 1, \dots, 2^N\}$ into the cycle $\mathbb{Z}_M$ of length $M = 2^{N+1}$ via the folding map $\pi(y) = \min(y, M - y)$. Verify that at $y = 0$, moving to $\pm 1 \bmod M$ both project under $\pi$ to $1$, matching the deterministic reflection at the boundary!
  - *Hint 2*: Thus the probability of landing at $Y \in \{0, \dots, 2^N\}$ on the path equals the sum of probabilities of landing at the preimages $\pi^{-1}(Y) \subseteq \mathbb{Z}_M$ on the cycle (which is $\{Y\}$ if $Y \in \{0, 2^N\}$, and $\{Y, M - Y\}$ if $0 < Y < 2^N$).
  - *Hint 3*: On the cycle $\mathbb{Z}_M$ ($M = 2^{N+1} \le 2^{21}$), the generating function is $2^{-T} x^X (x + x^{-1})^T \bmod (x^M - 1)$. Apply the **Roots of Unity Filter** of order $M = 2^{N+1}$: $[x^r] = \frac{1}{M}\sum_{j=0}^{M-1} \omega_M^{j(X - r)} (\omega_M^j + \omega_M^{-j})^T$ in $O(2^N \log T)$ time!
- **Full Algebraic Derivation**:
  1. **Official Reflecting Path Solution ($M = 2^{N+1} \mid 998244352$)**: Let $\omega = 3^{(p-1)/M} \bmod p$. For any target residue $r \in \mathbb{Z}_M$, the cycle walk probability after $T$ steps starting from $X$ is:
     $$P_{\text{cycle}}(X \to r) = \frac{1}{M \cdot 2^T} \sum_{j=0}^{M-1} \omega^{j(X - r)} (\omega^j + \omega^{-j})^T \bmod 998244353$$
     Summing $P_{\text{cycle}}(X \to r)$ over $r \in \pi^{-1}(Y)$ gives the exact answer in $O(2^N \log T)$ time.
  2. **General Cycle $\mathbb{Z}_m$ Extension**:
     - **Case 1 ($m \mid (p-1)$, all $r \in [0, m-1]$ requested)**: Compute $y_j = S(\omega_m^j)^T \bmod p$ for $j = 0, \dots, m-1$ in $O(m \log T)$, then apply **Bluestein's Chirp-Z Transform** (`bluestein_roots_filter`) to evaluate $c_r = \frac{1}{m}\sum_{j=0}^{m-1} y_j \omega_m^{-jr}$ for all $r$ simultaneously in $O(m \log m)$ time.
     - **Case 2 ($m \nmid (p-1)$)**: Compute $S(x)^T \bmod (x^m - 1)$ directly in $\mathbb{F}_p[x]/(x^m - 1)$ via binary exponentiation + NTT with cyclic folding in $O(m \log m \log T)$ time.

##### Problem 48 (`Mastery` — Iter 15): Luogu P5293 — [HNOI2019] 白兔之舞 (Dance of the White Rabbit) (`C1` / `C2-New` / `C2-Pre`)
- **Link**: <https://www.luogu.com.cn/problem/P5293>
- **Mathematical Statement**: Given an $n \times n$ transition matrix $W$ ($1 \le n \le 3$), a walk bound $L \le 10^9$, start/end vertices $x, y \in \{1, \dots, n\}$, a step modulus $k \le 65536$, and a prime modulus $p$ ($p \le 2^{30}$, guaranteed $k \mid (p - 1)$), compute for every $t \in \{0, 1, \dots, k-1\}$:
  $$\text{Ans}_t = \left(\sum_{\substack{0 \le i \le L \\ i \equiv t \pmod k}} \binom{L}{i} [W^i]_{x, y}\right) \bmod p$$
- **Diagnostic Signal**: Simultaneous multi-residue Roots of Unity Filter for all $t \in [0, k-1]$ with matrix transition $W^i$, arbitrary divisor $k \le 65536$ ($k \mid p-1$, not necessarily a power of $2$), and an arbitrary prime modulus $p \le 2^{30}$ (requiring MTT / 3-prime NTT inside Bluestein's Chirp-Z Transform).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Recognize $\sum_{i=0}^L \binom{L}{i} W^i z^i = (I + zW)^L$ in the matrix ring $\operatorname{Mat}_n(\mathbb{F}_p)[z]$.
  - *Hint 2*: By the $k$-th Roots of Unity Filter, $\text{Ans}_t = \frac{1}{k}\sum_{j=0}^{k-1} \omega_k^{-jt} y_j$, where $y_j = \big[(I + \omega_k^j W)^L\big]_{x,y}$ and $\omega_k = g^{(p-1)/k} \bmod p$. Computing all $y_j$ takes $O(n^3 k \log L)$ time.
  - *Hint 3*: To evaluate $\text{Ans}_t = \frac{1}{k}\sum_{j=0}^{k-1} y_j \omega_k^{-jt}$ for all $t \in [0, k-1]$ in $O(k \log k)$ time when $k$ is not a power of $2$, substitute $-jt = \binom{j}{2} + \binom{t}{2} - \binom{j+t}{2}$ (**Bluestein's Chirp-Z Transform**) and convolve via a 3-prime NTT / MTT since $p$ is arbitrary.
- **Full Algebraic Derivation**:
  1. **Primitive Root & Point Evaluations**: Factor $p - 1$ to find a primitive root $g \bmod p$, and set $\omega = g^{(p-1)/k} \bmod p$. For each $j = 0, \dots, k-1$, compute the scalar $y_j = \big[(I + \omega^j W)^L\big]_{x,y} \bmod p$ using $n \times n$ matrix binary exponentiation in $O(n^3 k \log L)$ time ($3^3 \times 65536 \times 30 \approx 5.3 \times 10^7$ ops).
  2. **Bluestein's Chirp-Z Transform**: Using the identity $-jt = \binom{j}{2} + \binom{t}{2} - \binom{j+t}{2}$, rewrite the inverse DFT:
     $$\text{Ans}_t = \frac{1}{k} \omega^{\binom{t}{2}} \sum_{j=0}^{k-1} \left(y_j \omega^{\binom{j}{2}}\right) \omega^{-\binom{j+t}{2}} \bmod p$$
  3. **Arbitrary-Modulus Convolution**: Let $A_j = y_j \omega^{\binom{j}{2}} \bmod p$ for $j \in [0, k-1]$ and $B_m = \omega^{-\binom{m}{2}} \bmod p$ for $m \in [0, 2k-2]$. Reversing $A$ reduces the sum $\sum_{j=0}^{k-1} A_j B_{j+t}$ to a standard polynomial convolution of length $3k$, which is evaluated modulo $p$ via 3-prime NTT (or split-radix FFT / MTT) in $O(k \log k)$ time. Total time: $O(n^3 k \log L + k \log k)$.

##### Problem 49 (`Mastery` — Iter 15): Codeforces 1054H — Epic Convolution (`C2-New` / `C2-Pre`)
- **Link**: <https://codeforces.com/problemset/problem/1054/H>
- **Mathematical Statement**: Given two arrays $a_0, \dots, a_{n-1}$ and $b_0, \dots, b_{m-1}$ ($n, m \le 10^5$) and a base $c \in \mathbb{F}_{490019}$, compute:
  $$S = \left(\sum_{i=0}^{n-1} \sum_{j=0}^{m-1} a_i b_j c^{i^2 j^3}\right) \bmod 490019$$
- **Diagnostic Signal**: Non-linear exponent $c^{i^2 j^3} \bmod P$ where $P = 490019$ is prime and $P - 1 = 490018 = 2 \times 491 \times 499$ is a product of small primes!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Since $c^e \bmod P$ only depends on the exponent $e = i^2 j^3 \bmod (P - 1)$, reduce $i^2 \bmod (P-1)$ and $j^3 \bmod (P-1)$ first to compress the arrays into lengths $\le P - 1$.
  - *Hint 2*: Approach A (Direct Bluestein): Rewrite $i^2 j^3 = (i^2)(j^3)$ using Bluestein's identity $XY = \binom{X+Y}{2} - \binom{X}{2} - \binom{Y}{2} \pmod{P-1}$, requiring a convolution of length $2(P-1) \approx 9.8 \times 10^5$. Approach B (CRT + Discrete Log): Factor $P - 1 = 2 \times 491 \times 499$; modulo each prime factor $q \in \{491, 499\}$, non-zero residues form a cyclic group $\mathbb{Z}_{q-1}$ generated by a primitive root!
  - *Hint 3*: Using CRT on $P - 1 = 2 \times 491 \times 499$, every index $(u \bmod 2, x \bmod 491, y \bmod 499)$ with $x \neq 0, y \neq 0$ can be written as $(u, g_1^{\alpha} \bmod 491, g_2^{\beta} \bmod 499)$. Then multiplication $x \cdot x' \bmod 491$ and $y \cdot y' \bmod 499$ becomes a 3D cyclic convolution of size $2 \times 490 \times 498 = 488,040$, computed via a single FFT!
- **Full Algebraic Derivation**:
  1. **Exponent Compression**: Accumulate $A[(i^2) \bmod 490018] \mathrel{+}= a_i$ and $B[(j^3) \bmod 490018] \mathrel{+}= b_j$.
  2. **Method 1 (1D Bluestein's Chirp-Z of size $2(P-1)$)**: Since $c^{XY} = c^{\binom{X+Y}{2}} c^{-\binom{X}{2}} c^{-\binom{Y}{2}} \pmod P$ where each binomial coefficient $\binom{k}{2} = \frac{k(k-1)}{2}$ is an integer reduced modulo $P - 1 = 490018$:
     $$S = \sum_{X=0}^{P-2} \sum_{Y=0}^{P-2} \left(A[X] c^{-\binom{X}{2}}\right) \left(B[Y] c^{-\binom{Y}{2}}\right) c^{\binom{X+Y}{2}} \bmod P$$
     This reduces directly to a single 1D convolution of size $2 \times 490018 \approx 9.8 \times 10^5$.
  3. **Method 2 (CRT + 3D FFT of size $2 \times 490 \times 498$)**: By CRT, $X \bmod 490018 \leftrightarrow (X \bmod 2, X \bmod 491, X \bmod 499)$. Handle the boundary cases $491 \mid X$ or $499 \mid X$ separately in $O(P)$ time. For $x = X \bmod 491 \neq 0$ and $y = X \bmod 499 \neq 0$, write $x \equiv g_{491}^\alpha \pmod{491}$ and $y \equiv g_{499}^\beta \pmod{499}$. Then $XY \bmod 490018$ corresponds to $(\text{AND on }\bmod 2, \alpha_1 + \alpha_2 \bmod 490, \beta_1 + \beta_2 \bmod 498)$, which is evaluated in a single convolution of length $2 \times 980 \times 996 < 2^{21}$ in $O(P \log P)$ time.

---

## 11. Cohort 3 Master Reconciliation & Verification Checklist

- [x] **100% Three-Way Read Verification**: Read every line of `iter_11_to_15_substitutions_transforms.md` (`C1`), `cohort2_new_iter_63_to_67_substitutions_transforms.md` (`C2-New`), and `cohort2_iter_63_to_67_substitutions_transforms.md` (`C2-Pre`).
- [x] **Cross-Cohort Blind-Spot Audit Complete**: Explicitly documented and merged all unique insights caught by individual cohorts (including `C2-New`'s Formal Residue Change-of-Variables theorem, characteristic $p=2$ Artin–Schreier collapse for quadratic radicals, Chebyshev Model I vs. Model II distinction, 2D $\mathbb{Q}(\zeta_{12})$ decoupling, 5-row Falling-Factorial basis matrix, and Newton–Girard $p \le N$ asymmetry; `C1`'s Krawtchouk involution proof, Stirling D&C row generation, and Floor-Sum Trick; and `C2-Pre`'s production C++20 implementations).
- [x] **18-Row Unified Operator Lookup Table & Production C++20 Library**: Compiled all non-linear substitutions, differential transforms, and sequence transforms into a single master reference table accompanied by clean, self-contained C++20 templates (`poly_taylor_shift`, `mobius_transform`, `bostan_mori_poly_mod`, `krawtchouk_transform`, `stirling_2nd_row`, `falling_factorial_point_values`, `point_values_to_falling_factorial`, `falling_factorial_mul`, `euler_multiset_transform`, `pow_sum_from_roots`, `bluestein_roots_filter`).
- [x] **Multilingual Bibliography (`[EN]`, `[ZH]`, `[JA]`)**: Reconciled 29 primary sources across English, Chinese, and Japanese competitive programming and analytic combinatorics literature.
- [x] **49 Curated Problems Across All 5 Iterations & All 4 Difficulty Tiers**: Every problem includes a self-contained mathematical statement, exact constraints, clickable source URL, diagnostic signal, 3-tier progressive hints, and full algebraic/algorithmic derivation, with 12 boilerplate template problems explicitly segregated into the Rejected Template Problems table.
- [x] **Strict LaTeX Formatting**: Enforced `$...$` and `$$...$$` math delimiters throughout the entire master file.
