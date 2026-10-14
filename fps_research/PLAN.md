# Implementation Plan & Multi-Cohort Research Roadmap: Formal Power Series (FPS) & Generating Functions Textbook Overhaul

> [!IMPORTANT]
> **Canonical Workspace Reference for All Agents**
> This file (`fps_research/PLAN.md`) is the canonical workspace copy of the approved implementation plan and multi-cohort task breakdown. All research, auditing, curation, and authoring subagents should refer to this document for project goals, pedagogical standards, multi-cohort redundancy protocols, problem curation rules, and target file locations.

---

## 1. Goal Description

This project pivots the competitive programming mathematics textbook (`/home/maomao90/Documents/IO/ICPC-math-notes`) to focus comprehensively on **Formal Power Series (FPS), Generating Functions (GF), Combinatorial-to-GF Modelling, Algebraic & Differential Manipulations, Multivariate Polynomials, and Fast Polynomial Techniques**.

The existing pages in the repository are too brief, written in a terse style that assumes university-level mathematical maturity, and lack sufficient practice problems and literature coverage. Most importantly, typical editorials and notes present clever polynomial manipulations as "magic" — e.g., pulling an unintuitive polynomial substitution, variable change, Taylor shift, Lagrange inversion setup, or differential equation transformation out of thin air without explaining **how someone would think of that manipulation in the first place**.

To achieve **100% coverage of FPS techniques** in a way that makes every concept and manipulation intuitive to an expert competitive programmer who is weak in abstract mathematics, we execute a four-stage pipeline:
1. **Phase 1 (100+ Iteration Multi-Cohort Redundant Multilingual Discovery & Resource Audit Loop)**: Use parallel `DeepInvestigator` subagent cohorts across 100+ iterative waves to exhaustively mine English (`[EN]`), Chinese (`[ZH]`: Luogu, QOJ, UOJ, LOJ, CN blogs, Chinese National Team papers), and Japanese (`[JA]`: AtCoder, yukicoder, `maspypy`, `noshi91`, `Nyaan`, `tatyam`, JP blogs) resources and problems. Multiple independent agent cohorts research the **same topic areas** so that if one agent misses a technique, paper, blog, or problem, the redundant agent on the same area catches it, followed by a cross-comparison and blind-spot reconciliation cohort.
2. **Phase 1.5 (Corpus-Driven Curriculum & Problem Curation)**: Once the complete database of techniques, manipulation patterns, and problems is compiled after Phase 1 completes, design the textbook's section and chapter structure directly from the discovered corpus, and curate the collected problems into:
   - **Per-Topic Curated Problem Ladders**: Every independent topic has its own dedicated set of best-in-class problems arranged along a **smooth difficulty curve** (`Stepping Stone` $\to$ `Intermediate` $\to$ `Advanced` $\to$ `Mastery`; problems may naturally combine other topics on top of the main topic).
   - **Blind Topic-Group Checkpoint Collections**: After each logical group of topics, include a dedicated collection of problems where **the required topic/technique is hidden** on the visible page, testing the reader's ability to recognize which technique applies without spoiler headers.
   - **Archived Reserve Problem Bank**: All other audited, useful problems organized by topic and difficulty in `fps_research/problem_archive.md` (and a textbook reserve archive) so the reader can request additional practice on any sub-topic in the future.
3. **Phase 2 (Part-by-Part Textbook Authoring Loop)**: Use subagents in an iterative loop to write the textbook part by part, explaining all abstract math concepts from scratch ($K[[x]]$, $K((x))$, fields, rings, diagonalization operators, formal residues, etc.), explicitly teaching the **diagnostic clues and reverse-engineering intuition** behind every combinatorial translation and algebraic manipulation, and presenting every problem with a **concise inline problem statement, exact constraints, progressive hints, and full solution** for zero-friction study.
4. **Phase 3 ($\ge 10$-Iteration Multi-Agent Textbook Audit & Refinement Loop)**: Continuously audit and refine the completed textbook over at least 10 full passes with specialized subagents to eliminate any logical gaps, unexplained steps, missing techniques, or unclear explanations until the textbook is in a publishable state.

---

## 2. Key Design Decisions & Editorial Standards

> [!IMPORTANT]
> **1. Teaching "How to Discover the Manipulation" (Zero Magic Steps)**
> Whenever a problem or technique uses a non-obvious algebraic manipulation — whether substituting another polynomial, changing variables, applying a Taylor shift, simplifying a differential equation via substitution, decoupling multivariate polynomials, or setting up Lagrange inversion — the textbook will **never** state "substitute $u = \dots$" unmotivated. Every manipulation must include:
> - **The Diagnostic Signal**: What structural feature in the ugly formula tells you which tool to reach for.
> - **The Reverse-Engineering Scratchpad**: How to derive the target substitution or transformation step-by-step from what you *want* to cancel or simplify, rather than guessing it in advance.

> [!IMPORTANT]
> **2. Per-Topic Smooth Difficulty Ladders + Blind Topic-Group Checkpoints + Reserve Archive**
> - **Per-Topic Smooth Difficulty Curve**: Every independent topic has its own curated problem set ordered along a smooth ramp (`Stepping Stone` $\to$ `Intermediate` $\to$ `Advanced` $\to$ `Mastery`). Problems may combine auxiliary topics on top of the main topic just like real contest problems.
> - **Blind Topic-Group Checkpoints (No Topic Spoilers)**: Knowing which chapter a problem sits in often gives away 50% of the solution. Therefore, after each group of topics, we include a **Blind Checkpoint Problem Set** where the required technique is **not revealed** in the visible text. Hint 1 nudges the reader on how to diagnose the right technique from the statement alone, Hint 2 reveals the topic and initial GF setup, Hint 3 guides the manipulation, and the Solution explains both recognition and derivation.
> - **Unselected Problem Archive**: Every valid, non-template problem that is not selected for the primary textbook is archived in `fps_research/problem_archive.md` (with full tags, concise summary, difficulty tier, and technique breakdown).
> - **Strict Exclusion of Pure Template Problems**: Library Checker and bare template problems (`【模板】`) are explicitly rejected and logged in a rejection table so the textbook focuses purely on genuine modelling and manipulation insights.

> [!IMPORTANT]
> **3. Zero-Friction Inline Problem Presentation & Full Bibliographic Citations**
> - Every textbook problem (both per-topic and blind checkpoint problems) includes a **concise, self-contained mathematical problem statement and exact constraints** (input bounds $N, K \le \dots$, modulus, and required complexity) written directly inside the textbook.
> - Directly beneath the statement and constraints, each problem provides **progressive collapsible hints** followed by a collapsible **Complete Derivation & Solution**, plus direct links to the original judge and editorial.
> - Every research paper, Chinese National Team paper (`国家集训队论文`), textbook, and educational blog (`[EN]`, `[ZH]`, `[JA]`) is recorded with full bibliographic citation metadata.

---

## 3. Multi-Cohort Research Schedule & File Map (`fps_research/`)

To guarantee that no technique, manipulation trick, blog series, or high-value contest problem is missed, Phase 1 is organized into **two independent discovery cohorts (Cohort 1: Iterations 01–52; Cohort 2: Iterations 53–104)** covering the exact same 10 topic waves in parallel, followed by **Cohort 3 (Iterations 105–115+)** which cross-compares Cohort 1 and Cohort 2 to reconcile any blind spots and synthesize the master tables.

### Cohort 1 & Cohort 2 Paired Wave Matrix

| Topic Wave | Core Topics & Questions Investigated (EN / ZH / JA) | Cohort 1 File (Iterations 01–52) | Cohort 2 Redundant File (Iterations 53–104) |
|---|---|---|---|
| **Wave 1A** | Foundational Algebra ($K[[x]]$, $K((x))$, rings, fields, units, valuation, operators $D$, $\vartheta$), Unlabelled OGFs (`SEQ`, `MSET`, `PSET`, `CYC`, Euler Transform, Partitions, Durfee squares, Pólya/Burnside), Labelled EGFs (`SET`, `CYC`, $\exp/\ln$, Pointing, Boxed Product), `[ZH]` & `[JA]` Modelling | `fps_research/iter_01_to_05_modelling_foundations.md` (Iter 01–05) | `fps_research/cohort2_iter_53_to_57_modelling_foundations.md` (Iter 53–57) |
| **Wave 1B** | Combinatorial-to-GF Modelling Archetypes, Mechanical 1D/2D/Automaton DP-to-GF Conversion & Boundary Term Engineering, Untangling Binomial & Falling-Factorial Sums via $[x^n]$ ("Snake Oil" & Egorychev), Hidden Convolutions (Difference/Correlation, Vandermonde, Upper-Index, Prefix/Difference Operators) | `fps_research/iter_06_to_10_dp_and_sums.md` (Iter 06–10) | `fps_research/cohort2_iter_58_to_62_dp_and_sums.md` (Iter 58–62) |
| **Wave 2A** | Rational/Linear/Mobius Substitutions ($x \mapsto \frac{x}{1-x}$, Euler Transform, Taylor Shifts), Radical/Catalan/Motzkin/Delannoy/Chebyshev Substitutions ($x = u(1-u)$, $x = \frac{z}{1+z^2}$), Transcendental Substitutions ($e^z-1$, $\ln(1+z)$), Binomial/Stirling/Lah & Falling-Factorial Polynomial Transforms, Logarithmic Derivatives ($F'/F$) & Newton's Identities, Roots of Unity Filters (`单位根反演`) | `fps_research/iter_11_to_15_substitutions_transforms.md` (Iter 11–15) | `fps_research/cohort2_iter_63_to_67_substitutions_transforms.md` (Iter 63–67) |
| **Wave 2B** | Inclusion–Exclusion in GFs (`连续段容斥`), Forbidden Substrings & Goulden–Jackson Cluster Method, Probability Generating Functions (PGFs), Stopping Times ($F'(1)$, $F''(1)$), First-Passage Renewal & FWT/Graph Random Walks, `[ZH]`/`[JA]` Substitution & Manipulation Deep-Dives | `fps_research/iter_16_to_20_ie_pgf_zh_ja_audit.md` (Iter 16–20) | `fps_research/cohort2_iter_68_to_72_ie_pgf_zh_ja_audit.md` (Iter 68–72) |
| **Wave 3A** | Standard Lagrange–Bürmann Inversion ($F = x\Phi(F)$) & Raney/Cycle Lemma, Formal Laurent Series $K((x))$, Formal Residue Calculus ($\operatorname{res}_x$) & Change-of-Variables (`炫酷反演魔术`), Derivative-Free & Compound Lagrange Forms, Tree/Forest/Prüfer/Cactus Enumerations, Graph Enumerations (Functional, Eulerian, Bipartite, DAGs, 2-Connected / Biconnected) | `fps_research/iter_21_to_25_lagrange_residues_trees_graphs.md` (Iter 21–25) | `fps_research/cohort2_iter_73_to_77_lagrange_residues_trees_graphs.md` (Iter 73–77) |
| **Wave 3B** | `[ZH]` (`Elegia`, `command_block`, `rqy`, Luogu, UOJ/QOJ) & `[JA]` (`maspypy`, `noshi91`, AtCoder, yukicoder) Implicit GF & Residue Deep-Dives, Extracting All Coefficients vs. Single Coefficient (Newton vs. LIF vs. CDQ), Small-Characteristic ($p \le n$) Pitfalls & Division-Free Extraction / Lucas-LIF Hybrids | `fps_research/iter_26_to_30_implicit_zh_ja_audit.md` (Iter 26–30) | `fps_research/cohort2_iter_78_to_82_implicit_zh_ja_audit.md` (Iter 78–82) |
| **Wave 4A** | Multivariate Rings ($K[x,y]$, $K[y][[x]]$ vs. $K[x][[y]]$, $K[[x,y]]$), Choosing the Primary Variable, Variable Decoupling Substitutions ($u = xy^a$, Homogenization), Auxiliary-Variable Evaluation–Interpolation, 2D FFT & Kronecker Substitution, 2D FPS Operations, Rational GFs & 1D/2D Bostan–Mori, Constant Term $\operatorname{CT}_z$ & Diagonal Operator $\operatorname{Diag}$ | `fps_research/iter_31_to_35_multivariate_bostan_mori_diag.md` (Iter 31–35) | `fps_research/cohort2_iter_83_to_87_multivariate_bostan_mori_diag.md` (Iter 83–87) |
| **Wave 4B** | Furstenberg's Method (Rational Diagonals via Formal Residues), The Kernel Method ($K(x,y)F(x,y) = A(x)+B(y)$, Reflection & Vietoris/Bousquet-Mélou Walks), Bivariate & Multivariate Good–Lagrange Inversion & MacMahon Master Theorem, `[ZH]`/`[JA]` 2D GF Deep-Dive & Multivariate Decision Tree | `fps_research/iter_36_to_40_furstenberg_kernel_good_lagrange.md` (Iter 36–40) | `fps_research/cohort2_iter_88_to_92_furstenberg_kernel_good_lagrange.md` (Iter 88–92) |
| **Wave 5A** | D-Finite / Holonomic Series & P-Recursive Sequences, Turning GFs into Linear ODEs ($P(x)F' + Q(x)F = R(x)$), Simplifying ODEs via Substitution, Sparse FPS Operations in $O(N \cdot K)$ (`inv`, `exp`, `ln`, `pow`, $\sqrt{}$, $F(P(x))$), Euler Homogeneous PDEs & Holonomic Binomial Sum Reductions (creative telescoping), Divide-and-Conquer FFT (CDQ NTT) & Relaxed/Online Convolution (van der Hoeven) | `fps_research/iter_41_to_45_ode_sparse_cdq_relaxed.md` (Iter 41–45) | `fps_research/cohort2_iter_93_to_97_ode_sparse_cdq_relaxed.md` (Iter 93–97) |
| **Wave 5B** | Tree DP + FPS Acceleration (Heavy-Light Decomposition / Globally Balanced BST + D&C Matrix/Polynomial Merging), Tellegen's Transposition Principle (`转置原理`) & Middle Product, Power Projection & Kinoshita–Li (2024) $O(N \log^2 N)$ Composition/Reversion, Chirp Z-Transform (Bluestein), Shift of Sampling Points, $q$-Analogues / Gaussian Binomials $\binom{n}{k}_q$, Set/Dirichlet Series Links | `fps_research/iter_46_to_52_tree_fps_transposition_compose_q.md` (Iter 46–52) | `fps_research/cohort2_iter_98_to_104_tree_fps_transposition_compose_q.md` (Iter 98–104) |

### Cohort 3 Per-Wave Compiled Reconciliation Files & Master Synthesis Files (`fps_research/`)

- **Per-Wave Cohort 3 Reconciled Master Files (Iterations 105–114)**:
  - `fps_research/cohort3_wave_1a_modelling_foundations.md`: Compiled from Cohort 1 (`iter_01_to_05_modelling_foundations.md`) + Cohort 2 (`cohort2_iter_53_to_57_modelling_foundations.md`).
  - `fps_research/cohort3_wave_1b_dp_and_sums.md`: Compiled from Cohort 1 (`iter_06_to_10_dp_and_sums.md`) + Cohort 2 (`cohort2_iter_58_to_62_dp_and_sums.md`).
  - `fps_research/cohort3_wave_2a_substitutions_transforms.md`: Three-way compilation from Cohort 1 (`iter_11_to_15_substitutions_transforms.md`) + Cohort 2 New (`cohort2_new_iter_63_to_67_substitutions_transforms.md`) + Pre-existing (`cohort2_iter_63_to_67_substitutions_transforms.md`).
  - `fps_research/cohort3_wave_2b_ie_pgf_zh_ja_audit.md`: Three-way compilation from Cohort 1 New (`cohort1_iter_16_to_20_ie_pgf_zh_ja_audit.md`) + Cohort 2 (`cohort2_iter_68_to_72_ie_pgf_zh_ja_audit.md`) + Pre-existing (`iter_16_to_20_ie_pgf_zh_ja_audit.md`).
  - `fps_research/cohort3_wave_3a_lagrange_residues_trees_graphs.md`: Three-way compilation from Cohort 1 New (`cohort1_iter_21_to_25_lagrange_residues_trees_graphs.md`) + Cohort 2 (`cohort2_iter_73_to_77_lagrange_residues_trees_graphs.md`) + Pre-existing (`iter_21_to_25_lagrange_residues_trees_graphs.md`).
  - `fps_research/cohort3_wave_3b_implicit_zh_ja_audit.md`: Compiled from Cohort 1 (`iter_26_to_30_implicit_zh_ja_audit.md`) + Cohort 2 (`cohort2_iter_78_to_82_implicit_zh_ja_audit.md`).
  - `fps_research/cohort3_wave_4a_multivariate_bostan_mori_diag.md`: Compiled from Cohort 1 (`iter_31_to_35_multivariate_bostan_mori_diag.md`) + Cohort 2 (`cohort2_iter_83_to_87_multivariate_bostan_mori_diag.md`).
  - `fps_research/cohort3_wave_4b_furstenberg_kernel_good_lagrange.md`: Compiled from Cohort 1 (`iter_36_to_40_furstenberg_kernel_good_lagrange.md`) + Cohort 2 (`cohort2_iter_88_to_92_furstenberg_kernel_good_lagrange.md`).
  - `fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md`: Three-way compilation from Cohort 1 New (`cohort1_iter_41_to_45_ode_sparse_cdq_relaxed.md`) + Cohort 2 (`cohort2_iter_93_to_97_ode_sparse_cdq_relaxed.md`) + Pre-existing (`iter_41_to_45_ode_sparse_cdq_relaxed.md`).
  - `fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md`: Three-way compilation from Cohort 1 New (`cohort1_iter_46_to_52_tree_fps_transposition_compose_q.md`) + Cohort 2 (`cohort2_iter_98_to_104_tree_fps_transposition_compose_q.md`) + Pre-existing (`iter_46_to_52_tree_fps_transposition_compose_q.md`).
- **Global Master Synthesis & Phase 1.5 Curriculum Files (Iterations 115+)**:
  - `fps_research/CITATIONS.md`: Consolidated master bibliography of all research papers, Chinese National Team papers, books, and `[EN]`/`[ZH]`/`[JA]` educational blogs discovered across Cohort 1, Cohort 2, and Pre-existing files (68 canonical entries + 52-iteration index + 75-entry Multilingual Terminology Rosetta Stone).
  - `fps_research/TECHNIQUE_TAXONOMY.md`: Complete synthesized taxonomy of all FPS/GF concepts, notations, modelling bridges, diagnostic signals, and manipulation discovery patterns reconciled across all 10 waves.
  - `fps_research/CURRICULUM_ARCHITECTURE.md`: Master 6-Part, 24-Chapter Zero-Forward-Reference Curriculum Architecture dissolving all 10 research waves and regional (`[ZH]`/`[JA]`) buckets into 24 granular pedagogical chapters, complete with prerequisite DAGs, diagnostic signals, reverse-engineering scratchpads, worked flagship examples, and 100% bijective problem routing.
  - `fps_research/PROBLEM_CURATION.md`: Master curation ledger mapping all **321 total cataloged problems** (`408` raw appearances) into **254 unique accepted non-template problems** (`#001`–`#254`: `192` across 24 8-problem **Per-Chapter 4-Tier Smooth Difficulty Ladders**, `48` across 6 8-problem **Part-End Blind Topic-Group Checkpoints** `CP-I`–`CP-VI`, and `14` **Grandmaster Multi-Chapter Synthesis Reserves** `Syn-01`–`Syn-14`) plus **67 Quarantined Template Problems** (`R-01`–`R-67`).
  - `fps_research/problem_archive.md`: Master encyclopedia of all 254 unique accepted non-template FPS problems (`#001`–`#254`) and 67 quarantined template problems (`R-01`–`R-67`), synchronized 100% with the 24-chapter curriculum (`§0`) and indexed by online judge (`§1`) and research wave (`§2`–`§11`).

---

## 4. Detailed Task Checklist

### Phase 1: 100+ Iteration Multilingual Discovery & Resource Audit Loop
- [x] Initialize `fps_research/` master database, `README.md`, and `PLAN.md`
- [x] **Cohort 1 (Iterations 01–52): Primary 10-Wave Multilingual Discovery & Audit**
  - [x] Wave 1A (Iter 01–05): `fps_research/iter_01_to_05_modelling_foundations.md`
  - [x] Wave 1B (Iter 06–10): `fps_research/iter_06_to_10_dp_and_sums.md`
  - [x] Wave 2A (Iter 11–15): `fps_research/iter_11_to_15_substitutions_transforms.md`
  - [x] Wave 2B (Iter 16–20): `fps_research/cohort1_iter_16_to_20_ie_pgf_zh_ja_audit.md` (+ pre-existing `fps_research/iter_16_to_20_ie_pgf_zh_ja_audit.md`)
  - [x] Wave 3A (Iter 21–25): `fps_research/cohort1_iter_21_to_25_lagrange_residues_trees_graphs.md` (+ pre-existing `fps_research/iter_21_to_25_lagrange_residues_trees_graphs.md`)
  - [x] Wave 3B (Iter 26–30): `fps_research/iter_26_to_30_implicit_zh_ja_audit.md`
  - [x] Wave 4A (Iter 31–35): `fps_research/iter_31_to_35_multivariate_bostan_mori_diag.md`
  - [x] Wave 4B (Iter 36–40): `fps_research/iter_36_to_40_furstenberg_kernel_good_lagrange.md`
  - [x] Wave 5A (Iter 41–45): `fps_research/cohort1_iter_41_to_45_ode_sparse_cdq_relaxed.md` (+ pre-existing `fps_research/iter_41_to_45_ode_sparse_cdq_relaxed.md`)
  - [x] Wave 5B (Iter 46–52): `fps_research/cohort1_iter_46_to_52_tree_fps_transposition_compose_q.md` (+ pre-existing `fps_research/iter_46_to_52_tree_fps_transposition_compose_q.md`)
- [x] **Cohort 2 (Iterations 53–104): Independent Redundant Agents Researching the Same 10 Areas**
  - [x] Redundant Wave 1A (Iter 53–57): `fps_research/cohort2_iter_53_to_57_modelling_foundations.md`
  - [x] Redundant Wave 1B (Iter 58–62): `fps_research/cohort2_iter_58_to_62_dp_and_sums.md`
  - [x] Redundant Wave 2A (Iter 63–67): `fps_research/cohort2_new_iter_63_to_67_substitutions_transforms.md` (+ pre-existing `fps_research/cohort2_iter_63_to_67_substitutions_transforms.md`)
  - [x] Redundant Wave 2B (Iter 68–72): `fps_research/cohort2_iter_68_to_72_ie_pgf_zh_ja_audit.md`
  - [x] Redundant Wave 3A (Iter 73–77): `fps_research/cohort2_iter_73_to_77_lagrange_residues_trees_graphs.md`
  - [x] Redundant Wave 3B (Iter 78–82): `fps_research/cohort2_iter_78_to_82_implicit_zh_ja_audit.md`
  - [x] Redundant Wave 4A (Iter 83–87): `fps_research/cohort2_iter_83_to_87_multivariate_bostan_mori_diag.md`
  - [x] Redundant Wave 4B (Iter 88–92): `fps_research/cohort2_iter_88_to_92_furstenberg_kernel_good_lagrange.md`
  - [x] Redundant Wave 5A (Iter 93–97): `fps_research/cohort2_iter_93_to_97_ode_sparse_cdq_relaxed.md`
  - [x] Redundant Wave 5B (Iter 98–104): `fps_research/cohort2_iter_98_to_104_tree_fps_transposition_compose_q.md`
- [x] **Cohort 3 (Iterations 105–115): Cross-Agent Comparison, Blind-Spot Reconciliation & Deep Gap-Hunting Loop**
  - [x] Iterations 105–109: Cross-compare Cohort 1 vs. Cohort 2 (+ Pre-existing) outputs across Waves 1–3 (`cohort3_wave_1a_*.md` to `cohort3_wave_3b_*.md`); hunt down any missing techniques, blog series, or problem tiers
  - [x] Iterations 110–115: Cross-compare Cohort 1 vs. Cohort 2 (+ Pre-existing) outputs across Waves 4–5 (`cohort3_wave_4a_*.md` to `cohort3_wave_5b_*.md`); verify 100% coverage of manipulations and problem difficulty curves across all topics

### Phase 1.5: Corpus-Driven Curriculum Design & Problem Curation
- [x] Synthesize complete technique taxonomy (`fps_research/TECHNIQUE_TAXONOMY.md`) and master bibliography (`fps_research/CITATIONS.md`) from the 115-iteration research corpus
- [x] Design and reconcile the 6-Part, 24-Chapter Zero-Forward-Reference Curriculum Architecture (`fps_research/CURRICULUM_ARCHITECTURE.md`) across 3 independent proposals and multi-agent audit rounds
- [x] Curate 24 8-problem Per-Chapter 4-Tier Smooth Difficulty Ladders (`192` problems: `Stepping Stone` $\to$ `Intermediate` $\to$ `Advanced` $\to$ `Mastery`) in `fps_research/PROBLEM_CURATION.md`
- [x] Curate 6 8-problem Part-End Blind Topic-Group Checkpoints (`48` problems: `CP-I`–`CP-VI`) and `14` Grandmaster Multi-Chapter Synthesis Reserves (`Syn-01`–`Syn-14`) in `fps_research/PROBLEM_CURATION.md` (`254` accepted problems + `67` quarantined templates = `321` total cataloged problems)
- [x] Synchronize `fps_research/problem_archive.md`, `fps_research/PROBLEM_CURATION.md`, and `fps_research/CURRICULUM_ARCHITECTURE.md` to 100% (254/254) bijective agreement
- [x] Configure final chapter and section navigation in `_quarto.yml` for Phase 2 textbook authoring

### Phase 2: Part-by-Part Educational Textbook Authoring Loop
- [x] Author and verify each chapter, per-topic problem ladder, blind checkpoint, and reference page in an iterative loop (`fps_research/TEXTBOOK_AUTHORING_AUDIT.md`)
- [x] Build comprehensive exact mathematical verification suite (`tests/audit_fps_math.py`)

### Phase 3: $\ge 10$-Iteration Multi-Agent Textbook Audit & Polish Loop
- [x] Audit Iteration 01: Abstract Math & Notation Clarity (Rings, Fields, $K[[x]]$, $K((x))$, Operators) (`fps_research/audits/phase3_iter01_abstract_math_notation.md`)
- [x] Audit Iteration 02: Combinatorial-to-GF Modelling Bridge Completeness (`fps_research/audits/phase3_iter02_modelling_bridges.md`)
- [x] Audit Iteration 03: Manipulation Discovery Intuition & Zero Magic Substitutions (`fps_research/audits/phase3_iter03_zero_magic_scratchpads.md`)
- [x] Audit Iteration 04: Single-Step Algebraic Derivations & Verbal Annotations (`fps_research/audits/phase3_iter04_single_step_derivations.md`)
- [x] Audit Iteration 05: Multivariate, Diagonal, Residue & Kernel Method Clarity (`fps_research/audits/phase3_iter05_multivariate_residues_kernel.md`)
- [x] Audit Iteration 06: Differential Equations, Sparse FPS & Fast Engine Completeness (`fps_research/audits/phase3_iter06_ode_sparse_fast_engines.md`)
- [x] Audit Iteration 07: Per-Topic Smooth Difficulty Ladders & Inline Problem Statements/Constraints (`fps_research/audits/phase3_iter07_problem_ladders_inline.md`)
- [x] Audit Iteration 08: Blind Checkpoint Spoiler-Free Design & Progressive Hints Quality (`fps_research/audits/phase3_iter08_blind_checkpoints_hints.md`)
- [x] Audit Iteration 09: Full Citation Verification, Reserve Problem Archive & Cross-Links (`fps_research/audits/phase3_iter09_citations_char_p_links.md`)
- [x] Audit Iteration 10+: Exact Math Oracles (`tests/audit_fps_math.py`), Full `quarto render`, Layout & Publishability Sign-Off (`fps_research/audits/phase3_iter10_math_oracle_quarto_signoff.md`)
