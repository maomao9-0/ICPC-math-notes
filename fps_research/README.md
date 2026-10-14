# Formal Power Series & Generating Functions Research Corpus (`fps_research/`)

This directory stores the cumulative multilingual research, bibliography, technique taxonomy, and problem audit records across 115+ iterative passes covering English (`[EN]`), Chinese (`[ZH]`), and Japanese (`[JA]`) competitive programming literature and online judges (~5.9 MB across 39 markdown documents).

## Canonical Plan & Roadmap
- [`PLAN.md`](PLAN.md): **Master Implementation Plan & Multi-Cohort Research Roadmap** — Read this first! Defines the 4-stage pipeline, editorial and pedagogical standards, problem curation rules, and the Cohort 1 / Cohort 2 / Pre-existing / Cohort 3 file matrix.

## Cohort 3 Global Master Synthesis & Phase 1.5 Curriculum Files (Iterations 115+)
- [`CITATIONS.md`](CITATIONS.md) (**89 KB**): Consolidated master bibliography of 68 canonical textbooks, seminal papers (Kinoshita–Li FOCS 2024, Bostan–Mori 2021, van der Hoeven, Furstenberg, Lipshitz, Good, Gessel, Wright), Chinese National Team papers (`国家集训队论文`), and `[EN]`/`[ZH]`/`[JA]` educational monographs (`Elegia`, `maspypy`, `noshi91`, `Nyaan`, `tatyam`), plus a 52-iteration topic-to-citation matrix and a 75-entry Multilingual Terminology Rosetta Stone.
- [`TECHNIQUE_TAXONOMY.md`](TECHNIQUE_TAXONOMY.md) (**88 KB**): Complete synthesized taxonomy of all FPS/GF operators, modelling bridges, **Zero Magic Steps** manipulation discovery playbooks (Diagnostic Signals + Reverse-Engineering Scratchpads), cross-cohort blind-spot reconciliations, and a 16-row Characteristic-$p$ & Failure-Mode Hazard Checklist.
- [`CURRICULUM_ARCHITECTURE.md`](CURRICULUM_ARCHITECTURE.md) (**315 KB**): Master **6-Part, 24-Chapter Zero-Forward-Reference Curriculum Architecture**, dissolving all 10 research collection waves and regional (`[ZH]`/`[JA]`) audit buckets into 24 granular pedagogical chapters with strict prerequisite DAGs, diagnostic signals, reverse-engineering scratchpads, worked flagship examples, and 100% bijective problem routing.
- [`PROBLEM_CURATION.md`](PROBLEM_CURATION.md) (**185 KB**): Master curation ledger indexing all **321 total cataloged problems** (`408` raw appearances across 16 online judges), bijectively routing **254 unique accepted non-template problems** (`#001`–`#254`) into **24 8-problem Per-Chapter 4-Tier Smooth Difficulty Ladders** (`192` problems: `Stepping Stone` $\to$ `Intermediate` $\to$ `Advanced` $\to$ `Mastery`), **6 8-problem Part-End Blind Topic-Group Checkpoints** (`48` problems: `CP-I`–`CP-VI`), and **14 Grandmaster Multi-Chapter Synthesis Reserves** (`Syn-01`–`Syn-14`), plus **67 Quarantined Template Problems** (`R-01`–`R-67`).
- [`problem_archive.md`](problem_archive.md) (**225 KB**): Master problem encyclopedia cataloging all **254 unique accepted non-template problems** (`#001`–`#254`) and **67 quarantined template problems** (`R-01`–`R-67`) across Waves 1A–5B, synchronized 100% with the 24-chapter curriculum (`§0`) and indexed by online judge (`§1`) and research wave (`§2`–`§11`).

## Cohort 3 Per-Wave Compiled & Reconciled Master Files (Iterations 105–114)
Each file reconciles 2 or 3 independent research files (Cohort 1 + Cohort 2, plus Pre-existing research where present), documenting cross-cohort blind spots, unified derivations, multilingual citations, and complete problem write-ups:
- [`cohort3_wave_1a_modelling_foundations.md`](cohort3_wave_1a_modelling_foundations.md) (**168 KB**, 2 files compiled): Wave 1A — Foundational Algebra ($R[[x]]$, $K((x))$, valuation, characteristic $p$), Unlabelled OGFs, Labelled EGFs, Pointing/Unpointing, Rational GFs & Transfer Matrix Method.
- [`cohort3_wave_1b_dp_and_sums.md`](cohort3_wave_1b_dp_and_sums.md) (**198 KB**, 2 files compiled): Wave 1B — 1D/2D DP-to-FPS Translation, Boundary Polynomial Perturbations, Vandermonde & Generalized Binomial Identities, Snake Oil & Egorychev Residue Calculus, Prefix Sums & Partial Fractions.
- [`cohort3_wave_2a_substitutions_transforms.md`](cohort3_wave_2a_substitutions_transforms.md) (**141 KB**, 3 files compiled): Wave 2A — Rational/Projective Substitutions & Taylor Shift, Quadratic Radicals & Chebyshev Substitutions, Transcendental Substitutions & Falling-Factorial Polynomials, Euler Transform & Newton's Identities, Roots of Unity Filter & Bluestein Chirp-Z.
- [`cohort3_wave_2b_ie_pgf_zh_ja_audit.md`](cohort3_wave_2b_ie_pgf_zh_ja_audit.md) (**164 KB**, 3 files compiled): Wave 2B — Inclusion–Exclusion Homomorphisms (`连续段容斥`), Goulden–Jackson Cluster Method, Stirling & Differential Operators $(xD)^k$, Probability Generating Functions (PGFs) & Stopping Times, `[ZH]`/`[JA]` Deep Audit.
- [`cohort3_wave_3a_lagrange_residues_trees_graphs.md`](cohort3_wave_3a_lagrange_residues_trees_graphs.md) (**187 KB**, 3 files compiled): Wave 3A — Formal Laurent Series & Formal Residue Operator $\operatorname{Res}$, Lagrange Inversion Formula (6 Forms), Combinatorial Proofs (Raney's Lemma, Łukasiewicz Paths, Prüfer Codes, Joyal Vertebrates), Rooted/Unrooted Tree Enumeration & Dissymmetry, Functional Graphs & Wright's $k$-Excess Graphs.
- [`cohort3_wave_3b_implicit_zh_ja_audit.md`](cohort3_wave_3b_implicit_zh_ja_audit.md) (**173 KB**, 2 files compiled): Wave 3B — Cactus Graphs, Block-Cut Trees & 2-Connected Graphs, Generalized Binomial $\mathcal{B}_t(x)$ & Exponential $\mathcal{E}_t(x)$ Series, Implicit Algebraic Equations & Newton–Puiseux Intuition, `[ZH]`/`[JA]` Deep Audit on Lagrange & Characteristic-$p$ Extraction.
- [`cohort3_wave_4a_multivariate_bostan_mori_diag.md`](cohort3_wave_4a_multivariate_bostan_mori_diag.md) (**152 KB**, 2 files compiled): Wave 4A — Multivariate Rings & Mixed OGF/EGF Calculus, Twisted Kronecker Substitution, 1D/2D Bostan–Mori & Graeffe Root-Squaring, Bivariate Rational Diagonals $\operatorname{Diag}$, MacMahon's Master Theorem (MMT) & Permanent/Determinant Duality.
- [`cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`](cohort3_wave_4b_furstenberg_kernel_good_lagrange.md) (**200 KB**, 2 files compiled): Wave 4B — Furstenberg's Diagonal Method, The Kernel Method (Single Boundary, Bounded Strips, Multi-Branch Vieta Jumping, Quarter-Plane Walks), Multivariate Good–Lagrange Inversion, `[EN]`/`[ZH]`/`[JA]` Lattice Path & 2D Audit.
- [`cohort3_wave_5a_ode_sparse_cdq_relaxed.md`](cohort3_wave_5a_ode_sparse_cdq_relaxed.md) (**148 KB**, 3 files compiled): Wave 5A — D-Finite / Holonomic Series & P-Recursive Sequences, ODE Substitutions & Integrating Factor Newton Solver, Sparse FPS Engine in $O(NK)$, Euler Homogeneous PDEs & `EI 科技` Binomial Sums, Semi-Online CDQ NTT & Fully Online Relaxed Convolution (van der Hoeven).
- [`cohort3_wave_5b_tree_fps_transposition_compose_q.md`](cohort3_wave_5b_tree_fps_transposition_compose_q.md) (**213 KB**, 3 files compiled): Wave 5B — Tree DP + HLD / Weight-Balanced Static Top Tree (`Rake`/`Compress`), Tellegen's Transposition Principle & Middle Product, Kinoshita–Li (2024) $O(N \log^2 N)$ Power Projection / Composition / Reversion, Chirp Z-Transform & Sampling Shift, $q$-Analogues & Pentagonal Number Theorem, Set Power Series (SPS), Dirichlet GFs, and Characteristic-$p$ Zero-Divisor Maintenance.

## Cohort 1 Independent Research Files (Iterations 01–52)
- [`iter_01_to_05_modelling_foundations.md`](iter_01_to_05_modelling_foundations.md) (**158 KB**): Wave 1A (Iter 01–05).
- [`iter_06_to_10_dp_and_sums.md`](iter_06_to_10_dp_and_sums.md) (**150 KB**): Wave 1B (Iter 06–10).
- [`iter_11_to_15_substitutions_transforms.md`](iter_11_to_15_substitutions_transforms.md) (**147 KB**): Wave 2A (Iter 11–15).
- [`cohort1_iter_16_to_20_ie_pgf_zh_ja_audit.md`](cohort1_iter_16_to_20_ie_pgf_zh_ja_audit.md) (**142 KB**): Wave 2B (Iter 16–20, fresh Cohort 1 run).
- [`cohort1_iter_21_to_25_lagrange_residues_trees_graphs.md`](cohort1_iter_21_to_25_lagrange_residues_trees_graphs.md) (**122 KB**): Wave 3A (Iter 21–25, fresh Cohort 1 run).
- [`iter_26_to_30_implicit_zh_ja_audit.md`](iter_26_to_30_implicit_zh_ja_audit.md) (**143 KB**): Wave 3B (Iter 26–30).
- [`iter_31_to_35_multivariate_bostan_mori_diag.md`](iter_31_to_35_multivariate_bostan_mori_diag.md) (**131 KB**): Wave 4A (Iter 31–35).
- [`iter_36_to_40_furstenberg_kernel_good_lagrange.md`](iter_36_to_40_furstenberg_kernel_good_lagrange.md) (**140 KB**): Wave 4B (Iter 36–40).
- [`cohort1_iter_41_to_45_ode_sparse_cdq_relaxed.md`](cohort1_iter_41_to_45_ode_sparse_cdq_relaxed.md) (**160 KB**): Wave 5A (Iter 41–45, fresh Cohort 1 run).
- [`cohort1_iter_46_to_52_tree_fps_transposition_compose_q.md`](cohort1_iter_46_to_52_tree_fps_transposition_compose_q.md) (**162 KB**): Wave 5B (Iter 46–52, fresh Cohort 1 run).

## Cohort 2 Independent Redundant Research Files (Iterations 53–104)
- [`cohort2_iter_53_to_57_modelling_foundations.md`](cohort2_iter_53_to_57_modelling_foundations.md) (**149 KB**): Redundant Wave 1A (Iter 53–57).
- [`cohort2_iter_58_to_62_dp_and_sums.md`](cohort2_iter_58_to_62_dp_and_sums.md) (**144 KB**): Redundant Wave 1B (Iter 58–62).
- [`cohort2_new_iter_63_to_67_substitutions_transforms.md`](cohort2_new_iter_63_to_67_substitutions_transforms.md) (**140 KB**): Redundant Wave 2A (Iter 63–67, fresh Cohort 2 run).
- [`cohort2_iter_68_to_72_ie_pgf_zh_ja_audit.md`](cohort2_iter_68_to_72_ie_pgf_zh_ja_audit.md) (**127 KB**): Redundant Wave 2B (Iter 68–72).
- [`cohort2_iter_73_to_77_lagrange_residues_trees_graphs.md`](cohort2_iter_73_to_77_lagrange_residues_trees_graphs.md) (**138 KB**): Redundant Wave 3A (Iter 73–77).
- [`cohort2_iter_78_to_82_implicit_zh_ja_audit.md`](cohort2_iter_78_to_82_implicit_zh_ja_audit.md) (**154 KB**): Redundant Wave 3B (Iter 78–82).
- [`cohort2_iter_83_to_87_multivariate_bostan_mori_diag.md`](cohort2_iter_83_to_87_multivariate_bostan_mori_diag.md) (**146 KB**): Redundant Wave 4A (Iter 83–87).
- [`cohort2_iter_88_to_92_furstenberg_kernel_good_lagrange.md`](cohort2_iter_88_to_92_furstenberg_kernel_good_lagrange.md) (**158 KB**): Redundant Wave 4B (Iter 88–92).
- [`cohort2_iter_93_to_97_ode_sparse_cdq_relaxed.md`](cohort2_iter_93_to_97_ode_sparse_cdq_relaxed.md) (**174 KB**): Redundant Wave 5A (Iter 93–97).
- [`cohort2_iter_98_to_104_tree_fps_transposition_compose_q.md`](cohort2_iter_98_to_104_tree_fps_transposition_compose_q.md) (**196 KB**): Redundant Wave 5B (Iter 98–104).

## Pre-Existing Baseline Research Files (Incorporated in Cohort 3 Three-Way Compilations)
- [`cohort2_iter_63_to_67_substitutions_transforms.md`](cohort2_iter_63_to_67_substitutions_transforms.md) (**97 KB**): Pre-existing Wave 2A file (compiled into `cohort3_wave_2a_substitutions_transforms.md`).
- [`iter_16_to_20_ie_pgf_zh_ja_audit.md`](iter_16_to_20_ie_pgf_zh_ja_audit.md) (**114 KB**): Pre-existing Wave 2B file (compiled into `cohort3_wave_2b_ie_pgf_zh_ja_audit.md`).
- [`iter_21_to_25_lagrange_residues_trees_graphs.md`](iter_21_to_25_lagrange_residues_trees_graphs.md) (**119 KB**): Pre-existing Wave 3A file (compiled into `cohort3_wave_3a_lagrange_residues_trees_graphs.md`).
- [`iter_41_to_45_ode_sparse_cdq_relaxed.md`](iter_41_to_45_ode_sparse_cdq_relaxed.md) (**37 KB**): Pre-existing Wave 5A file (compiled into `cohort3_wave_5a_ode_sparse_cdq_relaxed.md`).
- [`iter_46_to_52_tree_fps_transposition_compose_q.md`](iter_46_to_52_tree_fps_transposition_compose_q.md) (**127 KB**): Pre-existing Wave 5B file (compiled into `cohort3_wave_5b_tree_fps_transposition_compose_q.md`).
