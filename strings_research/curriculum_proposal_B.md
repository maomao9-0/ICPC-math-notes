# Post-Research Curriculum Proposal B: Combinatorial Invariant Progression & Cognitive Load Balance (`strings_research/curriculum_proposal_B.md`)

> [!IMPORTANT]
> **Curriculum Architect Subagent B — Phase 1.5 Independent Redesign**
> - **Design Lens**: **Combinatorial Invariant Progression & Cognitive Load Balance**
> - **Core Mandate**: Dissolve the 10 Phase 1 research waves and regional (`[EN]` / `[ZH]` / `[JA]`) buckets into a **Zero-Forward-Reference 7-Part, 30-Chapter Textbook Architecture** (plus 7 Part-End Blind Checkpoints `CP-I`–`CP-VII` and 1 Grandmaster Synthesis Capstone) that maps all **57 discovered technique families (`T-1A-01` through `T-5B-08`)** so that no single chapter is overloaded with incompatible data structures or competing algebraic paradigms.

---

## 1. Design Philosophy & Cognitive-Load Critique of the 24-Chapter Pre-Research Seed

An expert programmer learning advanced stringology from first principles does not struggle with standard templates (`SA`, `SAM`, `PAM`, `KMP`, `Z`, `AC`); they struggle when a chapter conflates **multiple independent combinatorial invariants** with **multiple heavy data structures**. Auditing the provisional 6-Part, 24-Chapter seed in `PLAN.md` §4 against the 115-iteration Phase 1 discovery corpus (`TECHNIQUE_TAXONOMY.md`, 57 technique families, 430+ curated problems) exposes **six severe cognitive-load and prerequisite-ordering bottlenecks**:

1. **The `Ch 12` Five-Paradigm Pileup (Suffix Structures Overload)**:
   - The 24-chapter seed packed Induced Sorting (`SA-IS`, `T-2B-01`), Virtual Suffix Trees (`T-2B-02`), Suffix Tree Dominant Pairs (`启发式合并支配对`, `T-2B-03`), Bi-Directional `SCDAWG` (`T-2B-05`), and Hash-Free Suffix Balanced Trees (`后缀平衡树`, `T-2B-06`) into a single chapter (`Ch 12`), while leaving `CDAWG` & Unamortized Persistent SAM (`T-2A-02`) homeless.
   - **Fix**: Split `Ch 12` into `Ch 12` (*Static Suffix-Tree Compression: `SA-IS`, Virtual Suffix Trees & DSU-on-Tree Dominant Pairs*, `T-2B-01..03`) and `Ch 13` (*Beyond Right-Appends: `CDAWG`, Unamortized Persistent SAM, Bi-Directional `SCDAWG` & Hash-Free Suffix Balanced Trees*, `T-2A-02, T-2B-05, T-2B-06`).
2. **Frontier Dictionary Compression & Grammar Indexing (`T-3B-05`, `T-5B-05`, `T-5B-08`) Misplacement**:
   - The 24-chapter seed buried Locally Consistent Parsing (`SLP`, `T-3B-05`) inside `Ch 23` alongside Non-Abelian $SL_2(\mathbb{F}_p)$ Stack Hashing (`T-5B-04`), and had no dedicated home for Kempa–Prezza String Attractors $\gamma(S)$, $\tau$-Synchronizing Sets (`T-5B-05`), or Kärkkäinen–Ukkonen LZ77/SLP 2D Orthogonal Range Indexing (`T-5B-08`).
   - **Fix**: Move Locally Consistent Parsing, Jeż's Recompression, String Attractors, $\tau$-Synchronizing Sets, and LZ77/SLP 2D Primary–Secondary Indexing into Part IV (`Ch 15`), immediately after Kociumaka's Basic Substring Dictionary & Bounded-Ratio IPM (`Ch 14`, `T-2B-04`). Both chapters answer the exact same structural question: *how to index, compare, and match internal substrings across static, grammar-compressed, or dynamic texts*.
3. **Palindromic Automaton Mechanics vs. Range Queries vs. Inverse Reconstruction (`T-3A-01..06`)**:
   - In the 24-chapter seed, `Ch 16` mixed 2D range data structures ($O(1)$ Range LPS `T-3A-03` and `[徐毅 2014]` `slink` periodic telescoping `T-3A-04`) with Rich Words (`T-3A-05`) and Inverse String Reconstruction from $\pi/Z/\text{rad}$ (`T-3A-06`).
   - **Fix**: Dedicate `Ch 16` to **Worst-Case & Bi-Directional Automaton Topology** (`quick_link` / `slink`-skip, Tree PAM, and 4-Way Deque PAM lazy surface push-down, `T-3A-01, T-3A-02`), `Ch 17` to **Range Palindrome Queries & Palindromic Factorization Combinatorics** (`T-3A-03..05`), and relocate **Inverse String Reconstruction (`T-3A-06`)** to `Ch 26` alongside String Inequality Digraphs & Suffix Array Adjacency Reconstruction (`T-5A-03`), where both share the **Equality + Forbidden-Edge / Chromatic DAG Invariant**.
4. **The `Ch 17` Algebraic / Approximate / Structural Matching Bottleneck (`T-3B-01..04`, `T-5B-06`, `T-5B-07`)**:
   - Stuffing 1-NTT indicator wildcards, Kalai's projection, 3-in-2 FFT, quartic involution matching, $k$-mismatch kangaroo jumps, Clifford–Gawrychowski–Uznański $2k$-period second-order differences, window-clipped `p-KMP` / `Order-KMP` / `Cartesian-KMP`, $1/z$ Weighted Suffix Trees, and 2D Baker–Bird / Vishkin Duel into one chapter (`Ch 17` in the seed) creates an impossible 6-technique wall.
   - **Fix**: Expand into a dedicated 3-chapter Part V (`Ch 18`–`Ch 20`), separating **Exact Algebraic Convolutions** (`Ch 18`), **Approximate $k$-Mismatch / $k$-Edit & the $2k$-Period Dichotomy** (`Ch 19`), and **Structural Isomorphisms, $1/z$ Weighted Strings & 2D Periodicity Lattices** (`Ch 20`).
5. **The Hidden Forward Reference Between Bit-Parallel LCS (`T-4B-05`) and `DP套DP` (`T-4A-05`)**:
   - In the 24-chapter seed, `Ch 19` taught LCS `DP套DP` (`T-4A-05`) *before* `Ch 20` introduced the Allison–Dix horizontal difference encoding $\Delta_i = dp[i] - dp[i-1] \in \{0, 1\}$ and 4-instruction bitwise borrow transition (`T-4B-05`)!
   - **Fix**: Pair `T-4B-05` (Allison–Dix Bit-Parallel LCS, Myers' Bit-Parallel Edit Distance & Hirschberg Bitset Reconstruction) and `T-4A-05` (the 4-stage `DP套DP` State-Compression Compiler & Binary-Grouped Dynamic AC) in `Ch 22` around their shared invariant: **Encoding Monotonic DP Row Differences as Bounded Bitmask / Strip Automata**. This frees `Ch 23` for **Subsequence Automata (`DASG`), Arch Factorization, Simon's Congruence & Invertible Subsequence Matrices** (`T-4B-01..03`) and `Ch 24` exclusively for **Tiskin's Seaweed Matrices, $O(K\log K)$ Unit-Monge $\boxdot$ Multiplication & $O(N\log^2 N)$ Range LIS** (`T-4B-04`).
6. **Unpacking the Part VI Catch-All (`Ch 21`–`Ch 24` $\to$ Part VII `Ch 25`–`Ch 30`)**:
   - The 24-chapter seed compressed Word Equations (`T-5A-01, T-5A-02`), String Inequalities (`T-5A-03`), De Bruijn / BEST (`T-5A-04`), and BWT / Wheeler / RLBWT (`T-5A-05`) into a single chapter (`Ch 21`).
   - **Fix**: Restructure Part VII into **six focused chapters (`Ch 25`–`Ch 30`)**: (1) Signed & Tree Binary-Lifting DSU + $N \le 10^{18}$ Period Folding (`Ch 25`), (2) String Inequality Digraphs, SA Adjacency & Inverse Reconstruction (`Ch 26`), (3) De Bruijn, AC-DFA BEST, BWT/BBWT, Wheeler Graphs & $O(1)$ RLBWT Move Structures (`Ch 27`), (4) Strings on Trees (`Ch 28`), (5) Non-Abelian $GL_2/SL_2(\mathbb{F}_p)$ Stack Hashing & Stack-Trie Path Isomorphism (`Ch 29`), and (6) Sturmian & Rytter's Singular Words, Thue–Morse Anti-Hash & Iterated Morphisms $\varphi^k(S_0)$ (`Ch 30`).

---

## 2. Master Architecture Overview & Cognitive-Load Balance Table

| Part | Title & Pedagogical Arc | Chapters | Checkpoints | Technique IDs Covered | Avg. IDs / Ch |
| :--- | :--- | :---: | :---: | :--- | :---: |
| **Part I** | Structural Periodicity, Border Algebra & Series-Link (`slink`) DP | `Ch 01`–`Ch 04` (4) | `CP-I` | `T-1A-01` – `T-1A-05` (5 IDs) | $1.25$ |
| **Part II** | Lyndon Theory, Significant Suffixes & The Runs Theorem | `Ch 05`–`Ch 08` (4) | `CP-II` | `T-1B-01` – `T-1B-06` (6 IDs) | $1.50$ |
| **Part III** | Suffix Automata, Suffix Trees, Endpos Merging & Dynamic Suffix Structures | `Ch 09`–`Ch 13` (5) | `CP-III` | `T-2A-01` – `T-2A-05`, `T-2B-01` – `T-2B-03`, `T-2B-05`, `T-2B-06` (10 IDs) | $2.00$ |
| **Part IV** | Internal Pattern Matching (IPM), Grammar Compression & Palindromic Theory | `Ch 14`–`Ch 17` (4) | `CP-IV` | `T-2B-04`, `T-3B-05`, `T-5B-05`, `T-5B-08`, `T-3A-01` – `T-3A-05` (9 IDs) | $2.25$ |
| **Part V** | Algebraic Convolution Matching, $k$-Mismatch & Structural Isomorphisms | `Ch 18`–`Ch 20` (3) | `CP-V` | `T-3B-01` – `T-3B-04`, `T-5B-06`, `T-5B-07` (6 IDs) | $2.00$ |
| **Part VI** | Autocorrelation Generating Functions, `DP套DP`, Subsequence & Seaweed Matrices | `Ch 21`–`Ch 24` (4) | `CP-VI` | `T-4A-01` – `T-4A-05`, `T-4B-01` – `T-4B-05` (10 IDs) | $2.50$ |
| **Part VII** | Word Equations, Wheeler/Tree Strings, Stack Groups & Combinatorics on Words | `Ch 25`–`Ch 30` (6) | `CP-VII` + `Capstone` | `T-5A-01` – `T-5A-06`, `T-3A-06`, `T-5B-01` – `T-5B-04` (11 IDs) | $1.83$ |
| **Total** | **Zero-Forward-Reference Complete Curriculum** | **30 Chapters** | **7 CPs + 1 Capstone** | **All 57 Technique Families (`T-1A-01..T-5B-08`)** | **$1.90$** |

---

## 3. Complete Chapter-by-Chapter Specification (`Ch 01`–`Ch 30`)

### Portal & Reference Pages (`strings/`)
- `strings/index.qmd`: Textbook scope, assumed prerequisite boundary (`Hash`, `KMP`, `Z`, `Trie`, `AC`, `Manacher`, `SA`, `SAM`, `PAM`), the 4-Step *"Zero Magic Invariants"* standard, and the 32-symptom Global Diagnostic Routing Atlas (`TECHNIQUE_TAXONOMY.md` §11).
- `strings/study-plan.qmd`: Multi-track study roadmaps (Track A: Combinatorics on Words & Periodicity; Track B: Suffix/Palindrome Data Structures & IPM; Track C: Algebraic, Matrix & Generating-Function String Engines) and Blind Checkpoint rules.
- `strings/notation.qmd`: Standardized stringology notation ($\text{Border}(S)$, $\text{Per}(S)$, $\text{diff}/`slink`$, $\text{Cand}(U)$, $\mathcal{R}(S)$, $\text{endpos}_S(u)$, $\boxdot$, $\gamma(S)$).
- `strings/sources.qmd`: Full multilingual bibliography and `[EN]` $\leftrightarrow$ `[ZH]` $\leftrightarrow$ `[JA]` Stringology Rosetta Stone (`CITATIONS.md`).

### Part I: Structural Periodicity, Border Algebra & Series-Link (`slink`) DP (`Ch 01`–`Ch 04` + `CP-I`)

#### `Ch 01` — `01-period-border-duality-fine-wilf.qmd`
- **Title**: Period–Border Duality, the Fine–Wilf Theorem, and Sub-Threshold Orbit Counting
- **Core Invariant Taught**: Exact bijection $b \in \text{Border}(S) \iff p = |S|-b \in \text{Per}(S)$; Fine–Wilf periodicity collapse $\gcd(p, q) \in \text{Per}(S)$ at threshold $N \ge p + q - \gcd(p, q)$ proved via directed Hamiltonian paths on $\mathbb{Z}/(p+q)\mathbb{Z}$ and first-return maps $\psi(x) = ((x+p-1)\bmod q)+1$; exact sub-threshold orbit formula $C(N; p, q) = p + q - N$ when $\max(p, q) \le N < p + q - \gcd(p, q)$ (yielding $|\Sigma|^{p+q-N}$ valid strings); and the Castelli–Mignosi–Restivo 3-period extension.
- **Assigned Technique IDs**: `T-1A-01` | **Prerequisites**: None (Assumes KMP $\pi$ and Z-array baseline).
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: `[BOI 2009] Radio Transmission` (`W1A-01`), `CF 535D — Tavas and Malekas` (`W1A-02`) $\to$ *Intermediate*: `[POI 2012] OKR-A Horrible Poem` (`W1A-11`), `CF 126B` variants $\to$ *Advanced*: `UCup / QOJ` Sub-Threshold Dual-Period Orbit Counting $|\Sigma|^{p+q-N}$ (`W1A-15`) $\to$ *Mastery*: `AtCoder AGC 032 F — One Third` (`W1A-24`).

#### `Ch 02` — `02-weak-periodicity-border-aps.qmd`
- **Title**: The Weak Periodicity Lemma, $O(\log N)$ Border Arithmetic Progressions, and Shortcut Link Duality (`slink` vs. `anc`)
- **Core Invariant Taught**: Half-Length Single-AP Theorem (all borders of $S[1..u]$ of length $\ge \lceil u/2 \rceil$ share minimum period $d = u - \pi[u]$); exact $\frac{2}{3}$ and $\frac{1}{2}$ border length-drop inequalities ($\pi[\pi[u]] < u/2$) when period steps change, partitioning $\text{Border}(S[1..u])$ into $\le \lceil \log_2 u \rceil$ half-open APs $(\text{slink}[u], u]$; and the Next-Character Equality Theorem proving that constant $\text{diff}$ forces $S[\pi[\pi[u]]+1] = S[\pi[u]+1]$ so `anc[u]` coarsens `slink[u]`.
- **Assigned Technique IDs**: `T-1A-02` | **Prerequisites**: `Ch 01`
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: `CF 1721E — Prefix Function Queries` (`W1A-06`) $\to$ *Intermediate*: `CF 1286E — Fedya the Potter Strikes Back` (`W1A-18`, monotone border weight maintenance via `slink`) $\to$ *Advanced*: `[SDOI2019] 连续子序列` (`W1A-28`), `CF 1764G` / Inverse Border AP Realizability (`W1A-22`) $\to$ *Mastery*: Worst-case Sturmian border-tree depth & online border-set sum queries.

#### `Ch 03` — `03-border-modulo-shortest-path.qmd`
- **Title**: Border-Group Modulo Shortest Path (`同余最短路`) and Dynamic Modulus Residue-Cycle Queues
- **Core Invariant Taught**: Partitioning $\Theta(N)$ period transition weights $\{N - b : b \in \text{Border}(S)\}$ into $K \le \lceil \log_2 N \rceil$ arithmetic progressions $\mathcal{A}_k = \{x_k + j d_k \mid 0 \le j \le c_k\}$; dynamic modulus switching $m_{\text{old}} \to x_k$ via $\gcd(m_{\text{old}}, x_k)$-cycle relaxation starting at the cycle argmin $u_{\min}$; and unbounded-knapsack sliding-window monotonic queues of width $c_k$ on $\gcd(d_k, x_k)$ residue cycles (enforcing update-before-push for unbounded reuse).
- **Assigned Technique IDs**: `T-1A-03` | **Prerequisites**: `Ch 01`, `Ch 02`
- **Target Problem Ladder Scope** (6 problems): *Stepping Stone*: Base-Period Modulo Shortest Path $\to$ *Intermediate*: Unbounded AP Knapsack on Residue Cycles $\to$ *Advanced*: `[WC2016] 论战捆竹竿` (`W1A-33`, Luogu P4156 / UOJ #179) $\to$ *Mastery*: Bounded-Copy & Weighted Border-Group Modulo Shortest Path (`W1A-38`).

#### `Ch 04` — `04-slink-dp-pam-kmp.qmd`
- **Title**: Series-Link (`slink` / `diff`) DP Acceleration, Double-End Interleaving, and Binomial Moment Splitting
- **Core Invariant Taught**: The Shift-Overlap Invariant $\mathcal{I}(u, r) = \mathcal{I}(\text{fail}[u], r - d) \sqcup \{r - \text{len}[\text{slink}[u]] - d\}$ and why $g[\text{fail}[u]]$ is guaranteed up-to-date at $r - d$ without stale overwrites; double-end interleaving ($T = S[1]S[N]S[2]S[N-1]\dots$ for symmetric blocks `CF 932G`) and reversal interleaving ($T = A[1]B[1]A[2]B[2]\dots$ for `CF 906E`); and Binomial Left-Endpoint Invariance $i = r - L$ expanding $(r - i)^m = \sum \binom{m}{t}(-1)^t r^{m-t} i^t$ for polynomial-weighted (`w(L) = P(L)`), parity-filtered, and length-windowed `slink` DP.
- **Assigned Technique IDs**: `T-1A-04`, `T-1A-05` | **Prerequisites**: `Ch 02`
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: Minimum/Count Palindrome Partition DP in $O(N \log N)$ (`W1A-34`) $\to$ *Intermediate*: `[CERC 2014] Virus Synthesis` (`W1A-27`), `CF 932G — Palindrome Partition` (`W1A-25`) $\to$ *Advanced*: `CF 906E — Reverses` (`W1A-26`) $\to$ *Mastery*: Polynomial-Weighted & Length-Windowed Palindrome Partition DP (`W1A-39`, `W1A-40`).

#### `CP-I` — `checkpoints/cp-01-periodicity-borders-slink.qmd`
- **Blind Checkpoint I**: 6–8 unspoiled problems testing recognition between Fine–Wilf orbit counting, KMP `slink` active-set deletion, Border Modulo Shortest Path, and interleaved PAM `slink` DP.

---

### Part II: Lyndon Theory, Significant Suffixes & The Runs Theorem (`Ch 05`–`Ch 08` + `CP-II`)

#### `Ch 05` — `05-cfl-duval-lyndon-factorization.qmd`
- **Title**: Chen–Fox–Lyndon Factorization, Duval's Automaton, All-Prefix State Sharing, and Witt's Necklace Formula
- **Core Invariant Taught**: Four-way Lyndon equivalence ($w \in \mathcal{L} \iff \forall uv, w < v$); unique non-increasing CFL factorization $S = w_1 \dots w_k$ ($w_1 \ge \dots \ge w_k$); Duval's 3-pointer periodic invariant $S[i..r] = w^d w'$ with potential $\Phi = 2i + k < 2N$, all-prefix state sharing $r \to r - dp$ (`Theorem 2.4`), and $O(M)$ RLE block-boundary alignment; plus Witt's necklace identity and the Bijective BWT (`BBWT`) cycle-Lyndon bijection under $\omega$-order $X^\omega \le Y^\omega$.
- **Assigned Technique IDs**: `T-1B-01`, `T-1B-02` | **Prerequisites**: `Ch 01`
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: `CF 1537E2 — Erase and Extend` (`W1B-02`), `AtCoder ARC 050 D — Suffix Concat` (`W1B-05`) $\to$ *Intermediate*: `Luogu P6127` / All-Prefix CFL XOR & Minimum Suffix via $r \to r - dp$ (`W1B-15`), FKM De Bruijn Generation (`W1B-18`) $\to$ *Advanced*: $O(M)$ RLE Lyndon Factorization (`W1B-35`) $\to$ *Mastery*: Bijective BWT (`BBWT`) Forward & Inverse Multi-Cycle Reconstruction (`W1B-36`).

#### `Ch 06` — `06-significant-suffixes-theorem.qmd`
- **Title**: The Significant Suffixes (`显著后缀`) Theorem, 1-Survivor Segment Tree Merging, and Dyadic SA-RMQ
- **Core Invariant Taught**: Tandem-Annihilation & Doubling Theorem (`Theorem 3.1`: if $u \sqsubset v$ and $|u| < |v| < 2|u|$, then $u = w u', v = w^2 u'$ and $\min(u'T, vT) < uT < \max(u'T, vT)$ for every right-extension $T \in \Sigma^*$, forcing $|u_{i+1}| \ge 2|u_i|$ and $|\text{Cand}(U)| \le \lfloor \log_2 |U| \rfloor + 1$); the Segment Tree `pushup` 1-Survivor Theorem (at most 1 left-child candidate survives in $\text{Cand}([L, R])$); and Segment-Tree-Free Dyadic SA-Rank RMQ extraction in $O(\log(r-l+1))$ time.
- **Assigned Technique IDs**: `T-1B-03` | **Prerequisites**: `Ch 02`, `Ch 05`
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: Static Substring Minimum Suffix ($T = \varepsilon$ shortest-border reduction) $\to$ *Intermediate*: `[JSOI2019] 节日庆典` (`W1B-03`, online prefix minimum cyclic shift) $\to$ *Advanced*: `[ZJOI2017] 字符串` (`W1B-22`, Segment Tree 1-Survivor `pushup` + $\sqrt{N}$ block hash) $\to$ *Mastery*: Substring Minimum Cyclic Shift & Tree-Path Significant Suffixes via HLD (`W1B-25`, `W1B-37`).

#### `Ch 07` — `07-lyndon-arrays-lyndon-trees.qmd`
- **Title**: Lyndon Arrays ($\lambda_<, \lambda_>$), Double-Order Monotonic Stacks, and Min-Cartesian Lyndon Tree Isomorphism
- **Core Invariant Taught**: Next-Smaller-Suffix identity $R_{\mathcal{L}}[i] + 1 = \text{nsv}[i] = \min\{j > i : S[j..N] < S[i..N]\}$; canonical isomorphism between internal nodes of the Lyndon Tree of $\$S[1..N]$ and the Min-Cartesian Tree of $\text{rk}[2..N+1]$ (where Cartesian node $m$ with span $[L_m, R_m]$ represents Lyndon word $S[L_m-1..R_m]$); why negating $-\text{rk}_<$ fails on proper prefixes ($S = \texttt{bab}$ counterexample) and how character inversion $\overline{S}$ or $O(1)$ LCE builds $\lambda_>$; and worst-case $O(\log N)$ persistent/online Lyndon factorization via right-spine binary lifting.
- **Assigned Technique IDs**: `T-1B-04` | **Prerequisites**: `Ch 05`
- **Target Problem Ladder Scope** (7 problems): *Stepping Stone*: Double-Order Lyndon Array Construction $\lambda_<, \lambda_>$ (`W1B-12`) $\to$ *Intermediate*: `AtCoder AGC 023 F — 01 on Tree` / Lyndon Tree Greedy Merge (`W1B-19`) $\to$ *Advanced*: Longest Lyndon Substring in $S[l..r]$ (`W1B-28`) $\to$ *Mastery*: Persistent / Online Worst-Case $O(\log N)$ Lyndon Factorization on Version Trees (`W1B-39`).

#### `Ch 08` — `08-runs-theorem-three-squares.qmd`
- **Title**: The Runs Theorem (Bannai et al.), the Three-Squares Lemma, and 2D Sweep-Line over Periodic Runs
- **Core Invariant Taught**: Lyndon-Root Disjointness Proof of $|\mathcal{R}(S)| \le N - 1$ and $\sum \text{exp}(R) < 3N$ (choosing $<_R \in \{<, >\}$ so $S[r+1] <_R S[r+1-p]$ locks each run's interior Lyndon roots $B(R) \subseteq \{2..N\}$ into disjoint ascent/descent sets $S[i] <_R S[i-1]$); $O(N \log N)$ harmonic LCE checkpoint gluing vs. $O(N)$ Lyndon-array seeding; Crochemore–Rytter Three-Squares Lemma ($|w| \ge |u| + |v|$) and the $< 2N$ Representative / Distinct Squares Lemma; Fine–Wilf substring run-clipping non-collision and 2D $(L, R)$-plane sweep-lines.
- **Assigned Technique IDs**: `T-1B-05`, `T-1B-06` | **Prerequisites**: `Ch 01`, `Ch 07`
- **Target Problem Ladder Scope** (9 problems): *Stepping Stone*: `[NOI2016] 优秀的拆分` (`W1B-01`, $AABB$ counting) $\to$ *Intermediate*: Square-Free String Partitioning in $O(N)$ (`W1B-31`), Distinct Square Enumeration (`W1B-34`) $\to$ *Advanced*: Substring Run Counting $|\mathcal{R}(S[L_q..R_q])|$ via 2D Sweep-Line (`W1B-26`), Sum over Distinct Squares (`W1B-33`) $\to$ *Mastery*: Palindromic Runs & $k$-th Power Range Queries (`W1B-40`).

#### `CP-II` — `checkpoints/cp-02-lyndon-significant-suffixes-runs.qmd`
- **Blind Checkpoint II**: 6–8 unspoiled problems testing recognition across Duval state sharing, Significant Suffixes (`Cand`), Lyndon Tree Cartesian structure, and 2D Runs sweep-lines.

---

### Part III: Suffix Automata, Suffix Trees, Endpos Merging & Dynamic Suffix Structures (`Ch 09`–`Ch 13` + `CP-III`)

#### `Ch 09` — `09-sam-duality-generalized-sam.qmd`
- **Title**: SAM $\leftrightarrow \text{ST}(S^R)$ Blumer–Crochemore Duality and 3-Case Generalized SAM (`广义 SAM`)
- **Core Invariant Taught**: Exact structural duality $\mathcal{T}_{\text{link}}(\text{SAM}(S)) \cong \text{ST}(S^R)$ and $\mathcal{T}_{\text{link}}(\text{SAM}(S^R)) \cong \text{ST}(S)$; contiguous equivalence length interval $[\text{len}(\text{link}(u))+1, \text{len}(u)]$; the 3-Case Generalized SAM invariant (eliminating the zero-length ghost-clone bug when $\delta(p, c) = q$ already exists); and the Binary-Alphabet $\Theta(V^2)$ Trie-DFS Counterexample (`{a^k b}`) proving why Compressed-Trie GSAM **must** be built in BFS order ($O(V|\Sigma|)$).
- **Assigned Technique IDs**: `T-2A-01` | **Prerequisites**: None beyond single-string SAM/SA baseline.
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: `CF 452E — Three Strings` (`W2A-14`), `CF 204E — Little Elephant and Strings` (`W2A-05`) $\to$ *Intermediate*: `[USACO 2017 Dec Plat] Standing Out from the Herd` (`W2A-08`) $\to$ *Advanced*: `[ZJOI2015] 诸神眷顾的幻想乡` (`W2A-02`, Trie-BFS GSAM on 20-leaf trees) $\to$ *Mastery*: Multi-Trie GSAM Substring Distribution & Zero-Clone Trap Stress Problems.

#### `Ch 10` — `10-sam-endpos-segment-tree-merging.qmd`
- **Title**: SAM + Persistent Segment Tree Merging on $\text{endpos}$ and Substring Containment Clipping
- **Core Invariant Taught**: The Substring Containment Clipping Identity ($P \in E(u)$ of length $L$ occurs inside $S[l..r] \iff L \le r - l + 1$ and $\text{endpos}_S(u) \cap [l + L - 1, r] \ne \emptyset$); Predecessor Maximum-Length Jump $L_{\text{valid}}(u) = \min(L_{\text{raw}}, e_{\max} - l + 1)$ where $e_{\max} = \max(\text{endpos}_S(u) \cap [1, r])$; single-witness sufficiency (`any_pos[u]`) on the Link Tree (`CF 700E`); and non-destructive persistent Segment Tree merging (`++seg_sz` on overlap).
- **Assigned Technique IDs**: `T-2A-03` | **Prerequisites**: `Ch 09`
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: `CF 666E — Forensic Examination` (`W2A-23`) $\to$ *Intermediate*: `CF 700E — Cool Slogans` (`W2A-24`), `[HEOI2016/TJOI2016] 字符串` $\to$ *Advanced*: `CF 1037H — Security` (`W2A-25`) $\to$ *Mastery*: `[NOI2018] 你的名字` (`W2A-34`, Luogu P4770 — two-pointer clipped $\text{endpos}$ matching + intra-state deduplication).

#### `Ch 11` — `11-dynamic-sam-lct-stratification.qmd`
- **Title**: Dynamic SAM + Link-Cut Tree (`access` Color-Chain Sweeping) and Intra-State Length Stratification
- **Core Invariant Taught**: Solid-Chain Last-Occurrence Telescoping (why a vertical LCT chain $C = (u_1 \dots u_k)$ sharing last-occurrence color $p_{\text{old}}$ tiles start positions without gaps into $[p_{\text{old}} - \text{len}(u_k) + 1, p_{\text{old}} - \text{len}(\text{link}(u_1))]$, reducing offline $[l, r]$ distinct substring queries to $O(N \log^2 N)$ `access` color sweeps); Second-Largest $\text{endpos}$ Sweeping ($e_2(u, r)$); online LCT-SAM `clone` lazy-tag flushing (`[BZOJ 2555]`); and Intra-State Length Stratification on $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$ for substring prefix-implication DAGs (`[十二省联考 2019] 字符串问题`).
- **Assigned Technique IDs**: `T-2A-04`, `T-2A-05` | **Prerequisites**: `Ch 09`, `Ch 10`
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: `[BZOJ 2555] SubString` (`W2A-26`) $\to$ *Intermediate*: `Luogu P6292 — 区间本质不同子串个数` (`W2A-35`, LCT `access` color-chain sweep) $\to$ *Advanced*: `[十二省联考 2019] 字符串问题` (`W2A-37`, Luogu P5284 — intra-state length sorting + Link-Tree DAG longest path) $\to$ *Mastery*: `[Code+#3] 白金元首与莫斯科` (`W2A-39`, 2-SAT on Link-Tree HLD) & Polynomial-Weighted Range Distinct Substrings (`W2A-36`).

#### `Ch 12` — `12-sais-virtual-suffix-trees-dominant-pairs.qmd`
- **Title**: Induced Sorting (`SA-IS`), Zero-Tree Virtual Suffix Trees, and Suffix Tree Dominant Pairs (`启发式合并支配对`)
- **Core Invariant Taught**: $\text{rk}$-Descent Duality ($\text{type}(i)=L \iff \text{rk}[i]>\text{rk}[i+1]$) and LMS-Substring Prefix-Free Order Homomorphism (`SA-IS` + Fischer's $O(N)$ induced LCP); Three-Way Isomorphism $\mathcal{T}_{\text{ST}}(S) \cong \mathcal{T}_{\text{link}}(\text{SAM}(S^R)) \cong \text{Min-Cartesian}(\text{height})$ and Zero-Tree Virtual Suffix Tree construction over $k$ query substrings via $O(1)$ LCE; and DSU-on-Tree Predecessor/Successor Dominance generating $\le 2N \log_2 N$ dominant triples $(i^-, i, \ell_u), (i, i^+, \ell_u)$ capturing all $\binom{N}{2}$ suffix pairs.
- **Assigned Technique IDs**: `T-2B-01`, `T-2B-02`, `T-2B-03` | **Prerequisites**: `Ch 09`
- **Target Problem Ladder Scope** (9 problems): *Stepping Stone*: `[AHOI2013] 差异` (`W2B-01`), `[NOI2015] 品酒大会` (`W2B-04`), `CF 802I` (`W2B-03`) $\to$ *Intermediate*: `CF 616F — Expensive Strings` (`W2B-15`), `CF 1073G — Yet Another LCP Problem` (`W2B-11`) $\to$ *Advanced*: `AtCoder AGC 060 D — Same Descent Set` (`W2B-42`), Range Longest Repeated Substring via Dominant Pairs (`W2B-35`) $\to$ *Mastery*: `CF 1043G — Speckled Band` (`W2B-36`), `CF 1098F — Ж-function` (`W2A-40`).

#### `Ch 13` — `13-cdawg-scdawg-suffix-balanced-trees.qmd`
- **Title**: Compact & Bi-Directional Suffix Structures: `CDAWG`, Unamortized Persistent SAM, `SCDAWG`, and Hash-Free Suffix Balanced Trees
- **Core Invariant Taught**: Unary out-degree compaction of $\text{SAM}(S)$ into Maximal Repeats ($\text{CDAWG}$, $V_{\text{CDAWG}}(S) = V_{\text{CDAWG}}(S^R)$); Persistent Ancestor-Transition Inheritance (`anc_trans[u][c]`) eliminating amortized link walks on version trees; Two-Sided Closure Commutativity ($\overleftrightarrow{u}$) and Ukkonen–Weiner Active-Frontier Duality in `SCDAWG` (`push_front` / `push_back`); and Dietz–Sleator 64-Bit Scapegoat Midpoint Tags + BST adjacent-`height` RMQ for deterministic Hash-Free Suffix Balanced Trees (`后缀平衡树`).
- **Assigned Technique IDs**: `T-2A-02`, `T-2B-05`, `T-2B-06` | **Prerequisites**: `Ch 09`, `Ch 12`
- **Target Problem Ladder Scope** (7 problems): *Stepping Stone*: `[BZOJ 3682] Phorni` (`W2B-37`) $\to$ *Intermediate*: `[BZOJ 4768] wxh loves substring` (`W2B-38`), `CDAWG` Maximal Repeat Counting (`W2B-41`) $\to$ *Advanced*: Online Persistent Version-Tree SAM Queries (`W2A-41`) $\to$ *Mastery*: Bi-Directional `SCDAWG` Online `push_front`/`push_back` Distinct Substring & Repeat Maintenance (`W2B-40`).

#### `CP-III` — `checkpoints/cp-03-suffix-structures-lct-dominant-pairs.qmd`
- **Blind Checkpoint III**: 8 unspoiled problems testing recognition between GSAM Trie-BFS, clipped $\text{endpos}$ Segment Tree Merge, LCT `access` color sweeps, Virtual Suffix Trees, Suffix Tree Dominant Pairs, and Suffix Balanced Trees.

---

### Part IV: Internal Pattern Matching (IPM), Grammar Compression & Palindromic Theory (`Ch 14`–`Ch 17` + `CP-IV`)

#### `Ch 14` — `14-basic-substring-dictionary-ipm-borders.qmd`
- **Title**: Kociumaka's Basic Substring Dictionary, Bounded-Ratio IPM, and the 6 Methods of Substring Borders (`[BJWC2018]`)
- **Core Invariant Taught**: Bounded-Ratio IPM Arithmetic Progression Theorem (`Theorem 4.1`: when $|P| \le |T| < 2|P|$, $\text{Occ}(P, T)$ forms a single AP with step $d = \text{per}(P)$ because all occurrences overlap on a common core); Dyadic Scale Coverage $b \in [2^m, 2^{m+1})$ via intersecting the AP of prefix $P_m$ in the tail window with the AP of suffix $Q_m$ in the head window; and the complete 6-method synthesis for `[BJWC2018] Border 的四种求法` (Dyadic IPM, SAM Link-Tree HLD, Link-Tree Centroid Decomposition, DSU-on-Tree, $\sqrt{N}$ SA-Neighborhood, and Runs Sweep-Line).
- **Assigned Technique IDs**: `T-2B-04` | **Prerequisites**: `Ch 02`, `Ch 08`, `Ch 10`, `Ch 12`
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: `CF 504E — Misha and LCP on Tree` (`W2B-13`), Substring Global Rank/Select (`W2B-25`) $\to$ *Intermediate*: Bounded-Ratio Internal Pattern Matching $\text{Occ}(S[l_1..r_1], S[l_2..r_2])$ $\to$ *Advanced*: `[BJWC2018] Border 的四种求法` (`W2B-33`, Luogu P4482) $\to$ *Mastery*: $O(1)$ Internal Shortest Period Queries & Substring Square/Border Counting (`W2B-34`).

#### `Ch 15` — `15-locally-consistent-parsing-slp-attractors.qmd`
- **Title**: Locally Consistent Parsing (`局部一致性剖析`), Dynamic SLPs, String Attractors $\gamma(S)$, and Compressed Indexing
- **Core Invariant Taught**: Three-Engine Alternating Contraction (Maximal RLE `RComp` + Cole–Vishkin deterministic 6-coloring / randomized local extrema / Jeż's $\Sigma_L \times \Sigma_R$ Recompression shrinking string length by $\le 5/6$ per level with $O(1)$ destroyed context radius under dynamic split/concat/reverse); Primary-Seam Border-AP Matching on SLPs (`Theorem 4.2`); Kempa–Prezza String Attractors $\gamma(S)$ (SAM `minlen(q)` hitting-set duality) and Kempa–Kociumaka $\tau$-Synchronizing Sets; and Kärkkäinen–Ukkonen Primary–Secondary 2D Wavelet Range Indexing on LZ77/SLPs.
- **Assigned Technique IDs**: `T-3B-05`, `T-5B-05`, `T-5B-08` | **Prerequisites**: `Ch 02`, `Ch 09`, `Ch 14`
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: Pattern Matching on Static SLPs via Primary-Seam KMP (`W3B-35`) $\to$ *Intermediate*: Minimum String Attractor Verification & SAM `minlen` Hitting Set (`W5B-45`), $\tau$-Synchronizing Set Anchor LCE (`W5B-46`) $\to$ *Advanced*: Dynamic String Cut/Paste/Reverse + $O(\log N)$ LCE via Locally Consistent Parsing (`W3B-29`), LZ77/SLP 2D Orthogonal Range Pattern Indexing (`W5B-50`) $\to$ *Mastery*: Significant Suffixes, Palindromes & Runs on Huge SLPs (`W3B-40`).

#### `Ch 16` — `16-deterministic-deque-persistent-pam.qmd`
- **Title**: Unamortized Deterministic PAM (`quick_link` / `slink`-Skip), Persistent Tree PAM, and 4-Way Double-Ended Deque PAM
- **Core Invariant Taught**: Uniform Preceding-Character Lemma (`Lemma 1.1`: every ancestor in a PAM `slink` AP shares the same preceding character $S[i-\text{len}(v)-1]$, enabling $O(1)$ `quick_link[u][c]` for small $|\Sigma|$ and alphabet-free $O(\log N)$ `slink`-skip for large $|\Sigma|$ on version trees); Shared-Trie Node Invariance on Tree PAM (`[钟知闲 2017]`); and Palindrome Reversal Self-Duality + Unique Vanishing Palindrome Theorem + Non-Cascading Lazy Surface Push-Down (`max_pref` / `max_suff`) for worst-case $O(1)$ 4-Way Deque PAM (`push_front`, `push_back`, `pop_front`, `pop_back`).
- **Assigned Technique IDs**: `T-3A-01`, `T-3A-02` | **Prerequisites**: `Ch 04`
- **Target Problem Ladder Scope** (7 problems): *Stepping Stone*: `Luogu P4555` / Rollback PAM with `quick_link` (`W3A-07`) $\to$ *Intermediate*: 2-Way Push-Only Deque PAM (`W3A-18`), Persistent PAM on Version Trees (`W3A-15`) $\to$ *Advanced*: `[钟知闲 2017]` Shared-Trie Tree-Path Palindrome Queries (`W3A-29`), Sliding-Window Palindromes (`W3A-36`) $\to$ *Mastery*: Full 4-Way Deque PAM (`push/pop_front/back`) with Distinct & Total Palindrome Maintenance (`W3A-35`).

#### `Ch 17` — `17-range-palindrome-queries-rich-words.qmd`
- **Title**: Substring Palindrome Range Queries ($O(1)$ Range LPS & `slink` Telescoping), Rich Words, and Palindrome Factorizations
- **Core Invariant Taught**: True $O(1)$ Online Range LPS via Two-Boundary Unclipping (`Theorem 3.2`: every Manacher center $c \in (c_L, c_R)$ strictly between the boundary-touching centers touches neither $l$ nor $r$, reducing $\text{LPS}(l, r)$ to one $O(1)$ Sparse-Table RMQ); Midpoint Odd/Even Decoupling for Range Palindrome Multiplicity; `[徐毅 2014]` `slink` Periodic Suffix Telescoping ($\text{start}_{r-1}(u_j) = \text{start}_r(u_{j-1})$, reducing Range Distinct Palindromes to 2 Fenwick updates per `slink` chain); Droubay–Pirillo Rich Word unioccurrent LPS criterion ($l \ge L_{\text{rich}}[r]$); `CF 1827C` shortest even-palindrome suffix stripping; top-2 `slink` online 2-palindromes; and even-length $\theta$-palindromes.
- **Assigned Technique IDs**: `T-3A-03`, `T-3A-04`, `T-3A-05` | **Prerequisites**: `Ch 04`, `Ch 11`, `Ch 16`
- **Target Problem Ladder Scope** (9 problems): *Stepping Stone*: `POI XVII — Antisymmetry` (`W3A-05`), `CF 1827C — Palindrome Partition` (`W3A-03`) $\to$ *Intermediate*: Online 2-Palindrome Prefix Recognition (`W3A-19`), $O(1)$ Range Rich Substring Queries (`W3A-26`), Online Range Palindrome Multiplicity (`W3A-11`) $\to$ *Advanced*: $O(1)$ Online Range LPS via Two-Boundary Unclipping (`W3A-21`), `LOJ #6071` / `[徐毅 2014]` Range Distinct Palindromes (`W3A-31`) $\to$ *Mastery*: Weighted Range Distinct Palindromes via PAM `slink` Telescoping / LCT `access` (`W3A-32`, `W3A-38`).

#### `CP-IV` — `checkpoints/cp-04-ipm-slp-advanced-palindromes.qmd`
- **Blind Checkpoint IV**: 7–8 unspoiled problems testing recognition across Bounded-Ratio IPM, `[BJWC2018]` internal borders, Locally Consistent Parsing (`SLP`), 4-Way Deque PAM, $O(1)$ Range LPS, and `slink` telescoping Range Distinct Palindromes.

---

### Part V: Algebraic Convolution Matching, $k$-Mismatch & Structural Isomorphisms (`Ch 18`–`Ch 20` + `CP-V`)

#### `Ch 18` — `18-fft-wildcard-involution-affine-matching.qmd`
- **Title**: Polynomial & FFT String Matching: 1-NTT Wildcards, Kalai's Projection, Involution, and Affine Matching
- **Core Invariant Taught**: Index-Reflection Cauchy Convolution Duality ($P^R[k] = P[M-1-k]$); Clifford–Clifford cubic penalty vs. Degree-Reduced Indicator Penalty $D_{\text{ind}}(i) = \sum u_{P[j]} u_{T[i+j]}(v_{P[j]}-v_{T[i+j]})^2 \le M(|\Sigma|-1)^2 < 998244353$ (exact in 1 NTT prime with zero overflow); Kalai's randomized $\mathbb{F}_p$ projection (1 or 2 NTTs); 3-in-2 Complex Conjugate FFT packing; the `CF 1334G` 4-method hierarchy ($\pi^2 = \text{id} \implies O(N+M)$ canonical KMP vs. general $\pi$ via quartic / unit-circle / Kalai); Cauchy–Schwarz affine matching on $\Delta P_j$; and $\sqrt{M \log M}$ value-bucket splitting.
- **Assigned Technique IDs**: `T-3B-01`, `T-3B-02` | **Prerequisites**: Assumed KMP and FFT/NTT baseline.
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: `CF 528D — Fuzzy Search` (`W3B-01`), `[BZOJ 4503] 两个串` (`W3B-03`) $\to$ *Intermediate*: `CF 827E — Rusty String`, `CF 1334G — Substring Search` (`W3B-04`) $\to$ *Advanced*: Affine Scale-and-Shift Pattern Matching $T_{i+j} = \alpha P_j + \beta$ (`W3B-18`) $\to$ *Mastery*: Dominance ($\forall j, P_j \le T_{i+j}$) & $L_1$ Distance String Matching via $\sqrt{M\log M}$ Bucket Splitting (`W3B-24`).

#### `Ch 19` — `19-k-mismatch-edit-distance-period-dichotomy.qmd`
- **Title**: $k$-Mismatch & $k$-Edit String Matching: Kangaroo Jumps, Wavefront DP, and the $2k$-Period Dichotomy
- **Core Invariant Taught**: Landau–Vishkin $O(1)$ LCE Kangaroo Jumps partitioning $\le k$ mismatches into $\le k+1$ exact-match jumps ($O(Nk)$ mismatch) and diagonal wavefront DP $L_{e, d}$ ($O(N + k^2)$ edit distance); Abrahamson's Heavy–Light Alphabet Frequency Split ($O(N\sqrt{M\log M})$); and the Clifford–Gawrychowski–Uznański $2k$-Period Dichotomy (`Theorem 2.3`: when $\text{per}(P) > 2k$, $\le 2k$ witness pairs filter alignments to $O(N/k)$ candidates verified in $O(N)$ total time; when $\text{per}(P) = p \le 2k$, second-order periodic differences $\text{diff}_p(S)[x] = \mathbf{1}[S[x] \ne S[x-p]]$ compress convolution support to $O(k)$ RLE boundaries in $O(N\sqrt{k\log k})$).
- **Assigned Technique IDs**: `T-3B-03` | **Prerequisites**: `Ch 01`, `Ch 14`, `Ch 18`
- **Target Problem Ladder Scope** (7 problems): *Stepping Stone*: $k$-Mismatch Substring Search via Kangaroo LCE Jumps (`W3B-15`) $\to$ *Intermediate*: `[BZOJ 4259] 残缺的字符串` (`W3B-08`), Abrahamson Heavy–Light $k$-Mismatch $\to$ *Advanced*: Landau–Vishkin $O(N + k^2)$ Diagonal Wavefront $k$-Edit Alignment (`W3B-27`) $\to$ *Mastery*: Clifford–Gawrychowski–Uznański $O(N\sqrt{k\log k})$ $2k$-Period Dichotomy Matching.

#### `Ch 20` — `20-structural-isomorphism-weighted-2d-matching.qmd`
- **Title**: Structural Isomorphism Matching (`p-KMP`, `Order-KMP`, `Cartesian-KMP`), $1/z$ Weighted Suffix Trees, and 2D Matching
- **Core Invariant Taught**: Unified Window-Clipped Backward Offset Invariance $\text{clip}(\text{prev}_S[x], q) = (\text{prev}_S[x] \le q \text{ ? } \text{prev}_S[x] : 0)$ restoring prefix monotonicity for $O(N+M)$ Parameterized KMP (`p-KMP`) and Parent-Distance Cartesian-Tree KMP (`PD_S[x]`); `LMax`/`LMin` neighbor sufficiency for Order-Preserving KMP; Baker's Single-Position Mutation Invariant for $O(N \log N)$ Parameterized SA (`p-SA`); Binary Abelian Parikh Continuity (`[m_\ell, M_\ell]`); Barton et al.'s Disjoint-Event Probability Sum Bound ($\le \lfloor z \rfloor$ heavy branches of total length $O(nz)$) for $1/z$ Weighted Suffix Trees; and Baker–Bird Row-ID Factoring + Vishkin's $O(1)$ 2D Witness Duel.
- **Assigned Technique IDs**: `T-3B-04`, `T-5B-06`, `T-5B-07` | **Prerequisites**: `Ch 01`, `Ch 12`
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: Parameterized KMP (`p-KMP`) & Binary Abelian Parikh Envelope Queries (`W3B-06`, `W3B-34`) $\to$ *Intermediate*: Order-Preserving KMP via `LMax`/`LMin` (`W3B-09`), $O(N+M)$ Parent-Distance Cartesian-Tree KMP (`W3B-31`, `W5B-48`) $\to$ *Advanced*: Parameterized Suffix Array (`p-SA`), Baker–Bird 2D Pattern Matching & Vishkin 2D Duel (`W5B-49`) $\to$ *Mastery*: $1/z$ Heavy-String Decomposition & Weighted Suffix Tree Pattern Indexing (`W5B-47`).

#### `CP-V` — `checkpoints/cp-05-fft-kmismatch-isomorphism-2d.qmd`
- **Blind Checkpoint V**: 6–8 unspoiled problems testing recognition across 1-NTT indicator wildcards, `CF 1334G` involution/permutation matching, $2k$-period $k$-mismatch dichotomy, window-clipped `p-KMP`/`Cartesian-KMP`, and 2D witness duels.

---

### Part VI: Autocorrelation Generating Functions, `DP套DP`, Subsequence & Seaweed Matrices (`Ch 21`–`Ch 24` + `CP-VI`)

#### `Ch 21` — `21-goulden-jackson-moment-shift-martingales.qmd`
- **Title**: The Guibas–Odlyzko Overlap Algebra: Goulden–Jackson Cluster GFs, the $t=1+u$ Moment Shift, and Conway's Casino Martingales
- **Core Invariant Taught**: The Guibas–Odlyzko Autocorrelation Polynomial $C_{i,j}(x) = \sum_{k \in \text{Overlap}(P_i, P_j)} x^{|P_j|-k}$ and Commutative-Ring Invertibility ($\mathbf{C}(0) = I_m \implies \det \mathbf{C}(x) \in 1 + x\mathcal{R}[[x]]$); Bivariate $(t-1)$ Exact $k$-Occurrence OGF $[t^k]F(x, t) = \frac{x^L D_1(x)^{k-1}}{D_0(x)^{k+1}}$ (factoring $x^{d_{\min}}$ from $D_1(x)$ before $\ln/\exp$) and Non-Antichain Embedded Substring Weight Absorption; the `Universal Cup / QOJ` $t = 1 + u$ Binomial Moment Shift collapsing the denominator to $(1-\sigma x)^{j+1}$ for $n \le 10^{18}$; and Conway's Fair-Betting Martingale Payoff $\Omega_{P_i, P_j}$ for waiting times, variance, $k$-th occurrence renewal $\mathbb{E}[T_{S,1}] + \frac{k-1}{\mathbb{P}(S)}$, and division-free pattern races (`[SDOI2017] 硬币游戏`).
- **Assigned Technique IDs**: `T-4A-01`, `T-4A-02`, `T-4A-03`, `T-4A-04` | **Prerequisites**: `Ch 01`
- **Target Problem Ladder Scope** (9 problems): *Stepping Stone*: `[CTSC2006] 歌唱王国` (`W4A-02`), Single-Pattern Avoidance OGF (`W4A-01`) $\to$ *Intermediate*: `[SDOI2017] 硬币游戏` (`W4A-09`), Variance & $k$-th Occurrence Renewal Waiting Time (`W4A-19`) $\to$ *Advanced*: Exact $k$-Occurrence FPS (`W4A-08`), Non-Antichain Weighted Multi-Pattern Cluster GFs (`W4A-28`), Pattern Race with Seed Prefix $S_0$ (`W4A-27`) $\to$ *Mastery*: `Universal Cup / QOJ` Expected $K$-th Power of Pattern Occurrences for $n \le 10^{18}$ via $t = 1 + u$ Shift (`W4A-39`).

#### `Ch 22` — `22-bit-parallel-lcs-automaton-dp-of-dp.qmd`
- **Title**: Bounded-Difference DP Encodings: Bit-Parallel Alignment (Allison–Dix & Myers), the `DP套DP` Compiler, and Binary-Grouped AC
- **Core Invariant Taught**: Monotonic DP row/column difference vectors ($\Delta_j = dp[i][j] - dp[i][j-1] \in \{0, 1\}$ for LCS; $\Delta V, \Delta H \in \{-1, 0, +1\}$ for Myers Levenshtein); Allison–Dix 4-Instruction Interval-Local Borrow Absorption $V' = X \mathbin{\&} \sim(X - Y)$ ($O(MN/w)$ time) + Hirschberg $O(M+N)$-space bitset alignment reconstruction; the 4-Stage `DP套DP` State-Compression Compiler (Difference/Strip Encoding $\to$ Reachable DFA BFS $\to$ Hopcroft/Brzozowski Minimization $\to$ Outer DP, using the Allison–Dix transition directly as the inner DFA step!); and Bentley–Saxe Binary-Grouped Dynamic Aho–Corasick (`CF 710F`).
- **Assigned Technique IDs**: `T-4B-05`, `T-4A-05` | **Prerequisites**: Assumed AC Automaton baseline.
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: `[JSOI2007] 文本生成器` (`W4A-05`), `CF 710F — String Set Queries` (`W4A-14`) $\to$ *Intermediate*: Bit-Parallel LCS + Hirschberg $O(M+N)$-Space Alignment Reconstruction (`W4B-19`), Myers' Bit-Parallel Semi-Local Substring Edit Distance (`W4B-26`) $\to$ *Advanced*: `[TJOI2018] 游园会` / LCS `DP套DP` (`W4A-30`), Bit-Parallel Circular LCS (`W4B-36`) $\to$ *Mastery*: Edit-Distance Strip `DP套DP` + Offline Hopcroft DFA Minimization (`W4A-37`).

#### `Ch 23` — `23-subsequence-automata-arch-invertible-matrices.qmd`
- **Title**: Subsequence Automata (`DASG`), Arch Factorization, Simon's Congruence ($\sim_k$), and Invertible Subsequence Matrices
- **Core Invariant Taught**: Leftmost-Prefix Greedy Dominance in $\text{DASG}(S)$, the `[HEOI2015]` Four-Comb Product Automaton $\mathcal{A}^+(A) \times \mathcal{A}^-(B)$ ($\text{SAM}/\text{DASG}$), and Alphabet-Independent $O(|A||B|)$ Distinct Common Subsequence counting via 2D Predecessor Rectangles; Hébrard's Arch Factorization ($\iota(S) = k \implies \text{sas}(S) = k+1$ with last-letter witness $m_1 \dots m_k m_{k+1}$), $O(\log N)$ Range SAS via binary lifting, and Simon's Congruence ($\sim_k$); and Rank-1 Elementary Matrix Invertibility ($M_c = I_{\sigma+1} + \mathbf{e}_c \mathbf{1}^T, \det M_c = 1, M_c^{-1} = I_{\sigma+1} - \mathbf{e}_c(\mathbf{1}-2\mathbf{e}_c)^T$) reducing range $[l, r]$ distinct subsequence queries to an $O(|\Sigma|)$ matrix-free dot product $\mathbf{u}_r^T \cdot \mathbf{v}_{l-1}$.
- **Assigned Technique IDs**: `T-4B-01`, `T-4B-02`, `T-4B-03` | **Prerequisites**: `Ch 09`
- **Target Problem Ladder Scope** (9 problems): *Stepping Stone*: `AtCoder ARC 081 E — Don't Be a Subsequence` (`W4B-02`), `CF 1303E` (`W4B-05`), `CF 1149B — Three Religions` (`W4B-12`) $\to$ *Intermediate*: `[HEOI2015] 最短不公共子串` (`W4B-11`), Distinct Common Subsequences via 2D Predecessor Rectangles (`W4B-07`), $O(\log N)$ Range SAS (`W4B-24`) $\to$ *Advanced*: `CF 1426F` (`W4B-15`), Matrix-Free $O((N+Q)|\Sigma|)$ Range Distinct Subsequences (`W4B-27`) $\to$ *Mastery*: Deque Distinct Subsequences (`W4B-33`) & Shortest Distinguishing Subsequence via Simon's Congruence (`W4B-41`).

#### `Ch 24` — `24-tiskin-seaweed-matrices-unit-monge-lcs.qmd`
- **Title**: Tiskin's Seaweed Matrices (`海草矩阵`), $O(K\log K)$ Unit-Monge $\boxdot$ Multiplication, and $O(N\log^2 N)$ Range LIS
- **Core Invariant Taught**: Planar Wire Uncrossing Invariant (wires cross at $(i, j)$ iff $A[i] \ne B[j]$ and they have not previously crossed; exiting bottom port permutation $W[k]$ is the exact Unit-Monge cross-difference of semi-local LCS); Three-Family Semi-Local Dominance ($\text{LCS}(A, B[l..r]) = \#\{k \in [l, r] : W[k] < l\}$ and $\text{LCS}(A[1..i], B[l..r]) = \#\{k \in [l, r] : -i \le W[k] < l\}$); Monotone Advantage Staircase Walking for $O(K \log K)$ Unit-Monge $\boxdot$ multiplication; and Sparse Row Divide-and-Conquer for $O(N \log^2 N)$ Range LIS $\text{LIS}(B[l..r])$.
- **Assigned Technique IDs**: `T-4B-04` | **Prerequisites**: `Ch 22`, `Ch 23`
- **Target Problem Ladder Scope** (7 problems): *Stepping Stone*: `[THUPC 2021] 区间 LCS` (`W4B-28`, $O(MN)$ comb + 2D dominance queries) $\to$ *Intermediate*: Prefix-Substring LCS $\text{LCS}(A[1..i], B[l..r])$ via Signed Seaweed Rowports (`W4B-35`) $\to$ *Advanced*: Dynamic Character Appends (`append_A`, `append_B`) + Semi-Local LCS (`W4B-39`) $\to$ *Mastery*: $O(N \log^2 N)$ Range LIS $\text{LIS}(B[l..r])$ via Sparse Seaweed Unit-Monge $\boxdot$ (`W4B-42`).

#### `CP-VI` — `checkpoints/cp-06-generating-functions-dp-of-dp-seaweed.qmd`
- **Blind Checkpoint VI**: 7–8 unspoiled problems testing recognition across Goulden–Jackson $t=1+u$ moment shifts, Conway's Casino pattern races, Bit-Parallel + `DP套DP`, Matrix-Free Invertible Subsequence queries, and Tiskin's Seaweed Matrices.

---

### Part VII: Word Equations, Wheeler/Tree Strings, Stack Groups & Combinatorics on Words (`Ch 25`–`Ch 30` + `CP-VII` + `Capstones`)

#### `Ch 25` — `25-word-equations-signed-tree-dsu.qmd`
- **Title**: Word Equations, Signed & Tree Binary-Lifting DSU (`倍增并查集`), and Huge-Length ($N \le 10^{18}$) Period Folding
- **Core Invariant Taught**: Lossless Dyadic Block Covering ($[0, 2^k-1] \cup [L-2^k, L-1] = [0, L-1]$); Signed Half-Block Pushdown ($d=1$ cross-swaps $B_{k-1}(i) \leftrightarrow B_{k-1}(r+2^{k-1})^R$) and the **Root Self-Palindrome Bit `is_pal[k][r] = 1`** when two endpoints in the same component merge with net reversal parity $1$; Online Potential Amortization ($\Phi = \sum (c_k + p_k) \le 2N(K+1)$); LCA Upward-Path Splitting for Signed Tree Binary-Lifting DSU; and Plandowski / Fine–Wilf Euclidean Period Folding + Dihedral Reflection-to-Translation Reduction for $N \le 10^{18}$ word equations.
- **Assigned Technique IDs**: `T-5A-01`, `T-5A-02` | **Prerequisites**: `Ch 01`, `Ch 15`
- **Target Problem Ladder Scope** (7 problems): *Stepping Stone*: `[SCOI2016] 萌萌哒` (`W5A-01`, Luogu P3295) $\to$ *Intermediate*: Signed Substring & Palindrome Word Equations with `is_pal[k][r]` (`W5A-14`) $\to$ *Advanced*: Online Word Equations with Conflict Rollback (`W5A-29`), Tree Path Word Equations via Signed Tree Binary-Lifting DSU (`W5A-48`) $\to$ *Mastery*: Huge-Length ($N \le 10^{18}$) Palindrome & Translation Word Equations via Euclidean Period Folding (`W5A-36`).

#### `Ch 26` — `26-string-inequalities-sa-adjacency-inverse-reconstruction.qmd`
- **Title**: String Inequality Digraphs, the Suffix Array Adjacency Theorem, and Inverse String Reconstruction
- **Core Invariant Taught**: The Suffix Array Adjacency Theorem (`Theorem 2.1`: with sentinel $\text{rk}[N+1]=0$, adjacent $u=\text{SA}[i], v=\text{SA}[i+1]$ force $S[u] < S[v]$ iff $\text{rk}[u+1] > \text{rk}[v+1]$, giving $|\Sigma|_{\min} = D + 1$ and $\binom{N+K-1-D}{N}$ valid strings); $\{0, 1\}$-Weighted Inequality Digraphs over DSU components (feasible iff no weight-$1$ edge lies inside a Tarjan SCC); 2-SAT Lexicographical Prefix Branching (`CF 568C`); and Equality + Forbidden-Character Dual Decomposition + Chordal Chromatic Product $\prod \max(0, \sigma - \text{deg}_{\text{prev}}(v))$ (+ mandatory forward verification) for Inverse KMP $\pi$, Z-Array, and Manacher Radius Reconstruction.
- **Assigned Technique IDs**: `T-5A-03`, `T-3A-06` | **Prerequisites**: `Ch 01`, `Ch 12`, `Ch 25`
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: `AtCoder ARC 044 D` (`W5A-03`), `CF 1526E — Oolimry and Suffix Array` (`W5A-04`) $\to$ *Intermediate*: Inverse KMP / Z-Array / Manacher Reconstruction & Chordal Counting (`W3A-08`, `W3A-14`), `[SDOI2017]` Period Array Reconstruction (`W5A-08`) $\to$ *Advanced*: `CF 568C — New Language` (`W5A-19`) $\to$ *Mastery*: Combined Substring Equations + LCP-Witnessed String Inequalities via Binary-Lifting DSU + SCC Longest Path (`W5A-33`).

#### `Ch 27` — `27-debruijn-best-bwt-wheeler-move-structures.qmd`
- **Title**: De Bruijn Graphs, the AC-DFA BEST Theorem, Wheeler Graphs, and $O(1)$ RLBWT Move Structures
- **Core Invariant Taught**: Subword-to-Edge Eulerian Bijection & the AC-DFA BEST Theorem dividing by character-transition multiplicities $\prod_{u \in V_{\text{act}}, c \in \Sigma} \text{count}(u, c)!$ (avoiding the parallel-edge trap when $u \xrightarrow{c_1} v$ and $u \xrightarrow{c_2} v$ land in the same AC state $v$); Lex-Smallest Hierholzer Post-Order Invariant; LF-Mapping Rank Preservation; Wheeler Graph Monotonicity Axioms and Two-Step Edge-Rank Interval Transitions ($[l_V, r_V] \to [l_E, r_E] \to [l'_V, r'_V]$); and Nishimoto–Tabei $O(1)$ RLBWT Move Structures for compressed texts of length $N \le 10^{18}$.
- **Assigned Technique IDs**: `T-5A-04`, `T-5A-05` | **Prerequisites**: `Ch 05`, `Ch 12`
- **Target Problem Ladder Scope** (7 problems): *Stepping Stone*: `CF 508D — Tanya and Password` (`W5A-11`), Cyclic BWT Inversion (`W5A-15`) $\to$ *Intermediate*: `AtCoder ABC 336 G — 16 Integers` (`W5A-24`), Multi-Cycle BBWT Necklace Counting (`W5A-31`) $\to$ *Advanced*: `UOJ #607` / AC-DFA BEST Theorem String Counting (`W5A-41`), Wheeler Graph Recognition & Interval DFA Matching (`W5A-38`) $\to$ *Mastery*: RLBWT Pattern Matching for $N \le 10^{18}$ via Nishimoto–Tabei $O(1)$ Move Structure (`W5A-43`).

#### `Ch 28` — `28-strings-on-trees-sa-gsam-centroid.qmd`
- **Title**: Strings on Trees: Dual-Rank Tree Suffix Arrays, Leaf-Rooted Tree GSAM, and Centroid + $\sqrt{M}$ Dual-SAM Split
- **Core Invariant Taught**: Why Kasai's $O(N)$ LCP fails on branched trees and how Dual-Rank Tree SA maintains both true equivalence $\text{rk}_k[u]$ and tie-broken permutation $\text{id}_k[u] \in \{1..N\}$ via 4-tuple radix sorting ($O(N \log N)$ build, $O(\log N)$ binary-lifting LCP); Leaf-Rooted Substring Cover (`[ZJOI2015]`: every simple path in a tree with $|\mathcal{L}| \le 20$ leaves is a suffix of a leaf-to-node path); and Centroid Decomposition + $\sqrt{M}$ Dual-SAM Split (`[CTSC2010] 珠宝商`, thresholding **both** centroid component size $S_c$ and individual child subtrees $|T_{\text{sub}}|$ against $\sqrt{M}$).
- **Assigned Technique IDs**: `T-5A-06` | **Prerequisites**: `Ch 09`, `Ch 10`, `Ch 12`
- **Target Problem Ladder Scope** (7 problems): *Stepping Stone*: `CF 291E` (Deterministic KMP DFA on Trees), `Luogu P5353 — 树上后缀排序` (`W5A-18`) $\to$ *Intermediate*: `ICPC WF 2019 D — First of Her Name` (`W2B-31`), `[ZJOI2015] 诸神眷顾的幻想乡` (`W5A-21`) $\to$ *Advanced*: `CF 914E — Palindromes in a Tree` (`W5A-35`) $\to$ *Mastery*: `[CTSC2010] 珠宝商` (`W5A-46`, Luogu P4218 — Centroid + $\sqrt{M}$ Dual-SAM Split with child-subtree thresholding).

#### `Ch 29` — `29-free-group-sl2-matrix-hashing-stack-trie.qmd`
- **Title**: Free Group / Coxeter Stack Reduction, Non-Abelian $GL_2(\mathbb{F}_p) / SL_2(\mathbb{F}_p)$ Matrix Hashing, and Stack-Trie Path Isomorphism
- **Core Invariant Taught**: The Deterministic Stack-Trie Path Isomorphism Theorem (`Theorem 3.1.2`: walking prefixes on the Stack-Trie $\mathcal{T}$ maps the reduced word $\text{red}(S[l..r]) = P_{l-1}^{-1}P_r$ bijectively to the simple tree path $u_{l-1} \leadsto \text{LCA}_{\mathcal{T}}(u_{l-1}, u_r) \leadsto u_r$, reducing $|\text{red}(S[l..r])|$ to $\text{dist}_{\mathcal{T}}(u_{l-1}, u_r)$ and lexicographical comparison of stack-reduced substrings to $O(\log N)$ Tree-Path LCE with **zero matrices**); Cayley–Hamilton trace-zero $\det=-1$ involutions $M_c^2 = I_2$ in $GL_2(\mathbb{F}_p)$ for `cc` $\to \varepsilon$; and Height-Indexed $(c, \text{bal}[i])$ random $SL_2(\mathbb{F}_p)$ generators for dynamic Segment Tree Dyck/stack maintenance.
- **Assigned Technique IDs**: `T-5B-04` | **Prerequisites**: `Ch 28`
- **Target Problem Ladder Scope** (7 problems): *Stepping Stone*: `CF 1223F — Stack Exterminable Arrays` (`W5B-01`) $\to$ *Intermediate*: `AtCoder AGC 050 C`, `ARC 119 E` / Stack-Cancellation Invariants $\to$ *Advanced*: Dynamic Point-Update Range Dyck / Stack Reduction via Height-Indexed $SL_2(\mathbb{F}_p)$ Segment Tree (`W5B-15`) $\to$ *Mastery*: Lexicographical Comparison & LCE of Stack-Reduced Substrings $\text{red}(S[l_1..r_1])$ vs. $\text{red}(S[l_2..r_2])$ via Stack-Trie Path LCE (`W5B-42`).

#### `Ch 30` — `30-sturmian-singular-words-thue-morse-morphisms.qmd`
- **Title**: Combinatorics on Words: Sturmian & Singular Words (`[周任飞 2017]`), Thue–Morse Anti-Hash, and Iterated Morphisms $\varphi^k(S_0)$
- **Core Invariant Taught**: Six-Way Sturmian Equivalence ($p_{\mathbf{w}}(n)=n+1 \iff$ unique special factors $L_n = R_n^R \iff$ 1-balanced $\iff$ mechanical rotation $s_{\alpha,\rho} \iff$ central bispecial palindromes $\pi_k$ hitting the Fine–Wilf threshold) and `[周任飞 2017]` Rytter's Singular Words $w_k$ partitioning Fibonacci factors into disjoint layers for $O(\log n)$ Zeckendorf queries at $n \le 10^{18}$; Thue–Morse overlap-freeness, Prouhet–Tarry–Escott vanishing derivatives, and 2-adic valuation $v_2 \ge k(k+1)/2$ annihilating `uint64_t` rolling hashes at $2^{11}=2048$; and the $(2m-2)$-Seam Decomposition for pattern counting in $\varphi^k(S_0)$ (Regime 1: 2-letter junction matrix; Regime 2: KMP functional composition for unit-growth letters; Regime 3: `CF 1466G` level promotion $r_0$).
- **Assigned Technique IDs**: `T-5B-01`, `T-5B-02`, `T-5B-03` | **Prerequisites**: `Ch 01`, `Ch 08`, `Ch 13`, `Ch 17`
- **Target Problem Ladder Scope** (8 problems): *Stepping Stone*: Universal Anti-`uint64_t` Rolling-Hash Construction (`W5B-02`), Tarry–Escott Equal-Power-Sum Partitioning (`W5B-11`) $\to$ *Intermediate*: `ICPC WF 2012 D — Fibonacci Words` (`W5B-18`), `CF 1466G — Song of the Sirens` (`W5B-06`) $\to$ *Advanced*: `AtCoder ABC 313 G` (`W5B-04`), General Iterated Morphism $\varphi^k(S_0)$ Pattern Counting for $k \le 10^{18}$ (`W5B-27`) $\to$ *Mastery*: `[周任飞 2017]` Exact Distinct Substrings, Palindromes & Runs in Fibonacci Prefixes $F_\infty[1..n]$ ($n \le 10^{18}$) via Singular Word Decomposition (`W5B-31`).

#### `CP-VII` — `checkpoints/cp-07-word-equations-trees-sl2-morphic.qmd`
- **Blind Checkpoint VII**: 8 unspoiled problems testing recognition across Signed/Tree Binary-Lifting DSU, SA Adjacency / Inverse Reconstruction, AC-DFA BEST Theorem, Nishimoto–Tabei RLBWT Move Structures, `[CTSC2010] 珠宝商` Centroid Dual-SAM, Stack-Trie Path LCE, and Singular Words / Morphic Matrices.

#### `Capstone` — `capstones/synthesis.qmd`
- **Grandmaster Multi-Chapter Synthesis Reserves (`Syn-01`–`Syn-25`)**: 25 multi-paradigm grandmaster problems combining 2–4 distinct parts (e.g., Runs + SAM + Segment Tree Merging; Lyndon Significant Suffixes + Locally Consistent Parsing SLPs; Tiskin's Seaweed Matrices + `DP套DP`; PAM `slink` Telescoping + String Attractors).

---

## 4. Verification Matrix: Complete Partition of All 57 Technique IDs (`T-1A-01..T-5B-08`)

Every single technique family in `TECHNIQUE_TAXONOMY.md` has a **unique primary home chapter** in `Ch 01`–`Ch 30` with zero forward references:

- **Wave 1A (`5/5`)**: `T-1A-01` $\to$ `Ch 01`; `T-1A-02` $\to$ `Ch 02`; `T-1A-03` $\to$ `Ch 03`; `T-1A-04`, `T-1A-05` $\to$ `Ch 04`.
- **Wave 1B (`6/6`)**: `T-1B-01`, `T-1B-02` $\to$ `Ch 05`; `T-1B-03` $\to$ `Ch 06`; `T-1B-04` $\to$ `Ch 07`; `T-1B-05`, `T-1B-06` $\to$ `Ch 08`.
- **Wave 2A (`5/5`)**: `T-2A-01` $\to$ `Ch 09`; `T-2A-02` $\to$ `Ch 13`; `T-2A-03` $\to$ `Ch 10`; `T-2A-04`, `T-2A-05` $\to$ `Ch 11`.
- **Wave 2B (`6/6`)**: `T-2B-01`, `T-2B-02`, `T-2B-03` $\to$ `Ch 12`; `T-2B-04` $\to$ `Ch 14`; `T-2B-05`, `T-2B-06` $\to$ `Ch 13`.
- **Wave 3A (`6/6`)**: `T-3A-01`, `T-3A-02` $\to$ `Ch 16`; `T-3A-03`, `T-3A-04`, `T-3A-05` $\to$ `Ch 17`; `T-3A-06` $\to$ `Ch 26`.
- **Wave 3B (`5/5`)**: `T-3B-01`, `T-3B-02` $\to$ `Ch 18`; `T-3B-03` $\to$ `Ch 19`; `T-3B-04` $\to$ `Ch 20`; `T-3B-05` $\to$ `Ch 15`.
- **Wave 4A (`5/5`)**: `T-4A-01`, `T-4A-02`, `T-4A-03`, `T-4A-04` $\to$ `Ch 21`; `T-4A-05` $\to$ `Ch 22`.
- **Wave 4B (`5/5`)**: `T-4B-01`, `T-4B-02`, `T-4B-03` $\to$ `Ch 23`; `T-4B-04` $\to$ `Ch 24`; `T-4B-05` $\to$ `Ch 22`.
- **Wave 5A (`6/6`)**: `T-5A-01`, `T-5A-02` $\to$ `Ch 25`; `T-5A-03` $\to$ `Ch 26`; `T-5A-04`, `T-5A-05` $\to$ `Ch 27`; `T-5A-06` $\to$ `Ch 28`.
- **Wave 5B & Frontier (`8/8`)**: `T-5B-01`, `T-5B-02`, `T-5B-03` $\to$ `Ch 30`; `T-5B-04` $\to$ `Ch 29`; `T-5B-05`, `T-5B-08` $\to$ `Ch 15`; `T-5B-06`, `T-5B-07` $\to$ `Ch 20`.
