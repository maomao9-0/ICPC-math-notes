# Cohort 3 — Wave 4B Master Reconciliation Monograph: LP Duality, Totally Unimodular (TU) Matrices, Submodular Function Minimization (SFM), and the Polyhedral Boundary of Network Flows

**Document Role**: Cohort 3 Cross-Comparison, Blind-Spot Audit, Gap-Hunt, and Definitive Synthesis for Wave 4B (reconciling Cohort 1 `flows_research/iter_36_to_40_lp_duality_tu_matrices_submodular.md` [Iterations 36–40] and Cohort 2 `flows_research/cohort2_iter_88_to_92_lp_duality_tu_matrices_submodular.md` [Iterations 88–92]).  
**Mandate**: Strictly enforces the **Zero Magic Gadgets** rule (4-Step English-to-Graph Compilation: Diagnostic Signal $\to$ Intermediate Algebraic / Logical Representation $\to$ Reverse-Engineering Scratchpad $\to$ Hand-Checkable Toy Trace & Broken Gadget Counterexamples) and **Zero Boilerplate Solver Code**.

---

## 1. Cross-Cohort Blind-Spot Audit & Reconciliation Matrix

A rigorous line-by-line audit of Cohort 1 (1,836 lines) and Cohort 2 (1,661 lines) reveals that the two cohorts approached the polyhedral and algebraic foundations of network flows from complementary angles:
- **Cohort 1** excelled in **explicit sign mnemonics ("Sensible vs. Bizarre")**, **post-augmentation residual SPFA engineering** (identifying the virtual super-root $Q$ vs. pre-augmentation Dijkstra potential trap), **edge-path tree incidence differences $D_T$**, **Kolmogorov–Zabih degree-2 cut representability vs. Zivný–Cohen–Jeavons degree-$\ge 3$ barriers**, and **Isotonic Regression (`保序回归`)** (`[省选联考 2020] 魔法商店` / `保序回归`).
- **Cohort 2** excelled in **formal polyhedral equivalence theorems** (the Column-Incidence Recognition Theorem, the Role Reversal Principle in Project Crashing, the Fundamental Duality Identity of Interval Networks, and the 4-Way Duality Gap Decomposition), **vertex-path tree incidence reductions**, **circular-ones flow rescue via parametric wrap-around volume $K$**, **Double-Counting / Dual Uncrossing proofs for SFM and Polymatroids**, and **Two Laminar Matroids (Hasse Out-Tree + In-Tree)**.
- **Shared Blind Spots**: Neither cohort stated **Seymour's Decomposition Theorem for Totally Unimodular Matrices (1980)** (which explains *why* every TU matrix in competitive programming reduces to either a Primal Flow or Dual Potential network, modulo $R_{10}$), nor **Murota's Discrete Convex Analysis ($L^\natural$-Convex vs. $M^\natural$-Convex Duality)** (which unifies Lovász extensions, node potentials $\pi$, multi-state cuts `[HNOI2013] 切糕`, and isotonic regression on the $L^\natural$ side with base polyhedra $B(f)$, conserved flows $f$, and WQS / simulated MCMF convexity on the $M^\natural$ side), nor the **$O(Q \log F)$ Parametric LP Duality Slope Envelope** (`CF 1307 G`) and **SCC DAG Node-Splitting Potential Initialization** (`ABC 214 H`).

### 1.1 Theoretical & Modelling Blind-Spot Matrix

| Iteration Topic | Cohort 1 Strengths (`iter_36_to_40`) | Cohort 2 Strengths (`cohort2_iter_88_to_92`) | Cohort 1 Blind Spots | Cohort 2 Blind Spots | Cohort 3 Reconciled Synthesis & Gap-Hunt |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Iter 36 / 88: Explicit LP Primal–Dual Compilation (`LP对偶转网络流`)** | Full Lagrangian derivation; **"Sensible vs. Bizarre" Sign Table**; Max-Flow/Min-Cut LP via return edge $f_{ts}$; dualizing both Min & Max potential problems; 3-position toy trace + 3 broken gadget proofs for `[ZJOI2013] 防守战线`. | **Column-Incidence Recognition Theorem** (adding ground row $r_0 = -\sum r_u$ turns any difference-constraint transpose into a Kirchhoff matrix); **Role Reversal Principle** (Primal money cost $\leftrightarrow$ Dual capacity; Primal duration $\leftrightarrow$ Dual edge cost); **Fundamental Duality Identity of Interval Networks**. | Did not explicitly prove the equivalence between Primal equation subtraction $E_t - E_{t-1}$ and Dual prefix potential substitution $p_t = \pi_t - \pi_{t-1}$. | Omitted the explicit "Sensible vs. Bizarre" sign table and the broken-gadget counterexample where $p_i \le 1$ is given $+1$ instead of $-1$ cost. | Unifies the Lagrangian derivation, Sign Table, Column-Incidence Theorem, Role Reversal Principle, and Fundamental Duality Identity of Interval Networks (**Section 2**). |
| **Iter 37 / 89: Difference Constraints, Inverse SP/MST, & Critical Path Compression** | Clean LP dualizations of Inverse Shortest Path (`防守战线`), Symmetric/Asymmetric Inverse MST (`SHOI2004`, `BZOJ 3118`), and PERT/CPM Project Crashing. | Formal theorem dualizing Bellman–Ford feasibility (`差分约束系统`) to minimum-cost negative-cycle detection; piecewise-linear convex crashing curve compilation to parallel edges; `Cow Loops` cycle compression. | Did not cover dynamic/offline Inverse/Parametric MST matroid contraction-reduction (`[WC2006] 水管局长` / `[HNOI2010] 城市建设`). | Treated `[SHOI2004]` and `[BZOJ 3118]` primarily in the problem bank rather than deriving the full symmetric vs. asymmetric matroid exchange spectrum in the main text. | Synthesizes Bellman–Ford vs. Circulation Duality, Inverse SP, Symmetric/Asymmetric/Dynamic Inverse MST, and DAG/Cycle Crashing (**Section 3**). |
| **Iter 38 / 90: Complementary Slackness (`互补松弛`) & Recovering $\pi^*$, Cuts, & Schedules** | **Reduced Cost Trichotomy** ($f>0 \Rightarrow c_\pi \le 0$, $f<u \Rightarrow c_\pi \ge 0$, $0<f<u \Rightarrow c_\pi = 0$); **3 Engineering Pitfalls** (pre-augmentation Dijkstra potentials, disconnected `INF` components, stopping at cost $0$ without tying $\pi(S)=\pi(T)$); full triangle trace for Inverse MST weights. | **4-Way Equivalence Theorem** via explicit Duality Gap Decomposition $\text{Gap}(f^*, \pi^*)$; DAG Project Crashing timestamp recovery trace ($t^*(v) = -\pi^*(v) + \pi^*(s)$); explicit primal schedule recovery in `[LOJ 6079]`. | Omitted the $O(Q \log F)$ parametric LP slope envelope (`CF 1307 G`) and SCC DAG condensation potential recovery (`ABC 214 H`). | Did not warn as sharply against the pre-augmentation Dijkstra potential trap or disconnected residual components when running SPFA from $S$ instead of a super-root $Q$. | Unifies the 4-Way Duality Gap proof, Reduced Cost Trichotomy, Virtual Super-Root $Q$ SPFA Contract, Parametric Slope Envelope $O(Q \log F)$, and Schedule Recovery (**Section 4**). |
| **Iter 39 / 91: Totally Unimodular (TU) Matrices, Consecutive-Ones, & Tree-Path Networks** | Proof of Hoffman–Kruskal via Cramer's Rule; Ghouila–Houri Equitable Bicoloring; **Edge-Path Incidence Matrix $D_T$** ($e_u - \sum_{v \in \text{child}(u)} e_v$) with $K_{1,3}$ star $\det = +2$ counterexample; split-interval & circular-interval counterexamples. | **Tutte Network Matrix Theorem**; **Vertex-Path Incidence Matrix** ($E'_v = E_v - \sum_{w \in \text{child}(v)} E_w$ compiling $P_j = u_j \rightsquigarrow v_j$ to $v_j \to \text{parent}(u_j)$); Row vs. Column Consecutive-Ones transpose trap; **Circular-Ones Rescue** via fixed wrap-around flow $K$ & complementation. | Covered only edge-path tree matrices (missing vertex-path compilation) and did not show how to rescue Circular-Ones matrices via parametric flow $K$. | Omitted the $K_{1,3}$ undirected tree path counterexample ($\det = +2$) and the explicit Cramer's rule proof of Hoffman–Kruskal. | Synthesizes Hoffman–Kruskal, Ghouila–Houri, Tutte Network Matrices, Row vs. Column Consecutive-Ones, Circular-Ones Rescue, and **both** Edge-Path & Vertex-Path Tree Compilations (**Section 5**). |
| **Iter 40 / 92: SFM, Lovász Extension, Base Polyhedra $B(f)$, & Matroid Intersection Boundary** | **Degree-2 Cut Representability** ($A+D \le B+C$) vs. **Degree-$\ge 3$ Barrier**; Coarea Theorem $\int_{-\infty}^\infty \hat{f}(\mathbf{1}_{x \ge \lambda}) d\lambda$; Polymatroid Flows (Edmonds–Giles TDI); **Flow Amnesia (`流量失忆`) & Wrong Layer Order** in 3DM; 2-Commodity half-integral 4-cycle ($\det = -2$). | **Double-Counting Cut Submodularity Proof**; **Dual Uncrossing Proof of Edmonds' Greedy Theorem**; **Two Laminar Matroids (Hasse Out-Tree + In-Tree)**; why degree bounds on an independent set $B \subseteq V$ form 2 Matroids (`CF 1284 G`) while general degree-bounded MST is NP-hard (3 Matroids). | Did not present the general Two Laminar Matroids Hasse Out-Tree + In-Tree construction or Landau's Tournament Base Polyhedron (`[WC2007] 剪刀石头布`). | Did not present the Degree-2 vs. Degree-$\ge 3$ pseudo-Boolean barrier or the explicit Wrong Layer Order counterexample for 3-partite flow. | Unifies the 4-Level Polyhedral Hierarchy, Lovász Coarea Theorem, Laminar Out-Tree + In-Tree, Flow Amnesia, Graphic $\cap$ Partition Matroid Intersection, and Multi-Commodity Barriers (**Section 6**). |
| **Cohort 3 Targeted Gap-Hunting (New Theoretical Unifications)** | Treated Primal Consecutive-Ones (`DA`) and Dual Consecutive-Ones (`A^T \pi`) as two empirical techniques without citing the deep matroid decomposition theorem. | Treated Lovász extensions (`[NOI2010] 海拔`, `CF 1427 G`) and Base Polyhedra (`[WC2007] 剪刀石头布`) without connecting them via discrete Legendre–Fenchel conjugacy. | Missing **Seymour's Regular Matroid / TU Decomposition Theorem (1980)** and **Murota's Discrete Convex Analysis ($L^\natural$- vs. $M^\natural$-Convexity)**. | Missing **Seymour's Decomposition Theorem (1980)** and **Murota's Discrete Convex Analysis ($L^\natural$- vs. $M^\natural$-Convexity)**. | Adds **Section 7.1 (Seymour's TU Decomposition Theorem)** and **Section 7.2 (Murota's $L^\natural$-Convex & $M^\natural$-Convex Duality)** plus the Master Recognition Table (**Section 7.3**). |

### 1.2 Practice Problem Cross-Cohort Deduplication & Tier Audit (32 Unique Problems)

Across Cohort 1 (20 problems) and Cohort 2 (22 problems), there were **13 overlapping problems**, **7 problems unique to Cohort 1**, **9 problems unique to Cohort 2**, and **3 high-priority gap-hunt problems** identified in the Cohort 3 prompt (`CF 1307 G`, `ABC 214 H`, and `[WC2006] 水管局长` / `[HNOI2010] 城市建设`). All **32 unique problems** are retained, deduplicated, and organized into four balanced 8-problem tiers in **Section 8**:

| Master ID & Tier | Problem Title & Judge Coordinates | Source Cohort(s) | Core Algebraic / Polyhedral Mechanism |
| :--- | :--- | :--- | :--- |
| **P01** (`Stepping Stone`) | `[USACO07OPEN] Dining G` (Luogu P2891 / POJ 3281) | C1 P01 & C2 P1 | 3-Entity Star Compatibility ($F \text{--} C \text{--} D$) & Middle-Vertex Split vs. 3DM Triangle Trap |
| **P02** (`Stepping Stone`) | `[NOI2008] 志愿者招募` (Luogu P3980 / BZOJ 1061) | C1 P02 & C2 P2 | Column-Consecutive-Ones $DA\mathbf{x} = \mathbf{0}$ vs. LP Dual Prefix Potentials |
| **P03** (`Stepping Stone`) | `[ZJOI2013] 防守战线` (Luogu P3337 / BZOJ 3112) | C1 P03 & C2 P3 | Row-Consecutive-Ones Transpose Dual to MCMF & fundamental interval duality |
| **P04** (`Stepping Stone`) | `Codeforces 362E — Petya and Pipes` | C1 P04 | Elastic Cut Dual / Two-Regime Capacity Expansion under Budget $K$ |
| **P05** (`Stepping Stone`) | `POJ 3680 — Intervals` (Luogu SP3871) | C1 P05 | Coordinate-Compressed Weighted Interval $k$-Packing via $D A \mathbf{x} = \mathbf{0}$ |
| **P06** (`Stepping Stone`) | `Codeforces 704D — Captain America` | C2 P5 | Two Partition Matroids / Bipartite Bounded Degree $[L_i, R_i]$ Flow |
| **P07** (`Stepping Stone`) | `[BZOJ 1283] 序列` (Hydro BZOJ 1283) | C2 P9 | Toeplitz Band Sliding-Window Consecutive-Ones $k$-Packing |
| **P08** (`Stepping Stone`) | `AtCoder ARC 085 E — MUL` | C1 P07 | Divisibility Poset Submodular Closure & LP Dual Integrality |
| **P09** (`Intermediate`) | `[SHOI2004] 最小生成树` (Luogu P4412 / BZOJ 1937) | C1 P06 & C2 P4 | Symmetric Inverse MST via Fundamental Cycle Bipartite Dual & SPFA Weight Recovery |
| **P10** (`Intermediate`) | `[BZOJ 3118] Orz the Immortal` | C1 P11 & C2 P6 | Asymmetric Weighted Inverse MST via Bipartite Capacitated MCMF Dual |
| **P11** (`Intermediate`) | `[AHOI2014 / JSOI2014] 支线剧情` (Luogu P4043) | C1 P08 & C2 P7 | Rooted DAG Edge Coverage Lower Bounds & Dual Longest-Path Potentials |
| **P12** (`Intermediate`) | `Codeforces 1288F — Red-Blue Graph` | C1 P09 & C2 P8 | Bipartite Signed Incidence Matrix & 3-State Edge Charge Lower-Bound MCMF |
| **P13** (`Intermediate`) | `[ONTAK 2010 / Luogu P6967] Vacation` & `[LOJ 6079] Delight for a Cat` | C2 P11 & C2 P14 | Two-Sided Window Bounds $[L, R]$ via Bounded Slack Edges $y_t \in [0, R-L]$ + Schedule Recovery |
| **P14** (`Intermediate`) | `[WC2007] 剪刀石头布` (Luogu P4249) | C2 P10 | Landau's Tournament Base Polyhedron $B(f)$, Convex Marginal Splitting & Matrix Recovery |
| **P15** (`Intermediate`) | `[BZOJ 1937 / Directed Tree Path Coverage]` | C1 P10 | Rooted Tree Incidence Difference Matrix $D_T$ ($e_u - \sum_{v \in \text{child}(u)} e_v$) |
| **P16** (`Intermediate`) | `Codeforces 1307G — Cow and Exercise` | **C3 Gap-Hunt** | Shortest-Path Extension LP Dual & $O(Q \log F)$ Parametric Slope Envelope |
| **P17** (`Advanced`) | `[NOI2010] 海拔` (Luogu P2046) | C2 P12 | Continuous Altitudes $h_v \in [0, 1]$ via Lovász Coarea Theorem & Planar Dual Shortest Path |
| **P18** (`Advanced`) | `AtCoder ARC 107 F — Sum of Abs` | C1 P12 | 3-State Sign Cut $\{-1, 0, +1\}$ on Connected Components via 2-Bit Submodular Chain |
| **P19** (`Advanced`) | `AtCoder AGC 038 F — Two Permutations` | C1 P13 | Permutation Cycle Decomposition & Rescuing Supermodularity via Bipartite Flip |
| **P20** (`Advanced`) | `[CTSC / Cow Loops / PERT Crashing Archetype]` | C2 P17 + Sec 3 | Critical Path & Cycle Compression with Piecewise Linear Costs & Residual Timestamps |
| **P21** (`Advanced`) | `[ICPC / UVa 1406 / Cyclic Volunteer Recruitment]` | C2 P15 | Circular-Ones Matrix Rescued via Parametric Midnight Flow $K = \sum_{i \in W} x_i$ & Ternary Search |
| **P22** (`Advanced`) | `[QOJ / CF 1067E Dual] Two-Tree Subtree Laminar Selection` | C2 P16 | Two Laminar Matroids Compiled via Hasse Out-Tree + In-Tree Bounded Circulation |
| **P23** (`Advanced`) | `AtCoder ABC 214 H — Collecting` | **C3 Gap-Hunt** | SCC Condensation, Node-Splitting Potential LP Dual & Topological Johnson Potentials |
| **P24** (`Advanced`) | `[WC2006] 水管局长` / `[HNOI2010] 城市建设` (Luogu P4174 / P3206) | **C3 Gap-Hunt** | Offline / Dynamic Inverse & Parametric MST via Matroid Contraction–Reduction |
| **P25** (`Mastery`) | `Codeforces 1427G — One Billion Shades of Grey` | C1 P16 & C2 P13 | Lovász Coarea Level-Set Cuts on Grid & $O(N^3)$ Incremental Residual Rollback |
| **P26** (`Mastery`) | `Codeforces 1284G — Seollal` | C1 P15 & C2 P18 | Chessboard Independent-Set Degree Bounds via Graphic $\cap$ Partition Matroid Intersection |
| **P27** (`Mastery`) | `Codeforces 1556H — DIY Tree` | C1 P14 & C2 P19 | FPT $2^{\binom{K}{2}}$ Core Forest Enumeration + Weighted Graphic $\cap$ Partition Matroid Intersection |
| **P28** (`Mastery`) | `[省选联考 2020 A 卷] 魔法商店` (Luogu P6621 / LOJ 3300) | C1 P17 | Inverse Linear Matroid Basis via XOR Exchange DAG & $L_2$ Isotonic Regression |
| **P29** (`Mastery`) | `[省选联考 2020 A 卷] 保序回归` (Luogu P6624 / LOJ 3303) | C1 P18 & C2 P20 | General $L_p$ Isotonic Regression via Submodular Level Cuts & Parallel Binary Search (`整体二分`) |
| **P30** (`Mastery`) | `AtCoder ARC 142 E — Pairing Wizards` | C1 P19 | Mandatory Baseline Raising, Bipartite Role Split & Unary Threshold Cut Chains |
| **P31** (`Mastery`) | `AtCoder AGC 031 E — Snuke the Phantom Thief` | C2 P21 | 2D Coordinate Prefix/Suffix Ranks Compiled to Two Laminar Slot Chains |
| **P32** (`Mastery`) | `[NOI2019] 序列` (Luogu P5470) & `UOJ 455 — [WC2019] 雪灾与外卖` | C1 P20 & C2 P22 | Complementary Slackness Residual Path Anatomy & Multi-Heap Simulated MCMF (`模拟费用流`) |

---

## 2. Explicit LP Primal–Dual Compilation (`LP对偶转网络流`)

### 2.1 The Algebraic Engine: Lagrangian Derivation & Master Primal–Dual Dictionary

In competitive programming, a vast family of optimization problems cannot be cast directly into a flow network because their natural decision variables represent **potentials, timestamps, prefix sums, or edge weight adjustments** rather than conserved quantities. Conversely, other problems naturally involve flow-like quantities but enforce **global interval or tree-path coverage constraints** where each variable participates in $O(N)$ inequalities instead of $2$ endpoints.

**Linear Programming (LP) Duality** is the universal compiler that translates between these two worlds. Let us derive the compilation dictionary from first principles using the **Lagrangian method**, so that no sign or inequality orientation is ever memorized by rote.

Consider a general **Primal Minimization LP** with $m$ constraints (split into $m_1$ inequalities and $m_2$ equalities) and $n$ variables (split into $n_1$ non-negative variables and $n_2$ free variables):

$$
\begin{aligned}
\min_{\mathbf{x}, \mathbf{z}} \quad & \mathbf{c}^\top \mathbf{x} + \mathbf{d}^\top \mathbf{z} \\
\text{s.t.} \quad & A_{11} \mathbf{x} + A_{12} \mathbf{z} \ge \mathbf{b}_1 \quad (\text{dual multiplier } \mathbf{y}_1 \ge \mathbf{0}) \\
& A_{21} \mathbf{x} + A_{22} \mathbf{z} = \mathbf{b}_2 \quad (\text{dual multiplier } \mathbf{y}_2 \in \mathbb{R}^{m_2} \text{ free}) \\
& \mathbf{x} \ge \mathbf{0}, \quad \mathbf{z} \in \mathbb{R}^{n_2} \text{ free}.
\end{aligned}
$$

To form a valid **lower bound** on the Primal objective for any primal-feasible $(\mathbf{x}, \mathbf{z})$, we multiply the $\ge \mathbf{b}_1$ inequalities by non-negative multipliers $\mathbf{y}_1 \ge \mathbf{0}$ (which preserves the $\ge$ direction) and the $=\mathbf{b}_2$ equalities by unconstrained real multipliers $\mathbf{y}_2 \in \mathbb{R}^{m_2}$. Summing these weighted constraints yields:

$$
(\mathbf{y}_1^\top A_{11} + \mathbf{y}_2^\top A_{21})\mathbf{x} + (\mathbf{y}_1^\top A_{12} + \mathbf{y}_2^\top A_{22})\mathbf{z} \ge \mathbf{b}_1^\top \mathbf{y}_1 + \mathbf{b}_2^\top \mathbf{y}_2.
$$

For the left-hand side to be bounded above by the Primal objective $\mathbf{c}^\top \mathbf{x} + \mathbf{d}^\top \mathbf{z}$ for *all* $\mathbf{x} \ge \mathbf{0}$ and *all* $\mathbf{z} \in \mathbb{R}^{n_2}$:
1. Since $\mathbf{x} \ge \mathbf{0}$, the coefficient vector on $\mathbf{x}$ cannot exceed $\mathbf{c}^\top$: $A_{11}^\top \mathbf{y}_1 + A_{21}^\top \mathbf{y}_2 \le \mathbf{c}$.
2. Since $\mathbf{z}$ is **free** (can be arbitrarily large positive or negative), any non-zero discrepancy between its coefficient and $\mathbf{d}^\top$ could be exploited to send the bound to $-\infty$. Thus its coefficient must match $\mathbf{d}^\top$ **with exact equality**: $A_{12}^\top \mathbf{y}_1 + A_{22}^\top \mathbf{y}_2 = \mathbf{d}$.

Maximizing this lower bound gives the **Dual Maximization LP**:

$$
\begin{aligned}
\max_{\mathbf{y}_1, \mathbf{y}_2} \quad & \mathbf{b}_1^\top \mathbf{y}_1 + \mathbf{b}_2^\top \mathbf{y}_2 \\
\text{s.t.} \quad & A_{11}^\top \mathbf{y}_1 + A_{21}^\top \mathbf{y}_2 \le \mathbf{c} \quad (\text{from } \mathbf{x} \ge \mathbf{0}) \\
& A_{12}^\top \mathbf{y}_1 + A_{22}^\top \mathbf{y}_2 = \mathbf{d} \quad (\text{from } \mathbf{z} \text{ free}) \\
& \mathbf{y}_1 \ge \mathbf{0}, \quad \mathbf{y}_2 \in \mathbb{R}^{m_2} \text{ free}.
\end{aligned}
$$

By the **Strong Duality Theorem** (von Neumann 1947; Gale–Kuhn–Tucker 1951), if both the Primal and Dual LPs are feasible, their optimal objective values coincide: $\text{OPT}_{\text{Primal}} = \text{OPT}_{\text{Dual}}$.

#### The "Sensible vs. Bizarre" Sign Mnemonic Table

In contest pressure, you never need to re-derive the signs if you classify every constraint and variable as **Tight (`=`)**, **Sensible** (the natural direction for the optimization sense: $\ge$ for $\min$, $\le$ for $\max$, $\ge 0$ for variables), or **Bizarre** (the opposite direction):

| Primal (Minimize $\mathbf{c}^\top \mathbf{x}$) | $\Longleftrightarrow$ | Dual (Maximize $\mathbf{b}^\top \mathbf{y}$) | Network Flow / Potential Interpretation |
| :--- | :---: | :--- | :--- |
| **Objective Coefficient Vector** $\mathbf{c}$ | $\leftrightarrow$ | **Constraint RHS Vector** $\mathbf{b}$ | Node Potential Demand $r_v \leftrightarrow$ Edge Cost $c_e$ |
| **Constraint RHS Vector** $\mathbf{b}$ | $\leftrightarrow$ | **Objective Coefficient Vector** $\mathbf{c}$ | Edge Length / Penalty $w_e \leftrightarrow$ Edge Cost / Capacity |
| **Constraint Matrix** $A$ ($m \times n$) | $\leftrightarrow$ | **Transposed Matrix** $A^\top$ ($n \times m$) | Difference Constraint Row $\leftrightarrow$ Directed Edge Column |
| **Tight Constraint** ($a_i^\top \mathbf{x} = b_i$) | $\leftrightarrow$ | **Free Variable** ($y_i \in \mathbb{R}$) | Flow Conservation $= 0 \leftrightarrow$ Unconstrained Node Potential $\pi_u \in \mathbb{R}$ |
| **Sensible Constraint** ($a_i^\top \mathbf{x} \ge b_i$) | $\leftrightarrow$ | **Sensible Variable** ($y_i \ge 0$) | Difference Inequality $\pi_v - \pi_u \ge w_e \leftrightarrow$ Non-negative Edge Flow $f_e \ge 0$ |
| **Bizarre Constraint** ($a_i^\top \mathbf{x} \le b_i$) | $\leftrightarrow$ | **Bizarre Variable** ($y_i \le 0$) | Upper Bound $\pi_v - \pi_u \le w_e \leftrightarrow$ Reverse Edge Flow $f_{v \to u} \ge 0$ |
| **Sensible Variable** ($x_j \ge 0$) | $\leftrightarrow$ | **Sensible Constraint** ($A_{\cdot,j}^\top \mathbf{y} \le c_j$) | Non-negative Flow $f_e \ge 0 \leftrightarrow$ Reduced Cost Feasibility $\pi_v - \pi_u \le c_e$ |
| **Free Variable** ($x_j \in \mathbb{R}$) | $\leftrightarrow$ | **Tight Constraint** ($A_{\cdot,j}^\top \mathbf{y} = c_j$) | Unconstrained Potential $\pi_u \in \mathbb{R} \leftrightarrow$ Exact Flow Conservation $\text{div}_f(u) = r_u$ |

---

### 2.2 The Column-Incidence Recognition Theorem

Why do difference constraints in node potentials dualize into network flows, and why do consecutive-ones / tree-path constraints in primal variables transform into network flows? Both phenomena are governed by a single structural theorem on the constraint matrix.

> [!IMPORTANT]
> **Theorem 2.1 (The Column-Incidence Recognition Theorem)**:
> Let $B \in \{0, +1, -1\}^{M \times N}$ be a constraint matrix.
> 1. **Primal Flow Space (Column-Incidence)**: $B$ is the node-arc incidence matrix of a directed graph $G = (V, E)$ with $|V| = M$ and $|E| = N$ if and only if **every column of $B$ contains at most one $+1$ and at most one $-1$** (with all other entries $0$). If a column $j$ has only a single $+1$ (at row $u$) or only a single $-1$ (at row $v$), adjoining a **redundant ground row** $r_0 = -\sum_{u=1}^M r_u$ completes column $j$ so that **every column has one $+1$ and one $-1$**, making $\widehat{B} = \begin{bmatrix} B \\ -\mathbf{1}^\top B \end{bmatrix}$ an exact Kirchhoff flow-conservation matrix $\widehat{B}\mathbf{f} = \mathbf{0}$.
> 2. **Dual Potential Space (Row-Incidence)**: If every **row** of $M \times N$ matrix $B$ contains at most one $+1$ and at most one $-1$ (i.e., $B\boldsymbol{\pi} \ge \mathbf{w}$ is a system of difference constraints $\pi_{v_e} - \pi_{u_e} \ge w_e$), then its transpose $B^\top$ satisfies condition (1): **every column of $B^\top$ has at most one $+1$ and at most one $-1$**. Therefore, the LP Dual of *any* linear program whose constraints are difference inequalities (and single-variable bounds $\pi_u \ge 0$ or $0 \le \pi_u - \pi_{u-1} \le u_u$) is **guaranteed** to be a pure Minimum-Cost Flow / Circulation problem!

---

### 2.3 Max-Flow / Min-Cut & MCMF / Elastic Potentials as Exact LP Duals

Let $G = (V, E)$ be a directed network with source $s$, sink $t$, capacities $u_e \ge 0$, and costs $c_e \in \mathbb{R}$.

#### Case A: Maximum $s$-$t$ Flow $\Longleftrightarrow$ Fractional Minimum $s$-$t$ Cut
Introduce a return edge $(t, s)$ with capacity $\infty$ so that flow conservation holds at **every** vertex $v \in V$.
- **Primal LP (Max-Flow)**:

$$
\max \quad f_{ts} \quad \text{s.t.} \quad \sum_{e \in \delta^+(v)} f_e - \sum_{e \in \delta^-(v)} f_e = 0 \;\; (\forall v \in V, \text{ dual } \pi_v \in \mathbb{R}), \qquad 0 \le f_e \le u_e \;\; (\forall e \in E, \text{ dual } \gamma_e \ge 0).
$$

- **Dual Compilation**:
  - For each normal edge $e = (u, v) \in E$, $f_e \ge 0$ has objective coefficient $0$. It appears with $+1$ in $\text{div}(u) = 0$ (dual $\pi_u$), $-1$ in $\text{div}(v) = 0$ (dual $\pi_v$), and $+1$ in $f_e \le u_e$ (dual $\gamma_e \ge 0$). Thus its dual constraint is:

    $$
    \pi_u - \pi_v + \gamma_e \ge 0 \iff \gamma_e \ge \pi_v - \pi_u.
    $$

  - For the return edge $f_{ts} \ge 0$, its objective coefficient is $+1$, and it has no capacity bound. Its dual constraint is:

    $$
    \pi_t - \pi_s \ge 1.
    $$

  - Since shifting all $\pi_v$ by a constant changes nothing, fix $\pi_s = 0$ and $\pi_t = 1$ (shifting $\pi_v \gets 1 - \pi_v$ gives the standard convention $\pi_s = 1, \pi_t = 0$, $\gamma_{uv} \ge \pi_u - \pi_v$).
- **Dual LP (Fractional Min-Cut)**:

$$
\min_{\boldsymbol{\pi}, \boldsymbol{\gamma}} \sum_{e=(u,v) \in E} u_e \gamma_e \quad \text{s.t.} \quad \gamma_{uv} \ge \pi_u - \pi_v \;\; (\forall (u,v) \in E), \quad \pi_s = 1, \; \pi_t = 0, \quad \gamma_e \ge 0.
$$

Because the incidence matrix is Totally Unimodular (Section 5), every extreme point of the Dual LP has $\pi_u \in \{0, 1\}$ and $\gamma_{uv} = \max(0, \pi_u - \pi_v) = [u \in S, v \in T]$, recovering the Ford–Fulkerson Max-Flow Min-Cut Theorem!

#### Case B: Minimum-Cost Flow (MCMF) $\Longleftrightarrow$ Elastic Node Potentials & Project Crashing
Consider the Primal Minimum-Cost Circulation / Demand Flow problem:

$$
\begin{aligned}
\min_{\mathbf{f}} \quad & \sum_{e=(u,v) \in E} c_e f_e \\
\text{s.t.} \quad & \sum_{e \in \delta^+(v)} f_e - \sum_{e \in \delta^-(v)} f_e = r_v \quad (\forall v \in V, \text{ dual } \pi_v \in \mathbb{R}) \\
& -f_e \ge -u_e \quad (\forall e \in E, \text{ dual } \gamma_e \ge 0) \\
& f_e \ge 0 \quad (\forall e \in E).
\end{aligned}
$$

Applying the Master Dictionary yields the **Dual Elastic Potential Problem**:

$$
\begin{aligned}
\max_{\boldsymbol{\pi}, \boldsymbol{\gamma}} \quad & \sum_{v \in V} r_v \pi_v - \sum_{e \in E} u_e \gamma_e \\
\text{s.t.} \quad & \pi_u - \pi_v - \gamma_{uv} \le c_{uv} \iff \pi_v - \pi_u + c_{uv} \ge -\gamma_{uv} \quad (\forall e=(u,v) \in E) \\
& \gamma_{uv} \ge 0, \quad \pi_v \in \mathbb{R}.
\end{aligned}
$$

Replacing $\pi_v \gets -\pi_v$ (so $\pi_v - \pi_u \le c_{uv} + \gamma_{uv}$ becomes the standard shortest-path potential inequality) shows the exact physical meaning of $\gamma_e$:
- If an edge $e = (u, v)$ is **uncapacitated** ($u_e = \infty$), $\gamma_e$ must be $0$ in any finite-objective solution, enforcing a **hard difference constraint** $\pi_v - \pi_u \le c_{uv}$.
- If an edge $e = (u, v)$ has **finite capacity** $u_e < \infty$, the dual variable $\gamma_e = \max(0, (\pi_v - \pi_u) - c_{uv}) \ge 0$ acts as an **elastic violation variable (soft constraint)** that allows $\pi_v - \pi_u$ to exceed $c_{uv}$ at a linear penalty rate of $u_e$ per unit of violation!

> [!TIP]
> **The Role Reversal Principle (Primal Potential vs. Dual Flow)**:
> When you formulate a problem in **Node Potential Space** (variables $\pi_v$, violation variables $\gamma_e$) and dualize it into **Network Flow Space** (flows $f_e$), the roles of **Cost** and **Capacity** swap:
> - **Potential Objective Coefficient** (e.g., unit crashing cost $u_e$ of violating a constraint by $\gamma_e$, or upper bound on $\gamma_e$) $\Longleftrightarrow$ **Dual Edge Capacity**!
> - **Potential Constraint RHS** (e.g., baseline edge duration / threshold $c_e$ in $\pi_v - \pi_u + \gamma_e \ge c_e$) $\Longleftrightarrow$ **Dual Edge Cost**!

---

### 2.4 The Universal 6-Line Recipe for Dualizing Potential LPs

Whenever a problem asks you to choose node values $p_1, \dots, p_n$ (potentials, prefix sums, altitudes, or timestamps) and edge violation / adjustment amounts $\gamma_e \ge 0$:

1. **Standardize the Potential LP**: Write the objective and all constraints so that every inequality has at most two potential variables $p_v - p_u$ (plus optional adjustment variables $\gamma_e$).
   - If the problem has constraints on sums of intervals $\sum_{i=l}^r x_i \ge c$, substitute **prefix potentials** $p_i = \sum_{k=1}^i x_k$ with $p_0 = 0$ so that $\sum_{i=l}^r x_i = p_r - p_{l-1}$ and $x_i = p_i - p_{i-1} \ge 0$.
2. **Assign One Non-Negative Dual Flow Variable per Inequality**:
   - Each difference inequality $p_v - p_u \ge w_e$ (in a $\min$ problem) or $p_v - p_u \le w_e$ (in a $\max$ problem) receives a directed edge flow variable $f_e \ge 0$.
   - Each single-variable bound $x_i = p_i - p_{i-1} \le u_i$ receives either a parallel reverse/slack edge flow variable $z_i \ge 0$, or directly bounds the capacity of a dual edge if $\gamma_e$ is an elastic variable.
3. **Read Off Node Conservation from Potential Columns**:
   - Each potential variable $p_i$ ($1 \le i \le n$) is a free (or non-negative) variable; its column in $A^\top$ yields flow conservation at vertex $i$: $\text{Inflow}(i) - \text{Outflow}(i) = \text{coeff}(p_i \text{ in objective})$.
4. **Adjoin the Ground Vertex $0$**:
   - Because every difference $p_v - p_u$ has one $+1$ and one $-1$, summing all node conservation equations and negating gives the exact conservation equation at the ground node $0$ (where $p_0 = 0$).
5. **Read Off Edge Capacities from Adjustment Columns $\gamma_e$**:
   - Every inequality of the form $p_v - p_u + \gamma_e \ge w_e$ where $\gamma_e \ge 0$ costs $u_e$ in the objective forces $0 \le f_e \le u_e$: the cost of $\gamma_e$ becomes the **capacity** of edge $e$!
6. **Eliminate Negative Costs / Convert Max-Cost to Min-Cost**:
   - Multiply the Dual maximization objective by $-1$ to get a standard **Minimum-Cost Circulation / MCMF** problem. If the graph is a DAG (or has negative-cost edges), either shift costs via topological DP potentials (Johnson's trick, Section 4.4) or use SPFA-based MCMF when no negative cycles exist.

---

### 2.5 The Fundamental Duality Identity of Interval Networks

In competitive programming, interval optimization problems appear in two seemingly opposite disguises:
- **Archetype 1 (`[NOI2008] 志愿者招募`, Column-Consecutive-Ones)**: Variables $x_j \ge 0$ correspond to **intervals** $[l_j, r_j]$ (volunteers), and constraints correspond to **points** $t \in \{1, \dots, n\}$ (days): $\sum_{j : t \in [l_j, r_j]} x_j \ge a_t$.
- **Archetype 2 (`[ZJOI2013] 防守战线`, Row-Consecutive-Ones)**: Variables $x_t \in [0, u_t]$ correspond to **points** $t \in \{1, \dots, n\}$ (towers), and constraints correspond to **intervals** $[l_j, r_j]$ (sensors): $\sum_{t=l_j}^{r_j} x_t \ge d_j$.

Cohorts 1 and 2 showed that both compile to the **exact same chain-plus-chords flow network topology**. Why? Because the two compilation techniques—**Primal Consecutive-Row Differencing** ($E_t - E_{t-1}$) and **Dual Prefix-Potential Substitution** ($p_t = \pi_t - \pi_{t-1}$)—are exact algebraic transposes of each other!

> [!IMPORTANT]
> **Theorem 2.2 (Fundamental Duality Identity of Interval Networks)**:
> Let $D \in \{0, +1, -1\}^{(n+1) \times n}$ be the $(n+1) \times n$ forward-difference matrix whose rows are $E'_1 = E_1$, $E'_t = E_t - E_{t-1}$ ($2 \le t \le n$), and $E'_{n+1} = -E_n$:
>
> $$
> D = \begin{bmatrix}
> +1 & 0 & \cdots & 0 \\
> -1 & +1 & \cdots & 0 \\
> 0 & -1 & \ddots & 0 \\
> \vdots & \vdots & \ddots & +1 \\
> 0 & 0 & \cdots & -1
> \end{bmatrix}_{(n+1) \times n}.
> $$
>
> Let $A \in \{0, 1\}^{n \times m}$ be a **Column-Consecutive-Ones** matrix where column $j$ is the indicator vector of interval $[l_j, r_j] \subseteq \{1, \dots, n\}$. Then:
> 1. **In Primal Space**: Left-multiplying the system $A\mathbf{x} - \mathbf{y} = \mathbf{a}$ by $D$ transforms each interval column $A_{\cdot, j}$ into $D A_{\cdot, j} = \mathbf{e}_{l_j} - \mathbf{e}_{r_j+1}$ (a directed edge $l_j \to r_j+1$), each slack column $-I_{\cdot, t}$ into $-\mathbf{e}_t + \mathbf{e}_{t+1}$ (a reverse backbone edge $t+1 \to t$), and the RHS $\mathbf{a}$ into supplies $D\mathbf{a} = (a_1, a_2 - a_1, \dots, -a_n)^\top$.
> 2. **In Dual Space**: The LP Dual of $\min\{\mathbf{c}^\top \mathbf{x} : A\mathbf{x} \ge \mathbf{a}, \mathbf{x} \ge \mathbf{0}\}$ is $\max\{\mathbf{a}^\top \boldsymbol{\pi} : A^\top \boldsymbol{\pi} \le \mathbf{c}, \boldsymbol{\pi} \ge \mathbf{0}\}$. Changing variables from point multipliers $\boldsymbol{\pi} \in \mathbb{R}_{\ge 0}^n$ to **prefix potentials** $\mathbf{p} = (p_0, p_1, \dots, p_n)^\top$ via $\boldsymbol{\pi} = -D^\top \mathbf{p}$ (i.e., $\pi_t = p_t - p_{t-1} \ge 0$ with $p_0 = 0$) transforms the dual constraint $\sum_{t=l_j}^{r_j} \pi_t \le c_j$ into $p_{r_j} - p_{l_j-1} \le c_j$ and the dual objective $\mathbf{a}^\top \boldsymbol{\pi}$ into $-\mathbf{a}^\top D^\top \mathbf{p} = -(D\mathbf{a})^\top \mathbf{p}$.
>
> Thus, **applying consecutive row subtraction $D$ in Primal space is the exact transpose of substituting prefix potentials $\boldsymbol{\pi} = -D^\top \mathbf{p}$ in Dual space**.

---

### 2.6 Complete 4-Step Compilation Scratchpad, Hand-Checkable Toy Trace & 3 Broken Gadget Counterexamples

Let us demonstrate the complete 4-Step Compilation on **`[ZJOI2013] 防守战线` (Defense Line, Luogu P3337)** ($n \le 1000$ positions, $m \le 10000$ intervals).

#### Step 1: Non-Graph Diagnostic Signal
- **Problem**: At each position $i \in \{1, \dots, n\}$, we can build at most one tower ($x_i \in \{0, 1\}$) at cost $c_i \ge 0$. We are given $m$ intervals $[l_j, r_j]$, each requiring $\sum_{i=l_j}^{r_j} x_i \ge d_j$. Minimize $\sum_{i=1}^n c_i x_i$.
- **Why DP / Greedy Fails**: Overlapping intervals create high-treewidth dependencies; $d_j$ can be up to $r_j - l_j + 1 \le 1000$, making bitmask or frontier DP impossible.
- **Diagnostic Signal**: The constraint matrix has **Row-Consecutive-Ones** ($\sum_{i=l_j}^{r_j} x_i \ge d_j$). Substituting prefix sums $p_i = \sum_{k=1}^i x_k$ turns every constraint into a **2-variable difference constraint** $p_{r_j} - p_{l_j-1} \ge d_j$. By Theorem 2.1, its LP Dual is a pure MCMF network on $n+1$ vertices!

#### Step 2: Intermediate Algebraic Representation (Primal LP $\to$ Dual LP)
Define prefix potentials $p_i = \sum_{k=1}^i x_k$ with $p_0 = 0$. The constraints on $x_i = p_i - p_{i-1}$ are $0 \le p_i - p_{i-1} \le 1$, and each interval requires $p_{r_j} - p_{l_j-1} \ge d_j$. Write every inequality in canonical $\ge$ form for a **Minimization LP**:

$$
\begin{aligned}
\min_{\mathbf{p}} \quad & \sum_{i=1}^n c_i (p_i - p_{i-1}) = -c_1 p_0 + \sum_{i=1}^{n-1} (c_i - c_{i+1}) p_i + c_n p_n \\
\text{s.t.} \quad & p_{r_j} - p_{l_j-1} \ge d_j \quad (\forall j \in \{1, \dots, m\}, \text{ dual } f_j \ge 0) \\
& p_i - p_{i-1} \ge 0 \quad (\forall i \in \{1, \dots, n\}, \text{ dual } y_i \ge 0) \\
& p_{i-1} - p_i \ge -1 \quad (\forall i \in \{1, \dots, n\}, \text{ dual } z_i \ge 0) \\
& p_0 = 0, \quad p_1, \dots, p_n \in \mathbb{R} \text{ free}.
\end{aligned}
$$

#### Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)
Apply the Master Primal–Dual Dictionary (Section 2.1):
1. **Dual Objective**:

   $$
   \max_{\mathbf{f}, \mathbf{y}, \mathbf{z} \ge \mathbf{0}} \sum_{j=1}^m d_j f_j - \sum_{i=1}^n 1 \cdot z_i \iff -\min \left( \sum_{i=1}^n 1 \cdot z_i - \sum_{j=1}^m d_j f_j \right).
   $$

2. **Dual Equality Constraints (one per free variable $p_i$, $1 \le i \le n$)**:
   In the Primal constraints, $p_i$ appears with $+1$ when an inequality has $+p_i$ (meaning the dual flow **enters** vertex $i$) and $-1$ when an inequality has $-p_i$ (meaning the dual flow **leaves** vertex $i$):

   $$
   \underbrace{\left( \sum_{j : r_j = i} f_j + y_i + z_{i+1} \right)}_{\text{Inflow}(i)} - \underbrace{\left( \sum_{j : l_j - 1 = i} f_j + y_{i+1} + z_i \right)}_{\text{Outflow}(i)} = \begin{cases} c_i - c_{i+1} & \text{if } 1 \le i < n, \\ c_n & \text{if } i = n. \end{cases}
   $$

   Adjoining the ground equation at $i = 0$ gives $\text{Inflow}(0) - \text{Outflow}(0) = -c_1$.
3. **Standardize to $\text{Outflow}(i) - \text{Inflow}(i) = b_i$**:
   Define net supply $b_0 = c_1$, $b_i = c_{i+1} - c_i$ ($1 \le i < n$), $b_n = -c_n$. Notice $\sum_{i=0}^n b_i = 0$. Each dual variable is a directed edge from its $-p_u$ endpoint to its $+p_v$ endpoint:
   - $f_j \ge 0$: Directed edge $(l_j - 1) \to r_j$, capacity $\infty$, min-cost $-d_j$ (max-cost $+d_j$).
   - $y_i \ge 0$: Directed edge $(i - 1) \to i$, capacity $\infty$, cost $0$.
   - $z_i \ge 0$: Directed edge $i \to (i - 1)$, capacity $\infty$, min-cost $+1$ (max-cost $-1$).

> [!NOTE]
> **Eliminating $z_i$ via Variable Substitution**: Notice that $y_i$ flows $(i-1) \to i$ with cost $0$ and $z_i$ flows $i \to (i-1)$ with supply shift $b_i = c_{i+1} - c_i$. Equivalently, if we instead retain $x_i \in [0, 1]$ as an elastic variable on the step $p_i - p_{i-1} - x_i = 0$, the Role Reversal Principle immediately turns $0 \le x_i \le 1$ with cost $c_i$ into a backbone edge $i \to i-1$ of **capacity $1$ and cost $c_i$**, avoiding negative demands! Both networks have the exact same optimum.

```
            f_j: cap = inf, cost = -d_j (or max-cost +d_j)
       +---------------------------------------------------+
       |                                                   v
     ( 0 ) ------> ( 1 ) ------> ( 2 ) ------> ... ------> ( n )
       ^    y_1:     ^    y_2:                 y_n:          |
       |   cap=inf   |   cap=inf              cap=inf        |
       |   cost=0    |   cost=0               cost=0         |
       +-------------+-------------+           ... <---------+
            z_1: cap=inf, cost=+1                   z_n: cap=inf, cost=+1
     Supplies b_i:  b_0 = c_1,  b_i = c_{i+1} - c_i,  b_n = -c_n
```

#### Step 4: Hand-Checkable Toy Trace & 3 Broken Gadget Counterexamples

**Toy Trace ($n = 3$)**:
- Costs: $c_1 = 10, c_2 = 2, c_3 = 8$.
- Intervals: $I_1 = [1, 2]$ with $d_1 = 1$; $I_2 = [2, 3]$ with $d_2 = 2$.
- **Primal Inspection**: $I_2 = [2, 3]$ has length $2$ and requires $d_2 = 2$, forcing $x_2 = 1$ and $x_3 = 1$. Then $I_1 = [1, 2]$ already gets $x_1 + x_2 \ge 0 + 1 = 1 = d_1$, so $x_1 = 0$. Optimal Primal cost: $c_2 + c_3 = 2 + 8 = 10$.
- **Dual Network Trace**:
  - Vertices $\{0, 1, 2, 3\}$ with supplies:
    - $b_0 = c_1 = 10$
    - $b_1 = c_2 - c_1 = 2 - 10 = -8$
    - $b_2 = c_3 - c_2 = 8 - 2 = +6$
    - $b_3 = -c_3 = -8$
    (Check: $10 - 8 + 6 - 8 = 0$; total positive supply $= 16$.)
  - Edges (using min-cost formulation, where $\text{OPT}_{\text{Primal}} = -\text{MinCost}$):
    - $y_1: 0 \to 1$, $y_2: 1 \to 2$, $y_3: 2 \to 3$ (all cap $\infty$, cost $0$).
    - $z_1: 1 \to 0$, $z_2: 2 \to 1$, $z_3: 3 \to 2$ (all cap $\infty$, cost $+1$).
    - $f_1: 0 \to 2$ (cap $\infty$, cost $-1$); $f_2: 1 \to 3$ (cap $\infty$, cost $-2$).
  - **Optimal Dual Flow**:
    1. Send $f_1 = 0$, $f_2 = 8$ on $1 \to 3$ (cost $8 \times (-2) = -16$).
    2. Now effective imbalances are: node $0$ has $+10$; node $1$ has $-8 - 8 = -16$; node $2$ has $+6$; node $3$ has $-8 + 8 = 0$.
    3. Send $y_1 = 10$ on $0 \to 1$ (cost $0$), and send $z_2 = 6$ on $2 \to 1$ (cost $6 \times (+1) = +6$).
    4. All supplies are balanced! Total Min-Cost $= -16 + 0 + 6 = -10 \implies \text{OPT}_{\text{Dual}} = -(-10) = 10$. Exact match!

**3 Broken Gadget Counterexamples**:
1. **Broken Gadget A (Omitting the $y_i: (i-1) \to i$ Slack Edges)**:
   Suppose we forget the primal constraint $p_i - p_{i-1} \ge 0$ ($x_i \ge 0$) and omit the edges $y_i: (i-1) \to i$. In the toy trace, node $0$ has supply $b_0 = +10$, and the only outgoing edge from $0$ is $f_1: 0 \to 2$. Force-routing $10$ units on $f_1$ and returning them via $z_2, z_1$ distorts the objective because the Primal LP is now allowed to set $x_1 < 0$ (negative towers at a refund of $c_1 = 10$)!
2. **Broken Gadget B (Reversing the Interval Edge to $r_j \to l_j - 1$)**:
   If we orient $f_j$ as $r_j \to l_j - 1$ instead of $(l_j - 1) \to r_j$, then $f_2: 3 \to 1$ forms a directed cycle $1 \xrightarrow{y_2} 2 \xrightarrow{y_3} 3 \xrightarrow{f_2} 1$ of total cost $0 + 0 - 2 = -2 < 0$ and infinite capacity! The dual objective diverges to $+\infty$ because we dualized $p_{l_j-1} - p_{r_j} \ge d_j$ ($\sum_{i=l_j}^{r_j} x_i \le -d_j$), which is **Primal Infeasible**.
3. **Broken Gadget C (Sign Error on the Upper-Bound Penalty $z_i$)**:
   If a solver writes $p_i - p_{i-1} \le 1$ with $+1$ instead of $-1$ in the Dual maximization objective ($\max \sum d_j f_j + \sum z_i$), then the 2-cycle $0 \xrightarrow{y_1} 1 \xrightarrow{z_1} 0$ has positive gain $+1$ per unit in the maximization problem, creating an infinite-gain cycle. Every upper bound $x_i \le u_i$ in a minimization problem **must** subtract $u_i z_i$ from the dual maximization objective.

---

## 3. Dualizing Difference Constraints (`差分约束系统的对偶`), Inverse Shortest Path, Inverse MST, and Critical Path Compression

### 3.1 Difference Constraints vs. Circulations: Bellman–Ford Feasibility as Farkas' Lemma

A **System of Difference Constraints** (`差分约束系统`) asks whether there exist real node potentials $\boldsymbol{\pi} = (\pi_1, \dots, \pi_n)^\top \in \mathbb{R}^n$ satisfying $m$ inequalities of the form:

$$
\pi_v - \pi_u \le w_e \quad \forall e = (u, v) \in E.
$$

Why does the **Bellman–Ford algorithm** solve this feasibility problem by checking for **negative-weight directed cycles**? Because a directed cycle is the exact **LP Dual (Farkas' Lemma certificate)** of a difference-constraint system!

> [!IMPORTANT]
> **Theorem 3.1 (Duality of Difference Constraints and Circulations)**:
> Consider the LP that tests feasibility of $\pi_v - \pi_u \le w_e$ by optimizing a zero objective:
>
> $$
> \text{Primal: } \quad \max_{\boldsymbol{\pi} \in \mathbb{R}^n} \; \mathbf{0}^\top \boldsymbol{\pi} \quad \text{s.t.} \quad \pi_v - \pi_u \le w_e \;\; (\forall e = (u, v) \in E).
> $$
>
> Assigning non-negative dual multipliers $f_e \ge 0$ to each inequality yields the **Dual Uncapacitated Circulation LP**:
>
> $$
> \text{Dual: } \quad \min_{\mathbf{f} \ge \mathbf{0}} \; \sum_{e \in E} w_e f_e \quad \text{s.t.} \quad \sum_{e \in \delta^-(v)} f_e - \sum_{e \in \delta^+(v)} f_e = 0 \;\; (\forall v \in V).
> $$
>
> By **Conformal Cycle Decomposition**, any circulation $\mathbf{f} \ge \mathbf{0}$ decomposes into a non-negative linear combination of simple directed cycles $C_1, \dots, C_k$. Therefore:
> 1. **Primal Feasible $\iff$ Dual Bounded ($\text{OPT} = 0$)**: Potentials $\boldsymbol{\pi}$ exist if and only if every directed cycle $C$ has $\sum_{e \in C} w_e \ge 0$.
> 2. **Primal Infeasible $\iff$ Dual Unbounded ($\text{OPT} = -\infty$)**: If a negative cycle $C$ ($\sum_{e \in C} w_e < 0$) exists, sending $f_e = M \to +\infty$ around $C$ drives the Dual objective to $-\infty$, and summing $\pi_v - \pi_u \le w_e$ around $C$ yields the impossible inequality $0 \le \sum_{e \in C} w_e < 0$.
> 3. **Soft / Elastic Difference Constraints**: When we allow each inequality to be violated by $\gamma_e \ge 0$ at cost $u_e$ per unit ($\pi_v - \pi_u - \gamma_e \le w_e$, $\min \sum u_e \gamma_e$), the Dual circulation acquires an **upper capacity bound** $0 \le f_e \le u_e$. Thus **minimizing total constraint violation to eliminate all negative cycles is the exact LP Dual of Minimum-Cost Circulation**!

---

### 3.2 Inverse Shortest Path & Shortest-Path Extension Duals

In the **Inverse / Parametric Shortest Path** problem (`CF 362E`, `CF 1307G`, or DAG Longest-Path Crashing), we are given a graph $G = (V, E)$ with initial edge weights $w_e \ge 0$ and adjustment costs $c_e > 0$. We want to increase edge weights by $\delta_e \ge 0$ so that the shortest $s$-$t$ path has length at least $D$ (at minimum cost $\sum c_e \delta_e$), or maximize the shortest $s$-$t$ path length subject to a total modification budget $\sum c_e \delta_e \le K$.

Let $\pi_v$ denote the shortest-path distance from $s$ to $v$ in the modified graph (with $\pi_s = 0$). A number $D$ is a lower bound on the shortest $s$-$t$ path length if and only if there exist potentials $\pi_v$ satisfying:

$$
\pi_v - \pi_u \le w_e + \delta_e \iff \pi_u - \pi_v + \delta_e \ge -w_e \quad \forall e = (u, v) \in E, \qquad \pi_t - \pi_s \ge D.
$$

#### Dualizing the Fixed-Target Version ($\min \sum_{e \in E} c_e \delta_e$ s.t. $\pi_t - \pi_s \ge D$)
Assign dual flow $f_e \ge 0$ to each edge inequality $\pi_u - \pi_v + \delta_e \ge -w_e$ and return flow $F \ge 0$ to $\pi_t - \pi_s \ge D$:

$$
\begin{aligned}
\max_{F, \mathbf{f} \ge \mathbf{0}} \quad & D \cdot F - \sum_{e \in E} w_e f_e \\
\text{s.t.} \quad & \text{div}_{\mathbf{f}}(v) = \begin{cases} F & \text{if } v = s, \\ -F & \text{if } v = t, \\ 0 & \text{otherwise}, \end{cases} \\
& 0 \le f_e \le c_e \quad (\forall e \in E).
\end{aligned}
$$

Look at the Dual objective: for any fixed $s$-$t$ flow value $F$, let $\text{MinCost}(F) = \min_{\mathbf{f}} \sum_{e \in E} w_e f_e$ be the minimum cost of sending $F$ units of flow from $s$ to $t$ where each edge $e$ has **capacity $c_e$** (the modification unit cost!) and **cost $w_e$** (the original edge length!). Then:
- **Fixed Target $D$**: Minimum modification cost $= \max_{F \ge 0} \big( D \cdot F - \text{MinCost}(F) \big)$, which is achieved by augmenting along all shortest $s$-$t$ residual paths of length $< D$!
- **Fixed Budget $K$ (`CF 1307G`, Section 4.3)**: By switching the role of objective and constraint (or taking the Lagrangian dual with multiplier $F$), the maximum achievable shortest-path distance from $s$ to $t$ under total modification budget $\sum_{e} c_e \delta_e \le K$ is:

  $$
  D^*(K) = \min_{F > 0} \frac{\text{MinCost}(F) + K}{F}.
  $$

---

### 3.3 The Inverse MST Spectrum: Symmetric, Asymmetric, and Dynamic Matroid Contraction–Reduction

Given an undirected connected graph $G = (V, E)$ with initial edge weights $w_e$ and a designated spanning tree $T \subseteq E$, when is $T$ a **Minimum Spanning Tree (MST)** of $G$ under modified weights $w'_e$?

By the **Matroid Cycle Property (Fundamental Cycle Optimality Condition)**, removing any tree edge $f \in T$ partitions $T$ into two connected components, and adding any non-tree edge $e = (u, v) \in E \setminus T$ creates a unique **fundamental cycle** $C_e \subseteq T \cup \{e\}$ consisting of $e$ and the unique tree path $P_T(u, v) \subseteq T$. The tree $T$ is an MST under weights $w'$ **if and only if** every non-tree edge $e \in E \setminus T$ is at least as heavy as every tree edge $f \in P_T(u, v)$ on its fundamental cycle:

$$
w'_f \le w'_e \quad \forall e = (u, v) \in E \setminus T, \;\; \forall f \in P_T(u, v).
$$

 notice that if we **decrement** tree edge weights by $x_f \ge 0$ ($w'_f = w_f - x_f$) and **increment** non-tree edge weights by $y_e \ge 0$ ($w'_e = w_e + y_e$)—since increasing a tree edge or decreasing a non-tree edge never helps $T$ become an MST—the condition becomes a pure **bipartite difference/sum constraint** between $T$ and $E \setminus T$:

$$
x_f + y_e \ge w_f - w_e \stackrel{\text{def}}{=} \Delta_{f,e} \quad \forall e \in E \setminus T, \;\; \forall f \in P_T(u_e, v_e) \quad (\text{whenever } \Delta_{f,e} > 0).
$$

#### The 3 Canonical Regimes of Inverse MST in Competitive Programming

| Regime & Representative Problem | Modification Costs & Bounds | Primal LP Formulation | Dual Graph / Matroid Compilation |
| :--- | :--- | :--- | :--- |
| **1. Symmetric Unit-Cost Unbounded** (`[SHOI2004] 最小生成树`, Luogu P4412) | Cost $1$ per unit change on any edge; unbounded adjustments $x_f, y_e \ge 0$. | $\min \sum_{f \in T} x_f + \sum_{e \notin T} y_e$ s.t. $x_f + y_e \ge \Delta_{f,e}$. | **Maximum Weight Bipartite Matching (KM / Kuhn–Munkres)** on $T \times (E \setminus T)$ with edge weights $\max(0, \Delta_{f,e})$: $\max \sum \Delta_{f,e} z_{f,e}$ s.t. $\sum_e z_{f,e} \le 1, \sum_f z_{f,e} \le 1$. Optimal modifications $x_f^*, y_e^*$ are the **KM vertex labels**! |
| **2. Asymmetric Weighted & Bounded** (`[BZOJ 3118] Orz the Immortal`) | Tree decrease costs $c_f$ (up to bound $u_f$); non-tree increase costs $c_e$ (up to bound $u_e$). | $\min \sum_{f \in T} c_f x_f + \sum_{e \notin T} c_e y_e$ s.t. $x_f + y_e \ge \Delta_{f,e}$, $0 \le x_f \le u_f$, $0 \le y_e \le u_e$. | **Capacitated Bipartite MCMF**: Source $S \to f \in T$ (cap $c_f$, cost $0$), $f \to e \in E \setminus T$ (cap $\infty$, cost $-\Delta_{f,e}$), $e \to T_{\text{snk}}$ (cap $c_e$, cost $0$), plus bound penalty edges if $u_f, u_e < \infty$. |
| **3. Offline / Dynamic Inverse & Parametric MST** (`[WC2006] 水管局长` / `[HNOI2010] 城市建设`) | $Q$ offline weight updates / deletions on $G$ ($N, M, Q \le 5 \times 10^4$). | Maintain MST / bottleneck spanning tree across time segments $[L, R]$. | **CDQ Divide-and-Conquer + Matroid Contraction–Reduction**: At node $[L, R]$ with $k = R - L + 1$ dynamic edges: (1) **Contract** (`Contraction`): set dynamic edges to $-\infty$, run Kruskal; static edges still in MST are **mandatory** (contract their endpoints). (2) **Reduce** (`Reduction`): set dynamic edges to $+\infty$, run Kruskal; static edges not in MST are **useless** (delete them). Graph shrinks to $\le k+1$ vertices and $\le 2k$ edges! |

---

### 3.4 Critical Path & Loop Compression (`PERT/CPM Crashing` & `Cow Loops`)

In **Project Management (PERT/CPM Crashing)** on a DAG $G = (V, E)$ (or a general directed graph with positive cycles in `Cow Loops`), each vertex $u$ has a timestamp $t_u \in \mathbb{R}$. Each directed edge $e = (u, v) \in E$ represents a precedence constraint $t_v - t_u \ge d_e - \gamma_e$, where $d_e$ is the baseline duration and $\gamma_e \in [0, m_e]$ is the **crashing (compression) amount**, costing $c_e \ge 0$ per unit of time compressed.

#### 1. Compressing the Critical Path (Makespan $\le T_{\max}$)
We want $t_{\text{snk}} - t_{\text{src}} \le T_{\max}$ at minimum crashing cost $\sum_{e \in E} c_e \gamma_e$:

$$
\begin{aligned}
\min_{\mathbf{t}, \boldsymbol{\gamma}} \quad & \sum_{e \in E} c_e \gamma_e \\
\text{s.t.} \quad & t_v - t_u + \gamma_e \ge d_e \quad (\forall e = (u, v) \in E, \text{ dual } f_e \ge 0) \\
& t_{\text{src}} - t_{\text{snk}} \ge -T_{\max} \quad (\text{dual } F \ge 0) \\
& -\gamma_e \ge -m_e \quad (\forall e \in E, \text{ dual } z_e \ge 0) \\
& \gamma_e \ge 0, \quad t_v \in \mathbb{R}.
\end{aligned}
$$

Dualizing via Section 2.4 yields:

$$
\max_{F, \mathbf{f}, \mathbf{z} \ge \mathbf{0}} \; \sum_{e \in E} d_e f_e - T_{\max} F - \sum_{e \in E} m_e z_e \quad \text{s.t.} \quad \text{div}_{\mathbf{f}}(v) = \begin{cases} F & v = \text{src}, \\ -F & v = \text{snk}, \\ 0 & \text{otherwise}, \end{cases} \quad f_e - z_e \le c_e.
$$

Look closely at the constraint $f_e - z_e \le c_e$ with objective contribution $d_e f_e - m_e z_e$:
- For the first $c_e$ units of flow on edge $e = (u, v)$ ($0 \le f_e \le c_e$), we set $z_e = 0$, earning $+d_e$ per unit of flow (min-cost $-d_e$).
- Once $f_e > c_e$, we must set $z_e = f_e - c_e$, so each additional unit of flow above $c_e$ earns $(d_e - m_e)$ per unit (min-cost $-(d_e - m_e)$)!
- **Mechanical Graph Compilation**: Every precedence constraint $t_v - t_u + \gamma_e \ge d_e$ with $\gamma_e \in [0, m_e]$ and unit crashing cost $c_e$ compiles into **two parallel directed edges** from $u$ to $v$:
  1. **compressible edge** $e^{(1)}: u \to v$ with **capacity $c_e$** and **min-cost $-d_e$**;
  2. **incompressible floor edge** $e^{(2)}: u \to v$ with **capacity $\infty$** and **min-cost $-(d_e - m_e)$** (representing the irreducible minimum duration $d_e - m_e$ once $\gamma_e$ hits its limit $m_e$!).
- **Piecewise-Linear Convex Crashing Curves**: More generally, if compressing edge $e$ has $K$ progressively more expensive regimes—regime $k$ allowing up to $m_{e,k}$ compression at marginal cost $c_{e,1} < c_{e,2} < \dots < c_{e,K}$—then in the Dual network, edge $e$ simply becomes **$K+1$ parallel edges** with capacities $c_{e,1}, c_{e,2} - c_{e,1}, \dots, c_{e,K} - c_{e,K-1}, \infty$ and min-costs $-d_e, -(d_e - m_{e,1}), \dots, -(d_e - \sum_{k=1}^K m_{e,k})$!

---

## 4. Complementary Slackness (`互补松弛定理`) & Recovering Dual Potentials $\pi^*$, Cut Partitions, and Primal Schedules

Solving the Dual flow network gives the optimal objective value $\text{OPT}_{\text{Primal}} = \text{OPT}_{\text{Dual}}$. However, many problems (`[SHOI2004] 最小生成树`, `[LOJ 6079]`, `AGC 043D`, `CF 1288F`, PERT Crashing) require outputting the **explicit Primal variables** (modified edge weights $w'_e$, node timestamps $t_v$, or interval schedules) or answering $Q \le 10^5$ parametric queries (`CF 1307G`, `ABC 214H`). The mathematical bridge that reconstructs Primal variables from a Dual residual graph is **Complementary Slackness (`互补松弛定理`)**.

### 4.1 The 4-Way Equivalence Theorem & Duality Gap Decomposition Proof

Consider the Primal Minimum-Cost Circulation problem ($\min \sum_{e \in E} c_e f_e$ s.t. $\text{div}_{\mathbf{f}}(v) = 0$ and $0 \le f_e \le u_e$) and its Dual Potential problem ($\max -\sum_{e \in E} u_e \gamma_e$ s.t. $\gamma_{uv} \ge \pi_u - \pi_v - c_{uv}$ and $\gamma_e \ge 0$). For any node potentials $\boldsymbol{\pi} \in \mathbb{R}^V$, define the **reduced cost** (`约化费用`) of directed edge $e = (u, v)$ as:

$$
c_{\boldsymbol{\pi}}(u, v) \stackrel{\text{def}}{=} c_{uv} - \pi_u + \pi_v.
$$

> [!IMPORTANT]
> **Theorem 4.1 (The 4-Way Equivalence Theorem for MCMF Optimality)**:
> Let $\mathbf{f}$ be a feasible circulation ($0 \le f_e \le u_e$, $\text{div}_{\mathbf{f}} = \mathbf{0}$). The following four conditions are equivalent:
> 1. **Primal Optimality**: $\mathbf{f}$ is a minimum-cost circulation.
> 2. **No Negative Residual Cycles**: The residual network $G_{\mathbf{f}}$ contains no directed cycle of strictly negative total cost.
> 3. **Existence of Feasible Residual Potentials**: There exist node potentials $\boldsymbol{\pi} \in \mathbb{R}^V$ such that every residual edge $e_{\text{res}} = (u, v) \in E(G_{\mathbf{f}})$ with positive residual capacity $u_{\mathbf{f}}(e_{\text{res}}) > 0$ has **non-negative reduced cost** $c_{\boldsymbol{\pi}}(u, v) \ge 0$.
> 4. **Complementary Slackness (The Reduced Cost Trichotomy)**: There exist node potentials $\boldsymbol{\pi} \in \mathbb{R}^V$ such that for every original edge $e = (u, v) \in E$:
>
>    $$
>    \begin{aligned}
>    f_e < u_e &\implies c_{\boldsymbol{\pi}}(u, v) \ge 0 \quad (\text{forward residual edge } u \to v \text{ has cost } \ge 0), \\
>    f_e > 0 &\implies c_{\boldsymbol{\pi}}(u, v) \le 0 \quad (\text{backward residual edge } v \to u \text{ has cost } -c_{\boldsymbol{\pi}}(u,v) \ge 0), \\
>    0 < f_e < u_e &\implies c_{\boldsymbol{\pi}}(u, v) = 0 \quad (\text{both } u \to v \text{ and } v \to u \text{ are in } G_{\mathbf{f}}, \text{ forcing } c_{\boldsymbol{\pi}}(u, v) = 0).
>    \end{aligned}
>    $$

**Proof via Duality Gap Decomposition**:
For any feasible circulation $\mathbf{f}$ (where $\sum_{e=(u,v)} (\pi_u - \pi_v) f_e = \sum_v \pi_v \text{div}_{\mathbf{f}}(v) = 0$) and any dual-feasible $(\boldsymbol{\pi}, \boldsymbol{\gamma})$ (where $c_{\boldsymbol{\pi}}(e) + \gamma_e \ge 0$ and $\gamma_e \ge 0$), the **Duality Gap** decomposes into a sum of non-negative terms over all edges:

$$
\text{Gap}(\mathbf{f}, \boldsymbol{\pi}, \boldsymbol{\gamma}) = \sum_{e \in E} c_e f_e - \left( -\sum_{e \in E} u_e \gamma_e \right) = \sum_{e \in E} \Big[ \underbrace{\big(c_{\boldsymbol{\pi}}(e) + \gamma_e\big)}_{\ge 0} \underbrace{f_e}_{\ge 0} + \underbrace{(u_e - f_e)}_{\ge 0} \underbrace{\gamma_e}_{\ge 0} \Big] \ge 0.
$$

Strong Duality ($\text{Gap} = 0$) holds if and only if for every $e \in E$:
- $(c_{\boldsymbol{\pi}}(e) + \gamma_e) f_e = 0$: if $f_e > 0$, then $c_{\boldsymbol{\pi}}(e) = -\gamma_e \le 0$;
- $(u_e - f_e) \gamma_e = 0$: if $f_e < u_e$, then $\gamma_e = 0 \implies c_{\boldsymbol{\pi}}(e) \ge 0$.
And by Theorem 3.1, potentials $\boldsymbol{\pi}$ satisfying $c_{\boldsymbol{\pi}}(e_{\text{res}}) \ge 0$ on $G_{\mathbf{f}}$ exist if and only if $G_{\mathbf{f}}$ has no negative cycles! $\blacksquare$

---

### 4.2 Post-Augmentation Residual SPFA Contract & The 3 Classic Engineering Pitfalls

Suppose your Primal problem had node potentials $p_v$ satisfying $p_v - p_u \le c_{uv}$ (on uncapacitated dual edges $e = (u, v)$ with capacity $\infty$), and you solved the Dual MCMF to obtain an optimal flow $\mathbf{f}^*$. How do you extract $p_v^*$ in code?

By Theorem 4.1(3), in the **final residual graph $G_{\mathbf{f}^*}$** (containing only edges with residual capacity $u_{\mathbf{f}^*}(u, v) > 0$), if we compute shortest-path distances $\text{dist}[v]$ so that the triangle inequality holds on every residual edge:

$$
\text{dist}[v] \le \text{dist}[u] + c_{\text{res}}(u, v) \iff \text{dist}[v] - \text{dist}[u] \le c_{\text{res}}(u, v),
$$

then setting $\pi^*_v = \text{dist}[v]$ (or $p^*_v = -\text{dist}[v]$ depending on whether the Primal constraint was $p_v - p_u \le c_{uv}$ or $p_u - p_v \le c_{uv}$) satisfies **all** Complementary Slackness conditions simultaneously!

```
   +-----------------------------------------------------------------------+
   |          VIRTUAL SUPER-ROOT Q RESIDUAL SPFA CONTRACT                  |
   +-----------------------------------------------------------------------+
   | 1. Run MCMF to optimality to obtain final residual graph G_{f*}.      |
   | 2. Create virtual super-root Q with 0-cost edges Q -> v for ALL v:    |
   |    Initialize dist[v] = 0 and in_queue[v] = true for ALL v in V!      |
   | 3. Run 1 pass of Bellman-Ford / SPFA using ONLY residual edges        |
   |    with residual capacity u_{f*}(u, v) > 0.                           |
   | 4. Shift by reference node: p*[v] = dist[v] - dist[ground_node].      |
   +-----------------------------------------------------------------------+
```

> [!CAUTION]
> **The 3 Classic Engineering Pitfalls When Recovering Dual Potentials**:
> 1. **Pitfall 1 (Using the Last Pre-Augmentation Dijkstra Potentials)**:
>    In Primal–Dual Dijkstra MCMF, the array `h[v]` stores shortest-path distances *before* the last augmentation (or before `SPFA` terminates when `dist[T] == INF`). After augmenting along the final shortest path $P$, newly saturated edges disappear from $G_{\mathbf{f}^*}$, so `h[v]` may violate Complementary Slackness on the final state. Always run **one final pass** on $G_{\mathbf{f}^*}$ *after* the last flow augmentation!
> 2. **Pitfall 2 (Running SPFA Only from Source $S$ — The `dist[v] = INF` Disconnection Trap)**:
>    At optimum $\mathbf{f}^*$, the minimum cut between $S$ and $T$ is saturated, so $T$ (and often many internal vertices) is **unreachable** from $S$ in $G_{\mathbf{f}^*}$! If you initialize `dist[S] = 0` and `dist[v] = +INF` for $v \neq S$, unreachable vertices stay at `+INF`, producing garbage potentials. Initializing `dist[v] = 0` and pushing **all** $v \in V$ into the SPFA queue is equivalent to connecting a virtual super-root $Q \to v$ with cost $0$, ensuring every component of $G_{\mathbf{f}^*}$ receives finite, valid potentials!
> 3. **Pitfall 3 (Stopping MCMF at Cost $\ge 0$ Without Tying $\pi(S) = \pi(T)$)**:
>    In problems like `[SHOI2004] 最小生成树` where dual flow is augmented from $S$ to $T$ only while shortest-path cost $< 0$ (stopping as soon as the shortest $S \to T$ path has cost $\ge 0$), the implicit primal constraint being enforced is that no $S \to T$ path has negative reduced cost relative to $\pi(S) = \pi(T) = 0$. To enforce $\pi(S) = \pi(T)$ during the post-augmentation SPFA, add a **bidirectional 0-cost residual link** $S \leftrightarrow T$ (or fix $\text{dist}[S] = \text{dist}[T] = 0$) when relaxing $G_{\mathbf{f}^*}$.

---

### 4.3 Parametric LP Duality & The $O(Q \log F)$ Residual Slope Envelope (`CF 1307G`)

Consider **`Codeforces 1307G — Cow and Exercise`**: we are given a directed graph $G = (V, E)$ ($N \le 50$, $M \le N(N-1)$) with edge weights $w_e \ge 1$, and $Q \le 10^5$ queries. Each query gives a budget $x_q \in [0, 10^5]$; we may increase each edge weight $w_e$ by $\delta_e \ge 0$ subject to $\sum_{e \in E} \delta_e \le x_q$ to maximize the shortest path from $1$ to $N$.

By our derivation in **Section 3.2** (with unit modification costs $c_e = 1$, so each edge has **capacity $1$** and **cost $w_e$** in the Dual MCMF network), for any integer flow value $F \in \{1, 2, \dots, F_{\max}\}$ (where $F_{\max} \le N - 1 \le 49$ is the max-flow from $1$ to $N$), let $C(F) = \text{MinCost}(F)$ be the minimum cost to send $F$ units of flow from $1$ to $N$. Because successive shortest paths have non-decreasing lengths, $C(F)$ is convex, and the minimum over all continuous $F > 0$ is attained at an **integer** breakpoint $F \in \{1, \dots, F_{\max}\}$:

$$
\text{Ans}(x_q) = \min_{F \in \{1, 2, \dots, F_{\max}\}} \frac{C(F) + x_q}{F} = \min_{F \in \{1, \dots, F_{\max}\}} \left( \frac{1}{F} \cdot x_q + \frac{C(F)}{F} \right).
$$

- **Why $O(Q \log F)$ Works**: Each integer flow step $F \in \{1, \dots, F_{\max}\}$ records a single pair $(F, C(F))$ during the SSP (Successive Shortest Path) MCMF run. This defines a lower envelope of at most $F_{\max} \le 50$ linear functions $L_F(x) = \frac{1}{F} x + \frac{C(F)}{F}$ with strictly decreasing slopes $1/F$. We can answer each query $x_q$ in $O(\log F_{\max})$ time via binary search on the lower convex hull (or $O(F_{\max})$ directly since $F_{\max} \le 50$)!

---

### 4.4 SCC Condensation, Node-Splitting Potentials & Primal Schedule Reconstruction (`ABC 214H`, `LOJ 6079`)

#### 1. `AtCoder ABC 214 H — Collecting` (SCC Condensation + Topological Johnson Potentials)
- **Problem**: A directed graph with $N \le 2 \times 10^5$ vertices, $M \le 2 \times 10^5$ edges, $K \le 10$ tokens starting at vertex $1$, and vertex values $A_v \ge 0$. Each token walks along a directed path; if **at least one** token visits vertex $v$, we collect $A_v$ once. Maximize total value collected.
- **LP Dual / Flow Compilation**:
  1. Contract Strongly Connected Components (SCCs) into a DAG where each SCC $C$ has weight $W_C = \sum_{v \in C} A_v$.
  2. Split each SCC $C$ into $C_{\text{in}} \to C_{\text{out}}$ with two parallel edges: one of **capacity $1$ and cost $-W_C$** (collecting the reward for the first token), and one of **capacity $\infty$ and cost $0$** (allowing subsequent tokens to pass through for free).
  3. Because $N, M \le 2 \times 10^5$ and $K \le 10$, we cannot run SPFA $K$ times on negative costs if it takes $O(NM)$. Instead, because the condensed graph is a **DAG**, we compute initial **Johnson node potentials** $\pi_v$ in $O(N + M)$ time via **topological DP** ($\pi_v = \min_{u \to v} (\pi_u + c_{uv})$) before the first flow augmentation! Then all $K \le 10$ augmentations use pure **Dijkstra** in $O(K (N + M) \log N)$ time!

#### 2. Recovering Primal Binary Schedules (`[LOJ 6079] Delight for a Cat`)
When a primal variable $x_i \in \{0, 1\}$ is compiled via consecutive equation subtraction $D A \mathbf{x} = \mathbf{0}$ (Section 2.5) into a **capacity-$1$ chord edge** $e_i$ in the Primal flow network, no SPFA is even needed: by integer flow integrality, the optimal $0$-$1$ value of $x_i^*$ is **directly equal to the final flow $f^*(e_i) \in \{0, 1\}$ on edge $e_i$**!

---

### 4.5 Hand-Checkable Toy Traces: Inverse MST Triangle Weight Recovery & DAG Crashing Timestamps

#### Trace 1: Inverse MST Weight Recovery (`[SHOI2004] 最小生成树` on a Triangle)
- **Graph**: Vertices $\{1, 2, 3\}$. Designated tree $T = \{f_1 = (1, 2), f_2 = (2, 3)\}$ with weights $w(f_1) = 10, w(f_2) = 8$. Non-tree edge $e_1 = (1, 3)$ with weight $w(e_1) = 4$.
- **Primal Inequalities**: $e_1 = (1, 3)$ spans $P_T(1, 3) = \{f_1, f_2\}$, requiring:
  - $x_{f_1} + y_{e_1} \ge 10 - 4 = 6$,
  - $x_{f_2} + y_{e_1} \ge 8 - 4 = 4$.
- **Optimal Solution**: Clearly it is cheaper to raise $y_{e_1} = 6$ (total cost $6$, making $w'(e_1) = 10 \ge \max(10, 8)$) than to lower both $f_1$ and $f_2$ ($6 + 4 = 10$).
- **Dual Network & Residual SPFA Trace**:
  - Bipartite network: $S \to f_1$ (cap $1$, cost $0$), $S \to f_2$ (cap $1$, cost $0$); $f_1 \to e_1$ (cap $\infty$, cost $-6$), $f_2 \to e_1$ (cap $\infty$, cost $-4$); $e_1 \to T_{\text{snk}}$ (cap $1$, cost $0$).
  - **MCMF Augmentation**: The shortest path is $S \to f_1 \to e_1 \to T_{\text{snk}}$ with flow $1$ and cost $-6$. Now $e_1 \to T_{\text{snk}}$ is saturated!
  - **Final Residual Graph $G_{\mathbf{f}^*}$** (with $S \leftrightarrow T_{\text{snk}}$ tied at $\text{dist}[S] = \text{dist}[T_{\text{snk}}] = 0$):
    - $f_1 \to S$ (cost $0$), $S \to f_2$ (cost $0$);
    - $f_1 \to e_1$ (cost $-6$) and $e_1 \to f_1$ (cost $+6$);
    - $f_2 \to e_1$ (cost $-4$);
    - $T_{\text{snk}} \to e_1$ (cost $0$).
  - **SPFA Relaxation from $\text{dist}[S] = \text{dist}[T_{\text{snk}}] = 0$**:
    - $\text{dist}[f_2] = 0$ (via $S \to f_2$);
    - $\text{dist}[e_1] = \min(0 + (-4) \text{ from } f_2, \; 0 \text{ from } T_{\text{snk}}) = -4$... wait: from $e_1 \to f_1 \to S$, we have $0 = \text{dist}[S] \le \text{dist}[f_1] + 0 \le \text{dist}[e_1] + 6$, which forces $\text{dist}[e_1] = -6$ and $\text{dist}[f_1] = 0$!
    - Let's check all residual edges with $\text{dist}[S] = 0, \text{dist}[T_{\text{snk}}] = 0, \text{dist}[f_1] = 0, \text{dist}[f_2] = 0, \text{dist}[e_1] = -6$:
      - $f_1 \to e_1$: $\text{dist}[e_1] = -6 \le \text{dist}[f_1] - 6 = -6$ (Tight!);
      - $e_1 \to f_1$: $\text{dist}[f_1] = 0 \le \text{dist}[e_1] + 6 = 0$ (Tight!);
      - $f_2 \to e_1$: $\text{dist}[e_1] = -6 \le \text{dist}[f_2] - 4 = -4$ (Valid!);
      - $T_{\text{snk}} \to e_1$: $\text{dist}[e_1] = -6 \le \text{dist}[T_{\text{snk}}] + 0 = 0$ (Valid!).
    - Recovering Primal variables: $x_{f_1}^* = -\text{dist}[f_1] = 0$, $x_{f_2}^* = -\text{dist}[f_2] = 0$, $y_{e_1}^* = -\text{dist}[e_1] = 6$. Total modification $= 0 + 0 + 6 = 6$, and modified weights are $w'(f_1) = 10, w'(f_2) = 8, w'(e_1) = 4 + 6 = 10$. Exact match!

---

## 5. Totally Unimodular (TU) Matrices, Hoffman–Kruskal Theorem, Ghouila–Houri Bicoloring, Consecutive-Ones Property (`连续1性质`), and Tree-Path Network Matrices

### 5.1 Total Unimodularity & Proof of the Hoffman–Kruskal Integrality Theorem

Why does an LP relaxation of a combinatorial problem sometimes return an **exact $0$-$1$ or integer solution** without Branch-and-Bound, and why does every such problem in competitive programming reduce to a flow or matching network?

**Definition 5.1 (Totally Unimodular Matrix)**:
A matrix $A \in \{-1, 0, +1\}^{m \times n}$ is **Totally Unimodular (TU)** (`全幺模矩阵`) if every square submatrix $B$ of $A$ (of any dimension $k \times k$, $1 \le k \le \min(m, n)$) has determinant:

$$
\det(B) \in \{-1, 0, +1\}.
$$

**Closure Properties of TU Matrices**:
A matrix $A$ remains TU under: (1) **Transposition** ($A^\top$), (2) **Adjoining Identity Matrices** ($[A \mid I_m]$ and $[A \mid -I_m]$), (3) **Multiplying any row or column by $-1$**, (4) **Permuting or duplicating rows/columns**, and (5) **Pivoting (Schur complement)** on any non-zero $\pm 1$ entry.

> [!IMPORTANT]
> **Theorem 5.1 (Hoffman–Kruskal Theorem, 1956)**:
> Let $A \in \{-1, 0, +1\}^{m \times n}$. The polyhedron
>
> $$
> P(\mathbf{a}, \mathbf{b}, \mathbf{l}, \mathbf{u}) = \big\{ \mathbf{x} \in \mathbb{R}^n : \mathbf{a} \le A\mathbf{x} \le \mathbf{b}, \; \mathbf{l} \le \mathbf{x} \le \mathbf{u} \big\}
> $$
>
> is an **integral polyhedron** (every vertex / extreme point $\mathbf{x}^* \in \mathbb{Z}^n$) for **all** integer bound vectors $\mathbf{a}, \mathbf{b} \in \mathbb{Z}^m$ and $\mathbf{l}, \mathbf{u} \in \mathbb{Z}^n$ **if and only if** $A$ is **Totally Unimodular**.
> Furthermore, when $A$ is TU and $\mathbf{c} \in \mathbb{Z}^n$, **both** the Primal LP and its Dual LP possess integral optimal extreme points (Total Dual Integrality, TDI).

**Proof of Sufficiency via Cramer's Rule**:
Add slack variables $\mathbf{s} \ge \mathbf{0}$ to write the system in standard equality form $\widetilde{A} \widetilde{\mathbf{x}} = \widetilde{\mathbf{b}}$, where $\widetilde{A}$ is formed from $A$ and identity columns $\pm I$, so $\widetilde{A}$ is also TU. Any vertex (basic feasible solution) $\widetilde{\mathbf{x}}^*$ is uniquely determined by fixing non-basic variables to their integer lower/upper bounds $l_j$ or $u_j$ and solving a non-singular $m \times m$ basis submatrix $B \mathbf{x}_B = \mathbf{b}'$, where $\mathbf{b}' = \widetilde{\mathbf{b}} - N \mathbf{x}_N \in \mathbb{Z}^m$. By **Cramer's Rule**, the $i$-th basic variable is:

$$
(x_B)_i = \frac{\det(B_i)}{\det(B)},
$$

where $B_i \in \mathbb{Z}^{m \times m}$ is obtained by replacing column $i$ of $B$ with the integer vector $\mathbf{b}'$. Since $B$ is a non-singular square submatrix of the TU matrix $\widetilde{A}$, $\det(B) \in \{-1, +1\}$, while $\det(B_i) \in \mathbb{Z}$. Dividing an integer by $\pm 1$ yields $(x_B)_i \in \mathbb{Z}$! $\blacksquare$

---

### 5.2 Ghouila–Houri Equitable Bicoloring Criterion & The Sufficient 4-Rule TU Checklist

> [!IMPORTANT]
> **Theorem 5.2 (Ghouila–Houri Equitable Bicoloring Theorem, 1962)**:
> A matrix $A \in \{-1, 0, +1\}^{m \times n}$ is Totally Unimodular **if and only if** for every subset of rows $R \subseteq \{1, \dots, m\}$, there exists a sign assignment (bicoloring) $\sigma : R \to \{-1, +1\}$ such that the signed row sum lies in $\{-1, 0, +1\}$ across **every** column:
>
> $$
> \sum_{i \in R} \sigma(i) A_{i, j} \in \{-1, 0, +1\} \quad \forall j \in \{1, \dots, n\}.
> $$
>
> *(By transposition $A^\top$, the exact same condition holds for subsets of columns $C \subseteq \{1, \dots, n\}$.)*

In competitive programming, the fastest way to recognize a direct flow/bipartite-matching matrix is the **Sufficient 4-Rule TU Checklist** (a corollary of Ghouila–Houri):
1. Every entry $A_{i,j} \in \{-1, 0, +1\}$;
2. Every column (or every row, via $A^\top$) contains **at most two non-zero entries**;
3. The rows can be partitioned into two sets $R_1 \sqcup R_2 = \{1, \dots, m\}$ such that for every column $j$ with two non-zero entries:
   - If the two entries have the **same sign** ($+1, +1$ or $-1, -1$), one lies in $R_1$ and the other in $R_2$ (*Bipartite Undirected Incidence Matrix*, where we set $\sigma(i) = +1$ on $R_1$ and $\sigma(i) = -1$ on $R_2$);
   - If the two entries have **opposite signs** ($+1$ and $-1$), both lie in the same part $R_1$ or $R_2$ (*Directed Graph Incidence Matrix*, where $R_1 = \{1, \dots, m\}, R_2 = \emptyset$ and $\sigma(i) = +1$ for all $i$).

---

### 5.3 Column vs. Row Consecutive-Ones Matrices & Rescuing Circular-Ones via Parametric Flow $K$

A $0$-$1$ matrix $A \in \{0, 1\}^{m \times n}$ has the **Column Consecutive-Ones Property (C1P)** (`列连续1性质`) if in every column $j$, the $1$s appear in a single contiguous block of rows $[l_j, r_j]$; it has the **Row Consecutive-Ones Property (R1P)** (`行连续1性质`) if in every row $i$, the $1$s appear in a contiguous block of columns $[l_i, r_i]$.

- **Why Every C1P and R1P Matrix is TU**:
  - If $A$ has **Column-C1P**, left-multiplying by the unimodular row-difference matrix $D$ ($\det = \pm 1$ on the square top-$m$ part, plus the redundant negated sum row $E'_{m+1} = -E_m$) transforms column $j$ (`1`s on $[l_j, r_j]$) into $\mathbf{e}_{l_j} - \mathbf{e}_{r_j+1}$, which has **one $+1$ and one $-1$**! Thus $DA$ is a directed graph incidence matrix, so $A$ is TU.
  - If $A$ has **Row-C1P**, $A^\top$ has Column-C1P, so $A = (A^\top)^\top$ is also TU!

> [!WARNING]
> **The Row vs. Column Consecutive-Ones Compilation Trap**:
> Never apply row differencing $E_i - E_{i-1}$ directly to a **Row-C1P** matrix! Subtracting two rows $[l_1, r_1]$ and $[l_2, r_2]$ creates a row with up to **two blocks** of $+1$s and $-1$s, which is **not** a flow conservation equation!
> - **Column-C1P** (each variable $x_j$ is an interval $[l_j, r_j]$, as in `[NOI2008] 志愿者招募`): Compile in **Primal Space** by subtracting consecutive equations $E_t - E_{t-1}$ ($DA\mathbf{x} = D\mathbf{b}$).
> - **Row-C1P** (each constraint $i$ is an interval $\sum_{t=l_i}^{r_i} x_t \ge d_i$, as in `[ZJOI2013] 防守战线`): Either substitute **Primal Prefix Potentials** $p_t = \sum_{k=1}^t x_k$ and take the **LP Dual**, or take the LP Dual first (turning Row-C1P $A$ into Column-C1P $A^\top$) and apply $D$ to the Dual!

#### Rescuing Circular-Ones (`循环连续1`) Matrices (`UVa 1406` / Cyclic Shifts)
A cyclic shift matrix where intervals can wrap around midnight ($I_j = [l_j, n] \cup [1, r_j]$ with $l_j > r_j$) is **NOT Totally Unimodular** in general (for $n = 3$, the three cyclic length-2 intervals $[1,2], [2,3], [3,1]$ have $\det = +2$). How do we rescue it in competitive programming?

> [!TIP]
> **Theorem 5.3 (Rescuing Circular-Ones via Parametric Wrap-Around Volume $K$)**:
> Partition the interval variables into **non-wrapping** intervals $N_{\text{std}}$ ($[l_j, r_j]$ with $l_j \le r_j$) and **wrapping** intervals $W$ ($[l_j, n] \cup [1, r_j]$ with $l_j > r_j$). Let
>
> $$
> K \stackrel{\text{def}}{=} \sum_{j \in W} x_j
> $$
>
> be the **total flow crossing midnight**. For any **fixed integer $K$**, every wrapping indicator vector can be rewritten by complementing against the full day $\mathbf{1}_{[1, n]}$:
>
> $$
> \mathbf{1}_{[l_j, n] \cup [1, r_j]} = \mathbf{1}_{[1, n]} - \mathbf{1}_{[r_j + 1, l_j - 1]}.
> $$
>
> Substituting this into the point coverage constraint $\sum_{j} A_{t, j} x_j \ge a_t$ shifts the RHS by $-K$ and replaces every wrapping interval $j \in W$ with a **contiguous reverse interval** on $[r_j + 1, l_j - 1]$:
>
> $$
> \sum_{j \in N_{\text{std}} : t \in [l_j, r_j]} x_j - \sum_{j \in W : t \in [r_j+1, l_j-1]} x_j \ge a_t - K \quad (\forall t \in \{1, \dots, n\}), \qquad \sum_{j \in W} x_j = K.
> $$
>
> In this transformed system, **every column is once again a single contiguous interval** (plus the global budget $\sum_{j \in W} x_j = K$, which simply routes $K$ units of flow through a dedicated midnight node)! Moreover, by LP convexity, the minimum cost $\Phi(K)$ is a **convex function of $K$**, so we can find the optimal integer $K^*$ by **ternary search** (or binary search on $\Phi(K+1) - \Phi(K)$) in $O(\log(\max K))$ MCMF runs!

---

### 5.4 Tutte Network Matrices & Rooted Tree Path Incidence Compilations

What is the natural generalization of Consecutive-Ones from a 1D line to a **tree**?

**Definition 5.2 (Tutte Network Matrix)**:
Let $T = (V, E_T)$ be a directed tree (an orientation of any undirected tree), and let $G = (V, E_G)$ be a second directed graph on the same vertex set $V$. The **Network Matrix** $M(T, G) \in \{-1, 0, +1\}^{|E_T| \times |E_G|}$ has rows indexed by tree arcs $e \in E_T$ and columns indexed by non-tree arcs $p = (u, v) \in E_G$:

$$
M(T, G)_{e, p} = \begin{cases} +1 & \text{if tree arc } e \text{ appears in the forward direction along the unique } T\text{-path from } u \text{ to } v, \\ -1 & \text{if tree arc } e \text{ appears in the backward direction along the unique } T\text{-path from } u \text{ to } v, \\ 0 & \text{if tree arc } e \text{ is not on the unique } T\text{-path from } u \text{ to } v. \end{cases}
$$

**Theorem 5.4 (Tutte 1965)**: Every Network Matrix $M(T, G)$ and its transpose $M(T, G)^\top$ is **Totally Unimodular**.

In competitive programming, when $T$ is a **rooted tree** (oriented away from root $r$, or toward root $r$) and each path $P_j$ is a **vertical (ancestor-to-descendant) path** from an ancestor $u_j$ down to a descendant $v_j$, we can compile both **Edge-Path** and **Vertex-Path** coverage constraints directly into a flow network using the tree generalization of $D$:

| Tree Coverage Variant | Algebraic Difference Transformation $D_T$ | Resulting Directed Edge for Vertical Path $P_j = (u_j \text{ down to } v_j)$ | Resulting Directed Edge for Slack Variable $s_v \ge 0$ |
| :--- | :--- | :--- | :--- |
| **1. Edge-Path Coverage** (`[BZOJ 1937]`): Constraint on each tree edge $e_v = (\text{parent}(v), v)$ for $v \neq r$, with virtual root edge $e_r$. | For each vertex $u \in V$, subtract all child tree-edge equations from $u$'s incoming parent tree-edge equation: $E'_u = E_{e_u} - \sum_{w \in \text{child}(u)} E_{e_w}$. | Along $P_j = (u_j \rightsquigarrow v_j)$, for every internal vertex $x \in P_j \setminus \{u_j\}$, both $e_x$ and the unique child edge on $P_j$ contain $P_j$, so $+1 - 1 = 0$ cancels! Only the endpoints survive: **directed edge $u_j \to v_j$** ($\mathbf{e}_{v_j} - \mathbf{e}_{u_j}$). | Slack $s_{e_v}$ on tree edge $e_v = (p, v)$ becomes a tree-backbone edge between $v$ and $p = \text{parent}(v)$. |
| **2. Vertex-Path Coverage**: Constraint on each tree vertex $v \in V$ (path $P_j$ includes all vertices from $u_j$ down to $v_j$ inclusive), with virtual super-root $0 = \text{parent}(r)$. | For each vertex $u \in V \cup \{0\}$, subtract all child vertex equations from $u$'s own vertex equation: $E'_u = E_u - \sum_{w \in \text{child}(u)} E_w$. | Along $P_j = (u_j \rightsquigarrow v_j)$, cancellation occurs at every vertex from $u_j$ down to $\text{parent}(v_j)$, while at $\text{parent}(u_j)$ only the child $u_j$ is in $P_j$! Survives as: **directed edge $v_j \to \text{parent}(u_j)$**. | Slack $s_v$ on vertex $v$ becomes a tree-backbone edge between $v$ and $\text{parent}(v)$. |

---

### 5.5 The 4 Classic Non-TU Counterexamples ($\det = \pm 2$)

Whenever a problem slightly violates the topological rules above, Total Unimodularity collapses via a $3 \times 3$ submatrix of determinant $\pm 2$, producing a **half-integral relaxation gap** ($x_i = 0.5$):

```
 (1) Odd Cycle Incidence     (2) Split Interval       (3) Circular Interval    (4) Undirected Tree Paths on K_{1,3}
     (Bipartite violated)        [1,1] U [3,3]            (Wrap-around)            (Leaves 1,2,3 around center 0)
       [ 1  0  1 ]                 [ 1  1  1 ]              [ 1  0  1 ]              e1 [ 1  0  1 ] (Paths 1-2, 2-3, 3-1
   A = [ 1  1  0 ]             A = [ 1  1  0 ]          A = [ 1  1  0 ]          A = e2 [ 1  1  0 ]  each use 2 of the 3
       [ 0  1  1 ]                 [ 0  1  1 ]              [ 0  1  1 ]              e3 [ 0  1  1 ]  star edges!)
      det(A) = +2                 det(A) = -1, but         det(A) = +2              det(A) = +2
                                  with [1,2],[2,3],[1,1]U[3,3]
                                  det = +2!
```

> [!CAUTION]
> **Why Undirected Tree Paths Fail TU ($K_{1,3}$ Star Counterexample)**:
> In Theorem 5.4, a Tutte Network Matrix requires each path $P_j$ to be a **directed path** in $T$ (or to contribute $+1$ on forward tree arcs and $-1$ on backward tree arcs). If instead we ask to cover tree edges using **arbitrary undirected paths** (where a path $u \text{--} \text{LCA}(u, v) \text{--} v$ contributes **$+1$ on both rising and falling branches**), then on a 3-leaf star $K_{1,3}$ with edges $e_1, e_2, e_3$, the three leaf-to-leaf paths $P_{12} = \{e_1, e_2\}$, $P_{23} = \{e_2, e_3\}$, $P_{31} = \{e_3, e_1\}$ form the odd-cycle incidence matrix with $\det = +2$! Requiring paths to be **vertical (ancestor-to-descendant)** guarantees every path is monotone in the rooted tree orientation.

---

## 6. Submodular Function Minimization (SFM), Lovász Extension, Base Polyhedra $B(f)$, and the Boundary with Matroid Intersection

### 6.1 The 4-Level Polyhedral Hierarchy: From $s$-$t$ Cuts to Matroid Intersection

Why do so many seemingly unrelated problems—Project Selection (`最大权闭合子图`), Multi-State Grid Cuts (`[HNOI2013] 切糕`), Continuous Altitudes (`[NOI2010] 海拔`, `CF 1427G`), Isotonic Regression (`保序回归`), Tournament Triples (`[WC2007] 剪刀石头布`), and Spanning Trees with Degree Bounds (`CF 1284G`, `CF 1556H`)—live in the same conceptual neighborhood? Because they sit on four consecutive levels of a single **Polyhedral Hierarchy**:

```
  +-----------------------------------------------------------------------------------+
  | LEVEL 4: MATROID INTERSECTION / SUBMODULAR FLOW (Edmonds-Giles 1977)              |
  |   Polyhedron: P(f_1) \cap P(f_2)   (e.g., Graphic \cap Partition Matroid)         |
  |   Solver: Successive Shortest Augmenting Paths in Exchange Graph (NOT Dinic!)     |
  |   +---------------------------------------------------------------------------+   |
  |   | LEVEL 3: POLYMATROID BASE POLYHEDRON B(f) & GENERAL SFM (Edmonds 1970)    |   |
  |   |   Polyhedron: B(f) = { x in R^V : x(S) <= f(S) (\forall S), x(V) = f(V) } |   |
  |   |   Solver: Edmonds' Greedy (for linear max over B(f)); General SFM         |   |
  |   |   +-------------------------------------------------------------------+   |   |
  |   |   | LEVEL 2: CUT-REPRESENTABLE SUBMODULAR / LOVASZ COAREA (K-Z 2004)  |   |   |
  |   |   |   Degree-2 Submodular Pseudo-Boolean & Convex Total Variation     |   |   |
  |   |   |   Solver: Standard s-t Min-Cut / Parametric Min-Cut (整体二分)    |   |   |
  |   |   |   +-----------------------------------------------------------+   |   |   |
  |   |   |   | LEVEL 1: PROJECT SELECTION / CLOSURE (Picard 1976)        |   |   |   |
  |   |   |   |   Modular weights + hard implications u -> v              |   |   |   |
  |   |   |   |   Solver: Single s-t Min-Cut                              |   |   |   |
  |   |   |   +-----------------------------------------------------------+   |   |   |
  |   |   +-------------------------------------------------------------------+   |   |
  |   +---------------------------------------------------------------------------+   |
  +-----------------------------------------------------------------------------------+
  === BARRIER: 3-Matroid Intersection (3DM, Degree-Bounded Spanning Tree) & ===
  ===          Multi-Commodity Flow (k >= 2) -> Non-TDI, Half-Integral, NP-Hard!  ===
```

---

### 6.2 Cut Submodularity (Double-Counting Identity) & Degree-2 vs. Degree-$\ge 3$ Cut Representability

Let $V$ be a finite ground set. A set function $f : 2^V \to \mathbb{R}$ is **submodular** (`次模函数`) if for all $A, B \subseteq V$:

$$
f(A) + f(B) \ge f(A \cup B) + f(A \cap B),
$$

or equivalently, if it exhibits **diminishing marginal returns**: $f(A \cup \{v\}) - f(A) \ge f(B \cup \{v\}) - f(B)$ whenever $A \subseteq B \subseteq V \setminus \{v\}$.

#### Why Directed Cut Capacity is Submodular (Double-Counting Proof)
In any directed network $G = (V, E)$ with non-negative capacities $c_{uv} \ge 0$, let $\kappa(A) = c(\delta^+(A)) = \sum_{u \in A, v \notin A} c_{uv}$. Partitioning $V$ into the four disjoint Venn regions $A \cap B$, $A \setminus B$, $B \setminus A$, and $V \setminus (A \cup B)$ gives the exact identity:

$$
\kappa(A) + \kappa(B) = \kappa(A \cup B) + \kappa(A \cap B) + c(A \setminus B, B \setminus A) + c(B \setminus A, A \setminus B).
$$

Since $c_{uv} \ge 0$, the two cross-terms between $A \setminus B$ and $B \setminus A$ are non-negative, immediately proving $\kappa(A) + \kappa(B) \ge \kappa(A \cup B) + \kappa(A \cap B)$! Moreover, projecting out auxiliary vertices $U$ via $f_{\text{proj}}(A) = \min_{W \subseteq U} \kappa(\{s\} \cup A \cup W)$ preserves submodularity.

> [!IMPORTANT]
> **Theorem 6.1 (Kolmogorov–Zabih 2004 vs. Zivný–Cohen–Jeavons 2009 Barrier)**:
> 1. **Degree $\le 2$ (Pairwise Interactions)**: A pseudo-Boolean function $E(x_1, \dots, x_n) = \sum_i E_i(x_i) + \sum_{i < j} E_{ij}(x_i, x_j)$ of binary variables $x_i \in \{0, 1\}$ is representable as the minimum $s$-$t$ cut of a non-negative network **if and only if** every pairwise term satisfies the submodularity inequality:
>
>    $$
>    E_{ij}(0, 0) + E_{ij}(1, 1) \le E_{ij}(0, 1) + E_{ij}(1, 0) \quad (A + D \le B + C).
>    $$
>
> 2. **Degree $3$ (Cubic Interactions)**: A cubic function $E_{ijk}(x_i, x_j, x_k)$ is cut-representable (using auxiliary vertices) if and only if it is both submodular and satisfies the **co-planar condition**.
> 3. **Degree $\ge 4$ Barrier**: There exist strictly submodular functions of $4$ binary variables ($2^4 = 16$ states, $14$ independent degrees of freedom after fixing $\emptyset$ and $V$) that **cannot be represented as the minimum cut of ANY directed graph**, no matter how many auxiliary vertices are added (via a dimension-counting / polyhedral facet obstruction).

---

### 6.3 The Lovász Extension $\hat{f}(\mathbf{x})$ & Coarea Level-Set Integration Theorem

How do we connect a discrete submodular function $f : 2^V \to \mathbb{R}$ (with $f(\emptyset) = 0$) on subsets $S \subseteq V$ (identified with $\mathbf{1}_S \in \{0, 1\}^V$) to continuous optimization over $\mathbf{x} \in \mathbb{R}^V$?

**Definition 6.1 (Lovász Extension, Lovász 1983)**:
For any $\mathbf{x} \in \mathbb{R}^V$, sort its coordinates in non-increasing order $x_{\pi_1} \ge x_{\pi_2} \ge \dots \ge x_{\pi_n}$ and set $S_k = \{\pi_1, \dots, \pi_k\}$ ($S_0 = \emptyset$). The **Lovász extension** $\hat{f} : \mathbb{R}^V \to \mathbb{R}$ is defined by two equivalent formulas:

$$
\begin{aligned}
\hat{f}(\mathbf{x}) &= \sum_{k=1}^{n} x_{\pi_k} \big( f(S_k) - f(S_{k-1}) \big) = x_{\pi_n} f(V) + \sum_{k=1}^{n-1} (x_{\pi_k} - x_{\pi_{k+1}}) f(S_k) \\
&= \int_{0}^{+\infty} f\big(\{v \in V : x_v \ge \lambda\}\big) \, d\lambda + \int_{-\infty}^{0} \Big( f\big(\{v \in V : x_v \ge \lambda\}\big) - f(V) \Big) \, d\lambda \quad \text{(Coarea Formula)}.
\end{aligned}
$$

> [!IMPORTANT]
> **Theorem 6.2 (Lovász 1983 — Convexity & Level-Set Decomposition)**:
> 1. $f : 2^V \to \mathbb{R}$ is **submodular** if and only if its Lovász extension $\hat{f} : \mathbb{R}^V \to \mathbb{R}$ is **convex**.
> 2. Minimizing $f(S)$ over discrete subsets $S \subseteq V$ is equivalent to minimizing the convex function $\hat{f}(\mathbf{x})$ over the continuous hypercube $\mathbf{x} \in [0, 1]^V$:
>
>    $$
>    \min_{S \subseteq V} f(S) = \min_{\mathbf{x} \in [0, 1]^V} \hat{f}(\mathbf{x}).
>    $$
>
> 3. **Level-Set Decoupling (`[NOI2010] 海拔`, `CF 1427G`, `保序回归`)**: For any directed graph $G = (V, E)$ with capacities $c_{uv} \ge 0$, the Lovász extension of the cut function $f(S) = \sum_{(u,v) \in E} c_{uv} [u \in S, v \notin S]$ is the **Total Variation** $\hat{f}(\mathbf{x}) = \sum_{(u,v) \in E} c_{uv} \max(0, x_u - x_v)$. By the Coarea formula, optimizing continuous or multi-valued variables $x_v \in [L, R]$ subject to Total Variation + separable convex vertex costs $\sum_v g_v(x_v)$ **decouples across independent threshold slices** $\lambda \in [L, R]$:
>
>    $$
>    \sum_{v \in V} g_v(x_v) + \sum_{(u,v) \in E} c_{uv} \max(0, x_u - x_v) = \sum_{v \in V} g_v(L) + \int_{L}^{R} \Bigg[ \sum_{v : x_v \ge \lambda} g'_v(\lambda) + \sum_{(u,v) \in E} c_{uv} \big[x_u \ge \lambda > x_v\big] \Bigg] d\lambda.
>    $$
>
>    Because the integrand at each threshold $\lambda$ is a **binary $s$-$t$ cut** for the indicator set $S_\lambda = \{v : x_v \ge \lambda\}$ with monotone vertex weights $g'_v(\lambda)$, the optimal thresholds $S_\lambda^*$ are **nested** ($S_{\lambda_1}^* \supseteq S_{\lambda_2}^*$ for $\lambda_1 < \lambda_2$)!
>    - If $g_v(x_v) = 0$ (as in `[NOI2010] 海拔`), the integrand is identical for all $\lambda \in [0, 1]$, so an optimal continuous solution takes values in $\{0, 1\}$!
>    - If $g_v(x_v) = w_v |x_v - a_v|^p$ (as in `CF 1427G` and `[省选联考 2020] 保序回归`), we find the nested level sets $S_\lambda^*$ for all $\lambda$ via **Incremental Residual Rollback** (when $K \le 400$ distinct values) or **Parallel Binary Search (`整体二分`)** in $O(\log V_{\max})$ layers of Min-Cut!

---

### 6.4 Polymatroid Base Polyhedra $B(f)$, Edmonds' Greedy Theorem, and Two Laminar Matroids

Given a submodular function $f : 2^V \to \mathbb{R}$ with $f(\emptyset) = 0$, define the **Submodular Polyhedron** $P(f)$ and the **Base Polyhedron** $B(f)$:

$$
P(f) = \Big\{ \mathbf{x} \in \mathbb{R}^V : \forall S \subseteq V, \; x(S) \stackrel{\text{def}}{=} \sum_{v \in S} x_v \le f(S) \Big\}, \qquad B(f) = \big\{ \mathbf{x} \in P(f) : x(V) = f(V) \big\}.
$$

> [!IMPORTANT]
> **Theorem 6.3 (Edmonds' Polymatroid Greedy Theorem, 1970)**:
> For any weight vector $\mathbf{w} \in \mathbb{R}^V$, sort $V$ so that $w_{\pi_1} \ge w_{\pi_2} \ge \dots \ge w_{\pi_n}$ and set $S_k = \{\pi_1, \dots, \pi_k\}$. Then the greedy marginal vector $\mathbf{x}^* \in \mathbb{R}^V$ defined by
>
> $$
> x^*_{\pi_k} = f(S_k) - f(S_{k-1}) \quad (1 \le k \le n)
> $$
>
> is a vertex of $B(f)$ that maximizes $\mathbf{w}^\top \mathbf{x}$ over $\mathbf{x} \in B(f)$, and its maximum value equals the Lovász extension $\hat{f}(\mathbf{w})$:
>
> $$
> \max_{\mathbf{x} \in B(f)} \mathbf{w}^\top \mathbf{x} = \hat{f}(\mathbf{w}).
> $$

**Proof Sketch via Dual Uncrossing**:
Consider the LP Dual of $\max\{\mathbf{w}^\top \mathbf{x} : x(S) \le f(S)\}$: $\min \sum_{S \subseteq V} f(S) y_S$ s.t. $\sum_{S \ni v} y_S = w_v$ and $y_S \ge 0$ for $S \subsetneq V$. If two active sets $A, B$ in the dual solution cross ($A \not\subseteq B$ and $B \not\subseteq A$), replacing $\epsilon = \min(y_A, y_B) > 0$ weight on $(A, B)$ with $+\epsilon$ on $A \cup B$ and $+\epsilon$ on $A \cap B$ preserves $\sum_{S \ni v} y_S = w_v$ and changes the dual objective by $\epsilon(f(A \cup B) + f(A \cap B) - f(A) - f(B)) \le 0$ by submodularity! Thus the optimal dual support is the **nested chain** $S_1 \subset S_2 \subset \dots \subset S_n$ with dual weights $y_{S_k} = w_{\pi_k} - w_{\pi_{k+1}} \ge 0$ (and $y_{S_n} = w_{\pi_n}$), whose objective is $\sum_{k=1}^{n-1} (w_{\pi_k} - w_{\pi_{k+1}}) f(S_k) + w_{\pi_n} f(S_n) = \hat{f}(\mathbf{w})$! $\blacksquare$

#### Compiling Two Laminar Matroids / Submodular Systems via Hasse Out-Tree + In-Tree
A family $\mathcal{L} \subseteq 2^V$ is **laminar** (`层状族`, e.g., subtrees of a rooted tree, or nested/disjoint intervals) if for any $A, B \in \mathcal{L}$, either $A \cap B = \emptyset$, $A \subseteq B$, or $B \subseteq A$. Its containment Hasse diagram is a **forest of rooted trees**.
- **Single Laminar Family**: If we have bounds $L_A \le x(A) \le R_A$ for all $A \in \mathcal{L}_1$, each element $v \in V$ belongs to a unique smallest set $A(v) \in \mathcal{L}_1$, and flow from the source passes down the **Hasse Out-Tree** (where the tree edge into node $A \in \mathcal{L}_1$ has lower/upper capacity $[L_A, R_A]$).
- **Two Laminar Families $\mathcal{L}_1$ and $\mathcal{L}_2$ (`P22`, `AGC 031E`)**: Sandwich the item edges $v_{\text{in}} \to v_{\text{out}}$ (cap $1$, cost $-w_v$) between the **Hasse Out-Tree of $\mathcal{L}_1$** (flowing $S \to \text{root}(\mathcal{L}_1) \to \dots \to A_1(v) \to v_{\text{in}}$) and the **Hasse In-Tree of $\mathcal{L}_2$** (flowing $v_{\text{out}} \to A_2(v) \to \dots \to \text{root}(\mathcal{L}_2) \to T$)! Every path $S \to T$ selects one item $v$ and increments the flow through **all** ancestor sets of $v$ in both $\mathcal{L}_1$ and $\mathcal{L}_2$ simultaneously!

---

### 6.5 The Exact Boundary of Flow: 3-Entity Star Split vs. Flow Amnesia in 3DM, Graphic $\cap$ Partition Matroid Intersection, and 2-Commodity Half-Integrality

#### 1. Why 3-Entity Star Compatibility Works (`[USACO07OPEN] Dining G`) While 3DM Triangle Compatibility Fails ("Flow Amnesia" `流量失忆`)
Suppose we must match triplets $(f, c, d) \in F \times C \times D$.
- **Case A (Star Compatibility $F \text{--} C \text{--} D$, Polynomial Max-Flow)**: Compatibility factors into $(f, c) \in E_{FC}$ and $(c, d) \in E_{CD}$ (food $f$ and drink $d$ do not directly care about each other once cow $c$ is fixed). We place **the central bottleneck entity $C$ in the middle layer**, split each cow $c$ into $c_{\text{in}} \xrightarrow{\text{cap } 1} c_{\text{out}}$, and route $S \to f \to c_{\text{in}} \to c_{\text{out}} \to d \to T$.
  - **Broken Gadget (Wrong Layer Order $S \to C \to F \to D \to T$)**: If a solver puts $F$ in the middle ($S \to c \to f \to d \to T$), then food $f$ forgets *which* cow $c$ sent it flow, and can forward that flow to a drink $d$ that cow $c$ hates!
- **Case B (Triangle / General 3DM Compatibility $(f, c, d) \in T$, NP-Complete)**: If compatibility requires a joint triple $(f, c, d)$ (e.g., Cow 1 likes $(F_1, D_1)$ and $(F_2, D_2)$, but NOT $(F_1, D_2)$), **no ordering of layers** works: any middle vertex $v_{\text{in}} \to v_{\text{out}}$ suffers from **Flow Amnesia (`流量失忆`)**—once flow enters $v_{\text{in}}$ from $u$, the Markovian conservation law $\text{Inflow}(v) = \text{Outflow}(v)$ erases the identity of $u$, allowing flow to exit $v_{\text{out}}$ to an incompatible $w$! In matroid terms, 3-Dimensional Matching is the **Intersection of 3 Partition Matroids** (NP-hard).

#### 2. When Degree-Bounded Spanning Tree is Polynomial (2 Matroids) vs. NP-Hard (3 Matroids)
- **General Degree-Bounded Spanning Tree (NP-Hard)**: Requiring $\deg_T(v) \le d_v$ for **all** $v \in V$ reduces from Hamiltonian Path ($d_v = 2$). Even on a **bipartite graph $V = A \sqcup B$**, enforcing degree bounds on both $A$ and $B$ plus Graphic Matroid acyclicity is the **Intersection of 3 Matroids** ($M_{\text{Graphic}} \cap M_{\text{Part}(A)} \cap M_{\text{Part}(B)}$), which is NP-hard!
- **Independent-Set Degree-Bounded Spanning Tree (`CF 1284G — Seollal`, Polynomial 2-Matroid Intersection)**: If degree bounds $\deg_T(v) \le d_v$ are enforced **only on an independent set $B \subseteq V$** (such as the black cells $(i+j) \equiv 0 \pmod 2$ of a chessboard where $(0,0)$ is excluded), then **no edge has both endpoints in $B$**! Consequently, every edge $e \in E$ is incident to **at most one** degree-constrained vertex in $B$. The degree constraints on $B$ therefore partition $E$ into **disjoint stars** $\{\delta(b)\}_{b \in B}$, which is a **SINGLE Partition Matroid $M_2$**! Intersecting $M_1 = M_{\text{Graphic}}$ and $M_2 = M_{\text{Partition}(B)}$ is a polynomial **2-Matroid Intersection** problem!
- **Fixed-Core Degree-Bounded Spanning Tree (`CF 1556H — DIY Tree`)**: If degree bounds hold only on the first $K \le 5$ vertices, enumerate the internal forest $F_{\text{core}}$ on $\{1, \dots, K\}$ in $O(2^{\binom{K}{2}})$ ($B_5 = 52$ or $\le 2^{10}$ states); once $F_{\text{core}}$ is fixed, no remaining edge connects two vertices inside $\{1, \dots, K\}$, so $\{1, \dots, K\}$ acts as an independent set for the remaining edges, reducing to **Weighted Graphic $\cap$ Partition Matroid Intersection**!

#### 3. The 2-Commodity Flow Half-Integrality Counterexample ($\det = -2$)
Even for $k = 2$ commodities on a $4$-vertex directed graph with unit capacities, Max Multi-Commodity Flow is **not** integral: consider the 4-cycle $1 \to 2 \to 3 \to 4 \to 1$ (unit capacities), with Commodity 1 routing $s_1 = 1 \to t_1 = 3$ (paths $P_1 = 1 \to 2 \to 3$ and $P_2 = 1 \to 4 \to 3$, plus shortcut $4 \to 2$ so $P_1 = 1 \to 4 \to 2 \to 3$) and Commodity 2 routing $s_2 = 4 \to t_2 = 2$. Three paths pairwise sharing unit edges form the $3 \times 3$ submatrix $\begin{bmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}$ of determinant $-2$, yielding a unique fractional optimum $f(P_1) = f(P_2) = f(P_3) = 0.5$ of total flow $1.5$ while the maximum integer flow is $1$.

---

## 7. Cohort 3 Targeted Gap-Hunting & Reconciled Master Recognition/Compilation Decision Table

### 7.1 Targeted Gap 1: Seymour's Decomposition Theorem for Totally Unimodular Matrices (1980)

In Sections 2–5, we observed a striking empirical phenomenon: **every single Totally Unimodular linear program encountered in competitive programming compiled into either a Primal Network Flow problem (via row operations $D A$ on a Network Matrix) or a Dual Potential Flow problem (via LP Duality $A^\top \boldsymbol{\pi}$ on the Transpose of a Network Matrix)**. Is this a coincidence, or a theorem of mathematics?

In 1980, Paul Seymour proved one of the crown jewels of matroid theory and polyhedral combinatorics, completely classifying all Totally Unimodular matrices (and equivalently all **Regular Matroids**, i.e., matroids representable over every field):

> [!IMPORTANT]
> **Theorem 7.1 (Seymour's Regular Matroid & Totally Unimodular Matrix Decomposition Theorem, 1980)**:
> Every Totally Unimodular matrix $A \in \{-1, 0, +1\}^{m \times n}$ can be constructed recursively via **$1$-sums** (block-diagonal concatenation $A_1 \oplus A_2$), **$2$-sums**, and **$3$-sums** (gluing along a rank-$1$ or rank-$2$ interface) starting from just **three atomic building blocks**:
> 1. **Tutte Network Matrices $M(T, G)$** (which compile directly in **Primal Space** into standard Minimum-Cost Flow / Circulation via the tree incidence transformation $D_T$ of Section 5.4);
> 2. **Transposes of Network Matrices $M(T, G)^\top$** (which compile via **LP Duality** into Minimum-Cost Flow / Circulation in **Dual Space**, because $(M(T, G)^\top)^\top = M(T, G)$ is a Network Matrix!);
> 3. **The Single Sporadic $5 \times 5$ Matrix $R_{10}$** (associated with the regular matroid $R_{10}$ on 10 elements, which is neither graphic nor cographic):
>
>    $$
>    R_{10} = \begin{bmatrix}
>    +1 & 0 & 0 & +1 & -1 \\
>    -1 & +1 & 0 & 0 & +1 \\
>    0 & -1 & +1 & 0 & +1 \\
>    0 & 0 & -1 & +1 & +1 \\
>    +1 & +1 & +1 & +1 & +1
>    \end{bmatrix}.
>    $$
>
> **Why This Explains All Competitive Programming Flow Compilations**:
> Aside from artificial $5 \times 5$ constructions built from $R_{10}$, **every natural TU constraint matrix in combinatorial optimization is built from Network Matrices and their Transposes**! Therefore:
> - If your problem's constraint matrix is a **Network Matrix** (e.g., Column-Consecutive-Ones `志愿者招募`, Directed Tree Edge/Vertex Coverage `BZOJ 1937`), row-reduction $D_T A$ compiles it **directly into a Primal Flow Network**.
> - If your problem's constraint matrix is the **Transpose of a Network Matrix** (e.g., Difference Constraints $\pi_v - \pi_u \le w_e$, Row-Consecutive-Ones `防守战线`, Inverse MST Cycle Inequalities `SHOI2004`), taking the **LP Dual** transposes $A$ into $A^\top$ (a Network Matrix!) and compiles it **directly into a Dual Flow Network**.

---

### 7.2 Targeted Gap 2: Discrete Convex Analysis (Murota's $L^\natural$-Convex & $M^\natural$-Convex Duality)

Why do **Lovász extensions / node potentials / multi-state cuts** on one side, and **polymatroid base polyhedra / conserved network flows / WQS convex slopes** on the other side, behave like dual mirror images? In **Discrete Convex Analysis (DCA)** (Murota 1998, 2003), integer-valued functions on $\mathbb{Z}^n$ admit two fundamental notions of "discrete convexity" that are exchanged by the **Discrete Legendre–Fenchel Conjugate** $g^*(\mathbf{y}) = \sup_{\mathbf{x} \in \mathbb{Z}^n} (\mathbf{y}^\top \mathbf{x} - g(\mathbf{x}))$:

| DCA Class | Defining Discrete Midpoint / Exchange Axiom | Polyhedral Domain & Continuous Counterpart | Competitive Programming Manifestations |
| :--- | :--- | :--- | :--- |
| **$L^\natural$-Convex Functions** (`L-自然凸函数`, "Lattice / Lovász Convex") | **Discrete Midpoint Convexity**: $g(\mathbf{p}) + g(\mathbf{q}) \ge g\big(\lceil \frac{\mathbf{p}+\mathbf{q}}{2} \rceil\big) + g\big(\lfloor \frac{\mathbf{p}+\mathbf{q}}{2} \rfloor\big)$, equivalently submodularity + translation subadditivity $g(\mathbf{p} + \mathbf{1}) - g(\mathbf{p})$. | Defined on **Node Potentials / Timestamps / Altitudes** $\mathbf{p} \in \mathbb{Z}^V$ constrained by difference bounds $p_v - p_u \le c_{uv}$; generated by **Lovász extensions** of submodular functions. | 1. **Dual Node Potentials $\boldsymbol{\pi}$** in MCMF<br>2. **Multi-State Monge Cuts** (`[HNOI2013] 切糕`)<br>3. **Continuous / Discrete Total Variation** (`[NOI2010] 海拔`, `CF 1427G`)<br>4. **$L_p$ Isotonic Regression** (`保序回归`, `P28`, `P29`) |
| **$M^\natural$-Convex Functions** (`M-自然凸函数`, "Matroid / Flow Convex") | **Symmetric Exchange Axiom**: For $\forall i$ with $x_i > y_i$, $\exists j \in \{k : x_k < y_k\} \cup \{0\}$ such that $f(\mathbf{x}) + f(\mathbf{y}) \ge f(\mathbf{x} - \mathbf{e}_i + \mathbf{e}_j) + f(\mathbf{y} + \mathbf{e}_i - \mathbf{e}_j)$. | Defined on **Polymatroid Base Polyhedra $B(f)$ & Conserved Flow Divisors** $\mathbf{x} \in \mathbb{Z}^V$ ($\sum_i x_i = r$); marginal increments form **concave/convex WQS slopes**. | 1. **Primal Conserved Network Flows $\mathbf{f}$**<br>2. **Matroid / Polymatroid Bases** (`[WC2007] 剪刀石头布`, `CF 1284G`, `CF 1556H`)<br>3. **Successive Shortest Path Cost Curve $C(F)$** (`CF 1307G`)<br>4. **Simulated MCMF (`模拟费用流`) & WQS Binary Search** (`[NOI2019] 序列`, `[WC2019] 雪灾与外卖`) |

> [!IMPORTANT]
> **Theorem 7.2 (Murota's Discrete Conjugacy Theorem)**:
> The discrete Legendre–Fenchel transform $\mathbf{p} \leftrightarrow \mathbf{x}$ establishes a **one-to-one bijection between $L^\natural$-convex functions and $M^\natural$-convex functions**!
> - Minimizing an **$L^\natural$-convex function** (potentials $\mathbf{p}$ with convex difference penalties $\sum_{(u,v)} \phi_{uv}(p_v - p_u)$) is the exact dual of minimizing an **$M^\natural$-convex function** (conserved flows $\mathbf{f}$ with separable convex edge costs $\sum_e \phi^*_e(f_e)$).
> - In competitive programming: whenever a problem is formulated in **Potential / Altitude / Regression Space** ($L^\natural$-convex), you can either minimize it directly via **Coarea Level-Set Min-Cuts (`整体二分`)** or dualize it into **Conserved Flow Space** ($M^\natural$-convex) and solve it via **MCMF / Simulated MCMF**!

---

### 7.3 Reconciled Master Recognition & Compilation Decision Table

| Surface Problem Structure | Algebraic / Polyhedral Signature | Primal or Dual Compilation | Target Solver & Complexity | Canonical Exemplars |
| :--- | :--- | :--- | :--- | :--- |
| **Each variable $x_j$ covers a contiguous interval $[l_j, r_j]$ of points** | Column-Consecutive-Ones $A\mathbf{x} \ge \mathbf{a}$ ($L^\natural$/$M^\natural$ Network Matrix) | **Primal Equation Subtraction** $E'_t = E_t - E_{t-1}$: $x_j$ becomes edge $l_j \to r_j+1$, slack $y_t$ becomes $t+1 \to t$ | MCMF on $n+1$ vertices | `[NOI2008] 志愿者招募` (`P02`), `POJ 3680` (`P05`), `[BZOJ 1283] 序列` (`P07`) |
| **Each constraint $j$ bounds the sum of point variables over $[l_j, r_j]$** | Row-Consecutive-Ones $\sum_{i=l_j}^{r_j} x_i \ge d_j$ (Transpose Network Matrix) | **Prefix Potentials $p_i = \sum_{k \le i} x_k$ + LP Dual**: interval $j$ becomes $(l_j-1) \to r_j$ | MCMF on $n+1$ vertices | `[ZJOI2013] 防守战线` (`P03`), `[LOJ 6079]` (`P13`) |
| **Cyclic intervals $[l_j, n] \cup [1, r_j]$ wrapping around midnight** | Circular-Ones Matrix (Non-TU globally, TU for fixed wrap-around flow $K$) | Fix $K = \sum_{j \in W} x_j$, complement wrapping intervals to $1 - \mathbf{1}_{[r_j+1, l_j-1]}$, **Ternary Search on $K$** | $O(\log(\max K)) \times \text{MCMF}$ | `UVa 1406 / Cyclic Volunteers` (`P21`) |
| **Each variable $x_j$ covers a vertical tree path $u_j \rightsquigarrow v_j$** | Tutte Network Matrix $M(T, G)$ on rooted tree $T$ | **Tree Difference $D_T$**: subtract child equations from parent equation ($u_j \to v_j$ or $v_j \to \text{pa}(u_j)$) | MCMF on $\|V\|$ vertices | `[BZOJ 1937]` (`P15`), `[AHOI2014] 支线剧情` (`P11`) |
| **Modify edge weights to make $T$ an MST or raise shortest path to $\ge D$** | Difference / Bipartite Sum Constraints $x_f + y_e \ge w_f - w_e$ or $\pi_v - \pi_u + \delta_e \ge w_e$ | **LP Dual to Bipartite Matching / MCMF**, recover weights via **Post-Augmentation SPFA** from super-root $Q$ | KM / MCMF + 1 SPFA pass (or $O(Q \log F)$ slope hull) | `[SHOI2004] 最小生成树` (`P09`), `BZOJ 3118` (`P10`), `CF 1307G` (`P16`) |
| **Continuous or large-range values $x_v \in [L, R]$ with $\sum c_{uv}\max(0, x_u-x_v) + \sum g_v(x_v)$** | $L^\natural$-Convex / Lovász Extension Coarea Integral over threshold slices $\lambda$ | **Coarea Level-Set Decoupling**: binary cut at each $\lambda$; solve via Planar Dual, Incremental Rollback, or `整体二分` | Planar Dijkstra (`P17`), $O(N^3)$ Rollback (`P25`), or $O(\log V) \times \text{Dinic}$ (`P29`) | `[NOI2010] 海拔` (`P17`), `CF 1427G` (`P25`), `[省选2020] 保序回归` (`P29`) |
| **Subtree / Prefix-Suffix rank caps across TWO trees or 2D coordinates** | Intersection of Two Laminar Matroids $\mathcal{L}_1 \cap \mathcal{L}_2$ | **Hasse Out-Tree ($\mathcal{L}_1$) + Item Split + Hasse In-Tree ($\mathcal{L}_2$)** | Bounded-Circulation Max-Flow / MCMF | `Two-Tree Subtree Selection` (`P22`), `AGC 031E` (`P31`) |
| **Spanning tree with degree bounds on an independent set or small core $K \le 5$** | Graphic Matroid $\cap$ Partition Matroid ($M_1 \cap M_2$) | **Matroid Intersection Exchange Graph** (plus $2^{\binom{K}{2}}$ core enumeration if $K \le 5$) | $O(N M^2)$ Augmenting Paths in Exchange Graph | `CF 1284G — Seollal` (`P26`), `CF 1556H — DIY Tree` (`P27`) |

---

## 8. Reconciled Master 4-Tier Curated Problem Bank (32 Problems)

Every problem below is compiled using the **4-Step Zero Magic Gadgets Protocol** and includes a **3-Tier Progressive Hint Cascade**.

---

### Tier 1: Stepping Stone (`P01` – `P08`)

---

#### P01 — `[USACO07OPEN] Dining G` (3-Entity Star Compatibility & Middle-Vertex Split vs. 3DM Trap)
- **Judge Coordinates**: [Luogu P2891](https://www.luogu.com.cn/problem/P2891) | [POJ 3281](http://poj.org/problem?id=3281)
- **Exact Constraints**: $N \le 100$ cows, $F \le 100$ foods, $D \le 100$ drinks; each food and drink can be consumed by at most $1$ cow, and each cow $c$ has subsets $F_c \subseteq \{1, \dots, F\}$ and $D_c \subseteq \{1, \dots, D\}$ of acceptable foods and drinks. Maximize the number of cows fed both a liked food and a liked drink.
- **Step 1: Non-Graph Diagnostic Signal**:
  We are matching triplets $(f, c, d) \in F \times C \times D$ where each entity has capacity $1$. While general 3-Dimensional Matching (3DM) is NP-hard, here compatibility is a **Star Graph** $F \text{--} C \text{--} D$: food $f$ and drink $d$ are conditionally independent given cow $c$ ($\text{Valid}(f, c, d) \iff (f \in F_c) \land (d \in D_c)$).
- **Step 2: Intermediate Algebraic Representation**:
  Introduce flow variables $x_{f,c} \in \{0, 1\}$ for $(f \in F_c)$ and $y_{c,d} \in \{0, 1\}$ for $(d \in D_c)$, plus cow indicator $z_c \in \{0, 1\}$:

  $$
  \max \sum_{c=1}^N z_c \quad \text{s.t.} \quad \sum_{c : f \in F_c} x_{f,c} \le 1, \quad \sum_{c : d \in D_c} y_{c,d} \le 1, \quad \sum_{f \in F_c} x_{f,c} = z_c = \sum_{d \in D_c} y_{c,d}, \quad z_c \le 1.
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. The equation $\sum_{f \in F_c} x_{f,c} = z_c = \sum_{d \in D_c} y_{c,d}$ with $z_c \le 1$ is flow conservation through a **split vertex** $c_{\text{in}} \xrightarrow{\text{cap } 1} c_{\text{out}}$!
  2. Edges: $S \to f$ (cap $1$), $f \to c_{\text{in}}$ (cap $1$ for $f \in F_c$), $c_{\text{in}} \to c_{\text{out}}$ (cap $1$), $c_{\text{out}} \to d$ (cap $1$ for $d \in D_c$), $d \to T$ (cap $1$).
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: Unit-capacity network with $|V| = F + 2N + D + 2 \le 402$; Dinic runs in $O(E \sqrt{V}) \approx 10^4$ operations.
  - **Broken Gadget Warning**: Putting $C$ on the left ($S \to c \to f \to d \to T$) or failing to split $c \mapsto (c_{\text{in}}, c_{\text{out}})$ fails catastrophically: if $c$ is not split, a cow can consume $2$ foods and $2$ drinks (stealing capacity from other cows); if $F$ is in the middle, food $f$ suffers from **Flow Amnesia (`流量失忆`)** and routes flow from cow $c_1$ to a drink $d_2$ liked only by cow $c_2$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Why isn't this NP-hard 3-Dimensional Matching? Which of the three entities ($F, C, D$) connects to the other two?
  - *Hint 2*: Place the central entity ($C$) in the middle layer so every $S \to T$ path represents a valid $(f, c, d)$ triple.
  - *Hint 3*: How do you prevent two different $(f_1, d_1)$ and $(f_2, d_2)$ paths from both passing through the same cow vertex $c$? Split $c \to (c_{\text{in}}, c_{\text{out}})$ with capacity $1$.

---

#### P02 — `[NOI2008] 志愿者招募` (Column-Consecutive-Ones $DA\mathbf{x} = \mathbf{0}$ vs. LP Dual Prefix Potentials)
- **Judge Coordinates**: [Luogu P3980](https://www.luogu.com.cn/problem/P3980) | [LOJ 6226](https://loj.ac/p/6226)
- **Exact Constraints**: $N \le 1000$ days, $M \le 10000$ volunteer types; day $t$ requires at least $A_t$ volunteers; type $j$ works on contiguous days $[S_j, T_j]$ at cost $C_j$ per person. Minimize total hiring cost.
- **Step 1: Non-Graph Diagnostic Signal**:
  Each decision variable $x_j \ge 0$ covers a contiguous range of constraints $t \in [S_j, T_j]$ (**Column-Consecutive-Ones Property**). Greedy fails because overlapping intervals trade off against each other; DP fails because up to $M$ intervals can overlap with unbounded counts $x_j$.
- **Step 2: Intermediate Algebraic Representation**:
  Introduce excess slack $y_t \ge 0$ on day $t$ ($1 \le t \le N$) so every day constraint is an exact equality $E_t$:

  $$
  E_t : \quad \sum_{j : t \in [S_j, T_j]} x_j - y_t = A_t \quad (1 \le t \le N), \qquad E_0 : 0 = 0, \quad E_{N+1} : 0 = 0.
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  Apply the difference operator $E'_t = E_t - E_{t-1}$ for $t = 1, \dots, N+1$:
  1. Variable $x_j$ (covering $[S_j, T_j]$) cancels in every $E'_t$ except at $t = S_j$ ($+x_j$) and $t = T_j + 1$ ($-x_j$). Thus $x_j$ becomes a directed edge **$S_j \to T_j + 1$** with capacity $\infty$ and cost $C_j$.
  2. Slack variable $y_t$ appears only in $E'_t$ ($-y_t$) and $E'_{t+1}$ ($+y_t$). Thus $y_t$ becomes a reverse backbone edge **$(t + 1) \to t$** with capacity $\infty$ and cost $0$.
  3. The RHS becomes net supply $b_t = A_t - A_{t-1}$ at vertex $t \in \{1, \dots, N+1\}$ (with $A_0 = A_{N+1} = 0$). Connect source $S_{\text{src}} \to t$ (cap $b_t$, cost $0$) if $b_t > 0$, and $t \to T_{\text{snk}}$ (cap $-b_t$, cost $0$) if $b_t < 0$.
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|V| = N + 3 \le 1003$, $|E| = M + 2N + 1 \le 12001$; MCMF runs in $< 50\text{ ms}$.
  - **Broken Gadget Warning**: Creating a $(N+1)$-th sentinel vertex is **mandatory**; without vertex $N+1$, intervals ending at $T_j = N$ have no $-x_j$ sink endpoint!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Write the $N$ inequalities as equalities by subtracting non-negative surplus variables $y_t \ge 0$.
  - *Hint 2*: Subtract equation $t-1$ from equation $t$ for $t = 1, \dots, N+1$ (setting $E_0$ and $E_{N+1}$ to $0=0$). How many times does $x_j$ appear now?
  - *Hint 3*: Each variable now has one $+1$ and one $-1$, which is a Kirchhoff flow network on vertices $1, \dots, N+1$.

---

#### P03 — `[ZJOI2013] 防守战线` (Row-Consecutive-Ones Transpose Dual to MCMF)
- **Judge Coordinates**: [Luogu P3337](https://www.luogu.com.cn/problem/P3337)
- **Exact Constraints**: $n \le 1000$ positions (cost $c_i$ to place at most $1$ tower at $i$), $m \le 10000$ intervals $[l_j, r_j]$ requiring $\sum_{i=l_j}^{r_j} x_i \ge d_j$.
- **Step 1: Non-Graph Diagnostic Signal**:
  Here variables $x_i \in [0, 1]$ are **points** and constraints are **intervals** (**Row-Consecutive-Ones**). This is the exact transpose of `P02`.
- **Step 2: Intermediate Algebraic Representation**:
  By Theorem 2.2 (and worked derivation in Section 2.6), substituting prefix potentials $p_i = \sum_{k=1}^i x_k$ turns the Primal LP into a difference-constraint system $p_{r_j} - p_{l_j-1} \ge d_j$, $0 \le p_i - p_{i-1} \le 1$, or equivalently dualizing $\min\{\mathbf{c}^\top \mathbf{x} : A\mathbf{x} \ge \mathbf{d}, \mathbf{0} \le \mathbf{x} \le \mathbf{1}\}$ yields:

  $$
  \max_{\mathbf{f}, \mathbf{z} \ge \mathbf{0}} \sum_{j=1}^m d_j f_j - \sum_{i=1}^n z_i \quad \text{s.t.} \quad \sum_{j : i \in [l_j, r_j]} f_j - z_i \le c_i \;\; (1 \le i \le n).
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  The dual inequality $\sum_{j : i \in [l_j, r_j]} f_j - z_i + y_i = c_i$ (with slack $y_i \ge 0$) has **Column-Consecutive-Ones** in $f_j$! Applying $E'_i = E_i - E_{i-1}$ on vertices $1, \dots, n+1$:
  - $f_j \ge 0$: Directed edge $l_j \to r_j + 1$ (cap $\infty$, min-cost $-d_j$).
  - $y_i \ge 0$ (from $\le c_i$): Directed edge $i \to i + 1$ (cap $\infty$, cost $0$).
  - $z_i \ge 0$ (from $x_i \le 1$): Directed edge $i + 1 \to i$ (cap $\infty$, cost $+1$).
  - Supplies: $b_i = c_i - c_{i-1}$ ($c_0 = c_{n+1} = 0$).
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: MCMF on $n+1$ vertices and $m + 2n$ edges; since all interval edges go forward ($l_j < r_j+1$) and only $+1$-cost $z_i$ edges go backward, there are **no negative cycles**.
  - **Broken Gadget Warning**: See the 3 Broken Gadgets proved in Section 2.6.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Compare the constraint matrix of this problem with `[NOI2008] 志愿者招募`: how are they related?
  - *Hint 2*: Either write $x_i = p_i - p_{i-1}$ and take the LP Dual, or take the LP Dual first so that interval multipliers $f_j$ form a Column-Consecutive-Ones matrix.
  - *Hint 3*: Don't forget the upper bound $x_i \le 1$: in the Dual, it creates a reverse edge $i+1 \to i$ with cost $+1$ and capacity $\infty$.

---

#### P04 — `Codeforces 362E — Petya and Pipes` (Elastic Cut Dual / Two-Regime Capacity Expansion)
- **Judge Coordinates**: [Codeforces 362E](https://codeforces.com/problemset/problem/362/E)
- **Exact Constraints**: $n \le 50$ vertices, directed capacities $c_{uv} \ge 0$, expansion budget $K \le 1000$. Each existing edge $(u, v)$ can have its capacity increased by $\delta_{uv} \in \mathbb{Z}_{\ge 0}$ at cost $1$ per unit. Maximize the $1$-to-$n$ flow subject to $\sum \delta_{uv} \le K$.
- **Step 1: Non-Graph Diagnostic Signal**:
  Each edge $(u, v)$ has two marginal cost regimes for routing flow: the first $c_{uv}$ units cost $0$, and any additional flow costs $1$ per unit up to total budget $K$.
- **Step 2: Intermediate Algebraic Representation**:
  Split the flow on each existing edge $e = (u, v)$ into base flow $f_e^{(0)} \in [0, c_e]$ (cost $0$) and expanded flow $f_e^{(1)} \in [0, \infty)$ (cost $1$):

  $$
  \max \text{val}(\mathbf{f}^{(0)} + \mathbf{f}^{(1)}) \quad \text{s.t.} \quad \sum_{e \in E} 1 \cdot f_e^{(1)} \le K.
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  For each original edge $e = (u, v)$ with $c_{uv} > 0$, place two parallel directed edges:
  1. $e^{(0)}: u \to v$ with capacity $c_{uv}$ and cost $0$;
  2. $e^{(1)}: u \to v$ with capacity $\infty$ and cost $+1$.
  Run Successive Shortest Path (SSP) MCMF from $1$ to $n$. In each step, let $d$ be the shortest path cost from $1$ to $n$:
  - If $d = 0$, augment all available capacity along cost-$0$ paths.
  - If $d > 0$, we can afford at most $\lfloor \text{remaining\_K} / d \rfloor$ additional units of flow along this path. Stop when $d > \text{remaining\_K}$ or no path exists.
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: Base max-flow + at most $K \le 1000$ unit-cost augmentations $= O(K \cdot M \log N) \approx 2.5 \times 10^6$ ops.
  - **Broken Gadget Warning**: Do **not** add expansion edges $e^{(1)}$ for pairs $(u, v)$ that had $c_{uv} = 0$ (no pipe exists in the input)!
- **3-Tier Progressive Hints**:
  - *Hint 1*: How much does it cost to send $f$ units of flow through a pipe of initial capacity $c$?
  - *Hint 2*: The cost function $\max(0, f - c)$ is convex and piecewise-linear with slope $0$ on $[0, c]$ and slope $1$ on $[c, \infty)$.
  - *Hint 3*: Model each pipe as two parallel edges and run SSP MCMF until the total cost would exceed $K$.

---

#### P05 — `POJ 3680 — Intervals` (Coordinate-Compressed Weighted Interval $k$-Packing via $DA\mathbf{x} = \mathbf{0}$)
- **Judge Coordinates**: [POJ 3680](http://poj.org/problem?id=3680) | [Luogu SP3871](https://www.luogu.com.cn/problem/SP3871)
- **Exact Constraints**: $N \le 200$ open intervals $(a_j, b_j)$ with weights $w_j > 0$, coordinates up to $10^5$, capacity $K \le 10^5$ (at most $K$ chosen intervals may cover any real point). Maximize $\sum w_j x_j$ for $x_j \in \{0, 1\}$.
- **Step 1: Non-Graph Diagnostic Signal**:
  Maximum-weight $k$-colorable interval subgraph (or $k$-capacitated interval packing). Coordinate-compress the $2N \le 400$ endpoints into $M \le 400$ elementary segments. The constraint matrix over elementary segments is **Column-Consecutive-Ones**.
- **Step 2: Intermediate Algebraic Representation**:
  After coordinate compression, interval $j$ covers contiguous elementary segments $[l_j, r_j - 1]$. With slack $y_t \ge 0$ on segment $t \in \{1, \dots, M-1\}$:

  $$
  E_t : \quad \sum_{j : t \in [l_j, r_j-1]} x_j + y_t = K \quad (1 \le t \le M - 1), \qquad x_j \in [0, 1], \; y_t \ge 0.
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  Subtract $E'_t = E_t - E_{t-1}$ ($1 \le t \le M$, with $E_0 = E_M = 0$):
  1. $x_j \in [0, 1]$: Directed chord edge $l_j \to r_j$ with **capacity $1$** and **min-cost $-w_j$**.
  2. $y_t \ge 0$: Directed backbone edge $t \to t + 1$ with **capacity $\infty$** and **cost $0$**.
  3. Supply $+K$ at vertex $1$ ($S \to 1$, cap $K$, cost $0$) and demand $-K$ at vertex $M$ ($M \to T$, cap $K$, cost $0$).
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: DAG on $M \le 400$ vertices with $N + M \le 600$ edges; MCMF runs in $O(N \cdot M \log M)$ using topological Johnson potentials (or SPFA).
  - **Broken Gadget Warning**: Because the problem uses **open** intervals $(a_j, b_j)$, two intervals $(1, 3)$ and $(3, 5)$ do **not** overlap at $3$! Thus $(a_j, b_j)$ maps directly to directed edge $\text{id}(a_j) \to \text{id}(b_j)$ (whereas closed intervals $[a_j, b_j]$ map to $\text{id}(a_j) \to \text{id}(b_j) + 1$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Only the $2N \le 400$ endpoints matter; discretize them into sorted coordinates $p_1 < p_2 < \dots < p_M$.
  - *Hint 2*: Imagine $K$ parallel timelines (units of flow) travelling from $p_1$ to $p_M$.
  - *Hint 3*: Taking interval $(p_{l_j}, p_{r_j})$ corresponds to $1$ unit of flow jumping along chord $l_j \to r_j$ at cost $-w_j$ instead of walking along the free backbone $t \to t+1$.

---

#### P06 — `Codeforces 704D — Captain America` (Two Partition Matroids / Bipartite Bounded Degree Flow)
- **Judge Coordinates**: [Codeforces 704D](https://codeforces.com/problemset/problem/704/D)
- **Exact Constraints**: $N \le 10^5$ points $(x_i, y_i)$ on a 2D grid, $M \le 10^5$ row/column discrepancy constraints ($\big|\#R(L) - \#B(L)\big| \le d_L$ on line $L$). Painting a point Red costs $r$, Blue costs $b$. Minimize total cost.
- **Step 1: Non-Graph Diagnostic Signal**:
  Assume WLOG $r \le b$ (otherwise swap $r, b$). Base cost is $N \cdot b$, and choosing $x_i = 1$ (Red) saves $b - r \ge 0$ per point. Each point $(x_i, y_i)$ belongs to **one horizontal line $X_u$** and **one vertical line $Y_v$**: this is a **Bipartite Incidence Matrix** (intersection of two Partition Matroids!).
- **Step 2: Intermediate Algebraic Representation**:
  If line $L$ has $cnt_L$ points and the tightest discrepancy bound is $d_L$, then $2 \cdot \text{sum}(L) - cnt_L \in [-d_L, +d_L]$, which forces the integer lower and upper bounds:

  $$
  L_{\text{line}} = \left\lceil \frac{cnt_L - d_L}{2} \right\rceil \le \sum_{i \in L} x_i \le \left\lfloor \frac{cnt_L + d_L}{2} \right\rfloor = R_{\text{line}}.
  $$

  If $L_{\text{line}} > R_{\text{line}}$ for any line, output `-1` immediately.
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. Left vertices: active X-lines $u$ ($S \to u$ with lower/upper capacity $[L_u, R_u]$).
  2. Right vertices: active Y-lines $v$ ($v \to T$ with lower/upper capacity $[L_v, R_v]$).
  3. Each point $i = (x_i, y_i)$ is a directed edge $u(x_i) \to v(y_i)$ with capacity $[0, 1]$.
  4. Solve **Maximum Flow with Lower and Upper Capacities** (`有源汇上下界最大流`): first check feasibility via super-source $S^*$ / super-sink $T^*$ on edge $T \to S$ (cap $\infty$), then augment in the residual network from $S$ to $T$ to maximize $\sum x_i$.
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: Bipartite-like bounded flow with $|V|, |E| \le 2 \times 10^5$; Dinic runs in $O(E \sqrt{V})$ time!
  - **Broken Gadget Warning**: Multiple constraints on the same line $x = c$ or $y = c$ may appear in the input; always take $d_L = \min(\text{all } d \text{ on line } L)$ before computing $[L_{\text{line}}, R_{\text{line}}]$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Map each point $(x_i, y_i)$ to an edge between row node $x_i$ and column node $y_i$.
  - *Hint 2*: Rewrite $|R - B| \le d$ with $R + B = cnt$ as an interval $[L, U]$ on the number of Red points $R$.
  - *Hint 3*: Use $s$-$t$ Maximum Flow with Lower Bounds (`上下界最大流`) and inspect whether edge $i$ carries flow $1$ in the final network to print `r` or `b`.

---

#### P07 — `[BZOJ 1283] 序列` (Toeplitz Band Sliding-Window Consecutive-Ones $k$-Packing)
- **Judge Coordinates**: [Hydro BZOJ 1283](https://hydro.ac/d/bzoj/p/1283)
- **Exact Constraints**: Array $c_1, \dots, c_N \ge 0$ ($N \le 1000$). Choose $x_i \in \{0, 1\}$ to maximize $\sum_{i=1}^N c_i x_i$ subject to: every contiguous window of length $M$ has at most $K$ chosen elements ($\sum_{j=i}^{i+M-1} x_j \le K$ for all $1 \le i \le N - M + 1$).
- **Step 1: Non-Graph Diagnostic Signal**:
  Look at the variable $x_j$: which window constraints $E_i$ ($1 \le i \le N - M + 1$) contain $x_j$? Exactly those windows with $\max(1, j - M + 1) \le i \le \min(j, N - M + 1)$—a **contiguous range of rows**! Thus the matrix is **both Row-C1P and Column-C1P** (a Toeplitz band matrix).
- **Step 2: Intermediate Algebraic Representation**:
  Pad with dummy constraints or view directly in Primal space: choosing $x_j = 1$ occupies $1$ unit of capacity across time steps $[j, j + M - 1]$. With slack $y_t \ge 0$:

  $$
  E_t : \quad \sum_{j = \max(1, t - M + 1)}^{t} x_j + y_t = K \quad (1 \le t \le N), \qquad x_j \in [0, 1].
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  Subtract $E'_t = E_t - E_{t-1}$ on vertices $1, \dots, N + 1$:
  1. Variable $x_j \in [0, 1]$ enters at $t = j$ and leaves at $t = \min(j + M, N + 1)$: directed chord edge **$j \to \min(j + M, N + 1)$** with **capacity $1$** and **min-cost $-c_j$**.
  2. Slack $y_t \ge 0$: directed backbone edge **$t \to t + 1$** with **capacity $\infty$** and **cost $0$**.
  3. Supply $+K$ at vertex $1$ ($S \to 1$, cap $K$, cost $0$) and demand $-K$ at vertex $N + 1$.
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $N + 1 \le 1001$ vertices, $2N \le 2000$ edges, $K$ units of flow; MCMF runs in $< 20\text{ ms}$.
  - **Broken Gadget Warning**: Don't forget to clamp the right endpoint of chord $j$ to $\min(j + M, N + 1)$ when $j + M > N + 1$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Choosing element $j$ consumes $1$ slot in every window that covers $j$, which is equivalent to blocking $1$ token for $M$ steps $[j, j+M-1]$.
  - *Hint 2*: Send $K$ tokens from index $1$ to index $N+1$.
  - *Hint 3*: A token can either step $t \to t+1$ for free (not picking $t$) or jump $j \to \min(j+M, N+1)$ (capacity $1$, reward $c_j$).

---

#### P08 — `AtCoder ARC 085 E — MUL` (Divisibility Poset Submodular Closure & LP Dual Integrality)
- **Judge Coordinates**: [AtCoder ARC085E](https://atcoder.jp/contests/arc085/tasks/arc085_c)
- **Exact Constraints**: $N \le 100$ gems indexed $1, \dots, N$ with values $a_i \in [-10^9, 10^9]$. We may smash all gems at multiples of $x$ ($x, 2x, 3x, \dots$) for any chosen $x \in \{1, \dots, N\}$. Maximize the sum of remaining gems.
- **Step 1: Non-Graph Diagnostic Signal**:
  Let $S \subseteq \{1, \dots, N\}$ be the set of **surviving** gems. If gem $i$ survives ($i \in S$), we could not have executed operation $x = i$, and conversely if we decide not to smash $i$, any multiple $k \cdot i$ that requires $i$ to be smashed creates a **poset closure dependency**: more clean is to define $x_i = 1$ if we **keep** gem $i$ (or if we **smash** $i$). Wait: if we smash all multiples of $i$, then keeping gem $j$ forbids choosing operation $i$ for any divisor $i \mid j$. Even simpler: the family of sets smashed by sequences of operations is closed under divisibility multiples ($i \text{ smashed} \implies k \cdot i \text{ smashed}$)!
- **Step 2: Intermediate Algebraic Representation**:
  Let $y_i \in \{0, 1\}$ be $1$ if gem $i$ is **kept** and $0$ if gem $i$ is **smashed**. Since smashing $i$ forces all multiples $k \cdot i$ ($k \ge 2$) to be smashed, contrapositively **keeping $k \cdot i$ requires keeping $i$** ($y_{k \cdot i} \le y_i$, or equivalently in the complement $z_i = 1 - y_i$: $z_i = 1 \implies z_{k \cdot i} = 1$):

  $$
  \max_{\mathbf{y} \in \{0, 1\}^N} \sum_{i=1}^N a_i y_i \quad \text{s.t.} \quad y_j - y_i \le 0 \quad (\forall i \mid j, \; j > i).
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  Notice that every constraint $y_j - y_i \le 0$ has one $+1$ and one $-1$ (**Transpose of a Directed Incidence Matrix**, Totally Unimodular!). This is **Maximum Weight Closure (`最大权闭合子图`)** on the divisibility DAG:
  1. Start with baseline sum of all positive gems: $\text{Base} = \sum_{i : a_i > 0} a_i$.
  2. For each $i$ with $a_i > 0$: edge $S \to i$ with capacity $a_i$.
  3. For each $i$ with $a_i < 0$: edge $i \to T$ with capacity $-a_i$.
  4. For each $i$ and multiple $j = k \cdot i$ ($k \ge 2$): edge $j \to i$ with capacity $\infty$ (if $j \in S_{\text{keep}}$, then $i \in S_{\text{keep}}$; or in the smash orientation, $S \to i$ for $-a_i > 0$, $i \to j$ with cap $\infty$, and $j \to T$ for $a_j > 0$).
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|V| = N + 2 \le 102$, $|E| = O(N \log N) \le 600$; Dinic runs in $< 1\text{ ms}$ (use `long long` for capacities up to $10^9$!).
  - **Broken Gadget Warning**: Wait—why is "smashing multiples of $i$" identical to the closure $z_i \le z_{k \cdot i}$? Because if $z_i = 1$ ($i$ is smashed) implies $z_{k \cdot i} = 1$ for all $k \ge 2$, then **any** upper-closed set $Z$ can be generated simply by executing the smash operation on every $i \in Z$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Suppose you decide which subset of gems $Z \subseteq \{1, \dots, N\}$ will end up smashed. What necessary and sufficient condition must $Z$ satisfy?
  - *Hint 2*: A subset $Z$ can be exactly smashed if and only if for every $i \in Z$ and every multiple $j = k \cdot i \le N$, we also have $j \in Z$.
  - *Hint 3*: This is a closure constraint ($i \in Z \implies k \cdot i \in Z$), solved by $\sum_{a_i > 0} a_i - \text{MinCut}(S, T)$.

---

### Tier 2: Intermediate (`P09` – `P16`)

---

#### P09 — `[SHOI2004] 最小生成树` (Symmetric Inverse MST & SPFA Weight Recovery)
- **Judge Coordinates**: [Luogu P4412](https://www.luogu.com.cn/problem/P4412) | [BZOJ 1937](https://hydro.ac/d/bzoj/p/1937)
- **Exact Constraints**: Undirected graph with $N \le 50$ vertices, $M \le 1000$ edges, initial weights $w_e$, and a given spanning tree $T$. Modify edge weights to $w'_e$ to minimize $\sum_{e \in E} |w'_e - w_e|$ so that $T$ becomes an MST. (Luogu P4412 asks to output the modified weights $w'_e$; BZOJ 1937 asks for the minimum total modification.)
- **Step 1: Non-Graph Diagnostic Signal**:
  We are given the target combinatorial object (tree $T$) and want the minimum $L_1$ perturbation of weights so $T$ is optimal (**Inverse Optimization**).
- **Step 2: Intermediate Algebraic Representation**:
  By Section 3.3, let $x_f = w_f - w'_f \ge 0$ for tree edges $f \in T$ and $y_e = w'_e - w_e \ge 0$ for non-tree edges $e \in E \setminus T$. Then $T$ is an MST iff:

  $$
  \min_{\mathbf{x}, \mathbf{y} \ge \mathbf{0}} \sum_{f \in T} x_f + \sum_{e \notin T} y_e \quad \text{s.t.} \quad x_f + y_e \ge w_f - w_e \quad \big(\forall e = (u, v) \notin T, \; \forall f \in P_T(u, v) \text{ with } w_f > w_e\big).
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  By the Master Primal–Dual Dictionary, this vertex-cover-like bipartite LP dualizes to **Maximum Weight Bipartite Matching (KM)** or **Min-Cost Flow**:
  - Source $S \to f \in T$ (cap $1$, cost $0$);
  - $f \to e \in E \setminus T$ (cap $\infty$, cost $-(w_f - w_e)$ whenever $w_f > w_e$ and $f \in P_T(u_e, v_e)$);
  - $e \to T_{\text{snk}}$ (cap $1$, cost $0$).
  - Augment shortest $S \to T_{\text{snk}}$ paths **only while path cost $< 0$** (or run KM on the bipartite graph $T \times (E \setminus T)$ with weights $\max(0, w_f - w_e)$).
  - **Recovering $w'_e$**: If using KM, the vertex labels $lx[f], ly[e]$ directly satisfy $lx[f] + ly[e] \ge w_f - w_e$ and $\sum lx[f] + \sum ly[e] = \text{OPT}$, so $w'_f = w_f - lx[f]$ and $w'_e = w_e + ly[e]$! If using MCMF, run the post-augmentation SPFA from Section 4.2 with $\text{dist}[S] = \text{dist}[T_{\text{snk}}] = 0$ (see Trace 1 in Section 4.5).
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: Bipartite sides $|T| = N - 1 \le 49$ and $|E \setminus T| \le 950$; KM or MCMF runs in $O(N \cdot M^2) \le 10^7$ ops.
  - **Broken Gadget Warning**: If using MCMF, do **not** force full max-flow if some paths have cost $0$; stop augmenting as soon as $\text{dist}[T_{\text{snk}}] \ge 0$, and tie $\text{dist}[S] = \text{dist}[T_{\text{snk}}] = 0$ when recovering potentials!
- **3-Tier Progressive Hints**:
  - *Hint 1*: When is a spanning tree $T$ an MST? Check the fundamental cycle $P_T(u, v) \cup \{e\}$ of every non-tree edge $e = (u, v) \notin T$.
  - *Hint 2*: Write the condition as $x_f + y_e \ge w_f - w_e$ for $f \in T$ and $e \notin T$. Why is this a bipartite graph between $T$ and $E \setminus T$?
  - *Hint 3*: Dualize to Maximum Weight Bipartite Matching (KM); the optimal weight adjustments are the KM dual vertex labels!

---

#### P10 — `[BZOJ 3118] Orz the Immortal` (Asymmetric Weighted Inverse MST via Capacitated Bipartite MCMF)
- **Judge Coordinates**: [Hydro BZOJ 3118](https://hydro.ac/d/bzoj/p/3118)
- **Exact Constraints**: $N \le 300$ vertices, $M \le 1000$ edges; designated tree $T$ given by $f_e \in \{0, 1\}$. Decreasing edge $e$'s weight costs $d_e$ per unit, increasing costs $b_e$ per unit (and tree edges are only decreased while non-tree edges are only increased). Minimize total modification cost so $T$ is an MST.
- **Step 1: Non-Graph Diagnostic Signal**:
  Identical to `P09`, except each tree edge $f \in T$ has modification cost $d_f$ per unit and each non-tree edge $e \notin T$ has modification cost $b_e$ per unit. Because $d_f, b_e$ are no longer $1$, KM vertex labels with capacity $1$ no longer apply—instead, by the **Role Reversal Principle**, the Primal objective coefficients $d_f$ and $b_e$ become the **Dual Edge Capacities**!
- **Step 2: Intermediate Algebraic Representation**:

  $$
  \begin{aligned}
  \text{Primal: } & \min_{\mathbf{x}, \mathbf{y} \ge \mathbf{0}} \sum_{f \in T} d_f x_f + \sum_{e \notin T} b_e y_e \quad \text{s.t.} \quad x_f + y_e \ge \Delta_{f,e} \;\; (\forall f \in P_T(u_e, v_e)), \\
  \text{Dual: } & \max_{\mathbf{z} \ge \mathbf{0}} \sum_{f, e} \Delta_{f,e} z_{f,e} \quad \text{s.t.} \quad \sum_{e} z_{f,e} \le d_f \; (\forall f \in T), \quad \sum_{f} z_{f,e} \le b_e \; (\forall e \notin T).
  \end{aligned}
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. Source $S \to f \in T$ with **capacity $d_f$** and **cost $0$**.
  2. For each $e \in E \setminus T$ and $f \in P_T(u_e, v_e)$ with $\Delta_{f,e} = w_f - w_e > 0$: edge $f \to e$ with **capacity $\infty$** and **min-cost $-\Delta_{f,e}$**.
  3. Each $e \in E \setminus T \to T_{\text{snk}}$ with **capacity $b_e$** and **cost $0$**.
  4. Run MCMF while shortest path cost $< 0$; return $-\text{MinCost}$.
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|V| \le 1002$, $|E| \le N \cdot M \le 3 \times 10^5$; MCMF runs in $< 0.3\text{ s}$.
  - **Broken Gadget Warning**: Do not swap cost and capacity! $d_f, b_e$ are **capacities**, while $\Delta_{f,e} = w_f - w_e$ is the **cost**.
- **3-Tier Progressive Hints**:
  - *Hint 1*: How does changing the objective from $\sum x_f + \sum y_e$ to $\sum d_f x_f + \sum b_e y_e$ affect the Dual LP?
  - *Hint 2*: By the Role Reversal Principle, Primal objective coefficients become Dual constraint RHS (capacities)!
  - *Hint 3*: Change the capacities of $S \to f$ from $1$ to $d_f$ and $e \to T_{\text{snk}}$ from $1$ to $b_e$, then run MCMF.

---

#### P11 — `[AHOI2014 / JSOI2014] 支线剧情` (Rooted DAG Edge Coverage Lower Bounds & Dual Longest-Path Potentials)
- **Judge Coordinates**: [Luogu P4043](https://www.luogu.com.cn/problem/P4043)
- **Exact Constraints**: A DAG with $N \le 300$ vertices rooted at $1$ (representing a visual novel's story tree/DAG). Every directed edge $e = (u, v)$ has traversal time $t_e \ge 0$ and must be traversed **at least once** across multiple playthroughs starting at vertex $1$ (any playthrough can be reset back to vertex $1$ from any vertex $v > 1$ at cost $0$). Minimize total time to cover all edges.
- **Step 1: Non-Graph Diagnostic Signal**:
  We are routing flow along paths from root $1$ to cover every edge $e \in E$ at least $1$ time ($f_e \in [1, \infty)$) at cost $t_e$, with free return edges $v \to 1$ (cap $\infty$, cost $0$). Equivalently, by **LP Duality**, this is the dual of finding node potentials $\pi_v$ with elastic violation penalties!
- **Step 2: Intermediate Algebraic Representation**:
  In Primal Flow space, each edge $e = (u, v)$ has lower bound $L_e = 1$, upper bound $U_e = \infty$, and cost $t_e$:

  $$
  \min_{\mathbf{f}} \sum_{e \in E} t_e f_e \quad \text{s.t.} \quad \text{div}_{\mathbf{f}}(v) = 0 \;\; (\forall v \in V), \quad f_e \ge 1 \;\; (\forall e \in E_{\text{story}}), \quad f_{v \to 1} \ge 0 \;\; (\forall v > 1).
  $$

  Decomposing $f_e = 1 + f'_e$ ($f'_e \ge 0$) separates the mandatory baseline cost $\sum_{e \in E} t_e$ from the imbalance adjustment flow $\mathbf{f}' \ge \mathbf{0}$!
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. Pre-pay $\text{BaseCost} = \sum_{e \in E} t_e$, and record node excess $\text{excess}[v] = \text{indeg}(v) - \text{outdeg}(v)$ from the mandatory $1$ unit on each edge.
  2. For each story edge $e = (u, v)$: add residual edge $u \to v$ with capacity $\infty$ and cost $t_e$.
  3. For each vertex $v > 1$: add reset edge $v \to 1$ with capacity $\infty$ and cost $0$.
  4. For each $v$ with $\text{excess}[v] > 0$: edge $S^* \to v$ (cap $\text{excess}[v]$, cost $0$); if $\text{excess}[v] < 0$: edge $v \to T^*$ (cap $-\text{excess}[v]$, cost $0$).
  5. Total minimum time $= \text{BaseCost} + \text{MinCostMaxFlow}(S^*, T^*)$.
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|V| \le 302$, $|E| \le 6000$; MCMF runs in $< 30\text{ ms}$.
  - **Broken Gadget Warning**: Do not forget the reset edges $v \to 1$ (cap $\infty$, cost $0$) for all $v > 1$, as the player can restart at $1$ after reaching any node!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Every edge must carry at least $1$ unit of flow, and restarting at vertex $1$ from $v$ is a directed edge $v \to 1$ of cost $0$ and capacity $\infty$.
  - *Hint 2*: Substitute $f_e = 1 + f'_e$ where $f'_e \ge 0$. What is the net flow imbalance at each vertex $v$ from the mandatory $1$s?
  - *Hint 3*: Route the excess $\text{indeg}(v) - \text{outdeg}(v)$ via super-source $S^*$ and super-sink $T^*$ using standard MCMF.

---

#### P12 — `Codeforces 1288F — Red-Blue Graph` (Bipartite Signed Incidence Matrix & 3-State Edge Charge Flow)
- **Judge Coordinates**: [Codeforces 1288F](https://codeforces.com/problemset/problem/1288/F)
- **Exact Constraints**: Bipartite graph $V_1 \sqcup V_2$ ($|V_1|, |V_2|, |E| \le 200$). Each vertex has color `'R'`, `'B'`, or `'U'` (uncolored). Each edge $e$ can be colored Red (cost $r$), Blue (cost $b$), or Uncolored (cost $0$). For `'R'` vertices, $\#\text{RedEdges} \ge \#\text{BlueEdges} + 1$; for `'B'` vertices, $\#\text{BlueEdges} \ge \#\text{RedEdges} + 1$. Minimize total edge cost.
- **Step 1: Non-Graph Diagnostic Signal**:
  Notice that for every vertex constraint, only the **net difference** $(\#\text{RedEdges} - \#\text{BlueEdges})$ matters! On a bipartite graph $V_1 \sqcup V_2$, we can orient every edge $e = (u, v)$ from $u \in V_1$ to $v \in V_2$ and interpret Red as $+1$ flow ($u \to v$), Uncolored as $0$ flow, and Blue as $-1$ flow ($v \to u$)!
- **Step 2: Intermediate Algebraic Representation**:
  Let $f_e = x_e^R - x_e^B \in \{-1, 0, +1\}$ where $x_e^R, x_e^B \in [0, 1]$ have costs $r$ and $b$ respectively. Then for $u \in V_1$, $\sum_{e \ni u} (x_e^R - x_e^B) = \text{Outflow}(u) - \text{Inflow}(u)$, whereas for $v \in V_2$, $\sum_{e \ni v} (x_e^R - x_e^B) = \text{Inflow}(v) - \text{Outflow}(v)$!
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. For each original edge $e = (u, v)$ ($u \in V_1, v \in V_2$):
     - Add Red edge $u \to v$ with capacity $1$ and cost $r$;
     - Add Blue edge $v \to u$ with capacity $1$ and cost $b$.
     (Notice that if both carry flow $1$, they cancel around a positive-cost $2$-cycle $r + b > 0$, which MCMF will never use!)
  2. Connect source $S$ and sink $T$ with lower/upper capacity bounds $[L, U]$ on net divergence:
     - $u \in V_1$: if `'R'`, $S \to u$ has $[1, \infty)$; if `'B'`, $u \to T$ has $[1, \infty)$; if `'U'`, both $S \to u$ and $u \to T$ have $[0, \infty)$.
     - $v \in V_2$ (**orientation flipped!**): if `'R'`, $v \to T$ has $[1, \infty)$; if `'B'`, $S \to v$ has $[1, \infty)$; if `'U'`, both $S \to v$ and $v \to T$ have $[0, \infty)$.
  3. Add $T \to S$ with capacity $[0, \infty]$ and solve Feasible Minimum-Cost Circulation with Lower Bounds (`上下界最小费用可行流`).
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|V| \le 404$, $|E| \le 1200$; lower-bound MCMF runs in $< 30\text{ ms}$.
  - **Broken Gadget Warning**: Remember that for $v \in V_2$, a Red edge $u \to v$ **enters** $v$ (increasing $\text{Inflow}(v)$), so `'R'` on $V_2$ requires $\text{Inflow}(v) - \text{Outflow}(v) \ge 1$ (an edge $v \to T$ with lower bound $1$), the **exact opposite** of `'R'` on $V_1$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Every constraint depends only on $(\#\text{Red}) - (\#\text{Blue})$ incident to a vertex.
  - *Hint 2*: Orient edges from $V_1$ to $V_2$: a Red edge sends $1$ unit $u \to v$ (cost $r$), a Blue edge sends $1$ unit $v \to u$ (cost $b$).
  - *Hint 3*: Enforce $\text{Out}(u) - \text{In}(u) \ge 1$ (or $\le -1$) using lower-bound edges $[1, \infty)$ from $S$ or to $T$.

---

#### P13 — `[ONTAK 2010 / Luogu P6967] Vacation` & `[LOJ 6079] Delight for a Cat` (Two-Sided Window Bounds $[L, R]$ & Schedule Recovery)
- **Judge Coordinates**: [Luogu P6967](https://www.luogu.com.cn/problem/P6967) | [LOJ 6079](https://loj.ac/p/6079)
- **Exact Constraints**: $n \le 1000$ hours; in hour $i$, sleeping earns $s_i$ and eating earns $e_i$. In every contiguous window of length $k$, the cat must sleep at least $m_S$ hours and eat at least $m_E$ hours. Maximize total happiness and output the `S`/`E` schedule string.
- **Step 1: Non-Graph Diagnostic Signal**:
  Pre-assign every hour to Sleep (base profit $\sum_{i=1}^n s_i$), and let $x_i \in \{0, 1\}$ indicate switching hour $i$ to Eat (marginal profit $w_i = e_i - s_i$). Then every length-$k$ window requires **both** a lower bound and an upper bound on $\sum_{j=t}^{t+k-1} x_j$:

  $$
  L \stackrel{\text{def}}{=} m_E \le \sum_{j=t}^{t+k-1} x_j \le k - m_S \stackrel{\text{def}}{=} R \quad (1 \le t \le n - k + 1).
  $$

- **Step 2: Intermediate Algebraic Representation**:
  How do we convert a **two-sided inequality** $L \le \sum_{j=t}^{t+k-1} x_j \le R$ into an equality for row differencing $DA\mathbf{x} = D\mathbf{b}$? Introduce a **bounded slack variable** $y_t \in [0, R - L]$!

  $$
  E_t : \quad \sum_{j=t}^{t+k-1} x_j + y_t = R \quad \text{where } 0 \le y_t \le R - L = k - m_S - m_E, \quad 0 \le x_j \le 1.
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  Pad early/late equations or apply $E'_t = E_t - E_{t-1}$ cleanly on vertices $1, \dots, n - k + 2$ (specifically, let $M = n - k + 1$ be the number of windows; variable $x_j$ appears in windows $[\max(1, j - k + 1), \min(j, M)]$, which is a single contiguous range $[l_j, r_j]$ of rows!):
  1. Variable $x_j \in [0, 1]$: Directed chord edge **$l_j \to r_j + 1$** with **capacity $1$** and **min-cost $-w_j = -(e_j - s_j)$**.
  2. Bounded slack $y_t \in [0, R - L]$: Directed backbone edge **$t \to t + 1$** ($1 \le t \le M$) with **capacity $R - L = k - m_S - m_E$** and **cost $0$**!
  3. Supply $+R$ at vertex $1$ ($S \to 1$, cap $R$, cost $0$) and demand $-R$ at vertex $M + 1$ ($M + 1 \to T$, cap $R$, cost $0$).
  4. **Schedule Reconstruction**: After running MCMF, inspect the flow $f^*(e_j) \in \{0, 1\}$ on each chord edge $l_j \to r_j + 1$: if $f^*(e_j) = 1$, print `'E'`, else print `'S'`!
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|V| = n - k + 4 \le 1004$, $|E| \le 2n + 2 \le 2002$; MCMF runs in $< 30\text{ ms}$.
  - **Broken Gadget Warning**: In `P07` (`BZOJ 1283`), the window constraint was one-sided ($\le K$), so backbone edges $t \to t+1$ had capacity $\infty$. Here, the lower bound $\ge L$ is enforced precisely by restricting the backbone slack edge $y_t$ to capacity $R - L$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Rewrite the two conditions ($\ge m_E$ Eating and $\ge m_S$ Sleeping) as $m_E \le \sum_{j=t}^{t+k-1} x_j \le k - m_S$.
  - *Hint 2*: Turn $L \le \text{sum}_t \le R$ into an exact equation $\text{sum}_t + y_t = R$ with a **bounded slack variable** $0 \le y_t \le R - L$.
  - *Hint 3*: Subtract consecutive window equations $E_t - E_{t-1}$: each $x_j$ covers a contiguous range of windows $[l_j, r_j]$, becoming a capacity-$1$ edge $l_j \to r_j + 1$, and $y_t$ becomes a capacity-$(R-L)$ backbone edge $t \to t+1$.

---

#### P14 — `[WC2007] 剪刀石头布` (Landau's Tournament Base Polyhedron $B(f)$ & Convex Marginal Splitting)
- **Judge Coordinates**: [Luogu P4249](https://www.luogu.com.cn/problem/P4249)
- **Exact Constraints**: A tournament on $N \le 100$ players where some directed edges $u \to v$ ($u$ beats $v$) are already fixed and the remaining edges are undecided. Complete the orientation of all undecided edges to **maximize the number of cyclic 3-tuples (rock-paper-scissors triples)**, and output the completed adjacency matrix.
- **Step 1: Non-Graph Diagnostic Signal**:
  Counting cyclic triples $\{u, v, w\}$ directly is a cubic interaction ($O(N^3)$ variables). Flip to the **complement**: a triple $\{u, v, w\}$ is **non-cyclic (transitive)** if and only if one of its 3 vertices beats the other 2! Across the entire tournament, if player $u$ has out-degree $d_u^+ = \sum_{v \neq u} x_{uv}$, then $u$ is the "2-win dominator" of exactly $\binom{d_u^+}{2}$ transitive triples!
- **Step 2: Intermediate Algebraic Representation**:
  Therefore, the number of cyclic triples is strictly determined by the out-degree sequence $(d_1^+, \dots, d_N^+)$:

  $$
  \#\text{CyclicTriples} = \binom{N}{3} - \sum_{u=1}^N \binom{d_u^+}{2},
  $$

  where by **Landau's Theorem (1953)**, achievable out-degree vectors $\mathbf{d}^+$ form the **Base Polyhedron $B(f)$** of the submodular function $f(S) = \binom{|S|}{2} + |S|(N - |S|)$ (represented by routing $1$ unit of flow from each undecided pair $\{u, v\}$ to either $u$ or $v$!).
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  We want to **minimize the separable convex function** $\sum_{u=1}^N \binom{d_u^+}{2}$:
  1. Notice the marginal increments of $\binom{d}{2}$ are strictly increasing integers:

     $$
     \binom{d+1}{2} - \binom{d}{2} = d \quad \text{for } d = 0, 1, 2, \dots, N - 2.
     $$

  2. For each undecided pair $e = \{u, v\}$: create an edge vertex $e$ with $S \to e$ (cap $1$, cost $0$), and directed edges $e \to u$ (cap $1$, cost $0$) and $e \to v$ (cap $1$, cost $0$).
  3. Let $d_{u,0}^+$ be the number of already-fixed wins of player $u$. Add $N - 1 - d_{u,0}^+$ parallel edges from $u \to T$, each of **capacity $1$**, with marginal costs $d_{u,0}^+, \; d_{u,0}^+ + 1, \; d_{u,0}^+ + 2, \; \dots, \; N - 2$.
  4. Run MCMF and read off whether $e \to u$ or $e \to v$ carries flow $1$ to reconstruct the tournament matrix!
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|V| \le \binom{N}{2} + N + 2 \le 5052$; MCMF runs in $< 0.2\text{ s}$.
  - **Broken Gadget Warning**: Because $\binom{d+1}{2} - \binom{d}{2} = d$ is **increasing** in $d$, MCMF automatically saturates the cheaper parallel edges $u \to T$ ($d = 0, 1, 2, \dots$) in exact order without needing any ordering gadgets!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Instead of counting cyclic triples $\{u, v, w\}$, count **non-cyclic (transitive)** triples! How many transitive triples have $u$ beating both $v$ and $w$?
  - *Hint 2*: Exactly $\binom{d_u^+}{2}$! So maximizing cyclic triples is equivalent to minimizing $\sum_{u=1}^N \binom{d_u^+}{2}$.
  - *Hint 3*: Since $\binom{d+1}{2} - \binom{d}{2} = d$ is convex, represent each additional win of player $u$ by parallel capacity-$1$ edges $u \to T$ with costs $0, 1, 2, \dots, N-2$.

---

#### P15 — `[BZOJ 1937 / Directed Tree Path Coverage]` (Rooted Tree Incidence Difference Matrix $D_T$)
- **Judge Coordinates**: [Hydro BZOJ 1937](https://hydro.ac/d/bzoj/p/1937) / Rooted Tree Path Packing & Covering Archetype
- **Exact Constraints**: A rooted tree $T$ on $N \le 1000$ vertices (root $1$), where each tree edge $e_v = (\text{parent}(v), v)$ requires coverage $\ge a_v$ (or $\le u_v$), and $M \le 10000$ vertical paths $P_j = (u_j \rightsquigarrow v_j)$ ($u_j$ is an ancestor of $v_j$) with cost $c_j$ and capacity $cap_j$. Minimize total cost.
- **Step 1: Non-Graph Diagnostic Signal**:
  Variables $x_j$ correspond to **vertical paths** $u_j \rightsquigarrow v_j$ on a rooted tree $T$, and constraints correspond to tree edges $e_v$. By Theorem 5.4, the constraint matrix is a **Tutte Network Matrix $M(T, G)$**, generalizing 1D intervals (`P02`) to trees!
- **Step 2: Intermediate Algebraic Representation**:
  For each non-root vertex $v \in V \setminus \{1\}$, write the coverage equation on tree edge $e_v = (\text{parent}(v), v)$ with surplus slack $y_v \ge 0$:

  $$
  E_v : \quad \sum_{j : e_v \in P_j} x_j - y_v = a_v \quad (v \in V \setminus \{1\}), \qquad E_1 : 0 = 0.
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  Apply the **Tree Difference Transformation $D_T$** (Section 5.4): for every vertex $u \in V$, replace $E_u$ with

  $$
  E'_u \stackrel{\text{def}}{=} E_u - \sum_{w \in \text{child}(u)} E_w = a_u - \sum_{w \in \text{child}(u)} a_w.
  $$

  1. Consider a vertical path $P_j = (u_j \text{ down to } v_j)$: it uses tree edges $e_w$ for all $w \in P_j \setminus \{u_j\}$.
     - At $u = u_j$: $e_{u_j} \notin P_j$, while the unique child $w \in \text{child}(u_j) \cap P_j$ has $e_w \in P_j$, giving coefficient **$-1$** at $u_j$!
     - At any internal vertex $x \in P_j \setminus \{u_j, v_j\}$: $e_x \in P_j$ ($+1$) and its unique child on $P_j$ has $e_w \in P_j$ ($-1$), cancelling to **$0$**!
     - At the bottom endpoint $v_j$: $e_{v_j} \in P_j$ ($+1$) and no child of $v_j$ is on $P_j$, giving coefficient **$+1$** at $v_j$!
     Thus $x_j$ compiles to a single directed edge **$u_j \to v_j$** (or $v_j \to u_j$ depending on sign convention) with capacity $cap_j$ and cost $c_j$!
  2. Slack variable $y_v \ge 0$ appears only in $E'_v$ ($-y_v$) and $E'_{\text{parent}(v)}$ ($+y_v$), compiling to a tree backbone edge **$v \to \text{parent}(v)$** with capacity $\infty$ and cost $0$!
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|V| = N + 2$, $|E| = M + 2N$; MCMF solves in $O(F \cdot M \log N)$.
  - **Broken Gadget Warning**: As proved in Section 5.5 ($K_{1,3}$ Star Counterexample), this compilation **only** works when paths are vertical ($u_j$ is an ancestor of $v_j$). If a path $u \text{--} \text{LCA}(u, v) \text{--} v$ bends at $\text{LCA}(u, v)$ and contributes $+1$ to both branches, at $u = \text{LCA}(u, v)$ two children are subtracted, giving coefficient $-2$ and destroying flow conservation!
- **3-Tier Progressive Hints**:
  - *Hint 1*: On a line graph (`志愿者招募`), each vertex $u$ has $1$ child, so we subtracted $E_u - E_{\text{child}(u)}$. What is the natural generalization when $u$ has multiple children in a rooted tree?
  - *Hint 2*: Define $E'_u = E_u - \sum_{w \in \text{child}(u)} E_w$. Since a vertical path $u_j \rightsquigarrow v_j$ enters at most $1$ child of any vertex $u$, all internal vertices cancel!
  - *Hint 3*: Each vertical path $u_j \rightsquigarrow v_j$ becomes a single directed edge between $u_j$ and $v_j$, and each slack $y_v$ becomes a tree edge between $v$ and $\text{parent}(v)$.

---

#### P16 — `Codeforces 1307G — Cow and Exercise` (Shortest-Path Extension LP Dual & $O(Q \log F)$ Residual Slope Envelope)
- **Judge Coordinates**: [Codeforces 1307G](https://codeforces.com/problemset/problem/1307/G)
- **Exact Constraints**: Directed graph with $N \le 50$ vertices, $M \le N(N-1)$ edges with weights $w_e \ge 1$, and $Q \le 10^5$ independent queries. Query $q$ gives budget $x_q \in [0, 10^5]$; we can increase edge weights $w_e \gets w_e + \delta_e$ ($\delta_e \ge 0$, $\sum_{e \in E} \delta_e \le x_q$) to maximize the shortest path from $1$ to $N$.
- **Step 1: Non-Graph Diagnostic Signal**:
  Maximizing the shortest path by increasing edge weights under an $L_1$ budget $\sum \delta_e \le x_q$ is the **Parametric Inverse Shortest Path** problem (Sections 3.2 and 4.3).
- **Step 2: Intermediate Algebraic Representation**:
  For a fixed query budget $x_q$:

  $$
  \begin{aligned}
  \text{Primal: } \quad & \max_{D, \boldsymbol{\pi}, \boldsymbol{\delta}} \; D \quad \text{s.t.} \quad \pi_N - \pi_1 \ge D, \quad \pi_u - \pi_v + \delta_{uv} \ge -w_{uv} \;\; (\forall (u, v) \in E), \quad \sum_{e \in E} \delta_e \le x_q, \quad \delta_e \ge 0.
  \end{aligned}
  $$

  Assigning dual flow $f_e \ge 0$ to each edge inequality, return flow $F = 1$ to $\pi_N - \pi_1 \ge D$, and multiplier $\mu \ge 0$ to $\sum \delta_e \le x_q$ gives $0 \le f_e \le \mu$. Rescaling $\tilde{f}_e = f_e / \mu \in [0, 1]$ and setting $k = 1/\mu = \text{val}(\tilde{\mathbf{f}}) > 0$ yields the exactDual envelope:

  $$
  D^*(x_q) = \min_{k \in \{1, 2, \dots, F_{\max}\}} \frac{\text{MinCost}(k) + x_q}{k},
  $$

  where $\text{MinCost}(k)$ is the minimum cost to send $k$ units of flow from $1$ to $N$ when every original edge $e = (u, v)$ has **capacity $1$** and **cost $w_e$**!
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. Build the MCMF network where each input edge $e = (u, v)$ has **capacity $1$** and **cost $w_e$**.
  2. Run Successive Shortest Path (SSP) MCMF from $1$ to $N$. After each unit augmentation $k = 1, 2, \dots, F_{\max}$ (where $F_{\max} \le N - 1 \le 49$), record the cumulative flow $k$ and cumulative cost $C_k = \text{MinCost}(k)$.
  3. Answer each query $x_q$ in $O(\log F_{\max})$ (via binary search on the lower envelope of lines $L_k(x) = \frac{1}{k} x + \frac{C_k}{k}$) or $O(F_{\max})$ time!
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: Precomputation is $F_{\max} \le 49$ Bellman–Ford/Dijkstra runs $= O(N \cdot M \log N) \approx 2 \times 10^5$ ops; answering $Q = 10^5$ queries takes $O(Q \log N)$!
  - **Broken Gadget Warning**: Why can we restrict $k$ to **integers** $k \in \{1, 2, \dots, F_{\max}\}$ even though the LP allows continuous $k > 0$? Because $\text{MinCost}(k)$ is piecewise-linear on unit intervals $[k-1, k]$, so for any fractional $k \in (k_0, k_0+1)$, the ratio $(\text{MinCost}(k) + x_q)/k$ is monotonic on $[k_0, k_0+1]$ and attains its minimum at one of the integer endpoints $k_0$ or $k_0 + 1$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Write the shortest-path condition using node potentials $\pi_v - \pi_u \le w_{uv} + \delta_{uv}$ and take the LP Dual.
  - *Hint 2*: In the Dual, each edge has capacity $1$ (from the coefficient $1$ of $\delta_e$ in $\sum \delta_e \le x_q$) and cost $w_e$.
  - *Hint 3*: Precompute the minimum cost $C_k$ to send $k = 1, 2, \dots, F_{\max}$ units of flow from $1$ to $N$; then the answer for budget $x_q$ is $\min_{k \ge 1} (C_k + x_q)/k$.

---

### Tier 3: Advanced (`P17` – `P24`)

---

#### P17 — `[NOI2010] 海拔` (Continuous Altitudes $h_v \in [0, 1]$ via Lovász Coarea Theorem & Planar Dual Shortest Path)
- **Judge Coordinates**: [Luogu P2046](https://www.luogu.com.cn/problem/P2046) | [LOJ 2251](https://loj.ac/p/2251)
- **Exact Constraints**: $(N+1) \times (N+1)$ directed grid ($N \le 500$, $|V| \le 2.5 \times 10^5$, $|E| \le 10^6$). Top-left corner $(0, 0)$ has altitude $h_{0,0} = 0$, bottom-right $(N, N)$ has $h_{N,N} = 1$. Each directed grid edge $e = (u, v)$ has traffic $w_{uv} \ge 0$, and climbing uphill from $u$ to $v$ ($h_v > h_u$) consumes $w_{uv} \cdot (h_v - h_u)$ energy (walking downhill or flat $h_v \le h_u$ consumes $0$). Choose real altitudes $h_v \in [0, 1]$ to minimize total energy.
- **Step 1: Non-Graph Diagnostic Signal**:
  The objective $\sum_{(u,v) \in E} w_{uv} \max(0, h_v - h_u)$ is the **Lovász extension** $\hat{f}(\mathbf{1} - \mathbf{h})$ of the directed $s$-$t$ cut capacity function $f(S)$! Even though $h_v \in \mathbb{R}$ can be arbitrary real numbers, by Theorem 6.2 (Lovász Coarea Theorem), the minimum over $[0, 1]^V$ equals the minimum over binary indicator vectors $\{0, 1\}^V$!
- **Step 2: Intermediate Algebraic Representation**:
  Substitute $\mathbf{x} = \mathbf{1} - \mathbf{h} \in [0, 1]^V$ (so $x_{0,0} = 1$, $x_{N,N} = 0$, and $\max(0, h_v - h_u) = \max(0, x_u - x_v)$). By the Coarea Identity (Section 6.3):

  $$
  \min_{\mathbf{x} \in [0, 1]^V : x_s = 1, x_t = 0} \sum_{(u,v) \in E} w_{uv} \max(0, x_u - x_v) = \min_{\mathbf{x}} \int_0^1 \Bigg( \sum_{(u,v) \in E} w_{uv} \big[ x_u \ge \lambda > x_v \big] \Bigg) d\lambda = \text{MinCut}(s, t).
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. The problem reduces to a directed $s$-$t$ Minimum Cut on an $(N+1) \times (N+1)$ **planar grid** with $|V| = 2.5 \times 10^5$.
  2. Since Dinic on $2.5 \times 10^5$ vertices can be tight, exploit **Planar Graph Duality** ($s$-$t$ Min-Cut $=$ $S^* \to T^*$ Shortest Path in the planar dual):
     - Add an imaginary return edge $(N, N) \to (0, 0)$ splitting the outer face into the **Bottom-Left Outer Face $S^*$** and the **Top-Right Outer Face $T^*$**.
     - Each inner $1 \times 1$ grid square $(i, j)$ ($1 \le i, j \le N$) is a dual vertex.
     - Each directed primal edge $u \to v$ (with capacity $w_{uv}$) induces a **directed dual edge** of weight $w_{uv}$ crossing $u \to v$ from left to right (clockwise rotation by $90^\circ$).
  3. Run **Dijkstra** from $S^*$ to $T^*$ in $O(N^2 \log N)$ time!
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|V_{\text{dual}}| = N^2 + 2 \le 2.5 \times 10^5$, $|E_{\text{dual}}| = 4N(N+1) \le 10^6$; Dijkstra runs in $0.15\text{ s}$.
  - **Broken Gadget Warning**: Because traffic is **asymmetric** ($w_{u \to v} \neq w_{v \to u}$), the dual graph is **directed**! Ensure every primal edge $u \to v$ (where $u \in S_{\text{alt}=0}, v \in T_{\text{alt}=1}$) maps to the correct directed dual orientation separating $S^*$ from $T^*$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Do optimal altitudes ever need to take fractional values like $0.3$ or $0.7$, or can every vertex be set to $0$ or $1$?
  - *Hint 2*: By the Coarea formula $\max(0, h_v - h_u) = \int_0^1 [h_v \ge \lambda > h_u] d\lambda$, an optimal solution exists with $h_v \in \{0, 1\}$, reducing the problem to a directed $s$-$t$ Min-Cut.
  - *Hint 3*: Since $(0,0)$ and $(N,N)$ lie on the outer boundary of a planar grid, convert the directed $s$-$t$ Min-Cut into a directed shortest path in the planar dual and run Dijkstra!

---

#### P18 — `AtCoder ARC 107 F — Sum of Abs` (3-State Sign Cut $\{-1, 0, +1\}$ via 2-Bit Submodular Chain)
- **Judge Coordinates**: [AtCoder ARC107F](https://atcoder.jp/contests/arc107/tasks/arc107_f)
- **Exact Constraints**: Undirected graph with $N \le 300$ vertices, $M \le 300$ edges, deletion costs $A_i \in [-10^6, 10^6]$ (actually $A_i$ can be any integer; deleting $i$ leaves it out of the score, keeping it puts it into a connected component $C$), and vertex values $B_i \in [-10^6, 10^6]$. Maximize $\sum_{\text{comp } C} \big| \sum_{i \in C} B_i \big| - \sum_{i \text{ deleted}} A_i$ (or equivalently, kept vertices in $C$ contribute $|\sum_{i \in C} B_i|$ and all vertices have base/deletion costs).
- **Step 1: Non-Graph Diagnostic Signal**:
  The absolute value $|\sum_{i \in C} B_i| = \max_{s_C \in \{-1, +1\}} \sum_{i \in C} s_C B_i$ allows us to assign each vertex $i$ a **3-state label** $\sigma_i \in \{-1, 0, +1\}$ (where $\sigma_i = 0$ means vertex $i$ is deleted, and $\sigma_i \in \{-1, +1\}$ means vertex $i$ is kept with sign $\sigma_i$). Two adjacent vertices $(u, v) \in E$ **cannot** have opposite signs $(\sigma_u = +1, \sigma_v = -1)$ without at least one of them being deleted ($\sigma = 0$)!
- **Step 2: Intermediate Algebraic Representation**:
  Encode the 3 ordered states $\sigma_i \in \{-1, 0, +1\}$ using a **2-bit unary threshold chain** $(x_{i,1}, x_{i,2}) \in \{(0, 0), (1, 0), (1, 1)\}$ with $x_{i,1} \ge x_{i,2}$:
  - State $-1 \leftrightarrow (0, 0)$ ($i_{\text{in}} \in T, i_{\text{out}} \in T$);
  - State $0 \text{ (deleted)} \leftrightarrow (1, 0)$ ($i_{\text{in}} \in S, i_{\text{out}} \in T$);
  - State $+1 \leftrightarrow (1, 1)$ ($i_{\text{in}} \in S, i_{\text{out}} \in S$).
  Then for any edge $(u, v) \in E$, forbidding $(\sigma_u, \sigma_v) \in \{(-1, +1), (+1, -1)\}$ is equivalent to forbidding $(x_{u,2} = 1 \land x_{v,1} = 0)$ and $(x_{v,2} = 1 \land x_{u,1} = 0)$!
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. For each vertex $i$, create two nodes $i_1$ ($i_{\text{in}}$) and $i_2$ ($i_{\text{out}}$) representing the chain $S \xrightarrow{w(i, -1)} i_1 \xrightarrow{w(i, 0)} i_2 \xrightarrow{w(i, +1)} T$:
     - Add reverse ordering edge $i_2 \to i_1$ with **capacity $\infty$** (enforcing $x_{i,1} \ge x_{i,2}$, so $(0, 1)$ is impossible).
     - Set the 3 cut capacities on $S \to i_1$, $i_1 \to i_2$, $i_2 \to T$ to match the penalties $\text{MaxGain}_i - \text{Gain}_i(\sigma_i)$ for $\sigma_i \in \{-1, 0, +1\}$ (specifically, shifting by $M_i = |B_i| + \max(0, -A_i)$ makes all three cut capacities non-negative!).
  2. For each original edge $(u, v) \in E$: add directed edges **$u_2 \to v_1$ (cap $\infty$)** and **$v_2 \to u_1$ (cap $\infty$)** (forbidding $u$ in state $+1$ while $v$ is in state $-1$, and vice versa!).
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|V| = 2N + 2 \le 602$, $|E| = 3N + 2M \le 1500$; Dinic runs in $< 5\text{ ms}$.
  - **Broken Gadget Warning**: Omitting the reverse $\infty$-edge $i_2 \to i_1$ allows the phantom 4th state $(x_{i,1}, x_{i,2}) = (0, 1)$, which bypasses the middle deletion cost $i_1 \to i_2$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Rewrite $|\sum_{i \in C} B_i|$ by choosing a sign $\sigma_C \in \{-1, +1\}$ for each connected component $C$.
  - *Hint 2*: Every vertex $i$ now chooses from 3 states $\sigma_i \in \{-1, 0, +1\}$ such that no edge $(u, v)$ connects $-1$ directly to $+1$.
  - *Hint 3*: Represent the 3 ordered states $-1 < 0 < +1$ by a 2-node cut chain $S \to i_1 \to i_2 \to T$ (with $i_2 \to i_1$ cap $\infty$) and add $\infty$-edges $u_2 \to v_1$ and $v_2 \to u_1$.

---

#### P19 — `AtCoder AGC 038 F — Two Permutations` (Cycle Decomposition & Rescuing Supermodularity via Bipartite Flip)
- **Judge Coordinates**: [AtCoder AGC038F](https://atcoder.jp/contests/agc038/tasks/agc038_f)
- **Exact Constraints**: Two permutations $P, Q$ of $\{0, \dots, N-1\}$ ($N \le 10^5$). We must construct permutations $A, B$ such that at each $i$, either $A_i = i$ or $A_i = P_i$, and either $B_i = i$ or $B_i = Q_i$. Maximize the number of indices $i$ where $A_i \neq B_i$ (equivalently, minimize $\#\{i : A_i = B_i\}$).
- **Step 1: Non-Graph Diagnostic Signal**:
  Consider the cycle decomposition of $P$: for $A$ to be a valid permutation (bijection) when $A_i \in \{i, P_i\}$, every cycle $C$ of $P$ must either **stay completely fixed** ($A_i = i \;\forall i \in C$, state $x_C = 0$) or **rotate completely** ($A_i = P_i \;\forall i \in C$, state $x_C = 1$)! Similarly, every cycle $D$ of $Q$ has a single binary variable $y_D \in \{0, 1\}$.
- **Step 2: Intermediate Algebraic Representation**:
  Each index $i \in \{0, \dots, N-1\}$ belongs to **one $P$-cycle $C(i)$** and **one $Q$-cycle $D(i)$**, so the interaction graph between $X = \{x_C\}$ and $Y = \{y_D\}$ is **Bipartite**! We want to minimize $\sum_{i=0}^{N-1} [A_i = B_i]$.
  Wait: at an index $i$ where $P_i = Q_i \neq i$, we get a collision $A_i = B_i$ both when $(x_C, y_D) = (0, 0)$ ($A_i = B_i = i$) AND when $(x_C, y_D) = (1, 1)$ ($A_i = B_i = P_i = Q_i$)! The cost table on $(x_C, y_D)$ is $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, which has $A + D = 2 > 0 = B + C$ (**Supermodular**, violating $A + D \le B + C$!).
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  Because the interaction is **Bipartite** between $P$-cycles $C$ and $Q$-cycles $D$, apply **Bipartite Variable Inversion**: replace $y_D$ with $\bar{y}_D = 1 - y_D$!
  Now for every index $i$ with $C = C(i)$ and $D = D(i)$, check the 5 cases of $(P_i, Q_i)$ under $(x_C, \bar{y}_D) \in \{0, 1\}^2$:
  1. $P_i = i \land Q_i = i$: always $A_i = B_i = i$ (constant $+1$).
  2. $P_i = i \land Q_i \neq i$: $A_i = B_i \iff y_D = 0 \iff \bar{y}_D = 1$ (edge $D \to T$, cap $1$).
  3. $P_i \neq i \land Q_i = i$: $A_i = B_i \iff x_C = 0$ (edge $S \to C$, cap $1$).
  4. $P_i \neq i \land Q_i \neq i \land P_i \neq Q_i$: $A_i = B_i \iff (x_C = 0 \land y_D = 0) \iff (x_C = 0 \land \bar{y}_D = 1)$ (directed edge $D \to C$, cap $1$).
  5. $P_i = Q_i \neq i$: $A_i = B_i \iff x_C = y_D \iff x_C \neq \bar{y}_D$ (**both** directed edges $C \to D$ and $D \to C$, cap $1$!).
  Every single term is now submodular ($A + D \le B + C$)! Answer $= N - \text{Constant} - \text{MinCut}(S, T)$.
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: Unit-capacity network with $|V|, |E| \le 2N + 2 \le 2 \times 10^5$; Dinic runs in $O(E \sqrt{V})$ ($< 0.15\text{ s}$).
  - **Broken Gadget Warning**: Without flipping $\bar{y}_D = 1 - y_D$, Case 4 ($x_C = 0 \land y_D = 0$) and Case 5 ($x_C = y_D$) are supermodular and impossible to represent as an $s$-$t$ cut!
- **3-Tier Progressive Hints**:
  - *Hint 1*: If $A_i \in \{i, P_i\}$ must form a permutation, what are the allowed choices on each cycle of $P$?
  - *Hint 2*: Each cycle $C$ of $P$ has a single binary choice $x_C \in \{0, 1\}$, and each cycle $D$ of $Q$ has a binary choice $y_D \in \{0, 1\}$.
  - *Hint 3*: Flip $\bar{y}_D = 1 - y_D$ on the $Q$-cycles so that same-state penalties $(0,0)$ and $(1,1)$ become cut penalties $(0,1)$ and $(1,0)$!

---

#### P20 — `[CTSC / Cow Loops / PERT Crashing Archetype]` (Critical Path & Cycle Compression with Piecewise Linear Costs)
- **Judge Coordinates**: `Cow Loops` / Project Crashing with Convex Piecewise-Linear Cost Curves (Section 3.4 Archetype)
- **Exact Constraints**: Directed graph $G = (V, E)$ ($N \le 300, M \le 2000$). Each edge $e = (u, v)$ has baseline weight $d_e$ and $K_e \ge 1$ compression stages: stage $k$ reduces the weight by up to $m_{e,k}$ at unit cost $c_{e,k}$ ($0 < c_{e,1} < c_{e,2} < \dots$). Find the minimum total cost to ensure: (a) the longest $s$-$t$ path is $\le T_{\max}$ (DAG PERT Crashing), or (b) all directed cycles have weight $\le 0$ (`Cow Loops`), and output the optimal node timestamps $t_v^*$.
- **Step 1: Non-Graph Diagnostic Signal**:
  We are choosing node potentials $t_v \in \mathbb{R}$ and edge compressions $\gamma_{e,k} \in [0, m_{e,k}]$ satisfying difference constraints $t_v - t_u + \sum_k \gamma_{e,k} \ge d_e$. By Theorem 2.1 and Section 3.4, the LP Dual is a pure Minimum-Cost Circulation!
- **Step 2: Intermediate Algebraic Representation**:

  $$
  \min_{\mathbf{t}, \boldsymbol{\gamma}} \sum_{e \in E} \sum_{k=1}^{K_e} c_{e,k} \gamma_{e,k} \quad \text{s.t.} \quad t_v - t_u + \sum_{k=1}^{K_e} \gamma_{e,k} \ge d_e \;\; (\forall e = (u,v) \in E), \quad 0 \le \gamma_{e,k} \le m_{e,k}.
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  By Section 3.4, let $c_{e,0} = 0$ and $c_{e, K_e+1} = \infty$. In the Dual Circulation network, each edge $e = (u, v)$ compiles into **$K_e + 1$ parallel directed edges** from $u$ to $v$:
  - For $k = 1, \dots, K_e + 1$: parallel edge $e^{(k)}: u \to v$ with **capacity $c_{e,k} - c_{e,k-1}$** and **min-cost $-\big(d_e - \sum_{j=1}^{k-1} m_{e,j}\big)$**.
  - For Makespan $\le T_{\max}$: add return edge $t \to s$ with capacity $\infty$ and cost $+T_{\max}$.
  - Find the **Minimum-Cost Circulation** (eliminate all negative cycles), and recover optimal timestamps $t_v^* = -\text{dist}[v] + \text{dist}[s]$ via the Virtual Super-Root $Q$ SPFA Contract (Section 4.2)!
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: Min-cost circulation on $N \le 300$ vertices; runs in $< 0.2\text{ s}$.
  - **Broken Gadget Warning**: If an edge has a hard minimum duration (cannot be compressed beyond $\sum m_{e,k}$), the $(K_e+1)$-th parallel edge **must** have capacity $\infty$ and cost $-(d_e - \sum_{j=1}^{K_e} m_{e,j})$; if its cost creates a negative cycle of capacity $\infty$, the problem is Primal Infeasible!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Write the precedence constraints $t_v - t_u \ge d_e - \sum \gamma_{e,k}$ with $0 \le \gamma_{e,k} \le m_{e,k}$ and take the LP Dual.
  - *Hint 2*: Notice how $f_e - z_{e,k} \le c_{e,k}$ splits the flow $f_e$ on edge $e$ into $K_e + 1$ capacity brackets $[c_{e,k-1}, c_{e,k}]$ of progressively smaller reward.
  - *Hint 3*: Recover the optimal timestamps $t_v^*$ by running 1 pass of SPFA from a virtual super-root $Q$ on the final residual graph $G_{\mathbf{f}^*}$.

---

#### P21 — `[ICPC / UVa 1406 / Cyclic Volunteer Recruitment]` (Circular-Ones Rescued via Parametric Flow $K$ & Ternary Search)
- **Judge Coordinates**: Cyclic Interval Covering / 24-Hour Shift Scheduling (`UVa 1406` / Cyclic `[NOI2008] 志愿者招募` Variant)
- **Exact Constraints**: $N \le 500$ cyclic time slots $1, \dots, N$ (where slot $N$ wraps around to slot $1$), $M \le 2000$ shift types. Non-wrapping shifts cover $[l_j, r_j]$ ($l_j \le r_j$); wrapping shifts $j \in W$ cover $[l_j, N] \cup [1, r_j]$ ($l_j > r_j$) at cost $c_j$ and capacity $u_j$. Slot $t$ requires at least $a_t$ workers. Minimize total cost.
- **Step 1: Non-Graph Diagnostic Signal**:
  Because wrapping shifts have two blocks of $1$s ($[1, r_j]$ and $[l_j, N]$), the constraint matrix is **Circular-Ones** (`循环连续1`), which is **not** Totally Unimodular (Section 5.3). However, if we fix the **total number of wrapping workers crossing midnight** $K = \sum_{j \in W} x_j$, every wrapping shift can be complemented against the full cycle!
- **Step 2: Intermediate Algebraic Representation**:
  By Theorem 5.3, for a fixed integer $K = \sum_{j \in W} x_j$, replace $\mathbf{1}_{[l_j, N] \cup [1, r_j]} = \mathbf{1}_{[1, N]} - \mathbf{1}_{[r_j+1, l_j-1]}$:

  $$
  E_t : \quad \sum_{j \in N_{\text{std}} : t \in [l_j, r_j]} x_j - \sum_{j \in W : t \in [r_j+1, l_j-1]} x_j - y_t = a_t - K \quad (1 \le t \le N), \qquad E_{N+1} : \sum_{j \in W} x_j = K.
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  Subtract $E'_t = E_t - E_{t-1}$ ($1 \le t \le N+1$, where $E_0 : 0 = 0$ and before subtraction we handle $\sum_{j \in W} x_j = K$ via a dedicated midnight node or directly observe that in $E_t - E_{t-1}$ with $E_{N+1}: 0 = 0$):
  1. Non-wrapping shift $j \in N_{\text{std}}$ ($[l_j, r_j]$): directed edge **$l_j \to r_j + 1$** (cap $u_j$, cost $c_j$).
  2. Wrapping shift $j \in W$ ($-\mathbf{1}_{[r_j+1, l_j-1]}$ has $-1$ at $r_j+1$ and $+1$ at $l_j$!): directed backward edge **$l_j \to r_j + 1$** (cap $u_j$, cost $c_j$).
  3. Slack $y_t \ge 0$: directed edge **$(t + 1) \to t$** (cap $\infty$, cost $0$).
  4. The RHS supplies $b_t = (a_t - K) - (a_{t-1} - K) = a_t - a_{t-1}$ are **independent of $K$** for $2 \le t \le N$, while $b_1 = a_1 - K$ and $b_{N+1} = -(a_N - K) = K - a_N$! (To enforce $\sum_{j \in W} x_j = K$, route wrapping edges $j \in W$ through a split midnight bridge of exact flow $K$, or note that shifting $b_1 \gets a_1 - K$ and $b_{N+1} \gets K - a_N$ fixes the net wrap-around flow to $K$!)
  5. Since the minimum cost $\Phi(K)$ is a **convex function** of $K \in [0, \sum_{j \in W} u_j]$, find $\min_K \Phi(K)$ via **ternary search** in $O(\log(\max K))$ MCMF runs!
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $O(\log(\sum u_j)) \le 30$ MCMF runs on $N + 2$ vertices.
  - **Broken Gadget Warning**: Wait—why doesn't integer LP relaxation without fixing $K$ work? Because for $N=3$ with shifts $[1,2], [2,3], [3,1]$ and demands $a = (1, 1, 1)$, the fractional LP uses $K = 1.5$ ($x_1 = x_2 = x_3 = 0.5$), whereas fixing $K \in \mathbb{Z}$ forces an integral flow!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Why does subtracting $E_t - E_{t-1}$ fail when an interval wraps around from $N$ to $1$? Because it creates $+1$ and $-1$ at four endpoints instead of two!
  - *Hint 2*: Suppose you guess the total number of wrapping shifts $K = \sum_{j \in W} x_j$. Then $\mathbf{1}_{\text{wrap}} = \mathbf{1}_{[1,N]} - \mathbf{1}_{[r_j+1, l_j-1]}$ turns every wrapping shift into a single contiguous negative interval!
  - *Hint 3*: By LP convexity, the optimal cost $\Phi(K)$ is convex in $K$, so ternary search over integer $K$.

---

#### P22 — `[QOJ / CF 1067E Dual] Two-Tree Subtree Laminar Selection` (Two Laminar Matroids via Hasse Out-Tree + In-Tree)
- **Judge Coordinates**: Two-Tree Subtree Bounded Selection Archetype (cf. AtCoder AGC 031E / ICPC Regional Two-Tree Problems)
- **Exact Constraints**: Ground set $V = \{1, \dots, N\}$ ($N \le 500$) with item weights $w_v$. We are given **two rooted trees** $T_1$ and $T_2$ on the same vertex set $V$. In $T_1$, the subtree of $u$ must have between $L_{1,u}$ and $R_{1,u}$ chosen items; in $T_2$, the subtree of $v$ must have between $L_{2,v}$ and $R_{2,v}$ chosen items. Maximize $\sum_{v \in S} w_v$.
- **Step 1: Non-Graph Diagnostic Signal**:
  The family of subtrees $\mathcal{L}_1 = \{\text{Sub}_{T_1}(u)\}_{u \in V}$ is a **Laminar Family** ($A, B \in \mathcal{L}_1 \implies A \cap B = \emptyset$ or $A \subseteq B$ or $B \subseteq A$), and $\mathcal{L}_2 = \{\text{Sub}_{T_2}(v)\}_{v \in V}$ is a second **Laminar Family**. By Section 6.4, the intersection of **two Laminar Matroids / Polymatroids** compiles into an exact Hasse Out-Tree + In-Tree flow network!
- **Step 2: Intermediate Algebraic Representation**:
  For each $u \in V$, the total flow entering $u$'s subtree node in $T_1$ equals the sum of item variables $x_w \in \{0, 1\}$ in $\text{Sub}_{T_1}(u)$:

  $$
  f(\text{pa}_{T_1}(u) \to u) = x_u + \sum_{c \in \text{child}_{T_1}(u)} f(u \to c) = \sum_{w \in \text{Sub}_{T_1}(u)} x_w \in [L_{1,u}, R_{1,u}].
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. **Left Hasse Out-Tree ($T_1$)**: Create nodes $u^{(1)}$ for $u \in V$. Add edge $S \to \text{root}(T_1)^{(1)}$ with capacity $[L_{1,r}, R_{1,r}]$, cost $0$. For each tree edge $(p, u) \in T_1$, add directed edge $p^{(1)} \to u^{(1)}$ with lower/upper capacity $[L_{1,u}, R_{1,u}]$ and cost $0$.
  2. **Middle Item Bridges**: For each item $v \in V$, add directed edge $v^{(1)} \to v^{(2)}$ with capacity $[0, 1]$ and min-cost $-w_v$.
  3. **Right Hasse In-Tree ($T_2$)**: Create nodes $v^{(2)}$ for $v \in V$. For each tree edge $(p, v) \in T_2$, add directed edge **$v^{(2)} \to p^{(2)}$** (oriented toward the root!) with lower/upper capacity $[L_{2,v}, R_{2,v}]$ and cost $0$, and $\text{root}(T_2)^{(2)} \to T$ with capacity $[L_{2,r}, R_{2,r}]$, cost $0$.
  4. Solve Minimum-Cost Feasible Circulation with Lower Bounds (`上下界最小费用可行流`).
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|V| = 2N + 4 \le 1004$, $|E| = 3N + 1 \le 1501$; lower-bound MCMF runs in $< 30\text{ ms}$.
  - **Broken Gadget Warning**: If there were a **third** tree $T_3$, intersecting 3 laminar families generalizes 3-Dimensional Matching and is **NP-hard**!
- **3-Tier Progressive Hints**:
  - *Hint 1*: How can a single edge capacity in $T_1$ bound the sum of all $x_w$ inside the entire subtree $\text{Sub}_{T_1}(u)$?
  - *Hint 2*: Route flow down the tree $T_1$ from root to leaves, let each vertex $v$ bleed off at most $1$ unit of flow ($x_v \in \{0, 1\}$), and collect those bled flows up the second tree $T_2$ from leaves to root!
  - *Hint 3*: Put lower/upper bounds $[L_{1,u}, R_{1,u}]$ on the tree edges of $T_1$ and $[L_{2,v}, R_{2,v}]$ on the reversed tree edges of $T_2$.

---

#### P23 — `AtCoder ABC 214 H — Collecting` (SCC Condensation, Node-Splitting Potential LP Dual & Topological Johnson Potentials)
- **Judge Coordinates**: [AtCoder ABC214H](https://atcoder.jp/contests/abc214/tasks/abc214_h)
- **Exact Constraints**: Directed graph with $N \le 2 \times 10^5$ vertices, $M \le 2 \times 10^5$ edges, $K \le 10$ tokens starting at vertex $1$, and vertex values $A_v \ge 1$. Each token walks along a directed path; if at least one token visits $v$, we collect $A_v$ once. Maximize total value collected.
- **Step 1: Non-Graph Diagnostic Signal**:
  Within any Strongly Connected Component (SCC), a token can visit every vertex in the SCC before leaving, so we first contract SCCs into a **DAG** where each SCC $C$ has weight $W_C = \sum_{v \in C} A_v$. Then we want $K$ paths starting at $C(1)$ to maximize the weight of their union—a classic node-splitting MCMF problem, except $N, M \le 2 \times 10^5$ is too large for naive SPFA!
- **Step 2: Intermediate Algebraic Representation**:
  Split each SCC $C$ into $C_{\text{in}} \to C_{\text{out}}$ with reward $W_C$ for the first unit of flow ($f_C^{(1)} \in [0, 1]$) and $0$ for subsequent units ($f_C^{(2)} \in [0, \infty)$). Because the graph is a **DAG** with costs $-W_C \le 0$ on $C_{\text{in}} \to C_{\text{out}}$, the initial dual potentials $\pi(v)$ (shortest path from source $C(1)_{\text{in}}$) can be computed in $O(V + E)$ via **Topological DP**:

  $$
  \pi(u) = \min_{p \to u} \big( \pi(p) + \text{cost}(p \to u) \big).
  $$

- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. Run Tarjan's SCC algorithm; keep only SCCs reachable from vertex $1$.
  2. For each reachable SCC $C$: create $C_{\text{in}}$ and $C_{\text{out}}$ with two parallel edges $C_{\text{in}} \to C_{\text{out}}$: (a) cap $1$, cost $-W_C$, and (b) cap $K$, cost $0$. Add $C_{\text{out}} \to T_{\text{snk}}$ (cap $K$, cost $0$).
  3. For each DAG edge $C_1 \to C_2$: add $C_{1,\text{out}} \to C_{2,\text{in}}$ (cap $K$, cost $0$).
  4. Compute initial potentials $\pi(\cdot)$ in **topological order** in $O(N + M)$ time so that every reduced cost $c_\pi(u, v) = c(u, v) + \pi(u) - \pi(v) \ge 0$.
  5. Run $K \le 10$ iterations of **Primal–Dual Dijkstra** in $O(K (N + M) \log N)$ time!
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $O(N + M + K(N + M) \log N) \approx 4 \times 10^6$ ops ($< 0.3\text{ s}$).
  - **Broken Gadget Warning**: Do NOT use standard `unsigned` or unshifted costs without Johnson potentials: subtracting a constant from each edge does **not** work here because paths in the DAG have different lengths (numbers of edges)! Topological DP potentials $\pi(v)$ are exact and $O(N + M)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: First contract Strongly Connected Components (SCCs) into a DAG.
  - *Hint 2*: Split each SCC node into `in` and `out` connected by a `(cap=1, cost=-W_C)` edge and a `(cap=K, cost=0)` edge.
  - *Hint 3*: Since $N, M \le 2 \times 10^5$, avoid SPFA by computing initial Johnson potentials $\pi(v)$ via $O(N+M)$ DP along the topological order of the DAG, then run $K \le 10$ Dijkstras!

---

#### P24 — `[WC2006] 水管局长` / `[HNOI2010] 城市建设` (Offline / Dynamic Parametric MST via Matroid Contraction–Reduction)
- **Judge Coordinates**: [Luogu P4174 / P4180](https://www.luogu.com.cn/problem/P3206) (`[HNOI2010] 城市建设` Luogu P3206)
- **Exact Constraints**: Undirected graph with $N \le 20000$ vertices, $M \le 50000$ edges, and $Q \le 50000$ dynamic edge weight updates $w_{e_q} \gets v_q$. After each update, output the weight of the Minimum Spanning Tree (MST).
- **Step 1: Non-Graph Diagnostic Signal**:
  Maintaining an MST under arbitrary dynamic edge weight updates (or solving dynamic parametric/inverse MST queries across time intervals $[L, R]$) cannot be done with static LCT alone if weights both increase and decrease, unless we use **Offline CDQ Divide-and-Conquer on the Graphic Matroid** (`Contraction–Reduction`)!
- **Step 2: Intermediate Algebraic Representation**:
  Consider a time interval $[L, R]$ of $k = R - L + 1$ updates, affecting a subset of dynamic edges $E_{\text{dyn}} \subseteq E$ ($|E_{\text{dyn}}| \le k$), while $E_{\text{stat}} = E \setminus E_{\text{dyn}}$ are static during $[L, R]$. By **Matroid Exchange Duality**:
  1. **Contraction (`必选边缩点`)**: Set all $e \in E_{\text{dyn}}$ to weight $-\infty$ and run Kruskal. Any static edge $e \in E_{\text{stat}}$ that **still** enters the MST will belong to the MST for *every* possible weight assignment to $E_{\text{dyn}}$! We can **permanently contract** its endpoints (adding its weight to `base_ans`) before recursing!
  2. **Reduction (`无用边删除`)**: Set all $e \in E_{\text{dyn}}$ to weight $+\infty$ and run Kruskal (on the contracted graph). Any static edge $e \in E_{\text{stat}}$ that **fails** to enter the MST will *never* belong to the MST for any weight assignment to $E_{\text{dyn}}$! We can **permanently delete** it before recursing!
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. After Contraction on interval $[L, R]$ with $|E_{\text{dyn}}| \le k$, the contracted graph has at most $k + 1$ vertices!
  2. After Reduction on that $(k + 1)$-vertex graph, at most $k$ static edges remain!
  3. Thus, when recursing to $[L, \text{mid}]$ and $[\text{mid}+1, R]$ (where $k \gets k/2$), the graph size $(|V|, |E|)$ shrinks to $O(k)$ at every node of the recursion tree!
  4. At a leaf $L = R$, apply update $L$ and run Kruskal on at most $2$ vertices and $2$ edges in $O(1)$ time!
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: At depth $d$ of the recursion tree, total vertices and edges across all $2^d$ subproblems is $O(Q)$, so sorting/DSU takes $O((M + Q) \log^2 Q)$ time ($< 0.4\text{ s}$)!
  - **Broken Gadget Warning**: You **must** run Contraction ($w_{\text{dyn}} = -\infty$) **before** passing the contracted vertex set to Reduction ($w_{\text{dyn}} = +\infty$); if you only run Reduction without Contraction, $|V|$ stays $N$ instead of shrinking to $\le k+1$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: In a recursion node $[L, R]$ with $k = R - L + 1$ updates, at most $k$ edges change weight; the other $|E| - k$ edges are completely static.
  - *Hint 2*: Which static edges are **guaranteed** to be in the MST even if all $k$ dynamic edges have weight $-\infty$? Contract them!
  - *Hint 3*: Which static edges **cannot** enter the MST even if all $k$ dynamic edges have weight $+\infty$? Delete them! Now $|V| \le k+1$ and $|E| \le 2k$.

---

### Tier 4: Mastery (`P25` – `P32`)

---

#### P25 — `Codeforces 1427G — One Billion Shades of Grey` (Lovász Coarea Level-Set Cuts & $O(N^3)$ Incremental Residual Rollback)
- **Judge Coordinates**: [Codeforces 1427G](https://codeforces.com/problemset/problem/1427/G)
- **Exact Constraints**: $N \times N$ grid ($N \le 200$). Boundary cells have fixed intensities $b_v \in [1, 10^9]$; internal cells are either blocked (`-1`) or free ($x_v \in \mathbb{R}$). Minimize $\sum_{(u,v) \in E} |x_u - x_v|$ over all adjacent non-blocked grid cells.
- **Step 1: Non-Graph Diagnostic Signal**:
  Total Variation $\sum_{(u,v) \in E} |x_u - x_v|$ is the **Lovász extension** of the undirected grid cut function! Let $v_1 < v_2 < \dots < v_K$ ($K \le 4N \le 800$) be the sorted distinct boundary values.
- **Step 2: Intermediate Algebraic Representation**:
  By Theorem 6.2 (Coarea Formula), for any real assignment $\mathbf{x}$:

  $$
  \sum_{(u,v) \in E} |x_u - x_v| = \sum_{k=1}^{K-1} (v_{k+1} - v_k) \sum_{(u,v) \in E} \Big| \big[x_u > v_k\big] - \big[x_v > v_k\big] \Big|.
  $$

  Because the binary threshold indicators $z_{u,k} = [x_u > v_k] \in \{0, 1\}$ decouple across each interval $(v_k, v_{k+1})$ and are nested by submodularity, the exact minimum is:

  $$
  \text{OPT} = \sum_{k=1}^{K-1} (v_{k+1} - v_k) \cdot \text{MinCut}(S_k, T_k),
  $$

  where at step $k$, boundary cells with $b_v \le v_k$ are connected to $S$ (cap $\infty$) and boundary cells with $b_v \ge v_{k+1}$ are connected to $T$ (cap $\infty$).
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  Running Dinic from scratch $K \le 800$ times on $N^2 = 40000$ vertices would TLE. Instead, notice how $(S_k, T_k)$ evolves from $k$ to $k+1$: only the boundary cells with $b_u = v_{k+1}$ **switch** from $T$ ($u \to T$ cap $\infty$) to $S$ ($S \to u$ cap $\infty$)!
  1. **Incremental Residual Rollback**: When boundary cell $u$ switches from $T$ to $S$:
     - If $u \to T$ currently carries $f \le 4$ units of flow (since $u$ has grid degree $\le 4$!), push $f$ units of flow **backward** along $u \to S$ (via BFS/DFS from $u$ to $S$ in the residual graph, at most $4$ paths!), delete $u \to T$, and decrement `current_flow -= f`.
     - Add edge $S \to u$ (cap $\infty$) and augment new $S \to T$ paths via DFS/BFS (`current_flow += new_pushed`).
  2. Across all $K$ steps, each boundary cell switches from $T$ to $S$ **once** (undoing at most $4$ units of flow), so the total number of augmenting paths across the **entire algorithm** is bounded by $4N + 4N = 8N \le 1600$!
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: At most $8N \le 1600$ unit-capacity BFS/DFS augmentations on $N^2 \le 40000$ vertices $\implies O(N^3) \approx 6.4 \times 10^7$ ops ($< 0.4\text{ s}$)!
  - **Broken Gadget Warning**: Grid edges between internal cells are **undirected** (capacity $1$ in **both** directions $u \to v$ and $v \to u$, i.e., `cap = 1` forward and `cap = 1` reverse in the residual graph).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Rewrite $|x_u - x_v| = \sum_{k=1}^{K-1} (v_{k+1} - v_k) |[x_u > v_k] - [x_v > v_k]|$ over the sorted boundary values $v_1 < \dots < v_K$.
  - *Hint 2*: For each $k$, minimizing $\sum |[x_u > v_k] - [x_v > v_k]|$ is a unit-capacity $S$-$T$ Min-Cut where boundary cells $\le v_k$ are in $S$ and $> v_k$ are in $T$.
  - *Hint 3*: Don't rebuild the network for each $k$! Roll back the $\le 4$ units of flow on $u \to T$ when $b_u = v_{k+1}$ moves from $T$ to $S$, and re-augment in $O(N^3)$ total time.

---

#### P26 — `Codeforces 1284G — Seollal` (Chessboard Independent-Set Degree Bounds via Graphic $\cap$ Partition Matroid Intersection)
- **Judge Coordinates**: [Codeforces 1284G](https://codeforces.com/problemset/problem/1284/G)
- **Exact Constraints**: $N \times M$ grid ($N, M \le 20$) of `'O'` (usable) and `'X'` (blocked) cells. Construct a spanning tree $T$ on all `'O'` cells such that every non-root **black cell** $(i + j) \equiv 0 \pmod 2$ with $(i, j) \neq (1, 1)$ has **degree $\ge 2$ in $T$** (so it is NOT a leaf of $T$!).
- **Step 1: Non-Graph Diagnostic Signal**:
  In the complement $F = E \setminus T$ (or directly by building a forest $I \subseteq E$ where each black cell $b \in B$ has **at most $2$ tree edges**? Wait: we need each black cell $b \in B$ to have $\deg_T(b) \ge 2$! Equivalently, in $I \subseteq E$, if we select $2|B|$ edges that are **both** a forest in $G$ (**Graphic Matroid $M_1$**) **and** assign **exactly $2$ incident edges to each black cell $b \in B$** (**Partition Matroid $M_2$**, where each edge $e$ has at most one endpoint in the independent set $B$!), then extending $I$ to a full spanning tree $T \supseteq I$ can only *increase* degrees, guaranteeing $\deg_T(b) \ge \deg_I(b) = 2$ for all $b \in B$!).
- **Step 2: Intermediate Algebraic Representation**:
  Why is $M_2$ a **Partition Matroid**? Because $B = \{(i, j) : (i+j) \text{ even}, (i,j) \neq (1,1)\}$ is an **independent set** of the grid graph $G$! Therefore, every grid edge $e \in E$ is incident to **at most one** black cell $b \in B$ (edges incident to $(1,1)$ are incident to $0$ cells in $B$). Partition $E = \bigsqcup_{b \in B} \delta(b) \sqcup \delta((1,1))$:
  - **Matroid $M_1$ (Graphic Matroid)**: $I \subseteq E$ is a forest in $G$ (contains no cycles).
  - **Matroid $M_2$ (Partition Matroid on $B$)**: $|I \cap \delta(b)| \le 2$ for every $b \in B$ (and $|I \cap \delta((1,1))| = 0$).
  A valid spanning tree exists **if and only if** the maximum common independent set $I^* \in \mathcal{I}_1 \cap \mathcal{I}_2$ has size $|I^*| = 2|B|$ (and $G$ is connected)!
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. Run **Unweighted Matroid Intersection** (Section 6.5) on $M_1 \cap M_2$ for at most $2|B| \le 400$ augmentations:
     - Source set $X_1 = \{e \notin I : I \cup \{e\} \in \mathcal{I}_1\}$ (edges not forming a cycle with $I$).
     - Sink set $X_2 = \{e \notin I : I \cup \{e\} \in \mathcal{I}_2\}$ (edges incident to $b \in B$ with $\deg_I(b) < 2$).
     - Exchange edges: for $y \in I$ and $x \notin I$:
       - $y \to x$ if $I - y + x \in \mathcal{I}_1$ ($y$ lies on the fundamental cycle of $x$ in $I$);
       - $x \to y$ if $I - y + x \in \mathcal{I}_2$ ($x$ and $y$ are incident to the same saturating black cell $b \in B$).
     - Find a **shortest** $X_1 \to X_2$ path via BFS and set $I \gets I \oplus V(P)$.
  2. If $|I^*| < 2|B|$ (or $G$ is disconnected), output `NO`. Otherwise, greedily add remaining edges of $E \setminus I^*$ that do not form a cycle (Kruskal extension) to complete $I^*$ into a full spanning tree $T$, and print the ASCII grid!
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|E| \le 800$, $r = 2|B| \le 400$; BFS Matroid Intersection takes $O(r \cdot |E|^2) \approx 5 \times 10^7$ ops across testcases ($< 0.3\text{ s}$).
  - **Broken Gadget Warning**: You **must** augment along a **shortest** path in the exchange graph (found via BFS) so that chord-free exchange preserves independence in both $M_1$ and $M_2$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Every grid edge connects a black cell and a white cell, so no edge connects two black cells!
  - *Hint 2*: First find a forest $I \subseteq E$ of size $2|B|$ in which every non-root black cell has degree **exactly $2$**, then extend $I$ to a spanning tree using any remaining edges.
  - *Hint 3*: Finding a forest $I$ ($M_1 = \text{Graphic}$) where each black cell has degree $\le 2$ ($M_2 = \text{Partition}$) is a textbook 2-Matroid Intersection problem!

---

#### P27 — `Codeforces 1556H — DIY Tree` (FPT $2^{\binom{K}{2}}$ Core Forest Enumeration + Weighted Graphic $\cap$ Partition Matroid Intersection)
- **Judge Coordinates**: [Codeforces 1556H](https://codeforces.com/problemset/problem/1556/H)
- **Exact Constraints**: Complete weighted undirected graph $K_N$ ($N \le 50$, $w_{uv} \le 100$). Find a minimum-weight spanning tree $T$ subject to degree bounds $\deg_T(i) \le d_i$ on the **first $K \le 5$ vertices** $\{1, \dots, K\}$.
- **Step 1: Non-Graph Diagnostic Signal**:
  Degree bounds on $\{1, \dots, K\}$ are NOT a single Partition Matroid if edges inside $\{1, \dots, K\}$ are present (since an edge $(u, v)$ with $1 \le u < v \le K$ touches **two** degree-constrained vertices!). However, $K \le 5$ has only $\binom{K}{2} \le 10$ internal edges (and only $5^{5-2} \dots$ or $\le 291$ labeled forests on $K = 5$ vertices!).
- **Step 2: Intermediate Algebraic Representation**:
  First, prune the $\binom{N - K}{2}$ edges that lie completely outside $\{1, \dots, K\}$ by running Kruskal on $\{K+1, \dots, N\}$ and keeping only the $\le N - K - 1$ MST edges among $\{K+1, \dots, N\}$ (since any other edge completely outside $\{1, \dots, K\}$ can never beat the MST of $\{K+1, \dots, N\}$!).
  Next, enumerate every valid **internal forest** $F_0$ on $\{1, \dots, K\}$ satisfying $\deg_{F_0}(i) \le d_i$. Once $F_0$ is fixed and contracted:
  - Every remaining candidate edge $e \in E_{\text{rem}}$ touches **at most one** vertex in $\{1, \dots, K\}$!
  - Thus, for each fixed $F_0$, completing the spanning tree is **Minimum-Weight Matroid Intersection** of $M_1$ (Graphic Matroid with $F_0$ contracted) and $M_2$ (Partition Matroid with residual degree caps $d'_i = d_i - \deg_{F_0}(i)$ on $i \in \{1, \dots, K\}$)!
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. Pre-reduce edges inside $\{K+1, \dots, N\}$ to at most $N - K - 1 \le 44$ edges. Now total candidate edges $|E_{\text{rem}}| \le K(N - K) + (N - K - 1) \le 269$!
  2. Enumerate all acyclic subsets $F_0 \subseteq \binom{\{1,\dots,K\}}{2}$ ($\le 291$ forests for $K = 5$) with $\deg_{F_0}(i) \le d_i$.
  3. Run **Weighted Matroid Intersection** (augmenting along shortest paths by `(weight, hop_count)` in the exchange graph for $N - 1 - |F_0|$ steps) and take the minimum total weight over all $F_0$.
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: Pre-reducing $\{K+1, \dots, N\}$ shrinks $|E_{\text{rem}}|$ from $1225$ to $\le 269$; further, only the $N - 1$ lightest edges incident to each $i \in \{1, \dots, K\}$ are needed, running comfortably in $< 1.5\text{ s}$.
  - **Broken Gadget Warning**: When finding the shortest augmenting path in **Weighted** Matroid Intersection, you **must** minimize the tuple `(total_weight, number_of_edges)` (breaking weight ties by **fewest edges**) so that shortcut chords do not invalidate matroid independence!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Which edges violate the Partition Matroid condition by touching **two** constrained vertices? Only the $\binom{K}{2} \le 10$ edges inside $\{1, \dots, K\}$!
  - *Hint 2*: Also notice that among the $\binom{N-K}{2}$ edges completely inside $\{K+1, \dots, N\}$, only the MST edges of $\{K+1, \dots, N\}$ can ever be useful!
  - *Hint 3*: Brute-force the forest $F_0$ on $\{1, \dots, K\}$ ($\le 291$ choices) and solve Weighted Graphic $\cap$ Partition Matroid Intersection on the remaining $\le 269$ edges.

---

#### P28 — `[省选联考 2020 A 卷] 魔法商店` (Inverse Linear Matroid Basis via XOR Exchange DAG & $L_2$ Isotonic Regression)
- **Judge Coordinates**: [Luogu P6621](https://www.luogu.com.cn/problem/P6621) | [LOJ 3300](https://loj.ac/p/3300)
- **Exact Constraints**: $n \le 1000$ items with 64-bit XOR attributes $c_i \le 2^{64}-1$ and initial prices $v_i \le 10^6$, plus two designated Linear Matroid bases $A, B \subseteq \{1, \dots, n\}$ ($|A| = |B| = m \le 64$). Modify prices to integer $w_i$ to minimize $\sum_{i=1}^n (w_i - v_i)^2$ so that $A$ is a **Minimum-Weight Basis** and $B$ is a **Maximum-Weight Basis** under $\mathbf{w}$.
- **Step 1: Non-Graph Diagnostic Signal**:
  First, by the **Matroid Basis Optimality Condition** applied to the Linear Matroid over $\mathbb{F}_2^{64}$:
  - $A$ is a Minimum-Weight Basis $\iff$ for every $y \notin A$ and every $x \in A$ in the unique $\mathbb{F}_2$-linear combination $c_y = \bigoplus_{x \in C_A(y)} c_x$, we have $w_x \le w_y$!
  - $B$ is a Maximum-Weight Basis $\iff$ for every $y \notin B$ and every $x \in B$ in the unique $\mathbb{F}_2$-linear combination $c_y = \bigoplus_{x \in C_B(y)} c_x$, we have $w_x \ge w_y$!
  Once this Partial Order DAG $(V, E_{\le})$ of inequalities $w_u \le w_v$ is built, minimizing $\sum_{i=1}^n (w_i - v_i)^2$ subject to $w_u \le w_v$ is **$L_2$ Isotonic Regression (`L_2 保序回归`)**!
- **Step 2: Intermediate Algebraic Representation**:
  By the Coarea / Parallel Binary Search theorem for Isotonic Regression (Section 6.3), testing whether each item $i$ should have $w_i \le \text{mid}$ or $w_i \ge \text{mid} + 1$ reduces to a **2-point Project Selection / Min-Cut** on the currently active subset $S \subseteq V$:
  - Choosing $w_i = \text{mid}$ costs $(\text{mid} - v_i)^2$;
  - Choosing $w_i = \text{mid} + 1$ costs $(\text{mid} + 1 - v_i)^2$;
  - Marginal difference $\Delta_i(\text{mid}) = (\text{mid} + 1 - v_i)^2 - (\text{mid} - v_i)^2 = 2(\text{mid} - v_i) + 1$, subject to closure $w_u > \text{mid} \implies w_v > \text{mid}$ for $(u, v) \in E_{\le}$!
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. Insert $A$ into a 64-bit Linear Basis (`线性基`); for each $y \notin A$, express $c_y$ as a unique XOR of $x \in C_A(y) \subseteq A$ and add DAG constraint $w_x \le w_y$ ($\forall x \in C_A(y)$).
  2. Insert $B$ into a second 64-bit Linear Basis; for each $y \notin B$, express $c_y = \bigoplus_{x \in C_B(y)} c_x$ and add DAG constraint $w_y \le w_x$ ($\forall x \in C_B(y)$).
  3. Run **Parallel Binary Search (`整体二分`)** `solve(V_sub, L, R)`:
     - Let $\text{mid} = \lfloor (L + R) / 2 \rfloor$. Build a Min-Cut network on $V_{\text{sub}}$:
       - If $\Delta_i(\text{mid}) < 0$ (prefer $\text{mid} + 1$): edge $S \to i$ with capacity $-\Delta_i(\text{mid})$.
       - If $\Delta_i(\text{mid}) > 0$ (prefer $\text{mid}$): edge $i \to T$ with capacity $+\Delta_i(\text{mid})$.
       - For $(u, v) \in E_{\le}$ with $u, v \in V_{\text{sub}}$: edge $u \to v$ with capacity $\infty$.
     - Vertices reachable from $S$ in the residual graph have $w_i^* \ge \text{mid} + 1$ (recurse right to $[\text{mid}+1, R]$); unreachable vertices have $w_i^* \le \text{mid}$ (recurse left to $[L, \text{mid}]$).
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|V| = 1000$, $|E_{\le}| \le 2 n m \le 1.28 \times 10^5$ (can be pruned via transitive/bipartite matching reduction to $O(nm)$); `整体二分` has $\log(10^6) \approx 20$ levels of Dinic, running in $< 0.3\text{ s}$.
  - **Broken Gadget Warning**: When recursing in `solve(V_sub, L, R)`, **only** include vertices in $V_{\text{sub}}$ and edges with **both** endpoints in $V_{\text{sub}}$ so the sum of graph sizes at each depth is $O(N + M)$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Use a 64-bit XOR Linear Basis to find which elements of $A$ represent each $y \notin A$: $A$ is a min-basis iff $w_x \le w_y$ for all such pairs.
  - *Hint 2*: Now you must minimize $\sum (w_i - v_i)^2$ subject to $w_u \le w_v$: this is $L_2$ Isotonic Regression (`保序回归`).
  - *Hint 3*: Use Parallel Binary Search (`整体二分`): at each midpoint $\text{mid}$, run a single $S$-$T$ Min-Cut to partition $V_{\text{sub}}$ into $\{w_i \le \text{mid}\}$ and $\{w_i \ge \text{mid} + 1\}$.

---

#### P29 — `[省选联考 2020 A 卷] 保序回归` (General $L_p$ Isotonic Regression via Submodular Level Cuts & `整体二分`)
- **Judge Coordinates**: [Luogu P6624](https://www.luogu.com.cn/problem/P6624) | [LOJ 3303](https://loj.ac/p/3303)
- **Exact Constraints**: General Isotonic Regression problem: given a poset DAG $(V, E_{\le})$, target values $y_i$, weights $w_i > 0$, and exponent $1 \le p \le 10$, find real (or integer) $x_i$ minimizing $\sum_{i \in V} w_i |x_i - y_i|^p$ subject to $x_u \le x_v$ for all $(u, v) \in E_{\le}$.
- **Step 1: Non-Graph Diagnostic Signal**:
  Generalizes `P28` from $p = 2$ to arbitrary convex $L_p$ norms $g_i(x_i) = w_i |x_i - y_i|^p$ ($p \ge 1$). By Murota's $L^\natural$-Convexity (Section 7.2) and the Lovász Coarea Theorem (Section 6.3), the level sets $S_\lambda = \{i \in V : x_i^* > \lambda\}$ are nested minimum closures!
- **Step 2: Intermediate Algebraic Representation**:
  For any threshold $\lambda$ (or midpoint pair $(\text{mid}, \text{mid} + \epsilon)$), restricting $x_i \in \{\text{mid}, \text{mid} + \epsilon\}$ minimizes:

  $$
  \sum_{i \in V_{\text{sub}}} \Big( g_i(\text{mid}) + \big[x_i = \text{mid} + \epsilon\big] \cdot \big(g_i(\text{mid} + \epsilon) - g_i(\text{mid})\big) \Big) \quad \text{s.t.} \quad x_u \le x_v \;\; (\forall (u, v) \in E_{\le}).
  $$

  By **nestedness of submodular minimizers**, the optimal decision $x_i \in \{\text{mid}, \text{mid} + \epsilon\}$ in the restricted 2-value problem is **identical** to the true global threshold comparison $[x_i^* \ge \text{mid} + \epsilon]$!
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. For $p = 1$ (integer $y_i$): the optimal $x_i^*$ are **integers** bounded by $[\min y_i, \max y_i]$, so we run `整体二分` on integer midpoints $\text{mid}$ with $\epsilon = 1$ and $\Delta_i = w_i(|\text{mid} + 1 - y_i| - |\text{mid} - y_i|) = w_i \cdot \text{sgn}(\text{mid} + 0.5 - y_i)$.
  2. For $p > 1$ (continuous real $x_i^*$): we either run `整体二分` with $\epsilon \to 0^+$ using the derivative $\Delta_i = g'_i(\text{mid}) = p \cdot w_i |\text{mid} - y_i|^{p-1} \text{sgn}(\text{mid} - y_i)$ for $50$ iterations of binary search, OR when an active component $C$ collapses to a single uniform value $x_C^*$, solve $\sum_{i \in C} w_i |x - y_i|^{p-1} \text{sgn}(x - y_i) = 0$ directly!
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $O(\log(\text{Range}/\epsilon) \cdot \text{MaxFlow}(N, M))$.
  - **Broken Gadget Warning**: For $p = 1$, multiple optimal solutions may exist; using integer midpoints $\text{mid}$ with $\epsilon = 1$ automatically finds an **integer** optimal vector $\mathbf{x}^* \in \mathbb{Z}^V$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: By the Coarea Theorem (Section 6.3), minimizing a separable convex function $\sum g_i(x_i)$ subject to $x_u \le x_v$ decouples into independent binary cuts at every threshold $\lambda$.
  - *Hint 2*: To test whether $x_i^* \le \text{mid}$ or $x_i^* > \text{mid}$ for all $i \in V_{\text{sub}}$ simultaneously, restrict $x_i$ to $\{\text{mid}, \text{mid} + \epsilon\}$ and solve a single Minimum Cut.
  - *Hint 3*: Partition $V_{\text{sub}}$ into the $S$-side ($x_i^* > \text{mid}$) and $T$-side ($x_i^* \le \text{mid}$) and recurse via Parallel Binary Search (`整体二分`).

---

#### P30 — `AtCoder ARC 142 E — Pairing Wizards` (Mandatory Baseline Raising, Bipartite Role Split & Unary Threshold Chains)
- **Judge Coordinates**: [AtCoder ARC142E](https://atcoder.jp/contests/arc142/tasks/arc142_e)
- **Exact Constraints**: $N \le 100$ wizards with initial strengths $a_i \in [1, 100]$ and target thresholds $b_i \in [1, 100]$. Given $M$ pairs $(u_e, v_e)$; each pair must satisfy $\max(x_{u_e}, x_{v_e}) \ge \max(b_{u_e}, b_{v_e})$ AND $\min(x_{u_e}, x_{v_e}) \ge \min(b_{u_e}, b_{v_e})$. Raising $a_i$ to $x_i \ge a_i$ costs $x_i - a_i$. Minimize $\sum (x_i - a_i)$.
- **Step 1: Non-Graph Diagnostic Signal**:
  Look at the two conditions on edge $(u, v)$:
  1. $\min(x_u, x_v) \ge \min(b_u, b_v) \iff x_u \ge \min(b_u, b_v) \text{ AND } x_v \ge \min(b_u, b_v)$. This is a **mandatory deterministic lower bound**! We can immediately update $a_u \gets \max(a_u, \min(b_u, b_v))$ and $a_v \gets \max(a_v, \min(b_u, b_v))$ before doing anything else!
  2. After raising all $a_i$ to their mandatory floors, every wizard falls into one of two disjoint sets:
     - **Satisfied Wizards** $L = \{i : a_i \ge b_i\}$;
     - **Deficient Wizards** $R = \{j : a_j < b_j\}$.
     Wait: can an edge connect two deficient wizards $j_1, j_2 \in R$? If $j_1, j_2$ had an edge, say $b_{j_1} \le b_{j_2}$, then the mandatory rule raised $a_{j_1} \ge \min(b_{j_1}, b_{j_2}) = b_{j_1}$, putting $j_1 \in L$! Thus **NO edge connects two wizards in $R$**! Every remaining active constraint is between $u \in L$ and $v \in R$ ($a_v < b_v$): either $v$ raises itself to $x_v = b_v$, OR its neighbor $u \in L$ raises itself to $x_u \ge b_v$!
- **Step 2: Intermediate Algebraic Representation**:
  - Each deficient wizard $v \in R$ has a **binary** choice $y_v \in \{0, 1\}$: pay $b_v - a_v$ to reach $b_v$ ($y_v = 1$), or stay at $a_v$ ($y_v = 0$).
  - Each satisfied wizard $u \in L$ chooses a threshold level $x_u \in \{a_u, a_u + 1, \dots, 100\}$, encoded by unary variables $z_{u, t} = [x_u \ge t] \in \{0, 1\}$ for $t \in (a_u, 100]$ (each costing $1$, with $z_{u, t} \ge z_{u, t+1}$).
  - For each edge $(u, v)$ with $u \in L, v \in R$ and $a_u < b_v$: we forbid $(y_v = 0 \land z_{u, b_v} = 0)$!
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  1. For each $v \in R$: edge $v \to T$ with capacity $b_v - a_v$ (if cut, $v \in S \implies y_v = 1$; if uncut, $v \in T \implies y_v = 0$).
  2. For each $u \in L$ and $t \in [a_u + 1, 100]$: create node $(u, t)$ with $S \to (u, t)$ of capacity $1$ (or a chain $S \to (u, a_u+1) \to \dots \to (u, 100)$ of capacities $100 - a_u, \dots$—even simpler: just edges $S \to (u, t)$ of cap $1$ and $(u, t+1) \to (u, t)$ of cap $\infty$ so cutting $S \to (u, t)$ for $t \le x_u$ costs $x_u - a_u$!).
     Specifically: let $(u, t) \in T$ mean $z_{u, t} = 1$ (cost $1$ on $S \to (u, t)$), with $(u, t) \to (u, t+1)$ of capacity $\infty$.
  3. For each active requirement $(u \in L, v \in R)$ with $b_v > a_u$: add directed edge **$(u, b_v) \to v$ with capacity $\infty$**! If $(u, b_v) \in S$ ($x_u < b_v$) and $v \in T$ ($y_v = 0$), this $\infty$-edge is cut!
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $|V| \le 100 \times 100 + 2 \le 10002$, $|E| \le 30000$; Dinic runs in $< 15\text{ ms}$.
  - **Broken Gadget Warning**: The entire bipartite decomposition $L \sqcup R$ hinges on first applying the mandatory update $a_u \gets \max(a_u, \min(b_u, b_v))$; without this step, $R$ is not an independent set!
- **3-Tier Progressive Hints**:
  - *Hint 1*: First enforce $\min(x_u, x_v) \ge \min(b_u, b_v)$ greedily by raising $a_u$ and $a_v$ to $\ge \min(b_u, b_v)$.
  - *Hint 2*: After this pre-processing, prove that in every edge $(u, v)$, at least one endpoint already satisfies $a \ge b$!
  - *Hint 3*: Partition wizards into $L = \{a_i \ge b_i\}$ and $R = \{a_i < b_i\}$; $v \in R$ has a binary choice ($a_v$ vs. $b_v$), and $u \in L$ has a unary chain of thresholds $t \in [a_u+1, 100]$.

---

#### P31 — `AtCoder AGC 031 E — Snuke the Phantom Thief` (2D Prefix/Suffix Ranks Compiled to Two Laminar Slot Chains)
- **Judge Coordinates**: [AtCoder AGC031E](https://atcoder.jp/contests/agc031/tasks/agc031_e)
- **Exact Constraints**: $N \le 80$ jewels at $(x_i, y_i)$ with values $v_i \le 10^{15}$, and $M \le 320$ constraints of 4 types:
  - `'L'`: at most $b$ stolen jewels have $x \le a$;
  - `'R'`: at most $b$ stolen jewels have $x \ge a$;
  - `'D'`: at most $b$ stolen jewels have $y \le a$;
  - `'U'`: at most $b$ stolen jewels have $y \ge a$.
  Maximize total stolen value.
- **Step 1: Non-Graph Diagnostic Signal**:
  Suppose we fix the **exact total number of stolen jewels** $K \in \{1, 2, \dots, N\}$, and sort the $K$ stolen jewels by X-coordinate as $x_{(1)} \le x_{(2)} \le \dots \le x_{(K)}$ and by Y-coordinate as $y_{(1)} \le y_{(2)} \le \dots \le y_{(K)}$.
  Then for a fixed $K$, **every constraint translates into a hard lower or upper bound on the $r$-th sorted slot**:
  - "`'L'`: at most $b$ jewels have $x \le a$" $\iff$ the $(b+1)$-th jewel from the left must have $x_{(b+1)} \ge a + 1$!
  - "`'R'`: at most $b$ jewels have $x \ge a$" $\iff$ the $(K - b)$-th jewel from the left must have $x_{(K - b)} \le a - 1$!
  - Analogously, `'D'` and `'U'` become hard coordinate intervals $[Y_{r}^{\min}, Y_{r}^{\max}]$ on the $r$-th Y-slot!
- **Step 2: Intermediate Algebraic Representation**:
  By propagating $X_r^{\min} = \max(X_r^{\min}, X_{r-1}^{\min})$ and $X_r^{\max} = \min(X_r^{\max}, X_{r+1}^{\max})$, for each fixed $K \in \{1, \dots, N\}$, we have $K$ X-rank slots $\{1, \dots, K\}$ with valid intervals $[X_r^{\min}, X_r^{\max}]$ and $K$ Y-rank slots $\{1, \dots, K\}$ with valid intervals $[Y_c^{\min}, Y_c^{\max}]$. Matching $K$ jewels simultaneously to $K$ distinct X-slots and $K$ distinct Y-slots is a **3-Entity Star Matching** $\text{X-Slot} \text{--} \text{Jewel} \text{--} \text{Y-Slot}$ (just like `P01`, or two Partition/Laminar Matroids)!
- **Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**:
  For each $K = 1, \dots, N$:
  1. Compute $[X_r^{\min}, X_r^{\max}]$ ($1 \le r \le K$) and $[Y_c^{\min}, Y_c^{\max}]$ ($1 \le c \le K$).
  2. Build an MCMF network:
     - $S \to \text{XSlot}_r$ ($1 \le r \le K$): capacity $1$, cost $0$.
     - $\text{XSlot}_r \to \text{Jewel}_{i,\text{in}}$ (if $X_r^{\min} \le x_i \le X_r^{\max}$): capacity $1$, cost $0$.
     - $\text{Jewel}_{i,\text{in}} \to \text{Jewel}_{i,\text{out}}$: capacity $1$, min-cost $-v_i$.
     - $\text{Jewel}_{i,\text{out}} \to \text{YSlot}_c$ (if $Y_c^{\min} \le y_i \le Y_c^{\max}$): capacity $1$, cost $0$.
     - $\text{YSlot}_c \to T$ ($1 \le c \le K$): capacity $1$, cost $0$.
  3. If the max-flow from $S$ to $T$ is $K$, update the global answer with $-\text{MinCost}$.
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: $N \le 80$ runs of MCMF on $|V| = 2K + 2N + 2 \le 322$ vertices; runs in $< 0.25\text{ s}$.
  - **Broken Gadget Warning**: Why don't we need to explicitly enforce $x_{(1)} \le x_{(2)} \le \dots \le x_{(K)}$ among the chosen jewels? Because the intervals $[X_r^{\min}, X_r^{\max}]$ are monotone ($X_1^{\min} \le \dots \le X_K^{\min}$ and $X_1^{\max} \le \dots \le X_K^{\max}$): by Hall's Marriage / Convex Bipartite Graph property, $K$ jewels can be matched to the $K$ slots **if and only if** sorting those $K$ jewels by $x_i$ places the $r$-th jewel inside $[X_r^{\min}, X_r^{\max}]$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: What changes if you fix the **total number of stolen jewels** $K \in \{1, \dots, N\}$ in an outer loop?
  - *Hint 2*: Once $K$ is fixed, "at most $b$ jewels have $x \ge a$" simply means the $(K-b)$-th stolen jewel (sorted by $x$) must satisfy $x_{(K-b)} \le a - 1$!
  - *Hint 3*: Match $K$ X-slots to $N$ split jewels to $K$ Y-slots via MCMF for each $K = 1, \dots, N$.

---

#### P32 — `[NOI2019] 序列` & `UOJ 455 — [WC2019] 雪灾与外卖` (Complementary Slackness Residual Anatomy & Simulated MCMF `模拟费用流`)
- **Judge Coordinates**: [Luogu P5470 (`[NOI2019] 序列`)](https://www.luogu.com.cn/problem/P5470) | [UOJ 455 (`[WC2019] 雪灾与外卖`)](https://uoj.ac/problem/455)
- **Exact Constraints**:
  - `NOI2019 序列`: Two arrays $a_1, \dots, a_n$ and $b_1, \dots, b_n$ ($n \le 2 \times 10^5$, $\sum n \le 10^6$). Choose $K$-element subsets $I, J \subseteq \{1, \dots, n\}$ ($|I| = |J| = K$) with $|I \cap J| \ge L$ ($k_{\text{free}} = K - L$ mismatched pairs allowed) to maximize $\sum_{i \in I} a_i + \sum_{j \in J} b_j$.
  - `WC2019 雪灾与外卖`: $N \le 10^5$ mice and $M \le 10^5$ holes (with capacities $c_j$ and shelter costs $w_j$) on a 1D line; minimize total matching distance + shelter cost.
- **Step 1: Non-Graph Diagnostic Signal**:
  In both problems, the underlying combinatorial model is a **Totally Unimodular MCMF network**, but $N \le 2 \times 10^5$ makes running a general graph MCMF solver impossible. By **Complementary Slackness & Residual Path Anatomy (Section 4.1)**, we classify the **finite set of residual augmenting path types** (or maintain the **node potentials / slope offsets** via priority queues) to simulate SSP MCMF in $O(N \log N)$!
- **Step 2: Intermediate Algebraic Representation (`[NOI2019] 序列`)**:
  In the exact MCMF network for `NOI2019 序列`, we send $K$ units of flow from $S$ to $T$. Each index $i$ has $S \to A_i$ (cap $1$, reward $a_i$) and $B_i \to T$ (cap $1$, reward $b_i$). A unit of flow can either:
  1. Cross the **direct matched edge** $A_i \to B_i$ (cap $1$, cost $0$), keeping $i \in I \cap J$; OR
  2. Pass through the **shared free-mismatch bridge** $A_i \to P_{\text{in}} \xrightarrow{\text{cap } K - L} P_{\text{out}} \to B_j$ ($i \neq j$), consuming $1$ unit of the $K - L$ mismatch capacity $c_{\text{free}}$.
- **Step 3: Reverse-Engineering Scratchpad (5 Residual Augmentation Types in `[NOI2019] 序列`)**:
  Maintain the set of indices in 4 states: $(0, 0)$ (neither chosen), $(1, 0)$ ($a_i$ chosen), $(0, 1)$ ($b_i$ chosen), and $(1, 1)$ (both chosen), using **5 max-heaps** ($Q_a, Q_b, Q_{a+b}$ on $(0,0)$, $Q'_{b}$ on $(1,0)$ for $b_i$, and $Q'_{a}$ on $(0,1)$ for $a_i$). At each of the $K$ augmentations:
  - **If $c_{\text{free}} > 0$**: simply pick $\max(Q_a) + \max(Q_b)$ and decrement $c_{\text{free}}$ (if the same index $i$ is picked or if pairing $a_i$ with an existing $(0,1)$ occurred, increment $c_{\text{free}}$ back!).
  - **If $c_{\text{free}} = 0$ (bridge $P_{\text{in}} \to P_{\text{out}}$ is saturated, only paths conserving or refunding $c_{\text{free}}$ are valid!)**: compare the **3 candidate residual paths**:
    1. **Direct Pair** ($S \to A_i \to B_i \to T$, $\Delta c_{\text{free}} = 0$): $\max_{i \in (0,0)} (a_i + b_i)$;
    2. **Complete $(1,0)$ + Pick new $A_j$** ($S \to A_j \to P_{\text{in}} \gets A_i \to B_i \to T$, $\Delta c_{\text{free}} = 0$): $\max_{i \in (1,0)} b_i + \max_{j \in (0,0)} a_j$;
    3. **Complete $(0,1)$ + Pick new $B_j$** ($S \to A_i \to B_i \gets P_{\text{out}} \to B_j \to T$, $\Delta c_{\text{free}} = 0$): $\max_{i \in (0,1)} a_i + \max_{j \in (0,0)} b_j$.
    *(Note: if both (2) and (3) are combined by completing both $(1,0)$ and $(0,1)$, $\Delta c_{\text{free}} = +1$, which is automatically handled on the next step when $c_{\text{free}} > 0$!)*
- **Step 4: Complete Solution, Complexity & Broken Gadget Warning**:
  - **Complexity**: Each of the $K$ steps performs $O(1)$ lazy heap pops/pushes $\implies O(N \log N)$ total time!
  - **Broken Gadget Warning**: When $c_{\text{free}} > 0$ and you greedily pop $i = \arg\max Q_a$ and $j = \arg\max Q_b$, if $i = j$ (or if $i$ was already in $(0,1)$ so it becomes $(1,1)$), you actually routed flow along $A_i \to B_i$ instead of $P_{\text{in}} \to P_{\text{out}}$, so you **must not decrement $c_{\text{free}}$** (or if both $i \in (0,1)$ and $j \in (1,0)$ became $(1,1)$, you **increment** $c_{\text{free}}$ by $+1$)!
- **3-Tier Progressive Hints**:
  - *Hint 1*: First draw the exact $S$-$T$ MCMF network with the capacity-$(K-L)$ bottleneck edge $P_{\text{in}} \to P_{\text{out}}$ for unmatched pairs.
  - *Hint 2*: What augmenting paths from $S$ to $T$ exist when $P_{\text{in}} \to P_{\text{out}}$ still has residual capacity vs. when it is saturated?
  - *Hint 3*: Maintain 5 priority queues for the 4 state sets $(0,0), (1,0), (0,1), (1,1)$ and simulate $K$ steps of SSP in $O(N \log N)$ time.

---

## 9. Reconciled Quarantined Templates Table (`R-01` to `R-10`)

In accordance with the **Zero Boilerplate Policy**, the following standard template problems from Cohort 1 and Cohort 2 are quarantined from the main problem bank and summarized below for reference:

| Quarantine ID | Problem Title & Judge Coordinates | Underlying Template Archetype | Why Quarantined |
| :--- | :--- | :--- | :--- |
| **R-01** | `Luogu P5960 — 【模板】差分约束算法` | Bellman–Ford Feasibility of $\pi_v - \pi_u \le w_e$ | Pure textbook difference-constraint feasibility template without LP dual optimization. |
| **R-02** | `Luogu P3275 — [SCOI2011] 糖果` | SCC Condensation + DAG Longest Path on $\pi_v - \pi_u \ge w_e$ | Direct difference-constraint lower-bound template. |
| **R-03** | `Luogu P2762 — 太空飞行计划问题` (`网络流 24 题`) | Picard (1976) Maximum Weight Closure (`最大权闭合子图`) | Level-1 Project Selection template without multi-state or submodular twists. |
| **R-04** | `Luogu P4174 — [NOI2006] 最大获利` | Bipartite Project Selection ($A \cap B$ tower-user closure) | Standard closure template covered in Wave 2. |
| **R-05** | `Luogu P3227 — [HNOI2013] 切糕` | Multi-State Monge Cut Chain with Distance-$D$ Cross-Links | Canonical Level-2 multi-state cut template (covered in depth in Wave 2 & referenced in Section 6/7). |
| **R-06** | `Luogu P2756 — 飞行员配对方案问题` (`网络流 24 题`) | Unweighted Bipartite Matching + Flow Inspection | Elementary TU bipartite matching template. |
| **R-07** | `Luogu P3355 — 骑士共存问题` (`网络流 24 题`) | Bipartite Maximum Independent Set via König's Theorem | Standard bipartite vertex cover / independent set template. |
| **R-08** | `Luogu P3381 — 【模板】最小费用最大流` | Standard SSP / Primal–Dual MCMF Solver | Pure algorithm implementation template. |
| **R-09** | `POJ 1273 / Luogu P3376 — 【模板】网络最大流` | Ford–Fulkerson / Dinic Max-Flow Min-Cut | Pure max-flow template. |
| **R-10** | `UOJ 80 — 【模板】二分图最大权匹配` | Kuhn–Munkres (KM) / Primal–Dual Bipartite Matching | Pure primal–dual assignment template. |

---

## 10. Unified Multilingual `[EN]` / `[ZH]` / `[JA]` Bibliography

### `[EN]` Foundational Papers, Polyhedral Combinatorics & Competitive Programming Treatises
1. **Hoffman, A. J., & Kruskal, J. B. (1956)**. *Integral boundary points of convex polyhedra*. In *Linear Inequalities and Related Systems* (Annals of Mathematics Studies, Vol. 38, pp. 223–246). Princeton University Press. (Proves Theorem 5.1: Total Unimodularity $\iff$ integral extreme points for all integer bounds.)
2. **Ghouila-Houri, A. (1962)**. *Caractérisation des matrices totalement unimodulaires*. *Comptes Rendus Hebdomadaires des Séances de l'Académie des Sciences*, 254, 1192–1194. (Proves Theorem 5.2: Equitable $\pm 1$ row/column bicoloring criterion for TU matrices.)
3. **Tutte, W. T. (1965)**. *Lectures on Matroids*. *Journal of Research of the National Bureau of Standards Section B*, 69B, 1–47. (Introduces Network Matrices $M(T, G)$ and proves their Total Unimodularity.)
4. **Edmonds, J. (1970)**. *Submodular functions, matroids, and certain polyhedra*. In *Combinatorial Structures and Their Applications* (pp. 69–87). Gordon and Breach. (Introduces Polymatroids $P(f)$, Base Polyhedra $B(f)$, Edmonds' Greedy Theorem, and the Matroid Intersection Theorem.)
5. **Edmonds, J., & Giles, R. (1977)**. *A min-max relation for submodular functions on graphs*. *Annals of Discrete Mathematics*, 1, 185–204. (Establishes Total Dual Integrality [TDI] of Submodular / Polymatroid Network Flows.)
6. **Seymour, P. D. (1980)**. *Decomposition of regular matroids*. *Journal of Combinatorial Theory, Series B*, 28(3), 305–359. (Proves Theorem 7.1: every Totally Unimodular matrix decomposes into $1$-, $2$-, and $3$-sums of Network Matrices, their Transposes, and $R_{10}$.)
7. **Lovász, L. (1983)**. *Submodular functions and convexity*. In *Mathematical Programming: The State of the Art* (pp. 235–257). Springer. (Introduces the Lovász extension $\hat{f}(\mathbf{x})$ and proves submodularity $\iff$ convexity of $\hat{f}$.)
8. **Murota, K. (1998, 2003)**. *Discrete Convex Analysis*. SIAM Monographs on Discrete Mathematics and Applications. (Develops the theory of $L^\natural$-convex and $M^\natural$-convex functions and their discrete Legendre–Fenchel duality, Theorem 7.2.)
9. **Schrijver, A. (2003)**. *Combinatorial Optimization: Polyhedra and Efficiency* (Vols. A–C). Springer. (Definitive reference on TU matrices, Network Matrices, Submodular Flows, and Matroid Intersection.)
10. **Kolmogorov, V., & Zabih, R. (2004)**. *What energy functions can be minimized via graph cuts?* *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 26(2), 147–159. (Proves Theorem 6.1: degree-2 cut representability $\iff A + D \le B + C$.)
11. **Zivný, S., Cohen, D. A., & Jeavons, P. G. (2009)**. *The expressive power of binary submodular functions*. *Discrete Applied Mathematics*, 157(15), 3347–3358. (Proves that general degree-$\ge 4$ submodular functions are not graph-cut representable even with auxiliary variables.)

### `[ZH]` Chinese Competitive Programming Monographs (`国家集训队论文`) & Tutorials
12. **胡伯涛 [Amber] (2007)**. 《最小割模型在信息学竞赛中的应用》 (*Applications of Minimum Cut Models in Olympiad in Informatics*). *2007 年信息学奥林匹克中国国家集训队论文*. (Establishes systematic pseudo-Boolean cut compilation and closure models.)
13. **周冬 (2008)**. 《浅析最大最小定理在信息学竞赛中的应用》 (*Analysis of Min-Max Theorems in Informatics Competitions*). *2008 年国家集训队论文*. (Derives theconsecutive equation subtraction $DA\mathbf{x} = \mathbf{0}$ and LP duality compilation of `[NOI2008] 志愿者招募` and `[NOI2010] 海拔`.)
14. **姜志豪 (2016)**. 《网络流的一些建模方法》 (*Modelling Methods in Network Flows*). *2016 年国家集训队论文*. (Covers LP Primal–Dual compilations, row-consecutive-ones vs. column-consecutive-ones, and tree-path incidence transformations.)
15. **高睿泉 (2018)**. 《浅谈保序回归问题》 (*On Isotonic Regression Problems*). *2018 年国家集训队论文*. (Introduces the Coarea level-set cut decomposition and Parallel Binary Search `整体二分` method for $L_p$ Isotonic Regression, directly inspiring `[省选联考 2020] 魔法商店` and `保序回归`.)
16. **钟子谦 (2018)**. 《浅谈拟阵的一些拓展及其应用》 (*Extensions of Matroids and Their Applications*). *2018 年国家集训队论文*. (Covers Graphic $\cap$ Partition Matroid Intersection and Submodular Polyhedra in competitive programming.)
17. **陈江伦 (2019)**. 《浅谈模拟费用流问题》 (*On Simulated Min-Cost Flow Problems*). *2019 年国家集训队论文*. (Analyzes residual path anatomy and priority-queue potential maintenance for `[WC2019] 雪灾与外卖` and `[NOI2019] 序列`.)

### `[JA]` Japanese Competitive Programming Treatises (`燃やす埋める` / Matroid / LP Duality)
18. **`noshi91` (2019)**. *「燃やす埋める」と劣モジュラ関数のグラフ表現可能性* (*"Burn or Bury" [Project Selection] and Graph Representability of Submodular Functions*). [noshi91.hatenablog.com](https://noshi91.hatenablog.com/). (Explains Kolmogorov–Zabih submodularity, unary threshold chains, and the Zivný–Cohen–Jeavons degree-4 barrier.)
19. **`maspypy` (2020)**. *線形計画問題（LP）の双対性と最小費用流* (*Duality of Linear Programming and Minimum-Cost Flow*). [maspypy.com](https://maspypy.com/). (Systematic guide to dualizing difference constraints, prefix potentials, and consecutive-ones matrices into MCMF.)
20. **`tatyam` (2021)**. *マトロイド交差の実装と応用* (*Implementation and Applications of Matroid Intersection*). (Covers weighted and unweighted exchange graph augmentation for Graphic $\cap$ Partition Matroid problems such as `CF 1284G` and `CF 1556H`.)
