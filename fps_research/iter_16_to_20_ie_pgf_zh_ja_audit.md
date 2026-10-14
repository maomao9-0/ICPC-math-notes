# Cohort 1 — Wave 2B (Iterations 16–20): Inclusion–Exclusion in Generating Functions, Goulden–Jackson Cluster Method, Probability Generating Functions, Stopping Times, and `[ZH]`/`[JA]` Deep-Dive Audit

> **Scope & Cohort Attribution**: Cohort 1 Primary Investigation — Wave 2B (Iterations 16–20)
> **Target Coverage**: Bivariate Inclusion–Exclusion ($y \mapsto y-1$ Taylor shift), Adjacent-Violation Cluster ("Smearing") PIE, Carlitz–Scoville–Vaughan / Smirnov Transformation, Forbidden Substrings & The Goulden–Jackson Cluster Method, Probability Generating Functions (PGFs), Stopping Times $F'(1)$ & $F''(1)$, Penney's Game & String Hitting Times, First-Passage Renewal Division $H_{s\to t}(x)/H_{t\to t}(x)$ & Pole Cancellation at $x=1$, EGF-to-OGF Renewal Bridge, Martingale Potential Duality, and `[ZH]`/`[JA]` Multilingual Literature & Cross-Judge Problem Audit.

---

## Iteration 16: Inclusion–Exclusion in Generating Functions, Adjacent-Violation Cluster PIE, and the Goulden–Jackson Cluster Method

### 16.1 Exact-$k$ vs. At-Least-$k$ Binomial Inversion as Polynomial Taylor Shift

#### Concrete Objects & Question Answered
Suppose we have a finite universe $\Omega$ of combinatorial configurations (for instance, permutations of $n$ elements, $n$-step walks, or colourings of a graph) and a family of $m$ "bad" properties (or violations) $P_1, P_2, \dots, P_m$. For each configuration $\omega \in \Omega$, let $v(\omega) \in \{0, 1, \dots, m\}$ denote the exact number of bad properties that $\omega$ satisfies.
- **Concrete target sequence**: $a_k$ is the number (or total weight) of configurations $\omega \in \Omega$ that violate **exactly** $k$ properties ($v(\omega) = k$). Its ordinary generating function (OGF) in an auxiliary indeterminate $y$ is
  $$A(y) = \sum_{k=0}^m a_k y^k \in \mathbb{Q}[y].$$
- **Relaxed ("chosen-violation") sequence**: Usually, enforcing that a configuration does *not* satisfy the remaining $m-k$ properties destroys product structure, whereas choosing a subset $S \subseteq \{1,\dots,m\}$ of $|S|=j$ properties, requiring $\omega$ to satisfy all properties in $S$, and leaving the remaining $m-j$ properties completely unconstrained ("at least $j$ violations, with $j$ distinguished") is easy to count via a generating function in $x$. Let $b_j$ be the total weight of pairs $(\omega, S)$ where $|S|=j$ and $\omega$ satisfies every property in $S$, with OGF
  $$B(y) = \sum_{j=0}^m b_j y^j \in \mathbb{Q}[y].$$

**Question answered**: How do we recover the exact-violation polynomial $A(y)$ from the relaxed chosen-violation polynomial $B(y)$ algebraically, and how does this translate into an $O(m \log m)$ polynomial algorithm?

#### Step-by-Step Double-Count Derivation
Every configuration $\omega \in \Omega$ with **exact** violation count $v(\omega) = i$ contains $\binom{i}{j}$ subsets $S$ of size $j$ of violated properties. Therefore, in the sum defining $b_j$, each such $\omega$ is counted $\binom{i}{j}$ times:
$$b_j = \sum_{i=j}^m \binom{i}{j} a_i.$$
Multiply by $y^j$ and sum over $0 \le j \le m$, exchanging the order of summation:
$$\begin{aligned}
B(y) = \sum_{j=0}^m b_j y^j
&= \sum_{j=0}^m y^j \sum_{i=j}^m \binom{i}{j} a_i \\
&= \sum_{i=0}^m a_i \sum_{j=0}^i \binom{i}{j} y^j \cdot 1^{i-j} \\
&= \sum_{i=0}^m a_i (y + 1)^i = A(y + 1).
\end{aligned}$$
Here each inner summand $\binom{i}{j} y^j$ assigns weight $y$ to the $j$ *distinguished* violations in $S$ and weight $1$ to the $i-j$ *undistinguished* actual violations not in $S$. Because $y \mapsto y + 1$ is an invertible ring automorphism of $K[y]$, substituting $y \leftarrow y - 1$ immediately inverts the relation:
$$A(y) = B(y - 1) = \sum_{j=0}^m b_j (y - 1)^j.$$
Extracting $[y^k]$ on both sides gives the classical generalized Inclusion–Exclusion (binomial inversion) formula:
$$a_k = [y^k] B(y - 1) = \sum_{j=k}^m (-1)^{j-k} \binom{j}{k} b_j.$$
For the special case $k = 0$ (zero violations / avoiding all bad conditions), evaluating at $y = 0$ yields $a_0 = A(0) = B(-1) = \sum_{j=0}^m (-1)^j b_j$.

#### Algorithmic Contract: Taylor Shift as Reversal Convolution
Assuming our coefficient ring $K$ is a field of characteristic $0$ or prime $p > m$ so that $1!, 2!, \dots, m!$ are units in $K$, expand $\binom{j}{k} = \frac{j!}{k!(j-k)!}$ and multiply both sides by $k!$:
$$k!\, a_k = \sum_{j=k}^m \bigl(j!\, b_j\bigr) \cdot \frac{(-1)^{j-k}}{(j-k)!} \quad (0 \le k \le m).$$
Define the reversed polynomial $U(z) = \sum_{t=0}^m (m-t)!\, b_{m-t}\, z^t$ and the exponential sign kernel $V(z) = \sum_{s=0}^m \frac{(-1)^s}{s!} z^s$. For any index $0 \le k \le m$, setting $t = m - j$ and $s = j - k$ (so $t + s = m - k$ with $0 \le t, s \le m$) gives the exact one-to-one index invariant:
$$k!\, a_k = [z^{m-k}] \bigl(U(z) \cdot V(z)\bigr).$$
Because $j \in [k, m]$ maps bijectively to $(t, s) = (m-j, j-k)$ with $t \ge 0, s \ge 0$, and $t+s = m-k \le m$, no valid index $j$ is omitted and no out-of-range term is counted twice. This computes all $a_0, a_1, \dots, a_m$ simultaneously in a single NTT multiplication in $O(m \log m)$ time.

---

### 16.2 Factorized Bivariate PIE: Moving $(y-1)$ Inside the Symbolic Method

The true power of $A(y) = B(y-1)$ in Formal Power Series emerges when $b_j = [x^n] B_j(x)$ is itself the coefficient of a generating function in $x$. Define the bivariate generating function of chosen violations:
$$B(x, y) = \sum_{n \ge 0} \sum_{j \ge 0} b_{n, j} x^n y^j,$$
where $b_{n, j}$ counts objects of size $n$ together with $j$ distinguished chosen violations. Then the bivariate generating function of **exact** violations is simply
$$A(x, y) = B(x, y - 1).$$
Because the substitution $y \mapsto y - 1$ is a ring homomorphism $K[y][[x]] \to K[y][[x]]$, **it commutes with every algebraic and analytic FPS operation in $x$**:
1. **Independent Product**: If $B(x, y) = \prod_{r=1}^R B^{(r)}(x, y)$, then $A(x, y) = \prod_{r=1}^R B^{(r)}(x, y - 1)$.
2. **Sequence (`SEQ`) Construction**: If objects are sequences of components where choosing a component with $j$ distinguished violations carries weight $y^j$, so $B(x, y) = \frac{1}{1 - C(x, y)}$, then $A(x, y) = \frac{1}{1 - C(x, y - 1)}$. For $k=0$ violations ($y=0$), we do **not** compute $b_{n, j}$ first; we push $y = 0$ directly into the component GF:
   $$A(x, 0) = \frac{1}{1 - C(x, -1)}.$$
3. **Labelled `SET` ($\exp$) Construction**: If $B(x, y) = \exp\bigl(C(x, y)\bigr)$, then $A(x, y) = \exp\bigl(C(x, y - 1)\bigr)$.

> **Discovery Intuition ("Why didn't I need a 2D DP?")**: Whenever each "chosen violation" is a local bond or mark (e.g., declaring that $p_{i+1}$ must immediately follow $p_i$, or that two vertices in a block must merge), the relaxed objects decompose into independent connected components (chains, blocks, or clusters). Replacing each chosen bond's weight $y$ by $y-1$ *before* assembling the components via `SEQ` or $\exp$ collapses the Inclusion–Exclusion sum directly into the single-variable component generating function!

---

### 16.3 Adjacent-Violation Cluster ("Smearing") PIE & The Carlitz–Scoville–Vaughan / Smirnov Transformation

#### Concrete Objects & Question Answered
Fix an alphabet $\Sigma = \{1, 2, \dots, m\}$ where character $v \in \Sigma$ has formal weight $x_v$ (or $w_v x$ when tracking total length by $x$). We wish to count **Smirnov words** (proper 1D colourings): words $w_1 w_2 \dots w_n \in \Sigma^n$ with **no adjacent equal characters** ($w_t \neq w_{t+1}$ for all $1 \le t < n$), or more generally words with **exact** (or bounded) numbers of adjacent equal pairs $w_t = w_{t+1}$.

#### Two Equivalent Derivations: Cluster PIE vs. Algebraic Compression

##### Route 1: Bivariate Cluster ("Smearing") PIE
For a word $w = w_1 \dots w_n$, there are $n-1$ adjacent slots $\{1, \dots, n-1\}$ where a violation $E_t : (w_t = w_{t+1})$ could occur. If we choose a subset $S \subseteq \{1, \dots, n-1\}$ of $|S| = j$ slots and force $w_t = w_{t+1}$ for every $t \in S$, the positions $\{1, \dots, n\}$ are partitioned by the bonds in $S$ into $c = n - j$ **monochromatic contiguous blocks (clusters)** of lengths $\ell_1 + \ell_2 + \dots + \ell_c = n$ ($\ell_r \ge 1$).
- A single monochromatic cluster of colour $v$ and length $\ell \ge 1$ contains $\ell - 1$ forced internal violation bonds, so in the relaxed bivariate GF $B(\mathbf{x}, y)$ it has weight $x_v^\ell y^{\ell - 1}$.
- Summing over all cluster lengths $\ell \ge 1$ gives the relaxed cluster GF for colour $v$:
  $$R_v(x_v, y) = \sum_{\ell = 1}^\infty x_v^\ell y^{\ell - 1} = \frac{x_v}{1 - y x_v}.$$
- Since the $c$ chosen clusters have **no** forced bonds between them, their colours are completely unconstrained in $B(\mathbf{x}, y)$! Thus $B(\mathbf{x}, y) = \operatorname{SEQ}\bigl(\sum_{v=1}^m R_v(x_v, y)\bigr)$.
- Applying the factorized bivariate substitution $y \leftarrow y - 1$ immediately transforms each cluster's GF into the **exact-violation cluster GF**:
  $$C_v(x_v, y) = R_v(x_v, y - 1) = \sum_{\ell = 1}^\infty x_v^\ell (y - 1)^{\ell - 1} = \frac{x_v}{1 - (y - 1) x_v},$$
  and the exact bivariate OGF for words with $y$ marking adjacent equal pairs is:
  $$A(\mathbf{x}, y) = B(\mathbf{x}, y - 1) = \frac{1}{1 - \sum_{v=1}^m \frac{x_v}{1 - (y - 1) x_v}}.$$
- Setting $y = 0$ (zero adjacent equalities) yields the celebrated **Carlitz–Scoville–Vaughan (Smirnov) formula**:
  $$A(\mathbf{x}, 0) = \frac{1}{1 - \sum_{v=1}^m \frac{x_v}{1 + x_v}}, \quad\text{where}\quad C_v(x_v, 0) = \sum_{\ell=1}^\infty (-1)^{\ell-1} x_v^\ell = \frac{x_v}{1 + x_v}.$$

##### Route 2: Direct Algebraic Automaton Isolation (Without PIE)
Every non-empty word can be uniquely compressed into a sequence of maximal monochromatic runs (a Smirnov word on run-blocks), where a run of colour $v$ has non-empty OGF $R_v(x_v) = \sum_{\ell \ge 1} x_v^\ell$. Let $F_v(\mathbf{x})$ be the OGF of run-compressed words ending with a run of colour $v$, and let $S(\mathbf{x}) = 1 + \sum_{u=1}^m F_u(\mathbf{x})$ be the total OGF (including the empty word $1$). Because a run of colour $v$ can be appended to any valid word *except* one already ending in colour $v$:
$$F_v(\mathbf{x}) = R_v(x_v)\bigl(S(\mathbf{x}) - F_v(\mathbf{x})\bigr).$$
Wait—instead of maintaining $m$ separate DP states $F_1, \dots, F_m$, solve this equation for $F_v(\mathbf{x})$ in terms of the single scalar series $S(\mathbf{x})$! Moving $R_v(x_v) F_v(\mathbf{x})$ to the left-hand side:
$$\bigl(1 + R_v(x_v)\bigr) F_v(\mathbf{x}) = R_v(x_v) S(\mathbf{x}) \implies F_v(\mathbf{x}) = \frac{R_v(x_v)}{1 + R_v(x_v)} S(\mathbf{x}).$$
Here $1 + R_v(x_v) \in K[[x_v]]$ has constant term $1$, which is a unit in any commutative ring $K$. Summing over $v = 1, \dots, m$ and adding $1$:
$$S(\mathbf{x}) = 1 + \sum_{v=1}^m F_v(\mathbf{x}) = 1 + S(\mathbf{x}) \sum_{v=1}^m \frac{R_v(x_v)}{1 + R_v(x_v)} \implies S(\mathbf{x}) = \frac{1}{1 - \sum_{v=1}^m \frac{R_v(x_v)}{1 + R_v(x_v)}}.$$
When $R_v(x_v) = \frac{x_v}{1 - x_v}$ (any run of length $\ell \ge 1$ is allowed, meaning no runs of length $\ge 2$ when we invert), wait: if we want **no** runs of length $\ge 2$, then in the run-compressed picture only runs of length $1$ ($R_v(x_v) = x_v$) are permitted! Substituting $R_v(x_v) = x_v$ into $\frac{R_v}{1 + R_v}$ immediately gives $C_v(x_v) = \frac{x_v}{1 + x_v}$!
More generally, if a problem allows maximal runs of colour $v$ to have arbitrary weight generating function $R_v(x)$ (with $[x^0] R_v(x) = 0$), the effective PIE-transformed cluster weight that allows us to pretend adjacent runs can be chosen *without* the $v_{\text{next}} \neq v_{\text{prev}}$ restriction is universally:
$$C_v(x) = \frac{R_v(x)}{1 + R_v(x)} = \sum_{k \ge 1} (-1)^{k-1} R_v(x)^k.$$

#### Two Essential Competitive Programming Specializations
1. **Fixed Color Frequencies (Multiset Permutations / EGF Form, e.g., `CF 840C` / `Luogu P4491`)**:
   Suppose colour $i$ appears **exactly** $s_i$ times ($n = \sum_{i=1}^m s_i$), and we only care about the coefficient $[x_1^{s_1} \dots x_m^{s_m}]$. In $\frac{x_i}{1 - (y-1)x_i} = \sum_{\ell \ge 1} (y-1)^{\ell-1} x_i^\ell$, partitioning the $s_i$ identical items of colour $i$ into $c_i$ non-empty ordered clusters ($1 \le c_i \le s_i$) can be done in $\binom{s_i - 1}{c_i - 1}$ ways by stars-and-bars, and always uses $s_i - c_i$ internal bonds of weight $(y-1)$. Since a sequence of $C = \sum_{i=1}^m c_i$ clusters of distinct types has $\frac{C!}{\prod_{i=1}^m c_i!}$ interlacings, we switch to an **Exponential Generating Function (EGF)** in $x$ (marking cluster count $c_i$ by $\frac{x^{c_i}}{c_i!}$):
   $$\widehat{C}_i(x, y) = \sum_{c_i = 1}^{s_i} \binom{s_i - 1}{c_i - 1} (y - 1)^{s_i - c_i} \frac{x^{c_i}}{c_i!}, \qquad A_{\text{fixed}}(y) = \sum_{C=1}^n C!\, [x^C] \prod_{i=1}^m \widehat{C}_i(x, y).$$
   If the $s_i$ items of colour $i$ are *labelled* (distinct), simply multiply the final result by $\prod_{i=1}^m s_i!$ (or include $s_i!$ inside $\widehat{C}_i$).
2. **Forbidding Maximal Runs of Length $\ge L$ (`ARC115 E` / `AGC058 D`)**:
   If runs of colour $v$ of length $1, 2, \dots, L-1$ are valid ($R_v(x) = \sum_{j=1}^{L-1} (w_v x)^j = \frac{w_v x - (w_v x)^L}{1 - w_v x}$), then the transformed cluster GF is:
   $$C_v(x) = \frac{R_v(x)}{1 + R_v(x)} = \frac{\frac{w_v x - (w_v x)^L}{1 - w_v x}}{1 + \frac{w_v x - (w_v x)^L}{1 - w_v x}} = \frac{w_v x - (w_v x)^L}{1 - (w_v x)^L} = \sum_{q \ge 0} \bigl((w_v x)^{qL + 1} - (w_v x)^{(q+1)L}\bigr).$$
   Notice the periodic coefficients $(+1, 0, \dots, 0, -1, +1, 0, \dots)$: clusters of length $\equiv 1 \pmod L$ carry $+1$, clusters of length $\equiv 0 \pmod L$ carry $-1$, and all other lengths vanish!

---

### 16.4 Forbidden Substrings & The Goulden–Jackson Cluster Method

#### Concrete Objects & Question Answered
Let $\Sigma$ be an alphabet of size $\sigma = |\Sigma|$ (or weighted alphabet with total character OGF $S(x) = \sum_{a \in \Sigma} w_a x$), and let $\mathcal{B} = \{u^{(1)}, u^{(2)}, \dots, u^{(k)}\} \subseteq \Sigma^+$ be a **reduced** set of forbidden words (no word in $\mathcal{B}$ is a factor/substring of another word in $\mathcal{B}$). For any word $w \in \Sigma^n$, let $\text{occ}_{\mathcal{B}}(w)$ be the total number of occurrences of words from $\mathcal{B}$ as contiguous factors of $w$.
**Question answered**: What is the bivariate OGF $F(x, y) = \sum_{w \in \Sigma^*} x^{|w|} y^{\text{occ}_{\mathcal{B}}(w)}$, and in particular $F(x, 0)$ (words avoiding all patterns in $\mathcal{B}$)?

#### Overlap Polynomials (Autocorrelation & Cross-Correlation)
For two patterns $u, v \in \mathcal{B}$ of lengths $|u|, |v|$, define the **overlap set** $\mathcal{O}(u, v)$ to be the set of non-empty words $z \in \Sigma^+$ ($1 \le |z| < \min(|u|, |v|)$ when $u \neq v$, and $1 \le |z| \le |u|$ when $u = v$) that are simultaneously a **suffix of $u$** and a **prefix of $v$**: $u = r z$ and $v = z s$. When a copy of $v$ is placed overlapping the right end of $u$ along their shared border $z$, the combined word $r z s$ extends $u$ to the right by the suffix $s = z^{-1} v$ of length $|v| - |z|$.
Define the **right-extension correlation polynomial**:
$$\operatorname{Corr}_{u \to v}(x) = \sum_{\substack{z \in \Sigma^+ \\ u = r z,\; v = z s \\ |s| > 0 \text{ if } u \neq v}} x^{|s|} = \sum_{\substack{1 \le \ell \le \min(|u|,|v|) \\ u[|u|-\ell+1 \dots |u|] = v[1 \dots \ell]}} x^{|v| - \ell}.$$
- When $u = v$, the full overlap $z = u$ ($\ell = |u|$, extension $s = \varepsilon$ of length $0$) is **included**, so the **autocorrelation polynomial** $A_u(x) := \operatorname{Corr}_{u \to u}(x)$ always has constant term $[x^0] A_u(x) = 1$:
  $$A_u(x) = 1 + \sum_{\substack{1 \le \ell < |u| \\ u[1\dots\ell] = u[|u|-\ell+1\dots|u|]}} x^{|u| - \ell}.$$
- When $u \neq v$, since $\mathcal{B}$ is reduced, $v$ cannot be a factor of $u$, so $\ell < |v|$ strictly, and every term in $\operatorname{Corr}_{u \to v}(x)$ has degree $|v| - \ell \ge 1$ ($[x^0] \operatorname{Corr}_{u \to v}(x) = 0$).

#### Step-by-Step Derivation of the Cluster Linear System
Applying the factorized bivariate PIE ($y \mapsto y - 1$) to the set of all occurrences of patterns from $\mathcal{B}$ in a word $w$:
1. Choosing a subset $S$ of distinguished occurrences of patterns from $\mathcal{B}$ and giving each chosen occurrence weight $(y - 1)$ partitions any word $w$ uniquely into an alternating sequence of **free single letters** (each of weight $\sigma x$) and **maximal overlapping clusters** of chosen pattern occurrences (where each chosen occurrence in a cluster overlaps the previous chosen occurrence in the cluster by at least $1$ character).
2. Therefore, if $C(x, y) = \sum_{u \in \mathcal{B}} C_u(x, y)$ is the generating function of all valid non-empty clusters (where $C_u(x, y)$ counts clusters whose **last (rightmost)** chosen occurrence is pattern $u \in \mathcal{B}$), then every marked word is a `SEQ` of single letters and clusters:
   $$F(x, y) = \operatorname{SEQ}(\Sigma \cup \mathcal{C}) = \frac{1}{1 - \sigma x - \sum_{u \in \mathcal{B}} C_u(x, y)}.$$
3. How is a cluster ending in $u \in \mathcal{B}$ formed? wait: consider a cluster whose rightmost occurrence is $u$, and suppose we also allow the rightmost occurrence to overlap $u$ with the trivial $0$-length extension $s = \varepsilon$ (which only happens if we append $u$ onto $u$ at the exact same position, which is not a distinct occurrence!). Instead, the standard Goulden–Jackson decomposition observes that if we take a cluster ending in some $v \in \mathcal{B}$ (or start a fresh cluster with $u$) and consider all ways an occurrence of $u$ can overlap the end of $v$—**including** the $\ell = |u|$ identity overlap of $u$ with itself—then:
   - Starting a cluster with $u$ alone contributes $(y - 1) x^{|u|}$.
   - Extending a cluster ending in $v \in \mathcal{B}$ by a strictly right-shifted overlapping occurrence of $u$ multiplies $C_v(x, y)$ by $(y - 1) \bigl(\operatorname{Corr}_{v \to u}(x) - [v = u]\bigr)$.
   Adding $(y-1) C_u(x, y)$ to both sides moves the $[v=u]$ term into $\operatorname{Corr}_{v \to u}(x)$ and yields the clean $k \times k$ linear system over $K(y)[[x]]$:
   $$C_u(x, y) + \sum_{v \in \mathcal{B}} (1 - y) \operatorname{Corr}_{v \to u}(x)\, C_v(x, y) = (y - 1) x^{|u|} \quad \text{for all } u \in \mathcal{B}.$$
   At $y = 0$ (forbidden substrings, $1 - y = 1$ and $y - 1 = -1$), this simplifies to:
   $$\sum_{v \in \mathcal{B}} \operatorname{Corr}_{v \to u}(x)\, C_v(x, 0) = -x^{|u|} \quad \text{for all } u \in \mathcal{B}.$$

#### Special Case $k = 1$ (Single Forbidden Pattern $u$ of Length $m$)
When $\mathcal{B} = \{u\}$, the $1 \times 1$ system is $(1 + (1-y)(A_u(x) - 1)) C_u(x, y) = (y-1) x^m$, or at $y = 0$:
$$A_u(x)\, C_u(x, 0) = -x^m \implies C_u(x, 0) = -\frac{x^m}{A_u(x)}.$$
Substituting this into $F(x, 0) = \frac{1}{1 - \sigma x - C_u(x, 0)}$ gives the famous closed-form rational generating function:
$$F(x, 0) = \frac{1}{1 - \sigma x + \frac{x^m}{A_u(x)}} = \frac{A_u(x)}{(1 - \sigma x) A_u(x) + x^m},$$
and for general $y$:
$$F(x, y) = \frac{1 + (1 - y)(A_u(x) - 1)}{(1 - \sigma x)\bigl(1 + (1 - y)(A_u(x) - 1)\bigr) + (1 - y) x^m}.$$

#### Hand-Checkable Example ($u = \texttt{ABA}$ over $\Sigma = \{\texttt{A}, \texttt{B}\}$, $\sigma = 2$)
- Here $m = 3$. Borders of $u = \texttt{ABA}$:
  - $\ell = 3$: $\texttt{ABA}$ (extension $\varepsilon$, length $0 \implies x^0$),
  - $\ell = 2$: prefix $\texttt{AB} \neq$ suffix $\texttt{BA}$,
  - $\ell = 1$: prefix $\texttt{A} =$ suffix $\texttt{A}$ (extension $\texttt{BA}$, length $3 - 1 = 2 \implies x^2$).
- Thus $A_{\texttt{ABA}}(x) = 1 + x^2$.
- Cluster GF at $y = 0$: $C_{\texttt{ABA}}(x, 0) = -\frac{x^3}{1 + x^2} = -x^3 + x^5 - x^7 + \cdots$ (where $-x^3$ is the single pattern $\texttt{ABA}$ with 1 chosen occurrence $(-1)^1$, $+x^5$ is the overlapping cluster $\texttt{ABABA}$ with 2 chosen occurrences $(-1)^2$, $-x^7$ is $\texttt{ABABABA}$ with 3 chosen occurrences $(-1)^3$, etc.).
- Total avoidance OGF:
  $$F(x, 0) = \frac{1 + x^2}{(1 - 2x)(1 + x^2) + x^3} = \frac{1 + x^2}{1 - 2x + x^2 - x^3} = 1 + 2x + 4x^2 + 7x^3 + 12x^4 + 21x^5 + \cdots$$
- Hand-check at $n = 3, 4$:
  - $n = 3$: Out of $2^3 = 8$ words, only $\texttt{ABA}$ contains $\texttt{ABA}$, leaving $8 - 1 = 7 = [x^3]F(x,0)$.
  - $n = 4$: Words containing $\texttt{ABA}$ are $\texttt{ABA}\ast$ ($2$ words) and $\ast\texttt{ABA}$ ($2$ words), which do not overlap at length $4$ (since their intersection would have length $3+3-1=5 > 4$). Thus $16 - 4 = 12 = [x^4]F(x,0)$.
  - $n = 5$: Naive subtraction gives $32 - 3 \cdot 2^2 = 20$, which undercounts by $1$ because $\texttt{ABABA}$ contains **two** overlapping copies of $\texttt{ABA}$. The $+x^5$ term in $C_{\texttt{ABA}}(x,0)$ restores $\texttt{ABABA}$, giving $20 + 1 = 21 = [x^5]F(x,0)$.

#### Algorithmic Regimes & Complexity Contract
| Regime | Constraints | Algorithm & Complexity |
|---|---|---|
| **Single pattern, large $N$** | $k = 1$, $m \le 10^5$, $N \le 10^{18}$ | Compute $A_u(x)$ via KMP prefix-function $\pi$ in $O(m)$; extract $[x^N] \frac{A_u(x)}{(1-\sigma x)A_u(x) + x^m}$ via **Bostan–Mori** in $O(m \log m \log N)$. |
| **Single pattern, all $n \le N$** | $k = 1$, $m, N \le 5 \cdot 10^5$ | Compute $A_u(x)$ via KMP in $O(m)$ and invert $(1-\sigma x)A_u(x) + x^m \bmod x^{N+1}$ via **FPS Inv** in $O(N \log N)$. |
| **Multi-pattern, small $k$, large $L = \sum |u_i|$** | $k \le 20$, $\sum |u_i| \le 10^5$, $N \le 10^5$ | Compute all $k^2$ polynomials $\operatorname{Corr}_{v \to u}(x)$ via Aho–Corasick or Z-algorithm in $O(k \sum |u_i|)$; solve the $k \times k$ linear system over $\mathbb{F}_p[[x]] \bmod x^{N+1}$ via Gaussian elimination or evaluated at NTT roots of unity in $O(k^3 N + k^2 N \log N)$ (whereas Aho–Corasick automaton DP would have $\sum |u_i|$ states!). |

---

## Iteration 17: Probability Generating Functions (PGFs), Stopping Times, First-Passage Renewal, and Random Walks

### 17.1 PGF Fundamentals, Factorial Moments, and the Stop-vs-Continue Survival Identity

#### Concrete Objects & Question Answered
Let $T \in \{0, 1, 2, \dots\} \cup \{\infty\}$ be a discrete stopping time (the step at which a random process first reaches an absorbing target state). Let $f_n = \Pr(T = n)$ be the probability of stopping at exact step $n$, and let $g_n = \Pr(T > n)$ be the **survival probability** (the probability that the process is still strictly alive after step $n$). Define their Ordinary Generating Functions:
$$F(x) = \sum_{n=0}^\infty f_n x^n, \qquad G(x) = \sum_{n=0}^\infty g_n x^n.$$
**Question answered**: How are $F(x)$ and $G(x)$ related algebraically, and how do we extract $\mathbb{E}[T]$, $\operatorname{Var}(T)$, and higher moments from $F(x)$ or $G(x)$?

#### Step-by-Step Derivation of the Survival Identity & Moments
Assuming the process eventually terminates with probability $1$ ($F(1) = \sum_{n=0}^\infty f_n = 1$), the event $\{T > n-1\}$ is the disjoint union of $\{T = n\}$ (stops at step $n$) and $\{T > n\}$ (survives step $n$):
$$g_{n-1} = f_n + g_n \quad (n \ge 1), \qquad f_0 + g_0 = \Pr(T = 0) + \Pr(T > 0) = 1.$$
Multiply $f_n + g_n - g_{n-1} = 0$ by $x^n$ and sum over $n \ge 1$, adding $f_0 + g_0 = 1$:
$$F(x) + (1 - x) G(x) = 1 \iff G(x) = \frac{1 - F(x)}{1 - x}.$$
Differentiating $F(x) = \sum_{n \ge 0} f_n x^n$ term-by-term and evaluating at $x = 1$ produces the **factorial moments**:
$$F^{(k)}(1) = \sum_{n \ge k} n(n-1)\cdots(n-k+1) f_n = \mathbb{E}\bigl[T^{\underline{k}}\bigr].$$
In particular, using $F(x) = 1 - (1-x)G(x) \implies F'(x) = G(x) - (1-x)G'(x)$ and $F''(x) = 2G'(x) - (1-x)G''(x)$, evaluating at $x = 1$ gives both the $F$-form and $G$-form moment formulas:
$$\mathbb{E}[T] = F'(1) = G(1),$$
$$\mathbb{E}[T(T-1)] = F''(1) = 2 G'(1),$$
$$\operatorname{Var}(T) = \mathbb{E}[T(T-1)] + \mathbb{E}[T] - (\mathbb{E}[T])^2 = F''(1) + F'(1) - F'(1)^2 = 2 G'(1) + G(1) - G(1)^2.$$
If one uses the pointing operator $\vartheta = x \frac{d}{dx}$, then $(\vartheta^k F)(1) = \mathbb{E}[T^k]$ gives ordinary power moments directly.

---

### 17.2 String Hitting Times & Multi-Pattern Penney's Game (`[CTSC2006] 歌唱王国` & `[SDOI2017] 硬币游戏`)

#### Single Pattern Stopping Time (`Luogu P4548 [CTSC2006] 歌唱王国`)
Suppose letters are drawn i.i.d. uniformly from an alphabet $\Sigma$ of size $\sigma$ (each letter with probability $p = \sigma^{-1}$, or more generally letter $a$ with probability $p_a$), and the process stops the very first time a target string $S = s_1 s_2 \dots s_m$ appears as a contiguous suffix.
- Let $F(x)$ be the PGF of the stopping time $T$ (where $f_n$ is the probability of first seeing $S$ at step $n$), and let $G(x)$ be the PGF of surviving prefixes (where $g_n$ is the probability of a length-$n$ string having **no** occurrence of $S$ at all).
- **Equation 1 (One-step survival)**: Appending any letter $a \in \Sigma$ to a surviving string of length $n$ creates a string of length $n+1$ that either survives or hits $S$ for the first time at step $n+1$. Since $T \ge m > 0$ ($f_0 = 0$), this is simply the survival identity:
  $$F(x) + (1 - x) G(x) = 1.$$
- **Equation 2 (Freely appending the pattern $S$ to a survivor)**: Take any surviving string $w$ of length $n$ (weight $g_n x^n$) and forcibly append the entire string $S = s_1 \dots s_m$ (multiplying the probability-weighted x-monomial by $\sigma^{-m} x^m$). Since $w$ contained no copy of $S$, the **first** occurrence of $S$ in $w S$ must end at some position $n + \ell$ inside the appended suffix $S$ ($1 \le \ell \le m$). For $S$ to end at position $n + \ell$, the prefix $S[1 \dots \ell]$ must match a suffix of $S$, meaning $\ell \in \operatorname{Borders}(S)$ ($S[1 \dots \ell] = S[m-\ell+1 \dots m]$), and the remaining $m - \ell$ characters $S[\ell+1 \dots m]$ are determined with probability $\sigma^{-(m-\ell)}$ and length $x^{m-\ell}$. This double-count yields the exact identity:
  $$G(x) \cdot \left(\frac{x}{\sigma}\right)^m = F(x) \sum_{\ell \in \operatorname{Borders}(S)} \left(\frac{x}{\sigma}\right)^{m - \ell}.$$
- **Extracting $\mathbb{E}[T]$ and $\operatorname{Var}(T)$**:
  Evaluate Equation 2 at $x = 1$ using $F(1) = 1$:
  $$G(1) \cdot \sigma^{-m} = 1 \cdot \sum_{\ell \in \operatorname{Borders}(S)} \sigma^{-(m-\ell)} \implies \mathbb{E}[T] = G(1) = \sum_{\ell \in \operatorname{Borders}(S)} \sigma^\ell.$$
  To find $\operatorname{Var}(T)$, multiply Equation 2 by $\sigma^m$ so that $x^m G(x) = F(x) \sum_{\ell \in \operatorname{Borders}(S)} \sigma^\ell x^{m-\ell}$, differentiate both sides with respect to $x$ at $x = 1$, and use $F'(1) = G(1) = \mathbb{E}[T]$ and $F''(1) = 2 G'(1)$:
  $$m G(1) + G'(1) = F'(1) \sum_{\ell \in \operatorname{Borders}(S)} \sigma^\ell + F(1) \sum_{\ell \in \operatorname{Borders}(S)} (m - \ell) \sigma^\ell \implies G'(1) = \left(\sum_{\ell \in \operatorname{Borders}(S)} \sigma^\ell\right)^2 - \sum_{\ell \in \operatorname{Borders}(S)} \ell \sigma^\ell,$$
  which immediately gives the closed-form variance:
  $$\operatorname{Var}(T) = 2 G'(1) + G(1) - G(1)^2 = \left(\sum_{\ell \in \operatorname{Borders}(S)} \sigma^\ell\right)^2 + \sum_{\ell \in \operatorname{Borders}(S)} (1 - 2\ell) \sigma^\ell.$$

#### Multi-Pattern Penney's Game (`Luogu P3706 [SDOI2017] 硬币游戏`)
Now suppose there are $k$ competing patterns $S_1, S_2, \dots, S_k \in \Sigma^m$, and the process stops the moment **any** $S_i$ appears. Let $F_i(x)$ be the PGF of stopping on pattern $S_i$, and $G(x)$ be the PGF of surviving without seeing any $S_1, \dots, S_k$.
- **Survival equation**: $\sum_{i=1}^k F_i(x) + (1 - x) G(x) = 1$. At $x = 1$, since $(1-x)G(x)|_{x=1} = 0$, this gives the probability normalization $\sum_{i=1}^k F_i(1) = 1$.
- **Appending $S_j$ to a survivor**: For each $j \in \{1, \dots, k\}$, appending $S_j$ to a surviving string triggers some $S_i$ at the earliest overlap border $\ell$ where a suffix of $S_i$ of length $\ell$ equals the prefix $S_j[1 \dots \ell]$:
  $$G(x) \left(\frac{x}{\sigma}\right)^m = \sum_{i=1}^k F_i(x) \sum_{\substack{1 \le \ell \le m \\ S_i[m-\ell+1 \dots m] = S_j[1 \dots \ell]}} \left(\frac{x}{\sigma}\right)^{m - \ell} \quad (1 \le j \le k).$$
- Evaluating at $x = 1$ (and multiplying by $\sigma^m$) gives $k$ linear equations relating $G(1)$ and the winning probabilities $P_i = F_i(1)$:
  $$G(1) = \sum_{i=1}^k P_i \cdot \operatorname{Corr}_{S_i \to S_j}(\sigma) \quad (1 \le j \le k), \qquad \sum_{i=1}^k P_i = 1,$$
  where $\operatorname{Corr}_{S_i \to S_j}(\sigma) = \sum_{\ell : S_i[\text{suf }\ell] = S_j[\text{pref }\ell]} \sigma^\ell$. This is a $(k+1) \times (k+1)$ linear system in the unknowns $(P_1, \dots, P_k, G(1))$, solvable via Gaussian elimination in $O(k^3 + k^2 m)$ time!

---

### 17.3 First-Passage Renewal $F_{s \to t}(x) = H_{s \to t}(x) / H_{t \to t}(x)$, Pole Cancellation at $x = 1$, and the EGF-to-OGF Renewal Bridge

#### Concrete Objects & Question Answered
Consider a Markov chain on state space $V$ starting at state $s$ with a target state $t$.
- Let $h_{s \to t, n} = \Pr(X_n = t \mid X_0 = s)$ be the **unrestricted** $n$-step transition probability of being at $t$ at step $n$ (possibly having visited $t$ multiple times before step $n$), with OGF $H_{s \to t}(x) = \sum_{n \ge 0} h_{s \to t, n} x^n$.
- Let $h_{t \to t, n} = \Pr(X_n = t \mid X_0 = t)$ be the unrestricted $n$-step return probability to $t$, with OGF $H_{t \to t}(x) = \sum_{n \ge 0} h_{t \to t, n} x^n$.
- Let $f_{s \to t, n} = \Pr(T_t = n \mid X_0 = s)$ be the **first-passage** probability of reaching $t$ for the **very first time** at step $n$, with PGF $F_{s \to t}(x) = \sum_{n \ge 0} f_{s \to t, n} x^n$.

**Question answered**: How do we compute $\mathbb{E}[T_t \mid X_0 = s] = F'_{s \to t}(1)$ when only the unrestricted walk OGFs $H_{s \to t}(x)$ and $H_{t \to t}(x)$ are easy to compute (for instance via Fast Walsh–Hadamard Transform or EGF product)?

#### Step-by-Step Renewal Derivation & Singularity Cancellation at $x = 1$
Every unrestricted path from $s$ to $t$ of length $n$ splits uniquely at the **first** time $k \in \{0, 1, \dots, n\}$ that it visits $t$:
- Steps $0 \to k$: a first-passage path from $s$ to $t$ of length $k$ (probability $f_{s \to t, k}$),
- Steps $k \to n$: an arbitrary unrestricted return path from $t$ to $t$ of length $n - k$ (probability $h_{t \to t, n-k}$).
Therefore $h_{s \to t, n} = \sum_{k=0}^n f_{s \to t, k} h_{t \to t, n-k}$, which in $K[[x]]$ is the exact convolution:
$$H_{s \to t}(x) = F_{s \to t}(x) \cdot H_{t \to t}(x) \implies F_{s \to t}(x) = \frac{H_{s \to t}(x)}{H_{t \to t}(x)}.$$
Notice that $[x^0] H_{t \to t}(x) = h_{t \to t, 0} = 1$, so $H_{t \to t}(x)$ is always invertible as a formal power series in $K[[x]]$.

**Failure Mode & Singularity Cancellation at $x = 1$**:
Can we simply differentiate $F_{s \to t}(x) = H_{s \to t}(x) / H_{t \to t}(x)$ at $x = 1$? **No!** On a finite recurrent Markov chain, the chain visits $t$ infinitely often, so $\sum_{n \ge 0} h_{s \to t, n} = \infty$: both $H_{s \to t}(x)$ and $H_{t \to t}(x)$ have a **simple pole at $x = 1$** (originating from the stationary eigenvalue $\lambda_0 = 1$, which contributes $\frac{\pi_t}{1 - x}$ to both series).
To cancel the pole algebraically, multiply both numerator and denominator by $(1 - x)$ and define the **regularized OGFs**:
$$\widetilde{H}_{s \to t}(x) = (1 - x) H_{s \to t}(x), \qquad \widetilde{H}_{t \to t}(x) = (1 - x) H_{t \to t}(x).$$
Now both $\widetilde{H}_{s \to t}(x)$ and $\widetilde{H}_{t \to t}(x)$ are regular at $x = 1$, with $\widetilde{H}_{s \to t}(1) = \widetilde{H}_{t \to t}(1) = \pi_t \neq 0$ (establishing $F_{s \to t}(1) = \frac{\pi_t}{\pi_t} = 1$). Applying the quotient rule to $F_{s \to t}(x) = \frac{\widetilde{H}_{s \to t}(x)}{\widetilde{H}_{t \to t}(x)}$ at $x = 1$ yields the fundamental **Pole-Cancelled First-Passage Expectation Formula**:
$$\mathbb{E}[T_t \mid X_0 = s] = F'_{s \to t}(1) = \frac{\widetilde{H}'_{s \to t}(1) \widetilde{H}_{t \to t}(1) - \widetilde{H}_{s \to t}(1) \widetilde{H}'_{t \to t}(1)}{\widetilde{H}_{t \to t}(1)^2} = \frac{\widetilde{H}'_{s \to t}(1) - \widetilde{H}'_{t \to t}(1)}{\widetilde{H}_{t \to t}(1)}.$$

#### The EGF-to-OGF Renewal Bridge (`[ZJOI2019] 开关` Luogu P5326, `ARC136 F`)
In many switch/flip problems, each item $i \in \{1, \dots, n\}$ is toggled independently with probability $p_i$ per step ($\sum_{i=1}^n p_i = 1$). Because steps are distributed among items as multinomials $\frac{m!}{m_1! \dots m_n!}$, the natural representation of $m$-step unrestricted probabilities is an **Exponential Generating Function (EGF)**:
$$\widehat{H}_{s \to t}(z) = \sum_{m=0}^\infty h_{s \to t, m} \frac{z^m}{m!} = \prod_{i=1}^n \frac{e^{p_i z} + (-1)^{\Delta_i} e^{-p_i z}}{2} = \sum_{\lambda} c_\lambda e^{\lambda z},$$
where $\lambda \in [-1, 1]$ ranges over eigenvalues of the form $\frac{k}{S}$ ($S = \sum p_i$).
How do we pass from the EGF $\widehat{H}(z) = \sum_\lambda c_\lambda e^{\lambda z}$ to the OGF $H(x) = \sum_{m \ge 0} h_m x^m$? Applying the formal Laplace/Borel bridge $\frac{z^m}{m!} \mapsto x^m$ term-by-term maps each exponential $e^{\lambda z} = \sum_{m \ge 0} \lambda^m \frac{z^m}{m!}$ to a geometric series:
$$\mathcal{L}\bigl[e^{\lambda z}\bigr](x) = \sum_{m=0}^\infty (\lambda x)^m = \frac{1}{1 - \lambda x}.$$
Therefore, if $\widehat{H}_{s \to t}(z) = \sum_\lambda c_\lambda e^{\lambda z}$ and $\widehat{H}_{t \to t}(z) = \sum_\lambda d_\lambda e^{\lambda z}$ (where $c_1 = d_1 = 2^{-n}$ is the coefficient of the stationary mode $\lambda = 1$), their regularized OGFs are:
$$\widetilde{H}_{s \to t}(x) = (1 - x) \sum_{\lambda} \frac{c_\lambda}{1 - \lambda x} = c_1 + (1 - x) \sum_{\lambda \neq 1} \frac{c_\lambda}{1 - \lambda x},$$
$$\widetilde{H}_{t \to t}(x) = (1 - x) \sum_{\lambda} \frac{d_\lambda}{1 - \lambda x} = d_1 + (1 - x) \sum_{\lambda \neq 1} \frac{d_\lambda}{1 - \lambda x}.$$
Evaluating at $x = 1$ gives $\widetilde{H}_{s \to t}(1) = \widetilde{H}_{t \to t}(1) = d_1$ and $\widetilde{H}'_{s \to t}(1) = -\sum_{\lambda \neq 1} \frac{c_\lambda}{1 - \lambda}$. Substituting into the pole-cancelled quotient formula yields the exact closed form:
$$\mathbb{E}[T_t \mid X_0 = s] = \frac{\widetilde{H}'_{s \to t}(1) - \widetilde{H}'_{t \to t}(1)}{\widetilde{H}_{t \to t}(1)} = \frac{1}{d_1} \sum_{\lambda \neq 1} \frac{d_\lambda - c_\lambda}{1 - \lambda}.$$

#### Hand-Checkable 2-Bit Switch Example
Let $n = 2$ switches with probabilities $p_1 = \frac{1}{3}, p_2 = \frac{2}{3}$, starting at $s = (0, 0)$ and targeting $t = (1, 1)$ (so both switches must have odd parity of flips: $\Delta_1 = \Delta_2 = 1$).
- Unrestricted EGFs:
  $$\widehat{H}_{s \to t}(z) = \left(\frac{e^{z/3} - e^{-z/3}}{2}\right)\left(\frac{e^{2z/3} - e^{-2z/3}}{2}\right) = \frac{1}{4}\bigl(e^z - e^{z/3} - e^{-z/3} + e^{-z}\bigr),$$
  $$\widehat{H}_{t \to t}(z) = \left(\frac{e^{z/3} + e^{-z/3}}{2}\right)\left(\frac{e^{2z/3} + e^{-2z/3}}{2}\right) = \frac{1}{4}\bigl(e^z + e^{z/3} + e^{-z/3} + e^{-z}\bigr).$$
- Here $c_1 = d_1 = \frac{1}{4}$, and for the non-unit modes $\lambda \in \{\frac{1}{3}, -\frac{1}{3}, -1\}$:
  - $\lambda = \frac{1}{3}$: $d_{1/3} - c_{1/3} = \frac{1}{4} - (-\frac{1}{4}) = \frac{1}{2}$, divided by $1 - \frac{1}{3} = \frac{2}{3}$ gives $\frac{3}{4}$.
  - $\lambda = -\frac{1}{3}$: $d_{-1/3} - c_{-1/3} = \frac{1}{4} - (-\frac{1}{4}) = \frac{1}{2}$, divided by $1 - (-\frac{1}{3}) = \frac{4}{3}$ gives $\frac{3}{8}$.
  - $\lambda = -1$: $d_{-1} - c_{-1} = \frac{1}{4} - \frac{1}{4} = 0$.
- Dividing by $d_1 = \frac{1}{4}$ gives $\mathbb{E}[T] = 4 \left(\frac{3}{4} + \frac{3}{8}\right) = 3 + \frac{3}{2} = \frac{9}{2}$.
- Direct Markov verification: From $(0,0)$, $E_{00} = 1 + \frac{1}{3} E_{10} + \frac{2}{3} E_{01}$; $E_{10} = 1 + \frac{1}{3} E_{00} + \frac{2}{3}(0)$; $E_{01} = 1 + \frac{1}{3}(0) + \frac{2}{3} E_{00}$. Substituting gives $E_{00} = 1 + \frac{1}{3}(1 + \frac{1}{3}E_{00}) + \frac{2}{3}(1 + \frac{2}{3}E_{00}) = 2 + \frac{5}{9} E_{00} \implies \frac{4}{9} E_{00} = 2 \implies E_{00} = \frac{9}{2}$. Exact match!

---

### 17.4 Duality Between PGF Renewal Division and Martingale Potential Functions (`Elegia`'s Poisson Equation Framework)

In Chinese competitive programming literature (notably `Elegia` / EI's tutorials on `CF 1349D Slime and Biscuits` and `CF 1025G Company Acquisitions`), stopping time expectations are often solved via a **Martingale Potential Function** $\Phi : V \to \mathbb{R}$ satisfying the one-step drift equation:
$$\mathbb{E}\bigl[\Phi(X_{t+1}) - \Phi(X_t) \mid X_t = s\bigr] = 1 \quad \text{for all } s \neq t_{\text{target}}.$$
How is this related to our PGF renewal division $F_{s \to t}(x) = H_{s \to t}(x) / H_{t \to t}(x)$?
Let $P$ be the transition matrix of the Markov chain. The matrix OGF of unrestricted walks is $\mathbf{H}(x) = (I - x P)^{-1}$. If $P$ is irreducible with stationary distribution $\pi$ ($\pi^\top P = \pi^\top$), then decomposing $\mathbf{H}(x)$ into the rank-1 stationary projection $\mathbf{1}\pi^\top$ and the transient resolvent shows that the column vector of pole-cancelled derivatives $\phi_s := -\widetilde{H}'_{s \to t}(1) = \sum_{n=0}^\infty \bigl(\Pr(X_n = t \mid X_0 = s) - \pi_t\bigr)$ is the **fundamental potential (Poisson equation solution)** of the Markov chain:
$$(I - P) \phi = e_t - \pi_t \mathbf{1} \iff \Phi(s) := \frac{\phi_t - \phi_s}{\pi_t} \text{ satisfies } (P - I)\Phi(s) = -1 \;(s \neq t),\quad (P - I)\Phi(t) = \frac{1}{\pi_t} - 1.$$
Thus, **PGF renewal division with pole cancellation at $x = 1$ and the Martingale potential method are exact algebraic duals**:
- Use **PGF + EGF/FWT Renewal Division** when the state space is a product/group structure (e.g., $\mathbb{Z}_2^n$ in `[ZJOI2019] 开关` or `ARC136 F`) where $(I - xP)^{-1}$ diagonalizes into independent exponential modes.
- Use **Martingale Potentials $\sum_i f(a_i)$** when the state is a partition or token configuration $(a_1, \dots, a_m)$ with symmetric pairwise transitions (`CF 1349D`, `CF 1025G`), reducing the Poisson equation to a 1D recurrence in $f(a)$!

---

## Iteration 18: Chinese (`[ZH]`) Deep-Dive on GF Inclusion–Exclusion, Cluster Method & PGFs

### 18.1 Chinese National Team Papers (`国家集训队论文`) & Canonical Author Synthesis
1. **Yang Maolong (杨懋龙, 2018 IOI Chinese National Team Paper)**: *《浅谈生成函数在掷骰子问题上的应用》 (On the Application of Generating Functions to Dice-Rolling Problems)*.
   - Systematizes the PGF stop-vs-continue framework $F(x) + (1-x)G(x) = 1$, string hitting time equations (`[CTSC2006] 歌唱王国`, `[SDOI2017] 硬币游戏`), variance extraction via $F''(1) + F'(1) - F'(1)^2 = 2G'(1) + G(1) - G(1)^2$, and first-passage renewal division $F(x) = H_{s \to t}(x) / H_{t \to t}(x)$.
2. **`command_block` (洛谷博客 / Cnblogs)**: *《生成函数杂谈》 (Miscellaneous Notes on Generating Functions)* & *《容斥原理与反演》*.
   - Formalizes **Block-Split / Contiguous-Run PIE (`连续段容斥`)** in two canonical templates:
     - **Chain-bond view**: Marking each forbidden adjacent equality with $(y-1)$ gives cluster weight $C(x) = \sum_{\ell \ge 1} (-1)^{\ell-1} w_\ell x^\ell$.
     - **Automaton isolation view**: Solving $F_c(x) = R_c(x)(S(x) - F_c(x)) \implies F_c(x) = \frac{R_c(x)}{1 + R_c(x)} S(x)$ directly yields the effective cluster GF $C_c(x) = \frac{R_c(x)}{1 + R_c(x)}$ without needing to guess PIE signs!
3. **`Elegia` / EI (洛谷 / UOJ)**: Tutorials on `[ZJOI2019] 开关`, `CF 1349D`, and ODE/rational post-processing of PGFs.
   - Introduces the **EGF-to-OGF Renewal Bridge** ($e^{\lambda z} \mapsto \frac{1}{1 - \lambda x}$) combined with **pole cancellation at $x = 1$** ($\widetilde{H}(x) = (1-x)H(x)$), and demonstrates how high-degree rational PGFs can be differentiated or evaluated in $O(N)$ via D-finite ODEs.
4. **`rqy` & OI-Wiki**: *OI-Wiki: 概率生成函数 (PGF)* & *容斥原理 / 二项式反演*.
   - Emphasizes keeping the auxiliary variable $(y-1)$ symbolic inside `SEQ` and $\exp$ until the final polynomial extraction, rather than expanding PIE sums over subsets outside the generating function.

---

## Iteration 19: Japanese (`[JA]`) Deep-Dive on FPS PIE, Prefix-Subtract DP, and PGFs

### 19.1 Japanese Competitive Programming Literature (`maspy`, `noshi91`, `Nyaan`, `maroonrk`)
1. **`maspy` (`maspypy.com`)**: *形式的べき級数解説 (FPS Tutorial Series)* & AtCoder Editorials (`ABC260 Ex`, `AGC058 D`, `ARC115 E`, `ARC136 F`).
   - Categorizes 1D adjacent-constraint problems under **包除原理 + FPS (Inclusion–Exclusion + FPS)**: whenever items of colour $i$ have multiplicity $s_i$, construct the per-colour cluster polynomial $P_i(x) = \sum_{c=1}^{s_i} \binom{s_i-1}{c-1} (-1)^{s_i-c} \frac{x^c}{c!}$, multiply all $P_i(x)$ via a divide-and-conquer FFT tree in $O(N \log^2 N)$, and multiply $[x^C]$ by $C!$.
   - Highlights the **Prefix-Sum / CDQ FPS Interpretation of Alternating Cluster Signs**: in `ARC115 E`, a transition with alternating block signs $(-1)^{\ell-1} \min(A_{i-1} \dots A_j)$ can be maintained either via an explicit monotonic stack DP or understood as the coefficient extraction of an alternating run-cluster equation.
2. **`noshi91` (`noshi91.hatenablog.com`)**: *文字列の出現位置と形式的べき級数 (String Occurrences and FPS / Goulden–Jackson Cluster Method)*.
   - Presents the Goulden–Jackson Cluster Method as a formal language decomposition of marked occurrences where every overlapping chain of forbidden patterns has generating function $-\frac{x^{|u|}}{A_u(x)}$, immediately solvable via Bostan–Mori in $O(m \log m \log N)$.
3. **`Nyaan` (`nyaannyaan.github.io`)**: *FPS と包除原理・確率母関数 (FPS, Inclusion–Exclusion, and PGFs)*.
   - Contrasts the **Taylor Shift NTT routine** (`PolynomialTaylorShift(B, -1)`) for binomial inversion with the **EGF/OGF Renewal Bridge** for hypercube/grid random walks (`ARC136 F`, `ABC242 Ex`).

---

## Iteration 20: Unified Diagnostic Matrices, Multilingual Terminology, Citations & Master Audited Problem Bank

### 20.1 Unified Diagnostic Signal & Scratchpad Intuition Matrix

| Problem Signal / Bottleneck | Naive Trap | Correct FPS / PGF Transformation | Complexity |
|---|---|---|---|
| Count objects with **exactly $k$** violations when "choose $j$ violations and ignore the rest" has a clean product/GF $B(x, y)$ | Expanding $\sum_{j \ge k} (-1)^{j-k}\binom{j}{k} b_j$ after a slow 2D DP | Substitute $y \leftarrow y - 1$ **inside** the component GF ($A(x, y) = B(x, y-1)$), or apply Taylor Shift $B(y-1)$ via reversal NTT | $O(N \log N)$ or $O(N \log^2 N)$ |
| Sequence of $N$ items where **adjacent equal colours** ($c_t = c_{t+1}$) are forbidden or counted, with fixed colour counts $s_1, \dots, s_m$ | State-space DP tracking the last colour ($O(m N^2)$) | **Cluster ("Smearing") PIE / Carlitz–Scoville–Vaughan**: group each colour $i$ into $c_i$ clusters via $\widehat{C}_i(x,y) = \sum_{c_i=1}^{s_i} \binom{s_i-1}{c_i-1}(y-1)^{s_i-c_i}\frac{x^{c_i}}{c_i!}$, multiply via D&C FFT, and weight $[x^C]$ by $C!$ | $O(N \log^2 N)$ |
| Sequence where **maximal monochromatic runs** must satisfy a length constraint $R_v(x)$ (e.g., no run of length $\ge L$) | Maintaining run length in DP state ($O(N L)$) | **Automaton Isolation / Run-Cluster Transform**: replace $R_v(x)$ by $C_v(x) = \frac{R_v(x)}{1 + R_v(x)}$ inside $\frac{1}{1 - \sum_v C_v(x)}$ (for length $< L$, $C_v(x) = \frac{w_v x - (w_v x)^L}{1 - (w_v x)^L}$) | $O(N \log N)$ |
| Count strings of length $N$ avoiding (or having $k$ occurrences of) forbidden substrings $\mathcal{B} = \{u_1, \dots, u_k\}$ where $\sum |u_i|$ is large | Aho–Corasick DP with $M = \sum |u_i|$ states ($O(M^3 \log N)$ or $O(N M)$) | **Goulden–Jackson Cluster Method**: solve the $k \times k$ overlap system $\sum_{v} \operatorname{Corr}_{v \to u}(x) C_v(x) = -x^{|u|}$ and compute $F(x) = \frac{1}{1 - \sigma x - \sum C_u(x)}$ | $O(m \log m \log N)$ for $k=1$; $O(k^3 N + k^2 N \log N)$ for small $k$ |
| Expected time $\mathbb{E}[T]$ or variance $\operatorname{Var}(T)$ until a pattern $S$ (or one of $S_1, \dots, S_k$) first appears | Building a Markov chain on all $m$ KMP states and inverting an $m \times m$ matrix | **PGF Survival + Free Append**: combine $F(x) + (1-x)G(x) = 1$ with $G(x)(x/\sigma)^m = F(x) \sum_{\ell \in \operatorname{Borders}(S)} (x/\sigma)^{m-\ell}$ and evaluate at $x=1$ | $O(m)$ for $k=1$; $O(k^3 + k^2 m)$ for $k$ patterns |
| Expected first-passage time $\mathbb{E}[T_{s \to t}]$ on a switch/flip/hypercube walk where unrestricted walks factorize as an EGF $\widehat{H}(z) = \sum_\lambda c_\lambda e^{\lambda z}$ | $2^n \times 2^n$ Gaussian elimination on the state space | **First-Passage Renewal + EGF-to-OGF Bridge + Pole Cancellation**: map $e^{\lambda z} \mapsto \frac{1}{1-\lambda x}$, multiply by $(1-x)$ to cancel the $\lambda=1$ pole, and compute $\mathbb{E}[T] = \frac{1}{d_1}\sum_{\lambda \neq 1} \frac{d_\lambda - c_\lambda}{1 - \lambda}$ | $O(N \sum p_i)$ knapsack DP or $O(2^n \cdot n)$ FWT |

---

### 20.2 Multilingual Terminology Matrix (`[EN]` / `[ZH]` / `[JA]`)

| Concept | English (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) |
|---|---|---|---|
| Binomial Inversion / Exact-$k$ PIE | Binomial Inversion / Generalized Inclusion–Exclusion | 二项式反演 / 恰好 $k$ 个与钦定 $k$ 个 | 二項反転 / 包除原理（ちょうど $k$ 個） |
| Polynomial Taylor Shift | Polynomial Taylor Shift ($B(y-1)$) | 多项式平移 / 泰勒展开平移 | 多項式の平行移動 (Taylor Shift) |
| Adjacent-Violation / Smirnov PIE | Carlitz–Scoville–Vaughan / Smirnov Words / Cluster PIE | 连续段容斥 / 相邻限制容斥 | ランレングス包除 / 隣接制約の包除原理 + FPS |
| Goulden–Jackson Cluster Method | Goulden–Jackson Cluster Method | Goulden–Jackson 簇方法 / 字符串重叠容斥 | Goulden–Jackson Cluster Method / 文字列重なり包除 |
| Autocorrelation Polynomial | Autocorrelation / Overlap Polynomial | 自相关多项式 / Border 多项式 | 自己相関多項式 |
| Probability Generating Function | Probability Generating Function (PGF) | 概率生成函数 (PGF) | 確率母関数 (PGF) |
| First-Passage Renewal Division | First-Passage Renewal Equation ($F = H_{s \to t}/H_{t \to t}$) | 首次到达生成函数 / 按首次到达拆分 | 初到達母関数 / 更新方程式 |
| Martingale Potential Function | Martingale / Poisson Equation Potential | 势能函数 / 鞅与停时定理 | ポテンシャル関数 / マルチンゲール |

---

### 20.3 Bibliographic Citations Table

| Ref ID | Author / Source | Year | Title & Venue / URL | Core Contribution Audited |
|---|---|---|---|---|
| `[EN-1]` | I. P. Goulden & D. M. Jackson | 1979 | *An inversion theorem for cluster decompositions of sequences with distinguished subsequences*, J. London Math. Soc. (2) 20, 567–576 | Original derivation of the Goulden–Jackson Cluster Method for marked substring occurrences. |
| `[EN-2]` | J. Noonan & D. Zeilberger | 1999 | *The Goulden–Jackson Cluster Method: Extensions, Applications, and Implementations*, J. Difference Eq. Appl. 5, 355–377 | Algorithmic formulation of the $k \times k$ overlap linear system and bivariate $(y-1)$ marking. |
| `[EN-3]` | L. Carlitz, R. Scoville & T. Vaughan | 1976 | *Enumeration of pairs of sequences by rises, falls and levels*, Manuscripta Math. 19, 211–243 | Smirnov word generating function $\bigl(1 - \sum \frac{x_i}{1+x_i}\bigr)^{-1}$ and adjacent-level cluster transformation. |
| `[EN-4]` | P. Flajolet & R. Sedgewick | 2009 | *Analytic Combinatorics*, Cambridge University Press (Chapters I, III, VIII) | Symbolic method with bivariate marking, Smirnov words (Example III.24), autocorrelation polynomials, and PGFs. |
| `[EN-5]` | H. S. Wilf | 2006 | *Generatingfunctionology* (3rd ed.), A K Peters / CRC Press | Rook polynomials, exact-$k$ PIE via $B(y-1)$, and PGF moment extraction. |
| `[RU-1]` | A. M. Odlyzko & L. B. Guibas | 1981 | *String overlaps, pattern matching, and nontransitive games*, J. Combin. Theory Ser. A 30(2), 183–208 | Autocorrelation polynomials, Penney's game linear system, and generating functions for pattern avoidance. |
| `[ZH-1]` | 杨懋龙 (Yang Maolong) | 2018 | *《浅谈生成函数在掷骰子问题上的应用》*, IOI 2018 中国国家集训队论文集 | Canonical Chinese CP reference for PGF stopping times, string hitting times (`歌唱王国`, `硬币游戏`), variance, and renewal division. |
| `[ZH-2]` | `command_block` | 2020 | *《生成函数杂谈》 & 《容斥原理与反演》*, Luogu Blog / Cnblogs | Formalization of `连续段容斥` (Block-Split PIE) and automaton isolation $C_v(x) = \frac{R_v(x)}{1+R_v(x)}$. |
| `[ZH-3]` | `Elegia` (EI) | 2019–2020 | *ZJOI2019 开关 题解 & CF1349D 题解*, Luogu / UOJ Blog | EGF-to-OGF renewal bridge ($e^{\lambda z} \mapsto \frac{1}{1-\lambda x}$), pole cancellation at $x=1$, and Martingale potential duality. |
| `[JA-1]` | `maspy` | 2022–2023 | *形式的べき級数解説 & AtCoder Editorials (`ABC260 Ex`, `AGC058 D`, `ARC115 E`, `ARC136 F`)*, `maspypy.com` | Japanese FPS + PIE cluster synthesis, divide-and-conquer FFT merging of cluster EGFs, and PGF walks. |
| `[JA-2]` | `noshi91` & `Nyaan` | 2021–2023 | *文字列の出現位置と形式的べき級数 & FPS ライブラリ解説*, Hatena Blog / GitHub Pages | Goulden–Jackson + Bostan–Mori pipeline and Taylor shift / PGF implementations. |

---

### 20.4 Explicitly Rejected Template / Library-Validation Problems

In accordance with repository editorial policy, the following pure template or routine validation problems were audited and **excluded** from the textbook problem ladders:
1. **Library Checker — `Polynomial Taylor Shift` (`polynomial_taylor_shift`)**: Pure implementation check of computing $B(x+c)$ via reversal NTT.
2. **Luogu P5395 — `第二类斯特林数·行` (Stirling Numbers of the Second Kind — Row)**: Direct convolution of $\sum_{j=0}^k \frac{(-1)^{k-j}}{(k-j)!} \frac{j^n}{j!}$ without a modelling layer.
3. **SPOJ `SUBLEX` / Basic Aho–Corasick Count Templates (small $N, \sum |u_i| \le 100$)**: Solvable by naive matrix exponentiation on the trie without cluster reduction.
4. **Pure Derangement / Montmort Number Templates ($D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$)**: Standard introductory calculus/PIE identity with no polynomial manipulation depth.
5. **Library Checker — `Sparse Polynomial Inv` / `Bostan–Mori` Raw Templates**: Pure black-box library verification without combinatorial translation.
6. **Standard Absorbing Markov Chain Gaussian Elimination ($V \le 100$)**: Direct $(I-Q)^{-1}\mathbf{1}$ matrix inversion without PGF renewal structure.

---

### 20.5 Master Audited Problem Bank (Clusters A–E, 33 Non-Template Problems)

#### Cluster A: Exact-$k$ vs. At-Least-$k$ Binomial Inversion, Taylor Shift & Factorized Bivariate PIE

##### Problem A1: AtCoder ABC172 E — `NEQ`
- **Metadata**: AtCoder `abc172_e` | URL: `https://atcoder.jp/contests/abc172/tasks/abc172_e` | **Difficulty**: `Stepping Stone` | **Role**: `TOPIC LADDER` | **Primary Topic**: Exact-$0$ PIE / Bivariate $(y-1)$ Substitution | **Secondary Topics**: EGF of Injections
- **Concise Inline Problem Statement & Constraints**:
  Count ordered pairs of sequences $(A, B)$ each of length $N$ with elements from $\{1, 2, \dots, M\}$ such that: (1) $A_i \neq A_j$ and $B_i \neq B_j$ for all $i \neq j$, and (2) $A_i \neq B_i$ for all $1 \le i \le N$. Output the count modulo $10^9 + 7$. Constraints: $1 \le N \le M \le 5 \cdot 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Fix any duplicate-free sequence $A$ ($M^{\underline{N}}$ choices). We must count duplicate-free sequences $B$ such that $B_i \neq A_i$ for all $i$. Let property $P_i$ be the violation $B_i = A_i$. Choosing $j$ indices where $B_i = A_i$ forces those $j$ entries of $B$ to match $A$ (1 way) and leaves the remaining $N-j$ entries of $B$ to be chosen as distinct elements from the remaining $M-j$ values in $(M-j)^{\underline{N-j}}$ ways. Thus the relaxed polynomial is $B(y) = M^{\underline{N}} \sum_{j=0}^N \binom{N}{j} (M-j)^{\underline{N-j}} y^j$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Evaluating $A(0) = B(-1)$ immediately gives $M^{\underline{N}} \sum_{j=0}^N (-1)^j \binom{N}{j} (M-j)^{\underline{N-j}}$ in $O(N)$ time. Moreover, if the problem asked for the answer for **all** $k = 0, \dots, N$ matches simultaneously, $A(y) = B(y-1)$ is a single Polynomial Taylor Shift computable in $O(N \log N)$ via reversal NTT.
- **Progressive Hints**:
  - *Hint 1*: Fix sequence $A$ first; by symmetry, the number of valid sequences $B$ does not depend on which $A$ was chosen.
  - *Hint 2*: What happens if you choose $j$ positions where $B_i = A_i$ and allow the remaining $N-j$ positions of $B$ to be any distinct elements from the remaining $M-j$ numbers?

##### Problem A2: Luogu P4491 — `[HAOI2018] 染色` (Coloring)
- **Metadata**: Luogu `P4491` | URL: `https://www.luogu.com.cn/problem/P4491` | **Difficulty**: `Stepping Stone` | **Role**: `TOPIC LADDER` | **Primary Topic**: Exact-$k$ Binomial Inversion as Reversal NTT ($A(y) = B(y-1)$) | **Secondary Topics**: EGF Multinomial Counting
- **Concise Inline Problem Statement & Constraints**:
  You are given a sequence of length $N$, $M$ available colours, and a threshold $S$. If a colour appears **exactly** $S$ times in the sequence, it is called a "featured colour". Given weights $W_0, W_1, \dots, W_M$, a colouring with **exactly** $k$ featured colours has weight $W_k$. Find the sum of weights over all $M^N$ colourings modulo $1004535809$. Constraints: $N \le 10^7$, $M \le 10^5$, $S \le 150$.
- **Bridge 1 (English $\to$ Initial GF)**:
  A featured colour requires $\text{cnt}(c) = S$, so at most $L = \min(M, \lfloor N/S \rfloor)$ colours can be featured. If we **choose** $j$ colours to appear exactly $S$ times each and leave the remaining $M - j$ colours completely unconstrained on the remaining $N - jS$ positions, the relaxed count is:
  $$b_j = \binom{M}{j} \frac{N!}{(S!)^j (N - jS)!} (M - j)^{N - jS} \quad (0 \le j \le L).$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Let $B(y) = \sum_{j=0}^L b_j y^j$. The exact-$k$ polynomial is $A(y) = B(y-1)$, so $k!\, a_k = \sum_{j=k}^L (j!\, b_j) \frac{(-1)^{j-k}}{(j-k)!}$. Because $1004535809 = 479 \cdot 2^{21} + 1$ is NTT-friendly, we precompute factorials up to $N = 10^7$ in $O(N)$ and run a single reversal NTT of size $L \le 10^5$ in $O(M \log M)$.
- **Progressive Hints**:
  - *Hint 1*: Can you count the number of colourings $b_j$ where a chosen subset of $j$ colours each appear *exactly* $S$ times, and the remaining $M-j$ colours are used arbitrarily on the remaining $N-jS$ slots?
  - *Hint 2*: Express $a_k$ in terms of $b_j$ via $A(y) = B(y-1)$ and rewrite $\binom{j}{k}$ as $\frac{j!}{k!(j-k)!}$ to turn the sum into a convolution.

##### Problem A3: Codeforces 1228E — `Another Filling the Grid` / Luogu P4859 — `已经没有什么好害怕的了`
- **Metadata**: Codeforces `1228E` / Luogu `P4859` | URL: `https://codeforces.com/problemset/problem/1228/E` & `https://www.luogu.com.cn/problem/P4859` | **Difficulty**: `Intermediate` | **Role**: `TOPIC LADDER` | **Primary Topic**: Factorized Bivariate PIE (`(y-1)` inside DP / Product) | **Secondary Topics**: Rook Polynomials on Ferrers Boards
- **Concise Inline Problem Statement & Constraints**:
  - *CF 1228E*: Fill an $n \times n$ grid with integers in $[1, K]$ ($n \le 250, K \le 10^9$) such that every row and every column has minimum element $1$.
  - *Luogu P4859*: Given two sorted arrays $A, B$ of length $N \le 2000$ ($2N$ distinct integers) and $K$, count matchings $\pi \in S_N$ with **exactly** $\frac{N+K}{2}$ pairs satisfying $A_i > B_{\pi(i)}$ modulo $10^9 + 9$.
- **Bridge 1 (English $\to$ Initial GF)**:
  - In *CF 1228E*, if $j$ columns are chosen to violate the condition (all entries in $[2, K]$), each row independently has $(K-1)^j K^{n-j} - (K-1)^n$ valid assignments, so $B_{\text{row}}(y) = (K + (K-1)y)^n - (K-1)^n (1+y)^n$, and $B_{\text{grid}}(y) = \sum_{j=0}^n \binom{n}{j} y^j \bigl((K-1)^j K^{n-j} - (K-1)^n\bigr)^n$.
  - In *Luogu P4859*, sorting $A$ and $B$ makes the condition $A_i > B_j$ a prefix $1 \le j \le c_i$ (a Ferrers board). A 2D rook DP computes $r_j$ (ways to choose $j$ non-attacking cells with $A_i > B_{\pi(i)}$), and the remaining $N-j$ elements can be matched arbitrarily in $(N-j)!$ ways: $B(y) = \sum_{j=0}^N r_j (N-j)! y^j$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Evaluating $A(0) = B(-1)$ in *CF 1228E* avoids a $2n$-variable inclusion-exclusion by keeping rows exact and only applying $y \leftarrow -1$ to columns ($O(n \log n)$). In *Luogu P4859*, extracting $[y^{(N+K)/2}] B(y-1)$ gives the exact-$k$ matching count.
- **Progressive Hints**:
  - *Hint 1*: For *CF 1228E*, instead of applying PIE to both rows and columns ($2^{2n}$), fix the set of $j$ bad columns and enforce the row condition *directly* on each row.
  - *Hint 2*: For *Luogu P4859*, sort both arrays so the valid choices for $A_i > B_j$ form nested prefixes $c_1 \le c_2 \le \dots \le c_N$.

##### Problem A4: Luogu P5400 — `[CTS2019] 珍珠` (Pearls)
- **Metadata**: Luogu `P5400` / LOJ `3120` | URL: `https://www.luogu.com.cn/problem/P5400` | **Difficulty**: `Intermediate` | **Role**: `TOPIC LADDER` | **Primary Topic**: Factorized Bivariate PIE inside EGF Product + Taylor Shift | **Secondary Topics**: Parity EGF $\frac{e^x + e^{-x}}{2}$
- **Concise Inline Problem Statement & Constraints**:
  Given $N, M, D$, a sequence of $N$ pearls with colours in $\{1, \dots, D\}$ can form $\sum_{c=1}^D \lfloor \text{cnt}(c)/2 \rfloor$ pairs of matching pearls. Count how many of the $D^N$ sequences can form **at least** $M$ pairs modulo $998244353$. Constraints: $D \le 10^5$, $N \le 10^9$, $M \le 10^9$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Since $\sum_{c=1}^D \lfloor \text{cnt}(c)/2 \rfloor = \frac{N - (\text{number of odd-count colours})}{2}$, forming at least $M$ pairs is equivalent to having **at most** $K = N - 2M$ colours with **odd** frequency! If we choose $j$ colours and force them to have odd frequency (EGF $\frac{e^x - e^{-x}}{2}$) while leaving the remaining $D-j$ colours unconstrained (EGF $e^x$), the relaxed EGF for $j$ chosen odd colours is:
  $$\widehat{B}_j(x) = \binom{D}{j} \left(\frac{e^x - e^{-x}}{2}\right)^j (e^x)^{D-j}.$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Instead of computing $\widehat{B}_j(x)$ for each $j$ separately, package $y$ into the bivariate EGF and apply $y \leftarrow y - 1$:
  $$\widehat{A}(x, y) = \widehat{B}(x, y-1) = \left(e^x + (y-1)\frac{e^x - e^{-x}}{2}\right)^D = 2^{-D} \bigl((y+1)e^x + (1-y)e^{-x}\bigr)^D.$$
  Wait—you can either expand $b_j = n![x^n]\widehat{B}_j(x) = \binom{D}{j} 2^{-j} \sum_{r=0}^j (-1)^{j-r}\binom{j}{r} (D - 2j + 2r)^N$ via one convolution and then apply a Taylor Shift $A(y) = B(y-1)$, or expand $\bigl((y+1)e^x + (1-y)e^{-x}\bigr)^D$ directly via a single convolution and Taylor Shift in $O(D \log D)$!
- **Progressive Hints**:
  - *Hint 1*: Rewrite the condition $\sum_{c=1}^D \lfloor \text{cnt}(c)/2 \rfloor \ge M$ in terms of the number of colours that appear an **odd** number of times.
  - *Hint 2*: What is the EGF of a colour whose frequency is required to be odd, versus a colour whose frequency is completely unconstrained?

##### Problem A5: AtCoder AGC005 F — `Many Easy Problems`
- **Metadata**: AtCoder `agc005_f` | URL: `https://atcoder.jp/contests/agc005/tasks/agc005_f` | **Difficulty**: `Intermediate` | **Role**: `RESERVE ARCHIVE` | **Primary Topic**: Reversal NTT Convolution for Simultaneous Binomial Sums | **Secondary Topics**: Tree Linearity of Expectation
- **Concise Inline Problem Statement & Constraints**:
  Given a tree $T$ on $N \le 2 \cdot 10^5$ vertices, for every $k = 1, 2, \dots, N$, compute the sum of sizes of the minimal subtree spanning $S$ over all $\binom{N}{k}$ subsets $S \subseteq V$ of size $k$, modulo $924844033$.
- **Bridge 1 (English $\to$ Initial GF)**:
  By complementary counting, a vertex $v$ belongs to the minimal spanning subtree of $S$ unless $S$ falls entirely inside one of the connected components formed when $v$ is removed. Thus, if $c_s$ is the number of directed component-edges of size $s$, the answer for $k$ is $N \binom{N}{k} - \sum_{s=k}^N c_s \binom{s}{k}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Writing $\sum_{s=k}^N c_s \binom{s}{k} = \frac{1}{k!} \sum_{s=k}^N (s!\, c_s) \frac{1}{(s-k)!}$ is the exact reversal convolution of $(s!\, c_s)$ with $\frac{1}{t!}$ modulo the NTT-friendly prime $924844033 = 441 \cdot 2^{21} + 1$, computable for all $k$ in $O(N \log N)$.
- **Progressive Hints**:
  - *Hint 1*: Count for each vertex $v$ how many subsets $S$ of size $k$ do *not* include $v$ in their spanning subtree.
  - *Hint 2*: Collect the component sizes across all vertices into a frequency array $c_s$ and recognize $\sum_s c_s \binom{s}{k}$ as a reversal convolution.

##### Problem A6: Luogu P6596 — `How Many of Them`
- **Metadata**: Luogu `P6596` | URL: `https://www.luogu.com.cn/problem/P6596` | **Difficulty**: `Advanced` | **Role**: `RESERVE ARCHIVE` | **Primary Topic**: Bivariate PIE on Bridge-Block Trees + EGF $\exp/\ln$ | **Secondary Topics**: Labelled Connected Graph Counting
- **Concise Inline Problem Statement & Constraints**:
  Count connected labelled undirected graphs on $n \le 50$ vertices with **at most** $m$ bridges ($0 \le m \le \binom{n}{2}$) modulo $10^9 + 7$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Contracting 2-edge-connected components turns the graph into a tree of blocks connected by bridges. If we **choose** $j$ bridges to remain visible (cutting the graph into $j+1$ connected components $V_1, \dots, V_{j+1}$ with arbitrary edges inside each $V_r$ and $j$ tree edges between them), Cayley's generalized formula gives $\prod_{r=1}^{j+1} |V_r|$ times $n^{j-1}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Marking each chosen visible bridge with $(y-1)$ inside the rooted tree EGF equation converts the exact bridge-count EGF into an implicit equation solvable via polynomial $\ln/\exp$ or $O(n^4)$ coefficient extraction.
- **Progressive Hints**:
  - *Hint 1*: Instead of forcing the contracted blocks to be 2-edge-connected immediately, what if you choose $j$ bridges to cut the graph into $j+1$ connected components and allow those components to have arbitrary internal bridges?
  - *Hint 2*: How many ways can $j+1$ labelled components of sizes $s_1, \dots, s_{j+1}$ be linked into a tree by $j$ bridges?

---

#### Cluster B: Adjacent-Violation Cluster ("Smearing") PIE & Carlitz–Scoville–Vaughan / Smirnov Transformation

##### Problem B1: Codeforces 840C — `On the Bench`
- **Metadata**: Codeforces `840C` | URL: `https://codeforces.com/problemset/problem/840/C` | **Difficulty**: `Stepping Stone` | **Role**: `TOPIC LADDER` | **Primary Topic**: Fixed-Frequency Cluster EGF $\widehat{C}_i(x, 0)$ | **Secondary Topics**: Square-Free Core Equivalence Classes
- **Concise Inline Problem Statement & Constraints**:
  Given an array $a_1, \dots, a_n$ ($n \le 300, a_i \le 10^9$), count the number of permutations of the $n$ elements such that no two adjacent elements have a perfect square product ($a_{\pi(i)} a_{\pi(i+1)} \neq k^2$), modulo $10^9 + 7$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Removing square factors from each $a_i$ maps the condition "$a_i a_j$ is a square" to "their square-free cores are equal". Group the $n$ distinct elements by their square-free core into $m$ colour classes of sizes $s_1, \dots, s_m$. We need permutations of $n$ labelled items with no two adjacent items of the same colour.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  For colour $i$ with $s_i$ labelled items, partitioning them into $c_i$ ordered clusters with $(y-1)\big|_{y=0} = -1$ internal bonds gives the EGF:
  $$\widehat{C}_i(x) = s_i! \sum_{c_i=1}^{s_i} \binom{s_i-1}{c_i-1} (-1)^{s_i - c_i} \frac{x^{c_i}}{c_i!}.$$
  Then the answer is $\sum_{C=1}^n C!\, [x^C] \prod_{i=1}^m \widehat{C}_i(x)$, computable in $O(n^2)$.
- **Progressive Hints**:
  - *Hint 1*: Show that "product is a perfect square" is an equivalence relation on positive integers, partitioning the array into colour groups of sizes $s_1, \dots, s_m$.
  - *Hint 2*: Apply the cluster EGF $\widehat{C}_i(x)$ to each colour group and multiply the polynomials.

##### Problem B2: Luogu P5339 — `[TJOI2019] 唱、跳、rap和篮球`
- **Metadata**: Luogu `P5339` | URL: `https://www.luogu.com.cn/problem/P5339` | **Difficulty**: `Stepping Stone` | **Role**: `TOPIC LADDER` | **Primary Topic**: Contiguous-Block PIE + Polynomial Convolution | **Secondary Topics**: Bounded Multinomial EGF
- **Concise Inline Problem Statement & Constraints**:
  Count sequences of length $n$ over $\{A, B, C, D\}$ containing at most $a$ `A`s, $b$ `B`s, $c$ `C`s, and $d$ `D`s, and containing **no** contiguous substring `"ABCD"`, modulo $998244353$. Constraints: $n \le 1000$, $a, b, c, d \le 500$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Because two occurrences of `"ABCD"` cannot overlap, choosing $j$ disjoint occurrences of `"ABCD"` compresses those $4j$ positions into $j$ super-tokens and leaves $n - 4j$ individual letters with upper bounds $a-j, b-j, c-j, d-j$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  With $j$ chosen blocks compressed into $j$ tokens among $n - 3j$ total tokens, there are $\binom{n-3j}{j}$ ways to place the `"ABCD"` blocks, and the remaining $n - 4j$ positions are filled by $(n-4j)!\, [x^{n-4j}] \prod_{t \in \{a,b,c,d\}} \bigl(\sum_{r=0}^{t-j} \frac{x^r}{r!}\bigr)$. Multiplying the four truncated EGFs via NTT for each $0 \le j \le \min(n/4, a, b, c, d)$ gives the exact avoidance count $\sum_{j \ge 0} (-1)^j \binom{n-3j}{j} \dots$ in $O(n^2 \log n)$ (or $O(n^2)$ via sliding update).
- **Progressive Hints**:
  - *Hint 1*: Can two copies of `"ABCD"` ever overlap? What does that tell you about choosing $j$ occurrences of `"ABCD"`?
  - *Hint 2*: Once $j$ occurrences of `"ABCD"` are contracted into $j$ single tokens, how many ways can you distribute the remaining $n-4j$ letters subject to the upper bounds $a-j, b-j, c-j, d-j$?

##### Problem B3: AtCoder ARC115 E — `LEQ and NEQ`
- **Metadata**: AtCoder `arc115_e` | URL: `https://atcoder.jp/contests/arc115/tasks/arc115_e` | **Difficulty**: `Intermediate` | **Role**: `TOPIC LADDER` | **Primary Topic**: Adjacent-Inequality Cluster PIE ($w_t = w_{t+1}$ Smearing) | **Secondary Topics**: Monotonic Stack / Divide-and-Conquer DP
- **Concise Inline Problem Statement & Constraints**:
  Given $A_1, \dots, A_N$ ($N \le 5 \cdot 10^5, 1 \le A_i \le 10^9$), count sequences $X_1, \dots, X_N$ such that $1 \le X_i \le A_i$ for all $i$ and $X_i \neq X_{i+1}$ for all $1 \le i < N$, modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Mark each adjacent equality $X_t = X_{t+1}$ with weight $(y-1)\big|_{y=0} = -1$. A chosen subset of equalities partitions $1 \dots N$ into contiguous monochromatic blocks $[l+1, r]$. For a block $[l+1, r]$ where all $X_t$ are forced to be equal, their common value can be any integer in $[1, \min_{l < t \le r} A_t]$, and its PIE sign is $(-1)^{r - l - 1}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  This yields the block-split recurrence $dp[r] = \sum_{l=0}^{r-1} (-1)^{r-l-1} dp[l] \cdot \min_{l < t \le r} A_t$. Factoring $(-1)^r dp[r] = -\sum_{l=0}^{r-1} \bigl((-1)^l dp[l]\bigr) \min_{l < t \le r} A_t$ allows maintaining the segments of constant suffix minimum $\min_{l < t \le r} A_t$ on a monotonic stack in $O(N)$ time!
- **Progressive Hints**:
  - *Hint 1*: Apply the adjacent-equality cluster PIE: if $X_{l+1} = X_{l+2} = \dots = X_r$, how many valid values can that entire block take, and what is its $(-1)^{\text{length}-1}$ sign?
  - *Hint 2*: Absorb $(-1)^i$ into $dp[i]$ and use a monotonic stack to maintain the suffix minima $\min_{l < t \le r} A_t$.

##### Problem B4: AtCoder ABC260 Ex — `Colorfulness`
- **Metadata**: AtCoder `abc260_h` | URL: `https://atcoder.jp/contests/abc260/tasks/abc260_h` | **Difficulty**: `Advanced` | **Role**: `TOPIC LADDER` | **Primary Topic**: Bivariate Cluster EGF + Divide-and-Conquer FFT + Taylor Shift | **Secondary Topics**: Smirnov Words with Exact Adjacency Score
- **Concise Inline Problem Statement & Constraints**:
  You have $N$ balls ($N \le 2.5 \cdot 10^5$) with colours $c_1, \dots, c_N$. For every $k = 0, 1, \dots, N-1$, count the number of permutations of the $N$ distinct balls with **exactly** $k$ adjacent pairs $(i, i+1)$ having the same colour ($c_{p_i} = c_{p_{i+1}}$), modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Let $s_i$ be the count of balls of colour $i$. Choosing $j_i$ adjacent equal bonds inside colour $i$ partitions its $s_i$ balls into $c_i = s_i - j_i$ ordered clusters in $s_i! \binom{s_i - 1}{c_i - 1}$ ways. Using $x$ to mark the number of clusters $c_i$, a sequence of $C = \sum c_i$ clusters has $N - C$ chosen adjacent equalities!
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Notice that $j = \sum j_i = \sum (s_i - c_i) = N - C$ depends **only on the total number of clusters $C$**! Therefore, we don't even need a 2D polynomial: define the 1D cluster EGF for colour $i$ as
  $$P_i(x) = s_i! \sum_{c_i=1}^{s_i} \binom{s_i - 1}{c_i - 1} \frac{x^{c_i}}{c_i!}.$$
  Multiply $\prod_{i=1}^m P_i(x)$ in $O(N \log^2 N)$ via divide-and-conquer FFT. Then $b_j = (N - j)!\, [x^{N-j}] \prod_{i=1}^m P_i(x)$ is the relaxed count of permutations with $j$ chosen same-colour adjacencies, and a single **Polynomial Taylor Shift** $A(y) = B(y - 1)$ in $O(N \log N)$ produces all exact counts $a_0, \dots, a_{N-1}$!
- **Progressive Hints**:
  - *Hint 1*: If colour $i$ (with $s_i$ balls) is partitioned into $c_i$ clusters, how many chosen same-colour adjacent bonds does it contain? Sum this over all colours!
  - *Hint 2*: Since $j = N - C$, multiply the 1D polynomials $P_i(x)$ via D&C FFT to get $b_j$ for all $j$, then apply a Polynomial Taylor Shift $B(y-1)$ to get $a_k$ for all $k$.

##### Problem B5: AtCoder AGC058 D — `Yet Another ABC String`
- **Metadata**: AtCoder `agc058_d` | URL: `https://atcoder.jp/contests/agc058/tasks/agc058_d` | **Difficulty**: `Advanced` | **Role**: `TOPIC LADDER` | **Primary Topic**: Cyclic Rotation Run-Cluster PIE / Carlitz–Scoville–Vaughan | **Secondary Topics**: Binomial Coefficient Extraction
- **Concise Inline Problem Statement & Constraints**:
  Count strings containing $A$ copies of `'A'`, $B$ copies of `'B'`, and $C$ copies of `'C'` ($A, B, C \le 10^6$) that contain **none** of `"ABC"`, `"BCA"`, or `"CAB"` as contiguous substrings, modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  In cyclic order $\text{A} \to \text{B} \to \text{C} \to \text{A}$, any string can be uniquely segmented into maximal cyclic runs $w_1, w_2, \dots, w_k$ where each run steps $+1 \pmod 3$ at every adjacent pair (`A->B`, `B->C`, `C->A`), and between consecutive runs $w_r$ and $w_{r+1}$ the step is **not** $+1 \pmod 3$. The condition "no `"ABC"`, `"BCA"`, `"CAB"`" simply says that **every maximal cyclic run has length $\le 2$**!
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Apply the Carlitz–Scoville–Vaughan / cluster PIE to maximal cyclic runs: choosing a run to have length $\ge 3$ (or replacing valid run lengths $\{1, 2\}$ via $\frac{R}{1+R}$) means that in the PIE expansion, every forbidden cyclic step of length $3$ (`ABC`, `BCA`, or `CAB`) can be contracted. Specifically, contracting $j$ occurrences of cyclic triples reduces $(A, B, C)$ to $(A-j, B-j, C-j)$ simultaneously! Using the run-cluster formula for length $< 3$, each contracted triple carries weight $-1$, and the number of ways to interlace $k$ clusters with $A-j, B-j, C-j$ items reduces to a direct $O(A+B+C)$ single-sum over $j$!
- **Progressive Hints**:
  - *Hint 1*: Notice that `"ABC"`, `"BCA"`, and `"CAB"` are exactly the substrings of length $3$ where each character advances by $+1 \pmod 3$ (`A->B->C->A`).
  - *Hint 2*: What happens to the character counts $(A, B, C)$ whenever you contract any 3-step cyclic violation? Every such contraction removes exactly one `A`, one `B`, and one `C`!

##### Problem B6: AtCoder ARC093 F — `Dark Horse`
- **Metadata**: AtCoder `arc093_d` | URL: `https://atcoder.jp/contests/arc093/tasks/arc093_d` | **Difficulty**: `Intermediate` | **Role**: `BLIND CHECKPOINT` | **Primary Topic**: Subset Block PIE + Exponential Size Packing | **Secondary Topics**: Bitmask DP + Multinomial Placements
- **Concise Inline Problem Statement & Constraints**:
  In a single-elimination tournament of $2^N$ players ($N \le 16$), player $1$ beats everyone except $M$ dark horses $A_1 < A_2 < \dots < A_M$ ($M \le 16$), and among all other pairs the smaller index wins. Count the permutations of the $2^N$ players into bracket leaves such that player $1$ wins the tournament, modulo $10^9 + 7$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Along player $1$'s path to the root, the $N$ opposing subtrees have sizes $2^0, 2^1, \dots, 2^{N-1}$. Player $1$ wins iff none of the $N$ opposing subtree winners is in $\{A_1, \dots, A_M\}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Wait: a subtree of size $2^k$ has winner $A_i$ iff $A_i$ is the **minimum** element among all $2^k$ players in that subtree! Thus, if we choose a subset mask $S \subseteq \{0, \dots, N-1\}$ of subtrees whose winners are dark horses, we process $A_M, A_{M-1}, \dots, A_1$ in descending order: when $A_i$ is assigned to be the minimum of subtree $2^k$, the remaining $2^k - 1$ slots of that subtree must be chosen from players $> A_i$ that have not yet been placed in earlier chosen subtrees! Multiplying by $(-1)^{|S|}$ and filling the remaining $2^N - 1 - S$ slots in $(2^N - 1 - S)!$ ways gives an $O(M \cdot N \cdot 2^N)$ solution.
- **Progressive Hints**:
  - *Hint 1*: Partition the bracket (relative to player $1$'s leaf) into $N$ opposing subtrees of sizes $2^0, 2^1, \dots, 2^{N-1}$. What condition determines the winner of one of these subtrees?
  - *Hint 2*: Apply PIE over which subset of the $N$ subtrees have a dark horse as their minimum element, and process the dark horses in **descending** order so you always know how many larger players remain available.

##### Problem B7: AtCoder AGC043 D — `Merge Triplets`
- **Metadata**: AtCoder `agc043_d` | URL: `https://atcoder.jp/contests/agc043/tasks/agc043_d` | **Difficulty**: `Advanced` | **Role**: `BLIND CHECKPOINT` | **Primary Topic**: Prefix-Maximum Block Characterization + Run-Length EGF (`exp` / DP) | **Secondary Topics**: Permutation Cycle / Block Structure
- **Concise Inline Problem Statement & Constraints**:
  Count permutations of $(1, 2, \dots, 3N)$ ($N \le 2000$) that can be produced by merging $N$ blocks of length $3$ using the standard merge-sort step (always taking the minimum of the current front elements of the non-empty blocks), modulo $M$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Break the output permutation at every left-to-right maximum (record). Whenever a record $x$ is popped from the front of a block of length $3$, any subsequent elements in that same block that are **smaller** than $x$ will be popped **immediately** after $x$, forming a contiguous record-block of length $1, 2,$ or $3$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Therefore, a permutation of $1 \dots 3N$ can be formed iff its left-to-right maxima partition it into blocks of lengths $b_i \in \{1, 2, 3\}$ such that $c_1 \ge c_2$ (every length-$2$ block can be paired with a length-$1$ block to form an original triplet). In EGF terms, a record-block of length $k$ has weight $\frac{(k-1)!}{k!} x^k = \frac{x^k}{k}$, so we seek $(3N)!\, [x^{3N} y^{\ge 0}] \exp\bigl(x y + \frac{x^2}{2} y^{-1} + \frac{x^3}{3}\bigr)$, solvable in $O(N^2)$ via the ODE/recurrence for $\exp$.
- **Progressive Hints**:
  - *Hint 1*: Consider what happens in the merge process immediately after a new left-to-right maximum is output.
  - *Hint 2*: Characterize valid permutations by the lengths of the segments between consecutive left-to-right maxima.

##### Problem B8: Codeforces 1326F2 — `Wise Men (Hard Version)`
- **Metadata**: Codeforces `1326F2` | URL: `https://codeforces.com/problemset/problem/1326/F2` | **Difficulty**: `Mastery` | **Role**: `RESERVE ARCHIVE` | **Primary Topic**: Adjacent-1 Cluster Relaxation + Partition Subset Convolution + SOS Mobius Inversion | **Secondary Topics**: Set Power Series
- **Concise Inline Problem Statement & Constraints**:
  Given an adjacency matrix on $n \le 18$ vertices, for every binary string $s \in \{0, 1\}^{n-1}$, count Hamiltonian paths $v_1, \dots, v_n$ where $[v_i \text{ knows } v_{i+1}] = s_i$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Relaxing $0$-bits (ignoring non-edges and only requiring $1$-bits to be edges) partitions $1 \dots n$ into connected path chains of lengths $\lambda_1, \dots, \lambda_k \vdash n$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Since the relaxed count depends only on the **integer partition** $\lambda \vdash n$ ($p(18) = 385$), compute the subset convolution over vertex masks for each chain length, multiply along the $385$ partitions in the FWT/OR-transform domain, reconstruct each binary string's relaxed value from its run-length partition, and invert the $y \mapsto y-1$ relaxation via SOS Mobius inversion (`AND`-superset subtraction) in $O(2^n n^2 + p(n) 2^n)$.
- **Progressive Hints**:
  - *Hint 1*: If you relax `0` to mean "either `0` or `1`" and keep `1` as "must be an edge", what does a binary string $s \in \{0,1\}^{n-1}$ decompose into?
  - *Hint 2*: Notice that the relaxed count depends only on the multiset of lengths of the `1`-runs (an integer partition of $n$), and $p(18) = 385$ is tiny!

##### Problem B9: UOJ #450 — `[集训队作业2018] 复读机` (Repeater)
- **Metadata**: UOJ `450` / LOJ `2541` | URL: `https://uoj.ac/problem/450` | **Difficulty**: `Intermediate` | **Role**: `RESERVE ARCHIVE` | **Primary Topic**: Multiplicity Divisibility PIE + Roots of Unity Filter in EGFs | **Secondary Topics**: Multivariate Multinomial Expansion
- **Concise Inline Problem Statement & Constraints**:
  Count sequences of length $n \le 10^9$ over $k \le 5 \cdot 10^5$ characters where every character's count is divisible by $d \in \{1, 2, 3\}$, modulo $19491001$.
- **Bridge 1 (English $\to$ Initial GF)**:
  The EGF of a single character whose frequency is a multiple of $d$ is $F_d(x) = \sum_{m \ge 0} \frac{x^{md}}{(md)!} = \frac{1}{d} \sum_{j=0}^{d-1} \exp(\omega_d^j x)$, where $\omega_d$ is a primitive $d$-th root of unity modulo $p = 19491001$ ($d \mid p-1$ since $19491000$ is divisible by $3$).
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Then $n!\, [x^n] F_d(x)^k = d^{-k} n!\, [x^n] \bigl(\sum_{j=0}^{d-1} e^{\omega_d^j x}\bigr)^k$. For $d=2$ this is a 1D binomial sum in $O(k)$; for $d=3$ expanding $(e^x + e^{\omega x} + e^{\omega^2 x})^k = \sum_{a+b+c=k} \frac{k!}{a!b!c!} e^{(a + b\omega + c\omega^2)x}$ seems $O(k^2)$, unless one sets $u(z_1, z_2) = (z_1 + z_2\omega + \omega^2)^k$ or uses the roots-of-unity/PIE symmetry to evaluate in $O(k \log n)$ or $O(k^2)$ for the given subtasks!
- **Progressive Hints**:
  - *Hint 1*: Use the roots-of-unity filter $\frac{1}{d}\sum_{j=0}^{d-1} \exp(\omega^j x)$ to represent the EGF of a single character whose count is divisible by $d$.
  - *Hint 2*: Expand $\bigl(\sum_{j=0}^{d-1} \exp(\omega^j x)\bigr)^k$ into a linear combination of exponentials $\exp(\lambda x)$ and extract $n!\, [x^n] \exp(\lambda x) = \lambda^n$.

---

#### Cluster C: Forbidden Substrings & The Goulden–Jackson Cluster Method

##### Problem C1: CSES 1112 — `Required Substring` / yukicoder No. 1810
- **Metadata**: CSES `1112` / yukicoder `1810` | URL: `https://cses.fi/problemset/task/1112` & `https://yukicoder.me/problems/no/1810` | **Difficulty**: `Stepping Stone` | **Role**: `TOPIC LADDER` | **Primary Topic**: Single-Pattern Autocorrelation $A_u(x)$ & Goulden–Jackson Avoidance Formula | **Secondary Topics**: KMP Prefix Function + Bostan–Mori
- **Concise Inline Problem Statement & Constraints**:
  Given a pattern $S$ of length $m$ over an alphabet of size $\sigma$ (for CSES 1112: $\sigma = 26, m \le 100, n \le 1000$; for yukicoder / FPS generalizations: $m \le 10^5, n \le 10^{18}$), count strings of length $n$ that contain $S$ at least once (or avoid $S$ completely) modulo $10^9 + 7$ / $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  By complementary counting, the number of strings containing $S$ at least once is $\sigma^n - [x^n] F(x, 0)$, where $F(x, 0)$ counts strings avoiding $S$. Using the Goulden–Jackson cluster method for a single forbidden word $S$, a cluster of overlapping chosen copies of $S$ satisfies $A_S(x) C_S(x) = -x^m$, where $A_S(x) = \sum_{\ell \in \operatorname{Borders}(S)} x^{m - \ell}$ is the autocorrelation polynomial computed via the KMP border chain of $S$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Substituting $C_S(x) = -\frac{x^m}{A_S(x)}$ into $\frac{1}{1 - \sigma x - C_S(x)}$ yields the exact rational function:
  $$F(x, 0) = \frac{A_S(x)}{(1 - \sigma x) A_S(x) + x^m}.$$
  This bypasses building an $m$-state KMP automaton and extracts $[x^n] F(x, 0)$ in $O(m \log m \log n)$ via Bostan–Mori (or $O(n \log n)$ via FPS inversion for all $n \le N$).
- **Progressive Hints**:
  - *Hint 1*: Count strings that *avoid* $S$ instead, and consider how two occurrences of $S$ can overlap along a border of $S$.
  - *Hint 2*: Compute the autocorrelation polynomial $A_S(x) = \sum_{\ell \in \operatorname{Borders}(S)} x^{m - \ell}$ using KMP and apply $F(x, 0) = \frac{A_S(x)}{(1 - \sigma x) A_S(x) + x^m}$.

##### Problem C2: Codeforces GYM 102978H — `Harbingers of the Apocalypse` (XVIII Open Cup GP of Tokyo)
- **Metadata**: Codeforces GYM `102978H` | URL: `https://codeforces.com/gym/102978` | **Difficulty**: `Intermediate` | **Role**: `TOPIC LADDER` | **Primary Topic**: Single-Pattern Goulden–Jackson Cluster Method + Bostan–Mori | **Secondary Topics**: Weighted Alphabet Avoidance
- **Concise Inline Problem Statement & Constraints**:
  Given a forbidden binary/alphabet string $S$ of length $M \le 10^5$ and target length $N \le 10^{18}$, compute the probability (or count) that a random string of length $N$ never contains $S$ as a contiguous substring, modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Let $S(x) = \sum_{a \in \Sigma} p_a x$ be the 1-step letter generating function and $w(S) x^M$ be the weight of pattern $S$. The autocorrelation polynomial is $A_S(x) = 1 + \sum_{1 \le \ell < M, \text{border }\ell} w(S[\ell+1 \dots M]) x^{M - \ell}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  The Goulden–Jackson avoidance OGF is $F(x) = \frac{A_S(x)}{(1 - S(x)) A_S(x) + w(S) x^M}$. Since $\deg A_S < M \le 10^5$ and $N \le 10^{18}$, a single call to Bostan–Mori extracts $[x^N] F(x)$ in $O(M \log M \log N)$.
- **Progressive Hints**:
  - *Hint 1*: Does an Aho–Corasick / KMP matrix exponentiation fit in time for $M = 10^5$ and $N = 10^{18}$? Why does the Goulden–Jackson cluster method avoid tracking all $M$ prefix states?
  - *Hint 2*: Express the avoidance OGF as a ratio of degree-$M$ polynomials using the weighted autocorrelation polynomial $A_S(x)$ and apply Bostan–Mori.

##### Problem C3: Luogu P3311 — `[SDOI2014] 数数` / Codeforces GYM 102331J (Multi-Pattern Comparison)
- **Metadata**: Luogu `P3311` / CF GYM `102331J` | URL: `https://www.luogu.com.cn/problem/P3311` | **Difficulty**: `Advanced` | **Role**: `TOPIC LADDER` | **Primary Topic**: Multi-Pattern Goulden–Jackson $k \times k$ Overlap System vs. Aho–Corasick | **Secondary Topics**: Reduced Pattern Set Preprocessing
- **Concise Inline Problem Statement & Constraints**:
  Given $k$ forbidden strings $u_1, \dots, u_k$ ($k \le 15$, $\sum |u_i| \le 5 \cdot 10^4$) and length $N \le 5 \cdot 10^4$, count strings of length $N$ avoiding all $u_i$ modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  First remove any pattern $u_i$ that contains another $u_j$ as a substring so $\mathcal{B} = \{u_1, \dots, u_k\}$ is reduced. Then the cluster generating functions $C_u(x)$ ($u \in \mathcal{B}$) satisfy the $k \times k$ polynomial linear system $\sum_{v \in \mathcal{B}} \operatorname{Corr}_{v \to u}(x) C_v(x) = -x^{|u|}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Whereas Aho–Corasick DP takes $O(N \sum |u_i|)$ (which TLEs when $N, \sum |u_i| = 5 \cdot 10^4$), the Goulden–Jackson system has dimension $k \times k$ ($k \le 15$)! Converting each polynomial $\operatorname{Corr}_{v \to u}(x) \bmod x^{N+1}$ into its NTT point-value representation of length $2^{\lceil \log_2(N+1) \rceil}$ decouples the polynomial system into $2^L$ independent $k \times k$ scalar linear systems over $\mathbb{F}_p$, solvable in $O(k^2 N \log N + k^3 N)$!
- **Progressive Hints**:
  - *Hint 1*: Remember to filter out any forbidden string that contains another forbidden string as a substring before setting up the overlap matrix.
  - *Hint 2*: How can you solve a $k \times k$ system of polynomial equations $\bmod x^{N+1}$ when $k \le 15$ and $N = 5 \cdot 10^4$? Apply NTT to each matrix entry and solve the $k \times k$ scalar system at each root of unity!

##### Problem C4: Codeforces 755G — `PolandBall and Many Other Balls`
- **Metadata**: Codeforces `755G` | URL: `https://codeforces.com/problemset/problem/755/G` | **Difficulty**: `Advanced` | **Role**: `RESERVE ARCHIVE` | **Primary Topic**: Bivariate Transfer / Cluster OGF + Bostan–Mori / Doubling | **Secondary Topics**: Chebyshev / matching polynomials on paths
- **Concise Inline Problem Statement & Constraints**:
  Given $n \le 10^9$ balls in a row and $k \le 2^{15}$, for each $m = 1, \dots, k$, count ways to form $m$ disjoint groups where each group is either a single ball $\{i\}$ or two adjacent balls $\{i, i+1\}$, modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  In bivariate variables ($x$ for ball count, $y$ for group count), a block of balls with chosen adjacent pairings has step transfer $1 - (1+y)x - y x^2$:
  $$F(x, y) = \frac{1}{1 - (1 + y)x - y x^2}.$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Extracting $[x^n] \frac{1}{1 - (1+y)x - y x^2} \bmod y^{k+1}$ via polynomial doubling of the Fibonacci-like recurrence $P_n(y) = (1+y) P_{n-1}(y) + y P_{n-2}(y)$ (with $P_{2m} = P_m^2 + y P_{m-1}^2$) computes all $k$ coefficients in $O(k \log k \log n)$.
- **Progressive Hints**:
  - *Hint 1*: Write the bivariate OGF $F(x, y)$ where $x$ marks the length of the row and $y$ marks the number of groups chosen.
  - *Hint 2*: Use the Cassini/d'Ocagne identity for the polynomials $P_n(y) = [x^n] F(x, y)$ to double the index $n \to 2n$ in $O(k \log k)$ per bit of $n$.

##### Problem C5: AtCoder AGC013 E — `Placing Squares`
- **Metadata**: AtCoder `agc013_e` | URL: `https://atcoder.jp/contests/agc013/tasks/agc013_e` | **Difficulty**: `Intermediate` | **Role**: `BLIND CHECKPOINT` | **Primary Topic**: Marked-Boundary `SEQ` Composition vs. Matrix Transfer | **Secondary Topics**: Combinatorial Interpretation of $\ell^2$ (`2` balls in segment)
- **Concise Inline Problem Statement & Constraints**:
  Divide a plank of length $N \le 10^9$ into segments at integer points, never cutting at $M$ forbidden points $X_1 < \dots < X_M$ ($M \le 10^5$), and sum the product of squares of segment lengths $\prod \ell_i^2$ over all valid partitions modulo $10^9 + 7$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Without forbidden points, the OGF of a single segment is $\sum_{\ell \ge 1} \ell^2 x^\ell = \frac{x(1+x)}{(1-x)^3}$, so the unconstrained total OGF is $\frac{1}{1 - \frac{x(1+x)}{(1-x)^3}} = \frac{(1-x)^3}{1 - 4x + 2x^2 - x^3}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Combinatorially, choosing a partition and weighting each segment by $\ell^2$ is equivalent to placing two distinguishable balls (white and black) in each segment, representable as a $3 \times 3$ transfer matrix $T$ for a normal unit step and $T_{\text{forbid}}$ at the $M$ forbidden cut points, computable in $O(M \log(\Delta X))$.
- **Progressive Hints**:
  - *Hint 1*: Interpret $\ell^2$ combinatorially as choosing an ordered pair of unit cells inside the segment of length $\ell$.
  - *Hint 2*: Track how many of the $\{0, 1, 2\}$ balls have been placed in the current active segment across each unit step.

##### Problem C6: Bivariate Exact-$K$ Pattern Occurrences (`Goulden–Jackson Bivariate Drill`)
- **Metadata**: Canonical Synthesis (`Noonan–Zeilberger` / QOJ String Drills) | **Difficulty**: `Advanced` | **Role**: `TOPIC LADDER` | **Primary Topic**: Bivariate Goulden–Jackson Cluster Method ($y \neq 0$) | **Secondary Topics**: Rational Coefficient Extraction in $K[y][[x]]$
- **Concise Inline Problem Statement & Constraints**:
  Given a pattern $u$ of length $m \le 2000$, alphabet size $\sigma$, length $N \le 2000$, and $K \le N$, count strings of length $N$ containing **exactly** $K$ (possibly overlapping) occurrences of $u$, modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  By the bivariate Goulden–Jackson theorem, $F(x, y) = \frac{1 + (1-y)(A_u(x)-1)}{(1 - \sigma x)(1 + (1-y)(A_u(x)-1)) + (1-y)x^m}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Substitute $z = y - 1$ (so $1 - y = -z$). Then $F(x, 1 + z) = \frac{1 - z(A_u(x)-1)}{1 - \sigma x - z\bigl((1-\sigma x)(A_u(x)-1) + x^m\bigr)}$. Expanding as a geometric series in $z$, the coefficient of $z^j$ is a polynomial power in $x$ of minimum degree $j$, from which $b_j = [x^N z^j] F(x, 1+z)$ and a single Taylor shift $A(y) = B(y-1)$ yields $[x^N y^K] F(x, y)$!
- **Progressive Hints**:
  - *Hint 1*: Set $z = y - 1$ in the bivariate Goulden–Jackson formula so that the denominator has the form $(1 - \sigma x) - z P(x)$.
  - *Hint 2*: Extract $[z^j]$ first to get a rational function of $x$, or compute $b_j = [x^N z^j]$ and invert via $A(y) = B(y-1)$.

##### Problem C7: Cyclic Forbidden Substrings (`Necklace Goulden–Jackson Trace Formula`)
- **Metadata**: Canonical Synthesis (`Goulden–Jackson Cyclic Extension` / UOJ/QOJ Drills) | **Difficulty**: `Mastery` | **Role**: `RESERVE ARCHIVE` | **Primary Topic**: Logarithmic Derivative / Matrix Trace of the Cluster Transfer Operator | **Secondary Topics**: Cyclic Words & Borders Wrap-Around
- **Concise Inline Problem Statement & Constraints**:
  Count cyclic words (or rooted necklaces of length $N \le 10^5$) over an alphabet of size $\sigma$ that contain **no** cyclic occurrence of a forbidden pattern $u$ of length $m \le N$, modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  In a cyclic word of length $N$, chosen occurrences of $u$ can either form linear clusters that wrap around the boundary $N \leftrightarrow 1$, or a single cyclic cluster that wraps all the way around the circle of length $N$!
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  When linear generating functions have the form $F(x) = \frac{1}{1 - W(x)} = \frac{Q(x)}{P(x)}$ where $W(x) = \sigma x + C_u(x)$ is the cluster generator, the cyclic sum where the root can fall anywhere inside a chosen component is given by the logarithmic derivative $x \frac{d}{dx} \ln \frac{1}{1 - W(x)} = \frac{x W'(x)}{1 - W(x)}$ plus the pure all-wrap-around periodic cluster correction $\operatorname{Tr}(T_{\text{overlap}}^N) = -x \frac{P'(x)}{P(x)}$, giving the remarkable identity $[x^N] \bigl(-x \frac{d}{dx} \ln P(x)\bigr)$ where $P(x) = \frac{(1-\sigma x)A_u(x) + x^m}{A_u(x)}$ when $N \ge m$!
- **Progressive Hints**:
  - *Hint 1*: Compare linear words $F(x) = \frac{A_u(x)}{(1-\sigma x)A_u(x) + x^m}$ with the trace $\sum \lambda_i^N$ of the underlying KMP transfer matrix.
  - *Hint 2*: Notice that the characteristic polynomial of the KMP avoidance automaton has reciprocal polynomial $P(x) = (1 - \sigma x)A_u(x) + x^m$ (divided by overlapping transient states), whose power sums $\sum \lambda_i^N$ are extracted by $-x \frac{d}{dx} \ln P(x)$!

---

#### Cluster D: Probability Generating Functions (PGFs), Stopping Times & String Hitting Games

##### Problem D1: Luogu P4548 — `[CTSC2006] 歌唱王国` (Singing Kingdom)
- **Metadata**: Luogu `P4548` | URL: `https://www.luogu.com.cn/problem/P4548` | **Difficulty**: `Stepping Stone` | **Role**: `TOPIC LADDER` | **Primary Topic**: PGF Survival Identity + Free Pattern Append | **Secondary Topics**: KMP Border Decomposition
- **Concise Inline Problem Statement & Constraints**:
  An alphabet has $\sigma \le 10^5$ characters, drawn uniformly and independently one by one. For $T \le 50$ query strings $S$ of length $m \le 10^5$, output the last $4$ digits ($\bmod 10^4$) of the expected number of characters drawn until $S$ appears as a contiguous substring.
- **Bridge 1 (English $\to$ Initial GF)**:
  Let $F(x)$ be the PGF of the stopping time and $G(x)$ be the OGF of surviving prefixes. Then $F(x) + (1-x)G(x) = 1$ and $G(x)(x/\sigma)^m = F(x) \sum_{\ell \in \operatorname{Borders}(S)} (x/\sigma)^{m-\ell}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Evaluating the second equation at $x = 1$ with $F(1) = 1$ immediately yields $\mathbb{E}[T] = G(1) = \sum_{\ell \in \operatorname{Borders}(S)} \sigma^\ell$, computable in $O(m)$ time via KMP!
- **Progressive Hints**:
  - *Hint 1*: Write the two PGF equations relating $F(x)$ (stops at step $n$) and $G(x)$ (survives step $n$) by considering (a) appending 1 random character to a survivor, and (b) appending the entire pattern $S$ to a survivor.
  - *Hint 2*: Set $x = 1$ in the second equation and use $F(1) = 1$ and $F'(1) = G(1)$.

##### Problem D2: Luogu P3706 — `[SDOI2017] 硬币游戏` (Coin Game / Multi-Pattern Penney's Game)
- **Metadata**: Luogu `P3706` | URL: `https://www.luogu.com.cn/problem/P3706` | **Difficulty**: `Intermediate` | **Role**: `TOPIC LADDER` | **Primary Topic**: Multi-Pattern PGF Hitting System | **Secondary Topics**: String Overlap Hashing / KMP + Gaussian Elimination
- **Concise Inline Problem Statement & Constraints**:
  $N \le 300$ players each choose a distinct binary string $S_i \in \{\texttt{H}, \texttt{T}\}^M$ ($M \le 300$). A fair coin is tossed repeatedly until one of the strings $S_i$ appears; that player wins. Compute the winning probability $P_i = F_i(1)$ of each player.
- **Bridge 1 (English $\to$ Initial GF)**:
  With $F_i(x)$ as the PGF of player $i$ winning at step $n$ and $G(x)$ as the survival OGF:
  $$\sum_{i=1}^N F_i(x) + (1 - x) G(x) = 1, \qquad G(x)\left(\frac{x}{2}\right)^M = \sum_{i=1}^N F_i(x) \sum_{\substack{1 \le \ell \le M \\ S_i[\text{suf }\ell] = S_j[\text{pref }\ell]}} \left(\frac{x}{2}\right)^{M - \ell} \quad (1 \le j \le N).$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Evaluating at $x = 1$ (and multiplying by $2^M$) yields $N+1$ linear equations in the $N+1$ unknowns $(F_1(1), \dots, F_N(1), G(1))$:
  $$\sum_{i=1}^N F_i(1) = 1, \qquad \sum_{i=1}^N F_i(1) \operatorname{Corr}_{S_i \to S_j}(2) - G(1) = 0 \quad (1 \le j \le N),$$
  solvable in $O(N^2 M + N^3)$.
- **Progressive Hints**:
  - *Hint 1*: For each player $j$, what happens if you append $S_j$ to a surviving string? Which player $i$ could possibly be triggered first, and at what overlap length $\ell$?
  - *Hint 2*: Evaluate the $N$ overlap equations and the survival equation at $x = 1$ to obtain an $(N+1) \times (N+1)$ linear system in $F_1(1), \dots, F_N(1)$ and $G(1)$.

##### Problem D3: String Hitting Time Variance (`Yang Maolong 2018 National Team Paper Drill`)
- **Metadata**: Canonical Synthesis (`[ZH-1]` Yang Maolong 2018) | **Difficulty**: `Intermediate` | **Role**: `TOPIC LADDER` | **Primary Topic**: Second Factorial Moment $F''(1) = 2 G'(1)$ & Variance Extraction | **Secondary Topics**: Differentiating PGF Overlap Identities
- **Concise Inline Problem Statement & Constraints**:
  Under the same setup as `[CTSC2006] 歌唱王国` (alphabet size $\sigma$, pattern $S$ of length $m \le 10^5$), compute the **variance** $\operatorname{Var}(T) = \mathbb{E}[T^2] - (\mathbb{E}[T])^2$ of the stopping time $T$ modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  From $F(x) + (1-x)G(x) = 1$ we have $F'(1) = G(1)$ and $F''(1) = 2G'(1)$, so $\operatorname{Var}(T) = 2G'(1) + G(1) - G(1)^2$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Differentiate $x^m G(x) = F(x) \sum_{\ell \in \operatorname{Borders}(S)} \sigma^\ell x^{m-\ell}$ at $x = 1$:
  $$m G(1) + G'(1) = F'(1) \sum_{\ell} \sigma^\ell + F(1) \sum_{\ell} (m - \ell)\sigma^\ell \implies G'(1) = G(1)^2 - \sum_{\ell \in \operatorname{Borders}(S)} \ell \sigma^\ell,$$
  which gives $\operatorname{Var}(T) = \bigl(\sum_{\ell \in \operatorname{Borders}(S)} \sigma^\ell\bigr)^2 + \sum_{\ell \in \operatorname{Borders}(S)} (1 - 2\ell)\sigma^\ell$ in $O(m)$ time!
- **Progressive Hints**:
  - *Hint 1*: Differentiate $F(x) = 1 - (1-x)G(x)$ twice at $x = 1$ to express $\operatorname{Var}(T)$ in terms of $G(1)$ and $G'(1)$.
  - *Hint 2*: Differentiate $x^m G(x) = F(x) \sum_{\ell \in \operatorname{Borders}(S)} \sigma^\ell x^{m-\ell}$ once at $x = 1$ and notice that the $m G(1)$ terms cancel on both sides!

##### Problem D4: AtCoder AGC038 E — `Gachapon`
- **Metadata**: AtCoder `agc038_e` | URL: `https://atcoder.jp/contests/agc038/tasks/agc038_e` | **Difficulty**: `Advanced` | **Role**: `TOPIC LADDER` | **Primary Topic**: Min-Max PIE + Multivariate EGF Stopping Time | **Secondary Topics**: Knapsack DP over Degree & Weight Sums
- **Concise Inline Problem Statement & Constraints**:
  Item $i \in \{1, \dots, N\}$ is drawn with probability $p_i = A_i / S$ ($S = \sum A_i$) and needs to be drawn at least $B_i$ times. Given $N \le 400, S = \sum A_i \le 400, \sum B_i \le 400$, find the expected number of draws until **every** item $i$ has been drawn at least $B_i$ times, modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  By Min-Max Inclusion–Exclusion ($\max_{i \in [N]} T_i = \sum_{\varnothing \neq T \subseteq [N]} (-1)^{|T|-1} \min_{i \in T} T_i$), for a fixed non-empty subset $T \subseteq [N]$, $\min_{i \in T} T_i$ is the time until **some** item $i \in T$ reaches $B_i$ draws. By the survival identity $\mathbb{E}[\min_{i \in T} T_i] = \sum_{k \ge 0} \Pr(\min_{i \in T} T_i > k)$, if we first condition on steps falling inside $T$ (probability $P_T = \frac{\sum_{i \in T} A_i}{S}$, so each effective step inside $T$ takes $1 / P_T$ real steps in expectation), the survival EGF inside $T$ is:
  $$\widehat{G}_T(z) = \prod_{i \in T} \left(\sum_{c_i = 0}^{B_i - 1} \frac{(A_i z)^{c_i}}{c_i! P_T^{c_i}}\right).$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Integrating $k!\, [z^k] \widehat{G}_T(z)$ over $k \ge 0$ means multiplying the coefficient of $z^k \left(\frac{\sum_{i \in T} A_i}{S}\right)^{-(k+1)}$ by $k!$. Because $\sum A_i \le 400$ and $\sum B_i \le 400$, we do not iterate over $2^N$ subsets $T$: we run a 2D polynomial DP over $(s = \sum_{i \in T} A_i,\; k = \sum_{i \in T} c_i)$, folding the $(-1)^{|T|-1}$ sign directly into each item's transition polynomial $-\sum_{c_i=0}^{B_i-1} \frac{A_i^{c_i}}{c_i!} z^{c_i}$ in $O(N \cdot (\sum A_i) \cdot (\sum B_i))$!
- **Progressive Hints**:
  - *Hint 1*: Apply Min-Max PIE to reduce "all items reach $B_i$" to "for a subset $T$, how many steps until the *first* item in $T$ reaches $B_i$?".
  - *Hint 2*: Within a subset $T$, write the EGF of sequences of draws from $T$ where every $i \in T$ appears $< B_i$ times, and use a 2D DP indexed by $(\sum_{i \in T} A_i, \sum_{i \in T} c_i)$ to sum over all $2^N - 1$ subsets $T$ at once!

##### Problem D5: AtCoder ABC242 Ex — `Random Painting`
- **Metadata**: AtCoder `abc242_h` | URL: `https://atcoder.jp/contests/abc242/tasks/abc242_h` | **Difficulty**: `Advanced` | **Role**: `BLIND CHECKPOINT` | **Primary Topic**: Subset PIE on Uncovered Cells + Geometric Survival PGF | **Secondary Topics**: Interval DP with PIE Signs
- **Concise Inline Problem Statement & Constraints**:
  There are $N \le 400$ white cells and $M \le \binom{N+1}{2}$ intervals $[L_j, R_j]$. Each step chooses one of the $M$ intervals uniformly at random and paints all cells in it black. Find the expected number of steps until all $N$ cells are black, modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  By Min-Max PIE over the set of cells $S \subseteq \{1, \dots, N\}$ that have not yet been painted, if $c(S)$ is the number of intervals completely disjoint from $S$, then the probability of surviving $k$ steps without painting any cell in $S$ is $\bigl(\frac{c(S)}{M}\bigr)^k$, so the survival OGF is $G(x) = \sum_{\varnothing \neq S \subseteq [N]} (-1)^{|S|-1} \frac{1}{1 - \frac{c(S)}{M} x}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Evaluating at $x = 1$ gives $\mathbb{E}[T] = G(1) = \sum_{k=0}^{M-1} \frac{M}{M - k} \sum_{S : c(S) = k} (-1)^{|S|-1}$. Since an interval $[L_j, R_j]$ is disjoint from $S$ iff it falls strictly between two consecutive elements of $S$, a 2D DP $dp[i][k]$ (last chosen element of $S$ is $i$, and $k$ intervals lie strictly to the left of $i$ without hitting $S$) computes the signed polynomial $\sum_S (-1)^{|S|-1} y^{c(S)}$ in $O(N^2 M) = O(N^4)$ time!
- **Progressive Hints**:
  - *Hint 1*: Use Min-Max PIE (or survival probability $\Pr(T > t)$) over non-empty subsets $S \subseteq \{1, \dots, N\}$ of cells that remain unpainted.
  - *Hint 2*: Notice that an interval $[L, R]$ avoids $S$ if and only if it is completely contained between two consecutive elements of $S$. Use DP over the last chosen element of $S$ and the count $k$ of avoided intervals!

---

#### Cluster E: First-Passage Renewal $H_{s \to t}(x) / H_{t \to t}(x)$, Pole Cancellation, EGF-to-OGF Bridge & Martingale Duality

##### Problem E1: Luogu P5326 — `[ZJOI2019] 开关` (Switches)
- **Metadata**: Luogu `P5326` / LOJ `3045` | URL: `https://www.luogu.com.cn/problem/P5326` | **Difficulty**: `Advanced` | **Role**: `TOPIC LADDER` | **Primary Topic**: First-Passage Renewal Division $F = H_{s \to t}/H_{t \to t}$ + EGF-to-OGF Renewal Bridge + Pole Cancellation | **Secondary Topics**: Subset-Sum DP on Exponential Modes $e^{\lambda z}$
- **Concise Inline Problem Statement & Constraints**:
  There are $n \le 100$ switches, initially all $0$, with target state $s_1, \dots, s_n \in \{0, 1\}$. At each step, switch $i$ is flipped with probability $p_i / P$ ($P = \sum_{i=1}^n p_i \le 5 \cdot 10^4$). Compute the expected number of steps to reach the target state $(s_1, \dots, s_n)$ for the **first time**, modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  The unrestricted walk EGF for reaching $s$ at step $m$ is $\widehat{H}_{0 \to s}(z) = \prod_{i=1}^n \frac{e^{(p_i/P)z} + (-1)^{s_i} e^{-(p_i/P)z}}{2} = \sum_{k=-P}^P c_k e^{(k/P)z}$, and the unrestricted return EGF is $\widehat{H}_{s \to s}(z) = \prod_{i=1}^n \frac{e^{(p_i/P)z} + e^{-(p_i/P)z}}{2} = \sum_{k=-P}^P d_k e^{(k/P)z}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Apply the EGF-to-OGF Laplace bridge $e^{(k/P)z} \mapsto \frac{1}{1 - (k/P)x}$ to get $H_{0 \to s}(x)$ and $H_{s \to s}(x)$, multiply both by $(1-x)$ to cancel the pole at $k = P$ ($\lambda = 1$, where $c_P = d_P = 2^{-n}$), and differentiate $F(x) = \frac{\widetilde{H}_{0 \to s}(x)}{\widetilde{H}_{s \to s}(x)}$ at $x = 1$:
  $$\mathbb{E}[T] = F'(1) = 2^n \sum_{k = -P}^{P - 1} \frac{d_k - c_k}{1 - k / P}.$$
  A simple 1D knapsack DP over $\pm p_i$ computes all coefficients $c_k, d_k$ in $O(n P)$ time!
- **Progressive Hints**:
  - *Hint 1*: Separate "reaching state $s$ at step $m$ (unrestricted)" from "reaching state $s$ for the *first time* at step $m$" using $H_{0 \to s}(x) = F_{0 \to s}(x) H_{s \to s}(x)$.
  - *Hint 2*: Expand the unrestricted EGFs as $\sum_{k=-P}^P c_k e^{(k/P)z}$, convert $e^{\lambda z} \mapsto \frac{1}{1 - \lambda x}$, and multiply numerator and denominator by $(1-x)$ before differentiating at $x = 1$!

##### Problem E2: AtCoder ARC136 F — `Flip Cells`
- **Metadata**: AtCoder `arc136_f` | URL: `https://atcoder.jp/contests/arc136/tasks/arc136_f` | **Difficulty**: `Mastery` | **Role**: `TOPIC LADDER` | **Primary Topic**: First-Passage Renewal Division + EGF-to-OGF Bridge + 2D Polynomial DP | **Secondary Topics**: Row-wise Binomial Flip Counting
- **Concise Inline Problem Statement & Constraints**:
  An $H \times W$ binary grid ($H, W \le 50$) starts at $S$ and has target $T$ where each row $i$ of $T$ is required to have $A_i$ ones (and we stop the first time the grid matches a specific target configuration or row-sum condition). At each step, one of the $H W$ cells is flipped uniformly at random. Find the expected stopping time modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  In each row $i$, let $d_i$ be the initial number of ones and $A_i$ the target number of ones. A cell in row $i$ flipped an odd/even number of times has EGF $\sinh(z/HW)$ or $\cosh(z/HW)$. Summing over valid target configurations in row $i$ gives a row EGF in $e^{z/HW}$ and $e^{-z/HW}$ of degree $W$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Multiplying the $H$ row polynomials gives $\widehat{H}_{\text{start} \to \text{target}}(z) = \sum_{k=-HW}^{HW} c_k e^{(k/HW)z}$ and $\widehat{H}_{\text{target} \to \text{target}}(z) = \sum_{k=-HW}^{HW} d_k e^{(k/HW)z}$, and the pole-cancelled renewal formula $\frac{1}{d_{HW}} \sum_{k < HW} \frac{d_k - c_k}{1 - k/(HW)}$ yields the exact expectation in $O(H^2 W^2)$.
- **Progressive Hints**:
  - *Hint 1*: Express the unrestricted EGF for each row $i$ as a polynomial in $u = e^{z/(HW)}$ and $u^{-1} = e^{-z/(HW)}$.
  - *Hint 2*: Apply $H_{\text{start} \to \text{target}}(x) = F(x) H_{\text{target} \to \text{target}}(x)$ and cancel the $(1-x)$ pole at $k = HW$.

##### Problem E3: AtCoder ABC289 Ex — `Trio`
- **Metadata**: AtCoder `abc289_h` | URL: `https://atcoder.jp/contests/abc289/tasks/abc289_h` | **Difficulty**: `Advanced` | **Role**: `TOPIC LADDER` | **Primary Topic**: Renewal Division $F = H_{s \to 0} / H_{0 \to 0}$ on 1D Lattice Walk + FPS Inv | **Secondary Topics**: Vandermonde / Reflection Convolution
- **Concise Inline Problem Statement & Constraints**:
  Three players start at coordinates $A, B, C$ on $\mathbb{Z}$ and each step independently move $+1$ or $-1$ with probability $1/2$. Find the expected probability that all three players meet at the **exact same coordinate** for the first time at step $T$ (or for all $n \le T \le 2 \cdot 10^5$), modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Notice that all three players meet at step $n$ at some coordinate $x$ iff $(X_n - A) + (B - A) = (Y_n - B) + (C - B) = \dots$; summing over the meeting coordinate $x \in \mathbb{Z}$ turns the unrestricted $n$-step meeting probability $h_{s \to \text{meet}, n}$ and return probability $h_{\text{meet} \to \text{meet}, n}$ into a single convolution of three binomial distributions!
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Specifically, $h_{\text{start}, n} = 8^{-n} \sum_{x} \binom{n}{\frac{n+x-A}{2}} \binom{n}{\frac{n+x-B}{2}} \binom{n}{\frac{n+x-C}{2}}$, which can be computed for all $n \le T$ via a single NTT convolution (writing $\binom{n}{i}\binom{n}{j} = \binom{n}{i}\binom{n}{n-j}$), and then first-passage renewal $F(x) = \frac{H_{\text{start}}(x)}{H_{\text{return}}(x)} \bmod x^{T+1}$ is a single **FPS Inv** in $O(T \log T)$!
- **Progressive Hints**:
  - *Hint 1*: Can three players who meet at coordinate $x_1$ and later meet at coordinate $x_2$ have different return distributions? By translation invariance of $\mathbb{Z}$, the return OGF $H_{\text{meet} \to \text{meet}}(x)$ does **not** depend on which coordinate $x$ they met at!
  - *Hint 2*: Compute $h_{\text{start}, n}$ and $h_{\text{return}, n}$ for all $n \le T$ using one convolution, then divide the two series via FPS Inv!

##### Problem E4: Codeforces 1349D — `Slime and Biscuits`
- **Metadata**: Codeforces `1349D` | URL: `https://codeforces.com/problemset/problem/1349/D` | **Difficulty**: `Mastery` | **Role**: `TOPIC LADDER` | **Primary Topic**: PGF Renewal / Martingale Potential Duality (`Elegia` Framework) | **Secondary Topics**: Tridiagonal Linear Recurrence for Potential $f(a_i)$
- **Concise Inline Problem Statement & Constraints**:
  There are $n \le 10^5$ players; player $i$ starts with $a_i$ biscuits ($S = \sum_{i=1}^n a_i \le 3 \cdot 10^5$). Each step picks one biscuit uniformly at random ($1/S$) and transfers it to one of the other $n-1$ players chosen uniformly at random ($1/(n-1)$). Find the expected number of steps until **some** player holds all $S$ biscuits, modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  By either PGF renewal symmetry across the $n$ absorbing states $e_i$ or `Elegia`'s Martingale Potential $\Phi(a_1, \dots, a_n) = \sum_{i=1}^n f(a_i)$, we seek a single-variable potential $f : \{0, 1, \dots, S\} \to \mathbb{R}$ such that the expected one-step change of $\sum_{i=1}^n f(a_i)$ is $-1$ for every non-terminal state $(a_1, \dots, a_n)$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Writing out $\mathbb{E}[\Delta \sum_i f(a_i)] = -1$ and decoupling the sum over $i = 1, \dots, n$ (since $\sum_{i=1}^n \frac{a_i}{S} = 1$) forces the per-player drift equation:
  $$\frac{a}{S} f(a - 1) + \frac{S - a}{S(n - 1)} f(a + 1) - \left(\frac{a}{S} + \frac{S - a}{S(n - 1)}\right) f(a) = -\frac{a}{S},$$
  which is a two-term recurrence in the first differences $\Delta f(a) = f(a+1) - f(a)$, solvable in $O(S)$ time! Then $\mathbb{E}[T] = \bigl(f(S) + (n-1)f(0)\bigr) - \sum_{i=1}^n f(a_i)$.
- **Progressive Hints**:
  - *Hint 1*: Look for an additive potential function $\Phi(a_1, \dots, a_n) = \sum_{i=1}^n f(a_i)$ whose expected change in one step is $-1$.
  - *Hint 2*: Notice that $\sum_{i=1}^n \frac{a_i}{S} = 1$, so you can distribute the constant $-1$ on the right-hand side as $-\sum_{i=1}^n \frac{a_i}{S}$ and equate the coefficient for each individual $a_i$!

##### Problem E5: Codeforces 1025G — `Company Acquisitions`
- **Metadata**: Codeforces `1025G` | URL: `https://codeforces.com/problemset/problem/1025/G` | **Difficulty**: `Advanced` | **Role**: `BLIND CHECKPOINT` | **Primary Topic**: Additive Martingale Potential $\sum f(a_i)$ | **Secondary Topics**: $f(k) = 2^k - 1$ Drift Cancellation
- **Concise Inline Problem Statement & Constraints**:
  $n \le 500$ companies are partitioned into active root companies, each with $a_i$ vassals. Each step chooses two active roots uniformly at random; one acquires the other (becoming a root with $a_i + 1$ vassals) while the acquired root's $a_j$ vassals are all released as independent active roots with $0$ vassals. Find the expected steps until a single root holds all $n-1$ vassals, modulo $10^9 + 7$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Seek an additive potential $\Phi = \sum_{\text{active } i} f(a_i)$ with $f(0) = 0$ such that every acquisition between $(a_i, a_j)$ increases $\Phi$ by $+1$ in expectation: $\frac{1}{2}\bigl(f(a_i + 1) + f(a_j + 1)\bigr) - f(a_i) - f(a_j) = 1$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  This decouples immediately into $\frac{1}{2} f(a + 1) - f(a) = \frac{1}{2} \implies f(a) = 2^a - 1$! Thus $\mathbb{E}[T] = f(n - 1) - \sum_{\text{active } i} f(a_i) = (2^{n-1} - 1) - \sum (2^{a_i} - 1)$ in $O(n)$ time!
- **Progressive Hints**:
  - *Hint 1*: What happens to $\sum f(a_i)$ when two active roots with $a_i$ and $a_j$ vassals interact, assuming $f(0) = 0$?
  - *Hint 2*: Solve $\frac{1}{2} f(a+1) - f(a) = \frac{1}{2}$ with $f(0) = 0$.

##### Problem E6: Luogu P5643 — `[PKUWC2018] 随机游走` (Random Walk on a Tree)
- **Metadata**: Luogu `P5643` | URL: `https://www.luogu.com.cn/problem/P5643` | **Difficulty**: `Advanced` | **Role**: `RESERVE ARCHIVE` | **Primary Topic**: Min-Max PIE + Tree Walk Elimination ($A_u x_{fa} + B_u$) + SOS DP (`FMT`) | **Secondary Topics**: Stopping Time on Graphs
- **Concise Inline Problem Statement & Constraints**:
  Given a tree on $n \le 18$ vertices rooted at $x$, answer $Q \le 5000$ queries: for a subset $S \subseteq V$, find the expected number of random walk steps starting at $x$ until **every** vertex in $S$ has been visited at least once, modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  By Min-Max PIE, $\mathbb{E}[\max_{v \in S} T_v] = \sum_{\varnothing \neq T \subseteq S} (-1)^{|T|-1} \mathbb{E}[\min_{v \in T} T_v]$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  For a fixed subset $T \subseteq V$, the expected hitting time $E_u$ to hit $T$ satisfies $E_u = 0$ for $u \in T$ and $E_u = 1 + \frac{1}{\deg(u)} \sum_{v \sim u} E_v$ for $u \notin T$. By bottom-up tree elimination $E_u = A_u E_{fa(u)} + B_u$, we find $E_x(T) = B_x$ in $O(n)$ for each of the $2^n$ subsets $T$, and precompute all subset sums via Fast Mobius Transform (SOS DP) in $O(n 2^n)$ to answer each query in $O(1)$!
- **Progressive Hints**:
  - *Hint 1*: Apply Min-Max PIE so you only need to compute the expected time to hit the *first* vertex in a subset $T$.
  - *Hint 2*: Use bottom-up tree Gaussian elimination ($E_u = A_u E_{fa(u)} + B_u$) for each mask $T$, then apply SOS DP over subsets $T \subseteq S$.

##### Problem E7: Second-Moment Switch Walk Variance (`Renewal Second Derivative at x = 1`)
- **Metadata**: Canonical Synthesis (`[ZH-1]` Yang Maolong / `[ZH-3]` `Elegia`) | **Difficulty**: `Mastery` | **Role**: `RESERVE ARCHIVE` | **Primary Topic**: Second Derivative of Pole-Cancelled Renewal Quotient $\widetilde{H}_{s \to t}(x) / \widetilde{H}_{t \to t}(x)$ | **Secondary Topics**: Variance of Hypercube Hitting Times
- **Concise Inline Problem Statement & Constraints**:
  In the setup of `[ZJOI2019] 开关` ($n \le 100$ switches, $P = \sum p_i \le 5 \cdot 10^4$), compute the **variance** $\operatorname{Var}(T) = F''(1) + F'(1) - F'(1)^2$ of the first-passage hitting time $T$, modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  With $\widetilde{H}_{0 \to s}(x) = (1-x)H_{0 \to s}(x) = c_P + (1-x)\sum_{k < P} \frac{c_k}{1 - (k/P)x}$ and $\widetilde{H}_{s \to s}(x) = d_P + (1-x)\sum_{k < P} \frac{d_k}{1 - (k/P)x}$, we have $F(x) = \frac{\widetilde{H}_{0 \to s}(x)}{\widetilde{H}_{s \to s}(x)}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Taking the second derivative of $\widetilde{H}(x) = c_P + (1-x) R(x)$ at $x = 1$ gives $\widetilde{H}'(1) = -R(1)$ and $\widetilde{H}''(1) = -2 R'(1) = -2 \sum_{k < P} \frac{c_k (k/P)}{(1 - k/P)^2}$. Substituting $\widetilde{H}(1), \widetilde{H}'(1), \widetilde{H}''(1)$ into the quotient rule for $F''(1) = \left(\frac{\widetilde{H}_{0 \to s}}{\widetilde{H}_{s \to s}}\right)''(1)$ yields $\operatorname{Var}(T)$ in $O(n P)$ time!
- **Progressive Hints**:
  - *Hint 1*: Write $\widetilde{H}(x) = c_P + (1-x) R(x)$ where $R(x) = \sum_{k < P} \frac{c_k}{1 - (k/P)x}$ is regular at $x = 1$.
  - *Hint 2*: Use Leibniz's rule on $(1-x) R(x)$ at $x = 1$ to see that $\widetilde{H}'(1) = -R(1)$ and $\widetilde{H}''(1) = -2 R'(1)$, then apply the second derivative of a quotient to $F(x) = \widetilde{H}_{0 \to s}(x) / \widetilde{H}_{s \to s}(x)$!
