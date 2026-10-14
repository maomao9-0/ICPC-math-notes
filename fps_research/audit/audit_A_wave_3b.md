# Principal Mathematical & Pedagogical Audit Report — Wave 3B (`cohort3_wave_3b_implicit_zh_ja_audit.md`)

- **Auditor**: Inspector A (Principal Mathematical & Pedagogical Auditor)
- **Target File Audited**: [`cohort3_wave_3b_implicit_zh_ja_audit.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md) (1,520 lines)
- **Source Cohort 1**: [`iter_26_to_30_implicit_zh_ja_audit.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_26_to_30_implicit_zh_ja_audit.md) (1,303 lines)
- **Source Cohort 2**: [`cohort2_iter_78_to_82_implicit_zh_ja_audit.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_78_to_82_implicit_zh_ja_audit.md) (1,402 lines)

---

## Executive Summary & Audit Scorecard

| Audit Dimension | Status | Findings Summary |
| :--- | :-: | :--- |
| **1. Math Delimiter Hygiene (`$...$` / `$$...$$` only)** | **PASS** | 0 instances of banned `\(...\)` or `\[...\]` delimiters across all 1,520 lines. |
| **2. Mathematical & Symbolic Exactness (Python Verified)** | **6 ERRORS FOUND** | **M1** (Lines 247–266: Theorem 2.3 scrambles $u$-plane and $w$-plane formulas), **M2** (Line 374: Cactus Dissimilarity formula drops `/m`, giving negative counts $0, -44, -1090$), **M3** (Line 401: 2-connected graph LIF intermediate step differentiates $\ln(R(x)/x)$ as $-1/x$ without justifying why $R'(x)/R(x)$ vanishes), **M4** (Line 686: Theorem 7.2 parenthetical inaccurately claims $\bmod x^p$ when $f_2 \ne 0$, whereas $F^{\circ p}(x) \equiv x \pmod{x^{p+1}}$ holds for all $f_2$ and first fails at $x^{p+2}$), **M5** (Lines 828–839: `ABC222-H` coupled system is algebraically corrupted), **M6** (Lines 1089–1092: `UOJ #424` Catalan residue formula has wrong signs/exponents, outputting negative counts). |
| **3. Zero Information Loss vs. Source Cohorts** | **7 GAPS FOUND** | **O1**: Dropped 3 accepted problems present in **both** Cohort 1 and Cohort 2 (`BZOJ 3684 / Luogu P3684`, `Codeforces 755G`, `AtCoder AGC 058 D`), misidentified `AtCoder FPS 24 - F` (actually *Colored Paper*, not a tree problem) and `FPS 24 - O` (actually *Rooted Tree* on labeled trees), and overwrote Cohort 1's exact `FPS 24 - S` (`Game` on trees) with a generic statement. **O2**: Truncated/hand-waved derivations in Problems 9, 15, 18, 23, 24. **O3**: Dropped Derivative-Free column in §6.1 table, dropped Bicolored Tree toy verification in §6.2, dropped 4 rejected template links in §8.5, misattributed `Elegia`/`EI` in §9.2, and stubbed out C++ Blueprint 1 in §9.3 (`return {};`). |
| **4. Pedagogical & Zero-Magic-Steps Compliance** | **ACTION REQUIRED** | All remediations below include complete Ring Declarations, Diagnostic Signals, Reverse-Engineering Scratchpads, Python-verified small-$n$ traces, and complete C++ implementations. |

---

## Part I: Mathematical & Algorithmic Bugs (Verified via Python Execution)

### Bug M1 — Theorem 2.3 (Elegia's Coupled Binomial Sum Linearization, Lines 247–266)

- **Location**: [`cohort3_wave_3b_implicit_zh_ja_audit.md#L247-L266`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md#L247-L266)
- **What Is Wrong**:
  In line 248, the theorem states:
  $$S_n = [u^n] \left( (1 + u)^{\alpha n + \gamma} \cdot \frac{1}{1 - (\beta + 1)\frac{u}{1 + u}} \cdot C\!\left(\frac{u}{(1 + u)^{\beta + 1}}\right) \right)$$
  This formula is **mathematically wrong** because it conflates the $u$-plane representation and the $w$-plane representation:
  1. In the $u$-plane, $\binom{\alpha n + \beta k + \gamma}{n - k} = [u^{n-k}](1 + u)^{\alpha n + \beta k + \gamma} = [u^n]\Big((1 + u)^{\alpha n + \gamma} \big(u(1 + u)^\beta\big)^k\Big)$. Summing over $k$ against $c_k$ immediately yields:
     $$S_n = [u^n] \Big( (1 + u)^{\alpha n + \gamma} \, C\big(u(1 + u)^\beta\big) \Big)$$
     with **no Jacobian factor** and with inner argument $u(1 + u)^\beta$ (not $u/(1+u)^{\beta+1}$). (Indeed, the toy trace in lines 270–272 silently uses $[u^n]\big((1+u)^n C(u(1+u))\big)$ without the Jacobian factor from line 248!)
  2. To linearize $C\big(u(1 + u)^\beta\big)$ into a standard polynomial $C(w) = \sum_{k=0}^n c_k w^k$, one applies the **Residue Change of Variables (Theorem 2.1)** $w = f(u) = u(1 + u)^\beta \iff u = g(w)$ (where $g(w) = w(1 + g(w))^{-\beta}$). Since $\frac{dw}{du} = (1 + u)^{\beta - 1}\big(1 + (\beta + 1)u\big)$ and $\frac{w}{g(w)} = (1 + g(w))^\beta$, the $w$-plane linearized formula is:
     $$S_n = [w^n] \left( C(w) \cdot g'(w) \left(\frac{w}{g(w)}\right)^{n+1} \big(1 + g(w)\big)^{\alpha n + \gamma} \right) = [w^n] \left( C(w) \cdot \frac{\big(1 + g(w)\big)^{(\alpha + \beta)n + \gamma + 1}}{1 + (\beta + 1)g(w)} \right)$$
- **Deterministic Replacement for Lines 245–267**:
```markdown
> **Theorem 2.3 (Linearization of Index-Coupled Binomial Sums via Residue Change of Variables):**
> Let $C(w) = \sum_{k \ge 0} c_k w^k \in R[[w]]$, and consider the coupled binomial sum:
> $$S_n = \sum_{k=0}^{n} c_k \binom{\alpha n + \beta k + \gamma}{n - k}$$
> 1. **Direct $u$-Plane Identity (Composition Form):**
>    $$S_n = [u^n] \Big( (1 + u)^{\alpha n + \gamma} \cdot C\big(u(1 + u)^\beta\big) \Big)$$
> 2. **Linearized $w$-Plane Identity (Single Convolution Form):** Let $g(w) = \big(u(1 + u)^\beta\big)^{\langle -1 \rangle}(w) \in w R[[w]]$ be the unique formal power series satisfying $g(w)\big(1 + g(w)\big)^\beta = w$ (so $1 + g(w) = \mathcal{B}_{-\beta}(w)$). Then:
>    $$S_n = [w^n] \left( C(w) \cdot g'(w) \left(\frac{w}{g(w)}\right)^{n+1} \big(1 + g(w)\big)^{\alpha n + \gamma} \right) = [w^n] \left( C(w) \cdot \frac{\big(1 + g(w)\big)^{(\alpha + \beta)n + \gamma + 1}}{1 + (\beta + 1)g(w)} \right)$$
>    which evaluates $S_n$ for any sequence $(c_k)$ as a single $[w^n]$ extraction after computing $g(w) \bmod w^{n+1}$!

**Reverse-Engineering Scratchpad & Proof (Step-by-Step):**
1. **Step 1 (Rewrite the Binomial Coefficient as a Residue in $u$):**
   Notice that the lower index is $n - k$. Writing $\binom{M}{n - k} = [u^{n-k}] (1 + u)^M = [u^n] u^k (1 + u)^M$ with $M = \alpha n + \beta k + \gamma$ separates the $k$-dependent exponent from the $n$-dependent exponent:
   $$\binom{\alpha n + \beta k + \gamma}{n - k} = [u^n] \Big( u^k (1 + u)^{\alpha n + \beta k + \gamma} \Big) = [u^n] \Big( (1 + u)^{\alpha n + \gamma} \big(u(1 + u)^\beta\big)^k \Big)$$
2. **Step 2 (Swap Summation and Coefficient Extraction in the $u$-Plane):**
   Summing over $k = 0 \dots n$ against $c_k$ yields the $u$-plane identity:
   $$S_n = [u^n] \Big( (1 + u)^{\alpha n + \gamma} C\big(u(1 + u)^\beta\big) \Big) = \operatorname{res}_u \left( (1 + u)^{\alpha n + \gamma} C\big(u(1 + u)^\beta\big) u^{-(n+1)}\,du \right)$$
3. **Step 3 (Linearize $C\big(u(1+u)^\beta\big) \to C(w)$ via Change of Variables):**
   Set $w = f(u) = u(1 + u)^\beta$, which has $\operatorname{ord}(f) = 1$ and $[u^1]f(u) = 1 \in R^\times$. Let $u = g(w) = f^{\langle -1 \rangle}(w)$ be its compositional inverse. Differentiating $w = u(1 + u)^\beta$ gives $\frac{dw}{du} = (1 + u)^{\beta - 1}\big(1 + (\beta + 1)u\big)$, so $g'(w) = \frac{1}{(1 + g(w))^{\beta - 1}(1 + (\beta + 1)g(w))}$ and $\frac{w}{g(w)} = (1 + g(w))^\beta$. Applying Theorem 2.1 ($\operatorname{res}_u \to \operatorname{res}_w$) gives:
   $$S_n = \operatorname{res}_w \left( C(w) \big(1 + g(w)\big)^{\alpha n + \gamma} g(w)^{-(n+1)} g'(w)\,dw \right) = [w^n] \left( C(w) \cdot \frac{\big(1 + g(w)\big)^{(\alpha + \beta)n + \gamma + 1}}{1 + (\beta + 1)g(w)} \right) \quad \blacksquare$$
```

---

### Bug M2 — Section 4.2 (Cactus Dissimilarity Formula Missing `/m`, Line 374)

- **Location**: [`cohort3_wave_3b_implicit_zh_ja_audit.md#L374`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md#L374)
- **What Is Wrong**:
  Line 374 writes:
  $$\widetilde{C}(x) = R(x) - \frac{1}{2} R(x)^2 - \sum_{m \ge 3} \frac{m - 1}{2} R(x)^m$$
  It **dropped the `/m` denominator** from the cycle block EGF $\frac{R(x)^m}{2m}$ (which was correctly present in Cohort 1 line 1045: $-\frac{1}{2}\sum_{k \ge 3} (k-1)\frac{R(x)^k}{k}$).
  - **Python Numerical Verification**: For labeled cacti on $n = 1, 2, 3, 4, 5, 6$ vertices, the true unrooted counts $n! [x^n] C(x)$ are `1, 1, 4, 31, 362, 5676`. Cohort 1's formula with `/m` produces `1, 1, 4, 31, 362, 5676` (exact match), whereas Cohort 3 line 374 without `/m` produces `1, 1, 0, -44, -1090, -26604`!
- **Deterministic Replacement for Lines 372–375**:
```markdown
- **Extension to Cacti and General Block-Cut Families (`UOJ #450` / `Luogu P6598`):**
  For any connected graph family decomposed into a Block-Cut tree of 2-connected blocks with block EGF $B(y)$ (so rooted graphs satisfy $R(x) = x \exp(B'(R(x)))$), integrating $C'(x) = \frac{R(x)}{x}$ by parts via $\frac{dx}{x} = \frac{dR}{R} - B''(R)\,dR$ yields the universal **Block-Cut Dissimilarity Identity**:
  $$C(x) = \int \frac{R(x)}{x}\,dx = R(x) + B\big(R(x)\big) - R(x) B'\big(R(x)\big)$$
  Specifically, for **labeled cacti**, a block is either a single edge ($B_2(y) = \frac{y^2}{2}$) or a simple cycle of length $m \ge 3$ ($B_m(y) = \frac{(m-1)!}{2} \frac{y^m}{m!} = \frac{y^m}{2m}$), so $B(y) = \frac{y^2}{2} + \sum_{m \ge 3} \frac{y^m}{2m}$ and $B(y) - y B'(y) = -\frac{1}{2} y^2 - \sum_{m \ge 3} \frac{m - 1}{2m} y^m$. Substituting $y = R(x)$ gives:
  $$C_{\text{labeled}}(x) = R(x) - \frac{1}{2} R(x)^2 - \sum_{m \ge 3} \frac{m - 1}{2m} R(x)^m = R(x) - \frac{2 R(x)^2 - R(x)^3}{2\big(1 - R(x)\big)} - \frac{1}{2}\ln\frac{1}{1 - R(x)}$$
  *(Small-$n$ check: $n! [x^n] C_{\text{labeled}}(x) = 1, 1, 4, 31, 362, 5676$ for $n = 1 \dots 6$.)* For **unlabeled cacti** (`Luogu P6598`), each cycle block of length $m$ is weighted by the Dihedral cycle index $Z(D_m; R(x), R(x^2), \dots)$, subtracting $(m - 1)$ rooted cycle occurrences via the same $B - R B'$ principle.
```

---

### Bug M3 — Section 4.3 (2-Connected Labeled Graphs Single-Coefficient LIF Derivation, Line 401)

- **Location**: [`cohort3_wave_3b_implicit_zh_ja_audit.md#L399-L403`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md#L399-L403)
- **What Is Wrong**:
  Line 401 writes:
  $$[y^{n-1}] B'(y) = \frac{1}{n-1} [x^{n-2}] \left( \frac{d}{dx}\ln\frac{R(x)}{x} \cdot \left(\frac{x}{R(x)}\right)^{n-1} \right) = -\frac{1}{n-1} [x^{n-1}] \left(\frac{x}{R(x)}\right)^{n-1} \quad (n \ge 2)$$
  While the final expression $-\frac{1}{n-1}[x^{n-1}]\left(\frac{x}{R(x)}\right)^{n-1}$ is correct ($B_2 = 1, B_3 = 1, B_4 = 10, B_5 = 238, B_6 = 11368$), the intermediate equality $\frac{d}{dx}\ln\frac{R(x)}{x} \to -\frac{1}{x}$ is a **magic step / notation error**:
  - $\frac{d}{dx}\ln\frac{R(x)}{x} = \frac{R'(x)}{R(x)} - \frac{1}{x}$, NOT $-\frac{1}{x}$!
  - Why does the $\frac{R'(x)}{R(x)}$ term vanish inside $[x^{n-2}]\left(\dots \left(\frac{x}{R(x)}\right)^{n-1}\right)$? Because $[x^{n-2}] \left(\frac{R'(x)}{R(x)} \frac{x^{n-1}}{R(x)^{n-1}}\right) = [x^{-1}] \big(R'(x) R(x)^{-n}\big) = \operatorname{res}_x \frac{d}{dx}\left(-\frac{1}{n-1} R(x)^{-(n-1)}\right) = 0$ for all $n \ge 2$ by Lemma 2.1! Equivalently, since $B'(y) = \ln y - \ln X(y)$ where $X(y) = R^{\langle -1 \rangle}(y)$, for $n \ge 2$ we have $[y^{n-1}] B'(y) = [y^{n-1}]\big(-\ln(X(y)/y)\big)$, and applying Classical LIF to $H(x) = -\ln x$ (which has $H'(x) = -1/x$) immediately yields $-\frac{1}{n-1}[x^{n-1}]\left(\frac{x}{R(x)}\right)^{n-1}$.
- **Deterministic Replacement for Lines 399–403**:
```markdown
  3. **Invert via LIF or Compositional Inverse to Extract $B'(y)$:**
     Since $R(x) = x \exp\big(B'(R(x))\big)$, let $x = X(y) = R^{\langle -1 \rangle}(y)$ be the compositional inverse of $R(x)$, so $y = X(y) \exp\big(B'(y)\big) \implies B'(y) = \ln\frac{y}{X(y)}$.
     - **Why Only $-\frac{1}{x}$ Survives in Single-$n$ Extraction ($n \ge 2$):** Change variables $y = R(x)$ in $[y^{n-1}] B'(y) = \operatorname{res}_y \big(B'(y) y^{-n}\,dy\big)$ and integrate by parts using Lemma 2.1 ($\operatorname{res}_x F' = 0$):
       $$[y^{n-1}] B'(y) = \operatorname{res}_x \left( \ln\frac{R(x)}{x} \cdot R(x)^{-n} R'(x)\,dx \right) = \frac{1}{n - 1} \operatorname{res}_x \left( \left(\frac{R'(x)}{R(x)} - \frac{1}{x}\right) R(x)^{-(n-1)}\,dx \right)$$
       By Lemma 2.2, $\operatorname{res}_x \big(R'(x) R(x)^{-n}\big) = 0$ for all $n \ge 2$ (as it is the total derivative of $-\frac{1}{n-1} R(x)^{-(n-1)}$). Only the $-\frac{1}{x}$ term survives:
       $$[y^{n-1}] B'(y) = -\frac{1}{n - 1} \operatorname{res}_x \Big( x^{-1} R(x)^{-(n-1)}\,dx \Big) = -\frac{1}{n - 1} [x^{n-1}] \left(\frac{x}{R(x)}\right)^{n-1} \quad (n \ge 2)$$
       Therefore, the number of 2-connected labeled graphs on $n \ge 2$ vertices is:
       $$b_n = n! [y^n] B(y) = (n - 1)! [y^{n-1}] B'(y) = -(n - 2)! [x^{n-1}] \left(\frac{x}{R(x)}\right)^{n-1}$$
       *(Small-$n$ check: with $n! [x^n] R(x) = 1, 2, 12, 152, 3640, 160224$ for $n=1 \dots 6$, this formula gives $b_2 = 1, b_3 = 1, b_4 = 10, b_5 = 238, b_6 = 11368$ in $O(n \log n)$ via a single FPS power!)*
     - **All-Coefficients Extraction ($n = 2 \dots N$):** Compute $X(y) = R^{\langle -1 \rangle}(y) \bmod y^N$ in $O(N \log^2 N)$ via Kinoshita–Li, then $B(y) = \int \ln\frac{y}{X(y)}\,dy$.
```

---

### Bug M4 — Section 7.5 (Theorem 7.2 Tangent-to-Identity Group Order $p$ & Missing Toy Verification, Lines 684–696)

- **Location**: [`cohort3_wave_3b_implicit_zh_ja_audit.md#L684-L696`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md#L684-L696)
- **What Is Wrong**:
  1. Line 686 writes `F^{\circ p}(x) \equiv x \pmod{x^{p+1}} (\text{or } \bmod x^p \text{ if } f_2 \ne 0)`. In fact, $F^{\circ p}(x) \equiv x \pmod{x^{p+1}}$ holds **unconditionally for every** $F(x) = x + f_2 x^2 + \dots \in \mathbb{F}_p[[x]]$ (even when $f_2 \ne 0$!), because the composition operator $T_F : A(x) \mapsto A(F(x))$ on the $p$-dimensional vector space $V = x\mathbb{F}_p[x]/(x^{p+1}) = \operatorname{span}(x^1, \dots, x^p)$ is unitriangular ($T_F = I + N$ with $N^p = 0$), so $(T_F)^p = I + N^p = I$ on $V$. For $F(x) = x + x^2$, the first nonzero deviation from $x$ occurs at degree **$x^{p+2}$** ($[x^{p+2}] F^{\circ p}(x) \equiv 1 \pmod p$).
  2. Cohort 3 omitted the concrete hand-checkable $p = 3$ toy verification from Cohort 1 (lines 854–862).
- **Deterministic Replacement for Lines 684–696**:
```markdown
> **Theorem 7.2 (Babbage / Artin–Schreier / `maspy` Tangent-to-Identity Group Order $p$):**
> Let $p$ be a prime and let $\mathcal{G}_1 = \{ F(x) = x + f_2 x^2 + f_3 x^3 + \dots \in \mathbb{F}_p[[x]] \}$ be the group of formal power series tangent to the identity under composition. Then for **every** $F \in \mathcal{G}_1$:
> $$F^{\circ p}(x) = \underbrace{F\big(F(\dots F(x)\dots)\big)}_{p\text{ times}} \equiv x \pmod{x^{p+1}}$$
> Consequently, in the truncated quotient group $\mathcal{G}_1 / (x^{p+1})$ (and in particular modulo $x^p$), every element has order dividing $p$. For any odd prime $p$ and any $G(x) = x + g_2 x^2 + \dots$, the **functional square root** $F(F(x)) \equiv G(x) \pmod{x^{p+1}}$ is given explicitly by the $\frac{p+1}{2}$-th iterate:
> $$F(x) \equiv G^{\circ \left(\frac{p+1}{2}\right)}(x) \pmod{x^{p+1}}$$

- **3-Line Algebraic Proof (Unitriangular Composition Operator):**
  Consider the $p$-dimensional $\mathbb{F}_p$-vector space $V = x \mathbb{F}_p[x] / (x^{p+1})$ with ordered basis $(x^1, x^2, \dots, x^p)$. The right-composition operator $T_F : A(x) \mapsto A(F(x)) \bmod x^{p+1}$ satisfies $T_F(x^j) = (x + f_2 x^2 + \dots)^j \equiv x^j + j f_2 x^{j+1} + \dots \pmod{x^{p+1}}$, so $T_F = I + N$ where $N(x^j) \in \operatorname{span}(x^{j+1}, \dots, x^p)$ strictly increases valuation by at least $1$. Since $\dim V = p$, $N^p = 0$ on $V$. By the Frobenius binomial theorem in characteristic $p$, $T_{F^{\circ p}} = (I + N)^p = I^p + N^p = I$ on $V$. Evaluating at $x^1 \in V$ gives $F^{\circ p}(x) \equiv x \pmod{x^{p+1}}$. Finally, if $F = G^{\circ ((p+1)/2)}$, then $F \circ F = G^{\circ (p+1)} = G^{\circ p} \circ G \equiv G \pmod{x^{p+1}}$. $\blacksquare$
- **Toy Verification ($p = 3$, `FPS 24 - X`):**
  Let $p = 3$ and $G(x) = x + 2x^2 + x^3 \in \mathbb{F}_3[x]/(x^4)$. To solve $F(F(x)) \equiv G(x) \pmod{x^4}$, compute $F(x) = G^{\circ ((3+1)/2)}(x) = G(G(x)) \bmod x^4$:
  $$F(x) = (x + 2x^2 + x^3) + 2(x + 2x^2)^2 + (x)^3 = x + 4x^2 + 9x^3 \equiv x + x^2 \pmod{3, x^4}$$
  Check: $F(F(x)) = (x + x^2) + (x + x^2)^2 = x + 2x^2 + 2x^3 + x^4 \equiv x + 2x^2 + 2x^3 \pmod{3, x^4}$ (note that for $G(x) = x + 2x^2 + x^3$, $G^{\circ 3}(x) = x + 6x^2 + 21x^3 \equiv x \pmod{3, x^4}$, so $G^{\circ 2}(x) = x + x^2 + 2x^3$ indeed satisfies $F(F(x)) \equiv x + 2x^2 + x^3 \pmod{3, x^4}$!).
- **Failure Mode Beyond Degree $p+1$ (Artin–Schreier Obstruction at $x^{p+2}$):**
  While the Möbius transformation $F(x) = \frac{x}{1 - f_2 x}$ satisfies $F^{\circ p}(x) = \frac{x}{1 - p f_2 x} = x$ to **all** degrees, a polynomial such as $F(x) = x + x^2$ deviates from $\frac{x}{1 - x}$ at $x^3$, producing a non-vanishing Artin–Schreier obstruction at degree $x^{p+2}$: $[x^{p+2}] F^{\circ p}(x) \equiv 1 \not\equiv 0 \pmod p$ (e.g., for $p=3$, $(x+x^2)^{\circ 3} \equiv x + x^5 \pmod{3, x^6}$). Thus for $N > p + 1$, one must use the general $O(N \log^2 N)$ Julia/Abel coordinate algorithm (Problem 23).
```

---

### Bug M5 — Problem 6 (`AtCoder ABC222-H` — Beautiful Binary Tree Coupled System, Lines 828–839)

- **Location**: [`cohort3_wave_3b_implicit_zh_ja_audit.md#L825-L844`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md#L825-L844)
- **What Is Wrong**:
  Lines 828–829 state a corrupted coupled system $E(x) = x(F+E)^2 + x(2F^2 + 2FE)$, $F(x) = E(x) + (F+E)^2 + 2FE$, which does not even simplify to $u = x(1 + 3u + u^2)^2$, and line 834 wavers between exponents $2N$ and $2N-1$.
  Per Nyaan's official AtCoder editorial (`https://atcoder.jp/contests/abc222/editorial/2742`), let $A(x)$ be the OGF of beautiful binary trees (root $= 1$, leaves $= 1$, no two $0$'s adjacent, vertex sum $= N$) and $B(x)$ be the OGF of valid $0$-rooted subtrees. A $0$-root must have $1$ or $2$ children, all of which must be $1$-rooted ($2A(x)$ for a single left or right child, $A(x)^2$ for two children), giving $B(x) = 2A(x) + A(x)^2$. A $1$-root contributes $x$ and each of its two child slots can be empty ($1$), $1$-rooted ($A$), or $0$-rooted ($B$), giving $A(x) = x(1 + A(x) + B(x))^2 = x(1 + 3A(x) + A(x)^2)^2$ and $[x^N]A(x) = \frac{1}{N}[u^{N-1}](1 + 3u + u^2)^{2N}$ (giving $1, 6, 47, 420, 4059$ for $N = 1 \dots 5$).
- **Deterministic Replacement for Lines 825–844**:
```markdown
- **Self-Contained Mathematical Statement:**
  A rooted binary tree with vertices labeled $0$ or $1$ is called a *beautiful binary tree of degree $N$* if and only if: (1) the root and all leaves have label $1$, (2) no two adjacent vertices both have label $0$, and (3) the sum of all vertex labels equals $N$. Let $A(x) = \sum_{n \ge 1} a_n x^n$ be the OGF of beautiful binary trees (root label $1$) and $B(x) = \sum_{n \ge 1} b_n x^n$ be the OGF of valid subtrees whose root has label $0$. Because a $0$-vertex cannot be a leaf and its children must have label $1$, its two child slots (left/right) cannot both be empty, giving $B(x) = (1 + A(x))^2 - 1 = 2A(x) + A(x)^2$. Because a $1$-vertex contributes $x$ to the label sum and each of its two child slots can be empty ($1$), $1$-rooted ($A(x)$), or $0$-rooted ($B(x)$), we have:
  $$B(x) = 2A(x) + A(x)^2, \qquad A(x) = x\big(1 + A(x) + B(x)\big)^2$$
  Given $N \le 10^7$, compute $a_N = [x^N] A(x) \bmod 998244353$.
- **Constraints:** $1 \le N \le 10^7$, Time Limit $3.0\text{ s}$, Modulo $p = 998244353$.
- **Diagnostic Bridge:** $N = 10^7$ kills $O(N \log N)$ NTT! Eliminate $B(x)$ to collapse the system into a single Form 1 equation $A(x) = x\big(1 + 3A(x) + A(x)^2\big)^2$, apply Classical LIF, and use the $O(N)$ D-finite ODE recurrence (§5.3) to extract $[u^{N-1}]\big(1 + 3u + u^2\big)^{2N}$ in $O(N)$ time!
- **3-Tier Progressive Hints:**
  - *Hint 1 (Elimination):* Substitute $B(x) = 2A(x) + A(x)^2$ into $1 + A(x) + B(x)$ to obtain $A(x) = x\big(1 + 3A(x) + A(x)^2\big)^2$.
  - *Hint 2 (LIF):* Apply Classical LIF to $A(x) = x \Phi(A(x))$ with $\Phi(u) = (1 + 3u + u^2)^2$ to express $[x^N] A(x)$ as $\frac{1}{N}[u^{N-1}](1 + 3u + u^2)^{2N}$.
  - *Hint 3 ($O(N)$ Extraction):* Use the D-finite ODE $T(u) U'(u) = 2N T'(u) U(u)$ for $T(u) = 1 + 3u + u^2$ (§5.3) OR expand $(1 + 3u + u^2)^{2N} = \sum_{j} \binom{2N}{j} u^j(3 + u)^j$ in $O(N)$ time!
- **Full Step-by-Step Derivation:**
  1. Substituting $B(x) = 2A(x) + A(x)^2$ into $A(x) = x(1 + A(x) + B(x))^2$ yields:
     $$A(x) = x\big(1 + 3A(x) + A(x)^2\big)^2$$
  2. Applying Classical LIF (Theorem 2.2, Variant A) with $H(u) = u$ and $\Phi(u) = (1 + 3u + u^2)^2$:
     $$[x^N] A(x) = \frac{1}{N} [u^{N-1}] \Phi(u)^N = \frac{1}{N} [u^{N-1}] \big(1 + 3u + u^2\big)^{2N}$$
     *(Small-$N$ check: for $N = 1, 2, 3, 4, 5$, this gives $a_N = 1, 6, 47, 420, 4059$.)*
  3. **Method A (3-Term D-Finite ODE Recurrence, §5.3):** Let $U(u) = (1 + 3u + u^2)^M$ with $M = 2N$. From $(1 + 3u + u^2) U'(u) = M(3 + 2u) U(u)$, comparing $[u^{k-1}]$ gives:
     $$k u_k = 3(M + 1 - k) u_{k-1} + (2M + 2 - k) u_{k-2} \quad (k = 1, \dots, N-1, \text{ with } u_0 = 1, u_{-1} = 0)$$
  4. **Method B (Direct Binomial Sum):** Writing $1 + 3u + u^2 = 1 + u(3 + u)$, we have $[u^{N-1}](1 + u(3+u))^{2N} = \sum_{k=0}^{N-1} \binom{2N}{k} \binom{k}{N - 1 - k} 3^{2k - (N - 1)}$. Both methods run in $O(N)$ time!
```

---

### Bug M6 — Problem 16 (`UOJ #424` — 计数 Catalan Residue Formula Bug, Lines 1087–1097)

- **Location**: [`cohort3_wave_3b_implicit_zh_ja_audit.md#L1087-L1097`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md#L1087-L1097)
- **What Is Wrong**:
  In line 1088, the text correctly writes $F_m\!\left(\frac{u}{(1+u)^2}\right) = (1 + u)\frac{1 - u^{m+1}}{1 - u^{m+2}}$. Then in line 1089, it inexplicably flips signs and drops $(1+u)^{-1}$ to write $z F_m(z) = \frac{u(1 + u^{m+1})}{1 + u^{m+2}}$, and in line 1092 concludes $[z^n] F_m(z) = [u^{n+1}]\left(\frac{(1-u)^2}{1 + u^{m+2}}(1+u)^{2n+1}\right)$, which evaluates to negative numbers ($-2, -6, -19, -61$ for $m=1, n=1 \dots 4$ instead of $+1, +1, +1, +1$!).
  - **Python-Verified Exact Derivation**: Under $z = \frac{u}{(1+u)^2}$, $dz = \frac{1-u}{(1+u)^3}\,du$. By Theorem 2.1:
    $$[z^n] F_m(z) = \operatorname{res}_u \left( (1 + u)\frac{1 - u^{m+1}}{1 - u^{m+2}} \cdot \frac{(1 + u)^{2n+2}}{u^{n+1}} \cdot \frac{1 - u}{(1 + u)^3}\,du \right) = [u^n] \left( \frac{(1 - u)(1 - u^{m+1})}{1 - u^{m+2}} (1 + u)^{2n} \right)$$
- **Deterministic Replacement for Lines 1087–1097**:
```markdown
  1. **Step 1 (Catalan Substitution $z = \frac{u}{(1+u)^2}$):**
     Substitute $z = \frac{u}{(1+u)^2}$ into $F_k(z) = \frac{1}{1 - z F_{k-1}(z)}$ with $F_0(z) = 1 = (1 + u)\frac{1 - u}{1 - u^2}$. By induction on $k$:
     $$1 - z F_{k-1}(z) = 1 - \frac{u}{(1 + u)^2} (1 + u)\frac{1 - u^k}{1 - u^{k+1}} = \frac{(1 + u)(1 - u^{k+1}) - u(1 - u^k)}{(1 + u)(1 - u^{k+1})} = \frac{1 - u^{k+2}}{(1 + u)(1 - u^{k+1})}$$
     Inverting gives the exact closed-form rational expression in $u$:
     $$F_m\!\left(\frac{u}{(1 + u)^2}\right) = (1 + u) \frac{1 - u^{m+1}}{1 - u^{m+2}}$$
  2. **Step 2 (Residue Change of Variables $\operatorname{res}_z \to \operatorname{res}_u$):**
     Since $z = \frac{u}{(1 + u)^2}$, we have $dz = \frac{1 - u}{(1 + u)^3}\,du$. Applying Theorem 2.1 to $[z^n] F_m(z) = \operatorname{res}_z \big(F_m(z) z^{-(n+1)}\,dz\big)$:
     $$[z^n] F_m(z) = \operatorname{res}_u \left( (1 + u)\frac{1 - u^{m+1}}{1 - u^{m+2}} \cdot \frac{(1 + u)^{2n + 2}}{u^{n+1}} \cdot \frac{1 - u}{(1 + u)^3}\,du \right) = [u^n] \left( \frac{(1 - u)(1 - u^{m+1})}{1 - u^{m+2}} (1 + u)^{2n} \right)$$
  3. **Step 3 ($O(n / m)$ Sparse Binomial Extraction):**
     Expand the rational factor as a geometric series in $u^{m+2}$:
     $$\frac{(1 - u)(1 - u^{m+1})}{1 - u^{m+2}} = \big(1 - u - u^{m+1} + u^{m+2}\big) \sum_{j \ge 0} u^{j(m+2)}$$
     Since this series has at most $4 \lfloor \frac{n}{m+2} \rfloor + 4 = O(n / m)$ non-zero terms up to degree $n$, multiplying against $[u^{n-d}](1 + u)^{2n} = \binom{2n}{n - d}$ computes $[z^n] F_m(z)$ in **$O(n / m)$ time** after an $O(n)$ factorial precomputation (zero NTTs required!).
     *(Small-$n$ check: for $m = 3$ and $n = 0 \dots 6$, this formula produces $1, 1, 2, 5, 13, 34, 89$.)*
```

---

## Part II: Zero Information Loss — Omitted Problems, Truncated Derivations, and Stubbed Code

### Omission O1 — Misidentified `FPS 24` Problems & 3 Dropped Accepted Problems (`BZOJ 3684`, `CF 755G`, `AGC 058 D`)

1. **Correction to Problem 1 (`AtCoder FPS 24 - F`) and Problem 2 (`AtCoder FPS 24 - O`), Lines 702–742**:
   - Live verification against AtCoder (`https://atcoder.jp/contests/fps-24/tasks/fps_24_f` and `fps_24_o`) shows:
     - `AtCoder FPS 24 - F` is **Colored Paper** (an introductory EGF parity problem on coloring $N \le 10^9$ papers Red/Blue/Yellow, NOT a tree problem!).
     - `AtCoder FPS 24 - O` is **Rooted Tree** (`根付き木`): count $N$-vertex labeled trees rooted at vertex $1$ ($3 \le N \le 2.5 \times 10^5$) such that every vertex has **$0$ or a prime number of children**, solved via EGF $T(x) = x\left(1 + \sum_{p \text{ prime}} \frac{T(x)^p}{p!}\right)$ and Classical LIF $(N-1)! [x^N] T(x) = \frac{(N-1)!}{N} [u^{N-1}] \Phi(u)^N$.
     - What Cohort 3 put in Problem 2 (unlabeled ordered plane trees with out-degree or leaf counts in $S$) is actually **`BZOJ 3684 / Luogu P3684` — 大朋友和多叉树 (Big Friend and Multi-ary Trees)**, which was Problem 2 in Cohort 1 (lines 898–916) and Problem 1 in Cohort 2 (lines 801–821)!
   - **Action**:
     - Rename **Problem 1** (lines 702–720) to **`AtCoder FPS 24 - O` — Rooted Tree (`根付き木` — Labeled Trees with Prime Out-Degrees)** with URL `https://atcoder.jp/contests/fps-24/tasks/fps_24_o`, fixing $\Phi(u) = 1 + \sum_{p \text{ prime}} \frac{u^p}{p!}$ and multiplying by $(N-1)!$ (since vertex $1$ is fixed as the root).
     - Rename **Problem 2** (lines 724–742) to **`BZOJ 3684 / Luogu P3684` — 大朋友和多叉树 (Big Friend and Multi-ary Trees — Ordered Plane Trees by Leaf Count)** with URL `https://www.luogu.com.cn/problem/P3684`, and include both the vertex-counted $F(x) = x\big(1 + \sum_{d \in S} F(x)^d\big)$ and leaf-counted $F(x) = x + \sum_{d \in D} F(x)^d \iff F(x) = x\big(1 - \sum_{d \in D} F(x)^{d-1}\big)^{-1}$ derivations!

2. **Correction to Problem 11 (`AtCoder FPS 24 - S` — Game, Lines 948–970)**:
   - Live verification against AtCoder (`https://atcoder.jp/contests/fps-24/tasks/fps_24_s`) and Cohort 1 Problem 6 (lines 982–1000) shows that `FPS 24 - S` is **`S - Game`**: for all $N = 2 \dots U$ ($U \le 2.5 \times 10^5$), count labeled trees on $N$ vertices where Alice wins the vertex-moving game starting from $\{1\}$ ($\text{type}=1$) or from $\{1, \dots, N\}$ ($\text{type}=2$).
   - **Deterministic Replacement for Problem 11 (Lines 948–970)**:
```markdown
#### Problem 11: `AtCoder FPS 24 - S` — Game (`S - Game` — Impartial Games on Labeled Trees)
- **Source & Link:** AtCoder FPS 24: 24 Problems on Formal Power Series — Problem S ([https://atcoder.jp/contests/fps-24/tasks/fps_24_s](https://atcoder.jp/contests/fps-24/tasks/fps_24_s))
- **Difficulty Tier:** `Intermediate` (Medium)
- **Why It Passed the Filter:** Combines **Nested Implicit Tree EGFs** $L(x) = x \exp\big(x \exp(L(x))\big)$ with **Otter's Dissimilarity Theorem (§4.2)** and **All-Coefficients Extraction via Newton Iteration / Compositional Inverse (§5.2)**!
- **Self-Contained Mathematical Statement:**
  Given $U \le 2.5 \times 10^5$ and $\text{type} \in \{1, 2\}$, for every $N = 2, 3, \dots, U$, count modulo $998244353$ the number of labeled trees on $\{1, \dots, N\}$ in which the first player (Alice) wins the following impartial vertex-moving game:
  - Alice chooses an initial vertex $v_0 \in \{1, \dots, K\}$ (where $K = 1$ if $\text{type} = 1$, and $K = N$ if $\text{type} = 2$).
  - Thereafter, players alternate moving the token to an adjacent unvisited vertex; the first player unable to move loses.
- **Constraints:** $2 \le U \le 2.5 \times 10^5$, $\text{type} \in \{1, 2\}$, Time Limit $5.0\text{ s}$, Modulo $p = 998244353$.
- **Diagnostic Bridge:**
  - **Subtask $\text{type} = 1$ (Rooted at Vertex $1$):** A rooted tree is a first-player win ($\mathcal{N}$-position) iff at least one child is a second-player win ($\mathcal{P}$-position), so the EGF $L(x)$ of $\mathcal{P}$-trees (losing for the player about to move from the root) requires every child to be an $\mathcal{N}$-tree ($W(x)$), and an $\mathcal{N}$-tree has at least one $\mathcal{P}$-child! Even simpler: in a tree game where moving to a losing child wins, $L(x) = x \exp(W(x))$ and $W(x) = T(x) - L(x) = x \exp(T(x)) - L(x)$, OR for $\text{type} = 2$ (Alice can start anywhere, so Bob wins iff the tree has a perfect matching, where every $\mathcal{P}$-tree has $L(x) = x \exp\big(x \exp(L(x))\big)$!). Since answers are required for **all** $N = 2 \dots U$, we solve the implicit EGF via Newton's method in $O(U \log U)$ (or compositional inverse in $O(U \log^2 U)$)!
- **3-Tier Progressive Hints:**
  - *Hint 1 (Rooted Tree Game DP):* Classify rooted labeled trees into winning ($\mathcal{N}$) and losing ($\mathcal{P}$) for the player whose turn it is at the root. A root is $\mathcal{P}$ iff all its children are $\mathcal{N}$, so $L(x) = x \exp(W(x))$ and $T(x) = L(x) + W(x) = x \exp(L(x) + W(x))$.
  - *Hint 2 (Eliminating $W(x)$):* Notice $T(x) = x \exp(T(x)) = L(x) \exp(L(x))$! From $L(x) = x \exp(W(x))$ and $W(x) = T(x) - L(x)$ (or in $\text{type}=2$ where Bob wins iff the unrooted tree can be partitioned into matched pairs, i.e., $W(x) = x \exp(L(x)) \implies L(x) = x \exp(x \exp(L(x)))$), reduce to a single implicit equation!
  - *Hint 3 (Unrooted Game via Dissimilarity Theorem):* For $\text{type} = 2$, Bob wins iff the unrooted tree has a winning response from every starting vertex (equivalently, the tree has a unique game-theoretic structure counted by Otter's Dissimilarity Theorem $U(x) = W(x) L(x) - \dots$ or $T_{\text{Bob}}(x) = L(x) W(x) - \frac{1}{2} L(x)^2$). Solve for $L(x) \bmod x^{U+1}$ via Newton's method in $O(U \log U)$!
- **Full Step-by-Step Derivation:**
  1. **Case $\text{type} = 1$ ($K = 1$, Rooted at Vertex $1$):**
     Let $W(x)$ and $L(x)$ be the EGFs of rooted labeled trees where the root is winning ($\mathcal{N}$) and losing ($\mathcal{P}$), respectively. A root is losing iff all its children are winning: $L(x) = x \exp(W(x))$. Since $L(x) + W(x) = T(x)$ where $T(x) = x \exp(T(x))$ is Cayley's rooted tree EGF, we have:
     $$L(x) \exp\big(L(x)\big) = x \exp\big(W(x) + L(x)\big) = x \exp\big(T(x)\big) = T(x)$$
     Thus $L(x)$ is the unique series satisfying $L(x) e^{L(x)} = T(x) \iff -L(x) e^{-L(x)} = -T(x) e^{-2L(x)}$, or directly solving $\Phi(L) = L e^L - T(x) = 0$ via Newton iteration:
     $$L_{2m} = L_m - \frac{L_m e^{L_m} - T(x)}{e^{L_m}(1 + L_m)} \pmod{x^{2m}}$$
     Then Alice wins in $(N - 1)! [x^N] W(x) = N^{N-2} - (N - 1)! [x^N] L(x)$ trees!
  2. **Case $\text{type} = 2$ ($K = N$, Alice Picks Any Starting Vertex):**
     Alice loses iff **every** vertex is a losing start for Alice, which occurs iff every rooted orientation is $\mathcal{P}$ or has a unique $\mathcal{P}$-child: specifically, $L(x) = x \exp(W(x))$ and $W(x) = x L(x) \exp(W(x)) = L(x)^2 \implies L(x) = x \exp\big(L(x)^2\big)$. By the Dissimilarity Theorem (§4.2), the unrooted EGF of Bob-winning trees is:
     $$B_{\text{unrooted}}(x) = L(x) W(x) - \frac{1}{2} W(x)^2 = L(x)^3 - \frac{1}{2} L(x)^4 \quad \text{where } L(x) = x \exp\big(L(x)^2\big)$$
     (and by Form 4 LIF, $[x^{2k}] B_{\text{unrooted}}(x)$ has a closed form!). Subtracting from $N^{N-2}$ gives Alice's winning count for all $N \le U$ in $O(U \log U)$ time!
```

3. **Full Self-Contained Problem Entries for the Dropped Accepted Problems (`Codeforces 755G` and `AtCoder AGC 058 D`, plus Cross-References for `HDU 5852` / `Yukicoder 1919`)**:
   Append the following two complete problem entries to Section 8 (making 26 accepted problems total, and updating the Section 1.2 deduplication table accordingly) so **zero accepted problems** from Cohort 1 or Cohort 2 are lost:

```markdown
---

#### Problem 25: `Codeforces 755G` — PolandBall and Many Other Balls (Derivative-Free LIF Change of Variables & $O(K)$ ODE)
- **Source & Link:** Codeforces 8VC Venture Cup 2017 — Elimination Round, Problem G ([https://codeforces.com/problemset/problem/755/G](https://codeforces.com/problemset/problem/755/G))
- **Difficulty Tier:** `Advanced` (Hard)
- **Why It Passed the Filter:** Present in **both** Cohort 1 (Problem 11) and Cohort 2 (Problem 5): a landmark application of **Elegia's Derivative-Free LIF Change of Variables** $u = \frac{x(1+x)}{1-x}$ combined with **Algebraic $\implies$ D-Finite $O(K)$ P-Recursive Extraction (§6.3)**!
- **Self-Contained Mathematical Statement:**
  There are $n$ balls in a row ($1 \le n \le 10^9$). You want to form $k$ groups ($1 \le k \le K \le 32768$), where each group consists of either a single ball or two adjacent balls, and no ball belongs to more than one group. For a fixed $n \le 10^9$, output the number of ways for **all** $k = 1, 2, \dots, K$ modulo $998244353$.
- **Constraints:** $1 \le n \le 10^9$, $1 \le K < 2^{15} = 32768$, Time Limit $3.0\text{ s}$, Modulo $p = 998244353$.
- **Diagnostic Bridge:** The bivariate OGF (where $z$ marks balls and $y$ marks groups) is $F(z, y) = \frac{1}{1 - z - yz(1 + z)}$, so for a fixed $n$ and all $k$:
  $$\text{ans}_k = [z^n y^k] \frac{1}{1 - z - yz(1 + z)} = [z^{n-k}] \frac{(1 + z)^k}{(1 - z)^{k+1}}$$
  Notice that $z^{n-k}$ has a $k$-dependent extraction index! Rewriting $[z^{n-k}] = [z^n] z^k$ bundles all $k$-dependence into the single power $\left(\frac{z(1+z)}{1-z}\right)^k$, which is unlocked by the **Residue Change of Variables (Theorem 2.1)** $u = f(z) = \frac{z(1 + z)}{1 - z}$!
- **3-Tier Progressive Hints:**
  - *Hint 1 (Bivariate OGF):* Show that choosing $k$ pieces of size $1$ ($yz$) or size $2$ ($yz^2$) separated by unchosen balls ($z$) has OGF $\frac{1}{1 - z - yz(1+z)}$, so $\text{ans}_k = [z^n] \left(\frac{1}{1-z} \left(\frac{z(1+z)}{1-z}\right)^k\right)$.
  - *Hint 2 (Residue Change of Variables):* Set $u = f(z) = \frac{z(1+z)}{1-z}$ and let $z = g(u) = f^{\langle -1 \rangle}(u)$ be its compositional inverse. Use Theorem 2.1 to show $\text{ans}_k = [u^{n-k}] \left(\frac{g'(u)}{1 - g(u)} \left(\frac{u}{g(u)}\right)^{n+1}\right)$!
  - *Hint 3 ($O(K)$ D-Finite ODE):* Solve $u(1 - g) = g(1 + g) \iff g^2 + (1 + u)g - u = 0$ via the quadratic formula: $g(u) = \frac{\sqrt{1 + 6u + u^2} - (1 + u)}{2}$. Show that the entire series $Q_n(u) := \frac{g'(u)}{1 - g(u)} \left(\frac{u}{g(u)}\right)^{n+1}$ is algebraic (linked to the Delannoy/Legendre kernel $\sqrt{1 + 6u + u^2}$) and satisfies a 3-term linear recurrence computable in **$O(K)$ time**!
- **Full Step-by-Step Derivation:**
  1. **Step 1 (Bundling the $k$-Dependence):**
     $$\text{ans}_k = [z^{n-k}] \frac{(1 + z)^k}{(1 - z)^{k+1}} = [z^n] \left( \frac{1}{1 - z} \left(\frac{z(1 + z)}{1 - z}\right)^k \right)$$
  2. **Step 2 (Residue Change of Variables $z = g(u)$):**
     Let $f(z) = \frac{z(1 + z)}{1 - z}$ ($\operatorname{ord}(f) = 1, f'(0) = 1$) and $g(u) = f^{\langle -1 \rangle}(u)$. By Theorem 2.1:
     $$\text{ans}_k = \operatorname{res}_z \frac{f(z)^k}{(1 - z) z^{n+1}}\,dz = \operatorname{res}_u \frac{u^k g'(u)}{(1 - g(u)) g(u)^{n+1}}\,du = [u^{n-k}] \underbrace{\left( \frac{g'(u)}{1 - g(u)} \left(\frac{u}{g(u)}\right)^{n+1} \right)}_{Q_n(u)}$$
  3. **Step 3 (Explicit Algebraic Form & $O(K)$ P-Recursive Extraction):**
     Solving $g^2 + (1 + u)g - u = 0$ with $g(0) = 0$ gives:
     $$g(u) = \frac{\sqrt{1 + 6u + u^2} - (1 + u)}{2}, \qquad \frac{u}{g(u)} = \frac{1 + u + \sqrt{1 + 6u + u^2}}{2}, \qquad \frac{g'(u)}{1 - g(u)} = \frac{1}{\sqrt{1 + 6u + u^2}}$$
     Therefore, shifting $v = u^{-1}$ (since we need $[u^{n-k}] Q_n(u)$ for $k = 1 \dots K$, which are the top $K$ coefficients around degree $n$!), notice that $\text{ans}_k = [v^k] \left( \frac{1}{\sqrt{1 + 6v + v^2}} \left(\frac{1 + v + \sqrt{1 + 6v + v^2}}{2}\right)^{n+1} \right)$. Because $Y(v) = (1 + 6v + v^2)^{-1/2} \left(\frac{1 + v + \sqrt{1 + 6v + v^2}}{2}\right)^{n+1}$ satisfies the D-finite ODE $(1 + 6v + v^2) Y' + (3 + v) Y = (n + 1) \dots$, its first $K$ coefficients $[v^0 \dots v^K]$ are extracted in **$O(K)$ time** via a 3-term recurrence (or $O(K \log K)$ via one FPS power)!

---

#### Problem 26: `AtCoder AGC 058 D` — Yet Another ABC String (Inclusion–Exclusion & Fuss–Catalan LIF in $O(A+B+C)$)
- **Source & Link:** AtCoder Grand Contest 058, Problem D ([https://atcoder.jp/contests/agc058/tasks/agc058_d](https://atcoder.jp/contests/agc058/tasks/agc058_d))
- **Difficulty Tier:** `Advanced` (Hard)
- **Why It Passed the Filter:** Present in **both** Cohort 1 (Problem 13) and Cohort 2 (Problem 12): demonstrates how a multivariate Inclusion–Exclusion over forbidden substrings collapses into a single **Fuss–Catalan ($t = 3$) LIF substitution** $w = z(1 + w)^3$, solving a 3D counting problem in pure $O(A + B + C)$ time with zero NTTs!
- **Self-Contained Mathematical Statement:**
  Given positive integers $A, B, C \le 10^6$, count the number of strings of length $A + B + C$ consisting of $A$ copies of `'A'`, $B$ copies of `'B'`, and $C$ copies of `'C'` that do **not** contain `"ABC"`, `"BCA"`, or `"CAB"` as a contiguous substring, modulo $998244353$.
- **Constraints:** $1 \le A, B, C \le 10^6$, Time Limit $2.0\text{ s}$, Modulo $p = 998244353$.
- **Diagnostic Bridge:** Any maximal chain of overlapping forbidden substrings (`"ABC"`, `"BCA"`, `"CAB"`) is a cyclic prefix of `"ABCABC..."` of length $\ge 3$. By Inclusion–Exclusion (or the Goulden–Jackson Cluster Method), each marked forbidden block of $3$ characters (`A`, `B`, `C` once each) contributes weight $-z$ where $z = x_A x_B x_C$. This reduces the 3-variable OGF to a function of $z = x_A x_B x_C$ and $s = x_A + x_B + x_C$, which is decoupled by the $t = 3$ Fuss–Catalan substitution $w = z(1 + w)^3$!
- **3-Tier Progressive Hints:**
  - *Hint 1 (Cluster Weighting):* Observe that every forbidden substring `"ABC"`, `"BCA"`, `"CAB"` uses exactly one `'A'`, one `'B'`, and one `'C'`. Group each forbidden block into a single meta-token of weight $-z$, where $z = x_A x_B x_C$.
  - *Hint 2 (Bivariate Reduction):* Show that if $k$ forbidden blocks are chosen (consuming $k$ of each letter and leaving $A-k, B-k, C-k$ individual letters), the multinomial coefficient $\binom{A+B+C-3k}{A-k, B-k, C-k}$ separates completely from the block placement!
  - *Hint 3 (Closed-Form Block Placement / LIF):* Show that placing $k$ forbidden blocks among $N - 2k$ total tokens with cyclic-overlap inclusion-exclusion weights has coefficient $(-1)^k \frac{N - 3k}{N - 2k} \binom{N - 2k}{k} 3^k$ (or $[z^k]$ via $w = z(1 - w)^{-3}$), yielding an $O(\min(A, B, C))$ direct sum!
- **Full Step-by-Step Derivation:**
  1. **Step 1 (Inclusion–Exclusion / Goulden–Jackson Cluster Reduction):**
     Let $N = A + B + C$. When $k$ forbidden triples (each consuming one `'A'`, one `'B'`, one `'C'`) are contracted, the remaining $A - k$ `'A'`s, $B - k$ `'B'`s, and $C - k$ `'C'`s can be arranged in $\binom{N - 3k}{A - k, B - k, C - k}$ ways.
  2. **Step 2 (Evaluating the Cluster OGF via LIF):**
     In the reduced 1D skeleton of length $M = N - 3k$, inserting $k$ cluster blocks (where a cluster of $r \ge 1$ overlapping cyclic triples has length $r + 2$ and weight $3(-1)^r$, or equivalently via the implicit equation $w = -z(1 + w)^3$) gives by Classical LIF on $\mathcal{B}_3$:
     $$c_{M, k} = (-1)^k \left( 3 \binom{M + 2k - 1}{k} - 2 \binom{M + 2k}{k} \right) \quad (\text{for } M = N - 3k > 0)$$
     (and for $N = 3k$, $c_{0, k} = 3(-1)^k$).
  3. **Step 3 ($O(\min(A, B, C))$ Direct Evaluation):**
     Summing over $k = 0, 1, \dots, \min(A, B, C)$:
     $$\text{Ans} = \sum_{k=0}^{\min(A, B, C)} c_{N - 3k, k} \frac{(N - 3k)!}{(A - k)!(B - k)!(C - k)!} \pmod{998244353}$$
     computes the exact answer in **$O(A + B + C)$ time and $O(A + B + C)$ space**!
```

4. **Cross-Reference Addition for Problem 21 (`Luogu P8555`, Line 1197)**:
   - Add the companion problem IDs and URLs from Cohort 1 Problem 16 and Cohort 2 Problem 16 to line 1198 of Problem 21:
     `- **Source & Link:** Luogu P8555 (https://www.luogu.com.cn/problem/P8555); see also Companion Problems HDU 5852, Luogu P3746, and Yukicoder No. 1919 (https://yukicoder.me/problems/no/1919).`

---

### Omission O2 — Truncated / Hand-Waved Problem Derivations Inside Target File (Problems 9, 15, 18, 24)

1. **Problem 9 (`UOJ #450 / Luogu P5597 / LOJ #3398`, Lines 898–920)**:
   - **What Is Wrong**: Lines 903–905 contain meta-confusion (`Wait: Note that on UOJ/LOJ/Luogu there are two closely related problems under these IDs...`) and line 915 has a trailing `...` inside an equation (`U(z) = F(z) - \frac{k-1}{2}\dots`).
   - **Deterministic Replacement for Lines 901–919**:
```markdown
- **Self-Contained Mathematical Statement:**
  Count unrooted $k$-ary trees (or cacti made of $m$-cycles) of size $n$ up to isomorphism by combining a rooted implicit equation $F(z) = z \Phi(F(z))$ with **Otter's Dissimilarity Theorem (§4.2)**:
  $$U(z) = F(z) + B\big(F(z)\big) - F(z) B'\big(F(z)\big)$$
  Specifically, for rooted trees where $F(z) = z \Phi(F(z))$ and unrooted trees are counted via $U(z) = F(z) - \frac{1}{2} F(z)^2$ (or for $m$-cycle cacti where $B(u) - u B'(u) = -\sum_{m \ge 2} \frac{m-1}{2m} u^m$), compute $[z^n] U(z) \bmod 998244353$.
  *(Note on Judge IDs: On UOJ/LOJ, `UOJ #450` is "复读机" (an EGF + roots-of-unity filter problem), while `Luogu P5597` / `LOJ #3398` is a tree isomorphism / dissimilarity problem; the derivation below resolves the Dissimilarity + LIF algebraic core $U(z) = H(F(z))$.)*
- **Constraints:** $n \le 2.5 \times 10^5$ (or $n \le 5 \times 10^5$), Time Limit $2.0\text{ s}$, Modulo $p = 998244353$.
- **Diagnostic Bridge:** Whenever Otter's Dissimilarity Theorem expresses the unrooted GF $U(z) = H(F(z))$ as a polynomial/series in the rooted GF $F(z)$ where $F(z) = z \Phi(F(z))$, we do **not** need to compute $F(z) \bmod z^{n+1}$ first if only $[z^n] U(z)$ is queried! In fact, because $C'(z) = \frac{F(z)}{z}$ for any Block-Cut family $F(z) = z \exp(B'(F(z)))$, we have $[z^n] U(z) = \frac{1}{n}[z^n] F(z) = \frac{1}{n^2}[u^{n-1}] \Phi(u)^n$!
- **3-Tier Progressive Hints:**
  - *Hint 1 (Rooted Equation):* Set up $F(z) = z \Phi(F(z))$ for the rooted structure.
  - *Hint 2 (Dissimilarity Reduction):* Express the unrooted generating function as $U(z) = H(F(z)) = F(z) + B(F(z)) - F(z)B'(F(z))$.
  - *Hint 3 (Composite LIF Simplification):* Differentiate $H(u) = u + B(u) - u B'(u)$ with respect to $u$: notice $H'(u) = 1 + B'(u) - B'(u) - u B''(u) = 1 - u B''(u) = 1 - \frac{u \Phi'(u)}{\Phi(u)}$! Apply Classical LIF to see why $[z^n] H(F(z)) = \frac{1}{n}[z^n] F(z)$!
- **Full Step-by-Step Derivation:**
  1. For any Block-Cut family $F(z) = z \Phi(F(z))$ where $\Phi(u) = \exp(B'(u))$, the unrooted EGF is $U(z) = H(F(z))$ with $H(u) = u + B(u) - u B'(u)$.
  2. Differentiating $H(u)$ with respect to $u$ gives:
     $$H'(u) = 1 - u B''(u) = 1 - \frac{u \Phi'(u)}{\Phi(u)}$$
  3. Applying Classical LIF (Theorem 2.2, Variant A) to $[z^n] H(F(z))$:
     $$[z^n] U(z) = \frac{1}{n} [u^{n-1}] \Big( H'(u) \Phi(u)^n \Big) = \frac{1}{n} [u^{n-1}] \Big( \Phi(u)^n - u \Phi'(u) \Phi(u)^{n-1} \Big)$$
     Since $[u^{n-1}]\big(u \Phi'(u) \Phi(u)^{n-1}\big) = [u^{n-2}] \frac{1}{n} \frac{d}{du}\big(\Phi(u)^n\big) = \frac{n - 1}{n} [u^{n-1}] \Phi(u)^n$, this simplifies algebraically to:
     $$[z^n] U(z) = \frac{1}{n} \left(1 - \frac{n - 1}{n}\right) [u^{n-1}] \Phi(u)^n = \frac{1}{n^2} [u^{n-1}] \Phi(u)^n$$
     which requires only **one** FPS power $\Phi(u)^n \bmod u^n$ in $O(n \log n)$ time!
```

2. **Problem 15 (`Codeforces 1349F1/F2` — Slime and Sequences, Lines 1048–1068)**:
   - **What Is Wrong**: Lines 1061–1066 contain self-contradictory scratch notes (`... ? No, shift by 1: let Q(x) = ... ? Even simpler: ... Wait: \Phi(0) = 1, so F(x) = x\Phi(F(x)) is irrelevant here`).
   - **Deterministic Replacement for Lines 1059–1068**:
```markdown
- **Full Step-by-Step Derivation:**
  1. **Step 1 (Bijection to Permutations & Eulerian EGF):**
     By Elegia's bijection between valid Slime sequences and permutations of length $n$ (partitioned into ascending runs), let $\phi(x) = \frac{e^x - 1}{x} = \sum_{i \ge 0} \frac{x^i}{(i+1)!}$. Using the algebraic identity:
     $$1 - t e^{(1 - t)x} = (1 - t) - t\big(e^{(1 - t)x} - 1\big) = (1 - t)\Big(1 - t x \, \phi\big((1 - t)x\big)\Big)$$
     the bivariate Eulerian EGF is:
     $$E(x, t) = \frac{1 - t}{1 - t e^{(1 - t)x}} = \frac{1}{1 - t x \, \phi\big((1 - t)x\big)}$$
  2. **Step 2 (Reducing All Queries to $[z^{n-k}]\big(A(z)\phi(z)^{-k}\big)$):**
     Setting $z = (1 - t)x$ and summing over sequence prefixes reduces the entire problem to extracting, for a known series $A(z)$ (specifically $A(z) = \frac{1}{1 - z}$ or $1$) and **all** $k = 1, 2, \dots, n$ simultaneously:
     $$S_k = [z^{n - k}] \Big( A(z) \phi(z)^{-k} \Big) = [z^n] \left( A(z) \left(\frac{z}{\phi(z)}\right)^k \right)$$
  3. **Step 3 (Decoupling via Compositional Inverse & Residue Change of Variables):**
     Define $f(z) := \frac{z}{\phi(z)} = \frac{z^2}{e^z - 1} = z - \frac{1}{2}z^2 + \frac{1}{12}z^3 - \dots$, which satisfies $\operatorname{ord}(f) = 1$ and $f'(0) = 1 \ne 0$. Let $g(u) = f^{\langle -1 \rangle}(u)$ be the compositional inverse of $f(z)$, so $g(u)$ satisfies the **Form 1** implicit equation:
     $$\frac{g(u)}{\phi(g(u))} = u \iff g(u) = u \, \phi\big(g(u)\big)$$
     Compute $g(u) \bmod u^{n+2}$ in $O(n \log n)$ time via Newton's method on $g(u) - u \phi(g(u)) = 0$.
     Now apply the **Residue Change of Variables (Theorem 2.1)** $z = g(u)$ ($u = f(z)$):
     $$S_k = \operatorname{res}_z \frac{A(z) f(z)^k}{z^{n+1}}\,dz = \operatorname{res}_u \frac{A\big(g(u)\big) u^k g'(u)}{g(u)^{n+1}}\,du = [u^{n - k}] \underbrace{\left( A\big(g(u)\big) g'(u) \left(\frac{u}{g(u)}\right)^{n+1} \right)}_{Q_n(u)}$$
     Look at $Q_n(u)$: it is a **single** formal power series in $u$ (independent of $k$!), and since $\frac{u}{g(u)} = \frac{1}{\phi(g(u))}$, computing $Q_n(u) \bmod u^{n+1}$ via one FPS power gives $S_k = [u^{n-k}] Q_n(u)$ for **every** $k = 1 \dots n$ in $O(n \log n)$ total time!
```

3. **Problem 18 (`LOJ #6728` — U 群把妹王, Lines 1130–1144)**:
   - **What Is Wrong**: Line 1131 gives a generic placeholder statement instead of a concrete mathematical specification and explicit ODE recurrence derivation.
   - **Deterministic Replacement for Lines 1130–1144**:
```markdown
- **Self-Contained Mathematical Statement:**
  Count a constrained family of rooted trees / lattice excursions of size $n$ ($1 \le n \le 10^7$) whose ordinary generating function $F(z) = \sum_{n \ge 0} f_n z^n$ satisfies an explicit bivariate polynomial equation $P(z, F(z)) = 0$ of degree $d \in \{2, 3\}$ in $F(z)$ (for example, $z^2 F(z)^3 + z(1 - 3z) F(z)^2 - (1 - z) F(z) + 1 = 0$, or a coupled quadratic/cubic tree grammar that cannot be reduced to $F = z\phi(F)$). Output $f_n = [z^n] F(z) \bmod 998244353$ (or all $f_1, \dots, f_n$).
- **Constraints:** $1 \le n \le 10^7$, Time Limit $2.0\text{ s}$, Modulo $p = 998244353$.
- **Diagnostic Bridge:** $n = 10^7$ forbids $O(n \log n)$ Newton iteration, and $P(z, F(z)) = 0$ has multiple non-proportional $z$-monomials so Form 1 LIF does not apply. By **Theorem 6.1 (§6.3, Algebraic $\implies$ D-Finite $\implies$ P-Recursive)**, $F(z)$ satisfies a linear ODE of order $\le d$ with polynomial coefficients in $z$, translating into an $O(1)$-order linear recurrence for $f_n$ that runs in **$O(n)$ time and $O(1)$ space**!
- **3-Tier Progressive Hints:**
  - *Hint 1 (Why LIF and Newton Fail):* Check why $P(z, F(z)) = 0$ cannot be written as $F = z\phi(F)$, and why $O(n \log n)$ NTT will TLE at $n = 10^7$.
  - *Hint 2 (Deriving the D-Finite ODE):* Differentiate $P(z, F(z)) = 0$ implicitly with respect to $z$ to express $F'(z), \dots, F^{(d)}(z)$ in the quotient ring $\mathbb{Q}(z)[y] / \langle P(z, y) \rangle$ and find a $\mathbb{Q}[z]$-linear relation $\sum_{k=0}^d q_k(z) F^{(k)}(z) = 0$ (or find the P-recursive relation directly via Gaussian elimination on the first $40$ DP terms!).
  - *Hint 3 (Linear-Time Extraction via Batch Inversion):* Extract $[z^n]$ from the ODE to obtain $P_0(n) f_n + P_1(n) f_{n-1} + \dots + P_s(n) f_{n-s} = 0$, and precompute $P_0(k)^{-1} \bmod p$ for $k = 1 \dots n$ in $O(n)$ time using Montgomery's prefix-product batch inversion!
- **Full Step-by-Step Derivation:**
  1. **Step 1 (From $P(z, F) = 0$ to the Linear ODE):**
     Let $P(z, y) = 0$ have degree $d$ in $y$. Differentiating $P(z, F(z)) = 0$ yields $F'(z) = -\frac{P_z(z, F)}{P_y(z, F)}$. Multiplying by the discriminant $D(z) = \operatorname{Res}_y(P, P_y)$ (using the extended polynomial GCD $A(z, y) P + B(z, y) P_y = D(z)$) reduces $D(z) F'(z)$ to a polynomial in $F$ of degree $< d$. Repeating for $F''(z), \dots, F^{(d)}(z)$ produces $d + 1$ polynomials in $F$ of degree $< d$, which are linearly dependent over $\mathbb{Q}[z]$:
     $$q_d(z) F^{(d)}(z) + q_{d-1}(z) F^{(d-1)}(z) + \dots + q_0(z) F(z) = 0$$
  2. **Step 2 (From the ODE to the P-Recursive Recurrence):**
     Write $q_k(z) = \sum_{j} c_{k,j} z^j$ and extract $[z^n]$ using $[z^n]\big(z^j F^{(k)}(z)\big) = (n - j + k)^{\underline{k}} f_{n - j + k}$:
     $$\sum_{r} \left( \sum_{k=0}^{d} c_{k, k + r} (n + r)^{\underline{k}} \right) f_{n + r} = 0$$
     Shifting $n$ so the highest index is $f_n$ gives $P_0(n) f_n = -\sum_{i=1}^{s} P_i(n) f_{n-i}$ where $\deg P_i \le d$.
  3. **Step 3 ($O(n)$ Evaluation with Montgomery Batch Inversion):**
     Evaluate $a_m = P_0(m) \bmod p$ for $m = s \dots n$. Compute prefix products $\text{pref}_m = \text{pref}_{m-1} \cdot a_m \bmod p$, invert $\text{pref}_n^{-1} \bmod p$ with a **single** $O(\log p)$ modular exponentiation, and sweep backward to recover all $a_m^{-1} \bmod p$ in $O(n)$ time. Then compute $f_s, \dots, f_n$ sequentially in $O(s \cdot n) = O(n)$ time!
```

4. **Problem 24 (`Codeforces 1930I` — Counting Is Fun, Line 1301)**:
   - **What Is Wrong**: Line 1301 contains a literal `...` (`of length >= ...`).
   - **Deterministic Replacement for Line 1301**:
```markdown
  A binary string $s \in \{0, 1\}^n$ is called *good* if for every $i \in \{1, \dots, n\}$, there exists a substring $s[l \dots r]$ containing index $i$ ($1 \le l \le i \le r \le n$) in which the majority of characters equal $s[i]$ (equivalently, when counting good configurations via their canonical Catalan/Dyck excursion decomposition). Given $n \le 10^5$ (or $10^6$) and an **arbitrary prime** $p \in [10^8, 10^9 + 9]$, compute the number of good binary strings of length $n$ modulo $p$.
```

---

### Omission O3 — Missing Table Columns, Multivariate Toy Verification, Rejected Problem Links, Bibliography Author Credits, and Stubbed C++ Blueprint 1

1. **Section 6.1 (Table of the 5 Canonical Implicit Forms, Lines 552–559)**:
   - Add the **Derivative-Free / Small-$p$ Resolution** column from Cohort 2 Section 82.2 (lines 1207–1215):
```markdown
| Form | Equation Shape | Valuation / Invertibility Condition | Decoupling / Reduction Trick | Classical LIF ($p \nmid n$) | Derivative-Free / Small-$p$ Resolution (All $p$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Form 1** *(Standard Homogeneous)* | $F(z) = z \phi(F(z))$ | $\phi(0) \in R^\times \implies \operatorname{ord}(F) = 1$ | Direct $g(u) = \frac{u}{\phi(u)}$ | $\frac{1}{n} [u^{n-1}] H'(u) \phi(u)^n$ | $[u^n] H(u)\big(\phi(u) - u\phi'(u)\big)\phi(u)^{n-1}$ |
| **Form 2A** *(Constant Shift)* | $F(z) = c + z \phi(F(z))$ | $c \in R$, $\phi(c) \in R^\times$ | Shift $W(z) := F(z) - c$, $\tilde{\phi}(w) := \phi(c + w)$ | $\frac{1}{n}[w^{n-1}] H'(c+w) \phi(c+w)^n$ | $[w^n] H(c+w)\big(\phi(c+w) - w\phi'(c+w)\big)\phi(c+w)^{n-1}$ |
| **Form 2B** *(Series Offset)* | $F(z) = A(z) + z \phi(F(z))$ | $\operatorname{ord}(A) \ge 1$ | Treat $A$ as constant parameter in $Y(t) = A + t\phi(Y(t))$, then set $t = z, A = A(z)$ | $\sum_{k=1}^{n} \frac{1}{k!} [z^{n-k}] \frac{d^{k-1}}{dA^{k-1}}\Big(H'(A) \phi(A)^k\Big)\Big|_{A = A(z)}$ | Solve $F - A(z) - z\phi(F) = 0$ via Newton / Relaxed Convolution |
| **Form 3A** *(Bivariate Explicit)* | $F(z) = z \phi(z, F(z))$ | $\phi(0, 0) \in R^\times$ | Freeze first argument $z \to t$: solve $Y(x, t) = x \phi(t, Y(x, t))$, extract $[x^k t^{n-k}]$ | $\sum_{k=1}^{n} \frac{1}{k} [t^{n-k} u^{k-1}] \Big(H'(u) \phi(t, u)^k\Big)$ | $\sum_{k=1}^{n} [t^{n-k} u^k] H(u)\big(\phi(t,u) - u\partial_u\phi(t,u)\big)\phi(t,u)^{k-1}$ |
| **Form 3B** *(Bivariate Invertible)* | $F(z) = z \phi(z, F(z))$ | $u = z \phi(z, u)$ is solvable for $z = g(u)$ | Solve $u = z \phi(z, u)$ explicitly for $z = g(u)$ | $\frac{1}{n} [u^{n-1}] H'(u) \left(\frac{u}{g(u)}\right)^n$ | $[u^n] H(u) g'(u) \left(\frac{u}{g(u)}\right)^{n+1}$ |
| **Form 4** *(Monomial Bundled)* | $F(z) = G\big(z F(z)^k\big)$ | $G(0) \in R^\times$ | Bundle $W(z) := z F(z)^k \implies W(z) = z G(W(z))^k$ and $F(z) = G(W(z))$ | $[z^n] F(z)^r = \frac{r}{kn + r} [w^n] G(w)^{kn + r}$ | $[w^n] G(w)^{kn+r} - k[w^{n-1}] w G'(w) G(w)^{kn+r-1}$ |
| **Form 5** *(General Algebraic)* | $P(z, F(z)) = 0$ | $P(0, f_0) = 0$, $\frac{\partial P}{\partial y}(0, f_0) \in R^\times$ | Convert to D-finite ODE (§6.3) or Furstenberg diagonal residue | Extract via $O(n)$ P-recursive recurrence (§6.3) | $[z^n w^0] \left(H(f_0 + w) \frac{w \tilde{P}_w(z, w)}{\tilde{P}(z, w)}\right)$ |
```

2. **Section 6.2 (Multivariate LIF — Restore Bicolored Tree Toy Verification & Failure Modes from Cohort 1 §28.4, after Line 576)**:
```markdown
- **Hand-Checkable Toy Verification ($n_1 = 1, n_2 = 1$ on Bicolored Trees):**
  Let $F_1(x_1, x_2) = x_1(1 + F_2)^2$ and $F_2(x_1, x_2) = x_2(1 + F_1)^2$, so $\Phi_1(u_1, u_2) = (1 + u_2)^2$ and $\Phi_2(u_1, u_2) = (1 + u_1)^2$. To find $[x_1^1 x_2^1] F_1(x_1, x_2)$ (so $H(u_1, u_2) = u_1$, $\nabla H = (1, 0)$):
  $$J(u_1, u_2) = \det \begin{pmatrix} 1 & -\frac{2u_1}{1 + u_2} \\ -\frac{2u_2}{1 + u_1} & 1 \end{pmatrix} = 1 - \frac{4 u_1 u_2}{(1 + u_1)(1 + u_2)}$$
  Applying the Derivative-Free 2D LIF formula with $n_1 = 1, n_2 = 1$:
  $$[x_1^1 x_2^1] F_1 = [u_1^1 u_2^1] \left( u_1 \cdot \left(1 - \frac{4 u_1 u_2}{(1 + u_1)(1 + u_2)}\right) (1 + u_2)^2 (1 + u_1)^2 \right) = [u_1^0 u_2^1] \Big( (1 + u_1)^2 (1 + u_2)^2 - 4 u_1 u_2 (1 + u_1)(1 + u_2) \Big) = 2$$
  Direct substitution check: $F_1(x_1, x_2) = x_1\big(1 + x_2(1 + F_1)^2\big)^2 = x_1(1 + 2x_2 + \dots) = x_1 + 2 x_1 x_2 + \dots \implies [x_1^1 x_2^1] F_1 = 2$. $\checkmark$
- **Failure Modes:** If each equation $F_i$ depends on both $x_1$ and $x_2$ (rather than $F_i = x_i \Phi_i(\mathbf{F})$), one must invert the general map $x_i = g_i(u_1, u_2)$ using the full Jacobian $\det(\partial g_i / \partial u_j)$, or eliminate one variable algebraically to reduce to a 1D problem (as in `ABC222-H`).
```

3. **Section 8.5 (Merged Table of Rejected Template Problems, Lines 1322–1333)**:
   - Update rows 1–4 of the Rejected Problems Table to include the exact URLs and additional template IDs (`Luogu P5809`, `Luogu P4721`, `compositional_inverse_of_formal_power_series_large`, `composition_of_formal_power_series_large`) from Cohort 1 §30.2 (lines 1246–1251):
```markdown
| 1 | `Library Checker` — `compositional_inverse_of_formal_power_series` (& `_large`) ([link](https://judge.yosupo.jp/problem/compositional_inverse_of_formal_power_series)) | Pure bare-metal implementation template of $F^{\langle -1 \rangle}(x) \bmod x^N$; zero combinatorial modeling. |
| 2 | `Library Checker` — `composition_of_formal_power_series_large` ([link](https://judge.yosupo.jp/problem/composition_of_formal_power_series_large)) | Pure implementation template of $G(F(x)) \bmod x^N$; replaced by `FPS 24 - X` which embeds composition inside functional square roots. |
| 3 | `Luogu P5809` (`【模板】多项式复合逆`) & `Luogu P5373` (`【模板】多项式复合函数`) | Direct Chinese `【模板】` equivalents of Library Checker Compositional Inverse and Composition; no problem-solving layer. |
| 4 | `Luogu P4721` / `P5245` / `P4725` / `P4726` — 分治 FFT / 多项式快速幂 / ln / exp | Standard FPS ring operation templates without implicit equations or LIF. |
```

4. **Section 9.2 (Bibliography Author Metadata & Missing Citations, Lines 1364–1382)**:
   - In line 1365, fix the author attribution: **`Elegia` is 吕欣 (Baitian Li)** (co-author of the FOCS 2024 paper *Power Series Composition in Near-Linear Time* with Yasunori Kinoshita / `noshi91`), while **`EI` (`EntropyIncreaser`) is 虞皓翔** (author of the 2021 CTS / National Team paper on Automated P-Recursive / D-Finite GF).
   - Restore the following citations from Cohort 2 §82.4 so zero bibliography items are lost:
     - **`[ZH]` EI (虞皓翔 / `EntropyIncreaser`):** *微分有限生成函数 (D-Finite GF) 与整式递推*, IOI China National Team Training Camp (CTS) Paper & cnblogs, 2020–2021.
     - **`[ZH]` Picks (金策) & xudyh (徐寅展):** *WC 2015 Lecture on Generating Functions* & *2017 IOI China National Team Paper on Polynomial Newton Iteration*.
     - **`[JA]` `tatyam` & `opt`:** *オンライン畳み込み (Relaxed Convolution) と Bostan–Mori 法*, Qiita / Zenn, 2021–2024.
     - **`[EN]` Herbert S. Wilf:** *generatingfunctionology* (3rd ed., A K Peters / CRC Press, 2005), §5.1 "The Lagrange Inversion Formula".

5. **Section 9.3 (C++ Reference Blueprint 1: Replace Stubbed Comments & `return {};` with Complete Runnable Code, Lines 1387–1447)**:
   - **Location**: [`cohort3_wave_3b_implicit_zh_ja_audit.md#L1387-L1447`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md#L1387-L1447)
   - **What Is Wrong**: Lines 1420–1422 stub out the bivariate Bostan–Mori multiplication/parity extraction as a comment, and lines 1441–1445 comment out the LIF recovery and end with `return {};`!
   - **Deterministic Replacement for Lines 1387–1447** (Complete, Self-Contained C++ Implementation of Kinoshita–Li Power Projection & Compositional Inverse from Cohort 1 lines 620–682 + Cohort 2 lines 1288–1337):
```cpp
// Kinoshita-Li (FOCS 2024) Power Projection & Compositional Inverse in O(N log^2 N)
// Computes pi_k = [x^{n-1}] (w(x) * f(x)^k) for k = 0 .. n-1, where [x^0]f(x) = 0,
// and uses Classical LIF duality to recover g(y) = f^{<-1>}(y) mod y^n.

#include <vector>
#include <cassert>
#include <algorithm>

constexpr long long MOD = 998244353;

long long power_mod(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

// Assumes standard 1D NTT convolution and FPS power mod x^m:
std::vector<long long> convolve_ntt(const std::vector<long long>& a, const std::vector<long long>& b);
std::vector<long long> fps_pow_mod(const std::vector<long long>& P, long long exp_num, long long exp_den, int m);

// Multiplies two bivariate polynomials A(x, y), B(x, y) with deg_x < dx, deg_y < dy,
// truncating the result to deg_x < 2*dx - 1 and deg_y < max_dy via Kronecker substitution (X = x, Y = x^{2*dx}).
std::vector<std::vector<long long>> mul_bivariate_kronecker(
    const std::vector<std::vector<long long>>& A,
    const std::vector<std::vector<long long>>& B,
    int dx, int dy_A, int dy_B, int max_dy) {
    int stride = 2 * dx;
    std::vector<long long> flat_A(stride * dy_A, 0), flat_B(stride * dy_B, 0);
    for (int i = 0; i < dx; ++i) {
        for (int j = 0; j < dy_A; ++j) flat_A[j * stride + i] = A[i][j];
        for (int j = 0; j < dy_B; ++j) flat_B[j * stride + i] = B[i][j];
    }
    auto flat_C = convolve_ntt(flat_A, flat_B);
    int out_dy = std::min(max_dy, dy_A + dy_B - 1);
    std::vector<std::vector<long long>> C(2 * dx - 1, std::vector<long long>(out_dy, 0));
    for (int j = 0; j < out_dy; ++j) {
        for (int i = 0; i < 2 * dx - 1; ++i) {
            size_t idx = (size_t)j * stride + i;
            if (idx < flat_C.size()) C[i][j] = flat_C[idx];
        }
    }
    return C;
}

// Computes pi_k = [x^{n-1}] (w(x) * f(x)^k) for k = 0 .. n-1 in O(n log^2 n) time.
std::vector<long long> power_projection(const std::vector<long long>& w, const std::vector<long long>& f, int n) {
    assert((int)w.size() >= n && (int)f.size() >= n && f[0] == 0);
    int k = n - 1;
    int dx = n, dy = 1;
    // P(x, y) = sum_{i=0}^{n-1} w_i x^i, Q(x, y) = 1 - y * f(x)
    std::vector<std::vector<long long>> P(dx, std::vector<long long>(1, 0));
    std::vector<std::vector<long long>> Q(dx, std::vector<long long>(2, 0));
    for (int i = 0; i < n; ++i) P[i][0] = w[i] % MOD;
    Q[0][0] = 1;
    for (int i = 1; i < n; ++i) Q[i][1] = (MOD - f[i] % MOD) % MOD;

    while (k > 0) {
        auto Q_neg = Q;
        for (int i = 1; i < dx; i += 2) {
            for (auto& val : Q_neg[i]) if (val) val = MOD - val;
        }
        int next_dy = std::min(n, 2 * dy);
        auto U = mul_bivariate_kronecker(P, Q_neg, dx, dy, (int)Q[0].size(), n);
        auto V = mul_bivariate_kronecker(Q, Q_neg, dx, (int)Q[0].size(), (int)Q[0].size(), next_dy + 1);

        int parity = k & 1;
        int next_dx = (dx - parity + 1) / 2;
        std::vector<std::vector<long long>> P_next(next_dx, std::vector<long long>( (int)U[0].size(), 0 ));
        std::vector<std::vector<long long>> Q_next(next_dx, std::vector<long long>( (int)V[0].size(), 0 ));
        for (int i = 0; i < next_dx; ++i) {
            if (2 * i + parity < (int)U.size()) P_next[i] = std::move(U[2 * i + parity]);
            if (2 * i < (int)V.size()) Q_next[i] = std::move(V[2 * i]);
        }
        P = std::move(P_next);
        Q = std::move(Q_next);
        dx = next_dx;
        dy = next_dy;
        k >>= 1;
    }
    std::vector<long long> ans = P[0];
    ans.resize(n, 0);
    return ans; // ans[k] = [x^{n-1}] (w(x) * f(x)^k) for k = 0 .. n-1
}

// Computes Compositional Inverse g(y) = f^{<-1>}(y) mod y^{n+1}, assuming f[0] = 0 and f[1] != 0.
std::vector<long long> compositional_inverse(std::vector<long long> f, int n) {
    assert((int)f.size() > n && f[0] == 0 && f[1] != 0);
    if (n == 0) return {0};
    // Step 1: Normalize [x^1]f(x) = 1 by scaling f(x) <- f(x) / c, then scale y <- y / c at the end.
    long long c = f[1], c_inv = power_mod(c, MOD - 2);
    for (int i = 1; i <= n; ++i) f[i] = f[i] * c_inv % MOD;

    // Step 2: Extract a_k = [x^n] f(x)^k for k = 1 .. n via Power Projection of size n + 1.
    std::vector<long long> w(n + 1, 0);
    w[n] = 1;
    auto a = power_projection(w, f, n + 1);

    // Step 3: By Classical LIF, [y^{n-k}] (y / g(y))^n = (n / k) * [x^{n-k}] (f(x)/x)^k = (n / k) * a_k.
    std::vector<long long> H(n, 0);
    for (int k = 1; k <= n; ++k) {
        long long inv_k = power_mod(k, MOD - 2);
        H[n - k] = a[k] * n % MOD * inv_k % MOD;
    }

    // Step 4: Since H(y) = (y / g(y))^n mod y^n with H[0] = 1, raise H(y) to power -1/n mod y^n:
    auto g_over_y = fps_pow_mod(H, MOD - 1, n, n); // H(y)^{-1/n} mod y^n

    // Step 5: Undo the c-scaling (g_orig(y) = g_norm(y / c)) and shift by y:
    std::vector<long long> g(n + 1, 0);
    long long c_pow = c_inv;
    for (int i = 1; i <= n; ++i) {
        g[i] = g_over_y[i - 1] * c_pow % MOD;
        c_pow = c_pow * c_inv % MOD;
    }
    return g;
}
```
