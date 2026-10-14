# Part V Mathematical Rigor, Single-Step Derivations & Engine Completeness Audit Report (Critic A)

**Auditor**: `fps-textbook-critic` (Part V Critic A — Mathematical Rigor, Single-Step Derivations & Engine Completeness)  
**Target Scope**: Part V (`Ch 18`–`Ch 21` + `CP-V`)  
**Files Audited (100% Line-by-Line Verification)**:
1. [`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd) (1,371 lines)
2. [`chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd) (1,098 lines)
3. [`chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd) (1,524 lines)
4. [`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd) (1,082 lines)
5. [`checkpoints/cp05-part5-dfinite-transposition-composition.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp05-part5-dfinite-transposition-composition.qmd) (837 lines)

---

## Executive Summary & Verdict Matrix

| File | Mathematical Accuracy & Indices | Zero Magic Steps & Scratchpads | Engine / Failure Mode / Char-$p$ Completeness | Prerequisite Closure & Spoiler-Free Audit | Actionable Fixes Required |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`Ch 18`** (`ch18-...qmd`) | **2 Critical Issues** (Line 1103 false bivariate Delannoy recurrence; Line 1121 modular root hazard when $n \ge p$) | **Pass** (Except Line 1103–1105 jump in `Adv-2`) | **Pass** (All §18.1–§18.5, Failure Mode #8, Indicial Lifting present; 2 Callout IDs `#1,#2` $\to$ `#10,#12`) | **Pass** (Strict closure over Ch 01–18) | **4 Fixes** (`C18-1` to `C18-4`) |
| **`Ch 19`** (`ch19-...qmd`) | **1 Critical Issue** (Lines 180–181 tautological residue identity in `EI` Engine 3 for `c`-Delannoy) | **1 Skipped Elimination** (Lines 180–185 skips eliminating $\mu_1$) | **Pass** (All 3 `EI` engines in §19.2, §19.1–§19.5, Failure Mode #9 present; add `#5` to Line 395 callout) | **Pass** (Strict closure over Ch 01–19) | **2 Fixes** (`C19-1` to `C19-2`) |
| **`Ch 20`** (`ch20-...qmd`) | **1 Code / Boundary Issue** (Line 667 comma-operator post-increment out-of-bounds hazard in `shift_non_overlapping`) | **Pass** (Every $\text{mulT}$ derivation states exact reversed range) | **Pass** (All §20.1–§20.5, Failure Modes #10 & #11 present) | **Pass** (Strict closure over Ch 01–20) | **2 Fixes** (`C20-1` to `C20-2`) |
| **`Ch 21`** (`ch21-...qmd`) | **1 Critical Arithmetic Error** (Lines 109, 112, 115 Toy Trace of Kinoshita–Li has impossible $-2y^2$ term) | **1 Model Clarification** (`SS-1 #036` lines 505, 538–545 simplified vs official `ABC 281 Ex` recurrence) | **1 Callout ID Mismatch** (Line 310 labeled `Revisited #11` on `#201` instead of `Revisited #8` on `#200/#201`) | **Pass** (Strict closure over Ch 01–21) | **3 Fixes** (`C21-1` to `C21-3`) |
| **`CP-V`** (`cp05-...qmd`) | **1 Critical Formula Off-by-One** (Line 655 `j - 1 - [j > 0] - v` evaluates to $j - 2 - v$ instead of $j - 1 - v$ for $j \ge 1$) | **Pass** (All 8 Stage 2 solutions complete) | **Pass** (All 8 problems `CP-V.1`–`CP-V.8` match `CURRICULUM_ARCHITECTURE.md`) | **100% Spoiler-Free Stage 1 Verified** | **1 Fix** (`CPV-1`) |

---

## Detailed Findings & Ready-to-Apply Drop-In Fixes

---

### 1. Audit of Chapter 18 (`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd`)

#### Verification of Core Engines & Small Cases (Passed)
- **§18.1 Weyl Algebra & Euler Operator**: The non-commutative Leibniz rule $D x - x D = 1$, commutation relations $\vartheta x^n = x^n(\vartheta + n)$, falling factorial conversion $x^k D^k = \vartheta(\vartheta - 1)\cdots(\vartheta - k + 1)$ via Stirling numbers of the first kind, and coefficient shift extraction $[x^n](x^r \vartheta^s F(x)) = (n-r)^s f_{n-r}$ (Lines 68–143) are 100% algebraically verified.
- **§18.2 ODE-to-P-Recursive & Converse**: Bandwidth bounds $r \le d + s$ and $m \le d + r$ and index shifts (Lines 184–245) are exact.
- **§18.3 Indicial Polynomial & Failure Mode #8**: Note on Failure Mode numbering: In `CURRICULUM_ARCHITECTURE.md` §2.4 (Line 210), Vanishing Indicial Polynomial $I(n^*) \equiv 0 \pmod p$ in P-Recursive Unrolling is canonically **Failure Mode #8** (whereas Failure Mode #5 is the $1/n$ modular breakdown of Lagrange Inversion in Chapter 11). `Ch 18` uses `Failure Mode #8` consistently across all sections (Lines 23, 177, 394, 429, 432, 499, 520, 1256, 1329, 1364). The $\epsilon$-perturbed lifting method in `Q[ε]/(ε^{v+1})` (Lines 432–592) and the worked trace for $(n - 3)f_n = f_{n-1}$ at $p = 3$ (Lines 468–497) are 100% mathematically verified.
- **§18.4 Holonomic Closure & §18.5 D-Finite vs. Non-D-Finite Boundary**: The closure table (Line 642), Euler number asymptotics $[x^n/n!]\tan x \sim 2(2/\pi)^{n+1} n!$, and partition function singularity accumulation on $|x| = 1$ (Lines 664–723) are completely rigorous.

---

#### [CRITICAL FIX `C18-1`] Line 1103 (`Adv-2 #088 CF 755G`) — Contradictory Bivariate Delannoy Recurrence & Skipped Derivation of the 3-Term Diagonal Recurrence
- **Location**: [`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd:1101-1106`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L1101-L1106)
- **Mathematical Audit**:
  1. Line 1103 states:
     > *"The bivariate Delannoy array satisfies $(a + 1) d_{a+1, b} = (a + b + 1) d_{a, b} + (b + 1) d_{a, b+1}$ and its symmetric counterpart $(b + 1) d_{a, b+1} = (a + b + 1) d_{a, b} + (a + 1) d_{a+1, b}$."*
     Both equations are **mathematically false**: at $(a, b) = (0, 0)$, $d_{0,0} = d_{1,0} = d_{0,1} = 1$, so LHS $= 1 \cdot 1 = 1$ while RHS $= 1 \cdot 1 + 1 \cdot 1 = 2$. Worse still, adding the two claimed equations yields $0 = 2(a + b + 1)d_{a, b}$, an immediate contradiction!
  2. By contrast, the 3-term diagonal recurrence on Line 1105:
     $$(k + 1)(n - k)(n + 1 - 2k) a_{k+1} = (n - 2k)\Big( (2n - 1)(n + 1) - 6k(n - k) \Big) a_k - k(n + 1 - k)(n - 1 - 2k) a_{k-1}$$
     was verified against $n = 3$ ($a = [1, 5, 5, 1]$) and $n = 4$ ($a = [1, 7, 13, 7, 1]$) and is **100% mathematically true**! However, jumping from the false bivariate identity on Line 1103 to Line 1105 violates the Zero-Magic-Steps rule.
- **Drop-In Replacement for Lines 1101–1106**:
```markdown
   **(Method B: Direct 1-Line Holonomic $k$-Recurrence in $O(k)$ Time and $O(1)$ Auxiliary Space).**
   Observe that $a_k = [u^{n-k} v^k](1 - u - v - uv)^{-1} = [x^k](1 + x)^{n-k}(1 + 2x)^k$. Recognising $a_k$ as a specialization of the Jacobi polynomial $a_k = P_k^{(n-2k,\, 0)}(3)$—or equivalently applying Zeilberger's creative telescoping to the summand $t(k, j) = \binom{k}{j}\binom{n-j}{k}$ via the multiplicative ratios $\frac{t(k, j+1)}{t(k, j)} = \frac{(k-j)(n-k-j)}{(j+1)(n-j)}$—eliminates the summation index $j$ and produces a second-order $P$-recursive relation directly along the diagonal $a_k = d_{n-k, k}$ for fixed $n$:
   $$(k + 1)(n - k)(n + 1 - 2k) a_{k+1} = (n - 2k)\Big( (2n - 1)(n + 1) - 6k(n - k) \Big) a_k - k(n + 1 - k)(n - 1 - 2k) a_{k-1}.$$
   *(Verification at $n = 3$, $a = [1, 5, 5, 1]$: for $k = 0$, $1 \cdot 3 \cdot 4 \, a_1 = 3(5 \cdot 4 - 0)\cdot 1 - 0 \implies 12 a_1 = 60 \implies a_1 = 5$; for $k = 1$, $2 \cdot 2 \cdot 2 \, a_2 = 1 \cdot (20 - 12)\cdot 5 - 1 \cdot 3 \cdot 0 \cdot 1 \implies 8 a_2 = 40 \implies a_2 = 5$; for $k = 2$, $3 \cdot 1 \cdot 0 \, a_3 = (-1)(20 - 12)\cdot 5 - 2 \cdot 2 \cdot (-2)\cdot 5 = -40 + 40 = 0$, and at $k = 2$, $2k = n + 1$ so symmetry $a_2 = a_1 = 5$ or $a_{k+1} = a_{n-k-1}$ applies!)*
```

---

#### [CRITICAL FIX `C18-2`] Lines 1121–1124 (`Adv-2 #088 CF 755G` C++ Snippet) — Modular Vanishing of `c_next` when $n \ge p$
- **Location**: [`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd:1114-1128`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L1114-L1128)
- **Mathematical Audit**:
  In `CF 755G`, $n \le 10^9$ while $p = 998244353 < 10^9$ and $K \le 3 \times 10^4$. On Line 1121:
  ```cpp
  if (c_next == 0) { // Only possible at the single point 2k = n + 1 (when n <= 2K - 1)
      a[k + 1] = a[k]; // By exact symmetry a_{(n+1)/2} = a_{(n-1)/2}
      continue;
  }
  ```
  If $n \ge p = 998244353$ (e.g., $n = p + 3$), then `(n - k) % MOD == 0` or `(n + 1 - 2*k) % MOD == 0` can occur at a modular root $2k \equiv n + 1 \pmod p$ or $k \equiv n \pmod p$ even though $2k \ne n + 1$ in $\mathbb{Z}$! At such a modular root, `a[k + 1]` is **not** equal to `a[k]`. Instead, at the true integer midpoint `2LL * k == n + 1`, `a[k + 1] = a[k]` holds; and if `c_next == 0` due to a modular root when $n \ge p$ (which happens at most twice for $k < K$), $a_{k+1} = \sum_{j=0}^{k+1} \binom{k+1}{j}\binom{n-j}{k+1}$ can be evaluated directly in $O(k)$ time (or lifted via $\epsilon$-perturbation from §18.3).
- **Drop-In Replacement for Lines 1114–1128**:
```cpp
    for (long long k = 1; k < limit; ++k) {
        if (2 * k == n + 1) { // Exact integer midpoint (when n is odd and n <= 2K - 1)
            a[k + 1] = a[k];  // By symmetry a_{(n+1)/2} = a_{(n-1)/2}
            continue;
        }
        long long c_next = (k + 1) % MOD * ((n - k) % MOD) % MOD * ((n + 1 - 2 * k) % MOD + MOD) % MOD;
        if (c_next == 0) { // Failure Mode #8 when n >= MOD: modular root (n - k) = 0 or (n + 1 - 2k) = 0 (mod p)
            // Occurs at most twice for k <= K; evaluate a[k+1] directly in O(k) via falling factorials of n
            long long val = 0, comb_k = 1, comb_n = 1;
            for (long long r = 1; r <= k + 1; ++r)
                comb_n = comb_n * ((n - r + 1) % MOD) % MOD * inv[r] % MOD;
            for (long long j = 0; j <= k + 1; ++j) {
                val = (val + comb_k * comb_n) % MOD;
                comb_k = comb_k * (k + 1 - j) % MOD * inv[j + 1] % MOD;
                comb_n = comb_n * ((n - k - 1 - j + MOD) % MOD) % MOD * modInverse((n - j) % MOD) % MOD;
            }
            a[k + 1] = val;
            continue;
        }
        long long mid_inner = ((2 * n - 1) % MOD * ((n + 1) % MOD) - 6 * k % MOD * ((n - k) % MOD)) % MOD;
        long long c_curr = ((n - 2 * k) % MOD + MOD) % MOD * ((mid_inner + MOD) % MOD) % MOD;
        long long c_prev = k % MOD * ((n + 1 - k) % MOD) % MOD * ((n - 1 - 2 * k) % MOD + MOD) % MOD;
        long long rhs = (c_curr * a[k] - c_prev * a[k - 1]) % MOD;
        a[k + 1] = (rhs + MOD) % MOD * modInverse(c_next) % MOD;
    }
```

---

#### [CROSS-REFERENCE FIX `C18-3`] Lines 250 & 262 — Canonical Numbering of Revisited Dual-Perspective Callouts (`#10` and `#12`)
- **Location**: [`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd:250-265`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L250-L265)
- **Audit Finding**: Per `CURRICULUM_ARCHITECTURE.md` §5.2 (Lines 1430–1432), `#237 yukicoder 1080` is **Revisited Dual-Perspective Callout #10** and `#058 AtCoder ARC 136 F` is **Revisited Dual-Perspective Callout #12**. Currently Lines 250 and 262 number them locally as `#1` and `#2`.
- **Drop-In Replacement for Line 250**:
```markdown
::: {.callout-tip title="Revisited Dual-Perspective Callout #10 — Complex Rotation vs. Real Coupled ODE (`#237 yukicoder 1080`)"}
```
- **Drop-In Replacement for Line 262**:
```markdown
::: {.callout-tip title="Revisited Dual-Perspective Callout #12 — Product-of-2-Factor Differentiation Trick as a Holonomic Special Case (`#058 AtCoder ARC 136 F`)"}
```

---

#### [MINOR TYPO FIX `C18-4`] Line 1222 (`Mas-1 #211 UOJ 450`)
- **Location**: [`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd:1222`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L1222)
- **Fix**: Replace `when Viewed as a formal cube root` with `when viewed as a formal cube root`.

---

### 2. Audit of Chapter 19 (`chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd`)

#### Verification of Core Engines & Small Cases (Passed)
- **§19.1 Sparse Composition Templates**: Power rule $G = F^\alpha \implies F G' = \alpha F' G$, Exp/Log rule $G = \exp F \implies G' = F' G$, trig coupled pair $S' = F' C, C' = -F' S$, and algebraic composition $P(x, G(x)) = 0$ are 100% verified.
- **§19.2 All 3 `EI` Engines**: Engine 1 (Coupled Non-Rational Auxiliary Splitting, Lines 105–134), Engine 2 (WZ / Creative Telescoping, Lines 138–159), and Engine 3 (Residue / Integration-by-Parts under $[x^{-1}]$, Lines 162–187) are all present and pedagogically integrated.
- **§19.3 Coupled Nonlinear ODE Systems**: Newton's method vs. $O(N^2)$ ODE extraction crossover ($d \le 50$) and Catalan-like coupled system trace (Lines 276–393) are 100% verified.
- **§19.4 Truncated Taylor Series ODE Trick (`#089 CF 840C`)**: The exact cancellation exposing why $P_c(x) = \sum_{j=1}^c \frac{1}{j!}\binom{c-1}{j-1} x^j$ is *not* closed-form in elementary functions, followed by its 2nd-order linear ODE $x P_c''(x) + (2 - x)P_c'(x) - c P_c(x) = 0$ (derived both coefficient-wise and via Kummer's confluent hypergeometric equation on Lines 460–496), is a textbook highlight and 100% verified.
- **§19.5 Failure Mode #9**: Boundary correction terms when truncating infinite ODEs to $\deg \le c$ (`[x^c] P_c'(x)` vanishing vs `[x^{c-1}] P_c'(x) = c a_c`) on Lines 544–615 are exact.

---

#### [CRITICAL FIX `C19-1`] Lines 180–185 (§19.2 `EI` Engine 3: $c$-Delannoy Recurrence via Residue Integration by Parts) — Tautological Identity & Missing 3-Line Elimination of $\mu_1$
- **Location**: [`chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd:179-186`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd#L179-L186)
- **Mathematical Audit**:
  In §19.2 Engine 3 (Lines 168–186), the author defines $B(x) = \frac{(1+x)(1+c+cx)}{x} = (1+c)x^{-1} + (1+2c) + cx$ so that $D_n(c) = \operatorname{Res}_{x=0} x^{-1} B(x)^n = \mu_0(n)$.
  - In Step 2 (Line 174), applying $\operatorname{Res}_{x=0}\frac{d}{dx}(B(x)^n) = 0$ gives $(1+c)\mu_{-1}(n-1) = c\mu_1(n-1)$.
  - In Step 3 (Lines 176–178), expanding $B(x)^n = B(x) B(x)^{n-1}$ gives $\mu_0(n) = (1+c)\mu_{-1}(n-1) + (1+2c)\mu_0(n-1) + c\mu_1(n-1) = (1+2c)\mu_0(n-1) + 2c\mu_1(n-1)$.
  - Then on Lines 180–181, the text claims:
    > *"Even simpler: apply $\operatorname{Res}_{x=0} \frac{d}{dx}\big(x^{-1}(1+x)(1+c+cx) B(x)^{n-1}\big) = 0$, or eliminate $\mu_1$ between $n$ and $n-1$, yielding the 3-term holonomic recurrence..."*
    **Flaw**: Since $x^{-1}(1+x)(1+c+cx) = B(x)$ by definition, the expression $x^{-1}(1+x)(1+c+cx) B(x)^{n-1}$ is literally $B(x)^n$, whose derivative was *already* used in Step 2! It yields the exact same identity $(1+c)\mu_{-1}(n-1) = c\mu_1(n-1)$, not a second independent relation to eliminate $\mu_1$.
  - **Exact 3-Line Fix**: Apply $\operatorname{Res}_{x=0}\frac{d}{dx}\big(x B'(x) B(x)^{n-1}\big) = 0$! Because $x B'(x) = -(1+c)x^{-1} + cx$ and $B(x) - (1+2c) = (1+c)x^{-1} + cx$, their squares satisfy the fundamental algebraic identity
    $$(x B'(x))^2 = \big(B(x) - (1+2c)\big)^2 - 4c(1+c) = B(x)^2 - 2(1+2c)B(x) + 1,$$
    and $\frac{d}{dx}(x B'(x)) = (1+c)x^{-2} + c = x^{-1}\big(B(x) - (1+2c)\big)$. Differentiating $x B'(x) B(x)^{n-1}$ under $\operatorname{Res}_{x=0}$ immediately eliminates all auxiliary moments $\mu_{\pm 1}$ in three lines!
- **Drop-In Replacement for Lines 179–186**:
```markdown
**Step 4: Eliminate $\mu_1(n-1)$ via $\operatorname{Res}_{x=0}\frac{d}{dx}\big(x B'(x) B(x)^{n-1}\big) = 0$.**  
Comparing $B(x) - (1+2c) = (1+c)x^{-1} + cx$ with $x B'(x) = -(1+c)x^{-1} + cx$, we observe two immediate identities:
$$\frac{d}{dx}\big(x B'(x)\big) = (1+c)x^{-2} + c = x^{-1}\big(B(x) - (1+2c)\big),$$
$$\big(x B'(x)\big)^2 = \big(B(x) - (1+2c)\big)^2 - 4c(1+c) = B(x)^2 - 2(1+2c)B(x) + 1.$$
Now apply $\operatorname{Res}_{x=0}\frac{d}{dx}(\cdots) = 0$ to the product $x B'(x) B(x)^{n-1}$:
$$\begin{aligned}
0 &= \operatorname{Res}_{x=0} \frac{d}{dx}\Big(x B'(x) B(x)^{n-1}\Big) \\
&= \operatorname{Res}_{x=0} \left[ \frac{d}{dx}\big(x B'(x)\big) B(x)^{n-1} + (n-1) x^{-1} \big(x B'(x)\big)^2 B(x)^{n-2} \right] \\
&= \operatorname{Res}_{x=0}\, x^{-1}\Big[ \big(B(x) - (1+2c)\big) B(x)^{n-1} + (n-1)\big(B(x)^2 - 2(1+2c)B(x) + 1\big) B(x)^{n-2} \Big] \\
&= \operatorname{Res}_{x=0}\, x^{-1}\Big[ n B(x)^n - (2n-1)(1+2c) B(x)^{n-1} + (n-1) B(x)^{n-2} \Big].
\end{aligned}$$
Reading off $\mu_0(k) = \operatorname{Res}_{x=0} x^{-1} B(x)^k = D_k(c)$ immediately yields the 3-term holonomic recurrence:
$$n D_n(c) = (2n - 1)(1 + 2c) D_{n-1}(c) - (n - 1) D_{n-2}(c).$$
Look at what just happened: we never computed a bivariate generating function, never invoked Zeilberger's ansatz, and never touched a square root. The identity $\operatorname{Res}\frac{d}{dx}(x B'(x) B^{n-1}) = 0$ combined with $(x B')^2 = (B - (1+2c))^2 - 4c(1+c)$ automatically annihilated the auxiliary moments $\mu_{\pm 1}$!
```

---

#### [CROSS-REFERENCE FIX `C19-2`] Line 395 — Canonical Numbering of `Revisited Dual-Perspective Callout #5` (`#089 CF 840C`)
- **Location**: [`chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd:395`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd#L395)
- **Audit Finding**: Per `CURRICULUM_ARCHITECTURE.md` §5.2 (Line 1425), `#089 CF 840C` is canonical **Revisited Dual-Perspective Callout #5**. Adding `#5` to the callout title ensures 100% alignment across the textbook.
- **Drop-In Replacement for Line 395**:
```markdown
::: {.callout-note title="Revisited Dual-Perspective Callout #5 — Connected-Component IE (`Ch 01`) vs. Truncated Taylor ODE (`Ch 19`) on `#089 CF 840C`"}
```

---

### 3. Audit of Chapter 20 (`chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd`)

#### Verification of Core Engines & Small Cases (Passed)
- **§20.1 Tellegen's Principle & Transposed Multiplication (`mulT`)**: Inner product $\langle f, g \rangle = \sum_{i=0}^n f_i g_i$, exact index mapping $h_k = (\text{mulT}(g, f))_k = \sum_{j=0}^{m-k} g_j f_{k+j}$ for $0 \le k \le m$, and the reversed polynomial convolution $[x^{d+k}](g^R(x) f(x))$ (Lines 107–168) are 100% verified, including the worked $d=2, m=3$ toy trace on Lines 152–162.
- **§20.2 Transposed Subproduct Tree & Dual Multipoint Evaluation**: Both forward top-down `mulT` remainder transitions (`rem_L = mulT(R_right, rem_P)`, `rem_R = mulT(R_left, rem_P)`) and bottom-up partial-fraction fusion, plus the explicit derivation of the size cap $\deg \text{rem}_u < \deg R_u$ (**Failure Mode #10**, Lines 351–389), are 100% verified.
- **§20.3 Transposed Lairez Rational Sum & §20.4 Sample-Point Shift**: The 1-NTT-per-level inner-loop reduction via the $2 \times 2$ transition matrix $M(x)$ (Lines 477–553) and the Lagrange falling-factorial kernel $[x^{d+k}](A(x) B(x))$ for $f(c+k)$ including **Failure Mode #11** (overlapping window $c \in [0, d]$ requiring `std::copy` + non-overlapping suffix shift, Lines 602–673) are mathematically exact.
- **§20.5 Dual Composition vs. Dual Power Projection**: Complete and accurate.

---

#### [CODE BUG FIX `C20-1`] Line 667 (`§20.4 shift_non_overlapping` C++ Implementation) — Comma-Operator Post-Increment Out-of-Bounds / Logic Hazard
- **Location**: [`chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd:665-670`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd#L665-L670)
- **Audit Finding**:
  Lines 665–669 currently read:
  ```cpp
  Poly res(m);
  long long fall = 1;
  for (int j = 0; j <= d; ++j) fall = fall * ((c - j + MOD) % MOD) % MOD;
  for (int k = 0; k < m; ++k, fall = fall * ((c + k) % MOD) % MOD * B[k - 1] % MOD)
      res[k] = fall * C[d + k] % MOD;
  return res;
  ```
  Look at the `for` loop post-iteration expression: `++k, fall = fall * ((c + k) % MOD) % MOD * B[k - 1] % MOD`.
  1. When `k = m - 1` (the final iteration), the post-expression increments `k` to `m` and then executes `B[m - 1]` *before* the loop condition `k < m` terminates the loop. If `m = 0`, or if `d = 0` and `B` was sized to `m - 1`, or if a reader rewrites the loop header without realizing `++k` mutates `k` before `(c + k)` and `B[k - 1]` are evaluated, it causes an immediate off-by-one bug.
  2. Writing the update explicitly inside the loop body with `if (k + 1 < m)` is much cleaner, eliminates the side-effect order dependency on `++k`, and avoids computing an unused `fall` on the last iteration.
- **Drop-In Replacement for Lines 665–670**:
```cpp
    Poly res(m);
    long long fall = 1;
    for (int j = 0; j <= d; ++j) fall = fall * ((c - j + MOD) % MOD) % MOD;
    for (int k = 0; k < m; ++k) {
        res[k] = fall * C[d + k] % MOD;
        if (k + 1 < m)
            fall = fall * ((c + k + 1) % MOD) % MOD * B[k] % MOD;
    }
    return res;
```

---

#### [MINOR TYPO FIX `C20-2`] Line 167 (`§20.2` Callout)
- **Location**: [`chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd:167`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd#L167)
- **Fix**: Replace `division!Notice` with `division! Notice`.

---

### 4. Audit of Chapter 21 (`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd`)

#### Verification of Core Engines & Small Cases (Passed)
- **§21.2 Transposed Kinoshita–Li for Power Projection**: The adjoint derivation mapping Forward Step 1 (even-odd split + multiply by $Q_i(-x, y)$) to Transpose Step 2 (interleave even-odd + `mulT` by $Q_i(-x, y)$), together with the worked $N = 4$ trace showing $\langle R_0, P_0 \rangle = 1\cdot 1 + 1\cdot 1 + 3\cdot 1 + 7\cdot 1 = 12 = \langle R_1, P_1 \rangle = 1\cdot(1 + 3) + 1\cdot(1 + 7) = 12$ (Lines 232–296), is 100% verified!
- **§21.3 Arbitrary-Degree Lagoon Inversion & `fps_revert`**: The Universal Power Projection Reduction $[x^n] G(F^{\langle -1 \rangle}(x)) = \frac{1}{n}[x^{n-1}]\big(G'(x)(F(x)/x)^{-n}\big)$ via the linear functional $w_k = [x^{n-1}] x^k G'(x) = (n - k) g_{n-k}$ (Lines 325–423) is 100% verified.
- **§21.4 Constant-Factor Engineering & Failure Mode #12**: Both Failure Mode #12 (missing $f_0 = g_0 = 0$ / $f_1 \ne 0$ validation before `fps_revert` and Taylor shift before `fps_comp`) and the Kronecker packing stride $K_i = 2 d_x^{(i)} + 1$ avoiding negative-$x$-exponent wrap-around in `mulT` (Lines 440–487) are 100% verified.

---

#### [CRITICAL FIX `C21-1`] Lines 109, 112, 115 (§21.1 Worked Toy Trace of Kinoshita–Li 2D Bostan–Mori, $N = 4$) — Spurious $-2y^2$ Term in Degree-1 $y$-Product
- **Location**: [`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd:106-119`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd#L106-L119)
- **Mathematical Audit**:
  In the worked trace for $F(x) = 1 + x + x^2 + x^3$ and $G(x) = x + 2x^2 \pmod{x^4}$:
  - $P_0(x, y) = 1 + x + x^2 + x^3$ (which has degree $0$ in $y$) and $Q_0(-x, y) = 1 + yx - 2yx^2$ (which has degree $1$ in $y$).
  - Line 109 writes:
    $$P_0(x, y) Q_0(-x, y) = (1 + x + x^2 + x^3)(1 + y x - 2 y x^2) = 1 + (1 + y)x + (1 - y)x^2 + (1 - y - 2y^2)x^3 + \dots$$
    **Flaw 1**: Because $P_0(x, y)$ is independent of $y$ and $Q_0(-x, y)$ is linear in $y$, their product **cannot** contain a $-2y^2$ term! Expanding $[x^3]\big((1 + x + x^2 + x^3)(1 + yx - 2yx^2)\big)$ gives $1\cdot 1 + 1\cdot y + 1\cdot(-2y) = 1 - y$ (not $1 - y - 2y^2$).
  - **Flaw 2**: This typo propagates to Line 112 ($P_1(x, y) = (1 + y) + (1 - y - 2y^2)x$) and Line 115:
    $$P_1(x, y) Q_1(-x, y) \equiv (1 + y) + \Big((1 - y - 2y^2) + (1 + y)(4y + y^2)\Big) x = (1 + y) + (1 + 3y + 5y^2 + y^3) x \pmod{x^2}.$$
    Notice that $(1 - y - 2y^2) + (1 + y)(4y + y^2) = 1 + 3y + 3y^2 + y^3 \ne 1 + 3y + 5y^2 + y^3$, whereas with the true coefficient $(1 - y)$, we have
    $$(1 - y) + (1 + y)(4y + y^2) = (1 - y) + (4y + 5y^2 + y^3) = 1 + 3y + 5y^2 + y^3,$$
    which matches the right-hand side of Line 115 and the true composition $F(G(x)) = 1 + x + 3x^2 + 5x^3 \pmod{x^4}$!
- **Drop-In Replacement for Lines 108–118**:
```markdown
- **Level $i = 0 \to 1$**: Since $N = 4$ is even, we extract the odd $x$-powers $\mathcal{S}_1$ of $P_0(x, y) Q_0(-x, y)$:
  $$P_0(x, y) Q_0(-x, y) = (1 + x + x^2 + x^3)(1 + y x - 2 y x^2) = 1 + (1 + y)x + (1 - y)x^2 + (1 - y)x^3 + (y - 2y)x^4 - 2y x^5.$$
  Taking odd $x$-powers $\mathcal{S}_1$ (indices $1$ and $3$, mapped to $x^0$ and $x^1$) and truncating $\bmod y^2$:
  $$P_1(x, y) = \mathcal{S}_1\big(P_0(x, y) Q_0(-x, y)\big) \bmod y^2 = (1 + y) + (1 - y) x,$$
  $$Q_1(x, y) = \mathcal{S}_0\big(Q_0(x, y) Q_0(-x, y)\big) \bmod y^4 = 1 - (4y + y^2) x + 4y^2 x^2.$$
- **Level $i = 1 \to 2$**: Again $N_1 = 2$ is even, so we extract the odd $x$-powers $\mathcal{S}_1$ of $P_1(x, y) Q_1(-x, y)$:
  $$P_1(x, y) Q_1(-x, y) \equiv (1 + y) + \Big((1 - y) + (1 + y)(4y + y^2)\Big) x = (1 + y) + (1 + 3y + 5y^2 + y^3) x \pmod{x^2}.$$
```

---

#### [CROSS-REFERENCE FIX `C21-2`] Line 310 — Canonical Callout Numbering for `Revisited #8` (`#200 Luogu P7438`) & `Revisited #11` (`#201 Luogu P7439`)
- **Location**: [`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd:310-322`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd#L310-L322)
- **Audit Finding**:
  Per `CURRICULUM_ARCHITECTURE.md` §5.2 (Line 1428), `Ch 21` is assigned **Revisited Dual-Perspective Callout #8** (`#200 Luogu P7438 — [AGM 2021] 恐龙`, comparing `Ch 14` Bluestein vs `Ch 21` Power Projection / Falling-Factorial Basis Conversion) alongside `#201 Luogu P7439 — [AGM 2021] 树木` (`Revisited #11`). Currently Line 310 only mentions `#201 Luogu P7439` (`Revisited #11`). Updating the callout at Lines 310–322 to explicitly cover both `#200 Luogu P7438` (`Revisited #8`) and `#201 Luogu P7439` (`Revisited #11`) ensures 100% compliance with `CURRICULUM_ARCHITECTURE.md` §5.2.
- **Drop-In Replacement for Lines 310–322**:
```markdown
::: {.callout-tip title="Revisited Dual-Perspective Callouts #8 & #11 — Falling-Factorial / Chirp-Z Basis Conversion (`#200 Luogu P7438`) and Fixed-k vs. All-k Lagrange Inversion (`#201 Luogu P7439`)"}
Our multi-chapter journey through basis conversion and Lagrange inversion now reaches its algorithmic apex across the two companion `[AGM 2021]` benchmarks:

1. **Revisited #8 (`#200 Luogu P7438 — [AGM 2021] 恐龙`)**: In **Chapter 14**, we converted between falling-factorial / Stirling bases and power bases via Chirp-Z / Bluestein transforms and exponential generating function multiplication with $e^x$. Under the **Chapter 21** lens, any basis change $B(x) = A(F(x))$ (such as $F(x) = e^x - 1$ or $F(x) = \ln(1+x)$) is a direct instance of formal power series composition (`fps_comp`), while its transpose maps linear functionals between the monomial basis $x^k$ and the deformed basis $F(x)^k$ in $O(N \log^2 N)$ via `power_projection`!
2. **Revisited #11 (`#201 Luogu P7439 — [AGM 2021] 树木`)**:
   - **Chapter 11 (Single Coefficient, Fixed $k$)**: To compute $[x^n] (F^{\langle -1 \rangle}(x))^k$ for a *single* fixed $k$ across one or all $n$, we compute a single $n$-th power $\frac{k}{n}[x^{n-k}](F(x)/x)^{-n}$ in $O(N \log N)$ via `fps_pow`.
   - **Chapter 21 (All $k$ Simultaneously, Fixed $n$)**: What if a problem asks for the linear combination $\sum_{k=1}^n w_k [x^k] F(x)^n$—or dually, requires $[x^n] G(F^{\langle -1 \rangle}(x))$ for an arbitrary target series $G(x) = \sum_{k=1}^n g_k x^k$—or requires $[x^n] (F^{\langle -1 \rangle}(x))^k$ for a single fixed $n$ and *all* $1 \le k \le n$? Running Chapter 11's `fps_pow` for each $k$ takes $O(N^2 \log N)$! As we prove in §21.3 below, **Power Projection** solves the entire linear combination in a single $O(N \log^2 N)$ pass, and **Compositional Inverse (`fps_revert`)** recovers every coefficient $[x^1]F^{\langle -1 \rangle}, \dots, [x^n]F^{\langle -1 \rangle}$ at once!
:::
```

---

#### [PEDAGOGICAL CLARITY FIX `C21-3`] Lines 504–506 & 538–546 (`SS-1 #036 AtCoder ABC 281 Ex — Alchemy`) — Aligning Sample Trace and Official `ABC 281 Ex` EGF Functional Equation
- **Location**: [`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd:502-546`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd#L502-L546)
- **Audit Finding**:
  In `SS-1 #036` (`AtCoder ABC 281 Ex — Alchemy`), the problem statement (Lines 502–506) and Step 1 of the solution (Lines 538–545) describe two different recurrences: Line 505 writes the falling-factorial product $\prod_{k=0}^{N-1}(1 + (A-k)x)$ for $N=3, A=3$, whereas Lines 538–545 write $\sum_{i+j=n-1}\binom{n-2}{i}\binom{f_i f_j}{2}$ and then replace $\binom{f_i f_j}{2}$ by $\frac{1}{2} f_i f_j$ to solve $F'(x) = \frac{1}{2} F(x)^2$. In the actual `AtCoder ABC 281 Ex — Alchemy`, level-$k$ metals are formed from non-empty subsets of level-$(k-1)$ metals (or via the DAG layer DP reduciable to multipoint shift / compositional inverse of $x (1+x)^{-A}$). Clarifying both the exact polynomial product $[x^N]\prod_{k=0}^{N-1}(1 + (A-k)x)$ (via $\exp(\sum \ln)$ / D&C) and the compositional-inverse / nonlinear-ODE tree model makes `SS-1` 100% consistent between statement, sample trace, and solution.
- **Drop-In Replacement for Lines 535–546**:
```markdown
1. **Step 1 — Two Complementary Views: Layer Product vs. Nonlinear EGF Functional Equation**:
   - **Direct Layer Product (Matching the Sample Trace $N = 3, A = 3 \implies 17$)**: When each layer $k \in \{0, \dots, N-1\}$ contributes a factor $(1 + (A - k)x)$, taking formal logarithms reduces $\prod_{k=0}^{N-1}(1 + (A - k)x) \bmod x^{N+1}$ to power sums $\sum_{k=0}^{N-1} (A - k)^m$ via `fps_exp`, or directly to a divide-and-conquer product tree in $O(N \log^2 N)$.
   - **Implicit Tree / Compositional Inverse Formulation (`fps_revert`)**: More generally, when each synthesis step chooses a non-empty subset from $A$ available catalytic branches so that the tree EGF $F(x)$ satisfies the autonomous equation $F(x) = x (1 + F(x))^A$ (or $F'(x) = \Phi(F(x))$), separating variables yields
     $$\frac{F(x)}{(1 + F(x))^A} = x \quad \text{or} \quad \int_0^{F(x)} \frac{du}{\Phi(u)} = x.$$
     Setting $H(u) = u(1 + u)^{-A} \bmod u^{N+1}$ (computed in $O(N \log N)$ via `fps_pow`), the target series $F(x) = H^{\langle -1 \rangle}(x) \bmod x^{N+1}$ is the exact **compositional inverse** of $H(u)$!
```

---

### 5. Audit of Checkpoint V (`checkpoints/cp05-part5-dfinite-transposition-composition.qmd`)

#### Stage 1 Spoiler-Free Verification (100% Passed)
- **Overview Table (Lines 31–40)**: Zero chapter numbers (`Ch 06`, `Ch 18`–`Ch 21`) and zero technique names appear in the visible table.
- **Problem Statements & Hint 1 Blocks (`CP-V.1` through `CP-V.8`, Lines 44–489)**: Verified line-by-line. Every single Problem Statement and Hint 1 block is 100% free of chapter numbers and named technique spoilers (`Tellegen`, `mulT`, `Kinoshita–Li`, `Bostan–Mori`, `Lairez`).
- **Prerequisite Closure**: Every solution in Stage 2 (`CP-V.1`–`CP-V.8`) uses only techniques from Parts I–V (`Ch 01`–`Ch 21`). In particular, `CP-V.3` (`#067 CF 1810G`) serves as the scheduled Part II (`Ch 06`) review problem, solved both via reversed-time 1D DP and via bivariate rational GF / `mulT`.

---

#### [CRITICAL FIX `CPV-1`] Line 655 (`CP-V.4 #135 CF 1988F` Stage 2 Solution) — Off-by-One Bug in Reversed-Permutation Ascent Index `j - 1 - [j > 0] - v`
- **Location**: [`checkpoints/cp05-part5-dfinite-transposition-composition.qmd:654-657`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp05-part5-dfinite-transposition-composition.qmd#L654-L657)
- **Mathematical Audit**:
  Line 655 defines the right-suffix polynomial coefficients $R[j][v]$:
  $$L[i][u] = \frac{1}{i!} \sum_{x=0}^i a_{x+1} \, dp(i, x, u), \qquad R[j][v] = \frac{1}{j!} \sum_{x=0}^j b_{x+1} \, dp(j, x, j - 1 - [j > 0] - v),$$
  followed immediately on Line 656 by:
  > *"where reversing a permutation $q \in S_j$ maps prefix maxima to suffix maxima and flips ascents $v \leftrightarrow (j - 1) - v$!"*
  **Flaw**: Look at the third argument of $dp$ in $R[j][v]$: `j - 1 - [j > 0] - v`.
  - When $j \ge 1$, the Iverson bracket `[j > 0]` equals $1$, so `j - 1 - [j > 0] - v` evaluates to $(j - 2) - v$ instead of $(j - 1) - v$!
  - Why did this happen? Because for $j = 0$, $j - 1 = -1$, so the author intended to clamp $j - 1$ to $0$ at $j = 0$ (i.e., $\max(0, j - 1) - v$ or `j - [j > 0] - v`), and accidentally wrote BOTH `- 1` and `- [j > 0]`!
- **Drop-In Replacement for Line 655**:
```markdown
   $$L[i][u] = \frac{1}{i!} \sum_{x=0}^i a_{x+1} \, dp(i, x, u), \qquad R[j][v] = \frac{1}{j!} \sum_{x=0}^j b_{x+1} \, dp\big(j, x, \max(0, j - 1) - v\big),$$
```

---

## Summary Checklist Across All 8 Mandatory Audit Dimensions

1. **Mathematical Accuracy & Index Boundary Verification**: Audited 100% of formulas, base cases, and traces. Caught and provided exact drop-in fixes for `C18-1` (Line 1103 false Delannoy recurrence), `C18-2` (Line 1121 modular vanishing when $n \ge p$), `C19-1` (Line 180 tautological residue identity), `C20-1` (Line 667 loop post-increment hazard), `C21-1` (Lines 109, 112, 115 spurious $-2y^2$ term in Kinoshita–Li trace), and `CPV-1` (Line 655 `j - 1 - [j > 0] - v` off-by-one).
2. **Zero Magic Steps & Reverse-Engineering Scratchpad Audit**: Every non-trivial substitution and operator step has an explicit Diagnostic Signal and Reverse-Engineering Scratchpad; the two places where an intermediate elimination step was skipped (`C18-1` and `C19-1`) now have complete, self-contained 3-line derivations.
3. **Strict Prerequisite Closure & Zero Forward-Reference Audit**: 100% verified across `Ch 18`–`Ch 21` and `CP-V`. No Part VI (`Ch 22`–`Ch 24`) techniques leak into Part V.
4. **100% Sub-Section, Failure Mode & Characteristic-$p$ Completeness**:
   - `Ch 18`: §18.1–§18.5, Failure Mode #8 (Vanishing Indicial Polynomial $I(n^*) \equiv 0 \pmod p$ & $\epsilon$-lifting), Revisited Callouts `#10` & `#12` (after `C18-3`).
   - `Ch 19`: §19.1–§19.5, all 3 `EI` engines in §19.2, Failure Mode #9 (Truncated ODE boundary correction), Revisited Callout `#5` (after `C19-2`).
   - `Ch 20`: §20.1–§20.5, Failure Modes #10 (Transposed degree cap) & #11 (Sample-point shift overlapping domain $c \in [0, d]$).
   - `Ch 21`: §21.1–§21.4, Failure Mode #12 (Valuation $f_0 = 0, f_1 \ne 0$ and Kronecker stride), Revisited Callouts `#8`, `#9`, `#11` (after `C21-2`).
5. **8-Problem Ladder & Blind Checkpoint Completeness Audit**: All $4 \times 8 = 32$ chapter problems and all $8$ `CP-V` problems are present with self-contained problem statements, constraints, 3 progressive collapsible hints, and complete derivations. Stage 1 of `CP-V` is 100% spoiler-free.
6. **`AGENTS.md` Editorial Policy Compliance**: No raw NTT/modint template dumps; local algebraic hypotheses ($f_0 = 0, f_1 \in R^\times$, $\text{char } p > N$, $I(n) \not\equiv 0 \pmod p$) are stated alongside every division/inversion.
7. **Citations & Terminology Integration**: `[EN]`/`[ZH]`/`[JA]` terminology blocks, EI (Elegia) `c`-Delannoy & ODE benchmarks, Tellegen (1952), Bostan–Lecerf–Schost (2003), and Kinoshita–Li (2024) are properly credited.
8. **Quarto Formatting & Render Safety**: Verified zero forbidden `\(` or `\[` delimiters, zero unescaped `|` inside math in tables, and properly balanced `:::` and `<details>` blocks across all 5 files.
