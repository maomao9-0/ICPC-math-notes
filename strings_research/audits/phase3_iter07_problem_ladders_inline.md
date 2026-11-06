# Phase 3 Global Audit Report — Iteration 07: Per-Chapter Smooth Difficulty Ladders & Inline Problem Statements/Constraints

- **Audit Target**: `§5` Curated 4-Tier Problem Ladders across all 30 chapters (`strings/chapters/ch01-*.qmd` through `strings/chapters/ch30-*.qmd`) and the 30 Synthesis Capstone Reserves (`Syn-01`–`Syn-30`) in `strings/capstones/synthesis.qmd`, cross-checked against `strings_research/PROBLEM_CURATION.md`, `strings_research/problem_archive.md`, and `strings/capstones/problem-archive-guide.qmd`.
- **Audit Status**: **100% PASS** (All **248** Chapter Ladder Problems and **30** Synthesis Capstone Problems verified and synchronized).

---

## 1. Executive Summary of Verification & Surgical Fixes

| Audit Criterion | Target Scope | Baseline Status | Post-Fix Verification |
| :--- | :--- | :--- | :--- |
| **1. Exact Problem Count & Cross-Ledger Bijection** | `248` Chapter Ladder Problems (`Ch 01`–`Ch 30`) + `30` Synthesis Problems (`Syn-01`–`Syn-30`) | `Ch 11`, `Ch 15`, `Ch 23`, `Ch 26` had 1 cross-chapter duplicate problem each (`252` raw blocks vs. `248` canonical); `PROBLEM_CURATION.md` and `problem_archive.md` Part VII totals and §7.2 `Syn-01`–`Syn-30` table had minor ledger drift | **100% PASS** (`248` Chapter Ladder Problems + `30` Synthesis Capstone Problems; exact 1-to-1 bijection across `.qmd` files, `PROBLEM_CURATION.md`, `problem_archive.md`, and `problem-archive-guide.qmd`) |
| **2. Self-Contained Inline Mathematical Statement & Exact Constraints** | All `248 + 30 = 278` problems | All problems contained inline mathematical statements and explicit constraints ($N, M, Q, |\Sigma|$, modulus, time/memory bounds) | **100% PASS** (`278 / 278` problems have self-contained mathematical definitions and explicit quantitative bounds) |
| **3. Smooth 4-Tier Progression** | `Stepping Stone` $\to$ `Intermediate` $\to$ `Advanced` $\to$ `Mastery` in all 30 chapters | All 30 chapters organized into explicit 4-tier monotonic difficulty ladders (`2` Stepping Stone $\to$ `2` Intermediate $\to$ `2` Advanced $\to$ `2–3` Mastery) | **100% PASS** (`30 / 30` chapters verified) |
| **4. Three Progressive Collapsible Hints (`Hint 1`, `Hint 2`, `Hint 3`)** | `3` separate `::: {.callout-note collapse="true"}` blocks per problem (`834` hint callouts total) | `Ch 07` (`8` problems) and `Ch 08` (`9` problems) bundled Hints 1–3 into a single callout; `Ch 03`–`Ch 06`, `Ch 09`–`Ch 12`, `Ch 28`–`Ch 29`, and `synthesis.qmd` used `.callout-tip` for hints instead of `.callout-note` | **100% PASS** (`278 / 278` problems have `3` separate collapsible `callout-note` blocks for `Hint 1`, `Hint 2`, `Hint 3`) |
| **5. Complete Collapsible 4-Step Derivation & Solution** | `1` `::: {.callout-tip collapse="true"}` block per problem with explicit 4-Step structure (`278` solution callouts total) | `Ch 03`–`Ch 12`, `Ch 28`–`Ch 29`, and `synthesis.qmd` used `.callout-note` (or `.callout-warning` in `Ch 07`–`Ch 08`) for solutions; `Ch 18` (`2` problems), `Ch 19` (`6` problems), and `synthesis.qmd` (`28` problems) merged steps 2–3 into 2–3 numbered items | **100% PASS** (`278 / 278` problems use `::: {.callout-tip collapse="true"}` with an explicit 4-Step Derivation & Solution) |

---

## 2. Surgical Fixes Applied

1. **Cross-Chapter Deduplication & Canonical `248`-Problem Bijection**:
   - `strings/chapters/ch11-dynamic-sam-lct-stratification.qmd`: Removed cross-chapter duplicate `Problem 11.7 (W2A-40 / CF 1098F)` (canonically covered as `Problem 13.9` in `Ch 13`) and renumbered `11.8–11.9` $\to$ `11.7–11.8` (`8` problems).
   - `strings/chapters/ch15-internal-pattern-matching-borders.qmd`: Removed cross-chapter duplicate `Problem 15.7 (W2B-35 / CF 1043G)` (canonically covered in `Ch 08`, `Ch 13`, and `Syn-01`) and renumbered `15.8–15.9` $\to$ `15.7–15.8` (`8` problems).
   - `strings/chapters/ch23-bit-parallel-lcs-seaweed-matrices.qmd`: Removed redundant `Problem 23.7 (W4B-37)` (covered in `Ch 25` `W4A-30`) and renumbered `23.8–23.9` $\to$ `23.7–23.8` (`8` problems).
   - `strings/chapters/ch26-word-equations-signed-parallel-dsu.qmd`: Removed cross-chapter duplicate `Problem 26.5 (W5A-33 / LOJ 6436)` (canonically covered in `Ch 18` and `Ch 27`) and renumbered `26.6–26.9` $\to$ `26.5–26.8` (`8` problems).
   - Synchronized Part VII counts (`8 + 8 + 8 + 8 + 9 = 41`, pairing `W5B-15 / W5B-22` in `Problem 29.6` of `Ch 29` and `9` problems in `Ch 30`) and the `Syn-01`–`Syn-30` table across `strings_research/PROBLEM_CURATION.md`, `strings_research/problem_archive.md`, and `strings/capstones/problem-archive-guide.qmd`.

2. **Progressive Hint Splitting (`Ch 07` & `Ch 08`)**:
   - Split the consolidated `Progressive Hints (1 -> 2 -> 3)` block in all `8` problems of `strings/chapters/ch07-lyndon-arrays-cartesian-trees.qmd` and all `9` problems of `strings/chapters/ch08-runs-theorem-squares-sweep.qmd` into **3 separate collapsible hint callouts** (`Hint 1 — Diagnostic Signal`, `Hint 2 — Combinatorial Word Invariant`, `Hint 3 — Algorithmic Assembly`), and normalized top-level section numbering `## 7.k` / `## 8.k` $\to$ `## k.`.

3. **Callout Class Standardization (`callout-note` for Hints, `callout-tip` for Solutions)**:
   - Standardized all hint and solution callouts in `§5` of `Ch 03`, `Ch 04`, `Ch 05`, `Ch 06`, `Ch 07`, `Ch 08`, `Ch 09`, `Ch 10`, `Ch 11`, `Ch 12`, `Ch 28`, `Ch 29`, and `strings/capstones/synthesis.qmd` so that every problem across the entire textbook uses `::: {.callout-note collapse="true"}` for `Hint 1`–`Hint 3` and `::: {.callout-tip collapse="true"}` for the 4-Step Derivation & Solution.

4. **Explicit 4-Step Derivation Normalization (`Ch 18`, `Ch 19`, `synthesis.qmd`)**:
   - Expanded merged step numbering in `strings/chapters/ch18-fft-wildcard-involution-matching.qmd` (`Problem 18.6`, `18.8`), `strings/chapters/ch19-kmismatch-wavefront-period-dichotomy.qmd` (`Problem 19.2`, `19.3`, `19.4`, `19.6`, `19.7`, `19.8`), and `strings/capstones/synthesis.qmd` (`Syn-02`–`Syn-30`) so every solution callout explicitly presents all 4 steps (`1.`, `2.`, `3.`, `4.`).

---

## 3. Chapter-by-Chapter Audit Matrix (`248` Chapter Problems + `30` Synthesis Capstones)

| Chapter / File | Count | Tier Split (`T1/T2/T3/T4`) | Archive IDs (`PROBLEM_CURATION.md` & `problem_archive.md`) | Inline Statement & Constraints | `3` Collapsible Hints (`callout-note`) | `1` Collapsible 4-Step Solution (`callout-tip`) | Status |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| **`Ch 01`** (`ch01-fine-wilf-periodicity-orbits.qmd`) | **8** | `2 / 2 / 2 / 2` | `W1A-02`, `W1A-04`, `W1A-06`, `W1A-08`, `W1A-10`, `W1A-28`, `W1A-12`, `W1A-40` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 02`** (`ch02-weak-periodicity-border-aps.qmd`) | **8** | `2 / 2 / 2 / 2` | `W1A-01`, `W1A-05`, `W1A-07`, `W1A-11`, `W1A-09`, `W1A-13`, `W1A-29`, `W1A-35` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 03`** (`ch03-border-modulo-shortest-path.qmd`) | **8** | `2 / 2 / 2 / 2` | `W1A-15`, `W1A-16`, `W1A-17`, `W1A-18`, `W1A-14`, `W1A-19`, `W1A-20`, `W1A-41` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 04`** (`ch04-series-link-dp-kmp-pam.qmd`) | **9** | `2 / 2 / 2 / 3` | `W1A-03`, `W1A-22`, `W1A-21`, `W1A-24`, `W1A-23`, `W1A-25`, `W1A-26`, `W1A-42`, `W1A-43` | PASS | `27 / 27` | `9 / 9` | **PASS** |
| **`Ch 05`** (`ch05-lyndon-factorization-duval-necklaces.qmd`) | **8** | `2 / 2 / 2 / 2` | `W1B-02`, `W1B-05`, `W1B-15`, `W1B-18`, `W1B-35`, `W1B-21`, `W1B-36`, `W1B-38` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 06`** (`ch06-significant-suffixes-substrings.qmd`) | **8** | `2 / 2 / 2 / 2` | `W1B-08`, `W1B-03`, `W1B-20`, `W1B-24`, `W1B-22`, `W1B-25`, `W1B-37`, `W1B-41` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 07`** (`ch07-lyndon-arrays-cartesian-trees.qmd`) | **8** | `2 / 2 / 2 / 2` | `W1B-01`, `W1B-06`, `W1B-19`, `W1B-26`, `W1B-28`, `W1B-39`, `W1B-30`, `W1B-42` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 08`** (`ch08-runs-theorem-squares-sweep.qmd`) | **9** | `2 / 2 / 2 / 3` | `W1B-04`, `W1B-09`, `W1B-27`, `W1B-29`, `W1B-31`, `W1B-32`, `W1B-34`, `W1B-33`, `W1B-40` | PASS | `27 / 27` | `9 / 9` | **PASS** |
| **`Ch 09`** (`ch09-sam-duality-gsam-trie-bfs.qmd`) | **8** | `2 / 2 / 2 / 2` | `W2A-01`, `W2A-02`, `W2A-04`, `W2A-06`, `W2A-08`, `W2A-11`, `W2A-14`, `W2A-17` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 10`** (`ch10-sam-endpos-segtree-merge.qmd`) | **9** | `2 / 2 / 2 / 3` | `W2A-05`, `W2A-18`, `W2A-12`, `W2A-19`, `W2A-20`, `W2A-22`, `W2A-21`, `W2A-23`, `W2A-25` | PASS | `27 / 27` | `9 / 9` | **PASS** |
| **`Ch 11`** (`ch11-dynamic-sam-lct-stratification.qmd`) | **8** | `2 / 2 / 2 / 2` | `W2A-26`, `W2A-32`, `W2A-35`, `W2A-36`, `W2A-37`, `W2A-42`, `W2A-39`, `W2A-43` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 12`** (`ch12-sais-induced-sorting-lcp.qmd`) | **8** | `2 / 2 / 2 / 2` | `W2B-01`, `W2B-02`, `W2B-04`, `W2B-06`, `W2B-05`, `W2B-09`, `W2B-10`, `W2B-12` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 13`** (`ch13-virtual-suffix-trees-dominant-pairs.qmd`) | **9** | `2 / 2 / 2 / 3` | `W2B-13`, `W2B-15`, `W2B-14`, `W2B-16`, `W2B-17`, `W2B-22`, `W2B-18`, `W2B-21`, `W2A-40` | PASS | `27 / 27` | `9 / 9` | **PASS** |
| **`Ch 14`** (`ch14-cdawg-scdawg-suffix-balanced-trees.qmd`) | **8** | `2 / 2 / 2 / 2` | `W2B-41`, `W2B-46`, `W2B-42`, `W2B-47`, `W2B-44`, `W2B-43`, `W2B-45`, `W2B-48` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 15`** (`ch15-internal-pattern-matching-borders.qmd`) | **8** | `2 / 2 / 2 / 2` | `W2B-26`, `W2B-27`, `W2B-29`, `W2B-31`, `W2B-34`, `W2B-38`, `W2B-36`, `W2B-40` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 16`** (`ch16-deterministic-tree-deque-pam.qmd`) | **8** | `2 / 2 / 2 / 2` | `W3A-01`, `W3A-05`, `W3A-06`, `W3A-08`, `W3A-18`, `W3A-21`, `W3A-16`, `W3A-35` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 17`** (`ch17-range-palindromes-rich-words.qmd`) | **9** | `2 / 2 / 2 / 3` | `W3A-03`, `W3A-28`, `W3A-29`, `W3A-36`, `W3A-25`, `W3A-26`, `W3A-31`, `W3A-32`, `W3A-40` | PASS | `27 / 27` | `9 / 9` | **PASS** |
| **`Ch 18`** (`ch18-fft-wildcard-involution-matching.qmd`) | **8** | `2 / 2 / 2 / 2` | `W3B-01`, `W3B-05`, `W3B-04`, `W3B-12`, `W3B-02`, `W3B-21`, `W3B-24`, `W3B-37` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 19`** (`ch19-kmismatch-wavefront-period-dichotomy.qmd`) | **8** | `2 / 2 / 2 / 2` | `W3B-15`, `W3B-08`, `W3B-20`, `W3B-25`, `W3B-27`, `W3B-30`, `W3B-38`, `W3B-41` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 20`** (`ch20-structural-isomorphism-weighted-strings.qmd`) | **8** | `2 / 2 / 2 / 2` | `W3B-17`, `W3B-18`, `W3B-23`, `W3B-29`, `W3B-28`, `W3B-31`, `W3B-39`, `W3B-42` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 21`** (`ch21-locally-consistent-parsing-slp-attractors.qmd`) | **8** | `2 / 2 / 2 / 2` | `W3B-19`, `W3B-32`, `W3B-34`, `W3B-36`, `W3B-33`, `W3B-35`, `W3B-40`, `W3B-43` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 22`** (`ch22-dasg-arch-simon-invertible-matrices.qmd`) | **9** | `2 / 2 / 2 / 3` | `W4B-01`, `W4B-02`, `W4B-05`, `W4B-10`, `W4B-04`, `W4B-13`, `W4B-16`, `W4B-33`, `W4B-39` | PASS | `27 / 27` | `9 / 9` | **PASS** |
| **`Ch 23`** (`ch23-bit-parallel-lcs-seaweed-matrices.qmd`) | **8** | `2 / 2 / 2 / 2` | `W4B-20`, `W4B-38`, `W4B-22`, `W4B-35`, `W4B-21`, `W4B-26`, `W4B-27`, `W4B-41` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 24`** (`ch24-goulden-jackson-moment-shift-fps.qmd`) | **8** | `2 / 2 / 2 / 2` | `W4A-01`, `W4A-02`, `W4A-03`, `W4A-08`, `W4A-10`, `W4A-13`, `W4A-18`, `W4A-35` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 25`** (`ch25-martingale-pgfs-automaton-dp-of-dp.qmd`) | **9** | `2 / 2 / 2 / 3` | `W4A-05`, `W4A-04`, `W4A-06`, `W4A-22`, `W4A-20`, `W4A-30`, `W4A-23`, `W4A-25`, `W4A-38` | PASS | `27 / 27` | `9 / 9` | **PASS** |
| **`Ch 26`** (`ch26-word-equations-signed-parallel-dsu.qmd`) | **8** | `2 / 2 / 2 / 2` | `W5A-01`, `W5A-02`, `W5A-04`, `W5A-08`, `W5A-06`, `W5A-35`, `W5A-47`, `W5A-50` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 27`** (`ch27-inverse-reconstruction-inequality-dags.qmd`) | **8** | `2 / 2 / 2 / 2` | `W5A-11`, `W5A-16`, `W5A-12`, `W5A-15`, `W5A-13`, `W5A-29`, `W5A-48`, `W5A-49` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 28`** (`ch28-debruijn-best-bwt-wheeler-rlbwt.qmd`) | **8** | `2 / 2 / 2 / 2` | `W5A-17`, `W5A-19`, `W5A-23`, `W5A-27`, `W5A-26`, `W5A-40`, `W5A-41`, `W5A-42` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 29`** (`ch29-tree-strings-stack-trie-sl2-hashing.qmd`) | **8** | `2 / 2 / 2 / 2` | `W5B-01`, `W5B-02`, `W5B-03`, `W5B-16`, `W5B-04`, `W5B-15 / W5B-22`, `W5B-07`, `W5B-42 / W5B-50` | PASS | `24 / 24` | `8 / 8` | **PASS** |
| **`Ch 30`** (`ch30-sturmian-singular-thue-morse-morphic-2d.qmd`) | **9** | `2 / 2 / 2 / 3` | `W5B-19`, `W5B-28`, `W5B-29`, `W5B-36`, `W5B-30`, `W5B-39`, `W5B-31`, `W5B-33`, `W5B-46` | PASS | `27 / 27` | `9 / 9` | **PASS** |
| **`Synthesis`** (`strings/capstones/synthesis.qmd`) | **30** | `Syn-01`–`Syn-30` | `W2B-36S` through `W4B-47` (`30` multi-chapter reserves) | PASS | `90 / 90` | `30 / 30` | **PASS** |
| **TOTAL** | **278** | **`248` Ch + `30` Syn** | **100% Bijection Verified** | **278 / 278** | **834 / 834** | **278 / 278** | **100% PASS** |
