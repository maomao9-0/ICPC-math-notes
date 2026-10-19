# Phase 3 Global Audit — Iteration 07: 320-Problem Archive Coverage, Multi-Judge Diversity & `AGENTS.md` Quarantine Audit

**Audit Date**: 2026-10-20  
**Scope**: [`flows_research/PROBLEM_CURATION.md`](../PROBLEM_CURATION.md), [`flows_research/problem_archive.md`](../problem_archive.md), [`flows/capstones/problem-archive-guide.qmd`](../../flows/capstones/problem-archive-guide.qmd), [`flows/capstones/synthesis-reserve.qmd`](../../flows/capstones/synthesis-reserve.qmd), and all 24 chapters + 6 checkpoints.  
**Audit Objective**: Verify that:
1. All **320 curated problems (`#001`–`#320`)** are accounted for across the 24 chapters (`192` problems `#001`–`#192`), 6 blind checkpoints (`48` problems `#193`–`#240`), Synthesis & Dual-Perspective Reserve (`80` problems `#241`–`#320`), and the Master Problem Archive Guide.
2. Every single one of the **45 naked library/template problems (`R-01`–`R-45`)** is strictly quarantined per [`AGENTS.md`](../../AGENTS.md) ("Do not add practice problems whose main task is copying, adapting, or validating a standard library routine. Library Checker and 'template' problems are normally excluded").

---

## 1. Accounting of the 320-Problem Master Archive (`#001`–`#320`)

| Problem Block | ID Range | Count | Textbook Location | Purpose & Pedagogical Role | Verification Status |
| :--- | :---: | :---: | :--- | :--- | :---: |
| **Part I: Flow Foundations & Structural Anatomy** | `#001`–`#032` | `32` (`8 × 4` chapters) | `Ch 01`–`Ch 04` | Conservation, Canonical Cut Extraction, Residual SCCs, Rollback, Vertex/Time Splitting, Lower-Bound Circulations & Matrix Rounding | **PASS** (`32 / 32`) |
| **Part II: Bipartite Matching, König, DM & Posets** | `#033`–`#064` | `32` (`8 × 4` chapters) | `Ch 05`–`Ch 08` | König MVC/MIS, Dulmage–Mendelsohn & Walk Games, Birkhoff–von Neumann & Edge Coloring, Dilworth Poset Chains & Hall Elimination | **PASS** (`32 / 32`) |
| **Part III: The Pseudo-Boolean Minimum Cut Compiler** | `#065`–`#104` | `40` (`8 × 5` chapters) | `Ch 09`–`Ch 13` | Max-Weight Closure, $2 \times 2$ Submodular & Higher-Order Clauses, Bipartite Inversion (`#087` **AGC 038 F**), Multi-State Chains (`#095` **ARC 107 F**, `#096` **ARC 142 E**), Ishikawa & Coarea (`#103` **CF 1427 G**) | **PASS** (`40 / 40`) |
| **Part IV: Fractional Cuts, Planar Duality & Cut Compression** | `#105`–`#128` | `24` (`8 × 3` chapters) | `Ch 14`–`Ch 16` | Dinkelbach & Goldberg Max-Density Subgraphs, Planar Cycle–Cut Duality & Dual Interval DP, Max-Flow $\to$ Min-Cut DP & Gomory–Hu Trees | **PASS** (`24 / 24`) |
| **Part V: Min-Cost Max-Flow, Equation Differencing & LP Duality** | `#129`–`#168` | `40` (`8 × 5` chapters) | `Ch 17`–`Ch 21` | MCMF Slope & Negative Cycles, Convex Marginal Splitting & Tournaments, Masao Iri's Equation Differencing, Dynamic Scheduling & 4-Hub Geometry, LP Duality & TU Matrices | **PASS** (`40 / 40`) |
| **Part VI: DS-Accelerated Flow, Blossom, Simulated MCMF & Isotonic** | `#169`–`#192` | `24` (`8 × 3` chapters) | `Ch 22`–`Ch 24` | Segment-Tree / Persistent DS Virtual Hub Graphs & Blossom, Simulated MCMF & Regret Greedy, $L_p$ Isotonic Regression & Matroid Intersection | **PASS** (`24 / 24`) |
| **Six Part Blind Checkpoints (`CP-I`–`CP-VI`)** | `#193`–`#240` | `48` (`8 × 6` checkpoints) | `cp01`–`cp06` | Untagged blind recognition problems + decoy boundary diagnostics | **PASS** (`48 / 48`) |
| **Synthesis & Dual-Perspective Reserve (`Capstones`)** | `#241`–`#320` | `80` | `synthesis-reserve.qmd` & `problem-archive-guide.qmd` | Multi-technique synthesis (`#241`–`#295`) and Dual-Perspective Bridges (`#296`–`#320`) | **PASS** (`80 / 80`) |
| **TOTAL** | **`#001`–`#320`** | **`320`** | **All 36 `.qmd` files** | **100% Non-Template Modelling & Recognition** | **100% PASS** |

---

## 2. Multi-Judge & Multilingual Ecosystem Distribution

The 320 curated problems span the entire international competitive programming ecosystem:
- **AtCoder (`AGC`, `ARC`, `ABC`, Educational DP)**: **56 problems** (including 3 of the 4 user-highlighted flagships: `AGC 038 F`, `ARC 107 F`, `ARC 142 E`, plus `AGC 031 E`, `AGC 034 D`, `AGC 029 F`, `ARC 085 E`, `ARC 106 E`, `ARC 125 E`, `ABC 193 F`, `ABC 259 G`, `ABC 326 G`, `ABC 347 G`, etc.).
- **Codeforces (Div. 1 / Global / Technocup / Gym)**: **94 problems** (including flagship `CF 1427 G — One Billion Shades of Grey`, `CF 724 E`, `CF 1919 F2`, `CF 865 D`, `CF 730 I`, `CF 436 E`, `CF 1517 G`, `CF 704 D`, `CF 1288 F`, `CF 343 E`, `CF 103 E`, `CF 311 E`, `CF 434 D`, etc.).
- **Chinese Olympiad & LuoguNetwork Flow 24 Classics (`网络流 24 题`, `NOI`, `WC`, `CTSC`, `ZJOI`, `SDOI`, `HNOI`, `SCOI`, `BJOI`, `AHOI`, `LOJ`, `UOJ`)**: **118 problems** (including all 24 of the `网络流 24 题` mapped to their exact modelling chapters, `[NOI2008] 志愿者招募`, `[NOI2009] 植物大战僵尸`, `[NOI2010] 海拔`, `[NOI2019] 序列`, `[HNOI2013] 切糕`, `[SCOI2007] 修车`, `[ZJOI2013] 防守战线`, `[WC2007] 剪刀石头布`, `UOJ #455 雪灾与外卖`, `[省选联考 2020] 魔法商店`, etc.).
- **ICPC World Finals, Regional Finals, SPOJ, POJ, UVa, TopCoder & Yukicoder**: **52 problems** (including `[ICPC WF 2018] Conquer The World`, `[NEERC 2016] Delight for a Cat`, `[CEOI 2008] Order`, `[BOI 2004] Sequence`, `UVA 1389 Hard Life`, `POJ 3469`, `TopCoder FoxAndCity`, `yukicoder 1541`, etc.).

---

## 3. Strict Verification of the 45 Quarantined Template Problems (`R-01`–`R-45`)

Per [`AGENTS.md`](../../AGENTS.md):
- **Zero** of the 45 naked library verification / template problems (`R-01` through `R-45`, including Library Checker `Maximum Flow`, `Bipartite Matching`, `Min Cost b-Flow`, `Assignment Problem`, `General Matching`, Luogu `P3376`, `P3381`, `P3386`, `P4722`, `P6113`, `P5192`, `LOJ #101`–`#102`, `LOJ #115`–`#117`, `AtCoder ACL Practice D/E`, `CSES Download Speed`, `School Dance`, etc.) appear as a chapter or checkpoint exercise in `#001`–`#320`.
- Instead, they are documented exclusively in the **Quarantined Template Reference Ledger** in [`flows/capstones/problem-archive-guide.qmd`](../../flows/capstones/problem-archive-guide.qmd) so readers know where to unit-test their pre-existing library before starting the modelling exercises.

---

## 4. Audit Conclusion

**Status**: **100% PASS**.
