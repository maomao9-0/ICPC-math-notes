# Network Flows, Minimum Cuts, Matching, Duality & Non-Graph Modelling Research Corpus (`flows_research/`)

This directory stores the cumulative multilingual research, bibliography, English-to-Graph modelling taxonomy, and problem audit records across 115+ iterative passes covering English (`[EN]`), Chinese (`[ZH]`), and Japanese (`[JA]`) competitive programming literature and online judges.

## Canonical Plan & Roadmap
- [`PLAN.md`](PLAN.md): **Master Implementation Plan & Multi-Cohort Research Roadmap** — Read this first! Defines the 4-stage pipeline, the **4-Step "Zero Magic Gadgets" English-to-Graph Compilation Standard**, problem curation rules, and the Cohort 1 / Cohort 2 / Cohort 3 file matrix.

## Cohort 1 Independent Research Files (Iterations 01–52 — `15,304` lines, `1.71 MB`)
- [`iter_01_to_05_foundations_residual_lower_bounds.md`](iter_01_to_05_foundations_residual_lower_bounds.md): Wave 1A (Iter 01–05) — Flow-Cut Duality, Residual Anatomy, Essential/Feasible Cut Edges, Dinic Complexity Regimes, Vertex/Time Gadgets, Demands & Lower Bounds (`上下界网络流`), Matrix Rounding & Mixed Eulerian Graphs.
- [`iter_06_to_10_bipartite_hall_dilworth_dm.md`](iter_06_to_10_bipartite_hall_dilworth_dm.md): Wave 1B (Iter 06–10) — Bipartite Matching, König's Duality, Dulmage–Mendelsohn (`DM`) Decomposition, Non-Graph Grid/Parity Bipartitions, Hall's Marriage Theorem & Segment Tree Eliminations, Dilworth's Theorem & DAG Path Covers.
- [`iter_11_to_15_mincut_closure_qpbo_bipartite_flip.md`](iter_11_to_15_mincut_closure_qpbo_bipartite_flip.md): Wave 2A (Iter 11–15) — Min-Cut as Binary Variable Assignment, Maximum Weight Closure (`最大权闭合子图`), Pairwise Pseudo-Boolean Optimization (`燃やす埋める`), Submodularity ($A+D \le B+C$), and Bipartite Variable Flipping (`AGC 038 F`).
- [`iter_16_to_20_multistate_monge_coarea_parametric.md`](iter_16_to_20_multistate_monge_coarea_parametric.md): Wave 2B (Iter 16–20) — Multi-State Ordered Vertex Chains (`K値燃やす埋める` / `切糕模型`), 3-State Sign/Deletion Cuts (`ARC 107 F`), Unary Threshold Layering & Disjunctive OR Cuts (`ARC 142 E`), Ishikawa Monge Cuts, and Coarea Level-Set Parametric Cuts (`CF 1427 G`).
- [`iter_21_to_25_density_planar_mincut_dp_gomory_hu.md`](iter_21_to_25_density_planar_mincut_dp_gomory_hu.md): Wave 3A (Iter 21–25) — 0-1 Fractional Programming, Maximum Density Subgraphs, Planar Graph Duality (`[NOI2010] 海拔`), Solving Max-Flow via Min-Cut DP (`CF 724 E`), Stoer–Wagner, and Gomory–Hu / Gusfield Cut Trees (`最小割树`).
- [`iter_26_to_30_mcmf_potentials_convex_diff_equations.md`](iter_26_to_30_mcmf_potentials_convex_diff_equations.md): Wave 3B (Iter 26–30) — SSP & Johnson Potentials, Zkw Primal–Dual, Convexity of $C(f)$ & WQS Binary Search, Negative-Cycle Saturation, Convex Marginal Edge Splitting (`凸费用拆边`), Interval $k$-Coverage, and Consecutive Equation Differencing (`[NOI2008] 志愿者招募`).
- [`iter_31_to_35_mcmf_cycles_dynamic_scheduling_ranks.md`](iter_31_to_35_mcmf_cycles_dynamic_scheduling_ranks.md): Wave 4A (Iter 31–35) — Disjoint Paths & Cycle Covers, Mixed Chinese Postman, Dynamic Lazy Vertex Generation (`[NOI2012] 美食节`), Resource Reuse (`餐巾计划`), 2D Prefix/Suffix Coordinate Ranks (`AGC 031 E`), and Manhattan Hub Linearization (`AGC 034 D`).
- [`iter_36_to_40_lp_duality_tu_matrices_submodular.md`](iter_36_to_40_lp_duality_tu_matrices_submodular.md): Wave 4B (Iter 36–40) — Explicit LP Primal–Dual Compilation (`LP对偶转网络流`), Complementary Slackness, Totally Unimodular (TU) Matrices, Consecutive-Ones Property (`连续 1 性质`), Submodular Function Minimization, and Matroid Intersection.
- [`iter_41_to_45_ds_graphs_simulated_mcmf_blossom.md`](iter_41_to_45_ds_graphs_simulated_mcmf_blossom.md): Wave 5A (Iter 41–45) — Data-Structure-Accelerated Flow Graphs (`线段树/主席树/KD-Tree优化建图`), Simulated Cost Flow (`模拟费用流` via Regret Heaps, Slope Trick, Segment Trees & Multi-Queue Transitions), Edmonds' Blossom Algorithm (`带花树`), Tutte–Berge, and Tutte Matrix.
- [`iter_46_to_52_isotonic_crossdomain_zh_ja_en_audit.md`](iter_46_to_52_isotonic_crossdomain_zh_ja_en_audit.md): Wave 5B (Iter 46–52) — $L_p$ Isotonic Regression (`保序回归` via Parallel Binary Search + Closure Min-Cut), Game/Geometry/Number-Theory Flow Bridges, and Exhaustive Multilingual (`[ZH]` 网络流 24 题 & 国家集训队论文 / `[JA]` AtCoder & 燃やす埋める / `[EN]` CF & ICPC WF) Audit.

## Cohort 2 Independent Redundant Research Files (Iterations 53–104 — `15,393` lines, `1.73 MB`)
- [`cohort2_iter_53_to_57_foundations_residual_lower_bounds.md`](cohort2_iter_53_to_57_foundations_residual_lower_bounds.md): Redundant Wave 1A (`1,542` lines)
- [`cohort2_iter_58_to_62_bipartite_hall_dilworth_dm.md`](cohort2_iter_58_to_62_bipartite_hall_dilworth_dm.md): Redundant Wave 1B (`1,564` lines)
- [`cohort2_iter_63_to_67_mincut_closure_qpbo_bipartite_flip.md`](cohort2_iter_63_to_67_mincut_closure_qpbo_bipartite_flip.md): Redundant Wave 2A (`1,605` lines)
- [`cohort2_iter_68_to_72_multistate_monge_coarea_parametric.md`](cohort2_iter_68_to_72_multistate_monge_coarea_parametric.md): Redundant Wave 2B (`1,433` lines)
- [`cohort2_iter_73_to_77_density_planar_mincut_dp_gomory_hu.md`](cohort2_iter_73_to_77_density_planar_mincut_dp_gomory_hu.md): Redundant Wave 3A (`1,621` lines)
- [`cohort2_iter_78_to_82_mcmf_potentials_convex_diff_equations.md`](cohort2_iter_78_to_82_mcmf_potentials_convex_diff_equations.md): Redundant Wave 3B (`1,511` lines)
- [`cohort2_iter_83_to_87_mcmf_cycles_dynamic_scheduling_ranks.md`](cohort2_iter_83_to_87_mcmf_cycles_dynamic_scheduling_ranks.md): Redundant Wave 4A (`1,419` lines)
- [`cohort2_iter_88_to_92_lp_duality_tu_matrices_submodular.md`](cohort2_iter_88_to_92_lp_duality_tu_matrices_submodular.md): Redundant Wave 4B (`1,661` lines)
- [`cohort2_iter_93_to_97_ds_graphs_simulated_mcmf_blossom.md`](cohort2_iter_93_to_97_ds_graphs_simulated_mcmf_blossom.md): Redundant Wave 5A (`1,637` lines)
- [`cohort2_iter_98_to_104_isotonic_crossdomain_zh_ja_en_audit.md`](cohort2_iter_98_to_104_isotonic_crossdomain_zh_ja_en_audit.md): Redundant Wave 5B (`1,410` lines)

## Cohort 3 Per-Wave Compiled & Reconciled Master Files (Iterations 105–114 — `16,282` lines, `1.87 MB`)
- [`cohort3_wave_1a_foundations_residual_lower_bounds.md`](cohort3_wave_1a_foundations_residual_lower_bounds.md): Master Reconciled Wave 1A (`1,622` lines)
- [`cohort3_wave_1b_bipartite_hall_dilworth_dm.md`](cohort3_wave_1b_bipartite_hall_dilworth_dm.md): Master Reconciled Wave 1B (`1,813` lines)
- [`cohort3_wave_2a_mincut_closure_qpbo_bipartite_flip.md`](cohort3_wave_2a_mincut_closure_qpbo_bipartite_flip.md): Master Reconciled Wave 2A (`1,646` lines)
- [`cohort3_wave_2b_multistate_monge_coarea_parametric.md`](cohort3_wave_2b_multistate_monge_coarea_parametric.md): Master Reconciled Wave 2B (`1,580` lines)
- [`cohort3_wave_3a_density_planar_mincut_dp_gomory_hu.md`](cohort3_wave_3a_density_planar_mincut_dp_gomory_hu.md): Master Reconciled Wave 3A (`1,603` lines)
- [`cohort3_wave_3b_mcmf_potentials_convex_diff_equations.md`](cohort3_wave_3b_mcmf_potentials_convex_diff_equations.md): Master Reconciled Wave 3B (`1,568` lines)
- [`cohort3_wave_4a_mcmf_cycles_dynamic_scheduling_ranks.md`](cohort3_wave_4a_mcmf_cycles_dynamic_scheduling_ranks.md): Master Reconciled Wave 4A (`1,635` lines)
- [`cohort3_wave_4b_lp_duality_tu_matrices_submodular.md`](cohort3_wave_4b_lp_duality_tu_matrices_submodular.md): Master Reconciled Wave 4B (`1,554` lines)
- [`cohort3_wave_5a_ds_graphs_simulated_mcmf_blossom.md`](cohort3_wave_5a_ds_graphs_simulated_mcmf_blossom.md): Master Reconciled Wave 5A (`1,615` lines)
- [`cohort3_wave_5b_isotonic_crossdomain_zh_ja_en_audit.md`](cohort3_wave_5b_isotonic_crossdomain_zh_ja_en_audit.md): Master Reconciled Wave 5B (`1,646` lines)

## Global Master Synthesis & Phase 1.5 Curriculum Files (`12,350` lines, `2.19 MB`)
- [`CITATIONS.md`](CITATIONS.md): Master Multilingual Bibliography (`132` sources across `[EN]`/`[ZH]`/`[JA]`) & `88`-Entry Terminology Rosetta Stone (`446` lines, `169.0 KB`).
- [`TECHNIQUE_TAXONOMY.md`](TECHNIQUE_TAXONOMY.md): Master Bidirectional Recognition & Compilation Atlas (`Direction A: Non-Graph -> Flow`, `Direction B: Flow -> Fast Algorithm`, `24` Failure Modes `FM-01`–`FM-24`) (`809` lines, `164.3 KB`).
- [`CURRICULUM_ARCHITECTURE.md`](CURRICULUM_ARCHITECTURE.md): Reconciled 6-Part, 24-Chapter + 6-Checkpoint Zero-Forward-Reference Curriculum Architecture (`1,712` lines, `264.4 KB`).
- [`PROBLEM_CURATION.md`](PROBLEM_CURATION.md): Reconciled 320-Problem Curation Specification (`#001`–`#192` Chapter Ladders, `#193`–`#240` Blind Checkpoints, `#241`–`#256` Capstones, `R-01`–`R-64` Quarantined Templates) (`1,114` lines, `237.2 KB`).
- [`problem_archive.md`](problem_archive.md): Complete 320-Problem Master Archive with 4-Step "Zero Magic Gadgets" Compilations (`3,847` lines, `559.3 KB`).
- [`phase1_5/`](phase1_5/): Round 1 Architecture & Problem Curation Proposals + 3 Independent Critic Audit Reports (`5` files, `4,424` lines).

## Phase 2 Authored Textbook (`flows/` — `36` `.qmd` files, `43,000+` lines)
- [`../flows/index.qmd`](../flows/index.qmd), [`../flows/notation.qmd`](../flows/notation.qmd), [`../flows/study-plan.qmd`](../flows/study-plan.qmd), [`../flows/sources.qmd`](../flows/sources.qmd)
- [`../flows/chapters/`](../flows/chapters/): 24 Core Chapters (`ch01` through `ch24`)
- [`../flows/checkpoints/`](../flows/checkpoints/): 6 Blind Part Checkpoints (`cp01` through `cp06`)
- [`../flows/capstones/`](../flows/capstones/): [`synthesis-reserve.qmd`](../flows/capstones/synthesis-reserve.qmd) & [`problem-archive-guide.qmd`](../flows/capstones/problem-archive-guide.qmd)

## Phase 3 Global Audit Reports & Automated Mathematical Oracle Suite (`11` `.md` files + `tests/audit_flows_models.py`)
- [`TEXTBOOK_AUTHORING_AUDIT.md`](TEXTBOOK_AUTHORING_AUDIT.md): **Master Textbook Authoring & Phase 3 Global Audit Sign-Off**
- [`../tests/audit_flows_models.py`](../tests/audit_flows_models.py): **24-Chapter Exact Mathematical & Graph-Compilation Oracle Suite + 36-File Quarto Hygiene Verifier** (`24/24` Oracles Passing, `0` Hygiene Errors)
- [`audits/phase3_iter01_zero_magic_4step_compilation.md`](audits/phase3_iter01_zero_magic_4step_compilation.md)
- [`audits/phase3_iter02_four_user_flagships_deep_audit.md`](audits/phase3_iter02_four_user_flagships_deep_audit.md)
- [`audits/phase3_iter03_pseudo_boolean_mincut_compiler.md`](audits/phase3_iter03_pseudo_boolean_mincut_compiler.md)
- [`audits/phase3_iter04_mcmf_equation_differencing_lp_duality.md`](audits/phase3_iter04_mcmf_equation_differencing_lp_duality.md)
- [`audits/phase3_iter05_direction_b_flow_elimination.md`](audits/phase3_iter05_direction_b_flow_elimination.md)
- [`audits/phase3_iter06_broken_gadget_failure_modes_catalog.md`](audits/phase3_iter06_broken_gadget_failure_modes_catalog.md)
- [`audits/phase3_iter07_320_problem_archive_quarantine_audit.md`](audits/phase3_iter07_320_problem_archive_quarantine_audit.md)
- [`audits/phase3_iter08_notation_terminology_conventions.md`](audits/phase3_iter08_notation_terminology_conventions.md)
- [`audits/phase3_iter09_pedagogical_pacing_AGENTS_compliance.md`](audits/phase3_iter09_pedagogical_pacing_AGENTS_compliance.md)
- [`audits/phase3_iter10_math_oracle_quarto_signoff.md`](audits/phase3_iter10_math_oracle_quarto_signoff.md)
