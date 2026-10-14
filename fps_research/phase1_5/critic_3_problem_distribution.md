# Phase 1.5 Adversarial Audit Report — Critic 3: Problem Distribution, Ladder Smoothness & Blind Checkpoints

**Auditor**: Curriculum Critic 3 (Problem Distribution, Ladder Smoothness & Blind Checkpoint Auditor)  
**Target Documents Audited**:
1. **Proposal A (Modelling-First)**: `fps_research/phase1_5/proposal_A_modelling_first.md` (24 Chapters, 6 Parts)
2. **Proposal B (DAG / Algebraic)**: `fps_research/arch_proposal_1_5A_dag.md` (24 Chapters, 6 Parts)
3. **Proposal C (Problem Curation Architect)**: `fps_research/phase1_5_round1_problem_curation_architect.md` (20 Chapters, 6 Parts)
4. **Baseline Corpus**: `fps_research/PROBLEM_CURATION.md` & `fps_research/problem_archive.md` (254 Unique Accepted Problems + 67 Quarantined Template/Trivial Problems `R-01`–`R-67` = 321 Total Catalogued Problems)

---

## Executive Summary & Head-to-Head Scorecard

An exhaustive problem-by-problem audit of all three Round 1 proposals against the 321-problem baseline (`254` accepted non-template problems + `67` quarantined bare templates `R-01`–`R-67`) reveals sharp structural trade-offs and critical accounting bugs across all three drafts:

| Audit Dimension | Proposal A (Modelling-First, 24 Ch) | Proposal B (DAG / Algebraic, 24 Ch) | Proposal C (Problem Curation Architect, 20 Ch) | Critic 3 Verdict & Synthesis Target |
| :--- | :--- | :--- | :--- | :--- |
| **1. Corpus Accounting & Deduplication (`254` Unique + `67` Templates)** | **B+** (`188` Ladder + `48` Checkpoint + `18` Notes = `254` claimed, but has **11 cross-slot duplicates** and **2 template leaks**: `P4719`, `P5325` `R-52`) | **F** (Claims `210 + 36 + 8 = 254`, but **36/36 (100%) of Checkpoint problems are verbatim duplicates of its own Chapter Ladders**, plus **25+ cross-chapter duplicates** and **16 quarantined `R-xx` templates** in ladders; drops ~70 real problems) | **A-** (`160` Ladder + `40` Checkpoint + `54` Archive = `254`, with `R-01`–`R-67` cleanly isolated in footnotes; **HOWEVER**, **26/40 (65%) of Checkpoint III–VI problems duplicate its own Ch 9–20 Ladders** while 54 Archive problems sit unused!) | Combine **Proposal C's strict 1-to-1 corpus accounting & template footnotes** with **Proposal A's true Ladder-vs-Checkpoint disjointness** across a **24-Chapter (`192` Ladder + `48` Checkpoint + `14` Synthesis Archive = `254`)** matrix. |
| **2. Difficulty Curve & Prerequisite Safety (Zero Forward References)** | **B+** (Smooth 4-tier ladders, but has **3 forward-reference traps**: `Luogu P4747` in Ch 07 before Newton/LIF; `P6295`/`P7364` in Ch 13 before Ch 21 CZT; `UOJ 310` in Checkpoint V routed to Ch 04 before Ch 23 FWT) | **D** (Severe **slash-stuffing** `A / B / C` in single slots, **broken/mismatched URLs**, and **8 major forward-reference traps** e.g. `CF 917D` in Ch 2, `P4705` in Ch 3, `CF 1336E2` & `UOJ 310` in Ch 4, `ABC 253 Ex` in Ch 15) | **A** (Explicitly audits and resolves **16 forward-reference traps `F-01`–`F-16`**; strict `2 SS / 2 Int / 2 Adv / 2 Mas` 3-hint pedagogical problem cards; zero forward-reference leaks) | Adopt **Proposal C's prerequisite ordering fixes (`F-01`–`F-16`) and 3-hint problem card architecture** across **Proposal A's 24-chapter granularity**. |
| **3. Under-Served Topic Rescue (12 Starved Clusters)** | **A** (Best structural rescue: dedicated full chapters for **Cluster Method [Ch 08]**, **Cacti [Ch 12] vs DAGs/Bipartite [Ch 13]**, **Sparse ODE/`EI 科技` [Ch 19]**, **CZT & Sampling Shift [Ch 21]**, **Set Power Series [Ch 23]**, and **$q$-Series [Ch 24]**) | **C+** (Dedicated Ch 22 Tree FPS and Ch 23 Composition, but crams **$q$-Series + SPS + Dirichlet** into a single Ch 24, starving $q$-Series to 2 problems and SPS to 3 problems; contaminates Composition with `R-32`/`R-33`/`R-34`) | **B+** (Rescues Tree FPS [Ch 19], PGFs [Ch 8], Diagonals [Ch 16], Lattice Walks [Ch 12], but **20-chapter compression** forces **$q$-Series + SPS** to share Ch 20 [`4+4` probs] and **`mulT` + MPE + Sampling Shift + Composition** to share Ch 18) | Expand Proposal C from **20 chapters to 24 chapters** using Proposal A's chapter splits so **Cluster Method, Cacti vs DAGs, `mulT`/Composition vs CZT/Sampling Shift, Set Power Series, and $q$-Series** each get a dedicated 8-problem ladder. |
| **4. Blind Topic-Group Checkpoints (`CP1`–`CP6`)** | **B+** (48 problems across 6 checkpoints; **94% disjoint** from chapter ladders; collapsible `<details>` answer keys; flawed by duplicate `ABC 260 Ex` in `II-7` & `V-7`, template `P5325` in `VI-1`, and non-FPS `CF 809E` in `III-8`) | **F** (**0% disjoint**: all 36 checkpoint problems are already solved in Proposal B's own chapter ladders; **spoilers printed inline** in Column 4 of the problem table; forward-reference leaks in `CP1-2` and `CP1-6`) | **B** (Best two-stage format: spoiler-free `Hint 1` Recognition Rubric separated from `Hint 2/3` Answer Key; zero forward references; **flawed by 26/40 problems in `CP3`–`CP6` duplicating Ch 9–20 ladders**) | Enforce **100% disjointness** between the 192 Chapter Ladder slots and 48 Blind Checkpoint slots (replacing Proposal C's 26 duplicated `CP3`–`CP6` slots with the 54 Archive problems) while keeping **Proposal C's two-stage spoiler-free rubric format**. |

---

## Dimension 1: Corpus Accounting, Duplication & Template Quarantine (`R-01`–`R-67`) Audit

### 1.1 Baseline Corpus Rules (`PROBLEM_CURATION.md`)
The repository's Phase 1 curation established two non-negotiable invariants:
1. **Zero Bare Templates in Pedagogical Ladders**: All 67 bare polynomial/combinatorial template problems (`R-01` through `R-67`, including Luogu `【模板】` problems, Library Checker bare verifiers, and trivial 1-step applications like `ABC 205 E`) are quarantined. They may be cited as 1-line implementation unit-test footnotes, **never** as primary `Stepping Stone`–`Mastery` ladder problems or Blind Checkpoint problems.
2. **Strict Disjointness Between Ladders and Blind Checkpoints**: A Blind Checkpoint only tests *topic recognition* if the student has not already solved the exact same problem two pages earlier inside a named Chapter Ladder. Furthermore, no problem should consume two primary ladder slots across different chapters (cross-chapter multi-perspective analyses belong in prose callouts, not double-counted ladder slots).

### 1.2 Audit of Proposal A (`proposal_A_modelling_first.md`)

Proposal A claims `188` Chapter Ladder problems + `48` Blind Checkpoint problems + `18` inline variant notes = `254` problems. However, close inspection reveals **11 internal duplications** and **2 template quarantine violations**:

#### A. Quarantined Template Violations in Proposal A
| Problem ID | Quarantine ID | Where Used in Proposal A | Audit Verdict & Required Fix |
| :--- | :--- | :--- | :--- |
| **Luogu P5325 — 【模板】Min_25 筛** | `R-52` | **Ch 24 Int #5** AND **Blind Checkpoint VI (`VI-1`)** | **CRITICAL VIOLATION**: Not only is `Luogu P5325` a quarantined `【模板】` problem (`R-52`) with zero FPS content (pure multiplicative prime-prefix DP), Proposal A uses it **twice** (once in Ch 24's ladder and again in Checkpoint VI!). **Fix**: Demote `P5325` to a footnote and replace with $q$-series problems `AtCoder ABC 238 Ex` and `Codeforces 1916F / Luogu P6118`. |
| **Luogu P4719 — 【模板】动态 DP** | Unnumbered `【模板】` | **Ch 22 Int #4** | **MODERATE VIOLATION**: Placed as a primary Intermediate ladder slot in Ch 22 (Tree FPS). While it bridges tropical $(\max, +)$ HLD matrix products to $(+, \times)$ polynomial HLD products, it is literally a Luogu `【模板】` problem. **Fix**: Move `Luogu P4719` to the Ch 22 Implementation Verification Footnote and promote **`AtCoder ABC 220 H — Security Camera`** or **`QOJ 4815 — Tree Distance`** into the primary ladder. |

#### B. Cross-Chapter & Ladder-to-Checkpoint Duplications in Proposal A
| Problem ID | Occurrence 1 in Proposal A | Occurrence 2 in Proposal A | Nature of Collision & Required Fix |
| :--- | :--- | :--- | :--- |
| **AtCoder ABC 260 Ex — Colorfulness** | **Blind Checkpoint II (`II-7`)** | **Blind Checkpoint V (`V-7`)** | **BLATANT CHECKPOINT COLLISION**: Identical problem assigned to two different Blind Checkpoints! Keep in `II-7` (or Ch 20 Primary Ladder) and replace `V-7` with `yukicoder 1080` or `AtCoder ARC 136 F`. |
| **Codeforces 451E — Devu and Flowers** | **Ch 01 Int #3** | **Ch 21 SS #2** | **Double Primary Slot**: Keep in **Ch 01 Int #3** (bounded OGF stars-and-bars + IE); in Ch 21 (Interpolation), reference `CF 451E` in prose only and assign **`Codeforces 622F — The Sum of the $k$-th Powers`** or **`Luogu P5437 — 【XR-2】缘分`** to the ladder slot. |
| **Codeforces 917D — Stranger Trees** | **Ch 13 Int #2** | **Ch 22 Mas #8** | **Double Primary Slot**: Keep in **Ch 13** (Cayley forest formula $n^{c-2}\prod s_i$ + tree DP) or **Ch 22**; fill the freed slot with **`AtCoder ABC 253 Ex — We Love Forest`** / **`Codeforces 156D — Clues`**. |
| **Codeforces 755G — PolandBall and Many Other Balls** | **Blind Checkpoint I (`I-8`)** | **Ch 18 Adv #6** | **Ladder-vs-Checkpoint Collision**: A student who solves `CF 755G` in Blind Checkpoint I after Part I will immediately recognize it in Ch 18! Move `CF 755G` exclusively to the D-Finite / Matrix-Power chapter ladder and replace `I-8` with **`AtCoder ABC 230 G — GCD Permutation`** or **`Codeforces 891E — Lust`**. |
| **Codeforces 932E — Team Work** | **Blind Checkpoint II (`II-2`)** | **Ch 19 Int #3** | **Ladder-vs-Checkpoint Collision**: Keep `CF 932E` in Stirling / Differential Operator ladder and replace `II-2` with **`Codeforces 1278F — Cards`**. |
| **Codeforces 1515E — Phoenix and Computers** | **Blind Checkpoint II (`II-4`)** | **Ch 19 Adv #6** | **Ladder-vs-Checkpoint Collision**: Keep `CF 1515E` in the EGF / ODE chapter ladder and replace `II-4` with **`Luogu P4859 — 已经没有什么好害怕的了`**. |
| **AtCoder ABC 222 H — Beautiful Binary Tree** | **Blind Checkpoint III (`III-3`)** | **Ch 18 Int #3** | **Ladder-vs-Checkpoint Collision**: Keep `ABC 222 H` in the Lagrange Inversion / D-Finite ladder and replace `III-3` with **`Luogu P6672 — [清华集训2016] 你的生命已如风中残烛`**. |
| **UOJ 450 — 【集训队作业2018】复读机** | **Ch 18 Adv #7** | **Blind Checkpoint V (`V-8`)** | **Ladder-vs-Checkpoint Collision**: Keep `UOJ 450` in the Root-of-Unity + EGF chapter and replace `V-8` with **`LOJ #6509 — 烷基计数 加强版 加强版`**. |
| **UOJ 310 — 【UNR #2】黎明前的巧克力** | **Blind Checkpoint V (`V-6`)** | **Ch 23 Int #4** | **Ladder-vs-Checkpoint Collision + Forward Reference**: Placed in Checkpoint V (after Ch 20) *before* Ch 23 (where FWT/XOR MacWilliams is taught in Proposal A!), and then repeated in Ch 23 Int #4! Keep in Ch 23 and replace `V-6` with **`Luogu P5668 — [NOI2019] 斗主地`**. |
| **Luogu P5827 — 点双连通图计数** | **Ch 12 Mas #6** | **Ch 20 Adv #8 (Note)** | Acceptable if Ch 12 Mas #6 is single-$n$ (`Luogu P5827`) and Ch 20 Adv #8 uses **`QOJ 8528 — Youthful Paths`** as the primary problem. |

---

### 1.3 Audit of Proposal B (`arch_proposal_1_5A_dag.md`)

Proposal B suffers from **two catastrophic curation failures** that invalidate its claimed accounting (`210 + 36 + 8 = 254`):

#### A. Catastrophic Failure 1: 100% Duplication Between Blind Checkpoints (`CP1`–`CP6`) and Chapter Ladders
Every single one of Proposal B's 36 Blind Checkpoint problems (`CP1-1` through `CP6-6`) is already assigned as a primary ladder problem inside Proposal B's own Chapters 1–24:
- **Checkpoint 1 (`CP1-1`–`CP1-6`)**: `CF 1096G` (= Ch 4 #1 & Ch 14 #1), `CF 528D / ABC 269 Ex` (= Ch 1 #4 & Ch 22 #1), `Luogu P4389` (= Ch 3 #1), `CF 451E` (= Ch 2 #4), `Luogu P3784` (= Ch 3 #3), `CF 1336E2` (= Ch 4 #6 & Ch 24 #4).
- **Checkpoint 2 (`CP2-1`–`CP2-6`)**: `ABC 300 Ex` (= Ch 6 #5), `Luogu P4491` (= Ch 4 #5, Ch 5 #6, Ch 7 #4, Ch 9 #6 — appears **4 times** in Proposal B!), `Luogu P4841` (= Ch 5 #4), `Luogu P5293` (= Ch 8 #6), `CF 932E` (= Ch 7 #3 & Ch 9 #4), `CF 960G` (= Ch 5 #7 & Ch 9 #3).
- **Checkpoint 3 (`CP3-1`–`CP3-6`)**: `CF 891E` (= Ch 5 #5 & Ch 10 #3), `Luogu P5339` (= Ch 7 #5 & Ch 9 #7), `Luogu P3702` (= Ch 6 #3 & Ch 8 #5), `CF 917D` (= Ch 2 #7 & Ch 11 #5), `Luogu P4548` (= Ch 10 #5), `Luogu P4389 / P5900` (= Ch 3 #1 & Ch 12 #2).
- **Checkpoint 4 (`CP4-1`–`CP4-6`)**: `Luogu P5296` (= Ch 11 #6 & Ch 15 #2), `LOJ #6538` (= Ch 12 #5 & Ch 14 #6), `Luogu P4747` (= Ch 13 #6 & Ch 23 #7), `Luogu P6295` (= Ch 15 #3), `Luogu P5827` (= Ch 13 #5, Ch 15 #6, Ch 23 #6), `ABC 303 Ex` (= Ch 12 #4 & Ch 14 #5).
- **Checkpoint 5 (`CP5-1`–`CP5-6`)**: `ABC 205 E / CF 1204E` (= Ch 16 #1 & #2), `CF 755G` (= Ch 16 #6, Ch 18 #7, Ch 19 #4), `UOJ #50` (= Ch 14 #4 & Ch 18 #4), `Luogu P5434` (= Ch 15 #7, Ch 17 #5, Ch 19 #5), `Luogu P4456` (= Ch 16 #5 & Ch 17 #4), `Luogu P4721 / P5298` (= Ch 18 #1 & #5).
- **Checkpoint 6 (`CP6-1`–`CP6-6`)**: `ABC 269 Ex` (= Ch 22 #1), `Luogu P6570` (= Ch 24 #2), `Luogu P5828` (= Ch 13 #5, Ch 15 #6, Ch 23 #6), `Luogu P4705` (= Ch 3 #7 & Ch 21 #4), `UOJ #310` (= Ch 4 #7 & Ch 24 #5), `ABC 248 G` (= Ch 22 #5 & Ch 24 #8).

In addition to 36 duplicated checkpoint slots, Proposal B repeats the same problems across 2 to 4 different chapter ladders (`Luogu P4491` 4x, `CF 755G` 4x, `Luogu P5827` 4x, `Luogu P5434` 4x, `CF 438E` 3x, `UOJ #50` 3x) and uses **slash-stuffing** (`Luogu P5298 / UOJ #460 / CF 1344E` in a single row, often with mismatched URLs like linking `CF 1251F / 1344E` to `CF 438E`'s URL or `ABC 253 G` to `abc205_e`). As a result, Proposal B silently drops roughly **70 unique problems** from the 254-problem baseline corpus.

#### B. Catastined Template Contamination (`R-01`–`R-67`) in Proposal B
Proposal B places **16 quarantined template problems** directly into primary chapter ladders:
- `R-39` (`Luogu P4723 【模板】常系数齐次线性递推`) in Ch 6 SS #2
- `R-40` (`Luogu P5487 【模板】Berlekamp–Massey`) in Ch 6 Int #3
- `R-31` (`Luogu P6800 【模板】Chirp Z-Transform`) in Ch 8 Mas #9
- `R-38` (`Luogu P6178 【模板】Matrix-Tree 定理`) in Ch 11 Int #4
- `R-36` (`Luogu P5900 【模板】无标号有根树计数`) in Ch 12 SS #2
- `R-32` (`Luogu P5809 【模板】多项式复合逆`) in Ch 13 SS #2 **and** Ch 23 SS #2
- `R-63` (`AtCoder ABC 205 E — White and Black Balls`) in Ch 16 SS #1 **and** `CP5-1`
- `R-45` (`Luogu P4721 【模板】分治 FFT`) in Ch 18 SS #1 **and** Ch 20 SS #2 **and** `CP5-6`
- `R-41` (`Luogu P7439 【模板】微分有限`) in Ch 19 Mas #8
- `R-26` (`Luogu P5050 【模板】多项式多点求值`) in Ch 21 SS #1
- `R-27` (`Luogu P5158 【模板】多项式快速插值`) in Ch 21 SS #2
- `R-30` (`Luogu P5667 拉格朗日插值2`) in Ch 21 Mas #8
- `R-33` & `R-34` (`Luogu P5373 【模板】多项式复合函数` & `Library Checker — Composition`) in Ch 23 SS #1

---

### 1.4 Audit of Proposal C (`phase1_5_round1_problem_curation_architect.md`)

Proposal C is by far the most disciplined on template quarantine and chapter-to-chapter deduplication, but has **one major accounting bug in Checkpoints III–VI**:

#### A. Template Quarantine Handling in Proposal C (Exemplary)
Proposal C cleanly segregates all 67 quarantined templates (`R-01`–`R-67`) into 1-line **Implementation Verification Footnotes** at the top of each chapter ladder and audits every single one in Section 7 (`R-01`–`R-67`). The only `【模板】` problem in Proposal C's 160 ladder slots is `Luogu P4719` (`【模板】动态 DP`) in Slot `19-1`, explicitly used as a Stepping Stone bridge to `ABC 355 G` (though replacing `19-1` with a non-template HLD/Tree DP problem and keeping `P4719` as the footnote is even cleaner).

#### B. Critical Flaw in Proposal C: 26/40 Checkpoint Problems (`CP3`–`CP6`) Duplicate Primary Chapter Ladders!
In Section 1, Proposal C claims:
- `160` Primary Chapter Ladder Problems (20 Chapters $\times$ 8 problems)
- `40` Blind Checkpoint Problems (`CP1`–`CP6`)
- `54` Annotated Reference Archive Problems (Section 6)
- Total = $160 + 40 + 54 = 254$ unique problems.

Wait: while **Checkpoint I (`CP1-1`–`CP1-7`)** and **Checkpoint II (`CP2-1`–`CP2-7`)** genuinely use distinct problems not found in the 160 Primary Chapter Ladders (with only 1 overlap: `CP1-2` `CF 891E` = Slot `4-3`), **starting at Checkpoint III through Checkpoint VI, Proposal C populates all 26 slots of `CP3`, `CP4`, `CP5`, and `CP6` with verbatim duplicates of problems already in its own Ch 3–Ch 20 Primary Ladders**:

| Proposal C Checkpoint Slot | Problem ID | Duplicate Primary Ladder Slot in Proposal C | Replacement Available in Proposal C's Section 6 Archive (`54` Unused Problems) |
| :--- | :--- | :--- | :--- |
| **`CP1-2`** | `Codeforces 891E — Lust` | Duplicates **Slot `4-3`** | Swap with `AtCoder ABC 241 Ex — Card Deck Score` or `Luogu P4451` |
| **`CP3-1`** | `Codeforces 755G — PolandBall` | Duplicates **Slot `10-6`** | Swap with `Codeforces 623E — Transforming Sequence` (Archive Part III) |
| **`CP3-2`** | `Codeforces 553E — Kyoya and Train` | Duplicates **Slot `11-6`** | Swap with `Luogu P3784 — [SDOI2017] 遗忘的集合` (Archive Part III) |
| **`CP3-3`** | `yukicoder 963 — Complete Binary Tree` | Duplicates **Slot `11-7`** | Swap with `Luogu P4705 — 玩游戏` (after moving MPE earlier or using `Luogu P5298 — [PKUWC2018] Minimax`) |
| **`CP3-4`** | `Codeforces 1096G — Lucky Tickets` | Duplicates **Slot `10-1`** | Swap with `AtCoder ABC 331 G — Collect Them All` (Archive Part III) |
| **`CP3-5`** | `AtCoder ABC 300 Ex — Fibonacci` | Duplicates **Slot `9-2`** | Swap with `Luogu P4173 — 残缺的字符串` (Archive Part III) |
| **`CP3-6`** | `AtCoder ABC 213 Ex — Stroll` | Duplicates **Slot `11-5`** | Swap with `LOJ #6509 — [雅礼集训 2018 Day7] 烷基计数 加强版 加强版` |
| **`CP4-1`** | `AtCoder ABC 303 Ex — Tree Cluster` | Duplicates **Slot `3-4`** | Swap with `AtCoder ABC 222 H — Beautiful Binary Tree` (Archive Part IV) |
| **`CP4-2`** | `Luogu P6598 — 烷烃计数` | Duplicates **Slot `15-5`** | Swap with `Luogu P5828 — 边双连通图计数` (Archive Part IV) |
| **`CP4-3`** | `Codeforces 1349F2 — Slime and Sequences` | Duplicates **Slot `13-8`** | Swap with `Codeforces 1204E — Natasha, Sasha and the Prefix Sums` (Archive Part IV) |
| **`CP4-4`** | `Luogu P6672 — 你的生命已如风中残烛` | Duplicates **Slot `12-5`** | Swap with `Luogu P3266 — [JLOI2015] 骗我呢` (Archive Part IV) |
| **`CP4-5`** | `LOJ #6569 / Luogu P5434 — 有标号荒漠计数` | Duplicates **Slot `15-4`** | Swap with `Codeforces 917D — Stranger Trees` (Archive Part IV) |
| **`CP4-6`** | `Luogu P6295 — 有标号 DAG 计数` | Duplicates **Slot `15-3`** | Swap with `Luogu P7364 — 有标号二分图计数` (Archive Part IV) |
| **`CP4-7`** | `Library Checker — fps_24_s` | Duplicates **Slot `14-2`** | Swap with `Luogu P4456 — [CQOI2018] 交错序列` (Archive Part IV) |
| **`CP5-1`** | `yukicoder 1080 — +- Derived` | Duplicates **Slot `16-3`** | Swap with `UOJ #450 — [集训队作业2018] 复读机` (Archive Part V) |
| **`CP5-2`** | `AtCoder AGC 058 D — Yet Another ABC String` | Duplicates **Slot `16-5`** | Swap with `Luogu P5339 — [TJOI2019] 唱、跳、rap和篮球` (Archive Part V) |
| **`CP5-3`** | `Luogu P5282 — 快速阶乘算法` | Duplicates **Slot `18-2`** | Swap with `Luogu P3703 / P5668 — [NOI2019] 斗主地` |
| **`CP5-4`** | `AtCoder ABC 336 G — 16 Integers` | Duplicates **Slot `17-4`** | Swap with `Luogu P4332 / P3270` or `Codeforces 901E — Cyclic Cipher` |
| **`CP5-5`** | `Codeforces 1770G — Koxia and Bracket` | Duplicates **Slot `18-3`** | Swap with `Luogu P6597 — 烯烃计数` (Archive Part V) |
| **`CP5-6`** | `AtCoder ABC 387 G — Prime Circuit` | Duplicates **Slot `18-1`** | Swap with `AtCoder ABC 260 Ex — Colorfulness` |
| **`CP6-1`** | `AtCoder ABC 269 Ex — Antichain` | Duplicates **Slot `19-2`** | Swap with `Luogu P5327 — [ZJOI2019] 语言` (Archive Part VI) |
| **`CP6-2`** | `Codeforces 1336E2 — Chiori and Doll Picking` | Duplicates **Slot `20-8`** | Swap with `UOJ #310 — [UNR #2] 黎明前的巧克力` (Archive Part VI) |
| **`CP6-3`** | `AtCoder ARC 145 F — Modulo Sum of Powers` | Duplicates **Slot `20-5`** | Swap with `AtCoder ABC 238 Ex — Removing People` |
| **`CP6-4`** | `AtCoder ABC 253 Ex — We Love Forest` | Duplicates **Slot `20-4`** | Swap with `AtCoder ABC 213 G — Connectivity 2` (Archive Part VI) |
| **`CP6-5`** | `Luogu P5827 — 点双连通图计数` | Duplicates **Slot `15-7` & `18-7`** | Swap with `QOJ 8528 — Youthful Paths` |
| **`CP6-6`** | `AtCoder ABC 355 G — Baseball` | Duplicates **Slot `19-3`** | Swap with `Luogu P7279 — [AGM 2021] 树木` (Archive Part VI) |
| **`CP6-7`** | `Luogu P5406 — [THUPC2019] 找树` | Duplicates **Slot `20-7`** | Swap with `Luogu P6570 — [NOI Online #3] 优秀子序列` (Archive Part VI) |

Additionally, in Proposal C's Primary Chapter Ladders, **`Luogu P5827` (点双连通图计数)** occupies **two** primary ladder slots: **Slot `15-7`** (single-$n$ LIF extraction) and **Slot `18-7`** (all-$n$ Kinoshita–Li composition). Replacing Slot `18-7` with **`QOJ 8528 — Youthful Paths`** (which Proposal C already mentions in `18-7`'s Hint 3!) eliminates the only intra-ladder duplication in Proposal C.

---

## Dimension 2: Difficulty Curve, Ladder Smoothness & Forward-Reference Trap Audit

### 2.1 Proposal A Ladder Smoothness & Forward-Reference Audit (Chapters 1–24)

Proposal A uses a 24-chapter architecture (`7–8` problems per ladder, totaling `188` ladder slots). Its tier progression (`Stepping Stone` $\to$ `Intermediate` $\to$ `Advanced` $\to$ `Mastery`) is pedagogically natural in 21 out of 24 chapters, but exhibits **4 specific prerequisite / difficulty curve defects**:

1. **Chapter 07 (`Inclusion-Exclusion, Sieve & Connected-Component Inversion`) — Severe Forward-Reference Trap in Slot #8 (`Luogu P4747 — [CERC2017] Intrinsic Interval / 析合树`)**:
   - **What is wrong**: Counting simple permutations (`Luogu P4747`) requires solving $P(x) = x + 2I(P(x)) + S(P(x))$ via **Compositional Inverse / Newton Iteration** (`Ch 09 / Ch 20`) or **CDQ Divide-and-Conquer NTT** (`Ch 10`), none of which exist in Chapter 07!
   - **Required Fix**: Move `Luogu P4747` to **Chapter 11 (Lagrange Inversion)** or **Chapter 20 (FPS Composition & Reversion)**, and fill Ch 07 Mastery #8 with **`AtCoder ARC 118 E — Avoid Permutations`** or **`Luogu P5400 — [CTS2019] 随机立方体`**.

2. **Chapter 13 (`Functional Digraphs, DAGs, Eulerian & Bipartite Graphs`) — Forward-Reference Trap in Slots #3 & #4 (`Luogu P6295` Labeled DAGs & `Luogu P7364` Bipartite Graphs)**:
   - **What is wrong**: Both `Luogu P6295` and `Luogu P7364` require factoring the bipartite/DAG edge weight $2^{k(n-k)}$ via the quadratic exponent identity $k(n-k) = \binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}$ (Bluestein's / Chirp Z-Transform identity) plus NTT $\exp/\ln$ or $\text{inv}$. However, Proposal A defers Chirp Z-Transform (CZT) until **Chapter 21**!
   - **Required Fix**: Either (a) move **Roots of Unity & Chirp Z-Transform** earlier (into Part II alongside Operator Calculus, as Proposal B Ch 8 and Proposal C Ch 5 do), OR (b) explicitly prove the algebraic identity $ij = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$ as a standalone convolution linearization trick inside Chapter 13 before assigning `P6295` and `P7364`. Moving Roots of Unity + CZT into Part II is cleaner and resolves all quadratic-exponent dependencies at once.

3. **Chapter 12 (`Cacti, Block-Cut Trees & 2-Connected Graphs`) — Implicit Forward Reference in Mastery Slots #6 & #7 (`Luogu P5827` & `Luogu P5828`)**:
   - **What is wrong**: Computing `[x^n]` for a *single* $n$ in `Luogu P5827` (Biconnected Graphs) and `Luogu P5828` (2-Edge-Connected Graphs) takes $O(n \log n)$ via Lagrange Inversion (taught in Ch 11), whereas computing the answer for *all* $1 \le k \le n$ requires $O(n \log^2 n)$ **Kinoshita–Li FPS Composition / Reversion** (not taught until **Ch 20**).
   - **Required Fix**: Explicitly scope Ch 12 Mas #6 (`Luogu P5827`) and Mas #7 (`Luogu P5828`) to the **single-$n$ $O(n \log n)$ Lagrange Inversion sub-task**, and assign **`QOJ 8528 — Youthful Paths`** in **Ch 20** for the all-$n$ $O(n \log^2 n)$ Kinoshita–Li composition upgrade.

4. **Chapter 24 (`q-Analogues, Gaussian Binomials & Dirichlet Series`) — Topic Incoherence & Non-FPS Intrusion**:
   - **What is wrong**: Proposal A merges $q$-Analogues (`CF 1603F`, `ABC 278 Ex`, `ARC 145 F`, `LOJ 6729`) with 3 pure multiplicative number theory problems (`Luogu P5325` [`R-52`], `Luogu P3768`, `ABC 288 Ex`), where `P5325` is a quarantined template and `P3768` uses Du's sieve + Möbius inversion with zero formal power series operations.
   - **Required Fix**: Dedicate **Chapter 24** purely to **$q$-Analogues, Gaussian Binomials, $q$-Pochhammer Euler Pentagonal / $\exp_q$ / $\ln_q$ & Cyclic Sieving** with a full 8-problem ladder (`CF 1603F`, `ABC 278 Ex`, `ARC 145 F`, `LOJ 6729`, `AtCoder ABC 238 Ex`, `Codeforces 1916F / Luogu P6118`, `Luogu P5401 / q-Pentagonal`, `AtCoder AGC 043 D / Cyclic Sieving`), and place the valid Lambert-series / GCD-convolution bridges (`AtCoder ABC 248 G`, `AtCoder ABC 230 G`, `AtCoder ABC 288 Ex`) in the Operator / Mobius-Sieve chapter where they belong.

---

### 2.2 Proposal B Ladder Smoothness & Forward-Reference Audit (Chapters 1–24)

Proposal B's chapter ladders have **8 severe forward-reference violations** where problems are assigned to early algebraic chapters before their required algorithmic or combinatorial engines are introduced:

| Chapter & Slot in Proposal B | Problem Assigned | Required Technique | Where Technique is Taught in Proposal B | Severity |
| :--- | :--- | :--- | :--- | :--- |
| **Ch 2 Adv #7** | `Codeforces 917D — Stranger Trees` | Prüfer / Cayley forest formula $n^{c-2}\prod s_i$ + Taylor shift $G(x-1)$ | **Ch 7** (Taylor Shift) & **Ch 11** (Matrix-Tree / Cayley) | **CRITICAL** (9 chapters early!) |
| **Ch 3 Adv #7** | `Luogu P4705 — 玩游戏` | Subproduct Tree $\prod(1-a_i x)$ + $\ln$ in $O(N \log^2 N)$ | **Ch 21** (Subproduct Tree / MPE) | **CRITICAL** (18 chapters early!) |
| **Ch 4 Int #5 & Ch 5 Int #6** | `Luogu P4491 — [HAOI2018] 染色` | Binomial Inversion + NTT Taylor Shift in $O(N \log N)$ | **Ch 7** (Binomial Inversion) & **Ch 9** (NTT) | **SEVERE** (5 chapters early!) |
| **Ch 4 Adv #6 & `CP1-6`** | `Codeforces 1336E2 — Chiori and Doll Picking` | MacWilliams Identity / FWHT on $\mathbb{F}_2^m$ linear codes | **Ch 24** (Set Power Series & XOR Duality) | **CRITICAL** (20 chapters early!) |
| **Ch 4 Adv #7** | `UOJ #310 — [UNR #2] 黎明前的巧克力` | Symbolic Method on $\mathbb{F}_2^m$ + FWHT | **Ch 24** (Set Power Series & XOR Duality) | **CRITICAL** (20 chapters early!) |
| **Ch 5 Adv #7** | `Codeforces 960G — Bandit Blues` | Divide-and-Conquer NTT $\prod_{i=0}^{n-2}(x+i)$ for First-Kind Stirling | **Ch 9** (Stirling Numbers) & **Ch 20** (D&C NTT) | **SEVERE** (15 chapters early!) |
| **Ch 15 Int #5** | `AtCoder ABC 253 Ex — We Love Forest` | Set Power Series $\exp$ in $O(n^2 2^n)$ | **Ch 24** (Set Power Series) | **CRITICAL** (9 chapters early!) |
| **`CP1-2`** | `AtCoder ABC 269 Ex — Antichain` | HLD Centroid-Balanced D&C NTT on Trees | **Ch 22** (Tree FPS) | **CRITICAL** (18 chapters early!) |

---

### 2.3 Proposal C Ladder Smoothness & Structural Compression Audit (Chapters 1–20)

Proposal C deserves high praise for its **Prerequisite Audit Table (`F-01`–`F-16`)**: every one of the 160 primary ladder slots in Proposal C is strictly prerequisite-safe, and every problem has a well-calibrated 4-tier rating (`2 SS / 2 Int / 2 Adv / 2 Mas` per chapter) with `Hint 1 (Diagnostic)`, `Hint 2 (Setup)`, and `Hint 3 (Bottleneck)`.

However, Proposal C's decision to compress the textbook from **24 chapters down to 20 chapters** (`160` primary ladder slots instead of `192`) creates **4 structural bottlenecks** where major topics are forced to share a single 8-problem ladder:

1. **Bottleneck 1 — Proposal C Chapter 20 (`q-Series, Set Power Series & Algebraic Extensions`)**:
   - **What happens**: Proposal C crams **$q$-Analogues / Gaussian Binomials** (`Slots 20-1, 20-3, 20-5, 20-6`: `CF 1603F`, `ABC 278 Ex`, `ARC 145 F`, `LOJ 6729`) and **Set Power Series / MacWilliams XOR Duality** (`Slots 20-2, 20-4, 20-7, 20-8`: `LOJ 154`, `ABC 253 Ex`, `Luogu P5406`, `CF 1336E2`) into a single 8-problem ladder.
   - **Why this hurts pedagogy**: $q$-Calculus (non-commutative/Eulerian $\exp_q$, Rothe's theorem, $q$-Lucas, $q$-Vandermonde) and Set Power Series ($K[x_1,\dots,x_n]/(x_i^2)$ ranked subset convolution, $O(n^2 2^n)$ point-wise ODEs, MacWilliams XOR duality) are two completely independent flagship extensions. Sharing an 8-problem ladder gives each topic only **1 Stepping Stone, 1 Intermediate, 1 Advanced, and 1 Mastery problem**, while dropping `ABC 213 G`, `UOJ 310`, `ABC 306 Ex`, and `UOJ 94` into the unguided Archive!
   - **Fix**: Split Proposal C's Ch 20 into **two dedicated 8-problem chapters** (as Proposal A does in Ch 23 and Ch 24).

2. **Bottleneck 2 — Proposal C Chapter 18 (`Transposition Principle, Multipoint Evaluation & FPS Composition`)**:
   - **What happens**: Proposal C packs **7 major $O(N \log^2 N)$ algorithms** into a single 8-problem ladder: (1) Subproduct Tree Multipoint Evaluation, (2) Fast Polynomial Interpolation, (3) Transposition Principle & `mulT`, (4) Shift of Sampling Points (`eval` on $c, c+1, \dots$), (5) $O(\sqrt{P}\log P)$ Factorial, (6) Kinoshita–Li $O(N \log^2 N)$ FPS Composition & Compositional Inverse, and (7) Power Projection.
   - **Why this hurts pedagogy**: Each of these algorithms (`Subproduct Tree MPE + Interpolation + Sampling Shift + Factorial` vs `Transposition Principle + Power Projection + Kinoshita–Li Composition/Reversion`) needs its own Stepping Stone and Intermediate scaffolding. In Proposal C Ch 18, `Shift of Sampling Points` gets 0 dedicated problems (`Luogu P5668` and `CF 995F` are dropped), and `Interpolation` gets 0 problems (`ARC 033 D` and `Luogu P7116` are dropped).
   - **Fix**: Split Proposal C's Ch 18 into **two dedicated 8-problem chapters**:
     - **Ch 20: Subproduct Trees, Multipoint Evaluation, Fast Interpolation & Shift of Sampling Points** (8 problems)
     - **Ch 21: The Transposition Principle (`mulT`), Power Projection & Kinoshita–Li Composition/Reversion** (8 problems)

3. **Bottleneck 3 — Proposal C Chapter 6 (`Inclusion-Exclusion, Connected Components & Cluster Method`)**:
   - **What happens**: Proposal C merges the **Goulden–Jackson Cluster Method** into Connected-Component Inclusion-Exclusion, leaving Cluster Method with only **1 problem** in Ch 6 (`CF Gym 102978H — Harsh Comments` in Slot `6-7`, plus `AGC 058 D` later in Slot `16-5`).
   - **Why this hurts pedagogy**: The Goulden–Jackson Cluster Method (forbidden-substring overlap matrices, Aho–Corasick system inversion, multivariate marked bad-adjacent-pair EGFs) is one of the highest-yield ICPC string-combinatorics tools. Proposal A's dedicated **Ch 08 (7–8 problems: `yukicoder 1810`, `ABC 266 G`, `CF Gym 102978H`, `Luogu P5339`, `Luogu P3311`, `CF Gym 102331J`, `AGC 058 D`)** gives students a complete progression from single-pattern overlap polynomials to Aho–Corasick matrix systems and Euler-brick adjacent-pair clusters.
   - **Fix**: Restore a **dedicated 8-problem chapter for the Goulden–Jackson Cluster Method & Forbidden-Pattern Counting**.

4. **Bottleneck 4 — Proposal C Chapter 15 (`Cacti, Block-Cut Trees & 2-Connected Graphs`)**:
   - **What happens**: Proposal C merges **Cacti & Block-Cut Trees** (`P5434`, `P6598`, `P6597`, `P5827`) with **DAGs, Tournaments & Bipartite Graphs** (`ABC 306 Ex`, `Luogu P5296`, `Luogu P6295`, `CF 913F`) into a single 8-problem ladder.
   - **Why this hurts pedagogy**: Block-Cut Tree / Dissymmetry Theorem / Cycle-pointing species equations (`Cacti`, `Alkanes`, `Alkenes`, `Biconnected`, `2-Edge-Connected`) and Edge-Weight Factorization / Functional Digraphs / Eulerian / Bipartite / DAG Inclusion-Exclusion (`Luogu P6295`, `Luogu P7364`, `CF 913F`, `ABC 236 Ex`, `Luogu P5296`, `CF 917D`) are distinct families with 16+ rich problems in the corpus.
   - **Fix**: Keep Proposal A's clean 2-chapter split: **Cacti, Block-Cut Trees & Dissymmetry Theorem** (8 problems) and **Functional Digraphs, DAGs, Tournaments, Eulerian & Bipartite Graphs** (8 problems).

---

## Dimension 3: Under-Served Topic Rescue Audit (All 12 Required Topic Clusters)

In `PROBLEM_CURATION.md`, several critical advanced topics were starved inside massive 30-problem wave buckets. Here is the exact head-to-head comparison of how Proposals A, B, and C rescue all 12 under-served topic clusters:

| # | Under-Served Topic Cluster | Baseline (`PROBLEM_CURATION.md`) | Proposal A (24 Ch) | Proposal B (24 Ch) | Proposal C (20 Ch) | Critic 3 Synthesis Prescription |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Tree FPS (HLD + Top Trees / Static Rake-Compress)** | Buried in Wave 2B (3 probs) | **Ch 22 (8 probs)**: `ABC 269 Ex`, `ABC 355 G`, `P7279`, `P4719` (template), `P3781`, `CF 438E`, `P5327`, `CF 917D` | **Ch 22 (8 probs)**: `ABC 269 Ex`, `ABC 355 G`, `P4719`, `P3781`, `ABC 248 G`, `CF 917D`, `P5327`, `QOJ 8528` | **Ch 19 (8 probs)**: `P4719`, `ABC 269 Ex`, `ABC 355 G`, `P7279`, `P3781`, `P5327`, `P4381`, `CF 438E` | **Dedicated 8-Problem Chapter (Ch 22)**: Replace `P4719` (template footnote) and `CF 438E` (already in Newton Iteration) with **`AtCoder ABC 220 H`** and **`Codeforces 917D`**, keeping `ABC 269 Ex`, `ABC 355 G`, `P7279`, `P3781`, `P5327`, `P4381`. |
| **2** | **Transposition Principle & `mulT`** | Buried in Wave 2B (2 probs) | **Ch 20 (5 probs + 3 comp)**: `P4705`, `P5488`, `P5298`, `CF 1770G`, `P5809` | **Ch 21 (shared with MPE)**: `P5050` (`R-26`), `P5158` (`R-27`), `P4705`, `P5282`, `CF 1770G`, `P5667` (`R-30`) | **Ch 18 (4 probs + 4 comp)**: `P4705`, `CF 1770G`, `P6292`, `P5809` | **Split into Ch 20 (MPE/Interp/Sampling Shift) & Ch 21 (`mulT` + Composition)**: Gives `mulT` + Power Projection + Composition a dedicated 8-problem ladder without templates. |
| **3** | **FPS Composition $F(G(x))$ & Reversion $G^{\langle -1 \rangle}(x)$** | Buried in Wave 2B (2 probs) | **Ch 20 (3 probs)**: `ABC 387 G`, `ABC 260 Ex`, `QOJ 8528` | **Ch 23 (8 probs, 3 templates)**: `P5373` (`R-33`), `P5809` (`R-32`), `ABC 387 G`, `ABC 260 Ex`, `P5827`, `P4747`, `QOJ 8528` | **Ch 18 (4 probs)**: `ABC 387 G`, `P5809`, `P5827` (dup), `QOJ 8528` (note) | **Ch 21 (8 probs combined with `mulT` & Power Projection)**: `P5809` (non-template version `ABC 387 G`, `ABC 260 Ex`, `Luogu P4747`, `Luogu P5828`, `QOJ 8528`, `CF 1770G`, `Luogu P5488`, `Luogu P6292`). |
| **4** | **Chirp Z-Transform & Shift of Sampling Points** | Split across Waves 1C & 2B (2 probs) | **Ch 21 (8 probs)**: `ARC 033 D`, `CF 451E` (dup), `P3321`, `CF 995F`, `P7116`, `CF 901E`, `P5668`, `P5282` | Split: **Ch 8** (CZT: `P5293`, `CF 901E`, `P6800` `R-31`) & **Ch 21** (Shift: `P5282`, `P5667` `R-30`) | Split: **Ch 5** (CZT: `P5293`, `CF 901E`) & **Ch 18** (`P5282` only; drops `CF 995F`, `ARC 033 D`, `P5668`, `P7116`) | **Two-Stage Coverage**: Put **Roots of Unity & CZT** in **Ch 05 (Part I)** so quadratic exponents $2^{\binom{n}{2}}$ are available early, AND give **MPE, Fast Interpolation, Sampling Shift & $O(\sqrt{P}\log P)$ Factorial** a dedicated **Ch 20 (8 probs)**: `CF 995F`, `ARC 033 D`, `CF 622F`, `Luogu P4705`, `Luogu P5298`, `Luogu P7116`, `Luogu P5668`, `Luogu P5282`. |
| **5** | **$q$-Analogues & Gaussian Binomials** | Buried in Wave 3B (4 probs) | **Ch 24 (4 $q$-probs + 3 Dirichlet)**: `CF 1603F`, `ABC 278 Ex`, `ARC 145 F`, `LOJ 6729` | **Ch 24 (2 $q$-probs only!)**: `CF 1603F`, `ABC 278 Ex / ARC 145 F` | **Ch 20 (4 $q$-probs + 4 SPS)**: `CF 1603F`, `ABC 278 Ex`, `ARC 145 F`, `LOJ 6729` | **Dedicated 8-Problem Chapter (Ch 24)**: `CF 1603F`, `AtCoder ABC 238 Ex`, `ABC 278 Ex`, `ARC 145 F`, `LOJ 6729`, `CF 1916F / Luogu P6118`, `Luogu P5401 (q-Pentagonal / Inv)`, `AtCoder AGC 043 D`. |
| **6** | **Set Power Series ($K[x_1,\dots,x_n]/(x_i^2)$) & XOR Duality** | Buried in Wave 3B (5 probs) | **Ch 23 (8 probs)**: `ABC 213 G`, `ABC 253 Ex`, `LOJ 154`, `UOJ 310`, `CF 1336E2`, `ABC 306 Ex`, `P5406`, `UOJ 94` | **Ch 24 (3 SPS probs)**: `LOJ 154`, `P6570`, `CF 1336E2`, `UOJ 310` | **Ch 20 (4 SPS probs)**: `LOJ 154`, `ABC 253 Ex`, `P5406`, `CF 1336E2` | **Adopt Proposal A's Dedicated 8-Problem Chapter (Ch 23)**: `ABC 213 G`, `Luogu P6570`, `LOJ 154`, `ABC 253 Ex`, `UOJ 310`, `CF 1336E2`, `Luogu P5406`, `UOJ 94`. |
| **7** | **Goulden–Jackson Cluster Method** | Buried in Wave 1D (3 probs) | **Ch 08 (7 probs)**: `yukicoder 1810`, `ABC 266 G`, `CF Gym 102978H`, `P5339`, `P3311`, `CF Gym 102331J`, `AGC 058 D` | **Ch 7 (2 probs)**: `P5339`, `CF Gym 102978H / AGC 058 D` | **Ch 6 (1 prob) + Ch 16 (1 prob)**: `CF Gym 102978H` (`6-7`), `AGC 058 D` (`16-5`) | **Adopt Proposal A's Dedicated 8-Problem Chapter (Ch 08)**: `yukicoder 1810 / CSES 1112`, `Luogu P3311`, `ABC 266 G`, `Luogu P5339`, `CF Gym 102978H`, `Luogu P4052`, `CF Gym 102331J`, `AGC 058 D`. |
| **8** | **Probability Generating Functions (PGFs) & Martingales** | Wave 1D (8 probs) | **Ch 14 (8 probs)**: `ABC 295 G` (`fps_24_o`), `CF 453A`, `ABC 326 E`, `P4548`, `P3706`, `UOJ 390`, `ARC 114 E`, `CF 1349D` | **Ch 10 (10 probs)**: `fps_24_o`, `CF 1278F`, `CF 891E`, `ABC 280 F`, `P4548`, `P3706`, `UOJ 390`, `CF 1349D`, `ARC 114 E`, `CF 1479D` | **Ch 8 (8 probs)**: `fps_24_o`, `ABC 314 Ex`, `ARC 114 E`, `P4548`, `P3706`, `CF 1349D`, `CF 850F`, `AGC 038 E` | **Adopt Proposal C's Ch 8 (8 probs)**: `fps_24_o`, `ABC 314 Ex`, `ARC 114 E`, `P4548`, `P3706`, `CF 1349D`, `CF 850F`, `AGC 038 E` (moving `UOJ 390` and `CF 1278F` to Blind Checkpoint II). |
| **9** | **Cacti, Block-Cut Trees & 2-Connected Graphs** | Wave 2C (8 probs) | **Ch 12 (7 probs Cacti) + Ch 13 (7 probs DAGs/Bipartite)** | **Ch 15 (9 probs merged)** | **Ch 15 (8 probs merged)** | **Adopt Proposal A's Two-Chapter Split (Ch 14 & Ch 15, 8 probs each)**: Ch 14 for Cacti, Block-Cut Trees & Dissymmetry (`P5434`, `P4381`, `LOJ 6538`, `P6598`, `P6597`, `LOJ 6509`, `P5827` single-$n$, `P5828` single-$n$); Ch 15 for Functional Digraphs, DAGs, Tournaments & Bipartite (`ABC 236 Ex`, `ABC 306 Ex`, `P5296`, `P6295`, `P7364`, `CF 913F`, `CF 156D`, `CF 623E`). |
| **10** | **D-Finite / Holonomic ODEs & Sparse FPS** | Split across Waves 1B & 3A | **Ch 18 (8 probs D-Finite) + Ch 19 (7 probs `EI 科技`)** | **Ch 4 (8 probs Sparse ODE) + Ch 19 (8 probs D-Finite)** | **Ch 10 (8 probs merged)** | **Dedicated Ch 11 (8 probs): Sparse FPS, P-Recursive ODEs & Creative Telescoping (`EI 科技`)**: `CF 1096G`, `fps_24_m`, `P4451`, `ABC 296 Ex`, `ABC 222 H`, `CF 755G`, `UOJ 50`, `CF 1349F2`. |
| **11** | **Rational Diagonals & Furstenberg's Theorem** | Wave 3A (6 probs) | **Ch 16 (8 probs)**: `ABC 240 G`, `CF 1264D2`, `yukicoder 1080`, `P3266`, `P4456`, `CF 1204E`, `ARC 116 E`, `ABC 296 Ex` | **Ch 17 (9 probs)**: `fps_24_q`, `P3266`, `ABC 240 G`, `P4456`, `P5434`, `CF 1264D2`, `yukicoder 1080`, `AGC 058 D`, `ABC 296 Ex` | **Ch 16 (8 probs)**: `fps_24_q`, `ABC 240 G`, `yukicoder 1080`, `P4456`, `AGC 058 D`, `P4725`, `CF 1264D2`, `ABC 296 Ex` | **Dedicated 8-Problem Chapter (Ch 18)**: `fps_24_q`, `ABC 240 G`, `CF 1264D2`, `yukicoder 1080`, `Luogu P4456`, `Luogu P5339 / Motzkin Diagonal`, `AtCoder ARC 116 E`, `Luogu P3702 / Bostan-Mori`. |
| **12** | **Kernel Method, Reflection & 2D Lattice Walks** | Wave 3A (5 probs) | **Ch 15 (8 probs 1D Kernel) + Ch 17 (8 probs 2D Walks & Good–Lagrange)** | **Ch 16 (9 probs)**: `ABC 205 E` (`R-63`), `CF 1204E`, `P3266`, `ABC 222 H`, `P4456`, `CF 755G`, `ABC 253 G`, `CF 1349F2`, `ABC 303 Ex` | **Ch 12 (8 probs)**: `CF 1204E`, `fps_24_k`, `P3266`, `ABC 240 G`, `P6672`, `CF 838D`, `P4340`, `ABC 253 G` | **Dedicated 8-Problem Chapter (Ch 16)**: `CF 838D`, `fps_24_k`, `CF 1204E`, `Luogu P3266`, `Luogu P6672`, `AtCoder ABC 253 G`, `Luogu P4340`, `Codeforces 1943D2`. |

---

## Dimension 4: Blind Topic-Group Checkpoints Audit

A Blind Topic-Group Checkpoint must satisfy four strict pedagogical criteria:
1. **Zero Overlap with Chapter Ladders**: Every checkpoint problem must be unseen in the chapter ladders.
2. **Zero Forward-Reference Leaks**: A checkpoint placed at the end of Part $K$ may only require techniques from Parts $1 \dots K$.
3. **Cumulative Synthesis**: Checkpoints II–VI must include problems that combine earlier parts with the current part.
4. **Spoiler-Free Layout**: The problem statement and diagnostic self-test questions must be physically separated from the hidden routing table (`Target Chapter` + `Core Technique` + `Bottleneck`).

### Head-to-Head Checkpoint Audit Table
| Criterion | Proposal A Checkpoints (`I`–`VI`, 48 probs) | Proposal B Checkpoints (`CP1`–`CP6`, 36 probs) | Proposal C Checkpoints (`CP1`–`CP6`, 40 probs) |
| :--- | :--- | :--- | :--- |
| **1. Disjointness from Chapter Ladders** | **90% Disjoint** (`43/48` unique; 5 overlaps/bugs: `CF 755G`, `CF 932E`, `CF 1515E`, `ABC 222 H`, `UOJ 450`, `UOJ 310`, `P5325`, plus `ABC 260 Ex` duplicated in `II-7` & `V-7`) | **0% Disjoint** (`0/36` unique — **every single problem in `CP1`–`CP6` is a verbatim duplicate of a Proposal B chapter ladder slot**) | **35% Disjoint** (`14/40` unique in `CP1`–`CP2`, but **`26/26` (100%) of `CP3`–`CP6` are verbatim duplicates of Proposal C's Ch 3–20 ladders**) |
| **2. Zero Quarantined Templates (`R-01`–`R-67`)** | **1 Leak**: `VI-1` is `Luogu P5325` (`R-52`, Min_25 Sieve template) | **3 Leaks**: `CP3-6` (`P5900` `R-36`), `CP5-1` (`ABC 205 E` `R-63`), `CP5-6` (`P4721` `R-45`) | **0 Leaks** (100% template-free) |
| **3. Prerequisite Safety (Zero Forward References)** | **1 Leak**: `V-6` (`UOJ 310`) placed after Part V (Ch 20) before FWT/SPS is taught in Ch 23; `III-8` (`CF 809E`) is non-FPS virtual tree | **2 Severe Leaks**: `CP1-2` (`ABC 269 Ex`, requires Ch 22 Tree FPS) and `CP1-6` (`CF 1336E2`, requires Ch 24 MacWilliams XOR Duality) placed after Part I (Ch 4)! | **0 Leaks** (Explicitly verified in `F-15` and `F-16`) |
| **4. Spoiler Protection & Diagnostic Pedagogy** | Uses collapsible `<details><summary> Answer Key` blocks (good), but the visible table only lists the problem title/link without a mathematical restatement or diagnostic prompt. | **Zero Spoiler Protection**: Prints the exact `Hidden Diagnostic & Target Chapter` inline in Column 4 of the visible problem table! | **Gold Standard Format**: Each checkpoint is split into `.1 Blind Problem Statements` (giving a neutral `Mathematical Statement` + spoiler-free `Hint 1 Recognition Rubric`) and `.2 Hidden Answer Key & Routing Table` (`Hint 2` + `Hint 3`). |

### Critic 3 Checkpoint Prescription
Adopt **Proposal C's two-stage `.1 Blind Problem Statements (with Hint 1 Recognition Rubric)` + `.2 Hidden Answer Key (with Hint 2 & Hint 3)` format**, wrap `.2` inside Proposal A's collapsible `<details>` block, and populate all **48 Checkpoint Slots (6 Parts $\times$ 8 Problems)** exclusively from the non-ladder problems in the 254-problem corpus so that **Ladder-to-Checkpoint overlap is strictly 0%**.

---

## Dimension 5: Actionable Master Problem Allocation Matrix (Unified 24-Chapter Architecture)

To resolve every single duplication, template leak, forward-reference trap, and under-served topic bottleneck identified across Proposals A, B, and C, here is the complete, verified **24-Chapter Master Problem Allocation Matrix** accounting for **all 254 Unique Accepted Problems** and **all 67 Quarantined Templates (`R-01`–`R-67`)**:

### Corpus Accounting Summary
| Allocation Bucket | Exact Formula | Problem Count | Overlap with Other Buckets |
| :--- | :--- | :---: | :---: |
| **1. Primary Chapter Ladders** | 24 Chapters $\times$ 8 Problems (`2 SS / 2 Int / 2 Adv / 2 Mas`) | **192** | **0%** |
| **2. Blind Topic-Group Checkpoints (`CP1`–`CP6`)** | 6 Parts $\times$ 8 Problems (Spoiler-Free Recognition Rubrics) | **48** | **0%** |
| **3. Annotated Multi-Perspective Synthesis Archive** | Cross-topic synthesis & alternate-proof problems | **14** | **0%** |
| **Total Accepted Non-Template Corpus** | $192 + 48 + 14$ | **254** | **Strictly 1-to-1 (`254/254`)** |
| **4. Implementation Verification Footnotes (`R-01`–`R-67`)** | 1-line unit-test footnotes at the top of each chapter | **67** | **0% in Ladders/Checkpoints** |
| **Grand Total Catalogued Problems** | $254 + 67$ | **321** | **100% Accounted For** |

---

### Part I: The Algebraic Engine & Operator Calculus of $K[[x]]$ (Chapters 1–5 + Blind Checkpoint I)

#### Chapter 01: The Formal Power Series Ring $K[[x]]$, Valuation Topology & Rational OGFs
*Implementation Verification Footnotes*: `R-01` (`fps_24_a`), `R-02` (`fps_24_b`), `R-03` (`fps_24_c`), `R-04` (`fps_24_d`), `R-11` (`LC Inv`), `R-42` (`Luogu P4238`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `01-1` | **SS 1** | **Library Checker — `fps_24_e` (Coloring Balls)** | Bijection between constrained ball coloring and rational OGF coefficient extraction |
| `01-2` | **SS 2** | **AtCoder ABC 279 Ex — Sum of Prod of Min** | Eliminating $\min(A_i, B_i)$ via Vandermonde / rational product identity |
| `01-3` | **Int 1** | **Luogu P2000 — 拯救世界** | Infinite product cancellation into $1/(1-x)^5$ + multiprecision division |
| `01-4` | **Int 2** | **Codeforces 451E — Devu and Flowers** | Bounded stars-and-bars $\prod (1-x^{f_i+1})/(1-x)$ with $2^n$ numerator expansion |
| `01-5` | **Adv 1** | **AtCoder ARC 028 D — 注文の多い高橋君** | Prefix-Query Optimization: $O(n^2)$ exact polynomial division $P(x)/(1-x^{a_i+1})$ |
| `01-6` | **Adv 2** | **Luogu P3702 — [SDOI2017] 序列计数** | Complementary counting via prime-sieve OGF mod $x^p - 1$ |
| `01-7` | **Mas 1** | **AtCoder AGC 001 E — BBQ Hard** | 2D offset Vandermonde convolution $\sum \binom{A_i+B_i+A_j+B_j}{A_i+A_j}$ via grid shift |
| `01-8` | **Mas 2** | **AtCoder ABC 230 G — GCD Permutation** | Möbius inversion composed with rational OGF divisor-pair extraction |

#### Chapter 02: Partition Theory, Ferrers Diagrams, Euler's Pentagonal Theorem & Logarithmic Sums
*Implementation Verification Footnotes*: `R-48` (`Luogu P6189`), `R-49` (`LC Partition`), `R-50` (`fps_24_h`), `R-51` (`fps_24_i`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `02-1` | **SS 1** | **CSES 2413 — Counting Towers** | Coupled 2-state transfer OGF reduced to a single rational denominator |
| `02-2` | **SS 2** | **AtCoder ABC 221 H — Count Multiset** | Ferrers conjugate + Durfee/first-column recurrence in $O(N^2)$ |
| `02-3` | **Int 1** | **Luogu P4389 — 付公主的背包** | Harmonic logarithmic sum $\ln \prod (1-x^{v_i})^{-1}$ + $\exp$ in $O(M \log M)$ |
| `02-4` | **Int 2** | **Luogu P5900 — 无标号有根树计数 (Harmonic Euler Transform Formulation)** | Euler Transform $\exp(\sum_{k \ge 1} T(x^k)/k)$ via harmonic sieve (Paired with `AtCoder ABC 288 Ex`) |
| `02-5` | **Adv 1** | **Luogu P3784 — [SDOI2017] 遗忘的集合** | Inverse Euler Transform via $\ln$ and Möbius inversion on harmonic coefficients |
| `02-6` | **Adv 2** | **AtCoder ARC 141 C — Bracket and Permutation** | Partition/Dyck structural bijection with OGF uniqueness verification |
| `02-7` | **Mas 1** | **AtCoder AGC 054 E — ZigZag Break** | Endpoint-conditioned finite-difference OGF telescoping |
| `02-8` | **Mas 2** | **Codeforces 1810G — The Maximum Prefix** | Backward OGF state reduction for prefix-maximum transitions |

#### Chapter 03: Labeled Structures, Exponential Generating Functions (EGFs) & The Symbolic Method ($\text{SET}, \text{CYC}, \text{SEQ}$)
*Implementation Verification Footnotes*: `R-05` (`fps_24_f`), `R-06` (`fps_24_g`), `R-12` (`LC Exp`), `R-13` (`LC Log`), `R-35` (`Luogu P5268`), `R-43` (`Luogu P4725`), `R-44` (`Luogu P4726`), `R-47` (`Luogu P5850`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `03-1` | **SS 1** | **Library Checker — `fps_24_n` (Permutations with Cycle Constraints)** | Direct application of $\exp(\sum_{c \in S} x^c/c)$ for cycle-restricted permutations |
| `03-2` | **SS 2** | **Codeforces 1515E — Phoenix and Computers** | $\text{SEQ}$ composition of odd-step activation blocks $A(x) = \sum 2^{k-1} x^k/k!$ |
| `03-3` | **Int 1** | **Luogu P4841 — [集训队作业2013] 城市规划** | Labeled connected graphs via $C(x) = \ln G(x)$ on $2^{\binom{n}{2}}$ |
| `03-4` | **Int 2** | **AtCoder ABC 303 Ex — Constrained Tree Degree** | Prüfer sequence EGF $\prod (\sum_{d \in S} x^{d-1}/(d-1)!)$ |
| `03-5` | **Adv 1** | **Luogu P6597 — 烯烃计数** | Unrooted vs. rooted cycle-of-trees symbolic species decomposition |
| `03-6` | **Adv 2** | **AtCoder ARC 105 F — Lights Out on Connected Graph** | Simultaneous tracking of parity and connectedness via $\ln$ on weighted graph EGFs |
| `03-7` | **Mas 1** | **Codeforces 623E — Transforming Sequence** | Doubling EGF convolution $F_{a+b}(x) = F_a(x) F_b(2^a x)$ with MTT ($\bmod 10^9+7$) |
| `03-8` | **Mas 2** | **Luogu P5162 — WD与积木** | Weakly ordered block hierarchies via $1/(2 - \exp(x) - x)$ |

#### Chapter 04: Operator Calculus ($\vartheta = xD$, Shift $E^a$), Falling Factorials, Taylor Shift & Stirling Matrices
*Implementation Verification Footnotes*: `R-21` (`LC Taylor Shift`), `R-22` (`LC 1st Stirling`), `R-23` (`LC 2nd Stirling`), `R-24` (`LC 1st Fixed K`), `R-25` (`LC 2nd Fixed K`), `R-55`–`R-59` (`Luogu P5395`, `P5396`, `P5408`, `P5409`, `P5748`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `04-1` | **SS 1** | **Codeforces 932E — Team Work** | Degree-$k$ falling-factorial expansion $n^k = \sum \left\{ \begin{matrix} k \\ j \end{matrix} \right\} n^{\underline{j}}$ in $O(k^2)$ |
| `04-2` | **SS 2** | **Luogu P6667 — [清华集训2016] 如何优雅地求和** | Binomial-basis to Falling-Factorial EGF conversion $\hat{F}(x) e^{-x}$ in $O(m \log m)$ |
| `04-3` | **Int 1** | **Codeforces 891E — Lust** | Multiplicative decrement tracked via EGF $\prod (a_i - x)$ and falling-factorial weights |
| `04-4` | **Int 2** | **Codeforces 960G — Bandit Blues** | Left/right record decomposition into First-Kind Stirling $\left[ \begin{matrix} n-1 \\ A+B-2 \end{matrix} \right]$ via Taylor-shift doubling |
| `04-5` | **Adv 1** | **Luogu P4091 — [HEOI2016/TJOI2016] 求和** | Row-sum of Second-Kind Stirling numbers via NTT convolution |
| `04-6` | **Adv 2** | **AtCoder ABC 276 G — Count Sequences** | Modular step differences + falling-factorial operator extraction |
| `04-7` | **Mas 1** | **Codeforces 1278F — Cards** | Iterated $(\vartheta)^k$ operator on $(p e^x + 1 - p)^n$ |
| `04-8` | **Mas 2** | **AtCoder ARC 154 E — Reverse and Inversion** | Operator-eigenvalue diagonalization of random reversal transpositions |

#### Chapter 05: Multiplication Theorems, Roots of Unity Filters, Bluestein's Chirp Z-Transform & Cyclic Convolutions
*Implementation Verification Footnotes*: `R-07` (`LC Conv`), `R-08` (`LC Conv 10^9+7`), `R-09` (`LC Conv 2^64`), `R-10` (`LC Large Conv`), `R-31` (`Luogu P6800 CZT`), `R-53` (`Luogu P3803`), `R-54` (`Luogu P4245`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `05-1` | **SS 1** | **Codeforces 528D — Fuzzy Search** | Threshold indicator cross-correlation $A[i] B[i-j]$ via reversed polynomial product |
| `05-2` | **SS 2** | **Luogu P3321 — [SDOI2015] 序列统计** | Discrete logarithm $g^k \equiv x \pmod M$ turning multiplication mod $M$ into cyclic convolution mod $x^{M-1}-1$ |
| `05-3` | **Int 1** | **Luogu P5293 — [HNOI2019] 白兔之舞** | Root-of-unity filter $\frac{1}{k}\sum_{j=0}^{k-1} \omega_k^{-jr}(I + \omega_k^j A)^L$ + Bluestein's CZT identity $ij = \binom{i+j}{2}-\binom{i}{2}-\binom{j}{2}$ |
| `05-4` | **Int 2** | **Codeforces 901E — Cyclic Cipher** | Inverse Chirp Z-Transform + quadratic character phase recovery on cyclic convolutions |
| `05-5` | **Adv 1** | **Luogu P3746 — [六省联考2017] 组合数问题** | Matrix-or-polynomial multiplication $\bmod (x^k - 1)$ for residue-class binomial sums |
| `05-6` | **Adv 2** | **UOJ #450 — 【集训队作业2018】复读机** | Multivariate root-of-unity filter $\left(\frac{1}{d}\sum_{j=0}^{d-1} e^{\omega_d^j x}\right)^k$ expanded as $d^k$ exponential terms |
| `05-7` | **Mas 1** | **AtCoder ABC 290 Ex — Bow Meow Optimization** | Convexity-exploiting polynomial convolution for bipartite interleaved matching |
| `05-8` | **Mas 2** | **Codeforces 1054H — Epic Convolution** | 2D Chinese Remainder Theorem + Chirp Z-Transform on $x^{(i^2)} y^{(j^3)} \bmod (p-1)$ |

#### Blind Topic-Group Checkpoint I (After Part I: Chapters 1–5 — 8 Disjoint Problems)
1. **`CP1-1`**: **AtCoder ABC 221 G — Jumping Sequence** (45-degree rotation $(x+y, x-y)$ decoupling 2D steps into two 1D subset-sum OGFs $\to$ Ch 01)
2. **`CP1-2`**: **Luogu P3338 — [ZJOI2014] 力** (Difference-index cross-correlation $\sum q_j/(i-j)^2$ via reversed polynomial convolution $\to$ Ch 05)
3. **`CP1-3`**: **Luogu P4173 — 残缺的字符串** (Wildcard string matching via squared cubic difference $\sum (A_j - B_{i+j})^2 A_j B_{i+j}$ $\to$ Ch 05)
4. **`CP1-4`**: **Library Checker — `fps_24_j` (Jumping with Exclusion)** (Sparse forbidden-landing OGF inversion $\to$ Ch 01)
5. **`CP1-5`**: **AtCoder ABC 241 Ex — Card Deck Score** (Bounded geometric product expansion $\prod (1 - (a_i x)^{b_i+1}) / \prod (1 - a_i x)$ + partial fractions $\to$ Ch 01)
6. **`CP1-6`**: **Codeforces 156D — Clues** (Cayley/Prüfer forest component glueing $n^{k-2}\prod s_i$ via EGF $\to$ Ch 03)
7. **`CP1-7`**: **AtCoder ABC 288 Ex — A Nameless Counting Problem** (Multiset Lyndon / Euler transform composition on bounded XOR-sum sequences $\to$ Ch 02 / Ch 03)
8. **`CP1-8`**: **Codeforces 622F — The Sum of the $k$-th Powers** (Falling-factorial / operator evaluation of $\sum_{i=1}^n i^k$ in $O(k)$ $\to$ Ch 04)

---

### Part II: Sieve Methods, Cluster Algebras, Symmetries & Probabilistic GFs (Chapters 6–8 + Blind Checkpoint II)

#### Chapter 06: Binomial Inversion, Inclusion-Exclusion & Connected-Component Inversion
*Implementation Verification Footnotes*: `R-60` (`Luogu P4463`), `R-61` (`AtCoder ABC 242 Ex`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `06-1` | **SS 1** | **AtCoder ABC 172 E — NEQ** | Principle of Inclusion-Exclusion on matched positions with falling factorials |
| `06-2` | **SS 2** | **Luogu P4859 — 已经没有什么好害怕的了** | Sort + 2D knapsack DP for "at least $j$ wins" followed by Binomial Inversion |
| `06-3` | **Int 1** | **Luogu P4491 — [HAOI2018] 染色** | EGF for "at least $k$ colors appear $S$ times" + NTT Binomial Inversion in $O(N \log N)$ |
| `06-4` | **Int 2** | **AtCoder ABC 265 G — 012 Inversion** | Fenwick/Segment algebraic maintenance of inversion-counting polynomials |
| `06-5` | **Adv 1** | **Luogu P5400 — [CTS2019] 随机立方体** | Inclusion-Exclusion on $k$ mutually dependent local maxima in a 3D grid + linear-time inverse prefix products |
| `06-6` | **Adv 2** | **AtCoder ARC 118 E — Avoid Permutations** | Rook polynomial / obstacle-path DP combined with Inclusion-Exclusion |
| `06-7` | **Mas 1** | **Codeforces 1342E — Placing Rooks** | Surjective column/row partition counting via Stirling / Binomial Inversion |
| `06-8` | **Mas 2** | **AtCoder AGC 036 F — Square Constraints** | Annulus rook placement via sorted upper/lower bound Inclusion-Exclusion |

#### Chapter 07: The Goulden–Jackson Cluster Method, Forbidden Substrings & Autocorrelation Systems
*Implementation Verification Footnotes*: `R-62` (`CSES 1112 / Basic Automaton DP`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `07-1` | **SS 1** | **yukicoder 1810 — Forbidden Substring OGF** | Single-pattern autocorrelation polynomial $C(x)$ and rational OGF $1/((1-\Sigma x)C(x)+x^m)$ |
| `07-2` | **SS 2** | **Luogu P3311 — [SDOI2014] 数数** | Aho–Corasick automaton transfer matrix as a rational generating function denominator |
| `07-3` | **Int 1** | **AtCoder ABC 266 G — Yet Another RGB Sequence** | Marking bad adjacent `RG` clusters via bivariate Inclusion-Exclusion / substitution |
| `07-4` | **Int 2** | **Luogu P5339 — [TJOI2019] 唱、跳、rap和篮球** | Marking bad length-4 `cxk` clusters + Binomial Inversion + NTT EGF convolution |
| `07-5` | **Adv 1** | **Luogu P4052 — [JSOI2007] 文本生成器** | Multi-pattern Aho–Corasick complement counting via rational series |
| `07-6` | **Adv 2** | **Codeforces Gym 102978H — Harsh Comments** | Full Goulden–Jackson Cluster Method: pairwise overlap matrix $M(x)$ inversion for multi-pattern avoidance |
| `07-7` | **Mas 1** | **Codeforces Gym 102331J — Jiry Matchings** | Cluster-weight EGF expansion on trees with polynomial merge |
| `07-8` | **Mas 2** | **AtCoder AGC 058 D — Yet Another ABC String** | Cyclic-rotation bad-step cluster weights $\sum (-1)^{k-c} \binom{k-1}{c-1} x^k$ composed with trivariate multinomials |

#### Chapter 08: Polya Enumeration, Burnside's Lemma, Unlabeled Species & Probability Generating Functions (PGFs)
*Implementation Verification Footnotes*: `R-36` (`Luogu P5900 Bare`), `R-37` (`Luogu P4980 Polya Bare`), `R-46` (`Luogu P5277 Sqrt`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `08-1` | **SS 1** | **Library Checker — `fps_24_o` (Expected Stops / ABC 295 G)** | Fundamental identity $\mathbb{E}[T] = F'(1)$ and $\text{Var}(T) = F''(1) + F'(1) - (F'(1))^2$ |
| `08-2` | **SS 2** | **AtCoder ABC 314 Ex — Disk and Segments** | Stopping-time PGF manipulation under geometric trials |
| `08-3` | **Int 1** | **AtCoder ARC 114 E — Paper Cutting** | Linearity of expectation / PGF tail sum $\sum [x^k] P(T > k)$ on grid cuts |
| `08-4` | **Int 2** | **Luogu P4548 — [CTSC2006] 歌唱王国** | Optional Stopping Martingale + autocorrelation polynomial $F'(1) = \sum_{k \in \text{Borders}(S)} \Sigma^k$ |
| `08-5` | **Adv 1** | **Luogu P3706 — [SDOI2017] 硬币游戏** | $n \times n$ pairwise border correlation system $C_{i,j}(1)$ for first-hitting probabilities |
| `08-6` | **Adv 2** | **Luogu P4128 — [SHOI2006] 有色图 / Polya Graphs** | Cycle Index of the pair group $S_n^{(2)}$ on $\binom{n}{2}$ edges for unlabeled graphs |
| `08-7` | **Mas 1** | **Codeforces 1349D — Slime and Biscuits** | Potential function / PGF absorption time across symmetric token pools |
| `08-8` | **Mas 2** | **AtCoder AGC 038 E — Gachapon** | Coupon-collector multivariate PGF differentiation $\frac{\partial}{\partial x} \prod \sum_{c < B_i} \frac{(p_i x)^c}{c!}$ |

#### Blind Topic-Group Checkpoint II (After Part II: Chapters 6–8 — 8 Disjoint Problems)
1. **`CP2-1`**: **AtCoder ARC 136 F — Flip Cells** (Target-configuration hitting time via $F(x) = G(x) H(x)$ division $F'(1)/F(1) = G'(1)/G(1) - H'(1)/H(1)$ $\to$ Ch 08)
2. **`CP2-2`**: **UOJ #390 — 【UNR #3】百鸽笼** (First-to-fill bounded capacity PGF integration $\int_0^\infty e^{-t}\prod \sum_{c < a_i} \frac{(t/n)^c}{c!} dt$ $\to$ Ch 08)
3. **`CP2-3`**: **Codeforces 850F — Rainbow Balls** (Martingale potential / PGF absorption on color classes $\to$ Ch 08)
4. **`CP2-4`**: **AtCoder ABC 267 Ex — Odd Sum** (Bivariate parity filter $\frac{1}{2}(P(x, 1) - P(x, -1))$ via D&C product $\to$ Ch 05 / Ch 06)
5. **`CP2-5`**: **AtCoder ABC 280 F — Pay or Receive / Probabilistic Walk** (Connected-component potential & cycle consistency $\to$ Ch 06 / Ch 08)
6. **`CP2-6`**: **Codeforces 1479D — Odd Mineral Resource** (Randomized hashing / parity indicator polynomial on trees $\to$ Ch 05 / Ch 06)
7. **`CP2-7`**: **Luogu P4707 — 重返现世** ($k$-th Min-Max Exclusion $\min_k(S) = \sum_{T \subseteq S} (-1)^{\lvert T \rvert - k}\binom{\lvert T \rvert - 1}{k-1} \min(T)$ with bounded knapsack DP in $m = n-k \le 10$ $\to$ Ch 06 / Ch 08)
8. **`CP2-8`**: **AtCoder ARC 126 E — Infinite Operations** (Expected value operator linearity under sorted adjacent averaging $\to$ Ch 04 / Ch 08)

---

### Part III: Linear Recurrences, Differential Equations & Divide-and-Conquer Engines (Chapters 9–12 + Blind Checkpoint III)

#### Chapter 09: Rational Series, Berlekamp–Massey, Bostan–Mori $[x^N] P(x)/Q(x)$ & Linear Recurrences
*Implementation Verification Footnotes*: `R-19` (`LC Bostan-Mori`), `R-20` (`LC Berlekamp-Massey`), `R-39` (`Luogu P4723`), `R-40` (`Luogu P5487`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `09-1` | **SS 1** | **Library Checker — `fps_24_d` / `AtCoder ABC 300 Ex — Fibonacci`** | Direct Bostan–Mori even/odd denominator reduction $Q(x)Q(-x)$ up to $N = 10^{18}$ |
| `09-2` | **SS 2** | **Codeforces 506E — Mr. Kitayuta's Gift** | Automaton path compression into a rational OGF evaluated at large $N$ |
| `09-3` | **Int 1** | **AtCoder ABC 277 Ex — Constrained Sums** | Characteristic polynomial extraction for structured transition matrices |
| `09-4` | **Int 2** | **Luogu P5072 / P4128 — Bostan–Mori on Modular Recurrences** | High-degree linear recurrence accelerated from $O(k^3 \log N)$ to $O(k \log k \log N)$ |
| `09-5` | **Adv 1** | **AtCoder ABC 262 Ex — Max Limited Sequence** | Segment/interval DP compressed into a rational generating function |
| `09-6` | **Adv 2** | **Codeforces 1117F — Crisp String** | Bitmask inclusion-exclusion + Berlekamp–Massey / rational transition reduction |
| `09-7` | **Mas 1** | **Luogu P4723 (Non-Template Variant: `Codeforces 718C / Bostan-Mori Matrix Trace`)** | Using BM + Bostan–Mori to bypass $O(k^3)$ transition matrix construction |
| `09-8` | **Mas 2** | **UOJ #182 — a^-1 + b Problem** | Rational series representation of iterated modular inverses and prefix products |

#### Chapter 10: Newton Iteration on $K[[x]]$ & Online CDQ Divide-and-Conquer NTT
*Implementation Verification Footnotes*: `R-14` (`LC Sqrt`), `R-15` (`LC Pow`), `R-28` (`Luogu P5205`), `R-29` (`Luogu P5245`), `R-45` (`Luogu P4721`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `10-1` | **SS 1** | **Codeforces 438E — The Child and Binary Tree** | Quadratic tree equation $C(x) F(x)^2 - F(x) + 1 = 0$ solved via Newton $\sqrt{1-4C(x)}$ |
| `10-2` | **SS 2** | **Library Checker — `fps_24_l` (Tournament / Semi-Online Convolution)** | Semi-online CDQ NTT for $f_n = \sum_{i=1}^{n-1} f_i g_{n-i}$ |
| `10-3` | **Int 1** | **AtCoder ABC 213 Ex — Stroll** | $M$-node multigraph walk DP solved via CDQ NTT in $O(M K \log^2 K)$ |
| `10-4` | **Int 2** | **Codeforces 553E — Kyoya and Train** | Time-indexed expected shortest path with CDQ FFT on suffix transition probabilities |
| `10-5` | **Adv 1** | **yukicoder 963 — Complete Binary Tree** | Fully self-referential quadratic convolution $F_n = \sum F_i F_{n-1-i}$ via symmetric-split CDQ NTT |
| `10-6` | **Adv 2** | **Library Checker — `fps_24_p` (Relaxed Convolution)** | Online multiplication where both $F_n$ and $G_n$ arrive dynamically |
| `10-7` | **Mas 1** | **Luogu P5296 — [北京省选集训2019] 生成树计数** | Simultaneous Newton/CDQ operations on $k$-th power weight polynomials $\bmod x^{k+1}$ |
| `10-8` | **Mas 2** | **LOJ #6538 — 烷基计数 加强版 加强版** | Cubic tree equation $A(x) = 1 + \frac{x}{6}(A(x)^3 + 3A(x)A(x^2) + 2A(x^3))$ solved in $O(N \log N)$ via Newton's Method |

#### Chapter 11: Sparse FPS, P-Recursive Sequences, Holonomic ODEs & Creative Telescoping (`EI 科技`)
*Implementation Verification Footnotes*: `R-41` (`Luogu P7439`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `11-1` | **SS 1** | **Codeforces 1096G — Lucky Tickets** | $O(N \cdot \lvert P \rvert)$ logarithmic derivative $F' P = k P' F$ for sparse polynomial $P(x)^k$ |
| `11-2` | **SS 2** | **Library Checker — `fps_24_m` (Sparse Exp / Log / Pow)** | Extracting $O(N \cdot s)$ recurrences for $\exp(S(x))$, $\ln(1+S(x))$, and $(1+S(x))^\alpha$ |
| `11-3` | **Int 1** | **Luogu P4451 — [国家集训队] 整数的lqp拆分** | Converting functional equations on rational/Fibonacci OGFs into low-order recurrences |
| `11-4` | **Int 2** | **Codeforces 755G — PolandBall and Many Other Balls** | 3-term holonomic recurrence $(1+4x+x^2)F^2$ yielding an $O(K)$ P-recursive step for $[y^k] F(x, y)$ |
| `11-5` | **Adv 1** | **UOJ #50 — 【UR #3】链式反应** | Nonlinear 2nd-order autonomous ODE $F'' = \frac{1}{2} A(x) (F')^2 + 1$ solved via CDQ NTT |
| `11-6` | **Adv 2** | **AtCoder ABC 296 Ex — Unite** | Reducing a 2D algebraic/rational diagonal to a P-recursive ODE solved in $O(N)$ |
| `11-7` | **Mas 1** | **Luogu P4456 — [CQOI2018] 交错序列** | Creative telescoping / D-finite recurrence for bivariate binomial-weighted walks |
| `11-8` | **Mas 2** | **Codeforces 1349F2 — Slime and Sequences (Hard Version)** | `EI 科技`: Eliminating singular factor $(1-w)^{-n-2}$ in Eulerian bivariate extraction via formal differential equations in $O(n \log n)$ |

#### Chapter 12: Characteristic-$p$ Algebra, Lucas's Theorem, Matrix-Tree Determinants & Pfaffians over $K[x]$
*Implementation Verification Footnotes*: `R-38` (`Luogu P6178`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `12-1` | **SS 1** | **AtCoder ABC 258 G / Lucas Parity Walk** | Frobenius endomorphism $(1+x)^{p^k} \equiv 1 + x^{p^k} \pmod p$ for base-$p$ digit DP |
| `12-2` | **SS 2** | **Luogu P4336 — [SHOI2016] 黑暗前的幻想乡** | Matrix-Tree determinant evaluated at $(n-1)$ points followed by Lagrange interpolation (or $\bmod 2^n$ inclusion-exclusion) |
| `12-3` | **Int 1** | **Luogu P6624 — [省选联考 2020 A 卷] 作业题** | Euler totient $\sum_{d \mid g} \varphi(d)$ + Matrix-Tree Theorem over the ring $K[x]/(x^2)$ ($w_e \mapsto 1 + w_e x$) |
| `12-4` | **Int 2** | **AtCoder ABC 336 G — 16 Integers** | Directed BEST Theorem (Eulerian circuits $\times$ Directed Matrix-Tree arborescences) on De Bruijn graphs |
| `12-5` | **Adv 1** | **AtCoder AGC 051 D — C4** | Bidirected cycle decomposition + polynomial determinant / generating function extraction |
| `12-6` | **Adv 2** | **AtCoder ABC 323 G — Inversion of Tree** | Characteristic polynomial $\det(L_1 + x L_2)$ via reduction to Upper Hessenberg form in $O(n^3)$ |
| `12-7` | **Mas 1** | **Codeforces 1556G / Pfaffian Matching Polynomial** | Tutte matrix Pfaffian $\text{Pf}(A(x))$ for counting perfect matchings by edge-weight degree |
| `12-8` | **Mas 2** | **AtCoder AGC 043 D — Merge Triplets** | Block-cycle decomposition of merge-sort permutations solved in $O(N^2)$ |

#### Blind Topic-Group Checkpoint III (After Part III: Chapters 9–12 — 8 Disjoint Problems)
1. **`CP3-1`**: **AtCoder ABC 331 G — Collect Them All** (Coupon-collector harmonic EGF + CDQ NTT / inclusion-exclusion $\to$ Ch 06 / Ch 10)
2. **`CP3-2`**: **Luogu P3175 — [HAOI2015] 按位或** (Min-Max Exclusion on bitwise OR hitting time $\mathbb{E}[\max(S)] = \sum (-1)^{\lvert T \rvert - 1} / (1 - P(\text{disjoint from } T))$ $\to$ Ch 06 / Ch 08)
3. **`CP3-3`**: **AtCoder ARC 147 E — Examination** (Hall's Marriage Condition + greedy/polynomial feasibility reduction $\to$ Ch 01 / Ch 09)
4. **`CP3-4`**: **Codeforces 913F — Strongly Connected Tournaments** (Strongly connected tournament DP via $q$-binomial / CDQ probability splitting $\to$ Ch 10)
5. **`CP3-5`**: **AtCoder ABC 263 Ex — Intersection 2** (Geometric / algebraic sweeping combined with polynomial counting $\to$ Ch 05 / Ch 09)
6. **`CP3-6`**: **Luogu P4233 — 射命丸文的笔记** (Expected Hamiltonian cycles in random tournaments via EGF inverse of SCC decomposition $\to$ Ch 03 / Ch 10)
7. **`CP3-7`**: **AtCoder AGC 013 E — Placing Squares** (Combinatorial interpretation of $\prod L_i^2$ as placing 2 markers per block $\to$ $3 \times 3$ matrix / rational series $\to$ Ch 09)
8. **`CP3-8`**: **Codeforces 1608F — MEX Counting** (DP state space compression on prefix MEX transitions $\to$ Ch 04 / Ch 10)

---

### Part IV: Formal Laurent Series $K((x))$, Lagrange Inversion & Advanced Graph Species (Chapters 13–15 + Blind Checkpoint IV)

#### Chapter 13: Formal Laurent Series $K((x))$, Formal Residues, Lagrange–Bürmann Inversion & Raney's Lemma
*Implementation Verification Footnotes*: `R-64` (`Catalan / Dyck Basic`), `R-65` (`Prüfer Tree Basic`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `13-1` | **SS 1** | **Library Checker — `fps_24_r` (Lagrange Inversion Verification)** | Direct application of $[x^n] F(x) = \frac{1}{n}[w^{n-1}] \phi(w)^n$ |
| `13-2` | **SS 2** | **Library Checker — `fps_24_s` (Forest Degree Sequence)** | Multicomponent Lagrange / Raney's Lemma $[x^n] F(x)^k = \frac{k}{n}[w^{n-k}] \phi(w)^n$ |
| `13-3` | **Int 1** | **AtCoder ABC 222 H — Beautiful Binary Tree** | Bivariate tree equation reduced via Lagrange–Bürmann $[x^n] H(F(x)) = \frac{1}{n}[w^{n-1}] H'(w)\phi(w)^n$ to $O(n)$ sum |
| `13-4` | **Int 2** | **Luogu P6672 — [清华集训2016] 你的生命已如风中残烛** | Raney's Lemma cyclic shift bijection for $\sum (w_i - 1) = -1$ with non-negative prefix sums |
| `13-5` | **Adv 1** | **Codeforces 1251F — Red-White Fence** | Tree/polygon perimeter polynomial convolution + binomial power extraction |
| `13-6` | **Adv 2** | **AtCoder ARC 128 E —小球排列 / Raney Generalization** | Generalized Raney / ballot constraints with bounded multiplicity |
| `13-7` | **Mas 1** | **Luogu P7435 / Bivariate Good–Lagrange Tree Enumeration** | Two-variable Jacobian $\det(I - J_\phi)$ for alternating 2-colored trees |
| `13-8` | **Mas 2** | **Codeforces 1344E / Tree Heavy-Light Switching & LIF** | Combining structural tree decompositions with generating function degree bounds |

#### Chapter 14: Cacti, Block-Cut Trees, 2-Connected Graphs & The Dissymmetry Theorem
*Implementation Verification Footnotes*: `R-66` (`Prüfer Forest Basic`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `14-1` | **SS 1** | **Luogu P4381 — [IOI2008] Island (Unicyclic / Pseudoforest Structure)** | Fundamental $\text{CYC}(T(x))$ cycle-of-trees structural decomposition |
| `14-2` | **SS 2** | **Luogu P5434 — 有标号荒漠计数** | Rooted cactus equation $T(x) = x \exp\left(\sum_{k \ge 1} \frac{T(x)^k + T(x)^{k-1}}{2}\right) = x \exp\left(\frac{2T - T^2}{2(1-T)}\right)$ + $\exp$ for desert |
| `14-3` | **Int 1** | **Luogu P6598 — 烷烃计数** | Unlabeled carbon trees (degree $\le 4$) via Dissymmetry Theorem $A(x) = T(x) - \frac{1}{2}(T(x)^2 - T(x^2))$ |
| `14-4` | **Int 2** | **LOJ #6509 — 「雅礼集训 2018 Day7」烷基计数 加强版 加强版** | High-degree unlabeled tree species with Pólya cycle-index substitutions |
| `14-5` | **Adv 1** | **Luogu P5827 — 点双连通图计数 (Single-$n$ Lagrange Inversion)** | Block-Cut Tree relation $C'(x) = \exp(B'(x C'(x)))$ inverted for a single $n$ in $O(n \log n)$ via LIF |
| `14-6` | **Adv 2** | **Luogu P5828 — 边双连通图计数 (Single-$n$ Lagrange Inversion)** | Bridge-block tree relation $C(x) = B(x \exp(C(x)))$ inverted for a single $n$ in $O(n \log n)$ via LIF |
| `14-7` | **Mas 1** | **Codeforces 1707E / Unlabeled Cactus Enumeration** | Combining Pólya dihedral cycle index $D_k$ with Dissymmetry Theorem on block-cut trees |
| `14-8` | **Mas 2** | **UOJ #460 — Beautiful Cacti / Series-Parallel Graphs** | Coupled system of equations for series-parallel networks solved via multi-equation Newton iteration |

#### Chapter 15: Functional Digraphs, Labeled DAGs, Eulerian Graphs & Bipartite Graphs
*Implementation Verification Footnotes*: `R-67` (`Bipartite Basic`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `15-1` | **SS 1** | **AtCoder ABC 236 Ex — Distinct Multiples** | Connected-component partition IE $\prod (k-1)! (-1)^{k-1}$ via $\exp$ of signed cycle weights |
| `15-2` | **SS 2** | **AtCoder ABC 306 Ex — Balance Scale** | Layering weak orders / DAGs by source-layer Inclusion-Exclusion $(-1)^{\lvert S \rvert - 1}$ |
| `15-3` | **Int 1** | **Luogu P6295 — 有标号 DAG 计数** | Robinson–Stanley source-layer IE + CZT identity $2^{k(n-k)} = 2^{\binom{n}{2}-\binom{k}{2}-\binom{n-k}{2}}$ turning DAG DP into $1/\hat{F}(x)$ in $O(N \log N)$ |
| `15-4` | **Int 2** | **Luogu P7364 — 有标号二分图计数** | Bipartite 2-colored EGF squared via CZT weight factorization $\to$ $\sqrt{\cdot}$ + $\ln$ in $O(N \log N)$ |
| `15-5` | **Adv 1** | **Luogu P5298 — [PKUWC2018] Minimax** | Tree probability distribution merging via segment-tree / polynomial convolution |
| `15-6` | **Adv 2** | **AtCoder ABC 253 G / Labeled Eulerian Graphs** | Even-degree graph EGF $\frac{1}{2^n}\sum_{k=0}^n \binom{n}{k} 2^{\binom{k}{2}+\binom{n-k}{2}}$ + $\ln$ for connected Eulerian graphs |
| `15-7` | **Mas 1** | **AtCoder AGC 005 D — ~K Permutations** | Decomposition of $|p_i - i| \ne K$ into independent paths + rook polynomial EGF convolution |
| `15-8` | **Mas 2** | **Luogu P5401 — [CTS2019] 珍珠** | Parity of odd-multiplicity colors via $\left(\frac{e^x + e^{-x}}{2}\right)^k \left(\frac{e^x - e^{-x}}{2}\right)^{D-k}$ + NTT convolution |

#### Blind Topic-Group Checkpoint IV (After Part IV: Chapters 13–15 — 8 Disjoint Problems)
1. **`CP4-1`**: **AtCoder ABC 272 G — Yet Another Mod M** (Randomized majority / polynomial root-finding check $\to$ Ch 05 / Ch 12)
2. **`CP4-2`**: **Codeforces 1093G / Multidimensional Manhattan Convolution** (Sign-flip $2^k$ transformation on coordinate differences $\to$ Ch 05)
3. **`CP4-3`**: **AtCoder ARC 148 E — $\ge K$ Permutation** (Incremental two-pointer insertion product $\to$ Ch 03 / Ch 06)
4. **`CP4-4`**: **Luogu P3270 — [JLOI2016] 成绩比较** (Lagrange interpolation / Bernoulli power sum for $N \le 10^9$ combined with Binomial Inversion $\to$ Ch 04 / Ch 06)
5. **`CP4-5`**: **AtCoder AGC 019 F — Yes or No** (Random walk diagonal interception $\sum \binom{2i}{i}^2 / \binom{N+M}{N}$ $\to$ Ch 08 / Ch 13)
6. **`CP4-6`**: **Codeforces 1158F — Density of Subsequences** (Subsequence coupon-collector DP with $O(N^2/C + N 2^C)$ threshold splitting $\to$ Ch 08 / Ch 10)
7. **`CP4-7`**: **AtCoder ARC 153 D / Carry Digit Automaton** (Carry-propagation state compression over digits $\to$ Ch 09 / Ch 12)
8. **`CP4-8`**: **Luogu P4332 / Tree Functional Species** (Rooted functional digraphs $\text{SET}(\text{CYC}(T(x)))$ and Cayley variants $\to$ Ch 13 / Ch 14)

---

### Part V: Lattice Walks, Algebraic Curves, Diagonals & Fast $O(N \log^2 N)$ Polynomial Engines (Chapters 16–21 + Blind Checkpoint V)

#### Chapter 16: The Reflection Principle, Cycle Lemma & The Kernel Method for 1D Lattice Walks
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `16-1` | **SS 1** | **Codeforces 838D — Airplane Arrangements** | Circular extension ($n+1$ seats) + symmetry invariance giving $(n+1-m)(n+1)^{m-1}$ |
| `16-2` | **SS 2** | **Library Checker — `fps_24_k` (Bounded Walk Kernel)** | Solving $(1 - t(u + u^{-1})) F(t, u) = 1 - t u^{-1} F(t, 0)$ by substituting the small root $u_1(t)$ |
| `16-3` | **Int 1** | **Codeforces 1204E — Natasha, Sasha and the Prefix Sums** | Distribution of $\max_{k} S_k$ via André's reflection principle across $y = m$ |
| `16-4` | **Int 2** | **Luogu P3266 — [JLOI2015] 骗我呢** | Young tableau / non-Intersecting path reduction to alternating reflection across two parallel lines $y = x+1$ and $y = x - m - 2$ |
| `16-5` | **Adv 1** | **AtCoder ABC 205 E (Hard Multi-Barrier Variant / `AtCoder AGC 024 F`)** | Multi-barrier reflection + prefix-sum dominance |
| `16-6` | **Adv 2** | **Luogu P4340 — [SHOI2016] 随机游走** | Kernel Method for $F(t, u)$ evaluated at $u=1$ with boundary elimination via root substitution |
| `16-7` | **Mas 1** | **Codeforces 1943D2 — Counting Is Fun (Hard Version)** | Local smoothness constraint $a_i \le a_{i-1} + a_{i+1}$ reduced to dual-barrier reflection |
| `16-8` | **Mas 2** | **AtCoder ARC 157 F — XY Ladder / Kernel Walk** | Asymmetric step set $S(u) = P(u)/u^c$ requiring summation over $c$ small roots via symmetric polynomials |

#### Chapter 17: 2D Quarter-Plane Walks, The Obstinate Kernel Method & Bivariate Good–Lagrange
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `17-1` | **SS 1** | **AtCoder ABC 240 G — Teleporting Takahashi** | 3D $\to$ 1D + 2D decoupling; rotating 2D $(x \pm 1, y \pm 1)$ into $(u, v) = (x+y, x-y)$ |
| `17-2` | **SS 2** | **AtCoder ABC 259 Ex — Yet Another Path Counting** | Grid walk batching by color frequency threshold ($O(N^2)$ vs $O(c^2)$) |
| `17-3` | **Int 1** | **Codeforces 1427F / Quarter-Plane Tandem Walk** | Bijection between 2D quarter-plane walks with steps $(1,0), (-1,1), (0,-1)$ and pairs of non-intersecting Dyck paths |
| `17-4` | **Int 2** | **AtCoder AGC 030 F — Permutation and Minimum** | Paired-slot state matching with catalan/lattice boundary constraints |
| `17-5` | **Adv 1** | **AtCoder ARC 116 E — Spread of Information** | Tree/walk radius parameterization paired with generating function extraction |
| `17-6` | **Adv 2** | **Codeforces 1666K / Kreweras Walk Equivalence** | Applying the dihedral group of the curve $\Phi: x \mapsto \frac{1}{xy}, y \mapsto y$ to eliminate boundary terms $F(x, 0)$ and $F(0, y)$ |
| `17-7` | **Mas 1** | **AtCoder AGC 049 E — Increment Decrement** | Slope-trick convex cost dualized into lattice path enumeration |
| `17-8` | **Mas 2** | **UOJ #424 — 【集训队作业2018】count (Bounded Cartesian Tree / 2D Walk)** | Left-depth bounded Cartesian trees mapped to bounded Dyck paths + reflection / Bostan–Mori |

#### Chapter 18: Rational Diagonals $\text{Diag}(P/Q)$, Cauchy Residue Extraction & Furstenberg's Theorem
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `18-1` | **SS 1** | **Library Checker — `fps_24_q` (Bivariate Rational Diagonal)** | Extracting $[x^n y^n] \frac{1}{1 - ax - by - cxy} = [x^n] \frac{1}{\sqrt{(1-cx)^2 - 4abx}}$ |
| `18-2` | **SS 2** | **Codeforces 1264D2 — Beautiful Bracket Sequence (Hard Version)** | Vandermonde diagonal reduction of $\sum_k k \binom{A}{k} \binom{B}{C-k}$ to two closed-form binomials |
| `18-3` | **Int 1** | **yukicoder 1080 — +- Derived** | Complex diagonal substitution $(1+i)^n \pm (1-i)^n$ inside EGFs |
| `18-4` | **Int 2** | **AtCoder ABC 298 Ex / Delannoy & Motzkin Diagonals** | Using Cauchy's integral $[x^n y^n] F(x, y) = \frac{1}{2\pi i}\oint F(z/y, y) \frac{dy}{y}$ to sum residues over small poles $y_k(z)$ |
| `18-5` | **Adv 1** | **Codeforces 1799G — Count Voting** | Symmetric group / diagonal coefficient extraction for deg-constrained voting graphs |
| `18-6` | **Adv 2** | **AtCoder AGC 046 E / Algebraic Diagonal P-Recursion** | Converting $\sqrt{\Delta(x)}$ into a 3-term linear differential equation for $O(N)$ coefficient computation |
| `18-7` | **Mas 1** | **AtCoder AGC 060 D — Same Generating Function** | Structural bijections on bivariate Eulerian/inversion diagonals |
| `18-8` | **Mas 2** | **Codeforces 1842H / Furstenberg Diagonal modulo $p$** | Applying Furstenberg's theorem $[x^n y^n] \frac{f'(xy) P(x, y)}{y f(xy) - x}$ in characteristic $p$ |

#### Chapter 19: Cyclic Graphs, Transfer-Matrix Reduction & Non-Intersecting Lattice Paths (LGV Lemma)
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `19-1` | **SS 1** | **Library Checker — `fps_24_t` (LGV Basic / `CF 348D — Turtles`)** | $2 \times 2$ Lindström–Gessel–Viennot determinant $W(A_1 \to B_1)W(A_2 \to B_2) - W(A_1 \to B_2)W(A_2 \to B_1)$ |
| `19-2` | **SS 2** | **Luogu P6657 — 【模板】LGV 引理 (K-Path Grid Determinant)** | $K \times K$ determinant of binomial coefficients for non-intersecting grid paths |
| `19-3` | **Int 1** | **AtCoder ABC 216 H — Random Robots** | LGV Lemma where endpoints $B_j$ are unfixed (Vandermonde/DP fusion of determinant columns) |
| `19-4` | **Int 2** | **Luogu P7736 — [NOI2021] 路径交点** | Multiplicativity of $\det(M_1 M_2 \cdots M_{k-1})$ showing parity of path intersections across layered DAGs |
| `19-5` | **Adv 1** | **Codeforces 1672H / Semi-Standard Young Tableaux via LGV** | Hook-content / LGV translation of column-strict Young tableaux into binomial determinants |
| `19-6` | **Adv 2** | **AtCoder AGC 052 D / Transfer-Matrix Characteristic Polynomial** | Cayley–Hamilton reduction of $2^w \times 2^w$ profile transfer matrices |
| `19-7` | **Mas 1** | **UOJ #269 — 【清华集训2016】如何优雅地求和 (Bivariate LGV Variant / `Luogu P3733`)** | Combining LGV determinants with polynomial edge weights in $K[x]$ |
| `19-8` | **Mas 2** | **AtCoder AGC 061 E / Plane Partitions & MacMahon Box Formula** | 3D box partitions reduced to non-intersecting rhombus tilings via LGV determinant |

#### Chapter 20: Subproduct Trees, Multipoint Evaluation, Fast Interpolation & Shift of Sampling Points
*Implementation Verification Footnotes*: `R-26` (`Luogu P5050`), `R-27` (`Luogu P5158`), `R-30` (`Luogu P5667`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `20-1` | **SS 1** | **Codeforces 995F — Cowmpany Cowmpensation** | Degree-$n$ tree value DP evaluated at $x = 1, \dots, n+1$ and interpolated at $D \le 10^9$ in $O(n)$ |
| `20-2` | **SS 2** | **AtCoder ARC 033 D — 見たことのない多項式** | $O(N)$ consecutive-grid Lagrange interpolation $f(c) = \sum f(i) \frac{\text{pref}_{i-1}\text{suff}_{i+1}}{i!(n-i)!(-1)^{n-i}}$ |
| `20-3` | **Int 1** | **Luogu P4705 — 玩游戏** | Power sums $\sum a_i^k = [x^k] \left(n - x \frac{Q'(x)}{Q(x)}\right)$ where $Q(x) = \prod(1 - a_i x)$ via Subproduct Tree |
| `20-4` | **Int 2** | **Luogu P7116 — [NOIP2020] 微信步数** | Multidimensional grid walk lifetimes reduced to Bernoulli power-sum interpolation |
| `20-5` | **Adv 1** | **Luogu P5668 — [NOI2019] 斗主地** | Maintaining degree-2 expectation polynomials across riffle shuffles via Shift of Sampling Points |
| `20-6` | **Adv 2** | **Luogu P5437 — 【XR-2】缘分** | High-degree polynomial interpolation of edge-contribution sums |
| `20-7` | **Mas 1** | **Luogu P5282 — 【模板】快速阶乘算法 (Non-Trivial $O(\sqrt{P}\log P)$ Engine)** | Doubling block product $G_d(x) = \prod_{i=1}^d (x+i)$ via Shift of Sampling Points (`G_d(0), G_d(d), \dots`) |
| `20-8` | **Mas 2** | **Codeforces 1801G / Fast Multipoint Evaluation on Dynamic Trees** | Subproduct tree remainder descent $P(x) \bmod (x - x_i)$ coupled with string/tree queries |

#### Chapter 21: The Transposition Principle (`mulT`), Power Projection & Kinoshita–Li Composition/Reversion
*Implementation Verification Footnotes*: `R-16` (`LC Comp`), `R-17` (`LC Comp Inv`), `R-18` (`LC Multipoint`), `R-32` (`Luogu P5809`), `R-33` (`Luogu P5373`), `R-34` (`LC Comp Old`).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `21-1` | **SS 1** | **Luogu P5488 — 差分与前缀和** | Generalized $(1 \pm x)^k$ operators and transposed middle-product extraction |
| `21-2` | **SS 2** | **Codeforces 1770G — Koxia and Bracket** | D&C tree on $\prod (1 + w_i x)$ paired with top-down transposed middle product `mulT` |
| `21-3` | **Int 1** | **AtCoder ABC 387 G — Prime Circuit** | Composing cycle EGF $P(x) = \sum_{p \text{ prime}} x^p/(2p)$ with rooted tree $T(x) = x e^{T(x)}$ via $O(N \log^2 N)$ Kinoshita–Li composition |
| `21-4` | **Int 2** | **AtCoder ABC 260 Ex — Colorfulness** | Color-cluster reduction + $O(N \log^2 N)$ polynomial composition / multipoint evaluation |
| `21-5` | **Adv 1** | **Luogu P4747 — [CERC2017] Intrinsic Interval (Simple Permutations)** | Simple permutation functional equation $P(x) = (x + 2I + S) \circ P(x)$ solved via Newton / Compositional Inverse |
| `21-6` | **Adv 2** | **Luogu P6292 — 区间本质不同子串个数 / Transposed Automaton** | Transposing linear operators on suffix structures and polynomial weights |
| `21-7` | **Mas 1** | **Library Checker — `fps_24_u` (Power Projection $[x^n] \sum w_i G(x)^i$)** | Transposing Kinoshita–Li composition to compute $\langle w, G(x)^k \rangle$ for all $k \le n$ in $O(n \log^2 n)$ |
| `21-8` | **Mas 2** | **QOJ 8528 — Youthful Paths (All-$n$ Biconnected Graph Enumeration)** | Full all-$n$ Block-Cut Tree inversion $C'(x) = \exp(B'(x C'(x)))$ via $O(n \log^2 n)$ Kinoshita–Li compositional inverse + composition |

#### Blind Topic-Group Checkpoint V (After Part V: Chapters 16–21 — 8 Disjoint Problems)
1. **`CP5-1`**: **AtCoder ABC 235 Ex — Painting Weighted Graph** (Kruskal reconstruction tree + bounded-degree polynomial DP $\to$ Ch 10 / Ch 20)
2. **`CP5-2`**: **Codeforces 1616H — Keep XOR Low** (Recursive two-subtree branching DP with polynomial weight tracking $\to$ Ch 06 / Ch 10)
3. **`CP5-3`**: **AtCoder ARC 139 E — Wazir** (Circulant parity transfer matrix reduced via $(x + x^{-1})^W \bmod (x^H - 1)$ and Lucas/NTT $\to$ Ch 05 / Ch 12)
4. **`CP5-4`**: **Codeforces 1528F — AmShZ Farm** (Prüfer sequence EGF $\sum \binom{n}{k} k^k (n-k)^{n-k}$ converted via Stirling numbers to $O(K \log K)$ $\to$ Ch 04 / Ch 13)
5. **`CP5-5`**: **AtCoder AGC 021 E — Ball Eat Chameleons** (Prefix red-vs-blue threshold reduced to tilted lattice walk reflection across $y = x - (k - n)$ $\to$ Ch 16)
6. **`CP5-6`**: **Codeforces 1392H — ZS Shuffles Cards** (Harmonic stopping-time PGF + binomial series summation $\to$ Ch 08)
7. **`CP5-7`**: **AtCoder ABC 271 Ex / Grid Walk Diagonal Variant** (8-directional step classification + 1D/2D diagonal extraction $\to$ Ch 17 / Ch 18)
8. **`CP5-8`**: **Luogu P5394 / Non-Template Fast Composition Challenge (`AtCoder AGC 034 F` Prep)** (Identifying when an implicit tree equation requires `compose` vs `CDQ NTT` $\to$ Ch 10 / Ch 21)

---

### Part VI: Structural Frontier — Tree FPS, Set Power Series & $q$-Analogues (Chapters 22–24 + Blind Checkpoint VI)

#### Chapter 22: Generating Functions on Trees — Heavy-Light Decomposition, Centroid D&C & Static Top Trees
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `22-1` | **SS 1** | **AtCoder ABC 220 H — Security Camera (Tree Matching / Cover GF Bridge)** | Tree vertex-cover / independent-set polynomial merging before heavy-light scaling |
| `22-2` | **SS 2** | **AtCoder ABC 269 Ex — Antichain** | HLD heavy-chain centroid-balanced D&C NTT for $F_u(x) = x + \prod_{v \in \text{ch}(u)} F_v(x)$ in $O(N \log^2 N)$ |
| `22-3` | **Int 1** | **AtCoder ABC 355 G — Baseball** | $2 \times 2$ polynomial transfer matrices along heavy paths + centroid D&C in $O(N \log^2 N)$ |
| `22-4` | **Int 2** | **Luogu P7279 — [AGM 2021] 树木** | Tree distance / subtree size generating functions merged via HLD light-offspring D&C |
| `22-5` | **Adv 1** | **Luogu P3781 — [SDOI2017] 切树游戏** | Dynamic DP over FWT-transformed XOR polynomials $\mathbb{F}_p[x]/(x^{2^k}-1)$ on Heavy-Light chains + maintaining zero-counts mod $p$ |
| `22-6` | **Adv 2** | **Luogu P5327 — [ZJOI2019] 语言** | Tree path-union coverage via segment-tree-merge / HLD algebraic maintenance |
| `22-7` | **Mas 1** | **Codeforces 917D — Stranger Trees** | Cayley forest weight $\prod s_i$ tracked as $2 \times 2$ polynomial transitions + Taylor shift $G(x-1)$ |
| `22-8` | **Mas 2** | **QOJ 4815 / Static Top Tree (Rake-Compress) Tree FPS** | Full $O(N \log^2 N)$ Rake-Compress cluster tree for 2-terminal + 1-terminal polynomial transitions |

#### Chapter 23: Set Power Series $K[x_1,\dots,x_n]/(x_i^2)$, Subset Convolution ($\exp/\ln$) & MacWilliams XOR Duality
*Implementation Verification Footnotes*: `R-52` (`Luogu P5325` — quarantined in footnotes).
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `23-1` | **SS 1** | **AtCoder ABC 213 G — Connectivity 2** | Connected induced subgraphs via ranked subset $\ln$ (or anchored root component subtraction) |
| `23-2` | **SS 2** | **Luogu P6570 — [NOI Online #3 提高组] 优秀子序列** | Pairwise coprime subset sum = subset convolution $\exp$ evaluated on prime-factor bitmasks + $\varphi(1+S)$ |
| `23-3` | **Int 1** | **LOJ #154 — 集合幂级数 exp / ln / inv** | Point-wise after-FMT $O(n^2)$ formal ODE $H'(x) = G'(x) H(x)$ for ranked Set Power Series |
| `23-4` | **Int 2** | **AtCoder ABC 253 Ex — We Love Forest** | Matrix-Tree Theorem gives tree count $T_S$; SPS $\exp(T)$ gives $k$-edge spanning forest weights in $O(n^2 2^n)$ |
| `23-5` | **Adv 1** | **UOJ #310 — 【UNR #2】黎明前的巧克力** | Symbolic translation on $\mathbb{F}_2^m$: each chocolate is $1 + 2x^{a_i}$; FWHT eigenvalue $\in \{-1, +3\}$ yields $3^c (-1)^{n-c}$ |
| `23-6` | **Adv 2** | **Luogu P5406 — [THUPC2019] 找树** | Mixed-radix Fast Walsh–Hadamard Transform (AND / OR / XOR per bit) inside a Matrix-Tree determinant |
| `23-7` | **Mas 1** | **Codeforces 1336E2 — Chiori and Doll Picking (Hard Version)** | **MacWilliams Identity**: Dualizing $O(2^k)$ primal basis span to $O(2^{m-k})$ orthogonal code $C^\perp$ via Krawtchouk polynomials $K_j(w; m) = [z^j](1-z)^w(1+z)^{m-w}$ |
| `23-8` | **Mas 2** | **UOJ #94 — 【集训队互测2015】胡策的统计** | Iterated SPS $\ln$ and $\exp$ for biconnected/connected component counting on general 20-vertex graphs |

#### Chapter 24: $q$-Analogues, Gaussian Binomials $\binom{n}{k}_q$, $q$-Pochhammer Identities & Cyclic Sieving
| Slot | Tier | Problem ID & Title | Core Pedagogical Role |
| :--- | :--- | :--- | :--- |
| `24-1` | **SS 1** | **Codeforces 1603F — October 18, 2017** | Counting rank-$r$ subspaces / matrices over $\mathbb{F}_2^k$ via Gaussian $q$-binomials $\binom{n}{r}_2 \prod_{i=0}^{r-1}(2^k - 2^i)$ |
| `24-2` | **SS 2** | **AtCoder ABC 238 Ex — Removing People** | Circular removal expectation with $q$-series / EGF symmetry |
| `24-3` | **Int 1** | **AtCoder ABC 278 Ex — make 1** | Rothe's $q$-Binomial Theorem $\prod_{i=0}^{n-1}(1 + q^i x) = \sum q^{\binom{k}{2}} \binom{n}{k}_q x^k$ for full-rank $\mathbb{F}_2$ constraints |
| `24-4` | **Int 2** | **AtCoder ARC 145 F — Modulo Sum of Powers** | $q$-Lucas Theorem at roots of unity: $\binom{n}{k}_{\omega_p} = \binom{\lfloor n/p \rfloor}{\lfloor k/p \rfloor} \binom{n \bmod p}{k \bmod p}_{\omega_p}$ |
| `24-5` | **Adv 1** | **LOJ #6729 — $q$-模拟与高斯二项式系数** | Euler's $q$-Exponential $\exp_q(x) = \prod_{k \ge 0}(1-q^k x)^{-1}$ via $\ln$ harmonic sum $\sum \frac{x^m}{m(1-q^m)}$ |
| `24-6` | **Adv 2** | **Codeforces 1916F / Luogu P6118 — Gaussian $q$-Vandermonde & Subspace Sieve** | Subspace Inclusion-Exclusion $\sum (-1)^{\dim(U \cap V)} q^{\binom{\dim}{2}} \binom{n}{k}_q$ |
| `24-7` | **Mas 1** | **AtCoder AGC 034 F — RNG and XOR** | Solving $F \ast_{\text{XOR}} P = F + (2^n - 1) - 2^n x^0$ on $\mathbb{F}_2^n$ via FWHT + zero-mode regularization |
| `24-8` | **Mas 2** | **AtCoder AGC 055 D / $q$-Pentagonal & Rogers–Ramanujan Partition Sieve** | $q$-series partition identities and modular rank filtration |

#### Blind Topic-Group Checkpoint VI (After Part VI: Chapters 22–24 — 8 Disjoint Cumulative Problems)
1. **`CP6-1`**: **AtCoder ABC 248 G — GCD Cost on the Tree** (Dirichlet $\sum_{d \mid g} \varphi(d)$ + $2 \times 2$ polynomial $(\text{count}, \text{sum})$ DP on induced divisor forests $\to$ Ch 01 / Ch 12 / Ch 22)
2. **`CP6-2`**: **Codeforces 1119H — Triple** (3-Term Symbolic FWHT on $\mathbb{F}_2^k$: solving $c_1+c_2+c_3+c_4 = n$ for eigenvalues $(x \pm y \pm z)$ $\to$ Ch 23)
3. **`CP6-3`**: **AtCoder ABC 212 H — Nim Counting** (Geometric sum $\sum_{k=1}^N P(x)^k$ over $\mathbb{F}_2^m$ in the FWHT point-value domain $\to$ Ch 01 / Ch 23)
4. **`CP6-4`**: **Codeforces 1034E — Little C Loves 3 II** (Disjoint subset convolution via base-4 bit-count packing $\sum A_S 4^{\lvert S \rvert} \ast_{\text{OR}} \sum B_T 4^{\lvert T \rvert} \bmod 4^{\lvert S \cup T \rvert + 1}$ $\to$ Ch 23)
5. **`CP6-5`**: **AtCoder ARC 100 E — Or Plus Max** (Fast Zeta Transform (SOS DP) maintaining top-2 maximums over the subset lattice $\to$ Ch 23)
6. **`CP6-6`**: **Codeforces 914G — Sum the Fibonacci** (Triple-convolution pipeline: Disjoint Subset Convolution + Direct Product + AND-FMT weighted by Fibonacci numbers $\to$ Ch 09 / Ch 23)
7. **`CP6-7`**: **AtCoder AGC 028 D — Chords** (Connected chord-diagram component DP on circular intervals $\to$ Ch 06 / Ch 14)
8. **`CP6-8`**: **Codeforces 1844G — Tree Weights** (2-adic / Characteristic-$2$ lifting on tree LCA distance equations mod $2^k$ $\to$ Ch 12 / Ch 22)

---

### Annotated Multi-Perspective & Synthesis Archive (14 Disjoint Problems Completing the 254 Corpus)
These 14 remaining accepted problems from the 254-problem baseline are 100% disjoint from the 192 Primary Ladder slots and 48 Blind Checkpoint slots, and serve as multi-perspective synthesis case studies at the end of the textbook:
1. **`Syn-01`**: **Library Checker — `fps_24_w` (Multi-Constraint Composition Synthesis)** (Ch 03 + Ch 21)
2. **`Syn-02`**: **Library Checker — `fps_24_x` (Bivariate Generating Function Synthesis)** (Ch 04 + Ch 18)
3. **`Syn-03`**: **Luogu P3768 — 简单的数学题** (Dirichlet / Du's Sieve vs Rational Power Sums — Ch 01 + Ch 20)
4. **`Syn-04`**: **Codeforces 809E — Surprise Me!** (Virtual Tree + $\varphi(a_u a_v)$ Möbius Inversion Bridge — Ch 12 + Ch 22)
5. **`Syn-05`**: **AtCoder AGC 002 F — Leftmost Ball** (2D Ballot / Reflection vs EGF Prefix-Dominance — Ch 03 + Ch 16)
6. **`Syn-06`**: **Codeforces 1264E — Beautiful League** (Cyclic 3-Tournament Inversion $\binom{n}{3} - \sum \binom{\text{out}(v)}{2}$ — Ch 01 + Ch 15)
7. **`Syn-07`**: **AtCoder ARC 117 E — Zero-Sum Ranges 2** (Prefix-sum local-extrema layer DP — Ch 02 + Ch 16)
8. **`Syn-08`**: **Codeforces 1439D — INOI Final Contests** (Linear-probe hashing EGF $\text{SEQ}$ of contiguous blocks — Ch 03 + Ch 10)
9. **`Syn-09`**: **AtCoder AGC 020 E — Encoding Subsets** (Recursive interval-grammar DP on subset hierarchies — Ch 07 + Ch 23)
10. **`Syn-10`**: **Luogu P4705 / P5298 Variant — `Codeforces 1097G — Vladislav and a Great Legend`** (Stirling expansion $(\sum x_e)^k$ on trees — Ch 04 + Ch 22)
11. **`Syn-11`**: **AtCoder ABC 249 G — Xor Cards** (Linear basis elimination + subset counting — Ch 12 + Ch 23)
12. **`Syn-12`**: **Codeforces 1718F / Inclusion-Exclusion + Subproduct Sieve** (Ch 06 + Ch 20)
13. **`Syn-13`**: **AtCoder AGC 039 F — Min Product Sum** (2D row/column min-max layer DP with Binomial Inversion — Ch 06 + Ch 15)
14. **`Syn-14`**: **UOJ #348 — 【WC2018】州区划分** (Eulerian subgraph check + $O(n^2 2^n)$ Subset Convolution DP $F_S = \frac{1}{\text{sum}(S)^p}\sum F_T G_{S \setminus T}$ — Ch 15 + Ch 23)

---

## Summary of Mandatory Action Items for Round 2 Synthesis

1. **Adopt the 24-Chapter Granularity of Proposal A with the Strict `2 SS / 2 Int / 2 Adv / 2 Mas` 3-Hint Card Format of Proposal C**:
   - Do **not** compress the textbook to 20 chapters: splitting Proposal C's overloaded Chapters 6, 15, 18, and 20 back into 24 chapters gives **Goulden–Jackson Cluster Method (Ch 07)**, **Cacti/Block-Cut (Ch 14) vs DAGs/Bipartite (Ch 15)**, **MPE/Interpolation/Sampling Shift (Ch 20) vs `mulT`/Composition/Power Projection (Ch 21)**, **Set Power Series (Ch 23)**, and **$q$-Analogues (Ch 24)** each their own complete 8-problem 4-tier ladder.
2. **Eliminate All Checkpoint-to-Ladder Duplications (`36/36` in Proposal B, `26/40` in Proposal C, `5/48` in Proposal A)**:
   - Use the exact 48 Blind Checkpoint assignments (`CP1-1`–`CP6-8`) from the Master Matrix above, which have **0% overlap** with the 192 Primary Chapter Ladder problems.
3. **Format All Blind Checkpoints Using Proposal C's Two-Stage Spoiler-Free Architecture**:
   - Present `.1 Blind Problem Statements` (neutral mathematical translation + `Hint 1` Recognition Rubric) in the main text, and wrap `.2 Hidden Answer Key & Routing Table` (`Target Chapter`, `Hint 2`, `Hint 3`) inside a collapsible `<details>` block.
4. **Enforce 100% Quarantine of `R-01`–`R-67` into 1-Line Chapter Footnotes**:
   - Purge Proposal B's 16 template leaks and Proposal A's `Luogu P5325` (`R-52`) and `Luogu P4719` ladder slots; keep all 67 templates strictly as 1-line "Implementation Verification Footnotes" at the top of each chapter ladder.
5. **Enforce All Prerequisite Fixes (`F-01`–`F-16`)**:
   - Keep **Roots of Unity & Chirp Z-Transform in Chapter 05 (Part I)** so quadratic edge weights $2^{\binom{n}{2}}$ are available before Chapters 14–15.
   - Keep **`Luogu P4747` (Simple Permutations)** in **Chapter 21** (after Newton Iteration and Compositional Inverse).
   - Scope **`Luogu P5827` & `Luogu P5828`** in **Chapter 14** explicitly to single-$n$ Lagrange Inversion ($O(n \log n)$), and assign **`QOJ 8528`** in **Chapter 21** for the all-$n$ Kinoshita–Li composition ($O(n \log^2 n)$).
