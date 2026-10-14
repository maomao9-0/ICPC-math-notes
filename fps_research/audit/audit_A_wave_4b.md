# Audit Report A — Wave 4B: Furstenberg's Diagonal Method, The Kernel Method & Multivariate Good–Lagrange Inversion

- **Auditor**: Inspector A (Principal Mathematical & Pedagogical Auditor)
- **Target File**: [`cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4b_furstenberg_kernel_good_lagrange.md) (1,782 lines)
- **Source Files Compared**:
  1. **Cohort 1**: [`iter_36_to_40_furstenberg_kernel_good_lagrange.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_36_to_40_furstenberg_kernel_good_lagrange.md) (1,335 lines)
  2. **Cohort 2**: [`cohort2_iter_88_to_92_furstenberg_kernel_good_lagrange.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_88_to_92_furstenberg_kernel_good_lagrange.md) (1,454 lines)

---

## Executive Summary of Audit Findings

| Audit Category | Count | Severity | Summary |
| :--- | :--- | :--- | :--- |
| **1. Critical Mathematical / Formula Bugs** | 7 | **CRITICAL / MAJOR** | (1) Two-Sided Kernel bounded-strip formula on L496 has swapped $(a, b)$ indices and wrong denominator factor $(1 - y_1^2)$ instead of $(y_1 - y_1^{-1})$; (2) Quarter-Plane Worked Example 4.3 (L669) and Problem 29 (L1669) conflate the Tandem Walk excursion count $\frac{2(3m)!}{m!(m+1)!(m+2)!}$ with the Kreweras Walk excursion count $\frac{4^m}{(m+1)(2m+1)}\binom{3m}{m}$; (3) Bipartite Labeled Tree trace table (L762–768) has wrong arithmetic in 9 of 16 cells (e.g., $t_{2,2}=2$ instead of $4$, $t_{3,3}=27$ instead of $81$, $t_{4,4}=65536$ instead of $4096$); (4) Dixon's Identity direct expansion (L815–822) has mismatched exponent bookkeeping; (5) Kinoshita–Li `PowerProjection` $n=4$ trace (L882–899) miscomputes $[x^4] P_0(x,y)Q_0(-x,y)$ as $-4y$ then $-3y$ instead of $+y$ and leaves an inline `"wait — at r=0..."` self-correction; (6) Problem 11 (`AGC 021 E`, L1307) writes $\binom{2R-1}{2R-N}$ instead of $\binom{2R-1}{2R-N+1}$ in the $R=B$ case; (7) Problem 27 (`AGC 058 D`, L1631) factors out $(-2)^k$ instead of $(-2)^{k-1}$ on the second binomial coefficient, giving $6$ instead of $3$ for $(A,B,C)=(1,1,1)$. |
| **2. Combinatorial Statement / Derivation Fixes** | 3 | **MAJOR** | (1) Problem 1 (`ABC 205 E`, L1103–1106) swaps $N$ and $M$ between Hint 1 and the derivation; (2) Problem 5 (`Luogu P6672`, L1182–1186) contains mid-proof hesitation (`"Wait..."`, `"Careful..."`, `"Actually..."`) and a stray Chinese word `虚拟` inside English prose; (3) Problem 12 (`CF 1821F`, L1315–1323) misstates the problem as counting `(positions, directions)` in $[0, n]$ instead of **sets of $m$ tree positions** in $[1, n]$ that admit a valid felling. |
| **3. Omitted Source Content (Cohort 1 & Cohort 2)** | 7 | **MODERATE / MAJOR** | (1) Explicit proof of why $F(z, t/z)$ lives in the formal ring $K((z))[[t]]$ (Cohort 1 §36.1, Cohort 2 §88.1); (2) First-principles proof of the formal residue change-of-variables formula $[u^{-1}] H(u) du = [x^{-1}] H(u(x)) u'(x) dx$ (Cohort 1 §38.2, Cohort 2 §90.2); (3) Characteristic-$p$ pitfall warning ($p \mid n$) for Lagrange Inversion Form 1 vs. Form 2 (Cohort 2 §90.2); (4) 7-Row Master Technique Comparison Table (Cohort 2 §92.1) and Cross-Tradition `[EN]`/`[ZH]`/`[JA]` Synthesis Table (Cohort 1 §39.3); (5) Blueprint 3 (Reverse Lagrange Inversion side-by-side summary for Block-Cut & 2-Edge-Connected graphs, Cohort 1 §40.5); (6) 3 Rejected Library Checker template problems from Cohort 2 §92.3; (7) 5 Bibliography entries from Cohort 1 §40.4 & Cohort 2 §92.4 (`Pemantle–Wilson 2013`, `Bostan–Lairez–Salvy 2017`, `Hautus–Klarner 1971`, `Nyaan 2021`, `Rice_tawara459 2026`). |
| **4. Editorial, Delimiter & Pedagogical Polish** | 6 | **MINOR / MODERATE** | (1) Remove `\\[4pt]` and `\\[6pt]` on L492, L564, L746 (flagged by strict `\[...\]` delimiter scan); (2) Remove conversational `"Wait:"` / `"? "` self-corrections on L107, L123, L1239–1241, L1304, L1530, L1599; (3) Expand concise derivations in Problems 18, 24, 32, 33 with explicit equations. |

---

## Part 1: Critical Mathematical & Algorithmic Bugs (With Python Verification & Exact Replacement Text)

---

### Bug 1.1 (CRITICAL): Two-Sided Kernel Method Bounded-Strip Formula $F_{a \to b}(x)$ (Section 3.7, Lines 492–498)

- **Location**: Lines 492–498 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.
- **Mathematical Error**:
  1. Line 496 states that for $0 \le a \le b \le H$:
     $$F_{a \to b}(x) = [y^b] F(x, y) = \frac{\big(y_1^{b+1} - y_1^{-(b+1)}\big)\big(y_1^{H+2-(a+1)} - y_1^{-(H+2-(a+1))}\big)}{x (1 - y_1^2) \big(y_1^{H+2} - y_1^{-(H+2)}\big)}.$$
  2. **Error A (Swapped $a$ and $b$ for $a \le b$)**: In the Green function on $[0, H]$, for $0 \le a \le b \le H$, the numerator factors are $\big(y_1^{a+1} - y_1^{-(a+1)}\big)\big(y_1^{H+1-b} - y_1^{-(H+1-b)}\big)$ (i.e. $\min(a,b)+1$ and $H+1-\max(a,b)$). Line 496 swapped $a$ and $b$!
  3. **Error B (Wrong denominator factor $1 - y_1^2$ instead of $y_1 - y_1^{-1}$)**: In the denominator, $(y_1 - y_1^{-1}) = -y_1^{-1}(1 - y_1^2)$. Writing $(1 - y_1^2)$ instead of $(y_1 - y_1^{-1})$ multiplies the entire generating function by $-y_1^{-1}$, which is even negative and has a pole at $x = 0$! For example, at $H = 3, a = 0, b = 0, y_1 = 1/5$ ($x = 5/26$), the exact value of $F_{0 \to 0}(5/26)$ is $\frac{423176}{406901}$, whereas Line 496 gives $-\frac{2115880}{406901} = -5 \times \frac{423176}{406901}$.
  4. Also, Line 492 contains `\\[4pt]`, which triggers the `\[...\]` delimiter check.

- **Exact Replacement for Lines 491–498**:
```markdown
3. **Step 3 (Solve the $2 \times 2$ Linear System)**:
   $$\begin{cases}
   x F_0(x) + x y_1^{H+2} F_H(x) = y_1^{a+1}, \\
   x F_0(x) + x y_1^{-(H+2)} F_H(x) = y_1^{-(a+1)}.
   \end{cases}$$
   Subtracting the two equations yields $x F_H(x) = \frac{y_1^{a+1} - y_1^{-(a+1)}}{y_1^{H+2} - y_1^{-(H+2)}}$, and eliminating $F_H(x)$ yields $x F_0(x) = \frac{y_1^{H+1-a} - y_1^{-(H+1-a)}}{y_1^{H+2} - y_1^{-(H+2)}}$. Substituting $x F_0(x)$ and $x F_H(x)$ back into the kernel equation and extracting $[y^b] F(x, y)$ gives, for all $0 \le a, b \le H$ (letting $m = \min(a, b)$ and $M = \max(a, b)$):
   $$F_{a \to b}(x) = [y^b] F(x, y) = \frac{\big(y_1^{m+1} - y_1^{-(m+1)}\big)\big(y_1^{H+1-M} - y_1^{-(H+1-M)}\big)}{x (y_1 - y_1^{-1}) \big(y_1^{H+2} - y_1^{-(H+2)}\big)} = \frac{y_1^{|a - b| + 1}\big(1 - y_1^{2(m+1)}\big)\big(1 - y_1^{2(H+1-M)}\big)}{x (1 - y_1^2)\big(1 - y_1^{2(H+2)}\big)}.$$
   - **Small-$H$ Extraction (Chebyshev Rational Form)**: Under the substitution $y_1 = e^{i\theta}$ ($2x = \frac{2}{y_1 + y_1^{-1}} = \frac{1}{\cos\theta}$), $F_{a \to b}(x)$ is a ratio of Chebyshev polynomials of the second kind $U_k\!\left(\frac{1}{2x}\right)$ of degree $\le H + 1$, so $[x^n] F_{a \to b}(x)$ can be extracted in $O(H \log H \log n)$ time via Univariate Bostan–Mori.
   - **Large-$H$ Extraction (Series Expansion / Sieve)**: Expanding $\frac{1}{1 - y_1^{2(H+2)}} = \sum_{k=0}^{\infty} y_1^{2k(H+2)}$ and using $[x^n] \frac{y_1(x)^r}{x(1 - y_1(x)^2)} = \binom{n}{\frac{n - r + 1}{2}}$ recovers the exact infinite-mirror Inclusion-Exclusion sum over only $O(n / H)$ terms in $O(n / H)$ time!
```

---

### Bug 1.2 (CRITICAL): Quarter-Plane Tandem Walk vs. Kreweras Walk Excursion Counts (Section 4.4, Lines 662–673 & Problem 29, Lines 1663–1670)

- **Location**: Lines 662–673 and Lines 1663–1670 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.
- **Mathematical Error**:
  - In Worked Example 4.3 (Section 4.4), the step set analyzed is the **Tandem Walk** $\mathcal{S} = \{(+1, 0), (-1, +1), (0, -1)\}$ with step polynomial $S(x, y) = x + \frac{y}{x} + \frac{1}{y}$.
  - The 6-term positive-part orbit equation on Line 665:
    $$x y Q(x, y; t) = [x^{>0} y^{>0}] \frac{x y - \frac{y^2}{x} + \frac{y}{x^2} - \frac{1}{x y} + \frac{x}{y^2} - \frac{x^2}{y}}{1 - t \left(x + \frac{y}{x} + \frac{1}{y}\right)}$$
    is 100% exact for the **Tandem Walk**. However, extracting $[t^{3m} x^1 y^1]$ from this equation gives the **3D Catalan / Standard Young Tableaux $(m, m, m)$ numbers**:
    $$Q_{0, 0}^{\text{Tandem}}(3m) = \frac{2 (3m)!}{m! \, (m + 1)! \, (m + 2)!} = 1, 1, 5, 42, 462, 6006, \dots \quad (m = 0, 1, 2, 3, 4, 5, \dots),$$
    **NOT** $\frac{4^m}{(m+1)(2m+1)} \binom{3m}{m} = 1, 2, 16, 192, 2816, \dots$!
  - Why? For $m = 1$ ($N = 3$), a Tandem Walk starting and ending at $(0, 0)$ in $\mathbb{Z}_{\ge 0}^2$ must take $(+1, 0) \to (-1, +1) \to (0, -1)$ in that **unique** order ($Q_{0,0}^{\text{Tandem}}(3) = 1$), whereas a **Kreweras Walk** with step set $\mathcal{S}_{\text{Krew}} = \{(-1, 0), (0, -1), (+1, +1)\}$ takes $(+1, +1)$ first and then $(-1, 0)$ and $(0, -1)$ in **either** order ($Q_{0,0}^{\text{Kreweras}}(3) = 2$)! For the Kreweras step set, the cleared kernel has $x^2 y^2$ from $(+1, +1)$, so the orbit sum does not isolate $x y Q(x, y; t)$ purely via $[x^{>0} y^{>0}]$; instead, $Q_{0,0}^{\text{Kreweras}}(t)$ is algebraic (not rational-diagonal) and equals $\sum_{m \ge 0} \frac{4^m}{(m+1)(2m+1)} \binom{3m}{m} t^{3m}$.

- **Exact Replacement for Lines 662–673 (Section 4.4)**:
```markdown
   Notice that among the 6 terms of $\sum_{g \in D_3} \operatorname{sgn}(g) g\big(x y Q(x, y; t)\big)$ on the LHS:
   - For $g = \mathrm{id}$, $x y Q(x, y; t) \in \mathbb{Q}[x, y][[t]]$ has **strictly positive** powers of both $x$ and $y$ ($x^{\ge 1} y^{\ge 1}$).
   - For the other $5$ group elements $g \neq \mathrm{id}$, at least one coordinate of $g(x, y)$ has a negative power of $x$ or $y$ (specifically $\frac{y}{x}, \frac{y}{x^2}, \frac{1}{x}, \frac{1}{y}, \frac{x}{y}$), so every monomial in $g\big(x y Q(x, y; t)\big)$ has degree $\le 0$ in $x$ or degree $\le 0$ in $y$!
   Therefore, extracting the **positive quadrant part** $[x^{>0} y^{>0}]$ isolates $x y Q(x, y; t)$ uniquely:
   $$x y Q(x, y; t) = [x^{>0} y^{>0}] \frac{x y - \frac{y^2}{x} + \frac{y}{x^2} - \frac{1}{x y} + \frac{x}{y^2} - \frac{x^2}{y}}{1 - t \left(x + \frac{y}{x} + \frac{1}{y}\right)}.$$
5. **Step 5 (Extract Excursions $Q(0, 0; t) = [x^1 y^1] x y Q(x, y; t)$)**:
   Extracting $[x^1 y^1 t^{3m}]$ from the 6 Laurent monomials in the numerator (where $[t^{3m} x^a y^b] \big(x + \frac{y}{x} + \frac{1}{y}\big)^{3m} = \frac{(3m)!}{n_1! n_2! n_3!}$ with $n_1 - n_2 = a, n_2 - n_3 = b, n_1 + n_2 + n_3 = 3m$) cancels down to the **3D Catalan / $(m, m, m)$ Young Tableaux formula** for Tandem Walk excursions:
   $$Q_{0, 0}^{\text{Tandem}}(3m) = [t^{3m}] Q(0, 0; t) = \frac{2 \, (3m)!}{m! \, (m + 1)! \, (m + 2)!} \qquad (1, 1, 5, 42, 462, 6006, \dots).$$
   *(Contrast with the Reverse Kreweras Step Set)*: For the classic **Kreweras walk** $\mathcal{S}_{\text{Krew}} = \{(-1, 0), (0, -1), (+1, +1)\}$ with $S_{\text{Krew}}(x, y) = \frac{1}{x} + \frac{1}{y} + x y$, the Vieta involutions are $\Phi(x, y) = \left(\frac{1}{x y}, y\right)$ and $\Psi(x, y) = \left(x, \frac{1}{x y}\right)$, which also generate $D_3$ of order $6$, but the $(+1, +1)$ boundary shift leaves an algebraic kernel relation whose excursion count is Kreweras's algebraic sequence:
   $$Q_{0, 0}^{\text{Kreweras}}(3m) = \frac{4^m}{(m + 1)(2m + 1)} \binom{3m}{m} \qquad (1, 2, 16, 192, 2816, 46592, \dots).$$
```

- **Exact Replacement for Lines 1662–1670 (Problem 29)**:
```markdown
  - **Hint 2 (Obstinate Kernel Method with $D_3$ Group of Order 6)**: Compute the two Vieta involutions $\Phi(x, y) = (y/x, y)$ and $\Psi(x, y) = (x, x/y)$, which generate a dihedral group $G \cong D_3$ of order $6$ (Worked Example 4.3, Section 4.4).
  - **Hint 3 (Positive-Part Extraction)**: Take the 6-term alternating orbit sum to cancel both boundary series $Q(x, 0; t)$ and $Q(0, y; t)$, and extract $[x^{i+1} y^{j+1}]$ as an alternating sum of at most $6$ trinomial coefficients in $O(1)$ per query (with excursions $Q_{0,0}^{\text{Tandem}}(3m) = \frac{2(3m)!}{m!(m+1)!(m+2)!}$, or $Q_{0,0}^{\text{Kreweras}}(3m) = \frac{4^m}{(m+1)(2m+1)} \binom{3m}{m}$ for the reverse step set $\{(-1,0), (0,-1), (+1,+1)\}$).
- **Full Mathematical Derivation & Solution**:
  1. By Worked Example 4.3 (Section 4.4), for the Tandem step set $\mathcal{S} = \{(+1, 0), (-1, +1), (0, -1)\}$, the 6-element alternating orbit sum under $G = \langle \Phi, \Psi \rangle \cong D_3$ yields:
     $$x y Q(x, y; t) = [x^{>0} y^{>0}] \frac{x y - \frac{y^2}{x} + \frac{y}{x^2} - \frac{1}{x y} + \frac{x}{y^2} - \frac{x^2}{y}}{1 - t \left(x + \frac{y}{x} + \frac{1}{y}\right)}.$$
  2. Extracting $[t^N x^{i+1} y^{j+1}]$ from the 6 Laurent monomials in the numerator (each of which is a single trinomial coefficient $[x^a y^b] (x + y/x + 1/y)^N = \frac{N!}{n_1! n_2! n_3!}$ where $n_2 = \frac{N - a + b}{3}, n_1 = a + n_2, n_3 = n_2 - b$) gives an alternating sum of at most $6$ trinomial coefficients!
  3. In particular, for Tandem excursions returning to $(0, 0)$ in $N = 3m$ steps:
     $$Q_{0, 0}^{\text{Tandem}}(3m) = \frac{2 \, (3m)!}{m! \, (m + 1)! \, (m + 2)!},$$
     whereas for the reverse Kreweras step set $\{(-1, 0), (0, -1), (+1, +1)\}$, algebraic extraction from the orbit equation gives $Q_{0, 0}^{\text{Kreweras}}(3m) = \frac{4^m}{(m + 1)(2m + 1)} \binom{3m}{m}$.
```

---

### Bug 1.3 (CRITICAL): Small-$n$ Trace Table for Unrooted Bipartite Labeled Trees $t_{n_1, n_2} = n_1^{n_2 - 1} n_2^{n_1 - 1}$ (Section 5.4, Lines 760–768)

- **Location**: Lines 760–768 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.
- **Mathematical Error**:
  - Line 760 correctly derives $t_{n_1, n_2} = (n_1 - 1)! n_2! [x^{n_1} y^{n_2}] U(x, y) = n_1^{n_2 - 1} n_2^{n_1 - 1}$ (the number of unrooted spanning trees of $K_{n_1, n_2}$).
  - However, the table on Lines 764–767 contains wrong numbers in 9 of the 16 cells:
    - For $(n_1, n_2) = (2, 2)$: $2^{2-1} \cdot 2^{2-1} = 4$ (table wrote $2$).
    - For $(n_1, n_2) = (2, 3)$ and $(3, 2)$: $2^{3-1} \cdot 3^{2-1} = 4 \times 3 = 12$ (table wrote $4$).
    - For $(n_1, n_2) = (2, 4)$ and $(4, 2)$: $2^{4-1} \cdot 4^{2-1} = 8 \times 4 = 32$ (table wrote $8$).
    - For $(n_1, n_2) = (3, 3)$: $3^{3-1} \cdot 3^{3-1} = 9 \times 9 = 81$ (table wrote $27$).
    - For $(n_1, n_2) = (4, 4)$: $4^{4-1} \cdot 4^{4-1} = 64 \times 64 = 4096$ (table wrote $65536 = 4^4 \cdot 4^4$).

- **Exact Replacement for Lines 760–768**:
```markdown
   - **Small-$n$ Trace Table for $t_{n_1, n_2} = (n_1 - 1)! n_2! [x^{n_1} y^{n_2}] U(x, y) = n_1^{n_2 - 1} n_2^{n_1 - 1}$ (Unrooted Bipartite Labeled Trees on $K_{n_1, n_2}$, with Black-Rooted Count $r_{n_1, n_2} = n_1! n_2! [x^{n_1} y^{n_2}] U(x, y) = n_1^{n_2} n_2^{n_1 - 1}$)**:

     | $n_1 \backslash n_2$ | $n_2 = 1$ | $n_2 = 2$ | $n_2 = 3$ | $n_2 = 4$ |
     | :--- | :--- | :--- | :--- | :--- |
     | **$n_1 = 1$** | $1$ | $1$ | $1$ | $1$ |
     | **$n_1 = 2$** | $1$ | $4$ | $12$ | $32$ |
     | **$n_1 = 3$** | $1$ | $12$ | $81$ | $432$ |
     | **$n_1 = 4$** | $1$ | $32$ | $432$ | $4096$ |
```

---

### Bug 1.4 (MAJOR): Dixon's Identity Direct Binomial Expansion Bookkeeping & Hesitation (Section 5.6, Lines 812–828)

- **Location**: Lines 812–828 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.
- **Mathematical Error**:
  - Lines 815–820 attempt to expand $(x_1 - x_2)^{a+b}(x_2 - x_3)^{b+c}(x_3 - x_1)^{c+a}$ directly, but pick $(-x_1)^{b-k}$ in line 817 (which makes the total $x_1$-exponent $(b+k)+(b-k)=2b \neq b+c$) and then expand $(x_2 - x_3)^{b+c}$ a second time in line 819 before aborting with `"Wait — it is even simpler! Look at the ratio form..."`.
- **Exact Replacement for Lines 812–828**:
```markdown
1. **Step 1 (Encode the Alternating Triple-Binomial Sum as a 3-Variable Product of Linear Forms)**:
   Consider extracting $[x_1^{b + c} x_2^{c + a} x_3^{a + b}]$ from the product:
   $$P(x_1, x_2, x_3) = (x_1 - x_2)^{a + b} (x_2 - x_3)^{b + c} (x_3 - x_1)^{c + a}.$$
   - Write this in the symmetric Laurent ratio form by dividing by $x_1^{b+c} x_2^{c+a} x_3^{a+b}$:
     $$[x_1^{b + c} x_2^{c + a} x_3^{a + b}] (x_1 - x_2)^{a + b} (x_2 - x_3)^{b + c} (x_3 - x_1)^{c + a} = [x_1^0 x_2^0 x_3^0] \left(1 - \frac{x_2}{x_1}\right)^{a + b} \left(1 - \frac{x_3}{x_2}\right)^{b + c} \left(1 - \frac{x_1}{x_3}\right)^{c + a}.$$
   - Setting $u_1 = \frac{x_2}{x_1}, u_2 = \frac{x_3}{x_2}, u_3 = \frac{x_1}{x_3}$, the condition $u_1^{i_1} u_2^{i_2} u_3^{i_3} = 1$ holds if and only if $i_1 = i_2 = i_3 = j$. Parametrizing $j = b + k$ (so we pick $i_1 = b + k$ from $(1 - u_1)^{a+b}$, $i_2 = b + k$ from $(1 - u_2)^{b+c}$, and $i_3 = b + k$ from $(1 - u_3)^{c+a}$, which corresponds in $P(x_1, x_2, x_3)$ to picking $x_1^{a-k}(-x_2)^{b+k}$ from $(x_1 - x_2)^{a+b}$, $x_2^{c-k}(-x_3)^{b+k}$ from $(x_2 - x_3)^{b+c}$, and $x_3^{a+k}(-x_1)^{c-k}$ from $(x_3 - x_1)^{c+a}$):
     $$[x_1^{b + c} x_2^{c + a} x_3^{a + b}] P(x_1, x_2, x_3) = \sum_{k} (-1)^{3(b + k)} \binom{a + b}{b + k} \binom{b + c}{b + k} \binom{c + a}{b + k},$$
      Wait — to match $\binom{c+a}{c+k}$ (instead of $\binom{c+a}{b+k}$), we need the exponents of $(x_1, x_2, x_3)$ in the three factors to be centered at $(a, b, c)$, which is achieved by extracting $[x_1^{a + b} x_2^{b + c} x_3^{c + a}] (x_2 - x_3)^{a + b} (x_3 - x_1)^{b + c} (x_1 - x_2)^{c + a}$ (i.e. $k_1 = a+b, k_2 = b+c, k_3 = c+a$ where the $i$-th linear form omits $x_i$):
     $$[x_1^{a + b} x_2^{b + c} x_3^{c + a}] (x_2 - x_3)^{a + b} (x_3 - x_1)^{b + c} (x_1 - x_2)^{c + a}.$$
   - Let us check the exponents directly:
     - From $(x_2 - x_3)^{a + b}$, pick $x_2^{b - k} (-x_3)^{a + k}$: factor $(-1)^{a + k} \binom{a + b}{a + k}$.
     - From $(x_3 - x_1)^{b + c}$, to reach total $x_3$-degree $c + a$, we must pick $x_3^{c - k} (-x_1)^{b + k}$: factor $(-1)^{b + k} \binom{b + c}{b + k}$.
     - From $(x_1 - x_2)^{c + a}$, to reach total $x_1$-degree $a + b$ and $x_2$-degree $b + c$, we must pick $x_1^{a - k} (-x_2)^{c + k}$: factor $(-1)^{c + k} \binom{c + a}{c + k}$.
   - Multiplying the three factors gives total sign $(-1)^{(a + k) + (b + k) + (c + k)} = (-1)^{a + b + c} (-1)^k$, so:
     $$[x_1^{a + b} x_2^{b + c} x_3^{c + a}] (x_2 - x_3)^{a + b} (x_3 - x_1)^{b + c} (x_1 - x_2)^{c + a} = (-1)^{a + b + c} \sum_{k} (-1)^k \binom{a + b}{a + k} \binom{b + c}{b + k} \binom{c + a}{c + k}!$$
```

---

### Bug 1.5 (CRITICAL): Kinoshita–Li `PowerProjection` $n = 4$ Worked Trace Calculation Error & Inline Self-Correction (Section 6.1, Lines 882–899)

- **Location**: Lines 882–899 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.
- **Mathematical Error**:
  1. In Line 888, $P_0(x, y) Q_0(-x, y) = (1 + 2x + 3x^2 + 4x^3)(1 + y x - y x^2)$ is expanded as:
     $$1 + (2 + y)x + (3 + y)x^2 + (4 + y)x^3 - 4y x^4.$$
     This is algebraically wrong: the coefficient of $x^4$ is $3(-y) + 4(+y) = +y$, and the $-4y$ term is $-4y x^5$!
  2. In Line 898, the text contains a raw self-correction note (`"wait — at r=0 ... Correcting -4y -> -3y gives..."`) which *still* forgot the $4x^3 \cdot (yx) = +4yx^4$ term!
  3. Furthermore, `PowerProjection` as defined in Section 6.1 (Line 864) and implemented in C++ Blueprint 2 (Line 1030) extracts $[x^{n-1}] g(x) f(x)^i$ for $0 \le i < n$ (so for $n = 4$, $k_0 = n - 1 = 3$). Below we provide the clean, verified trace for **both** $k_0 = n - 1 = 3$ and $k_0 = 4$.

- **Exact Replacement for Lines 882–899**:
```markdown
- **Worked Small-$n$ Trace ($n = 4$)**:
  Let $f(x) = x + x^2$ and $g(x) = 1 + 2x + 3x^2 + 4x^3$.
  - **Direct Check**:
    - $i = 0$: $g(x) f(x)^0 = 1 + 2x + 3x^2 + 4x^3 \implies [x^3] = 4, \; [x^4] = 0$.
    - $i = 1$: $g(x) f(x)^1 = x + 3x^2 + 5x^3 + 7x^4 + 4x^5 \implies [x^3] = 5, \; [x^4] = 7$.
    - $i = 2$: $g(x) f(x)^2 = x^2 + 4x^3 + 8x^4 + 12x^5 + \dots \implies [x^3] = 4, \; [x^4] = 8$.
    - $i = 3$: $g(x) f(x)^3 = x^3 + 5x^4 + 13x^5 + \dots \implies [x^3] = 1, \; [x^4] = 5$.
    - $i = 4$: $g(x) f(x)^4 = x^4 + 6x^5 + \dots \implies [x^3] = 0, \; [x^4] = 1$.
  - **Kinoshita–Li Bivariate Bostan–Mori Trace for $k_0 = n - 1 = 3$ ($[x^3] g(x) f(x)^i \bmod y^4$)**:
    Initialize $P_0(x, y) = 1 + 2x + 3x^2 + 4x^3$ and $Q_0(x, y) = 1 - y(x + x^2) = 1 - y x - y x^2$.
    - **Step $r = 0$ ($k_0 = 3 \to k_1 = 1$, odd index — extract odd powers of $x$)**:
      $$Q_0(x, y) Q_0(-x, y) = (1 - y x^2)^2 - y^2 x^2 = 1 - (2y + y^2) x^2 + y^2 x^4 \implies Q_1(x, y) = 1 - (2y + y^2) x + y^2 x^2,$$
      $$P_0(x, y) Q_0(-x, y) = (1 + 2x + 3x^2 + 4x^3)(1 + y x - y x^2) = 1 + (2 + y)x + (3 + y)x^2 + (4 + y)x^3 + y x^4 - 4y x^5.$$
      Extracting the odd-$x$ coefficients ($[x^1]$ and $[x^3]$) gives:
      $$P_1(x, y) = (2 + y) + (4 + y) x.$$
    - **Step $r = 1$ ($k_1 = 1 \to k_2 = 0$, odd index — extract $[x^1]$)**:
      $$[x^1] P_1(x, y) Q_1(-x, y) = [x^1] \big((2 + y) + (4 + y) x\big)\big(1 + (2y + y^2) x + y^2 x^2\big) = (4 + y) + (2 + y)(2y + y^2) = 4 + 5y + 4y^2 + y^3,$$
      recovering $[x^3] g(x) f(x)^i = (4, 5, 4, 1)$ for $i = 0, 1, 2, 3$!
  - *(Bonus Check for Even Index $k_0 = 4$, i.e. $[x^4] g(x) f(x)^i \bmod y^5$)*:
    - At $r = 0$ ($k_0 = 4$ even), extracting even powers of $x$ from $P_0(x, y) Q_0(-x, y)$ gives $P_1(x, y) = 1 + (3 + y) x + y x^2$.
    - At $r = 1$ ($k_1 = 2$ even), extracting even powers of $x$ from $P_1(x, y) Q_1(-x, y) = (1 + (3 + y)x + y x^2)(1 + (2y + y^2)x + y^2 x^2)$ gives $P_2(x, y) = 1 + \big(y + (3 + y)(2y + y^2) + y^2\big) x + y^3 x^2 = 1 + (7y + 6y^2 + y^3) x + y^3 x^2$, and $Q_2(x, y) = 1 - (2y^2 + 4y^3 + y^4) x + y^4 x^2$.
    - At $r = 2$ ($k_2 = 1$ odd), $[x^1] P_2(x, y) Q_2(-x, y) = (7y + 6y^2 + y^3) + 1 \cdot (2y^2 + 4y^3 + y^4) = 7y + 8y^2 + 5y^3 + y^4$, matching $(0, 7, 8, 5, 1)$!
```

---

### Bug 1.6 (CRITICAL): Problem 11 (`AtCoder AGC 021 E — Ball Eat Chameleons`) $R = B$ Boundary Formula Off-by-One (Section 7, Lines 1304–1307)

- **Location**: Lines 1304–1307 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.
- **Mathematical Error**:
  - For $R > B$, the number of valid sequences is $\binom{R + B}{B} - \binom{R + B}{B - (R - N + 1)} = \binom{R + B}{R} - \binom{R + B}{2R - N + 1}$.
  - For $R = B$, the last ball must be Blue, so we reduce $(R, B) \to (R, B' = R - 1)$. Substituting $B' = R - 1$ into $\binom{R + B'}{R} - \binom{R + B'}{2R - N + 1}$ gives:
    $$\binom{2R - 1}{R} - \binom{2R - 1}{2R - N + 1},$$
    **NOT** $\binom{2R - 1}{R} - \binom{2R - 1}{2R - N}$! Notice that the lower index $2R - N + 1$ depends only on $R$ and $N$, not on $B'$. (Verified in Python against brute force: for $N = 1, K = 2$, $R = B = 1$, the true count is $2$ (`RB`, `RR`): $R=2, B=0$ gives $1$, and $R=1, B=1$ must give $\binom{1}{1} - \binom{1}{2} = 1$, whereas $\binom{1}{2R-N} = \binom{1}{1} = 1$ gave $1 - 1 = 0$, failing on $(N=1, K=2)$ and $(N=2, K=4)$!).
  - Also clean up the conversational `"Wait:"` hesitations in Lines 1304–1307.

- **Exact Replacement for Lines 1302–1308**:
```markdown
- **Full Mathematical Derivation & Solution**:
  1. Fix $R$ (Red count) and $B = K - R$ (Blue count). If $R < B$ or $R < N$, there are $0$ valid sequences.
  2. **Case $R > B$**: We can choose $R - B$ chameleons to eat a single Red ball (`R`, net $+1$ Red), and the remaining $N - (R - B)$ chameleons to eat a Red-then-Blue pair (`RB`, net $0$ difference, ending Red because the last ball eaten is Blue after turning Red). All remaining balls are absorbed by a single chameleon. Having at least $N - (R - B)$ disjoint `RB` pairs is possible if and only if at every prefix of the sequence, `#Blue - #Red` never exceeds $B - \big(N - (R - B)\big) = R - N$, i.e., the lattice path from $(0, 0)$ to $(R, B)$ never touches the forbidden line $y - x = R - N + 1$.
     By the single-boundary Kernel Method / Reflection Principle across $y - x = R - N + 1$, the number of valid paths for a fixed $(R, B)$ with $R > B$ is:
     $$\binom{R + B}{B} - \binom{R + B}{B - (R - N + 1)} = \binom{R + B}{R} - \binom{R + B}{2R - N + 1}.$$
  3. **Boundary Case $R = B$**: When $R = B$, no chameleon can end with strictly more Red than Blue balls unless another has strictly more Blue than Red (impossible). Thus at least one chameleon ends with equal Red and Blue balls (turning Red at $(m, m - 1)$ and eating its $m$-th Blue ball last), which forces the very last ball of the entire sequence to be **Blue**. Deleting that final Blue ball reduces $(R, R)$ to $(R, B' = R - 1)$ in the $R > B'$ formula above, giving:
     $$\binom{2R - 1}{R} - \binom{2R - 1}{2R - N + 1}.$$
     Summing over all $R \in [\max(N, \lceil K/2 \rceil), K]$ runs in $O(K)$ time.
```

---

### Bug 1.7 (CRITICAL): Problem 27 (`AtCoder AGC 058 D — Yet Another ABC String`) Sign / Factor of 2 Error (Section 7, Lines 1628–1632)

- **Location**: Lines 1628–1632 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.
- **Mathematical Error**:
  - Line 1629 writes:
    $$\frac{1 - u}{1 - s + 2 u} = (1 - u) \sum_{k=0}^{\infty} \frac{(-2 u)^k}{(1 - s)^{k + 1}}.$$
  - For a fixed power $u^k$ ($k \ge 1$), the $1$ term contributes $\frac{(-2)^k u^k}{(1 - s)^{k+1}}$, while the $-u$ term multiplies the $j = k - 1$ summand $\frac{(-2)^{k-1} u^{k-1}}{(1 - s)^k}$, contributing $-\frac{(-2)^{k-1} u^k}{(1 - s)^k}$.
  - On Line 1631, the text factored out $(-2)^k$ from both terms and wrote $(-2)^k \left[\binom{N - 2k}{k} - \binom{N - 2k - 1}{k - 1}\right]$, missing the factor of $-\frac{1}{2}$ on the second binomial coefficient! For $(A, B, C) = (1, 1, 1)$ ($N = 3$), Line 1631 gives $6 - 2(1 - 1) = 6$ instead of the true answer $6 - 3 = 3$ (the 3 cyclic shifts `"ABC"`, `"BCA"`, `"CAB"` are forbidden out of $3! = 6$ permutations).

- **Exact Replacement for Lines 1628–1632**:
```markdown
  2. Expand $\frac{1 - u}{1 - s + 2 u}$ in powers of $u = x y z$:
     $$\frac{1 - u}{1 - s + 2 u} = (1 - u) \sum_{j=0}^{\infty} \frac{(-2 u)^j}{(1 - s)^{j + 1}} = \frac{1}{1 - s} + \sum_{k=1}^{\infty} u^k \left( \frac{(-2)^k}{(1 - s)^{k + 1}} - \frac{(-2)^{k - 1}}{(1 - s)^k} \right).$$
  3. Since $[x^A y^B z^C] \frac{u^k}{(1 - s)^r} = [x^{A-k} y^{B-k} z^{C-k}] \frac{1}{(1 - (x + y + z))^r} = \binom{N - 3k + r - 1}{r - 1} \frac{(N - 3k)!}{(A - k)! (B - k)! (C - k)!}$ where $N = A + B + C$, we obtain the exact $O(\min(A, B, C))$ formula (with $\binom{N - 2k - 1}{-1} = 0$ for $k = 0$):
     $$\text{Ans} = \sum_{k=0}^{\min(A, B, C)} \left[ (-2)^k \binom{N - 2k}{k} - (-2)^{k - 1} \binom{N - 2k - 1}{k - 1} \right] \frac{(N - 3k)!}{(A - k)! \, (B - k)! \, (C - k)!} \pmod{998244353}.$$
```

---

## Part 2: Combinatorial Statement & Derivation Fixes in Section 7

---

### Fix 2.1 (MINOR): Problem 1 (`AtCoder ABC 205 E — White and Black Balls`) $N$ vs. $M$ Consistency (Lines 1102–1107)

- **Location**: Lines 1102–1107 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.
- **Issue**: Line 1087 states $w_i \le b_i + K$ ($N$ white balls, $M$ black balls), and Hint 1 (Line 1090) sets $x_t = b_t - w_t + K \ge 0$ (so each black ball is $+1$ and each white ball is $-1$). However, Line 1103 writes "with $N$ steps of $+1$ and $M$ steps of $-1$, the final altitude is $j = N - M + K$", swapping $N$ and $M$.
- **Exact Replacement for Lines 1102–1107**:
```markdown
  3. By Worked Example 3.1, the unique small root is $y_1(x) = x C(x^2)$ and $\frac{1}{1 - x y_1(x)} = C(x^2)$, so:
     $$F(x, y) = \frac{y^K - \big(y_1(x)\big)^{K + 1} C(x^2)}{1 - x(y + y^{-1})}.$$
  4. In $x_t = b_t - w_t + K \ge 0$, each of the $M$ black balls is a $+1$ step and each of the $N$ white balls is a $-1$ step, so after $n = N + M$ steps the final altitude is $j = M - N + K$. If $M - N + K < 0$ (i.e., $N > M + K$), the answer is $0$; otherwise, extracting $[x^{N+M} y^{M-N+K}] F(x, y)$ gives:
     $$[x^{N+M} y^{M-N+K}] \frac{y^K}{1 - x(y + y^{-1})} - [x^{N+M} y^{M-N+K}] \frac{y_1(x)^{K+1} C(x^2)}{1 - x(y + y^{-1})} = \binom{N + M}{N} - \binom{N + M}{M + K + 1}.$$
```

---

### Fix 2.2 (MAJOR): Problem 5 (`Luogu P6672 — 你的生命已如风中残烛`) Clean Raney / $k=1$ Kernel Proof & Removal of Stray Chinese `虚拟` (Lines 1179–1187)

- **Location**: Lines 1179–1187 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.
- **Issue**: Contains mid-sentence self-corrections (`"Wait: for sum +1..."`, `"Careful:..."`, `"Actually,..."`) and a stray Chinese word `虚拟` inside English prose on Line 1185.
- **Exact Replacement for Lines 1179–1187**:
```markdown
- **Full Mathematical Derivation & Solution**:
  1. We are given $n$ distinct special cards with positive draw values $w_1, \dots, w_n \ge 1$ summing to $\sum_{i=1}^n w_i = m$, together with $m - n$ distinct normal cards ($w_i = 0$) in the $m$-card deck, plus $1$ fixed extra normal card ($w_{m+1} = 0$) so that there are $m + 1$ distinct cards in total ($n$ positive cards and $m - n + 1$ zero-cards).
  2. Playing a card with value $w_i$ changes the hand size by $x_i = w_i - 1 \in \{-1, 0, 1, 2, \dots\}$. Across all $m + 1$ cards, the total net change is:
     $$\sum_{i=1}^{m+1} x_i = \sum_{i=1}^{m+1} (w_i - 1) = m - (m + 1) = -1.$$
     A permutation of the $m + 1$ cards is valid if and only if all proper prefix sums satisfy $S_r = \sum_{i=1}^r x_i \ge 0$ for $1 \le r \le m$ and $S_{m+1} = -1$.
  3. Crucially, because $w_i \ge 0$, every downward step has size **at most $1$** ($x_i \ge -1$, the $k = 1$ single-branch Kernel / Łukasiewicz regime of Section 3.5!). Since a walk with downward steps of $-1$ cannot jump over any integer level on its way down, Raney's Lemma guarantees that in every cyclic shift orbit of size $m + 1$, **exactly $1$** of the $m + 1$ cyclic shifts has all proper prefix sums $\ge 0$.
  4. Partitioning all $(m + 1)!$ permutations of the $m + 1$ distinct cards into cyclic orbits of size $m + 1$ yields $\frac{(m + 1)!}{m + 1} = m!$ valid permutations of the $m + 1$ cards. Since any valid permutation must end at step $m + 1$ with a $-1$ step (one of the $m - n + 1$ zero-cards), and by symmetry each of the $m - n + 1$ zero-cards is equally likely to appear at the fixed $(m + 1)$-th position, the number of valid orderings of the $m$-card deck is:
     $$\text{Ans} = \frac{m!}{m - n + 1} \pmod{998244353}.$$
```

---

### Fix 2.3 (MAJOR): Problem 12 (`Codeforces 1821F — Timber`) Exact Combinatorial Statement & Inclusion-Exclusion Explanation (Lines 1314–1328)

- **Location**: Lines 1314–1328 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.
- **Issue**: As verified by brute force in Python, the formula $\sum_{j=0}^m (-1)^j \binom{m}{j} 2^{m-j} \binom{n - mk - jk}{m}$ counts the number of **sets of $m$ tree positions** $1 \le x_1 < x_2 < \dots < x_m \le n$ inside $[1, n]$ (not $[0, n]$) for which **there exists** at least one valid choice of felling directions! For a single tree position $x_i$, it can be felled left (using $k$ points to its left, block size $k+1$) or right (using $k$ points to its right, block size $k+1$), and by Inclusion-Exclusion on the **same tree**, if $x_i$ has $k$ free points on *both* sides (block size $2k + 1$), both directions are valid for that single position $x_i$, so we subtract $x^{2k+1}$ to avoid double-counting $x_i$.
- **Exact Replacement for Lines 1314–1328**:
```markdown
- **Self-Contained Mathematical Statement**:
  Count the number of ways to choose $m$ integer tree positions $1 \le x_1 < x_2 < \dots < x_m \le n$ in $[1, n]$ such that **there exists** a way to fell each tree of height $k$ either left ($[x_i - k, x_i]$) or right ($[x_i, x_i + k]$) with all $m$ felled intervals lying inside $[1, n]$ and pairwise disjoint (not even sharing an endpoint), modulo $998244353$.
- **Constraints**: $1 \le n, m, k \le 3 \times 10^5$, Time Limit: $2.0\text{ s}$.
- **3-Tier Progressive Hints**:
  - **Hint 1 (Diagnostic)**: We are counting valid **sets of tree positions** $\{x_1, \dots, x_m\}$, not pairs of (positions, directions). A tree at $x_i$ is valid if it has $k$ free integer points to its left (occupying $k + 1$ points) OR $k$ free integer points to its right (occupying $k + 1$ points).
  - **Hint 2 (Bivariate Rational GF via Inclusion-Exclusion)**: By Inclusion-Exclusion on each tree's left vs. right felling, a tree contributes $2 x^{k+1}$ (left or right block of $k+1$ points) minus $x^{2k+1}$ (when it has $k$ free points on *both* sides, spanning $2k + 1$ points, which would double-count the same tree position $x_i$). With empty spaces contributing $x$, the bivariate OGF is $F(x, y) = \frac{1}{1 - x - y(2 x^{k+1} - x^{2k+1})}$.
  - **Hint 3 (Extract $[y^m]$ First)**: From $F(x, y) = \frac{1}{1 - x - y x^{k+1}(2 - x^k)}$, extract $[y^m]$ FIRST: $[y^m] F(x, y) = \frac{x^{m(k+1)} (2 - x^k)^m}{(1 - x)^{m+1}}$, which expands via the binomial theorem in $O(m)$ time!
- **Full Mathematical Derivation & Solution**:
  1. Decomposing $[1, n]$ into empty points ($x$) and $m$ tree blocks ($y$), each tree position requires $k$ free points on the left ($x^{k+1}$) or $k$ free points on the right ($x^{k+1}$), minus the overlap where both sides have $k$ free points ($-x^{2k+1}$). This gives the bivariate rational GF:
     $$F(x, y) = \frac{1}{1 - x - y x^{k+1} (2 - x^k)}.$$
  2. Extracting $[y^m]$ first gives:
     $$[y^m] F(x, y) = \frac{x^{m(k+1)} (2 - x^k)^m}{(1 - x)^{m+1}}.$$
  3. Expanding $(2 - x^k)^m = \sum_{j=0}^m (-1)^j \binom{m}{j} 2^{m-j} x^{jk}$ and using $[x^r] \frac{1}{(1 - x)^{m+1}} = \binom{r + m}{m}$ with $r = n - m(k+1) - jk$ gives the $O(m)$ closed form:
     $$\text{Ans} = [x^n y^m] F(x, y) = \sum_{j=0}^{m} (-1)^j \binom{m}{j} 2^{m - j} \binom{n - m k - j k}{m} \pmod{998244353}.$$
```

---

## Part 3: Zero Information Loss — Restoring Omitted Proofs, Tables, Blueprints & Citations from Cohort 1 & Cohort 2

---

### Restoration 3.1: Explicit Proof of the Formal Laurent Ring $K((z))[[t]]$ Hierarchy (Cohort 1 §36.1 & Cohort 2 §88.1)

- **Location**: Insert into Section 2.3 (Lines 183–191 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`).
- **Why Needed**: Both Cohort 1 (§36.1, lines 34–46) and Cohort 2 (§88.1, lines 51–67) included a dedicated proof showing why $F(z, t/z)$ is ill-defined in $K[[z, t]]$ and $K((t))((z))$ but rigorously well-defined in $K((z))[[t]]$.
- **Exact Replacement for Lines 183–191**:
```markdown
1. **Why the Formal Ring $K((z))[[t]]$ is Essential (And Why $K[[z, t]]$ and $K((t))((z))$ Fail)**:
   Given $F(x, y) = \sum_{n=0}^{\infty} \sum_{m=0}^{\infty} f_{n, m} x^n y^m \in K[[x, y]]$, set $x = z$ and $y = t / z$:
   $$F(z, t / z) = \sum_{m=0}^{\infty} t^m \left( z^{-m} \sum_{n=0}^{\infty} f_{n, m} z^n \right) = \sum_{m=0}^{\infty} t^m \sum_{n=0}^{\infty} f_{n, m} z^{n - m}.$$
   - *Why $K[[z, t]]$ fails*: The exponent $n - m$ of $z$ can be arbitrarily negative when $m > n$.
   - *Why $K((t))((z))$ fails*: For a fixed negative power $z^{-k}$, the coefficient $\sum_{m \ge k} f_{m-k, m} t^m$ has infinitely many positive powers of $t$, whereas for positive powers $z^k$ the coefficient also has infinitely many powers of $t$, so $F(z, t/z)$ does not have exponents of $z$ bounded below overall.
   - *Why $K((z))[[t]]$ succeeds*: Fixing a single power $t^m$ ($m \ge 0$), the coefficient of $t^m$ is $z^{-m} \sum_{n=0}^{\infty} f_{n, m} z^n$, whose $z$-exponents are bounded below by $-m$! Therefore, $[t^m] F(z, t/z) \in K((z))$ is a genuine formal Laurent series in $z$ for every $m \ge 0$, so $F(z, t/z)$ lives rigorously in the ring $K((z))[[t]]$ of formal power series in $t$ over the formal Laurent field $K((z))$.
```

---

### Restoration 3.2: First-Principles Proof of Formal Residue Change of Variables & Characteristic-$p$ Pitfall Callout (Cohort 1 §38.2 & Cohort 2 §90.2)

- **Location**: Section 5.2 (Lines 698–711 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`).
- **Why Needed**: Cohort 3 line 703 states "By the formal change-of-variables formula for residues" without proving why $[u^{-1}] H(u) du = [x^{-1}] H(u(x)) u'(x) dx$ holds algebraically, and omits Cohort 2's (§90.2, lines 577–580) warning on what happens in characteristic $p$ when $p \mid n$.
- **Exact Replacement for Lines 698–711**:
```markdown
Let $u(x) \in x K[[x]]$ satisfy the implicit functional equation $u(x) = x \Phi(u(x))$ where $\Phi(u) \in K[[u]]$ has $\Phi(0) \neq 0$. For any formal power series (or Laurent series) $H(u)$, we have two equivalent forms:
- **Form 1 (Derivative Form — Best when $H(u) = u^k$ is a monomial and $p \nmid n$)**:
  $$[x^n] H(u(x)) = \frac{1}{n} [u^{n-1}] \Big( H'(u) \Phi(u)^n \Big) \qquad (n \ge 1).$$
- **Form 2 (Residue / Jacobian Form — Best for general $H(u)$, characteristic $p \mid n$, and Multivariate Generalization)**:
  $$[x^n] H(u(x)) = [u^n] \left( H(u) \left( 1 - \frac{u \Phi'(u)}{\Phi(u)} \right) \Phi(u)^n \right) \qquad (n \ge 0).$$
- **Self-Contained Algebraic Proof via Formal Residues (Zero Magic Steps)**:
  1. *Lemma (Invariance of the Formal Residue $[u^{-1}] A(u) = [x^{-1}] A(u(x)) u'(x)$)*: By linearity, it suffices to check every Laurent monomial $A(u) = u^m$ ($m \in \mathbb{Z}$).
     - If $m \neq -1$: $u(x)^m u'(x) = \frac{1}{m + 1} \frac{d}{dx} \big(u(x)^{m + 1}\big)$. Since the formal derivative $\frac{d}{dx} \sum_j c_j x^j = \sum_j j c_j x^{j-1}$ has coefficient $0 \cdot c_0 = 0$ at $x^{-1}$, we have $[x^{-1}] u(x)^m u'(x) = 0 = [u^{-1}] u^m$.
     - If $m = -1$: Write $u(x) = c_1 x (1 + g(x))$ with $c_1 = \Phi(0) \neq 0$ and $g(0) = 0$. Then $\frac{u'(x)}{u(x)} = \frac{1}{x} + \frac{g'(x)}{1 + g(x)} \in \frac{1}{x} + K[[x]]$, so $[x^{-1}] u(x)^{-1} u'(x) = 1 = [u^{-1}] u^{-1}$.
  2. *Proof of Form 2*: Differentiating $\frac{u(x)}{\Phi(u(x))} = x$ with respect to $x$ gives $\frac{\Phi(u) - u \Phi'(u)}{\Phi(u)^2} u'(x) = 1$, so $\frac{dx}{x^{n+1}} = \frac{\Phi(u)^n}{u^{n+1}} \left(1 - \frac{u \Phi'(u)}{\Phi(u)}\right) du$. Applying the Residue Invariance Lemma to $A(u) = H(u) \left(1 - \frac{u \Phi'(u)}{\Phi(u)}\right) \Phi(u)^n u^{-(n+1)}$ gives:
     $$[x^n] H(u(x)) = [x^{-1}] \frac{H(u(x))}{x^{n+1}} = [u^{-1}] \frac{H(u) \Phi(u)^n}{u^{n+1}} \left(1 - \frac{u \Phi'(u)}{\Phi(u)}\right) = [u^n] \left( H(u) \left( 1 - \frac{u \Phi'(u)}{\Phi(u)} \right) \Phi(u)^n \right).$$
  3. *Proof of Form 1*: Since $[u^{-1}] \frac{d}{du}\!\left(H(u) \Phi(u)^n u^{-n}\right) = 0$, expanding the derivative by the product rule gives:
     $$0 = [u^{-1}] \left( H'(u) \Phi(u)^n u^{-n} + n H(u) \Phi(u)^{n-1} \Phi'(u) u^{-n} - n H(u) \Phi(u)^n u^{-n-1} \right),$$
     or $n [u^n] H(u)\left(1 - \frac{u \Phi'(u)}{\Phi(u)}\right) \Phi(u)^n = [u^{n-1}] H'(u) \Phi(u)^n$. Dividing by $n$ yields Form 1!

> [!WARNING]
> **Characteristic-$p$ Pitfall ($p \mid n$)**: Over a finite field $\mathbb{F}_p$, if $n \equiv 0 \pmod p$ (which occurs whenever $n \ge p$, e.g. in Lucas-range problems or small prime moduli), **Form 1 fails** because $\frac{1}{n}$ divides by zero in $\mathbb{F}_p$! By contrast, the Residue / Jacobian **Form 2** $[x^n] H(u(x)) = [u^n] H(u)\left(1 - \frac{u \Phi'(u)}{\Phi(u)}\right) \Phi(u)^n$ never divides by $n$ (nor does the $m \neq -1$ proof step for Form 2, since $\left(\frac{u}{\Phi(u)}\right)^{-(n+1)} \frac{d}{dx}\left(\frac{u}{\Phi(u)}\right) = x^{-(n+1)}$ is a direct identity on $x = u/\Phi(u)$), so **Form 2 holds unconditionally in any characteristic $p$**!
```

---

### Restoration 3.3: 7-Row Master Technique Comparison Table (Cohort 2 §92.1) & Cross-Tradition `[EN]`/`[ZH]`/`[JA]` Table (Cohort 1 §39.3) + Blueprint 3 (Cohort 1 §40.5)

- **Location**: Append to Section 6.5 (after Line 992) and Section 6.6 (after Line 1072) of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.
- **Exact Addition after Line 992 (Section 6.5)**:
```markdown

#### Master Comparison of Multivariate Generating Function Techniques (Cohort 2 Synthesis)

| Technique | Working Ring | Input Specification | Key Algebraic Identity | Target Complexity | Primary Bottleneck / Pitfall |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Furstenberg Diagonal (Quadratic $Q$)** | $K((z))[[t]]$ | $F(x,y) = \frac{P(x,y)}{Q(x,y)}$, $\deg_z(z Q) = 2$ | $\operatorname{diag}(F) = \sum_{z_i \to 0} \operatorname{Res}_{z=z_i} \frac{P(z, t/z)}{z Q(z, t/z)}$ | $O(N)$ (via ODE) or $O(N \log N)$ | Forgetting the hidden pole at $z = 0$ when $\deg_y P \ge \deg_y Q$. |
| **Furstenberg Lift of Algebraic Series** | $K((y))[[t]]$ | $P(x, f(x)) = 0$, $f(0) = 0$ | $F(x,y) = \frac{y^2 P_y(xy, y)}{P(xy, y)} \implies \operatorname{diag}(F) = f$ | $O(d \cdot N)$ via D-finite recurrence | Requires $f(0)=0$ and $P_y(0,0) \neq 0$ (or Puiseux shift first). |
| **1-Branch Kernel Method ($k=1$)** | $K[y, y^{-1}][[x]]$ | Walk on $j \ge 0$, max downward step $-1$ | Substitute unique small root $y_1(x) \in x K[[x]]$ | $O(N)$ or $O(N \log N)$ | Taking the wrong conjugate branch $Y_2(x) \sim 1/x \notin K[[x]]$. |
| **Multi-Branch Kernel Method ($k \ge 2$)** | $K[[x^{1/k}]][y]$ | Walk on $j \ge 0$, downward steps $-1, \dots, -k$ | $\widetilde{K}(x, y_i(x)) = 0$ for $i=1,\dots,k$; $F_0(x) = \frac{(-1)^{k-1}}{w_{-k} x} \prod_{i=1}^k y_i(x)$ | $O(N \log N)$ (or $O(N)$ when $d=1$ via Vieta) | Individual roots $y_i(x)$ are Puiseux series; only symmetric sums lie in $K[[x]]$. |
| **Obstinate Kernel Method (2D Quadrant)** | $K[x, \bar{x}, y, \bar{y}][[t]]$ | 2D walk in $i, j \ge 0$ with small steps | Orbit sum over dihedral group $\langle \Phi, \Psi \rangle$ + $[x^{>0} y^{>0}]$ | $O(N)$ (when $\|G\| < \infty$) | Infinite group $\|G\| = \infty$ yields non-D-finite series (`Bousquet-Mélou & Mishna`). |
| **Multivariate Good–Lagrange Inversion** | $K[[x_1,\dots,x_d]]$ | Coupled system $u_i = x_i \Phi_i(\mathbf{u})$ | $[\mathbf{x}^{\mathbf{n}}] H(\mathbf{u}) = [\mathbf{u}^{\mathbf{n}}] H(\mathbf{u}) \det\!\left(\delta_{i,j} - \frac{u_j}{\Phi_i}\frac{\partial \Phi_i}{\partial u_j}\right) \mathbf{\Phi}^{\mathbf{n}}$ | $O(N \log N)$ (1D/bipartite) or $O(V \log V)$ (multi-D) | Omitting $\det J(\mathbf{u})$ double-counts disconnected directed cycles! |
| **Kinoshita–Li Bivariate Bostan–Mori** | $(K[y]/(y^n))[[x]]$ | Power Projection $[x^{n-1}] g(x) f(x)^i$ | Halve $\deg_x$ and double $\deg_y$ via $Q(x,y)Q(-x,y)$ | $O(n \log^2 n)$ | Requires $[x^0] f(x) = 0$ so $Q_r(0, y) = 1$ at all recursion levels. |

#### Cross-Tradition Comparative Synthesis (`[EN]` vs. `[ZH]` vs. `[JA]`, Cohort 1 Synthesis)

| Dimension | Western Analytic Combinatorics (`[EN]`) | Chinese Competitive Programming (`[ZH]` — `Elegia`, `command_block`) | Japanese Competitive Programming (`[JA]` — `maspypy`, `noshi91`, `Nyaan`) |
| :--- | :--- | :--- | :--- |
| **Diagonal Extraction** | Cauchy contour integrals $\frac{1}{2\pi i} \oint F(z, t/z) \frac{dz}{z}$ and Puiseux residues (Stanley, Flajolet–Sedgewick). | Formal Laurent residue $[z^{-1}]$ paired with algebraic-to-ODE $O(n)$ recurrences (`Elegia`). | Bivariate Bostan–Mori over $\mathbb{F}_p[x,y]$ and Laurent coordinate factoring $(x+x^{-1}+y+y^{-1})^T$ (`maspypy`, `noshi91`). |
| **Kernel Method** | Banderier–Flajolet $k$-root symmetric function theory and Bousquet-Mélou dihedral group orbits. | Concrete problem reductions (reflection principles, Vieta root products, gambler's ruin matrices). | Clean polynomial division and FPS substitution via small-branch fixed points. |
| **Good–Lagrange & Composition** | Gessel's combinatorial cycle-cancellation proof and MacMahon's Master Theorem. | Reverse Lagrange Inversion for graph blocks/bridges (`Luogu P5827`/`P5828`) & placeholder multidimensional FFT (`UOJ 596`). | Kinoshita–Li bivariate Bostan–Mori `PowerProjection` and Bivariate PDE matrix products (`QOJ 6184`). |
```

- **Exact Addition after Line 1072 (Section 6.6 — Blueprint 3 from Cohort 1 §40.5)**:
```markdown

#### Blueprint 3: Reverse Lagrange Inversion Summary for Block-Cut (`Luogu P5827`) & 2-Edge-Connected (`Luogu P5828`) Graphs
Given the rooted connected labeled graph EGF $R(x) = x C'(x)$ where $C(x) = \ln \sum_{k=0}^n 2^{\binom{k}{2}} \frac{x^k}{k!}$, both biconnected and 2-edge-connected labeled graph counts for a fixed $n$ reduce to **a single FPS $\ln$ and $\exp$ in $O(n \log n)$ time** without full compositional inversion:
- **Vertex-Biconnected Graphs ($n \ge 2$, Block-Cut Equation $R(x) = x \exp(B'(R(x)))$)**:
  $$n! [u^n] B(u) = (n - 1)! [u^{n-1}] B'(u) = -(n - 2)! \, [x^{n-1}] \left(\frac{x}{R(x)}\right)^{n-1} = -(n - 2)! \, [x^{n-1}] \exp\!\left(-(n - 1) \ln \frac{R(x)}{x}\right).$$
- **2-Edge-Connected Graphs ($n \ge 1$, Bridge-Tree Equation $R(x) = B_{\bullet}(x e^{R(x)})$ where $B_{\bullet}(u) = u B'(u)$)**:
  $$n! [u^n] B(u) = (n - 1)! [u^n] B_{\bullet}(u) = (n - 1)! \, [x^n] \Big( R(x) \big(1 + x R'(x)\big) \exp\!\big(-n R(x)\big) \Big).$$
```

---

### Restoration 3.4: 3 Additional Rejected Template Problems from Cohort 2 §92.3 (Section 8, Lines 1742–1758)

- **Location**: Append to the table in Section 8 (after Line 1757 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`).
- **Exact Addition after Line 1757**:
```markdown
| 11 | `Library Checker` — **Compositional Inverse of Formal Power Series (Large)** | Cohort 2 | Pure implementation benchmark for Kinoshita–Li $O(N \log^2 N)$ bivariate Bostan–Mori compositional inverse (`compositional_inverse_of_formal_power_series_large`). |
| 12 | `Library Checker` — **Composition of Formal Power Series (Large)** | Cohort 2 | Pure implementation benchmark for $f(g(x)) \bmod x^N$ via transposed bivariate Bostan–Mori (`composition_of_formal_power_series_large`). |
| 13 | `Library Checker` — **Inv of Formal Power Series** | Cohort 2 | Bare univariate polynomial inversion template (`inv_of_formal_power_series`) with zero combinatorial modeling. |
```

---

### Restoration 3.5: 5 Omitted Bibliography Entries from Cohort 1 §40.4 & Cohort 2 §92.4 (Section 9, Lines 1761–1782)

- **Location**: Section 9 of `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.
- **Exact Additions**:
  - Append to **Section 9.1 (`[EN]`)** after Line 1772:
```markdown
10. **`[EN]` Hautus & Klarner (1971)** — M. L. J. Hautus and D. A. Klarner, *"The diagonal of a double power series"*, Duke Mathematical Journal **38**(2), 229–235 (1971). Gives the constructive contour and formal residue derivation of Furstenberg's diagonal in characteristic $0$ by separating small roots ($z_i(t) \to 0$) from large roots ($z_j(t) \not\to 0$) of $z Q(z, t/z) = 0$.
11. **`[EN]` Pemantle & Wilson (2013)** — R. Pemantle and M. C. Wilson, *Analytic Combinatorics in Several Variables*, Cambridge University Press (2013). Modern multivariate asymptotic and residue theory for rational and algebraic generating functions.
12. **`[EN]` Bostan, Lairez, & Salvy (2017)** — A. Bostan, P. Lairez, and B. Salvy, *"Multiple binomial sums"*, Journal of Symbolic Computation **80**, 351–386 (2017). Proves that every multiple binomial sum is the diagonal of a rational function and analyzes creative telescoping / D-finite differential equations for diagonals.
```
  - Append to **Section 9.3 (`[JA]`)** after Line 1781:
```markdown
15. **`[JA]` Nyaan (2021)** — *"AtCoder ABC 222 H - Beautiful Binary Tree Official Editorial"* ([https://atcoder.jp/contests/abc222/editorial/2742](https://atcoder.jp/contests/abc222/editorial/2742)). Complete pedagogical derivation of coupled tree DP ($B = 2A + A^2, A = x(1+A+B)^2$), Lagrange inversion, and the $O(N)$ D-finite ODE recurrence $T U' = m T' U$.
16. **`[JA]` Rice_tawara459 (`trap.jp`, 2026)** — *"ラグランジュ反転公式の組合せ論からの導出 (Combinatorial Derivation of the Lagrange Inversion Formula)"*, Tokyo Tech Digital Creation Circle traP ([https://trap.jp/post/2934/](https://trap.jp/post/2934/)). Derives Lagrange Inversion and tree enumeration via Łukasiewicz paths and Raney's cyclic shift lemma, with a complete combinatorial walkthrough of `AtCoder ABC 222 H`.
```

---

## Part 4: Editorial, Delimiter & Pedagogical Polish

1. **Banned Math Delimiter Substrings (`\\[4pt]` and `\\[6pt]`)**:
   - **Line 492**: Replace `\\[4pt]` with `\\` (already included in Bug 1.1 replacement above).
   - **Line 564**: Replace `x F_0(x) + x y_1(x) F_1(x) = y_1(x)^2, \\[4pt]` with `x F_0(x) + x y_1(x) F_1(x) = y_1(x)^2, \\`.
   - **Line 746**: Replace `\\[6pt]` inside `\begin{pmatrix} ... \end{pmatrix}` with `\\`.

2. **Conversational Artifacts (`"Wait:"` / `"? "` in Main Text & Problem Derivations)**:
   - **Line 107**: Replace `Wait: the denominator $P(x y, y)$ has an overall factor of $y$` with `Notice that the denominator $P(x y, y)$ has an overall factor of $y$`.
   - **Line 123**: Replace `(Wait — how is $\frac{y^2}{y - f(t)}$ expanded in $K((y))[[t]]$? Since $f(0) = 0$ and $f(t) = O(t)$, we factor out $y$ from the denominator!)` with `(Since $f(0) = 0$ and $f(t) = O(t)$, we expand $\frac{y^2}{y - f(t)}$ in $K((y))[[t]]$ by factoring $y$ out of the denominator:)`.
   - **Lines 1239–1241 (Problem 8, `CF 1109D`)**: Replace the conversational question marks on Lines 1239 and 1241 with:
```markdown
     Since the $s = k + 1$ roots are already specified and ordered along the path from $a$ to $b$:
     - Choose and order the $k - 1$ internal vertices on the $a$–$b$ path: $\binom{n - 2}{k - 1} (k - 1)! = \frac{(n - 2)!}{(n - k - 1)!}$.
     - Count labeled forests on the $n$ vertices rooted at those $s = k + 1$ specified vertices: $(n - s)! [x^{n-s}] e^{n x} \cdot \dots = (k + 1) n^{n - k - 2}$ by Cayley's forest formula (for $k < n - 1$, and $1$ when $k = n - 1$).
```
   - **Line 1530 (Problem 22, `CF 1479E`)**: Replace `- With probability $\frac{1}{2} \frac{N - s}{N} \frac{s}{N - 1}$? Actually, with probability $\frac{s}{2N}$ it loses a member without replacement, and with probability $\frac{N - s}{2N} \frac{s}{N}$ it gains a member, leading to the second-order difference equation:` with `- In a single step, a club of size $s$ either loses a chosen member or gains a member from the remaining $N - s$ students with probability proportional to $s / N$, yielding the second-order difference equation:`.
   - **Line 1599 (Problem 26, `CF 1349F2`)**: Replace `(every occurrence of $k$ is preceded by at least one $k - 1$? More precisely, every $k > 1$ appearing in $a$ appears at least once after the first occurrence of $k - 1$)` with `(every occurrence of $k > 1$ in $a$ appears strictly before the last occurrence of $k - 1$, or equivalently in the reversed sequence every $k > 1$ is preceded by $k - 1$)`.

3. **Expanded Explicit Derivations for Problems 18, 24, 32, and 33**:
   - **Problem 24 (`LibreOJ 6728`, Lines 1565–1569)**: Explicitly write out the 2-layer exponential/ordinary tree composition reduction $u(x) = x \Psi(u(x))$, apply Form 2 of Lagrange Inversion $[x^n] H(u(x)) = [u^n] H(u)\left(1 - \frac{u \Psi'(u)}{\Psi(u)}\right) \Psi(u)^n$, and apply the logarithmic derivative identity $T(u) U'(u) = n T'(u) U(u)$ (`poly_pow_ode`) to extract $[u^n]$ in $O(n)$ time.
   - **Problem 32 (`LibreOJ 3398`, Lines 1719–1722)**: Explicitly show how after expanding the $2 \times 2$ Good–Lagrange determinant $\det J(u_1, u_2) = \left(1 - \frac{u_1 \partial_{u_1}\Phi_1}{\Phi_1}\right)\left(1 - \frac{u_2 \partial_{u_2}\Phi_2}{\Phi_2}\right) - \frac{u_1 u_2 (\partial_{u_2}\Phi_1)(\partial_{u_1}\Phi_2)}{\Phi_1 \Phi_2}$, eliminating $u_2$ reduces the inner extraction to a linear combination of $[u_1^{n_1}] G(u_1) F(u_1)^k$, which is solved in $O(n \log^2 n)$ via Kinoshita–Li `PowerProjection` (`Blueprint 2`).
   - **Problem 33 (`AtCoder ARC 145 F`, Lines 1735–1739)**: Explicitly write the root-of-unity filter $\text{Ans}_r = \frac{1}{M} \sum_{j=0}^{M-1} \zeta_M^{-jr} [x^N] F(x, \zeta_M^j)$, group by $d = \frac{M}{\gcd(j, M)}$ so that $\prod_{k=0}^{d-1} (1 + x \zeta_d^k \dots) = (1 \pm x^d \dots)$, and note that since each divisor $d \mid M$ only involves powers of $x^d$, the polynomial operations at divisor $d$ have degree $\lfloor N / d \rfloor$, summing to $\sum_{d \mid M} O((N/d) \log(N/d)) = O(N \log^2 N)$ total time.
