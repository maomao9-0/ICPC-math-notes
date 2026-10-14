# Audit Report B (Independent Second-Pass): Wave 4B — Furstenberg's Theorem, The Kernel Method, and Good–Lagrange Multivariate Inversion

**Target File**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4b_furstenberg_kernel_good_lagrange.md` (1,782 lines)
**Source Files Cross-Checked**:
1. `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_36_to_40_furstenberg_kernel_good_lagrange.md` (Cohort 1, 1,335 lines)
2. `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_88_to_92_furstenberg_kernel_good_lagrange.md` (Cohort 2, 1,454 lines)
**Prior Audit Reviewed & Cross-Checked**:
3. `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/audit/audit_A_wave_4b.md` (Inspector A Report, 425 lines)

**Auditor**: Inspector B (Principal Mathematical & Pedagogical Auditor)
**Audit Status**: **REMEDIATION REQUIRED** — 9 mathematical/algebraic/editorial defect groups identified in `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`, plus **6 critical mathematical/line-number errors in Inspector A's proposed fixes (`audit_A_wave_4b.md`)** that MUST NOT be applied as written.

---

## Executive Summary

1. **Zero Information Loss Check**:
   - All 6 major sections, all 6 C++17 reference implementations (`Furstenberg`, `KernelMethod`, `BivariateDFinite`, `GoodLagrange`, `MacMahonMaster`, `PRecursiveRootFinder`), all characteristic-$p$ warnings, all complexity tables, all 30 accepted problems (Problems 1–30), and all 23 rejected template problems from Cohort 1 (`iter_36_to_40`) and Cohort 2 (`cohort2_iter_88_to_92`) are present in `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.
2. **Critical Alert on Inspector A's Report (`audit_A_wave_4b.md`)**:
   - Before applying any remediation to `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`, **DO NOT blindly apply `audit_A_wave_4b.md`**. Our independent Python verification and line-by-line cross-check revealed that `audit_A_wave_4b.md` contains **wrong line numbers, mismatched problem numbers, and three mathematically false replacement formulas**:
     1. **Inspector A Fix 2.1 (`audit_A_wave_4b.md` Lines 212–237)**: Cites *"Problem 1 (`AtCoder ABC 205 E`), Lines 1102–1107"*. In reality, Lines 1086–1105 of `cohort3_wave_4b` are **Problem 1 (`AtCoder ARC 012 D — Don't Step on the Threshold!`)**, whereas `AtCoder ABC 205 E` is in the **Rejected Table (Line 1755)**. Applying Fix 2.1 would overwrite the derivation of `ARC 012 D` with Catalan path reflection!
     2. **Inspector A Bug 1.5 (`audit_A_wave_4b.md` Lines 154–207)**: Cites *"Problem 15 (`AtCoder AGC 058 D — Yet Another ABC String`), Lines 1375–1382"*. In reality, Lines 1375–1393 are **Problem 15 (`HDU 4656 / LOJ 6570 — Fun with Sequences`)**, whereas `AtCoder AGC 058 D` is **Problem 27 (Lines 1614–1632)**. Even worse, Inspector A's proposed replacement formula using $(-3)^k \left[\binom{N-2k}{k} - \binom{N-2k-1}{k-1}\right]$ is **mathematically wrong**: for $(A,B,C) = (2,1,1)$ it gives $6$ instead of the true count $7$, and for $(A,B,C) = (2,2,1)$ it gives $12$ instead of $16$! (See **Bug B.5** below for the exact Python-verified derivation and formula.)
     3. **Inspector A Bug 1.1 (`audit_A_wave_4b.md` Lines 18–57)**: Cites *"Section 3.5, Lines 357–362 (and Problem 25, Lines 1554–1557)"* (actual lines are **Extension 2.4B, Lines 251–271** and **Problem 25, Lines 1572–1588**), and proposes replacing the general $(p, q)$-diagonal with $[s^n] \frac{1}{1-(p+q)u(s)} = \binom{(p+q)n}{pn}$ where $u(s) = s(1-u)^{-(p+q)}$. That formula is **mathematically false for $p > 1, q > 1$**: by Lagrange Inversion, $[s^n] \frac{1}{1-(p+q)u(s)} = \binom{(p+q)n}{n} \neq \binom{(p+q)n}{pn}$ (e.g., for $p=2, q=3, n=1$, it yields $\binom{5}{1} = 5 \neq \binom{5}{2} = 10$). (See **Bug B.1** below for the exact multi-branch residue and $q=1$ specialization.)
     4. **Inspector A Bug 1.3 (`audit_A_wave_4b.md` Lines 85–116)**: Cites *"Section 5.4, Lines 763–774"* and replaces the trace table with unrooted counts $t_{n_1,n_2}$, **missing the actual algebraic bug on Line 761** where `cohort3_wave_4b` writes $T_{n, m} = n! m! \cdot \frac{1}{n} \frac{m^{n-1}}{(n-1)!} \frac{n^m}{m!} = n^{m-1} m^{n-1}$ (which is algebraically $n^m m^{n-1}$, not $n^{m-1} m^{n-1}$!) and writes false equalities $2 = 2^0 1^1$ and $8 = 2^1 2^1$ in the table on Lines 764–769. (See **Bug B.3** below.)
     5. **Inspector A Bug 1.4 (`audit_A_wave_4b.md` Lines 119–151)**: In attempting to remove `"Wait"` artifacts from Dixon's Identity (Lines 808–835), Inspector A's replacement text (`audit_A_wave_4b.md` Line 132) **introduces a brand-new `"Wait —"` conversational artifact**! (See **Bug B.4** below for a clean, zero-hesitation derivation.)
     6. **Inspector A Fix 2.2 (`audit_A_wave_4b.md` Lines 240–279)**: Cites *"Problem 22 (`Codeforces 1479E`), Lines 1488–1495"* (actual lines: **Lines 1517–1535**), and writes $(N-s)g(s) - (2N-s)g(s-1) = -2N$ and $g(s) = -2N \prod_{j=1}^s \frac{2N-j}{N-j}$ with $f(0) = f(1) = 0$. This is **off by a factor of $N$, contradicts $g(0) = f(1) - f(0) = 0$, and produces negative expected values**! (See **Bug B.7** below for the exact Python-verified recurrence and sign convention.)

This report (**Audit Report B**) supersedes `audit_A_wave_4b.md` and provides 100% self-contained, Python-verified, exact line-number replacements for every issue in `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`.

---

## Part 1: Mathematical & Algebraic Bugs (Verified via Python)

### Bug B.1 — Extension 2.4B (Lines 251–271) & Problem 25 (Lines 1572–1588): Asymmetric $(p, q)$-Diagonal Coprimality Condition, Multi-Branch Residue vs. $q=1$ Specialization, and Sign Error in Problem 25

- **Location 1**: Section 2.4, Extension 2.4B (`Asymmetric (p, q)-Diagonals via Furstenberg`), **Lines 251–271**.
- **Location 2**: Section 7, Problem 25 (`Asymmetric Lattice Diagonal — Custom / Generalized Delannoy`), **Lines 1572–1588**.
- **Diagnosis**:
  1. On **Line 255–257**, `cohort3_wave_4b` substitutes $x = z^q$ and $y = t z^{-p}$ so that $x^a y^b = z^{qa - pb} t^b$. For $qa - pb = 0$ to hold if and only if $(a, b) = (pn, qn)$ for $n \ge 0$, we **must require $\gcd(p, q) = 1$** (otherwise if $\gcd(p, q) = g > 1$, the substitution extracts $(p'n, q'n)$ where $p' = p/g, q' = q/g$).
  2. Furthermore, on **Line 257**, the extracted series in $t$ has terms $f_{pn, qn} t^{qn}$ (a series in $s = t^q$). If we instead substitute $x = z^q, y = s z^{-p}$ or symmetrically extract $[z^0] F(z^q, s^{1/q} z^{-p})$, we should be completely explicit about the power $t^{qn}$ vs $s^n$. Even better: for the rational example $F(x, y) = \frac{1}{1 - x - y}$ on **Lines 261–270**, when $q > 1$, the denominator $z^p(1 - z^q) - t = 0$ has $p$ small roots $z_1(t), \dots, z_p(t) \to 0$ and $q$ large roots near the $q$-th roots of unity $\zeta_q^j$. Summing the residues over the $p$ small roots (or minus the residues at the $q$ large roots) yields:
     $$D_{p, q}(t) = \sum_{i=1}^p \frac{1}{p - (p+q) z_i(t)^q} = \sum_{n=0}^{\infty} \binom{(p+q)n}{pn} t^{qn}.$$
     When $q = 1$ (the $(p, 1)$-diagonal, as in **Problem 25**), there is a **single** large root $z_{\text{large}}(t) = 1 - w(t)$ satisfying $z^p(1 - z) = t \iff w = t(1 - w)^{-p}$ with $w(0) = 0$.
  3. **Sign Bug in Problem 25 (Line 1586)**: Let us compute $-\operatorname{Res}_{z = 1 - w(t)} \frac{z^{p - 1 - a}}{z^p - z^{p+1} - t}$ for $q = 1$:
     $$\frac{\partial}{\partial z}(z^p - z^{p+1} - t)\Big|_{z = 1 - w} = p z^{p-1} - (p+1) z^p = z^{p-1}\big(p - (p+1)(1 - w)\big) = z^{p-1}\big((p+1)w - 1\big).$$
     Because the residue inside the contour is the sum over the $p$ small roots, which by the Residue Theorem on $\mathbb{P}^1(\mathbb{C})$ equals **minus** the residue at the single large root $z_{\text{large}}(t) = 1 - w(t)$ (for $a \ge 0$, the residue at $z = \infty$ vanishes since $\deg(\text{num}) = p - 1 - a \le p - 1 \le \deg(\text{den}) - 2 = p - 1$), we obtain:
     $$D_{p, 1}^{(a)}(t) = -\operatorname{Res}_{z = 1 - w(t)} \frac{z^{p - 1 - a}}{z^p - z^{p+1} - t} = -\frac{(1 - w(t))^{-a}}{(p + 1) w(t) - 1} = \frac{(1 - w(t))^{-a}}{1 - (p + 1) w(t)}.$$
     On **Line 1586**, `cohort3_wave_4b` forgot the minus sign from the exterior residue and wrote $\frac{(1 - w(t))^{-a}}{(p + 1) w(t) - 1}$, which evaluates to **$-1$ instead of $+1$** at $t = 0$ ($w = 0$)!
- **Drop-In Replacement for Location 1 (Lines 251–271)**:
  Replace Lines 251–271 with:
```markdown
### Extension 2.4B: Asymmetric $(p, q)$-Diagonals via Furstenberg

For an asymmetric diagonal $\sum_{n \ge 0} f_{pn, qn} s^n$ where $p, q \in \mathbb{Z}_{\ge 1}$ are coprime ($\gcd(p, q) = 1$), we reduce to a constant-term extraction by balancing the exponents of $z$:

$$\text{Substitute } x = z^q, \quad y = t z^{-p} \quad (\gcd(p, q) = 1).$$

Then $x^a y^b = z^{qa - pb} t^b$. Since $\gcd(p, q) = 1$, the exponent of $z$ vanishes ($qa - pb = 0$) if and only if $(a, b) = (pn, qn)$ for some integer $n \ge 0$, in which case $t^b = t^{qn}$. Setting $s = t^q$, we obtain:

$$D_{p, q}(t) = [z^0] F(z^q, t z^{-p}) = \sum_{n=0}^{\infty} f_{pn, qn} t^{qn}.$$

By Cauchy's integral theorem, this constant term is the contour integral:

$$D_{p, q}(t) = \frac{1}{2\pi i} \oint_{|z| = r} F(z^q, t z^{-p}) \frac{dz}{z}.$$

For example, when $F(x, y) = \frac{1}{1 - x - y}$, we have $f_{a, b} = \binom{a+b}{a}$, and the integrand is:

$$\frac{1}{z(1 - z^q - t z^{-p})} = \frac{z^{p-1}}{z^p - z^{p+q} - t}.$$

As $t \to 0$, the denominator $Q(z, t) = z^p(1 - z^q) - t$ has $p$ small roots $z_1(t), \dots, z_p(t) = O(t^{1/p})$ inside the contour $|z| = r$ and $q$ large roots near the $q$-th roots of unity outside the contour. Summing the residues at the $p$ small roots yields:

$$D_{p, q}(t) = \sum_{i=1}^{p} \operatorname{Res}_{z = z_i(t)} \frac{z^{p-1}}{z^p - z^{p+q} - t} = \sum_{i=1}^{p} \frac{z_i(t)^{p-1}}{p z_i(t)^{p-1} - (p+q) z_i(t)^{p+q-1}} = \sum_{i=1}^{p} \frac{1}{p - (p+q) z_i(t)^q} = \sum_{n=0}^{\infty} \binom{(p+q)n}{pn} t^{qn}.$$

In the crucial special case $q = 1$ (the $(p, 1)$-diagonal $\sum_{n \ge 0} \binom{(p+1)n}{pn} t^n$), there is only a **single** large root $z_{\text{large}}(t) = 1 - w(t)$ outside the contour, where $w(t) = O(t)$ satisfies $(1 - w)^p w = t \iff w = t(1 - w)^{-p}$. Since the rational 1-form $\frac{z^{p-1} dz}{z^p - z^{p+1} - t}$ is regular at $z = \infty$ (the numerator has degree $p - 1 \le (p + 1) - 2$), the sum of residues at the $p$ small roots inside $|z| = r$ equals **minus** the single residue at $z_{\text{large}}(t) = 1 - w(t)$:

$$D_{p, 1}(t) = -\operatorname{Res}_{z = 1 - w(t)} \frac{z^{p-1}}{z^p - z^{p+1} - t} = -\frac{(1 - w)^{p-1}}{p(1 - w)^{p-1} - (p+1)(1 - w)^p} = \frac{1}{1 - (p+1) w(t)}, \quad w(t) = t(1 - w(t))^{-p}.$$
```
- **Drop-In Replacement for Location 2 (Problem 25, Lines 1572–1588)**:
  Replace Lines 1572–1588 with:
```markdown
### Problem 25: Asymmetric Lattice Diagonal — Custom / Generalized Delannoy
- **Source**: Classical / Pólya–Furstenberg Benchmark
- **URL**: https://judge.yosupo.jp/problem/polynomial_root_finding
- **Problem Statement**: Given integers $p \ge 1, a \ge 0$, and $N \le 2 \cdot 10^5$, compute $d_n = [x^{pn + a} y^n] \frac{1}{1 - x - y} = \binom{(p+1)n + a}{n}$ for all $0 \le n \le N \pmod{998244353}$ using Furstenberg's residue method and compare with Generalized Binomial Series $\mathcal{B}_{p+1}(t)^a$.
- **Hints**:
  - *Hint 1 (Diagnostic)*: To align $(pn + a, n)$ onto the constant term, extract $[z^0] z^{-a} F(z, t z^{-p})$.
  - *Hint 2 (Structural)*: Write the integrand as $\frac{z^{p - 1 - a}}{z^p - z^{p+1} - t}$. Instead of summing over the $p$ small roots $z_i \sim t^{1/p}$, use the Residue Theorem at infinity to express the contour integral via the single large root $z_{\text{large}}(t) = 1 - w(t) \to 1$.
  - *Hint 3 (Algorithmic)*: Show that $w(t) = t(1 - w(t))^{-p}$ and apply Lagrange Inversion.
- **Full Mathematical Derivation & Solution**:
  1. **Furstenberg Substitution**:
     $$[x^{pn + a} y^n] \frac{1}{1 - x - y} = [z^0 t^n] \frac{z^{-a}}{1 - z - t z^{-p}} = [t^n] \frac{1}{2\pi i} \oint_{|z| = r} \frac{z^{p - 1 - a}}{z^p - z^{p + 1} - t} \, dz.$$
  2. **Exterior Residue at $z_{\text{large}} = 1 - w(t)$**:
     As $t \to 0$, $z^p(1 - z) - t = 0$ has $p$ small roots inside $|z| = r$ and one root $z_{\text{large}}(t) = 1 - w(t)$ near $1$ outside $|z| = r$, where $(1 - w)^p w = t \iff w = t(1 - w)^{-p}$. For $a \ge 0$, the integrand behaves as $O(z^{-2-a})$ as $z \to \infty$, so its residue at $z = \infty$ is $0$. By the Residue Theorem on $\mathbb{P}^1(\mathbb{C})$, the sum of the $p$ interior residues equals **minus** the exterior residue at $z = 1 - w(t)$:
     $$D_{p, 1}^{(a)}(t) = -\operatorname{Res}_{z = 1 - w(t)} \frac{z^{p - 1 - a}}{z^p - z^{p + 1} - t} = -\frac{(1 - w)^{-a}}{p(1 - w)^{p-1} - (p+1)(1 - w)^p \cdot (1 - w)^{1-p}} = -\frac{(1 - w(t))^{-a}}{(p + 1) w(t) - 1} = \frac{(1 - w(t))^{-a}}{1 - (p + 1) w(t)}.$$
  3. **Lagrange Inversion Check**: With $w = t \phi(w)$ where $\phi(w) = (1 - w)^{-p}$, we have $1 - t \phi'(w) = 1 - \frac{w}{\phi(w)} p(1 - w)^{-p-1} = \frac{1 - (p + 1)w}{1 - w}$. Thus $\frac{(1 - w)^{-a}}{1 - (p + 1)w} = \frac{(1 - w)^{-a - 1}}{1 - t \phi'(w)}$, whose $[t^n]$ coefficient by Variant B of LIF is $[w^n] (1 - w)^{-a - 1} (1 - w)^{-pn} = \binom{(p + 1)n + a}{n}$. Complexity: $O(N)$ with precomputed factorials or $O(N \log N)$ via FPS Newton iteration.
```

---

### Bug B.2 — Section 4.4 (Worked Example 4.3: Quarter-Plane Tandem/Kreweras Walk, Lines 656–668): Conversational `"Wait:"` Artifact & Incomplete Positive-Part Extraction

- **Location**: Section 4.4, Worked Example 4.3 (`Quarter-Plane Walk and the Algebraic Group of the Kernel (Tandem / Kreweras Walk)`), **Lines 656–668**.
- **Diagnosis**:
  - Line 662 contains a conversational self-correction (`"Wait: on the LHS, look at the 6 terms..."`) and hand-waves how the positive-part extraction $[x^{>0} y^{>0}]$ leads to Kreweras' closed-form formula $Q_{0,0}(3m) = \frac{4^m}{(m+1)(2m+1)} \binom{3m}{m}$.
- **Drop-In Replacement for Lines 656–668**:
  Replace Lines 656–668 with:
```markdown
**Step 3 (Alternating Orbit Sum & Extraction of Kreweras' Formula)**:
Writing the kernel equation as $x y K(x, y; t) Q(x, y; t) = x y + R(x; t) + S(y; t)$ where $R(x; t) = t x Q(x, 0; t) - t Q(0, 0; t)$ depends only on $x$ and $S(y; t) = t y Q(0, y; t)$ depends only on $y$, we can eliminate $S(y; t)$ using the two roots $Y_1(x; t), Y_2(x; t)$ of the quadratic kernel $y K(x, y; t) = t y^2 - (1 - t x^{-1}) y + t x = 0$:
1. Let $Y_0(x; t) = \frac{1 - t x^{-1} - \sqrt{(1 - t x^{-1})^2 - 4 t^2 x}}{2t} = t x + t^2 + O(t^3)$ be the unique small branch in $\mathbb{Q}[x, x^{-1}][[t]]$.
2. Because the involution $\iota_x(x, y) = (\frac{1}{x y}, y)$ fixes $y = Y_0(x; t)$ while mapping $x \mapsto X_0(x; t) = \frac{1}{x Y_0(x; t)}$, setting $y = Y_0(x; t)$ in the kernel equation at both $(x, Y_0)$ and $(X_0, Y_0)$ and subtracting eliminates $S(Y_0(x; t))$:

$$R(x; t) - R(X_0(x; t); t) = X_0(x; t) Y_0(x; t) - x Y_0(x; t) = \frac{1}{x} - x Y_0(x; t).$$

3. Expanding this functional equation via the symmetric function $W(x; t) = Y_0(x; t) + X_0(x; t)^{-1}$ (Bousquet-Mélou 2005) and extracting the constant term $[x^0] R(x; t) = -t Q(0, 0; t)$ via Lagrange Inversion yields Kreweras' celebrated closed form for excursions returning to $(0, 0)$ (which requires $n = 3m$ steps):

$$Q_{0, 0}(3m) = [t^{3m}] Q(0, 0; t) = \frac{4^m}{(m + 1)(2m + 1)} \binom{3m}{m}.$$

For $m = 0, 1, 2, 3$:
- $m = 0$ ($n = 0$): $\frac{1}{1 \cdot 1} \binom{0}{0} = 1$.
- $m = 1$ ($n = 3$): $\frac{4}{2 \cdot 3} \binom{3}{1} = \mathbf{2}$ (the two excursions $(+1,0) \to (0,+1) \to (-1,-1)$ and $(0,+1) \to (+1,0) \to (-1,-1)$).
- $m = 2$ ($n = 6$): $\frac{16}{3 \cdot 5} \binom{6}{2} = \mathbf{16}$.
- $m = 3$ ($n = 9$): $\frac{64}{4 \cdot 7} \binom{9}{3} = \mathbf{192}$.
```

---

### Bug B.3 — Section 5.4 (Worked Example 5.1: Bipartite Labeled Trees, Lines 755–770): Good–Lagrange Exponent Error ($[u_1^{n-1} u_2^{m-1}]$ vs $[u_1^{n-1} u_2^m]$), Algebraic Exponent Error ($n^{m-1} m^{n-1}$ vs $n^m m^{n-1}$), & False Equalities in Trace Table

- **Location**: Section 5.4, Worked Example 5.1 (`Bipartite Labeled Trees via 2D Good–Lagrange`), **Lines 755–770**.
- **Diagnosis**:
  1. **Good–Lagrange Exponent Error on Line 756**: In Theorem 5.1 (Line 707), with $H(u_1, u_2) = u_1$, the right-hand side extracts $[u_1^n u_2^m] \big(u_1 (1 - u_1 u_2) e^{n u_2 + m u_1}\big) = [u_1^{n-1} u_2^m] \big((1 - u_1 u_2) e^{n u_2 + m u_1}\big)$. Notice that the factor $u_1$ shifts the exponent of $u_1$ from $n$ to $n - 1$, while the exponent of $u_2$ stays **$m$**! On **Line 756**, `cohort3_wave_4b` erroneously wrote $[u_1^{n-1} u_2^{m-1}]$, and in the trace table on **Lines 764–769**, it extracted $[u_1^{n-1} u_2^{m-1}]$ and pretended the $-u_1 u_2$ term contributed $0$ even for $(n, m) = (2, 2)$!
     With the correct exponent $[u_1^{n-1} u_2^m]$:
     $$[u_1^{n-1} u_2^m] \big((1 - u_1 u_2) e^{n u_2 + m u_1}\big) = \frac{m^{n-1}}{(n-1)!} \frac{n^m}{m!} - \frac{m^{n-2}}{(n-2)!} \frac{n^{m-1}}{(m-1)!} = \left(1 - \frac{n-1}{n}\right) \frac{m^{n-1}}{(n-1)!} \frac{n^m}{m!} = \frac{1}{n} \frac{m^{n-1}}{(n-1)!} \frac{n^m}{m!}.$$
  2. **Algebraic Exponent Error on Line 761**: On **Line 761**, `cohort3_wave_4b` computes the number of **white-rooted** bipartite labeled trees $T_{n, m} = n! m! [x^n y^m] u(x, y)$ as:
     $$T_{n, m} = n! m! [x^n y^m] u(x, y) = n! m! \cdot \frac{1}{n} \frac{m^{n-1}}{(n-1)!} \frac{n^m}{m!} = n^{m-1} m^{n-1}.$$
     Look at the algebra: $\frac{n!}{n (n-1)!} = 1$ and $\frac{m!}{m!} = 1$, so the product is **$n^m m^{n-1}$**, **NOT** $n^{m-1} m^{n-1}$! Because $u(x, y) = x e^{y e^u}$ is rooted at one of the $n$ white vertices, the white-rooted count is $T_{n, m} = n^m m^{n-1}$, and dividing by $n$ gives the **unrooted** bipartite labeled tree count $t_{n, m} = \frac{1}{n} T_{n, m} = n^{m-1} m^{n-1}$.
  3. **False Equalities in the Trace Table (Lines 768–769)**:
     - Line 768 (Row $(2, 1)$): `$2! 1! (1) = \mathbf{2} = 2^0 1^1$` — False ($2^0 1^1 = 1 \neq 2$).
     - Line 769 (Row $(2, 2)$): `$2! 2! (2) = \mathbf{8} = 2^1 2^1$` — False ($2^1 2^1 = 4 \neq 8$).

- **Drop-In Replacement for Lines 755–770**:
  Replace Lines 755–770 with:
```markdown
**Step 3 (Coefficient Extraction for $H(u_1, u_2) = u_1$)**:
Applying Theorem 5.1 with $H(u_1, u_2) = u_1$, the factor $u_1$ shifts the extracted power of $u_1$ from $n$ to $n - 1$ while the power of $u_2$ remains $m$:

$$\begin{aligned}
[x^n y^m] u(x, y) &= [u_1^n u_2^m] \Big( u_1 (1 - u_1 u_2) e^{n u_2} e^{m u_1} \Big) = [u_1^{n-1} u_2^m] \Big( (1 - u_1 u_2) e^{n u_2 + m u_1} \Big) \\
&= [u_1^{n-1} u_2^m] e^{n u_2 + m u_1} - [u_1^{n-2} u_2^{m-1}] e^{n u_2 + m u_1} \\
&= \frac{m^{n-1}}{(n-1)!} \frac{n^m}{m!} - \frac{m^{n-2}}{(n-2)!} \frac{n^{m-1}}{(m-1)!} = \left(1 - \frac{n-1}{n}\right) \frac{m^{n-1}}{(n-1)!} \frac{n^m}{m!} = \frac{1}{n} \frac{m^{n-1}}{(n-1)!} \frac{n^m}{m!}.
\end{aligned}$$

Since $u(x, y)$ is the EGF of bipartite labeled trees **rooted at one of the $n$ white vertices**, multiplying by $n! m!$ gives the white-rooted count $T_{n, m}$, and dividing by $n$ gives the **unrooted** spanning tree count $t_{n, m}$ of $K_{n, m}$:

$$T_{n, m} = n! m! [x^n y^m] u(x, y) = n! m! \cdot \frac{1}{n} \frac{m^{n-1}}{(n-1)!} \frac{n^m}{m!} = n^m m^{n-1}, \qquad t_{n, m} = \frac{T_{n, m}}{n} = n^{m-1} m^{n-1}.$$

**Small-$(n, m)$ Trace Verification**:
| $(n, m)$ | $\Delta(u_1, u_2) \phi_1^n \phi_2^m$ | $[u_1^{n-1} u_2^m] \big((1 - u_1 u_2) e^{n u_2 + m u_1}\big)$ | $[x^n y^m] u(x, y)$ | White-Rooted $T_{n,m} = n^m m^{n-1}$ | Unrooted $t_{n,m} = n^{m-1} m^{n-1}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $(1, 1)$ | $(1 - u_1 u_2) e^{u_2 + u_1}$ | $\frac{1^0}{0!}\frac{1^1}{1!} - 0 = 1 - 0 = 1$ | $1$ | $1! 1! (1) = \mathbf{1} = 1^1 1^0$ | $\mathbf{1} = 1^0 1^0$ |
| $(1, 2)$ | $(1 - u_1 u_2) e^{2u_2 + u_1}$ | $\frac{2^0}{0!}\frac{1^2}{2!} - 0 = \frac{1}{2} - 0 = \frac{1}{2}$ | $\frac{1}{2}$ | $1! 2! (\frac{1}{2}) = \mathbf{1} = 1^2 2^0$ | $\mathbf{1} = 1^1 2^0$ |
| $(2, 1)$ | $(1 - u_1 u_2) e^{u_2 + 2u_1}$ | $\frac{1^1}{1!}\frac{2^1}{1!} - \frac{1^0}{0!}\frac{2^0}{0!} = 2 - 1 = 1$ | $1$ | $2! 1! (1) = \mathbf{2} = 2^1 1^1$ | $\mathbf{1} = 2^0 1^1$ |
| $(2, 2)$ | $(1 - u_1 u_2) e^{2u_2 + 2u_1}$ | $\frac{2^1}{1!}\frac{2^2}{2!} - \frac{2^0}{0!}\frac{2^1}{1!} = 4 - 2 = 2$ | $2$ | $2! 2! (2) = \mathbf{8} = 2^2 2^1$ | $\mathbf{4} = 2^1 2^1$ |
```

---

### Bug B.4 — Section 5.6 (Worked Example 5.3: Dixon's Binomial Identity via MacMahon's Master Theorem, Lines 808–835): Three Conversational `"Wait"` False Starts

- **Location**: Section 5.6, Worked Example 5.3 (`Dixon's Binomial Identity via MacMahon's Master Theorem`), **Lines 808–835**.
- **Diagnosis**:
  - Lines 815, 819, and 822 contain three conversational false starts (`"Wait: if we choose..."`, `"Wait: for the binomial coefficients to match..."`, `"Wait — why is the exponent..."`).
  - As noted in the Executive Summary, Inspector A's proposed replacement (`audit_A_wave_4b.md` Line 132) accidentally introduced a new `"Wait —"`!
  - By choosing the index $k$ directly in the expansion of $(u_1 - u_2)^{a+b}$ as the term $\binom{a+b}{a+k} u_1^{b-k} (-u_2)^{a+k}$, the exponents required from $(u_2 - u_3)^{b+c}$ and $(u_3 - u_1)^{c+a}$ are immediately forced to be $u_2^{c-k} (-u_3)^{b+k}$ and $u_3^{a-k} (-u_1)^{c+k}$, yielding Dixon's identity in one clean step with zero index re-parameterizations and zero `"Wait"`s.
- **Drop-In Replacement for Lines 808–835**:
  Replace Lines 808–835 with:
```markdown
### Worked Example 5.3: Dixon's Binomial Identity via MacMahon's Master Theorem

**Problem**: Prove Dixon's Identity for non-negative integers $a, b, c$:

$$\sum_{k = -\infty}^{\infty} (-1)^k \binom{a+b}{a+k} \binom{b+c}{b+k} \binom{c+a}{c+k} = \frac{(a+b+c)!}{a! \, b! \, c!}.$$

**Step 1 (Encoding the Alternating Product as a Matrix System)**:
Consider the product of three linear forms:

$$P(u_1, u_2, u_3) = (u_2 - u_3)^{b+c} (u_3 - u_1)^{c+a} (u_1 - u_2)^{a+b},$$

and extract the coefficient $[u_1^{b+c} u_2^{c+a} u_3^{a+b}] P(u_1, u_2, u_3)$.
In the factor $(u_1 - u_2)^{a+b}$, index each term by $k \in \mathbb{Z}$ by choosing $b - k$ copies of $u_1$ and $a + k$ copies of $(-u_2)$, which contributes $\binom{a+b}{a+k} u_1^{b-k} (-u_2)^{a+k}$.
- Since the total target exponent of $u_2$ is $c + a$ and $u_2$ only appears in $(u_1 - u_2)^{a+b}$ and $(u_2 - u_3)^{b+c}$, we are forced to choose $(c + a) - (a + k) = c - k$ copies of $u_2$ and $(b + c) - (c - k) = b + k$ copies of $(-u_3)$ from $(u_2 - u_3)^{b+c}$, contributing $\binom{b+c}{b+k} u_2^{c-k} (-u_3)^{b+k}$.
- Since the total target exponent of $u_3$ is $a + b$ and $u_3$ only appears in $(u_2 - u_3)^{b+c}$ and $(u_3 - u_1)^{c+a}$, we are forced to choose $(a + b) - (b + k) = a - k$ copies of $u_3$ and $(c + a) - (a - k) = c + k$ copies of $(-u_1)$ from $(u_3 - u_1)^{c+a}$, contributing $\binom{c+a}{c+k} u_3^{a-k} (-u_1)^{c+k}$.
- The resulting power of $u_1$ is $(b - k) + (c + k) = b + c$, which automatically matches the target exponent of $u_1$.
- The combined sign is $(-1)^{(a+k) + (b+k) + (c+k)} = (-1)^{a+b+c + 3k} = (-1)^{a+b+c} (-1)^k$.

Summing over all $k \in \mathbb{Z}$ gives:

$$[u_1^{b+c} u_2^{c+a} u_3^{a+b}] (u_2 - u_3)^{b+c} (u_3 - u_1)^{c+a} (u_1 - u_2)^{a+b} = (-1)^{a+b+c} \sum_{k=-\infty}^{\infty} (-1)^k \binom{a+b}{a+k} \binom{b+c}{b+k} \binom{c+a}{c+k}.$$
```

---

### Bug B.5 — Problem 27 (`AtCoder AGC 058 D — Yet Another ABC String`, Lines 1625–1632): Sign/Factor Error in Final Closed-Form Formula & Incorrect Cluster Length Claim

- **Location**: Section 7, Problem 27 (`AtCoder AGC 058 D — Yet Another ABC String`), **Lines 1614–1632**.
- **Diagnosis**:
  1. **Mathematical Bug on Line 1631**: Look at how **Lines 1629–1631** expand $[x^A y^B z^C] \frac{1 - x y z}{1 - (x + y + z) + 2 x y z}$. Let $s = x + y + z$ and $u = x y z$. Then:
     $$\frac{1 - u}{1 - s + 2u} = (1 - u) \sum_{k=0}^{\infty} \frac{(-2u)^k}{(1 - s)^{k+1}} = \sum_{k=0}^{\infty} \frac{(-2)^k u^k}{(1 - s)^{k+1}} - \sum_{k=1}^{\infty} \frac{(-2)^{k-1} u^k}{(1 - s)^k}.$$
     Look at the coefficient of $u^k$ in the second sum: it is **$-(-2)^{k-1} = +\frac{1}{2}(-2)^k$**, **NOT** $-(-2)^k$!
     On **Line 1631**, `cohort3_wave_4b` factored out $(-2)^k$ from both terms and wrote:
     $$\text{Ans} = \sum_{k=0}^{\min(A, B, C)} (-2)^k \left[ \binom{N - 2k}{k} - \binom{N - 2k - 1}{k - 1} \right] \frac{(N - 3k)!}{(A - k)! \, (B - k)! \, (C - k)!} \pmod{998244353}.$$
     Let us test $(A, B, C) = (1, 1, 1)$ ($N = 3$):
     - There are $3! = 6$ permutations of `ABC`, of which $3$ (`ABC`, `BCA`, `CAB`) are cyclic rotations of `ABC` (forbidden) and $3$ (`ACB`, `BAC`, `CBA`) are valid. So the true answer is **$3$**.
     - Line 1631's formula gives:
       - $k = 0$: $(-2)^0 [1 - 0] \frac{3!}{1!1!1!} = 6$.
       - $k = 1$: $(-2)^1 \left[\binom{1}{1} - \binom{0}{0}\right] \frac{0!}{0!0!0!} = -2(1 - 1)(1) = 0$.
       - Total: $6 + 0 = \mathbf{6 \neq 3}$!
     - With the correct second-term coefficient $-(-2)^{k-1}$:
       - $k = 0$: $1 \cdot 1 \cdot 6 = 6$.
       - $k = 1$: $\left[(-2)^1 \binom{1}{1} - (-2)^0 \binom{0}{0}\right] \cdot 1 = (-2 - 1) = -3$.
       - Total: $6 - 3 = \mathbf{3}$!
     - Python brute-force verification across all small $(A, B, C)$ confirms that:
       $$\text{Ans} = \sum_{k=0}^{\min(A, B, C)} \left[ (-2)^k \binom{N - 2k}{k} - (-2)^{k-1} \binom{N - 2k - 1}{k - 1} \right] \frac{(N - 3k)!}{(A - k)! \, (B - k)! \, (C - k)!} \pmod{998244353}$$
       (with $\binom{N - 2k - 1}{-1} = 0$ for $k = 0$, or equivalently $(-2)^{k-1}\left[(-2)\binom{N-2k}{k} - \binom{N-2k-1}{k-1}\right]$ for $k \ge 1$) matches brute force 100% of the time ($3$ for $(1,1,1)$, $7$ for $(2,1,1)$, $16$ for $(2,2,1)$, $36$ for $(2,2,2)$).
  2. **Cluster Length Explanation on Line 1625**: On Line 1625, `cohort3_wave_4b` states that a cluster can extend for "$3k, 3k+1$, or $3k+2$ characters". In the Goulden–Jackson Cluster Method for the forbidden set $\mathcal{B} = \{\texttt{ABC}, \texttt{BCA}, \texttt{CAB}\}$, a single word has correlation polynomial $1 + v + v^2$ (overlap of length $0$ with itself, plus overlaps of length $1$ and $2$ with the other two cyclic shifts), so the single-starter cluster generating function is $\frac{-v^3}{1 + v + v^2} = \frac{-v^3(1 - v)}{1 - v^3} = \sum_{k=1}^{\infty} (-x^k y^k z^k + x^k y^k z^k (x + y + z))$ (clusters of length $3k + 2$ cancel out to weight $0$!). Multiplying by $3$ for the $3$ choices of starting word in $\mathcal{B}$ gives the total cluster generating function $C(x, y, z) = \frac{-3 x y z + x y z (x + y + z)}{1 - x y z}$, so:
     $$F(x, y, z) = \frac{1}{1 - (x + y + z) - C(x, y, z)} = \frac{1}{1 - (x + y + z) - \frac{-3 x y z + x y z(x + y + z)}{1 - x y z}} = \frac{1 - x y z}{1 - (x + y + z) + 2 x y z}.$$
- **Drop-In Replacement for Lines 1624–1632**:
  Replace Lines 1624–1632 with:
```markdown
- **Full Mathematical Derivation & Solution**:
  1. **Goulden–Jackson Cluster Generating Function**: The forbidden set is $\mathcal{B} = \{\texttt{ABC}, \texttt{BCA}, \texttt{CAB}\}$. Every word in $\mathcal{B}$ is a cyclic shift of $\texttt{ABC}$; if we track the transitions inside a cluster, each consecutive overlapping forbidden word shifts the period-3 phase by $+1$ (adding $1$ character) or $+2$ (adding $2$ characters). Thus, in a formal variable $v$ marking character steps inside a cluster after the initial $3$-character forbidden word (which has monomial weight $u = x y z$), the cluster extension factor is $\frac{1}{1 + v + v^2} = \frac{1 - v}{1 - v^3}$.
     Notice that in $\frac{1 - v}{1 - v^3} = \sum_{k=0}^{\infty} (v^{3k} - v^{3k+1})$, every full period of $3$ characters contributes weight $u = x y z$, a single extra step $v$ (summed over the $3$ cyclic starting words $\texttt{ABC}, \texttt{BCA}, \texttt{CAB}$) contributes $u(x + y + z)$, and extensions of $3k + 2$ characters have net weight $0$. Therefore, the total cluster generating function over all $3$ starting words is:
     $$C(x, y, z) = \frac{-3 x y z + x y z (x + y + z)}{1 - x y z}.$$
     Substituting $C(x, y, z)$ into the Goulden–Jackson master formula yields the exact rational trivariate OGF:
     $$F(x, y, z) = \frac{1}{1 - (x + y + z) - C(x, y, z)} = \frac{1}{1 - (x + y + z) + \frac{3 x y z - x y z(x + y + z)}{1 - x y z}} = \frac{1 - x y z}{1 - (x + y + z) + 2 x y z}.$$
  2. **Coefficient Extraction**: Let $s = x + y + z$ and $u = x y z$. Expanding in powers of $u$:
     $$F(x, y, z) = (1 - u) \sum_{k=0}^{\infty} \frac{(-2u)^k}{(1 - s)^{k+1}} = \sum_{k=0}^{\infty} \frac{(-2)^k u^k}{(1 - s)^{k+1}} - \sum_{k=1}^{\infty} \frac{(-2)^{k-1} u^k}{(1 - s)^k}.$$
     For a fixed $k$, $u^k = x^k y^k z^k$ consumes $k$ of each character, leaving $A - k, B - k, C - k$ characters of total length $N - 3k$ where $N = A + B + C$. Since $[x^{A-k} y^{B-k} z^{C-k}] s^{N-3k} = \frac{(N - 3k)!}{(A - k)! \, (B - k)! \, (C - k)!}$, and $[s^{N-3k}] (1 - s)^{-(k+1)} = \binom{N - 2k}{k}$ while $[s^{N-3k}] (1 - s)^{-k} = \binom{N - 2k - 1}{k - 1}$ (with $\binom{N - 1}{-1} = 0$ at $k = 0$), we obtain:
     $$\text{Ans} = \sum_{k=0}^{\min(A, B, C)} \left[ (-2)^k \binom{N - 2k}{k} - (-2)^{k - 1} \binom{N - 2k - 1}{k - 1} \right] \frac{(N - 3k)!}{(A - k)! \, (B - k)! \, (C - k)!} \pmod{998244353}.$$
     Evaluated in $O(\min(A, B, C)) = O(N)$ time. (Small-$N$ check: for $A = B = C = 1$, $k = 0$ gives $1 \cdot \binom{3}{0} \cdot 6 = 6$ and $k = 1$ gives $[(-2)\binom{1}{1} - 1\binom{0}{0}] \cdot 1 = -3$, totaling $6 - 3 = 3$.)
```

---

### Bug B.6 — Problem 12 (`Codeforces 1821F — Timber`, Lines 1314–1327): Misstated Combinatorial Object (`[0, n]` vs `[1, n]` and Sets of Tree Positions vs Orientations) & `"Wait:"` in Hint 2

- **Location**: Section 7, Problem 12 (`Codeforces 1821F — Timber`), **Lines 1314–1327**.
- **Diagnosis**:
  1. On **Line 1315**, the statement says: *"Count the number of ways to place $m$ trees at integer coordinates in $[1, n]$ and fell each tree either left ($[x - k, x]$) or right ($[x, x + k]$) so that all $m$ felled intervals are pairwise disjoint (not even sharing endpoints) and lie inside $[0, n]$."*
     In actual Codeforces 1821F ("Timber"), all felled intervals must lie inside **$[1, n]$** (NOT $[0, n]$), and the problem asks for the number of **sets of $m$ tree positions** $1 \le x_1 < \dots < x_m \le n$ for which **there exists** at least one valid felling orientation (NOT the number of pairs of positions and orientations!).
     - Why does the generating function on Line 1326 have transfer block $2 z^{k+1} + z^{2k+1}$? Because by Inclusion-Exclusion (or canonical state decomposition), a tree felled right occupies $k+1$ integer points $[x, x+k]$ (`+1`), a tree felled left occupies $k+1$ integer points $[x-k, x]$ (`+1`), and a tree whose $2k+1$ neighborhood $[x-k, x+k]$ is completely free can be felled **either** left or right, so we **subtract** $z^{2k+1}$ (`-1`) to count each valid set of tree positions **once**!
     - Python verification for $n = 5, m = 2, k = 1$: the formula on Line 1327 gives $2^2 \binom{2}{0}\binom{2}{2} - 2^1 \binom{2}{1}\binom{1}{1} = 4 \cdot 1 - 2 \cdot 2 = 0$? Wait: let's check $n = 5, m = 2, k = 1$ in the formula on Line 1327:
       Line 1327 has $\binom{n - m k - j k}{m} = \binom{5 - 2 - j}{2}$: for $j = 0$, $2^2 \binom{2}{0} \binom{3}{2} = 4 \cdot 1 \cdot 3 = 12$; for $j = 1$, $-2^1 \binom{2}{1} \binom{2}{2} = -4 \cdot 1 = -4$; total $12 - 4 = \mathbf{8}$, which is the exact number of subsets $\{x_1, x_2\} \subset \{1, 2, 3, 4, 5\}$ of size $2$ that admit a valid felling inside $[1, 5]$!
  2. On **Line 1319**, Hint 2 contains `"Wait: each tree occupies... Actually, the transfer block..."`.
- **Drop-In Replacement for Lines 1314–1327**:
  Replace Lines 1314–1327 with:
```markdown
### Problem 12: Codeforces 1821F — Timber
- **Source**: Codeforces Educational Round 147 F
- **URL**: https://codeforces.com/problemset/problem/1821/F
- **Problem Statement**: Given $n, m, k \le 3 \cdot 10^5$, count the number of subsets of $m$ integer tree coordinates $1 \le x_1 < x_2 < \dots < x_m \le n$ for which there exists a way to fell each tree $x_i$ either left (covering $[x_i - k, x_i]$) or right (covering $[x_i, x_i + k]$) such that all $m$ felled intervals lie strictly inside $[1, n]$ and are pairwise disjoint (not even sharing endpoints), modulo $998244353$.
- **Hints**:
  - *Hint 1 (Diagnostic)*: Since we count **subsets of tree positions** $\mathcal{X} = \{x_1, \dots, x_m\}$ rather than orientations, a tree at $x_i$ that has both $[x_i - k, x_i]$ and $[x_i, x_i + k]$ disjoint from all other felled intervals can be felled either left or right. Use Inclusion-Exclusion on trees that are simultaneously felled both ways!
  - *Hint 2 (Structural)*: A tree felled left or right covers $k + 1$ integer points ($2$ choices, weight $+2 z^{k+1}$), while a "double-felled" tree (subtracted by Inclusion-Exclusion) covers $[x_i - k, x_i + k]$, which contains $2k + 1$ integer points (weight $-z^{2k+1}$).
  - *Hint 3 (Algorithmic)*: With $m$ trees and $m + 1$ gaps of free integer points (each gap contributing $\frac{1}{1 - z}$), extract $[z^n] \frac{(2z^{k+1} - z^{2k+1})^m}{(1 - z)^{m+1}}$ in $O(m)$ time.
- **Full Mathematical Derivation & Solution**:
  1. **Inclusion-Exclusion Transfer OGF**: Each tree felled in a single direction occupies an interval of $k + 1$ integer points in $\{1, \dots, n\}$ ($2$ directions: weight $+2 z^{k+1}$). A tree that could be felled in both directions without overlapping its neighbors occupies $[x_i - k, x_i + k]$ of $2k + 1$ integer points (weight $-z^{2k+1}$ by Inclusion-Exclusion). Separated by $m + 1$ possibly empty gaps of unused integer points in $\{1, \dots, n\}$ (each gap having OGF $\frac{1}{1 - z}$), the OGF for $m$ trees is:
     $$F_m(z) = \frac{(2 z^{k + 1} - z^{2k + 1})^m}{(1 - z)^{m + 1}} = \frac{z^{m(k + 1)} (2 - z^k)^m}{(1 - z)^{m + 1}}.$$
  2. **Closed-Form Extraction**:
     $$[z^n] F_m(z) = [z^{n - m(k + 1)}] \frac{(2 - z^k)^m}{(1 - z)^{m + 1}} = \sum_{j = 0}^{m} (-1)^j 2^{m - j} \binom{m}{j} \binom{n - m k - j k}{m} \pmod{998244353}.$$
     Evaluated in $O(m)$ time.
```

---

### Bug B.7 — Problem 22 (`Codeforces 1479E — School Clubs`, Lines 1528–1535): Hesitation `? Actually,` & Sign Inversion in Final Output

- **Location**: Section 7, Problem 22 (`Codeforces 1479E — School Clubs`), **Lines 1517–1535**.
- **Diagnosis**:
  1. On **Line 1530**, the derivation contains a conversational hesitation: `"With probability \frac{1}{2}\frac{N-s}{N}\frac{s}{N-1}? Actually..."`.
  2. On **Line 1534**, it sets $f(0) = 0, f(1) = -2$ (so $g(0) = f(1) - f(0) = -2$) and claims the answer is $f(N) - \sum_{i=1}^m f(a_i)$.
     Let us check the sign! In the recurrence on Line 1532:
     $$s(N - s) g(s) - s(2N - s) g(s - 1) = 0 \quad (s \ge 1),$$
     and at $s = 0$, the constant drift $-1$ on the RHS of $\mathbb{E}[\Delta \Phi] = -1$ comes from the $m$ empty clubs of size $0$ that each transition $0 \to 1$ with probability $\frac{1}{2} \frac{1}{N}$ (summed over all $N$ students splitting off into a new club of size $1$, the total rate of creating a new club of size $1$ is $\frac{1}{2}$, contributing $\frac{1}{2}(f(1) - f(0)) = \frac{1}{2} g(0)$ to $\mathbb{E}[\Delta \Phi]$!).
     Wait: if $\mathbb{E}[\Phi(t + 1) - \Phi(t) \mid \mathcal{F}_t] = -1$, then by Optional Stopping:
     $$\mathbb{E}[\Phi(T) - \Phi(0)] = -\mathbb{E}[T] \implies \mathbb{E}[T] = \Phi(0) - \Phi(T) = \sum_{i=1}^m f(a_i) - f(N).$$
     Conversely, if we want $\mathbb{E}[T] = f(N) - \sum_{i=1}^m f(a_i)$ (as written on Line 1534), we need $\mathbb{E}[\Phi(t + 1) - \Phi(t) \mid \mathcal{F}_t] = +1$, which corresponds to $f(0) = 0, f(1) = +2$ ($g(0) = +2 > 0$, so $g(s) = 2 \prod_{j=1}^s \frac{2N - j}{N - j} > 0$ and $f(N) > \sum f(a_i)$)!
     Because Line 1534 set $f(1) = -2$ AND wrote $f(N) - \sum_{i=1}^m f(a_i)$, its output is **negative** ($-4$ instead of $+4$ for $N = 2, a = (1, 1)$, and $-18$ instead of $+18$ for $N = 3, a = (2, 1)$)!
- **Drop-In Replacement for Lines 1528–1535**:
  Replace Lines 1528–1535 with:
```markdown
- **Full Mathematical Derivation & Solution**:
  1. **Martingale Construction**: Seek $f(s)$ with $f(0) = 0$ such that $\Phi = \sum_{i} f(a_i)$ satisfies $\mathbb{E}[\Delta \Phi] = +1$ at every step before termination, so that Optional Stopping yields $\mathbb{E}[T] = \Phi(T) - \Phi(0) = f(N) - \sum_{i=1}^m f(a_i)$.
  2. **Per-Club Drift Isolation**: In one step, a student is chosen uniformly (probability $\frac{a_i}{N}$ from club $i$ of size $s = a_i$):
     - With probability $\frac{1}{2}$, the student forms a new club of size $1$: club $i$ changes $s \to s - 1$, and a new club of size $1$ is created ($0 \to 1$).
     - With probability $\frac{1}{2}$, the student joins another student's club (chosen uniformly among all $N - 1$ other students): club $i$ changes $s \to s - 1$ with probability $\frac{s}{N} \frac{1}{2} \frac{N - s}{N - 1}$, while if the first student was outside club $i$ (probability $\frac{N - s}{N}$) and joins a member of club $i$ (probability $\frac{1}{2} \frac{s}{N - 1}$), club $i$ changes $s \to s + 1$.
     Summing the expected change across all clubs (plus the creation of a size-$1$ club with total probability $\frac{1}{2}$, which contributes $\frac{1}{2} f(1)$) and setting the coefficient of each club of size $s \ge 1$ to zero in $\mathbb{E}[\Delta \Phi] - 1 = 0$:
     $$\frac{1}{2} f(1) + \sum_{i=1}^m \left[ \frac{a_i(N - a_i)}{2N(N - 1)} \big(f(a_i + 1) - f(a_i)\big) - \frac{a_i(2N - 1 - a_i)}{2N(N - 1)} \big(f(a_i) - f(a_i - 1)\big) \right] = 1.$$
     Setting $g(s) = f(s + 1) - f(s)$ with $f(0) = 0$ and $g(0) = f(1) = 2$ (so that the constant term $\frac{1}{2} f(1) = 1$ cancels the $+1$ on the RHS), each summand vanishes identically when:
     $$(N - s) g(s) = (2N - 1 - s) g(s - 1) \quad (1 \le s \le N - 1) \implies g(s) = 2 \prod_{j = 1}^{s} \frac{2N - j}{N - j}.$$
  3. **Rational Product Evaluation**: Since $g(s)$ is a hypergeometric term, we maintain the numerator and denominator products $\prod_{j=1}^s (2N - j)$ and $\prod_{j=1}^s (N - j)$ and accumulate $f(a_i) = \sum_{s=0}^{a_i - 1} g(s)$ at the sorted club sizes $a_i$ and at $N$ using Montgomery batch inversion in $O(m \log m)$ or $O(N)$ time, outputting $\mathbb{E}[T] = f(N) - \sum_{i=1}^m f(a_i) \pmod{998244353}$. (Small-$N$ check: for $N = 2, a = (1, 1)$, $g(0) = 2, g(1) = 2 \cdot \frac{3}{1} = 6$, so $f(1) = 2, f(2) = 8$, and $\mathbb{E}[T] = 8 - (2 + 2) = 4$.)
```

---

## Part 2: Complete Remediation of All Conversational Artifacts (`"Wait"`, `?`, Chinese Typo `虚拟`, Truncated Formula) & Delimiter Violations

### Bug B.8 — All Remaining Conversational Artifacts Across `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`

Below are the exact line numbers and drop-in replacements for every remaining `"Wait"`, self-answering `?`, typo, and truncated expression in the file:

#### 1. Section 3.3, Worked Example 3.2 (Line 408)
- **Location**: **Line 408**.
- **Current Text**:
```markdown
Wait: since $x Y_2(x) = \frac{1}{y_1(x)}$ from $x y_1(x) Y_2(x) = 1$, we can write this purely in terms of $y_1(x)$:
```
- **Drop-In Replacement for Line 408**:
```markdown
Since $x Y_2(x) = \frac{1}{y_1(x)}$ from Vieta's relation $x y_1(x) Y_2(x) = 1$, we can write this purely in terms of $y_1(x)$:
```

#### 2. Section 4.2, Worked Example 4.1 (Lines 569–580)
- **Location**: **Lines 569–580**.
- **Current Text**: Contains `"Wait: how do we compute $y_1(x) y_2(x)$ and $y_1(x) + y_2(x)$ when there are 3 roots?"` followed by a conversational monologue.
- **Drop-In Replacement for Lines 569–580**:
```markdown
To express $y_1(x) y_2(x)$ and $y_1(x) + y_2(x)$ algebraically, let $Y_3(x) = x^{-1} - 1 - x + O(x^2)$ denote the unique **large root** of the degree-3 polynomial $P(y) = x y^3 + x y^2 - y + x = 0$. By Vieta's formulas for $P(y) = x(y - y_1)(y - y_2)(y - Y_3) = x y^3 + x y^2 - y + x$:
- $y_1 + y_2 + Y_3 = -1 \implies y_1 + y_2 = -1 - Y_3$,
- $y_1 y_2 Y_3 = -1 \implies y_1 y_2 = -\frac{1}{Y_3}$.

Even more directly, evaluating $P(y)$ at $y = 1$ gives:

$$P(1) = x(1 - y_1(x))(1 - y_2(x))(1 - Y_3(x)) = x(1 + 1 + 1) - 1 = 3x - 1.$$

For small $x$, we can expand $y_1(x)$ and $y_2(x)$ in powers of $x^{1/2}$ by setting $y = x^{1/2} u$:

$$x^{3/2} u^3 + x^2 u^2 - x^{1/2} u + x = 0 \implies u = x^{1/2} + x u^3 + x^{3/2} u^2.$$
```

#### 3. Problem 5 (`Luogu P6672 — [清华集训2016] 你的生命已如风中残烛`, Lines 1181–1188)
- **Location**: **Lines 1181–1188**.
- **Current Text**: Contains `(Wait: for sum $+1$...)`, `? Careful: ... wait — ... Actually...`, an unedited Chinese word `虚拟` (`extra虚拟 $-1$`), and a missing space (`thedeck`).
- **Drop-In Replacement for Lines 1181–1188**:
```markdown
- **Full Mathematical Derivation & Solution**:
  1. **Raney Lemma Reduction**: A sequence of $n$ cards (consisting of the $m$ special cards $w_1, \dots, w_m$ with $\sum_{i=1}^m w_i = n$ and $n - m$ ordinary $0$-cards) is valid iff all proper prefix sums of $(w_i - 1)$ are $\ge 0$ while the total sum is $0$. Append one auxiliary $-1$ card ($w_{n+1} = 0$, net shift $-1$) so that the total sum of $a_i = w_i - 1$ over the $N = n + 1$ cards is $-1$.
  2. **Cyclic Shift Analysis**: In any cyclic permutation of the $N = n + 1$ values $a_1, \dots, a_{n+1}$ summing to $-1$, Raney's Lemma guarantees there is a **unique** cyclic shift whose partial sums $S_k = \sum_{j=1}^k a_j$ satisfy $S_k \ge 0$ for all $1 \le k \le n$ and $S_{n+1} = -1$. In that unique valid cyclic shift, the final element $a_{n+1}$ must be $-1$ (since $S_n = 0$ and $S_{n+1} = -1$).
  3. **Counting Valid Permutations**: There are $(n + 1)!$ permutations of all $n + 1$ cards (treating the $n - m + 1$ zero-value cards as distinguishable). Grouping them into $(n + 1)$-cycles of cyclic shifts gives $n!$ valid sequences in which the final card is one of the $n - m + 1$ zero-value cards. By symmetry among the $n - m + 1$ zero-value cards, the fraction of valid sequences ending specifically with our auxiliary card is $\frac{1}{n - m + 1}$, yielding:
     $$\text{Ans} = \frac{n!}{n - m + 1} \pmod{998244353}.$$
     (When card types are indistinguishable or have variable weights, the generating function $[x^n] \phi(x)^n$ is extracted via Lagrange Inversion in $O(n \log n)$ time.)
```

#### 4. Problem 8 (`Codeforces 1109D — Sasha and Interesting Fact from Graph Theory`, Lines 1239–1242)
- **Location**: **Lines 1239–1242**.
- **Current Text**: Contains two `?` self-corrections and a spurious $(n - s)!$ factor before $(k + 1) n^{n - k - 2}$.
- **Drop-In Replacement for Lines 1239–1242**:
```markdown
  2. **Stars-and-Bars + Forest Glueing**: For a fixed path length $k$ ($1 \le k \le \min(n - 1, m)$):
     - Choose the $k - 1$ internal vertices on the path between $a$ and $b$ in $\binom{n - 2}{k - 1} (k - 1)!$ ways.
     - Assign positive integer weights to the $k$ path edges summing to $m$ in $\binom{m - 1}{k - 1}$ ways.
     - Assign weights in $\{1, \dots, m\}$ to the remaining $n - 1 - k$ non-path edges in $m^{n - 1 - k}$ ways.
     - By Generalized Cayley's Formula, the number of trees on $n$ labeled vertices containing a fixed forest of $k + 1$ vertices in a single component of size $k + 1$ (and $n - k - 1$ isolated vertices) is $(k + 1) n^{n - k - 2}$ (with $(n - 1 + 1) n^{-1} = 1$ when $k = n - 1$).
     Summing over $1 \le k \le \min(n - 1, m)$:
     $$\text{Ans} = \sum_{k=1}^{\min(n - 1, m)} \binom{n - 2}{k - 1} (k - 1)! \binom{m - 1}{k - 1} m^{n - 1 - k} \cdot (k + 1) n^{n - k - 2} \pmod{10^9 + 7}.$$
```

#### 5. Problem 11 (`AtCoder AGC 021 E — Ball Eat Chameleons`, Lines 1303–1311)
- **Location**: **Lines 1303–1311**.
- **Current Text**: Contains two `"Wait:"` self-corrections (one on Line 1304 and one on Line 1307; note that Inspector A missed the second `"Wait:"` on Line 1307).
- **Drop-In Replacement for Lines 1303–1311**:
```markdown
- **Full Mathematical Derivation & Solution**:
  1. **Characterization of Valid Sequences**: Let $R$ be the total number of red balls and $B = K - R$ be the total number of blue balls. For all $N$ chameleons to turn red:
     - If $R < B$, it is impossible ($0$ ways).
     - If $R > B$, let $z$ be the number of chameleons that eat strictly more red balls than blue balls (requiring at least one `'R'`), and let the remaining $N - z$ chameleons eat an equal number $(\ge 1)$ of red and blue balls, with their **final** ball being `'B'` (so they eat `'R'` before that final `'B'`). Each of the $z$ chameleons provides at least $+1$ net surplus of $R$ over $B$, so $R - B \ge z \iff B \le R - N + (N - z)$. Equivalently, at least $N - (R - B)$ chameleons must be paired $(\texttt{R}, \texttt{B})$, meaning any prefix of the sequence can have $B_{\text{prefix}} - R_{\text{prefix}}$ at most $R - N$: the lattice path from $(0, 0)$ to $(R, B)$ must never touch the line $y - x = R - N + 1$.
     - If $R = B$ (requires $R = B \ge N$), the very last ball of the entire sequence must be `'B'` (serving as the final ball of one of the $N$ paired chameleons), so we delete the last ball `'B'` and reduce to a path from $(0, 0)$ to $(R, R - 1)$ that never touches $y - x = R - N + 1$.
  2. **Reflection Principle Formula**: By André's Reflection Principle, the number of lattice paths from $(0, 0)$ to $(r, b)$ staying strictly below $y - x = R - N + 1$ is:
     $$W(r, b) = \binom{r + b}{r} - \binom{r + b}{r + (R - N + 1)}$$
     (where $(r, b) = (R, B)$ for $R > B$ and $(r, b) = (R, R - 1)$ for $R = B$). Summing $W(r, b)$ over all $\max(N, K - R) \le R \le K$ computes the answer in $O(K)$ time.
```

#### 6. Problem 21 (`AtCoder ARC 136 F — Flip Cells`, Lines 1508–1514)
- **Location**: **Lines 1508–1514**.
- **Current Text**: Line 1509 truncates the row product as `\prod_{i=1}^H [y^{A_i}] (y + 1)^{\dots}`.
- **Drop-In Replacement for Lines 1508–1514**:
```markdown
- **Full Mathematical Derivation & Solution**:
  1. **EGF of Target and Reset States**: Let $N = H W$. In each row $i$, if the initial row has $c_i$ ones and $W - c_i$ zeros, and the target row weight is $A_i$, the EGF of flipping cells in row $i$ to reach weight $A_i$ is $P_i(z) = [y^{A_i}] \left(y \sinh\frac{z}{N} + \cosh\frac{z}{N}\right)^{W - c_i} \left(\sinh\frac{z}{N} + y \cosh\frac{z}{N}\right)^{c_i}$, while the EGF of returning from any row of weight $A_i$ to itself is $Q_i(z) = [y^{A_i}] \left(y \sinh\frac{z}{N} + \cosh\frac{z}{N}\right)^{W - A_i} \left(\sinh\frac{z}{N} + y \cosh\frac{z}{N}\right)^{A_i}$.
     Multiplying over all $H$ rows and converting to OGFs via the Borel/Laplace transform $\mathcal{L}\left[\sum_{k} \alpha_k e^{k z / N}\right] = \sum_{k} \frac{\alpha_k}{1 - \frac{k}{N} x}$ gives rational OGFs $F(x) = \sum_{k=-N}^{N} \frac{f_k}{1 - \frac{k}{N} x}$ and $G(x) = \sum_{k=-N}^{N} \frac{g_k}{1 - \frac{k}{N} x}$.
  2. **First-Passage Derivative**: By first-passage decomposition $H(x) = \frac{F(x)}{G(x)}$, differentiating at $x = 1$ (handling the simple pole at $k = N$ by multiplying numerator and denominator by $1 - x$) gives the exact expected stopping time in $O(H W^2) = O(N W)$ time.
```

#### 7. Problem 26 (`Codeforces 1349F2 — Slime and Sequences (Hard Version)`, Line 1599)
- **Location**: **Line 1599**.
- **Current Text**: Contains a self-questioning parenthetical: `(every occurrence of $k$ is preceded by at least one $k - 1$? More precisely, every $k > 1$ appearing in $a$ appears at least once after the first occurrence of $k - 1$)`. Moreover, in Codeforces 1349F2, a sequence is good iff for every $k > 1$ in the sequence, there is at least one occurrence of $k - 1$ before the **last** occurrence of $k$ (or equivalently, every occurrence of $k$ appears after the first occurrence of $k - 1$).
- **Drop-In Replacement for Line 1599**:
```markdown
- **Problem Statement**: A sequence $a_1, \dots, a_n$ of positive integers is "good" if for every $k > 1$ appearing in $a$, every occurrence of $k$ appears after the first occurrence of $k - 1$. For each $k = 1, \dots, n$, compute the total number of occurrences of $k$ across all good sequences of length $n$, modulo $998244353$, for $n \le 10^5$.
```

---

### Bug B.9 — Prohibited Math Delimiter Check (`\\[4pt]` / `\\[6pt]` Matching `\[`)

- **Locations**: **Lines 617, 618, 694, 718**.
- **Diagnosis**:
  - Although no inline `\(...\)` or display `\[...\]` delimiters appear in the file, Lines 617, 618, 694, and 718 use `\\[4pt]` or `\\[6pt]` for line spacing inside `aligned` environments, which triggers strict regex checks for `\[`.
- **Drop-In Replacements**:
  1. **Lines 616–620**: Replace `\\[4pt]` with `\\`:
```markdown
$$\begin{aligned}
x y Q(x, y; t) \big(1 - t S(x, y)\big) &= x y - t x Q(x, 0; t) - t(1 + x^2 + x y) Q(0, y; t) \\
&\quad - t y Q(-x, y; t) + t(1 + x^2) Q(0, 0; t) + t x \frac{\partial Q}{\partial x}(0, 0; t),
\end{aligned}$$
```
  2. **Lines 693–696**: Replace `\\[4pt]` with `\\`:
```markdown
$$\begin{aligned}
u_1(x_1, \dots, x_d) &= x_1 \, \phi_1\big(u_1(\mathbf{x}), \dots, u_d(\mathbf{x})\big), \\
&\;\;\vdots \\
u_d(x_1, \dots, x_d) &= x_d \, \phi_d\big(u_1(\mathbf{x}), \dots, u_d(\mathbf{x})\big),
\end{aligned}$$
```
  3. **Lines 716–720**: Replace `\\[6pt]` with `\\`:
```markdown
$$\begin{aligned}
[x_1^{n_1} \cdots x_d^{n_d}] \frac{H(\mathbf{u}(\mathbf{x}))}{\det\!\left(\delta_{i,j} - x_i \frac{\partial \phi_i}{\partial u_j}(\mathbf{u}(\mathbf{x}))\right)} &= [x_1^{n_1} \cdots x_d^{n_d}] \frac{H(\mathbf{u}(\mathbf{x}))}{\det\!\left(\delta_{i,j} - \frac{u_i}{\phi_i(\mathbf{u})} \frac{\partial \phi_i}{\partial u_j}(\mathbf{u})\right)} \\
&= [u_1^{n_1} \cdots u_d^{n_d}] \, H(\mathbf{u}) \prod_{i=1}^{d} \phi_i(\mathbf{u})^{n_i}.
\end{aligned}$$
```

---

## Summary Checklist for Remediation Agent

| Issue ID | Target Lines in `cohort3_wave_4b` | Category | Summary of Fix |
| :--- | :--- | :--- | :--- |
| **Bug B.1** | Lines 251–271 & Lines 1572–1588 | Mathematical / Sign Bug | Add $\gcd(p, q) = 1$, distinguish $p$-branch residue sum for general $(p, q)$ vs single exterior residue for $q = 1$, and fix sign of exterior residue in Problem 25 from $\frac{(1-w)^{-a}}{(p+1)w - 1}$ to $\frac{(1-w)^{-a}}{1 - (p+1)w}$. |
| **Bug B.2** | Lines 656–668 | Pedagogical / Editorial | Remove `"Wait:"` in Worked Example 4.3 (Kreweras Walk) and provide clean kernel elimination and small-$m$ verification. |
| **Bug B.3** | Lines 755–770 | Mathematical / Algebraic Bug | Fix Good–Lagrange exponent $[u_1^{n-1} u_2^m]$ (was $[u_1^{n-1} u_2^{m-1}]$), fix white-rooted count $T_{n,m} = n^m m^{n-1}$ vs unrooted count $t_{n,m} = n^{m-1} m^{n-1}$, and fix false equalities $2 = 2^0 1^1$ and $8 = 2^1 2^1$ in the trace table. |
| **Bug B.4** | Lines 808–835 | Pedagogical / Editorial | Remove all three `"Wait"` false starts in Worked Example 5.3 (Dixon's Identity) using direct $(u_1 - u_2)^{a+b}$ indexing. |
| **Bug B.5** | Lines 1624–1632 | Mathematical / Sign Bug | Fix second-term factor in Problem 27 (`AtCoder AGC 058 D`) from $-(-2)^k \binom{N-2k-1}{k-1}$ to $-(-2)^{k-1} \binom{N-2k-1}{k-1}$ and clarify cluster extension factor $\frac{1-v}{1-v^3}$. |
| **Bug B.6** | Lines 1314–1327 | Mathematical / Statement | Fix Problem 12 (`Codeforces 1821F`) statement ($[1, n]$ and subsets of tree positions via Inclusion-Exclusion) and remove `"Wait:"` in Hint 2. |
| **Bug B.7** | Lines 1528–1535 | Mathematical / Sign Bug | Remove `? Actually,` in Problem 22 (`Codeforces 1479E`) and fix sign convention $f(1) = g(0) = +2$ so $f(N) - \sum f(a_i) > 0$. |
| **Bug B.8** | Lines 408, 569–580, 1181–1188, 1239–1242, 1303–1311, 1508–1514, 1599 | Editorial / Polish | Remove all remaining `"Wait"`, `?`, Chinese typo `虚拟`, and truncated `^{\dots}` across worked examples and problems. |
| **Bug B.9** | Lines 617, 618, 694, 718 | Formatting / Delimiter | Replace `\\[4pt]` and `\\[6pt]` with `\\` to ensure zero `\[` regex matches. |
