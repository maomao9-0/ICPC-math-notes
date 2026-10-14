# Audit Report B (Independent Second-Pass): Wave 1B — Combinatorial-to-GF Modelling, Mechanical DP-to-GF Conversion, Binomial Sum Untangling & Hidden Convolutions

**Target File**: [`cohort3_wave_1b_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md) (1,926 lines)  
**Source Files Audited Against**:
1. **Cohort 1**: [`iter_06_to_10_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_06_to_10_dp_and_sums.md) (1,493 lines)
2. **Cohort 2**: [`cohort2_iter_58_to_62_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_58_to_62_dp_and_sums.md) (1,381 lines)
3. **Prior Audit (Inspector A)**: [`audit_A_wave_1b.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/audit/audit_A_wave_1b.md) (626 lines)

**Auditor**: Principal Mathematical & Pedagogical Auditor (Inspector B — Independent Redundant Pass)  
**Audit Verdict**: **CONDITIONAL PASS PENDING REMEDIATION** — The compiled manuscript [`cohort3_wave_1b_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md) successfully synthesizes the 5-archetype ring taxonomy, Iverson-bracket protocol, Snake Oil vs. Egorychev dual framework, and 27 accepted contest problems, and contains **zero** forbidden `\(...\)` or `\[...\]` delimiters. However, this independent second-pass audit uncovered **10 new mathematical, C++ buffer-overflow, editorial, and source-loss defects** missed by Inspector A, **AND caught 2 critical errors inside Inspector A's own proposed replacements (`audit_A_wave_1b.md` Defects 1.1 and 1.2)** where Inspector A used hallucinated problem statements for `AtCoder JSC 2019 Qual F` and `AtCoder AISing 2020 F`. Every replacement block below has been verified against official AtCoder problem statements and sample test cases via Python scripts.

---

## Executive Summary of Inspector B Findings

1. **Critical Corrections to Inspector A's Report (`audit_A_wave_1b.md` Defects 1.1 & 1.2)**:
   - **Problem 15 (`AtCoder JSC 2019 Qual F — Candy Retribution`, Lines 1500–1528)**:
     - **Inspector A Error**: In `audit_A_wave_1b.md` (Defect 1.1), Inspector A claimed that `JSC 2019 Qual F` asks for sequences where "the sum of the $M$ largest elements of $A$ lies in $[L, R]$ and all elements sum to $S$". Fetching the live AtCoder task statement (`https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_f`) proves that `cohort3_wave_1b_dp_and_sums.md` Lines 1503–1504 already had the **exact official problem statement**: count sequences $A_1, \dots, A_N \ge 0$ with $L \le \sum_{i=1}^N A_i \le R$ such that when sorted in non-increasing order $B_1 \ge \dots \ge B_N$, we have $B_M = B_{M+1}$. **Do NOT apply Inspector A's fake problem statement for Problem 15!**
     - **True Defects in `cohort3_wave_1b_dp_and_sums.md` Lines 1506–1528**:
       1. Lines 1506 and 1510 write the unsubtracted OGF $x^{M(t+1)}(1-x)^{-M}\left(\frac{1-x^{t+1}}{1-x}\right)^{N-M}$, which overcounts sequences with $B_M - B_{M+1} \ge 2$ by a factor of $B_M - B_{M+1}$.
       2. Line 1514 leaves a raw conversational self-correction (`"Wait: for a given sorted tuple..."`) that contradicts Lines 1506 and 1510.
       3. Line 1523 defines $H(B, t)$ with only **one** threshold parameter $t$ (`for M elements >= t and N-M elements <= t`), which cannot represent either $H(B, t+1, t) - H(B, t+2, t)$ or $H(B, t+1, t) - H(B, t+1, t-1)$, and truncates without writing the final answer formula!
     - **Verified Fix (Defect B.1 below)**: Uses the 2-parameter helper $H(S, a, b) = [x^S] \frac{x^{Ma}(1-x^{b+1})^{N-M}}{(1-x)^{N+1}}$, verified against all 3 official AtCoder samples (`Sample 1: 4 2 3 7 -> 105`, `Sample 2: 2 1 4 8 -> 3`, `Sample 3: 141592 6535 89793 238462 -> 933832916`).
   - **Problem 22 (`AtCoder AISing 2020 F — Two Snuke`, Lines 1739–1760)**:
     - **Cohort 1, Cohort 2, Cohort 3, AND Inspector A Error**: Cohort 1 (`iter_06_to_10` Problem 17) hallucinated "every $n_i - s_i$ is odd"; Cohort 2 (`cohort2_iter_58_to_62` Problem 13) and Inspector A (`audit_A_wave_1b.md` Defect 1.2) hallucinated "20 integers with weight $\prod (n_{2i-1}-s_{2i-1}+n_{2i}-s_{2i}+1)$"; Cohort 3 (Lines 1739–1760) pasted both hallucinated versions side by side as "Version A" and "Version B"!
     - **True Official Statement & Verified Formula (Defect B.2 below)**: Fetching `https://atcoder.jp/contests/aising2020/tasks/aising2020_f` shows that **Two Snuke** chooses 10 integers $(s_1, s_2, n_1, n_2, u_1, u_2, k_1, k_2, e_1, e_2)$ (two copies of the letters `s, n, u, k, e`) satisfying $0 \le x_1 < x_2$ for each letter $x \in \{s,n,u,k,e\}$ and $\sum (x_1 + x_2) \le N$, weighted by $\prod_{x \in \{s,n,u,k,e\}} (x_2 - x_1) \bmod (10^9 + 7)$. Each pair $(x_1, x_2)$ has $x_1 \ge 0$ and $d = x_2 - x_1 \ge 1$ with sum $2x_1 + d$, giving single-pair OGF $A(z) = \frac{z}{(1-z^2)(1-z)^2}$ and total answer:
       $$\text{Ans}(N) = [z^N] \frac{1}{1-z} A(z)^5 = [z^N] \frac{z^5}{(1-z)^{11}(1-z^2)^5} = [z^{N-5}] \frac{(1+z)^{11}}{(1-z^2)^{16}} = \sum_{\substack{0 \le j \le 11 \\ j \equiv N-5 \pmod 2}} \binom{11}{j} \binom{\frac{N-5-j}{2} + 15}{15},$$
       verified against all 4 official sample cases (`N = 4 -> 0`, `N = 6 -> 11`, `N = 10 -> 4598`, `N = 10^9 -> 257255556`).

2. **New Defects Found by Inspector B (Missed by Inspector A)**:
   - **Defect B.3 (C++ Out-of-Bounds Buffer Overflow at $D = 21$ & Redundant $O(D 2^D)$ Inverse Loop in `sps_ln` / `sps_exp`, Lines 358–413)**: Section 2.1 (Line 53) and Section 2.6 (Line 305) state $d \le 21$, but `sps_ln` and `sps_exp` allocate `array<long long, 21>` (valid indices `0..20`) and index `p[k]`, `ln_p[k]`, `exp_p[k]` up to `k = D = 21`, causing **stack buffer overflow / undefined behavior** when $D = 21$. In addition, `sps_ln` (Line 376) recomputes the modular inverse table `inv[1..D]` inside the `2^D` mask loop instead of once outside the loop.
   - **Defect B.4 (Stream-of-Consciousness `"wait: let us check carefully!"` & False Chirp Identity in Section 4.4, Line 590)**: Line 590 states `(or ij = \binom{i}{2} + \binom{j}{2} - \binom{i-j}{2})` and then writes `"wait: let us check carefully!"` before showing that expression equals $ij - j \neq ij$.
   - **Defect B.5 (Stream-of-Consciousness `"wait: C(x) - xC(x)^2 = 1!"` inside Master Kernel Table K4, Line 706)**: Line 706 contains raw self-correction inside the Markdown table cell.
   - **Defect B.6 (Omitted 2D Row-to-Row Shift & Differential Operator Dictionary Table from `iter_06_to_10_dp_and_sums.md` Lines 410–420)**: The 7-row operator dictionary translating 2D DP recurrence terms into algebraic/differential operators on $F_{n-1}(y)$ was dropped prior to Section 6.5.
   - **Defect B.7 (Omitted Eulerian Recurrence Origin, $N=3$ Toy Trace $F_3(y) = 1 + 4y + y^2$, and Infinite-Series Truncation Pitfall in Section 6.5 from `iter_06_to_10_dp_and_sums.md` Lines 424–468)**: Section 6.5 omits the explicit 2D Eulerian recurrence $dp[n][k] = (k+1)dp[n-1][k] + (n-k)dp[n-1][k-1]$, the $N=3$ toy trace, and the truncation warning for $G_0(y) = \frac{F_0(y)}{1-y} \bmod y^{N+1}$.
   - **Defect B.8 (Omitted Case 2 of 2D Random Walk Decoupling $P(x,y) = A(x)B(y) - c$ from `iter_06_to_10_dp_and_sums.md` Lines 485–488 in Section 4.6)**: Section 4.6 omits the Binomial Theorem decoupling trick for coupled 2D steps like King/Delannoy walks $x + y + xy = (1+x)(1+y) - 1$.
   - **Defect B.9 (Omitted $w = 0$ Zero-Weight Division Pitfall in Section 3.2 from `iter_06_to_10_dp_and_sums.md` Line 391)**: Section 3.2 omits the warning that weight-$0$ items $(1 + cx^0)$ cannot be multiplied/divided via the shift loop `for (int j = w; j <= K; ++j)` and must scale the array by $(1+c)^{\pm 1} \pmod p$.
   - **Defect B.10 (Inexact Title & Missing Product $\prod_{i=1}^N$ in Problem 10 `AtCoder ARC 012 D`, Lines 1344–1366, and Official Constraints in Problem 1 `AtCoder fps-24 A`, Line 1079)**: Clarifies the official title (`Don't worry. Be Together`), coordinates $|x_i|, |y_i| \le 10^6$, and explicit product $\prod_{i=1}^N \binom{T}{\frac{T+x_i+y_i}{2}}\binom{T}{\frac{T+x_i-y_i}{2}} \bmod M$ in Problem 10, plus $D \le 2 \cdot 10^5, N \le 10^6$ in Problem 1.

3. **Confirmation of Inspector A's Remaining Valid Fixes**:
   - All other fixes in `audit_A_wave_1b.md` (removing `"Wait!"` on Line 136; restoring the $O(K^2)$ Stirling DP in Problem 12 `CF 932E` on Lines 1396–1420; restoring the 3 missing bibliography items and 2 missing rejected templates in Section 7; and restoring the worked toy traces for Sections 3.2, 4.1, 4.2, 4.5, 5.6.4, and 6.2) are mathematically sound and verified.

---

## Part 1: Critical Mathematical, Code & Problem Remediation Blocks (Inspector B)

### Defect B.1: Problem 15 (`AtCoder JSC 2019 Qual F — Candy Retribution`) — Contradictory Hint/Scratchpad, 1-Parameter Helper Bug & Correction to `audit_A_wave_1b.md` Defect 1.1
- **Location**: [`cohort3_wave_1b_dp_and_sums.md` Lines 1500–1528](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1500-L1528)
- **Mathematical Diagnosis**:
  1. **Warning on `audit_A_wave_1b.md` Defect 1.1**: Inspector A misread `JSC 2019 Qual F` and proposed replacing Problem 15 with a fabricated problem statement ("sum of the $M$ largest elements lies in $[L, R]$"). The official AtCoder statement (`https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_f`) matches Lines 1503–1504 of `cohort3_wave_1b_dp_and_sums.md`: count sequences $A_1, \dots, A_N \ge 0$ with $L \le \sum_{i=1}^N A_i \le R$ such that when sorted in non-increasing order $B_1 \ge \dots \ge B_N$, we have $B_M = B_{M+1}$.
  2. **Bugs in `cohort3_wave_1b_dp_and_sums.md` Lines 1506–1528**:
     - Lines 1506 and 1510 claim that for a fixed $t$, sequences with $B_M > t \ge B_{M+1}$ have OGF $x^{M(t+1)}(1-x)^{-M}\left(\frac{1-x^{t+1}}{1-x}\right)^{N-M}$, forgetting that summing over $t \ge 0$ counts any sequence with $B_M > B_{M+1}$ a total of $(B_M - B_{M+1})$ times unless we restrict to the disjoint events $[B_M = t+1 \text{ and } B_{M+1} \le t]$ (or equivalently $[B_M \ge t+1 \text{ and } B_{M+1} = t]$).
     - Line 1514 contains the raw self-correction `"Wait: for a given sorted tuple B_1 >= ... >= B_N, how many sequences have B_M > t >= B_{M+1}?"`.
     - Line 1523 defines $H(B, t)$ with only one parameter $t$ (`for M elements >= t and N-M elements <= t`), which cannot evaluate either $H(B, t+1, t) - H(B, t+2, t)$ or $H(B, t+1, t) - H(B, t+1, t-1)$, and omits the final answer formula!
- **Deterministic Drop-In Replacement for Lines 1500–1528**:
```markdown
#### Problem 15: AtCoder JSC 2019 Qual F — Candy Retribution (Advanced)
- **Metadata**: AtCoder `jsc2019_qual_f` | **Difficulty Tier**: `Advanced` | **Archetype**: Complementary Counting + Bounded Knapsack OGF + Harmonic Summation $O(R \log R)$ (Sections 3.2 & 4.5)
- **Direct URL**: `https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_f`
- **Mathematical Statement & Constraints**:
  Count sequences of $N$ non-negative integers $(A_1, \dots, A_N)$ such that $L \le \sum_{i=1}^N A_i \le R$ and, when sorted in non-increasing order $B_1 \ge B_2 \ge \dots \ge B_N$, the $M$-th and $(M+1)$-th elements are equal ($B_M = B_{M+1}$), modulo $10^9 + 7$.
  **Constraints**: $1 \le M < N \le 3 \cdot 10^5$, $1 \le L \le R \le 3 \cdot 10^5$. Target complexity: $O(N + R \log R)$.
- **Diagnostic Signal & Modelling Bridge**:
  Directly enforcing $B_M = B_{M+1} = t$ allows other elements to also equal $t$, making the multinomial symmetry factor depend on the multiplicities of $t$ above and below index $M$. Instead, pass to the **complement** $B_M > B_{M+1}$! Every sequence with $B_M > B_{M+1}$ belongs to a **unique** threshold $t = B_M - 1 \ge 0$ for which $B_M = t + 1$ and $B_{M+1} \le t$ (or dual-equivalently, $t = B_{M+1} \ge 0$ for which $B_M \ge t + 1$ and $B_{M+1} = t$). Because there is a strict gap between the $M$ largest elements ($\ge t+1$) and the $N-M$ smallest elements ($\le t$), the $M$ indices of the largest elements are uniquely determined and can be chosen in $\binom{N}{M}$ ways!
- **Progressive 3-Tier Hints**:
  - *Hint 1 (Diagnostic Nudge)*: Subtract the count of sequences with $B_M > B_{M+1}$ from all sequences with sum in $[L, R]$. For a fixed $t \ge 0$, how can you express the disjoint event $[B_M = t+1 \text{ and } B_{M+1} \le t]$ as a difference of two simpler prefix/suffix value constraints?
  - *Hint 2 (GF Setup)*: Having $M$ chosen elements $\ge a$ and the remaining $N-M$ elements in $[0, b]$ has OGF $x^{Ma}(1-x)^{-M} \left(\frac{1-x^{b+1}}{1-x}\right)^{N-M} = \frac{x^{Ma}(1-x^{b+1})^{N-M}}{(1-x)^N}$. The event $[B_M = t+1 \text{ and } B_{M+1} \le t]$ is simply $(a = t+1, b = t)$ minus $(a = t+2, b = t)$!
  - *Hint 3 (Algebraic Manipulation)*: Multiply by $\frac{1}{1-x}$ to sum over total sums $\le S$, and expand $(1 - x^{t+1})^{N-M} = \sum_{j=0}^{N-M} (-1)^j \binom{N-M}{j} x^{j(t+1)}$. Since $M(t+1) + j(t+1) \le S \implies (M+j)(t+1) \le S$, how many $(t, j)$ pairs have non-zero contribution across all $t \ge 0$? By the harmonic series, at most $\sum_{t \ge 1} \frac{S}{t} = O(S \log S)$ pairs!
- **Complete Algebraic Derivation & Solution**:
  For any upper sum bound $S \ge 0$, the total number of sequences $A \in \mathbb{Z}_{\ge 0}^N$ with $\sum_{i=1}^N A_i \le S$ is $[x^S] \frac{1}{(1-x)^{N+1}} = \binom{S+N}{N}$.
  For integers $a \ge 1$ and $b \ge 0$, define $H(S, a, b)$ to be the number of sequences where a fixed subset of $M$ elements are $\ge a$, the remaining $N-M$ elements are in $[0, b]$, and the total sum is $\le S$:
  $$\begin{aligned}
  H(S, a, b) &= [x^S] \frac{1}{1 - x} \left( \frac{x^a}{1 - x} \right)^M \left( \frac{1 - x^{b+1}}{1 - x} \right)^{N-M} \\
  &= [x^{S - Ma}] \frac{(1 - x^{b+1})^{N-M}}{(1 - x)^{N+1}} \\
  &= \sum_{j=0}^{\min\left(N-M, \, \lfloor \frac{S - Ma}{b+1} \rfloor\right)} (-1)^j \binom{N - M}{j} \binom{S - Ma - j(b+1) + N}{N},
  \end{aligned}$$
  with $H(S, a, b) = 0$ whenever $S < Ma$ or $b < 0$.
  For each $t \ge 0$, a sequence satisfies $B_M = t + 1$ and $B_{M+1} \le t$ if and only if its $M$ largest elements are $\ge t + 1$ (but not all $\ge t + 2$) and its $N - M$ smallest elements are $\le t$. Summing over all $0 \le t < \lfloor S / M \rfloor$:
  $$\text{Good}_{\le}(S) = \binom{S + N}{N} - \binom{N}{M} \sum_{t=0}^{\lfloor S/M \rfloor - 1} \left( H(S, t + 1, t) - H(S, t + 2, t) \right).$$
  *(Note: Dually, decomposing by $B_{M+1} = t$ and $B_M \ge t+1$ replaces the summand by $H(S, t+1, t) - H(S, t+1, t-1)$ and yields the exact same sum.)*
  Finally, the answer for $[L, R]$ is $(\text{Good}_{\le}(R) - \text{Good}_{\le}(L - 1)) \bmod (10^9 + 7)$, evaluated in $O(N + R \log R)$ time.
```

---

### Defect B.2: Problem 22 (`AtCoder AISing 2020 F — Two Snuke`) — Hallucinated Problem Statements in Cohort 1, Cohort 2, Cohort 3 & `audit_A_wave_1b.md` Defect 1.2
- **Location**: [`cohort3_wave_1b_dp_and_sums.md` Lines 1739–1760](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1739-L1760)
- **Mathematical Diagnosis**:
  1. Both "Version A" (from Cohort 1, claiming $n_i - s_i$ is odd) and "Version B" (from Cohort 2 and repeated in `audit_A_wave_1b.md` Defect 1.2, claiming 20 variables with weight $n_{2i-1}-s_{2i-1}+n_{2i}-s_{2i}+1$) are **hallucinated problem statements** that fail on the official AtCoder sample test cases (`N = 4 -> 0`, `N = 6 -> 11`, `N = 10 -> 4598`, `N = 10^9 -> 257255556`).
  2. The official AtCoder statement (`https://atcoder.jp/contests/aising2020/tasks/aising2020_f`) chooses 10 integers $(s_1, s_2, n_1, n_2, u_1, u_2, k_1, k_2, e_1, e_2)$ satisfying $0 \le x_1 < x_2$ for each of the 5 letters $x \in \{s, n, u, k, e\}$ and $\sum (x_1 + x_2) \le N$, and asks for the sum of $\prod_{x \in \{s,n,u,k,e\}} (x_2 - x_1) \bmod (10^9 + 7)$.
- **Deterministic Drop-In Replacement for Lines 1739–1760**:
```markdown
#### Problem 22: AtCoder AISing Programming Contest 2020 F — Two Snuke (Mastery)
- **Metadata**: AtCoder `aising2020_f` | **Difficulty Tier**: `Mastery` | **Archetype**: OGF Derivative Weighting + Parity Decomposition / Bostan-Mori (Sections 3.1, 4.3 & 6.4)
- **Direct URL**: `https://atcoder.jp/contests/aising2020/tasks/aising2020_f`
- **Mathematical Statement & Constraints**:
  Given an integer $N$, Snuke chooses 10 integers $(s_1, s_2, n_1, n_2, u_1, u_2, k_1, k_2, e_1, e_2)$ satisfying:
  - $0 \le s_1 < s_2$, $0 \le n_1 < n_2$, $0 \le u_1 < u_2$, $0 \le k_1 < k_2$, $0 \le e_1 < e_2$, and
  - $s_1 + s_2 + n_1 + n_2 + u_1 + u_2 + k_1 + k_2 + e_1 + e_2 \le N$.
  For every valid 10-tuple, compute $(s_2 - s_1)(n_2 - n_1)(u_2 - u_1)(k_2 - k_1)(e_2 - e_1)$, and find the sum of all computed values modulo $10^9 + 7$.
  **Constraints**: $1 \le T \le 100$ test cases, $1 \le N \le 10^9$. Target complexity: $O(1)$ (or $O(\log N)$ via Bostan-Mori) per testcase.
- **Diagnostic Signal & Modelling Bridge**:
  The 5 letter pairs $(s_1, s_2), (n_1, n_2), (u_1, u_2), (k_1, k_2), (e_1, e_2)$ are **completely independent** except that their total sum is $\le N$. For a single pair $(x_1, x_2)$ with $0 \le x_1 < x_2$, change variables to $x_1 \ge 0$ and $d = x_2 - x_1 \ge 1$. Then the pair's sum is $x_1 + x_2 = 2x_1 + d$ and its weight is $d$, so $x_1$ and $d$ decouple into a product of two univariate OGFs!
- **Progressive 3-Tier Hints**:
  - *Hint 1 (Diagnostic Nudge)*: For a single pair $(x_1, x_2)$ with $0 \le x_1 < x_2$, substitute $d = x_2 - x_1 \ge 1$ so that $x_1 + x_2 = 2x_1 + d$. What is the univariate OGF $A(z)$ for one pair weighted by $d$?
  - *Hint 2 (GF Setup)*: Summing independently over $x_1 \ge 0$ and $d \ge 1$ gives $A(z) = \left(\sum_{x_1=0}^\infty z^{2x_1}\right) \left(\sum_{d=1}^\infty d \, z^d\right) = \frac{1}{1 - z^2} \cdot \frac{z}{(1 - z)^2}$. Since there are 5 independent pairs and the total sum is $\le N$, the answer is $[z^N] \frac{1}{1 - z} A(z)^5 = [z^N] \frac{z^5}{(1 - z)^{11} (1 - z^2)^5}$.
  - *Hint 3 (Algebraic Manipulation)*: To make the denominator a function of $z^2$ alone (the single step of Bostan-Mori!), multiply numerator and denominator by $(1 + z)^{11}$ so $(1 - z)^{11}(1 + z)^{11} = (1 - z^2)^{11}$:
    $$\text{Ans}(N) = [z^{N-5}] \frac{(1 + z)^{11}}{(1 - z^2)^{16}},$$
    which expands into a finite sum of at most 6 binomial coefficients per testcase!
- **Complete Algebraic Derivation & Solution**:
  $$\begin{aligned}
  A(z) &= \left(\sum_{x_1=0}^{\infty} z^{2x_1}\right) \left(\sum_{d=1}^{\infty} d \, z^d\right) = \frac{1}{1 - z^2} \cdot \frac{z}{(1 - z)^2}, \\
  \text{Ans}(N) &= [z^N] \frac{1}{1 - z} A(z)^5 = [z^N] \frac{z^5}{(1 - z)^{11} (1 - z^2)^5} \\
  &= [z^{N - 5}] \frac{(1 + z)^{11}}{(1 - z)^{11} (1 + z)^{11} (1 - z^2)^5} = [z^{N - 5}] \frac{(1 + z)^{11}}{(1 - z^2)^{16}}.
  \end{aligned}$$
  Expanding $(1 + z)^{11} = \sum_{j=0}^{11} \binom{11}{j} z^j$ and $(1 - z^2)^{-16} = \sum_{m=0}^\infty \binom{m + 15}{15} z^{2m}$, only indices $0 \le j \le 11$ with $j \equiv N - 5 \pmod 2$ and $j \le N - 5$ contribute:
  $$\text{Ans}(N) = \sum_{\substack{0 \le j \le 11 \\ j \le N - 5, \, j \equiv N - 5 \pmod 2}} \binom{11}{j} \binom{\frac{N - 5 - j}{2} + 15}{15} \pmod{10^9 + 7}.$$
  *(Toy Check on Official Samples: for $N = 4$, $\text{Ans}(4) = 0$; for $N = 6$, $N - 5 = 1 \implies j = 1, m = 0 \implies \binom{11}{1}\binom{15}{15} = 11$; for $N = 10$, $N - 5 = 5 \implies j \in \{1, 3, 5\} \implies \binom{11}{1}\binom{17}{15} + \binom{11}{3}\binom{16}{15} + \binom{11}{5}\binom{15}{15} = 11(136) + 165(16) + 462(1) = 4598$.)*
```

---

### Defect B.3: C++ Stack Buffer Overflow at $D = 21$ & Redundant $O(D 2^D)$ Inverse Computation in `sps_ln` and `sps_exp`
- **Location**: [`cohort3_wave_1b_dp_and_sums.md` Lines 358–413](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L358-L413)
- **Code & Mathematical Diagnosis**:
  1. Both Table 2.1 (Line 53) and Section 2.6 (Line 305) specify ground sets of size $d \le 21$. However, `sps_ln` (Lines 366, 374) and `sps_exp` (Lines 394, 401) declare `array<long long, 21>` (valid indices `0..20`). When $D = 21$, `__builtin_popcount((1<<21)-1) == 21` and the inner loops `for (int k = 1; k <= D; ++k)` access index `21` of `hat[mask]`, `p`, `ln_p`, and `exp_p`, causing **Undefined Behavior / Stack Buffer Overflow**. The array capacity must be `22` (indices `0..21`).
  2. In `sps_ln` (Lines 375–376), the modular inverse array `inv[1..D]` is recomputed inside the `for (int mask = 0; mask < N; ++mask)` loop ($2^D$ times!), whereas `sps_exp` (Lines 397–399) properly precomputes `inv[1..D]` once outside the loop.
- **Deterministic Drop-In Replacement for Lines 358–413**:
```cpp
// Compute C(x) = ln G(x) in K[x_1..x_D]/(x_i^2) in O(D^2 2^D) time.
// Precondition: g[0] == 1, N == (1 << D) with D <= 21.
vector<long long> sps_ln(const vector<long long>& g) {
    int N = g.size();
    int D = __builtin_ctz(N);
    assert(D <= 21);
    // hat[mask][k] stores [t^k] of the ranked polynomial at subset 'mask'
    vector<array<long long, 22>> hat(N);
    for (int mask = 0; mask < N; ++mask) {
        hat[mask].fill(0);
        hat[mask][__builtin_popcount(mask)] = g[mask];
    }
    // 1. Forward Ranked FMT (OR-Zeta Transform)
    for (int i = 0; i < D; ++i)
        for (int mask = 0; mask < N; ++mask)
            if (mask & (1 << i))
                for (int k = 0; k <= D; ++k)
                    hat[mask][k] = (hat[mask][k] + hat[mask ^ (1 << i)][k]) % MOD;

    // Precompute modular inverses 1..D once outside the 2^D loop
    array<long long, 22> inv{};
    inv[1] = 1;
    for (int k = 2; k <= D; ++k)
        inv[k] = (MOD - MOD / k) * inv[MOD % k] % MOD;

    // 2. Pointwise truncated polynomial ln: P(t) = ln(A(t)) mod t^{D+1}
    // Using k * P_k = k * A_k - sum_{j=1}^{k-1} j * P_j * A_{k-j}
    for (int mask = 0; mask < N; ++mask) {
        auto& a = hat[mask];
        array<long long, 22> ln_a{};
        for (int k = 1; k <= D; ++k) {
            long long sum = 0;
            for (int j = 1; j < k; ++j)
                sum = (sum + 1LL * j * ln_a[j] % MOD * a[k - j]) % MOD;
            long long k_ln_k = (1LL * k * a[k] - sum + MOD) % MOD;
            ln_a[k] = k_ln_k * inv[k] % MOD;
        }
        a = ln_a;
    }

    // 3. Inverse Ranked FMT (OR-Mobius Transform)
    for (int i = 0; i < D; ++i)
        for (int mask = 0; mask < N; ++mask)
            if (mask & (1 << i))
                for (int k = 0; k <= D; ++k)
                    hat[mask][k] = (hat[mask][k] - hat[mask ^ (1 << i)][k] + MOD) % MOD;

    vector<long long> c(N, 0);
    for (int mask = 0; mask < N; ++mask)
        c[mask] = hat[mask][__builtin_popcount(mask)];
    return c;
}

// Compute G(x) = exp C(x) in K[x_1..x_D]/(x_i^2) in O(D^2 2^D) time.
// Precondition: c[0] == 0, N == (1 << D) with D <= 21.
vector<long long> sps_exp(const vector<long long>& c) {
    int N = c.size();
    int D = __builtin_ctz(N);
    assert(D <= 21);
    vector<array<long long, 22>> hat(N);
    for (int mask = 0; mask < N; ++mask) {
        hat[mask].fill(0);
        hat[mask][__builtin_popcount(mask)] = c[mask];
    }
    for (int i = 0; i < D; ++i)
        for (int mask = 0; mask < N; ++mask)
            if (mask & (1 << i))
                for (int k = 0; k <= D; ++k)
                    hat[mask][k] = (hat[mask][k] + hat[mask ^ (1 << i)][k]) % MOD;

    array<long long, 22> inv{};
    inv[1] = 1;
    for (int k = 2; k <= D; ++k)
        inv[k] = (MOD - MOD / k) * inv[MOD % k] % MOD;

    for (int mask = 0; mask < N; ++mask) {
        auto& p = hat[mask];
        array<long long, 22> exp_p{};
        exp_p[0] = 1;
        for (int k = 1; k <= D; ++k) {
            long long sum = 0;
            for (int j = 1; j <= k; ++j)
                sum = (sum + 1LL * j * p[j] % MOD * exp_p[k - j]) % MOD;
            exp_p[k] = sum * inv[k] % MOD;
        }
        p = exp_p;
    }

    for (int i = 0; i < D; ++i)
        for (int mask = 0; mask < N; ++mask)
            if (mask & (1 << i))
                for (int k = 0; k <= D; ++k)
                    hat[mask][k] = (hat[mask][k] - hat[mask ^ (1 << i)][k] + MOD) % MOD;

    vector<long long> g(N, 0);
    for (int mask = 0; mask < N; ++mask)
        g[mask] = hat[mask][__builtin_popcount(mask)];
    return g;
}
```

---

### Defect B.4: Stream-of-Consciousness `"wait: let us check carefully!"` & False Chirp Identity in Section 4.4 (Bluestein's CZT)
- **Location**: [`cohort3_wave_1b_dp_and_sums.md` Lines 590–596](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L590-L596)
- **Editorial & Mathematical Diagnosis**:
  Line 590 states `(or ij = \binom{i}{2} + \binom{j}{2} - \binom{i-j}{2})` and then immediately writes `"Since \binom{i}{2} + \binom{j}{2} - \binom{i-j}{2} = ... = ij - (i-j)... wait: let us check carefully!"` before proving that $\binom{i}{2} + \binom{j}{2} - \binom{i-j}{2} = ij - j \neq ij$. This violates the `AGENTS.md` prohibition on raw self-correction artifacts.
- **Deterministic Drop-In Replacement for Lines 590–596**:
```markdown
- **Chirp Identity**: Use either the symmetric sum-index binomial identity or the asymmetric difference-index binomial identity:
  $$ij = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}, \qquad \text{or} \qquad ij = \binom{i}{2} + \binom{j+1}{2} - \binom{i-j}{2}.$$
  *(Pitfall Warning: Do **not** write $\binom{i}{2} + \binom{j}{2} - \binom{i-j}{2}$ for the difference-index form! Expanding $\frac{i(i-1) + j(j-1) - (i-j)(i-j-1)}{2}$ yields $ij - j = j(i-1)$, which is off by $-j$; shifting $\binom{j}{2} \to \binom{j+1}{2}$ adds $+j$ and restores exact equality $ij$.)*
- **Reduction to Convolution**:
  $$y_i = c^{-\binom{i}{2}} \sum_{j=0}^{n-1} \left( a_j c^{-\binom{j}{2}} \right) c^{\binom{i+j}{2}} = c^{-\binom{i}{2}} [x^i] \text{ (via difference convolution of } u_j = a_j c^{-\binom{j}{2}} \text{ and } v_{k} = c^{\binom{k}{2}}\text{)},$$
  evaluating $A(x)$ at $m$ geometric points $1, c, c^2, \dots, c^{m-1}$ in a **single NTT**!
```

---

### Defect B.5: Stream-of-Consciousness `"wait: C(x) - xC(x)^2 = 1!"` inside Master Kernel Table K4
- **Location**: [`cohort3_wave_1b_dp_and_sums.md` Line 706](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L706)
- **Editorial Diagnosis**:
  Inside the Markdown table cell for **K4 (Central Binomial & Catalan)** on Line 706, the text reads: `Since $C(x) = 1 + x C(x)^2 \iff 1 - x C(x)^2 = 1 + x C(x)^2 - 2x C(x)^2 = C(x)(2 - C(x)) \dots$ wait: $C(x) - xC(x)^2 = 1$!`.
- **Deterministic Drop-In Replacement for Line 706**:
```markdown
| **K4. Central Binomial & Catalan** | $\binom{2k}{k}$ and $C_k = \frac{1}{k+1}\binom{2k}{k}$ | $\sum_{k=0}^\infty \binom{2k}{k} x^k = \frac{1}{\sqrt{1 - 4x}}, \quad C(x) = \sum_{k=0}^\infty C_k x^k = \frac{1 - \sqrt{1 - 4x}}{2x}$ | Furthermore, for any $m \ge 0$: $\sum_{k=0}^\infty \binom{2k + m}{k} x^k = \frac{C(x)^m}{\sqrt{1 - 4x}} = \frac{C(x)^{m+1}}{2 - C(x)} = \frac{C(x)^m}{1 - x C(x)^2}$. *(Proof of denominator identity: $C(x) = 1 + x C(x)^2 \implies x C(x) = \frac{C(x) - 1}{C(x)}$, so $\sqrt{1 - 4x} = 1 - 2x C(x) = \frac{2 - C(x)}{C(x)}$ and $\frac{1}{\sqrt{1 - 4x}} = \frac{C(x)}{2 - C(x)} = \frac{1}{1 - x C(x)^2}$.)* |
```

---

## Part 2: Zero-Information-Loss Restoration Blocks (Missed by Inspector A)

### Defect B.6 & B.7: Omitted 2D Row-to-Row Shift/Differential Operator Dictionary Table, Eulerian Recurrence Origin, $N=3$ Toy Trace & Truncation Pitfall in Section 6.5
- **Source**: [`iter_06_to_10_dp_and_sums.md` Lines 406–468](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_06_to_10_dp_and_sums.md#L406-L468)
- **Target Location in Cohort 3**: [`cohort3_wave_1b_dp_and_sums.md` Lines 1004–1020 (Section 6.5)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1004-L1020)
- **Diagnosis**:
  Section 6.5 in `cohort3_wave_1b_dp_and_sums.md` dropped:
  1. The 7-row **Dictionary of 2D Row-to-Row Operators ($F_{n-1}(y) \mapsto F_n(y)$)** from `iter_06_to_10_dp_and_sums.md` Lines 410–420.
  2. The explicit 2D Eulerian recurrence $dp[n][k] = (k+1)dp[n-1][k] + (n-k)dp[n-1][k-1]$ showing how the PDE operator $F_n(y) = (1 + (n-1)y)F_{n-1}(y) + y(1-y)F'_{n-1}(y)$ arises from the Operator Dictionary.
  3. The **Hand-Checkable Toy Example ($F_0(y) = 1, N = 3 \implies F_3(y) = 1 + 4y + y^2$)** (`iter_06_to_10` Lines 456–464).
  4. The **Truncation Pitfall** (`iter_06_to_10` Line 467) warning that $G_0(y) = \frac{F_0(y)}{1-y}$ is an infinite power series and must be expanded to $y^N$ before multiplying by $(m+1)^N$ and $(1-y)^{N+1} \bmod y^{N+1}$, as well as the $O(N)$ linear-time evaluation remark when multiplying by $(1-y)^{N+1}$ for $F_0(y)=1$ or via NTT for general $F_0(y)$.
- **Deterministic Drop-In Replacement for Lines 1004–1020**:
```markdown
### 6.5 2D Row-to-Row Differential Operators & `alpha1022`'s Eulerian PDE Trick

When a 2D DP has states $dp[n][k]$, we eliminate the inner loop over $k$ by forming the **Row Generating Function** $F_n(y) = \sum_{k} dp[n][k] y^k$ and translating index shifts and $k$-dependent coefficients into algebraic and differential operators on $F_{n-1}(y)$:

| 2D DP Term in Recurrence for $dp[n][k]$ | Effect on Monomial $y^k$ | Equivalent Operator on $F_{n-1}(y) = \sum_k dp[n-1][k] y^k$ |
| :--- | :--- | :--- |
| $dp[n-1][k]$ | $y^k \gets y^k$ | $1 \cdot F_{n-1}(y)$ |
| $dp[n-1][k - s]$ | $y^k \gets y^{k-s} \cdot y^s$ | $y^s F_{n-1}(y)$ |
| $dp[n-1][k + 1]$ | $y^k \gets y^{k+1} / y$ | $\frac{F_{n-1}(y) - F_{n-1}(0)}{y}$ |
| $k \cdot dp[n-1][k]$ | $k y^k = y \frac{d}{dy}(y^k)$ | $y \frac{d}{dy} F_{n-1}(y) = \vartheta_y F_{n-1}(y)$ |
| $(k + 1) \cdot dp[n-1][k + 1]$ | $(k+1) y^k = \frac{d}{dy}(y^{k+1})$ | $\frac{d}{dy} F_{n-1}(y)$ |
| $(n - k) \cdot dp[n-1][k - 1]$ | $(n - 1 - (k-1)) y^k$ | $y \left(n - 1 - y \frac{d}{dy}\right) F_{n-1}(y)$ |
| $\sum_{j=0}^{k} dp[n-1][j]$ (prefix sum in $k$) | $\sum_{k \ge j} y^k = \frac{y^j}{1-y}$ | $\frac{1}{1 - y} F_{n-1}(y)$ |

#### Diagonalizing the Eulerian Differential Operator $\mathcal{L}_n = (n-1)y + 1 + y(1-y)\frac{d}{dy}$
Consider the Eulerian recurrence (or its generalizations with arbitrary initial polynomial $F_0(y)$):
$$dp[n][k] = (k + 1) dp[n-1][k] + (n - k) dp[n-1][k-1].$$
Translating via the Operator Dictionary above yields the first-order differential recurrence on $F_{n-1}(y)$:
$$F_n(y) = (1 + y\frac{d}{dy}) F_{n-1}(y) + y\left(n - 1 - y\frac{d}{dy}\right) F_{n-1}(y) = \left( (n-1)y + 1 + y(1-y)\frac{d}{dy} \right) F_{n-1}(y).$$
- **Reverse-Engineering Scratchpad (Diagonalizing the Differential Operator)**:
  Why do $y$ and $y(1-y)\frac{d}{dy}$ mix adjacent powers of $y$? Because we are expanding in the wrong basis $y^m$! Let us test how the operator $\mathcal{L}_n = (n-1)y + 1 + y(1-y)\frac{d}{dy}$ acts on $B_{n-1, m}(y) = (1-y)^n y^m$:
  $$\begin{aligned}
  \mathcal{L}_n \left( (1-y)^n y^m \right) &= \left((n-1)y + 1\right)(1-y)^n y^m + y(1-y) \left[ -n(1-y)^{n-1} y^m + m(1-y)^n y^{m-1} \right] \\
  &= (1-y)^n y^m \left[ (n-1)y + 1 - n y + m(1-y) \right] \\
  &= (m + 1) (1-y)^{n+1} y^m = (m + 1) B_{n, m}(y)!
  \end{aligned}$$
  The basis $B_{n-1, m}(y) = (1-y)^n y^m$ **completely diagonalizes** the recurrence!
- **Algorithmic Pipeline ($O(N \log N)$ for general $F_0(y)$, or $O(N)$ for single coefficient / $F_0(y) = 1$)**:
  1. Divide the initial polynomial $F_0(y)$ (of degree $d$) by $(1-y)$ via a single prefix-sum sweep to obtain $G_0(y) = \frac{F_0(y)}{1-y} = \sum_{m=0}^\infty c_m y^m \bmod y^{N+d+1}$.
  2. After $N$ steps of the recurrence, each basis term $(1-y)^1 y^m$ is multiplied by $(m+1)^N$ and becomes $(1-y)^{N+1} y^m$:
     $$F_N(y) \equiv (1-y)^{N+1} \sum_{m=0}^{N+d} c_m (m+1)^N y^m \pmod{y^{N+d+1}},$$
     computable in $O(N \log N)$ via a single NTT (or $O(N)$ linear time for a single coefficient $[y^k]F_N(y)$!).
- **Hand-Checkable Toy Example ($F_0(y) = 1$, standard Eulerian numbers for $N = 3$)**:
  - $G_0(y) = \frac{1}{1-y} = \sum_{m \ge 0} 1 \cdot y^m$, so $c_m = 1$ for all $m \ge 0$.
  - Multiply $[y^m]$ by $(m+1)^3$: $1 + 8y + 27y^2 + 64y^3 + O(y^4)$.
  - Multiply by $(1-y)^4 = 1 - 4y + 6y^2 - 4y^3 + y^4$:
    - $[y^0]F_3 = 1$,
    - $[y^1]F_3 = 8 - 4(1) = 4$,
    - $[y^2]F_3 = 27 - 4(8) + 6(1) = 1$,
    - $[y^3]F_3 = 64 - 4(27) + 6(8) - 4(1) = 0$.
  - Thus $F_3(y) = 1 + 4y + y^2$, the exact Eulerian polynomial for $N = 3$!
- **Failure Mode / Truncation Pitfall**:
  - **Truncating $\frac{F_0(y)}{1-y}$ too early**: Even when $F_0(y) = 1$ has degree $0$, $G_0(y) = \frac{F_0(y)}{1-y}$ is an **infinite** power series! You must expand $G_0(y)$ up to $y^{N+d}$, scale the $m$-th coefficient by $(m+1)^N$, and only *then* multiply by $(1-y)^{N+1} \bmod y^{N+d+1}$.
```

---

### Defect B.8: Omitted Case 2 of 2D Random Walk Decoupling ($P(x, y) = A(x)B(y) - c$ via Binomial Theorem) in Section 4.6
- **Source**: [`iter_06_to_10_dp_and_sums.md` Lines 485–488](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_06_to_10_dp_and_sums.md#L485-L488)
- **Target Location in Cohort 3**: [`cohort3_wave_1b_dp_and_sums.md` Lines 649–660 (Section 4.6)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L649-L660)
- **Diagnosis**:
  Section 4.6 covers Case 1 (4-directional axial walk $x + x^{-1} + y + y^{-1} = (xy)^{-1}(1+xy)(x+y)$) but omits Case 2 from `iter_06_to_10_dp_and_sums.md` Lines 485–488: when a 2D walk polynomial $P(x, y)$ does not factor directly (such as a Delannoy walk $x + y + xy$ or King's walk $\sum_{dx,dy \in \{-1,0,1\}} x^{dx}y^{dy} - 1$), shifting by a constant $c$ so that $P(x, y) + c = A(x)B(y)$ decouples $x$ and $y$ via a single Binomial Theorem sum!
- **Deterministic Drop-In Replacement for Lines 649–660**:
```markdown
#### Archetype B: 2D Manhattan & Coupled Random Walks via Bivariate Factorization (`ARC 012 D`, `FPS 24 H`, `FPS 24 V`)
- **Case 1 (4-Directional Axial Walk $S(x, y) = x + x^{-1} + y + y^{-1}$ — Chebyshev $45^\circ$ Rotation)**:
  In $K[x^{\pm 1}, y^{\pm 1}]$, a single unit Manhattan step has Laurent polynomial $S(x, y) = x + x^{-1} + y + y^{-1}$. Factor it into two binomials:
  $$x + x^{-1} + y + y^{-1} = (xy)^{-1} (1 + xy)(x + y) = \left(x^{1/2} y^{1/2} + x^{-1/2} y^{-1/2}\right)\left(x^{1/2} y^{-1/2} + x^{-1/2} y^{1/2}\right)!$$
  Raising $S(x, y)$ to the $T$-th power completely decouples into two 1D binomials:
  $$[x^X y^Y] (x + x^{-1} + y + y^{-1})^T = [x^{X + T} y^{Y + T}] (1 + xy)^T (x + y)^T = \binom{T}{\frac{T + X + Y}{2}} \binom{T}{\frac{T + X - Y}{2}}!$$
  *(Combinatorially, rotating coordinates to $(u, v) = (x + y, x - y)$ turns each axial step $(\pm 1, 0), (0, \pm 1)$ into $(\Delta u, \Delta v) \in \{+1, -1\}^2$—two completely independent 1D walks in $u$ and $v$!)*
- **Case 2 (Shifted Rank-1 Coupled Walk $P(x, y) = A(x) B(y) - c$, e.g., Delannoy / King's Walk)**:
  Even when $P(x, y)$ does **not** factor directly (such as the Delannoy step set $P(x, y) = x + y + xy$ or the 8-neighbor King's walk $P(x, y) = (x^{-1} + 1 + x)(y^{-1} + 1 + y) - 1$), if adding a scalar constant $c$ makes it factor as $P(x, y) + c = A(x) B(y)$, the Binomial Theorem decouples $x$ and $y$ in $O(N)$ terms:
  $$P(x, y)^T = (A(x) B(y) - c)^T = \sum_{k=0}^{T} \binom{T}{k} (-c)^{T - k} A(x)^k B(y)^k \implies [x^X y^Y] P(x, y)^T = \sum_{k=0}^{T} \binom{T}{k} (-c)^{T - k} \left([x^X] A(x)^k\right) \left([y^Y] B(y)^k\right)!$$
```

---

### Defect B.9: Omitted $w = 0$ Zero-Weight Division Pitfall in Section 3.2 (Bounded Knapsack & Reversible DP)
- **Source**: [`iter_06_to_10_dp_and_sums.md` Line 391](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_06_to_10_dp_and_sums.md#L391)
- **Target Location in Cohort 3**: [`cohort3_wave_1b_dp_and_sums.md` Lines 522–527](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L522-L527)
- **Deterministic Drop-In Replacement for Lines 522–527 (including the Toy Trace from `cohort2_iter_58_to_62` L414–429)**:
```markdown
#### e. Hand-Checkable Toy Example ($K = 3$, Bounded Add & Rollback)
Suppose we have two items with bounds $c_1 = 1, c_2 = 2$ (weights $w_1 = w_2 = 1$), and capacity $K = 3$:
- Start with $F_0(x) = 1 \implies [1, 0, 0, 0]$.
- **Add item 1** ($c_1 = 1$, multiply by $\frac{1-x^2}{1-x}$):
  - Divide by $1-x$ (upward sweep): $[1, 1, 1, 1]$.
  - Multiply by $1-x^2$ (downward sweep): $[1, 1, 1-1, 1-1] = [1, 1, 0, 0]$.
- **Add item 2** ($c_2 = 2$, multiply by $\frac{1-x^3}{1-x}$):
  - Divide by $1-x$ (upward sweep): $[1, 2, 2, 2]$.
  - Multiply by $1-x^3$ (downward sweep): $[1, 2, 2, 2-1] = [1, 2, 2, 1]$.
- **Remove item 1** (multiply by $\frac{1-x}{1-x^2}$):
  - Multiply by $1-x$ (downward sweep): $[1, 2-1, 2-2, 1-2] = [1, 1, 0, -1]$.
  - Divide by $1-x^2$ (upward sweep $j=2,3$, `f[j] += f[j-2]`): $f[2] = 0 + 1 = 1$, $f[3] = -1 + 1 = 0 \implies [1, 1, 1, 0] = 1 + x + x^2$, recovering item 2 alone!

#### f. Failure Modes, Pitfalls & Edge Cases
- **Loop direction bugs in in-place sparse sweeps**:
  - Multiplying by $1 \pm c x^d$ (`f[j] += ±c * f[j-d]`) **must** iterate $j$ **downwards** ($K \to d$) so `f[j-d]` still holds the old value.
  - Dividing by $1 - c x^d$ (`f[j] += c * f[j-d]`) **must** iterate $j$ **upwards** ($d \to K$) so `f[j-d]` already holds the new cumulative value.
- **Zero-weight items ($w = 0$)**: Never pass $d = w = 0$ into the shift loop `for (int j = d; j <= K; ++j)`! When $w = 0$, the factor is the scalar $1 + c x^0 = 1 + c$ (or $c_i + 1$ for bounded knapsack); multiplying or dividing requires scaling the entire array by $(1 + c)^{\pm 1} \pmod p$ (which is valid if and only if $1 + c \not\equiv 0 \pmod p$).
- **Zero-divisors in non-FPS rollback**: Evaluating at a point $x_0 \in \mathbb{F}_p$ can fail if $1 + x_0 + \dots + x_0^{c_i} \equiv 0 \pmod p$. Working in the truncated polynomial ring $K[x]/(x^{K+1})$ completely avoids zero-divisors because $[x^0]T_i(x) = 1$ is always a unit!
```

---

### Defect B.10: Official Title, Constraints & Explicit Product $\prod_{i=1}^N$ in Problem 10 (`AtCoder ARC 012 D`) and Official Constraints in Problem 1 (`AtCoder fps-24 A`)
- **Locations**:
  - [`cohort3_wave_1b_dp_and_sums.md` Lines 1073–1080 (Problem 1)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1073-L1080)
  - [`cohort3_wave_1b_dp_and_sums.md` Lines 1344–1366 (Problem 10)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1344-L1366)
- **Deterministic Drop-In Replacement for Lines 1078–1080 (Problem 1 Constraints)**:
```markdown
  Over $D$ days, on each day you pay $1, 3, 4,$ or $6$ yen for a snack. Count the number of sequences of daily snack choices $(s_1, \dots, s_D) \in \{1, 3, 4, 6\}^D$ such that $\sum_{i=1}^D s_i = N$, modulo $998244353$.
  **Constraints**: $1 \le D \le 2 \cdot 10^5$, $1 \le N \le 10^6$, Time Limit 2.0s. Note that $O(D)$ binomial summation avoids FFT completely and runs in $< 10$ ms!
```
- **Deterministic Drop-In Replacement for Lines 1344–1366 (Problem 10)**:
```markdown
#### Problem 10: AtCoder ARC 012 D — Don't worry. Be Together (Intermediate)
- **Metadata**: AtCoder `arc012_4` | **Difficulty Tier**: `Intermediate` | **Archetype**: 2D Random Walk Bivariate Laurent Factorization (Section 4.6)
- **Direct URL**: `https://atcoder.jp/contests/arc012/tasks/arc012_4`
- **Mathematical Statement & Constraints**:
  There are $N$ people on $\mathbb{Z}^2$; person $i$ starts at $(x_i, y_i)$. In each of $T$ turns, every person independently moves to one of their $4$ unit Manhattan neighbors $(\pm 1, 0)$ or $(0, \pm 1)$. Find the number of ways for **all $N$ people simultaneously** to gather at $(0, 0)$ at the end of turn $T$, modulo a given integer $M$ (not necessarily prime!).
  **Constraints**: $1 \le N, T \le 10^5$, $|x_i|, |y_i| \le 10^6$, $1 \le M \le 10^9 + 7$. Target complexity: $O(N + T \log \log T)$.
- **Diagnostic Signal & Modelling Bridge**:
  The single-person OGF in $K[x^{\pm 1}, y^{\pm 1}]$ is $[x^{-x_i} y^{-y_i}] (x + x^{-1} + y + y^{-1})^T$. Factoring the bivariate base decouples $(x, y)$ into a product of two 1D binomial coefficients per person, so the total number of ways across all $N$ independent people is a single product of $2N$ binomial coefficients modulo $M$!
- **Progressive 3-Tier Hints**:
  - *Hint 1 (Diagnostic Nudge)*: Write one Manhattan step as $x + x^{-1} + y + y^{-1}$. Can you factor this 4-term Laurent polynomial?
  - *Hint 2 (GF Setup)*: Verify that $x + x^{-1} + y + y^{-1} = (xy)^{-1}(1 + xy)(x + y)$.
  - *Hint 3 (Algebraic Manipulation)*: Raise to the $T$-th power: $[x^X y^Y] (xy)^{-T}(1+xy)^T(x+y)^T = \binom{T}{\frac{T+X+Y}{2}} \binom{T}{\frac{T+X-Y}{2}}$. Since the overall answer is the product over $i=1 \dots N$ and $M$ is composite, accumulate the exponent of each factorial $k!$ ($1 \le k \le T$) across the numerators and denominators of all $2N$ binomial coefficients and factor via a linear sieve!
- **Complete Algebraic Derivation & Solution**:
  By Section 4.6, if $|x_i| + |y_i| > T$ or $T + x_i + y_i$ is odd for any $i$, the answer is $0$. Otherwise, the total number of valid collective walk combinations is:
  $$\text{Ans} = \prod_{i=1}^{N} \binom{T}{\frac{T + x_i + y_i}{2}} \binom{T}{\frac{T + x_i - y_i}{2}} \bmod M.$$
  Represent each binomial coefficient $\binom{T}{k} = \frac{T!}{k!(T-k)!}$ by adding $+1$ to the multiplicity of $T!$ and $-1$ to the multiplicities of $k!$ and $(T-k)!$. Prefix-sum the factorial multiplicities to get the net exponent of each integer $2 \le v \le T$, push composite exponents down to their prime factors using a linear sieve in $O(T)$, and multiply $p^{e_p} \bmod M$ in $O(N + T)$ time.
```

---

## Part 3: Consolidated Verification Checklist of Inspector A's Valid Fixes

For completeness during remediation, the following fixes from [`audit_A_wave_1b.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/audit/audit_A_wave_1b.md) were independently verified and **SHOULD** be applied alongside Part 1 and Part 2 of this report:

1. **Line 136 (`audit_A_wave_1b.md` Defect 2.1)**: Remove `"Wait!"` from Section 2.3 Reverse-Engineering Scratchpad (`so c_n is not \sum_k \tilde{a}_k \tilde{b}_{n-k} directly. However, look at the factorization of \binom{n}{k}:`).
2. **Lines 1396–1420 (`audit_A_wave_1b.md` Defect 3.1 — Problem 12 `Codeforces 932E — Team Work`)**: Include both **Method 1 (Stirling Numbers of the Second Kind + Falling Factorial Absorption in $O(K^2)$ or $O(K \log K)$)**:
   $$\sum_{i=1}^{N} \binom{N}{i} i^K = \sum_{j=1}^{\min(N, K)} \begin{Bmatrix} K \\ j \end{Bmatrix} N^{\underline{j}} \, 2^{N - j} \pmod{10^9 + 7}$$
   and **Method 2 (EGF Differential Operator $\vartheta_x = x D_x$)** so zero information is lost from Cohort 2 Problem 10.
3. **Lines 1044–1064 (`audit_A_wave_1b.md` Defects 3.2 & 3.3 — Section 7 Bibliography & Rejected Templates)**:
   - Append the 3 missing bibliography items (`[EN] Renzo Sprugnoli (1994) Riordan Arrays`, `[EN] Marko Riedel et al. Egorychev Method`, and `[JA] physics0523 (2025) FPS 24題`) to Section 7.1.
   - Append the 2 missing rejected templates (`Library Checker log_of_formal_power_series`, `Library Checker pow_of_formal_power_series`) and explicit `Luogu P3803` to Section 7.2.
4. **Worked Toy Traces (`audit_A_wave_1b.md` Defects 3.4–3.8)**:
   - Section 4.1 (`N=2, M=2` difference convolution trace after Line 570),
   - Section 4.2 ($n=4, a=1, b=1$ upper-index Chu-Vandermonde trace after Line 581),
   - Section 4.5 ($N=4, k=2$ prefix sweep trace after Line 646),
   - Section 5.6 Worked Derivation 4 ($n=2$ Strehl trace after Line 846),
   - Section 6.2 ($D=2$ polynomial transfer matrix trace after Line 956).

---

## Summary Remediation Checklist for Compiler

| Priority | Target Lines in `cohort3_wave_1b_dp_and_sums.md` | Defect ID | Action Required |
| :--- | :--- | :--- | :--- |
| **P0 (Blocker)** | Lines 1500–1528 | **Defect B.1** (Supersedes A.1.1) | Replace Problem 15 (`JSC 2019 Qual F`) with the 2-parameter $H(S, a, b)$ derivation verified on Official Samples 1–3 (**ignore A.1.1's hallucinated statement**). |
| **P0 (Blocker)** | Lines 1739–1760 | **Defect B.2** (Supersedes A.1.2) | Replace Problem 22 (`AISing 2020 F — Two Snuke`) with the official 10-variable statement and $[z^{N-5}]\frac{(1+z)^{11}}{(1-z^2)^{16}}$ derivation verified on Official Sample 1 (**ignore A.1.2's hallucinated 20-variable statement**). |
| **P0 (Blocker)** | Lines 358–413 | **Defect B.3** | Change `array<long long, 21>` to `array<long long, 22>` in `sps_ln` and `sps_exp` to fix the $D=21$ stack buffer overflow, and hoist `inv[1..D]` outside the `2^D` loop in `sps_ln`. |
| **P1 (Editorial/Math)** | Lines 590–596 | **Defect B.4** | Remove `"wait: let us check carefully!"` and false identity in Section 4.4 Bluestein's CZT. |
| **P1 (Editorial/Math)** | Line 706 | **Defect B.5** | Remove `"wait: C(x) - xC(x)^2 = 1!"` inside Master Kernel Table K4. |
| **P1 (Source Loss)** | Lines 1004–1020 | **Defect B.6 & B.7** | Restore the 7-row 2D Shift/Differential Operator Dictionary Table, Eulerian recurrence origin, $N=3$ toy trace, and truncation pitfall in Section 6.5. |
| **P1 (Source Loss)** | Lines 649–660 | **Defect B.8** | Restore Case 2 of 2D Walk Decoupling ($P(x,y) = A(x)B(y) - c$) in Section 4.6. |
| **P1 (Source Loss)** | Lines 522–527 | **Defect B.9** | Restore $K=3$ rollback toy trace and $w=0$ zero-weight division pitfall in Section 3.2. |
| **P2 (Precision)** | Lines 1078–1080, 1344–1366 | **Defect B.10** | Update official constraints in Problem 1 (`fps-24 A`) and official title/product formula in Problem 10 (`ARC 012 D`). |
| **P2 (From Audit A)** | Lines 136, 570, 581, 646, 846, 956, 1044–1064, 1396–1420 | **Defects A.2.1, A.3.1–3.8** | Apply verified narrative/trace/bibliography restorations from `audit_A_wave_1b.md`. |
