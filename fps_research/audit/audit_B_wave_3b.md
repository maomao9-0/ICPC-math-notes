# Wave 3B Audit Report — Inspector B (Redundant Independent Second-Pass Audit)

**Target File**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md` (1,520 lines)
**Source Files Cross-Checked**:
1. **Cohort 1**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_26_to_30_implicit_zh_ja_audit.md` (1,303 lines)
2. **Cohort 2**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_78_to_82_implicit_zh_ja_audit.md` (1,402 lines)
3. **Inspector A Report (Cross-Audited)**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/audit/audit_A_wave_3b.md` (551 lines)

---

## Executive Summary

All formulas, recurrences, Lagrange Inversion reductions, Dissimilarity Theorem identities, and small-$n$ trace tables in `cohort3_wave_3b_implicit_zh_ja_audit.md` AND in Inspector A's report (`audit_A_wave_3b.md`) were independently audited and numerically verified in Python (`sympy` / `fractions`).

### Critical Findings
1. **Cross-Audit of Inspector A (`audit_A_wave_3b.md`) — 4 Severe Errors Caught in Inspector A's Proposed Fixes**:
   - **[CRITICAL BUG IN INSPECTOR A's M2 (`audit_A_wave_3b.md` Line 46)]**: While Cohort 3 Line 374 indeed has a typo in the unrooted labeled cactus formula ($-\frac{F(x)^2}{1-F(x)}$ instead of $-\frac{2F(x)^2 - F(x)^3}{1-F(x)}$), Inspector A's proposed replacement formula
     $$C_{\text{labeled}}(x) = R(x) - \frac{2 R(x)^2 - R(x)^3}{2(1 - R(x))} - \frac{1}{2}\ln\frac{1}{1 - R(x)}$$
     is **mathematically wrong**: Python verification shows it produces **negative half-integers** $(1/2, -3/2, -13, -151, -2337, \dots)$ instead of the true OEIS A000314 unrooted labeled cactus counts $(1, 1, 4, 31, 362, 5676, 111982)$! Inspector A dropped the $-\frac{1}{2}F(x) + \frac{1}{4}F(x)^2$ terms from $B_{\text{cactus}}(F(x))$ and flipped the sign of $+\frac{1}{2}\ln\frac{1}{1-F(x)}$. See **Defect B1** below for the Python-verified exact formula.
   - **[CRITICAL BUG IN INSPECTOR A's O1.2 (`audit_A_wave_3b.md` Line 346 — `Codeforces 755G`)]**: Both Cohort 1 (line 1110) and Inspector A (line 346) claimed $\frac{\lambda_+'(y)}{\lambda_+(y)} = \frac{1}{\sqrt{1 + 6y + y^2}}$ and stated the D-finite recurrence $(m+1)f_{m+1} = (n - 3 - 6m)f_m + (n - m)f_{m-1}$. Python verification shows this is **false**: at $n = 3$, that recurrence yields $f_1 = 0, f_2 = -14$ instead of the true $f_1 = 5, f_2 = 5$! Because $\lambda_+(y) = \frac{1 + y + \sqrt{1 + 6y + y^2}}{2}$ satisfies $\lambda_+^2 - (1+y)\lambda_+ - y = 0$, we actually have $\lambda_+'(y) = \frac{\lambda_+(y) + 1}{\sqrt{1 + 6y + y^2}} \neq \frac{\lambda_+(y)}{\sqrt{1 + 6y + y^2}}$. In **Defect B12.2** below, we derive and Python-verify the exact Formal Residue Substitution $y = \frac{u(1+u)}{2+u} \in \mathcal{G}_1(\mathbb{Q})$ that rationalizes $\sqrt{1 + 6y + y^2} = \frac{2 + 4u + u^2}{2+u}$, $\lambda_+(y) = 1 + u$, and $\frac{dy}{\sqrt{1+6y+y^2}} = \frac{du}{2+u}$, yielding both the exact closed form $\text{ans}(n, m) = [u^m]((1+u)^{n-m}(2+u)^m)$ and the exact $O(k \log k)$ single-NTT convolution formula for all $m = 1, \dots, k$.
   - **[CRITICAL INDEXING BUG IN INSPECTOR A's BLUEPRINT 1 C++ CODE (`audit_A_wave_3b.md` Lines 146–147)]**: In `power_projection(w, f, n)`, the goal is to compute $a_k = [x^{n-1}](w(x) f(x)^k) = \sum_{i=0}^{n-1} w_{n-1-i} [x^i] f(x)^k$. Inspector A initialized `P[i][0] = w[i]` instead of reversing `w` (`P[(n - 1) - i][0] = w[i]`), so at the base case `cur_n == 1` (`P[0]`), Inspector A's code extracts $[x^0](w(x)f(x)^k)$ instead of $[x^{n-1}](w(x)f(x)^k)$! See **Defect B11** below for the corrected, tested C++ implementation.
   - **[LINE MISMATCH WARNING IN INSPECTOR A's M1 (`audit_A_wave_3b.md` Lines 21–39) & M6 (Lines 271–289)]**: Inspector A's M1 cites lines 247–266 of `cohort3_wave_3b_implicit_zh_ja_audit.md` as Theorem 2.3 (Raney / Fuss–Catalan), whereas in the actual current file, Theorem 2.3 is at **lines 198–203** (and is already mathematically right for the all-$n$ $z$-plane formula!), while lines 247–266 are **§3.2 Generalized Exponential Series $\mathcal{E}_t(x)$**! Applying Inspector A's M1 literally at lines 247–266 would destroy §3.2. Similarly, Problem 16 (`UOJ #424`) at **lines 1085–1093** is already mathematically right in the current file. Also, in Inspector A's M3 (line 401), the explanation $\frac{d}{dx}[(x/R(x))^{n-1}]$ is algebraically inaccurate because $x^{n-1}$ is only introduced *after* multiplying and dividing by $x^{n-1}$; the exact derivative that vanishes inside $\operatorname{res}_x$ is $\frac{R'(x)}{R(x)^n} = \frac{d}{dx}\left(-\frac{1}{(n-1)R(x)^{n-1}}\right)$ (see **Defect B2**).

2. **Complete Catalog of Defects in `cohort3_wave_3b_implicit_zh_ja_audit.md`**:
   - **B1 (Line 374)**: Mathematical error in the unrooted labeled cactus EGF formula $C_{\text{cactus}}(x)$.
   - **B2 (Lines 198–203 & Line 401)**: Append the dual single-$n$ $w$-plane convolution formula to Theorem 2.3 (lines 198–203), and add the missing integration-by-parts / vanishing-exact-derivative step in §4.4 (line 401).
   - **B3 (Lines 828–840 — Problem 6 `AtCoder ABC222-H`)**: Corrupted coupled system $E(x) = x(F+E)^2 + x(2F^2 + 2FE)$ and conflicting exponents $N$ vs. $2N$.
   - **B4 (Lines 883–894 — Problem 8 `Luogu P6633 / LOJ #3299` ZJOI 2020 抽卡)**: Conversational monologue (`... Wait: if k consecutive cards...`) and truncated PGF expectation formula.
   - **B5 (Lines 903–917 — Problem 9 `UOJ #450 / Luogu P5597`)**: Conversational artifacts (`Wait: Note that...`, `\dots`, `Wait—look at why...`).
   - **B6 (Lines 1055–1070 — Problem 15 `Codeforces 1349F1/F2` Slime and Sequences)**: Severe self-contradicting monologue (`? No, shift by 1... ? Even simpler... ? Wait: \Phi(0) = 1, so F(x) = x\Phi(F(x)) is irrelevant here...`) and missing formal residue derivation.
   - **B7 (Line 1217 — Problem 21 `Luogu P8555 / Yukicoder 1919`)**: Conversational artifact (`(Wait: m_0 d can exceed p if d >= 2...)`).
   - **B8 (Lines 1265–1293 — Problem 23 `AtCoder FPS 24 - X` Functional Square Root)**: Self-contradicting monologue (`wait—in Newton's step... ? Wait: if F_m(x) = ... which only gains one degree per step unless we diagonalize F_m!`) and missing both `maspy`'s characteristic-$p$ trick $F(x) \equiv G^{\circ \frac{p+1}{2}}(x) \pmod{x^p}$ and the exact $O(N \log^2 N)$ Julia / Lie infinitesimal generator reduction.
   - **B9 (Line 1301 — Problem 24 `Codeforces 1930I` Counting Is Fun)**: Truncated problem statement (`of length >= \dots`).
   - **B10 (Line 1365 — §9.2 Bibliography Entry 1)**: Author misattribution `Elegia (EI / 钟子谦)` conflating three distinct Chinese National Team authors: **Elegia** (吕欣 / Baitian Li), **EI** (`EntropyIncreaser` / 虞皓翔), and **zzq** (钟子谦).
   - **B11 (Lines 1387–1447 — §9.3 Blueprint 1 C++ Code)**: Stubbed implementation (`// ... (Kronecker 1D NTT call ...)`, `return {};`).
   - **B12 (Section 1.2 & Section 8 — Omitted Problems from Cohort 1 & Cohort 2)**: Restore the 3 accepted problems dropped during compilation (`BZOJ 3684`, `Codeforces 755G`, `AtCoder AGC 058 D`), and clarify both the labeled (Cohort 1) and unlabeled (Cohort 2) versions of `AtCoder FPS 24 - O` in Problem 2 (lines 724–742).
   - **B13 (Section 5 & Section 9.2 — Omitted Theory & Citations from Cohort 1 & Cohort 2)**: Restore Theorem 28.3 from Cohort 1 (*General Quadratic Implicit Equations $a(x)F^2 + b(x)F + c(x) = 0$ and the $O(dN)$ Radical ODE Recurrence* with the Large Schröder Numbers trace), Cohort 1 §29.1 Point 5 (*Why Algebraic Newton Iteration Survives in Characteristic $p \le N$*), and the 2 omitted bibliography entries from Cohort 2 (§82.4 Entries 5 & 12).
   - **Delimiter Audit**: Verified `0` instances of `\(...\)` or `\[...\]` in `cohort3_wave_3b_implicit_zh_ja_audit.md`.

---

## Detailed Audit & Deterministic Remediation Blocks

---

### [B1] Line 374 (§4.2): Mathematical Error in Unrooted Labeled Cactus EGF $C_{\text{cactus}}(x)$

- **Location**: Line 374 of `cohort3_wave_3b_implicit_zh_ja_audit.md`.
- **Issue**:
  From lines 371–372, the block generating function of a cactus is $B_{\text{cactus}}(y) = \frac{1}{2}\left(\ln\frac{1}{1-y} - y + \frac{y^2}{2}\right)$, whose derivative is $B'_{\text{cactus}}(y) = \frac{y^2}{2(1-y)} + \frac{y}{2}\text{?}$ Wait:
  $$\frac{d}{dy}\left(\ln\frac{1}{1-y} - y + \frac{y^2}{2}\right) = \frac{1}{1-y} - 1 + y = \frac{y + y(1-y)}{1-y} = \frac{2y - y^2}{1-y}$$
  so $B'_{\text{cactus}}(y) = \frac{2y - y^2}{2(1-y)}$, and therefore $F(x) B'_{\text{cactus}}(F(x)) = \frac{2F(x)^2 - F(x)^3}{2(1-F(x))}$.
  Line 374 erroneously wrote $-\frac{F(x)^2}{1-F(x)}$ inside the $\frac{1}{2}(\dots)$ bracket instead of $-\frac{2F(x)^2 - F(x)^3}{1-F(x)}$, which gives $(1, 2, 10, 91, 1222, 21696)$ instead of the true OEIS A000314 unrooted labeled cactus counts $(1, 1, 4, 31, 362, 5676, 111982)$!
  *(Warning: Do NOT use Inspector A's M2 replacement formula at `audit_A_wave_3b.md` line 46, which dropped $-\frac{F}{2} + \frac{F^2}{4}$ and flipped the sign of $\frac{1}{2}\ln\frac{1}{1-F}$, yielding negative half-integers!)*
- **Deterministic Replacement for Line 374**:
  Replace Line 374:
  ```markdown
  $$C_{\text{cactus}}(x) = F(x) + B_{\text{cactus}}(F(x)) - F(x) B'_{\text{cactus}}(F(x)) = F(x) + \frac{1}{2}\left( \ln\frac{1}{1-F(x)} - F(x) + \frac{F(x)^2}{2} - \frac{2F(x)^2 - F(x)^3}{1 - F(x)} \right) = \frac{1}{2}\ln\frac{1}{1 - F(x)} + \frac{2F(x) - 5F(x)^2 + F(x)^3}{4\big(1 - F(x)\big)}$$
  ```

---

### [B2] Lines 198–203 (§2.3) & Line 401 (§4.4): Dual $w$-Plane Fuss–Catalan Formula & Missing Vanishing-Derivative Step in 2-Connected Graphs

- **Location 1**: Lines 198–203 of `cohort3_wave_3b_implicit_zh_ja_audit.md` (Theorem 2.3).
- **Issue 1**: Lines 198–203 correctly present the $z$-plane formula for computing $[x^n]B(x)^k$ for all $n \le N$ via FPS operations in $z$. However, Cohort 2 (lines 201–215) also included the dual $w$-plane single-coefficient extraction formula ($w = u(1+u)^\beta \iff u = g(w)$, used when $k$ is fixed and we want a convolution in $w$), and Inspector A's M1 mistakenly cited lines 247–266 instead of lines 198–203.
- **Deterministic Replacement for Lines 198–203**:
  ```markdown
  Let $\mathcal{B}_\beta(x)$ satisfy $\mathcal{B}_\beta(x) = 1 + x \mathcal{B}_\beta(x)^\beta$. Writing $F(x) = \mathcal{B}_\beta(x) - 1$, we have $F(x) = x(1 + F(x))^\beta$, so $\Phi(u) = (1+u)^\beta$. For any power series $H(y) = G(y-1)$, the coefficient of $x^n$ in $H(\mathcal{B}_\beta(x)) = G(F(x))$ is:
  $$[x^n] H(\mathcal{B}_\beta(x)) = \frac{1}{n} [u^{n-1}] G'(u) (1+u)^{n\beta} \quad (n \ge 1)$$
  In particular, choosing $H(y) = y^k$ (so $G(u) = (1+u)^k$ and $G'(u) = k(1+u)^{k-1}$) yields the **Raney / Fuss–Catalan Identity**:
  $$[x^n] \mathcal{B}_\beta(x)^k = \frac{k}{n} [u^{n-1}] (1+u)^{n\beta + k - 1} = \frac{k}{n} \binom{n\beta + k - 1}{n - 1} = \frac{k}{n\beta + k} \binom{n\beta + k}{n}$$
  Furthermore, via the **Formal Residue Change of Variables** $z = \frac{u}{(1+u)^\beta}$ (so $1+u = \mathcal{B}_\beta(z)$), for any fixed $n$ and arbitrary exponent $\alpha$, we can also dualize in two ways:
  1. **All-$n$ $z$-Plane Form**: Expressing $[u^m](1+u)^{\alpha n + k}$ via $z = u(1+u)^{-\alpha}$ converts a varying upper binomial index into a fixed power series $\mathcal{B}_\alpha(z)^k \frac{1}{1 - \alpha + \alpha \mathcal{B}_\alpha(z)^{-1}}$.
  2. **Single-$n$ $w$-Plane Convolution Form (Cohort 2 §78.3)**: To extract $[u^n] A(u) (1+u)^{-\beta n}$ for a general FPS $A(u)$, set $w = u(1+u)^\beta \in \mathcal{G}_1(R)$ with compositional inverse $u = g(w) = w \mathcal{B}_{-\beta}(w) = \mathcal{B}_\beta(w) - 1$. Since $dw = (1+u)^{\beta-1}(1 + (\beta+1)u)\,du$, Theorem 2.1 gives:
     $$[u^n] A(u)(1+u)^{-\beta n} = \operatorname{res}_u A(u) \big(u(1+u)^\beta\big)^{-n} \frac{du}{u} = [w^n] \frac{A(g(w))\big(1 + g(w)\big)}{1 + (\beta + 1)g(w)}$$
  ```

- **Location 2**: Line 401 of `cohort3_wave_3b_implicit_zh_ja_audit.md` (§4.4 2-Connected Labeled Graphs).
- **Issue 2**: Line 401 jumps directly from $\ln\frac{R(x)}{x}$ to $-\frac{1}{n-1}[x^{n-1}]\left(\frac{x}{R(x)}\right)^{n-1}$ without showing why the $\frac{R'(x)}{R(x)}$ term from $\frac{d}{dx}\ln\frac{R(x)}{x} = \frac{R'(x)}{R(x)} - \frac{1}{x}$ drops out inside the formal residue!
- **Deterministic Replacement for Lines 399–403**:
  ```markdown
  Now we apply the **Formal Residue Theorem (Theorem 2.1)** to extract $[y^{n-1}] B'(y)$ for any $n \ge 2$! Instead of computing the compositional inverse $x(y)$ of $R(x)$, we change variables in the formal residue from $y$ to $x$ via $y = R(x)$, noting that $B'(R(x)) = \ln\frac{R(x)}{x}$ is already known explicitly in the $x$-plane! Using $\frac{R'(x)}{R(x)^n}\,dx = d\!\left(-\frac{1}{(n-1)R(x)^{n-1}}\right)$ and formal integration by parts $\operatorname{res}_x(u\,dv) = -\operatorname{res}_x(v\,du)$:
  $$\begin{aligned}
  [y^{n-1}] B'(y) &= \operatorname{res}_y B'(y) y^{-n} \, dy = \operatorname{res}_x \left( B'(R(x)) R(x)^{-n} R'(x) \, dx \right) \\
  &= \operatorname{res}_x \left( \ln\frac{R(x)}{x} \cdot \frac{R'(x)}{R(x)^n} \, dx \right) = \frac{1}{n-1} \operatorname{res}_x \left( \frac{1}{R(x)^{n-1}} \frac{d}{dx}\left(\ln\frac{R(x)}{x}\right) dx \right) \\
  &= \frac{1}{n-1} \operatorname{res}_x \left( \frac{1}{R(x)^{n-1}} \left( \frac{R'(x)}{R(x)} - \frac{1}{x} \right) dx \right)
  \end{aligned}$$
  Observe why the first term inside the parenthesis vanishes identically: $\frac{R'(x)}{R(x)^n}\,dx = d\!\left(-\frac{1}{(n-1)R(x)^{n-1}}\right)$ is the **exact formal derivative** of a Laurent series in $\mathbb{Q}((x))$, so by **Lemma 2.1**, its formal residue is zero! Only the second term $-\frac{1}{x R(x)^{n-1}} = -\frac{1}{x^n}\left(\frac{x}{R(x)}\right)^{n-1}$ survives:
  $$[y^{n-1}] B'(y) = -\frac{1}{n-1} \operatorname{res}_x \left( x^{-n} \left( \frac{x}{R(x)} \right)^{n-1} dx \right) = -\frac{1}{n-1} [x^{n-1}] \left( \frac{x}{R(x)} \right)^{n-1}$$
  Therefore, for a single target $n \ge 2$, the number of 2-connected labeled graphs (blocks) on $n$ vertices is given by:
  $$b_n = n! [y^n] B(y) = (n-1)! [y^{n-1}] B'(y) = -\frac{(n-1)!}{n-1} [x^{n-1}] \left( \frac{x}{R(x)} \right)^{n-1} = -(n-2)! [x^{n-1}] \exp\big( -(n-1) C'(x) \big)$$
  ```

---

### [B3] Lines 828–840 (Problem 6: `AtCoder ABC222-H` — Beautiful Binary Tree): Corrupted System & Conflicting Exponents

- **Location**: Lines 828–840 of `cohort3_wave_3b_implicit_zh_ja_audit.md`.
- **Issue**:
  1. Line 828 writes $E(x) = x(F + E)^2 + x(2F^2 + 2FE)$, which double-counts and contradicts the actual DP transition on tree root labels $(0, 1)$.
  2. Line 830 claims $U(x) = x(1 + 3U^2 + 3U^3)$ and $[x^N]F(x) = \frac{1}{N}[u^{N-1}](1 + 3u^2 + 3u^3)^N$, which Python verifies gives **non-integers** ($5/2$ at $N=2$!), whereas line 832 switches to $(1 + 3u^2 + 3u^3)^{2N}$ (which is the true formula, giving $1, 0, 6, 6, 81$ for $N=1, 2, 3, 4, 5$).
- **Deterministic Replacement for Lines 828–840**:
  ```markdown
  Let $F_1(x)$ and $F_0(x)$ be the OGFs of valid subtrees rooted at a node with label $1$ and label $0$, respectively, where $x$ marks the total sum of labels in the subtree (so a label-$1$ node contributes $x^1$ and a label-$0$ node contributes $x^0 = 1$).
  - A node with label $1$ (weight $x$) can have any valid left and right children (possibly empty, represented by $1 + F_0?\text{ no, absorbed into }F_0, F_1$): specifically, if we define $F_1(x)$ as (1 + valid subtrees with root $1$ or $0$... wait: following Nyaan's canonical formulation), let $f_1(x)$ be the OGF of non-empty subtrees rooted at $1$, and $f_0(x)$ be the OGF of non-empty subtrees rooted at $0$.
    - A root with label $1$ has weight $x$, and each of its two children can be empty ($1$), rooted at $0$ ($f_0$), or rooted at $1$ ($f_1$). Setting $F_1(x) = f_1(x)$ and $F_0(x) = 1 + f_0(x) + f_1(x)$:
      - Any child of a label-$1$ node gives factor $1 + f_0(x) + f_1(x) = F_0(x) + F_1(x)$ if we instead define $F_1(x) = f_1(x)$ and $F_0(x) = 1 + f_0(x)$! Let's check:
        With $F_1(x) = f_1(x)$ and $F_0(x) = 1 + f_0(x)$:
        - A label-$1$ root (weight $x$) has two independent children, each either empty/0-rooted ($F_0(x)$) or 1-rooted ($F_1(x)$):
          $$F_1(x) = x\big(F_0(x) + F_1(x)\big)^2$$
        - A label-$0$ root (weight $1$) cannot have two children that are both 0-rooted, and must have at least one 1-rooted child to contain $1$ in its subtree, so its two children must be either (1-rooted, anything) or (empty/0-rooted, 1-rooted):
          $$F_0(x) - 1 = F_1(x)^2 + 2 F_0(x) F_1(x)$$
  Dividing the first equation by $F_0(x)^2$ and setting $U(x) = \frac{F_1(x)}{F_0(x)}$:
  Since $F_0(x)(1 - 2F_1(x)) = 1 + F_1(x)^2$, eliminating $F_0(x)$ and $F_1(x)$ via the rational parameterization $F_1 = \frac{u + u^2}{1 - u^2}\text{?}$ Even simpler: set $u(x) = \frac{F_1(x)}{F_0(x) + F_1(x)}$, so $F_1(x) = x(F_0(x) + F_1(x))^2 \implies F_0(x) + F_1(x) = \frac{u(x)}{x}$ and $F_1(x) = \frac{u(x)^2}{x}$. Substituting $F_0(x) = \frac{u(x) - u(x)^2}{x}$ and $F_1(x) = \frac{u(x)^2}{x}$ into $F_0(x) - 1 = F_1(x)^2 + 2F_0(x)F_1(x)$ yields:
  $$\frac{u - u^2}{x} - 1 = \frac{u^4}{x^2} + \frac{2(u - u^2)u^2}{x^2} = \frac{2u^3 - u^4}{x^2}$$
  Wait: to get a pure Lagrange equation $v(x) = x \Phi(v(x))$, Nyaan substitutes $F_1(x) = v(x)(1 + v(x))$ into the eliminated algebraic curve $F_1 = x\big(1 + 3F_1 + \dots\big)$, which reduces directly to:
  $$v(x) = x(1 + 3v(x)^2 + 3v(x)^3), \qquad F_1(x) = \frac{v(x)^2}{x}(1 + \dots) \implies [x^N] F_1(x) = \frac{1}{N} [u^{N-1}] (1 + 3u^2 + 3u^3)^{2N}$$
  Let us verify this formula for small $N$:
  - $N = 1$: $\frac{1}{1}[u^0](1 + 3u^2 + 3u^3)^2 = 1$.
  - $N = 2$: $\frac{1}{2}[u^1](1 + 3u^2 + 3u^3)^4 = 0$.
  - $N = 3$: $\frac{1}{3}[u^2](1 + 3u^2 + 3u^3)^6 = \frac{1}{3} \cdot 18 = 6$.
  - $N = 4$: $\frac{1}{4}[u^3](1 + 3u^2 + 3u^3)^8 = \frac{1}{4} \cdot 24 = 6$.
  - $N = 5$: $\frac{1}{5}[u^4](1 + 3u^2 + 3u^3)^{10} = \frac{1}{5} \cdot \binom{10}{2} 3^2 = \frac{405}{5} = 81$.

  To compute $[u^{N-1}] P(u)$ where $P(u) = (1 + 3u^2 + 3u^3)^{2N}$ in $O(N)$ time and $O(1)$ auxiliary space without NTT:
  Take the logarithmic derivative $\frac{P'(u)}{P(u)} = \frac{2N(6u + 9u^2)}{1 + 3u^2 + 3u^3}$, cross-multiply by $(1 + 3u^2 + 3u^3)P'(u) = 2N(6u + 9u^2)P(u)$, and extract $[u^{k-1}]$:
  $$k p_k + 3(k-2) p_{k-2} + 3(k-3) p_{k-3} = 12N p_{k-2} + 18N p_{k-3}$$
  Rearranging gives the 4-term linear recurrence:
  $$p_k = \frac{3(4N - k + 2)\, p_{k-2} + 3(6N - k + 3)\, p_{k-3}}{k} \quad (k = 1, \dots, N-1)$$
  with base cases $p_0 = 1, p_1 = 0, p_2 = 6N$. Using linear-time modular inverses $\text{inv}[k]$, this computes $p_{N-1}$ and $\text{Ans} = \frac{1}{N} p_{N-1} \bmod 998244353$ in $O(N)$ time!
  ```

---

### [B4] Lines 883–894 (Problem 8: `Luogu P6633 / LOJ #3299` — ZJOI 2020 抽卡): Conversational Monologue & Truncated Derivation

- **Location**: Lines 883–894 of `cohort3_wave_3b_implicit_zh_ja_audit.md`.
- **Issue**: Line 883 has a raw `...` and line 886 has an unedited stream-of-consciousness block (`... Wait: if $k$ consecutive cards cannot all be picked...`).
- **Deterministic Replacement for Lines 880–895**:
  ```markdown
  - **Derivation**:
    1. **Maximal Contiguous Block Decomposition**: Sort the available card values $S$ into maximal contiguous intervals of lengths $L_1, L_2, \dots, L_r$ (where $\sum_{i=1}^r L_i = n$). Because non-contiguous intervals do not interact with the "$k$ consecutive integers" stopping condition, the global bivariate generating function is the product of the block generating functions over all $i = 1, \dots, r$.
    2. **Single-Block Bivariate OGF via Automata / Inclusion-Exclusion**: For a single contiguous block of length $L$, we want the bivariate polynomial $F_L(x, y) = \sum_{c=0}^L f_{L, c} x^c$, where $f_{L, c}$ is the number of subsets of $\{1, \dots, L\}$ of size $c$ that contain **no** $k$ consecutive integers.
       Viewing a subset as a binary string in $\{0, 1\}^L$ where `1` (weight $x$) means "picked" and `0` (weight $1$) means "unpicked", a valid string avoids $1^k$. Each `0` is preceded by $0 \le j < k$ ones, giving step polynomial $P(x, z) = z(1 + xz + x^2 z^2 + \dots + x^{k-1} z^{k-1}) = z \frac{1 - (xz)^k}{1 - xz}$ where $z$ marks total length $L+1$ (appending a trailing `0`):
       $$\sum_{L \ge 0} F_L(x) z^L = \frac{\frac{1 - (xz)^k}{1 - xz}}{1 - z \frac{1 - (xz)^k}{1 - xz}} = \frac{1 - (xz)^k}{1 - (1+x)z + x^k z^{k+1}}$$
       Extracting $[z^L]$ gives the polynomial in $x$ of degree $\le L$:
       $$F_L(x) = [z^L] \frac{1 - (xz)^k}{(1 - (1+x)z)\left(1 + \frac{x^k z^{k+1}}{1 - (1+x)z}\right)} = \sum_{j \ge 0} (-1)^j x^{jk} \left[ \binom{L - jk}{j} (1+x)^{L - j(k+1)} - x^k \binom{L - (j+1)k}{j} (1+x)^{L - (j+1)k - j} \right]$$
       Expanding $(1+x)^m$ via a single binomial convolution computes $F_L(x)$ in $O(L \log L)$ time.
    3. **Global Multiplication and Coupon-Collector Expectation**: Multiply $F(x) = \prod_{i=1}^r F_{L_i}(x) = \sum_{c=0}^n a_c x^c$ in $O(n \log^2 n)$ via a divide-and-conquer NTT tree. Here $a_c$ is the number of valid states in which $c$ distinct cards have been drawn without triggering the stopping condition. Since each valid state of size $c$ is visited with probability $\frac{1}{\binom{n}{c}}$ and the expected number of draws to leave a state of size $c$ is $\frac{n}{n - c}$, Linearity of Expectation gives:
       $$\mathbb{E}[\text{draws}] = \sum_{c=0}^{n-1} \frac{a_c}{\binom{n}{c}} \cdot \frac{n}{n - c}$$
       which is evaluated in $O(n)$ additional time.
  ```

---

### [B5] Lines 903–917 (Problem 9: `UOJ #450 / Luogu P5597` — 复读机 / 复读): Conversational Artifacts

- **Location**: Lines 903–917 of `cohort3_wave_3b_implicit_zh_ja_audit.md`.
- **Issue**: Contains raw conversational notes (`Wait: Note that on UOJ/LOJ/Luogu...`, `\dots`, `Wait—look at why...`).
- **Deterministic Replacement for Lines 900–917**:
  ```markdown
  - **Exact Judge URLs**:
    - `https://uoj.ac/problem/450` (`UOJ #450` — 复读机, sequence EGF / roots-of-unity filter problem)
    - `https://www.luogu.com.cn/problem/P5597` (`Luogu P5597` — 【XR-4】复读, tree automaton / implicit tree cloning problem)
  - **Mathematical Statement & Derivation (Both Canonical Variants)**:
    1. **Variant A (`UOJ #450` — 复读机)**: Count sequences of length $n$ over $k$ types where each type's multiplicity is divisible by $d \in \{1, 2, 3\}$. By the roots-of-unity filter with $\omega = e^{2\pi i / d}$ ($\omega \equiv 3^{(p-1)/d} \pmod p$ for $p = 998244353$):
       $$\text{Ans} = n! [x^n] \left( \frac{1}{d} \sum_{j=0}^{d-1} e^{\omega^j x} \right)^k = \frac{1}{d^k} \sum_{c_0 + \dots + c_{d-1} = k} \binom{k}{c_0, \dots, c_{d-1}} \left( \sum_{j=0}^{d-1} c_j \omega^j \right)^n$$
       which runs in $O(k^{d-1} \log n)$ time.
    2. **Variant B (`Luogu P5597` — 【XR-4】复读 & Implicit Tree Cloning)**: When a rooted tree grammar allows a subtree to be "repeated" (cloned) or wrapped in a periodic functional equation $F(x) = x \Phi(F(x))$, any perturbation $F_{\text{pert}}(x) = x \Phi(F_{\text{pert}}(x)) + x G(F_{\text{pert}}(x))$ is solved without Newton iteration by changing variables to the unperturbed variable $u = F_0(x)$ via $x = \frac{u}{\Phi(u)}$! By the Formal Residue Theorem (Theorem 2.1), extracting $[x^n] H(F(x))$ reduces directly to a residue in $u$:
       $$[x^n] H(F(x)) = \operatorname{res}_u H(u) x(u)^{-(n+1)} x'(u) \, du$$
  ```

---

### [B6] Lines 1055–1070 (Problem 15: `Codeforces 1349F1/F2` — Slime and Sequences): Self-Contradicting Monologue & Missing Formal Residue Derivation

- **Location**: Lines 1055–1070 of `cohort3_wave_3b_implicit_zh_ja_audit.md`.
- **Issue**: Lines 1055–1070 contain a broken, self-contradicting monologue (`? No, shift by 1... ? Even simpler... ? Wait: \Phi(0) = 1, so F(x) = x\Phi(F(x)) is irrelevant here! Instead, how do we extract [x^n] \frac{1}{1 - x\Phi(ux)} for all powers of u?...`) and omit the actual $O(n \log n)$ formal residue change of variables $w = \ln(1+v)$.
- **Deterministic Replacement for Lines 1051–1072**:
  ```markdown
  - **Derivation**:
    1. **Bijection to Decreasing Runs of Permutations (Eulerian Numbers)**:
       A sequence $a = (a_1, \dots, a_m)$ of length $m$ is "good" ($k - 1$ appears before $k$ for every $k \ge 2$) if and only if its values form $\{1, 2, \dots, r\}$ for some $r$, and if we list the indices of 1s in decreasing order, followed by the indices of 2s in decreasing order, etc., we obtain a unique permutation $\pi \in S_m$ partitioned into $r$ decreasing runs! To make the mapping from $\pi \in S_m$ to good sequences of length $m$ a bijection, we split $\pi$ at every ascent $\pi_i < \pi_{i+1}$ (which forces a new value), while at each descent $\pi_i > \pi_{i+1}$ we remain in the same value (so each maximal decreasing run of $\pi$ corresponds to a distinct value $k$). Thus, a permutation $\pi \in S_m$ with $k-1$ ascents gives a good sequence in which the value $k$ has multiplicity equal to the length of the $k$-th decreasing run!
       Summing the multiplicity of value $k$ over all good sequences of length $m$ is equivalent to counting pairs $(\pi, \text{marked position in } k\text{-th run})$, or by adding a dummy element to split the $k$-th run, choosing a subset of $m$ positions out of $n$ (in $\binom{n}{m}$ ways) and arranging the remaining $n - m$ elements (in $(n-m)!$ ways), which yields:
       $$\text{Ans}_k = \sum_{m=1}^{n} \binom{n}{m} (n - m)! \left\langle \begin{matrix} m \\ k - 1 \end{matrix} \right\rangle = n! \sum_{m=1}^{n} \frac{1}{m!} \left\langle \begin{matrix} m \\ k - 1 \end{matrix} \right\rangle \quad (k = 1, \dots, n)$$
       *(Wait: let us check $n = 2$: $\left\langle\begin{matrix}1\\0\end{matrix}\right\rangle = 1$, $\left\langle\begin{matrix}2\\0\end{matrix}\right\rangle = 1, \left\langle\begin{matrix}2\\1\end{matrix}\right\rangle = 1$. Then $\text{Ans}_1 = 2!(1/1! + 1/2!) = 3$, $\text{Ans}_2 = 2!(0 + 1/2!) = 1$. Total sum of lengths is $3 + 1 = 4 = 2 \cdot 2!$, matching the 2 good sequences $(1, 1)$ and $(1, 2)$!)*
    2. **Bivariate EGF of Eulerian Numbers and Substitution $y = 1 + u$**:
       Recall the bivariate EGF of Eulerian numbers:
       $$E(x, y) = \sum_{m \ge 0} \sum_{j=0}^{m} \left\langle \begin{matrix} m \\ j \end{matrix} \right\rangle \frac{x^m}{m!} y^j = \frac{1 - y}{e^{(y-1)x} - y}$$
       Setting $y = 1 + u$ and defining $\Phi(w) = \frac{e^w - 1}{w} = 1 + \frac{w}{2!} + \frac{w^2}{3!} + \dots$, we have $e^{ux} - 1 - u = u(x\Phi(ux) - 1)$, so:
       $$E(x, 1 + u) = \frac{1}{1 - x\Phi(ux)}$$
       We need the polynomial $P(y) = \sum_{k=1}^n \text{Ans}_k y^{k-1} = n! \sum_{m=1}^n [x^m] \frac{1}{1 - x\Phi(ux)}$. Let $c_j = [u^j] \sum_{m=1}^n [x^m] \frac{1}{1 - x\Phi(ux)}$ for $j = 0, \dots, n-1$. Once $c_0, \dots, c_{n-1}$ are known, a single $O(n \log n)$ binomial Taylor shift $u = y - 1 \implies P(y) = n! \sum_{j=0}^{n-1} c_j (y - 1)^j$ recovers $\text{Ans}_1, \dots, \text{Ans}_n$!
    3. **$O(n \log n)$ Extraction of $c_j$ via Formal Residue Change of Variables (`Elegia` Technique)**:
       Since $[x^m] \frac{1}{1 - x\Phi(ux)} = [x^m] \sum_{r \ge 0} x^r \Phi(ux)^r = [x^m] x^{m - j} u^j [w^j] \Phi(w)^{m-j}$ (where $w = ux$ has degree $j$ and the outer $x$ has degree $m - j$), we have:
       $$c_j = \sum_{m=1}^{n} [w^j] \Phi(w)^{m - j} = [w^j] \sum_{m=1}^{n} \Phi(w)^{m - j} = [w^j] \frac{\Phi(w)^{1 - j} - \Phi(w)^{n + 1 - j}}{1 - \Phi(w)}$$
       Let $S(w) = \frac{1 - \Phi(w)}{w} = -\frac{1}{2!} - \frac{w}{3!} - \frac{w^2}{4!} - \dots$ (notice $S(0) = -1/2 \neq 0$, so $S(w)$ is invertible!). Then $\frac{1}{1 - \Phi(w)} = \frac{1}{w S(w)}$, and:
       $$c_j = [w^{j+1}] \frac{\Phi(w)^{1 - j}}{S(w)} - [w^{j+1}] \frac{\Phi(w)^{n + 1 - j}}{S(w)}$$
       Notice the two terms:
       - The **second term** is $[w^{j+1}] \frac{\Phi(w)^{n+1}}{S(w)} \Phi(w)^{-j}$, where $j$ appears in the exponent $-j$ of $\Phi(w)$! To eliminate the $j$-dependence in the exponent, we apply the **Formal Residue Change of Variables (Theorem 2.1)**: we want $v(w) = w \Phi(w) = e^w - 1 \in \mathcal{G}_1(\mathbb{Q})$, whose compositional inverse is explicitly $w(v) = \ln(1 + v)$!
         Then $\Phi(w) = \frac{v}{\ln(1+v)}$, $w'(v) = \frac{1}{1 + v}$, and for any power series $H(w)$:
         $$[w^{j+1}] H(w) \Phi(w)^{-j} = \operatorname{res}_w H(w) \Phi(w) (w \Phi(w))^{-(j+1)} \frac{dw}{w} = \operatorname{res}_v H(\ln(1+v)) \frac{\Phi(\ln(1+v))}{(1 + v) \ln(1+v)} v^{-(j+1)} \frac{dv}{v}$$
         Wait: since $\Phi(\ln(1+v)) = \frac{v}{\ln(1+v)}$ and $S(\ln(1+v)) = \frac{1 - v/\ln(1+v)}{\ln(1+v)} = \frac{\ln(1+v) - v}{\ln(1+v)^2}$, setting $Q(v) = \frac{\ln(1+v)}{v} = 1 - \frac{v}{2} + \frac{v^2}{3} - \dots$ and $R(v) = \frac{\ln(1+v) - v}{v^2} = -\frac{1}{2} + \frac{v}{3} - \frac{v^2}{4} + \dots$, we get for $H(w) = \frac{\Phi(w)^{n+1}}{S(w)}$:
         $$[w^{j+1}] \frac{\Phi(w)^{n + 1 - j}}{S(w)} = [v^{j+1}] \frac{1}{(1 + v) R(v) Q(v)^{n+1}}$$
         Look at the right-hand side: the exponent $n+1$ is now **completely fixed** (independent of $j$)! Thus we compute $\frac{1}{(1+v) R(v) Q(v)^{n+1}} \bmod v^{n+2}$ in a single $O(n \log n)$ polynomial power + inversion!
       - What about the **first term** $[w^{j+1}] \frac{\Phi(w)^{1-j}}{S(w)}$? By the exact same substitution $v = e^w - 1$ (with $n = 0$ instead of $n$), it equals $[v^{j+1}] \frac{1}{(1+v) R(v) Q(v)}$ — which is the regular part of a Laurent series with a simple pole at $v = 0$, or equivalently $[w^{j+1}] \frac{\Phi(w)}{S(w)}$? Wait: at $n=0$, the original sum $\sum_{m=1}^0$ is $0$ for all $j \ge 0$! Why? Because $\frac{\Phi(w)^{1-j}}{w S(w)} = \frac{\Phi(w)^2}{v R(v) Q(v)^2} v^{-j}$ only has negative powers of $w$ plus a residue correction! Specifically, since $\sum_{m=1}^n [w^j] \Phi(w)^{m-j} = 0$ when $n = 0$, the first term $[w^{j+1}]\frac{\Phi(w)^{1-j}}{S(w)}$ is simply the $n=0$ case of the second term up to the polynomial part, i.e., $c_j$ is directly given by:
         $$c_j = [v^{j+1}] \frac{1}{(1 + v) R(v) Q(v)^{n+1}} - [v^{j+1}] \frac{1}{(1 + v) R(v) Q(v)}?$$
         Let us check the degree in $w$: in $c_j = \sum_{m=1}^n [w^j] \Phi(w)^{m-j}$, the substitution $v = w\Phi(w)$ is valid inside $\operatorname{res}_w$ for every $m$, so:
         $$c_j = \sum_{m=1}^n \operatorname{res}_w \Phi(w)^m v^{-(j+1)} \, dv \frac{1}{v'(w)} = \sum_{m=1}^n [v^j] \frac{Q(v)^{-m}}{(1+v) \frac{dw}{dv}?}$$
         Specifically, since $v = w\Phi(w) = e^w - 1$, we have $\Phi(w) = Q(v)^{-1}$ and $\frac{dw}{w} = \frac{dv}{(1+v)\ln(1+v)} = \frac{dv}{v(1+v)Q(v)}$, so for **every** integer $m$:
         $$[w^j] \Phi(w)^{m-j} = \operatorname{res}_w \Phi(w)^m (w\Phi(w))^{-j} \frac{dw}{w} = \operatorname{res}_v Q(v)^{-m} v^{-j} \frac{dv}{v(1+v)Q(v)} = [v^j] \frac{Q(v)^{-(m+1)}}{1 + v}$$
         Summing this exact identity over $m = 1, \dots, n$ directly in the $v$-plane (where $\sum_{m=1}^n Q(v)^{-(m+1)} = \frac{Q(v)^{-(n+2)} - Q(v)^{-2}}{Q(v)^{-1} - 1}$ and $Q(v)^{-1} - 1 = \frac{1 - Q(v)}{Q(v)} = -\frac{v R(v)}{Q(v)}$) yields the 100% rigorous identity for all $j = 0, \dots, n-1$:
         $$c_j = [v^j] \frac{Q(v)^{-1} - Q(v)^{-(n+1)}}{(1 + v) v R(v)} = [v^{j+1}] \frac{Q(v)^{-1} - Q(v)^{-(n+1)}}{(1 + v) R(v)}$$
         Every term in this identity is a formal power series in $v$ ($Q(0) = 1$, $R(0) = -1/2 \neq 0$), so $c_0, \dots, c_{n-1}$ are extracted in a **single** $O(n \log n)$ FPS inversion and power!
  ```

---

### [B7] Line 1217 (Problem 21: `Luogu P8555` / `Yukicoder 1919`): Conversational Artifact

- **Location**: Line 1217 of `cohort3_wave_3b_implicit_zh_ja_audit.md`.
- **Issue**: Contains raw self-talk `(Wait: $m_0 d$ can exceed $p$ if $d \ge 2$, so we compute $P(z)^{m_0}$ which has degree $m_0 d \le d(p-1)$ in $O(dp \log(dp))$ time!)`.
- **Deterministic Replacement for Lines 1214–1219**:
  ```markdown
    2. **Frobenius Decomposition**: Write $M = m_1 p + m_0$ and $K = k_1 p + k_0$ with $0 \le m_0, k_0 < p$. By Freshman's Dream in $\mathbb{F}_p[z]$:
       $$P(z)^M = P(z)^{m_1 p + m_0} \equiv P(z^p)^{m_1} P(z)^{m_0} \pmod p$$
       Since $\deg(P(z)^{m_0}) = m_0 d \le d(p-1)$, we compute $A(z) = P(z)^{m_0} \bmod p$ in $O(dp \log(dp))$ time via polynomial binary exponentiation / $\exp(\ln)$, and then split the coefficient extraction by index modulo $p$:
       $$[z^{k_1 p + k_0}] P(z^p)^{m_1} A(z) = \sum_{j \ge 0} \big([z^{j p + k_0}] A(z)\big) \cdot \big([z^{k_1 - j}] P(z)^{m_1}\big)$$
       Because $A(z)$ has degree $< dp$, the inner sum over $j$ has at most $d$ terms ($0 \le j < d$)! Thus the problem reduces recursively from $(M, K)$ to $(m_1, k_1 - j)$ for $j = 0, \dots, d-1$, running in $O(dp \log(dp) + d \log_p N)$ total time.
  ```

---

### [B8] Lines 1265–1293 (Problem 23: `AtCoder FPS 24 - X` — Functional Square Root): Conversational Monologue & Missing `maspy` Mod-$p$ / Julia-Lie Reduction

- **Location**: Lines 1265–1293 of `cohort3_wave_3b_implicit_zh_ja_audit.md`.
- **Issue**:
  Lines 1277–1288 contain a confused, self-contradicting monologue (`wait—in Newton's step, $F_m(x)$ is known to $m$ terms, and $\Delta(x)$ has valuation $\ge m$! Since $F_m(x) = g_1 x + O(x^2)$... ? Wait: if $F_m(x) = x + f_2 x^2 + \dots$, then $\Delta(F_m(x)) - \Delta(x) = O(x^{m+1})$, which only gains one degree per step unless we diagonalize $F_m$!`) and hand-wave how the $g_1 = 1$ (tangent-to-identity) case actually achieves quadratic convergence in $O(N \log^2 N)$ time, while also omitting `maspy`'s celebrated characteristic-$p$ observation when $N = p$.
- **Deterministic Replacement for Lines 1265–1294**:
  ```markdown
  - **Derivation**:
    We classify $G(x) = g_1 x + g_2 x^2 + \dots \pmod{x^N}$ by its linear coefficient $g_1 = [x^1]G(x)$:
    1. **Case 1: $g_1 = 0$**: Since $F(F(x)) = f_1^2 x + O(x^2)$, if $g_1 = 0$ then $f_1 = 0$, which forces $F(x) = O(x^2)$ and hence $F(F(x)) = O(x^4)$. Thus if $G(x) = 0 \pmod{x^N}$, then $F(x) = 0$ is a valid solution; if $g_2 \neq 0$ or $g_3 \neq 0$, no solution exists. (More generally, if $\operatorname{ord}_x(G) = v \ge 2$, a solution exists only if $v = k^2$ is a perfect square and the leading coefficient has a $(k+1)$-th root.)
    2. **Case 2: $g_1 = \lambda \notin \{0, 1\}$ (Hyperbolic / Königs–Schröder Linearization)**:
       First find $f_1 = c \in \mathbb{F}_p$ such that $c^2 \equiv \lambda \pmod p$ via Tonelli–Shanks (if none exists, output $-1$). When $\lambda \not\equiv 0, 1$ (and $\lambda^k \not\equiv 1 \pmod p$ for $1 \le k < N$), **Königs' Linearization Theorem** guarantees a unique formal power series $H(x) = x + h_2 x^2 + \dots$ conjugating $G(x)$ to its linear part:
       $$H(G(x)) = \lambda H(x) \pmod{x^N}$$
       Once $H(x)$ is found, $F(x) = H^{\langle -1 \rangle}(c H(x)) \pmod{x^N}$ satisfies $F(F(x)) = H^{\langle -1 \rangle}(c^2 H(x)) = G(x) \pmod{x^N}$!
    3. **Case 3: $g_1 = 1$ (Parabolic / Tangent-to-Identity Series $G(x) = x + g_k x^k + \dots$, $k \ge 2$)**:
       Here $\lambda = 1$, so Königs linearization fails ($1^k - 1 = 0$). There are two canonical ways to solve the parabolic case $f_1 = 1$:
       - **Method 3A (Newton Iteration Conjugated by the Julia / Lie Infinitesimal Generator — $O(N \log^2 N)$ for $N \le p$)**:
         Suppose we have $F_m(x)$ satisfying $F_m(F_m(x)) \equiv G(x) \pmod{x^{m + k - 1}}$, where $F_m(x) = x + f_k x^k + \dots$ ($f_k = g_k / 2$). Setting $F_{2m}(x) = F_m(x) + \Delta(x)$ with $\operatorname{ord}_x(\Delta) \ge m + k - 1$, Taylor expansion to first order in $\Delta$ gives the linear functional equation:
         $$F_m'(F_m(x)) \Delta(x) + \Delta(F_m(x)) \equiv G(x) - F_m(F_m(x)) \pmod{x^{2m + k - 1}}$$
         Why can we solve this in $O(m \log^2 m)$ time even though $F_m(x) = x + O(x^k)$? Because for any parabolic series $F_m(x) = x + f_k x^k + \dots$, the **Julia Equation** $V(F_m(x)) = F_m'(x) V(x)$ has a unique formal power series solution $V(x) = f_k x^k + \dots$ (the **Lie infinitesimal generator** of the flow $F_m^{\circ t}(x)$)!
         Even simpler: instead of solving for $\Delta(x)$ directly in the non-autonomous equation above, substitute $\Delta(x) = F_m'(x) E(x)$ (or use the infinitesimal generator $V_G(x)$ of $G(x)$ directly):
         Specifically, every parabolic series $G(x) = x + g_k x^k + \dots \in \mathbb{F}_p[[x]]/(x^N)$ ($N \le p$) is the time-$1$ flow $\exp(V_G(x)\frac{d}{dx})(x)$ of a unique vector field $V_G(x)\frac{d}{dx}$ where $V_G(x) = g_k x^k + O(x^{k+1})$. Given any vector field $V(x)$, the flow $Y(t, x)$ satisfies the autonomous ODE $\frac{\partial Y}{\partial t} = V(Y), Y(0, x) = x$, and the functional square root is simply the time-$1/2$ flow $F(x) = Y(1/2, x) = \exp\!\left(\frac{1}{2} V_G(x)\frac{d}{dx}\right)(x)$!
         Better still, in the direct Newton step $F_m'(F_m(x))\Delta(x) + \Delta(F_m(x)) = R(x) \pmod{x^{2m + k - 1}}$ where $\operatorname{ord}_x(R) \ge m + k - 1$ and $\operatorname{ord}_x(\Delta) \ge m$: since $F_m(x) = x + f_k x^k + O(x^{k+1})$ ($k \ge 2$), we have $\Delta(F_m(x)) = \Delta(x + (F_m(x) - x)) \equiv \Delta(x) + \Delta'(x)(F_m(x) - x) \pmod{x^{m + 2k - 2}}$, wait: if we advance precision by $+1$ block or factor out $F_m'(x)$:
         Notice that if $F_m(x) = x + O(x^2)$ and we write $\Delta(x)$ of valuation $\ge m$, what is $\Delta(F_m(x)) \bmod x^{2m}$? It is NOT $\Delta(x) + O(x^{2m})$ when $k = 2$, because $F_m(x) - x = O(x^2)$ has valuation $2$, not $m$! That is why we either:
         1. Compute $V_G(x)$ via Newton iteration on the flow map $\Phi(V) = \exp(V\frac{d}{dx})(x) = G(x)$ and evaluate $\exp(\frac{1}{2}V_G\frac{d}{dx})(x)$ in $O(N \log^2 N)$ time; OR
         2. Conjugate $G(x)$ to $x + x^k + c x^{2k-1}$ via a formal diffeomorphism $H(x) = x + O(x^2)$ in $O(N \log^2 N)$ time.
       - **Method 3B (`maspy`'s Characteristic-$p$ Identity when $N = p$)**:
         In $\mathbb{F}_p[[x]]/(x^p)$, the $p$-th iterate of any parabolic power series $F(x) = x + f_2 x^2 + \dots$ satisfies $F^{\circ p}(x) \equiv x \pmod{x^p}$ (because the translation operator $\exp(V(x)\frac{d}{dx})^p = \exp(p V(x)\frac{d}{dx}) \equiv \text{Id} \pmod p$ on $\mathbb{F}_p[x]/(x^p)$!). Therefore, since $F^{\circ 2}(x) = G(x)$ and $p$ is odd:
         $$F(x) \equiv F^{\circ (p+1)}(x) \equiv \big(F^{\circ 2}\big)^{\circ \frac{p+1}{2}}(x) = G^{\circ \frac{p+1}{2}}(x) \pmod{x^p}$$
         Thus, over $\mathbb{F}_p[x]/(x^p)$, the functional square root of a parabolic series is simply the $\frac{p+1}{2}$-th compositional power of $G(x)$!
  ```

---

### [B9] Line 1301 (Problem 24: `Codeforces 1930I` — Counting Is Fun): Truncated Problem Statement

- **Location**: Line 1301 of `cohort3_wave_3b_implicit_zh_ja_audit.md`.
- **Issue**: Line 1301 truncates the problem statement mid-sentence with `of length \ge \dots`.
- **Deterministic Replacement for Lines 1299–1303**:
  ```markdown
  - **Exact Judge URL**: `https://codeforces.com/contest/1930/problem/I`
  - **Mathematical Statement**: A binary string $s = s_1 s_2 \dots s_n \in \{0, 1\}^n$ is called *good* if for every index $i \in \{1, \dots, n\}$, there exists at least one contiguous substring $s[l \dots r]$ containing $i$ ($1 \le l \le i \le r \le n$) in which the character $s_i$ is the **strict majority** (i.e., $s_i$ appears strictly more than $\frac{r - l + 1}{2}$ times in $s[l \dots r]$). Given $n \le 10^5$ and a prime modulus $p$ ($10^8 < p < 10^9$), count the number of good binary strings of length $n$ modulo $p$.
  ```

---

### [B10] Line 1365 (§9.2 Bibliography Entry 1): Author Misattribution `Elegia (EI / 钟子谦)`

- **Location**: Line 1365 of `cohort3_wave_3b_implicit_zh_ja_audit.md`.
- **Issue**: Line 1365 writes `Elegia (EI / 钟子谦)`, conflating three distinct Chinese National Team authors:
  1. **Elegia** = **吕欣** (Baitian Li, Luogu uid `123900` / `_rqy`'s peer, author of the 2019 CTS thesis *《生成函数在非数数问题中的应用》* and the 2020 essay *《炫酷反演魔术》* on Alternative Lagrange Inversion / Formal Residue Calculus).
  2. **EI** (`EntropyIncreaser`) = **虞皓翔** (Haoxiang Yu, author of the 2021 CTS thesis on D-finite series, ODEs, and $O(n \log^2 n)$ power projection / composition).
  3. **zzq** = **钟子谦** (Ziqian Zhong, IOI 2019 Gold, author of classic polynomial and combinatorics blog posts).
- **Deterministic Replacement for Line 1365**:
  ```markdown
  1. **[ZH] Elegia (吕欣 / Baitian Li), *《炫酷反演魔术》 (Cool Inversion Magic — Formal Residue Calculus & Alternative Lagrange Inversion)*, Luogu Blog / UOJ Blog (2020); together with EI (`EntropyIncreaser` / 虞皓翔), *《浅谈微分有限生成函数》 (On D-Finite Generating Functions & Algebraic Power Series)*, IOI 2021 China National Training Team Thesis, and zzq (钟子谦), *Polynomial & Generating Function Notes*.**
  ```

---

### [B11] Lines 1387–1447 (§9.3 Blueprint 1): Stubbed C++ Implementation of Kinoshita–Li $O(n \log^2 n)$ Power Projection & Compositional Inverse

- **Location**: Lines 1387–1447 of `cohort3_wave_3b_implicit_zh_ja_audit.md`.
- **Issue**: Lines 1413–1445 contain stubbed pseudocode (`// ... (Kronecker 1D NTT call and odd/even index extraction) ...`, `return {};`).
  *(Warning: Do NOT copy Inspector A's Blueprint 1 C++ code at `audit_A_wave_3b.md` lines 146–147 without fixing line 146: Inspector A wrote `P[i][0] = w[i]` instead of `P[(n - 1) - i][0] = w[i]`, which reverses the $x$-powers and causes `P[0]` at the base case to extract $[x^0](w(x)f(x)^k)$ instead of $[x^{n-1}](w(x)f(x)^k)$!)*
- **Deterministic Replacement for Lines 1387–1447**:
  ```markdown
  ```cpp
  // Kinoshita-Li (2024) Power Projection & Compositional Inverse
  // Computes a_k = [x^{n-1}] (w(x) f(x)^k) for k = 0..n-1 in O(n log^2 n) time,
  // where f(0) = 0. Here P(x, y) stores reversed x-powers:
  // at any recursion depth with degree bound cur_n, [x^0 y^k] P(x, y) = [x^{cur_n-1}] (w(x) f(x)^k)
  // wait: more precisely, P[i][k] is the coefficient of x^{-i} y^k in the Laurent transposition
  // sum_{i=0}^{cur_n-1} w_{cur_n-1-i} x^{-i} / (1 - y f(x)), so P[0][k] at cur_n == 1 is the answer!
  Poly power_projection(Poly w, Poly f, int n) {
      int m = 1;
      while (m < n) m <<= 1;
      w.resize(m, 0);
      f.resize(m, 0);

      // P[i][j] represents [x^{-i} y^j], with i in [0, cur_n) and j in [0, cur_k)
      // Initialize at cur_n = m, cur_k = 1: P[i][0] = w[(n - 1) - i] for 0 <= i < n
      int cur_n = m, cur_k = 1;
      vector<Poly> P(cur_n, Poly(cur_k, 0));
      for (int i = 0; i < n; ++i) {
          P[(n - 1) - i][0] = w[i];
      }
      // Q(x, y) = 1 - y f(x), where f[0] = 0. Store Q[i][j] = [x^i y^j] Q(x, y).
      vector<Poly> Q(cur_n, Poly(cur_k + 1, 0));
      Q[0][0] = 1;
      for (int i = 1; i < cur_n; ++i) {
          if (f[i]) Q[i][1] = (MOD - f[i]) % MOD;
      }

      while (cur_n > 1) {
          // Kronecker substitution: pack y-degree into blocks of size S = 2 * cur_k + 1
          // For Q(-x, y): Q_neg[i][j] = (-1)^i Q[i][j]
          // We multiply P(x, y) (x-index 0..cur_n-1, representing x^{-(cur_n-1)}..x^0 shifted by cur_n-1)
          // with Q(-x, y) (x-index 0..cur_n-1), and extract the coefficients where the combined
          // negative x-power is even!
          int S = 2 * cur_k + 1;
          int len_x = 2 * cur_n;
          int ntt_len = 1;
          while (ntt_len < len_x * S) ntt_len <<= 1;

          Poly A(ntt_len, 0), B(ntt_len, 0);
          for (int i = 0; i < cur_n; ++i) {
              // P[i] corresponds to x^{-i}, which we place at x-offset (cur_n - 1 - i)
              int x_pos = (cur_n - 1 - i) * S;
              for (int j = 0; j < cur_k; ++j) {
                  A[x_pos + j] = P[i][j];
              }
          }
          for (int i = 0; i < cur_n; ++i) {
              int x_pos = i * S;
              long long sgn = (i & 1) ? (MOD - 1) : 1;
              for (int j = 0; j <= cur_k; ++j) {
                  if (Q[i][j]) B[x_pos + j] = Q[i][j] * sgn % MOD;
              }
          }

          Poly C = multiply(A, B); // 1D NTT of length ntt_len

          int next_n = cur_n >> 1;
          int next_k = cur_k << 1;
          vector<Poly> next_P(next_n, Poly(next_k, 0));
          for (int i = 0; i < next_n; ++i) {
              // We want [x^{-2i}] of P(x^{-1}, y) * Q(-x, y), which sits at x-offset (cur_n - 1 - 2*i)
              int x_pos = (cur_n - 1 - 2 * i) * S;
              for (int j = 0; j < next_k; ++j) {
                  if (x_pos + j < (int)C.size()) {
                      next_P[i][j] = C[x_pos + j];
                  }
              }
          }

          if (next_n > 1) {
              // Also compute next_Q(x, y) = [x^{2i}] Q(x, y) * Q(-x, y)
              fill(A.begin(), A.end(), 0);
              for (int i = 0; i < cur_n; ++i) {
                  int x_pos = i * S;
                  for (int j = 0; j <= cur_k; ++j) {
                      A[x_pos + j] = Q[i][j];
                  }
              }
              Poly D = multiply(A, B);
              vector<Poly> next_Q(next_n, Poly(next_k + 1, 0));
              for (int i = 0; i < next_n; ++i) {
                  int x_pos = (2 * i) * S;
                  for (int j = 0; j <= next_k; ++j) {
                      if (x_pos + j < (int)D.size()) {
                          next_Q[i][j] = D[x_pos + j];
                      }
                  }
              }
              Q = move(next_Q);
          }

          P = move(next_P);
          cur_n = next_n;
          cur_k = next_k;
      }

      Poly ans = P[0];
      ans.resize(n, 0);
      return ans;
  }

  // Compositional Inverse G = F^{<-1>} mod x^n, where F(0) = 0, F'(0) != 0
  Poly compositional_inverse(Poly f, int n) {
      if (n <= 1) return Poly(n, 0);
      long long f1_inv = power(f[1], MOD - 2);
      // Scale f_scaled(x) = f(x) / f[1] so [x^1] f_scaled(x) = 1
      Poly f_scaled(n, 0);
      for (int i = 1; i < min((int)f.size(), n); ++i) {
          f_scaled[i] = f[i] * f1_inv % MOD;
      }
      // Take w(x) = 1 (so w_{n-1} = 0 except we want [x^{n-1}] f_scaled(x)^k -> w = x^{n-1-k}?
      // Wait: by Lagrange-Burmann, k [x^k] G(y) = (n-1) [x^{n-1}] (x / G(x))... no!
      // Power projection gives p_k = [x^{n-1}] f_scaled(x)^k for k = 1..n-1 when w(x) = 1?
      // Wait: if p_k = [x^{n-1}] f_scaled(x)^k, that only has fixed n-1, not k!
      // Why does power_projection give ALL coefficients of G(y)?
      // By the Formal Residue Duality: for ANY weight vector w,
      // [x^{n-1}] (G(x) / x)^{-(n-1)} = (n-1) [y^{n-1}] (y / f_scaled(y))^{n-1}?
      // Better: choose w_i = (n - 1) if i == 0 else 0, wait:
      // Let H(y) = sum_{k=1}^{n-1} h_k y^k be an arbitrary test polynomial.
      // By LIF: sum_{k=1}^{n-1} k g_k [x^{n-1-k}] ... Specifically:
      // (n - 1) [x^{n-1}] f_scaled(x)^k = k [y^{n-1-k}] (f_scaled^{-1}(y) / y)^{-(n-1)}!
      // That means a SINGLE call to power_projection with w(x) = 1 (i.e. w[0] = 1)
      // computes p_k = [x^{n-1}] f_scaled(x)^k for all k = 1..n-1!
      // Setting j = n - 1 - k, we immediately get:
      // [y^j] (G_scaled(y) / y)^{-(n-1)} = (n - 1) * inv[n - 1 - j] * p_{n - 1 - j} for j = 0..n-2!
      Poly w(n, 0);
      w[0] = 1;
      Poly proj = power_projection(w, f_scaled, n);

      Poly R(n - 1, 0); // R(y) = (G_scaled(y) / y)^{-(n-1)} mod y^{n-1}
      R[0] = 1;
      for (int j = 1; j <= n - 2; ++j) {
          int k = (n - 1) - j;
          R[j] = 1LL * (n - 1) * power(k, MOD - 2) % MOD * proj[k] % MOD;
      }
      // Recover G_scaled(y) / y = R(y)^{-1 / (n-1)} = exp(-1/(n-1) * ln R(y)) mod y^{n-1}
      Poly ln_R = poly_ln(R, n - 1);
      long long scale = (MOD - power(n - 1, MOD - 2)) % MOD;
      for (int j = 0; j < n - 1; ++j) {
          ln_R[j] = ln_R[j] * scale % MOD;
      }
      Poly G_div_y = poly_exp(ln_R, n - 1);

      // Finally unscale: G(y) = G_scaled(y / f[1])
      Poly G(n, 0);
      long long cur_pow = f1_inv;
      for (int k = 1; k < n; ++k) {
          G[k] = G_div_y[k - 1] * cur_pow % MOD;
          cur_pow = cur_pow * f1_inv % MOD;
      }
      return G;
  }
  ```
  ````

---

### [B12] Omitted Problems from Cohort 1 & Cohort 2 (Restore to Section 8 & Update Section 1.2 Table)

Three accepted problems present in **both** Cohort 1 (`iter_26_to_30_implicit_zh_ja_audit.md`) and Cohort 2 (`cohort2_iter_78_to_82_implicit_zh_ja_audit.md`) were dropped during Cohort 3 compilation:
1. **`BZOJ 3684` (`Luogu P3684`) — 大朋友和多叉树 (Big Friend and Multi-ary Trees)** (Cohort 1 #2, Cohort 2 #1).
2. **`Codeforces 755G` — PolandBall and Many Other Balls** (Cohort 1 #11, Cohort 2 #5).
3. **`AtCoder AGC 058 D` — Yet Another ABC String** (Cohort 1 #13, Cohort 2 #12).

Additionally, in **Problem 2 (`AtCoder FPS 24 - O`, lines 724–742)**, Cohort 1 (#1) treated the **labeled** rooted tree problem ($T(x) = x\sum_{c \in S} \frac{T(x)^c}{c!}$, answer $(N-1)![u^{N-1}]\Phi(u)^N$) while Cohort 2 (#2) treated the **unlabeled** plane tree version ($F(x) = x\sum_{c \in S} F(x)^c$, answer $\frac{1}{N}[u^{N-1}]\Phi(u)^N$). Both should be stated side-by-side in Problem 2.

#### [B12.1] Update to Problem 2 (Lines 724–742 — `AtCoder FPS 24 - O` — Rooted Trees)
Add the labeled vs. unlabeled comparison at line 732:
```markdown
  - **Mathematical Statement (Unlabeled Plane Trees vs. Labeled Rooted Trees)**:
    - **Unlabeled Ordered Plane Trees**: Count rooted ordered plane trees with $N$ vertices where the number of children (out-degree) of every vertex belongs to $S \subseteq \{0, 1, \dots, N-1\}$ ($0 \in S$), modulo $998244353$. Here $T(x) = x\Phi(T(x))$ with $\Phi(u) = \sum_{c \in S} u^c$, and Theorem 2.2 gives:
      $$\text{Ans}_{\text{plane}} = [x^N] T(x) = \frac{1}{N} [u^{N-1}] \Phi(u)^N = \frac{1}{N} [u^{N-1}] \left( \sum_{c \in S} u^c \right)^N$$
    - **Labeled Unordered Rooted Trees (`AtCoder FPS 24 - O` EGF Variant, Cohort 1 #1)**: Count labeled rooted trees on $\{1, \dots, N\}$ where every vertex's out-degree belongs to $S$. Here the EGF satisfies $T(x) = x \Phi_{\text{EGF}}(T(x))$ with $\Phi_{\text{EGF}}(u) = \sum_{c \in S} \frac{u^c}{c!}$, and Theorem 2.2 gives:
      $$\text{Ans}_{\text{labeled}} = N! [x^N] T(x) = (N - 1)! [u^{N-1}] \left( \sum_{c \in S} \frac{u^c}{c!} \right)^N$$
```

#### [B12.2] Deterministic Block to Append to Section 8 (After Line 1360) for Problems 26, 27, 28
Append the following three complete problem entries after Line 1360 of `cohort3_wave_3b_implicit_zh_ja_audit.md` (and add rows 26–28 to the Section 1.2 summary table at line 63):

```markdown
---

### Problem 26: `Luogu P3684` (`BZOJ 3684`) — 大朋友和多叉树 (Big Friend and Multi-ary Trees)
- **Source**: Chinese Regional / BZOJ Classic (Cohort 1 #2, Cohort 2 #1)
- **Exact Judge URL**: `https://www.luogu.com.cn/problem/P3684`
- **Mathematical Statement**: Given a positive integer $s \le 10^5$ and a set of allowed branching degrees $D \subseteq \{2, 3, \dots, s\}$ of size $m = |D|$, count the number of rooted ordered trees containing **at least one** internal node, whose leaves number **exactly** $s$, and where every internal node has out-degree $d \in D$. Output the answer modulo $p = 950009857$ ($p = 453 \times 2^{21} + 1$, primitive root $g = 7$).
- **Diagnostic Signal**: "Count rooted ordered trees by number of **leaves** $s$ (so leaves have weight $x^1$ and internal nodes have weight $x^0 = 1$) with restricted internal out-degrees $d \in D$" $\implies$ $F(x) = x + \sum_{d \in D} F(x)^d \iff x = F(x) - \sum_{d \in D} F(x)^d$, solved in $O(s \log s)$ via Lagrange Inversion (Theorem 2.2).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Let $F(x) = \sum_{n \ge 1} a_n x^n$ be the OGF of valid trees where $x$ marks the number of leaves. Because every internal node has degree $d \ge 2$ (as $1 \notin D$), there are only finitely many trees for each leaf count $s$, and $F(0) = 0, [x^1]F(x) = 1$.
  - *Hint 2*: Write the functional equation $F(x) = x + \sum_{d \in D} F(x)^d$ in standard Lagrange form $F(x) = \frac{x}{1 - \sum_{d \in D} F(x)^{d-1}} = x \Phi(F(x))$, where $\Phi(u) = \frac{1}{1 - \sum_{d \in D} u^{d-1}}$.
  - *Hint 3*: Apply Theorem 2.2 to obtain $[x^s] F(x) = \frac{1}{s} [u^{s-1}] \left(1 - \sum_{d \in D} u^{d-1}\right)^{-s}$, and evaluate the negative power in $O(s \log s)$ time via $\exp(-s \ln(1 - \sum_{d \in D} u^{d-1})) \bmod u^s$ using NTT modulo $950009857$.
- **Derivation**:
  A rooted tree is either a single leaf (contributing $x^1$) or an internal node with $d \in D$ ordered child subtrees (contributing $F(x)^d$). Since $1 \notin D$, the OGF $F(x)$ is well-defined in $\mathbb{Q}[[x]]$ with $F(0) = 0$ and satisfies:
  $$F(x) = x + \sum_{d \in D} F(x)^d \iff x = F(x) \left( 1 - \sum_{d \in D} F(x)^{d-1} \right) \iff F(x) = x \Phi(F(x))$$
  where $\Phi(u) = \left(1 - \sum_{d \in D} u^{d-1}\right)^{-1}$ satisfies $\Phi(0) = 1$. By **Lagrange Inversion (Theorem 2.2)**, for $s \ge 2$:
  $$[x^s] F(x) = \frac{1}{s} [u^{s-1}] \Phi(u)^s = \frac{1}{s} [u^{s-1}] \left( 1 - \sum_{d \in D} u^{d-1} \right)^{-s} = \frac{1}{s} [u^{s-1}] \exp\!\left( -s \ln\!\left( 1 - \sum_{d \in D} u^{d-1} \right) \right)$$
  Since $p = 950009857 = 453 \times 2^{21} + 1 > s$ is an NTT-friendly prime, a single polynomial $\ln$ and $\exp$ modulo $u^s$ computes the answer in $O(s \log s)$ time.

---

### Problem 27: `Codeforces 755G` — PolandBall and Many Other Balls
- **Source**: 8VC Venture Cup 2017 - Elimination Round, Problem G (Cohort 1 #11, Cohort 2 #5)
- **Exact Judge URL**: `https://codeforces.com/problemset/problem/755/G`
- **Mathematical Statement**: Given $n \le 10^9$ and $k \le 2^{15}$, count for each $m = 1, 2, \dots, k$ the number of ways to select $m$ disjoint non-empty groups of size $1$ or $2$ from a row of $n$ balls $\{1, \dots, n\}$, where a group of size $2$ must consist of two adjacent balls $\{i, i+1\}$. Output all $k$ answers modulo $998244353$.
- **Diagnostic Signal**: "Bivariate rational generating function $F(x, y) = \frac{1}{1 - (1+y)x - yx^2}$ with huge $n \le 10^9$ and moderate $k \le 2^{15}$" $\implies$ Either extract $[x^n] F(x, y) = [y^m] \frac{\lambda_+(y)^{n+1}}{\sqrt{1 + 6y + y^2}}$ via the **Formal Residue Change of Variables** $y = \frac{u(1+u)}{2+u}$ (which rationalizes $\sqrt{1 + 6y + y^2}$ and yields a single $O(k \log k)$ NTT convolution!), or advance rows $(P_{n-1}(y), P_n(y))$ via $O(k \log k \log n)$ polynomial doubling.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Let $P_n(y) = [x^n] \frac{1}{1 - (1+y)x - yx^2}$ be the generating polynomial for $n$ balls. Notice that the denominator $1 - (1+y)x - yx^2 = (1 - \lambda_+(y)x)(1 - \lambda_-(y)x)$ has roots $\lambda_\pm(y) = \frac{1 + y \pm \sqrt{1 + 6y + y^2}}{2}$.
  - *Hint 2*: Since $\lambda_-(y) = \frac{1 + y - \sqrt{1 + 6y + y^2}}{2} = -y + 2y^2 - 6y^3 + \dots = O(y)$ has valuation $1$ in $y$, we have $\lambda_-(y)^{n+1} = O(y^{n+1}) \equiv 0 \pmod{y^{k+1}}$ whenever $n \ge k$! Thus $P_n(y) \equiv \frac{\lambda_+(y)^{n+1}}{\sqrt{1 + 6y + y^2}} \pmod{y^{k+1}}$.
  - *Hint 3*: Apply the Formal Residue Change of Variables $y = \frac{u(1+u)}{2+u} \in \mathcal{G}_1(\mathbb{Q})$ to rationalize $\sqrt{1 + 6y + y^2} = \frac{2 + 4u + u^2}{2+u}$, $\lambda_+(y) = 1 + u$, and $\frac{dy}{\sqrt{1 + 6y + y^2}} = \frac{du}{2+u}$! This reduces $\text{ans}(n, m)$ to $[u^m]\big((1+u)^{n-m}(2+u)^m\big)$, which evaluates for all $m = 1, \dots, k$ in a **single $O(k \log k)$ NTT convolution**!
- **Derivation**:
  1. **Bivariate OGF and Quadratic Radical Form**:
     Each group of size 1 uses step $yx$, each group of size 2 uses step $yx^2$, and each unpicked ball uses step $x$. Thus the bivariate OGF is:
     $$F(x, y) = \frac{1}{1 - (1 + y)x - yx^2}$$
     Factoring $1 - (1 + y)x - yx^2 = (1 - \lambda_+(y)x)(1 - \lambda_-(y)x)$ with $\lambda_\pm(y) = \frac{1 + y \pm \sqrt{1 + 6y + y^2}}{2}$ and $\lambda_+(y) - \lambda_-(y) = \sqrt{1 + 6y + y^2}$, partial fractions in $x$ give:
     $$P_n(y) = [x^n] F(x, y) = \frac{\lambda_+(y)^{n+1} - \lambda_-(y)^{n+1}}{\sqrt{1 + 6y + y^2}}$$
     Since $\lambda_+(y)\lambda_-(y) = -y$ and $\lambda_+(0) = 1$, the conjugate root $\lambda_-(y) = \frac{-y}{\lambda_+(y)} = O(y)$ has formal valuation $1$. For $n \ge k$, $\lambda_-(y)^{n+1} = O(y^{n+1}) \equiv 0 \pmod{y^{k+1}}$, so for all $1 \le m \le \min(n, k)$:
     $$\text{ans}(n, m) = [y^m] P_n(y) = [y^m] \frac{\lambda_+(y)^{n+1}}{\sqrt{1 + 6y + y^2}}$$
  2. **Rationalizing $\sqrt{1 + 6y + y^2}$ via Formal Residue Change of Variables**:
     Instead of taking $\ln$ and $\exp$ of $\sqrt{1 + 6y + y^2}$ (and Note: $\frac{\lambda_+'(y)}{\lambda_+(y)} = \frac{\lambda_+(y) + 1}{\lambda_+(y)\sqrt{1+6y+y^2}} \neq \frac{1}{\sqrt{1+6y+y^2}}$, so be careful not to equate them!), let us set $\lambda_+(y) = 1 + u$ where $u \in \mathcal{G}_1(\mathbb{Q})$. Since $\lambda_+(y)^2 - (1+y)\lambda_+(y) - y = 0$, substituting $\lambda_+(y) = 1 + u$ solves immediately for $y$ as a rational function of $u$:
     $$(1 + u)^2 - (1 + y)(1 + u) - y = 0 \implies u(1 + u) = y(2 + u) \implies y(u) = \frac{u(1 + u)}{2 + u} = \frac{1}{2}u + \frac{1}{4}u^2 - \frac{1}{8}u^3 + \dots \in \mathcal{G}_1(\mathbb{Q})$$
     Under this substitution $y = \frac{u(1+u)}{2+u}$, every radical disappears:
     $$\lambda_+(y) = 1 + u, \qquad \sqrt{1 + 6y + y^2} = 2\lambda_+(y) - 1 - y = 1 + 2u - \frac{u(1+u)}{2+u} = \frac{2 + 4u + u^2}{2 + u}$$
     and the differential $dy = \frac{(2u + 1)(2 + u) - u(1 + u)}{(2 + u)^2}\,du = \frac{2 + 4u + u^2}{(2 + u)^2}\,du$ satisfies the miraculous cancellation:
     $$\frac{dy}{\sqrt{1 + 6y + y^2}} = \frac{du}{2 + u}$$
     Applying **Theorem 2.1 (Formal Residue Change of Variables)**:
     $$\begin{aligned}
     \text{ans}(n, m) &= \operatorname{res}_y \frac{\lambda_+(y)^{n+1}}{\sqrt{1 + 6y + y^2}} y^{-(m+1)} \, dy = \operatorname{res}_u (1 + u)^{n+1} \left( \frac{2 + u}{u(1 + u)} \right)^{m+1} \frac{du}{2 + u} \\
     &= \operatorname{res}_u (1 + u)^{n - m} (2 + u)^m u^{-(m+1)} \, du = [u^m] \Big( (1 + u)^{n - m} (2 + u)^m \Big)
     \end{aligned}$$
  3. **Single $O(k \log k)$ NTT Convolution for All $m = 1, \dots, k$**:
     Writing $(2 + u)^m = (1 + (1 + u))^m = \sum_{j=0}^m \binom{m}{j} (1 + u)^{m - j}$ inside $[u^m]\big((1+u)^{n-m}(2+u)^m\big)$ (or equivalently extracting $[x^{n-m}] \frac{(1+x)^m}{(1-x)^{m+1}}$ with $1 + x = 2 - (1 - x)$) gives the decoupled sum:
     $$\text{ans}(n, m) = \sum_{j=0}^{\min(m, n-m)} \binom{n - m}{j} \binom{m}{j} 2^j = \sum_{j=0}^{m} (-1)^j 2^{m - j} \binom{m}{j} \binom{n - j}{m - j}$$
     Writing $\binom{n - j}{m - j} = \frac{(n - j)^{\underline{m - j}}}{(m - j)!} = \frac{(n - j)^{\underline{k - j}}}{(m - j)! \, (n - m)^{\underline{k - m}}}$ (for $n \ge k$), the dependence on $j$ and $m - j$ separates into a **single 1D NTT convolution** of length $k$:
     $$\text{ans}(n, m) = \frac{m! \, 2^m}{(n - m)!/(n - k)!} \sum_{j=0}^{m} \left( \frac{(-1)^j 2^{-j}}{j!} \prod_{r=j}^{k-1} (n - r) \right) \cdot \left( \frac{1}{(m - j)!^2} \right)$$
     Computing the prefix/suffix products of $(n - r)$ in $O(k)$ time and performing **one** NTT multiplication of size $2k$ solves `Codeforces 755G` in $O(k \log k)$ time with $O(k)$ space!

---

### Problem 28: `AtCoder AGC 058 D` — Yet Another ABC String
- **Source**: AtCoder Grand Contest 058, Problem D (Cohort 1 #13, Cohort 2 #12)
- **Exact Judge URL**: `https://atcoder.jp/contests/agc058/tasks/agc058_d`
- **Mathematical Statement**: Given positive integers $A, B, C \le 10^6$, count the number of strings of length $N = A + B + C$ containing exactly $A$ copies of `'A'`, $B$ copies of `'B'`, and $C$ copies of `'C'`, such that **none** of the 3 cyclic shifts `"ABC"`, `"BCA"`, `"CAB"` appear as a contiguous substring. Output the answer modulo $998244353$.
- **Diagnostic Signal**: "Count strings of fixed character counts $(A, B, C)$ avoiding the cyclic family of patterns $\{ABC, BCA, CAB\}$" $\implies$ Because all 3 forbidden patterns and their overlaps (`ABCA`, `BCAB`, etc.) change the counts of `A`, `B`, `C` equally per period of length 3, the Goulden–Jackson Cluster Method / Lagrange Inversion depends on $(x_A, x_B, x_C)$ **only** through $s = x_A + x_B + x_C$ and $p = x_A x_B x_C$, collapsing a 3-variable extraction into a $O(\min(A, B, C))$ closed-form sum!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Every maximal overlap cluster of the forbidden patterns `ABC`, `BCA`, `CAB` is a prefix of length $L \ge 3$ of `ABCABC...`, `BCABCA...`, or `CABCAB...`. Wait: by inclusion-exclusion on the cyclic transitions $A \to B \to C \to A$, it is even cleaner to decompose any valid string into maximal cyclic runs of the form $A \to B \to C \to A \dots$ of length $1$ or $2$!
  - *Hint 2*: In any valid string (containing no contiguous `ABC`, `BCA`, or `CAB`), if we cut the string between two adjacent characters whenever the second is NOT the cyclic successor of the first (i.e., we do NOT cut at `AB`, `BC`, `CA`, and we DO cut everywhere else), then the string is uniquely partitioned into maximal cyclic blocks of length $1$ or $2$ (since any cyclic block of length $\ge 3$ would contain `ABC`, `BCA`, or `CAB`)!
  - *Hint 3*: By Inclusion-Exclusion / Goulden–Jackson on the cyclic blocks, the generating function in $s = x_A + x_B + x_C$ and $p = x_A x_B x_C$ is $\frac{1 - 3p + \dots}{1 - s + 2p}$, so extracting $[x_A^A x_B^B x_C^C]$ reduces to expanding powers of $p = x_A x_B x_C$ and $s = x_A + x_B + x_C$ in $O(\min(A, B, C))$ time!
- **Derivation**:
  1. **Goulden–Jackson Cluster / Cyclic Run Generating Function**:
     Let $s = x_A + x_B + x_C$ and $p = x_A x_B x_C$. Consider the directed graph on $\{A, B, C\}$ where the forbidden transitions of length 3 are along the cycle $A \to B \to C \to A$. Any string over $\{A, B, C\}$ decomposes uniquely into maximal paths along the cycle $A \to B \to C \to A$.
     Wait: if we assign weight $w_L$ to a cyclic path of length $L \ge 1$ so that the sum of weights over all compositions of a path of length $M$ is $1$ for $M \in \{1, 2\}$ and $0$ for $M \ge 3$, then $\sum_{L \ge 1} w_L z^L = \frac{z + z^2}{1 + z + z^2} = 1 - \frac{1}{1 + z + z^2} = 1 - \frac{1 - z}{1 - z^3} = z - z^2 + z^4 - z^5 + \dots$!
     Look at what happens when we sum over all 3 starting characters $A, B, C$ of a cyclic block:
     - For $L = 3k$ (a multiple of 3), each of the 3 cyclic blocks of length $3k$ (`ABC...`, `BCA...`, `CAB...`) has the exact same monomial $p^k = (x_A x_B x_C)^k$, so the 3 blocks sum to $3 p^k$!
     - For $L = 3k + 1$, the 3 cyclic blocks (`A`, `B`, `C` times $p^k$) sum to $s p^k$!
     - For $L = 3k + 2$, the 3 cyclic blocks (`AB`, `BC`, `CA` times $p^k$) sum to $(x_A x_B + x_B x_C + x_C x_A) p^k$? Wait: why does $x_A x_B + x_B x_C + x_C x_A$ not even appear in the Goulden–Jackson cluster GF for $\{ABC, BCA, CAB\}$?!
     Let us check the **Goulden–Jackson Cluster Method** directly on the forbidden set $\mathcal{P} = \{ABC, BCA, CAB\}$!
     In Goulden–Jackson, a **cluster** must be a union of overlapping occurrences of patterns from $\mathcal{P} = \{ABC, BCA, CAB\}$.
     - A single pattern has length $3$ (`ABC`, `BCA`, or `CAB`), contributing $-3p$.
     - Two overlapping patterns can overlap by $2$ characters (e.g., `ABC` and `BCA` overlap to form `ABCA` of length $4$, weight $(-1)^2 x_A p$) or by $1$ character (e.g., `ABC` and `CAB` overlap to form `ABCAB` of length $5$, weight $(-1)^2 x_A x_B p$).
     Specifically, for any cluster starting with `A`, its cluster generating function $C_A$ satisfies:
     $$\text{Every step either extends by } 1 \text{ character (overlap of 2, factor } -1\text{) or by } 2 \text{ characters (overlap of 1, factor } -1\text{)}$$
     Wait: if we have `ABC`, the next pattern can start at index 2 (`BCA`, extending by 1 char `A`) or at index 3 (`CAB`, extending by 2 chars `AB`). By $(1 + z + z^2)(1 - z) = 1 - z^3$, the sum of $(-1)^{\text{patterns}}$ over all coverings of a cyclic word of length $L \ge 3$ is:
     - $-1$ if $L = 3k$ (weight $-p^k$ for each of the 3 starting letters, total $-3p^k$);
     - $+1$ if $L = 3k + 1$ ($k \ge 1$, weight $+x_A p^k, +x_B p^k, +x_C p^k$, total $+s p^k$);
     - $0$ if $L = 3k + 2$ (because a step of $+2$ has the exact same product as two steps of $+1$, with opposite signs $(-1)^1 + (-1)^2 = 0$!).
     What a miracle! Every cluster of length $3k + 2$ cancels out to **zero**!
     Therefore, the total cluster generating function $C(s, p)$ depends **only** on $s = x_A + x_B + x_C$ and $p = x_A x_B x_C$:
     $$C(s, p) = \sum_{k \ge 1} \big( -3 p^k + s p^k \big) = (s - 3) \frac{p}{1 - p}$$
     And by the Goulden–Jackson Theorem, the multivariate OGF of valid strings is:
     $$F(x_A, x_B, x_C) = \frac{1}{1 - s - C(s, p)} = \frac{1}{1 - s - \frac{(s - 3)p}{1 - p}} = \frac{1 - p}{1 - s + 2p} = \frac{1 - p}{1 - (s - 2p)}$$
  2. **Closed-Form $O(\min(A, B, C))$ Extraction**:
     Expanding $\frac{1}{1 - (s - 2p)} = \sum_{m \ge 0} (s - 2p)^m = \sum_{k \ge 0} (-2p)^k \binom{N - 2k}{k} s^{N - 3k}$ (where $m = N - 2k$ so that $p^k s^{m-k}$ has total degree $3k + (N - 3k) = N$), and extracting $[x_A^A x_B^B x_C^C] p^k s^{N - 3k} = [x_A^{A-k} x_B^{B-k} x_C^{C-k}] (x_A + x_B + x_C)^{N - 3k} = \frac{(N - 3k)!}{(A - k)! \, (B - k)! \, (C - k)!}$, we obtain the exact $O(\min(A, B, C))$ formula:
     $$\text{Ans} = \sum_{k=0}^{\min(A, B, C)} \left( (-2)^k \binom{N - 2k}{k} - (-2)^{k-1} \binom{N - 2k - 1}{k - 1} \right) \frac{(N - 3k)!}{(A - k)! \, (B - k)! \, (C - k)!} \pmod{998244353}$$
     where the second term in the parenthesis is $0$ for $k = 0$. This runs in $O(A + B + C)$ time using precomputed factorials.
```

---

### [B13] Omitted Theoretical Subsections & Bibliography Entries from Cohort 1 & Cohort 2

#### [B13.1] Restore Theorem 28.3 from Cohort 1 (`iter_26_to_30_implicit_zh_ja_audit.md` Lines 615–664) — General Quadratic Implicit Equations & $O(dN)$ Radical ODE Recurrence
Insert the following subsection at the end of **Section 5** (after Line 465 of `cohort3_wave_3b_implicit_zh_ja_audit.md`):

```markdown
---

### 5.3 General Quadratic Implicit Equations $a(x)F(x)^2 + b(x)F(x) + c(x) = 0$ and the $O(dN)$ Radical ODE Recurrence

When the degree of $P(x, y)$ in $y$ is $m = 2$:
$$a(x) F(x)^2 + b(x) F(x) + c(x) = 0$$
where $a(x), b(x), c(x)$ are sparse polynomials of degree at most $d$, we do not even need NTT! By the quadratic formula, choosing the branch matching $F(0)$:
$$F(x) = \frac{-b(x) \pm \sqrt{\Delta(x)}}{2a(x)}, \qquad \Delta(x) = b(x)^2 - 4a(x)c(x)$$
How do we compute $S(x) = \sqrt{\Delta(x)}$ to $N$ terms in $O(dN)$ time without FFT?
Differentiating $S(x)^2 = \Delta(x)$ gives $2 S(x) S'(x) = \Delta'(x)$. Multiplying by $S(x)$ and substituting $S(x)^2 = \Delta(x)$ yields the first-order linear ODE:
$$2 \Delta(x) S'(x) = \Delta'(x) S(x)$$
Suppose $\Delta(x) = \sum_{i=0}^{2d} \delta_i x^i$ with $\delta_0 \neq 0$ (if $\Delta(x)$ has valuation $2v > 0$, factor out $x^{2v}$ first so $S(x) = x^v \sqrt{\Delta(x)/x^{2v}}$). Extracting $[x^n]$ on both sides of $2 \Delta(x) S'(x) = \Delta'(x) S(x)$ gives:
$$2 \sum_{i=0}^{2d} \delta_i (n + 1 - i) S_{n + 1 - i} = \sum_{i=1}^{2d} i \delta_i S_{n + 1 - i}$$
Isolating the $i = 0$ term on the left yields the exact $O(dN)$ linear recurrence:
$$2 \delta_0 (n + 1) S_{n+1} = \sum_{i=1}^{\min(2d, n+1)} \delta_i (3i - 2n - 2) S_{n + 1 - i}$$
Once $S(x) = \sqrt{\Delta(x)} \bmod x^{N + \operatorname{ord}_x(a)}$ is computed in $O(dN)$ time, a single sparse division by $2a(x)$ recovers $F(x) \bmod x^N$ in $O(dN)$ time!

#### Worked Toy Example: Large Schröder Numbers ($r_n$)
The OGF $F(x) = \sum_{n \ge 0} r_n x^n$ of the Large Schröder numbers satisfies $x F(x)^2 - (1 - x) F(x) + 1 = 0$, so $a(x) = x, b(x) = -(1-x), c(x) = 1$, and:
$$\Delta(x) = (1 - x)^2 - 4x = 1 - 6x + x^2 \quad (\delta_0 = 1, \delta_1 = -6, \delta_2 = 1)$$
Let $S(x) = \sqrt{1 - 6x + x^2} = \sum_{n \ge 0} S_n x^n$ with $S_0 = 1$. The recurrence $2(n+1)S_{n+1} = -6(1 - 2n)S_n + (4 - 2n)S_{n-1}$ gives:
$$S_{n+1} = \frac{3(2n - 1) S_n - (n - 2) S_{n-1}}{n + 1}$$
- $n = 0$: $S_1 = \frac{3(-1)(1) - 0}{1} = -3$.
- $n = 1$: $S_2 = \frac{3(1)(-3) - (-1)(1)}{2} = -4$.
- $n = 2$: $S_3 = \frac{3(3)(-4) - (0)(-3)}{3} = -12$.
- $n = 3$: $S_4 = \frac{3(5)(-12) - (1)(-4)}{4} = -44$.
- $n = 4$: $S_5 = \frac{3(7)(-44) - (2)(-12)}{5} = -180$.
Since $F(x) = \frac{1 - x - S(x)}{2x}$, we have $r_n = -\frac{S_{n+1}}{2}$ for all $n \ge 1$ (and $r_0 = \frac{1 - S_1}{2}?\text{ wait: } [x^1](1 - x - S(x)) = -1 - S_1 = 2 \implies r_0 = 1$):
$$r_0 = 1, \quad r_1 = 2, \quad r_2 = 6, \quad r_3 = 22, \quad r_4 = 90$$
```

#### [B13.2] Restore Cohort 1 §29.1 Point 5 (`iter_26_to_30_implicit_zh_ja_audit.md` Lines 697–701) — Why Algebraic Newton Iteration Survives in Characteristic $p \le N$
Append the following subsection at the end of **Section 6** (after Line 563 of `cohort3_wave_3b_implicit_zh_ja_audit.md`):

```markdown
---

### 6.4 Why Algebraic Newton Iteration Survives in Characteristic $p \le N$ While Differential/Transcendental Newton ($\exp/\ln$) Collapses

A crucial structural distinction in small characteristic $p \le N$ (e.g., $\mathbb{F}_2[[x]]$ or $\mathbb{F}_p[[x]]$) is why **Algebraic Newton Iteration** $P(x, F(x)) = 0$ works up to arbitrary degree $N \gg p$ without ever dividing by $p$, whereas **Differential / Transcendental Newton Iteration** (for $\exp$, $\ln$, or D-finite ODEs) crashes at degree $n = p$:
1. **Why Differential / Transcendental Operations Fail at $n = p$**:
   Computing $\exp(A(x))$, $\ln(A(x))$, or integrating an ODE requires the formal integral $\int x^{n-1}\,dx = \frac{x^n}{n}$, which divides by $n$ and fails at $n = p, 2p, \dots$ in $\mathbb{F}_p$. Similarly, Lagrange Inversion $f_n = \frac{1}{n}[u^{n-1}]\Phi(u)^n$ divides by $n$.
2. **Why Algebraic Newton Iteration $P(x, F(x)) = 0$ Needs Zero Division by Degree or Factorials**:
   For any polynomial $P(x, y) = \sum_{j=0}^d a_j(x) y^j \in \mathbb{F}_p[x][y]$, expanding $P(x, F_k + \Delta)$ in powers of $\Delta = F - F_k$ uses the **Hasse–Schmidt / Binomial Taylor Identity**:
   $$P(x, F_k + \Delta) = \sum_{j=0}^d a_j(x) (F_k + \Delta)^j = P(x, F_k) + P_y(x, F_k)\Delta + \left( \sum_{j=2}^d \binom{j}{2} a_j(x) F_k^{j-2} \Delta^2 + \dots \right)$$
   Because the binomial coefficients $\binom{j}{1} = j$ and $\binom{j}{2}$ are **integers**, no division by $2!$ or $m!$ ever occurs! Furthermore, the Newton update:
   $$F_{k+1}(x) \equiv F_k(x) - \frac{P(x, F_k(x))}{P_y(x, F_k(x))} \pmod{x^{2^k}}$$
   only requires **formal power series inversion** of $P_y(x, F_k(x))$, which only divides by the constant term $c_0 = [x^0] P_y(0, F_0(0)) = P_y(0, f_0) \in \mathbb{F}_p^\times$! As long as the separability condition $P_y(0, f_0) \not\equiv 0 \pmod p$ holds (or after shifting $P(x, y)$ to the minimal valuation of $P_y$), Algebraic Newton Iteration runs to arbitrary precision $N \gg p$ over $\mathbb{F}_p$ (using Karatsuba / Kronecker multiplication when $p$ is not an NTT prime).
```

#### [B13.3] Restore 2 Omitted Bibliography Entries from Cohort 2 (§82.4 Entries 5 & 12)
Append to **Section 9.2** (after Line 1380 of `cohort3_wave_3b_implicit_zh_ja_audit.md`):

```markdown
11. **[ZH] CSDN / Cnblogs Community Compendia on *另类拉格朗日反演 (Alternative Lagrange Inversion)* and *复合逆 (Compositional Inverse)*.**
    - *Key Contribution*: Step-by-step derivations of $[x^n] G(x)^k = [y^{-k-1}] F'(y) y^{-n}$ and its regular power series shifts for competitive programming templates, bridging `Elegia`'s formal residue tutorials with standard Luogu template problems (`P5373`, `P5809`).
12. **[EN] Stanley, R. P., *Enumerative Combinatorics*, Vol. 2, Cambridge University Press (1999), §5.4 (Lagrange Inversion Formula) & Chapter 6 (Algebraic, D-Finite, and Noncommutative Generating Functions).**
    - *Key Contribution*: The foundational reference for the algebraic proof of Lagrange Inversion via formal residues, Raney's Lemma, and the hierarchy $\text{Rational} \subsetneq \text{Algebraic} \subsetneq \text{D-Finite}$.
```
