# Part I Audit Report — Critic B: Problem Ladders, Self-Containment, Quarantined Templates & Blind Checkpoint (`CP-I`)

- **Auditor**: Part I Critic B (FPS Textbook Critic & Mathematical Auditor)
- **Scope**:
  1. `chapters/ch01-ring-convolutions-newton-inv.qmd` (§1.5 Problem Ladder `SS-1`–`Mas-2`, §1.6 Quarantined Templates)
  2. `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd` (§2.6 Problem Ladder `SS-1`–`Mas-2`, §2.7 Quarantined Templates)
  3. `chapters/ch03-mset-partitions-euler-polya.qmd` (§3.6 Problem Ladder `SS-1`–`Mas-2`, §3.7 Quarantined Templates)
  4. `chapters/ch04-egf-set-cyc-boxed-prufer.qmd` (§4.5 Problem Ladder `SS-1`–`Mas-2`, §4.6 Quarantined Templates)
  5. `checkpoints/cp01-part1-foundations.qmd` (Full file: Stage 1 Spoiler-Free Protocol, Stage 2 Routing Key, `CP-I.1`–`CP-I.8`, Revisited Threads, Quarantined Templates)
- **Reference Standards**: `AGENTS.md`, `fps_research/CURRICULUM_ARCHITECTURE.md`, `fps_research/PROBLEM_CURATION.md`, `fps_research/TECHNIQUE_TAXONOMY.md`, `fps_research/problem_archive.md`, `fps_research/cohort3_wave_1a_modelling_foundations.md`.

---

## Executive Summary & Verdict

| File | Bijective Slot Match (`8/8`) | Self-Containment & 3 Hints (`8/8`) | Derivation & Code Rigor | Prerequisite Closure | Quarantined / Revisited Coverage | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `ch01-ring-convolutions-newton-inv.qmd` | 8 / 8 PASS | 8 / 8 PASS | PASS | PASS | 8 / 8 `R-*` PASS | **PASS** (1 minor polish item) |
| `ch02-calculus-frobenius-sparse-ode-newton.qmd` | 8 / 8 PASS | 8 / 8 PASS | 1 Minor Code Helper Missing | 2 Minor Forward-Ref Notes Needed | `R-*` Grouped Bullet Polish + Revisited #1 PASS | **CONDITIONAL PASS** |
| `ch03-mset-partitions-euler-polya.qmd` | 8 / 8 PASS | 8 / 8 PASS | PASS | PASS | `R-25` PASS + Revisited #2 PASS | **PASS** (Exemplary) |
| `ch04-egf-set-cyc-boxed-prufer.qmd` | 8 / 8 IDs Match (3 Hedged Dual-Statements) | 8 / 8 PASS | 1 Minor Code Helper Missing | 1 Binomial Inv Note Needed | `R-24, R-37` PASS + Revisited #3 PASS | **NEEDS TARGETED REVISION** |
| `cp01-part1-foundations.qmd` | 8 / 8 PASS | 6 / 8 PASS (`CP-I.3`, `CP-I.5` flawed statements) | `CP-I.5` has `\dots` & "Wait:" drafts | `Ch 24` SPS Forward-Ref in `CP-I.8` & §1 | 3 Stage-1 Spoiler Leaks in Hints | **FAIL — REQUIRES REVISION** |

### Summary of Critical & Major Action Items
1. **[CRITICAL — `cp01` lines 536–605 (`CP-I.5 #079 JSC 2019 Qual F`)]**: The visible problem statement contains an **unfinished equation ending in `\dots`** (line 543) followed by meta-commentary (*"Wait — let us state the exact mathematical condition..."*, lines 545–548), and the derivation contains unedited stream-of-consciousness self-corrections (*"Wait: when is a sorted sequence bad? ... Wait: if $c_1=5$..."*, lines 593–605).
2. **[MAJOR — `cp01` lines 317–336 (`CP-I.3 #246 HDU 5279`)]**: The visible problem statement hedges between two variants (*"either: 1. Inside every island... or (in the circular block-partition formulation of HDU 5279)... Let us state both exact sub-problems"*). Replace with a single clean, authoritative statement.
3. **[MAJOR — `cp01` Stage 1 Spoiler-Free Protocol Violations (lines 241, 691, 889)]:**
   - `CP-I.2` Hint 1 (line 241) explicitly reveals the Stage 2 Routing Key technique name (**"Standard Convolution + Reverse-Indexing Difference Convolution (Cross-Correlation)"**).
   - `CP-I.6` Hint 1 (line 691) explicitly reveals the operator name and generating function (**"0-1 Subset-Sum ($\operatorname{PSET}$) Construction with Ordinary Generating Function $P(x) = \prod_{k \ge 2}(1 + x^{F_k})$"**).
   - `CP-I.8` Hint 1 (line 889) has a typo (`ofInclusion-Exclusion`) and prematurely names the exponential formula before Hint 2.
4. **[MAJOR — `ch04` Hedged "Part A / Part B" Problem Statements in `SS-2 (#007)`, `Int-2 (#008)`, and `Adv-1 (#083)`]**:
   - In `ch04` lines 477–541 (`SS-2 #007 fps_24_m`), the author writes **Part A (Labeled Connected Simple Graphs)** and **Part B (Cycle-Weight Sum over Permutations)**. Part A duplicates `Int-1 (#161 Luogu P4841)` immediately below it! Per `CURRICULUM_ARCHITECTURE.md`, `SS-2 (#007)` is **Value of Permutation (`1A#20`): Cycle Decomposition EGF $\ln\frac{1}{1-x}$ & Pointer Tracking**.
   - In `ch04` lines 617–681 (`Int-2 #008 fps_24_n`), the author writes **Part A (Prüfer Sequence Tree Degree EGF)** and **Part B (Indecomposable Permutations `fps_24_k`)**. `fps_24_k` is reserved for **`Syn-01 (#006)`** in Chapter 25 — including it in `Ch 04 Int-2` violates the 259-problem bijection!
   - In `ch04` lines 685–757 (`Adv-1 #083 CF 407E / Gym — k-Cycle`), clean up the "Variant A / Variant B" meta-framing into a single unified problem statement.
5. **[MODERATE — Prerequisite / Forward-Reference Closure (`cp01` lines 63, 89, 940–945; `ch02` lines 963–993, 1173–1182; `ch04` lines 945–957)]**:
   - `cp01` line 63 cites *"Set Power Series (`Ch 04`)"* (Set Power Series is `Ch 24`, not `Ch 04`!), and `CP-I.8` (lines 89, 940–945) invokes Set Power Series ring $\mathbb{Q}[z_1,\dots,z_N]/(z_i^2)$ (`Ch 24.2`). Frame the primary `CP-I.8` solution via `Ch 04.3` Minimum-Label Boxed Product DP $F_S = \sum_{T \ni \min(S)} W_T F_{S \setminus T}$, keeping `Ch 24.2` SPS as a forward-looking remark.
   - `ch02` `Adv-1 (#157 Luogu P4705)` (line 977) and `ch04` `Adv-2 (#011 fps_24_q)` (line 814) call `build_prod(0, n - 1)` / `daq_prod(0, N - 1)` without defining the 6-line binary product tree helper in the snippet or noting that general D&C Product Trees are studied systematically in `Ch 09.1`.

---

## 1. Bijective Slot Audit (`32/32` Chapter Ladder Problems + `8/8` `CP-I` Problems)

We cross-checked every problem slot in `ch01`–`ch04` and `cp01` against `CURRICULUM_ARCHITECTURE.md` (§3 Part I & `CP-I`) and `PROBLEM_CURATION.md` (§2 Part I & §6.1 Bijective Lookup Table).

### 1.1 Chapter 01 Ladder (`chapters/ch01-ring-convolutions-newton-inv.qmd`, lines 453–1157)
| Slot | Expected (`CURRICULUM_ARCHITECTURE.md`) | Actual in `ch01` (Lines) | Statement | Constraints | 3 Hints | Full Solution & Code | Verdict |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `SS-1` | `#019` ABC 178 D — Redistribution (`1A#1`) | `#019` ABC 178 D — Redistribution (459–547) | Yes | $S \le 2000$, $10^9+7$ | 3/3 | Yes (DP + FPS inv) | **PASS** |
| `SS-2` | `#043` ABC 321 F — #(subset sum = K) (`1A#2`) | `#043` ABC 321 F — #(subset sum = K) (551–629) | Yes | $Q, K \le 5000$, $998244353$ | 3/3 | Yes (reversible $1+x^v$ DP) | **PASS** |
| `Int-1` | `#004` `fps_24_g` — Coin (`1A#10`) | `#004` `fps_24_g` — Coin (633–709) | Yes | $N, M \le 5000$, $998244353$ | 3/3 | Yes (sliding window $(1-x^c)$) | **PASS** |
| `Int-2` | `#077` EDPC M — Candies (`1A#12`) | `#077` EDPC M — Candies (713–778) | Yes | $N \le 100, K \le 10^5$, $10^9+7$ | 3/3 | Yes (prefix-sum $(1-x^{a_i+1})/(1-x)$) | **PASS** |
| `Adv-1` | `#049` ARC 028 D — 注文の多い高橋商店 (`1A#13`) | `#049` ARC 028 D — 注文の多い高橋商店 (782–855) | Yes | $N, M \le 2000, Q \le 5\cdot 10^5$ | 3/3 | Yes (commutative factor Rollback) | **PASS** |
| `Adv-2` | `#097` CF 993E — Nikita and Order Statistics (`1B#15`) | `#097` CF 993E — Nikita and Order Statistics (859–931) | Yes | $N \le 2\cdot 10^5$, exact $\mathbb{Z}$ | 3/3 | Yes (reverse-index correlation) | **PASS** |
| `Mas-1` | `#066` AGC 001 E — BBQ Hard (`1B#2`) | `#066` AGC 001 E — BBQ Hard (935–1031) | Yes | $N \le 2\cdot 10^5, A_i,B_i \le 2000$ | 3/3 | Yes (2D offset grid translation) | **PASS** |
| `Mas-2` | `#107` CF 1251F — Red-White Fence (`1B#6`) | `#107` CF 1251F — Red-White Fence (1035–1139) | Yes | $n, q \le 3\cdot 10^5, k \le 5$ | 3/3 | Yes ($(1+2x)^{c_1}(1+x)^2)^{c_2}$ NTT) | **PASS** |

### 1.2 Chapter 02 Ladder (`chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd`, lines 657–1242)
| Slot | Expected (`CURRICULUM_ARCHITECTURE.md`) | Actual in `ch02` (Lines) | Statement | Constraints | 3 Hints | Full Solution & Code | Verdict |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `SS-1` | `#238` yukicoder 1145 — Sum of Powers (`1A#5`) | `#238` yukicoder 1145 — Sum of Powers (663–723) | Yes | $N, M \le 2\cdot 10^5$, $998244353$ | 3/3 | Yes ($-\vartheta \ln \prod(1-a_i x)$) | **PASS** |
| `SS-2` | `#165` Luogu P4389 / Subset Sum via ln/exp (`1A#11`) | `#165` Luogu P4389 (0-1 Subset Sum Variant) (727–789) | Yes | $N, M \le 10^5$, $998244353$ | 3/3 | Yes (harmonic sieve + $\exp$) | **PASS** |
| `Int-1` | `#101` CF 1096G — Lucky Tickets (`1A#18`) | `#101` CF 1096G — Lucky Tickets (793–861) | Yes | $n \le 2\cdot 10^5$, $998244353$ | 3/3 | Yes (sparse ODE $O(kN)$ vs NTT) | **PASS** |
| `Int-2` | `#222` LOJ 6261 — 一个人的高三 (`1A#19`) | `#222` LOJ 6261 — 一个人的高三 (865–929) | Yes | $n \le 10^5, k \le 10^9$ | 3/3 | Yes ($(1-x)^{-k} * A(x)$) | **PASS** |
| `Adv-1` | `#157` Luogu P4705 — 玩游戏 (`1A#6`) | `#157` Luogu P4705 — 玩游戏 (933–999) | Yes | $n, m, t \le 10^5$, $998244353$ | 3/3 | Missing `build_prod` helper in code | **MINOR FIX** |
| `Adv-2` | `#084` CF 438E — The Child and Binary Tree (`1A#22`) | `#084` CF 438E — The Child and Binary Tree (1003–1065) | Yes | $n, m \le 10^5$, $998244353$ | 3/3 | Yes + Revisited Note (`Ch 02->09->10`) | **PASS** |
| `Mas-1` | `#030` ABC 267 Ex — Odd Sum (`1B#11`) | `#030` ABC 267 Ex — Odd Sum (1069–1142) | Yes | $N \le 10^5, M \le 10^6, A_i \le 10$ | 3/3 | Yes (parity filter + $\ln/\exp$) | **PASS** |
| `Mas-2` | `#091` CF 891E — Lust (`1A#7`) | `#091` CF 891E — Lust (1146–1224) | Yes | $n \le 5000, k \le 10^9$, $10^9+7$ | 3/3 | Yes ($O(n^2)$ Vieta + EGF operator) | **PASS** |

### 1.3 Chapter 03 Ladder (`chapters/ch03-mset-partitions-euler-polya.qmd`, lines 885–1508)
| Slot | Expected (`CURRICULUM_ARCHITECTURE.md`) | Actual in `ch03` (Lines) | Statement | Constraints | 3 Hints | Full Solution & Code | Verdict |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `SS-1` | `#001` `fps_24_a` — Snack (`1A#14`) | `#001` `fps_24_a` — Snack (891–973) | Yes | $N, M \le 2.5\cdot 10^5$, $998244353$ | 3/3 | Yes (Pentagonal $\prod(1-x^k)^{-1}$ + Newton) | **PASS** |
| `SS-2` | `#188` Luogu P6189 — 跑步 (`1A#15`) | `#188` Luogu P6189 — [NOI Online #1] 跑步 (977–1052) | Yes | $n \le 10^5$, arbitrary $p$ | 3/3 | Yes (Pentagonal $O(n\sqrt{n})$ char-$p$ safe) | **PASS** |
| `Int-1` | `#153` Luogu P4389 — 付公主的背包 (`1A#3`) | `#153` Luogu P4389 — 付公主的背包 (1056–1115) | Yes | $n, m \le 10^5$, $998244353$ | 3/3 | Yes + Revisited Note (`Ch 03->02->09`) | **PASS** |
| `Int-2` | `#009` `fps_24_n` — Coin 2 (`1A#16`) | `#009` `fps_24_n` — Coin 2 (1119–1186) | Yes | $N, M \le 2.5\cdot 10^5$, $998244353$ | 3/3 | Yes (Bounded $\operatorname{MSET}$ log sieve) | **PASS** |
| `Adv-1` | `#223` LOJ 6268 — 分拆数 / 逆オイラー変換 (`1A#17`) | `#223` LOJ 6268 / yukicoder 899 (1190–1249) | Yes | $N \le 10^5$, $998244353$ | 3/3 | Yes ($\ln$ + divisor Möbius inversion) | **PASS** |
| `Adv-2` | `#221` LOJ 6089 — 小 Y 的背包计数问题 (`1A#23`) | `#221` LOJ 6089 — 小 Y 的背包计数问题 (1253–1325) | Yes | $n \le 10^5$, $23333333$ (non-NTT!) | 3/3 | Yes ($B=\sqrt{n}$ split + Durfee DP) | **PASS** |
| `Mas-1` | `#150` Luogu P3784 — 遗忘的集合 (`1A#24`) | `#150` Luogu P3784 — [SDOI2017] 遗忘的集合 (1329–1400) | Yes | $n \le 2\cdot 10^5$, arbitrary $p$ | 3/3 | Yes (MTT `ln` or $O(n\ln n)$ $\vartheta\ln$ + $\mu$) | **PASS** |
| `Mas-2` | `#159` Luogu P4727 — 图的同构记数 (`5B#4`) | `#159` Luogu P4727 — [HNOI2009] 图的同构记数 (1404–1499) | Yes | $n \le 60$, $997$ | 3/3 | Yes (Burnside on $S_n^{(2)}$ + $\gcd$ cycle count) | **PASS** |

### 1.4 Chapter 04 Ladder (`chapters/ch04-egf-set-cyc-boxed-prufer.qmd`, lines 401–1027)
| Slot | Expected (`CURRICULUM_ARCHITECTURE.md`) | Actual in `ch04` (Lines) | Statement | Constraints | 3 Hints | Full Solution & Code | Verdict |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `SS-1` | `#002` `fps_24_e` — Sequence 2 / 3 (`1A#8`) | `#002` `fps_24_e` — Sequence 2 / 3 (407–473) | Yes | $N, M \le 2.5\cdot 10^5$ | 3/3 | Yes (EGF $\prod_{m=1}^M E_m(x)$ via $\ln/\exp$) | **PASS** |
| `SS-2` | `#007` `fps_24_m` — Value of Permutation (`1A#20`) | `#007` `fps_24_m` — Part A (Graphs) + Part B (Permutations) (477–541) | **Hedged Dual Statement** | $N \le 2.5\cdot 10^5$ | 3/3 | Part A duplicates `Int-1 (#161)`! | **NEEDS FIX** |
| `Int-1` | `#161` Luogu P4841 — 城市规划 (`1A#9a`) | `#161` Luogu P4841 — 城市规划 (545–613) | Yes | $n \le 1.3\cdot 10^5$, $1004535809$ | 3/3 | Yes + Revisited Note (`Ch 04->07/13->09`) | **PASS** |
| `Int-2` | `#008` `fps_24_n` — Tree (`3A#2`) | `#008` `fps_24_n` — Part A (Prüfer) + Part B (`fps_24_k` Permutations) (617–681) | **Hedged Dual Statement** | $N \le 2.5\cdot 10^5$ | 3/3 | Part B (`fps_24_k`) steals `Syn-01 (#006)`! | **NEEDS FIX** |
| `Adv-1` | `#083` CF 407E / Gym — k-Cycle (`1A#21`) | `#083` CF 407E / Gym & `fps_24_l` (685–757) | **Hedged Variant A/B** | $n \le 2.5\cdot 10^5$ | 3/3 | Yes ($\exp(\sum_{s\in S} x^s/s)$) | **MINOR FIX** |
| `Adv-2` | `#011` `fps_24_q` — Dice (`1B#13`) | `#011` `fps_24_q` — Dice (761–839) | Yes | $N, K, M \le 10^5$ | 3/3 | Missing `daq_prod` helper in snippet | **MINOR FIX** |
| `Mas-1` | `#041` ABC 303 Ex — Constrained Tree Degree (`3A#3`) | `#041` ABC 303 Ex — Constrained Tree Degree (843–907) | Yes | $N \le 2.5\cdot 10^5$ | 3/3 | Yes (Prüfer $[x^{N-2}]P(x)^N$) | **PASS** |
| `Mas-2` | `#174` Luogu P5401 — 珍珠 (`1B#9`) | `#174` Luogu P5401 — [CTS2019] 珍珠 (911–990) | Yes | $D \le 10^5, n, m \le 10^9$ | 3/3 | Yes (Parity EGF + $(x-1)$-basis shift) | **PASS** (Add `Ch 08` note) |

### 1.5 Blind Checkpoint `CP-I` (`checkpoints/cp01-part1-foundations.qmd`, lines 1–1037)
| Slot | Expected (`CURRICULUM_ARCHITECTURE.md`) | Actual in `cp01` (Lines) | Stage 1 Spoiler-Free? | Statement Self-Contained? | 3 Hints | Full Solution & Code | Verdict |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `CP-I.1` | `#078` Typical90 #065 — RGB Balls 2 (`1B#5`) | `#078` Typical90 #065 — RGB Balls 2 (125–218) | Yes | Yes | 3/3 | Yes (1D convolution + lower bound cut) | **PASS** |
| `CP-I.2` | `#144` Luogu P3338 — [ZJOI2014] 力 (`1B#16`) | `#144` Luogu P3338 — [ZJOI2014] 力 (222–311) | **NO** (Hint 1 line 241 names technique) | Yes | 3/3 | Yes (2-pass FFT difference convolution) | **FIX HINT 1** |
| `CP-I.3` | `#246` HDU 5279 — YJC plays minecraft (`1A#26`) | `#246` HDU 5279 — YJC plays minecraft (315–419) | Yes | **NO** ("either... or... Let us state both", 321–333) | 3/3 | Yes ($\ln G$ + circular inv) | **FIX STATEMENT** |
| `CP-I.4` | `#032` ABC 276 G — Count Sequences (`1A#4`) | `#032` ABC 276 G — Count Sequences (423–529) | Yes | Yes | 3/3 | Yes ($[x^k]\frac{(1+x+x^2)^N}{(1-x)^2(1-x^3)^{N-1}}$) | **PASS** |
| `CP-I.5` | `#079` JSC 2019 Qual F — Candy Retribution (`1A#25`) | `#079` JSC 2019 Qual F — Candy Retribution (533–669) | Yes | **NO** (`\dots` on line 543 + "Wait —" on 545) | 3/3 | Draft "Wait:" notes on lines 593–605 | **CRITICAL FIX** |
| `CP-I.6` | `#250` Project Euler 755 — Not Zeckendorf (`1B#14`) | `#250` Project Euler 755 — Not Zeckendorf (673–762) | **NO** (Hint 1 line 691 names $\operatorname{PSET}$ OGF) | Yes | 3/3 | Yes (tail sum $S_k = F_{k+2}-2$ DP) | **FIX HINT 1** |
| `CP-I.7` | `#037` ABC 284 Ex — Count Unlabeled Graphs (`5B#3`) | `#037` ABC 284 Ex — Count Unlabeled Graphs (766–867) | Yes | Yes | 3/3 | Yes (Burnside over $p(N) \le 42$ + UF/DFS) | **PASS** |
| `CP-I.8` | `#024` ABC 236 Ex — Distinct Multiples (`1A#27`) | `#024` ABC 236 Ex — Distinct Multiples (871–996) | Minor leak + typo in Hint 1 (line 889) | Yes | 3/3 | Uses `Ch 24` SPS alongside `Ch 04.3` Boxed DP | **FIX SPS REF & HINT 1** |

---

## 2. Detailed Line-Referenced Findings & Required Fixes

### 2.1 Critical & Major Defects in `checkpoints/cp01-part1-foundations.qmd`

#### Finding CP-1 (CRITICAL): Unfinished Equation (`\dots`) and Unedited Stream-of-Consciousness Draft Notes in `CP-I.5 (#079 JSC 2019 Qual F — Candy Retribution)`
- **Location**: `checkpoints/cp01-part1-foundations.qmd`, lines 536–554 (Problem Statement) and lines 593–605 (Full Derivation).
- **Evidence**:
  - In lines 541–548, the visible problem statement reads:
    > $$\text{there exists a threshold } t \ge 0 \text{ such that } M \text{ children have } c_i = t + 1 \text{ (or } \ge t + 1\text{) and } N - M \text{ children have } c_i \le t \text{ with } \max c_i - \min_{\text{top } M} c_i \le \dots$$
    > Wait — let us state the exact mathematical condition of **AtCoder JSC 2019 Qualification Problem F (Candy Retribution)**:
    > You distribute $S \in [L, R]$ identical candies among $N$ distinguishable children ($c_1 + \dots + c_N = S$, $c_i \ge 0$). If we sort the candy counts in non-increasing order $b_1 \ge b_2 \ge \dots \ge b_N \ge 0$, the distribution is valid if and only if it is **not** the case that $b_M > b_{M+1}$ and $b_1 - b_M > 1$? Let us state the exact condition cleanly so that the problem is 100% self-contained:
  - In lines 593–605, the solution derivation again contains raw stream-of-consciousness hesitation:
    > Wait: when is a sorted sequence $b_1 \ge \dots \ge b_N$ **bad** (not achievable by $S$ step-by-step greedily)? ... Wait: if $c_1 = 5, c_2 = 1, c_3 = 1$ ($N=3, M=2$), the top $M=2$ are $\{5, 1\}$...
- **Mathematical Audit of JSC 2019 Qual F**:
  - In AtCoder JSC 2019 Qual F (*Candy Retribution*), $N$ children receive $a_1, \dots, a_N \ge 0$ candies with $L \le \sum_{i=1}^N a_i \le R$. A child is angry if another child received strictly more candies. Wait: in the official JSC 2019 Qual F problem, we count tuples $(a_1, \dots, a_N)$ with $L \le \sum a_i \le R$ such that when sorted $b_1 \ge b_2 \ge \dots \ge b_N$, the $M$ children with the largest values... Specifically, in `problem_archive.md` §2 (`1A-25`, lines 318–322) and `cohort3_wave_1a_modelling_foundations.md`, JSC 2019 Qual F reduces to subtracting invalid tuples where $\ge M$ elements are $\ge k$ and the remaining elements are $< k$ (or where $b_1, \dots, b_M \ge t$ and $b_{M+1}, \dots, b_N \le t-1$ with bounded range $[0, t-1]$), evaluated in $O(R \ln R)$ harmonic time via $\binom{N}{M}$ and Inclusion-Exclusion / Bounded Composition $(1 - x^t)^{N-M}(1-x)^{-N}$.
- **Required Fix**:
  1. Delete lines 536–550 completely and replace them with a single, clean, self-contained mathematical problem statement matching the exact recurrence solved in lines 605–665 (counting tuples $(c_1, \dots, c_N) \in \mathbb{Z}_{\ge 0}^N$ with $L \le \sum_{i=1}^N c_i \le R$ satisfying the threshold dominance condition over $t \ge 1$, or the exact JSC 2019 Qual F condition).
  2. Delete the hesitant `"Wait: ..."` paragraphs on lines 593–605 and present the direct algebraic reduction to the harmonic sum $\sum_{t \ge 1} \sum_{j} (-1)^j \binom{N-M}{j} [x^S] \frac{x^{\text{offset}(t, j)}}{(1-x)^N}$ cleanly.

#### Finding CP-2 (MAJOR): Hedged "Either / Or / Let Us State Both" Problem Statement in `CP-I.3 (#246 HDU 5279 — YJC plays minecraft)`
- **Location**: `checkpoints/cp01-part1-foundations.qmd`, lines 317–336.
- **Evidence**:
  - Lines 321–333 state:
    > ...either:
    > 1. Inside every island $i$, you may choose any **connected spanning subgraph** on its $a_i$ vertices...
    > 2. Or (in the circular block-partition formulation of HDU 5279), you have $N$ labeled vertices arranged on a circle...
    > Let us state both exact sub-problems so the problem is 100% self-contained:
- **Required Fix**:
  - State the canonical problem cleanly without meta-commentary ("either / or / Let us state both"): ask for the connected spanning subgraph EGF $C(x) = \ln G(x)$ (`Ch 04.1`) combined with the cyclic sequence composition $(1 - C(x))^{-1}$ (`Ch 01.4`), and show how both queries ($c_n = n![x^n]\ln G(x)$ and $z_n = n![x^n](1 - C(x))^{-1}$) are answered in a single `ln` + `inv` pipeline.

#### Finding CP-3 (MAJOR): Stage 1 Spoiler-Free Protocol Violations in `CP-I` Hints
- **Location**: `checkpoints/cp01-part1-foundations.qmd`, lines 241 (`CP-I.2`), 691 (`CP-I.6`), and 889 (`CP-I.8`).
- **Rule (`CURRICULUM_ARCHITECTURE.md` §5.1 & System Instructions Dim 5)**:
  - *"For Blind Checkpoints (`CP-I`–`CP-VI`), verify 100% Spoiler-Free Stage 1: the visible problem table and problem statement + Hint 1 must NOT reveal the chapter number or technique name!"*
- **Violations**:
  1. **Line 241 (`CP-I.2` Hint 1)**: Says *"This is the textbook signature of **Standard Convolution + Reverse-Indexing Difference Convolution (Cross-Correlation)**."* — This literally copies the Stage 2 Routing Key into Hint 1!
     - **Fix**: Rewrite Hint 1 to focus purely on the index pattern: *"Notice that $q_i / (i - j)^2$ depends only on the index $i$ and the distance $d = i - j$. In a standard polynomial product $C_k = \sum_{a+b=k} A_a B_b$, the indices sum to a constant. How can you re-index the sequence $q_1, \dots, q_N$ so that the difference $i - j$ becomes a sum of two array indices?"*
  2. **Line 691 (`CP-I.6` Hint 1)**: Says *"Selecting a subset of distinct elements from $\{F_2, F_3, F_4, \dots\}$ is the **0-1 Subset-Sum ($\operatorname{PSET}$) Construction** with Ordinary Generating Function: $P(x) = \prod_{k \ge 2}(1 + x^{F_k})$."* — Explicitly gives away the `PSET` operator name and OGF in Hint 1!
     - **Fix**: Rewrite Hint 1 to ask the reader to model choosing each Fibonacci number at most once as a product of two-term factors, and then ask why direct coefficient array expansion up to $N = 10^{13}$ is impossible without exploiting the rapid growth of $F_k$.
  3. **Line 889 (`CP-I.8` Hint 1)**: Has a missing space typo (`Instead ofInclusion-Exclusion`) and immediately names *"the **connected-component exponential formula**"*.
     - **Fix**: Fix the typo `of Inclusion-Exclusion` and keep Hint 1 focused on translating the $\binom{N}{2}$ pairwise inequalities $x_i \neq x_j$ into a sum over spanning graphs $G = (V, E)$ with edge weights $-1$, saving the Connected-Component Exponential Formula ($\operatorname{SET}$ / Boxed Product) for Hint 2.

#### Finding CP-4 (MODERATE): Forward Reference to `Ch 24` Set Power Series in `CP-I`
- **Location**: `checkpoints/cp01-part1-foundations.qmd`, lines 63, 89, and 940–945.
- **Evidence**:
  - Line 63: *"Set Power Series (`Ch 04`)"* — Incorrect chapter attribution! Set Power Series ($\operatorname{SPS}$) is taught in **Chapter 24** (`Part VI`), whereas Chapter 04 teaches **Labeled EGFs & the Minimum-Label Boxed Product ($\operatorname{SET}$ ODE $F' = C' F$)**.
  - Line 89 (Stage 2 Routing Key) & lines 940–945 (`CP-I.8` Derivation): Refers to the Set Power Series ring $\mathbb{Q}[z_1, \dots, z_N]/(z_1^2, \dots, z_N^2)$ and Ranked Mobius/Zeta Transform (`Ch 24.2`).
- **Required Fix**:
  - In line 63 and line 89, replace *"Set Power Series (`Ch 04`)"* with *"Subset-Indexed Labeled $\operatorname{SET}$ / Boxed Product DP (`Ch 04.3`)"*.
  - In `CP-I.8` lines 940–950, present the subset-indexed Minimum-Label Boxed Product recurrence $F_S = \sum_{T \subseteq S,\, \min(S) \in T} W_T F_{S \setminus T}$ (`Ch 04.3`, which runs in $O(3^N) \approx 4.3 \times 10^7$ operations for $N=16$) as the primary Part I method, and add a brief forward-reference callout noting that in `Ch 24.2` (Set Power Series) this $O(3^N)$ subset convolution is accelerated to $O(N^2 2^N)$ via Ranked Zeta/Möbius transforms.

---

### 2.2 Major & Moderate Issues in `chapters/ch04-egf-set-cyc-boxed-prufer.qmd`

#### Finding CH04-1 (MAJOR): Duplicate Connected-Graph Problem in `SS-2 (#007 fps_24_m)`
- **Location**: `chapters/ch04-egf-set-cyc-boxed-prufer.qmd`, lines 477–541 (`SS-2 #007`) vs. lines 545–613 (`Int-1 #161`).
- **Diagnosis**:
  - `CURRICULUM_ARCHITECTURE.md` (line 202) and `PROBLEM_CURATION.md` (line 135) assign:
    - `SS-2 (#007)`: `fps_24_m` — Value of Permutation (`1A#20`): Cycle Decomposition EGF $\ln\frac{1}{1-x}$ & Pointer Tracking.
    - `Int-1 (#161)`: Luogu P4841 — [集训队作业2013] 城市规划 (`1A#9a`): Labeled Connected Graphs via $\ln G(x)$.
  - Because `problem_archive.md` §1.1 lists `fps_24_m` as Connected Graph (`1A#9b`), the author tried to cover both by splitting `SS-2 (#007)` into **Part A (Labeled Connected Simple Graphs)** and **Part B (Cycle-Weight Sum over Permutations)**. However, Part A is mathematically identical to `Int-1 (#161 Luogu P4841)` immediately following it!
- **Required Fix**:
  - Make `SS-2 (#007)` a focused, single-statement problem on **Cycle Decomposition EGF $\ln\frac{1}{1-x}$ & Pointer Tracking (Value of Permutation, `1A#20`)**, where each permutation $\pi \in S_n$ has weight $\prod_{C \in \pi} w(|C|)$ or $\sum_{C \in \pi} w(|C|)$. Keep only a 1-sentence parenthetical note mentioning that on AtCoder Library Practice / `fps_24_m`, the $\ln G(x)$ template is also tested via Labeled Connected Graphs (which is solved in full in `Int-1 #161` right below).

#### Finding CH04-2 (MAJOR): Bijection Violation in `Int-2 (#008 fps_24_n — Tree)` (Stealing `fps_24_k` from `Syn-01 #006`)
- **Location**: `chapters/ch04-egf-set-cyc-boxed-prufer.qmd`, lines 617–681.
- **Diagnosis**:
  - `CURRICULUM_ARCHITECTURE.md` (line 204) assigns `Int-2 (#008)` to:
    - `#008` `fps_24_n` — Tree (`3A#2`): Prüfer Sequence Degree-Distribution EGF $n![x^{n-2}]\prod E_{d_i}(x)$.
  - In `ch04` lines 617–681, the author split `Int-2 (#008)` into **Part A (Labeled Trees with Degree Constraints via Prüfer EGF)** and **Part B (Indecomposable Permutations `fps_24_k` via $I(x) = 1 - F(x)^{-1}$)**.
  - However, `#006 fps_24_k — Permutation` is explicitly assigned to **Chapter 25 (`Syn-01 #006`, `CURRICULUM_ARCHITECTURE.md` line 1255)**! Solving `fps_24_k` inside `Ch 04 Int-2` breaks the strict 259-problem bijection across the textbook.
- **Required Fix**:
  - Remove Part B (`fps_24_k` Indecomposable Permutations) from `Ch 04 Int-2 (#008)`, and dedicate `Int-2 (#008)` 100% to **Prüfer Sequence Degree-Distribution EGF (`3A#2`)** (counting labeled trees on $N$ vertices where each vertex $i$ has degree $d_i \in S_i$ or where the degree sequence / degree-weight EGF is given).

#### Finding CH04-3 (MINOR): Clean Up "Variant A / Variant B" Framing in `Adv-1 (#083 CF 407E / Gym — k-Cycle)`
- **Location**: `chapters/ch04-egf-set-cyc-boxed-prufer.qmd`, lines 685–757.
- **Diagnosis**:
  - Lines 685–691 present `#083` as **Variant A (Involutions $p_{p_i} = i$ vs. Derangements / Forbidden 1- and 2-Cycles)** and **Variant B (General Allowed Cycle-Length Set $S \subseteq \{1, \dots, N\}$)**. Since Variant A is simply the special case $S = \{3, 4, \dots, N\}$ (or $S = \{1, 2\}$) of Variant B, merge them into a single clean statement: given $N$ and an allowed cycle-length set $S \subseteq \{1, \dots, N\}$ (highlighting $S = \{3, \dots, N\}$, i.e., $p_i \neq i$ and $p_{p_i} \neq i$, as a concrete motivating example), compute the number of permutations in $S_N$ whose cycle lengths all lie in $S$.

#### Finding CH04-4 (MINOR): Missing `daq_prod` Helper in `Adv-2 (#011 fps_24_q — Dice)` & Binomial Inversion Cross-Reference in `Mas-2 (#174 Luogu P5401)`
- **Location**: `chapters/ch04-egf-set-cyc-boxed-prufer.qmd`, lines 814 (`Adv-2`) and 945–957 (`Mas-2`).
- **Details**:
  1. In `Adv-2 (#011 fps_24_q — Dice)` line 814, the C++ snippet calls `Poly Q = daq_prod(0, N - 1);` without defining `daq_prod` in the code block (or using the `Ch 02` frequency-bucketed $\ln/\exp$ sum when $A_i$ values repeat). Add the 7-line recursive binary product tree function `daq_prod(int l, int r)` inside the code block and add a 1-sentence note that Divide-and-Conquer Product Trees are analyzed in full in `Ch 09.1`.
  2. In `Mas-2 (#174 Luogu P5401 — 珍珠)` lines 945–957, the author commendably derives the $(x-1)$ Taylor shift identity $\sum_{k=0}^j \binom{j}{k}(x-1)^k = x^j \implies f_k = \sum_{j=k}^D (-1)^{j-k}\binom{j}{k}g_j$ directly from the Binomial Theorem so that no unproved black box is used. Add a 1-sentence cross-reference noting that this exact $(x-1)$-basis change is formalized as **Binomial Inversion** in `Ch 08.1`.

---

### 2.3 Minor Polish Items in `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd`

#### Finding CH02-1 (MINOR): Define `build_prod` Helper in `Adv-1 (#157 Luogu P4705 — 玩游戏)` and Add EGF Preview Note
- **Location**: `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd`, lines 963–993 (`Adv-1 #157`) and lines 1173–1182 (`Mas-2 #091`).
- **Details**:
  1. In `Adv-1 (#157 Luogu P4705)` line 977, `Poly PA = build_prod(0, n - 1);` is called without defining `build_prod` in the C++ snippet. Include the 7-line recursive binary merge function `build_prod(int l, int r)` in the snippet so the code is 100% self-contained, accompanied by a brief pointer to `Ch 09.1` (Divide-and-Conquer Product Trees).
  2. Both `Adv-1 (#157 Luogu P4705)` (lines 963–965) and `Mas-2 (#091 CF 891E)` (lines 1173–1182) use factorial-scaled series $\sum_{p=0}^t \frac{S_A(p)}{p!}x^p$ and $e^{nx}\prod(a_i - x)$. While all steps are algebraically derived from the Binomial Theorem inside `ch02` without invoking any unproved `Ch 04` theorem, add a 1-sentence remark in `Adv-1` noting that dividing by $p!$ turns binomial convolution into ordinary Cauchy multiplication — previewing **Exponential Generating Functions (EGFs)** in `Ch 04`.

#### Finding CH02-2 (MINOR): Unbundle Grouped Bullet Points in §2.7 Quarantined Reference Templates (`R-*`)
- **Location**: `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd`, lines 1230–1242.
- **Details**:
  - `PROBLEM_CURATION.md` §5 assigns 11 quarantined templates to Chapter 02: `R-06`, `R-09`, `R-10`, `R-12`, `R-13`, `R-14`, `R-15`, `R-16`, `R-17`, `R-18`, `R-19`.
  - In `ch02` lines 1239–1242, `R-13`–`R-16` and `R-17`–`R-19` are compressed into two summary bullets (`R-13`–`R-16: Library Checker / Luogu P4726 & P5245...` and `R-17`–`R-19: Library Checker — Log / Exp / Pow of Formal Power Series (Sparse)`). Expand them or list the exact ID-to-problem mapping (`R-13` Luogu P4726 `exp`, `R-14` Luogu P5245 `pow`, `R-15` `inv_of_formal_power_series_sparse`, `R-16` `sqrt_of_formal_power_series_sparse`, `R-17` `log_of_formal_power_series_sparse`, `R-18` `exp_of_formal_power_series_sparse`, `R-19` `pow_of_formal_power_series_sparse`) so every `R-*` ID is individually searchable.

---

## 3. Audit of Revisited Cross-References & Quarantined Templates (`R-01`–`R-67`)

### 3.1 Multi-Resolution Revisited Cross-References (`CURRICULUM_ARCHITECTURE.md` §4.2 & §5.2)
All 3 Part I Revisited Threads required by `CURRICULUM_ARCHITECTURE.md` §4.2 and `PROBLEM_CURATION.md` §4.2 are present, mathematically accurate, and cross-referenced in both the chapter ladders and `CP-I`:
1. **Thread #1 (`#084` CF 438E — The Child and Binary Tree)**:
   - Present in `ch02` lines 1054–1063 (*Multi-Resolution Revisited Note (`Ch 02` $\to$ `Ch 09` $\to$ `Ch 10`)*) and `cp01` lines 1004–1007. Accurately contrasts `Ch 02` Quadratic Radical $\frac{1-\sqrt{1-4C(x)}}{2C(x)}$, `Ch 09` CDQ Divide-and-Conquer NTT, and `Ch 10` Implicit Newton Iteration.
2. **Thread #2 (`#153` Luogu P4389 — 付公主的背包)**:
   - Present in `ch03` lines 1110–1113 (*Multi-Resolution Revisited Note (`Ch 03` $\to$ `Ch 02` $\to$ `Ch 09`)*) and `cp01` lines 1009–1012. Accurately contrasts the `Ch 03`/`Ch 02` $O(M \ln M + M \log M)$ Frequency-Grouped Harmonic Sieve + $\exp$ against `Ch 09` Divide-and-Conquer Product Tree + $\ln/\exp$.
3. **Thread #3 (`#161` Luogu P4841 — [集训队作业2013] 城市规划)**:
   - Present in `ch04` lines 608–611 (*Multi-Resolution Revisited Note (`Ch 04` $\to$ `Ch 07/13` $\to$ `Ch 09`)*) and `cp01` lines 1014–1017. Accurately contrasts `Ch 04` EGF Logarithm $C(x) = \ln G(x)$, `Ch 04.3` Boxed Product ODE $G' = C' G$ solved via `Ch 09` CDQ NTT, and `Ch 13` Chirp-Z Transform for $\binom{n}{2}$ edge weights.

### 3.2 Quarantined Pure-Engine Templates (`PROBLEM_CURATION.md` §5)
| Chapter | Assigned `R-*` Templates in `PROBLEM_CURATION.md` §5 | Verified in `.qmd` File | Status |
| :--- | :--- | :--- | :---: |
| `Ch 01` | `R-01`, `R-02`, `R-03`, `R-04`, `R-11`, `R-44`, `R-47`, `R-60` (8 templates) | `ch01` §1.6 (lines 1143–1157) & `cp01` (line 1025) | **100% PASS** |
| `Ch 02` | `R-06`, `R-09`, `R-10`, `R-12`, `R-13`, `R-14`, `R-15`, `R-16`, `R-17`, `R-18`, `R-19` (11 templates) | `ch02` §2.7 (lines 1230–1242) & `cp01` (line 1026) | **PASS** (unbundle `R-13`–`R-19` bullets in `ch02`) |
| `Ch 03` | `R-25` (1 template: `partition_function`) | `ch03` §3.7 (lines 1505–1508) & `cp01` (line 1027) | **100% PASS** |
| `Ch 04` | `R-24`, `R-37` (2 templates: `bell_number`, `labeled_graph`) | `ch04` §4.6 (lines 1019–1027) & `cp01` (line 1028) | **100% PASS** |

---

## 4. Quarto Formatting & Render Safety Check (Problem Ladders & `CP-I`)

- **Forbidden Math Delimiters (`\(` or `\[`)**: Zero occurrences across all 5 files.
- **Unclosed `<details>` or `:::` Blocks**: All 40 problem entries (32 in `Ch 01`–`Ch 04` + 8 in `CP-I`) have properly balanced `<details><summary>...</summary> ... </details>` blocks (4 per problem in `Ch 01`–`Ch 04`, plus the Stage 2 Routing Key in `CP-I`).
- **Markdown Table Pipe Escaping**: No unescaped `|` inside `$...$` in any Markdown table across the problem ladders or `CP-I`.
