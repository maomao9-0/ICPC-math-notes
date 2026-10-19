# Network Flows & Modelling Textbook — Master Authoring & Phase 3 Global Audit Report

**Audit Date**: 2026-10-20  
**Scope**: Complete `flows/` Quarto Textbook (`36` `.qmd` files, `43,000+` lines), `flows_research/` Corpus (`40` Phase 1/1.5 files + `11` Phase 3 audit files = `51` research/audit documents), and `tests/audit_flows_models.py` (`24` exact mathematical oracles + `36`-file hygiene verifier).  
**Status**: **100% COMPLETE — ALL 24 MATHEMATICAL ORACLES & 36 FILE HYGIENE CHECKS PASSED (`0` ERRORS)**

---

## 1. Executive Summary of the Three-Phase Pipeline

| Pipeline Phase | Deliverable Scope | Total Files | Total Lines | Verification & Sign-Off |
| :--- | :--- | :---: | :---: | :--- |
| **Phase 1: Deep Multilingual Domain Research (`Iterations 01–115`)** | 5 Specialist Cohorts (`Foundations`, `Bipartite/Matching/Posets`, `Pseudo-Boolean Min-Cut Compiler`, `MCMF/Equation Differencing/LP Duality`, `DS Flow/Blossom/Simulated MCMF/Isotonic`) + 35 Multilingual Deep-Dive Reports (`EN`, `ZH`, `JA`, `RU`) | `32` `.md` files | `48,234` lines (`5.64 MB`) | [`flows_research/AUDIT_REPORT.md`](AUDIT_REPORT.md) (**PASS**) |
| **Phase 1.5: Curriculum Architecture & 320-Problem Curation** | 24-Chapter Master Curriculum Blueprint (`CURRICULUM_ARCHITECTURE.md`), 320-Problem Master Archive (`#001`–`#320`) + 45-Problem Quarantine Ledger (`R-01`–`R-45`), 4-Step Non-Graph-to-Flow Compilation Framework | `8` `.md` files | `11,095` lines (`1.86 MB`) | [`flows_research/PHASE_1_5_SIGNOFF.md`](PHASE_1_5_SIGNOFF.md) (**PASS**) |
| **Phase 2: Quarto Textbook Authoring (`flows/`)** | 4 Front-Matter pages (`index`, `notation`, `study-plan`, `sources`), 24 Core Chapters (`Ch 01`–`Ch 24`), 6 Blind Part Checkpoints (`CP-I`–`CP-VI`), and 2 Capstones (`synthesis-reserve`, `problem-archive-guide`) + Website Integration (`_quarto.yml`, root `index.qmd`) | `36` `.qmd` files | `43,000+` lines (`3.5+ MB`) | `python3 tests/audit_flows_models.py` (**36 / 36 PASS**) |
| **Phase 3: 10-Iteration Global Audit & Exact Math Oracles** | 10 Global Audit Reports (`flows_research/audits/phase3_iter01..10.md`) + `tests/audit_flows_models.py` (`24 / 24` exact mathematical oracles) + `quarto render` verification | `11` `.md` files + `1` `.py` test suite | `2,500+` lines | **100% PASS (`0` errors)** |

---

## 2. Complete Inventory of the 36 Authored `flows/` Textbook Files

### 2.1 Front-Matter (`4` files)

| File Path | Title / Role | Status |
| :--- | :--- | :---: |
| [`flows/index.qmd`](../flows/index.qmd) | **Network Flows, Minimum Cuts, Matching & Duality Modelling** — Textbook Landing Portal, 6-Part Architecture & 4-Step Compilation Workflow | **PASS** |
| [`flows/notation.qmd`](../flows/notation.qmd) | **Notation, Cut Conventions & Graph Primitives** — Global Partition Convention Lock ($x_i = [i \in S]$), Residual Capacities, Potentials & Multilingual Glossary | **PASS** |
| [`flows/study-plan.qmd`](../flows/study-plan.qmd) | **Study Plan & Diagnostic Triage Tracks** — 4 Reader Tracks, Complexity Triage Table & Blind Checkpoint Protocol | **PASS** |
| [`flows/sources.qmd`](../flows/sources.qmd) | **Multilingual Sources, Papers & Problem Archives** — Annotated Bibliography across `[EN]`, `[ZH]`, `[JA]`, `[RU]` | **PASS** |

### 2.2 Part I — Flow Foundations, Residual Anatomy & Conservation Compilers (`Ch 01`–`Ch 04` + `CP-I`)

| Chapter / Checkpoint | File Path | Problems | Math Oracle | Status |
| :--- | :--- | :---: | :--- | :---: |
| **Chapter 1** | [`flows/chapters/ch01-conservation-residual-maxflow-mincut.qmd`](../flows/chapters/ch01-conservation-residual-maxflow-mincut.qmd) | `#001`–`#008` | `oracle_ch01_maxflow_mincut_canonical()` | **PASS** |
| **Chapter 2** | [`flows/chapters/ch02-residual-anatomy-cut-edges-rollback.qmd`](../flows/chapters/ch02-residual-anatomy-cut-edges-rollback.qmd) | `#009`–`#016` | `oracle_ch02_residual_scc_and_rollback()` | **PASS** |
| **Chapter 3** | [`flows/chapters/ch03-vertex-splitting-time-layered-path-decomposition.qmd`](../flows/chapters/ch03-vertex-splitting-time-layered-path-decomposition.qmd) | `#017`–`#024` | `oracle_ch03_vertex_splitting_dining()` | **PASS** |
| **Chapter 4** | [`flows/chapters/ch04-lower-bounds-circulations-matrix-rounding.qmd`](../flows/chapters/ch04-lower-bounds-circulations-matrix-rounding.qmd) | `#025`–`#032` | `oracle_ch04_lower_bound_minflow()` | **PASS** |
| **Checkpoint I** | [`flows/checkpoints/cp01-part1-foundations.qmd`](../flows/checkpoints/cp01-part1-foundations.qmd) | `#193`–`#200` | Hygiene & Link Audit | **PASS** |

### 2.3 Part II — Bipartite Matching, König Duality, Dulmage–Mendelsohn & Posets (`Ch 05`–`Ch 08` + `CP-II`)

| Chapter / Checkpoint | File Path | Problems | Math Oracle | Status |
| :--- | :--- | :---: | :--- | :---: |
| **Chapter 5** | [`flows/chapters/ch05-bipartite-matching-konig-mvc-mis.qmd`](../flows/chapters/ch05-bipartite-matching-konig-mvc-mis.qmd) | `#033`–`#040` | `oracle_ch05_konig_mvc_extraction()` | **PASS** |
| **Chapter 6** | [`flows/chapters/ch06-grid-parity-dulmage-mendelsohn-games.qmd`](../flows/chapters/ch06-grid-parity-dulmage-mendelsohn-games.qmd) | `#041`–`#048` | `oracle_ch06_dulmage_mendelsohn_game()` | **PASS** |
| **Chapter 7** | [`flows/chapters/ch07-birkhoff-von-neumann-row-col-edge-coloring.qmd`](../flows/chapters/ch07-birkhoff-von-neumann-row-col-edge-coloring.qmd) | `#049`–`#056` | `oracle_ch07_birkhoff_von_neumann()` | **PASS** |
| **Chapter 8** | [`flows/chapters/ch08-poset-dilworth-hall-flow-elimination.qmd`](../flows/chapters/ch08-poset-dilworth-hall-flow-elimination.qmd) | `#057`–`#064` | `oracle_ch08_dilworth_transitive_closure()` | **PASS** |
| **Checkpoint II** | [`flows/checkpoints/cp02-part2-bipartite-matching-duality.qmd`](../flows/checkpoints/cp02-part2-bipartite-matching-duality.qmd) | `#201`–`#208` | Hygiene & Link Audit | **PASS** |

### 2.4 Part III — The Minimum Cut Compiler (`燃やす埋める`): Closure, Submodularity, Bipartite Inversion, Multi-State Chains & Coarea (`Ch 09`–`Ch 13` + `CP-III`)

| Chapter / Checkpoint | File Path | Problems & User Flagships | Math Oracle | Status |
| :--- | :--- | :---: | :--- | :---: |
| **Chapter 9** | [`flows/chapters/ch09-maximum-weight-closure-project-selection.qmd`](../flows/chapters/ch09-maximum-weight-closure-project-selection.qmd) | `#065`–`#072` | `oracle_ch09_closure_and_arc085e()` | **PASS** |
| **Chapter 10** | [`flows/chapters/ch10-pseudo-boolean-cuts-submodularity-burn-bury.qmd`](../flows/chapters/ch10-pseudo-boolean-cuts-submodularity-burn-bury.qmd) | `#073`–`#080` | `oracle_ch10_submodular_and_clause_hub()` | **PASS** |
| **Chapter 11** | [`flows/chapters/ch11-bipartite-variable-inversion-supermodular-rescue.qmd`](../flows/chapters/ch11-bipartite-variable-inversion-supermodular-rescue.qmd) | `#081`–`#088` (**Flagship #1: `AGC 038 F`**) | `oracle_ch11_bipartite_inversion_and_agc038f()` | **PASS** |
| **Chapter 12** | [`flows/chapters/ch12-multi-state-unary-chains-threshold-cuts.qmd`](../flows/chapters/ch12-multi-state-unary-chains-threshold-cuts.qmd) | `#089`–`#096` (**Flagships #2 & #3: `ARC 107 F`, `ARC 142 E`**) | `oracle_ch12_unary_chains_arc107f_arc142e()` | **PASS** |
| **Chapter 13** | [`flows/chapters/ch13-ishikawa-convex-penalties-coarea-parametric-cuts.qmd`](../flows/chapters/ch13-ishikawa-convex-penalties-coarea-parametric-cuts.qmd) | `#097`–`#104` (**Flagship #4: `CF 1427 G`**) | `oracle_ch13_coarea_and_cf1427g()` | **PASS** |
| **Checkpoint III** | [`flows/checkpoints/cp03-part3-mincut-compiler.qmd`](../flows/checkpoints/cp03-part3-mincut-compiler.qmd) | `#209`–`#216` | Hygiene & Link Audit | **PASS** |

### 2.5 Part IV — Fractional Cuts, Planar Duality, Cut DP & Gomory–Hu Trees (`Ch 14`–`Ch 16` + `CP-IV`)

| Chapter / Checkpoint | File Path | Problems | Math Oracle | Status |
| :--- | :--- | :---: | :--- | :---: |
| **Chapter 14** | [`flows/chapters/ch14-fractional-programming-maximum-density-subgraphs.qmd`](../flows/chapters/ch14-fractional-programming-maximum-density-subgraphs.qmd) | `#105`–`#112` | `oracle_ch14_dinkelbach_max_density()` | **PASS** |
| **Chapter 15** | [`flows/chapters/ch15-planar-cycle-cut-duality-shortest-paths.qmd`](../flows/chapters/ch15-planar-cycle-cut-duality-shortest-paths.qmd) | `#113`–`#120` | `oracle_ch15_planar_dual_shortest_path()` | **PASS** |
| **Chapter 16** | [`flows/chapters/ch16-mincut-dp-global-mincut-gomory-hu-trees.qmd`](../flows/chapters/ch16-mincut-dp-global-mincut-gomory-hu-trees.qmd) | `#121`–`#128` | `oracle_ch16_gomory_hu_cut_tree()` | **PASS** |
| **Checkpoint IV** | [`flows/checkpoints/cp04-part4-density-planar-mincut-dp-gh.qmd`](../flows/checkpoints/cp04-part4-density-planar-mincut-dp-gh.qmd) | `#217`–`#224` | Hygiene & Link Audit | **PASS** |

### 2.6 Part V — Min-Cost Max-Flow, Convex Splitting, Equation Differencing & LP Duality (`Ch 17`–`Ch 21` + `CP-V`)

| Chapter / Checkpoint | File Path | Problems | Math Oracle | Status |
| :--- | :--- | :---: | :--- | :---: |
| **Chapter 17** | [`flows/chapters/ch17-mcmf-foundations-potentials-slope-negative-cycles.qmd`](../flows/chapters/ch17-mcmf-foundations-potentials-slope-negative-cycles.qmd) | `#129`–`#136` | `oracle_ch17_mcmf_slope_and_potentials()` | **PASS** |
| **Chapter 18** | [`flows/chapters/ch18-convex-marginal-splitting-degree-penalties-tournaments.qmd`](../flows/chapters/ch18-convex-marginal-splitting-degree-penalties-tournaments.qmd) | `#137`–`#144` | `oracle_ch18_convex_splitting_and_tournaments()` | **PASS** |
| **Chapter 19** | [`flows/chapters/ch19-k-interval-coverage-equation-difference-method.qmd`](../flows/chapters/ch19-k-interval-coverage-equation-difference-method.qmd) | `#145`–`#152` | `oracle_ch19_equation_differencing_volunteers()` | **PASS** |
| **Chapter 20** | [`flows/chapters/ch20-cycle-covers-dynamic-scheduling-resource-reuse-hubs.qmd`](../flows/chapters/ch20-cycle-covers-dynamic-scheduling-resource-reuse-hubs.qmd) | `#153`–`#160` | `oracle_ch20_reverse_queue_scheduling()` | **PASS** |
| **Chapter 21** | [`flows/chapters/ch21-lp-duality-totally-unimodular-matrices-polymatroids.qmd`](../flows/chapters/ch21-lp-duality-totally-unimodular-matrices-polymatroids.qmd) | `#161`–`#168` | `oracle_ch21_lp_duality_and_tu_potentials()` | **PASS** |
| **Checkpoint V** | [`flows/checkpoints/cp05-part5-mcmf-diff-equations-lp-duality.qmd`](../flows/checkpoints/cp05-part5-mcmf-diff-equations-lp-duality.qmd) | `#225`–`#232` | Hygiene & Link Audit | **PASS** |

### 2.7 Part VI & Capstones — DS-Accelerated Flow, Blossom, Simulated MCMF, Isotonic Regression & Archive (`Ch 22`–`Ch 24` + `CP-VI` + `2 Capstones`)

| Chapter / Capstone | File Path | Problems | Math Oracle | Status |
| :--- | :--- | :---: | :--- | :---: |
| **Chapter 22** | [`flows/chapters/ch22-ds-accelerated-flow-graphs-blossom-matching.qmd`](../flows/chapters/ch22-ds-accelerated-flow-graphs-blossom-matching.qmd) | `#169`–`#176` | `oracle_ch22_segtree_virtual_hub_flow()` | **PASS** |
| **Chapter 23** | [`flows/chapters/ch23-simulated-mcmf-regret-greedy-heap-segtree.qmd`](../flows/chapters/ch23-simulated-mcmf-regret-greedy-heap-segtree.qmd) | `#177`–`#184` | `oracle_ch23_simulated_mcmf_regret_heap()` | **PASS** |
| **Chapter 24** | [`flows/chapters/ch24-isotonic-regression-matroid-intersection-synthesis.qmd`](../flows/chapters/ch24-isotonic-regression-matroid-intersection-synthesis.qmd) | `#185`–`#192` | `oracle_ch24_isotonic_regression_threshold_cut()` | **PASS** |
| **Checkpoint VI** | [`flows/checkpoints/cp06-part6-ds-blossom-simulated-isotonic.qmd`](../flows/checkpoints/cp06-part6-ds-blossom-simulated-isotonic.qmd) | `#233`–`#240` | Hygiene & Link Audit | **PASS** |
| **Capstone 1** | [`flows/capstones/synthesis-reserve.qmd`](../flows/capstones/synthesis-reserve.qmd) | `#241`–`#320` (`Syn` & `Rev-01`–`Rev-14`) | Hygiene & Link Audit | **PASS** |
| **Capstone 2** | [`flows/capstones/problem-archive-guide.qmd`](../flows/capstones/problem-archive-guide.qmd) | Master Index `#001`–`#320` + Quarantine `R-01`–`R-45` | Hygiene & Link Audit | **PASS** |

---

## 3. Index of Phase 3 Global Audit Reports (`flows_research/audits/`)

1. **[Iteration 01 — Zero-Magic 4-Step Non-Graph-to-Flow Compilation Audit](audits/phase3_iter01_zero_magic_4step_compilation.md)**
2. **[Iteration 02 — Deep Audit of the Four User-Highlighted Benchmark Flagships (`AGC 038 F`, `ARC 107 F`, `ARC 142 E`, `CF 1427 G`)](audits/phase3_iter02_four_user_flagships_deep_audit.md)**
3. **[Iteration 03 — Pseudo-Boolean Cut Compiler (`燃やす埋める`), Multi-State Chains & Coarea Verification (`Ch 09`–`Ch 13`)](audits/phase3_iter03_pseudo_boolean_mincut_compiler.md)**
4. **[Iteration 04 — MCMF, Convex Marginal Splitting, Masao Iri's Equation Differencing & LP Duality (`Ch 17`–`Ch 21`)](audits/phase3_iter04_mcmf_equation_differencing_lp_duality.md)**
5. **[Iteration 05 — Direction B Flow Elimination (`Flow -> Non-Flow Fast Algorithm`) Across All 14 Archetypes (`Rev-01`–`Rev-14`)](audits/phase3_iter05_direction_b_flow_elimination.md)**
6. **[Iteration 06 — 25 Broken-Gadget Failure Modes & Counterexamples (`FM-01`–`FM-25`)](audits/phase3_iter06_broken_gadget_failure_modes_catalog.md)**
7. **[Iteration 07 — 320-Problem Archive Coverage, Multi-Judge Diversity & `AGENTS.md` Quarantine Audit (`R-01`–`R-45`)](audits/phase3_iter07_320_problem_archive_quarantine_audit.md)**
8. **[Iteration 08 — Notation, Terminology & Multilingual Convention Consistency (`flows/notation.qmd` vs. All 24 Chapters)](audits/phase3_iter08_notation_terminology_conventions.md)**
9. **[Iteration 09 — Pedagogical Pacing, Self-Contained Derivations & `AGENTS.md` Editorial Policy Compliance](audits/phase3_iter09_pedagogical_pacing_AGENTS_compliance.md)**
10. **[Iteration 10 — Automated Mathematical Oracle Suite (`tests/audit_flows_models.py`) & Quarto Build Sign-Off](audits/phase3_iter10_math_oracle_quarto_signoff.md)**
