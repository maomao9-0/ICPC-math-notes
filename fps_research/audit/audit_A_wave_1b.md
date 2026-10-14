# Principal Mathematical & Pedagogical Audit Report — Wave 1B (`cohort3_wave_1b_dp_and_sums.md`)

- **Auditor**: Inspector A (Principal Mathematical & Pedagogical Auditor)
- **Target File**: [`cohort3_wave_1b_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md) (1,926 lines)
- **Source Files Audited Against**:
  1. **Cohort 1**: [`iter_06_to_10_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_06_to_10_dp_and_sums.md) (1,493 lines)
  2. **Cohort 2**: [`cohort2_iter_58_to_62_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_58_to_62_dp_and_sums.md) (1,381 lines)
- **Cross-Referenced Archive**: [`problem_archive.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md)

---

## Executive Summary & Audit Scorecard

| Audit Dimension | Status | Summary of Findings |
| :--- | :--- | :--- |
| **1. Mathematical & Algorithmic Exactness** | **FAIL (5 Critical Bugs)** | **Bug 1.1 (`AtCoder JSC 2019 Qual F`, L1500–L1528)**: Formula overcounts $B_M > B_{M+1}$ by factor $(B_M - B_{M+1})$ (inherited from Cohort 1 L1254; also affects `problem_archive.md` L629–L635).<br>**Bug 1.2 (`AtCoder fps-24 A`, L1076–L1110)**: Hallucinated snack costs $\{1,1,2,3\}$ ($2x+x^2+x^3$) instead of true AtCoder costs $\{1,3,4,6\}$ ($x+x^3+x^4+x^6 = x(1+x^2)(1+x^3)$), and dropped Cohort 2's $\mathcal{O}(D)$ binomial factorization.<br>**Bug 1.3 (Worked Derivation 6, L858–L875)**: Moriarty/Catalan-shift closed form on L874 is off by $m \mapsto m+1$ and fails for every $n, m \ge 0$.<br>**Bug 1.4 (Worked Derivation 4, L794–L820)**: Aborts mid-derivation without ever finding the closed form $\binom{2m}{2n}$.<br>**Bug 1.5 (Worked Derivation 2, L760–L772)**: Mis-copied Cohort 2 Worked Derivation 2 by writing lower index $n-k$ instead of $n+m$ in $\binom{2n-2k}{\cdot}$, getting stuck at an unsimplifiable $[x^n]\frac{(1-x)^n}{\sqrt{1-4x}}$. |
| **2. Zero Information Loss vs. Source Cohorts** | **FAIL (8 Omissions)** | **Problem Curation**: All 27 unique accepted problems (18 Cohort 1 + 17 Cohort 2, 8 shared) and all 11 rejected templates are present.<br>**Omitted Derivations & Theory**: Section 4.2 dropped Cohort 2's 1st/2nd-moment weighted Vandermonde identities (explicitly promised in L24); Section 5.5 dropped Cohort 1 Walkthroughs 8.3.2 (`Failure Modes`), 8.3.3, 8.3.5 (promised in L25) and Cohort 2 Worked Derivations 2, 3 (Chebyshev residue change-of-variables), 4 (Li Shanlan/Strehl), plus Cohort 2's Pitfall 1 & 2 callout boxes.<br>**Omitted C++ Reference Kernels**: Dropped Cohort 1's `diff_convolution` C++ kernel and Cohort 2's `kth_prefix_sum` $\mathcal{O}(n \log n)$ C++ kernel. |
| **3. Pedagogical & Editorial Completeness (`AGENTS.md`)** | **NEEDS REMEDIATION** | **Unedited Stream-of-Consciousness**: L804–L819 (Derivation 4), L836–L856 (Derivation 5), L882 (Derivation 7), L1080–L1083 (`fps-24 A`), L1504 (`JSC 2019 Qual F`), and L1652 (`CF 438E`) contain raw "wait — let us be careful..." self-corrections or hand-waved steps.<br>**Structural Seam at L498**: Sections 1–3 use `## Section 1..3` with full `a–f` Zero Magic Steps (`Concrete Object` through `Failure Modes`), whereas Sections 4–6 switch to `## 4..6` and drop the `a–f` scaffolding, small-$n$ toy traces, and failure mode subsections. |
| **4. LaTeX Formatting & Delimiter Hygiene** | **PASS (100%)** | Zero instances of banned `\(...\)` or `\[...\]` delimiters across all 1,926 lines. |

---

## Part I: Critical Mathematical & Algorithmic Bugs (With 100% Deterministic Replacements)

### Defect 1.1 — Problem 15 (`AtCoder JSC 2019 Qual F — Candy Retribution`, Lines 1500–1528)
- **Severity**: **CRITICAL (False Formula + Garbled Problem Statement; also propagates to `problem_archive.md` Lines 629–635)**
- **Location**: [`cohort3_wave_1b_dp_and_sums.md#L1500-L1528`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1500-L1528) (and [`problem_archive.md#L629-L635`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md#L629-L635))
- **Diagnosis**:
  1. **Statement Error (L1504)**: The live AtCoder statement (`https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_f`) asks for the number of non-negative integer sequences $A = (A_1, \dots, A_N)$ with $L \le \sum_{i=1}^N A_i \le R$ such that when sorted in non-increasing order $B_1 \ge B_2 \ge \dots \ge B_N$, the $M$-th and $(M+1)$-th elements are equal: **$B_M = B_{M+1}$** (equivalently, there is no way to choose $M$ children who each receive strictly more candies than each of the remaining $N-M$ children). Line 1504 garbles this as *"the sum of the largest $M$ elements equals... (or when sorted $B_1 \ge B_2 \ge \cdots \ge B_N$, $B_M = B_{M+1}$)"*.
  2. **Mathematical Overcounting Error (L1511–L1527)**: To count the complement ($B_M > B_{M+1}$), both Cohort 1 (L1254) and Cohort 3 (L1521–L1527) sum over a threshold $q \ge 0$ where the top $M$ elements satisfy $A_i \ge q+1$ (OGF $\frac{x^{M(q+1)}}{(1-x)^M}$) and the bottom $N-M$ elements satisfy $0 \le A_j \le q$ (OGF $\frac{(1-x^{q+1})^{N-M}}{(1-x)^{N-M}}$):
     $$
     G_{\text{wrong}}(x) = \sum_{q=0}^{R/M} \binom{N}{M} \frac{x^{M(q+1)} (1 - x^{q+1})^{N-M}}{(1 - x)^N}.
     $$
     **Why this is false**: For any sequence with $B_M > B_{M+1}$, **every** integer $q$ in the range $B_{M+1} \le q \le B_M - 1$ satisfies "top $M$ elements are $\ge q+1$ and bottom $N-M$ elements are $\le q$"! Thus the formula counts each sequence with $B_M > B_{M+1}$ **$(B_M - B_{M+1})$ times** instead of once!
  3. **Numerical Verification**:
     - For $N=4, M=2, S=4$: true number of sequences with $B_2 > B_3$ is $18$ (out of $\binom{4+4-1}{4-1} = 35$, leaving $35 - 18 = 17$ valid sequences with $B_2 = B_3$). The formula on L1524 gives $24$ instead of $18$ because the $\binom{4}{2} = 6$ permutations of $(2, 2, 0, 0)$ have $B_2 = 2, B_3 = 0$ and are counted $B_2 - B_3 = 2$ times (at $q=0$ and $q=1$).
     - On AtCoder Sample 1 (`N=4, M=2, L=3, R=7`), true answer is `105`, whereas the L1524 formula gives `45`.
  4. **Exact Mathematical Fix**: Fix the exact value of the $M$-th largest element $d = B_M \ge 1$. Then:
     - The top $M$ elements are all $\ge d$, **and at least one of them equals $d$** (so it is NOT the case that all $M$ elements are $\ge d+1$). Their OGF is:
       $$
       \left(\frac{x^d}{1 - x}\right)^M - \left(\frac{x^{d+1}}{1 - x}\right)^M = \frac{x^{Md} - x^{M(d+1)}}{(1 - x)^M}.
       $$
     - The remaining $N - M$ elements lie in $[0, d-1]$, with OGF $\left(\frac{1 - x^d}{1 - x}\right)^{N-M}$.
     - Multiplying by $\binom{N}{M}$ and summing over $d \ge 1$ gives the exact OGF for $B_M > B_{M+1}$ (Verified against all 3 AtCoder samples: Sample 1 `4 2 3 7 -> 105`, Sample 2 `2 1 4 8 -> 3`, Sample 3 `141592 6535 89793 238462 -> 933832916`):
       $$
       G_{\text{comp}}(x) = \frac{\binom{N}{M}}{(1 - x)^N} \sum_{d=1}^{\lfloor R/M \rfloor} \left(x^{Md} - x^{M(d+1)}\right) (1 - x^d)^{N-M}.
       $$
- **Deterministic Replacement Text for Lines 1500–1528 of `cohort3_wave_1b_dp_and_sums.md`**:

```markdown
#### Problem 15: `AtCoder JSC 2019 Qual F — Candy Retribution` *(Cohort 1 Unique Discovery)*
- **Source & Link**: [AtCoder Japanese Student Championship 2019 Qualification — Task F](https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_f)
- **Difficulty Tier**: Advanced (Iteration 07 / 10 — Complementary Counting + Exact Minimum Threshold OGF + Harmonic Binomial Expansion)
- **Self-Contained Mathematical Statement**:
  Count the number of non-negative integer sequences $A = (A_1, A_2, \dots, A_N)$ such that $L \le \sum_{i=1}^N A_i \le R$ and, when $A$ is sorted in non-increasing order as $B_1 \ge B_2 \ge \cdots \ge B_N$, the $M$-th and $(M+1)$-th elements are equal: $B_M = B_{M+1}$. Output the answer modulo $10^9 + 7$.
  - **Constraints**: $1 \le M < N \le 3 \cdot 10^5$, $1 \le L \le R \le 3 \cdot 10^5$, Modulus $p = 10^9 + 7$, Time Limit $2.0\text{ s}$.
- **Why It Passes the Non-Template Filter**: Combines **Complementary Counting ($B_M > B_{M+1}$)** with **Inclusion-Exclusion on the Minimum of the Top $M$ Elements** and the **Harmonic Number Bound $\sum_{d=1}^{R/M} \frac{R}{d} = \mathcal{O}(R \log R)$**: avoids overcounting the gap $[B_{M+1}, B_M - 1]$ by pinning $d = B_M \ge 1$ via $(x^{Md} - x^{M(d+1)})$ and expanding $(1 - x^d)^{N-M}$ in $\mathcal{O}(R \log R)$ total operations without any NTT!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Complementary Counting & The Overcounting Trap)*: Count sequences where $B_M > B_{M+1}$ and subtract from the total number of sequences with sum in $[L, R]$. Why can't we simply sum over a threshold $q \ge 0$ where $M$ elements are $\ge q+1$ and $N-M$ elements are $\le q$? Because a sequence with $B_M > B_{M+1}$ satisfies that condition for **every** $q \in [B_{M+1}, B_M - 1]$, overcounting it $(B_M - B_{M+1})$ times!
  - *Hint 2 (Pinning the Exact Value $d = B_M$)*: To count each sequence with $B_M > B_{M+1}$ **uniquely**, fix $d = B_M \ge 1$. Then the $N-M$ smallest elements must lie in $[0, d-1]$ (OGF $\left(\frac{1-x^d}{1-x}\right)^{N-M}$), while the $M$ largest elements must all be $\ge d$ **with at least one equal to $d$**. What is the OGF for $M$ elements $\ge d$ minus the OGF for $M$ elements $\ge d+1$?
  - *Hint 3 (Harmonic Binomial Expansion)*: The top $M$ elements have OGF $\left(\frac{x^d}{1-x}\right)^M - \left(\frac{x^{d+1}}{1-x}\right)^M = \frac{x^{Md} - x^{M(d+1)}}{(1-x)^M}$. Multiplying by $\binom{N}{M}\left(\frac{1-x^d}{1-x}\right)^{N-M}$ and the prefix-sum operator $\frac{1}{1-x}$ yields:
    $$
    [x^S] \frac{1}{1 - x} G_{\text{comp}}(x) = \binom{N}{M} \sum_{d=1}^{\lfloor S/M \rfloor} \sum_{j=0}^{N-M} (-1)^j \binom{N-M}{j} [x^S] \frac{x^{(M+j)d} - x^{M(d+1) + jd}}{(1 - x)^{N+1}},
    $$
    which has only $\mathcal{O}(S \log S)$ non-zero terms where $(M+j)d \le S$!
- **Full Algebraic Derivation & Implementation Blueprint**:
  1. **Unconstrained Prefix Sum**:
     The total number of sequences $A \in \mathbb{Z}_{\ge 0}^N$ with $\sum_{i=1}^N A_i \le S$ is $[x^S] \frac{1}{(1-x)^{N+1}} = \binom{S + N}{N}$.
  2. **Unique Decomposition of the Complement ($B_M > B_{M+1}$)**:
     When $B_M > B_{M+1}$, let $d = B_M \in \{1, 2, \dots, \lfloor S/M \rfloor\}$. The subset of $M$ indices with values $\ge d$ can be chosen in $\binom{N}{M}$ ways:
     - Those $M$ elements lie in $[d, \infty)$ with minimum **equal to $d$** (i.e., not all in $[d+1, \infty)$), giving OGF:
       $$
       \left(\frac{x^d}{1 - x}\right)^M - \left(\frac{x^{d+1}}{1 - x}\right)^M = \frac{x^{Md} - x^{M(d+1)}}{(1 - x)^M}.
       $$
     - The remaining $N - M$ elements lie in $[0, d-1]$, giving OGF $\left(\frac{1 - x^d}{1 - x}\right)^{N-M}$.
     Multiplying these factors and summing over $d \ge 1$ gives the exact OGF of the complement:
     $$
     G_{\text{comp}}(x) = \frac{\binom{N}{M}}{(1 - x)^N} \sum_{d=1}^{\lfloor R/M \rfloor} \left(x^{Md} - x^{M(d+1)}\right) (1 - x^d)^{N-M}.
     $$
  3. **$\mathcal{O}(R \log R)$ Harmonic Prefix-Sum Evaluation**:
     To evaluate $C(S) = \sum_{k=0}^S [x^k] G_{\text{comp}}(x) = [x^S] \frac{1}{1-x} G_{\text{comp}}(x)$ for $S \in \{R, L-1\}$, expand $(1 - x^d)^{N-M} = \sum_{j=0}^{N-M} (-1)^j \binom{N-M}{j} x^{jd}$ and use $[x^K] (1 - x)^{-(N+1)} = \binom{K + N}{N}$:
     $$
     C(S) = \binom{N}{M} \sum_{d=1}^{\lfloor S/M \rfloor} \sum_{j=0}^{\min\left(N-M,\, \lfloor (S - Md)/d \rfloor\right)} (-1)^j \binom{N-M}{j} \left[ \binom{S - (M+j)d + N}{N} - \binom{S - M(d+1) - jd + N}{N} \right],
     $$
     where the second binomial coefficient is $0$ whenever $S < M(d+1) + jd$.
     For each $d \ge 1$, the inner loop runs at most $\lfloor S/d \rfloor - M + 1$ times, so the total work is $\sum_{d=1}^{\lfloor S/M \rfloor} \frac{S}{d} = \mathcal{O}(S \log S)$ in $\mathcal{O}(N + R)$ space! Subtracting $C(R) - C(L-1)$ from $\binom{R+N}{N} - \binom{L-1+N}{N}$ yields the exact answer.
```

---

### Defect 1.2 — Problem 1 (`AtCoder fps-24 A — Snack`, Lines 1076–1110)
- **Severity**: **CRITICAL (Hallucinated Problem Statement & Polynomial + Dropped Cohort 2 $\mathcal{O}(D)$ Factorization)**
- **Location**: [`cohort3_wave_1b_dp_and_sums.md#L1076-L1110`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1076-L1110)
- **Diagnosis**:
  1. **Statement & Polynomial Error (L1080–L1089)**: The live AtCoder statement (`https://atcoder.jp/contests/fps-24/tasks/fps_24_a`) specifies $D$ days ($1 \le D \le 2 \cdot 10^5$), total budget $N$ yen ($1 \le N \le 10^6$), and 4 daily snack options with costs **$\{1, 3, 4, 6\}$ yen** (total cost over $D$ days must be **exactly $N$ yen**). Thus the daily OGF is:
     $$
     P(x) = x + x^3 + x^4 + x^6 = x(1 + x^2)(1 + x^3),
     $$
     which Cohort 2 (`cohort2_iter_58_to_62_dp_and_sums.md` L1042–L1060) stated and derived accurately!
  2. In `cohort3_wave_1b_dp_and_sums.md` L1080–L1090, the compiler hallucinated snack costs *"A (1 yen), B (1 yen), C (2 yen), E (3 yen)"* with $P(x) = 2x + x^2 + x^3$ and wrote an uncertain parenthetical *(or $\le N$)* on L1082.
  3. **Fix**: Restore the exact AtCoder problem statement ($D \le 2\cdot 10^5, N \le 10^6$, costs $\{1, 3, 4, 6\}$, exact sum $N$) and present **both** Cohort 2's $\mathcal{O}(D)$ binomial factorization $[x^{N-D}](1+x^2)^D(1+x^3)^D$ (verified on AtCoder Sample 1 `2 7 -> 4` and Sample 2 `200000 1000000 -> 688682037`) **and** the general $\mathcal{O}(N)$ D-finite recurrence $(P(x)/x) F'(x) = D (P(x)/x)' F(x)$.
- **Deterministic Replacement Text for Lines 1076–1110 of `cohort3_wave_1b_dp_and_sums.md`**:

```markdown
#### Problem 1: `AtCoder fps-24 A — Snack` *(Cohort 2 Unique Discovery)*
- **Source & Link**: [AtCoder FPS 24: 24 Problems on Formal Power Series — Task A](https://atcoder.jp/contests/fps-24/tasks/fps_24_a)
- **Difficulty Tier**: Stepping Stone (Iteration 06 / 58 — Algebraic Factorization $[x^N](x + x^3 + x^4 + x^6)^D$ & D-Finite $F'/F$ Recurrence)
- **Self-Contained Mathematical Statement**:
  Over $D$ days, on each day you buy exactly one snack chosen from $4$ distinct types costing $1, 3, 4,$ and $6$ yen respectively. Find the number of $D$-day snack sequences whose total cost is **exactly** $N$ yen, modulo $998244353$.
  - **Constraints**: $1 \le D \le 2 \cdot 10^5$, $1 \le N \le 10^6$, Modulus $p = 998244353$, Time Limit $2.0\text{ s}$.
- **Why It Passes the Non-Template Filter**: Teaches two foundational FPS paradigms on a single problem before touching NTT:
  1. **Algebraic Polynomial Factorization ($\mathcal{O}(D)$ time)**: Factoring the single-day OGF $P(x) = x + x^3 + x^4 + x^6 = x(1 + x^2)(1 + x^3)$ collapses $P(x)^D$ into the product of two sparse binomial expansions $(1 + x^2)^D (1 + x^3)^D$!
  2. **Logarithmic Derivative / D-Finite Recurrence ($\mathcal{O}(N)$ time)**: Even if $P(x)$ did not factor, $Q(x) = (P(x)/x)^D$ satisfies $Q'(x) (P(x)/x) = D (P(x)/x)' Q(x)$, yielding a $6$-term linear recurrence in $\mathcal{O}(N)$ time without FFT!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Single-Day OGF & Shift)*: Write the single-day OGF $P(x) = x + x^3 + x^4 + x^6$. Factor out $x$ so that $[x^N] P(x)^D = [x^{N-D}] (1 + x^2 + x^3 + x^5)^D$.
  - *Hint 2 (Algebraic Factorization)*: Notice that $1 + x^2 + x^3 + x^5 = (1 + x^2)(1 + x^3)$! Expand $(1 + x^2)^D = \sum_{a=0}^D \binom{D}{a} x^{2a}$ and $(1 + x^3)^D = \sum_{b=0}^D \binom{D}{b} x^{3b}$.
  - *Hint 3 (Alternative $\mathcal{O}(N)$ D-Finite Recurrence)*: Let $Q(x) = (1 + x^2 + x^3 + x^5)^D = \sum_{k \ge 0} q_k x^k$. Differentiate $\ln Q(x) = D \ln(1 + x^2 + x^3 + x^5)$ to get $(1 + x^2 + x^3 + x^5) Q'(x) = D(2x + 3x^2 + 5x^4) Q(x)$ and extract $[x^{k-1}]$!
- **Full Algebraic Derivation & Implementation Blueprint**:
  1. **Method 1 — $\mathcal{O}(D)$ Binomial Factorization (Cohort 2 Canonical Solution)**:
     Factor the single-day generating function:
     $$
     P(x) = x + x^3 + x^4 + x^6 = x(1 + x^2)(1 + x^3).
     $$
     Raising $P(x)$ to the $D$-th power and setting $K = N - D$ (if $K < 0$, the answer is $0$):
     $$
     [x^N] P(x)^D = [x^{N-D}] (1 + x^2)^D (1 + x^3)^D = [x^K] \left(\sum_{a=0}^{D} \binom{D}{a} x^{2a}\right) \left(\sum_{b=0}^{D} \binom{D}{b} x^{3b}\right).
     $$
     For each $a \in [0, D]$ such that $K - 2a \ge 0$ and $3 \mid (K - 2a)$, set $b = (K - 2a)/3$. If $0 \le b \le D$, accumulate $\binom{D}{a} \binom{D}{b} \bmod 998244353$:
     $$
     \text{ans} = \sum_{\substack{0 \le a \le D \\ 0 \le K - 2a \le 3D \\ K \equiv 2a \pmod 3}} \binom{D}{a} \binom{D}{(K - 2a)/3} \pmod{998244353}.
     $$
     This runs in $\mathcal{O}(D)$ time and $\mathcal{O}(D)$ space (evaluating Sample 1 `D=2, N=7` $\to 4$ and Sample 2 `D=200000, N=1000000` $\to 688682037$).
  2. **Method 2 — $\mathcal{O}(N)$ D-Finite ODE Recurrence (General Unfactorable $P(x)$)**:
     Let $A(x) = 1 + x^2 + x^3 + x^5$ and $Q(x) = A(x)^D = \sum_{k=0}^{5D} q_k x^k$. Taking logarithmic derivatives:
     $$
     \frac{Q'(x)}{Q(x)} = D \frac{A'(x)}{A(x)} \implies (1 + x^2 + x^3 + x^5) Q'(x) = D (2x + 3x^2 + 5x^4) Q(x).
     $$
     Extracting $[x^{k-1}]$ from both sides gives $q_0 = 1$ and, for $k = 1, \dots, N - D$:
     $$
     k \, q_k = \big(2D - (k - 2)\big) q_{k-2} + \big(3D - (k - 3)\big) q_{k-3} + \big(5D - (k - 5)\big) q_{k-5},
     $$
     which computes $q_{N-D}$ in $\mathcal{O}(N)$ time using precomputed modular inverses $\text{inv}[1..N]$.
```

---

### Defect 1.3 — Section 5.5 Worked Derivation 6 (`Moriarty's Identity via Beta-Integral / Partial Fraction Parameter Shift`, Lines 858–875)
- **Severity**: **CRITICAL (False Closed-Form Formula + Hand-Waved Proof)**
- **Location**: [`cohort3_wave_1b_dp_and_sums.md#L858-L875`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L858-L875)
- **Diagnosis**:
  1. Line 860 defines the sum:
     $$
     M(n, m) = \sum_{k=0}^{n} \binom{n+k}{2k} \binom{2k}{k} \frac{(-1)^k}{k + 1 + m} \qquad (m \ge 0).
     $$
  2. Line 874 claims:
     $$
     M(n, m) = (-1)^n \frac{m!(m-1)!}{(m+n)!(m-n)!} = \frac{(-1)^n m}{m + n} \frac{\binom{m}{n}}{\binom{m+n-1}{n}}.
     $$
  3. **Numerical Refutation**:
     - At $n = 0, m = 0$: true sum is $1$, whereas L874 has $0 / 0$ or $(-1)!\to \infty$.
     - At $n = 0, m = 1$: true sum is $\frac{1}{2}$, whereas L874 gives $1$.
     - At $n = 1, m = 1$: true sum is $\frac{1}{2} - \frac{2}{3} = -\frac{1}{6}$, whereas L874 gives $-\frac{1}{2}$.
     - At $n = 1, m = 2$: true sum is $\frac{1}{3} - \frac{2}{4} = -\frac{1}{6}$, whereas L874 gives $-\frac{1}{3}$.
     The formula on Line 874 is off by $m \mapsto m + 1$ because the denominator of the summand is $k + 1 + m = k + (m + 1)$, not $k + m$. Furthermore, Line 872 hand-waves the proof (*"partial fraction / finite difference reduction yields..."*).
- **Deterministic Replacement Text for Lines 858–875 of `cohort3_wave_1b_dp_and_sums.md`**:

```markdown
#### Worked Derivation 6: Catalan-Shift Rational Sum via Partial-Fraction Heaviside Cover-Up
- **Target Sum**:
  $$
  M(n, m) = \sum_{k=0}^{n} \binom{n+k}{2k} \binom{2k}{k} \frac{(-1)^k}{k + m + 1} \qquad (n, m \ge 0).
  $$
- **a. Concrete Object**: Alternating binomial sum coupling the Catalan/Delannoy factor $\binom{n+k}{2k}\binom{2k}{k}$ with the shifted rational denominator $\frac{1}{k+m+1}$.
- **b. Diagnostic Signal**: The factor $\binom{n+k}{2k}\binom{2k}{k}$ simplifies via trinomial revision to $\binom{n}{k}\binom{n+k}{n}$, turning the sum into $\sum_{k=0}^n (-1)^k \binom{n}{k} \frac{Q(k)}{k + x}$ where $Q(k) = \binom{n+k}{n}$ is a degree-$n$ polynomial in $k$ and $x = m + 1$. Any sum of the form $\sum_{k=0}^n (-1)^k \binom{n}{k} \frac{Q(k)}{k+x}$ with $\deg Q \le n$ is the **exact Heaviside partial fraction expansion** of $\frac{n! \, Q(-x)}{x(x+1)\cdots(x+n)}$!
- **c. Reverse-Engineering Scratchpad**:
  Consider the rational function $R(x) = \frac{n! \, Q(-x)}{x(x+1)\cdots(x+n)}$ where $\deg Q \le n$. Since $\deg Q \le n < n + 1$, $R(x)$ is a proper rational function in $x$ with simple poles at $x = -k$ for $k = 0, 1, \dots, n$. By Heaviside cover-up (Section 6.5), the residue at $x = -k$ is:
  $$
  \lim_{x \to -k} (x + k) R(x) = \frac{n! \, Q(k)}{(-k)(-k+1)\cdots(-1) \cdot 1 \cdot 2 \cdots (n-k)} = (-1)^k \binom{n}{k} Q(k).
  $$
  Hence $R(x) = \sum_{k=0}^n (-1)^k \binom{n}{k} \frac{Q(k)}{x + k}$ identically! (Note that at $m = 0$, Snake Oil with Kernel K2 + Catalan Kernel K4 also gives $M(n, 0) = [x^n] \frac{1}{1-x} C\left(\frac{-x}{(1-x)^2}\right) = [x^n] \frac{1-x}{1-x} = [n = 0]$.)
- **d. Step-by-Step Algebraic Derivation**:
  1. **Trinomial Revision**:
     $$
     \binom{n+k}{2k}\binom{2k}{k} = \frac{(n+k)!}{(n-k)!(2k)!} \cdot \frac{(2k)!}{k! k!} = \frac{n!}{k!(n-k)!} \cdot \frac{(n+k)!}{n! k!} = \binom{n}{k} \binom{n+k}{n}.
     $$
  2. **Polynomial Partial-Fraction Collapse**:
     Let $Q(k) = \binom{n+k}{n} = \frac{(k+1)(k+2)\cdots(k+n)}{n!}$ (degree $n$ in $k$) and set $x = m + 1$:
     $$
     M(n, m) = \sum_{k=0}^{n} (-1)^k \binom{n}{k} \frac{Q(k)}{k + (m + 1)} = \frac{n! \, Q(-m - 1)}{(m + 1)(m + 2)\cdots(m + n + 1)}.
     $$
  3. **Upper Negation at $k = -m - 1$**:
     By upper negation, $Q(-m - 1) = \binom{n - m - 1}{n} = (-1)^n \binom{m}{n}$. Substituting $(m+1)\cdots(m+n+1) = \frac{(m+n+1)!}{m!}$ yields:
     $$
     M(n, m) = \frac{n! \, (-1)^n \binom{m}{n}}{(m + n + 1)! / m!} = \frac{(-1)^n \, (m!)^2}{(m - n)! \, (m + n + 1)!} = \frac{(-1)^n}{m + n + 1} \frac{\binom{m}{n}}{\binom{m + n}{n}},
     $$
     which equals $0$ whenever $n > m$ (since $\binom{m}{n} = 0$ for $0 \le m < n$).
- **e. Hand-Checkable Toy Trace ($n = 1, m = 1$ and $n = 2, m = 1$)**:
  - For $n = 1, m = 1$: LHS $= \binom{1}{0}\binom{0}{0}\frac{1}{2} - \binom{2}{2}\binom{2}{1}\frac{1}{3} = \frac{1}{2} - \frac{2}{3} = -\frac{1}{6}$. Formula gives $\frac{(-1)^1 (1!)^2}{0! \, 3!} = -\frac{1}{6}$. Matches!
  - For $n = 2, m = 1$ ($n > m$): LHS $= \frac{1}{2} - \binom{3}{2}\binom{2}{1}\frac{1}{3} + \binom{4}{4}\binom{4}{2}\frac{1}{4} = \frac{1}{2} - 2 + \frac{3}{2} = 0$. Formula gives $\binom{1}{2} = 0$. Matches!
```

---

### Defect 1.4 — Section 5.5 Worked Derivation 4 (`Root-of-Unity Parity Split + Snake Oil`, Lines 794–820)
- **Severity**: **CRITICAL (Abandoned Derivation — Stops Mid-Sentence Without Finding the Closed Form $\binom{2m}{2n}$)**
- **Location**: [`cohort3_wave_1b_dp_and_sums.md#L794-L820`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L794-L820)
- **Diagnosis**:
  Lines 804–819 contain a confused, aborted scratchpad (*"wait: let us be careful with signs! ... Wait: even simpler!"*) that abruptly stops at Line 819 without ever deriving the closed form $\binom{2m}{2n}$!
- **Deterministic Replacement Text for Lines 794–820 of `cohort3_wave_1b_dp_and_sums.md`**:

```markdown
#### Worked Derivation 4: Root-of-Unity Parity Split + Quadratic-Variable Egorychev Extraction
- **Target Sums**:
  $$
  S_{\text{odd}}(m, n) = \sum_{k=0}^{n} \binom{2n+1}{2k+1} \binom{m+k}{2n}, \qquad S_{\text{even}}(m, n) = \sum_{k=0}^{n} \binom{2n+1}{2k} \binom{m+k}{2n}.
  $$
- **a. Concrete Object**: Sums over $k$ coupling a parity-strided binomial coefficient $\binom{2n+1}{2k+1}$ (or $\binom{2n+1}{2k}$) with an upper-index $k$-dependent binomial coefficient $\binom{m+k}{2n}$.
- **b. Diagnostic Signal**:
  1. Lower-index symmetry $\binom{2n+1}{2k+1} = \binom{2n+1}{2(n-k)}$ aligns the stride $2(n-k)$ with the upper index of $\binom{m+k}{2n}$ when we set $j = n - k$.
  2. In $\binom{m+n-j}{2n} = [z^{m-n-j}](1 - z)^{-2n-1}$, $j$ steps by $1$ while $\binom{2n+1}{2j}$ has $2j$ stepping by $2$. Substituting $z = u^2$ matches the stride $2j$ to $u^{2j}$ and factors $(1 - u^2)^{2n+1} = (1 - u)^{2n+1}(1 + u)^{2n+1}$!
- **c. Reverse-Engineering Scratchpad**:
  Set $j = n - k \in \{0, 1, \dots, n\}$. Then $\binom{2n+1}{2k+1} = \binom{2n+1}{2j}$ and:
  $$
  \binom{m+k}{2n} = \binom{m+n-j}{2n} = [z^{m-n-j}] (1 - z)^{-2n-1} = [u^{2m-2n-2j}] (1 - u^2)^{-2n-1} = [u^{2m-2n}] \frac{u^{2j}}{(1 - u^2)^{2n+1}}.
  $$
  Now the internal sum over $j$ is simply the even part of $(1 + u)^{2n+1}$!
- **d. Step-by-Step Algebraic Derivation**:
  1. **Quadratic Substitution ($z = u^2$) & Shift Rule**:
     With $j = n - k$:
     $$
     S_{\text{odd}}(m, n) = \sum_{j=0}^{n} \binom{2n+1}{2j} [u^{2m-2n}] \frac{u^{2j}}{(1 - u^2)^{2n+1}} = [u^{2m-2n}] \frac{1}{(1 - u^2)^{2n+1}} \sum_{j=0}^{n} \binom{2n+1}{2j} u^{2j}.
     $$
  2. **Root-of-Unity Parity Filter**:
     By the $2$-nd root-of-unity filter (Section 4.5):
     $$
     \sum_{j=0}^{n} \binom{2n+1}{2j} u^{2j} = \frac{(1 + u)^{2n+1} + (1 - u)^{2n+1}}{2}.
     $$
  3. **Factor Cancellation against $(1 - u^2)^{2n+1} = (1 - u)^{2n+1}(1 + u)^{2n+1}$**:
     $$
     S_{\text{odd}}(m, n) = \frac{1}{2} [u^{2m-2n}] \left( \frac{1}{(1 - u)^{2n+1}} + \frac{1}{(1 + u)^{2n+1}} \right).
     $$
     Since $2m - 2n$ is **even**, $(-1)^{2m-2n} = +1$, so both terms contribute equally:
     $$
     S_{\text{odd}}(m, n) = [u^{2m-2n}] (1 - u)^{-2n-1} = \binom{(2m - 2n) + 2n}{2n} = \binom{2m}{2n}.
     $$
  4. **Companion Even-Index Sum $S_{\text{even}}(m, n)$**:
     Replacing $\binom{2n+1}{2k+1}$ with $\binom{2n+1}{2k} = \binom{2n+1}{2j+1}$ and multiplying by $u$ inside $[u^{2m-2n+1}]$ yields:
     $$
     S_{\text{even}}(m, n) = [u^{2m-2n+1}] \frac{(1+u)^{2n+1} - (1-u)^{2n+1}}{2(1-u^2)^{2n+1}} = \frac{1}{2}[u^{2m-2n+1}]\Big((1-u)^{-2n-1} - (1+u)^{-2n-1}\Big) = \binom{2m+1}{2n},
     $$
     since $2m - 2n + 1$ is **odd** so $-(-1)^{2m-2n+1} = +1$.
- **e. Hand-Checkable Toy Trace ($m = 2, n = 1$)**:
  - $S_{\text{odd}}(2, 1) = \binom{3}{1}\binom{2}{2} + \binom{3}{3}\binom{3}{2} = 3(1) + 1(3) = 6 = \binom{4}{2}$.
  - $S_{\text{even}}(2, 1) = \binom{3}{0}\binom{2}{2} + \binom{3}{2}\binom{3}{2} = 1(1) + 3(3) = 10 = \binom{5}{2}$.
```

---

### Defect 1.5 — Section 5.5 Worked Derivation 2 (`Alternating Central Binomial Convolution`, Lines 760–772)
- **Severity**: **HIGH (Mis-Copied Cohort 2 Worked Derivation 2 — Lower Index $n-k$ Instead of $n+m$ Causes Sum to Stall Without Closed Form)**
- **Location**: [`cohort3_wave_1b_dp_and_sums.md#L760-L772`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L760-L772)
- **Diagnosis**:
  In Cohort 2 Worked Derivation 2 ([`cohort2_iter_58_to_62_dp_and_sums.md#L653-L682`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_58_to_62_dp_and_sums.md#L653-L682)), the target sum is:
  $$
  S_2(n, m) = \sum_{k=0}^{n} (-1)^k \binom{n}{k} \binom{2n-2k}{n+m} = \binom{n}{m} 2^{n-m} \quad (\text{and } 2^n \text{ at } m = 0).
  $$
  In `cohort3_wave_1b_dp_and_sums.md` L762, the author accidentally wrote $n - k$ in the lower index ($\sum_{k=0}^n \binom{n}{k}\binom{2n-2k}{n-k}(-1)^k$), which reduces to $[x^n]\frac{(1-x)^n}{\sqrt{1-4x}}$ and **has no closed form**, and then tried to salvage it on L771 with a parenthetical remark about $\sum_{k=0}^n \binom{2k}{k}\binom{2n-2k}{n-k}(-1)^k = [2 \mid n]\binom{n}{n/2} 2^n$.
- **Deterministic Replacement Text for Lines 760–772 of `cohort3_wave_1b_dp_and_sums.md` (Presenting Both Cohort 2's $S_2(n, m)$ and the Central Binomial Convolution $\tilde{S}_n$)**:

```markdown
#### Worked Derivation 2: Alternating Double-Step Binomial Sum & Central Binomial Convolution
- **Target Sums**:
  $$
  S_2(n, m) = \sum_{k=0}^{n} (-1)^k \binom{n}{k} \binom{2n - 2k}{n + m} \quad (0 \le m \le n), \qquad \tilde{S}_n = \sum_{k=0}^{n} (-1)^k \binom{2k}{k} \binom{2n - 2k}{n - k}.
  $$
- **a. Concrete Object**:
  1. $S_2(n, m)$: Alternating sum where $k$ steps by $-2$ in the upper index of $\binom{2n-2k}{n+m}$ while the lower index $n+m$ is independent of $k$.
  2. $\tilde{S}_n$: Alternating Cauchy convolution of central binomial coefficients $\binom{2k}{k}$ and $\binom{2(n-k)}{n-k}$.
- **b. Diagnostic Signal**:
  - In $S_2(n, m)$, $\binom{2n-2k}{n+m} = [z^{n+m}](1 + z)^{2n-2k}$ puts $k$ purely in the exponent of $(1 + z)^{-2}$, which collapses against $(-1)^k \binom{n}{k}$ via the binomial theorem!
  - In $\tilde{S}_n$, the indices $k$ and $n-k$ sum to $n$, signaling a direct Cauchy product of $\sum_{k \ge 0} \binom{2k}{k}(-x)^k = (1 + 4x)^{-1/2}$ and $\sum_{m \ge 0} \binom{2m}{m} x^m = (1 - 4x)^{-1/2}$.
- **c. Step-by-Step Algebraic Derivation**:
  1. **Part A — Evaluating $S_2(n, m)$ (Cohort 2 Worked Derivation 2)**:
     Replace $\binom{2n-2k}{n+m}$ by $[z^{n+m}] (1 + z)^{2n-2k}$. Note that for $k > n - \lceil(n+m)/2\rceil$, the polynomial $(1+z)^{2n-2k}$ has degree $2n - 2k < n + m$, so $[z^{n+m}](1+z)^{2n-2k} = 0$ automatically (no non-zero tail!):
     $$
     S_2(n, m) = [z^{n+m}] (1 + z)^{2n} \sum_{k=0}^{n} \binom{n}{k} \left(-(1 + z)^{-2}\right)^k = [z^{n+m}] (1 + z)^{2n} \left(1 - \frac{1}{(1 + z)^2}\right)^n.
     $$
     Simplify the inner factor $1 - (1+z)^{-2} = \frac{(1+z)^2 - 1}{(1+z)^2} = \frac{z(z + 2)}{(1+z)^2}$:
     $$
     S_2(n, m) = [z^{n+m}] (1 + z)^{2n} \cdot \frac{z^n (z + 2)^n}{(1 + z)^{2n}} = [z^{n+m}] z^n (z + 2)^n = [z^m] (z + 2)^n = \binom{n}{m} 2^{n-m}.
     $$
  2. **Part B — Evaluating $\tilde{S}_n$ via Radical Product Cancellation**:
     Using Kernel **K3** ($\binom{2m}{m} = [x^m](1 - 4x)^{-1/2}$):
     $$
     \tilde{S}_n = [x^n] \left( (1 + 4x)^{-1/2} (1 - 4x)^{-1/2} \right) = [x^n] (1 - 16x^2)^{-1/2} = \begin{cases} \binom{n}{n/2} 2^n & \text{if } 2 \mid n, \\ 0 & \text{if } 2 \nmid n. \end{cases}
     $$
- **d. Hand-Checkable Toy Trace ($n = 2, m = 1$)**:
  - $S_2(2, 1) = \binom{2}{0}\binom{4}{3} - \binom{2}{1}\binom{2}{3} + \binom{2}{2}\binom{0}{3} = 4 - 0 + 0 = 4 = \binom{2}{1} 2^{2-1}$.
  - $\tilde{S}_2 = \binom{0}{0}\binom{4}{2} - \binom{2}{1}\binom{2}{1} + \binom{4}{2}\binom{0}{0} = 6 - 4 + 6 = 8 = \binom{2}{1} 2^2$.
```

---

## Part II: Stream-of-Consciousness Artifacts & Mislabeled Derivations

### Defect 2.1 — Section 5.5 Worked Derivation 5 (`Dixon's Identity`, Lines 821–856)
- **Severity**: **HIGH (Unedited Trial-and-Error Stream-of-Consciousness + Hand-Waved Final Step)**
- **Location**: [`cohort3_wave_1b_dp_and_sums.md#L821-L856`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L821-L856)
- **Diagnosis**:
  Lines 836–856 contain raw trial-and-error text (*"even better, write..."*, *"wait — only $r$ where $r \le b+c$ contributes! Even better..."*, *"Wait: inside the sum..."*) and end by asserting *"This collapses via Chu-Vandermonde to $\frac{(a+b+c)!}{a!b!c!}$"* without completing the reduction.
  Using **Good's (1970) Egorychev Constant-Term + Lagrange Partial-Fraction Proof** makes the derivation 100% rigorous in 4 short steps while directly connecting Section 5 (Constant-Term Extraction) with Section 6.5 (Heaviside Partial Fractions).
- **Deterministic Replacement Text for Lines 821–856 of `cohort3_wave_1b_dp_and_sums.md`**:

```markdown
#### Worked Derivation 5: Dixon's Identity via Egorychev Constant-Term & Good's Partial-Fraction Reduction
- **Target Sum**:
  $$
  S(a, b, c) = \sum_{k \in \mathbb{Z}} (-1)^k \binom{a+b}{a+k} \binom{b+c}{b+k} \binom{c+a}{c+k} = \frac{(a + b + c)!}{a! \, b! \, c!} \qquad (a, b, c \in \mathbb{Z}_{\ge 0}).
  $$
- **a. Concrete Object**: Alternating sum of a product of three cyclic binomial coefficients over $k \in \mathbb{Z}$ (the general $3$-parameter Dixon's Identity; setting $a = b = c = n$ gives $\sum_{k=-n}^n (-1)^k \binom{2n}{n+k}^3 = \frac{(3n)!}{(n!)^3}$).
- **b. Diagnostic Signal**: Three binomial coefficients all containing $k$ in their lower indices have $3$-fold cyclic symmetry $(a, b, c)$. Writing each factor in symmetric Laurent form $\left(1 - \frac{v}{u}\right)^a \left(1 - \frac{u}{v}\right)^b$ turns the sum over $k$ into the **Dyson $n = 3$ constant term** $[u^0 v^0 w^0]$, which collapses via **Lagrange / Heaviside partial fractions**!
- **c. Reverse-Engineering Scratchpad**:
  Observe that in the Laurent ring $\mathbb{K}[u^{\pm 1}, v^{\pm 1}]$:
  $$
  \left(1 - \frac{v}{u}\right)^a \left(1 - \frac{u}{v}\right)^b = (-1)^b \left(\frac{u}{v}\right)^b \left(1 - \frac{v}{u}\right)^{a+b} = \sum_{j=0}^{a+b} (-1)^{b-j} \binom{a+b}{j} \left(\frac{u}{v}\right)^{b-j} = \sum_{k=-a}^{b} (-1)^k \binom{a+b}{a+k} \left(\frac{u}{v}\right)^k,
  $$
  where we set $k = b - j$ and used $\binom{a+b}{b-k} = \binom{a+b}{a+k}$. Multiplying the three cyclic factors in $(u/v), (v/w), (w/u)$ and extracting $[u^0 v^0 w^0]$ forces the three summation indices $k_1, k_2, k_3$ to be equal ($k_1 = k_2 = k_3 = k$) with total sign $(-1)^{3k} = (-1)^k$!
- **d. Step-by-Step Algebraic Derivation**:
  1. **Symmetric Constant-Term Representation (Dyson $N = 3$)**:
     Multiplying the three cyclic expansions above and extracting $[u^0 v^0 w^0]$ gives:
     $$
     S(a, b, c) = [u^0 v^0 w^0] \, F_{a,b,c}(u, v, w),
     $$
     where:
     $$
     F_{a,b,c}(u, v, w) = \left(1 - \frac{v}{u}\right)^a \left(1 - \frac{w}{u}\right)^a \left(1 - \frac{u}{v}\right)^b \left(1 - \frac{w}{v}\right)^b \left(1 - \frac{u}{w}\right)^c \left(1 - \frac{v}{w}\right)^c.
     $$
     *(Note: Equivalently, setting $x = v/u$ and $y = w/v$ yields the 2-variable Egorychev form $S(a,b,c) = (-1)^c [x^{b+c} y^{2c}](1+x)^{a+b}(1+y)^{b+c}(1-xy)^{c+a}$.)*
  2. **Good's (1970) Lagrange Partial-Fraction Identity**:
     By Heaviside partial fractions (or Lagrange interpolation of the constant polynomial $1$ at the three points $u, v, w$):
     $$
     \frac{1}{\left(1 - \frac{v}{u}\right)\left(1 - \frac{w}{u}\right)} + \frac{1}{\left(1 - \frac{u}{v}\right)\left(1 - \frac{w}{v}\right)} + \frac{1}{\left(1 - \frac{u}{w}\right)\left(1 - \frac{v}{w}\right)} = \frac{u^2}{(u-v)(u-w)} + \frac{v^2}{(v-u)(v-w)} + \frac{w^2}{(w-u)(w-v)} = 1.
     $$
  3. **3-Term Pascal Recurrence & Base Case**:
     Multiplying $F_{a,b,c}(u, v, w)$ by the identity above immediately yields:
     $$
     F_{a,b,c} = F_{a-1,b,c} + F_{a,b-1,c} + F_{a,b,c-1} \implies S(a, b, c) = S(a-1, b, c) + S(a, b-1, c) + S(a, b, c-1) \quad (a, b, c \ge 1).
     $$
     When one parameter is $0$ (say $c = 0$), $F_{a,b,0}(u,v,w) = \left(1 - \frac{v}{u}\right)^a \left(1 - \frac{u}{v}\right)^b \left(1 - \frac{w}{u}\right)^a \left(1 - \frac{w}{v}\right)^b$ contains only non-positive powers of $w^{-1}$ (i.e. non-negative powers of $w$), so extracting $[w^0]$ simply sets $w = 0$, leaving:
     $$
     S(a, b, 0) = [u^0 v^0] \left(1 - \frac{v}{u}\right)^a \left(1 - \frac{u}{v}\right)^b = \binom{a + b}{a} = \frac{(a + b + 0)!}{a! \, b! \, 0!}.
     $$
     By induction on $a + b + c$, $S(a, b, c) = \frac{(a + b + c)!}{a! \, b! \, c!}$. $\blacksquare$
- **e. Hand-Checkable Toy Trace ($a = 1, b = 1, c = 1$)**:
  - LHS ($k \in \{-1, 0, 1\}$): $(-1)^{-1} \binom{2}{0}\binom{2}{0}\binom{2}{0} + (-1)^0 \binom{2}{1}\binom{2}{1}\binom{2}{1} + (-1)^1 \binom{2}{2}\binom{2}{2}\binom{2}{2} = -1 + 8 - 1 = 6$.
  - RHS: $\frac{(1+1+1)!}{1! \, 1! \, 1!} = 3! = 6$. Matches!
```

---

### Defect 2.2 — Section 5.5 Worked Derivation 7 (`Formal Residue Change-of-Variables Sum`, Lines 877–893) and Dropped Chebyshev Change-of-Variables Proof from Cohort 2
- **Severity**: **HIGH (Mislabeled Derivation That Pivots Away from Theorem 5.1 + Dropped Cohort 2 Worked Derivation 3 Which Actually Proves Chebyshev's Identity via Theorem 5.1)**
- **Location**: [`cohort3_wave_1b_dp_and_sums.md#L877-L893`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L877-L893)
- **Diagnosis**:
  Worked Derivation 7 is titled `Formal Residue Change-of-Variables Sum`, but Line 882 says *"Wait — even faster: use Rule 1..."* and never uses Theorem 5.1! Meanwhile, **Cohort 2 Worked Derivation 3** ([`cohort2_iter_58_to_62_dp_and_sums.md#L685-L723`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_58_to_62_dp_and_sums.md#L685-L723)) gave a full, rigorous application of Theorem 5.1 (Formal Residue Change of Variables $w = \frac{v}{1-v}, dw = \frac{dv}{(1-v)^2}$) to prove the **Chebyshev / Moriarty Identity** $\sum_{k=0}^{\lfloor n/2 \rfloor} (-1)^k \binom{n-k}{k} (q+q^{-1})^{n-2k} = \frac{q^{n+1}-q^{-(n+1)}}{q-q^{-1}}$, and was completely dropped from Cohort 3!
- **Deterministic Replacement Text for Lines 877–893 of `cohort3_wave_1b_dp_and_sums.md` (Presenting Both the Chebyshev Formal Residue Change-of-Variables Proof and the $\sum_k \binom{2k}{k}\binom{n}{k}(-1/4)^k$ Identity)**:

```markdown
#### Worked Derivation 7: Formal Residue Change-of-Variables Sum (Chebyshev / Moriarty Identity) & Central Binomial Scaling
- **Target Sums**:
  $$
  T_n(q) = \sum_{k=0}^{\lfloor n/2 \rfloor} (-1)^k \binom{n - k}{k} (q + q^{-1})^{n - 2k}, \qquad S_n = \sum_{k=0}^{n} \binom{2k}{k} \binom{n}{k} \left(-\frac{1}{4}\right)^k.
  $$
- **a. Concrete Object**:
  1. $T_n(q)$: Diagonal binomial sum with $n - k$ in the upper index and $k$ in the lower index, coupled with $(q + q^{-1})^{n-2k}$ (whose special case $q = e^{i\theta}$ is Chebyshev's identity $\sum_k (-1)^k \binom{n-k}{k}(2\cos\theta)^{n-2k} = \frac{\sin((n+1)\theta)}{\sin\theta}$, and $q \to 1$ gives $\sum_k (-1)^k \binom{n-k}{k} 2^{n-2k} = n + 1$).
  2. $S_n$: Hypergeometric product of $\binom{2k}{k}$ and $\binom{n}{k}$ weighted by $(-1/4)^k$.
- **b. Diagnostic Signal**:
  - In $T_n(q)$, $k$ appears in both the upper and lower indices of $\binom{n-k}{k}$ and with stride $-2k$ in $(q+q^{-1})^{n-2k}$. Using Rule 3 ($\binom{n-k}{k} = [w^{n-2k}](1-w)^{-k-1}$) aligns the power $n - 2k$, and **Theorem 5.1 (Formal Residue Change of Variables $w = \frac{v}{1-v}$)** eliminates the $k$-dependent denominator!
  - In $S_n$, extracting $\binom{n}{k} = [x^n] x^k (1+x)^n$ turns the inner sum over $k$ into $\sum_{k \ge 0} \binom{2k}{k}(-x/4)^k = (1 + x)^{-1/2}$, which merges directly into $(1+x)^{n - 1/2}$!
- **c. Step-by-Step Algebraic Derivation**:
  1. **Part A — Evaluating $T_n(q)$ via Theorem 5.1 (Formal Residue Change of Variables)**:
     Let $\alpha = q + q^{-1}$. By Egorychev Rule 3, $\binom{n-k}{k} = [w^{n-2k}](1 - w)^{-k-1}$. Shifting $[w^{n-2k}] = [w^n] w^{2k}$:
     $$
     T_n(q) = \sum_{k=0}^{\lfloor n/2 \rfloor} (-1)^k \alpha^{n-2k} [w^n] \frac{w^{2k}}{(1 - w)^{k+1}} = \alpha^n [w^n] \frac{1}{1 - w} \sum_{k=0}^{\lfloor n/2 \rfloor} \left( \frac{-w^2}{\alpha^2 (1 - w)} \right)^k.
     $$
     Since $\operatorname{val}\!\left(\frac{-w^2}{\alpha^2(1-w)}\right) = 2 \ge 1$, terms with $k > \lfloor n/2 \rfloor$ have valuation $2k > n$ and contribute $0$ to $[w^n]$. Extending the geometric series to $k \to \infty$ (or applying the formal residue change of variables $w = \frac{v}{1+v}$, $1 - w = \frac{1-v}{1+v}$, $dw = \frac{dv}{(1+v)^2}$ from Theorem 5.1):
     $$
     T_n(q) = \alpha^n [w^n] \frac{1}{1 - w} \cdot \frac{1}{1 + \frac{w^2}{\alpha^2 (1 - w)}} = \alpha^n [w^n] \frac{1}{1 - w + \alpha^{-2} w^2} = [u^n] \frac{1}{1 - \alpha u + u^2} \quad (u = \alpha w).
     $$
     Since $1 - \alpha u + u^2 = (1 - (q + q^{-1})u + u^2) = (1 - qu)(1 - q^{-1}u)$, Heaviside partial fractions (Section 6.5) yield:
     $$
     T_n(q) = [u^n] \frac{1}{(1 - qu)(1 - q^{-1}u)} = \frac{q^{n+1} - q^{-(n+1)}}{q - q^{-1}} \quad (\text{and } \lim_{q \to 1} T_n(q) = n + 1).
     $$
  2. **Part B — Evaluating $S_n = \sum_{k=0}^n \binom{2k}{k}\binom{n}{k}(-1/4)^k$**:
     Extract $\binom{n}{k} = [x^{n-k}](1 + x)^n = [x^n] x^k (1 + x)^n$ and collapse the inner central binomial series via Kernel **K3** ($\sum_{k \ge 0} \binom{2k}{k} w^k = (1 - 4w)^{-1/2}$ at $w = -x/4$):
     $$
     S_n = [x^n] (1 + x)^n \sum_{k \ge 0} \binom{2k}{k} \left(-\frac{x}{4}\right)^k = [x^n] (1 + x)^n (1 + x)^{-1/2} = [x^n] (1 + x)^{n - 1/2} = \binom{n - 1/2}{n} = 2^{-2n} \binom{2n}{n}.
     $$
- **d. Hand-Checkable Toy Trace ($n = 2$)**:
  - $T_2(q) = \binom{2}{0}(q+q^{-1})^2 - \binom{1}{1}(q+q^{-1})^0 = (q^2 + 2 + q^{-2}) - 1 = q^2 + 1 + q^{-2} = \frac{q^3 - q^{-3}}{q - q^{-1}}$.
  - $S_2 = \binom{0}{0}\binom{2}{0} - \frac{1}{4}\binom{2}{1}\binom{2}{1} + \frac{1}{16}\binom{4}{2}\binom{2}{2} = 1 - 1 + \frac{6}{16} = \frac{3}{8} = 2^{-4}\binom{4}{2}$.
```

---

### Defect 2.3 — Editorial Self-Correction Left Inside Problem 20 (`Codeforces 438E`, Line 1652) & Minor Formula Typo in Problem 19 (`AtCoder ABC 276 G`, Line 1624)
- **Severity**: **MEDIUM (Editorial Polish & Formula Typo)**
- **Locations & Replacements**:
  1. [`cohort3_wave_1b_dp_and_sums.md#L1652`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1652):
     - **Current Text**:
       `You are given a set $S = \{c_1, c_2, \dots, c_n\}$ of $n$ distinct positive integer weights. A rooted binary tree (where every vertex has either $0$ or $2$ ordered children, or an empty tree; wait: in CF 438E, every vertex has a weight chosen from $S$, and each vertex can have a left child, right child, both, or neither, i.e., $T = \mathcal{E} + \mathcal{C} \times T \times T$). For every total weight $s = 1, 2, \dots, m$, find the number of valid vertex-weighted rooted binary trees whose vertex weights sum to $s$, modulo $998244353$.`
     - **Replacement Text**:
       `You are given a set $S = \{c_1, c_2, \dots, c_n\}$ of $n$ distinct positive integer weights. A valid vertex-weighted rooted binary tree is a rooted binary tree in which every vertex is assigned a weight from $S$, and each vertex may have a left child, a right child, both, or neither (equivalently, viewing missing children as empty trees $\mathcal{E}$ of weight $0$, the combinatorial class $\mathcal{T}$ satisfies $\mathcal{T} = \mathcal{E} + \mathcal{C} \times \mathcal{T} \times \mathcal{T}$). For every total weight $s = 1, 2, \dots, m$, find the number of valid non-empty vertex-weighted rooted binary trees whose vertex weights sum to $s$, modulo $998244353$.`
  2. [`cohort3_wave_1b_dp_and_sums.md#L1624`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1624):
     - **Current Text**:
       `reducing the entire problem to $[x^M] \frac{1+x+x^2}{1-x} \cdot \left(\frac{x+x^2}{1-x^3}\right)^{N-1} \cdot \frac{1}{1-x^3}$, which evaluates in **strictly $\mathcal{O}(N + M)$ linear time**!`
     - **Replacement Text**:
       `reducing the entire problem to $[x^M] \left(\frac{1+x+x^2}{1-x^3}\right)^2 \left(\frac{x+x^2}{1-x^3}\right)^{N-1} = [x^M] (1+x+x^2)^2 \frac{x^{N-1}(1+x)^{N-1}}{(1-x^3)^{N+1}}$, which evaluates in **strictly $\mathcal{O}(N + M)$ linear time**!`

---

## Part III: Zero-Information-Loss Audit Against Cohort 1 & Cohort 2 (Omitted Content with Complete Insertion Blocks)

### Omission 3.1 — Dropped 1st- and 2nd-Moment Weighted Vandermonde Identities in Section 4.2
- **Source**: [`cohort2_iter_58_to_62_dp_and_sums.md#L872-L873`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_58_to_62_dp_and_sums.md#L872-L873) (and explicitly promised in `cohort3_wave_1b_dp_and_sums.md` Section 1.1 Line 24!)
- **Target Insertion Point**: Append after Line 541 of [`cohort3_wave_1b_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L541).
- **Complete Insertion Block**:

```markdown
- **Identity 4 (1st- and 2nd-Moment Weighted Vandermonde Convolutions via the Euler Operator $\vartheta_x = x\frac{d}{dx}$)**:
  Applying the pointing / Euler differential operator $\vartheta_x = x \frac{d}{dx}$ to the first factor $(1 + x)^r$ in $(1 + x)^r (1 + x)^s$ before multiplying yields:
  1. **First Moment**: Since $\vartheta_x \big((1+x)^r\big) = r x (1+x)^{r-1}$, multiplying by $(1+x)^s$ and extracting $[x^n]$ gives:
     $$
     \sum_{k=0}^{n} k \binom{r}{k} \binom{s}{n-k} = [x^n] \, r x (1 + x)^{r+s-1} = r \binom{r+s-1}{n-1}.
     $$
  2. **Second Moment**: Applying $\vartheta_x^2 \big((1+x)^r\big) = r x (1+x)^{r-1} + r(r-1) x^2 (1+x)^{r-2}$, multiplying by $(1+x)^s$, and extracting $[x^n]$ gives:
     $$
     \sum_{k=0}^{n} k^2 \binom{r}{k} \binom{s}{n-k} = r \binom{r+s-1}{n-1} + r(r-1) \binom{r+s-2}{n-2}.
     $$
  3. **General $m$-th Moment**: Decomposing $k^m = \sum_{j=0}^m \left\{ \begin{matrix} m \\ j \end{matrix} \right\} k^{\underline{j}}$ via Stirling numbers of the second kind (Section 4.6) and using $k^{\underline{j}} \binom{r}{k} = r^{\underline{j}} \binom{r-j}{k-j}$ yields:
     $$
     \sum_{k=0}^{n} k^m \binom{r}{k} \binom{s}{n-k} = \sum_{j=0}^{m} \left\{ \begin{matrix} m \\ j \end{matrix} \right\} r^{\underline{j}} \binom{r+s-j}{n-j}.
     $$
```

---

### Omission 3.2 — Dropped Boundary Warning (`n = 0, m = 0` Lower-Index Symmetry Trap) in Worked Derivation 1 (Line 758)
- **Source**: [`iter_06_to_10_dp_and_sums.md#L713-L718`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_06_to_10_dp_and_sums.md#L713-L718) (Cohort 1 Walkthrough 8.3.2 `f. Failure Modes & Off-By-One Diagnostics`)
- **Target Insertion Point**: Append immediately after Line 758 of [`cohort3_wave_1b_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L758).
- **Complete Insertion Block**:

```markdown
  > [!WARNING]
  > **Boundary Trap at $n = 0, m = 0$ ($\binom{n-1}{n-m}$ vs. $\binom{n-1}{m-1}$)**:
  > Notice that $[x^{n-m}](1 - x)^{-m} = (-1)^{n-m} \binom{-m}{n-m} = \binom{n-1}{n-m}$. When $n \ge 1$, lower-index symmetry gives $\binom{n-1}{n-m} = \binom{n-1}{m-1}$. However, at the boundary **$n = 0, m = 0$**, the original sum has $k = 0$ term $\binom{0}{0}\binom{0}{0}\frac{1}{1} = 1$, which matches $\binom{n-1}{n-m} = \binom{-1}{0} = 1$, whereas $\binom{n-1}{m-1} = \binom{-1}{-1} = 0$ **fails** because lower-index symmetry $\binom{A}{B} = \binom{A}{A-B}$ is invalid for negative upper index $A = -1$! Always keep the form $\binom{n-1}{n-m}$ directly produced by $[x^{n-m}](1-x)^{-m}$.
```

---

### Omission 3.3 — Three Dropped Worked Derivations from Cohort 1 & Cohort 2 in Section 5.5
- **Sources**:
  1. **Cohort 1 Walkthrough 8.3.3** ([`iter_06_to_10_dp_and_sums.md#L721-L757`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_06_to_10_dp_and_sums.md#L721-L757)): $\sum_{k=0}^n (-1)^k \binom{n}{k} \binom{k+r}{m} = (-1)^n \binom{r}{m-n}$ and the negative-upper-index boundary warning for $\sum_{k=0}^n (-1)^k \binom{n}{k} \binom{r-k}{m} = \binom{r-n}{m-n}$.
  2. **Cohort 1 Walkthrough 8.3.5** ([`iter_06_to_10_dp_and_sums.md#L800-L834`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_06_to_10_dp_and_sums.md#L800-L834)): Double upper-negation Cauchy product $\sum_{k=0}^n \binom{n+k}{k} \binom{2n-k}{n-k} = \binom{3n+1}{n}$ (explicitly promised in `cohort3` Line 25!).
  3. **Cohort 2 Worked Derivation 4** ([`cohort2_iter_58_to_62_dp_and_sums.md#L726-L750`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_58_to_62_dp_and_sums.md#L726-L750)): Li Shanlan / Strehl's identity $\sum_{k=0}^n \binom{n}{k}^2 \binom{n+k}{k} = \sum_{j=0}^n \binom{n}{j}^2 \binom{2n-j}{n-j}$.
- **Target Insertion Point**: Insert after Worked Derivation 7 (Line 893 of [`cohort3_wave_1b_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L893)), updating the Section 5.5 heading from `7 Complete "Zero Magic Steps" Worked Derivations` to `10 Complete "Zero Magic Steps" Worked Derivations`.
- **Complete Insertion Block**:

```markdown
#### Worked Derivation 8: Alternating Vandermonde Shift & The Negative-Upper-Index Boundary Warning *(Cohort 1 Walkthrough 8.3.3)*
- **Target Sums**:
  $$
  A(n, m, r) = \sum_{k=0}^{n} (-1)^k \binom{n}{k} \binom{k + r}{m}, \qquad B(n, m, r) = \sum_{k=0}^{n} (-1)^k \binom{n}{k} \binom{r - k}{m}.
  $$
- **a. Diagnostic Signal**: The factor $(-1)^k \binom{n}{k}$ is the $n$-th backward difference kernel, while $\binom{k+r}{m} = [x^m](1+x)^{k+r}$ has $k$ in the upper index and a fixed non-negative integer $m$ in the lower index.
- **b. Step-by-Step Algebraic Derivation**:
  1. **Evaluating $A(n, m, r)$**:
     Substitute $\binom{k+r}{m} = [x^m] (1 + x)^{k+r}$:
     $$
     A(n, m, r) = [x^m] (1 + x)^r \sum_{k=0}^{n} \binom{n}{k} (-1)^k (1 + x)^k = [x^m] (1 + x)^r \big(1 - (1 + x)\big)^n = (-1)^n [x^{m-n}] (1 + x)^r = (-1)^n \binom{r}{m - n}.
     $$
  2. **Evaluating $B(n, m, r)$**:
     Substitute $\binom{r-k}{m} = [x^m] (1 + x)^{r-k}$ (which holds for **all** $r - k \in \mathbb{Z}$, even when $r - k < 0$, because the generalized binomial series $(1+x)^{r-k} = \sum_{m \ge 0} \binom{r-k}{m} x^m$ matches the falling-factorial definition of $\binom{r-k}{m}$!):
     $$
     B(n, m, r) = [x^m] (1 + x)^r \sum_{k=0}^{n} \binom{n}{k} \big(-(1 + x)^{-1}\big)^k = [x^m] (1 + x)^r \left(\frac{x}{1 + x}\right)^n = [x^{m-n}] (1 + x)^{r-n} = \binom{r - n}{m - n}.
     $$
- **c. Hand-Checkable Toy Trace ($n = 2, m = 2, r = 1$, where $r - k$ becomes negative at $k = 2$)**:
  - For $k = 0$: $(-1)^0 \binom{2}{0}\binom{1}{2} = 0$.
  - For $k = 1$: $(-1)^1 \binom{2}{1}\binom{0}{2} = 0$.
  - For $k = 2$: $(-1)^2 \binom{2}{2}\binom{-1}{2} = 1 \cdot \frac{(-1)(-2)}{2!} = 1$.
  - Total $B(2, 2, 1) = 1$, which matches $\binom{r-n}{m-n} = \binom{-1}{0} = 1$!

---

#### Worked Derivation 9: Double Upper-Negation Cauchy Product *(Cohort 1 Walkthrough 8.3.5)*
- **Target Sum**:
  $$
  S_n = \sum_{k=0}^{n} \binom{n + k}{k} \binom{2n - k}{n - k} \qquad (n \ge 0).
  $$
- **a. Diagnostic Signal**: Both binomial coefficients have $k$ in **both** the upper and lower indices, and the lower indices $k$ and $n - k$ sum to $n$. However, the upper indices $(n+k)$ and $(2n-k)$ also vary with $k$, blocking direct Vandermonde! Applying **Upper Negation (Rule 3)** moves the constant difference $(n+k) - k = n$ into the exponent of $(1 - x)^{-n-1}$!
- **b. Step-by-Step Algebraic Derivation**:
  1. **Upper Negation on Both Factors**:
     - Factor 1: $\binom{n + k}{k} = (-1)^k \binom{-n - 1}{k} = [x^k] (1 - x)^{-n-1}$.
     - Factor 2: $\binom{2n - k}{n - k} = (-1)^{n-k} \binom{-n - 1}{n - k} = [x^{n-k}] (1 - x)^{-n-1}$.
  2. **Cauchy Product Collapse**:
     $$
     S_n = \sum_{k=0}^{n} \Big([x^k] (1 - x)^{-n-1}\Big) \Big([x^{n-k}] (1 - x)^{-n-1}\Big) = [x^n] (1 - x)^{-2n-2} = \binom{n + (2n + 2) - 1}{n} = \binom{3n + 1}{n}.
     $$
- **c. Hand-Checkable Toy Trace ($n = 2$)**:
  - LHS: $\binom{2}{0}\binom{4}{2} + \binom{3}{1}\binom{3}{1} + \binom{4}{2}\binom{2}{0} = 6 + 9 + 6 = 21$.
  - RHS: $\binom{3(2)+1}{2} = \binom{7}{2} = 21$. Matches!

---

#### Worked Derivation 10: Li Shanlan's / Strehl's Identity via Egorychev Basis Transformation *(Cohort 2 Worked Derivation 4)*
- **Target Identity**:
  $$
  L_n = \sum_{k=0}^{n} \binom{n}{k}^2 \binom{n + k}{k} = \sum_{j=0}^{n} \binom{n}{j}^2 \binom{2n - j}{n - j}.
  $$
- **a. Diagnostic Signal**: Shows what to do when Egorychev extraction does **not** collapse to a single binomial coefficient: expanding the inner polynomial in a shifted basis $(1 + w) = (1 + z) - (z - w)$ transforms one hypergeometric sum into a dual hypergeometric sum!
- **b. Step-by-Step Algebraic Derivation**:
  1. **Extract Two Factors of $L_n$**:
     Write $\binom{n}{k} = \binom{n}{n-k} = [z^{n-k}](1 + z)^n$ and $\binom{n+k}{k} = \binom{n+k}{n} = [w^n](1 + w)^{n+k}$:
     $$
     L_n = [z^n w^n] (1 + z)^n (1 + w)^n \sum_{k=0}^{n} \binom{n}{k} z^k (1 + w)^k = [z^n w^n] (1 + z)^n (1 + w)^n \big(1 + z(1 + w)\big)^n.
     $$
  2. **Basis Shift $1 + z(1 + w) = (1 + z) + zw$**:
     Expand $\big((1 + z) + zw\big)^n = \sum_{j=0}^n \binom{n}{j} (1 + z)^{n-j} z^j w^j$ by the binomial theorem:
     $$
     L_n = \sum_{j=0}^{n} \binom{n}{j} \Big([z^n] z^j (1 + z)^{2n-j}\Big) \Big([w^n] w^j (1 + w)^n\Big) = \sum_{j=0}^{n} \binom{n}{j}^2 \binom{2n - j}{n - j}. \quad \blacksquare
     $$
```

---

### Omission 3.4 — Dropped Pitfall Callout Boxes in Section 5.6 (Lines 896–905)
- **Source**: [`cohort2_iter_58_to_62_dp_and_sums.md#L783-L798`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_58_to_62_dp_and_sums.md#L783-L798)
- **Target Insertion Point**: Append after Line 905 of [`cohort3_wave_1b_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L905).
- **Complete Insertion Block**:

```markdown
> [!CAUTION]
> **Pitfall 1 (The Non-Zero Tail Trap When Extending $k \to \infty$)**:
> Suppose you want to evaluate $\sum_{k=0}^n \binom{n-k}{m} c^k$ and you substitute $\binom{n-k}{m} = [w^m] (1 + w)^{n-k}$. You **cannot** extend the upper limit $k = n$ to $k = \infty$! Why? Because for $k > n$, the exponent $n - k$ is **negative**, and $(1 + w)^{n-k} = \sum_{j \ge 0} \binom{n-k}{j} w^j$ is an infinite negative-binomial power series whose $[w^m]$ coefficient is $\binom{n-k}{m} = (-1)^m \binom{k-n+m-1}{m} \neq 0$!
> **Correct Fix**: Use Rule 4 ($\binom{n-k}{m} = [w^{n-k-m}](1 - w)^{-m-1} = [w^{n-m}] w^k (1 - w)^{-m-1}$). Then for $k > n - m$, the term $w^k (1 - w)^{-m-1}$ has formal valuation $k > n - m$, so its $[w^{n-m}]$ coefficient is **identically zero**, making the extension $k \to \infty$ 100% legal in $\mathbb{K}[[w]]$!

> [!CAUTION]
> **Pitfall 2 (Non-Convergent Geometric Series in the Formal Topology)**:
> After swapping $[w^n]$ and $\sum_{k \ge 0} R(w)^k$, the infinite geometric sum $\sum_{k \ge 0} R(w)^k = \frac{1}{1 - R(w)}$ is valid in $\mathbb{K}[[w]]$ **if and only if** $\operatorname{val}(R(w)) \ge 1$ (i.e., $R(0) = 0$) or the sum over $k$ is kept finite ($0 \le k \le n$) and collapsed via $\sum_{k=0}^n \binom{n}{k} R(w)^k = (1 + R(w))^n$. Never sum an infinite geometric series $\sum_{k=0}^\infty R(w)^k$ when $[w^0] R(w) \neq 0$!
```

---

### Omission 3.5 — Dropped C++ Reference Kernels in Sections 4.3 & 6.3
- **Sources**:
  1. **Cohort 1 Iteration 08 Difference Convolution C++ Kernel** ([`iter_06_to_10_dp_and_sums.md#L911-L929`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_06_to_10_dp_and_sums.md#L911-L929))
  2. **Cohort 2 Iteration 62 $k$-th Order Prefix Sum C++ Kernel** ([`cohort2_iter_58_to_62_dp_and_sums.md#L942-L964`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_58_to_62_dp_and_sums.md#L942-L964))
- **Target Insertion Point 1**: Insert at the end of Section 4.3 Archetype 1 (after Line 558 of [`cohort3_wave_1b_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L558)).

```markdown
- **Reference C++ Kernel (Cross-Correlation / Difference-Index Convolution with Offset Verification)**:
  ```cpp
  // Computes D[d] = sum_{i - j = d} A[i] * B[j] for d in [-(m - 1), n - 1]
  // Returned array `res` is shifted by +(m - 1), so D[d] is stored at res[d + m - 1].
  vector<long long> diff_convolution(const vector<long long>& A, const vector<long long>& B) {
      int n = (int)A.size(), m = (int)B.size();
      vector<long long> B_rev(m);
      for (int j = 0; j < m; ++j) B_rev[m - 1 - j] = B[j];
      vector<long long> C = multiply(A, B_rev); // Standard NTT / polynomial multiplication
      // For any d in [-(m - 1), n - 1]: D[d] = C[d + m - 1]
      return C;
  }
  ```
```

- **Target Insertion Point 2**: Insert at the end of Section 6.3 (after Line 960 of [`cohort3_wave_1b_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L960)).

```markdown
- **Reference C++ Kernel ($\mathcal{O}(n \log n)$ $k$-th Order Prefix Sum / Difference Operator for $k \le 10^{18}$)**:
  ```cpp
  // Computes b[i] = [x^i] (1 - x)^(-k) * A(x) mod MOD for 0 <= i < n.
  // Works for any integer k (positive for k-th prefix sum, negative for (-k)-th difference).
  vector<long long> kth_prefix_sum(const vector<long long>& a, long long k,
                                   const vector<long long>& inv, long long MOD) {
      int n = (int)a.size();
      long long km = ((k % MOD) + MOD) % MOD;
      if (km == 0) return a; // (1 - x)^0 = 1 (e.g., k is a multiple of p)
      vector<long long> w(n, 0);
      w[0] = 1;
      for (int j = 1; j < n; ++j) {
          w[j] = w[j - 1] * ((km - 1 + j) % MOD) % MOD * inv[j] % MOD;
      }
      vector<long long> c = multiply(a, w); // 1D NTT convolution
      c.resize(n);
      return c;
  }
  ```
```

---

## Part IV: Pedagogical & Structural Audit (`AGENTS.md` Compliance)

### Finding 4.1 — Heading Format & Zero Magic Steps Scaffolding Seam at Line 498
- **Location**: [`cohort3_wave_1b_dp_and_sums.md#L498-L1066`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L498-L1066)
- **Diagnosis**:
  - Lines 1–497 use top-level headings `## Section 1: ...`, `## Section 2: ...`, `## Section 3: ...` and include explicit `a–f` Zero Magic Steps blocks (`Concrete Object`, `Diagnostic Signal`, `Reverse-Engineering Scratchpad`, `Step-by-Step Derivation`, `Hand-Checkable Toy Trace`, `Failure Modes`).
  - Starting at Line 498, top-level headings switch to `## 4. Iteration 08 / 60: ...`, `## 5. Iteration 09 / 61: ...`, `## 6. Iteration 10 / 62 (Part A): ...`, `## 7. ...`, `## 8. ...`.
  - Applying the replacement blocks in Parts I–III above restores the `a–e` Zero Magic Steps scaffolding, toy traces, failure modes, and C++ reference kernels across Sections 4, 5, and 6.
  - Additionally, normalize the top-level headings at Lines 498, 652, 908, 1023, and 1066 to `## Section 4: ...`, `## Section 5: ...`, `## Section 6: ...`, `## Section 7: ...`, `## Section 8: ...` so the entire 8-section document has a uniform heading hierarchy.

---

## Summary Checklist for Deterministic Remediation

1. **Replace Lines 1500–1528 (`Problem 15: AtCoder JSC 2019 Qual F`)** with the Defect 1.1 block (and update `problem_archive.md` Lines 629–635 with the same corrected OGF $G_{\text{comp}}(x) = \frac{\binom{N}{M}}{(1-x)^N} \sum_{d \ge 1} (x^{Md} - x^{M(d+1)})(1-x^d)^{N-M}$).
2. **Replace Lines 1076–1110 (`Problem 1: AtCoder fps-24 A — Snack`)** with the Defect 1.2 block (restoring the true AtCoder costs $\{1, 3, 4, 6\}$ and Cohort 2's $\mathcal{O}(D)$ factorization $x(1+x^2)(1+x^3)$ alongside the $\mathcal{O}(N)$ D-finite recurrence).
3. **Replace Lines 858–875 (`Worked Derivation 6`)** with the Defect 1.3 block (fixing the off-by-one closed form to $\frac{(-1)^n (m!)^2}{(m-n)!(m+n+1)!}$ and providing the complete Heaviside partial-fraction proof).
4. **Replace Lines 794–820 (`Worked Derivation 4`)** with the Defect 1.4 block (completing the aborted derivation to $\binom{2m}{2n}$ and $\binom{2m+1}{2n}$).
5. **Replace Lines 760–772 (`Worked Derivation 2`)** with the Defect 1.5 block (restoring Cohort 2's $S_2(n, m) = \binom{n}{m}2^{n-m}$ alongside $\tilde{S}_n$).
6. **Replace Lines 821–856 (`Worked Derivation 5: Dixon's Identity`)** with the Defect 2.1 block (replacing the trial-and-error scratchpad with Good's 4-step constant-term + Lagrange partial-fraction proof).
7. **Replace Lines 877–893 (`Worked Derivation 7`)** with the Defect 2.2 block (restoring Cohort 2's Chebyshev Formal Residue Change-of-Variables proof alongside $S_n = 2^{-2n}\binom{2n}{n}$).
8. **Apply the 2 minor edits in Defect 2.3** (Line 1652 in `CF 438E` and Line 1624 in `ABC 276 G`).
9. **Insert Omissions 3.1–3.5** (Section 4.2 weighted Vandermonde identities, Line 758 boundary warning, Worked Derivations 8–10, Section 5.6 Pitfalls 1 & 2, and the two C++ reference kernels in Sections 4.3 & 6.3).
10. **Normalize top-level headings** at Lines 498, 652, 908, 1023, and 1066 to `## Section 4..8`.
