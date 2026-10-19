# Cohort 3 — Wave 3A Master Reconciled Monograph: 0-1 Fractional Programming + Min-Cut, Maximum Density Subgraphs, Planar Graph Duality, Min-Cut DP / Data Structures, and Gomory–Hu Cut Trees

**Iteration 109 (Synthesizing Cohort 1 Iterations 21–25 & Cohort 2 Iterations 73–77)**  
**Author**: `FlowDeepInvestigator` (Cohort 3 Master Reconciliation Investigator)  
**Target Monograph**: `/home/maomao90/Documents/IO/ICPC-math-notes/flows_research/cohort3_wave_3a_density_planar_mincut_dp_gomory_hu.md`

---

## Executive Summary & Architectural Philosophy

This Cohort 3 Master Reconciled Monograph unifies, cross-examines, and expands the independent research investigations of **Cohort 1 (`iter_21_to_25_density_planar_mincut_dp_gomory_hu.md`, 1,491 lines)** and **Cohort 2 (`cohort2_iter_73_to_77_density_planar_mincut_dp_gomory_hu.md`, 1,621 lines)** across five foundational pillars where combinatorial network flow intersects continuous optimization, computational topology, dynamic programming, and polyhedral cut theory:

1. **Iteration 21 / 73 — 0-1 Fractional Programming + Minimum Cut (`分数规划最小割` / Dinkelbach's Method)**: Reducing ratio objectives $R(x) = f(x)/g(x)$ to parametric pseudo-Boolean cut polynomials $h(\lambda) = \min_{x \in \{0,1\}^N} [f(x) - \lambda g(x)]$ under the **Submodularity Sign Law**, comparing Binary Search, Dinkelbach's Secant Method, and Gallo–Grigoriadis–Tarjan (GGT) Parametric Preflow.
2. **Iteration 22 / 74 — Maximum Density Subgraph (`最大密度子图` / Goldberg's Reduction & Amber's Treatise)**: Unifying the $|V|+|E|$ Bipartite Closure model and the $|V|$-only Degree-Identity model ($|E(S)| = \frac{1}{2}\sum_{v \in S} \deg(v) - \frac{1}{2}|\delta(S)|$), proving the exact $\frac{1}{N(N-1)}$ rational gap, and bridging to **Hakimi's Orientation Theorem**, **Nash-Williams Arboricity**, and Charikar's 2-approximation peeling.
3. **Iteration 23 / 75 — Planar Graph Duality ($s$-$t$ Planar Min-Cut $\leftrightarrow$ Dual Dijkstra)**: Formalizing the Coarea Formula for continuous/discrete potential fields (`[NOI2010] 海拔`), reconciling opposite $S^*/T^*$ clockwise/counter-clockwise rotation conventions via a single Left/Right Bank Orientation Invariant, solving Multi-Terminal Outerplanar Cuts via circular interval DP (`[CSP-S 2021] 交通规划`), and handling interior $s$-$t$ cuts via Reif's primal-path slicing and $\mathbb{Z}_2$-parity double cover.
4. **Iteration 24 / 76 — Solving Max-Flow via Min-Cut DP, Greedy & Segment Trees**: Eliminating explicit flow engines when $N \le 5 \times 10^5$ by translating $s$-$t$ cut capacities into $O(N \log N)$ slope-trick greedies (`CF 724 E`), $2 \times 2$ $(\min, +)$ tropical matrix segment trees (`CF 1919 F1/F2`), Dynamic DP on Heavy-Light Decompositions (`Luogu P4719`), coordinate rank-slot transformations (`AGC 031 E`), and bipartite degree-sorted prefix queries (`ARC 125 E`).
5. **Iteration 25 / 77 — Global Minimum Cut (Stoer–Wagner) & All-Pairs Min-Cut Trees (Gomory–Hu / Gusfield `最小割树`)**: Proving symmetric submodularity and posimodularity, contrasting recursive vertex-bucket Gomory–Hu construction with Gusfield's 15-line star-splitting algorithm, characterizing ultrametric tree realizability (`CF 343 E`), and expanding to **Karger–Stein randomized contraction** and the **Dinits–Karzanov–Lomonosov (DKL) Cactus Representation of All Global Minimum Cuts**.

Every theoretical derivation and all **32 curated contest problems** strictly obey the **4-Step "Zero Magic Gadgets" Compilation Mandate**: (1) Non-Graph Diagnostic Signal, (2) Intermediate Algebraic / Logical Representation, (3) Reverse-Engineering Scratchpad, and (4) Hand-Checkable Toy Trace & Broken Gadget Counterexamples.

---

## Section 1: Cross-Cohort Blind-Spot Audit & Reconciliation Matrix

Before synthesizing the unified theory, we audit what Cohort 1 (`iter_21_to_25`) and Cohort 2 (`cohort2_iter_73_to_77`) independently discovered, where each cohort had blind spots or subtle discrepancies, and how Cohort 3 reconciles them into a single gold-standard reference.

### 1.1 Theoretical & Modelling Blind-Spot Matrix

| Topic / Iteration | Cohort 1 (`iter_21_to_25`) Unique Strengths | Cohort 2 (`cohort2_iter_73_to_77`) Unique Strengths | Discrepancies / Conflicts Identified | Cohort 3 Master Reconciliation & New Expansions |
| :--- | :--- | :--- | :--- | :--- |
| **Iter 21 / 73: 0-1 Fractional Programming + Min-Cut** | • Explicit diagnostic contrast between **Minimum Mean Cycle (`[HNOI2009] 最小圈` — Karp/Bellman-Ford)** and **Minimum Ratio Cut/Closure (Dinic)**.<br>• Archetype 21A network edge sign-splitting (`neg_sum` greedy severing when $a_e - \lambda b_e \le 0$). | • Complete **Submodularity Sign Law Table** classifying tractable vs. NP-hard ratio objectives ($\Delta_{u,v}(\lambda B - A) \le 0$ for $\lambda > 0$).<br>• 3-Engine comparison table (Binary Search vs. Dinkelbach vs. GGT Parametric Preflow).<br>• **Two-Scale Epsilon Hierarchy** ($\varepsilon_{\text{flow}} \ll \varepsilon_{\text{cut\_sign}} \ll \Delta_{\min}$). | None (complementary focus). Neither cohort connected ratio closure to **Lovász Extension / Submodular Function Minimization (SFM)** breakpoints. | • Unifies the Mean-Cycle vs. Ratio-Cut diagnostic table with the Submodularity Sign Law Table.<br>• Formalizes the 3-Engine Complexity & Breakpoint Theorem and the Two-Scale IEEE-754 Epsilon Hierarchy.<br>• Bridges parametric breakpoints to the **Principal Partition** of submodular functions. |
| **Iter 22 / 74: Maximum Density Subgraph (`最大密度子图`)** | • Concrete **Charikar Peeling Counterexample** ($K_{d,d}$ with pendant leaves vs. $K_{d+2}$ where greedy degree peeling destroys the denser clique first).<br>• **Dynamic Sign Splitting ($\beta_v(\lambda) \gtrless 0$)** as a zero-shift alternative to Amber's uniform $+U$ shift.<br>• Explicit proof of **Hakimi's Orientation Duality (`CF 847 J`)**. | • Rigorous two-case proof of the **$\frac{1}{N(N-1)}$ Rational Gap** ($k_1 \neq k_2$ vs. $k_1 = k_2$).<br>• Explicit counterexamples showing why Goldberg's $|V|$-only reduction fails on **$k$-uniform hypergraphs ($k \ge 3$)** and why directed subgraphs still require symmetric cut capacities. | Cohort 1 favored dynamic sign-splitting ($\beta_v(\lambda) \gtrless 0$) to avoid large $+U$ capacities; Cohort 2 favored Amber's uniform $+U$ shift because it guarantees monotone source/sink attachment under GGT Parametric Preflow. | • Presents **both** Amber's $+U$ shift and Dynamic Sign-Splitting side-by-side, proving that $+U$ is required for GGT Parametric Preflow monotonicity while Dynamic Sign-Splitting reduces total capacity in standard binary search.<br>• Combines the two-case $\frac{1}{N(N-1)}$ gap proof, Charikar peeling failure trace, Hypergraph $|V|+|E|$ mandate, and Hakimi/Nash-Williams dualities. |
| **Iter 23 / 75: Planar Graph Duality** | • Full **Discrete Coarea Formula** proof $\sum c_{uv}\max(0, h_v - h_u) = \int_0^1 \text{ Cut}(S_\lambda)\,d\lambda$ for `[NOI2010] 海拔`.<br>• Reif's primal-path Left/Right bank slicing (`P_L`, `P_R`) for interior $s$-$t$ cuts. | • Explicit **$\mathbb{Z}_2$-Parity Double Cover $G^* \times \{0,1\}$** for interior $s$-$t$ cuts and non-trivial homology.<br>• Crucial `[CSP-S 2021] 交通规划` boundary stepping-stone invariant: monochromatic boundary segments ($c_r = c_{r+1}$) must remain in $G^*$ as intermediate Dijkstra nodes! | **Apparent $90^\circ$ Rotation Conflict in `[NOI2010] 海拔`**:<br>• Cohort 1 placed $S^*$ at **Bottom-Left** and $T^*$ at **Top-Right**, deriving a **$90^\circ$ Counter-Clockwise (CCW)** rule.<br>• Cohort 2 placed $S^*$ at **Top-Right** and $T^*$ at **Bottom-Left**, deriving a **$90^\circ$ Clockwise (CW)** rule! | • **Reconciles the $90^\circ$ Rotation Rule**: Proves that swapping $S^*$ and $T^*$ reverses the direction of travel along the dual cut path, which reverses its Left and Right banks! Establishes the **Universal Left/Right Bank Orientation Law** alongside a side-by-side table of both conventions.<br>• Enforces the `[CSP-S 2021]` monochromatic boundary stepping-stone invariant. |
| **Iter 24 / 76: Max-Flow via Min-Cut DP, Greedy & SegTree** | • **Dynamic Tree Max-Flow via HLD + $(\min,+)$ Matrices (`Luogu P4719` DDP)**.<br>• **`AGC 031 E — Snuke the Phantom Thief`** 2D coordinate rank-slot transformation. | • **`CF 1919 F1` vs. `F2`** progressive compilation: why infinite pipes reduce to prefix/suffix segment tree (`F1`) while finite pipes require $2 \times 2$ $(\min,+)$ tropical matrices (`F2`). | **Coefficient Conflict in `[BZOJ 2039] 人员雇佣`**:<br>• Cohort 1 Section 5.4 wrote $s \to i$ capacity $D_i$ and $i \to j$ capacity $E_{ij}$, whereas Cohort 1 Problem 5 and Cohort 2 used $s \to i$ capacity $D_i$ and $i \to j$ capacity $2E_{ij}$ (or $2D_i$ and $2E_{ij}$). | • **Resolves `[BZOJ 2039]` exact statement algebra**: For ordered pairs $(i,j)$, hiring both gives $+E_{ij}$ and hiring $i$ without $j$ penalizes $-E_{ij}$ (twice per unordered pair): $x_i x_j - x_i(1-x_j) = x_i - 2x_i(1-x_j)$, yielding $c(s, i) = \sum_j E_{ij}$, $c(i, t) = A_i$, and directed $c(i, j) = 2E_{ij}$.<br>• Unifies `CF 724 E`, `CF 1919 F1/F2`, `Luogu P4719` HLD-DDP, `ARC 125 E`, and `AGC 031 E`. |
| **Iter 25 / 77: Stoer–Wagner & Gomory–Hu / Gusfield Cut Trees** | • Recursive **Vertex-Bucket Partitioning (`build(B)`)** vs. strict Gomory–Hu tree re-attachment.<br>• Directed 3-cycle counterexample proving why directed graphs fail posimodularity (requiring Schnorr's directed cactus). | • **Iterative 15-Line Gusfield Star-Splitting Loop** with explicit proof of the optional 4th line (`p[t] \in S` adjustment).<br>• **Cut Sensitivity / Upward Bottleneck Analysis** via residual $s$-$t$ SCCs on $T_{\text{GH}}$. | None (highly complementary). However, **both cohorts missed** randomized contraction bounds and the representation of *all* global minimum cuts! | • Combines recursive bucket partitioning and Gusfield's 15-line star-splitting.<br>• **Cohort 3 New Addition (Section 7)**: Adds **Karger–Stein Randomized Contraction** ($O(N^2 \log^3 N)$ and the $\le \binom{N}{2}$ global min-cut count proof) and the **Dinits–Karzanov–Lomonosov (DKL) Cactus of All Global Minimum Cuts (`最小割仙人掌`)**. |

---

### 1.2 Practice Problem Cross-Cohort Deduplication & Tier Audit (32 Problems)

Merging Cohort 1's 22 problems, Cohort 2's 20 problems, and Cohort 3's targeted gap-hunting yields **32 unique, deduplicated, non-template problems** organized across four progressive mastery tiers in **Section 8**:

| Master ID | Problem Name & Judge / Source | Cohort 1 ID | Cohort 2 ID | Assigned Tier | Primary Archetype & Key Pedagogical Feature |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`P01`** | `[BJWC2006] 狼抓兔子` (Luogu P4001 / BZOJ 1001) | C1-P01 | C2-P01 | **Tier 1: Stepping Stone** | Undirected $s$-$t$ planar grid cut with diagonal triangles $\to$ Dual Dijkstra ($N,M \le 1000$). |
| **`P02`** | `Hard Life` (POJ 3155 / UVa 1389 / Amber 2007) | C1-P02 | C2-P02 | **Tier 1: Stepping Stone** | Canonical unweighted Maximum Density Subgraph $\max \frac{|E(S)|}{|S|}$ via Goldberg/Amber $+U$ shift & $\frac{1}{N(N-1)}$ gap. |
| **`P03`** | `[ZJOI2011] 最小割` (Luogu P3329 / BZOJ 2229) | C1-P03 | C2-P03 | **Tier 1: Stepping Stone** | Gomory–Hu / Gusfield Cut Tree construction + $O(N^2)$ all-pairs bottleneck $\le X$ counting. |
| **`P04`** | `[CQOI2016] 不同的最小割` (Luogu P4123 / BZOJ 4519) | C1-P04 | C2-P04 | **Tier 1: Stepping Stone** | Distinct pairwise minimum cut values = distinct edge weights in $T_{\text{GH}}$ ($\le N-1$ theorem). |
| **`P05`** | `[BZOJ 2039] 人员雇佣` (Employing Personnel) | C1-P05 | C2-P06 | **Tier 1: Stepping Stone** | Degree-identity reduction $x_i x_j - x_i(1-x_j) = x_i - 2x_i(1-x_j)$ shrinking $O(N^2)$ closure to $N$ vertices. |
| **`P06`** | `Minimum Cut` (POJ 2914) | — | C2-P05 | **Tier 1: Stepping Stone** | Global undirected minimum cut via Stoer–Wagner $O(N^3)$ maximum adjacency search (`MAS`). |
| **`P07`** | `CF 1919 F1 — Wine Factory (Easy Version)` | — | C2-P07 | **Tier 1: Stepping Stone** | Dynamic max-flow with $c_i = \infty \implies$ valid cut has at most one $T \to S$ jump $\to$ prefix/suffix segment tree. |
| **`P08`** | `[NOI2006] 最大获利` (Luogu P4174) | — | C2-P12 (Var) | **Tier 1: Stepping Stone** | Contrast between $N+M$ Bipartite Closure and $N$-only Goldberg degree-identity reduction when $E(S)$ is 2-uniform. |
| **`P09`** | `[TJOI2012 / Amber 2007] Network Cost-to-Time Ratio Cut` | C1-P06 | C2-P08 | **Tier 2: Intermediate** | 0-1 Fractional Programming on $s$-$t$ cuts with negative modified weights $w_e(\lambda) \le 0$ severed greedily. |
| **`P10`** | `CF 847 J — Students Initiation` | C1-P07 | — | **Tier 2: Intermediate** | Hakimi's Orientation Duality: $\min \max_v \text{outdeg}(v) = \lceil \max_S \frac{|E(S)|}{|S|} \rceil$ via binary search / parametric flow. |
| **`P11`** | `CF 724 E — Goods Transportation` | C1-P08 | C2-P10 | **Tier 2: Intermediate** | Complete DAG $s$-$t$ cut $\sum_{i \in S, j \in T, i < j} c \implies O(N^2)$ count DP & $O(N \log N)$ slope-trick greedy. |
| **`P12`** | `CF 1082 G — Petya and Graph` | — | C2-P12 (Base) | **Tier 2: Intermediate** | Maximum weight subgraph $\sum_{e \in E(S)} w_e - \sum_{v \in S} a_v$ via $|V|$-only degree-sum transformation vs. closure. |
| **`P13`** | `Generalized Ratio Closure & Weighted MDS` (Amber 2007) | C1-P09 | C2-P12 | **Tier 2: Intermediate** | Maximizing $\frac{\sum_{e \in E(S)} w_e + \sum_{v \in S} p_v - \sum_{e \in \delta(S)} \gamma_e}{\sum_{v \in S} c_v}$ via dynamic sign-splitting vs. $+U$ shift. |
| **`P14`** | `Dynamic Tree Max-Flow via HLD & DDP` (Luogu P4719 Cut Var) | C1-P10 | — | **Tier 2: Intermediate** | Tree min-cut under point capacity updates via Heavy-Light Decomposition + $2 \times 2$ $(\min,+)$ tropical matrices. |
| **`P15`** | `AtCoder ARC 076 F — Exhausted?` | **Cohort 3 New** | **Cohort 3 New** | **Tier 2: Intermediate** | Bipartite interval complement matching ($x \le L_i$ or $x \ge R_i$) $\to$ Hall's Theorem / Min-Cut 2D prefix-suffix Segment Tree. |
| **`P16`** | `Inverse Gomory–Hu Ultrametric Realizability & Synthesis` (`CF 472 D` Cut Dual) | C1-P11 | C2-P11 | **Tier 2: Intermediate** | Verifying if an $N \times N$ matrix $M$ is an all-pairs min-cut matrix ($M_{uv} \ge \min(M_{uk}, M_{kv})$) via Maximum Spanning Tree. |
| **`P17`** | `[NOI2010] 海拔` (Altitude — Luogu P2046 / BZOJ 2007) | C1-P12 | C2-P09 | **Tier 3: Advanced** | Continuous potential $h_v \in [0,1]$ on directed grid $\to$ Coarea Formula $\{0,1\}$ reduction $\to$ Directed Dual Dijkstra. |
| **`P18`** | `CF 343 E — Pumping Stations` | C1-P13 | C2-P14 | **Tier 3: Advanced** | Traveling Salesman max-sum of adjacent $s$-$t$ min-cuts $\to$ Gomory–Hu tree bottleneck upper bound + DSU ordering. |
| **`P19`** | `CF 1919 F2 — Wine Factory (Hard Version)` | C1-P14 | C2-P15 | **Tier 3: Advanced** | Finite pipe capacity $c_i < \infty \implies$ arbitrary $S \leftrightarrow T$ alternations $\to 2 \times 2$ $(\min,+)$ matrix segment tree. |
| **`P20`** | `AtCoder ARC 125 E — Snack` | C1-P15 | C2-P16 | **Tier 3: Advanced** | Complete bipartite $K_{N,M}$ flow with $c(i,j) = B_j \implies$ for fixed $|S|=k$, optimal $T$-side threshold + two-pointer sweep. |
| **`P21`** | `Single-Edge Capacity Sensitivity on Gomory–Hu Trees` | — | C2-P13 | **Tier 3: Advanced** | Counting pairs $(u,v)$ whose min-cut strictly increases when $e$ is upgraded $\to$ residual $s$-$t$ SCC endpoints on $T_{\text{GH}}$. |
| **`P22`** | `Nash-Williams Arboricity & Rooted Forest Packing` | C1-P16 | — | **Tier 3: Advanced** | Testing $E$-decomposition into $k$ forests ($\max_{\emptyset \neq S} \frac{|E(S)|}{|S|-1} \le k$) via rooted density cut. |
| **`P23`** | `CF 1383 F — Special Edges` | C1-P17 | — | **Tier 3: Advanced** | $K \le 10$ dynamic edges on general graph $\to 2^K$ precomputed residual cuts via incremental Ford-Fulkerson + $O(2^K)$ query DP. |
| **`P24`** | `AtCoder ABC 347 G — Grid Coloring 2` | **Cohort 3 New** | **Cohort 3 New** | **Tier 3: Advanced** | Multi-valued grid potential $a_{i,j} \in \{1,\dots,5\}$ minimizing $\sum (a_u - a_v)^2 \to$ Threshold / Planar Cut & Coarea decomposition. |
| **`P25`** | `[CSP-S 2021] 交通规划` (Traffic Planning — Luogu P7916) | C1-P18 | C2-P17 | **Tier 4: Mastery** | $k \le 50$ boundary terminals with dynamic capacities $\to$ $2t$ dual boundary switching points + Circular Non-Crossing Interval DP. |
| **`P26`** | `AtCoder AGC 031 E — Snuke the Phantom Thief` | C1-P19 | — | **Tier 4: Mastery** | 2D prefix/suffix coordinate cardinality bounds ("at most $c$ jewels with $x \le a$") $\to$ sorted rank-slot bipartite MCMF / Cut. |
| **`P27`** | `Reif's Interior s-t Planar Minimum Cut` | C1-P20 | C2-P18 | **Tier 4: Mastery** | Non-boundary $s, t$ in planar graph $\to$ Primal $s$-$t$ path slicing ($P_L, P_R$) & $\mathbb{Z}_2$-Parity Double Cover $O(N \log^2 N)$ D&C. |
| **`P28`** | `All-Lambda Parametric Maximum Density Hull (GGT)` | C1-P21 | C2-P19 | **Tier 4: Mastery** | Answering $Q \le 10^5$ queries $\max_S (|E(S)| - \lambda |S|)$ via Gallo–Grigoriadis–Tarjan nested min-cuts in $O(1)$ Dinic time. |
| **`P29`** | `CF 1765 I — Infinite Chess` / `Bounded-Aspect Strip Cut` | C1-P22 | — | **Tier 4: Mastery** | $8 \times 10^8$ board shortest path / cut duality via coordinate compression of piece attack zones. |
| **`P30`** | `AtCoder AGC 029 F — Construction of a Tree` | — | C2-P20 | **Tier 4: Mastery** | Hyperedge-to-tree assembly ($|E(S)| \le |S|-1$ for $1 \notin S$) via Hall / Bipartite Max-Flow + BFS orientation. |
| **`P31`** | `Dinits–Karzanov–Lomonosov Cactus of All Global Min-Cuts` (`CF 528 E` / `ICPC Cactus Cut`) | **Cohort 3 New** | **Cohort 3 New** | **Tier 4: Mastery** | Constructing the $O(N)$-vertex Cactus Graph representing *all* $\le \binom{N}{2}$ global minimum cuts and counting/querying cuts. |
| **`P32`** | `AtCoder ABC 326 G — Unlock Achievement` / `Slope-Trick & Projective Cut Duality` | **Cohort 3 New** | **Cohort 3 New** | **Tier 4: Mastery** | Multi-level skill threshold chains + achievement rewards with special structure where Min-Cut vs. LP Duality / Slope Trick meet. |

---

## Section 2: 0-1 Fractional Programming + Minimum Cut (`分数规划最小割` & Dinkelbach's Method) — Reconciling Iter 21 & 73

### 2.1 Step 1: Non-Graph Diagnostic Signal (Recognition) & The Mean-Cycle vs. Ratio-Cut Dichotomy

#### Surface Clues in the English Statement
1. **Ratio Objective over a Combinatorial Subset**: You are asked to maximize or minimize a fraction of two linear or quadratic set functions over a subset $S \subseteq V$ (represented by binary indicators $x \in \{0, 1\}^N$):
   $$\max_{x \in \mathcal{F}} R(x) = \frac{f(x)}{g(x)} \quad \text{or} \quad \min_{x \in \mathcal{F}} R(x) = \frac{f(x)}{g(x)}, \quad g(x) > 0$$
   Examples include *"maximize total profit divided by total setup time"*, *"minimize cut cost divided by cut bandwidth"*, or *"find a subgraph maximizing edges per vertex"*.
2. **Why Naive Greedy & DP Fail**:
   - **Non-Additivity of Ratios**: Mediants do not obey linear Bellman optimality: $\frac{a_1}{b_1} < \frac{a_2}{b_2}$ does not imply $\frac{a_1 + c}{b_1 + d} < \frac{a_2 + c}{b_2 + d}$. An item with mediocre standalone ratio $a_i/b_i$ may unlock massive synergy $w_{ij}$ with ten other items, while a high-ratio item may trigger heavy boundary penalties.
   - **Exponential Dependency Graph**: Because items interact across an arbitrary graph $G = (V, E)$ via synergy rewards ($x_u x_v$) or separation penalties ($x_u(1 - x_v)$), tree/sequence DP states require $O(2^{\text{tw}(G)})$ memory.
3. **Constraint Bounds**: Typically $N \le 500 \sim 2,000$ and $M \le 5,000 \sim 20,000$, which easily supports $O(\log(\frac{1}{\varepsilon}))$ calls to Dinic's algorithm (or a single $O(N^3)$ parametric preflow run).

#### Crucial Diagnostic Dichotomy: Minimum Mean Cycle vs. Minimum Ratio Cut/Closure

A classic contest trap is confusing two fundamentally different fractional graph optimization families. Before building a flow network, check whether the feasible domain $\mathcal{F}$ consists of **walk/cycle subgraphs** (Flow / Circulation space) or **vertex partitions / closed subsets** (Potential / Cut space):

| Diagnostic Feature | Family A: Minimum / Maximum Mean Cycle (`[HNOI2009] 最小圈`) | Family B: Ratio Cut / Closure / Subgraph (`分数规划最小割`) |
| :--- | :--- | :--- |
| **Primal Object Selected** | A directed cycle $C$ (or Eulerian circulation) in $G$ | A vertex subset $S \subseteq V$ (or $s$-$t$ cut $(S, T)$) |
| **Ratio Objective** | $\min_{C} \frac{\sum_{e \in C} a_e}{\sum_{e \in C} b_e}$ | $\min_{(S,T)} \frac{\sum_{e \in \delta^+(S)} a_e}{\sum_{e \in \delta^+(S)} b_e}$ or $\max_{S} \frac{\sum_{e \in E(S)} a_e + \sum_{v \in S} p_v}{\sum_{v \in S} b_v}$ |
| **Parametric Subproblem $h(\lambda)$** | $\min_{C} \sum_{e \in C} (a_e - \lambda b_e) < 0$ | $\min_{x \in \{0,1\}^N} [f(x) - \lambda g(x)] < 0$ |
| **Core Solver Engine** | **Negative Cycle Detection** (Bellman-Ford / SPFA / Karp's $O(NM)$ algorithm) | **Minimum $s$-$t$ Cut** (Dinic / Push-Relabel / GGT Parametric Preflow) |
| **LP Duality Role** | Primal is a circulation ($B f = 0$); Dual is node potentials ($p_v - p_u \le a_e - \lambda b_e$) | Primal is node potentials $x_v \in \{0,1\}$; Dual is an $s$-$t$ flow |

---

### 2.2 Step 2: Intermediate Algebraic Representation & The Submodularity Sign Law

#### The Parametric Equivalence Theorem (Dinkelbach 1967)
Let $\mathcal{F} \subseteq \{0, 1\}^N$ be a finite non-empty set of indicator vectors with $g(x) > 0$ for all $x \in \mathcal{F}$, and let $\lambda^* = \max_{x \in \mathcal{F}} \frac{f(x)}{g(x)}$ (or $\min_{x \in \mathcal{F}} \frac{f(x)}{g(x)}$). Define the **parametric auxiliary function**:
$$h_{\max}(\lambda) = \max_{x \in \mathcal{F}} \big( f(x) - \lambda g(x) \big) = -\min_{x \in \mathcal{F}} \big( \lambda g(x) - f(x) \big)$$
(or $h_{\min}(\lambda) = \min_{x \in \mathcal{F}} (f(x) - \lambda g(x))$ for minimization).

> [!IMPORTANT]
> **Theorem 2.1 (Properties of $h(\lambda)$ — Jagannathan 1966, Dinkelbach 1967)**:
> 1. **Convexity / Concavity & Strict Monotonicity**: Because $h_{\max}(\lambda)$ is the pointwise maximum of affine lines $\ell_x(\lambda) = f(x) - \lambda g(x)$ with strictly negative slopes $-g(x) < 0$, $h_{\max}(\lambda)$ is **piecewise-linear, convex, continuous, and strictly decreasing** on $\mathbb{R}$. (Similarly, $h_{\min}(\lambda)$ is piecewise-linear, concave, and strictly decreasing.)
> 2. **Unique Root at $\lambda^*$**: For any trial parameter $\lambda \in \mathbb{R}$, Since $g(x) > 0$:
>    $$\begin{aligned}
>    h_{\max}(\lambda) > 0 &\iff \exists x \in \mathcal{F},\; \frac{f(x)}{g(x)} > \lambda \iff \lambda < \lambda^*, \\
>    h_{\max}(\lambda) = 0 &\iff \max_{x \in \mathcal{F}} \frac{f(x)}{g(x)} = \lambda \iff \lambda = \lambda^*, \\
>    h_{\max}(\lambda) < 0 &\iff \forall x \in \mathcal{F},\; \frac{f(x)}{g(x)} < \lambda \iff \lambda > \lambda^*.
>    \end{aligned}$$

#### The Submodularity Sign Law (When is $h(\lambda)$ Min-Cut Representable?)
To evaluate $h_{\max}(\lambda)$ via a minimum $s$-$t$ cut, we must minimize the pseudo-Boolean energy:
$$\Phi_\lambda(x) = \lambda g(x) - f(x), \quad x \in \{0, 1\}^N.$$
By the Kolmogorov–Zabih submodularity theorem (established in Wave 1), a quadratic pseudo-Boolean function $\Phi_\lambda(x) = C_0 + \sum_u c_u(\lambda) x_u + \sum_{u < v} c_{uv}(\lambda) x_u x_v$ is directly $s$-$t$ min-cut representable (without variable flipping) if and only if **every pairwise cross-derivative is non-positive**:
$$\Delta_{u,v}\Phi_\lambda = \Phi_\lambda(1,1) - \Phi_\lambda(1,0) - \Phi_\lambda(0,1) + \Phi_\lambda(0,0) = \lambda \Delta_{u,v} g - \Delta_{u,v} f \le 0 \quad \forall u \neq v.$$

Assume $\lambda > 0$ (which holds whenever the optimal ratio is positive, or after shifting $f(x) \gets f(x) + K g(x)$). Then $\lambda \Delta_{u,v} g - \Delta_{u,v} f \le 0$ holds unconditionally for all $\lambda > 0$ whenever:
- **Numerator $f(x)$ (to be maximized) is Supermodular** ($\Delta_{u,v} f \ge 0$): e.g., internal edge rewards $\sum_{(u,v) \in E(S)} w_{uv} = \sum w_{uv} x_u x_v$ (where $\Delta_{u,v} = +w_{uv} \ge 0$), plus modular vertex profits $\sum p_u x_u$, minus cut penalties $\sum \gamma_{uv} x_u(1-x_v)$ (where $\Delta_{u,v} = +\gamma_{uv} \ge 0$).
- **Denominator $g(x)$ (to be minimized) is Submodular** ($\Delta_{u,v} g \le 0$): e.g., modular vertex costs $\sum c_u x_u$ (where $\Delta_{u,v} = 0$) plus cut capacities $\sum d_{uv} x_u(1-x_v)$ (where $\Delta_{u,v} = -d_{uv} \le 0$).

This yields the master classification table of tractable vs. NP-hard fractional graph problems:

| Ratio Objective | $f(x)$ Curvature | $g(x)$ Curvature | Energy $\Phi_\lambda(x)$ Curvature ($\lambda > 0$) | Complexity Class |
| :--- | :---: | :---: | :---: | :--- |
| **Max Density Subgraph**: $\max_{\emptyset \neq S} \frac{|E(S)|}{|S|}$ | Supermodular ($+x_u x_v$) | Modular ($+x_u$) | **Submodular** ($\Delta_{u,v} = -1 < 0$) | **Polynomial (Min-Cut)** |
| **Max Ratio Closure**: $\max_S \frac{\text{Profit}(S) - \text{Cut}(S)}{\text{Cost}(S) + \text{Cut}'(S)}$ | Supermodular | Submodular | **Submodular** ($\Delta_{u,v} \le 0$) | **Polynomial (Min-Cut)** |
| **Min Ratio $s$-$t$ Cut**: $\min_{(S,T)} \frac{\sum_{e \in \delta^+(S)} a_e}{\sum_{e \in \delta^+(S)} b_e}$ | Submodular (Min) | Submodular (Max) | Submodular on $w_e(\lambda) \ge 0$; negative edges severed if edge-subset allowed | **Polynomial if edge-cut subset allowed**; NP-hard if strict vertex partition with $w_e(\lambda) < 0$ |
| **Sparsest Cut**: $\min_{\emptyset \subset S \subset V} \frac{|\delta(S)|}{|S| \cdot |\bar{S}|}$ | Submodular (Min) | Submodular (Max: $\sum x_u(1-x_v)$) | **Supermodular** for large $\lambda$ | **NP-Hard** ($O(\sqrt{\log N})$ SDP approx) |
| **Max Cut-to-Size**: $\max_{\emptyset \neq S} \frac{|\delta(S)|}{|S|}$ | Submodular (Max: $x_u(1-x_v)$) | Modular ($+x_u$) | **Supermodular** ($\Delta_{u,v} = +2 > 0$) | **NP-Hard** (Reduces from Max-Cut) |

---

### 2.3 Step 3: Reverse-Engineering Scratchpad — Two Canonical Archetypes & Three Solver Engines

#### Archetype 21A: Minimum Ratio $s$-$t$ Network Disconnection (`[TJOI2012] / Amber 2007`)
Suppose we must disconnect source $s$ from sink $t$ in $G = (V, E)$ by removing a cut-set $C \subseteq E$ to minimize $\frac{\sum_{e \in C} a_e}{\sum_{e \in C} b_e}$ ($b_e > 0$). For a trial $\lambda \ge 0$, each edge $e$ has modified weight $w_e(\lambda) = a_e - \lambda b_e$.
- **Why Naive Min-Cut Breaks on Negative Edges**: Standard Dinic cannot find a minimum $s$-$t$ cut when edge capacities $w_e(\lambda) < 0$.
- **Key Combinatorial Insight (Edge-Set Disconnection vs. Strict Partition)**: Because our decision variable is the **removed edge set $C \subseteq E$** (subject only to the constraint that $G \setminus C$ has no $s \to t$ path), any edge $e$ with $w_e(\lambda) \le 0$ helps reduce (or does not increase) the objective $\sum_{e \in C} w_e(\lambda)$ and helps disconnect $s$ from $t$!
- **Mechanical Compilation Rule**:
  1. Partition $E$ at trial $\lambda$ into $E^-(\lambda) = \{e \in E : w_e(\lambda) \le 0\}$ and $E^+(\lambda) = \{e \in E : w_e(\lambda) > 0\}$.
  2. **Unconditionally sever all $e \in E^-(\lambda)$** and accumulate $\text{neg\_sum}(\lambda) = \sum_{e \in E^-(\lambda)} w_e(\lambda) \le 0$.
  3. On the remaining graph $(V, E^+(\lambda))$ with strictly positive capacities $c_e = w_e(\lambda) > 0$, run Dinic to compute $\text{MaxFlow}(G^+(\lambda))$.
  4. Total optimal value is $h(\lambda) = \text{neg\_sum}(\lambda) + \text{MaxFlow}(G^+(\lambda))$. If $h(\lambda) < 0$, then $\lambda^* < \lambda$ (decrease $\lambda$); if $h(\lambda) > 0$, then $\lambda^* > \lambda$ (increase $\lambda$).

#### Archetype 21B: Maximum Ratio Project Selection / Closure
Given projects $i \in \{1, \dots, N\}$ with profit $p_i \ge 0$, cost $c_i > 0$, prerequisite DAG edges $(u, v) \in \mathcal{D}$ ($x_u = 1 \implies x_v = 1$), pairwise synergy rewards $s_{uv} \ge 0$ if both $u, v$ are chosen, and separation penalties $\gamma_{uv} \ge 0$ if $u$ is chosen without $v$, maximize:
$$R(x) = \frac{\sum_{i=1}^N p_i x_i + \sum_{(u,v) \in E_s} s_{uv} x_u x_v - \sum_{(u,v) \in E_\gamma} \gamma_{uv} x_u(1-x_v)}{\sum_{i=1}^N c_i x_i}.$$
- **Algebraic Transformation to Min-Cut**: Set $x_i = 1$ if $i \in S$ (source side) and $x_i = 0$ if $i \in T$ (sink side). Subtracting from total positive baseline $P_{\text{tot}} = \sum_i p_i + \sum_{u,v} s_{uv}$, maximizing $f(x) - \lambda g(x)$ is equivalent to minimizing the lost profit plus incurred cost:
  $$\Phi_\lambda(x, y) = \sum_{i=1}^N p_i(1 - x_i) + \sum_{i=1}^N \lambda c_i x_i + \sum_{e=(u,v) \in E_s} s_e(1 - y_e) + \sum_{e \in E_s} \infty \cdot (y_e(1-x_u) + y_e(1-x_v)) + \sum_{(u,v) \in \mathcal{D}} \infty \cdot x_u(1-x_v) + \sum_{(u,v) \in E_\gamma} \gamma_{uv} x_u(1-x_v)$$
  where auxiliary indicator $y_e \in \{0, 1\}$ represents receiving synergy $s_e$. Every term is now a standard positive cut monomial $c \cdot z_a(1 - z_b)$!

#### Comparing the Three Parametric Solver Engines

| Feature | Engine 1: Binary Search | Engine 2: Dinkelbach's Secant Method | Engine 3: GGT Parametric Preflow (1989) |
| :--- | :--- | :--- | :--- |
| **Iteration Rule** | $\lambda_{\text{mid}} = \frac{L + R}{2}$ | $\lambda_{k+1} = \frac{f(x^{(k)})}{g(x^{(k)})}$ where $x^{(k)} = \arg\min \Phi_{\lambda_k}(x)$ | Maintain valid preflow & exact heights across increasing $\lambda_1 < \lambda_2 < \dots$ |
| **Convergence Rate** | Linear (1 bit per step) | **Superlinear** (Newton-secant on convex hull; strictly decreases integer denominator $g(x^{(k)})$ when $h(\lambda)$ is non-zero) | Exact (discovers all $\le N$ breakpoints of the piecewise-linear curve $h(\lambda)$) |
| **Number of Calls** | $\lceil \log_2 \frac{\lambda_{\max} - \lambda_{\min}}{\Delta_{\min}} \rceil \approx 40\text{--}60$ | Typically **$5\text{--}12$ Dinic calls** in practice; worst-case $O(\min(N, B_{\max}))$ | Equivalent to **$1$ single Push-Relabel run** |
| **Worst-Case Time** | $O(T_{\text{flow}}(N,M) \log(\text{Range}/\varepsilon))$ | $O(K_{\text{Dink}} \cdot T_{\text{flow}}(N,M))$ | $O(N^2 M)$ or $O(N^3)$ total across **all** $\lambda$ |
| **Best Use Case** | General implementation when $T_{\text{flow}}$ is fast | **Best contest speedup** when Dinic is near TLE ($5\times$ fewer Dinic runs than binary search) | Answering $Q \le 10^5$ queries for **all** $\lambda$ simultaneously (see `P28`) |

> [!TIP]
> **Two-Scale IEEE-754 Epsilon Hierarchy (Preventing Dinic Infinite Loops)**:
> When running Dinic with `double` capacities on $G(\lambda)$, floating-point subtraction `cap[e] -= pushed` leaves microscopic residuals $\approx 10^{-16}$. If your BFS checks `cap[e] > 0`, it will traverse zero-capacity edges and loop forever! Conversely, if your Dinic threshold is larger than the binary search precision, Dinic will ignore valid augmenting paths. Always enforce a strict **three-tier separation**:
> $$\varepsilon_{\text{flow}} = 10^{-11} \;\ll\; \varepsilon_{\text{cut\_sign}} = 10^{-8} \;\ll\; \Delta_{\min} = \frac{1}{B_{\max}^2} \approx 10^{-6}.$$
> Inside Dinic's BFS and DFS, test `if (e.cap > 1e-11)` (`EPS_FLOW`). In the outer binary search, test `if (h_lambda > -1e-8)` (`EPS_CUT`). Better yet, when $g(x)$ is integer-valued and bounded by $B_{\max} \le 10^4$, **Dinkelbach's method can be run in 100% exact 64-bit integer arithmetic**: to test $\lambda = P/Q$, scale all capacities by $Q$ so $w_e = Q a_e - P b_e \in \mathbb{Z}$, eliminating `double` precision bugs entirely!

---

### 2.4 Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Concrete Toy Trace (Dinkelbach vs. Binary Search on Ratio Closure)
Consider 2 projects: Project 1 has $(p_1, c_1) = (4, 2)$, Project 2 has $(p_2, c_2) = (5, 4)$, and choosing both yields synergy $s_{12} = 6$. The non-empty subsets have ratios:
- $\{1\}: \frac{4}{2} = 2.0$; $\{2\}: \frac{5}{4} = 1.25$; $\{1, 2\}: \frac{4 + 5 + 6}{2 + 4} = \frac{15}{6} = 2.5$.
- **Dinkelbach Trace**:
  - Initialize with $x^{(0)} = (1, 0) \implies \lambda_0 = \frac{4}{2} = 2.0$.
  - At $\lambda_0 = 2.0$: Baseline $P_{\text{tot}} = 4 + 5 + 6 = 15$. Cut capacities: $s \to v_1 (4), s \to v_2 (5), s \to e_{12} (6)$; $v_1 \to t (2.0 \times 2 = 4), v_2 \to t (2.0 \times 4 = 8)$; $e_{12} \to v_1 (\infty), e_{12} \to v_2 (\infty)$.
  - Min-cut at $\lambda_0 = 2.0$: Cutting $v_1 \to t (4)$ and $v_2 \to t (8)$ costs $12$ ($S = \{s, v_1, v_2, e_{12}\}$); cutting $s \to \{v_1, v_2, e_{12}\}$ costs $15$. Thus $\text{MinCut}(2.0) = 12$, so $h(2.0) = 15 - 12 = +3 > 0$ with $x^{(1)} = (1, 1)$.
  - Secant update: $\lambda_1 = \frac{f(1,1)}{g(1,1)} = \frac{15}{6} = 2.5$.
  - At $\lambda_1 = 2.5$: $v_1 \to t$ has capacity $5$, $v_2 \to t$ has capacity $10$. Now cutting $v_1 \to t (5)$ and $v_2 \to t (10)$ costs $15$, matching $P_{\text{tot}} = 15$. Thus $h(2.5) = 15 - 15 = 0$, terminating in **2 iterations** with exact optimum $\lambda^* = 2.5$!

#### Broken Gadget Counterexample (Clamping Negative Edges to $0$ in Archetype 21A)
In Archetype 21A (Network Disconnection), suppose a solver replaces $w_e(\lambda) = a_e - \lambda b_e < 0$ with $\max(0, w_e(\lambda))$ instead of severing $e$ and adding $w_e(\lambda)$ to `neg_sum`.
- **Counterexample**: Let $G$ have two parallel $s \to t$ edges: $e_1$ with $(a_1, b_1) = (10, 1)$ and $e_2$ with $(a_2, b_2) = (2, 10)$. Clearly the single cut $\{e_1, e_2\}$ has ratio $\frac{12}{11} \approx 1.09$.
- Test $\lambda = 1.0$: $w_1(1.0) = 9 > 0$, $w_2(1.0) = 2 - 10 = -8 < 0$.
- **Correct Compilation**: Sever $e_2$ ($\text{neg\_sum} = -8$) and cut $e_1$ ($\text{MaxFlow} = 9$), giving $h(1.0) = -8 + 9 = +1 > 0 \implies \lambda^* > 1.0$ (correct!).
- **Broken Clamping ($\max(0, w_e)$)**: Clamping $w_2$ to $0$ gives $\text{MaxFlow} = 9 + 0 = 9 > 0$ even at $\lambda = 5.0$ ($w_1(5.0) = 5, w_2(5.0) = 0 \implies \text{MaxFlow} = 5 > 0$), falsely concluding $\lambda^* = 10.0$ (the ratio of $e_1$ alone, completely ignoring $e_2$)!

---

## Section 3: Maximum Density Subgraph (`最大密度子图` — Goldberg's Reduction & Amber's Treatise) — Reconciling Iter 22 & 74

### 3.1 Step 1: Non-Graph Diagnostic Signal (Recognition) & Why Greedy Peeling Fails

#### Surface Clues in the English Statement
Given an undirected graph $G = (V, E)$, find a **non-empty** vertex subset $S \subseteq V$ ($S \neq \emptyset$) that maximizes the **edge-to-vertex ratio (density)** of the induced subgraph $G[S] = (S, E(S))$:
$$\max_{\emptyset \neq S \subseteq V} D(S) = \frac{|E(S)|}{|S|} \quad \text{where} \quad E(S) = \big\{ \{u, v\} \in E : u \in S \land v \in S \big\}.$$
More generally (Amber / Hu Botao 2007 `《最小割模型在信息学竞赛中的应用》`), each edge $e \in E$ has internal reward $w_e \ge 0$ and boundary cut penalty $\gamma_e \ge 0$, and each vertex $v \in V$ has standalone profit $p_v$ and positive denominator weight $c_v > 0$:
$$\max_{\emptyset \neq S \subseteq V} D_{\text{gen}}(S) = \frac{\sum_{e \in E(S)} w_e + \sum_{v \in S} p_v - \sum_{e \in \delta(S)} \gamma_e}{\sum_{v \in S} c_v}.$$
- **Contrasting Maximum Clique (NP-Hard) vs. Maximum Density Subgraph (Polynomial)**: Finding a subgraph of size $k$ with all $\binom{k}{2}$ edges is NP-complete, and constraining $|S| \le k$ ( the *Densest $k$-Subgraph* problem) immediately destroys submodularity because the cardinality constraint cannot be priced with a single $\lambda$. However, **unconstrained** Maximum Density Subgraph is solvable in exact polynomial time via minimum cut!

#### Why Greedy Minimum-Degree Peeling (Charikar 2000) Only Gives a 2-Approximation
A natural greedy heuristic repeatedly deletes a vertex of minimum current degree in the remaining graph and records the best subgraph encountered. While Charikar (2000) proved this achieves a $\frac{1}{2}$-approximation in $O(N + M)$ time, Cohort 1 constructed the exact structural counterexample showing why greedy peeling fails to find the exact optimum:
- **Explicit Counterexample**: Let $G = G_1 \sqcup G_2$ be the disjoint union of two components ($d = 100$):
  1. $G_1$ is a clique $K_{d+2}$ on $d + 2 = 102$ vertices: every vertex in $G_1$ has degree $d + 1 = 101$, and its density is $D(G_1) = \frac{\binom{d+2}{2}}{d+2} = \frac{d+1}{2} = 50.5$.
  2. $G_2$ is a complete bipartite core $K_{d, d}$ ($2d = 200$ vertices), where each of the $2d$ core vertices also has $2$ private degree-$1$ leaves attached ($4d$ leaves), except we instead attacheach core vertex $u \in K_{d,d}$ to a small shared booster clique $B$ of size $4$ so that every vertex in $G_2$ has initial degree $\ge d + 2 = 102$, while the global density of $G_2$ is diluted or its core $K_{d,d}$ has density $\frac{d^2}{2d} = 50.0 < 50.5$. Even simpler: take $K_{d+2}$ (every vertex has degree $d+1 = 101$, density $50.5$) vs. a regular or near-regular high-girth graph $H$ on $N_H \gg d$ vertices where minimum degree in $H$ is $d + 2 = 102$ does not exist (since $\bar{d} \ge d_{\min}$), **or** attach $K_{d+2}$ to a sparse hub so that peeling Order-ties or weighted degrees peel $K_{d+2}$ first! Specifically, in **vertex-weighted or edge-weighted MDS**, let $G_1$ be a single edge with weight $100$ between two vertices of cost $1$ (density $100/2 = 50$, weighted degree $100$ each), and $G_2$ be a star $K_{1, 10}$ where the center has cost $1$ and each leaf has cost $0.01$ and edge weight $11$: each leaf has weighted degree-to-cost ratio $11 / 0.01 = 1100 > 100$, and the center has weighted degree $110 / 1 = 110 > 100$, so greedy peeling deletes $G_1$ (density $50$) before touching $G_2$ (whose density is $\frac{110}{1.1} = 100$ or if center cost is $2.5$, density $\frac{110}{2.6} = 42.3 < 50$)! Thus greedy peeling destroys the true optimal subgraph $G_1$ before $G_2$ is ever peeled.

---

### 3.2 Step 2: Intermediate Algebraic Representation — Bipartite Closure ($|V|+|E|$) vs. Goldberg's Degree Identity ($|V|$-Only)

Applying Dinkelbach's fractional transformation at trial parameter $\lambda \ge 0$, we test whether there exists a **non-empty** $S \subseteq V$ such that:
$$|E(S)| - \lambda |S| > 0 \iff \min_{\emptyset \neq S \subseteq V} \big( \lambda |S| - |E(S)| \big) < 0.$$
There are two mathematically equivalent ways to compile $\lambda |S| - |E(S)|$ into an $s$-$t$ minimum cut. Both cohorts emphasized that a master solver must know both:

#### Model I: The $|V| + |E|$ Bipartite Project-Selection Closure (Picard–Queyranne 1982)
Treat each edge $e = \{u, v\} \in E$ as a project of profit $+1$ and each vertex $v \in V$ as a prerequisite of cost $\lambda$:
$$\max_{S \subseteq V} \big( |E(S)| - \lambda |S| \big) = |E| - \min_{\substack{x \in \{0,1\}^V \\ y \in \{0,1\}^E}} \left[ \sum_{e \in E} (1 - y_e) + \sum_{v \in V} \lambda x_v + \sum_{e=(u,v) \in E} \infty \cdot \big(y_e(1 - x_u) + y_e(1 - x_v)\big) \right].$$
- **Network Size**: $|V_{\text{flow}}| = N + M + 2$ vertices, $|E_{\text{flow}}| = N + 3M$ directed edges.
- **When to Use**: When $M$ is moderate ($N, M \le 5,000$) **or** when edges are **hyperedges of size $k \ge 3$** (where Model II fails!).

#### Model II: Goldberg's (1984) & Amber's (2007) $|V|$-Only Degree-Identity Reduction
When $M \approx \binom{N}{2}$ is dense (e.g., $N = 1,000, M = 5 \times 10^5$), creating $M$ auxiliary edge vertices in Model I slows Dinic down significantly. Can we eliminate all $M$ edge nodes?
Observe the **Handshaking / Cut-Degree Identity** for any vertex partition $(S, \bar{S})$ with $\bar{S} = V \setminus S$:
$$\sum_{v \in S} \deg(v) = 2|E(S)| + |\delta(S)| \implies |E(S)| = \frac{1}{2} \sum_{v \in S} \deg(v) - \frac{1}{2} |\delta(S)|$$
where $\delta(S) = \{\{u, v\} \in E : |\{u, v\} \cap S| = 1\}$ is the undirected cut separating $S$ and $\bar{S}$.
Substitute this identity directly into $2(\lambda |S| - |E(S)|)$ (multiplying by $2$ to clear fractions):
$$2\big(\lambda |S| - |E(S)|\big) = \sum_{v \in S} \big(2\lambda - \deg(v)\big) + |\delta(S)|.$$
Notice the algebraic miracle: the quadratic reward $-2|E(S)|$ (which required $M$ auxiliary closure nodes) has been transformed into a **modular vertex weight $-\deg(v)$** plus a **standard undirected cut penalty $+|\delta(S)|$** on the original graph $G$!

---

### 3.3 Step 3: Reverse-Engineering Scratchpad — Reconciling Amber's $+U$ Shift vs. Dynamic Sign-Splitting & Exact Termination

In the degree-identity objective $\Psi_\lambda(S) = \sum_{v \in S} (2\lambda - \deg(v)) + |\delta(S)|$, the coefficient $2\lambda - \deg(v)$ can be negative when $2\lambda < \deg(v)$. How do we compile this into non-negative $s$-$t$ edge capacities? Cohort 1 and Cohort 2 used two complementary techniques—here we reconcile both:

#### Method A: Amber's Uniform Shift $+U$ (Mandatory for GGT Parametric Preflow)
For every vertex $v \in V$, rewrite $1 = x_v + (1 - x_v)$, or simply add the constant $U \cdot |V|$ by shifting each vertex's $T$-side penalty by $U \ge \max_{v \in V} \deg(v)$ (commonly $U = |E|$ or $U = 2|E|$ in the scaled model):
$$\sum_{v \in S} \big(2\lambda - \deg(v)\big) + |\delta(S)| = \sum_{v \in S} (U + 2\lambda - \deg(v)) + \sum_{v \notin S} U + |\delta(S)| - U|V|.$$
- **Graph Construction (Unscaled / Direct Form)**:
  - **Source $s \to v$**: Capacity $c(s, v) = U$ (cut if $v \notin S$, i.e., $x_v = 0$).
  - **Vertex $v \to t$**: Capacity $c(v, t) = U + 2\lambda - \deg(v) \ge 0$ (cut if $v \in S$, i.e., $x_v = 1$).
  - **Original Edges $\{u, v\} \in E$**: Undirected edge of capacity $c(u, v) = c(v, u) = 1$ (cut if $x_u \neq x_v$).
  - **Cut Value Identity**: Any $s$-$t$ cut $(S \cup \{s\}, \bar{S} \cup \{t\})$ has capacity:
    $$\text{Cap}(S) = U|V| + 2\big(\lambda |S| - |E(S)|\big).$$
    Since the trivial empty cut $S = \emptyset$ has capacity $\text{Cap}(\emptyset) = U|V|$, a non-empty subgraph with density $> \lambda$ exists if and only if $\text{MinCut}(\lambda) < U|V|$!
- **Why Method A is Required for GGT Parametric Preflow**: In Method A, $c(s, v) = U$ is **independent of $\lambda$**, and $c(v, t) = U + 2\lambda - \deg(v)$ is **monotonically non-decreasing** with $\lambda$. This monotonicity is the exact hypothesis required by the Gallo–Grigoriadis–Tarjan (1989) parametric preflow algorithm!

#### Method B: Dynamic Sign-Splitting (Zero-Shift Optimization for Binary Search / Dinkelbach)
If we use standard Binary Search or Dinkelbach's method (rebuilding $G(\lambda)$ from scratch at each step), adding a huge shift $U = 2|E|$ inflates all source/sink capacities. Instead, for any fixed $\lambda$, let $\beta_v(\lambda) = \deg(v) - 2\lambda$ be the net modular reward of placing $v \in S$:
$$\min_{S \subseteq V} \left[ |\delta(S)| - \sum_{v \in S} \beta_v(\lambda) \right] = -\sum_{\beta_v(\lambda) > 0} \beta_v(\lambda) + \min_{S \subseteq V} \left[ |\delta(S)| + \sum_{\beta_v(\lambda) > 0} \beta_v(\lambda)(1 - x_v) + \sum_{\beta_v(\lambda) \le 0} (-\beta_v(\lambda)) x_v \right].$$
- **Graph Construction (Zero-Shift Form)**:
  - If $\beta_v(\lambda) > 0$: add edge $s \to v$ with capacity $\beta_v(\lambda)$.
  - If $\beta_v(\lambda) \le 0$: add edge $v \to t$ with capacity $-\beta_v(\lambda) = 2\lambda - \deg(v) \ge 0$.
  - Original edges $\{u, v\} \in E$: undirected capacity $1$ in both directions.
  - Then $2(\lambda |S| - |E(S)|) = \text{Cap}(S) - \sum_{\beta_v(\lambda) > 0} \beta_v(\lambda) < 0 \iff \text{MinCut}(\lambda) < \sum_{\beta_v(\lambda) > 0} \beta_v(\lambda)$.

#### General Weighted Master Formula (Amber 2007)
For the general objective $D_{\text{gen}}(S) = \frac{\sum_{e \in E(S)} w_e + \sum_{v \in S} p_v - \sum_{e \in \delta(S)} \gamma_e}{\sum_{v \in S} c_v}$, define the weighted degree $\deg_w(v) = \sum_{e \ni v} w_e$. Using $2\sum_{e \in E(S)} w_e = \sum_{v \in S} \deg_w(v) - \sum_{e \in \delta(S)} w_e$, we obtain:
- **Undirected Edge $\{u, v\} \in E$**: Capacity $c(u, v) = c(v, u) = w_e + 2\gamma_e$.
- **Vertex Modular Coefficient**: $\beta_v(\lambda) = \deg_w(v) + 2p_v - 2\lambda c_v$ (handled via either Amber's $+U$ shift or Dynamic Sign-Splitting).

#### Two-Case Proof of the Exact Rational Gap $\frac{1}{N(N-1)}$ & Subgraph Extraction
> [!IMPORTANT]
> **Theorem 3.1 (Exact Rational Separation Bound for Unweighted MDS)**:
> Let $S_1, S_2 \subseteq V$ be two non-empty vertex subsets in an unweighted graph $G$ on $N = |V|$ vertices with distinct densities $D(S_1) \neq D(S_2)$, where $k_1 = |S_1| \in [1, N]$ and $k_2 = |S_2| \in [1, N]$. Then:
> $$\big| D(S_1) - D(S_2) \big| = \left| \frac{m_1}{k_1} - \frac{m_2}{k_2} \right| \ge \frac{1}{N(N - 1)}.$$
> *Proof*:
> - **Case 1 ($k_1 \neq k_2$)**: Without loss of generality, $1 \le k_1 < k_2 \le N$, so $k_1 \le N - 1$ and $k_2 \le N$. Since $m_1/k_1 \neq m_2/k_2$, the integer numerator $|m_1 k_2 - m_2 k_1| \ge 1$, giving:
>   $$\left| \frac{m_1}{k_1} - \frac{m_2}{k_2} \right| = \frac{|m_1 k_2 - m_2 k_1|}{k_1 k_2} \ge \frac{1}{(N - 1)N}.$$
> - **Case 2 ($k_1 = k_2 = k$)**: Since the denominators are equal and the densities differ, $|m_1 - m_2| \ge 1$, giving:
>   $$\left| \frac{m_1}{k} - \frac{m_2}{k} \right| \ge \frac{1}{k} \ge \frac{1}{N} > \frac{1}{N(N - 1)}. \quad \blacksquare$$
>
> **Practical Consequence for Binary Search & Reconstruction (`POJ 3155`)**:
> 1. If we only need the **numerical value** $\lambda^*$, stopping at interval width $R - L < \frac{1}{N(N-1)}$ determines the exact rational fraction $\frac{m^*}{k^*}$ (recoverable via Stern-Brocot / continued fractions).
> 2. If we must **output the actual vertex set $S^*$**, observe that at the exact optimal $\lambda = \lambda^*$, the empty set $S = \emptyset$ and the optimal subgraph $S^*$ **tie** at $h(\lambda^*) = 0$! If we run Dinic at $\lambda \ge \lambda^*$, the source-side residual reachability set gives $S = \emptyset$. Therefore, we **must reconstruct $S^*$ from the last valid lower bound $\lambda = L < \lambda^*$** (where $h(L) > 0$, strictly beating $S = \emptyset$ by at least $\frac{1}{N(N-1)}$), taking all vertices $v \in V$ reachable from $s$ in the residual graph $G_f(L)$!

#### Structural Dualities: Hakimi's Orientation Theorem & Nash-Williams Arboricity
Maximum Density Subgraph is the dual certificate for two celebrated packing/orientation theorems:
1. **Hakimi's Orientation Theorem (1965) (`CF 847 J`)**: An undirected graph $G = (V, E)$ can be oriented so that every vertex $v$ has out-degree $\text{outdeg}(v) \le d_v$ if and only if $|E(S)| \le \sum_{v \in S} d_v$ for all $S \subseteq V$. Setting $d_v = D$ for all $v$ yields:
   $$\min_{\text{orientations}} \max_{v \in V} \text{outdeg}(v) = \left\lceil \max_{\emptyset \neq S \subseteq V} \frac{|E(S)|}{|S|} \right\rceil.$$
2. **Nash-Williams Forest Packing / Arboricity Theorem (1964)**: The edge set $E$ of an undirected graph can be partitioned into at most $k$ forests if and only if:
   $$\Upsilon(G) = \max_{\substack{S \subseteq V \\ |S| \ge 2}} \left\lceil \frac{|E(S)|}{|S| - 1} \right\rceil \le k \iff \max_{\substack{S \subseteq V \\ |S| \ge 2}} \big( |E(S)| - k|S| \big) \le -k.$$

---

### 3.4 Step 4: Hand-Checkable Toy Trace & Three Broken Gadget Counterexamples

#### Hand-Checkable Toy Trace ($N=4$ "Paw Graph")
Let $G$ have $V = \{1, 2, 3, 4\}$ with triangle $\{1, 2, 3\}$ and pendant edge $\{3, 4\}$ ($M = 4$). Degrees: $\deg(1) = \deg(2) = 2$, $\deg(3) = 3$, $\deg(4) = 1$.
- True densest subgraph is the triangle $S^* = \{1, 2, 3\}$ with $|E(S^*)| = 3, |S^*| = 3 \implies D(S^*) = 1.0$ (whereas $V$ has density $4/4 = 1.0$ as well; if we test $\lambda = 0.9$, $S^*$ has $2(0.9)(3) - 2(3) = -0.6 < 0$).
- Let us trace Goldberg's $|V|$-only model with Amber's shift $U = 4$ at $\lambda = 0.8$:
  - $s \to v$ has capacity $U = 4$ for $v \in \{1,2,3,4\}$ ($U|V| = 16$).
  - $v \to t$ capacities $U + 2\lambda - \deg(v) = 5.6 - \deg(v)$: $c(1,t) = 3.6, c(2,t) = 3.6, c(3,t) = 2.6, c(4,t) = 4.6$.
  - For $S = \{1, 2, 3\}$: we cut $1 \to t (3.6), 2 \to t (3.6), 3 \to t (2.6)$, $s \to 4 (4.0)$, and graph edge $3 \to 4 (1.0)$. Total cut $= 3.6 + 3.6 + 2.6 + 4.0 + 1.0 = 14.8 < 16.0$! Indeed, $14.8 - 16.0 = -1.2 = 2(0.8 \times 3 - 3)$, confirming $D(\{1,2,3\}) > 0.8$.

#### Three Broken Gadget Counterexamples
1. **The Empty Subgraph Trap ($S = \emptyset$)**: Since $0 - \lambda \cdot 0 = 0$, the empty set $S = \emptyset$ always achieves objective $0$. If a problem asks for the densest non-empty subgraph in a graph where all vertex profits are negative ($p_v < 0$) so $\lambda^* < 0$, or if you test `MinCut(lambda) <= U|V|` at $\lambda > \lambda^*$, the solver will return $S = \emptyset$! Whenever $\lambda^*$ can be negative, force non-emptiness by either shifted ratios or testing each vertex $r \in V$ forced into $S$ (or in Nash-Williams arboricity, running $N$ rooted cuts with $c(s, r) = \infty$).
2. **The Directed Induced Subgraph Fallacy**: Suppose $G$ is a *directed* graph and we want to maximize $\frac{|E(S)|}{|S|}$ where $E(S) = \{(u,v) \in E : u \in S \land v \in S\}$. A common mistake is replacing undirected cut edges with directed edges in Goldberg's $|V|$-only model. **Why it breaks**: In the identity $\sum_{v \in S} (\text{indeg}(v) + \text{outdeg}(v)) = 2|E(S)| + |\delta^+(S)| + |\delta^-(S)|$, **both** outgoing edges $\delta^+(S)$ and incoming edges $\delta^-(S)$ cross the boundary once! Therefore, even for a directed graph, the induced subgraph $E(S)$ only cares whether *both* endpoints $u, v \in S$, which is symmetric in $u$ and $v$: you simply forget edge orientations and run the **undirected** Goldberg model!
3. **Why Goldberg's $|V|$-Only Identity Fails on $k$-Uniform Hypergraphs ($k \ge 3$)**: For a 3-uniform hypergraph $H = (V, \mathcal{E})$, a hyperedge $e = \{u, v, w\}$ can be split $2$-vs-$1$ or $1$-vs-$2$ across $(S, \bar{S})$. In $\sum_{v \in S} \deg(v) = 3|E(S)| + 2|\delta_{2,1}(S)| + 1|\delta_{1,2}(S)|$, the boundary contributions are asymmetric ($2$ vs. $1$), which cannot be represented by pairwise undirected graph edges! Thus **3-uniform hypergraph density requires Model I ($|V| + |\mathcal{E}|$ Bipartite Closure)**.

---

## Section 4: Planar Graph Duality ($s$-$t$ Planar Min-Cut $\leftrightarrow$ Dual Shortest Path) — Reconciling Iter 23 & 75

### 4.1 Step 1: Non-Graph Diagnostic Signal (Recognition)

1. **Grid or Planar Topology with Massive Bounds**: The graph is an $N \times M$ grid, a triangulated mesh (`[BJWC2006] 狼抓兔子`), or a road network embedded in the plane without edge crossings, with $V, E \le 10^6$ (e.g., $500 \times 500$ to $1000 \times 1000$ grids). At $V = 10^6$, Dinic's algorithm can be pushed to TLE by grid-snake adversarial capacities, whereas Dijkstra's algorithm on the planar dual $G^*$ runs in a guaranteed $O(V \log V)$ time!
2. **Continuous / Monotone Potential Fields (`[NOI2010] 海拔`)**: Each vertex chooses a real number $h_v \in [0, 1]$ (or integer $h_v \in \{0, \dots, K\}$) subject to boundary conditions $h_s = 0, h_t = 1$, minimizing a convex or linear edge difference cost $\sum_{(u,v) \in E} c_{uv} \max(0, h_v - h_u)$.
3. **Small Number of Boundary Terminals (`[CSP-S 2021] 交通规划`)**: A huge planar grid has $k \le 50$ sources and sinks on its outer boundary per query.

---

### 4.2 Step 2: Intermediate Algebraic & Topological Representation

#### 1. Cycle-Cut Orthogonality & $s$-$t$ Planar Duality (Whitney 1932, Hassin 1981)
Let $G = (V, E)$ be a connected plane graph with dual graph $G^* = (F, E^*)$, where each face $f \in F$ of $G$ is a dual vertex and each primal edge $e \in E$ corresponds to a dual edge $e^* \in E^*$ connecting the two faces bordering $e$. In algebraic topology over $\mathbb{R}$ (or $\mathbb{F}_2$), a minimal edge cut $\delta(S)$ in $G$ corresponds 1-to-1 with a simple cycle $C^*$ in $G^*$.

When **both $s$ and $t$ lie on the outer boundary face $f_\infty$** of $G$ ($s$-$t$ planar graph):
- Add an imaginary edge $e_\infty = (t, s)$ inside the outer face $f_\infty$. This splits $f_\infty$ into two distinct dual faces: $S^*$ (on one side of the $s$-$t$ axis) and $T^*$ (on the other side).
- Every minimal $s$-$t$ cut in $G$ forms a cycle with $e_\infty$ in $G \cup \{e_\infty\}$, which dualizes to a simple path between $S^*$ and $T^*$ in $G^*$! Thus:
  $$\text{MaxFlow}_{G}(s, t) = \text{MinCut}_{G}(s, t) = \text{ShortestPath}_{G^*}(S^*, T^*).$$

#### 2. The Coarea Formula / Threshold Layer-Cake Decomposition (`[NOI2010] 海拔`)
In `[NOI2010] 海拔`, each vertex $v$ chooses a continuous altitude $h_v \in \mathbb{R}$ with $h_{(1,1)} = 0$ and $h_{(n+1,n+1)} = 1$, minimizing:
$$\Phi(h) = \sum_{(u, v) \in E} c_{uv} \max(0, h_v - h_u).$$
Why can we restrict $h_v \in \{0, 1\}$?
- First, clamping $h_v \gets \min(1, \max(0, h_v))$ never increases $\max(0, h_v - h_u)$, so $h_v \in [0, 1]$.
- Second, for any threshold $\lambda \in (0, 1]$, define the level-set indicator $x_v(\lambda) = [h_v < \lambda] \in \{0, 1\}$. Since $h_{(1,1)} = 0 < \lambda \le 1 = h_{(n+1,n+1)}$, the set $S(\lambda) = \{v \in V : h_v < \lambda\}$ is a valid $s$-$t$ cut with $s \in S(\lambda)$ and $t \in T(\lambda) = V \setminus S(\lambda)$!
- By the **Coarea (Layer-Cake) Identity**, for any $h_u, h_v \in [0, 1]$:
  $$\max(0, h_v - h_u) = \int_0^1 \big[ h_u < \lambda \le h_v \big]\, d\lambda = \int_0^1 x_u(\lambda)\big(1 - x_v(\lambda)\big)\, d\lambda.$$
- Summing over all directed edges $(u, v) \in E$ and exchanging sum and integral by linearity:
  $$\Phi(h) = \int_0^1 \left( \sum_{(u,v) \in E} c_{uv} x_u(\lambda)\big(1 - x_v(\lambda)\big) \right) d\lambda = \int_0^1 \text{Cut}_G\big(S(\lambda), T(\lambda)\big)\, d\lambda \ge \int_0^1 C_{\min}\, d\lambda = C_{\min}$$
  where $C_{\min}$ is the minimum binary $s$-$t$ cut in $G$! Conversely, setting $h_v = 0$ for $v \in S^*$ and $h_v = 1$ for $v \in T^*$ achieves $\Phi(h) = C_{\min}$, proving that the continuous optimum equals the binary $\{0, 1\}$ $s$-$t$ minimum cut (the **Lovász Extension** of the cut function).

---

### 4.3 Step 3: Reverse-Engineering Scratchpad — Reconciling the $90^\circ$ Rotation Conventions, Multi-Terminal Cuts & Interior Cuts

#### 1. Reconciling Cohort 1 (CCW) vs. Cohort 2 (CW) in Directed Planar Duals (`[NOI2010] 海拔`)
In a **directed** planar graph, a primal directed edge $e = (u \to v)$ is paid in the $s$-$t$ cut $(S, T)$ **only if $u \in S$ and $v \in T$** (whereas $u \in T, v \in S$ pays $0$). In Cohort 1, the rule given was *"rotate primal arrows $90^\circ$ Counter-Clockwise (CCW)"*; in Cohort 2, the rule given was *"rotate primal arrows $90^\circ$ Clockwise (CW)"*. Why did the two cohorts derive opposite rotations, and why are **both 100% correct**?

> [!IMPORTANT]
> **The Universal Left/Right Bank Orientation Invariant**:
> Imagine walking in the plane along the directed dual path $P^*$ from $S^*$ to $T^*$. This path slices the primal graph $G$ into two banks: your **Left Bank** and your **Right Bank**.
> - **Convention I (Cohort 1 — Bottom-Left $S^*$ to Top-Right $T^*$)**:
>   - Primal source $s = (1, 1)$ is at the **Top-Left**; primal sink $t = (n+1, n+1)$ is at the **Bottom-Right**.
>   - Place dual source $S^*$ at the **Bottom-Left** outer face and dual sink $T^*$ at the **Top-Right** outer face.
>   - As you walk from $S^*$ (Bottom-Left) to $T^*$ (Top-Right), the primal source $s$ (Top-Left) lies on your **LEFT Bank**, and the primal sink $t$ (Bottom-Right) lies on your **RIGHT Bank**!
>   - Therefore, a primal edge $e = (u \to v)$ goes from $S$ (Left Bank) to $T$ (Right Bank) if and only if $e$ crosses the dual arrow $e^*$ from **Left to Right**, which means **rotating $e$ by $90^\circ$ Counter-Clockwise (CCW) gives $e^*$**:
>     $$\text{East } (\to) \xrightarrow{90^\circ\text{ CCW}} \text{North } (\uparrow), \quad \text{South } (\downarrow) \xrightarrow{90^\circ\text{ CCW}} \text{East } (\to), \quad \text{West } (\leftarrow) \xrightarrow{90^\circ\text{ CCW}} \text{South } (\downarrow), \quad \text{North } (\uparrow) \xrightarrow{90^\circ\text{ CCW}} \text{West } (\leftarrow).$$
> - **Convention II (Cohort 2 — Top-Right $S^*$ to Bottom-Left $T^*$)**:
>   - Keep $s = (1, 1)$ at Top-Left and $t = (n+1, n+1)$ at Bottom-Right, but swap the dual terminals: place $S^*$ at the **Top-Right** outer face and $T^*$ at the **Bottom-Left** outer face.
>   - Now, as you walk from $S^*$ (Top-Right) to $T^*$ (Bottom-Left), the primal source $s$ (Top-Left) lies on your **RIGHT Bank**, and the primal sink $t$ (Bottom-Right) lies on your **LEFT Bank**!
>   - Consequently, a primal edge $e = (u \to v)$ from $S$ (Right Bank) to $T$ (Left Bank) crosses the dual arrow from **Right to Left**, which means **rotating $e$ by $90^\circ$ Clockwise (CW) gives $e^*$**!
>   - Notice the exact isomorphism: reversing $S^* \leftrightarrow T^*$ reverses the direction of every dual edge on the path, which is identical to replacing a $90^\circ$ CCW rotation with a $90^\circ$ CW rotation!

| Convention | Primal $s, t$ | Dual $S^*, T^*$ | Which Bank of $S^* \to T^*$ Contains Primal $s$? | Exact Rotation Rule ($e \mapsto e^*$) |
| :--- | :---: | :---: | :---: | :--- |
| **Convention I (Cohort 1)** | $s$: Top-Left, $t$: Bottom-Right | $S^*$: **Bottom-Left**, $T^*$: **Top-Right** | **Left Bank** ($S$ on Left, $T$ on Right) | **$90^\circ$ Counter-Clockwise (CCW)** |
| **Convention II (Cohort 2)** | $s$: Top-Left, $t$: Bottom-Right | $S^*$: **Top-Right**, $T^*$: **Bottom-Left** | **Right Bank** ($S$ on Right, $T$ on Left) | **$90^\circ$ Clockwise (CW)** |

#### 2. Multi-Terminal Outerplanar Cuts (`[CSP-S 2021] 交通规划`)
When $k \le 50$ boundary terminals have colors $c_1, \dots, c_k \in \{0 (\text{white}/S), 1 (\text{black}/T)\}$ in clockwise circular order around the outer boundary of an $N \times M$ grid:
- Removing the $k$ terminal edges splits the outer face $f_\infty$ into $k$ boundary dual nodes $b_1^*, \dots, b_k^*$, where $b_r^*$ lies on the perimeter interval between terminal $r$ and terminal $r+1$.
- **Color-Alternating Endpoints vs. Monochromatic Stepping Stones (Cohort 2 Critical Catch)**:
  - A boundary node $b_r^*$ is a **demand endpoint (defect)** if and only if $c_r \neq c_{r+1}$. Since colors alternate around a cycle, there is an **even number $2t \le k$** of defect nodes $u_1^*, \dots, u_{2t}^*$, which must be paired up by $t$ edge-disjoint dual paths.
  - **Crucial Bug Alert**: What about the remaining $k - 2t$ boundary intervals where $c_r = c_{r+1}$ (monochromatic intervals)? They are **NOT** endpoints of the matching, **but they MUST remain as normal vertices in $G^*$** connected to adjacent perimeter grid faces and adjacent boundary intervals via the terminal edge capacities! Why? Because a shortest dual path between two defects $u_a^*$ and $u_b^*$ might exit the grid into a monochromatic boundary interval $b_r^*$, traverse a cheap terminal edge into $b_{r+1}^*$, and re-enter the grid!
- **Circular Non-Crossing Interval DP**: Since optimal shortest paths cannot cross without permitting an uncrossing of less or equal weight, the optimal pairing of $u_1^*, \dots, u_{2t}^*$ is a **non-crossing circular matching**, solved in $O(k^3)$ after $2t$ Dijkstra runs:
  $$dp[l][r] = \min\Big( D(u_l^*, u_r^*) + dp[l+1][r-1],\; \min_{\substack{m = l+1 \\ (m-l)\text{ odd}}}^{r-2} \big( dp[l][m] + dp[m+1][r] \big) \Big).$$

#### 3. Interior $s$-$t$ Cuts in General Planar Graphs (Reif 1983 & $\mathbb{Z}_2$-Parity Double Cover)
When $s$ and $t$ lie strictly in the **interior** of a planar graph $G$ (not on the same face), any minimal $s$-$t$ cut dualizes to a **simple cycle $C^*$ in $G^*$ that topologically separates $s$ from $t$**. We can find the minimum-weight separating dual cycle via two equivalent views:
- **View 1: Primal-Path Left/Right Slicing (Reif 1983)**: Find any shortest $s$-$t$ path $P = (v_0 = s, v_1, \dots, v_L = t)$ in the primal graph $G$. Any cycle $C^*$ separating $s$ from $t$ must cross $P$ an odd number of times, so it crosses at least one edge $e_i$ of $P$. Slice $G^*$ open along the dual edges $e_1^*, \dots, e_L^*$, duplicating the incident faces into a Left Bank $f_{i, L}$ and Right Bank $f_{i, R}$. Then the minimum separating cycle through $e_i^*$ is $w(e_i^*) + \text{dist}_{G^* \setminus P^*}(f_{i, L}, f_{i, R})$. By non-crossing monotonicity of shortest paths, a divide-and-conquer recursion (`solve(l, r, optL, optR)`) finds the global minimum across all $i \in [1, L]$ in $O(N \log^2 N)$ time!
- **View 2: $\mathbb{Z}_2$-Parity Double Cover $G^* \times \{0, 1\}$**: Build a 2-sheeted covering graph $G^* \times \{0, 1\}$ where every dual edge $e^*$ NOT in $P^*$ connects $(f, p) \to (g, p)$ (preserving parity $p \in \{0, 1\}$), while every dual edge $e_i^* \in P^*$ connects $(f, p) \to (g, p \oplus 1)$ (flipping parity!). Then a closed walk from $(f, 0)$ to $(f, 1)$ in $G^* \times \{0, 1\}$ has odd intersection number with $P$, hence topologically separates $s$ from $t$!

---

### 4.4 Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Hand-Checkable Toy Trace ($2 \times 2$ Directed Grid Under Both CCW and CW Conventions)
Consider a $1 \times 1$ cell ($2 \times 2$ vertices: $v_{1,1}=s$ Top-Left, $v_{1,2}$ Top-Right, $v_{2,1}$ Bottom-Left, $v_{2,2}=t$ Bottom-Right) with one interior face $f_{1,1}$:
- Directed primal capacities: Top $v_{1,1} \to v_{1,2}$ has $c = 10$, Right $v_{1,2} \to v_{2,2}$ has $c = 2$, Left $v_{1,1} \to v_{2,1}$ has $c = 3$, Bottom $v_{2,1} \to v_{2,2}$ has $c = 20$. Reverse primal edges all have capacity $100$.
- Clearly the minimum $s$-$t$ cut in $G$ is $S = \{v_{1,1}, v_{1,2}\}, T = \{v_{2,1}, v_{2,2}\}$, cutting $v_{1,1} \to v_{2,1}$ ($3$) and $v_{1,2} \to v_{2,2}$ ($2$) for total cut $3 + 2 = 5$.
- **Trace in Convention I ($S^*$ Bottom-Left, $T^*$ Top-Right, $90^\circ$ CCW)**:
  - Left edge $v_{1,1} \to v_{2,1}$ (South $\downarrow$, $c=3$) rotates $90^\circ$ CCW to East ($\to$): $S^* \to f_{1,1}$ with weight $3$.
  - Right edge $v_{1,2} \to v_{2,2}$ (South $\downarrow$, $c=2$) rotates $90^\circ$ CCW to East ($\to$): $f_{1,1} \to T^*$ with weight $2$.
  - Shortest path $S^* \to f_{1,1} \to T^*$ has length $3 + 2 = 5$!
- **Trace in Convention II ($S^*$ Top-Right, $T^*$ Bottom-Left, $90^\circ$ CW)**:
  - Right edge $v_{1,2} \to v_{2,2}$ (South $\downarrow$, $c=2$) rotates $90^\circ$ CW to West ($\leftarrow$): $S^* \to f_{1,1}$ with weight $2$.
  - Left edge $v_{1,1} \to v_{2,1}$ (South $\downarrow$, $c=3$) rotates $90^\circ$ CW to West ($\leftarrow$): $f_{1,1} \to T^*$ with weight $3$.
  - Shortest path $S^* \to f_{1,1} \to T^*$ has length $2 + 3 = 5$! Both conventions yield the exact same optimal path and weight $5$.

#### Broken Gadget Counterexamples
1. **Mixing Convention I Terminals with Convention II Rotation**: If you place $S^*$ at Bottom-Left and $T^*$ at Top-Right (Convention I) but rotate primal arrows $90^\circ$ **CW** instead of CCW, then $S^* \to f_{1,1} \to T^*$ uses the *reverse* upward edges $v_{2,1} \to v_{1,1}$ ($100$) and $v_{2,2} \to v_{1,2}$ ($100$), computing the minimum **$t$-$s$ cut** ($200$) instead of the $s$-$t$ cut ($5$)!
2. **Omitting Monochromatic Boundary Nodes in `[CSP-S 2021]`**: Suppose terminals $1, 2$ are both White ($c_1 = c_2 = 0$), terminal $2$ has capacity $1$, and the grid interior edges adjacent to terminal $2$ have capacity $1000$. If you delete $b_1^*$ (between $1$ and $2$) from $G^*$ because $c_1 = c_2$, the dual path cannot route around terminal $2$ via its capacity-$1$ terminal edge and is forced to pay $1000$ through the grid interior!

---

## Section 5: Solving Max-Flow via Min-Cut DP, Greedy & Segment Trees (`最小割转 DP 与数据结构`) — Reconciling Iter 24 & 76

### 5.1 Step 1: Non-Graph Diagnostic Signal (Recognition)

1. **Explicit Flow Graph, Impossible Scale**: The problem either explicitly asks for the maximum $s$-$t$ flow (e.g., `CF 724 E`, `CF 1919 F1/F2`, `ARC 125 E`) or compiles via standard min-cut gadgets into a flow network, **but**:
   - $N, Q \le 2 \times 10^5 \sim 5 \times 10^5$ with online point updates to capacities (`CF 1919 F2`), or
   - The graph is a **complete DAG** ($\binom{N}{2}$ edges of uniform capacity $c$ in `CF 724 E`, $N \le 10^4$) or **complete bipartite graph** ($N \times M \approx 4 \times 10^{10}$ edges in `ARC 125 E`).
2. **The Fundamental Paradigm Shift**: By the Max-Flow Min-Cut Theorem, instead of pushing flow along augmenting paths in $O(\text{Poly}(N, M))$ time, we write the exact algebraic cost of assigning every vertex $v \in V$ a binary label $x_v \in \{S, T\}$:
   $$\text{MaxFlow}(s, t) = \min_{x \in \{S, T\}^V} \text{CutCost}(x).$$
   Because the underlying graph has **low treewidth** (a linear chain or tree) or **permutation symmetry** (a complete DAG or complete bipartite graph), minimizing $\text{CutCost}(x)$ over $\{S, T\}^V$ reduces to a 1D DP, a $2 \times 2$ $(\min, +)$ matrix segment tree, or a convex slope-trick greedy!

---

### 5.2 Step 2 & Step 3: Five Canonical Compilation Paradigms

#### Paradigm 24A: Complete DAG Min-Cut DP & $O(N \log N)$ Slope-Trick Greedy (`CF 724 E — Goods Transportation`)
- **Network Structure**: Vertices $1, \dots, N$ have source edges $s \to i$ of capacity $p_i$, sink edges $i \to t$ of capacity $s_i$, and **complete forward DAG edges** $i \to j$ for all $1 \le i < j \le N$ of uniform capacity $c$.
- **Intermediate Algebraic Cut Representation**: Let $x_i \in \{S, T\}$ be the side of vertex $i$:
  - If $x_i = T$: edge $s \to i$ is cut, paying $p_i$.
  - If $x_i = S$: edge $i \to t$ is cut, paying $s_i$, **plus** every $j > i$ with $x_j = T$ cuts edge $i \to j$, paying $c$.
  - **Double-Counting Resolution**: Instead of looking forward from $i \in S$ to $j \in T$, charge the cross-edge $i \to j$ ($i < j, x_i = S, x_j = T$) to **either** the left endpoint $i$ or the right endpoint $j$:
    - *Charging to $j \in T$ ($O(N^2)$ Count DP)*: If $j \in T$ and exactly $k$ vertices before $j$ are in $S$, vertex $j$ pays $p_j + k \cdot c$:
      $$dp[i][k] = \min\big(\underbrace{dp[i-1][k] + p_i + k \cdot c}_{x_i = T},\; \underbrace{dp[i-1][k-1] + s_i}_{x_i = S}\big).$$
    - *Global Cardinality Algebraic Identity ($O(N \log N)$ Slope-Trick Greedy)*: Suppose in total $k = |S|$ vertices are placed in $S$ at indices $i_1 < i_2 < \dots < i_k$. How many pairs $(i, j)$ with $i < j$ have $i \in S$ and $j \in T$?
      Every $i \in S$ has $N - i$ vertices after it in total; subtracting the pairs $(i, j)$ where **both** $i, j \in S$ (of which there are exactly $\binom{k}{2}$!) yields:
      $$\big|\{(i, j) : i < j, i \in S, j \in T\}\big| = \sum_{i \in S} (N - i) - \binom{k}{2}.$$
      Substitute this into the total cut cost starting from the all-$T$ baseline $\sum_{i=1}^N p_i$:
      $$\text{Cut}(S) = \sum_{i=1}^N p_i - \binom{k}{2}c + \sum_{i \in S} \underbrace{\big(s_i - p_i + (N - i)c\big)}_{\text{independent weight } w_i}.$$
      Since $w_i = s_i - p_i + (N - i)c$ depends **only on $i$** (completely independent of which other vertices are in $S$!), for any fixed size $k = |S|$, the optimal subset $S$ simply picks the $k$ vertices with the **smallest values of $w_i$**! Sorting $w_1, \dots, w_N$ once in $O(N \log N)$ and sweeping $k = 0 \dots N$ solves `CF 724 E` in $O(N \log N)$ time!

#### Paradigm 24B: Linear Pipeline Dynamic Max-Flow via $(\min,+)$ Tropical Matrix Segment Tree (`CF 1919 F1` vs. `F2`)
- **Network Structure**: A pipeline of $N$ towers $1 \to 2 \to \dots \to N$, where $s \to i$ has capacity $a_i$ (water), $i \to t$ has capacity $b_i$ (wizard), and directed pipe $i \to i+1$ has capacity $c_i$. We must support $Q \le 2 \times 10^5$ point updates to $(a_i, b_i, c_i)$.
- **Local Cut Transition Algebra**:
  - Vertex $i$ pays $a_i$ if $x_i = T$, and $b_i$ if $x_i = S$.
  - Directed pipe $i \to i+1$ is cut **if and only if $x_i = S$ and $x_{i+1} = T$** (paying $c_i$). Crucially, if $x_i = T$ and $x_{i+1} = S$, the directed pipe $i \to i+1$ goes from $T$ to $S$ and **pays $0$**!
- **Why `CF 1919 F1` ($c_i = \infty$) Reduces to Prefix/Suffix Segment Tree**:
  When $c_i = \infty$, the transition $x_i = S \to x_{i+1} = T$ is forbidden! Thus the sequence $(x_1, \dots, x_N)$ must be of the form $\underbrace{T, T, \dots, T}_{1 \dots k}, \underbrace{S, S, \dots, S}_{k+1 \dots N}$ for some split point $k \in [0, N]$ (a single $T \to S$ jump), easily maintained by a standard range-add range-min segment tree over $k$.
- **Why `CF 1919 F2` ($c_i < \infty$) Requires a $2 \times 2$ $(\min,+)$ Matrix Segment Tree**:
  When $c_i < \infty$, the cut can alternate $S \leftrightarrow T$ arbitrarily many times! Encode the transition at node $i$ as a $2 \times 2$ matrix in the tropical semiring $(\mathbb{R} \cup \{\infty\}, \min, +)$, where row $u \in \{T=0, S=1\}$ is the state entering $i$ and column $v \in \{T=0, S=1\}$ is the state entering $i+1$:
  $$M_i = \begin{pmatrix} T \to T & T \to S \\ S \to T & S \to S \end{pmatrix} = \begin{pmatrix} a_i & a_i \\ b_i + c_i & b_i \end{pmatrix} \quad \text{or (state at } i \text{ directly)} \quad T_i = \begin{pmatrix} a_i & a_i \\ b_i + c_{i-1} & b_i \end{pmatrix}.$$
  A segment tree maintaining the tropical matrix product $M_{[1, N]} = M_1 \otimes M_2 \otimes \dots \otimes M_{N-1}$ answers each update in $O(\log N)$ time with $2^3 = 8$ operations per node!

#### Paradigm 24C: Dynamic Tree Min-Cut via Heavy-Light Decomposition + DDP (`Luogu P4719` Cut Dual)
When the underlying network is an arbitrary **tree** $T = (V, E)$ (instead of a path) where each node $u$ has $s \to u$ capacity $a_u$, $u \to t$ capacity $b_u$, and tree edge $(u, v)$ has capacity $c_{uv}$, under online updates to $a_u, b_u$:
- Decompose the tree via **Heavy-Light Decomposition (HLD)**. For each node $u$, let $\text{hv}(u)$ be its heavy child, and aggregate all light children $v \in \text{light}(u)$ into modified local weights:
  $$L_{u, S} = b_u + \sum_{v \in \text{light}(u)} \min\big(dp[v][S],\; dp[v][T] + c_{uv}\big), \quad L_{u, T} = a_u + \sum_{v \in \text{light}(u)} \min\big(dp[v][T],\; dp[v][S] + c_{vu}\big).$$
- Along each heavy chain, the transition from $\text{hv}(u)$ to $u$ is a $2 \times 2$ $(\min, +)$ tropical matrix multiplication:
  $$\begin{pmatrix} dp[u][S] \\ dp[u][T] \end{pmatrix} = \begin{pmatrix} L_{u, S} & L_{u, S} + c_{u, \text{hv}(u)} \\ L_{u, T} + c_{\text{hv}(u), u} & L_{u, T} \end{pmatrix} \otimes \begin{pmatrix} dp[\text{hv}(u)][S] \\ dp[\text{hv}(u)][T] \end{pmatrix}.$$
  Updating a node $u$ walks up at most $O(\log N)$ light edges to the root, updating each heavy-chain segment tree in $O(\log^2 N)$ time!

#### Paradigm 24D: Complete Bipartite Degree-Sorted Min-Cut (`AtCoder ARC 125 E — Snack`)
- **Network Structure**: $N$ snacks $i \in [1, N]$ ($s \to i$ capacity $A_i$), $M$ children $j \in [1, M]$ ($j \to t$ capacity $C_j$), and every pair $(i, j) \in [1, N] \times [1, M]$ has directed edge $i \to j$ of capacity $B_j$ (depending only on $j$).Here $N, M \le 2 \times 10^5$.
- **Algebraic Min-Cut Decomposition**: Suppose we choose $S_X \subseteq [1, N]$ of cardinality $k = |S_X|$.
  - On the left side, we cut $s \to i$ for $i \notin S_X$, paying $\sum_{i \notin S_X} A_i$. To minimize this for a fixed $k$, $S_X$ **must consist of the $k$ snacks with the largest $A_i$**!
  - On the right side, each child $j \in [1, M]$ independently chooses whether to be in $S_Y$ (cutting $j \to t$, paying $C_j$) or in $T_Y$ (cutting all $k$ edges from $S_X$ to $j$, paying $k \cdot B_j$). Thus child $j$ pays $\min(C_j, k \cdot B_j)$!
  - Total min-cut is completely decoupled into a 1D function of $k \in [0, N]$:
    $$\text{MaxFlow} = \min_{0 \le k \le N} \left[ \sum_{i=k+1}^N A_{(i)} + \sum_{j=1}^M \min\big(C_j,\; k \cdot B_j\big) \right]$$
    where $A_{(1)} \ge A_{(2)} \ge \dots \ge A_{(N)}$. Sorting $A$ descending and sorting children $j$ by threshold $\frac{C_j}{B_j}$ evaluates all $k \in [0, N]$ in $O((N + M) \log(N + M))$ time via prefix sums and two pointers!

#### Paradigm 24E: Reconciling `[BZOJ 2039] 人员雇佣` & `AGC 031 E` Coordinate Rank-Slot Duality
- **Resolving the `[BZOJ 2039]` Coefficient Convention**: In `[BZOJ 2039]`, hiring person $i$ costs $A_i$. For every ordered pair $(i, j) \in [1, N]^2$:
  - If both $i$ and $j$ are hired ($x_i = 1, x_j = 1$), they generate profit $+E_{ij}$ (so $+2E_{ij}$ per unordered pair $\{i, j\}$).
  - If $i$ is hired and $j$ is NOT hired ($x_i = 1, x_j = 0$), $i$ suffers a penalty $-E_{ij}$.
  - Combine the two terms for each ordered pair $(i, j)$ using the exact boolean identity:
    $$E_{ij} x_i x_j - E_{ij} x_i(1 - x_j) = E_{ij} x_i\big(x_j - (1 - x_j)\big) = E_{ij} x_i\big(1 - 2(1 - x_j)\big) = E_{ij} x_i - 2E_{ij} x_i(1 - x_j).$$
  - Summing over all $i, j \in [1, N]$ with $D_i = \sum_{j=1}^N E_{ij}$:
    $$\text{NetProfit}(x) = \sum_{i=1}^N D_i x_i - \sum_{i=1}^N A_i x_i - \sum_{i=1}^N \sum_{j=1}^N 2E_{ij} x_i(1 - x_j) = \sum_{i=1}^N D_i - \min_{x \in \{0,1\}^N} \left[ \sum_{i=1}^N D_i(1 - x_i) + \sum_{i=1}^N A_i x_i + \sum_{i < j} 2E_{ij}\big(x_i(1-x_j) + x_j(1-x_i)\big) \right].$$
    This shrinks an $N + \binom{N}{2}$ closure graph to just $N$ vertices (`c(s, i) = D_i`, `c(i, t) = A_i`, undirected `c(i, j) = 2E_{ij}`)!

---

### 5.3 Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Hand-Checkable Toy Trace (`CF 724 E` Slope-Trick Greedy on $N=3$)
Let $N = 3, c = 2$, with $p = [5, 1, 6]$ and $s = [2, 8, 3]$.
- All-$T$ baseline ($k = 0$): $\sum p_i = 5 + 1 + 6 = 12$.
- Compute $w_i = s_i - p_i + (N - i)c$:
  - $i = 1: w_1 = 2 - 5 + (3 - 1)\times 2 = +1$.
  - $i = 2: w_2 = 8 - 1 + (3 - 2)\times 2 = +9$.
  - $i = 3: w_3 = 3 - 6 + (3 - 3)\times 2 = -3$.
- Sort $w$: $w_{(1)} = -3$ (index $3$), $w_{(2)} = +1$ (index $1$), $w_{(3)} = +9$ (index $2$).
- Sweep $k = |S| \in \{0, 1, 2, 3\}$ with $\text{Cut}(k) = 12 - \binom{k}{2}c + \sum_{r=1}^k w_{(r)}$:
  - $k = 0: 12 - 0 + 0 = 12$ ($S = \emptyset$).
  - $k = 1: 12 - 0 + (-3) = 9$ ($S = \{3\}$).
  - $k = 2: 12 - 1(2) + (-3 + 1) = 8$ ($S = \{1, 3\}$: cuts $s \to 2 (1), 1 \to t (2), 3 \to t (3), 1 \to 2 (2) \implies 1+2+3+2 = 8$).
  - $k = 3: 12 - 3(2) + (-3 + 1 + 9) = 13$ ($S = \{1, 2, 3\}$).
- Minimum cut is **$8$** at $S = \{1, 3\}$.

#### Broken Gadget Counterexamples
1. **Symmetric Charging Bug in `CF 1919 F2`**: If a solver writes $M_i = \begin{pmatrix} a_i & a_i + c_i \\ b_i + c_i & b_i \end{pmatrix}$ (charging $c_i$ on **both** $S \to T$ and $T \to S$, treating the pipe $i \to i+1$ as undirected), then whenever $x_i = T$ and $x_{i+1} = S$, the cut falsely pays $c_i$ for a backward edge $T \to S$! In directed $s$-$t$ cuts, only $S \to T$ pays capacity $c_i$; $T \to S$ always pays $0$.
2. **Greedy Without the $(N-i)c$ Positional Term in `CF 724 E`**: If you sort vertices simply by $s_i - p_i$ instead of $w_i = s_i - p_i + (N - i)c$, you treat an early vertex $i = 1$ (which has $N - 1$ forward edges to cut!) as identical to $i = N$ (which has $0$ forward edges to cut).

---

## Section 6: Global Minimum Cut (Stoer–Wagner) & All-Pairs Min-Cut Trees (Gomory–Hu / Gusfield `最小割树`) — Reconciling Iter 25 & 77

### 6.1 Step 1: Non-Graph Diagnostic Signal (Recognition)

1. **All-Pairs Minimum Cut Queries on an Undirected Graph**: Given an undirected capacitated graph $G = (V, E, w)$ with $N \le 500 \sim 3,000$, the problem asks for a function of $\lambda(u, v) = \text{MinCut}_G(u, v)$ across **all $\binom{N}{2}$ pairs**: e.g., counting pairs with $\lambda(u, v) \le X$ (`[ZJOI2011] 最小割`), counting the number of distinct values in $\{\lambda(u, v)\}$ (`[CQOI2016] 不同的最小割`), or finding a permutation maximizing $\sum_{i=1}^{N-1} \lambda(p_i, p_{i+1})$ (`CF 343 E`).
2. **Global Minimum Cut Without Fixed Terminals**: Disconnect an undirected graph into two non-empty pieces at minimum total weight ($N \le 500$, `POJ 2914`). Running $N - 1$ Dinic calls takes $O(N \cdot N^2 M)$, whereas Stoer–Wagner takes $O(NM + N^2 \log N)$ without building any residual graph!

---

### 6.2 Step 2: Intermediate Algebraic & Polyhedral Foundations

Let $f(S) = w(\delta(S)) = \sum_{u \in S, v \notin S} w_{uv}$ be the undirected cut capacity function on $G = (V, E, w)$ with $w_{uv} \ge 0$. Every property of Stoer–Wagner and Gomory–Hu trees flows from two fundamental inequalities of $f$:

> [!IMPORTANT]
> **Theorem 6.1 (Symmetric Submodularity & Posimodularity of Undirected Cuts)**:
> For any two subsets $A, B \subseteq V$ in an undirected graph with non-negative edge weights:
> 1. **Submodularity**: $f(A) + f(B) \ge f(A \cap B) + f(A \cup B)$.
> 2. **Posimodularity**: $f(A) + f(B) \ge f(A \setminus B) + f(B \setminus A)$ (proven by applying submodularity to $A$ and $V \setminus B$, using symmetry $f(S) = f(V \setminus S)$).
>
> **Corollary 6.2 (The Ultrametric Triangle Inequality & $\le N-1$ Distinct Values Theorem)**:
> For any three distinct vertices $u, v, w \in V$:
> $$\lambda(u, w) \ge \min\big(\lambda(u, v),\; \lambda(v, w)\big).$$
> *Proof*: Let $(S, \bar{S})$ be a minimum $u$-$w$ cut with $u \in S, w \in \bar{S}$ and $f(S) = \lambda(u, w)$. The third vertex $v$ must fall in either $S$ or $\bar{S}$: if $v \in S$, then $(S, \bar{S})$ separates $v$ from $w$, so $\lambda(u, w) = f(S) \ge \lambda(v, w)$; if $v \in \bar{S}$, then $(S, \bar{S})$ separates $u$ from $v$, so $\lambda(u, w) = f(S) \ge \lambda(u, v)$. $\blacksquare$
> Consequently, among any triple $\{u, v, w\}$, the **two smallest pairwise min-cuts are always equal**, and across all $\binom{N}{2}$ pairs, $\lambda(u, v)$ can take **at most $N - 1$ distinct values**!
>
> **Lemma 6.3 (The Cut Uncrossing Lemma — Gomory & Hu 1961)**:
> Let $(S, \bar{S})$ be a minimum $s$-$t$ cut ($s \in S, t \in \bar{S}$). For any two vertices $u, v \in S$ lying on the **same side** of $(S, \bar{S})$, there exists a minimum $u$-$v$ cut $(A, \bar{A})$ that **does not cross** $(S, \bar{S})$ (i.e., either $A \subseteq S$ or $\bar{A} \subseteq S$).
> *Proof*: Let $(B, \bar{B})$ be any minimum $u$-$v$ cut with $u \in B, v \in \bar{B}$. Consider the four quadrants dividing $V$:
> - **Case 1 ($t \in \bar{B}$, on the same side of $B$ as $v$)**: By submodularity on $S$ and $B$, $f(S) + f(B) \ge f(S \cap B) + f(S \cup B)$. Notice that $S \cap B$ separates $u \in S \cap B$ from $v \notin B$, so $f(S \cap B) \ge \lambda(u, v) = f(B)$. And $S \cup B$ separates $s \in S$ from $t \notin S \cup B$, so $f(S \cup B) \ge \lambda(s, t) = f(S)$. Thus $f(S \cap B) = \lambda(u, v)$, so $A = S \cap B \subseteq S$ is an uncrossed minimum $u$-$v$ cut!
> - **Case 2 ($t \in B$, on the same side of $B$ as $u$)**: Apply posimodularity to $B$ and $\bar{S}$ (or submodularity to $S$ and $\bar{B}$): $A = S \cap \bar{B} \subseteq S$ is an uncrossed minimum $u$-$v$ cut! $\blacksquare$

---

### 6.3 Step 3: Reverse-Engineering Scratchpad — Stoer–Wagner, Recursive Gomory–Hu, and Gusfield's 15-Line Algorithm

#### 1. Stoer–Wagner Global Minimum Cut ($O(NM + N^2 \log N)$)
How do we find a global minimum cut without running max-flow?
- **Maximum Adjacency Search (`MAS`)**: Build an ordering $v_1, v_2, \dots, v_k$ of the active vertices $V'$ by starting with $A_1 = \{v_1\}$ and at each step $i$, appending the vertex $v_i \notin A_{i-1}$ that maximizes $w(A_{i-1}, v_i) = \sum_{u \in A_{i-1}} w_{u, v_i}$.
- **Theorem (Stoer & Wagner 1997)**: For the **last two vertices** $s = v_{k-1}$ and $t = v_k$ added in the `MAS` ordering, the cut $(\{v_1, \dots, v_{k-1}\}, \{v_k\})$ is a **minimum $s$-$t$ cut** in the current graph $G'$ of weight $\text{cut\_of\_phase} = w(A_{k-1}, v_k)$!
- **Contraction Step**: Update the global answer with $w(A_{k-1}, v_k)$, contract $s = v_{k-1}$ and $t = v_k$ into a single supernode (summing parallel edge weights), and repeat $N - 1$ phases!

#### 2. Gomory–Hu Tree (`最小割树`): Recursive Bucket Partitioning vs. Gusfield's 15-Line Star-Splitting
A **Gomory–Hu Tree** $T_{\text{GH}} = (V, E_T, w_T)$ is a weighted tree on the **exact original vertex set $V$** (no Steiner nodes) such that for every pair $u, v \in V$:
1. **Value Property (Flow-Equivalent Tree)**: $\lambda_G(u, v) = \min_{e \in \text{Path}_{T_{\text{GH}}}(u, v)} w_T(e)$.
2. **Partition Property (Cut-Equivalent Tree)**: Deleting the minimum-weight edge $e^*$ on $\text{Path}_{T_{\text{GH}}}(u, v)$ splits $T_{\text{GH}}$ into two connected components $(C_u, C_v)$ which form an **actual minimum $u$-$v$ cut partition in $G$**!

Both cohorts highlighted two implementation paradigms for building $T_{\text{GH}}$ in exactly $N - 1$ max-flow calls on the **original uncontracted graph $G$**:

- **Method A: Recursive Vertex-Bucket Partitioning (Cohort 1 Favorite)**:
  Maintain a active bucket $B \subseteq V$ (initially $B = V$). Pick $s = B[0], t = B[1]$, and run $\text{MaxFlow}_G(s, t)$ on the **entire original graph $G$**. Find the source-side reachable set $S \subset V$ in the residual graph $G_f$, add tree edge $(s, t)$ with weight $\lambda(s, t)$, split the bucket $B$ into $B_L = B \cap S$ and $B_R = B \setminus S$, and recurse on $B_L$ and $B_R$! (To get the strict Gomory–Hu partition property in addition to the flow-equivalent property, also re-attach any previously added tree edges incident to $B$ that lie in $\bar{S}$ from $s$ to $t$).
- **Method B: Gusfield's (1990) 15-Line Iterative Star-Splitting Loop (Cohort 2 Favorite)**:
  Initialize all vertices $2 \dots N$ as leaves attached to center $1$: `p[i] = 1` for all $i \in \{2, \dots, N\}$ (a star graph). Then loop $s$ from $2$ to $N$:
  ```cpp
  vector<int> p(N + 1, 1);
  vector<long long> w_tree(N + 1, 0);
  for (int s = 2; s <= N; ++s) {
      int t = p[s];
      w_tree[s] = dinic_on_original_G(s, t); // 1. Reset flow & run s-t MaxFlow on G
      vector<bool> in_S = get_source_side_cut(s); // 2. BFS from s on residual graph G_f
      for (int u = s + 1; u <= N; ++u)
          if (p[u] == t && in_S[u]) p[u] = s; // 3. Split future star neighbors in S to s
      if (in_S[p[t]]) { // 4. Optional 4th line: Upgrades Flow-Equivalent to true Gomory-Hu Tree!
          p[s] = p[t]; p[t] = s;
          swap(w_tree[s], w_tree[t]);
      }
  }
  ```
  Notice the extraordinary elegance of Line 4 (`if (in_S[p[t]])`): without Line 4, Gusfield's 3-line loop produces a **Flow-Equivalent Tree** (all pairwise path bottlenecks $\min_{e \in P_{uv}} w_T(e)$ are 100% exact, which suffices for `[ZJOI2011]`, `[CQOI2016]`, and `CF 343 E`); **with Line 4**, it produces a true **Cut-Equivalent Gomory–Hu Tree** where deleting each tree edge yields the exact physical vertex partition in $G$!

#### 3. Single-Edge Capacity Sensitivity Analysis on $T_{\text{GH}}$
Suppose we can increase the capacity of a **single undirected edge $e = \{x, y\} \in E$** by $\Delta > 0$. Which pairs $(u, v)$ experience a strict increase in $\lambda(u, v)$?
- A pair $(u, v)$ has its min-cut strictly increased by upgrading $e = \{x, y\}$ if and only if $e$ belongs to **every** minimum $u$-$v$ cut in $G$ (an **upward vital edge** for $(u, v)$).
- By the Picard–Queyranne residual DAG theorem (Wave 1), in any single $s$-$t$ max-flow residual graph $G_f$, an edge $e = \{x, y\}$ belongs to every minimum $s$-$t$ cut if and only if $e$ is saturated and $x \in \text{SCC}(s), y \in \text{SCC}(t)$ (or vice versa) in $G_f$.
- Translating this onto the Gomory–Hu tree $T_{\text{GH}}$: when each tree edge $e_T = (s, t)$ of weight $W = w_T(e_T)$ is computed, record the residual SCCs $C_s = \text{SCC}_{G_f}(s)$ and $C_t = \text{SCC}_{G_f}(t)$. Any pair $(u, v)$ whose unique bottleneck edge on $\text{Path}_{T_{\text{GH}}}(u, v)$ is $e_T$ has $\lambda(u, v)$ strictly increased by $e = \{x, y\}$ if and only if $u, x \in C_s$ and $v, y \in C_t$!

---

### 6.4 Step 4: Hand-Checkable Toy Trace & Three Broken Gadget Counterexamples

#### Hand-Checkable Toy Trace (Gusfield's Algorithm on $N=4$ Cycle with Chord)
Let $G$ have $V = \{1, 2, 3, 4\}$ with edges $(1,2)=3, (2,3)=4, (3,4)=5, (4,1)=2, (2,4)=1$.
- **Init**: `p = [_, 1, 1, 1, 1]`.
- **$s = 2, t = p[2] = 1$**: $\text{MinCut}_G(2, 1) = 5$ with $S = \{2, 3, 4\}, \bar{S} = \{1\}$. For $u \in \{3, 4\}$, since $p[u] == 1$ and $u \in S$, set `p[3] = 2, p[4] = 2`, `w_tree[2] = 5`.
- **$s = 3, t = p[3] = 2$**: $\text{MinCut}_G(3, 2) = 8$ with $S = \{3, 4\}, \bar{S} = \{1, 2\}$. For $u = 4$, since $p[4] == 2$ and $4 \in S$, set `p[4] = 3`, `w_tree[3] = 8`. (`p[2] = 1 \notin S`, so Line 4 does not trigger).
- **$s = 4, t = p[4] = 3$**: $\text{MinCut}_G(4, 3) = 8$ with $S = \{4\}, \bar{S} = \{1, 2, 3\}$, `w_tree[4] = 8`.
- **Resulting Gomory–Hu Tree**: Path $1 \xrightarrow{5} 2 \xrightarrow{8} 3 \xrightarrow{8} 4$. Every pair's min-cut matches the path bottleneck!

#### Three Broken Gadget Counterexamples
1. **Why Directed Graphs Do Not Have Gomory–Hu Trees (Posimodularity Failure)**: Consider the directed 3-cycle $1 \xrightarrow{1} 2 \xrightarrow{1} 3 \xrightarrow{1} 1$. For $A = \{1, 2\}$ and $B = \{2, 3\}$, $\delta^+(A) = \{(2,3)\}$ ($f(A)=1$) and $\delta^+(B) = \{(3,1)\}$ ($f(B)=1$), so $f(A) + f(B) = 2$. However, $A \setminus B = \{1\}$ has $\delta^+(\{1\}) = \{(1,2)\}$ and $B \setminus A = \{3\}$ has $\delta^+(\{3\}) = \{(3,1)\}$, and in a weighted asymmetric version ($1 \xrightarrow{10} 2 \xrightarrow{1} 3 \xrightarrow{10} 1$), $\lambda(1,2) = 1, \lambda(2,3) = 10, \lambda(3,1) = 1$, which **violates symmetry** and requires **Schnorr's (1979) Directed Cut Cactus** instead of a tree!
2. **Contracting / Deleting Subtrees During Recursive Gomory–Hu**: When recursing on bucket $B_L = B \cap S$, you **cannot** delete $\bar{S}$ from the flow graph $G$! You must either contract $\bar{S}$ into a single supernode or simply run Dinic on the **full uncontracted graph $G$** (since $N \le 500$). Deleting $\bar{S}$ destroys augmenting paths between $u, v \in B_L$ that detour through $\bar{S}$!
3. **Confusing Flow-Equivalent Trees with Cut-Equivalent Trees**: Without Line 4 of Gusfield's algorithm, the tree edge weights $\min_{e \in P_{uv}} w_T(e)$ are 100% correct, **but** deleting that edge from the tree may not give the true vertex partition $(S, \bar{S})$ in $G$! Always include Line 4 (or use Recursive Bucket Partitioning with re-attachment) if a problem depends on the physical vertex sets of the cuts.

---

## Section 7: Cohort 3 Targeted Gap-Hunting & Reconciled Master Decision Table

Auditing both Cohort 1 and Cohort 2 revealed three advanced theoretical topics that neither cohort covered. We resolve all three here before presenting the Master Compilation Decision Table.

### 7.1 Gap 1: Karger's Randomized Contraction & The $\le \binom{N}{2}$ Global Min-Cut Bound

While Stoer–Wagner finds *one* global minimum cut deterministically in $O(NM + N^2 \log N)$ time, how many **distinct global minimum cuts** can an undirected connected graph $G = (V, E, w)$ have?

> [!IMPORTANT]
> **Theorem 7.1 (Karger 1993 — The $\binom{N}{2}$ Upper Bound on Global Minimum Cuts)**:
> Any undirected connected graph $G = (V, E, w)$ on $N$ vertices has **at most $\binom{N}{2} = \frac{N(N-1)}{2}$ distinct global minimum cuts**! (This bound is tight, achieved by the unweighted cycle $C_N$, where removing any pair of edges gives a minimum cut of size $2$.)
>
> *Proof via Karger's Random Contraction Process*:
> Fix any specific global minimum cut $C^* = \delta(S^*)$ of weight $\lambda^*$. Since $\lambda^*$ is the global minimum cut, every vertex $v \in V$ has weighted degree $\deg_w(v) = w(\delta(\{v\})) \ge \lambda^*$, so the total edge weight of $G$ satisfies:
> $$W = \frac{1}{2} \sum_{v \in V} \deg_w(v) \ge \frac{N \lambda^*}{2}.$$
> Now perform $N - 2$ steps of **Random Contraction**: at each step, pick an edge $e \in E$ with probability proportional to its weight $w_e$ and contract its two endpoints (removing self-loops, keeping parallel edges).
> - In step 1 (when the graph has $N$ vertices), the probability that we accidentally contract an edge belonging to $C^*$ is $\frac{w(C^*)}{W} \le \frac{\lambda^*}{N \lambda^* / 2} = \frac{2}{N}$. Thus $C^*$ survives step 1 with probability $\ge 1 - \frac{2}{N} = \frac{N - 2}{N}$.
> - In step $k$ (when the contracted multigraph has $n = N - k + 1$ supernodes), since every cut in the contracted multigraph is also a cut in $G$, the minimum cut of the contracted multigraph is still $\ge \lambda^*$, so its total edge weight is at least $\frac{n \lambda^*}{2}$. Thus $C^*$ survives step $k$ (given survival so far) with probability $\ge 1 - \frac{2}{n} = \frac{n - 2}{n}$.
> - Telescoping the survival probability across all $N - 2$ contractions down to $2$ supernodes:
>   $$\Pr\big[C^* \text{ survives to the end}\big] \ge \frac{N - 2}{N} \cdot \frac{N - 3}{N - 1} \cdot \frac{N - 4}{N - 2} \cdots \frac{2}{4} \cdot \frac{1}{3} = \frac{2}{N(N - 1)} = \frac{1}{\binom{N}{2}}.$$
> Since the final 2-supernode graph defines a **unique** partition of $V$, the events $\mathcal{E}(C_i^*)$ that distinct global minimum cuts $C_1^*, \dots, C_M^*$ survive are **mutually exclusive** ($\sum_{i=1}^M \Pr[\mathcal{E}(C_i^*)] \le 1$). Therefore $M \cdot \frac{1}{\binom{N}{2}} \le 1 \implies M \le \binom{N}{2}$! $\blacksquare$

- **Karger–Stein Recursive Contraction (1996)**: Because the failure probability $\frac{2}{n}$ is tiny when $n$ is large and only grows near $n \to 2$, **Karger–Stein** contracts from $n$ vertices down to $\lceil n / \sqrt{2} + 1 \rceil$ vertices (where $C^*$ survives with probability $\ge \frac{1}{2}$!) and branches into **two independent recursive trials**. By $T(n) = 2T(n/\sqrt{2}) + O(n^2) = O(n^2 \log n)$, a single Karger–Stein tree succeeds with probability $\Omega(\frac{1}{\log N})$, so $O(\log^2 N)$ repetitions find all global minimum cuts in $O(N^2 \log^3 N)$ total time!

---

### 7.2 Gap 2: Dinits–Karzanov–Lomonosov (1976) Cactus Representation of All Global Minimum Cuts (`最小割仙人掌`)

A Gomory–Hu tree $T_{\text{GH}}$ stores **one** canonical minimum $s$-$t$ cut for each pair, and a Picard–Queyranne DAG stores **all** minimum $s$-$t$ cuts for a *fixed* pair $(s, t)$. What data structure simultaneously represents **all $\le \binom{N}{2}$ global minimum cuts** of an undirected graph $G$?
- **Why a Tree Fails on Crossing Global Min-Cuts**: In an unweighted cycle $C_4 = (1 - 2 - 3 - 4 - 1)$, the global min-cut is $\lambda^* = 2$, and both $A = \{1, 2\}$ and $B = \{2, 3\}$ are global minimum cuts. However, $A$ and $B$ **cross** ($A \cap B = \{2\} \neq \emptyset, A \setminus B = \{1\} \neq \emptyset, B \setminus A = \{3\} \neq \emptyset, \overline{A \cup B} = \{4\} \neq \emptyset$). No tree can represent both $(A, \bar{A})$ and $(B, \bar{B})$ as single-edge removals!
- **The Empty-Corner Crossing Property**: Suppose two global minimum cuts $(A, \bar{A})$ and $(B, \bar{B})$ cross ($f(A) = f(B) = \lambda^*$). Since all four quadrants $Q_1 = A \cap B, Q_2 = A \setminus B, Q_3 = \bar{A} \cap \bar{B}, Q_4 = B \setminus A$ are non-empty, their cuts have weight $\ge \lambda^*$. By submodularity and posimodularity:
  $$\begin{aligned}
  2\lambda^* = f(A) + f(B) &\ge f(Q_1) + f(Q_3) + 2w(Q_2, Q_4) \ge 2\lambda^* + 2w(Q_2, Q_4) \implies w(Q_2, Q_4) = 0, \\
  2\lambda^* = f(A) + f(B) &\ge f(Q_2) + f(Q_4) + 2w(Q_1, Q_3) \ge 2\lambda^* + 2w(Q_1, Q_3) \implies w(Q_1, Q_3) = 0!
  \end{aligned}$$
  Furthermore, $w(Q_1, Q_2) = w(Q_2, Q_3) = w(Q_3, Q_4) = w(Q_4, Q_1) = \frac{\lambda^*}{2}$! That is, any family of mutually crossing global minimum cuts partitions $V$ into a **circular necklace (cycle)** $Q_1 - Q_2 - \dots - Q_k - Q_1$ where adjacent beads have edge weight $\frac{\lambda^*}{2}$ and non-adjacent beads have weight $0$!
- **Theorem 7.2 (Dinits–Karzanov–Lomonosov 1976 — The Global Min-Cut Cactus $\mathcal{K}(G)$)**:
  For any undirected graph $G$ with global minimum cut $\lambda^* > 0$, there exists a unique canonical **Cactus Graph** $\mathcal{K}(G)$ (a connected graph in which every edge belongs to at most one simple cycle) with **at most $2N$ nodes** and a mapping $\phi : V \to V(\mathcal{K})$ such that:
  1. Every **tree edge (bridge)** of $\mathcal{K}(G)$ has weight $\lambda^*$, and every **cycle edge** of $\mathcal{K}(G)$ has weight $\frac{\lambda^*}{2}$.
  2. The global minimum cuts of $G$ are in **exact 1-to-1 correspondence** with the minimum cuts of $\mathcal{K}(G)$, obtained by either:
     - Removing **1 tree edge (bridge)** of $\mathcal{K}(G)$, OR
     - Removing **any 2 edges from the same simple cycle** of length $L_i$ in $\mathcal{K}(G)$!
  3. Therefore, the exact number of global minimum cuts in $G$ is:
     $$\#\text{GlobalMinCuts}(G) = b + \sum_{C_i \in \text{Cycles}(\mathcal{K})} \binom{|C_i|}{2}$$
     where $b$ is the number of bridges in $\mathcal{K}(G)$ and $|C_i|$ is the length of cycle $C_i$!

---

### 7.3 Gap 3: The Lovász Extension & Principal Partition Bridge

Unifying Section 2 (Parametric Ratio Cuts), Section 3 (Maximum Density Subgraph), and Section 4 (`[NOI2010] 海拔` Coarea Formula): for any set function $f : 2^V \to \mathbb{R}$ with $f(\emptyset) = 0$, its **Lovász Extension** $\hat{f} : \mathbb{R}^V \to \mathbb{R}$ is defined by sorting $h_{\pi_1} \ge h_{\pi_2} \ge \dots \ge h_{\pi_N}$ and integrating over level sets:
$$\hat{f}(h) = \int_0^1 f\big(\{v \in V : h_v \ge \lambda\}\big)\, d\lambda \quad \text{for } h \in [0, 1]^V.$$
- **Lovász (1983) Convexity Theorem**: A set function $f : 2^V \to \mathbb{R}$ is **submodular** if and only if its Lovász extension $\hat{f}(h)$ is a **convex** function on $\mathbb{R}^V$!
- In `[NOI2010] 海拔`, the cut function $f(S) = \sum_{(u,v) \in E} c_{uv}[u \in S, v \notin S]$ is submodular, so its Lovász extension $\hat{f}(h) = \sum_{(u,v) \in E} c_{uv} \max(0, h_u - h_v)$ is convex and achieves its minimum over $h \in [0, 1]^V$ (with $h_s = 1, h_t = 0$) at an extreme point $h \in \{0, 1\}^V$!
- In GGT Parametric Preflow (`P28`), the nested chain of minimum cuts $\emptyset = S_0 \subset S_1 \subset \dots \subset S_k = V$ across all $\lambda \in (-\infty, \infty)$ is the **Principal Partition (Narayanan / Fujishige)** of the submodular function $f(S) = |\delta(S)| - \sum_{v \in S} \deg(v)$, and the unique solution to $\min_{h \in \mathbb{R}^V} \big(\hat{f}(h) + \frac{1}{2}\sum_{v \in V} h_v^2\big)$ assigns constant value $h_v = \lambda_i$ on each ring $S_i \setminus S_{i-1}$!

---

### 7.4 Reconciled Master Recognition & Compilation Decision Table

| Problem Signature & Constraint Bounds | Underlying Algebraic / Topological Identity | Compiled Target Algorithm | Time Complexity |
| :--- | :--- | :--- | :--- |
| **Ratio of Cut/Closure to Cost**: $\max \frac{f(x)}{g(x)}$, $N \le 10^3$ | $h(\lambda) = \max_x (f(x) - \lambda g(x)) \gtrless 0$; $f$ supermodular, $g$ submodular | **Dinkelbach's Secant + Dinic** (or Binary Search with $\varepsilon_{\text{flow}} \ll \varepsilon_{\text{cut}}$) | $O(K_{\text{Dink}} \cdot T_{\text{Dinic}})$, $K_{\text{Dink}} \approx 8$ |
| **Max Density Subgraph**: $\max_{\emptyset \neq S} \frac{\sum_{e \in E(S)} w_e + \sum_{v \in S} p_v}{\sum_{v \in S} c_v}$, dense $M$ | $2\sum_{e \in E(S)} w_e = \sum_{v \in S} \deg_w(v) - w(\delta(S))$ (**$|V|$-Only Degree Identity**) | **Goldberg/Amber $|V|$-Only Min-Cut** ($+U$ shift or $\beta_v(\lambda) \gtrless 0$ split) | $O(T_{\text{Dinic}}(N, M) \log(N^2))$ or $O(N^3)$ via GGT |
| **Max Density on $k$-Uniform Hypergraphs ($k \ge 3$)** | $\sum_{e \in \mathcal{E}} w_e (1 - y_e) + \sum_{v \in V} \lambda c_v x_v + \infty \sum_{v \in e} y_e(1-x_v)$ | **Model I ($|V| + |\mathcal{E}|$ Bipartite Closure)** ($|V|$-only fails for $k \ge 3$!) | $O(T_{\text{Dinic}}(N + |\mathcal{E}|, k|\mathcal{E}|) \log(\cdot))$ |
| **Outerplanar $s$-$t$ Grid Cut / Continuous Potential**, $N \le 10^6$ | Coarea Formula $\int_0^1 \text{Cut}(S_\lambda)\,d\lambda$ + Planar Cycle-Cut Duality | **Directed Dual Dijkstra** ($90^\circ$ CCW if $S$ on Left of $S^* \to T^*$; CW if $S$ on Right) | $O(V \log V)$ |
| **Multi-Terminal Boundary Planar Cut**, $k \le 50$ per query | Even number $2t$ of color-alternating boundary defects $c_r \neq c_{r+1}$ | **$2t$ Dual Dijkstras + $O(k^3)$ Circular Non-Crossing Interval DP** | $O(k V \log V + k^3)$ per query |
| **Interior $s$-$t$ Planar Minimum Cut**, $N \le 10^5$ | Separating dual cycle = odd intersection with primal $s$-$t$ shortest path $P$ | **Reif's Primal-Path Left/Right Slicing + D&C Dijkstra** (or $\mathbb{Z}_2$ Double Cover) | $O(V \log^2 V)$ |
| **Dynamic Pipeline Flow ($N, Q \le 2 \times 10^5$)** | Directed pipe $i \to i+1$ pays $c_i$ on $S \to T$ and $0$ on $T \to S$ | **$2 \times 2$ $(\min, +)$ Tropical Matrix Segment Tree** (or HLD-DDP on trees) | $O((N + Q) \log N)$ |
| **Complete DAG / Bipartite Flow ($N \le 2 \times 10^5$)** | $\sum_{i \in S, j \in T, i < j} c = \sum_{i \in S}(N-i)c - \binom{|S|}{2}c$ | **Sort by $w_i = s_i - p_i + (N-i)c$** (`CF 724 E`) or **Threshold Sweep** (`ARC 125 E`) | $O(N \log N)$ |
| **Global Undirected Min-Cut ($N \le 500$)** | `MAS` last two vertices $s = v_{k-1}, t = v_k$ satisfy $\lambda_{G'}(s,t) = w(A_{k-1}, v_k)$ | **Stoer–Wagner Contraction** (or **DKL Cactus** for *all* global min-cuts) | $O(NM + N^2 \log N)$ |
| **All-Pairs Undirected Min-Cuts ($N \le 500$)** | Cut Uncrossing Lemma + Ultrametric $\lambda(u,w) \ge \min(\lambda(u,v), \lambda(v,w))$ | **Gusfield's 15-Line Star-Splitting** (or Recursive Bucket Gomory–Hu) | $(N - 1) \times T_{\text{Dinic}}(N, M)$ |

---

## Section 8: Reconciled Master 4-Tier Curated Problem Bank (32 Problems)

Every problem below has been cross-verified across Cohort 1 and Cohort 2, deduplicated, and compiled using the **4-Step "Zero Magic Gadgets" Standard** with 3-tier progressive hints.

---

### Tier 1: Stepping Stone (`P01` – `P08`)

---

#### Problem P01: `[BJWC2006] 狼抓兔子` (Wolves Catching Rabbits)
- **Judge / Source**: [Luogu P4001](https://www.luogu.com.cn/problem/P4001) / BZOJ 1001 (`[ZH]`)
- **Constraints**: $N, M \le 1,000$ ($V \le 10^6$ grid vertices, $E \approx 3 \times 10^6$ undirected edges: horizontal, vertical, and main-diagonal $\searrow$).
- **1. Non-Graph Diagnostic Signal**:
  We must find the minimum number of wolves (edge capacities) needed to block all paths of rabbits from the Top-Left corner $s = (1, 1)$ to the Bottom-Right corner $t = (N, M)$ on a triangulated planar grid. At $V = 10^6, E = 3 \times 10^6$, while a well-tuned Dinic sometimes squeaks through on weak test data, the problem was specifically designed as the historical Chinese OI flagship for **$s$-$t$ Planar Minimum Cut $\leftrightarrow$ Dual Shortest Path**, which guarantees $O(V \log V)$ worst-case time.
- **2. Intermediate Algebraic / Topological Representation**:
  Let $x_{i,j} \in \{0, 1\}$ with $x_{1,1} = 1, x_{N,M} = 0$. The undirected cut objective is:
  $$\min_{x \in \{0,1\}^{NM}} \sum_{\{u, v\} \in E} w_{uv} |x_u - x_v|.$$
  Since both $s = (1, 1)$ and $t = (N, M)$ lie on the outer boundary face $f_\infty$, adding the artificial boundary edge $(t, s)$ splits $f_\infty$ into $S^*$ (Bottom-Left outer region, bordering the Left column and Bottom row) and $T^*$ (Top-Right outer region, bordering the Top row and Right column). Every minimal $s$-$t$ cut in $G$ is a simple path from $S^*$ to $T^*$ in the planar dual $G^*$.
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Each unit grid square $(i, j)$ ($1 \le i < N, 1 \le j < M$) is split by its diagonal $(i, j) - (i+1, j+1)$ into **two triangular faces**:
    - Lower-left triangle $F_{\text{low}}(i, j) = \text{id}(i, j, 0)$ and Upper-right triangle $F_{\text{up}}(i, j) = \text{id}(i, j, 1)$, giving $2(N-1)(M-1)$ interior dual vertices.
  - **Dual Edges (Undirected)**:
    - Horizontal edge $(i, j) - (i, j+1)$: connects $F_{\text{low}}(i-1, j)$ and $F_{\text{up}}(i, j)$ (with $i=1$ attached to $T^*$ and $i=N$ attached to $S^*$).
    - Vertical edge $(i, j) - (i+1, j)$: connects $F_{\text{up}}(i, j-1)$ and $F_{\text{low}}(i, j)$ (with $j=1$ attached to $S^*$ and $j=M$ attached to $T^*$).
    - Diagonal edge $(i, j) - (i+1, j+1)$: connects $F_{\text{low}}(i, j)$ and $F_{\text{up}}(i, j)$ inside cell $(i, j)$.
  - **Degenerate Edge Case**: When $N = 1$ or $M = 1$, there are $0$ interior triangles! The graph is a single path of $M-1$ (or $N-1$) edges, and the minimum cut is simply $\min_e w_e$ (or $0$ if $N=M=1$).
  - **Complexity**: Dijkstra on $2(N-1)(M-1) + 2$ dual nodes and $\approx 3NM$ dual edges runs in $O(NM \log(NM))$ time.
- **4. Toy Trace & Progressive Hints**:
  - *Toy Trace ($2 \times 2$ grid)*: 2 triangular faces $F_{\text{low}}(1,1)$ and $F_{\text{up}}(1,1)$. $S^*$ connects to $F_{\text{low}}$ via Left ($w_L$) and Bottom ($w_B$); $T^*$ connects to $F_{\text{up}}$ via Top ($w_T$) and Right ($w_R$); $F_{\text{low}} \leftrightarrow F_{\text{up}}$ via Diagonal ($w_D$). Shortest $S^* \to T^*$ path has weight $\min(w_L, w_B) + \min(w_T, w_R, w_D + \dots)$, matching the 4 possible $s$-$t$ cuts!
  - *Hint 1 (Diagnostic)*: Why does every minimal $s$-$t$ cut enter each triangular cell through one edge and exit through another?
  - *Hint 2 (Algebraic)*: Add an imaginary edge from $(N, M)$ to $(1, 1)$ outside the grid. Which two outer regions of the grid perimeter become $S^*$ and $T^*$?
  - *Hint 3 (Compilation)*: Number the two triangles in cell $(i, j)$ as $2((i-1)(M-1) + (j-1)) + 1$ and $+2$, and don't forget to handle $N=1$ or $M=1$ separately!

---

#### Problem P02: `Hard Life` (Maximum Density Subgraph)
- **Judge / Source**: [POJ 3155](http://poj.org/problem?id=3155) / UVa 1389 / Amber (Hu Botao) 2007 National Team Thesis (`[EN]` / `[ZH]`)
- **Constraints**: $N \le 100$ employees, $M \le 1,000$ undirected quarrel pairs. Output the actual vertex subset $S^* \neq \emptyset$.
- **1. Non-Graph Diagnostic Signal**:
  Find a non-empty subset $S \subseteq V$ maximizing $\frac{|E(S)|}{|S|}$ and print the vertices of $S$. As shown in Section 3.1, greedy minimum-degree peeling is only a $2$-approximation, whereas $N \le 100$ is tailor-made for 0-1 Fractional Programming + Goldberg's $|V|$-Only Minimum Cut.
- **2. Intermediate Algebraic Representation**:
  At trial density $\lambda \ge 0$, using Goldberg's degree identity $2|E(S)| = \sum_{v \in S} \deg(v) - |\delta(S)|$ and Amber's uniform shift $U = M$:
  $$\text{MinCut}(\lambda) = \min_{S \subseteq V} \left[ U|V| + \sum_{v \in S} \big(2\lambda - \deg(v)\big) + |\delta(S)| \right] < U|V| \iff \exists S \neq \emptyset,\; \frac{|E(S)|}{|S|} > \lambda.$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - **Edges**: For each $v \in V$, add $s \to v$ with capacity $U = M$, and $v \to t$ with capacity $U + 2\lambda - \deg(v)$. For each $\{u, v\} \in E$, add undirected edge $u \leftrightarrow v$ with capacity $1$.
  - **Binary Search Termination**: By Theorem 3.1, distinct densities differ by at least $\frac{1}{N(N-1)} \ge \frac{1}{9900}$. Binary search on $\lambda \in [0, M]$ until $R - L < \frac{1}{N(N-1)} \approx 10^{-5}$ ($\approx 35$ iterations), using `EPS_FLOW = 1e-11` inside Dinic and `EPS_CUT = 1e-8` for `U * N - max_flow > 1e-8`.
  - **Subgraph Extraction Trap**: Reconstruct $S^*$ by running one final Dinic at $\lambda = L$ (strictly below $\lambda^*$, so $S^* \neq \emptyset$ strictly beats $\emptyset$) and collecting all vertices reachable from $s$ in $G_f(L)$! (If $M = 0$, output `{1}`).
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Apply Dinkelbach's paradigm: for a fixed guess $\lambda$, you want to maximize $|E(S)| - \lambda |S|$.
  - *Hint 2 (Algebraic)*: Replace $2|E(S)|$ with $\sum_{v \in S} \deg(v) - |\delta(S)|$ so you don't need $M$ edge nodes.
  - *Hint 3 (Compilation)*: Why does reconstructing the cut at $\lambda = R \ge \lambda^*$ always return $S = \emptyset$? Always reconstruct at $\lambda = L$!

---

#### Problem P03: `[ZJOI2011] 最小割` (All-Pairs Min-Cut Threshold Counting)
- **Judge / Source**: [Luogu P3329](https://www.luogu.com.cn/problem/P3329) / BZOJ 2229 (`[ZH]`)
- **Constraints**: $T \le 10$ testcases, $N \le 150, M \le 3,000$, $Q \le 30$ queries per testcase asking for the number of unordered pairs $\{u, v\}$ with $\text{MinCut}_G(u, v) \le X$.
- **1. Non-Graph Diagnostic Signal**:
  Computing $\binom{150}{2} = 11,175$ max-flows per testcase TLEs by $100\times$. Because the graph is **undirected**, all $\binom{N}{2}$ pairwise minimum cuts are encoded as path bottlenecks on a single $N$-vertex **Gomory–Hu / Gusfield Cut Tree** built in $N - 1 = 149$ Dinic calls!
- **2. Intermediate Algebraic Representation**:
  On the flow-equivalent tree $T_{\text{GH}} = (V, E_T, w_T)$:
  $$\lambda_G(u, v) = \min_{e \in \text{Path}_{T_{\text{GH}}}(u, v)} w_T(e) \quad \forall u, v \in V.$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Run Gusfield's 15-line star-splitting loop (Section 6.3) using $N - 1$ Dinic runs on the original graph $G$ (resetting flow to $0$ before each run).
  - Run $N$ simple tree DFS/BFS traversals on $T_{\text{GH}}$ in $O(N^2)$ time to populate the $N \times N$ table $\lambda(u, v)$ (or sort the $N-1$ tree edges descending and use DSU to count connected pairs for offline queries in $O(N \log N)$).
  - **Complexity**: $O(N \cdot T_{\text{Dinic}}(N, M) + N^2)$ per testcase.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: How many max-flow runs are actually needed to find all $\binom{N}{2}$ pairwise minimum cuts in an undirected graph?
  - *Hint 2 (Algebraic)*: By the Cut Uncrossing Lemma, pairwise cuts never need to cross.
  - *Hint 3 (Compilation)*: Implement Gusfield's star-splitting loop: initialize `p[2..N] = 1`, and for $s = 2 \dots N$, run Dinic between $s$ and $t = p[s]$ and update `p[u] = s` for $u > s$ with `p[u] == t` and $u \in S$.

---

#### Problem P04: `[CQOI2016] 不同的最小割` (Distinct Pairwise Minimum Cuts)
- **Judge / Source**: [Luogu P4123](https://www.luogu.com.cn/problem/P4123) / BZOJ 4519 (`[ZH]`)
- **Constraints**: $N \le 850, M \le 8,500$. Output the number of distinct values among $\{\lambda_G(u, v) : 1 \le u < v \le N\}$.
- **1. Non-Graph Diagnostic Signal**:
  At $N = 850$, $\binom{N}{2} \approx 3.6 \times 10^5$, yet the problem asks how many distinct values $\lambda(u, v)$ can take. By Corollary 6.2 (the Ultrametric Triangle Inequality), $\lambda(u, v)$ can take **at most $N - 1$ distinct values**, which are precisely the distinct edge weights of the Gomory–Hu tree $T_{\text{GH}}$!
- **2. Intermediate Algebraic Representation**:
  $$\big\{ \lambda_G(u, v) : 1 \le u < v \le N \big\} = \big\{ w_T(e) : e \in E(T_{\text{GH}}) \big\}.$$
  Why? Because every tree edge $e = (s, t) \in E(T_{\text{GH}})$ has $w_T(e) = \lambda_G(s, t)$, so its weight is achieved by $(s, t)$; conversely, every pair's bottleneck equals the weight of some edge on its tree path!
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Run Gusfield's algorithm in $N - 1$ Dinic calls, collect the $N - 1$ values `w_tree[2..N]` into a `std::set<long long>`, and output `set.size()`.
  - **Complexity**: $(N - 1) \times T_{\text{Dinic}}(N, M)$, running in $< 0.3\text{s}$ for $N = 850$.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: For any 3 vertices $u, v, w$, prove that the two smallest values among $\lambda(u,v), \lambda(v,w), \lambda(u,w)$ must be equal.
  - *Hint 2 (Algebraic)*: What does the ultrametric inequality imply about the set of all pairwise path bottlenecks in a tree?
  - *Hint 3 (Compilation)*: You don't even need to build the tree adjacency list—just insert the $N-1$ max-flow answers from Gusfield's loop into a hash set!

---

#### Problem P05: `[BZOJ 2039] 人员雇佣` (Employing Personnel)
- **Judge / Source**: BZOJ 2039 (`[ZH]`)
- **Constraints**: $N \le 1,000$ employees, dense $N \times N$ symmetric matrix $E_{ij} \ge 0$ ($10^6$ entries), hiring costs $A_i \ge 0$.
- **1. Non-Graph Diagnostic Signal**:
  Hiring $i$ costs $A_i$. For each ordered pair $(i, j)$, if both $i$ and $j$ are hired, the company gains $+E_{ij}$; if $i$ is hired and $j$ is NOT hired, the company loses $-E_{ij}$. A naive closure graph creates $N + \binom{N}{2} \approx 5 \times 10^5$ vertices, causing TLE/MLE. We must use the **Degree-Sum Identity** (Section 5.2, Paradigm 24E) to eliminate all $\binom{N}{2}$ pair nodes!
- **2. Intermediate Algebraic Representation**:
  Let $x_i \in \{0, 1\}$ indicate hiring $i$ ($x_i = 1 \iff i \in S$). For each ordered pair $(i, j)$, using $x_i x_j - x_i(1 - x_j) = x_i - 2x_i(1 - x_j)$ and setting $D_i = \sum_{j=1}^N E_{ij}$:
  $$\max_{x \in \{0,1\}^N} \left[ \sum_{i=1}^N D_i x_i - \sum_{i=1}^N A_i x_i - \sum_{i=1}^N \sum_{j=1}^N 2E_{ij} x_i(1 - x_j) \right] = \sum_{i=1}^N D_i - \min_{x \in \{0,1\}^N} \left[ \sum_{i=1}^N D_i(1 - x_i) + \sum_{i=1}^N A_i x_i + \sum_{i=1}^N \sum_{j=1}^N 2E_{ij} x_i(1 - x_j) \right].$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - **Graph ($N + 2$ vertices)**:
    - Source $s \to i$ with capacity $D_i = \sum_{j=1}^N E_{ij}$ (cut if $x_i = 0$).
    - Sink $i \to t$ with capacity $A_i$ (cut if $x_i = 1$).
    - For every $i \neq j$, directed edge $i \to j$ with capacity $2E_{ij}$ (cut if $x_i = 1, x_j = 0$).
  - Answer is $\sum_{i=1}^N D_i - \text{MaxFlow}(s, t)$.
  - **Complexity**: Dinic on $N = 1,000$ vertices and $N^2 = 10^6$ edges runs in $< 0.2\text{s}$.
- **4. Toy Trace & Progressive Hints**:
  - *Toy Trace ($N=2$)*: $A = [5, 5]$, $E_{12} = E_{21} = 4$ ($D_1 = D_2 = 4$). Baseline $\sum D_i = 8$. Cuts: $S = \emptyset \implies \text{cut } s \to 1 (4), s \to 2 (4) = 8 \implies \text{Profit } 0$; $S = \{1, 2\} \implies \text{cut } 1 \to t (5), 2 \to t (5) = 10 \implies \text{Profit } 8 - 10 = -2$; $S = \{1\} \implies \text{cut } 1 \to t (5), s \to 2 (4), 1 \to 2 (8) = 17 \implies \text{Profit } 8 - 17 = -9$. Max profit is $0$ ($S = \emptyset$).
  - *Hint 1 (Diagnostic)*: Why can't you create a vertex for every pair $(i, j)$ when $N = 1000$?
  - *Hint 2 (Algebraic)*: Simplify $E_{ij} x_i x_j - E_{ij} x_i(1 - x_j)$ using $x_j = 1 - (1 - x_j)$.
  - *Hint 3 (Compilation)*: Notice that the quadratic term $x_i x_j$ completely disappears, leaving only linear $D_i x_i$ and pairwise cut terms $2E_{ij} x_i(1 - x_j)$!

---

#### Problem P06: `Minimum Cut` (Global Undirected Minimum Cut)
- **Judge / Source**: [POJ 2914](http://poj.org/problem?id=2914) (`[EN]`)
- **Constraints**: $N \le 500$ vertices, $M$ undirected weighted edges (with possible parallel edges). Find the global minimum cut separating $G$ into two non-empty components.
- **1. Non-Graph Diagnostic Signal**:
  We need $\min_{\emptyset \subset S \subset V} w(\delta(S))$ with no fixed $s$ or $t$. Running $N - 1$ Dinic calls is too slow at $N = 500$ on POJ's tight time limit; **Stoer–Wagner's Algorithm** finds the global minimum cut in $O(N^3)$ using simple array sweeps (`MAS`) and vertex contractions!
- **2. Intermediate Algebraic Representation**:
  In phase $r$, let $v_1, \dots, v_k$ be the Maximum Adjacency Search (`MAS`) ordering where $v_i = \arg\max_{u \notin A_{i-1}} w(A_{i-1}, u)$. By the Stoer–Wagner Theorem ( proven via submodularity uncrossing on active vertices), $\lambda_{G'}(v_{k-1}, v_k) = w(A_{k-1}, v_k)$.
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Store the graph as an $N \times N$ adjacency matrix `g[u][v]` (summing parallel edges on input).
  - Maintain `alive[1..N] = true`. Repeat $N - 1$ phases:
    - Run `MAS` in $O(N^2)$ to find the last two vertices $s = v_{k-1}$ and $t = v_k$, and update `ans = min(ans, wag[t])`.
    - Contract $t$ into $s$: set `alive[t] = false`, and for all `u` with `alive[u]`, do `g[s][u] += g[t][u]; g[u][s] += g[u][t]`.
  - **Complexity**: $O(N^3)$ time with tiny constant factor ($\approx 2 \times 10^7$ additions), $O(N^2)$ space.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Do you need to know the global minimum cut between *every* pair, or can you just find one pair $(s, t)$, record their min-cut, and merge $(s, t)$?
  - *Hint 2 (Algebraic)*: Why does Maximum Adjacency Search (`MAS`), which looks identical to Prim's MST algorithm except summing weights to $A_{i-1}$, guarantee that the last two vertices have min-cut equal to $w(A_{k-1}, v_k)$?
  - *Hint 3 (Compilation)*: Be sure to sum parallel edges (`g[u][v] += w`) both during input reading and during vertex contraction!

---

#### Problem P07: `CF 1919 F1 — Wine Factory (Easy Version)`
- **Judge / Source**: [Codeforces 1919F1](https://codeforces.com/problemset/problem/1919/F1) (`[EN]`)
- **Constraints**: $N, Q \le 5 \times 10^5$, $a_i, b_i \le 10^9$, and **pipe capacities $c_i = 10^{18}$ ($\infty$)** for $1 \le i \le N-1$. Point updates to $(a_i, b_i, c_i)$ (where $c_i$ remains $\ge 10^{18}$).
- **1. Non-Graph Diagnostic Signal**:
  A linear pipeline max-flow problem with $N, Q = 5 \times 10^5$. Because $c_i = \infty$, we cannot cut any forward pipe $i \to i+1$!
- **2. Intermediate Algebraic Representation**:
  In an $s$-$t$ cut $x \in \{S, T\}^N$, cutting pipe $i \to i+1$ costs $c_i = \infty$ whenever $x_i = S$ and $x_{i+1} = T$. Therefore, $(x_1, \dots, x_N)$ **cannot contain any $S \to T$ transition**! The only valid finite-cost cuts have the prefix-suffix form:
  $$x_1 = \dots = x_k = T, \quad x_{k+1} = \dots = x_N = S \quad \text{for some } k \in \{0, 1, \dots, N\}.$$
  The cut cost for split index $k$ is:
  $$\text{Cut}(k) = \sum_{i=1}^k a_i + \sum_{i=k+1}^N b_i = \sum_{i=1}^N b_i + \sum_{i=1}^k (a_i - b_i).$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Maintain $\sum_{i=1}^N b_i$ globally and maintain the prefix sums $P_k = \sum_{i=1}^k (a_i - b_i)$ for $k \in [0, N]$ in a Segment Tree supporting **Range Add** and **Range Minimum Query** (or maintain node tuples `(sum_a, sum_b, min_cut)` where `min_cut = min(L.min_cut + R.sum_b, L.sum_a + R.min_cut)`!).
  - **Complexity**: $O((N + Q) \log N)$ time, $O(N)$ space.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Write the flow network: $s \to i$ ($a_i$), $i \to t$ ($b_i$), and $i \to i+1$ ($\infty$). Which transition ($S \to T$ or $T \to S$) cuts the $\infty$-capacity edge?
  - *Hint 2 (Algebraic)*: Since $S \to T$ costs $\infty$, all $T$'s must come before all $S$'s!
  - *Hint 3 (Compilation)*: Each segment tree node only needs to store `sum_a`, `sum_b`, and `ans = min(L.ans + R.sum_b, L.sum_a + R.ans)`—which immediately prepares you for the $2 \times 2$ matrix in `F2`!

---

#### Problem P08: `[NOI2006] 最大获利` (Maximum Profit — Closure vs. Degree-Identity Comparison)
- **Judge / Source**: [Luogu P4174](https://www.luogu.com.cn/problem/P4174) (`[ZH]`)
- **Constraints**: $N \le 5,000$ base stations (cost $c_v$), $M \le 50,000$ user pairs $e = \{u, v\}$ (profit $w_e$ if both $u$ and $v$ are built).
- **1. Non-Graph Diagnostic Signal**:
  Maximize $\sum_{e=\{u,v\} \in E(S)} w_e - \sum_{v \in S} c_v$. While the textbook solution uses Model I ($N + M = 55,000$ vertex Bipartite Closure), every demand involves **exactly 2 stations** (a 2-uniform graph)! Thus we can apply Goldberg's Model II ($|V|$-only degree identity) to solve the problem on just **$N = 5,000$ vertices** (a $10\times$ smaller vertex set)!
- **2. Intermediate Algebraic Representation**:
  Using $\sum_{e \in E(S)} w_e = \frac{1}{2}\sum_{v \in S} \deg_w(v) - \frac{1}{2}w(\delta(S))$:
  $$\max_{S \subseteq V} \left( \sum_{e \in E(S)} w_e - \sum_{v \in S} c_v \right) = \frac{1}{2} \max_{S \subseteq V} \left( \sum_{v \in S} \big(\deg_w(v) - 2c_v\big) - w(\delta(S)) \right).$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Double all weights to keep integers: for each $v \in V$, let $\beta_v = \deg_w(v) - 2c_v$.
  - If $\beta_v > 0$, add $s \to v$ with capacity $\beta_v$ (and add $\beta_v$ to `PosSum`); if $\beta_v < 0$, add $v \to t$ with capacity $-\beta_v$.
  - For each user pair $e = \{u, v\} \in E$, add undirected edge $u \leftrightarrow v$ with capacity $w_e$.
  - Answer is $\frac{1}{2}(\text{PosSum} - \text{MaxFlow}(s, t))$.
  - **Complexity**: Dinic on $5,002$ vertices and $55,000$ edges runs in $< 30\text{ms}$!
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Compare the standard $N+M$ project selection graph with Goldberg's $N$-vertex degree-identity graph.
  - *Hint 2 (Algebraic)*: Write $2 w_e x_u x_v = w_e x_u + w_e x_v - w_e |x_u - x_v|$.
  - *Hint 3 (Compilation)*: Group all linear terms $(\deg_w(v) - 2c_v) x_v$ at vertex $v$ and split by sign!

---

### Tier 2: Intermediate (`P09` – `P16`)

---

#### Problem P09: `[TJOI2012 / Amber 2007] Network Cost-to-Time Ratio Cut` (`网络严密性 / 最小比率割`)
- **Judge / Source**: Amber (Hu Botao) 2007 Thesis Section 2 / UVa 1389 Var (`[ZH]`)
- **Constraints**: $N \le 100, M \le 1,000$ undirected or directed edges with cost $a_e > 0$ and capacity/time $b_e > 0$. Find a cut-set $C \subseteq E$ disconnecting $s$ from $t$ minimizing $\frac{\sum_{e \in C} a_e}{\sum_{e \in C} b_e}$.
- **1. Non-Graph Diagnostic Signal**:
  Minimizing the ratio of two linear sums over an $s$-$t$ disconnecting edge-set $C \subseteq E$. This is the canonical **Archetype 21A** from Section 2.3.
- **2. Intermediate Algebraic Representation**:
  For trial $\lambda \ge 0$, $h(\lambda) = \min_{C \in \mathcal{C}_{s,t}} \sum_{e \in C} (a_e - \lambda b_e)$. Splitting $w_e(\lambda) = a_e - \lambda b_e$ by sign:
  $$h(\lambda) = \sum_{e : w_e(\lambda) \le 0} w_e(\lambda) + \text{MinCut}_{G^+(\lambda)}(s, t).$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Binary search $\lambda \in [0, \max_e (a_e / b_e)]$ (or run Dinkelbach's secant method).
  - At each $\lambda$, initialize `neg_sum = 0` and clear the flow graph. For each edge $e \in E$:
    - If $a_e - \lambda b_e \le 0$: add $a_e - \lambda b_e$ to `neg_sum` (severed unconditionally).
    - Else: add edge $e$ to the flow network with capacity $a_e - \lambda b_e > 0$.
  - Run Dinic to get `flow`. If `neg_sum + flow < 0`, set $R = \lambda$; else set $L = \lambda$.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Convert $\frac{\sum a_e}{\sum b_e} \le \lambda$ into $\sum (a_e - \lambda b_e) \le 0$.
  - *Hint 2 (Algebraic)*: What should you do with an edge whose modified weight $a_e - \lambda b_e$ is negative?
  - *Hint 3 (Compilation)*: Include all negative-weight edges in $C$ automatically (`neg_sum += w_e`), and run Dinic only on the remaining positive-weight edges!

---

#### Problem P10: `CF 847 J — Students Initiation` (Hakimi's Orientation Duality)
- **Judge / Source**: [Codeforces 847J](https://codeforces.com/problemset/problem/847/J) (`[EN]`)
- **Constraints**: $N \le 5,000$ students, $M \le 5,000$ undirected pairs. Orient each edge $e = \{u, v\}$ as $u \to v$ or $v \to u$ to minimize $\max_{v \in V} \text{outdeg}(v)$, and output the orientation.
- **1. Non-Graph Diagnostic Signal**:
  By **Hakimi's Orientation Theorem** (Section 3.3), the minimum possible maximum out-degree is $\lceil \max_{\emptyset \neq S \subseteq V} \frac{|E(S)|}{|S|} \rceil$ (the ceiling of the Maximum Density Subgraph!). Moreover, since we must also output the actual edge orientations for $N, M \le 5,000$, we can binary search the integer cap $D \in [0, M]$ and test feasibility via bipartite max-flow!
- **2. Intermediate Algebraic Representation**:
  By Max-Flow Min-Cut on the orientation network (Source $s \to e$ capacity $1$, $e \to u, v$ capacity $1$, $v \to t$ capacity $D$):
  $$\text{MaxFlow}(D) = \min_{S \subseteq V} \big( |E \setminus E(S)| + D|S| \big) = M - \max_{S \subseteq V} \big( |E(S)| - D|S| \big).$$
  Thus $\text{MaxFlow}(D) = M \iff \max_{S \subseteq V} (|E(S)| - D|S|) \le 0 \iff D \ge \max_{\emptyset \neq S} \frac{|E(S)|}{|S|}$!
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Binary search integer $D \in [0, M]$ ($\le 13$ steps).
  - Build the bipartite network ($N + M + 2$ nodes) and check if Dinic achieves flow $M$. (Even faster: since $D$ increases monotonically, you can increment $D = 0, 1, 2, \dots$ and augment incrementally on the residual graph!).
  - For each edge node $e = \{u, v\}$, inspect which of $e \to u$ or $e \to v$ carries $1$ unit of flow to output the exact orientation.
  - **Complexity**: $O(\log M \cdot (N + M)\sqrt{N + M})$, running in $< 50\text{ms}$.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Each edge $e = \{u, v\}$ has $1$ unit of "indegree/outdegree responsibility" that must be assigned to either $u$ or $v$.
  - *Hint 2 (Algebraic)*: What does the minimum cut of this bipartite assignment graph represent? It is literally the Maximum Density Subgraph!
  - *Hint 3 (Compilation)*: Binary search $D \in [0, M]$ and test whether max-flow equals $M$.

---

#### Problem P11: `CF 724 E — Goods Transportation`
- **Judge / Source**: [Codeforces 724E](https://codeforces.com/problemset/problem/724/E) (`[EN]`)
- **Constraints**: $N \le 10,000$, $c \le 10^9$, $p_i, s_i \le 10^9$.
- **1. Non-Graph Diagnostic Signal**:
  Explicitly asks for the maximum $s$-$t$ flow on $N = 10,000$ vertices where $s \to i$ has capacity $p_i$, $i \to t$ has capacity $s_i$, and every pair $1 \le i < j \le N$ has directed edge $i \to j$ of capacity $c$. With $\binom{N}{2} \approx 5 \times 10^7$ edges, Dinic TLEs. This is **Paradigm 24A** from Section 5.2!
- **2. Intermediate Algebraic Representation**:
  For any subset $S \subseteq \{1, \dots, N\}$ of size $k = |S|$:
  $$\text{Cut}(S) = \sum_{i \notin S} p_i + \sum_{i \in S} s_i + c \cdot |\{(i, j) : i < j, i \in S, j \notin S\}| = \sum_{i=1}^N p_i - \binom{k}{2}c + \sum_{i \in S} \big(s_i - p_i + (N - i)c\big).$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - **Method 1 ($O(N \log N)$ Slope-Trick Greedy)**: Compute $w_i = s_i - p_i + (N - i)c$ for $i = 1 \dots N$, sort $w_1 \le w_2 \le \dots \le w_N$, and take $\min_{0 \le k \le N} \big(\sum_{i=1}^N p_i - \frac{k(k-1)}{2}c + \sum_{r=1}^k w_{(r)}\big)$.
  - **Method 2 ($O(N^2)$ Rolling-Array DP)**: $dp[k] = \min(dp[k] + p_i + k \cdot c,\; dp[k-1] + s_i)$.
  - **Complexity**: $O(N \log N)$ time, $O(N)$ space!
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Convert Max-Flow into Min-Cut: each node $i$ chooses $S$ or $T$.
  - *Hint 2 (Algebraic)*: If $k$ nodes are in $S$, how many pairs $(i, j)$ with $i < j$ have both $i \in S$ and $j \in S$? Always $\binom{k}{2}$, regardless of which nodes are chosen!
  - *Hint 3 (Compilation)*: Use $\sum_{i \in S, j \in T, i < j} 1 = \sum_{i \in S} (N - i) - \binom{|S|}{2}$ to decouple the cost of every vertex $i \in S$!

---

#### Problem P12: `CF 1082 G — Petya and Graph`
- **Judge / Source**: [Codeforces 1082G](https://codeforces.com/problemset/problem/1082/G) (`[EN]`)
- **Constraints**: $N, M \le 1,000$, vertex weights $a_v \ge 1$, edge weights $w_e \ge 1$. Find a subgraph maximizing $\sum_{e \in E(S)} w_e - \sum_{v \in S} a_v$.
- **1. Non-Graph Diagnostic Signal**:
  Identical in structure to `[NOI2006] 最大获利` (`P08`) and a fixed-$\lambda$ step of Weighted Maximum Density Subgraph ($\lambda = 1$)! Can be solved via either $N+M$ Bipartite Closure or Goldberg's $N$-only Degree-Identity Min-Cut.
- **2. Intermediate Algebraic Representation**:
  $$2\left(\sum_{e \in E(S)} w_e - \sum_{v \in S} a_v\right) = \sum_{v \in S} \big(\deg_w(v) - 2a_v\big) - w(\delta(S)).$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - For each $v \in V$, let $\beta_v = \deg_w(v) - 2a_v$. If $\beta_v > 0$, add $s \to v$ capacity $\beta_v$ (and add to `PosSum`); else add $v \to t$ capacity $-\beta_v$.
  - Add undirected edge $u \leftrightarrow v$ of capacity $w_e$ for each $e = \{u, v\} \in E$.
  - Output $(\text{PosSum} - \text{MaxFlow}(s, t)) / 2$.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Choosing an edge $e = \{u, v\}$ requires choosing both endpoints $u$ and $v$.
  - *Hint 2 (Algebraic)*: Either build the $N+M$ closure graph or apply $2\sum_{e \in E(S)} w_e = \sum_{v \in S} \deg_w(v) - w(\delta(S))$.
  - *Hint 3 (Compilation)*: Remember to use `long long` for capacities since $\sum w_e$ can reach $10^{12}$!

---

#### Problem P13: `Generalized Weighted Ratio Closure & MDS` (Amber 2007 General Model)
- **Judge / Source**: Amber (Hu Botao) 2007 Thesis Section 3 (`[ZH]`)
- **Constraints**: $N \le 400, M \le 4,000$, internal edge profit $w_e \ge 0$, boundary cut penalty $\gamma_e \ge 0$, vertex profit $p_v \in \mathbb{R}$, vertex cost $c_v > 0$. Maximize $D_{\text{gen}}(S) = \frac{\sum_{e \in E(S)} w_e + \sum_{v \in S} p_v - \sum_{e \in \delta(S)} \gamma_e}{\sum_{v \in S} c_v}$ over $\emptyset \neq S \subseteq V$.
- **1. Non-Graph Diagnostic Signal**:
  Combines fractional programming, internal subgraph rewards $E(S)$, standalone vertex profits $p_v$, and boundary separation penalties $\delta(S)$ into a single ratio objective.
- **2. Intermediate Algebraic Representation**:
  Using $2\sum_{e \in E(S)} w_e = \sum_{v \in S} \deg_w(v) - \sum_{e \in \delta(S)} w_e$, we test $2(f(S) - \lambda g(S)) > 0$:
  $$\max_{\emptyset \neq S \subseteq V} \left[ \sum_{v \in S} \underbrace{\big(\deg_w(v) + 2p_v - 2\lambda c_v\big)}_{\beta_v(\lambda)} - \sum_{e \in \delta(S)} (w_e + 2\gamma_e) \right] > 0.$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Each original edge $e = \{u, v\} \in E$ gets undirected capacity $w_e + 2\gamma_e$.
  - With Amber's shift $U = \max_v (\deg_w(v) + 2|p_v|) + 2|\lambda| \max_v c_v$: $c(s, v) = U$ and $c(v, t) = U - \beta_v(\lambda)$.
  - Check if $\text{MinCut}(\lambda) < U|V|$ via Dinkelbach's secant method.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Why do both internal edge rewards $w_e \in E(S)$ and boundary cut penalties $\gamma_e \in \delta(S)$ end up on the same undirected graph edge $(u, v)$?
  - *Hint 2 (Algebraic)*: Because $2w_e x_u x_v = w_e x_u + w_e x_v - w_e |x_u - x_v|$, so $w_e$ contributes $+w_e$ to $\deg_w$ and $+w_e$ to the cut, while $-2\gamma_e$ contributes $+2\gamma_e$ directly to the cut!
  - *Hint 3 (Compilation)*: Undirected edge capacity is $w_e + 2\gamma_e$, and vertex coefficient is $\beta_v(\lambda) = \deg_w(v) + 2p_v - 2\lambda c_v$.

---

#### Problem P14: `Dynamic Tree Max-Flow via HLD & DDP` (`Luogu P4719` Cut Dual)
- **Judge / Source**: [Luogu P4719](https://www.luogu.com.cn/problem/P4719) (Dynamic DP Framework applied to Tree Min-Cut) (`[ZH]`)
- **Constraints**: Tree on $N \le 10^5$ vertices, $Q \le 10^5$ online point updates to source capacities $a_u = c(s, u)$ and sink capacities $b_u = c(u, t)$, with fixed undirected tree edge capacities $c_{uv}$. Output $\text{MaxFlow}(s, t)$ after each update.
- **1. Non-Graph Diagnostic Signal**:
  Running Dinic on a tree of size $10^5$ for $10^5$ queries is $O(Q N^2)$, which is impossible. By Max-Flow Min-Cut, the problem is a **Dynamic 2-State Tree DP** ($x_u \in \{S, T\}$) solvable in $O(Q \log^2 N)$ via **Heavy-Light Decomposition + $(\min, +)$ Tropical Matrix Segment Tree** (Paradigm 24C, Section 5.2)!
- **2. Intermediate Algebraic Representation**:
  For each node $u$ with heavy child $w = \text{hv}(u)$ and light children $v \in \text{light}(u)$, let:
  $$L_{u, S} = b_u + \sum_{v \in \text{light}(u)} \min(dp[v][S], dp[v][T] + c_{uv}), \quad L_{u, T} = a_u + \sum_{v \in \text{light}(u)} \min(dp[v][T], dp[v][S] + c_{uv}).$$
  Then $\binom{dp[u][S]}{dp[u][T]} = \begin{pmatrix} L_{u, S} & L_{u, S} + c_{uw} \\ L_{u, T} + c_{uw} & L_{u, T} \end{pmatrix} \otimes \binom{dp[w][S]}{dp[w][T]}$.
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Decompose the tree into heavy chains and map HLD DFS order `dfn[u]` onto a Segment Tree of $2 \times 2$ $(\min, +)$ matrices.
  - When $a_u$ or $b_u$ is updated, update $L_{u, S}, L_{u, T}$ and walk up the HLD chain tops: before updating the current heavy chain's segment tree, subtract the old contribution of the chain head from its parent's $L_{\text{fa}, S}, L_{\text{fa}, T}$, update the segment tree, and add the new contribution!
  - **Complexity**: $O(N + Q \log^2 N)$ time, $O(N)$ space.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: On a tree, how would you compute the minimum $s$-$t$ cut in $O(N)$ time if there were no updates?
  - *Hint 2 (Algebraic)*: Separate each node's transition into its light children aggregate $(L_{u,S}, L_{u,T})$ and its single heavy child transition matrix.
  - *Hint 3 (Compilation)*: Express the heavy-chain recurrence in the $(\min, +)$ tropical matrix semiring and maintain chain products on a segment tree!

---

#### Problem P15: `AtCoder ARC 076 F — Exhausted?` (Bipartite Prefix-Suffix Interval Cut + Segment Tree)
- **Judge / Source**: [AtCoder ARC 076 F](https://atcoder.jp/contests/arc076/tasks/arc076_d) (`[JA]` / `[EN]`)
- **Constraints**: $N \le 2 \times 10^5$ people, $M \le 2 \times 10^5$ chairs at positions $1 \dots M$. Person $i$ can sit on chair $x$ if $x \le L_i$ or $x \ge R_i$. Find the minimum number of people who cannot sit ($N - \text{MaxMatching}$).
- **1. Non-Graph Diagnostic Signal**:
  Bipartite matching with $N, M = 2 \times 10^5$ where each person $i$'s allowed neighborhood is the union of a **prefix** $[1, L_i]$ and a **suffix** $[R_i, M]$ of chairs! Building the graph takes $O(NM)$ edges, and greedy interval scheduling fails because choices are split across two disjoint ends. We must use **Hall's Marriage Theorem / Bipartite Min-Cut Duality + Segment Tree**!
- **2. Intermediate Algebraic Representation**:
  By Hall's Theorem (which is Max-Flow Min-Cut on the bipartite matching graph), the maximum matching is:
  $$\text{MaxMatching} = N - \max_{S \subseteq \{1,\dots,N\}} \big( |S| - |N(S)| \big) \implies N - \text{MaxMatching} = \max_{S \subseteq \{1,\dots,N\}} \big( |S| - |N(S)| \big).$$
  For any subset of people $S$, every person $i \in S$ connects to $[1, L_i] \cup [R_i, M]$. Therefore, the neighborhood $N(S)$ is simply the union of the longest prefix $[1, l]$ and longest suffix $[r, M]$ among $i \in S$, where $l = \max_{i \in S} L_i$ and $r = \min_{i \in S} R_i$!
  If $l \ge r - 1$, then $N(S) = [1, M]$ has size $M$, so $|S| - |N(S)| \le N - M$.
  If $0 \le l < r \le M + 1$, then $|N(S)| = l + (M - r + 1)$, and to maximize $|S|$ for fixed $(l, r)$, we should include **all** people $i$ with $L_i \le l$ and $R_i \ge r$:
  $$\text{Ans} = \max\Big(0,\; N - M,\; \max_{0 \le l < r \le M + 1} \big( \text{count}(L_i \le l \land R_i \ge r) - l - (M - r + 1) \big)\Big).$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Sort people by $L_i$ ascending. Sweep $l$ from $0$ to $M$:
  - Maintain a Range-Add Range-Max Segment Tree over $r \in [1, M + 1]$, initialized at index $r$ with value $r - M - 1$.
  - When sweeping to $l$, for each person $i$ with $L_i = l$, add $+1$ to the range $r \in [1, R_i]$ in the segment tree.
  - Query the maximum over $r \in [l + 1, M + 1]$ in the segment tree and subtract $l$!
  - **Complexity**: $O((N + M) \log M)$ time, $O(N + M)$ space!
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Apply Hall's Theorem / Min-Cut: what can the neighborhood $N(S)$ of a subset of people $S$ look like?
  - *Hint 2 (Algebraic)*: Since each person's neighborhood is $[1, L_i] \cup [R_i, M]$, the union $N(S)$ is always $[1, l] \cup [r, M]$ for some $0 \le l < r \le M+1$ (or the whole $[1, M]$)!
  - *Hint 3 (Compilation)*: Sweep $l$ from $0$ to $M$ and use a segment tree over $r$ to maintain $\text{count}(L_i \le l \land R_i \ge r) + r$!

---

#### Problem P16: `Inverse Gomory–Hu Ultrametric Realizability & Synthesis` (`CF 472 D` Cut Dual)
- **Judge / Source**: Inverse Network Synthesis / Dual of [Codeforces 472D](https://codeforces.com/problemset/problem/472/D) (`[EN]`)
- **Constraints**: Given an $N \times N$ symmetric matrix $M_{uv}$ ($N \le 2,000$), determine if there exists an undirected graph $G$ with $\text{MinCut}_G(u, v) = M_{uv}$ for all $u \neq v$, and if so, construct one with minimum total edge weight.
- **1. Non-Graph Diagnostic Signal**:
  Instead of computing cuts from a graph, we are given the $\binom{N}{2}$ target min-cut matrix $M$ and asked if it is realizable!
- **2. Intermediate Algebraic Representation**:
  By Corollary 6.2 and Gomory–Hu theory, a symmetric matrix $M$ is the all-pairs minimum cut matrix of an undirected graph if and only if $M$ satisfies the **Ultrametric Inequality** $M_{uw} \ge \min(M_{uv}, M_{vw})$ for all $u, v, w \in V$, which holds if and only if $M$ is the path-bottleneck matrix of a **Maximum Spanning Tree** $T^*$ of the complete graph $(V, M)$! Moreover, any graph $G$ realizing $M$ has $\sum_{v} \deg_G(v) \ge \sum_{v} \deg_{T^*}(v)$, so $T^*$ itself is the minimum-weight realizing network!
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Run Prim's or Kruskal's algorithm in $O(N^2)$ time to find a **Maximum Spanning Tree** $T^*$ of $M$.
  - Run $N$ tree DFS traversals on $T^*$ in $O(N^2)$ time to compute the tree path bottlenecks $B_{uv} = \min_{e \in \text{Path}_{T^*}(u,v)} w(e)$, and verify $B_{uv} == M_{uv}$ for all $u, v$.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Every realizable all-pairs min-cut matrix can be realized by a *tree* (its Gomory–Hu tree!).
  - *Hint 2 (Algebraic)*: On a tree where $\lambda(u, v)$ is the minimum weight on the path between $u$ and $v$, why must the tree be a *Maximum* Spanning Tree of $M$?
  - *Hint 3 (Compilation)*: Build the Maximum Spanning Tree of $M$ in $O(N^2)$ and check if all $\binom{N}{2}$ path minimums on the tree match $M_{uv}$!

---

### Tier 3: Advanced (`P17` – `P24`)

---

#### Problem P17: `[NOI2010] 海拔` (Altitude — Coarea Formula + Directed Planar Dual)
- **Judge / Source**: [Luogu P2046](https://www.luogu.com.cn/problem/P2046) / BZOJ 2007 (`[ZH]`)
- **Constraints**: $(N + 1) \times (N + 1)$ grid ($N \le 500$, $V \approx 2.5 \times 10^5$ vertices, $E \approx 10^6$ directed edges with asymmetric capacities in 4 compass directions). $h_{(1,1)} = 0, h_{(N+1,N+1)} = 1$. Minimize $\sum_{(u,v) \in E} c_{uv} \max(0, h_v - h_u)$.
- **1. Non-Graph Diagnostic Signal**:
  Continuous potential optimization $h_v \in \mathbb{R}$ on a directed planar grid of $2.5 \times 10^5$ vertices. By the **Coarea Formula / Lovász Extension Theorem** (Section 4.2), the continuous optimum equals the binary $\{0, 1\}$ $s$-$t$ minimum cut, which in turn reduces to **Directed Dual Dijkstra** (Section 4.3)!
- **2. Intermediate Algebraic Representation**:
  $$\min_{\substack{h \in [0,1]^V \\ h_s = 0, h_t = 1}} \sum_{(u,v) \in E} c_{uv} \max(0, h_v - h_u) = \min_{\substack{x \in \{0,1\}^V \\ x_s = 1, x_t = 0}} \sum_{(u,v) \in E} c_{uv} x_u(1 - x_v) = \text{ShortestPath}_{G^*}(S^*, T^*).$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Use **Convention I** ($S^*$ at Bottom-Left outer face, $T^*$ at Top-Right outer face) with **$90^\circ$ Counter-Clockwise (CCW)** rotation (or **Convention II** with $S^*$ at Top-Right, $T^*$ at Bottom-Left, and **$90^\circ$ Clockwise (CW)** rotation — see Section 4.3 Table):
  - In Convention I ($S^*$ Bottom-Left, $T^*$ Top-Right, $90^\circ$ CCW):
    - Primal East $(i, j) \to (i, j+1)$ rotates $90^\circ$ CCW to Dual North: `cell(i, j) -> cell(i-1, j)`.
    - Primal West $(i, j+1) \to (i, j)$ rotates $90^\circ$ CCW to Dual South: `cell(i-1, j) -> cell(i, j)`.
    - Primal South $(i, j) \to (i+1, j)$ rotates $90^\circ$ CCW to Dual East: `cell(i, j-1) -> cell(i, j)`.
    - Primal North $(i+1, j) \to (i, j)$ rotates $90^\circ$ CCW to Dual West: `cell(i, j) -> cell(i, j-1)`.
    - Out-of-bounds cells `i = 0` or `j = N` map to $T^*$; `i = N` or `j = 0` map to $S^*$.
  - **Complexity**: Dijkstra on $N^2 + 2 = 250,002$ nodes and $4N(N+1) \approx 10^6$ directed edges takes $O(N^2 \log N)$.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Prove via the Coarea Formula $\max(0, h_v - h_u) = \int_0^1 [h_u < \lambda \le h_v]\,d\lambda$ that all optimal altitudes can be chosen in $\{0, 1\}$.
  - *Hint 2 (Algebraic)*: Only directed edges going from $h_u = 0$ ($S$) to $h_v = 1$ ($T$) pay capacity $c_{uv}$.
  - *Hint 3 (Compilation)*: Walk from $S^*$ to $T^*$ in the dual graph and apply the Universal Left/Right Bank Orientation Law (Section 4.3)!

---

#### Problem P18: `CF 343 E — Pumping Stations` (Gomory–Hu Tree + DSU Permutation)
- **Judge / Source**: [Codeforces 343E](https://codeforces.com/problemset/problem/343/E) (`[EN]`)
- **Constraints**: $N \le 200, M \le 1,000$. Find a permutation $p_1, p_2, \dots, p_N$ of $V$ maximizing $\sum_{i=1}^{N-1} \lambda_G(p_i, p_{i+1})$ and output both the maximum sum and the permutation.
- **1. Non-Graph Diagnostic Signal**:
  Maximizing a Hamiltonian path in the complete graph of pairwise min-cuts $\lambda_G(u, v)$. By building the **Gomory–Hu Tree** $T_{\text{GH}}$, we discover a remarkable upper bound: the maximum possible sum is **equal to the sum of all $N - 1$ edge weights of $T_{\text{GH}}$**!
- **2. Intermediate Algebraic Representation**:
  Let $e_{\min} = \arg\min_{e \in E(T_{\text{GH}})} w_T(e)$ be the minimum-weight edge of $T_{\text{GH}}$, splitting $T_{\text{GH}}$ into $(C_1, C_2)$. Any permutation $p_1, \dots, p_N$ must cross between $C_1$ and $C_2$ **at least once**, and that crossing step has $\lambda(p_i, p_{i+1}) \le w_T(e_{\min})$. By induction on subtrees, for every edge $e \in E(T_{\text{GH}})$, at least one adjacent pair in $p$ uses $e$ as its bottleneck, so:
  $$\sum_{i=1}^{N-1} \lambda_G(p_i, p_{i+1}) \le \sum_{e \in E(T_{\text{GH}})} w_T(e).$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - **Step 1**: Build the Gomory–Hu tree $T_{\text{GH}}$ in $N - 1$ Dinic calls.
  - **Step 2 (Constructive Equality via DSU)**: Sort the $N - 1$ edges of $T_{\text{GH}}$ in **descending** order of weight $w_T(e)$! Maintain for each DSU component a linked list (or vector) of its vertices. When processing edge $e = (u, v)$ in descending order, concatenate the vertex list of $\text{find}(u)$ and the vertex list of $\text{find}(v)$!
  - Why does this achieve equality? Because when $e = (u, v)$ is merged last (or after heavier edges inside $\text{find}(u)$ and $\text{find}(v)$), all edges inside the two components have weight $\ge w_T(e)$, so the single boundary junction between the last vertex of $\text{find}(u)$ and the first vertex of $\text{find}(v)$ has bottleneck **exactly $w_T(e)$**!
  - **Complexity**: $(N-1) \cdot T_{\text{Dinic}}(N, M) + O(N \log N)$.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Build the Gomory–Hu tree $T_{\text{GH}}$. Can the answer ever exceed the sum of the $N-1$ edge weights of $T_{\text{GH}}$?
  - *Hint 2 (Algebraic)*: Consider the lightest edge $e_{\min}$ in $T_{\text{GH}}$. If you visit all vertices on one side of $e_{\min}$ before crossing to the other side, you pay $w_T(e_{\min})$ **only once**!
  - *Hint 3 (Compilation)*: Sort the edges of $T_{\text{GH}}$ from heaviest to lightest and concatenate component vertex lists using DSU!

---

#### Problem P19: `CF 1919 F2 — Wine Factory (Hard Version)`
- **Judge / Source**: [Codeforces 1919F2](https://codeforces.com/problemset/problem/1919/F2) (`[EN]`)
- **Constraints**: $N, Q \le 5 \times 10^5$, $a_i, b_i, c_i \le 10^9$ (finite pipe capacities!). Online point updates to $(a_i, b_i, c_i)$.
- **1. Non-Graph Diagnostic Signal**:
  Unlike `F1` (`P07`), here $c_i < \infty$, so the minimum $s$-$t$ cut can cross pipes $i \to i+1$ whenever $x_i = S$ and $x_{i+1} = T$. This is **Paradigm 24B** (Section 5.2), solved by a $2 \times 2$ $(\min, +)$ Tropical Matrix Segment Tree!
- **2. Intermediate Algebraic Representation**:
  Let state $0$ be $x_i = T$ (paying $a_i$) and state $1$ be $x_i = S$ (paying $b_i$). Transitioning from $x_i$ to $x_{i+1}$ pays $c_i$ **if and only if $x_i = 1 (S)$ and $x_{i+1} = 0 (T)$**.
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - In a segment tree over intervals $[L, R]$, each node stores a $2 \times 2$ matrix `dp[u][v]` ($u, v \in \{0, 1\}$) representing the minimum cost on $[L, R]$ given $x_L = u$ and $x_R = v$:
    - **Leaf $i$**: `dp[0][0] = a[i]`, `dp[1][1] = b[i]`, `dp[0][1] = dp[1][0] = INF`.
    - **Merge `Left` ($[L, M]$) and `Right` ($[M+1, R]$) across pipe $c_M$**:
      $$\text{res}[u][v] = \min_{x \in \{0,1\}} \min_{y \in \{0,1\}} \Big( \text{Left}[u][x] + \text{Right}[y][v] + [x == 1 \land y == 0] \cdot c_M \Big).$$
  - Global answer is $\min_{u, v \in \{0,1\}} \text{root.dp}[u][v]$.
  - **Complexity**: $O((N + Q) \log N)$ with $16$ additions/comparisons per segment tree pushup!
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: What changes from `F1` when $c_i$ is finite? The cut sequence $(x_1, \dots, x_N) \in \{S, T\}^N$ can now switch $S \to T$ multiple times!
  - *Hint 2 (Algebraic)*: Write down the exact cost of merging interval $[L, M]$ (ending in state $x \in \{S, T\}$) with $[M+1, R]$ (starting in state $y \in \{S, T\}$).
  - *Hint 3 (Compilation)*: Only $(x, y) = (S, T)$ adds $+c_M$; $(T, S), (S, S), (T, T)$ add $0$!

---

#### Problem P20: `AtCoder ARC 125 E — Snack` (Complete Bipartite Degree-Sorted Min-Cut)
- **Judge / Source**: [AtCoder ARC 125 E](https://atcoder.jp/contests/arc125/tasks/arc125_e) (`[JA]` / `[EN]`)
- **Constraints**: $N, M \le 2 \times 10^5$, $A_i \le 10^{12}, B_j, C_j \le 10^{12}$.
- **1. Non-Graph Diagnostic Signal**:
  Maximum flow on $K_{N, M}$ where $s \to i$ has capacity $A_i$, $i \to j$ has capacity $B_j$, and $j \to t$ has capacity $C_j$. With $4 \times 10^{10}$ edges, this is **Paradigm 24D** (Section 5.2)!
- **2. Intermediate Algebraic Representation**:
  Fixing $k = |S_X| \in [0, N]$ and sorting $A_{(1)} \ge A_{(2)} \ge \dots \ge A_{(N)}$:
  $$\text{MaxFlow} = \min_{0 \le k \le N} \left[ \sum_{i=k+1}^N A_{(i)} + \sum_{j=1}^M \min\big(C_j,\; k \cdot B_j\big) \right].$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Sort $A$ descending and compute suffix sums.
  - Sort children $j \in [1, M]$ by $\frac{C_j}{B_j}$ ascending, and precompute prefix sums of $C_j$ and suffix sums of $B_j$.
  - For each $k = 0 \dots N$, advance a two-pointer index $p(k)$ such that $\frac{C_j}{B_j} \le k \iff j \le p(k)$, and evaluate $\sum_{j \le p(k)} C_j + k \sum_{j > p(k)} B_j$ in $O(1)$ time!
  - **Complexity**: $O((N + M) \log(N + M))$ time, $O(N + M)$ space.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: If you know that exactly $k$ left vertices are in $S$, which $k$ left vertices should they be, and what does each right vertex $j$ pay?
  - *Hint 2 (Algebraic)*: Right vertex $j$ pays $\min(C_j, k B_j)$, which switches from $k B_j$ to $C_j$ at $k \ge \lceil C_j / B_j \rceil$.
  - *Hint 3 (Compilation)*: Sort right vertices by $C_j / B_j$ and sweep $k = 0 \dots N$ with a single pointer!

---

#### Problem P21: `Single-Edge Capacity Sensitivity on Gomory–Hu Trees`
- **Judge / Source**: Advanced Gomory–Hu Sensitivity / UOJ / QOJ Variant (`[EN]` / `[ZH]`)
- **Constraints**: Undirected graph $G = (V, E, w)$ with $N \le 400, M \le 4,000$. For each edge $e \in E$ (or $Q$ queried edges), determine how many unordered pairs $\{u, v\}$ have their minimum cut $\lambda_G(u, v)$ **strictly increased** if the capacity of $e$ is increased by $+1$.
- **1. Non-Graph Diagnostic Signal**:
  Combines **Gomory–Hu Cut Trees** (Section 6.3) with **Picard–Queyranne Residual SCC Vital Edge Analysis** (Wave 1)!
- **2. Intermediate Algebraic Representation**:
  Increasing $w(e)$ for $e = \{x, y\}$ strictly increases $\lambda_G(u, v)$ if and only if $e$ belongs to **every** minimum $u$-$v$ cut in $G$. In any $s$-$t$ max-flow residual graph $G_f$, let $\text{id}(v)$ be the Strongly Connected Component (SCC) of $v$ in $G_f$: then $e = \{x, y\}$ is in every minimum $s$-$t$ cut only if $e$ is saturated and $\{\text{id}(x), \text{id}(y)\} = \{\text{id}(s), \text{id}(t)\}$.
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Build the Gomory–Hu tree $T_{\text{GH}}$. During each of the $N - 1$ max-flow calls for tree edge $e_T = (s, t)$ of weight $W$:
    - Run Tarjan's SCC on the residual graph $G_f(s, t)$.
    - An original edge $e = \{x, y\}$ is vital for the cut $e_T$ if $e$ is saturated in $G_f(s, t)$ and $(\text{id}(x) == \text{id}(s) \land \text{id}(y) == \text{id}(t))$ (or vice versa).
    - More generally, for any pair $(u, v)$ whose unique minimum-weight bottleneck on $\text{Path}_{T_{\text{GH}}}(u, v)$ is $e_T$ (or across all tied minimum edges on $\text{Path}_{T_{\text{GH}}}(u, v)$), $e = \{x, y\}$ increases $\lambda(u, v)$ if and only if for **every** minimum-weight edge $e_T$ on $\text{Path}_{T_{\text{GH}}}(u, v)$, $u$ is in the same residual SCC of $G_f(e_T)$ as $x$, and $v$ is in the same residual SCC as $y$!
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: When does increasing a single edge $e = \{x, y\}$ increase $\text{MinCut}_G(u, v)$? Only when $e$ crosses *every* minimum $u$-$v$ cut!
  - *Hint 2 (Algebraic)*: In the residual graph $G_f$ of a max-flow, how do you test if $(u, x)$ cannot be separated by any minimum cut? They must lie in the same residual SCC!
  - *Hint 3 (Compilation)*: Combine Tarjan's SCC on each of the $N-1$ residual graphs with path-bottleneck decomposition on $T_{\text{GH}}$.

---

#### Problem P22: `Nash-Williams Arboricity & Rooted Forest Packing`
- **Judge / Source**: Classical Combinatorial Optimization / Matroid Union vs. MDS Duality (`[EN]`)
- **Constraints**: Undirected graph $G = (V, E)$ with $N \le 300, M \le 2,000$. Compute the **arboricity** $\Upsilon(G) = \max_{|S| \ge 2} \lceil \frac{|E(S)|}{|S| - 1} \rceil$ (the minimum number of forests needed to cover $E$).
- **1. Non-Graph Diagnostic Signal**:
  Unlike standard MDS $\max \frac{|E(S)|}{|S|}$, the denominator is $|S| - 1$ for $|S| \ge 2$! If we naively minimize $k|S| - |E(S)|$, the empty set $S = \emptyset$ gives $0$ and singletons $S = \{v\}$ give $k$, whereas we need $\max_{|S| \ge 2} (|E(S)| - k|S|) \le -k \iff \min_{|S| \ge 2} (k|S| - |E(S)|) \ge k$.
- **2. Intermediate Algebraic Representation**:
  How do we force $S \neq \emptyset$ and account for the $-1$ in $|S| - 1$? Pick a **root vertex $r \in V$** and force $r \in S$ ($x_r = 1$) at zero denominator cost! Then for any $S \ni r$:
  $$|E(S)| - k(|S| - 1) = |E(S)| - k \sum_{v \in S \setminus \{r\}} 1.$$
  By taking the maximum over all $N$ choices of root $r \in V$ (or in matroid/flow terms, using the Picard–Queyranne closure with $r$ attached to $s$ with capacity $\infty$ and cost $0$):
  $$\Upsilon(G) \le k \iff \forall r \in V,\; \max_{S \ni r} \Big( |E(S)| - k|S \setminus \{r\}| \Big) \le 0.$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Binary search integer $k \in [1, N]$.
  - Using Goldberg's $|V|$-only model with shift $U = M$: for each $v \in V$, $c(s, v) = U$ and $c(v, t) = U + 2k - \deg(v)$.
  - To test all $r \in V$ efficiently without rebuilding from scratch: temporarily add $r \to t$ capacity $-2k$ (or $s \to r$ capacity $\infty$), run max-flow, and check if $\text{MinCut}_r(k) \ge U|V|$!
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Why does the $-1$ in $\frac{|E(S)|}{|S| - 1}$ make $S = \emptyset$ invalid?
  - *Hint 2 (Algebraic)*: Notice that $|S| - 1 = |S \setminus \{r\}|$ whenever $r \in S$!
  - *Hint 3 (Compilation)*: Force a root $r \in S$ with denominator weight $0$ while all other $v \neq r$ have denominator weight $k$.

---

#### Problem P23: `CF 1383 F — Special Edges` ($2^K$ Parametric Min-Cut Precomputation)
- **Judge / Source**: [Codeforces 1383F](https://codeforces.com/problemset/problem/1383/F) (`[EN]`)
- **Constraints**: Directed graph with $N \le 10^4, M \le 10^4$, edge capacities $w_e \le 25$, **$K \le 10$ special edges**, and $Q \le 2 \times 10^5$ queries. Each query specifies the capacities $(w_1, \dots, w_K)$ of the $K$ special edges and asks for $\text{MaxFlow}(1, N)$.
- **1. Non-Graph Diagnostic Signal**:
  Running Dinic per query for $Q = 2 \times 10^5$ queries is impossible. However, **only $K \le 10$ edges change per query**!
- **2. Intermediate Algebraic Representation**:
  Contract/isolate the $K$ special edges. Any $s$-$t$ cut in $G$ induces a binary subset mask $\text{mask} \in \{0, 1\}^K$ of which special edges cross the cut $(S, T)$. If we force the special edges in $\text{mask}$ to have capacity $\infty$ (cannot be cut) and the remaining special edges to have capacity $0$, the minimum cut of the rest of the graph is a fixed constant $C[\text{mask}]$! Then for any query $(w_1, \dots, w_K)$:
  $$\text{MaxFlow}(w) = \min_{\text{mask} \in \{0,1\}^K} \left( C[\text{mask}] + \sum_{i \notin \text{mask}} w_i \right).$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - **Precomputation ($2^K = 1,024$ states)**:
    - First run Dinic once with all $K$ special edges at capacity $0$ to get the base residual graph $G_f(0)$ and base flow $C[0]$.
    - Traverse the $2^K$ masks in a **DFS / Gray-code tree**: to transition from `mask` to `mask | (1 << i)`, copy the residual graph of `mask` and saturate special edge $i$ (capacity $25$) using at most $25$ simple Ford-Fulkerson augmenting paths!
  - **Per Query ($O(2^K)$)**: Compute $\text{sum\_w}[\text{mask}] = \sum_{i \notin \text{mask}} w_i$ in $O(2^K)$ via subset sum DP (`sum_w[m] = sum_w[m ^ lsb] + w[lsb]`) and take $\min_{\text{mask}} (C[\text{mask}] + \text{sum\_w}[\text{mask}])$!
  - **Complexity**: $O(T_{\text{Dinic}} + 2^K \cdot 25 M + Q \cdot 2^K)$.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Each of the $K \le 10$ special edges is either cut or not cut by the minimum $s$-$t$ cut.
  - *Hint 2 (Algebraic)*: There are only $2^{10} = 1,024$ ways the minimum cut can sever the $K$ special edges!
  - *Hint 3 (Compilation)*: Precompute the residual min-cut $C[\text{mask}]$ for all $1,024$ masks by incrementally augmenting at most $25$ units of flow along each special edge in a DFS over masks!

---

#### Problem P24: `AtCoder ABC 347 G — Grid Coloring 2` (Multi-Label Grid Potential $\to$ Threshold Coarea Cut)
- **Judge / Source**: [AtCoder ABC 347 G](https://atcoder.jp/contests/abc347/tasks/abc347_g) (`[JA]` / `[EN]`)
- **Constraints**: $N \times N$ grid ($N \le 20$), some cells have fixed values $A_{i,j} \in \{1, 2, 3, 4, 5\}$, others are unknown ($0$). Choose $a_{i,j} \in \{1, \dots, 5\}$ for unknown cells to minimize $\sum_{\{u, v\} \in E_{\text{grid}}} (a_u - a_v)^2$.
- **1. Non-Graph Diagnostic Signal**:
  Discrete convex potential minimization on a grid with $K = 5$ levels. This connects **Wave 1 Unary Threshold Chains (Burn-and-Bury / `燃やす埋める`)** with **Section 4 Coarea Level-Set Cuts**!
- **2. Intermediate Algebraic Representation**:
  Represent each cell's integer choice $a_u \in \{1, 2, 3, 4, 5\}$ by **$4$ unary threshold bits** $z_{u, t} = [a_u > t] \in \{0, 1\}$ for $t \in \{1, 2, 3, 4\}$, enforcing the monotonicity chain $z_{u,1} \ge z_{u,2} \ge z_{u,3} \ge z_{u,4}$ via $\infty$-capacity edges $z_{u, t+1} \to z_{u, t}$ (so $a_u = 1 + \sum_{t=1}^4 z_{u, t}$).
  How does the quadratic edge penalty $(a_u - a_v)^2$ decompose across the threshold bits $z_{u, t}, z_{v, t'}$?
  Observe that for any integers $a_u, a_v \in \{1, \dots, 5\}$:
  $$(a_u - a_v)^2 = \sum_{t=1}^4 |z_{u, t} - z_{v, t}| + 2 \sum_{1 \le t < t' \le 4} \big( z_{u, t'}(1 - z_{v, t}) + z_{v, t'}(1 - z_{u, t}) \big)!$$
  *Verification*: Suppose $a_u = 4$ ($z_u = (1,1,1,0)$) and $a_v = 2$ ($z_v = (1,0,0,0)$). Then $|a_u - a_v| = 2$:
  - Same-level cuts $t \in \{2, 3\}$ have $|z_{u,t} - z_{v,t}| = 1$, contributing $1 + 1 = 2$.
  - Cross-level cuts $(t, t')$ with $1 \le t < t' \le 4$ where $z_{u, t'} = 1$ and $z_{v, t} = 0$: only $(t, t') = (2, 3)$ qualifies, contributing $2 \times 1 = 2$.
  - Total $= 2 + 2 = 4 = (4 - 2)^2$!
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Create $4 N^2$ vertices $(u, t)$ for $u \in [1, N^2], t \in \{1, 2, 3, 4\}$.
  - **Monotonicity Chain**: Add directed edge $(u, t+1) \to (u, t)$ with capacity $\infty$.
  - **Fixed Cells**: If $A_u \neq 0$, force $z_{u, t} = 1$ ($s \to (u,t)$ capacity $\infty$) for $t < A_u$, and $z_{u, t} = 0$ ($(u,t) \to t_{\text{sink}}$ capacity $\infty$) for $t \ge A_u$.
  - **Convex Quadratic Cut Edges**: For each grid edge $\{u, v\} \in E_{\text{grid}}$:
    - For $t = 1 \dots 4$: add undirected edge $(u, t) \leftrightarrow (v, t)$ of capacity $1$.
    - For $1 \le t < t' \le 4$: add directed edges $(u, t') \to (v, t)$ and $(v, t') \to (u, t)$ of capacity $2$!
  - Reconstruct $a_u = 1 + \sum_{t=1}^4 [z_{u,t} \in S]$ from the residual graph!
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Encode $a_u \in \{1, \dots, 5\}$ using 4 binary variables $z_{u,t} = [a_u > t]$ for $t = 1, 2, 3, 4$.
  - *Hint 2 (Algebraic)*: Note that $|a_u - a_v|^2 = \big(\sum_{t=1}^4 |z_{u,t} - z_{v,t}|\big)^2$ whenever $z_u$ and $z_v$ are monotone!
  - *Hint 3 (Compilation)*: Expand $\big(\sum_{t=1}^4 \Delta_t\big)^2 = \sum_{t=1}^4 \Delta_t + 2\sum_{t < t'} \Delta_t \Delta_{t'}$ into cut edges of capacity $1$ (same level) and $2$ (cross levels)!

---

### Tier 4: Mastery (`P25` – `P32`)

---

#### Problem P25: `[CSP-S 2021] 交通规划` (Traffic Planning — Multi-Terminal Outerplanar Cut + Circular DP)
- **Judge / Source**: [Luogu P7916](https://www.luogu.com.cn/problem/P7916) / LOJ 3544 (`[ZH]`)
- **Constraints**: $N, M \le 500$ grid, $T \le 50$ independent queries, each specifying $k_i \le 50$ outer-boundary terminals with capacities and colors $c_r \in \{0 (\text{White}/S), 1 (\text{Black}/T)\}$.
- **1. Non-Graph Diagnostic Signal**:
  Running multi-source multi-sink Dinic on a $2.5 \times 10^5$-vertex grid for $50$ queries TLEs. Because all $k \le 50$ terminals lie on the **outer boundary**, we apply **Multi-Terminal Outerplanar Duality + Circular Non-Crossing Interval DP** (Section 4.3)!
- **2. Intermediate Algebraic Representation**:
  Sort the $k$ terminals clockwise around the perimeter. The $k$ perimeter intervals between adjacent terminals form $k$ boundary dual vertices $b_1^*, \dots, b_k^*$. An interval $b_r^*$ is a **demand defect** if $c_r \neq c_{r+1}$, yielding an even number $2t \le k$ of defects $u_1^*, \dots, u_{2t}^*$. The minimum multi-terminal cut is the minimum-cost **non-crossing circular pairing** of $u_1^*, \dots, u_{2t}^*$ via shortest paths in $G^*$.
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - **Precomputation**: Build the static interior dual graph on $(N-1)(M-1)$ cells once.
  - **Per Query**:
    - Create $k$ boundary dual nodes $b_1^*, \dots, b_k^*$ (including monochromatic ones where $c_r = c_{r+1}$ as stepping-stone vertices!), connect $b_r^* \leftrightarrow b_{r+1}^*$ with weight equal to terminal $r+1$'s capacity, and attach each perimeter grid edge to its corresponding $b_r^*$.
    - Identify the $2t$ defect nodes $u_1^*, \dots, u_{2t}^*$ where $c_r \neq c_{r+1}$. (If $t = 0$, output $0$).
    - Run Dijkstra $2t$ times from $u_1^*, \dots, u_{2t}^*$ on $G^*$ to get the $2t \times 2t$ distance matrix $D(a, b)$.
    - Duplicate the sequence to length $4t$ and run the $O(t^3)$ Circular Interval DP (Section 4.3)!
  - **Complexity**: $O(\sum k_i \cdot NM \log(NM) + \sum k_i^3)$.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: What happens to the outer face $f_\infty$ when $k$ boundary terminals are attached to the perimeter of the grid?
  - *Hint 2 (Algebraic)*: Only boundary intervals between terminals of *different* colors ($c_r \neq c_{r+1}$) need to emit/absorb a dual cut path!
  - *Hint 3 (Compilation)*: Never delete monochromatic boundary intervals ($c_r = c_{r+1}$) from $G^*$—keep them as intermediate vertices in Dijkstra, then run Circular Interval DP on the $2t$ defect nodes!

---

#### Problem P26: `AtCoder AGC 031 E — Snuke the Phantom Thief` (2D Coordinate Rank-Slot Duality)
- **Judge / Source**: [AtCoder AGC 031 E](https://atcoder.jp/contests/agc031/tasks/agc031_e) (`[JA]` / `[EN]`)
- **Constraints**: $N \le 80$ jewels at $(x_i, y_i)$ with value $v_i \le 10^{15}$; $M \le 320$ constraints of 4 types (`L`, `R`, `D`, `U`): e.g., *"at most $b_j$ stolen jewels can have $x$-coordinate $\le a_j$"*. Maximize total stolen value.
- **1. Non-Graph Diagnostic Signal**:
  Prefix/suffix cardinality constraints on coordinates look like polyhedral knapsack, **until we fix the total number of stolen jewels $K \in [1, N]$**!
- **2. Intermediate Algebraic Representation**:
  Suppose we steal **exactly $K$ jewels**, sorted by $x$-coordinate as $x_{i_1} \le x_{i_2} \le \dots \le x_{i_K}$ (assigning jewel $i_r$ to **$x$-rank slot $r \in \{1, \dots, K\}$**):
  - **"At most $b$ jewels have $x \le a$"** $\iff$ the $(b+1)$-th stolen jewel from the left must have $x > a$ $\iff \forall r \in [b+1, K],\; L_x[r] \ge a + 1$!
  - **"At most $b$ jewels have $x \ge a$"** $\iff$ the $(K - b)$-th stolen jewel from the left must have $x < a$ $\iff \forall r \in [1, K - b],\; R_x[r] \le a - 1$!
  Identical rank-slot bounds $[L_y[c], R_y[c]]$ hold for the $y$-rank slots $c \in \{1, \dots, K\}$!
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Loop over $K = 1 \dots N$. For a fixed $K$:
    - Compute the allowed coordinate interval $[L_x[r], R_x[r]]$ for each $x$-slot $r \in [1, K]$ (enforcing $L_x[r] \le L_x[r+1]$ and $R_x[r] \le R_x[r+1]$) and $[L_y[c], R_y[c]]$ for each $y$-slot $c \in [1, K]$.
    - Build a Min-Cost Max-Flow network:
      - $s \to x\text{-slot } r$ (cap $1$, cost $0$).
      - $x\text{-slot } r \to \text{jewel } i_{\text{in}}$ (cap $1$, cost $0$) if $x_i \in [L_x[r], R_x[r]]$.
      - $\text{jewel } i_{\text{in}} \to \text{jewel } i_{\text{out}}$ (cap $1$, cost $-v_i$).
      - $\text{jewel } i_{\text{out}} \to y\text{-slot } c$ (cap $1$, cost $0$) if $y_i \in [L_y[c], R_y[c]]$.
      - $y\text{-slot } c \to t$ (cap $1$, cost $0$).
    - If max-flow is $K$, update global max profit with $-\text{MinCost}(K)$.
  - **Complexity**: $N$ runs of MCMF with flow $K \le 80$ on $3N$ vertices, running in $< 0.2\text{s}$.
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: What if you guess the exact total number of stolen jewels $K \in [1, N]$?
  - *Hint 2 (Algebraic)*: Once $K$ is fixed, "at most $b$ stolen jewels have $x \le a$" translates into a hard lower bound $x \ge a + 1$ on the $(b+1)$-th stolen jewel!
  - *Hint 3 (Compilation)*: Match $K$ $x$-rank slots to $K$ jewels and $K$ $y$-rank slots via Min-Cost Flow!

---

#### Problem P27: `Reif's Interior s-t Planar Minimum Cut` (Primal Path Slicing & $\mathbb{Z}_2$ Lift)
- **Judge / Source**: Reif (1983) / Hassin & Johnson (1985) / Planar Interior Cut Benchmark (`[EN]`)
- **Constraints**: Connected undirected planar graph $G = (V, E, w)$ with $N \le 10^5$, given with its planar embedding (cyclic clockwise edge ordering around each vertex), where $s, t \in V$ lie in the **interior** of $G$ (not on the same face).
- **1. Non-Graph Diagnostic Signal**:
  Because $s$ and $t$ do not share a face, we cannot add $(t, s)$ without crossing edges! Any minimal $s$-$t$ cut in $G$ corresponds to a **minimum-weight $s$-$t$ separating cycle $C^*$ in $G^*$**.
- **2. Intermediate Algebraic / Topological Representation**:
  Let $P = (e_1, e_2, \dots, e_L)$ be a shortest $s$-$t$ path (by hop count) in the primal graph $G$. In $\mathbb{Z}_2$ homology on the punctured plane $\mathbb{R}^2 \setminus \{s, t\}$, a dual cycle $C^*$ separates $s$ from $t$ if and only if its algebraic/parity intersection number with $P$ is non-zero (odd), so $C^*$ must cross at least one dual edge $e_i^* \in P^*$.
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Slice $G^*$ open along $P^* = (e_1^*, \dots, e_L^*)$, splitting each crossed dual edge $e_i^*$ into a Left terminal $u_{i, L}$ and Right terminal $u_{i, R}$.
  - Define $f(i) = w(e_i^*) + \text{dist}_{G^* \setminus P^*}(u_{i, L}, u_{i, R})$, the shortest cycle crossing $P^*$ at $e_i^*$.
  - Because shortest paths in a planar graph can be chosen not to cross each other, if we compute the shortest path $C_{\text{mid}}^*$ for $m = \lfloor (l + r)/2 \rfloor$, $C_{\text{mid}}^*$ slices the dual graph into two smaller pieces! Recursively solving $[l, m-1]$ inside one piece and $[m+1, r]$ inside the other piece (`Reif's Divide-and-Conquer`) takes $O(\log L)$ recursion levels, with total Dijkstra work $O(N \log N)$ per level!
  - **Complexity**: $O(N \log^2 N)$ deterministic time (or $O(N \log \log N)$ via Italiano et al. 2011).
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Why does a minimum $s$-$t$ cut dualize to a *cycle* instead of a path when $s$ and $t$ are in the interior?
  - *Hint 2 (Algebraic)*: Any cycle separating $s$ from $t$ must cross any primal $s$-$t$ path $P$ an odd number of times!
  - *Hint 3 (Compilation)*: Cut the dual graph along $P^*$ into Left and Right banks and use Divide-and-Conquer Dijkstra!

---

#### Problem P28: `All-Lambda Parametric Maximum Density Hull (GGT Nested Subgraphs)`
- **Judge / Source**: Gallo–Grigoriadis–Tarjan (1989) / Advanced Parametric Density Queries (`[EN]` / `[ZH]`)
- **Constraints**: Undirected graph $G = (V, E, w)$ with $N \le 500, M \le 5,000$, and $Q \le 2 \times 10^5$ online queries. Each query gives a real penalty $\lambda \ge 0$ and asks for $\max_{S \subseteq V} \big(|E(S)| - \lambda |S|\big)$.
- **1. Non-Graph Diagnostic Signal**:
  We must evaluate the piecewise-linear convex curve $h(\lambda) = \max_{S \subseteq V} (|E(S)| - \lambda |S|)$ at $Q = 2 \times 10^5$ different values of $\lambda$.
- **2. Intermediate Algebraic Representation**:
  By the **Nested Cut Theorem (GGT 1989)**, because source capacities $c(s, v) = U$ are constant and sink capacities $c(v, t) = U + 2\lambda - \deg(v)$ are monotonically non-decreasing in $\lambda$, the minimal source-side optimal subgraphs $S^*(\lambda)$ form a **strictly nested chain**:
  $$V = S_0 \supsetneq S_1 \supsetneq S_2 \supsetneq \dots \supsetneq S_k = \emptyset.$$
  Therefore, the upper hull of $\{ (|S|, |E(S)|) : S \subseteq V \}$ has **at most $N$ vertices (breakpoints)**!
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - **Milstein / Eisner–Severance Recursive Hull Discovery**:
    - Define `solve(S_L, S_R)` where $S_R \subsetneq S_L \subseteq V$ are the optimal subgraphs at two endpoints $\lambda_L < \lambda_R$.
    - Compute the intersection point (secant slope) $\lambda_{\text{mid}} = \frac{|E(S_L)| - |E(S_R)|}{|S_L| - |S_R|}$.
    - Run Dinic at $\lambda = \lambda_{\text{mid}}$ (contracting $S_R$ into $s$ and $V \setminus S_L$ into $t$ so the subproblem graph only has $|S_L \setminus S_R|$ vertices!).
    - If the resulting optimal subgraph $S_{\text{mid}}$ has $|E(S_{\text{mid}})| - \lambda_{\text{mid}} |S_{\text{mid}}| > |E(S_L)| - \lambda_{\text{mid}} |S_L|$, add $(|S_{\text{mid}}|, |E(S_{\text{mid}})|)$ to the upper convex hull and recurse on `(S_L, S_mid)` and `(S_mid, S_R)`!
  - **Per Query**: Binary search on the $\le N$ hull vertices in $O(\log N)$ time!
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: As $\lambda$ increases from $0$ to $\infty$, can a vertex $v$ ever leave $S^*(\lambda)$ and re-enter later?
  - *Hint 2 (Algebraic)*: By submodularity, $S^*(\lambda_1) \supseteq S^*(\lambda_2)$ for $\lambda_1 < \lambda_2$, so there are at most $N$ distinct optimal subgraphs across all $\lambda \in [0, \infty)$!
  - *Hint 3 (Compilation)*: Contract $S_R$ into $s$ and $V \setminus S_L$ into $t$ during recursive hull discovery so the total vertex count across each recursion layer is $\le N$!

---

#### Problem P29: `CF 1765 I — Infinite Chess` (Coordinate-Compressed Strip Cut / Dual Shortest Path)
- **Judge / Source**: [Codeforces 1765I](https://codeforces.com/problemset/problem/1765/I) (`[EN]`)
- **Constraints**: $8 \times 10^8$ chessboard, King moves from $(x_s, y_s)$ to $(x_t, y_t)$ avoiding cells attacked by $N \le 15$ static chess pieces (queens, rooks, bishops, knights, kings).
- **1. Non-Graph Diagnostic Signal**:
  A planar grid of height $8$ and width $10^8$ where obstacles/attacks are horizontal, vertical, and $45^\circ$ diagonal rays. By Planar Cycle-Cut / Obstacle-Separating Duality, any long empty vertical strip $[x_L, x_R]$ with no piece at distance $\le 8$ has **translation-invariant** attack patterns!
- **2. Intermediate Algebraic Representation**:
  Since the board height is only $H = 8$, a $45^\circ$ diagonal ray from any piece at column $x_i$ can only intersect the board within columns $[x_i - 8, x_i + 8]$! Outside $\bigcup_{i=1}^N [x_i - 8, x_i + 8]$, the attack status of every row $y \in [1, 8]$ is purely horizontal and constant across each interval of columns.
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - Collect all interesting columns $\mathcal{X} = \bigcup_{i=1}^N [x_i - 8, x_i + 8] \cup \{x_s, x_t\}$ ($\le 17 \times 17 \approx 300$ columns).
  - Compress each gap $(x_r, x_{r+1})$ between consecutive interesting columns into a single column transition of horizontal weight $x_{r+1} - x_r$, and run Dijkstra on the $8 \times |\mathcal{X}| \approx 2,400$ states!
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: The board has only $8$ rows! How far horizontally can a Bishop or Queen at column $x_i$ attack along a diagonal?
  - *Hint 2 (Algebraic)*: At most $7$ columns to the left and $7$ columns to the right!
  - *Hint 3 (Compilation)*: Keep all columns within $\pm 8$ of each piece explicitly, and compress all other empty column intervals into weighted horizontal edges!

---

#### Problem P30: `AtCoder AGC 029 F — Construction of a Tree` (Hyperedge-to-Tree Arboricity & Hall Duality)
- **Judge / Source**: [AtCoder AGC 029 F](https://atcoder.jp/contests/agc029/tasks/agc029_f) (`[JA]` / `[EN]`)
- **Constraints**: $N \le 10^5$ vertices and $N - 1$ subsets $E_1, \dots, E_{N-1} \subseteq V$ with $\sum |E_i| \le 2 \times 10^5$. Choose two vertices $u_i, v_i \in E_i$ from each subset so that the $N - 1$ edges $(u_i, v_i)$ form a spanning tree of $V$, or report `-1`.
- **1. Non-Graph Diagnostic Signal**:
  Every tree on $V$ rooted at vertex $1$ establishes a **1-to-1 bijection** between the $N - 1$ edges $E_1, \dots, E_{N-1}$ and the $N - 1$ non-root vertices $V \setminus \{1\}$ (where each edge $e_i = (u_i, v_i)$ is matched to its **child** endpoint $v_i \in E_i \setminus \{1\}$, and its parent endpoint $u_i \in E_i$ has smaller depth)!
- **2. Intermediate Algebraic Representation**:
  By Nash-Williams / Hall's Marriage Theorem:
  1. **Necessary Condition**: There must exist a perfect matching $M$ between the $N - 1$ hyperedges $\{E_1, \dots, E_{N-1}\}$ and the $N - 1$ non-root vertices $V \setminus \{1\}$ such that $v_i \in E_i$ for all $i$.
  2. **Sufficiency & Tree Connectivity**: Given such a perfect matching $M$ ($E_i \leftrightarrow v_i$), start a BFS from the root $r = 1$: whenever a vertex $u$ is visited, for every unmatched-parent hyperedge $E_i \ni u$, we can set $u_i = u$ and visit its matched partner $v_i$! If this BFS visits all $N$ vertices, we have a valid tree; if the BFS gets stuck at a subset $S \subsetneq V$ ($1 \in S$), then all hyperedges touching $S$ are matched inside $S \setminus \{1\}$, so $|E(V \setminus S)| \ge |V \setminus S|$ (a subset of $k$ vertices containing $k$ internal hyperedges, which can never be acyclic!), proving **no solution exists**!
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - **Step 1**: Build a bipartite graph between $L = \{E_1, \dots, E_{N-1}\}$ ($N-1$ nodes) and $R = V \setminus \{1\}$ ($N-1$ nodes), connecting $E_i \to v$ for all $v \in E_i \setminus \{1\}$.
  - **Step 2**: Run **Hopcroft–Karp (Dinic on unit bipartite network)** in $O(\sum |E_i| \sqrt{N})$ time. If maximum matching $< N - 1$, output `-1`.
  - **Step 3**: Let `match[i] = v_i` be the vertex matched to $E_i$. Run a BFS starting from queue `Q = {1}`: when popping $u$, for each hyperedge $E_i \ni u$ not yet used, record edge $(u, \text{match}[i])$, mark $E_i$ used, and push `match[i]` to `Q`.
  - If `< N` vertices are visited, output `-1`; otherwise output the $N - 1$ pairs!
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Root the target tree at vertex $1$. Every edge $E_i$ has a unique *deeper* endpoint (child) in $V \setminus \{1\}$!
  - *Hint 2 (Algebraic)*: Match the $N-1$ sets $E_i$ to $V \setminus \{1\}$ via Hopcroft–Karp. Does *any* perfect matching work?
  - *Hint 3 (Compilation)*: Yes! Start a BFS from vertex $1$ to assign the parent endpoint $u_i \in E_i$ of each set $E_i$ and advance to its matched child $v_i$; if the BFS fails to reach all vertices, the complement violates $|E(S)| \le |S|-1$ so `-1` is guaranteed!

---

#### Problem P31: `Dinits–Karzanov–Lomonosov Cactus of All Global Min-Cuts` (`CF 528 E` / `ICPC Cactus Cut`)
- **Judge / Source**: Dinits–Karzanov–Lomonosov (1976) / Gabow (1995) / All Global Min-Cuts Cactus (`[EN]` / `[ZH]`)
- **Constraints**: Undirected weighted graph $G = (V, E, w)$ with $N \le 300, M \le 3,000$. Construct the **Global Min-Cut Cactus $\mathcal{K}(G)$** and output the exact number of distinct global minimum cuts in $G$ (and answer whether two vertices $u, v$ can be separated by a global minimum cut).
- **1. Non-Graph Diagnostic Signal**:
  Stoer–Wagner (`P06`) only finds *one* global minimum cut, and a Gomory–Hu tree (`P03`) only represents one cut per pair (missing crossing global min-cuts in cycles!). By **Theorem 7.2 (Section 7.2)**, all $\le \binom{N}{2}$ global minimum cuts are represented by the **DKL Cactus $\mathcal{K}(G)$**!
- **2. Intermediate Algebraic Representation**:
  Let $\lambda^* = \min_{\emptyset \subset S \subset V} w(\delta(S))$ be the global minimum cut value (found via Stoer–Wagner). A pair $(u, v)$ can be separated by a global minimum cut if and only if $\lambda_G(u, v) = \lambda^*$. For any fixed $(s, t)$ with $\lambda_G(s, t) = \lambda^*$, the Picard–Queyranne residual DAG $D_{s,t} = \text{SCC}(G_f(s, t))$ represents all global minimum cuts separating $s$ and $t$!
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - **Step 1**: Run Stoer–Wagner (or Gomory–Hu) to find $\lambda^* = \min_{u \neq v} \lambda_G(u, v)$.
  - **Step 2 (Counting & Cactus Construction via Gomory–Hu + PQ-DAGs / Gabow)**:
    - In the Gomory–Hu tree $T_{\text{GH}}$, every global minimum cut separates at least one tree edge $e_T = (s, t) \in E(T_{\text{GH}})$ with $w_T(e_T) = \lambda^*$.
    - Even more directly (Recursive Partition / Karger–Stein or PQ-DAG Ordering): pick a root $r = 1$. Every global minimum cut $(S, \bar{S})$ with $r \notin S$ separates $r$ from some $v \in S$. By ordering vertices $v_2, \dots, v_N$ and computing the Picard–Queyranne DAG of $G_f(r, v_i)$ whenever $\lambda(r, v_i) = \lambda^*$ (contracting already-processed $v_2, \dots, v_{i-1}$ into $r$ if we only want cuts where $v_i$ is the *first* vertex in $S$!), we count every global minimum cut $(S, \bar{S})$ **exactly once** at its minimum-index vertex $v_i = \min(S)$!
    - Specifically, in iteration $i = 2 \dots N - 1$: run $\text{MaxFlow}(1, i)$ on the graph where $\{1, \dots, i-1\}$ are contracted into supernode $1$. If $\text{MaxFlow}(1, i) == \lambda^*$, build the Picard–Queyranne residual DAG of $G_f(1, i)$: because global min-cuts only cross in circular necklaces (Section 7.2), the PQ-DAG of $(1, i)$ is a **chain of cycle/bridge blocks**, and counting its closed sets (or constructing the DKL cactus cycles of weight $\lambda^*/2$) gives the exact count of global min-cuts with $\min(S) = i$!
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Every global minimum cut $(S, \bar{S})$ has one side not containing vertex $1$; let $S$ be that side, and let $i = \min(S) \in \{2, \dots, N\}$ be the smallest-numbered vertex in $S$.
  - *Hint 2 (Algebraic)*: A cut $(S, \bar{S})$ with $1 \notin S$ has $\min(S) = i$ if and only if $\{1, 2, \dots, i-1\} \subseteq \bar{S}$ and $i \in S$!
  - *Hint 3 (Compilation)*: Contract $\{1, \dots, i-1\}$ into $1$ and find all minimum $1$-$i$ cuts of weight $\lambda^*$ via the Picard–Queyranne DAG!

---

#### Problem P32: `AtCoder ABC 326 G — Unlock Achievement` (Multi-Level Threshold Chains vs. Projective Cut Duality)
- **Judge / Source**: [AtCoder ABC 326 G](https://atcoder.jp/contests/abc326/tasks/abc326_g) (`[JA]` / `[EN]`)
- **Constraints**: $N \le 50$ skills (levels $1 \dots 5$, upgrading skill $i$ by $+1$ level costs $C_i$), $M \le 50$ achievements (achievement $j$ gives reward $A_j$ if $\forall i,\; \text{level}_i \ge L_{j, i}$). Maximize total reward minus upgrade cost.
- **1. Non-Graph Diagnostic Signal**:
  The textbook synthesis linking **Wave 1 Multi-State Threshold Chains (`燃やす埋める`)**, **Section 3 Bipartite Closure**, and **Section 5 Min-Cut Structural Reductions**!
- **2. Intermediate Algebraic Representation**:
  For each skill $i \in [1, N]$ and threshold $k \in \{2, 3, 4, 5\}$, let $z_{i, k} = [\text{level}_i \ge k] \in \{0, 1\}$ with cost $C_i$, subject to $z_{i, 2} \ge z_{i, 3} \ge z_{i, 4} \ge z_{i, 5}$. For each achievement $j \in [1, M]$, let $y_j \in \{0, 1\}$ indicate unlocking achievement $j$ (reward $A_j$), subject to $y_j = 1 \implies z_{i, L_{j,i}} = 1$ for all $i$ with $L_{j,i} \ge 2$:
  $$\max_{y, z} \left( \sum_{j=1}^M A_j y_j - \sum_{i=1}^N \sum_{k=2}^5 C_i z_{i, k} \right) = \sum_{j=1}^M A_j - \min_{y, z} \left[ \sum_{j=1}^M A_j(1 - y_j) + \sum_{i=1}^N \sum_{k=2}^5 C_i z_{i, k} + \infty \sum_{i, k} z_{i, k+1}(1 - z_{i, k}) + \infty \sum_{j, i} y_j(1 - z_{i, L_{j,i}}) \right].$$
- **3. Reverse-Engineering Scratchpad (Mechanical Compilation)**:
  - **Vertices**: $4N$ skill-threshold nodes $(i, k)$ ($k \in \{2,3,4,5\}$) and $M$ achievement nodes $j$, plus $s, t$ ($252$ vertices total).
  - **Edges**:
    - $s \to j$ with capacity $A_j$.
    - $(i, k) \to t$ with capacity $C_i$.
    - Chain monotonicity: $(i, k+1) \to (i, k)$ with capacity $\infty$.
    - Achievement prerequisite: $j \to (i, L_{j, i})$ with capacity $\infty$ whenever $L_{j, i} \ge 2$.
  - Output $\sum_{j=1}^M A_j - \text{MaxFlow}(s, t)$!
- **4. Toy Trace & Progressive Hints**:
  - *Hint 1 (Diagnostic)*: Each skill starts at level $1$ and can take $4$ binary upgrade steps $k \in \{2, 3, 4, 5\}$.
  - *Hint 2 (Algebraic)*: Write $z_{i, k} = [\text{level}_i \ge k] \in \{0, 1\}$ with $z_{i, k+1} \le z_{i, k}$.
  - *Hint 3 (Compilation)*: Notice that because $y_j \le z_{i, L_{j,i}}$ and $z_{i, k+1} \le z_{i, k}$ already enforce monotonicity, you can even omit the $(i, k+1) \to (i, k)$ $\infty$-edges if you just connect $(i, k) \to t$ with $C_i$ and $j \to (i, k)$ for all $2 \le k \le L_{j,i}$!

---

## Section 9: Reconciled Quarantined Template Problems Table

In accordance with the **Zero Boilerplate / Quarantine Mandate**, naked template verification problems that require no algebraic modelling beyond pasting a standard algorithm are quarantined here:

| Quarantine ID | Problem Name & Judge URL | Underlying Naked Template | Reason for Quarantine |
| :--- | :--- | :--- | :--- |
| **`R-01`** | [Luogu P3376 — 【模板】网络最大流](https://www.luogu.com.cn/problem/P3376) | Standard Dinic Max-Flow | Direct $s$-$t$ max-flow input with zero compilation. |
| **`R-02`** | [Luogu P4722 — 【模板】最大流 加强版 / HLPP](https://www.luogu.com.cn/problem/P4722) | Highest-Label Push-Relabel | Pure constant-factor / engine benchmark. |
| **`R-03`** | [Luogu P5632 — 【模板】Stoer–Wagner 全局最小割](https://www.luogu.com.cn/problem/P5632) | Stoer–Wagner `MAS` | Naked global minimum cut template verification. |
| **`R-04`** | [Luogu P4897 — 【模板】最小割树 (Gomory–Hu Tree)](https://www.luogu.com.cn/problem/P4897) | Gusfield / Gomory–Hu + LCA | Naked pairwise $\text{MinCut}(u, v)$ query template. |
| **`R-05`** | [LOJ 2042 — 最小割树模板](https://loj.ac/p/2042) | Gusfield Cut Tree | Identical to Luogu P4897. |
| **`R-06`** | [POJ 2987 — Firing](http://poj.org/problem?id=2987) | Maximum Weight Closure | Naked Picard–Queyranne closure without ratio or degree reduction. |
| **`R-07`** | [POJ 2728 — Desert King](http://poj.org/problem?id=2728) | 0-1 Fractional MST | Dinkelbach on Spanning Trees (Prim), not Min-Cut. |
| **`R-08`** | [Luogu P3199 — [HNOI2009] 最小圈](https://www.luogu.com.cn/problem/P3199) | Minimum Mean Cycle | Contrasted in Section 2.1 (solved via SPFA/Karp, not Min-Cut). |
| **`R-09`** | [Luogu P1344 — [USACO4.4] 追查坏牛奶](https://www.luogu.com.cn/problem/P1344) | Min-Cut Edge Count ($W \cdot c_e + 1$) | Basic tie-breaking scaling from Wave 1. |
| **`R-10`** | [HDU 3061 — Battle](https://acm.hdu.edu.cn/showproblem.php?pid=3061) | Naked Max-Weight Closure | Direct prerequisite DAG closure without fractional or planar twists. |

---

## Section 10: Unified Multilingual `[EN]` / `[ZH]` / `[JA]` Bibliography

### `[EN]` English Foundational Papers, Monographs & Editorials
1. **Dinkelbach, W. (1967)**. *"On Nonlinear Fractional Programming."* Management Science, 13(7), 492–498. (Proves convexity, strict monotonicity, and superlinear Newton-secant convergence of $h(\lambda) = \max_x (f(x) - \lambda g(x))$).
2. **Goldberg, A. V. (1984)**. *"Finding a Maximum Density Subgraph."* Technical Report UCB/CSD-84-171, University of California, Berkeley. (Introduces the $|V|$-only degree-sum reduction $2|E(S)| = \sum_{v \in S} \deg(v) - |\delta(S)|$ and proves the $\frac{1}{N(N-1)}$ rational separation bound).
3. **Gallo, G., Grigoriadis, M. D., & Tarjan, R. E. (1989)**. *"A Fast Parametric Maximum Flow Algorithm and Applications."* SIAM Journal on Computing, 18(1), 30–55. (Proves the Nested Cut Theorem and shows that all $\le N$ breakpoints of a monotone parametric network can be found in $O(N^2 M)$ time).
4. **Charikar, M. (2000)**. *"Greedy Approximation Algorithms for Finding Dense Components in a Graph."* APPROX 2000, LNCS 1913, 84–95. (LP relaxation of Maximum Density Subgraph and 2-approximation guarantee of minimum-degree peeling).
5. **Hakimi, S. L. (1965)**. *"On the Degrees of the Vertices of a Directed Graph."* Journal of the Franklin Institute, 279(4), 290–308. (Characterizes out-degree constrained graph orientations via subgraph density).
6. **Nash-Williams, C. St. J. A. (1964)**. *"Decomposition of Finite Graphs into Forests."* Journal of the London Mathematical Society, 1(1), 12. (Proves $\Upsilon(G) = \max_{|S| \ge 2} \lceil \frac{|E(S)|}{|S|-1} \rceil$).
7. **Hassin, R. (1981)**. *"Maximum Flow in $(s, t)$ Planar Networks."* Information Processing Letters, 13(3), 107. (Establishes the $O(N \log N)$ reduction from $s$-$t$ planar min-cut to dual Dijkstra).
8. **Reif, J. H. (1983)**. *"Minimum $s$-$t$ Cut of a Planar Undirected Network in $O(n \log^2 n)$ Time."* SIAM Journal on Computing, 12(1), 71–81. (Introduces primal-path Left/Right bank slicing and divide-and-conquer Dijkstra for interior $s$-$t$ cuts).
9. **Hassin, R., & Johnson, D. B. (1985)**. *"An $O(n \log^2 n)$ Algorithm for Maximum Flow in Undirected Planar Networks."* SIAM Journal on Computing, 14(3), 612–624.
10. **Gomory, R. E., & Hu, T. C. (1961)**. *"Multi-Terminal Network Flows."* Journal of the Society for Industrial and Applied Mathematics, 9(4), 551–570. (Proves the Cut Uncrossing Lemma and constructs the $N-1$ max-flow Cut Tree).
11. **Gusfield, D. (1990)**. *"Very Simple Methods for All Pairs Network Flow Analysis."* SIAM Journal on Computing, 19(1), 143–155. (Derives the 15-line uncontracted star-splitting algorithm for Flow-Equivalent and Cut-Equivalent Gomory–Hu trees).
12. **Stoer, M., & Wagner, F. (1997)**. *"A Simple Min-Cut Algorithm."* Journal of the ACM, 44(4), 585–591. (Proves the Maximum Adjacency Search `MAS` contraction theorem for global undirected minimum cuts).
13. **Karger, D. R. (1993)** & **Karger, D. R., & Stein, C. (1996)**. *"A New Approach to the Minimum Cut Problem."* Journal of the ACM, 43(4), 601–640. (Proves the $\le \binom{N}{2}$ upper bound on global minimum cuts via random edge contraction and the $O(N^2 \log^3 N)$ recursive contraction algorithm).
14. **Dinits, E. A., Karzanov, A. V., & Lomonosov, M. V. (1976)**. *"On the Structure of the System of Minimum Edge Cuts in a Graph."* Studies in Discrete Optimization (in Russian / English translation), 290–306. (Establishes the canonical Cactus Representation $\mathcal{K}(G)$ of all global minimum cuts).
15. **Lovász, L. (1983)**. *"Submodular Functions and Convexity."* Mathematical Programming: The State of the Art, 235–257. (Connects submodular set functions to convex optimization via the Coarea / Lovász extension).

### `[ZH]` Chinese Competitive Programming Treatises (`国家集训队论文`) & Technical Blogs
16. **Hu Botao (胡伯涛 / Amber, 2007)**. 《最小割模型在信息学竞赛中的应用》 (*Applications of Minimum Cut Models in Olympiad in Informatics*), Chinese IOI National Training Team Papers (`2007年国家集训队论文`). (The seminal Chinese treatise introducing 0-1 Fractional Programming + Min-Cut, Goldberg's $|V|$-only Maximum Density Subgraph reduction with $+U$ shift, vertex/edge weighted extensions, and exact rational gap analysis via `POJ 3155 Hard Life`).
17. **Zhou Dong (周冬, 2009)**. 《浅析最大最小定理在信息学竞赛中的应用》 (*Applications of the Max-Flow Min-Cut Theorem in OI*), Chinese IOI National Training Team Papers (`2009年国家集训队论文`). (Detailed treatment of `[BJWC2006] 狼抓兔子`, planar dual shortest paths, and directed grid rotation rules).
18. **NOI 2010 Official Editorial (`[NOI2010] 海拔`) & CSP-S 2021 Official Editorial (`[CSP-S 2021] 交通规划`)**, CCF (`中国计算机学会`). (Establishes the discrete Coarea $\{0,1\}$ reduction on directed planar grids and multi-terminal outerplanar boundary pairing via circular interval DP).
19. **OI-Wiki Contributors**. [《最大权闭合子图与最大密度子图》](https://oi-wiki.org/graph/flow/min-cut/) & [《最小割树 (Gomory–Hu Tree)》](https://oi-wiki.org/graph/flow/gomory-hu/).

### `[JA]` Japanese Competitive Programming Treatises (`燃やす埋める` / `双対性`)
20. **noshi91 (2019)**. [「燃やす埋める問題と劣モジュラ関数の最小化」](https://noshi91.hatenablog.com/entry/2021/06/29/044225) (*Burn-and-Bury Problems and Submodular Function Minimization*). (Formalizes the Submodularity Sign Law, multi-level threshold chains $z_{i,t} = [a_i \ge t]$ as in `ABC 326 G` and `ABC 347 G`, and degree-identity reductions).
21. **maspypy (2020)**. [「最大流・最小カットの双対性と DP への言い換え」](https://maspypy.com/) (*Duality of Max-Flow / Min-Cut and Reformulation as DP*). (Covers `ARC 125 E`, `ARC 076 F`, and `AGC 031 E` rank-slot and degree-sorted min-cut reductions).
22. **tatyam (2022)**. *AtCoder Editorial Series on Planar Duality and Monge / Submodular Cuts*.

---

## Appendix A: Worked End-to-End Verification Traces & Cross-Pillar Synthesis

To make every Subtlety from Sections 2–7 immediately concrete at the keyboard, this appendix provides five self-contained, hand-checkable numerical traces and structural verification checklists across all five reconciled iterations.

---

### A.1 Complete Numerical Trace of the Dinits–Karzanov–Lomonosov (DKL) Global Min-Cut Cactus

Consider an undirected weighted graph $G = (V, E, w)$ on $N = 6$ vertices consisting of two triangles $\{1, 2, 3\}$ and $\{4, 5, 6\}$ joined by two parallel bridge-like paths, or more illustratively, a **4-cycle of clusters**:
- Let $V = \{1, 2, 3, 4, 5, 6\}$ where:
  - Cluster $Q_1 = \{1, 2\}$ with internal edge $w(1, 2) = 3$.
  - Cluster $Q_2 = \{3\}$, Cluster $Q_3 = \{4, 5\}$ with internal edge $w(4, 5) = 2$, Cluster $Q_4 = \{6\}$.
  - Cycle edges between clusters: $w(2, 3) = 2, w(3, 4) = 2, w(5, 6) = 2, w(6, 1) = 2$.
  - Additionally, inside $Q_1$, vertex $1$ has degree $w(6,1) + w(1,2) = 5$, except if $w(1, 2) = 4$, then breaking $\{1, 2\}$ costs $4 + 2 = 6 > 4$. Let us set $w(1, 2) = 4$ and $w(4, 5) = 4$.

#### Step 1: Global Minimum Cut Value $\lambda^*$
- Any cut that does not split $Q_1 = \{1, 2\}$ or $Q_3 = \{4, 5\}$ is a cut of the 4-cycle $(Q_1 - Q_2 - Q_3 - Q_4 - Q_1)$ where every cycle edge has weight $2 = \frac{\lambda^*}{2}$, so cutting any two edges of the 4-cycle has weight:
  $$\lambda^* = 2 + 2 = 4.$$
- What if we split $Q_3 = \{4, 5\}$ by isolating $\{4\}$ or $\{5\}$? Since $w(4, 5) = 4$ causes $\deg_w(4) = w(3, 4) + w(4, 5) = 2 + 4 = 6 > 4$, no global minimum cut can separate $4$ from $5$, **unless** $w(4, 5)$ is a tree bridge of weight $4$!
- Specifically, modify $G$ so that $4$ and $5$ are connected **only** by a single bridge edge $e_{\text{bridge}} = (4, 5)$ of weight $4$ (and the cycle edges are $(2, 3) = 2, (3, 4) = 2, (4, 6) = 2, (6, 1) = 2, (1, 2) = 2$, with $5$ attached solely to $4$ by weight $4$):
  1. Then $V \setminus \{5\} = \{1, 2, 3, 4, 6\}$ forms a **5-cycle** of edge weight $2 = \frac{\lambda^*}{2}$.
  2. Vertex $5$ is attached to vertex $4$ of the 5-cycle via a **tree bridge** of weight $4 = \lambda^*$.

#### Step 2: Enumerating All Global Minimum Cuts via $\mathcal{K}(G)$
- The DKL Cactus $\mathcal{K}(G)$ consists of:
  - A **5-cycle** $C_1 = (1 - 2 - 3 - 4 - 6 - 1)$ with cycle edge weights $\frac{\lambda^*}{2} = 2$.
  - A **1-edge tree bridge** $e_1 = (4, 5)$ with bridge weight $\lambda^* = 4$.
- By **Theorem 7.2**:
  - Removing the single bridge $e_1 = (4, 5)$ gives **$1$ global minimum cut**: $(\{5\}, \{1, 2, 3, 4, 6\})$ of weight $4$.
  - Removing **any pair of edges** from the 5-cycle $C_1$ gives $\binom{5}{2} = 10$ global minimum cuts (where node $4$ always drags node $5$ along with it into the same side of the cut!):
    1. $\{1\}$ vs. $\{2, 3, 4, 5, 6\}$ (cuts $(6,1)$ and $(1,2)$, weight $2+2=4$)
    2. $\{2\}$ vs. $\{1, 3, 4, 5, 6\}$ (cuts $(1,2)$ and $(2,3)$, weight $4$)
    3. $\{3\}$ vs. $\{1, 2, 4, 5, 6\}$ (cuts $(2,3)$ and $(3,4)$, weight $4$)
    4. $\{4, 5\}$ vs. $\{1, 2, 3, 6\}$ (cuts $(3,4)$ and $(4,6)$, weight $4$)
    5. $\{6\}$ vs. $\{1, 2, 3, 4, 5\}$ (cuts $(4,6)$ and $(6,1)$, weight $4$)
    6. $\{1, 2\}$ vs. $\{3, 4, 5, 6\}$ (cuts $(6,1)$ and $(2,3)$, weight $4$)
    7. $\{2, 3\}$ vs. $\{1, 4, 5, 6\}$ (cuts $(1,2)$ and $(3,4)$, weight $4$)
    8. $\{3, 4, 5\}$ vs. $\{1, 2, 6\}$ (cuts $(2,3)$ and $(4,6)$, weight $4$)
    9. $\{4, 5, 6\}$ vs. $\{1, 2, 3\}$ (cuts $(3,4)$ and $(6,1)$, weight $4$)
    10. $\{6, 1\}$ vs. $\{2, 3, 4, 5\}$ (cuts $(4,6)$ and $(1,2)$, weight $4$)
- Total number of global minimum cuts is:
  $$\#\text{GlobalMinCuts}(G) = b + \binom{|C_1|}{2} = 1 + \binom{5}{2} = 11 \le \binom{6}{2} = 15.$$
- Notice how a Gomory–Hu tree $T_{\text{GH}}$ on $G$ can only keep $5 - 1 = 4$ edges of the 5-cycle plus the bridge $(4, 5)$, representing only $5$ of the $11$ global minimum cuts, whereas the DKL Cactus $\mathcal{K}(G)$ represents **all $11$ cuts** without loss!

---

### A.2 Complete Walkthrough of `[CSP-S 2021] 交通规划` Monochromatic Stepping-Stone Trap

Let us trace a concrete $1 \times 2$ grid ($2$ interior cells $f_1, f_2$) with $k = 4$ perimeter terminals to see why deleting monochromatic boundary intervals ($c_r = c_{r+1}$) produces a wrong answer:

```
          Terminal 1 (White, cap=100)      Terminal 2 (White, cap=1)
                    |                                |
   (b_4*: B-W)      v          (b_1*: W-W)           v       (b_2*: W-B)
  +-------------------------------------------------------------------+
  |                                 |                                 |
  |             Cell f_1            |             Cell f_2            |
  |         (interior cap=50)       |         (interior cap=50)       |
  |                                 |                                 |
  +-------------------------------------------------------------------+
                    ^                                ^
                    |                                |
          Terminal 4 (Black, cap=100)      Terminal 3 (Black, cap=100)
                               (b_3*: B-B)
```

1. **Terminal Colors & Capacities**:
   - $T_1$: White ($c_1 = 0$), capacity $100$.
   - $T_2$: White ($c_2 = 0$), capacity $1$.
   - $T_3$: Black ($c_3 = 1$), capacity $100$.
   - $T_4$: Black ($c_4 = 1$), capacity $100$.
   - All grid edges bordering $f_1, f_2$ have huge capacity $50$.
2. **True Primal Minimum Cut**:
   - Since $T_1, T_2$ are White ($S$) and $T_3, T_4$ are Black ($T$), we can simply cut the terminal edge of $T_2$ (cost $1$) and cut the grid edge separating $T_1$ from $T_3, T_4$ around $f_1$ (cost $50$), for total cut **$51$** (instead of cutting through both $f_1$ and $f_2$ for $50 + 50 = 100$).
3. **Dual Graph $G^*$ Trace**:
   - The $4$ boundary intervals are:
     - $b_1^*$ (between $T_1$ and $T_2$): $c_1 = 0, c_2 = 0$ (**Monochromatic** $W$-$W$, NOT a defect!).
     - $b_2^*$ (between $T_2$ and $T_3$): $c_2 = 0 \neq c_3 = 1$ (**Defect $u_1^*$**).
     - $b_3^*$ (between $T_3$ and $T_4$): $c_3 = 1, c_4 = 1$ (**Monochromatic** $B$-$B$, NOT a defect!).
     - $b_4^*$ (between $T_4$ and $T_1$): $c_4 = 1 \neq c_1 = 0$ (**Defect $u_2^*$**).
   - We need the shortest path in $G^*$ between defect $u_1^* = b_2^*$ and defect $u_2^* = b_4^*$:
     - **With $b_1^*$ kept in $G^*$ (Correct)**: The path starts at $u_1^* = b_2^*$, crosses terminal edge $T_2$ (cost $1$!) into the monochromatic boundary node $b_1^*$, enters cell $f_1$ across the top boundary, and exits into $u_2^* = b_4^*$ for total distance $1 + 50 = 51$!
     - **If $b_1^*$ is omitted from $G^*$ (Broken)**: The dual path cannot cross $T_2$ because $b_1^*$ does not exist! It is forced to enter $f_2$ (cost $50$) and $f_1$ (cost $50$) to reach $b_4^*$, returning $100 \neq 51$!

---

### A.3 Complete Matrix Pushup Trace for `CF 1919 F2 — Wine Factory`

Suppose $N = 3$ towers with:
- Tower 1: $a_1 = 10, b_1 = 2$, pipe $c_1 = 3$.
- Tower 2: $a_2 = 1, b_2 = 10$, pipe $c_2 = 4$.
- Tower 3: $a_3 = 8, b_3 = 3$.

Let us trace the $2 \times 2$ $(\min, +)$ segment tree matrices (Section 8, `P19`) where state $0 = T$ (cuts $s \to i$, pays $a_i$) and state $1 = S$ (cuts $i \to t$, pays $b_i$), and only transition $1 \to 0$ ($S \to T$) across pipe $i$ pays $+c_i$:

1. **Leaf Matrices**:
   $$M_{[1,1]} = \begin{pmatrix} 10 & \infty \\ \infty & 2 \end{pmatrix}, \quad M_{[2,2]} = \begin{pmatrix} 1 & \infty \\ \infty & 10 \end{pmatrix}, \quad M_{[3,3]} = \begin{pmatrix} 8 & \infty \\ \infty & 3 \end{pmatrix}.$$
2. **Merge $[1, 1]$ and $[2, 2]$ across Pipe $c_1 = 3$**:
   - $(0, 0)$ ($T_1 \to T_2$): $10 + 1 = 11$.
   - $(0, 1)$ ($T_1 \to S_2$): $10 + 10 + \mathbf{0} = 20$ (note: $T \to S$ pays $0$ pipe cost!).
   - $(1, 0)$ ($S_1 \to T_2$): $2 + 1 + \mathbf{3} = 6$ (note: $S \to T$ pays $+c_1 = 3$!).
   - $(1, 1)$ ($S_1 \to S_2$): $2 + 10 = 12$.
   $$M_{[1,2]} = \begin{pmatrix} 11 & 20 \\ 6 & 12 \end{pmatrix}.$$
3. **Merge $[1, 2]$ and $[3, 3]$ across Pipe $c_2 = 4$**:
   - $(0, 0)$: $\min(11 + 8,\; 20 + 8 + 4) = 19$ ($T, T, T$).
   - $(0, 1)$: $\min(11 + 3 + 0,\; 20 + 3) = 14$ ($T, T, S$).
   - $(1, 0)$: $\min(6 + 8,\; 12 + 8 + 4) = 14$ ($S, T, T$).
   - $(1, 1)$: $\min(6 + 3 + 0,\; 12 + 3) = 9$ ($S, T, S$: Tower 1 in $S$ pays $b_1=2$, Pipe 1 cut $S_1 \to T_2$ pays $c_1=3$, Tower 2 in $T$ pays $a_2=1$, Pipe 2 $T_2 \to S_3$ pays $0$, Tower 3 in $S$ pays $b_3=3$; total $= 2 + 3 + 1 + 0 + 3 = 9$!).
   $$M_{[1,3]} = \begin{pmatrix} 19 & 14 \\ 14 & 9 \end{pmatrix} \implies \text{MaxFlow} = \min_{u,v} M_{[1,3]}[u][v] = 9.$$
- **Flow Verification**: How much wine is actually produced?
  - Tower 1 receives $10$ water, wizard 1 turns $2$ into wine, and sends $\min(10-2, c_1=3) = 3$ water to Tower 2.
  - Tower 2 receives $1 + 3 = 4$ water, wizard 2 turns $\min(4, b_2=10) = 4$ into wine (or sends up to $c_2 = 4$ to Tower 3, where Tower 3 already has $a_3 = 8 \ge b_3 = 3$ water to saturate wizard 3 with $3$ wine).
  - Total wine produced $= 2 + 4 + 3 = 9$, matching $\min M_{[1,3]} = 9$!

---

### A.4 Pre-Submission Debugging & Invariant Checklist for Wave 3A Problems

Whenever a solution in Wave 3A produces `WA`, `TLE`, or `MLE`, run through this 8-point diagnostic checklist:

1. **Fractional Programming Precision (`Iter 21/73`)**:
   - Did you separate `EPS_FLOW = 1e-11` (inside Dinic BFS/DFS) from `EPS_CUT = 1e-8` (outer binary search sign check)?
   - In Network Disconnection (`P09`), did you unconditionally sever edges with $w_e(\lambda) \le 0$ and add them to `neg_sum` instead of clamping them to $0$?
2. **Maximum Density Subgraph Reconstruction (`Iter 22/74`)**:
   - Did you reconstruct the vertex set $S^*$ at $\lambda = L$ (the last strictly feasible lower bound where $h(L) > 0$) instead of $\lambda = R$ (where $S = \emptyset$ ties or wins)?
   - Are you applying the $|V|$-only degree reduction only to $2$-uniform graphs, and switching to the $|V| + |\mathcal{E}|$ Bipartite Closure when hyperedges have size $k \ge 3$?
3. **Planar Duality Orientation & Degeneracy (`Iter 23/75`)**:
   - Did you verify the **Universal Left/Right Bank Orientation Law** (if Primal $S$ is on the Left of $S^* \to T^*$, rotate $90^\circ$ CCW; if Primal $S$ is on the Right of $S^* \to T^*$, rotate $90^\circ$ CW)?
   - Did you handle degenerate 1D grids ($N = 1$ or $M = 1$) in `[BJWC2006] 狼抓兔子` (`P01`) where $(N-1)(M-1) = 0$?
   - In `[CSP-S 2021] 交通规划` (`P25`), did you keep monochromatic boundary intervals ($c_r = c_{r+1}$) in $G^*$ as intermediate Dijkstra stepping stones?
4. **Min-Cut DP & Gomory–Hu Trees (`Iter 24/76 & 25/77`)**:
   - In `CF 1919 F2` (`P19`), did you charge $+c_i$ **only** on the $S \to T$ transition and $0$ on $T \to S$?
   - In Gusfield / Gomory–Hu (`P03, P04, P18`), did you reset all flow values to $0$ on the **original uncontracted graph $G$** before each of the $N - 1$ Dinic runs, and include Line 4 (`if (in_S[p[t]])`) whenever the problem queries physical cut partitions rather than just path bottleneck values?
