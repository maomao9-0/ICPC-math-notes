# Audit Report A: Master Technique Taxonomy & Multilingual Bibliography Synthesis (`TECHNIQUE_TAXONOMY.md` & `CITATIONS.md`)

- **Auditor**: Inspector A-Taxonomy-Citations (Principal Mathematical & Pedagogical Auditor)
- **Target Files Audited**:
  1. [`TECHNIQUE_TAXONOMY.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md) (360 lines, 89,090 bytes)
  2. [`CITATIONS.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md) (286 lines, 90,920 bytes)
- **Source Files Cross-Checked**: All 10 Cohort 3 synthesis wave files (`cohort3_wave_1a_*.md` through `cohort3_wave_5b_*.md`) and all Cohort 1 / Cohort 2 / Pre-existing source files (`iter_*.md`, `cohort2_*.md`) in `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/`.

---

## 1. Executive Summary & Audit Verdict

| Audit Dimension | Target File | Issues Found | Severity Breakdown | Status & Remediation Path |
| :--- | :--- | :---: | :--- | :--- |
| **1. Mathematical & Algorithmic Exactness** | `TECHNIQUE_TAXONOMY.md` & `CITATIONS.md` | **10** (`M-1` to `M-10`) | **5 Critical** (inverted Jacobian factor, sign flip, missing $z^2/y^2$ power in Furstenberg, false Snake Oil identity, wrong Kronecker $\chi$-grading formula)<br>**5 Moderate** (Wright excess vs. cyclomatic index mismatch, MacMahon $\Phi_i$ specialization, $\mathcal{E}_t(x)$ exponent, Goulden–Jackson $t=0$ matrix singularity, draft text artifact) | 100% deterministic line-by-line patches provided in **Section 2**. |
| **2. Taxonomy Completeness (vs. Waves 1A–5B)** | `TECHNIQUE_TAXONOMY.md` | **6** (`T-1` to `T-6`) | **3 Major** (omitted Iteration 49/101 CZT + Shift of Sampling Points + $O(\sqrt{P}\log P)$ Factorial; omitted Regime D Quarter-Plane Obstinate Kernel Method in 4-Regime table; non-canonical iteration numbering in §1.1)<br>**3 Moderate** (missing DAG/Bridge-Tree/Bipartite/Eulerian graph rows in §2.2; missing Roots-of-Unity Filter in §3.2 & Bivariate PDE Matrix Product in §3.5; missing Master Complexity Table & Decision Flowchart) | Drop-in replacement rows and subsections provided in **Section 3**. |
| **3. Citation Completeness & Attribution** | `CITATIONS.md` | **6** (`C-1` to `C-6`) | **1 Major** (author/handle attribution across `Elegia` / 吕欣, `EntropyIncreaser` / `rushcheyo` / 虞皓翔, and `Athekatelan` / 钱易)<br>**5 Moderate** (missing `[EN-Pr-BGS07]` Bostan–Gaudry–Schost 2007, `[EN-CP-CPA]` CP-Algorithms, `[ZH-NT-YJ18]` Yang Jun 2018 Dynamic DP, `[ZH-Bg-War21]` `warzone` Transposition, `[JA-Bg-Ha21]` `hamamu` Qiita & `DEGwer` PDF) | Drop-in bibliography entries provided in **Section 4**. |
| **4. Formatting & Delimiter Compliance** | `TECHNIQUE_TAXONOMY.md` & `CITATIONS.md` | **14 lines** (`F-1`, `F-2`) | **0 Banned Delimiters** (`\(...\)` / `\[...\]` = 0 occurrences)<br>**14 Table Rows** with unescaped `|` inside `$...$` math spans (8 lines in `TECHNIQUE_TAXONOMY.md`, 6 lines in `CITATIONS.md`) | Exact `\lvert ... \rvert` line patches provided in **Section 5**. |

---

## 2. Mathematical & Algorithmic Verification (`TECHNIQUE_TAXONOMY.md` & `CITATIONS.md`)

Every identity, recurrence, Jacobian factor, and residue substitution in both files was verified symbolically and numerically via Python. Below are the **10 mathematical and algorithmic errors** caught during the audit, ordered by severity.

---

### Bug M-1 [CRITICAL]: Inverted Jacobian Factor in `Elegia`'s Coupled Binomial Sum Linearization (`炫酷反演魔术`)
- **Location**: [`TECHNIQUE_TAXONOMY.md` Line 170](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L170) (Section 3.4.A, Row 6)
- **Current Text (Line 170, Column 4)**:
  ```markdown
  By Form 2 or Form 3 of Lagrange Inversion:<br>$$S_n = [z^n] \frac{1 - (\alpha - 1)u(z)}{1 + u(z)} (1 + u(z))^\gamma F\!\left(u(z)(1 + u(z))^\beta\right)!$$
  ```
- **Mathematical Error & Numerical Counterexample**:
  - For $u(z) = z \Phi(u(z))$ with $\Phi(u) = (1 + u)^\alpha$, we want to evaluate:
    $$S_n = \sum_{k=0}^n f_k \binom{\alpha n + \beta k + \gamma}{n - k} = [u^n] (1 + u)^{\alpha n + \gamma} F\!\left(u(1 + u)^\beta\right) = [u^n] H(u) \Phi(u)^n,$$
    where $H(u) := (1 + u)^\gamma F\!\left(u(1 + u)^\beta\right)$.
  - By **Form 3 (Gessel's Diagonal / Jacobian-Denominator Form)** on Line 167:
    $$[u^n] H(u) \Phi(u)^n = [z^n] \frac{H(u(z))}{1 - z \Phi'(u(z))}.$$
  - Since $z = \frac{u}{\Phi(u)} = \frac{u}{(1 + u)^\alpha}$, the denominator on the $z$-side is:
    $$1 - z \Phi'(u) = 1 - \frac{u \Phi'(u)}{\Phi(u)} = 1 - \frac{\alpha u}{1 + u} = \frac{1 - (\alpha - 1)u}{1 + u}.$$
  - Dividing $H(u(z))$ by $1 - z \Phi'(u(z)) = \frac{1 - (\alpha - 1)u(z)}{1 + u(z)}$ puts $1 - (\alpha - 1)u(z)$ in the **denominator** and $1 + u(z)$ in the **numerator**! Line 170 multiplied by $\frac{1 - (\alpha - 1)u(z)}{1 + u(z)}$ instead of dividing by it.
  - **Python Numerical Verification** ($\alpha = 2, \beta = 1, \gamma = 3, f = [1, 2, 3, 5, 7]$):
    - Exact values $S_n = \sum_{k=0}^n f_k \binom{2n + k + 3}{n - k}$ for $n = 0 \dots 4$: **`[1, 7, 40, 212, 1081]`**
    - Line 170 claimed formula: **`[1, 3, 12, 52, 233]`** (FALSE for all $n \ge 1$)
    - Corrected formula $[z^n] \frac{(1 + u(z))^{\gamma + 1}}{1 - (\alpha - 1)u(z)} F\!\left(u(z)(1 + u(z))^\beta\right)$: **`[1, 7, 40, 212, 1081]`** (EXACT MATCH)
- **Exact Fix for `TECHNIQUE_TAXONOMY.md` Line 170**:
  Replace:
  ```markdown
  $$S_n = [z^n] \frac{1 - (\alpha - 1)u(z)}{1 + u(z)} (1 + u(z))^\gamma F\!\left(u(z)(1 + u(z))^\beta\right)!$$
  ```
  with:
  ```markdown
  $$S_n = [z^n] \frac{1 + u(z)}{1 - (\alpha - 1)u(z)} (1 + u(z))^\gamma F\!\left(u(z)(1 + u(z))^\beta\right) = [z^n] \frac{(1 + u(z))^{\gamma + 1}}{1 - (\alpha - 1)u(z)} F\!\left(u(z)(1 + u(z))^\beta\right)!$$
  ```

---

### Bug M-2 [CRITICAL]: Global Sign Flip in Golden Rule Row #7 (`(n - 2k)` vs. `k - (n - k)`)
- **Location**: [`TECHNIQUE_TAXONOMY.md` Line 111](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L111) (Section 3.1.A, Row 7)
- **Current Text (Line 111)**:
  ```markdown
  | **7** | $(n - 2k) = k - (n - k)$ | Asymmetric difference | $1 \cdot k \cdot 1 - 1 \cdot 1 \cdot (n-k)$ | $(\vartheta_x A(x)) B(x) - A(x) (\vartheta_x B(x))$ |
  ```
- **Mathematical Error**:
  - $k - (n - k) = 2k - n = -(n - 2k)$!
  - Since $[x^n]\big((\vartheta_x A(x)) B(x) - A(x) (\vartheta_x B(x))\big) = \sum_{k=0}^n \big(k - (n - k)\big) a_k b_{n-k} = \sum_{k=0}^n (2k - n) a_k b_{n-k}$, the identity $(n - 2k) = k - (n - k)$ has the wrong sign.
  - In fact, $(n - 2k) = (n - k) - k$, which corresponds to $A(x)(\vartheta_x B(x)) - (\vartheta_x A(x))B(x)$.
- **Exact Fix for `TECHNIQUE_TAXONOMY.md` Line 111**:
  ```markdown
  | **7** | $(n - 2k) = (n - k) - k$ | Asymmetric difference | $1 \cdot 1 \cdot (n-k) - 1 \cdot k \cdot 1$ | $A(x) (\vartheta_x B(x)) - (\vartheta_x A(x)) B(x)$ |
  ```

---

### Bug M-3 [CRITICAL]: Missing Power of $z$ / $y$ in Furstenberg Forward Rational Lift
- **Locations**:
  1. [`CITATIONS.md` Line 44](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L44) (Category II, `[EN-Pr-Fu67]`)
  2. [`TECHNIQUE_TAXONOMY.md` Line 224](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L224) (Section 3.5.B, Row 1)
- **Current Text**:
  - `CITATIONS.md` Line 44:
    ```markdown
    every univariate algebraic formal power series $P(t, F(t)) = 0$ over any field $K$ is the diagonal $\operatorname{Diag}_{x,y}\!\left(\frac{y P_y(xy, y)}{P(xy, y)}\right)$ of a bivariate rational function
    ```
  - `TECHNIQUE_TAXONOMY.md` Line 224 (Column 4):
    ```markdown
    $$\boxed{F(t) = \operatorname{Diag}\!\left( \frac{y^2 P_y(x y, y)}{P(x y, y)} \right) = [z^0] \frac{z P_y(t, z)}{P(t, z)}!}$$
    ```
- **Mathematical Error & Numerical Counterexample**:
  - Let $P(t, z) = 0$ with $F(0) = 0$ and $P_z(0, 0) \neq 0$. Around the unique small root $z = F(t)$, the logarithmic derivative has the Laurent expansion in $K((z))[[t]]$:
    $$\frac{P_z(t, z)}{P(t, z)} = \frac{1}{z - F(t)} + \text{holomorphic}(z) = \frac{1}{z} + \frac{F(t)}{z^2} + \frac{F(t)^2}{z^3} + \dots + \text{holomorphic}(z).$$
  - Multiplying by $z$ gives $\frac{z P_z(t, z)}{P(t, z)} = 1 + \frac{F(t)}{z} + \dots$, so its **residue** $[z^{-1}]$ is $F(t)$, whereas its **constant term** $[z^0]$ is $1$!
  - Multiplying by $z^2$ shifts $[z^{-1}]$ to $[z^0]$:
    $$F(t) = [z^{-1}] \frac{z P_z(t, z)}{P(t, z)} = [z^0] \frac{z^2 P_z(t, z)}{P(t, z)} = \operatorname{Diag}_{x, y}\!\left(\frac{y^2 P_y(x y, y)}{P(x y, y)}\right) \quad (\text{setting } t = xy, z = y).$$
  - **Python Verification** ($P(x, y) = y - x(1+y)^2 = 0$, Catalan series $F(t) = t + 2t^2 + 5t^3 + 14t^4 + \dots$):
    - $[x^n y^n] \frac{y^2 P_y(xy, y)}{P(xy, y)} = [z^0] \frac{z^2 P_y(t, z)}{P(t, z)}$ for $n = 1 \dots 4$: **`[1, 2, 5, 14]`** $= F_n$.
    - $[x^n y^n] \frac{y P_y(xy, y)}{P(xy, y)} = [z^0] \frac{z P_y(t, z)}{P(t, z)}$ for $n = 1 \dots 4$: **`[0, 0, 0, 0]`** (and $1$ at $n = 0$).
- **Exact Fixes**:
  1. In **`CITATIONS.md` Line 44**, replace `\frac{y P_y(xy, y)}{P(xy, y)}` with `\frac{y^2 P_y(xy, y)}{P(xy, y)}`.
  2. In **`TECHNIQUE_TAXONOMY.md` Line 224**, replace `[z^0] \frac{z P_y(t, z)}{P(t, z)}` with `[z^0] \frac{z^2 P_y(t, z)}{P(t, z)} = [z^{-1}] \frac{z P_y(t, z)}{P(t, z)}` (and replace `|y| = \varepsilon` in Column 3 with `\lvert y \rvert = \varepsilon`).

---

### Bug M-4 [CRITICAL]: False Identity in `CITATIONS.md` Rosetta Stone Entry #19 (The Snake Oil Method)
- **Location**: [`CITATIONS.md` Line 208](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L208) (Section 3.2, Entry #19)
- **Current Text (Line 208)**:
  ```markdown
  | **19** | **The Snake Oil Method** | 蛇油法 (交换求和次序提取系数) | Snake Oil 法 (和の順序交換) | $\sum_k \binom{n}{k} f(k) = [x^n] \sum_k f(k) x^k (1+x)^{n-k}$ |
  ```
- **Mathematical Error**:
  1. $[x^n] x^k (1+x)^{n-k} = [x^{n-k}](1+x)^{n-k} = 1$ (not $\binom{n}{k}$!), so the right-hand side evaluates to $\sum_{k=0}^n f(k) \neq \sum_{k=0}^n \binom{n}{k} f(k)$.
  2. Furthermore, the defining property of Wilf's Snake Oil Method is summing over the external variable $n$ first so that $n$ is eliminated from the inner sum: for $S_n = \sum_k \binom{a+bk}{n-ck} f_k$, $\sum_{n \ge 0} S_n x^n = \sum_k f_k x^{ck} (1+x)^{a+bk}$.
- **Exact Fix for `CITATIONS.md` Line 208**:
  ```markdown
  | **19** | **The Snake Oil Method** | 蛇油法 (交换求和次序提取系数) | Snake Oil 法 (和の順序交換) | $\sum_k \binom{a+bk}{n-ck} f_k = [x^n] \sum_{k \ge 0} f_k x^{ck} (1+x)^{a+bk}$ |
  ```

---

### Bug M-5 [CRITICAL]: Incorrect $\chi$-Grading Formula in `CITATIONS.md` Rosetta Stone Entry #51 (Twisted Kronecker Substitution)
- **Location**: [`CITATIONS.md` Line 254](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L254) (Section 3.4, Entry #51)
- **Current Text (Line 254)**:
  ```markdown
  | **51** | **Twisted / $\chi$-Graded Kronecker Substitution** | 循环梯度 Kronecker 代入 (多元截断幂级数乘法) | 次数制限付き多変数多項式の Kronecker 置換 | Track $\chi(I) = \bigl(\sum_j i_j\bigr) \bmod (d + 1)$ to eliminate wrap-around carries |
  ```
- **Mathematical Error**:
  - In mixed-radix Kronecker packing $I = i_1 + n_1 i_2 + \dots + N_{d-1} i_d$ (where $N_r = n_1 \cdots n_r$), when $J + K = I$ has a carry $c_r \in \{0, 1\}$ across radix boundary $r \in \{1, \dots, d-1\}$, the coordinate digits satisfy $j_r + k_r = i_r + n_r c_r - c_{r-1}$, so $\sum_r (j_r + k_r - i_r) = \sum_{r=1}^{d-1} (n_r - 1) c_r$, which depends on $n_r$ and vanishes whenever $n_r \equiv 1 \pmod{d+1}$!
  - Instead, as proved in [`cohort3_wave_4a_multivariate_bostan_mori_diag.md` §3.4](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4a_multivariate_bostan_mori_diag.md#L319-L382) and [`TECHNIQUE_TAXONOMY.md` Line 81](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L81), the carry detector sums the **mixed-radix quotients** $\lfloor I / N_r \rfloor$ (since $\lfloor J/N_r \rfloor + \lfloor K/N_r \rfloor = \lfloor I/N_r \rfloor - c_r$) modulo $d$:
    $$\chi(I) = \left(\sum_{r=1}^{d-1} \left\lfloor \frac{I}{N_r} \right\rfloor\right) \bmod d \in \mathbb{Z}/d\mathbb{Z}.$$
- **Exact Fix for `CITATIONS.md` Line 254**:
  ```markdown
  | **51** | **Twisted / $\chi$-Graded Kronecker Substitution** | 循环梯度 Kronecker 代入 (多元截断幂级数乘法) | 次数制限付き多変数多項式の Kronecker 置換 | Track $\chi(I) = \bigl(\sum_{r=1}^{d-1} \lfloor I / N_r \rfloor\bigr) \bmod d$ to eliminate wrap-around carries |
  ```

---

### Bug M-6 [MODERATE]: Wright's $k$-Excess Connected Graphs — Cyclomatic Number vs. Excess Indexing Mismatch
- **Location**: [`TECHNIQUE_TAXONOMY.md` Line 71](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L71) (Section 2.2, Row 13)
- **Current Text (Line 71)**:
  ```markdown
  | **Wright's $k$-Excess Connected Graphs** | $C_k(x)$ ($V$ vertices, $V+k-1$ edges) | $C_0(x) = T(x) - \frac{1}{2}T(x)^2, \quad C_1(x) = \frac{1}{2}\ln\frac{1}{1-T(x)} - \frac{T(x)}{2} - \frac{T(x)^2}{4}$<br>$C_k(x) = \frac{W_k(T(x))}{(1 - T(x))^{3k}} \quad (k \ge 2)$ | Smooths degree-$1$ vertices (trees attached to the 2-core) by substituting $T(x)$ into the finite rational kernel $W_k(T)/(1-T)^{3k}$ ($\deg W_k \le 3k$). |
  ```
- **Mathematical Error**:
  - Column 2 defines $C_k(x)$ by **cyclomatic number** ($V$ vertices, $V + k - 1$ edges: $k = 0$ trees, $k = 1$ unicyclic, $k \ge 2$ bicyclic and higher), whereas Column 3 writes the denominator $(1 - T(x))^{3k}$, which is Wright's formula for **excess** $k = \lvert E \rvert - \lvert V \rvert \ge 1$ ($V + k$ edges, as in `CITATIONS.md` Lines 48 & 244 and `cohort3_wave_3a` Iter 25/77)!
  - Specifically, for bicyclic graphs ($\lvert E \rvert = \lvert V \rvert + 1$, excess $1$, cyclomatic number $2$), the denominator is $(1 - T(x))^3$, whereas Line 71 gives $(1 - T(x))^6$.
- **Exact Fix for `TECHNIQUE_TAXONOMY.md` Line 71** (aligning with Wright 1977, `cohort3_wave_3a`, and `CITATIONS.md` Lines 48 & 244 by using excess $k = \lvert E \rvert - \lvert V \rvert \ge -1$):
  ```markdown
  | **Wright's $k$-Excess Connected Graphs** | $C_k(x)$ ($V$ vertices, $V+k$ edges; excess $k = \lvert E \rvert - \lvert V \rvert$) | $C_{-1}(x) = T(x) - \frac{1}{2}T(x)^2, \quad C_0(x) = \frac{1}{2}\ln\frac{1}{1-T(x)} - \frac{T(x)}{2} - \frac{T(x)^2}{4}$<br>$C_k(x) = \frac{W_k(T(x))}{(1 - T(x))^{3k}} \quad (k \ge 1)$ | Smooths degree-$1$ vertices (trees attached to the 2-core) and degree-$2$ chains by substituting $T(x)$ into the rational kernel $W_k(T)/(1-T)^{3k}$ ($k = \lvert E \rvert - \lvert V \rvert \ge 1$). |
  ```

---

### Bug M-7 [MODERATE]: Incorrect $\Phi_i(\mathbf{u})$ Specialization in MacMahon's Master Theorem & Truncated Bipartite Good–Lagrange Formula
- **Locations**:
  1. [`TECHNIQUE_TAXONOMY.md` Line 227](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L227) (Section 3.5.B, Row 4)
  2. [`CITATIONS.md` Line 46](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L46) (Category II, `[EN-Pr-Go60]`)
- **Mathematical Errors**:
  1. **`TECHNIQUE_TAXONOMY.md` Line 227**:
     - Writes `• **MacMahon's Master Theorem** (setting $\Phi_i(\mathbf{u}) = \exp(\sum_j a_{ij} u_j)$ and using LIF):`. Setting $\Phi_i(\mathbf{u}) = \exp(\sum_j a_{ij} u_j)$ yields $\prod_{i=1}^d \Phi_i(\mathbf{u})^{m_i} = \exp(\sum_{i,j} m_i a_{ij} u_j)$, NOT $\prod_{i=1}^d (\sum_j a_{ij} u_j)^{m_i}$! As proved in [`cohort3_wave_4b` Lines 785–797](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4b_furstenberg_kernel_good_lagrange.md#L785-L797), MacMahon's Master Theorem is obtained from Good–Lagrange Form 2 by setting the shifted affine linear forms $\Phi_i(\mathbf{u}) = 1 + \sum_{j=1}^d a_{i,j} u_j$ and using homogeneity of $\sum_{j=1}^d a_{i,j} u_j$.
     - Also on Line 227, the **Bipartite Shortcut** ends with an unexpanded placeholder `(a rank-1 perturbation, giving $1 - \frac{(n_1 k_2)(n_2 k_1)}{\dots}$!)` instead of the exact formula from `cohort3_wave_4b` Line 754: $[x_1^{n_1} x_2^{n_2}](u_1^a u_2^b) = \frac{a n_2 + b n_1 - a b}{n_1 n_2} ([u_1^{n_1-a}]\Phi_2(u_1)^{n_2})([u_2^{n_2-b}]\Phi_1(u_2)^{n_1})$.
  2. **`CITATIONS.md` Line 46 (`[EN-Pr-Go60]`)**:
     - Writes `by specializing $\Phi_i(\mathbf{u}) = (\sum_j A_{i,j} u_j)^{n_i}$.` Since Good–Lagrange already contains $\prod_{i=1}^d \Phi_i(\mathbf{u})^{n_i}$, $\Phi_i(\mathbf{u})$ is specialized to the affine linear form $1 + \sum_j A_{i,j} u_j$ (not raised to $n_i$ a second time).
- **Exact Fixes**:
  1. In **`TECHNIQUE_TAXONOMY.md` Line 227**, replace the last two bullets in Column 4 with:
     ```markdown
     • **Bipartite Shortcut ($d=2$, $u_1 = x_1 \Phi_1(u_2), u_2 = x_2 \Phi_2(u_1)$)**: $\det(I - J) = 1 - \frac{u_1 \Phi_2'(u_1)}{\Phi_2(u_1)} \frac{u_2 \Phi_1'(u_2)}{\Phi_1(u_2)}$, which separates variables completely:<br>$$[x_1^{n_1} x_2^{n_2}](u_1^a u_2^b) = \frac{a n_2 + b n_1 - a b}{n_1 n_2} \left([u_1^{n_1-a}] \Phi_2(u_1)^{n_2}\right) \left([u_2^{n_2-b}] \Phi_1(u_2)^{n_1}\right)!$$<br>• **MacMahon's Master Theorem** (setting $\Phi_i(\mathbf{u}) = 1 + \sum_{j=1}^d a_{i,j} u_j$ in Form 2 with $H(\mathbf{u}) = 1$ and using homogeneity):<br>$$\boxed{[u_1^{m_1} \cdots u_d^{m_d}] \prod_{i=1}^d \left(\sum_{j=1}^d a_{i, j} u_j\right)^{m_i} = [x_1^{m_1} \cdots x_d^{m_d}] \frac{1}{\det(I - X A)}, \quad X = \operatorname{diag}(x_1, \dots, x_d)!}$$
     ```
  2. In **`CITATIONS.md` Line 46**, replace `by specializing $\Phi_i(\mathbf{u}) = (\sum_j A_{i,j} u_j)^{n_i}$.` with `by specializing $\Phi_i(\mathbf{u}) = 1 + \sum_j A_{i,j} u_j$ and using homogeneity of the linear forms.`

---

### Bug M-8 [MODERATE]: Generalized Exponential Series $\mathcal{E}_t(x)$ Exponent Typo in `CITATIONS.md`
- **Location**: [`CITATIONS.md` Line 240](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L240) (Section 3.3, Entry #44)
- **Current Text (Line 240, Column 5)**:
  ```markdown
  $T(x) = x e^{T(x)} = \sum_{n \ge 1} n^{n-1} \frac{x^n}{n!}, \; \mathcal{E}_t(x) = e^{tx\mathcal{E}_t(x)}$
  ```
- **Mathematical Error**:
  - In Graham–Knuth–Patashnik (*Concrete Mathematics*, §7.5, Eq. 7.60) and [`TECHNIQUE_TAXONOMY.md` Line 179](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L179), the Generalized Exponential Series is defined by $\mathcal{E}_t(x) = e^{x \mathcal{E}_t(x)^t} = \sum_{n \ge 0} \frac{(tn+1)^{n-1}}{n!} x^n$ (where $t$ is an exponent on $\mathcal{E}_t(x)$, not a linear multiplier on $x$).
- **Exact Fix for `CITATIONS.md` Line 240**:
  Replace `\mathcal{E}_t(x) = e^{tx\mathcal{E}_t(x)}` with `\mathcal{E}_t(x) = e^{x\mathcal{E}_t(x)^t}`.

---

### Bug M-9 [MODERATE]: Goulden–Jackson Cluster Method Regime 2 Singularity at $t=0$ & Missing 4th Regime
- **Location**: [`TECHNIQUE_TAXONOMY.md` Line 152](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L152) (Section 3.3, Row 5)
- **Current Text (Line 152, Column 4)**:
  ```markdown
  • **Regime 1 (Single Pattern $w$)**: $F(x) = \frac{C(x)}{(1 - \alpha x)C(x) + x^{|w|}}$.<br>• **Regime 2 (Multi-Pattern $m \times m$)**: Solve $(I + \frac{1}{t-1} C(x)) \mathbf{r}(x) = -(t-1)\mathbf{x}^{|\mathbf{w}|}$, then $F(x, t) = \frac{1}{1 - \alpha x - \mathbf{1}^T \mathbf{r}(x)}$ ($t=0$ for avoidance).<br>• **Regime 3 (Cyclic Strings / Necklaces)**: If bad words have length $\le L$, the cluster transfer matrix $T$ gives $\sum_{n \ge 1} \operatorname{tr}(T^n) x^n = \frac{-x Q'(x)}{Q(x)}$ where $Q(x) = \det(I - x T)$!
  ```
- **Mathematical & Structural Error**:
  1. In Column 3 of Line 152, $C_{i,j}(x)$ is defined to **include** the $k = \lvert w_i \rvert$ trivial overlap $x^0 = 1$ on the diagonal: *"Note $C_{i,i}(x)$ always starts with $1 = x^0$ ($k = \lvert w_i \rvert$)."*
  2. Therefore, $C(x) = I + \widetilde{C}(x)$ where $\widetilde{C}(0) = 0$. If we plug $t = 0$ into Column 4's formula $I + \frac{1}{t-1} C(x)$, we get $I - C(x) = -\widetilde{C}(x)$, which has **zero constant term** at $x = 0$ and is non-invertible!
  3. Specifically:
     - For **Multi-Pattern Avoidance ($t = 0$)**: the cluster generator solves $C(x) \mathbf{r}(x) = -\mathbf{w}(x)$ where $\mathbf{w}(x) = (x^{\lvert w_1 \rvert}, \dots, x^{\lvert w_m \rvert})^T$, giving $F(x) = \frac{1}{1 - \alpha x + \mathbf{1}^T C(x)^{-1} \mathbf{w}(x)}$ (matching `CITATIONS.md` Line 60 & Line 217 and `cohort3_wave_2b` Line 427).
     - For **Bivariate Exact-Occurrence Marking ($t$ marks occurrences, weight $v = t - 1$)**: only **proper** overlaps $\widetilde{C}(x) = C(x) - I$ propagate between distinct marked words in a cluster, so the cluster matrix is $I - (t - 1)\widetilde{C}(x) = t I - (t - 1)C(x)$ (which reduces cleanly to $C(x)$ at $t = 0$!), giving $F(x, t) = \frac{1}{1 - \alpha x - (t - 1)\mathbf{1}^T \big(t I - (t - 1)C(x)\big)^{-1} \mathbf{w}(x)}$.
  4. Separating **Regime 2 (Multi-Pattern Avoidance $t=0$)** and **Regime 3 (Bivariate Occurrence Marking $F(x, t)$)** (with **Regime 4: Cyclic Strings / Necklaces**) also restores all **4 Regimes** promised in the title **`5. Goulden–Jackson Cluster Method (4 Regimes)`** (and listed in Section 1.1 Line 20)!
- **Exact Fix for `TECHNIQUE_TAXONOMY.md` Line 152**:
  ```markdown
  | **5. Goulden–Jackson Cluster Method (4 Regimes)** | Strings over alphabet $\Sigma$ ($\lvert \Sigma \rvert = \alpha$) avoiding (or weighting by $t$) occurrences of reduced pattern set $\mathcal{P} = \{w_1, \dots, w_m\}$. | Overlapping bad words form **clusters**. For $w_i, w_j \in \mathcal{P}$, define the **overlap polynomial** (correlation polynomial):<br>$$C_{i, j}(x) = \sum_{\substack{1 \le k \le \lvert w_i \rvert \\ w_i[\lvert w_i \rvert-k+1 \dots \lvert w_i \rvert] = w_j[1 \dots k]}} x^{\lvert w_j \rvert - k}.$$<br>Note $C(x) = I + \widetilde{C}(x)$ always starts with $I$ ($k = \lvert w_i \rvert$). Let $\mathbf{w}(x) = (x^{\lvert w_1 \rvert}, \dots, x^{\lvert w_m \rvert})^T$. | • **Regime 1 (Single Pattern $w$)**: $F(x) = \frac{C(x)}{(1 - \alpha x)C(x) + x^{\lvert w \rvert}}$.<br>• **Regime 2 (Multi-Pattern Avoidance, $m \times m$)**: Solve $C(x)\mathbf{r}(x) = -\mathbf{w}(x)$, then $F(x) = \frac{1}{1 - \alpha x - \mathbf{1}^T \mathbf{r}(x)} = \frac{1}{1 - \alpha x + \mathbf{1}^T C(x)^{-1} \mathbf{w}(x)}$.<br>• **Regime 3 (Bivariate Marking by $t$)**: Replace $C(x)$ by $\frac{1}{t-1}\big((t-1)C(x) - t I\big) = \widetilde{C}(x) - \frac{1}{t-1}I$, giving $F(x, t) = \frac{1}{1 - \alpha x - (t-1)\mathbf{1}^T \big(t I - (t-1)C(x)\big)^{-1} \mathbf{w}(x)}$.<br>• **Regime 4 (Cyclic Strings / Necklaces)**: If bad words have length $\le L$, the cluster transfer matrix $T$ gives $\sum_{n \ge 1} \operatorname{tr}(T^n) x^n = \frac{-x Q'(x)}{Q(x)}$ where $Q(x) = \det(I - x T)$! |
  ```

---

### Bug M-10 [MINOR]: Unedited Conversational Draft Artifact in `TECHNIQUE_TAXONOMY.md` Line 186
- **Location**: [`TECHNIQUE_TAXONOMY.md` Line 186](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L186) (Section 3.4.B, Item 2)
- **Current Text (Line 186)**:
  ```markdown
  Notice that $\frac{G'(u)}{1 - G(u)} = -\frac{d}{du} \ln(1 - G(u))$ is independent of $n$? Even better, for the standard case where $F(x)$ is the compositional inverse, if we want $A_k = \sum_{n=1}^{N} c_n [x^k] F(x)^n$, or if we change variables in $[x^{M-1}]\frac{F(x)^n}{1-x}$: let $R(u) = \left(\frac{u}{G(u)}\right)^M \frac{G'(u)}{1 - G(u)} \bmod u^M$. Then:
  ```
- **Exact Fix for `TECHNIQUE_TAXONOMY.md` Line 186**:
  ```markdown
  Factoring $G(u)^{-M} = u^{-M} \left(\frac{u}{G(u)}\right)^M$ and defining the $n$-independent series $R(u) = \left(\frac{u}{G(u)}\right)^M \frac{G'(u)}{1 - G(u)} \bmod u^M$ (where $\frac{u}{G(u)}$ has constant term $[x^1]F(x) \neq 0$) immediately yields:
  ```

---

## 3. Taxonomy Completeness Audit (`TECHNIQUE_TAXONOMY.md` vs. All 10 Cohort 3 Waves)

Cross-checking `TECHNIQUE_TAXONOMY.md` against all 10 `cohort3_wave_*.md` files and `PLAN.md` revealed **6 structural / coverage gaps** (`T-1` through `T-6`). Below are the exact drop-in fixes for each gap.

---

### Gap T-1 [MAJOR]: Non-Canonical Iteration Numbering & Merged Wave 3A/3B Row in Section 1.1 Table
- **Location**: [`TECHNIQUE_TAXONOMY.md` Lines 17–25](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L17-L25)
- **Issue**:
  1. Column 2 (`Iterations Covered`) uses ad-hoc numbers (`Iters 1–6 / 53 / 63–68`, `Iters 7–12 / 54 / 69–74`, etc.) that contradict the canonical 52-iteration C1 (`01–52`) / C2 (`53–104`) numbering used across `PLAN.md`, `CITATIONS.md` Section 2 (Lines 120–171), and all 10 `cohort3_wave_*.md` titles! Also Line 4 of the header says `Cohort 1 (Iterations 53–62), Cohort 2 (Iterations 63–104)` instead of `Cohort 1 (Iterations 01–52), Cohort 2 (Iterations 53–104)`.
  2. Wave 3A (`Iters 21–25 / 73–77`) and Wave 3B (`Iters 26–30 / 78–82`) are merged into a single row on Line 21, whereas all other 8 waves have their own row.
- **Exact Fix**:
  - On **Line 4**, replace `**Cohort 1** (Iterations 53–62), **Cohort 2** (Iterations 63–104)` with `**Cohort 1** (Iterations 01–52), **Cohort 2** (Iterations 53–104)`.
  - In **Lines 17–25**, update Column 2 (`Iterations Covered`) to the canonical C1 / C2 numbers and split Wave 3A and Wave 3B:
    - **Wave 1A**: `Iters 01–05 / 53–57`
    - **Wave 1B**: `Iters 06–10 / 58–62`
    - **Wave 2A**: `Iters 11–15 / 63–67`
    - **Wave 2B**: `Iters 16–20 / 68–72`
    - **Wave 3A** (`Lagrange Inversion, Trees & Graphs`): `Iters 21–25 / 73–77`
    - **Wave 3B** (`Implicit FPS, Cacti & Char-p LIF`): `Iters 26–30 / 78–82`
    - **Wave 4A**: `Iters 31–35 / 83–87`
    - **Wave 4B**: `Iters 36–40 / 88–92`
    - **Wave 5A**: `Iters 41–45 / 93–97`
    - **Wave 5B**: `Iters 46–52 / 98–104`

---

### Gap T-2 [MAJOR]: Missing Regime D (Quarter-Plane Walks & Obstinate Kernel Method) in Section 3.5.B Row 3
- **Location**: [`TECHNIQUE_TAXONOMY.md` Line 226](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L226) (Section 3.5.B, Row 3: `3. Kernel Method (4 Regimes)`)
- **Issue**:
  - Column 1 explicitly titles the row **`3. Kernel Method (4 Regimes)`**, but Column 4 only lists **3 regimes** (`Regime A`, `Regime B`, `Regime C`), completely omitting **Regime D: 2D Quarter-Plane Lattice Walks ($i, j \ge 0$) & The Obstinate Kernel Method (Bousquet-Mélou & Mishna 2010)** from [`cohort3_wave_4b_furstenberg_kernel_good_lagrange.md` §4.3–4.4](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4b_furstenberg_kernel_good_lagrange.md#L596-L675)!
- **Exact Fix for `TECHNIQUE_TAXONOMY.md` Line 226**:
  Append the 4th bullet to Column 4 of Line 226:
  ```markdown
  <br>• **Regime D (2D Quarter-Plane Walks $i, j \ge 0$ & Obstinate Kernel Method)**: For $K(x, y) F(x, y) = 1 - x y - R(x, y) F(x, 0) - S(x, y) F(0, y) + \dots$ with steps in $\{-1, 0, +1\}^2$, generate the **dihedral group of Vieta birational involutions** $G = \langle \Phi, \Psi \rangle$ fixing $K(x, y) = 0$: $\Phi(x, y) = \left(\frac{c_0(y)}{c_2(y) x}, y\right)$, $\Psi(x, y) = \left(x, \frac{d_0(x)}{d_2(x) y}\right)$. When $\lvert G \rvert = 2m < \infty$ (e.g. $\lvert G \rvert = 4$ symmetric or $\lvert G \rvert = 6$ Kreweras/Tandem), take the **alternating orbit sum** $\sum_{g \in G} \operatorname{sgn}(g) g(x y) = K(x, y) \Delta(x, y)$ so all boundary terms telescope, and extract the positive quadrant $[x^{>0} y^{>0}]$!
  ```

---

### Gap T-3 [MAJOR]: Omitted Iteration 49 / 101 (Chirp Z-Transform, Shift of Sampling Points & $O(\sqrt{P}\log P)$ Subquadratic Factorial) in Section 3.7
- **Location**: [`TECHNIQUE_TAXONOMY.md` Line 325](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L325) (End of Section 3.7)
- **Issue**:
  - In [`cohort3_wave_5b_tree_fps_transposition_compose_q.md` Section 5 (Lines 616–696)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md#L616-L696), **Iteration 49 / 101** is dedicated to **Chirp Z-Transform (CZT / Bluestein's Algorithm)**, **Shift of Sampling Points (`连续点值平移`)**, and **Subquadratic Factorial $N! \bmod P$ in $O(\sqrt{P} \log P)$**.
  - Section 3.7 of `TECHNIQUE_TAXONOMY.md` covers Iterations 45/97 (3.7.A), 46/98 (3.7.B), and 47–48/99–100 (3.7.C), and then jumps directly to Section 3.8 (Iterations 50–51/102–103), completely omitting Iteration 49/101!
- **Exact Drop-In Addition (Insert as Subsection `3.7.D` right after Line 324 of `TECHNIQUE_TAXONOMY.md`)**:
  ```markdown
  ---

  #### D. Chirp Z-Transform (Bluestein's Algorithm), Shift of Sampling Points (`连续点值平移`) & $O(\sqrt{P}\log P)$ Factorial

  | Technique | Diagnostic Signal | Reverse-Engineering Scratchpad | Master Identity & Complexity |
  | :--- | :--- | :--- | :--- |
  | **1. Bluestein's Chirp Z-Transform (CZT)** | Evaluate $F(x) = \sum_{j=0}^{n-1} f_j x^j$ on a **geometric progression** $x_i = a \cdot c^i$ for $i = 0, \dots, m-1$ (or compute an arbitrary-length-$K$ DFT). | Substitute $x_i = a c^i$: $F(a c^i) = \sum_{j=0}^{n-1} (f_j a^j) c^{i j}$. To turn $c^{i j}$ into a convolution in $i + j$, **never** use $ij = \frac{1}{2}((i+j)^2 - i^2 - j^2)$ (which requires $\sqrt{c} \in \mathbb{F}_p$)! Use **Bluestein's Binomial Identity**:<br>$$i j = \binom{i + j}{2} - \binom{i}{2} - \binom{j}{2}!$$ | $$F(a c^i) = c^{-\binom{i}{2}} \sum_{j=0}^{n-1} \left(f_j a^j c^{-\binom{j}{2}}\right) c^{\binom{i + j}{2}}$$<br>A single **Middle Product (`mulT`) / reversed NTT** of length $n + m - 1$ in **$O((n + m)\log(n + m))$**!<br>• **Edge Case**: If $c = 0$, $F(a c^0) = F(a)$ and $F(0) = f_0$ for $i \ge 1$. |
  | **2. Shift of Sampling Points (`连续点值平移`)** | Given point values $F(0), F(1), \dots, F(d)$ of a degree-$d$ polynomial $F(x)$, compute $F(c), F(c+1), \dots, F(c+m-1)$. | By Lagrange interpolation on $\{0, 1, \dots, d\}$:<br>$$F(c + k) = \sum_{i=0}^{d} F(i) \frac{(-1)^{d-i}}{i!(d-i)!} \prod_{j=0}^{d} (c + k - j) \cdot \frac{1}{c + k - i}.$$<br>Factor out the falling factorial window $\Pi(c+k) = \prod_{j=0}^d (c + k - j)$! | Let $a_i = \frac{(-1)^{d-i} F(i)}{i!(d-i)!}$ and $b_t = \frac{1}{c + t - d}$ ($0 \le t < d + m$). Then:<br>$$F(c + k) = \left(\prod_{j=0}^{d} (c + k - j)\right) \cdot [x^{d + k}]\big(A(x) B(x)\big)$$ in **$O((d + m)\log(d + m))$** via **1 NTT** + Montgomery batch inversion! |
  | **3. Subquadratic Factorial $N! \bmod P$ in $O(\sqrt{P}\log P)$** | Compute $N! \bmod P$ for huge prime $P \le 10^9 + 7$ (or $10^{12}$). | Set block size $B = 2^k \approx \sqrt{N}$ and define the block rising-factorial polynomial $G_d(x) = \prod_{j=1}^{d} (x + j)$ of degree $d$. Notice $G_{2d}(x) = G_d(x) \cdot G_d(x + d)$! | At each doubling step $d \to 2d$, use **Shift of Sampling Points** on $G_d(0), G_d(B), \dots, G_d(d B)$ to evaluate at shifted points $+d$ and $+dB$, doubling the degree in $O(d \log d)$! Total time: **$\sum_{s=0}^{\log_2 B} O(2^s \log 2^s) = O(\sqrt{N} \log N)$**! |
  ```

---

### Gap T-4 [MODERATE]: Missing Graph Enumeration Rows in Section 2.2 (DAGs, Strongly Connected Digraphs, 2-Edge-Connected Graphs, Bipartite Graphs, Eulerian Graphs)
- **Location**: [`TECHNIQUE_TAXONOMY.md` Line 73](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L73) (End of Section 2.2 Table)
- **Issue**:
  - In [`cohort3_wave_3a_lagrange_residues_trees_graphs.md` (Iter 25 / 77)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3a_lagrange_residues_trees_graphs.md) and [`cohort3_wave_4b` (§6.3 & Problem 20)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4b_furstenberg_kernel_good_lagrange.md#L920-L943), four major labeled graph enumeration families are derived in full and indexed in `CITATIONS.md` (Lines 144, 243), but are missing from the Section 2.2 Operator Table in `TECHNIQUE_TAXONOMY.md`:
    1. **2-Edge-Connected Graphs & Bridge-Tree Inversion (`Luogu P5828`)**
    2. **Labeled DAGs & Strongly Connected Digraphs (`Luogu P6295`)**
    3. **Labeled Bipartite & 2-Colored Graphs (`Luogu P7364`)**
    4. **Labeled Eulerian Graphs**
- **Exact Drop-In Rows (Append after Line 72 of `TECHNIQUE_TAXONOMY.md`)**:
  ```markdown
  | **2-Edge-Connected Graphs & Bridge-Trees** | $\widehat{B}(u)$ (2-edge-conn.), $\widehat{R}(x)$ (rooted conn.) | $\widehat{R}(x) = \widehat{B}_\bullet\!\left(x e^{\widehat{R}(x)}\right)$<br>$n! [u^n] \widehat{B}(u) = (n - 1)! [x^n] \widehat{R}(x)\big(1 + x \widehat{R}'(x)\big) e^{-n \widehat{R}(x)}$ | Shrinking bridges in a rooted connected graph $\widehat{R}(x)$ yields a rooted 2-edge-connected core $\widehat{B}_\bullet(u)$ with $u = x e^{\widehat{R}(x)}$. Extracted via Derivative-Free LIF in $O(n \log n)$ (`Luogu P5828`). |
  | **Labeled DAGs & Strongly Connected Digraphs** | $\hat{D}(x) = \sum_{n \ge 0} \frac{d_n}{n! 2^{\binom{n}{2}}} x^n$ (Graphic EGF) | $\hat{D}(x) = \left(\sum_{n \ge 0} \frac{(-1)^n}{n! \, 2^{\binom{n}{2}}} x^n\right)^{-1}$<br>$\widehat{S}(x) = -\ln\!\Big(2 - \exp^*\!\big(\hat{D}(x)\big)\Big)$ | Source-layer IE on $k$ independent sources divides by $2^{\binom{n}{2}} = 2^{\binom{k}{2} + \binom{n-k}{2} + k(n-k)}$ (**Graphic EGF**). Multiplying termwise by $2^{\binom{n}{2}}$ ($\exp^*$) and taking $-\ln(2 - \cdot)$ extracts strongly connected digraphs (`Luogu P6295`). |
  | **Labeled Bipartite & 2-Colored Graphs** | $\widehat{G}_{\text{2-col}}(x), \; \widehat{B}_{\text{bip}}(x)$ | $\widehat{G}_{\text{2-col}}(x) = \sum_{n \ge 0} 2^{\binom{n}{2}} \frac{x^n}{n!} [t^n]\!\left(\sum_{k \ge 0} \frac{2^{-\binom{k}{2}}}{k!} t^k\right)^2$<br>$\widehat{B}_{\text{bip}}(x) = \exp\!\left(\frac{1}{2} \ln \widehat{G}_{\text{2-col}}(x)\right) = \sqrt{\widehat{G}_{\text{2-col}}(x)}$ | Chirp-Z identity $2^{k(n-k)} = 2^{\binom{n}{2}} 2^{-\binom{k}{2}} 2^{-\binom{n-k}{2}}$ decouples 2-colored graphs into 1 square; every connected bipartite component has $2$ colorings, so $\widehat{C}_{\text{bip}} = \frac{1}{2}\ln \widehat{G}_{\text{2-col}}$ (`Luogu P7364`). |
  | **Labeled Connected Eulerian Graphs** | $\widehat{E}_{\text{conn}}(x)$ | $\widehat{E}_{\text{all}}(x) = \sum_{n \ge 1} 2^{\binom{n-1}{2}} \frac{x^n}{n!}, \quad \widehat{E}_{\text{conn}}(x) = \ln \widehat{E}_{\text{all}}(x)$ | Deleting vertex $n$ bijects even-degree graphs on $n$ vertices to arbitrary graphs on $n-1$ vertices ($\binom{n-1}{2}$ free edges). Connected via $\ln$ in $O(N \log N)$. |
  ```

---

### Gap T-5 [MODERATE]: Missing Roots-of-Unity Filter Row in Section 3.2 & Bivariate PDE Matrix Product Row in Section 3.5.B
- **Locations**:
  1. [`TECHNIQUE_TAXONOMY.md` Line 141](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L141) (End of Section 3.2 Table)
  2. [`TECHNIQUE_TAXONOMY.md` Line 228](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L228) (End of Section 3.5.B Table)
- **Exact Drop-In Rows**:
  1. **Append to Section 3.2 Table (after Line 140)**:
     ```markdown
     | **Signal 7: Modular Index Filter ($k \equiv r \pmod m$)**<br>$S_r(x) = \sum_{k \equiv r \pmod m} f_k x^k$ (`单位根反演`) | Summing every $m$-th coefficient of $F(x)$ when $F(x) = (1+x)^N$ or a rational/exp GF with huge $N \le 10^{18}$. | **Roots of Unity Filter**:<br>Use the orthogonality relation $\frac{1}{m}\sum_{j=0}^{m-1} \omega_m^{j(k - r)} = [k \equiv r \pmod m]$:<br>$$S_r(x) = \frac{1}{m} \sum_{j=0}^{m-1} \omega_m^{-j r} F(\omega_m^j x)!$$ | • **Case 1 ($m \mid (p - 1)$)**: $\omega_m = g^{(p-1)/m} \in \mathbb{F}_p$; evaluate $F(\omega_m^j x)$ at $m$ scalars in $O(m \log N)$ (or **Chirp-Z** if $m$ is large!).<br>• **Case 2 ($m \nmid (p - 1)$, $\gcd(m, p) = 1$)**: Work in the **Cyclotomic Quotient Ring $\mathbb{F}_p[\omega] / (\Phi_m(\omega))$** (`Luogu P5591`, `LOJ #6485`)! |
     ```
  2. **Append to Section 3.5.B Table (after Line 227)**:
     ```markdown
     | **5. Bivariate PDE Companion Matrix Product (`maspypy` & `Elegia`, `QOJ #6184`)** | Need $[x^N] \exp(z g(x)) \bmod z^{K+1}$ or $[x^N] H(x, z)$ where $H$ satisfies a bivariate PDE $a(x) \partial_x H(x, z) = z b(x) H(x, z)$ ($\deg a, \deg b \le d$). | Extracting $[x^n]$ from $a(x) \partial_x H = z b(x) H$ relates $h_n(z) = [x^n] H(x, z)$ to $h_{n-1}(z), \dots, h_{n-d}(z)$ with coefficients that are **linear in $z$** (degree $\le 1$ in $z$)! | Form the $d \times d$ companion transfer matrix $M_n(z) \in K[z]^{d \times d}$ (entries of $z$-degree $\le 1$). Multiply $M_N(z) \cdots M_1(z) \bmod z^{K+1}$ via a **Divide-and-Conquer Matrix Product Tree** in **$O(d^3 N \log^2 N)$** time! |
     ```

---

### Gap T-6 [MODERATE]: Add Section 5 (Master Algorithmic Complexity Reference & 52-Iteration Decision Flowchart)
- **Location**: [`TECHNIQUE_TAXONOMY.md` Line 360](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L360) (End of File)
- **Issue**: Adding a compact Section 5 at the end of `TECHNIQUE_TAXONOMY.md` provides a single-table complexity lookup across all 22 core FPS primitives and a Mermaid decision flowchart routing problem diagnostics to their exact sub-domain in Sections 2–4.
- **Exact Drop-In Section (Append after Line 359 of `TECHNIQUE_TAXONOMY.md`)**:
  ```markdown

  ---

  ## Section 5: Master Algorithmic Complexity Lookup Table & Diagnostic Decision Tree

  ### 5.1 Master Complexity & Precondition Lookup Table ($\bmod x^N$)

  | Operation / Primitive | Dense Complexity | Sparse ($K$ non-zero terms) | Exact Algebraic / Modular Preconditions |
  | :--- | :--- | :--- | :--- |
  | **Multiply $A(x) \cdot B(x)$ / Middle Product `mulT`** | $O(N \log N)$ ($3$ NTTs; $\frac{1}{2}$ length for `mulT`) | $O(N K)$ | NTT prime $p = c \cdot 2^k + 1$ (or 3-Prime CRT for arbitrary $\bmod M$). |
  | **Series Inverse $A(x)^{-1} \bmod x^N$** | $O(N \log N)$ ($1.5\,\mathcal{M}(N)$ via `mulT` Newton) | $O(N K)$ | $[x^0]A \in R^\times$ (zero $n^{-1}$ needed!). |
  | **Square Root $A(x)^{1/2} \bmod x^N$** | $O(N \log N)$ | $O(N K)$ | $2 \in R^\times$; after shifting $\operatorname{val}(A) = 2v$, leading coeff $c_{2v}$ is a QR. |
  | **Derivative $A'(x)$ / Integral $\int A(x)\,dx$** | $O(N)$ | $O(K)$ | $\int$ requires $1, 2, \dots, N-1 \in R^\times$ (**fails for $p \le N-1$**). |
  | **Logarithm $\ln A(x)$ / Exponential $\exp A(x)$** | $O(N \log N)$ | $O(N K)$ | $\ln$: $[x^0]A = 1$; $\exp$: $[x^0]A = 0$; both require $p \ge N$. |
  | **General Power $A(x)^\alpha \bmod x^N$** | $O(N \log N)$ | $O(N K)$ | 3-Way reduction of $\alpha$: shift $v\alpha \in \mathbb{Z}$, scalar $c_v^{\alpha \bmod (p-1)}$, ODE $\alpha \bmod p$. |
  | **Euler / Pólya Transform $\operatorname{MSET}, \operatorname{PSET}, \operatorname{CYC}$** | $O(N \log N)$ (harmonic sieve + $\exp$) | — | $[x^0]A = 0$ and $p \ge N$. |
  | **Taylor Shift $F(x + c)$ / $\alpha$-Euler Transform** | $O(N \log N)$ ($1$ reversed NTT) | — | $p > N$ (or split at pole $k = d + 1$ when $\alpha = -d \le 0$). |
  | **Chirp-Z Transform $F(a \cdot c^i)$ ($m$ points)** | $O((N + m)\log(N + m))$ ($1$ `mulT`) | — | Binomial identity $ij = \binom{i+j}{2}-\binom{i}{2}-\binom{j}{2}$ works for **all** $c \in \mathbb{F}_p^\times$. |
  | **Shift of Sampling Points $F(0..d) \mapsto F(c..c+m-1)$** | $O((d + m)\log(d + m))$ ($1$ NTT) | — | $p > d$. Powers $O(\sqrt{P}\log P)$ factorial. |
  | **Multipoint Evaluation / Interpolation ($N$ points)** | $O(N \log^2 N)$ (division-free `mulT` tree) | — | Interpolation requires $x_i - x_j \in R^\times$ ($i \neq j$). |
  | **1D Bostan–Mori $[x^N] P(x)/Q(x)$ ($\deg Q = d$)** | $O(d \log d \log N)$ ($\frac{2}{3}\mathcal{M}(d)\log_2 N$) | $O(d^2 \log N)$ | $[x^0]Q \in R^\times$ (purely algebraic; works for all $p$!). |
  | **Semi-Online CDQ NTT / Full-Online Relaxed Conv** | $O(N \log^2 N)$ | — | Relaxed conv uses `lowbit(q+1)` binary prefixes (no $p > N$ needed unless $\exp$ ODE). |
  | **Tree DP + Static Top Tree (`Rake` + `Compress`)** | $O(c^2 N \log^2 N)$ ($3c^2$ NTTs per merge) | — | 3-way weighted midpoint split along heavy chains + min-heap on light children. |
  | **Power Projection & Kinoshita–Li `compose`** | $O(N \log^2 N)$ | $O(r N K)$ if $F$ is D-finite | `[x^0]F = 0` (Taylor-shift $G(x + f_0)$ first if $f_0 \neq 0$). |
  | **Compositional Inverse `revert` ($F^{\langle -1 \rangle} \bmod x^N$)** | $O(N \log^2 N)$ | — | $[x^0]F = 0, [x^1]F \in R^\times$. Use Route B (Newton + `compose`) when $p \le N$! |
  | **Twisted Kronecker $d$-Variate $\text{mul}, \text{inv}, \ln, \exp$** | $O(d \cdot N \log N)$ ($N = \prod n_r$) | — | Carry-detector $\chi(I) = (\sum_{r=1}^{d-1}\lfloor I/N_r \rfloor) \bmod d$. |
  | **Set Power Series $\mathcal{R}_n$ ($\text{mul}, \text{inv}, \ln, \exp, \text{comp}$)** | $O(n^2 2^n)$ | — | Contiguous `P[mask * (n+1) + d]` layout; MSB derivative split for $\exp/\ln$ (zero $1/k$!). |
  | **Dirichlet Series $\mathcal{D}_f$ ($\text{mul}, \text{inv}, \ln_D, \exp_D$)** | $O(N \log N)$ (divisor sieve) | — | Uses completely additive $\Omega(n)$-derivation $\vartheta f(n) = \Omega(n)f(n)$ ($p > \log_2 N$). |

  ### 5.2 Master 7-Stage Diagnostic Flowchart

  ```mermaid
  flowchart TD
      Start["Problem Input: Count / Expected Value / DP / Binomial Sum"] --> S1{"1. Underlying Index Ring?"}
      S1 -- "Subset Union (n <= 21)" --> SPS["Set Power Series R_n: O(n^2 2^n) Ranked Zeta + ODE (§2.3, §3.8)"]
      S1 -- "Divisibility i * j = n" --> DGF["Dirichlet GF: O(N log N) Sieve + Omega(n)-Derivation (§2.3, §3.8)"]
      S1 -- "q-Inversions / F_q^n Subspaces" --> QSer["q-Series: x -> qx Difference Eq / Pentagonal / q-Lucas (§2.3, §3.8)"]
      S1 -- "Additive i + j = n or Difference i - j = k" --> S2{"2. Combinatorial / DP Structure?"}

      S2 -- "Unlabelled (MSET / PSET / CYC / Trees)" --> OGF["OGF Symbolic Method + Euler Transform + Otter Dissimilarity (§2.1, §2.2)"]
      S2 -- "Labelled (SET / Boxed / Graphs / Cacti)" --> EGF["EGF Symbolic Method + exp/ln + Boxed Product + Block-Cut (§2.2)"]
      S2 -- "Adjacent / Pattern / Stopping Time" --> IEPGF["Run-Length IE W/(1+W) / Cluster Method / PGF F(1+t) mod t^3 (§3.3)"]
      S2 -- "Coupled Sum / Implicit / Walk / Tree DP" --> S3{"3. Algebraic / Analytic Bottleneck?"}

      S3 -- "Binomial Sum S_n = sum_k T(n, k)" --> Bin["4-Engine Binomial Guide: Snake Oil / Egorychev / EI Diff-Residue (§3.1.B)"]
      S3 -- "Implicit F = x Phi(F) or Coupled System" --> LIF["6-Form Lagrange Inversion / Good-Lagrange / MacMahon (§3.4, §3.5.B)"]
      S3 -- "2D Rational [x^N] P(x,y)/Q(x,y) or Walk" --> Biv["4-Regime 2D Bostan-Mori / Furstenberg Residue / Kernel Method (§3.5)"]
      S3 -- "D-Finite ODE / Sparse P(x) / Huge N <= 10^7" --> ODE["7-Archetype ODE Linearization / O(NK) Sparse FPS / EI Truncated ODE (§3.6)"]
      S3 -- "Self-Referential / Tree DP / Compose / CZT" --> Adv["CDQ vs Relaxed Conv / Static Top Tree / Kinoshita-Li / CZT (§3.7)"]
  ```
  ```

---

## 4. Citation Completeness & Attribution Audit (`CITATIONS.md` vs. All Source Files)

Every bibliography table across all 10 `cohort3_wave_*.md` files and all Cohort 1 / Cohort 2 (`iter_*.md`, `cohort2_*.md`) files was cross-checked against `CITATIONS.md`. Below are the **6 attribution and completeness findings** (`C-1` through `C-6`) with drop-in additions.

---

### Issue C-1 [MAJOR]: Author & Handle Attribution Clarification (`Elegia` / 吕欣 vs. `EntropyIncreaser` / `rushcheyo` / 虞皓翔 vs. `Athekatelan` / 钱易)
- **Location**: [`CITATIONS.md` Lines 70–72 (`[ZH-NT-El19a]`, `[ZH-NT-El19b]`, `[ZH-NT-El18]`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L70-L72)
- **Issue**:
  - Across the Cohort 1/2/3 files (`iter_31_to_35` L1462, `iter_36_to_40` L696 & L1246, `cohort2_iter_78_to_82` L42 & L1252, `cohort3_wave_4a` L1299–1300), three Chinese Olympiad authors who collaborated closely on generating function theory are referenced:
    1. **吕欣 (Lü Xin / Baitian Li / `Elegia` / `EI` / `EI_Captain` / `铃悬`)**: Author of the 2018 & 2019 IOI National Team papers (*《集合幂级数的性质与应用及其快速算法》*, *《生成函数的组合意义与代数操作》* / *《浅谈微分有限生成函数》*), WC 2019 lecture notes, `UOJ #514` / `[ZJOI2019] 开关` editorials, and co-author of Kinoshita–Li (FOCS 2024).
    2. **虞皓翔 (Yu Haoxiang / `EntropyIncreaser` / `rushcheyo`, `https://entropyincreaser.com/`, `https://rushcheyo.blog.uoj.ac/blog/6547`)**: Author of *《炫酷反演魔术》*, *《再谈 Binomial Sum：多项式复合、插值与泰勒展开》*, *《驻波》*, *《多元形式幂级数算法简明指南》*, and `UOJ #596` notes on Luogu / UOJ / `entropyincreaser.com`.
    3. **钱易 (Qian Yi / `Athekatelan`)**: Co-author with 吕欣 (`Elegia`) of the 2021 IOI National Team homework thesis *《信息学竞赛中的生成函数计算理论框架》* (`iter_36_to_40` L696 & L1246).
  - Currently, `CITATIONS.md` Lines 70–72 merge all three into `吕欣 (Lü Xin / Elegia / EntropyIncreaser)` and omit 虞皓翔 (`Yu Haoxiang / rushcheyo`) and 钱易 (`Qian Yi / Athekatelan`) by name. (Note also that `cohort3_wave_5a` Lines 1410–1413 erroneously wrote `Elegia / 钟子谦 (EntropyIncreaser)` — 钟子谦 is `zzq`, not `Elegia`!).
- **Exact Fix for `CITATIONS.md` Lines 70–72**:
  Explicitly credit both **吕欣 (Lü Xin / Baitian Li / `Elegia` / `EI_Captain`)** and **虞皓翔 (Yu Haoxiang / `EntropyIncreaser` / `rushcheyo`)** as well as **钱易 (Qian Yi / `Athekatelan`)** in `[ZH-NT-El19a]`, `[ZH-NT-El19b]`, and `[ZH-NT-El18]`:
  - Line 70 Author column: `**吕欣 (Lü Xin / `Elegia`) & 虞皓翔 (Yu Haoxiang / `EntropyIncreaser` / `rushcheyo`)**`
  - Line 71 Author column: `**吕欣 (Lü Xin / `Elegia` / `EI_Captain`) & 虞皓翔 (Yu Haoxiang / `EntropyIncreaser`)**`
  - Line 72 Author column: `**吕欣 (Lü Xin / `Elegia`), 虞皓翔 (`EntropyIncreaser` / `rushcheyo`), & 钱易 (Qian Yi / `Athekatelan`)**` (and add *《信息学竞赛中的生成函数计算理论框架》* (2021) and *《多元形式幂级数算法简明指南》* (`https://rushcheyo.blog.uoj.ac/blog/6547`) to Column 3 of Line 72).

---

### Issue C-2 [MODERATE]: Missing `[EN-Pr-BGS07]` (Bostan, Gaudry, & Schost 2007) in Category II
- **Source**: [`iter_46_to_52_tree_fps_transposition_compose_q.md` Line 529](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_46_to_52_tree_fps_transposition_compose_q.md#L529) (Wave 5B, Iter 49 / 101)
- **Why Essential**: This is the foundational paper that invented the **$O(\sqrt{P}\log P)$ Subquadratic Factorial & Holonomic Matrix Baby-Step Giant-Step Algorithm via Shift of Sampling Points** (`LOJ #161` / `Luogu P5282`), which is a core topic of Iteration 49 / 101 (`CITATIONS.md` Line 168).
- **Exact Drop-In Row for `CITATIONS.md` Category II (Insert after Line 62)**:
  ```markdown
  | **`[EN-Pr-BGS07]`** | **Alin Bostan, Pierrick Gaudry, & Éric Schost (2007)** | *"Linear Recurrences with Polynomial Coefficients and Application to Integer Factorization and Cartier–Manin Operator"*, **SIAM Journal on Computing** 36(6), 1777–1806. URL: <https://specfun.inria.fr/bostan/publications/BoGaSc07.pdf> | Introduces **Shift of Sampling Points** via falling-factorial Lagrange convolution $F(0..d) \mapsto F(c..c+m-1)$ in $O(d \log d)$ time, achieving **$O(\sqrt{P}\log P)$ factorial evaluation $N! \bmod P$** and $O(\sqrt{N}\log N)$ evaluation of P-recursive sequences. | Wave 5B |
  ```
  *(Also add `"[EN-Pr-BGS07]"` to Column 4 of Row `49 / 101` on Line 168 of `CITATIONS.md`.)*

---

### Issue C-3 [MODERATE]: Missing `[ZH-NT-YJ18]` (杨骏 Yang Jun 2018 National Team Paper on Dynamic DP & `全局平衡二叉树`) in Category III
- **Source**: [`iter_46_to_52_tree_fps_transposition_compose_q.md` Lines 487 & 535](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_46_to_52_tree_fps_transposition_compose_q.md#L535) (Wave 5B, Iter 46 / 98)
- **Why Essential**: Yang Jun's 2018 IOI Chinese National Team Paper *《浅谈“动态DP”》* is the original source of **Globally Balanced Binary Search Trees (`全局平衡二叉树`)** and heavy-light chain matrix divide-and-conquer (`Luogu P4719`), which is featured in Iteration 46 / 98 (`CITATIONS.md` Line 165 & Entry #65 Line 275).
- **Exact Drop-In Row for `CITATIONS.md` Category III (Insert after Line 78)**:
  ```markdown
  | **`[ZH-NT-YJ18]`** | **杨骏 (Yang Jun)** | *《浅谈“动态DP”》 (A Brief Discussion on Dynamic DP)* (**2018 IOI Chinese National Team Paper**). URL: <https://github.com/hzwer/shareOI> | Origin of **Globally Balanced Binary Search Trees (`全局平衡二叉树`)** and Heavy-Light Decomposition transfer-matrix divide-and-conquer (`Luogu P4719`), proving the $O(N \log^2 N)$ worst-case bound via weighted-midpoint splitting along heavy chains. | Wave 5B |
  ```
  *(Also add `"[ZH-NT-YJ18]"` to Column 5 of Row `46 / 98` on Line 165 of `CITATIONS.md`.)*

---

### Issue C-4 [MODERATE]: Missing `[ZH-Bg-War21]` (`warzone` 2021 on Transposition Principle) in Category III
- **Source**: [`iter_46_to_52_tree_fps_transposition_compose_q.md` Line 541](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_46_to_52_tree_fps_transposition_compose_q.md#L541) (Wave 5B, Iter 47 / 99)
- **ExactFix**: Append `warzone` (2021), *《浅谈转置原理》 (Luogu Column & `Luogu P7440` / `UOJ #604` Editorial)* (`https://www.luogu.com.cn/problem/solution/P7440`) to **`[ZH-NT-CY20]`** on **Line 77** of `CITATIONS.md`.

---

### Issue C-5 [MODERATE]: Missing `[JA-Bg-Ha21]` (`hamamu` Qiita FPS Compendium & `DEGwer` *数え上げPDF*) in Category IV
- **Sources**:
  - [`iter_06_to_10_dp_and_sums.md` Line 1489](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_06_to_10_dp_and_sums.md#L1489)
  - [`cohort2_iter_58_to_62_dp_and_sums.md` Lines 987 & 1011](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_58_to_62_dp_and_sums.md#L987-L1011)
- **Exact Drop-In Row for `CITATIONS.md` Category IV (Insert after Line 100)**:
  ```markdown
  | **`[JA-Bg-Ha21]`** | **`hamamu` & `DEGwer`** | **`hamamu` (2021–2025)**: *AtCoderで解ける形式的べき級数問題を集めました (Collection of ~100 FPS Problems on AtCoder)*, Qiita (<https://qiita.com/hamamu/items/05cdfd3a15ecab22119e>); **`DEGwer` (2017)**: *数え上げテクニック集 (`数え上げPDF`)* (<https://degwer.hatenablog.com/entry/20171220>). | Comprehensive Japanese problem-to-technique classification of ~100 AtCoder FPS problems by difficulty and algebraic pattern, alongside `DEGwer`'s classic Olympiad enumeration handbook (Vandermonde, Snake Oil, trees, and inclusion-exclusion). | Waves 1A, 1B, 2A, 2B |
  ```
  *(Also add `https://noshi91.hatenablog.com/entry/2024/11/08/214805` [Lagrange Inversion Variants Cheat Sheet] and `https://noshi91.github.io/algorithm-encyclopedia/` to **`[JA-Bg-No19]`** on Line 94 of `CITATIONS.md`.)*

---

### Issue C-6 [MODERATE]: Missing `[EN-CP-CPA]` (CP-Algorithms Polynomial & Graph Enumeration Series) in Category V
- **Sources**:
  - [`iter_11_to_15_substitutions_transforms.md` Line 1597](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_11_to_15_substitutions_transforms.md#L1597)
  - [`cohort2_new_iter_63_to_67_substitutions_transforms.md` Line 1538](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_new_iter_63_to_67_substitutions_transforms.md#L1538)
  - [`cohort2_iter_73_to_77_lagrange_residues_trees_graphs.md` Line 1369](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_73_to_77_lagrange_residues_trees_graphs.md#L1369)
- **Exact Fix**: Add *CP-Algorithms: "Operations on Polynomials and Series"* (`https://cp-algorithms.com/algebra/polynomial.html`) and *"Counting Labeled Graphs"* (`https://cp-algorithms.com/combinatorics/counting_labeled_graphs.html`) to **`[EN-CP-Ad20]`** on **Line 108** of `CITATIONS.md` (since `adamant` / Maxim Akhmedov authored the CP-Algorithms polynomial section).

---

## 5. Formatting & Delimiter Check (`TECHNIQUE_TAXONOMY.md` & `CITATIONS.md`)

### 5.1 Banned Math Delimiters (`\(...\)` and `\[...\]`)
- **`TECHNIQUE_TAXONOMY.md`**: **0 occurrences** of `\(...\)` or `\[...\]` (100% compliant).
- **`CITATIONS.md`**: **0 occurrences** of `\(...\)` or `\[...\]` (100% compliant).

### 5.2 Broken Markdown Pipe Tables Caused by Unescaped `|` Inside Inline Math (`$...$`)
In GitHub-Flavored Markdown (GFM) and standard Markdown parsers, raw pipe characters `|` inside `$...$` inline math inside a Markdown table row `| ... |` are parsed as **table column separators** unless replaced by `\lvert ... \rvert` (or `\mid` / `\rvert`).

#### A. 8 Table Rows to Fix in `TECHNIQUE_TAXONOMY.md`

| Line # | Current Raw Pipe Expression Inside Table Cell | Exact Replacement (`\lvert ... \rvert`) |
| :---: | :--- | :--- |
| **[Line 49](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L49)** | `$\frac{1}{|G|} \sum_{g \in G} \prod_{j=1}^k s_j^{c_j(g)}$` | `$\frac{1}{\lvert G \rvert} \sum_{g \in G} \prod_{j=1}^k s_j^{c_j(g)}$` |
| **[Line 59](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L59)** | `with $|S|=k$.` | `with $\lvert S \rvert = k$.` |
| **[Line 82](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L82)** | `$\widehat{F}_M(t) = \sum_{S \subseteq M} f_S t^{|S|} \in K[t]/(t^{n+1})$` | `$\widehat{F}_M(t) = \sum_{S \subseteq M} f_S t^{\lvert S \rvert} \in K[t]/(t^{n+1})$` |
| **[Line 150](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L150)** | `($|E| \le N$).` | `($\lvert E \rvert \le N$).` |
| **[Line 152](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L152)** | `($|\Sigma| = \alpha$)`, `$1 \le k \le |w_i|$`, `$w_i[|w_i|-k+1 \dots |w_i|]$`, `$x^{|w_j| - k}$`, `$x^{|w|}$`, `$\mathbf{x}^{|\mathbf{w}|}$` | `($\lvert \Sigma \rvert = \alpha$)`, `$1 \le k \le \lvert w_i \rvert$`, `$w_i[\lvert w_i \rvert-k+1 \dots \lvert w_i \rvert]$`, `$x^{\lvert w_j \rvert - k}$`, `$x^{\lvert w \rvert}$`, `$\mathbf{x}^{\lvert \mathbf{w} \rvert}$` |
| **[Line 224](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L224)** | `over $|y| = \varepsilon$:` | `over $\lvert y \rvert = \varepsilon$:` |
| **[Line 332](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L332)** | `with $|\lambda| = \frac{m(3m-1)}{2}$` | `with $\lvert \lambda \rvert = \frac{m(3m-1)}{2}$` |
| **[Line 333](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L333)** | `$\widehat{F}_M(t) = \sum_{S \subseteq M} f_S t^{|S|} \in K[t]/(t^{n+1})$` | `$\widehat{F}_M(t) = \sum_{S \subseteq M} f_S t^{\lvert S \rvert} \in K[t]/(t^{n+1})$` |

#### B. 6 Table Rows to Fix in `CITATIONS.md`

| Line # | Current Raw Pipe Expression Inside Table Cell | Exact Replacement (`\lvert ... \rvert`) |
| :---: | :--- | :--- |
| **[Line 48](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L48)** | `fixed excess $k = |E| - |V| \ge 1$` | `fixed excess $k = \lvert E \rvert - \lvert V \rvert \ge 1$` |
| **[Line 53](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L53)** | `whenever $|G| < \infty$.` | `whenever $\lvert G \rvert < \infty$.` |
| **[Line 150](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L150)** | `via $\partial_y|_{y=1}$,` | `via $\partial_y\rvert_{y=1}$,` |
| **[Line 218](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L218)** | `$C_S(x) = \sum_{k \in \operatorname{Border}(S)} c^k x^{|S|-k}$` | `$C_S(x) = \sum_{k \in \operatorname{Border}(S)} c^k x^{\lvert S \rvert - k}$` |
| **[Line 223](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L223)** | `$\sum_{|T| \ge k} (-1)^{|T|-k}\binom{|T|-1}{k-1}\mathbb{E}[\min_{i \in T} T_i]$` | `$\sum_{\lvert T \rvert \ge k} (-1)^{\lvert T \rvert - k}\binom{\lvert T \rvert - 1}{k-1}\mathbb{E}[\min_{i \in T} T_i]$` |
| **[Line 244](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CITATIONS.md#L244)** | `$k = |E|-|V|$` and `(k = |E| - |V| \ge 1)` | `$k = \lvert E \rvert - \lvert V \rvert$` and `(k = \lvert E \rvert - \lvert V \rvert \ge 1)` |
