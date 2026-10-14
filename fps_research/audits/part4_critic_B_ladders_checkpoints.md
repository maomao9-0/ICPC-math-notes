# Part IV Critic B Audit Report: Problem Ladders, Inline Self-Containment, Progressive Hints & Blind Checkpoint (`Ch 14`–`Ch 17` & `CP-IV`)

**Auditor**: Part IV Critic B (Problem Ladders, Inline Self-Containment, Progressive Hints & Blind Checkpoint Auditor)  
**Scope**: All `40` problems across the `5` Part IV files (`8` per chapter in `Ch 14`–`Ch 17` + `8` in `CP-IV`):
1. [ch14-pgf-stopping-times-renewal-poisson-martingales.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd) (`8` problems: `SS-1`–`Mas-2`)
2. [ch15-1d-lattice-walks-chebyshev-kernel-method.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd) (`8` problems: `SS-1`–`Mas-2`)
3. [ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd) (`8` problems: `SS-1`–`Mas-2`)
4. [ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd) (`8` problems: `SS-1`–`Mas-2`)
5. [cp04-part4-pgf-walks-multivariate.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd) (`8` problems: `CP-IV.1`–`CP-IV.8`)

**Reference Authorities Cross-Examined**:
- [CURRICULUM_ARCHITECTURE.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md) (lines 728–867 for `Ch 14`–`Ch 17`; lines 1285–1315 for `CP-IV`)
- [PROBLEM_CURATION.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md) (lines 430–511, 1140–1310)
- [problem_archive.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/problem_archive.md) (lines 31–45, 1520–1592)
- [AGENTS.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/AGENTS.md)

---

## 1. Executive Summary & Audit Verdict

| File | Pool ID Match (`8/8`) | Single Statement & $N \le 4$ Trace | 3 Hints & Full Derivation | Spoiler-Free / Editorial Compliance | Overall Status |
| :--- | :-: | :-: | :-: | :-: | :-: |
| **`Ch 14`** (`ch14-*.qmd`) | **8 / 8 PASS** | **8 / 8 PASS** | **8 / 8 PASS** *(Hint 1 spoilers noted)* | 1 broken link (`L1298`) | **MINOR REVISIONS** |
| **`Ch 15`** (`ch15-*.qmd`) | **8 / 8 PASS** | **8 / 8 PASS** | **7 / 8 PASS** (`Mas-2` Hint 2 vs. Solution base-case bug; missing explicit `Algorithm Contract` boxes) | Minor `Ch 20` forward-ref in `Adv-1` | **MODERATE REVISIONS** |
| **`Ch 16`** (`ch16-*.qmd`) | **8 / 8 PASS** | **7 / 8 PASS** (`Adv-1` abbreviated trace + parenthetical hedge) | **7 / 8 PASS** (`Mas-2` false 2nd equality in $\chi(I)$ formula) | 4 broken links (`L8–L11`) | **CRITICAL MATH FIX REQUIRED** |
| **`Ch 17`** (`ch17-*.qmd`) | **8 / 8 IDs PASS** *(see `#204` / `#234` Special Check)* | **8 / 8 PASS** *(minor parentheticals in `Int-1`, `Adv-1`)* | **7 / 8 PASS** (`Mas-2` false $\chi$ formula + wrong `Ch 15` ref; `SS-2` raw `"Wait:"` monologue) | 4 broken links (`L11–L14`) | **MODERATE / CRITICAL FIXES** |
| **`CP-IV`** (`cp04-*.qmd`) | **8 / 8 PASS** | **7 / 8 PASS** (`CP-IV.8` dual/hedged statement & constraint mismatch) | **7 / 8 PASS** (`CP-IV.1` Hint 3 vs. Solution `dp[0][0]` sign contradiction + raw `"Wait:"` monologue) | **FAIL** (`CP-IV.7` & `CP-IV.8` Stage 1 statements/walkthroughs & `Hint 1`s contain explicit paradigm spoilers) | **CRITICAL REVISIONS REQUIRED** |

### Summary of Critical & High-Priority Findings Across All 40 Problems
1. **[CRITICAL — Mathematical Error in Carry-Grading Formula $\chi(I)$ in `Ch 16 Mas-2 (#214)` & `Ch 17 Mas-2 (#234)`]**:
   - In [ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L1269-L1306) (`Mas-2 #214`, lines 1269, 1304–1305, and Theorem 16.1 line 386), the floor-quotient formula $\chi(I) = \big(\lfloor I/(A+1) \rfloor + \lfloor I/((A+1)(B+1)) \rfloor\big) \bmod 3$ (used in the proof of Theorem 16.1 and in `Mas-2` Step 2 line 1328) is 100% correct, **but** the simplified coordinate formulas $\chi(I) = (b + 2c) \bmod 3$, $(a + b + c) \bmod 3$, and $(b + c) \bmod 3$ stated on lines 386, 1269, and 1304–1305 are **mathematically false** whenever $A + 1 \not\equiv 1 \pmod 3$ or $B + 1 \not\equiv 1 \pmod 3$! For example, in the `Mas-2` sample trace $A = B = C = 1$ ($n_1 = n_2 = n_3 = 2$), multiplying $y^1 \cdot y^1$ ($I = 2$) produces $I + I = 4 \leftrightarrow z^1$ (a false carry from $y$ into $z$), where $(b + 2c) \bmod 3$ gives $1 + 1 \equiv 0 + 2(1) \pmod 3$ and **fails to detect the carry**, whereas the floor-quotient formula gives $1 + 1 = 2 \not\equiv 0 = \lfloor 4/2 \rfloor + \lfloor 4/4 \rfloor \pmod 3$.
   - The exact same false formula $\chi(i_1, i_2, i_3) = (i_1 + i_2 + i_3) \bmod 3$ and a wrong chapter reference (`Chapter 15` instead of `Chapter 16 (§16.3)`) appear in [ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L1172-L1231) (`Mas-2 #234`, lines 1172, 1203, 1231).
2. **[CRITICAL — Hint-vs-Solution Mathematical Contradictions & Raw `"Wait:"` Scratchpad Monologues]**:
   - **`CP-IV.1 (#158)`** ([cp04-part4-pgf-walks-multivariate.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L77-L80) vs. [L552-L564](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L552-L564)): `Hint 3` (line 79) specifies the base case `$dp[0][0] = -1$` for the recurrence $dp_{\text{new}}[j+p_i][r] = dp[j+p_i][r] + dp[j][r-1] - dp[j][r]$. In the Complete Solution (lines 555–558), the text starts with `dp[0][0] = -1`, computes `-1 - 0 = -1? Wait: we want +1 for r = 1, s = 1!`, and corrects it mid-sentence to **`dp[0][0] = +1`**. Thus `Hint 3` has the wrong sign (`-1` instead of `+1`) and the solution contains an unedited `"Wait:"` self-correction monologue.
   - **`Ch 15 Mas-2 (#210)`** ([ch15-1d-lattice-walks-chebyshev-kernel-method.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L1296) vs. [L1326](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L1326)): `Hint 2` (line 1296) states the Chebyshev tree recurrence with base case **`$F_{-1}(z) = 0$`**, whereas the Complete Derivation (line 1326) states **`$F_{-1}(z) = 1$`**. Mathematically, **$F_{-1}(z) = 1$ is right and $F_{-1}(z) = 0$ is wrong** (for $m = 1 \implies k = 0$, empty left subtrees have weight $1$, giving $F_0(z) = \frac{1}{1 - z} = \frac{Q_1(z)}{Q_2(z)}$; setting $F_{-1}(z) = 0$ gives $F_0(z) = 1$, shifting the Chebyshev index by $1$).
   - **`Ch 17 SS-2 (#044)`** ([ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L686)): Line 686 contains a raw parenthetical `(Wait: if all u initially have d^+(u) = d^-(u)...)` inside the formal derivation.
3. **[CRITICAL — Stage 1 Spoiler Violations in `CP-IV` (`cp04-part4-pgf-walks-multivariate.qmd`)]**:
   - **`CP-IV.7 (#243)`** ([L364-L400](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L364-L400)): The Stage 1 problem title (`Asymmetric Fuss–Catalan Diagonal`) and Stage 1 problem statement (line 380: *"by applying the **Furstenberg diagonal residue representation** and the **Global Residue Theorem** (replacing the $p$ fractional small poles with the single large pole)"*) explicitly give away the exact paradigm and theorem before the student even begins blind triage!
   - **`CP-IV.8 (#082)`** ([L440-L460](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L440-L460)): The Stage 1 problem statement (line 440), small-instance walkthrough (lines 447, 452), and `Hint 1` (line 459) explicitly name **"Łukasiewicz walk"**, **"Raney's simple cyclic rotation"**, and **"1D Kernel Method ... one small root"**.
   - **`CP-IV.6 (#058)`** ([L340](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L340)), **`CP-IV.3 (#099)`** ([L175](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L175)), and **`CP-IV.4 (#116)`** ([L236](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L236)): `Hint 1` blocks (which are labeled `Spoiler-Free`) explicitly reveal `first-passage deconvolution F = H_{S \to \mathcal{T}} / H_{\mathcal{T} \to \mathcal{T}}` (`CP-IV.6`) or the additive martingale potential ansatz $\Phi = \sum \phi(a_i)$ with $\mathbb{E}[\Delta \Phi] = +1$ (`CP-IV.3`, `CP-IV.4`).

---

## 2. Checklist Item 1: Exact Problem ID & Assignment Match (`40 / 40` Problems)

### 2.1 Master Verification Table Against `CURRICULUM_ARCHITECTURE.md`

| File & Slot | Assigned Pool ID & Title in `CURRICULUM_ARCHITECTURE.md` | Actual Pool ID & Title in `.qmd` File | Line Range | ID Match & Status |
| :--- | :--- | :--- | :-: | :-: |
| **`Ch 14 SS-1`** | `#115` — **CF 1392H ZS Shuffles Cards** | `#115` — **ZS Shuffles Cards (CF 1392H)** | `L552–L643` | **PASS** |
| **`Ch 14 SS-2`** | `#026` — **ABC 242 Ex Random Painting** | `#026` — **Random Painting (AtCoder ABC 242 Ex)** | `L646–L734` | **PASS** |
| **`Ch 14 Int-1`** | `#156` — **Luogu P4548 [CTSC2006] 歌唱王国** | `#156` — **Singing Kingdom (Luogu P4548 — [CTSC2006] 歌唱王国)** | `L737–L830` | **PASS** |
| **`Ch 14 Int-2`** | `#071` — **AGC 038 E Gachapon** | `#071` — **Gachapon (AtCoder AGC 038 E)** | `L833–L923` | **PASS** |
| **`Ch 14 Adv-1`** | `#148` — **Luogu P3706 [SDOI2017] 硬币游戏** | `#148` — **Coin Game (Luogu P3706 — [SDOI2017] 硬币游戏)** | `L926–L1007` | **PASS** |
| **`Ch 14 Adv-2`** | `#209` — **UOJ 390 [UNR #3] 百鸽笼** | `#209` — **Hundred Pigeon Cages (UOJ 390 — [UNR #3] 百鸽笼)** | `L1010–L1091` | **PASS** |
| **`Ch 14 Mas-1`** | `#039` — **ABC 289 Ex Trio** | `#039` — **Trio (AtCoder ABC 289 Ex)** | `L1094–L1189` | **PASS** |
| **`Ch 14 Mas-2`** | `#113` — **CF 1349D Slime and Biscuits** | `#113` — **Slime and Biscuits (Codeforces 1349D)** | `L1192–L1294` | **PASS** |
| **`Ch 15 SS-1`** | `#105` — **CF 1204E Natasha, Sasha and the Prefix Sums** | `#105` — **Natasha, Sasha and the Prefix Sums (CF 1204E)** | `L525–L609` | **PASS** |
| **`Ch 15 SS-2`** | `#070` — **AGC 021 E Ball Eat Chameleons** | `#070` — **Ball Eat Chameleons (AtCoder AGC 021 E)** | `L612–L707` | **PASS** |
| **`Ch 15 Int-1`** | `#220` — **Luogu P3266 [JLOI2015] 骗我呢** | `#220` — **Don't Lie to Me (Luogu P3266 — [JLOI2015] 骗我呢)** | `L710–L808` | **PASS** |
| **`Ch 15 Int-2`** | `#140` — **CF Gym 103415K / yukicoder 1341 Gambler's Walk** | `#140` — **Asymmetric $+1, -2$ Gambler's Walk (CF Gym 103415K / yukicoder 1341)** | `L811–L904` | **PASS** |
| **`Ch 15 Adv-1`** | `#128` — **CF 1810G The Maximum Prefix** | `#128` — **The Maximum Prefix (Codeforces 1810G)** | `L907–L1002` | **PASS** |
| **`Ch 15 Adv-2`** | `#134` — **CF 1967E2 Again Counting Arrays** | `#134` — **Again Counting Arrays (Codeforces 1967E2)** | `L1005–L1136` | **PASS** |
| **`Ch 15 Mas-1`** | `#076` — **AGC 070 C No Streak** | `#076` — **No Streak (AtCoder AGC 070 C)** | `L1139–L1261` | **PASS** |
| **`Ch 15 Mas-2`** | `#210` — **UOJ 424 count (Cartesian / Left-Depth Trees)** | `#210` — **count / Cartesian & Left-Depth Bounded Trees (UOJ 424)** | `L1264–L1375` | **PASS** |
| **`Ch 16 SS-1`** | `#048` — **ARC 012 D Don't Step on the Threshold!** | `#048` — **Don't Step on the Threshold! (AtCoder ARC 012 D)** | `L685–L765` | **PASS** |
| **`Ch 16 SS-2`** | `#129` — **CF 1821F Timber** | `#129` — **Timber (Codeforces 1821F)** | `L768–L856` | **PASS** |
| **`Ch 16 Int-1`** | `#025` — **ABC 240 G Teleporting Takahashi** | `#025` — **Teleporting Takahashi (AtCoder ABC 240 G)** | `L859–L929` | **PASS** |
| **`Ch 16 Int-2`** | `#232` — **QOJ 4815 2D Bostan–Mori / Implicit Tree** | `#232` — **2D Rational Bostan–Mori & Small-Prime Implicit Tree (QOJ 4815)** | `L932–L1014` | **PASS** |
| **`Ch 16 Adv-1`** | `#237` — **yukicoder 1080 Delannoy / Chebyshev Sum** | `#237` — **Delannoy & Chebyshev Rational Diagonal Sum (yukicoder 1080)** | `L1017–L1089` | **PASS** |
| **`Ch 16 Adv-2`** | `#074` — **AGC 058 D Yet Another ABC String** | `#074` — **Yet Another ABC String (AtCoder AGC 058 D)** | `L1092–L1175` | **PASS** |
| **`Ch 16 Mas-1`** | `#240` — **yukicoder 1783 Digits-Sum-Mod-10 Convolution** | `#240` — **Digits-Sum-Mod-10 Convolution (yukicoder 1783)** | `L1178–L1263` | **PASS** |
| **`Ch 16 Mas-2`** | `#214` — **UOJ 596 [集训队互测2021] 三维立体混元劲** | `#214` — **3D Connected Hypergraphs (UOJ 596 — [集训队互测2021] 三维立体混元劲)** | `L1266–L1373` | **PASS** |
| **`Ch 17 SS-1`** | `#154` — **Luogu P4456 [CQOI2018] 交错序列** | `#154` — **Alternating Sequences (Luogu P4456 — [CQOI2018] 交错序列)** | `L538–L625` | **PASS** |
| **`Ch 17 SS-2`** | `#044` — **ABC 336 G 16 Integers** | `#044` — **16 Integers (AtCoder ABC 336 G)** | `L628–L715` | **PASS** |
| **`Ch 17 Int-1`** | `#228` — **LOJ 6671 Unlabeled Phylogenetic Trees** | `#228` — **Unlabeled Phylogenetic Trees (LOJ 6671)** | `L718–L802` | **PASS** |
| **`Ch 17 Int-2`** | `#219` — **LOJ 3398 带加强和多项木** | `#219` — **Strengthened Multi-Type Trees (LOJ 3398 — 带加强和多项木)** | `L805–L904` | **PASS** |
| **`Ch 17 Adv-1`** | `#015` — **`fps_24_v` 12 Directions** | `#015` — **12 Directions (`fps_24_v`)** | `L907–L988` | **PASS** |
| **`Ch 17 Adv-2`** | `#204` — **Luogu P7599 [APIO2021] 雨林跳跃** | `#204` — **Coupled Bipartite Tree Enumeration (Luogu P7599 / 2021 CoE-II E 数树)** | `L991–L1069` | **SEE §2.2** |
| **`Ch 17 Mas-1`** | `#138` — **CF Gym 102538F 3D Walk / Quarter Plane** | `#138` — **Quarter-Plane Tandem & Kreweras Walks (CF Gym 102538F / 102586J)** | `L1072–L1156` | **PASS** |
| **`Ch 17 Mas-2`** | `#234` — **QOJ 8048 Good–Lagrange Multivariate** | `#234` — **3-Type Directed Arborescences & Multivariate Good–Lagrange (QOJ 8048 / UOJ 596)** | `L1159–L1258` | **SEE §2.2** |
| **`CP-IV.1`** | `#158` — **Luogu P4707 重返现世** | `#158` — **Return to the World (重返现世, Luogu P4707)** | `L31–L82`, `L529–L582` | **PASS** |
| **`CP-IV.2`** | `#169` — **Luogu P5326 [ZJOI2019] 开关** | `#169` — **Switches (`[ZJOI2019] 开关`, Luogu P5326)** | `L85–L138`, `L585–L633` | **PASS** |
| **`CP-IV.3`** | `#099` — **CF 1025G Company Acquisitions** | `#099` — **Company Acquisitions (CF 1025G)** | `L141–L200`, `L636–L662` | **PASS** |
| **`CP-IV.4`** | `#116` — **CF 1479E School Clubs** | `#116` — **School Clubs (CF 1479E)** | `L203–L260`, `L665–L704` | **PASS** |
| **`CP-IV.5`** | `#194` — **Luogu P6633 [ZJOI2020] 抽卡** | `#194` — **Card Drawing (`[ZJOI2020] 抽卡`, Luogu P6633)** | `L263–L311`, `L707–L744` | **PASS** |
| **`CP-IV.6`** | `#058` — **ARC 136 F Flip Cells** | `#058` — **Flip Cells (AtCoder ARC 136 F)** | `L314–L361`, `L747–L791` | **PASS** |
| **`CP-IV.7`** | `#243` — **yukicoder 2104 Fuss–Catalan Diagonal** | `#243` — **Asymmetric Fuss–Catalan Diagonal (yukicoder 2104 / CF 1666H)** | `L364–L421`, `L794–L838` | **PASS** |
| **`CP-IV.8`** | `#082` — **Toyota 2023 Spring Final E Replace Digits** | `#082` — **Replace Digits (Toyota 2023 Spring Final E)** | `L424–L480`, `L841–L886` | **PASS** |

---

### 2.2 Special Check on `Ch 17 Adv-2 (#204)` and `Ch 17 Mas-2 (#234)`

We cross-checked `Ch 17 Adv-2 (#204)` ([ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L991-L1069)) and `Ch 17 Mas-2 (#234)` ([L1159-L1258](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L1159-L1258)) against `CURRICULUM_ARCHITECTURE.md` (lines 864, 866), `PROBLEM_CURATION.md` (lines 505, 507, 1249, 1279), and `problem_archive.md` (lines 34, 1553–1586):

1. **`Ch 17 Adv-2 (#204)` (`L991–L1069`)**:
   - **Self-Containment & Unified Statement Check**: The problem in `ch17` has a **single, unified, self-contained mathematical statement** (`L996–L1005`: coupled bipartite system $F_1(x_1, x_2) = x_1 \Phi_1(F_2(x_1, x_2))$, $F_2(x_1, x_2) = x_2 \Phi_2(F_1(x_1, x_2))$, computing $[x_1^{n_1} x_2^{n_2}] F_1^{r_1} F_2^{r_2} \bmod 998244353$ via Corollary 17.1 Bipartite Rank-1 Good–Lagrange Collapse), a verified $N \le 4$ sample trace (`L1007–L1012`), 3 progressive hints, and a complete proof.
   - **Title / Metadata Discrepancy to Clean Up**:
     - In `CURRICULUM_ARCHITECTURE.md` (`L864`), `#204` was labeled `Luogu P7599 — [APIO2021] 雨林跳跃 | 4B#16 | 2D Dominance Lattice Walk + Bivariate Kernel Method` (note that actual APIO 2021 Rainforest Jumps is a tree-jumping binary lifting problem, while in `problem_archive.md` `L1553` `4B#16` is `ABC 336 G` and `#203 Luogu P7592` is `2021 CoE-II E 数树`).
     - Because `ch17` `L991–L993` writes `### Advanced 2 (#204) — Coupled Bipartite Tree Enumeration (Luogu P7599 / 2021 CoE-II E 数树)` and `**Source**: Luogu P7599 / Bipartite Good–Lagrange Synthesis`, this hybrid contest citation (`Luogu P7599 / 2021 CoE-II E`) creates confusion with `#203` (`Ch 11 Mas-2`).
     - **Recommendation**: Either keep the clean Bipartite Rank-1 Good–Lagrange problem in `ch17` `L991–L1069` and remove the misleading `Luogu P7599` label from the source line (citing `#204 — Coupled Bipartite Tree Enumeration (Bipartite Good–Lagrange Synthesis)`), OR if the 2D Dominance Lattice Walk + Bivariate Kernel Method from `CURRICULUM_ARCHITECTURE.md` `L864` is desired, use the drop-in replacement provided in Section 4.4 below.

2. **`Ch 17 Mas-2 (#234)` (`L1159–L1258`)**:
   - **Self-Containment & Unified Statement Check**: The problem in `ch17` has a **single, unified, self-contained mathematical statement** (`L1164–L1173`: 3-type labeled rooted arborescences with out-degree weight factors $\Phi_i(u_1, u_2, u_3) = \exp(a_{i,1}u_1 + a_{i,2}u_2 + a_{i,3}u_3)$ and general polynomial $\Phi_i$, extracting $[x_1^{k_1} x_2^{k_2} x_3^{k_3}] F_1(x_1, x_2, x_3)$ via $3 \times 3$ Multivariate Good–Lagrange Jacobian $\det(I_3 - J_{\Phi}(u))$), with a verified $N=3$ sample trace (`L1175–L1182`).
   - **Two Bugs Found in `Ch 17 Mas-2 (#234)`**:
     1. **Dual Source Tag (`QOJ 8048 / UOJ 596`)**: Lines 1159 and 1161 cite `QOJ 8048 / UOJ 596`. However, `UOJ 596` (`[集训队互测2021] 三维立体混元劲`) is Pool ID `#214`, which is already the dedicated `Mas-2` problem of **Chapter 16**! Furthermore, in `problem_archive.md` `L1584`, the 3D Multivariate Good–Lagrange digraph/arborescence problem is `QOJ 6184 / 6505 ([CTT2022] 欧拉? 欧拉!)` (`Wave 4B#31`) alongside `QOJ 8048` in `CURRICULUM_ARCHITECTURE.md` `L866`. Drop `/ UOJ 596` from the title and source line of `#234`.
     2. **False $\chi$-Grading Formula & Wrong Chapter Reference (`L1172, L1203, L1231`)**: Lines 1172, 1203, and 1231 refer to *"the $\chi$-twisted Kronecker FFT (Chapter 15) with $\chi(i_1, i_2, i_3) = (i_1 + i_2 + i_3) \bmod 3$"*. First, Twisted Kronecker Convolution is **Chapter 16 (§16.3)**, not Chapter 15! Second, $\chi(i_1, i_2, i_3) = (i_1 + i_2 + i_3) \bmod 3$ is **mathematically wrong** for general mixed-radix dimensions $(k_1+1, k_2+1, k_3+1)$; the exact carry-detection grading from §16.3 is $\chi(I) = \big(\lfloor I/(k_1+1) \rfloor + \lfloor I/((k_1+1)(k_2+1)) \rfloor\big) \bmod 3$.

---

## 3. Detailed File-by-File Audit & Drop-In Fixes (Checklist Items 2, 3, and 4)

### 3.1 Chapter 14: `chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd`

#### Overview of the 8 Problems (`L545–L1304`)
- **`SS-1 (#115, CF 1392H)`** (`L552–L643`): Single authoritative statement (`L560–L565`), verified $n=2, m=1$ sample trace ($\mathbb{E}[T] = 5$, `L567–L574`), 3 progressive hints (`L579–L603`), complete derivation with `Algorithm Contract` (`L605–L642`).
- **`SS-2 (#026, ABC 242 Ex)`** (`L646–L734`): Single authoritative statement (`L654–L658`), verified $N=3, M=2$ sample trace ($\mathbb{E}[T] = 7/2$, `L660–L664`), 3 progressive hints (`L668–L695`), complete derivation with `Algorithm Contract` (`L697–L733`).
- **`Int-1 (#156, Luogu P4548)`** (`L737–L830`): Single authoritative statement (`L745–L749`), verified $\Sigma=2, S=(1, 2, 1)$ sample trace ($\mathbb{E}[T] = 10, \operatorname{Var}(T) = 54$, `L751–L755`), 3 progressive hints (`L759–L784`), complete derivation with `Algorithm Contract` (`L786–L829`).
- **`Int-2 (#071, AGC 038 E)`** (`L833–L923`): Single authoritative statement (`L841–L845`), verified $n=2, (A_1, B_1)=(1, 2), (A_2, B_2)=(1, 1)$ sample trace ($\mathbb{E}[T] = 7/2$, `L847–L853`), 3 progressive hints (`L857–L882`), complete derivation with `Algorithm Contract` (`L884–L922`).
- **`Adv-1 (#148, Luogu P3706)`** (`L926–L1007`): Single authoritative statement (`L934–L938`), verified $n=2, m=2, S_1=\mathtt{HT}, S_2=\mathtt{TH}$ sample trace ($P_1 = P_2 = 1/2$, `L940–L946`), 3 progressive hints (`L950–L970`), complete derivation with `Algorithm Contract` (`L972–L1006`).
- **`Adv-2 (#209, UOJ 390)`** (`L1010–L1091`): Single authoritative statement (`L1018–L1022`), verified $n=2, a=(2, 2)$ sample trace ($P_1 = P_2 = 1/2$, `L1024–L1029`), 3 progressive hints (`L1033–L1057`), complete derivation with `Algorithm Contract` (`L1059–L1090`).
- **`Mas-1 (#039, ABC 289 Ex)`** (`L1094–L1189`): Single authoritative statement (`L1102–L1106`), verified $A=0, B=1, C=1, T=1$ sample trace ($\mathbb{E}[\tau] = 4$, `L1108–L1112`), 3 progressive hints (`L1116–L1140`), complete derivation with `Algorithm Contract` (`L1142–L1188`).
- **`Mas-2 (#113, CF 1349D)`** (`L1192–L1294`): Single authoritative statement (`L1200–L1205`), verified $n=2, a=(1, 1)$ sample trace ($\mathbb{E}[T] = 1$, `L1207–L1210`), 3 progressive hints (`L1214–L1239`), complete derivation with `Algorithm Contract` (`L1241–L1293`).

#### Specific Issues & Drop-In Replacements for `Ch 14`

1. **[MINOR — Broken Internal `.qmd` Link on Line 1298]**:
   - **Location**: [ch14-pgf-stopping-times-renewal-poisson-martingales.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd#L1298)
   - **Issue**: Links to `(ch15-lattice-walks-reflection-kernel-method.qmd)`, which does not exist; the actual filename is `(ch15-1d-lattice-walks-chebyshev-kernel-method.qmd)`.
   - **Drop-In Fix (`L1298`)**:
     ```markdown
     In **[Chapter 15: 1D Lattice Walks, Reflection Principle, Chebyshev Rational Functions & The Kernel Method](ch15-1d-lattice-walks-chebyshev-kernel-method.qmd)**, we introduce a spatial boundary (such as a floor $y \ge 0$ or a strip $0 \le y \le H$) and study how algebraic roots of the **kernel equation** $K(x, y) = 1 - x S(y) = 0$ annihilate boundary unknowns.
     ```

2. **[MINOR — `Hint 1` Gives Away Explicit Formulas / Theorem Names in `SS-1`, `SS-2`, `Int-1`, `Int-2`, `Mas-1`, `Mas-2`]**:
   - **Locations**: `L580–L584` (`SS-1`), `L669–L673` (`SS-2`), `L760–L763` (`Int-1`), `L858–L862` (`Int-2`), `L1117–L1121` (`Mas-1`), `L1215–L1220` (`Mas-2`).
   - **Issue**: To preserve progressive pedagogy (`Hint 1` = structural observation without naming the theorem or formula; `Hint 2` = paradigm & algebraic equation; `Hint 3` = extraction & complexity), move the explicit formula / theorem name from `Hint 1` to `Hint 2`:
     - **`SS-1` (`L582`)**: Replace *"By Wald's Identity, $\mathbb{E}[T] = \mathbb{E}[R] \cdot \mathbb{E}[L]$"* in `Hint 1` with: *"Decompose the game into rounds separated by joker draws. Since the deck is fully reshuffled after every joker, each round has the exact same expected length $\mathbb{E}[L]$, and the event that a round reveals a new number depends only on how many numbers are currently uncollected."*
     - **`SS-2` (`L671–L673`) & `Int-2` (`L860–L862`)**: Remove the explicit Min–Max IE sum $\mathbb{E}[\max_i T_i] = \sum_{\emptyset \neq S} (-1)^{|S|-1} \mathbb{E}[\min_{i \in S} T_i]$ from `Hint 1` (since `Hint 2` already states it), leaving the structural prompt: *"Stopping when every target has reached its threshold is the maximum $\max_i T_i$ of individual completion times, whereas the minimum $\min_{i \in S} T_i$ over a subset $S$ only cares about the first time something happens inside $S$."*
     - **`Int-1` (`L762`)**: Remove `"Apply Theorem 14.3 (§14.3) and Proposition 14.1 (§14.1):"` and the variance formula from `Hint 1`, asking instead: *"What happens if you place a bet of $1$ coin on a fresh pattern prefix at every step $t$, multiplying your stake by $\Sigma$ whenever the next character matches? How is the terminal payout at $t = T$ related to the border lengths of $S$?"*
     - **`Mas-1` (`L1119`)**: Remove `"Apply the Renewal First-Passage Formula $F(z) = H_{\text{hit}}(z) / H_{\text{return}}(z)$ from §14.3:"` from `Hint 1`, asking instead: *"Can you first compute the probability $h_n$ that all three walkers stand at the same coordinate at step $n$ without stopping earlier, and relate that unconstrained sequence to the first meeting time $\tau$?"*
     - **`Mas-2` (`L1217–L1219`)**: Remove `"This is the canonical symmetric multi-urn process of §14.4 Part C. Seek an additively separable potential... By Doob's Optional Stopping Theorem"` from `Hint 1`, asking instead: *"The state is a partition $a_1 + \dots + a_n = N$ of $N$ biscuits among $n$ symmetric slimes. Because all slimes are symmetric, what happens if we assign a score $f(a_i)$ to each slime based only on how many biscuits it currently holds?"*

---

### 3.2 Chapter 15: `chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`

#### Overview of the 8 Problems (`L518–L1375`)
- **`SS-1 (#105, CF 1204E)`** (`L525–L609`): Single authoritative statement (`L533–L536`), verified $n=2, m=2$ sample trace (sum $= 8$, `L538–L548`), 3 progressive hints (`L552–L574`), complete derivation (`L576–L608`).
- **`SS-2 (#070, AGC 021 E)`** (`L612–L707`): Single authoritative statement (`L620–L625`), verified $N=2, K=3$ sample trace (answer $= 5$, `L627–L634`), 3 progressive hints (`L638–L664`), complete derivation (`L666–L706`).
- **`Int-1 (#220, Luogu P3266)`** (`L710–L808`): Single authoritative statement (`L718–L724`), verified $n=1, m=2$ sample trace (answer $= 10$, `L726–L732`), 3 progressive hints (`L736–L763`), complete derivation (`L765–L807`).
- **`Int-2 (#140, CF Gym 103415K / yukicoder 1341)`** (`L811–L904`): Single authoritative statement (`L819–L824`), verified $N=3$ sample trace (`L826–L833`), 3 progressive hints (`L837–L861`), complete derivation (`L863–L903`).
- **`Adv-1 (#128, CF 1810G)`** (`L907–L1002`): Single authoritative statement (`L915–L920`), verified $n=2, p=(1/2, 1/2), h=(1, 2, 4)$ sample trace (`L922–L927`), 3 progressive hints (`L931–L957`), complete derivation (`L959–L1001`).
- **`Adv-2 (#134, CF 1967E2)`** (`L1005–L1136`): Single authoritative statement (`L1013–L1021`), verified $n=2, m=2, b_0=0$ sample trace (answer $= 7$, `L1023–L1031`), 3 progressive hints (`L1035–L1063`), complete derivation (`L1065–L1135`).
- **`Mas-1 (#076, AGC 070 C)`** (`L1139–L1261`): Single authoritative statement (`L1147–L1153`), verified minimal non-trivial $N=5, A=2, B=2, X=1$ sample trace (answer $= 2$, `L1155–L1163`), 3 progressive hints (`L1167–L1199`), complete derivation (`L1201–L1260`).
- **`Mas-2 (#210, UOJ 424)`** (`L1264–L1375`): Single authoritative statement (`L1272–L1276`), verified $n=3, m=2$ sample trace (answer $= 4$, `L1278–L1283`), 3 progressive hints (`L1287–L1314`), complete derivation (`L1316–L1374`).

#### Specific Issues & Drop-In Replacements for `Ch 15`

1. **[CRITICAL — Mathematical Contradiction Between `Hint 2` (`L1296`) and Complete Derivation (`L1326`) in `Mas-2 (#210, UOJ 424)`]**:
   - **Locations**: [ch15-1d-lattice-walks-chebyshev-kernel-method.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L1296) (`Hint 2`) vs. [L1326](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L1326) (`Complete Derivation`).
   - **Issue**:
     - `Hint 2` (`L1296`) writes:
       $$F_k(z) = 1 + z F_{k-1}(z) F_k(z) \Longrightarrow F_k(z) = \frac{1}{1 - z F_{k-1}(z)} \quad (k \ge 0,\ F_{-1}(z) = 0).$$
     - `Complete Derivation` (`L1326`) writes:
       $$F_k(z) = 1 + z F_{k-1}(z) F_k(z) \Longrightarrow F_k(z) = \frac{1}{1 - z F_{k-1}(z)}, \qquad F_{-1}(z) = 1.$$
     - **Mathematical Audit**: When $m = 1$, $k = m - 1 = 0$, every vertex has left-depth $\le 0$, which means every left subtree must be **empty** (having $1$ valid configuration of size $0$, i.e., $F_{-1}(z) = 1$), while right subtrees can be arbitrary right-chains! Thus $F_0(z) = \frac{1}{1 - z \cdot 1} = \frac{1}{1 - z} = \frac{Q_1(z)}{Q_2(z)}$ ($1$ tree for every $n \ge 0$). If $F_{-1}(z) = 0$ as claimed in `Hint 2`, then $F_0(z) = 1$, which falsely claims there are $0$ valid trees for $n \ge 1, m = 1$ and shifts the Chebyshev index $Q_{k+1}/Q_{k+2}$ down by $1$!
   - **Drop-In Fix for `Hint 2` (`L1294–L1301`)**:
     ```markdown
     <details>
     <summary><strong>Hint 2 — Key Generating Function / Algebraic Formulation</strong></summary>

     Let $F_k(z)$ be the OGF of binary trees whose maximum left-depth is at most $k = m - 1$ (where an empty tree has $F_k(0) = 1$, and for $k = -1$ only the empty tree of size $0$ is allowed, so $F_{-1}(z) = 1$). Decomposing at the root (whose left subtree has left-depth $\le k - 1$ and right subtree has left-depth $\le k$) gives the continued-fraction recurrence:
     $$F_k(z) = 1 + z F_{k-1}(z) F_k(z) \Longrightarrow F_k(z) = \frac{1}{1 - z F_{k-1}(z)} \quad (k \ge 0,\ F_{-1}(z) = 1).$$
     By §15.2 (`Theorem 15.3`), this continued fraction evaluates to the shifted Chebyshev rational function:
     $$F_{m-1}(z) = \frac{Q_m(z)}{Q_{m+1}(z)}, \qquad \text{where } Q_k(z) = \sum_{j=0}^{\lfloor k/2 \rfloor} (-1)^j \binom{k - j}{j} z^j.$$

     </details>
     ```

2. **[MODERATE — Missing Explicit `#### Algorithm Contract` Subsections in All 8 `Ch 15` Solutions]**:
   - **Locations**: `L605–L607` (`SS-1`), `L702–L705` (`SS-2`), `L803–L806` (`Int-1`), `L899–L902` (`Int-2`), `L997–L1000` (`Adv-1`), `L1131–L1134` (`Adv-2`), `L1256–L1259` (`Mas-1`), `L1369–L1373` (`Mas-2`).
   - **Issue**: Whereas `Ch 14`, `Ch 16`, `Ch 17`, and `CP-IV` include an explicit `#### Algorithm Contract` block at the end of every problem solution, `Ch 15` places two bullets (`- **Verification on ...**` and `- **Complexity**: ...`) at the bottom of `#### Step 3`.
   - **Drop-In Fix**: Add `#### Algorithm Contract` right before the verification/complexity bullets in each of the 8 `Ch 15` problems, stating **Input**, **Output**, **Algebraic Preconditions** (e.g., prime modulus $p > N + M$ for factorial inverses, or $p = 998244353$ for NTT / Bostan–Mori), and **Time & Space Complexity**.

3. **[MINOR — Forward-Reference Terminology (`Transposition Principle`) in `Ch 15 Adv-1 (#128, CF 1810G)` (`L929, L963, L989–L995`)]**:
   - **Locations**: [ch15-1d-lattice-walks-chebyshev-kernel-method.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L929-L995)
   - **Issue**: The solution invokes the **Transposition Principle** ($T_k^\top \cdots T_1^\top \mathbf{h}$), which is formally taught in Part V (`Ch 20`). Because the recurrence $dp_i[m] = p_i dp_{i-1}[m+1] + q_i dp_{i-1}[\max(0, m-1)]$ has a 100% self-contained probabilistic meaning (namely, the conditional expected value of $h(\text{prefix max of } i\text{-step walk})$ starting from initial prefix margin $m \ge 0$), frame Step 3 primarily as **Backward / Initial-Margin Conditional Expectation DP (Lindley's Duality)**, and mention the linear-algebraic transpose $T_i^\top$ only as an elementary matrix-vector associative reordering $\mathbf{e}_0^\top (T_1 \cdots T_k \mathbf{h}) = ((\cdots(\mathbf{h}^\top T_k^\top)\cdots) T_1^\top)_0$ without relying on `Ch 20`.

---

### 3.3 Chapter 16: `chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`

#### Overview of the 8 Problems (`L679–L1373`)
- **`SS-1 (#048, ARC 012 D)`** (`L685–L765`): Single authoritative statement (`L693–L697`), verified $T=2, (x,y)=(1,0)$ sample trace (answer $= 2$, `L699–L703`), 3 progressive hints (`L707–L729`), complete derivation + `Algorithm Contract` (`L731–L764`).
- **`SS-2 (#129, CF 1821F)`** (`L768–L856`): Single authoritative statement (`L776–L782`), verified $n=4, m=1, k=1$ sample trace (answer $= 6$, `L784–L789`), 3 progressive hints (`L793–L817`), complete derivation + `Algorithm Contract` (`L819–L855`).
- **`Int-1 (#025, ABC 240 G)`** (`L859–L929`): Single authoritative statement (`L867–L870`), verified $N=2, (X,Y,Z)=(1,1,0)$ sample trace (answer $= 2$, `L872–L877`), 3 progressive hints (`L881–L901`), complete derivation + `Algorithm Contract` (`L903–L928`).
- **`Int-2 (#232, QOJ 4815)`** (`L932–L1014`): Single authoritative statement (`L940–L946`), verified $n=2, m=1$ sample trace (`L948–L951`), 3 progressive hints (`L955–L976`), complete derivation + `Algorithm Contract` (`L978–L1013`).
- **`Adv-1 (#237, yukicoder 1080)`** (`L1017–L1089`): Has a parenthetical hedge (`L1021`) and an abbreviated sample trace (`L1026–L1028`) referencing §16.4 — **flagged below**.
- **`Adv-2 (#074, AGC 058 D)`** (`L1092–L1175`): Single authoritative statement (`L1100–L1104`), verified $A=B=C=1$ sample trace (answer $= 3$, `L1106–L1110`), 3 progressive hints (`L1114–L1136`), complete derivation + `Algorithm Contract` (`L1138–L1174`).
- **`Mas-1 (#240, yukicoder 1783)`** (`L1178–L1263`): Single authoritative statement (`L1186–L1193`), verified $D=2, M=2, K=2$ sample trace (`L1195–L1200`), 3 progressive hints (`L1204–L1226`), complete derivation + `Algorithm Contract` (`L1228–L1262`).
- **`Mas-2 (#214, UOJ 596)`** (`L1266–L1373`): Single authoritative statement (`L1274–L1281`), verified $A=B=C=1$ sample trace (answer $= 29$, `L1283–L1289`), 3 progressive hints (`L1293–L1316`), complete derivation + `Algorithm Contract` (`L1318–L1372`). **Contains the false second equality in the $\chi(I)$ formula (`L1269, L1304–L1305`) — flagged below.**

#### Specific Issues & Drop-In Replacements for `Ch 16`

1. **[CRITICAL — Mathematical Error in Second Equality of Carry-Grading Formula $\chi(I)$ (`L386, L1269, L1304–L1305`)]**:
   - **Locations**:
     - [ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L386) (Theorem 16.1 in §16.3)
     - [ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L1269) (`Mas-2 #214` Key Technique header)
     - [ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L1304-L1305) (`Mas-2 #214` Hint 2)
   - **Mathematical Audit**:
     For mixed-radix encoding $I(i_1, \dots, i_d) = \sum_{r=1}^d i_r N_{r-1}$ with $N_r = n_1 n_2 \cdots n_r$, the quotient $\lfloor I / N_r \rfloor$ is:
     $$\left\lfloor \frac{I}{N_r} \right\rfloor = i_{r+1} + i_{r+2} n_{r+1} + i_{r+3} n_{r+1} n_{r+2} + \dots$$
     Summing $\lfloor I / N_r \rfloor$ over $r = 1, \dots, d - 1$ satisfies:
     $$\left\lfloor \frac{I + J}{N_r} \right\rfloor - \left\lfloor \frac{I}{N_r} \right\rfloor - \left\lfloor \frac{J}{N_r} \right\rfloor = c_r \in \{0, 1\},$$
     where $c_r$ is the carry out of digit $r$. Therefore, the floor-quotient sum:
     $$\chi(I) := \left( \sum_{r=1}^{d-1} \left\lfloor \frac{I}{N_r} \right\rfloor \right) \bmod d$$
     is **100% mathematically exact** for all grid dimensions $(n_1, \dots, n_d)$!
     **HOWEVER**, on line 386 (`Theorem 16.1`) and line 1304 (`Mas-2 Hint 2`), the text writes:
     $$\chi(I) := \left(\sum_{r=1}^{d-1} \left\lfloor \frac{I}{N_r} \right\rfloor\right) \bmod d = \left(\sum_{r=2}^d (r - 1) i_r\right) \bmod d \qquad \text{and} \qquad \chi(I) = (b + 2c) \bmod 3.$$
     That second equality is **FALSE** unless $n_r \equiv 1 \pmod d$ for all $r \ge 2$! Indeed, for $d = 3$ with $I = a + b n_1 + c n_1 n_2$:
     $$\left\lfloor \frac{I}{n_1} \right\rfloor + \left\lfloor \frac{I}{n_1 n_2} \right\rfloor = (b + c n_2) + c = b + (n_2 + 1) c,$$
     which equals $b + 2c \pmod 3$ **only when $n_2 \equiv 1 \pmod 3$**! When $n_2 = 2$ (as in the `Mas-2` sample trace $A = B = C = 1 \implies n_1 = n_2 = n_3 = 2$), $b + (n_2 + 1)c = b + 3c \equiv b \pmod 3 \neq b + 2c \pmod 3$, and using $(b + 2c) \bmod 3$ fails to detect carries from $y$ into $z$ (since $y^1 \cdot y^1 \mapsto z^1$ has $(b+2c) = 1+1 = 2$ on the left and $0 + 2(1) = 2$ on the right!). Even worse, line 1269 writes $\chi(I) = (b + c) \bmod 3$ and line 1305 writes $(a + b + c) \bmod 3$, which don't even detect carries from $x$ into $y$!
   - **Drop-In Fixes**:
     - **Theorem 16.1 (`L386`)**: Remove the false second equality, keeping only the exact floor-quotient definition:
       ```markdown
       $$\chi(I) := \left( \sum_{r=1}^{d-1} \left\lfloor \frac{I}{N_r} \right\rfloor \right) \bmod d.$$
       ```
     - **`Mas-2` Key Technique (`L1269`)**:
       ```markdown
       * **Key Technique**: 3D Radial Derivation $\mathfrak{D} = x\partial_x + y\partial_y + z\partial_z$ on $\ln G$ + Twisted 3D Kronecker Convolution ($\chi(I) = \big(\lfloor I/(A+1) \rfloor + \lfloor I/((A+1)(B+1)) \rfloor\big) \bmod 3$).
       ```
     - **`Mas-2` Hint 2 (`L1304–L1306`)**:
       ```markdown
       Pack $(a, b, c) \mapsto I = a + b(A+1) + c(A+1)(B+1)$ of total length $L = (A+1)(B+1)(C+1)$ and use the **Twisted 3D Kronecker Grading** (§16.3):
       $$\chi(I) = \left(\left\lfloor \frac{I}{A+1} \right\rfloor + \left\lfloor \frac{I}{(A+1)(B+1)} \right\rfloor\right) \bmod 3.$$
       Because any false carry out of $x$ or $y$ increments $\lfloor I/(A+1) \rfloor + \lfloor I/((A+1)(B+1)) \rfloor$ by $c_1 + c_2 \in \{1, 2\} \not\equiv 0 \pmod 3$, restricting to $\chi(I) + \chi(J) \equiv \chi(I+J) \pmod 3$ eliminates all wrap-around carries with zero zero-padding!
       ```

2. **[MODERATE — Parenthetical Hedge & Abbreviated Sample Trace in `Ch 16 Adv-1 (#237, yukicoder 1080)` (`L1021–L1028`)]**:
   - **Location**: [ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L1021-L1028)
   - **Issue**: Line 1021 has a parenthetical hedge `(alongside the Chebyshev / diagonal rational sums in yukicoder 1080...)` and lines 1026–1028 abbreviate the sample trace by saying `As traced in §16.4, for a = b = c = 1 we obtain... (1, 3, 13, 63)`.
   - **Drop-In Fix for `L1020–L1029`**:
     ```markdown
     **Problem Statement.** Given step weights $a, b, c \in \mathbb{F}_p$ (with $p = 998244353$) and an integer $N \le 2 \times 10^5$, consider weighted Delannoy paths from $(0, 0)$ to $(n, n)$ where each horizontal step $(1, 0)$ has weight $a$, each vertical step $(0, 1)$ has weight $b$, and each diagonal step $(1, 1)$ has weight $c$. Compute the diagonal generating function coefficients
     $$d_n = [x^n y^n] \frac{1}{1 - a x - b y - c x y}$$
     for all $n = 0, 1, \dots, N$ modulo $998244353$ in $O(N \log N)$ time (and note the $O(N)$ D-finite recurrence previewed for Part V).

     *Small-instance trace ($a = 1, b = 1, c = 1, N = 2$)*:
     - $n = 0$: $1$ empty path at $(0, 0) \implies d_0 = 1$.
     - $n = 1$: From $(0, 0)$ to $(1, 1)$, we have $(1,0)\to(1,1)$, $(0,1)\to(1,1)$, or the single diagonal step $(1,1)$, giving $d_1 = 1 + 1 + 1 = 3$.
     - $n = 2$: Summing over the number $k \in \{0, 1, 2\}$ of diagonal steps $(1, 1)$ gives $\sum_{k=0}^2 \binom{2}{k}\binom{4-k}{2} = \binom{4}{2} + 2\binom{3}{2} + \binom{2}{2} = 6 + 6 + 1 = 13 = d_2$.
     ```

3. **[MINOR — 4 Broken Prerequisite `.qmd` Links in `Ch 16` Header (`L8–L11`)]**:
   - **Location**: [ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L8-L11)
   - **Drop-In Fix (`L8–L11`)**:
     ```markdown
     - [Chapter 5: Rational Generating Functions, Bostan–Mori & Berlekamp–Massey](ch05-rational-bostan-mori-berlekamp-massey.qmd) (univariate Bostan–Mori parity splitting $Q(x)Q(-x)$)
     - [Chapter 3: Formal Logarithm, Exponential & Radix-2 Newton Iteration](ch03-ln-exp-newton-radix2-lifting.qmd) and [Chapter 10: Implicit Equations, Multivariate Newton & Relaxed Convolution](ch10-implicit-equations-multivariate-newton-relaxation.qmd) (Newton iteration for $1/F, \ln F, \exp F$)
     - [Chapter 11: Lagrange–Bürmann Inversion, Raney's Lemma & Formal Laurent Residues](ch11-lagrange-inversion-raney-formal-residues.qmd) (formal Laurent residues $[z^{-1}]$ and residue change-of-variables)
     - [Chapter 15: 1D Lattice Walks, Reflection Principle, Chebyshev Rational Functions & The Kernel Method](ch15-1d-lattice-walks-chebyshev-kernel-method.qmd) (small vs. large roots of bivariate kernels $K(x, y) = 0$)
     ```

---

### 3.4 Chapter 17: `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`

#### Overview of the 8 Problems (`L532–L1258`)
- **`SS-1 (#154, Luogu P4456)`** (`L538–L625`): Single authoritative statement (`L543–L549`), verified $N=3, a=1, b=1$ sample trace (answer $= 4$, `L551–L559`), 3 progressive hints (`L563–L584`), complete derivation + `Algorithm Contract` (`L586–L624`).
- **`SS-2 (#044, ABC 336 G)`** (`L628–L715`): Single authoritative statement (`L633–L639`), verified $4$-bit window sample trace (`01010`, answer $= 1$, `L641–L645`), 3 progressive hints (`L649–L670`), complete derivation + `Algorithm Contract` (`L672–L714`). **Contains a raw `"Wait:"` monologue on line 686 — flagged below.**
- **`Int-1 (#228, LOJ 6671)`** (`L718–L802`): Single authoritative statement (`L723–L732`, after trimming parenthetical on `L724`), verified $n=1, 2, 3, 4$ sample trace (`L734–L740`), 3 progressive hints (`L744–L766`), complete derivation + `Algorithm Contract` (`L768–L801`).
- **`Int-2 (#219, LOJ 3398)`** (`L805–L904`): Single authoritative statement (`L810–L819`), verified $n_1=1, n_2=1$ sample trace (`L821–L828`), 3 progressive hints (`L832–L859`), complete derivation + `Algorithm Contract` (`L861–L903`).
- **`Adv-1 (#015, fps_24_v)`** (`L907–L988`): Single authoritative statement (`L912–L923`, after trimming parenthetical on `L915`), verified $N=1, 2$ sample trace (`L925–L931`), 3 progressive hints (`L935–L958`), complete derivation + `Algorithm Contract` (`L960–L987`).
- **`Adv-2 (#204)`** (`L991–L1069`): Audited in §2.2 above; drop-in replacement options provided below.
- **`Mas-1 (#138, CF Gym 102538F)`** (`L1072–L1156`): Single authoritative statement (`L1077–L1083`), verified $N=3$ sample trace (`L1085–L1092`), 3 progressive hints (`L1096–L1120`), complete derivation + `Algorithm Contract` (`L1122–L1155`).
- **`Mas-2 (#234, QOJ 8048)`** (`L1159–L1258`): Audited in §2.2 above; drop-in fix for `L1159–L1235` provided below.

#### Specific Issues & Drop-In Replacements for `Ch 17`

1. **[CRITICAL — Wrong Chapter Reference (`Chapter 15` $\to$ `Chapter 16 (§16.3)`), False $\chi$-Grading Formula, and Duplicate `UOJ 596` Label in `Mas-2 (#234)` (`L1159–L1235`)]**:
   - **Locations**: [ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L1159-L1235) (`L1159, L1161, L1172, L1203, L1231`).
   - **Drop-In Fixes**:
     - **Header & Source (`L1159–L1162`)**:
       ```markdown
       ### Mastery 2 (#234) — 3-Type Directed Arborescences & Multivariate Good–Lagrange (QOJ 8048)

       * **Source**: QOJ 8048 (`4B#30`)
       * **Key Technique**: $3 \times 3$ Multivariate Good–Lagrange Jacobian Determinant $\det(I_3 - J_{\Phi}(u))$ + 3D Twisted Kronecker Convolution (§16.3).
       ```
     - **Statement Part 2 (`L1171–L1173`)**:
       ```markdown
       2. **Part 2 (General Polynomial Degree Factors)**: When $\Phi_1, \Phi_2, \Phi_3$ are general polynomials in $(u_1, u_2, u_3)$, show how to extract $[x_1^{k_1} x_2^{k_2} x_3^{k_3}] F_1(x_1, x_2, x_3)$ in $O(K \log K)$ time (where $K = (k_1+1)(k_2+1)(k_3+1)$) by expanding the $3 \times 3$ Jacobian determinant $\det(I_3 - J_{\Phi}(u))$ and multiplying the resulting 3D series via the **$\chi$-Twisted Kronecker FFT of Chapter 16 (§16.3, Theorem 16.1)** with $\chi(I) = \big(\lfloor I/(k_1+1) \rfloor + \lfloor I/((k_1+1)(k_2+1)) \rfloor\big) \bmod 3$.
       ```
     - **Hint 3 (`L1202–L1204`) & Solution Step 2 (`L1230–L1232`)**: Replace `Chapter 15` with `Chapter 16 (§16.3, Theorem 16.1)` and replace `\chi(i_1, i_2, i_3) = (i_1 + i_2 + i_3) \bmod 3` with `\chi(I) = \big(\lfloor I/(k_1+1) \rfloor + \lfloor I/((k_1+1)(k_2+1)) \rfloor\big) \bmod 3`.

2. **[MODERATE — Raw `"Wait:"` Monologue in `Ch 17 SS-2 (#044, ABC 336 G)` (`L686`)]**:
   - **Location**: [ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L686)
   - **Issue**: Line 686 contains `(Wait: if all u initially have d^+(u) = d^-(u), then s = t can be any vertex in V_{\text{active}}...)`.
   - **Drop-In Fix (`L685–L688`)**:
     ```markdown
     A pair $(s, t) \in V_{\text{active}}^2$ can support an Eulerian trail if and only if $d^+_{\text{aug}}(u) = d^-_{\text{aug}}(u)$ for all $u \in V$. Specifically, if every $u \in V$ initially satisfies $d^+(u) = d^-(u)$, then $s = t$ may be chosen as any vertex in $V_{\text{active}}$; if exactly one vertex has $d^+(u) - d^-(u) = +1$ and one has $d^+(v) - d^-(v) = -1$, then $s = u$ and $t = v$ are uniquely forced; otherwise, no Eulerian trail exists and the answer is $0$.
     ```

3. **[MINOR — Parenthetical Variant Mentions in `Ch 17 Int-1 (#228)` (`L724`) and `Adv-1 (#015)` (`L915`)]**:
   - **Locations**: `L724` and `L915`.
   - **Drop-In Fix (`L723–L726`)**: Delete `(or n total vertices in the general phylogenetic cactus variant)` and `(or in the subset variant, child multisets with no single-child pass-through vertices)` so the statement directly defines the rooted phylogenetic tree functional equation $T(x) = x + (1 + T(x))^m - 1 - m T(x)$.
   - **Drop-In Fix (`L913–L918`)**: Delete `(or in the unweighted 12-direction compass rose variant, the 12 steps (\pm 1, 0), (0, \pm 1), (\pm 1, \pm 1), (\pm 2, \pm 1), (\pm 1, \pm 2))` so the statement directly defines the 12-step polynomial $S(x, y) = P(x y) x^{-1} + Q(x y) y^{-1}$.

4. **[OPTIONAL — Drop-In Replacement for `Ch 17 Adv-2 (#204)` if Aligning with `Luogu P7599` Dominance Lattice Walk in `CURRICULUM_ARCHITECTURE.md` `L864`]**:
   - As noted in §2.2, if the editors keep the current Bipartite Rank-1 Good–Lagrange problem in `ch17` `L991–L1069`, simply remove `Luogu P7599` from `L991` and `L993` (and update `CURRICULUM_ARCHITECTURE.md` `L864` to match). Conversely, if `Ch 17 Adv-2 (#204)` should match `CURRICULUM_ARCHITECTURE.md` `L864` (`2D Dominance Lattice Walk + Bivariate Kernel Method`), here is a complete self-contained drop-in replacement:
     ```markdown
     ### Advanced 2 (#204) — 2D Dominance Lattice Walk in the Weyl Chamber (Luogu P7599 — Walk Variant)

     * **Source**: Luogu P7599 (`4B#16` Dominance Walk Synthesis)
     * **Key Technique**: 2D Weyl Chamber Dominance Walk ($x_1 \ge x_2 \ge 0$) + $D_4$ Obstinate Kernel Reflection / Bivariate Kernel Method.

     **Problem Statement.** A particle starts at $(0, 0)$ in the 2D dominance wedge $\mathcal{W} = \{(i, j) \in \mathbb{Z}^2 : i \ge j \ge 0\}$. In each step, it takes one of the four unit steps $(+1, 0), (-1, 0), (0, +1), (0, -1)$ and must remain inside $\mathcal{W}$ (so both $j \ge 0$ and $i - j \ge 0$ hold after every step). Given $N \le 2 \times 10^5$ and a target endpoint $(a, b) \in \mathcal{W}$, compute the number of $N$-step walks in $\mathcal{W}$ from $(0, 0)$ to $(a, b)$ modulo $998244353$ in $O(N)$ time.

     *Small-instance trace ($N = 2, (a, b) = (0, 0)$)*:
     - Step 1 must move from $(0, 0)$ to $(1, 0)$ (since $(0, 1) \notin \mathcal{W}$ and negative steps are forbidden).
     - Step 2 from $(1, 0)$ can only return to $(0, 0)$ (since $(2, 0)$ and $(1, 1)$ do not end at $(0, 0)$).
     - Thus there is $1$ valid walk of length $N = 2$ ending at $(0, 0)$: $(0,0) \to (1,0) \to (0,0)$.
     ```

5. **[MINOR — 4 Broken Prerequisite `.qmd` Links in `Ch 17` Header (`L11–L14`)]**:
   - **Location**: [ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L11-L14)
   - **Drop-In Fix (`L11–L14`)**:
     ```markdown
     - [Chapter 11: Lagrange–Bürmann Inversion, Raney's Lemma & Formal Laurent Residues](ch11-lagrange-inversion-raney-formal-residues.qmd) (univariate Lagrange Inversion and formal residues)
     - [Chapter 10: Implicit Equations, Multivariate Newton & Relaxed Convolution](ch10-implicit-equations-multivariate-newton-relaxation.qmd) and [Chapter 13: Labeled Graphs, Cayley's Formula, Matrix-Tree & Tournaments](ch13-labeled-graphs-cayley-matrix-tree-tournaments.qmd) (coupled Newton iteration and Matrix-Tree determinants)
     - [Chapter 15: 1D Lattice Walks, Reflection Principle, Chebyshev Rational Functions & The Kernel Method](ch15-1d-lattice-walks-chebyshev-kernel-method.qmd) (1D Kernel Method and small-root elimination)
     - [Chapter 16: The Bivariate Hierarchy, 2D Bostan–Mori, Twisted Kronecker & Furstenberg Diagonals](ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd) (iterated Laurent rings $K((x))((y))$, Twisted Kronecker FFT, and Furstenberg diagonals)
     ```

---

### 3.5 Blind Checkpoint IV: `checkpoints/cp04-part4-pgf-walks-multivariate.qmd`

#### Specific Issues & Drop-In Replacements for `CP-IV`

1. **[CRITICAL — Mathematical Sign Contradiction Between `Hint 3` (`L79`) and Complete Solution (`L555–L568`) + Raw `"Wait:"` Monologue in `CP-IV.1 (#158, Luogu P4707)`]**:
   - **Locations**: [cp04-part4-pgf-walks-multivariate.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L77-L80) (`Hint 3`) and [L552-L564](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L552-L564) (`Complete Solution`).
   - **Issue**:
     - `Hint 3` (`L79`) says: `with base convention dp[0][0] = -1 (so when S = {i} is a singleton of weight p_i and r = 1, it receives +dp[0][0] - dp[0][1] = (-1)^{1-1}\binom{0}{0} if initialized appropriately).`
     - With $+dp[0][0] - dp[0][1]$, setting $dp[0][0] = -1$ produces **$-1$**, NOT $(-1)^{1-1}\binom{0}{0} = +1$!
     - In the Complete Solution (`L555–L558`), the author wrote `dp[0][0] = -1`, realized on line 557 that `-1 - 0 = -1? Wait: we want +1 for r = 1, s = 1!`, and changed it on line 558 to `dp[0][0] = +1` without fixing `Hint 3` (`L79`) or deleting the `"Wait:"` monologue (`L555–L558`)!
   - **Drop-In Fix for `CP-IV.1 Hint 3` (`L77–L80`)**:
     ```markdown
     Define $dp[j][r]$ (for $0 \le j \le m$ and $1 \le r \le K$) as the sum of $(-1)^{|S| - r} \binom{|S| - 1}{r - 1}$ over all non-empty subsets $S$ of the items processed so far with $\sum_{i \in S} p_i = j$. When adding item $i$ with weight $p_i$:
     $$dp_{\text{new}}[j + p_i][r] = dp[j + p_i][r] + dp[j][r - 1] - dp[j][r] \quad (1 \le r \le K),$$
     with boundary seed **$dp[0][0] = +1$** and $dp[j][0] = 0$ for all $j \ge 1$ (so when $S = \{i\}$ is a singleton of weight $p_i$, it receives $dp[0][0] - dp[0][1] = +1 = (-1)^{1-1}\binom{0}{0}$ at $r = 1$ and $0$ at $r \ge 2$). Finally, $\mathbb{E}[T] = \sum_{j=1}^m dp[j][K] \cdot \frac{m}{j} \bmod 998244353$ in $O(n m K)$ time and $O(m K)$ space.
     ```
   - **Drop-In Fix for `CP-IV.1 Complete Solution` (`L552–L564`)**:
     ```markdown
     Let us verify the boundary seed when $S$ transitions from the empty set ($s = 0, j = 0$) to a singleton ($s = 1, j = p_i$):
     For $s = 1$, we require $f(1, r) = (-1)^{1 - r} \binom{0}{r - 1} = [r = 1]$.
     Therefore, we initialize the empty-set state ($j = 0$) with:
     $$dp[0][0] = +1, \qquad dp[0][r] = 0 \quad (1 \le r \le K),$$
     and keep $dp[j][0] = 0$ for all $j \ge 1$ by looping $r$ only over $1 \le r \le K$ (from $K$ down to $1$ in place). Let us trace the first two insertions:
     - Adding a 1st element (weight $p_1$ from $j = 0$): for $r = 1$, $dp[p_1][1] \gets dp[0][0] - dp[0][1] = 1 - 0 = +1 = (-1)^{1-1}\binom{0}{0}$. For $r \ge 2$, $dp[p_1][r] \gets dp[0][r-1] - dp[0][r] = 0$.
     - Adding a 2nd element (weight $p_2$ on top of $j = p_1$):
       - For $r = 1$: $dp[p_1 + p_2][1] \gets dp[p_1][0] - dp[p_1][1] = 0 - 1 = -1 = (-1)^{2-1}\binom{1}{0}$.
       - For $r = 2$: $dp[p_1 + p_2][2] \gets dp[p_1][1] - dp[p_1][2] = 1 - 0 = +1 = (-1)^{2-2}\binom{1}{1}$.
     Both match $f(s, r) = (-1)^{s - r}\binom{s - 1}{r - 1}$ for all $s \ge 1$ and $1 \le r \le K$.
     ```

2. **[CRITICAL — Stage 1 Spoiler Violations in `CP-IV.7 (#243)` (`L364, L377–L382, L391, L397–L400`)]**:
   - **Locations**: [cp04-part4-pgf-walks-multivariate.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L364-L400)
   - **Issue**:
     1. Line 364 titles the problem `### Problem CP-IV.7 (#243) — Asymmetric Fuss–Catalan Diagonal` (whereas `CURRICULUM_ARCHITECTURE.md` `L1297` strips the paradigm name in Stage 1).
     2. Line 380 in the **Stage 1 Problem Statement** explicitly says: *"by applying the **Furstenberg diagonal residue representation** and the **Global Residue Theorem** (replacing the $p$ fractional small poles with the single large pole)"* and reveals the denominator $1 - (p+1)w(t)$!
     3. Line 391 in the walkthrough names *"the ternary Fuss–Catalan numbers"* and gives $\frac{1}{1 - 3w(t)}$.
     4. Lines 397–400 (`Hint 1`) name *"residue $[z^{-1}]$"*, *"small poles"*, and *"large poles"*.
   - **Drop-In Spoiler-Free Fix for `CP-IV.7` Stage 1 (`L364–L401`)**:
     ```markdown
     ### Problem `CP-IV.7` (`#243`) — Asymmetric Ray Extraction on a Grid

     * **Source**: [yukicoder No. 2104](https://yukicoder.me/problems/no/2104) / [Codeforces 1666H](https://codeforces.com/problemset/problem/1666/H)
     * **Input Parameters & Constraints**:
       - Positive integers $p \ge 1$, $a \ge 0$, and $N$ ($1 \le N \le 10^5$, $1 \le p \le 10^9$, $0 \le a \le 10^5$).
       - Target coefficients for $n = 0, 1, \dots, N$ (both for the pure ray series $D_{p, a}(t)$ and for general polynomial numerators of degree $d \le N$).
       - Modulus: $998244353$.
       - Target Complexity: $O(N \log N)$ time (and $O(1)$ per term for a single ray).

     #### Problem Statement

     Consider the bivariate generating function of 2D lattice paths with unit steps $(1, 0)$ and $(0, 1)$:
     $$F(x, y) = \frac{1}{1 - x - y}.$$
     For a fixed slope parameter $p \ge 1$ and horizontal offset $a \ge 0$, define the univariate generating function of coefficients along the ray $(i, j) = (p n + a, n)$:
     $$D_{p, a}(t) := \sum_{n=0}^{\infty} \left( [x^{p n + a} y^n] \frac{1}{1 - x - y} \right) t^n.$$
     More generally, given a rational bivariate series $P(x, y) / (1 - x - y)$ where $P(x, y)$ has degree $\le d \le N$, determine an algebraic characterization of $D_{p, a}(t)$ and compute the ray coefficients $[x^{p n + a} y^n] \frac{P(x, y)}{1 - x - y}$ for all $n = 0, 1, \dots, N$ modulo $998244353$ in $O(N \log N)$ time.

     #### Small-Instance Walkthrough ($p = 2, a = 0, N = 3$)

     Suppose $p = 2$, $a = 0$, and $P(x, y) = 1$. For each $n = 0, 1, 2, 3$, the coefficient $[x^{2n} y^n] \frac{1}{1 - x - y}$ counts lattice paths from $(0, 0)$ to $(2n, n)$:

     - $n = 0$: $[x^0 y^0] \frac{1}{1 - x - y} = \binom{0}{0} = 1$.
     - $n = 1$: $[x^2 y^1] \frac{1}{1 - x - y} = \binom{3}{1} = 3$.
     - $n = 2$: $[x^4 y^2] \frac{1}{1 - x - y} = \binom{6}{2} = 15$.
     - $n = 3$: $[x^6 y^3] \frac{1}{1 - x - y} = \binom{9}{3} = 84$.
     - Thus $D_{2, 0}(t) = 1 + 3t + 15t^2 + 84t^3 + O(t^4)$. How can you express $D_{p, a}(t)$ directly in terms of a single implicit power series without summing over $p$ separate branches?

     #### Progressive Triage Hints

     <details>
     <summary><strong>Hint 1 — Structural Triage & Monomial Alignment Observation (Spoiler-Free)</strong></summary>

     We want to isolate the terms $x^i y^j$ inside $F(x, y)$ where the exponents satisfy the linear relation $i - p j = a$. What monomial change of variables $(x, y) \mapsto (z, \dots)$ makes the difference $i - p j$ appear as the exponent of $z$ while tracking $j = n$ as the exponent of $t$? Once you rewrite $F$ in terms of $z$ and $t$, compare the roots of the denominator that approach $0$ as $t \to 0$ against the root that approaches $1$ as $t \to 0$.

     </details>
     ```

3. **[CRITICAL — Stage 1 Spoiler Violations & Split/Hedged Statement in `CP-IV.8 (#082, Toyota 2023 Spring Final E)` (`L428–L461, L880–L885`)]**:
   - **Locations**: [cp04-part4-pgf-walks-multivariate.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L428-L461) and [L880-L885](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L880-L885).
   - **Issues**:
     1. **Stage 1 Spoilers**: Line 440 names `Łukasiewicz walk`, line 447 names `Łukasiewicz walk`, line 452 names `Raney's simple cyclic rotation`, and line 459 (`Hint 1`) names `1D Kernel Method` and `one small root`.
     2. **Dual/Hedged Statement & Constraint Mismatch**: Line 435 hedges `(and assigning distinguishable labels or transition weights w_d to each step of type d)`, line 440 hedges `(We solve both the pure fixed-multiplicity Łukasiewicz walk and the general weighted generating-function transition)`, line 428 sets $N \le 2 \times 10^5$ with complexity $O(N \log N)$ or $O(N \log^2 N)$, Table 2.2 (`L521`) says $O(N \log^2 N)$, and the Stage 2 Algorithm Contract (`L881–L885`) switches to $N \le 10^6$, introduces $\text{val}_d$, and gives complexity $O(N)$ / $O(N \log N)$!
   - **Drop-In Spoiler-Free & Unified Fix for `CP-IV.8` Stage 1 (`L427–L461`)**:
     ```markdown
     * **Input Parameters & Constraints**:
       - Digits $d \in \{1, 2, \dots, 9\}$, each with a replacement length $k_d \ge 0$ ($0 \le k_d \le 9$), a step weight $w_d \in \mathbb{F}_p$, and (in the fixed-multiplicity query) a usage count $c_d \ge 0$ with total steps $N = \sum_{d=1}^9 c_d \le 2 \times 10^5$.
       - Initial stack size $s_0 \ge 1$.
       - Modulus: $p = 998244353$.
       - Target Complexity: $O(N \log N)$ time for general weighted $N$-step walks (reducing to $O(N)$ when the final stack size is $0$ with fixed multiplicities $c_d$) and $O(N)$ space.

     #### Problem Statement

     You start with a stack containing $s_0 \ge 1$ digits. In each of $N$ steps, you must pop $1$ digit from the stack (which requires the stack to be **non-empty** before the step) and push $k_d$ new digits onto the stack for some operation type $d \in \{1, \dots, 9\}$, changing the stack size by $\Delta_d = k_d - 1 \in \{-1, 0, +1, \dots, +8\}$:

     1. **(Fixed-Multiplicity Consumption)**: Given exact usage counts $c_1, \dots, c_9$ with $\sum_{d=1}^9 c_d = N$ and net stack change $\sum_{d=1}^9 c_d (k_d - 1) = -s_0$ (so the stack becomes empty for the first time after step $N$), count the number of valid operation sequences $(d_1, \dots, d_N) \in \{1, \dots, 9\}^N$ using each type $d$ exactly $c_d$ times such that the stack is non-empty before every step $t = 1, \dots, N$.
     2. **(Weighted Arbitrary-Endpoint Walk)**: Given step weights $w_0, w_1, \dots, w_9 \in \mathbb{F}_p$ (where step $k$ changes the stack size by $k - 1$), compute for each $n = 0, 1, \dots, N$ the total weight of $n$-step sequences starting at stack size $s_0 \ge 1$ that remain non-empty before every step, modulo $998244353$.

     #### Small-Instance Walkthrough ($N = 3, s_0 = 1$)

     Suppose $s_0 = 1$ and $N = 3$, with two operations of type $A$ having $k_A = 0$ ($\Delta_A = -1$, $c_A = 2$) and one operation of type $B$ having $k_B = 2$ ($\Delta_B = +1$, $c_B = 1$):

     - Total net change after $N = 3$ steps is $2(-1) + 1(+1) = -1$, so every ordering of $\{A, A, B\}$ ends at final stack size $1 + (-1) = 0$.
     - Let us check all $\binom{3}{1} = 3$ orderings of $\{A, A, B\}$:
       1. $(B, A, A)$: stack sizes $1 \xrightarrow{+1} 2 \xrightarrow{-1} 1 \xrightarrow{-1} 0$ (valid: always $\ge 1$ before each step!).
       2. $(A, B, A)$: stack sizes $1 \xrightarrow{-1} 0$ at step $1$ — invalid, stack becomes empty before step $2$!
       3. $(A, A, B)$: stack sizes $1 \xrightarrow{-1} 0$ at step $1$ — invalid!
     - Thus $1$ out of the $3$ sequences is valid. What structural property of the step sizes $\Delta_d = k_d - 1 \in \{-1, 0, +1, \dots, +8\}$ makes downward crossings of $0$ far simpler to analyze than upward jumps?

     #### Progressive Triage Hints

     <details>
     <summary><strong>Hint 1 — Structural Triage & Walk Direction Observation (Spoiler-Free)</strong></summary>

     In each step, the stack size changes by $\Delta_d = k_d - 1 \in \{-1, 0, +1, \dots, +8\}$. Notice the crucial asymmetry: a step can jump **up** by up to $+8$, but can step **down** by **at most $-1$**! Because the stack size can never decrease by more than $1$ in a single step, a walk starting at $s_0 \ge 1$ cannot jump from $\ge 1$ to $< 0$ without passing through $0$ one unit at a time. How does this single-step downward property simplify both cyclic shifts of a walk and the boundary equation at stack size $0$?

     </details>
     ```
   - **Also synchronize `L521` (Table 2.2) and `L881` (Algorithm Contract)**: Set `N \le 2 \times 10^5` in `L881` and `$O(N \log N)$ time ($O(N)$ for fixed-multiplicity), $O(N)$ space` in `L521`.

4. **[MODERATE — Stage 1 `Hint 1` Spoiler Leaks in `CP-IV.3 (#099)`, `CP-IV.4 (#116)`, and `CP-IV.6 (#058)`]**:
   - **Locations**: `L175` (`CP-IV.3`), `L236` (`CP-IV.4`), and `L340` (`CP-IV.6`).
   - **Drop-In Spoiler-Free Replacements for `Hint 1`**:
     - **`CP-IV.3 Hint 1` (`L175`)**:
       ```markdown
       Notice that in any step, the transition depends *only* on the two interacting active companies $u$ and $v$ (with $a$ and $b$ vassals), regardless of how many other active companies exist! Moreover, when a company with $b$ vassals is acquired, all $b$ of its vassals reset to active companies with $0$ vassals. How can you measure the "progress" of the entire configuration toward the single-company terminal state so that every step advances that progress by $+1$ in expectation regardless of which pair $(u, v)$ is picked?
       ```
     - **`CP-IV.4 Hint 1` (`L236`)**:
       ```markdown
       At any moment, the state is a partition of the $N$ students into club sizes $(a_1, \dots, a_k)$ with $\sum_{i} a_i = N$. In a single step, each existing club of size $s$ can only change size to $s - 1$, $s$, or $s + 1$, while a new club of size $1$ is created with probability $\frac{1}{2}$. How can you assign a score to each club size $s$ so that the expected one-step change summed over all clubs is constant across all partitions of $N$?
       ```
     - **`CP-IV.6 Hint 1` (`L340`)**:
       ```markdown
       Unlike `CP-IV.2`, where there was a single target configuration $s$, here the stopping condition is an entire **set of target grids** $\mathcal{T}$ (all grids whose $i$-th row has $A_i$ ones, so $|\mathcal{T}| = \prod_{i=1}^H \binom{W}{A_i}$). If the process enters $\mathcal{T}$ for the first time at some grid $t_0 \in \mathcal{T}$, does the probability of subsequently returning to $\mathcal{T}$ after $m$ additional steps depend on *which* specific grid $t_0 \in \mathcal{T}$ was hit first? Why does column symmetry within each row matter?
       ```

---

## 4. Verification Summary Across All 4 Mandatory Audit Dimensions

1. **Checklist Item 1 (Exact Problem ID & Assignment Match)**:
   - All `40/40` problem slots across `Ch 14` (`8`), `Ch 15` (`8`), `Ch 16` (`8`), `Ch 17` (`8`), and `CP-IV` (`8`) match the exact Pool IDs in `CURRICULUM_ARCHITECTURE.md` (`L728–L867`, `L1285–L1315`).
   - Special Check on `Ch 17 Adv-2 (#204)` and `Ch 17 Mas-2 (#234)` completed in §2.2 with concrete drop-in fixes for `#204`'s title/source alignment and `#234`'s duplicate `UOJ 596` tag, `Ch 16 (§16.3)` cross-reference, and $\chi(I)$ formula.
2. **Checklist Item 2 (Single Authoritative Problem Statement & Visible $N \le 4$ Sample Trace)**:
   - `38/40` problems already have a single authoritative mathematical statement and a self-contained visible $N \le 4$ sample trace directly beneath the statement; concrete drop-in fixes are provided above for the remaining `2/40` (`Ch 16 Adv-1 #237` and `CP-IV.8 #082`), plus trimming minor parenthetical remarks in `Ch 17 Int-1 (#228)` and `Ch 17 Adv-1 (#015)`.
3. **Checklist Item 3 (3 Progressive Collapsible Hints & Complete Step-by-Step Solution)**:
   - All `40/40` problems have 3 collapsible hints and complete derivations.
   - All mathematical contradictions between hints and solutions (`CP-IV.1` Hint 3 `dp[0][0] = -1` vs. Solution `dp[0][0] = +1`; `Ch 15 Mas-2 #210` Hint 2 $F_{-1}(z) = 0$ vs. Solution $F_{-1}(z) = 1$; `Ch 16 Mas-2 #214` and `Ch 17 Mas-2 #234` false coordinate formula for $\chi(I)$) and all raw `"Wait:"` monologues (`CP-IV.1` `L557` and `Ch 17 SS-2` `L686`) have been caught with exact drop-in fixes.
4. **Checklist Item 4 (100% Spoiler-Free Stage 1 in `CP-IV`)**:
   - Stage 2 properly houses the Mermaid decision tree (`2.1`) and Master Paradigm Comparison Table (`2.2`), and all Stage 1 spoilers in `CP-IV.7`, `CP-IV.8`, `CP-IV.6`, `CP-IV.4`, and `CP-IV.3` have exact drop-in spoiler-free replacements in §3.5.
