# Phase 1.5 Curriculum Audit Report — Critic 2: Cognitive Load, Pedagogical Coherence & Blind Checkpoint Boundary Auditor (`strings_research/curriculum_critic_2.md`)

> [!IMPORTANT]
> **Audit Scope & Methodology**
> This report audits Post-Research Curriculum Proposals **A** ([curriculum_proposal_A.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/strings_research/curriculum_proposal_A.md)), **B** ([curriculum_proposal_B.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/strings_research/curriculum_proposal_B.md)), and **C** ([curriculum_proposal_C.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/strings_research/curriculum_proposal_C.md)) against the 57-technique master inventory ([TECHNIQUE_TAXONOMY.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/strings_research/TECHNIQUE_TAXONOMY.md)) and repository conventions ([_quarto.yml](file:///home/maomao90/Documents/IO/ICPC-math-notes/_quarto.yml)) along three axes:
> 1. **Chapter-Level Cognitive Load & Thematic Cohesion** (eliminating chapters that conflate orthogonal mathematical invariants or heavy data structures, and eliminating cross-chapter forward references).
> 2. **Blind Checkpoint (`CP-I`–`CP-VII`) Diagnostic Discrimination** (ensuring every Part groups techniques that share deceptive surface contest symptoms so each Part-End Blind Checkpoint tests genuine diagnostic routing across 4–6 chapters).
> 3. **Naming, Slug & Quarto Sidebar Ergonomics** (enforcing exact `ch01-..` to `ch30-..` and `cp01-part1-..` to `cp07-part7-..` parity with `fps/` and `flows/` inside a `270px` docked Quarto sidebar).

---

## 1. Audit Axis I: Chapter-Level Cognitive Load, Invariant Cohesion & Part-by-Part Synthesis

An expert competitive programmer learning advanced stringology from first principles does not struggle with standard library templates; cognitive overload occurs when a single chapter demands mastering **two or more unrelated combinatorial word invariants** or **incompatible data-structure engines** simultaneously. Below we audit every chapter across Proposals A, B, and C that mixes unrelated mathematical invariants, and select the cleanest split for `Part I` through `Part VII`.

### 1.1 Specific Chapter-Level Invariant Collisions Identified Across Proposals A, B, and C

| Proposal & Chapter | Mixed Techniques | Cognitive-Load & Pedagogical Cohesion Defect | Recommended Resolution |
| :--- | :--- | :--- | :--- |
| **Prop B `Ch 12`** | `T-2B-01`, `T-2B-02`, `T-2B-03` | Packs **Induced Sorting (`SA-IS`) + Fischer LCP + `AGC 060 D` $\text{rk}$-descents**, **Zero-Tree Virtual Suffix Trees (`CF 1073G`)**, and **DSU-on-Tree Dominant Pairs (`启发式合并支配对`, `CF 1043G`)** into a single 9-problem chapter. Each has a heavy, distinct proof and failure mode. | **Adopt Proposal A's 3-way split (`Ch 12`–`Ch 14`)**: `Ch 12` (`SA-IS` + Fischer LCP + 3-Way Isomorphism), `Ch 13` (Virtual Suffix Trees + DSU-on-Tree Dominant Pairs), `Ch 14` (`CDAWG` + `SCDAWG` + Suffix Balanced Trees). |
| **Prop C `Ch 13`** | `T-2B-03`, `T-2B-05`, `T-2B-06` | Pairs static offline **DSU-on-Tree Dominant Pairs** (`T-2B-03`, 2D sweep-line over tree predecessor/successor events) with online **Bi-Directional `SCDAWG`** (`T-2B-05`) and **Dietz–Sleator Scapegoat Suffix Balanced Trees** (`T-2B-06`). | Move `T-2B-03` (Dominant Pairs) into `Ch 13` alongside Virtual Suffix Trees (`T-2B-02`), and group `CDAWG` (`T-2A-02`), `SCDAWG` (`T-2B-05`), and Suffix Balanced Trees (`T-2B-06`) in `Ch 14` (Proposal A). |
| **Prop A `Ch 16`** | `T-3A-01`, `T-3A-02`, `T-3A-05` | Mixes worst-case pointer mechanics (`quick_link` / `slink`-skip Tree PAM and 4-Way Deque PAM lazy surface push-down) with pure word combinatorics (Droubay–Pirillo Rich Words, `CF 1827C` even-palindrome greedy, and $\theta$-palindromes). | **Adopt Proposal B's split (`Ch 16`–`Ch 17`)**: dedicate `Ch 16` exclusively to **Unamortized, Tree & 4-Way Deque PAM Mechanics** (`T-3A-01`, `T-3A-02`), and pair `T-3A-05` (Rich Words & Palindrome Factorizations) with Range Palindromes (`T-3A-03`, `T-3A-04`) in `Ch 17`. |
| **Prop C `Ch 17`** | `T-3A-05`, `T-3A-06` | Couples palindromic factorization combinatorics (`T-3A-05`) with **Inverse String Reconstruction from KMP/Z/Manacher** (`T-3A-06`), separating `T-3A-06` from its natural twin **Suffix Array Adjacency & String Inequality Digraphs** (`T-5A-03`). | **Adopt Proposal A/B (`Ch 27`)**: unify Inverse Reconstruction (`T-3A-06`) and String Inequality Digraphs / SA Adjacency (`T-5A-03`) under their shared **Equality DSU + Forbidden/Directed DAG Chromatic Invariant**. |
| **Prop C `Ch 19`** | `T-3B-03`, `T-3B-04`, `T-5B-06` | Squeezes Landau–Vishkin Kangaroo jumps, Abrahamson heavy–light, the **Clifford–Gawrychowski–Uznański $O(N\sqrt{k\log k})$ $2k$-Period Dichotomy** (`T-3B-03`), `p-KMP`, `p-SA`, `Order-KMP`, `Cartesian-KMP` (`T-3B-04`), and **$1/z$ Weighted Suffix Trees** (`T-5B-06`) into one overloaded chapter. | **Adopt Proposal A (`Ch 19` & `Ch 20`)**: dedicate `Ch 19` solely to **$k$-Mismatch / $k$-Edit & the $2k$-Period Dichotomy** (`T-3B-03`), and `Ch 20` to **Window-Clipped Structural Isomorphisms (`p-KMP`, `Order-KMP`, `Cartesian-KMP`) & $1/z$ Weighted Strings** (`T-3B-04`, `T-5B-06`). |
| **Prop B `Ch 20`** | `T-3B-04`, `T-5B-06`, `T-5B-07` | Attaches **2D Periodicity Lattices, Baker–Bird & Vishkin's 2D Witness Duel** (`T-5B-07`) onto 1D window-clipped structural KMP (`T-3B-04`), forcing a 1D-to-2D context switch mid-chapter. | Keep `Ch 20` purely 1D (`T-3B-04` + `T-5B-06`, Proposal A) and place 2D Periodicity & Baker–Bird/Vishkin Duel (`T-5B-07`) in `Ch 30` alongside multidimensional/morphic periodicity (Proposal A/C). |
| **Prop B `Ch 21`** | `T-4A-01`–`T-4A-04` | Merges deterministic **Goulden–Jackson Cluster OGFs, Bivariate $(t-1)$ Exact-$k$ FPS & the `UCup` $t=1+u$ Moment Shift** (`T-4A-01..03`) with stochastic **Conway's Casino Martingales, Optional Stopping & Pattern Races** (`T-4A-04`)—4 dense techniques in one chapter. | **Adopt Proposal A/C's 2-chapter split**: `Ch 22` for Goulden–Jackson, Bivariate $(t-1)$ FPS & the $t=1+u$ Binomial Moment Shift (`T-4A-01..03`), and `Ch 23` for Conway's Casino Martingale PGFs & Pattern Races (`T-4A-04`). |
| **Prop A `Ch 23` vs `Ch 25`** | `T-4A-05` before `T-4B-05` | **Hidden Forward Reference**: Proposal A teaches LCS `DP套DP` (`[TJOI2018] 游园会`, `T-4A-05`) in `Ch 23` *before* teaching the **4-instruction Allison–Dix hardware borrow identity** ($V' = X \mathbin{\&} \sim(X-Y)$, `T-4B-05`) in `Ch 25`, even though LCS `DP套DP` uses the Allison–Dix bitmask transition as its inner DFA step! | **Hybrid B/C Fix inside Part VI**: teach **Bit-Parallel Alignment (`T-4B-05`) + `DP套DP` Compiler (`T-4A-05`)** together (or place Subsequence/Bit-Parallel/Seaweed before `DP套DP` inside Part VI) so the Allison–Dix difference encoding is derived immediately before `DP套DP` consumes it. |
| **Prop C `Ch 26`** | `T-5A-04`, `T-5A-05`, `T-5A-06` | Mixes **Eulerian De Bruijn / AC-DFA BEST Theorem** (`T-5A-04`) and **Wheeler Graphs / $O(1)$ RLBWT Move Structures** (`T-5A-05`) with **Strings on Trees: Dual-Rank Tree SA, Tree GSAM & `[CTSC2010] 珠宝商` Centroid Dual-SAM** (`T-5A-06`). | **Adopt Proposal A (`Ch 28` & `Ch 29`)**: dedicate `Ch 28` to De Bruijn, AC-DFA BEST, BWT/BBWT, Wheeler Graphs & $O(1)$ RLBWT Move Structures (`T-5A-04`, `T-5A-05`), and `Ch 29` to Strings on Trees + Tree Binary-Lifting DSU + Stack-Trie Path Isomorphism (`T-5A-06`, `T-5A-02`, `T-5B-04`). |

---

### 1.2 Part-by-Part Selection of the Cleanest Split (`Part I`–`Part VII`)

1. **Part I (`Ch 01`–`Ch 04`): Unanimous Consensus Across A, B, and C**
   - All three proposals identically partition Wave 1A into `Ch 01` (Fine–Wilf & Sub-Threshold Orbits `T-1A-01`), `Ch 02` (Weak Periodicity, Border APs & `slink` vs. `anc` `T-1A-02`), `Ch 03` (Border-Group Modulo Shortest Path `T-1A-03`), and `Ch 04` (`slink` DP on PAM/KMP + Polynomial/Windowed `slink` DP `T-1A-04`, `T-1A-05`). Cognitive load is ideal ($1.25$ IDs/chapter).
2. **Part II (`Ch 05`–`Ch 08`): Unanimous Consensus Across A, B, and C (with Proposal A's `T-1B-02` Bridge)**
   - All three proposals identically assign `Ch 05` (CFL, Duval, All-Prefix State Sharing, RLE Duval & Witt/FKM/BBWT Cycle Bijection `T-1B-01`, `T-1B-02`), `Ch 06` (Significant Suffixes, 1-Survivor `pushup` & Dyadic SA-RMQ `T-1B-03`), `Ch 07` (Lyndon Arrays $\lambda_<, \lambda_>$ & Min-Cartesian Lyndon Tree `T-1B-04`), and `Ch 08` (Bannai et al. Runs Theorem, Three-Squares Lemma & 2D Run Sweeps `T-1B-05`, `T-1B-06`). Proposal A's explicit split of `T-1B-02` (Witt's Necklace Formula & Lyndon-Cycle Bijection in `Ch 05` $\to$ LF-Mapping & Multi-Cycle `BBWT` Inversion in `Ch 28`) cleanly eliminates duplication with `T-5A-05`.
3. **Part III (`Ch 09`–`Ch 14`): Select Proposal A's 6-Chapter Architecture**
   - Proposals B and C compress Wave 2A + Wave 2B (excluding `T-2B-04`) into 5 chapters by overloading either `Ch 12` (Proposal B) or `Ch 13` (Proposal C). **Proposal A's 6-chapter Part III (`Ch 09`–`Ch 14`)** is significantly cleaner:
     - `Ch 09`: SAM $\leftrightarrow \text{ST}(S^R)$ Duality, 3-Case Trie-BFS GSAM & Unamortized Persistent SAM (`T-2A-01`, `T-2A-02` persistent half).
     - `Ch 10`: SAM + Persistent Segment Tree Merging on $\text{endpos}$ & Substring Containment Clipping (`T-2A-03`).
     - `Ch 11`: Dynamic SAM + LCT `access` Color-Chain Sweeping & Intra-State Length Stratification (`T-2A-04`, `T-2A-05`).
     - `Ch 12`: Linear-Time Induced Sorting (`SA-IS`), Fischer's $O(N)$ LCP, $\text{rk}$-Descent Duality & 3-Way Suffix Tree Isomorphism (`T-2B-01`, `T-2B-02` foundation).
     - `Ch 13`: Zero-Tree Substring Virtual Suffix Trees & DSU-on-Tree Dominant Pairs (`启发式合并支配对`) (`T-2B-02` virtual half, `T-2B-03`).
     - `Ch 14`: Compact & Bi-Directional Suffix Structures — `CDAWG`, `SCDAWG` & Hash-Free Suffix Balanced Trees (`后缀平衡树`) (`T-2A-02` CDAWG half, `T-2B-05`, `T-2B-06`).
4. **Part IV (`Ch 15`–`Ch 17`): Select Proposal A's 3-Chapter Core with Proposal B's `Ch 16`/`Ch 17` Internal Split**
   - Proposal B places Locally Consistent Parsing & Attractors (`T-3B-05`, `T-5B-05`, `T-5B-08`) inside Part IV (`Ch 15`), interrupting the transition from Internal Pattern Matching (`[BJWC2018]`) to Palindromic Structures. Proposal A's 3-chapter Part IV (`Ch 15`–`Ch 17`) keeps Part IV focused on **Internal Substring Queries & Palindromic Engines**, while adopting Proposal B's cleaner boundary between `Ch 16` (`T-3A-01`, `T-3A-02`: Deterministic/Tree PAM & 4-Way Deque PAM) and `Ch 17` (`T-3A-03`, `T-3A-04`, `T-3A-05`: $O(1)$ Range LPS, `slink` Telescoping Range Distinct Palindromes, Rich Words & Palindrome Factorizations).
5. **Part V (`Ch 18`–`Ch 21`): Select Proposal A's 4-Chapter Architecture**
   - Proposal A's Part V cleanly separates: `Ch 18` (1-NTT Wildcards, Kalai Projection, 3-in-2 FFT, Involution & Affine/Bucket Matching `T-3B-01`, `T-3B-02`), `Ch 19` ($k$-Mismatch Kangaroo Jumps, Wavefronts & $O(N\sqrt{k\log k})$ $2k$-Period Dichotomy `T-3B-03`), `Ch 20` (Window-Clipped Structural KMP `p-KMP`/`Order-KMP`/`Cartesian-KMP`, `p-SA`, Abelian & $1/z$ Weighted Suffix Trees `T-3B-04`, `T-5B-06`), and `Ch 21` (Locally Consistent Parsing, Jeż Recompression SLPs, String Attractors $\gamma(S)$, $\tau$-Synchronizing Sets & LZ77/SLP 2D Indexing `T-3B-05`, `T-5B-05`, `T-5B-08`).
6. **Part VI (`Ch 22`–`Ch 25`): Select Proposal A's 4-Chapter Scope with Reordered Internal Sequence (`Ch 22`–`Ch 25`) to Fix the Allison–Dix Dependency**
   - To preserve Proposal A's 1-chapter-per-engine clarity while eliminating Proposal A's forward reference between `DP套DP` (`T-4A-05`) and Bit-Parallel LCS (`T-4B-05`), order Part VI (`Ch 22`–`Ch 25`) as:
     - `Ch 22`: Subsequence Automata (`DASG`), Arch Factorization, Simon's Congruence ($\sim_k$) & Matrix-Free $O(|\Sigma|)$ Invertible Subsequence Matrices (`T-4B-01`, `T-4B-02`, `T-4B-03`).
     - `Ch 23`: Bit-Parallel Alignment (`Allison–Dix`, `Myers`, `Hirschberg`) & Tiskin's Seaweed Matrices (`海草矩阵`, Unit-Monge $\boxdot$, $O(N\log^2 N)$ Range LIS) (`T-4B-05`, `T-4B-04`).
     - `Ch 24`: The Goulden–Jackson Cluster Method, Bivariate $(t-1)$ Exact-$k$ FPS & the $t = 1 + u$ Binomial Moment Shift (`T-4A-01`, `T-4A-02`, `T-4A-03`).
     - `Ch 25`: Conway's Casino Martingale PGFs, Pattern Races (`[SDOI2017]`), the 4-Stage `DP套DP` Compiler (consuming `Ch 23`'s Allison–Dix bitmask!) & Binary-Grouped Dynamic AC (`T-4A-04`, `T-4A-05`).
7. **Part VII (`Ch 26`–`Ch 30`): Select Proposal A's 5-Chapter Architecture**
   - Proposal A's Part VII (`Ch 26`–`Ch 30`) achieves the tightest thematic cohesion:
     - `Ch 26`: Word Equations, Signed Binary-Lifting DSU (`倍增并查集`, `is_pal[k][r]`) & $N \le 10^{18}$ Euclidean Period Folding (`T-5A-01`, `T-5A-02` huge-$N$ half).
     - `Ch 27`: Inverse String Reconstruction (`KMP`/`Z`/`Manacher`/`SA`) & String Inequality Digraphs (`T-3A-06`, `T-5A-03`).
     - `Ch 28`: De Bruijn Graphs, the AC-DFA BEST Theorem, BWT/`BBWT`, Wheeler Graphs & Nishimoto–Tabei $O(1)$ RLBWT Move Structures (`T-5A-04`, `T-5A-05`, `T-1B-02` inversion half).
     - `Ch 29`: Strings on Trees (`Dual-Rank Tree SA`, `Tree GSAM`, `[CTSC2010] 珠宝商` Centroid Dual-SAM), Signed Tree Binary-Lifting DSU, Stack-Trie Path Isomorphism & Non-Abelian $SL_2(\mathbb{F}_p)$ Group Hashing (`T-5A-06`, `T-5A-02` tree half, `T-5B-04`)—unifying tree-path string indexing with Stack-Trie LCA/LCE!
     - `Ch 30`: Combinatorics on Words — Sturmian & Rytter's Singular Words (`[周任飞 2017]`), Thue–Morse Anti-Hash, Iterated Morphisms $\varphi^k(S_0)$ & 2D Periodicity Lattices (`T-5B-01`, `T-5B-02`, `T-5B-03`, `T-5B-07`).

---

## 2. Audit Axis II: Blind Checkpoint (`CP-I`–`CP-VII`) Diagnostic Discrimination

A Part-End Blind Checkpoint (`CP-I` through `CP-VII`) only succeeds if the chapters inside that Part share **competing surface contest symptoms** (so the reader cannot guess the technique from the problem domain alone and must diagnose the underlying combinatorial invariant).

| Blind Checkpoint | Recommended Part Boundary | Competing Contest Symptoms & Diagnostic Discrimination Tested | Comparative Verdict (A vs. B vs. C) |
| :--- | :--- | :--- | :--- |
| **`CP-I`** (`Part I`: `Ch 01`–`Ch 04`, 4 ch) | Periodicity, Border APs & `slink` DP | All problems involve **overlapping borders or palindromic prefixes/suffixes**. Discriminates: (1) static dual-period orbit counting (`Ch 01`) vs. (2) online active border weight maintenance (`Ch 02`) vs. (3) $W \le 10^{18}$ unbounded border-overlap concatenation (`Ch 03`) vs. (4) 1D partition DP / interleaved `CF 932G`/`906E` / binomial moment `slink` DP (`Ch 04`). | **Tie (A = B = C)**: 4 chapters, razor-sharp diagnostic boundary. |
| **`CP-II`** (`Part II`: `Ch 05`–`Ch 08`, 4 ch) | Lyndon Theory, Significant Suffixes & Runs | All problems involve **lexicographical order or periodic square/run structure**. Discriminates: (1) global/all-prefix CFL & RLE Duval (`Ch 05`) vs. (2) range/extension-sensitive minimum suffix/cyclic shift via $|\text{Cand}| \le \log_2 N + 1$ (`Ch 06`) vs. (3) Lyndon Tree Cartesian merges (`Ch 07`) vs. (4) 2D sweep-line over Runs / Three-Squares (`Ch 08`). | **Tie (A = B = C)**: 4 chapters, exemplary diagnostic contrast between Duval (`Ch 05`) and Significant Suffixes (`Ch 06`). |
| **`CP-III`** (`Part III`: `Ch 09`–`Ch 14`, 6 ch) | SAM/GSAM, Endpos Merge, LCT, SA-IS, Dominant Pairs & Bi-Directional Suffixes | All problems query **substring occurrences, LCPs, or repeats**. Discriminates: (1) Trie-BFS GSAM & Persistent SAM (`Ch 09`) vs. (2) $[l+L-1, r]$-clipped $\text{endpos}$ Segment Tree Merge (`Ch 10`) vs. (3) LCT `access` color-chain sweeps & intra-state length stratification (`Ch 11`) vs. (4) `SA-IS` $\text{rk}$-descents (`Ch 12`) vs. (5) Virtual Suffix Trees vs. $2N\log_2 N$ Dominant Pairs (`Ch 13`) vs. (6) online front-prepend `SCDAWG` / Suffix Balanced Trees (`Ch 14`). | **Winner: Proposal A (6 chapters)**. Separates Virtual Suffix Tree subset queries from range Dominant Pairs and front-prepend Suffix BSTs. |
| **`CP-IV`** (`Part IV`: `Ch 15`–`Ch 17`, 3–4 ch) | Internal Pattern Matching (IPM) & Advanced Palindromic Engines | All problems query **substring intervals $S[l..r]$ for internal borders, occurrences, or palindromes**. Discriminates: (1) Bounded-Ratio IPM AP intersection & 6-method borders (`Ch 15`) vs. (2) Tree/Rollback PAM & 4-Way Deque PAM surface push-down (`Ch 16`) vs. (3) $O(1)$ two-boundary unclipped Range LPS vs. `[徐毅 2014]` `slink`-telescoping Range Distinct Palindromes vs. Rich Words (`Ch 17`). | **Winner: Proposal A + B's `Ch 16/17` split**. Keeping SLPs out of Part IV prevents grammar-compression problems from giving themselves away via $N \le 10^{18}$ cut/paste constraints. |
| **`CP-V`** (`Part V`: `Ch 18`–`Ch 21`, 4 ch) | FFT Matching, $k$-Mismatch, Structural Isomorphism & Compressed Indexing (SLPs) | All problems test **non-exact, generalized, or grammar-compressed pattern matching**. Discriminates: (1) 1-NTT indicator wildcards vs. `CF 1334G` involution KMP vs. general $\pi$ FFT (`Ch 18`) vs. (2) Kangaroo LCE jumps vs. $2k$-period second-order differences (`Ch 19`) vs. (3) window-clipped `p-KMP`/`Order-KMP`/`Cartesian-KMP` & $1/z$ weighted strings (`Ch 20`) vs. (4) Jeż Recompression SLPs, Attractors $\gamma(S)$ & LZ77 2D indexing (`Ch 21`). | **Winner: Proposal A (4 chapters)**. Tests whether a non-standard matching relation compiles to 1D KMP clipping, FFT convolution, $2k$-period dichotomy, or SLP seam compression. |
| **`CP-VI`** (`Part VI`: `Ch 22`–`Ch 25`, 4 ch) | Subsequence Matrices, Seaweed Braids, Cluster GFs, Martingales & `DP套DP` | All problems involve **subsequence/LCS optimization or string enumeration/probability**. Discriminates: (1) DASG product BFS, Arch Factorization & $O(|\Sigma|)$ invertible subsequence matrices (`Ch 22`) vs. (2) tropical/gap-2 non-invertible DP vs. Tiskin's Seaweed Unit-Monge $\boxdot$ & Allison–Dix bit-parallel LCS (`Ch 23`) vs. (3) Goulden–Jackson $(t-1)$ vs. $t=1+u$ moment shift (`Ch 24`) vs. (4) Conway Martingale pattern races & `DP套DP` (`Ch 25`). | **Winner: Reordered Proposal A (4 chapters)**. Proposal C's Part VI mixes Goulden–Jackson GFs with Wheeler Graphs and Tree SA (`Ch 26`), which have zero symptom overlap. |
| **`CP-VII`** (`Part VII`: `Ch 26`–`Ch 30`, 5 ch) | Word Equations, Inverse Strings, Wheeler/RLBWT, Tree/Stack-Trie & Morphic Words | All problems impose **global structural constraints, graph/tree topologies, cancellation rules, or infinite morphic words**. Discriminates: (1) Signed Parallel DSU & $10^{18}$ period folding (`Ch 26`) vs. (2) Inverse KMP/Z/Manacher chordal counting & SA Adjacency (`Ch 27`) vs. (3) AC-DFA BEST & $O(1)$ RLBWT Move Structures (`Ch 28`) vs. (4) Centroid Dual-SAM on Trees vs. Stack-Trie Path LCE / $SL_2(\mathbb{F}_p)$ (`Ch 29`) vs. (5) Rytter's Singular Words & Morphic 3-Regime KMP (`Ch 30`). | **Winner: Proposal A (5 chapters)**. Cleanly groups constraint-satisfaction, graph/tree/stack reduction, and morphic word theory. |

---

## 3. Audit Axis III: Naming, Slug & Quarto Sidebar Ergonomics (`_quarto.yml` Alignment)

Inspecting `_quarto.yml` (`lines 46–165`) reveals strict repository conventions across `fps/` and `flows/`:
1. **Chapter Slugs**: Proposals B (`01-period-border...`) and C (no slugs for chapters, `cp-1.qmd` for checkpoints) deviate from the repository's `chXX-` and `cpXX-partX-` schema. **Proposal A's `ch01-...` to `ch30-...` convention is mandatory** to match `fps/chapters/ch01-...qmd` and `flows/chapters/ch01-...qmd`.
2. **Checkpoint & Capstone Slugs**: Must follow `strings/checkpoints/cp01-part1-...qmd` through `cp07-part7-...qmd`, plus `strings/capstones/synthesis-reserve.qmd` and `strings/capstones/problem-archive-guide.qmd`.
3. **Sidebar Section Width (`270px`)**: Quarto sidebar `section:` headers must use Roman numerals + middle dot (`I · ...` through `VII · ...`) and stay under ~42 characters so they do not wrap into 3 lines in the `270px` docked sidebar.

### Recommended Canonical 7-Part, 30-Chapter Slug & Sidebar Table (`id: strings`)

| Part Header (`_quarto.yml` `section:`) | Chapter / Checkpoint Path (`strings/...`) | Crisp Chapter / Checkpoint Title | Technique IDs |
| :--- | :--- | :--- | :--- |
| **Start here** | `strings/index.qmd`, `notation.qmd`, `study-plan.qmd` | Portal, Notation & Diagnostic Study Plan | 32-Symptom Atlas |
| **I · Periodicity, Borders & `slink` DP** | `chapters/ch01-fine-wilf-periodicity-orbits.qmd` | Ch 01: Period–Border Duality, Fine–Wilf & Orbit Counting | `T-1A-01` |
| | `chapters/ch02-weak-periodicity-border-aps.qmd` | Ch 02: Weak Periodicity, Border APs & Shortcut Links (`slink` / `anc`) | `T-1A-02` |
| | `chapters/ch03-border-modulo-shortest-path.qmd` | Ch 03: Border-Group Modulo Shortest Path & Residue Queues | `T-1A-03` |
| | `chapters/ch04-series-link-dp-kmp-pam.qmd` | Ch 04: Series-Link (`slink`) DP, Interleaving & Binomial Weights | `T-1A-04`, `T-1A-05` |
| | `checkpoints/cp01-part1-periodicity-borders-slink.qmd` | CP-I: Blind Checkpoint I — Periodicity, Border APs & `slink` DP | Part I Synthesis |
| **II · Lyndon Theory, `Cand` & Runs** | `chapters/ch05-lyndon-factorization-duval-necklaces.qmd` | Ch 05: CFL Factorization, Duval's Automaton, RLE Duval & Necklaces | `T-1B-01`, `T-1B-02` |
| | `chapters/ch06-significant-suffixes-substrings.qmd` | Ch 06: Significant Suffixes (`Cand`), 1-Survivor Merge & SA-RMQ | `T-1B-03` |
| | `chapters/ch07-lyndon-arrays-cartesian-trees.qmd` | Ch 07: Lyndon Arrays ($\lambda_<, \lambda_>$) & Min-Cartesian Lyndon Trees | `T-1B-04` |
| | `chapters/ch08-runs-theorem-squares-sweep.qmd` | Ch 08: The Runs Theorem, Three-Squares Lemma & 2D Run Sweeps | `T-1B-05`, `T-1B-06` |
| | `checkpoints/cp02-part2-lyndon-candidates-runs.qmd` | CP-II: Blind Checkpoint II — Lyndon Theory, `Cand` & Periodic Runs | Part II Synthesis |
| **III · Suffix Structures & Dominant Pairs** | `chapters/ch09-sam-duality-gsam-persistent.qmd` | Ch 09: SAM $\leftrightarrow \text{ST}(S^R)$ Duality, Trie-BFS GSAM & Persistent SAM | `T-2A-01`, `T-2A-02` |
| | `chapters/ch10-sam-endpos-segtree-merge.qmd` | Ch 10: SAM Persistent Segment Tree Merging & Substring Clipping | `T-2A-03` |
| | `chapters/ch11-dynamic-sam-lct-stratification.qmd` | Ch 11: Dynamic SAM + LCT Color Sweeps & Length Stratification | `T-2A-04`, `T-2A-05` |
| | `chapters/ch12-sais-induced-sorting-lcp.qmd` | Ch 12: Induced Sorting (`SA-IS`), Fischer LCP & $\text{rk}$-Descents | `T-2B-01`, `T-2B-02` |
| | `chapters/ch13-virtual-suffix-trees-dominant-pairs.qmd` | Ch 13: Zero-Tree Virtual Suffix Trees & DSU-on-Tree Dominant Pairs | `T-2B-02`, `T-2B-03` |
| | `chapters/ch14-cdawg-scdawg-suffix-balanced-trees.qmd` | Ch 14: `CDAWG`, Bi-Directional `SCDAWG` & Suffix Balanced Trees | `T-2A-02`, `T-2B-05`, `T-2B-06` |
| | `checkpoints/cp03-part3-suffix-structures-dominant-pairs.qmd` | CP-III: Blind Checkpoint III — Suffix Structures, LCT & Dominant Pairs | Part III Synthesis |
| **IV · Internal Matching & Palindromes** | `chapters/ch15-internal-pattern-matching-borders.qmd` | Ch 15: Basic Substring Dictionary, Bounded-Ratio IPM & 6-Method Borders | `T-2B-04` |
| | `chapters/ch16-deterministic-tree-deque-pam.qmd` | Ch 16: Deterministic/Tree PAM (`quick_link`) & 4-Way Deque PAM | `T-3A-01`, `T-3A-02` |
| | `chapters/ch17-range-palindromes-rich-words.qmd` | Ch 17: $O(1)$ Range LPS, `slink` Telescoping, Rich Words & Factorizations | `T-3A-03`–`T-3A-05` |
| | `checkpoints/cp04-part4-ipm-deque-range-palindromes.qmd` | CP-IV: Blind Checkpoint IV — Internal Matching & Advanced Palindromes | Part IV Synthesis |
| **V · FFT, Isomorphism & Grammar SLPs** | `chapters/ch18-fft-wildcard-involution-matching.qmd` | Ch 18: 1-NTT Wildcards, Kalai Projection, 3-in-2 FFT & Involutions | `T-3B-01`, `T-3B-02` |
| | `chapters/ch19-kmismatch-wavefront-period-dichotomy.qmd` | Ch 19: $k$-Mismatch Kangaroo Jumps, Wavefronts & $2k$-Period Dichotomy | `T-3B-03` |
| | `chapters/ch20-structural-isomorphism-weighted-strings.qmd` | Ch 20: Window-Clipped `p-KMP`, `Order`/`Cartesian-KMP` & $1/z$ Strings | `T-3B-04`, `T-5B-06` |
| | `chapters/ch21-locally-consistent-parsing-slp-attractors.qmd` | Ch 21: Locally Consistent Parsing, SLPs, Attractors & LZ77 Indexing | `T-3B-05`, `T-5B-05`, `T-5B-08` |
| | `checkpoints/cp05-part5-fft-isomorphism-slp-indexing.qmd` | CP-V: Blind Checkpoint V — FFT, $k$-Mismatch, Isomorphism & SLPs | Part V Synthesis |
| **VI · Subsequences, Seaweed & String GFs** | `chapters/ch22-dasg-arch-simon-invertible-matrices.qmd` | Ch 22: `DASG`, Arch Factorization, Simon's $\sim_k$ & Invertible Matrices | `T-4B-01`–`T-4B-03` |
| | `chapters/ch23-bit-parallel-lcs-seaweed-matrices.qmd` | Ch 23: Bit-Parallel LCS, Tiskin's Seaweed Matrices & $\boxdot$ Range LIS | `T-4B-05`, `T-4B-04` |
| | `chapters/ch24-goulden-jackson-moment-shift-fps.qmd` | Ch 24: Goulden–Jackson Clusters, $(t-1)$ FPS & $t=1+u$ Moment Shift | `T-4A-01`–`T-4A-03` |
| | `chapters/ch25-martingale-pgfs-automaton-dp-of-dp.qmd` | Ch 25: Conway Martingale PGFs, Pattern Races, `DP套DP` & Dynamic AC | `T-4A-04`, `T-4A-05` |
| | `checkpoints/cp06-part6-subsequences-seaweed-string-gfs.qmd` | CP-VI: Blind Checkpoint VI — Subsequences, Seaweed, Cluster GFs & `DP套DP` | Part VI Synthesis |
| **VII · Equations, Trees, Groups & Words** | `chapters/ch26-word-equations-signed-parallel-dsu.qmd` | Ch 26: Word Equations, Signed Parallel DSU & $10^{18}$ Period Folding | `T-5A-01`, `T-5A-02` |
| | `chapters/ch27-inverse-reconstruction-inequality-dags.qmd` | Ch 27: Inverse String Reconstruction (`KMP`/`Z`/`SA`) & Inequality DAGs | `T-3A-06`, `T-5A-03` |
| | `chapters/ch28-debruijn-best-bwt-wheeler-rlbwt.qmd` | Ch 28: De Bruijn BEST, BWT/`BBWT`, Wheeler Graphs & $O(1)$ RLBWT Move | `T-5A-04`, `T-5A-05`, `T-1B-02` |
| | `chapters/ch29-tree-strings-stack-trie-sl2-hashing.qmd` | Ch 29: Strings on Trees, Tree DSU, Stack-Trie LCE & $SL_2(\mathbb{F}_p)$ Hashing | `T-5A-06`, `T-5A-02`, `T-5B-04` |
| | `chapters/ch30-sturmian-singular-thue-morse-morphic-2d.qmd` | Ch 30: Sturmian Singular Words, Thue–Morse, Morphisms $\varphi^k$ & 2D Grids | `T-5B-01`–`03`, `T-5B-07` |
| | `checkpoints/cp07-part7-equations-trees-groups-morphic.qmd` | CP-VII: Blind Checkpoint VII — Equations, Wheeler, Trees, $SL_2$ & Words | Part VII Synthesis |
| **Capstones & Reference** | `capstones/synthesis-reserve.qmd`, `problem-archive-guide.qmd`, `sources.qmd` | Grandmaster Multi-Part Synthesis Reserves (`Syn-01..Syn-30`) & Sources | Cross-Part Mastery |

---

## 4. Concrete Blind Checkpoint Decoy Pairings & Diagnostic Discrimination Protocol (`CP-I`–`CP-VII`)

To ensure each Part-End Blind Checkpoint (`CP-I` through `CP-VII`) tests non-trivial diagnostic discrimination rather than chapter-order memorization, every checkpoint should include at least two **Diagnostic Decoy Pairs**—problems with nearly identical surface statements that route to different chapters within the same Part based on a subtle constraint or algebraic property:

1. **`CP-I` Decoy Pair (`Ch 02` vs. `Ch 04`)**:
   - *Surface Symptom*: Maintain an online string $S[1..r]$ and aggregate values over all active borders/palindromic suffixes ending at $r$.
   - *Diagnostic Fork*: If each step deletes invalid borders and updates global weights on remaining borders (`CF 1286E`), route to **`Ch 02` (`slink` active-border deletion)**. If each step transitions $dp[r] = \bigoplus dp[r - L]$ from fixed historical left endpoints $i = r - L$, route to **`Ch 04` (`g[u]` shift-overlap `slink` DP)**.
2. **`CP-II` Decoy Pair (`Ch 05` vs. `Ch 06`)**:
   - *Surface Symptom*: Find the lexicographically smallest suffix or cyclic shift of a prefix/substring.
   - *Diagnostic Fork*: For all prefixes $S[1..r]$ with no right-extension ($T = \varepsilon$), route to **`Ch 05` ($O(N)$ Duval all-prefix state sharing $r \to r - dp$)**. For arbitrary substrings $S[l..r]$ or concatenation with a suffix $T \ne \varepsilon$ (`[ZJOI2017]`, `[JSOI2019]`), Duval's greedy commitment fails (`Counterexample: S = "aaba"` on $[2, 4]$); route to **`Ch 06` (Significant Suffixes $|\text{Cand}| \le \lfloor \log_2 N \rfloor + 1$)**.
3. **`CP-III` Decoy Pair (`Ch 10` vs. `Ch 13` vs. `Ch 14`)**:
   - *Surface Symptom*: Answer substring LCP or repeat queries over $S[l..r]$ or online string extensions.
   - *Diagnostic Fork*: Substring occurrence/containment of an external pattern $T$ inside $S[l..r]$ routes to **`Ch 10` (SAM $\text{endpos}$ Segment Tree Merge clipped to $[l+L-1, r]$)**; internal pairwise LCP optimization $\max_{l \le a < b \le r} f(\text{LCP}(a, b), a, b)$ routes to **`Ch 13` ($2N\log_2 N$ DSU-on-Tree Dominant Pairs)**; online encrypted front-prepends `push_front(c)` route to **`Ch 14` (Hash-Free Suffix Balanced Tree with 64-bit Scapegoat tags)**.
4. **`CP-IV` Decoy Pair (`Ch 15` vs. `Ch 17`)**:
   - *Surface Symptom*: Query the longest border vs. longest palindrome inside $S[l..r]$.
   - *Diagnostic Fork*: Substring borders are **not** hereditary on centers and require **`Ch 15` (Dyadic Bounded-Ratio IPM AP intersection of $P_m$ and $Q_m$)**, whereas substring palindromes preserve midpoint centers and admit **`Ch 17` ($O(1)$ two-boundary unclipping `c_L = rightmost_reach[2l-1]`, `c_R = leftmost_reach[2r-1]`)**.
5. **`CP-V` Decoy Pair (`Ch 18` vs. `Ch 19` vs. `Ch 20`)**:
   - *Surface Symptom*: Generalized pattern matching under character transformations or mismatches.
   - *Diagnostic Fork*: Involution $\pi^2 = \text{id}$ in `CF 1334G` collapses to **`Ch 18` ($O(N+M)$ canonical KMP)** whereas general $\pi$ requires **quartic/Kalai FFT**; bijective character renaming (`p-KMP`) or Cartesian-tree shape matching preserves prefix monotonicity after window clipping $\text{clip}(\text{prev}[x], q)$ and routes to **`Ch 20` ($O(N+M)$ structural KMP)**; bounded Hamming distance $\le k$ routes to **`Ch 19` ($2k$-period dichotomy)**.
6. **`CP-VI` Decoy Pair (`Ch 22` vs. `Ch 23`)**:
   - *Surface Symptom*: Range queries $(l, r)$ on subsequence DP or alignment over $S[l..r]$.
   - *Diagnostic Fork*: Algebraic ring counting of distinct/fixed-pattern subsequences has $\det M_c = 1$ and routes to **`Ch 22` ($O(|\Sigma|)$ matrix-free dot product $\mathbf{u}_r^T \cdot \mathbf{v}_{l-1}$)**; gap $\ge 2$ (`det = 0`) or tropical $(\min, +)$ DP (`CF 750E`) lacks matrix inverses and requires Segment Trees; all-pairs semi-local $\text{LCS}(A, B[l..r])$ routes to **`Ch 23` (Tiskin's Seaweed permutation $W[k] < l$)**.
7. **`CP-VII` Decoy Pair (`Ch 26` vs. `Ch 29`)**:
   - *Surface Symptom*: Substring/path equivalence queries under reversals or adjacent cancellations.
   - *Diagnostic Fork*: Static bulk equations $S[l_1..r_1] = S[l_2..r_2]^R$ route to **`Ch 26` (Signed Binary-Lifting DSU with `is_pal[k][r]`)**; free-group/stack cancellation `cc -> empty` or Dyck reduction routes to **`Ch 29` (Deterministic Stack-Trie LCA/LCE or Height-Indexed $SL_2(\mathbb{F}_p)$ Segment Tree)**.

---

## 5. Executive Synthesis Checklist for Phase 1.5 Master Curriculum Reconciliation

- [x] **Base Architecture**: Adopt **Proposal A's 7-Part, 30-Chapter spine** (`Ch 01`–`Ch 04`, `Ch 05`–`Ch 08`, `Ch 09`–`Ch 14`, `Ch 15`–`Ch 17`, `Ch 18`–`Ch 21`, `Ch 22`–`Ch 25`, `Ch 26`–`Ch 30`), which achieves the best Part-level diagnostic cohesion and avoids the `Ch 12`/`Ch 13` suffix-structure pileups of Proposals B and C.
- [x] **Refinement 1 (Part IV `Ch 16`–`Ch 17` Split from Proposal B)**: Move Rich Words, Even-Palindrome Greedy & $\theta$-Palindromes (`T-3A-05`) from `Ch 16` to `Ch 17` so `Ch 16` is 100% dedicated to Unamortized/Tree PAM & 4-Way Deque PAM pointer mechanics (`T-3A-01`, `T-3A-02`).
- [x] **Refinement 2 (Part VI `Ch 22`–`Ch 25` Internal Ordering from Proposals B & C)**: Place Subsequence Automata & Invertible Matrices (`Ch 22`) and Bit-Parallel LCS & Seaweed Matrices (`Ch 23`) *before* Goulden–Jackson (`Ch 24`) and Martingale PGFs + `DP套DP` (`Ch 25`), eliminating the forward reference from LCS `DP套DP` (`T-4A-05`) to the 4-instruction Allison–Dix bit-parallel transition (`T-4B-05`).
- [x] **Refinement 3 (`_quarto.yml` Naming & Slug Standardization)**: Enforce `ch01-...` to `ch30-...` for chapters, `cp01-part1-...` to `cp07-part7-...` for Blind Checkpoints, `capstones/synthesis-reserve.qmd` + `capstones/problem-archive-guide.qmd` for Capstones, and Roman-numeral middle-dot (`I · ...` to `VII · ...`) sidebar headers under 42 characters.
