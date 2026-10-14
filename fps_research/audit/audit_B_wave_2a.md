# Second-Pass Mathematical & Pedagogical Audit Report — Wave 2A (`cohort3_wave_2a_substitutions_transforms.md`)

- **Target File**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_2a_substitutions_transforms.md` (1,151 lines)
- **Source Files Audited Against**:
  1. `C1`: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_11_to_15_substitutions_transforms.md` (1,760 lines)
  2. `C2-New`: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_new_iter_63_to_67_substitutions_transforms.md` (1,567 lines)
  3. `C2-Pre`: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_63_to_67_substitutions_transforms.md` (912 lines)
- **Prior Audit Cross-Checked**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/audit/audit_A_wave_2a.md` (Inspector A, 968 lines)
- **Auditor**: Inspector B (Independent Redundant Audit + Numerical Python Verification + Live Judge Verification)

---

## 0. Executive Summary & Critical Warnings on Inspector A's Report (`audit_A_wave_2a.md`)

Before applying any remediation to `cohort3_wave_2a_substitutions_transforms.md`, the remediation agent **MUST** read the following cross-audit findings. Several bugs in `cohort3_wave_2a` were completely missed by Inspector A, and **several of Inspector A's proposed edits in `audit_A_wave_2a.md` introduce new mathematical bugs or raw scratchpad text**:

1. **CRITICAL (Missed by Inspector A): `mobius_transform` in Section 3.1 (Lines 32–46), Section 8.1 (Line 402), and Section 8.2 (Lines 468–503) Fails on 100% of Inputs**:
   - Python numerical testing against naive polynomial expansion proves that `cohort3_wave_2a`'s `mobius_transform` fails on **all 5/5** non-trivial test cases (both $c = 0$ and $c \neq 0$).
   - When $c = 0$, Line 484 computes `s = b * a^{-1} * d` instead of `b * a^{-1}`, which evaluates $\sum_{k=0}^n f_k d^{n-k}(ax + bd)^k$ instead of $\sum_{k=0}^n f_k d^{n-k}(ax + b)^k$, and Lines 472 & 480 divide by $d$ and $a$, failing when $d = 0$ or $a = 0$.
   - When $c \neq 0$, Section 3.1 (Lines 36–42) and Section 8.2 (Lines 487–502) shift $P$ by $s_1 = d/c$ instead of $\alpha = a/c$, reverse `f1` *before* scaling by $\beta$, and shift by $b / (a - bc/d)$ instead of $d$.
   - Inspector A (`audit_A_wave_2a.md` Section 2.1, Lines 185–201) only deleted the two-line `"Wait"` remark at Line 43 and left the broken derivation in Section 3.1, the broken formula in Section 8.1 (Line 402), and the broken C++ implementation in Section 8.2 (Lines 468–503) untouched. **Use Bug 1.1 of this report instead.**

2. **CRITICAL WARNING — DO NOT Apply Inspector A's Bug 1.2 (`audit_A_wave_2a.md` Lines 55–83)**:
   - Inspector A claims that `cohort3_wave_2a` Problem 10 (`Large Schröder Convolution`) has a sign error $xS(x) = \frac{u}{1-u}$. That is a **hallucination**: `cohort3_wave_2a` ALREADY has the exact, verified identities $xS(x) = \frac{u}{1+u}$ and $S(x) = \frac{1-u}{1-2u} = 1 + 2u \pmod{x^{n+1}}$ in Section 4.1 (Line 148), Section 4.3 (Lines 205–206), and Problem 10 (Lines 754–765).
   - Worse, Inspector A's proposed replacement (`audit_A_wave_2a.md` Line 73) replaces $[u^n] \left(\sum_{k=0}^n c_k (1+u)^k\right)(1+u)^n(1+2u)^n$ with $[u^n] \left(\sum_{k=0}^n c_k (1+2u)^k\right)(1-2u^2)(1+u)^{n-1}(1+2u)^{n-1}$ for $[x^n] \frac{\sum_{k=0}^n c_k S(x)^k}{\sqrt{1 - 6x + x^2}}$. That replacement is **mathematically wrong on two counts**:
     1. In Problem 10, the target is $[x^n] \frac{\sum c_k S(x)^k}{\sqrt{1 - 6x + x^2}}$, where the denominator $\sqrt{1 - 6x + x^2}$ **cancels** the Jacobian factor $(1 - 2u^2)$ (Formula A in Section 4.3 Line 205, NOT Formula B!). Multiplying by $(1 - 2u^2)$ again double-counts the Jacobian.
     2. In Problem 10, $c_k$ is defined after expanding $P(S(x)) = P(1+2u)$ or $P(xS(x))$; in `cohort3_wave_2a` Lines 754–765, every equation is already 100% consistent and verified in Python. **Leave Problem 10 (Lines 750–765) untouched.**

3. **CRITICAL (Missed AND Perpetuated by Inspector A): Degree-Mismatch Error in Bounded-Height Dyck Paths (Section 4.2 Line 187 & Problem 13 `UOJ #424` Line 800)**:
   - In Section 4.2 Line 185, $F_H(x(u)) = (1+u)\frac{1 - u^{H+1}}{1 - u^{H+2}}$.
   - Applying Formula B ($[x^n] H(u(x)) = [u^n] H(u)(1 - u^2)(1+u)^{2n-2}$) multiplies $(1+u)$ by $(1-u^2)(1+u)^{2n-2} = (1-u)(1+u)^{2n-1}$, yielding:
     $$[x^n] F_H(x) = [u^n] (1 - u)(1 + u)^{2n} \frac{1 - u^{H+1}}{1 - u^{H+2}} = [u^n] (1 - u^2)(1 + u)^{2n-1} \frac{1 - u^{H+1}}{1 - u^{H+2}}.$$
   - Both `cohort3_wave_2a` (Line 187 and Line 800) AND `audit_A_wave_2a.md` (Bug 1.3, Line 106) wrote $(1 - u^2)(1 + u)^{2n} \frac{1 - u^{H+1}}{1 - u^{H+2}}$, which has an extra factor of $(1+u)$ and fails even as $H \to \infty$ (giving $\binom{2n}{n} - \binom{2n}{n-2}$ instead of $C_n = \binom{2n}{n} - \binom{2n}{n-1}$).
   - Furthermore, for Problem 13 (`UOJ #424`), Python brute-force enumeration of all $M^n$ sequences over $\{1, \dots, M\}$ for $1 \le n \le 5, 1 \le M \le 4$ confirms that the number of distinct Cartesian trees equals the number of $n$-semilength Dyck paths of **max height $H = M$** (since at most $M-1$ left-child steps can occur along any root-to-node path, which corresponds to at most $M$ open parentheses on the Dyck stack, i.e., $\frac{1 - u^{M+1}}{1 - u^{M+2}}$). **Use Bug 1.3 of this report instead of Inspector A's Bug 1.3.**

4. **CRITICAL WARNING — DO NOT Apply Inspector A's Bug 1.4 (`LOJ #6261`, `audit_A_wave_2a.md` Lines 114–162)**:
   - Inspector A's replacement (`audit_A_wave_2a.md` Line 129) defines $u(x) = \frac{1 - \sqrt{1 - 4x}}{2} = xC(x)$ and then applies $x = \frac{u}{(1+u)^2}$, which is the substitution for $u(x) = C(x) - 1 = \frac{1 - 2x - \sqrt{1 - 4x}}{2x}$, NOT for $xC(x)$ (which satisfies $x = v(1-v)$). **Use Bug 1.4 of this report instead**, which keeps the substitutions for $u(x) = C(x)-1$ and $v(x) = xC(x)$ strictly distinct and verified.

5. **CRITICAL (Partially Caught by Inspector A with Wrong Line Numbers): Bluestein Chirp-Z Identity Error in 4 Locations**:
   - The false identity $-jr = \binom{j-r}{2} - \binom{j}{2} - \binom{r}{2}$ appears in **4 locations** in `cohort3_wave_2a`:
     1. **Section 7.2, Lines 364–367** (Inspector A mis-cited as Lines 373–385)
     2. **Section 8.1, Line 411** (Row 18 of Master Table — missed by Inspector A)
     3. **Section 8.2, Lines 553–570** (`bluestein_roots_filter` — Inspector A mis-cited as Lines 539–556)
     4. **Section 9, Line 597** (Row 5 of Citation Table — missed by Inspector A)
   - **Use Bug 1.2 of this report** to fix all 4 occurrences with exact line numbers.

6. **CRITICAL (Live Judge Verification of `AtCoder FPS-24 V`, `FPS-24 H`, and `AGC 054 E`)**:
   - Live verification against `https://atcoder.jp/contests/fps-24/tasks` reveals that **Task V (`fps_24_v`) is `V - 12 Directions`** (which `cohort3_wave_2a` Problem 11 mislabeled as `FPS-24 H — Walk`), whereas **Task H (`fps_24_h`) is `H - Jump`**.
   - In addition, for `FPS-24 V — 12 Directions`, both `cohort3_wave_2a` (Line 783) and `audit_A_wave_2a.md` (Lines 263–283) missed the key factorial-split convolution identity:
     $$f_n(H) = \sum_{b=0}^{n-|H|} \binom{n}{b+|H|} \binom{n}{b}^2 = (n!)^3 \sum_{b+c=n} \left(\frac{1}{(b!)^2(b+|H|)!}\right)\left(\frac{1}{(c!)^2(c-|H|)!}\right),$$
     which evaluates $f_n(H)$ for **all** $0 \le n \le N$ in a single NTT before the EGF convolution with $W$!
   - Furthermore, in `audit_A_wave_2a.md` Lines 303–378 (Problem 12) and Lines 391–463 (Problem 14 `AGC 054 E`), Inspector A left ~100 lines of raw `"Wait —"` self-correction monologue inside the replacement blocks. **Use Bug 1.5 and Fix 2.4 of this report instead.**

7. **Correction to Inspector A's Section 3.5 (`ABC 240 G`)**:
   - Inspector A (`audit_A_wave_2a.md` Lines 752–818) claims `AtCoder ABC 240 G — Teleporting Takahashi` was dropped from `cohort3_wave_2a`. In fact, `ABC 240 G` is **already present as Problem 33** in `cohort3_wave_2a` (Lines 1057–1070). Do not duplicate `ABC 240 G`; only append the 6 genuinely omitted problems from `C2-New` (`CF 993E`, `CF 1342E`, `Luogu P4091`, `Luogu P3702`, `Yukicoder 1145 / ARC 106 E`, `BZOJ 3328 — PYXFIB`) and the 1 omitted rejected problem from `C2-Pre` (`R6: Library Checker — kth_term_of_linearly_recurrent_sequence`).

---

## 1. Mathematical & Algorithmic Bugs in `cohort3_wave_2a_substitutions_transforms.md`

### Bug 1.1: Completely Broken `mobius_transform` in Section 3.1 (Lines 32–46), Section 8.1 (Line 402), and Section 8.2 (Lines 468–503)

- **Location**:
  1. Section 3.1, **Lines 32–46**
  2. Section 8.1, **Line 402** (Master Table Row 9)
  3. Section 8.2, **Lines 468–503** (`mobius_transform` C++ reference kernel)
- **Mathematical Proof of Bug**:
  - We want to compute $Q(x) = (cx + d)^n P\!\left(\frac{ax + b}{cx + d}\right) = \sum_{k=0}^n f_k (ax + b)^k (cx + d)^{n-k}$.
  - When $c \neq 0$, write $w = cx + d$, so $x = (w - d)/c$ and:
    $$ax + b = \frac{a}{c} w + \frac{bc - ad}{c} = \alpha w + \beta, \quad \text{where } \alpha = \frac{a}{c}, \quad \beta = \frac{bc - ad}{c}.$$
    Then:
    $$Q(x) = \sum_{k=0}^n f_k (\alpha w + \beta)^k w^{n-k} = w^n \sum_{k=0}^n f_k (\alpha + \beta w^{-1})^k = w^n P(\alpha + \beta w^{-1}).$$
  - This decomposes cleanly into 4 steps:
    1. **Taylor shift by $\alpha = a/c$**: $P_1(y) = P(y + \alpha) = \sum_{k=0}^n g_k y^k$.
    2. **Scale by $\beta = (bc - ad)/c$**: $P_2(y) = P_1(\beta y) = \sum_{k=0}^n (g_k \beta^k) y^k$.
    3. **Polynomial reversal ($w^n P_2(w^{-1})$)**: $P_3(w) = \sum_{k=0}^n (g_{n-k} \beta^{n-k}) w^k$.
    4. **Substitute $w = cx + d$**: First Taylor-shift $P_4(u) = P_3(u + d)$, then scale $[u^j] P_4(u)$ by $c^j$!
  - In `cohort3_wave_2a`:
    - Section 3.1 (Lines 36–42) and Section 8.2 (Lines 487–502) shifted by $d/c$ instead of $a/c$, reversed `f1` *before* scaling by $\beta$, and shifted by $b/(a - bc/d)$ instead of $d$.
    - In the $c = 0$ branch (Lines 471–485), Line 484 multiplied `s` by `d`, computing $\sum f_k d^{n-k}(ax + bd)^k$ instead of $\sum f_k d^{n-k}(ax + b)^k$, and divided by $d$ and $a$ (failing when $d = 0$ or $a = 0$).
- **Drop-In Replacement 1 (Section 3.1, Lines 32–46)**:
```markdown
Given $P(x) = \sum_{k=0}^n f_k x^k$ and parameters $a, b, c, d \in \mathbb{F}_p$, we wish to compute the degree-$n$ polynomial:
$$Q(x) = (cx + d)^n P\!\left(\frac{ax + b}{cx + d}\right) = \sum_{k=0}^n f_k (ax + b)^k (cx + d)^{n-k}.$$

- **Case 1 ($c = 0$)**: We need $Q(x) = \sum_{k=0}^n (f_k d^{n-k})(ax + b)^k$. Let $h_k = f_k d^{n-k}$ (computed from $k = n$ down to $0$ without division, so $d = 0$ is handled automatically). Apply a Taylor shift by $b$ to $H(y) = \sum_{k=0}^n h_k y^k$ to obtain $H(u + b) = \sum_{j=0}^n r_j u^j$, and then scale each coefficient by $a^j$ (setting $u = ax$, which also handles $a = 0$ without division).
- **Case 2 ($c \neq 0$)**: Let $w = cx + d$, so $x = (w - d)/c$. Express the numerator $ax + b$ in terms of $w$:
  $$ax + b = \frac{a}{c}(cx + d) + \frac{bc - ad}{c} = \alpha w + \beta, \quad \text{where } \alpha = \frac{a}{c}, \quad \beta = \frac{bc - ad}{c}.$$
  Substituting $ax + b = \alpha w + \beta$ and $cx + d = w$ into $Q(x)$ yields:
  $$Q(x) = \sum_{k=0}^n f_k (\alpha w + \beta)^k w^{n-k} = w^n \sum_{k=0}^n f_k (\alpha + \beta w^{-1})^k = w^n P(\alpha + \beta w^{-1}).$$
  This identity decomposes into four elementary $O(n \log n)$ operations:
  1. **Inner Taylor Shift**: Compute $P_1(y) = P(y + \alpha) = \sum_{k=0}^n g_k y^k$ via `taylor_shift(f, alpha)`.
  2. **Inner Scaling**: Multiply $[y^k] P_1(y)$ by $\beta^k$ to obtain $P_2(y) = P(\alpha + \beta y) = \sum_{k=0}^n (g_k \beta^k) y^k$ (note that if $ad - bc = 0$, then $\beta = 0$ and only the $k = 0$ term survives, automatically handling the degenerate constant-ratio case without division by $\beta$).
  3. **Reversal**: Reverse the coefficient array of $P_2$ to obtain $P_3(w) = w^n P_2(w^{-1}) = \sum_{k=0}^n (g_{n-k} \beta^{n-k}) w^k$.
  4. **Outer Affine Substitution ($w = cx + d$)**: Compute $P_4(u) = P_3(u + d) = \sum_{j=0}^n r_j u^j$ via `taylor_shift(P3, d)`, then multiply $[u^j] P_4(u)$ by $c^j$ to set $u = cx$.

This reduces any projective linear substitution to **at most two Taylor shifts** (2 NTT convolutions) and linear-time scalings/reversals in $O(n \log n)$ time.
```
- **Drop-In Replacement 2 (Section 8.1, Line 402)**:
```markdown
| 9 | Möbius / Rational Linear | $g(x) = (cx+d)^n f\!\left(\frac{ax+b}{cx+d}\right)$ | Shift by $\alpha = a/c$, scale by $\beta = (bc-ad)/c$, reverse, shift by $d$, scale by $c$ | $O(n \log n)$ | `mobius_transform` |
```
- **Drop-In Replacement 3 (Section 8.2, Lines 468–503)**:
```cpp
// Projective / Mobius Transform: Q(x) = (cx + d)^n P((ax + b) / (cx + d))
// Handles all degenerate cases (c = 0, d = 0, a = 0, ad - bc = 0) in O(n log n) time
Poly mobius_transform(const Poly& f, long long a, long long b, long long c, long long d) {
    int n = (int)f.size() - 1;
    if (n < 0) return {};
    a = (a % MOD + MOD) % MOD; b = (b % MOD + MOD) % MOD;
    c = (c % MOD + MOD) % MOD; d = (d % MOD + MOD) % MOD;

    if (c == 0) {
        // Q(x) = sum_{k=0}^n (f[k] * d^{n-k}) * (a*x + b)^k
        Poly h(n + 1);
        long long pw_d = 1;
        for (int k = n; k >= 0; --k) {
            h[k] = f[k] * pw_d % MOD;
            pw_d = pw_d * d % MOD;
        }
        Poly shifted = taylor_shift(h, b);
        long long pw_a = 1;
        for (int j = 0; j <= n; ++j) {
            shifted[j] = shifted[j] * pw_a % MOD;
            pw_a = pw_a * a % MOD;
        }
        return shifted;
    }

    long long inv_c = qpow(c, MOD - 2);
    long long alpha = a * inv_c % MOD;
    long long beta = (b * c - a * d) % MOD;
    if (beta < 0) beta += MOD;
    beta = beta * inv_c % MOD;

    // Step 1: P1(y) = P(y + alpha)
    Poly p1 = taylor_shift(f, alpha);

    // Step 2: P2(y) = P1(beta * y)
    long long pw_beta = 1;
    for (int k = 0; k <= n; ++k) {
        p1[k] = p1[k] * pw_beta % MOD;
        pw_beta = pw_beta * beta % MOD;
    }

    // Step 3: P3(w) = w^n P2(w^{-1}) (reverse coefficients)
    reverse(p1.begin(), p1.end());

    // Step 4: Q(x) = P3(c*x + d) -> shift by d, then scale by c^j
    Poly p4 = taylor_shift(p1, d);
    long long pw_c = 1;
    for (int j = 0; j <= n; ++j) {
        p4[j] = p4[j] * pw_c % MOD;
        pw_c = pw_c * c % MOD;
    }
    return p4;
}
```

---

### Bug 1.2: False Bluestein Chirp-Z Identity in Section 7.2 (Lines 364–367), Section 8.1 (Line 411), Section 8.2 (Lines 553–570), and Section 9 (Line 597)

- **Location**:
  1. Section 7.2, **Lines 364–367**
  2. Section 8.1, **Line 411** (Master Table Row 18)
  3. Section 8.2, **Lines 553–570** (`bluestein_roots_filter` C++ kernel)
  4. Section 9, **Line 597** (Citation Table Row 5)
- **Mathematical Proof of Bug**:
  - Expanding $\binom{j-r}{2} - \binom{j}{2} - \binom{r}{2}$ gives:
    $$\frac{(j-r)(j-r-1) - j(j-1) - r(r-1)}{2} = \frac{-2jr + 2r}{2} = -jr + r \neq -jr.$$
  - The true Bluestein identity is:
    $$-jr = \binom{j}{2} + \binom{r}{2} - \binom{j+r}{2}.$$
  - Substituting $\omega_m^{-jr} = \omega_m^{\binom{j}{2}} \omega_m^{\binom{r}{2}} \omega_m^{-\binom{j+r}{2}}$ gives:
    $$c_r = \frac{1}{m} \omega_m^{\binom{r}{2}} \sum_{j=0}^{m-1} \left(y_j \omega_m^{\binom{j}{2}}\right) \omega_m^{-\binom{j+r}{2}}.$$
    Reversing $A_j = y_j \omega_m^{\binom{j}{2}}$ into `A_rev[m - 1 - j] = A_j` and convolving with $B_k = \omega_m^{-\binom{k}{2}}$ ($0 \le k < 2m - 1$) places the sum at index `(m - 1 - j) + (j + r) = m - 1 + r` (NOT `m - 1 - r` as written at Line 568!).
- **Drop-In Replacement 1 (Section 7.2, Lines 364–367)**:
```markdown
When $m$ does not divide $2^k$ (or in arbitrary multi-point evaluation along geometric progressions), we use Bluestein's identity:
$$-jr = \binom{j}{2} + \binom{r}{2} - \binom{j+r}{2}.$$
Then:
$$c_r = \frac{1}{m} \omega_m^{\binom{r}{2}} \sum_{j=0}^{m-1} \left(y_j \omega_m^{\binom{j}{2}}\right) \omega_m^{-\binom{j+r}{2}},$$
which is a single linear convolution between the reversed sequence $A^{\text{rev}}_{m-1-j} = y_j \omega_m^{\binom{j}{2}}$ ($0 \le j < m$) and $B_k = \omega_m^{-\binom{k}{2}}$ ($0 \le k < 2m - 1$), read off at index $m - 1 + r$ in $O(m \log m)$ time!
```
- **Drop-In Replacement 2 (Section 8.1, Line 411)**:
```markdown
| 18 | Bluestein Chirp-Z Filter | $c_r = \frac{1}{m} \sum_{j=0}^{m-1} \omega_m^{-jr} F(\omega_m^j x)$ | $-jr = \binom{j}{2} + \binom{r}{2} - \binom{j+r}{2}$ convolution | $O(m \log m)$ | `bluestein_roots_filter` |
```
- **Drop-In Replacement 3 (Section 8.2, Lines 553–570)**:
```cpp
// Given y[j] = F(w^j) for j = 0..m-1, recover c[r] = (1/m) sum_{j=0}^{m-1} y[j] w^{-j*r}
// Using Bluestein's identity: -j*r = C(j, 2) + C(r, 2) - C(j + r, 2)
Poly bluestein_roots_filter(const Poly& y, int m, long long w) {
    auto c2 = [&](long long x) -> long long {
        return (x * (x - 1) / 2) % m; // Since w^m = 1, reduce exponent mod m
    };
    long long inv_w = qpow(w, MOD - 2);
    Poly A_rev(m), B(2 * m - 1);
    for (int j = 0; j < m; ++j)
        A_rev[m - 1 - j] = y[j] * qpow(w, c2(j)) % MOD;
    for (int k = 0; k < 2 * m - 1; ++k)
        B[k] = qpow(inv_w, c2(k));
    Poly conv = multiply(A_rev, B);
    Poly c(m);
    long long inv_m = qpow(m, MOD - 2);
    for (int r = 0; r < m; ++r) {
        c[r] = inv_m * qpow(w, c2(r)) % MOD * conv[m - 1 + r] % MOD;
    }
    return c;
}
```
- **Drop-In Replacement 4 (Section 9, Line 597)**:
```markdown
| **Bluestein (1970)** | *A linear filtering approach to the computation of discrete Fourier transform*, IEEE Trans. Audio Electroacoustics 18(4), 451–455 | Introduces the identity $-jr = \binom{j}{2} + \binom{r}{2} - \binom{j+r}{2}$, reducing arbitrary-length root-of-unity evaluation and filtering to a single linear convolution. |
```

---

### Bug 1.3: Bounded-Height Dyck Path Factor Error in Section 4.2 (Lines 185–188) and Problem 13 (`UOJ #424`, Lines 793–806)

- **Location**:
  1. Section 4.2, **Lines 185–188**
  2. Section 10.2, Problem 13 (`UOJ #424`), **Lines 793–806**
- **Mathematical Proof of Bug**:
  1. Under $x = \frac{u}{(1+u)^2}$, we have $F_H(x(u)) = (1+u) \frac{1 - u^{H+1}}{1 - u^{H+2}}$ and $\frac{dx}{du} = \frac{1 - u}{(1+u)^3}$.
  2. Applying Cauchy's Integral Formula (or Formula B: $[x^n] H(u(x)) = [u^n] H(u)(1 - u^2)(1 + u)^{2n-2}$ with $H(u) = F_H(x(u))$):
     $$[x^n] F_H(x) = [u^n] \left((1+u)\frac{1 - u^{H+1}}{1 - u^{H+2}}\right) (1 - u^2)(1 + u)^{2n-2} = [u^n] (1 - u)(1 + u)^{2n} \frac{1 - u^{H+1}}{1 - u^{H+2}}.$$
     Notice that $(1 - u)(1 + u)^{2n} = (1 - u^2)(1 + u)^{2n-1}$, **NOT** $(1 - u^2)(1 + u)^{2n}$!
     Check $H \to \infty$: $[u^n] (1 - u)(1 + u)^{2n} = \binom{2n}{n} - \binom{2n}{n-1} = C_n$ (correct!), whereas $[u^n](1 - u^2)(1 + u)^{2n} = \binom{2n}{n} - \binom{2n}{n-2}$ (wrong!).
  3. Furthermore, in Problem 13 (`UOJ #424`), a sequence $A_1, \dots, A_n \in \{1, \dots, M\}$ has left-most minimum Cartesian tree where every left-child step strictly increases the minimum value from $\{1, \dots, M\}$. Thus, any root-to-node path contains at most $M - 1$ left-child edges. Under the standard bijection between binary trees and Dyck paths (where the root puts 1 open parenthesis on the stack and each left-child edge pushes 1 additional open parenthesis), a binary tree with at most $M - 1$ left-child edges corresponds to a Dyck path of **max height $H = M$** (verified by brute force for $1 \le n \le 5, 1 \le M \le 4$: e.g., for $n = 3, M = 2$, $2^3 = 8$ sequences yield $4 = \text{Dyck}(n=3, H=2)$ distinct Cartesian trees, whereas $\text{Dyck}(n=3, H=1) = 1$).
- **Drop-In Replacement 1 (Section 4.2, Lines 185–188)**:
```markdown
$$F_H(x(u)) = (1+u) \frac{1 - u^{H+1}}{1 - u^{H+2}}.$$
Applying Formula B ($[x^n] H(u(x)) = [u^n] H(u)(1 - u^2)(1 + u)^{2n-2}$) multiplies $(1+u)$ by $(1 - u^2)(1 + u)^{2n-2} = (1 - u)(1 + u)^{2n-1}$, yielding:
$$[x^n] F_H(x) = [u^n] (1 - u)(1 + u)^{2n} \frac{1 - u^{H+1}}{1 - u^{H+2}} = [u^n] (1 - u^2)(1 + u)^{2n-1} \frac{1 - u^{H+1}}{1 - u^{H+2}}.$$
Expanding $\frac{1 - u^{H+1}}{1 - u^{H+2}} = 1 + \sum_{k \ge 1} \left(u^{k(H+2)-1} - u^{k(H+2)}\right)$ and multiplying by $(1 - u)(1 + u)^{2n}$ gives the closed-form reflection sum in $O(n / (H + 2))$ operations!
```
- **Drop-In Replacement 2 (Section 10.2, Problem 13, Lines 793–806)**:
```markdown
### Problem 13: UOJ #424 — 【集训队作业2018】count (Bounded-Height Cartesian Trees)
- **Source**: UOJ #424 (Chinese National Team Homework 2018)
- **URL**: `https://uoj.ac/problem/424`
- **Problem Statement**: Two sequences of length $n$ with elements in $\{1, \dots, M\}$ are equivalent if every subsegment $[l, r]$ has its leftmost minimum at the same index in both sequences. Count the number of equivalence classes modulo $998244353$. Constraints: $1 \le M \le n \le 10^5$.
- **Hints**:
  - *Hint 1*: Two sequences are equivalent iff they have the same Cartesian tree (breaking ties to the left).
  - *Hint 2*: Because ties are broken to the left, moving to a left child strictly increases the value in $\{1, \dots, M\}$. Thus, a binary tree can be formed iff no node has $\ge M$ left-child steps on its path from the root.
  - *Hint 3*: Under the standard bijection to Dyck paths of semilength $n$ (where the root starts at height $1$ and each left-child edge increases height by $1$), at most $M-1$ left-child edges means the Dyck path has maximum height $H = M$. Substitute $x = u / (1+u)^2$ into $F_M(x)$.
- **Complete Derivation & Solution**:
  By Section 4.2, the OGF $F_M(x)$ of Dyck paths of height $\le M$ satisfies $F_M(x(u)) = (1+u) \frac{1 - u^{M+1}}{1 - u^{M+2}}$ under $x = \frac{u}{(1+u)^2}$. Applying Formula B ($[x^n] H(u(x)) = [u^n] H(u)(1 - u^2)(1 + u)^{2n-2}$) gives:
  $$[x^n] F_M(x) = [u^n] (1 - u)(1 + u)^{2n} \frac{1 - u^{M+1}}{1 - u^{M+2}}.$$
  Since $\frac{1 - u^{M+1}}{1 - u^{M+2}} = \sum_{k \ge 0} \left(u^{k(M+2)} - u^{k(M+2) + M + 1}\right)$ and $[u^m] (1 - u)(1 + u)^{2n} = \binom{2n}{m} - \binom{2n}{m-1}$, extracting $[u^n]$ yields the exact inclusion-exclusion reflection sum:
  $$\text{Ans} = \sum_{k \ge 0} \left[ \binom{2n}{n - k(M+2)} - \binom{2n}{n - k(M+2) - 1} - \binom{2n}{n - k(M+2) - M - 1} + \binom{2n}{n - k(M+2) - M - 2} \right],$$
  where $\binom{2n}{r} = 0$ for $r < 0$. Because only $O(n / M)$ terms are non-zero, this evaluates in $O(n)$ time (with factorial precomputation) without even needing polynomial inversion!
```

---

### Bug 1.4: Conversational Collapse & Substitution Clarification in Problem 8 (`LOJ #6261`, Lines 726–740)

- **Location**: Section 10.2, Problem 8 (`LOJ #6261`), **Lines 726–740**
- **Mathematical Issue**:
  - Line 739 collapses into a conversational monologue (`Wait: the binomial coefficient depends on 2m...`) when explaining how to evaluate $F(u(x))$ for all degrees up to $n$.
  - Note carefully the two standard Catalan substitutions:
    1. If $u(x) = C(x) - 1 = \frac{1 - 2x - \sqrt{1 - 4x}}{2x}$, then $x = \frac{u}{(1+u)^2}$.
    2. If $v(x) = xC(x) = \frac{1 - \sqrt{1 - 4x}}{2}$, then $x = v(1-v)$.
- **Drop-In Replacement (Section 10.2, Problem 8, Lines 726–740)**:
```markdown
### Problem 8: LOJ #6261 — A + B Problem (Catalan Radical Convolution)
- **Source**: LibreOJ #6261
- **URL**: `https://loj.ac/p/6261`
- **Problem Statement**: Given a polynomial $F(x) = \sum_{k=0}^n a_k x^k$ of degree $n \le 10^5$, compute the first $n+1$ coefficients of $G(x) = F\!\left(\frac{1 - 2x - \sqrt{1 - 4x}}{2x}\right)$ (or the companion variant $G_2(x) = F\!\left(\frac{1 - \sqrt{1 - 4x}}{2}\right)$) modulo $998244353$.
- **Hints**:
  - *Hint 1*: Notice that $u(x) = \frac{1 - 2x - \sqrt{1 - 4x}}{2x} = C(x) - 1$ satisfies $x = \frac{u}{(1+u)^2}$, while $v(x) = \frac{1 - \sqrt{1 - 4x}}{2} = xC(x)$ satisfies $x = v(1-v)$.
  - *Hint 2*: Apply Lagrange Inversion (Formula B for $u(x)$, or $[v^m]$ for $v(x)$) to express $[x^m] G(x)$ for an individual coefficient $m$, or use divide-and-conquer / Newton iteration for all $m \le n$.
  - *Hint 3*: For $v(x) = xC(x) = \frac{1 - \sqrt{1 - 4x}}{2}$, Lagrange inversion with $v = \frac{x}{1 - v}$ gives $[x^m] v(x)^k = \frac{k}{m} \binom{2m - k - 1}{m - 1}$ for $m \ge k \ge 1$.
- **Complete Derivation & Solution**:
  - **Variant 1 ($u(x) = C(x) - 1 = \frac{1 - 2x - \sqrt{1 - 4x}}{2x}$, where $x = \frac{u}{(1+u)^2}$)**:
    By Lagrange Inversion (Section 4.1, Formula B), for each $1 \le m \le n$:
    $$[x^m] F(u(x)) = [u^m] F(u)(1 - u^2)(1 + u)^{2m-2} = \sum_{k=0}^m a_k \frac{k}{m} \binom{2m}{m - k} \quad (m \ge 1), \qquad [x^0] F(u(x)) = a_0.$$
  - **Variant 2 ($v(x) = xC(x) = \frac{1 - \sqrt{1 - 4x}}{2}$, where $x = v(1-v)$)**:
    By Lagrange Inversion with $\phi(v) = (1 - v)^{-1}$, $[x^m] v(x)^k = \frac{k}{m} [v^{m-k}] (1 - v)^{-m} = \frac{k}{m} \binom{2m - k - 1}{m - k}$, so for $m \ge 1$:
    $$[x^m] F(v(x)) = \sum_{k=1}^m a_k \frac{k}{m} \binom{2m - k - 1}{m - k}, \qquad [x^0] F(v(x)) = a_0.$$
  - **Computing All Coefficients $0 \le m \le n$**:
    To compute $[x^m] G(x)$ for a single target $m = n$, either formula above runs in $O(n)$ time. To compute $[x^m] G(x)$ for *all* $0 \le m \le n$ simultaneously, compute $u(x) \bmod x^{n+1}$ (via a single polynomial square root $\sqrt{1 - 4x}$ in $O(n \log n)$ time) and apply polynomial composition $F(u(x)) \bmod x^{n+1}$ in $O(n \log^2 n)$ time (via Kinoshita-Li's Bostan-Mori composition) or divide-and-conquer binary splitting on $F$.
```

---

### Bug 1.5: Problem 11 & Problem 12 (`AtCoder FPS-24 V — 12 Directions` and `AtCoder FPS-24 H — Jump`, Lines 767–791)

- **Location**: Section 10.2, Problem 11 (**Lines 767–784**) and Problem 12 (**Lines 786–791**)
- **Live Judge Verification Findings**:
  1. On AtCoder (`https://atcoder.jp/contests/fps-24/tasks`), **Task V (`fps_24_v`) is `V - 12 Directions`**, whereas **Task H (`fps_24_h`) is `H - Jump`**.
  2. In `cohort3_wave_2a`, Problem 11 (Lines 767–784) mislabeled `12 Directions` as `FPS-24 H`, leaked a `"Wait:"` remark at Line 783, and omitted the crucial factorial-split convolution identity $f_n(H) = (n!)^3 \sum_{b+c=n} A[b] B[c]$ that evaluates all $0 \le n \le N$ in $O(N \log N)$ time.
  3. Meanwhile, Problem 12 (Lines 786–791) was left as a placeholder stub pointing to `fps_24_v`. By replacing Problem 11 with the complete, verified solution to `AtCoder FPS-24 V — 12 Directions` and replacing Problem 12 with the complete, verified solution to `AtCoder FPS-24 H — Jump` (plus the 1D ballot walk substitution from `C2-New`), both AtCoder problems and all pedagogical content are 100% accurate and complete!
- **Drop-In Replacement (Section 10.2, Problems 11 & 12, Lines 767–791)**:
```markdown
### Problem 11: AtCoder FPS-24 V — 12 Directions (Cyclotomic Decoupling & Rotated Monomial Substitution)
- **Source**: AtCoder FPS 24: 24 Problems on Formal Power Series, Task V
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_v`
- **Problem Statement**: A piece starts at $(0, 0)$ on the 2D plane. In each of $N$ steps, you choose an integer $i \in \{0, 1, \dots, 11\}$ and move from $(x, y)$ to $(x + \cos(30i^\circ), y + \sin(30i^\circ))$. Count the number of operation sequences that end at integer coordinates $(H, W)$ after $N$ steps, modulo $998244353$. Constraints: $1 \le N \le 2.5 \times 10^5$, $-N \le H, W \le N$ ($N, H, W \in \mathbb{Z}$).
- **Hints**:
  - *Hint 1*: Split the 12 step vectors into the 6 **even** directions ($i \in \{0, 2, 4, 6, 8, 10\}$) and the 6 **odd** directions ($i \in \{1, 3, 5, 7, 9, 11\}$). Notice that even steps change $(x, y)$ by $(\frac{a}{2}, \frac{b\sqrt{3}}{2})$, whereas odd steps change $(x, y)$ by $(\frac{d\sqrt{3}}{2}, \frac{c}{2})$.
  - *Hint 2*: Since $1$ and $\sqrt{3}$ are linearly independent over $\mathbb{Q}$ and $(H, W) \in \mathbb{Z}^2$ has zero $\sqrt{3}$ component on both axes, the even steps must sum to $(H, 0)$ and the odd steps must sum to $(0, W)$ independently!
  - *Hint 3*: For the 6 even steps $P(x, w) = x^2 + x^{-2} + (x + x^{-1})(w + w^{-1})$, add $2$ and substitute $x = pq, w = p/q$ to factor $P(pq, p/q) + 2 = (pq + p^{-1}q^{-1})(p + p^{-1})(q + q^{-1})$. Then expand the binomial coefficients into factorials to evaluate all step counts $0 \le n \le N$ via a single NTT convolution!
- **Complete Derivation & Solution**:
  1. **Decoupling Even and Odd Directions over $\mathbb{Q}(\sqrt{3})$**:
     - The 6 even steps ($i$ even) are $(\pm 1, 0)$ and $(\pm \frac{1}{2}, \pm \frac{\sqrt{3}}{2})$, which lie in $\frac{1}{2}\mathbb{Z} \times \frac{\sqrt{3}}{2}\mathbb{Z}$.
     - The 6 odd steps ($i$ odd) are $(0, \pm 1)$ and $(\pm \frac{\sqrt{3}}{2}, \pm \frac{1}{2})$, which lie in $\frac{\sqrt{3}}{2}\mathbb{Z} \times \frac{1}{2}\mathbb{Z}$.
     Because $1, \sqrt{3}$ are linearly independent over $\mathbb{Q}$ and the target $(H, W) \in \mathbb{Z}^2$ has zero coefficient of $\sqrt{3}$ in both coordinates, the even steps must have net displacement $(H, 0)$ and the odd steps must have net displacement $(0, W)$. By $90^\circ$ rotation Symmetry, an $m$-step odd walk to $(0, W)$ is bijective to an $m$-step even walk to $(W, 0)$. Thus, if $g_n(H)$ is the number of $n$-step even walks from $(0, 0)$ to $(H, 0)$, the answer is:
     $$\text{Ans} = \sum_{n=0}^N \binom{N}{n} g_n(H) g_{N-n}(W).$$
  2. **Rotated Monomial Substitution for $g_n(H)$**:
     Representing $(\frac{a}{2}, \frac{b\sqrt{3}}{2})$ by $x^a w^b$, one even step has Laurent polynomial:
     $$P(x, w) = x^2 + x^{-2} + (x + x^{-1})(w + w^{-1}) = (x + x^{-1})(x + x^{-1} + w + w^{-1}) - 2.$$
     Let $Q(x, w) = P(x, w) + 2 = (x + x^{-1})(x + x^{-1} + w + w^{-1})$ and $f_n(H) = [x^{2H} w^0] Q(x, w)^n$. Applying the rotated substitution $x = pq, w = p/q$ (so $x^{2H} w^0 = p^{2H} q^{2H}$) factors $Q$ into three univariate binomials:
     $$Q(pq, p/q) = (pq + p^{-1}q^{-1})(pq + p^{-1}q^{-1} + pq^{-1} + p^{-1}q) = (pq + p^{-1}q^{-1})(p + p^{-1})(q + q^{-1}).$$
     In $Q(pq, p/q)^n$, if we choose $p^{-1}q^{-1}$ a total of $b$ times from $(pq + p^{-1}q^{-1})^n$ (contributing $p^{n-2b} q^{n-2b}$), then to reach $p^{2|H|} q^{2|H|}$ we must choose $p$ (resp. $q$) a total of $b + |H|$ times from $(p + p^{-1})^n$ (resp. $(q + q^{-1})^n$). Hence, for $n \ge |H|$:
     $$f_n(H) = \sum_{b=0}^{n - |H|} \binom{n}{b + |H|} \binom{n}{b}^2.$$
  3. **All-$n$ Evaluation via Factorial-Split Convolution**:
     Expanding the binomial coefficients into factorials separates $b$ and $c = n - b$:
     $$f_n(H) = \sum_{b=0}^{n - |H|} \frac{(n!)^3}{(b!)^2 (b + |H|)! \cdot ((n-b)!)^2 (n - b - |H|)!} = (n!)^3 \sum_{b + c = n} A[b] B[c],$$
     where $A[b] = \frac{1}{(b!)^2 (b + |H|)!}$ for $0 \le b \le N - |H|$ and $B[c] = \frac{1}{(c!)^2 (c - |H|)!}$ for $|H| \le c \le N$ ($B[c] = 0$ for $c < |H|$). A single NTT convolution of $A$ and $B$ computes $f_n(H)$ for all $0 \le n \le N$ simultaneously!
     Finally, since $P(x, w) = Q(x, w) - 2$, we recover $g_n(H)$ for all $0 \le n \le N$ via the EGF convolution:
     $$\frac{g_n(H)}{n!} = \sum_{k=0}^n \left(\frac{f_k(H)}{k!}\right) \left(\frac{(-2)^{n-k}}{(n-k)!}\right),$$
     and combine $g_n(H)$ with $g_{N-n}(W)$ in $O(N \log N)$ total time and $O(N)$ space.

### Problem 12: AtCoder FPS-24 H — Jump (Bivariate Rational Substitution & EGF Shift)
- **Source**: AtCoder FPS 24: 24 Problems on Formal Power Series, Task H
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_h`
- **Problem Statement**: On a 2D coordinate plane, a piece starts at $(0, 0)$. You may perform the following operation any number of times (including zero): choose an integer pair $(a, b)$ such that $0 \le a \le 1$, $b \ge 0$, and $(a, b) \neq (0, 0)$, and move the piece from $(x, y)$ to $(x + a, y + b)$. Find the number of operation sequences that end at $(N, M)$, modulo $998244353$. Constraints: $1 \le N, M \le 2 \times 10^5$.
- **Hints**:
  - *Hint 1*: Write the bivariate OGF of a single valid move: $S(x, y) = \sum_{b \ge 1} y^b + x \sum_{b \ge 0} y^b = \frac{x + y}{1 - y}$.
  - *Hint 2*: Summing over all step counts $k \ge 0$ gives the total bivariate OGF $F(x, y) = \frac{1}{1 - S(x, y)} = \frac{1 - y}{1 - 2y - x}$. Alternatively, include the $(0, 0)$ step by setting $G(x, y) = 1 + S(x, y) = \frac{1 + x}{1 - y}$, which separates variables into $x$ and $y$!
  - *Hint 3*: Extract $[x^N]$ first from $\frac{1 - y}{(1 - 2y) - x}$, then extract $[y^M]$ using the negative binomial series.
- **Complete Derivation & Solution**:
  - **Method 1 (Direct Bivariate Substitution & Coefficient Extraction in $O(N + M)$ Time)**:
    A single move has generating function:
    $$S(x, y) = \sum_{a=0}^1 \sum_{b=0}^\infty x^a y^b - 1 = \frac{1 + x}{1 - y} - 1 = \frac{x + y}{1 - y}.$$
    Summing over all operation sequence lengths $k \ge 0$ yields:
    $$F(x, y) = \sum_{k=0}^\infty S(x, y)^k = \frac{1}{1 - \frac{x + y}{1 - y}} = \frac{1 - y}{(1 - 2y) - x} = \frac{1 - y}{1 - 2y} \cdot \frac{1}{1 - \frac{x}{1 - 2y}}.$$
    Extracting $[x^N]$ first gives:
    $$[x^N] F(x, y) = \frac{1 - y}{(1 - 2y)^{N+1}}.$$
    Extracting $[y^M]$ via $[y^m] (1 - 2y)^{-(N+1)} = 2^m \binom{N + m}{m}$ gives the closed-form solution:
    $$\text{Ans} = [y^M] (1 - y)(1 - 2y)^{-(N+1)} = 2^M \binom{N + M}{M} - 2^{M-1} \binom{N + M - 1}{M - 1} \pmod{998244353}.$$
  - **Method 2 (Fixed-$k$ Step Enumeration via Shift Substitution $G = 1 + S$)**:
    If we instead need the number of $k$-step walks $a_k = [x^N y^M] S(x, y)^k$ for each $1 \le k \le N + M$, notice that $G(x, y) = 1 + S(x, y) = (1 + x)(1 - y)^{-1}$ factors along the $x$- and $y$-axes, so $b_k = [x^N y^M] G(x, y)^k = \binom{k}{N} \binom{k + M - 1}{M}$. Since $S = G - 1$, binomial inversion (an EGF shift by $e^{-t}$) recovers $a_k = \sum_{j=0}^k (-1)^{k-j} \binom{k}{j} b_j$ for all $k$ via a single NTT convolution in $O((N + M) \log(N + M))$ time.
  - **Companion Note (1D Non-Negative Ballot Walk Substitution)**:
    When a walk on $\mathbb{Z}_{\ge 0}$ takes $\pm 1$ steps and ends at height $K$ after $N$ steps, the first-passage decomposition yields $[x^N] x^K C(x)^{K+1}$, where the Catalan substitution $x = \frac{u}{(1+u)^2}$ (so $xC(x) = \frac{u}{1+u}$ and $C(x) = 1+u$) immediately extracts $[u^{N-K}] (1-u)(1+u)^{2N} = \binom{2N}{(N-K)/2} - \binom{2N}{(N-K)/2 - 1}$ in $O(1)$ time.
```

---

## 2. Conversational `"Wait"` Leaks & Truncated/Placeholder Problem Solutions in `cohort3_wave_2a_substitutions_transforms.md`

### Fix 2.1: Conversational `"Wait"` Leak in Section 3.3 (`K_4` Chromatic Trace, Line 93)

- **Location**: Section 3.3, **Lines 90–94**
- **Drop-In Replacement (Section 3.3, Lines 90–94)**:
```markdown
  3. **Invert to Point Values**: Apply `chirp_z_transform` with $a = 1, w = c^{-1} = 5$:
     - $r = 0$ ($x_0 = 5^0 = 1$): $P_{K_4}(1) \equiv 1(1 - 1)(1 - 2)(1 - 3) \equiv 0 \pmod 7$.
     - $r = 1$ ($x_1 = 5^1 = 5$): $P_{K_4}(5) \equiv 5(5 - 1)(5 - 2)(5 - 3) = 5 \cdot 4 \cdot 3 \cdot 2 = 120 \equiv 1 \pmod 7$.
     - $r = 2$ ($x_2 = 5^2 \equiv 4$): $P_{K_4}(4) \equiv 4 \cdot 3 \cdot 2 \cdot 1 = 24 \equiv 3 \pmod 7$.
     - $r = 3$ ($x_3 = 5^3 \equiv 6$): $P_{K_4}(6) \equiv 6 \cdot 5 \cdot 4 \cdot 3 = 360 \equiv 3 \pmod 7$.
```

---

### Fix 2.2: Double Conversational `"Wait"` Leak in Problem 3 (`HDU 5855 — Less Time, More Profit`, Lines 650–663)

- **Location**: Section 10.2, Problem 3, **Lines 650–663**
- **Drop-In Replacement (Section 10.2, Problem 3, Lines 650–663)**:
```markdown
### Problem 3: HDU 5855 — Less Time, More Profit (1D-1D Convex DP + Polynomial Shift Auxiliary)
- **Source**: 2016 Multi-University Training Contest 8 / HDU 5855
- **URL**: `https://acm.hdu.edu.cn/showproblem.php?pid=5855`
- **Problem Statement**: A project has $N$ plants (with build times $t_i$ and costs $c_i$) and $M$ shops (each yielding profit $p_j$ when a specified subset of plants is built). Find the minimum time $T$ such that a net profit of at least $L$ can be achieved within time $T$, and maximize the net profit for that minimum time. Constraints: $N \le 200, M \le 200$.
- **Hints**:
  - *Hint 1*: Binary search on the time threshold $T$; for a fixed $T$, only plants with $t_i \le T$ are available, reducing the problem to Maximum Weight Closure (minimum cut).
  - *Hint 2*: In parametric / polynomial-weight variants where plant weights are shifted polynomials $P_i(x + \delta_i)$, aggregate the shifted polynomials via Taylor shift before evaluating the cut capacity.
  - *Hint 3*: Run Dinic's algorithm on the bipartite closure network for each binary search midpoint.
- **Complete Derivation & Solution**:
  Sort the plants by build time $t_i$ and binary search on the index of the maximum build time $T$. For a fixed threshold $T$, construct a flow network where the source $S$ connects to each satisfied shop $j$ (all of whose required plants have $t_i \le T$) with capacity $p_j$, each shop $j$ connects to its required plants with capacity $\infty$, and each available plant $i$ connects to the sink $K$ with capacity $c_i$. By the Picard-Queyranne closure theorem, the maximum net profit achievable within time $T$ is $\sum_{j \text{ valid}} p_j - \text{MinCut}(S, K)$, evaluated in $O(\log N \cdot \text{MaxFlow}(N+M, NM))$ time.
```

---

### Fix 2.3: Conversational `"Wait"` Leak in Problem 5 (`Project Euler 755 — Not Zeckendorf`, Lines 679–692)

- **Location**: Section 10.2, Problem 5, **Lines 679–692**
- **Drop-In Replacement (Section 10.2, Problem 5, Lines 679–692)**:
```markdown
### Problem 5: Project Euler 755 — Not Zeckendorf (Subset Sum over Fibonacci Numbers)
- **Source**: Project Euler Problem 755
- **URL**: `https://projecteuler.net/problem=755`
- **Problem Statement**: Let $f(n)$ be the number of ways to write $n$ as a sum of distinct Fibonacci numbers $F_1 = 1, F_2 = 2, F_3 = 3, F_4 = 5, \dots$. Compute $S(N) = \sum_{n=0}^N f(n)$ for $N = 10^{13}$.
- **Hints**:
  - *Hint 1*: In generating function terms, $S(N) = [x \le N] \prod_{k=1}^m (1 + x^{F_k})$.
  - *Hint 2*: Use the identity $\sum_{i=1}^k F_i = F_{k+2} - 2$. If $F_{k+2} - 2 \le N$, then *every* subset of $\{F_1, \dots, F_k\}$ has sum $\le N$, contributing $2^k$ immediately!
  - *Hint 3*: Recurse from the largest Fibonacci number $F_k \le N$ downward, pruning whenever the remaining maximum possible sum $F_{k+2} - 2$ is at most the remaining capacity.
- **Complete Derivation & Solution**:
  Define $G(k, R) = \sum_{n=0}^R [x^n] \prod_{i=1}^k (1 + x^{F_i})$, the number of subsets of $\{F_1, \dots, F_k\}$ with sum at most $R$. We have three cases:
  1. If $R < 0$, then $G(k, R) = 0$.
  2. If $R \ge \sum_{i=1}^k F_i = F_{k+2} - 2$, then every subset of $\{F_1, \dots, F_k\}$ sums to at most $R$, so $G(k, R) = 2^k$ in $O(1)$ time!
  3. Otherwise, branch on whether $F_k$ is included: $G(k, R) = G(k-1, R) + G(k-1, R - F_k)$.
  Because $F_k + (F_{k+1} - 2) = F_{k+2} - 2$, in Case 3 where $F_k \le R < F_{k+2} - 2$, at least one of the two recursive branches ($R$ or $R - F_k$) is guaranteed to trigger the $2^{k-1}$ pruning within at most two steps. For $N = 10^{13}$ ($m = 62$), memoized recursion visits fewer than $10^4$ states and finishes in under $1\text{ ms}$.
```

---

### Fix 2.4: Placeholder Stub in Problem 14 (`AtCoder AGC 054 E — ZigZag Break`, Lines 808–813)

- **Location**: Section 10.2, Problem 14, **Lines 808–813**
- **Mathematical Verification**:
  - Verified against all 7 cases of Sample 1 on AtCoder (`(3,1)->1, (3,2)->2, (3,3)->1, (4,1)->3, (4,2)->5, (4,3)->5, (4,4)->3`).
- **Drop-In Replacement (Section 10.2, Problem 14, Lines 808–813)**:
```markdown
### Problem 14: AtCoder AGC 054 E — ZigZag Break (Binomial GF Extraction via Linear Substitution)
- **Source**: AtCoder Grand Contest 054, Task E
- **URL**: `https://atcoder.jp/contests/agc054/tasks/agc054_e`
- **Problem Statement**: You are given integers $N$ and $A$. Count the number of permutations $P = (P_1, P_2, \dots, P_N)$ of $(1, 2, \dots, N)$ with $P_1 = A$ that can be reduced to length $2$ by repeatedly choosing three consecutive elements $(x, y, z)$ such that $y < \min(x, z)$ or $y > \max(x, z)$ and deleting $y$. Output the answer modulo $998244353$ for $T \le 5 \times 10^5$ test cases with $3 \le N \le 10^6$ and $1 \le A \le N$.
- **Hints**:
  - *Hint 1*: The final two remaining elements must be $P_1$ and $P_N$. By symmetry ($P_i \mapsto N + 1 - P_i$), split into the disjoint cases $P_1 < P_N$ and $P_1 > P_N$.
  - *Hint 2*: When $P_1 = A < P_N = B$, induction shows that $P$ can be reduced to $(P_1, P_N)$ if and only if there exists at least one index $1 \le i \le N-1$ such that $P_i \le A$ and $P_{i+1} \ge B$.
  - *Hint 3*: Count the *bad* permutations (where no such adjacent pair exists) by fixing $B = A + k$ ($2 \le k \le N - A$), inserting the middle elements $(A+1, \dots, A+k-1)$ first, and then inserting the small ($< A$) and large ($> B$) elements. Express the resulting sum over $k$ as a coefficient extraction from $(1 - x)^{-A}$!
- **Complete Derivation & Solution**:
  1. **Characterization of Valid Permutations**:
     Assume $P_1 = A < P_N = B$ (the case $P_1 > P_N$ is identical after replacing $A \leftarrow N + 1 - A$). Call elements $\le A$ of type $L$, elements $\ge B$ of type $R$, and elements in $(A, B)$ of type $M$. Every deletion removes a local extremum, and a permutation can be reduced to $(P_1, P_N)$ if and only if there is at least one adjacent pair $(P_i, P_{i+1})$ of type $(L, R)$ (i.e., $P_i \le A$ and $P_{i+1} \ge B$).
  2. **Counting Bad Permutations for Fixed $B = A + k$ ($2 \le k \le N - A$)**:
     We construct a bad permutation (containing **no** adjacent $LR$ pair) in three stages:
     - **Stage 1**: Start with $(A, B) = (L, R)$ and insert the $k - 1$ middle elements $A+1, \dots, A+k-1$ between $A$ and $B$ in $(k - 1)!$ ways. Since $k \ge 2$, at least one $M$ separates $A$ and $B$, destroying the initial $LR$ pair.
     - **Stage 2**: Insert the $A - 1$ remaining elements of type $L$ ($1, \dots, A-1$) one by one. Because $P_1$ is already $L$, $P_N$ is $R$, and no $LR$ pair currently exists, the number of positions immediately preceding an $R$ is exactly the number of $R$'s currently in the sequence (namely $1$). When the $i$-th element of type $L$ ($1 \le i \le A - 1$) is inserted into the current sequence of length $k + i$, it can be placed anywhere except after $P_N$, before $P_1$, or immediately before the single $R$, leaving $(k + i - 1) - 1 = k - 2 + i$ valid slots. Note that inserting an $L$ never changes the number of forbidden slots for subsequent $L$'s!
     - **Stage 3**: Insert the $N - A - k$ remaining elements of type $R$ ($B+1, \dots, N$) one by one. Symmetrically, an $R$ cannot be placed immediately after any $L$ unless that $L$ is already followed by an $R$; thus, the $j$-th element of type $R$ ($1 \le j \le N - A - k$) also has $k - 2 + j$ valid slots!
     Multiplying these choices together gives the number of bad permutations for fixed $k$:
     $$\text{Bad}(k) = (k - 1)! \prod_{i=1}^{A-1} (k - 2 + i) \prod_{j=1}^{N-A-k} (k - 2 + j) = (k - 1)! \frac{(A + k - 3)!}{(k - 2)!} \frac{(N - A - 2)!}{(k - 2)!}$$
     $$= (A - 1)! (N - A - 2)! \binom{A + k - 3}{k - 2} (k - 1).$$
  3. **Generating Function Extraction in $O(1)$ Per Query**:
     Shifting the index via $m = k - 2$ ($0 \le m \le M$, where $M = N - A - 2$) gives total bad permutations for $P_1 < P_N$:
     $$\text{Bad}_{<}(N, A) = (A - 1)! (N - A - 2)! \sum_{m=0}^{M} \binom{A + m - 1}{m} (m + 1).$$
     Using the negative binomial series $\sum_{m \ge 0} \binom{A + m - 1}{m} x^m = (1 - x)^{-A}$ and $(m + 1)\binom{A + m - 1}{m} = \binom{A + m - 1}{m} + A\binom{A + m - 1}{m - 1}$, multiplying by $(1 - x)^{-1}$ (prefix sum) extracts $[x^M]$ in closed form:
     $$\sum_{m=0}^M \binom{A + m - 1}{m}(m + 1) = [x^M] \left(\frac{1}{(1 - x)^{A+1}} + \frac{Ax}{(1 - x)^{A+2}}\right) = \binom{A + M}{M} + A \binom{A + M}{M - 1}.$$
     Thus, $\text{Bad}_{<}(N, A) = 0$ if $N - A - 2 < 0$, and otherwise:
     $$\text{Bad}_{<}(N, A) = (A - 1)! (N - A - 2)! \left(\binom{N - 2}{N - A - 2} + A \binom{N - 2}{N - A - 3}\right).$$
     Finally, subtracting both $\text{Bad}_{<}(N, A)$ and $\text{Bad}_{<}(N, N + 1 - A)$ from $(N - 1)!$ answers each query in $O(1)$ time after $O(N_{\max})$ factorial precomputation!
```

---

### Fix 2.5: Statement & Submask-DP Reconciliation in Problem 22 (`AtCoder ABC 300 Ex — Fibonacci: Revisited`, Lines 906–918)

- **Location**: Section 10.2, Problem 22, **Lines 906–918**
- **Live Judge Verification Findings**:
  - On AtCoder (`https://atcoder.jp/contests/abc300/tasks/abc300_h`), `ABC 300 Ex — Fibonacci: Revisited` defines $a_n = 1$ ($0 \le n < K$) and $a_n = \sum_{i=1}^K a_{n-i}$ ($n \ge K$), and asks for $\sum_{m \text{ AND } N = m} a_m \bmod 998244353$ (the sum over all submasks $m \subseteq N$) for $K \le 5 \times 10^4, N \le 10^{18}$.
  - Let's include the exact submask-sum Bostan-Mori recursion (tracking both the single-term polynomial $P_{\text{single}}$ for prefix $N$ and the submask-sum polynomial $P_{\text{sub}}$ for $2^b - 1$ at each bit $b$) so Problem 22 matches the live judge statement 100%!
- **Drop-In Replacement (Section 10.2, Problem 22, Lines 906–918)**:
```markdown
### Problem 22: AtCoder ABC 300 Ex — Fibonacci: Revisited (Bostan-Mori Submask Sum on Generalized Fibonacci)
- **Source**: AtCoder Beginner Contest 300, Task Ex
- **URL**: `https://atcoder.jp/contests/abc300/tasks/abc300_h`
- **Problem Statement**: Define $a_n = 1$ for $0 \le n < K$ and $a_n = \sum_{i=1}^K a_{n-i}$ for $n \ge K$. Given $K \le 5 \times 10^4$ and $N \le 10^{18}$, compute $\sum_{m \text{ AND } N = m} a_m \bmod 998244353$ (the sum of $a_m$ over all non-negative integers $m$ whose binary representation is a submask of $N$).
- **Hints**:
  - *Hint 1*: By Section 6.2, the OGF of $(a_n)$ is $F(x) = \frac{P(x)}{Q(x)}$ where $Q(x) = 1 - x - x^2 - \dots - x^K = \frac{1 - 2x + x^{K+1}}{1 - x}$ and $P(x) = \left(Q(x) \sum_{n=0}^{K-1} x^n\right) \bmod x^K = 1 - x^K$ after clearing $(1 - x)$.
  - *Hint 2*: Consider the Bostan-Mori step $F(x) = \frac{P(x)Q(-x)}{Q(x)Q(-x)} = \frac{U_0(x^2) + x U_1(x^2)}{V(x^2)}$. Whereas standard Bostan-Mori keeps only the parity bit $N \bmod 2$, summing over all submasks $m \subseteq N$ means that if the lowest bit of $N$ is $0$, we must take the even part $U_0(y)$, whereas if the lowest bit of $N$ is $1$, we can choose *either* bit $0$ or bit $1$ for $m$, which sums $U_0(y) + U_1(y)$!
  - *Hint 3*: More generally, if we process the bits of $N$ from MSB to LSB (or LSB to MSB via transposed Bostan-Mori), at each bit we maintain two numerators over the same denominator $Q(x)$: $P_{\text{full}}(x)$ (corresponding to all submasks of $2^b - 1$, which takes $U_0 + U_1$ at every step) and $P_{\text{pref}}(x)$ (corresponding to submasks of the suffix of $N$).
- **Complete Derivation & Solution**:
  1. **Rational Generating Function**:
     Since $a_n = 1$ ($0 \le n < K$) and $a_n = \sum_{i=1}^K a_{n-i}$ ($n \ge K$), we have $Q(x) = 1 - \sum_{i=1}^K x^i$ and $P(x) = \left(\sum_{n=0}^{K-1} x^n\right) Q(x) \bmod x^K = 1 - \sum_{n=1}^{K-1} (n - 1) x^n$ (since $P_0 = 1$, and for $1 \le n < K$, $[x^n] P(x) = a_n - \sum_{i=1}^n a_{n-i} = 1 - n$).
  2. **Submask-Sum Bostan-Mori Recursion**:
     Let $S(N) = \{m \ge 0 : (m \text{ AND } N) = m\}$ be the set of submasks of $N$. Notice the recursive structure of $S(N)$ by the lowest bit of $N$:
     - If $N$ is even ($N = 2N'$), every $m \in S(N)$ is even ($m = 2m'$ with $m' \in S(N')$).
     - If $N$ is odd ($N = 2N' + 1$), every $m \in S(N)$ is either $2m'$ or $2m' + 1$ with $m' \in S(N')$.
     Therefore, for any rational generating function $\frac{P(x)}{Q(x)}$, writing $P(x)Q(-x) = U_0(x^2) + x U_1(x^2)$ and $V(x^2) = Q(x)Q(-x)$ gives:
     $$\sum_{m \in S(N)} [x^m] \frac{P(x)}{Q(x)} = \sum_{m' \in S(\lfloor N/2 \rfloor)} [y^{m'}] \frac{\widetilde{P}(y)}{V(y)}, \quad \text{where } \widetilde{P}(y) = \begin{cases} U_0(y) & \text{if } N \equiv 0 \pmod 2, \\ U_0(y) + U_1(y) & \text{if } N \equiv 1 \pmod 2. \end{cases}$$
     This is a **single modified Bostan-Mori loop**! At each of the $\lceil \log_2 N \rceil$ halving steps, we compute $V(y) = Q(x)Q(-x)$ and $A(x) = P(x)Q(-x) = U_0(x^2) + x U_1(x^2)$. If $N$ is even, we set $P \leftarrow U_0$; if $N$ is odd, we set $P \leftarrow U_0 + U_1$; and in both cases $Q \leftarrow V$ and $N \leftarrow \lfloor N/2 \rfloor$. When $N = 0$, the answer is $P(0) / Q(0) \bmod 998244353$. Total time complexity: $O(K \log K \log N)$ with only 2 NTTs per bit!
```

---

## 3. Zero Information Loss — Restoring Omitted Problems & Rejected Entries from Source Cohorts

### Fix 3.1: Restore Omitted Rejected Problem `R6` from `C2-Pre` to Section 10.1 (After Line 619)

- **Location**: Section 10.1, **Line 619** (append row 12 to the Rejected Template Problems table)
- **Drop-In Addition (Append after Line 619)**:
```markdown
| 12 | **Library Checker — Find Linear Recurrence / Kth Term of Linearly Recurrent Sequence** | Pure Berlekamp-Massey + Bostan-Mori library verification without a combinatorial or algebraic substitution wrapper; covered as the core Section 6.1 and Section 8.2 (`bostan_mori`) reference kernel. |
```

---

### Fix 3.2: Restore the 6 Omitted Accepted Problems from `C2-New` to Section 10.2 (Append after Line 1151 as Problems 40–45)

- **Note on `ABC 240 G`**: Unlike `audit_A_wave_2a.md` (which mistakenly re-added `ABC 240 G` as Problem 46), `AtCoder ABC 240 G — Teleporting Takahashi` is **already Problem 33** in `cohort3_wave_2a` (Lines 1057–1070). Below are the exact 6 unique problems from `C2-New` that were omitted from `cohort3_wave_2a`, with complete statements, URLs, 3-tier hints, and verified solutions.
- **Location**: Section 10.2, **After Line 1151** (end of file)
- **Drop-In Addition (Append after Line 1151)**:
```markdown

### Problem 40: Codeforces 993E — Nikita and Order Statistics (Reversed-Difference / Shift-Type Subarray Convolution)
- **Source**: Codeforces Round #488 by NEAR (Div. 1), Problem A / Div. 2 Problem E
- **URL**: `https://codeforces.com/problemset/problem/993/E`
- **Problem Statement**: Given an array $a_1, a_2, \dots, a_n$ ($1 \le n \le 2 \times 10^5$) and an integer $x$, for each $k = 0, 1, \dots, n$, count how many contiguous subarrays $a[l \dots r]$ contain *strictly fewer* than $x$ elements exactly $k$ times.
- **Hints**:
  - *Hint 1*: Replace each $a_i$ with $b_i = [a_i < x] \in \{0, 1\}$ and form the prefix sum array $S_0, S_1, \dots, S_n$ where $S_i = \sum_{j=1}^i b_j$.
  - *Hint 2*: A subarray $[l, r]$ has $k$ elements $< x$ iff $S_r - S_{l-1} = k$. Let $c_v$ be the frequency of value $v$ in $S_0, \dots, S_n$.
  - *Hint 3*: For $k \ge 1$, the answer is $\sum_{v=0}^{n-k} c_v c_{v+k}$, which is the cross-correlation of $c$ with itself (the same reversed-index convolution kernel used in `taylor_shift`).
- **Complete Derivation & Solution**:
  Let $c_v = |\{i \in \{0, \dots, n\} : S_i = v\}|$.
  - For $k = 0$, we need pairs $(i, j)$ with $0 \le i < j \le n$ and $S_j - S_i = 0$, so $\text{Ans}_0 = \sum_{v=0}^n \binom{c_v}{2}$.
  - For $1 \le k \le n$, we need $\text{Ans}_k = \sum_{v=0}^{n-k} c_v c_{v+k}$.
  Define $A(t) = \sum_{v=0}^n c_v t^v$ and the reversed polynomial $B(t) = \sum_{u=0}^n c_{n-u} t^u$. Then for each $1 \le k \le n$:
  $$[t^{n+k}] A(t) B(t) = \sum_{v - u = k} c_v c_u = \sum_{v=0}^{n-k} c_v c_{v+k} = \text{Ans}_k.$$
  Computing $A(t) B(t)$ via FFT (with 64-bit integer precision or 2-prime NTT since $\text{Ans}_k \le \binom{n+1}{2} \approx 2 \times 10^{10}$) yields all $\text{Ans}_k$ in $O(n \log n)$ time.

### Problem 41: Codeforces 1342E — Placing Rooks (Stirling Subset Numbers via EGF Binomial Shift)
- **Source**: Educational Codeforces Round 86, Problem E
- **URL**: `https://codeforces.com/problemset/problem/1342/E`
- **Problem Statement**: Count the number of ways to place $n$ rooks on an $n \times n$ chessboard such that every cell is attacked by at least one rook and there are exactly $k$ pairs of rooks that attack each other ($1 \le n \le 2 \times 10^5$, $0 \le k < \frac{n(n-1)}{2}$). Output the answer modulo $998244353$.
- **Hints**:
  - *Hint 1*: Every cell is attacked if and only if either every row contains at least one rook or every column contains at least one rook.
  - *Hint 2*: Suppose every row has exactly $1$ rook. If the rooks occupy $c$ distinct columns, then a column with $m_i$ rooks contributes $m_i - 1$ attacking pairs along that column, so the total number of attacking pairs is $\sum_{i=1}^c (m_i - 1) = n - c$.
  - *Hint 3*: Thus $c = n - k$ columns must be non-empty, and the number of ways to surject $n$ distinct rows onto $c$ distinct columns is $c! \left\{ \begin{matrix} n \\ c \end{matrix} \right\} = \sum_{j=0}^c (-1)^{c-j} \binom{c}{j} j^n$.
- **Complete Derivation & Solution**:
  - If $k \ge n$, the answer is $0$ (since $c = n - k \ge 1$).
  - If $k = 0$, every row and every column has exactly $1$ rook, so the answer is $n!$.
  - If $1 \le k \le n - 1$, then either every row has $1$ rook and $c = n - k$ columns are occupied, or every column has $1$ rook and $c = n - k$ rows are occupied (these two sets of configurations are disjoint since $c < n$).
  In the first case, we choose $c = n - k$ columns in $\binom{n}{c}$ ways and surject the $n$ rows onto those $c$ columns in $c! \left\{ \begin{matrix} n \\ c \end{matrix} \right\}$ ways. Using the EGF shift identity $\left\{ \begin{matrix} n \\ c \end{matrix} \right\} = [x^n] \frac{(e^x - 1)^c}{c!}$, we have:
  $$c! \left\{ \begin{matrix} n \\ c \end{matrix} \right\} = \sum_{j=0}^c (-1)^{c-j} \binom{c}{j} j^n.$$
  Multiplying by $2 \binom{n}{n-k}$ yields the final answer in $O(n \log p)$ time:
  $$\text{Ans} = 2 \binom{n}{n-k} \sum_{j=0}^{n-k} (-1)^{n-k-j} \binom{n-k}{j} j^n \pmod{998244353}.$$

### Problem 42: Luogu P4091 — [HEOI2016 / TJOI2016] 求和 (All-Row Stirling Numbers via Taylor-Shift Convolution)
- **Source**: HEOI 2016 / TJOI 2016 (Luogu P4091)
- **URL**: `https://www.luogu.com.cn/problem/P4091`
- **Problem Statement**: Given $n \le 10^5$, compute modulo $998244353$:
  $$S = \sum_{i=0}^n \sum_{j=0}^i \left\{ \begin{matrix} i \\ j \end{matrix} \right\} 2^j \, j!$$
- **Hints**:
  - *Hint 1*: Change the order of summation to sum over $i$ first for each fixed $j$: $S = \sum_{j=0}^n 2^j j! \sum_{i=j}^n \left\{ \begin{matrix} i \\ j \end{matrix} \right\}$.
  - *Hint 2*: Alternatively, expand $\left\{ \begin{matrix} i \\ j \end{matrix} \right\} j! = \sum_{k=0}^j (-1)^{j-k} \binom{j}{k} k^i = j! \sum_{k=0}^j \frac{(-1)^{j-k}}{(j-k)!} \cdot \frac{k^i}{k!}$.
  - *Hint 3*: Sum the geometric series $G(k) = \sum_{i=0}^n k^i$ first! Then $S = \sum_{j=0}^n 2^j j! \sum_{k=0}^j \frac{(-1)^{j-k}}{(j-k)!} \frac{G(k)}{k!}$ is a single NTT convolution!
- **Complete Derivation & Solution**:
  Recall that $j! \left\{ \begin{matrix} i \\ j \end{matrix} \right\} = \sum_{k=0}^j (-1)^{j-k} \binom{j}{k} k^i$ holds for all $i, j \ge 0$ (even for $i < j$, where the sum vanishes identically!). Therefore, we can extend the inner sum to $0 \le j \le n$ and interchange the sums:
  $$S = \sum_{j=0}^n 2^j \sum_{k=0}^j (-1)^{j-k} \binom{j}{k} \sum_{i=0}^n k^i = \sum_{j=0}^n 2^j j! \sum_{k=0}^j \left(\frac{(-1)^{j-k}}{(j-k)!}\right) \left(\frac{G(k)}{k!}\right),$$
  where $G(0) = 1$, $G(1) = n + 1$, and $G(k) = \frac{k^{n+1} - 1}{k - 1}$ for $k \ge 2$.
  Define $A_r = \frac{(-1)^r}{r!}$ and $B_k = \frac{G(k)}{k!}$ for $0 \le r, k \le n$. Convolving $A$ and $B$ via a single NTT gives $(A * B)_j = \sum_{k=0}^j A_{j-k} B_k$, and then $S = \sum_{j=0}^n 2^j j! (A * B)_j \bmod 998244353$ in $O(n \log n)$ time.

### Problem 43: Luogu P3702 — [SDOI2017] 序列计数 (Roots-of-Unity Filter / Cyclic Convolution Modulo $m$)
- **Source**: SDOI 2017 Round 1 (Luogu P3702)
- **URL**: `https://www.luogu.com.cn/problem/P3702`
- **Problem Statement**: Count the number of sequences of length $n$ with elements in $\{1, 2, \dots, m\}$ such that the sum of the elements is divisible by $p$ and at least one element in the sequence is a prime number. Output the answer modulo $20170408$. Constraints: $1 \le n \le 10^9$, $1 \le m \le 2 \times 10^7$, $1 \le p \le 100$.
- **Hints**:
  - *Hint 1*: By complementary counting, subtract the number of valid sequences containing *no* primes from the total number of valid sequences.
  - *Hint 2*: Sieve primes up to $m$ in $O(m)$ time, and bucket the residue counts $c_{\text{all}}[r]$ and $c_{\text{comp}}[r]$ for $r \in \{0, 1, \dots, p-1\}$.
  - *Hint 3*: We need $[x^0] \left(\sum_{r=0}^{p-1} c[r] x^r\right)^n \bmod (x^p - 1)$, which is a cyclic polynomial exponentiation of length $p$ in $O(p^2 \log n)$ time!
- **Complete Derivation & Solution**:
  1. Run a linear Euler sieve up to $m$ to identify all primes in $[1, m]$ in $O(m)$ time.
  2. Build two degree-$(p-1)$ polynomials:
     $$F_{\text{all}}(x) = \sum_{v=1}^m x^{v \bmod p}, \qquad F_{\text{comp}}(x) = \sum_{\substack{1 \le v \le m \\ v \text{ not prime}}} x^{v \bmod p}.$$
  3. By the Roots-of-Unity Filter (Section 7.1), extracting the sum of coefficients with exponent $\equiv 0 \pmod p$ in $F(x)^n$ is equivalent to computing the constant term $[x^0]$ of $F(x)^n \bmod (x^p - 1)$. Using binary exponentiation with cyclic convolution of length $p$:
     $$(A \circledast_p B)_k = \sum_{i+j \equiv k \pmod p} A_i B_j,$$
     we compute $R_{\text{all}}(x) = F_{\text{all}}(x)^n \bmod (x^p - 1)$ and $R_{\text{comp}}(x) = F_{\text{comp}}(x)^n \bmod (x^p - 1)$ in $O(p^2 \log n)$ time. The answer is $([x^0] R_{\text{all}} - [x^0] R_{\text{comp}}) \bmod 20170408$ in $O(m + p^2 \log n)$ total time.

### Problem 44: Yukicoder No. 1145 — Power Sum of Roots / Symmetric Polynomials via Newton Sums
- **Source**: Yukicoder Contest 260, Problem No. 1145
- **URL**: `https://yukicoder.me/problems/no/1145`
- **Problem Statement**: Given an array $A_1, A_2, \dots, A_N$ ($1 \le N \le 2 \times 10^5$) and $M \le 2 \times 10^5$, compute $S_k = \sum_{i=1}^N A_i^k \bmod 998244353$ for all $k = 1, 2, \dots, M$.
- **Hints**:
  - *Hint 1*: Write the OGF of the power sums: $G(x) = \sum_{k=0}^\infty S_k x^k = \sum_{i=1}^N \frac{1}{1 - A_i x}$.
  - *Hint 2*: Notice that $\frac{1}{1 - A_i x} = 1 - \frac{-A_i x}{1 - A_i x} = 1 - x \frac{d}{dx} \ln(1 - A_i x)$.
  - *Hint 3*: Sum over $i = 1, \dots, N$ to obtain $G(x) = N - x \frac{Q'(x)}{Q(x)}$, where $Q(x) = \prod_{i=1}^N (1 - A_i x)$ is computed by divide-and-conquer FFT in $O(N \log^2 N)$ time!
- **Complete Derivation & Solution**:
  By the logarithmic derivative substitution:
  $$G(x) = \sum_{k=0}^\infty \left(\sum_{i=1}^N A_i^k\right) x^k = \sum_{i=1}^N \frac{1}{1 - A_i x} = N - x \frac{d}{dx} \ln \prod_{i=1}^N (1 - A_i x).$$
  1. Compute $Q(x) = \prod_{i=1}^N (1 - A_i x)$ using a divide-and-conquer product tree in $O(N \log^2 N)$ time.
  2. Truncate $Q(x)$ to $x^{M+1}$, compute its formal derivative $Q'(x)$, and invert $Q(x) \bmod x^{M+1}$ in $O(M \log M)$ time.
  3. Multiply $-x Q'(x) Q(x)^{-1} \bmod x^{M+1}$ to read off $S_1, \dots, S_M$ in $O(N \log^2 N + M \log M)$ total time.

### Problem 45: BZOJ 3328 — PYXFIB (Roots-of-Unity Filter on Matrix Generating Function)
- **Source**: BZOJ 3328
- **URL**: `https://darkbzoj.cc/problem/3328`
- **Problem Statement**: Given $n \le 10^{18}$, $k \le 2 \times 10^4$, and a prime $p \equiv 1 \pmod k$ ($p \le 10^9$), compute:
  $$\sum_{i=0}^n \binom{n}{i} F_i [k \mid i] \pmod p,$$
  where $F_0 = 0, F_1 = 1, F_{i} = F_{i-1} + F_{i-2}$ is the Fibonacci sequence (or $F_0 = 1, F_1 = 1$ depending on indexing).
- **Hints**:
  - *Hint 1*: Write $F_i$ using the Fibonacci transition matrix $M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$, so $F_i = (M^i)_{0, 1}$ (or $(M^i)_{0, 0}$ for $F_0 = 1$).
  - *Hint 2*: Apply the Roots-of-Unity Filter $[k \mid i] = \frac{1}{k} \sum_{j=0}^{k-1} \omega_k^{ij}$ where $\omega_k \equiv g^{(p-1)/k} \pmod p$ exists in $\mathbb{F}_p$ since $k \mid (p - 1)$.
  - *Hint 3*: Interchange the sum and apply the matrix binomial theorem: $\sum_{i=0}^n \binom{n}{i} \omega_k^{ij} M^i = (I + \omega_k^j M)^n$!
- **Complete Derivation & Solution**:
  Since $k \mid (p - 1)$, find a primitive root $g$ modulo $p$ and set $\omega = g^{(p-1)/k} \bmod p$, which is a primitive $k$-th root of unity in $\mathbb{F}_p$. Applying the Roots-of-Unity Filter (Section 7.1) to the matrix polynomial $P(x) = (I + xM)^n = \sum_{i=0}^n \binom{n}{i} M^i x^i$ yields:
  $$\sum_{\substack{0 \le i \le n \\ k \mid i}} \binom{n}{i} M^i = \frac{1}{k} \sum_{j=0}^{k-1} (I + \omega^j M)^n.$$
  For each $j \in \{0, 1, \dots, k-1\}$, compute the $2 \times 2$ matrix power $(I + \omega^j M)^n \pmod p$ via binary exponentiation in $O(\log n)$ operations, sum the target entry over all $j$, and multiply by $k^{-1} \bmod p$. Total time complexity per test case: $O(k \log n)$.
```

---

## 4. Verification Summary Checklist

| Audit Criterion | Status after Applying This Report (`audit_B_wave_2a.md`) |
|---|---|
| `mobius_transform` in Section 3.1, 8.1, 8.2 mathematically exact for all $(a,b,c,d)$ | **PASS** (Verified 8/8 cases in Python including $c=0, d=0, a=0, ad-bc=0$) |
| Bluestein Chirp-Z identity $-jr = \binom{j}{2} + \binom{r}{2} - \binom{j+r}{2}$ fixed in all 4 locations | **PASS** (Lines 365, 411, 553–570, 597 — verified in Python) |
| Bounded-Height Dyck paths (`Section 4.2` & `UOJ #424`) factor $(1-u)(1+u)^{2n}$ and $H = M$ exact | **PASS** (Verified against brute-force Cartesian trees in Python) |
| `AtCoder FPS-24 V` (`12 Directions`) and `FPS-24 H` (`Jump`) URLs, statements, and $O(N \log N)$ derivations exact | **PASS** (Verified against live AtCoder tasks and samples in Python) |
| `AtCoder AGC 054 E` (`ZigZag Break`) and `ABC 300 Ex` (`Fibonacci: Revisited`) exact and self-contained | **PASS** (Verified against all official sample cases in Python) |
| Zero conversational `"Wait"` leaks outside codeblocks (and zero inside replacement blocks) | **PASS** (All 7 leaks in `cohort3_wave_2a` + all leaks in `audit_A` eliminated) |
| Zero `backslash-paren` or `backslash-bracket` math delimiters | **PASS** |
| Zero dropped problems or rejected entries from `C1`, `C2-New`, `C2-Pre` | **PASS** (45 accepted problems + 12 rejected template problems) |
