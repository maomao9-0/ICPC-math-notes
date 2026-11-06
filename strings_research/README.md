# Advanced Stringology, Combinatorics on Words & Algebraic/Automaton String Algorithms Research Corpus (`strings_research/`)

This directory stores the cumulative multilingual research, bibliography, structural-invariant taxonomy, curriculum architecture, problem curation, and 10-iteration Phase 3 global audit records across 156+ iterative passes covering English (`[EN]`), Chinese (`[ZH]`), and Japanese (`[JA]`) competitive programming literature and online judges, supporting the 43-page **Advanced Strings & Word Combinatorics** textbook (`strings/`).

---

## 1. Master Completion Status Table (Phases 1, 1.5, 2 & 3 — 100% Complete)

| Phase | Milestone / Deliverable | Scope & Coverage | Verification Status |
| :--- | :--- | :--- | :---: |
| **Phase 1 (Cohorts 1–3)** | 30 Multilingual Wave Files (`iter_01_to_52`, `cohort2_iter_53_to_104`, `cohort3_wave_1a_to_5b`) | 156+ iterative passes across Waves `1A`–`5B` (`[EN]`, `[ZH]`, `[JA]`) | **100% Complete** |
| **Phase 1 Synthesis** | [`CITATIONS.md`](CITATIONS.md), [`problem_archive.md`](problem_archive.md), [`TECHNIQUE_TAXONOMY.md`](TECHNIQUE_TAXONOMY.md) | 220+ verified citations, 330 curated problems + 80 quarantined templates, 13-family invariant taxonomy | **100% Complete** |
| **Phase 1.5 Architecture** | Proposals `A`/`B`/`C`, Critics `1`/`2`, [`CURRICULUM_ARCHITECTURE.md`](CURRICULUM_ARCHITECTURE.md), [`PROBLEM_CURATION.md`](PROBLEM_CURATION.md) | 7-Part, 30-Chapter, 43-Page Textbook Blueprint & 330-Problem Bijective Assignment (`Zero Overlap`) | **100% Complete** |
| **Phase 2 Authoring** | 43 `.qmd` Pages in `strings/` + [`TEXTBOOK_AUTHORING_AUDIT.md`](TEXTBOOK_AUTHORING_AUDIT.md) | 4 Front-Matter Guides + 30 Core Chapters (`Ch 01`–`Ch 30`) + 7 Two-Stage Blind Checkpoints (`CP-I`–`CP-VII`) + 2 Capstones (`27,480+` lines) | **100% Complete** |
| **Phase 3 Global Audits** | 10 Independent Audit & Remediation Passes (`audits/phase3_iter01`–`iter10`) + [`tests/audit_strings_math.py`](../tests/audit_strings_math.py) | 12/12 Exact Python Stringology Oracles (`100% PASS`), 43/43 `.qmd` Quarto Render & Offline `.zip` Bundle Sign-Off | **100% Complete** |

---

## 2. Canonical Plan & Architectural Blueprints

- [`PLAN.md`](PLAN.md): **Master Implementation Plan & Multi-Cohort Research Roadmap** — Defines:
  1. **Master Coordinator & Subagent Delegation Mandate (`§0`)**: Lean orchestrator protocol delegating research, synthesis, curriculum redesign, authoring, and auditing to subagents (`invoke_subagent`).
  2. **Prerequisite Boundary (`§1`)**: Assumes black-box fluency in polynomial rolling hash, KMP, Z-algorithm, Aho–Corasick, Manacher, SA+LCP, standard SAM, and standard Eertree/PAM, and enforces the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**.
  3. **Post-Research Corpus-Driven Textbook Restructuring (`§2.4` & `§4`)**: Expands the initial 24-chapter seed into the 7-Part, 30-Chapter, 43-Page textbook architecture.
- [`TECHNIQUE_TAXONOMY.md`](TECHNIQUE_TAXONOMY.md): **13-Family Structural Word-Invariant & Substring Decomposition Taxonomy** — Maps 60+ advanced stringology theorems, 25 named boundary pitfalls (`BP-01`–`BP-25`), and 15 cross-paradigm bridges.
- [`CURRICULUM_ARCHITECTURE.md`](CURRICULUM_ARCHITECTURE.md): **Definitive 7-Part, 30-Chapter, 43-Page Textbook Architecture** — Synthesized from three independent competing proposals ([`curriculum_proposal_A.md`](curriculum_proposal_A.md), [`curriculum_proposal_B.md`](curriculum_proposal_B.md), [`curriculum_proposal_C.md`](curriculum_proposal_C.md)) and two adversarial critiques ([`curriculum_critic_1.md`](curriculum_critic_1.md), [`curriculum_critic_2.md`](curriculum_critic_2.md)).
- [`PROBLEM_CURATION.md`](PROBLEM_CURATION.md) & [`problem_archive.md`](problem_archive.md): **330-Problem Bijective Curation & 80-Problem Template Quarantine (`R-01`–`R-80`)** — Assigns 240 Chapter Ladder problems (`30 Chapters × 8 Problems`), 56 Two-Stage Blind Checkpoint problems (`7 Checkpoints × 8 Problems`), and 34 Grandmaster Synthesis & Flagship Reserve problems with zero duplicates and zero forward-reference violations.
- [`CITATIONS.md`](CITATIONS.md): **Master Multilingual Bibliography** — 220+ primary academic papers, China NOI/IOI National Team Candidate Papers (`国家集训队论文`, 2004–2024), Japanese stringology literature (`[JA]`), and online judge editorial archives.
- [`TEXTBOOK_AUTHORING_AUDIT.md`](TEXTBOOK_AUTHORING_AUDIT.md): **Phase 2 & Phase 3 Per-Page Authoring & Audit Tracker** across all 43 `.qmd` files in `strings/`.

---

## 3. Completed Phase 1 Wave Files (`strings_research/`, 30 Files Across 3 Cohorts)

- **Wave 1A (`iter_01_to_05` / `cohort2_iter_53_to_57` / `cohort3_wave_1a`)**: Structural Periodicity, Border Theory, Weak Periodicity Lemma, Border-Group Modulo Shortest Path (`[WC2016] 论战捆竹竿`), and Series-Link (`slink`) DP Acceleration on KMP & PAM (`CF 932G`, `CF 906E`).
- **Wave 1B (`iter_06_to_10` / `cohort2_iter_58_to_62` / `cohort3_wave_1b`)**: Lyndon Words, Duval's Algorithm, Significant Suffixes (`显著后缀`, `[ZJOI2017] 字符串`), Lyndon Arrays & Lyndon Trees, Three-Squares Lemma, and the Runs Theorem (`极长周期子串`, Bannai et al. 2017).
- **Wave 2A (`iter_11_to_15` / `cohort2_iter_63_to_67` / `cohort3_wave_2a`)**: Advanced Suffix Automaton (SAM), Generalized SAM (`广义 SAM`), CDAWG, SAM + Segment Tree Merging on $\text{endpos}$ (`[NOI2018] 你的名字`, `CF 1037H`), and Dynamic SAM + Link-Cut Tree (`access`) / HLD Coupling.
- **Wave 2B (`iter_16_to_20` / `cohort2_iter_68_to_72` / `cohort3_wave_2b`)**: Induced Sorting (SA-IS), Virtual Suffix Trees (`后缀树虚树`), Dominant Pairs (`启发式合并支配对`), Internal Pattern Matching (IPM) & Basic Substring Dictionary (`[BJWC2018] Border 的四种求法`, 2D SA Range Queries), and Bi-Directional Suffix Structures (SCDAWG, Suffix Balanced Trees `后缀平衡树`, Affix Automata).
- **Wave 3A (`iter_21_to_25` / `cohort2_iter_73_to_77` / `cohort3_wave_3a`)**: Deterministic & Double-Ended (Deque) PAM (`双向 PAM`), Persistent/Tree PAM, Substring Palindrome Range Queries ($S[l..r]$ Longest & Distinct Palindromes), Rich Words, and Inverse String Reconstruction.
- **Wave 3B (`iter_26_to_30` / `cohort2_iter_78_to_82` / `cohort3_wave_3b`)**: Algebraic / FFT String Matching (Wildcards, $k$-Mismatch Kangaroo + FFT, Involution Matching), Parameterized, Order-Preserving & Cartesian-Tree Matching, and Locally Consistent Parsing (`局部一致性剖析` / Jeż Recompression / SLPs).
- **Wave 4A (`iter_31_to_35` / `cohort2_iter_83_to_87` / `cohort3_wave_4a`)**: Goulden–Jackson Cluster Method, Autocorrelation Systems, String Martingales & PGFs (`康威赌博`, `[SDOI2017] 硬币游戏`), Bivariate Cluster Moments, and Automaton DP / DP-of-DP (`自動機上のDP`).
- **Wave 4B (`iter_36_to_40` / `cohort2_iter_88_to_92` / `cohort3_wave_4b`)**: Direct Acyclic Subsequence Graph (`序列自动机` / DASG), Arch Factorization & Simon's Congruence, Invertible Subsequence Matrices (`CF 750E`, `ABC 214F`), Tiskin's Seaweed Matrices (Unit-Monge Braid Multiplication for All-Pairs Interval LCS, `[THUPC 2021] 区间 LCS`), and Bit-Parallel LCS.
- **Wave 5A (`iter_41_to_45` / `cohort2_iter_93_to_97` / `cohort3_wave_5a`)**: Word Equations & Binary-Lifting DSU (`倍增并查集`, `[SCOI2016] 萌萌哒`), String Inequality Graphs, De Bruijn / Wheeler Graphs & BWT / Move Structures, and Strings on Trees (Tree SA, Tree GSAM, Centroid Decomposition + Automata).
- **Wave 5B (`iter_46_to_52` / `cohort2_iter_98_to_104` / `cohort3_wave_5b`)**: Combinatorics on Words (Sturmian Words, Fibonacci & Singular Words, Substitutive Morphisms $\varphi^k(S)$), Free Group / $SL_2(\mathbb{F}_p)$ Non-Abelian Stack Hashing & Stack-Trie Path LCE (`CF 1223F`), String Attractors & $\tau$-Synchronizing Sets, and Exhaustive Multilingual (`[ZH]` / `[JA]` / `[EN]`) Master Audit.

---

## 4. Phase 3 Multi-Agent Global Audit Reports (`strings_research/audits/`)

1. [`audits/phase3_iter01_notation_prereqs.md`](audits/phase3_iter01_notation_prereqs.md) — **Iteration 1**: Prerequisite Boundary & Notation Consistency Audit across all 43 `.qmd` files.
2. [`audits/phase3_iter02_periodicity_lyndon_runs_proofs.md`](audits/phase3_iter02_periodicity_lyndon_runs_proofs.md) — **Iteration 2**: Mathematical Proof Audit I (`Parts I & II`, `Ch 01`–`Ch 08`: Fine–Wilf, `slink` DP, Duval, Significant Suffixes, Runs).
3. [`audits/phase3_iter03_zero_magic_scratchpads.md`](audits/phase3_iter03_zero_magic_scratchpads.md) — **Iteration 3**: "Zero Magic Invariants" & Reverse-Engineering Scratchpad Audit across all 30 chapters.
4. [`audits/phase3_iter04_sam_endpos_lct_vst.md`](audits/phase3_iter04_sam_endpos_lct_vst.md) — **Iteration 4**: Mathematical Proof Audit II (`Part III`, `Ch 09`–`Ch 14`: GSAM, $\text{endpos}$ Clipping, LCT-SAM, SA-IS, Virtual Suffix Trees, CDAWG/SCDAWG).
5. [`audits/phase3_iter05_ipm_borders_pam.md`](audits/phase3_iter05_ipm_borders_pam.md) — **Iteration 5**: Mathematical Proof Audit III (`Part IV`, `Ch 15`–`Ch 17`: Internal Pattern Matching, 6-Method Borders, Deque PAM, Range LPS).
6. [`audits/phase3_iter06_fft_gj_seaweed.md`](audits/phase3_iter06_fft_gj_seaweed.md) — **Iteration 6**: Mathematical Proof Audit IV (`Parts V, VI & VII`, `Ch 18`–`Ch 30`: FFT Wildcards, `p-KMP`, SLPs, Subsequence Matrices, Seaweed $\boxdot$, Goulden–Jackson, Martingales, Signed DSU, RLBWT, Stack-Trie / $SL_2(\mathbb{F}_p)$, Sturmian & Morphic Words).
7. [`audits/phase3_iter07_problem_ladders_inline.md`](audits/phase3_iter07_problem_ladders_inline.md) — **Iteration 7**: Problem Ladders, Inline Statements, 3-Tier Hints, Full Solutions & Forward-Reference Audit (`240/240` chapter ladder problems).
8. [`audits/phase3_iter08_blind_checkpoints_hints.md`](audits/phase3_iter08_blind_checkpoints_hints.md) — **Iteration 8**: Blind Checkpoints (`CP-I`–`CP-VII`, `56/56` problems) & Capstones (`34/34` synthesis/flagship problems) Spoiler-Quarantine Audit.
9. [`audits/phase3_iter09_citations_links.md`](audits/phase3_iter09_citations_links.md) — **Iteration 9**: Citation, Attribution, External URL & Internal Cross-Link Audit (`100%` link resolution).
10. [`audits/phase3_iter10_oracle_quarto_signoff.md`](audits/phase3_iter10_oracle_quarto_signoff.md) — **Iteration 10+**: Exact Stringology Oracles (`tests/audit_strings_math.py`, `12/12 PASS`), Quarto Render (`43/43` HTML pages), Offline `.zip` Bundle Verification & Final Publishability Sign-Off.
