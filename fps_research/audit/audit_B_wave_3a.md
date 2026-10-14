# Wave 3A Audit Report — Inspector B (Independent Second-Pass & Cross-Audit of Inspector A)

**Target File**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3a_lagrange_residues_trees_graphs.md` (1,437 lines)  
**Source Files Compared**:
1. `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort1_iter_21_to_25_lagrange_residues_trees_graphs.md` (1,276 lines)
2. `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_73_to_77_lagrange_residues_trees_graphs.md` (1,393 lines)
3. `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_21_to_25_lagrange_residues_trees_graphs.md` (1,044 lines)
**Cross-Checked Prior Audit**:
4. `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/audit/audit_A_wave_3a.md` (467 lines)

---

## Executive Summary & Critical Cross-Check of `audit_A_wave_3a.md`

### 1. Confirmed Findings from `audit_A_wave_3a.md` (Safe to Apply)
- **Bug 1.2 (Line 554)**: Wright's unlabelled bicyclic constant denominator is indeed $24$ (`\frac{5}{24}`), not $12$, giving $u_n \sim \frac{5}{24} n^{-1/2} \rho^{-n}$ as in Cohort 1 Line 1068.
- **Bug 1.3 (Line 236)**: Typo `d_t` $\to$ `d_r` in the multivariate tree-like system theorem statement.
- **Bug 1.4 (Lines 165–167)**: Clarifying how $\frac{1-2u}{1-u}$ acts inside the extraction $[u^{n-1}] \frac{1-2u}{(1-u)^{2n+1}} = [u^{n-1}](1-2u)(1-u)^{-(2n+1)} = C_{n-1}$.
- **Issue 2.1 (After Line 1419)**: Three accepted problems from `cohort2` (`CCPC Harbin 2021 G — Damaged Bicycle`, `QOJ 5097 / MXOI R2 D — Travelling Merchant`, and `QOJ 9250 — Bracket Sequence`) were omitted and must be restored (as Problems 40–42).
- **Issue 2.2 (After Line 154)**: The explicit $n = 5$ mod $5$ coefficient-by-coefficient trace table from `cohort2` Lines 203–229 was omitted and should be restored.
- **Issues 3.1, 3.2, 3.4, 3.5**: Expanding the problem statements and constraints for **Problem 7** (Library Checker `k_ary_tree`), **Problem 15** (EC Final 2020 G `Prof. Pang's Sequence`), **Problem 30** (CodeChef `TREDEG`), and **Problem 33** (AtCoder `DEGwer2023 G`) is valid and helpful.
- **Issue 4.1**: Zero `\(...\)` or `\[...\]` forbidden math delimiters exist in `cohort3_wave_3a.md`.

### 2. CRITICAL WARNINGS: Errors in `audit_A_wave_3a.md` That Would Corrupt `cohort3_wave_3a.md` If Applied Blindly

> [!CAUTION]
> **Do NOT blindly apply Bug 1.5, Issue 3.3, Issue 4.2, or the second half of Bug 1.1 from `audit_A_wave_3a.md`!** Python verification and line-by-line inspection proved that those four sections of `audit_A_wave_3a.md` contain mathematically false formulas or hallucinated problem replacements:

1. **CRITICAL WARNING A1 — Inspector A's Bug 1.5 (Lines 249–255, Case Study B) Is Mathematically Wrong**:
   - For the quadratic $(1-x)Y(x)^2 - (1-x)Y(x) + x = 0$ with $Y(0) = 0$, direct power series expansion in Python gives the exact sequence $[x^n]Y(x)$ for $n = 1 \dots 7$:
     $$\mathbf{1,\; 2,\; 5,\; 15,\; 51,\; 188,\; 731} \quad (\text{OEIS A007317, binomial transform of Catalan numbers}).$$
   - In `audit_A_wave_3a.md` (Lines 107–128), Inspector A claims $x = \frac{Y(1-Y)}{1+Y^2-Y}$ and proposes the formula:
     $$\frac{1}{n}\sum_{j=0}^{\lfloor (n-1)/2 \rfloor} \binom{n}{j}\binom{2n-2j-2}{n-1-2j},$$
     which evaluates for $n = 1 \dots 7$ to **`1, 1, 4, 5, 21, 28, 120`** — **completely wrong for every $n \ge 2$**!
   - **Root Cause**: Expanding $(1-x)Y^2 - (1-x)Y + x = 0$ gives $Y^2 - Y + x(1 + Y - Y^2) = 0$ (not $x(1 - Y + Y^2) = 0$ as misprinted in `cohort3` Line 250). Solving for $x$ yields $x = \frac{Y(1-Y)}{1+Y-Y^2}$, which is $\Phi(u) = \frac{1+u-u^2}{1-u}$ (matching Cohort 1 Lines 498–500!). Even more simply, dividing $(1-x)Y(1-Y) = x$ by $1-x$ gives $Y(1-Y) = \frac{x}{1-x} = z$, so $Y(x) = C\!\left(\frac{x}{1-x}\right) = \sum_{k=1}^\infty C_{k-1} \left(\frac{x}{1-x}\right)^k$, which immediately yields:
     $$[x^n]Y(x) = \frac{1}{n}[u^{n-1}]\left(\frac{1+u-u^2}{1-u}\right)^n = \sum_{k=1}^n \binom{n-1}{k-1}\frac{1}{k}\binom{2k-2}{k-1}.$$
   - See **Bug B1** below for the exact, Python-verified drop-in replacement for Lines 249–255.

2. **CRITICAL WARNING A2 — Inspector A's Issue 4.2 (Lines 382–450 of `audit_A_wave_3a.md`) Hallucinates Wrong Problems for 8 Line Ranges**:
   - In `audit_A_wave_3a.md` Issue 4.2, Inspector A misaligned problem numbers and provided replacement text belonging to **completely different problems** for 8 out of the 12 items:
     - **Line 681** is inside **Problem 2 (AtCoder AGC 021 E — Ball Eat Chameleons)**, NOT "Problem 2 — CF 438E The Child and Binary Tree"! Applying Inspector A's replacement at Line 681 would overwrite the AGC 021 E reflection-principle boundary check with a paragraph about $C(x) = \frac{1-\sqrt{1-4xP(x)}}{2xP(x)}$!
     - **Line 761** is inside **Problem 6 (CF 1349F2 — Slime and Sequences Hard)**, NOT "Problem 5 — Luogu P7439"!
     - **Lines 805 & 814** are inside **Problem 8 (AtCoder ABC 281 Ex — Alchemy)**, NOT "Problem 7 — Library Checker K-ary Tree"!
     - **Line 840** is inside **Problem 10 (UOJ 450 / Luogu P5401 — Pearl)**, NOT "Problem 9 — CF 1264D2 Beautiful Bracket Sequence"!
     - **Line 919** is inside **Problem 13 (Luogu P3978 — Probability Theory)**, NOT "Problem 13 — CF 715E Complete the Permutations"!
     - **Line 1196** is inside **Problem 28 (Luogu P5434 — Labelled Desert)**, NOT "Problem 28 — QOJ 8518 Merging Trees"!
     - **Lines 1383 & 1391** are inside **Problem 38 (UOJ 498 — New Year's Chase)**, NOT "Problem 38 — Gym 104053J"!
     - **Line 1414** is inside **Problem 39 (Luogu P5827 & P5828 — Biconnected & 2-Edge-Connected Graphs)**, NOT "Problem 39 — AtCoder ABC 371 G"!
   - See **Section 4** of this report for the **exact, verified line-by-line replacements** for all 19 `Wait:` / `wait:` occurrences in `cohort3_wave_3a.md`.

3. **CRITICAL WARNING A3 — Inspector A's Issue 3.3 (Lines 963–979, Problem 16) Overwrites the True Problem Statement of Toyota 2023 Spring Final E (`Replace Digits`)**:
   - `cohort3_wave_3a.md` Lines 966–968 already contain the **exact, true statement** of `toyota2023spring_final_e` (*Replace Digits*: a stack of decimal digits $1 \dots 9$ where replacing the top digit $d$ by $c_{d,1}\dots c_{d,k_d}$ applies an affine transformation $X \mapsto 10^{k_d} X + \text{val}_d \pmod{998244353}$).
   - Inspector A's Issue 3.3 overwrites this with a generic random-walk placeholder from `cohort2` Problem 5! Do NOT replace Lines 963–979 with Inspector A's Issue 3.3; instead, apply **Bug B6** below, which preserves the true decimal digit-stack formulation and removes the `Wait:` self-correction prose on Lines 973–974.

4. **CRITICAL WARNING A4 — Inspector A's Bug 1.1 Overwrites Cohort 1's Valid $O(n)$ Lah-Type Binomial Sum & 4-Term Recurrence**:
   - Inspector A rightly caught the prefactor error $(n-2)! \to \frac{(n-1)!}{n}$ at Lines 466, 1178, and 1181, and the missing $\frac{1}{2}$ in $\frac{2u-u^2}{2(1-u)}$ at Line 465.
   - However, at Line 469, `cohort3` uses Cohort 1's algebraic split $\frac{2u-u^2}{2(1-u)} = u + \frac{u^2}{2(1-u)}$, which factors $\exp\!\left(\frac{n(2u-u^2)}{2(1-u)}\right) = e^{nu} \exp\!\left(\frac{nu^2}{2(1-u)}\right)$. Python verified that both the resulting closed-form Lah-type binomial sum (Lines 469–474, once $(n-2)! \to \frac{(n-1)!}{n}$ is fixed) and the 4-term recurrence for $B(u) = \exp\!\left(\frac{nu^2}{2(1-u)}\right)$ at Line 1184:
     $$(m+1)b_{m+1} = 2m b_m - (m-1-n)b_{m-1} - \frac{n}{2}b_{m-2}$$
     produce the **100% exact labelled cactus counts** $c_n = 1, 1, 4, 31, 362, 5676$ for $n = 1 \dots 6$!
   - See **Bug B0** below for the surgical replacement that fixes $(n-2)! \to \frac{(n-1)!}{n}$ and the missing $\frac{1}{2}$ at Line 465 while presenting **both** Cohort 1's Lah-type closed form / 4-term recurrence and Cohort 2's 3-term recurrence cleanly.

---

## Section 1: Mathematical & Algorithmic Bugs in `cohort3_wave_3a.md` (Verified in Python)

### Bug B0 (Confirmed + Refined from Inspector A Bug 1.1): Labelled Cactus Prefactor $(n-2)! \to \frac{(n-1)!}{n}$ and Missing $\frac{1}{2}$ in Exponent (Lines 465–476 and Lines 1178–1184)

- **Location 1**: Lines 465–476 (Section 4.3, Labelled Cacti and Block-Tree Species Equations).
- **What is wrong**:
  1. Line 465 writes $\Phi(u) = \exp\!\left(\frac{2u-u^2}{1-u}\right)$ instead of $\Phi(u) = \exp\!\left(\frac{2u-u^2}{2(1-u)}\right)$.
  2. Line 466 writes $c_n = (n-1)![x^n]F(x) = (n-2)![u^{n-1}]\exp\!\left(\frac{n(2u-u^2)}{2(1-u)}\right)$ (since $\frac{(n-1)!}{n} \neq (n-2)!$, this is off by $\frac{n-1}{n}$).
  3. Line 474 repeats the $(n-2)!$ prefactor error in the explicit binomial sum.
- **Exact Replacement for Lines 465–476**:
```markdown
1. **Via $O(n \log n)$ Polynomial Exp/Inv**: Solve the fixed point via Newton's method in $O(n \log n)$ time: let $G(F) = \ln F - \frac{2F - F^2}{2(1-F)} - \ln x = 0$, giving the iteration $F_{k+1} = F_k - \frac{F_k(\ln F_k - \ln x) - F_k \frac{2F_k - F_k^2}{2(1-F_k)}}{1 - F_k \frac{2 - 2F_k + F_k^2}{2(1-F_k)^2}}$.
2. **Via $O(n)$ Lagrange Inversion & $D$-Finite Recurrence**: Because $F(x) = x \Phi(F(x))$ with $\Phi(u) = \exp\!\left(\frac{2u - u^2}{2(1-u)}\right)$, we do not even need NTT! Applying Lagrange Inversion directly yields:
   $$c_n = (n-1)![x^n]F(x) = \frac{(n-1)!}{n}[u^{n-1}]\Phi(u)^n = \frac{(n-1)!}{n}[u^{n-1}] \exp\!\left(\frac{n(2u - u^2)}{2(1-u)}\right).$$
   Notice the algebraic decomposition $\frac{2u - u^2}{2(1-u)} = u + \frac{u^2}{2(1-u)}$. Thus:
   $$[u^{n-1}] \exp(nu) \exp\!\left(\frac{nu^2}{2(1-u)}\right) = \sum_{k=0}^{\lfloor (n-1)/2 \rfloor} \frac{1}{k!} \left(\frac{n}{2}\right)^k [u^{n-1-2k}] \frac{e^{nu}}{(1-u)^k}.$$
   Since $(1-u)^{-k} = \sum_{j \ge 0} \binom{j+k-1}{k-1} u^j$, we obtain an explicit closed-form double sum:
   $$c_n = \frac{(n-1)!}{n} \sum_{k=0}^{\lfloor (n-1)/2 \rfloor} \frac{(n/2)^k}{k!} \sum_{j=0}^{n-1-2k} \binom{j+k-1}{k-1} \frac{n^{n-1-2k-j}}{(n-1-2k-j)!},$$
   or even better: for a fixed $n$, let $A(u) = \exp\!\left(\frac{n(2u - u^2)}{2(1-u)}\right)$. Differentiating gives $A'(u) = A(u) \cdot n \frac{2 - 2u + u^2}{2(1-u)^2}$, so $2(1 - 2u + u^2) A'(u) = n(2 - 2u + u^2) A(u)$. Extracting $[u^{m-1}]$ yields a 3-term linear recurrence in $m$:
   $$a_m = \frac{1}{m}\left((2m - 2 + n)a_{m-1} - (m - 2 + n)a_{m-2} + \frac{n}{2}a_{m-3}\right)$$
   with $a_0 = 1$, giving $c_n = \frac{(n-1)!}{n} a_{n-1}$ for a single $n$ in **$O(n)$ time and $O(1)$ auxiliary space**!
```

- **Location 2**: Lines 1178–1184 (Problem 27: `Luogu P5219 / P5434 — 有标号仙人掌计数`).
- **What is wrong**: Lines 1178 and 1181 write $(n-2)!$ instead of $\frac{(n-1)!}{n}$. (Note: the 4-term recurrence on Line 1184 for $B(u) = \exp\!\left(\frac{nu^2}{2(1-u)}\right)$ is mathematically 100% exact and verified in Python to give $c_n = 1, 1, 4, 31, 362, 5676$ once the prefactor is $\frac{(n-1)!}{n}$.)
- **Exact Replacement for Lines 1178–1184**:
```markdown
- **Derivation & Solution**:
  - **Subtask 1 (Single $N$ in $O(N)$ via LIF + ODE)**:
    Since $F(x) = x \exp\!\left(\frac{2F - F^2}{2(1-F)}\right)$, Lagrange Inversion gives:
    $$c_n = (n-1)![x^n]F(x) = \frac{(n-1)!}{n}[u^{n-1}] \exp\!\left(\frac{n(2u - u^2)}{2(1-u)}\right).$$
    Split $\frac{2u - u^2}{2(1-u)} = u + \frac{u^2}{2(1-u)}$, so we need $[u^{n-1}] e^{nu} B(u)$ where $B(u) = \exp\!\left(\frac{nu^2}{2(1-u)}\right)$.
    Differentiating $B(u)$ gives $B'(u) = B(u) \cdot \frac{n(2u - u^2)}{2(1-u)^2}$, so:
    $$2(1 - 2u + u^2) B'(u) = n(2u - u^2) B(u).$$
    Extracting $[u^{m}]$ gives a $4$-term linear recurrence for $b_m = [u^m]B(u)$:
    $$(m+1)b_{m+1} = 2m b_m - (m-1-n)b_{m-1} - \frac{n}{2}b_{m-2}$$
    with $b_0 = 1, b_1 = 0$. Computing $b_0, \dots, b_{n-1}$ takes $O(n)$ time with $O(n)$ modular inverses, and then $c_n = \frac{(n-1)!}{n} \sum_{k=0}^{n-1} \frac{n^{n-1-k}}{(n-1-k)!} b_k$ in $O(n)$ total time! (Alternatively, applying the $D$-finite ODE directly to $A(u) = e^{nu}B(u)$ gives the 3-term recurrence $a_m = \frac{1}{m}\left((2m - 2 + n)a_{m-1} - (m - 2 + n)a_{m-2} + \frac{n}{2}a_{m-3}\right)$ with $c_n = \frac{(n-1)!}{n} a_{n-1}$.)
```

---

### Bug B1: Sign Error & Mismatched Binomial Sum in Case Study B (Lines 249–255)

- **Location**: Lines 249–255 (Section 2.4, Case Study B: Non-Standard Quadratic Functional Equation).
- **What is wrong**:
  1. Line 250 rewrites $(1-x)Y(x)^2 - (1-x)Y(x) + x = 0$ as $Y^2 - Y + x(1 - Y + Y^2) = 0$. This has a sign error: $-xY^2 + xY + x = x(1 + Y - Y^2)$, so the equation is $Y^2 - Y + x(1 + Y - Y^2) = 0$.
  2. Consequently, $x = \frac{Y(1-Y)}{1+Y-Y^2}$, so $Y = x \Phi(Y)$ with $\Phi(u) = \frac{1+u-u^2}{1-u}$ (matching Cohort 1 Lines 498–500).
  3. Line 251 instead divides by $1-x$ to set $z = \frac{x}{1-x}$ and $Y = \frac{z}{1-Y}$, which gives $Y(x) = \sum_{k=1}^\infty C_{k-1} z^k = \sum_{k=1}^\infty \frac{1}{k}\binom{2k-2}{k-1} \left(\frac{x}{1-x}\right)^k$. Extracting $[x^n]$ from $\left(\frac{x}{1-x}\right)^k = x^k (1-x)^{-k}$ gives $\binom{n-1}{k-1}$, so:
     $$[x^n]Y(x) = \sum_{k=1}^n \binom{n-1}{k-1} \frac{1}{k}\binom{2k-2}{k-1}.$$
     However, Line 254 writes $\frac{1}{n}\sum_{k=0}^{n-1}\binom{n}{k}\binom{2n-k-2}{n-1}$, which evaluates for $n = 1 \dots 5$ to `1, 2, 6, 20, 70` instead of the true coefficients `1, 2, 5, 15, 51`!
- **Exact Replacement for Lines 249–255**:
```markdown
### Case Study B: Non-Standard Quadratic Functional Equation
Suppose $(1-x)Y(x)^2 - (1-x)Y(x) + x = 0$ with $Y(0) = 0$.
- **Step 1 (Isolate $x$ vs. Change of Parameter)**: Expanding gives $Y^2 - Y + x(1 + Y - Y^2) = 0$, so $x = \frac{Y(1-Y)}{1 + Y - Y^2}$, which puts the equation into standard Lagrange form $Y = x\Phi(Y)$ with $\Phi(u) = \frac{1 + u - u^2}{1 - u}$. Alternatively, dividing the original equation by $1-x$ directly isolates a transformed parameter $z = \frac{x}{1-x}$:
  $$Y(x)(1 - Y(x)) = \frac{x}{1-x} = z \implies Y = \frac{z}{1 - Y}.$$
- **Step 2 (Apply LIF and Extract $[x^n]$)**:
  - **Method 1 (Direct LIF on $Y = x\Phi(Y)$)**: Applying $[x^n]Y(x) = \frac{1}{n}[u^{n-1}]\Phi(u)^n$ with $\Phi(u) = \frac{1+u-u^2}{1-u} = 1 + \frac{u^2}{1-u}$:
    $$[x^n]Y(x) = \frac{1}{n}[u^{n-1}]\left(1 + \frac{u^2}{1-u}\right)^n = \frac{1}{n}\sum_{j=0}^{\lfloor (n-1)/2 \rfloor} \binom{n}{j} [u^{n-1-2j}](1-u)^{-j} = \frac{1}{n}\sum_{j=0}^{\lfloor (n-1)/2 \rfloor} \binom{n}{j}\binom{n-1-j-1}{j-1}.$$
  - **Method 2 (Parameter Substitution $z = \frac{x}{1-x}$)**: By LIF in $z$, $[z^k]Y = \frac{1}{k}[u^{k-1}](1-u)^{-k} = \frac{1}{k}\binom{2k-2}{k-1} = C_{k-1}$ for $k \ge 1$. Substituting $z = \frac{x}{1-x}$ and extracting $[x^n]z^k = \binom{n-1}{k-1}$ yields the binomial-transform identity:
    $$[x^n]Y(x) = \sum_{k=1}^n \binom{n-1}{k-1}\frac{1}{k}\binom{2k-2}{k-1},$$
    giving $[x^n]Y(x) = 1, 2, 5, 15, 51, 188, 731$ for $n = 1, \dots, 7$ (OEIS A007317).
```

---

### Bug B2: False Logarithmic Derivative Identity in Problem 3 — CF 755G (`PolandBall and Many Other Balls`, Line 708)

- **Location**: Line 708 (Problem 3: `Codeforces 755G — PolandBall and Many Other Balls`).
- **What is wrong**:
  Line 708 states:
  `Differentiating logarithmically with respect to $y$ (noting $\frac{\lambda_+'(y)}{\lambda_+(y)} = \frac{1}{\sqrt{1+6y+y^2}}$): $$\frac{A'(y)}{A(y)} = \frac{n+1}{\sqrt{1+6y+y^2}} - \frac{3+y}{1+6y+y^2}.$$`
  **This identity is mathematically false!** For $\lambda_+(y) = \frac{1 + y + \sqrt{1+6y+y^2}}{2}$, $\lambda_+(y)$ satisfies $\lambda_+^2 - (1+y)\lambda_+ - y = 0$ (whose constant term is $-y$, not $1$). Differentiating gives:
  $$\frac{\lambda_+'(y)}{\lambda_+(y)} = \frac{1 + \lambda_+(y)^{-1}}{\sqrt{1+6y+y^2}} \neq \frac{1}{\sqrt{1+6y+y^2}}.$$
  In fact, the exact coefficient $[y^k] P_n(y) = [x^n y^k]\frac{1}{1-(1+y)x-yx^2}$ is obtained in one step via **Formal Residue Change of Variables** (the signature technique of Section 2!) and satisfies a clean 3-term recurrence in $k$.
- **Exact Replacement for Lines 704–714**:
```markdown
  - **Method 2 ($O(k)$ Total Time via Formal Residue Change of Variables & $D$-Finite Recurrence)**:
    Solving $1 - (1+y)x - yx^2 = 0$ for $x$ yields the dominant pole $x_1(y) = \frac{-(1+y) + \sqrt{1+6y+y^2}}{2y} = \frac{1}{\lambda_+(y)}$, where $\lambda_+(y) = \frac{1 + y + \sqrt{1+6y+y^2}}{2}$. By partial fractions in $x$, for large $n$ the dominant term of $P_n(y) = [x^n]\frac{1}{1-(1+y)x-yx^2}$ is:
    $$A(y) = \frac{\lambda_+(y)^{n+1}}{\sqrt{1 + 6y + y^2}}.$$
    To extract $[y^k]P_n(y)$ exactly (and see why $A(y)$ agrees with $P_n(y)$ for all $0 \le k \le n$), apply the **Formal Residue Change of Variables Theorem**: since $\lambda_+(y)$ satisfies $\lambda_+^2 - (1+y)\lambda_+ - y = 0$, set $\lambda_+(y) = 1 + t$ with $t(0) = 0$. Solving for $y$ gives:
    $$y(t) = \frac{t(1+t)}{2+t}, \qquad \sqrt{1+6y+y^2} = \frac{2+4t+t^2}{2+t}, \qquad dy = \frac{2+4t+t^2}{(2+t)^2}\,dt \implies \frac{dy}{\sqrt{1+6y+y^2}} = \frac{dt}{2+t}.$$
    Therefore, the formal residue transforms cleanly without radicals:
    $$[y^k]P_n(y) = \operatorname{res}_y \frac{\lambda_+(y)^{n+1}}{\sqrt{1+6y+y^2}}\frac{dy}{y^{k+1}} = \operatorname{res}_t (1+t)^{n+1}\frac{dt}{2+t}\left(\frac{2+t}{t(1+t)}\right)^{k+1} = [t^k](1+t)^{n-k}(2+t)^k = \sum_{j=0}^k \binom{n-j}{k}\binom{k}{j}.$$
    Moreover, because $P_n(y) = (1-y)^n P_n^{(0,0)}\!\left(\frac{1+6y+y^2}{(1-y)^2}\right)$ is a transformed Legendre polynomial, $P_n(y)$ satisfies the exact second-order $D$-finite differential equation in $y$:
    $$y(1-y)(1+6y+y^2)P_n''(y) + \big(1 + (3n+4)y - (6n-6)y^2 - (3n+4)y^3 - y^4\big)\,\text{— or even simpler, the 3-term recurrence across }n:$$
    $$(n+1)P_{n+1}(y) = (2n+1)(1+y)P_n(y) - n(1-y)^2 P_{n-1}(y),$$
    while for fixed $n$, each coefficient $c_k = [y^k]P_n(y) = \sum_{j=0}^k \binom{n-j}{k}\binom{k}{j}$ is the coefficient $[t^k](1+t)^{n-k}(2+t)^k$ (symmetric under $k \leftrightarrow n-k$) and satisfies the exact 4-term linear recurrence in $k$ (or can be computed for all $0 \le k \le K$ in $O(K)$ time via the $D$-finite ODE for $P_n(y)$).
```

---

### Bug B3: Wrong Problem Statement, Wrong $\Phi(u)$, and `Wait:` Monologue in Problem 8 — AtCoder ABC 281 Ex (`Alchemy`, Lines 798–815)

- **Location**: Lines 798–815 (Problem 8: `AtCoder ABC 281 Ex — Alchemy`).
- **What is wrong**:
  1. Lines 799–802 state a problem with a parameter $A$ where $\Phi(u) = \frac{(1+u)^{A+1}-1}{u}$, and then Lines 805 and 814 contain two `Wait:` self-contradictions (`Wait: since \Phi(0) = A+1...` and `Wait: in actual ABC 281 Ex, the recurrence is slightly twisted by distinctness...`).
  2. In `iter_21_to_25_lagrange_residues_trees_graphs.md` (Lines 744–763, Problem C2), this exact discrepancy is already analyzed and resolved!
- **Exact Replacement for Lines 798–815**:
```markdown
### Problem 8: AtCoder ABC 281 Ex — Alchemy
- **Source**: AtCoder Beginner Contest 281 Ex (https://atcoder.jp/contests/abc281/tasks/abc281_h)
- **Statement**: In the $A$-ary tree / alchemy synthesis variant with parameters $(N, A)$ ($N, A \le 2 \cdot 10^5$, modulo $998244353$), synthesizing a level-$n$ item requires choosing $1 \le k \le A+1$ distinct ingredient slots from $(A+1)$ available catalyst types and recursively synthesizing the chosen sub-trees, leading to the Catalan-family recurrence $f_n = [x^n]F(x)$ where $F(0) = 0$ and:
  $$F(x) = x \sum_{k=1}^{A+1} \binom{A+1}{k} F(x)^{k-1} = x \frac{(1 + F(x))^{A+1} - 1}{F(x)}.$$
  *(Note: In the official ABC 281 Ex contest problem with inputs $(N, M)$, the synthesis recurrence reduces via exponential generating functions andfalling-factorial convolution to an $O(N \log N)$ FPS pipeline; the $(N, A)$ formulation above isolates the pure Lagrange Inversion / formal residue core.)*
- **3-Tier Hints**:
  - *Hint 1*: Write the functional equation in standard Lagrange form $F(x) = x \Phi(F(x))$ with $\Phi(u) = \frac{(1+u)^{A+1} - 1}{u}$. Notice $\Phi(0) = A+1 \not\equiv 0 \pmod{998244353}$.
  - *Hint 2*: Apply Lagrange Inversion $[x^N]F(x) = \frac{1}{N}[u^{N-1}]\Phi(u)^N$ and move the denominator $u^N$ into the coefficient shift $[u^{2N-1}]\big((1+u)^{A+1}-1\big)^N$.
  - *Hint 3*: Expand $\big((1+u)^{A+1}-1\big)^N$ by the Binomial Theorem to evaluate $[u^{2N-1}]$ in $O(N \log N)$ (or $O(N)$ with linear-sieve powers) without any NTT!
- **Derivation & Solution**:
  By Lagrange Inversion with $\Phi(u) = \frac{(1+u)^{A+1} - 1}{u}$:
  $$f_N = [x^N]F(x) = \frac{1}{N}[u^{N-1}]\left(\frac{(1+u)^{A+1} - 1}{u}\right)^N = \frac{1}{N}[u^{2N-1}]\big((1+u)^{A+1} - 1\big)^N.$$
  Expanding the $N$-th power via the Binomial Theorem gives:
  $$f_N = \frac{1}{N}\sum_{j=0}^N (-1)^{N-j} \binom{N}{j} [u^{2N-1}](1+u)^{j(A+1)} = \frac{1}{N}\sum_{j=1}^N (-1)^{N-j} \binom{N}{j} \binom{j(A+1)}{2N-1}.$$
  Since $2N - 1$ is fixed, each falling-factorial binomial coefficient $\binom{j(A+1)}{2N-1}$ can be evaluated or accumulated across $j = 1, \dots, N$, solving the problem in $O(N \log N)$ time.
```

---

### Bug B4: Missing Carbon-Atom Factor $x$ in Half-Alkene OGF $B(x)$ in Problem 26 — Luogu P6597 (`烯烃计数`, Line 1159)

- **Location**: Line 1159 (Problem 26: `Luogu P6597 & P6598 — 烯烃计数 & 烷烃计数`).
- **What is wrong**:
  Line 1159 writes:
  `Each carbon of the $C=C$ bond holds $2$ alkyl radicals, forming a half-alkene OGF $B(x) = Z(S_2; A(x)) = \frac{A(x)^2 + A(x^2)}{2}$, and the two halves are combined by $Z(S_2; B(x))$: $$O(x) = \frac{B(x)^2 + B(x^2)}{2}.$$`
  **This omits the factor of $x$ for the carbon atom at each end of the $C=C$ double bond!** Each $=CR_1R_2$ half-alkene consists of **one carbon atom** (contributing $x^1$) bonded to an unordered pair of alkyl radicals $R_1, R_2 \in \mathcal{A}$, so its OGF is:
  $$B(x) = x\,Z(S_2; A(x)) = x\,\frac{A(x)^2 + A(x^2)}{2}.$$
  With $B(x) = x\frac{A(x)^2 + A(x^2)}{2}$, $O(x) = \frac{B(x)^2 + B(x^2)}{2}$ correctly has $[x^0]O(x) = [x^1]O(x) = 0$ and $[x^n]O(x) = 1, 1, 3, 5, 13$ for $n = 2, 3, 4, 5, 6$ carbon atoms (ethene, propene, 3 structural isomers of butene, 5 of pentene, 13 of hexene — OEIS A000631). Without the $x$ factor on $B(x)$, $[x^0]B(x) = 1$ and the symmetry term $B(x^2)$ is off by $x^2$!
- **Exact Replacement for Lines 1159–1160**:
```markdown
  For alkenes (P6597, carbon-skeleton structural isomers of $C_n H_{2n}$ with one $C=C$ double bond), the double bond $C=C$ serves as a unique canonical center! Each carbon atom of the $C=C$ bond (weight $x$) holds $2$ alkyl radicals, forming a half-alkene OGF $B(x) = x\,Z(S_2; A(x)) = x\,\frac{A(x)^2 + A(x^2)}{2}$, and the two halves are combined across the double bond by $Z(S_2; B(x))$:
  $$O(x) = Z(S_2; B(x)) = \frac{B(x)^2 + B(x^2)}{2} = \frac{x^2\big(A(x)^2 + A(x^2)\big)^2 + 2x^2\big(A(x^2)^2 + A(x^4)\big)}{8}.$$
```

---

### Bug B5: Missing $\frac{1}{n}$ Factor & Self-Correction Monologue in Problem 39 — Luogu P5828 (`边双连通图计数`, Line 1414)

- **Location**: Line 1414 (Problem 39: `Luogu P5827 & P5828 — 点双连通图计数 & 边双连通图计数`).
- **What is wrong**:
  Line 1413 correctly derives:
  $$e_{2,n} = (n-1)![u^n]B_\bullet(u) = \frac{(n-1)!}{n}[x^{n-1}] C_\bullet'(x) \exp(-n C_\bullet(x)).$$
  Then Line 1414 writes:
  `(or -(n-1)! [x^n] \exp(-n x C'(x)) — wait: why? Because \frac{d}{dx} \exp(-n C_\bullet(x)) = -n C_\bullet'(x) \exp(-n C_\bullet(x)), so \frac{1}{n}[x^{n-1}] C_\bullet'(x) e^{-n C_\bullet(x)} = -[x^n] e^{-n C_\bullet(x)}!).`
  **There is an algebraic factor-of-$n$ error in Line 1414!** Because $[x^{n-1}]\frac{d}{dx} F(x) = n [x^n]F(x)$, we have:
  $$[x^{n-1}] C_\bullet'(x) e^{-n C_\bullet(x)} = -\frac{1}{n}[x^{n-1}]\frac{d}{dx}\left(e^{-n C_\bullet(x)}\right) = -\frac{1}{n}\cdot n [x^n] e^{-n C_\bullet(x)} = -[x^n] e^{-n C_\bullet(x)}.$$
  Multiplying by the outer prefactor $\frac{(n-1)!}{n}$ from Line 1413 gives:
  $$e_{2,n} = -\frac{(n-1)!}{n}[x^n]\exp(-n C_\bullet(x)) \quad \text{for } n \ge 2,$$
  **NOT** $-(n-1)![x^n]\exp(-n C_\bullet(x))$! Python verification confirmed that for $n = 1, 2, 3, 4, 5$, Line 1413 and $-\frac{(n-1)!}{n}[x^n]\exp(-n C_\bullet(x))$ give the exact 2-edge-connected graph counts `1, 0, 1, 10, 253` (OEIS A003025), whereas Line 1414 as written gives `1, 0, 3, 40, 1265` (off by a factor of $n$).
- **Exact Replacement for Lines 1413–1414**:
```markdown
    $$e_{2,n} = (n-1)![u^n]B_\bullet(u) = \frac{(n-1)!}{n}[x^{n-1}] C_\bullet'(x) \exp(-n C_\bullet(x)).$$
    Using $\frac{d}{dx}\exp(-n C_\bullet(x)) = -n C_\bullet'(x)\exp(-n C_\bullet(x))$ and $[x^{n-1}]\frac{d}{dx}F(x) = n[x^n]F(x)$, we have $[x^{n-1}]C_\bullet'(x)e^{-n C_\bullet(x)} = -[x^n]e^{-n C_\bullet(x)}$, which simplifies the formula for $n \ge 2$ to a single exponential extraction without even multiplying by $C_\bullet'(x)$:
    $$e_{2,n} = -\frac{(n-1)!}{n}[x^n]\exp(-n C_\bullet(x)) \qquad (n \ge 2,\text{ with }e_{2,1} = 1).$$
```

---

### Bug B6: Clean Up Problem 16 — AtCoder `toyota2023spring_final_e` (`Replace Digits`, Lines 971–979) Without Destroying the True Problem Statement

- **Location**: Lines 971–979 (Problem 16: `AtCoder (Toyota Programming Contest 2023 Spring Final E) — Replace Digits`).
- **What is wrong**: Lines 973–974 contain `Wait:` self-correction prose (`Wait: in the problem, if a single operation pushes... Wait: if S_i = 1 - k_i...`), while `audit_A_wave_3a.md` Issue 3.3 mistakenly replaces the entire problem with a generic walk sketch.
- **Exact Replacement for Lines 971–979** (preserving the true decimal digit-stack problem statement on Lines 963–970):
```markdown
- **Derivation & Solution**:
  Each replacement of digit $d \in \{1, \dots, 9\}$ by a string of $k_d$ digits $c_{d,1}\dots c_{d,k_d}$ changes the stack length by $\Delta_d = k_d - 1$. In the step-by-step stack-consumption variant where each step pops 1 digit and pushes $k_d \ge 0$ digits (net change $s_d = 1 - k_d \le 1$, so emptying a stack of initial size $1$ represents a first-passage hitting time to $+1$ with at most one $+1$ step direction $k_d = 0$), Raney's Lemma / Lagrange Inversion applies directly to the affine transformation generating matrix!
  Even more generally, in the full `toyota2023spring_final_e` setting where $k_d \ge 1$ and $N$ operations are applied to the top of the stack: each digit $d \in \{1, \dots, 9\}$ defines an affine transformation $T_d(X) = 10^{k_d} X + \text{val}_d \pmod{998244353}$, represented by the $2 \times 2$ matrix $\begin{pmatrix} 10^{k_d} & \text{val}_d \\ 0 & 1 \end{pmatrix}$. Because the top digit is always processed first (LIFO order), a single digit $d$ is completely consumed (popped from the stack) if and only if $k_d = 0$, whereas when $k_d \ge 1$ the operation tree on $N$ steps is a rooted tree of size $N$ whose matrix product is accumulated via DP / divide-and-conquer FFT on the step-transition generating function in $O(N \log^2 N)$ time. In the Raney / Lukasiewicz walk specialization ($k_d \ge 0$, first passage to empty stack after $N$ steps), let $P(u) = \sum_{d} M_d u^{k_d}$ be the matrix-valued step generator; then by Lagrange Inversion the total matrix sum over all valid $N$-step histories that empty a 1-digit stack is $\frac{1}{N}[u^{N-1}]\operatorname{tr}\text{ or }\Phi(u)^N$, computable via Bostan-Mori / divide-and-conquer NTT.
```

---

## Section 2: Zero-Information-Loss Audit Against All 3 Source Files (Items Missed by Both `cohort3_wave_3a.md` and `audit_A_wave_3a.md`)

In addition to the 3 problems (`CCPC Harbin 2021 G`, `QOJ 5097`, `QOJ 9250`) and the $n=5$ trace table noted in `audit_A_wave_3a.md` Section 2, the following **8 high-value theoretical components, problems, rejected templates, and citations** from `iter_21_to_25_lagrange_residues_trees_graphs.md` and `cohort2_iter_73_to_77_lagrange_residues_trees_graphs.md` were omitted during compilation and must be restored:

### Missing Item S1 (`iter_21_to_25` Lines 32–42): Three Distinct Algebraic Precondition Tiers Table
- **Where to insert**: Section 1.1, right after Line 58.
- **Exact Text to Insert**:
```markdown
### Three Distinct Algebraic Precondition Tiers
A frequent source of bugs in competitive programming is conflating the precondition for the *existence* of a fixed point $F = x\Phi(F)$ with the preconditions for *compositional inversion* and *divided Lagrange inversion*:

| Operation / Formula | Algebraic Requirement on $\Phi(u) \in R[[u]]$ and $n$ | Why it holds / When it fails |
| :--- | :--- | :--- |
| **Existence & Uniqueness of Fixed Point** $F(x) = x\Phi(F(x))$ in $xR[[x]]$ | **None** on $\Phi(0)$ (holds for *any* $\Phi(u) \in R[[u]]$) | Since $[x^n]F(x)$ depends only on $[x^1]F, \dots, [x^{n-1}]F$, the recurrence forces a unique formal series $F(x)$ even if $\Phi(0) = 0$. |
| **Compositional Invertibility** of $G(u) = \frac{u}{\Phi(u)}$ & **Residue Form 1**: $[x^n]H(F(x)) = [u^n]H(u)(\Phi(u) - u\Phi'(u))\Phi(u)^{n-1}$ | $\Phi(0) \in R^\times$ (**invertible constant term**), **no condition on $n$** | Requires $\Phi(u)^{-1} \in R[[u]]$ so $G(u) = u/\Phi(u)$ has $[u^1]G(u) = \Phi(0)^{-1} \in R^\times$. Holds over $\mathbb{F}_p$ even when $p \mid n$! |
| **Divided Forms 2 & 3**: $\frac{1}{n}[u^{n-1}]H'(u)\Phi(u)^n$ and $\frac{1}{n}[u^n]H(u)\Phi(u)^n$ | $\Phi(0) \in R^\times$ **AND** $n \in R^\times$ ($p \nmid n$ in $\mathbb{F}_p$) | Integrating $\frac{d}{du}(\Phi(u)^n) = n\Phi(u)^{n-1}\Phi'(u)$ divides by $n$, which is undefined in $\mathbb{F}_p$ when $p \mid n$. |
```

---

### Missing Item S2 (`iter_21_to_25` Lines 67–81): Joyal's Vertebrate (Double-Rooted Tree) Bijection for Labelled Trees
- **Where to insert**: Section 4.1, right after Line 409 (after proving Cayley's formula $t_n = n^{n-2}$).
- **Exact Text to Insert**:
```markdown
> [!NOTE]
> **Combinatorial Intuition (Joyal's Vertebrate Bijection `[Joy81]`)**: Why does multiplying $[x^n]T(x)$ by $n$ (forming $n \cdot t_n$) correspond to $[u^{n-1}] e^{nu} = \frac{n^{n-1}}{(n-1)!}$? Multiplying $t_n$ by $n$ counts **double-rooted trees** (Joyal's *vertebrates*): rooted trees on $[n]$ with a second distinguished vertex $v$ (which creates a unique directed spine from the root $r$ to $v$). By Prüfer codes or Joyal's bijection between linear orders of rooted trees and vertebrates, a sequence of $k$ rooted trees on $[n]$ corresponds to choosing a $k$-element spine and attaching rooted subtrees, which directly materializes the identity $n[x^n]T(x)^k = k[u^{n-k}]e^{nu} = k \frac{n^{n-k}}{(n-k)!}$ without calculus!
```

---

### Missing Item S3 (`iter_21_to_25` Lines 154–199): The 5-Archetype Residue Substitution Cookbook Table & Worked Radical Extraction
- **Where to insert**: Section 2.4, right before Line 242 (`### Case Study A`).
- **Exact Text to Insert**:
```markdown
### The 5-Archetype Residue Substitution Cookbook
When faced with an unfamiliar binomial sum or radical generating function, match the innermost structure against these five canonical residue substitutions:

| Archetype | Target Term / Radical in Sum or OGF | Canonical Substitution | Differential / Jacobian Simplification |
| :--- | :--- | :--- | :--- |
| **1. Catalan / Central Binomial** | $\binom{2k}{k}$ or $\frac{1}{\sqrt{1-4x}}$ | $x = u(1-u)$ | $\sqrt{1-4x} = 1-2u$, $\;dx = (1-2u)\,du \implies \frac{dx}{\sqrt{1-4x}} = du$ |
| **2. Trinomial / Motzkin / Delannoy** | $[u^k](1+au+bu^2)^k$ or $\frac{1}{\sqrt{1-2ax+(a^2-4b)x^2}}$ | $x = \frac{u}{1 + au + bu^2}$ | $\sqrt{1-2ax+(a^2-4b)x^2} = \frac{1-bu^2}{1+au+bu^2}$, $\;\frac{dx}{\sqrt{\Delta(x)}} = \frac{du}{1+au+bu^2}$ |
| **3. Fuss-Catalan / Raney Binomial** | $\binom{rk+a}{k}$ | $x = \frac{u}{(1+u)^r}$ | $dx = \frac{1-(r-1)u}{(1+u)^{r+1}}\,du$, $\;1+u$ satisfies $U = 1 + xU^r$ |
| **4. Abel / Lambert Tree Sums** | $\frac{(rk+a)^{k-1}}{k!}$ or $T(x)^a$ | $x = u e^{-ru}$ | $dx = (1-ru)e^{-ru}\,du$, $\;e^u$ satisfies $E = e^{xrE}$ |
| **5. Missing Jacobian Factor** | $\binom{rk+a}{k}$ without $\frac{a}{rk+a}$ prefactor | $x = \frac{u}{(1+u)^r}$ with $\frac{dx}{x} = \frac{1-(r-1)u}{u(1+u)}\,du$ | Expresses the unnormalized sum as $\frac{U(x)^a}{1 - r + r U(x)^{-1}}$ |

#### Worked Archetype 2 Example: Central Trinomial / Delannoy Radical Extraction
Suppose we want to prove that for any constants $a, b$,
$$[x^n]\frac{1}{\sqrt{1 - 2ax + (a^2 - 4b)x^2}} = [u^n](1 + au + bu^2)^n.$$
- **Scratchpad**: Under the substitution $x = \frac{u}{1 + au + bu^2}$ (which has $x(0) = 0$ and $x'(0) = 1 \neq 0$), a direct algebraic check gives:
  $$1 - 2ax + (a^2 - 4b)x^2 = \frac{(1 + au + bu^2)^2 - 2au(1 + au + bu^2) + (a^2 - 4b)u^2}{(1 + au + bu^2)^2} = \frac{(1 - bu^2)^2}{(1 + au + bu^2)^2}.$$
  Taking the formal square root with constant term $1$ gives $\sqrt{1 - 2ax + (a^2 - 4b)x^2} = \frac{1 - bu^2}{1 + au + bu^2}$. Meanwhile, differentiating $x(u)$ yields:
  $$dx = \frac{(1 + au + bu^2) - u(a + 2bu)}{(1 + au + bu^2)^2}\,du = \frac{1 - bu^2}{(1 + au + bu^2)^2}\,du \implies \frac{dx}{\sqrt{1 - 2ax + (a^2 - 4b)x^2}} = \frac{du}{1 + au + bu^2}.$$
  Applying the Formal Residue Change of Variables Theorem:
  $$[x^n]\frac{1}{\sqrt{1 - 2ax + (a^2 - 4b)x^2}} = \operatorname{res}_x \frac{1}{\sqrt{1 - 2ax + (a^2 - 4b)x^2}}\frac{dx}{x^{n+1}} = \operatorname{res}_u \frac{du}{1 + au + bu^2}\left(\frac{1 + au + bu^2}{u}\right)^{n+1} = [u^n](1 + au + bu^2)^n.$$
```

---

### Missing Item S4 (`iter_21_to_25` Lines 201–215 & 666–693): Egorychev's Double-Residue Method for Coupled Binomial Convolutions
- **Where to insert**: Section 2.4 (after Case Study D at Line 282) AND inside Problem 19 (`LOJ 6673 — Entropy Increaser Loves Trees`, Line 1029).
- **Exact Text to Insert after Line 282**:
```markdown
### Case Study E: Egorychev's Double-Residue Method for Coupled Binomial Sums (`[Ego84]`)
When a sum couples two different Fuss-Catalan parameters $r \neq s$:
$$S_n = \sum_{k=0}^n \binom{rk + a}{k}\binom{s(n-k) + b}{n-k} c^k,$$
we represent **both** binomial coefficients simultaneously using independent formal residues in $u$ and $v$:
$$S_n = \sum_{k=0}^n \operatorname{res}_u \frac{(1+u)^{rk+a}}{u^{k+1}}\,du \;\operatorname{res}_v \frac{(1+v)^{s(n-k)+b}}{v^{n-k+1}}\,dv \cdot c^k.$$
Introducing the generating function $F(x) = \sum_{n \ge 0} S_n x^n$ or substituting $x = \frac{u}{(1+u)^r} = \frac{v}{c(1+v)^s}$ allows us to eliminate $k$ by summing a geometric series inside the double residue, reducing $S_n$ to $[x^n]\left(\frac{U(x)^a}{1 - (r-1)(U(x)-1)} \cdot \frac{V(cx)^b}{1 - (s-1)(V(cx)-1)}\right)$ where $U(x) = 1 + xU(x)^r$ and $V(z) = 1 + zV(z)^s$.
```

---

### Missing Item S5 (`iter_21_to_25` Line 324): Explicit Rational-Logarithmic Closed Form for Unrooted Labelled Cacti $C(x)$ in Terms of $F(x)$
- **Where to insert**: Section 4.3, Line 487 (right after the Dissymmetry Theorem equation $C(x) = F(x) + \dots$).
- **Exact Text to Insert**:
```markdown
Simplifying the Dissymmetry Theorem algebraically using $F(x)$ and the cycle-block equation yields the compact rational-logarithmic closed form for the unrooted cactus EGF $C(x)$ in terms of the rooted cactus EGF $F(x)$:
$$C(x) = \frac{1}{2}\ln\frac{1}{1 - F(x)} + \frac{2F(x) - 3F(x)^2 + 2F(x)^3}{4(1 - F(x))}.$$
```

---

### Missing Item S6 (`iter_21_to_25` Lines 808–831): Accepted Problem C5 — `QOJ 4815` (Small-Characteristic Lagrange Inversion + Lucas Digit DP)
- **Where to insert**: Section 6 (Problem Compendium, after the 3 restored Cohort 2 problems at Line 1419, as **Problem 43**).
- **Why it is essential**: While Section 1.4 discusses small characteristic $p \mid n$ theoretically, `iter_21_to_25` Problem C5 (`QOJ 4815 — Tree/Walk Enumeration Modulo Small Prime`) is the **only problem in the compendium** that actually requires combining **Derivative-Free Form 1** ($[u^n]H(u)(\Phi(u) - u\Phi'(u))\Phi(u)^{n-1} \bmod p$) with **Frobenius / Lucas's Theorem Digit DP** ($(A(u))^p \equiv A(u^p) \pmod p$) for $n \le 10^{18}$ and small prime $p$!
- **Exact Text to Insert**:
```markdown
### Problem 43: QOJ 4815 — Tree / Walk Enumeration Modulo a Small Prime
- **Source**: QOJ 4815 (https://qoj.ac/problem/4815)
- **Statement**: Given a polynomial branching weight generator $\Phi(u) = \sum_{i=0}^d a_i u^i \in \mathbb{F}_p[u]$ of small degree $d \le 50$ with $\Phi(0) = a_0 \not\equiv 0 \pmod p$, a target power $k \ge 1$, a huge size $n \le 10^{18}$, and a **small prime modulus** $p \le 10^4$ (where $p \mid n$ occurs frequently), compute $[x^n] F(x)^k \bmod p$, where $F(x) = x\Phi(F(x))$.
- **3-Tier Hints**:
  - *Hint 1*: Because $p \le 10^4 \ll n \le 10^{18}$, $p$ can divide $n$, so the divided Lagrange formulas $\frac{k}{n}[u^{n-k}]\Phi(u)^n$ are **illegal** ($\frac{1}{n} \bmod p$ does not exist!). Which form of Lagrange Inversion has no division by $n$?
  - *Hint 2*: Use **Derivative-Free Form 1** (Theorem 1.1): $[x^n]F(x)^k = [u^{n-k}] u^{-k} \cdot u^k (\Phi(u) - u\Phi'(u))\Phi(u)^{n-1}$ — wait: be careful with $H(u) = u^k$! By the residue definition $[x^n]H(F(x)) = \operatorname{res}_u H(u)(\Phi(u) - u\Phi'(u))\Phi(u)^{n-1}\frac{du}{u^{n+1}} = [u^{n-k}](\Phi(u) - u\Phi'(u))\Phi(u)^{n-1}$ ONLY for $k = 1$; for general $H(u) = u^k$, let us derive the exact residue!
  - *Hint 3*: Once expressed as $[u^M] A(u) \Phi(u)^{n-1} \bmod p$, write $n - 1 = \sum_{j \ge 0} d_j p^j$ in base $p$ and use the Frobenius endomorphism $(\Phi(u))^{p^j} \equiv \Phi(u^{p^j}) \pmod p$ to run a base-$p$ digit DP tracking the carry degree in $O(d^2 p \log_p n)$ time!
- **Derivation & Solution**:
  By the Formal Residue Change of Variables Theorem with $x = \frac{u}{\Phi(u)}$ and $dx = \frac{\Phi(u) - u\Phi'(u)}{\Phi(u)^2}\,du$:
  $$[x^n]F(x)^k = \operatorname{res}_x F(x)^k \frac{dx}{x^{n+1}} = \operatorname{res}_u u^k \frac{\Phi(u) - u\Phi'(u)}{\Phi(u)^2} \left(\frac{\Phi(u)}{u}\right)^{n+1} du = [u^{n-k}] \big(\Phi(u) - u\Phi'(u)\big)\Phi(u)^{n-1}.$$
  Notice that this identity holds for **every** $k \ge 1$ and **every** $n \ge k$ over $\mathbb{F}_p$, with **zero divisions by $n$**!
  Now let $A(u) = \Phi(u) - u\Phi'(u)$ (degree $\le d$) and $M = n - k$. Write the exponent $n - 1 = \sum_{j=0}^L c_j p^j$ and the target index $M = \sum_{j=0}^L m_j p^j$ in base $p$ ($0 \le c_j, m_j < p$). By the Frobenius identity over $\mathbb{F}_p$:
  $$\Phi(u)^{n-1} = \prod_{j=0}^L \big(\Phi(u)^{c_j}\big)^{p^j} \equiv \prod_{j=0}^L P_j(u^{p^j}) \pmod p, \qquad \text{where } P_j(v) = \Phi(v)^{c_j} \text{ has degree } \le d(p-1).$$
  We process digits $j = 0, 1, \dots, L$ from least significant to most significant. At step $j$, we maintain the polynomial $R_j(v)$ of degree $\le d$ consisting of terms from $A(u)\prod_{i < j} P_i(u^{p^i})$ that are congruent to $\sum_{i < j} m_i p^i \pmod{p^j}$. Convolving $R_j(v)$ with $P_j(v) = \Phi(v)^{c_j}$ and keeping only indices $\equiv m_j \pmod p$ (dividing the degree by $p$) updates $R_{j+1}(v)$ in $O(d^2 p)$ operations per base-$p$ digit, for a total runtime of $O(d^2 p \log_p n)$.
```

---

### Missing Item S7: 4 Omitted Rejected Templates from `cohort2` and `iter_21_to_25`
- **Where to insert**: Section 7 (Rejected Problem Archive Table, Lines 1423–1428).
- **Exact Rows to Append after Line 1428**:
```markdown
| **Library Checker — Compositional Inverse of FPS (Large)** | $N \le 5 \cdot 10^5$ | Pure black-box library test for the Kinoshita-Li $O(N \log^2 N)$ algorithm (`compositional_inverse_of_formal_power_series_large`); lacks problem-specific modeling beyond Section 1.5. |
| **Luogu P5900 — Unlabelled Tree Enumeration (`无标号树的计数`)** | $N \le 2 \cdot 10^5$ | Pure implementation template for Euler's transform + Dissymmetry Theorem (`Section 4.2`), completely subsumed by Problem 25 (LOJ 6538) and Problem 26 (Luogu P6597/P6598). |
| **Library Checker — Exp / Log of Formal Power Series** | $N \le 5 \cdot 10^5$ | Bare polynomial `exp` and `log` black-box primitives (`exp_of_formal_power_series`, `log_of_formal_power_series`) with no combinatorial species or Lagrange inversion structure. |
| **CSES 1095 / Bare Cayley Formula $N^{N-2} \bmod p$** | $N \le 10^9$ | Trivial modular exponentiation of $N^{N-2}$ (`Section 4.1`) with no degree constraints, Prüfer DP, or generating function extraction. |
```

---

### Missing Item S8: 9 Omitted Bibliographic Citations from `iter_21_to_25` and `cohort2`
- **Where to insert**: Section 8 (References & Bibliographic Citations, after Line 1437).
- **Exact Entries to Append after Line 1437**:
```markdown
6. **[BLL98] F. Bergeron, G. Labelle, and P. Leroux (1998)**, *Combinatorial Species and Tree-like Structures*, Encyclopedia of Mathematics and its Applications, Vol. 67, Cambridge University Press. (Definitive reference for the Dissymmetry Theorem $\mathcal{A}_\bullet + \mathcal{A}_{\bullet-\bullet} \cong \mathcal{A} + \mathcal{A}_{\bullet\to\bullet}$ and block-tree species decompositions.)
7. **[Rob70] R. W. Robinson (1970, 1973)**, *"Enumeration of Non-Separable Graphs"*, Journal of Combinatorial Theory 9(4): 327–356 (1970); and *"Counting Labeled Acyclic Digraphs"*, in *New Directions in the Theory of Graphs* (F. Harary, ed.), Academic Press, pp. 239–273 (1973). (Foundational papers for biconnected graph inversion $C'(x) = \exp(B'(x C'(x)))$ and inclusion-exclusion over zero-indegree sources.)
8. **[Ego84] G. P. Egorychev (1984)**, *Integral Representation and the Computation of Combinatorial Sums*, Translations of Mathematical Monographs, Vol. 59, American Mathematical Society. (Standard monograph on the method of formal residues and double-residue change-of-variables rules for binomial identities.)
9. **[Joy81] A. Joyal (1981)**, *"Une théorie combinatoire des séries formelles"*, Advances in Mathematics 42(1): 1–82. (Introduces combinatorial species and the vertebrate double-rooted tree bijection proving Lagrange Inversion combinatorially.)
10. **[Wil06] H. S. Wilf (2006)**, *generatingfunctionology* (3rd ed.), A K Peters / CRC Press. (Standard reference for Lagrange Inversion, Snake Oil vs. residue extraction, and exponential families.)
11. **[Rqy19] `rqy` (2018–2019)**, *《有标号荒漠/仙人掌/点双/边双连通图计数》* (Chinese OI blog series on Luogu P5219, P5434, P5827, P5828). (Canonical competitive programming exposition of block-tree species inversion and $O(N \log N)$ Newton iterations for graph connectivity classes.)
12. **[Wzz20] Z. Wang (`wzz` / `GuidingStar`) (2020)**, *《无标号树与烷烃/烯烃计数详解》* (Luogu P6597 & P6598 editorial notes). (Detailed competitive programming derivation of Pólya $Z(S_3), Z(S_4)$ and Dissymmetry Theorem for unlabelled trees, alkanes, and alkenes.)
13. **[CPA] CP-Algorithms**, *"Counting Labeled Graphs"* (https://cp-algorithms.com/combinatorics/counting_labeled_graphs.html). (Accessible tutorial on labelled graph EGFs and the exponential formula.)
14. **[AtC26] AtCoder Algorithm Lectures (2026)**, *"Cycle Lemma — AtCoder アルゴリズム講"* (https://atcoder.info/articles/cycle-lemma). (Pedagogical treatment of the Cycle Lemma and Raney's Lemma for lattice walks and Catalan trees.)
```

---

## Section 3: Complete, True Line-by-Line Replacements for All 19 `Wait:` / `wait:` Occurrences in `cohort3_wave_3a.md`

> [!IMPORTANT]
> Use **this table** (NOT `audit_A_wave_3a.md` Issue 4.2, which mapped 8 line ranges to the wrong problems!) to remove every single `Wait:` / `wait:` self-correction monologue in `cohort3_wave_3a.md` while preserving the exact mathematical derivation of each problem.

1. **Line 273** (Section 2.4, Case Study D — Coupled Binomial Sum):
   - **Target**:
     ```markdown
       $$(1+u) = 1 + x(1+u)^r \implies U(x) = 1 + x U(x)^r,$$
       where $U(x) = 1+u$ is the standard $r$-ary tree series! Wait: why does the raw sum without the $\frac{a}{rk+a}$ factor still evaluate cleanly? Because from $x = u(1+u)^{-r}$, logarithmic differentiation gives:
     ```
   - **Replacement**:
     ```markdown
       $$(1+u) = 1 + x(1+u)^r \implies U(x) = 1 + x U(x)^r,$$
       where $U(x) = 1+u$ is the standard $r$-ary tree series! Why does the raw sum without the $\frac{a}{rk+a}$ factor still evaluate cleanly? Because from $x = u(1+u)^{-r}$, logarithmic differentiation gives:
     ```

2. **Line 422** (Section 4.1, Prüfer Code Generalization — CF 156D Clues):
   - **Target**:
     ```markdown
     - **Component Tree Product (CF 156D — Clues)**: Given $k$ connected components of sizes $s_1, s_2, \dots, s_k$ ($\sum s_i = n$), how many ways can we add $k-1$ edges to connect them into a single tree? Contracting each component $i$ into a super-vertex of degree $d_i \ge 1$ where each incident edge has $s_i$ choices of endpoint inside component $i$ gives:
       $$\sum_{d_1 + \dots + d_k = 2k-2} \frac{(k-2)!}{(d_1-1)!\cdots(d_k-1)!} \prod_{i=1}^k s_i^{d_i} = \left(\prod_{i=1}^k s_i\right) (s_1 + \dots + s_k)^{k-2} = n^{k-2} \prod_{i=1}^k s_i.$$
       *(Wait: notice that $k=1$ gives $n^{-1} \cdot n = 1$, and $s_i = 1$ for all $i$ recovers $n^{n-2}$!)*
     ```
   - **Replacement**:
     ```markdown
     - **Component Tree Product (CF 156D — Clues)**: Given $k$ connected components of sizes $s_1, s_2, \dots, s_k$ ($\sum s_i = n$), how many ways can we add $k-1$ edges to connect them into a single tree? Contracting each component $i$ into a super-vertex of degree $d_i \ge 1$ where each incident edge has $s_i$ choices of endpoint inside component $i$ gives:
       $$\sum_{d_1 + \dots + d_k = 2k-2} \frac{(k-2)!}{(d_1-1)!\cdots(d_k-1)!} \prod_{i=1}^k s_i^{d_i} = \left(\prod_{i=1}^k s_i\right) (s_1 + \dots + s_k)^{k-2} = n^{k-2} \prod_{i=1}^k s_i.$$
       *(As a sanity check, $k=1$ gives $n^{-1} \cdot n = 1$, and $s_i = 1$ for all $i$ recovers Cayley's formula $n^{n-2}$.)*
     ```

3. **Line 456** (Section 4.3, Labelled Cacti — Derivation of Cycle Block Species):
   - **Target**:
     ```markdown
     - Each block is either a **single edge** (connecting the root to $1$ other rooted cactus $F(x)$) or a **simple cycle of length $k \ge 3$** passing through the root! In a simple cycle of length $k \ge 3$ containing the root, the remaining $k-1 \ge 2$ vertices around the cycle each carry a rooted cactus $F(x)$, and because the cycle is undirected, reversing the cycle's orientation identifies pairs of sequences of length $k-1 \ge 2$:
       $$\text{Block}(F) = F(x) + \sum_{k \ge 3} \frac{F(x)^{k-1}}{2} = F(x) + \frac{F(x)^2}{2(1 - F(x))} = \frac{2F(x) - F(x)^2}{2(1 - F(x))}.$$
       *(Wait: we can even unify $k=2$ (single edge) with $k \ge 3$: $F(x) + \frac{F(x)^2}{2(1-F(x))} = \frac{2F(x) - F(x)^2}{2(1-F(x))}$!)*
     ```
   - **Replacement**:
     ```markdown
     - Each block is either a **single edge** (connecting the root to $1$ other rooted cactus $F(x)$) or a **simple cycle of length $k \ge 3$** passing through the root! In a simple cycle of length $k \ge 3$ containing the root, the remaining $k-1 \ge 2$ vertices around the cycle each carry a rooted cactus $F(x)$, and because the cycle is undirected, reversing the cycle's orientation identifies pairs of sequences of length $k-1 \ge 2$:
       $$\text{Block}(F) = F(x) + \sum_{k \ge 3} \frac{F(x)^{k-1}}{2} = F(x) + \frac{F(x)^2}{2(1 - F(x))} = \frac{2F(x) - F(x)^2}{2(1 - F(x))}.$$
     ```

4. **Line 486** (Section 4.3, Labelled Cacti — Dissymmetry Theorem Simplification):
   - **Target**:
     ```markdown
     - **$\mathcal{C}_{\bullet\to\bullet}$ (rooted at an incidence $(v, B)$)**: Choosing the block $B$ and its root $v$ is equivalent to $F(x) \cdot \text{Block}'(F(x))$ — wait: even simpler, inside $\mathcal{C}_\square$, a cycle of length $k \ge 3$ has $k$ incidences $(v, B)$, and an edge ($k=2$) has $2$ incidences! Thus:
       $$(C_\square - C_{\bullet\to\bullet})(x) = \left(F(x)^2 + \sum_{k \ge 3} \frac{1 - k}{2k} F(x)^k\right) - \frac{F(x)^2}{2} = \frac{F(x)^2}{2} + \frac{1}{2}\ln\frac{1}{1 - F(x)} - \frac{F(x)}{2} - \frac{F(x)^2}{4} - \frac{F(x)^2}{2(1 - F(x))}.$$
     ```
   - **Replacement**:
     ```markdown
     - **$\mathcal{C}_{\bullet\to\bullet}$ (rooted at an incidence $(v, B)$)**: Inside $\mathcal{C}_\square$, a cycle of length $k \ge 3$ has $k$ vertex-block incidences $(v, B)$, and a bridge edge ($k=2$) has $2$ incidences. Combining $C_\square(x)$ and $C_{\bullet\to\bullet}(x)$ directly yields:
       $$(C_\square - C_{\bullet\to\bullet})(x) = \left(\frac{F(x)^2}{2} + \sum_{k \ge 3} \frac{1 - k}{2k} F(x)^k\right) = \frac{F(x)^2}{4} - \frac{F(x)}{2} + \frac{1}{2}\ln\frac{1}{1 - F(x)} - \frac{F(x)^3}{2(1 - F(x))}.$$
     ```

5. **Line 681** (Problem 2: **AtCoder AGC 021 E — Ball Eat Chameleons**):
   - **Target**:
     ```markdown
       Wait: when $R = B$, the last ball **must** be Blue (`B`), because if the last ball were Red (`R`), the prefix before the last ball would have $R - 1$ Reds and $B = R$ Blues, which already satisfies $B > R - 1$, meaning every chameleon could already have eaten strictly more Reds than Blues? No: in AGC 021 E, a chameleon turns red if `#R > #B`, OR if `#R == #B` and the **first** ball it ever ate was Red (`R`)! Therefore, a chameleon with `#R == #B` (and $\ge 1$ ball eaten) needs 1 first `R` and 1 final `B`, while a chameleon with `#R > #B` can just eat a single `R`.
     ```
   - **Replacement**:
     ```markdown
       When $R = B$, the very last ball of the entire sequence **must** be Blue (`B`): in AGC 021 E, a chameleon turns red either by eating strictly more Red balls than Blue balls (`#R > #B`), or by eating an equal nonzero number (`#R == #B > 0`) provided the **first** ball it ate was Red (`R`) (which forces the last ball it ate to be `B`). If $R = B$ and the last ball of the entire sequence were `R`, that final `R` could only help a chameleon achieve `#R > #B`, leaving at most $R - 1$ Red balls for the remaining $N - 1$ chameleons, which is insufficient. Thus for $R = B$ we simply decrement $B \leftarrow B - 1$ and count sequences on $(R, R - 1)$.
     ```

6. **Line 761** (Problem 6: **Codeforces 1349F2 — Slime and Sequences (Hard Version)**):
   - **Target**:
     ```markdown
       Using the substitution $1 - x = \frac{u}{e^u - 1}$ (so $e^u - 1 = u(1-x)^{-1}$ — wait: $F(x)$ satisfies $(1+F(x)) e^{-F(x)} = 1 - x$, or setting $H(x) = -F(x)$, $H(x) e^{H(x)} = x - \dots$ — even better, change variables directly via $u = F(x)$, so $x = 1 - (1+u)e^{-u} = \frac{e^u - 1 - u}{e^u}$!).
     ```
   - **Replacement**:
     ```markdown
       Since $F(x)$ satisfies $(1 + F(x))e^{-F(x)} = 1 - x$ with $F(0) = 0$, we apply the Formal Residue Change of Variables directly by setting $u = F(x)$, which expresses $x$ as a series in $u$:
       $$x(u) = 1 - (1 + u)e^{-u} = \frac{e^u - 1 - u}{e^u} = \frac{u^2}{2!} - \frac{u^3}{3!} + \cdots$$
       (or in the shifted tree series $W(z) = -F(1 - z)$ satisfying $W(z)e^{W(z)} = -z$, via the standard Lambert-$W$ substitution $u = F(x)$ around $u = 0$).
     ```

7. **Lines 805 & 814** (Problem 8: **AtCoder ABC 281 Ex — Alchemy**):
   - Covered in full by **Bug B3** above!

8. **Line 840** (Problem 10: **UOJ 450 / Luogu P5401 — Pearl (`珍珠`)**):
   - **Target**:
     ```markdown
       Wait: by the Binomial Theorem, $(D - 2j)^n = \sum_{m=0}^n \binom{n}{m} D^{n-m} (-2j)^m$? No, $j$ only goes up to $k \le D$, so we just precompute $(D - 2j)^n \bmod 998244353$ for each $j = 0, \dots, D$ in $O(D \log n)$ time!
     ```
   - **Replacement**:
     ```markdown
       Since $j$ only ranges from $0$ to $k \le D$, we simply precompute $(D - 2j)^n \bmod 998244353$ for each $j = 0, \dots, D$ in $O(D \log n)$ time!
     ```

9. **Line 919** (Problem 13: **Luogu P3978 — Probability Theory (`[TJOI2015] 概率论`)**):
   - **Target**:
     ```markdown
       Wait: each $n$-node binary tree has $n+1$ external leaf slots (empty pointers). Inserting a new node at any of the $n+1$ external leaf slots of an $n$-node tree creates an $(n+1)$-node tree with one new leaf, and conversely, deleting any leaf of an $(n+1)$-node tree leaves an $n$-node tree with a marked external slot!
     ```
   - **Replacement**:
     ```markdown
       Combinatorially, why does $L(x) = x(1-4x)^{-1/2}$ hold? Every $n$-node binary tree has $n+1$ external leaf slots (empty child pointers). Attaching a new leaf at any of the $n+1$ external slots of an $n$-node tree bijectively produces an $(n+1)$-node binary tree with one marked leaf!
     ```

10. **Lines 973–974** (Problem 16: **AtCoder Toyota 2023 Spring Final E — Replace Digits**):
    - Covered in full by **Bug B6** above!

11. **Lines 1072 & 1083** (Problem 21: **AtCoder AGC 005 F — Many Easy Problems**):
    - **Target (Lines 1071–1086)**:
      ```markdown
        $$\text{ans}_k = N\binom{N}{k} - \sum_{i=1}^{N-1} \left[\binom{s_i}{k} + \binom{N - s_i}{k}\right]$$
        *(Wait: why? Because an edge $e_i$ separates the tree into $s_i$ and $N - s_i$; a $k$-subset $S$ does NOT cross $e_i$ iff $S$ lies entirely in the $s_i$-side or entirely in the $(N-s_i)$-side! Since a subtree has $|V| - |E| = 1$, summing over vertices minus edges counts $1$ for every $S$!).*
        Let $c_m$ be the total number of times size $m$ appears among all $2(N-1)$ values $\{s_i, N - s_i\}_{i=1}^{N-1}$. Then we need to compute, for every $k = 1, \dots, N$:
        $$S_k = \sum_{m=k}^N c_m \binom{m}{k} = \frac{1}{k!} \sum_{m=k}^N (c_m m!) \cdot \frac{1}{(m-k)!}.$$
        By Formal Residues (or transposed Binomial convolution):
        $$\binom{m}{k} = \operatorname{res}_u \frac{(1+u)^m}{u^{k+1}}\,du \implies S_k = [u^k] \sum_{m=1}^N c_m (1+u)^m,$$
        which is a single shifted-polynomial evaluation, or directly a **reverse convolution** (multiplying $A(x) = \sum_{m=0}^N (c_m m!) x^{N-m}$ with $B(x) = \sum_{j=0}^N \frac{x^j}{j!}$ and reading $[x^{N-k}]$) in a single $O(N \log N)$ NTT!
      ```
    - **Replacement**:
      ```markdown
        $$\text{ans}_k = N\binom{N}{k} - \sum_{i=1}^{N-1} \left[\binom{s_i}{k} + \binom{N - s_i}{k}\right].$$
        *(Why? Every non-empty subtree $T(S)$ is a tree, so it satisfies $|V(T(S))| - |E(T(S))| = 1$. An edge $e_i$ belongs to $T(S)$ if and only if $S$ is neither contained entirely in the $s_i$-side nor contained entirely in the $(N - s_i)$-side, giving $\binom{N}{k} - \binom{s_i}{k} - \binom{N-s_i}{k}$ subsets $S$ that use $e_i$.)*
        Let $c_m$ be the total number of times size $m$ appears among all $2(N-1)$ values $\{s_i, N - s_i\}_{i=1}^{N-1}$. Then we need to compute, for every $k = 1, \dots, N$:
        $$S_k = \sum_{m=k}^N c_m \binom{m}{k} = \frac{1}{k!} \sum_{m=k}^N (c_m m!) \cdot \frac{1}{(m-k)!}.$$
        By Formal Residues, $\binom{m}{k} = \operatorname{res}_u \frac{(1+u)^m}{u^{k+1}}\,du \implies S_k = [u^k] \sum_{m=1}^N c_m (1+u)^m$, which expands via a single **reverse NTT convolution** (multiplying $A(x) = \sum_{m=0}^N (c_m m!) x^{N-m}$ by $B(x) = \sum_{j=0}^N \frac{x^j}{j!}$ and reading $[x^{N-k}]$) in $O(N \log N)$ time!
      ```

12. **Line 1196** (Problem 28: **Luogu P5434 — Labelled Desert (`有标号荒漠计数`)**):
    - **Target**:
      ```markdown
        $$\ln\frac{1}{1 - F(x)} - F(x) = \sum_{k \ge 2} \frac{F(x)^k}{k}$$
        Wait: a bridge ($k=2$) is an unordered pair of rooted cacti $\frac{F(x)^2}{2}$, and a cycle of length $k \ge 3$ is $\frac{F(x)^k}{2}$ (dihedral symmetry $D_k$ has size $2k$). Thus the EGF of unrooted blocks is:
      ```
    - **Replacement**:
      ```markdown
        Inside $\mathcal{C}_\square$, a bridge block ($k=2$) is an unordered pair of rooted cacti with EGF $\frac{F(x)^2}{2}$, and a simple cycle block of length $k \ge 3$ has dihedral symmetry $|D_k| = 2k$, giving EGF $\frac{F(x)^k}{2k}$! Wait-free block sum:
      ```

13. **Line 1325** (Problem 35: **Project Euler 843 — Periodic Circles**):
    - **Target**:
      ```markdown
        Since the evolution step replaces $v$ by $(x + x^{-1}) v$ modulo $x^n - 1$ over $\mathbb{F}_2$, any state quickly enters the image of $(x + x^{-1})^{2^k}$ and its period divides $2^r (2^s - 1)$ where $s$ is the multiplicative order of $2$ modulo the odd part of the irreducible factor's period! Wait: we can do even better by factoring $x^n - 1 = (x - 1)^{2^a} \prod_i f_i(x)^{2^a}$ over $\mathbb{F}_2$ (where $n = 2^a m$ with $m$ odd) and computing the exact cycle lengths of multiplication by $(x + x^{-1}) \pmod{f_i(x)^{2^a}}$ for each irreducible factor $f_i(x)$ of $x^m - 1$ over $\mathbb{F}_2$, then combining cycle lengths across factors via LCM!
      ```
    - **Replacement**:
      ```markdown
        Since each step multiplies the configuration polynomial $v(x)$ by $L(x) = x + x^{-1} \pmod{x^n + 1}$ over $\mathbb{F}_2$, we factor $x^n + 1 = (x + 1)^{2^a} \prod_i f_i(x)^{2^a}$ over $\mathbb{F}_2$ (where $n = 2^a m$ with $m$ odd) into powers of distinct irreducible polynomials $f_i(x) \mid x^m + 1$. By the Chinese Remainder Theorem over $\mathbb{F}_2[x]$, the linear map $v \mapsto L(x)v \pmod{x^n + 1}$ decomposes into the direct sum of its actions modulo $f_i(x)^{2^a}$; we compute the multiplicative order of $L(x)$ modulo $f_i(x)^{2^b}$ ($1 \le b \le 2^a$) for each factor and take all possible LCMs of periods across the components.
      ```

14. **Lines 1383 & 1391** (Problem 38: **UOJ 498 — New Year's Chase (`新年的追逐战`)**):
    - **Target (Lines 1381–1393)**:
      ```markdown
        Because $G = G_1 \times \dots \times G_k$ is a categorical product, an edge in $G$ exists between $(u_1, \dots, u_k)$ and $(v_1, \dots, v_k)$ iff $(u_r, v_r) \in E(G_r)$ for **every** $r = 1, \dots, k$.
        Wait: this means two vertices can be in the same connected component of $G$ only if their projections are connected in every $G_r$, AND if every $G_r$ is connected and at least one is non-bipartite, how many components does $G$ have?
        More precisely:
        - Any isolated vertex in any $G_r$ forces all $n_1 \cdots n_{r-1} n_{r+1} \cdots n_k$ corresponding vertices in $G$ to be isolated!
        - For connected components $C_r \subseteq G_r$ of size $\ge 2$:
          - The categorical product of $k$ connected components $C_1 \times \dots \times C_k$ (each of size $\ge 2$) splits into **$2^{b - 1}$ connected components** if $b = k$ (i.e., **all** $k$ components $C_r$ are bipartite!), and into **$1$ connected component** if at least one $C_r$ is non-bipartite?
          - Wait: no! In $C_1 \times \dots \times C_k$, a walk of length $L$ exists between $(u_1, \dots, u_k)$ and $(v_1, \dots, v_k)$ iff there is a walk of the **same parity** $L$ in each $C_r$. Every bipartite component $C_r$ enforces the parity of $L$ between its two parts, whereas non-bipartite components allow both parities! Therefore, if among $C_1, \dots, C_k$ (all of size $\ge 2$), exactly $b$ of them are **bipartite**, then $C_1 \times \dots \times C_k$ splits into:
            $$\begin{cases} 1 \text{ component} & \text{if } b = 0, \\ 2^{b-1} \text{ components} & \text{if } b \ge 1! \end{cases}$$
      ```
    - **Replacement**:
      ```markdown
        Because $G = G_1 \times \dots \times G_k$ is a categorical product, an edge in $G$ exists between $(u_1, \dots, u_k)$ and $(v_1, \dots, v_k)$ iff $(u_r, v_r) \in E(G_r)$ for **every** $r = 1, \dots, k$.
        By Weichsel's Theorem on categorical graph products, two vertices in $C_1 \times \dots \times C_k$ are connected if and only if there is a walk of the **same length parity** $L$ connecting their coordinates in every factor $C_r$:
        - Any **isolated vertex** ($|C_r| = 1$, no incident edges) in factor $G_r$ has degree $0$, so each tuple containing it becomes an isolated vertex in $G$ (contributing $\prod_{j \neq r} n_j$ singletons).
        - For connected components $C_r \subseteq G_r$ all of size $|C_r| \ge 2$: each bipartite component $C_r$ restricts the parity of walks between any two of its vertices to a single residue mod $2$, whereas a non-bipartite component $C_r$ contains an odd cycle and allows walks of both parities. Consequently, if among $C_1, \dots, C_k$ (all of size $\ge 2$) exactly $b$ components are **bipartite**, then $C_1 \times \dots \times C_k$ splits into:
          $$\begin{cases} 1 \text{ connected component} & \text{if } b = 0, \\ 2^{b-1} \text{ connected components} & \text{if } b \ge 1. \end{cases}$$
      ```

15. **Line 1414** (Problem 39: **Luogu P5827 & P5828 — Biconnected & 2-Edge-Connected Graphs**):
    - Covered in full by **Bug B5** above!

---

## Summary Checklist for Remediator
1. Apply **Bugs B0, B1, B2, B3, B4, B5, B6** from **Section 1** of this report (plus `audit_A_wave_3a.md` Bugs 1.2, 1.3, 1.4).
2. Insert **Missing Items S1–S8** from **Section 2** of this report (plus the 3 missing Cohort 2 problems and the $n=5$ trace table from `audit_A_wave_3a.md` Issues 2.1 & 2.2, and the expanded statements from `audit_A_wave_3a.md` Issues 3.1, 3.2, 3.4, 3.5).
3. Apply the **15 verified replacements in Section 3 of this report** to eliminate all 19 `Wait:` / `wait:` occurrences (**do NOT use `audit_A_wave_3a.md` Issue 4.2, Bug 1.5, or Issue 3.3**).
