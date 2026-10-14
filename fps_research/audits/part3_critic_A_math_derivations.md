# Part III Critic A Audit Report: Mathematical Rigor, Single-Step Derivations & Zero-Magic-Steps (`Ch 09`–`Ch 13` & `CP-III`)

- **Auditor**: FPS Textbook Critic & Mathematical Auditor (Part III Critic A)
- **Scope**:
  1. `chapters/ch09-cdq-fft-online-relaxed-convolution.qmd` (1,350 lines)
  2. `chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd` (1,351 lines)
  3. `chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd` (1,654 lines)
  4. `chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd` (1,117 lines)
  5. `chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd` (1,532 lines)
  6. `checkpoints/cp03-part3-online-implicit-lif-graphs.qmd` (1,296 lines)
- **Audit Dimensions**:
  1. Mathematical Accuracy & Index Boundary Verification ($n = 0, 1, 2$ base cases & hand traces)
  2. Zero Magic Steps & Reverse-Engineering Scratchpads (no skipped steps, no raw draft trial-and-error / `"Wait..."` monologues)
  3. Strict Prerequisite Closure & Zero Forward-Reference Audit (`<= Ch k` and `<= Part III`)
  4. 100% Sub-Section, Failure Mode & Characteristic-$p$ Completeness + Revisited Cross-References
  5. 8-Problem Ladder & Blind Checkpoint Spoiler-Free Completeness Audit
  6. `AGENTS.md` Editorial Policy Compliance
  7. Citations & Terminology Integration
  8. Quarto Formatting & Render Safety (emphatic `!` inside `$...$` / `$$...$$`, broken internal `.qmd` links, chapter number mismatches)

---

## Executive Summary & Severity Matrix

| File | Critical Issues | Major Issues | Minor / Editorial Issues | Overall Assessment |
| :--- | :-: | :-: | :-: | :--- |
| **`ch09-cdq-fft-online-relaxed-convolution.qmd`** | **2** | **4** | **1** | Theory & code contracts are strong, but `SS-2 (#021)` has a severe mathematical contradiction ($H_2 = 8$ vs. $H_2 = 6$), `Mas-1 (#206)` misses the $k=0$ base-case transfer in CDQ NTT, `SS-1 (#060)` leaves transition weights undefined, and §9.3 / `Mas-2` contain raw draft false-starts (`"Wait..."`). |
| **`ch10-implicit-equations-newton-unlabeled-trees-otter.qmd`** | **0** | **2** | **2** | Excellent exposition of 1D/2D Newton, Pólya higher-power trick, and Otter's theorem. Needs repair in `Adv-2 (#126/#167)` (incomplete `\dots` fraction at L1068 and forward-reference to Ch 11 LIF at L1094) and removal of emphatic `!` inside `$$...$$`. |
| **`ch11-laurent-residues-raney-lagrange-inversion.qmd`** | **1** | **2** | **4** | Masterful treatment of Laurent residues, 6-form LIF, and char-$p$ Frobenius decimation, **except** `Mas-1 (#114 CF 1349F2)` has a sign error in $\text{Term}_2(j)$ ($w + 1 - e^w$ instead of $e^w - 1 - w$, giving $c_0 = 5/3 \neq 1$), refers to Newton's method as "Chapter 7" instead of "Chapter 10" in 5 places, and has raw trial-and-error (`"BINGO!"`, `"Wait..."`) in `Mas-1` and `Int-1`. |
| **`ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`** | **0** | **0** | **0** | **Gold Standard (100% Clean)**. Every derivation, sign, base case ($n=1, 2, 3, 4$), failure mode, and practice problem solution in `Ch 12` is mathematically airtight and editorially polished. |
| **`ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd`** | **0** | **1** | **0** | **Mathematically 100% Clean**. All graphical EGFs, Chirp-$z$ twists, Robinson–Stanley IE, Matrix-Tree, BEST, and Symbolic Matrix-Tree derivations are rigorous and verified on $n \le 4$. Only internal `.qmd` link filenames and chapter numbers (`Ch 06` vs `Ch 07`, `Ch 12` filename, `Ch 14` filename) need fixing. |
| **`cp03-part3-online-implicit-lif-graphs.qmd`** | **0** | **0** | **1** | **99.9% Clean**. Stage 1 is 100% spoiler-free (zero chapter/technique leaks in statements or `Hint 1`), and all 8 Stage 2 derivations and hand-traces are exact. Only a single conversational `"Wait —"` in `CP-III.7` (L1161) needs trimming. |

---

## Detailed File-by-File Audit Findings & Concrete Fixes

---

### 1. `chapters/ch09-cdq-fft-online-relaxed-convolution.qmd`

#### [CRITICAL-09-1] Mathematical Self-Contradiction & Wrong Functional Equation in `SS-2 (#021) ABC 222 H — Beautiful Binary Tree` (Lines 644–741)
- **Location**: Lines 648, 667–669, 695–739.
- **What Is Wrong**:
  1. **Self-Contradiction Between Method 1 and Method 2**:
     - In Step 1 (lines 695–698), the text writes the coupled system
       $$T_0(x) = x\big(1 + T_0(x) + T_1(x)\big)^2, \qquad T_1(x) = T_0(x)\big(1 + T_0(x)\big)^2,$$
       which eliminates to $T_0(x) = x\big(1 + 2T_0(x) + 2T_0(x)^2 + T_0(x)^3\big)^2$.
     - In Step 2 (Method 1, lines 700–712), expanding this equation gives $t_1 = 1$, $t_2 = [x^1](1 + 4T_0 + \dots) = 4$, and $H_2 = 2 t_2 = \mathbf{8}$ (line 712).
     - In Step 3 (Method 2, lines 715–739), the author attempts a substitution $U(x) = T_0(x)(1 + T_0(x))$ and claims at line 717:
       $$U(x) = x\big(1 + T_0(x)\big)\Big(1 + 3 U(x) + U(x)^2\big(1 + U(x)\big)\Big)?$$
       Then at lines 719–723 (`"Wait: let us check that identity by expanding the right-hand side:"`), the author notices that $(1+T_0)(1+2T_0+2T_0^2+T_0^3)^2$ is **not** a function of $U(x) = T_0(1+T_0)$ alone, abandons $U(x)$, and abruptly asserts at lines 730–739 without proof that
       $$H_N = N [x^N] T_0(x) = [y^{N-1}] P(y)^N \quad \text{where } P(y) = 1 + 3y + y^2(1 + y)^2 = 1 + 3y + y^2 + 2y^3 + y^4,$$
       computing $H_2 = [y^1] P(y)^2 = \mathbf{6}$ at line 739!
     - Thus **Line 712 says $H_2 = 8$ while Line 739 says $H_2 = 6$**, and mathematically by Lagrange Inversion on $T_0(x) = x \Phi(T_0(x))$ with $\Phi(y) = (1 + 2y + 2y^2 + y^3)^2$, we actually have $N [x^N] T_0(x) = [y^{N-1}] \Phi(y)^N = [y^{N-1}](1 + 2y + 2y^2 + y^3)^{2N}$ (which gives $H_2 = [y^1](1 + 2y + \dots)^4 = 8$), **not** $[y^{N-1}] P(y)^N$!
  2. **Mismatch with Actual AtCoder `ABC 222 H` Rules**:
     - In the actual AtCoder problem `ABC 222 H`, a vertex with label `0` **cannot be a leaf** and can only have children with label `1` (so $T_0 = (1 + T_1)^2 - 1 = 2T_1 + T_1^2$), while a vertex with label `1` has $x$-weight $x$ and children of label `0` or `1` (so $T_1 = x(1 + T_0 + T_1)^2 = x(1 + 3T_1 + T_1^2)^2$), which yields $H_N = \frac{1}{N}[y^{N-1}](1 + 3y + y^2)^{2N}$.
     - Whether you keep the simplified problem statement currently written in lines 646–650 (where $T_0 = x(1 + 2T_0 + 2T_0^2 + T_0^3)^2$, so $\Phi(y) = (1 + 2y + 2y^2 + y^3)^2$ and $H_N = N[x^N]T_0(x) = [y^{N-1}](1 + 2y + 2y^2 + y^3)^{2N}$, giving $H_1 = 1, H_2 = 8, H_3 = 60$) or update the rules to match official `ABC 222 H` ($T_1 = x(1 + 3T_1 + T_1^2)^2$, giving $H_1 = 1, H_2 = 6, H_3 = 45$), **Method 1 and Method 2 must solve the exact same equation, give the exact same numbers, and contain zero `"Wait:"` self-corrections**.

#### [CRITICAL-09-2] Missing $k = 0$ Base-Case Transfer in CDQ NTT for `Mas-1 (#206) UOJ 50 — Chain Reaction` (Lines 1201–1205)
- **Location**: Lines 1190–1205.
- **What Is Wrong**:
  - In Solution 2 (Coupled CDQ Divide-and-Conquer NTT for $F'(x) = \frac{1}{2}A(x)F(x)^2 + 1$), the recurrence is written in shifted variables $\tilde{f}_n = \frac{f_n}{n!}$, $\tilde{a}_n = \frac{a_n}{n!}$, $S(x) = F(x)^2$, and $P(x) = A(x) S(x)$:
    $$p_n = \sum_{i + k = n} s_i \, \tilde{a}_k, \qquad \tilde{f}_{n+1} = \frac{p_n}{2(n + 1)} \quad (n \ge 1).$$
  - At line 1205, the cross-boundary transfer from $[l, m]$ to $[m+1, r]$ computes:
    $$\text{Transfer } s[l \dots m] \times \tilde{a}[0 \dots r - l] \to p[m+1 \dots r].$$
  - Notice that for any target index $j \in [m+1, r]$ and source index $i \in [l, m]$, their difference is $k = j - i \ge 1$. Therefore, **no cross-boundary transfer ever adds the $k = 0$ term $s_j \tilde{a}_0$ to $p_j$**!
  - Since $a_0 \in \{0, 1\}$ can be $1$ (in fact, the hand trace at line 1197 explicitly uses $p_2 = \tilde{a}_0 s_2 = a_0$!), omitting $s_q \tilde{a}_0$ at the leaf $l = r = q$ produces wrong answers whenever $a_0 = 1$.
  - Furthermore, line 1203 contains a draft self-correction (`"We first finalize $s[l \dots m]$? Careful: $s_i$ is finalized at the leaf $l = r = i$!"`).
- **Concrete Fix**:
  - In the leaf base case $l = r = q$ ($q \ge 1$):
    1. Finalize $s_q$ by adding the diagonal/endpoint terms ($2 \tilde{f}_0 \tilde{f}_q = 0$ since $\tilde{f}_0 = 0$, and $+ \tilde{f}_{q/2}^2$ if $2 \mid q$).
    2. **Add the $k = 0$ term**: `p[q] = (p[q] + s[q] * a_tilde[0]) % MOD;`.
    3. Finalize $\tilde{f}_{q+1} = \frac{p_q}{2(q + 1)}$.
  - In the cross-boundary step $[l, m] \to [m+1, r]$, convolve $s[l \dots m]$ with $\tilde{a}[1 \dots r - l]$ into $p[m+1 \dots r]$.

#### [MAJOR-09-1] Undefined Symbols $\psi_n$ and $w_{n,i}$ in `SS-1 (#060) ARC 138 E — Decreasing Subsequence` (Lines 607–631)
- **Location**: Lines 616 and 628.
- **What Is Wrong**:
  - Hint 2 (line 616) and the Complete Derivation (line 628) write:
    $$dp[n] = \psi_n\!\left(\sum_{i=0}^{n-1} dp[i] \binom{n+i}{n-i} w_{n, i}\right),$$
    without **ever defining** what the function $\psi_n(\cdot)$, the weight $w_{n, i}$, or the base case $dp[0]$ are! This violates the Zero-Magic-Steps and Self-Contained Solution rules.
- **Concrete Fix**:
  - State the exact combinatorial meaning of $dp[i]$, the exact closed form of the transition coefficient, and how it splits into $f_i \cdot g_{n-i} \cdot h_{n+i}$ (a standard convolution plus a correlation/Hankel convolution, both handled in $O(N \log^2 N)$ by CDQ NTT or $O(N \log N)$).

#### [MAJOR-09-2] Confusing False Start & Conversational Self-Correction in §9.3 `RelaxedConvolution` Grid (Lines 304–370)
- **Location**: Lines 304–370.
- **What Is Wrong**:
  - Lines 304–340 present a 0-indexed `lowbit(q + 1)` rule with `A[d - 1 ... 2d - 2] x B[d - 1 ... 2d - 2]` and draw a 0-indexed table where $(0, 5)$ and $(5, 0)$ are labeled $q = 5$.
  - Then at line 349, the text interrupts itself mid-sentence:
    `"—wait! Why did the table above show $q = 5$ at $(0, 5)$ and $(5, 0)$? Because if we want a clean 0-indexed boundary where $a_0$ and $b_0$ are also handled..."`
    and admits that `B[1..2]` does **not** cover $(5, 0)$ or $(0, 5)$, before switching to **Convention A** (handling border terms $a_q b_0 + a_0 b_q$ in $O(1)$ and running 1-indexed `lowbit(q)` on the interior $i, j \ge 1$).
  - Also line 311 contains `"(Wait: since $c[0 \dots d - 2]$ have already been output...)"`.
- **Concrete Fix**:
  - Teach **Convention A** (1-indexed interior grid $i, j \ge 1$ with $d = \operatorname{lowbit}(q)$ and explicit $O(1)$ border terms $a_q b_0 + a_0 b_q$) directly from the start of §9.3! Draw the 1-indexed interior partition table for $(i, j) \in \{1 \dots 8\}^2$, and delete the broken 0-indexed false start and `"—wait!"` monologue.

#### [MAJOR-09-3] False Start, Draft Monologue & Hint Contradiction in `Mas-2 (#075) AGC 060 D — Same Descent Set` (Lines 1254–1297)
- **Location**: Lines 1256–1261 and 1286–1297.
- **What Is Wrong**:
  - In Step 2 (lines 1286–1291), the author derives an incorrect formula $U(x) = \frac{e^x - 1}{2e^x - 1}$, checks $M = 1$, writes `"= 1? Wait: if we force \sigma_i(P) = 2[P_i < P_{i+1}] - 1..."`, realizes $e^x - 1$ had the wrong sign on $k - 1$, and re-derives the correct formula $U(x) = \frac{e^{2x} - 1}{e^{2x} + 1} = \tanh(x)$ at lines 1292–1297.
  - Meanwhile, Hint 3 (lines 1256–1261) still contains a third incompatible formula $U(x) = \frac{2(e^x - 1)}{e^x + 1}$ and $\text{Ans}_N = (N!)^2 2^{N-1}[x^N]\frac{W(x)}{1 \pm \frac{1}{4}W(x)}$, which contradicts Step 3 (line 1311: $\text{Ans}_N = \frac{(N!)^2}{2^{N+1}}[x^N]\frac{W(x)}{1 - W(x)}$).
- **Concrete Fix**:
  - Delete the false start at lines 1286–1291 and present the $(-1)^k (e^{2x} - 1)$ run-block derivation of $U(x) = \frac{e^{2x} - 1}{e^{2x} + 1}$ cleanly on the first pass. Update Hint 3 (lines 1256–1261) to match Step 2 and Step 3 ($U(x) = \frac{e^{2x}-1}{e^{2x}+1}$ and $\text{Ans}_N = \frac{(N!)^2}{2^{N+1}}[x^N]\frac{W(x)}{1 - W(x)}$).

#### [MAJOR-09-4] Emphatic Exclamation Marks `!` Inside Display Math `$$...$$` Rendering as Factorials in `Ch 09`
- **Location**: Lines 375, 550, 721, 882, 1261, 1277, 1286, 1296.
- **What Is Wrong**:
  - Ending a display math block with `!$$` renders a LaTeX factorial symbol `!` right after the formula (e.g., line 882 renders $0 \le r < k!$ and line 1261 renders $\frac{W(x)}{1 \pm \frac{1}{4}W(x)}!$, which is mathematically misleading).
- **Concrete Fix**: Replace every trailing `!$$` with `.$$` (or move the exclamation mark outside `$$...$$`).

#### [MINOR-09-1] Missing Revisited Dual-Perspective Cross-Reference (`#244 yukicoder 3029`) in §9.3
- **Location**: Section 9.3 (around line 552).
- **What Is Wrong**: `CURRICULUM_ARCHITECTURE.md` §5.2 (Row 7) specifies that `Ch 09 (9.3)` should include a cross-reference to `#244 yukicoder 3029 — Colored Tree` comparing Coupled Online Relaxed Convolution ($O(N \log^2 N)$) with `Ch 10.2` $2 \times 2$ Jacobian Newton ($O(N \log N)$).
- **Concrete Fix**: Add a 2-sentence callout/note at the end of §9.3 pointing to `#244 yukicoder 3029` in `Ch 10 (Int-1)`.

---

### 2. `chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd`

#### [MAJOR-10-1] Incomplete Placeholder Fraction & Unjustified Forward Reference to `Ch 11` LIF in `Adv-2 (#126 / #167) CF 1687F — Koishi's Unconscious Permutation` (Lines 1068 & 1091–1095)
- **Location**: Lines 1068 and 1091–1095.
- **What Is Wrong**:
  1. Line 1068 contains a raw, unfinished LaTeX fraction with `\dots` in the numerator and `1` in the denominator:
     $$C(z, t) = \ln \frac{1}{1 - t \frac{e^z - 1 - (1 - t^{-1})\dots}{1}} = \ln \frac{1}{1 - \sum_{m \ge 1} (t - 1)^{m-1} t \frac{z^m}{m!}} = -\ln\!\left(1 - \frac{t}{t - 1}\big(e^{(t - 1)z} - 1\big)\right).$$
  2. In Step 3 (lines 1091–1095), instead of solving the implicit equation via Chapter 10 Newton iteration (or giving the complete self-contained algebraic steps), line 1094 abruptly writes:
     $$\text{"Using }\left(\frac{g(w)}{w}\right)^{-n} g'(w) \bmod w^{n+1}\text{ (`pow` + `mul`) extracts all required coefficients }\alpha_k\text{ in }O(n \log n)\text{ time."}$$
     This formula is **Canonical Form 2 of Lagrange Inversion**, which is not taught until **Chapter 11 (§11.2)**! Moreover, the exact indices and relationship between $\alpha_k$, $s$, and the final answer for each $k = 0 \dots n-1$ are hand-waved in 4 lines.
- **Concrete Fix**:
  - Replace the `\frac{1}{1 - t \frac{e^z - 1 - (1 - t^{-1})\dots}{1}}` placeholder at line 1068 with the clean geometric sum $\sum_{m \ge 1} t(t-1)^{m-1} \frac{z^m}{m!} = \frac{t}{t-1}(e^{(t-1)z} - 1)$.
  - In Step 3 (lines 1091–1095), show how $g(w) = \frac{\ln(1 + w)}{\ln(1 + w) - w/(1+w)}$ (or the implicit compositional inverse $w(z)$ satisfying $g(w(z)) = z$) is inverted up to $z^n$ using **Chapter 10 Newton Iteration** $w_{2d}(z) = w_d(z) - \frac{g(w_d(z)) - z}{g'(w_d(z))} \bmod z^{2d}$ (and add a brief forward pointer noting that `Ch 11` Lagrange Inversion will provide a single-`pow` shortcut for fixed $n$). Write out the explicit convolution extracting the answer for each $k \in \{0, \dots, n-1\}$.

#### [MAJOR-10-2] Emphatic Exclamation Marks `!` Inside Display Math `$$...$$` Rendering as Factorials in `Ch 10`
- **Location**: Lines 166 (`= 0!`), 351 (`\pmod{x^{2d}}!`), 393 (`\pmod{x^{2d}}!`), 429 (`\pmod{x^4}!`), 966 (`= \Phi(u)!`), 1150 (`\Big)!`), 1268 (`\Big)!`).
- **What Is Wrong**: In line 166, `= 0!` literally renders as $0! = 1$ inside the verification of the Newton step!
- **Concrete Fix**: Remove the trailing `!` from inside `$$...$$` on all 7 lines.

#### [MINOR-10-1] Base-Case Convention Mismatch on `UOJ 50` Between `Ch 09` and `Ch 10` (Lines 196, 233, 268)
- **Location**: Lines 196, 233, 268.
- **What Is Wrong**: In `Ch 09` (`Mas-1`, lines 1147 & 1181), `UOJ 50` has base case $F(0) = 0$ ($f_0 = 0$, since a tree has at least $1$ vertex), whereas `Ch 10` §10.1 (lines 196, 233, 268) writes $F(0) = 1$ for `UOJ 50`.
- **Concrete Fix**: Add a short parenthetical at line 196 noting that in `UOJ 50` $F(0) = 0$ (or $F(0) = c_0$ in general initial-value problems $F' = \frac{1}{2}AF^2 + 1$), or align the trace to $F(0) = 0$ so the reader does not get confused comparing §10.1 with `Ch 09 Mas-1`.

#### [MINOR-10-2] Conversational `"Wait:"` Prompt in `Adv-1 (#179) Luogu P5597` (Line 987)
- **Location**: Line 987 (`"Wait: why isn't $T_\infty$ infinite in size?"`).
- **Concrete Fix**: Replace `"Wait: why isn't $T_\infty$ infinite in size?"` with `"Why is $T_\infty$ finite in size?"`.

---

### 3. `chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd`

#### [CRITICAL-11-1] Mathematical Sign Error in `Mas-1 (#114) CF 1349F2 — Slime and Sequences (Hard Version)` (Lines 1526–1540) + Raw Trial-and-Error Monologue (Lines 1465–1525)
- **Location**: Lines 1465–1540.
- **What Is Wrong (Mathematical Proof of Sign Error)**:
  - In Step 4 (lines 1505–1524), the author decomposes $c_j = [w^j] \Phi(w)^{n+1} = \text{Term}_1(j) - \text{Term}_2(j)$, where
    $$\text{Term}_2(j) = \operatorname{Res}_{z=0} \frac{Q(z)}{(1 + z)\big(Q(z) - 1\big)} \frac{dz}{\big(\ln(1 + z)\big)^{j+1}}, \qquad Q(z) = \frac{z}{\ln(1 + z)}.$$
  - At line 1526, the author changes variables back to $w = \ln(1 + z) \iff z = e^w - 1$, where $dz = e^w\,dw = (1 + z)\,dw$ and $Q(z) = \frac{e^w - 1}{w}$.
  - Let us compute $\frac{Q(z)}{Q(z) - 1}$ in terms of $w$:
    $$\frac{Q(z)}{Q(z) - 1} = \frac{\frac{e^w - 1}{w}}{\frac{e^w - 1}{w} - 1} = \frac{e^w - 1}{e^w - 1 - w} = -\frac{e^w - 1}{w + 1 - e^w}.$$
  - However, at **line 1528**, the author writes:
    $$\text{Term}_2(j) = \operatorname{Res}_{w=0} \frac{1}{w^{j+1}\left(\frac{w}{e^w - 1} - 1\right)}\,dw = [w^j] \frac{e^w - 1}{w + 1 - e^w},$$
    confusing $\frac{Q}{Q - 1} = \frac{1}{1 - Q^{-1}}$ with $\frac{1}{Q^{-1} - 1} = -\frac{Q}{Q - 1}$ and **dropping the minus sign**!
  - **Concrete Numerical Counterexample ($n = 1, j = 0$)**:
    - Since $\Phi(w) = 1 + \frac{1}{2}w + \dots$, at $n = 1, j = 0$ we must have $c_0 = [w^0] \Phi(w)^1 = \mathbf{1}$.
    - Using the textbook's formula for $\text{Term}_1(0)$ at $n = 1$ (line 1517):
      $$Q(z) = 1 + \frac{1}{2}z - \frac{1}{12}z^2 + \dots, \quad R(z) = \frac{Q(z) - 1}{z/2} = 1 - \frac{1}{6}z + \dots$$
      $$\text{Term}_1(0) = \frac{2}{1} [z^1] \frac{Q(z)^3}{(1 + z) R(z)} = 2 [z^1] \left(1 + \left(\frac{3}{2} - 1 + \frac{1}{6}\right) z\right) = 2 \cdot \frac{2}{3} = \frac{4}{3}.$$
    - For $\text{Term}_2(0)$, the true integral gives
      $$\text{Term}_2(0) = [w^0] \frac{e^w - 1}{e^w - 1 - w} = [w^1] \frac{1 + \frac{1}{2}w + \dots}{\frac{1}{2} + \frac{1}{6}w + \dots} = 2 \left(\frac{1}{2} - \frac{1}{3}\right) = +\frac{1}{3},$$
      so $c_0 = \text{Term}_1(0) - \text{Term}_2(0) = \frac{4}{3} - \frac{1}{3} = \mathbf{1}$ (correct!).
    - In contrast, the textbook's formula at lines 1528, 1532, 1536, and 1540 has $w + 1 - e^w = -\frac{1}{2}w^2 - \frac{1}{6}w^3 - \dots$ in the denominator, which gives $\text{Term}_2(0) = -\frac{1}{3}$ and $c_0 = \frac{4}{3} - \left(-\frac{1}{3}\right) = \frac{5}{3} \neq 1$!
  - Furthermore, lines 1465–1525 contain raw exploratory stream-of-consciousness (`"? No, v and x are coupled!"`, `"Wait—in that direction, x appears inside..."`, `"BINGO!"`, `"wait: in the residue..."`, `"Wait: why did Q(z)^{j+2} appear?"`).
- **Concrete Fix**:
  1. In lines 1528, 1530, 1532, 1536, and 1540, replace $w + 1 - e^w$ with $e^w - 1 - w$ (which has positive leading term $+\frac{1}{2}w^2 + \frac{1}{6}w^3 + \dots$, making $\frac{e^w - 1 - w}{w^2} = \sum_{k \ge 0} \frac{w^k}{(k+2)!}$ have constant term $+\frac{1}{2}$!).
  2. Streamline lines 1465–1525 so that the substitution $t = \Phi(w) - 1 \iff e^w - 1 = w(1 + t)$ and the second substitution $z = e^w - 1 = w(1 + t)$ are motivated directly without false starts or `"BINGO!"` / `"Wait:"` monologues.

#### [MAJOR-11-1] Wrong Chapter Number Cross-References (`Chapter 7` Instead of `Chapter 10` for Newton's Method)
- **Location**: Lines 6, 950, 1550, 1584, and 1613.
- **What Is Wrong**:
  - All five lines refer to Newton's method on implicit equations as **Chapter 7** (e.g., line 6: `"In Chapters 3 through 7, our standard workflow for an implicit combinatorial equation F(x) = x\Phi(F(x)) was to... run Newton's method"`; line 950: `"Newton (Ch 7)"`; line 1550: `"Chapter 7 (Newton's method)"`; line 1584: `"Newton's method (Chapter 7)"`; line 1613: `"Newton's Method (Chapter 7)"`).
  - In the canonical 24-chapter architecture (`CURRICULUM_ARCHITECTURE.md`), Chapter 7 is Point-Value Duality, Roots-of-Unity Filters & Chirp-$z$, whereas Implicit Functional Equations & Newton's Method is **Chapter 10**!
- **Concrete Fix**: Change `"Chapter 7"` / `"Ch 7"` to `"Chapter 10"` / `"Ch 10"` in lines 6, 950, 1550, 1584, and 1613.

#### [MAJOR-11-2] Emphatic Exclamation Marks `!` Inside Display Math `$$...$$` Rendering as Factorials in `Ch 11`
- **Location**: Lines 488, 525 (`\binom{tn + r}{n}!`), 690 (`\pmod p!`), 712 (`\pmod p!`), 729 (`= D!`), 932, 1070 (`\pmod{998244353}!`), 1263 (`\phi_2(u_1)^M!`), 1371 (`Y(w)^{-1}!`), 1477, 1482 (`dw!`), 1493, 1507 (`= 1!`), 1528, 1532, 1536.
- **What Is Wrong**: Line 525 renders $\binom{tn+r}{n}!$ (looks like the factorial of a binomial coefficient!), line 729 renders $= D!$ (looks like $D$ factorial!), and line 1507 renders $= 1!$.
- **Concrete Fix**: Remove all trailing `!` from inside `$$...$$` on these 16 lines.

#### [MINOR-11-1] Raw Draft Self-Corrections (`"Wait..."`) and Typo in `Int-1 (#196)`, `Int-2 (#201)`, `Adv-2 (#229)`, and `Mas-1 (#114)`
- **Location**:
  1. Lines 1047–1057 (`Int-1 Luogu P6672`): Contains two raw self-interruptions (`"the fraction ... is 1/(m-n+1)? *Wait—be careful with what the problem states!*"`, `"Wait: why is (0, 2) invalid? ... —Wait: for (2, 0)..."`).
  2. Line 1162 (`Int-2 Luogu P7439`): `"Wait: even simpler..."`.
  3. Line 1304 (`Adv-2 LOJ 6703`): Missing space before `Wait:` (`\bigr)$.Wait: $n$ is **fixed** here!`).
  4. Line 1417 (`Mas-1 CF 1349F2`): `"... ? Wait: more directly, ..."`.
- **Concrete Fix**: Rewrite these transitions directly without `"Wait:"` self-questioning.

---

### 4. `chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`

- **Audit Result**: **ZERO ISSUES FOUND**.
- Every formula, base case ($n = 1, 2, 3, 4, 5$), sign, valuation precondition, failure mode, and 8-problem ladder derivation (`#176`, `#245`, `#146`, `#227`, `#228`, `#016`, `#183`, `#184`) was verified line by line and is 100% mathematically accurate, self-contained, and free of formatting defects.

---

### 5. `chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd`

#### [MAJOR-13-1] Broken Internal `.qmd` Links & Outdated Chapter Number Cross-References
- **Location**: Lines 5, 27, 28, 29, 30, 333, 669, 685, 820, 915, 1525.
- **What Is Wrong**:
  1. **Broken Link to Chapter 12 (Lines 5 and 27)**:
     - Links to `[Chapter 12](ch12-pointed-trees-cacti-block-cut-tutte.qmd)`, which does not exist! The actual filename is `ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`.
  2. **Broken Link & Wrong Title for Chapter 14 (Line 1525)**:
     - Line 1525 writes: `Before moving to [Chapter 14](ch14-stirling-eulerian-bernoulli-poly-interp.qmd)...`
     - In our 24-chapter textbook (`CURRICULUM_ARCHITECTURE.md`), Chapter 14 is **Probabilistic Generating Functions, Renewal & Martingales** (and it is separated from Chapter 13 by `checkpoints/cp03-part3-online-implicit-lif-graphs.qmd`).
  3. **Verify Chapter 6, 7, 8, 24 Link Filenames (Lines 13, 28, 29, 30, 333, 669, 685, 820, 915)**:
     - Ensure that the relative `.qmd` links for `Ch 06`, `Ch 07`, `Ch 08`, and `Ch 24` match the exact filenames in `chapters/` (and point line 1525 to `[Checkpoint III](../checkpoints/cp03-part3-online-implicit-lif-graphs.qmd)` or the exact `ch14` filename).
- **Mathematical Audit Result for `Ch 13`**: **100% Clean**. All derivations and hand-traces in §13.1–§13.5 are mathematically exact and contain zero magic steps.

---

### 6. `checkpoints/cp03-part3-online-implicit-lif-graphs.qmd`

#### [MINOR-CP03-1] Single Conversational `"Wait —"` in `CP-III.7 (#205 Luogu P8555)` Failure Mode Box (Line 1161)
- **Location**: Line 1161.
- **What Is Wrong**:
  - Line 1161 writes: `"...or even simpler: apply the P-recursive differential recurrence for $P(u) = \Phi(u)^{m_0}$ only within degree $< p$? Wait — in $\mathbb{F}_p[u]$, binary exponentiation of $\Phi(u)$ using polynomial multiplication uses **zero divisions** and runs in $O(d p \log(dp))$ time per digit!"`
  - Suggesting the P-recursive ODE (which is a `Ch 18` topic and fails at degree $\ge p$ anyway) and then retracting it with `"Wait —"` is unnecessary.
- **Concrete Fix**:
  - Replace line 1161 with:
    `- **Remedy**: Because $\deg \Phi = d \le 5$ is tiny and $m_0 < p$, compute $\Phi(u)^{m_0} \bmod p$ directly via binary exponentiation using division-free polynomial multiplication (either $O(d^2 p^2)$ schoolbook multiplication for $d \le 5$ or 64-bit NTT convolution followed by reduction $\bmod\, p$ in $O(d p \log(dp))$ time per base-$p$ digit), which requires **zero divisions**!`
- **Stage 1 Spoiler-Free & Mathematical Audit Result for `CP-III`**: **100% Pass**. All 8 problems (`#090`, `#131`, `#133`, `#160`, `#119`, `#035`, `#205`, `#163`) match `CURRICULUM_ARCHITECTURE.md`, Stage 1 is 100% spoiler-free, and every Stage 2 derivation and trace is mathematically verified.
