# Master Reserve Problem Bank & Complete Problem Encyclopedia (`problem_archive.md`)

> **Phase 1 & Phase 1.5 — Cohort 3 Master Problem Encyclopedia, Cross-Wave Index & 24-Chapter Curriculum Router**
> **Source Authority**: Synthesized and deduplicated across all 10 Cohort 3 Master Wave Reports (`cohort3_wave_1a` through `cohort3_wave_5b`) and synchronized with the **Phase 1.5 Canonical 6-Part, 24-Chapter Curriculum (`PROBLEM_CURATION.md`)**, covering **408 total problem appearances** across Waves 1A–5B (**254 unique accepted non-template competitive programming problems** `#001`–`#254` across 16 online judges, plus **67 quarantined bare-template verification problems** `R-01`–`R-67` in Section 12; `321` total cataloged problems).
> **Purpose for Phase 2–4 Textbook Authors**:
> 1. **Zero Problem Loss**: Every problem discovered across Cohort 1, Cohort 2, and the Pre-Existing Baseline — whether assigned to a Chapter Ladder (`192`), a Blind Topic-Group Checkpoint (`48`), or the Grandmaster Synthesis Reserve (`14`) — is preserved here with its **exact constraints, self-contained mathematical statement, primary/secondary FPS tags, diagnostic signal, 3-tier progressive hints, complete solution formula/derivation sketch, and cross-reference pointer** to the corresponding `cohort3_wave_*.md` file.
> 2. **Multi-Wave & Multi-Chapter Cross-Indexing**: Landmark problems that bridge multiple chapters (e.g., `CF 438E`, `ABC 222 H`, `CF 1349D`, `AGC 058 D`, `Luogu P4389`, `Luogu P4841`, `LOJ 6538`, `LOJ 6728`, `ABC 240 G`, `ABC 300 Ex`, `ABC 281 Ex`, `AGC 005 F`) are cross-referenced across every wave and chapter where they appear, highlighting how each chapter attacks the same problem from a distinct algebraic angle.
> 3. **Strict Anti-Template-Bloat Enforcement**: Bare template-verification problems (`R-01`–`R-67`, e.g., Library Checker `inv`/`exp`/`log`/`sqrt`/`pow`, Luogu `P4238`/`P4721`/`P4725`/`P4726`/`P5205`/`P5245`, etc.) are strictly quarantined in **Section 12** (and Section 5 of `PROBLEM_CURATION.md`) as implementation unit tests rather than pedagogical exercises.

---

## 0. Phase 1.5 Canonical 24-Chapter Curriculum Routing Table (`#001`–`#254`)

> **Phase 1.5 Bijective Synchronization**: Every accepted problem `#001`–`#254` in this encyclopedia is bijectively routed into the **6-Part, 24-Chapter Curriculum Architecture** in [`PROBLEM_CURATION.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md) (`192` Chapter Ladder Problems + `48` Blind Checkpoint Problems + `14` Grandmaster Synthesis Reserve Problems = `254`).

| Ch / Unit | SS-1 & SS-2 (or `.1` & `.2`) | Int-1 & Int-2 (or `.3` & `.4`) | Adv-1 & Adv-2 (or `.5` & `.6`) | Mas-1 & Mas-2 (or `.7` & `.8`) |
| :-: | :--- | :--- | :--- | :--- |
| **Ch 01** | `#019` ABC 178 D; `#043` ABC 321 F | `#004` `fps_24_g`; `#077` EDPC M | `#049` ARC 028 D; `#097` CF 993E | `#066` AGC 001 E; `#107` CF 1251F |
| **Ch 02** | `#238` yukicoder 1145; `#165` Luogu P4389 (0-1 Subset Sum Variant) / AtCoder FPS Subset Sum via ln/exp | `#101` CF 1096G; `#222` LOJ 6261 | `#157` Luogu P4705; `#084` CF 438E | `#030` ABC 267 Ex; `#091` CF 891E |
| **Ch 03** | `#001` `fps_24_a`; `#188` Luogu P6189 | `#153` Luogu P4389; `#009` `fps_24_n` | `#223` yukicoder 899 / LOJ 6268; `#221` LOJ 6089 | `#150` Luogu P3784; `#159` Luogu P4727 |
| **Ch 04** | `#002` `fps_24_e`; `#007` `fps_24_m` | `#161` Luogu P4841; `#008` `fps_24_n` | `#083` CF 407E / Gym; `#011` `fps_24_q` | `#041` ABC 303 Ex; `#174` Luogu P5401 |
| **Ch 05** | `#104` CF 1117D; `#034` ABC 279 G | `#187` Luogu P6078; `#069` AGC 013 E | `#040` ABC 300 Ex; `#081` AISing 2020 F | `#177` Luogu P5487; `#073` AGC 054 E |
| **Ch 06** | `#005` `fps_24_h`; `#055` ARC 110 D | `#193` Luogu P6620; `#080` KUPC 2019 K | `#094` CF 923E; `#096` CF 960G | `#098` CF 995F; `#109` CF 1278F |
| **Ch 07** | `#224` LOJ 6485; `#248` BZOJ 3328 | `#178` Luogu P5591; `#143` Luogu P3321 | `#147` Luogu P3702; `#012` `fps_24_r` | `#092` CF 901E; `#168` Luogu P5293 |
| **Ch 08** | `#018` ABC 172 E; `#241` yukicoder 1810 | `#155` Luogu P4491; `#089` CF 840C | `#067` AGC 005 D; `#139` CF Gym 102978H | `#052` ARC 100 F / LOJ 3395; `#137` CF Gym 102331J |
| **Ch 09** | `#060` ARC 138 E; `#021` ABC 222 H | `#086` CF 553E; `#023` ABC 230 Ex | `#056` ARC 123 F; `#225` LOJ 6503 | `#206` UOJ 50; `#075` AGC 060 D |
| **Ch 10** | `#186` Luogu P5900; `#226` LOJ 6538 | `#244` yukicoder 3029; `#013` `fps_24_s` | `#179` Luogu P5597; `#126` CF 1687F | `#191` Luogu P6598; `#192` Luogu P6597 |
| **Ch 11** | `#003` `fps_24_f`; `#200` Luogu P7438 | `#196` Luogu P6672; `#201` Luogu P7439 | `#010` `fps_24_p`; `#229` LOJ 6703 | `#114` CF 1349F2; `#203` Luogu P7592 |
| **Ch 12** | `#176` Luogu P5434; `#245` 51Nod 1728 | `#146` Luogu P3684 / BZOJ 3684; `#227` LOJ 6569 | `#190` Luogu P6596; `#016` `fps_24_w` | `#183` Luogu P5827; `#184` Luogu P5828 |
| **Ch 13** | `#164` Luogu P5219; `#103` CF 1109D | `#093` CF 917D; `#189` Luogu P6295 | `#199` Luogu P7364; `#053` ARC 105 F / LOJ 6539 | `#122` CF 1556F; `#212` UOJ 498 |
| **Ch 14** | `#115` CF 1392H; `#026` ABC 242 Ex | `#156` Luogu P4548; `#071` AGC 038 E | `#148` Luogu P3706; `#209` UOJ 390 | `#039` ABC 289 Ex; `#113` CF 1349D |
| **Ch 15** | `#105` CF 1204E; `#070` AGC 021 E | `#220` Luogu P3266; `#140` CF Gym 103415K / yukicoder 1341 | `#128` CF 1810G; `#134` CF 1967E2 | `#076` AGC 070 C; `#210` UOJ 424 |
| **Ch 16** | `#048` ARC 012 D; `#129` CF 1821F | `#025` ABC 240 G; `#232` QOJ 4815 | `#237` yukicoder 1080; `#074` AGC 058 D | `#240` yukicoder 1783; `#214` UOJ 596 |
| **Ch 17** | `#154` Luogu P4456; `#044` ABC 336 G | `#228` LOJ 6671; `#219` LOJ 3398 | `#015` `fps_24_v`; `#204` Luogu P7599 (Variant) | `#138` CF Gym 102538F; `#234` QOJ 8048 |
| **Ch 18** | `#151` Luogu P4002; `#064` ARC 153 D | `#022` ABC 226 H; `#239` yukicoder 1504 | `#125` CF 1667E; `#088` CF 755G | `#211` UOJ 450; `#230` LOJ 6728 |
| **Ch 19** | `#242` yukicoder 1939; `#120` CF 1548C | `#095` CF 932E; `#195` Luogu P6667 | `#028` ABC 260 Ex; `#118` CF 1515E | `#072` AGC 043 D; `#213` UOJ 514 |
| **Ch 20** | `#050` ARC 033 D; `#197` Luogu P7116 | `#127` CF 1770G; `#167` Luogu P5284 | `#208` UOJ 182; `#202` Luogu P7440 | `#181` Luogu P5668; `#217` LOJ 161 |
| **Ch 21** | `#036` ABC 281 Ex; `#045` ABC 345 G | `#047` ABC 387 G; `#059` ARC 137 F | `#065` ARC 154 F; `#218` LOJ 171 / QOJ 6504 | `#235` QOJ 8528; `#017` `fps_24_x` |
| **Ch 22** | `#031` ABC 269 Ex; `#124` CF 1613F | `#046` ABC 355 G; `#198` Luogu P7279 | `#149` Luogu P3781 / LOJ 2269; `#136` CF 2006E | `#166` Luogu P5281 / LOJ 3044; `#145` Luogu P3348 |
| **Ch 23** | `#123` CF 1603F; `#033` ABC 278 Ex | `#233` QOJ 5097 / SOJ 703; `#057` ARC 134 E | `#062` ARC 139 F; `#132` CF 1916F | `#063` ARC 145 F; `#111` CF 1336E2 |
| **Ch 24** | `#216` CF 449D; `#020` ABC 213 G | `#027` ABC 253 Ex; `#042` ABC 306 Ex | `#110` CF 1326F2; `#207` UOJ 94 | `#231` LOJ 6729; `#038` ABC 288 Ex |
| **CP-I** *(Blind)* | `#078` Typical90 #065; `#144` Luogu P3338 | `#246` HDU 5279; `#032` ABC 276 G | `#079` JSC 2019 Qual F; `#250` Project Euler 755 | `#037` ABC 284 Ex; `#024` ABC 236 Ex |
| **CP-II** *(Blind)* | `#085` CF 451E; `#152` Luogu P4091 | `#251` CF 1264D1; `#252` CF 622F | `#100` CF 1054H; `#029` ABC 266 G | `#162` Luogu P4859; `#141` Luogu P2290 / P4430 |
| **CP-III** *(Blind)* | `#090` CF 848E; `#131` CF 1906J | `#133` CF 1930I; `#160` Luogu P4747 | `#119` CF 1528F; `#035` ABC 279 Ex | `#205` Luogu P8555; `#163` Luogu P5206 |
| **CP-IV** *(Blind)* | `#158` Luogu P4707; `#169` Luogu P5326 | `#099` CF 1025G; `#116` CF 1479E | `#194` Luogu P6633; `#058` ARC 136 F | `#243` yukicoder 2104; `#082` Toyota 2023 Spring Final E |
| **CP-V** *(Blind)* | `#236` yukicoder 963; `#108` CF 1264D2 | `#130` CF 1842I; `#135` CF 1988F | `#185` Luogu P5853; `#215` UOJ 604 | `#061` ARC 138 F; `#068` AGC 005 F |
| **CP-VI** *(Blind)* | `#102` CF 1097G; `#121` CF 1553I | `#117` CF 1510H; `#170` Luogu P5327 | `#054` ARC 106 E; `#254` UOJ 310 | `#175` Luogu P5406; `#180` Luogu P5643 |

- **Grandmaster Multi-Chapter Synthesis Reserve (`Syn-01`–`Syn-14`)**: **Syn-01**: `#006` `fps_24_k` $\mid$ **Syn-02**: `#014` `fps_24_t` $\mid$ **Syn-03**: `#051` ARC 093 F $\mid$ **Syn-04**: `#087` CF 623E $\mid$ **Syn-05**: `#106` CF 1228E $\mid$ **Syn-06**: `#112` CF 1342E $\mid$ **Syn-07**: `#142` Luogu P3311 $\mid$ **Syn-08**: `#171` Luogu P5339 $\mid$ **Syn-09**: `#173` Luogu P5400 $\mid$ **Syn-10**: `#182` Luogu P5824 $\mid$ **Syn-11**: `#172` Luogu P5366 $\mid$ **Syn-12**: `#247` HDU 5855 $\mid$ **Syn-13**: `#249` CSES 1112 $\mid$ **Syn-14**: `#253` CF 961G.

---

## 1. Judge-by-Judge Quick Lookup Index

### 1.1 AtCoder — Educational FPS Contest (`fps_24`: 24 Problems)
| Problem ID | Canonical Pool ID | Title | Primary FPS Technique | Wave Entry Pointer(s) | Canonical Curriculum Slot |
| :--- | :-: | :--- | :--- | :--- | :--- |
| **`fps_24_a`** | `#001` | Snack / Snacks | OGF Product & Polynomial Power $P(x)^D$ / Subset-Sum $\ln$-$\exp$ | Wave 1A (#1), Wave 1B (#1) | **`Ch 03 [SS-1]`** |
| **`fps_24_b`** | `#T43` | Number | Unbounded Change-Making $(1-x^v)^{-1}$ | Section 12 (#T43) | Quarantined Template (`Ch 01`) |
| **`fps_24_c`** | `#T43` | Sequence | Bounded Sum OGF $\left(\frac{1-x^{M+1}}{1-x}\right)^N$ | Section 12 (#T43) | Quarantined Template (`Ch 01` / `Ch 06`) |
| **`fps_24_d` / `fps_24_e`** | `#002` | Sequence 2 | Labeled Multiset Permutation EGF $\prod_{m=1}^M \sum_{j=0}^m \frac{x^j}{j!}$ | Wave 1A (#3 / #15) | **`Ch 04 [SS-1]`** |
| **`fps_24_e` (Alt)** | `#T43` | Sequence 3 | Bounded Exponential Factor $\prod \sum_{k=0}^c \frac{x^k}{k!}$ | Section 12 (#T43) | Quarantined Template (`Ch 04`) |
| **`fps_24_f`** | `#003` | Colored Paper / Colored Tree | Parity EGF $e^{2x}\sinh^2 x = \frac{4^N-2^N}{4}$ & Even-Degree Tree $F=x\cosh F$ | Wave 3B (#1) | **`Ch 11 [SS-1]`** |
| **`fps_24_g`** | `#004` | Coin | Dynamic Sliding-Window Partition $\prod_{j=k}^{k+L-1}(1-x^j)^{-1}$ & Reversible Coin DP | Wave 1A (#2) | **`Ch 01 [Int-1]`** |
| **`fps_24_h`** | `#005` | Jump | Bivariate Rational Substitution $\frac{1-y}{1-2y-x}$ & Taylor Shift | Wave 2A (#1) | **`Ch 06 [SS-1]`** |
| **`fps_24_i`** | `#T43` | Set | Subset Product & Log-Exp Sum | Section 12 (#T43) | Quarantined Template (`Ch 02`) |
| **`fps_24_j`** | `#T43` | Magick | Semi-Online CDQ / Relaxed Convolution | Section 12 (#T43) | Quarantined Template (`Ch 09`) |
| **`fps_24_k`** | `#006` | Permutation | Derangement EGF $\frac{e^{-x}}{1-x}$ & Shared-Ascent IE $\frac{1}{1-\sum (-1)^{s-1}x^s/(s!)^2}$ | Wave 1A (#4) | **`Syn-01`** |
| **`fps_24_l`** | `#007` (Alt) | Permutation 2 | Constrained Cycle EGF $\exp(\sum_{c \notin S} \frac{x^c}{c})$ & Complementary-Pair IE | Wave 1A (#5) | Companion to `#007` (`Ch 04 [SS-2]`) |
| **`fps_24_m`** | `#007` | Value of Permutation / Connected Graph | Connected Labeled Graph $\ln G(x)$ & Block $\exp(F(x))$ | Wave 1A (#9b / #20) | **`Ch 04 [SS-2]`** |
| **`fps_24_n` (Coins)** | `#009` | Coin 2 / Coins 2 | Harmonic $\ln$-$\exp$ Compression $\prod(1+x^{A_i})$ & Bounded Numerator $\prod(1-x^{A_i+1})$ | Wave 1A (#7b), Wave 2A (#31) | **`Ch 03 [Int-2]`** |
| **`fps_24_o` / `fps_24_n` (Tree)** | `#008` | Rooted Tree / Tree | Prüfer Sequence Degree-Distribution EGF $n![x^{n-2}]\prod E_{d_i}(x)$ | Wave 1A (#21), Wave 3A (#2/#15), Wave 3B (#2) | **`Ch 04 [Int-2]`** |
| **`fps_24_p`** | `#010` | Ball | Bivariate Roots-of-Unity Filter | Wave 1A (#29), Section 12 (#T43) | **`Ch 11 [Adv-1]`** |
| **`fps_24_q`** | `#011` | Dice | Newton–Girard Power-Sum $N - x\frac{A'(x)}{A(x)}$ & EGF Moment Pipeline | Wave 2A (#34) | **`Ch 04 [Adv-2]`** |
| **`fps_24_r`** | `#012` | Random Walk | Cyclic Convolution $\bmod (x^M - 1)$ via Roots of Unity & Catalan Kernel | Wave 2A (#47) | **`Ch 07 [Adv-2]`** |
| **`fps_24_s`** | `#013` | Game | Tree Normal-Play Game $L = x\exp(x e^x - L)$ via Newton / Lambert $W$ | Wave 1A (#30), Wave 3B (#17) | **`Ch 10 [Int-2]`** |
| **`fps_24_t`** | `#014` | Colorful | Cycle-Parity Bivariate EGF & Run-Length Adjacent-Color IE | Wave 1A (#22) | **`Syn-02`** |
| **`fps_24_u`** | `#T43` | Bag | Pólya Cycle Index / Unlabeled Multiset | Section 12 (#T43) | Quarantined Template (`Ch 03`) |
| **`fps_24_v`** | `#015` | 12 Directions | Factorized 2D Lattice Walk & Radical / Rotation Decoupling | Wave 2A (#19) | **`Ch 17 [Adv-1]`** |
| **`fps_24_w`** | `#016` | Biconnected Graphs | Dissymmetry Theorem & Compositional Inverse $F(x) = x e^{B'(F(x))}$ | Wave 3A (#40) | **`Ch 12 [Adv-2]`** |
| **`fps_24_x`** | `#017` | Functional Square Root | Iterated Composition $F(F(x)) = G(x)$ in $\mathbb{F}_p[[x]]/(x^N)$ | Wave 1A (#31), Wave 3B (#23) | **`Ch 21 [Mas-2]`** |

### 1.2 AtCoder — ABC / ARC / AGC / Other Rated Contests
| Problem ID | Canonical Pool ID | Title | Primary FPS Technique | Wave Entry Pointer(s) | Canonical Curriculum Slot |
| :--- | :-: | :--- | :--- | :--- | :--- |
| **ABC 172 E** | `#018` | NEQ | Binomial Inversion & Rook-Style EGF | Wave 2B (#A2) | **`Ch 08 [SS-1]`** |
| **ABC 178 D** | `#019` | Redistribution | Restricted Composition $x^3/(1-x)$ | Wave 1B (#4) | **`Ch 01 [SS-1]`** |
| **ABC 213 G** | `#020` | Connectivity 2 | Connected Subgraph Subset Convolution ($\ln$) | Wave 1B (#24), Wave 5B (#F1) | **`Ch 24 [SS-2]`** |
| **ABC 222 H** | `#021` | Beautiful Binary Tree | Implicit Algebraic Tree + Lagrange / D-Finite ODE | Wave 1A (#13), Wave 2A (#13), Wave 3A (#18), Wave 3B (#6), Wave 4B (#9), Wave 5A (#5), Wave 5B (#C4) | **`Ch 09 [SS-2]`** |
| **ABC 226 H** | `#022` | Random K-th Max | Order-Statistic Integral $\int_0^1 t^k(1-t)^{n-k} dt$ & Holonomic Recurrence | `2B#E2` | **`Ch 18 [Int-1]`** |
| **ABC 230 Ex** | `#023` | Bullion | Online Pólya Euler Transform via Relaxed Convolution | Wave 5A (#20), Wave 5B (#C2) | **`Ch 09 [Int-2]`** |
| **ABC 236 Ex** | `#024` | Distinct Multiples | Set-Partition Inclusion-Exclusion & $\exp(\sum (-1)^{k-1} w_k x^k/k)$ | Wave 1A (#19) | **`CP-I.8`** ($\to$ `Ch 04`) |
| **ABC 240 G** | `#025` | Teleporting Takahashi | 3D Walk Decoupling via $(u,v) = (x+y, x-y)$ & D-Finite | Wave 2A (#43), Wave 4A (#P5), Wave 4B (#2) | **`Ch 16 [Int-1]`** |
| **ABC 242 Ex** | `#026` | Random Painting | Continuous-Time Min-Max Stopping PGF $F'(1)$ | Wave 2B (#E8) | **`Ch 14 [SS-2]`** |
| **ABC 253 Ex** | `#027` | We Love Forest | Set Power Series $\exp$ on Spanning Trees | Wave 5A (#14), Wave 5B (#F4) | **`Ch 24 [Int-1]`** |
| **ABC 260 Ex** | `#028` | Colorfulness | Adjacent-Pair IE + Divide-and-Conquer NTT + Taylor Shift | Wave 2B (#B7), Wave 5A (#21) | **`Ch 19 [Adv-1]`** |
| **ABC 266 G** | `#029` | Yet Another RGB Sequence | Substring Inclusion-Exclusion / Non-Overlapping Cluster GF | Wave 2B (#A5) | **`CP-II.6`** ($\to$ `Ch 08`) |
| **ABC 267 Ex** | `#030` | Odd Sum | Bivariate Parity Filter + $\ln$-$\exp$ Compression | Wave 1B (#12), Wave 2A (#32) | **`Ch 02 [Mas-1]`** |
| **ABC 269 Ex** | `#031` | Antichain | Heavy-Light Decomposition + D&C Tree FPS | Wave 5B (#A1) | **`Ch 22 [SS-1]`** |
| **ABC 276 G** | `#032` | Count Sequences | Mod-3 Step Encoding $1+x+x^2$ + Binomial Extraction | Wave 1B (#19), Wave 2B (#A3), Wave 4A (#P2) | **`CP-I.4`** ($\to$ `Ch 01`) |
| **ABC 278 Ex** | `#033` | make 1 | Basis / XOR Space $q$-Binomial & $q$-Pochhammer | Wave 5B (#E2) | **`Ch 23 [SS-2]`** |
| **ABC 279 G** | `#034` | At Most 2 Colors | Sliding-Window / Transfer-Matrix Rational GF | Wave 2B (#B3) | **`Ch 05 [SS-2]`** |
| **ABC 279 Ex** | `#035` | Sum of Prod of Min | Infinite Product $\prod_{i=1}^N \min(i, A_i) \implies [x^{M-N}]\prod_{i=1}^N \frac{1-(i+1)x^i+ix^{i+1}}{(1-x)^2}$ | Wave 4A (#P10) | **`CP-III.6`** ($\to$ `Ch 03`) |
| **ABC 281 Ex** | `#036` | Alchemy | Falling-Factorial EGF + Lagrange Inversion / Composition | Wave 2B (#B12), Wave 3A (#8), Wave 5B (#C7) | **`Ch 21 [SS-1]`** |
| **ABC 284 Ex** | `#037` | Count Unlabeled Graphs | Burnside's Lemma + Partition Cycle Index | Wave 3A (#38) | **`CP-I.7`** ($\to$ `Ch 03`) |
| **ABC 288 Ex** | `#038` | A Nameless Counting Problem | Dirichlet / Multiplicative Bell Series & XOR DP | Wave 5B (#F10) | **`Ch 24 [Mas-2]`** |
| **ABC 289 Ex** | `#039` | Trio | 3-Walker Return-to-Origin Absorbing PGF $(P^3) \oslash Q$ | Wave 2B (#E12) | **`Ch 14 [Mas-1]`** |
| **ABC 300 Ex** | `#040` | Fibonacci: Revisited | 3-Sparse Denominator $(1-x)Q(x) = 1-2x+x^{K+1}$ + Bostan–Mori | Wave 2A (#8), Wave 4A (#P3), Wave 5A (#22), Wave 5B (#B2) | **`Ch 05 [Adv-1]`** |
| **ABC 303 Ex** | `#041` | Constrained Tree Degree | Prüfer Sequence OGF $\ln$-$\exp$ Power Extraction | Wave 3A (#25) | **`Ch 04 [Mas-1]`** |
| **ABC 306 Ex** | `#042` | Balance Scale | DAG Orientation Set Power Series / Subset Inversion | Wave 5B (#F5) | **`Ch 24 [Int-2]`** |
| **ABC 321 F** | `#043` | #(subset sum = K) with Add/Erase | Reversible $O(K)$ DP Division by $(1+x^v)$ | Wave 1B (#3) | **`Ch 01 [SS-2]`** |
| **ABC 336 G** | `#044` | 16 Integers | De Bruijn Eulerian Circuit + BEST Theorem + Good–Lagrange | Wave 4B (#16), Wave 5B (#C5) | **`Ch 17 [SS-2]`** |
| **ABC 345 G** | `#045` | Sugoroku 5 | Hitting-Time Distribution via Polynomial Composition $F(G(x))$ | Wave 3B (#10) | **`Ch 21 [SS-2]`** |
| **ABC 355 G** | `#046` | Baseball | Laminar Containment Tree + Tree-DP Convolution | Wave 5B (#A3) | **`Ch 22 [Int-1]`** |
| **ABC 387 G** | `#047` | Prime Circuit | Connected Cactus / Prime Cycle Exp-Log + Composition | Wave 4A (#P21), Wave 5B (#C1) | **`Ch 21 [Int-1]`** |
| **ARC 012 D** | `#048` | Don't Step on the Mines! | 2D Walk Factoring + Prime-Power Kummer/Lucas Valuation | Wave 1B (#11), Wave 4B (#1) | **`Ch 16 [SS-1]`** |
| **ARC 028 D** | `#049` | 注文の多い高橋商店 | Reversible Bounded Knapsack Divide-by-$\frac{1-x^{a_i+1}}{1-x}$ | Wave 1B (#6) | **`Ch 01 [Adv-1]`** |
| **ARC 033 D** | `#050` | 多項式 (Polynomial) | $O(N)$ Sequential Prefix/Suffix Lagrange Interpolation | Wave 5B (#D1) | **`Ch 20 [SS-1]`** |
| **ARC 093 F** | `#051` | Dark Horse | Tournament Tree Subset-Min Inclusion-Exclusion | Wave 2B (#C2) | **`Syn-03`** |
| **ARC 100 F / LOJ 3395** | `#052` | Colorful Sequences | Forbidden Rainbow Window Automaton / IE OGF | Wave 2B (#B8) | **`Ch 08 [Mas-1]`** |
| **ARC 105 F / LOJ 6539** | `#053` | Lights Out on Connected Graph | Connected Bipartite Graph $\ln$ of Sqrt-Scaled Sum | Wave 1A (#20) | **`Ch 13 [Adv-2]`** |
| **ARC 106 E** | `#054` | Medals | Fast Zeta / SOS Transform + Hall's Marriage Theorem | Wave 5B (#F3) | **`CP-VI.5`** ($\to$ `Ch 24`) |
| **ARC 110 D** | `#055` | Binomial Coefficient is Fun | Vandermonde Convolution $\prod (1-x)^{-(A_i+1)}$ | Wave 1B (#16), Wave 2B (#A6) | **`Ch 06 [SS-2]`** |
| **ARC 123 F** | `#056` | Arithmetic Progression | Non-Homogeneous Causal Recurrence via CDQ / Relaxed Convolution | `4B#32` | **`Ch 09 [Adv-1]`** |
| **ARC 134 E** | `#057` | Modulo Nim | $q$-Analogue / Subset Modulo Game Reduction | Wave 5B (#E9) | **`Ch 23 [Int-2]`** |
| **ARC 136 F** | `#058` | Flip Cells | Exponential Parity Walk + Switching-PGF Residue Extraction | Wave 2A (#11), Wave 2B (#E11), Wave 4B (#21), Wave 5B (#B3) | **`CP-IV.6`** ($\to$ `Ch 16`) |
| **ARC 137 F** | `#059` | Overlaps | Implicit Algebraic Chord-Diagram / Tree Equation + Newton | Wave 3B (#19), Wave 4B (#18) | **`Ch 21 [Int-2]`** |
| **ARC 138 E** | `#060` | Decreasing Subsequence | RSK / Greene Theorem Semi-Online Block Convolution | Wave 5A (#22) | **`Ch 09 [SS-1]`** |
| **ARC 138 F** | `#061` | KD-Tree | Kinoshita–Li $O(N \log^2 N)$ Dense Composition / Power Projection | Wave 4A (#P26) | **`CP-V.7`** ($\to$ `Ch 21`) |
| **ARC 139 F** | `#062` | Many Xor Optimization Problems | $q$-Binomial Gaussian Elimination Basis Enumeration | Wave 5B (#E4) | **`Ch 23 [Adv-1]`** |
| **ARC 145 F** | `#063` | Modulo Sum of Increasing Sequences | $q$-Pentagonal / Cyclic Orbit Sum + Good–Lagrange | Wave 4B (#33), Wave 5B (#E3) | **`Ch 23 [Mas-1]`** |
| **ARC 153 D** | `#064` | Sum of Sum of Digits | Carry-Propagation Digit Convolution / Shift | Wave 5B (#D9) | **`Ch 18 [SS-2]`** |
| **ARC 154 F** | `#065` | Dice Game | Coupon Collector Moment EGF + Polynomial Composition | Wave 4A (#P23), Wave 5B (#C8) | **`Ch 21 [Adv-1]`** |
| **AGC 001 E** | `#066` | BBQ Hard | Offset Lattice-Path Vandermonde Shift $\binom{a_i+a_j+b_i+b_j}{a_i+a_j}$ | Wave 1B (#9) | **`Ch 01 [Mas-1]`** |
| **AGC 005 D** | `#067` | ~K Perm Counting | Disjoint Rook Paths + Inclusion-Exclusion Convolution | Wave 2B (#B2) | **`Ch 08 [Adv-1]`** |
| **AGC 005 F** | `#068` | Many Easy Problems | Subtree Size Frequency + Vandermonde / Taylor Shift Convolution | Wave 1A (#12), Wave 1B (#18), Wave 2A (#6), Wave 2B (#A11), Wave 5A (#34), Wave 5B (#A17) | **`CP-V.8`** ($\to$ `Ch 20`) |
| **AGC 013 E** | `#069` | Placing Squares | Combinatorial Split-or-Pass $3 \times 3$ Matrix / Rational OGF | Wave 2B (#D5), Wave 4A (#P11) | **`Ch 05 [Int-2]`** |
| **AGC 021 E** | `#070` | Ball Eat Chameleons | Reflection Principle / Raney's Lemma Weak Ballot Bound | Wave 2A (#18), Wave 3A (#2), Wave 4B (#11) | **`Ch 15 [SS-2]`** |
| **AGC 038 E** | `#071` | Gachapon | Multivariate Min-Max Stopping Time EGF $F'(1)$ | Wave 2B (#E6), Wave 5B (#B4) | **`Ch 14 [Int-2]`** |
| **AGC 043 D** | `#072` | Merge Triplets | Prefix-Max Cycle Decomposition + Constrained $1,2,3$-Cycle EGF | Wave 2B (#C3), Wave 5A (#13) | **`Ch 19 [Mas-1]`** |
| **AGC 054 E** | `#073` | ZigZag Break | Difference Cancellation / Telescoping Rational Series | Wave 2A (#21) | **`Ch 05 [Mas-2]`** |
| **AGC 058 D** | `#074` | Yet Another ABC String | Cyclic Forbidden Substring IE $\frac{1-xyz}{1-(x+y+z)+2xyz}$ + Diagonal | Wave 2B (#C1), Wave 3B (#27), Wave 4A (#P15), Wave 4B (#27), Wave 5A (#31), Wave 5B (#C16) | **`Ch 16 [Adv-2]`** |
| **AGC 060 D** | `#075` | Same Generating Function | Square of Eulerian / Alternation GF via CDQ NTT | Wave 2B (#C6) | **`Ch 09 [Mas-2]`** |
| **AGC 070 C** | `#076` | No Clar | Bivariate Ballot / Catalan Path Pair Extraction | Wave 3A (#20) | **`Ch 15 [Mas-1]`** |
| **EDPC M** | `#077` | Candies | Prefix-Sum Optimization of $\prod \frac{1-x^{a_i+1}}{1-x}$ | Wave 1B (#2) | **`Ch 01 [Int-2]`** |
| **Typical90 #065** | `#078` | RGB Balls 2 | 2-Way Split Convolution + Lower Bound Filtering | Wave 4A (#P1) | **`CP-I.1`** ($\to$ `Ch 01`) |
| **JSC 2019 Qual F** | `#079` | Candy Retribution | 2-Parameter Harmonic Bounded-Range IE $H(S,a,b) = [x^{S-Ma}]\frac{(1-x^{b+1})^{N-M}}{(1-x)^{N+1}}$ | Wave 1B (#15) | **`CP-I.5`** ($\to$ `Ch 03`) |
| **KUPC 2019 K** | `#080` | One or All | Projective Möbius Substitution $(1-x)^N A(\frac{1+x}{1-x})$ | Wave 2A (#4), Wave 4B (#10) | **`Ch 06 [Int-2]`** |
| **AISing 2020 F** | `#081` | Two Snuke | 10-Tuple Difference Weight OGF $F(z) = \frac{z^5(1+z)^{11}}{(1-z^2)^{16}}$ + Parity Extraction | Wave 1B (#22) | **`Ch 05 [Adv-2]`** |
| **Toyota 2023 Spring Final E** | `#082` | Replace Digits / Tree Constraint | Expected Value of Random Digit Replacement / Implicit Tree Constraint | Wave 3A (#16) | **`CP-IV.8`** ($\to$ `Ch 14`) |

### 1.3 Codeforces (Main Rounds & Gym)
| Problem ID | Canonical Pool ID | Title | Primary FPS Technique | Wave Entry Pointer(s) | Canonical Curriculum Slot |
| :--- | :-: | :--- | :--- | :--- | :--- |
| **CF 407E / Gym** | `#083` | k-Cycle | Constrained Cycle-Length Permutation EGF $\exp(\sum_{k \in S} \frac{x^k}{k})$ | `1A#21` | **`Ch 04 [Adv-1]`** |
| **CF 438E** | `#084` | The Child and Binary Tree | Quadratic Catalan Equation $C = 1 + C^2 D(x)$ ($\sqrt{\cdot}$ / Newton / CDQ) | Wave 1A (#10), Wave 1B (#20), Wave 2A (#14), Wave 3A (#14), Wave 3B (#13), Wave 4B (#3), Wave 5A (#4), Wave 5B (#A7) | **`Ch 02 [Adv-2]`** |
| **CF 451E** | `#085` | Devu and Flowers | Bounded Composition $\prod \frac{1-x^{f_i+1}}{1-x}$ for $N \le 20, S \le 10^{14}$ | Wave 2B (#A1), Wave 5B (#D2) | **`CP-II.1`** ($\to$ `Ch 06`) |
| **CF 553E** | `#086` | Kyoya and Train | Time-Window DAG Shortest Path via Online CDQ FFT | Wave 5A (#11) | **`Ch 09 [Int-1]`** |
| **CF 623E** | `#087` | Transforming Sequence | Bin-Shift Doubling $F_{2n}(x) = F_n(x) F_n(2^n x)$ + MTT | Wave 1B (#23), Wave 4A (#P6), Wave 5A (#8), Wave 5B (#B7) | **`Syn-04`** |
| **CF 755G** | `#088` | PolandBall and Many Other Balls | Continuant Matrix GF + Hyperbola Residue + $O(K)$ 2nd-Order D-Finite ODE | Wave 2B (#D4), Wave 3A (#3), Wave 3B (#26), Wave 4A (#P14), Wave 4B (#17), Wave 5A (#12) | **`Ch 18 [Adv-2]`** |
| **CF 840C** | `#089` | On the Bench | Adjacent-Block Inclusion-Exclusion via Falling-Factorial EGF | Wave 2B (#B4) | **`Ch 08 [Int-2]`** |
| **CF 848E** | `#090` | Days of Floral Colours | $4 \times 4$ Matrix Rational Denominator + CDQ NTT | Wave 5A (#15) | **`CP-III.1`** ($\to$ `Ch 09`) |
| **CF 891E** | `#091` | Lust | Expected Product Decrement EGF $\prod (a_i - x)$ | Wave 1A (#16), Wave 1B (#21), Wave 2A (#45), Wave 3A (#24) | **`Ch 02 [Mas-2]`** |
| **CF 901E** | `#092` | Periodicovsky | Cyclic Chirp-$Z$ Transform (Bluestein's Algorithm) | Wave 5B (#D10) | **`Ch 07 [Mas-1]`** |
| **CF 917D** | `#093` | Stranger Trees | Weighted Matrix-Tree Determinant Interpolation / Prüfer | Wave 3A (#36), Wave 3B (#3) | **`Ch 13 [Int-1]`** |
| **CF 923E** | `#094` | Perpetual Subtraction | Diagonalization of Pascal / Shift Operator via Taylor Shift | Wave 2A (#2), Wave 5B (#B1) | **`Ch 06 [Adv-1]`** |
| **CF 932E** | `#095` | Team Work | Stirling S2 Expansion $\sum S(K,j) \binom{N}{j} j! 2^{N-j}$ + $O(K)$ `EI 科技` | Wave 1B (#10), Wave 2A (#26), Wave 2B (#A13), Wave 5A (#17) | **`Ch 19 [Int-1]`** |
| **CF 960G** | `#096` | Bandit Blues | Unsigned Stirling S1 $\left[\begin{smallmatrix} n-1 \\ A+B-2 \end{smallmatrix}\right] \binom{A+B-2}{A-1}$ via Doubling Shift | Wave 1A (#23), Wave 2A (#27), Wave 4A (#P7), Wave 4B (#7), Wave 5A (#33) | **`Ch 06 [Adv-2]`** |
| **CF 993E** | `#097` | Nikita and Order Statistics | Prefix-Count Reverse Indexing Difference Convolution | Wave 1B (#17), Wave 2A (#3) | **`Ch 01 [Adv-2]`** |
| **CF 995F** | `#098` | Cowmpany Cowmpensation | Tree DP Polynomial Degree Bound + $O(N)$ Lagrange Interpolation | Wave 5B (#D6) | **`Ch 06 [Mas-1]`** |
| **CF 1025G** | `#099` | Company Acquisitions | Martingale Potential Function $f(x) = 2^x - 1$ | Wave 2B (#E14) | **`CP-IV.3`** ($\to$ `Ch 14`) |
| **CF 1054H** | `#100` | Epic Convolution | 2D Index-Calculus + Mixed-Radix Chirp-$Z$ Transform | Wave 2A (#49), Wave 5B (#D4) | **`CP-II.5`** ($\to$ `Ch 07`) |
| **CF 1096G** | `#101` | Lucky Tickets | $N/2$-th Power of 10-Term Polynomial via `SparseFPS::pow` | Wave 5A (#1) | **`Ch 02 [Int-1]`** |
| **CF 1097G** | `#102` | Vladislav and a Great Legend | Edge-Subset Stirling Expansion $x^K = \sum S(K,j) \binom{x}{j} j!$ on Trees | Wave 2A (#28), Wave 2B (#A14), Wave 5A (#19), Wave 5B (#A14) | **`CP-VI.1`** ($\to$ `Ch 22`) |
| **CF 1109D** | `#103` | Sasha and Interesting Fact | Generalized Cayley Forest Formula $k n^{n-k-1}$ | Wave 4B (#8) | **`Ch 13 [SS-2]`** |
| **CF 1117D** | `#104` | Magic Gems | Sparse Denominator $1/(1-x-x^M)$ + Bostan–Mori | Wave 4A (#P4) | **`Ch 05 [SS-1]`** |
| **CF 1204E** | `#105` | Natasha, Sasha and the Prefix Sums | Reflection Principle on Exceedance Thresholds | Wave 3A (#1) | **`Ch 15 [SS-1]`** |
| **CF 1228E** | `#106` | Another Filling the Grid | 2D Row/Column Inclusion-Exclusion + Binomial Theorem | Wave 2B (#A8) | **`Syn-05`** |
| **CF 1251F** | `#107` | Red-White Fence | $2x(1+2x)^{c_1}(1+x)^{2c_2}$ Frequency Grouping | Wave 1A (#11), Wave 2A (#5), Wave 5A (#32) | **`Ch 01 [Mas-2]`** |
| **CF 1264D2** | `#108` | Beautiful Bracket Sequence (Hard) | Vandermonde Absorption Identity $i \binom{A}{i} = A \binom{A-1}{i-1}$ | Wave 4A (#P12), Wave 5B (#B11) | **`CP-V.2`** ($\to$ `Ch 06`) |
| **CF 1278F** | `#109` | Cards | Expected $K$-th Moment of Binomial via Falling Factorials | Wave 2A (#29) | **`Ch 06 [Mas-2]`** |
| **CF 1326F2** | `#110` | Wise Men (Hard Version) | Partition Subset Convolution + SOS / Möbius Inversion | Wave 2B (#C4), Wave 5B (#F6) | **`Ch 24 [Adv-1]`** |
| **CF 1336E2** | `#111` | Chiori and Doll Picking (Hard) | MacWilliams Dual-Code Krawtchouk Transform ($O(2^{m-r})$) | Wave 4A (#P17), Wave 5B (#E8) | **`Ch 23 [Mas-2]`** |
| **CF 1342E** | `#112` | Placing Rooks | Non-Attacking Rooks with $k$ Empty Columns $\implies S(n, n-k)$ | Wave 2A (#22) | **`Syn-06`** |
| **CF 1349D** | `#113` | Slime and Biscuits | Martingale Stopping Potential + First-Difference Order Reduction | Wave 2A (#12), Wave 2B (#E13), Wave 5A (#25) | **`Ch 14 [Mas-2]`** |
| **CF 1349F2** | `#114` | Slime and Sequences (Hard Version) | Eulerian Bivariate EGF $\to$ Lambert-$W$ Substitution + Lagrange Inversion | `1A#30` | **`Ch 11 [Mas-1]`** |
| **CF 1392H** | `#115` | ZS Shuffles Cards | Memoryless Geometric Stopping PGF + Harmonic Expectation | Wave 2B (#E1) | **`Ch 14 [SS-1]`** |
| **CF 1479E** | `#116` | School Clubs | First-Order Homogeneous Martingale Difference Recurrence | Wave 2B (#E15), Wave 4B (#22), Wave 5A (#26) | **`CP-IV.4`** ($\to$ `Ch 14`) |
| **CF 1510H** | `#117` | Hard Optimization | Tree Interval Covering DP + Minkowskian / FPS Merge | Wave 5B (#A12) | **`CP-VI.3`** ($\to$ `Ch 22`) |
| **CF 1515E** | `#118` | Phoenix and Computers | Bivariate EGF $\frac{1}{1-x(e^y-1)}$ + D-Finite Row Recurrence | Wave 2B (#B1), Wave 5A (#30) | **`Ch 19 [Adv-2]`** |
| **CF 1528F** | `#119` | AmShZ Farm | Cyclic Parking Function / Raney Orbit $\binom{n}{m}n^{n-m}$ + Stirling S2 | Wave 3A (#17) | **`CP-III.5`** ($\to$ `Ch 11`) |
| **CF 1548C** | `#120` | The Three Little Pigs | Polynomial Division $\frac{(1+x)^{3N+3}-1}{(1+x)^3-1}$ in $O(N)$ | Wave 2A (#7), Wave 2B (#A4) | **`Ch 19 [SS-2]`** |
| **CF 1553I** | `#121` | Stairs | $2 \times 2$ Block-Merging Divide-and-Conquer NTT | Wave 4A (#P16), Wave 5B (#A9) | **`CP-VI.2`** ($\to$ `Ch 22`) |
| **CF 1556F** | `#122` | Sports Betting (Strongly Connected Variant) | Strongly Connected Digraphs via Semiring/FPS Inversion | Wave 3A (#37) | **`Ch 13 [Mas-1]`** |
| **CF 1603F** | `#123` | October 18, 2017 | $q$-Binomial Rank Enumeration in $\mathbb{F}_2^k$ | Wave 5B (#E1) | **`Ch 23 [SS-1]`** |
| **CF 1613F** | `#124` | Tree Coloring | Derangement-Style Tree Degree Inclusion-Exclusion $\prod(1 + c_u x)$ | Wave 2A (#36), Wave 5B (#A16) | **`Ch 22 [SS-2]`** |
| **CF 1667E** | `#125` | Centroid Probabilities | Tree Centroid Differential Recurrence + Reverse Convolution | `3A#8` | **`Ch 18 [Adv-1]`** |
| **CF 1687F** | `#126` | Koishi's Unconscious Permutation | Implicit Bivariate / Cycle-Rise Permutation Equations | Wave 3B (#20) | **`Ch 10 [Adv-2]`** |
| **CF 1770G** | `#127` | Koxia and Bracket | Transposed Divide-and-Conquer NTT on Bracket Prefixes | Wave 5B (#B8) | **`Ch 20 [Int-1]`** |
| **CF 1810G** | `#128` | The Maximum Prefix | Backward DP / Kernel Method on Prefix Maxima | Wave 3A (#9), Wave 4B (#4), Wave 5B (#B9) | **`Ch 15 [Adv-1]`** |
| **CF 1821F** | `#129` | Timber | Inclusion-Exclusion on Domino Fall Directions $\frac{1}{1-x-yx^{k+1}(2-x^k)}$ | Wave 4B (#12) | **`Ch 16 [SS-2]`** |
| **CF 1842I** | `#130` | Tenzing and Necklace | Monge / Circular Cut DP + Transposed D&C NTT | Wave 5B (#B17) | **`CP-V.3`** ($\to$ `Ch 20`) |
| **CF 1906J** | `#131` | Count BFS Graphs | Tree / Queue Interval Convolution | Wave 5B (#A10) | **`CP-III.2`** ($\to$ `Ch 09`) |
| **CF 1916F** | `#132` | Group Division | Bipolar Orientation / Biconnected $q$-Analogue | Wave 5B (#E6) | **`Ch 23 [Adv-2]`** |
| **CF 1930I** | `#133` | Counting Is Fun | Implicit Bivariate Binary-String Coverings + Newton | Wave 3B (#24) | **`CP-III.3`** ($\to$ `Ch 10`) |
| **CF 1967E2** | `#134` | Again Counting Arrays (Hard) | Bounded-Wall Reflection Principle ($\pm 1$ Walk between $0$ and $M$) | Wave 3A (#4), Wave 5B (#C14) | **`Ch 15 [Adv-2]`** |
| **CF 1988F** | `#135` | Heartbeat | Prefix-Suffix Maximum DP via Tellegen Transposition | Wave 5B (#B15) | **`CP-V.4`** ($\to$ `Ch 20`) |
| **CF 2006E** | `#136` | Iris's Full Binary Tree | Centroid / Heavy-Light Tree Convolution | Wave 5B (#A15) | **`Ch 22 [Adv-2]`** |
| **CF Gym 102331J** | `#137` | Forbidden Strings | Multi-Pattern Aho–Corasick Correlation Matrix Inversion | Wave 2B (#D3) | **`Ch 08 [Mas-2]`** |
| **CF Gym 102538F** | `#138` | 3D Walk / Quarter Plane | Quarter-Plane Obstinate Kernel / Algebraic Group Involution | `4B#31` | **`Ch 17 [Mas-1]`** |
| **CF Gym 102978H** | `#139` | Harsh Comments / Motzkin | Motzkin Trinomial Radical + Multi-Pattern Goulden–Jackson | Wave 2A (#16), Wave 2B (#D2) | **`Ch 08 [Adv-2]`** |
| **CF Gym 103415K / yukicoder 1341** | `#140` | Gambler's Walk | Asymmetric $+1, -2$ Walk via Small-Root Kernel Factoring | Wave 4B (#14) | **`Ch 15 [Int-2]`** |
| **CF 449D** | `#216` | Jzzhu and Numbers | Superset SOS DP / Fast Zeta Transform + Inclusion-Exclusion (`#216`, `Ch 24 [SS-1]`) | Wave 5B (#F1) | **`Ch 24 [SS-1]`** |
| **CF 1264D1** | `#251` | Beautiful Bracket Sequence (Easy) | Bracket Depth Contribution Sum + Vandermonde Convolution Identity $\sum_i i \binom{a}{i} \binom{b}{c-i}$ | `2A#3` | **`CP-II.3`** ($\to$ `Ch 06`) |
| **CF 622F** | `#252` | The Sum of the k-th Powers | $O(k)$ Consecutive-Point Lagrange Interpolation for $\sum_{i=1}^n i^k$ | `2A#26` | **`CP-II.4`** ($\to$ `Ch 06`) |
| **CF 961G** | `#253` | Partitions | Ch 04 (EGF $\exp$) $\times$ Ch 06 (Stirling S2 Linear Decomposition) $\times$ Ch 14 (Linearity of Expectation) | `2A#25` | **`Syn-14`** |

### 1.4 Luogu (`P2290` – `P8555`)
| Problem ID | Canonical Pool ID | Title | Primary FPS Technique | Wave Entry Pointer(s) | Canonical Curriculum Slot |
| :--- | :-: | :--- | :--- | :--- | :--- |
| **Luogu P2290 / P4430** | `#141` | 树的计数 / 猴猴吃香蕉 | Prüfer Sequence Multinomial Coefficient $\frac{(n-2)!}{\prod (d_i-1)!}$ | Wave 1B (#7) | **`CP-II.8`** ($\to$ `Ch 04`) |
| **Luogu P3311** | `#142` | [SDOI2014] 数数 | Aho–Corasick Automaton Transfer Matrix / Rational GF | Wave 2B (#D3) | **`Syn-07`** |
| **Luogu P3321** | `#143` | [SDOI2015] 序列统计 | Primitive Root Discrete Log + Cyclic Convolution $\bmod (x^{p-1}-1)$ | Wave 5B (#D3) | **`Ch 07 [Int-2]`** |
| **Luogu P3338** | `#144` | [ZJOI2014] 力 | Reverse-Indexing Difference Convolution $\sum q_i q_j / (i-j)^2$ | Wave 1B (#5) | **`CP-I.2`** ($\to$ `Ch 01`) |
| **Luogu P3348** | `#145` | [ZJOI2016] 大森林 | Offline Tree Modification + HLD Polynomial Chain Product | Wave 5B (#A19) | **`Ch 22 [Mas-2]`** |
| **Luogu P3684 / BZOJ 3684** | `#146` | 大朋友和多叉树 | Degree-Constrained Multi-Way Tree Lagrange Inversion $[u^{s-1}](\frac{u}{F^{\langle -1 \rangle}(u)})^s$ | Wave 3B (#25) | **`Ch 12 [Int-1]`** |
| **Luogu P3702** | `#147` | [SDOI2017] 序列计数 | Prime Complementary Sieve + Cyclic Convolution $\bmod (x^p - 1)$ | Wave 1B (#14), Wave 2A (#42) | **`Ch 07 [Adv-1]`** |
| **Luogu P3706** | `#148` | [SDOI2017] 硬币游戏 | Multi-Player Guibas–Odlyzko Correlation Linear System | Wave 2B (#E3) | **`Ch 14 [Adv-1]`** |
| **Luogu P3781 / LOJ 2269** | `#149` | [SDOI2017] 切树游戏 | FWT + Heavy-Light Decomposition + Zero-Count $(\text{val}, \text{cnt})$ Ring | Wave 5B (#A8) | **`Ch 22 [Adv-1]`** |
| **Luogu P3784** | `#150` | [SDOI2017] 遗忘的集合 | Inverse Euler Transform (Recovering Item Set from Subset Sums) | Wave 1B (#25), Wave 5B (#A5) | **`Ch 03 [Mas-1]`** |
| **Luogu P4002** | `#151` | [清华集训2017] 生成树计数 | Algebraic / Prüfer Tree Block Sum $\to$ D-Finite Differential Reduction | `3A#27` | **`Ch 18 [SS-1]`** |
| **Luogu P4091** | `#152` | [HEOI2016] 求和 | Row-Sum of Stirling Numbers of the Second Kind via NTT | Wave 2A (#23) | **`CP-II.2`** ($\to$ `Ch 06`) |
| **Luogu P4389** | `#153` | 付公主的背包 | Harmonic $\ln$-$\exp$ Subset-Sum Compression ($O(M \log M)$) | Wave 1A (#7a), Wave 1B (#25), Wave 2A (#30), Wave 5A (#2), Wave 5B (#A2) | **`Ch 03 [Int-1]`** |
| **Luogu P4456** | `#154` | [CQOI2018] 交错序列 | Bivariate Automaton + $2 \times 2$ Matrix Binary Exponentiation | Wave 5A (#7) | **`Ch 17 [SS-1]`** |
| **Luogu P4491** | `#155` | [HAOI2018] 染色 | Exact-$k$ Color Frequency Binomial Inversion Convolution | Wave 2B (#A7) | **`Ch 08 [Int-1]`** |
| **Luogu P4548** | `#156` | [CTSC2006] 歌唱王国 | KMP Border Polynomial / Guibas–Odlyzko $F'(1) = \sum_{\text{border } L} m^L$ | Wave 1A (#15), Wave 1B (#26), Wave 2B (#E2) | **`Ch 14 [Int-1]`** |
| **Luogu P4705** | `#157` | 玩游戏 | Expected $(a_i+b_j)^k$ via Power-Sum $\ln(1 - a_i x)$ + EGF | Wave 1A (#24), Wave 2A (#33), Wave 5B (#B6) | **`Ch 02 [Adv-1]`** |
| **Luogu P4707** | `#158` | 重返现世 | $k$-th Maximum-Minimum Identity $\min_k(S) = \sum_{T} (-1)^{\lvert T \rvert-k}\binom{\lvert T \rvert-1}{k-1} \min(T)$ | Wave 2B (#E5) | **`CP-IV.1`** ($\to$ `Ch 14`) |
| **Luogu P4727** | `#159` | [HNOI2009] 图的同构记数 | Burnside's Lemma + Partition Cycle Index $Z(S_n)$ | Wave 2A (#39) | **`Ch 03 [Mas-2]`** |
| **Luogu P4747** | `#160` | [CERC2017] Intrinsic Interval | Simple Permutations via Inversion of Substitution | Wave 2B (#B11) | **`CP-III.4`** ($\to$ `Ch 10`) |
| **Luogu P4841** | `#161` | [集训队作业2013] 城市规划 | Labeled Connected Graphs $C(x) = \ln G(x)$ (+ Companion Eulerian Graph $\ln$) | Wave 1A (#9a), Wave 1B (#13), Wave 3A (#31, #32), Wave 5A (#3), Wave 5B (#F2) | **`Ch 04 [Int-1]`** |
| **Luogu P4859** | `#162` | 已经没有什么好害怕的了 | Sort-and-DP + Binomial Inversion Convolution | Wave 2B (#A9) | **`CP-II.7`** ($\to$ `Ch 08`) |
| **Luogu P5206** | `#163` | [WC2019] 数树 | 3-Subtask Tree Intersection ($y^{n-\lvert E_1\cap E_2\rvert}$, Tree DP, $\exp(\frac{n^2y}{1-y}T(x))$) | Wave 2B (#B9) | **`CP-III.8`** ($\to$ `Ch 13`) |
| **Luogu P5219** | `#164` | 无聊的水题 I | Max-Degree Tree Count via Prüfer Bounded-Degree EGF | Wave 3A (#22) | **`Ch 13 [SS-1]`** |
| **Luogu P4389 (0-1 Subset Sum Variant) / AtCoder FPS Subset Sum via ln/exp** | `#165` | Luogu P4389 (0-1 Subset Sum Variant) / AtCoder FPS Subset Sum via ln/exp | Subset-Sum Product $\prod(1 + x^{a_i})$ via Logarithmic Derivative & $\exp$ | Wave 1D (#4), Wave 5B (#C3) | **`Ch 02 [SS-2]`** |
| **Luogu P5281 / LOJ 3044** | `#166` | [ZJOI2019] Minimax 搜索 | Dynamic Tree DP + HLD Rational / Polynomial Chain Product | Wave 5B (#A11) | **`Ch 22 [Mas-1]`** |
| **Luogu P5284** | `#167` | [十二省联考2019] 字符串问题 | Suffix Automaton DAG Path via Segment-Tree / Transposed Optimization | Wave 5B (#B5) | **`Ch 20 [Int-2]`** |
| **Luogu P5293** | `#168` | [HNOI2019] 白兔之舞 | $k \times k$ Matrix Walk Modulo $x^L - 1$ + Bluestein Chirp-$Z$ | Wave 2A (#48), Wave 5B (#D5) | **`Ch 07 [Mas-2]`** |
| **Luogu P5326** | `#169` | [ZJOI2019] 开关 | Switching-Walk EGF $F = G * H \implies F'(1) = \frac{d}{dx}(G/H)\big\rvert_{x=1}$ | Wave 2B (#E10), Wave 5B (#A13) | **`CP-IV.2`** ($\to$ `Ch 14`) |
| **Luogu P5327** | `#170` | [ZJOI2019] 语言 | Tree Path Union Maintenance + HLD / Tree Merge | Wave 5B (#A18) | **`CP-VI.4`** ($\to$ `Ch 22`) |
| **Luogu P5339** | `#171` | [TJOI2019] 唱、跳、rap和篮球 | Forbidden `"cxk"` Block Inclusion-Exclusion + Bounded EGF | Wave 2B (#B5), Wave 4A (#P9) | **`Syn-08`** |
| **Luogu P5366** | `#172` | [SNOI2017] 遗失的答案 | Prime-Exponent Divisor Lattice Subset / Möbius Convolution | Wave 5B (#E5) | **`Syn-11`** |
| **Luogu P5400** | `#173` | [CTS2019] 随机立方体 | $k$-th Local Maxima Inclusion-Exclusion + Falling Product | Wave 2B (#A10) | **`Syn-09`** |
| **Luogu P5401** | `#174` | [CTS2019] 珍珠 | Parity-Constrained Frequency EGF $(e^x+e^{-x})/2$ | Wave 1A (#28), Wave 3A (#10) | **`Ch 04 [Mas-2]`** |
| **Luogu P5406** | `#175` | [THUPC2019] 找树 | Mixed Bitwise FWT (AND/OR/XOR) inside Matrix-Tree Determinant | Wave 4A (#P8) | **`CP-VI.7`** ($\to$ `Ch 24`) |
| **Luogu P5434** | `#176` | 有标号荒漠计数 | Labeled Desert / Cactus Forest $T = x \exp\big(\frac{2T-T^2}{2(1-T)}\big)$ | Wave 1A (#27), Wave 3A (#28), Wave 3B (#7), Wave 4B (#6), Wave 5B (#C9) | **`Ch 12 [SS-1]`** |
| **Luogu P5487** | `#177` | [BJOI2019] 勘破神机 | Berlekamp–Massey + Bostan–Mori + Stirling S1 Power Sums | Wave 4A (#P18) | **`Ch 05 [Mas-1]`** |
| **Luogu P5591** | `#178` | 小猪佩奇学数学 | Floor-Sum Roots-of-Unity Filter $\sum_{k=0}^n \binom{n}{k} p^k \lfloor k/w \rfloor$ | Wave 2A (#46) | **`Ch 07 [Int-1]`** |
| **Luogu P5597** | `#179` | 【XR-4】复读 | Unlabeled $k$-ary Tree Automaton Minimization + Coupled Implicit Newton (`#179`, `Ch 10 [Adv-1]`) | Wave 3B (#9/#18) | **`Ch 10 [Adv-1]`** |
| **Luogu P5643** | `#180` | [PKUWC2018] 随机游走 | Tree Random Walk Elimination + SOS Subset Sum | Wave 2B (#E16) | **`CP-VI.8`** ($\to$ `Ch 24`) |
| **Luogu P5668** | `#181` | N-Step Shift | Sequential Lagrange Shift + Multipoint Evaluation | Wave 5B (#D8) | **`Ch 20 [Mas-1]`** |
| **Luogu P5824** | `#182` | 十二重计数法 | Complete Twelvefold Way Master Synthesis | Wave 1A (#25) | **`Syn-10`** |
| **Luogu P5827** | `#183` | 点双连通图计数 | Labeled Biconnected Graphs via Inversion of $Z(x) = x e^{B'(Z(x))}$ | Wave 2B (#B10), Wave 3A (#40), Wave 4B (#19), Wave 5B (#C12) | **`Ch 12 [Mas-1]`** |
| **Luogu P5828** | `#184` | 边双连通图计数 | Labeled 2-Edge-Connected Graphs via Inversion of $W(x) = C'(x e^{W(x)})$ | Wave 3A (#40), Wave 4B (#28), Wave 5B (#C13) | **`Ch 12 [Mas-2]`** |
| **Luogu P5853** | `#185` | Stirling & Falling Factorial Transpose | Transposed Vandermonde / Stirling Basis Conversion | Wave 5B (#B14) | **`CP-V.5`** ($\to$ `Ch 20`) |
| **Luogu P5900** | `#186` | 无标号无根树计数 | Otter's Dissymmetry Theorem $U(x) = R(x) - \frac{1}{2}(R(x)^2 - R(x^2))$ | Wave 1A (#29), Wave 3B (#11) | **`Ch 10 [SS-1]`** |
| **Luogu P6078** | `#187` | [CEOI2004] Sweet | Sparse Denominator $(1-x)^{-n} \prod (1-x^{m_i+1})$ | Wave 1B (#8) | **`Ch 05 [Int-1]`** |
| **Luogu P6189** | `#188` | [NOI Online #1] 跑步 | Integer Partition $O(N\sqrt{N})$ Durfee Square / Pentagonal Number Theorem | Wave 1A (#6) | **`Ch 03 [SS-2]`** |
| **Luogu P6295** | `#189` | 有标号 DAG 计数 | Robinson–Stanley EGF $\sum (-1)^{k-1} \frac{x^k}{k! 2^{\binom{k}{2}}}$ Inversion + $\ln$ | Wave 3A (#34) | **`Ch 13 [Int-2]`** |
| **Luogu P6596** | `#190` | How Many of Them | Connected Graphs with $\le m$ Bridges via Bridge-Block Tree Gluing | Wave 2B (#A12), Wave 3A (#35), Wave 4B (#13) | **`Ch 12 [Adv-1]`** |
| **Luogu P6598** | `#191` | 烷烃计数 (Alkanes) | Pólya $S_3, S_4$ Cycle Index + Otter Dissimilarity | `1A#14` | **`Ch 10 [Mas-1]`** |
| **Luogu P6597** | `#192` | 烯烃计数 (Alkenes) | Double-Bond Unrooted Carbon Trees via Cycle Index | Wave 1A (#14), Wave 3A (#26, #29), Wave 3B (#12), Wave 5A (#23) | **`Ch 10 [Mas-2]`** |
| **Luogu P6620** | `#193` | [省选联考2020 A卷] 组合数问题 | Polynomial-Weighted Binomial Sum via Falling Factorials $k^{\underline{j}}\binom{n}{k} = n^{\underline{j}}\binom{n-j}{k-j}$ | Wave 2A (#24) | **`Ch 06 [Int-1]`** |
| **Luogu P6633** | `#194` | [ZJOI2020] 抽卡 | Coupon Collector of Contiguous Runs via EGF + NTT | Wave 3B (#8) | **`CP-IV.5`** ($\to$ `Ch 14`) |
| **Luogu P6667** | `#195` | [清华集训2016] 如何优雅地求和 | Binomial Sum $\sum \binom{n}{k} x^k (1-x)^{n-k} f(k)$ via Falling Factorials / $O(m)$ ODE | Wave 2A (#25), Wave 4A (#P22), Wave 5A (#18) | **`Ch 19 [Int-2]`** |
| **Luogu P6672** | `#196` | [清华集训2016] 你的生命已如风中残烛 | Raney's Lemma Cyclic Shift $\frac{1}{m+1}$ | Wave 4B (#5) | **`Ch 11 [Int-1]`** |
| **Luogu P7116** | `#197` | [NOIP2020] 微信步数 | High-Dimensional Walk Volume Sum via Bernoulli / Lagrange Interpolation | Wave 5B (#D7) | **`Ch 20 [SS-2]`** |
| **Luogu P7279** | `#198` | 光棱碎片 (Prism Shards) | $2 \times 2$ Polynomial Matrix Heavy-Light Decomposition | Wave 5B (#A4) | **`Ch 22 [Int-2]`** |
| **Luogu P7364** | `#199` | 有标号二分图计数 | 2-Colored Graph EGF $B_2(x) \implies \text{Connected } \frac{1}{2}\ln B_2(x) \implies \text{Total } \sqrt{B_2(x)}$ | Wave 3A (#33), Wave 4B (#20) | **`Ch 13 [Adv-1]`** |
| **Luogu P7438** | `#200` | [AGM 2021] 恐龙 | Implicit Functional Equation + Lagrange Inversion | Wave 3A (#7) | **`Ch 11 [SS-2]`** |
| **Luogu P7439** | `#201` | [KrOI2021] 蕾切尔 | Coupled Catalan Binomial Sum Linearization | Wave 3B (#4) | **`Ch 11 [Int-2]`** |
| **Luogu P7440** | `#202` | [KrOI2021] Feux Follets | Multipoint Evaluation + Transposed Polynomial Divide-and-Conquer | Wave 5B (#B13) | **`Ch 20 [Adv-2]`** |
| **Luogu P7592** | `#203` | 2021 CoE-II E (数树) | Multi-Colored Implicit Tree System + Small-Prime Frobenius / LIF | Wave 3B (#22) | **`Ch 11 [Mas-2]`** |
| **Luogu P7599 (Variant)** | `#204` | Coupled Bipartite Tree Enumeration | 2D Good–Lagrange Bipartite Forest EGF & Jacobian Determinant | `4B#16` | **`Ch 17 [Adv-2]`** |
| **Luogu P8555** | `#205` | 密码学第三次小作业 | Algebraic Series Modulo Small Prime $p \le 10^5$ for $n \le 10^{18}$ | Wave 3B (#21) | **`CP-III.7`** ($\to$ `Ch 11`) |
| **Luogu P3266** | `#220` | [JLOI2015] 骗我呢 | Two-Wall Alternating Reflection Principle Strip Walk (`#220`, `Ch 15 [Int-1]`) | Wave 4B (#3) | **`Ch 15 [Int-1]`** |
| **Luogu P5158** | `R-27` | 【模板】多项式快速插值 | Subproduct Tree + Transposed Evaluation + D&C Interpolation | Wave 5B (#B10), Section 12 (#T34) | Quarantined Template `R-27` (`Ch 20`) |
| **Luogu P5325** | `R-52` | 【模板】Min_25 筛 (Dirichlet GF) | Multiplicative Prime-Power Bell Series & Dirichlet Prefix Sum | Wave 5B (#F8) | Quarantined Template `R-52` (`Ch 24`) |
| **Luogu P5809** | `R-32` | 【模板】多项式复合逆 | Kinoshita–Li Compositional Inverse / Power Projection | Wave 5B (#C11), Section 12 (#T42) | Quarantined Template `R-32` (`Ch 21`) |

### 1.5 UOJ / LibreOJ (LOJ) / QOJ / yukicoder / Other Judges
| Problem ID | Canonical Pool ID | Title | Primary FPS Technique | Wave Entry Pointer(s) | Canonical Curriculum Slot |
| :--- | :-: | :--- | :--- | :--- | :--- |
| **UOJ 50** | `#206` | [UR #3] 链式反应 | Non-Autonomous ODE $F' = \frac{1}{2} A(x) F^2 + 1$ via CDQ / Newton | Wave 1A (#18), Wave 3B (#14) | **`Ch 09 [Mas-1]`** |
| **UOJ 94** | `#207` | [集训队互测2015] 胡策的统计 | Biconnected Subgraphs via Vertex-by-Vertex Set Power Series $\ln$ | Wave 5B (#F7) | **`Ch 24 [Adv-2]`** |
| **UOJ 182** | `#208` | a^-1 + b problem | Alternating Fractional Linear Möbius Transforms + Multipoint Eval | Wave 5B (#B12) | **`Ch 20 [Adv-1]`** |
| **UOJ 390** | `#209` | [UNR #3] 百鸽笼 | Bounded-Capacity Stopping Time EGF $\prod \sum_{j < a_i} \frac{x^j}{j!}$ | Wave 2B (#E7) | **`Ch 14 [Adv-2]`** |
| **UOJ 424** | `#210` | count (Cartesian / Left-Depth Trees) | Chebyshev Rational Function $Q_m(x)/Q_{m+1}(x)$ + Reflection | Wave 2A (#20), Wave 2B (#B10), Wave 3A (#19), Wave 3B (#16), Wave 4A (#P13), Wave 5A (#29), Wave 5B (#A20) | **`Ch 15 [Mas-2]`** |
| **UOJ 450** | `#211` | [集训队作业2018] 复读机 | Mod-$d$ Roots-of-Unity Filter $(e^x + e^{\omega x} + e^{\omega^2 x})^k$ + 2D PDE ($p=19491001$) | Wave 1A (#28), Wave 2A (#44), Wave 2B (#E9), Wave 3A (#10), Wave 3B (#9), Wave 5A (#28) | **`Ch 18 [Mas-1]`** |
| **UOJ 498** | `#212` | 新年的追逐 | Game on Random Graphs via Connected Component EGF | Wave 3A (#39), Wave 4B (#19) | **`Ch 13 [Mas-2]`** |
| **UOJ 514** | `#213` | [UR #19] 通用测评号 | `EI 科技` Truncated Exponential Derivative $\frac{d}{dx}(e^{-x} S_{<a}(x)) = -e^{-x} \frac{x^{a-1}}{(a-1)!}$ | Wave 5A (#24) | **`Ch 19 [Mas-2]`** |
| **UOJ 596** | `#214` | [集训队互测2021] 三维立体混元劲 | 3D Connected Hypergraphs via Twisted Kronecker $\chi$-Graded $\ln G(x,y,z)$ & Radial Derivation $\mathfrak{D} = x\partial_x + y\partial_y + z\partial_z$ in $O(ABC \log(ABC))$ | Wave 4A (#P28), Wave 4B (#30) | **`Ch 16 [Mas-2]`** |
| **UOJ 604** | `#215` | [UR #20] 跳蚤电话 | 2D Lattice Walk / Tree History Transposed Convolution | Wave 4A (#P27), Wave 5B (#B13) | **`CP-V.6`** ($\to$ `Ch 20`) |
| **LOJ 161** | `#217` | 快速阶乘算法 | $O(\sqrt{P} \log P)$ Sampling Shift Evaluation | Wave 5B (#D11) | **`Ch 20 [Mas-2]`** |
| **LOJ 171 / QOJ 6504** | `#218` | 幂投影 (Power Projection) | Kinoshita–Li Transposed Composition $\sum_i w_i [x^i] F(x)^k$ | Wave 5B (#B16) | **`Ch 21 [Adv-2]`** |
| **LOJ 3398** | `#219` | 带加强和多项木 | Multivariate Implicit Tree System + Good–Lagrange Jacobian $\det(I - J_G(u))$ (`#219`, `Ch 17 [Int-2]`) | Wave 3B (#9), Wave 4B (#32) | **`Ch 17 [Int-2]`** |
| **LOJ 6089** | `#221` | 小 Y 的背包计数问题 | $\sqrt{N}$ Split: Small Items DP + Large Items Partition Pentagonal Number | Wave 2A (#37) | **`Ch 03 [Adv-2]`** |
| **LOJ 6261** | `#222` | 一个人的高三 (Lonely Senior Year) | $(1-\sqrt{1-4x})/2x$ Power Series Extraction | Wave 2A (#15) | **`Ch 02 [Int-2]`** |
| **yukicoder 899 / LOJ 6268** | `#223` | 逆オイラー変換 (Inverse Euler) | Möbius Inversion on $\ln A(x)$ to Recover Generator Sequence | Wave 1A (#8) | **`Ch 03 [Adv-1]`** |
| **LOJ 6485** | `#224` | LJJ 学二项式定理 | Mod-4 Roots-of-Unity Filter $(1 \pm x)^n, (1 \pm ix)^n$ | Wave 2A (#40) | **`Ch 07 [SS-1]`** |
| **LOJ 6503** | `#225` | Magic (魔术) | Run-Length Inclusion-Exclusion + D&C NTT | Wave 2A (#38) | **`Ch 09 [Adv-2]`** |
| **LOJ 6538** | `#226` | 烷基计数 加强版 加强版 | Pólya $S_3$ Ternary Tree via Newton or 12-Line Chained Relaxed Convolution | Wave 1A (#14), Wave 3A (#26), Wave 3B (#12), Wave 5A (#23) | **`Ch 10 [SS-2]`** |
| **LOJ 6569** | `#227` | 仙人掌计数 (Cactus Counting) | Labeled Cactus $C = x \exp\big(\frac{2C - C^2}{2(1-C)}\big)$ via Newton / $O(n)$ D-Finite ODE | Wave 3A (#27) | **`Ch 12 [Int-2]`** |
| **LOJ 6671** | `#228` | Unlabeled Phylogenetic Trees | Multivariate Burnside Cycle Index + Good–Lagrange | `3B#17` | **`Ch 17 [Int-1]`** |
| **LOJ 6703** | `#229` | 小 Q 的序列 | Derivative-Free Form 4 LIF $[x^n] H(F(x)) = [u^n] H(u)(1 - u\phi'/\phi)\phi(u)^n$ | `3B#27` | **`Ch 11 [Adv-2]`** |
| **LOJ 6728** | `#230` | U 群把妹王 | Power Projection / Kinoshita–Li / Algebraic-to-ODE $O(n)$ Extraction | Wave 3A (#12, #23), Wave 3B (#18), Wave 4A (#P27), Wave 4B (#24) | **`Ch 18 [Mas-2]`** |
| **LOJ 6729** | `#231` | 幂数 (Powerful Numbers) | Prime-Power Bell Series Division & Dirichlet $\exp/\ln$ | Wave 5B (#F9) | **`Ch 24 [Mas-1]`** |
| **QOJ 4815** | `#232` | 2D Bostan–Mori / Implicit Tree | 2D Rational Bostan–Mori $[x^n y^m] P(x,y)/Q(x,y)$ & Small-Prime Implicit Tree | Wave 3A (#11), Wave 4A (#P20) | **`Ch 16 [Int-2]`** |
| **QOJ 5097 / SOJ 703** | `#233` | 布尔立方 (Boolean Cube) | $q$-Analogue / Subspace Intersection | Wave 5B (#E7) | **`Ch 23 [Int-1]`** |
| **QOJ 8048** | `#234` | Good–Lagrange Multivariate | Multivariate Good–Lagrange Jacobian $\det(I - J_G(u))$ + Newton | `4B#30` | **`Ch 17 [Mas-2]`** |
| **QOJ 8528** | `#235` | FPS Composition / Power Projection | Kinoshita–Li $O(N \log^2 N)$ Algorithm | Wave 4A (#P26), Wave 5B (#C6, #C10) | **`Ch 21 [Mas-1]`** |
| **yukicoder 963** | `#236` | 門松列列 2 | Alternating Permutations $\sec x + \tan x$ via ODE / CDQ | Wave 5A (#9) | **`CP-V.1`** ($\to$ `Ch 19`) |
| **yukicoder 1080** | `#237` | Delannoy / Chebyshev Sum | Rational Bivariate Diagonal | Wave 4A (#P22) | **`Ch 16 [Adv-1]`** |
| **yukicoder 1145** | `#238` | Sum of Powers | Newton's Identities $-\sum_{i=1}^n \frac{-a_i x}{1 - a_i x}$ | Wave 2A (#35) | **`Ch 02 [SS-1]`** |
| **yukicoder 1504** | `#239` | Holonomic Walk | Algebraic-to-D-Finite ODE Compilation for $O(N)$ Walk Extraction | `5A#25` | **`Ch 18 [Int-2]`** |
| **yukicoder 1783** | `#240` | Digits-Sum-Mod-10 Convolution | Radix-10 Multivariate DFT + Twisted Kronecker Truncated Power $F(x)^K$ | Wave 4A (#P25) | **`Ch 16 [Mas-1]`** |
| **yukicoder 1810** | `#241` | Substring Avoidance | Single-Pattern Guibas–Odlyzko Denominator | Wave 2B (#D1) | **`Ch 08 [SS-2]`** |
| **yukicoder 1939** | `#242` | Numbered Colorful Balls | Sparse EGF Convolution | Wave 5A (#6) | **`Ch 19 [SS-1]`** |
| **yukicoder 2104** | `#243` | Fuss–Catalan Diagonal | Asymmetric $(p, q)$-Diagonal Extraction | Wave 4B (#25) | **`CP-IV.7`** ($\to$ `Ch 16`) |
| **yukicoder 3029** | `#244` | Colored Tree (FPS 24) | $2 \times 2$ Jacobian Newton / Substitution Elimination | Wave 3B (#5) | **`Ch 10 [Int-1]`** |
| **51Nod 1728** | `#245` | 不动点 | Iterated Functional $F_k(x) = x e^{F_{k-1}(x)}$ & Cycle-Divisor EGF | Wave 1A (#17), Wave 3A (#30) | **`Ch 12 [SS-2]`** |
| **HDU 5279** | `#246` | YJC plays minecraft | Circular Component DP via $F(x)^{-1}$ | Wave 1A (#26) | **`CP-I.3`** ($\to$ `Ch 01`) |
| **HDU 5855** | `#247` | Less Time, More Profit | Minimum Cut + Rational / Generating Function Optimization | Wave 2A (#9) | **`Syn-12`** |
| **BZOJ 3328** | `#248` | PYXFIB | Matrix Fibonacci + Bluestein / Roots-of-Unity Filter | Wave 2A (#41) | **`Ch 07 [SS-2]`** |
| **CSES 1112** | `#249` | Required Substring | Complementary Pattern-Avoidance OGF | Wave 2B (#D1) | **`Syn-13`** |
| **Project Euler 755** | `#250` | Not Zeckendorf | Fibonacci Subset-Sum Decomposition $\prod(1 + x^{F_k})$ | Wave 2A (#10) | **`CP-I.6`** ($\to$ `Ch 03`) |
| **UOJ 310** | `#254` | [UNR #2] 黎明前的巧克力 | Small-Support Bitwise XOR FWT Eigenvalue Trick $\prod(1 + 2x^{a_i})$ (`#254`, `CP-VI.6`) | Wave 5B (#F2) | **`CP-VI.6`** ($\to$ `Ch 24`) |
### 1.6 Cross-Wave Multi-Perspective Consolidation & Title Disambiguation

1. **Canonical Title & Judge Disambiguation (`#179` vs. `#219`)**:
   - **`#179`** is **`Luogu P5597 — 【XR-4】复读`**, assigned to **`Ch 10 [Adv-1]`** (Unlabeled $k$-ary tree automaton minimization + coupled implicit Newton iteration; Wave `3B#9/#18`).
   - **`#219`** is **`LOJ 3398 — 带加强和多项木`**, assigned to **`Ch 17 [Int-2]`** (Multivariate implicit tree system + Good–Lagrange Jacobian $\det(I - J_G(u))$; Wave `3B#9`, `4B#32`).
2. **The 12 Flagship Dual-Perspective Problems (`CURRICULUM_ARCHITECTURE.md` §5.2)**: Each problem below is counted **once** in its Primary Home Slot and revisited from a second algebraic angle in its Secondary Chapter:

| # | Primary Home Slot | Pool ID | Problem ID & Title | First Perspective (Primary Chapter) | Second Perspective (Revisited Chapter) |
| :-: | :--- | :-: | :--- | :--- | :--- |
| 1 | **`Ch 02 [Int-1]`** | `#101` | **CF 1096G — Lucky Tickets** | **Ch 02 (2.4)**: $O(NK)$ Sparse Power ODE $(1-x)(1-x^{10})G' = k P' G$ (zero NTTs). | **Ch 01 / Ch 07**: Direct NTT cyclic power $\bmod (x^N - 1)$ via roots of unity. |
| 2 | **`Ch 02 [Adv-2]`** | `#084` | **CF 438E — The Child and Binary Tree** | **Ch 02 (2.5)**: Quadratic closed form $F(x) = \frac{2}{1 + \sqrt{1 - 4C(x)}}$ via 1D `sqrt` & `inv`. | **Ch 10 (10.2)**: Direct 1D Fréchet Newton iteration on $\Phi(F) = C(x)F(x)^2 - F(x) + 1 = 0$. |
| 3 | **`Ch 05 [Adv-1]`** | `#040` | **ABC 300 Ex — Fibonacci: Revisited** | **Ch 05 (5.3)**: $O(K \log K \log N)$ Bostan–Mori on $Q(x) = 1 - x - \dots - x^K$. | **Ch 02 (2.4)**: Multiply top/bottom by $(1-x)$ so $(1-x)Q(x) = 1 - 2x + x^{K+1}$ becomes 3-sparse. |
| 4 | **`Ch 06 [Adv-1]`** | `#094` | **CF 923E — Perpetual Subtraction** | **Ch 06 (6.3)**: Two Taylor shifts $P(x-1) \to (k+1)^{-M} \to A(x+1)$ in $O(N \log N)$. | **Ch 13 (13.3)**: Upper-triangular Pascal eigenbasis factorization $T = V \Lambda V^{-1}$ with $V_{i,j} = \binom{i}{j}$. |
| 5 | **`Ch 08 [Int-2]`** | `#089` | **CF 840C — On the Bench** | **Ch 08 (8.3)**: Connected-Component IE (`连续段容斥`) with signed per-color EGF. | **Ch 19 (19.3)**: Laguerre / Truncated Taylor-shift D&C NTT (`#028 ABC 260 Ex`, $N \le 2.5 \times 10^5$). |
| 6 | **`Ch 09 [Int-2]`** | `#023` | **ABC 230 Ex — Bullion** | **Ch 09 (9.4)**: Online Relaxed Convolution updating harmonic multiples $d f_d \to g_{kd}$ in $O(N \log^2 N)$. | **Ch 10 (10.3)**: Offline Pólya Newton Iteration treating $F(x^2), F(x^3), \dots$ as constants in $O(N \log N)$. |
| 7 | **`Ch 10 [Int-1]`** | `#244` | **yukicoder 3029 — Colored Tree (FPS 24)** | **Ch 10 (10.2)**: $2 \times 2$ Coupled Jacobian Newton Iteration on $(F(x), G(x))$ in $O(N \log N)$. | **Ch 09 (9.3)**: Coupled Online Relaxed Convolution solving the same system in $O(N \log^2 N)$ without Jacobians. |
| 8 | **`Ch 11 [SS-2]`** | `#200` | **Luogu P7438 — [AGM 2021] 恐龙** | **Ch 11 (11.2)**: Lagrange–Bürmann Inversion extracting single $[x^N] F(x)^k$ in $O(N \log N)$. | **Ch 21 (21.3)**: Kinoshita–Li `compositional_inverse` computing $[x^n] F(x)$ for all $1 \le n \le N$ in $O(N \log^2 N)$. |
| 9 | **`Ch 12 [Mas-1]`** | `#183` | **Luogu P5827 — 点双连通图计数** | **Ch 12 (12.3)**: Pointed Block-Cut Tree $\ln(R(x)/x) = B'(R(x))$ inverted at single degree $N$ via LIF. | **Ch 21 (21.3) & Ch 24 (24.3)**: All-$n$ extraction via `compose_inv` (`#016 fps_24_w`) & fixed-graph Pointed SPS (`#207 UOJ 94`). |
| 10 | **`Ch 14 [Int-1]`** | `#156` | **Luogu P4548 — [CTSC2006] 歌唱王国** | **Ch 14 (14.2)**: Stopping-time PGF $F(z) + (1-z)G(z) = 1$ + KMP border identity $G(1) = \sum_{k \in \text{Borders}} m^k$. | **Ch 08 (8.4) & Ch 14 (14.5)**: Goulden–Jackson cluster inversion at $z = 1/m$, and Martingale casino betting game. |
| 11 | **`Ch 15 [Int-1]`** | `#220` | **Luogu P3266 — [JLOI2015] 骗我呢** | **Ch 15 (15.1)**: André's Reflection Principle & Kelvin alternating image sum across parallel walls. | **Ch 15 (15.3) & Ch 05**: Bivariate Kernel Method $(u - tuS(u))F(t,u) = \dots$ and rational transfer matrix. |
| 12 | **`CP-IV.6`** | `#058` | **ARC 136 F — Flip Cells** | **Ch 16 (16.3–16.4)**: Bivariate rational / exponential parity walk reduced to algebraic residue extraction. | **Ch 18 (18.2)**: Differentiating the algebraic diagonal into a D-finite ODE and unrolling in $O(N)$ time. |

### 1.7 Quarantined Bare-Template Verification Index (`R-01`–`R-67` $\to$ `Ch 01`–`Ch 24`)

All **67 bare-template unit tests (`R-01`–`R-67`)** are strictly excluded from the 254 pedagogical problem slots and routed as 1-line C++ engine verification footnotes to their home chapters:

| Template ID | Template Problem & Judge Source | Source Wave | Quarantine Rationale & Primitive Verified | Home Chapter |
| :-: | :--- | :-: | :--- | :-: |
| **`R-01`** | **Luogu P3803** — *【模板】多项式乘法 (FFT)* (Luogu) | `1B#L1289` | Pure polynomial multiplication $A(x)B(x)$ with zero combinatorial modeling or index transformation. | **Ch 01** |
| **`R-02`** | **Library Checker** — *`convolution_mod` (Convolution $\bmod 998244353$)* (LC) | `1B#L1289` | Raw NTT unit test. | **Ch 01** |
| **`R-03`** | **Library Checker / Luogu P4245** — *`convolution_mod_1000000007` / 【模板】任意模数多项式乘法 (MTT)* (Luogu) | `1B#L1289` | Tests 3-prime CRT / split-radix FFT precision mechanics in isolation without any generating function derivation. | **Ch 01** |
| **`R-04`** | **Luogu P4238 / Library Checker** — *【模板】多项式乘法逆 / `inv_of_formal_power_series`* (Luogu) | `1A#L1594` | Directly asks for $F(x)^{-1} \pmod{x^n}$. | **Ch 01** |
| **`R-05`** | **Luogu P4512 / Library Checker** — *【模板】多项式除法 / `division_of_polynomials`* (Luogu) | `1B#L1290` | Pure Euclidean quotient/remainder $A(x) = Q(x)B(x) + R(x)$ via reversal $x^n A(1/x)$ with no problem context. | **Ch 05** |
| **`R-06`** | **Luogu P5205 / P5277 / Library Checker** — *【模板】多项式开根 / `sqrt_of_formal_power_series`* (Luogu) | `1A#L1597` | Directly asks for $F(x)^{1/2} \pmod{x^n}$. | **Ch 02** |
| **`R-07`** | **Luogu P4717 / Library Checker** — *【模板】快速莫比乌斯/沃尔什变换 (FMT/FWT) / `bitwise_and_convolution`, `bitwise_xor_convolution`* (Luogu) | `1B#L1289` | Explicitly names OR, AND, and XOR convolutions on given arrays $A, B$. | **Ch 24** |
| **`R-08`** | **Luogu P6097 / Library Checker** — *【模板】子集卷积 / `subset_convolution`* (Luogu) | `5B#L3064` | Raw ranked Zeta/Möbius transform verification without graph/hypergraph connectivity interpretation. | **Ch 24** |
| **`R-09`** | **LOJ #150** — *挑战多项式 (Polynomial Challenge All-in-One Template)* (LOJ #150) | `3B#L1536` | Chains 8 arbitrary polynomial operations ($\sqrt{\cdot}, \exp, \ln, \arcsin$, power, derivative) in a synthetic expression. | **Ch 02** |
| **`R-10`** | **Luogu P5264 / P5265** — *多项式三角函数 / 多项式反三角函数 ($\sin, \cos, \arcsin, \arctan$)* (Luogu) | `3B#L1536` | Artificial template testing $\frac{e^{iF} \pm e^{-iF}}{2}$ and $\int \frac{F'}{\sqrt{1-F^2}}$ without combinatorial meaning (unlike André's alternating permutations). | **Ch 02** |
| **`R-11`** | **Library Checker** — *`product_of_polynomial_sequence`* (LC) | `1B#L1289` | Directly asks for $\prod_{i=1}^n P_i(x)$ given the list of polynomials $P_i(x)$. | **Ch 01** |
| **`R-12`** | **Luogu P4725 / Library Checker** — *【模板】多项式对数函数 (多项式 ln) / `log_of_formal_power_series`* (Luogu) | `1A#L1596` | Computes $\int \frac{F'(x)}{F(x)}dx$ on a given array without teaching connected-component extraction $C(x) = \ln G(x)$ or Newton power sums. | **Ch 02** |
| **`R-13`** | **Luogu P4726 / Library Checker** — *【模板】多项式指数函数 (多项式 exp) / `exp_of_formal_power_series`* (Luogu) | `1A#L1595` | Computes $\exp(F(x))$ on raw input. | **Ch 02** |
| **`R-14`** | **Luogu P5245 / P5273 / Library Checker** — *【模板】多项式快速幂 / `pow_of_formal_power_series`* (Luogu) | `1A#L1598` | Directly asks for $F(x)^k \pmod{x^n}$. | **Ch 02** |
| **`R-15`** | **Library Checker** — *`inv_of_formal_power_series_sparse`* (LC) | `2B#L1473` | Explicitly hands the coder a sparse polynomial with $K$ non-zero entries and asks for $F^{-1}$ in $O(NK)$. | **Ch 02** |
| **`R-16`** | **Library Checker** — *`sqrt_of_formal_power_series_sparse`* (LC) | `5A#L1682` | Explicitly hands a sparse polynomial for $O(NK)$ ODE square root without testing radical diagonal extraction. | **Ch 02** |
| **`R-17`** | **Library Checker** — *`log_of_formal_power_series_sparse`* (LC) | `5A#L1681` | Raw $O(NK)$ ODE logarithmic derivative check. | **Ch 02** |
| **`R-18`** | **Library Checker** — *`exp_of_formal_power_series_sparse`* (LC) | `5A#L1680` | Raw $O(NK)$ ODE exponential check $F' = P' F$. | **Ch 02** |
| **`R-19`** | **Library Checker** — *`pow_of_formal_power_series_sparse`* (LC) | `5A#L1683` | Raw $O(NK)$ ODE power recurrence $P G' = M P' G$. | **Ch 02** |
| **`R-20`** | **Luogu P5395 / Library Checker** — *第二类斯特林数·行 / `stirling_number_of_the_second_kind`* (Luogu) | `1B#L1296` | Directly asks for row $n$ of $\left\{ \begin{matrix} n \\ k \end{matrix} \right\}$. | **Ch 06** |
| **`R-21`** | **Luogu P5396 / Library Checker** — *第二类斯特林数·列 / `stirling_number_of_the_second_kind_fixed_k`* (Luogu) | `2A#L750` | Directly asks for column $k$ of $\left\{ \begin{matrix} n \\ k \end{matrix} \right\} = \frac{n!}{k!}[x^n](e^x - 1)^k$. | **Ch 06** |
| **`R-22`** | **Luogu P5408 / Library Checker** — *第一类斯特林数·行 / `stirling_number_of_the_first_kind`* (Luogu) | `2A#L744` | Directly asks for $x^{\overline{n}} = \prod_{k=0}^{n-1}(x+k)$. | **Ch 06** |
| **`R-23`** | **Luogu P5409 / Library Checker** — *第一类斯特林数·列 / `stirling_number_of_the_first_kind_fixed_k`* (Luogu) | `2A#L746` | Directly asks for $\frac{n!}{k!}[x^n]\left(\ln\frac{1}{1-x}\right)^k$. | **Ch 06** |
| **`R-24`** | **Luogu P5748 / Library Checker** — *集合划分计数 (Bell Numbers) / `bell_number`* (Luogu) | `5B#L3058` | Directly asks for $\exp(e^x - 1) \pmod{x^{n+1}}$ without modeling equivalence relations. | **Ch 04** |
| **`R-25`** | **Library Checker** — *`partition_function` (Pure Unrestricted Partition Template)* (LC) | `1A#L1602` | Directly asks for $\prod_{k \ge 1}(1-x^k)^{-1}$ via Pentagonal Number Theorem with no modeling. | **Ch 03** |
| **`R-26`** | **Luogu P5050 / Library Checker** — *【模板】多项式多点求值 / `multipoint_evaluation`* (Luogu) | `5B#L3052` | Raw subproduct tree remainder evaluation $P(x_i)$ with no transposition or combinatorial context. | **Ch 20** |
| **`R-27`** | **Luogu P5158 / Library Checker** — *【模板】多项式快速插值 / `polynomial_interpolation`* (Luogu) | `5B#L3052` | Raw Lagrange interpolation from arbitrary $(x_i, y_i)$. | **Ch 20** |
| **`R-28`** | **Luogu P5393 / P5394** — *下降幂多项式乘法 / 【模板】下降幂多项式乘法* (Luogu) | `2A#L742` | Explicitly asks to multiply polynomials in the $x^{\underline{k}}$ basis via EGF $e^x$. | **Ch 06** |
| **`R-29`** | **Library Checker** — *`polynomial_taylor_shift` ($F(x+c)$)* (LC) | `1B#L1295` | Directly asks for $F(x+c)$. | **Ch 06** |
| **`R-30`** | **Luogu P5667 / Library Checker** — *拉格朗日插值2 (连续点值平移) / `shift_of_sampling_points_of_polynomial`* (Luogu) | `4A#L1376` | Directly gives $f(0), \dots, f(d)$ and asks for $f(c), \dots, f(c+d)$. | **Ch 20** |
| **`R-31`** | **Luogu P6800 / Library Checker** — *【模板】Chirp Z-Transform / `multipoint_evaluation_on_geometric_sequence`* (Luogu) | `1B#L1297` | Directly asks for $P(a c^k)$ via Bluestein's identity $ij = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$. | **Ch 07** |
| **`R-32`** | **Luogu P5808 / P5809 / Library Checker** — *【模板】多项式复合逆 / `compositional_inverse_of_formal_power_series`* (Luogu) | `1A#L1600` | Directly asks for $G(x)$ such that $F(G(x)) = x$. | **Ch 21** |
| **`R-33`** | **Luogu P5373 / Library Checker** — *【模板】多项式复合函数 / `composition_of_formal_power_series`* (Luogu) | `1A#L1599` | Directly asks for $G(F(x)) \pmod{x^N}$. | **Ch 21** |
| **`R-34`** | **Library Checker** — *`composition_of_formal_power_series_large`* (LC) | `2B#L1457` | Benchmark for Kinoshita–Li $O(N \log^2 N)$ `compose` at $N = 2\cdot 10^5$. | **Ch 21** |
| **`R-35`** | **Library Checker** — *`compositional_inverse_of_formal_power_series_large` & `power_projection_of_formal_power_series`* (LC) | `2B#L1458` | Benchmark for Power Projection + LIF `revert` at $N = 2\cdot 10^5$. | **Ch 21** |
| **`R-36`** | **Luogu P5900 / P4841** — *Template-Only Usage of 无标号树计数 / 城市规划 in Higher Waves* (Luogu) | `3A#L1492` | When treated as a bare 1-line $\ln G(x)$ or Euler transform call in Wave 3 without Otter's dissimilarity or degree constraints (covered in Wave 1A/1B/3B). | **Ch 10** |
| **`R-37`** | **Luogu P6086** — *【模板】Prufer 序列* (Luogu) | `3A#L1490` | Pure constructive bijection between tree parent array and Prüfer array. | **Ch 04** |
| **`R-38`** | **Luogu P6178 / Library Checker** — *【模板】Matrix-Tree 定理 / `counting_spanning_trees_directed`, `counting_spanning_trees_undirected`* (Luogu) | `3A#L1493` | Direct Laplacian determinant computation without multivariate polynomial edge weights or BEST Eulerian reduction. | **Ch 13** |
| **`R-39`** | **Luogu P4723 / Library Checker** — *【模板】常系数齐次线性递推 / `kth_term_of_linearly_recurrent_sequence`* (Luogu) | `1B#L1294` | Hands the coder the linear recurrence coefficients $c_1, \dots, c_k$ and asks for $a_N$. | **Ch 05** |
| **`R-40`** | **Luogu P5487 (Pure BM Template Usage) / Library Checker** — *【模板】Berlekamp–Massey 算法 / `find_linear_recurrence`* (LC) | `2A#L752` | Pure shortest LFSR synthesis on a given sequence $a_0, \dots, a_{2d}$. | **Ch 05** |
| **`R-41`** | **Luogu P7439 (Pure Recurrence Template) / Library Checker** — *【模板】常系数齐次线性递推 (加强版) / `consecutive_terms_of_linear_recurrent_sequence`* (Luogu) | `4A#L1369` | Directly asks for $a_M, a_{M+1}, \dots, a_{M+N-1}$ of a given linear recurrence via transposed Bostan–Mori. | **Ch 05** |
| **`R-42`** | **Library Checker** — *`multivariate_convolution`* (LC) | `4A#L1374` | Raw multidimensional truncated convolution $\pmod{(x_1^{n_1}, \dots, x_k^{n_k})}$ via radix-mixed grading $\chi(\mathbf{i})$. | **Ch 16** |
| **`R-43`** | **Library Checker** — *`multivariate_convolution_cyclic`* (LC) | `4A#L1374` | Raw multidimensional cyclic DFT $\pmod{(x_1^{n_1}-1, \dots, x_k^{n_k}-1)}$. | **Ch 16** |
| **`R-44`** | **Codeforces 632E / Pure Subset-Sum Power Template** — *Thief in a Shop* (CF 632E) | `3B#L1540` | Unweighted boolean knapsack $P(x)^k$ solvable by $O(NK)$ BFS or basic binary-exponentiation FFT without bivariate or implicit structure. | **Ch 01** |
| **`R-45`** | **Luogu P4721** — *【模板】分治 FFT (CDQ Divide-and-Conquer FFT)* (Luogu) | `2B#L1464` | Explicitly gives $f_n = \sum_{i=1}^n f_{n-i} g_i$ (which is actually solvable in $O(N \log N)$ via $(1-G(x))^{-1}$!) and asks for CDQ FFT. | **Ch 09** |
| **`R-46`** | **Codeforces 1264D2 (When Used as 1-Line Vandermonde Identity in Wave 4B)** | `4B#L1883` | In Wave 4B (Kernel Method), `CF 1264D2` is rejected because it collapses to a 1-line Vandermonde sum without boundary reflections (it is placed in Wave 4A/5B instead). | **Ch 06** |
| **`R-47`** | **AtCoder Educational DP Contest M (When Used in Wave 2B IE/PGF)** — *Candies* | `2B#L1468` | Basic sliding-window prefix sum DP (appropriate as a Stepping Stone in Wave 1B, but rejected in Wave 2B where $O(N/s)$ harmonic or multivariate IE is required). | **Ch 01** |
| **`R-48`** | **Library Checker** — *`q_binomial_coefficient_prime_mod` (Pure Gaussian Binomial $\binom{n}{k}_q$ Verification)* (LC) | `5B#L3063` | Directly asks for $\binom{n}{k}_q \pmod P$. | **Ch 23** |
| **`R-49`** | **Luogu P6198 / Pure $(q;q)_n$ Exp/Ln Template** | `5B#L3063` | Raw $\exp\left(-\sum \frac{x^k}{k(1-q^k)}\right)$ template without graph or matrix rank modeling. | **Ch 23** |
| **`R-50`** | **Library Checker** — *`exp_of_set_power_series`* (LC) | `5B#L3065` | Directly asks for $\exp_{\text{SPS}}(F)$ on a $2^N$ array. | **Ch 24** |
| **`R-51`** | **Library Checker** — *`log_of_set_power_series` / `power_projection_of_set_power_series`* (LC) | `5B#L3065` | Raw $O(N^2 2^N)$ ranked FMT logarithm / transposed composition check without graph orientation or biconnectivity context. | **Ch 24** |
| **`R-52`** | **Luogu P5325** — *【模板】Min_25 筛 (Pure Multiplicative Prefix Sum Template)* (Luogu) | `5B#L2989` | Synthetic multiplicative function $f(p^k) = p^k(p^k - 1)$ designed purely to test Min_25 sieve mechanics. | **Ch 24** |
| **`R-53`** | **CSES 1729 & CSES 1725** — *Stick Game & Dice Probability* (CSES) | `2B#L1467` | Elementary $O(NK)$ game/probability DP requiring zero generating function algebra or PGF stopping-time analysis. | **Ch 14** |
| **`R-54`** | **Codeforces 280C & Luogu P1291** — *Game on Tree & `[SHOI2002]` 百事世界杯之旅* (CF 280C) | `2B#L1469` | Introductory Linearity of Expectation $\sum 1/\text{depth}(u)$ and coupon collector $\sum n/i$ exercises requiring no PGF or Min-Max IE. | **Ch 14** |
| **`R-55`** | **UVa 10759 & HDU 4336** — *Dice Throwing & Card Collector* (HDU 4336) | `2B#L1470` | Naive $O(n^2)$ dice DP and $O(2^n)$ bitmask Min-Max IE. | **Ch 14** |
| **`R-56`** | **Luogu P3375 & SPOJ `SUBLEX`** — *`【模板】KMP` & Lexicographical Substring Search* (Luogu) | `2B#L1471` | Pure string-matching / suffix-automaton data structure templates with no Goulden–Jackson cluster GF or PGF renewal system. | **Ch 08** |
| **`R-57`** | **Standard Montmort Derangement Templates** — *$D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$* | `2B#L1472` | Single-constraint textbook derangement formula with no bivariate shift or cycle-length constraint. | **Ch 08** |
| **`R-58`** | **Standard Absorbing Markov Chain Gaussian Elimination Templates** — *$E_u = 1 + \sum P_{uv} E_v$* | `2B#L1474` | Generic $O(V^3)$ dense Gaussian elimination without tridiagonal potential deconvolution or PGF pole cancellation. | **Ch 14** |
| **`R-59`** | **Library Checker** — *`counting_eulerian_circuits`* (LC) | `3A#L1493` | Bare directed BEST Theorem determinant template on a given small graph without sequence/walk modeling. | **Ch 13** |
| **`R-60`** | **CSES 1095** — *Exponentiation ($a^b \bmod 10^9+7$)* (CSES) | `3A#L1494` | Trivial scalar modular binary exponentiation with zero FPS content. | **Ch 01** |
| **`R-61`** | **Luogu P7591** — *2021 CoE-II D (Bare LIF Verification)* (Luogu) | `3B#L1537` | Strictly dominated by its 4-subtask sequel `Luogu P7592` (`2021 CoE-II E: 数树`). | **Ch 11** |
| **`R-62`** | **SPOJ `LARMY` / CSES 2064 / CSES 2187 / Luogu P1044** — *Bracket Sequences I & II / 栈* (CSES) | `3B#L1538` | Elementary 1-line Catalan number $\frac{1}{n+1}\binom{2n}{n}$ or 1-mirror reflection $\binom{2n-k}{n} - \binom{2n-k}{n-1}$ requiring no Kernel Method or Newton iteration. | **Ch 11** |
| **`R-63`** | **Codeforces 896D / AtCoder ABC 205 E / Luogu P1641** — *Nephren Runs a Cinema / White and Black Balls / `[SCOI2010]` 生成字符串* (CF 896D) | `4B#L1880` | Standard 1-mirror ballot reflection $\binom{n+m}{n} - \binom{n+m}{n+k+1}$ or direct Motzkin trinomial expansion without small-branch kernel elimination. | **Ch 15** |
| **`R-64`** | **Yukicoder No. 2677 & SPOJ `FIBOSUM`** — *Simple Linear Recurrence & Matrix Exponentiation Templates* (yukicoder) | `4A#L1370` | Fixed $2\times 2$ / $3\times 3$ matrix exponentiation exercises that do not exercise $O(d \log d \log N)$ Bostan–Mori parity splitting. | **Ch 05** |
| **`R-65`** | **AtCoder ABC 130 E** — *Common Subsequence* (AtCoder) | `4A#L1378` | Basic $O(NM)$ 2D prefix-sum DP where the inputs $S, T$ are arbitrary strings rather than translation-invariant lattice step sets. | **Ch 05** |
| **`R-66`** | **Luogu P5488 & Luogu P6115** — *差分与前缀和 & `【模板】整式递推`* (Luogu) | `5A#L1690` | Direct $(1 \pm x)^{\pm k} \bmod x^n$ template and bare BSGS P-recursive matrix product template without combinatorial D-finite ODE derivation. | **Ch 18** |
| **`R-67`** | **Library Checker** — *`static_top_tree` / `point_set_tree_path_composite_sum` & `polynomial_composite_set_power_series`* (LC) | `5B#L3051` | Pure data-structure / Set Power Series black-box verification templates without combinatorial tree or subgraph modeling. | **Ch 22** |

### 1.8 24-Chapter Master Curriculum Index (`Ch 01`–`Ch 24`), Blind Checkpoints (`CP-I`–`CP-VI`) & Synthesis Reserve (`Syn-01`–`Syn-14`)

Because Tables `1.1`–`1.5` above are ordered by Canonical Pool ID (`#001`–`#017` in `1.1`, `#018`–`#082` in `1.2`, `#083`–`#140` + `#216, #251–#253` in `1.3`, `#141`–`#205` + `#220` in `1.4`, `#206`–`#250` + `#254` in `1.5`), the table below provides the inverse bijection from each chapter `Ch 01`–`Ch 24` to its 8 Ladder Problems (`SS-1..Mas-2`), routed Blind Checkpoints (`CP-I`–`CP-VI`), Synthesis Reserve bridges (`Syn-01`–`Syn-14`), and Quarantined Templates (`R-01`–`R-67`):

| Chapter | 8-Problem Chapter Ladder (`SS-1, SS-2, Int-1, Int-2, Adv-1, Adv-2, Mas-1, Mas-2`) | Routed Blind Checkpoints (`CP-I`–`CP-VI`) | Quarantined Templates (`R-01`–`R-67`) |
| :-: | :--- | :--- | :--- |
| **Ch 01** | **SS-1**: `#019` (ABC 178 D, `1B#4`); **SS-2**: `#043` (ABC 321 F, `1B#3`); **Int-1**: `#004` (`fps_24_g`, `1A#2`); **Int-2**: `#077` (EDPC M, `1B#2`); **Adv-1**: `#049` (ARC 028 D, `1B#6`); **Adv-2**: `#097` (CF 993E, `1B#17`); **Mas-1**: `#066` (AGC 001 E, `1B#9`); **Mas-2**: `#107` (CF 1251F, `1A#11`) | **CP-I.4**: `#032` (ABC 276 G), **CP-I.1**: `#078` (Typical90 #065), **CP-I.2**: `#144` (Luogu P3338), **CP-I.3**: `#246` (HDU 5279) | `R-01`, `R-02`, `R-03`, `R-04`, `R-11`, `R-44`, `R-47`, `R-60` |
| **Ch 02** | **SS-1**: `#238` (yukicoder 1145, `2A#35`); **SS-2**: `#165` (Luogu P4389 (0-1 Subset Sum Variant) / AtCoder FPS Subset Sum via ln/exp, `1D#4`); **Int-1**: `#101` (CF 1096G, `1B#8`); **Int-2**: `#222` (LOJ 6261, `1A#10`); **Adv-1**: `#157` (Luogu P4705, `1A#24`); **Adv-2**: `#084` (CF 438E, `1A#7`); **Mas-1**: `#030` (ABC 267 Ex, `1B#7`); **Mas-2**: `#091` (CF 891E, `1A#16`) | — | `R-06`, `R-09`, `R-10`, `R-12`, `R-13`, `R-14`, `R-15`, `R-16`, `R-17`, `R-18`, `R-19` |
| **Ch 03** | **SS-1**: `#001` (`fps_24_a`, `1A#1`); **SS-2**: `#188` (Luogu P6189, `1A#6`); **Int-1**: `#153` (Luogu P4389, `1A#7a`); **Int-2**: `#009` (`fps_24_n`, `1A#7b`); **Adv-1**: `#223` (yukicoder 899 / LOJ 6268, `1A#8`); **Adv-2**: `#221` (LOJ 6089, `2A#37`); **Mas-1**: `#150` (Luogu P3784, `1B#25`); **Mas-2**: `#159` (Luogu P4727, `2A#39`) | **CP-III.6**: `#035` (ABC 279 Ex), **CP-I.7**: `#037` (ABC 284 Ex), **CP-I.5**: `#079` (JSC 2019 Qual F), **CP-I.6**: `#250` (Project Euler 755) | `R-25` |
| **Ch 04** | **SS-1**: `#002` (`fps_24_e`, `1A#15`); **SS-2**: `#007` (`fps_24_m`, `1A#20`); **Int-1**: `#161` (Luogu P4841, `1A#14`); **Int-2**: `#008` (`fps_24_n`, `3A#2`); **Adv-1**: `#083` (CF 407E / Gym, `1A#21`); **Adv-2**: `#011` (`fps_24_q`, `1B#18`); **Mas-1**: `#041` (ABC 303 Ex, `3A#5`); **Mas-2**: `#174` (Luogu P5401, `1B#14`) | **CP-I.8**: `#024` (ABC 236 Ex), **CP-II.8**: `#141` (Luogu P2290 / P4430) | `R-24`, `R-37` |
| **Ch 05** | **SS-1**: `#104` (CF 1117D, `4A#P4`); **SS-2**: `#034` (ABC 279 G, `2B#B3`); **Int-1**: `#187` (Luogu P6078, `1B#8`); **Int-2**: `#069` (AGC 013 E, `2B#D5`); **Adv-1**: `#040` (ABC 300 Ex, `2A#8`); **Adv-2**: `#081` (AISing 2020 F, `1B#22`); **Mas-1**: `#177` (Luogu P5487, `4A#P18`); **Mas-2**: `#073` (AGC 054 E, `2A#21`) | — | `R-05`, `R-39`, `R-40`, `R-41`, `R-64`, `R-65` |
| **Ch 06** | **SS-1**: `#005` (`fps_24_h`, `2A#1`); **SS-2**: `#055` (ARC 110 D, `1B#16`); **Int-1**: `#193` (Luogu P6620, `2A#24`); **Int-2**: `#080` (KUPC 2019 K, `2A#4`); **Adv-1**: `#094` (CF 923E, `2A#2`); **Adv-2**: `#096` (CF 960G, `1A#23`); **Mas-1**: `#098` (CF 995F, `5B#D6`); **Mas-2**: `#109` (CF 1278F, `2A#29`) | **CP-II.1**: `#085` (CF 451E), **CP-V.2**: `#108` (CF 1264D2), **CP-II.2**: `#152` (Luogu P4091), **CP-II.3**: `#251` (CF 1264D1), **CP-II.4**: `#252` (CF 622F) | `R-20`, `R-21`, `R-22`, `R-23`, `R-28`, `R-29`, `R-46` |
| **Ch 07** | **SS-1**: `#224` (LOJ 6485, `2A#40`); **SS-2**: `#248` (BZOJ 3328, `2A#41`); **Int-1**: `#178` (Luogu P5591, `2A#46`); **Int-2**: `#143` (Luogu P3321, `5B#D3`); **Adv-1**: `#147` (Luogu P3702, `1B#14`); **Adv-2**: `#012` (`fps_24_r`, `2A#47`); **Mas-1**: `#092` (CF 901E, `5B#D10`); **Mas-2**: `#168` (Luogu P5293, `2A#48`) | **CP-II.5**: `#100` (CF 1054H) | `R-31` |
| **Ch 08** | **SS-1**: `#018` (ABC 172 E, `2B#A2`); **SS-2**: `#241` (yukicoder 1810, `2B#D1`); **Int-1**: `#155` (Luogu P4491, `2B#A7`); **Int-2**: `#089` (CF 840C, `2B#B4`); **Adv-1**: `#067` (AGC 005 D, `2B#B2`); **Adv-2**: `#139` (CF Gym 102978H, `2A#16`); **Mas-1**: `#052` (ARC 100 F / LOJ 3395, `2B#B8`); **Mas-2**: `#137` (CF Gym 102331J, `2B#D3`) | **CP-II.6**: `#029` (ABC 266 G), **CP-II.7**: `#162` (Luogu P4859) | `R-56`, `R-57` |
| **Ch 09** | **SS-1**: `#060` (ARC 138 E, `5A#22`); **SS-2**: `#021` (ABC 222 H, `3B#1`); **Int-1**: `#086` (CF 553E, `1B#13`); **Int-2**: `#023` (ABC 230 Ex, `1A#27`); **Adv-1**: `#056` (ARC 123 F, `4B#32`); **Adv-2**: `#225` (LOJ 6503, `2B#B6`); **Mas-1**: `#206` (UOJ 50, `2A#46`); **Mas-2**: `#075` (AGC 060 D, `1B#25`) | **CP-III.1**: `#090` (CF 848E), **CP-III.2**: `#131` (CF 1906J) | `R-45` |
| **Ch 10** | **SS-1**: `#186` (Luogu P5900, `1A#29`); **SS-2**: `#226` (LOJ 6538, `1A#14`); **Int-1**: `#244` (yukicoder 3029, `3B#5`); **Int-2**: `#013` (`fps_24_s`, `1A#30`); **Adv-1**: `#179` (Luogu P5597, `3B#18`); **Adv-2**: `#126` (CF 1687F, `3B#20`); **Mas-1**: `#191` (Luogu P6598, `1A#14`); **Mas-2**: `#192` (Luogu P6597, `1A#14`) | **CP-III.3**: `#133` (CF 1930I), **CP-III.4**: `#160` (Luogu P4747) | `R-36` |
| **Ch 11** | **SS-1**: `#003` (`fps_24_f`, `1A#2`); **SS-2**: `#200` (Luogu P7438, `3B#28`); **Int-1**: `#196` (Luogu P6672, `4B#5`); **Int-2**: `#201` (Luogu P7439, `3B#29`); **Adv-1**: `#010` (`fps_24_p`, `1A#29`); **Adv-2**: `#229` (LOJ 6703, `3B#27`); **Mas-1**: `#114` (CF 1349F2, `1A#30`); **Mas-2**: `#203` (Luogu P7592, `3B#11`) | **CP-III.5**: `#119` (CF 1528F), **CP-III.7**: `#205` (Luogu P8555) | `R-61`, `R-62` |
| **Ch 12** | **SS-1**: `#176` (Luogu P5434, `3A#9`); **SS-2**: `#245` (51Nod 1728, `3A#19`); **Int-1**: `#146` (Luogu P3684 / BZOJ 3684, `3B#25`); **Int-2**: `#227` (LOJ 6569, `3A#7`); **Adv-1**: `#190` (Luogu P6596, `3A#14`); **Adv-2**: `#016` (`fps_24_w`, `3A#11`); **Mas-1**: `#183` (Luogu P5827, `3A#10`); **Mas-2**: `#184` (Luogu P5828, `3A#13`) | — | — |
| **Ch 13** | **SS-1**: `#164` (Luogu P5219, `3A#3`); **SS-2**: `#103` (CF 1109D, `4B#8`); **Int-1**: `#093` (CF 917D, `3A#36`); **Int-2**: `#189` (Luogu P6295, `3A#34`); **Adv-1**: `#199` (Luogu P7364, `3A#33`); **Adv-2**: `#053` (ARC 105 F / LOJ 6539, `1A#20`); **Mas-1**: `#122` (CF 1556F, `3A#37`); **Mas-2**: `#212` (UOJ 498, `3A#39`) | **CP-III.8**: `#163` (Luogu P5206) | `R-38`, `R-59` |
| **Ch 14** | **SS-1**: `#115` (CF 1392H, `2B#E1`); **SS-2**: `#026` (ABC 242 Ex, `2B#E8`); **Int-1**: `#156` (Luogu P4548, `1A#15`); **Int-2**: `#071` (AGC 038 E, `2B#E6`); **Adv-1**: `#148` (Luogu P3706, `2B#E3`); **Adv-2**: `#209` (UOJ 390, `2B#E7`); **Mas-1**: `#039` (ABC 289 Ex, `2B#E12`); **Mas-2**: `#113` (CF 1349D, `2A#12`) | **CP-IV.1**: `#158` (Luogu P4707), **CP-IV.2**: `#169` (Luogu P5326), **CP-IV.3**: `#099` (CF 1025G), **CP-IV.4**: `#116` (CF 1479E), **CP-IV.5**: `#194` (Luogu P6633), **CP-IV.8**: `#082` (Toyota 2023 Spring Final E) | `R-53`, `R-54`, `R-55`, `R-58` |
| **Ch 15** | **SS-1**: `#105` (CF 1204E, `3A#1`); **SS-2**: `#070` (AGC 021 E, `2A#18`); **Int-1**: `#220` (Luogu P3266, `4B#3`); **Int-2**: `#140` (CF Gym 103415K / yukicoder 1341, `4B#14`); **Adv-1**: `#128` (CF 1810G, `3A#9`); **Adv-2**: `#134` (CF 1967E2, `3A#4`); **Mas-1**: `#076` (AGC 070 C, `3A#20`); **Mas-2**: `#210` (UOJ 424, `2A#20`) | — | `R-63` |
| **Ch 16** | **SS-1**: `#048` (ARC 012 D, `1B#11`); **SS-2**: `#129` (CF 1821F, `4B#12`); **Int-1**: `#025` (ABC 240 G, `2A#43`); **Int-2**: `#232` (QOJ 4815, `3A#11`); **Adv-1**: `#237` (yukicoder 1080, `4A#P22`); **Adv-2**: `#074` (AGC 058 D, `2B#A8`); **Mas-1**: `#240` (yukicoder 1783, `4A#P25`); **Mas-2**: `#214` (UOJ 596, `4A#P28`) | **CP-IV.6**: `#058` (ARC 136 F), **CP-IV.7**: `#243` (yukicoder 2104) | `R-42`, `R-43` |
| **Ch 17** | **SS-1**: `#154` (Luogu P4456, `5A#7`); **SS-2**: `#044` (ABC 336 G, `3A#33`); **Int-1**: `#228` (LOJ 6671, `3B#17`); **Int-2**: `#219` (LOJ 3398, `3B#9`); **Adv-1**: `#015` (`fps_24_v`, `1A#33`); **Adv-2**: `#204` (Luogu P7599 (Variant), `4B#16`); **Mas-1**: `#138` (CF Gym 102538F, `4B#31`); **Mas-2**: `#234` (QOJ 8048, `4B#30`) | — | — |
| **Ch 18** | **SS-1**: `#151` (Luogu P4002, `3A#27`); **SS-2**: `#064` (ARC 153 D, `5B#D9`); **Int-1**: `#022` (ABC 226 H, `2B#E2`); **Int-2**: `#239` (yukicoder 1504, `5A#25`); **Adv-1**: `#125` (CF 1667E, `3A#8`); **Adv-2**: `#088` (CF 755G, `2B#D4`); **Mas-1**: `#211` (UOJ 450, `1A#28`); **Mas-2**: `#230` (LOJ 6728, `3A#12`) | — | `R-66` |
| **Ch 19** | **SS-1**: `#242` (yukicoder 1939, `5A#2`); **SS-2**: `#120` (CF 1548C, `2A#7`); **Int-1**: `#095` (CF 932E, `1B#10`); **Int-2**: `#195` (Luogu P6667, `2A#25`); **Adv-1**: `#028` (ABC 260 Ex, `2B#B7`); **Adv-2**: `#118` (CF 1515E, `2B#B1`); **Mas-1**: `#072` (AGC 043 D, `2B#C3`); **Mas-2**: `#213` (UOJ 514, `5A#24`) | **CP-V.1**: `#236` (yukicoder 963) | — |
| **Ch 20** | **SS-1**: `#050` (ARC 033 D, `5B#D1`); **SS-2**: `#197` (Luogu P7116, `5B#D7`); **Int-1**: `#127` (CF 1770G, `5B#B8`); **Int-2**: `#167` (Luogu P5284, `5B#B5`); **Adv-1**: `#208` (UOJ 182, `5B#B12`); **Adv-2**: `#202` (Luogu P7440, `5B#B13`); **Mas-1**: `#181` (Luogu P5668, `5B#D8`); **Mas-2**: `#217` (LOJ 161, `5B#D11`) | **CP-V.8**: `#068` (AGC 005 F), **CP-V.3**: `#130` (CF 1842I), **CP-V.4**: `#135` (CF 1988F), **CP-V.5**: `#185` (Luogu P5853), **CP-V.6**: `#215` (UOJ 604) | `R-26`, `R-27`, `R-30` |
| **Ch 21** | **SS-1**: `#036` (ABC 281 Ex, `2B#B12`); **SS-2**: `#045` (ABC 345 G, `5B#B2`); **Int-1**: `#047` (ABC 387 G, `4A#P25`); **Int-2**: `#059` (ARC 137 F, `3B#22`); **Adv-1**: `#065` (ARC 154 F, `4A#P23`); **Adv-2**: `#218` (LOJ 171 / QOJ 6504, `5B#B16`); **Mas-1**: `#235` (QOJ 8528, `4A#P26`); **Mas-2**: `#017` (`fps_24_x`, `1A#31`) | **CP-V.7**: `#061` (ARC 138 F) | `R-32`, `R-33`, `R-34`, `R-35` |
| **Ch 22** | **SS-1**: `#031` (ABC 269 Ex, `5B#A1`); **SS-2**: `#124` (CF 1613F, `2A#36`); **Int-1**: `#046` (ABC 355 G, `5B#A3`); **Int-2**: `#198` (Luogu P7279, `5B#A4`); **Adv-1**: `#149` (Luogu P3781 / LOJ 2269, `5B#A8`); **Adv-2**: `#136` (CF 2006E, `5B#A15`); **Mas-1**: `#166` (Luogu P5281 / LOJ 3044, `5B#A11`); **Mas-2**: `#145` (Luogu P3348, `5B#A19`) | **CP-VI.1**: `#102` (CF 1097G), **CP-VI.3**: `#117` (CF 1510H), **CP-VI.2**: `#121` (CF 1553I), **CP-VI.4**: `#170` (Luogu P5327) | `R-67` |
| **Ch 23** | **SS-1**: `#123` (CF 1603F, `5B#E1`); **SS-2**: `#033` (ABC 278 Ex, `5B#E2`); **Int-1**: `#233` (QOJ 5097 / SOJ 703, `5B#E7`); **Int-2**: `#057` (ARC 134 E, `5B#E9`); **Adv-1**: `#062` (ARC 139 F, `5B#E4`); **Adv-2**: `#132` (CF 1916F, `5B#E6`); **Mas-1**: `#063` (ARC 145 F, `4B#33`); **Mas-2**: `#111` (CF 1336E2, `4A#P17`) | — | `R-48`, `R-49` |
| **Ch 24** | **SS-1**: `#216` (CF 449D, `5B#F1`); **SS-2**: `#020` (ABC 213 G, `1B#24`); **Int-1**: `#027` (ABC 253 Ex, `5A#14`); **Int-2**: `#042` (ABC 306 Ex, `5B#F5`); **Adv-1**: `#110` (CF 1326F2, `2B#C4`); **Adv-2**: `#207` (UOJ 94, `5B#F7`); **Mas-1**: `#231` (LOJ 6729, `5B#F9`); **Mas-2**: `#038` (ABC 288 Ex, `5B#F10`) | **CP-VI.5**: `#054` (ARC 106 E), **CP-VI.7**: `#175` (Luogu P5406), **CP-VI.8**: `#180` (Luogu P5643), **CP-VI.6**: `#254` (UOJ 310) | `R-07`, `R-08`, `R-50`, `R-51`, `R-52` |

- **Grandmaster Multi-Chapter Synthesis Reserve (`Syn-01`–`Syn-14`, 14 Problems)**: **Syn-01**: `#006` (`fps_24_k`, `1A#4`) $\mid$ **Syn-02**: `#014` (`fps_24_t`, `1A#22`) $\mid$ **Syn-03**: `#051` (ARC 093 F, `2B#C2`) $\mid$ **Syn-04**: `#087` (CF 623E, `1B#23`) $\mid$ **Syn-05**: `#106` (CF 1228E, `2B#A8`) $\mid$ **Syn-06**: `#112` (CF 1342E, `2A#22`) $\mid$ **Syn-07**: `#142` (Luogu P3311, `2B#D3`) $\mid$ **Syn-08**: `#171` (Luogu P5339, `2B#B5`) $\mid$ **Syn-09**: `#173` (Luogu P5400, `2B#A10`) $\mid$ **Syn-10**: `#182` (Luogu P5824, `1A#25`) $\mid$ **Syn-11**: `#172` (Luogu P5366, `5B#E5`) $\mid$ **Syn-12**: `#247` (HDU 5855, `2A#9`) $\mid$ **Syn-13**: `#249` (CSES 1112, `2B#D1`) $\mid$ **Syn-14**: `#253` (CF 961G, `2A#25`).

---

## 2. Wave 1A Problem Encyclopedia: Generating Function Foundations & Symbolic Method (`cohort3_wave_1a_modelling_foundations.md`)

> **Full Reference**: See `fps_research/cohort3_wave_1a_modelling_foundations.md`, Section 7 (Lines 859–1587).

### Tier 1: Stepping Stone (`Stepping Stone` — Problems 1–6)

#### Problem 1A-1: AtCoder `fps_24_a` — Snack (Snacks)
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_a` | **Constraints**: $1 \le D, N \le 2.5 \times 10^5$ (or $N, M \le 2.5 \times 10^5$), $\bmod 998244353$.
- **Statement**: Choose $D$ ordered daily snack combinations with total cost $N$ yen, where each day's snack has cost in $\{1, 3, 4, 6\}$ with given type multiplicities $(1, 2, 1, 3)$.
- **Tags**: `[OGF-Seq]`, `[Poly-Pow]` | **Diagnostic Signal**: Ordered sequence of $D$ independent choices summing to $N \implies [x^N] P(x)^D$.
- **3-Tier Hints**: (1) Write the single-day OGF $P(x) = x + 2x^3 + x^4 + 3x^6$. (2) Factor out $x^D$ so $P(x)/x = 1 + 2x^2 + x^3 + 3x^5$ has constant term $1$. (3) Compute $[x^{N-D}] \exp(D \ln(P(x)/x))$ in $O(N \log N)$ time or use the $O(N)$ D-finite ODE $(P/x) F' = D (P/x)' F$.
- **Solution Formula**: $[x^{N-D}] (1 + 2x^2 + x^3 + 3x^5)^D \bmod 998244353$.

#### Problem 1A-2: AtCoder `fps_24_g` — Coin
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_g` | **Constraints**: $N, M \le 5000, L \le M$ (sliding-window coin change) or $N, M \le 2.5 \times 10^5$, $\bmod 998244353$.
- **Statement**: For each sliding window $[k, k+L-1] \subseteq [1, M]$ of coin denominations ($k = 1, \dots, M-L+1$), count the number of ways to make change for total value $N$ using an unbounded supply of coins in $[k, k+L-1]$. (Also covers the length-$N$ non-decreasing sequence partition variant.)
- **Tags**: `[OGF-MSet]`, `[Reversible-DP]` | **Diagnostic Signal**: Sliding window of unbounded knapsack $\prod_{v=k}^{k+L-1} (1-x^v)^{-1} \bmod x^{N+1}$.
- **3-Tier Hints**: (1) Unbounded knapsack over $[k, k+L-1]$ has OGF $\prod_{v=k}^{k+L-1} (1-x^v)^{-1}$. (2) Inserting coin $v$ multiplies by $(1-x^v)^{-1}$ ($f_i \gets f_i + f_{i-v}$ forward for $i = v \dots N$). (3) Removing coin $v$ multiplies by $(1-x^v)$ ($f_i \gets f_i - f_{i-v}$ backward for $i = N \dots v$).
- **Solution Formula**: Sliding-window $O(N)$ update per step, total $O(N(M+L))$ time.

#### Problem 1A-3: AtCoder `fps_24_d` — Sequence 2
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_d` | **Constraints**: $N, M \le 2.5 \times 10^5$, $\bmod 998244353$.
- **Statement**: Count sequences of length $N$ over $\{1, \dots, M\}$ under two equivalent FPS perspectives: (i) frequency-factorial weighted sequences where value $v$ appearing $c_v$ times contributes weight $c_v!$ (Borel–Laplace bridge), or (ii) sequences with prescribed adjacent/distinctness parity constraints solved via signed EGF convolution.
- **Tags**: `[EGF-Set]`, `[Laplace-Bridge]` | **Diagnostic Signal**: Multiplying by $c_v!$ inside an EGF turns $\frac{x^{c_v}}{c_v!}$ back into the OGF $x^{c_v}$; adjacent-difference constraints reduce to $N! \sum_{k=0}^N \frac{(M-N+k)^{\underline{k}}}{k!} (-1)^k$.
- **3-Tier Hints**: (1) Set up the EGF over the $M$ values. (2) Under the Borel–Laplace transform $\mathcal{L}\{x^k/k!\} = x^k$, factorial weights convert EGF products into OGF powers. (3) Extract $[x^N]$ via polynomial power/inversion or closed-form alternating sum.
- **Solution Formula**: $N! [x^N] F(x)^M \bmod 998244353$ (Laplace variant) or $N! \sum_{k=0}^N \binom{M-N+k}{k} (-1)^k \bmod 998244353$.

#### Problem 1A-4: AtCoder `fps_24_k` — Permutation (Derangements & Disjoint Derangement Pairs)
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_k` | **Constraints**: $N \le 2.5 \times 10^5$, $\bmod 998244353$.
- **Statement**: Count (i) derangements of $\{1, \dots, N\}$ ($p_i \neq i$ for all $i$), and (ii) pairs of permutations $(P, Q)$ of $\{1, \dots, N\}$ that disagree everywhere ($P_i \neq Q_i$, or $P_i \neq i, Q_i \neq i, P_i \neq Q_i$ via inclusion-exclusion square).
- **Tags**: `[EGF-Cyc]`, `[Symbolic-Set]`, `[IE-Convolution]` | **Diagnostic Signal**: Permutations without fixed points = $\text{SET}(\text{CYC}_{\ge 2}(\mathcal{Z})) \implies D(x) = \frac{e^{-x}}{1-x}$; two coupled conditions square the IE polynomial.
- **3-Tier Hints**: (1) $\text{CYC}_{\ge 2}(x) = \sum_{k \ge 2} \frac{x^k}{k} = \ln\frac{1}{1-x} - x$. (2) Exponentiate: $D(x) = \exp(\ln\frac{1}{1-x} - x) = \frac{e^{-x}}{1-x}$. (3) For the squared IE variant, compute $N! [x^N] \left(\sum_{k=0}^N (-1)^k (N-k)! \frac{x^k}{k!}\right)^2$ via NTT.
- **Solution Formula**: $D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$, or $N! [x^N] \left(\sum_{k=0}^N (-1)^k (N-k)! \frac{x^k}{k!}\right)^2 \bmod 998244353$.

#### Problem 1A-5: AtCoder `fps_24_l` — Permutation 2
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_l` | **Constraints**: $N \le 2.5 \times 10^5$, $\bmod 998244353$.
- **Statement**: Count permutations of $\{1, \dots, N\}$ by cycle structure: (i) permutations whose cycle lengths all belong to an allowed set $S \subseteq \{1, \dots, N\}$, and (ii) permutations with exactly $K$ cycles (unsigned Stirling numbers of the first kind $\left[\begin{matrix} N \\ K \end{matrix}\right]$).
- **Tags**: `[EGF-Cyc]`, `[Poly-Exp]`, `[Stirling-S1]` | **Diagnostic Signal**: Restricted cycle sizes $\implies \exp\left(\sum_{c \in S} \frac{x^c}{c}\right)$; cycle count $y$ $\implies \exp\left(y \ln\frac{1}{1-x}\right) = (1-x)^{-y}$.
- **3-Tier Hints**: (1) A labeled cycle of length $c$ has $(c-1)!$ orientations, so its EGF is $\frac{(c-1)!}{c!} x^c = \frac{x^c}{c}$. (2) A permutation is a set of disjoint cycles, so restricted cycle lengths have EGF $\exp\left(\sum_{c \in S} \frac{x^c}{c}\right)$. (3) Marking each cycle with $y$ gives $N! [x^N] (1-x)^{-y} = \prod_{k=0}^{N-1} (y + k)$, computed in $O(N \log N)$ via doubling Taylor shift.
- **Solution Formula**: $N! [x^N] \exp\left(\sum_{c \in S} \frac{x^c}{c}\right)$ or $[y^K] \prod_{k=0}^{N-1} (y + k) \bmod 998244353$.

#### Problem 1A-6: Luogu P6189 — [NOI Online #1 入门组] 跑步
- **URL**: `https://www.luogu.com.cn/problem/P6189` | **Constraints**: $N \le 10^5$, arbitrary modulus $P \le 10^9$.
- **Statement**: Compute the number of unrestricted integer partitions $p(N) \bmod P$.
- **Tags**: `[OGF-MSet]`, `[Pentagonal-Number]`, `[Durfee-Square]` | **Diagnostic Signal**: Arbitrary modulus $P$ + $O(N \sqrt{N})$ target for $\prod_{k \ge 1} (1-x^k)^{-1}$.
- **3-Tier Hints**: (1) Euler's Pentagonal Number Theorem states $\prod_{k \ge 1} (1-x^k) = 1 + \sum_{m \ge 1} (-1)^m (x^{m(3m-1)/2} + x^{m(3m+1)/2})$. (2) Alternatively, split parts at $B = \lfloor\sqrt{N}\rfloor$ (or decompose by Durfee square size $d$). (3) Invert the sparse pentagonal denominator in $O(N\sqrt{N})$ additions without NTT (works for any modulus $P$).
- **Solution Formula**: $p(n) = \sum_{m \ge 1} (-1)^{m-1} \big(p(n - \frac{m(3m-1)}{2}) + p(n - \frac{m(3m+1)}{2})\big) \bmod P$.

---

### Tier 2: Intermediate (`Intermediate` — Problems 7–15)

#### Problem 1A-7a: Luogu P4389 — 付公主的背包 (Princess Fu's Knapsack)
- **URL**: `https://www.luogu.com.cn/problem/P4389` | **Constraints**: $N, M \le 10^5$, $\bmod 998244353$.
- **Statement**: Given $N$ item types with volumes $v_i \in [1, M]$ (each in unbounded supply), compute the number of ways to fill a knapsack of volume $s$ for all $s = 1, \dots, M$.
- **Tags**: `[Euler-Transform]`, `[Harmonic-Ln-Exp]` | **Diagnostic Signal**: $\prod_{i=1}^N (1 - x^{v_i})^{-1} \bmod x^{M+1}$ where $N, M \le 10^5$.
- **3-Tier Hints**: (1) Count frequency $c_v$ of each volume $v \in [1, M]$. (2) Take the formal logarithm: $\ln F(x) = \sum_{v=1}^M c_v \sum_{k \ge 1} \frac{x^{kv}}{k}$. (3) Accumulate $\ln F(x) \bmod x^{M+1}$ via harmonic sieve in $O(M \log M)$ time, then call one `exp`.
- **Solution Formula**: $F(x) = \exp\left(\sum_{v=1}^M c_v \sum_{k=1}^{\lfloor M/v \rfloor} \frac{x^{kv}}{k}\right) \bmod x^{M+1}$.

#### Problem 1A-7b: AtCoder `fps_24_n` — Coin 2 (Bounded Coin Change via Harmonic $\ln$-$\exp$)
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_n` | **Constraints**: $N, M \le 2.5 \times 10^5$, $\bmod 998244353$.
- **Statement**: Given coins of value $i \in \{1, \dots, M\}$ with multiplicity bound $c_i$ (e.g., at most $i$ coins of value $i$, plus unbounded $1$-yen coins), compute the number of ways to form total sum $N$.
- **Tags**: `[Bounded-Knapsack]`, `[Harmonic-Ln-Exp]` | **Diagnostic Signal**: $\prod_{i=1}^M \frac{1 - x^{i(c_i+1)}}{1 - x^i}$ converts to a harmonic sum under $\ln$!
- **3-Tier Hints**: (1) Write the bounded coin OGF as $F(x) = (1-x)^{-1} \prod_{i=1}^M \frac{1 - x^{i(c_i+1)}}{1 - x^i}$. (2) Take $\ln F(x) = \sum_{k \ge 1} \frac{x^k}{k} + \sum_{i=1}^M \sum_{k \ge 1} \frac{x^{ik} - x^{i(c_i+1)k}}{k}$. (3) Accumulate the coefficients of $\ln F(x) \bmod x^{N+1}$ in $O(N \log N)$ harmonic time and exponentiate via `exp`.
- **Solution Formula**: $[x^N] \exp\left(\sum_{k=1}^N \frac{x^k}{k} + \sum_{i=1}^M \sum_{k \ge 1} \frac{x^{ik} - x^{i(c_i+1)k}}{k}\right) \bmod 998244353$.

#### Problem 1A-8: yukicoder 899 / LOJ 6268 — 逆オイラー変換 (Inverse Euler Transform)
- **URL**: `https://loj.ac/p/6268` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
- **Statement**: Given the unlabeled multiset counts $b_1, \dots, b_N$ where $1 + \sum_{n=1}^N b_n x^n = \prod_{k=1}^N (1 - x^k)^{-a_k} \bmod x^{N+1}$, recover the generator counts $a_1, \dots, a_N$.
- **Tags**: `[Inverse-Euler-Transform]`, `[Poly-Ln]`, `[Mobius-Inversion]` | **Diagnostic Signal**: Inverting $\text{MSET}(\mathcal{A}) = \mathcal{B}$ to find $\mathcal{A}$.
- **3-Tier Hints**: (1) Take $\ln B(x) = \sum_{n=1}^N \frac{x^n}{n} \sum_{d \mid n} d a_d$. (2) Let $L_n = n [x^n] \ln B(x) = \sum_{d \mid n} d a_d$. (3) Apply Dirichlet Möbius inversion: $n a_n = \sum_{d \mid n} \mu(n/d) L_d$.
- **Solution Formula**: $a_n = \frac{1}{n} \sum_{d \mid n} \mu(n/d) \cdot d [x^d] \ln B(x)$ in $O(N \log N)$ time.

#### Problem 1A-9a: Luogu P4841 — [集训队作业2013] 城市规划 (Connected Labeled Graphs)
- **URL**: `https://www.luogu.com.cn/problem/P4841` | **Constraints**: $N \le 1.3 \times 10^5$, $\bmod 1004535809$.
- **Statement**: Count the number of simple connected labeled undirected graphs on $N$ vertices.
- **Tags**: `[EGF-Ln]`, `[Connected-Component]` | **Diagnostic Signal**: Every labeled graph is a $\text{SET}$ of connected components $\implies G(x) = \exp(C(x))$.
- **3-Tier Hints**: (1) Total graphs on $n$ vertices is $g_n = 2^{\binom{n}{2}}$. (2) Form the EGF $G(x) = \sum_{n=0}^N \frac{2^{\binom{n}{2}}}{n!} x^n$. (3) Compute $C(x) = \ln G(x) \bmod x^{N+1}$ and extract $N! [x^N] C(x)$.
- **Solution Formula**: $c_N = N! [x^N] \ln\left(\sum_{n=0}^N 2^{\binom{n}{2}} \frac{x^n}{n!}\right) \bmod 1004535809$.

#### Problem 1A-9b: AtCoder `fps_24_m` — Connected Graph / Tree-or-Unicyclic Components
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_m` | **Constraints**: $N \le 2.5 \times 10^5$, $\bmod 998244353$.
- **Statement**: Count labeled graphs on $N$ vertices under component-level EGF operations: (i) connected graphs via $\ln G(x)$, or (ii) graphs where every connected component has $\le 1$ cycle (trees and unicyclic graphs, i.e., undirected functional graphs).
- **Tags**: `[EGF-Exp]`, `[Cayley-Tree]`, `[Unicyclic-Graph]` | **Diagnostic Signal**: Unrooted trees have EGF $T_{\text{un}}(x) = T(x) - \frac{1}{2} T(x)^2$ where $T(x) = x e^{T(x)}$; unicyclic components have EGF $\frac{1}{2}\ln\frac{1}{1-T(x)} - \frac{T(x)}{2} - \frac{T(x)^2}{4}$.
- **3-Tier Hints**: (1) Let $T(x) = \sum_{n \ge 1} n^{n-1} \frac{x^n}{n!}$ be the EGF of rooted labeled trees. (2) Unrooted trees have EGF $T - \frac{1}{2} T^2$, and simple cycles of rooted trees of length $\ge 3$ have EGF $\frac{1}{2}\ln\frac{1}{1-T} - \frac{T}{2} - \frac{T^2}{4}$. (3) Exponentiating the sum of tree + unicyclic EGFs gives $\frac{\exp(T(x)/2 - 3T(x)^2/4)}{\sqrt{1 - T(x)}}$ (or $\frac{\exp(T - T^2/2)}{\sqrt{1-T}}$ if $1$- and $2$-cycles are allowed).
- **Solution Formula**: $N! [x^N] \frac{\exp(T(x)/2 - 3T(x)^2/4)}{\sqrt{1 - T(x)}}$ (simple graphs) or $N! [x^N] \frac{\exp(T(x) - T(x)^2/2)}{\sqrt{1 - T(x)}} \bmod 998244353$.

#### Problem 1A-10: Codeforces 438E — The Child and Binary Tree
- **URL**: `https://codeforces.com/problemset/problem/438/E` | **Constraints**: $N, M \le 10^5$, $\bmod 998244353$.
- **Statement**: Given a set of allowed node weights $S \subseteq \{1, \dots, M\}$ with indicator OGF $D(x) = \sum_{w \in S} x^w$, count rooted binary trees of total weight $s$ for each $s = 1, \dots, M$.
- **Tags**: `[Catalan-Quadratic]`, `[Poly-Sqrt]`, `[Rationalization]` | **Diagnostic Signal**: $\mathcal{C} = \mathcal{E} + \mathcal{D} \times \mathcal{C} \times \mathcal{C} \implies C(x) = 1 + D(x) C(x)^2$.
- **3-Tier Hints**: (1) Solve the quadratic $D(x) C(x)^2 - C(x) + 1 = 0$. (2) Choose the minus sign so $C(0) = 1$: $C(x) = \frac{1 - \sqrt{1 - 4 D(x)}}{2 D(x)}$. (3) Rationalize the numerator because $D(0) = 0$: $C(x) = \frac{2}{1 + \sqrt{1 - 4 D(x)}}$.
- **Solution Formula**: $C(x) = 2 \big(1 + \sqrt{1 - 4 D(x)}\big)^{-1} \bmod x^{M+1}$ in $O(M \log M)$ time.

#### Problem 1A-11: Codeforces 1251F — Red-White Fence
- **URL**: `https://codeforces.com/problemset/problem/1251/F` | **Constraints**: $N \le 3 \times 10^5, K \le 5, Q \le 3 \times 10^5$, $\bmod 998244353$.
- **Statement**: Given $N$ white boards and $K$ red boards, count valid fence configurations for each query perimeter $Q$, where one red board of height $r_k$ is chosen as the peak, white boards of height $< r_k$ and multiplicity $1$ can be placed on either side ($2$ choices), and white boards of multiplicity $\ge 2$ can be placed on at most both sides.
- **Tags**: `[OGF-Prod]`, `[Poly-Pow]` | **Diagnostic Signal**: Multiplicities $\ge 2$ saturate at $2$, collapsing the factor to $1 + 2x + x^2 = (1+x)^2$, while the red board contributes $2 x^{r_k + 1}$ to the semi-perimeter $Q/2$.
- **3-Tier Hints**: (1) A fence with $m$ white boards and red peak $r_k$ has perimeter $Q = 2(r_k + 1 + m)$, so $m + r_k + 1 = Q/2$. (2) For each red board $r_k$, count white boards $< r_k$ with multiplicity $1$ ($c_1$) and multiplicity $\ge 2$ ($c_2$). Including the red board factor $2x$ (shifted by $r_k$), the OGF is $P_k(x) = 2 x^{r_k+1} (1 + 2x)^{c_1} (1 + x)^{2 c_2}$. (3) Multiply $(1 + 2x)^{c_1}$ and $(1 + x)^{2c_2}$ via NTT in $O(N \log N)$ per red board ($K \le 5$).
- **Solution Formula**: $\text{Ans}(Q) = \sum_{k=1}^K [x^{Q/2}] \Big(2 x^{r_k+1} (1 + 2x)^{c_1(k)} (1 + x)^{2 c_2(k)}\Big) = \sum_{k=1}^K 2 [x^{Q/2 - r_k - 1}] (1 + 2x)^{c_1(k)} (1 + x)^{2 c_2(k)}$.

#### Problem 1A-12: AtCoder AGC 005 F — Many Easy Problems
- **URL**: `https://atcoder.jp/contests/agc005/tasks/agc005_f` | **Constraints**: $N \le 2 \times 10^5$, $\bmod 924844033$.
- **Statement**: For each $k = 1, \dots, N$, find the sum over all $\binom{N}{k}$ vertex subsets $S$ of the size of the minimal subtree spanning $S$.
- **Tags**: `[Lagrangian-Contribution]`, `[Reverse-Convolution]` | **Diagnostic Signal**: Vertex $v$ is NOT in the spanning tree of $S$ iff $S$ lies entirely inside one connected component of $T \setminus \{v\}$.
- **3-Tier Hints**: (1) By linearity of expectation, count for each $v$ how many subsets $S$ of size $k$ use $v$: $\binom{N}{k} - \sum_{C \in \text{comp}(T \setminus v)} \binom{|C|}{k}$. (2) Every component size $|C|$ is either $s_u$ or $N - s_u$ across the $N-1$ edges. Let $c_s$ be the frequency of component size $s$. (3) Compute $\sum_{s=k}^N c_s \binom{s}{k} = \frac{1}{k!} \sum_{s=k}^N (c_s s!) \frac{1}{(s-k)!}$ via one reverse NTT convolution.
- **Solution Formula**: $\text{Ans}_k = N \binom{N}{k} - \frac{1}{k!} [x^{N-k}] \left(\sum_{s=1}^{N-1} c_s s! x^{N-s}\right) \left(\sum_{j=0}^N \frac{x^j}{j!}\right)$.

#### Problem 1A-13: AtCoder ABC 222 H — Beautiful Binary Tree
- **URL**: `https://atcoder.jp/contests/abc222/tasks/abc222_h` | **Constraints**: $N \le 10^7$, $\bmod 998244353$.
- **Statement**: Count beautiful binary trees of size $N$, whose generating function satisfies $T(x) = x(1 + T(x) + T(x)^2)^2$ (with root weight extraction $[x^N] N T(x)$ or Lagrange form).
- **Tags**: `[Implicit-Tree]`, `[Lagrange-Inversion]`, `[D-Finite-ODE]` | **Diagnostic Signal**: $N \le 10^7$ requires $O(N)$ coefficient extraction via Lagrange Inversion or D-finite recurrence.
- **3-Tier Hints**: (1) Rewrite the coupled tree equations into a single algebraic equation $F(x) = x \phi(F(x))$ where $\phi(u) = (1 + 3u + u^2)$ or $(u+1)^2$-variant. (2) Apply Lagrange Inversion $[x^N] F(x) = \frac{1}{N} [u^{N-1}] \phi(u)^N$. (3) Extract the trinomial coefficient in $O(N)$ time via a single sum over binomials!
- **Solution Formula**: $\frac{1}{N} \sum_{k=0}^{N-1} \binom{2N}{N - 1 - k} \binom{N + k - 1}{k} 2^k \bmod 998244353$ (in $O(N)$ time).

#### Problem 1A-14: LibreOJ 6538 / Luogu P6597 & P6598 — 烷基计数 加强版 & 烷烃计数 (Alkyl Radicals & Unrooted Alkanes)
- **URL**: `https://loj.ac/p/6538` / `https://www.luogu.com.cn/problem/P6598` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
- **Statement**: Count (i) unlabeled rooted ternary trees (alkyl radicals $C_n H_{2n+1}$, Luogu P6597 / LOJ 6538) of size $n \le N$ where the $\le 3$ subtrees of each node are unordered, and (ii) unlabeled unrooted trees with maximum vertex degree $\le 4$ (alkanes $C_n H_{2n+2}$, Luogu P6598).
- **Tags**: `[Polya-Cycle-Index]`, `[Newton-Iteration]`, `[Otter-Dissymmetry]` | **Diagnostic Signal**: Unordered $\le 3$ children $\implies Z(S_3; A(x), A(x^2), A(x^3))$; unrooted degree-$\le 4$ trees $\implies Z(S_4)$ vertex-rooted minus $Z(S_2)$ edge-rooted via Otter's Dissymmetry Theorem.
- **3-Tier Hints**: (1) For rooted alkyls, $Z(S_3) = \frac{1}{6}(s_1^3 + 3 s_1 s_2 + 2 s_3)$, so $A(x) = 1 + \frac{x}{6}(A(x)^3 + 3 A(x) A(x^2) + 2 A(x^3))$. During Newton's method modulo $x^{2m}$, $A(x^2)$ and $A(x^3)$ are already known from precision $x^m$, so their derivative w.r.t. $A(x)$ is $0$! (2) For unrooted alkanes (P6598), vertex-rooted trees of degree $\le 4$ have OGF $P(x) = x Z(S_4; A(x)) = \frac{x}{24}\big(A(x)^4 + 6A(x)^2 A(x^2) + 3A(x^2)^2 + 8A(x)A(x^3) + 6A(x^4)\big)$. (3) Edge-rooted alkanes have OGF $Q(x) = Z(S_2; A(x)-1) = \frac{1}{2}\big((A(x)-1)^2 + A(x^2) - 1\big)$, and symmetric edge-rooted alkanes have $S(x) = A(x^2) - 1$, so by Otter's Dissymmetry Theorem $U(x) = P(x) - Q(x) + S(x)$.
- **Solution Formula**: Rooted alkyls: $A_{k+1} = A_k - \frac{A_k - 1 - \frac{x}{6}(A_k^3 + 3 A_k A_k(x^2) + 2 A_k(x^3))}{1 - \frac{x}{2}(A_k^2 + A_k(x^2))}$; Unrooted alkanes: $U(x) = P(x) - \frac{1}{2}\big((A(x)-1)^2 - (A(x^2)-1)\big)$.

#### Problem 1A-15: Luogu P4548 — [CTSC2006] 歌唱王国 (Singing Kingdom)
- **URL**: `https://www.luogu.com.cn/problem/P4548` | **Constraints**: $\sum |S| \le 10^5$, alphabet $m$, $\bmod 10000$.
- **Statement**: Roll an $m$-sided die repeatedly until a target pattern $S$ of length $n$ appears as a contiguous substring. Compute the expected number of rolls $\mathbb{E}[T] \bmod 10000$.
- **Tags**: `[PGF-Stopping-Time]`, `[Guibas-Odlyzko]`, `[KMP-Border]` | **Diagnostic Signal**: First hitting time of pattern $S$ $\implies$ appending $S$ to a non-stopping string $N$ decomposes across all KMP borders of $S$.
- **3-Tier Hints**: (1) Let $F(x)$ be the PGF of stopping time and $G(x)$ be the PGF of strings not yet containing $S$. (2) Two-equation system: $1 + x G(x) = G(x) + F(x)$ and $(x/m)^n G(x) = \sum_{L \in \text{Borders}(S)} (x/m)^{n-L} F(x)$. (3) Evaluate at $x = 1$: since $F(1) = 1$, $\mathbb{E}[T] = F'(1) = G(1) = \sum_{L \in \text{Borders}(S)} m^L$.
- **Solution Formula**: $\mathbb{E}[T] = \sum_{L \in \text{Borders}(S)} m^L \bmod 10000$ in $O(n)$ time via KMP.

---

### Tier 3: Advanced (`Advanced` — Problems 16–26)

#### Problem 1A-16: Codeforces 891E — Lust
- **URL**: `https://codeforces.com/problemset/problem/891/E` | **Constraints**: $N \le 5000, K \le 10^9$, $\bmod 10^9+7$.
- **Statement**: Given $a_1, \dots, a_N$, perform $K$ steps where a random $a_i$ is decremented by $1$ and $\prod_{j \neq i} a_j$ is added to the score. Find the expected total score.
- **Tags**: `[Telescoping-Expectation]`, `[EGF-Prod]` | **Diagnostic Signal**: $\sum_{\text{steps}} \Delta(\prod a_i) = \prod a_i^{(0)} - \prod a_i^{(K)}$, so we only need $\mathbb{E}[\prod_{i=1}^N (a_i - c_i)]$.
- **3-Tier Hints**: (1) By telescoping, total score $= \prod a_i - \mathbb{E}[\prod (a_i - c_i)]$. (2) The EGF of $(a_i - c_i)$ under $c_i$ selections is $\sum_{c \ge 0} (a_i - c) \frac{x^c}{c!} = (a_i - x) e^x$. (3) Multiply $P(x) = \prod_{i=1}^N (a_i - x) = \sum_{j=0}^N p_j x^j$ in $O(N^2)$ and extract $K! [x^K] P(x) e^{Nx} / N^K$.
- **Solution Formula**: $\prod_{i=1}^N a_i - \sum_{j=0}^{\min(N, K)} [x^j]\left(\prod_{i=1}^N (a_i - x)\right) \cdot \frac{K^{\underline{j}}}{N^j} \bmod (10^9+7)$.

#### Problem 1A-17: 51Nod 1728 — 不动点 (Fixed Point of Functions & Iterated Functional Graphs)
- **URL**: `https://www.51nod.com/Challenge/Problem.html#problemId=1728` | **Constraints**: $N \le 2 \times 10^6, k \in \{1, 2\}$ (or general $k$), $\bmod 985661441$.
- **Statement**: Count functions $f : \{1, \dots, n\} \to \{1, \dots, n\}$ satisfying $f^{(k+1)}(x) = f^{(k)}(x)$ for all $x$ (51Nod 1728 for $k \in \{1, 2\}$), as well as the general-$k$ periodic variants $f^{(k)}(x) = x$ (permutations with cycle lengths dividing $k$) and $f^{(k+1)}(x) = f(x)$ (depth-$\le 1$ trees on divisor cycles).
- **Tags**: `[Functional-Digraph]`, `[EGF-Exp]` | **Diagnostic Signal**: $f^{(k+1)} = f^{(k)}$ means every component is a rooted tree of height $\le k$ rooted at a $1$-cycle ($T_k(x) = x \exp(T_{k-1}(x))$); $f^{(k)} = \text{id}$ means cycle lengths divide $k$ ($\exp(\sum_{d \mid k} x^d/d)$).
- **3-Tier Hints**: (1) For $f^{(k+1)} = f^{(k)}$, each component is a tree of height $\le k$ rooted at a fixed point: $T_0(x) = x$, $T_1(x) = x e^x$, $T_2(x) = x e^{x e^x}$, and total EGF $\exp(T_k(x))$. (2) For $k=1$, $n![x^n] e^{x e^x} = \sum_{j=0}^n \binom{n}{j} j^{n-j}$; for $k=2$, expand $e^{x e^{x e^x}}$ via Bell/binomial convolution. (3) For the periodic variant $f^{(k)}(x) = x$, components are cycles of length $d \mid k$, giving EGF $\exp\left(\sum_{d \mid k} \frac{x^d}{d}\right)$ (and replacing $x$ by $x e^x$ gives $f^{(k+1)}(x) = f(x)$).
- **Solution Formula**: $n! [x^n] \exp(T_k(x)) \bmod 985661441$ where $T_0(x) = x, T_m(x) = x \exp(T_{m-1}(x))$; periodic variant: $n! [x^n] \exp\left(\sum_{d \mid k} \frac{x^d}{d}\right)$.

#### Problem 1A-18: UOJ 50 — 链式反应 (Chain Reaction)
- **URL**: `https://uoj.ac/problem/50` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
- **Statement**: Count labeled trees generated by a ternary chain reaction where each firing node has an unordered pair of active children plus passive leaves determined by a given set $A$, yielding $F'(x) = \frac{1}{2} A(x) F(x)^2 + 1$.
- **Tags**: `[Riccati-ODE]`, `[Newton-ODE]`, `[CDQ-NTT]` | **Diagnostic Signal**: Nonlinear first-order differential equation $F'(x) = \frac{1}{2} A(x) F(x)^2 + 1$.
- **3-Tier Hints**: (1) Every step has $F'(x)$ on the LHS and a quadratic in $F(x)$ on the RHS. (2) Method 1 (CDQ NTT): Since $n f_n = [x^{n-1}](1 + \frac{1}{2} A F^2)$, apply semi-online self-convolution CDQ NTT in $O(N \log^2 N)$ time. (3) Method 2 (Newton on ODE): Linearize $G' - A F_k G = \dots$ and solve via integrating factor $\mu(x) = \exp(-\int A F_k dx)$ in $O(N \log N)$ time.
- **Solution Formula**: $F_{k+1} = F_k - e^{I_k} \int e^{-I_k} \big(F_k' - \frac{1}{2} A F_k^2 - 1\big) dx$ where $I_k = \int A F_k dx$.

#### Problem 1A-19: AtCoder ABC 236 Ex — Distinct Multiples
- **URL**: `https://atcoder.jp/contests/abc236/tasks/abc236_h` | **Constraints**: $N \le 16, M \le 10^{18}$, $\bmod 998244353$.
- **Statement**: Count tuples $(A_1, \dots, A_N)$ with $1 \le A_i \le M$, $D_i \mid A_i$, and $A_i \neq A_j$ for all $i \neq j$.
- **Tags**: `[Set-Partition-IE]`, `[Subset-Exp]` | **Diagnostic Signal**: Pairwise distinctness on arbitrary constraints $\implies$ inclusion-exclusion over set partitions where a block of size $k$ has weight $(-1)^{k-1} (k-1)! \lfloor M / \text{lcm}(S) \rfloor$.
- **3-Tier Hints**: (1) In inclusion-exclusion over the complete graph $K_N$, summing $(-1)^{|E|}$ over all connected spanning subgraphs on a vertex set $S$ of size $k$ equals $(-1)^{k-1} (k-1)!$. (2) Thus each subset $S \subseteq \{1, \dots, N\}$ has connected weight $w(S) = (-1)^{|S|-1} (|S|-1)! \lfloor M / \text{lcm}_{i \in S}(D_i) \rfloor$. (3) Take the Set Power Series $\exp$ over the $2^N$ subsets in $O(N^2 2^N)$ or $O(3^N)$ time.
- **Solution Formula**: $[x^{\{1,\dots,N\}}] \exp_{\text{subset}}\left(\sum_{\emptyset \neq S \subseteq [N]} (-1)^{|S|-1} (|S|-1)! \left\lfloor \frac{M}{\text{lcm}(S)} \right\rfloor x^S\right)$.

#### Problem 1A-20: LibreOJ 6539 / AtCoder ARC 105 F — Lights Out on Connected Graph
- **URL**: `https://atcoder.jp/contests/arc105/tasks/arc105_f` | **Constraints**: $N \le 17$ (ARC) or $N \le 10^5$ (LOJ 6539 labeled version).
- **Statement**: Count connected bipartite graphs on $N$ labeled vertices (up to 2-coloring).
- **Tags**: `[Bipartite-EGF]`, `[Poly-Ln]`, `[Poly-Sqrt]` | **Diagnostic Signal**: 2-colored graphs have EGF $\sum \binom{n}{k} 2^{k(n-k)} \frac{x^n}{n!}$; connected bipartite graphs have $2 C_{\text{bip}}(x) = \ln G_{\text{2-col}}(x)$.
- **3-Tier Hints**: (1) Rewrite $k(n-k) = \binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}$ (chirp-$Z$ identity!). (2) Then $G_{\text{2-col}}(x)$ is $2^{\binom{n}{2}}$ times the square of $\sum_{k \ge 0} \frac{2^{-\binom{k}{2}}}{k!} x^k$. (3) Take $\frac{1}{2} \ln G_{\text{2-col}}(x)$ for connected bipartite graphs, and $\exp$ for general bipartite graphs!
- **Solution Formula**: $C_{\text{bip}}(x) = \frac{1}{2} \ln\left(\sum_{n=0}^N 2^{\binom{n}{2}} \frac{x^n}{n!} [y^n] \left(\sum_{k=0}^N \frac{2^{-\binom{k}{2}}}{k!} y^k\right)^2\right)$.

#### Problem 1A-21: AtCoder `fps_24_o` — Rooted Tree (and Generalized Bracket Sequences)
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_o` | **Constraints**: $N \le 2.5 \times 10^5$, $\bmod 998244353$.
- **Statement**: Solve implicit tree/bracket recurrence via Lagrange Inversion: (i) count labeled rooted trees on $N$ vertices where every vertex's out-degree belongs to $S$, or (ii) count generalized ternary/Motzkin bracket sequences satisfying $F(x) = 1 + x F(x) + x^2 F(x)^3$.
- **Tags**: `[Lagrange-Inversion]`, `[Cayley-Tree]` | **Diagnostic Signal**: $T(x) = x \sum_{d \in S} \frac{T(x)^d}{d!}$ or $W(x) = x \phi(W(x))$ with $W(x) = x F(x)$.
- **3-Tier Hints**: (1) By the symbolic method, a labeled rooted tree with child-count in $S$ satisfies $T(x) = x \phi(T(x))$ where $\phi(u) = \sum_{d \in S} \frac{u^d}{d!}$. (2) By Lagrange Inversion, $[x^N] T(x) = \frac{1}{N} [u^{N-1}] \phi(u)^N$. (3) Compute $\phi(u)^N \bmod u^N$ via `pow` in $O(N \log N)$ time (or extract $[u^{N-k}] \binom{N+1}{k} \binom{N+1-k}{N-2k}$ in $O(N)$ for the ternary bracket variant).
- **Solution Formula**: $(N-1)! [u^{N-1}] \left(\sum_{d \in S} \frac{u^d}{d!}\right)^N \bmod 998244353$.

#### Problem 1A-22: AtCoder `fps_24_t` — Colorful
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_t` | **Constraints**: $N \le 2.5 \times 10^5$, $\bmod 998244353$.
- **Statement**: Count colorings under (i) cycle-parity weighting $(-1)^{c-1}$ on permutations, or (ii) adjacent-distinct colorings of $N$ cells where monochrome runs of length $k$ are compressed via $x \mapsto \frac{x}{1+x}$.
- **Tags**: `[Signed-Cycle-EGF]`, `[Poly-Exp]`, `[Run-Compression]` | **Diagnostic Signal**: Cycle sign $(-1)^{c-1}$ gives $\exp(\sum (-1)^{c-1} a_c x^c/c)$; adjacent-distinct runs replace $x^k$ by $\left(\frac{x}{1+x}\right)^k$ inside $(1+x)^N Q(x)$.
- **3-Tier Hints**: (1) For signed cycles, a cycle of length $c$ has sign $(-1)^{c-1}$, giving $C(x) = \sum_{c=1}^N (-1)^{c-1} \frac{a_c}{c} x^c$ and $\exp(C(x))$. (2) For adjacent-distinct sequences, inclusion-exclusion on equal adjacent pairs replaces each block of size $k$ with $\left(\frac{x}{1+x}\right)^k$. (3) Evaluate $Q\left(\frac{x}{1+x}\right)$ via Taylor shift and multiply by $(1+x)^N$.
- **Solution Formula**: $N! [x^N] \exp\left(\sum_{c=1}^N (-1)^{c-1} \frac{a_c}{c} x^c\right)$ or $[x^N] (1+x)^N \sum_{k=1}^N c_k \left(\frac{x}{1+x}\right)^k$.

#### Problem 1A-23: Codeforces 960G — Bandit Blues
- **URL**: `https://codeforces.com/problemset/problem/960/G` | **Constraints**: $N \le 10^5, A, B \le N$, $\bmod 998244353$.
- **Statement**: Count permutations of $\{1, \dots, N\}$ with exactly $A$ prefix maxima and $B$ suffix maxima.
- **Tags**: `[Stirling-S1]`, `[Taylor-Shift-Doubling]` | **Diagnostic Signal**: The global maximum $N$ splits the remaining $N-1$ elements into $A-1$ left records and $B-1$ right records, which by Foata's bijection correspond to $A+B-2$ cycles.
- **3-Tier Hints**: (1) Place $N$ at position $p$; the remaining $N-1$ elements form $A-1$ left-to-right maxima on the left and $B-1$ right-to-left maxima on the right. (2) Summing over all $N-1$ splits gives $\left[\begin{matrix} N-1 \\ A+B-2 \end{matrix}\right] \binom{A+B-2}{A-1}$. (3) Compute the rising factorial $x^{\overline{N-1}} = x(x+1)\cdots(x+N-2)$ in $O(N \log N)$ time via doubling Taylor shift $P_{2m}(x) = P_m(x) P_m(x+m)$.
- **Solution Formula**: $\binom{A+B-2}{A-1} [x^{A+B-2}] \prod_{k=0}^{N-2} (x + k) \bmod 998244353$.

#### Problem 1A-24: Luogu P4705 — 玩游戏 (Playing Games)
- **URL**: `https://www.luogu.com.cn/problem/P4705` | **Constraints**: $N, M, T \le 10^5$, $\bmod 998244353$.
- **Statement**: Given arrays $a_1, \dots, a_N$ and $b_1, \dots, b_M$, compute $\frac{1}{NM} \sum_{i=1}^N \sum_{j=1}^M (a_i + b_j)^k$ for all $k = 1, \dots, T$.
- **Tags**: `[Newton-Power-Sums]`, `[Log-Derivative]`, `[EGF-Convolution]` | **Diagnostic Signal**: Binomial expansion reduces $\sum_{i,j} (a_i+b_j)^k$ to an EGF convolution of the power sums $S_A(p) = \sum_{i=1}^N a_i^p$ and $S_B(q) = \sum_{j=1}^M b_j^q$.
- **3-Tier Hints**: (1) $(a_i + b_j)^k = k! \sum_{p+q=k} \frac{a_i^p}{p!} \frac{b_j^q}{q!}$, so we need the power sums $S_A(p)$ for $p = 0, \dots, T$. (2) The OGF of power sums is $\sum_{p \ge 1} S_A(p) x^p = -x \frac{d}{dx} \ln \prod_{i=1}^N (1 - a_i x)$. (3) Compute $\prod (1 - a_i x)$ via divide-and-conquer NTT in $O(N \log^2 N)$ time, take $-x (\ln P)'$, convert to EGF, and multiply!
- **Solution Formula**: $\text{Ans}_k = \frac{k!}{NM} [x^k] \left(\sum_{p=0}^T \frac{S_A(p)}{p!} x^p\right) \left(\sum_{q=0}^T \frac{S_B(q)}{q!} x^q\right)$.

#### Problem 1A-25: Luogu P5824 — 十二重计数法 (The Twelvefold Way)
- **URL**: `https://www.luogu.com.cn/problem/P5824` | **Constraints**: $n, m \le 2 \times 10^5$, $\bmod 998244353$.
- **Statement**: Given $n$ balls and $m$ boxes, output the number of mappings under all 12 combinations of (Labeled/Unlabeled balls) $\times$ (Labeled/Unlabeled boxes) $\times$ (Unrestricted / Injective $\le 1$ / Surjective $\ge 1$).
- **Tags**: `[Twelvefold-Way]`, `[Stirling-Row]`, `[Partition-Number]` | **Diagnostic Signal**: Unified synthesis of $m^n$, $m^{\underline{n}}$, $m! S(n,m)$, $\sum_{k=0}^m S(n,k)$, $\binom{m}{n}$, $\binom{n+m-1}{n}$, $\binom{n-1}{m-1}$, $p_{\le m}(n)$, $p_{\le m}(n-m)$.
- **3-Tier Hints**: (1) Cases I–IX reduce to factorials and a single row of Stirling numbers of the second kind $S(n, k) = [x^k] \left(\sum \frac{(-1)^i}{i!} x^i\right)\left(\sum \frac{j^n}{j!} x^j\right)$. (2) Cases X–XII reduce to bounded integer partitions $[x^n] \prod_{k=1}^m (1 - x^k)^{-1}$. (3) Compute $\prod_{k=1}^m (1 - x^k)^{-1} \bmod x^{n+1}$ via harmonic $\ln$-$\exp$ or Pentagonal Number Theorem in $O(n \log n)$ time.
- **Solution Formula**: All 12 answers computed in $O((n+m)\log(n+m))$ total time.

#### Problem 1A-26: HDU 5279 — YJC plays minecraft
- **URL**: `https://acm.hdu.edu.cn/showproblem.php?pid=5279` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
- **Statement**: Given $N$ cliques of sizes $a_1, \dots, a_N$ arranged in a circle with $N$ bridge edges between adjacent cliques, count edge subsets where removing all bridges leaves connected components that are trees or connected graphs, such that the global graph stays connected.
- **Tags**: `[Circular-DP]`, `[Poly-Inv]` | **Diagnostic Signal**: Cutting $\le 1$ circular bridge edge reduces the circular recurrence to a linear convolution inverted via $F(x)^{-1}$.
- **3-Tier Hints**: (1) Compute connected spanning subgraphs $c_k$ of $K_k$ for all $k \le \max a_i$ via $\ln$. (2) Either 0 circular bridges are cut ($1$ way per bridge) or 1 circular bridge is cut (and vertices inside the split clique must connect to the two bridge endpoints). (3) Express the linear chain transition via polynomial inversion.
- **Solution Formula**: Solved in $O(N \log N)$ via `ln` and `inv`.

---

### Tier 4: Mastery (`Mastery` — Problems 27–31)

#### Problem 1A-27: Luogu P5434 — 有标号荒漠计数 (Labeled Desert Enumeration)
- **URL**: `https://www.luogu.com.cn/problem/P5434` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
- **Statement**: Count labeled deserts (forests of cactus graphs, where every edge belongs to at most one simple cycle) on $N$ vertices.
- **Tags**: `[Cactus-EGF]`, `[Newton-Iteration]`, `[Lagrange-Inversion]` | **Diagnostic Signal**: A rooted cactus vertex is attached to a set of edges ($T$) and simple cycles of length $\ge 3$ ($\frac{1}{2} \sum_{k \ge 2} T^k = \frac{T^2}{2(1-T)}$).
- **3-Tier Hints**: (1) Rooted cactus EGF satisfies $T(x) = x \exp\left(\frac{2 T(x) - T(x)^2}{2(1 - T(x))}\right)$. (2) Unrooted cactus EGF by Dissymmetry / integration is $\int \frac{T(x)}{x} dx$ (or $T - \frac{1}{2} T^2 - \frac{T^2}{2(1-T)} + \dots$). (3) A desert is a $\text{SET}$ of connected cacti, so take $\exp(C_{\text{unrooted}}(x))$!
- **Solution Formula**: $T(x) = x \exp\left(\frac{2T - T^2}{2(1-T)}\right)$, $C(x) = T(x) + \frac{T(x)^2 - 2T(x)}{2(1-T(x))}$ (or $\int T(x)/x \, dx$), $D(x) = \exp(C(x))$.

#### Problem 1A-28: UOJ 450 / Luogu P5401 — [CTS2019] 珍珠 (Pearls)
- **URL**: `https://www.luogu.com.cn/problem/P5401` | **Constraints**: $D \le 10^5, N, M \le 10^9$, $\bmod 998244353$.
- **Statement**: Count sequences of length $N$ over $\{1, \dots, D\}$ containing at least $M$ pairs of matching pearls (i.e., $\sum_{i=1}^D \lfloor c_i / 2 \rfloor \ge M$, equivalently at most $N - 2M$ odd frequencies).
- **Tags**: `[Roots-of-Unity-Filter]`, `[Binomial-Inversion]`, `[EGF-Parity]` | **Diagnostic Signal**: Parity of frequencies is filtered by $\frac{e^x + e^{-x}}{2}$ (even) and $\frac{e^x - e^{-x}}{2}$ (odd).
- **3-Tier Hints**: (1) Having $\ge M$ pairs is equivalent to having $\le N - 2M$ colors with odd frequency. (2) The number of sequences where a specific set of $k$ colors has odd frequency is $n! [x^n] \left(\frac{e^x - e^{-x}}{2}\right)^k e^{(D-k)x}$. (3) Expand $(e^x - e^{-x})^k e^{(D-k)x}$ via one NTT convolution to get $g_k$, then apply Binomial Inversion in a second NTT convolution!
- **Solution Formula**: $g_k = \binom{D}{k} 2^{-k} \sum_{j=0}^k (-1)^{k-j} \binom{k}{j} (D - 2k + 2j)^N$, $f_i = \sum_{k=i}^D (-1)^{k-i} \binom{k}{i} g_k$.

#### Problem 1A-29: Luogu P5900 — 无标号无根树计数 (Unlabeled Unrooted Trees)
- **URL**: `https://www.luogu.com.cn/problem/P5900` | **Constraints**: $N \le 2 \times 10^5$, $\bmod 998244353$.
- **Statement**: Count unlabeled unrooted trees on $N$ vertices.
- **Tags**: `[Otter-Dissymmetry]`, `[Euler-Transform]`, `[Newton-Tree]` | **Diagnostic Signal**: Rooted unlabeled trees satisfy $R(x) = x \exp\left(\sum_{k \ge 1} \frac{R(x^k)}{k}\right)$; unrooted trees follow by Otter's Dissymmetry Theorem.
- **3-Tier Hints**: (1) Solve $R(x) = x \exp\left(R(x) + \sum_{k \ge 2} \frac{R(x^k)}{k}\right)$ via Newton's method: at precision $x^{2m}$, $S_{\ge 2}(x) = \sum_{k \ge 2} \frac{R(x^k)}{k}$ depends only on known terms of degree $< m$! (2) Thus the Newton step is $R \gets R - \frac{R - x e^{R + S_{\ge 2}}}{1 - R}$. (3) Apply Otter's Dissymmetry Theorem: $U(x) = R(x) - \frac{1}{2}\big(R(x)^2 - R(x^2)\big)$.
- **Solution Formula**: $[x^N]\left(R(x) - \frac{1}{2} R(x)^2 + \frac{1}{2} R(x^2)\right)$ in $O(N \log N)$ time.

#### Problem 1A-30: AtCoder `fps_24_s` — Game
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_s` | **Constraints**: $N \le 2.5 \times 10^5$, $\bmod 998244353$.
- **Statement**: Solve the `fps_24_s` game generating function under both formulations: (i) non-monic quadratic equation $A(x) F(x)^2 + B(x) F(x) + C(x) = 0$ with pole-cancelling branch selection, and (ii) normal-play / bipartite matching game enumeration via bivariate EGF.
- **Tags**: `[Kernel-Method]`, `[Quadratic-Branch]`, `[Poly-Sqrt]` | **Diagnostic Signal**: Non-monic quadratic functional equation with valuation shift in the discriminant.
- **3-Tier Hints**: (1) Complete the square: $(2 A F + B)^2 = B^2 - 4 A C$. (2) Factor out the leading even valuation $x^{2v}$ from $B(x)^2 - 4 A(x) C(x)$ before calling `sqrt`. (3) Select the sign of $\sqrt{B^2 - 4AC}$ so the numerator vanishes to the same order as $2 A(x)$ at $x = 0$.
- **Solution Formula**: $F(x) = \frac{-B(x) \pm x^v \sqrt{(B^2 - 4AC)/x^{2v}}}{2 A(x)} \bmod x^{N+1}$.

#### Problem 1A-31: AtCoder `fps_24_x` — Functional Square Root & Sequence 3
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_x` | **Constraints**: $N \le 8000$ (or $N \le 2.5 \times 10^5$), $\bmod 998244353$.
- **Statement**: Covers both (i) the Functional Square Root problem: given $G(x) = x + g_2 x^2 + \dots + g_N x^N$, find $F(x) = x + f_2 x^2 + \dots + f_N x^N$ such that $F(F(x)) \equiv G(x) \pmod{x^{N+1}}$, and (ii) Sequence 3: count sequences of length $2N$ from $\{1, \dots, K\}$ where all adjacent differences are $\equiv 1 \pmod K$ and sum is $0 \pmod K$, yielding $\sum_{j=0}^{2N} (-1)^{2N-j} \binom{2N}{j} [x^0]\left(\frac{x(1-x^K)}{1-x}\right)^j \bmod (x^K - 1)$.
- **Tags**: `[Functional-Square-Root]`, `[Newton-Composition]`, `[Cyclic-IE]` | **Diagnostic Signal**: Iterated composition $F(F(x)) = G(x)$ tangent to the identity $F(x) = x + \dots$; or cyclic step-1 walk with inclusion-exclusion.
- **3-Tier Hints**: (1) For $F(F(x)) = G(x)$, since $[x^1]G = 1$, choose the branch $[x^1]F = 1$. (2) At Newton step $F_k \to F_k + \Delta$ with $\Delta = O(x^{m+1})$, $F(F(x)) = F_k(F_k(x)) + F_k'(F_k(x)) \Delta(x) + \Delta(F_k(x)) + O(x^{2m+1})$. (3) Extract coefficients in $O(N^2)$ or via Newton + Kinoshita–Li composition in $O(N \log^2 N)$ time.
- **Solution Formula**: Functional square root solved in $O(N^2)$ or $O(N \log^2 N)$; Sequence 3 solved via $\sum_{j \equiv 0 \pmod K} (-1)^{2N-j} \binom{2N}{j} \binom{j}{j/K}$ in $O(N)$ time.

---

## 3. Wave 1B Problem Encyclopedia: DP-to-FPS Translation & Convolution Sums (`cohort3_wave_1b_dp_and_sums.md`)

> **Full Reference**: See `fps_research/cohort3_wave_1b_dp_and_sums.md`, Section 8 (Lines 1301–2174).

### Tier 1: Stepping Stone (`Stepping Stone` — Problems 1–5)

#### Problem 1B-1: AtCoder `fps_24_a` — Snack
- **Cross-Reference**: Identical to **Problem 1A-1** above; in Wave 1B, solved via the $O(N)$ D-finite recurrence $(P/x) F' = D (P/x)' F$.

#### Problem 1B-2: AtCoder EDPC M — Candies
- **URL**: `https://atcoder.jp/contests/dp/tasks/dp_m` | **Constraints**: $N \le 100, K \le 10^5$, $\bmod 10^9+7$.
- **Statement**: Distribute $K$ indistinguishable candies among $N$ children where child $i$ receives at most $a_i$ candies.
- **Tags**: `[Bounded-Knapsack]`, `[Prefix-Sum-DP]` | **Diagnostic Signal**: Multiplying by $\frac{1 - x^{a_i+1}}{1 - x}$ is a two-step operation: multiply by $(1 - x^{a_i+1})$ ($O(K)$ sparse subtraction), then divide by $(1 - x)$ ($O(K)$ prefix sum).
- **3-Tier Hints**: (1) The OGF is $\prod_{i=1}^N \frac{1 - x^{a_i+1}}{1 - x}$. (2) Instead of a $O(K a_i)$ inner loop, view $\frac{1 - x^{a_i+1}}{1 - x} F(x)$ algebraically. (3) First compute $G(x) = \frac{F(x)}{1 - x}$ via prefix sums, then $F_{\text{new}}(x) = (1 - x^{a_i+1}) G(x)$ via $g_k - g_{k - a_i - 1}$.
- **Solution Formula**: $[x^K] \prod_{i=1}^N \frac{1 - x^{a_i+1}}{1 - x}$ in $O(NK)$ time.

#### Problem 1B-3: AtCoder ABC 321 F — #(subset sum = K) with Add and Erase
- **URL**: `https://atcoder.jp/contests/abc321/tasks/abc321_f` | **Constraints**: $Q, K \le 5000$, $\bmod 998244353$.
- **Statement**: Maintain a multiset of integers under `+ x` (insert) and `- x` (erase), outputting the number of subsets summing to $K$ after each query.
- **Tags**: `[Reversible-DP]`, `[Sparse-Division]` | **Diagnostic Signal**: Insert = multiply by $(1 + x^v)$; Erase = divide by $(1 + x^v) \bmod x^{K+1}$.
- **3-Tier Hints**: (1) The subset-sum OGF is $F(x) = \prod (1 + x^v) \bmod x^{K+1}$. (2) Multiplication $F_{\text{new}}(x) = (1 + x^v) F_{\text{old}}(x)$ updates $f_i \gets f_i + f_{i-v}$ from $i = K$ down to $v$. (3) Division $F_{\text{old}}(x) = \frac{F_{\text{new}}(x)}{1 + x^v}$ inverts this exact loop: update $f_i \gets f_i - f_{i-v}$ from $i = v$ **up** to $K$!
- **Solution Formula**: Forward loop `for (int i = v; i <= K; ++i) dp[i] -= dp[i - v];` in $O(QK)$ time.

#### Problem 1B-4: AtCoder ABC 178 D — Redistribution
- **URL**: `https://atcoder.jp/contests/abc178/tasks/abc178_d` | **Constraints**: $S \le 2000$, $\bmod 10^9+7$.
- **Statement**: Count ordered sequences of integers $\ge 3$ whose sum is $S$.
- **Tags**: `[OGF-Seq]`, `[Stars-and-Bars]` | **Diagnostic Signal**: $\text{SEQ}(\mathcal{Z}_{\ge 3}) \implies \frac{1}{1 - \frac{x^3}{1-x}} = \frac{1 - x}{1 - x - x^3}$.
- **3-Tier Hints**: (1) Each summand has OGF $A(x) = x^3 + x^4 + \dots = \frac{x^3}{1 - x}$. (2) Summing over $k$ terms gives $\sum_{k=1}^{\lfloor S/3 \rfloor} [x^S] \frac{x^{3k}}{(1-x)^k} = \sum_{k} \binom{S - 2k - 1}{k - 1}$. (3) Or read off the 3-term linear recurrence $f_n = f_{n-1} + f_{n-3}$ from the denominator $1 - x - x^3$.
- **Solution Formula**: $[x^S] \frac{x^3}{1 - x - x^3} = \sum_{k=1}^{\lfloor S/3 \rfloor} \binom{S - 2k - 1}{k - 1}$.

#### Problem 1B-5: Luogu P3338 — [ZJOI2014] 力 (Force)
- **URL**: `https://www.luogu.com.cn/problem/P3338` | **Constraints**: $N \le 10^5$, real floating-point FFT.
- **Statement**: Given charges $q_1, \dots, q_N$, compute $E_j = \sum_{i < j} \frac{q_i}{(j - i)^2} - \sum_{i > j} \frac{q_i}{(i - j)^2}$ for all $j = 1, \dots, N$.
- **Tags**: `[Difference-Convolution]`, `[Index-Reversal]` | **Diagnostic Signal**: Sums over $j - i$ (standard convolution) and $i - j$ (cross-correlation / reverse-index convolution).
- **3-Tier Hints**: (1) Define $g_k = 1/k^2$ for $k \ge 1$ and $g_0 = 0$. The first sum is $\sum_{i < j} q_i g_{j-i} = [x^j] Q(x) G(x)$. (2) For the second sum $\sum_{i > j} q_i g_{i-j}$, reverse the array $q$: let $q^R_k = q_{N-k}$. (3) Then $\sum_{i > j} q_i g_{i-j} = \sum_{i > j} q^R_{N-i} g_{i-j} = [x^{N-j}] Q^R(x) G(x)$.
- **Solution Formula**: $E_j = [x^j](Q * G) - [x^{N-j}](Q^R * G)$ in $O(N \log N)$ via FFT.

---

### Tier 2: Intermediate (`Intermediate` — Problems 6–14)

#### Problem 1B-6: AtCoder ARC 028 D — 注文の多い高橋商店
- **URL**: `https://atcoder.jp/contests/arc028/tasks/arc028_4` | **Constraints**: $N, M \le 2000, Q \le 5 \times 10^5$, $\bmod 10^9+7$.
- **Statement**: Given $N$ item types with bounds $a_1, \dots, a_N$, answer $Q$ queries: "if item $k$ must be chosen exactly $x$ times, how many ways to choose $M$ items in total?"
- **Tags**: `[Reversible-Knapsack]`, `[Polynomial-Division]` | **Diagnostic Signal**: Precompute the full product $P(x) = \prod_{i=1}^N \frac{1-x^{a_i+1}}{1-x}$, then for each item $k$ precompute $P^{(-k)}(x) = P(x) \cdot \frac{1-x}{1-x^{a_k+1}}$ in $O(M)$ time!
- **3-Tier Hints**: (1) Precompute $P(x) \bmod x^{M+1}$ in $O(NM)$ time. (2) Removing factor $k$ multiplies $P(x)$ by $\frac{1 - x}{1 - x^{a_k+1}}$, which is a forward difference followed by an unbounded knapsack step of stride $a_k + 1$! (3) Store all $N$ reduced polynomials $P^{(-k)}(x)$ in $O(NM)$ total time and answer each query as $[x^{M-x}] P^{(-k)}(x)$ in $O(1)$ time.
- **Solution Formula**: $\text{Ans}(k, x) = [x^{M-x}] \left(P(x) \cdot \frac{1-x}{1-x^{a_k+1}}\right)$ in $O(NM + Q)$ time.

#### Problem 1B-7: Luogu P2290 / P4430 — [HNOI2004] 树的计数
- **URL**: `https://www.luogu.com.cn/problem/P2290` | **Constraints**: $N \le 150$ (exact integer) or $N \le 10^6$ (modular).
- **Statement**: Count labeled trees on $N$ vertices where vertex $i$ has degree $d_i$ (or where degrees belong to a constraint set).
- **Tags**: `[Prufer-EGF]`, `[Multinomial-Extraction]` | **Diagnostic Signal**: Vertex $i$ with degree $d_i$ appears $d_i - 1$ times in the Prüfer sequence of length $N - 2$.
- **3-Tier Hints**: (1) By Prüfer's bijection, the EGF over vertex degrees is $\prod_{i=1}^N \frac{x^{d_i - 1}}{(d_i - 1)!}$. (2) Extracting $(N-2)! [x^{N-2}]$ yields $\frac{(N-2)!}{\prod_{i=1}^N (d_i - 1)!}$ when $\sum (d_i - 1) = N - 2$ and $d_i \ge 1$. (3) If degrees are constrained rather than fixed, multiply the degree-constraint EGFs via NTT!
- **Solution Formula**: $(N-2)! [x^{N-2}] \prod_{i=1}^N \left(\sum_{d \in S_i} \frac{x^{d-1}}{(d-1)!}\right)$.

#### Problem 1B-8: CEOI 2004 Sweet (Luogu P6078) & POJ 3734 Blocks
- **URL**: `https://www.luogu.com.cn/problem/P6078` | **Constraints**: $N \le 10, A, B \le 10^7, \bmod 2004$.
- **Statement**: (Sweet) Count ways to eat between $A$ and $B$ sweets from $N$ jars of sizes $m_1, \dots, m_N$. (Blocks) Color $N$ blocks with 4 colors where Red and Green appear an even number of times.
- **Tags**: `[Sparse-Numerator-Expansion]`, `[EGF-Parity]` | **Diagnostic Signal**: $N \le 10$ is tiny while $B \le 10^7$ is large $\implies$ expand the $2^N$-term numerator $\prod_{i=1}^N (1 - x^{m_i+1})$ explicitly and multiply by $(1-x)^{-(N+1)}$!
- **3-Tier Hints**: (1) For Sweet, $\sum_{k=0}^B [x^k] \prod_{i=1}^N \frac{1-x^{m_i+1}}{1-x} = [x^B] \frac{\prod_{i=1}^N (1 - x^{m_i+1})}{(1-x)^{N+1}}$. (2) Expand $\prod_{i=1}^N (1 - x^{m_i+1}) = \sum_{S \subseteq [N]} (-1)^{|S|} x^{\sum_{i \in S}(m_i+1)}$ in $2^N = 1024$ terms. (3) For Blocks, the EGF is $e^{2x} \left(\frac{e^x + e^{-x}}{2}\right)^2 = \frac{1}{4}(e^{4x} + 2 e^{2x} + 1)$.
- **Solution Formula**: (Sweet) $\sum_{S \subseteq [N]} (-1)^{|S|} \binom{B - \sum_{i \in S}(m_i+1) + N}{N}$; (Blocks) $4^{N-1} + 2^{N-1}$.

#### Problem 1B-9: AtCoder AGC 001 E — BBQ Hard
- **URL**: `https://atcoder.jp/contests/agc001/tasks/agc001_e` | **Constraints**: $N \le 2 \times 10^5, A_i, B_i \le 2000$, $\bmod 10^9+7$.
- **Statement**: Compute $\sum_{1 \le i < j \le N} \binom{A_i + A_j + B_i + B_j}{A_i + A_j} \bmod (10^9+7)$.
- **Tags**: `[Offset-Vandermonde]`, `[2D-Grid-GF]` | **Diagnostic Signal**: $\binom{(A_i+A_j)+(B_i+B_j)}{A_i+A_j} = [x^{A_j} y^{B_j}] \frac{x^{-A_i} y^{-B_i}}{1 - (x + y)}$, i.e., lattice paths from $(-A_i, -B_i)$ to $(A_j, B_j)$.
- **3-Tier Hints**: (1) $N = 2 \times 10^5$ is large, but $A_i, B_i \le 2000$ is small! (2) Place a source of weight $+1$ at $(-A_i, -B_i)$ for every $i = 1, \dots, N$ on a $[-2000, 2000]^2$ grid. (3) Propagate the 2D OGF multiplier $\frac{1}{1 - x - y}$ across the grid in $O(\max(A)^2)$ time, subtract the diagonal $i = j$, and divide by $2$.
- **Solution Formula**: $\frac{1}{2} \left(\sum_{j=1}^N \text{dp}[A_j][B_j] - \sum_{i=1}^N \binom{2A_i + 2B_i}{2A_i}\right)$ in $O(N + (\max A_i)(\max B_i))$ time.

#### Problem 1B-10: Codeforces 932E — Team Work
- **URL**: `https://codeforces.com/problemset/problem/932/E` | **Constraints**: $N \le 10^9, K \le 5000$ (or $10^7$), $\bmod 10^9+7$.
- **Statement**: Compute $\sum_{i=1}^N \binom{N}{i} i^K \bmod (10^9+7)$.
- **Tags**: `[Stirling-S2]`, `[Theta-Operator]`, `[Binomial-Power-Sum]` | **Diagnostic Signal**: $\sum_{i=0}^N \binom{N}{i} i^K = (\vartheta_x^K (1+x)^N)\big|_{x=1}$ where $i^K = \sum_{j=0}^K \left\{\begin{matrix} K \\ j \end{matrix}\right\} i^{\underline{j}}$.
- **3-Tier Hints**: (1) Substitute $i^K = \sum_{j=0}^K \left\{\begin{matrix} K \\ j \end{matrix}\right\} j! \binom{i}{j}$. (2) Use $\binom{N}{i}\binom{i}{j} = \binom{N}{j}\binom{N-j}{i-j}$ and sum over $i$: $\sum_{i=j}^N \binom{N-j}{i-j} = 2^{N-j}$. (3) Thus the sum collapses to $\sum_{j=0}^{\min(N, K)} \left\{\begin{matrix} K \\ j \end{matrix}\right\} N^{\underline{j}} 2^{N-j}$!
- **Solution Formula**: $\sum_{j=0}^{\min(N, K)} \left\{\begin{matrix} K \\ j \end{matrix}\right\} N^{\underline{j}} 2^{N-j} \bmod (10^9+7)$.

#### Problem 1B-11: AtCoder ARC 012 D — Don't Step on the Mines!
- **URL**: `https://atcoder.jp/contests/arc012/tasks/arc012_4` | **Constraints**: $N, T \le 10^5$, arbitrary modulus $M \le 10^9$.
- **Statement**: Count 2D lattice walks of length $T$ from $(x_i, y_i)$ to $(0, 0)$ for $N$ walkers modulo an arbitrary (possibly composite) $M$.
- **Tags**: `[2D-Walk-Decoupling]`, `[Prime-Power-Factoring]` | **Diagnostic Signal**: Rotate coordinates $(u, v) = (x+y, x-y)$ so $(x+x^{-1}+y+y^{-1})^T = (u+u^{-1})^T (v+v^{-1})^T$.
- **3-Tier Hints**: (1) Under $u = x+y, v = x-y$, each step changes $u$ by $\pm 1$ and $v$ by $\pm 1$ independently! (2) Thus the number of walks for walker $i$ is $\binom{T}{(T + x_i + y_i)/2} \binom{T}{(T + x_i - y_i)/2}$. (3) Multiply all $2N$ binomial coefficients modulo $M$ by accumulating the prime-exponent array of $1, \dots, T$ via a linear sieve in $O(T)$ time.
- **Solution Formula**: $\prod_{i=1}^N \binom{T}{\frac{T + x_i + y_i}{2}} \binom{T}{\frac{T + x_i - y_i}{2}} \bmod M$.

#### Problem 1B-12: AtCoder ABC 267 Ex — Odd Sum
- **URL**: `https://atcoder.jp/contests/abc267/tasks/abc267_h` | **Constraints**: $N \le 10^5, M \le 10^6, A_i \le 10$, $\bmod 998244353$.
- **Statement**: Given $N$ integers $A_1, \dots, A_N \in [1, 10]$, count subsets of **odd cardinality** whose sum is $M$.
- **Tags**: `[Parity-Filter]`, `[Bivariate-OGF]` | **Diagnostic Signal**: Mark cardinality by $y$ and sum by $x$ in $\prod_{i=1}^N (1 + y x^{A_i})$, then filter odd powers of $y$ via $\frac{P(x, 1) - P(x, -1)}{2}$.
- **3-Tier Hints**: (1) Let $P(x, y) = \prod_{i=1}^N (1 + y x^{A_i}) = \prod_{v=1}^{10} (1 + y x^v)^{c_v}$. (2) Odd-size subsets are generated by $\frac{P(x, 1) - P(x, -1)}{2}$. (3) Since $A_i \le 10$, each $(1 \pm x^v)^{c_v}$ can be expanded directly or multiplied in $O(M \log M)$ time.
- **Solution Formula**: $\frac{1}{2} [x^M] \left(\prod_{v=1}^{10} (1 + x^v)^{c_v} - \prod_{v=1}^{10} (1 - x^v)^{c_v}\right) \bmod 998244353$.

#### Problem 1B-13: Luogu P4841 — 城市规划 (CDQ Semi-Online Perspective)
- **Cross-Reference**: Identical to **Problem 1A-9a**; in Wave 1B, solved via the semi-online recurrence $c_n = g_n - \sum_{k=1}^{n-1} \binom{n-1}{k-1} c_k g_{n-k}$ using CDQ Divide-and-Conquer NTT.

#### Problem 1B-14: Luogu P3702 — [SDOI2017] 序列计数
- **URL**: `https://www.luogu.com.cn/problem/P3702` | **Constraints**: $N \le 10^9, M \le 2 \times 10^7, p \le 100$, $\bmod 20170408$.
- **Statement**: Count length-$N$ sequences from $\{1, \dots, M\}$ containing at least one prime and having total sum divisible by $p$.
- **Tags**: `[Cyclic-Convolution]`, `[Complementary-Counting]` | **Diagnostic Signal**: Sum $\bmod p \equiv 0$ is $[x^0] P(x)^N \bmod (x^p - 1)$; "at least one prime" = (All sequences) $-$ (Composite-only sequences).
- **3-Tier Hints**: (1) Sieve primes up to $M \le 2 \times 10^7$ in $O(M)$ time. (2) Construct degree-$(p-1)$ polynomials $A_{\text{all}}(x)$ and $A_{\text{comp}}(x)$ grouping numbers in $[1, M]$ by residue $\bmod p$. (3) Compute $[x^0] A_{\text{all}}(x)^N \bmod (x^p - 1) - [x^0] A_{\text{comp}}(x)^N \bmod (x^p - 1)$ via binary exponentiation in $O(p^2 \log N)$ time.
- **Solution Formula**: $[x^0]\big(A_{\text{all}}(x)^N - A_{\text{comp}}(x)^N\big) \bmod (x^p - 1)$.

---

### Tier 3: Advanced (`Advanced` — Problems 15–22)

#### Problem 1B-15: AtCoder JSC 2019 Qual F — Candy Retribution
- **URL**: `https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_f` | **Constraints**: $1 \le M < N \le 3 \times 10^5$, $1 \le L \le R \le 3 \times 10^5$, $\bmod 10^9+7$.
- **Statement**: Distribute $S$ indistinguishable candies among $N$ distinguishable children for each $S \in [L, R]$ so that Snuke cannot choose $M$ children whose candy counts $(B_1 \ge B_2 \ge \dots \ge B_N \ge 0$ after sorting) violate the condition — specifically, by complementary counting, a distribution is **bad** iff the $M$-th largest value and $(M+1)$-th largest value are equal? No: a distribution is **good** unless the $M$ chosen children can be tied, which reduces by complementary counting to subtracting distributions where $B_M > B_{M+1}$ fails or where a fixed subset of $M$ children all have $\ge t+1$ candies while the remaining $N - M$ children all have $\le t$ candies!
- **Tags**: `[Bounded-Partition-IE]`, `[Harmonic-Enumeration]` | **Diagnostic Signal**: Complementary counting over the unique subset of $M$ children having $\ge a$ candies while the remaining $N - M$ children have $\le b$ candies yields $H(S, a, b) = [x^{S - M a}] \frac{(1 - x^{b+1})^{N - M}}{(1 - x)^{N + 1}}$; summing over $t < \lfloor S/M \rfloor$ and $j \le \frac{S - M a}{b + 1}$ takes $O(R \log R)$ harmonic time!
- **3-Tier Hints**: (1) Replace the range $[L, R]$ by prefix difference $\text{Good}_{\le}(R) - \text{Good}_{\le}(L - 1)$, where multiplying by $\frac{1}{1-x}$ sums over all total candy counts $\le S$. (2) Define the helper $H(S, a, b) = [x^S] \frac{x^{M a} (1 - x^{b+1})^{N - M}}{(1 - x)^{N + 1}} = \sum_{j=0}^{\min(N - M, \lfloor \frac{S - M a}{b + 1} \rfloor)} (-1)^j \binom{N - M}{j} \binom{S - M a - j(b + 1) + N}{N}$, which counts distributions with sum $\le S$ where $M$ fixed children get $\ge a$ and $N - M$ children get $\le b$. (3) For each threshold $t = 0, \dots, \lfloor S/M \rfloor - 1$, subtract $H(S, t + 1, t) - H(S, t + 2, t)$ weighted by $\binom{N}{M}$; since $j(t + 1) \le S - M(t + 1)$, the total work across all $(t, j)$ is bounded by $\sum_{t \ge 0} \frac{S}{t + 1} = O(S \log S)$.
- **Solution Formula**: $\text{Ans} = \text{Good}_{\le}(R) - \text{Good}_{\le}(L - 1)$, where $\text{Good}_{\le}(S) = \binom{S + N}{N} - \binom{N}{M} \sum_{t=0}^{\lfloor S / M \rfloor - 1} \big(H(S, t + 1, t) - H(S, t + 2, t)\big)$ and $H(S, a, b) = [x^{S - M a}] \frac{(1 - x^{b+1})^{N - M}}{(1 - x)^{N + 1}} = \sum_{j=0}^{\min(N - M, \lfloor \frac{S - M a}{b + 1} \rfloor)} (-1)^j \binom{N - M}{j} \binom{S - M a - j(b + 1) + N}{N} \bmod (10^9+7)$.

#### Problem 1B-16: AtCoder ARC 110 D — Binomial Coefficient is Fun
- **URL**: `https://atcoder.jp/contests/arc110/tasks/arc110_d` | **Constraints**: $N \le 2000, M \le 10^9, A_i \le 2000$, $\bmod 10^9+7$.
- **Statement**: Compute $\sum_{B_1 + \dots + B_N \le M} \prod_{i=1}^N \binom{B_i}{A_i} \bmod (10^9+7)$.
- **Tags**: `[Negative-Binomial]`, `[Vandermonde-Identity]` | **Diagnostic Signal**: $[x^{B_i}] \frac{x^{A_i}}{(1-x)^{A_i+1}} = \binom{B_i}{A_i}$, and summing over $\le M$ multiplies by $\frac{1}{1-x}$.
- **3-Tier Hints**: (1) Replace $\binom{B_i}{A_i}$ by its OGF $[x^{B_i}] \frac{x^{A_i}}{(1-x)^{A_i+1}}$. (2) Multiply across $i = 1, \dots, N$ and multiply by $\frac{1}{1-x}$ for the prefix sum $\sum B_i \le M$. (3) Extract $[x^M] \frac{x^{\sum A_i}}{(1-x)^{\sum A_i + N + 1}} = \binom{M + N}{\sum_{i=1}^N A_i + N}$.
- **Solution Formula**: $\binom{M + N}{\sum_{i=1}^N A_i + N} \bmod (10^9+7)$ in $O(N + \sum A_i)$ time.

#### Problem 1B-17: Codeforces 993E — Nikita and Order Statistics
- **URL**: `https://codeforces.com/problemset/problem/993/E` | **Constraints**: $N \le 2 \times 10^5$, exact 64-bit integer FFT.
- **Statement**: Given an array $a_1, \dots, a_N$ and $X$, for each $k = 0, \dots, N$, count contiguous subarrays containing exactly $k$ elements $< X$.
- **Tags**: `[Difference-Convolution]`, `[Prefix-Count]` | **Diagnostic Signal**: Let $S_r$ be the prefix count of elements $< X$. We want $\sum_{r - l \text{ has } S_r - S_l = k} 1 = \sum_{s - t = k} c_s c_t$.
- **3-Tier Hints**: (1) Replace each $a_i$ by $[a_i < X] \in \{0, 1\}$ and compute prefix sums $S_0, S_1, \dots, S_N$. (2) Let $c_s$ be the frequency of prefix sum $s$. For $k = 0$, the answer is $\sum_s \binom{c_s}{2}$. (3) For $k \ge 1$, the answer is $\sum_{s=k}^N c_s c_{s-k} = [x^{N+k}] \left(\sum c_s x^s\right)\left(\sum c_t x^{N-t}\right)$.
- **Solution Formula**: $\text{Ans}_k = [x^{N+k}] C(x) C^R(x)$ for $k \ge 1$, $\text{Ans}_0 = \sum_s \binom{c_s}{2}$.

#### Problem 1B-18: AtCoder AGC 005 F — Many Easy Problems
- **Cross-Reference**: Identical to **Problem 1A-12**; in Wave 1B, also solved via Bluestein's Chirp-$Z$ Transform for non-NTT prime $924844033 = 441 \times 2^{21} + 1$.

#### Problem 1B-19: AtCoder ABC 276 G — Count Sequences
- **URL**: `https://atcoder.jp/contests/abc276/tasks/abc276_g` | **Constraints**: $N, M \le 10^7$, $\bmod 998244353$.
- **Statement**: Count integer sequences $0 \le a_1 \le \dots \le a_N \le M$ where $a_i \not\equiv a_{i+1} \pmod 3$.
- **Tags**: `[Step-Residue-OGF]`, `[Sparse-Binomial-Extraction]` | **Diagnostic Signal**: Adjacent steps $d_i = a_{i+1} - a_i$ satisfy $d_i \equiv 1, 2 \pmod 3$, so the step OGF is $\frac{x + x^2}{1 - x^3}$.
- **3-Tier Hints**: (1) Rewrite $a_1 \ge 0$ and $M - a_N \ge 0$ as two unrestricted steps $\frac{1}{1-x}$, and the $N-1$ internal steps as $\left(\frac{x + x^2}{1 - x^3}\right)^{N-1}$. (2) Total OGF is $\frac{x^{N-1} (1 + x)^{N-1}}{(1-x)^2 (1 - x^3)^{N-1}}$. (3) Expand $(1+x)^{N-1}$ and $(1-x^3)^{-(N-1)}$; for each $k$ from $(1-x^3)^{-(N-1)}$, the remaining power $r = M - (N-1) - 3k$ is extracted from $\frac{(1+x)^{N-1}}{(1-x)^2}$ via prefix sums in $O(N + M)$ time!
- **Solution Formula**: $[x^{M-N+1}] \frac{(1+x)^{N-1}}{(1-x)^2 (1-x^3)^{N-1}}$ in $O(N + M)$ time.

#### Problem 1B-20: Codeforces 438E — The Child and Binary Tree
- **Cross-Reference**: Identical to **Problem 1A-10**; in Wave 1B, derived directly from the quadratic DP $f_s = \sum_{c \in S} \sum_{i+j=s-c} f_i f_j$.

#### Problem 1B-21: Codeforces 891E — Lust
- **Cross-Reference**: Identical to **Problem 1A-16**.

#### Problem 1B-22: AtCoder AISing 2020 F — Two Snuke
- **URL**: `https://atcoder.jp/contests/aising2020/tasks/aising2020_f` | **Constraints**: $N \le 10^9, T \le 200$, $\bmod 10^9+7$.
- **Statement**: Given $N \le 10^9$, sum the product $(s_2 - s_1)(n_2 - n_1)(u_2 - u_1)(k_2 - k_1)(e_2 - e_1)$ over all $10$-tuples of non-negative integers $(s_1, s_2, n_1, n_2, u_1, u_2, k_1, k_2, e_1, e_2)$ satisfying $s_1 < s_2$, $n_1 < n_2$, $u_1 < u_2$, $k_1 < k_2$, $e_1 < e_2$ and $s_1 + s_2 + n_1 + n_2 + u_1 + u_2 + k_1 + k_2 + e_1 + e_2 \le N$.
- **Tags**: `[Parity-Split-OGF]`, `[Bostan-Mori]` | **Diagnostic Signal**: Each pair $(x_{i,1}, x_{i,2})$ with $x_{i,1} < x_{i,2}$ has OGF $\sum_{x_{i,2} > x_{i,1} \ge 0} (x_{i,2} - x_{i,1}) z^{x_{i,1} + x_{i,2}} = \frac{z}{(1 - z)^2 (1 - z^2)}$; multiplying by $(1+z)^{11}/(1+z)^{11}$ makes the denominator a pure function of $z^2$!
- **3-Tier Hints**: (1) For a single pair, write $x_{i,2} = x_{i,1} + d_i$ with $x_{i,1} \ge 0$ and $d_i \ge 1$; its sum is $2 x_{i,1} + d_i$, so the single-pair OGF is $\left(\sum_{x \ge 0} z^{2x}\right)\left(\sum_{d \ge 1} d z^d\right) = \frac{1}{1 - z^2} \cdot \frac{z}{(1 - z)^2}$. (2) Raising to the $5$-th power across the $5$ independent pairs and multiplying by $\frac{1}{1 - z}$ for total sum $\le N$ gives $F(z) = \frac{z^5}{(1 - z^2)^5 (1 - z)^{11}} = \frac{z^5 (1 + z)^{11}}{(1 - z^2)^{16}}$. (3) Expand the degree-$11$ numerator $z^5 (1 + z)^{11} = \sum_{j=0}^{11} \binom{11}{j} z^{j+5}$ and extract $[z^N]$ directly from $(1 - z^2)^{-16} = \sum_{m \ge 0} \binom{m + 15}{15} z^{2m}$ in $O(1)$ operations per query!
- **Solution Formula**: $\text{Ans}(N) = [z^N] \frac{z^5 (1 + z)^{11}}{(1 - z^2)^{16}} = \sum_{\substack{0 \le j \le 11 \\ j \equiv N - 5 \pmod 2}} \binom{11}{j} \binom{\frac{N - 5 - j}{2} + 15}{15} \bmod (10^9+7)$.

---

### Tier 4: Mastery (`Mastery` — Problems 23–27)

#### Problem 1B-23: Codeforces 623E — Transforming Sequence
- **URL**: `https://codeforces.com/problemset/problem/623/E` | **Constraints**: $N \le 10^{18}, K \le 3 \times 10^4$, $\bmod 10^9+7$.
- **Statement**: Count sequences $a_1, \dots, a_N$ with $1 \le a_i < 2^K$ such that $a_1 \mid a_2 \mid \dots \mid a_{i-1} < (a_1 \mid \dots \mid a_i)$ at every step (strictly increasing bitwise OR prefix).
- **Tags**: `[Scale-Shift-Doubling]`, `[MTT-Arbitrary-Mod]` | **Diagnostic Signal**: Step $i$ must activate $c_i \ge 1$ new bits while picking any subset of the already active $\sum_{j < i} c_j$ bits ($2^{\sum_{j < i} c_j}$ choices).
- **3-Tier Hints**: (1) If the $N$ steps activate $c_1, \dots, c_N \ge 1$ bits, the number of choices is $\binom{K}{c_1, \dots, c_N, K-\sum c} \prod_{i=1}^N 2^{\sum_{j < i} c_j}$. (2) Let $F_m(x)$ be the EGF for $m$ steps; then $F_{m_1 + m_2}(x) = F_{m_1}(x) \cdot F_{m_2}(2^{m_1} x)$! (3) Compute $F_N(x) \bmod x^{K+1}$ in $O(\log N)$ doubling steps using MTT modulo $10^9+7$ in $O(K \log K \log N)$ time.
- **Solution Formula**: $\sum_{s=N}^K \binom{K}{s} s! [x^s] F_N(x)$ where $F_1(x) = e^x - 1$ and $F_{2m}(x) = F_m(x) F_m(2^m x)$.

#### Problem 1B-24: AtCoder ABC 213 G — Connectivity 2
- **URL**: `https://atcoder.jp/contests/abc213/tasks/abc213_g` | **Constraints**: $N \le 17$, $\bmod 998244353$.
- **Statement**: Given a graph $G = (V, E)$ on $N \le 17$ vertices, for each $k = 2, \dots, N$, count spanning subgraphs in which vertices $1$ and $k$ are connected.
- **Tags**: `[Subset-DP-Ln]`, `[Connected-Subgraph]` | **Diagnostic Signal**: Total subgraphs on $S \subseteq V$ is $g(S) = 2^{|E(S)|}$; connected subgraphs $c(S)$ satisfy $c(S) = g(S) - \sum_{v_0 \in T \subsetneq S} c(T) g(S \setminus T)$.
- **3-Tier Hints**: (1) Fix $v_0 = 1$ as the anchor vertex to break symmetry (equivalent to $x_1 \frac{\partial}{\partial x_1} \ln G$). (2) Compute $c(S)$ for all $1 \in S \subseteq V$ in $O(3^N)$ via submask iteration (or $O(N^2 2^N)$ via Set Power Series $\ln$). (3) Then the answer for vertex $k$ is $\sum_{S \ni 1, k} c(S) g(V \setminus S)$.
- **Solution Formula**: $\text{Ans}_k = \sum_{\{1, k\} \subseteq S \subseteq V} c(S) 2^{|E(V \setminus S)|}$.

#### Problem 1B-25: Luogu P4389 — 付公主的背包 & Luogu P3784 — [SDOI2017] 遗忘的集合 (Forward & Inverse Euler Transform)
- **URL**: `https://www.luogu.com.cn/problem/P4389` / `https://www.luogu.com.cn/problem/P3784` | **Constraints**: $N, M \le 10^5$ ($\bmod 998244353$) or $N < 2^{18}$ (arbitrary prime $p$).
- **Statement**: Covers both directions of the Euler Transform on knapsack products $F(x) = \prod_{i=1}^N (1 - x^i)^{-a_i} \bmod x^{M+1}$: (i) **Luogu P4389 (Forward Euler Transform)**: given item volumes $v_1, \dots, v_N$, compute $F(x) \bmod x^{M+1}$ via harmonic $\ln$ and $\exp$ (see **Problem 1A-7a**); and (ii) **Luogu P3784 (Inverse Euler Transform)**: given $f_1, \dots, f_N \bmod p$ with $a_i \in \{0, 1\}$ under an arbitrary prime modulus $p$, recover which items $a_i = 1$ belong to the set.
- **Tags**: `[Euler-Transform]`, `[Inverse-Euler-Transform]`, `[MTT-Ln]` | **Diagnostic Signal**: Forward product-to-sum via $\ln F(x) = \sum_{i=1}^M a_i \sum_{k \ge 1} \frac{x^{ik}}{k}$; inverse recovery via $n [x^n] \ln F(x) = \sum_{d \mid n} d a_d \bmod p$ using MTT-backed $\ln$.
- **3-Tier Hints**: (1) For P4389, accumulate $\ln F(x)$ in $O(M \log M)$ harmonic steps and apply `exp`. (2) For P3784, compute $\ln F(x) \bmod (x^{N+1}, p)$ using MTT-backed Newton inversion. (3) Multiply $[x^n] \ln F(x)$ by $n \bmod p$ to obtain $\sum_{d \mid n} d a_d \bmod p$, then apply Möbius inversion over divisors to recover $a_n \in \{0, 1\}$.
- **Solution Formula**: Forward: $F(x) = \exp\left(\sum_{i=1}^M a_i \sum_{k \ge 1} \frac{x^{ik}}{k}\right)$; Inverse: $a_n = n^{-1} \sum_{d \mid n} \mu(n/d) \cdot d [x^d] \ln F(x) \bmod p$.

#### Problem 1B-26: Luogu P4548 — 歌唱王国
- **Cross-Reference**: Identical to **Problem 1A-15**.

#### Problem 1B-27: AtCoder ABC 213 Ex — Stroll
- **URL**: `https://atcoder.jp/contests/abc213/tasks/abc213_h` | **Constraints**: $N \le 10, M \le 10, T \le 4 \times 10^4$, $\bmod 998244353$.
- **Statement**: On a multigraph with $N \le 10$ vertices where traversing edge $e$ at step $t$ has weight $p_{e, t}$, count weighted walks of length $T$ from vertex $1$ to vertex $1$.
- **Tags**: `[CDQ-Divide-and-Conquer-NTT]`, `[Time-Indexed-Graph-DP]` | **Diagnostic Signal**: $f_u(t) = \sum_{(v, u) \in E} \sum_{k=1}^t f_v(t - k) p_{e, k}$, which is a system of $N$ coupled semi-online convolutions!
- **3-Tier Hints**: (1) For each vertex $u$, define the OGF $F_u(x) = \sum_{t=0}^T f_u(t) x^t$, and for each edge $e = (u, v)$, $P_e(x) = \sum_{k=1}^T p_{e, k} x^k$. (2) Then $F_u(x) = [u = 1] + \sum_{e=(v, u)} F_v(x) P_e(x) \bmod x^{T+1}$. (3) Run CDQ Divide-and-Conquer on $[0, T]$: at midpoint $m$, forward-NTT the $N$ polynomials $F_v[l..m]$ once, multiply in point-value domain along the $M$ edges, and inverse-NTT the $N$ target accumulators!
- **Solution Formula**: Solved in $O((N + M) T \log^2 T)$ time via CDQ NTT with point-value caching.

---

## 4. Wave 2A Problem Encyclopedia: Substitutions, Radicals, Stirling & Euler Transforms (`cohort3_wave_2a_substitutions_transforms.md`)

> **Full Reference**: See `fps_research/cohort3_wave_2a_substitutions_transforms.md`, Section 10.2 (Lines 756–1458).

### Module A: Rational & Linear Substitutions (Problems 2A-1 to 2A-8)

#### Problem 2A-1: AtCoder `fps_24_h` — Jump (`Stepping Stone`)
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_h` | **Constraints**: $N, M \le 2.5 \times 10^5$, $\bmod 998244353$.
- **Statement**:
  - **Formulation A (Rational Möbius Substitution)**: Count sequences of jumps with linear shift/step weights reducible to $F\left(\frac{ax+b}{cx+d}\right)$ or $[x^N] (1+x)^A (1-x)^{-B}$.
  - **Formulation B (Jump Partition Product — `fps_24_h`)**: Count ways to jump across an $N, M$ grid or sequence where step sizes and gaps produce the coefficient extraction $[x^N y^M] \frac{1}{(1-x-y)}$ / $\binom{N+M-1}{N}\binom{N+M-1}{M} \bmod 998244353$.
- **Tags**: `[Linear-Substitution]`, `[Taylor-Shift]`, `[Vandermonde-Convolution]` | **Diagnostic Signal**: Composition of a polynomial $F(y)$ with a Möbius transformation $y = \frac{ax+b}{cx+d}$, or decoupling positive and negative step sizes into $\binom{N+M-1}{N}\binom{N+M-1}{M}$.
- **3-Tier Hints**: (1) Factor $(cx+d)^D F\left(\frac{ax+b}{cx+d}\right)$ into a sequence of three elementary operators: reversal, scaling $x \mapsto \lambda x$, and Taylor shift $x \mapsto x + c$. (2) Execute each Taylor shift via a single EGF convolution $P(x+c) = \sum \frac{x^k}{k!} \sum_{j \ge k} p_j j! \frac{c^{j-k}}{(j-k)!}$. (3) Invert the denominator power at the end (or evaluate $\binom{N+M-1}{N}\binom{N+M-1}{M}$ directly in $O(N+M)$ time).
- **Solution Formula**: Executed in $O(N \log N)$ via 2 Taylor shifts and 1 scaling; for Formulation B, $\binom{N+M-1}{N}\binom{N+M-1}{M} \bmod 998244353$.

#### Problem 2A-2: Codeforces 923E — Perpetual Subtraction (`Intermediate`)
- **URL**: `https://codeforces.com/problemset/problem/923/E` | **Constraints**: $N \le 10^5, M \le 10^{18}$, $\bmod 998244353$.
- **Statement**: Given an initial probability distribution $p_0, \dots, p_N$, at each of $M$ steps replace $x$ uniformly at random with $y \in \{0, 1, \dots, x\}$. Find the final distribution.
- **Tags**: `[Taylor-Shift-Diagonalization]`, `[Eigenbasis-Change]` | **Diagnostic Signal**: One step maps $P(x) = \sum_{k=0}^N p_k x^k \mapsto \sum_{k=0}^N \frac{p_k}{k+1} \frac{1 - x^{k+1}}{1 - x}$; under $x = u + 1$, the operator becomes diagonal!
- **3-Tier Hints**: (1) Substitute $x = u - 1$ (or $x = u + 1$): notice that $\int_0^x (t - 1)^k dt = \frac{(x - 1)^{k+1} - (-1)^{k+1}}{k + 1}$. (2) Thus in the shifted basis $Q(u) = P(u - 1) = \sum_{k=0}^N q_k u^k$, one transition step simply divides the $k$-th coefficient by $k + 1$ (up to alternating sign)! (3) Apply Taylor shift $u = x + 1$, divide $[u^k]$ by $(k + 1)^M$, and apply the inverse Taylor shift $x = u - 1$!
- **Solution Formula**: $P^{(M)}(x) = \mathcal{T}_{-1} \circ \text{Diag}\big((k+1)^{-M}\big) \circ \mathcal{T}_{+1} (P)(x)$ in $O(N \log N)$ time.

#### Problem 2A-3: AtCoder KUPC 2019 K — One or All (`Intermediate`)
- **URL**: `https://atcoder.jp/contests/kupc2019/tasks/kupc2019_k` | **Constraints**: $N, M \le 2 \times 10^5$, $\bmod 998244353$.
- **Statement**: Count operation sequences on $N$ counters with increment-one and increment-all moves, reducing to a rational substitution into a Catalan / binomial series.
- **Tags**: `[Rational-Substitution]`, `[Catalan-Kernel]` | **Diagnostic Signal**: Increment-all shifts the threshold, corresponding to substituting $y = \frac{x}{(1-x)^k}$ into a base OGF.
- **3-Tier Hints**: (1) Write the bivariate OGF marking single-increments by $x$ and all-increments by $y$. (2) Eliminate $y$ via the capacity constraint, yielding a univariate composition $A(x/(1-x))$. (3) Extract coefficients via Lagrange Inversion or Taylor shift in $O(N \log N)$ time.
- **Solution Formula**: $[x^N] A\left(\frac{x}{1-x}\right) = \sum_{k=0}^N a_k \binom{N-1}{k-1}$.

#### Problem 2A-4: HDU 5855 — Less Time, More Profit (`Stepping Stone`)
- **URL**: `https://acm.hdu.edu.cn/showproblem.php?pid=5855` | **Constraints**: $N \le 10^5$.
- **Statement**: Compute sequence transforms where each element can be delayed by an arbitrary number of idle steps, corresponding to the rational substitution $y = \frac{x}{1 - x}$ into an OGF $A(y) = \sum_{k=0}^n a_k y^k$.
- **Tags**: `[Rational-Substitution]`, `[Euler-Series-Transform]` | **Diagnostic Signal**: Substituting $y = \frac{x}{1 - x}$ (or $y = \frac{x}{1 + x}$ for Euler's alternating series acceleration) maps $a_k y^k \mapsto a_k x^k (1 - x)^{-k}$.
- **3-Tier Hints**: (1) Expand $[x^n] A\left(\frac{x}{1 - x}\right) = \sum_{k=0}^n a_k \binom{n - 1}{k - 1}$. (2) Rewrite $\binom{n - 1}{k - 1} = \frac{(n - 1)!}{(k - 1)! (n - k)!}$ to recognize a standard EGF convolution! (3) Multiply $\sum_{k=1}^n \frac{a_k}{(k - 1)!} x^k$ by $\sum_{j=0}^n \frac{x^j}{j!}$ via NTT in $O(n \log n)$ time.
- **Solution Formula**: $[x^n] A\left(\frac{x}{1 - x}\right) = a_0 [n = 0] + (n - 1)! [x^n] \left(\sum_{k=1}^n \frac{a_k}{(k - 1)!} x^k\right) e^x$.

#### Problem 2A-5: AtCoder ABC 300 Ex — Fibonacci: Revisited (`Advanced`)
- **URL**: `https://atcoder.jp/contests/abc300/tasks/abc300_h` | **Constraints**: $K \le 2.5 \times 10^5, N \le 10^{18}$, $\bmod 998244353$.
- **Statement**: Given $a_0 = \dots = a_{K-1} = 1$ and $a_n = \sum_{i=1}^K a_{n-i}$ for $n \ge K$, compute $a_N \bmod 998244353$.
- **Tags**: `[Bostan-Mori]`, `[3-Sparse-Denominator]` | **Diagnostic Signal**: $Q(x) = 1 - x - \dots - x^K = \frac{1 - 2x + x^{K+1}}{1 - x}$.
- **3-Tier Hints**: (1) Express $A(x) = \frac{P(x)}{1 - x - \dots - x^K}$ where $\deg P < K$. (2) Run Bostan–Mori $[x^N] \frac{P(x)}{Q(x)} = [x^{\lfloor N/2 \rfloor}] \frac{U(x^2)}{Q(x)Q(-x)}$ in $O(K \log K \log N)$ time. (3) Alternatively, use $(1-x)Q(x) = 1 - 2x + x^{K+1}$ to perform $O(K)$ 3-sparse modular reduction during binary exponentiation!
- **Solution Formula**: $[x^N] \frac{1 - x^K}{1 - 2x + x^{K+1}} \bmod 998244353$.

#### Problem 2A-6: AtCoder ARC 136 F — Flip Cells (`Advanced`)
- **URL**: `https://atcoder.jp/contests/arc136/tasks/arc136_f` | **Constraints**: $H, W \le 50, HW \le 2500$, $\bmod 998244353$.
- **Statement**: In an $H \times W$ binary grid, each step flips a uniformly random cell; stop when the row-sums match target counts $A_1, \dots, A_H$ and the grid reaches target state $S$. Find the expected stopping time.
- **Tags**: `[Switching-PGF]`, `[Exponential-Parity-Substitution]`, `[Residue-Derivative]` | **Diagnostic Signal**: Expected hitting time of a Markov walk on $\{0, 1\}^{HW}$ is $\left(\frac{F}{G}\right)'(1)$ where $F, G$ are exponential generating functions evaluated at $e^{x / HW}$ and $e^{-x / HW}$.
- **3-Tier Hints**: (1) For row $i$ with initial distance $d_i$ and target ones $A_i$, the row EGF is $\sum_{k} c_{i, k} (e^{x} + e^{-x})^k (e^x - e^{-x})^{W - k}$. (2) Multiply across all $H$ rows in the basis $u = e^{-2x / HW}$ to get $\sum_{j=0}^{HW} c_j e^{(1 - 2j/HW) x}$. (3) Transform the EGF into the ordinary PGF via $\sum_{n \ge 0} \lambda^n z^n = \frac{1}{1 - \lambda z}$ and evaluate $\frac{d}{dz}\left(\frac{F(z)}{G(z)}\right)\Big|_{z=1}$ canceling the $(1 - z)^{-1}$ pole at $j = 0$!
- **Solution Formula**: $\text{Ans} = \frac{F_{\text{reg}}(1) - G_{\text{reg}}(1)}{c_0}$ where $F_{\text{reg}}(1) = \sum_{j=1}^{HW} \frac{f_j}{1 - \lambda_j}$.

#### Problem 2A-7: Codeforces 1349D — Slime and Biscuits (`Mastery`)
- **Cross-Reference**: See **Problem 5A-25** (and Wave 2A #7, Wave 2B #E13) for full martingale potential + first-difference order reduction.

#### Problem 2A-8: Luogu P4491 — [HAOI2018] 染色 (`Intermediate`)
- **Cross-Reference**: Identical to **Problem 2B-A7** (Binomial Inversion $F(x) = G(x - 1)$ via reverse NTT Taylor shift in $O(M \log M)$ time).

---

### Module B: Algebraic Radicals, Catalan, Motzkin & Schröder Paths (Problems 2A-9 to 2A-18)

#### Problem 2A-9: AtCoder ABC 222 H — Beautiful Binary Tree (`Stepping Stone`)
- **Cross-Reference**: Identical to **Problem 1A-13**.

#### Problem 2A-10: Project Euler 755 — Not Zeckendorf (`Stepping Stone`)
- **URL**: `https://projecteuler.net/problem=755` | **Constraints**: $N \le 10^{13}$.
- **Statement**: Count representations of $n \le N$ as a sum of distinct Fibonacci numbers $F_2 = 1, F_3 = 2, F_4 = 3, F_5 = 5, \dots$, i.e., compute $\sum_{n=0}^N [x^n] \prod_{k \ge 2} (1 + x^{F_k})$.
- **Tags**: `[Fibonacci-Generating-Function]`, `[Subset-Sum-Pruning]` | **Diagnostic Signal**: Since $\sum_{j=2}^{k-1} F_j = F_{k+1} - 2$, whenever the remaining budget exceeds $F_{k+1} - 2$, ALL $2^{k-2}$ subsets of $\{F_2, \dots, F_{k-1}\}$ are valid!
- **3-Tier Hints**: (1) Write the OGF $P(x) = \prod_{k=2}^{64} (1 + x^{F_k})$ and seek $\sum_{n=0}^N [x^n] P(x)$. (2) Recurse from largest Fibonacci number $F_k$ down to $F_2$ with current upper bound $N$: if $N \ge F_{k+1} - 2$, return $2^{k-1}$ immediately in $O(1)$! (3) Otherwise branch on excluding $F_k$ vs. including $F_k$ (when $N \ge F_k$).
- **Solution Formula**: Recursive prefix-sum extraction of $\prod_{k \ge 2} (1 + x^{F_k})$ in $< 1\text{ ms}$.

#### Problem 2A-11: LibreOJ 6261 — Catalan Radical Convolution (`Stepping Stone`)
- **URL**: `https://loj.ac/p/6261` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
- **Statement**: Compute powers and convolutions of the Catalan generating function $C(x) = \frac{1 - \sqrt{1 - 4x}}{2x}$ and generalized radical $(1 - 4x)^{-k/2}$.
- **Tags**: `[Catalan-Power]`, `[Generalized-Binomial]` | **Diagnostic Signal**: $C(x)^k$ has closed-form coefficient $[x^n] C(x)^k = \frac{k}{2n + k} \binom{2n + k}{n}$.
- **3-Tier Hints**: (1) Use the identity $C(x) = 1 + x C(x)^2$. (2) By Lagrange Inversion, $[x^n] C(x)^k = \frac{k}{n + k} \binom{2n + k - 1}{n}$. (3) Convolve with the input polynomial via a single NTT in $O(N \log N)$ time.
- **Solution Formula**: $[x^n] C(x)^k = \frac{k}{2n + k} \binom{2n + k}{n}$.

#### Problem 2A-12: Codeforces Gym 102978 H — Motzkin Paths / Harsh Comments (`Intermediate`)
- **URL**: `https://codeforces.com/gym/102978/problem/H` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
- **Statement**: Count weighted lattice paths with up $(+1)$, level $(0)$, and down $(-1)$ steps satisfying $M(x) = 1 + ax M(x) + bx^2 M(x)^2$ (or see **Problem 2B-D2** for the Aho–Corasick forbidden-substring variant).
- **Tags**: `[Motzkin-Radical]`, `[Lagrange-Trinomial]` | **Diagnostic Signal**: Quadratic equation $b x^2 M^2 + (ax - 1) M + 1 = 0 \implies M(x) = \frac{1 - ax - \sqrt{(1 - ax)^2 - 4bx^2}}{2bx^2}$.
- **3-Tier Hints**: (1) By Lagrange Inversion on $T(x) = x(1 + a T + b T^2)$ where $T(x) = x M(x)$, $[x^n] M(x) = \frac{1}{n+1} [u^n] (1 + au + bu^2)^{n+1}$. (2) Expand $(1 + au + bu^2)^{n+1} = \sum_k \binom{n+1}{k} (bu^2)^k (1 + au)^{n+1-k}$. (3) Or use the 3-term D-finite recurrence $(n+2) M_n = (2n+1) a M_{n-1} + (3n-3)(4b - a^2) M_{n-2}$ in $O(N)$ time!
- **Solution Formula**: $M_n = \frac{1}{n+1} \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n+1}{k} \binom{n+1-k}{n-2k} b^k a^{n-2k}$.

#### Problem 2A-13: LibreOJ 6077 — 逆序对 / Schröder & Delannoy Path Convolution (`Intermediate`)
- **URL**: `https://loj.ac/p/6077` | **Constraints**: $N, K \le 10^5$, $\bmod (10^9+7)$.
- **Statement**: Count permutations of length $N$ with $K$ inversions (or weighted Delannoy/Schröder lattice paths) via $\prod_{i=1}^N \frac{1 - x^i}{1 - x} = (1 - x)^{-N} \prod_{i=1}^N (1 - x^i)$.
- **Tags**: `[Mahonian-Inversion]`, `[Pentagonal-DP]` | **Diagnostic Signal**: $\prod_{i=1}^N (1 - x^i) \equiv \prod_{i \ge 1} (1 - x^i) \pmod{x^{K+1}}$ when $K \le N$, or split by size $\sqrt{K}$!
- **3-Tier Hints**: (1) Write $F(x) = \frac{1}{(1-x)^N} \prod_{i=1}^N (1 - x^i)$. (2) Compute $\prod_{i=1}^N (1 - x^i) \bmod x^{K+1}$ in $O(K \sqrt{K})$ time using bounded partition DP (choosing distinct parts from $\{1, \dots, N\}$). (3) Convolve with $[x^j] (1-x)^{-N} = \binom{N + j - 1}{j}$ in $O(K)$ time!
- **Solution Formula**: $[x^K] (1-x)^{-N} \prod_{i=1}^N (1 - x^i)$ in $O(K \sqrt{K})$ time (works for any modulus!).

#### Problem 2A-14: AtCoder AGC 021 E — Ball Eat Chameleons (`Intermediate`)
- **URL**: `https://atcoder.jp/contests/agc021/tasks/agc021_e` | **Constraints**: $N, K \le 5 \times 10^5$, $\bmod 998244353$.
- **Statement**: Count sequences of $K$ red/blue balls fed to $N$ chameleons so all $N$ chameleons turn red.
- **Tags**: `[Reflection-Principle]`, `[Ballot-Catalan]` | **Diagnostic Signal**: For a fixed count $R$ of red balls and $B = K - R$ of blue balls ($R \ge B$), a sequence is valid iff the minimum prefix sum of $(+1 \text{ for } B, -1 \text{ for } R)$ does not exceed $N - (R - B + [R = B])$.
- **3-Tier Hints**: (1) If $R < B$, answer is $0$. If $R = B$, the last ball must be Blue, reducing to $(R, B-1)$. (2) A chameleon can turn red with 1 Red + 0 Blue, or $m+1$ Red + $m$ Blue (ending in Blue). This holds iff no prefix has $B_{\text{prefix}} - R_{\text{prefix}} > R - N$. (3) By the Reflection Principle, the number of such paths for a given $(R, B)$ is $\binom{R+B}{R} - \binom{R+B}{2R - N + 1}$.
- **Solution Formula**: $\sum_{R = \max(N, \lceil K/2 \rceil)}^K \left(\binom{R + B'}{R} - \binom{R + B'}{2R - N + 1}\right)$ where $B' = K - R - [R = K - R]$.

#### Problem 2A-15: AtCoder `fps_24_v` — 12 Directions (`Intermediate`)
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_v` | **Constraints**: $N \le 2.5 \times 10^5$, $\bmod 998244353$.
- **Statement**: Count $N$-step 2D lattice walks from $(0, 0)$ to $(X, Y)$ (or returning to the origin / staying in the upper half-plane) where each step belongs to a 12-direction step set $S(x, y)$.
- **Tags**: `[2D-Step-Factorization]`, `[Binomial-Convolution]`, `[Lagrange-D-Finite]` | **Diagnostic Signal**: Either the 12-step Laurent polynomial $S(x, y)$ factors into a product of lower-degree factors, or it reduces to a 1D Laurent step polynomial $P(y) = y^{-2} + a y^{-1} + b + c y + y^2$ whose excursions are solved via the Kernel Method / Lagrange Inversion / D-finite recurrence!
- **3-Tier Hints**: (1) Write out the Laurent polynomial $S(x, y) = \sum_{(dx, dy) \in D} x^{dx} y^{dy}$. (2) When $S(x, y)$ factors into $(x^\alpha + y^\beta)(x^\gamma + y^\delta)(x^\epsilon + y^\zeta)$ (or $(x+x^{-1}+y+y^{-1})(1+xy+x^{-1}y^{-1})$), expand into products of binomial coefficients. (3) When non-separable or restricted to $y \ge 0$, apply Lagrange Inversion / D-finite holonomic recurrence on $P(x, y)^N$ in $O(N \log N)$ or $O(N)$ time!
- **Solution Formula**: $[x^X y^Y] S(x, y)^N$ extracted in $O(N)$ or $O(N \log N)$ time.

#### Problem 2A-16: Luogu P3978 — [TJOI2015] 概率论 (`Intermediate`)
- **Cross-Reference**: Identical to **Problem 3A-13** ($\frac{N(N+1)}{2(2N-1)}$ via $\frac{x}{\sqrt{1-4x}}$).

#### Problem 2A-17: UOJ 424 — count (`Advanced`)
- **Cross-Reference**: See **Problem 5A-29** (Chebyshev rational function $Q_m(x)/Q_{m+1}(x)$ for bounded left-depth Cartesian trees).

#### Problem 2A-18: AtCoder AGC 054 E — ZigZag Break (`Advanced`)
- **URL**: `https://atcoder.jp/contests/agc054/tasks/agc054_e` | **Constraints**: $T \le 3 \times 10^5, N \le 10^6$, $\bmod 998244353$.
- **Statement**: Count permutations of $\{1, \dots, N\}$ starting with $A$ that can be reduced to length $2$ by repeatedly deleting the middle element of any monotone triplet $x < y < z$ or $x > y > z$.
- **Tags**: `[Telescoping-Rational-GF]`, `[Complementary-Condition]` | **Diagnostic Signal**: A permutation is irreducible iff its endpoints trap all interior steps, yielding a clean linear combination of 4 binomial coefficients per query!
- **3-Tier Hints**: (1) Characterize bad permutations by the first/last elements and local extrema. (2) Express the OGF of irreducible configurations via inclusion-exclusion. (3) The resulting coefficient $[x^N]$ collapses into a closed-form $O(1)$ binomial expression per test case!
- **Solution Formula**: Closed-form $O(1)$ per query after $O(N)$ factorial precomputation.

---

### Module C: Stirling Numbers, Falling Factorials & Binomial Sums (Problems 2A-19 to 2A-29)

#### Problem 2A-19: Codeforces 1342E — Placing Rooks (`Stepping Stone`)
- **URL**: `https://codeforces.com/problemset/problem/1342/E` | **Constraints**: $N \le 2 \times 10^5, K \le N^2$, $\bmod 998244353$.
- **Statement**: Place $N$ rooks on an $N \times N$ board so that every cell is attacked and exactly $K$ pairs of rooks attack each other.
- **Tags**: `[Stirling-S2-Single-Term]`, `[Inclusion-Exclusion]` | **Diagnostic Signal**: Every cell is attacked iff either all $N$ rows or all $N$ columns contain a rook; $K$ attacking pairs means the $N$ rooks occupy $N - K$ columns.
- **3-Tier Hints**: (1) If $K \ge N$, answer is $0$. Place 1 rook per row; if they occupy $c$ distinct columns, there are $N - c$ attacking pairs, so $c = N - K$. (2) The number of ways to map $N$ rows surjectively onto $N - K$ chosen columns is $\binom{N}{N-K} (N-K)! \left\{\begin{matrix} N \\ N - K \end{matrix}\right\}$. (3) Multiply by $2$ if $K > 0$ (for rows vs. columns symmetry).
- **Solution Formula**: $[K=0] N! + [1 \le K < N] \cdot 2 \binom{N}{N-K} \sum_{j=0}^{N-K} (-1)^{N-K-j} \binom{N-K}{j} j^N$.

#### Problem 2A-20: AtCoder `fps_24_n` — Coins 2 (`Stepping Stone`)
- **Cross-Reference**: Identical to **Problem 1A-7b**.

#### Problem 2A-21: Luogu P4091 — [HEOI2016 / TJOI2016] 求和 (`Intermediate`)
- **URL**: `https://www.luogu.com.cn/problem/P4091` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
- **Statement**: Compute $\sum_{i=0}^N \sum_{j=0}^i \left\{\begin{matrix} i \\ j \end{matrix}\right\} 2^j j! \bmod 998244353$.
- **Tags**: `[Stirling-S2-Column-Sum]`, `[NTT-Convolution]` | **Diagnostic Signal**: Expand $\left\{\begin{matrix} i \\ j \end{matrix}\right\} j! = \sum_{k=0}^j (-1)^{j-k} \binom{j}{k} k^i$ and swap the summation order so $\sum_{i=0}^N k^i = \frac{k^{N+1} - 1}{k - 1}$ is evaluated in $O(1)$ BEFORE the NTT!
- **3-Tier Hints**: (1) Swap the sum over $i$ inside: $\sum_{j=0}^N 2^j j! \sum_{i=j}^N \left\{\begin{matrix} i \\ j \end{matrix}\right\}$ (note $\left\{\begin{matrix} i \\ j \end{matrix}\right\} = 0$ for $i < j$). (2) Substitute $j! \left\{\begin{matrix} i \\ j \end{matrix}\right\} = \sum_{k=0}^j (-1)^{j-k} \binom{j}{k} k^i$ and sum over $i = 0, \dots, N$: $S(k) = \sum_{i=0}^N k^i$. (3) Now $\sum_{j=0}^N 2^j j! \sum_{k=0}^j \frac{(-1)^{j-k}}{(j-k)!} \frac{S(k)}{k!}$ is a single NTT convolution!
- **Solution Formula**: $\sum_{j=0}^N 2^j j! [x^j] \left(\sum_{r=0}^N \frac{(-1)^r}{r!} x^r\right) \left(\sum_{k=0}^N \frac{\sum_{i=0}^N k^i}{k!} x^k\right)$.

#### Problem 2A-22: Luogu P6667 — [清华集训2016] 如何优雅地求和 (`Intermediate`)
- **URL**: `https://www.luogu.com.cn/problem/P6667` | **Constraints**: $n \le 10^9, m \le 2 \times 10^4, x \in [0, 998244352]$, $\bmod 998244353$.
- **Statement**: Given $f(0), f(1), \dots, f(m)$ for a degree-$m$ polynomial $f$, compute $\sum_{k=0}^n \binom{n}{k} x^k (1 - x)^{n-k} f(k) \bmod 998244353$.
- **Tags**: `[Falling-Factorial-Polynomial]`, `[Point-Value-to-Falling-Factorial]` | **Diagnostic Signal**: $\binom{n}{k} k^{\underline{j}} = n^{\underline{j}} \binom{n-j}{k-j}$, so converting $f(k) = \sum_{j=0}^m b_j \binom{k}{j}$ makes the sum over $k$ collapse via the Binomial Theorem to $\sum_{j=0}^m b_j \binom{n}{j} x^j$!
- **3-Tier Hints**: (1) Express $f(k)$ in the binomial / falling-factorial basis: $f(k) = \sum_{j=0}^m b_j \binom{k}{j}$. (2) By finite differences (or EGF convolution), $\sum_{j=0}^m \frac{b_j}{j!} t^j = e^{-t} \sum_{i=0}^m \frac{f(i)}{i!} t^i \bmod t^{m+1}$! (3) Substitute into the sum: $\sum_{j=0}^m b_j \binom{n}{j} x^j \sum_{k=j}^n \binom{n-j}{k-j} x^{k-j} (1-x)^{n-k} = \sum_{j=0}^m b_j \binom{n}{j} x^j$.
- **Solution Formula**: $\sum_{j=0}^m \binom{n}{j} x^j j! [t^j] \left(e^{-t} \sum_{i=0}^m \frac{f(i)}{i!} t^i\right)$ in $O(m \log m)$ (or $O(m)$ via Wave 5A #18).

#### Problem 2A-23: Luogu P6620 — [省选联考 2020 A 卷] 组合数问题 (`Intermediate`)
- **URL**: `https://www.luogu.com.cn/problem/P6620` | **Constraints**: $n, x \le 10^9, m \le 1000$, arbitrary modulus $p \le 10^9$.
- **Statement**: Given $f(k) = \sum_{i=0}^m a_i k^i$, compute $\sum_{k=0}^n f(k) x^k \binom{n}{k} \bmod p$.
- **Tags**: `[Stirling-S2-Expansion]`, `[Falling-Factorial-Binomial-Absorption]` | **Diagnostic Signal**: Since $p$ is an arbitrary modulus and $m \le 1000$, convert $k^i = \sum_{j=0}^i \left\{\begin{matrix} i \\ j \end{matrix}\right\} k^{\underline{j}}$ in $O(m^2)$ without division!
- **3-Tier Hints**: (1) Precompute Stirling numbers $\left\{\begin{matrix} i \\ j \end{matrix}\right\} \bmod p$ for $0 \le j \le i \le m$ via Pascal-like DP in $O(m^2)$ time. (2) Change basis: $f(k) = \sum_{j=0}^m b_j k^{\underline{j}}$ where $b_j = \sum_{i=j}^m a_i \left\{\begin{matrix} i \\ j \end{matrix}\right\} \bmod p$. (3) Use $k^{\underline{j}} \binom{n}{k} = n^{\underline{j}} \binom{n-j}{k-j}$ and sum over $k$ to get $\sum_{j=0}^m b_j n^{\underline{j}} x^j (1 + x)^{n-j} \bmod p$!
- **Solution Formula**: $\sum_{j=0}^{\min(n, m)} \left(\sum_{i=j}^m a_i \left\{\begin{matrix} i \\ j \end{matrix}\right\}\right) n^{\underline{j}} x^j (1 + x)^{n-j} \bmod p$ in $O(m^2)$ time.

#### Problem 2A-24: Codeforces 932E — Team Work (`Intermediate`)
- **Cross-Reference**: Identical to **Problem 1B-10**.

#### Problem 2A-25: Codeforces 1613F — Tree Coloring (`Intermediate`)
- **URL**: `https://codeforces.com/problemset/problem/1613/F` | **Constraints**: $N \le 2.5 \times 10^5$, $\bmod 998244353$.
- **Statement**: Given a rooted tree on $N$ vertices, count permutations $p_1, \dots, p_N$ such that for every vertex $u$ and child $v$ of $u$, $p_v \neq p_u - 1$.
- **Tags**: `[Rook-Polynomial-Tree]`, `[D&C-NTT]`, `[Inclusion-Exclusion]` | **Diagnostic Signal**: Choosing $k$ violated edges $(u, v)$ where $p_v = p_u - 1$ requires picking at most 1 child $v$ for each vertex $u$! Thus vertex $u$ with $c_u$ children independently contributes $(1 + c_u x)$!
- **3-Tier Hints**: (1) A set of $k$ violated tree edges is valid iff no two edges share the same parent $u$ (and since it's a tree, they automatically form disjoint paths). (2) Therefore, the number of ways to pick $k$ violated edges is $[x^k] \prod_{u=1}^N (1 + c_u x)$, where $c_u$ is the number of children of $u$. (3) Compute $\prod_{u=1}^N (1 + c_u x)$ via divide-and-conquer NTT in $O(N \log^2 N)$ time and sum $(-1)^k c_k (N - k)!$.
- **Solution Formula**: $\sum_{k=0}^{N-1} (-1)^k (N - k)! [x^k] \prod_{u=1}^N (1 + c_u x) \bmod 998244353$.

#### Problem 2A-26: Codeforces 960G — Bandit Blues (`Advanced`)
- **Cross-Reference**: Identical to **Problem 1A-23**.

#### Problem 2A-27: AtCoder `fps_24_q` — Dice (`Advanced`)
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_q` | **Constraints**: $N, M \le 2.5 \times 10^5$, $\bmod 998244353$.
- **Statement**:
  - **Formulation A (Falling-Factorial Dice Moments)**: Compute higher-order moments / falling-factorial expectations of $N$-dice sums via the EGF-to-Falling-Factorial bridge $P(1+t)^N$.
  - **Formulation B (Mod-$M$ Cyclic Exclusion — `fps_24_q`)**: Roll a 6-sided die $N$ times; if a face appears $M$ times in a row (or the sum hits a forbidden boundary), reduce via the rational OGF $[x^N] \frac{1-x}{1-7x+6x^{M+1}}$!
- **Tags**: `[Falling-Factorial-GF]`, `[Moment-Generating-Function]`, `[Sparse-Denominator-Series]` | **Diagnostic Signal**: $P(1 + t) = \sum_{j \ge 0} \mathbb{E}[X^{\underline{j}}] \frac{t^j}{j!}$ for moments; $\frac{1-x}{1-7x+6x^{M+1}}$ expanded via geometric series in $x^{M+1}$ for run-length exclusion.
- **3-Tier Hints**: (1) For moments, shift $P(x)$ to $1+t$, take $P(1+t)^N \bmod t^{M+1}$, and multiply by Stirling numbers $\left\{\begin{matrix} K \\ j \end{matrix}\right\}$. (2) For $[x^N] \frac{1-x}{1-7x+6x^{M+1}}$, expand $\frac{1}{1 - 7x(1 - \frac{6}{7} x^M)} = \sum_{k=0}^{\lfloor N/(M+1) \rfloor} (-6)^k x^{k(M+1)} (1 - 7x)^{-(k+1)}$. (3) Sum the $\lfloor N/M \rfloor$ terms in $O(N/M)$ time!
- **Solution Formula**: $\mathbb{E}[X^{\underline{j}}] = j! [t^j] P(1 + t)^N$; or $[x^N]\frac{1-x}{1-7x+6x^{M+1}} = (1 - \Delta_N) \sum_{k=0}^{\lfloor N/(M+1) \rfloor} (-6)^k 7^{N - k(M+1)} \binom{N - kM}{k}$.

#### Problem 2A-28: Codeforces 1278F — Cards (`Advanced`)
- **URL**: `https://codeforces.com/problemset/problem/1278/F` | **Constraints**: $N, M \le 998244352, K \le 5000$ (or $10^7$), $\bmod 998244353$.
- **Statement**: Shuffle a deck of $M$ cards (1 Joker) $N$ times, each time looking at the top card. Let $X \sim \text{Binomial}(N, 1/M)$ be the number of times the Joker is seen. Compute $\mathbb{E}[X^K] \bmod 998244353$.
- **Tags**: `[Binomial-Moment]`, `[Stirling-S2]` | **Diagnostic Signal**: $\mathbb{E}[X^{\underline{j}}] = N^{\underline{j}} p^j$ where $p = 1/M$.
- **3-Tier Hints**: (1) Expand $X^K = \sum_{j=0}^K \left\{\begin{matrix} K \\ j \end{matrix}\right\} X^{\underline{j}}$. (2) By linearity of expectation, $\mathbb{E}[X^{\underline{j}}] = N^{\underline{j}} M^{-j}$. (3) Sum over $j = 0, \dots, \min(N, K)$ in $O(K^2)$ (or $O(K)$ via `EI 科技` Wave 5A #17).
- **Solution Formula**: $\sum_{j=0}^{\min(N, K)} \left\{\begin{matrix} K \\ j \end{matrix}\right\} N^{\underline{j}} M^{-j} \bmod 998244353$.

#### Problem 2A-29: Codeforces 1097G — Vladislav and a Great Legend (`Mastery`)
- **Cross-Reference**: Identical to **Problem 2B-A14** (Stirling power decomposition $f(X)^K = \sum_{j=0}^K \left\{\begin{matrix} K \\ j \end{matrix}\right\} j! \binom{f(X)}{j}$ + $O(NK)$ tree knapsack DP).

---

### Module D: Harmonic $\ln$-$\exp$ Compression, Power Sums & Euler Transform (Problems 2A-30 to 2A-39)

#### Problem 2A-30: Luogu P4389 — 付公主的背包 (`Stepping Stone`)
- **Cross-Reference**: Identical to **Problem 1A-7a**.

#### Problem 2A-31: AtCoder ABC 267 Ex — Odd Sum (`Intermediate`)
- **Cross-Reference**: Identical to **Problem 1B-12**.

#### Problem 2A-32: Luogu P4705 — 玩游戏 (`Intermediate`)
- **Cross-Reference**: Identical to **Problem 1A-24**.

#### Problem 2A-33: AtCoder ARC 106 E / yukicoder 1145 — Sum of Powers (`Intermediate`)
- **URL**: `https://yukicoder.me/problems/no/1145` | **Constraints**: $N, M \le 2 \times 10^5$, $\bmod 998244353$.
- **Statement**: Given $a_1, \dots, a_N$, compute $S_k = \sum_{i=1}^N a_i^k \bmod 998244353$ for all $k = 1, \dots, M$.
- **Tags**: `[Newton-Identities]`, `[Log-Derivative]` | **Diagnostic Signal**: $\sum_{k \ge 1} S_k x^k = \sum_{i=1}^N \frac{a_i x}{1 - a_i x} = -x \frac{P'(x)}{P(x)}$ where $P(x) = \prod_{i=1}^N (1 - a_i x)$.
- **3-Tier Hints**: (1) Multiply $\prod_{i=1}^N (1 - a_i x)$ via a divide-and-conquer binary tree of NTTs in $O(N \log^2 N)$ time. (2) Compute $P'(x) P(x)^{-1} \bmod x^M$ via one polynomial inversion. (3) Negate and shift by $x$ to read off $S_1, \dots, S_M$.
- **Solution Formula**: $\sum_{k=1}^M S_k x^k = -x \frac{d}{dx} \ln \prod_{i=1}^N (1 - a_i x) \pmod{x^{M+1}}$.

#### Problem 2A-34: Luogu P4727 — [HNOI2009] 图的同构记数 (`Intermediate`)
- **URL**: `https://www.luogu.com.cn/problem/P4727` | **Constraints**: $N \le 60$, $\bmod 997$.
- **Statement**: Count unlabeled simple undirected graphs on $N$ vertices up to isomorphism.
- **Tags**: `[Burnside-Lemma]`, `[Polya-Cycle-Index]` | **Diagnostic Signal**: Average $2^{c(\sigma)}$ over all $\sigma \in S_N$, where $c(\sigma)$ depends only on the cycle-type partition $\lambda \vdash N$ of $\sigma$!
- **3-Tier Hints**: (1) By Burnside's Lemma, $\text{Ans} = \frac{1}{N!} \sum_{\sigma \in S_N} 2^{c_{\text{edge}}(\sigma)}$. (2) If $\sigma$ has cycle lengths $l_1, \dots, l_k$, a cycle of length $l_i$ induces $\lfloor l_i / 2 \rfloor$ internal edge orbits, and two cycles of lengths $l_i, l_j$ induce $\gcd(l_i, l_j)$ cross-edge orbits. (3) Enumerate all $p(N)$ integer partitions of $N$ ($p(60) = 966,467$) and sum over their conjugacy class sizes $\frac{N!}{\prod c_r! r^{c_r}}$.
- **Solution Formula**: $\sum_{\lambda \vdash N} \frac{1}{\prod_r c_r! r^{c_r}} 2^{\sum_i \lfloor l_i / 2 \rfloor + \sum_{i < j} \gcd(l_i, l_j)}$.

#### Problem 2A-35: LibreOJ 6089 — 小 Y 的背包计数问题 (`Advanced`)
- **URL**: `https://loj.ac/p/6089` | **Constraints**: $N \le 10^5$, $\bmod 23333333$ (non-NTT modulus!).
- **Statement**: Given item $i$ of weight $i$ and maximum count $i$ for $i = 1, \dots, N$, count ways to fill a knapsack of weight $N$ modulo $23333333$.
- **Tags**: `[Sqrt-Decomposition-Knapsack]`, `[Ferrers-Diagram-DP]` | **Diagnostic Signal**: For $i > B = \lfloor\sqrt{N}\rfloor$, the count bound $c_i \le i$ is automatically satisfied because $i \cdot (i + 1) > N$! And the modulus $23333333$ is non-NTT, demanding an $O(N\sqrt{N})$ combinatorial split.
- **3-Tier Hints**: (1) Set $B = \lfloor\sqrt{N}\rfloor$. For small items $1 \le i \le B$, run bounded knapsack DP using prefix sums of stride $i$ (like **Problem 1B-2**) in $O(N \sqrt{N})$ time. (2) For large items $i > B$, the upper bound $c_i \le i$ is redundant ($i^2 > N$), so we just need unrestricted partitions into parts $> B$. (3) Count partitions into $j \le B$ parts of size $> B$ via the standard Ferrers-diagram recurrence $g(j, w) = g(j, w - j) + g(j - 1, w - (B + 1))$ in $O(N\sqrt{N})$ time, and convolve!
- **Solution Formula**: $\sum_{w=0}^N f_{\le B}(w) \cdot \left(\sum_{j=0}^B g_{>B}(j, N - w)\right) \bmod 23333333$ in $O(N\sqrt{N})$ time.

#### Problem 2A-36: Luogu P3784 — [SDOI2017] 遗忘的集合 (`Advanced`)
- **Cross-Reference**: See **Problem 1B-25** (Inverse Euler Transform: compute $g(x) = \ln A(x) \bmod x^{n+1}$, then recover $c_d \in \{0, 1\}$ by Möbius inversion $d c_d = \sum_{k \mid d} \mu(d/k) k g_k$ in $O(n \log n)$ time).

#### Problem 2A-37: LibreOJ 6503 — Magic (`Advanced`)
- **URL**: `https://loj.ac/p/6503` | **Constraints**: $m \le 10^5, N = \sum a_i \le 4 \times 10^5$, $\bmod 998244353$.
- **Statement**: Given $m$ card colors with counts $a_1, \dots, a_m$, count permutations of the $N$ cards with no two adjacent cards of the same color (or with exact $k$ adjacent monochromatic pairs).
- **Tags**: `[Run-Length-IE]`, `[Laguerre-Polynomial]`, `[D&C-NTT]` | **Diagnostic Signal**: Splitting $a_i$ identical cards of color $i$ into $j$ non-empty blocks has EGF weight $\binom{a_i - 1}{j - 1} (-1)^{a_i - j} \frac{x^j}{j!}$.
- **3-Tier Hints**: (1) By inclusion-exclusion on adjacent equal pairs within color $i$, partitioning $a_i$ labeled/unlabeled items into $j$ runs contributes $\binom{a_i - 1}{j - 1} (-1)^{a_i - j} \frac{x^j}{j!}$. (2) Construct this degree-$a_i$ polynomial $P_i(x)$ for each color $i = 1, \dots, m$. (3) Multiply $\prod_{i=1}^m P_i(x)$ via divide-and-conquer NTT in $O(N \log^2 N)$ time and sum $k! [x^k]$.
- **Solution Formula**: $\sum_{k=1}^N k! [x^k] \prod_{i=1}^m \left(\sum_{j=1}^{a_i} (-1)^{a_i - j} \binom{a_i - 1}{j - 1} \frac{x^j}{j!}\right)$.

#### Problem 2A-38: Luogu P5824 — 十二重计数法 (`Advanced`)
- **Cross-Reference**: Identical to **Problem 1A-22** (The Twelvefold Way in $O((n+m)\log(n+m))$).

#### Problem 2A-39: LibreOJ 6268 / yukicoder 899 & Pólya Cycle Index Necklaces (`Mastery`)
- **URL**: `https://loj.ac/p/6268` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
- **Statement**: Given a component OGF $A(x)$ with $[x^0] A(x) = 0$, simultaneously compute the sequence OGF $\text{SEQ}(A) = \frac{1}{1 - A(x)}$, the cyclic necklace OGF $\text{CYC}(A) = \sum_{k=1}^N \frac{\varphi(k)}{k} \ln \frac{1}{1 - A(x^k)}$, and the multiset Euler transform $\text{MSET}(A) = \exp\left(\sum_{k=1}^N \frac{A(x^k)}{k}\right) \bmod x^{N+1}$.
- **Tags**: `[Polya-Cycle-Index]`, `[Euler-Transform]`, `[Harmonic-Sieve]` | **Diagnostic Signal**: $\text{CYC}(A)$ and $\text{MSET}(A)$ share the inner series $L(x) = -\ln(1 - A(x)) = \sum_{m \ge 1} \frac{A(x)^m}{m}$!
- **3-Tier Hints**: (1) Compute $L(x) = -\ln(1 - A(x)) \bmod x^{N+1}$ once in $O(N \log N)$ time. (2) Note that $-\ln(1 - A(x^k)) = L(x^k)$, so $[x^n] \text{CYC}(A) = \sum_{k \mid n} \frac{\varphi(k)}{k} [x^{n/k}] L(x)$ is obtained in $O(N \log N)$ harmonic time without recomputing logs! (3) Similarly, $\ln \text{MSET}(A) = \sum_{k=1}^N \frac{A(x^k)}{k}$, followed by one $\exp$ in $O(N \log N)$ time.
- **Solution Formula**: $Z_{\text{cycle}}(x) = \sum_{k=1}^N \frac{\varphi(k)}{k} L(x^k)$ where $L(x) = \ln\frac{1}{1 - A(x)}$.

---

### Module E: Roots of Unity Filter, Cyclic Convolution & Chirp-$Z$ (Problems 2A-40 to 2A-49)

#### Problem 2A-40: LibreOJ 6485 — LJJ 学二项式定理 (`Stepping Stone`)
- **URL**: `https://loj.ac/p/6485` | **Constraints**: $T \le 10^5, N \le 10^{18}$, $\bmod 998244353$.
- **Statement**: Given $N, s, a_0, a_1, a_2, a_3$, compute $\sum_{i=0}^N \binom{N}{i} s^i a_{i \bmod 4} \bmod 998244353$.
- **Tags**: `[Roots-of-Unity-Filter]` | **Diagnostic Signal**: $4$-th roots of unity in $\mathbb{F}_{998244353}$ are $\omega_0 = 1, \omega_1 = g^{(p-1)/4}, \omega_2 = -1, \omega_3 = -\omega_1$.
- **3-Tier Hints**: (1) By the Roots of Unity Filter, $\sum_{i \equiv r \pmod 4} \binom{N}{i} s^i = \frac{1}{4} \sum_{j=0}^3 \omega^{-jr} (1 + \omega^j s)^N$. (2) Evaluate $(1 + \omega^j s)^N$ for $j = 0, 1, 2, 3$ using binary exponentiation. (3) Take the linear combination with $a_0, a_1, a_2, a_3$.
- **Solution Formula**: $\frac{1}{4} \sum_{r=0}^3 a_r \sum_{j=0}^3 \omega^{-jr} (1 + \omega^j s)^N \bmod 998244353$.

#### Problem 2A-41: BZOJ 3328 — PYXFIB (`Intermediate`)
- **URL**: `https://darkbzoj.cc/problem/3328` | **Constraints**: $N \le 10^{18}, K \le 2 \times 10^4$, prime $P \equiv 1 \pmod K$.
- **Statement**: Compute $\sum_{i=0 \atop K \mid i}^N \binom{N}{i} F_i \bmod P$, where $F_i$ is the $i$-th Fibonacci number and $K \mid (P - 1)$.
- **Tags**: `[Matrix-Roots-of-Unity-Filter]` | **Diagnostic Signal**: Replace $F_i$ with the $2 \times 2$ Fibonacci matrix $M^i$ and apply the $K$-th roots of unity filter to $(I + \omega^j M)^N$!
- **3-Tier Hints**: (1) Since $K \mid (P - 1)$, a primitive $K$-th root of unity $\omega = g^{(P-1)/K} \bmod P$ exists. (2) $\sum_{K \mid i} \binom{N}{i} M^i = \frac{1}{K} \sum_{j=0}^{K-1} (I + \omega^j M)^N$. (3) Compute the $K$ matrix powers of size $2 \times 2$ in $O(K \log N)$ time!
- **Solution Formula**: $\frac{1}{K} \sum_{j=0}^{K-1} \big[(I + \omega^j M)^N\big]_{0, 1} \bmod P$.

#### Problem 2A-42: Luogu P3702 — [SDOI2017] 序列计数 (`Intermediate`)
- **Cross-Reference**: Identical to **Problem 1B-14**.

#### Problem 2A-43: AtCoder ABC 240 G — Teleporting Takahashi (`Intermediate`)
- **URL**: `https://atcoder.jp/contests/abc240/tasks/abc240_g` | **Constraints**: $N \le 10^7$, $\bmod 998244353$.
- **Statement**: Count $N$-step 3D lattice walks from $(0, 0, 0)$ to $(X, Y, Z)$ using steps $(\pm 1, 0, 0), (0, \pm 1, 0), (0, 0, \pm 1)$.
- **Tags**: `[3D-to-2D-Walk-Decoupling]` | **Diagnostic Signal**: Fix the number of $z$-steps $k = |Z| + 2j$; the remaining $N - k$ steps lie in the 2D $(x, y)$-plane, which decouples into two independent 1D walks via $(u, v) = (x+y, x-y)$!
- **3-Tier Hints**: (1) If $n_{xy}$ steps are taken in the 2D plane to reach $(X, Y)$, rotating by $45^\circ$ gives $\binom{n_{xy}}{(n_{xy} + X + Y)/2} \binom{n_{xy}}{(n_{xy} + X - Y)/2}$ ways. (2) Iterate over the number of $z$-steps $n_z = |Z|, |Z|+2, \dots, N$ (same parity as $N - |X| - |Y|$). (3) Multiply by $\binom{N}{n_z} \binom{n_z}{(n_z + Z)/2}$ and sum in $O(N)$ time!
- **Solution Formula**: $\sum_{n_z = |Z|}^N \binom{N}{n_z} \binom{n_z}{\frac{n_z + Z}{2}} \binom{N - n_z}{\frac{N - n_z + X + Y}{2}} \binom{N - n_z}{\frac{N - n_z + X - Y}{2}}$.

#### Problem 2A-44: UOJ 450 — [集训队作业2018] 复读机 (`Intermediate`)
- **Cross-Reference**: Identical to **Problem 5A-28** (3rd roots of unity filter $\left(\frac{1}{3}(e^x + e^{\omega x} + e^{\omega^2 x})\right)^k$ for $k \le 5 \times 10^5, d \in \{1, 2, 3\}$).

#### Problem 2A-45: Codeforces 891E — Lust & The Floor-Sum Trick (`Advanced`)
- **Cross-Reference**: See **Problem 1A-16** (EGF of falling factorials $\prod_{i=1}^n (a_i - x)$) and **Problem 2A-46** for the roots-of-unity floor-sum trick $\lfloor i / k \rfloor = \frac{i - (i \bmod k)}{k}$.

#### Problem 2A-46: Luogu P5591 — 小猪佩奇学数学 (`Advanced`)
- **URL**: `https://www.luogu.com.cn/problem/P5591` | **Constraints**: $n, p < 998244353$, $k = 2^w \le 2^{20}$, $\bmod 998244353$.
- **Statement**: Compute $\sum_{i=0}^n \binom{n}{i} p^i \left\lfloor \frac{i}{k} \right\rfloor \bmod 998244353$.
- **Tags**: `[Floor-Sum-Roots-of-Unity]`, `[Geometric-Derivative-Identity]` | **Diagnostic Signal**: Rewrite $\left\lfloor \frac{i}{k} \right\rfloor = \frac{i - (i \bmod k)}{k}$ and express $i \bmod k = \sum_{r=0}^{k-1} r [i \equiv r \pmod k]$ via the $k$-th roots of unity filter, then collapse the inner sum over $r$ in $O(1)$!
- **3-Tier Hints**: (1) Split into $\frac{1}{k} \sum_{i=0}^n i \binom{n}{i} p^i - \frac{1}{k} \sum_{r=0}^{k-1} r \sum_{i \equiv r \pmod k} \binom{n}{i} p^i$. The first sum is $\frac{1}{k} n p (1 + p)^{n-1}$. (2) In the second sum, substitute $[i \equiv r \pmod k] = \frac{1}{k} \sum_{j=0}^{k-1} \omega_k^{-jr} \omega_k^{ji}$ to get $\frac{1}{k^2} \sum_{j=0}^{k-1} (1 + p \omega_k^j)^n \sum_{r=0}^{k-1} r \omega_k^{-jr}$. (3) For $j = 0$, $\sum_{r=0}^{k-1} r = \frac{k(k-1)}{2}$; for $j \neq 0$, $\sum_{r=0}^{k-1} r \omega_k^{-jr} = \frac{k}{\omega_k^{-j} - 1}$!
- **Solution Formula**: $\frac{1}{k} \left( n p (1 + p)^{n-1} - \frac{k - 1}{2} (1 + p)^n - \sum_{j=1}^{k-1} \frac{(1 + p \omega_k^j)^n}{\omega_k^{-j} - 1} \right) \bmod 998244353$ in $O(k \log n)$ time!

#### Problem 2A-47: AtCoder `fps_24_r` — Random Walk (`Advanced`)
- **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_r` | **Constraints**: $N \le 2.5 \times 10^5, K \le 10^{18}$, $\bmod 998244353$.
- **Statement**:
  - **Formulation A (Cyclic Walk on $\mathbb{Z}/N\mathbb{Z}$ / Reflecting Path on $[0, 2^N]$)**: Compute transition probabilities after $K$ steps via $P(x)^K \bmod (x^N - 1)$, or unfold a reflecting walk on $[0, 2^N]$ into a cyclic walk on $\mathbb{Z}_{2^{N+1}}$ evaluated at $2^{N+1}$-th roots of unity!
  - **Formulation B (Expected First Return / Step Weight — `fps_24_r`)**: Compute the expected value or survival probability of a random walk via renewal decomposition $F(x) = 1 - \frac{1}{G(x)}$ or cyclic DFT diagonalization.
- **Tags**: `[Cyclic-Convolution]`, `[Reflection-Unfolding]`, `[Renewal-GF]` | **Diagnostic Signal**: Walk on cycle $\mathbb{Z}/N\mathbb{Z} \implies P(x)^K \bmod (x^N - 1)$; reflecting barriers at $0$ and $2^N$ unfold to a periodic walk of period $2^{N+1}$!
- **3-Tier Hints**: (1) If the walk is on $\mathbb{Z}_{2^{N+1}}$ (or unfolded from $[0, 2^N]$), apply a length-$2^{N+1}$ NTT to diagonalize the step operator, raise point values to the $K$-th power, and INTT in $O(2^N \cdot N)$ time. (2) For general $N$, binary exponentiation modulo $x^N - 1$ folds terms $x^{i + N} \mapsto x^i$ in $O(N)$ after each NTT squaring. (3) For first-return probabilities, invert the return series $G(x)$ via polynomial inversion.
- **Solution Formula**: $P(x)^K \bmod (x^N - 1)$ (or $F(x) = 1 - G(x)^{-1} \bmod x^{N+1}$).

#### Problem 2A-48: Luogu P5293 — [HNOI2019] 白兔之舞 (`Mastery`)
- **URL**: `https://www.luogu.com.cn/problem/P5293` | **Constraints**: $n \le 3, L \le 10^8, k \le 65536$, prime $p \equiv 1 \pmod k$.
- **Statement**: On a directed graph with $n \le 3$ vertices and adjacency matrix $W$, for each $t = 0, \dots, k-1$, compute the sum of weights of walks of length $m \equiv t \pmod k$ (for $0 \le m \le L$) from $x$ to $y$, modulo $p$.
- **Tags**: `[Chirp-Z-Transform]`, `[Matrix-Roots-of-Unity]` | **Diagnostic Signal**: For each $j = 0, \dots, k-1$, let $c_j = \big[(I + \omega^j W)^L\big]_{x, y}$; then the answers $ans_t = \frac{1}{k} \sum_{j=0}^{k-1} \omega^{-jt} c_j$ form an IDFT of length $k$ over $\mathbb{F}_p$, evaluated via Bluestein's Chirp-$Z$ Transform + MTT!
- **3-Tier Hints**: (1) Find a primitive $k$-th root of unity $\omega = g^{(p-1)/k} \bmod p$. (2) Compute $c_j = \big[(I + \omega^j W)^L\big]_{x, y}$ for $j = 0, \dots, k-1$ via $k$ matrix binary exponentiations of size $3 \times 3$ in $O(n^3 k \log L)$ time. (3) Rewrite $\omega^{-jt} = \omega^{\binom{j-t}{2} - \binom{j}{2} - \binom{t}{2}}$ and compute the convolution modulo arbitrary $p$ using 3-prime NTT / MTT in $O(k \log k)$ time!
- **Solution Formula**: $\text{ans}_t = \frac{1}{k} \omega^{-\binom{t}{2}} \sum_{j=0}^{k-1} \left(c_j \omega^{-\binom{j}{2}}\right) \omega^{\binom{t - j}{2}} \bmod p$.

#### Problem 2A-49: Codeforces 1054H — Epic Convolution (`Mastery`)
- **URL**: `https://codeforces.com/problemset/problem/1054/H` | **Constraints**: $N, M \le 10^5$, $p = 490019$ ($p - 1 = 2 \times 491 \times 499$).
- **Statement**: Given $a_0, \dots, a_{N-1}$ and $b_0, \dots, b_{M-1}$, compute $\sum_{i=0}^{N-1} \sum_{j=0}^{M-1} a_i b_j c^{(i^2 j^3) \bmod (p-1)} \bmod 490019$.
- **Tags**: `[CRT-Mixed-Radix-Chirp-Z]`, `[2D-Bluestein]` | **Diagnostic Signal**: $p - 1 = 2 \times 491 \times 499$. By CRT and discrete logarithms in $\mathbb{Z}_{491}^\times \times \mathbb{Z}_{499}^\times$, the exponent $i^2 j^3 \bmod (p-1)$ becomes a 2D cyclic sum $u_1 + v_1 \pmod{490}$ and $u_2 + v_2 \pmod{498}$!
- **3-Tier Hints**: (1) Separate $i \equiv 0$ or $j \equiv 0$ mod $2, 491, 499$. For the coprime bulk, map $i^2 \bmod (p-1)$ and $j^3 \bmod (p-1)$ to CRT coordinates $(r_2, g_{491}^{x_1}, g_{499}^{x_2})$. (2) Alternatively, apply Bluestein's identity directly in the multiplicative group $\mathbb{F}_p^\times$: $c^{i^2 j^3} = c^{\binom{i^2 + j^3}{2} - \binom{i^2}{2} - \binom{j^3}{2}}$! (3) Group $a_i$ by $I = i^2 \bmod (p-1)$ and $b_j$ by $J = j^3 \bmod (p-1)$, then run one 1D convolution of length $2(p - 1) \approx 9.8 \times 10^5$!
- **Solution Formula**: $\sum_{I, J = 0}^{p-2} A_I B_J c^{-\binom{I}{2} - \binom{J}{2}} c^{\binom{I + J}{2}} \bmod 490019$ via one FFT/MTT of size $2^{20}$!

---

## 5. Wave 2B Problem Encyclopedia: Inclusion-Exclusion, Forbidden Patterns & PGFs (`cohort3_wave_2b_ie_pgf_zh_ja_audit.md`)

> **Full Reference**: See `fps_research/cohort3_wave_2b_ie_pgf_zh_ja_audit.md`, Section 6 (Lines 638–1450).

### Cluster A: Binomial Inversion & Subset Inclusion-Exclusion (Problems 2B-A1 to 2B-A14)

- **Problem 2B-A1: Codeforces 451E — Devu and Flowers** (`Stepping Stone`)
  - **URL**: `https://codeforces.com/problemset/problem/451/E` | **Constraints**: $N \le 20, S \le 10^{14}$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Count solutions to $x_1 + \dots + x_N = S$ with $0 \le x_i \le f_i$. Expand $[x^S] \frac{\prod_{i=1}^N (1 - x^{f_i+1})}{(1-x)^N} = \sum_{T \subseteq [N]} (-1)^{|T|} \binom{S - \sum_{i \in T}(f_i+1) + N - 1}{N - 1}$ in $O(2^N \cdot N)$ time.
- **Problem 2B-A2: AtCoder ABC 172 E — NEQ** (`Stepping Stone`)
  - **URL**: `https://atcoder.jp/contests/abc172/tasks/abc172_e` | **Constraints**: $N \le M \le 5 \times 10^5$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Count pairs of length-$N$ permutations from $\{1, \dots, M\}$ with $A_i \neq B_i$ for all $i$. By Binomial Inversion, $\binom{M}{N} N! \sum_{k=0}^N (-1)^k \binom{N}{k} \binom{M-k}{N-k} (N-k)!$.
- **Problem 2B-A3: AtCoder ABC 276 G — Count Sequences** (`Stepping Stone`): Cross-ref **Problem 1B-19**.
- **Problem 2B-A4: Codeforces 1548C — The Three Little Pigs** (`Stepping Stone`)
  - **URL**: `https://codeforces.com/problemset/problem/1548/C` | **Constraints**: $N \le 10^6, Q \le 2 \times 10^5$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Answer queries for $\sum_{i=1}^N \binom{3i}{x}$. Sum the geometric series in polynomial form: $\sum_{i=0}^N (1+x)^{3i} = \frac{(1+x)^{3N+3} - 1}{(1+x)^3 - 1} = \frac{(1+x)^{3N+3} - 1}{x^3 + 3x^2 + 3x}$, computed in $O(N)$ via synthetic division by $x^2 + 3x + 3$!
- **Problem 2B-A5: AtCoder ABC 266 G — Yet Another RGB Sequence** (`Stepping Stone`)
  - **URL**: `https://atcoder.jp/contests/abc266/tasks/abc266_g` | **Constraints**: $R, G, B, K \le 10^6$, $\bmod 998244353$.
  - **Statement & Formula**: Count strings with $R$ `'R'`s, $G$ `'G'`s, $B$ `'B'`s and exactly $K$ occurrences of `"RG"`. Fuse $K$ copies of `"RG"` into single blocks and forbid any remaining `'R'` from preceding `'G'`: $\frac{(R - K + G + B)!}{K! (R - K)! (G - K)! B!} \binom{G + B}{R - K}$.
- **Problem 2B-A6: AtCoder ARC 110 D — Binomial Coefficient is Fun** (`Stepping Stone`): Cross-ref **Problem 1B-16**.
- **Problem 2B-A7: Luogu P4491 — [HAOI2018] 染色** (`Intermediate`)
  - **URL**: `https://www.luogu.com.cn/problem/P4491` | **Constraints**: $N \le 10^7, M \le 10^5, S \le 150$, $\bmod 1004535809$.
  - **Statement & Formula**: Color $N$ positions with $M$ colors; if $k$ colors appear **exactly** $S$ times, score is $w_k$. Let $g_j = \binom{M}{j} \frac{N!}{(S!)^j (N - jS)!} (M - j)^{N - jS}$; then $f_k = \sum_{j=k}^{\min(M, N/S)} (-1)^{j-k} \binom{j}{k} g_j$ via one reverse NTT convolution in $O(M \log M)$ time.
- **Problem 2B-A8: Codeforces 1228E — Another Filling the Grid** (`Intermediate`)
  - **URL**: `https://codeforces.com/problemset/problem/1228/E` | **Constraints**: $N \le 250, K \le 10^9$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Fill an $N \times N$ grid with $\{1, \dots, K\}$ so every row and column has minimum $1$. By 2D Inclusion-Exclusion collapsed via the Binomial Theorem: $\sum_{i=0}^N (-1)^i \binom{N}{i} \big(K^{N-i}(K-1)^i - (K-1)^N\big)^N$.
- **Problem 2B-A9: Luogu P4859 — 已经没有什么好害怕的了** (`Intermediate`)
  - **URL**: `https://www.luogu.com.cn/problem/P4859` | **Constraints**: $N \le 2000$, $\bmod (10^9+9)$.
  - **Statement & Formula**: Pair $A_1, \dots, A_N$ and $B_1, \dots, B_N$ (all $2N$ values distinct) so that the number of pairs with $A_i > B_{\pi(i)}$ exceeds the number of pairs with $A_i < B_{\pi(i)}$ by $K$. First check parity: if $(N + K) \bmod 2 \neq 0$, the answer is $0$; otherwise we need $k = (N + K)/2$ pairs with $A_i > B_{\pi(i)}$. Sort both arrays, compute $dp[i][j]$ (choosing $j$ strict matches), set $g_j = dp[N][j] (N - j)!$, and apply Binomial Inversion $f_k = \sum_{j=k}^N (-1)^{j-k} \binom{j}{k} g_j$.
- **Problem 2B-A10: Luogu P5400 — [CTS2019] 随机立方体** (`Advanced`)
  - **URL**: `https://www.luogu.com.cn/problem/P5400` | **Constraints**: $n, m, l \le 5 \times 10^6$, $\bmod 998244353$.
  - **Statement & Formula**: Fill an $n \times m \times l$ cube with a random permutation of $1, \dots, nml$; find the probability of having at least $k$ local maxima (strictly greatest in their row, column, and pillar). Conditioning on $j$ local maxima gives $g_j = \binom{n}{j}\binom{m}{j}\binom{l}{j} (j!)^2 \prod_{r=1}^j \frac{1}{nml - (n-r)(m-r)(l-r)}$, inverted via $\sum_{j=k}^{\min(n,m,l)} (-1)^{j-k} \binom{j-1}{k-1} g_j$ in $O(\min(n,m,l))$ time using prefix-product batch inversion!
- **Problem 2B-A11: AtCoder AGC 005 F — Many Easy Problems** (`Intermediate`): Cross-ref **Problem 1A-12**.
- **Problem 2B-A12: Luogu P6596 — How Many of Them** (`Intermediate`)
  - **URL**: `https://www.luogu.com.cn/problem/P6596` | **Constraints**: $n \le 50, m \le \binom{n}{2}$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Count connected labeled graphs on $n$ vertices with at most $m$ bridges. Contract bridge-blocks into super-vertices via Prüfer/Cayley weight $n^{k-2} \prod s_i$ and apply Binomial Inversion on the number of bridges.
- **Problem 2B-A13: Codeforces 932E — Team Work** (`Intermediate`): Cross-ref **Problem 1B-10**.
- **Problem 2B-A14: Codeforces 1097G — Vladislav and a Great Legend** (`Advanced`)
  - **URL**: `https://codeforces.com/problemset/problem/1097/G` | **Constraints**: $N \le 10^5, K \le 200$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Sum $f(X)^K$ over all non-empty vertex subsets $X$ of a tree, where $f(X)$ is the number of edges in the minimal subtree spanning $X$. Expand $f(X)^K = \sum_{j=0}^K \left\{\begin{matrix} K \\ j \end{matrix}\right\} j! \binom{f(X)}{j}$ and count edge-subsets of size $j \le K$ on the tree via $O(NK)$ tree knapsack DP!

---

### Cluster B: Cluster Method (Goulden–Jackson) & Non-Adjacent Block IE (Problems 2B-B1 to 2B-B12)

- **Problem 2B-B1: Codeforces 1515E — Phoenix and Computers** (`Stepping Stone`): Cross-ref **Problem 5A-30**.
- **Problem 2B-B2: AtCoder AGC 005 D — ~K Perm Counting** (`Intermediate`)
  - **URL**: `https://atcoder.jp/contests/agc005/tasks/agc005_d` | **Constraints**: $N \le 2000$, $\bmod 924844033$.
  - **Statement & Formula**: Count permutations $\pi \in S_N$ with $|\pi(i) - i| \neq K$ for all $i$. Decompose the forbidden bipartite graph into $2K$ disjoint paths; the matching polynomial of a path of $m$ edges is $\sum_j \binom{m - j + 1}{j} x^j$. Multiply and apply inclusion-exclusion $\sum_{j=0}^N (-1)^j c_j (N - j)!$.
- **Problem 2B-B3: AtCoder ABC 279 G — At Most 2 Colors** (`Intermediate`)
  - **URL**: `https://atcoder.jp/contests/abc279/tasks/abc279_g` | **Constraints**: $N, K \le 10^6, C \le 10^9$, $\bmod 998244353$.
  - **Statement & Formula**: Color $N$ cells with $C$ colors so every window of length $K$ has at most $2$ distinct colors. Decompose by the distance to the last color change, yielding a linear recurrence / rational OGF solved in $O(N)$ time.
- **Problem 2B-B4: Codeforces 840C — On the Bench** (`Intermediate`): Equivalent to **Problem 2A-37** after grouping numbers by square-free core ($O(N^2)$ DP version for $N \le 300$).
- **Problem 2B-B5: Luogu P5339 — [TJOI2019] 唱、跳、rap和篮球** (`Intermediate`)
  - **URL**: `https://www.luogu.com.cn/problem/P5339` | **Constraints**: $N \le 1000, a,b,c,d \le 500$, $\bmod 998244353$.
  - **Statement & Formula**: Count length-$N$ sequences with at most $a, b, c, d$ copies of `'A'`, `'B'`, `'C'`, `'D'` containing no contiguous `"ABCD"`. Fuse $k$ copies of `"ABCD"` with sign $(-1)^k$: $\sum_{k=0}^{\lfloor N/4 \rfloor} (-1)^k \binom{N - 3k}{k} (N - 4k)! [x^{N-4k}] \prod_{r \in \{a,b,c,d\}} \left(\sum_{j=0}^{r - k} \frac{x^j}{j!}\right)$.
- **Problem 2B-B6: AtCoder ARC 115 E — LEQ and NEQ** (`Intermediate`)
  - **URL**: `https://atcoder.jp/contests/arc115/tasks/arc115_e` | **Constraints**: $N \le 5 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count arrays $1 \le X_i \le A_i$ with $X_i \neq X_{i+1}$. Fuse adjacent equal runs: a fused block $[l, r]$ contributes $(-1)^{r - l} \min_{k=l}^r A_k$. Maintain on a monotonic stack in $O(N)$ time (or CDQ on the Cartesian tree).
- **Problem 2B-B7: AtCoder ABC 260 Ex — Colorfulness** (`Advanced`): Cross-ref **Problem 5A-21**.
- **Problem 2B-B8: LibreOJ 3395 / AtCoder ARC 100 F — Colorful Sequences** (`Advanced`)
  - **URL**: `https://atcoder.jp/contests/arc100/tasks/arc100_d` | **Constraints**: $N \le 25000, K \le 400$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Sum over all length-$N$ sequences from $\{1, \dots, K\}$ of the number of occurrences of a given $M$-length sequence $A$, provided the sequence contains at least one rainbow window (all $K$ colors in $K$ consecutive positions). Count rainbow-free sequences via a $(K-1)$-state prefix-distinct DP!
- **Problem 2B-B9: Luogu P5206 — [WC2019] 数树 (Counting Trees)** (`Advanced`)
  - **URL**: `https://www.luogu.com.cn/problem/P5206` | **Constraints**: $N \le 10^5$, $\bmod 998244353$, $\text{op} \in \{0, 1, 2\}$.
  - **Statement & Formula**: Sum $y^{N - |E(T_1) \cap E(T_2)|}$ (handle $y = 1$ first as $1, N^{N-2}, N^{2N-4}$):
    - **Subtask $\text{op}=0$ (Fixed $T_1, T_2$)**: Count shared edges $|E(T_1) \cap E(T_2)|$ via hash table in $O(N)$ and output $y^{N - |E(T_1) \cap E(T_2)|}$.
    - **Subtask $\text{op}=1$ (Fixed $T_1$, sum over $T_2$)**: Replace $y^{-|E(T_1) \cap E(T_2)|} = \prod_{e \in T_1 \cap T_2} (1 + (y^{-1}-1))$. Choosing a subset $F \subseteq E(T_1)$ of $N - k$ edges splits $T_1$ into $k$ components of sizes $s_1, \dots, s_k$, which can be extended to $T_2$ in $N^{k-2} \prod_{i=1}^k s_i$ ways. Absorbing one factor of $N(y^{-1}-1) s_i$ into each component yields a linear $O(N)$ tree DP on $T_1$!
    - **Subtask $\text{op}=2$ (Sum over both $T_1, T_2$)**: A forest $F$ with $k$ components of sizes $s_1, \dots, s_k$ extends to both $T_1$ and $T_2$ in $\left(N^{k-2} \prod_{i=1}^k s_i\right)^2$ ways, and itself can be formed in $\prod_{i=1}^k s_i^{s_i - 2}$ ways. Thus each component of size $s$ has EGF weight $\frac{N^2(y^{-1}-1) s^s}{s!} x^s$, and $\text{Ans} = N! N^{-4} y^N [x^N] \exp\left(\sum_{s=1}^N \frac{N^2(y^{-1}-1) s^s}{s!} x^s\right)$ in $O(N \log N)$ time!
- **Problem 2B-B10: UOJ 424 / Luogu P5827** (`Mastery`): Cross-ref **Problem 5A-29** and **Problem 1A-27**.
- **Problem 2B-B11: Luogu P4747 — [CERC2017] Intrinsic Interval / Simple Permutations** (`Mastery`)
  - **URL**: `https://www.luogu.com.cn/problem/P4747` | **Constraints**: $N \le 10^5$.
  - **Statement & Formula**: Enumerate simple permutations (no non-trivial contiguous interval maps to a contiguous value range). By the Albert–Atkinson Substitution Decomposition, $P(x) = x + 2 \frac{P(x)^2}{1 - P(x)} + S(P(x))$, so the simple permutation OGF $S(u)$ is recovered from the compositional inverse $P^{\langle -1 \rangle}(u)$!
- **Problem 2B-B12: AtCoder ABC 281 Ex — Alchemy** (`Mastery`)
  - **URL**: `https://atcoder.jp/contests/abc281/tasks/abc281_h` | **Constraints**: $N \le 2 \times 10^5, A \le 10^{18}$, $\bmod 998244353$.
  - **Statement & Formula**: Count reaction trees of size $N$ with initial supply $A$. Reduces via inclusion-exclusion / EGF to $[x^N] \prod_{k=0}^{N-1} (1 + (A - k)x)$ or falling-factorial Lagrange Inversion, solved via divide-and-conquer NTT + Taylor shift in $O(N \log^2 N)$ time.

---

### Cluster C: Cyclic & Alternating Forbidden Patterns (Problems 2B-C1 to 2B-C6)

- **Problem 2B-C1: AtCoder AGC 058 D — Yet Another ABC String** (`Intermediate`): Cross-ref **Problem 3B-27** and **Problem 5A-31** (for avoiding $\{\texttt{ABC}, \texttt{BCA}, \texttt{CAB}\}$, a maximal periodic cluster of length $L \ge 3$ has net cluster weight $-1$ when $L \equiv 0 \pmod 3$ and $+1$ when $L \equiv 1 \pmod 3$, giving trivariate OGF $F(x_A, x_B, x_C) = \frac{1 + p}{1 + 4p - s}$ where $s = x_A + x_B + x_C, p = x_A x_B x_C$; for single-block fusion of `"ABC"`, $\frac{1 - p}{1 - s + 2p}$).
- **Problem 2B-C2: AtCoder ARC 093 F — Dark Horse** (`Intermediate`)
  - **URL**: `https://atcoder.jp/contests/arc093/tasks/arc093_d` | **Constraints**: $N \le 16, M \le 16$, $\bmod (10^9+7)$.
  - **Statement & Formula**: In a $2^N$-player knockout tournament, player $1$ beats everyone except $A_1, \dots, A_M$ (while for $i, j > 1$, the smaller index wins). Count initial bracket permutations where player $1$ wins. By Inclusion-Exclusion over which subset of the $N$ subtree brackets facing player $1$ have their minimum in $\{A_1, \dots, A_M\}$, solved via $O(M 2^N)$ bitmask DP.
- **Problem 2B-C3: AtCoder AGC 043 D — Merge Triplets** (`Intermediate`)
  - **URL**: `https://atcoder.jp/contests/agc043/tasks/agc043_d` | **Constraints**: $N \le 2000$, arbitrary prime $M$.
  - **Statement & Formula**: Count permutations of $1, \dots, 3N$ obtainable by merging $N$ blocks of size $3$. Decompose into prefix-maximum blocks of lengths $1, 2, 3$ with total count of $1$-blocks $\ge$ count of $2$-blocks: $[x^{3N} y^{\ge 0}] \exp\left(x y + \frac{x^2 y^{-1}}{2} + \frac{x^3}{3}\right)$ via $O(N^2)$ ODE recurrence!
- **Problem 2B-C4: Codeforces 1326F2 — Wise Men (Hard Version)** (`Advanced`)
  - **URL**: `https://codeforces.com/problemset/problem/1326/F2` | **Constraints**: $N \le 18$.
  - **Statement & Formula**: For a tournament graph on $N \le 18$ vertices, for every binary string $s \in \{0, 1\}^{N-1}$, count Hamiltonian paths matching adjacency pattern $s$. Relax the condition to $0 \to$ "any" and $1 \to$ "must have edge": then the count depends ONLY on the integer partition $\lambda \vdash N$ of the $1$-run lengths! Compute via subset OR-convolution over all $p(18) = 385$ partitions, then invert via SOS Möbius inversion!
- **Problem 2B-C5: Codeforces 1349F1/F2 — Slime and Sequences** (`Mastery`): Cross-ref **Problem 5A-27**.
- **Problem 2B-C6: AtCoder AGC 060 D — Same Descent Set** (`Mastery`)
  - **URL**: `https://atcoder.jp/contests/agc060/tasks/agc060_d` | **Constraints**: $N \le 2 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count pairs of permutations $(\pi, \sigma) \in S_N^2$ having the exact same descent set. By Inclusion-Exclusion over the $N-1$ positions where neither can have a descent, a run of length $L$ where both are increasing contributes $\left(\frac{x^L}{L!}\right)^2 = \frac{x^{2L}}{(L!)^2}$, reduced via semi-online CDQ NTT in $O(N \log^2 N)$ time!

---

### Cluster D: String Autocorrelation & Goulden–Jackson Cluster Method (Problems 2B-D1 to 2B-D7)

- **Problem 2B-D1: CSES 1112 (Required Substring) & yukicoder 1810** (`Stepping Stone`)
  - **Statement & Formula**: Count length-$N$ strings over an alphabet of size $\Sigma$ avoiding pattern $P$ of length $m$ with autocorrelation polynomial $C_P(x) = \sum_{L \in \text{Borders}(P)} x^{m-L}$. The OGF is $G(x) = \frac{C_P(x)}{(1 - \Sigma x) C_P(x) + x^m}$.
- **Problem 2B-D2: Codeforces Gym 102978 H — Harsh Comments** (`Intermediate`): Cross-ref **Problem 2A-12**.
- **Problem 2B-D3: Luogu P3311 ([SDOI2014] 数数) & CF Gym 102331 J** (`Advanced`)
  - **Statement & Formula**: Multi-pattern avoidance for $k$ reduced patterns $P_1, \dots, P_k$: define the $k \times k$ cross-correlation matrix $C_{i, j}(x) = \sum_{\text{suffix of } P_i = \text{prefix of } P_j \text{ of length } L} x^{|P_j| - L}$, solve $C(x)^T \mathbf{w}(x) = (-x^{|P_1|}, \dots, -x^{|P_k|})^T$ (or $C(x) \mathbf{w}(x) = -\mathbf{x}$ when indexing $C_{i,j}$ by suffix of $P_j$ matching prefix of $P_i$), and set $G(x) = \frac{1}{1 - \Sigma x - \sum_{i=1}^k w_i(x)}$.
- **Problem 2B-D4: Codeforces 755G — PolandBall and Many Other Balls** (`Advanced`): Cross-ref **Problem 5A-12**.
- **Problem 2B-D5: AtCoder AGC 013 E — Placing Squares** (`Intermediate`)
  - **URL**: `https://atcoder.jp/contests/agc013/tasks/agc013_e` | **Constraints**: $N \le 10^9, M \le 10^5$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Partition a board of length $N$ into contiguous segments avoiding split points $X_1, \dots, X_M$, weighting each segment of length $L$ by $L^2$. An unsplit step has OGF $\sum_{L \ge 1} L^2 x^L = \frac{x(1+x)}{(1-x)^3}$, equivalent to a $3 \times 3$ transfer matrix choosing $0, 1,$ or $2$ marked balls per segment!
- **Problem 2B-D6: Bivariate Exact-$K$ Pattern Counting Drill** (`Intermediate`)
  - **Statement & Formula**: Replace cluster weight $-1$ by $(u - 1)$ in the Goulden–Jackson Cluster Method to obtain the bivariate OGF $G(x, u) = \frac{C_P(x)}{(1 - \Sigma x) C_P(x) + (1 - u) x^m}$ marking exact occurrences of $P$ by $u^K$.
- **Problem 2B-D7: Cyclic Forbidden Substrings Drill** (`Advanced`)
  - **Statement & Formula**: For cyclic strings of length $N$ avoiding $P$, the trace of the Aho–Corasick transition matrix $\text{Tr}(A^N)$ equals $[x^N] \left(-x \frac{d}{dx} \ln Q(x)\right)$ where $Q(x) = \det(I - x A)$ is the Goulden–Jackson denominator!

---

### Cluster E: Probability Generating Functions (PGFs), Stopping Times & Min-Max Identity (Problems 2B-E1 to 2B-E17)

- **Problem 2B-E1: Codeforces 1392H — ZS Shuffles Cards** (`Intermediate`)
  - **URL**: `https://codeforces.com/problemset/problem/1392/H` | **Constraints**: $N, M \le 2 \times 10^6$, $\bmod 998244353$.
  - **Statement & Formula**: Deck has $N$ number cards and $M$ jokers; draw until a joker appears, then reshuffle; stop when all $N$ number cards have been seen. By linearity + memorylessness: $\mathbb{E}[\text{iterations}] = 1 + \sum_{k=1}^N \frac{M}{k}$, and $\mathbb{E}[\text{cards per iteration}] = 1 + \frac{N}{M + 1}$; multiply the two!
- **Problem 2B-E2: Luogu P4548 — [CTSC2006] 歌唱王国** (`Intermediate`): Cross-ref **Problem 1A-15**.
- **Problem 2B-E3: Luogu P3706 — [SDOI2017] 硬币游戏** (`Advanced`)
  - **URL**: `https://www.luogu.com.cn/problem/P3706` | **Constraints**: $N, M \le 300$, real Gaussian elimination.
  - **Statement & Formula**: Given $N$ patterns $S_1, \dots, S_N$ of length $M$, flip a coin until the first pattern $S_i$ appears; find each player's winning probability $F_i(1)$. Solve the $(N+1) \times (N+1)$ linear system $\sum_{j=1}^N C_{i, j}(1/2) F_j(1) = 2^{-M} G(1)$ and $\sum_{j=1}^N F_j(1) = 1$.
- **Problem 2B-E4: String Hitting Time Variance Drill** (`Intermediate`)
  - **Statement & Formula**: For a single pattern $S$ with border polynomial $P(x) = \sum_{L \in \text{Borders}(S)} m^{L} x^{n-L}$, $\mathbb{E}[T] = P(1)$ and $\text{Var}(T) = F''(1) + F'(1) - F'(1)^2 = P(1)^2 - (2n - 1) P(1) - 2 P'(1)$.
- **Problem 2B-E5: Luogu P4707 — 重返现世 (Min-Max Identity with $k$-th Max)** (`Advanced`)
  - **URL**: `https://www.luogu.com.cn/problem/P4707` | **Constraints**: $N \le 1000, M = \sum p_i \le 10^4, N - K \le 10$, $\bmod 998244353$.
  - **Statement & Formula**: Expected time to collect at least $K$ of $N$ items (equivalent to the $k = N - K + 1$-th maximum). Apply $\max_k(S) = \sum_{\emptyset \neq T \subseteq S} (-1)^{|T|-k} \binom{|T|-1}{k-1} \frac{M}{\sum_{i \in T} p_i}$ via a $O(N \cdot M \cdot (N-K))$ knapsack DP tracking $(j = \sum_{i \in T} p_i, r = |T| - k \in [0, 10])$.
- **Problem 2B-E6: AtCoder AGC 038 E — Gachapon** (`Advanced`)
  - **URL**: `https://atcoder.jp/contests/agc038/tasks/agc038_e` | **Constraints**: $N, \sum A_i, \sum B_i \le 400$, $\bmod 998244353$.
  - **Statement & Formula**: Expected draws until item $i$ is drawn at least $B_i$ times for all $i = 1, \dots, N$. By Min-Max / Poissonization EGF: $\sum_{\emptyset \neq T \subseteq [N]} (-1)^{|T|-1} \sum_{c_i < B_i (i \in T)} \frac{(\sum c_i)!}{\prod c_i!} \frac{S_{\text{all}}}{\sum_{i \in T} A_i} \prod_{i \in T} \left(\frac{A_i}{\sum_{j \in T} A_j}\right)^{c_i}$, solved via $O((\sum A_i)(\sum B_i)^2)$ DP.
- **Problem 2B-E7: UOJ 390 — [UNR #3] 百鸽笼** (`Advanced`)
  - **URL**: `https://uoj.ac/problem/390` | **Constraints**: $N \le 30, a_i \le 30$, $\bmod 998244353$.
  - **Statement & Formula**: $N$ pigeonholes have capacities $a_1, \dots, a_N$; balls are placed uniformly into non-full holes. Find the probability that hole $1$ fills last. Equivalent to the continuous-time Poisson arrival process where hole $1$ reaches $a_1$ after some subset $T$ of other holes have $< a_i$ balls: expand $\prod_{i \in T} \left(\sum_{j=0}^{a_i-1} \frac{x^j}{j!}\right)$.
- **Problem 2B-E8: AtCoder ABC 242 Ex — Random Painting** (`Intermediate`)
  - **URL**: `https://atcoder.jp/contests/abc242/tasks/abc242_h` | **Constraints**: $N \le 400, M \le 400$, $\bmod 998244353$.
  - **Statement & Formula**: Given $M$ intervals covering $[1, N]$, each step picks a random interval and paints it; find the expected steps to paint all $N$ cells. By Min-Max Identity on the $N$ cells, a subset $T \subseteq [1, N]$ has $\min(T) = \frac{M}{M - c(T)}$ where $c(T)$ is the number of intervals disjoint from $T$, computed via $O(N^2 M)$ interval DP.
- **Problem 2B-E9: UOJ 450 — [集训队作业2018] 复读机** (`Advanced`): Cross-ref **Problem 5A-28**.
- **Problem 2B-E10: Luogu P5326 — [ZJOI2019] 开关** (`Advanced`)
  - **URL**: `https://www.luogu.com.cn/problem/P5326` | **Constraints**: $N \le 100, \sum p_i \le 5 \times 10^4$, $\bmod 998244353$.
  - **Statement & Formula**: Switch $i$ is flipped with probability $p_i / S$; find the expected steps to reach target state $(s_1, \dots, s_N)$. Let $F_{\text{EGF}}(x) = \prod_{i=1}^N \frac{e^{p_i x/S} + (-1)^{s_i} e^{-p_i x/S}}{2}$ and $G_{\text{EGF}}(x) = \prod_{i=1}^N \frac{e^{p_i x/S} + e^{-p_i x/S}}{2}$. Convert to OGFs $F(z), G(z)$ via $\frac{1}{1 - \lambda z}$ and evaluate $\left(\frac{F}{G}\right)'(1)$ in $O(N \sum p_i)$ time!
- **Problem 2B-E11: AtCoder ARC 136 F — Flip Cells** (`Advanced`): Cross-ref **Problem 2A-6**.
- **Problem 2B-E12: AtCoder ABC 289 Ex — Trio** (`Advanced`)
  - **URL**: `https://atcoder.jp/contests/abc289/tasks/abc289_h` | **Constraints**: $A, B, C, T \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Three walkers start at $A, B, C$ on $\mathbb{Z}$ and step $\pm 1$ for $\le T$ steps; find the probability that they all meet at some point and time. By renewal decomposition (first meeting time $F(x)$ vs any meeting time $G(x)$ and return-to-origin $H(x)$): $F(x) = \frac{G(x)}{H(x)} \bmod x^{T+1}$, where $[x^t] G(x)$ and $[x^t] H(x)$ are sums of triple binomial coefficients computed via divide-and-conquer NTT!
- **Problem 2B-E13: Codeforces 1349D — Slime and Biscuits** (`Mastery`): Cross-ref **Problem 5A-25**.
- **Problem 2B-E14: Codeforces 1025G — Company Acquisitions** (`Advanced`)
  - **URL**: `https://codeforces.com/problemset/problem/1025/G` | **Constraints**: $N \le 500$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Each step, two random active companies fight; the loser becomes a vassal of the winner and all the loser's vassals become independent active companies. Potential function $f(x) = 2^x - 1$ decreases by $1$ in expectation at every step! Thus $\mathbb{E}[T] = (2^{N-1} - 1) - \sum_{i \text{ active}} (2^{c_i} - 1)$.
- **Problem 2B-E15: Codeforces 1479E — School Clubs** (`Mastery`): Cross-ref **Problem 5A-26**.
- **Problem 2B-E16: Luogu P5643 — [PKUWC2018] 随机游走** (`Advanced`)
  - **URL**: `https://www.luogu.com.cn/problem/P5643` | **Constraints**: $N \le 18, Q \le 5000$, $\bmod 998244353$.
  - **Statement & Formula**: Random walk on a tree of $N \le 18$ vertices starting at $x$; answer $Q$ queries for the expected time to visit all vertices in $S \subseteq V$. For each subset $T \subseteq V$, compute the first hitting time $\mathbb{E}[\min_{v \in T} \tau_v]$ in $O(N)$ via bottom-up tree linear elimination $E_u = A_u E_{fa(u)} + B_u$, then apply Min-Max Identity via SOS DP in $O(N 2^N)$ time!
- **Problem 2B-E17: Second-Moment Switch Walk Variance Drill** (`Mastery`)
  - **Statement & Formula**: For a switching walk $F(z) = G(z) / H(z)$ with $G(1) = H(1) = 0$ (simple pole at $z = 1$ in $G, H$), the second factorial moment $F''(1)$ is extracted from the Laurent expansion up to $(z - 1)^2$ of $G_{\text{reg}}(z)$ and $H_{\text{reg}}(z)$.

---

## 6. Wave 3A Problem Encyclopedia: Lagrange Inversion, Formal Residues, Tree & Graph Enumeration (`cohort3_wave_3a_lagrange_residues_trees_graphs.md`)

> **Full Reference**: See `fps_research/cohort3_wave_3a_lagrange_residues_trees_graphs.md`, Section 4 (Lines 662–1480).

### Iterations 21–22: Formal Calculus, Residues, Reflection Principle & Lagrange Inversion (Problems 3A-1 to 3A-12)

- **Problem 3A-1: Codeforces 1204E — Natasha, Sasha and the Prefix Sums** (`Stepping Stone`)
  - **URL**: `https://codeforces.com/problemset/problem/1204/E` | **Constraints**: $N, M \le 2000$, $\bmod 998244353$.
  - **Statement & Formula**: Sum the maximum prefix sum over all sequences of $N$ $+1$s and $M$ $-1$s. By the Reflection Principle, the number of paths reaching height $\ge k$ is $\binom{N+M}{N}$ if $k \le N - M$, and $\binom{N+M}{N - k}$ if $k > \max(0, N - M)$. Thus $\text{Ans} = \sum_{k=1}^N \min\left(\binom{N+M}{N}, \binom{N+M}{N-k}\right)$.
- **Problem 3A-2: AtCoder AGC 021 E — Ball Eat Chameleons** (`Stepping Stone`): Cross-ref **Problem 2A-11**.
- **Problem 3A-3: Codeforces 755G — PolandBall and Many Other Balls** (`Stepping Stone`): Cross-ref **Problem 5A-12** and **Problem 3B-26** (in Wave 3A, derived via the formal residue / Lagrange change of variables $y = \frac{u(1+u)}{2+u}$ turning $\sum_i \binom{n-i}{i} \binom{n-2i}{k-i} 2^{k-i}$ into $[u^k] (1+u)^{n-k} (2+u)^k$, or $x = \frac{u}{1+u}$ yielding $[u^k](1+u)^{n+1-k}(1+2u)^k$!).
- **Problem 3A-4: Codeforces 1967E2 — Again Counting Arrays (Hard Version)** (`Intermediate`)
  - **URL**: `https://codeforces.com/problemset/problem/1967/E2` | **Constraints**: $N, M \le 2 \times 10^6$, $\bmod 998244353$.
  - **Statement & Formula**: Count valid $\pm 1$ walks bounded between two parallel walls $y = -1$ and $y = M$. By the Two-Wall Reflection Principle (Kelvin's method of images), the inclusion-exclusion sum over alternating reflections across $y = -1$ and $y = M$ has stride $2(M + 1)$, taking $O\left(\frac{N}{M + 1}\right)$ operations!
- **Problem 3A-5: LibreOJ 6673 — EntropyIncreaser 与山林** (`Intermediate`)
  - **URL**: `https://loj.ac/p/6673` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Extract coefficients of an implicit tree/graph series satisfying $F(x) = x \phi(F(x))$ with degree/parity weights via Lagrange Inversion $[x^n] H(F(x)) = \frac{1}{n} [u^{n-1}] H'(u) \phi(u)^n$.
- **Problem 3A-6: Codeforces 1349F2 — Slime and Sequences (Hard)** (`Advanced`): Cross-ref **Problem 5A-27**.
- **Problem 3A-7: Luogu P7438 — [KrOI2021] Maple Leaf Story** (`Intermediate`)
  - **URL**: `https://www.luogu.com.cn/problem/P7438` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Solve a recurrence induced by substituting an algebraic/exponential series via the Formal Residue Change-of-Variables theorem $[x^{-1}] F(G(x)) G'(x) = [u^{-1}] F(u)$.
- **Problem 3A-8: AtCoder ABC 281 Ex — Alchemy** (`Advanced`): Cross-ref **Problem 2B-B12**.
- **Problem 3A-9: Codeforces 1810G — The Maximum Prefix** (`Intermediate`)
  - **URL**: `https://codeforces.com/problemset/problem/1810/G` | **Constraints**: $N \le 5000$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Given step probabilities $p_i$ for $+1$ and $1 - p_i$ for $-1$ at step $i$, compute the expected score $h(\max_{0 \le r \le k} S_r)$ for every prefix length $k = 1, \dots, N$. Reverse the walk direction (process from right to left): $dp[j] \gets p_i dp[j + 1] + (1 - p_i) dp[\max(0, j - 1)]$, or apply the Kernel Method when $p_i$ is homogeneous!
- **Problem 3A-10: UOJ 450 / Luogu P5401 — [CTS2019] 珍珠** (`Intermediate`): Cross-ref **Problem 1A-28**.
- **Problem 3A-11: QOJ 4815 — Shift of Sampling Points / Rational Diagonal** (`Advanced`): Cross-ref **Problem 4A-P20**.
- **Problem 3A-12: LibreOJ 6728 — Power Projection / Kinoshita–Li** (`Mastery`): Cross-ref **Problem 4A-P26**.

---

### Iteration 23: Catalan Variants, Narayana, Schröder & Implicit Tree Functional Equations (Problems 3A-13 to 3A-20)

- **Problem 3A-13: Luogu P3978 — [TJOI2015] 概率论** (`Stepping Stone`)
  - **URL**: `https://www.luogu.com.cn/problem/P3978` | **Constraints**: $N \le 10^9$, floating-point.
  - **Statement & Formula**: Expected number of leaves in a uniformly random $N$-node binary tree. Mark leaves by $u$ in $T(x, u) = 1 + x(u - 1) + x T(x, u)^2$. Differentiating at $u = 1$ gives $\frac{\partial T}{\partial u}\big|_{u=1} = \frac{x}{\sqrt{1 - 4x}} = \sum_{n \ge 1} \binom{2n-2}{n-1} x^n$! Dividing by $C_n = \frac{1}{n+1} \binom{2n}{n}$ yields $\frac{N(N + 1)}{2(2N - 1)}$ in $O(1)$ time!
- **Problem 3A-14: Codeforces 438E — The Child and Binary Tree** (`Stepping Stone`): Cross-ref **Problem 1A-10**.
- **Problem 3A-15: AtCoder `fps_24_o` — Rooted Tree** (`Stepping Stone`): Cross-ref **Problem 1A-21**.
- **Problem 3A-16: AtCoder Toyota 2023 Spring Final E — Tree Constraint** (`Intermediate`)
  - **Statement & Formula**: Count rooted trees with degree parity/interval constraints via Lagrange Inversion $[x^n] T(x) = \frac{1}{n} [u^{n-1}] \phi(u)^n$.
- **Problem 3A-17: Codeforces 1528F — AmShZ Farm** (`Intermediate`)
  - **URL**: `https://codeforces.com/problemset/problem/1528/F` | **Constraints**: $N \le 10^9, K \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Sum $\sum_{a_1, \dots, a_N} \sum_{i=1}^N c_i^K$ over all valid parking functions of length $N$, where $c_i$ is the frequency of $i$. By Pollak's circular shift argument on $\mathbb{Z}/(N+1)\mathbb{Z}$, a random sequence is a parking function with probability $\frac{1}{N+1}$ independent of its frequency multiset! Thus $\text{Ans} = \frac{N}{N + 1} \sum_{j=1}^{\min(N, K)} \left\{\begin{matrix} K \\ j \end{matrix}\right\} N^{\underline{j}} (N + 1)^{N - j}$.
- **Problem 3A-18: AtCoder ABC 222 H — Beautiful Binary Tree** (`Intermediate`): Cross-ref **Problem 1A-13**.
- **Problem 3A-19: UOJ 424 — count** (`Advanced`): Cross-ref **Problem 5A-29**.
- **Problem 3A-20: AtCoder AGC 070 C — No Clar** (`Mastery`)
  - **URL**: `https://atcoder.jp/contests/agc070/tasks/agc070_c` | **Constraints**: $N \le 10^7$, $\bmod 998244353$.
  - **Statement & Formula**: Count non-crossing / ballot game configurations via bivariate Lagrange Inversion and $O(N)$ D-finite hypergeometric extraction.

---

### Iteration 24: Prüfer Sequences, Cayley Forests, Unlabeled Trees & Cactus Enumeration (Problems 3A-21 to 3A-29)

- **Problem 3A-21: Codeforces 156D — Clues** (`Stepping Stone`)
  - **URL**: `https://codeforces.com/problemset/problem/156/D` | **Constraints**: $N \le 10^5$, arbitrary modulus $P$.
  - **Statement & Formula**: Given a graph with $k$ connected components of sizes $s_1, \dots, s_k$, count ways to add $k - 1$ edges to make it connected. If $k = 1$, answer is $1 \bmod P$; if $k \ge 2$, by generalized Cayley's formula (via Prüfer sequences or EGF $\exp$), the answer is $N^{k-2} \prod_{i=1}^k s_i \bmod P$.
- **Problem 3A-22: Luogu P5219 — 无聊的水题 I (Max-Degree Trees)** (`Intermediate`)
  - **URL**: `https://www.luogu.com.cn/problem/P5219` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count labeled trees on $N$ vertices with maximum degree exactly $M$. By Prüfer's bijection, trees with maximum degree $\le D$ have count $(N-2)! [x^{N-2}] \left(\sum_{j=0}^{D-1} \frac{x^j}{j!}\right)^N$. Subtract the answers for $D = M$ and $D = M - 1$ using `pow` in $O(N \log N)$ time!
- **Problem 3A-23: LibreOJ 6728 — U 群把妹王** (`Advanced`): Cross-ref **Problem 4A-P27**.
- **Problem 3A-24: Codeforces 891E — Lust** (`Intermediate`): Cross-ref **Problem 1A-16**.
- **Problem 3A-25: AtCoder ABC 303 Ex — Constrained Tree Degree** (`Intermediate`): Identical to **Problem 1A-21** on unrooted trees via Prüfer EGF $(N-2)! [x^{N-2}] \left(\sum_{d \in S} \frac{x^{d-1}}{(d-1)!}\right)^N$.
- **Problem 3A-26: LibreOJ 6538 — 烷基计数 加强版** (`Intermediate`): Cross-ref **Problem 1A-14** and **Problem 5A-23**.
- **Problem 3A-27: LibreOJ 6569 — 仙人掌计数 (Labeled Cactus Enumeration)** (`Advanced`)
  - **URL**: `https://loj.ac/p/6569` | **Constraints**: $N \le 1.3 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count connected labeled cactus graphs on $n$ vertices for $1 \le n \le N$. Solve $T(x) = x \exp\left(\frac{2T(x) - T(x)^2}{2(1 - T(x))}\right)$ via Newton's method: $T_{k+1} = T_k - \frac{2(T_k - x E_k)(1 - T_k)^2}{2(1 - T_k)^2 - T_k(2 - 2T_k + T_k^2)}$, then divide $[x^n] T(x)$ by $n$ (unrooting).
- **Problem 3A-28: Luogu P5434 — 有标号荒漠计数** (`Advanced`): Cross-ref **Problem 1A-27**.
- **Problem 3A-29: Luogu P6597 & P6598 — 烯烃计数 & 烷烃计数 (Alkenes & Alkanes)** (`Mastery`)
  - **URL**: `https://www.luogu.com.cn/problem/P6597` & `https://www.luogu.com.cn/problem/P6598` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count unlabeled unrooted trees with maximum degree $\le 4$ (alkanes $C_n H_{2n+2}$, **P6598**) and unrooted carbon skeletons with a single double bond (alkenes $C_n H_{2n}$, **P6597**). First compute rooted ternary trees $A(x)$ ($\deg \le 3$, **Problem 1A-14**). Then a vertex-rooted degree-$\le 4$ tree has OGF $P(x) = x Z(S_4; A(x), A(x^2), A(x^3), A(x^4)) = \frac{x}{24}\big(A(x)^4 + 6 A(x)^2 A(x^2) + 3 A(x^2)^2 + 8 A(x) A(x^3) + 6 A(x^4)\big)$, an unordered edge-rooted tree has $Q(x) = Z(S_2; A(x) - 1) = \frac{1}{2}\big((A(x)-1)^2 + A(x^2) - 1\big)$, and a symmetric edge has $S(x) = A(x^2) - 1$. By Otter's Dissymmetry Theorem, $\text{Alkanes}(x) = P(x) - Q(x) + S(x)$!

---

### Iteration 25: Graph Enumeration — Connected, Bipartite, Eulerian, DAGs, Strongly Connected & Biconnected (Problems 3A-30 to 3A-40)

- **Problem 3A-30: 51Nod 1728 — 不动点** (`Stepping Stone`): Cross-ref **Problem 1A-17**.
- **Problem 3A-31: Luogu P4841 — 城市规划** (`Stepping Stone`): Cross-ref **Problem 1A-9a**.
- **Problem 3A-32: LibreOJ 6539 — 烷基计数 / 二分图计数 (Bipartite Graphs)** (`Intermediate`): Cross-ref **Problem 1A-9b** and **Problem 1A-20** ($\exp\big(\frac{1}{2} \ln G_{\text{2-col}}(x)\big) = \sqrt{G_{\text{2-col}}(x)}$).
- **Problem 3A-33: Luogu P7364 — 有标号欧拉图计数 (Labeled Eulerian Graphs)** (`Intermediate`)
  - **URL**: `https://www.luogu.com.cn/problem/P7364` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: A labeled graph on $n$ vertices has all even degrees in $2^{\binom{n-1}{2}}$ ways (since deleting vertex $1$ leaves an arbitrary graph on $n-1$ vertices whose parities uniquely force the edges incident to $1$). Take $\ln\left(\sum_{n=0}^N \frac{2^{\binom{n-1}{2}}}{n!} x^n\right)$ for connected Eulerian graphs!
- **Problem 3A-34: Luogu P6295 — 有标号 DAG 计数 (Labeled DAG Enumeration)** (`Intermediate`)
  - **URL**: `https://www.luogu.com.cn/problem/P6295` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count labeled Directed Acyclic Graphs (DAGs) on $n$ vertices (and connected DAGs via $\ln$). By Robinson–Stanley inclusion-exclusion on the set of sources (vertices of in-degree $0$), $D_n = \sum_{k=1}^n (-1)^{k-1} \binom{n}{k} 2^{k(n-k)} D_{n-k}$. Using $k(n-k) = \binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}$, define $\widehat{D}(x) = \sum_{n=0}^N \frac{D_n}{n! 2^{\binom{n}{2}}} x^n$ and $\phi(x) = \sum_{k=0}^N \frac{(-1)^k}{k! 2^{\binom{k}{2}}} x^k$; then $\widehat{D}(x) = \phi(x)^{-1} \bmod x^{N+1}$ via a SINGLE polynomial inversion!
- **Problem 3A-35: Luogu P6596 — How Many of Them** (`Intermediate`): Cross-ref **Problem 2B-A12**.
- **Problem 3A-36: Codeforces 917D — Stranger Trees** (`Intermediate`)
  - **URL**: `https://codeforces.com/problemset/problem/917/D` | **Constraints**: $N \le 100$ (or $10^5$), $\bmod (10^9+7)$.
  - **Statement & Formula**: Given a tree $T$ on $N$ vertices, for each $k = 0, \dots, N-1$, count spanning trees of $K_N$ sharing exactly $k$ edges with $T$. Cross-ref **Problem 2B-B9** ($\text{op}=1$): replace shared edges by weight $y$, contract $(y - 1)$-components of sizes $s_1, \dots, s_c$ via an $O(N^2)$ tree DP tracking component size and $(y-1)$-count, and multiply by $N^{c-2} \prod s_i$.
- **Problem 3A-37: Strongly Connected Labeled Digraphs (CF 1556F / QOJ Variant)** (`Advanced`)
  - **Statement & Formula**: Every digraph condenses into a DAG of Strongly Connected Components (SCCs), where the source SCCs have no incoming edges from the rest. By the Robinson–Stanley inversion lifted to SCCs, if $S(x) = \sum_{n \ge 1} \frac{s_n}{n! 2^{\binom{n}{2}}} x^n$ is the Chirp-scaled EGF of SCCs and $G(x) = \sum_{n \ge 0} \frac{2^{\binom{n}{2}}}{n!} x^n$, then $1 - \exp(-S(x))$ (in the Chirp-convolved ring) inverts $G(x)$, solved via CDQ NTT in $O(N \log^2 N)$ time!
- **Problem 3A-38: AtCoder ABC 284 Ex — Count Unlabeled Graphs** (`Mastery`): Identical to **Problem 2A-30** with connected/chromatic extensions.
- **Problem 3A-39: UOJ 498 — 新年的追逐 (Weichsel's Tensor Product of Graphs & Bipartite EGF)** (`Mastery`)
  - **URL**: `https://uoj.ac/problem/498` | **Constraints**: $k \le 10^5, n_i \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Given $k$ vertex counts $n_1, \dots, n_k$, sum the number of connected components in the tensor product $G_1 \times G_2 \times \dots \times G_k$ over all $\prod_{i=1}^k 2^{\binom{n_i}{2}}$ tuples of labeled graphs $(G_1, \dots, G_k)$. By **Weichsel's Theorem**, if we decompose each $G_i$ into connected components, a tuple of connected components $(C_1, \dots, C_k)$ has $|V(C_i)| = 1$ (isolated vertex) in some factor $\implies \prod |V(C_i)|$ isolated vertices in the product; otherwise (all $|V(C_i)| \ge 2$), $C_1 \times \dots \times C_k$ splits into **$2^{k-1}$ connected components if all $k$ components $C_i$ are bipartite**, and **$1$ connected component if at least one $C_i$ is non-bipartite**! Thus we compute the EGFs of connected graphs $C(x) = \ln G(x)$ and connected bipartite graphs $B(x) = \frac{1}{2} \ln G_{\text{2-col}}(x)$ (**Problem 1A-20**), extract for each $n_i$ the total number of non-isolated connected components $A_i = n_i! [x^{n_i}] (C(x) - x) G(x)$ and non-isolated bipartite components $D_i = n_i! [x^{n_i}] (B(x) - x) G(x)$, and combine across the $k$ factors via $\prod A_i + (2^{k-1} - 1) \prod D_i$ (plus the isolated-vertex inclusion-exclusion contribution) in $O(N \log N)$ time!
- **Problem 3A-40: Luogu P5827 (点双连通图计数) & Luogu P5828 (边双连通图计数) & `fps_24_w`** (`Mastery`)
  - **URL**: `https://www.luogu.com.cn/problem/P5827` & `https://www.luogu.com.cn/problem/P5828` | **Constraints**: $N \le 10^5$ (single $N$), $\bmod 998244353$.
  - **Statement & Formula**:
    - **2-Edge-Connected Graphs (Luogu P5828)**: Let $C(x) = \ln G(x)$ be connected graphs, $R(x) = x C'(x)$ be rooted connected graphs, and $B_{\text{2e}}(x)$ be rooted 2-edge-connected graphs. Removing the root's 2-edge-connected component of size $k$ leaves $k$ independent attachments of $R(x)$, so $R(x) = B_{\text{2e}}\big(x e^{R(x)}\big)$! Setting $u = x e^{R(x)}$, we have $B_{\text{2e}}(u) = R(x(u))$, so by Lagrange Inversion in **$O(N \log N)$** time:
      $$[u^N] B_{\text{2e}}(u) = \frac{1}{N} [x^{N-1}] R'(x) e^{-N R(x)} \quad \Longleftrightarrow \quad e_{2, N} = -\frac{(N - 1)!}{N} [x^N] \exp\big(-N x C'(x)\big)$$
    - **2-Vertex-Connected / Biconnected Graphs (Luogu P5827)**: Let $R(x) = x C'(x)$ be rooted connected graphs and $B(y)$ be unrooted biconnected graphs ($y = R(x)$). Removing the root splits its incident biconnected blocks, each of size $k+1$ having $k$ non-root vertices that each root a connected graph $R(x)$: thus $R(x) = x \exp\big(B'(R(x))\big) \implies \ln\frac{R(x)}{x} = B'(R(x))$. Let $H(x) = \ln\frac{R(x)}{x}$; then $B'(y) = H(R^{\langle -1 \rangle}(y))$, so by Lagrange Inversion (both the $H'(x)$ form and the log-free $C'(x)$ form for $N \ge 3$):
      $$N [y^{N-1}] B'(y) = (N - 1) [x^{N-1}] H'(x) \left(\frac{x}{R(x)}\right)^{N-1} \quad \Longleftrightarrow \quad b_N = -(N - 2)! [x^{N-1}] \big(C'(x)^{-(N-1)}\big) \quad (N \ge 3)$$
      giving $b_N = N! [y^N] B(y)$ for a single $N$ in **$O(N \log N)$** time!

---

## 7. Wave 3B Problem Encyclopedia: Implicit Functional Equations, Newton's Method & Multicolor Trees (`cohort3_wave_3b_implicit_zh_ja_audit.md`)

> **Full Reference**: See `fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md`, Section 8 (Lines 774–1526).

### Tier 1: Stepping Stone (`Stepping Stone` — Problems 3B-1 to 3B-5)

- **Problem 3B-1: AtCoder `fps_24_f` — Colored Tree**
  - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_f` | **Constraints**: $N \le 2.5 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**:
    - **Formulation A (2-Colored Rooted Tree Implicit System)**: Count 2-colored labeled rooted trees where red nodes have only blue children and blue nodes have at most $K$ red children. The coupled system $R(x) = x e^{B(x)}, B(x) = x \sum_{j=0}^K \frac{R(x)^j}{j!}$ reduces by substitution to $R(x) = x \exp\left(x \sum_{j=0}^K \frac{R(x)^j}{j!}\right)$, solved via Newton's method in $O(N \log N)$ time.
    - **Formulation B (Odd/Even Degree Red-Blue Unrooted Tree via Prüfer Sequences)**: Count 2-colored labeled unrooted trees on $N$ vertices with $R$ red vertices (every red vertex has **odd** degree, so even Prüfer multiplicity) and $N - R$ blue vertices (every blue vertex has **even** degree, so odd Prüfer multiplicity). By Prüfer's bijection, the EGF per red vertex is $\cosh(x) = \frac{e^x + e^{-x}}{2}$ and per blue vertex is $\sinh(x) = \frac{e^x - e^{-x}}{2}$, yielding $(N - 2)! [x^{N-2}] \cosh(x)^R \sinh(x)^{N-R}$ in $O(N)$ time via binomial expansion!
- **Problem 3B-2: AtCoder `fps_24_o` — Rooted Trees**: Cross-ref **Problem 1A-21**.
- **Problem 3B-3: Codeforces 917D — Stranger Trees**: Cross-ref **Problem 3A-36**.
- **Problem 3B-4: Luogu P7439 — [KrOI2021] Krzyżówka**
  - **URL**: `https://www.luogu.com.cn/problem/P7439` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Solve an implicit functional equation $F(x) = x \phi(F(x))$ via univariate Newton iteration $F_{k+1} = F_k - \frac{F_k - x \phi(F_k)}{1 - x \phi'(F_k)}$.
- **Problem 3B-5: yukicoder 3029 — 2-Colored Implicit System**
  - **URL**: `https://yukicoder.me/problems/no/3029` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Solve a coupled $2 \times 2$ implicit system $\Phi_1(F, G) = 0, \Phi_2(F, G) = 0$ via $2 \times 2$ Jacobian matrix inversion $J^{-1} = \frac{1}{\det J} \begin{pmatrix} \partial_G \Phi_2 & -\partial_G \Phi_1 \\ -\partial_F \Phi_2 & \partial_F \Phi_1 \end{pmatrix}$ in Newton's method.

---

### Tier 2: Intermediate (`Intermediate` — Problems 3B-6 to 3B-12)

- **Problem 3B-6: AtCoder ABC 222 H — Beautiful Binary Tree**: Cross-ref **Problem 1A-13**.
- **Problem 3B-7: Luogu P5434 — 有标号荒漠计数**: Cross-ref **Problem 1A-27**.
- **Problem 3B-8: Luogu P6633 / LOJ 3299 — [ZJOI2020] 抽卡**
  - **URL**: `https://www.luogu.com.cn/problem/P6633` | **Constraints**: $N \le 2 \times 10^5, K \le N$, $\bmod 998244353$.
  - **Statement & Formula**: Given a set $S$ of $N$ card numbers, draw with replacement until $K$ consecutive numbers appear. Decompose $S$ into maximal contiguous intervals of lengths $L_1, \dots, L_c$: inside an interval of length $L$, the EGF/OGF of subsets containing no $K$ consecutive elements is extracted via a $2 \times 2$ divide-and-conquer NTT, multiplied across intervals, and integrated against the Coupon Collector denominator!
- **Problem 3B-9a (`#179`, `Ch 10 [Adv-1]`): Luogu P5597 — 【XR-4】复读 (Tree Automaton Minimization & Implicit Newton)**
  - **URL**: `https://www.luogu.com.cn/problem/P5597` | **Constraints**: $N \le 2000$ (tree states), $\bmod 998244353$.
  - **Statement & Formula**: Given a rooted ternary tree $T$, count infinite periodic extensions / subtree isomorphism classes via bottom-up tree DFA minimization followed by coupled implicit Newton iteration (`Wave 3B #18`).
- **Problem 3B-9b (`#219`, `Ch 17 [Int-2]`): LibreOJ 3398 — 带加强和多项木 (Multivariate Implicit Tree System & Good–Lagrange)**
  - **URL**: `https://loj.ac/p/3398` | **Constraints**: Multi-type tree degree bounds, $\bmod 998244353$.
  - **Statement & Formula**: Count multi-type labeled/unlabeled trees via a multivariate implicit functional system $u_i = x_i \phi_i(\mathbf{u})$ and extract coefficients via the Good–Lagrange Jacobian determinant $\det(I - J_G(\mathbf{u}))$ (`Wave 3B #9`, `Wave 4B #32`).
- **Problem 3B-10: AtCoder ABC 345 G — Sugoroku 5**
  - **URL**: `https://atcoder.jp/contests/abc345/tasks/abc345_g` | **Constraints**: $N, K \le 2 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Roll a die on $\{1, \dots, K\}$ until reaching $\ge N$. For each $i = 1, \dots, N$, find the probability of finishing in $\le i$ steps. Let $P(x) = \frac{1}{K} \sum_{j=1}^K x^j = \frac{x(1 - x^K)}{K(1 - x)}$. We need $[x^n] P(x)^i$ summed over $n < N$. Equivalently, compute the polynomial composition $F(P(x)) \bmod x^N$ via Kinoshita–Li or divide-and-conquer on $(1 - x)^{-i}$!
- **Problem 3B-11: Luogu P5900 — 无标号无根树计数**: Cross-ref **Problem 1A-29**.
- **Problem 3B-12: LibreOJ 6538 / Luogu P6598 — 烷烃计数**: Cross-ref **Problem 3A-29**.

---

### Tier 3: Advanced (`Advanced` — Problems 3B-13 to 3B-20)

- **Problem 3B-13: Codeforces 438E — The Child and Binary Tree (Newton Perspective)**: Cross-ref **Problem 1A-10** ($F_{k+1} = F_k - \frac{D F_k^2 - F_k + 1}{2 D F_k - 1}$).
- **Problem 3B-14: UOJ 50 — 链式反应**: Cross-ref **Problem 1A-18**.
- **Problem 3B-15: Codeforces 1349F1/F2 — Slime and Sequences**: Cross-ref **Problem 5A-27**.
- **Problem 3B-16: UOJ 424 / LOJ 2555 — count**: Cross-ref **Problem 5A-29**.
- **Problem 3B-17: AtCoder `fps_24_s` — Game**: Cross-ref **Problem 1A-30**.
- **Problem 3B-18: LibreOJ 6728 — U 群把妹王**: Cross-ref **Problem 4A-P27**.
- **Problem 3B-19: AtCoder ARC 137 F — Overlaps**
  - **URL**: `https://atcoder.jp/contests/arc137/tasks/arc137_f` | **Constraints**: $N, K \le 2 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Place $N$ random intervals in $[0, 1]$ and filter by maximum depth / overlap structure; reduces to solving an implicit algebraic/differential equation on chord diagrams via Newton's method + Lagrange Inversion in $O(N \log N)$ time.
- **Problem 3B-20: Codeforces 1687F — Koishi's Unconscious Permutation**
  - **URL**: `https://codeforces.com/problemset/problem/1687/F` | **Constraints**: $N \le 2 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count permutations by cycle-minima and ascent counts simultaneously; reduces via Foata's Fundamental Transformation and Eulerian generating functions to a bivariate implicit equation solved via Lagrange Inversion and double-pole singularity subtraction (analogous to `CF 1349F2`).

---

### Tier 4: Mastery (`Mastery` — Problems 3B-21 to 3B-27)

- **Problem 3B-21: Luogu P8555 — 密码学第三次小作业**
  - **URL**: `https://www.luogu.com.cn/problem/P8555` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Solve a coupled higher-order differential-algebraic system by reducing it to a first-order vector ODE $\mathbf{F}' = \mathbf{\Phi}(x, \mathbf{F})$ and applying Newton's method with $2 \times 2$ variation-of-parameters integrating factors.
- **Problem 3B-22: Luogu P7592 — 2021 CoE-II E: 数树**
  - **URL**: `https://www.luogu.com.cn/problem/P7592` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Multi-colored implicit tree enumeration solved via $k \times k$ multivariate Newton Iteration $\mathbf{F}_{m+1} = \mathbf{F}_m - (D\mathbf{\Phi}(\mathbf{F}_m))^{-1} \mathbf{\Phi}(\mathbf{F}_m)$.
- **Problem 3B-23: AtCoder `fps_24_x` — Functional Square Root**: Cross-ref **Problem 1A-31**.
- **Problem 3B-24: Codeforces 1930I — Counting Is Fun**
  - **URL**: `https://codeforces.com/problemset/problem/1930/I` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count binary strings coverable by majority blocks; reduces via inclusion-exclusion on canonical runs to a coupled implicit functional equation solved via Newton's method / Lagrange Inversion.
- **Problem 3B-25: Luogu P3684 / BZOJ 3684 — 大朋友和多叉树 (Multi-Branch Ordered Trees)**
  - **URL**: `https://www.luogu.com.cn/problem/P3684` | **Constraints**: $N \le 10^5, |S| \le 10^5$, $\bmod 950009857$.
  - **Statement & Formula**: Count ordered rooted trees with $N$ leaves where every internal node has out-degree in $S \subseteq \{2, \dots, N\}$. The leaf OGF satisfies $T(x) = x + \sum_{d \in S} T(x)^d \implies x = \frac{T(x)}{1 - \sum_{d \in S} T(x)^{d-1}}$. By Lagrange Inversion, $[x^N] T(x) = \frac{1}{N} [u^{N-1}] \left(1 - \sum_{d \in S} u^{d-1}\right)^{-N}$, computed via a single polynomial `ln` + `exp` (`pow`) in $O(N \log N)$ time!
- **Problem 3B-26: Codeforces 755G — PolandBall and Many Other Balls (Formal Laurent Residue Change-of-Variables Perspective)**: Cross-ref **Problem 3A-3** and **Problem 5A-12** ($[u^m](1+u)^{n-m}(2+u)^m$ via $y = \frac{u(1+u)}{2+u}$).
- **Problem 3B-27: AtCoder AGC 058 D — Yet Another ABC String (3-Letter Forbidden Cyclic Pattern)**: Cross-ref **Problem 5A-31** (trivariate generating function $\frac{1+p}{1+4p-s}$ where $s = x+y+z, p = xyz$).

---

## 8. Wave 4A Problem Encyclopedia: Multivariate FPS, Bostan–Mori & Rational Diagonals (`cohort3_wave_4a_multivariate_bostan_mori_diag.md`)

> **Full Reference**: See `fps_research/cohort3_wave_4a_multivariate_bostan_mori_diag.md`, Section 6 (Lines 707–1358).

### Tier 1: Stepping Stone (`Stepping Stone` — Problems 4A-P1 to 4A-P7)

- **Problem 4A-P1: AtCoder Typical90 #065 — RGB Balls 2**
  - **URL**: `https://atcoder.jp/contests/typical90/tasks/typical90_bm` | **Constraints**: $R, G, B, K \le 2 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Choose $K$ balls from $R$ red, $G$ green, $B$ blue balls subject to $r + g \le X, g + b \le Y, b + r \le Z$. Rewrite as lower bounds $b \ge K - X, r \ge K - Y, g \ge K - Z$. Truncate the polynomials $\sum_{r \ge K-Y} \binom{R}{r} x^r$ and $\sum_{g \ge K-Z} \binom{G}{g} x^g$, multiply via one NTT, and dot-product with $\binom{B}{K - (r+g)}$.
- **Problem 4A-P2: AtCoder ABC 276 G — Count Sequences**: Cross-ref **Problem 1B-19**.
- **Problem 4A-P3: AtCoder ABC 300 Ex — Fibonacci: Revisited**: Cross-ref **Problem 2A-4**.
- **Problem 4A-P4: Codeforces 1117D — Magic Gems**
  - **URL**: `https://codeforces.com/problemset/problem/1117/D` | **Constraints**: $N \le 10^{18}, M \le 100$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Compute $[x^N] \frac{1}{1 - x - x^M} \bmod (10^9+7)$ via Bostan–Mori or binary exponentiation $x^N \bmod (x^M - x^{M-1} - 1)$ in $O(M \log M \log N)$ time.
- **Problem 4A-P5: AtCoder ABC 240 G — Teleporting Takahashi**: Cross-ref **Problem 2A-33**.
- **Problem 4A-P6: Codeforces 623E — Transforming Sequence**: Cross-ref **Problem 1B-23**.
- **Problem 4A-P7: Codeforces 960G — Bandit Blues**: Cross-ref **Problem 1A-23**.

---

### Tier 2: Intermediate (`Intermediate` — Problems 4A-P8 to 4A-P15)

- **Problem 4A-P8: Luogu P5406 — [THUPC2019] 找树**
  - **URL**: `https://www.luogu.com.cn/problem/P5406` | **Constraints**: $N \le 70, w_e < 2^{12}$.
  - **Statement & Formula**: Given an undirected graph where each bit position $b \in \{0, \dots, 11\}$ uses a specified bitwise operation $\oplus_b \in \{\text{AND}, \text{OR}, \text{XOR}\}$, find the maximum bitwise weight among all spanning trees. Apply the mixed-radix Fast Walsh–Hadamard Transform (FWT) to the $N \times N$ Laplacian matrix entries, compute $\det L^{(k)}$ at each of the $2^{12} = 4096$ point-value frequencies in $O(N^3)$ time, and IFWT!
- **Problem 4A-P9: Luogu P5339 — [TJOI2019] 唱、跳、rap和篮球**: Cross-ref **Problem 2B-B5**.
- **Problem 4A-P10: AtCoder ABC 279 Ex — Sum of Prod of Min**
  - **URL**: `https://atcoder.jp/contests/abc279/tasks/abc279_h` | **Constraints**: $N \le 10^6, M \le 10^{12}$, $\bmod 200003$.
  - **Statement & Formula**: Sum $\prod_{i=1}^N \min(A_i, B_i)$ over $1 \le A_i \le B_i$ with $\sum A_i = S_A, \sum B_i = M$. By a generating-function / Pentagonal Number miracle, the bivariate sum telescopes into $[x^{M - N}] \frac{1}{(1-x)^{2N}} \prod_{k \ge 1} (1 - x^k)$, evaluated modulo the small prime $P = 200003$ via Euler's Pentagonal Number Theorem + Lucas's Theorem in $O(\sqrt{M} + P)$ time!
- **Problem 4A-P11: AtCoder AGC 013 E — Placing Squares**: Cross-ref **Problem 2B-D5**.
- **Problem 4A-P12: Codeforces 1264D2 — Beautiful Bracket Sequence (Hard Version)**
  - **URL**: `https://codeforces.com/problemset/problem/1264/D2` | **Constraints**: $|S| \le 10^6$, $\bmod 998244353$.
  - **Statement & Formula**: Sum the maximum depth of a matched bracket subsequence over all $2^{\# '?'}$ completions of `S`. Choosing the split point between left `'('`s and right `')'`s yields $\sum_i i \binom{A}{i - L} \binom{B}{R - i}$, which collapses via the absorption identity $k \binom{A}{k} = A \binom{A-1}{k-1}$ + Vandermonde's Identity into $L \binom{A+B}{A + L - R} + A \binom{A+B-1}{A + L - R}$ in $O(1)$ per split!
- **Problem 4A-P13: UOJ 424 — count**: Cross-ref **Problem 5A-29**.
- **Problem 4A-P14: Codeforces 755G — PolandBall and Many Other Balls**: Cross-ref **Problem 5A-12**.
- **Problem 4A-P15: AtCoder AGC 058 D — Yet Another ABC String**: Cross-ref **Problem 5A-31**.

---

### Tier 3: Advanced (`Advanced` — Problems 4A-P16 to 4A-P22)

- **Problem 4A-P16: Codeforces 1553I — Stairs**
  - **URL**: `https://codeforces.com/problemset/problem/1553/I` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Given stair-block sizes $a_1, \dots, a_N$, partition the array into contiguous blocks of lengths $L_1, \dots, L_m$ matching $a_i$, and count permutations of the blocks where adjacent blocks in value are not merged, via Inclusion-Exclusion: each merged super-block of $c \ge 2$ stairs has weight $2$, while a single stair of length $1$ has weight $1$. Maintain a $2 \times 2$ polynomial matrix (boundary stair length $= 1$ vs $\ge 2$) via divide-and-conquer NTT in $O(N \log^2 N)$ time!
- **Problem 4A-P17: Codeforces 1336E2 — Chiori and Doll Picking (Hard Version)**
  - **URL**: `https://codeforces.com/problemset/problem/1336/E2` | **Constraints**: $N \le 2 \times 10^5, m \le 53$, $\bmod 998244353$.
  - **Statement & Formula**: Given $N$ integers $< 2^{53}$, for each $c = 0, \dots, m$, count subsets whose XOR sum has popcount $c$. Let $r$ be the rank of the XOR linear basis.
    - If $r \le 26$: enumerate all $2^r$ XOR sums directly in $O(2^r)$ time.
    - If $r > 26$: by the **MacWilliams Identity / FWT Duality**, the weight enumerator of the code $C$ of dimension $r$ is related to the weight enumerator of the orthogonal dual code $C^\perp$ of dimension $m - r \le 26$ via the Krawtchouk polynomial transform $P_c(w; m) = [x^c] (1 - x)^w (1 + x)^{m - w}$, computed in $O(2^{m-r} + m^3)$ time!
- **Problem 4A-P18: Luogu P5487 — [BJOI2019] 勘破神机**
  - **URL**: `https://www.luogu.com.cn/problem/P5487` | **Constraints**: $L, R \le 10^{18}, K \le 501$, $\bmod 998244353$.
  - **Statement & Formula**: Sum $\binom{f_n}{K}$ for $L \le n \le R$, where $f_n$ is either the $n$-th Fibonacci number ($m=2$) or the number of $3 \times n$ tilings ($m=3$). Expand $\binom{f_n}{K} = \frac{1}{K!} \sum_{j=0}^K (-1)^{K-j} \left[\begin{matrix} K \\ j \end{matrix}\right] f_n^j$, express $f_n = \alpha \lambda_1^n + \beta \lambda_2^n$ over $\mathbb{F}_{p^2} = \mathbb{F}_p[\sqrt{5}]$ (or $\mathbb{F}_p[\sqrt{3}]$), expand $f_n^j$ via the binomial theorem, and sum the geometric series in $O(K^2 \log R)$ time!
- **Problem 4A-P19: Codeforces 1349F2 — Slime and Sequences (Hard)**: Cross-ref **Problem 5A-27**.
- **Problem 4A-P20: QOJ 4815 — Bivariate Walk with Bounded Height & Weight (2D Bostan–Mori)**
  - **URL**: `https://qoj.ac/problem/4815` | **Constraints**: $d \le 15, N \le 10^{18}, K \le 10^4$, $\bmod 998244353$.
  - **Statement & Formula**: Given a directed graph on $d \le 15$ vertices with edge weights in $\{0, \dots, c\}$, count length-$N$ walks from $1$ to $d$ with total weight $0 \le k \le K$. Extract $[x^N y^k] \frac{P(x, y)}{\det(I - x A(y))} \bmod y^{K+1}$ via **Regime A 2D Bostan–Mori** in $(\mathbb{F}_p[y]/(y^{K+1}))[[x]]$ ($O(d K \log(dK) \log N)$) or **Regime B** (evaluate $y$ at $L > K$ roots of unity, run $L$ scalar 1D Bostan–Mori calls of degree $d$, and INTT in $O(K d \log d \log N + K d^3)$)!
- **Problem 4A-P21: AtCoder ABC 387 G — Prime Circuit**
  - **URL**: `https://atcoder.jp/contests/abc387/tasks/abc387_g` | **Constraints**: $N \le 2.5 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count connected labeled graphs on $N$ vertices in which every cycle has prime length. Every biconnected block is either a single edge ($K_2$) or a simple cycle of odd prime length $p \ge 3$! Similar to cactus graphs (**Problem 3A-27**), let $T(x)$ be rooted prime-circuit graphs: removing the root gives a $\text{SET}$ of edges ($T(x)$) and prime-length cycles ($\frac{1}{2} \sum_{p \ge 3 \text{ prime}} T(x)^{p-1}$). Thus $T(x) = x \exp\left(T(x) + \frac{1}{2} \sum_{p \ge 3 \text{ prime}} T(x)^{p-1}\right)$, solved via Lagrange Inversion $[x^N] T(x) = \frac{1}{N} [u^{N-1}] \exp\left(N u + \frac{N}{2} \sum_{p \ge 3 \text{ prime}} u^{p-1}\right)$ in **one `exp` call** in $O(N \log N)$ time!
- **Problem 4A-P22: yukicoder 1080 / Luogu P6667 — Generalized Delannoy & Elegant Summation**: Cross-ref **Problem 2A-18** and **Problem 5A-18** ($[x^n y^n]\frac{1}{1-ax-by-cxy} = [t^n]\big((1-ct)^2 - 4abt\big)^{-1/2}$ via Furstenberg's residue theorem in $O(N)$ time).

---

### Tier 4: Mastery (`Mastery` — Problems 4A-P23 to 4A-P28)

- **Problem 4A-P23: AtCoder ARC 154 F — Dice Game**
  - **URL**: `https://atcoder.jp/contests/arc154/tasks/arc154_f` | **Constraints**: $N \le 2 \times 10^5, M \le 2 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Roll an $N$-sided die until all $N$ faces have appeared; output $\mathbb{E}[T^k]$ for all $k = 1, \dots, M$. The PGF of the Coupon Collector stopping time is $F(z) = \prod_{i=0}^{N-1} \frac{\frac{N-i}{N} z}{1 - \frac{i}{N} z}$. The Moment Generating Function is $M(t) = F(e^t) = \sum_{k=0}^M \mathbb{E}[T^k] \frac{t^k}{k!}$. Compute $F(z) = \frac{A(z)}{B(z)}$ via a D&C NTT product tree, evaluate $B(e^t) \bmod t^{M+1}$ via $[t^k]B(e^t) = \frac{1}{k!}[t^k]\sum_{j=0}^{N-1}\frac{b_j}{1 - j t}$ (or partial fractions + $H(e^t - 1)$), and invert in $O((N+M)\log^2(N+M))$ time!
- **Problem 4A-P24: UOJ 596 — [集训队互测2021] 三维立体混元劲 (3D Twisted Kronecker FPS $\ln$)**
  - **URL**: `https://uoj.ac/problem/596` | **Constraints**: $A, B, C \le 50$ ($N = (A+1)(B+1)(C+1) \le 132,651$), $\bmod 998244353$.
  - **Statement & Formula**: Count connected labeled 3-colored graphs with $a \le A$ red, $b \le B$ green, and $c \le C$ blue vertices weighted by edge fugacities $\alpha^{\binom{a}{2}}\beta^{\binom{b}{2}}\gamma^{\binom{c}{2}}\lambda_{rg}^{ab}\lambda_{gb}^{bc}\lambda_{br}^{ca}$. By the Multivariate Exponential Formula, $F(x, y, z) = \ln G(x, y, z) \bmod (x^{A+1}, y^{B+1}, z^{C+1})$. Pack $(a, b, c) \mapsto I = a + b(A+1) + c(A+1)(B+1)$ with carry-tracking grading $\chi(I) = (b + c) \bmod 3$ and compute $\ln G = \mathfrak{D}^{-1}\big(\mathfrak{D}(G) \cdot_\chi G^{-1}\big)$ via **Twisted Kronecker ($\chi$-Graded) 3D FPS $\ln$** in $O(3 ABC \log(ABC))$ time!
- **Problem 4A-P25: yukicoder 1783 — Remix Sum (Hybrid Cyclic / Truncated Multivariate FPS Power)**
  - **URL**: `https://yukicoder.me/problems/no/1783` | **Constraints**: $K \le 5, 10^K \le 10^5, M \le 10^{18}$, prime modulus $P = 120586241 = 2^{20} \cdot 115 + 1$ ($10 \mid P - 1$).
  - **Statement & Formula**: Given $N$ $K$-digit base-10 integers where each digit position $r \in \{1, \dots, K\}$ adds either cyclically $\pmod{10}$ (modulo $z_r^{10} - 1$) or with truncation $< 10$ (modulo $z_r^{10}$), compute $F(z_1, \dots, z_K)^M$ for all $10^K$ targets modulo $P = 120586241$. Apply a $(K - T)$-dimensional radix-10 DFT (using $\omega_{10} = g^{(P-1)/10} \bmod P$) along cyclic dimensions to decouple into $10^{K-T}$ independent $T$-variate truncated slices of size $10^T$, compute $F_\omega^M$ on each slice via Twisted Kronecker FPS $\exp(M \ln F_\omega)$, and apply the radix-10 IDFT in $O(10^K T^2 \log 10 + 10^{K+1}(K - T))$ time!
- **Problem 4A-P26: AtCoder ARC 138 F / QOJ 8528 — General Dense FPS Composition & Power Projection**
  - **URL**: `https://qoj.ac/problem/8528` | **Constraints**: $N \le 2 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Given $F(x), G(x)$ with $G(0) = 0$, compute $F(G(x)) \bmod x^N$ (and its transpose, Power Projection $\langle \mathbf{w}, G^k \rangle$ for $0 \le k < N$) in $O(N \log^2 N)$ time via the **Kinoshita–Li (2024) Bostan–Mori Lift**: treat $F(G(x)) = [y^0] \frac{F(y)}{1 - y^{-1} G(x)}$ as a bivariate rational function and apply Bostan–Mori parity halving $(1 - y^{-1}G(x))(1 + y^{-1}G(-x))$ while dynamically trading $x$-degree for $y$-degree ($d_x \gets d_x / 2, d_y \gets 2 d_y$)!
- **Problem 4A-P27: LibreOJ 6728 (U 群把妹王) & UOJ 604 (2D Lattice Walk First Return to Origin)**
  - **URL**: `https://loj.ac/p/6728` & `https://uoj.ac/problem/604` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**:
    - **Part A (LOJ 6728 — U 群把妹王)**: Solve high-degree implicit/transposed tree enumeration via Kinoshita–Li Power Projection + Lagrange Inversion in $O(N \log^2 N)$ time.
    - **Part B (UOJ 604 — 2D Lattice Walk First Return to Origin)**: Given $S(x, y) = A(y)x + B(y) + C(y)x^{-1} \in \mathbb{F}_p[x, x^{-1}, y, y^{-1}]$, total returns to $(0, 0)$ have OGF $R(t) = \operatorname{CT}_{x,y}\frac{1}{1 - t S(x,y)} = \operatorname{CT}_y\big((1 - t B(y))^2 - 4t^2 A(y)C(y)\big)^{-1/2}$ (computed up to $t^N$ via its order-$\le 4$ D-finite P-recursion in $O(N)$ time), and first returns have OGF $F(t) = 1 - R(t)^{-1} \bmod t^{N+1}$ in $O(N \log N)$ time!
- **Problem 4A-P28: Frobenius Bivariate/Trivariate Diagonal & MacMahon's Master Theorem / Generalized Dixon Cubes**
  - **Statement & Formula**:
    - **Part A (Cyclic Linear-Form Diagonal via MMT, $N \le 10^6$)**: Compute $D_n = [x^n y^n z^n] \prod_{i=1}^3 (a_{i1}x + a_{i2}y + a_{i3}z)^n = [x^n y^n z^n] \det(I_3 - \operatorname{diag}(x,y,z)A)^{-1}$ for all $0 \le n \le N$ via MacMahon's Master Theorem + Furstenberg's quadratic residue reduction to an order-$\le 4$ D-finite P-recursion in $O(N)$ time!
    - **Part B (Huge-$N$ Modulo Small Prime $p$, $N \le 10^{18}, p \le 101$)**: Compute $[x^N y^N z^N] Q(x,y,z)^{-1} \bmod p$ via **Bostan–Christol–Dumas Frobenius Reduction**: since $Q(x,y,z)^p \equiv Q(x^p, y^p, z^p) \pmod p$, iterate $P_{k+1} = \mathcal{S}_{N_k \bmod p}\big(P_k Q^{p-1}\big) \bmod p$ across the $\lfloor\log_p N\rfloor + 1$ base-$p$ digits of $N$ in $O(p^3 \log_p N)$ time!

---

## 9. Wave 4B Problem Encyclopedia: Furstenberg's Theorem, Kernel Method & Good–Lagrange Inversion (`cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`)

> **Full Reference**: See `fps_research/cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`, Section 7 (Lines 710–1474).

### Tier 1: Stepping Stone (`Stepping Stone` — Problems 4B-1 to 4B-8)

- **Problem 4B-1: AtCoder ARC 012 D — Don't Step on the Threshold!**: Cross-ref **Problem 1B-11**.
- **Problem 4B-2: AtCoder ABC 240 G — Teleporting Takahashi**: Cross-ref **Problem 2A-33**.
- **Problem 4B-3: Codeforces 438E — The Child and Binary Tree**: Cross-ref **Problem 1A-10**.
- **Problem 4B-4: Codeforces 1810G — The Maximum Prefix**: Cross-ref **Problem 3A-9**.
- **Problem 4B-5: Luogu P6672 — [清华集训2016] 你的生命已如风中残烛**
  - **URL**: `https://www.luogu.com.cn/problem/P6672` | **Constraints**: $N \le 40$, exact / modular.
  - **Statement & Formula**: Given $m$ cards with values $w_i \ge 0$ summing to $m$, append a $0$ so $\sum_{i=1}^{m+1} (w_i - 1) = -1$. By **Raney's Lemma**, among the $m + 1$ cyclic shifts of any arrangement, **exactly 1** has all proper prefix sums $\ge 0$! Since the $0$ must land at the very end in that valid cyclic shift, the fraction of valid arrangements is $\frac{1}{m + 1}$!
- **Problem 4B-6: Luogu P5434 — 有标号荒漠计数**: Cross-ref **Problem 1A-27**.
- **Problem 4B-7: Codeforces 960G — Bandit Blues**: Cross-ref **Problem 1A-23**.
- **Problem 4B-8: Codeforces 1109D — Sasha and Interesting Fact from Graph Theory**
  - **URL**: `https://codeforces.com/problemset/problem/1109/D` | **Constraints**: $N, M \le 10^6$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Count weighted trees on $N$ vertices where the path between vertex $1$ and vertex $2$ has total weight $M$. Fix the number of edges $k$ on the path between $1$ and $2$: choose the $k - 1$ internal vertices in $\binom{N-2}{k-1} (k-1)!$ ways, assign weights summing to $M$ in $\binom{M-1}{k-1}$ ways, assign the remaining $N - 1 - k$ weights in $M^{N - 1 - k}$ ways, and connect the $k + 1$ path vertices into a spanning forest of $N$ vertices in $(k + 1) N^{N - k - 2}$ ways by Generalized Cayley's Formula!

---

### Tier 2: Intermediate (`Intermediate` — Problems 4B-9 to 4B-16)

- **Problem 4B-9: AtCoder ABC 222 H — Beautiful Binary Tree**: Cross-ref **Problem 1A-13**.
- **Problem 4B-10: AtCoder KUPC 2019 K — One or All**: Cross-ref **Problem 2A-3**.
- **Problem 4B-11: AtCoder AGC 021 E — Ball Eat Chameleons**: Cross-ref **Problem 2A-11**.
- **Problem 4B-12: Codeforces 1821F — Timber**
  - **URL**: `https://codeforces.com/problemset/problem/1821/F` | **Constraints**: $N, M \le 3 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Place $M$ trees of height $K$ in $[1, N]$ and choose left/right fall directions so intervals don't overlap. By Inclusion-Exclusion / Kernel OGF, an isolated tree contributes $2 x^{K+1}$ while a chain of $c \ge 2$ overlapping trees cancels to a 2-term polynomial: $[x^N] \frac{1}{(1-x)^2} \left(\frac{x^K(2 + x^K)}{1 + x^K}\right)^M$, expanded in $O(M)$ time!
- **Problem 4B-13: Luogu P6596 — How Many of Them**: Cross-ref **Problem 2B-A12**.
- **Problem 4B-14: yukicoder 1341 / CF Gym 103415 K — Asymmetric $+1, -2$ Gambler's Walk (Kernel Method)**
  - **Statement & Formula**: Count walks on $\mathbb{Z}_{\ge 0}$ with steps $+1$ (weight $p$) and $-2$ (weight $q$). The kernel equation is $K(t, u) F(t, u) = 1 - q t u^{-2} \big(F_0(t) + u F_1(t)\big)$, where $K(t, u) = 1 - t(p u + q u^{-2}) = 0 \implies u^2 - p t u^3 - q t = 0$. This cubic has **two** small roots $u_1(t), u_2(t) = \pm \sqrt{q t} + O(t)$ as $t \to 0$! Substituting both $u_1(t)$ and $u_2(t)$ into the numerator gives a $2 \times 2$ linear system determining BOTH boundary series $F_0(t)$ and $F_1(t)$!
- **Problem 4B-15: HDU 4656 / LibreOJ 6570 — MacMahon Master Theorem**
  - **Statement & Formula**: Compute $[x_1^{a_1} \dots x_k^{a_k}] \prod_{i=1}^k \left(\sum_{j=1}^k M_{i, j} x_j\right)^{a_i} = [x_1^{a_1} \dots x_k^{a_k}] \frac{1}{\det(I - \text{diag}(x_1, \dots, x_k) M)}$ via MacMahon's Master Theorem!
- **Problem 4B-16: AtCoder ABC 336 G — 16 Integers**
  - **URL**: `https://atcoder.jp/contests/abc336/tasks/abc336_g` | **Constraints**: $\sum X_i \le 10^6$, $\bmod 998244353$.
  - **Statement & Formula**: Count binary strings where every $4$-bit window $w \in \{0, 1\}^4$ appears $X_w$ times. This is Eulerian paths on the $8$-vertex De Bruijn graph $B(2, 3)$, counted in $O(\sum X_w)$ time via the **BEST Theorem** (Matrix-Tree cofactor $\det L^{(v)}$ of size $7 \times 7$ times $\prod_u (\text{outdeg}(u) - 1)! / \prod_w X_w!$), which is combinatorially dual to Multivariate Good–Lagrange Inversion!

---

### Tier 3: Advanced (`Advanced` — Problems 4B-17 to 4B-25)

- **Problem 4B-17: Codeforces 755G — PolandBall**: Cross-ref **Problem 5A-12**.
- **Problem 4B-18: AtCoder ARC 137 F — Overlaps**: Cross-ref **Problem 3B-19**.
- **Problem 4B-19: Luogu P5827 / UOJ 498 — 点双连通图计数**: Cross-ref **Problem 3A-39** and **Problem 3A-40**.
- **Problem 4B-20: Luogu P7364 — 有标号二分图计数**: Cross-ref **Problem 3A-32** and **Problem 3A-33**.
- **Problem 4B-21: AtCoder ARC 136 F — Flip Cells**: Cross-ref **Problem 2A-5**.
- **Problem 4B-22: Codeforces 1479E — School Clubs**: Cross-ref **Problem 5A-26**.
- **Problem 4B-23: Luogu P8333 — [SDOI/SXOI2022] 多边形**
  - **URL**: `https://www.luogu.com.cn/problem/P8333` | **Constraints**: $N \le 5 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count dissections / triangulations of a generalized polygon with collinear boundary vertices using Tutte's catalytic variable / Good–Lagrange Inversion + Schröder path convolution in $O(N \log N)$ time.
- **Problem 4B-24: LibreOJ 6728 — U 群把妹王**: Cross-ref **Problem 4A-P27**.
- **Problem 4B-25: yukicoder 2104 / Codeforces 1666H — Asymmetric $(p, q)$-Diagonal Fuss–Catalan Extraction**
  - **Statement & Formula**: Extract $[x^{p n} y^{q n}] \frac{1}{1 - x - y}$ or Fuss–Catalan diagonals via Furstenberg's theorem: set $x = t / y^r$ so $y^{p+q} - t y^q - y^{p+q+1} = 0$, and apply Lagrange Inversion to the small roots!

---

### Tier 4: Mastery (`Mastery` — Problems 4B-26 to 4B-33)

- **Problem 4B-26: Codeforces 1349F2 — Slime and Sequences**: Cross-ref **Problem 5A-27**.
- **Problem 4B-27: AtCoder AGC 058 D — Yet Another ABC String (Furstenberg Diagonal Perspective)**: Cross-ref **Problem 5A-31**.
- **Problem 4B-28: Luogu P5828 — 边双连通图计数**: Cross-ref **Problem 3A-40** and **Problem 5B-C13**.
- **Problem 4B-29: Codeforces Gym 102586 J — Quarter-Plane Kreweras / Tandem Walk Excursions**
  - **Statement & Formula**: Count 2D quarter-plane walks in $\mathbb{Z}_{\ge 0}^2$ with tandem steps $(+1, 0), (-1, +1), (0, -1)$ via the **Algebraic Kernel Method** (Bousquet-Mélou & Mishna): the dihedral group of symmetries of the kernel $K(x, y) = 1 - t(x + \bar{x} y + \bar{y})$ has order $6$, and taking the alternating orbit sum eliminates both boundary series $F(x, 0)$ and $F(0, y)$, yielding $[t^{3n}] F(0, 0) = \frac{2}{(n+1)(2n+1)(3n+1)} \binom{3n}{n, n, n}$!
- **Problem 4B-30: UOJ 596 — [集训队互测2021] 三维立体混元劲**: Cross-ref **Problem 4A-P24**.
- **Problem 4B-31: QOJ 6184 ([CTT2022] 欧拉? 欧拉!) & QOJ 6505**
  - **URL**: `https://qoj.ac/problem/6184` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Apply **Multivariate Good–Lagrange Inversion** $[\mathbf{x}^{\mathbf{n}}] H(\mathbf{F}(\mathbf{x})) = [\mathbf{u}^{\mathbf{n}}] H(\mathbf{u}) \det\left(\delta_{i,j} - \frac{u_j}{\phi_i(\mathbf{u})} \frac{\partial \phi_i}{\partial u_j}\right) \prod_{i=1}^k \phi_i(\mathbf{u})^{n_i}$ to enumerate multi-type directed trees and Eulerian digraph walks!
- **Problem 4B-32: LibreOJ 3398 — 带加强和多项木**: Cross-ref **Problem 3B-9b (`#219`, `Ch 17 [Int-2]`)**.
- **Problem 4B-33: AtCoder ARC 145 F — Modulo Sum of Increasing Sequences / Potentials**
  - **URL**: `https://atcoder.jp/contests/arc145/tasks/arc145_f` | **Constraints**: $N, M \le 10^6, P \le 10^6$, $\bmod 998244353$.
  - **Statement & Formula**: For each $r = 0, \dots, P-1$, count integer sequences $0 \le A_1 \le \dots \le A_N \le M$ with $\sum A_i \equiv r \pmod P$. Decompose $M + 1 = q P + s$ and apply the Roots-of-Unity / $q$-Binomial orbit decomposition over $g = \gcd(N, P)$ to extract all $P$ residues in $O((N + P) \log P)$ time!

---

## 10. Wave 5A Problem Encyclopedia: D-Finite ODEs, Sparse $O(NK)$ FPS, CDQ NTT & Relaxed Convolution (`cohort3_wave_5a_ode_sparse_cdq_relaxed.md`)

> **Full Reference**: See `fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md`, Section 7 (Lines 860–1670).

### Tier 1: Stepping Stone (`Stepping Stone` — Problems 5A-1 to 5A-8)

- **Problem 5A-1: Codeforces 1096G — Lucky Tickets**
  - **URL**: `https://codeforces.com/problemset/problem/1096/G` | **Constraints**: $N \le 2 \times 10^5, K \le 10$, $\bmod 998244353$.
  - **Statement & Formula**: Given $K$ allowed decimal digits $D \subseteq \{0, \dots, 9\}$, count $N$-digit tickets whose first $N/2$ digits have the same sum as the last $N/2$ digits. Let $A(x) = \sum_{d \in D} x^d$; we want $\sum_{s} ([x^s] A(x)^{N/2})^2$. Since $A(x)$ has at most $K \le 10$ nonzero terms, `SparseFPS::pow` ($A B' = \frac{N}{2} A' B$) computes $A(x)^{N/2}$ in **$O(NK)$ time** without NTT!
- **Problem 5A-2: Luogu P4389 — 付公主的背包**: Cross-ref **Problem 1A-7a** (solved in Wave 5A via CDQ NTT on $F' = A' F$ after harmonic sieve).
- **Problem 5A-3: Luogu P4841 — 城市规划**: Cross-ref **Problem 1A-9a** (solved via `RelaxedConvolution` `get_interior()` in 10 lines).
- **Problem 5A-4: Codeforces 438E — The Child and Binary Tree**: Cross-ref **Problem 1A-10** (solved via self-referential `RelaxedConvolution` on $F = 1 + D F^2$).
- **Problem 5A-5: AtCoder ABC 222 H — Beautiful Binary Tree ($O(N)$ D-Finite ODE Method)**
  - **URL**: `https://atcoder.jp/contests/abc222/tasks/abc222_h` | **Constraints**: $N \le 10^7$, $\bmod 998244353$.
  - **Statement & Formula**: By Lagrange Inversion, $a_N = \frac{1}{N} [x^{N-1}] P(x)^N$ where $P(x) = (x+1)^2(x^2 + 3x + 1)$ has only $K = 5$ nonzero terms! Applying `SparseFPS::pow` ($P B' = N P' B$) yields a 4-term P-recursive recurrence computing $[x^{N-1}] P(x)^N$ in **$O(N)$ time and $O(1)$ auxiliary memory**!
- **Problem 5A-6: yukicoder 1939 — Numbered Colorful Balls**
  - **URL**: `https://yukicoder.me/problems/no/1939` | **Constraints**: $N, M \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Multiply $M$ sparse 2-term/3-term polynomial factors via `SparseFPS::ln` + `SparseFPS::exp` or divide-and-conquer NTT in $O(N \log^2 N)$ time.
- **Problem 5A-7: Luogu P4456 — [CQOI2018] 交错序列**
  - **URL**: `https://www.luogu.com.cn/problem/P4456` | **Constraints**: $N \le 10^7, a, b \le 45$, arbitrary prime $P$.
  - **Statement & Formula**: Sum $x^a y^b$ over all binary strings of length $N$ with no two adjacent $1$s ($x = \# 0, y = \# 1$). Instead of $O((a+b)^3 \log N)$ matrix exponentiation, use $x = N - y$ to reduce to a single variable $y$, or use the 2-state recurrence for $(1 + x + y x^2)$ to get a P-recursive recurrence in $N$.
- **Problem 5A-8: Codeforces 623E — Transforming Sequence**: Cross-ref **Problem 1B-23**.

---

### Tier 2: Intermediate (`Intermediate` — Problems 5A-9 to 5A-16)

- **Problem 5A-9: yukicoder 963 — 門松列列 2 (Alternating Permutations)**
  - **URL**: `https://yukicoder.me/problems/no/963` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count alternating (up-down) permutations of length $N$ via André's ODE $2 F'(x) = 1 + F(x)^2$, solved online via `RelaxedConvolution` (`f[n] = inv[n] * rc.next(f[n-1], f[n-1]) / 2`) in $O(N \log^2 N)$ or Newton ODE in $O(N \log N)$.
- **Problem 5A-10: AtCoder ABC 213 Ex — Stroll**: Cross-ref **Problem 1B-27**.
- **Problem 5A-11: Codeforces 553E — Kyoya and Train**
  - **URL**: `https://codeforces.com/problemset/problem/553/E` | **Constraints**: $N \le 50, M \le 100, T \le 2 \times 10^4$, real FFT.
  - **Statement & Formula**: Expected minimum cost to reach node $N$ within time $T$ where traversing edge $e = (u, v)$ takes random time $k \in [1, T]$ with probability $p_{e, k}$. Run **backward** CDQ Divide-and-Conquer FFT from $t = T$ down to $0$: at node $u$, $f_u(t) = \min_{e=(u, v)} \big(c_e + \sum_{k=1}^{T-t} p_{e, k} f_v(t + k)\big)$ in $O(M T \log^2 T + N^3)$ time!
- **Problem 5A-12: Codeforces 755G — PolandBall and Many Other Balls (`EI 科技` $O(K)$ ODE Solution)**
  - **URL**: `https://codeforces.com/problemset/problem/755/G` | **Constraints**: $N \le 10^9, K \le 2^{15}$, $\bmod 998244353$.
  - **Statement & Formula**: Group $N$ balls in a row into $k$ sets of size $1$ ($\{i\}$) or $2$ ($\{i, i+1\}$). The bivariate OGF is $F(x, y) = \frac{1}{1 - x(1 + y) - x^2 y} = \sum_{n \ge 0} P_n(y) x^n$. By Furstenberg / discriminant theory, $Z_n(y) = [x^n] F(x, y)$ satisfies the **3-term D-finite ODE** in $y$:
    $$(1 + 6y + y^2) Z_n'(y) + \big((1 - n) - (3n + 1) y\big) Z_n(y) = \dots \implies (k + 1) c_{k+1} = (2N + 1 - k) c_k + (N + k) c_{k-1} \text{ (shifted basis!)}$$
    More precisely, $P_N(y) = \left(\frac{1 + y + \Delta}{2}\right)^N$ where $\Delta = \sqrt{1 + 6y + y^2}$ satisfies $\Delta^2 P_N'' + \Delta \Delta' P_N' - N^2 y P_N = 0$, giving a 5-term P-recursive recurrence that computes ALL $c_1, \dots, c_K$ in **$O(K)$ time** without a single NTT!
- **Problem 5A-13: AtCoder AGC 043 D — Merge Triplets**: Cross-ref **Problem 2B-C3**.
- **Problem 5A-14: AtCoder ABC 253 Ex — We Love Forest**: Cross-ref **Problem 5B-F4**.
- **Problem 5A-15: Codeforces 848E — Days of Floral Colours**
  - **URL**: `https://codeforces.com/problemset/problem/848/E` | **Constraints**: $N \le 5 \times 10^4$, $\bmod 998244353$.
  - **Statement & Formula**: Partition $2N$ circular vertices into opposite pairs or adjacent pairs of length $\ge 1$, weighting each contiguous segment of length $L$ by $L^2$. The $3 \times 3$ state transitions (no boundary / 1 boundary / 2 boundaries) satisfy a linear system of rational OGFs inverted via CDQ NTT in $O(N \log^2 N)$ time (or $O(N)$ via the degree-16 characteristic denominator!).
- **Problem 5A-16: yukicoder 1533 — Non-Stop Random Walk**
  - **URL**: `https://yukicoder.me/problems/no/1533` | **Constraints**: $N, K \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count non-backtracking walks via the Ihara-style rational generating function / sparse ODE recurrence in $O(N)$ time.

---

### Tier 3: Advanced (`Advanced` — Problems 5A-17 to 5A-22)

- **Problem 5A-17: Codeforces 932E — Team Work (Strengthened $O(K)$ `EI 科技` Version for $K \le 10^7$)**
  - **URL**: `https://codeforces.com/problemset/problem/932/E` | **Constraints**: $N \le 10^9, K \le 10^7$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Compute $\sum_{i=0}^N \binom{N}{i} i^K x^i$ (for $x = 1$). Since $i^K = K! [t^K] e^{it}$, we need $K! [t^K] (1 + x e^t)^N$. Set $u = e^t - 1$, so $(1 + x e^t)^N = (1 + x)^N \left(1 + \frac{x}{1+x} u\right)^N$. Truncate the Binomial series to degree $K$ in $u$:
    $$F(u) = \sum_{j=0}^K \binom{N}{j} (1 + x)^{N-j} x^j u^j$$
    Now $F(u)$ satisfies the **exact first-order inhomogeneous ODE**:
    $$(1 + x + x u) F'(u) - N x F(u) = -(K + 1) \binom{N}{K + 1} (1 + x)^{N - K} x^{K + 1} u^K$$
    Substitute $u = e^t - 1$ ($\frac{d}{dt} = (1 + u) \frac{d}{du}$): then $G(t) = F(e^t - 1)$ satisfies a 2-term ODE in $e^t$, and since $[t^k] (e^t - 1)^K$ can be precomputed via a linear sieve of $i^K$, we extract $[t^K] G(t)$ in **$O(K)$ time**!
- **Problem 5A-18: Luogu P6667 — [清华集训2016] 如何优雅地求和 ($O(m)$ Lagrange-Basis ODE)**
  - **URL**: `https://www.luogu.com.cn/problem/P6667` | **Constraints**: $n \le 10^9, m \le 2 \times 10^4$ (strengthened to $m \le 10^7$).
  - **Statement & Formula**: By **Problem 5A-17**, once we compute $c_j = [u^j] (1 + x u)^n \bmod u^{m+1}$ in the shifted basis $u = e^t - 1$ — or directly express $\sum_{k=0}^n \binom{n}{k} x^k (1-x)^{n-k} \binom{k}{j} = \binom{n}{j} x^j$ and apply the backwards recurrence on the Lagrange interpolation basis $\binom{k}{i}\binom{m-k}{m-i}$ — the entire sum $\sum_{k=0}^n \binom{n}{k} x^k (1-x)^{n-k} f(k)$ is evaluated from $f(0), \dots, f(m)$ in **$O(m)$ time** with zero NTTs!
- **Problem 5A-19: Codeforces 1097G — Vladislav and a Great Legend**: Cross-ref **Problem 2B-A14**.
- **Problem 5A-20: AtCoder ABC 230 Ex — Bullseye (Chained `RelaxedConvolution`)**
  - **URL**: `https://atcoder.jp/contests/abc230/tasks/abc230_h` | **Constraints**: $W \le 2 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Given allowed coin weights $W_x(x) = \sum_{w \in S} x^w$, count unlabeled rooted trees/bags where $B(x) = x W_x(x) \exp\left(\sum_{k \ge 1} \frac{B(x^k)}{k}\right)$. Let $A(x) = \sum_{k \ge 1} \frac{B(x^k)}{k}$ and $E(x) = \exp(A(x))$, so $E'(x) = A'(x) E(x)$ and $B(x) = x W_x(x) E(x)$. Run **two parallel `RelaxedConvolution` instances** (`rc_exp` for $A' \cdot E$ and `rc_B` for $W_x \cdot E$) together with an $O(W \log W)$ harmonic divisor sieve updating $a_n = \sum_{d \mid n} \frac{d}{n} b_d$: total time $O(W \log^2 W)$ in 20 lines of code!
- **Problem 5A-21: AtCoder ABC 260 Ex — Colorfulness**
  - **URL**: `https://atcoder.jp/contests/abc260/tasks/abc260_h` | **Constraints**: $N, M \le 2.5 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Given $N$ balls with colors $a_1, \dots, a_N$, for each $m = 1, \dots, M$, sum $x^m$ over all permutations where $x$ is the number of adjacent different-color pairs. First compute $f_v$ (permutations with $v$ adjacent different-color pairs) via Inclusion-Exclusion + Divide-and-Conquer NTT + Taylor shift (**Problem 2A-29**). Then compute $\sum_{v=1}^N f_v v^m = [x^m] \sum_{v=1}^N \frac{f_v}{1 - v x}$ for all $m \le M$ via a binary product tree of $2 \times 2$ fraction merges followed by one polynomial inversion in $O((N + M) \log^2 N)$ time!
- **Problem 5A-22: AtCoder ABC 300 Ex & ARC 138 E**: Cross-ref **Problem 2A-4** (with $O(K \log N)$ 3-sparse division modulo $x^{K+1} - 2x^K + 1$ for ABC 300 Ex and RSK block binomial convolution for ARC 138 E).

---

### Tier 4: Mastery (`Mastery` — Problems 5A-23 to 5A-34)

- **Problem 5A-23: LibreOJ 6538 / Luogu P5293 / P6597 — 烷基计数 加强版 加强版 (12-Line Chained `RelaxedConvolution`)**: Cross-ref **Problem 1A-14** ($F(x)^3 + 3 F(x) F(x^2) + 2 F(x^3) = F(x)(F(x)^2 + 3 F(x^2)) + 2 F(x^3)$ solved online via two `RelaxedConvolution` instances `rc_S` and `rc_P` in $O(N \log^2 N)$ time with zero polynomial inversions).
- **Problem 5A-24: UOJ 514 — [UR #19] 通用测评号 (`EI 科技` Truncated Exponential Derivative)**
  - **URL**: `https://uoj.ac/problem/514` | **Constraints**: $n \le 250, 1 \le b < a \le 250$, $\bmod 998244353$.
  - **Statement & Formula**: $n$ tanks receive fuel $1$ at a time at random until all $n$ tanks have $\ge b$ fuel; find the expected number of tanks with $\ge a$ fuel at that moment. Under Poissonization, $S_{<m}(x) = \sum_{j=0}^{m-1} \frac{x^j}{j!}$ satisfies $S_{<m}'(x) = S_{<m}(x) - \frac{x^{m-1}}{(m-1)!}$, so $\frac{d}{dx}\big(S_{<a}(x)^k\big) = k S_{<a}(x)^k - k \frac{x^{a-1}}{(a-1)!} S_{<a}(x)^{k-1}$, collapsing the $O(n^3 a^2)$ polynomial power table to an **$O(n^2 a)$** 3-term ODE recurrence!
- **Problem 5A-25: Codeforces 1349D — Slime and Biscuits**
  - **URL**: `https://codeforces.com/problemset/problem/1349/D` | **Constraints**: $m \le 10^5, S = \sum a_i \le 3 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Martingale potential $f(x)$ satisfies $\mathbb{E}[\Delta \sum_{i=1}^m f(a_i)] = -1$. Taking the first difference $g(x) = f(x+1) - f(x)$ reduces the second-order equation to the first-order P-recursive recurrence $(S - x) g(x) = x(m - 1) g(x - 1) - S(m - 1)$ with $g(0) = -(m - 1)$, solved in $O(S)$ time!
- **Problem 5A-26: Codeforces 1479E — School Clubs**
  - **URL**: `https://codeforces.com/problemset/problem/1479/E` | **Constraints**: $m \le 1000, S = \sum a_i \le 10^9$, $\bmod 998244353$.
  - **Statement & Formula**: Martingale potential $f(x)$ ($f(0) = 0$) over club sizes has first difference $d_x = f(x+1) - f(x)$ satisfying the homogeneous first-order P-recursive recurrence $(S - x) d_x = (2S - x) d_{x-1}$ with $d_0 = -2$, evaluated at $a_1, \dots, a_m, S$ in $O(\sqrt{S} \log S + m \log^2 m)$ time via $2 \times 2$ polynomial matrix BSGS multipoint evaluation!
- **Problem 5A-27: Codeforces 1349F2 — Slime and Sequences (Hard Version)**
  - **URL**: `https://codeforces.com/problemset/problem/1349/F2` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Bijection to Eulerian numbers $\left\langle \begin{matrix} m \\ j \end{matrix} \right\rangle$ with bivariate EGF $\frac{1 - y}{e^{(y-1)x} - y}$. Extracting all $k = 1, \dots, N$ via Lagrange Inversion on $w = 1 - \frac{u}{\ln(1+u)}$ yields a rational function $\frac{H(w)}{(1-w)^2}$ with a double pole at $w = 1$; subtract $H(1)(1-w)^{-2} - H'(1)(1-w)^{-1}$ before polynomial inversion to solve in $O(N \log N)$ time.
- **Problem 5A-28: UOJ 450 — [集训队作业2018] 复读机 (Bivariate Euler PDE + Roots of Unity Filter)**
  - **URL**: `https://uoj.ac/problem/450` | **Constraints**: $n \le 10^9, k \le 5 \times 10^5$ ($k \le 2000$ for $d=3$), $d \in \{1, 2, 3\}$, $\bmod 19491001$.
  - **Statement & Formula**: Compute $n! [z^n] \big(\sum_{m \ge 0} \frac{z^{dm}}{(dm)!}\big)^k \bmod 19491001$. For $d = 3$, let $\omega = 7^{(p-1)/3} \bmod p = 663067$ be a primitive cube root of unity and set $x = e^z, y = e^{\omega z}$ so $e^{\omega^2 z} = x^{-1} y^{-1}$. Apply the bivariate Euler operators $\vartheta_x, \vartheta_y$ to $P(x, y) = (x + y + x^{-1} y^{-1})^k$ to extract all $(2k+1)^2$ coefficients $c_{i, j}$ in $O(k^2)$ time and sum $3^{-k} \sum_{i, j} c_{i, j} (i + j\omega)^n \bmod 19491001$!
- **Problem 5A-29: UOJ 424 — [集训队作业2018] count**
  - **URL**: `https://uoj.ac/problem/424` | **Constraints**: $n, m \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: RMQ-equivalence classes of length-$n$ arrays over $\{1, \dots, m\}$ biject to $n$-node Cartesian binary trees with maximum left-chain depth $\le m$, whose OGF is $\frac{Q_m(x)}{Q_{m+1}(x)}$ where $Q_k(x) = \sum_{j=0}^{\lfloor k/2 \rfloor} (-1)^j \binom{k - j}{j} x^j$, inverted in $O(n \log n)$ time!
- **Problem 5A-30: Codeforces 1515E — Phoenix and Computers**
  - **URL**: `https://codeforces.com/problemset/problem/1515/E` | **Constraints**: $n \le 400$, arbitrary modulus $M \le 10^9$.
  - **Statement & Formula**: Manual computer activation blocks have EGF $\frac{e^{2x}-1}{2}$ separated by single automatic computers, giving bivariate EGF $F(x, y) = \frac{e^{2xy}-1}{2 - x(e^{2xy}-1)}$ and closed-form sum $\sum_{c=1}^{\lfloor(n+1)/2\rfloor} 2^{n+1-2c} c! \left\{\begin{matrix} n+1-c \\ c \end{matrix}\right\} \bmod M$ in $O(n^2)$ time (or $O(n)$ via D-finite recurrence for prime $M$).
- **Problem 5A-31: AtCoder AGC 058 D — Yet Another ABC String**
  - **URL**: `https://atcoder.jp/contests/agc058/tasks/agc058_d` | **Constraints**: $A, B, C \le 10^6$, $\bmod 998244353$.
  - **Statement & Formula**: By Goulden–Jackson cluster inclusion-exclusion on cyclic shifts of `"ABC"`, $[x^A y^B z^C] \frac{1 - xyz}{1 - (x + y + z) + 2xyz} = h(A, B, C) - h(A-1, B-1, C-1)$ where $h(A, B, C) = \sum_{k=0}^{\min(A,B,C)} (-2)^k \frac{(A+B+C-2k)!}{k!(A-k)!(B-k)!(C-k)!}$ in $O(A + B + C)$ time!
- **Problem 5A-32: Codeforces 1251F — Red-White Fence ($O(n)$ 2-Sparse Log-Derivative ODE)**
  - **URL**: `https://codeforces.com/problemset/problem/1251/F` | **Constraints**: $n, q \le 3 \times 10^5, k \le 5$, $\bmod 998244353$.
  - **Statement & Formula**: For each of the $k \le 5$ red boards $B$, if there are $c_1$ white board lengths $< B$ of multiplicity $1$ and $c_2$ of multiplicity $\ge 2$, the perimeter generating polynomial is $P_B(x) = (1 + 2x)^{c_1}(1 + x)^{2c_2}$, which satisfies $(1 + 3x + 2x^2) P_B'(x) = \big(2(c_1 + c_2) + (2c_1 + 4c_2)x\big) P_B(x)$, unrolling $P_B(x)$ in $O(n)$ time with zero NTTs!
- **Problem 5A-33: Codeforces 960G — Bandit Blues**: Cross-ref **Problem 1A-23** ($\binom{A+B-2}{A-1} \left[\begin{matrix} n-1 \\ A+B-2 \end{matrix}\right] = \binom{A+B-2}{A-1}[x^{A+B-2}] x^{\overline{n-1}}$ via D&C NTT or Taylor-shift doubling).
- **Problem 5A-34: AtCoder AGC 005 F — Many Easy Problems**
  - **URL**: `https://atcoder.jp/contests/agc005/tasks/agc005_f` | **Constraints**: $n \le 2 \times 10^5$, $\bmod 924844033$ ($g = 5$).
  - **Statement & Formula**: Sum of minimal spanning subtree sizes over all $k$-vertex subsets $S \subseteq V$ is $\text{Ans}_k = n\binom{n}{k} - \sum_{s=k}^{n-1} c_s \binom{s}{k}$ where $c_s$ counts directed subtree components of size $s$, evaluated for all $k = 1, \dots, n$ via a single reversed NTT convolution modulo $924844033$ in $O(n \log n)$ time!

---

## 11. Wave 5B Problem Encyclopedia: Tree FPS (HLD + D&C), Transposition Principle, Composition/Projection, $q$-Analogues & Set/Dirichlet Series (`cohort3_wave_5b_tree_fps_transposition_compose_q.md`)

> **Full Reference**: See `fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md`, Section 10 (Lines 1430–3160).

### Cluster A: Tree FPS via Heavy-Light Decomposition + Divide-and-Conquer NTT (Problems 5B-A1 to 5B-A20)

- **Problem 5B-A1: AtCoder ABC 269 Ex — Antichain** (`Stepping Stone`)
  - **URL**: `https://atcoder.jp/contests/abc269/tasks/abc269_h` | **Constraints**: $N \le 2 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: For a rooted tree $T$ on $N$ vertices, for each $k = 1, \dots, N$, count antichains of size $k$ ($f_u(x) = x + \prod_{v \in \text{children}(u)} f_v(x)$). Decompose into Heavy-Light chains: along a heavy chain $u_1, \dots, u_L$, first multiply the light children of each $u_i$ into $g_i(x)$ via a min-heap / D&C product tree; then solve the affine chain recurrence $f_{u_i}(x) = x + g_i(x) f_{u_{i+1}}(x)$ via a $2 \times 2$ or $(P_L, Q_L)$ binary product tree in $O(N \log^2 N)$ total time!
- **Problem 5B-A2: Luogu P4389 — 付公主的背包 (Princess's Knapsack)** (`Stepping Stone`): Cross-ref **Problem 1A-7a** and **Problem 5A-2** (Harmonic $\ln / \exp$ subset-product knapsack).
- **Problem 5B-A3: AtCoder ABC 355 G — Baseball** (`Intermediate`)
  - **URL**: `https://atcoder.jp/contests/abc355/tasks/abc355_g` | **Constraints**: $N, K \le 5 \times 10^4$, $\bmod 998244353$.
  - **Statement & Formula**: Laminar interval containment tree + Static Top Tree (`Compress` / `Rake` $2 \times 2$ boundary polynomial matrices) in $O(N \log^2 N)$ time!
- **Problem 5B-A4: Luogu P7279 — 光棱碎片 (Prism Shards)** (`Intermediate`)
  - **URL**: `https://www.luogu.com.cn/problem/P7279` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: $2 \times 2$ polynomial transfer matrix multiplication along Heavy-Light chains via D&C NTT in $O(N \log^2 N)$ time.
- **Problem 5B-A5: Luogu P3784 — [SDOI2017] 遗忘的集合 (Forgotten Set)** (`Intermediate`): Cross-ref **Problem 1A-17** (Inverse Euler transform via polynomial $\ln$ + Möbius inversion).
- **Problem 5B-A6: Luogu P4719 — 【模板】动态 DP (Offline Polynomial Matrix Perspective)** (`Intermediate`)
  - **URL**: `https://www.luogu.com.cn/problem/P4719` | **Constraints**: $N \le 10^5$.
  - **Statement & Formula**: Independent set / matching generating polynomial on a tree via $2 \times 2$ HLD transfer matrices $\begin{pmatrix} g_{u, 0}(x) & g_{u, 0}(x) \\ g_{u, 1}(x) & 0 \end{pmatrix}$ multiplied along heavy paths in $O(N \log^2 N)$ time.
- **Problem 5B-A7: Codeforces 438E — The Child and Binary Tree** (`Intermediate`): Cross-ref **Problem 1A-10** (Rooted binary tree quadratic FPS $\frac{2}{1+\sqrt{1-4C(x)}}$).
- **Problem 5B-A8: Luogu P3781 / P4381 — [SDOI2017] 切树游戏 (Tree Cutting Game)** (`Advanced`)
  - **URL**: `https://www.luogu.com.cn/problem/P3781` | **Constraints**: $N, Q \le 3 \times 10^4, V < 128$, $\bmod 10007$.
  - **Statement & Formula**: Count connected subtrees with XOR sum $k$ under dynamic vertex updates. Apply FWT of length $128$ to convert XOR convolution into pointwise multiplication, and maintain Globally Balanced BST / heavy-light chains using the **Zero-Count Ring** $(v, c) \equiv v \cdot 0^c$ so dividing by a light child when $F_v(\omega) \equiv 0 \pmod{10007}$ simply decrements $c$ instead of dividing by zero!
- **Problem 5B-A9: Codeforces 1553I — Stairs** (`Advanced`): Cross-ref **Problem 4A-P16** ($2 \times 2$ polynomial matrix D&C + inclusion-exclusion).
- **Problem 5B-A10: Codeforces 1906J — Count BFS Graphs** (`Advanced`): Cross-ref **Problem 2B-B4** (BFS queue interval/tree DP + prefix-sum generating function).
- **Problem 5B-A11: Luogu P5281 — [ZJOI2019] Minimax 搜索** (`Mastery`): Cross-ref **Problem 2B-E12** (De Morgan depth-parity normalization + Static Top Tree / Global BST sweep with zero-divisor tracking).
- **Problem 5B-A12: Codeforces 1510H — Hard Optimization** (`Mastery`)
  - **URL**: `https://codeforces.com/problemset/problem/1510/H` | **Constraints**: $N \le 2000$.
  - **Statement & Formula**: Disjoint subsegment selection on a laminar interval tree via $2 \times 2$ boundary-endpoint state $(\text{left free/used}, \text{right free/used})$ Minkowski sum / polynomial convolution on the tree.
- **Problem 5B-A13: Luogu P5326 — [ZJOI2019] 开关 (Switches)** (`Mastery`): Cross-ref **Problem 2B-E10** (EGF/OGF first-passage ratio + D&C NTT).
- **Problem 5B-A14: Codeforces 1097G — Vladislav and a Great Legend** (`Mastery`): Cross-ref **Problem 2B-A14** and **Problem 5A-19** ($O(NK)$ Stirling power $(1+x)$ tree knapsack).
- **Problem 5B-A15: Codeforces 2006E — Iris's Full Binary Tree** (`Mastery`)
  - **URL**: `https://codeforces.com/problemset/problem/2006/E` | **Constraints**: $N \le 2 \times 10^5$.
  - **Statement & Formula**: Centroid / heavy-path tree depth optimization maintained dynamically across incremental vertex insertions in $O(N \log^2 N)$ time.
- **Problem 5B-A16: Codeforces 1613F — Tree Coloring** (`Mastery`): Cross-ref **Problem 1B-21** (Out-degree star factorization $\prod_{u=1}^N (1 + c_u x)$ + D&C NTT + inclusion-exclusion).
- **Problem 5B-A17: AtCoder AGC 005 F — Many Easy Problems** (`Mastery`): Cross-ref **Problem 5A-34** (Subtree complement contribution + reversed binomial NTT modulo $924844033$).
- **Problem 5B-A18: Luogu P5327 — [ZJOI2019] 语言 (Language)** (`Mastery`)
  - **URL**: `https://www.luogu.com.cn/problem/P5327` | **Constraints**: $N, M \le 10^5$.
  - **Statement & Formula**: Maintain the size of the union of Steiner trees of paths passing through each vertex $u$ via Euler-tour segment tree merging in $O(N \log^2 N)$ time.
- **Problem 5B-A19: Luogu P3348 — [ZJOI2016] 大森林 (Great Forest)** (`Mastery`)
  - **URL**: `https://www.luogu.com.cn/problem/P3348` | **Constraints**: $N, M \le 10^5$.
  - **Statement & Formula**: Offline sweep-line across trees $1 \dots N$ using Link-Cut Tree auxiliary virtual nodes to re-hang subtrees in $O(M \log N)$ time.
- **Problem 5B-A20: UOJ 424 — [集训队作业2018] count** (`Mastery`): Cross-ref **Problem 5A-29** (Bounded left-depth Cartesian tree rational OGF $\frac{Q_m(x)}{Q_{m+1}(x)}$).

---

### Cluster B: Tellegen's Transposition Principle, Multipoint Evaluation & Interpolation (Problems 5B-B1 to 5B-B17)

- **Problem 5B-B1: Codeforces 923E — Perpetual Subtraction** (`Stepping Stone`): Cross-ref **Problem 2A-2** (Middle Product `mulT` spectral diagonalization of backward binomial transitions).
- **Problem 5B-B2: AtCoder ABC 300 Ex — Fibonacci: Revisited** (`Intermediate`): Cross-ref **Problem 2A-4** and **Problem 5A-22** (Bostan–Mori negacyclic frequency half-swap).
- **Problem 5B-B3: AtCoder ARC 136 F — Flip Cells** (`Intermediate`): Cross-ref **Problem 2A-5** (EGF first-hit ratio + rational sum of fractions).
- **Problem 5B-B4: AtCoder AGC 038 E — Gachapon** (`Intermediate`): Cross-ref **Problem 2B-E11** (Min-Max inclusion-exclusion + 2D EGF knapsack).
- **Problem 5B-B5: Luogu P5284 — [十二省联考2019] 字符串问题** (`Intermediate`)
  - **URL**: `https://www.luogu.com.cn/problem/P5284` | **Constraints**: $\sum |S| \le 2 \times 10^5$.
  - **Statement & Formula**: Suffix Automaton parent-tree persistent optimization for longest path in prefix-dominance DAG in $O(N \log N)$ time.
- **Problem 5B-B6: Luogu P4705 — 玩游戏 (Playing Games)** (`Advanced`): Cross-ref **Problem 1A-24** (Power-sum generating function $A(x) = n - x \frac{Q'(x)}{Q(x)}$ via D&C NTT product tree + `ln`).
- **Problem 5B-B7: Codeforces 623E — Transforming Sequence** (`Advanced`): Cross-ref **Problem 1B-23** (Geometric variable scaling $F_A(2^B x) F_B(x)$ + 3-prime NTT / MTT).
- **Problem 5B-B8: Codeforces 1770G — Koxia and Bracket** (`Advanced`)
  - **URL**: `https://codeforces.com/problemset/problem/1770/G` | **Constraints**: $|S| \le 2.5 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count minimum bracket removals via **Transposed Divide-and-Conquer NTT**: when a linear DP transition on $[l, r]$ reduces the degree of the state vector from $r - l$ as we descend the recursion tree, run `mulT` top-down on the recursion tree in $O(N \log^2 N)$ time!
- **Problem 5B-B9: Codeforces 1810G — The Maximum Prefix** (`Advanced`): Cross-ref **Problem 3A-9** (Backwards absorption DP + transposed linear functional extraction).
- **Problem 5B-B10: Luogu P5158 — 【模板】多项式快速插值 (Algorithmic Deep-Dive)** (`Advanced`)
  - **URL**: `https://www.luogu.com.cn/problem/P5158` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Subproduct tree $M_{u}(x) = \prod (x - x_i)$ + Bostan–Lecerf–Schost `mulT` multipoint evaluation of $M'(x_i)$ + bottom-up linear combination $\sum \frac{y_i}{M'(x_i)} \frac{M(x)}{x - x_i}$ in $O(N \log^2 N)$ time.
- **Problem 5B-B11: Codeforces 1264D2 — Beautiful Bracket Sequence (Hard Version)** (`Advanced`): Cross-ref **Problem 4A-P12** (Vandermonde identity collapse on pivot split).
- **Problem 5B-B12: UOJ 182 — `a^-1 + b problem`** (`Mastery`)
  - **URL**: `https://uoj.ac/problem/182` | **Constraints**: $N, M \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Apply a sequence of $M$ operations ($x \gets x + b$ and $x \gets x^{-1}$) to $a_1, \dots, a_N$ and output $\sum_{i=1}^N a_i$ after each step. Compose the $2 \times 2$ Möbius matrices $\begin{pmatrix} \alpha_t & \beta_t \\ \gamma_t & \delta_t \end{pmatrix}$ so $a_i^{(t)} = \frac{\alpha_t a_i + \beta_t}{\gamma_t a_i + \delta_t} = \frac{\alpha_t}{\gamma_t} + \frac{\beta_t - \alpha_t \delta_t / \gamma_t}{\gamma_t a_i + \delta_t}$. Evaluating $\sum_{i=1}^N \frac{1}{a_i + c_t}$ for all $t = 1, \dots, M$ reduces to computing $P(x) = \prod_{i=1}^N (x + a_i)$ and evaluating $\frac{P'(-c_t)}{P(-c_t)}$ at the $M$ query points $-c_1, \dots, -c_M$ via **Multipoint Evaluation** in $O((N + M) \log^2 N)$ time!
- **Problem 5B-B13: Luogu P7440 — [KrOI2021] Feux Follets** (`Mastery`)
  - **URL**: `https://www.luogu.com.cn/problem/P7440` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Apply **Tellegen's Transposition Principle** to a $2 \times 2$ polynomial matrix product tree using middle products (`mulT`) in $O(N \log^2 N)$ time with $1/3$ the NTT overhead of remainder-tree division!
- **Problem 5B-B14: Luogu P5853 — Stirling & Falling Factorial Matrix Transpose** (`Mastery`)
  - **URL**: `https://www.luogu.com.cn/problem/P5853` | **Constraints**: $N \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Basis conversion between monomial, falling-factorial, and Stirling bases via transposed subproduct tree + middle product (`mulT`) in $O(N \log^2 N)$ time.
- **Problem 5B-B15: Codeforces 1988F — Heartbeat (Prefix-Suffix Maximum DP via Transposition)** (`Mastery`)
  - **URL**: `https://codeforces.com/problemset/problem/1988/F` | **Constraints**: $N \le 700$ (or $N \le 10^5$ D&C NTT variant), $\bmod 998244353$.
  - **Statement & Formula**: Split permutations at the global maximum $N$ (as in **Problem 1A-23**), decoupling prefix maxima on the left and suffix maxima on the right via transposed convolution.
- **Problem 5B-B16: QOJ 6504 / LibreOJ 171 — Power Projection** (`Mastery`): Cross-ref **Problem 4A-P26** (Kinoshita–Li 2D Graeffe parity splitting $[x^{n-1}] g(x) f(x)^k$ in $O(n \log^2 n)$ time).
- **Problem 5B-B17: Codeforces 1842I — Tenzing and Necklace** (`Mastery`)
  - **URL**: `https://codeforces.com/problemset/problem/1842/I` | **Constraints**: $N, K \le 5 \times 10^5$.
  - **Statement & Formula**: Circular $k$-cut minimum cost partition solved via Monge / WQS / SMAWK + CDQ divide-and-conquer.

---

### Cluster C: Kinoshita–Li $O(N \log^2 N)$ FPS Composition & Power Projection (Problems 5B-C1 to 5B-C16)

- **Problem 5B-C1: AtCoder ABC 387 G — Prime Circuit** (`Stepping Stone`): Cross-ref **Problem 4A-P21** ($O(N \log^2 N)$ `fps_compose` / $O(N \log N)$ Lagrange Inversion on prime-cycle cactus EGF).
- **Problem 5B-C2: AtCoder ABC 230 Ex — Bullseye** (`Stepping Stone`): Cross-ref **Problem 5A-20** (Euler transform $B(x) = W(x)\exp(\sum B(x^k)/k)$).
- **Problem 5B-C3: Luogu P5268 / Subset Sum Product & EGF Exp-Ln** (`Stepping Stone`): Logarithmic derivative & Newton `exp` warmup.
- **Problem 5B-C4: AtCoder ABC 222 H — Beautiful Binary Tree** (`Intermediate`): Cross-ref **Problem 1A-13** and **Problem 5A-5** (Composite Lagrange Inversion $[u^{N-1}] H'(u)\Phi(u)^N$).
- **Problem 5B-C5: AtCoder ABC 336 G — 16 Integers** (`Intermediate`): Cross-ref **Problem 4B-16** (De Bruijn graph Eulerian tours via BEST Theorem).
- **Problem 5B-C6: Library Checker — `compositional_inverse_of_formal_power_series` (Algorithmic Benchmark)** (`Intermediate`): Cross-ref **T18** (Brent–Kung / Lagrange Inversion for $N \le 8000$).
- **Problem 5B-C7: AtCoder ABC 281 Ex — Alchemy** (`Advanced`): Cross-ref **Problem 2B-B12** (Falling-factorial EGF + semi-relaxed D&C NTT).
- **Problem 5B-C8: AtCoder ARC 154 F — Dice Game** (`Advanced`): Cross-ref **Problem 4A-P23** (Taylor shift + Kinoshita–Li `fps_compose(R, e^t - 1)`).
- **Problem 5B-C9: Luogu P5434 — 有标号荒漠计数 (Labeled Cactus Forest)** (`Advanced`): Cross-ref **Problem 1A-27** and **Problem 3A-27** ($O(N \log^2 N)$ `compositional_inverse` on cactus EGF $T(x) = x\exp(T + \frac{T^2}{2(1-T)})$).
- **Problem 5B-C10: Library Checker — `compositional_inverse_of_formal_power_series_large` (Algorithmic Benchmark)** (`Advanced`): Cross-ref **T18** (Kinoshita–Li Power Projection + $\frac{n}{k} p_k$ for $N \le 131072$).
- **Problem 5B-C11: Luogu P5809 — Latest / Compositional Inverse Application** (`Advanced`): Cross-ref **T42** (Implicit tree/graph EGF via series reversion).
- **Problem 5B-C12: Luogu P5827 — 点双连通图计数 (All-$N$ Biconnected Labeled Graphs)** (`Mastery`): Cross-ref **Problem 3A-40** (To compute $[y^n] B(y)$ for **all** $n = 1, \dots, N$ simultaneously from $R(x) = x e^{B'(R(x))}$, compute $R^{\langle -1 \rangle}(y)$ via Kinoshita–Li Power Projection + Lagrange Inversion, then apply `fps_ln` $B'(y) = \ln\frac{y}{R^{\langle -1 \rangle}(y)}$ in $O(N \log^2 N)$ time!).
- **Problem 5B-C13: Luogu P5828 — 边双连通图计数 (All-$N$ 2-Edge-Connected Labeled Graphs)** (`Mastery`): Cross-ref **Problem 3A-40** (Bridge-block tree $R(x) = B_{\text{2e}}(x e^{R(x)}) \implies B_{\text{2e}}(y) = R(y e^{-B_{\text{2e}}(y)})$ solved for all $n \le N$ via Kinoshita–Li series reversion in $O(N \log^2 N)$ time!).
- **Problem 5B-C14: Codeforces 1967E2 — Again Counting Arrays (Hard Version)** (`Mastery`): Cross-ref **Problem 3A-4** (Reflection principle + Catalan rational substitution).
- **Problem 5B-C15: Codeforces 1349F2 — Slime and Sequences (Hard Version)** (`Mastery`): Cross-ref **Problem 5A-27** (Bivariate Eulerian GF + Lagrange Inversion + `mulT`).
- **Problem 5B-C16: AtCoder AGC 058 D — Yet Another ABC String** (`Mastery`): Cross-ref **Problem 5A-31** (Goulden–Jackson cluster GF $\frac{1-xyz}{1-(x+y+z)+2xyz}$).

---

### Cluster D: Chirp-$Z$ Transform, Sequential Lagrange Shift & $O(\sqrt{P}\log P)$ Factorial (Problems 5B-D1 to 5B-D11)

- **Problem 5B-D1: AtCoder ARC 033 D — 多項式 (Seen At)** (`Stepping Stone`)
  - **URL**: `https://atcoder.jp/contests/arc033/tasks/arc033_4` | **Constraints**: $N \le 10^5$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Given $P(0), P(1), \dots, P(N)$ for a degree-$N$ polynomial, evaluate $P(T)$ in **$O(N)$ time** via prefix/suffix products of $(T - i)$ and precomputed factorials $(-1)^{N-i} / (i!(N-i)!)$.
- **Problem 5B-D2: Codeforces 451E — Devu and Flowers** (`Stepping Stone`): Cross-ref **Problem 1A-3** (Bounded-box inclusion-exclusion $\prod_{i=1}^n (1 - x^{f_i+1}) (1-x)^{-n}$).
- **Problem 5B-D3: Luogu P3321 — [SDOI2015] 序列统计 (Sequence Statistics)** (`Intermediate`)
  - **URL**: `https://www.luogu.com.cn/problem/P3321` | **Constraints**: $N \le 10^9, M \le 8000$ (prime), $\bmod 1004535809$.
  - **Statement & Formula**: Count length-$N$ sequences from $S \subseteq \{1, \dots, M-1\}$ (prime $M$) with product $\equiv X \pmod M$. Take discrete logarithms base a primitive root $g$ of $\mathbb{F}_M^\times$ to convert multiplication $\bmod M$ into cyclic addition $\bmod (M - 1)$, solved via cyclic NTT binary exponentiation in $O(M \log M \log N)$ time!
- **Problem 5B-D4: Codeforces 1054H — Epic Convolution** (`Intermediate`): Cross-ref **Problem 2A-37** (Bluestein CZT + CRT order reduction modulo $490019 - 1 = 2 \times 491 \times 499$).
- **Problem 5B-D5: Luogu P5293 / LOJ 3058 — [HNOI2019] 白兔之舞 (White Rabbit's Dance)** (`Advanced`): Cross-ref **Problem 2A-36** ($3 \times 3$ matrix roots-of-unity filter + arbitrary-length Bluestein CZT).
- **Problem 5B-D6: Codeforces 995F — Cowmpany Cowmpensation** (`Intermediate`)
  - **URL**: `https://codeforces.com/problemset/problem/995/F` | **Constraints**: $N \le 3000, D \le 10^9$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Assign salaries $1 \le s_u \le D$ on an $N$-node tree so $s_u \le s_{\text{parent}(u)}$. By induction, $dp_u(D)$ is a polynomial in $D$ of degree at most $N$; compute $dp_{\text{root}}(1), \dots, dp_{\text{root}}(N + 1)$ in $O(N^2)$ time and evaluate at $D$ in $O(N)$ time via sequential Lagrange interpolation!
- **Problem 5B-D7: Luogu P7116 — [NOIP2020] 微信步数 (WeChat Steps)** (`Advanced`): Cross-ref **Problem 1B-17** (Walk bounding-box periodicity + Faulhaber / sequential Lagrange interpolation).
- **Problem 5B-D8: Luogu P5668 — Polynomial $N$-Step Shift & Sampling Evaluation** (`Advanced`)
  - **URL**: `https://www.luogu.com.cn/problem/P5668` | **Constraints**: $N \le 10^5$.
  - **Statement & Formula**: Given $P(0), P(1), \dots, P(N)$, compute $P(c), P(c+1), \dots, P(c+N)$ in **$O(N \log N)$ time** via a single NTT convolution:
    $$P(c + k) = \left(\prod_{j=0}^N (c + k - j)\right) \sum_{i=0}^N \left(\frac{(-1)^{N-i} P(i)}{i! (N - i)!}\right) \frac{1}{c + k - i}$$
- **Problem 5B-D9: AtCoder ARC 153 D — Sum of Sum of Digits** (`Intermediate`)
  - **URL**: `https://atcoder.jp/contests/arc153/tasks/arc153_d` | **Constraints**: $N \le 2 \times 10^5, A_i < 10^9$.
  - **Statement & Formula**: Radix-carry suffix ordering digit DP: at digit position $d$, the set of numbers generating a carry depends only on the suffix modulo $10^d$, which forms a contiguous prefix after sorting by $A_i \bmod 10^d$.
- **Problem 5B-D10: Codeforces 901E — Periodicovsky** (`Mastery`)
  - **URL**: `https://codeforces.com/problemset/problem/901/E` | **Constraints**: $N \le 10^5$.
  - **Statement & Formula**: Recover a periodic signal from cyclic squared distances $\sum_{j=0}^{N-1} (b_{(j+k)\bmod N} - a_j)^2$ by applying Bluestein's Chirp-$Z$ Transform over a prime $P \equiv 1 \pmod N$ to invert the length-$N$ cyclic cross-correlation!
- **Problem 5B-D11: LibreOJ 161 / Luogu P5282 — 【模板】快速阶乘算法 ($N! \bmod P$ in $O(\sqrt{P} \log P)$)** (`Mastery`)
  - **URL**: `https://www.luogu.com.cn/problem/P5282` | **Constraints**: $N < P \le 2^{31}-1$.
  - **Statement & Formula**: Set $v = \lfloor\sqrt{N}\rfloor$ and define the block product $G_d(x) = \prod_{j=1}^d (x + j)$. Starting from $G_1(0), G_1(v)$, use the **Shift of Sampling Points** (**Problem 5B-D8**) at each doubling step $d \to 2d$ to compute $G_v(0), G_v(v), G_v(2v), \dots, G_v((v-1)v)$ in $O(\sqrt{N} \log N)$ time, then multiply the $v$ blocks and the $\le v$ remainder terms!

---

### Cluster E: $q$-Analogues, $q$-Binomials, Euler's Pentagonal Theorem & Gaussian $q$-Series (Problems 5B-E1 to 5B-E9)

- **Problem 5B-E1: Codeforces 1603F — October 18, 2017** (`Stepping Stone`)
  - **URL**: `https://codeforces.com/problemset/problem/1603/F` | **Constraints**: $N, K \le 10^7$, $\bmod 998244353$.
  - **Statement & Formula**: Count length-$N$ arrays over $[0, 2^K)$ whose subsets cannot XOR to $x$.
    - For $x = 0$: the $N$ elements must be linearly independent over $\mathbb{F}_2$, giving $\prod_{i=0}^{N-1} (2^K - 2^i)$.
    - For $x \neq 0$: by symmetry all $2^K - 1$ nonzero values have the same count, so sum over the dimension $r$ of the span via the $q$-binomial coefficient $\left[\begin{matrix} K \\ r \end{matrix}\right]_2$ in $O(\min(N, K))$ time!
- **Problem 5B-E2: AtCoder ABC 278 Ex — make 1** (`Mastery`)
  - **URL**: `https://atcoder.jp/contests/abc278/tasks/abc278_h` | **Constraints**: $A \le B \le 10^{18}, B - A \le 2 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Count binary matrices of rank/span constraints over $n \in [A, B]$ using **$q$-Binomial Inversion** $\prod_{i=0}^{k-1} (1 + q^i x) = \sum_{j=0}^k q^{\binom{j}{2}} \left[\begin{matrix} k \\ j \end{matrix}\right]_q x^j$ and $\prod_{i=0}^{k-1} (1 - q^i x)^{-1} = \sum_{j \ge 0} \left[\begin{matrix} k + j - 1 \\ j \end{matrix}\right]_q x^j$ ($q = 2$) combined with Bluestein CZT on $2^{-n}$ in $O((B - A + K) \log(B - A))$ time!
- **Problem 5B-E3: AtCoder ARC 145 F — Modulo Sum of Increasing Sequences** (`Advanced`): Cross-ref **Problem 4B-33** ($\left[\begin{matrix} N+M \\ N \end{matrix}\right]_q \bmod (q^P - 1)$ via $q$-Lucas theorem & orbit decomposition).
- **Problem 5B-E4: AtCoder ARC 139 F — Many Xor Optimization Problems** (`Mastery`)
  - **URL**: `https://atcoder.jp/contests/arc139/tasks/arc139_f` | **Constraints**: $N, M \le 2.5 \times 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: Sum the maximum XOR subset value over all $2^{NM}$ arrays of $N$ integers in $[0, 2^M)$. Group by the Reduced Row Echelon Form (RREF) pivot columns $1 \le p_1 < \dots < p_r \le M$ of the basis using $q$-binomial weights $\left[\begin{matrix} N \\ r \end{matrix}\right]_2$ ($q = 2$) and compute the expectation in $O(M + N)$ time!
- **Problem 5B-E5: Luogu P5366 — [SNOI2017] 遗失的答案 (Lost Answer)** (`Advanced`)
  - **URL**: `https://www.luogu.com.cn/problem/P5366` | **Constraints**: $N, G, L \le 10^8, Q \le 10^5$.
  - **Statement & Formula**: Count subsets of divisors in $[1, N]$ with $\gcd = G$ and $\operatorname{lcm} = L$ by encoding prime-exponent min/max boundary touches as a $2\omega(L/G)$-bit mask ($\le 16$ bits) and running OR-FWT with prefix/suffix exclusion of single divisors in $O(D \cdot 2^{2\omega} + Q)$ time!
- **Problem 5B-E6: Codeforces 1916F — Group Division** (`Advanced`)
  - **URL**: `https://codeforces.com/problemset/problem/1916/F` | **Constraints**: $n_1 + n_2 \le 2000$.
  - **Statement & Formula**: Partition a biconnected graph $G$ into two connected induced subgraphs of sizes $n_1$ and $n_2$ by Maintain-Biconnectivity / Block-Cut Tree non-cut-vertex leaf extraction in $O(N(N + M))$ time.
- **Problem 5B-E7: QOJ 5097 / SOJ 703 — 布尔立方 (Boolean Cube)** (`Mastery`)
  - **URL**: `https://qoj.ac/problem/5097` | **Constraints**: $n \le 10^5$, $\bmod 998244353$.
  - **Statement & Formula**: High-dimensional $\mathbb{F}_2^n$ subspace intersection enumeration via $q$-Möbius inversion $\mu_q(U, V) = (-1)^d q^{\binom{d}{2}}$, $q$-falling factorials, and Bluestein's Chirp-$Z$ Transform in $O(n \log n)$ time!
- **Problem 5B-E8: Codeforces 1336E2 — Chiori and Doll Picking (Hard Version)** (`Mastery`): Cross-ref **Problem 4A-P17** (Linear basis dual code $C^\perp$ + MacWilliams Krawtchouk transform in $O(2^{\min(r, m-r)} + m^3)$ time).
- **Problem 5B-E9: AtCoder ARC 134 E — Modulo Nim** (`Advanced`)
  - **URL**: `https://atcoder.jp/contests/arc134/tasks/arc134_e` | **Constraints**: $N \le 200, A_i \le 200$, $\bmod 998244353$.
  - **Statement & Formula**: Modulo Nim game states rapidly reduce to multiples of $12$ in $\{12, 24, \dots, 192\}$ ($16$ possible values), whose closure under modulo reduction is solved via $2^{16}$ subset DP!

---

### Cluster F: Set Power Series ($\exp$, $\ln$, Subset Convolution) & Dirichlet Generating Functions (Problems 5B-F1 to 5B-F10)

- **Problem 5B-F1: AtCoder ABC 213 G — Connectivity 2** (`Stepping Stone`): Cross-ref **Problem 1B-24** (Connected subgraphs via $O(N^2 2^N)$ ranked Set Power Series $\ln$).
- **Problem 5B-F2: Luogu P4841 — [集训队作业2013] 城市规划 (City Planning)** (`Stepping Stone`): Cross-ref **Problem 1A-9a** and **Problem 5A-3** (Symmetric $K_n$ univariate EGF logarithm $\ln G(x)$ vs Set Power Series $\ln_{\text{subset}} G(x)$).
- **Problem 5B-F3: LibreOJ 154 — 集合幂级数的指数、对数与幂 (SPS Calculus)** (`Intermediate`)
  - **URL**: `https://loj.ac/p/154` | **Constraints**: $n \le 20$, $\bmod 998244353$.
  - **Statement & Formula**: Ranked Zeta transform $\hat{F}_k(S) = \sum_{T \subseteq S, |T|=k} F_T$ maps subset convolution to degree-$n$ truncated polynomial multiplication $\mathbb{F}_p[z]/(z^{n+1})$ at each of the $2^n$ masks, enabling $\exp, \ln,$ and $\text{pow}$ of Set Power Series in $O(n^2 2^n)$ time via point-value ODEs!
- **Problem 5B-F4: AtCoder ABC 253 Ex — We Love Forest** (`Advanced`)
  - **URL**: `https://atcoder.jp/contests/abc253/tasks/abc253_h` | **Constraints**: $N \le 14, M \le 500$, $\bmod 998244353$.
  - **Statement & Formula**: Given a multigraph $G$ on $N \le 14$ vertices, for each $k = 1, \dots, N-1$, find the probability that $k$ random edges form a forest. First compute $t(S)$ (spanning trees on subset $S$) for all $\emptyset \neq S \subseteq V$ using Matrix-Tree / Set Power Series. A forest of $k$ edges on $N$ vertices has exactly $N - k$ connected tree components, so compute $\frac{1}{(N-k)!} [x^V y^{N-k}] T(x)^y$ via ranked subset convolution in $O(N^3 2^N)$ time!
- **Problem 5B-F5: AtCoder ABC 306 Ex — Balance Scale** (`Advanced`)
  - **URL**: `https://atcoder.jp/contests/abc306/tasks/abc306_h` | **Constraints**: $N \le 17, M \le \binom{N}{2}$, $\bmod 998244353$.
  - **Statement & Formula**: Given $M$ balance comparisons on $N \le 17$ weights, count assignments of $\{<, >, =\}$ consistent with some total preorder. Contracting `$=$`-components leaves a DAG on the super-vertices! By Robinson–Stanley source inclusion-exclusion on the subset lattice (**Problem 3A-34**), an independent set of contracted components of size $c(S)$ has weight $(-1)^{c(S) - 1}$, so the Set Power Series is $F(x) = \frac{1}{1 - A(x)}$, inverted in $O(N^2 2^N)$ time via ranked subset inversion!
- **Problem 5B-F6: Codeforces 1326F2 — Wise Men (Hard Version)** (`Advanced`): Cross-ref **Problem 2B-C4** (Ranked Zeta transform + integer partition $p(N)$ compression + IFWT).
- **Problem 5B-F7: UOJ 94 — [集训队互测2015] 胡策的统计** (`Mastery`)
  - **URL**: `https://uoj.ac/problem/94` | **Constraints**: $N \le 20$, $\bmod 998244353$.
  - **Statement & Formula**: Sum $k!(c - 1)!$ or $c!$-weighted connected component / biconnected partitions over all spanning subgraphs of $G$ ($N \le 20$). Compute the connected subgraph Set Power Series $C(x) = \ln_{\text{subset}} G(x)$ via $O(N^2 2^N)$ ranked Möbius transform + point-value ODE $C' = G' / G$, then apply polynomial composition $\sum_{k \ge 1} k! \frac{C(x)^k}{k!} = \frac{1}{1 - C(x)}$ (or vertex-by-vertex SPS $\ln$ for biconnectivity) in the ranked point-value ring!
- **Problem 5B-F8: Luogu P5325 — 【模板】Min_25 筛 (Bell Series & Powerful Number Perspective)** (`Intermediate`)
  - **URL**: `https://www.luogu.com.cn/problem/P5325` | **Constraints**: $N \le 10^{10}$, $\bmod (10^9+7)$.
  - **Statement & Formula**: Prefix sum $\sum_{n=1}^N f(n)$ for multiplicative $f(p^k) = p^k(p^k - 1)$ via Min_25 sieve or Powerful Number (PN) Bell series division $B_p(h)(x) = B_p(f)(x) / B_p(g)(x)$ in $O(N^{3/4}/\log N)$ or $O(N^{2/3})$ time.
- **Problem 5B-F9: LibreOJ 6729 — 幂数 (Powerful Numbers & Dirichlet $\exp / \ln$)** (`Intermediate`)
  - **URL**: `https://loj.ac/p/6729` | **Constraints**: $N \le 10^{11}$.
  - **Statement & Formula**: Grade the Dirichlet series by $\Omega(n)$ (total prime factors with multiplicity) and apply **Dirichlet $\ln$ and $\exp$** ($\Omega(n) f(n) = (g * f)(n)$) on the $\lfloor N / i \rfloor$ quotient ring / Powerful Numbers!
- **Problem 5B-F10: AtCoder ABC 288 Ex — A Nameless Counting Problem** (`Mastery`)
  - **URL**: `https://atcoder.jp/contests/abc288/tasks/abc288_h` | **Constraints**: $N \le 200, M, X \le 2^{30}-1$, $\bmod 998244353$.
  - **Statement & Formula**: Count non-decreasing sequences $0 \le A_1 \le \dots \le A_N \le M$ with $A_1 \oplus \dots \oplus A_N = X$ by reducing non-decreasing tuples to unordered tuples via XOR-cancel parity decomposition (canceling pairs of equal elements leaves $c \equiv N \pmod 2$ strictly increasing elements) + digit DP!

---

## 12. Master Consolidated Rejected Template Problems Reference Table (Excluded from Pedagogical Ladders)

In strict compliance with the textbook's anti-template-bloat policy, bare library-verification tasks that test only black-box polynomial / FPS algebra without combinatorial modeling or nontrivial algebraic reduction are **excluded** from the pedagogical chapter ladders (Sections 2–11) and consolidated below as **implementation unit tests** for the textbook's C++ engines:

| # | Platform & Problem ID | Title & Direct URL | Target Engine Unit-Tested | Rejection Rationale | Wave(s) Flagged |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T1** | **Library Checker** | `convolution_mod` ([link](https://judge.yosupo.jp/problem/convolution_mod)) | 998244353 NTT | Bare $A(x) B(x) \bmod 998244353$ convolution check. | 1B, 2A |
| **T2** | **Library Checker** | `convolution_mod_1000000007` ([link](https://judge.yosupo.jp/problem/convolution_mod_1000000007)) | 3-Prime NTT / MTT | Bare arbitrary-modulus convolution check. | 1B, 2A |
| **T3** | **Library Checker** | `inv_of_formal_power_series` ([link](https://judge.yosupo.jp/problem/inv_of_formal_power_series)) | Dense Newton `inv` | Bare $A(x)^{-1} \bmod x^N$ unit test. | 1A, 1B, 3B, 5A |
| **T4** | **Library Checker** | `exp_of_formal_power_series` ([link](https://judge.yosupo.jp/problem/exp_of_formal_power_series)) | Dense Newton / CDQ `exp` | Bare $\exp(A(x)) \bmod x^N$ unit test. | 1A, 3B, 5A |
| **T5** | **Library Checker** | `log_of_formal_power_series` ([link](https://judge.yosupo.jp/problem/log_of_formal_power_series)) | Dense `ln` ($\int A'/A$) | Bare $\ln(A(x)) \bmod x^N$ unit test. | 1A, 3B, 5A |
| **T6** | **Library Checker** | `sqrt_of_formal_power_series` ([link](https://judge.yosupo.jp/problem/sqrt_of_formal_power_series)) | Dense Newton `sqrt` + Cipolla | Bare $A(x)^{1/2} \bmod x^N$ unit test. | 1A, 2A, 3B, 5A |
| **T7** | **Library Checker** | `pow_of_formal_power_series` ([link](https://judge.yosupo.jp/problem/pow_of_formal_power_series)) | Dense `pow` + valuation shift | Bare $A(x)^M \bmod x^N$ unit test. | 1A, 2A, 3B, 5A |
| **T8** | **Library Checker** | `inv_of_formal_power_series_sparse` ([link](https://judge.yosupo.jp/problem/inv_of_formal_power_series_sparse)) | `SparseFPS::inv` ($O(NK)$) | Bare sparse inversion unit test ($K \le 10, N \le 10^6$). | 5A |
| **T9** | **Library Checker** | `exp_of_formal_power_series_sparse` ([link](https://judge.yosupo.jp/problem/exp_of_formal_power_series_sparse)) | `SparseFPS::exp` ($O(NK)$) | Bare sparse exponential unit test via $E' = A' E$. | 5A |
| **T10** | **Library Checker** | `log_of_formal_power_series_sparse` ([link](https://judge.yosupo.jp/problem/log_of_formal_power_series_sparse)) | `SparseFPS::ln` ($O(NK)$) | Bare sparse logarithm unit test via $L' = A' / A$. | 5A |
| **T11** | **Library Checker** | `sqrt_of_formal_power_series_sparse` ([link](https://judge.yosupo.jp/problem/sqrt_of_formal_power_series_sparse)) | `SparseFPS::sqrt` ($O(NK)$) | Bare sparse square root unit test via $2 A B' = A' B$. | 5A |
| **T12** | **Library Checker** | `pow_of_formal_power_series_sparse` ([link](https://judge.yosupo.jp/problem/pow_of_formal_power_series_sparse)) | `SparseFPS::pow` ($O(NK)$) | Bare sparse power unit test via $A B' = M A' B$. | 5A |
| **T13** | **Library Checker** | `polynomial_taylor_shift` ([link](https://judge.yosupo.jp/problem/polynomial_taylor_shift)) | `taylor_shift` ($A(x+c)$) | Bare Taylor shift convolution check. | 2A, 5B |
| **T14** | **Library Checker** | `shift_of_sampling_points_of_polynomial` ([link](https://judge.yosupo.jp/problem/shift_of_sampling_points_of_polynomial)) | Sequential Lagrange Shift | Bare $P(0..N) \mapsto P(c..c+M)$ unit test. | 5B |
| **T15** | **Library Checker** | `multipoint_evaluation` ([link](https://judge.yosupo.jp/problem/multipoint_evaluation)) | `mulT` Multipoint Eval | Bare $P(x_1), \dots, P(x_M)$ evaluation check. | 5B |
| **T16** | **Library Checker** | `polynomial_interpolation` ([link](https://judge.yosupo.jp/problem/polynomial_interpolation)) | D&C Lagrange Interpolation | Bare $(x_i, y_i) \mapsto P(x)$ interpolation check. | 5B |
| **T17** | **Library Checker** | `composition_of_formal_power_series` / `_large` ([link](https://judge.yosupo.jp/problem/composition_of_formal_power_series_large)) | Kinoshita–Li `compose` | Bare $F(G(x)) \bmod x^N$ unit test. | 3A, 3B, 4A, 5B |
| **T18** | **Library Checker** | `compositional_inverse_of_formal_power_series` / `_large` ([link](https://judge.yosupo.jp/problem/compositional_inverse_of_formal_power_series_large)) | Power Projection + Lagrange | Bare $F^{\langle -1 \rangle}(x) \bmod x^N$ unit test. | 3A, 3B, 4A, 5B |
| **T19** | **Library Checker** | `kth_term_of_linearly_recurrent_sequence` ([link](https://judge.yosupo.jp/problem/kth_term_of_linearly_recurrent_sequence)) | Bostan–Mori | Bare $[x^K] P(x)/Q(x)$ linear recurrence check. | 1B, 4A |
| **T20** | **Library Checker** | `find_linear_recurrence` ([link](https://judge.yosupo.jp/problem/find_linear_recurrence)) | Berlekamp–Massey | Bare shortest LFSR discovery check. | 4A |
| **T21** | **Library Checker** | `stirling_number_of_the_first_kind` / `_second_kind` | Stirling Row NTT | Bare single-row Stirling S1 / S2 generation. | 1A, 2A |
| **T22** | **Library Checker** | `partition_function` ([link](https://judge.yosupo.jp/problem/partition_function)) | Pentagonal Number Inversion | Bare $\prod (1-x^k)^{-1} \bmod x^N$ unit test. | 1A, 2A, 5B |
| **T23** | **Library Checker** | `sharp_p_subset_sum` ([link](https://judge.yosupo.jp/problem/sharp_p_subset_sum)) | Harmonic $\ln$-$\exp$ | Bare $\prod (1 + x^{s_i}) \bmod x^{T+1}$ unit test. | 1A, 2A |
| **T24** | **Library Checker** | `subset_convolution` / `exp_of_set_power_series` | Ranked Subset Zeta/Mobius | Bare $O(N^2 2^N)$ Set Power Series unit test. | 5B |
| **T25** | **Luogu P3803** | 【模板】多项式乘法 (FFT) ([link](https://www.luogu.com.cn/problem/P3803)) | FFT / NTT | Bare polynomial multiplication check. | 1B |
| **T26** | **Luogu P4238** | 【模板】多项式乘法逆 ([link](https://www.luogu.com.cn/problem/P4238)) | Newton `inv` | Bare $A(x)^{-1} \bmod x^N$ check. | 1B, 3B, 5A |
| **T27** | **Luogu P4239** | 任意模数多项式乘法逆 ([link](https://www.luogu.com.cn/problem/P4239)) | MTT + Newton `inv` | Bare $A(x)^{-1} \bmod (x^N, 10^9+7)$ check. | 2A |
| **T28** | **Luogu P4512** | 【模板】多项式除法 ([link](https://www.luogu.com.cn/problem/P4512)) | Reversal + `inv` | Bare $A(x) = Q(x)B(x) + R(x)$ division check. | 1B, 5B |
| **T29** | **Luogu P4721** | 【模板】分治 FFT ([link](https://www.luogu.com.cn/problem/P4721)) | `cdq_semi_online` | Bare $f_i = \sum_{j=1}^i f_{i-j} g_j$ unit test. | 1B, 5A |
| **T30** | **Luogu P4723** | 【模板】常系数齐次线性递推 ([link](https://www.luogu.com.cn/problem/P4723)) | Bostan–Mori | Bare linear recurrence $[x^N] P/Q$ check. | 1B, 4A |
| **T31** | **Luogu P4725** | 【模板】多项式对数函数 (多项式 ln) ([link](https://www.luogu.com.cn/problem/P4725)) | Dense `ln` | Bare $\ln A(x) \bmod x^N$ check. | 1A, 2A, 5A |
| **T32** | **Luogu P4726** | 【模板】多项式指数函数 (多项式 exp) ([link](https://www.luogu.com.cn/problem/P4726)) | Dense `exp` | Bare $\exp A(x) \bmod x^N$ check. | 1A, 2A, 5A |
| **T33** | **Luogu P5050** | 【模板】多项式多点求值 ([link](https://www.luogu.com.cn/problem/P5050)) | `mulT` Multipoint Eval | Bare multipoint evaluation check. | 5B |
| **T34** | **Luogu P5158** | 【模板】多项式快速插值 ([link](https://www.luogu.com.cn/problem/P5158)) | D&C Interpolation | Bare fast interpolation check. | 5B |
| **T35** | **Luogu P5205** | 【模板】多项式开根 ([link](https://www.luogu.com.cn/problem/P5205)) | Dense `sqrt` | Bare $A(x)^{1/2} \bmod x^N$ check ($a_0 = 1$). | 1A, 2A, 5A |
| **T36** | **Luogu P5245** | 【模板】多项式快速幂 ([link](https://www.luogu.com.cn/problem/P5245)) | Dense `pow` | Bare $A(x)^K \bmod x^N$ check ($a_0 = 1$). | 1A, 2A, 5A |
| **T37** | **Luogu P5273** | 【模板】多项式幂函数 (加强版) ([link](https://www.luogu.com.cn/problem/P5273)) | Valuation-shifted `pow` | Bare $A(x)^K \bmod x^N$ with arbitrary leading term. | 2A, 5A |
| **T38** | **Luogu P5277** | 【模板】多项式开根 (加强版) ([link](https://www.luogu.com.cn/problem/P5277)) | Cipolla + `sqrt` | Bare $A(x)^{1/2} \bmod x^N$ with quadratic residue $a_0$. | 2A, 3B |
| **T39** | **Luogu P5373** | 【模板】多项式复合函数 ([link](https://www.luogu.com.cn/problem/P5373)) | Brent–Kung / Kinoshita–Li | Bare $F(G(x)) \bmod x^N$ check. | 3A, 5B |
| **T40** | **Luogu P5395 / P5396 / P5408 / P5409** | 第二类/第一类斯特林数·行/列 | Stirling Row/Col NTT | Bare Stirling number row/column generation. | 2A |
| **T41** | **Luogu P5488** | 差分与前缀和 ([link](https://www.luogu.com.cn/problem/P5488)) | $(1 \pm x)^{\pm k} \bmod x^N$ | Bare binomial convolution with $(1-x)^{-k}$. | 1B, 5A |
| **T42** | **Luogu P5809** | 【模板】多项式复合逆 ([link](https://www.luogu.com.cn/problem/P5809)) | Lagrange Inversion | Bare compositional inverse $F^{\langle -1 \rangle}(x)$ check. | 3A, 5B |
| **T43** | **AtCoder `fps_24_b` / `c` / `e` / `i` / `j` / `p` / `u`** | Educational FPS Bare Drills | Elementary FPS Ops | Direct one-line definitions without secondary reduction (used as inline text examples rather than end-of-chapter problems). | 1A, 2A |
| **T44** | **Luogu P6115** | 【模板】整式递推 ([link](https://www.luogu.com.cn/problem/P6115)) | P-Recursive BSGS Matrix Eval | Bare $O(\sqrt{N}\log N)$ P-recursive sequence evaluation check. | 5A |
| **T45** | **Luogu P7439** | 【模板】常系数齐次线性递推 (加强版) ([link](https://www.luogu.com.cn/problem/P7439)) | Bit-Reversed Bostan–Mori | Bare constant-factor NTT optimization check for Bostan–Mori. | 4A |
| **T46** | **yukicoder 2677** | Simple Linear Recurrence ([link](https://yukicoder.me/problems/no/2677)) | Bostan–Mori | Bare linear recurrence $[x^N] P(x)/Q(x)$ template check. | 4A |
| **T47** | **Library Checker** | `power_projection_of_formal_power_series` ([link](https://judge.yosupo.jp/problem/power_projection_of_formal_power_series)) | Kinoshita–Li `power_projection` | Bare $[x^{n-1}] g(x) f(x)^k$ for $0 \le k < n$ unit test. | 4A, 5B |
| **T48** | **Library Checker** | `multivariate_convolution` ([link](https://judge.yosupo.jp/problem/multivariate_convolution)) | Twisted Kronecker $\chi$-Graded Mul | Bare $d$-variate truncated polynomial multiplication check. | 4A |
| **T49** | **Codeforces 632E** | Thief in a Shop ([link](https://codeforces.com/problemset/problem/632/E)) | 1D Boolean Subset-Sum FFT | Bare 1D boolean polynomial power $(\sum x^{a_i})^k$ check. | 4A |
| **T50** | **AtCoder ABC 130 E** | Common Subsequence ([link](https://atcoder.jp/contests/abc130/tasks/abc130_e)) | Elementary 2D Prefix-Sum DP | Introductory $O(NM)$ DP requiring no FPS machinery. | 4A |
| **T51** | **SPOJ FIBOSUM** | Fibonacci Sum ([link](https://www.spoj.com/problems/FIBOSUM/)) | $2 \times 2$ Matrix Exponentiation | Bare Fibonacci prefix-sum $F_{n+2}-1$ warmup. | 4A |
| **T52** | **Library Checker** | `static_top_tree` / `point_set_tree_path_composite` | Static Top Tree (`Compress`/`Rake`) | Bare tree DP maintenance template without polynomial algebra. | 5B |
| **T53** | **Luogu P5808** | 【模板】多项式复合逆 ([link](https://www.luogu.com.cn/problem/P5808)) | Lagrange Inversion | Duplicate bare compositional inverse template check. | 5B |
| **T54** | **Luogu P5748** | 集合划分计数 ([link](https://www.luogu.com.cn/problem/P5748)) | Dense `exp` ($\exp(e^x - 1)$) | Bare Bell number EGF generation check. | 1A, 5B |
| **T55** | **Library Checker** | `multipoint_evaluation_on_geometric_sequence` ([link](https://judge.yosupo.jp/problem/multipoint_evaluation_on_geometric_sequence)) | Bluestein Chirp-$Z$ Transform | Bare $P(a r^k)$ geometric multipoint evaluation unit test. | 2A, 5B |
| **T56** | **Luogu P6800** | 【模板】Chirp Z-Transform ([link](https://www.luogu.com.cn/problem/P6800)) | Bluestein Chirp-$Z$ Transform | Bare Chirp-$Z$ Transform template check. | 2A, 5B |
| **T57** | **Luogu P5667** | 【模板】拉格朗日插值2 (连续点值平移) ([link](https://www.luogu.com.cn/problem/P5667)) | Sequential Lagrange Shift | Bare $P(0..N) \mapsto P(m..m+N)$ convolution check. | 5B |
| **T58** | **Library Checker** | `q_binomial_coefficient_prime_mod` | Gaussian $q$-Binomial $\left[\begin{smallmatrix}n\\k\end{smallmatrix}\right]_q$ | Bare $q$-factorial / $q$-Lucas prime-modulus check. | 5B |
| **T59** | **Library Checker** | `power_projection_of_set_power_series` ([link](https://judge.yosupo.jp/problem/power_projection_of_set_power_series)) | Transposed SPS Composition | Bare Set Power Series power projection unit test. | 5B |
| **T60** | **Library Checker** | `polynomial_composite_set_power_series` ([link](https://judge.yosupo.jp/problem/polynomial_composite_set_power_series)) | Elegia $O(n^2 2^n)$ SPS Compose | Bare polynomial composition over a Set Power Series check. | 5B |
| **T61** | **AtCoder Typical90 #050 / ABC 129 C** | Stair Jump / Typical Stairs | Elementary 1D Linear DP | Introductory $O(N)$ Fibonacci-style stair DP warmup. | 1B |
| **T62** | **CSES 1633 / 1634 / 1635 / 1636** | Dice & Coin Combinations I–II | Elementary 1D Knapsack DP | Introductory $O(NK)$ coin change DP without FPS reduction. | 1B |
| **T63** | **Codeforces 474D** | Flowers ([link](https://codeforces.com/problemset/problem/474/D)) | Prefix-Summed Linear Recurrence | Elementary $f_n = f_{n-1} + f_{n-k}$ DP warmup. | 1B |
| **T64** | **HDU 1028 / POJ 1664** | Ignatius and the Princess III | $O(N^2)$ Partition DP | Elementary integer partition table for $N \le 120$. | 1A, 2A |
| **T65** | **HDU 1521 / HDU 2082** | 排列组合 / 找单词 | $O(N^2)$ Polynomial Multiplication | Introductory small-degree OGF/EGF expansion for $N \le 50$. | 1A |
| **T66** | **Luogu P2000** | 拯救世界 ([link](https://www.luogu.com.cn/problem/P2000)) | BigInt $\binom{n+4}{4}$ | Closed-form $\binom{n+4}{4}$ reducing to BigInt multiplication. | 1A |
| **T67** | **POJ 3734** | Blocks ([link](http://poj.org/problem?id=3734)) | 4-Color Parity EGF | Elementary $4^{n-1} + 2^{n-1}$ modular exponentiation warmup. | 1A |
| **T68** | **Codeforces 696E / HLD Templates** | Bare Tree Path Maintenance | Heavy-Light Decomposition | Pure data-structure path query without FPS algebra. | 2B, 5B |
| **T69** | **Luogu P3389** | 【模板】高斯消元法 ([link](https://www.luogu.com.cn/problem/P3389)) | $O(N^3)$ Gaussian Elimination | Bare linear system solver template check. | 2B |
| **T70** | **Luogu P4781** | 【模板】拉格朗日插值 ([link](https://www.luogu.com.cn/problem/P4781)) | $O(N^2)$ Lagrange Interpolation | Bare single-point Lagrange interpolation check. | 2B, 5B |
| **T71** | **Library Checker** | `inv_of_polynomials` ([link](https://judge.yosupo.jp/problem/inv_of_polynomials)) | Polynomial Extended GCD | Bare polynomial modular inverse $A(x)^{-1} \bmod B(x)$ check. | 3A, 3B |
| **T72** | **Luogu P3807** | 【模板】卢卡斯定理 ([link](https://www.luogu.com.cn/problem/P3807)) | Lucas's Theorem $\binom{n}{m} \bmod p$ | Bare Lucas theorem binomial residue check. | 4A, 5B |
