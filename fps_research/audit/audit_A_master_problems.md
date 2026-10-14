# Master Problem Synthesis Audit Report (`PROBLEM_CURATION.md` & `problem_archive.md`)

> **Auditor**: Inspector A-Problems (Principal Mathematical & Pedagogical Auditor)  
> **Audited Files**:
> 1. [`fps_research/PROBLEM_CURATION.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md) (900 lines)
> 2. [`fps_research/problem_archive.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md) (1,702 lines)  
> **Ground-Truth Sources**: All 10 Cohort 3 Master Synthesis Wave Files ([`cohort3_wave_1a_modelling_foundations.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md) through [`cohort3_wave_5b_tree_fps_transposition_compose_q.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md)).

---

## Executive Summary of Audit Findings

| Audit Dimension | [`PROBLEM_CURATION.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md) | [`problem_archive.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md) | Severity |
| :--- | :--- | :--- | :--- |
| **0. Math Delimiter Hygiene (`\(...\)` / `\[...\]`)** | **PASS** (0 instances) | **PASS** (0 instances) | — |
| **1. Accepted Problem Accounting vs. 10 Waves** | **FAIL**: Sec 1 accounts for all 344 wave problem headers (except 2 malformed anchors and 1 wrong line target), **but** Ladders 2.1, 2.2, and Checkpoint 3.1 fabricate **23 phantom/rejected problem entries** that do **not** exist in Wave 1A or Wave 1B! Also Sec 1.1 & Sec 1.3 have internal count mismatches. | **FAIL**: Drops **2 unique worked accepted problems** from Wave 5B (`Luogu P7279 — 光棱碎片` at `5B#L1041` and `Luogu P5281 / LOJ 3044 — [ZJOI2019] Minimax 搜索` at `5B#L1099`) because Section 11 copied Wave 5B's stale summary table (`10.8`) instead of the actual worked problems in `10.1–10.6`. Also drops secondary paired problems (`ARC 105 F`, `Luogu P4389`) in headers. | **CRITICAL** |
| **2. Rejected Template Problem Accounting** | **FAIL**: Section 4 (52 entries) omits **15 rejected problems** that are explicitly listed in the Rejected tables of Waves 3A, 3B, 4A, 4B, and 5B. Worse, `CF 632E` (rejected in Wave 4A) and `fps_24_c, e, i, j, p` (rejected as bare templates) are placed inside Pedagogical Ladders 2.1/2.2 and Checkpoint 1! | **FAIL**: Section 12 (45 entries) omits **16 rejected problems** from the Rejected tables of Waves 3A, 3B, 4A, 4B, and 5B. | **HIGH** |
| **3. Line Number (`#L...`) & Cross-Ref Verification** | **FAIL**: **99 broken/mismatched `#L...` links** across Sections 1.2, 2.1–2.10, and 3.1–3.3 (including 2 syntax-broken anchors `#L3B` and `#L1326F2`, 100% of links in Ladders 2.1 & 2.2 and Checkpoint 1, and almost all secondary `*(also in Wave X)*` links in Ladders 2.3–2.10). | **FAIL**: **6 of 10 Wave Section Header line ranges** (`Waves 2B, 3A, 4A, 4B, 5A, 5B`) cite non-existent line numbers exceeding the file lengths (e.g., `Lines 1000–2712` for a 1,259-line file). Plus **9 broken internal Cross-Ref IDs** (`Problem 5A-27B`, `5A-28B`, `5A-25B`). | **CRITICAL** |
| **4. Mathematical & Entry Quality / Anti-Spoiler Audit** | **FAIL**: **20 of 40 Hint 1 (Spoiler-Free Recognition Rubric)** entries in Section 3 explicitly name the target theorem/technique (e.g., *"Wald's Identity!"*, *"Otter's Dissimilarity Theorem"*, *"Raney's Lemma / Lagrange Inversion"*, *"André's differential equation"*, *"Kinoshita–Li's bivariate Bostan–Mori"*), violating L520's anti-spoiler rule. Also `1A-6` (`fps_24_d`) is misidentified as *Permutation Inversions* (Mahonian product) instead of *Sequence (`数列`)*. | **FAIL**: (a) **2 completely wrong problem statements/formulas** (`Problem 1A-4: fps_24_k` is falsely written as Derangements $e^{-x}/(1-x)$ instead of Indecomposable Permutations $1 - P(x)^{-1}$; `Problem 1A-5: fps_24_l` is falsely written as cycle lengths in $S$ instead of $p_{p_i} \neq i$); (b) `LOJ 6539` is misnamed *Lights Out Connected*; (c) **250 problem entries** in Sections 5–11 omit Tags, Diagnostic Signals, and 3-Tier Hints; (d) **42 non-cross-ref entries** omit URLs/Constraints. | **CRITICAL** |

---

## Part I: Detailed Audit of `PROBLEM_CURATION.md`

### 1. Section 1.1 & 1.3 — Statistical & Header Count Inconsistencies

#### 1.1 Row-Sum Mismatches in Section 1.1 Table (`PROBLEM_CURATION.md` Lines 16–27)
In the global summary table at [`PROBLEM_CURATION.md` (Lines 16–27)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md#L16-L27), the column **`Total Problem Slots`** counts markdown problem headers (`345` across the 10 waves, or `344` worked problem headers since Wave 5B has 42 in Section 10 plus 1 inline problem header `#### Problem Statement` at `5B#L650`), whereas **`Single-Wave Unique Problems + Multi-Wave Shared Problems`** counts split sub-problems (`168 + 190 = 358`). Consequently, `Single-Wave Unique + Multi-Wave Shared != Total Problem Slots` on 6 of the 10 rows:

| Wave Row | Line | `Total Problem Slots` | `Single-Wave Unique` | `Multi-Wave Shared` | Actual Sum (`Unique + Shared`) | Discrepancy Cause |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Wave 1A** | L16 | `31` | `12` | `20` | `32` ($\neq 31$) | `Problem 20` (`LOJ 6539 & ARC 105F`) split into 2 problems (`M15`, `M16`) |
| **Wave 1B** | L17 | `27` | `13` | `16` | `29` ($\neq 27$) | `Problem 25` (`P4389 & P3784`) and `Problem 21` split |
| **Wave 3B** | L21 | `24` | `9` | `17` | `26` ($\neq 24$) | Compound problem headers split in `M1..M76` |
| **Wave 4A** | L22 | `28` | `11` | `19` | `30` ($\neq 28$) | `Problem 19` (`CF 1349F1/F2`) & `Problem 22` (`P5827/fps_24_w`) split |
| **Wave 5A** | L24 | `28` | `9` | `23` | `32` ($\neq 28$) | `Problems 22, 25, 27, 28` each pair 2 problems (`ABC 300Ex & ARC 138E`, `CF 1349D & 1479E`, `UOJ 450 & 424`, `CF 1515E & AGC 058D`) |
| **Wave 5B** | L25 | `42` | `29` | `19` | `48` ($\neq 42$) | 6 compound headers (`A4, B6, C7, C8, D4, E5`) pair 2 problems each |
| **Total** | L26 | **`345`** | **`165`** (sum is `168`!) | **`180`** (sum is `190`!) | **`358`** | Column sums `165` and `180` in L26 do not even equal the vertical sums of their own columns (`12+13+24+41+26+9+11+19+9+29 = 193` or `168`)! |

- **Deterministic Fix for Section 1.1 (Lines 16–27)**:
  - Check vertical column addition: in L16–L25, the `Single-Wave Unique Problems` column values are `12 + 13 + 24 + 41 + 26 + 9 + 11 + 19 + 9 + 29 = 193` (NOT `165` as claimed in L26!), and the `Multi-Wave Shared Problems` column values are `20 + 16 + 13 + 15 + 13 + 17 + 19 + 14 + 23 + 19 = 169` (NOT `180` as claimed in L26!).
  - Furthermore, the Rejected Templates column (`26 + 8 + 12 + 7 + 9 + 10 + 8 + 10 + 13 + 16 = 119`, NOT `100` as claimed in L26!).
  - Reconcile every row and column sum in L16–L26 so that vertical sums are mathematically exact and compound problem slots (`344` slots / `362` distinct problem appearances) are explicitly noted.

#### 1.2 Header Count Mismatches in Section 1.3 (`PROBLEM_CURATION.md` Lines 119–305)
In Section 1.3 ([`PROBLEM_CURATION.md` Lines 119–305](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md#L119-L305)), the subsection titles state a count of unique problems that contradicts both Section 1.1 and the actual number of numbered items in that subsection:

| Subsection | Line | Header Claim | Section 1.1 Claim | Actual Listed Items in Subsection | Fix Required |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `1.3.1 Wave 1A` | L121 | `21 Unique Problems` | `12` | **16** numbered items (`1..16`) | Change header to `(16 Single-Wave Problems)` and sync Sec 1.1 |
| `1.3.2 Wave 1B` | L140 | `15 Unique Problems` | `13` | **15** numbered items (`1..15`) | Sync Sec 1.1 to `15` |
| `1.3.3 Wave 2A` | L158 | `24 Unique Problems` | `24` | **26** numbered items (`1..26`) | Change header & Sec 1.1 to `26` |
| `1.3.4 Wave 2B` | L187 | `41 Unique Problems` | `41` | **41** items across 5 clusters | Counts match (`10+9+5+5+12 = 41`) |
| `1.3.5 Wave 3A` | L205 | `26 Unique Problems` | `26` | **25** numbered items (`1..25`) | Change header & Sec 1.1 to `25` |
| `1.3.6 Wave 3B` | L234 | `17 Unique Problems` | `9` | **18** numbered items (`1..18`) | Change header to `(18 Single-Wave Problems)` and sync Sec 1.1 |
| `1.3.7 Wave 4A` | L256 | `20 Unique Problems` | `11` | **17** numbered items (`1..17`) | Change header to `(17 Single-Wave Problems)` and sync Sec 1.1 |
| `1.3.8 Wave 4B` | L277 | `19 Unique Problems` | `19` | **13** items across 3 bullets | Change header & Sec 1.1 to `13` |
| `1.3.9 Wave 5A` | L285 | `15 Unique Problems` | `9` | **13** numbered items (`1..13`) | Change header to `(13 Single-Wave Problems)` and sync Sec 1.1 |
| `1.3.10 Wave 5B` | L298 | `29 Unique Problems` | `29` | **27** problem links across 6 bullets | Change header & Sec 1.1 to `27` |

---

### 2. Critical Fabrication / Phantom Problems in Ladders 2.1, 2.2, and Blind Checkpoint 1

> [!CAUTION]
> **23 Problem Entries in Ladders 2.1, 2.2, and Blind Checkpoint 1 Do Not Exist in Wave 1A or Wave 1B!**  
> Whoever drafted Sections 2.1, 2.2, and 3.1 of `PROBLEM_CURATION.md` invented a set of problems (`Luogu P2000`, `CF 893E`, `CF 785D`, `CF 623E`, `CF 1251F`, `Kattis kinversions`, `CF 528D`, `Luogu P3723`, `CF 1099F`, `CF 632E`, `CF 1613F`, `ARC 147E`, `CF 662C`, `CF 954I`, `CF 1096F`, plus rejected bare templates `fps_24_b, c, e, i, j, p`) that **never appear as accepted problems in `cohort3_wave_1a_modelling_foundations.md` or `cohort3_wave_1b_dp_and_sums.md`**, and then attached arbitrary `#L...` line numbers pointing into the middle of unrelated problem derivations!

#### 2.1 Complete Audit of Ladder 2.1 (`PROBLEM_CURATION.md` Lines 319–329)

| Ladder Slot | Line | Problem Listed in Ladder 2.1 | Status in `cohort3_wave_1a_modelling_foundations.md` | Broken Link in Ladder 2.1 | Actual Content at Target Line in Wave 1A |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1A-1** | L319 | `AtCoder fps_24_a` — *Snacks* | Accepted (`Problem 1` at `#L670`) | `#L670` (OK) | `#### Problem 1: AtCoder fps_24_a — Snacks` |
| **1A-2** | L320 | `Luogu P2000` — *拯救世界 (Saving the World)* | **DOES NOT EXIST IN WAVE 1A!** | `#L698` | Inside `Problem 2 (fps_24_d — Sequence)` constraints! |
| **1A-3** | L321 | `Codeforces 893E` — *Counting Arrays* | **DOES NOT EXIST IN WAVE 1A!** | `#L731` | Inside `Problem 3 (ABC 276 G)` Hint 1! |
| **1A-4** | L322 | `AtCoder fps_24_c` — *Sequence* | **REJECTED TEMPLATE (`R2` at `1A#L1330`, `T43` in `problem_archive.md`)!** | `#L755` | `#### Problem 5: AtCoder fps_24_l — Permutation 2`! |
| **1A-5** | L323 | `Codeforces 785D` — *Anton and School - 2* | **DOES NOT EXIST IN WAVE 1A!** | `#L803` | Inside `Problem 7 (LOJ 6268 — 分拆数)` statement! |
| **1A-6** | L324 | `AtCoder fps_24_d` — *Permutation Inversions* | **WRONG PROBLEM STATEMENT!** In Wave 1A (`#L695`), `fps_24_d` is *Sequence (`数列`)* (counting sequences with non-zero adjacent differences via $F(x) = [y^0]\prod(y + \frac{x}{1-x} - x)$), **NOT** Permutation Inversions $\prod \frac{1-x^i}{1-x}$! | `#L828`, `1B#L1140` | `#L828` is inside `Problem 8 (P4841/fps_24_m)` Hint 1; `1B#L1140` is inside `1B Problem 3 (CSES Apples and Bananas)`! |
| **1A-7** | L325 | `AtCoder fps_24_e` — *Sequence 2 (Bounded EGF)* | **REJECTED TEMPLATE (`R3` at `1A#L1331`, `R-04` in `PROBLEM_CURATION.md` L811)!** | `#L859`, `2A#L761` | `#L859` is inside `Problem 9 (CF 438E)` derivation; `2A#L761` is inside `2A Problem 10 (LOJ 6077)` Hint 3! |
| **1A-8** | L326 | `AtCoder fps_24_i` — *Boxes and Balls (EGF `SEQ`/`SET`)* | **REJECTED TEMPLATE (`R7` at `1A#L1335`, `T43` in `problem_archive.md`)!** | `#L884`, `1B#L1275` | `#L884` is inside `Problem 11 (fps_24_f)` derivation; `1B#L1275` is inside `1B Problem 8 (CF 755G)`! |
| **1A-9** | L327 | `Codeforces 623E` — *Transforming Sequence* | **DOES NOT EXIST IN WAVE 1A!** (Appears in 1B, 2A, 4A) | `#L971`, `2A#L815`, `5B#L1470` | `#L971` is inside `Problem 15 (Luogu P4548)` Hint 1; `2A#L815` is `---`; `5B#L1470` is inside `5B Problem D2 (CF 1054H)`! |
| **1A-10** | L328 | `Luogu P4841` — *城市规划 (Connected Labeled Graphs)* | Accepted (`Problem 8` at `#L821`) | `#L1030`, `1B#L1318`, `3A#L931`, `3B#L735` | `#L1030` is inside `Problem 18 (UOJ 50)`! Actual is **`1A#L821`**, **`1B#L1436`**, **`3A#L1372`**, **`5A#L868`**, **`5B#L1717`**. |
| **1A-11** | L329 | `Codeforces 1251F` — *Red-White Fence* | **DOES NOT EXIST IN WAVE 1A!** (Appears only in Wave 1B as `Problem 5` at `1B#L1192`) | `#L940` | `#L940` is inside `Problem 14 (LOJ 6538 — 烷基计数)`! |

- **Deterministic Remediation for Ladder 2.1 (`PROBLEM_CURATION.md` Lines 319–329)**:
  Replace Ladder 2.1 with 11 actual accepted problems from [`cohort3_wave_1a_modelling_foundations.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md) spanning `Stepping Stone` $\to$ `Intermediate` $\to$ `Advanced` $\to$ `Mastery` with exact line numbers:
  1. `1A-1`: **AtCoder `fps_24_a`** — *Snacks* (`Stepping Stone`, [`1A#L670`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md#L670), also [`1B#L1076`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1076))
  2. `1A-2`: **AtCoder `fps_24_d`** — *Sequence (`数列`)* (`Stepping Stone`, [`1A#L695`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md#L695))
  3. `1A-3`: **AtCoder ABC 276 G** — *Count Sequences* (`Stepping Stone`, [`1A#L720`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md#L720), also [`1B#L1626`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1626), [`2B#L494`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_2b_ie_pgf_zh_ja_audit.md#L494), [`4A#L852`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4a_multivariate_bostan_mori_diag.md#L852))
  4. `1A-4`: **AtCoder `fps_24_k`** — *Permutation (Indecomposable Permutations)* (`Intermediate`, [`1A#L737`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md#L737), also [`3B#L742`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md#L742), [`5A#L844`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L844))
  5. `1A-5`: **AtCoder `fps_24_l`** — *Permutation 2 ($p_{p_i} \neq i$)* (`Intermediate`, [`1A#L755`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md#L755))
  6. `1A-6`: **LOJ #6268** — *分拆数 (Inverse Euler Transform)* (`Intermediate`, [`1A#L797`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md#L797))
  7. `1A-7`: **Luogu P4841 / `fps_24_m`** — *城市规划 (Connected Labeled Graphs)* (`Intermediate`, [`1A#L821`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md#L821), also [`1B#L1436`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1436), [`3A#L1372`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3a_lagrange_residues_trees_graphs.md#L1372), [`5A#L868`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L868), [`5B#L1717`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md#L1717))
  8. `1A-8`: **AtCoder `fps_24_n`** — *Sequence 3 (Cyclic Shifts / Burnside + Inverse Euler)* (`Advanced`, [`1A#L914`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md#L914))
  9. `1A-9`: **51Nod 1728** — *不动点 (Fixed Points of Iterated Endofunctions)* (`Advanced`, [`1A#L1001`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md#L1001), also [`3A#L1063`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3a_lagrange_residues_trees_graphs.md#L1063), [`3B#L1019`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md#L1019))
  10. `1A-10`: **Luogu P5824** — *十二重计数法 (The Twelvefold Way)* (`Mastery`, [`1A#L1161`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md#L1161), also [`2A#L825`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_2a_substitutions_transforms.md#L825))
  11. `1A-11`: **Luogu P5900** — *无标号无根树计数 (Unlabeled Unrooted Trees via Otter's Theorem)* (`Mastery`, [`1A#L1256`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md#L1256))

#### 2.2 Complete Audit of Ladder 2.2 (`PROBLEM_CURATION.md` Lines 339–349)

| Ladder Slot | Line | Problem Listed in Ladder 2.2 | Status in `cohort3_wave_1b_dp_and_sums.md` | Broken Link in Ladder 2.2 | Actual Content at Target Line in Wave 1B |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1B-1** | L339 | `CSES 1731 / Apples and Bananas` | Accepted (`Problem 3` at `#L1136`) | `#L1076` | `#L1076` is `Problem 1: AtCoder FPS 24 A — Snacks`! |
| **1B-2** | L340 | `AtCoder fps_24_b` — *Tickets* | **REJECTED TEMPLATE (`R2` at `1B#L1054`, `R-02` in `PROBLEM_CURATION.md` L809)!** | `#L1083` | Inside `Problem 1 (Snacks)` statement (`- Snack C: 2 kcal`)! |
| **1B-3** | L341 | `AtCoder ABC 260 Ex` — *Colorfulness* | **DOES NOT EXIST IN WAVE 1B!** (Appears in 2B, 3A, 5A, 5B) | `#L1101` | Inside `Problem 1 (Snacks)` derivation! |
| **1B-4** | L342 | `Kattis kinversions` — *K-Inversions* | **DOES NOT EXIST IN WAVE 1B!** | `#L1121` | Inside `Problem 2 (FPS 24 G — Coin)` hints! |
| **1B-5** | L343 | `Codeforces 528D` — *Fuzzy Search* | **DOES NOT EXIST IN WAVE 1B!** | `#L1163` | Inside `Problem 4 (ARC 028 D)` complexity line! |
| **1B-6** | L344 | `AtCoder ARC 028 D` — *注文の多い高橋商店* | Accepted (`Problem 4` at `#L1149`) | `#L1185` | Inside `Problem 5 (CF 1251F)`! Actual is **`1B#L1149`**. |
| **1B-7** | L345 | `Luogu P3723` — *[AH2017/HNOI2017] 礼物* | **DOES NOT EXIST IN WAVE 1B!** | `#L1204` | Inside `Problem 5 (CF 1251F)` hints! |
| **1B-8** | L346 | `Codeforces 1099F / CF 1218E` — *Subset Product Queries* | **DOES NOT EXIST IN WAVE 1B!** | `#L1228`, `1A#L912` | `#L1228` is inside `Problem 6 (CF 1473E / ABC 214 E)`! |
| **1B-9** | L347 | `Codeforces 632E` — *Thief in a Shop* | **REJECTED TEMPLATE (`R5` at `4A#L1280`) & DOES NOT EXIST IN WAVE 1B!** | `#L1254` | Blank line inside `Problem 7`! |
| **1B-10** | L348 | `Codeforces 1613F` — *Tree Coloring* | **DOES NOT EXIST IN WAVE 1B!** (Appears in 2B, 3A, 5B) | `#L1408`, `2B#L500` | `#L1408` is `---`; `2B#L500` is inside `2B Problem A2`! |
| **1B-11** | L349 | `AtCoder ARC 147 E / CF 1808E3` — *Minibuses on Venus* | **DOES NOT EXIST IN WAVE 1B!** (`CF 1808E3` is in Wave 2B `B14` at `2B#L774`) | `#L1498` | `#L1498` is `---`! |

- **Deterministic Remediation for Ladder 2.2 (`PROBLEM_CURATION.md` Lines 339–349)**:
  Replace Ladder 2.2 with 11 actual accepted problems from [`cohort3_wave_1b_dp_and_sums.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md) with exact line numbers:
  1. `1B-1`: **CSES 2111** — *Apples and Bananas* (`Stepping Stone`, [`1B#L1136`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1136))
  2. `1B-2`: **AtCoder `fps_24_g`** — *Coin (Sliding-Window Knapsack Rollback)* (`Stepping Stone`, [`1B#L1107`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1107))
  3. `1B-3`: **AtCoder ARC 028 D** — *注文の多い高橋商店 (Rollback Knapsack Queries)* (`Stepping Stone`, [`1B#L1149`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1149))
  4. `1B-4`: **Codeforces 1251F** — *Red-White Fence* (`Intermediate`, [`1B#L1192`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1192))
  5. `1B-5`: **Codeforces 1096G** — *Lucky Tickets* (`Intermediate`, [`1B#L1213`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1213), also [`5A#L821`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L821))
  6. `1B-6`: **AtCoder AGC 001 E** — *BBQ Hard* (`Intermediate`, [`1B#L1239`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1239))
  7. `1B-7`: **Luogu P3338** — *[ZJOI2014] 力 (Force — Difference Convolution)* (`Intermediate`, [`1B#L1312`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1312))
  8. `1B-8`: **Codeforces 993E** — *Nikita and Order Statistics* (`Intermediate`, [`1B#L1331`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1331))
  9. `1B-9`: **Codeforces 954I** — *Yet Another String Matching Problem* (`Advanced`, [`1B#L1349`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1349))
  10. `1B-10`: **Codeforces 755G** — *PolandBall and Many Other Balls* (`Advanced`, [`1B#L1270`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1270), also [`2A#L728`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_2a_substitutions_transforms.md#L728), [`4A#L920`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4a_multivariate_bostan_mori_diag.md#L920), [`5A#L999`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L999))
  11. `1B-11`: **AtCoder ABC 213 Ex** — *Stroll (Online DAG Path Convolution via CDQ NTT)* (`Mastery`, [`1B#L1897`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1b_dp_and_sums.md#L1897), also [`5A#L1052`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L1052))

#### 2.3 Complete Audit of Blind Checkpoint 1 (`PROBLEM_CURATION.md` Lines 532–575)

In Section 3.1 ([`PROBLEM_CURATION.md` Lines 532–575](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md#L532-L575)), **4 of the 8 problems do not exist in Wave 1A or Wave 1B**, and **all 8 Answer Key links in Section 3.1.2 (Lines 568–575) point to wrong lines**:

| Checkpoint ID | Problem in Sec 3.1 | Actual Status in Waves 1A & 1B | Wrong Link in Sec 3.1.2 (L568–L575) | Actual Content at Target Line | Fix Required |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CP1-1** | `Codeforces 662C` — *Binary Table* | **DOES NOT EXIST IN WAVE 1A OR 1B!** | `1B#L1469` | Inside `1B Problem 14 (Luogu P3702 — 序列计数)`! | Replace `CP1-1` with **`1B Problem 14: Luogu P3702`** (`1B#L1463`) or **`1B Problem 15: CF 1707E / BZOJ 3992`** (`1B#L1501`) |
| **CP1-2** | `AtCoder fps_24_j` — *coloring (EGF Parity)* | **REJECTED TEMPLATE (`R8` at `1A#L1336`, `T43` in `problem_archive.md`)!** | `1B#L1296` | Inside `1B Problem 8 (CF 755G)`! | Replace `CP1-2` with **`1A Problem 13: AtCoder fps_24_r — Random Jump`** (`1A#L909`) or **`1A Problem 19: ABC 236 Ex`** (`1A#L1039`) |
| **CP1-3** | `AtCoder fps_24_g` — *Coin* | Accepted in Wave 1B (`Problem 2` at `1B#L1107`), **NOT** Wave 1A! | `1A#L912` | Blank line before `1A Problem 14`! | Fix link to **`[cohort3_wave_1b_dp_and_sums.md#L1107](./cohort3_wave_1b_dp_and_sums.md#L1107)`** |
| **CP1-4** | `Codeforces 954I` — *Yet Another String Matching Problem* | Accepted in Wave 1B (`Problem 10` at `1B#L1349`) | `1B#L1163` | Inside `1B Problem 4 (ARC 028 D)`! | Fix link to **`[cohort3_wave_1b_dp_and_sums.md#L1349](./cohort3_wave_1b_dp_and_sums.md#L1349)`** |
| **CP1-5** | `Codeforces 1096F` — *Inversions* | **DOES NOT EXIST IN WAVE 1A OR 1B!** | `1A#L828` | Inside `1A Problem 8 (Luogu P4841)` Hint 1! | Replace `CP1-5` with **`1B Problem 12: CF 553E — Kyoya and Train`** (`1B#L1399`) or **`1A Problem 16: CF 891E — Lust`** (`1A#L980`) |
| **CP1-6** | `AtCoder fps_24_m` — *Connected Graph* | Accepted in Wave 1A (`Problem 8` at `1A#L821`) | `1A#L1001` | `1A#L1001` is `Problem 17: 51Nod 1728`! | Fix link to **`[cohort3_wave_1a_modelling_foundations.md#L821](./cohort3_wave_1a_modelling_foundations.md#L821)`** |
| **CP1-7** | `AtCoder fps_24_n` — *Sequence 3* | Accepted in Wave 1A (`Problem 13` at `1A#L914`) — **WAIT**: Sec 3.1 describes `fps_24_n` as $A_i \equiv i \pmod 2$ parity EGF, which is **FALSE** (`fps_24_n` at `1A#L914` is cyclic shift necklaces via Burnside + Inverse Euler)! | `1B#L1275` | Inside `1B Problem 8 (CF 755G)`! | Fix `CP1-7` card to match actual `fps_24_n` (Burnside cyclic shift equivalence classes) and fix link to **`[cohort3_wave_1a_modelling_foundations.md#L914](./cohort3_wave_1a_modelling_foundations.md#L914)`** |
| **CP1-8** | `AtCoder fps_24_p` — *Subset Sum* | **REJECTED TEMPLATE (`R9` at `1A#L1337`, `T43` in `problem_archive.md`)!** | `1B#L1318` | Inside `1B Problem 9 (Luogu P3338)`! | Replace `CP1-8` with **`1B Problem 25: Luogu P4389 & P3784 — 付公主的背包 / 遗忘的集合`** (`1B#L1830`, `1A#L774`) |

---

### 3. Complete Table of All Other Broken `#L...` Links in `PROBLEM_CURATION.md`

Every single broken/mismatched link in Sections 1.2, 2.3–2.10, and 3.2–3.5 of [`PROBLEM_CURATION.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md) is cataloged below with its exact deterministic replacement:

| Line in `PROBLEM_CURATION.md` | Context / Slot | Current (Broken) Link | Why It Is Broken | Exact Deterministic Replacement |
| :--- | :--- | :--- | :--- | :--- |
| **L45** | `M3` (`CF 438E`) | `[3B:L995](./cohort3_wave_3b_implicit_zh_ja_audit.md#L3B)` | Anchor `#L3B` is non-numeric | `[3B:L995](./cohort3_wave_3b_implicit_zh_ja_audit.md#L995)` |
| **L54** | `M12` (`CF 623E`) | `[5B:L1235](./cohort3_wave_5b_tree_fps_transposition_compose_q.md#L1235)` | `5B#L1235` is `Problem B6: CF 1770G & CF 1988F` (`CF 623E` is only in the stale summary table at `5B#L1871`, not a worked problem in 5B) | Remove `5B:L1235` and change Wave Count from `4` to `3` (`1B:L1755`, `2A:L801`, `4A:L906`) |
| **L93** | `M51` (`CF 1326F2`) | `[5B:L1774](./cohort3_wave_5b_tree_fps_transposition_compose_q.md#L1326F2)` | Anchor `#L1326F2` is malformed | `[5B:L1774](./cohort3_wave_5b_tree_fps_transposition_compose_q.md#L1774)` |
| **L359** | `2A-1` (`CF 932E`) | `2A#L906`, `2B#L540`, `5A#L1100` | `2A#L906` is `Problem 22 (CF 1278F)`; `2B#L540` is `Problem A6`; `5A#L1100` is mid-derivation | `2A#L872`, `2B#L641`, `5A#L1085` |
| **L361** | `2A-3` (`fps_24_h`) | `2A#L774`, `4A#L890`, `4B#L1120` | All 3 land mid-paragraph! | `2A#L638`, `4A#L984`, `4B#L1142` |
| **L362** | `2A-4` (`Luogu P4491`) | `2A#L829`, `1A#L1120`, `5A#L835` | `2A#L829` is mid-P5824; `P4491` is not in 1A or 5A (`P4491` is in `2B#L555`) | `2A#L843`, `2B#L555` |
| **L363** | `2A-5` (`Luogu P4705`) | `1A#L1149`, `4A#L964`, `4B#L1206`, `5B#L1213` | `1A`, `4A`, `4B` links land mid-paragraph (and `P4705` is not in 4A/4B) | `2A#L944` *(also in `1A#L1141`, `5B#L1213`)* |
| **L364** | `2A-6` (`ABC 222 H`) | `1B#L1429`, `3A#L729`, `5A#L893`, `5B#L1315` | `1B#L1429` is inside `P3702`; `3A#L729` is `CF 438E`; `5A#L893` is mid-text | `2A#L708` *(also in `3A#L699`, `3B#L719`, `4B#L1301`, `5A#L891`, `5B#L1315`)* |
| **L365** | `2A-7` (`LOJ #6077`) | `1A#L1091`, `2B#L596`, `3A#L789`, `4B#L1359` | `1A#L1091` is inside `fps_24_o`; `2B#L596` is `ABC 236 Ex`; `3A#L789` is `P4091`; `4B#L1359` is `UOJ 50` | `2A#L750` *(also in `2B#L628`, `3A#L742`, `4B#L1231`)* |
| **L367** | `2A-9` (`Luogu P6667`) | `1B#L1364` | `1B#L1364` is inside `CF 954I`! (`P6667` is in `5A#L1115`) | `2A#L857` *(also in `5A#L1115`)* |
| **L369** | `2A-11` (`CF 1054H`) | `1B#L1501` | `1B#L1501` is `CF 1707E / BZOJ 3992` (not `CF 1054H`) | `2A#L1124` *(also in `5B#L1452`)* |
| **L384** | `2B-6` (`LOJ #6538`) | `5A#L1230` | Lands inside Hints of `5A Problem 23` | `1A#L934`, `3B#L935`, `5A#L1224` |
| **L385** | `2B-7` (`ARC 105 F`) | `1A#L1294`, `1B#L1450`, `3A#L956`, `5B#L1717` | `1A#L1294` is inside `fps_24_s`; `1B#L1450` is inside `P4841`; `3A#L956` is `ABC 253 Ex`; `5B#L1717` is `P4841` | `2B#L851` *(also in `1A#L1060`)* |
| **L386** | `2B-8` (`Luogu P4548`) | `1A#L953`, `1B#L1862`, `2A#L688` | `2A#L688` is blank line (`P4548` is not in 2A) | `2B#L1044` *(also in `1A#L953`, `1B#L1862`)* |
| **L404** | `3A-5` (`CF 960G`) | `1A#L1176`, `1B#L1705`, `2A#L883`, `4A#L936` | `1A#L1176` is inside `P5824`; `1B#L1705` is `ABC 267 Ex`; `4A#L936` is `P5406` | `3A#L873` *(also in `1A#L1122`, `1B#L1782`, `2A#L883`, `4A#L920`)* |
| **L406** | `3A-7` (`ABC 260 Ex`) | `2B#L999`, `5A#L1179`, `5B#L1301` | `5B#L1301` is inside `ABC 230 Ex` (`ABC 260 Ex` is not in 5B) | `3A#L990` *(also in `2B#L999`, `5A#L1179`)* |
| **L407** | `3A-8` (`ABC 222 H`) | `1A#L1264`, `2A#L708`, `3B#L719`, `4B#L1593`, `5B#L1325` | `1A#L1264` is `P5900`; `4B#L1593` & `5B#L1325` land mid-text | `3A#L699` *(also in `2A#L708`, `3B#L719`, `4B#L1301`, `5A#L891`, `5B#L1315`)* |
| **L409** | `3A-10` (`CF 1349F2`) | `2B#L828`, `3B#L1275`, `4A#L1232`, `5A#L1308`, `5B#L1392` | `2B, 3B, 4A, 5A` links all land mid-text! | `3A#L1150` *(also in `2B#L814`, `3B#L1203`, `4A#L1122`, `5A#L1302`, `5B#L1392`)* |
| **L410** | `3A-11` (`UOJ #596`) | `4B#L1674` | Lands mid-text (`UOJ 596` header is `4B#L1672`) | `3A#L1256` *(also in `4B#L1672`)* |
| **L423** | `3B-4` (`UOJ #424`) | `1A#L1204`, `2A#L870`, `3A#L832`, `4B#L1557`, `5A#L939`, `5B#L1391` | All 6 secondary links point to wrong lines/problems! | `3B#L803` *(also in `2A#L777`, `3A#L817`, `4A#L1217`, `4B#L1554`, `5A#L1321`)* |
| **L426** | `3B-7` (`Luogu P5434`) | `1A#L1234`, `3A#L1107`, `5B#L1372` | `1A#L1234` is blank line (`P5434` is `1A#L1213`; `3A` is `3A#L1343`) | `3B#L956` *(also in `1A#L1213`, `3A#L1343`, `5B#L1372`)* |
| **L427** | `3B-8` (`ABC 230 Ex`) | `1A#L1234`, `5A#L1185`, `5B#L1297` | `ABC 230 Ex` is not in 1A; `5A#L1185` is inside `ABC 260 Ex` | `3B#L1068` *(also in `5A#L1155`, `5B#L1297`)* |
| **L428** | `3B-9` (`fps_24_s`) | `1A#L1310`, `3A#L1000` | `1A#L1310` is inside `fps_24_x`; `fps_24_s` is not in 3A | `3B#L1097` *(also in `1A#L1277`)* |
| **L429** | `3B-10` (`LOJ #6728`) | `3A#L1329`, `4A#L1150`, `4B#L1458` | All 3 secondary links point to wrong lines! | `3B#L1228` *(also in `3A#L1178`, `4A#L1200`, `4B#L1621`)* |
| **L430** | `3B-11` (`fps_24_x`) | `3B#L1252`, `1A#L1310` | `1A#L1310` is mid-text (`fps_24_x` header is `1A#L1300`) | `3B#L1252` *(also in `1A#L1300`)* |
| **L442** | `4A-3` (`ABC 300 Ex`) | `2A#L732`, `5A#L879`, `5B#L1161` | All 3 secondary links land mid-text! | `4A#L866` *(also in `2A#L679`, `5A#L1199`, `5B#L1158`)* |
| **L443** | `4A-4` (`ABC 240 G`) | `2A#L1065`, `4B#L1187` | Both secondary links land mid-text! | `4A#L894` *(also in `2A#L1057`, `4B#L1168`)* |
| **L445** | `4A-6` (`AGC 013 E`) | `2B#L641` | `2B#L641` is `Problem A13: CF 932E` (`AGC 013 E` is `2B#L959`) | `4A#L1026` *(also in `2B#L959`)* |
| **L446** | `4A-7` (`AGC 058 D`) | `2B#L969`, `4B#L1331`, `5A#L939`, `5B#L1599` | All 4 secondary links point to wrong lines! | `4A#L1055` *(also in `2B#L943`, `4B#L1459`, `5A#L1347`, `5B#L1410`)* |
| **L449** | `4A-10` (`CF 1349D`) | `2A#L721`, `4B#L1268`, `5A#L1274` | `4B#L1268` is inside `ABC 222 H` (`CF 1349D` is not in 4B) | `4A#L1235` *(also in `2A#L721`, `2B#L1059`, `5A#L1274`)* |
| **L461** | `4B-3` (`ABC 296 Ex`) | `3A#L696` | `3A#L696` is inside `Problem 3: Z(n,m)` (`ABC 296 Ex` is not in 3A) | `4B#L1123` |
| **L463** | `4B-5` (`AGC 021 E`) | `2A#L870`, `3A#L664` | Both secondary links land mid-text! | `4B#L1207` *(also in `2A#L764`, `3A#L670`)* |
| **L468** | `4B-10` (`Luogu P5828`) | `3A#L1401` | Lands mid-text (`P5827 & P5828` header is `3A#L1396`) | `4B#L1649` *(also in `3A#L1396`)* |
| **L481** | `5A-3` (`fps_24_o`) | `1A#L1081`, `1B#L1296`, `3A#L844`, `3B#L850` | `1B#L1296` is inside `CF 755G` (`fps_24_o` is not in 1B) | `5A#L909` *(also in `1A#L1081`, `3A#L844`, `3B#L850`)* |
| **L484** | `5A-6` (`fps_24_r`) | `2A#L1091`, `2B#L627`, `3A#L886`, `4A#L938`, `4B#L1247` | `2B, 3A, 4A, 4B` links point to wrong problems! | `5A#L967` *(also in `1A#L909`, `2A#L1091`)* |
| **L487** | `5A-9` (`ABC 230 Ex`) | `3B#L1068`, `5B#L993` | `5B#L993` is Section 10 header (`ABC 230 Ex` is `5B#L1297`) | `5A#L1155` *(also in `3B#L1068`, `5B#L1297`)* |
| **L500** | `5B-2` (`CF 1770G`) | `2A#L788` | `2A#L788` is inside `fps_24_v` (`CF 1770G` is only in `5B#L1235`) | `5B#L1235` |
| **L503** | `5B-5` (`CF 901E`) | `1B#L1386` | `1B#L1386` is inside `ABC 292 Ex` (`CF 901E` is only in `5B#L1531`) | `5B#L1531` |
| **L506** | `5B-8` (`Luogu P5366`) | `2A#L1051` | `2A#L1051` is inside `P3702` (`P5366` is only in `5B#L1659`) | `5B#L1659` |
| **L508** | `5B-10` (`ABC 387 G`) | `3A#L971`, `4A#L1122` | `4A#L1122` is `CF 1349F2` (`ABC 387 G` is `4A#L1150`) | `5B#L1334` *(also in `3A#L971`, `4A#L1150`)* |
| **L509** | `5B-11` (`ARC 154 F`) | `2B#L1178`, `4A#L1180` | `4A#L1180` is Tier 4 header (`ARC 154 F` is `4A#L1182`) | `5B#L1351` *(also in `2B#L1178`, `4A#L1182`)* |

---

### 4. Section 3 (Blind Checkpoints 3.1–3.5) — Spoiler-Free Recognition Rubric Violations

Section 3 ([`PROBLEM_CURATION.md` Line 520](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md#L520)) explicitly establishes the pedagogical rule:
> *"No technique names appear in the problem cards or Hint 1."*

While the **Problem Cards** (`**Problem Statement**:`) in `3.1.1`–`3.5.1` obey this rule, **20 of the 40 `Hint 1 (Spoiler-Free Recognition Rubric)` entries** directly name the target theorem, algorithm, or generating function transform! Every spoiler leak is listed below with its line number and required fix:

1. **`CP1-5` (L550)**: Leaks *"By **Linearity of Expectation**"* and *"classical **Mahonian inversion generating function** $(1+x)(1+x+x^2)\cdots(1+x+\dots+x^{k-1})$"*. $\to$ Rewrite to ask how adding the $k$-th largest missing element affects the inversion count independently of previous choices.
2. **`CP1-6` (L554)**: Leaks *"**Exponential Generating Function**"* and *"what relation connects $G(x)$ and $C(x)$?"*. $\to$ Rewrite to ask how arbitrary labeled structures decompose into unordered collections of connected components.
3. **`CP1-7` (L558)**: Leaks *"write the **EGF** for the allowed frequencies of odd values vs. even values. What **symbolic operator** combines $M$ labeled alphabet types..."*. $\to$ Replace along with fixing `CP1-7` (`fps_24_n`) to Burnside's Lemma on cyclic shifts.
4. **`CP2-3` (L596)**: Leaks *"**Principle of Inclusion-Exclusion**"* and *"**Roots-of-Unity Filter**"*. $\to$ Ask how to bound the maximum run length by penalizing violations and how to isolate indices congruent to $r \pmod d$.
5. **`CP2-6` (L608)**: Leaks *"Look at **Wald's Identity!**"* and *"border-overlap polynomial"*. $\to$ Ask what conservation law relates the state values at the moment $S$ appears to the overlaps of $S$ with its own prefixes.
6. **`CP2-8` (L616)**: Leaks *"**generalized Min-Max IE formula** for the $k$-th largest stopping time"* and *"**Pascal's identity**"*. $\to$ Ask how $\max_{i \in S} T_i$ relates to $\min_{i \in T} T_i$ and how to express the $k$-th maximum as an alternating sum over subset minima.
7. **`CP3-1` (L642)**: Leaks *"In a **Prüfer code** of length $N-2$..."*. $\to$ Ask what classic bijection maps labeled trees on $N$ vertices with degrees $d_i$ to sequences of length $N-2$.
8. **`CP3-3` (L650)**: Leaks *"**composite LIF** $\frac{1}{N}[u^{N-1}] H'(u) \phi(u)^N$ without ever running **Newton Iteration**"*. $\to$ Ask whether you need to solve for the full series $T(x)$ first or if you can directly extract the $N$-th coefficient of an implicit equation $T = x \phi(T)$ composed with another polynomial.
9. **`CP3-4` (L654)**: Leaks *"**1D Newton Iteration** in $O(K \log K)$"*. $\to$ Ask how to eliminate $M-1$ of the $M$ coupled equations so only one unknown series remains.
10. **`CP3-5` (L658)**: Leaks *"**Pólya's cycle index $Z(S_3)$** and **Newton iteration**"* and *"**Otter's Dissimilarity Theorem**"*. $\to$ Ask how to account for 3-way child symmetries at a rooted vertex and how to unroot an unlabeled tree by comparing vertex symmetries and edge symmetries.
11. **`CP3-7` (L666)**: Leaks *"**Raney's Lemma / Lagrange Inversion**"*. $\to$ Ask what cyclic rotation lemma counts lattice paths of total sum $+1$ that stay strictly positive.
12. **`CP3-8` (L670)**: Leaks *"**generalized Cayley formula (`CF 156D`)**"*. $\to$ Ask how many ways $k$ components of sizes $s_1, \dots, s_k$ can be connected by $k-1$ tree edges, and how each factor $s_i$ can be interpreted combinatorially inside component $i$.
13. **`CP4-1` (L696)**: Leaks *"**Connected-Component IE (`连续段容斥`)**"*. $\to$ Ask how to replace the local adjacency constraint $A_i + A_{i+1} \neq K$ with weights on maximal violating chains.
14. **`CP4-3` (L704)**: Leaks *"**Hermite / formal Gaussian integration**"*. $\to$ Ask how to decouple the all-pairs interaction $\prod_{i<j}(x_i + x_j)$ using an antisymmetric determinant identity.
15. **`CP4-6` (L716)**: Leaks *"**generalized Cayley formula (or Good–Lagrange / bridge-block substitution)**"*. $\to$ Ask what happens when you contract every 2-edge-connected component into a single super-vertex.
16. **`CP4-7` (L720)**: Leaks *"**Pentagonal Number Theorem** supports in $O(N \sqrt{N})$"*. $\to$ Ask how sparse the reciprocal of the partition denominator $\prod_{j \ge 1}(1 - x^j)$ is.
17. **`CP4-8` (L724)**: Leaks *"By factoring $Q(x, y)$ through the **roots of the kernel $1 - x S(u) = 0$ (or Chebyshev rational division)**"*. $\to$ Ask how to set up a bivariate recursion for the remaining capacity and eliminate the boundary condition at capacity $0$.
18. **`CP5-1` (L750)**: Leaks *"**middle product (`mulT`)**"*. $\to$ Ask what linear operator is dual to multipoint evaluation when you reverse the circuit arrows.
19. **`CP5-2` (L753–754)**: Leaks *"**Dynamic DP**"* and *"**HLD**"*. $\to$ Ask how to decompose the tree into heavy chains so that light-child contributions can be merged via divide-and-conquer and chain transitions via $2 \times 2$ polynomial matrices.
20. **`CP5-3` (L758, `CP5-4` L762, `CP5-6` L770, `CP5-7` L774)**:
    - `CP5-3` (L758) leaks *"**Gaussian $q$-binomial coefficient** $\binom{A+B}{A}_q$"*, *"**roots of unity filter**"*, and *"**$q$-Lucas theorem**"*.
    - `CP5-4` (L762) leaks *"**Matrix-Tree or ranked subset convolution**"* and *"**Set Power Series**"*.
    - `CP5-6` (L770) leaks *"**André's differential equation** $F' = \frac{1}{2}(F^2 + 1)$"*, *"**CDQ FFT**"*, and *"**Newton**"*.
    - `CP5-7` (L774) leaks *"**CDQ divide-and-conquer (or semi-relaxed convolution) with Kinoshita–Li's bivariate Bostan–Mori**"*.
    $\to$ Rewrite each Hint 1 to pose a pure structural/modelling question without naming the theorem or algorithm.

---

### 5. Section 4 (Rejected Template Problems) — 15 Omitted Rejected Problems from Wave Files

The following **15 rejected problems** appear in the Rejected Template tables of `cohort3_wave_3a` through `cohort3_wave_5b` but are missing from Section 4 of [`PROBLEM_CURATION.md` (Lines 795–900)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md#L795-L900):

| Wave Source | Line in Wave File | Judge & Problem ID | Problem Title | Reason for Rejection in Wave File | Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Wave 3A** | [`3A#L1434`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3a_lagrange_residues_trees_graphs.md#L1434) | **Luogu P5900** | 无标号树计数 | Unlabeled Otter tree template in 3A | *(Note: Accepted as `Problem 29` in Wave 1A `#L1256`; add cross-note!)* |
| **Wave 3A** | [`3A#L1435`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3a_lagrange_residues_trees_graphs.md#L1435) | **Library Checker** | `counting_eulerian_circuits` | Direct BEST Theorem + Matrix-Tree verification without GF | Add to Category IV (Sec 4.4) |
| **Wave 3A** | [`3A#L1436`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3a_lagrange_residues_trees_graphs.md#L1436) | **CSES 1095** | Exponentiation | Trivial modular exponentiation drill | Add to Category I (Sec 4.1) |
| **Wave 3B** | [`3B#L1328`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md#L1328) | **Luogu P7591** | 2021 CoE-II D | Pure formula evaluation / bare verification | Add to Category IV (Sec 4.4) |
| **Wave 3B** | [`3B#L1329`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md#L1329) | **SPOJ LARMY** | Lannister Army | Pure DP optimization (Divide & Conquer / Knuth), non-GF | Add to Category I (Sec 4.1) |
| **Wave 3B / 4B** | [`3B#L1330`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md#L1330), [`4B#L1752`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4b_furstenberg_kernel_good_lagrange.md#L1752) | **CSES 2064 / Luogu P1044** | Bracket Sequences I / `[NOIP2003]` 栈 | Bare Catalan number $C_n = \frac{1}{n+1}\binom{2n}{n}$ formula check | Add to Category IV (Sec 4.4) |
| **Wave 4A** | [`4A#L1280`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4a_multivariate_bostan_mori_diag.md#L1280) | **Codeforces 632E** | Thief in a Shop | Bare 1D boolean knapsack FFT power $A(x)^k$ | Add to Category I (Sec 4.1) & remove from Ladder 2.2! |
| **Wave 4A** | [`4A#L1281`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4a_multivariate_bostan_mori_diag.md#L1281) | **AtCoder ABC 130 E** | Common Subsequence | Trivial 2D prefix-sum DP without GF content | Add to Category V (Sec 4.5) |
| **Wave 4A** | [`4A#L1282`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4a_multivariate_bostan_mori_diag.md#L1282) | **SPOJ FIBOSUM** | Fibonacci Sum | Trivial $2 \times 2$ matrix exponentiation | Add to Category V (Sec 4.5) |
| **Wave 4B** | [`4B#L1753`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4b_furstenberg_kernel_good_lagrange.md#L1753) | **CSES 2187** | Bracket Sequences II | Bare Catalan prefix ballot formula $\frac{k+1}{n+1}\binom{2n-k}{n}$ | Add to Category IV (Sec 4.4) |
| **Wave 4B** | [`4B#L1754`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4b_furstenberg_kernel_good_lagrange.md#L1754) | **Codeforces 896D** | Nephren Runs a Cinema | Direct single-reflection ballot + Lucas/CRT drill | Add to Category IV (Sec 4.4) |
| **Wave 4B** | [`4B#L1755`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4b_furstenberg_kernel_good_lagrange.md#L1755) | **AtCoder ABC 205 E** | White and Black Balls | Direct single-reflection ballot theorem $\binom{N+M}{N} - \binom{N+M}{N+K+1}$ | Add to Category IV (Sec 4.4) |
| **Wave 4B** | [`4B#L1756`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_4b_furstenberg_kernel_good_lagrange.md#L1756) | **Luogu P1641** | `[SCOI2010]` 生成字符串 | Direct $\binom{n+m}{m} - \binom{n+m}{m-1}$ reflection template | Add to Category IV (Sec 4.4) |
| **Wave 5B** | [`5B#L1839`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md#L1839) | **Library Checker** | `static_top_tree` / `point_set_tree_path_composite_sum` | Pure data-structure template without polynomial D&C NTT | Add to Category IV (Sec 4.4) |
| **Wave 5B** | [`5B#L1854`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md#L1854) | **Library Checker** | `polynomial_composite_set_power_series` | Bare SPS composition template | Add to Category VII (Sec 4.7) |

*(Note: Wave 3B also lists `CF 1096G` and `Luogu P4841` in its local rejected table at `3B#L1331–1332` because they belong to Waves 1A/1B/5A rather than Newton Iteration, and Wave 4B lists `CF 1264D2` at `4B#L1757` while Wave 4A accepts `CF 1264D2` at `4A#L1012` — document those 3 as "Rejected in Wave X as off-topic, Accepted in Wave Y".)*

---

## Part II: Detailed Audit of `problem_archive.md`

### 1. Wrong Wave File Line-Range Pointers in Sections 2–11 of `problem_archive.md`

In [`problem_archive.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md), every Wave Section (`Sections 2–11`) begins with a `> **Full Reference**:` blockquote giving the line range of the problem encyclopedia inside the corresponding `cohort3_wave_*.md` file. **6 of the 10 line ranges are completely fabricated (exceeding the total line count of the target file by 400–1,400 lines!)**:

| Section in `problem_archive.md` | Line | Target Wave File | Actual Total Lines in Wave File | Claimed Line Range in `problem_archive.md` | Actual Problem Section Line Range in Wave File | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **Sec 2 (Wave 1A)** | L288 | `cohort3_wave_1a_modelling_foundations.md` | 1,362 | `Section 7 (Lines 662–1323)` | `Section 7.1 (Lines 662–1324)` | Off by 1 line |
| **Sec 3 (Wave 1B)** | L520 | `cohort3_wave_1b_dp_and_sums.md` | 1,925 | `Section 7.3 (Lines 1066–1925)` | `Section 7.3 (Lines 1066–1925)` | Exact |
| **Sec 4 (Wave 2A)** | L711 | `cohort3_wave_2a_substitutions_transforms.md` | 1,150 | `Section 10.2 (Lines 631–1150)` | `Section 10.2 (Lines 631–1150)` | Exact |
| **Sec 5 (Wave 2B)** | L951 | `cohort3_wave_2b_ie_pgf_zh_ja_audit.md` | **1,259** | `Section 6 (Lines 1000–2712)` | **`Section 6 (Lines 468–1246)`** | **BROKEN** (exceeds file length by 1,453 lines!) |
| **Sec 6 (Wave 3A)** | L1094 | `cohort3_wave_3a_lagrange_residues_trees_graphs.md` | **1,436** | `Section 4 (Lines 740–2465)` | **`Section 4 (Lines 642–1422)`** | **BROKEN** (exceeds file length by 1,029 lines!) |
| **Sec 7 (Wave 3B)** | L1207 | `cohort3_wave_3b_implicit_zh_ja_audit.md` | 1,519 | `Section 8 (Lines 695–1316)` | `Section 8 (Lines 695–1317)` | Off by 1 line |
| **Sec 8 (Wave 4A)** | L1277 | `cohort3_wave_4a_multivariate_bostan_mori_diag.md` | **1,513** | `Section 6 (Lines 830–1940)` | **`Section 6 (Lines 836–1269)`** | **BROKEN** (exceeds file length by 427 lines!) |
| **Sec 9 (Wave 4B)** | L1365 | `cohort3_wave_4b_furstenberg_kernel_good_lagrange.md` | **1,781** | `Section 7 (Lines 1070–2219)` | **`Section 7 (Lines 1082–1741)`** | **BROKEN** (exceeds file length by 438 lines!) |
| **Sec 10 (Wave 5A)** | L1440 | `cohort3_wave_5a_ode_sparse_cdq_relaxed.md` | 1,420 | `Section 7 (Lines 850–1371)` | **`Section 7 (Lines 817–1372)`** | **BROKEN** (`L850` misses Problems 1 & 2 at `L821` & `L844`!) |
| **Sec 11 (Wave 5B)** | L1539 | `cohort3_wave_5b_tree_fps_transposition_compose_q.md` | **2,050** | `Section 10 (Lines 1230–2541)` | **`Section 10 (Lines 993–1832)`** | **BROKEN** (exceeds file length by 491 lines and misses `L993–L1229`!) |

---

### 2. Critical Mathematical & Problem Misidentifications in `problem_archive.md`

#### 2.1 `Problem 1A-4: AtCoder fps_24_k — Permutation` (`problem_archive.md` Lines 315–320)
- **What `problem_archive.md` (Lines 315–320) currently says**:
  - **Statement**: *"Count the number of permutations $p$ of $\{1, \dots, N\}$ with no fixed points ($p_i \neq i$, i.e., derangements), or more generally with forbidden cycle lengths."*
  - **Solution Formula**: $D_N = N! [x^N] \frac{e^{-x}}{1-x} = N! \sum_{k=0}^N \frac{(-1)^k}{k!}$.
- **Why this is 100% WRONG**:
  - In [`cohort3_wave_1a_modelling_foundations.md` (Lines 737–752)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md#L737-L752), [`cohort3_wave_3b_implicit_zh_ja_audit.md` (Lines 742–757)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md#L742-L757), and [`cohort3_wave_5a_ode_sparse_cdq_relaxed.md` (Lines 844–866)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L844-L866), **AtCoder `fps_24_k` (Permutation)** counts **indecomposable permutations** of $\{1, \dots, N\}$ satisfying $\{p_1, \dots, p_k\} \neq \{1, \dots, k\}$ for all $1 \le k < N$!
- **Exact Replacement Text for `problem_archive.md` Lines 315–320**:
  ```markdown
  #### Problem 1A-4: AtCoder `fps_24_k` — Permutation
  - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_k` | **Constraints**: $N \le 2.5 \times 10^5$, $\bmod 998244353$.
  - **Statement**: Count the number of indecomposable permutations $P = (P_1, \dots, P_N)$ of $(1, \dots, N)$ such that for every $1 \le k < N$, $\{P_1, \dots, P_k\} \neq \{1, \dots, k\}$.
  - **Tags**: `[OGF-SEQ-Inversion]`, `[Poly-Inv]`, `[Connected-Prefix]` | **Diagnostic Signal**: Every permutation decomposes uniquely into a non-empty sequence (`SEQ`) of minimal prefix blocks that map $\{1,\dots,k\}$ to itself.
  - **3-Tier Hints**: (1) Any permutation $P$ has a unique smallest $k \ge 1$ where $\{P_1,\dots,P_k\} = \{1,\dots,k\}$. (2) Thus total permutations $A(x) = \sum_{n=0}^N n! x^n$ and indecomposable permutations $F(x) = \sum_{n=1}^N f_n x^n$ satisfy $A(x) = \frac{1}{1 - F(x)}$. (3) Rearrange to $F(x) = 1 - A(x)^{-1} \bmod x^{N+1}$ and invert in $O(N \log N)$.
  - **Solution Formula**: $f_N = [x^N]\left(1 - \left(\sum_{n=0}^N n! x^n\right)^{-1}\right) \bmod 998244353$.
  ```
- **Also Fix Section 1.1 Index Row (`problem_archive.md` Line 22)**:
  - Currently Line 22 says `fps_24_k | Permutation (Derangements / Cycle E...) | 1A-4, 3B-3, 5A-2`. Change `Permutation (Derangements / Cycle E...)` to `Permutation (Indecomposable Permutations)`.

#### 2.2 `Problem 1A-5: AtCoder fps_24_l — Permutation 2` (`problem_archive.md` Lines 322–327)
- **What `problem_archive.md` (Lines 322–327) currently says**:
  - **Statement**: *"Count permutations of $\{1, \dots, N\}$ whose cycle lengths all belong to a given subset $S \subseteq \{1, \dots, N\}$ (or have constrained cycle parity/divisibility)."*
  - **Solution Formula**: $N! [x^N] \exp\left(\sum_{k \in S} \frac{x^k}{k}\right)$.
- **Why this is 100% WRONG**:
  - In [`cohort3_wave_1a_modelling_foundations.md` (Lines 755–772)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md#L755-L772), **AtCoder `fps_24_l` (Permutation 2)** asks for the number of permutations of $(1, \dots, N)$ satisfying $P_{P_i} \neq i$ for all $1 \le i \le N$ (i.e., **no cycles of length $1$ or $2$**), solved in $O(N)$ time via EGF $\frac{\exp(-x - x^2/2)}{1-x}$!
- **Exact Replacement Text for `problem_archive.md` Lines 322–327**:
  ```markdown
  #### Problem 1A-5: AtCoder `fps_24_l` — Permutation 2
  - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_l` | **Constraints**: $N \le 2.5 \times 10^5$, $\bmod 998244353$.
  - **Statement**: Count the number of permutations $P$ of $(1, \dots, N)$ such that $P_{P_i} \neq i$ for all $1 \le i \le N$.
  - **Tags**: `[EGF]`, `[Cycle-Index]`, `[Exp-Symbolic-Method]` | **Diagnostic Signal**: Condition $P_{P_i} \neq i$ forbids fixed points ($1$-cycles) and $2$-cycles in the disjoint cycle decomposition of $P$.
  - **3-Tier Hints**: (1) Decompose $P$ into disjoint directed cycles; $P_{P_i} = i$ holds iff $i$ lies in a cycle of length $1$ or $2$. (2) By the Symbolic Method, the EGF of allowed cycles is $C(x) = \sum_{k \ge 3} \frac{x^k}{k} = \ln\frac{1}{1-x} - x - \frac{x^2}{2}$. (3) Exponentiate: $\widehat{F}(x) = \exp(C(x)) = \frac{\exp(-x - x^2/2)}{1-x}$.
  - **Solution Formula**: $N! [x^N] \frac{\exp(-x - x^2/2)}{1-x}$ (or D-finite recurrence $a_n = (n-1)a_{n-1} + (n-1)(n-2)a_{n-3}$).
  ```

#### 2.3 Misidentification of `LOJ 6539` in Section 1.5 (`problem_archive.md` Line 258)
- In [`problem_archive.md` (Line 258)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md#L258), `LOJ 6539` is listed as:
  `| LOJ 6539 | Lights Out Connected | 1A-20 | [EGF-Ln], [Bipartite] | Intermediate |`
- **Why this is WRONG**: `LOJ 6539` is **`仙人掌计数` (Labeled Cactus Graph Enumeration)** via Newton iteration on $C(x) = x \exp\left(\sum_{k \ge 1} \frac{C(x)^k}{2}\right)$, whereas *Lights Out Connected* is **`AtCoder ARC 105 F`** (which shares slot `Problem 20` at `1A#L1060`).
- **Fix**: Update Line 258 to `| LOJ 6539 | 仙人掌计数 (Labeled Cactus Enumeration) | 1A-20 | [EGF-Exp], [Newton-Cactus] | Mastery |`, and add `AtCoder ARC 105 F | Lights Out Connected | 1A-20, 2B-C5` to Section 1.1 & `Problem 1A-20` (Line 431).

---

### 3. Dropped Accepted Problems & Split-Brain in Wave 5B (`problem_archive.md` Section 11 vs. `cohort3_wave_5b`)

In [`cohort3_wave_5b_tree_fps_transposition_compose_q.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md), Section `10.1–10.6` (Lines 1001–1832) contains the **42 full worked problem derivations**, whereas Section `10.8` (Lines 1858–1904) is an older summary table whose Cluster A–C rows were never synced with `10.1–10.3`. Because `problem_archive.md` Section 11 (Lines 1537–1650) copied the stale table `10.8` instead of the actual worked problems in `10.1–10.6`, **two unique worked accepted problems in Wave 5B were completely dropped from `problem_archive.md`**, and 11 problem slots in Section 11 do not match `cohort3_wave_5b` Section `10.1–10.3`:

| Slot | Actual Worked Problem in `cohort3_wave_5b` (`Sec 10.1–10.6`) | Entry in `problem_archive.md` (`Sec 11`, Lines 1543–1648) | Audit Status & Required Action |
| :--- | :--- | :--- | :--- |
| **5B-A2** | **`AtCoder ABC 355 G — Baseball`** (`5B#L1022`) | `CF 438E / UOJ 747 — 面基之路` (L1546) | **MISMATCH**: Restore `AtCoder ABC 355 G — Baseball` to `5B-A2` (and keep `UOJ 747` as a secondary variant if desired). |
| **5B-A3** | **`Luogu P7279 — 光棱碎片 (Prism Shards)`** (`5B#L1041`) | `AtCoder ABC 355 G — Baseball` (L1547) | **CRITICAL DROPPED PROBLEM**: **`Luogu P7279 — 光棱碎片`** is completely missing from `problem_archive.md` (both Sec 1.3 and Sec 11)! Must be added with full metadata from `5B#L1041–1059`. |
| **5B-A4** | **`Codeforces 1613F (Tree Coloring) & Luogu P4707 (重返现世)`** (`5B#L1060`) | `Luogu P4707 — 重返现世` (L1550) | Add `Codeforces 1613F` to `5B-A4` header. |
| **5B-A6** | **`Luogu P5281 / LOJ 3044 — [ZJOI2019] Minimax 搜索`** (`5B#L1099`) | `Luogu P5326 ([ZJOI2019] 开关) & Luogu P5298 ([PKUWC2018] Minimax)` (L1554) | **CRITICAL DROPPED PROBLEM**: **`Luogu P5281 / LOJ 3044 — [ZJOI2019] Minimax 搜索`** is completely missing from `problem_archive.md` (both Sec 1.3/1.5 and Sec 11)! Must be added from `5B#L1099–1119`. |
| **5B-B2** | **`AtCoder ABC 300 Ex — Fibonacci: Revisited`** (`5B#L1158`) | `Luogu P4705 (玩游戏) & ABC 300 Ex` (L1562) | Sync header with `5B#L1158`. |
| **5B-B3** | **`AtCoder ARC 136 F — Flip Cells`** (`5B#L1176`) | `AtCoder ARC 136 F & Codeforces 623E` (L1563) | Sync header with `5B#L1176`. |
| **5B-B4** | **`AtCoder AGC 038 E — Gachapon`** (`5B#L1195`) | `AtCoder AGC 038 E & Luogu P7440` (L1564) | Sync header (`Luogu P7440` is in `5B-C7` at `5B#L1392`). |
| **5B-B6** | **`Codeforces 1770G (Koxia and Bracket) & CF 1988F (Heartbeat)`** (`5B#L1235`) | `Codeforces 1770G & Luogu P5827` (L1568) | **DROPPED VARIANT**: `CF 1988F (Heartbeat)` is in `5B#L1235` (and `PROBLEM_CURATION.md` L300) but missing from `problem_archive.md` L1568! |
| **5B-B7** | **`UOJ 182 (a^-1 + b problem) & UOJ 604 / Luogu P7439`** (`5B#L1255`) | `UOJ 182 & UOJ 604` (L1571) | Add `Luogu P7439 ([KrOI2021]Feux Follets)` to `5B-B7` & Sec 1.3. |
| **5B-C2..C6** | `C2: ABC 230 Ex` (`#L1297`), `C3: ABC 222 H` (`#L1315`), `C5: ARC 154 F` (`#L1351`), `C6: Luogu P5434` (`#L1372`) | Mixes `ABC 336 G`, `Luogu P5434`, `Luogu P5827`, `CF 1967E2` from stale table `10.8` (L1580–1585) | Sync `5B-C2..C6` headers with `cohort3_wave_5b` Lines 1297–1391 (and also update `cohort3_wave_5b` Table `10.8` at Lines 1864–1882 to match `10.1–10.3`!). |

#### Additional Dropped Secondary Problems in Compound Headers (`problem_archive.md`)
- **`Problem 1A-20` (Line 431)**: Header in `1A#L1060` is `#### Problem 20: LOJ #6539 — 仙人掌计数 & AtCoder ARC 105 F — Lights Out Connected`, but `problem_archive.md` L431 omits `AtCoder ARC 105 F — Lights Out Connected`.
- **`Problem 1B-25` (Line 691)**: Header in `1B#L1830` is `#### Problem 25: Luogu P4389 付公主的背包 & Luogu P3784 (SDOI 2017) — 遗忘的集合`, but `problem_archive.md` L691 omits `Luogu P4389`.
- **`Problem 5A-22` (Line 1508)**: Header in `5A#L1199` is `#### Problem 22: AtCoder ABC 300 Ex — Fibonacci: Revisited & ARC 138 E — Decreasing Subsequence`, but `problem_archive.md` L1508 omits `AtCoder ARC 138 E — Decreasing Subsequence` (which is completely absent from `problem_archive.md`!).
- **`Problem 5A-25` (Line 1517)**: Header in `5A#L1274` is `#### Problem 25: Codeforces 1349D — Slime and Biscuits & Codeforces 1479E — School Clubs`, but `problem_archive.md` L1517 omits `Codeforces 1479E — School Clubs`.
- **`Problem 5A-27` (Line 1525)**: Header in `5A#L1321` is `#### Problem 27: UOJ #450 — 【集训队作业2018】复读机 (Repeater) & UOJ #424 — count`, but `problem_archive.md` L1525 omits `UOJ #424 — count`.

---

### 4. Broken Internal Cross-Reference IDs & Missing Metadata in `problem_archive.md`

#### 4.1 9 Broken Internal Cross-Reference Pointers (`Problem 5A-27B`, `5A-28B`, `5A-25B`)
In Sections 5–11 of [`problem_archive.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md), 9 cross-reference stubs point to non-existent problem IDs (`5A-27B`, `5A-28B`, `5A-25B`) that do not exist in Section 10:

1. **Line 1015 (`Problem 2B-B10: UOJ 450 — 复读机`)**: Says `Cross-ref **Problem 5A-27B**` $\to$ Must be **`Problem 1A-28`** and **`Problem 5A-27`** (L1525).
2. **Line 1089 (`Problem 2B-E15: Codeforces 1479E — School Clubs`)**: Says `Cross-ref **Problem 5A-25B**` $\to$ `Problem 5A-25` (L1517) only cross-refs `2A-6` (`CF 1349D`)! **Because `2B-E15`, `4B-22`, and `5A-25` all cross-ref each other in a circle without writing the formula for `CF 1479E`, `CF 1479E` has NO URL, NO constraints, and NO solution formula anywhere in `problem_archive.md`!**
3. **Line 1150 (`Problem 3A-19: UOJ 450 — 复读机`)**: Says `Cross-ref **Problem 5A-27B**` $\to$ Must be **`Problem 1A-28`** and **`Problem 5A-27`**.
4. **Line 1252 (`Problem 3B-16: UOJ 450 — 复读机`)**: Says `Cross-ref **Problem 5A-27B**` $\to$ Must be **`Problem 1A-28`** and **`Problem 5A-27`**.
5. **Line 1312 (`Problem 4A-P13: UOJ 450 — 复读机`)**: Says `Cross-ref **Problem 5A-27B**` $\to$ Must be **`Problem 1A-28`** and **`Problem 5A-27`**.
6. **Line 1314 (`Problem 4A-P15: AtCoder AGC 058 D`)**: Says `Cross-ref **Problem 2B-D5** and **Problem 5A-28B**` $\to$ Must be **`Problem 2B-D5`** and **`Problem 5A-28`** (L1530).
7. **Line 1410 (`Problem 4B-22: Codeforces 1479E — School Clubs`)**: Says `Cross-ref **Problem 2B-E15** and **Problem 5A-25B**` $\to$ Circular reference (`2B-E15` points to `5A-25B` which doesn't exist)! Write out the full URL, constraints ($M \le 1000, \sum a_i \le 4\times 10^4$), and rational D-finite PGF recurrence for `CF 1479E` at `2B-E15` (from `2B#L1230`).
8. **Line 1423 (`Problem 4B-27: AtCoder AGC 058 D`)**: Says `Cross-ref **Problem 2B-D5** and **Problem 5A-28B**` $\to$ Must be **`Problem 2B-D5`** and **`Problem 5A-28`**.
9. **Line 1587 (`Problem 5B-C8: AtCoder AGC 058 D & QOJ 8518`)**: Says `Cross-ref **Problem 2B-D5** and **Problem 5A-28B**` $\to$ Must be **`Problem 2B-D5`** and **`Problem 5A-28`**, AND must include the statement/formula for **`QOJ 8518 — 树的染色 (Tree Coloring)`** (from `5B#L1410`), which is currently dropped by turning `5B-C8` into a bare cross-ref!

#### 4.2 Other Compound Problems Dropped by Bare Cross-Ref Stubs in `problem_archive.md`
- **`Problem 5B-A2` (Line 1546)**: Turning `5B-A2` into `Cross-ref Problem 1A-10` dropped **`UOJ 747 — 面基之路`** (and **`ABC 355 G — Baseball`**).
- **`Problem 5B-B3` (Line 1563)**: OK (`ARC 136 F` is `2A-5` and `CF 623E` is `1B-23`).
- **`Problem 5B-C2` (Line 1580)**: Says `Problem 5B-C2: AtCoder ABC 230 Ex & ABC 336 G: Cross-ref Problem 3B-18 and Problem 5A-20` — neither `3B-18` nor `5A-20` covers `ABC 336 G`!
- **`Problem 5B-C6` (Line 1585)**: Says `Problem 5B-C6: Luogu P5434 & Codeforces 1967E2: Cross-ref Problem 1A-27` — `1A-27` does not cover `CF 1967E2`!

#### 4.3 42 Non-Cross-Ref Entries Missing URLs and/or Exact Constraints in `problem_archive.md`
In violation of [`problem_archive.md` Line 6](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md#L6), the following **42 primary problem entries** in Sections 4–11 lack a `**URL**:` field and/or `**Constraints**:` field (all URLs and constraints are present in the corresponding `cohort3_wave_*.md` files and must be copied over):
- **Wave 2A**: `2A-29` (L888 — missing URL & constraints).
- **Wave 2B**: `2B-A9` (L975), `2B-A10` (L977), `2B-B9` (L1012), `2B-B11` (L1016), `2B-C5` (L1035), `2B-D1` (L1044), `2B-D2` (L1046), `2B-D3` (L1048), `2B-D4` (L1050), `2B-D6` (L1055), `2B-E3` (L1065), `2B-E7` (L1074), `2B-E12` (L1083).
- **Wave 3A**: `3A-12` (L1125), `3A-36` (L1196).
- **Wave 3B**: `3B-8` (L1232), `3B-15` (L1249), `3B-21` (L1264), `3B-22` (L1266).
- **Wave 4A**: `4A-P20` (L1331), `4A-P28` (L1358).
- **Wave 4B**: `4B-14` (L1393), `4B-15` (L1395), `4B-25` (L1414), `4B-29` (L1425).
- **Wave 5A**: `5A-28` (L1530 — missing constraints & URL for `AGC 058D` / `CF 1515E`).
- **Wave 5B**: `5B-B5` (L1567), `5B-C5` (L1583), `5B-D5` (L1606), `5B-E5` (L1629), `5B-F2` (L1637), `5B-F7` (L1648).
- Additionally, **all 250 entries in Sections 5–11 (Lines 949–1650)** omit `**Tags**:`, `**Diagnostic Signal**:`, and `**3-Tier Hints**:` (which were included in Sections 2–4 for Waves 1A, 1B, 2A). Either enrich Sections 5–11 with Tags/Diagnostic Signal/3-Tier Hints from `cohort3_wave_2b..5b` or update Line 6 of `problem_archive.md` to accurately describe the compact format used in Sections 5–11.

#### 4.4 16 Omitted Rejected Template Problems in Section 12 of `problem_archive.md`
Section 12 of [`problem_archive.md` (Lines 1653–1702)](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md#L1653-L1702) lists `T1..T45`, omitting the same **15 rejected problems** listed in Part I Section 5 above (`Luogu P5900 [3A]`, `LC counting_eulerian_circuits`, `CSES 1095`, `Luogu P7591`, `SPOJ LARMY`, `CSES 2064 / Luogu P1044`, `CF 632E`, `ABC 130 E`, `SPOJ FIBOSUM`, `CSES 2187`, `CF 896D`, `ABC 205 E`, `Luogu P1641`, `LC static_top_tree`, `LC polynomial_composite_set_power_series`) **plus** **`Luogu P6114` (`【模板】Lyndon 分解`)** from `Wave 2A#L624` (which is `R-27` in `PROBLEM_CURATION.md` L851 but missing from `problem_archive.md` Section 12!). Add all 16 as rows `T46..T61` in Section 12 of `problem_archive.md`.

---

## Summary Checklist for Deterministic Remediation

1. **In `PROBLEM_CURATION.md`**:
   - Fix the vertical & horizontal sums in Section 1.1 (Lines 16–27) and the subsection header counts in Section 1.3 (Lines 121–298).
   - Fix the 3 broken links in Section 1.2 (`L45` `#L3B` $\to$ `#L995`, `L54` remove `5B:L1235`, `L93` `#L1326F2` $\to$ `#L1774`).
   - Replace the fabricated/rejected problem entries and broken `#L...` links in **Ladder 2.1** (Lines 319–329), **Ladder 2.2** (Lines 339–349), and **Blind Checkpoint 1** (Lines 532–575) using the exact tables in Part I Section 2 above.
   - Apply all 38 exact `#L...` link replacements in **Ladders 2.3–2.10** from Part I Section 3 above.
   - Rewrite the 20 spoiler-leaking **Hint 1** entries in **Section 3 (Lines 550–774)** so no theorem or technique names appear in Hint 1.
   - Append the **15 missing rejected problems** from Waves 3A–5B to **Section 4 (Lines 795–900)**.
2. **In `problem_archive.md`**:
   - Fix the 6 fabricated Wave Section line-range headers in **Sections 5, 6, 8, 9, 10, 11** (`L951, L1094, L1277, L1365, L1440, L1539`).
   - Replace the 2 mathematically wrong problem entries **`Problem 1A-4: fps_24_k`** (Lines 315–320, Indecomposable Permutations, NOT Derangements) and **`Problem 1A-5: fps_24_l`** (Lines 322–327, $P_{P_i} \neq i$, NOT general cycle subset $S$), and fix `LOJ 6539` (`仙人掌计数`, NOT *Lights Out Connected*) at Line 258.
   - Add the **2 missing worked Wave 5B problems** (**`Luogu P7279 — 光棱碎片`** from `5B#L1041` and **`Luogu P5281 / LOJ 3044 — [ZJOI2019] Minimax 搜索`** from `5B#L1099`), plus missing paired problems (`ARC 105 F`, `Luogu P4389`, `ARC 138 E`, `CF 1479E`, `CF 1988F`, `QOJ 8518`), and sync Section 11 (`5B-A1..F7`) with `cohort3_wave_5b` Section `10.1–10.6`.
   - Fix all 9 broken internal cross-references (`Problem 5A-27B` $\to$ `5A-27`, `5A-28B` $\to$ `5A-28`, and write out `CF 1479E` at `2B-E15` instead of the circular `5A-25B` reference).
   - Add missing URLs and exact constraints to the 42 entries listed in Part II Section 4.3, and append `T46..T61` (the 16 omitted rejected template problems) to Section 12.
