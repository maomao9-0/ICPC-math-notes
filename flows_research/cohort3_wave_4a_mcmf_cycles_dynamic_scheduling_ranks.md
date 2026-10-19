# Cohort 3 — Wave 4A Master Reconciliation Monograph (Iteration 111)
## Min-Cost Max-Flow (MCMF) Advanced Modelling Part I: Disjoint Paths, Cycle Covers, Dynamic Lazy Scheduling, Resource Reuse, Order-Statistic Ranks & Manhattan Hubs

**Synthesized & Audited From**:
- **Cohort 1 (Iterations 31–35)**: `flows_research/iter_31_to_35_mcmf_cycles_dynamic_scheduling_ranks.md` (1,616 lines, 178 KB)
- **Cohort 2 (Iterations 83–87)**: `flows_research/cohort2_iter_83_to_87_mcmf_cycles_dynamic_scheduling_ranks.md` (1,419 lines, 171 KB)
- **Cohort 3 Targeted Gap-Hunting (Iteration 111)**: Matroid Intersection vs. 2D/3D Coordinate-Rank MCMF Boundaries, Cycle Cover vs. Subtour Elimination & Functional-Graph Decomposition (`CF 1510 B`, `CF 387 D`), and Unified Direction A $\leftrightarrow$ Direction B Compilation Bridges.

---

## Document Role & Pedagogical Mandate

This master monograph is the definitive **Cohort 3 Reconciliation** for **Wave 4A** of the *Network Flows, Minimum Cuts, Matching, Duality & Modelling* textbook. It unifies and stress-tests the independent investigations of Cohort 1 (Iterations 31–35) and Cohort 2 (Iterations 83–87) on the first pillar of **Min-Cost Max-Flow (MCMF) Advanced Modelling**: how multi-agent routing, permutation/cycle decomposition, reverse completion-time scheduling, inventory/cache token conservation, 2D coordinate order-statistics, and $\ell_1^d / \ell_\infty^d$ geometric distances compile mechanically into linear flow conservation equations and convex/linear edge costs.

Every archetype and every curated contest problem in this monograph strictly enforces the **4-Step "Zero Magic Gadgets" Compilation Standard**:
1. **Step 1 — Non-Graph Diagnostic Signal (Recognition)**: What surface pattern in the English problem statement and constraint bounds ($N, M, K, V_{\max}$) tells a solver to abandon greedy or subset-DP and reach for MCMF, and why naive sequential approaches fail.
2. **Step 2 — Intermediate Algebraic / Logical Representation**: Translate the English rules into exact binary/integer decision variables $x_e \in \{0, 1\}$, flow balance equations, potential-reduced costs $c^\pi(u,v)$, reverse-rank multipliers, consecutive interval differences $\Delta_t = I_t - I_{t-1}$, order-statistic box intersections, or dual-norm sign linearizations *before* drawing a single vertex or edge.
3. **Step 3 — Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**: Show step-by-step how each algebraic equation or objective term forces a specific vertex split, directed arc, capacity bound, cost coefficient, or lazy vertex-spawning trigger.
4. **Step 4 — Hand-Checkable Toy Trace & Broken Gadget Counterexamples**: Trace a concrete small instance ($N \le 4$) through residual augmentations (including negative-cost residual backward arcs that uncross paths or reorder job queues), followed by explicit **Broken Gadget Counterexamples** proving what fails if a subtle structural invariant is violated.

---

## 1. Cross-Cohort Blind-Spot Audit & Reconciliation Matrix

Before synthesizing the unified theory and problem bank, we audit Cohort 1 (`iter_31_to_35`) against Cohort 2 (`cohort2_iter_83_to_87`) to record what each cohort caught, what each cohort missed, and how Cohort 3 resolves every discrepancy and fills the remaining theoretical boundaries.

### 1.1 Theoretical & Modelling Blind-Spot Matrix

| Wave 4A Iteration Topic | What Cohort 1 Caught (`iter_31_to_35`) | What Cohort 2 Caught (`cohort2_iter_83_to_87`) | Cohort 1 Blind Spots Fixed by Cohort 2 | Cohort 2 Blind Spots Fixed by Cohort 1 | Cohort 3 Synthesis & Gap-Hunt Additions |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Iter 31 / 83: Disjoint Paths, Cycle Covers, $b$-Matchings & Chinese Postman** | Complete treatment of Suurballe's $k$-disjoint paths; Directed Cycle Covers; **General $b$-Matchings & Degree-Constrained Subgraphs (`度数限制子图`)** with convex degree costs $w(d_v)$; explicit **TU / Odd-Cycle Boundary** (why undirected non-bipartite $b$-matching yields half-integral odd cycles under MCMF and requires Tutte's reduction to General Blossom Matching); Fortune–Hopcroft–Wyllie (1980) NP-completeness of asymmetric round-trip vertex-disjoint paths. | Algebraic **Component-Merging Invariant** ($\text{Paths} = N - \sum x_{u,v} = \sum s_v$) with explicit starter hub $H_{\text{start}}$ for bounded-fleet $K$ path covers (`ICPC WF 2015 Catering`); Restricted Floyd–Warshall $d^{(\le \max(u,v))}(u,v)$ derivation for `[ZJOI2011] 营救皮卡丘`; formal **$T$-Join formulation** of Undirected CPP; 3-Node Parity-Aware Vertex Splitting (`[CQOI2012] 交换棋子`). | Cohort 1 did not write out the explicit starter-hub equation $s_v + \sum_u x_{u,v} = 1$ for bounded-fleet DAG path covers or the 3-node endpoint vs. transit parity split (`交换棋子`). | Cohort 2 omitted general $b$-matchings (`度数限制子图`), the non-bipartite odd-cycle half-integrality counterexample + Tutte blossom gadget, and the Fortune–Hopcroft–Wyllie directed round-trip NP-completeness barrier. | **Reconciled in Section 2 & Section 7.2**: Unifies Suurballe, $V_{\text{out}} \to V_{\text{in}}$ cycle covers, the starter-hub fleet invariant, 3-node parity splitting, $b$-matching TU boundaries, and characterizes **when cycle covers decompose cleanly into independent trees + cycles** (`CF 1510 B` Button Lock, `CF 387 D`). |
| **Iter 32 / 84: Dynamic / Lazy Vertex Generation (`动态加点费用流`)** | Full 4-step derivation of reverse completion-time indexing $C = \sum_{j,r} r \cdot t_{\pi(j,r), j}$; **Frontier Slot Dominance Theorem**; $O(N)$ dynamic Johnson potential initialization $\pi(j, r+1)$; **Zkw Primal–Dual Multi-Push Failure Mode** (why pushing $>1$ unit along zero-reduced-cost blocking flows before spawning $(j, r+1)$ misses cheaper second slots on fast chefs). | Explicit proof of **Zero Processing Time ($t_{i,j} = 0$) Stability** (why lazy spawning remains valid when $r \cdot t_{i,j} = (r+1) \cdot t_{i,j}$); detailed **Residual Queue-Reordering Trace** showing how a backward arc $(2,1) \to \text{Job } 1 \to (2,2)$ dynamically shifts an already-scheduled job to an earlier slot on the same machine. | Cohort 1 did not explicitly analyze the degenerate $t_{i,j} = 0$ tie-breaking case or trace intra-machine slot shifting via residual backward arcs. | Cohort 2 did not analyze the Zkw / Dinic-style multi-augmenting blocking flow failure mode when lazy vertex spawning is deferred to the end of a phase instead of inside the DFS. | **Reconciled in Section 3**: Combines the Frontier Slot Dominance proof, $t_{i,j}=0$ degeneracy analysis, intra-machine residual queue-reordering trace, $O(N)$ dynamic Johnson potential update, and the Zkw single-unit / inline-spawning contract. |
| **Iter 33 / 85: Resource Reuse, Inventory & Caching Networks** | Full algebraic derivation connecting Model B (Circulation with lower bounds $f(e) \ge r_t$) via demand substitution $f(e) = r_t + y_e$ to Model A (Bipartite Day/Night Split $X_t, Y_t$); **Direction B Bridge** to extreme-scale $N \le 2 \times 10^5$ Napkin Plan (`[BJWC2018] 餐巾计划问题` Luogu P4480) via **Convexity in Total Fresh Purchases $B$ + Greedy Monotone Deque (FIFO slow laundry / LIFO fast laundry)**. | Head-to-head comparison of **two distinct $K$-Cache Compilation Topologies**: **Compilation 1** (Continuous Timeline Spine of capacity $K-1$ + Saving Chords $(t+1) \to \text{next}(t)$ of cost $-c_{a_t}$) vs. **Compilation 2** (Split-Day Token Routing $t_{\text{in}} \to t_{\text{out}}$ with explicit capacity-1 demand enforcement for `CF 802 C`); explicit proof of why adding a free disposal edge $X_t \to T$ destroys Model A in `餐巾计划问题`. | Cohort 1 presented only the timeline saving-chord model for $K$-caching without contrasting it against the split-day $t_{\text{in}} \to t_{\text{out}}$ token routing model of `CF 802 C`, and did not include the $X_t \to T$ disposal counterexample. | Cohort 2 missed the major **Direction B Bridge** to $N \le 2 \times 10^5$ (`[BJWC2018] 餐巾计划问题`) showing how the MCMF graph is completely eliminated by ternary search + two-pointer monotone deques in $O(N \log(\sum r_t))$. | **Reconciled in Section 4**: Unifies the Model B $\equiv$ Model A algebraic transformation, the $X_t \to T$ disposal trap, the dual $K$-cache compilations (Timeline Saving Chord vs. Split-Day Token Routing), and the $O(N \log(\sum r_t))$ Direction B monotone-deque elimination. |
| **Iter 34 / 86: 2D Prefix/Suffix Coordinate Rank Translation (`AGC 031 E`)** | 4-step derivation of fixed-cardinality $K$ rank translation (`L/R/D/U` $\to$ bounding boxes $[L_p^x, R_p^x] \times [L_q^y, R_q^y]$); complete proof of the **Monotone Interval Uncrossing Lemma** via cross-difference inequality $(x_2 - x_1)(y_2 - y_1) \ge 0$ and zero-cost residual cycle cancellation. | Explicit **Interval Monotonization Recurrences** $L_X(p) = \max(L_X(p-1), \dots)$, $R_X(p) = \min(R_X(p+1), \dots)$ before graph construction; explicit failure mode of accepting flows of size $f < K$ when suffix bounds $K - b_m$ are parameterized by exact cardinality $K$. | Cohort 1 did not write the explicit prefix/suffix preprocessing recurrence for $L_X(p), R_X(p)$ or highlight the $f < K$ partial-flow invalidation trap. | Cohort 2 did not explain *why* 2D coordinate-rank translation works in 2D (`L/R/D/U`) yet breaks down if a 3rd coordinate $Z$ (`F/B`) is added. | **Reconciled in Section 5 & Section 7.1**: Unifies the rank translation, interval monotonization recurrences, Uncrossing Theorem, and proves the **Matroid Intersection Boundary** (why 2D is the intersection of two laminar/chain partition matroids solvable by 4-layer MCMF, whereas 3D is NP-hard 3-Matroid Intersection). |
| **Iter 35 / 87: Absolute-Value & Manhattan / Chebyshev Hub Linearization (`AGC 034 D`)** | Full derivation of $\ell_1^d$ dual-norm sign linearization $\|p - q\|_1 = \max_{\sigma \in \{\pm 1\}^d} \langle \sigma, p - q \rangle$ via $2^d$ sign-combination hubs; **Minimization Failure Proof** (why min-cost $\ell_1$ matching picks antipodal sign hubs $\sigma' = -\sigma$ to produce $-\|p - q\|_1$); synthesis of 3D Manhattan hubs with lazy convex degree penalties $a_i d_i^2$. | Generalization to **$d$-Dimensional Chebyshev ($\ell_\infty^d$) Matching**, proving that $\ell_\infty^d$ requires **only $2d$ hubs** $(k, s) \in \{1,\dots,d\} \times \{\pm 1\}$ instead of $2^d$ hubs! Plus **Direction B Regret-Heap Bridge** for $K$-group assignment (`AGC 018 C — Coins`). | Cohort 1 did not include the $2d$-hub Chebyshev ($\ell_\infty^d$) linearization or the `AGC 018 C` 3-group regret-heap elimination. | Cohort 2 did not combine multi-dimensional sign hubs with convex degree-cost penalties $a_i d_i^2$. | **Reconciled in Section 6**: Synthesizes both the $2^d$-hub $\ell_1^d$ and $2d$-hub $\ell_\infty^d$ dual-norm linearizations, proves why $\ell_1 \leftrightarrow \ell_\infty$ rotate in $2D$ ($4 = 2^2 = 2 \cdot 2$) but diverge for $d \ge 3$ ($2^d$ vs. $2d$), and unifies hub topologies with convex degree penalties and regret-heap elimination. |

---

### 1.2 Practice Problem Cross-Cohort Deduplication & Tier Audit

Across Cohort 1 (22 problems) and Cohort 2 (22 problems), there were **14 shared benchmark problems** and **16 cohort-unique problems**, yielding a combined master pool of **30 unique non-template problems**. In Section 8, all 30 problems are retained and reconciled into a unified 4-Tier progression (`Stepping Stone` P01–P07, `Intermediate` P08–P15, `Advanced` P16–P23, `Mastery` P24–P30) with zero omissions.

| Master ID & Tier | Problem Title & Judge Coordinates | Cohort 1 ID | Cohort 2 ID | Core Reconciled Modelling Archetype |
| :--- | :--- | :---: | :---: | :--- |
| **P01** (`Stepping Stone`) | **Collect-Once Multi-Walker Grid** (`Luogu P2045 方格取数加强版` / `POJ 3422` / `Luogu P1006 传纸条`) | C1-P01 | C2-P01 | Parallel $(1, 1 - w_{i,j}) \oplus (K-1, 0)$ cell-splitting for $K$ monotone walkers |
| **P02** (`Stepping Stone`) | **Maximum Internally Vertex-Disjoint Shortest Paths** (`Luogu P2153 [SDOI2009] 晨跑`) | — | C2-P02 | Classical Suurballe vertex-splitting $v_{\text{in}} \to v_{\text{out}}$ (`cap = 1, cost = 0`) |
| **P03** (`Stepping Stone`) | **Suurballe's Edge-Disjoint Round Trip** (`UVa 10806` / `POJ 2135 Dijkstra, Dijkstra.`) | C1-P05 | — | Two-unit edge-disjoint min-cost flow & residual path uncrossing |
| **P04** (`Stepping Stone`) | **DAG Path Cover with Arbitrary Teleport Resets** (`Luogu P2469 [SDOI2010] 星际竞速`) | C1-P02 | C2-P03 | Bipartite $V_{\text{out}} \to V_{\text{in}}$ path cover with $S \to v_{\text{in}}$ teleport start arcs |
| **P05** (`Stepping Stone`) | **Multi-Speed Resource Refurbishment** (`Luogu P1251 [网络流24题] 餐巾计划问题`) | C1-P03 | C2-P04 | Bipartite Day/Night split ($X_t, Y_t$) $\equiv$ Lower-bound spine demand substitution |
| **P06** (`Stepping Stone`) | **Heterogeneous Parallel Machine Total Completion Time** (`Luogu P2053 [SCOI2007] 修车`) | C1-P04 | C2-P06 | Reverse completion-time slot indexing $(j, r)$ with weight $r \cdot t_{i,j}$ |
| **P07** (`Stepping Stone`) | **Multi-Period Capacitated Inventory** (`Luogu P2517 [HAOI2010] 订货`) | C1-P07 | — | Single-line temporal flow balance $I_{t-1} + x_t = d_t + I_t$ with warehouse cap $S$ |
| **P08** (`Intermediate`) | **Weighted $K$-Slot Cache Retention** (`CF 802 C — Heidi and Library (medium)`) | — | C2-P05 | Dual $K$-Cache Compilations: Timeline saving chords vs. Split-day $t_{\text{in}} \to t_{\text{out}}$ |
| **P09** (`Intermediate`) | **Maximum-Weight $K$-Overlap Interval Selection** (`POJ 3680 — Intervals`) | C1-P10 | C2-P07 | Consecutive coordinate-compressed inequality differences & $K$-spine bypass chords |
| **P10** (`Intermediate`) | **Bitonic Round-Trip Max-Vertex Tour** (`Luogu P2770 [网络流24题] 航空路线问题`) | C1-P08 | C2-P08 | Monotone index-ordered 2-path flow + path reconstruction via residual flow |
| **P11** (`Intermediate`) | **Multi-Rover Collect-Once Grid & Flow Path Decomposition** (`Luogu P3356 [网络流24题] 火星探险问题`) | — | C2-P10 | Collect-once grid MCMF + greedy DFS unit-flow decomposition into $K$ rover trajectories |
| **P12** (`Intermediate`) | **Fleet Bounded-Start DAG Path Cover** (`ICPC WF 2015 C — Catering` / `UVA 1711`) | C1-P20 | C2-P09 | Component-merging invariant with capacity-$K$ starter hub $H_{\text{start}}$ |
| **P13** (`Intermediate`) | **Weighted Mixed Graph Eulerian Orientation** (`POJ 1637 Sightseeing Tour` Weighted / `CF 1070 I`) | C1-P09 | — | Reference orientation parity check $\Delta(v) \equiv 0 \pmod 2$ + half-unit reversal MCMF |
| **P14** (`Intermediate`) | **Branch Network / Lower-Bound Directed CPP on DAGs** (`Luogu P4043 [AHOI2014/JSOI2014] 支线网络`) | C1-P14 | — | Tree/DAG edge coverage $f(e) \ge 1$ with free return arcs $u \to 1$ via demand substitution |
| **P15** (`Intermediate`) | **Parametric All-$k$ Bipartite Matching Curve** (`AtCoder ABC 247 G — Dream Team`) | — | C2-P11 | Step-by-step SSP slope profile extraction across all flow volumes $k = 1 \dots K_{\max}$ |
| **P16** (`Advanced`) | **Dynamic Lazy Vertex Spawning for Large-Scale Scheduling** (`Luogu P2050 [NOI2012] 美食节`) | C1-P12 | C2-P12 | Frontier slot dominance (`动态加点费用流`), $O(P)$ active slots, dynamic potentials |
| **P17** (`Advanced`) | **Precedence-Locked Multi-Agent Shortest Path Cover** (`Luogu P4542 [ZJOI2011] 营救皮卡丘`) | C1-P06 | C2-P13 | Restricted Floyd–Warshall $d^{(\le \max(u,v))}(u,v)$ + $K$-walker DAG path cover |
| **P18** (`Advanced`) | **Scaling Collect-Once $K$-Walks via SCC Condensation** (`AtCoder ABC 214 H — Collecting`) | C1-P13 | C2-P14 | Tarjan SCC condensation + potential-initialized DAG MCMF at $N, M \le 2 \times 10^5$ |
| **P19** (`Advanced`) | **Next-Occurrence Hub Sparsification for $K$-Subsequence Cover** (`CF 818 G — Four Melodies`) | C1-P11 | C2-P15 | Persistent value & $\bmod 7$ residue relay hubs reducing $O(N^2)$ transitions to $4N$ arcs |
| **P20** (`Advanced`) | **2D Dominance Poset Transitive Reduction for Collect-Once Walks** (`BZOJ 1930 / Luogu P2172 [SHOI2003] 吃豆豆`) | C1-P15 | C2-P16 | Hasse diagram / running-minimum $Y$-threshold pruning + bypass node $v_{\text{pass}}$ |
| **P21** (`Advanced`) | **Boolean Poset DAG Path Cover with Reset Transitions** (`CF 1510 B — Button Lock`) | — | C2-P17 | Bitmask subset DAG path cover where `R` resets compile to $u_{\text{out}} \to T$ cost $+1$ |
| **P22** (`Advanced`) | **Parity-Aware 3-Node Vertex Splitting for Endpoint vs. Transit Costs** (`Luogu P3159 [CQOI2012] 交换棋子`) | — | C2-P21 | Tri-split $(v_{\text{in}}, v_{\text{mid}}, v_{\text{out}})$ decoupling odd/even swap budgets $m_{i,j}$ |
| **P23** (`Advanced`) | **Multi-Shift Server Reuse & Interval Equation Differences** (`Luogu P3980 [NOI2008] 志愿者招募`) | C1-P17 | — | Consecutive equality differencing $E_t - E_{t-1}$ turning range coverage into single chords |
| **P24** (`Mastery`) | **2D Prefix/Suffix Coordinate Rank Translation** (`AtCoder AGC 031 E — Snuke the Phantom Thief`) | C1-P18 | C2-P18 | Fixed-$K$ rank bounding boxes + 4-layer MCMF + Monotone Interval Uncrossing Theorem |
| **P25** (`Mastery`) | **4-Hub Dual-Norm Manhattan Linearization** (`AtCoder AGC 034 D — Manhattan Max Matching`) | C1-P19 | C2-P19 | $2^2 = 4$ sign-combination hubs $H_{\pm 1, \pm 1}$ reducing $O(N^2)$ bipartite matching to $4N$ arcs |
| **P26** (`Mastery`) | **Time-Expanded Quadratic Congestion Flow with Lazy Parallel Edges** (`CF 1187 G — Gang Up`) | C1-P21 | — | Time-layered graph $V \times \{0 \dots N+K\}$ with marginal odd-number cost increments $(2k-1)d$ |
| **P27** (`Mastery`) | **Extreme-Scale Napkin Plan via Convexity + Monotone Deque** (`Luogu P4480 [BJWC2018] 餐巾计划问题`) | C1-P16 | — | Direction B elimination: Ternary search on total purchases $B$ + FIFO/LIFO two-pointer deques |
| **P28** (`Mastery`) | **Parametric MCMF Slope Envelope & LP Duality** (`CF 1307 G — Cow and Exercise`) | — | C2-P20 | Residual shortest-path slope profile $(f_k, C_k)$ evaluating $\min_k (C_k + x)/f_k$ in $O(1)$ per query |
| **P29** (`Mastery`) | **Direction B Bridge: Eliminating 3-Group MCMF via Regret Heaps** (`AtCoder AGC 018 C — Coins`) | — | C2-P22 | Coordinate shift $c_i + (a_i - c_i)x_i + (b_i - c_i)y_i$ + prefix/suffix split priority queues |
| **P30** (`Mastery`) | **3D Manhattan–Chebyshev Hub Matching with Lazy Convex Degree Penalties & Cycle-Cover Synthesis** (`Grandmaster Synthesis` / `CF 387 D` / `QOJ Multi-Hub`) | C1-P22 | — | $2^3=8$ $\ell_1^3$ hubs $\oplus$ $2d$ $\ell_\infty^d$ hubs + lazy convex degree penalties $a_i d_i^2$ |

---

### 1.3 Quarantine & Template Exclusion Reconciliation

Both Cohort 1 and Cohort 2 quarantined textbook templates (`Luogu P3381`, `Luogu P4014`, `Luogu P3376`, `CSES Task Assignment`, `Luogu P2763`, `Luogu P2756`). Cohort 1 additionally quarantined `LOJ #102`, `POJ 2195`, `Luogu P4015`, and `Luogu P2762`, while Cohort 2 additionally quarantined `Luogu P2764` ( unweighted minimum path cover) and `Library Checker — Assignment Problem`. All 12 quarantined template problems are consolidated in **Section 8.5 (`R-01` through `R-12`)** so they never pollute the curated problem bank.

---

## 2. Iteration 31 / 83 Reconciled: Min-Cost Disjoint Paths, Cycle Covers, $b$-Matchings & Chinese Postman

### 2.1 Suurballe's $k$-Disjoint Shortest Paths & Collect-Once Grid/DAG Walks

#### Step 1: Non-Graph Diagnostic Signal (Recognition)
- **Surface Clues**:
  1. "Find $k$ edge-disjoint (or internally vertex-disjoint) paths from $s$ to $t$ minimizing total edge weight."
  2. "Send $k$ agents across a DAG or grid from $(1, 1)$ to $(H, W)$ to maximize total collected cell/vertex rewards, where each cell's reward can be collected **at most once** even if multiple agents visit it."
  3. "Find a minimum-cost round trip from $s$ to $t$ and back to $s$ using no shared edges/vertices."
- **Why Naive Greedy Fails (The Interlacing Trap)**:
  Suppose we greedily extract the single shortest $s \leadsto t$ path $P_1$, delete its edges, and then find the shortest path $P_2$ in $G \setminus P_1$. On the standard 4-vertex interlacing diamond $s \xrightarrow{1} u \xrightarrow{1} v \xrightarrow{1} t$ with side chords $s \xrightarrow{2} v$, $u \xrightarrow{2} t$, and a long bypass $s \xrightarrow{10} t$:
  - Greedy picks $P_1 = (s \to u \to v \to t)$ of cost $3$. Deleting $P_1$ destroys the middle bridge $u \to v$, forcing $P_2 = (s \to t)$ of cost $10$ (total cost $13$, or complete disconnect if the bypass is absent).
  - The optimal $2$-disjoint paths are $(s \to u \to t)$ and $(s \to v \to t)$ of total cost $6$, which avoids $u \to v$ altogether!
- **Why Multi-Walker DP Fails**: Tracking $k$ simultaneous walkers via dynamic programming requires $O(N^k)$ state space, which explodes for $k \ge 3$ or general graphs.

#### Step 2: Intermediate Algebraic / Logical Representation
Let $x_{u,v} \in \{0, 1\}$ indicate whether directed edge $(u,v) \in E$ is traversed by one of the $k$ paths.

1. **Flow Conservation ($k$ Concurrent Paths)**:
   $$\sum_{v: (u,v) \in E} x_{u,v} - \sum_{w: (w,u) \in E} x_{w,u} = \begin{cases} +k & \text{if } u = s, \\ -k & \text{if } u = t, \\ 0 & \text{if } u \in V \setminus \{s, t\}. \end{cases}$$

2. **Vertex-Disjointness via Auxiliary Flow Variable $y_u$**:
   If paths must be *internally vertex-disjoint*, let $y_u = \sum_{w} x_{w,u} = \sum_{v} x_{u,v}$ be the total flow passing through vertex $u \notin \{s, t\}$. Enforcing $y_u \le 1$ is a linear capacity constraint on the scalar vertex throughput $y_u$.

3. **Collect-Once Node Rewards via Two-Piece Concave Gain Decomposition**:
   Suppose $y_u \in \{0, 1, \dots, k\}$ walkers pass through vertex $u$, which yields reward $w_u \ge 0$ if $y_u \ge 1$ and $0$ if $y_u = 0$. The reward function $R(y_u) = w_u \cdot \min(y_u, 1)$ is concave in $y_u$ (or equivalently, $-R(y_u)$ is convex). We decompose $y_u$ into two parallel binary/integer variables:
   $$y_u = y_u^{(1)} + y_u^{(2)}, \qquad y_u^{(1)} \in [0, 1], \quad y_u^{(2)} \in [0, k-1]$$
   with linear cost contribution $-w_u y_u^{(1)} + 0 \cdot y_u^{(2)}$. Since $-w_u \le 0$, any min-cost solver saturates the reward-bearing slot $y_u^{(1)} = 1$ on the **first** walker before routing the remaining $y_u^{(2)} = y_u - 1$ walkers through the zero-cost bypass slot!

#### Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)

| Algebraic Constraint / Objective Term | Compiled Graph Gadget (Vertices, Arcs, `(cap, cost)`) |
| :--- | :--- |
| **Edge-Disjoint Routing** $x_{u,v} \in [0, 1]$ | Direct arc $u \to v$ with `(cap = 1, cost = c(u,v))`. |
| **Undirected Edge $(u, v)$ Used in At Most One Direction** | Directed arcs $u \to v$ and $v \to u$, each with `(cap = 1, cost = w(u,v))`. By cost positivity, sending $1$ unit on both $u \to v$ and $v \to u$ forms a positive-cost 2-cycle of net flow $0$, which is strictly suboptimal and automatically cancelled. |
| **Internal Vertex-Disjointness** $y_u \le 1$ | Split $u$ into $u_{\text{in}}$ and $u_{\text{out}}$ connected by internal bridge $u_{\text{in}} \to u_{\text{out}}$ with `(cap = 1, cost = 0)`. Redirect all incoming arcs to $u_{\text{in}}$ and outgoing arcs from $u_{\text{out}}$. |
| **Collect-Once Vertex Reward** $R(y_u) = w_u \min(y_u, 1)$ | Split $u$ into $u_{\text{in}}$ and $u_{\text{out}}$ connected by **two parallel internal arcs**:<br>1. **Harvest Arc**: $u_{\text{in}} \to u_{\text{out}}$ with `(cap = 1, cost = -w_u)` (or shifted to `1 - w_u` / potential-reduced $\ge 0$).<br>2. **Transit Bypass Arc**: $u_{\text{in}} \to u_{\text{out}}$ with `(cap = k - 1, cost = 0)`. |

> [!IMPORTANT]
> **Theorem 2.1 (Suurballe's Edge-Switching & Potential Re-Weighting Invariant, 1974 / 1984)**
> Let $G = (V, E, c)$ have $c(e) \ge 0$. After computing shortest-path distances $\pi(v) = d_G(s, v)$ from $s$ via Dijkstra's algorithm and augmenting $1$ unit of flow along the shortest path $P_1$:
> 1. Every forward edge $(u, v) \in E$ has non-negative reduced cost $c^\pi(u, v) = c(u, v) + \pi(u) - \pi(v) \ge 0$, with $c^\pi(u, v) = 0$ for all $(u, v) \in P_1$.
> 2. In the residual network $G_f$, reversing each saturated edge $(u, v) \in P_1$ into a backward arc $(v, u)$ with residual cost $-c(u, v)$ yields a reduced cost of:
>    $$c^\pi(v, u) = -c(u, v) + \pi(v) - \pi(u) = -c^\pi(u, v) = 0.$$
> 3. Consequently, **all edges in the residual network $G_f$ have non-negative reduced costs $c^\pi \ge 0$**. A second run of Dijkstra's algorithm on $(G_f, c^\pi)$ finds the augmenting path $P_2$ in $O(M \log N)$ time without Bellman–Ford or SPFA! Taking the symmetric difference $P_1 \oplus P_2$ cancels any backward arc $(v, u) \in P_2$ against the forward edge $(u, v) \in P_1$ and splices the prefix $s \leadsto u$ of $P_1$ onto the suffix $u \leadsto t$ of $P_2$ (and $s \leadsto v$ of $P_2$ onto $v \leadsto t$ of $P_1$), yielding two edge-disjoint paths of minimum total weight.

#### Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples
- **Numerical Trace on the Interlacing Diamond**:
  - Vertices $\{s, u, v, t\}$, edges $s \to u (1)$, $u \to v (1)$, $v \to t (1)$, $s \to v (2)$, $u \to t (2)$.
  - **Step 1 (Dijkstra #1)**: $\pi(s)=0, \pi(u)=1, \pi(v)=2, \pi(t)=3$. Shortest path $P_1 = (s \to u \to v \to t)$ has cost $3$.
  - **Step 2 (Residual Re-Weighting)**:
    - Unused chords: $c^\pi(s, v) = 2 + 0 - 2 = 0$, $c^\pi(u, t) = 2 + 1 - 3 = 0$.
    - Reversed arcs of $P_1$: $(u \to s), (v \to u), (t \to v)$ all have $c^\pi = 0$.
  - **Step 3 (Dijkstra #2 on $G_f$)**: Shortest path in $G_f$ under $c^\pi$ is $P_2 = (s \to v \to u \to t)$ with reduced cost $0 + 0 + 0 = 0$ and true cost $c(s,v) - c(u,v) + c(u,t) = 2 - 1 + 2 = 3$.
  - **Step 4 (Uncrossing $P_1 \oplus P_2$)**: The backward arc $v \to u \in P_2$ cancels $u \to v \in P_1$. The remaining active forward arcs are $\{s \to u, u \to t\}$ (cost $3$) and $\{s \to v, v \to t\}$ (cost $3$), giving total cost $3 + 3 = 6$.

- **Broken Gadget Counterexamples**:
  1. **Deleting $P_1$ Instead of Reversing It**: Fails on the diamond above ($P_1$ deletion strands the graph).
  2. **Splitting an Undirected Edge Instead of Using Directed Residual Cancellation**: If an undirected edge $\{u, v\}$ of cost $w$ is naively replaced by a single gadgets or if both $u \to v$ and $v \to u$ are NOT linked properly, one might worry that $u \to v$ and $v \to u$ can both be used. In fact, giving $u \to v$ `(cap=1, cost=w)` and $v \to u$ `(cap=1, cost=w)` independently **is completely safe for $w \ge 0$**: if $P_1$ uses $u \to v$ (leaving residual backward arc $v \to u$ of cost $-w$) and $P_2$ needs to go from $v$ to $u$, Dijkstra will always pick the residual backward arc $v \to u$ of cost $-w$ (cancelling the flow on $\{u,v\}$) before the fresh arc $v \to u$ of cost $+w$. However, if $w < 0$ (reward maximization), independent arcs $u \to v$ and $v \to u$ of cost $-|w| < 0$ create a **negative 2-cycle $u \leftrightarrow v$ of cost $-2|w|$**! Thus, for negative edge weights or undirected graphs with arbitrary costs, undirected capacity must be modelled carefully or run only on DAGs.
  3. **Asymmetric Round-Trip Trap (Fortune–Hopcroft–Wyllie Theorem, 1980)**: Suppose we want an $s \leadsto t$ path $P_1$ and a return $t \leadsto s$ path $P_2$ in a **general directed graph** that are internally vertex-disjoint. Sending $1$ unit from $s \to t$ and $1$ unit from $t \to s$ is a **2-commodity flow** problem; if we merge them into a single circulation, $s \to t$ and $t \to s$ cancel out! Indeed, deciding whether vertex-disjoint $s \leadsto t$ and $t \leadsto s$ paths exist in a general directed graph is **NP-complete** (Fortune, Hopcroft & Wyllie 1980). Round-trip vertex-disjoint routing reduces to single-commodity $2$-flow from $s \to t$ **only when**:
     - The underlying graph is **undirected** (so reversing $t \leadsto s$ produces a valid $s \leadsto t$ path), OR
     - The round trip is **bitonic** over a vertex ordering $1 < 2 < \dots < N$ (`Luogu P2770 航空路线问题`), where both the outbound leg $1 \leadsto N$ and the reversed inbound leg $1 \leadsto N$ move strictly left-to-right along the DAG.

---

### 2.2 Min-Cost Directed Cycle Covers, Component-Merging Invariant & Precedence-Locked Tours

#### Step 1: Non-Graph Diagnostic Signal (Recognition)
- **Surface Clues**:
  1. "Partition all $N$ vertices of a weighted directed graph into a collection of vertex-disjoint directed cycles of minimum total weight."
  2. "Cover all $N$ vertices of a weighted DAG (or metric space with precedence constraints) using at most $K$ vehicles/paths minimizing total travel + vehicle activation cost."
- **Why TSP DP Fails**: For $N \ge 25$, $O(2^N N^2)$ Held–Karp DP is intractable. The key structural question is: **does the problem forbid disjoint cycles (TSP, NP-hard), or does it allow arbitrary cycles / operate on a DAG where cycles cannot exist?**

#### Step 2: Intermediate Algebraic / Logical Representation
Let $x_{u,v} \in \{0, 1\}$ indicate whether directed edge $(u,v) \in E$ is chosen.

1. **Exact Cycle Cover Degree Equations**:
   Every vertex $v \in V$ belongs to a unique directed cycle if and only if its chosen out-degree and in-degree are both $1$:
   $$\sum_{v: (u,v) \in E} x_{u,v} = 1 \quad (\forall u \in V), \qquad \sum_{u: (u,v) \in E} x_{u,v} = 1 \quad (\forall v \in V).$$
   This is the exact **Bipartite Perfect Matching** LP between $V_{\text{out}}$ and $V_{\text{in}}$.

2. **The Component-Merging Invariant for DAG Path Covers**:
   On a DAG, cycles are impossible. In any collection of vertex-disjoint directed paths covering all $N$ vertices:
   - Each vertex $v$ has out-degree $\sum_w x_{v,w} \le 1$ and in-degree $\sum_u x_{u,v} \le 1$.
   - Let $s_v \in \{0, 1\}$ indicate whether vertex $v$ is the **starting vertex** of a path (i.e., has in-degree $0$), and $e_u \in \{0, 1\}$ indicate whether $u$ is the **ending vertex** of a path (i.e., has out-degree $0$). Then:
     $$s_v + \sum_{u: (u,v) \in E} x_{u,v} = 1 \quad (\forall v \in V), \qquad \sum_{w: (u,w) \in E} x_{u,w} + e_u = 1 \quad (\forall u \in V).$$
   - Summing the first equation over all $v \in V$ gives the fundamental **Component-Merging Invariant**:
     $$\underbrace{\sum_{v \in V} s_v}_{\text{Number of Paths } P} + \underbrace{\sum_{(u,v) \in E} x_{u,v}}_{\text{Number of Internal Edges } M_{\text{used}}} = N \iff P = N - \sum_{(u,v) \in E} x_{u,v}.$$
   - If at most $K$ vehicles/paths may be started ($\sum_{v \in V} s_v \le K$), then at least $N - K$ internal transitions must be matched ($\sum_{u,v} x_{u,v} \ge N - K$).

#### Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)

Split each vertex $v \in V$ into a **departure copy $v_{\text{out}}$** (left side) and an **arrival copy $v_{\text{in}}$** (right side).

```
                     +--- (cap K, cost 0) ---> [ H_start ] --- (cap 1, cost start_v) ---+
                     |                                                                  |
                     |                                                                  v
  [ Source S ] ------+--- (cap 1, cost 0) ---> [ u_out ] ----- (cap 1, cost c(u,v)) -> [ v_in ] --- (cap 1, cost 0) ---> [ Sink T ]
                                                   |                                                                         ^
                                                   +---------- (cap 1, cost end_u) ------------------------------------------+
```

| Problem Variant | Compiled Arcs Between $S$, $V_{\text{out}}$, $V_{\text{in}}$, and $T$ | Required Flow Volume |
| :--- | :--- | :--- |
| **Exact Directed Cycle Cover** | • $S \to u_{\text{out}}$ `(cap=1, cost=0)`<br>• $u_{\text{out}} \to v_{\text{in}}$ `(cap=1, cost=c(u,v))`<br>• $v_{\text{in}} \to T$ `(cap=1, cost=0)` | Exact flow $F = N$ |
| **Unbounded-Fleet DAG Path Cover with Teleport Cost $A_v$** (`[SDOI2010] 星际竞速`) | Same as Cycle Cover, plus:<br>• Direct start arc $S \to v_{\text{in}}$ with `(cap=1, cost=A_v)` (representing $s_v = 1$, starting a new path at $v$ for cost $A_v$). | Exact flow $F = N$ (onto $V_{\text{in}} \to T$) |
| **Bounded-Fleet ($\le K$) DAG Path Cover** (`ICPC WF 2015 Catering`) | Introduce a **Starter Hub $H_{\text{start}}$**:<br>• $S \to H_{\text{start}}$ `(cap=K, cost=0)` (bounds total path starts $\sum s_v \le K$)<br>• $H_{\text{start}} \to v_{\text{in}}$ `(cap=1, cost=start_v)`<br>• $S \to u_{\text{out}}$ `(cap=1, cost=0)` and $u_{\text{out}} \to v_{\text{in}}$ `(cap=1, cost=c(u,v))`<br>• $v_{\text{in}} \to T$ `(cap=1, cost=0)` | Exact flow $F = N$ into $T$ (or push $N-K$ units strictly across $V_{\text{out}} \to V_{\text{in}}$) |

> [!TIP]
> **Precedence-Locked Metric Closure (`[ZJOI2011] 营救皮卡丘` — Restricted Floyd–Warshall Trick)**
> Suppose an undirected graph has vertices $0, 1, \dots, N$, and $K$ agents starting at $0$ must visit all vertices such that **vertex $v$ cannot be unlocked/visited until all vertices $1, 2, \dots, v-1$ have been visited**, and moving directly from an already-unlocked vertex $u < v$ to $v$ can traverse intermediate vertices $w$ **only if $w$ is already unlocked ($w \le v$)**.
> - We cannot run standard all-pairs Floyd–Warshall because the shortest path from $u$ to $v$ might pass through a locked vertex $k > v$!
> - Instead, during Floyd–Warshall with outer loop $k = 0, 1, \dots, N$, we record the **restricted shortest path** $D(u, v)$ for $u < v$ using **only intermediate vertices $k \le \max(u, v) = v$**:
>   ```
>   for k = 0 .. N:
>       for i = 0 .. N:
>           for j = 0 .. N:
>               if k <= max(i, j):
>                   dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
>   ```
> - This converts the arbitrary undirected graph into a **weighted transitive DAG** on $\{0, 1, \dots, N\}$ with edges $u \to v$ ($u < v$) of weight $D(u, v)$, which then compiles directly into the Bounded-Fleet ($K$) DAG Path Cover above!

#### Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples
- **Toy Trace (`[SDOI2010] 星际竞速` on $N = 3$ DAG)**:
  - Teleport costs $A = (10, 10, 10)$. Directed edges: $1 \to 2$ (cost $3$), $2 \to 3$ (cost $4$), $1 \to 3$ (cost $9$).
  - Every $v_{\text{in}} \to T$ demands $1$ unit ($F = 3$).
  - Path 1: $S \to 1_{\text{out}} \xrightarrow{3} 2_{\text{in}} \to T$ (cost $3$).
  - Path 2: $S \to 2_{\text{out}} \xrightarrow{4} 3_{\text{in}} \to T$ (cost $4$).
  - Node $1_{\text{in}}$ has no incoming DAG edges, so it must take $S \xrightarrow{10} 1_{\text{in}} \to T$ (cost $10$).
  - Total cost $= 3 + 4 + 10 = 17$, corresponding to $s_1 = 1$ (start at $1$ for cost $10$) followed by $1 \xrightarrow{3} 2 \xrightarrow{4} 3$ (a single path covering all $3$ nodes).
- **Broken Gadget Counterexample (Applying $V_{\text{out}} \to V_{\text{in}}$ Path Cover to a Cyclic Graph)**:
  Suppose we want a **single Hamiltonian path** (fleet size $K = 1$) on a cyclic graph consisting of two triangles $(1 \to 2 \to 3 \to 1)$ and $(4 \to 5 \to 6 \to 4)$ of edge cost $1$, connected by a bridge $3 \to 4$ of cost $100$.
  - With $K = 1$, we need $N - K = 6 - 1 = 5$ edges from $V_{\text{out}} \to V_{\text{in}}$.
  - The bipartite network greedily picks $1 \to 2, 2 \to 3, 3 \to 1$ (a **closed cycle** of $3$ edges!) and $4 \to 5, 5 \to 6$ (an open path of $2$ edges), using $5$ edges of total cost $5$ while completely ignoring the bridge $3 \to 4$!
  - **Why it broke**: A closed cycle of length $L$ absorbs $L$ edges of $V_{\text{out}} \to V_{\text{in}}$ without reducing the number of open path starts $\sum s_v$. Thus, the Component-Merging Invariant $P = N - \sum x_{u,v}$ holds **if and only if the chosen subgraph is acyclic** (guaranteed automatically when $G$ is a DAG, or when closed cycles can be legally absorbed/broken at zero extra cost, see Section 7.2).

---

### 2.3 General $b$-Matchings, Degree-Constrained Subgraphs & The TU / Odd-Cycle Boundary

#### Step 1: Non-Graph Diagnostic Signal (Recognition)
- **Surface Clues**: "Select a subset of edges $F \subseteq E$ such that each vertex $v$ has degree $L_v \le d_F(v) \le R_v$ (or incurs a convex cost $w_v(d_F(v))$ where $w_v(d+1) - w_v(d)$ is non-decreasing) to minimize/maximize total edge + degree weight."
- **Crucial Structural Fork**: Is the underlying graph **Bipartite / Directed**, or is it a **General Non-Bipartite Undirected Graph**?

#### Step 2 & Step 3: Algebraic Formulation & The TU / Odd-Cycle Boundary

1. **Case A — Bipartite Undirected or General Directed Graphs (Exact via MCMF)**:
   - In a bipartite graph $G = (L \cup R, E)$ (or a directed graph with out-degree bounds $d^+(u) \in [L_u^+, R_u^+]$ and in-degree bounds $d^-(v) \in [L_v^-, R_v^-]$), the constraint matrix is **Totally Unimodular (TU)**: every edge variable $x_e \in \{0, 1\}$ has coefficient $+1$ in one row of $L$ (or $V_{\text{out}}$) and $+1$ in one row of $R$ (or $V_{\text{in}}$).
   - **Convex Degree Cost Gadget**: If vertex $u \in L$ pays a convex function $g_u(d)$ of its degree $d \in \{0, 1, \dots, R_u\}$ where marginal costs $\Delta_u(k) = g_u(k) - g_u(k-1)$ satisfy $\Delta_u(1) \le \Delta_u(2) \le \dots \le \Delta_u(R_u)$, we connect $S \to u$ with **$R_u$ parallel unit-capacity arcs**:
     $$\text{Arc } k \in \{1, \dots, R_u\}: \quad S \to u \quad \text{with } (\text{cap} = 1, \text{cost} = \Delta_u(k)).$$
     Because $\Delta_u(1) \le \Delta_u(2) \le \dots$, the min-cost flow solver automatically saturates arc $1$, then arc $2$, ..., up to arc $d$, accumulating the exact convex sum $\sum_{k=1}^d \Delta_u(k) = g_u(d) - g_u(0)$!

2. **Case B — Non-Bipartite Undirected Graphs (Why Bipartite MCMF Fails on Odd Cycles & Tutte's Reduction)**:
   - **Broken Gadget Counterexample (The Odd-Cycle Half-Integrality Trap)**:
     Suppose we take a non-bipartite undirected graph $G = (V, E)$ and try to find a $1$-factor ($d_F(v) = 1$ for all $v$) or $b$-matching by building the bipartite double cover $V_{\text{out}} \to V_{\text{in}}$, adding both $(u_{\text{out}} \to v_{\text{in}})$ and $(v_{\text{out}} \to u_{\text{in}})$ of cost $w(e)$ for each undirected edge $e = \{u, v\} \in E$.
     - Consider $G$ consisting of two disjoint triangles $(1, 2, 3)$ and $(4, 5, 6)$ of edge weight $1$, joined by a single bridge $\{3, 4\}$ of weight $100$.
     - A valid undirected $1$-factor must use the bridge $\{3, 4\}$ (e.g., $\{1,2\}, \{3,4\}, \{5,6\}$ of total weight $1 + 100 + 1 = 102$), because a triangle has $3$ (odd!) vertices and cannot be paired internally.
     - However, in the bipartite double cover $V_{\text{out}} \to V_{\text{in}}$, the solver picks the directed 3-cycles $1_{\text{out}} \to 2_{\text{in}}, 2_{\text{out}} \to 3_{\text{in}}, 3_{\text{out}} \to 1_{\text{in}}$ and $4_{\text{out}} \to 5_{\text{in}}, 5_{\text{out}} \to 6_{\text{in}}, 6_{\text{out}} \to 4_{\text{in}}$ of total cost $6$! In the undirected graph, this corresponds to setting $x_e = 1/2$ around each odd triangle—a **half-integral vertex of the fractional $b$-matching polytope** that violates Edmonds's Odd-Set Blossom inequalities $\sum_{e \in E(U)} x_e \le \lfloor \sum_{v \in U} b_v / 2 \rfloor$!
   - **Tutte's Exact Gadget Reduction (General Undirected $b$-Matching $\to$ 1-Matching / Blossom)**:
     When $G$ is non-bipartite and undirected with small degree bounds $b_v$ and edge capacities $1$:
     - Replace each undirected edge $e = \{u, v\}$ by a path of $2$ edges through two edge-subdivision vertices $e_u, e_v$: $\{u, e_u\}, \{e_u, e_v\}, \{e_v, v\}$.
     - Replace each vertex $v$ by a cluster of $b_v$ clones $v^{(1)}, \dots, v^{(b_v)}$, each connected to $e_v$ for all incident edges $e \ni v$.
     - A perfect 1-matching in this expanded graph (solved via Edmonds's Weighted Blossom algorithm in $O(N^3)$) corresponds bijectively to an integral $b$-matching in $G$: if $e = \{u, v\}$ is selected in the $b$-matching, $e_u$ matches to a clone of $u$ and $e_v$ matches to a clone of $v$; if $e$ is not selected, $e_u$ and $e_v$ match to each other!

---

### 2.4 Directed, Undirected, and Mixed Chinese Postman (CPP)

#### Step 1: Non-Graph Diagnostic Signal (Recognition)
- **Surface Clues**: "Traverse **every edge** of a graph at least once and return to the starting vertex, minimizing total traversal distance (or edge-orientation cost)."
- **Core Principle**: Instead of tracking the Eulerian circuit order, solve for the **extra edge multi-set (augmentation)** $x_e \ge 0$ needed to make the graph Eulerian!

#### Step 2 & Step 3: Algebraic & Graph Compilation across All Three Graph Types

Let $G$ be strongly connected (if directed/mixed) or connected (if undirected).

| CPP Variant | Eulerian Condition | Algebraic Decision Variable $x_e$ & Balance Equation | Exact Solver Compilation |
| :--- | :--- | :--- | :--- |
| **1. Directed CPP** (and DAG Branch Networks `[AHOI2014] 支线网络`) | Every $v \in V$ has $d^+(v) = d^-(v)$. | Let $x_e \in \mathbb{Z}_{\ge 0}$ be extra copies of directed edge $e=(u,v)$ on top of the mandatory $1$ copy. With initial imbalance $\Delta(v) = d^-(v) - d^+(v)$:<br>$$\sum_{e \in \delta^+(v)} x_e - \sum_{e \in \delta^-(v)} x_e = \Delta(v).$$ | **MCMF**: Each $e=(u,v) \in E$ becomes an arc $u \to v$ with `(cap = \infty, cost = c(e))`. Connect $S \to v$ `(cap = \Delta(v), cost = 0)` if $\Delta(v) > 0$, and $v \to T$ `(cap = -\Delta(v), cost = 0)` if $\Delta(v) < 0$. |
| **2. Undirected CPP** | Every $v \in V$ has $d(v) \equiv 0 \pmod 2$. | Let $O = \{v \in V : d(v) \text{ is odd}\}$ ($|O|$ is always even). Adding paths between pairs in $O$ flips the parity of endpoints and adds $+2$ to internal vertices. Thus $x \subseteq E$ must form a **minimum-weight $O$-join**. | **All-Pairs Shortest Paths + General Graph Min-Weight Perfect Matching (Blossom)** on the complete graph $K_{|O|}$ with edge weights $d_G(u, v)$ (cannot use bipartite MCMF because $K_{|O|}$ is non-bipartite!). |
| **3. Weighted Mixed Graph Eulerian Orientation & CPP** (`POJ 1637` Weighted) | Orienting each undirected edge gives $d^+(v) = d^-(v)$. | Arbitrarily orient each undirected edge $e=\{u,v\}$ as $u \to v$ (cost $c_{u \to v}$). Reversing it to $v \to u$ (indicator $x_e \in \{0,1\}$, net cost $\Delta c_e = c_{v \to u} - c_{u \to v}$) changes $d^-(u) - d^+(u)$ by $+2$ and $d^-(v) - d^+(v)$ by $-2$. Thus:<br>1. **Parity Condition**: Initial $\Delta(v) = d^-(v) - d^+(v)$ must be **even** for all $v \in V$ (otherwise impossible!).<br>2. **Half-Unit Flow**: $\sum_{e \in \delta^-(v)} x_e - \sum_{e \in \delta^+(v)} x_e = -\frac{\Delta(v)}{2}$. | **MCMF**: For each arbitrarily oriented undirected edge $u \to v$, add arc $u \to v$ with `(cap = 1, cost = c_{v \to u} - c_{u \to v})`. Supply $b(v) = -\Delta(v)/2$. Saturated flow $x_e = 1$ means reverse $u \to v$ to $v \to u$. |

---

## 3. Iteration 32 / 84 Reconciled: Dynamic / Lazy Vertex Generation in Scheduling (`动态加点费用流`)

### 3.1 Reverse-Order Completion Time Indexing (`[SCOI2007] 修车`)

#### Step 1: Non-Graph Diagnostic Signal (Recognition)
- **Surface Clues**:
  1. "Assign $P$ jobs/orders to $M$ heterogeneous machines/chefs."
  2. "Each machine processes its assigned jobs **sequentially** (one at a time), and the objective is to minimize the **sum of completion times** (or average waiting time) $\sum_{i=1}^P C_i$ across all jobs."
- **Why Forward Indexing Fails**:
  Suppose machine $j$ processes $k_j$ jobs in forward order $q_1, q_2, \dots, q_{k_j}$, where job $q_s$ takes $t_{q_s, j}$ time on machine $j$. Then the completion time of the $s$-th job is $C_{q_s} = \sum_{a=1}^s t_{q_a, j}$.
  - If we index slots in **forward order** ($s = 1, 2, \dots, k_j$), the contribution of job $q_s$ to the total completion time $\sum_{b=s}^{k_j} C_{q_b}$ is $(k_j - s + 1) \cdot t_{q_s, j}$. Because this coefficient depends on the **unknown total number of jobs $k_j$** eventually assigned to machine $j$, forward slot $(j, s)$ cannot be assigned a fixed static edge cost!
- **Why Greedy Fails**:
  Locally assigning each job to the machine that minimizes its immediate completion time ignores how a long job delays all subsequent jobs queued behind it, and ignores heterogeneous compatibility across machines.

#### Step 2: Intermediate Algebraic / Logical Representation (The Reverse-Rank Transformation)
Index the jobs assigned to machine $j$ in **reverse chronological order** (countdown rank from the end of machine $j$'s schedule):
- Rank $r = 1$: the **last** job processed by machine $j$ (delays only itself $\implies$ multiplier $1$).
- Rank $r = 2$: the **second-to-last** job processed by machine $j$ (delays itself and the last job $\implies$ multiplier $2$).
- Rank $r$: the **$r$-th from last** job processed by machine $j$ (delays itself and the $r - 1$ jobs after it $\implies$ multiplier $r$).

Summing over all machines $j \in \{1, \dots, M\}$ and reverse ranks $r \in \{1, \dots, k_j\}$:
$$\sum_{i=1}^P C_i = \sum_{j=1}^M \sum_{r=1}^{k_j} r \cdot t_{\pi(j, r), j}.$$
Now the cost coefficient of assigning job $i$ to reverse slot $(j, r)$ is **completely decoupled** from $k_j$: it is simply $c_{i, (j, r)} = r \cdot t_{i,j}$!

Let $x_{i, j, r} \in \{0, 1\}$ indicate whether job $i$ is placed in reverse slot $(j, r)$. The exact integer program is:
$$\min \sum_{i=1}^P \sum_{j=1}^M \sum_{r=1}^P \left(r \cdot t_{i,j}\right) x_{i, j, r} \quad \text{s.t.} \quad \sum_{j=1}^M \sum_{r=1}^P x_{i, j, r} = 1 \;\; (\forall i), \qquad \sum_{i=1}^P x_{i, j, r} \le 1 \;\; (\forall j, r).$$

> [!NOTE]
> **Automatic Gap-Free Contiguity ($t_{i,j} > 0$ and the Degenerate $t_{i,j} = 0$ Case)**
> Does the LP relaxation need an explicit constraint $\sum_i x_{i, j, r+1} \le \sum_i x_{i, j, r}$ to prevent leaving a hole at rank $r$ while filling rank $r+1$?
> - **When $t_{i,j} > 0$**: Since $r \cdot t_{i,j} < (r+1) \cdot t_{i,j}$, every job strictly prefers slot $(j, r)$ over $(j, r+1)$. Thus any min-cost solution fills slots $r = 1, 2, \dots, k_j$ contiguously without gaps.
> - **When $t_{i,j} = 0$ (Cohort 2 Degeneracy Check)**: If $t_{i,j} = 0$, then $r \cdot t_{i,j} = (r+1) \cdot t_{i,j} = 0$ for all $r$. In the full static graph, a solver could place a zero-time job at $(j, 5)$ while leaving $(j, 1)$ empty, which does not change the objective ($0 = 0$) and can be compressed into a contiguous schedule during post-processing. Under **dynamic lazy spawning** (Section 3.2), slot $(j, r+1)$ does not even exist in the graph until $(j, r)$ is saturated, so contiguous filling $r = 1, 2, \dots, k_j$ is enforced *topologically* even when $t_{i,j} = 0$!

---

### 3.2 Dynamic Lazy Vertex Spawning (`[NOI2012] 美食节`): Frontier Dominance, Residual Queue Reordering, Dynamic Potentials & Zkw Pitfalls

#### Step 1: Scaling Bottleneck & Recognition
In `[SCOI2007] 修车`, $N \le 9, P \le 60$, so the static bipartite graph has $M \cdot P = 540$ slot vertices and $M \cdot P^2 = 32,400$ edges—easily solved in $< 10\text{ ms}$.
In `[NOI2012] 美食节`, there are $N \le 40$ dish types, $M \le 100$ chefs, and $P = \sum p_i \le 800$ total dishes ordered.
- **Static Graph Explosion**: Building all $M \cdot P = 80,000$ slot vertices and $N \cdot M \cdot P = 3.2 \times 10^6$ edges upfront causes SPFA/Dijkstra to scan millions of redundant edges per augmentation, resulting in TLE.
- **Key Observation**: Across all $M$ chefs, the total number of dishes cooked is exactly $P = 800$. Therefore, at the end of the algorithm, **at most $P$ slot vertices $(j, r)$ out of $M \cdot P = 80,000$ are ever saturated!**

#### Step 2: The Frontier Slot Dominance Theorem
For each chef $j \in \{1, \dots, M\}$, define the **frontier rank** $r_j \ge 1$ to be the smallest rank on chef $j$ that is currently unsaturated ($\text{flow}((j, r_j) \to T) = 0$).

> [!IMPORTANT]
> **Theorem 3.1 (Frontier Slot Dominance & Lazy Spawning Invariant)**
> At any stage of the Successive Shortest Path (SSP) algorithm, no shortest augmenting path from $S$ to $T$ needs to visit any unspawned slot $(j, r)$ with $r > r_j$ (and if $t_{i,j} > 0$, no shortest augmenting path *can* visit $(j, r)$ for $r > r_j$).
>
> *Proof*:
> 1. Every unspawned slot $(j, r)$ with $r \ge r_j$ has zero current flow ($\text{flow}((j, r) \to T) = 0$). Therefore, in the residual network $G_f$, the only arcs incident to $(j, r)$ with non-zero residual capacity are **forward incoming arcs** $i \to (j, r)$ (of cost $r \cdot t_{i,j}$) and the **forward sink arc** $(j, r) \to T$ (of capacity $1$, cost $0$). There are **no outgoing residual arcs** from $(j, r)$ back to any dish $i$ because no flow has ever entered $(j, r)$.
> 2. Consequently, any simple augmenting path that visits $(j, r)$ for $r \ge r_j$ must use $(j, r)$ as its **penultimate vertex** immediately before $T$:
>    $$S \leadsto i \xrightarrow{r \cdot t_{i,j}} (j, r) \xrightarrow{0} T.$$
> 3. Since the frontier slot $(j, r_j)$ is also unsaturated, the alternative path $S \leadsto i \xrightarrow{r_j \cdot t_{i,j}} (j, r_j) \xrightarrow{0} T$ is residual-feasible and strictly cheaper by $(r - r_j) t_{i,j} \ge 0$.
> 4. Notice what happens to **already-saturated slots** $(j, s)$ with $1 \le s < r_j$: they *do* have residual backward arcs $(j, s) \to i_{\text{old}}$ of cost $-s \cdot t_{i_{\text{old}}, j}$ and remain in the graph permanently so that future augmentations can **dynamically reorder or reassign** earlier dishes!

#### Step 3: Reverse-Engineering Scratchpad (Lazy Graph Compilation & $O(N)$ Dynamic Potential Update)

1. **Initial Graph ($0$ units of flow)**:
   - Dish nodes $i \in \{1, \dots, N\}$ with $S \to i$ `(cap = p_i, cost = 0)`.
   - Only **rank-1 frontier nodes** $(j, 1)$ for $j \in \{1, \dots, M\}$, with $i \to (j, 1)$ `(cap = 1, cost = 1 \cdot t_{i,j})` and $(j, 1) \to T$ `(cap = 1, cost = 0)`.
   - Initial size: $N + M \le 140$ vertices and $N \cdot M \le 4,000$ arcs.

2. **Single-Unit Augmentation & Inline Spawning Trigger**:
   - In iteration $f \in \{1, \dots, P\}$, find the shortest augmenting path $P_f$ from $S$ to $T$ in $G_f$ and push $\Delta = 1$ unit of flow.
   - Let $(j^*, r_{j^*})$ be the unique frontier node whose sink edge $(j^*, r_{j^*}) \to T$ was just saturated at the end of $P_f$.
   - Immediately **spawn** node $(j^*, r_{j^*} + 1)$, add $(j^*, r_{j^*} + 1) \to T$ `(cap = 1, cost = 0)`, and for each dish type $i \in \{1, \dots, N\}$ add $i \to (j^*, r_{j^*} + 1)$ `(cap = 1, cost = (r_{j^*} + 1) \cdot t_{i, j^*})`.

3. **$O(N)$ Dynamic Johnson Potential Initialization (Cohort 1 & 2 Synthesis)**:
   If we use Dijkstra with Johnson potentials $\pi(v)$ instead of SPFA, what potential $\pi(j^*, r_{j^*} + 1)$ should be assigned to the newly spawned vertex so that all reduced costs remain non-negative *before* the next Dijkstra call?
   - After updating potentials $\pi(v) \gets \pi(v) + d(v)$ from the current Dijkstra run, the newly spawned node $(j^*, r_{j^*} + 1)$ has only incoming residual arcs from $i \in \{1, \dots, N\}$ (of cost $(r_{j^*} + 1) t_{i, j^*}$) and one outgoing residual arc to $T$ (of cost $0$).
   - However, notice that $(j^*, r_{j^*} + 1)$ is a dead-end into $T$: during the *next* Dijkstra run from $S$, the distance $d(j^*, r_{j^*} + 1)$ will be computed directly from $d(i)$ via incoming edges $i \to (j^*, r_{j^*} + 1)$! To ensure both $c^\pi(i, (j^*, r+1)) \ge 0$ and $c^\pi((j^*, r+1), T) \ge 0$, or simply by setting:
     $$\pi(j^*, r_{j^*} + 1) = \min_{1 \le i \le N} \left( \pi(i) + (r_{j^*} + 1) \cdot t_{i, j^*} \right),$$
     every incoming arc $i \to (j^*, r_{j^*} + 1)$ has $c^\pi = (r_{j^*}+1) t_{i, j^*} + \pi(i) - \pi(j^*, r_{j^*}+1) \ge 0$, and because $\pi(i) + r_{j^*} t_{i, j^*} \ge \pi(j^*, r_{j^*}) = \pi(T)$, we also have $\pi(j^*, r_{j^*}+1) \ge \pi(T)$, which means the sink arc $(j^*, r_{j^*}+1) \to T$ can be relaxed or we can set $\pi(T)$ accordingly (or simply treat $(j^*, r_{j^*}+1) \to T$ as having cost $0$ and let $\pi(j^*, r) = \pi(T)$ only when we don't even need $\pi(j^*, r+1)$ until it is reached!). In fact, an even cleaner implementation contracts $(j, r_j) \to T$ conceptually during shortest-path search or initializes $\pi$ via SPFA/Dijkstra.
   - **Final Graph Size**: At termination ($P$ units of flow), the graph has $N + M + P \le 940$ vertices and $N(M + P) \le 36,000$ edges—a **$90\times$ reduction** over the static graph!

#### Step 4: Hand-Checkable Toy Trace (Intra-Machine Queue Reordering) & Broken Gadget Counterexamples
- **Numerical Trace Showing Residual Queue Reordering (`Cohort 2 Trace`)**:
  - $P = 2$ cars (`Car 1`, `Car 2`), $M = 2$ mechanics (`Mech 1`, `Mech 2`).
  - Processing times:
    - `Car 1`: $t_{1,1} = 10$, $t_{1,2} = 2$.
    - `Car 2`: $t_{2,1} = 10$, $t_{2,2} = 5$.
  - **Initial Frontier**: Slots $(1, 1)$ and $(2, 1)$.
  - **Augmentation 1**: Shortest path is $S \to \text{Car } 1 \xrightarrow{2} (2, 1) \to T$ (cost $+2$).
    - Slot $(2, 1)$ is saturated! **Spawn slot $(2, 2)$** with arcs $\text{Car } 1 \xrightarrow{4} (2, 2)$ and $\text{Car } 2 \xrightarrow{10} (2, 2)$.
  - **Augmentation 2 (Residual Queue Reordering!)**: Compare the three available paths from $S \to \text{Car } 2$:
    1. Assign `Car 2` to `Mech 1` slot 1: $S \to \text{Car } 2 \xrightarrow{10} (1, 1) \to T$ (cost $+10$).
    2. Assign `Car 2` to `Mech 2` slot 2 (second-to-last, i.e., **before** `Car 1`): $S \to \text{Car } 2 \xrightarrow{10} (2, 2) \to T$ (cost $+10$).
    3. **Reorder `Mech 2`'s queue via the residual backward arc $(2, 1) \to \text{Car } 1$**:
       $$S \to \text{Car } 2 \xrightarrow{+5} (2, 1) \xrightarrow{-2} \text{Car } 1 \xrightarrow{+4} (2, 2) \to T \quad \text{with net cost } 5 - 2 + 4 = +7!$$
  - The solver takes Path 3 (cost $+7$), bringing the total cost to $2 + 7 = 9$.
  - **Physical Meaning of Path 3**: The residual backward arc $(2, 1) \xrightarrow{-2} \text{Car } 1 \xrightarrow{+4} (2, 2)$ evicts `Car 1` from the *last* slot $(2, 1)$ on `Mech 2` and shifts `Car 1` into the *second-to-last* slot $(2, 2)$ (so `Car 1` now runs **first**, taking $2\text{ min}$), while placing the slower `Car 2` ($5\text{ min}$) into the *last* slot $(2, 1)$! Total completion time $= 2 + (2 + 5) = 9$.

- **Broken Gadget Counterexamples**:
  1. **The Zkw Primal–Dual / Dinic Multi-Path Blocking Flow Trap (`Cohort 1 Discovery`)**:
     Suppose you implement MCMF using **Zkw's Primal–Dual algorithm** (which runs a Dinic-like DFS on the zero-reduced-cost subgraph to push a multi-unit blocking flow in each phase) and only spawn new vertices $(j, r_j + 1)$ **at the end of each phase** rather than immediately after each single unit of flow.
     - **Counterexample**: Suppose Dish 1 has demand $p_1 = 2$. Chef 1 is ultra-fast ($t_{1,1} = 1$) and Chef 2 is slightly slower ($t_{1,2} = 1$). Wait: suppose $t_{1,1} = 1$ and $t_{1,2} = 3$. In Phase 1, $(1, 1)$ has cost $1$. If two dishes have tied costs or if a zero-reduced-cost phase pushes multiple units before $(1, 2)$ (cost $2$) is spawned, the solver is blind to the existence of $(1, 2)$ during the phase and routes the second unit of Dish 1 to Chef 2 at cost $3$ instead of Chef 1's second slot $(1, 2)$ at cost $2$!
     - **Mandatory Fix**: Either push **at most $1$ unit of flow per augmentation** (standard single-path SSP), OR spawn $(j, r_j + 1)$ **inline inside the DFS** the exact instant $(j, r_j) \to T$ becomes saturated!
  2. **Deleting Saturated Slot Nodes $(j, s)$**:
     If you delete $(2, 1)$ after Augmentation 1 in the toy trace to "save memory", Path 3 ($S \to \text{Car } 2 \to (2, 1) \to \text{Car } 1 \to (2, 2) \to T$) becomes impossible, locking `Car 1` permanently into the last slot and forcing suboptimal cost $2 + 10 = 12$ instead of $9$.

---

## 4. Iteration 33 / 85 Reconciled: Resource Reuse, Inventory & Caching Networks

### 4.1 Multi-Speed Resource Refurbishment (`餐巾计划问题`): Bipartite Day/Night Split vs. Lower-Bound Spine Equivalence

#### Step 1: Non-Graph Diagnostic Signal (Recognition)
- **Surface Clues**:
  1. "Over a discrete horizon $t = 1, \dots, N$, day $t$ requires $r_t$ clean resources (napkins, servers, surgical kits)."
  2. "After day $t$'s usage, the $r_t$ used resources become **dirty/exhausted** and can either be stored dirty to the next night or sent to one of several refurbishment modes (e.g., fast laundry taking $d_1$ days at cost $c_1$, slow laundry taking $d_2$ days at cost $c_2$) to re-enter the clean pool on day $t + d_k$."
- **Why Standard Time-Layered Flow Fails**:
  In a standard single-node-per-day timeline $1 \to 2 \to \dots \to N$, a unit of flow leaving day $t$ represents a **clean** resource if it goes to $T$ (satisfying demand $r_t$), leaving **zero** units of flow to travel along the laundry edge $t \to t + d_k$! That is, a single conserved flow token cannot simultaneously exit at $T$ (to verify that $r_t$ clean napkins were consumed on day $t$) *and* continue to day $t + d_k$ as a dirty napkin.

#### Step 2 & Step 3: Algebraic Proof of Equivalence Between Model B (Lower-Bound Circulation) and Model A (Bipartite Day/Night Split)

We now prove algebraically that the two classic representations—**Model B (Circulation with Mandatory Lower Bounds)** and **Model A (Bipartite Morning/Evening Split $X_t, Y_t$)**—are the exact same linear system under a change of variables!

1. **Model B (Continuous Token Timeline with Lower Bounds)**:
   Imagine tracking each physical napkin as a single continuous flow token from purchase ($S$) to final disposal ($T$):
   - Split day $t$ into $t_{\text{in}}$ (start of day $t$'s usage) and $t_{\text{out}}$ (end of day $t$'s usage).
   - **Mandatory Usage Bridge**: Arc $e_t = (t_{\text{in}} \to t_{\text{out}})$ with **lower bound $L(e_t) = r_t$**, upper bound $\infty$ (or exact $L = U = r_t$ if clean storage is separate), cost $0$.
   - **Fresh Purchase**: $S \to t_{\text{in}}$ `(cap = \infty, cost = p)`.
   - **Clean Carryover**: $t_{\text{in}} \to (t+1)_{\text{in}}$ `(cap = \infty, cost = 0)`.
   - **Dirty Storage**: $t_{\text{out}} \to (t+1)_{\text{out}}$ `(cap = \infty, cost = 0)`.
   - **Refurbishment Mode $k$**: $t_{\text{out}} \to (t + d_k)_{\text{in}}$ `(cap = \infty, cost = c_k)`.
   - **End-of-Horizon Disposal**: $t_{\text{out}} \to T$ `(cap = \infty, cost = 0)`.

2. **Algebraic Demand Substitution ($f(e_t) = r_t$) $\implies$ Model A (Standard MCMF Without Lower Bounds)**:
   Set the flow on the usage bridge $e_t = (t_{\text{in}} \to t_{\text{out}})$ to be **exact** $f(e_t) = r_t$ (since any unused clean napkins can bypass $e_t$ via the clean carryover arc $t_{\text{in}} \to (t+1)_{\text{in}}$).
   Substituting $f(e_t) = r_t$ into the flow conservation equations of $t_{\text{in}}$ and $t_{\text{out}}$ eliminates the bridge $e_t$ completely:
   - At clean node $Y_t \equiv t_{\text{in}}$:
     $$\text{Inflow}(Y_t) = \text{Outflow}(Y_t) = r_t + f(Y_t \to Y_{t+1}) \implies \text{Send } Y_t \to T \text{ with } (\text{cap} = r_t, \text{cost} = 0)!$$
   - At dirty node $X_t \equiv t_{\text{out}}$:
     $$\text{Outflow}(X_t) = \text{Inflow}(X_t) = r_t + f(X_{t-1} \to X_t) \implies \text{Send } S \to X_t \text{ with } (\text{cap} = r_t, \text{cost} = 0)!$$
   - Delete the disposal edge $t_{\text{out}} \to T$ (instead, leftover dirty napkins simply stay unpushed at $S \to X_t$, or rather, wait: let's check what happens to $S \to X_t$ vs. $X_t \to T$!).

```
  [Source S] --- (cap r_t, cost 0) ---> [ Dirty Node X_t ] --- (cap inf, cost 0) ---> [ Dirty Node X_{t+1} ]
      |                                         |
      |                                         +--- (cap inf, cost f) ---> [ Clean Node Y_{t+m} ]
      |                                         +--- (cap inf, cost s) ---> [ Clean Node Y_{t+n} ]
      |
      +--------- (cap inf, cost p) ---> [ Clean Node Y_t ] --- (cap r_t, cost 0) ---> [ Sink T ]
                                                |
                                                +--- (cap inf, cost 0) ---> [ Clean Node Y_{t+1} ]
```

#### Step 4: Hand-Checkable Toy Trace & The Broken Disposal-Edge Counterexample
- **Broken Gadget Counterexample 1: Adding a Free Disposal Edge $X_t \to T$ in Model A (`Cohort 2 Audit`)**:
  A very common student mistake in Model A is thinking: *"Not all dirty napkins $r_t$ generated on night $t$ need to be washed; leftover dirty napkins at the end of the horizon are thrown away, so I should add a free disposal arc $X_t \to T$ `(cap = \infty, cost = 0)`."*
  - **What breaks**: If you add $X_t \to T$ with `(cap = \infty, cost = 0)`, the MCMF solver routes all $\sum r_t$ units of flow along the zero-cost path $S \xrightarrow{0} X_t \xrightarrow{0} T$, achieving max flow $\sum r_t$ at **total cost $0$** while leaving every clean demand arc $Y_t \to T$ completely empty!
  - **Why**: In Model A, the sink $T$ is the collector for **satisfied clean demands** $Y_t \to T$. Dirty napkins that are discarded at the end of the horizon simply correspond to **unsaturated capacity** on the supply arcs $S \to X_t$! Because $\text{cut}(T) = \sum_{t=1}^N r_t$ is bottlenecked exclusively by the clean demand arcs $Y_t \to T$, max flow of value $\sum r_t$ saturates every $Y_t \to T$ while only pulling from $S \to X_t$ the exact number of dirty napkins that are actually laundered.
- **Broken Gadget Counterexample 2: Omitting Dirty Deferral $X_t \to X_{t+1}$ When Clean Storage $Y_t \to Y_{t+1}$ Exists (or Vice Versa)**:
  - Usually $Y_t \to Y_{t+1}$ (storing a clean napkin for free) and $X_t \to X_{t+1}$ (storing a dirty napkin for free) are redundant when laundry costs are time-invariant, *except* when $X_t \to X_{t+1}$ has a storage limit or when laundry availability varies by day. Including $X_t \to X_{t+1}$ `(cap = \infty, cost = 0)` is the canonical minimal edge set ($O(N)$ vertices, $4N$ arcs).

---

### 4.2 Direction B Elimination at Extreme Scale (`[BJWC2018] 餐巾计划问题`, $N \le 2 \times 10^5$): Convexity + Monotone Deque

When the horizon scales from $N \le 2,000$ (`Luogu P1251`) to $N \le 2 \times 10^5$ (`Luogu P4480 [BJWC2018] 餐巾计划问题`), even $O(N \log N)$ per augmentation is far too slow because total demand $\sum r_t \le 2 \times 10^{11}$. We must compile the MCMF network *back* into a greedy data-structure algorithm (**Direction B**):

1. **Convexity in Total Fresh Napkins Purchased $B$**:
   Assume without loss of generality that $c_{\text{slow}} < c_{\text{fast}} < p$ and $d_{\text{slow}} > d_{\text{fast}}$ (if $c_{\text{fast}} \le c_{\text{slow}}$, slow laundry is dominated; if $p \le c_{\text{fast}}$, laundry is dominated). All fresh purchases can be made on Day 1 (since clean storage is free). Let $B \in [\max_{t} \text{early\_deficit}, \sum_{t=1}^N r_t]$ be the total number of fresh napkins purchased across the entire horizon. By the convexity of minimum-cost flow cost as a function of total flow on the purchase arc $S \to Y_1$, the minimum total cost $F(B)$ is a **convex (unimodal) function of $B$**!

2. **Evaluating $F(B)$ in $O(N)$ Time via Two-Pointer Monotone Deque (FIFO Slow vs. LIFO Fast)**:
   For a fixed initial clean stock $B$ purchased at cost $B \cdot p$:
   - Sweep days $t = 1, 2, \dots, N$ in chronological order. On day $t$, after using $r_t$ napkins, push the batch $(t, r_t)$ of newly dirty napkins into a **waiting pool** $Q$.
   - To satisfy day $t$'s demand $r_t$:
     1. **Tier 0 (Free Initial Clean Stock $B$)**: Use any remaining initial clean stock from $B$ (cost $0$).
     2. **Tier 1 (Cheap Slow Laundry — FIFO from the Oldest Dirty Napkins)**: Any dirty batch $(s, \text{cnt})$ in $Q$ with $s \le t - d_{\text{slow}}$ is eligible for **both** slow and fast laundry. If we must use slow laundry ($c_{\text{slow}}$), which eligible dirty napkins should we consume? The **oldest** ones ($s$ smallest, **front of the deque / FIFO**), or doesn't it matter among $s \le t - d_{\text{slow}}$? Actually, once $s \le t - d_{\text{slow}}$, batch $s$ can reach day $t$ via slow laundry; consuming the oldest batch $s$ is optimal.
     3. **Tier 2 (Expensive Fast Laundry — LIFO from the Newest Eligible Dirty Napkins!)**: Suppose all batches with $s \le t - d_{\text{slow}}$ are exhausted, and we still have a deficit on day $t$. We must use **fast laundry** ($c_{\text{fast}}$) from batches $(s, \text{cnt})$ satisfying $t - d_{\text{slow}} < s \le t - d_{\text{fast}}$. Which batch $s$ in this window should we consume via fast laundry?
        - **Crucial Insight**: An **older** batch $s_1$ in $(t - d_{\text{slow}}, t - d_{\text{fast}}]$ will mature into the cheap slow-laundry window $s_1 \le t' - d_{\text{slow}}$ on an earlier future day $t' = s_1 + d_{\text{slow}}$ than a **newer** batch $s_2 > s_1$!
        - Therefore, to preserve older dirty napkins so they can become eligible for cheap slow laundry on future days, fast laundry must greedily consume the **most recent (newest / largest $s \le t - d_{\text{fast}}$)** dirty napkins first (**LIFO** from the back of the fast-eligible window)!
   - Thus a double-ended queue (deque) over the matured dirty batches evaluates $F(B)$ in $O(N)$ time, and **ternary search** over $B$ solves the entire problem in **$O(N \log(\sum r_t))$ time**!

---

### 4.3 Weighted $K$-Slot Caching & Interval Selection (`CF 802 C`, `POJ 3680`): Dual Compilations

#### Step 1: Non-Graph Diagnostic Signal (Recognition)
- **Surface Clues**:
  1. **Weighted $K$-Slot Caching (`CF 802 C — Heidi and Library`, Offline Weighted Belady)**: "A cache holds at most $K$ items. On day $t \in \{1, \dots, N\}$, item $a_t$ is requested. If $a_t$ is not in cache, we must buy/fetch it at cost $c_{a_t}$. Minimize total cost."
  2. **Maximum-Weight $K$-Overlap Interval Selection (`POJ 3680 — Intervals`)**: "Given $N$ weighted open intervals $(l_i, r_i)$ with weight $w_i > 0$, select a subset of intervals such that no point on the real line is covered by more than $K$ intervals."
- **Why Belady's Farthest-in-Future Greedy Fails on Weighted Caching**:
  When fetch costs $c_b$ are uniform ($c_b = 1$), Belady's greedy algorithm (evict the cached item whose next request is farthest in the future) is optimal. When $c_b$ varies, evicting an item with huge fetch cost $c_{\text{heavy}} = 10^9$ whose next request is at $t + 10$ in order to keep a cheap item $c_{\text{light}} = 1$ requested at $t + 2, t + 3$ is catastrophic if $10^9 > 2 \times 1$. There is a continuous tradeoff between **eviction duration** and **re-fetch cost**.

#### Step 2 & Step 3: Head-to-Head Comparison of Two Canonical $K$-Cache Graph Compilations (`Cohort 1 + Cohort 2 Synthesis`)

Let $\text{next}(t)$ be the next day $t' > t$ on which the same item $a_{t'} = a_t$ is requested (if none, no retention is ever needed after day $t$).

##### Compilation 1: Continuous Timeline Spine of Capacity $K - 1$ + Saving Chords (`POJ 3680` Dual View)
- **Baseline**: Assume we pay for **every** request upfront: $\text{BaseCost} = \sum_{t=1}^N c_{a_t}$.
- **Saving Variable $x_t \in \{0, 1\}$**: Set $x_t = 1$ if we **retain** item $a_t$ in cache across the open time interval $(t, \text{next}(t))$, which **saves** $c_{a_t}$ on day $\text{next}(t)$!
- **Capacity Constraint**: On any day $s$, the requested item $a_s$ occupies $1$ mandatory slot in the cache. Therefore, at most **$K - 1$ other items** can be retained in the background across day $s$:
  $$\sum_{t : t < s < \text{next}(t)} x_t \le K - 1 \qquad (\forall s \in \{1, \dots, N\}).$$
- **Graph Gadget ($N$ vertices, $2N$ arcs)**:
  - Build a horizontal timeline $1 \to 2 \to \dots \to N$ where each spine edge $s \to s+1$ has `(cap = K - 1, cost = 0)`.
  - For each day $t$ with $\text{next}(t) \le N$, add a **Saving Chord** $(t+1) \to \text{next}(t)$ with `(cap = 1, cost = -c_{a_t})` (if $t + 1 = \text{next}(t)$, $a_{t+1} = a_t$ is requested on the very next day, which occupies the mandatory slot on day $t+1$ and saves $c_{a_t}$ unconditionally with $0$ background cache load!).
  - Send $K - 1$ units of flow from $1$ to $N$: $\text{Ans} = \sum_{t=1}^N c_{a_t} + \text{MinCostFlow}(1 \to N, \text{flow} = K - 1)$.

##### Compilation 2: Split-Day Token Routing $t_{\text{in}} \to t_{\text{out}}$ with Lower-Bound Demand (`CF 802 C` Primal Token View)
Instead of subtracting savings from a baseline, track the **$K$ physical cache slots** directly as $K$ tokens flowing through split day nodes $t_{\text{in}}, t_{\text{out}}$:
- **Mandatory Request Satisfaction**: Day $t$ requires $a_t$ in cache, so the bridge $t_{\text{in}} \to t_{\text{out}}$ has lower bound $L = 1, U = 1$ (converted via standard demand substitution to $S \to t_{\text{out}}$ `(cap=1, cost=0)` and $t_{\text{in}} \to T$ `(cap=1, cost=0)`).
- **Buying / Fetching on Day $t$**: Arc $S_{\text{slots}} \to t_{\text{in}}$ `(cap = 1, cost = c_{a_t})`, where $S_{\text{slots}}$ receives `(cap = K, cost = 0)` from $S$ (or idle cache slots flow along $t_{\text{out}} \to (t+1)_{\text{in}}$).
- **Evicting on Day $t$ and Buying a New Book on Day $t+1$**: Arc $t_{\text{out}} \to (t+1)_{\text{in}}$ `(cap = 1, cost = c_{a_{t+1}})` (or idle spine $t_{\text{out}} \to (t+1)_{\text{out}}$ `(cap = K - 1, cost = 0)` plus fetch $t_{\text{out}} \to (t+1)_{\text{in}}$ `(cap = 1, cost = c_{a_{t+1}})`).
- **Retaining the Same Book Until $\text{next}(t)$ for Free**: Direct chord $t_{\text{out}} \to \text{next}(t)_{\text{in}}$ with **`(cap = 1, cost = 0)`**!

| Feature | Compilation 1 (Timeline Saving Chords) | Compilation 2 (Split-Day Token Routing) |
| :--- | :--- | :--- |
| **Vertices & Edges** | $N$ vertices, $2N$ arcs | $2N + 2$ vertices, $4N$ arcs |
| **Edge Costs** | Negative saving costs $-c_{a_t}$ on DAG (eliminated in $O(N)$ via topological potentials) | Strictly non-negative costs $+c_{a_t} \ge 0$ (or shifted $-M$ on $t_{\text{in}} \to t_{\text{out}}$) |
| **Best Use Case** | Fastest implementation; unifies directly with `POJ 3680` $K$-interval selection | Best when transitions between consecutive days have state-dependent reconfiguration costs |

---

## 5. Iteration 34 / 86 Reconciled: 2D Prefix/Suffix Coordinate Rank & Order-Statistic Slot Assignment (`AtCoder AGC 031 E — Snuke the Phantom Thief`)

### 5.1 Fixed-Cardinality $K$ Order-Statistic Translation & Interval Monotonization Recurrences

#### Step 1: Non-Graph Diagnostic Signal (Recognition)
- **Surface Clues**:
  1. "Select a subset of items in the 2D plane $(x_i, y_i)$ with value $v_i > 0$ to maximize total value."
  2. "Subject to $M$ directional prefix/suffix count constraints of the form: *at most $b_m$ selected items have coordinate $x_i \le a_m$* (`L`), *at most $b_m$ have $x_i \ge a_m$* (`R`), *at most $b_m$ have $y_i \le a_m$* (`D`), and *at most $b_m$ have $y_i \ge a_m$* (`U`)."
- **Why Standard 2D Range-Tree / Quadtree Flow Fails**:
  In general 2D rectangle packing, a single point $(x_i, y_i)$ can belong to an arbitrary set of overlapping half-planes; intersecting $X$-half-planes and $Y$-half-planes directly creates a hypergraph whose incidence matrix is not Totally Unimodular.
- **Why Subset / Sweep-Line DP Fails**:
  Simultaneously tracking how many items have been chosen below every active $X$-threshold *and* every active $Y$-threshold requires exponential state space.

#### Step 2: Intermediate Algebraic Representation (Order-Statistic Equivalence)
The breakthrough insight of `AGC 031 E` is to **fix the total number of chosen items $K \in \{1, 2, \dots, N\}$ in an outer loop**, and sort the $K$ chosen items twice:
- Let $x_{(1)} \le x_{(2)} \le \dots \le x_{(K)}$ be the $X$-coordinates of the $K$ chosen items sorted in non-decreasing order.
- Let $y_{(1)} \le y_{(2)} \le \dots \le y_{(K)}$ be the $Y$-coordinates of the $K$ chosen items sorted in non-decreasing order.

Now translate every directional half-plane constraint into a **pointwise bound on a specific order-statistic slot $p \in \{1, \dots, K\}$**:
1. **Type `L` ("At most $b_m$ chosen items have $x \le a_m$")**:
   $$\text{Count}(x \le a_m) \le b_m \iff \text{The } (b_m + 1)\text{-th smallest } X\text{-coordinate satisfies } x_{(b_m + 1)} \ge a_m + 1 \quad (\text{if } b_m + 1 \le K).$$
2. **Type `R` ("At most $b_m$ chosen items have $x \ge a_m$")**:
   Since the total number of chosen items is **fixed at $K$**, having at most $b_m$ items in $[a_m, \infty)$ is equivalent to having at least $K - b_m$ items in $(-\infty, a_m - 1]$:
   $$\text{Count}(x \ge a_m) \le b_m \iff \text{The } (K - b_m)\text{-th smallest } X\text{-coordinate satisfies } x_{(K - b_m)} \le a_m - 1 \quad (\text{if } K - b_m \ge 1).$$
3. **Types `D` and `U` on $Y$-coordinates**:
   By the exact same logic, `D` ($a_m, b_m$) forces $y_{(b_m + 1)} \ge a_m + 1$, and `U` ($a_m, b_m$) forces $y_{(K - b_m)} \le a_m - 1$.

#### Interval Monotonization Recurrences (`Cohort 2 Explicit Synthesis`)
Because $x_{(1)} \le x_{(2)} \le \dots \le x_{(K)}$ and $y_{(1)} \le \dots \le y_{(K)}$, any lower bound on slot $p-1$ automatically applies to slot $p$, and any upper bound on slot $p+1$ automatically applies to slot $p$. Before constructing the graph for a fixed $K$, we propagate the bounds to form **monotone intervals** $[L_X(p), R_X(p)]$ and $[L_Y(q), R_Y(q)]$:
$$L_X(p) = \max\!\Big(\{1\} \cup \{L_X(p-1)\} \cup \{a_m + 1 : \text{type}_m = \text{'L'},\; b_m + 1 = p\}\Big) \quad (p = 1 \dots K),$$
$$R_X(p) = \min\!\Big(\{\infty\} \cup \{R_X(p+1)\} \cup \{a_m - 1 : \text{type}_m = \text{'R'},\; K - b_m = p\}\Big) \quad (p = K \dots 1),$$
and identically for $L_Y(q)$ and $R_Y(q)$. This guarantees the **Monotone Interval Property**:
$$L_X(1) \le L_X(2) \le \dots \le L_X(K), \qquad R_X(1) \le R_X(2) \le \dots \le R_X(K).$$
(If $L_X(p) > R_X(p)$ or $L_Y(q) > R_Y(q)$ for any slot, cardinality $K$ is immediately infeasible!)

---

### 5.2 4-Layer MCMF Compilation & Proof of the Monotone Interval Uncrossing Theorem

#### Step 3: Reverse-Engineering Scratchpad (4-Layer Bipartite Slot-to-Jewel-to-Slot Graph)
For a fixed $K \in \{1, \dots, N\}$, a jewel $i$ is selected if and only if it is assigned to **one $X$-rank slot $p \in \{1, \dots, K\}$** (such that $x_i \in [L_X(p), R_X(p)]$) AND **one $Y$-rank slot $q \in \{1, \dots, K\}$** (such that $y_i \in [L_Y(q), R_Y(q)]$), with each jewel used at most once:

```
  Layer 1: X-Rank Slots       Layer 2: Jewel_in         Layer 3: Jewel_out        Layer 4: Y-Rank Slots
  
  [S] --(1, 0)--> [ X_1 ] --(1, 0 if x_i in I_1)--> [ i_in ] --(1, -v_i)--> [ i_out ] --(1, 0 if y_i in J_1)--> [ Y_1 ] --(1, 0)--> [T]
  [S] --(1, 0)--> [ X_2 ] --(1, 0 if x_i in I_2)--> [ i_in ] --(1, -v_i)--> [ i_out ] --(1, 0 if y_i in J_2)--> [ Y_2 ] --(1, 0)--> [T]
        ...                                               ...                                                          ...
  [S] --(1, 0)--> [ X_K ] --(1, 0 if x_i in I_K)--> [ i_in ] --(1, -v_i)--> [ i_out ] --(1, 0 if y_i in J_K)--> [ Y_K ] --(1, 0)--> [T]
```

> [!IMPORTANT]
> **Theorem 5.1 (The Monotone Interval Uncrossing Theorem)**
> The 4-layer MCMF graph above enforces $x_{\pi(p)} \in [L_X(p), R_X(p)]$ for each $p$, **without** explicitly enforcing that the jewel $\pi(1)$ assigned to $X_1$ has a smaller $X$-coordinate than the jewel $\pi(2)$ assigned to $X_2$ ($x_{\pi(1)} \le x_{\pi(2)} \le \dots \le x_{\pi(K)}$). Why doesn't an inverted assignment $x_{\pi(1)} > x_{\pi(2)}$ violate the original `L/R` constraints?
>
> *Proof*:
> Suppose an integral flow of size $K$ assigns jewel $i_1$ to $X_{p_1}$ and jewel $i_2$ to $X_{p_2}$ with slot indices $p_1 < p_2$, but their coordinates are inverted: $x_{i_1} > x_{i_2}$.
> 1. Since the flow uses edges $X_{p_1} \to i_1$ and $X_{p_2} \to i_2$, we have:
>    $$L_X(p_1) \le x_{i_1} \le R_X(p_1) \quad \text{and} \quad L_X(p_2) \le x_{i_2} \le R_X(p_2).$$
> 2. By the Monotone Interval Property ($p_1 < p_2 \implies L_X(p_1) \le L_X(p_2)$ and $R_X(p_1) \le R_X(p_2)$) combined with our assumption $x_{i_2} < x_{i_1}$:
>    $$L_X(p_1) \le L_X(p_2) \le x_{i_2} < x_{i_1} \le R_X(p_1) \implies x_{i_2} \in [L_X(p_1), R_X(p_1)],$$
>    $$L_X(p_2) \le x_{i_2} < x_{i_1} \le R_X(p_1) \le R_X(p_2) \implies x_{i_1} \in [L_X(p_2), R_X(p_2)].$$
> 3. Therefore, **both cross-edges $X_{p_1} \to i_2$ and $X_{p_2} \to i_1$ also exist in the network with cost $0$**! Swapping the slot assignments of $i_1$ and $i_2$ on the $X$-side preserves feasibility and leaves the set of chosen jewels (and total value) completely unchanged. Repeating this bubble-sort swap eliminates all inversions on both the $X$-side and $Y$-side, proving that **a $K$-subset of jewels can be matched in the 4-layer network if and only if its true sorted order statistics satisfy all `L/R/D/U` constraints**!

### 5.3 Hand-Checkable Toy Trace & Partial-Flow Invalidation Counterexamples
- **Numerical Uncrossing Trace ($K = 2$)**:
  - Jewels: $J_1 = (x=4, y=2, v=10)$, $J_2 = (x=6, y=5, v=20)$.
  - Constraints for $K = 2$:
    - `L`: $a_1 = 3, b_1 = 0 \implies x_{(1)} \ge 4 \implies [L_X(1), R_X(1)] = [4, \infty), [L_X(2), R_X(2)] = [4, \infty)$.
    - `R`: $a_2 = 5, b_2 = 1 \implies x_{(2-1)} = x_{(1)} \le 4 \implies [L_X(1), R_X(1)] = [4, 4], [L_X(2), R_X(2)] = [4, \infty)$.
  - Here $J_1 (x=4) \in [4, 4]$ matches $X_1$, and $J_2 (x=6) \in [4, \infty)$ matches $X_2$. Both jewels are selected for total value $30$.
- **Broken Gadget Counterexample 1: Accepting a Partial Flow $f < K$ (`Cohort 2 Audit`)**:
  Suppose for trial $K = 3$ there is a constraint `R` with $a = 5, b = 1$ ("at most $1$ jewel has $x \ge 5$"). For $K = 3$, this translates to $x_{(3 - 1)} = x_{(2)} \le 4$ (at least $2$ jewels have $x \le 4$).
  - If only $1$ jewel in the input has $x \le 4$ and $1$ jewel has $x = 10$, then for $K = 3$ the network can push at most $f = 2$ units of flow (matching $x \le 4$ to $X_1$ and $x = 10$ to $X_3$, leaving $X_2$ unmatched!).
  - If you foolishly record the cost of this partial flow $f = 2$ during the $K = 3$ run, you have accepted a 2-jewel subset using the **wrong rank slot $X_3$**! For $K$ fixed, the translation $K - b_m$ is valid **if and only if the maximum flow reaches exactly $f = K$**; if $f < K$, the trial $K$ must be discarded completely.
- **Broken Gadget Counterexample 2: Omitting the Monotonization Pass**:
  Suppose `L` gives $x_{(1)} \ge 10$ ($b_1 = 0, a_1 = 9$) and no constraint explicitly mentions $x_{(2)}$. Without propagating $L_X(2) = \max(L_X(2), L_X(1)) = 10$, interval $I_2^x$ remains $[1, \infty)$, allowing a jewel with $x = 3$ to match to $X_2$ while a jewel with $x = 12$ matches to $X_1$, violating `L`!

---

## 6. Iteration 35 / 87 Reconciled: Absolute-Value, Manhattan ($\ell_1^d$) & Chebyshev ($\ell_\infty^d$) Hub Linearization (`AtCoder AGC 034 D — Manhattan Max Matching`)

### 6.1 Dual-Norm Sign Linearization: $2^d$ Hubs for Manhattan ($\ell_1^d$) vs. $2d$ Hubs for Chebyshev ($\ell_\infty^d$)

#### Step 1: Non-Graph Diagnostic Signal (Recognition)
- **Surface Clues**:
  1. "Match $N$ red points (or clusters of supply $a_i$) with $N$ blue points (demand $b_j$) in $\mathbb{R}^d$ ($d$ small, e.g., $d \in \{1, 2, 3, 4\}$) to **maximize** total Manhattan ($\ell_1^d$) or Chebyshev ($\ell_\infty^d$) distance."
  2. Constraints $N \le 1,000$ to $5,000$, where explicit complete bipartite matching has $O(N^2)$ edges ($10^6$ to $2.5 \times 10^7$ arcs) and TLEs under MCMF.
- **Why Complete Bipartite Graph Construction Fails**:
  The distance $|x_i - x_j| + |y_i - y_j|$ couples $(x_i, y_i)$ and $(x_j, y_j)$ non-linearly via $|\cdot|$. However, under **maximization**, both the $\ell_1^d$ norm and the $\ell_\infty^d$ norm are **pointwise maxima of $O(1)$ linear functions**!

#### Step 2: Intermediate Algebraic Representation ($\ell_1^d$ vs. $\ell_\infty^d$ Dual Linearization)

1. **Manhattan ($\ell_1^d$) Norm — Pointwise Maximum over $2^d$ Sign Vectors $\sigma \in \{-1, +1\}^d$**:
   $$\lVert p - q \rVert_1 = \sum_{k=1}^d |p_k - q_k| = \max_{\sigma \in \{-1, +1\}^d} \sum_{k=1}^d \sigma_k (p_k - q_k) = \max_{\sigma \in \{-1, +1\}^d} \left[ \underbrace{\left(\sum_{k=1}^d \sigma_k p_k\right)}_{\text{Red Point Term}} + \underbrace{\left(\sum_{k=1}^d (-\sigma_k) q_k\right)}_{\text{Blue Point Term}} \right].$$
   For $d = 2$ (`AGC 034 D`), there are $2^2 = 4$ sign vectors $\sigma = (s_1, s_2) \in \{ (+1,+1), (+1,-1), (-1,+1), (-1,-1) \}$.

2. **Chebyshev ($\ell_\infty^d$) Norm — Pointwise Maximum over Only $2d$ Signed Axes (`Cohort 2 Generalization`)**:
   $$\lVert p - q \rVert_\infty = \max_{1 \le k \le d} |p_k - q_k| = \max_{\substack{1 \le k \le d \\ s \in \{-1, +1\}}} \Big[ \underbrace{(s \cdot p_k)}_{\text{Red Point Term}} + \underbrace{(-s \cdot q_k)}_{\text{Blue Point Term}} \Big].$$
   Notice the dramatic scaling difference in high dimensions:
   - $\ell_1^d$ requires **$2^d$ hubs** (each hub combines *all* $d$ coordinates with signs $\sigma \in \{\pm 1\}^d$).
   - $\ell_\infty^d$ requires **only $2d$ hubs** $H_{k, s}$ for $k \in \{1, \dots, d\}$ and $s \in \{-1, +1\}$ (each hub isolates a *single* coordinate axis $k$ and sign $s$)!
   - In $d = 2$, $2^2 = 2 \cdot 2 = 4$ because the $45^\circ$ rotation $(u, v) = (x+y, x-y)$ is an isomorphism between $\ell_1^2$ and $\ell_\infty^2$. For $d \ge 3$, $2^d > 2d$ (e.g., for $d = 10$, $\ell_\infty^{10}$ needs only $20$ hubs whereas $\ell_1^{10}$ needs $1,024$ hubs!).

---

### 6.2 Mechanical Graph Compilation, Minimization Failure Proof & Synthesis with Lazy Convex Degree Penalties

#### Step 3: Reverse-Engineering Scratchpad (Hub Sparsification Topology)
Because the objective **maximizes** distance (or minimizes negative distance), replacing $|p - q|$ with a choice among the hub relays $H_\sigma$ is **exact**: for any matched pair $(i, j)$, the max-cost flow solver will always route the unit of flow from $R_i$ to $B_j$ through whichever hub $H_{\sigma^*}$ achieves the maximum $\sum_k \sigma_k (p_{i,k} - q_{j,k}) = \|p_i - q_j\|_1$!

```
                                   +---> [ Hub H_{+,+} ] --- (cap inf, cost -x'_j - y'_j) ---+
                                   |     (cost +x_i + y_i)                                   |
                                   +---> [ Hub H_{+,-} ] --- (cap inf, cost -x'_j + y'_j) ---+
                                   |     (cost +x_i - y_i)                                   v
  [S] --(cap c_i, cost 0)--> [R_i] +---> [ Hub H_{-,+} ] --- (cap inf, cost +x'_j - y'_j) -> [B_j] --(cap d_j, cost 0)--> [T]
                                   |     (cost -x_i + y_i)                                   ^
                                   +---> [ Hub H_{-,-} ] --- (cap inf, cost +x'_j + y'_j) ---+
                                         (cost -x_i - y_i)
```

- **Graph Size Reduction**: Instead of $N^2 = 10^6$ edges, the graph has $2N + 2^d$ vertices (for $\ell_1^d$) or $2N + 2d$ vertices (for $\ell_\infty^d$) and only $2 \cdot 2^d N$ (or $4dN$) edges!
- **Wait—Can Different Flow Units Cross at the Same Hub $H_\sigma$?**
  Suppose red point $R_1$ sends $1$ unit to $H_{+,+}$ and $R_2$ sends $1$ unit to $H_{+,+}$, which then exit to $B_1$ and $B_2$. Because the hub cost decomposes additively into $(+x_i + y_i) + (-x'_j - y'_j)$, it does not matter whether $R_1$ pairs with $B_1$ or $B_2$ inside $H_{+,+}$—both pairings have the exact same sum of linear hub costs!

#### Step 4: Hand-Checkable Toy Trace & Why Minimization Fails Catastrophically
- **Numerical Trace ($N = 1$ pair)**:
  - $R_1 = (1, 5)$, $B_1 = (4, 1)$. True Manhattan distance $= |1 - 4| + |5 - 1| = 3 + 4 = 7$.
  - Costs of $R_1 \to H_{s_1, s_2} \to B_1$ across the $4$ hubs:
    1. $H_{+,+}$: $(1 + 5) + (-4 - 1) = +1$.
    2. $H_{+,-}$: $(1 - 5) + (-4 + 1) = -7$.
    3. $H_{-,+}$: $(-1 + 5) + (4 - 1) = +7$ (**Maximum!**).
    4. $H_{-,-}$: $(-1 - 5) + (4 + 1) = -1$.
  - Max-cost flow routes $R_1 \to H_{-,+} \to B_1$ and achieves $+7$.
- **Broken Gadget Counterexample: Why Hub Linearization FAILS for Min-Cost Manhattan Matching**:
  Suppose we want to **minimize** $\sum \|p_i - q_j\|_1$ and run **Min-Cost** Max-Flow on the exact same 4-hub network.
  - In the toy trace above, Min-Cost Max-Flow does NOT pick $+7$; it picks $H_{+,-}$ of cost **$-7 = -\|R_1 - B_1\|_1$**!
  - Why? Because $\min_{\sigma \in \{\pm 1\}^d} \langle \sigma, p - q \rangle = -\max_{\sigma} \langle \sigma, p - q \rangle = -\|p - q\|_1$.
  -To minimize $\|p - q\|_1 = \max_\sigma \langle \sigma, p - q \rangle$, a single unit of flow would have to satisfy $z_{i,j} \ge \langle \sigma, p_i - q_j \rangle$ **simultaneously for all $2^d$ sign vectors $\sigma$**, which cannot be represented by choosing a single path through one hub! (Min-cost geometric matching requires geometric data structures / K-D trees / planar separators, not sign hubs.)

---

## 7. Cohort 3 Targeted Gap-Hunting & Reconciled Master Recognition/Compilation Decision Table

### 7.1 Gap-Hunt 1: Matroid Intersection vs. Bipartite MCMF with Partition/Rank Constraints (`AGC 031 E` in 2D vs. 3D NP-Hardness)

Why does the 4-layer order-statistic MCMF compilation of `AGC 031 E` (Section 5) work in **2D** (`L, R, D, U` constraints on $(x_i, y_i)$), and what happens if we add a **3rd coordinate $z_i$** with Front/Back (`F, B`) constraints?

> [!IMPORTANT]
> **Theorem 7.1 (The 2-Matroid vs. 3-Matroid Intersection Boundary in Coordinate-Rank Selection)**
> For a fixed subset cardinality $K$:
> 1. **Each Coordinate Axis Defines a Transversal / Laminar Matroid**:
>    On the $X$-axis alone, a subset $S \subseteq \{1, \dots, N\}$ of size $|S| = K$ satisfies all `L` and `R` prefix/suffix constraints if and only if $S$ has a perfect matching to the $K$ monotone intervals $I_1^x, \dots, I_K^x$ in the bipartite graph $G_X = (S, \{X_1, \dots, X_K\})$. By Rado's / Edmonds's theorem, the family of subsets matchable in $G_X$ is the set of bases of a **Transversal Matroid $\mathcal{M}_X$** (in fact, because the intervals $[L_X(p), R_X(p)]$ are monotone, $\mathcal{M}_X$ is a **Laminar Matroid / Generalized Partition Matroid** over the 1D chain of $X$-coordinates!).
> 2. **Why 2D (`L/R/D/U`) Compiles to 4-Layer MCMF**:
>    In 2D, selecting a maximum-weight subset $S$ of size $K$ satisfying both $X$-rank and $Y$-rank constraints is precisely the **Weighted 2-Matroid Intersection Problem** on $\mathcal{M}_X \cap \mathcal{M}_Y$:
>    $$\max_{S \subseteq \{1, \dots, N\},\; |S| = K} \left\{ \sum_{i \in S} v_i \;:\; S \in \mathcal{B}(\mathcal{M}_X) \cap \mathcal{B}(\mathcal{M}_Y) \right\}.$$
>    Because $\mathcal{M}_X$ sits on the left of the split jewel nodes $(i_{\text{in}} \to i_{\text{out}})$ and $\mathcal{M}_Y$ sits on the right, the two bipartite matching polytopes are glued in series:
>    $$S \to \text{Slots}_X \to \text{Jewel}_{\text{in}} \xrightarrow{-v_i} \text{Jewel}_{\text{out}} \to \text{Slots}_Y \to T.$$
>    Since the series concatenation of two bipartite/network-flow matrices remains a standard single-commodity network flow matrix (Totally Unimodular!), **Weighted 2-Matroid Intersection of two transversal/laminar matroids compiles directly into a single 4-layer MCMF network!**
> 3. **Why 3D (`L/R/D/U/F/B`) Fails & Becomes NP-Hard**:
>    If each jewel has 3 coordinates $(x_i, y_i, z_i)$ with prefix/suffix constraints along all three axes, feasible subsets of size $K$ must lie in the **3-Matroid Intersection** $\mathcal{B}(\mathcal{M}_X) \cap \mathcal{B}(\mathcal{M}_Y) \cap \mathcal{B}(\mathcal{M}_Z)$.
>    - Topologically, a flow token can enter $i_{\text{in}}$ from **one** matroid ($\mathcal{M}_X$) and exit $i_{\text{out}}$ into **one** matroid ($\mathcal{M}_Y$). There is **no third port** on a single-commodity flow vertex $i$ to require that the *same* jewel $i$ is simultaneously matched to a unique $Z$-slot $Z_r \in \mathcal{M}_Z$ without splitting or cloning the flow!
>    - Algebraically, the intersection of 3 partition/transversal matroids includes **3-Dimensional Matching (3DM)** as a special case (where $L_X(p)=R_X(p)=p$, $L_Y(q)=R_Y(q)=q$, $L_Z(r)=R_Z(r)=r$), which is **strongly NP-hard**!

---

### 7.2 Gap-Hunt 2: When Do Cycle Covers Decompose Cleanly into Independent Trees + Cycles?

A major subtlety across contest problems (`Luogu P2469 星际竞速`, `ICPC WF 2015 Catering`, `CF 1510 B Button Lock`, `CF 387 D George and Interesting Graph`) is knowing **when** the bipartite $V_{\text{out}} \to V_{\text{in}}$ relaxation is exact versus when closed subtours corrupt the answer:

| Graph & Objective Regime | Does $V_{\text{out}} \to V_{\text{in}}$ Produce Spurious Subtours? | Exact Resolution & Contest Archetype |
| :--- | :--- | :--- |
| **1. Underlying Graph is a DAG** (`星际竞速`, `Catering`, `营救皮卡丘`, `CF 1510 B Button Lock`) | **Never.** A DAG has no directed cycles, so every subgraph with $d^+(u) \le 1, d^-(v) \le 1$ is a collection of vertex-disjoint open directed paths! | **100% Exact via Bipartite Flow/MCMF.** In `CF 1510 B` (Button Lock), transitions $u \to v$ only go from strictly smaller bitmasks $u \subsetneq v$ (a DAG!), and pressing `R` (reset to $0$) is simply ending a path at $u_{\text{out}} \to T$ and starting a new path from $0$. |
| **2. Objective Explicitly Seeks a Permutation / Vertex-Disjoint Cycle Cover** (`CF 387 D George and Interesting Graph`, Weighted Cycle Cover) | **Exact by Definition.** Every vertex must have $d^+(v) = d^-(v) = 1$ in the chosen subgraph. | **100% Exact via Bipartite Matching / MCMF.** In `CF 387 D`, after fixing the universal center vertex $c$ ($O(N)$ choices), the remaining $N-1$ vertices must each have $d^+(v) = d^-(v) = 1$, which is a minimum-edit bipartite matching on $V \setminus \{c\}$! |
| **3. Functional Graph ($d^+(u) = 1$) Rewiring to a Single Cycle / Arborescence** | **Yes**, if edge costs are arbitrary and a single connected component is required. | Must break each disjoint cycle and splice them together (Minimum Cost Arborescence / Chu–Liu–Edmonds algorithm in $O(NM)$ or $O(M \log N)$), **not** bipartite matching! |
| **4. General Cyclic Graph Where We Need $\le K$ Open Paths / Single TSP Tour** | **Fails (NP-Hard).** Bipartite matching greedily forms cheap disconnected short cycles instead of paying for bridges between components. | Requires Held–Karp $O(2^N N^2)$ DP, Subtour Elimination LP, or SCC condensation (`ABC 214 H`) if traversing an entire SCC is free. |

---

### 7.3 Reconciled Master Recognition & Compilation Decision Table

| Diagnostic Signal in Problem Statement | Algebraic Intermediate Form | Compiled MCMF Gadget | Complexity / Scaling Upgrade |
| :--- | :--- | :--- | :--- |
| **$k$ disjoint shortest paths / collect-once grid walks** | $y_u = y_u^{(1)} + y_u^{(2)}$, $y_u^{(1)} \in [0,1]$, $y_u^{(2)} \in [0, k-1]$ | Split $u_{\text{in}} \to u_{\text{out}}$ into `(1, -w_u)` $\oplus$ `(k-1, 0)` | SCC Condensation (`ABC 214 H`) or 2D Hasse Pruning (`吃豆豆`) |
| **Bounded-fleet ($\le K$) DAG path cover** | $s_v + \sum_u x_{u,v} = 1$, $\sum_v s_v \le K$ | Starter hub $S \xrightarrow{(K, 0)} H_{\text{start}} \xrightarrow{(1, c_v)} v_{\text{in}}$ + $u_{\text{out}} \to v_{\text{in}}$ | Restricted Floyd–Warshall $d^{(\le \max(u,v))}$ if precedence-locked (`营救皮卡丘`) |
| **Minimize total completion time $\sum C_i$ on $M$ machines** | $\sum_{j, r} r \cdot t_{\pi(j,r), j}$ (reverse rank $r$ from end) | Lazy frontier slot $(j, r_j)$: spawn $(j, r_j+1)$ **immediately** when $(j, r_j) \to T$ saturates | $O(N + M + P)$ vertices (`[NOI2012] 美食节`); single-unit push mandatory! |
| **Consumable resource with multi-speed delayed reuse** | $f(t_{\text{in}} \to t_{\text{out}}) = r_t \iff S \to X_t$ and $Y_t \to T$ | Morning/Evening split: $S \xrightarrow{(r_t, 0)} X_t \xrightarrow{(\infty, c_k)} Y_{t+d_k} \xrightarrow{(r_t, 0)} T$ | For $N \le 2 \times 10^5$ (`[BJWC2018]`): Ternary search on fresh $B$ + FIFO/LIFO deques |
| **Weighted $K$-slot cache / $K$-overlap intervals** | $\sum_{t < s < \text{next}(t)} x_t \le K - 1$ | Spine $s \to s+1$ `(K-1, 0)` + Saving chord $(t+1) \to \text{next}(t)$ `(1, -c_{a_t})` | Initialize potentials $\pi$ on the DAG in $O(N)$ before running Dijkstra |
| **2D `L/R/D/U` prefix/suffix coordinate bounds** | Fixed $|S|=K$: $x_{(b+1)} \ge a+1$, $x_{(K-b)} \le a-1$ | Monotonize $[L_X(p), R_X(p)]$; 4-layer graph $X_p \to i_{\text{in}} \to i_{\text{out}} \to Y_q$ | Works in 2D (2-Matroid Intersection); NP-hard in 3D (3-Matroid Intersection) |
| **Max-weight $\ell_1^d$ or $\ell_\infty^d$ matching** | $\|p-q\|_1 = \max_{\sigma \in \{\pm 1\}^d} \langle \sigma, p-q \rangle$; $\|p-q\|_\infty = \max_{k, s} s(p_k - q_k)$ | **$2^d$ sign hubs** $H_\sigma$ for $\ell_1^d$; **$2d$ axis-sign hubs** $H_{k,s}$ for $\ell_\infty^d$ | Valid **only for maximization**; combines cleanly with lazy convex degree arcs |

---

## 8. Reconciled Master 4-Tier Curated Problem Bank (30 Non-Template Problems)

Every problem from Cohort 1 (22 problems) and Cohort 2 (22 problems) has been audited, deduplicated, and synthesized into this 30-problem master bank across four difficulty tiers. Every problem includes its exact judge coordinates, constraints, 4-step compilation scratchpad, failure modes, and 3-tier progressive hints.

---

### 8.1 Tier 1: `Stepping Stone` (`P01` – `P07`)

---

#### P01 — Collect-Once Multi-Walker Grid (`Luogu P2045 方格取数加强版` / `POJ 3422 Kaka's Matrix Travels` / `Luogu P1006 传纸条`)
- **Judge URL**: [Luogu P2045](https://www.luogu.com.cn/problem/P2045) / [POJ 3422](http://poj.org/problem?id=3422) / [Luogu P1006](https://www.luogu.com.cn/problem/P1006)
- **Constraints**: Grid size $N \times N$ with $N \le 50$, walker count $K \le 10$, cell rewards $w_{i,j} \in [0, 1000]$.
- **Step 1 — Diagnostic Signal & Failure of Naive DP/Greedy**:
  - **Signal**: $K$ monotone walkers move from $(1,1)$ to $(N,N)$ moving only right or down. Each cell's reward $w_{i,j}$ can be harvested **at most once** even if multiple walkers traverse it.
  - **Why Multi-Walker DP Fails**: Tracking $K$ walkers at step $s = i + j$ requires $O(N^{K+1})$ states, which blows up for $K > 3$. Greedy single-walker extraction ($K$ passes of 2D DP) fails because Walker 1 can cut diagonally across the grid, severing high-value corridors for Walkers $2 \dots K$ unless paths can uncross via residual arcs.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Let $y_{i,j} \in \{0, 1, \dots, K\}$ be the number of walkers passing through cell $(i,j)$. The reward $w_{i,j} \min(y_{i,j}, 1)$ is concave in $y_{i,j}$ (cost $-w_{i,j} \min(y_{i,j}, 1)$ is convex).
  - Decompose $y_{i,j} = y_{i,j}^{(1)} + y_{i,j}^{(2)}$ with $y_{i,j}^{(1)} \in [0, 1]$ (cost $-w_{i,j}$) and $y_{i,j}^{(2)} \in [0, K-1]$ (cost $0$).
  - **Compiled Graph ($2N^2 + 2$ vertices, $\approx 6N^2$ arcs)**:
    1. Split each cell $(i,j)$ into $(i,j)_{\text{in}}$ and $(i,j)_{\text{out}}$.
    2. Add two parallel internal bridges $(i,j)_{\text{in}} \to (i,j)_{\text{out}}$:
       - **Harvest Bridge**: `(cap = 1, cost = -w_{i,j})`
       - **Transit Bypass Bridge**: `(cap = K - 1, cost = 0)`
    3. Grid transitions: $(i,j)_{\text{out}} \to (i+1, j)_{\text{in}}$ and $(i,j)_{\text{out}} \to (i, j+1)_{\text{in}}$ with `(cap = K, cost = 0)`.
    4. Source/Sink: $S \to (1,1)_{\text{in}}$ `(cap = K, cost = 0)` and $(N,N)_{\text{out}} \to T$ `(cap = K, cost = 0)`.
  - Run SSP for $K$ units of flow; since the grid is a DAG, initialize Johnson potentials in $O(N^2)$ via 2D DP and run $K$ Dijkstra passes in $O(K N^2 \log N)$ time.
- **Step 4 — Broken Gadget Trap & Progressive Hints**:
  - *Trap*: For `Luogu P1006 传纸条` (strictly internal vertex-disjoint 2-paths), the transit bypass arc `(cap = K-1, cost = 0)` must be **removed** on all internal cells $(i,j) \notin \{(1,1), (N,N)\}$ so that $y_{i,j} \le 1$.
  - **Hint 1**: How do you express the function $f(y) = -w \cdot \min(y, 1)$ for $y \in \{0, \dots, K\}$ as the sum of independent bounded edge flows?
  - **Hint 2**: Split each grid cell into `in` and `out` connected by two parallel edges of capacities $1$ and $K-1$.
  - **Hint 3**: Because all edges move $(i,j) \to (i+1,j)$ or $(i,j+1)$, the graph is a DAG; compute initial shortest paths via DP in $O(N^2)$ so all subsequent augmentations use Dijkstra.

---

#### P02 — Maximum Internally Vertex-Disjoint Shortest Paths (`Luogu P2153 [SDOI2009] 晨跑`)
- **Judge URL**: [Luogu P2153](https://www.luogu.com.cn/problem/P2153)
- **Constraints**: $N \le 200$ intersections, $M \le 2 \times 10^4$ directed streets with lengths $w_e \ge 0$.
- **Step 1 — Diagnostic Signal & Failure of Naive Greedy**:
  - **Signal**: Maximize the number of days (paths from $1$ to $N$) such that no intermediate intersection $v \in \{2, \dots, N-1\}$ and no directed street $e$ is ever visited more than once, and subject to maximum path count, minimize total distance.
  - **Why Greedy Fails**: Extracting the shortest path $P_1$ and deleting its intermediate vertices can cut a critical vertex separator, reducing the total number of disjoint paths below the true Menger vertex-cut capacity.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Internal vertex-disjointness enforces $\sum_{e \in \delta^-(v)} x_e \le 1$ for $v \in \{2, \dots, N-1\}$.
  - **Compiled Graph ($2N$ vertices, $M + N$ arcs)**:
    1. Split every $v \in \{2, \dots, N-1\}$ into $v_{\text{in}} \to v_{\text{out}}$ with `(cap = 1, cost = 0)`. For endpoints $v \in \{1, N\}$, set $v_{\text{in}} \to v_{\text{out}}$ `(cap = \infty, cost = 0)`.
    2. Each directed street $(u, v)$ of length $w$ becomes $u_{\text{out}} \to v_{\text{in}}$ with `(cap = 1, cost = w)`.
    3. Run standard MCMF from $1_{\text{out}}$ to $N_{\text{in}}$; the max flow $F$ is the maximum number of days, and the min cost $C$ is the minimum total running distance.
- **Step 4 — Broken Gadget Trap & Progressive Hints**:
  - *Trap*: Giving $1_{\text{in}} \to 1_{\text{out}}$ or $N_{\text{in}} \to N_{\text{out}}$ capacity $1$ restricts the runner to only $1$ day total! Endpoints must have capacity $\infty$.
  - **Hint 1**: This is the textbook combination of Menger's Vertex-Connectivity Theorem and Suurballe's algorithm.
  - **Hint 2**: How do you turn a capacity constraint on a vertex into a capacity constraint on a directed edge?
  - **Hint 3**: Split each internal vertex $v \notin \{1, N\}$ into $v_{\text{in}} \to v_{\text{out}}$ of capacity $1$ and cost $0$, and route all streets $u_{\text{out}} \to v_{\text{in}}$.

---

#### P03 — Suurballe's Edge-Disjoint Round Trip (`UVa 10806` / `POJ 2135 Dijkstra, Dijkstra.`)
- **Judge URL**: [POJ 2135](http://poj.org/problem?id=2135) / [UVa 10806](https://onlinejudge.org/external/108/10806.pdf)
- **Constraints**: $N \le 1,000$ vertices, $M \le 10,000$ undirected weighted edges $w_e > 0$.
- **Step 1 — Diagnostic Signal & Failure of Sequential Shortest Paths**:
  - **Signal**: Find a shortest path from $1$ to $N$ and a return path from $N$ to $1$ in an undirected graph using no undirected edge twice.
  - **Why Sequential Dijkstra Fails**: Running Dijkstra from $1 \to N$, deleting the path edges, and running Dijkstra from $N \to 1$ fails on any interlacing bridge graph where the unique pair of disjoint paths must avoid a central shortcut.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Since the graph is undirected, a round trip $1 \leadsto N \leadsto 1$ using edge-disjoint undirected edges is equivalent to **two edge-disjoint directed paths from $1$ to $N$**!
  - **Compiled Graph ($N + 2$ vertices, $2M + 2$ arcs)**:
    1. Replace each undirected edge $\{u, v\}$ of weight $w$ with two directed arcs $u \to v$ `(cap = 1, cost = w)` and $v \to u$ `(cap = 1, cost = w)`.
    2. Connect $S \to 1$ `(cap = 2, cost = 0)` and $N \to T$ `(cap = 2, cost = 0)`.
    3. Run 2 iterations of Dijkstra with Suurballe potentials in $O(M \log N)$ time.
- **Step 4 — Broken Gadget Trap & Progressive Hints**:
  - *Trap*: Students often worry: *"What if Augmentation 1 uses $u \to v$ (cost $+w$) and Augmentation 2 uses the other directed arc $v \to u$ (cost $+w$), using the same undirected edge in opposite directions?"* As proved in Section 2.1, once $u \to v$ is saturated, the residual graph contains the backward arc $v \to u$ of cost **$-w < +w$**! Thus Augmentation 2 will **always** traverse the residual backward arc of cost $-w$ (cancelling the flow on $\{u,v\}$) rather than the fresh arc of cost $+w$.
  - **Hint 1**: Reversing a path from $N$ to $1$ in an undirected graph gives a second path from $1$ to $N$.
  - **Hint 2**: Replace each undirected edge with two directed arcs of capacity $1$ and cost $w$, and push $2$ units of flow from $1$ to $N$.
  - **Hint 3**: After finding the first shortest path via Dijkstra, update vertex potentials $\pi(v) = d(1, v)$ and run a second Dijkstra on the residual graph.

---

#### P04 — DAG Path Cover with Arbitrary Teleport Resets (`Luogu P2469 [SDOI2010] 星际竞速`)
- **Judge URL**: [Luogu P2469](https://www.luogu.com.cn/problem/P2469)
- **Constraints**: $N \le 800$ planets, $M \le 15,000$ directed airways $(u \to v \text{ only if } u < v)$, teleport costs $A_v \ge 0$.
- **Step 1 — Diagnostic Signal & Failure of DAG DP**:
  - **Signal**: Visit all $N$ planets in a DAG $(u < v)$. At any time, the racer can either follow a directed edge $u \to v$ (cost $w_{u,v}$) or teleport from anywhere to planet $v$ (cost $A_v$), visiting each planet **at least once** (in fact, **exactly once**, since teleporting skips intermediate planets!).
  - **Why DAG DP Fails**: The constraint that **every** planet $1 \dots N$ must have in-degree $1$ and out-degree $\le 1$ couples all paths globally; a single path cannot cover the graph, and tracking which subset of planets has been covered requires $2^N$ states.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Each planet $v \in \{1, \dots, N\}$ is entered exactly once: either via a teleport start ($s_v = 1$, cost $A_v$) or via a DAG edge $(u, v)$ ($x_{u,v} = 1$, cost $w_{u,v}$):
    $$s_v + \sum_{u < v} x_{u,v} = 1 \quad (\forall v), \qquad \sum_{v > u} x_{u,v} \le 1 \quad (\forall u).$$
  - **Compiled Graph ($2N + 2$ vertices, $M + 3N$ arcs)**:
    1. Split each planet $v$ into $v_{\text{out}}$ (left) and $v_{\text{in}}$ (right).
    2. Supply/Demand: $S \to u_{\text{out}}$ `(cap = 1, cost = 0)` and $v_{\text{in}} \to T$ `(cap = 1, cost = 0)`.
    3. **Teleport Start Arc**: $S \to v_{\text{in}}$ `(cap = 1, cost = A_v)`.
    4. **Airway Transition Arc**: $u_{\text{out}} \to v_{\text{in}}$ `(cap = 1, cost = w_{u,v})` for $u < v$.
  - Push $F = N$ units of flow from $S$ to $T$; every $v_{\text{in}} \to T$ is saturated, choosing the globally optimal mix of teleports and airway transitions.
- **Step 4 — Broken Gadget Trap & Progressive Hints**:
  - *Trap*: Connecting the teleport edge to $v_{\text{out}}$ instead of $v_{\text{in}}$ fails to satisfy $v$'s arrival requirement ($v_{\text{in}} \to T$).
  - **Hint 1**: Teleporting to planet $v$ simply starts a new directed path at $v$ with initiation cost $A_v$.
  - **Hint 2**: Every planet $v$ must have exactly one incoming transition (either a teleport of cost $A_v$ or an edge $u \to v$ from some $u < v$), and each planet $u$ can have at most one outgoing edge.
  - **Hint 3**: Build the standard bipartite path-cover graph $V_{\text{out}} \to V_{\text{in}}$ and add direct edges $S \to v_{\text{in}}$ with capacity $1$ and cost $A_v$.

---

#### P05 — Multi-Speed Resource Refurbishment (`Luogu P1251 [网络流24题] 餐巾计划问题`)
- **Judge URL**: [Luogu P1251](https://www.luogu.com.cn/problem/P1251)
- **Constraints**: $N \le 2,000$ days, daily demand $r_t \le 10^7$, fresh cost $p$, fast laundry $(m \text{ days}, \text{cost } f)$, slow laundry $(n \text{ days}, \text{cost } s)$.
- **Step 1 — Diagnostic Signal & Failure of Greedy**:
  - **Signal**: Consumable resource with daily demand $r_t$, reusable after delayed multi-speed refurbishment.
  - **Why Greedy Fails**: Locally buying vs. fast-washing vs. slow-washing on day $t$ depends on whether dirty napkins saved today are needed for cheap slow laundry $n$ days later or urgent fast laundry $m$ days later.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Use the Bipartite Day/Night Split (Model A of Section 4.1) with $2N + 2$ vertices ($X_t$ dirty night supply, $Y_t$ clean morning demand) and $6N$ arcs:
    - $S \to X_t$ `(cap = r_t, cost = 0)` (dirty napkins generated on day $t$)
    - $Y_t \to T$ `(cap = r_t, cost = 0)` (clean napkins consumed on day $t$)
    - $S \to Y_t$ `(cap = \infty, cost = p)` (buy fresh napkin)
    - $X_t \to X_{t+1}$ `(cap = \infty, cost = 0)` (defer dirty napkin to next night)
    - $X_t \to Y_{t+m}$ `(cap = \infty, cost = f)` (fast laundry)
    - $X_t \to Y_{t+n}$ `(cap = \infty, cost = s)` (slow laundry)
- **Step 4 — Broken Gadget Trap & Progressive Hints**:
  - *Trap*: Use 64-bit integers (`long long`) for both flow and cost ($\sum r_t \le 2 \times 10^{10}$), and **never** add $X_t \to T$!
  - **Hint 1**: Why can't a single node per day enforce both "consume $r_t$ clean napkins" and "output $r_t$ dirty napkins"?
  - **Hint 2**: Decouple each day $t$ into a Dirty Supply node $X_t$ (fed by $S$ with capacity $r_t$) and a Clean Demand node $Y_t$ (draining to $T$ with capacity $r_t$).
  - **Hint 3**: Connect $X_t \to X_{t+1}$ (cost $0$), $X_t \to Y_{t+m}$ (cost $f$), $X_t \to Y_{t+n}$ (cost $s$), and $S \to Y_t$ (cost $p$).

---

#### P06 — Heterogeneous Parallel Machine Total Completion Time (`Luogu P2053 [SCOI2007] 修车`)
- **Judge URL**: [Luogu P2053](https://www.luogu.com.cn/problem/P2053)
- **Constraints**: $M \le 9$ mechanics, $N \le 60$ cars, repair times $t_{i,j} \le 1,000$.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Minimize average waiting time $\frac{1}{N} \sum_{i=1}^N C_i$ across $M$ parallel heterogeneous machines.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Apply the Reverse-Order Completion Time Indexing (Section 3.1): car $i$ placed in the $r$-th from last slot $(j, r)$ on mechanic $j$ contributes $r \cdot t_{i,j}$ to $\sum C_k$.
  - **Compiled Graph ($N + NM + 2 \le 602$ vertices, $\approx 33,000$ arcs)**:
    - $S \to \text{Car } i$ `(cap = 1, cost = 0)` for $i \in \{1, \dots, N\}$.
    - $\text{Car } i \to (j, r)$ `(cap = 1, cost = r \cdot t_{i,j})` for $j \in \{1, \dots, M\}$, $r \in \{1, \dots, N\}$.
    - $(j, r) \to T$ `(cap = 1, cost = 0)`.
  - Run MCMF for $N$ units of flow; output $\text{MinCost} / N$ formatted to $2$ decimal places.
- **Step 4 — Progressive Hints**:
  - **Hint 1**: If a mechanic repairs $k$ cars in order $c_1, c_2, \dots, c_k$, how many cars wait for $c_k$? Only $1$ ($c_k$ itself). How many wait for $c_{k-1}$? Exactly $2$!
  - **Hint 2**: Index each mechanic's queue in **reverse order** $r = 1, 2, \dots, N$ from the end of the schedule.
  - **Hint 3**: Build a bipartite matching graph between the $N$ cars and the $M \times N$ reverse slots $(j, r)$ with edge weight $r \cdot t_{i,j}$.

---

#### P07 — Multi-Period Capacitated Inventory (`Luogu P2517 [HAOI2010] 订货`)
- **Judge URL**: [Luogu P2517](https://www.luogu.com.cn/problem/P2517)
- **Constraints**: $N \le 50$ months, monthly demand $U_t \ge 0$, unit order cost $d_t$, storage cost $m$ per unit per month, warehouse capacity $S$.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Single-commodity production and inventory planning over a discrete timeline with time-varying purchase prices and bounded storage carryover.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Unlike `餐巾计划问题` (where used napkins come back), ordered goods are **permanently consumed** when meeting demand $U_t$. Thus no vertex splitting is needed!
  - Flow conservation at month $t$: $I_{t-1} + x_t = U_t + I_t$, where $x_t \ge 0$ is ordered quantity (cost $d_t$) and $I_t \in [0, S]$ is ending inventory carried to month $t+1$ (cost $m$).
  - **Compiled Graph ($N + 2$ vertices, $3N$ arcs)**:
    - $S_{\text{src}} \to t$ `(cap = \infty, cost = d_t)` (order in month $t$)
    - $t \to T_{\text{sink}}$ `(cap = U_t, cost = 0)` (satisfy demand in month $t$)
    - $t \to t+1$ `(cap = S, cost = m)` (store in warehouse overnight)
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Why don't we need to split day $t$ into two vertices here, unlike the Napkin Problem?
  - **Hint 2**: Because goods consumed by customers never re-enter the system! Write the standard inventory conservation law $I_{t-1} + x_t = U_t + I_t$.
  - **Hint 3**: Connect $S \to t$ with cost $d_t$, $t \to T$ with capacity $U_t$, and $t \to t+1$ with capacity $S$ and cost $m$.

---

### 8.2 Tier 2: `Intermediate` (`P08` – `P15`)

---

#### P08 — Weighted $K$-Slot Cache Retention (`CF 802 C — Heidi and Library (medium)`)
- **Judge URL**: [Codeforces 802C](https://codeforces.com/problemset/problem/802/C)
- **Constraints**: $N, K \le 80$, book IDs $a_t \in [1, N]$, purchase costs $c_b \in [1, 10^6]$.
- **Step 1 — Diagnostic Signal & Failure of Belady Greedy**:
  - **Signal**: Offline weighted paging/caching with cache capacity $K$ and heterogeneous item fetch costs $c_b$.
  - **Why Belady Fails**: Evicting a book with distant next use $\text{next}(t)$ can be suboptimal if its re-purchase cost $c_{a_t}$ is much larger than the sum of re-purchase costs of books requested sooner.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Use **Compilation 1 (Timeline Saving Chords)** from Section 4.3:
    - Baseline cost if we buy on every request: $\text{Base} = \sum_{t=1}^N c_{a_t}$.
    - Let $\text{next}(t)$ be the next occurrence of book $a_t$ after day $t$. Retaining $a_t$ across $(t, \text{next}(t))$ saves $c_{a_t}$ and consumes $1$ of the $K - 1$ background cache slots on days $s \in \{t+1, \dots, \text{next}(t)-1\}$.
    - **Compiled Graph ($N + 2$ vertices, $2N$ arcs)**:
      1. Timeline spine: $s \to s+1$ `(cap = K - 1, cost = 0)` for $s = 1 \dots N-1$.
      2. If $\text{next}(t) = t + 1$, subtract $c_{a_t}$ from $\text{Base}$ immediately (zero background cache needed!).
      3. If $\text{next}(t) > t + 1$, add saving chord $(t+1) \to \text{next}(t)$ with `(cap = 1, cost = -c_{a_t})`.
      4. Send $K - 1$ units of flow from $1$ to $N$; answer is $\text{Base} + \text{MinCost}$.
- **Step 4 — Broken Gadget Trap & Progressive Hints**:
  - *Trap*: Sending the saving chord from $t \to \text{next}(t)$ instead of $(t+1) \to \text{next}(t)$ wrongly charges book $a_t$ a background slot on day $t$ itself (when it is already in the mandatory active slot!).
  - **Hint 1**: Start by assuming you pay $c_{a_t}$ on every single day $t$, and reformulate the problem as maximizing total **cost saved** by keeping books between consecutive requests $t$ and $\text{next}(t)$.
  - **Hint 2**: On any day $s$, the requested book $a_s$ occupies $1$ slot, leaving $K - 1$ slots for other books carried over from before $s$ to after $s$.
  - **Hint 3**: Build a path $1 \to 2 \to \dots \to N$ of capacity $K-1$ and add chords $(t+1) \to \text{next}(t)$ of capacity $1$ and cost $-c_{a_t}$.

---

#### P09 — Maximum-Weight $K$-Overlap Interval Selection (`POJ 3680 — Intervals`)
- **Judge URL**: [POJ 3680](http://poj.org/problem?id=3680)
- **Constraints**: $N \le 200$ open intervals $(a_i, b_i)$ with weight $w_i > 0$, overlap limit $K \le 10$, coordinates $\le 10^5$.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Select a maximum-weight subset of open intervals such that every point on the real line is covered by at most $K$ intervals.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Coordinate-compress all endpoints into $1 < 2 < \dots < M \le 2N$.
  - Let $x_i \in \{0, 1\}$ indicate selecting interval $i$, and let $s_j \ge 0$ be the slack on elementary segment $(j, j+1)$:
    $$\left(\sum_{i : a_i \le j < b_i} x_i\right) + s_j = K \qquad (j = 1, \dots, M-1).$$
  - Taking consecutive differences $E_j - E_{j-1}$ gives exact flow conservation at vertex $j$: interval $i$ enters at $a_i$ and exits at $b_i$ (or equivalently, $x_i = 1$ diverts $1$ unit of the $K$-stream from $a_i$ to $b_i$ at cost $-w_i$!).
  - **Compiled Graph ($M + 2$ vertices, $M + N$ arcs)**:
    - Spine $j \to j+1$ `(cap = K, cost = 0)` for $j = 1 \dots M-1$.
    - Interval chord $a_i \to b_i$ `(cap = 1, cost = -w_i)`.
    - $S \to 1$ `(cap = K, cost = 0)` and $M \to T$ `(cap = K, cost = 0)`. Output $-\text{MinCost}$.
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Coordinate-compress the endpoints so there are at most $2N = 400$ distinct coordinates.
  - **Hint 2**: Imagine $K$ parallel tracks running from coordinate $1$ to coordinate $M$. Selecting interval $(a_i, b_i)$ occupies $1$ track from $a_i$ to $b_i$.
  - **Hint 3**: Add spine edges $j \to j+1$ `(cap = K, cost = 0)` and interval chords $a_i \to b_i$ `(cap = 1, cost = -w_i)`.

---

#### P10 — Bitonic Round-Trip Max-Vertex Tour (`Luogu P2770 [网络流24题] 航空路线问题`)
- **Judge URL**: [Luogu P2770](https://www.luogu.com.cn/problem/P2770)
- **Constraints**: $N \le 100$ cities ordered west-to-east $1 < 2 < \dots < N$, $M$ undirected flights.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Fly from City $1$ strictly east to City $N$, then strictly west back to City $1$, visiting no intermediate city twice and maximizing the total number of cities visited (and printing the actual tour!).
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Reversing the west-bound return leg $N \leadsto 1$ turns the bitonic tour into **two internally vertex-disjoint west-to-east paths from $1$ to $N$** in the DAG where edges are oriented $u \to v$ for $u < v$.
  - **Compiled Graph ($2N$ vertices, $M + N$ arcs)**:
    1. Split $v \in \{2, \dots, N-1\}$ into $v_{\text{in}} \to v_{\text{out}}$ `(cap = 1, cost = -1)`.
    2. Split endpoints $1$ and $N$ into $v_{\text{in}} \to v_{\text{out}}$ `(cap = 2, cost = -1)`.
    3. For each undirected flight $\{u, v\}$ with $u < v$, add $u_{\text{out}} \to v_{\text{in}}$ `(cap = 1, cost = 0)` (**unless** $\{u, v\} = \{1, N\}$, which gets `cap = 2` to allow the degenerate $1 \to N \to 1$ direct flight if $K=2$!).
  - Push $F = 2$ units from $1_{\text{in}}$ to $N_{\text{out}}$; max cities visited is $(-\text{MinCost}) - 2$. To reconstruct the tour, trace the two unit-flow paths from $1$ to $N$: print Path 1 forward ($1 \leadsto N$) and Path 2 in reverse ($N \leadsto 1$).
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Why is a west-to-east path followed by an east-to-west path equivalent to two west-to-east paths?
  - **Hint 2**: Split internal cities $v_{\text{in}} \to v_{\text{out}}$ with capacity $1$ and cost $-1$, and endpoints $1, N$ with capacity $2$.
  - **Hint 3**: Watch out for the edge case where a direct flight $(1, N)$ exists and is used in both directions ($1 \to N \to 1$, total $2$ cities): give edge $(1_{\text{out}}, N_{\text{in}})$ capacity $2$, or reject if flow $< 2$.

---

#### P11 — Multi-Rover Collect-Once Grid & Flow Path Decomposition (`Luogu P3356 [网络流24题] 火星探险问题`)
- **Judge URL**: [Luogu P3356](https://www.luogu.com.cn/problem/P3356)
- **Constraints**: $P, Q \le 35$ grid, $K \le 50$ rovers, cell types $0$ (flat), $1$ (obstacle), $2$ (rock specimen).
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Identical collect-once grid mechanics to `P01`, plus the requirement to **reconstruct and print the exact step-by-step movement commands** (`0` for South, `1` for East) of each of the $K$ rovers!
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation & Flow Decomposition**:
  - Build the exact cell-split graph of `P01`, deleting obstacle cells (`type == 1`), giving specimen cells (`type == 2`) a harvest arc `(cap = 1, cost = -1)` $\oplus$ bypass arc `(cap = \infty, cost = 0)`, and flat cells (`type == 0`) a single arc `(cap = \infty, cost = 0)`.
  - **Path Reconstruction**: After running MCMF for $K$ rovers, the integer flow values $f(u_{\text{out}} \to v_{\text{in}}) \in \{0, 1, \dots, K\}$ on the grid transition arcs form a DAG flow of value $K$. For each rover $r = 1 \dots K$, start at $(1,1)$ and greedily walk to whichever neighbor $(i+1, j)$ or $(i, j+1)$ has remaining positive flow $f > 0$, decrementing $f \gets f - 1$ along the chosen edges!
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Finding the maximum number of collected rocks is identical to `Luogu P2045`. How do you extract the $K$ individual rover paths after the flow finishes?
  - **Hint 2**: Because all rovers are identical and any unit-flow decomposition of the final flow collects the exact same set of rocks, you can decompose the flow greedily!
  - **Hint 3**: Run $K$ DFS walks from $(1,1)$ to $(P,Q)$, following any transition edge with `flow > 0` and decrementing `flow` by $1$.

---

#### P12 — Fleet Bounded-Start DAG Path Cover (`ICPC WF 2015 C — Catering` / `UVA 1711`)
- **Judge URL**: [LiveArchive 7152 / UVA 1711](https://onlinejudge.org/external/17/1711.pdf)
- **Constraints**: $N \le 100$ chronologically ordered events $1 \dots N$, $K \le 100$ catering teams at depot $0$.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Cover all $N$ events in a DAG using **at most $K$ teams** starting from depot $0$, minimizing total transition cost.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Apply the **Component-Merging Invariant** (Section 2.2): every event $v \in \{1, \dots, N\}$ must be entered by either a team dispatched fresh from depot $0$ ($s_v = 1$, where $\sum_{v=1}^N s_v \le K$) or a team relocating from an earlier event $u < v$ ($x_{u,v} = 1$).
  - **Compiled Graph ($2N + 3$ vertices, $O(N^2)$ arcs)**:
    1. Starter Hub $H_0$ (depot): $S \to H_0$ `(cap = K, cost = 0)`, and $H_0 \to v_{\text{in}}$ `(cap = 1, cost = c(0, v))` for $v = 1 \dots N$.
    2. Departures: $S \to u_{\text{out}}$ `(cap = 1, cost = 0)` and $u_{\text{out}} \to v_{\text{in}}$ `(cap = 1, cost = c(u, v))` for $1 \le u < v \le N$.
    3. Arrivals: $v_{\text{in}} \to T$ `(cap = 1, cost = 0)` for $v = 1 \dots N$.
    4. Push exact flow $F = N$ into $T$.
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Every event $v \in \{1, \dots, N\}$ has in-degree $1$ (from depot $0$ or some $u < v$) and out-degree $\le 1$.
  - **Hint 2**: How do you bound the total number of edges leaving depot $0$ by $K$ while requiring all $N$ events to be covered?
  - **Hint 3**: Give the depot node $H_0$ a single supply edge $S \to H_0$ of capacity $K$, give each $u_{\text{out}}$ a supply edge $S \to u_{\text{out}}$ of capacity $1$, and require $N$ units of flow to reach $T$ via $v_{\text{in}} \to T$.

---

#### P13 — Weighted Mixed Graph Eulerian Orientation (`POJ 1637 Sightseeing Tour` Weighted / `CF 1070 I`)
- **Judge URL**: [POJ 1637](http://poj.org/problem?id=1637)
- **Constraints**: $N \le 200$ vertices, $M \le 1,000$ edges (some directed, some undirected with orientation reversal cost $w_e \ge 0$).
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Orient all undirected edges of a mixed graph at minimum cost so that the resulting directed graph is Eulerian ($d^+(v) = d^-(v)$ for all $v$).
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Arbitrarily orient each undirected edge $e = \{u, v\}$ as $u \to v$ (paying initial cost $c_{u \to v}$).
  - Compute initial degree imbalance $\Delta(v) = d^-(v) - d^+(v)$.
  - Reversing $u \to v$ into $v \to u$ ($x_e \in \{0, 1\}$, marginal cost $\Delta c_e = c_{v \to u} - c_{u \to v}$) changes $\Delta(u)$ by $+2$ and $\Delta(v)$ by $-2$.
  - **Necessary & Sufficient Parity Check**: If any $\Delta(v)$ is odd, output `impossible` immediately!
  - Otherwise, set supply $b(v) = -\Delta(v) / 2$:
    - If $\Delta(v) < 0$ (excess out-degree), add $S \to v$ `(cap = -\Delta(v)/2, cost = 0)`.
    - If $\Delta(v) > 0$ (excess in-degree), add $v \to T$ `(cap = \Delta(v)/2, cost = 0)`.
    - For each undirected edge initially oriented $u \to v$, add arc $u \to v$ `(cap = 1, cost = c_{v \to u} - c_{u \to v})`.
  - Run MCMF; if max flow saturates all supplies, minimum orientation cost is $\sum c_{\text{init}} + \text{MinCost}$.
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Fix an arbitrary initial orientation for every undirected edge and compute $d^-(v) - d^+(v)$ at every vertex.
  - **Hint 2**: How much does $d^-(u) - d^+(u)$ change when you flip a single edge $u \to v$ to $v \to u$? By $+2$!
  - **Hint 3**: Divide all degree imbalances by $2$ and model each flippable edge $u \to v$ as a unit-capacity arc of cost $c_{v \to u} - c_{u \to v}$.

---

#### P14 — Branch Network / Lower-Bound Directed CPP on DAGs (`Luogu P4043 [AHOI2014/JSOI2014] 支线网络`)
- **Judge URL**: [Luogu P4043](https://www.luogu.com.cn/problem/P4043)
- **Constraints**: $N \le 300$ vertices in a rooted DAG (root $1$), $M \le 5,000$ weighted directed edges; every path can reset to root $1$ at any vertex $u > 1$ for cost $0$.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Cover **every directed edge** of a DAG at least once using walks starting at root $1$, minimizing total edge weight.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Ending a walk at vertex $u$ and starting a new walk at root $1$ is equivalent to traversing a free return arc $u \to 1$ `(cap = \infty, cost = 0)`.
  - Each original edge $e = (u, v)$ has flow lower bound $L(e) = 1$, upper bound $U(e) = \infty$, cost $w_e$.
  - **Demand Substitution ($f(e) = 1 + y_e$)**:
    1. Initialize $\text{BaseCost} = \sum_{e \in E} w_e$ and net balance $\Delta(v) = d^-(v) - d^+(v)$ from the mandatory $1$ unit on each edge.
    2. For each original edge $e = (u, v)$, add spare arc $u \to v$ `(cap = \infty, cost = w_e)`.
    3. For each $u > 1$, add return arc $u \to 1$ `(cap = \infty, cost = 0)`.
    4. Connect $S \to v$ `(cap = \Delta(v), cost = 0)` if $\Delta(v) > 0$, and $v \to T$ `(cap = -\Delta(v), cost = 0)` if $\Delta(v) < 0$.
    5. Output $\text{BaseCost} + \text{MinCost}$.
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Why is this problem an edge-covering problem (Chinese Postman) rather than a vertex-covering problem?
  - **Hint 2**: Give every original edge $(u,v)$ a lower bound of $1$ and capacity $\infty$, and add free return edges $u \to 1$ of capacity $\infty$ and cost $0$.
  - **Hint 3**: Eliminate the lower bounds by pre-paying $\sum w_e$ and routing the resulting degree imbalances $\Delta(v) = d^-(v) - d^+(v)$ via standard MCMF.

---

#### P15 — Parametric All-$k$ Bipartite Matching Curve (`AtCoder ABC 247 G — Dream Team`)
- **Judge URL**: [AtCoder ABC 247G](https://atcoder.jp/contests/abc247/tasks/abc247_g)
- **Constraints**: $N \le 3 \times 10^4$ students, university $A_i \in [1, 150]$, subject $B_i \in [1, 150]$, power $C_i \in [1, 10^9]$.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Output the maximum possible team power for **every possible team size $k = 1, 2, \dots, K_{\max}$**, where no two chosen students share a university $A_i$ or a subject $B_i$.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Each student $i$ is a bipartite edge between Left vertex $A_i \in \{1, \dots, 150\}$ and Right vertex $B_i \in \{1, \dots, 150\}$ of capacity $1$ and reward $C_i$. (Keep only the highest-$C_i$ student for each pair $(A_i, B_i)$.)
  - Shift edge costs to non-negative: $\text{cost}(A_i \to B_i) = M - C_i$ where $M = 10^9$.
  - **All-$k$ Parametric Extraction**: By the **Successive Shortest Path (SSP) Optimality Invariant**, after the $k$-th unit augmentation from $S$ to $T$, the current flow is an optimal min-cost flow of volume $k$! Thus a **single run** of SSP (at most $150$ Dijkstra steps on $302$ vertices) yields the answers for all $k = 1 \dots K_{\max}$: $\text{Ans}(k) = k \cdot M - \text{TotalCost}(k)$.
- **Step 4 — Progressive Hints**:
  - **Hint 1**: View each student as an edge connecting University $A_i$ to Subject $B_i$ in a $150 \times 150$ bipartite graph.
  - **Hint 2**: Do you need to run MCMF separately for each $k$? No—SSP computes the optimal flow for $k = 1, 2, 3, \dots$ sequentially!
  - **Hint 3**: Shift costs to $10^9 - C_i \ge 0$ so Dijkstra works directly without SPFA, and record $k \cdot 10^9 - \text{cost}_k$ after each unit augmentation.

---

### 8.3 Tier 3: `Advanced` (`P16` – `P23`)

---

#### P16 — Dynamic Lazy Vertex Spawning for Large-Scale Scheduling (`Luogu P2050 [NOI2012] 美食节`)
- **Judge URL**: [Luogu P2050](https://www.luogu.com.cn/problem/P2050)
- **Constraints**: $N \le 40$ dish types, $M \le 100$ chefs, total dishes $P = \sum_{i=1}^N p_i \le 800$, cooking times $t_{i,j} \le 1,000$.
- **Step 1 — Diagnostic Signal & Static Graph Bottleneck**:
  - **Signal**: Same reverse-rank completion time objective $\sum_{j, r} r \cdot t_{\pi(j,r), j}$ as `P06 ([SCOI2007] 修车)`, but scaled up so that the static graph has $M \cdot P = 80,000$ slot vertices and $N \cdot M \cdot P = 3.2 \times 10^6$ arcs (TLE).
- **Step 2 & Step 3 — Dynamic Lazy Graph Compilation**:
  - Apply the **Frontier Slot Dominance Theorem** (Section 3.2):
    1. Start with only the $N$ dish vertices $i \in \{1, \dots, N\}$ (`S -> i` with `cap = p_i, cost = 0`) and the $M$ **rank-1 frontier slots** $(j, 1)$ (`i -> (j, 1)` with `cap = 1, cost = 1 * t_{i,j}`, and `(j, 1) -> T` with `cap = 1, cost = 0`).
    2. In each of the $P$ iterations, run a **single-unit** shortest augmenting path from $S$ to $T$.
    3. Let $(j^*, r_{j^*})$ be the unique frontier node whose edge $(j^*, r_{j^*}) \to T$ was just saturated. Immediately create node $(j^*, r_{j^*} + 1)$, add $(j^*, r_{j^*} + 1) \to T$ `(cap = 1, cost = 0)`, and connect all $i \in \{1, \dots, N\}$ to $(j^*, r_{j^*} + 1)$ with `(cap = 1, cost = (r_{j^*} + 1) * t_{i, j^*})`.
  - Final active graph has $N + M + P \le 940$ vertices and $N(M + P) \le 36,000$ edges, running in $< 0.15\text{ s}$.
- **Step 4 — Broken Gadget Trap & Progressive Hints**:
  - *Trap*: Never push multiple units of flow along a zero-reduced-cost blocking flow (Zkw multi-push) before spawning $(j^*, r_{j^*} + 1)$; always push $1$ unit at a time or spawn inline!
  - **Hint 1**: Across all $M = 100$ chefs, at most $P = 800$ total slots are ever used. Why create $80,000$ slot nodes upfront?
  - **Hint 2**: For each chef $j$, only the smallest currently empty slot $(j, r_j)$ needs to exist in the graph.
  - **Hint 3**: After each unit augmentation saturates $(j^*, r_{j^*}) \to T$, dynamically allocate $(j^*, r_{j^*} + 1)$ and add its $N$ incoming edges from the dish nodes.

---

#### P17 — Precedence-Locked Multi-Agent Shortest Path Cover (`Luogu P4542 [ZJOI2011] 营救皮卡丘`)
- **Judge URL**: [Luogu P4542](https://www.luogu.com.cn/problem/P4542)
- **Constraints**: $N \le 150$ bases numbered $0, 1, \dots, N$, $M \le 20,000$ undirected edges, $K \le 10$ teams starting at $0$. Base $v$ must be unlocked only after $1, 2, \dots, v-1$ are unlocked, and teams cannot pass through any locked base $w > v$ on their way to $v$.
- **Step 1 — Diagnostic Signal & Failure of Standard APSP**:
  - **Signal**: Cover vertices $1 \dots N$ using at most $K$ vehicles starting at $0$, where moving from an already-unlocked vertex $u < v$ to the next target $v$ can only traverse intermediate vertices $w \le v$.
  - **Why Standard Floyd–Warshall Fails**: Standard APSP $d(u, v)$ might route through an intermediate vertex $w > v$, which has not been unlocked yet at the moment $v$ is first visited!
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  1. **Restricted Floyd–Warshall Metric Closure**: Compute $D(u, v)$ for all $0 \le u < v \le N$ by restricting intermediate transitions $k$ to $k \le \max(u, v) = v$:
     $$D(u, v) = \text{shortest path from } u \text{ to } v \text{ using only internal vertices } \{0, 1, \dots, v\}.$$
  2. **Bounded-Fleet ($K$) DAG Path Cover**:
     - Split each $v \in \{1, \dots, N\}$ into $v_{\text{out}}$ and $v_{\text{in}}$.
     - Starter depot $0_{\text{out}}$: $S \to 0_{\text{out}}$ `(cap = K, cost = 0)` and $0_{\text{out}} \to v_{\text{in}}$ `(cap = 1, cost = D(0, v))`.
     - Relocations: $S \to u_{\text{out}}$ `(cap = 1, cost = 0)` and $u_{\text{out}} \to v_{\text{in}}$ `(cap = 1, cost = D(u, v))` for $1 \le u < v \le N$.
     - Arrivals: $v_{\text{in}} \to T$ `(cap = 1, cost = 0)` for $v = 1 \dots N$. Push exact flow $F = N$.
- **Step 4 — Progressive Hints**:
  - **Hint 1**: When a team travels from an already-unlocked base $u < v$ to unlock base $v$, which bases are currently unlocked? Exactly $\{0, 1, \dots, v-1\}$!
  - **Hint 2**: Modify Floyd–Warshall so that `dist[i][j]` is updated via `k` only when `k <= max(i, j)`.
  - **Hint 3**: Once `D(u, v)` is known for all $u < v$, the problem reduces to covering a DAG of $N$ vertices with at most $K$ paths starting from $0$.

---

#### P18 — Scaling Collect-Once $K$-Walks to $N = 2 \times 10^5$ via SCC Condensation (`AtCoder ABC 214 H — Collecting`)
- **Judge URL**: [AtCoder ABC 214H](https://atcoder.jp/contests/abc214/tasks/abc214_h)
- **Constraints**: $N, M \le 2 \times 10^5$ directed graph, $K \le 10$ players starting at vertex $1$, vertex rewards $X_v \ge 0$.
- **Step 1 — Diagnostic Signal & Failure of Direct Cyclic MCMF**:
  - **Signal**: $K$ walkers start at vertex $1$ in a general **cyclic** directed graph and can end at **any** vertices, maximizing the sum of distinct vertex rewards collected.
  - **Why Direct Cell-Splitting Fails**: Adding `(cap = 1, cost = -X_v)` inside a directed cycle creates **negative-cost cycles** in $G$, which both invalidates Dijkstra potentials and allows detached circulation flows inside unreachable or self-looping cycles!
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  1. **Tarjan SCC Condensation**: Any walker entering a Strongly Connected Component $C$ can visit **every** vertex in $C$ and exit from any vertex in $C$. Condense $G$ into its SCC DAG $G_{\text{DAG}}$ where each super-node $C$ has aggregated reward $W_C = \sum_{v \in C} X_v$. (Prune all SCCs not reachable from $C_{\text{start}} = \text{SCC}(1)$.)
  2. **Collect-Once DAG Compilation**:
     - Split each reachable SCC $C$ into $C_{\text{in}} \to C_{\text{out}}$ with parallel arcs `(cap = 1, cost = -W_C)` $\oplus$ `(cap = K - 1, cost = 0)`.
     - DAG edges: $C_{\text{out}} \to D_{\text{in}}$ `(cap = K, cost = 0)`.
     - Since walkers can stop anywhere, connect $C_{\text{out}} \to T$ `(cap = K, cost = 0)` for **all** $C$.
  3. **Potential Initialization on DAG**: Compute initial shortest paths $\pi(v)$ from $S$ via topological DP in $O(N + M)$ time so that all $K \le 10$ augmentations run via pure Dijkstra in $O(K (N + M) \log N)$ time!
- **Step 4 — Progressive Hints**:
  - **Hint 1**: If a player enters a strongly connected component (SCC), how many vertices inside that SCC can they collect? All of them!
  - **Hint 2**: Contract SCCs into a DAG and split each SCC node into `in` and `out` with parallel edges `(1, -W_C)` and `(K-1, 0)`.
  - **Hint 3**: Because $N, M \le 2 \times 10^5$, SPFA will TLE; compute initial Johnson potentials $\pi(v)$ in $O(N + M)$ using topological sort DP on the SCC DAG, then run $K$ steps of Dijkstra.

---

#### P19 — Next-Occurrence Hub Sparsification for $K$-Subsequence Cover (`CF 818 G — Four Melodies`)
- **Judge URL**: [Codeforces 818G](https://codeforces.com/problemset/problem/818/G)
- **Constraints**: $N \le 3,000$ notes $a_1, \dots, a_N$ ($a_i \in [1, 10^5]$), $K = 4$ vertex-disjoint subsequences.
- **Step 1 — Diagnostic Signal & Failure of Explicit $O(N^2)$ DAG**:
  - **Signal**: Choose $K = 4$ index-disjoint subsequences maximizing total length, where adjacent elements $a_i, a_j$ ($i < j$) satisfy $|a_i - a_j| = 1$ or $a_i \equiv a_j \pmod 7$.
  - **Why Explicit $O(N^2)$ Edges TLE**: With $N = 3,000$, adding all valid pairs $i_{\text{out}} \to j_{\text{in}}$ creates up to $4.5 \times 10^6$ arcs, which is too slow for MCMF.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation (Persistent Relay Hubs)**:
  - Instead of connecting $i_{\text{out}}$ to *all* future $j > i$ with $a_j \equiv a_i \pmod 7$, build a **persistent relay chain** for each residue $r \in \{0, \dots, 6\}$ and each value $v \in [1, 10^5]$:
    - At step $i$ (sweeping $i = N$ down to $1$), let $M_{i, r}$ be the hub for the earliest index $\ge i$ with $a \equiv r \pmod 7$, and $V_{i, v}$ be the hub for the earliest index $\ge i$ with $a = v$.
    - Actually, even simpler: for each note $i$, let:
      - $\text{next\_same}(i) = \min\{j > i : a_j = a_i\}$
      - $\text{next\_plus}(i) = \min\{j > i : a_j = a_i + 1\}$
      - $\text{next\_minus}(i) = \min\{j > i : a_j = a_i - 1\}$
      - $\text{next\_mod}(i) = \min\{j > i : a_j \equiv a_i \pmod 7\}$
    - Introduce one **relay hub $H_i^{\text{val}}$** (representing "a flow token at position $\ge i$ looking for value $a_i$") and one **relay hub $H_i^{\text{mod}}$** (looking for residue $a_i \bmod 7$):
      - $H_i^{\text{val}} \to i_{\text{in}}$ `(cap = 1, cost = 0)` and $H_i^{\text{val}} \to H_{\text{next\_same}(i)}^{\text{val}}$ `(cap = K, cost = 0)`.
      - $H_i^{\text{mod}} \to i_{\text{in}}$ `(cap = 1, cost = 0)` and $H_i^{\text{mod}} \to H_{\text{next\_mod}(i)}^{\text{mod}}$ `(cap = K, cost = 0)`.
      - Now $i_{\text{out}}$ only needs **at most 3 outgoing transition arcs**: to $H_{\text{next\_plus}(i)}^{\text{val}}$, $H_{\text{next\_minus}(i)}^{\text{val}}$, and $H_{\text{next\_mod}(i)}^{\text{mod}}$!
  - Total vertices $= 4N + 2 \le 12,002$; total arcs $\approx 9N \le 27,000$!
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Why do we need to connect $i_{\text{out}}$ to *every* $j > i$ with $a_j \equiv a_i \pmod 7$ when all such $j$ can be chained together in a single linked list?
  - **Hint 2**: Create a relay node $H_i^{\text{mod}}$ for each $i$ that forwards flow either into $i_{\text{in}}$ or to the next index $\text{next\_mod}(i)$ with the same $\bmod 7$ residue.
  - **Hint 3**: Do the same for exact value matches $H_i^{\text{val}} \to H_{\text{next\_same}(i)}^{\text{val}}$, reducing the graph from $O(N^2)$ edges to $O(N)$ edges!

---

#### P20 — 2D Dominance Poset Transitive Reduction for Collect-Once Walks (`BZOJ 1930 / Luogu P2172 [SHOI2003] 吃豆豆`)
- **Judge URL**: [Luogu P2172](https://www.luogu.com.cn/problem/P2172)
- **Constraints**: $N \le 2,000$ beans at $(x_i, y_i)$ in the plane, $K = 2$ Pac-Men moving non-decreasingly in both $X$ and $Y$.
- **Step 1 — Diagnostic Signal & Failure of Full Poset Graph**:
  - **Signal**: Two monotone walkers in $\mathbb{R}^2$ collect beans (at most once per bean).
  - **Why Explicit Poset Edges TLE**: Sorting beans by $(x_i, y_i)$ and adding $i \to j$ whenever $x_i \le x_j$ and $y_i \le y_j$ creates up to $N(N-1)/2 \approx 2 \times 10^6$ edges.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation (Hasse Diagram + Bypass Port)**:
  - Sort beans so $(x_1, y_1) \le_{\text{lex}} (x_2, y_2) \le_{\text{lex}} \dots \le_{\text{lex}} (x_N, y_N)$.
  - Split each bean $i$ into $i_{\text{in}} \to i_{\text{out}}$ `(cap = 1, cost = -1)` (harvests bean $i$) plus a parallel **bypass node $i_{\text{pass}}$** (`i_{\text{in}} \to i_{\text{pass}}` and `i_{\text{pass}} \to i_{\text{out}}` of `cap = 2, cost = 0`) so walkers can transit through bean $i$'s dominance neighborhood without consuming its unit harvest arc!
  - **Running-Minimum $Y$-Threshold Pruning**: For a fixed $i$, sweep $j = i + 1 \dots N$ while maintaining the smallest $Y$-coordinate $Y_{\min}$ seen so far among valid $j$ with $y_j \ge y_i$:
    - Only add the edge $i_{\text{out}} \to j_{\text{in}}$ if $y_i \le y_j < Y_{\min}$, and then update $Y_{\min} \gets y_j$!
    - Why? Because if $y_k \ge y_j \ge y_i$ for $k > j$ (which implies $x_k \ge x_j \ge x_i$), then bean $k$ is already reachable from $i$ via the transitive path $i_{\text{out}} \to j_{\text{in}} \to j_{\text{pass}} \to j_{\text{out}} \to k_{\text{in}}$!
- **Step 4 — Progressive Hints**:
  - **Hint 1**: If $i$ can reach $j$ and $j$ can reach $k$, do you need the direct edge $i \to k$?
  - **Hint 2**: For transitive routing through $j$ to work even when $j$ is already eaten by another walker, give each bean $j$ a zero-cost bypass edge `cap = 2, cost = 0` alongside its harvest edge `cap = 1, cost = -1`.
  - **Hint 3**: Sweep $j > i$ and only add $i \to j$ when $y_j$ is strictly smaller than all previous $y_{j'} \ge y_i$ seen during the sweep.

---

#### P21 — Boolean Poset DAG Path Cover with Reset Transitions (`CF 1510 B — Button Lock`)
- **Judge URL**: [Codeforces 1510B](https://codeforces.com/problemset/problem/1510/B)
- **Constraints**: $d \le 10$ bits, $N \le 2^d - 1 \le 1,023$ required target bitmasks.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Start at bitmask $0$. You can toggle individual bits $0 \to 1$ (cost $1$ per bit) or press Reset `R` (cost $1$) to return to $0$. Visit all $N$ given bitmasks using the minimum total number of button presses, and print the sequence!
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Pressing `R` ends the current monotone bitmask chain at mask $u$ (having pressed $\text{popcount}(u)$ bit buttons plus $1$ for `R`, except the very last chain which doesn't need `R`!).
  - Equivalently, every target mask $u$ starts with baseline cost $\text{popcount}(u) + 1$ (if it ends a chain and presses `R`), and **continuing** a chain from $u$ to a strict superset $v \supsetneq u$ saves the entire $\text{popcount}(u) + 1$ cost of resetting after $u$!
  - **Compiled Graph ($2N + 2$ vertices, $O(3^d)$ arcs)**:
    1. Split each required mask $u$ into $u_{\text{out}}$ (left) and $u_{\text{in}}$ (right).
    2. $S \to u_{\text{out}}$ `(cap = 1, cost = 0)` and $v_{\text{in}} \to T$ `(cap = 1, cost = 0)`.
    3. For every pair of required masks $u \subsetneq v$ (`(u & v) == u`), add $u_{\text{out}} \to v_{\text{in}}$ with **`(cap = 1, cost = -(\text{popcount}(u) + 1))`**.
    4. Add a bypass $u_{\text{out}} \to T$ `(cap = 1, cost = 0)` so $u$ can be the end of a path (not matched to any $v \supsetneq u$).
    5. Total button presses $= \left(\sum_{u} (\text{popcount}(u) + 1)\right) + \text{MinCost} - 1$ (subtracting $1$ because the final path does not press `R`).
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Between two presses of `R`, the visited bitmasks form a strictly increasing chain $u_1 \subsetneq u_2 \subsetneq \dots \subsetneq u_k$ in the Boolean lattice (a DAG!).
  - **Hint 2**: What is the cost of a chain $u_1 \subsetneq \dots \subsetneq u_k$ followed by `R`? Exactly $\text{popcount}(u_k) + 1$, which depends **only on the last mask $u_k$** of the chain!
  - **Hint 3**: Charge $\text{popcount}(u) + 1$ to every mask upfront, and give each transition $u_{\text{out}} \to v_{\text{in}}$ ($u \subsetneq v$) a saving of $-(\text{popcount}(u) + 1)$ because $u$ is no longer the end of a chain!

---

#### P22 — Parity-Aware 3-Node Vertex Splitting for Endpoint vs. Transit Costs (`Luogu P3159 [CQOI2012] 交换棋子`)
- **Judge URL**: [Luogu P3159](https://www.luogu.com.cn/problem/P3159)
- **Constraints**: $N, M \le 20$ grid ($8$-connected), swap budgets $m_{i,j}$ per cell.
- **Step 1 — Diagnostic Signal & Failure of 2-Node Splitting**:
  - **Signal**: Route black tokens from initial cells to target cells via adjacent swaps so that cell $(i,j)$ participates in **at most $m_{i,j}$ total swaps** (incoming + outgoing), minimizing total swaps.
  - **Why Standard 2-Node Splitting ($v_{\text{in}} \to v_{\text{out}}$) Fails**:
    - An **internal transit cell** on a path participates in **2 swaps** ($1$ incoming + $1$ outgoing) per unit of flow.
    - A **start cell** or **end cell** of a path participates in **1 swap** ($1$ outgoing or $1$ incoming) for its endpoint role, plus $2$ swaps for each additional unit of flow transiting through it!
    - A single bridge $v_{\text{in}} \to v_{\text{out}}$ cannot charge $1$ unit of capacity to endpoints and $2$ units of capacity to transiting paths without half-integers!
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation (3-Node Tri-Split)**:
  - Split each cell $v = (i,j)$ into **three vertices**: $(v_{\text{in}}, v_{\text{mid}}, v_{\text{out}})$, where $v_{\text{in}} \to v_{\text{mid}}$ counts **incoming swaps** into $v$ and $v_{\text{mid}} \to v_{\text{out}}$ counts **outgoing swaps** from $v$!
  - Since every transit unit uses *both* $v_{\text{in}} \to v_{\text{mid}}$ and $v_{\text{mid}} \to v_{\text{out}}$, while a path starting at $v$ enters directly at $S \to v_{\text{mid}}$ (using only $v_{\text{mid}} \to v_{\text{out}}$) and a path ending at $v$ exits at $v_{\text{mid}} \to T$ (using only $v_{\text{in}} \to v_{\text{mid}}$):
    1. **Transit Cell** (`init == target`): $\text{in\_swaps} = \text{out\_swaps} \le \lfloor m_v / 2 \rfloor$. Set $\text{cap}(v_{\text{in}} \to v_{\text{mid}}) = \text{cap}(v_{\text{mid}} \to v_{\text{out}}) = \lfloor m_v / 2 \rfloor$.
    2. **Start Cell** (`init == 1, target == 0`): $\text{out\_swaps} = \text{in\_swaps} + 1$, so $\text{in\_swaps} + \text{out\_swaps} \le m_v \iff \text{in\_swaps} \le \lfloor (m_v - 1)/2 \rfloor$ and $\text{out\_swaps} \le \lfloor (m_v + 1)/2 \rfloor$. Connect $S \to v_{\text{mid}}$ `(cap = 1, cost = 0)`.
    3. **Target Cell** (`init == 0, target == 1`): $\text{in\_swaps} = \text{out\_swaps} + 1$, so $\text{in\_swaps} \le \lfloor (m_v + 1)/2 \rfloor$ and $\text{out\_swaps} \le \lfloor (m_v - 1)/2 \rfloor$. Connect $v_{\text{mid}} \to T$ `(cap = 1, cost = 0)`.
    4. Neighbor moves: $u_{\text{out}} \to v_{\text{in}}$ `(cap = \infty, cost = 1)`.
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Count how many swaps cell $v$ participates in if $k$ paths transit through $v$: $2k$ swaps if $v$ is neither a start nor a target, and $2k + 1$ swaps if $v$ is a start or target!
  - **Hint 2**: Split $v$ into three nodes $v_{\text{in}} \to v_{\text{mid}} \to v_{\text{out}}$ so incoming swaps and outgoing swaps are capacity-bounded on separate edges.
  - **Hint 3**: Inject start tokens at $S \to v_{\text{mid}}$ and extract target tokens at $v_{\text{mid}} \to T$, with capacities $\lfloor (m_v \mp 1)/2 \rfloor$ on the two half-bridges.

---

#### P23 — Multi-Shift Server Reuse & Interval Equation Differences (`Luogu P3980 [NOI2008] 志愿者招募`)
- **Judge URL**: [Luogu P3980](https://www.luogu.com.cn/problem/P3980)
- **Constraints**: $N \le 1,000$ days, $M \le 10,000$ volunteer types $[s_i, t_i]$ with cost $c_i$, daily requirement $a_d \ge 0$.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Cover a 1D demand profile $a_1, \dots, a_N$ at minimum cost using unlimited copies of weighted intervals $[s_i, t_i]$.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation (Consecutive Equality Differencing)**:
  - Introduce slack variable $y_d \ge 0$ on day $d \in \{1, \dots, N\}$ (with $a_0 = a_{N+1} = y_0 = y_{N+1} = 0$):
    $$E_d : \quad \left(\sum_{i : s_i \le d \le t_i} x_i\right) - y_d = a_d \qquad (d = 1, \dots, N).$$
  - Subtract consecutive equations $E_d - E_{d-1}$ for $d = 1, \dots, N+1$:
    $$\sum_{i : s_i = d} x_i - \sum_{i : t_i + 1 = d} x_i + y_{d-1} - y_d = a_d - a_{d-1}.$$
  - Every variable $x_i$ now appears **once with $+1$ (at $s_i$)** and **once with $-1$ (at $t_i + 1$)**, and every slack $y_d$ appears **once with $-1$ (at $d$)** and **once with $+1$ (at $d+1$)**!
  - **Compiled Graph ($N + 3$ vertices, $N + M$ arcs)**:
    - Volunteer interval $i$: arc $s_i \to t_i + 1$ `(cap = \infty, cost = c_i)`.
    - Slack variable $y_d$: reverse spine arc $d + 1 \to d$ `(cap = \infty, cost = 0)`.
    - Supply/Demand at node $d \in \{1, \dots, N+1\}$: let $\Delta_d = a_d - a_{d-1}$. If $\Delta_d > 0$, add $S \to d$ `(cap = \Delta_d, cost = 0)`; if $\Delta_d < 0$, add $d \to T$ `(cap = -\Delta_d, cost = 0)`.
- **Step 4 — Progressive Hints**:
  - **Hint 1**: In the inequality $\sum_{s_i \le d \le t_i} x_i \ge a_d$, variable $x_i$ appears in $t_i - s_i + 1$ consecutive rows. How do you make it appear in only $2$ rows?
  - **Hint 2**: Turn each inequality into an equality by subtracting a non-negative slack variable $y_d \ge 0$, then take consecutive differences $E_d - E_{d-1}$ for $d = 1 \dots N+1$.
  - **Hint 3**: Each interval $[s_i, t_i]$ becomes a forward arc $s_i \to t_i + 1$ of cost $c_i$, and each slack $y_d$ becomes a backward arc $d+1 \to d$ of cost $0$.

---

### 8.4 Tier 4: `Mastery` (`P24` – `P30`)

---

#### P24 — 2D Prefix/Suffix Coordinate Rank Translation (`AtCoder AGC 031 E — Snuke the Phantom Thief`)
- **Judge URL**: [AtCoder AGC 031E](https://atcoder.jp/contests/agc031/tasks/agc031_e)
- **Constraints**: $N \le 80$ jewels at $(x_i, y_i)$ with value $v_i \le 10^{15}$, $M \le 320$ `L/R/D/U` constraints.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Select a 2D point subset maximizing value under directional half-plane count constraints (`count(x <= a) <= b`, etc.).
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Apply the full compilation of **Section 5**:
    1. Outer loop over exact chosen cardinality $K \in \{1, \dots, N\}$.
    2. Translate `L` ($a, b$) to $L_X(b+1) \ge a+1$ and `R` ($a, b$) to $R_X(K-b) \le a-1$ (and similarly `D, U` for $Y$).
    3. Run the **Interval Monotonization Recurrences** ($L_X(p) = \max(L_X(p), L_X(p-1))$, $R_X(p) = \min(R_X(p), R_X(p+1))$). If any $L > R$, skip $K$.
    4. Build the 4-layer graph $S \to X_p \to i_{\text{in}} \xrightarrow{-v_i} i_{\text{out}} \to Y_q \to T$ and run MCMF. If max flow $= K$, update global answer with $-\text{MinCost}$.
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Fix the total number of stolen jewels $K \in \{1, \dots, N\}$. How does "at most $b$ jewels have $x \ge a$" translate into the sorted $X$-coordinates $x_{(1)} \le \dots \le x_{(K)}$?
  - **Hint 2**: It means the $(K-b)$-th smallest $X$-coordinate satisfies $x_{(K-b)} \le a - 1$! Propagate these bounds so each rank slot $p \in \{1, \dots, K\}$ has a valid interval $[L_X(p), R_X(p)]$.
  - **Hint 3**: Build a 4-layer network matching $X$-rank slots to jewels and jewels to $Y$-rank slots; by the Monotone Interval Uncrossing Theorem, any valid matching satisfies all order-statistic bounds.

---

#### P25 — 4-Hub Dual-Norm Manhattan Linearization (`AtCoder AGC 034 D — Manhattan Max Matching`)
- **Judge URL**: [AtCoder AGC 034D](https://atcoder.jp/contests/agc034/tasks/agc034_d)
- **Constraints**: $N \le 1,000$ red/blue point clusters $(x_i, y_i, c_i)$, $\sum c_i \le 10,000$.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Maximum-weight bipartite matching under 2D Manhattan distance $|x_i - x'_j| + |y_i - y'_j|$ where $N^2 = 10^6$ edges is too dense.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Apply the 4-Hub Dual-Norm Linearization of **Section 6**:
    $$|x_i - x'_j| + |y_i - y'_j| = \max_{s_1, s_2 \in \{\pm 1\}} \Big[ (s_1 x_i + s_2 y_i) + (-s_1 x'_j - s_2 y'_j) \Big].$$
  - Create $4$ hub vertices $H_{s_1, s_2}$ for $(s_1, s_2) \in \{\pm 1\}^2$.
  - Connect $S \to R_i$ `(cap = c_i, cost = 0)`, $R_i \to H_{s_1, s_2}$ `(cap = \infty, cost = -(s_1 x_i + s_2 y_i))`, $H_{s_1, s_2} \to B_j$ `(cap = \infty, cost = -(-s_1 x'_j - s_2 y'_j))`, and $B_j \to T$ `(cap = d_j, cost = 0)`.
  - Run MCMF on $2N + 6 \le 2,006$ vertices and $10N \le 10,000$ edges; output $-\text{MinCost}$.
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Rewrite $|x_i - x'_j| + |y_i - y'_j|$ as the maximum of $4$ linear expressions without absolute values.
  - **Hint 2**: Since we are **maximizing** total distance, replacing the edge $R_i \to B_j$ with $4$ parallel paths through sign hubs $H_{\pm 1, \pm 1}$ is exact.
  - **Hint 3**: Connect every red cluster to the $4$ hubs and the $4$ hubs to every blue cluster, reducing $O(N^2)$ edges to $8N$ edges.

---

#### P26 — Time-Expanded Quadratic Congestion Flow with Lazy Parallel Edges (`CF 1187 G — Gang Up`)
- **Judge URL**: [Codeforces 1187G](https://codeforces.com/problemset/problem/1187/G)
- **Constraints**: $N \le 50$ vertices, $M \le 50$ undirected edges, $K \le 50$ agents, linear time penalty $c$, quadratic edge congestion penalty $d \cdot f_e^2$.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Route $K$ agents across a graph over discrete time steps $t = 0, 1, 2, \dots$ to reach vertex $1$, paying $c \cdot t$ per agent arrival time plus $d \cdot k^2$ whenever $k$ agents traverse the same directed edge at the same time step.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  - Time horizon bound: $T_{\max} = N + K \le 100$. Build time-layered vertices $(v, t)$ for $v \in \{1, \dots, N\}$ and $t \in \{0, \dots, T_{\max}\}$.
  - Waiting at vertex $v$: $(v, t) \to (v, t+1)$ `(cap = \infty, cost = 0)` (or cost $c$, if we charge $+c$ per step before reaching $1$).
  - Reaching destination $1$: $(1, t) \to T_{\text{sink}}$ `(cap = \infty, cost = c \cdot t)`.
  - **Quadratic Edge Congestion $d \cdot k^2$**: Since $k^2 - (k-1)^2 = 2k - 1$, replace each directed edge $(u, t) \to (v, t+1)$ with $K$ parallel unit-capacity arcs (or spawn them lazily as in Section 3.2!) with marginal costs:
    $$\text{Arc } k \in \{1, \dots, K\}: \quad (u, t) \to (v, t+1) \quad \text{with } (\text{cap} = 1, \text{cost} = (2k - 1) \cdot d).$$
- **Step 4 — Progressive Hints**:
  - **Hint 1**: What is the maximum time step any agent ever needs to reach vertex $1$? At most $N + K \le 100$.
  - **Hint 2**: How do you linearize the convex edge cost $d \cdot k^2$ for integer flow $k \in \{0, 1, \dots, K\}$?
  - **Hint 3**: Use the odd-number difference identity $k^2 = \sum_{r=1}^k (2r - 1)$: add unit-capacity parallel arcs of cost $d, 3d, 5d, \dots, (2K-1)d$ (or spawn the $(r+1)$-th arc lazily when the $r$-th arc saturates!).

---

#### P27 — Extreme-Scale Napkin Plan via Convexity + Monotone Deque Simulation (`Luogu P4480 [BJWC2018] 餐巾计划问题`)
- **Judge URL**: [Luogu P4480](https://www.luogu.com.cn/problem/P4480)
- **Constraints**: $N \le 2 \times 10^5$ days, daily demands $r_t \le 10^6$, $p, f, s \le 10^4$.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Exact same problem as `P05 (餐巾计划问题)`, but $N \le 2 \times 10^5$ and $\sum r_t \le 2 \times 10^{11}$ make explicit MCMF impossible (**Direction B Bridge**).
- **Step 2 & Step 3 — Algebraic-to-Greedy Deque Compilation**:
  - Apply the **Convexity + Two-Pointer Monotone Deque** reduction of **Section 4.2**:
    1. Ternary search over the total number of fresh napkins $B \in [\max \text{early\_need}, \sum_{t=1}^N r_t]$ purchased across the entire horizon.
    2. For a fixed $B$ (all available on Day 1 since clean storage is free), simulate $t = 1 \dots N$ in $O(N)$ time using a deque of dirty napkin batches $(s, \text{cnt})$:
       - First consume remaining initial clean stock from $B$ (cost $0$).
       - Next, consume **oldest** dirty batches with $s \le t - d_{\text{slow}}$ via cheap **slow laundry** (`FIFO` from front of slow pool, cost $c_{\text{slow}}$).
       - Finally, if demand remains, consume **newest** dirty batches in $t - d_{\text{slow}} < s \le t - d_{\text{fast}}$ via expensive **fast laundry** (`LIFO` from back of fast pool, cost $c_{\text{fast}}$) so older dirty batches survive to mature into the slow-laundry window on future days!
  - Total complexity: $O(N \log(\sum r_t))$.
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Why is the minimum total cost $F(B)$ a convex function of the total number of fresh napkins $B$ bought?
  - **Hint 2**: Because $B$ is just the flow on the purchase edge $S \to Y_1$ in the MCMF network, and the min-cost flow value is always convex in any edge's flow!
  - **Hint 3**: For a fixed $B$, sweep days $1 \dots N$: use slow laundry in FIFO order ($s \le t - d_{\text{slow}}$) and fast laundry in LIFO order ($t - d_{\text{slow}} < s \le t - d_{\text{fast}}$).

---

#### P28 — Parametric MCMF Slope Envelope & LP Duality (`CF 1307 G — Cow and Exercise`)
- **Judge URL**: [Codeforces 1307G](https://codeforces.com/problemset/problem/1307/G)
- **Constraints**: $N \le 50$ vertices, $M \le 2,500$ directed edges with lengths $w_e \ge 1$, $Q \le 10^5$ queries $x_q \in [0, 10^5]$.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Given a budget $x$ to increase edge weights ($\sum \Delta_e \le x$, $\Delta_e \ge 0$), **maximize** the shortest path distance from $1$ to $N$. Answer $Q = 10^5$ queries for different $x$.
- **Step 2 & Step 3 — LP Duality to Parametric Unit-Capacity MCMF**:
  - The primal LP for a fixed budget $x$ maximizes $d_N - d_1$ subject to $d_v - d_u \le w_e + \Delta_e$ and $\sum \Delta_e \le x$.
  - Taking the LP Dual (or viewing via Menger/Min-Cut): increasing the length of $k$ edge-disjoint paths from $1$ to $N$ of total base weight $C_k$ by $+L$ requires at least $k \cdot L$ budget! Conversely, by LP strong duality:
    $$\text{MaxShortestPath}(x) = \min_{k \ge 1} \frac{C_k + x}{k},$$
    where $C_k$ is the minimum cost of a flow of volume $k$ in the network where every original edge $e = (u, v)$ has **`(cap = 1, cost = w_e)`**!
  - Run SSP from $1$ to $N$ once (at most $N \le 50$ unit augmentations), recording the sequence of pairs $(k, C_k)$ after each shortest augmenting path. Answer each query $x_q$ in $O(N)$ (or $O(\log N)$ via lower hull) by evaluating $\min_{1 \le k \le F_{\max}} \frac{C_k + x_q}{k}$!
- **Step 4 — Progressive Hints**:
  - **Hint 1**: Write the LP that maximizes $d_N$ subject to $d_v - d_u - \Delta_e \le w_e$ and $\sum \Delta_e \le x$, and take its dual!
  - **Hint 2**: The dual variables $f_e \in [0, 1]$ form a flow of value $k$ from $1$ to $N$ in the unit-capacity network, giving the exact duality formula $\min_{k \ge 1} (C_k + x) / k$.
  - **Hint 3**: Run SSP once on the graph with `(cap = 1, cost = w_e)` to collect $(k, C_k)$ for all $1 \le k \le F_{\max}$, then answer each query in $O(F_{\max})$ time.

---

#### P29 — Direction B Bridge: Eliminating 3-Group MCMF via Regret Heaps (`AtCoder AGC 018 C — Coins`)
- **Judge URL**: [AtCoder AGC 018C](https://atcoder.jp/contests/agc018/tasks/agc018_c)
- **Constraints**: $X + Y + Z = N \le 10^5$ people, each person $i$ has $(A_i, B_i, C_i)$ gold/silver/bronze coins. Choose $X$ people to give gold, $Y$ to give silver, $Z$ to give bronze to maximize total coins.
- **Step 1 — Diagnostic Signal**:
  - **Signal**: $K = 3$ group assignment with $N = 10^5$ items (too large for explicit $O(N)$ MCMF, requiring a **Direction B** coordinate-shift + heap reduction).
- **Step 2 & Step 3 — Algebraic Coordinate Shift & Prefix/Suffix Split**:
  - Subtract $C_i$ from every person: assume everyone initially gives Bronze ($\text{Base} = \sum_{i=1}^N C_i$). Now choosing person $i$ for Gold gives net gain $a'_i = A_i - C_i$, choosing Silver gives net gain $b'_i = B_i - C_i$, and Bronze gives $0$.
  - Sort all $N$ people in descending order of $a'_i - b'_i = A_i - B_i$.
  - **Exchange Argument (Uncrossing)**: In the sorted order $1 \dots N$, every person chosen for Gold (`A`) must appear **to the left** of every person chosen for Silver (`B`)! (If person $i < j$ had Silver and $j$ had Gold, swapping them changes the sum by $(A_i - B_i) - (A_j - B_j) \ge 0$.)
  - Therefore, there exists a split index $k \in \{X, X+1, \dots, N - Y\}$ such that:
    - All $X$ Gold people are chosen from the prefix $1 \dots k$ (picking the $X$ largest $a'_i = A_i - C_i$ via a min-heap of size $X$).
    - All $Y$ Silver people are chosen from the suffix $k+1 \dots N$ (picking the $Y$ largest $b'_i = B_i - C_i$ via a min-heap of size $Y$).
  - Sweep $k$ in $O(N \log N)$ time!
- **Step 4 — Progressive Hints**:
  - **Hint 1**: This is a bipartite MCMF with $N = 10^5$ left nodes and $3$ right nodes of capacities $(X, Y, Z)$. How do you eliminate the 3rd node $Z$?
  - **Hint 2**: Pre-assign everyone to $Z$ (Bronze) and replace $(A_i, B_i, C_i)$ with $(A_i - C_i, B_i - C_i, 0)$.
  - **Hint 3**: Sort by $(A_i - C_i) - (B_i - C_i) = A_i - B_i$ so the $X$ Gold picks and $Y$ Silver picks are separated by a clean prefix/suffix boundary $k \in [X, N-Y]$, then maintain two priority queues of sizes $X$ and $Y$.

---

#### P30 — 3D Manhattan–Chebyshev Hub Matching with Lazy Convex Degree Penalties & Cycle-Cover Synthesis (`Grandmaster Synthesis` / `CF 387 D` / `QOJ Multi-Hub`)
- **Judge Coordinates & Synthesis Sources**: Synthesized from `AGC 034 D` (3D $\ell_1^3$ / $\ell_\infty^d$ extension), `Luogu P2050` (Lazy Convex Penalties), and [CF 387D — George and Interesting Graph](https://codeforces.com/problemset/problem/387/D).
- **Constraints**: $N, M \le 1,500$ supply/demand nodes in $\mathbb{R}^3$, total matched pairs $K \le 2,000$, node $i$ pays convex congestion penalty $a_i d_i^2$ for matching $d_i$ units, edge $(i, j)$ earns $\ell_1^3$ reward $|x_i - x'_j| + |y_i - y'_j| + |z_i - z'_j|$ (or $\ell_\infty^d$ reward $\max_{k=1}^d |p_{i,k} - q_{j,k}|$).
- **Step 1 — Diagnostic Signal**:
  - **Signal**: Combines dense geometric matching ($O(NM)$ pairs) with non-linear convex degree penalties $a_i d_i^2$.
- **Step 2 & Step 3 — Algebraic-to-Graph Compilation**:
  1. **Geometric Hub Layer**:
     - For $\ell_1^3$: create **$2^3 = 8$ sign hubs** $H_{s_1, s_2, s_3}$ ($s_k \in \{\pm 1\}$) with $R_i \to H_\sigma$ `(cap = \infty, cost = -\langle \sigma, p_i \rangle)` and $H_\sigma \to B_j$ `(cap = \infty, cost = -\langle -\sigma, q_j \rangle)`.
     - For $\ell_\infty^d$: create **$2d$ axis-sign hubs** $H_{k, s}$ ($k \in \{1, \dots, d\}, s \in \{\pm 1\}$) with $R_i \to H_{k,s}$ `(cap = \infty, cost = -s \cdot p_{i,k})` and $H_{k,s} \to B_j$ `(cap = \infty, cost = s \cdot q_{j,k})`.
  2. **Lazy Convex Degree Penalty Layer**:
     - Since $a_i d_i^2 - a_i (d_i - 1)^2 = (2d_i - 1) a_i$ is strictly increasing in $d_i$, initially add only the $d_i = 1$ arc $S \to R_i$ with `(cap = 1, cost = a_i)` (and similarly $B_j \to T$ with `(cap = 1, cost = b_j)`).
     - Whenever the $r$-th degree arc on $R_i$ (or $B_j$) saturates during a unit augmentation, lazily spawn the $(r+1)$-th arc with `(cap = 1, cost = (2r + 1) a_i)`!
- **Step 4 — Progressive Hints**:
  - **Hint 1**: How many sign hubs are needed for 3D Manhattan distance $\ell_1^3$ vs. $d$-dimensional Chebyshev distance $\ell_\infty^d$? Exactly $2^3 = 8$ for $\ell_1^3$, and $2d$ for $\ell_\infty^d$!
  - **Hint 2**: How do you incorporate the quadratic degree penalty $a_i d_i^2$ at vertex $R_i$ without creating $K$ parallel edges at every vertex upfront?
  - **Hint 3**: Use marginal differences $(2r - 1)a_i$ and spawn the $(r+1)$-th supply arc $S \to R_i$ lazily only when the $r$-th arc is saturated.

---

### 8.5 Reconciled Quarantined Template Problems Table (`R-01` – `R-12`)

The following 12 problems from Cohort 1 and Cohort 2 are **quarantined** because they are direct, un-disguised textbook templates with zero non-trivial algebraic or structural compilation steps:

| Quarantine ID | Problem Title & Judge Coordinates | Reason for Quarantine |
| :--- | :--- | :--- |
| **R-01** | `Luogu P3381` — 【模板】最小费用最大流 | Bare MCMF API verification; zero modelling. |
| **R-02** | `LOJ #102` — 最小费用流 | Bare MCMF API verification; zero modelling. |
| **R-03** | `Luogu P4014` — [网络流24题] 分配问题 | Direct unweighted/weighted complete bipartite assignment $K_{N,N}$. |
| **R-04** | `CSES 2129` — Task Assignment | Direct $N \times N$ bipartite min-cost perfect matching template. |
| **R-05** | `Library Checker` — Assignment Problem | Direct Hungarian / MCMF bipartite assignment template. |
| **R-06** | `POJ 2195` — Going Home | Small $N \le 100$ explicit $O(N^2)$ bipartite matching where hub linearization is unnecessary. |
| **R-07** | `Luogu P4015` — [网络流24题] 运输问题 | Direct textbook Hitchcock transportation problem ($S \to A_i \to B_j \to T$). |
| **R-08** | `Luogu P3376` — 【模板】网络最大流 | Pure max-flow template without costs. |
| **R-09** | `Luogu P2756` — 飞行员配对方案问题 | Unweighted bipartite matching template. |
| **R-10** | `Luogu P2763` — 试题库问题 | Unweighted $b$-matching template without costs. |
| **R-11** | `Luogu P2764` — 最小路径覆盖问题 | Unweighted DAG minimum path cover template (subsumed by weighted `P04` and `P12`). |
| **R-12** | `Luogu P2762` — 太空飞行计划问题 | Pure s-t min-cut project selection (covered in Wave 2). |

---

## 9. Unified Multilingual Bibliography (`[EN]`, `[ZH]`, `[JA]`)

1. **[EN] Suurballe, J. W. (1974)**, *"Disjoint paths in a network"*, Networks, 4(2), 125–145; **Suurballe, J. W., & Tarjan, R. E. (1984)**, *"A quick method for finding shortest pairs of disjoint paths"*, Networks, 14(2), 325–336. (Foundational potential re-weighting and residual path-uncrossing theory for Section 2.1.)
2. **[EN] Fortune, S., Hopcroft, J., & Wyllie, J. (1980)**, *"The directed subgraph homeomorphism problem"*, Theoretical Computer Science, 10(2), 111–121. (Proves NP-completeness of asymmetric vertex-disjoint $(s \to t)$ and $(t \to s)$ round trips in general directed graphs.)
3. **[EN] Edmonds, J., & Johnson, E. L. (1973)**, *"Matching, Euler tours and the Chinese postman"*, Mathematical Programming, 5(1), 88–124. (Establishes the $T$-join and odd-set Blossom polytope theory for Undirected CPP and general $b$-matchings in Sections 2.3–2.4.)
4. **[EN] Papadimitriou, C. H. (1976)**, *"On the complexity of edge traversing"*, Journal of the ACM, 23(3), 544–554. (Proves NP-completeness of Mixed Chinese Postman while Eulerian orientation of mixed graphs with even degree parity reduces to network flow.)
5. **[EN] Orlin, J. B. (1993)**, *"A faster strongly polynomial minimum cost flow algorithm"*, Operations Research, 41(2), 338–350; **Ahuja, R. K., Magnanti, T. L., & Orlin, J. B. (1993)**, *Network Flows: Theory, Algorithms, and Applications*, Prentice Hall. (Canonical reference for consecutive equality differencing $E_t - E_{t-1}$ and LP duality in Sections 4 and 8.)
6. **[ZH] 胡伯涛 (Amber / Hu Botao, 2007)**, 《最小割模型在信息学竞赛中的应用》 & **刘汝佳 (Liu Rujia, 2012)**, 《算法竞赛入门经典：训练指南》 (*AOAPC II: Training Guide*). (Canonical Chinese OI references on vertex/edge splitting, lower-bound circulations, and `网络流 24 题`.)
7. **[ZH] NOI 2012 命题报告 & 国家集训队论文 (2012)**, 《[NOI2012] 美食节 — 动态加点费用流》 (*Dynamic Lazy Vertex Generation in Min-Cost Flow*). (Establishes the Frontier Slot Dominance Theorem and inline vertex spawning for reverse-indexed completion time scheduling in Section 3.)
8. **[ZH] 姜志豪 (Jiang Zhihao, 2016)**, 《网络流的一些建模方法》 (*中國國家集訓隊論文 2016*) & **高睿泉 (Gao Ruiquan, 2018)**, 《浅谈保序回归问题》 / **王修涵 (Wang Xiuhan, 2019)**, 《浅谈模拟费用流问题》. (Bridges Direction A MCMF compilations to Direction B greedy regret-heap and monotone-deque simulations such as `[BJWC2018] 餐巾计划问题` and `AGC 018 C`.)
9. **[JA] AtCoder Grand Contest 031 Editorial (2019)**, *"AGC 031 E — Snuke the Phantom Thief"*, & **maspy (`maspypy`)**, *"AGC031E 解説 — 最小費用流・マトロイド交差"*. (Establishes fixed-$K$ order-statistic coordinate rank translation, interval monotonization, and the 2-Matroid Intersection interpretation in Sections 5 and 7.1.)
10. **[JA] AtCoder Grand Contest 034 Editorial (2019)**, *"AGC 034 D — Manhattan Max Matching"*, & **noshi91 / tatyam**, *"マンハッタン距離・チェビシェフ距離の超頂点テク (Hub Vertex Sparsification for $\ell_1^d$ and $\ell_\infty^d$ Metrics)"*. (Establishes the $2^d$-hub $\ell_1^d$ and $2d$-hub $\ell_\infty^d$ dual-norm linearizations in Section 6.)

---

## 10. Deep Verification Appendix: Hand-Checkable Numerical Traces & Broken-Gadget Stress Tests for Advanced & Mastery Archetypes

To ensure that every advanced and mastery compilation in Section 8 can be hand-verified and stress-tested during contest implementation, this appendix provides complete numerical traces ($N \le 4$), residual augmentation logs, and broken-gadget proofs for the flagship problems of Wave 4A.

---

### 10.1 Trace A: Fleet Bounded-Start DAG Path Cover & Precedence-Locked Tours (`P12 Catering` & `P17 [ZJOI2011] 营救皮卡丘`)

#### Concrete Numerical Instance ($N = 3$ Bases, Fleet Size $K = 2$)
Suppose we have depot $0$ and $N = 3$ bases $\{1, 2, 3\}$ with precedence locks ($v$ unlocked only after $1 \dots v-1$), and raw undirected edges:
- $\{0, 1\}$ weight $4$
- $\{0, 3\}$ weight $2$
- $\{3, 2\}$ weight $2$
- $\{1, 2\}$ weight $10$
- $\{2, 3\}$ is the same as $\{3, 2\}$ (weight $2$).

1. **Why Unrestricted Floyd–Warshall Gives the Wrong Answer**:
   - In the unrestricted graph, the shortest path from $0$ to $2$ is $0 \xrightarrow{2} 3 \xrightarrow{2} 2$ of length $4$, passing through intermediate vertex $3 > 2$.
   - However, when Base $2$ is first unlocked, Base $3$ is **still locked**! A team moving to unlock Base $2$ is forbidden from transiting through Base $3$.
2. **Restricted Floyd–Warshall ($k \le \max(u, v)$) Trace**:
   - **Phase $k = 0$**: $d^{(0)}(0, 1) = 4$, $d^{(0)}(0, 2) = \infty$, $d^{(0)}(0, 3) = 2$.
   - **Phase $k = 1$**:
     - For $(0, 2)$ ($\max = 2 \ge 1$): $d^{(1)}(0, 2) = \min(\infty, d(0,1) + d(1,2)) = 4 + 10 = 14$.
     - For $(1, 2)$ ($\max = 2 \ge 1$): $d^{(1)}(1, 2) = 10$.
   - **Phase $k = 2$**:
     - For $(1, 3)$ ($\max = 3 \ge 2$): $d^{(2)}(1, 3) = d(1, 2) + d(2, 3) = 10 + 2 = 12$.
   - **Phase $k = 3$**:
     - Since $k = 3 > \max(0, 2) = 2$, pair $(0, 2)$ is **not updated** via $k = 3$!
   - Final restricted DAG weights $D(u, v)$ for $u < v$:
     - $D(0, 1) = 4, \quad D(0, 2) = 14, \quad D(0, 3) = 2$,
     - $D(1, 2) = 10, \quad D(1, 3) = 12, \quad D(2, 3) = 2$.
3. **MCMF Augmentation Trace ($K = 2$ teams, Required Flow $F = N = 3$ into $T$)**:
   - **Augmentation 1**: $S \to 0_{\text{out}} \xrightarrow{2} 3_{\text{in}} \to T$ (cost $+2$, uses $1$ of $K=2$ starts at $0_{\text{out}}$).
   - **Augmentation 2**: $S \to 0_{\text{out}} \xrightarrow{4} 1_{\text{in}} \to T$ (cost $+4$, saturates $S \to 0_{\text{out}}$ capacity $K = 2$).
   - **Augmentation 3**: Now $2_{\text{in}}$ must be satisfied, and $S \to 0_{\text{out}}$ is full! Compare the two residual ways to reach $2_{\text{in}}$:
     - **Option A (Extend from $1_{\text{out}}$)**: $S \to 1_{\text{out}} \xrightarrow{10} 2_{\text{in}} \to T$ (cost $+10$).
     - **Option B (Reassign $0_{\text{out}} \to 3_{\text{in}}$ and extend $2_{\text{out}} \to 3_{\text{in}}$)**:
       $$S \to 2_{\text{out}} \xrightarrow{+2} 3_{\text{in}} \xrightarrow{-2} 0_{\text{out}} \xrightarrow{+14} 2_{\text{in}} \to T \quad (\text{cost } 2 - 2 + 14 = +14).$$
   - The solver chooses **Option A** (cost $+10$), giving total cost $2 + 4 + 10 = 16$:
     - Team 1: $0 \xrightarrow{4} 1 \xrightarrow{10} 2$ (cost $14$)
     - Team 2: $0 \xrightarrow{2} 3$ (cost $2$).

---

### 10.2 Trace B: Persistent Next-Occurrence Relay Hubs (`P19 CF 818 G — Four Melodies`)

#### Concrete Numerical Instance ($N = 4, K = 2$, Array $a = [10, 3, 17, 4]$)
Notice that $10 \equiv 3 \equiv 17 \pmod 7$ (all have residue $3 \pmod 7$), and $|3 - 4| = 1$.
1. **Why Direct Linking Creates Quadratic Edges**:
   In an array of $N$ elements all congruent to $3 \pmod 7$, direct linking adds $\binom{N}{2}$ edges.
2. **Relay Chain Trace**:
   - $\text{next\_mod}(1) = 2$, $\text{next\_mod}(2) = 3$, $\text{next\_mod}(3) = \text{none}$.
   - $\text{next\_plus}(2) = 4$ ($a_4 = 4 = a_2 + 1$).
   - The $\bmod 7$ relay chain is $H_1^{\text{mod}} \xrightarrow{(K, 0)} H_2^{\text{mod}} \xrightarrow{(K, 0)} H_3^{\text{mod}}$, with unit-capacity drop-offs $H_i^{\text{mod}} \xrightarrow{(1, 0)} i_{\text{in}}$.
   - Element $1_{\text{out}}$ connects only to $H_2^{\text{mod}}$. A flow token leaving $1_{\text{out}}$ can either drop into $2_{\text{in}}$ (forming $10 \to 3$) **or** slide along $H_2^{\text{mod}} \to H_3^{\text{mod}} \to 3_{\text{in}}$ (forming $10 \to 17$), while a second token can use $2_{\text{out}} \to H_4^{\text{val}} \to 4_{\text{in}}$ (forming $3 \to 4$)!
   - For $K = 2$, the optimal 2-melody cover decomposes into $(a_1=10 \to a_3=17)$ and $(a_2=3 \to a_4=4)$, covering all $4$ elements!

---

### 10.3 Trace C: Boolean Lattice Path Cover with Reset Savings (`P21 CF 1510 B — Button Lock`)

#### Concrete Numerical Instance ($d = 3$ bits, Target Masks $\{ \mathtt{001}_2, \mathtt{011}_2, \mathtt{101}_2 \}$)
1. **Upfront Baseline**:
   If every mask $u$ were visited by starting at $\mathtt{000}_2$, pressing its 1-bits, and pressing `R`:
   - $u_1 = \mathtt{001}_2$ ($\text{popcount} = 1$): baseline cost $1 + 1 = 2$.
   - $u_2 = \mathtt{011}_2$ ($\text{popcount} = 2$): baseline cost $2 + 1 = 3$.
   - $u_3 = \mathtt{101}_2$ ($\text{popcount} = 2$): baseline cost $2 + 1 = 3$.
   - Sum of baselines $= 2 + 3 + 3 = 8$, minus $1$ (last chain omits `R`) $= 7$.
2. **Strict Superset Transitions ($u \subsetneq v$)**:
   - $u_1 = \mathtt{001}_2 \subsetneq u_2 = \mathtt{011}_2$: edge $u_{1,\text{out}} \to u_{2,\text{in}}$ of saving cost $-(\text{popcount}(u_1) + 1) = -2$.
   - $u_1 = \mathtt{001}_2 \subsetneq u_3 = \mathtt{101}_2$: edge $u_{1,\text{out}} \to u_{3,\text{in}}$ of saving cost $-2$.
   - Note that $u_1,\text{out}$ has capacity $1$, so it can merge into **either** $u_2$ **or** $u_3$, not both!
3. **Result**:
   - Max saving is $-2$ (say $u_1 \to u_2$). Total button presses $= 7 - 2 = 5$:
     - Press bit $0$ ($\mathtt{001}_2$), press bit $1$ ($\mathtt{011}_2$), press `R` ($\mathtt{000}_2$), press bits $0, 2$ ($\mathtt{101}_2$) $\implies 1 + 1 + 1 + 2 = 5$ presses!

---

### 10.4 Trace D: Parity-Aware 3-Node Vertex Splitting (`P22 [CQOI2012] 交换棋子`)

#### Concrete Numerical Instance ($1 \times 3$ Grid: Cell $1$ has a token, Cell $3$ is the target)
- Initial state: `[1, 0, 0]`, Target state: `[0, 0, 1]`.
- Swap limits: $m_1 = 1$, $m_2 = 2$, $m_3 = 1$.
1. **Why 2-Node Splitting Fails**:
   - Moving the token $1 \to 2 \to 3$ requires two swaps: Swap$(1, 2)$ and Swap$(2, 3)$.
   - Cell $1$ participates in $1$ swap; Cell $2$ participates in **$2$ swaps** (incoming $1 \to 2$ and outgoing $2 \to 3$); Cell $3$ participates in $1$ swap.
   - If we gave each cell capacity $\lfloor m_v / 2 \rfloor$, Cell $1$ and Cell $3$ would get capacity $\lfloor 1 / 2 \rfloor = 0$, blocking the flow completely! If we gave each cell capacity $m_v$, Cell $2$ with $m_2 = 1$ would wrongly allow a token to transit through Cell $2$ (which actually costs $2$ swaps on Cell $2$).
2. **3-Node Split $(v_{\text{in}}, v_{\text{mid}}, v_{\text{out}})$ Capacities**:
   - **Cell 1 (Start: $\text{init}=1, \text{target}=0, m_1 = 1$)**:
     - $\text{cap}(1_{\text{in}} \to 1_{\text{mid}}) = \lfloor (1 - 1)/2 \rfloor = 0$.
     - $\text{cap}(1_{\text{mid}} \to 1_{\text{out}}) = \lfloor (1 + 1)/2 \rfloor = 1$.
     - Supply injected at $S \to 1_{\text{mid}}$ (`cap = 1`).
   - **Cell 2 (Transit: $\text{init}=0, \text{target}=0, m_2 = 2$)**:
     - $\text{cap}(2_{\text{in}} \to 2_{\text{mid}}) = \lfloor 2 / 2 \rfloor = 1$.
     - $\text{cap}(2_{\text{mid}} \to 2_{\text{out}}) = \lfloor 2 / 2 \rfloor = 1$.
   - **Cell 3 (Target: $\text{init}=0, \text{target}=1, m_3 = 1$)**:
     - $\text{cap}(3_{\text{in}} \to 3_{\text{mid}}) = \lfloor (1 + 1)/2 \rfloor = 1$.
     - $\text{cap}(3_{\text{mid}} \to 3_{\text{out}}) = \lfloor (1 - 1)/2 \rfloor = 0$.
     - Demand extracted at $3_{\text{mid}} \to T$ (`cap = 1`).
   - **Unique Feasible Path**:
     $$S \to 1_{\text{mid}} \xrightarrow{\text{cap } 1} 1_{\text{out}} \xrightarrow{\text{cost } 1} 2_{\text{in}} \xrightarrow{\text{cap } 1} 2_{\text{mid}} \xrightarrow{\text{cap } 1} 2_{\text{out}} \xrightarrow{\text{cost } 1} 3_{\text{in}} \xrightarrow{\text{cap } 1} 3_{\text{mid}} \to T,$$
     achieving exact cost $2$ swaps while respecting all parity-dependent swap budgets!

---

### 10.5 Trace E: Consecutive Equality Differencing (`P23 [NOI2008] 志愿者招募`)

#### Concrete Numerical Instance ($N = 3$ Days, Demands $a = [2, 3, 1]$)
- Volunteer Type 1: covers $[1, 2]$ at cost $c_1 = 4$.
- Volunteer Type 2: covers $[2, 3]$ at cost $c_2 = 5$.
- Volunteer Type 3: covers $[1, 3]$ at cost $c_3 = 6$.
1. **Original Inequality System (With Slack $y_d \ge 0$)**:
   $$\begin{aligned}
   E_0 &: & 0 &= 0 \\
   E_1 &: & x_1 + x_3 - y_1 &= 2 \\
   E_2 &: & x_1 + x_2 + x_3 - y_2 &= 3 \\
   E_3 &: & x_2 + x_3 - y_3 &= 1 \\
   E_4 &: & 0 &= 0
   \end{aligned}$$
2. **Consecutive Differences $\Delta E_d = E_d - E_{d-1}$ ($d = 1, 2, 3, 4$)**:
   $$\begin{aligned}
   \text{Node } 1 \;(E_1 - E_0) &: & +x_1 + x_3 - y_1 &= +2 \quad (\text{Supply } S \to 1 \text{ of } 2) \\
   \text{Node } 2 \;(E_2 - E_1) &: & +x_2 + y_1 - y_2 &= +1 \quad (\text{Supply } S \to 2 \text{ of } 1) \\
   \text{Node } 3 \;(E_3 - E_2) &: & -x_1 + y_2 - y_3 &= -2 \quad (\text{Demand } 3 \to T \text{ of } 2) \\
   \text{Node } 4 \;(E_4 - E_3) &: & -x_2 - x_3 + y_3 &= -1 \quad (\text{Demand } 4 \to T \text{ of } 1)
   \end{aligned}$$
3. **Compiled Arcs & Optimal Flow**:
   - $x_1$: arc $1 \to 3$ `(cap = \infty, cost = 4)`
   - $x_2$: arc $2 \to 4$ `(cap = \infty, cost = 5)`
   - $x_3$: arc $1 \to 4$ `(cap = \infty, cost = 6)`
   - Slacks $y_1, y_2, y_3$: backward arcs $2 \to 1, 3 \to 2, 4 \to 3$ `(cap = \infty, cost = 0)`.
   - **Optimal Flow of Volume $3$**:
     - Send $2$ units along $S \to 1 \xrightarrow{x_1, \text{cost } 4} 3 \to T$ (cost $2 \times 4 = 8$).
     - Send $1$ unit along $S \to 2 \xrightarrow{x_2, \text{cost } 5} 4 \to T$ (cost $1 \times 5 = 5$).
     - Wait—can we do better using $x_3$ ($1 \to 4$, cost $6$) and backward slack $y_1$ ($2 \to 1$, cost $0$)?
       - Send $1$ unit along $S \to 2 \xrightarrow{y_1, \text{cost } 0} 1 \xrightarrow{x_3, \text{cost } 6} 4 \to T$ (cost $6$ instead of $5$, which is worse).
     - Thus $x_1 = 2, x_2 = 1, x_3 = 0$ is optimal with cost $8 + 5 = 13$, covering demands $[2, 2+1, 1] = [2, 3, 1]$!

---

### 10.6 Trace F: Parametric MCMF Slope Envelope (`P28 CF 1307 G — Cow and Exercise`)

#### Concrete Numerical Instance ($N = 4$ Diamond Graph)
- Edges: $1 \to 2$ (cost $1$), $2 \to 4$ (cost $1$), $1 \to 3$ (cost $2$), $3 \to 4$ (cost $2$), and middle bridge $2 \to 3$ (cost $0$), each with unit capacity `cap = 1`.
1. **Successive Shortest Path (SSP) Profile $(k, C_k)$**:
   - **Step $k = 1$**: Shortest path is $1 \xrightarrow{1} 2 \xrightarrow{0} 3 \xrightarrow{2} 4$? Wait: $1 \to 2 \to 4$ has cost $1 + 1 = 2$. So $k = 1$ has $C_1 = 2$.
   - **Step $k = 2$**: Second path is $1 \xrightarrow{2} 3 \xrightarrow{2} 4$ of cost $4$. Total cost for $k = 2$ is $C_2 = 2 + 4 = 6$.
   - Max flow is $F_{\max} = 2$.
2. **Query Evaluation $\text{Ans}(x) = \min_{k \in \{1, 2\}} \frac{C_k + x}{k}$**:
   - For $k = 1$: $\frac{2 + x}{1} = 2 + x$.
   - For $k = 2$: $\frac{6 + x}{2} = 3 + 0.5 x$.
   - Crossover point: $2 + x = 3 + 0.5 x \iff x = 2$.
   - For $x \in [0, 2]$, the budget is spent entirely on path $1 \to 2 \to 4$, giving shortest path $2 + x$.
   - For $x > 2$, once $1 \to 2 \to 4$ is stretched to length $4$, any excess budget $x - 2$ must be split equally ($0.5$ each) across both disjoint paths $1 \to 2 \to 4$ and $1 \to 3 \to 4$, giving shortest path $3 + 0.5 x$!

---

### 10.7 Trace G: Direction B Monotone-Deque Simulation (`P27 [BJWC2018] 餐巾计划问题`)

#### Concrete Numerical Instance ($N = 4$ Days, Demands $r = [3, 2, 4, 3]$)
- Fresh purchase price $p = 10$.
- Fast laundry: $d_{\text{fast}} = 1$ day, cost $c_{\text{fast}} = 6$.
- Slow laundry: $d_{\text{slow}} = 2$ days, cost $c_{\text{slow}} = 3$.
1. **Why FIFO Slow + LIFO Fast Is Mandatory**:
   Suppose we test trial purchase volume $B = 5$ fresh napkins (cost $5 \times 10 = 50$).
   - **Day $t = 1$ ($r_1 = 3$)**:
     - Consume $3$ fresh napkins from $B$ (remaining clean stock $= 5 - 3 = 2$).
     - Push dirty batch $(s=1, \text{cnt}=3)$ into the dirty deque $Q = [(1, 3)]$.
   - **Day $t = 2$ ($r_2 = 2$)**:
     - Consume remaining $2$ fresh napkins from $B$ (remaining clean stock $= 0$).
     - Push dirty batch $(s=2, \text{cnt}=2)$ into $Q = [(1, 3), (2, 2)]$.
   - **Day $t = 3$ ($r_3 = 4$)**:
     - Clean stock $= 0$.
     - **Tier 1 (Slow Laundry, $s \le 3 - 2 = 1$)**: Batch $(1, 3)$ has matured into the slow-laundry window! Wash all $3$ units of $(1, 3)$ via slow laundry at cost $3 \times 3 = 9$. Deficit remaining on Day 3 is $4 - 3 = 1$.
     - **Tier 2 (Fast Laundry, $1 < s \le 3 - 1 = 2$)**: Batch $(2, 2)$ is in the fast-laundry window. Wash $1$ unit from the **back (LIFO)** of $(2, 2)$ via fast laundry at cost $1 \times 6 = 6$, leaving $(2, 1)$ in $Q$.
     - Push Day 3's dirty napkins $(3, 4)$ into $Q = [(2, 1), (3, 4)]$.
   - **Day $t = 4$ ($r_4 = 3$)**:
     - **Tier 1 (Slow Laundry, $s \le 4 - 2 = 2$)**: The surviving unit $(2, 1)$ has now matured into the cheap slow-laundry window! Wash $(2, 1)$ via slow laundry at cost $1 \times 3 = 3$. Deficit remaining is $3 - 1 = 2$.
     - **Tier 2 (Fast Laundry, $2 < s \le 4 - 1 = 3$)**: Wash $2$ units from $(3, 4)$ via fast laundry at cost $2 \times 6 = 12$.
   - **Total Cost for $B = 5$**: $50 + 9 + 6 + 3 + 12 = 80$.
   - **What Would Break Under FIFO Fast Laundry?**
     Suppose on Day 3, both $(1, 3)$ and $(2, 2)$ were only in a fast window (e.g., if $d_{\text{slow}} = 3, d_{\text{fast}} = 1$) and we needed $1$ fast napkin on Day 3:
     - If we foolishly consumed $1$ unit of $(1, 3)$ (oldest, FIFO) for fast laundry on Day 3, then on Day 4 ($t = 4$), only $2$ units of $(1, \cdot)$ would remain for cheap slow laundry ($s \le 4 - 3 = 1$), whereas consuming $1$ unit of $(2, 2)$ (newest, **LIFO**) on Day 3 preserves all $3$ units of $(1, 3)$ to be slow-washed on Day 4!

---

### 10.8 Trace H: Direction B Coordinate-Shift & Regret-Heap Split (`P29 AGC 018 C — Coins`)

#### Concrete Numerical Instance ($X = 1, Y = 1, Z = 1, N = 3$)
- Person 1: $(A_1, B_1, C_1) = (10, 9, 0)$
- Person 2: $(A_2, B_2, C_2) = (8, 4, 0)$
- Person 3: $(A_3, B_3, C_3) = (5, 7, 6)$
1. **Step 1 (Subtract $C_i$, Baseline $\sum C_i = 0 + 0 + 6 = 6$)**:
   - Person 1: $(a'_1, b'_1) = (10, 9)$, difference $a'_1 - b'_1 = +1$.
   - Person 2: $(a'_2, b'_2) = (8, 4)$, difference $a'_2 - b'_2 = +4$.
   - Person 3: $(a'_3, b'_3) = (-1, +1)$, difference $a'_3 - b'_3 = -2$.
2. **Step 2 (Sort Descending by $a'_i - b'_i = A_i - B_i$)**:
   - Sorted order:
     1. **Pos 1 (Person 2)**: $a' - b' = +4$, $(a', b') = (8, 4)$
     2. **Pos 2 (Person 1)**: $a' - b' = +1$, $(a', b') = (10, 9)$
     3. **Pos 3 (Person 3)**: $a' - b' = -2$, $(a', b') = (-1, 1)$
3. **Step 3 (Evaluate Split Boundary $k \in [X, N - Y] = [1, 2]$)**:
   - **Split $k = 1$**:
     - Prefix $\{1\}$ picks top $X = 1$ of $a'$: Pos 1 gives $a' = 8$.
     - Suffix $\{2, 3\}$ picks top $Y = 1$ of $b'$: $\max(9, 1) = 9$ (Pos 2).
     - Total coins $= \text{Base } 6 + 8 + 9 = 23$ (Person 2 Gold $8$, Person 1 Silver $9$, Person 3 Bronze $6$).
   - **Split $k = 2$**:
     - Prefix $\{1, 2\}$ picks top $X = 1$ of $a'$: $\max(8, 10) = 10$ (Pos 2).
     - Suffix $\{3\}$ picks top $Y = 1$ of $b'$: Pos 3 gives $b' = 1$.
     - Total coins $= \text{Base } 6 + 10 + 1 = 17$.
   - Global optimum is $23$ at split $k = 1$!

---

### 10.9 Trace I: Cycle-Cover + Center Decomposition (`CF 387 D — George and Interesting Graph`)

#### Problem Mechanics & Why It Completes Section 7.2
In `CF 387 D` ($N \le 500, M \le 1,000$), a directed graph is called **interesting** if there is a special center vertex $c \in \{1, \dots, N\}$ such that:
1. $c$ has a self-loop $c \to c$, an outgoing edge $c \to v$ to every other vertex $v \ne c$, and an incoming edge $v \to c$ from every other vertex $v \ne c$ ($2N - 1$ incident edges on $c$).
2. Every other vertex $v \in V \setminus \{c\}$ has **total out-degree $2$ and total in-degree $2$** in $G$ (which means, after removing the edges $v \to c$ and $c \to v$ incident to $c$, the induced subgraph $G[V \setminus \{c\}]$ has **exact out-degree $1$ and exact in-degree $1$** at every vertex $v \ne c$—i.e., a **Directed Cycle Cover** on $V \setminus \{c\}$!).

#### Step-by-Step Compilation ($O(N \cdot M \sqrt{N})$)
1. Iterate over all $N$ choices of the center vertex $c \in \{1, \dots, N\}$.
2. For a fixed $c$:
   - Count how many of the $2N - 1$ mandatory center edges $\{c \to c\} \cup \{c \to v, v \to c : v \ne c\}$ already exist in $E$, say $E_{\text{center}}$. We must **add** $(2N - 1) - E_{\text{center}}$ missing center edges.
   - Among the remaining $M - E_{\text{center}}$ edges in $G[V \setminus \{c\}]$, we want to keep a maximum-cardinality subset $F \subseteq E(G[V \setminus \{c\}])$ such that every $v \in V \setminus \{c\}$ has $d_F^+(v) \le 1$ and $d_F^-(v) \le 1$—which is a **Maximum Bipartite Matching** of size $K_c$ on the $(N-1) \times (N-1)$ bipartite graph $V_{\text{out}} \setminus \{c\} \to V_{\text{in}} \setminus \{c\}$!
   - To turn $F$ into an exact cycle cover of $V \setminus \{c\}$, we **delete** the $(M - E_{\text{center}}) - K_c$ unused edges of $G[V \setminus \{c\}]$ and **add** $(N - 1) - K_c$ new edges to complete the matching to size $N - 1$.
3. Total edge edits for center $c$:
   $$\text{Edits}(c) = \big((2N - 1) - E_{\text{center}}\big) + \big((M - E_{\text{center}}) - K_c\big) + \big((N - 1) - K_c\big) = 3N - 2 + M - 2 E_{\text{center}} - 2 K_c.$$
4. Take the minimum over all $c \in \{1, \dots, N\}$! This cleanly demonstrates **Regime 2 of Section 7.2**: because any disjoint union of directed cycles on $V \setminus \{c\}$ is already connected through the universal center $c$, no subtour elimination is needed and bipartite matching is $100\%$ exact!

---

### 10.10 Trace J: Time-Expanded Quadratic Congestion & SCC Potential Initialization (`P26 CF 1187 G` & `P18 ABC 214 H`)

#### Part 1: Concrete Numerical Trace of Quadratic Edge Congestion (`P26 CF 1187 G`)
Suppose $N = 2$ vertices $\{1, 2\}$ connected by a single undirected edge $\{1, 2\}$, $K = 2$ agents starting at vertex $2$ at time $t = 0$, destination vertex $1$, time penalty $c = 2$, and quadratic edge congestion parameter $d = 3$.
1. **Option A — Both Agents Cross $2 \to 1$ Together at $t = 0 \to 1$ ($k = 2$ agents on the same edge)**:
   - In the time-expanded graph, the edge $(2, 0) \to (1, 1)$ has two parallel unit-capacity arcs with marginal odd-number costs:
     - Arc $r = 1$: `(cap = 1, cost = (2*1 - 1)*d = 1 * 3 = 3)`
     - Arc $r = 2$: `(cap = 1, cost = (2*2 - 1)*d = 3 * 3 = 9)`
   - Both agents arrive at $(1, 1)$ and exit via $(1, 1) \to T$ at cost $c \cdot 1 = 2$ each.
   - Total cost of Option A $= (3 + 9) + 2 \times 2 = 12 + 4 = 16$ (which matches $d \cdot 2^2 + 2 c \cdot 1 = 3 \times 4 + 4 = 16$).
2. **Option B — Staggered Crossing (Agent 1 Crosses at $t = 0 \to 1$, Agent 2 Waits at $(2,0) \to (2,1)$ and Crosses at $t = 1 \to 2$)**:
   - Agent 1 uses Arc $r = 1$ of $(2, 0) \to (1, 1)$ (cost $3$) and exits at $(1, 1) \to T$ (cost $c \cdot 1 = 2$).
   - Agent 2 waits along $(2, 0) \to (2, 1)$ (cost $0$), uses Arc $r = 1$ of $(2, 1) \to (1, 2)$ (cost $3$), and exits at $(1, 2) \to T$ (cost $c \cdot 2 = 4$).
   - Total cost of Option B $= (3 + 2) + (0 + 3 + 4) = 5 + 7 = 12 < 16$!
3. **Why SSP Automatically Finds the Staggered Optimum**:
   - Augmentation 1 routes Agent 1 along $(2, 0) \xrightarrow{3} (1, 1) \xrightarrow{2} T$ (cost $5$), saturating Arc $r = 1$ of $(2, 0) \to (1, 1)$ and lazily spawning Arc $r = 2$ of cost $9$.
   - Augmentation 2 compares $(2, 0) \xrightarrow{9} (1, 1) \xrightarrow{2} T$ (cost $11$) against $(2, 0) \xrightarrow{0} (2, 1) \xrightarrow{3} (1, 2) \xrightarrow{4} T$ (cost $7$), choosing the staggered path of cost $7$ for total cost $5 + 7 = 12$!

#### Part 2: Topological Potential Initialization on Condensed SCC DAG (`P18 AtCoder ABC 214 H`)
Suppose after Tarjan SCC condensation, we have $3$ SCCs $C_1, C_2, C_3$ in topological order with aggregated rewards $W_1 = 5, W_2 = 10, W_3 = 4$ and DAG edges $C_1 \to C_2$, $C_2 \to C_3$, $C_1 \to C_3$.
1. **Why Initial Negative Costs $-W_C$ Break Un-Initialized Dijkstra**:
   - The harvest bridges $C_{i,\text{in}} \to C_{i,\text{out}}$ have negative costs $-5, -10, -4$.
2. **$O(N + M)$ Topological DP Potential Initialization**:
   - Since the condensed graph is a strict DAG ($C_{i,\text{in}} \to C_{i,\text{out}} \to C_{j,\text{in}}$ for $i < j$), we compute shortest-path potentials $\pi(v)$ from $S$ in a single linear scan:
     - $\pi(S) = 0$, $\pi(C_{1,\text{in}}) = 0$, $\pi(C_{1,\text{out}}) = -5$.
     - $\pi(C_{2,\text{in}}) = -5$, $\pi(C_{2,\text{out}}) = -5 - 10 = -15$.
     - $\pi(C_{3,\text{in}}) = \min(\pi(C_{1,\text{out}}), \pi(C_{2,\text{out}})) = \min(-5, -15) = -15$, $\pi(C_{3,\text{out}}) = -15 - 4 = -19$.
     - $\pi(T) = \min_i \pi(C_{i,\text{out}}) = -19$.
   - Under these potentials $\pi$, **every forward arc in the entire network has reduced cost $c^\pi(u, v) = c(u, v) + \pi(u) - \pi(v) \ge 0$** (for example, the transit bypass arc $C_{2,\text{in}} \to C_{2,\text{out}}$ of cost $0$ has $c^\pi = 0 + (-5) - (-15) = +10 \ge 0$, and the harvest arc of cost $-10$ has $c^\pi = -10 + (-5) - (-15) = 0$!).
   - Thus all $K \le 10$ augmentations run via pure $O((N+M) \log N)$ Dijkstra with zero SPFA passes!
