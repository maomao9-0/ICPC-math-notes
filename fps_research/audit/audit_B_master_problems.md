# Master Problem Synthesis Audit Report — Inspector B (`audit_B_master_problems.md`)

- **Target Files Audited**:
  1. [PROBLEM_CURATION.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md) (899 lines)
  2. [problem_archive.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md) (1,702 lines)
- **Cross-Checked Authorities**:
  - All 10 Cohort 3 Master Wave Reports (`cohort3_wave_1a_*.md` through `cohort3_wave_5b_*.md`)
  - All 10 Wave Audit Reports ([audit_A_wave_1a.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/audit/audit_A_wave_1a.md) through [audit_A_wave_5b.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/audit/audit_A_wave_5b.md))
  - Inspector A's Master Problem Report ([audit_A_master_problems.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/audit/audit_A_master_problems.md))
- **Auditor**: Inspector B-Problems (Independent Second-Pass Mathematical & Pedagogical Verification)

---

## Executive Summary

An independent line-by-line and Python-verified audit of `PROBLEM_CURATION.md` and `problem_archive.md` — cross-referenced against all 10 Cohort 3 wave files, all 10 `audit_A_wave_*.md` reports, and `audit_A_master_problems.md` — revealed three major classes of defects that must be remediated together:

1. **Errors & Omissions in Inspector A's Report (`audit_A_master_problems.md`) Caught by Inspector B (Section 1)**:
   - **2 Missed Unescaped Pipes (`|\Sigma|`) in `PROBLEM_CURATION.md`** at **L571** and **L626** (Inspector A caught 9 of 11).
   - **Misidentified Problem (`fps_24_d` vs. `fps_24_g`) and Off-by-50 Line Citations in Inspector A's Issue 2.1**: Inspector A conflated `fps_24_d` (*Sequence 2*, at `1A#L656`) with `fps_24_g` (*Modulo*, at `1A#L693–L695`), and cited non-existent or shifted line numbers (`1A#L695, L720, L797, L821, L914`) in its proposed replacement table for Ladder 2.1.
   - **Major Systemic Blind Spot in `audit_A_master_problems.md`**: Inspector A compared `PROBLEM_CURATION.md` and `problem_archive.md` only against the **un-remediated** `cohort3_wave_*.md` headers and **failed to cross-check against `audit_A_wave_1a.md` through `audit_A_wave_5b.md`**. Consequently, Inspector A missed **21 mathematical/statement bugs** propagated into `problem_archive.md` and `PROBLEM_CURATION.md`, plus **brand-new mathematical errors** unique to `problem_archive.md` (such as a completely false OGF for `Codeforces 1821F — Timber` at `problem_archive.md#L1391`).
2. **Mathematical Formula Bugs & Hallucinated Problem Statements in `problem_archive.md` and `PROBLEM_CURATION.md` (Section 2)**:
   - **21 exact mathematical / problem-statement fixes** verified by Python scripts, including `Codeforces 1821F` (`L1391`), `AtCoder fps_24_a` (`L17, L294–L300`), `fps_24_d` (`L20, L308–L313`), `fps_24_f` (`L22, L1215–L1217`), `fps_24_g` (`L23, L301–L306`), `fps_24_h` (`L24, L716–L721`), `fps_24_l` (`L28, L322–L327`), `fps_24_n` (`L30, L340–L345, L817–L818`), `fps_24_o` (`L31, L442–L447`), `fps_24_q` (`L33, L840–L845`), `fps_24_r` (`L34, L926–L931`), `fps_24_s` (`L35, L509–L514`), `fps_24_t` (`L36, L449–L454`), `fps_24_v` (`L38, L789–L794`), `CF 1251F` (`L137`), `ABC 300 Ex` (`L68, L737–L742`), `LOJ 6077` (`L251, L775–L780`), `AGC 054 E` (`L99, L799–L804`), `Luogu P5206` (`L1012–L1014`), `CF 1528F` (`L1146–L1148`), `Luogu P7364` (`L225, L1183–L1187`), `ABC 279 Ex` (`L63, L1305–L1307`), and `CF 755G` (`L1472–L1476`).
3. **Cross-Wave Pointer Bugs & Wave-Audit Restored Problems (Section 3)**:
   - Exact line-by-line pointer fixes in `problem_archive.md` (`L183`, `L218`, `L219`) and corrected replacement tables for `PROBLEM_CURATION.md` that incorporate both Inspector A's structural alignment and the wave audits' mathematical corrections.

---

## 1. Corrections & Additions to Inspector A's Report (`audit_A_master_problems.md`)

### 1.1 Two Additional Unescaped Pipes (`|`) in `PROBLEM_CURATION.md` Missed by Inspector A
In [audit_A_master_problems.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/audit/audit_A_master_problems.md#L334-L364) (Issue 5.1), Inspector A listed 9 lines in `PROBLEM_CURATION.md` containing unescaped `|` inside `$...$` within Markdown tables (`L56, L343, L344, L387, L401, L445, L446, L629, L830`), but **missed 2 additional lines** where `|\Sigma|` inside `$...$` corrupts Markdown table column parsing:

1. **[PROBLEM_CURATION.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md#L571) (L571)**:
   - **Current (Broken)**:
     ```markdown
     | **CP1-4** (`CF 954I`) | Cross-Correlation Indicator + DSU on $|\Sigma|=6$ Graph | $\sum_{t=0}^{m-1} (S_{i+t} - T_t)^2 = 0$ (Wildcard String Matching) | $\implies$ For each pair $(c_1, c_2) \in \Sigma^2$, convolve $A_{c_1}(x) B_{c_2}^R(x)$ via FFT to find which character pairs must be merged at each alignment offset |
     ```
   - **Replacement (Fixed)**:
     ```markdown
     | **CP1-4** (`CF 954I`) | Cross-Correlation Indicator + DSU on $\lvert\Sigma\rvert=6$ Graph | $\sum_{t=0}^{m-1} (S_{i+t} - T_t)^2 = 0$ (Wildcard String Matching) | $\implies$ For each pair $(c_1, c_2) \in \Sigma^2$, convolve $A_{c_1}(x) B_{c_2}^R(x)$ via FFT to find which character pairs must be merged at each alignment offset |
     ```
2. **[PROBLEM_CURATION.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md#L626) (L626)**:
   - **Current (Broken)**:
     ```markdown
     | **CP2-5** (`CSES 1112`) | Complementary Pattern-Avoidance OGF $[x^N]\frac{A_P(x)}{(1 - |\Sigma|x)A_P(x) + x^M}$ |Wave 2B (#21) | — |
     ```
   - **Replacement (Fixed)**:
     ```markdown
     | **CP2-5** (`CSES 1112`) | Complementary Pattern-Avoidance OGF $[x^N]\frac{A_P(x)}{(1 - \lvert\Sigma\rvert x)A_P(x) + x^M}$ | Wave 2B (#21) | — |
     ```

*(Note: All 9 lines in `PROBLEM_CURATION.md` and all 3 lines in `problem_archive.md` at `L139, L181, L264` flagged by Inspector A in Issues 5.1–5.2 are confirmed valid.)*

---

### 1.2 Correction to Inspector A's Issue 2.1 (`PROBLEM_CURATION.md` L315–L331 — Ladder 2.1)
In [audit_A_master_problems.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/audit/audit_A_master_problems.md#L78-L97), Inspector A's replacement block for **Section 2.1 (`PROBLEM_CURATION.md` L315–L331)** contains three factual errors:
1. **Conflation of `fps_24_d` and `fps_24_g`**: Inspector A wrote that `1A-6` is `AtCoder fps_24_d — Sequence 2 — Modular Residue Extraction [y^0] \prod_{i=1}^N (y + \frac{x}{1-x} - x)` at `1A#L695`. In fact:
   - In `cohort3_wave_1a_modelling_foundations.md`, **Problem 3 (`1A#L656`)** is `fps_24_d` (*Sequence 2 / 数列 2* — non-decreasing sequences $0 \le A_1 \le \dots \le A_N \le M$ with $A_i \not\equiv A_{i+1} \pmod 2$, solved by $[x^{M-N+1}]\frac{1}{(1-x)^2(1-x^2)^{N-1}}$; see `audit_A_wave_1a.md` Bug M-1).
   - **Problem 5 (`1A#L693–L695`)** is `fps_24_g` (*Modulo* — for each $k=1,\dots,M$, count sequences of length $N$ summing to $S$ with no element $\equiv 0 \pmod k$, solved via $f(k) = [x^S]\left(\frac{x - x^k}{1 - x} + \frac{x^{k+1} - x^{2k}}{1 - x} + \dots\right)^N = [x^S]\left(\frac{x}{1-x} - \frac{x^k}{1-x^k}\right)^N$).
2. **Propagated Wrong Formula for `fps_24_a` (`1A-1`)**: Inspector A retained `[x^{S-N}](1 + x + x^2 + x^4)^N`, which corresponds to snack costs $\{1,2,3,5\}$ instead of the official `fps_24_a` costs $\{1,3,4,6\}$: $[x^N](x + x^3 + x^4 + x^6)^D = [x^{N-D}](1 + x^2)^D(1 + x^3)^D$ (`audit_A_wave_1a.md` Bug M-2).
3. **Wrong Line Numbers in `cohort3_wave_1a_modelling_foundations.md`**: `cohort3_wave_1a_modelling_foundations.md` has 939 lines total. The actual line numbers in `1A` are:
   - Problem 1 (`fps_24_a`): `1A#L628`
   - Problem 3 (`fps_24_d`): `1A#L656`
   - Problem 4 (`CF 993E`): `1A#L670`
   - Problem 5 (`fps_24_g`): `1A#L693`
   - Problem 6 (`CF 1251F`): `1A#L682` (or `L705`)
   - Problem 11 (`CF 755G`): `1A#L755`
   - Problem 15 (`CF 623E`): `1A#L783`
   - Problem 27 (`CF 438E`): `1A#L868`

#### Deterministic Replacement for `PROBLEM_CURATION.md` L315–L331 (Superseding Inspector A's Issue 2.1):
```markdown
### 2.1 Wave 1A: Generating Function Foundations & Symbolic Method (`cohort3_wave_1a_modelling_foundations.md`)
*Target*: **31 Problems** (6 Stepping Stone, 9 Intermediate, 11 Advanced, 5 Mastery). Full problem statements, 3-tier hints, and derivations in `cohort3_wave_1a_modelling_foundations.md` §7 (`L625–L935`) and `problem_archive.md` §2.

| Slot | Tier | Problem ID & Title | Core FPS / Combinatorial Technique | Reference Pointer |
| :--- | :--- | :--- | :--- | :--- |
| **1A-1** | Stepping Stone | **AtCoder `fps_24_a`** — Snack (`お菓子`) — Fixed-Count Snack OGF | Factor out $x^D$ from $(x + x^3 + x^4 + x^6)^D = x^D (1 + x^2)^D (1 + x^3)^D$ and extract $[x^{N-D}]$ in $O(D)$ | `1A#L628`, `Arch#1A-1` |
| **1A-2** | Stepping Stone | **AtCoder `fps_24_c`** — Sequence (`数列`) — Bounded Composition OGF | Finite geometric series $[x^S]\left(\frac{1-x^{M+1}}{1-x}\right)^N$ expanded in $O(S/M)$ via binomial convolution | `1A#L642`, `Arch#T43` |
| **1A-3** | Stepping Stone | **AtCoder `fps_24_d`** — Sequence 2 (`数列 2`) — Alternating-Parity Difference OGF | Difference encoding $d_i = A_{i+1} - A_i \equiv 1 \pmod 2$: $[x^{M-N+1}]\frac{1}{(1-x)^2(1-x^2)^{N-1}}$ in $O(M)$ | `1A#L656`, `Arch#1A-3` |
| **1A-4** | Stepping Stone | **Codeforces 993E** — Nikita and Order Statistics | Prefix-sum frequency polynomial $P(x)$ convolved with reversed $P(x^{-1})$ via FFT | `1A#L670`, `Arch#1B-17` |
| **1A-5** | Stepping Stone | **Codeforces 1251F** — Red-White Fence | Multiplicity saturation $(1+2x)^{c_1}(1+x)^{2c_2}$ per red board height | `1A#L682`, `Arch#1A-11` |
| **1A-6** | Stepping Stone | **AtCoder `fps_24_g`** — Modulo (`コイン`) — Sliding-Window / Residue-Exclusion OGF | Reversible knapsack DP multiplying by $(1-x^k)$ and dividing by $(1-x^{k+L})$ in $O(NM)$ | `1A#L693`, `Arch#1A-2` |
| **1A-7..15** | Intermediate | **9 Problems**: `fps_24_i` (Set), `fps_24_j` (Magick), `fps_24_k` (Derangement EGF $e^{-x}/(1-x)$), `fps_24_l` (Cycle-Avoiding EGF $e^{-x^2/2}/(1-x)$), `CF 755G` (PolandBall Bivariate OGF), `Luogu P4389` (付公主的背包 Harmonic $\ln$-$\exp$), `Luogu P4841` / `fps_24_m` (Connected Graphs $\ln G(x)$), `LOJ #6268` / `yuki 899` (Inverse Euler Transform), `CF 623E` (Transforming Sequence Scale-Shift EGF) | Symbolic $\text{MSET}/\text{PSET}/\text{CYC}$, $\ln/\exp$ component extraction, Inverse Euler Möbius recovery | `1A#L705–L795`, `Arch#1A-4..10` |
| **1A-16..26** | Advanced | **11 Problems**: `fps_24_n` (Coin 2 Bounded Knapsack), `fps_24_o` (Rooted Prime-Child Tree LIF), `Luogu P5824` (Twelvefold Way Master Synthesis), `fps_24_t` (Colorful Multipartite Walk OGF), `CF 891E` (Lust Expected Product Decrement EGF), `Luogu P4705` (玩游戏 Newton Power Sums), `LOJ #6538` (烷基计数 $S_3$ Cycle Index), `LOJ #6539` (有标号连通二分图计数), `51Nod 1728` (不动点 $x e^{x e^x}$), `UOJ #50` (链式反应 Riccati ODE), `CF 960G` (Bandit Blues Stirling S1) | Pólya Cycle Index $Z(S_3)$, Newton Power Sums $-x P'/P$, Lagrange Inversion, Riccati ODE | `1A#L796–L865`, `Arch#1A-14..25` |
| **1A-27..31** | Mastery | **5 Problems**: `CF 438E` (The Child and Binary Tree Rationalized $\sqrt{1-4D}$), `Luogu P4548` (歌唱王国 KMP PGF), `HDU 5279` (YJC plays minecraft Circular DP), `Luogu P5434` (有标号荒漠计数 Cactus EGF), `fps_24_s` (Game Tree EGF $L e^L = T$ & $L = x e^{L^2}$) | Rationalized $\sqrt{\cdot}$, Guibas–Odlyzko PGF, Cactus Block-Tree EGF + Otter's Dissymmetry | `1A#L868–L935`, `Arch#1A-10,15,26,27,30` |
```

---

## 2. Mathematical & Problem-Statement Bugs in `problem_archive.md` and `PROBLEM_CURATION.md`

Every defect below was missed by `audit_A_master_problems.md` and has been cross-verified against official contest statements, `audit_A_wave_1a.md`–`audit_A_wave_5b.md`, and Python numerical scripts.

### Bug 2.1: `AtCoder fps_24_a` (Snack / お菓子) — Hallucinated Snack Costs & Multiplicities
- **Affected Locations**:
  - `PROBLEM_CURATION.md` **L161** (`M58`) and **L319** (`1A-1`)
  - `problem_archive.md` **L17** (Table 1.1) and **L294–L300** (`Problem 1A-1`)
- **Audit Diagnosis** (cf. `audit_A_wave_1a.md` Bug M-2 & `audit_A_wave_1b.md` Defect 1.2):
  - `PROBLEM_CURATION.md` L161 and L319 write `[x^{N-D}](1 + x + x^2 + x^4)^D` / `[x^{S-N}](1 + x + x^2 + x^4)^N` (corresponding to costs $\{1,2,3,5\}$).
  - `problem_archive.md` L296–L299 fabricates *"each snack has cost in $\{1, 3, 4, 6\}$ with given color multiplicities $(1, 2, 1, 3)$ ... $P(x) = x + 2x^3 + x^4 + 3x^6$"*.
  - In the official AtCoder problem `fps_24_a` (*Snack*), there are $D$ days ($1 \le D \le 2.5\times 10^5$, $1 \le N \le 10^6$), and each day you buy **one** snack from 4 types costing $\{1, 3, 4, 6\}$ yen (each with multiplicity $1$), so $P(x) = x + x^3 + x^4 + x^6 = x(1+x^2)(1+x^3)$, and the answer is $[x^N] P(x)^D = [x^{N-D}](1+x^2)^D(1+x^3)^D$, computed in **$O(D)$ time** without NTT!
- **Exact Fixes**:
  1. In `PROBLEM_CURATION.md` **L161**, replace `$[x^{N-D}](1 + x + x^2 + x^4)^D$` with `$[x^{N-D}](1 + x^2)^D(1 + x^3)^D$`.
  2. In `problem_archive.md` **L294–L300**, replace with:
     ```markdown
     #### Problem 1A-1: AtCoder `fps_24_a` — Snack (`お菓子`)
     - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_a` | **Constraints**: $1 \le D \le 2.5 \times 10^5, 1 \le N \le 10^6$, $\bmod 998244353$.
     - **Statement**: Over $D$ days, each day you buy one snack costing $1, 3, 4,$ or $6$ yen. Count the number of ways to spend a total of **exactly** $N$ yen.
     - **Tags**: `[OGF-Seq]`, `[Polynomial-Factoring]` | **Diagnostic Signal**: Ordered sequence of $D$ independent choices summing to $N \implies [x^N] (x + x^3 + x^4 + x^6)^D$.
     - **3-Tier Hints**: (1) Write the single-day OGF $P(x) = x + x^3 + x^4 + x^6$. (2) Factor $P(x) = x(1 + x^2)(1 + x^3)$ so $P(x)^D = x^D (1 + x^2)^D (1 + x^3)^D$. (3) Expand $(1+x^2)^D$ and $(1+x^3)^D$ explicitly via the Binomial Theorem and sum $\binom{D}{j}\binom{D}{k}$ over $2j + 3k = N - D$ in $O(D)$ time!
     - **Solution Formula**: $[x^{N-D}] (1 + x^2)^D (1 + x^3)^D = \sum_{j=0}^{\lfloor (N-D)/2 \rfloor} [3 \mid (N - D - 2j)] \binom{D}{j} \binom{D}{(N - D - 2j)/3} \bmod 998244353$.
     ```

---

### Bug 2.2: `AtCoder fps_24_d` (Sequence 2 / 数列 2) — Fabricated Laplace-Bridge & Mahonian Statements
- **Affected Locations**:
  - `PROBLEM_CURATION.md` **L176**, **L324** (`1A-6`)
  - `problem_archive.md` **L20** (Table 1.1) and **L308–L313** (`Problem 1A-3`)
- **Audit Diagnosis** (cf. `audit_A_wave_1a.md` Bug M-1):
  - `problem_archive.md` L20 & L308–L313 claim `fps_24_d` is an *"EGF-to-OGF Laplace Bridge $\sum k! x^k$ ... where if value $v$ appears $c_v$ times, its weight is $c_v!$"*, while `PROBLEM_CURATION.md` L324 claims `fps_24_d` is *"Permutation (`順列`) — Mahonian Inversion OGF"*.
  - In reality, official `AtCoder fps_24_d` (*Sequence 2 / 数列 2*) asks: count non-decreasing integer sequences $0 \le A_1 \le A_2 \le \dots \le A_N \le M$ ($N, M \le 2.5 \times 10^5$) such that $A_i \not\equiv A_{i+1} \pmod 2$ for all $1 \le i \le N-1$.
  - Setting $d_0 = A_1 \ge 0$, $d_i = A_{i+1} - A_i \in \{1, 3, 5, \dots\}$ for $1 \le i \le N-1$, and $d_N = M - A_N \ge 0$, the OGF is:
    $$[x^M] \frac{1}{(1-x)^2} \left(\frac{x}{1-x^2}\right)^{N-1} = [x^{M-N+1}] \frac{1}{(1-x)^2 (1-x^2)^{N-1}}$$
- **Exact Fixes**:
  1. In `problem_archive.md` **L20**, replace with:
     ```markdown
     | **`fps_24_d`** | Sequence 2 | Alternating-Parity Difference OGF $[x^{M-N+1}]\frac{1}{(1-x)^2(1-x^2)^{N-1}}$ | Wave 1A (#3) | Stepping Stone |
     ```
  2. In `problem_archive.md` **L308–L313**, replace with:
     ```markdown
     #### Problem 1A-3: AtCoder `fps_24_d` — Sequence 2 (`数列 2`)
     - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_d` | **Constraints**: $N, M \le 2.5 \times 10^5$, $\bmod 998244353$.
     - **Statement**: Count integer sequences $0 \le A_1 \le A_2 \le \dots \le A_N \le M$ such that $A_i \not\equiv A_{i+1} \pmod 2$ for all $1 \le i \le N-1$.
     - **Tags**: `[Step-Parity-OGF]`, `[Negative-Binomial-Extraction]` | **Diagnostic Signal**: Non-decreasing sequence with odd interior differences $d_i = A_{i+1} - A_i \in \{1, 3, 5, \dots\} \implies \frac{x}{1 - x^2}$.
     - **3-Tier Hints**: (1) Encode $A_1 \ge 0$ and $M - A_N \ge 0$ by two boundary factors $\frac{1}{1-x}$. (2) Each of the $N-1$ interior steps $d_i = A_{i+1} - A_i$ is a positive odd integer with OGF $\frac{x}{1-x^2}$. (3) Extract $[x^{M-N+1}] \frac{1}{(1-x)^2 (1-x^2)^{N-1}}$ in $O(M)$ time by summing over even powers $2k$ from $(1-x^2)^{-(N-1)}$.
     - **Solution Formula**: $\sum_{k=0}^{\lfloor (M-N+1)/2 \rfloor} \binom{N - 2 + k}{k} (M - N + 2 - 2k) \bmod 998244353$.
     ```

---

### Bug 2.3: `AtCoder fps_24_f` (Colored Paper / 色紙), `fps_24_l` (Permutation 2), and `fps_24_o` (Rooted Tree) — Swapped & Corrupted Statements
- **Affected Locations**:
  - `PROBLEM_CURATION.md` **L236** (`Wave 3B #1`), **L415** (`3B-1`), **L416** (`3B-2`)
  - `problem_archive.md` **L22**, **L28**, **L31**, **L322–L327** (`Problem 1A-5`), **L442–L447** (`Problem 1A-21`), **L1215–L1218** (`Problems 3B-1 & 3B-2`)
- **Audit Diagnosis** (cf. `audit_A_wave_1a.md` Bug M-5 & `audit_A_wave_3b.md` Omission O1):
  1. **`fps_24_f` is Colored Paper (`色紙`), NOT "Colored Tree" or "Rooted Tree"**: You have $N$ sheets of colored paper; each sheet is colored Red (even count), Blue (odd count), or Green/Yellow, solved via parity EGF $\frac{e^x+e^{-x}}{2} \cdot \frac{e^x-e^{-x}}{2} \cdot e^{2x} = \frac{e^{4x} - 1}{4}$.
  2. **`fps_24_l` is Permutation 2 (`順列 2`)**: Count permutations of $\{1, \dots, N\}$ with **no 2-cycles** ($P_{P_i} \neq i$? Wait: $P_i \neq i$ is `fps_24_k`; `fps_24_l` forbids cycles of length $2$, so $E(x) = \frac{e^{-x^2/2}}{1-x}$ — note `problem_archive.md` L28 wrote $\exp(\sum_{c \notin S} x^c/c)$ while L324 wrote $c \in S$).
  3. **`fps_24_o` is Rooted Tree (`根付き木`)**: Count labeled trees on $N$ vertices **rooted at vertex 1** where every vertex has $0$ or a prime number of children. Because vertex 1 is fixed as the root, we must divide $N! [x^N] T(x) = (N-1)! [u^{N-1}] \Phi(u)^N$ by $N$! In `problem_archive.md` **L447** (`Problem 1A-21`), the formula writes $(N-1)! [u^{N-1}] \left(\sum_{d \in S} \frac{u^d}{d!}\right)^N$ — **missing the factor $\frac{1}{N}$** for fixing the root label to $1$ (or else state clearly that the root label is arbitrary among $\{1,\dots,N\}$)!
  4. In `PROBLEM_CURATION.md` **L236** and **L415–L416**, `fps_24_f` and `fps_24_o` are assigned to `3B-1` and `3B-2` where `3B-2` is actually `BZOJ 3684 / Luogu P3684 — 大朋友和多叉树`!
- **Exact Fixes**:
  1. In `PROBLEM_CURATION.md` **L236**, replace `AtCoder fps_24_f (Rooted Tree / 根付き木)` with `AtCoder fps_24_o (Rooted Tree / 根付き木)`.
  2. In `PROBLEM_CURATION.md` **L415–L416**, replace with:
     ```markdown
     | **3B-1** | Stepping Stone | **AtCoder `fps_24_o`** — Rooted Tree (`根付き木`) — Classical LIF | $T(x) = x\Phi(T(x)) \implies \frac{(N-1)!}{N}[u^{N-1}]\Phi(u)^N$ via one `pow` call | `3B#L1079`, `Arch#1A-21` |
     | **3B-2** | Stepping Stone | **Luogu P3684 / BZOJ 3684** — 大朋友和多叉树 (Ordered Plane Trees) | Leaf-counted implicit equation $T(x) = x + \sum_{d \in S} T(x)^d \implies \frac{1}{N}[u^{N-1}]\left(\frac{u}{u - \sum_{d \in S} u^d}\right)^N$ | `3B#L1129`, `Arch#3B-2` |
     ```
  3. In `problem_archive.md` **L22**, replace `Colored Tree | 2-Color Mutual EGF System & Substitution` with `Colored Paper (色紙) | Parity EGF (e^x+e^{-x})(e^x-e^{-x})e^{2x}/4`.
  4. In `problem_archive.md` **L447** (`Problem 1A-21`), update the Solution Formula to:
     ```markdown
     - **Solution Formula**: $\frac{(N-1)!}{N} [u^{N-1}] \left(\sum_{d \in S} \frac{u^d}{d!}\right)^N \bmod 998244353$ (when rooted at fixed vertex $1$; multiply by $N$ if the root label is free).
     ```
  5. In `problem_archive.md` **L1215–L1218** (`Problems 3B-1 & 3B-2`), replace with:
     ```markdown
     - **Problem 3B-1: AtCoder `fps_24_o` — Rooted Tree (`根付き木`)**: Cross-ref **Problem 1A-21** ($\frac{(N-1)!}{N}[u^{N-1}]\big(1 + \sum_{p \text{ prime}} \frac{u^p}{p!}\big)^N$).
     - **Problem 3B-2: Luogu P3684 / BZOJ 3684 — 大朋友和多叉树 (Ordered Plane Trees with Degree Set $S$)**
       - **URL**: `https://www.luogu.com.cn/problem/P3684` | **Constraints**: $N \le 10^5, |S| \le 10^5$, $\bmod 998244353$.
       - **Statement & Formula**: Count unlabeled ordered plane trees with $N$ leaves where every internal node has out-degree in $S \subseteq \{2, \dots, N\}$. The leaf OGF satisfies $T(x) - \sum_{d \in S} T(x)^d = x$, so by Lagrange Inversion $[x^N] T(x) = \frac{1}{N} [u^{N-1}] \left(1 - \sum_{d \in S} u^{d-1}\right)^{-N}$ in $O(N \log N)$ time!
     ```

---

### Bug 2.4: `AtCoder fps_24_h` (Jump / ジャンプ) — Fabricated Shift-Composition Statement
- **Affected Locations**:
  - `PROBLEM_CURATION.md` **L177**, **L182**, **L361** (`2A-3`)
  - `problem_archive.md` **L24** (Table 1.1) and **L716–L721** (`Problem 2A-1`)
- **Audit Diagnosis** (cf. `audit_A_wave_2a.md` Corrupted Problem 2.1):
  - `PROBLEM_CURATION.md` L177 calls `fps_24_h` *"Botan (`ボタン`) — EGF $\exp/\ln$"* and L361 calls it *"Grid Walk with Diagonal Steps"*, while `problem_archive.md` L716–L721 fabricates a generic Möbius shift $F(\frac{ax+b}{cx+d})$.
  - In official `AtCoder fps_24_h` (*Jump / ジャンプ*), you walk from $(0,0)$ to $(N,M)$ using jump vectors $(a,b) \in (\{0,1\} \times \mathbb{Z}_{\ge 0}) \setminus \{(0,0)\}$. The bivariate step OGF is $S(x,y) = \frac{1+x}{1-y} - 1 = \frac{x+y}{1-y}$, so:
    $$[x^N y^M] \frac{1}{1 - \frac{x+y}{1-y}} = [x^N y^M] \frac{1 - y}{1 - 2y - x} = 2^M \binom{N+M}{N} - 2^{M-1} \binom{N+M-1}{N} \pmod{998244353}$$
- **Exact Fixes**:
  1. In `PROBLEM_CURATION.md` **L177**, replace `fps_24_h (Botan / ボタン — EGF \exp/\ln)` with `fps_24_h (Jump / ジャンプ — Bivariate Rational OGF [x^N y^M]\frac{1-y}{1-2y-x})`.
  2. In `PROBLEM_CURATION.md` **L361** (`2A-3`), replace with:
     ```markdown
     | **2A-3** | Stepping Stone | **AtCoder `fps_24_h`** — Jump (`ジャンプ`) — Bivariate Rational Walk OGF | Step OGF $S(x,y) = \frac{1+x}{1-y} - 1 \implies [x^N y^M]\frac{1-y}{1-2y-x} = 2^M\binom{N+M}{N} - 2^{M-1}\binom{N+M-1}{N}$ | `2A#L1278`, `Arch#2A-1` |
     ```
  3. In `problem_archive.md` **L24** and **L716–L721**, replace `Problem 2A-1` with:
     ```markdown
     #### Problem 2A-1: AtCoder `fps_24_h` — Jump (`ジャンプ`) (`Stepping Stone`)
     - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_h` | **Constraints**: $N, M \le 2.5 \times 10^5$, $\bmod 998244353$.
     - **Statement**: Starting at $(0, 0)$, in each step you can jump by $(a, b) \in (\{0, 1\} \times \mathbb{Z}_{\ge 0}) \setminus \{(0, 0)\}$. Count the number of paths to $(N, M)$.
     - **Tags**: `[Bivariate-Rational-OGF]`, `[Geometric-Collapse]` | **Diagnostic Signal**: Step set $\{0,1\}\times\mathbb{Z}_{\ge 0}\setminus\{(0,0)\}$ has factored geometric OGF $S(x, y) = \frac{1+x}{1-y} - 1 = \frac{x+y}{1-y}$.
     - **3-Tier Hints**: (1) Sum over all path lengths $k \ge 0$: $F(x, y) = \frac{1}{1 - S(x, y)} = \frac{1 - y}{1 - 2y - x}$. (2) Extract $[x^N]$ first: $[x^N]\frac{1-y}{(1-2y)(1 - \frac{x}{1-2y})} = \frac{1-y}{(1-2y)^{N+1}}$. (3) Extract $[y^M]$ in $O(1)$ time via negative binomial coefficients!
     - **Solution Formula**: $[x^N y^M] \frac{1-y}{1-2y-x} = 2^M \binom{N+M}{N} - [M \ge 1] 2^{M-1} \binom{N+M-1}{N} \bmod 998244353$.
     ```

---

### Bug 2.5: `AtCoder fps_24_q` (Dice), `fps_24_r` (Random Walk), `fps_24_s` (Game), `fps_24_t` (Colorful), and `fps_24_v` (12 Directions)
- **Affected Locations**:
  - `PROBLEM_CURATION.md` **L182**, **L192**, **L368** (`2A-10`)
  - `problem_archive.md` **L33–L38**, **L449–L454** (`Problem 1A-22`), **L509–L514** (`Problem 1A-30`), **L789–L794** (`Problem 2A-12`), **L840–L845** (`Problem 2A-21`), **L926–L931** (`Problem 2A-35`)
- **Audit Diagnosis** (cf. `audit_A_wave_1a.md` Bugs M-3, M-4 & `audit_A_wave_2a.md` Corrupted Problems 2.4–2.6):
  1. **`fps_24_q` (Dice / サイコロ)** (`problem_archive.md` L840–L845 & `PROBLEM_CURATION.md` L368): Currently a generic placeholder about falling-factorial moments $P(1+t)^N$. In the true problem, given an $N$-sided die $A$ and an $M$-sided die $B$, we must compute $\mathbb{E}[(A+B)^k]$ for $1 \le k \le K$ via Newton's power-sum logarithmic derivative $S_A(x) = N - \frac{x Q_A'(x)}{Q_A(x)}$ where $Q_A(x) = \prod_{i=1}^N (1 - A_i x)$, followed by EGF convolution!
  2. **`fps_24_r` (Random Walk / ランダムウォーク)** (`problem_archive.md` L926–L931): The walk is on a **reflecting path** $\{1, 2, \dots, 2^N+1\}$ (where stepping from $1$ goes to $2$ and stepping from $2^N+1$ goes to $2^N$), unfolded by the method of images onto the cycle $\mathbb{Z}_{2^{N+1}}$ where $x$ and $-x \bmod 2^{N+1}$ are identified!
  3. **`fps_24_s` (Game / ゲーム)** (`problem_archive.md` L509–L514): Currently a generic placeholder about non-monic quadratics $A F^2 + B F + C = 0$. The actual problem counts $N$-vertex labeled trees on which Bob (second player) wins a vertex-moving game under `type = 1` (fixed start at vertex 1: losing tree EGF $L e^L = T(x) \implies \text{Ans} = N^{N-2} - (N-1)![x^N]L(x)$) and `type = 2` (Alice picks any start vertex: $L = x e^{L^2}$, unrooted all-losing tree EGF $L^3 - \frac{1}{2}L^4$ by Otter's Dissymmetry Theorem)!
  4. **`fps_24_t` (Colorful / カラフル)** (`problem_archive.md` L449–L454): Currently fabricates a signed cycle EGF $\exp(\sum (-1)^{c-1} a_c x^c/c)$. The actual problem counts closed walks of length $T \le 10^{18}$ starting and ending at vertex $(1, 1)$ on a complete multipartite graph with color class sizes $A_1, \dots, A_N$, solved by $[x^{T-1}] \frac{S(x)}{1 - (1 + A_1 x) S(x)}$ where $S(x) = \sum_{i=2}^N \frac{A_i x}{1 + A_i x}$ via D&C NTT + Bostan–Mori!
  5. **`fps_24_v` (12 Directions / 12 方向)** (`problem_archive.md` L789–L794): The step set is the 12 unit-and-$\sqrt{3}$ vectors in $\mathbb{Z}[\zeta_{12}]$, whose 2D step polynomial satisfies $S(x,y) + 2 = (x^{1/2}+x^{-1/2})(y^{1/2}+y^{-1/2})(x^{1/2}y^{1/2}+x^{-1/2}y^{-1/2})$, decoupled via EGF multiplication by $e^{-2z}$ (or $e^{-4z}$) and extracted in $O(N \log N)$ time!
- **Exact Fixes in `problem_archive.md`**:
  - **L449–L454 (`Problem 1A-22: AtCoder fps_24_t — Colorful`)**:
    ```markdown
    #### Problem 1A-22: AtCoder `fps_24_t` — Colorful (`カラフル`)
    - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_t` | **Constraints**: $N \le 2.5 \times 10^5, T \le 10^{18}$, $\bmod 998244353$.
    - **Statement**: A complete $N$-partite graph has color classes of sizes $A_1, \dots, A_N$. Count closed walks of length $T$ starting and ending at a fixed vertex $(1, 1)$ in color class $1$.
    - **Tags**: `[Multipartite-Walk-OGF]`, `[D&C-NTT]`, `[Bostan-Mori]` | **Diagnostic Signal**:Eigenvalue/generating-function compression of color class $i$ contributes $\frac{A_i x}{1 + A_i x}$ to the return walk OGF.
    - **3-Tier Hints**: (1) Define $S(x) = \sum_{i=2}^N \frac{A_i x}{1 + A_i x}$. (2) Separating vertex $(1,1)$ from the other $A_1 - 1$ vertices in color $1$, the OGF of walks from $(1,1)$ to $(1,1)$ is $1 + \frac{x S(x)}{1 - (1 + A_1 x) S(x)}$. (3) Clear denominators via divide-and-conquer NTT in $O(N \log^2 N)$ and extract $[x^T]$ via Bostan–Mori in $O(N \log N \log T)$ time!
    - **Solution Formula**: $[x^{T-1}] \frac{S(x)}{1 - (1 + A_1 x) S(x)}$ where $S(x) = \sum_{i=2}^N \frac{A_i x}{1 + A_i x}$.
    ```
  - **L509–L514 (`Problem 1A-30: AtCoder fps_24_s — Game`)**:
    ```markdown
    #### Problem 1A-30: AtCoder `fps_24_s` — Game (`ゲーム`)
    - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_s` | **Constraints**: $N \le 2.5 \times 10^5, \text{type} \in \{1, 2\}$, $\bmod 998244353$.
    - **Statement**: Count $N$-vertex labeled trees on which the second player (Bob) wins the simple-path token movement game when (`type = 1`) the token starts at vertex $1$, or (`type = 2`) Alice chooses the starting vertex.
    - **Tags**: `[Implicit-Tree-EGF]`, `[Otter-Dissymmetry]`, `[Newton-Iteration]` | **Diagnostic Signal**: A rooted tree is losing ($\mathcal{L}$) iff all children are winning ($\mathcal{W}$), and winning iff at least one child is losing.
    - **3-Tier Hints**: (1) For `type = 1`, $W(x) = T(x) - L(x)$ and $L(x) = x e^{W(x)} \implies L(x) e^{L(x)} = T(x) = x e^{T(x)}$, solved via Newton's method; Bob wins $(N-1)! [x^N] L(x)$ trees, or Alice wins $N^{N-2} - (N-1)! [x^N] L(x)$. (2) For `type = 2`, Bob wins iff every vertex is a losing start, which means every winning subtree has exactly $1$ losing child: $W(x) = L(x)^2 \implies L(x) = x \exp(L(x)^2)$. (3) By Otter's Dissymmetry Theorem between $\mathcal{L}$-nodes and $\mathcal{W}$-nodes, the unrooted EGF for `type = 2` is $L(x) + L(x)^2 - L(x) \cdot L(x)^2 + \dots = L(x)^3 - \frac{1}{2} L(x)^4$ (for $N \ge 2$).
    - **Solution Formula**: `type = 1`: $(N-1)! [x^N] L(x)$ where $L e^L = T(x)$; `type = 2`: $N! [x^N] \big(L(x)^3 - \frac{1}{2} L(x)^4\big)$ where $L = x e^{L^2}$.
    ```
  - **L840–L845 (`Problem 2A-21: AtCoder fps_24_q — Dice`)**:
    ```markdown
    #### Problem 2A-21: AtCoder `fps_24_q` — Dice (`サイコロ`) (`Advanced`)
    - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_q` | **Constraints**: $N, M, K \le 2.5 \times 10^5$, $\bmod 998244353$.
    - **Statement**: Given an $N$-sided die with faces $A_1, \dots, A_N$ and an $M$-sided die with faces $B_1, \dots, B_M$, compute $\mathbb{E}[(A + B)^k] \bmod 998244353$ for all $k = 1, \dots, K$.
    - **Tags**: `[Newton-Power-Sums]`, `[Log-Derivative]`, `[EGF-Convolution]` | **Diagnostic Signal**: Identical algebraic core to **Problem 1A-24** (`Luogu P4705`): $\sum_{i,j} (A_i + B_j)^k = k! [x^k] \left(\sum_{p \ge 0} \frac{S_A(p)}{p!} x^p\right)\left(\sum_{q \ge 0} \frac{S_B(q)}{q!} x^q\right)$.
    - **3-Tier Hints**: (1) Compute $Q_A(x) = \prod_{i=1}^N (1 - A_i x)$ and $Q_B(x) = \prod_{j=1}^M (1 - B_j x)$ via divide-and-conquer NTT in $O((N+M)\log^2(N+M))$ time. (2) Obtain the power sums via logarithmic derivatives: $\sum_{p=0}^K S_A(p) x^p = N - \frac{x Q_A'(x)}{Q_A(x)} \bmod x^{K+1}$. (3) Scale by $1/p!$, convolve the two EGFs via NTT, and multiply $[x^k]$ by $\frac{k!}{NM}$.
    - **Solution Formula**: $\mathbb{E}[(A+B)^k] = \frac{k!}{NM} [x^k] \left(\widehat{S}_A(x) \cdot \widehat{S}_B(x)\right) \bmod 998244353$.
    ```

---

### Bug 2.6: `Codeforces 1821F` (Timber) — Mathematically False OGF in `problem_archive.md` L1391
- **Affected Location**: `problem_archive.md` **L1389–L1391** (`Problem 4B-12: Codeforces 1821F — Timber`)
- **Audit Diagnosis** (Caught by Inspector B via Python brute-force verification; cf. `audit_A_wave_4b.md` Bug 1.6):
  - `problem_archive.md` L1391 states:
    `[x^N] \frac{1}{(1-x)^2} \left(\frac{x^K(2 + x^K)}{1 + x^K}\right)^M`
  - This formula is doubly wrong:
    1. It omits the $M - 1$ internal gap factors $\frac{1}{(1-x)^{M-1}}$ between consecutive trees (using $(1-x)^{-2}$ instead of $(1-x)^{-(M+1)}$).
    2. It uses $\frac{x^K(2+x^K)}{1+x^K}$ instead of the exact inclusion-exclusion / canonical-greedy factor $2 x^{K+1} - x^{2K+1}$! Specifically, `CF 1821F` asks for the number of **sets of $M$ tree positions** $1 \le p_1 < \dots < p_M \le N$ that admit at least one valid assignment of left/right fall directions $[p_i - K, p_i]$ or $[p_i, p_i + K]$ with no shared endpoints. Each tree occupies $K+1$ integer points if it falls in one direction ($2 x^{K+1}$), minus the intersection where **both** directions are disjoint from neighbors ($-x^{2K+1}$), separated by $M+1$ gaps $\ge 0$ ($\frac{1}{(1-x)^{M+1}}$).
  - Python verification for $M = 2, K = 2, N = 7 \dots 12$ confirms that `[x^N] \frac{(2 x^{K+1} - x^{2K+1})^M}{(1-x)^{M+1}}` produces the exact answers `12, 20, 28, 37, 47, 58`.
- **Exact Fix for `problem_archive.md` L1389–L1391**:
  ```markdown
  - **Problem 4B-12: Codeforces 1821F — Timber**
    - **URL**: `https://codeforces.com/problemset/problem/1821/F` | **Constraints**: $N, M, K \le 3 \times 10^5$, $\bmod 998244353$.
    - **Statement & Formula**: Count sets of $M$ tree positions $1 \le p_1 < \dots < p_M \le N$ such that each tree of height $K$ can fall left ($[p_i - K, p_i]$) or right ($[p_i, p_i + K]$) within $[1, N]$ with pairwise disjoint intervals (no shared endpoints). By Inclusion-Exclusion on trees that can fall in **both** directions (or canonical greedy left-first assignment), each tree contributes $2 x^{K+1} - x^{2K+1}$ and the $M + 1$ gaps contribute $(1 - x)^{-(M+1)}$:
      $$\text{Ans} = [x^N] \frac{(2 x^{K+1} - x^{2K+1})^M}{(1 - x)^{M+1}} = \sum_{j=0}^M (-1)^j \binom{M}{j} 2^{M-j} \binom{N - M K - j K}{M} \pmod{998244353}$$
      evaluated in $O(M)$ time!
  ```

---

### Bug 2.7: `AtCoder ABC 300 Ex` (Fibonacci: Revisited) & `AtCoder ABC 279 Ex` (Sum of Prod of Min) — Omitted/Corrupted Problem Statements
- **Affected Locations**:
  - `PROBLEM_CURATION.md` **L440** (`4A-1`)
  - `problem_archive.md` **L63**, **L68**, **L737–L742** (`Problem 2A-4`), **L1305–L1307** (`Problem 4A-P10`)
- **Audit Diagnosis** (cf. `audit_A_wave_4a.md` Findings F-04 & F-05):
  1. **`ABC 300 Ex` (`problem_archive.md` L737–L742 & `PROBLEM_CURATION.md` L440)**: States only "compute $a_N \bmod 998244353$". The actual `ABC 300 Ex` problem asks for the **bitwise submask sum** $\sum_{m \text{ AND } N = m} a_m \bmod 998244353$ (for $N \le 10^{18}, K \le 2.5 \times 10^5$), solved by modifying Bostan–Mori so that when the lowest bit of $N$ is $1$, we keep the sum of the even AND odd parts $\mathcal{E}(U) + \mathcal{O}(U)$ (corresponding to $m$ having bit $0$ or $1$), and when the lowest bit of $N$ is $0$, we keep only the even part $\mathcal{E}(U)$!
  2. **`ABC 279 Ex` (`problem_archive.md` L1305–L1307)**: States constraints $N \le 10^6, M \le 10^{12}$ and $\prod_{i=1}^N \min(A_i, B_i)$. The actual problem has $1 \le N \le 10^{12}, N \le M \le 2N \pmod{200003}$ and asks for $\sum_{S_1 + \dots + S_N = M, S_k \ge 1} \prod_{k=1}^N \min(k, S_k) = [x^{M-N}] \frac{1}{(1-x)^{2N+1}} \prod_{k=1}^N (1 - x^k)$!
- **Exact Fixes**:
  1. In `PROBLEM_CURATION.md` **L440** (`4A-1`), replace with:
     ```markdown
     | **4A-1** | Stepping Stone | **AtCoder ABC 300 Ex** — Fibonacci: Revisited | Bitwise-submask Bostan–Mori ($\mathcal{E} + \mathcal{O}$ when $N \bmod 2 = 1$) on $\frac{1-x}{1-2x+x^{K+1}}$ | `4A#L755`, `Arch#2A-4` |
     ```
  2. In `problem_archive.md` **L737–L742** (`Problem 2A-4`), replace with:
     ```markdown
     #### Problem 2A-4: AtCoder ABC 300 Ex — Fibonacci: Revisited (`Advanced`)
     - **URL**: `https://atcoder.jp/contests/abc300/tasks/abc300_h` | **Constraints**: $K \le 2.5 \times 10^5, N \le 10^{18}$, $\bmod 998244353$.
     - **Statement**: Let $a_0 = 0, a_1 = \dots = a_K = 1$, and $a_n = \sum_{i=1}^K a_{n-i}$ for $n > K$. Compute the bitwise submask sum $\sum_{m \text{ AND } N = m} a_m \bmod 998244353$ (as well as the single-term $a_N$).
     - **Tags**: `[Bitwise-Submask-Bostan-Mori]`, `[3-Sparse-Denominator]` | **Diagnostic Signal**: $Q(x) = 1 - x - \dots - x^K = \frac{1 - 2x + x^{K+1}}{1 - x}$; summing over submasks $m \subseteq N$ means at bit $0$ of $N$: if $N_0 = 0$, extract even indices $\mathcal{E}$; if $N_0 = 1$, sum BOTH even and odd indices $\mathcal{E} + \mathcal{O}$!
     - **3-Tier Hints**: (1) Express $A(x) = \frac{P(x)}{Q(x)}$ with $Q(x) = 1 - x - \dots - x^K$. (2) At each Bostan–Mori step, compute $U(x) = P(x) Q(-x) = U_{\text{even}}(x^2) + x U_{\text{odd}}(x^2)$ and $V(x^2) = Q(x) Q(-x)$. (3) Update $P_{\text{next}}(x) = U_{\text{even}}(x) + [N \bmod 2 = 1] U_{\text{odd}}(x)$ and $N \gets \lfloor N / 2 \rfloor$ in $O(K \log K \log N)$ time!
     - **Solution Formula**: Submask Bostan–Mori recursion $P \gets \mathcal{E}(P(x)Q(-x)) + (N \bmod 2)\mathcal{O}(P(x)Q(-x))$ in $O(K \log K \log N)$ time.
     ```
  3. In `problem_archive.md` **L1305–L1307** (`Problem 4A-P10`), replace with:
     ```markdown
     - **Problem 4A-P10: AtCoder ABC 279 Ex — Sum of Prod of Min**
       - **URL**: `https://atcoder.jp/contests/abc279/tasks/abc279_h` | **Constraints**: $1 \le N \le 10^{12}, N \le M \le 2N$, $\bmod 200003$.
       - **Statement & Formula**: Sum $\prod_{k=1}^N \min(k, S_k)$ over all positive integer sequences $(S_1, \dots, S_N)$ with $\sum_{k=1}^N S_k = M$. Since $\sum_{s \ge 1} \min(k, s) x^s = \frac{x(1 - x^k)}{(1 - x)^2}$, the answer is $[x^{M-N}] \frac{1}{(1-x)^{2N}} \prod_{k=1}^N (1 - x^k) = [x^{M-N}] \frac{1}{(1-x)^{2N}} \prod_{k \ge 1} (1 - x^k)$ (since $M - N \le N$). Expand $\prod_{k \ge 1}(1 - x^k)$ via Euler's Pentagonal Number Theorem in $O(\sqrt{M-N})$ terms and evaluate $\binom{2N + r - 1}{r} \bmod 200003$ via Lucas's Theorem in $O(\sqrt{M-N} + P)$ time!
     ```

---

### Bug 2.8: Seven Additional Formula / Title Corrections in `problem_archive.md` and `PROBLEM_CURATION.md`
1. **`Codeforces 1251F` (`problem_archive.md` L137)**:
   - Fix LaTeX exponent typo `$(1+2x)^{c_1}(1+x)^2{c_2}$` $\to$ `$(1+2x)^{c_1}(1+x)^{2c_2}$`.
2. **`Codeforces 1528F — AmShZ Farm` (`problem_archive.md` L1148)**:
   - Remove the erroneous prefactor $\frac{N}{N+1}$ (cf. `audit_A_wave_3a.md` Bug 1.2):
     - **Current**: `Thus \text{Ans} = \frac{N}{N + 1} \sum_{j=1}^{\min(N, K)} \left\{\begin{matrix} K \\ j \end{matrix}\right\} N^{\underline{j}} (N + 1)^{N - j}.`
     - **Fixed**: `Thus \text{Ans} = \sum_{j=1}^{\min(N, K)} \left\{\begin{matrix} K \\ j \end{matrix}\right\} N^{\underline{j}} (N + 1)^{N - j} \bmod 998244353.`
3. **`Luogu P5206 — [WC2019] 数树` (`problem_archive.md` L1014)**:
   - Fix the $\text{op} = 2$ exponent (cf. `audit_A_wave_2b.md` Issue 1.1):
     - **Current**: `so the EGF is \exp\left(\sum_{s \ge 1} \frac{N(y^{-1}-1) s^s}{s!} x^s\right)!`
     - **Fixed**: `so the EGF is \frac{(1-y)^N}{N^4} N! [x^N] \exp\left(\sum_{s \ge 1} \frac{N^2 y}{1 - y} \frac{s^s}{s!} x^s\right) (for y \neq 1)!`
4. **`Codeforces 755G — PolandBall and Many Other Balls` (`PROBLEM_CURATION.md` L448 & `problem_archive.md` L1475)**:
   - In `PROBLEM_CURATION.md` **L448** (`4A-9`), replace the false 3-term recurrence `3-term ODE recurrence in K in O(K) time` with `4-term holonomic recurrence a_m f_{n,m} = (2n(n+2)-5a_m)f_{n,m-1} + (5a_{m-2}-2n(n+2))f_{n,m-2} + a_{m-2}f_{n,m-3} (a_r = r(n-r+1)) in O(K) time` (cf. `audit_A_wave_4a.md` Finding F-01 & `audit_A_wave_5a.md` Bug 5).
   - In `problem_archive.md` **L1475**, replace the hand-waved `\dots \implies (k+1)c_{k+1} = ...` with the exact 4-term recurrence $m(N+1-m) f_{N,m} = \big(2N(N+2) - 5m(N+1-m)\big) f_{N,m-1} + \big(5(m-2)(N+3-m) - 2N(N+2)\big) f_{N,m-2} + (m-2)(N+3-m) f_{N,m-3}$.
5. **`AtCoder AGC 058 D — Yet Another ABC String` (`PROBLEM_CURATION.md` L446)**:
   - Fix the numerator typo `(1-xyz)^2` (cf. `audit_A_wave_4b.md` Bug 1.7):
     - **Current (`L446`)**: `Bivariate/trivariate diagonal of \frac{(1-xyz)^2}{1-(x+y+z)+2xyz}`
     - **Fixed (`L446`)**: `Trivariate rational coefficient [x^A y^B z^C] \frac{1-xyz}{1-(x+y+z)+2xyz}`
6. **`Luogu P7364` vs. `Luogu P6596` (`PROBLEM_CURATION.md` L142, L221, L223 & `problem_archive.md` L225, L1183)**:
   - `Luogu P7364` is titled **有标号二分图计数** (Labeled Bipartite Graphs), NOT Eulerian Graphs (`audit_A_wave_3a.md` Issue 2.1).
   - `Luogu P6596` is **How Many of Them** (Connected Labeled Graphs with $\le m$ Bridges), NOT Bipartite Graphs (`PROBLEM_CURATION.md` L223).
   - In `PROBLEM_CURATION.md` **L142**, change `Luogu P7364 (Eulerian Graphs)` to `Labeled Eulerian Graphs (\ln \sum 2^{\binom{n-1}{2}} \frac{x^n}{n!})`.
   - In `PROBLEM_CURATION.md` **L221**, change `Luogu P7364 (有标号欧拉图计数)` to `Labeled Eulerian Graphs (有标号欧拉图计数)`.
   - In `PROBLEM_CURATION.md` **L223**, change `Luogu P6596 / P7364 (有标号二分图计数)` to `Luogu P7364 (有标号二分图计数)` and list `Luogu P6596 (How Many of Them — Connected Graphs with \le m Bridges)` properly at `#23`.
7. **`LOJ #6539` (`PROBLEM_CURATION.md` L217 & `problem_archive.md` L258)**:
   - In `PROBLEM_CURATION.md` **L217**, change `LOJ #6539 (仙人掌计数)` to `LOJ #6539 (有标号连通二分图计数)` (cactus enumeration is `LOJ #6569`; cf. `audit_A_wave_1a.md` Bug M-8).

---

## 3. Cross-Reference Pointer Bugs & Restored Wave Problems

### 3.1 Broken Cross-Reference Pointers in `problem_archive.md` Section 1
1. **`problem_archive.md` L183 (`Luogu P4389 — 付公主的背包`)**:
   - Lists `Wave 1B (#25)`. In Section 3 (`L691`), `Problem 1B-25` is `Luogu P3784 — [SDOI2017] 遗忘的集合` (Inverse Euler Transform), NOT `Luogu P4389`! Remove `Wave 1B (#25)` from `L183`.
2. **`problem_archive.md` L218 (`Luogu P6295 — 有标号 DAG 计数`)**:
   - Lists `Wave 3A (#34)`. In Section 6 (`L1188`), `Luogu P6295` is **Problem 3A-33** (`Wave 3A (#33)`). Change `Wave 3A (#34)` to `Wave 3A (#33)`.
3. **`problem_archive.md` L219 (`Luogu P6596 — How Many of Them`)**:
   - Lists `Wave 3A (#35)`. In Section 6 (`L1191`), `Luogu P6596` is **Problem 3A-34** (`Wave 3A (#34)`), while `#35` is `Codeforces 917D — Stranger Trees`. Change `Wave 3A (#35)` to `Wave 3A (#34)`.
4. **`problem_archive.md` L1143 (`Problem 3A-15: AtCoder fps_24_o — Rooted Tree`)**:
   - Ensure cross-reference to `Problem 1A-21` includes the root-$1$ factor $\frac{1}{N}$ (Fixed in Bug 2.3 above).
5. **`problem_archive.md` L1313 (`Problem 4A-P13`), L1150 (`Problem 3A-19`), L1252 (`Problem 3B-16`)**:
   - Note that in `cohort3_wave_3b_implicit_zh_ja_audit.md` (`3B-16`) and `cohort3_wave_4a_multivariate_bostan_mori_diag.md` (`4A-9`), `UOJ 424` is solved via Lagrange Inversion / Reflection Principle $[u^N] \frac{(1-u)(1-u^{M+1})}{1-u^{M+2}} (1+u)^{2N}$ (remediated from the broken negative-output formula in `audit_A_wave_3b.md` Bug M6). Add this explicit $O(N \log N)$ reflection formula to **Problem 5A-27B** (`problem_archive.md` **L1529**):
     ```markdown
     - **UOJ 424**: Left-depth $\le m$ binary trees have OGF $\frac{Q_m(x)}{Q_{m+1}(x)}$ where $Q_k(x) = \sum_{j=0}^{\lfloor k/2 \rfloor} (-1)^j \binom{k - j}{j} x^j$, or by the Two-Wall Reflection Principle under $x = \frac{u}{(1+u)^2}$, $[x^n] F_m(x) = [u^n] \frac{(1 - u)(1 - u^{m+1})}{1 - u^{m+2}} (1 + u)^{2n}$, solved in $O(n \log n)$ time!
     ```

### 3.2 Unbundling Multi-Problem Slots in `problem_archive.md` Section 11 (Wave 5B)
As flagged in `audit_A_wave_5b.md` (Section 1.1) and confirmed in `problem_archive.md` **L1553–L1650**, Wave 5B's archive entries currently bundle two or more distinct problems into single bullets (`5B-A2`, `5B-A5`, `5B-A6`, `5B-A7`, `5B-B2`, `5B-B3`, `5B-B4`, `5B-B5`, `5B-B6`, `5B-B7`, `5B-C2`, `5B-C3`, `5B-C5`, `5B-C6`, `5B-C8`, `5B-D1`, `5B-D4`, `5B-E4`, `5B-E5`, `5B-E6`, `5B-F7`). When `cohort3_wave_5b_tree_fps_transposition_compose_q.md` is unbundled per `audit_A_wave_5b.md`, each unbundled problem in `problem_archive.md` Section 11 should be given its own sub-bullet (`5B-A5a` / `5B-A5b`, etc.) with its own URL, constraints, and solution formula (specifically adding the explicit solution summaries for `CF 1906J`, `Luogu P5298`, `CF 2006E`, `ABC 355 G`, `CF 1510H`, `CF 1616H`, `Luogu P5853`, `UOJ 604`, `Luogu P7116`, `ABC 238 Ex`, `CF 1916F` provided in `audit_A_wave_5b.md` Section 1.1 and `audit_A_master_problems.md` Issue 3.2).

---

## 4. Verification Summary Checklist

| Audit Criterion | `PROBLEM_CURATION.md` Status | `problem_archive.md` Status | Remediation Action |
| :--- | :--- | :--- | :--- |
| **Zero Banned Math Delimiters (`\(...\)`, `\[...\]`)** | PASS (`0` occurrences) | PASS (`0` occurrences) | None required |
| **Zero Conversational Filler (`Wait, ...`)** | PASS (`0` occurrences) | PASS (`0` occurrences) | None required |
| **Markdown Table Pipe Escaping (`\lvert ... \rvert`)** | **11 lines to fix** (`9` in Audit A + **2 new** at `L571, L626`) | **3 lines to fix** (`L139, L181, L264`) | Apply Audit A Issue 5 + Audit B §1.1 |
| **Wave-to-Curation Ladder Alignment** | Fix Ladders 2.1, 2.3, 2.4, 2.5, 2.6, 2.8, 2.9, 2.10 | Fix broken pointers at `L183, L218, L219` | Apply Audit A §2 (with Audit B §1.2 override for Ladder 2.1) + Audit B §3.1 |
| **Mathematical & Official Statement Exactness** | Fix `fps_24_a`, `fps_24_d`, `fps_24_f/o`, `fps_24_h`, `fps_24_q`, `ABC 300 Ex`, `AGC 058 D`, `CF 755G`, `LOJ 6539`, `Luogu P7364/P6596` | Fix 21 problem statements/formulas (`CF 1821F`, `fps_24_a/d/f/h/o/q/r/s/t/v`, `ABC 300 Ex`, `ABC 279 Ex`, `CF 1251F`, `CF 1528F`, `Luogu P5206`, `CF 755G`, `UOJ 424`) | Apply Audit B §2.1–2.8 in full |
