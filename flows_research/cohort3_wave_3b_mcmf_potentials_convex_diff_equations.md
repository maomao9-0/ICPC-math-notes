# Cohort 3 — Wave 3B Master Reconciliation Monograph: Min-Cost Max-Flow (MCMF), Potentials, Slope Convexity, Convex Marginal Splitting & The Algebraic Equation-Difference Method

**Document Role**: Definitive cross-cohort reconciliation, theoretical synthesis, blind-spot audit, and unified problem bank for **Part III, Wave 3B** (reconciling Cohort 1 `iter_26_to_30_mcmf_potentials_convex_diff_equations.md` and Cohort 2 `cohort2_iter_78_to_82_mcmf_potentials_convex_diff_equations.md`, plus Cohort 3 targeted gap-hunting).
**Pedagogical Mandate**: Strict adherence to the **4-Step "Zero Magic Gadgets" Compilation Framework** (1. Non-Graph Diagnostic Signal $\to$ 2. Intermediate Algebraic / Logical Representation $\to$ 3. Mechanical Graph Compilation Scratchpad $\to$ 4. Hand-Checkable Toy Trace & Broken Gadget Counterexamples), zero boilerplate solver dumps, and multilingual exhaustiveness (`[EN]`, `[ZH]`, `[JA]`).

---

## 1. Cross-Cohort Blind-Spot Audit & Reconciliation Matrix

A rigorous side-by-side audit of **Cohort 1** (`iter_26_to_30`, 1,604 lines, 179.2 KB) and **Cohort 2** (`cohort2_iter_78_to_82`, 1,511 lines, 149.4 KB) reveals that while both cohorts achieved exceptional depth, each surfaced critical theoretical invariants, edge-case implementation traps, and canonical contest applications that the other omitted or treated only in passing.

### 1.1 Theoretical & Modelling Blind-Spot Matrix

| Topic / Iteration | Caught by Cohort 1 (`iter_26_to_30`), Missed or Under-Specified by Cohort 2 | Caught by Cohort 2 (`cohort2_iter_78_to_82`), Missed or Under-Specified by Cohort 1 | Cohort 3 Master Synthesis & Targeted Gap-Hunting Resolution |
| :--- | :--- | :--- | :--- |
| **Iter 26 / 78: MCMF Foundations, Johnson Potentials & Zkw vs. SSP** | 1. **4-Regime Potential Initialization Table** comparing Zero, DAG DP, Bipartite Explicit, and Bellman-Ford.<br>2. **Explicit 4-Vertex Negative-Cost DAG Trace** $(s,a,b,t)$ with costs $(-5, -2)$ showing $\pi_0$ initialization and 3 exact Dijkstra augmentations.<br>3. **Zkw `vis[u]` Retention Rule** on exponential zero-cost diamond DAGs.<br>4. **Undirected MCMF Edge Failure Mode**: Why sharing a single residual pair with cost $+c/-c$ creates a $-2c$ negative cycle, requiring two independent directed pairs $(u\to v, U, +c)$ and $(v\to u, U, +c)$. | 1. **LP Primal–Dual & Complementary Slackness Derivation** of Min-Cost $b$-Flow ($z_{uv} \ge -c_{uv}^\pi$), proving Potential Optimality (Theorem 78.4) directly from linear programming duality.<br>2. **Unreachable-Vertex Potential Corruption Hazard**: When vertices are unreachable from $s$ or when Dijkstra early-terminates at $t$, updating $\pi(w) \gets \pi(w) + d(w)$ overflows or corrupts future reverse edges unless capped via $\pi'(w) = \pi(w) + \min(d(w), d(t))$.<br>3. **Weakly Polynomial Edmonds–Karp Bit-Scaling** ($O(E \log U (E + V \log V))$). | Unifies the skew-symmetric primal circulation decomposition and LP complementary slackness; codifies the 4 initialization regimes alongside the **Unreachable-Vertex / Early-Exit Capping Contract**; synthesizes the 4-vertex DAG trace, Zkw `vis[u]` retention proof, and undirected edge gadget. |
| **Iter 27 / 79: Slope Convexity of $C(f)$, Early Stopping, WQS & Negative-Cycle Elimination** | 1. **Budget-Threshold Fractional Prefix Stopping (`C(f) <= 0`)**: How to maximize flow volume $f$ subject to total cost $\sum \text{cost} \le 0$ by accumulating a negative-cost buffer and taking $\lfloor -C_{\text{cur}} / d_k \rfloor$ on the threshold augmentation (`[SDOI2016] 数字配对`).<br>2. **WQS Penalty Failure on Cyclic Initial Graphs**: Why subtracting $\lambda$ per unit flow fails if $G$ has uneliminated negative cycles.<br>3. **Optimality Proof of Phase 2 in Lower-Bound MCMF**: Why deleting $S^*, T^*, (t\to s)$ and pushing additional $s\to t$ flow preserves global cost-optimality. | 1. **Parametric Slope Profile (`atcoder::mcf_graph::slope`)**: Exact breakpoint extraction of the piecewise-linear convex curve $C(f)$.<br>2. **The Variable-Hop $+M$ Cost-Shift Fallacy**: Explicit 4-node counterexample where adding $+10$ per edge makes a 2-hop path of true cost $-12$ lose to a 1-hop path of true cost $-10$, plus the **3 Exact Remedies** (Fixed-Hop Shift, Topological Potential Pre-Shift $C(f) = C_{\pi_0}(f) + f\cdot \pi_0(t)$, and Mandatory Initial Saturation). | Integrates the two proofs of slope convexity (Residual Decomposition + Potential Monotonicity), all stopping regimes (Max-Flow, Min-Cost Feasible `d_t >= 0`, Budget-Threshold `C(f) <= 0`, and Parametric `slope`), the Variable-Hop $+M$ Fallacy + 3 Remedies, 1D/2D WQS Collinear Recovery, and Mandatory Initial Saturation (`负权边强制满流消圈法`). |
| **Iter 28 / 80: Convex Marginal Splitting, Tournament 3-Cycles & Coupled Variables** | 1. **Pre-Existing Degree Offset Hazard in $\Delta \binom{k}{2}$**: When team $v$ already has $w_0(v)$ fixed wins before undecided matches, the $k$-th additional win costs $w_0(v) + k - 1$, not $k - 1$.<br>2. **Dynamic Lazy Edge Insertion**: Spawning $(v_{\text{id}}, k+1)$ only when $(v_{\text{id}}, k)$ is saturated (`[NOI2012] 美食节`). | 1. **Canonical Piecewise-Linear Compilation Table**: Exact $O(1)$-edge gadgets for Symmetric Absolute Deviation $c|f-a|$, Asymmetric Target Deviation $\alpha(a-f)_+ + \beta(f-a)_+$, Huber Loss, and Multi-Tier Elastic Tariffs without splitting into $U$ unit edges. | Synthesizes unit-step marginal splitting, the pre-existing degree offset rule, coupled $W_i + L_i = T_i$ elimination, the $O(1)$-breakpoint piecewise-linear table, dynamic lazy edge insertion, and weakly polynomial capacity bit-scaling. |
| **Iter 29 / 81: $k$-Interval Coverage & Discretization** | 1. **Open vs. Closed Endpoint Discretization Table**: Exact half-open normalization $[l_i, r_i] \mapsto [l_i, r_i + 1)$ vs. $(l_i, r_i) \mapsto [l_i, r_i)$ before `sort + unique`.<br>2. **Sliding-Window Fixed-Length Isomorphism** (`BZOJ 1283 序列`). | 1. **Algebraic Polarity Contrast**: Why upper-bound packing ($\sum x_i + y_t = K$) yields a **forward spine** $t \to t+1$ (acyclic DAG!) whereas lower-bound coverage ($\sum x_i - y_t = A_t$) yields a **backward spine** $t+1 \to t$ (cyclic!). | Reconciles primal $k$-lane chain-blocking with dual equation-difference; enforces the half-open discretization contract; contrasts forward-DAG upper-bound spines against backward-cyclic lower-bound spines. |
| **Iter 30 / 82: Algebraic Equation-Difference Method (`流守恒差分建模法`)** | 1. **Forward-DAG Formulation of Two-Sided Bounds**: In `[NEERC 2016] Delight for a Cat`, rewriting $L \le \sum x_j \le R$ using upper-bound slack $y_t = R - \sum x_j \in [0, R-L]$ makes the spine point **forward** ($t \to t+1$), keeping the graph an **acyclic DAG**! | 1. **Backward-Saturation Formulation of Two-Sided Bounds**: Writing $\sum x_j - y_t = L$ with $y_t \in [0, R-L]$ and resolving via Mandatory Initial Saturation.<br>2. **Dual-Slack Equation-Difference (`AtCoder ARC 137 E — Bakery`)**: Simultaneous shortfall slack $z_t \in [0, A_t]$ (cost $+D$) and surplus slack $y_t \in [0, \infty)$ (cost $0$). | Proves the exact algebraic isomorphism between the **Forward-DAG Upper-Slack** formulation and the **Backward-Spine Lower-Slack** formulation of two-sided interval constraints; integrates Dual Transposition (`[ZJOI2013] 防守战线`) and Multi-Slack Differencing (`ARC 137 E`). |
| **Cohort 3 Targeted Gap-Hunting (New in Section 7)** | *Omitted Cost Scaling & Minimum-Mean Cycle Canceling; treated non-contiguous column matrices only as an unsolvable NP-hard boundary.* | *Omitted Cost Scaling & Minimum-Mean Cycle Canceling; treated non-contiguous column matrices only via a 2-fragment counterexample.* | **1. Section 7.1**: Full derivation of **Goldberg–Tarjan Cost Scaling ($\epsilon$-Optimality, $O(V^2 E \log(VC))$)** and **Karp's Minimum-Mean Cycle Canceling ($O(V^2 E^3 \log V)$)**.<br>**2. Section 7.2**: **When Non-Contiguous Matrices CAN Be Transformed into Network Matrices**: Circular-Ones Matrices (`循环 1 矩阵` via modular difference $E_t - E_{t-1} \pmod T$) and **Tree/Laminar Path Matrices (`树上流守恒差分`: $\Delta E_u = E_u - \sum_{v \in \text{child}(u)} E_v$)** vs. the true Equal-Flow NP-hardness barrier. |

---

### 1.2 Practice Problem Cross-Cohort Deduplication & Tier Audit (32 Unique Problems)

Every problem from Cohort 1 (22 problems) and Cohort 2 (22 problems) has been audited, deduplicated (15 shared benchmarks merged to combine the sharpest algebraic derivations and implementation notes from both cohorts, 14 cohort-exclusive gems preserved), and augmented with **3 new Cohort 3 Gap-Hunting problems** (`P2.8`, `P4.7`, `P4.8`) to form a **32-problem Master Bank** (8 per tier):

| Master ID & Tier | Problem Title & Judge Coordinates | Source Status | Core Reconciliation Value Added |
| :--- | :--- | :--- | :--- |
| **P1.1** (Stepping Stone) | `Luogu P4016 / P2512` — 负载平衡问题 / 糖果传递 (HAOI 2008) | Shared (C1 `1.1` + C2 `P5`) | Bridges $O(N^2)$ circular MCMF with $O(N \log N)$ algebraic cycle-flow median elimination $\sum |x_i - \text{median}(c)|$. |
| **P1.2** (Stepping Stone) | `POJ 3422 / Luogu P2045` — Kaka's Matrix Travels / 方格取数加强版 | C1 Exclusive (`1.2`) | Canonical $(1, -A_{i,j})$ + $(K-1, 0)$ Diminishing-Returns Vertex Split + DAG DP $\pi_0$ initialization. |
| **P1.3** (Stepping Stone) | `Luogu P3358 / POJ 3680` — 最长 $k$ 可重区间集问题 / Intervals | Shared (C1 `1.3` + C2 `P4`) | Synthesizes open vs. closed endpoint discretization with forward-DAG equation-difference. |
| **P1.4** (Stepping Stone) | `Luogu P4553` — 80人环游世界 | C1 Exclusive (`1.4`) | Exact $[V_i, V_i]$ vertex-visit lower bounds via $S^* \to T^*$ feasible circulation. |
| **P1.5** (Stepping Stone) | `AtCoder ABC 247 G` — Dream Team | Shared (C1 `1.5` + C2 `P8`) | Full convex slope extraction $C(k)$ via Fixed-Hop $+M$ shift vs. `mcf_graph::slope`. |
| **P1.6** (Stepping Stone) | `AtCoder ABC 214 H` — Collecting | C2 Exclusive (`P2`) | Scaling MCMF to $N = 2\times 10^5$ via Tarjan SCC contraction + DAG DP $\pi_0$ + $K=10$ Dijkstra augmentations. |
| **P1.7** (Stepping Stone) | `Codeforces 863 F` — Almost Permutation | C2 Exclusive (`P3`) | Hard range-bound intersections $[L_v, R_v]$ + quadratic $cnt(x)^2$ odd marginal splitting $1, 3, \dots, 2N-1$. |
| **P1.8** (Stepping Stone) | `[AHOI2014 / JSOI2014] 支线剧情` (`Luogu P4043`) | Shared (C1 `2.4` + C2 `P1`) | Minimum-cost DAG edge cover with lower bounds $l_e = 1$ via demand-imbalance $S^*, T^*$ reduction. |
| **P2.1** (Intermediate) | `[WC2007] 剪刀石头布` (`Luogu P4249`) | Shared (C1 `2.1` + C2 `P6`) | Tournament 3-cycle maximization via complement $\binom{n}{3} - \sum \binom{d^+(v)}{2}$ + pre-existing win offset $w_0(v)$. |
| **P2.2** (Intermediate) | `[JSOI2009] 球队收益 / 球队预算` (`Luogu P4307`) | Shared (C1 `2.2` + C2 `P7`) | Coupled win/loss quadratic costs via $L_u = T_u - W_u$ elimination into univariate convex marginals. |
| **P2.3** (Intermediate) | `Codeforces 164 C` — Machine Programming | Shared (C1 `2.3` + C2 `P9`) | $K$-machine interval packing where Anti-SPFA tests TLE without $O(V+E)$ DAG DP potential initialization. |
| **P2.4** (Intermediate) | `[SDOI2011] 工作安排` (`Luogu P2488`) | C2 Exclusive (`P10`) | Piecewise-linear convex anger schedule compiled into $P+1 \le 6$ bundled breakpoint arcs per employee. |
| **P2.5** (Intermediate) | `Codeforces 277 E` — Binary Tree on Plane | Shared (C1 `2.5` + C2 `P16`) | Degree-bounded planar arborescence on a $y$-monotone DAG + floating-point $\epsilon = 10^{-9}$ Dijkstra guard. |
| **P2.6** (Intermediate) | `BZOJ 1283` — 序列 | C1 Exclusive (`2.6`) | Sliding-window length-$M$ subsequence packing via equation-difference. |
| **P2.7** (Intermediate) | `Codeforces 818 G` — Four Melodies | C2 Exclusive (`P11`) | $K=4$ disjoint subsequences optimized from $O(N^2)$ to $O(N)$ edges via persistent suffix relay hubs. |
| **P2.8** (Intermediate) | `[NOI2012] 美食节` (`Luogu P2050`) | **Cohort 3 Gap-Hunt** | Flagship **Dynamic Lazy Edge Insertion**: spawning chef slot $(j, k+1)$ only when slot $(j, k)$ is saturated. |
| **P3.1** (Advanced) | `[NOI2008] 志愿者招募` (`Luogu P3980`) | Shared (C1 `3.1` + C2 `P12`) | Flagship equation-difference $\Delta E_t = E_t - E_{t-1}$ converting lower-bound interval coverage into MCMF. |
| **P3.2** (Advanced) | `[SDOI2016] 数字配对` (`Luogu P3705`) | C1 Exclusive (`3.2`) | Prime-factor parity $\Omega(A_i) \bmod 2$ bipartite partition + Budget-Threshold Prefix Stopping $C(f) \le 0$. |
| **P3.3** (Advanced) | `Codeforces 717 G` — Underfail | C1 Exclusive (`3.3`) | Substring occurrence weighted interval packing via equation-difference. |
| **P3.4** (Advanced) | `Codeforces 1288 F` — Red-Blue Graph | Shared (C1 `3.4` + C2 `P15`) | Bipartite majority edge coloring ($d_R - d_B \ge 1$) via bidirectional edges + degree lower bounds. |
| **P3.5** (Advanced) | `[ICPC NEERC 2016 D / Luogu P6967]` — Delight for a Cat | Shared (C1 `3.5` + C2 `P18`) | Master reconciliation of **Forward-DAG Upper-Slack** vs. **Backward-Saturation Lower-Slack** on two-sided windows. |
| **P3.6** (Advanced) | `AtCoder AGC 018 C` — Coins | C1 Exclusive (`3.6`) | 3-choice transportation ($N = 10^5$) reduced via residual cycle-freeness to $A_i - B_i$ sorting + two heaps. |
| **P3.7** (Advanced) | `AtCoder AGC 034 D` — Manhattan Max Matching | C2 Exclusive (`P17`) | 4-sign $\ell_1$ Manhattan hub linearization ($2N+6$ vertices) + proof of why Min-Manhattan fails. |
| **P3.8** (Advanced) | `[TJOI2013] 循环格` (`Luogu P3965`) | C1 Exclusive (`4.4`) | Toroidal grid cycle cover comparing In/Out Bipartite Matching vs. Mandatory Initial Saturation. |
| **P4.1** (Mastery) | `[ZJOI2013] 防守战线` (`Luogu P3337`) | Shared (C1 `4.1` + C2 `P13`) | Point variables vs. interval constraints solved by LP Dual Transposition $\to$ Equation-Difference. |
| **P4.2** (Mastery) | `Codeforces 802 O` — April Fools' Problem (hard) | Shared (C1 `4.2` + C2 `P20`) | Convexity of $C(k)$ + 1D WQS Binary Search + 1-pass Min-Heap with Regret ($N = 5\times 10^5$). |
| **P4.3** (Mastery) | `Codeforces 739 E` — Gosha is hunting | Shared (C1 `4.3` + C2 `P19`) | 2-commodity convex MCMF concavity proof + 2D Nested WQS Binary Search ($O(N \log^2(1/\epsilon))$). |
| **P4.4** (Mastery) | `Codeforces 708 D` — Incorrect Flow | Shared (C1 `4.5` + C2 `P14`) | Circulation repair synthesizing pre-injected flow $f_e$, Mandatory Initial Saturation & 3-piece convex split. |
| **P4.5** (Mastery) | `AtCoder ARC 137 E` — Bakery | C2 Exclusive (`P21`) | Equation-difference with dual slack variables (shortfall penalty $z_t \in [0, A_t]$ + free surplus $y_t \ge 0$). |
| **P4.6** (Mastery) | `Codeforces 1307 G` — Cow and Exercise | C2 Exclusive (`P22`) | LP Duality between Shortest-Path Interdiction and Parametric MCMF Slope $\min_F \frac{C(F)+x}{F}$. |
| **P4.7** (Mastery) | `[八省联考 2018] 林克卡特树` (`Luogu P4383`) | **Cohort 3 Gap-Hunt** | $K+1$ vertex-disjoint tree paths: proving concavity of $F(k)$ via Tree-Path MCMF + WQS on Tree DP. |
| **P4.8** (Mastery) | `[LOJ #6405 / Tree Path Coverage]` — 树上流守恒差分 | **Cohort 3 Gap-Hunt** | **Tree Equation-Difference** ($\Delta E_u = E_u - \sum_{v \in \text{child}(u)} E_v$) for ancestor–descendant path coverage. |

---

## 2. Reconciled Iteration 26 / 78: MCMF Foundations, Residual Skew-Symmetry, Negative-Cycle Optimality, Johnson Potentials & Zkw vs. SSP

### 2.1 Step 1: Non-Graph Diagnostic Signal (When to Reach for MCMF)

Reach for **Minimum-Cost Flow (MCF)** or **Minimum-Cost Maximum-Flow (MCMF)** when a problem exhibits all three structural markers:
1. **Conserved Resource Allocation with Unit Costs**: Discrete units (items, workers, intervals, paths, or degree increments) must be routed or matched subject to hard capacity bounds $[l_e, u_e]$ and vertex balance laws, while optimizing a linear or separable convex objective $\sum_e c_e f_e$.
2. **Failure of Unweighted Max-Flow / Bipartite Matching**: Many feasible maximum matchings or maximum flows exist, and local greedy choices (e.g., repeatedly picking the globally cheapest edge) block pairs of slightly costlier edges whose combined value is superior—requiring **revocable regret** via reverse residual edges of negated cost $-c_e$.
3. **Small Polynomial Horizon ($V \le 5\,000$, $E \le 50\,000$, Total Flow $F \le 10^5$ or $U \le 10^9$ with Scaling)**: When $F \cdot E \log V \le 2\times 10^7$, explicit Successive Shortest Path (SSP) or Primal–Dual (Zkw) MCMF passes directly; when $N \ge 10^5$, MCMF provides the exact mathematical scaffolding to prove convexity for WQS binary search or priority-queue simulated flow (`模拟费用流`).

---

### 2.2 Step 2: Intermediate Algebraic & LP Primal–Dual Representation

#### A. Primal Skew-Symmetric Formulation vs. Standard Non-Negative Formulation
Let $G = (V, E)$ be a directed multigraph where each edge $e = (u \to v)$ has capacity $u_e \ge 0$ and unit cost $c_e \in \mathbb{R}$. Given vertex supplies/demands $b: V \to \mathbb{R}$ with $\sum_{v \in V} b(v) = 0$ (for standard $s$-$t$ flow of volume $F$, set $b(s) = +F$, $b(t) = -F$, and $b(v) = 0$ otherwise), the **Minimum-Cost $b$-Flow LP** is:

$$\begin{aligned}
\min_{f} \quad & C(f) = \sum_{e \in E} c_e f_e \\
\text{s.t.} \quad & \sum_{e \in \delta^+(v)} f_e - \sum_{e \in \delta^-(v)} f_e = b(v) \quad \forall v \in V \quad (\text{Dual multiplier: } -\pi(v) \in \mathbb{R}) \\
& 0 \le f_e \le u_e \quad \forall e \in E \quad (\text{Dual multiplier for } -f_e \ge -u_e: \; z_e \ge 0)
\end{aligned}$$

In the **skew-symmetric residual representation**, each primal edge $e = (u \to v)$ is paired with a reverse residual edge $e^{\text{rev}} = (v \to u)$ of initial capacity $0$ and cost $c_{e^{\text{rev}}} = -c_e$. For any feasible flow $f$, the **residual network** $G_f = (V, E_f)$ contains:
- The **forward residual edge** $e = (u \to v)$ with residual capacity $r_f(e) = u_e - f_e$ and cost $+c_e$ (whenever $f_e < u_e$), representing the marginal cost of pushing one more unit of flow.
- The **reverse residual edge** $e^{\text{rev}} = (v \to u)$ with residual capacity $r_f(e^{\text{rev}}) = f_e$ and cost $-c_e$ (whenever $f_e > 0$), representing the marginal refund of **canceling (regretting)** one unit of previously committed flow.

#### B. Circulation Decomposition & The Negative-Cycle Optimality Theorem

> [!IMPORTANT]
> **Lemma 2.1 (Residual Circulation Decomposition)**: Let $f$ and $f^*$ be any two feasible $b$-flows (or any two $s$-$t$ flows of the same volume $|f| = |f^*| = F$). Then the difference $\Delta f = f^* - f$ is a feasible **circulation** ($\nabla \cdot \Delta f = 0$ at every vertex) in the residual network $G_f$, and can be decomposed into at most $|E|$ directed simple cycles $W_1, W_2, \dots, W_k$ in $G_f$ carrying positive cycle flows $\gamma_1, \dots, \gamma_k > 0$ such that:
> $$C(f^*) - C(f) = \sum_{e \in E_f} c_e (\Delta f)_e = \sum_{j=1}^k \gamma_j \cdot c(W_j), \quad \text{where } c(W_j) = \sum_{e \in W_j} c_e$$

**Theorem 2.2 (Negative-Cycle Optimality Criterion)**: A feasible $b$-flow $f$ (or $s$-$t$ flow of volume $F$) has minimum cost among all feasible flows of the same volume if and only if the residual network $G_f$ contains **no directed cycle of strictly negative total cost**.
*Proof*:
- ($\Rightarrow$) If $G_f$ contains a directed cycle $W$ with $c(W) < 0$ and bottleneck capacity $\gamma = \min_{e \in W} r_f(e) > 0$, augmenting $\gamma$ units around $W$ preserves all vertex balances and capacities while strictly reducing cost by $\gamma |c(W)| > 0$.
- ($\Leftarrow$) Suppose $G_f$ has no negative-cost directed cycle ($c(W_j) \ge 0$ for all residual cycles $W_j$). Then for any other feasible flow $f^*$ of the same volume, Lemma 2.1 gives $C(f^*) - C(f) = \sum_{j=1}^k \gamma_j c(W_j) \ge 0$, so $C(f) \le C(f^*)$. $\blacksquare$

#### C. LP Duality, Reduced Costs & Complementary Slackness
Taking the LP dual of the Min-Cost $b$-Flow problem with vertex potentials $\pi(v)$ and dual edge slacks $z_e \ge 0$:

$$\max_{\pi, z \ge 0} \sum_{v \in V} b(v) (-\pi(v)) - \sum_{e \in E} u_e z_e \quad \text{s.t.} \quad z_{uv} \ge \pi(v) - \pi(u) - c_{uv} \quad \forall (u \to v) \in E$$

Define the **Johnson Reduced Cost** of any residual edge $e = (u \to v) \in E_f$ with respect to potential $\pi: V \to \mathbb{R}$ as:

$$c_{uv}^\pi := c_{uv} + \pi(u) - \pi(v)$$

Notice that skew-symmetry is preserved under potentials: $c_{vu}^\pi = -c_{uv} + \pi(v) - \pi(u) = -c_{uv}^\pi$. The dual constraint $z_{uv} \ge -c_{uv}^\pi$ combined with $z_{uv} \ge 0$ means $z_{uv} = \max(0, -c_{uv}^\pi)$ at dual optimality. By **LP Complementary Slackness**, a primal flow $f$ and dual potentials $\pi$ are jointly optimal if and only if for every primal edge $e = (u \to v) \in E$:
1. $f_e > 0 \implies z_e = -c_e^\pi \implies c_e^\pi \le 0$ (so the reverse residual edge $e^{\text{rev}}$ has $c_{e^{\text{rev}}}^\pi = -c_e^\pi \ge 0$).
2. $f_e < u_e \implies z_e = 0 \implies c_e^\pi \ge 0$ (so the forward residual edge $e$ has $c_e^\pi \ge 0$).

Combined, **Complementary Slackness is equivalent to $c_e^\pi \ge 0$ for every residual edge $e \in E_f$**!

---

### 2.3 Step 3: Mechanical Compilation of Johnson Potentials & SSP vs. Zkw

#### A. Potential Invariance & Shortest-Path Maintenance
For any path $P = (v_0 \to v_1 \to \dots \to v_k)$ and any cycle $W = (v_0 \to \dots \to v_k = v_0)$ in $G_f$, the intermediate potentials telescope:

$$c^\pi(P) = \sum_{i=0}^{k-1} \big(c(v_i, v_{i+1}) + \pi(v_i) - \pi(v_{i+1})\big) = c(P) + \pi(v_0) - \pi(v_k), \qquad c^\pi(W) = c(W)$$

Thus:
- A path $P$ from $s$ to $t$ is a shortest path in $G_f$ under true costs $c$ **if and only if** it is a shortest path under reduced costs $c^\pi$, with true length $c(P) = c^\pi(P) - \pi(s) + \pi(t)$.
- If $c_e^\pi \ge 0$ for all $e \in E_f$, we can compute shortest paths $d^\pi(v)$ from $s$ in $G_f$ using **Dijkstra's algorithm in $O((V + E) \log V)$ or $O(V^2 + E)$ time** instead of SPFA's $O(VE)$.

**Lemma 2.3 (Potential Update & Tight-DAG Invariant)**: Suppose $c_e^\pi \ge 0$ for all $e \in E_f$. Let $d^\pi(v)$ be the shortest-path distance from $s$ to $v$ in $(G_f, c^\pi)$, and define the updated potential:

$$\pi'(v) := \pi(v) + d^\pi(v)$$

Then:
1. For every edge $e = (u \to v) \in E_f$ reachable from $s$, triangle inequality $d^\pi(v) \le d^\pi(u) + c_{uv}^\pi$ implies:
   $$c_{uv}^{\pi'} = c_{uv}^\pi + d^\pi(u) - d^\pi(v) \ge 0$$
2. For every edge $e = (u \to v)$ lying on the **shortest-path subnetwork** (where $d^\pi(v) = d^\pi(u) + c_{uv}^\pi$), we have $c_{uv}^{\pi'} = 0$ and its reverse residual edge newly created by augmenting flow along $e$ has $c_{vu}^{\pi'} = -c_{uv}^{\pi'} = 0 \ge 0$.
Therefore, augmenting flow along any shortest path (or blocking flow of shortest paths) preserves $c_e^{\pi'} \ge 0$ across the entire updated residual network $G_{f'}$!

> [!CAUTION]
> **The Unreachable-Vertex & Early-Termination Potential Corruption Hazard (Cohort 2 Blind-Spot Catch)**:
> In practice, two situations arise where $d^\pi(w) = +\infty$:
> 1. Vertex $w$ is currently unreachable from $s$ in $G_f$ (e.g., all paths to $w$ are saturated), but a later augmentation reaches a neighbor $v$ of $w$ and unlocks a pre-existing edge $w \to v$ or $v \to w$.
> 2. You optimize Dijkstra to terminate early as soon as $t$ is popped from the priority queue, leaving vertices $w$ with $d^\pi(w) > d^\pi(t)$ unfinalized.
>
> If you naively skip updating $\pi(w)$ when $d^\pi(w) = \infty$ (or unfinalized), then $\pi'(v) = \pi(v) + d^\pi(v)$ increases while $\pi'(w) = \pi(w)$ stays frozen, causing $c_{wv}^{\pi'} = c_{wv}^\pi + 0 - d^\pi(v) < 0$! Conversely, adding $+\infty$ overflows 64-bit integers.
> **The Exact Capping Rule**:
> - If you run full Dijkstra to completion, any edge $(w \to v) \in E_f$ from an unreachable $w$ ($d^\pi(w) = \infty$) to a reachable $v$ ($d^\pi(v) < \infty$) can only become reachable later if flow is pushed into $w$ via some $u \to w$, which requires $w$ to already be reachable—**except** if you terminate Dijkstra early at $d^\pi(t)$!
> - Whenever terminating Dijkstra early as soon as $t$ is popped, you **must** update every vertex $w \in V$ via the capped formula:
>   $$\pi'(w) \gets \pi(w) + \min\big(d^\pi(w),\, d^\pi(t)\big)$$
>   Since $d^\pi(u) \le d^\pi(t)$ for all popped vertices $u$ and $\min(d^\pi(w), d^\pi(t))$ still satisfies the triangle inequality on all edges out of popped vertices, $c_e^{\pi'} \ge 0$ holds unconditionally without integer overflow.

#### B. The Four Regimes of Initial Potential Construction $\pi_0(v)$

| Regime | Structural Precondition on Initial $G$ | How to Compute $\pi_0(v)$ | Complexity of $\pi_0$ | Typical Contest Archetype |
| :--- | :--- | :--- | :--- | :--- |
| **1. Non-Negative Costs** | $c_e \ge 0$ for all initial edges $e \in E$ with $u_e > 0$. | Set $\pi_0(v) = 0$ for all $v \in V$. | $O(V)$ | Standard transportation, distance-cost matching, convex penalties $c_e \ge 0$. |
| **2. Acyclic Initial Graph (DAG) with Negative Costs** | $G$ has edges with $c_e < 0$, but the subgraph of positive-capacity edges is a **DAG**. | Compute shortest paths from $s$ via **Topological-Order DP**: $\pi_0(v) = \min_{(u\to v)\in E} (\pi_0(u) + c_{uv})$. | $O(V + E)$ | Maximum-weight interval packing (`CF 164C`), grid walks (`POJ 3422`), SCC-contracted graphs (`ABC 214 H`). |
| **3. Bipartite / Layered Fixed-Hop Graph** | Every $s \to L \to R \to t$ path has fixed hop structure and negative costs only on $L \to R$. | Set $\pi_0(s)=0, \pi_0(u)=0$ ($\forall u\in L$), $\pi_0(v) = \min_{u\in L} c_{uv}$ ($\forall v\in R$), $\pi_0(t) = \min_{v\in R} \pi_0(v)$. | $O(V + E)$ | Maximum-weight bipartite matching (`ABC 247 G`), assignment problems. |
| **4. General Graph with Negative Costs (No Negative Cycles)** | $G$ contains directed cycles of non-negative cost and negative-cost edges. | Run one initial **SPFA / Bellman-Ford** pass from a virtual super-source $s_0$ to set $\pi_0(v) = \text{dist}(s_0, v)$. (Or eliminate negative edges via Mandatory Initial Saturation!) | $O(VE)$ once | General circulation (`CF 708D`), lower-bound equation-difference (`NOI 2008 志愿者招募`). |

#### C. SSP (Dijkstra + 1 Path) vs. Zkw Primal–Dual (Dijkstra + Dinic Blocking Flow)

Once $\pi$ maintains $c_e^\pi \ge 0$, two augmentation engines exist:
1. **Successive Shortest Path (SSP)**: In each phase, run Dijkstra to find a single shortest $s$-$t$ path $P$, update $\pi(v) \gets \pi(v) + d^\pi(v)$, and push $\Delta = \min_{e \in P} r_f(e)$ along $P$.
   - *Best when*: Capacities along shortest paths are large or unique, or we need exact per-path prefix stopping (`[SDOI2016] 数字配对`).
2. **Zkw Primal–Dual (`zkw费用流`)**: In each phase, run Dijkstra to update $\pi$, then extract the **zero-reduced-cost tight subnetwork** $E_0 = \{e \in E_f : c_e^\pi = 0\}$ and run **Dinic-style multi-path DFS with current-arc pointers `cur[u]`** to push a maximal blocking flow of equal-cost shortest paths before the next Dijkstra pass.
   - *Best when*: Unit capacities ($u_e = 1$) with many parallel equal-cost paths (e.g., dense bipartite graphs or grid graphs).

> [!WARNING]
> **The Two Fatal Zkw Pitfalls (Cohort 1 Blind-Spot Catch)**:
> 1. **Zero-Cost Cycles in $E_0$**: Unlike Dinic's level graph (which is strictly layered by hop count), the tight subgraph $E_0 = \{e \in E_f : c_e^\pi = 0\}$ can contain **directed cycles of $0$ reduced cost**! Therefore, Zkw's DFS **must** maintain an on-stack recursion guard `vis[u] = true` upon entering $u$.
> 2. **The `vis[u]` Retention Rule on Failed Nodes**: When `dfs(u, pushed)` finishes exploring $u$:
>    - If $u$ successfully pushed all requested flow (or we are resetting for the next phase), we clear `vis[u] = false` only if $u$ might still have residual capacity to $t$.
>    - If `dfs(u, flow)` returns `used == 0` (meaning $u$ is a dead end that cannot reach $t$ in $E_0$), you **MUST KEEP `vis[u] = true`** for the remainder of the current DFS phase! If you reset `vis[u] = false` upon backtracking from a dead end, a diamond DAG of $0$-cost edges will re-explore $u$ exponentially ($O(2^V)$ TLE).

---

### 2.4 Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### A. Complete Numerical Trace of Negative-Cost DAG Initialization + 3 Dijkstra Passes
Consider $G = (V, E)$ with $V = \{s, a, b, t\}$, where we want the minimum-cost flow of volume $F = 3$ from $s$ to $t$:
- $s \to a$: capacity $2$, cost $0$
- $s \to b$: capacity $2$, cost $0$
- $a \to b$: capacity $1$, cost $-5$ (negative-cost edge!)
- $a \to t$: capacity $2$, cost $4$
- $b \to t$: capacity $2$, cost $-2$ (negative-cost edge!)

**Phase 0 (Topological DP Potential $\pi_0$)**:
Topological order is $(s, a, b, t)$.
- $\pi_0(s) = 0$
- $\pi_0(a) = \pi_0(s) + c(s,a) = 0 + 0 = 0$
- $\pi_0(b) = \min(\pi_0(s) + c(s,b),\, \pi_0(a) + c(a,b)) = \min(0 + 0,\, 0 - 5) = -5$
- $\pi_0(t) = \min(\pi_0(a) + c(a,t),\, \pi_0(b) + c(b,t)) = \min(0 + 4,\, -5 - 2) = -7$

Verify initial reduced costs $c_{uv}^{\pi_0} = c_{uv} + \pi_0(u) - \pi_0(v) \ge 0$:
- $c^{\pi_0}(s,a) = 0 + 0 - 0 = 0$
- $c^{\pi_0}(s,b) = 0 + 0 - (-5) = +5 \ge 0$
- $c^{\pi_0}(a,b) = -5 + 0 - (-5) = 0$
- $c^{\pi_0}(a,t) = 4 + 0 - (-7) = +11 \ge 0$
- $c^{\pi_0}(b,t) = -2 + (-5) - (-7) = 0$
All reduced costs are non-negative!

**Augmentation 1**:
- Dijkstra on $c^{\pi_0}$ finds $d^{\pi_0} = (0, 0, 0, 0)$ along $P_1 = s \to a \to b \to t$ (bottleneck $\Delta_1 = \min(2, 1, 2) = 1$).
- True path cost: $c(P_1) = d^{\pi_0}(t) - \pi_0(s) + \pi_0(t) = 0 - 0 + (-7) = -7$.
- Potentials update: $\pi_1 = \pi_0 + d^{\pi_0} = (0, 0, -5, -7)$. Edge $a \to b$ saturates ($r_f(a,b) = 0$, $r_f(b,a) = 1$ with $c^{\pi_1}(b,a) = 0$).

**Augmentation 2**:
- From $s$, $s \to a$ has $r_f = 1, c^{\pi_1} = 0$, so $d^{\pi_1}(a) = 0$. Since $a \to b$ is saturated, reaching $b$ requires $s \to b$ ($c^{\pi_1}(s,b) = 5 \implies d^{\pi_1}(b) = 5$), and $b \to t$ ($r_f = 1, c^{\pi_1} = 0 \implies d^{\pi_1}(t) = 5$).
- Shortest path is $P_2 = s \to b \to t$ with $\Delta_2 = 1$ and true cost $c(P_2) = d^{\pi_1}(t) + \pi_1(t) = 5 + (-7) = -2$.
- Potentials update: $\pi_2 = \pi_1 + d^{\pi_1} = (0, 0, 0, -2)$. Now $b \to t$ is saturated!

**Augmentation 3**:
- Under $\pi_2 = (0, 0, 0, -2)$, reduced costs from $s$: $c^{\pi_2}(s,a) = 0 \implies d^{\pi_2}(a) = 0$; $a \to t$ has $c^{\pi_2}(a,t) = 4 + 0 - (-2) = 6 \implies d^{\pi_2}(t) = 6$.
- Shortest path is $P_3 = s \to a \to t$ with $\Delta_3 = 1$ and true cost $c(P_3) = d^{\pi_2}(t) + \pi_2(t) = 6 + (-2) = +4$.
- Potentials update: $\pi_3 = (0, 0, 0, +4)$.
- Total flow $F = 3$, total minimum cost $C(3) = -7 + (-2) + 4 = -5$. Notice the strictly non-decreasing marginal slopes: $-7 < -2 < +4$.

#### B. Broken Gadget Counterexample: Undirected Edges in MCMF
Suppose a problem gives an **undirected** communication cable $\{u, v\}$ of capacity $U$ and cost $c > 0$ per unit flow in either direction.
- **Broken Construction**: Creating a single edge pair where $(u \to v)$ has initial capacity $U$, cost $+c$, and its reverse residual partner $(v \to u)$ has initial capacity $U$, cost $-c$.
  - *Why it breaks*: Because $(v \to u)$ starts with positive residual capacity $U$ and cost $-c < 0$, the 2-cycle $u \to v \to u$ is immediately active or $(v \to u)$ acts as a negative-cost generator! Conversely, if you give both $(u \to v)$ and its partner $(v \to u)$ cost $+c$, then canceling flow on $(u \to v)$ charges $+c$ instead of refunding $-c$, violating skew-symmetry.
- **Exact Repair**: An undirected edge $\{u, v\}$ of capacity $U$ and cost $c \ge 0$ **must** be compiled into **two independent directed residual pairs** (4 directed arcs in the adjacency list):
  1. Pair 1 for $u \to v$: forward $(u \to v, \text{cap } U, \text{cost } +c)$ and reverse $(v \to u, \text{cap } 0, \text{cost } -c)$.
  2. Pair 2 for $v \to u$: forward $(v \to u, \text{cap } U, \text{cost } +c)$ and reverse $(u \to v, \text{cap } 0, \text{cost } -c)$.
  Since $c \ge 0$, sending flow simultaneously on Pair 1 and Pair 2 costs $+2c \ge 0$ and never occurs in a min-cost solution; their net difference $f_{u\to v} - f_{v\to u} \in [-U, U]$ faithfully models the undirected flow with cost $c |f_{u\to v} - f_{v\to u}|$.

---

## 3. Reconciled Iteration 27 / 79: Slope Convexity of $C(f)$, Early Stopping, Parametric Slope, WQS Binary Search & Mandatory Initial Saturation

### 3.1 Step 1: Non-Graph Diagnostic Signal
Look for **Slope Convexity & Stopping / Penalty Variants** when:
1. **Optional Flow Volume ("Select at most $K$ items/paths to maximize profit")**: You are not forced to send maximum flow; pushing beyond the profit peak forces positive-cost augmentations that degrade total profit.
2. **Budget-Constrained Volume ("Maximize the number of matched pairs subject to total cost $\le 0$")**: You must stop at a fractional prefix of the first positive-cost augmenting path (`[SDOI2016] 数字配对`).
3. **Exact Cardinality $K$ at Large Scale ($N, K \ge 10^5$)**: Explicit MCMF is too slow, but the problem is equivalent to finding the minimum-cost flow of volume $K$, so the convex slope profile $C(k)$ unlocks **WQS Binary Search (Aliens Trick)** (`CF 802O`, `CF 739E`, `[八省联考 2018] 林克卡特树`).
4. **Initial Negative Cycles or Edge Lower Bounds $[l_e, u_e]$**: The graph contains genuine negative-cost cycles or mandatory flow lower bounds that must be resolved before Dijkstra can run (`CF 708D`, `[NOI2008] 志愿者招募`).

---

### 3.2 Step 2: Intermediate Algebraic Representation & Two Proofs of Slope Convexity

Let $C(f)$ denote the minimum cost of an $s$-$t$ flow of volume $f \in [0, F_{\max}]$.

> [!IMPORTANT]
> **Theorem 3.1 (Convexity of the Minimum-Cost Flow Function $C(f)$)**: In any flow network $(G, u, c)$ whose initial residual graph $G_0$ has no negative-cost directed cycle, the function $C: [0, F_{\max}] \to \mathbb{R}$ is continuous, piecewise-linear, and **convex**. Equivalently, for integer capacities, the marginal cost sequence $\Delta C(k) := C(k) - C(k-1)$ is non-decreasing:
> $$\Delta C(1) \le \Delta C(2) \le \dots \le \Delta C(F_{\max})$$

We reconcile the two complementary proofs from Cohort 1 and Cohort 2:

#### Proof 1: Combinatorial Residual Decomposition (Midpoint Convexity)
Let $f_1$ and $f_2$ be optimal flows of integer volumes $k-1$ and $k+1$, respectively. The difference $\Delta f = f_2 - f_1$ has net $s$-$t$ volume $2$, so by flow decomposition in $G_{f_1}$, $\Delta f$ decomposes into two unit $s$-$t$ augmenting paths $P_a, P_b$ in $G_{f_1}$ plus a collection of residual cycles $W_j$. Since $f_1$ is optimal for volume $k-1$, $G_{f_1}$ has no negative cycles ($c(W_j) \ge 0$), so $C(k+1) - C(k-1) \ge c(P_a) + c(P_b)$.
Moreover, augmenting $f_1$ along $P_a$ yields a valid flow of volume $k$ of cost $C(k-1) + c(P_a) \ge C(k)$, while reversing $P_a$ in $G_{f_2}$ (which is a valid $t \to s$ residual path of cost $-c(P_a)$ in $G_{f_2}$) yields a valid flow of volume $k$ of cost $C(k+1) - c(P_a) \ge C(k)$ (or using $P_b$: $C(k-1) + c(P_b) \ge C(k)$). Adding $C(k) \le C(k-1) + c(P_a)$ and $C(k) \le C(k-1) + c(P_b)$ gives:

$$2 C(k) \le 2 C(k-1) + c(P_a) + c(P_b) \le C(k-1) + C(k+1) \iff C(k) - C(k-1) \le C(k+1) - C(k) \quad \blacksquare$$

#### Proof 2: Potential Monotonicity in Successive Shortest Path
Normalize $\pi_0(s) = 0$. At each SSP step $i$, Dijkstra finds $d^{\pi_{i-1}}(s) = 0$ and $d^{\pi_{i-1}}(t) \ge 0$ (since $c_e^{\pi_{i-1}} \ge 0$ for all $e \in E_{f_{i-1}}$). The true cost of the $i$-th shortest augmenting path $P_i$ is:

$$c(P_i) = d^{\pi_{i-1}}(t) - \pi_{i-1}(s) + \pi_{i-1}(t) = \pi_{i-1}(t) + d^{\pi_{i-1}}(t) = \pi_i(t)$$

Since $\pi_{i+1}(t) = \pi_i(t) + d^{\pi_i}(t)$ and $d^{\pi_i}(t) \ge 0$ in every step, the sequence of path costs $\pi_1(t) \le \pi_2(t) \le \dots \le \pi_m(t)$ is monotonically non-decreasing! $\blacksquare$

---

### 3.3 Step 3: Mechanical Compilation of Stopping Regimes, Slope Queries, WQS & Negative-Cycle Elimination

#### A. The Four Augmentation Stopping Regimes

| Stopping Regime | Mathematical Objective | Exact Termination Rule on Step $i$ (Path Unit Cost $d_i = \pi_i(t)$, Bottleneck $\Delta_i$) | Canonical Problem |
| :--- | :--- | :--- | :--- |
| **1. Standard Min-Cost Max-Flow** | $\min C(f)$ subject to $f = F_{\max}$. | Run until $t$ is unreachable from $s$ in $G_f$ ($d^{\pi}(t) = +\infty$). | `[NOI2008] 志愿者招募` |
| **2. Min-Cost Feasible Flow (Unconstrained Profit Peak)** | $\min_{0 \le f \le F_{\max}} C(f)$ (or max profit $-C(f)$ over any volume). | Stop **immediately before** pushing any path with $d_i = \pi_i(t) \ge 0$. Only augment while $\pi_i(t) < 0$. | `CF 164C`, `BZOJ 1283` |
| **3. Budget-Threshold Prefix Stopping (`C(f) <= B`)** | $\max f$ subject to $C(f) \le B$ (typically $B = 0$ after negating profits). | Maintain running cost $C_{\text{cur}}$. While $d_i \le 0$, push full $\Delta_i$. When $d_i > 0$, max affordable units on $P_i$ is $\delta = \min\big(\Delta_i,\, \lfloor (B - C_{\text{cur}}) / d_i \rfloor\big)$; push $\delta$, and if $\delta < \Delta_i$, **terminate immediately**. | `[SDOI2016] 数字配对` |
| **4. Parametric Slope Extraction (`mcf_graph::slope`)** | Output all $(f_k, C(f_k))$ breakpoints of the convex hull of $C(f)$. | Coalesce consecutive augmentations with identical unit cost $d_i = d_{i-1}$ to emit the exact vertices $(F_k, C(F_k))$ of the piecewise-linear curve. | `ABC 247 G`, `CF 1307 G` |

#### B. The Variable-Hop $+M$ Cost-Shift Fallacy & Its 3 Exact Remedies (Cohort 2 Blind-Spot Catch)
When an initial graph has negative edge costs $c_e < 0$ (e.g., from negating profits $w_e > 0$ into $c_e = -w_e$), a common temptation is to add a large constant $+M$ to every edge so all costs become non-negative for Dijkstra.

> [!CAUTION]
> **Broken Gadget (The Variable-Hop $+M$ Fallacy)**:
> Suppose $P_1 = s \to a \to t$ is a $2$-hop path of true cost $-6 + (-6) = -12$, and $P_2 = s \to t$ is a $1$-hop path of true cost $-10$. The true optimum for $f=1$ is $P_1$ (cost $-12$).
> If you add $M = +10$ to **every edge**, $P_1$ now costs $(-6+10) + (-6+10) = +8$, whereas $P_2$ costs $-10 + 10 = 0$! Dijkstra picks the suboptimal $P_2$ because shifting every edge by $+M$ changes path cost by $c(P) + M \cdot |P|$ (penalizing hop count $|P|$).
>
> **The 3 Exact Remedies**:
> 1. **Remedy 1 (Single-Layer / Fixed-Hop Shift)**: Add $+M$ **only** to a cut of edges crossed **exactly once** by every $s$-$t$ path (e.g., only the $L \to R$ matching edges in a bipartite graph, where every augmenting path uses $k+1$ forward and $k$ backward $L \to R$ edges, so net traversal is always $+1$).
> 2. **Remedy 2 (Topological Potential Pre-Shift on DAGs — `atcoder::mcf_graph` trick)**: Compute $\pi_0(v)$ via DAG DP in $O(V+E)$, replace every edge cost $c_{uv}$ with $c_{uv}^{\pi_0} = c_{uv} + \pi_0(u) - \pi_0(v) \ge 0$, run non-negative MCMF to get shifted cost $C^{\pi_0}(f)$, and recover true cost via the exact telescoping identity:
>    $$C(f) = C^{\pi_0}(f) + f \cdot \big(\pi_0(t) - \pi_0(s)\big)$$
> 3. **Remedy 3 (Mandatory Initial Saturation)**: Pre-saturate all negative edges and repair vertex imbalances via $S^* \to T^*$ (Section 3.3.D below).

#### C. 1D and 2D WQS Binary Search (Lagrangian Penalty Relaxation)
Because $C(k)$ is convex on $k \in \{0, 1, \dots, F_{\max}\}$ (and profit $P(k) = -C(k)$ is concave), we can find $C(K)$ without enforcing the cardinality constraint $f = K$ by binary searching a Lagrangian penalty $\lambda \in \mathbb{R}$ added to every unit of flow entering $t$:

$$g(\lambda) := \min_{0 \le f \le F_{\max}} \big(C(f) - \lambda f\big)$$

- **Geometric Meaning**: A flow $f^*$ minimizes $C(f) - \lambda f$ if and only if $\Delta C(f^*) \le \lambda \le \Delta C(f^* + 1)$.
- **Collinear Slope Tie-Breaking Contract**: If multiple flow volumes $f \in [f_L(\lambda), f_R(\lambda)]$ achieve the exact minimum $g(\lambda)$ (because $\Delta C(f) = \lambda$ across a flat segment of the convex hull), a consistent tie-breaking rule (e.g., always taking the minimum-cardinality optimizer $f_L(\lambda)$, or maximum-cardinality $f_R(\lambda)$) finds the optimal slope $\lambda^*$ where $K \in [f_L(\lambda^*), f_R(\lambda^*)]$, and the exact answer is recovered by:
  $$C(K) = g(\lambda^*) + \lambda^* \cdot K$$
  *(Notice we multiply $\lambda^*$ by the target $K$, **not** by the tie-broken volume $f_L(\lambda^*)$ returned by the inner check!)*
- **2D Nested WQS (`CF 739E — Gosha is hunting`)**: If a problem routes two coupled commodities of volumes $(A, B)$ over a joint convex MCMF network, the joint optimum $C(A, B)$ is jointly convex in $(A, B)$, allowing an outer WQS binary search on $\lambda_A$ and an inner WQS binary search on $\lambda_B$ in $O(N \log^2(1/\epsilon))$.

#### D. Lower-Bound MCMF & Mandatory Initial Saturation (`负权边强制满流消圈法`)

Suppose each edge $e = (u \to v)$ has lower/upper bounds $[l_e, u_e]$ ($0 \le l_e \le u_e$) and unit cost $c_e \in \mathbb{R}$ (possibly with negative cycles!). We unify both problems into a single canonical transformation:

**Unified Compilation Contract**:
1. **Determine Pre-Saturated Flow $f_e^0$**:
   - If $c_e \ge 0$: pre-send only the mandatory lower bound $f_e^0 = l_e$, leaving forward residual edge $(u \to v)$ with capacity $u_e - l_e$ and cost $+c_e \ge 0$.
   - If $c_e < 0$ (**Mandatory Initial Saturation**): pre-send the **entire upper bound** $f_e^0 = u_e$! This saturates $(u \to v)$ and places its residual capacity $u_e - l_e$ onto the **reverse edge** $(v \to u)$ with cost $-c_e = |c_e| > 0$!
2. **Accumulate Base Cost and Vertex Imbalance**:
   $$C_{\text{base}} = \sum_{e \in E} f_e^0 c_e, \qquad M(v) = b(v) + \sum_{e \in \delta^-(v)} f_e^0 - \sum_{e \in \delta^+(v)} f_e^0$$
   *(where $b(v)$ is external net supply, or $0$ for pure circulation; for $s$-$t$ flow, add feedback edge $t \to s$ with $[0, \infty)$ and cost $0$).*
3. **Auxiliary Repair Network $(G^*, S^*, T^*)$**:
   - For each $v$ with $M(v) > 0$, add edge $(S^* \to v)$ with capacity $M(v)$ and cost $0$.
   - For each $v$ with $M(v) < 0$, add edge $(v \to T^*)$ with capacity $-M(v)$ and cost $0$.
4. **Execution & Phase-2 Optimality**:
   - Every edge in $G^*$ now has **non-negative cost $c \ge 0$**, so $\pi_0 \equiv 0$ is immediately valid for Dijkstra!
   - Run MCMF from $S^*$ to $T^*$. If max flow $< \sum_{M(v)>0} M(v)$, the lower bounds are infeasible. Otherwise, $C_{\text{base}} + C_{S^*\to T^*}$ is the **exact minimum-cost feasible flow** (automatically canceling only those negative-cost edges that fail to form negative cycles, and saturating all genuine negative cycles!).
   - **Theorem 3.2 (Optimality of Phase 2 for Min-Cost Max-Flow)**: For $s$-$t$ Min-Cost Max-Flow with lower bounds, after saturating $S^* \to T^*$, delete $S^*, T^*$ and $(t \to s)$ (recording $f_0 = f(t \to s)$), and run standard MCMF from $s$ to $t$ in the remaining residual network $G^*_f$. Because $G^*_f$ had no negative-cost cycles before deletion, deleting edges cannot create any negative-cost cycle; thus $f_0$ is a minimum-cost flow of volume $f_0$, and continuing SSP from $s$ to $t$ yields the globally optimal Min-Cost Max-Flow!

---

### 3.4 Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Toy Trace: Eliminating a Genuine Negative Cycle via Mandatory Initial Saturation
Consider a 3-vertex circulation network $V = \{1, 2, 3\}$ ($b(v) = 0$) with three directed edges forming a cycle of total cost $-4 + (-3) + 2 = -5 < 0$:
- $e_1 = (1 \to 2)$, $[0, 2]$, cost $-4 < 0$
- $e_2 = (2 \to 3)$, $[0, 3]$, cost $-3 < 0$
- $e_3 = (3 \to 1)$, $[0, 5]$, cost $+2 \ge 0$

1. **Pre-Saturation**:
   - $e_1$ has $c < 0 \implies f_{e_1}^0 = 2$. Reverse edge $(2 \to 1)$ gets capacity $2$, cost $+4$.
   - $e_2$ has $c < 0 \implies f_{e_2}^0 = 3$. Reverse edge $(3 \to 2)$ gets capacity $3$, cost $+3$.
   - $e_3$ has $c \ge 0 \implies f_{e_3}^0 = 0$. Forward edge $(3 \to 1)$ keeps capacity $5$, cost $+2$.
   - Base cost: $C_{\text{base}} = 2(-4) + 3(-3) + 0(2) = -17$.
   - Vertex imbalances $M(v) = \text{in}^0(v) - \text{out}^0(v)$:
     - $M(1) = 0 - 2 = -2 \implies$ edge $(1 \to T^*, \text{cap } 2, \text{cost } 0)$
     - $M(2) = 2 - 3 = -1 \implies$ edge $(2 \to T^*, \text{cap } 1, \text{cost } 0)$
     - $M(3) = 3 - 0 = +3 \implies$ edge $(S^* \to 3, \text{cap } 3, \text{cost } 0)$
2. **Dijkstra MCMF from $S^*$ to $T^*$ (all edge costs $\ge 0$)**:
   - **Path 1**: $S^* \to 3 \xrightarrow{\text{cost } 2} 1 \to T^*$, pushes $\Delta_1 = 2$ at unit cost $+2$ (routing 2 units along $e_3$ to complete the 2-unit negative cycle $1 \to 2 \to 3 \to 1$).
   - **Path 2**: $S^* \to 3 \xrightarrow{\text{rev } e_2, \text{ cost } 3} 2 \to T^*$, pushes $\Delta_2 = 1$ at unit cost $+3$ (canceling the 1 excess unit on $e_2$ that could not pass through bottleneck $e_1$).
3. **Final Result**: Total cost $C_{\text{base}} + 2(2) + 1(3) = -17 + 4 + 3 = -10$, corresponding to $f = (2, 2, 2)$ around the negative cycle of cost $2 \times (-5) = -10$. Zero Bellman-Ford or cycle-detection steps required!

---

## 4. Reconciled Iteration 28 / 80: Convex Marginal Cost Edge Splitting (`凸费用拆边`), Tournament 3-Cycles, Coupled Variables & Capacity Scaling

### 4.1 Step 1: Non-Graph Diagnostic Signal
Reach for **Convex Marginal Cost Splitting** or **Piecewise-Linear Bundling** when:
1. **Separable Non-Linear Objective**: The cost/profit is a sum of univariate convex penalties $\sum_v \phi_v(f_v)$ where $\phi_v$ has non-decreasing marginal differences (e.g., $f^2$, $\binom{f}{2}$, $|f - a|$, piecewise-linear tax brackets, or chef waiting-time weights).
2. **Symmetric Pairwise / Triad Counting (`剪刀石头布`)**: Counting 3-cycles in tournaments or monochromatic triangles where direct triad variables require hypergraphs, but complement counting reduces the objective to vertex degrees $\sum_v \binom{d^+(v)}{2}$.
3. **Coupled Complementary Variables ($W_i + L_i = T_i$)**: Costs depend on both wins $W_i$ and losses $L_i$, or both selected and unselected counts, where $W_i + L_i = T_i$ is fixed (`[JSOI2009] 球队收益`).

---

### 4.2 Step 2: Intermediate Algebraic Representation

#### A. Discrete Second-Difference Convexity & Unit-Step Marginal Splitting
A discrete function $\phi: \{0, 1, \dots, U\} \to \mathbb{R}$ is **discrete convex** if its first differences (marginal costs):

$$\Delta \phi(k) := \phi(k) - \phi(k-1) \quad (k = 1, 2, \dots, U)$$

satisfy $\Delta \phi(1) \le \Delta \phi(2) \le \dots \le \Delta \phi(U)$ (i.e., $\Delta^2 \phi(k) = \phi(k+1) - 2\phi(k) + \phi(k-1) \ge 0$). Writing the telescoping sum:

$$\phi(f) = \phi(0) + \sum_{k=1}^{f} \Delta \phi(k)$$

allows us to replace a single integer flow variable $f \in [0, U]$ with $U$ binary parallel edges $x_1, x_2, \dots, x_U \in [0, 1]$ where edge $k$ has capacity $1$ and linear unit cost $c_k = \Delta \phi(k)$. Because $c_1 \le c_2 \le \dots \le c_U$, any minimum-cost flow automatically saturates $x_1 = \dots = x_f = 1$ before touching $x_{f+1} = 0$!

#### B. Tournament 3-Cycle Complement Identity & Pre-Existing Win Offset
In an $n$-vertex tournament $T$ (where every pair $\{u, v\}$ has a directed edge), a subset of 3 vertices $\{u, v, w\}$ fails to form a directed 3-cycle if and only if it is transitive (one vertex beats the other two). Since a vertex with out-degree $d^+(v)$ beats $\binom{d^+(v)}{2}$ pairs of vertices, and each transitive triple has a unique winner of out-degree $2$ within the triple:

$$\text{\# of Directed 3-Cycles} = \binom{n}{3} - \sum_{v \in V} \binom{d^+(v)}{2}$$

Maximizing directed 3-cycles is **identical** to minimizing the separable convex sum $\sum_{v \in V} \binom{d^+(v)}{2}$!

> [!WARNING]
> **The Pre-Existing Win Offset Hazard (Cohort 1 Blind-Spot Catch)**:
> If team $v$ already has $w_0(v)$ fixed wins from pre-decided matches, and receives $k \ge 1$ additional wins from undecided matches, its total out-degree becomes $w_0(v) + k$. The marginal cost of the $k$-th **additional** win is:
> $$\Delta_k = \binom{w_0(v) + k}{2} - \binom{w_0(v) + k - 1}{2} = w_0(v) + k - 1 \quad (\text{for } k = 1, 2, \dots, \text{rem}(v))$$
> Withholding the constant base $\sum_v \binom{w_0(v)}{2}$ or forgetting $+w_0(v)$ in the marginal edge cost corrupts the relative priority between vertices!

#### C. Coupled Win/Loss Elimination ($W_i + L_i = T_i$)
In `[JSOI2009] 球队收益` (`Luogu P4307`), team $i$ has $T_i$ total matches, current wins $w_0(i)$, current losses $l_0(i)$, remaining undecided matches $rem(i) = T_i - w_0(i) - l_0(i)$, and quadratic cost $C_i W_i^2 + D_i L_i^2$. Instead of creating separate flow variables for wins and losses, substitute $L_i = T_i - W_i$ directly into the objective:

$$\phi_i(W_i) = C_i W_i^2 + D_i (T_i - W_i)^2$$

Then the marginal cost of transitioning from $W_i - 1$ wins to $W_i$ wins (which simultaneously decreases losses from $L_i + 1$ to $L_i$, where $L_i = T_i - W_i$) is:

$$\Delta \phi_i(W_i) = C_i(2W_i - 1) - D_i(2L_i + 1) = 2(C_i + D_i) W_i - 2 D_i T_i - (C_i + D_i)$$

Since $\Delta^2 \phi_i = 2(C_i + D_i) \ge 0$ whenever $C_i + D_i \ge 0$, this is strictly convex in $W_i$ alone!

---

### 4.3 Step 3: Mechanical Compilation of Piecewise-Linear Bundles, Lazy Insertion & Capacity Scaling

#### A. Canonical Piecewise-Linear & Convex Gadget Compilation Table (Cohort 2 Synthesis)
When $\phi(f)$ is piecewise-linear with $P \ll U$ breakpoints $0 = b_0 < b_1 < \dots < b_P = U$ and slopes $s_1 < s_2 < \dots < s_P$, **never split into $U$ unit edges**; compile into **$P$ bundled parallel edges** where edge $j$ has capacity $b_j - b_{j-1}$ and cost $s_j$:

| Convex Cost Function $\phi(f)$ on $f \in [0, U]$ | Algebraic Transformation / Base Offset | Parallel Edge Gadget Compilation $(u \to v)$ |
| :--- | :--- | :--- |
| **Quadratic $a f^2 + b f$** ($a > 0$, integer $f$) | $\Delta \phi(k) = a(2k - 1) + b$ for $k = 1 \dots U$. | $U$ edges of capacity $1$ and cost $a(2k-1) + b$. |
| **Binomial $\binom{f}{2}$** (with base $w_0$) | Base $\binom{w_0}{2}$; $\Delta \phi(k) = w_0 + k - 1$. | $U$ edges of capacity $1$ and cost $w_0 + k - 1$ ($k = 1 \dots U$). |
| **Diminishing-Returns First-Visit Bonus** (`POJ 3422`, `ABC 214 H`) | First unit gives reward $W > 0$; remaining $K-1$ units give $0$. | **2 edges**: $(1, \text{cost } -W)$ and $(K-1, \text{cost } 0)$. |
| **Symmetric Absolute Deviation $c \cdot |f - a|$** ($c > 0, a \in [0, U]$) | Base cost $c \cdot a$ at $f=0$; slope is $-c$ on $[0, a]$ and $+c$ on $[a, U]$. | **2 edges**: Edge 1 has $(\text{cap } a, \text{cost } -c)$ (pre-saturate or DAG DP); Edge 2 has $(\text{cap } U-a, \text{cost } +c)$. |
| **Asymmetric Target Penalty $\alpha(a - f)_+ + \beta(f - a)_+$** ($\alpha + \beta \ge 0$) | Base cost $\alpha \cdot a$ at $f=0$; slope is $-\alpha$ on $[0, a]$ and $+\beta$ on $[a, U]$. | **2 edges**: Edge 1 has $(\text{cap } a, \text{cost } -\alpha)$; Edge 2 has $(\text{cap } U-a, \text{cost } +\beta)$. |
| **3-Piece Circulation Repair (`CF 708D`)** (Current flow $f_e$, capacity $c_e$) | Case $f_e \le c_e$ vs. Case $f_e > c_e$ (pre-pay $f_e - c_e$). | **3 edges**: $(v \to u, \text{cap } \min(f_e, c_e), \text{cost } 1)$, $(u \to v, \text{cap } (c_e - f_e)_+, \text{cost } 1)$, $(u \to v, \text{cap } \infty, \text{cost } 2)$, plus free $(v \to u, \text{cap } (f_e - c_e)_+, \text{cost } 0)$. |

#### B. Dynamic Lazy Edge Insertion (`动态加边` — `[NOI2012] 美食节`)
When $M$ entities each have $P$ convex marginal slots ($k = 1, 2, \dots, P$) where each slot requires $N$ incoming edges (so pre-building all slots takes $O(NMP)$ edges), observe that by convexity $\Delta \phi(1) < \Delta \phi(2) < \dots < \Delta \phi(P)$, slot $(j, k+1)$ can **never** carry flow before slot $(j, k)$ is saturated!
- **Lazy Insertion Protocol**:
  1. Initially build only slot $k = 1$ for each entity $j \in \{1, \dots, M\}$.
  2. After each SSP augmentation saturates the edge from slot $(j, k)$ to the sink $t$, **dynamically allocate** vertex $(j, k+1)$ and its incoming edges, setting its initial potential $\pi(j, k+1)$ via $\min_{u} (\pi(u) + c(u \to (j, k+1)))$ (or running a single SPFA/Dijkstra pass).
  3. Total active vertices and edges remain bounded by $O(M + F)$ instead of $O(MP)$!

#### C. Weakly Polynomial Capacity Scaling (`Edmonds–Karp Bit-Scaling`, $O(E \log U (E + V \log V))$)
When edge capacities $u_e \le 10^9$ are huge and cannot be bundled into $O(1)$ linear pieces of known volume, standard SSP takes $O(F)$ augmentations (exponential in $\log U$). **Capacity Bit-Scaling** maintains an optimal flow and valid potentials $\pi$ across bit scales $\Delta = 2^{\lfloor \log_2 U \rfloor}, \dots, 2^1, 2^0$:
1. At scale $\Delta = 2^k$, double all current edge flows (moving from $G^{(k+1)}$ to $G^{(k)}$).
2. Add the $k$-th bit of each edge's capacity: if $(u_e \gg k) \& 1 = 1$, increment the capacity of $e = (u \to v)$ by $1$.
3. **Repair Violation**: If $c_{uv}^\pi < 0$ for the newly unlocked unit of capacity on $(u \to v)$, push $1$ unit of flow from $u$ to $v$ and route $1$ unit back from $v$ to $u$ via a shortest path in $G_f$ using Dijkstra!
Because at most $E$ single-unit repairs occur per bit scale across $\lfloor \log_2 U \rfloor + 1$ scales, total complexity is **strictly polynomial**: $O(E \log U (E + V \log V))$.

---

### 4.4 Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Broken Gadget: Concave Bulk-Discount Costs in MCMF
Suppose shipping $f \in \{0, 1, 2\}$ units along edge $e = (s \to t)$ has a **concave** bulk discount: $\phi(0) = 0, \phi(1) = 10, \phi(2) = 14$, so marginal costs are $\Delta \phi(1) = 10 > \Delta \phi(2) = 4$.
- **What Breaks**: If you create two parallel edges $e_1 = (s \to t, \text{cap } 1, \text{cost } 10)$ and $e_2 = (s \to t, \text{cap } 1, \text{cost } 4)$, then when sending $f = 1$ unit of flow, MCMF greedily picks the **second** marginal edge $e_2$ of cost $4$ without paying the first-unit setup cost $10$, falsely reporting $\phi(1) = 4$ instead of $10$!
- **Mathematical Boundary**: Minimizing a concave cost over a flow network is **NP-hard** (it subsumes the Fixed-Charge Network Flow / Steiner Tree problem). When $K$ is very small, concave costs require either **Min-Cut / Project Selection** (if supermodular) or branching / DP over the active support.

---

## 5. Reconciled Iteration 29 / 81: Maximum Weight $k$-Interval Coverage (`最长k可重区间集`), Coordinate Discretization & Open vs. Closed Endpoints

### 5.1 Step 1: Non-Graph Diagnostic Signal
Look for **Maximum Weight $k$-Interval Coverage / Packing** when:
1. **1D Timeline with Concurrency Cap $K$**: Given $N$ weighted intervals $I_i$ on a timeline (or sliding windows of length $M$), you must select a subset maximizing $\sum_{i \in S} w_i$ such that no point $t$ on the timeline is covered by more than $K$ selected intervals.
2. **Coordinate Range $10^9$ with $N \le 2\,000$**: Dynamic programming over the $K$ rightmost endpoints takes $O(N^{K+1})$, which is exponential for $K \ge 3$, whereas coordinate compression reduces the active timeline to $M \le 2N$ vertices.

---

### 5.2 Step 2: Intermediate Algebraic & Dual Perspectives

#### A. Half-Open Normalization Contract (Open vs. Closed Endpoints — Cohort 1 Catch)
Before applying `sort + unique` coordinate compression, **always normalize every interval into a right-open half-interval $[L_i, R_i)$** so that two intervals share a timeline point if and only if their half-open spans overlap:

| Problem Overlap Rule for $I_1 = (a_1, b_1)$ and $I_2 = (a_2, b_2)$ | Half-Open Normalization $[L_i, R_i)$ (Integer Coordinates) | Arc Span After Compressing Unique Endpoints $x_1 < x_2 < \dots < x_M$ |
| :--- | :--- | :--- |
| **Open intervals $(a_i, b_i)$** (touching at $b_1 = a_2$ allowed, e.g. `Luogu P3358`) | $[L_i, R_i) = [a_i, b_i)$ | $\text{rank}(a_i) \to \text{rank}(b_i)$ |
| **Closed integer intervals $[a_i, b_i]$** (touching at $b_1 = a_2$ **forbidden**, e.g. `[NOI2008] 志愿者招募`) | $[L_i, R_i) = [a_i,\, b_i + 1)$ | $\text{rank}(a_i) \to \text{rank}(b_i + 1)$ |
| **Sliding window of $M$ consecutive indices $\{i, i+1, \dots, i+M-1\}$** (`BZOJ 1283`) | $[L_i, R_i) = [i,\, i + M)$ | $i \to \min(N+1, i + M)$ |

Let the sorted unique endpoints be $p_1 < p_2 < \dots < p_M$. These partition the timeline into $M-1$ elementary atomic segments $S_t = [p_t, p_{t+1})$ for $t = 1, \dots, M-1$. Let $l_i = \text{rank}(L_i)$ and $r_i = \text{rank}(R_i)$ ($1 \le l_i < r_i \le M$). Then interval $i$ covers atomic segment $S_t$ if and only if $l_i \le t < r_i$.

#### B. Two Isomorphic Interpretations (Primal $K$-Lanes vs. Equation-Difference)
1. **Interpretation A (Primal $K$-Machine Timeline Sharing)**: Send $K$ units of flow from $s \to 1$ along the spine $1 \to 2 \to \dots \to M \to t$ (each spine edge $t \to t+1$ has capacity $K$ and cost $0$). Selecting interval $i$ detours $1$ unit of flow from vertex $l_i$ directly to vertex $r_i$ via arc $(l_i \to r_i)$ of capacity $1$ and cost $-w_i$, reducing the available flow on spine edges $l_i \to l_i+1, \dots, r_i-1 \to r_i$ by $1$. Since spine flows must remain $\ge 0$, at most $K$ intervals can bypass any segment $S_t$!
2. **Interpretation B (Consecutive Equation-Difference)**: Write the linear inequality for each atomic segment $t \in \{1, \dots, M-1\}$ with non-negative slack $y_t \ge 0$:
   $$E_t: \quad \sum_{i : l_i \le t < r_i} x_i + y_t = K \quad (x_i \in [0, 1],\; y_t \in [0, K])$$
   Taking $E_1$, $E_t - E_{t-1}$ ($2 \le t \le M-1$), and $-E_{M-1}$ yields the **exact same** acyclic DAG!

---

### 5.3 Step 3: Mechanical Compilation & DAG Potential Initialization
- **Vertices**: Timeline vertices $1, 2, \dots, M$, source $s$, sink $t$ (or identify $s = 1, t = M$).
- **Spine Edges**: For $t = 1, \dots, M-1$, add $(t \to t+1)$ with capacity $K$ and cost $0$. Source edge $(s \to 1)$ with capacity $K$, cost $0$.
- **Interval Edges**: For each interval $i = 1, \dots, N$, add $(l_i \to r_i)$ with capacity $1$ and cost $-w_i$.
- **Crucial Anti-SPFA Contract (`CF 164C`)**: Because $l_i < r_i$ and $t < t+1$ for every edge, the initial graph is a **strictly topological DAG** ($1 < 2 < \dots < M$). **Never run SPFA**! Compute $\pi_0(1) = 0$ and for $v = 2 \dots M$:
  $$\pi_0(v) = \min\Big(\pi_0(v-1),\; \min_{i : r_i = v} (\pi_0(l_i) - w_i)\Big)$$
  in $O(N + M)$ time, then run $K$ steps of Dijkstra SSP in $O(K (N + M) \log M)$ total time!

---

### 5.4 Step 4: Hand-Checkable Toy Trace
Let $K = 2$ with 3 open intervals: $I_1 = (1, 3), w_1 = 5$; $I_2 = (2, 4), w_2 = 6$; $I_3 = (1, 4), w_3 = 7$.
- Endpoints $1 < 2 < 3 < 4$ ($M = 4$). Spine edges $1 \to 2 \to 3 \to 4$ (cap $2$, cost $0$).
- Interval edges: $e_1 = (1 \to 3, \text{cap } 1, \text{cost } -5)$, $e_2 = (2 \to 4, \text{cap } 1, \text{cost } -6)$, $e_3 = (1 \to 4, \text{cap } 1, \text{cost } -7)$.
- **DAG DP $\pi_0$**: $\pi_0(1) = 0$, $\pi_0(2) = 0$, $\pi_0(3) = \min(0, 0-5) = -5$, $\pi_0(4) = \min(-5, 0-6, 0-7) = -7$.
- **Augmentation 1**: Shortest path $1 \xrightarrow{e_3} 4$ (cost $-7$, flow $1$).
- **Augmentation 2**: Under updated potentials, path $1 \to 2 \xrightarrow{e_2} 4$ has cost $-6$, while $1 \xrightarrow{e_1} 3 \to 4$ has cost $-5$. Note that $e_1$ and $e_2$ overlap on $[2, 3)$, where $e_3$ already uses $1$ lane of $[2, 3)$, so $[2, 3)$ has only $1$ lane left—we cannot take both $e_1$ and $e_2$ alongside $e_3$! Does the residual network allow canceling $e_3$?
  - If we push flow $1 \xrightarrow{e_1} 3 \xleftarrow{\text{rev } (2\to 3)} 2 \xrightarrow{e_2} 4$? Wait: spine $(2 \to 3)$ currently has **only $0$ flow** (since $e_3$ bypassed $1 \to 4$ directly!), so reverse spine $(3 \to 2)$ has **0 residual capacity**! Instead, $e_3$ can be canceled via $(4 \to 1)$ of cost $+7$, giving $1 \xrightarrow{e_1} 3 \to 4 \xrightarrow{\text{rev } e_3} 1 \to 2 \xrightarrow{e_2} 4$ of net cost $-5 + 7 - 6 = -4 < -6$ (Wait: $-7 + (-6) = -13$ uses $e_3 + e_2$, which covers $[1,2)$ once, $[2,3)$ twice, $[3,4)$ twice—valid for $K=2$!).
  - Indeed, for $K=2$, selecting $\{I_2, I_3\}$ gives weight $6 + 7 = 13$ and maximum overlap $2$ on $[2, 4)$! So Augmentation 2 directly pushes $1 \to 2 \xrightarrow{e_2} 4$ of cost $-6$, achieving total cost $-7 + (-6) = -13$ (profit $13$).

---

## 6. Reconciled Iteration 30 / 82: The Algebraic Equation-Difference Method (`流守恒差分建模法`)

### 6.1 Step 1: Non-Graph Diagnostic Signal
Reach for the **Algebraic Equation-Difference Method (`流守恒差分建模法` / Consecutive Constraint Differencing)**—pioneered in competitive programming by Bushu Zhou (`周冬`, 2009 National Training Team Paper on `[NOI2008] 志愿者招募`)—whenever:
1. **Consecutive / Interval Coverage Constraints**: A linear program has $T$ ordered constraints $E_1, E_2, \dots, E_T$, and each decision variable $x_j$ appears with coefficient $+1$ in a **contiguous interval of constraints** $t \in [L_j, R_j]$.
2. **Failure of Direct Vertex-Per-Item Mapping**: Because $x_j$ participates in $R_j - L_j + 1$ constraints simultaneously, standard flow conservation (where an edge enters one vertex and leaves one vertex) seems impossible until you **subtract adjacent equations** $\Delta E_t = E_t - E_{t-1}$!

---

### 6.2 Step 2: Intermediate Algebraic Derivation (The Telescoping Law)

Consider any linear program of the form:

$$\min \sum_{j=1}^M c_j x_j + \sum_{t=1}^T d_t y_t \quad \text{s.t.} \quad E_t: \sum_{j : L_j \le t \le R_j} x_j + \sigma_t y_t = B_t \quad (t = 1, \dots, T)$$

where $x_j \in [l_j, u_j]$, $y_t \ge 0$ is a slack or surplus variable with sign $\sigma_t \in \{+1, -1\}$, and $B_t \in \mathbb{R}$ is the right-hand side constant.

Append boundary dummy equations $E_0: 0 = 0$ and $E_{T+1}: 0 = 0$, and replace the system $\{E_1, \dots, E_T\}$ with the $T+1$ **differenced equations**:

$$\Delta E_t := E_t - E_{t-1} \quad \text{for } t = 1, 2, \dots, T+1$$

> [!IMPORTANT]
> **Theorem 6.1 (The Consecutive-Ones Telescoping Law)**:
> When we form the difference system $\Delta E_t = E_t - E_{t-1}$ for $t = 1, \dots, T+1$:
> 1. **Interval Variable $x_j$ ($t \in [L_j, R_j]$)**:
>    - In $\Delta E_{L_j} = E_{L_j} - E_{L_j - 1}$: $x_j$ appears with coefficient **$+1$**.
>    - In $\Delta E_t$ for $L_j < t \le R_j$: $x_j$ cancels completely ($1 - 1 = 0$)!
>    - In $\Delta E_{R_j + 1} = E_{R_j + 1} - E_{R_j}$: $x_j$ appears with coefficient **$-1$**.
> 2. **Point Slack Variable $\sigma_t y_t$ (appearing only in $E_t$)**:
>    - In $\Delta E_t$: $y_t$ appears with coefficient **$+\sigma_t$**.
>    - In $\Delta E_{t+1}$: $y_t$ appears with coefficient **$-\sigma_t$**.
> 3. **Right-Hand Side Supply/Demand**:
>    - Equation $\Delta E_t$ has constant right-hand side $\Delta B_t := B_t - B_{t-1}$ (with $B_0 = B_{T+1} = 0$), satisfying $\sum_{t=1}^{T+1} \Delta B_t = 0$.
>
> **Result**: Every variable ($x_j$ and $y_t$) now has **exactly one $+1$ coefficient and one $-1$ coefficient** across the entire system $\Delta E_1, \dots, \Delta E_{T+1}$! By adopting the convention $\text{Outflow}(t) - \text{Inflow}(t) = \Delta B_t$ at vertex $t \in \{1, \dots, T+1\}$:
> - A variable with **$+1$ in $\Delta E_u$ and $-1$ in $\Delta E_v$** compiles directly into a **directed edge $u \to v$**!

---

### 6.3 Step 3: Mechanical Compilation Across Constraint Polarities

#### A. Flagship Case 1: Lower-Bound Coverage (`[NOI2008] 志愿者招募`)
- **System**: $\sum_{j : L_j \le t \le R_j} x_j \ge A_t \implies \sum_{j : L_j \le t \le R_j} x_j - y_t = A_t$ ($y_t \ge 0$).
- **Differenced System** ($\Delta E_t = E_t - E_{t-1}$, $t = 1 \dots T+1$, $A_0 = A_{T+1} = 0$):
  $$\sum_{j : L_j = t} x_j - \sum_{j : R_j + 1 = t} x_j - y_t + y_{t-1} = A_t - A_{t-1}$$
- **Edge Compilation ($\text{Out}(t) - \text{In}(t) = A_t - A_{t-1}$)**:
  - **Volunteer $x_j$** ($+1$ at $L_j$, $-1$ at $R_j+1$): Edge **$L_j \to R_j + 1$**, capacity $\infty$, cost $c_j \ge 0$.
  - **Surplus Slack $y_t$** ($-1$ at $t$, $+1$ at $t+1$): Edge **$t + 1 \to t$** (backward spine!), capacity $\infty$, cost $0$.
  - **Node Supply $\Delta A_t = A_t - A_{t-1}$**: If $\Delta A_t > 0$, add $(S \to t, \text{cap } \Delta A_t, \text{cost } 0)$; if $\Delta A_t < 0$, add $(t \to T, \text{cap } -\Delta A_t, \text{cost } 0)$.
  - **Notice**: Since $c_j \ge 0$ and spine costs are $0$, **all initial edge costs are non-negative** ($\pi_0 \equiv 0$), even though the graph contains cycles $L_j \to R_j+1 \to \dots \to L_j$!

#### B. Flagship Reconciliation: Two-Sided Window Bounds (`[ICPC NEERC 2016 D] Delight for a Cat`)
Suppose each window $t \in \{1, \dots, T\}$ requires the number of chosen items $\sum_{j \in W_t} x_j$ to lie in $[L_t, R_t]$, where each item $j$ has profit $w_j$ (cost $-w_j$). Cohort 1 and Cohort 2 discovered two seemingly different compilations—here we prove their exact algebraic relationship:

| Method | Algebraic Slack Definition | Resulting Graph Structure | Initial Potentials / Pre-Processing |
| :--- | :--- | :--- | :--- |
| **Method 1: Forward-DAG Upper-Slack (Cohort 1 Discovery)** | Define $y_t := R_t - \sum_{j \in W_t} x_j \in [0, R_t - L_t]$, so:<br>$$E_t: \sum_{j \in W_t} x_j + y_t = R_t$$ | - Item $x_j$: **$L_j \to R_j + 1$** (cap $1$, cost $-w_j$)<br>- Slack $y_t$: **$t \to t + 1$** (forward spine! cap $R_t - L_t$, cost $0$) | Because **all edges point forward** ($u < v$), the graph is a **pure DAG**! Compute $\pi_0$ via $O(N)$ topological DP (or use Lower/Upper bounds $[L_t, R_t]$ on $t \to t+1$). |
| **Method 2: Backward-Spine Lower-Slack (Cohort 2 Discovery)** | Define $z_t := \sum_{j \in W_t} x_j - L_t \in [0, R_t - L_t]$, so:<br>$$E_t: \sum_{j \in W_t} x_j - z_t = L_t$$ | - Item $x_j$: **$L_j \to R_j + 1$** (cap $1$, cost $-w_j$)<br>- Slack $z_t$: **$t + 1 \to t$** (backward spine! cap $R_t - L_t$, cost $0$) | Graph has directed cycles with negative costs $-w_j < 0$; must apply **Mandatory Initial Saturation** to all edges with $-w_j < 0$. |

> [!TIP]
> **Reconciliation Takeaway**: Because $y_t + z_t = R_t - L_t$, reversing the flow on the slack edge $t+1 \to t$ ($z_t$) is algebraically identical to sending residual flow $y_t = (R_t - L_t) - z_t$ forward along $t \to t+1$! Whenever $L_t, R_t$ are upper/lower window bounds, **Method 1 (Upper-Bound Slack $y_t = R_t - \sum x_j \in [0, R_t - L_t]$)** keeps the entire network an **acyclic forward DAG**!

#### C. Dual Transposition When Point Variables Face Interval Constraints (`[ZJOI2013] 防守战线`)
What if each variable $x_i$ is a **single point** $i \in \{1, \dots, N\}$ with upper bound $x_i \le C_i$, while each constraint $j \in \{1, \dots, M\}$ is an **interval** $\sum_{i=L_j}^{R_j} x_i \ge D_j$?
- **Primal View**: Variable $x_i$ appears in an arbitrary non-contiguous subset of interval constraints $j$, so direct equation-differencing on primal constraints fails!
- **Dual Transposition Remedy**: Take the **LP Dual**! In the dual LP, each interval constraint $j$ becomes a single variable $u_j \ge 0$, and each point $i \in \{1, \dots, N\}$ becomes a constraint:
  $$E_i^{\text{dual}}: \quad \sum_{j : L_j \le i \le R_j} u_j - v_i \le W_i \quad (i = 1, \dots, N)$$
  In the dual LP, each variable $u_j$ once again spans a **contiguous interval of rows $i \in [L_j, R_j]$**, so Equation-Difference compiles the dual LP directly into a standard MCMF network!

---

### 6.4 Step 4: Hand-Checkable Toy Trace (`[NOI2008] 志愿者招募`, $T=3$)
Let $T = 3$ days with demands $A = (2, 3, 1)$, and 3 volunteer types:
- Type 1: $[1, 2]$, cost $4$; Type 2: $[2, 3]$, cost $5$; Type 3: $[1, 3]$, cost $8$.

1. **Equations & Differences ($A_0 = A_4 = 0$)**:
   - $\Delta E_1 = E_1 - E_0$: $+x_1 + x_3 - y_1 = 2 - 0 = +2$
   - $\Delta E_2 = E_2 - E_1$: $+x_2 - y_2 + y_1 = 3 - 2 = +1$
   - $\Delta E_3 = E_3 - E_2$: $-x_1 - y_3 + y_2 = 1 - 3 = -2$
   - $\Delta E_4 = E_4 - E_3$: $-x_2 - x_3 + y_3 = 0 - 1 = -1$
2. **Compiled Graph ($V = \{S, T, 1, 2, 3, 4\}$)**:
   - Supplies/Demands: $(S \to 1, \text{cap } 2, \text{cost } 0)$, $(S \to 2, \text{cap } 1, \text{cost } 0)$, $(3 \to T, \text{cap } 2, \text{cost } 0)$, $(4 \to T, \text{cap } 1, \text{cost } 0)$.
   - Volunteer arcs: $x_1 = (1 \to 3, \infty, 4)$, $x_2 = (2 \to 4, \infty, 5)$, $x_3 = (1 \to 4, \infty, 8)$.
   - Slack arcs: $y_1 = (2 \to 1, \infty, 0)$, $y_2 = (3 \to 2, \infty, 0)$, $y_3 = (4 \to 3, \infty, 0)$.
3. **SSP Execution (Total supply $2 + 1 = 3$)**:
   - **Step 1**: $S \to 1 \xrightarrow{x_1} 3 \to T$ sends $2$ units at cost $4 \times 2 = 8$ ($x_1 = 2$).
   - **Step 2**: $S \to 2 \xrightarrow{x_2} 4 \to T$ sends $1$ unit at cost $5 \times 1 = 5$ ($x_2 = 1$).
   - **Check**: Can we use $x_3$ ($1 \to 4$, cost $8$) instead of $x_1 + x_2$ (cost $4 + 5 = 9$)? In the residual network after Steps 1–2, reverse $x_1$ is $(3 \to 1, \text{cap } 2, \text{cost } -4)$ and reverse $x_2$ is $(4 \to 2, \text{cap } 1, \text{cost } -5)$, but $x_3$ goes $1 \to 4$: the cycle $1 \xrightarrow{x_3} 4 \xrightarrow{\text{rev } x_2} 2 \xleftarrow{y_2} 3 \xrightarrow{\text{rev } x_1} 1$ is blocked because $y_2$ points $3 \to 2$, so $1 \to 4 \to 2$ cannot reach $3$! (Algebraically, on Day 2 we need $A_2 = 3$ volunteers: $x_1 + x_2 = 2 + 1 = 3$ covers Day 2 three times, whereas replacing one $(x_1, x_2)$ pair with one $x_3$ leaves only $1 + 0 + 1 = 2 < 3$ volunteers on Day 2!). Thus $x = (2, 1, 0)$ with cost $13$ is uniquely optimal.

---

## 7. Cohort 3 Targeted Gap-Hunting: Cost Scaling, Minimum-Mean Cycle Canceling & Network Matrix Transformations

Both Cohort 1 and Cohort 2 left two high-level theoretical gaps that appear in advanced ICPC/IOI/National Team problems and literature:
1. **Cost-Scaling ($\epsilon$-Optimality) and Minimum-Mean Cycle Canceling**: How strongly polynomial and cost-scaling MCMF algorithms work when both capacities $U$ and costs $C$ are huge or when analyzing parametric cycle-canceling complexity.
2. **Beyond Linear Contiguous-Ones Matrices**: When a constraint matrix $A x = b$ does **not** have contiguous $1$s in each column under the natural row order, when can it **still** be transformed into an exact flow network (Circular-Ones Matrices and **Tree / Laminar Path Matrices `树上流守恒差分`**), and where is the exact NP-hardness boundary?

---

### 7.1 Gap-Hunt 1: Cost Scaling (`Goldberg–Tarjan` $\epsilon$-Optimality) & Minimum-Mean Cycle Canceling (`Karp's Theorem`)

#### A. $\epsilon$-Optimality and Goldberg–Tarjan Cost Scaling ($O(V^2 E \log(V C))$)
In Section 2.2.C, complementary slackness showed that a flow $f$ is optimal if and only if there exist potentials $\pi: V \to \mathbb{R}$ such that $c_e^\pi = c_e + \pi(u) - \pi(v) \ge 0$ for all residual edges $e \in E_f$. **Goldberg and Tarjan (1990)** relaxed this condition by introducing an approximation parameter $\epsilon \ge 0$:

> [!IMPORTANT]
> **Definition 7.1 ($\epsilon$-Optimality)**: A feasible flow (or circulation) $f$ and vertex potentials $\pi: V \to \mathbb{R}$ are **$\epsilon$-optimal** if every residual edge $e = (u \to v) \in E_f$ satisfies:
> $$c_{uv}^\pi = c_{uv} + \pi(u) - \pi(v) \ge -\epsilon$$
>
> **Theorem 7.2 (Threshold of Exact Optimality)**: If all edge costs $c_e$ are integers and $f$ is $\epsilon$-optimal for any $\epsilon < \frac{1}{|V|}$, then $f$ is **strictly optimal** ($0$-optimal)!
> *Proof*: For any simple directed cycle $W$ in the residual network $G_f$, $|W| \le |V|$ and potentials telescope around $W$, so:
> $$c(W) = \sum_{e \in W} c_e = \sum_{e \in W} c_e^\pi \ge -|W| \cdot \epsilon \ge -|V| \cdot \epsilon > -1$$
> Since all $c_e \in \mathbb{Z}$, $c(W)$ is an integer strictly greater than $-1$, which forces $c(W) \ge 0$! By Theorem 2.2, $f$ is optimal. $\blacksquare$

**Mechanics of the Cost-Scaling Algorithm**:
1. **Multiply all integer costs by $|V|$** (or scale $\epsilon$ down to $< 1/|V|$): Initially set $\epsilon_0 = C_{\max} = \max_e |c_e|$, $\pi \equiv 0$, and $f$ to any feasible $b$-flow (found via one standard max-flow call). Trivially $(f, \pi)$ is $\epsilon_0$-optimal.
2. **Halving Phase ($\epsilon \gets \epsilon / 2$)**: Given a $2\epsilon$-optimal flow $f$ and potentials $\pi$:
   - First **saturate all admissible negative edges**: for every residual edge $e = (u \to v) \in E_f$ with $c_{uv}^\pi < 0$, push $r_f(e)$ units of flow across $e$. Now every remaining residual edge has $c_e^\pi \ge -2\epsilon$ (in fact, newly created reverse edges of saturated negative edges have $c_{vu}^\pi = -c_{uv}^\pi > 0 \ge -\epsilon$), so $(f, \pi)$ is already $\epsilon$-optimal as a **preflow**, though vertices now have excesses $e(v) = \text{in}(v) - \text{out}(v) - b(v)$.
   - **Push/Relabel on the Admissible Graph ($-\epsilon \le c_{uv}^\pi < 0$)**: While some vertex $u$ has positive excess $e(u) > 0$:
     - **Push**: If there is a residual edge $(u \to v) \in E_f$ with $-\epsilon \le c_{uv}^\pi < 0$, push $\min(e(u), r_f(u,v))$ from $u$ to $v$. (The newly created reverse edge $(v \to u)$ has $c_{vu}^\pi = -c_{uv}^\pi \in (0, \epsilon] \ge -\epsilon$, preserving $\epsilon$-optimality!)
     - **Relabel**: If no residual edge out of $u$ has $c_{uv}^\pi < 0$ (meaning $c_{uv}^\pi \ge 0$ for all $(u \to v) \in E_f$), decrease $u$'s potential by $\epsilon$:
       $$\pi(u) \gets \pi(u) - \epsilon$$
       Since $c_{uv}^\pi \ge 0$ before relabeling, subtracting $\epsilon$ from $\pi(u)$ lowers $c_{uv}^\pi$ to at least $-\epsilon$, preserving $\epsilon$-optimality while making at least one outgoing edge admissible!
3. **Complexity**: Across each $\epsilon$-halving phase, each vertex is relabeled $O(V)$ times, yielding $O(V^2 E)$ work per scale (or $O(V E \log(V^2/E))$ with dynamic trees), and $\lceil \log_2(V C_{\max}) \rceil$ phases yield **$O(V^2 E \log(V C_{\max}))$**—the engine inside `LEDA` and high-performance circulation solvers!

#### B. Minimum-Mean Cycle Canceling & Karp's Theorem ($O(V^2 E^3 \log V)$ Strongly Polynomial)
Naive cycle canceling (finding any negative cycle and saturating it) can take $\Omega(E U C)$ iterations on pathological graphs (`Zadeh's bad networks`). **Goldberg and Tarjan (1989)** proved that if, in every step, we cancel a directed cycle $W^*$ in $G_f$ of **minimum mean cost**:

$$\mu(G_f) := \min_{\text{directed cycle } W \subseteq G_f} \frac{c(W)}{|W|}$$

then the algorithm terminates in **strongly polynomial time $O(V^2 E^3 \log V)$** (independent of both $U$ and $C$!).
- **Karp's Minimum-Mean Cycle Theorem (1978)**: Fix a source vertex $s$ (or a virtual super-source reaching all $v \in V$ with $0$-cost edges) and let $D_k(v)$ be the minimum cost of a directed walk of **exactly $k$ edges** from $s$ to $v$ in $G_f$ (computed in $O(VE)$ time via $D_k(v) = \min_{(u\to v)\in E_f} (D_{k-1}(u) + c_{uv})$ for $k = 1 \dots V$). Then:
  $$\mu(G_f) = \min_{v \in V} \max_{0 \le k \le V-1} \frac{D_V(v) - D_k(v)}{V - k}$$
- **Connection to $\epsilon$-Optimality**: The minimum cycle mean $\mu(G_f)$ is the exact negation of the smallest $\epsilon^*$ for which $G_f$ admits an $\epsilon^*$-optimal potential: $\epsilon^*(G_f) = \max(0, -\mu(G_f))$. Every $O(VE)$ minimum-mean cycle cancellations shrink $\epsilon^*(G_f)$ by a factor of at least $(1 - 1/V)$, which after $V \ln V$ blocks reduces $\epsilon^*$ by a factor of $1/V$, guaranteeing that at least one edge becomes permanently fixed in flow direction after $O(V E^2 \log V)$ cancellations!

---

### 7.2 Gap-Hunt 2: Transforming Non-Contiguous Matrices into Network Matrices (Circular-Ones & Tree Equation-Differencing)

In Section 6, we saw that if every variable $x_j$ appears in a contiguous interval of rows $[L_j, R_j]$ (the **Consecutive-Ones Property (C1P)** on columns), then $\Delta E_t = E_t - E_{t-1}$ compiles the LP into a flow network. What if the columns do **not** have contiguous $1$s?

#### A. Case 1: Circular-Ones Matrices (`循环 1 矩阵` — 24-Hour Cyclic Shift Scheduling)
Suppose a 24-hour call center has $T$ cyclic time slots $0, 1, \dots, T-1$, and shift $j$ works a contiguous cyclic window of hours from $L_j$ to $R_j \pmod T$.
- If $L_j \le R_j$, column $j$ has $1$s in $[L_j, R_j]$.
- If $L_j > R_j$ (an **overnight wrap-around shift**), column $j$ has $1$s in $[0, R_j] \cup [L_j, T-1]$—which is **two disjoint blocks** in linear row order!
- **Why Naive Linear Differencing $\Delta E_t = E_t - E_{t-1}$ (with $E_{-1} = E_T = 0$) Fails**: A wrap-around column has $+1$ at $0$, $-1$ at $R_j+1$, $+1$ at $L_j$, and $-1$ at $T$ (four non-zero entries!).
- **The Two Exact Network Matrix Transformations**:
  1. **Parametric Total-Workforce Fixing (Bartholdi–Orlin–Ratliff 1980)**: Let $W = \sum_{j : L_j > R_j} x_j$ be the total number of overnight workers active at the wrap-around boundary between $T-1$ and $0$. Instead of setting $E_0 - E_{-1}$ against $0$, take **cyclic modular differences** $\Delta^{\text{cyc}} E_t := E_t - E_{(t-1) \bmod T}$ for $t = 0, 1, \dots, T-1$!
     In $\Delta^{\text{cyc}} E_t$, **even a wrap-around shift $x_j$ has ONLY ONE $+1$ (at $t = L_j$) and ONE $-1$ (at $t = (R_j + 1) \bmod T$)** because $E_0 - E_{T-1}$ cancels the wrap-around ($1 - 1 = 0$)!
     *Subtlety*: The slack variable $y_{T-1}$ also wraps around from $0 \to T-1$, and the total number of active shifts at midnight is controlled by the circulation around the cycle $0 \leftarrow 1 \leftarrow \dots \leftarrow T-1 \leftarrow 0$. Thus, Circular-Ones LPs reduce directly to **Minimum-Cost Circulation on a Cyclic Spine**!
  2. **Column Complement Flipping**: Equivalently, fix or binary-search the total number of chosen shifts $S = \sum_j x_j$, and for every wrap-around shift $j$ ($L_j > R_j$), substitute $x_j$ out of $[0, R_j] \cup [L_j, T-1]$ by subtracting $x_j$ from all rows: $\mathbf{1}_{[0, R_j] \cup [L_j, T-1]} = \mathbf{1}_{[0, T-1]} - \mathbf{1}_{[R_j + 1, L_j - 1]}$, which restores linear contiguous-ones!

#### B. Case 2: Laminar & Tree-Path Equation-Differencing (`树上流守恒差分`)
Suppose we are given a rooted tree $T = (V, E)$ with root $r$, where each node $u \in V$ has a coverage requirement $E_u$ (e.g., at least $A_u$ paths must pass through $u$), and each variable $x_j$ corresponds to a **vertical ancestor–descendant path** from an ancestor $a_j$ down to a descendant $d_j$ in $T$.
- Under any linear DFS order of $V$, a vertical path $P(a_j, d_j)$ visits **non-contiguous** DFS indices (skipping entire subtrees of siblings along the path)!
- **Can we still difference the equations so every variable $x_j$ has at most one $+1$ and one $-1$?** **YES!**

> [!IMPORTANT]
> **Theorem 7.3 (Tree / Laminar Equation-Difference Law — `树上流守恒差分`)**:
> For each vertex $u \in V$ in a rooted tree $T$, define the **tree-differenced equation**:
> $$\Delta^{\text{tree}} E_u := E_u - \sum_{v \in \text{child}(u)} E_v$$
> together with a single root sink equation $\Delta^{\text{tree}} E_{\text{sink}} := -E_r$.
> Let $x_j$ be any variable whose support in $\{E_u\}_{u \in V}$ is a **vertical path $P(a_j, d_j)$** from ancestor $a_j$ to descendant $d_j$. Then for every $u \in V$:
> - How many children $v \in \text{child}(u)$ lie on the vertical path $P(a_j, d_j)$?
>   - If $u = d_j$ (the bottom endpoint): $u \in P(a_j, d_j)$ has **$0$ children** on $P(a_j, d_j)$, so $x_j$ has coefficient **$1 - 0 = +1$ in $\Delta^{\text{tree}} E_{d_j}$**!
>   - If $u \in P(a_j, d_j) \setminus \{d_j\}$ (an internal or top vertex of the path): $u$ has **exactly $1$ child** on $P(a_j, d_j)$, so $x_j$ cancels completely ($1 - 1 = 0$) in $\Delta^{\text{tree}} E_u$!
>   - If $u = \text{parent}(a_j)$ (the parent of the top endpoint): $u \notin P(a_j, d_j)$, but $u$ has **exactly $1$ child ($a_j$)** on $P(a_j, d_j)$, so $x_j$ has coefficient **$0 - 1 = -1$ in $\Delta^{\text{tree}} E_{\text{parent}(a_j)}$** (or in $\Delta^{\text{tree}} E_{\text{sink}}$ if $a_j = r$)!
>   - For all other $u \in V$: coefficient is $0 - 0 = 0$.
>
> **Compilation Rule**: Under $\Delta^{\text{tree}} E_u = E_u - \sum_{v \in \text{child}(u)} E_v$:
> - Every vertical tree path $x_j$ on $P(a_j, d_j)$ compiles into a **single directed edge from bottom to parent-of-top**:
>   $$d_j \longrightarrow \text{parent}(a_j) \quad (\text{cost } c_j)$$
> - Every vertex slack variable $y_u$ (appearing only in $E_u$ with coefficient $-1$ for lower-bound coverage $\sum x_j - y_u = A_u$) has $-1$ in $\Delta^{\text{tree}} E_u$ and $+1$ in $\Delta^{\text{tree}} E_{\text{parent}(u)}$, compiling into a **single tree edge**:
>   $$\text{parent}(u) \longrightarrow u \quad (\text{cost } 0)$$
> - Node supply at $u$ is $\Delta^{\text{tree}} A_u = A_u - \sum_{v \in \text{child}(u)} A_v$!

Notice that 1D linear equation-differencing ($\Delta E_t = E_t - E_{t-1}$) is simply the special case of Theorem 7.3 when the tree $T$ is a **path graph** $T \to T-1 \to \dots \to 1$!

#### C. The True Boundary: Network Matrices vs. Equal-Flow NP-Hardness
By **Tutte's & Truemper's Network Matrix Theorem**, a $\{0, \pm 1\}$ constraint matrix $A$ can be transformed by invertible row operations into a flow incidence matrix (at most one $+1$ and one $-1$ per column) **if and only if** $A$ is the tree-path incidence matrix of some directed spanning tree $\mathcal{T}$ (recognizable in $O(\text{nnz}(A))$ time).
- **When $A$ is NOT a Network Matrix**: If variables $x_j$ are arbitrary general tree paths $u_j \leftrightarrow v_j$ (passing through $\text{LCA}(u_j, v_j)$ with **two** children on the path, producing coefficient $1 - 2 = -1$ at $\text{LCA}$ and $-1$ at $\text{parent}(\text{LCA})$), or arbitrary 2-interval variables $[L_j^{(1)}, R_j^{(1)}] \cup [L_j^{(2)}, R_j^{(2)}]$, then $x_j$ requires **two edges to carry equal integer flow** ($f_{e_1} = f_{e_2}$). The **Integer Equal-Flow Problem** is NP-hard (reducible from 3-SAT and Disjoint Paths).

---

### 7.3 Reconciled Master Recognition & Compilation Decision Table

| Problem Archetype | Surface Signal in Statement | Canonical Compilation / Engine | Complexity |
| :--- | :--- | :--- | :--- |
| **1. Standard Assignment / Bipartite Profit** | Match $L$ to $R$ with edge costs/profits, capacities $\le U$. | Bipartite MCMF with explicit $\pi_0$ or Fixed-Hop $+M$ shift. | $O(F E \log V)$ |
| **2. Diminishing-Returns Grid / DAG Walks** | $K$ walks collecting cell/SCC rewards **at most once**. | Tarjan SCC (if cyclic) + Vertex split $(1, -W_v)$ & $(K-1, 0)$ + DAG DP $\pi_0$. | $O(K(V+E)\log V)$ |
| **3. Separable Convex / Quadratic Degree Costs** | Cost $\sum f_v^2$, $\sum \binom{d^+(v)}{2}$, or piecewise-linear brackets. | Split into $U$ unit marginal edges $\Delta \phi(k)$ (or $P$ breakpoint arcs); use Lazy Insertion if $M P$ is huge. | $O(F E \log V)$ |
| **4. Tournament 3-Cycle Maximization** | Orient undecided edges of tournament to maximize 3-cycles. | Complement $\binom{n}{3} - \sum_v \binom{d^+(v)}{2}$; marginal cost $w_0(v) + k - 1$. | $O(N^3 \log N)$ |
| **5. $k$-Interval Packing (Upper Bound $\le K$)** | Select intervals to max weight with overlap $\le K$. | Half-open $[L_i, R_i)$, forward spine $t \to t+1$ (cap $K$, cost $0$), interval $(l_i \to r_i, 1, -w_i)$, DAG DP $\pi_0$. | $O(K (N+M) \log M)$ |
| **6. 1D Interval Coverage ($\ge A_t$ or $\in [L_t, R_t]$)** | Hire intervals to cover timeline demands $A_t$ at min cost. | Consecutive Equation-Difference $\Delta E_t = E_t - E_{t-1}$; volunteer $(L_j \to R_j+1, \infty, c_j)$, slack $(t+1 \to t, \infty, 0)$. | $O(F E \log V)$ |
| **7. Vertical Tree-Path Coverage ($\ge A_u$)** | Select ancestor–descendant paths to cover tree nodes $u$. | **Tree Equation-Difference** $\Delta^{\text{tree}} E_u = E_u - \sum_{v \in \text{child}(u)} E_v$; path $(d_j \to \text{pa}(a_j))$, slack $(\text{pa}(u) \to u)$. | $O(F E \log V)$ |
| **8. Point Variables & Interval Constraints** | Choose $x_i \in [0, C_i]$ at points $i$ s.t. $\sum_{i=L_j}^{R_j} x_i \ge D_j$. | **LP Dual Transposition** (swap variables and constraints) $\to$ 1D Equation-Difference. | $O(F E \log V)$ |
| **9. Large-Scale Exact Cardinality $K$ ($N \ge 10^5$)** | Pick $K$ items/paths on timeline or tree when MCMF TLEs. | Prove slope convexity of $C(k)$ via MCMF equivalence $\to$ **WQS Binary Search** + Greedy Heap / Tree DP. | $O(N \log N \log C)$ |
| **10. Lower Bounds & Negative Cycles** | Edge bounds $[l_e, u_e]$ or negative cycles in circulation. | **Mandatory Initial Saturation** ($f_e^0 = u_e$ if $c_e < 0$, else $l_e$) + $S^* \to T^*$ imbalance repair. | $O(F E \log V)$ |

---

## 8. Reconciled Master 4-Tier Curated Problem Bank (32 Unique Problems)

Every problem below has been audited across Cohort 1, Cohort 2, and Cohort 3 Gap-Hunting, following the **4-Step "Zero Magic Gadgets" Compilation Mandate** and equipped with **3-Tier Progressive Hints**.

---

### Tier 1: Stepping Stone (`P1.1` – `P1.8`)

---

#### Problem P1.1 — Circular Load Balancing & Cycle-Flow Median Elimination (`Luogu P4016 负载平衡问题` / `Luogu P2512 [HAOI2008] 糖果传递`)
- **Judge URL**: [Luogu P4016](https://www.luogu.com.cn/problem/P4016) ($N \le 100$, 网络流 24 题) / [Luogu P2512](https://www.luogu.com.cn/problem/P2512) ($N \le 10^6$, HAOI 2008)
- **Diagnostic Signal (Step 1)**: $N$ warehouses in a ring hold $A_i$ items ($\bar{A} = \frac{1}{N}\sum A_i \in \mathbb{Z}$). Shifting $1$ item between adjacent warehouses $i \leftrightarrow (i \bmod N) + 1$ costs $1$. Minimize total transport cost so every warehouse holds $\bar{A}$. For $N \le 100$, direct MCMF passes; for $N \le 10^6$, eliminating flow conservation along the cycle yields an $O(N \log N)$ median formula!
- **Algebraic Representation (Step 2)**:
  Let $b_i = A_i - \bar{A}$ be the net supply at node $i$ ($\sum_{i=1}^N b_i = 0$), and let $x_i = f_{i \to i+1} - f_{i+1 \to i} \in \mathbb{R}$ be the net clockwise transfer from $i$ to $i+1$. Flow conservation at each node $i$ is:
  $$x_i - x_{i-1} = b_i \quad (i = 1, \dots, N, \text{ with } x_0 \equiv x_N)$$
  Telescoping from $x_N$ gives $x_i = x_N + \sum_{k=1}^i b_k = x_N - c_i$, where $c_i := -\sum_{k=1}^i (A_k - \bar{A})$. The objective is:
  $$\min_{f \ge 0} \sum_{i=1}^N (f_{i\to i+1} + f_{i+1\to i}) = \min_{x_N \in \mathbb{R}} \sum_{i=1}^N |x_N - c_i|$$
- **Mechanical Graph Compilation & Algebraic Collapse (Step 3)**:
  - **MCMF Network ($N \le 100$)**: Source $S$, sink $T$, ring nodes $1 \dots N$. If $b_i > 0$, add $(S \to i, \text{cap } b_i, \text{cost } 0)$; if $b_i < 0$, add $(i \to T, \text{cap } -b_i, \text{cost } 0)$. For each ring adjacency, add **two directed pairs**: $(i \to i+1, \infty, 1)$ and $(i+1 \to i, \infty, 1)$.
  - **Algebraic Collapse ($N \le 10^6$)**: Because the network is a single cycle, the space of homogeneous circulations is $1$-dimensional (parameterized by $x_N$). Minimizing $\sum_{i=1}^N |x_N - c_i|$ is solved uniquely by setting $x_N = \text{median}(c_1, \dots, c_N)$ in $O(N)$ (`std::nth_element`) or $O(N \log N)$!
- **Toy Trace (Step 4)**: $A = (7, 1, 2, 6)$, $\bar{A} = 4$, $b = (+3, -3, -2, +2)$. Prefix offsets $c = (-3, 0, 2, 0)$. Sorted $c = (-3, 0, 0, 2)$, median $x_4 = 0$, minimum cost $|-3| + |0| + |2| + |0| = 5$.
- **Progressive Hints**:
  - *Hint 1*: Express the net imbalance at each node as $b_i = A_i - \bar{A}$. How do you model bidirectional unit-cost edges in MCMF?
  - *Hint 2*: For $N = 10^6$, let $x_i$ be the net signed flow from $i$ to $i+1$. Express every $x_i$ in terms of $x_N$.
  - *Hint 3*: Once $x_i = x_N - c_i$, total cost is $\sum |x_N - c_i|$, minimized at the median of $\{c_i\}$.

---

#### Problem P1.2 — Grid $K$-Walks with Diminishing Returns (`POJ 3422 Kaka's Matrix Travels` / `Luogu P2045 方格取数加强版`)
- **Judge URL**: [POJ 3422](http://poj.org/problem?id=3422) / [Luogu P2045](https://www.luogu.com.cn/problem/P2045) ($N \le 50, K \le 10, A_{i,j} \in [0, 1000]$)
- **Diagnostic Signal (Step 1)**: Route $K$ monotone paths from $(1,1)$ to $(N,N)$ moving right/down. Cell $(i,j)$ yields reward $A_{i,j}$ on the **first visit** and $0$ on subsequent visits. Greedy 1-by-1 DP fails (classic Suurballe diamond counterexample); $K \le 10$ signals $K$-unit MCMF with convex marginal splitting.
- **Algebraic Representation (Step 2)**:
  Let $f_{i,j} \in \{0, 1, \dots, K\}$ be the number of walks passing through cell $(i,j)$. The reward $\phi(f_{i,j}) = A_{i,j} \cdot \min(1, f_{i,j})$ has diminishing marginal returns $\Delta \phi(1) = A_{i,j} \ge \Delta \phi(2) = \dots = \Delta \phi(K) = 0$. Negating into costs yields convex marginals $\Delta c(1) = -A_{i,j} \le 0 = \Delta c(2) = \dots = \Delta c(K)$.
- **Mechanical Graph Compilation (Step 3)**:
  - Split each cell $(i,j)$ into $u_{\text{in}}(i,j)$ and $u_{\text{out}}(i,j)$ connected by **two parallel arcs**:
    1. Reward arc: $(u_{\text{in}} \to u_{\text{out}}, \text{cap } 1, \text{cost } -A_{i,j})$.
    2. Bypass arc: $(u_{\text{in}} \to u_{\text{out}}, \text{cap } K - 1, \text{cost } 0)$.
  - Grid transitions: $(u_{\text{out}}(i,j) \to u_{\text{in}}(i+1,j), \text{cap } K, \text{cost } 0)$ and $(u_{\text{out}}(i,j) \to u_{\text{in}}(i,j+1), \text{cap } K, \text{cost } 0)$.
  - Since the grid is a DAG ordered by $i + j$, compute $\pi_0$ via $O(N^2)$ topological DP and run $K$ steps of Dijkstra SSP in $O(K N^2 \log N)$.
- **Broken Gadget Check (Step 4)**: If you enforce vertex-disjointness (capacity $1$ total on $u_{\text{in}} \to u_{\text{out}}$), walks get blocked when $K > 2$; the $(K-1, 0)$ bypass arc is mandatory so walks may share cells without double-counting $A_{i,j}$.
- **Progressive Hints**:
  - *Hint 1*: How does the marginal reward of cell $(i,j)$ change between the 1st visit and visits $2 \dots K$?
  - *Hint 2*: Split each cell into `in` and `out` vertices connected by two parallel edges of capacities $1$ and $K-1$.
  - *Hint 3*: Initialize Johnson potentials $\pi_0$ in $O(N^2)$ by row-major DP before running $K$ Dijkstra augmentations.

---

#### Problem P1.3 — Maximum Weight $k$-Interval Packing (`Luogu P3358 最长k可重区间集问题` / `POJ 3680 Intervals`)
- **Judge URL**: [Luogu P3358](https://www.luogu.com.cn/problem/P3358) ($N \le 500, K \le 3$, open intervals) / [POJ 3680](http://poj.org/problem?id=3680) ($N \le 200, K \le 10^5$)
- **Diagnostic Signal (Step 1)**: Select a subset of weighted intervals so no point is covered $> K$ times. Coordinates up to $10^9$ require discretization to $M \le 2N$ endpoints.
- **Algebraic Representation (Step 2)**:
  Normalize open $(a_i, b_i)$ to $[L_i, R_i) = [a_i, b_i)$, compress unique endpoints $p_1 < \dots < p_M$, and write $\sum_{i : l_i \le t < r_i} x_i + y_t = K$ for $t = 1 \dots M-1$ ($x_i \in [0, 1], y_t \in [0, K]$).
- **Mechanical Graph Compilation (Step 3)**:
  - Differencing $\Delta E_t = E_t - E_{t-1}$ compiles $y_t$ into forward spine $(t \to t+1, \text{cap } K, \text{cost } 0)$ and $x_i$ into $(l_i \to r_i, \text{cap } 1, \text{cost } -w_i)$.
  - Source $(s \to 1, \text{cap } K, \text{cost } 0)$, sink $t = M$. Compute $\pi_0$ by $O(N + M)$ DAG DP and run SSP in $O(\min(K, N) (N+M) \log M)$.
- **Endpoint Trap (Step 4)**: For open intervals (`Luogu P3358`), $(1, 2)$ and $(2, 3)$ do **not** overlap at $2$, so $l_i = \text{rank}(a_i), r_i = \text{rank}(b_i)$ directly allows $1 \to 2 \to 3$ on a single lane. If intervals were closed $[a_i, b_i]$, we would map $b_i \mapsto b_i + 1$ before compression.
- **Progressive Hints**:
  - *Hint 1*: Only the $2N$ interval endpoints matter; compress them into $1 \dots M$.
  - *Hint 2*: Route $K$ units of flow along the spine $1 \to 2 \to \dots \to M$, and let interval $i$ be a shortcut $l_i \to r_i$ of capacity $1$ and cost $-w_i$.
  - *Hint 3*: Compute initial potentials $\pi_0$ in $O(N+M)$ topological order so Dijkstra runs without SPFA.

---

#### Problem P1.4 — Exact Vertex-Visit Lower Bounds (`Luogu P4553 80人环游世界`)
- **Judge URL**: [Luogu P4553](https://www.luogu.com.cn/problem/P4553) ($N \le 100, M \le 70, V_i \le 70$)
- **Diagnostic Signal (Step 1)**: Up to $M$ travellers traverse a DAG of $N$ countries; country $i$ must be visited **exactly $V_i$ times**, and edge $(i \to j)$ costs $c_{ij}$ per person. Minimize total travel cost.
- **Algebraic Representation (Step 2)**:
  Split country $i$ into $i_{\text{in}} \to i_{\text{out}}$ with lower and upper flow bounds $[l_e, u_e] = [V_i, V_i]$ and cost $0$. Total travelers used is bounded by $[0, M]$ on $(s \to T_{\text{start}})$.
- **Mechanical Graph Compilation (Step 3)**:
  - Add $(s \to v_0, [0, M], 0)$, $(v_0 \to i_{\text{in}}, [0, \infty), 0)$, $(i_{\text{out}} \to t, [0, \infty), 0)$, $(i_{\text{out}} \to j_{\text{in}}, [0, \infty), c_{ij})$, and feedback $(t \to s, [0, \infty), 0)$.
  - For each country $i$, pre-saturate $(i_{\text{in}} \to i_{\text{out}})$ with $V_i$ units (creating no residual edge since $u_e - l_e = 0$), which sets $M(i_{\text{out}}) = +V_i \implies (S^* \to i_{\text{out}}, V_i, 0)$ and $M(i_{\text{in}}) = -V_i \implies (i_{\text{in}} \to T^*, V_i, 0)$.
  - Since all $c_{ij} \ge 0$, run Dijkstra MCMF from $S^*$ to $T^*$ in $O((\sum V_i) N^2 \log N)$.
- **Toy Check (Step 4)**: Because $l_e = u_e = V_i$, the edge $i_{\text{in}} \to i_{\text{out}}$ disappears completely from $G^*$ after pre-saturation, leaving only $(S^* \to i_{\text{out}})$ and $(i_{\text{in}} \to T^*)$!
- **Progressive Hints**:
  - *Hint 1*: Model "visited exactly $V_i$ times" as flow bounds $[V_i, V_i]$ on the internal vertex-split edge $i_{\text{in}} \to i_{\text{out}}$.
  - *Hint 2*: Add a feedback edge $t \to s$ of capacity $\infty$ and cost $0$, then apply the $S^* \to T^*$ lower-bound transformation.
  - *Hint 3*: Because $u_e - l_e = V_i - V_i = 0$, the internal edge has $0$ residual capacity; the minimum cost of saturating $S^* \to T^*$ is the exact answer.

---

#### Problem P1.5 — Parametric Slope Extraction on Bipartite Matching (`AtCoder ABC 247 G — Dream Team`)
- **Judge URL**: [AtCoder ABC 247 G](https://atcoder.jp/contests/abc247/tasks/abc247_g) ($N \le 3\times 10^4$, grid $150 \times 150$, $C_i \le 10^9$)
- **Diagnostic Signal (Step 1)**: Each contestant has university $A_i \in [1, 150]$, subject $B_i \in [1, 150]$, power $C_i$. Pick $k$ contestants with distinct $A_i$ and distinct $B_i$ maximizing sum of $C_i$, and output the answer for **every** $k = 1, 2, \dots, K_{\max}$.
- **Algebraic Representation (Step 2)**:
  For parallel contestants with identical $(A_i, B_i)$, only the maximum $C_i$ can ever be chosen (capacity is $1$ on $A_i$ and $B_i$). Each chosen contestant is a unit of flow on $s \to u_A \to v_B \to t$, so the maximum profit for size $k$ is $-C(k)$ along the SSP augmentation curve!
- **Mechanical Graph Compilation (Step 3)**:
  - Deduplicate edges to at most $150^2$ pairs $(u_a \to v_b, \text{cap } 1, \text{cost } M - C_{a,b})$ where $M = 10^9$ (valid by **Remedy 1: Fixed-Hop Shift**, since every $s$-$t$ flow crosses $L \to R$ with net count $+1$ per unit!).
  - Run SSP (or `atcoder::mcf_graph::slope(s, t)`). The $k$-th unit of flow gives answer $k \cdot M - C_{\text{shifted}}(k)$ in $O(K_{\max} E \log V)$ ($V = 302, K_{\max} \le 150$).
- **Slope Pitfall (Step 4)**: When using `mcf_graph::slope(s, t)`, the returned vector contains only the **hull corner vertices** $(f_j, C(f_j))$; you must linearly interpolate integer steps $f \in [f_{j-1}, f_j]$ between consecutive corners!
- **Progressive Hints**:
  - *Hint 1*: Why can at most one person per $(A_i, B_i)$ pair ever be selected?
  - *Hint 2*: Add $M = 10^9$ to each $L \to R$ edge cost $M - C_i \ge 0$, run SSP, and record the cumulative cost after each unit of flow.
  - *Hint 3*: Subtract $k \cdot M$ from the negated cost after step $k$.

---

#### Problem P1.6 — SCC Contraction + Topological Potential Pre-Shift (`AtCoder ABC 214 H — Collecting`)
- **Judge URL**: [AtCoder ABC 214 H](https://atcoder.jp/contests/abc214/tasks/abc214_h) ($N, M \le 2\times 10^5, K \le 10, X_i \le 10^9$)
- **Diagnostic Signal (Step 1)**: $K \le 10$ tokens start at vertex $1$ on a directed graph ($N, M \le 2\times 10^5$) and collect $X_v$ on the first visit to $v$. Cycles exist in the input graph, and $N = 2\times 10^5$ forbids SPFA!
- **Algebraic Representation (Step 2)**:
  Any token entering a Strongly Connected Component (SCC) $C$ can visit every vertex in $C$. Contracting SCCs via Tarjan's algorithm in $O(N+M)$ produces a **Condensation DAG** with $C_{\text{cnt}} \le N$ nodes and aggregated weights $W_C = \sum_{v \in C} X_v$.
- **Mechanical Graph Compilation (Step 3)**:
  - Split each SCC $C$ reachable from $\text{scc}(1)$ into $C_{\text{in}} \to C_{\text{out}}$ with two arcs: $(1, -W_C)$ and $(K-1, 0)$. Add $(C_{\text{out}} \to T, K, 0)$ and DAG edges $(u_{\text{out}} \to v_{\text{in}}, K, 0)$.
  - **Remedy 2 (Topological Potential Pre-Shift)**: Compute $\pi_0(v)$ via topological DP in $O(V + E)$, shift every edge cost to $c_{uv}^{\pi_0} = c_{uv} + \pi_0(u) - \pi_0(v) \ge 0$, and run $K \le 10$ passes of Dijkstra in $O(K (N + M) \log N)$!
- **Toy Check (Step 4)**: Without SCC contraction, initial cycles with negative vertex-reward edges create negative-cost cycles and break MCMF.
- **Progressive Hints**:
  - *Hint 1*: Contract SCCs first so the graph becomes a DAG with aggregated SCC weights $W_C$.
  - *Hint 2*: Split each SCC into `in` and `out` connected by $(1, -W_C)$ and $(K-1, 0)$.
  - *Hint 3*: Compute $\pi_0$ via topological DP in $O(N+M)$ so all $K \le 10$ augmentations use pure Dijkstra.

---

#### Problem P1.7 — Range-Bound Intersection + Quadratic Marginal Splitting (`Codeforces 863 F — Almost Permutation`)
- **Judge URL**: [Codeforces 863 F](https://codeforces.com/problemset/problem/863/F) ($N \le 50, Q \le 100$)
- **Diagnostic Signal (Step 1)**: Construct array $a[1 \dots N] \in \{1, \dots, N\}^N$ subject to range min/max queries ($\forall i \in [l, r], a_i \ge v$ or $a_i \le v$) minimizing $\sum_{x=1}^N \text{cnt}(x)^2$.
- **Algebraic Representation (Step 2)**:
  Intersect all constraints at index $i$ to obtain $a_i \in [L_i, R_i]$ (if $L_i > R_i$, output $-1$). The objective $\sum_{x=1}^N \text{cnt}(x)^2$ is separable convex with odd marginal steps $\Delta(k^2) = k^2 - (k-1)^2 = 2k - 1$ for $k = 1, 2, \dots, N$.
- **Mechanical Graph Compilation (Step 3)**:
  - Source $S \to \text{val}_x$ has **$N$ parallel unit-capacity edges** with costs $1, 3, 5, \dots, 2N-1$.
  - Value $\text{val}_x \to \text{pos}_i$ has capacity $1$, cost $0$ whenever $L_i \le x \le R_i$.
  - Position $\text{pos}_i \to T$ has capacity $1$, cost $0$. Run MCMF of volume $N$ in $O(N^3 \log N)$.
- **Progressive Hints**:
  - *Hint 1*: First compute the tightest valid interval $[L_i, R_i]$ for each position $i$ independently.
  - *Hint 2*: What is the marginal cost of assigning a value $x$ for the $k$-th time ($k^2 - (k-1)^2$)?
  - *Hint 3*: Add $N$ edges from $S$ to each value node $x$ with capacity $1$ and costs $1, 3, \dots, 2N-1$.

---

#### Problem P1.8 — Minimum-Cost DAG Edge Cover with Lower Bounds (`Luogu P4043 [AHOI2014 / JSOI2014] 支线剧情`)
- **Judge URL**: [Luogu P4043](https://www.luogu.com.cn/problem/P4043) ($N \le 300, K_i \le 50$)
- **Diagnostic Signal (Step 1)**: Starting from node $1$ in a story DAG, every story choice edge $e = (u \to v)$ (duration $t_e \ge 0$) must be traversed **at least once**. You can restart at node $1$ from any node $u > 1$ at cost $0$. Minimize total time.
- **Algebraic Representation (Step 2)**:
  Each story edge $e = (u \to v)$ has lower/upper flow bounds $[1, \infty)$ and cost $t_e \ge 0$. Restarting from $u > 1$ to $1$ is an edge $(u \to 1, [0, \infty), \text{cost } 0)$.
- **Mechanical Graph Compilation (Step 3)**:
  - Pre-send $f_e^0 = 1$ on every story edge $e = (u \to v)$, accumulating $C_{\text{base}} = \sum_e t_e$ and $M(v) = \text{in}^0(v) - \text{out}^0(v)$, while keeping residual edge $(u \to v, \infty, t_e)$.
  - Add $(S^* \to v, M(v), 0)$ for $M(v) > 0$ and $(v \to T^*, -M(v), 0)$ for $M(v) < 0$.
  - Since all $t_e \ge 0$, run Dijkstra MCMF from $S^*$ to $T^*$ with $\pi_0 \equiv 0$, and output $C_{\text{base}} + C_{S^*\to T^*}$.
- **Progressive Hints**:
  - *Hint 1*: Model "restart from any node $u > 1$" as a free edge $(u \to 1, \text{cap } \infty, \text{cost } 0)$.
  - *Hint 2*: Every story edge has lower bound $l_e = 1$ and upper bound $\infty$.
  - *Hint 3*: Pre-saturate $1$ unit on every story edge and use $S^* \to T^*$ MCMF to balance vertex excesses/deficits.

---

### Tier 2: Intermediate (`P2.1` – `P2.8`)

---

#### Problem P2.1 — Tournament 3-Cycle Maximization (`Luogu P4249 [WC2007] 剪刀石头布`)
- **Judge URL**: [Luogu P4249](https://www.luogu.com.cn/problem/P4249) ($N \le 100$)
- **Diagnostic Signal (Step 1)**: Orient the undecided edges of an $N$-vertex tournament to maximize directed 3-cycles, and reconstruct the full adjacency matrix.
- **Algebraic Representation (Step 2)**:
  By Section 4.2.B, $\text{3-Cycles} = \binom{N}{3} - \sum_{v=1}^N \binom{d^+(v)}{2}$. Let $w_0(v)$ be the number of already-fixed wins of $v$, and $rem(v)$ be its number of undecided matches. The $k$-th additional win for $v$ ($k = 1 \dots rem(v)$) increases $\binom{d^+(v)}{2}$ by $w_0(v) + k - 1$.
- **Mechanical Graph Compilation (Step 3)**:
  - For each undecided match $e = \{u, v\}$ ($u < v$), add match node $m_e$ with $(S \to m_e, 1, 0)$, $(m_e \to u, 1, 0)$, $(m_e \to v, 1, 0)$.
  - For each vertex $v$, add $rem(v)$ parallel unit-capacity edges $(v \to T)$ with costs $w_0(v), w_0(v)+1, \dots, w_0(v)+rem(v)-1$.
  - Run MCMF (all costs $\ge 0$), subtract $\sum_v \binom{w_0(v)}{2} + C_{\min}$ from $\binom{N}{3}$, and read the winner of each match $e$ from whichever of $(m_e \to u)$ or $(m_e \to v)$ carries flow $1$.
- **Progressive Hints**:
  - *Hint 1*: Count non-3-cycle triples instead: every transitive triple has a unique vertex with $2$ wins inside the triple.
  - *Hint 2*: Minimize $\sum_v \binom{d^+(v)}{2}$ where $d^+(v) = w_0(v) + f_v$.
  - *Hint 3*: Remember to offset marginal edge costs by the pre-existing wins $w_0(v)$!

---

#### Problem P2.2 — Coupled Win/Loss Quadratic Costs (`Luogu P4307 [JSOI2009] 球队收益 / 球队预算`)
- **Judge URL**: [Luogu P4307](https://www.luogu.com.cn/problem/P4307) ($N \le 5000, M \le 1000$)
- **Diagnostic Signal (Step 1)**: $N$ teams, $M$ remaining matches. Team $i$ has initial wins $w_0(i)$, initial losses $l_0(i)$, remaining matches $rem(i)$, and final cost $C_i W_i^2 + D_i L_i^2$. Minimize total cost.
- **Algebraic Representation (Step 2)**:
  Since $W_i + L_i = T_i := w_0(i) + l_0(i) + rem(i)$ is constant, assume initially that team $i$ **loses all remaining matches** ($W_i^{(0)} = w_0(i), L_i^{(0)} = l_0(i) + rem(i)$), giving base cost $C_{\text{base}} = \sum_{i=1}^N \big(C_i w_0(i)^2 + D_i (l_0(i) + rem(i))^2\big)$.
  When team $i$ wins its $k$-th remaining match ($k = 1 \dots rem(i)$), its wins change from $w = w_0(i) + k - 1$ to $w + 1$ and its losses change from $l = l_0(i) + rem(i) - k + 1$ to $l - 1$, yielding marginal cost:
  $$\Delta_i(k) = C_i(2w + 1) - D_i(2l - 1)$$
  Since $\Delta_i(k+1) - \Delta_i(k) = 2(C_i + D_i) \ge 0$, the marginals are strictly non-decreasing!
- **Mechanical Graph Compilation (Step 3)**:
  - Match nodes $S \to m_e \to \{u_e, v_e\}$ (cap $1$, cost $0$).
  - Team $i \to T$ has $rem(i)$ unit-capacity edges with costs $\Delta_i(1) \le \dots \le \Delta_i(rem(i))$. Since $\Delta_i(k)$ can be negative when $D_i > 0$, either shift every $(i \to T)$ edge by $+K_{\text{shift}}$ (valid by **Remedy 1: Fixed-Hop Shift** since every unit of flow crosses $(i \to T)$ once!) or use bipartite $\pi_0$.
- **Progressive Hints**:
  - *Hint 1*: Do not create separate flow variables for wins and losses; use $L_i = T_i - W_i$.
  - *Hint 2*: Initialize by assuming every team loses all remaining matches, then compute the marginal cost of converting the $k$-th loss into a win.
  - *Hint 3*: Add a constant shift $+K_{\text{shift}}$ to all $(i \to T)$ edges so Dijkstra runs with $\pi_0 \equiv 0$, then subtract $M \cdot K_{\text{shift}}$ at the end.

---

#### Problem P2.3 — $K$-Machine Interval Scheduling with Anti-SPFA DAG Potentials (`Codeforces 164 C — Machine Programming`)
- **Judge URL**: [Codeforces 164 C](https://codeforces.com/problemset/problem/164/C) ($N \le 1000, K \le 50, s_i, t_i, c_i \le 10^9$)
- **Diagnostic Signal (Step 1)**: $N$ tasks $[s_i, s_i + t_i)$ with profit $c_i$, $K$ machines, reconstruct which tasks are chosen ($0/1$). Codeforces tests include Anti-SPFA graphs where naive SPFA MCMF TLEs!
- **Algebraic Representation & Compilation (Steps 2 & 3)**:
  Compress the $2N$ endpoints $s_i$ and $s_i + t_i$ into $1 \dots M$ ($M \le 2000$). Add spine $(t \to t+1, \text{cap } K, \text{cost } 0)$ and task edge $e_i = (\text{rank}(s_i) \to \text{rank}(s_i + t_i), \text{cap } 1, \text{cost } -c_i)$.
  Compute $\pi_0(v)$ via $O(N + M)$ topological DP on the DAG $1 \dots M$, then run at most $K$ Dijkstra passes (stopping early if $\pi_k(M) \ge 0$). Task $i$ is selected iff $r_f(e_i) = 0$.
- **Progressive Hints**:
  - *Hint 1*: $[s_i, s_i + t_i)$ is already half-open; compress $\{s_i, s_i + t_i\}$ into $1 \dots M$.
  - *Hint 2*: Why is the initial graph guaranteed to be a DAG? Compute $\pi_0$ in one left-to-right pass!
  - *Hint 3*: Store the edge index of each task $i$ to output `1` if its residual capacity is $0$ after MCMF.

---

#### Problem P2.4 — Piecewise-Linear Breakpoint Bundling (`Luogu P2488 [SDOI2011] 工作安排`)
- **Judge URL**: [Luogu P2488](https://www.luogu.com.cn/problem/P2488) ($M, N \le 250, P \le 5$)
- **Diagnostic Signal (Step 1)**: $M$ employees, $N$ products (demand $C_j$). Employee $i$'s anger is a $P+1$-piece convex piecewise-linear function of total tasks $x_i$ with breakpoints $0 = T_{i,0} < T_{i,1} < \dots < T_{i,P} < \infty$ and slopes $W_{i,1} < \dots < W_{i,P+1}$. Since $\sum C_j$ can be large, unit-edge splitting is too slow!
- **Algebraic Representation & Compilation (Steps 2 & 3)**:
  By the **Piecewise-Linear Bundling Table** (Section 4.3.A), compile employee $i$'s workload $S \to \text{emp}_i$ into **$P+1 \le 6$ parallel arcs**: arc $k \in \{1, \dots, P\}$ has capacity $T_{i,k} - T_{i,k-1}$ and cost $W_{i,k}$, while arc $P+1$ has capacity $\infty$ and cost $W_{i,P+1}$. Connect $\text{emp}_i \to \text{prod}_j$ (cap $\infty$, cost $0$) if $A_{i,j} = 1$, and $\text{prod}_j \to T$ (cap $C_j$, cost $0$). Run MCMF in $O(F E \log V)$ where $E \le 6M + MN$.
- **Progressive Hints**:
  - *Hint 1*: Do not split employee $i$'s workload into unit edges; bundle each constant-slope bracket $[T_{i,k-1}, T_{i,k}]$ into a single edge!
  - *Hint 2*: Because $W_{i,1} < W_{i,2} < \dots < W_{i,P+1}$, MCMF saturates bracket $k$ before touching bracket $k+1$.
  - *Hint 3*: Watch out for 64-bit integer overflow (`long long`) in total anger.

---

#### Problem P2.5 — Degree-Bounded Planar Arborescence (`Codeforces 277 E — Binary Tree on Plane`)
- **Judge URL**: [Codeforces 277 E](https://codeforces.com/problemset/problem/277/E) ($N \le 400$)
- **Diagnostic Signal (Step 1)**: Build a rooted binary tree on $N$ planar points where parents have strictly greater $y$-coordinate than children ($y_u > y_v$) and out-degree $\le 2$, minimizing sum of Euclidean edge lengths.
- **Algebraic Representation & Compilation (Steps 2 & 3)**:
  Every node except the unique global maximum-$y$ root $r$ must have in-degree $1$, and every node has out-degree $\le 2$. Since $y_u > y_v$ is a strict partial order, no directed cycles can form! Thus degree constraints alone guarantee a valid tree.
  Build a bipartite network: $(S \to u_{\text{out}}, \text{cap } 2, \text{cost } 0)$ for all $u$; $(v_{\text{in}} \to T, \text{cap } 1, \text{cost } 0)$ for all $v \ne r$; and $(u_{\text{out}} \to v_{\text{in}}, \text{cap } 1, \text{cost } \text{dist}(u,v))$ whenever $y_u > y_v$. If max flow $< N-1$ (e.g., two tied max-$y$ points), output `-1`.
- **Floating-Point Guard (Step 4)**: In `double`-cost Dijkstra, relax only when `d[u] + c_pi < d[v] - 1e-9` to prevent infinite loops on $0$-cost cycles caused by `1e-16` rounding noise.
- **Progressive Hints**:
  - *Hint 1*: Why can a set of directed edges with $y_u > y_v$ never contain a cycle?
  - *Hint 2*: Because cycles are impossible, enforcing in-degree $1$ for all $N-1$ non-root nodes and out-degree $\le 2$ for all nodes is necessary and sufficient!
  - *Hint 3*: Use an $\epsilon = 10^{-9}$ tolerance when relaxing floating-point reduced costs in Dijkstra.

---

#### Problem P2.6 — Sliding-Window Subsequence Packing (`BZOJ 1283 序列`)
- **Judge URL**: [Hydro BZOJ 1283](https://hydro.ac/p/bzoj-P1283) ($N \le 1000, M \le 100, K \le 10$)
- **Diagnostic Signal (Step 1)**: Pick a subsequence from $c_1, \dots, c_N \ge 0$ maximizing total weight such that every contiguous window of length $M$ contains at most $K$ chosen elements.
- **Algebraic Representation & Compilation (Steps 2 & 3)**:
  Selecting element $i$ occupies $1$ unit of capacity across all windows covering $i$, which is equivalent to an interval $[i, \min(N+1, i+M))$ on the timeline $1 \dots N+1$.
  Build spine $(t \to t+1, \text{cap } K, \text{cost } 0)$ for $t = 1 \dots N$, and item edge $(i \to \min(N+1, i+M), \text{cap } 1, \text{cost } -c_i)$. Initialize $\pi_0$ via $O(N)$ DAG DP and run $K$ steps of Dijkstra SSP in $O(K N \log N)$.
- **Progressive Hints**:
  - *Hint 1*: Think of choosing index $i$ as locking $1$ slot for $M$ consecutive steps $i \to i + M$.
  - *Hint 2*: Use a spine $1 \to 2 \to \dots \to N+1$ of capacity $K$ and cost $0$, with shortcut $(i \to \min(N+1, i+M), 1, -c_i)$.
  - *Hint 3*: Compute $\pi_0$ by linear DP before running $K$ Dijkstra passes.

---

#### Problem P2.7 — $K=4$ Disjoint Subsequences via Persistent Suffix Relay Hubs (`Codeforces 818 G — Four Melodies`)
- **Judge URL**: [Codeforces 818 G](https://codeforces.com/problemset/problem/818/G) ($N \le 3000, K = 4$)
- **Diagnostic Signal (Step 1)**: Find $4$ vertex-disjoint subsequences maximizing total length where adjacent elements $i < j$ satisfy $|a_i - a_j| = 1$ or $a_i \equiv a_j \pmod 7$. Naive $O(N^2)$ transitions create $4.5 \times 10^6$ edges; persistent suffix relay hubs compress this to $O(N)$ edges!
- **Algebraic Representation & Compilation (Steps 2 & 3)**:
  Split each element $i$ into $i_{\text{in}} \to i_{\text{out}}$ (cap $1$, cost $-1$). Instead of connecting $i_{\text{out}}$ to all $j > i$, maintain from right to left ($i = N \dots 1$) the **next occurrence** $\text{nxt}_{\text{mod}}[r]$ ($r \in [0, 6]$) and $\text{nxt}_{\text{val}}[v]$ ($v \in [1, 10^5]$). Create at element $i$ two relay hubs:
  - $H_{\text{mod}}(i)$: connected to $i_{\text{in}}$ (cap $1$, cost $0$) and to $H_{\text{mod}}(\text{nxt}_{\text{mod}}[a_i \bmod 7])$ (cap $K$, cost $0$).
  - $H_{\text{val}}(i)$: connected to $i_{\text{in}}$ (cap $1$, cost $0$) and to $H_{\text{val}}(\text{nxt}_{\text{val}}[a_i])$ (cap $K$, cost $0$).
  Then $i_{\text{out}}$ needs **only 3 outgoing transition edges**: to $H_{\text{mod}}(\text{nxt}_{\text{mod}}[a_i \bmod 7])$, $H_{\text{val}}(\text{nxt}_{\text{val}}[a_i - 1])$, and $H_{\text{val}}(\text{nxt}_{\text{val}}[a_i + 1])$!
  Because all edges go from smaller index to larger index, compute $\pi_0$ via $O(N)$ DAG DP and run $4$ Dijkstra passes in $O(N \log N)$!
- **Progressive Hints**:
  - *Hint 1*: Split each index $i$ into $i_{\text{in}} \to i_{\text{out}}$ of capacity $1$ and cost $-1$ to enforce vertex-disjointness.
  - *Hint 2*: Create chain relay hubs for each $\bmod 7$ class and each exact value so $i_{\text{out}}$ only connects to the first valid successor in each class.
  - *Hint 3*: The relay-hub graph is still a DAG; use $O(N)$ topological DP for $\pi_0$ and 4 Dijkstra augmentations.

---

#### Problem P2.8 — Dynamic Lazy Edge Insertion for Waiting-Time Convexity (`Luogu P2050 [NOI2012] 美食节`)
- **Judge URL**: [Luogu P2050](https://www.luogu.com.cn/problem/P2050) ($N \le 40$ dishes, $M \le 100$ chefs, total dishes $P = \sum p_i \le 800$)
- **Diagnostic Signal (Step 1)**: Dish $i$ is ordered $p_i$ times ($P = \sum p_i \le 800$). Chef $j$ takes $t_{i,j}$ time to cook dish $i$. Minimize the sum of completion times of all $P$ dishes.
  If chef $j$ cooks $k_j$ dishes in order $d_1, d_2, \dots, d_{k_j}$, the **last** dish cooked by chef $j$ contributes $1 \times t_{d_{k_j}, j}$ to total waiting time, the second-to-last contributes $2 \times t_{d_{k_j-1}, j}$, ..., and the $k$-th dish from the end contributes $k \times t_{d, j}$!
  Pre-building all $M \times P = 80\,000$ chef-slot vertices with $N \times M \times P = 3.2 \times 10^6$ edges TLEs—requiring **Dynamic Lazy Edge Insertion (`动态加边`)**!
- **Algebraic Representation (Step 2)**:
  Assigning a dish of type $i$ to the **$k$-th reverse slot** ($k = 1, 2, \dots$) of chef $j$ incurs marginal cost $k \cdot t_{i,j}$. Since $1 \cdot t_{i,j} < 2 \cdot t_{i,j} < 3 \cdot t_{i,j} \dots$, chef $j$'s reverse slot $k+1$ will **never** be used before reverse slot $k$ is saturated!
- **Mechanical Graph Compilation (Step 3)**:
  - Dish vertices $i \in \{1, \dots, N\}$ with $(S \to i, \text{cap } p_i, \text{cost } 0)$.
  - Initially allocate **only slot $k = 1$** for each chef $j \in \{1, \dots, M\}$: add vertex $v_{j, 1}$ with $(v_{j, 1} \to T, \text{cap } 1, \text{cost } 0)$ and edges $(i \to v_{j, 1}, \text{cap } 1, \text{cost } 1 \cdot t_{i,j})$ for all $i = 1 \dots N$.
  - **Lazy Insertion Loop**: In each of the $P$ SSP augmentations, find the shortest augmenting path from $S$ to $T$. Suppose this path saturates $(v_{j^*, k} \to T)$ for chef $j^*$. Immediately allocate a single new vertex $v_{j^*, k+1}$, add $(v_{j^*, k+1} \to T, \text{cap } 1, \text{cost } 0)$, and add $N$ edges $(i \to v_{j^*, k+1}, \text{cap } 1, \text{cost } (k+1) \cdot t_{i,j^*})$!
  - Total active vertices $\le N + M + P \le 940$, total active edges $\le N(M + P) \le 36\,000$, running in $< 50\text{ ms}$!
- **Potential Update for Newly Spawned Node (Step 4)**: When spawning $v_{j^*, k+1}$ inside a Dijkstra-based SSP solver, its initial potential before the next Dijkstra pass is simply $\pi(v_{j^*, k+1}) = \min_{1 \le i \le N} (\pi(i) + (k+1) t_{i, j^*})$ (and since $(v_{j^*, k+1} \to T)$ has cost $0$ and $\pi(v_{j^*, k+1}) \ge \pi(v_{j^*, k}) = \pi(T)$, $c^\pi(v_{j^*, k+1} \to T) \ge 0$ is automatically preserved!).
- **Progressive Hints**:
  - *Hint 1*: Count each chef's dishes from the **last** dish backwards: the $k$-th dish from the end delays exactly $k$ dishes (itself and the $k-1$ dishes after it), contributing $k \cdot t_{i,j}$.
  - *Hint 2*: Why can reverse slot $k+1$ of chef $j$ never be chosen before reverse slot $k$ of chef $j$?
  - *Hint 3*: Start with only slot $k=1$ for each chef; whenever chef $j$'s current slot $k$ is saturated by an augmenting path, dynamically add slot $(j, k+1)$ and its $N$ incoming dish edges!

---

### Tier 3: Advanced (`P3.1` – `P3.8`)

---

#### Problem P3.1 — Flagship Consecutive Equation-Difference (`Luogu P3980 [NOI2008] 志愿者招募`)
- **Judge URL**: [Luogu P3980](https://www.luogu.com.cn/problem/P3980) ($N \le 1000, M \le 10000$)
- **Diagnostic Signal (Step 1)**: Day $t \in [1, N]$ requires $\ge A_t$ volunteers. Type $j \in [1, M]$ works days $[S_j, T_j]$ at cost $C_j$ per person. Minimize total hiring cost.
- **Algebraic Representation & Compilation (Steps 2 & 3)**:
  As derived in Section 6.3.A, write $\sum_{j : S_j \le t \le T_j} x_j - y_t = A_t$ ($x_j, y_t \ge 0$) and take $\Delta E_t = E_t - E_{t-1}$ ($t = 1 \dots N+1$, $A_0 = A_{N+1} = 0$):
  - Volunteer $x_j$: $(S_j \to T_j + 1, \text{cap } \infty, \text{cost } C_j \ge 0)$.
  - Surplus slack $y_t$: $(t + 1 \to t, \text{cap } \infty, \text{cost } 0)$.
  - Node balance $\Delta A_t = A_t - A_{t-1}$: $(S \to t, \Delta A_t, 0)$ if $\Delta A_t > 0$, else $(t \to T, -\Delta A_t, 0)$.
  - Because all initial costs $C_j \ge 0$, set $\pi_0 \equiv 0$ and run Dijkstra MCMF in $O(F (N + M) \log N)$.
- **Progressive Hints**:
  - *Hint 1*: Convert $\sum x_j \ge A_t$ into an equality by subtracting surplus slack $y_t \ge 0$.
  - *Hint 2*: Subtract equation $E_{t-1}$ from $E_t$ for $t = 1 \dots N+1$ ($E_0 = E_{N+1} = 0$).
  - *Hint 3*: Map $+1$ to outflow and $-1$ to inflow: $x_j$ becomes $S_j \to T_j + 1$ (cost $C_j$) and $y_t$ becomes $t+1 \to t$ (cost $0$).

---

#### Problem P3.2 — Prime-Factor Parity Bipartition + Budget-Threshold Prefix Stopping (`Luogu P3705 [SDOI2016] 数字配对`)
- **Judge URL**: [Luogu P3705](https://www.luogu.com.cn/problem/P3705) ($N \le 200, A_i \le 10^9, B_i \le 10^5, C_i \in [-10^5, 10^5]$)
- **Diagnostic Signal (Step 1)**: Type $i$ has $B_i$ copies of value $A_i$ and weight $C_i$. Pair $(i, j)$ can match if $A_i / A_j$ or $A_j / A_i$ is prime, yielding value $C_i \cdot C_j$. Maximize the total number of matched pairs subject to total value $\sum C_i C_j \ge 0$.
- **Algebraic Representation (Step 2)**:
  Let $\Omega(A_i)$ be the number of prime factors of $A_i$ with multiplicity. Every valid edge connects $\Omega(A_i)$ and $\Omega(A_j) = \Omega(A_i) \pm 1$, which have **opposite parities**! Thus the compatibility graph is **bipartite**: $L = \{i : \Omega(A_i) \text{ odd}\}$, $R = \{j : \Omega(A_j) \text{ even}\}$.
  Negating values into costs $c_{ij} = -C_i C_j$, we want to maximize flow $f$ subject to $C(f) \le 0$ (**Stopping Regime 3: Budget-Threshold Prefix Stopping**).
- **Mechanical Graph Compilation (Step 3)**:
  - For $i \in L$: $(S \to i, \text{cap } B_i, \text{cost } 0)$; for $j \in R$: $(j \to T, \text{cap } B_j, \text{cost } 0)$; for valid pairs: $(i \to j, \text{cap } \infty, \text{cost } -C_i C_j)$.
  - Run SSP from $S$ to $T$. Maintain accumulated cost $C_{\text{cur}} \le 0$ and flow $F_{\text{cur}}$. On path $P_k$ with unit cost $d_k$ and bottleneck $\Delta_k$:
    - If $d_k \le 0$: push full $\Delta_k$, update $C_{\text{cur}} \gets C_{\text{cur}} + \Delta_k d_k$.
    - If $d_k > 0$: max affordable units is $\delta = \min(\Delta_k, \lfloor -C_{\text{cur}} / d_k \rfloor)$; add $\delta$ to $F_{\text{cur}}$, update $C_{\text{cur}} \gets C_{\text{cur}} + \delta d_k$, and if $\delta < \Delta_k$, **stop immediately**!
- **Progressive Hints**:
  - *Hint 1*: Count the total prime factors $\Omega(A_i)$ of each number; why can odd-$\Omega$ only match even-$\Omega$?
  - *Hint 2*: Because $C(f)$ is convex, augment along shortest paths (most positive $C_i C_j$ first) to build a profit buffer $-C_{\text{cur}} \ge 0$.
  - *Hint 3*: When path cost $d_k > 0$, take $\min(\Delta_k, \lfloor -C_{\text{cur}} / d_k \rfloor)$ units before terminating.

---

#### Problem P3.3 — Substring Occurrence Interval Packing (`Codeforces 717 G — Underfail`)
- **Judge URL**: [Codeforces 717 G](https://codeforces.com/problemset/problem/717/G) ($N \le 500, M \le 100, X \le 100$)
- **Diagnostic Signal (Step 1)**: Given string $S$ of length $N$ and $M$ weighted dictionary words $(w_j, p_j)$, select non-overlapping occurrences so each index of $S$ is covered at most $X$ times, maximizing total score.
- **Algebraic Representation & Compilation (Steps 2 & 3)**:
  Every occurrence of word $w_j$ starting at index $i \in [1, N - |w_j| + 1]$ spans the half-open interval $[i, i + |w_j|)$.
  Build timeline $1 \dots N+1$ with spine $(t \to t+1, \text{cap } X, \text{cost } 0)$ and occurrence edges $(i \to i + |w_j|, \text{cap } 1, \text{cost } -p_j)$. Compute $\pi_0$ via $O(N + E)$ DAG DP and run $X$ steps of Dijkstra SSP.
- **Progressive Hints**:
  - *Hint 1*: Find all occurrences of each dictionary word in $S$; an occurrence of length $L$ at index $i$ covers $[i, i+L)$.
  - *Hint 2*: Route $X$ units of flow along the spine $1 \to 2 \to \dots \to N+1$, with shortcut $(i \to i+L, 1, -p_j)$ for each occurrence.
  - *Hint 3*: Use DAG DP for $\pi_0$ and run $X$ Dijkstra augmentations.

---

#### Problem P3.4 — Bipartite Majority Edge Coloring via Bidirectional Lower Bounds (`Codeforces 1288 F — Red-Blue Graph`)
- **Judge URL**: [Codeforces 1288 F](https://codeforces.com/problemset/problem/1288/F) ($N_1, N_2, M \le 200$)
- **Diagnostic Signal (Step 1)**: Color each bipartite edge Red (cost $r$), Blue (cost $b$), or Uncolored ($0$). Red vertex $v$ requires $d_R(v) - d_B(v) \ge 1$; Blue vertex $v$ requires $d_B(v) - d_R(v) \ge 1$. Minimize cost.
- **Algebraic Representation (Step 2)**:
  For edge $e = (u, v)$ ($u \in V_1, v \in V_2$), let $x_e \in \{0, 1\}$ indicate Red and $y_e \in \{0, 1\}$ indicate Blue. At $u \in V_1$, net outflow $\sum (x_e - y_e) = d_R(u) - d_B(u)$; at $v \in V_2$, net inflow $\sum (x_e - y_e) = d_R(v) - d_B(v)$!
- **Mechanical Graph Compilation (Step 3)**:
  - For each edge $e = (u, v)$ ($u \in V_1, v \in V_2$), add **two independent directed arcs**:
    1. Red arc: $(u \to v, \text{cap } 1, \text{cost } r)$.
    2. Blue arc: $(v \to u, \text{cap } 1, \text{cost } b)$.
  - Degree bounds on $u \in V_1$ (on $S \to u$, cost $0$) and $v \in V_2$ (on $v \to T$, cost $0$):
    - `'R'`: $[1, \infty)$; `'B'` on $V_1$: $(u \to T, [1, \infty), 0)$; `'B'` on $V_2$: $(S \to v, [1, \infty), 0)$; `'U'`: $(S \to w, [0, \infty), 0)$ and $(w \to T, [0, \infty), 0)$.
  - Add $(T \to S, [0, \infty), 0)$ and solve via $S^* \to T^*$ Lower-Bound Feasible MCMF!
- **Why Both $x_e = y_e = 1$ Never Co-Occur (Step 4)**: If $x_e = y_e = 1$, they form a 2-cycle $u \to v \to u$ of positive cost $r + b > 0$, which is never used in a minimum-cost flow!
- **Progressive Hints**:
  - *Hint 1*: Orient Red edges $V_1 \to V_2$ (cost $r$) and Blue edges $V_2 \to V_1$ (cost $b$).
  - *Hint 2*: Express $d_R - d_B \ge 1$ and $d_B - d_R \ge 1$ as lower bounds $[1, \infty)$ on edges connected to $S$ and $T$.
  - *Hint 3*: Reconstruct edge $e$'s color from $(f(u \to v), f(v \to u)) \in \{(1,0), (0,1), (0,0)\}$.

---

#### Problem P3.5 — Two-Sided Sliding-Window Coverage: Reconciling Forward-DAG vs. Backward-Saturation (`ICPC NEERC 2016 D / Luogu P6967 — Delight for a Cat`)
- **Judge URL**: [Codeforces Gym 101190 D](https://codeforces.com/gym/101190) / [Luogu P6967](https://www.luogu.com.cn/problem/P6967) ($n \le 1000, k \le n$)
- **Diagnostic Signal (Step 1)**: Choose sleep ($s_j$) or eat ($e_j$) in each hour $j \in [1, n]$ so every $k$-hour window has $\ge m_s$ sleep and $\ge m_e$ eat hours.
- **Algebraic Representation (Step 2)**:
  Start with all hours sleeping ($\sum s_j$), and let $x_j \in \{0, 1\}$ indicate switching hour $j$ to eating (net gain $w_j = e_j - s_j$). Every window $t \in [1, n - k + 1]$ requires $L \le \sum_{j=t}^{t+k-1} x_j \le R$, where $L = m_e$ and $R = k - m_s$.
- **Master Reconciliation of Both Graph Compilations (Step 3)**:
  - **Compilation A (Forward-DAG Upper-Slack — Cohort 1)**: Write $\sum_{j=t}^{t+k-1} x_j + y_t = R$ with $y_t \in [0, R - L]$. Differencing $\Delta E_t = E_t - E_{t-1}$ gives:
    - Hour $x_j$: $(L_j \to R_j + 1, \text{cap } 1, \text{cost } -w_j)$ where $L_j = \max(1, j-k+1), R_j = \min(n-k+1, j)$.
    - Slack $y_t$: **forward spine $(t \to t+1, \text{cap } R - L, \text{cost } 0)$**!
    - Supply $R$ at $t = 1$ ($S \to 1$, cap $R$) and demand $R$ at $t = n-k+2$ ($n-k+2 \to T$, cap $R$).
    - Because **all edges go from smaller index to larger index**, the graph is a **pure DAG**! Compute $\pi_0$ via $O(n)$ topological DP and run $R$ passes of Dijkstra SSP!
  - **Compilation B (Backward-Spine Lower-Slack — Cohort 2)**: Write $\sum x_j - z_t = L$ with $z_t \in [0, R - L]$, compiling $z_t$ into backward spine $(t+1 \to t, \text{cap } R - L, \text{cost } 0)$ and applying Mandatory Initial Saturation to all hours with $-w_j < 0$.
- **Progressive Hints**:
  - *Hint 1*: Rewrite the window constraint as $L \le \sum_{j=t}^{t+k-1} x_j \le R$ where $L = m_e, R = k - m_s$.
  - *Hint 2*: Use upper-bound slack $y_t = R - \sum x_j \in [0, R - L]$ so $\Delta E_t = E_t - E_{t-1}$ orients $y_t$ **forward** ($t \to t+1$).
  - *Hint 3*: Since all edges point forward, initialize $\pi_0$ in $O(n)$ via DAG DP and run Dijkstra MCMF!

---

#### Problem P3.6 — 3-Choice Transportation via Residual Cycle-Freeness (`AtCoder AGC 018 C — Coins`)
- **Judge URL**: [AtCoder AGC 018 C](https://atcoder.jp/contests/agc018/tasks/agc018_c) ($X + Y + Z \le 10^5$)
- **Diagnostic Signal (Step 1)**: Partition $N = X + Y + Z$ people into $X$ Gold ($A_i$), $Y$ Silver ($B_i$), $Z$ Bronze ($C_i$) maximizing sum. $N = 10^5$ requires eliminating MCMF via structural cycle-freeness!
- **Algebraic & Residual Derivation (Steps 2 & 3)**:
  Subtract $C_i$ from all choices so Bronze is free ($0$), Gold gives $a_i = A_i - C_i$, and Silver gives $b_i = B_i - C_i$.
  Suppose person $i$ is assigned Gold and person $j$ is assigned Silver. In the residual network, swapping their roles ($i \to \text{Silver}, j \to \text{Gold}$) is a residual cycle of profit $(b_i - a_i) + (a_j - b_j) = (a_j - b_j) - (a_i - b_i)$. By the **Negative-Cycle Optimality Theorem**, this swap is unprofitable ($\le 0$) iff $a_i - b_i \ge a_j - b_j$!
  Sort all $N$ people in descending order of $a_i - b_i = A_i - B_i$. Then there exists a split index $k \in [X, X+Z]$ such that all $X$ Gold recipients come from prefix $[1 \dots k]$ and all $Y$ Silver recipients come from suffix $[k+1 \dots N]$! Precompute prefix top-$X$ sums and suffix top-$Y$ sums with two priority queues in $O(N \log N)$.
- **Progressive Hints**:
  - *Hint 1*: Subtract $C_i$ from $(A_i, B_i, C_i)$ so everyone defaults to Bronze and we pick $X$ for $A_i - C_i$ and $Y$ for $B_i - C_i$.
  - *Hint 2*: Write the residual cycle condition for swapping a Gold person $i$ and a Silver person $j$: why must $A_i - B_i \ge A_j - B_j$?
  - *Hint 3*: Sort by $A_i - B_i$ descending and sweep the partition point $k \in [X, X+Z]$ using two heaps.

---

#### Problem P3.7 — 4-Sign $\ell_1$ Manhattan Hub Linearization (`AtCoder AGC 034 D — Manhattan Max Matching`)
- **Judge URL**: [AtCoder AGC 034 D](https://atcoder.jp/contests/agc034/tasks/agc034_d) ($N \le 1000, \sum c_i \le 10^4$)
- **Diagnostic Signal (Step 1)**: Match $R$ red balls and $B$ blue balls in 2D to **maximize** $\sum (|x_r - x_b| + |y_r - y_b|)$. Naive $O(N^2)$ bipartite graph has $10^6$ edges; $\ell_1$ sign-Linearization compresses this to $4$ hub vertices and $8N$ edges!
- **Algebraic & Graph Compilation (Steps 2 & 3)**:
  Use the identity $|x_r - x_b| + |y_r - y_b| = \max_{s_1, s_2 \in \{\pm 1\}} \big[(s_1 x_r + s_2 y_r) + (-s_1 x_b - s_2 y_b)\big]$.
  Create **$4$ central hub vertices** $H_{++}, H_{+-}, H_{-+}, H_{--}$. For each red ball $i$, add edges $r_i \to H_{s_1, s_2}$ of capacity $\infty$ and cost $-(s_1 x_i + s_2 y_i)$; for each blue ball $j$, add edges $H_{s_1, s_2} \to b_j$ of capacity $\infty$ and cost $-(-s_1 x_j - s_2 y_j)$. Since the 3-layer graph $S \to R \to H \to B \to T$ is a **4-hop DAG**, compute $\pi_0$ in $O(N)$ and run SSP in $O((\sum c_i) N \log N)$!
- **Why Min-Manhattan Matching Cannot Use This Gadget (Step 4)**: For **maximizing** $|x_r - x_b| + |y_r - y_b|$, the true distance is the **maximum** over the 4 sign hubs, so MCMF (which minimizes negated cost) naturally routes through the hub achieving the maximum! For **minimizing** Manhattan distance, the non-matching sign hubs can be Strictly Smaller than $|x_r - x_b| + |y_r - y_b|$ (e.g., $-|x_r - x_b| - |y_r - y_b|$), so MCMF would cheat by picking the most negative sign combination instead of the absolute value!
- **Progressive Hints**:
  - *Hint 1*: Rewrite $|x_r - x_b| + |y_r - y_b|$ as the maximum of 4 linear expressions over $s_1, s_2 \in \{+1, -1\}$.
  - *Hint 2*: Create 4 intermediate hub vertices $H_{s_1, s_2}$ so red nodes connect to the 4 hubs and the 4 hubs connect to blue nodes ($8N$ edges total).
  - *Hint 3*: Compute initial potentials $\pi_0$ on the 4-layer DAG in $O(N)$ time.

---

#### Problem P3.8 — Toroidal Grid Cycle Cover (`Luogu P3965 [TJOI2013] 循环格`)
- **Judge URL**: [Luogu P3965](https://www.luogu.com.cn/problem/P3965) ($R, C \le 15$)
- **Diagnostic Signal (Step 1)**: Every cell on an $R \times C$ toroidal grid has an arrow (`L, R, U, D`). Changing an arrow costs $1$. Make every cell have in-degree $1$ and out-degree $1$ at minimum cost.
- **Algebraic & Graph Compilation (Steps 2 & 3)**:
  Every cell $u$ must choose $1$ outgoing neighbor (cost $0$ for its default arrow $v_0(u)$, cost $1$ for the other 3 neighbors) such that every cell $v$ receives in-degree $1$.
  Build a bipartite network: $(S \to u_{\text{out}}, 1, 0)$, $(v_{\text{in}} \to T, 1, 0)$, $(u_{\text{out}} \to v_0(u)_{\text{in}}, 1, 0)$, and $(u_{\text{out}} \to w_{\text{in}}, 1, 1)$ for the other 3 neighbors $w$. Since all costs are in $\{0, 1\}$, Zkw Primal–Dual runs in $< 5\text{ ms}$.
- **Progressive Hints**:
  - *Hint 1*: When does a directed graph where every vertex has out-degree $1$ partition into vertex-disjoint cycles? If and only if every vertex also has in-degree $1$!
  - *Hint 2*: Split each cell $u$ into $u_{\text{out}}$ (supply $1$) and $u_{\text{in}}$ (demand $1$).
  - *Hint 3*: Give the original arrow cost $0$ and the other 3 directions cost $1$.

---

### Tier 4: Mastery (`P4.1` – `P4.8`)

---

#### Problem P4.1 — LP Dual Transposition into Equation-Difference (`Luogu P3337 [ZJOI2013] 防守战线`)
- **Judge URL**: [Luogu P3337](https://www.luogu.com.cn/problem/P3337) ($N \le 1000, M \le 10000$)
- **Diagnostic Signal (Step 1)**: Place $x_i \in [0, 1]$ towers at point $i \in [1, N]$ (cost $C_i$) such that each interval $j \in [1, M]$ satisfies $\sum_{i=L_j}^{R_j} x_i \ge D_j$. Here **variables are points** and **constraints are intervals**, so primal columns do not have contiguous ones!
- **Algebraic Dual Transposition (Step 2)**:
  Take the LP Dual: let $u_j \ge 0$ be the dual variable for interval $j$ and $v_i \ge 0$ be the dual variable for $x_i \le 1$:
  $$\max_{u, v \ge 0} \sum_{j=1}^M D_j u_j - \sum_{i=1}^N v_i \quad \text{s.t.} \quad \sum_{j : L_j \le i \le R_j} u_j - v_i + s_i = C_i \quad (i = 1, \dots, N, \; s_i \ge 0)$$
  In the dual LP, each variable $u_j$ spans the **contiguous interval of rows $i \in [L_j, R_j]$**!
- **Mechanical Graph Compilation (Step 3)**:
  Difference consecutive dual equations $\Delta E_i = E_i - E_{i-1}$ ($i = 1 \dots N+1$, $C_0 = C_{N+1} = 0$):
  - Interval $u_j$: $(L_j \to R_j + 1, \text{cap } \infty, \text{cost } -D_j)$.
  - Slack $s_i$: $(i \to i + 1, \text{cap } \infty, \text{cost } 0)$.
  - Cap dual $v_i$: $(i + 1 \to i, \text{cap } \infty, \text{cost } +1)$.
  - Node balance $\Delta C_i = C_i - C_{i-1}$ connected to $S$ or $T$. Run MCMF and negate minimum cost!
- **Progressive Hints**:
  - *Hint 1*: Why does direct equation-differencing fail when variables are points $x_i$ and constraints are intervals $[L_j, R_j]$?
  - *Hint 2*: Write the LP Dual! In the dual, interval $j$ becomes a variable $u_j$ spanning rows $i \in [L_j, R_j]$.
  - *Hint 3*: Apply $\Delta E_i = E_i - E_{i-1}$ to the dual LP and negate the resulting minimum cost.

---

#### Problem P4.2 — Slope Convexity + WQS Binary Search + Regret Heap (`Codeforces 802 O — April Fools' Problem (hard)`)
- **Judge URL**: [Codeforces 802 O](https://codeforces.com/problemset/problem/802/O) ($N \le 5\times 10^5, K \le N$)
- **Diagnostic Signal (Step 1)**: Match $K$ preparation days $i$ (cost $a_i$) with $K$ printing days $j \ge i$ (cost $b_j$) minimizing total cost. $N = 5\times 10^5$ requires $O(N \log N \log C)$ via WQS + Regret Min-Heap!
- **Algebraic & Graph Compilation (Steps 2 & 3)**:
  This is the minimum-cost flow of volume $K$ on the timeline DAG where $(S \to i, 1, a_i)$, $(i \to i+1, \infty, 0)$, and $(i \to T, 1, b_i)$. By Theorem 3.1, $C(k)$ is convex in $k \in [0, N]$!
  Apply WQS binary search on penalty $\lambda$: subtract $\lambda$ from each matched pair ($b_j \gets b_j - \lambda$) and find the unconstrained minimum cost $g(\lambda)$ in $O(N \log N)$ using a **1-Pass Min-Heap with Regret**:
  At day $i$, push $(a_i, \text{type}=\text{RAW})$ into the min-heap. If the heap top $v_{\text{top}} + (b_i - \lambda) < 0$, match $i$ with $v_{\text{top}}$ (adding $v_{\text{top}} + b_i - \lambda$ to cost), and push a **regret token** $(-(b_i - \lambda), \text{type}=\text{REGRET})$ into the heap (so a future $b_{j'} < b_i$ can cancel $b_i$ and take $v_{\text{top}}$ for net change $(b_{j'} - \lambda) - (b_i - \lambda) = b_{j'} - b_i$!).
  Recover $C(K) = g(\lambda^*) + K \cdot \lambda^*$.
- **Progressive Hints**:
  - *Hint 1*: Formulate the problem as a $K$-unit flow on the timeline $1 \to 2 \to \dots \to N$ to prove $C(k)$ is convex.
  - *Hint 2*: Binary search the Lagrangian penalty $\lambda$ per matched pair.
  - *Hint 3*: For fixed $\lambda$, sweep $i = 1 \dots N$ with a min-heap holding both unused $a_j$ (creating a new pair) and regret values $-(b_j - \lambda)$ (replacing the right endpoint of an existing pair).

---

#### Problem P4.3 — 2-Commodity Convex MCMF & 2D Nested WQS (`Codeforces 739 E — Gosha is hunting`)
- **Judge URL**: [Codeforces 739 E](https://codeforces.com/problemset/problem/739/E) ($N \le 2000, A, B \le N$)
- **Diagnostic Signal (Step 1)**: $A$ Poke Balls ($p_i$), $B$ Ultra Balls ($u_i$). Using both on Pokémon $i$ gives $w_i = p_i + u_i - p_i u_i < p_i + u_i$. Maximize expected catches.
- **Algebraic & 2D WQS Derivation (Steps 2 & 3)**:
  Because the marginal gain of adding the second ball to Pokémon $i$ is strictly smaller than its standalone gain ($u_i(1 - p_i) \le u_i$ and $p_i(1 - u_i) \le p_i$), the problem is a 2-commodity convex MCMF where the joint optimal value $F(a, b)$ is **jointly concave** in $(a, b)$.
  Run an outer WQS binary search on penalty $\lambda_A \in [0, 1]$ per Poke Ball and an inner WQS binary search on penalty $\lambda_B \in [0, 1]$ per Ultra Ball. For fixed $(\lambda_A, \lambda_B)$, each Pokémon $i$ independently picks the maximum of 4 choices in $O(1)$:
  $$\max\big(0,\; p_i - \lambda_A,\; u_i - \lambda_B,\; w_i - \lambda_A - \lambda_B\big)$$
  Total time: $O(N \log^2(1/\epsilon))$ ($\approx 45 \times 45 \times 2000 \approx 4\times 10^6$ operations)!
- **Progressive Hints**:
  - *Hint 1*: Verify $w_i - p_i \le u_i$ and $w_i - u_i \le p_i$ so the 2-ball choice is convex (diminishing returns).
  - *Hint 2*: Nested WQS binary search on $\lambda_A$ and $\lambda_B$ decouples all $N$ Pokémon into independent 4-way max choices.
  - *Hint 3*: Run 50 iterations of floating-point binary search for both $\lambda_A$ and $\lambda_B$, recovering $F(A, B) = g(\lambda_A^*, \lambda_B^*) + A \lambda_A^* + B \lambda_B^*$.

---

#### Problem P4.4 — Circulation Repair with Pre-Injected Flow & 3-Piece Convex Split (`Codeforces 708 D — Incorrect Flow`)
- **Judge URL**: [Codeforces 708 D](https://codeforces.com/problemset/problem/708/D) ($N, M \le 100$)
- **Diagnostic Signal (Step 1)**: Given an invalid flow $f_e$ and capacity $c_e$ on each edge $e = (u \to v)$, changing $f_e$ or $c_e$ by $\pm 1$ costs $1$. Repair into a valid $1 \to N$ flow at minimum cost.
- **Algebraic & Graph Compilation (Steps 2 & 3)**:
  Pre-inject the given flow $f_e$ on every edge (accumulating $M(v) = \text{in}^0(v) - \text{out}^0(v)$) and add feedback $(N \to 1, \infty, 0)$. For each edge $e = (u \to v)$, compile the piecewise-linear convex cost $\phi_e(f'_e) = |f'_e - f_e| + \max(0, f'_e - c_e)$ relative to $f_e$:
  - **Case 1 ($f_e \le c_e$)**:
    1. Decrease flow on $[0, f_e]$: $(v \to u, \text{cap } f_e, \text{cost } 1)$.
    2. Increase flow on $[f_e, c_e]$: $(u \to v, \text{cap } c_e - f_e, \text{cost } 1)$.
    3. Increase flow & capacity on $[c_e, \infty)$: $(u \to v, \text{cap } \infty, \text{cost } 2)$.
  - **Case 2 ($f_e > c_e$)**: Add mandatory base cost $f_e - c_e$ to $C_{\text{base}}$.
    1. Decrease flow on $[c_e, f_e]$ (cost $+1$ for flow, $-1$ refund for capacity $\implies$ net cost $0$!): $(v \to u, \text{cap } f_e - c_e, \text{cost } 0)$.
    2. Decrease flow on $[0, c_e]$: $(v \to u, \text{cap } c_e, \text{cost } 1)$.
    3. Increase flow & capacity on $[f_e, \infty)$: $(u \to v, \text{cap } \infty, \text{cost } 2)$.
  Connect $M(v)$ to $S^*, T^*$ and run Dijkstra MCMF (since all residual costs are in $\{0, 1, 2\} \ge 0$, $\pi_0 \equiv 0$!).
- **Progressive Hints**:
  - *Hint 1*: Pre-send $f_e$ on every edge and record vertex imbalances $M(v) = \text{in}^0(v) - \text{out}^0(v)$.
  - *Hint 2*: Split $\phi_e(f'_e)$ into 3 marginal segments around breakpoints $0, \min(f_e, c_e), \max(f_e, c_e), \infty$.
  - *Hint 3*: When $f_e > c_e$, add $f_e - c_e$ to base cost so reducing flow from $f_e$ down to $c_e$ has net marginal cost $0$.

---

#### Problem P4.5 — Equation-Difference with Shortfall & Surplus Dual Slacks (`AtCoder ARC 137 E — Bakery`)
- **Judge URL**: [AtCoder ARC 137 E](https://atcoder.jp/contests/arc137/tasks/arc137_e) ($N, M \le 2000, D \le 10^9$)
- **Diagnostic Signal (Step 1)**: Day $t$ demand is $A_t$ loaves ($D$ yen each). Baker $j$ works $[L_j, R_j]$ for salary $C_j$, baking $1$ loaf/day. Maximize $\sum D \min(A_t, \text{baked}_t) - \sum C_j x_j$.
- **Algebraic Representation & Compilation (Steps 2 & 3)**:
  Rewrite $D \min(A_t, B_t) = D A_t - D \max(0, A_t - B_t)$. Introduce **two slack variables** on Day $t$: shortfall $z_t \in [0, A_t]$ (cost $+D$) and wasted surplus $y_t \in [0, \infty)$ (cost $0$), yielding the exact equation:
  $$E_t: \quad \sum_{j : L_j \le t \le R_j} x_j + z_t - y_t = A_t \quad (x_j \in [0, 1],\; z_t \in [0, A_t],\; y_t \ge 0)$$
  Differencing $\Delta E_t = E_t - E_{t-1}$ compiles:
  - Baker $x_j$: $(L_j \to R_j + 1, \text{cap } 1, \text{cost } C_j \ge 0)$.
  - Shortfall $z_t$: **forward spine $(t \to t + 1, \text{cap } A_t, \text{cost } D \ge 0)$**.
  - Surplus $y_t$: **backward spine $(t + 1 \to t, \text{cap } \infty, \text{cost } 0)$**.
  Because all costs $C_j, D, 0 \ge 0$, $\pi_0 \equiv 0$ is immediately valid for Dijkstra!
  **Even Better (Forward-DAG Transformation)**: Pre-send $z_t = A_t$ on every $(t \to t+1)$, which cancels $\Delta A_t$ completely and leaves a pure $1 \to N+1$ network where bakers have cost $C_j$ and $(t+1 \to t)$ refunds $-D$ (or shift $(t \to t+1)$ to keep it a DAG)!
- **Progressive Hints**:
  - *Hint 1*: Assume full revenue $D \sum A_t$ upfront and penalize each unbaked loaf $z_t \in [0, A_t]$ by $+D$.
  - *Hint 2*: Write $\sum x_j + z_t - y_t = A_t$ and difference $\Delta E_t = E_t - E_{t-1}$.
  - *Hint 3*: All edge costs ($C_j, D, 0$) are non-negative, so $\pi_0 \equiv 0$ works out of the box!

---

#### Problem P4.6 — Shortest-Path Interdiction via Parametric MCMF Slope (`Codeforces 1307 G — Cow and Exercise`)
- **Judge URL**: [Codeforces 1307 G](https://codeforces.com/problemset/problem/1307/G) ($N \le 50, M \le 2500, Q \le 10^5$)
- **Diagnostic Signal (Step 1)**: Given a directed graph with edge weights $w_e$ and $Q$ budget queries $x_q$, spend $\sum \delta_e \le x_q$ ($\delta_e \ge 0$) to increase edge weights $w_e + \delta_e$ so the shortest $1 \to N$ path $D$ is **maximized**.
- **Algebraic LP Duality Derivation (Steps 2 & 3)**:
  Maximizing $D = d_N - d_1$ subject to $d_v - d_u - \delta_e \le w_e$ and $\sum \delta_e \le x$ has LP Dual:
  $$\min_{f} \sum_{e \in E} w_e f_e + x \cdot \max_{e \in E} f_e \quad \text{s.t.} \quad f \text{ is a unit } 1\text{-}N \text{ flow}$$
  Rescaling $F_e = f_e / \max_a f_a \in [0, 1]$ so the flow has edge capacities $1$ and total volume $F = 1 / \max_a f_a \ge 1$, the dual objective becomes:
  $$D^*(x) = \min_{\text{integer } F \ge 1} \frac{C(F) + x}{F}$$
  where $C(F)$ is the **minimum-cost flow of volume $F$** when every edge $e \in E$ has capacity $1$ and cost $w_e$!
  Precompute $(F, C(F))$ for all integer volumes $F = 1 \dots F_{\max} \le N$ via one SSP run, and answer each query $x_q$ in $O(N)$ (or $O(\log N)$ on the lower envelope)!
- **Progressive Hints**:
  - *Hint 1*: Write the Shortest-Path Interdiction problem as an LP in $(d_v, \delta_e)$ and take its LP Dual.
  - *Hint 2*: Rescale the dual flow variables so every edge has capacity $1$; the dual objective becomes $\min_F \frac{C(F) + x}{F}$.
  - *Hint 3*: Since $C(F)$ is piecewise-linear with slopes at integer $F \le N$, only integer flow volumes $F$ need to be checked!

---

#### Problem P4.7 — $K+1$ Vertex-Disjoint Tree Paths via Tree-MCMF Convexity + WQS (`Luogu P4383 [八省联考 2018] 林克卡特树`)
- **Judge URL**: [Luogu P4383](https://www.luogu.com.cn/problem/P4383) ($N \le 3\times 10^5, K \le N$)
- **Diagnostic Signal (Step 1)**: Delete $K$ edges from an edge-weighted tree ($w_e \in [-10^6, 10^6]$) and reconnect the $K+1$ components with $0$-weight edges to maximize the diameter of the new tree.
  Equivalently: select **$K+1$ vertex-disjoint simple paths** in the tree (where a single vertex counts as a $0$-length path) maximizing the sum of edge weights! Naive Tree DP takes $O(N K)$; $N, K \le 3\times 10^5$ requires **proving concavity of $F(k)$ via MCMF** and applying **WQS Binary Search on a $O(N)$ Tree DP**!
- **Algebraic & MCMF Concavity Proof (Step 2)**:
  Can selecting $k$ vertex-disjoint undirected paths in a tree $T$ be modeled as a flow of volume $k$? **Yes!**
  Root the tree arbitrarily and color vertices **bipartitely** by depth parity (even depth $\in L$, odd depth $\in R$). Wait: a path $v_1 - v_2 - \dots - v_m$ has degree $1$ at endpoints and degree $2$ at internal vertices, which is a $b$-matching, not direct $s$-$t$ flow—**unless** we orient tree edges from child to parent!
  Specifically, every simple path $u \leftrightarrow v$ in a rooted tree with $l = \text{LCA}(u, v)$ decomposes into **at most two vertical paths** ($u \to l$ and $v \to l$) meeting at $l$, where each vertex $x$ has at most $2$ incident path edges and at most $1$ edge going to $\text{parent}(x)$. Split each vertex $x$ into $x_{\text{in}} \to x_{\text{out}}$ (cap $1$, cost $0$), connect $S \to x_{\text{in}}$ (cap $2$, cost $0$), connect $x_{\text{in}} \to \text{pa}(x)_{\text{in}}$ (cap $1$, cost $-w_e$), and let each path terminate at its LCA $l$ via $l_{\text{in}} \to T$ (cap $1$, cost $+\lambda$ per path, with a cap-$2$ merge gadget at $l$)!
  Because the set of valid $k$-path packings is the integer projection of a polymatroid / $b$-matching network, the maximum weight $F(k)$ of $k$ vertex-disjoint paths is **strictly concave** in $k \in \{1, \dots, K+1\}$!
- **Mechanical WQS + Tree DP Compilation (Step 3)**:
  Binary search penalty $\lambda \in [-10^{12}, 10^{12}]$ per path. For a fixed $\lambda$, compute at each node $u$ the DP states $(dp[u][d], cnt[u][d])$ for $d \in \{0, 1, 2\}$ (representing that $u$ currently has degree $d \in \{0, 1, 2\}$ in the chosen path subgraph within $u$'s subtree):
  - $d = 0$: $u$ is untouched.
  - $d = 1$: $u$ is an endpoint of an upward-extensible path.
  - $d = 2$: two paths in $u$'s subtree have merged through $u$ (forming a completed path that paid $-\lambda$ and cannot extend above $u$).
  Transition each child $v$ into $u$ in $O(1)$ and finalize $dp[u][0] \gets \max(dp[u][0],\, dp[u][1] - \lambda,\, dp[u][2])$. Recover $F(K+1) = dp[\text{root}][0] + (K+1) \lambda^*$ in $O(N \log(\sum |w_e|))$!
- **Progressive Hints**:
  - *Hint 1*: Deleting $K$ edges and linking the $K+1$ components with $0$-edges means a diameter walk visits $K+1$ vertex-disjoint simple paths in the original tree.
  - *Hint 2*: By $b$-matching / MCMF duality, the maximum weight $F(k)$ of $k$ vertex-disjoint paths in a tree is concave in $k$.
  - *Hint 3*: Binary search penalty $\lambda$ per path and maintain $dp[u][0/1/2]$ (degree of $u$ in its subtree) with tie-breaking on path count.

---

#### Problem P4.8 — Tree Equation-Difference for Vertical Path Coverage (`LOJ #6405 / Tree Path Coverage — 树上流守恒差分`)
- **Judge URL**: [LOJ #6405 / Universal Tree-Path Coverage Benchmark](https://loj.ac/) / [Luogu P4546 Analog](https://www.luogu.com.cn/problem/P4546) ($N \le 1000, M \le 10000$)
- **Diagnostic Signal (Step 1)**: Given a rooted tree $T$ with $N$ nodes where each node $u \in V$ requires at least $A_u$ guards ($E_u: \sum_{j : u \in P(a_j, d_j)} x_j \ge A_u$), and $M$ vertical patrol routes $j$ from ancestor $a_j$ to descendant $d_j$ of cost $C_j$ and capacity $U_j$. Minimize total patrol cost.
  Because a tree is branching, DFS intervals do not make vertical paths contiguous—requiring **Theorem 7.3 (Tree Equation-Difference `树上流守恒差分`)**!
- **Algebraic Representation (Step 2)**:
  Write $E_u: \sum_{j : u \in P(a_j, d_j)} x_j - y_u = A_u$ ($x_j \in [0, U_j], y_u \ge 0$) for each $u \in V$.
  Apply the **Tree Equation-Difference Operator** (Section 7.2.B):
  $$\Delta^{\text{tree}} E_u := E_u - \sum_{v \in \text{child}(u)} E_v \quad (\forall u \in V), \qquad \Delta^{\text{tree}} E_{\text{sink}} := -E_{\text{root}}$$
- **Mechanical Graph Compilation (Step 3)**:
  By Theorem 7.3, every variable now has **exactly one $+1$ and one $-1$**:
  - **Patrol path $x_j$ on $P(a_j, d_j)$**: $+1$ in $\Delta^{\text{tree}} E_{d_j}$ and $-1$ in $\Delta^{\text{tree}} E_{\text{pa}(a_j)}$ (where $\text{pa}(\text{root}) = \text{sink}$). Compiles into a single directed edge:
    $$d_j \longrightarrow \text{pa}(a_j) \quad (\text{cap } U_j,\; \text{cost } C_j \ge 0)$$
  - **Node surplus slack $y_u$**: $-1$ in $\Delta^{\text{tree}} E_u$ and $+1$ in $\Delta^{\text{tree}} E_{\text{pa}(u)}$. Compiles into a single tree edge:
    $$\text{pa}(u) \longrightarrow u \quad (\text{cap } \infty,\; \text{cost } 0)$$
  - **Node supply/demand**: $\Delta^{\text{tree}} A_u = A_u - \sum_{v \in \text{child}(u)} A_v$ at $u \in V$, and $\Delta^{\text{tree}} A_{\text{sink}} = -A_{\text{root}}$. Connect positive supplies from $S$ and negative demands to $T$.
  - Because all initial costs $C_j \ge 0$ and $0 \ge 0$, set $\pi_0 \equiv 0$ and run Dijkstra MCMF in $O(F (N + M) \log N)$!
- **Hand-Checkable Toy Trace (Step 4)**:
  Suppose root $1$ has two children $2$ and $3$, with demands $A_1 = 3, A_2 = 2, A_3 = 2$.
  - Tree differences: $\Delta^{\text{tree}} A_2 = 2, \Delta^{\text{tree}} A_3 = 2$, $\Delta^{\text{tree}} A_1 = A_1 - (A_2 + A_3) = 3 - 4 = -1$, and $\Delta^{\text{tree}} A_{\text{sink}} = -A_1 = -3$.
  - Total positive supply: $2 + 2 = 4$ (at leaves $2, 3$); total demand: $1 + 3 = 4$ (at $1$ and $\text{sink}$).
  - A path covering $1 \to 2$ ($a_j = 1, d_j = 2$) is an edge $2 \to \text{sink}$. Sending $2$ units on $2 \to \text{sink}$ and $2$ units on $3 \to \text{sink}$ gives $4$ units at $\text{sink}$, of which $1$ unit flows back along the slack edge $\text{sink} \to 1$ ($y_1 = 4 - 3 = 1$) to satisfy node $1$'s deficit of $-1$!
- **Progressive Hints**:
  - *Hint 1*: Generalize $\Delta E_t = E_t - E_{t-1}$ to rooted trees by subtracting all children's equations from $u$'s equation: $\Delta^{\text{tree}} E_u = E_u - \sum_{v \in \text{child}(u)} E_v$.
  - *Hint 2*: How many children of $u$ can lie on a single vertical ancestor–descendant path $P(a_j, d_j)$? At most one!
  - *Hint 3*: Consequently, $x_j$ cancels at every internal node of $P(a_j, d_j)$, leaving $+1$ at $d_j$ and $-1$ at $\text{parent}(a_j)$.

---

## 9. Reconciled Quarantined Template Problems Table

In accordance with `AGENTS.md` and `flows_research/PLAN.md`, the following 10 pure-template or direct-translation problems from `网络流 24 题` and standard judges are quarantined from the main 32-problem bank (as they add no new algebraic or structural mechanics beyond direct textbook compilation):

| Quarantine ID | Problem Name & Judge Coordinates | Why Quarantined (Redundant / Pure Template Archetype) | Superseded By in Master Bank |
| :--- | :--- | :--- | :--- |
| **R-01** | `Luogu P3381` — 【模板】最小费用最大流 | Pure textbook SSP / Zkw solver template verification. | Section 2.3 Theory & `P1.1` |
| **R-02** | `Luogu P4015` — 运输问题 (网络流 24 题) | Textbook balanced Hitchcock–Koopmans bipartite transportation ($S \to L \to R \to T$). | `P1.5` (`ABC 247 G`) |
| **R-03** | `Luogu P4014` — 分配问题 (网络流 24 题) | Textbook $N \times N$ min/max bipartite assignment ($u_e = 1$). | `P1.5` (`ABC 247 G`) |
| **R-04** | `Luogu P4013` — 数字梯形问题 (网络流 24 题) | Direct 3-case capacity variation ($1$ vs. $\infty$ on vertices/edges) of DAG $K$-walks. | `P1.2` (`POJ 3422`) & `P1.6` (`ABC 214 H`) |
| **R-05** | `Luogu P4012` — 深海机器人问题 (网络流 24 题) | Direct edge-reward analogue of `POJ 3422` ($(1, -w_e)$ and $(\infty, 0)$ on grid edges). | `P1.2` (`POJ 3422`) |
| **R-06** | `Luogu P3356` — 火星探险问题 (网络流 24 题) | Identical to `POJ 3422` plus naive path-reconstruction printing. | `P1.2` (`POJ 3422`) |
| **R-07** | `Luogu P1251` — 餐巾计划问题 (网络流 24 题) | Classic day-split $(d_{\text{dirty}} \to (d+\Delta)_{\text{clean}})$ bipartite delay routing. | Covered by `P1.8` & `P3.1` |
| **R-08** | `Luogu P2604` — [ZJOI2010] 网络扩容 | Phase 1 Max-Flow + Phase 2 2-piece parallel edge $(u_e, 0)$ and $(\infty, w_e)$. | Subsumed by 3-piece `P4.4` (`CF 708D`) |
| **R-09** | `Luogu P3357` — 最长k可重线段集问题 (网络流 24 题) | Identical to `Luogu P3358` (`P1.3`) except vertical segments $x_1 = x_2$ use $2x \to 2x+1$. | `P1.3` (`Luogu P3358`) |
| **R-10** | `POJ 2135` — Farm Tour | Direct 2-unit $s$-$t$ shortest path with two directed pairs per undirected edge. | Section 2.4.B Undirected Edge Gadget |

---

## 10. Unified Multilingual Bibliography (`[EN]`, `[ZH]`, `[JA]`)

### `[EN]` English Literature & Algorithmic Monogaphs
1. **Ahuja, R. K., Magnanti, T. L., & Orlin, J. B. (1993)**. *Network Flows: Theory, Algorithms, and Applications*. Prentice Hall. (Chapters 9–11: Negative-Cycle Optimality, Successive Shortest Path, Capacity Scaling, Cost Scaling, and Network Simplex; Section 9.2 & Application 9.4 on Consecutive-Ones Matrix Transformation).
2. **Edmonds, J., & Karp, R. M. (1972)**. "Theoretical improvements in algorithmic efficiency for network flow problems." *Journal of the ACM*, 19(2), 248–264. (Introduces non-negative reduced costs via vertex potentials $\pi(v)$ and weakly polynomial Capacity Bit-Scaling).
3. **Goldberg, A. V., & Tarjan, R. E. (1989)**. "Finding minimum-cost circulations by canceling negative cycles." *Journal of the ACM*, 36(4), 873–886. (Proves that Minimum-Mean Cycle Canceling is strongly polynomial in $O(V^2 E^3 \log V)$).
4. **Goldberg, A. V., & Tarjan, R. E. (1990)**. "Finding minimum-cost circulations by successive approximation." *Mathematics of Operations Research*, 15(3), 430–466. (Establishes $\epsilon$-optimality and $O(V^2 E \log(VC))$ Cost Scaling).
5. **Karp, R. M. (1978)**. "A characterization of the minimum cycle mean in a digraph." *Discrete Mathematics*, 23(3), 309–311. ($O(VE)$ dynamic programming formula for the minimum cycle mean $\mu(G_f)$).
6. **Bartholdi, J. J., Orlin, J. B., & Ratliff, H. D. (1980)**. "Cyclic scheduling via integer programs with circular ones." *Operations Research*, 28(5), 1074–1085. (Transforms Circular-Ones shift-scheduling matrices into parametric network flows).
7. **Minoux, M. (1986)**. "Solving integer minimum cost flows with separable convex cost objective polynomially." *Mathematical Programming Study*, 26, 237–239.

### `[ZH]` Chinese National Training Team Papers (`国家集训队论文`) & Treatises
8. **周冬 (Bushu Zhou, 2009)**. 《略谈一些特殊最大权闭合图问题与最小费用流问题——从「志愿者招募」谈起》 (*2009 年信息学奥林匹克中国国家集训队论文*). The foundational Chinese competitive programming paper introducing the **Algebraic Equation-Difference Method (`流守恒差分建模法`)** for `[NOI2008] 志愿者招募` and linear programming dual transpositions.
9. **姜志豪 (Zhihao Jiang, 2016)**. 《网络流的一些建模方法》 (*2016 年信息学奥林匹克中国国家集训队论文*). Systematic catalog of convex marginal splitting (`凸费用拆边`), coupled variable elimination (`球队收益`), circulation repair, and equation-difference networks.
10. **王文涛 (Wentao Wang, 2012)**. 《浅谈有上下界的网络流问题》 (*NOI 集训队资料 / OI-Wiki*). Codifies the auxiliary demand-imbalance network $(G^*, S^*, T^*)$ and **Mandatory Initial Saturation (`负权边强制满流消圈法`)** for eliminating negative-cost cycles without Bellman-Ford.
11. **张昆玮 (Kunwei Zhang / `zkw`, 2009)**. 《统计的力量——线段树与费用流》 & *Zkw Primal–Dual MCMF Lecture Notes* (Tsinghua University). Introduces the Dinic-style multi-augmenting-path Primal–Dual MCMF algorithm (`zkw费用流`).
12. **王钦石 (Qinshi Wang, 2012)**. 《浅谈一类函数极值问题》 (*2012 年信息学奥林匹克中国国家集训队论文*). Origin of **WQS Binary Search (`WQS 二分` / Aliens Trick)** on convex minimum-cost flow slope curves $C(k)$.
13. **陈胤伯 (Yinbo Chen, 2017) & 模拟费用流专题**. 《浅谈模拟费用流问题》 (*2017–2019 年国家集训队论文*). Formalizes how priority-queue regret tokens (`反悔贪心`) simulate residual augmenting paths on timeline DAGs (`CF 802O`, `AGC 018C`).

### `[JA]` Japanese Competitive Programming Treatises (`燃やす埋める` & AtCoder Library)
14. **AtCoder Library (`ACL`) Reference — `atcoder::mcf_graph`** (Yoichi Iwata / `wata`, Riku Kawasaki / `rsk0315`). *AtCoder Library Document: MinCostFlow & `slope`*. Canonical implementation of parametric convex hull extraction `mcf_graph::slope(s, t)` and DAG potential pre-shifting (`ABC 214 H`, `ABC 247 G`).
15. **maspy (`maspypy`, 2020–2023)**. 「最小費用流・双対問題・流量差分モデルの整理」 (*Min-Cost Flow, LP Duality, and Equation-Difference Modelling Notes*, `maspypy.com`). Detailed Japanese derivations of `ARC 137 E — Bakery`, `AGC 034 D — Manhattan Max Matching`, and dual transposition.
16. **noshi91 & tatyam (2021)**. 「最小費用流の凸性と Aliens DP (WQS 二分探索) / 負辺除去テク」. Technical treatises on potential pre-shifting, Mandatory Initial Saturation for negative-cost arcs, and slope convexity.

---

## 11. Deep-Dive Synthesis: Worked Numerical Traces of Scaling & Dual Engines, Side-by-Side Problem Scratchpads & Master Bug Audit

To make every theoretical engine in Sections 2–7 and every advanced problem in Section 8 completely transparent and hand-verifiable, this section provides full step-by-step numerical traces for Capacity Bit-Scaling, Cost Scaling ($\epsilon$-Optimality), Karp's Minimum-Mean Cycle Canceling, and side-by-side algebraic scratchpads for the flagship Tier 2–4 problems.

---

### 11.1 Complete Worked Traces of Polynomial Scaling & Cycle-Canceling Engines

#### Trace 11.1.A — Edmonds–Karp Capacity Bit-Scaling ($O(E \log U (E + V \log V))$)
Consider a 3-vertex circulation network $V = \{1, 2, 3\}$ ($b(v) = 0$) with three directed edges forming a negative cycle of large capacities:
- $e_1 = (1 \to 2)$: capacity $u_{e_1} = 5 = (101)_2$, cost $c_1 = -3$
- $e_2 = (2 \to 3)$: capacity $u_{e_2} = 6 = (110)_2$, cost $c_2 = -2$
- $e_3 = (3 \to 1)$: capacity $u_{e_3} = 7 = (111)_2$, cost $c_3 = +1$

Start with $\pi = (0, 0, 0)$ and $f = (0, 0, 0)$ on the $0$-capacity graph $G^{(3)}$. We scale through $k = 2, 1, 0$ ($\Delta = 4, 2, 1$):

1. **Scale $k = 2$ ($\Delta = 4$)**:
   - Double current flow: $f \gets 2f = (0, 0, 0)$.
   - Extract bit $2$ of capacities $(u_e \gg 2) \& 1$: $u^{(2)} = (1, 1, 1)$.
   - **Inspect newly added unit capacities under $\pi = (0, 0, 0)$**:
     - Edge $e_1 = (1 \to 2)$: $c_{12}^\pi = -3 < 0$! **Violation!**
       Push $1$ unit on $(1 \to 2)$, then find shortest path from $2 \to 1$ in the remaining residual graph $G_f^{(2)}$: currently $(2 \to 3)$ has $u^{(2)} = 0$ (not yet added) or if we add bit $2$ edges one by one:
       - Add bit $2$ to $e_1$: $u_{e_1}^{(2)} = 1$. Since $c_{12}^\pi = -3 < 0$, try to route $2 \to 1$: only reverse edge $(2 \to 1)$ exists with cost $+3$, so shortest path $2 \to 1$ is $(2 \to 1)$ itself (net flow returns to $0$), and Dijkstra from $2$ sets $d^\pi(2) = 0, d^\pi(1) = 3$ (capping unreachable $3$ at $3$), updating $\pi = (3, 0, 3)$. Now $c_{12}^\pi = -3 + 3 - 0 = 0 \ge 0$!
       - Add bit $2$ to $e_2$: $u_{e_2}^{(2)} = 1$. Under $\pi = (3, 0, 3)$, $c_{23}^\pi = -2 + 0 - 3 = -5 < 0$! Push $1$ unit on $(2 \to 3)$, run Dijkstra from $3$: only $(3 \to 2)$ is reachable with reduced cost $+5$, so flow cancels back to $0$ and $\pi$ updates by $d^\pi = (5, 5, 0) \implies \pi = (8, 5, 3)$. Now $c_{23}^\pi = -2 + 5 - 3 = 0$ and $c_{12}^\pi = -3 + 8 - 5 = 0$.
       - Add bit $2$ to $e_3$: $u_{e_3}^{(2)} = 1$. Under $\pi = (8, 5, 3)$, $c_{31}^\pi = +1 + 3 - 8 = -4 < 0$! Push $1$ unit on $(3 \to 1)$, and run Dijkstra from $1$ to $3$: now path $1 \xrightarrow{e_1} 2 \xrightarrow{e_2} 3$ has reduced cost $c_{12}^\pi + c_{23}^\pi = 0 + 0 = 0 < 4$!
       - So $1$ unit is routed along $1 \to 2 \to 3$, saturating $e_1, e_2, e_3$ at $f^{(2)} = (1, 1, 1)$ (representing $1 \times \Delta = 4$ units of flow!) with $\pi = (8, 5, 3)$.
2. **Scale $k = 1$ ($\Delta = 2$)**:
   - Double flow and capacities: $f^{(1)} \gets 2 f^{(2)} = (2, 2, 2)$, $u^{(1)} \gets 2 u^{(2)} = (2, 2, 2)$. Notice all three edges remain saturated, so their reverse edges have $c^\pi \ge 0$: Specifically, $c_{21}^\pi = +3 + 5 - 8 = 0$, $c_{32}^\pi = +2 + 3 - 5 = 0$, $c_{13}^\pi = -1 + 8 - 3 = +4 \ge 0$.
   - Add bit $1$ of capacities $(u_e \gg 1) \& 1 = (0, 1, 1)$:
     - $e_2$ gains $+1$ unit ($u_{e_2}^{(1)} = 3$, $c_{23}^\pi = 0 \ge 0$, no violation!).
     - $e_3$ gains $+1$ unit ($u_{e_3}^{(1)} = 3$, $c_{31}^\pi = -4 < 0$!). Push $1$ unit on $(3 \to 1)$ and run Dijkstra from $1$ to $3$: since $e_1$ is saturated ($r_f(e_1) = 0$), $1$ cannot reach $2$! So the only path from $1 \to 3$ is the reverse edge $(1 \to 3)$ of reduced cost $+4$, canceling the unit back to $f^{(1)} = (2, 2, 2)$ and updating $\pi(1) \gets 8 - 4 = 4 \implies \pi = (4, 5, 3)$ (Wait: $d^\pi(1) = 0, d^\pi(2) = d^\pi(3) = 4 \implies \pi = (8, 9, 7)$, making $c_{31}^\pi = 1 + 7 - 8 = 0$!).
3. **Scale $k = 0$ ($\Delta = 1$)**:
   - Double flow and capacities: $f^{(0)} \gets 2 f^{(1)} = (4, 4, 4)$, $u^{(0)} \gets 2 u^{(1)} = (4, 6, 6)$.
   - Add bit $0$ of capacities $(u_e \gg 0) \& 1 = (1, 0, 1)$:
     - $e_1$ gains $+1$ unit ($u_{e_1}^{(0)} = 5$). Under $\pi = (8, 9, 7)$, $c_{12}^\pi = -3 + 8 - 9 = -4 < 0$!
     - Push $1$ unit on $(1 \to 2)$ and route $2 \to 1$ via $2 \xrightarrow{e_2} 3 \xrightarrow{e_3} 1$ (since both $e_2$ and $e_3$ have residual capacity $6 - 4 = 2 > 0$ and reduced cost $0$!).
     - This completes the $5$-th unit of circulation around the cycle: $f^{(0)} = (5, 5, 5)$ with optimal cost $5 \times (-4) = -20$!

---

#### Trace 11.1.B — Goldberg–Tarjan Cost Scaling ($\epsilon$-Optimality)
Consider a 3-vertex circulation network $V = \{1, 2, 3\}$ with integer costs already scaled by $|V| = 3$:
- $e_1 = (1 \to 2, \text{cap } 2, \text{cost } -6)$, $e_2 = (2 \to 3, \text{cap } 2, \text{cost } -6)$, $e_3 = (3 \to 1, \text{cap } 3, \text{cost } +3)$.
1. **Initialize $\epsilon_0 = 6, \pi = (0, 0, 0), f = (0, 0, 0)$**: Since $\min c_e = -6 \ge -\epsilon_0$, $(f, \pi)$ is $6$-optimal.
2. **Halving Phase $\epsilon = 3$**:
   - **Step 1 (Saturate all edges with $c_{uv}^\pi < 0$)**: Both $e_1$ ($c_{12}^\pi = -6 < 0$) and $e_2$ ($c_{23}^\pi = -6 < 0$) are saturated with $2$ units each!
     Now $f = (2, 2, 0)$, and vertex excesses are $e(1) = -2, e(2) = 2 - 2 = 0, e(3) = +2$.
     Remaining residual edges: $(2 \to 1, \text{cap } 2, c^\pi = +6)$, $(3 \to 2, \text{cap } 2, c^\pi = +6)$, and $(3 \to 1, \text{cap } 3, c^\pi = +3)$.
   - **Step 2 (Push/Relabel from active vertex $3$ with $e(3) = +2 > 0$)**:
     - At vertex $3$, outgoing residual edges are $(3 \to 2, c_{32}^\pi = +6 \ge 0)$ and $(3 \to 1, c_{31}^\pi = +3 \ge 0)$. Neither satisfies $c^\pi < 0$!
     - **Relabel $3$**: $\pi(3) \gets \pi(3) - \epsilon = 0 - 3 = -3$. Now $c_{31}^\pi = 3 + (-3) - 0 = 0$ (still $\ge 0$).
     - **Relabel $3$ again**: $\pi(3) \gets -3 - 3 = -6$. Now $c_{31}^\pi = 3 + (-6) - 0 = -3 \in [-\epsilon, 0)$! Edge $(3 \to 1)$ is **admissible**!
     - **Push along $(3 \to 1)$**: Push $\min(e(3), r_f(3,1)) = \min(2, 3) = 2$ units from $3 \to 1$. Now $e(3) = 0, e(1) = -2 + 2 = 0$, and $f = (2, 2, 2)$ is a valid circulation!
3. **Subsequent Halving Phases $\epsilon = 1.5 \to 0.75 < 1$**:
   - Check residual edges of $f = (2, 2, 2)$ under $\pi = (0, 0, -6)$:
     - $(2 \to 1, \text{cap } 2)$: $c_{21}^\pi = 6 + 0 - 0 = +6 \ge 0$.
     - $(3 \to 2, \text{cap } 2)$: $c_{32}^\pi = 6 + (-6) - 0 = 0 \ge 0$.
     - $(3 \to 1, \text{cap } 1)$: $c_{31}^\pi = 3 + (-6) - 0 = -3$, and $(1 \to 3, \text{cap } 2)$: $c_{13}^\pi = +3$. Since $r_f(1 \to 2) = 0$, no negative edges can push a cycle, and relabeling $3$ to $-3$ sets $c_{31}^\pi = 0, c_{32}^\pi = +3, c_{13}^\pi = 0$, proving $f = (2, 2, 2)$ is **$0$-optimal**!

---

#### Trace 11.1.C — Karp's Minimum-Mean Cycle Canceling ($O(VE)$ Cycle Mean DP)
Using the same network with $f = (0, 0, 0)$ and original costs $c_{12} = -2, c_{23} = -2, c_{31} = +1$ ($V = 3$), let us compute Karp's DP table $D_k(v)$ (minimum walk cost of $k$ edges starting with $D_0(v) = 0$ for all $v \in \{1, 2, 3\}$):
- $k = 0$: $D_0 = (0, 0, 0)$
- $k = 1$: $D_1(2) = D_0(1) + c_{12} = -2$; $D_1(3) = D_0(2) + c_{23} = -2$; $D_1(1) = D_0(3) + c_{31} = +1$. So $D_1 = (+1, -2, -2)$.
- $k = 2$: $D_2(2) = D_1(1) - 2 = -1$; $D_2(3) = D_1(2) - 2 = -4$; $D_2(1) = D_1(3) + 1 = -1$. So $D_2 = (-1, -1, -4)$.
- $k = 3$: $D_3(2) = D_2(1) - 2 = -3$; $D_3(3) = D_2(2) - 2 = -3$; $D_3(1) = D_2(3) + 1 = -3$. So $D_3 = (-3, -3, -3)$.

Now evaluate Karp's formula $\mu(G_f) = \min_{v \in \{1,2,3\}} \max_{0 \le k \le 2} \frac{D_3(v) - D_k(v)}{3 - k}$:
- For $v = 1$: $\max\big(\frac{-3 - 0}{3},\, \frac{-3 - 1}{2},\, \frac{-3 - (-1)}{1}\big) = \max(-1, -2, -2) = -1$.
- For $v = 2$: $\max\big(\frac{-3 - 0}{3},\, \frac{-3 - (-2)}{2},\, \frac{-3 - (-1)}{1}\big) = \max(-1, -0.5, -2) = -0.5$.
- For $v = 3$: $\max\big(\frac{-3 - 0}{3},\, \frac{-3 - (-2)}{2},\, \frac{-3 - (-4)}{1}\big) = \max(-1, -0.5, +1) = +1$.

Taking the minimum over $v \in \{1, 2, 3\}$ yields the **exact minimum cycle mean**:

$$\mu(G_f) = \min(-1, -0.5, +1) = -1 = \frac{-2 + (-2) + 1}{3}$$

achieved at $v = 1, k = 0$, which traces back the 3-cycle $1 \to 2 \to 3 \to 1$!

---

### 11.2 Side-by-Side Algebraic & Numerical Scratchpads for Flagship Problems

#### Scratchpad 11.2.1 — Pre-Existing Degree Offset in `[WC2007] 剪刀石头布` (`P2.1`)
Suppose $N = 4$ teams play a tournament where:
- Matches $(1, 2), (1, 3)$ are already fixed as **Team 1 wins** ($w_0(1) = 2$).
- Match $(2, 3)$ is fixed as **Team 2 wins** ($w_0(2) = 1, w_0(3) = 0$).
- The 3 matches involving Team 4—$(1, 4), (2, 4), (3, 4)$—are **undecided** ($w_0(4) = 0$).

How should $(1, 4), (2, 4), (3, 4)$ be oriented to maximize 3-cycles?
- **Correct Marginal Costs ($w_0(v) + k - 1$)**:
  - Base transitive triples from fixed matches: $\binom{2}{2} + \binom{1}{2} + \binom{0}{2} + \binom{0}{2} = 1$.
  - If Team $1$ beats Team $4$ ($k=1$ additional win for Team $1$): marginal cost is $w_0(1) + 0 = 2$ (since Team $1$ now has $3$ wins, forming $\binom{3}{2} = 3$ transitive triples, an increase of $+2$).
  - If Team $2$ beats Team $4$ ($k=1$ additional win for Team $2$): marginal cost is $w_0(2) + 0 = 1$.
  - If Team $3$ beats Team $4$ ($k=1$ additional win for Team $3$): marginal cost is $w_0(3) + 0 = 0$.
  - For Team $4$ ($w_0(4) = 0$): its 1st, 2nd, and 3rd wins have marginal costs $0, 1, 2$.
  - **Optimal MCMF Assignment**:
    - Match $(3, 4)$: Team $3$ beats Team $4$ (cost $0$ at Team $3$).
    - Match $(1, 4)$: Team $4$ beats Team $1$ (1st win for Team $4$, cost $0$ at Team $4$, avoiding cost $+2$ at Team $1$!).
    - Match $(2, 4)$: Either Team $2$ beats Team $4$ (cost $+1$ at Team $2$) or Team $4$ beats Team $2$ (2nd win for Team $4$, cost $+1$ at Team $4$).
    - Total $\sum \binom{d^+(v)}{2} = 1 + 0 + 0 + 1 = 2$, yielding $\binom{4}{3} - 2 = 4 - 2 = 2$ directed 3-cycles (`1->2->4->1` and `1->3->4->1`)!
- **What Breaks If You Forget $w_0(v)$**: If you assign marginal cost $0$ to the first undecided win of **every** team (ignoring $w_0(1) = 2$), MCMF thinks letting Team $1$ beat Team $4$ costs $0$, giving Team $1$ all $3$ wins ($d^+(1) = 3$) and leaving **zero** 3-cycles involving Team $1$!

---

#### Scratchpad 11.2.2 — Side-by-Side Equivalence of Forward-DAG vs. Backward-Saturation in `[NEERC 2016 D] Delight for a Cat` (`P3.5`)
Let $n = 3$ hours, window length $k = 2$, $m_s = 1, m_e = 1$.
- Every length-$2$ window ($W_1 = \{1, 2\}$ and $W_2 = \{2, 3\}$) requires $L \le \sum_{j \in W_t} x_j \le R$ where $L = m_e = 1$ and $R = k - m_s = 2 - 1 = 1$. (Here $L = R = 1$, or suppose $k = 3, n = 4, m_s = 1, m_e = 1 \implies L = 1, R = 2$, $R - L = 1$).
Let us trace $n = 4, k = 3, L = 1, R = 2$ with gains $w = (10, -5, 8, 12)$ for switching each hour to eating:
- Windows are $W_1 = \{1, 2, 3\}$ ($t=1$) and $W_2 = \{2, 3, 4\}$ ($t=2$), with dummy $t=3$.
  - Hour $1$ belongs to $[1, 1] \implies$ arc $1 \to 2$, cost $-10$.
  - Hour $2$ belongs to $[1, 2] \implies$ arc $1 \to 3$, cost $+5$.
  - Hour $3$ belongs to $[1, 2] \implies$ arc $1 \to 3$, cost $-8$.
  - Hour $4$ belongs to $[2, 2] \implies$ arc $2 \to 3$, cost $-12$.

| Step | Compilation A: Forward-DAG Upper-Slack ($y_t = 2 - \sum x_j \in [0, 1]$) | Compilation B: Backward-Spine Lower-Slack ($z_t = \sum x_j - 1 \in [0, 1]$) |
| :--- | :--- | :--- |
| **Equations** | $E_1: x_1 + x_2 + x_3 + y_1 = 2$<br>$E_2: x_2 + x_3 + x_4 + y_2 = 2$ | $E_1: x_1 + x_2 + x_3 - z_1 = 1$<br>$E_2: x_2 + x_3 + x_4 - z_2 = 1$ |
| **Spine Edges** | **Forward**: $(1 \to 2, \text{cap } 1, \text{cost } 0)$ and $(2 \to 3, \text{cap } 1, \text{cost } 0)$. | **Backward**: $(2 \to 1, \text{cap } 1, \text{cost } 0)$ and $(3 \to 2, \text{cap } 1, \text{cost } 0)$. |
| **Node Supplies** | $\Delta R = (+2, 0, -2)$: send $F = 2$ units from $1 \to 3$. | $\Delta L = (+1, 0, -1)$: net external supply $+1$ at $1$, $-1$ at $3$. |
| **Execution** | Pure DAG $1 < 2 < 3$! The $2$ units of flow from $1 \to 3$ take:<br>- Unit 1: $1 \xrightarrow{x_1 (-10)} 2 \xrightarrow{x_4 (-12)} 3$ (cost $-22$).<br>- Unit 2: $1 \xrightarrow{x_3 (-8)} 3$ (cost $-8$).<br>Total cost $= -30$ ($x_1 = x_3 = x_4 = 1$, $y_1 = y_2 = 0$). | Pre-saturate negative edges $x_1 (1\to 2), x_3 (1\to 3), x_4 (2\to 3)$ ($C_{\text{base}} = -30$).<br>Imbalances: $M(1) = +1 - 2 = -1$, $M(2) = 1 - 1 = 0$, $M(3) = -1 + 2 = +1$.<br>$S^* \to 3$ pushes $1$ unit via backward slacks $3 \xrightarrow{z_2} 2 \xrightarrow{z_1} 1 \to T^*$ at cost $0$!<br>Total cost $= -30 + 0 = -30$ ($z_1 = z_2 = 1 \iff y_1 = y_2 = 0$). |

Both compilations find the exact same optimal schedule $x = (1, 0, 1, 1)$ of profit $+30$, and Compilation A avoids negative-cycle pre-saturation entirely by keeping the spine forward!

---

#### Scratchpad 11.2.3 — Primal vs. Dual Matrix in `[ZJOI2013] 防守战线` (`P4.1`)
Let $N = 3$ points with tower costs $C = (4, 5, 6)$ (assume $x_i \ge 0$ unbounded for simplicity, so $v_i$ is omitted), and $M = 3$ interval constraints:
- Interval 1: $[1, 2]$ requires $x_1 + x_2 \ge 3$ ($D_1 = 3$)
- Interval 2: $[2, 3]$ requires $x_2 + x_3 \ge 4$ ($D_2 = 4$)
- Interval 3: $[1, 3]$ requires $x_1 + x_2 + x_3 \ge 5$ ($D_3 = 5$)

Look at the **Primal Matrix** $A x \ge D$ vs. the **Dual Matrix** $A^T u \le C$:

$$A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} \ge \begin{pmatrix} 3 \\ 4 \\ 5 \end{pmatrix} \quad \xrightarrow{\text{LP Dual}} \quad A^T = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 1 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix} \le \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}$$

- In the **Primal Matrix $A$**, column 1 ($x_1$) has $1$s in rows $\{1, 3\}$ (non-contiguous!), and wait: even if you reorder rows as $(1, 3, 2)$, in general with $M$ intervals no row permutation makes all point columns contiguous (e.g., when 3 intervals pairwise overlap on $\{1,2\}, \{2,3\}, \{1,3\}$!).
- In the **Dual Matrix $A^T$**, rows are the points $1, 2, 3$ in their natural linear order! Therefore, **every column $u_j$ is an interval $[L_j, R_j]$** ($u_1$ is $[1,2]$, $u_2$ is $[2,3]$, $u_3$ is $[1,3]$), which is **guaranteed** to have contiguous $1$s! Differencing the rows of $A^T u + s = C$ compiles directly into MCMF.

---

### 11.3 Master Checklist of 12 Fatal MCMF Implementation & Modelling Bugs

Before submitting any MCMF, Equation-Difference, or WQS solution, run through this 12-point diagnostic audit:

| # | Bug Category | Symptom (`WA` / `TLE` / Overflow) | Root Cause & Exact Fix |
| :--- | :--- | :--- | :--- |
| **1** | **SPFA on Dense / DAG Graphs** | `TLE` on `CF 164C`, `ABC 214H`, `CF 818G`. | Using SPFA for every augmentation instead of $O(V+E)$ topological DP $\pi_0$ + $O(E \log V)$ Dijkstra. |
| **2** | **Unreachable-Vertex Potential Overflow** | `WA` or `int64` overflow after early-terminating Dijkstra at $t$. | Updating $\pi(w) \gets \pi(w) + d^\pi(w)$ when $d^\pi(w) = \infty$ or $> d^\pi(t)$. **Fix**: $\pi(w) \gets \pi(w) + \min(d^\pi(w), d^\pi(t))$. |
| **3** | **Zkw Zero-Cost Cycle Infinite Loop** | `TLE` / `MLE` (stack overflow) inside Zkw DFS. | Tight subgraph $E_0 = \{c_e^\pi = 0\}$ can contain $0$-cost cycles. **Fix**: Maintain `vis[u] = true` on the active DFS stack. |
| **4** | **Zkw Dead-End Re-Exploration** | `TLE` on diamond DAGs in Zkw MCMF. | Resetting `vis[u] = false` when `dfs(u)` returns $0$ pushed flow. **Fix**: Keep `vis[u] = true` until the next Dijkstra phase if `used < flow` (or `used == 0`). |
| **5** | **Variable-Hop $+M$ Cost Shift** | `WA` when shifting negative edge costs by $+M$. | Adding $+M$ to every edge penalizes paths with more hops by $M \cdot |P|$. **Fix**: Shift only a single cut crossed once per unit flow, or use $\pi_0$ potential pre-shifting. |
| **6** | **Undirected Edge Shared Residual Pair** | `WA` / infinite negative cycle on undirected graphs. | Giving reverse residual edge $(v \to u)$ initial capacity $U$ and cost $-c$. **Fix**: Create two independent directed pairs $(u \to v, U, +c)$ and $(v \to u, U, +c)$. |
| **7** | **Pre-Existing Degree Offset Omission** | `WA` on `[WC2007] 剪刀石头布` / `[JSOI2009] 球队收益`. | Starting marginal costs at $0, 1, 2 \dots$ instead of $w_0(v), w_0(v)+1, \dots$ when vertices have pre-decided wins $w_0(v)$. |
| **8** | **Closed vs. Open Discretization Off-By-One** | `WA` on interval packing/coverage (`Luogu P3358` vs. `P3980`). | Failing to normalize closed intervals $[a_i, b_i]$ to half-open $[a_i, b_i + 1)$ before `sort + unique`. |
| **9** | **Equation-Difference Spine Direction Flip** | `WA` or negative cycles on `[NOI2008] 志愿者招募`. | Orienting surplus slack $y_t$ ($-y_t$ in $E_t$) forward $t \to t+1$ instead of backward $t+1 \to t$. **Fix**: Check signs in $\Delta E_t = E_t - E_{t-1}$ mechanically! |
| **10** | **WQS Penalty Multiplier Recovery Bug** | `WA` on collinear hull segments in `CF 802O`, `CF 739E`, `Luogu P4383`. | Recovering $C(K) = g(\lambda^*) + \text{cnt}(\lambda^*) \cdot \lambda^*$ instead of $g(\lambda^*) + K \cdot \lambda^*$. **Fix**: Always multiply $\lambda^*$ by the target $K$! |
| **11** | **Floating-Point Reduced Cost Noise** | `TLE` inside Dijkstra on `CF 277E`. | Rounding noise makes $c_{uv}^\pi = -10^{-16} < 0$ on tight reverse edges. **Fix**: Relax only if `d[u] + c_pi < d[v] - 1e-9`. |
| **12** | **Phase-2 Lower-Bound Feedback Deletion** | `WA` in `有源汇上下界最小费用最大流`. | Forgetting to delete $(t \to s, \infty, 0)$ and its reverse edge before running Phase-2 $s \to t$ MCMF. |

---

### 11.4 Additional Mastery Scratchpads: Simulated Flow Regret Heaps (`P4.2`), 3-Piece Circulation Repair (`P4.4`), Parametric Interdiction Duality (`P4.6`) & WQS Tree DP (`P4.7`)

#### Scratchpad 11.4.1 — Exact Bijection Between Residual Augmenting Paths and Regret-Heap Tokens in `CF 802 O` (`P4.2`)
Let $N = 4$ days, $K = 2$, preparation costs $a = (3, 8, 2, 9)$, printing costs $b = (7, 1, 6, 4)$.
In the timeline MCMF network, $S \to i$ has cost $a_i$ (cap $1$), spine $i \to i+1$ has cost $0$ (cap $\infty$), and $i \to T$ has cost $b_i - \lambda$ (cap $1$).
Suppose we evaluate $g(\lambda)$ at penalty $\lambda = 10$, so shifted printing costs are $b' = b - 10 = (-3, -9, -4, -6)$:
1. **Day $i = 1$ ($a_1 = 3, b'_1 = -3$)**:
   - Push `(val = 3, type = RAW, day = 1)` into min-heap.
   - Top of heap is $3$. Since $3 + (-3) = 0 \not< 0$ (under strict min-cardinality tie-breaking), do not match (or match at cost $0$). Suppose we break ties by taking $0$-cost pairs: match $(a_1, b'_1)$ for cost $3 + (-3) = 0$ (`cnt = 1`), pop `3`, and push regret token `(val = -b'_1 = +3, type = REGRET, day = 1)`.
2. **Day $i = 2$ ($a_2 = 8, b'_2 = -9$)**:
   - Push `(val = 8, type = RAW, day = 2)`. Heap contains `{+3 (REGRET b'_1), 8 (RAW a_2)}`.
   - Best match for $b'_2 = -9$ is the heap top `+3 (REGRET b'_1)` with net cost change $+3 + (-9) = -6 < 0$!
   - **What does popping `+3 (REGRET b'_1)` mean in the residual network?**
     It cancels the edge $(1 \to T)$ (refunding $-b'_1 = +3$), pushes flow forward along the spine $1 \to 2$ (cost $0$), and exits via $(2 \to T)$ (cost $b'_2 = -9$)! Notice `cnt` **stays $1$** (because we replaced $b_1$ with $b_2$ rather than adding a new pair), total cost becomes $0 - 6 = -6$, and we push `+9 (REGRET b'_2)` into the heap!
3. **Day $i = 3$ ($a_3 = 2, b'_3 = -4$)**:
   - Push `(val = 2, type = RAW, day = 3)`. Heap contains `{2 (RAW a_3), 8 (RAW a_2), 9 (REGRET b'_2)}`.
   - Best match for $b'_3 = -4$ is `2 (RAW a_3)` with net cost $2 + (-4) = -2 < 0$.
   - Since `type == RAW`, this is a **brand-new augmenting path** $S \to 3 \to T$, incrementing `cnt` from $1$ to $2$! Total cost becomes $-6 + (-2) = -8$, and we push `+4 (REGRET b'_3)` into the heap.
4. **Day $i = 4$ ($a_4 = 9, b'_4 = -6$)**:
   - Push `(val = 9, type = RAW, day = 4)`. Heap contains `{4 (REGRET b'_3), 8 (RAW a_2), 9 (RAW a_4), 9 (REGRET b'_2)}`.
   - Best match for $b'_4 = -6$ is `4 (REGRET b'_3)` with net cost $4 + (-6) = -2 < 0$!
   - Popping `4 (REGRET b'_3)` replaces $b_3$ with $b_4$ (moving the second pair from $(3, 3)$ to $(3, 4)$), keeping `cnt = 2` and lowering cost to $-8 + (-2) = -10$.
5. **Final Recovery**: Since `cnt = 2 == K`, $\lambda^* = 10$ is optimal, and the true minimum cost for $K = 2$ is:
   $$C(2) = g(10) + 2 \times 10 = -10 + 20 = 10 \quad (\text{pairs } (1, 2) \text{ of cost } 3+1=4 \text{ and } (3, 4) \text{ of cost } 2+4=6)$$

---

#### Scratchpad 11.4.2 — Complete 3-Piece Convex Repair Trace in `CF 708 D — Incorrect Flow` (`P4.4`)
Suppose $V = \{1, 2, 3\}$ ($s = 1, t = 3$) has two edges with corrupted initial flows $f_e$ and capacities $c_e$:
- Edge $e_1 = (1 \to 2)$: given $f_{e_1} = 5$, capacity $c_{e_1} = 3$ (**Case 2: $f_e > c_e$!**).
- Edge $e_2 = (2 \to 3)$: given $f_{e_2} = 1$, capacity $c_{e_2} = 4$ (**Case 1: $f_e \le c_e$!**).

Let us trace the exact compilation from Section 8 (`P4.4`):
1. **Pre-Injected Flow & Base Cost**:
   - On $e_1 = (1 \to 2)$, pre-inject $f_{e_1} = 5$. Since $f_{e_1} = 5 > c_{e_1} = 3$, add $5 - 3 = 2$ to $C_{\text{base}}$.
   - On $e_2 = (2 \to 3)$, pre-inject $f_{e_2} = 1$. Since $f_{e_2} \le c_{e_2}$, add $0$ to $C_{\text{base}}$.
   - Vertex imbalances $M(v) = \text{in}^0(v) - \text{out}^0(v)$:
     - $M(1) = -5 \implies (1 \to T^*, \text{cap } 5, \text{cost } 0)$
     - $M(2) = 5 - 1 = +4 \implies (S^* \to 2, \text{cap } 4, \text{cost } 0)$
     - $M(3) = +1 \implies (S^* \to 3, \text{cap } 1, \text{cost } 0)$
   - Feedback edge: $(3 \to 1, \text{cap } \infty, \text{cost } 0)$.
2. **3-Piece Marginal Arcs Relative to Pre-Injected Flow**:
   - **For $e_1 = (1 \to 2)$ ($f_1 = 5 > c_1 = 3$)**:
     1. Reduce flow on $[3, 5]$ (saves $+1$ capacity expansion while paying $+1$ flow reduction $\implies$ **net cost $0$**!): $(2 \to 1, \text{cap } 2, \text{cost } 0)$.
     2. Reduce flow on $[0, 3]$: $(2 \to 1, \text{cap } 3, \text{cost } 1)$.
     3. Increase flow & capacity on $[5, \infty)$: $(1 \to 2, \text{cap } \infty, \text{cost } 2)$.
   - **For $e_2 = (2 \to 3)$ ($f_2 = 1 \le c_2 = 4$)**:
     1. Reduce flow on $[0, 1]$: $(3 \to 2, \text{cap } 1, \text{cost } 1)$.
     2. Increase flow on $[1, 4]$: $(2 \to 3, \text{cap } 3, \text{cost } 1)$.
     3. Increase flow & capacity on $[4, \infty)$: $(2 \to 3, \text{cap } \infty, \text{cost } 2)$.
3. **MCMF Execution from $S^*$ to $T^*$ (Total demand $= 5$)**:
   - **Path 1 (Cost $0$)**: $S^* \to 3 \xrightarrow{\text{feedback}} 1 \to T^*$, pushes $1$ unit at cost $0$.
   - **Path 2 (Cost $0$)**: $S^* \to 2 \xrightarrow{\text{free reduce } [3,5]} 1 \to T^*$, pushes $2$ units at cost $0$ (reducing $f_{e_1}$ from $5$ down to $3$!).
   - **Path 3 (Cost $1$)**: Remaining supply at $2$ is $4 - 2 = 2$. We can either push $2 \xrightarrow{\text{reduce } [0,3]} 1 \to T^*$ (cost $1$ per unit) OR push $2 \xrightarrow{\text{increase } [1,4]} 3 \xrightarrow{\text{feedback}} 1 \to T^*$ (also cost $1$ per unit!). Pushing $2$ units gives cost $2 \times 1 = 2$.
   - **Total Repair Cost**: $C_{\text{base}} + C_{S^*\to T^*} = 2 + (0 + 0 + 2) = 4$ (corresponding to setting $f'_1 = f'_2 = 3 \le c_1, c_2$, paying $|3-5| + |3-1| = 2 + 2 = 4$).

---

#### Scratchpad 11.4.3 — Complete Tree-DP State Machine for `[八省联考 2018] 林克卡特树` (`P4.7`)
When binary searching the Lagrangian penalty $\lambda$ per path in `[八省联考 2018] 林克卡特树` (where we want to maximize total weight of $K+1$ vertex-disjoint paths, so each completed path pays $-\lambda$), every vertex $u$ maintains 3 pairs `dp[u][d] = {max_weight, min_paths}` for $d \in \{0, 1, 2\}$:
- **Initialization at leaf / before children**:
  - `dp[u][0] = {0, 0}` ($u$ is not part of any path yet; or we only charge $-\lambda$ when a path **closes**).
  - `dp[u][1] = {0, 0}` ($u$ starts an open vertical path that has not yet closed).
  - `dp[u][2] = {-INF, 0}`.
- **Merging child $v$ (connected by edge $e = (u, v)$ of weight $w$) into $u$**:
  Let `best_v = dp[v][0]` be the finalized best state of $v$'s subtree (where any path inside $v$'s subtree cannot extend to $u$), and let `ext_v = max(dp[v][1], {0, 0}) + {w, 0}` be the best upward-extensible path from $v$ through edge $(u, v)$ into $u$. Update $u$'s states in reverse order $d = 2, 1, 0$:
  1. **Degree $d = 2$ (two paths meet at $u$, closing a path and paying $-\lambda$)**:
     $$\text{dp}[u][2] \gets \max\big(\text{dp}[u][2] + \text{best\_v},\; \text{dp}[u][1] + \text{ext\_v} + \{-\lambda, +1\}\big)$$
  2. **Degree $d = 1$ (one path extends into $u$)**:
     $$\text{dp}[u][1] \gets \max\big(\text{dp}[u][1] + \text{best\_v},\; \text{dp}[u][0] + \text{ext\_v}\big)$$
  3. **Degree $d = 0$ ($u$ untouched by incident tree edges)**:
     $$\text{dp}[u][0] \gets \text{dp}[u][0] + \text{best\_v}$$
- **Finalizing $u$ after all children are merged (closing any path whose highest vertex is $u$)**:
  $$\text{dp}[u][0] \gets \max\Big(\text{dp}[u][0],\; \text{dp}[u][1] + \{-\lambda, +1\},\; \text{dp}[u][2]\Big)$$
  *(Note: a single isolated vertex $u$ as a $0$-edge path is captured by `dp[u][1] + {-lambda, +1}` since `dp[u][1]` starts at `{0, 0}`!)*

---

### 11.5 Complete Worked Scratchpad for Circular-Ones Shift Scheduling (`循环 1 矩阵`)

To illustrate **Section 7.2.A (Circular-Ones Matrix Transformation)**, suppose a 24-hour system is divided into $T = 3$ cyclic 8-hour shifts ($t = 0, 1, 2$) with worker demands $A_0 = 3, A_1 = 4, A_2 = 2$, and 3 shift types where each worker works 2 consecutive slots (wrapping around modulo $3$):
- Shift $x_0$: works slots $\{0, 1\}$ ($L_0 = 0, R_0 = 1$, linear contiguous), cost $c_0 = 5$.
- Shift $x_1$: works slots $\{1, 2\}$ ($L_1 = 1, R_1 = 2$, linear contiguous), cost $c_1 = 6$.
- Shift $x_2$: works slots $\{2, 0\}$ ($L_2 = 2, R_2 = 0$, **overnight wrap-around shift!**), cost $c_2 = 4$.

1. **Original Cyclic Equations ($t = 0, 1, 2$)**:
   $$\begin{aligned}
   E_0: \quad & x_0 \phantom{{}+ x_1} + x_2 - y_0 = 3 \\
   E_1: \quad & x_0 + x_1 \phantom{{}+ x_2} - y_1 = 4 \\
   E_2: \quad & \phantom{x_0 +{}} x_1 + x_2 - y_2 = 2
   \end{aligned}$$
   Notice that column $x_2$ has $1$s in rows $0$ and $2$ (non-contiguous!).
2. **Apply Cyclic Modular Differencing $\Delta^{\text{cyc}} E_t := E_t - E_{(t-1) \bmod 3}$**:
   $$\begin{aligned}
   \Delta^{\text{cyc}} E_0 = E_0 - E_2: \quad & +x_0 - x_1 \phantom{{}+ 0x_2} - y_0 + y_2 = 3 - 2 = +1 \\
   \Delta^{\text{cyc}} E_1 = E_1 - E_0: \quad & \phantom{+0x_0} + x_1 - x_2 - y_1 + y_0 = 4 - 3 = +1 \\
   \Delta^{\text{cyc}} E_2 = E_2 - E_1: \quad & -x_0 \phantom{{}+ 0x_1} + x_2 - y_2 + y_1 = 2 - 4 = -2
   \end{aligned}$$
3. **Inspect the Columns of $\Delta^{\text{cyc}} E$**:
   - Column $x_0$: $+1$ at $0$, $-1$ at $2 \implies$ directed edge $0 \to 2$ (cost $5$).
   - Column $x_1$: $+1$ at $1$, $-1$ at $0 \implies$ directed edge $1 \to 0$ (cost $6$).
   - Column $x_2$ (**the wrap-around shift!**): $+1$ at $2$, $-1$ at $1 \implies$ directed edge $2 \to 1$ (cost $4$)!
   - Slack columns $y_t$: $y_0$ is $1 \to 0$, $y_1$ is $2 \to 1$, $y_2$ is $0 \to 2$ (cost $0$).
   *(Subtlety: In the cyclic difference system, $\Delta^{\text{cyc}} E_0 + \Delta^{\text{cyc}} E_1 + \Delta^{\text{cyc}} E_2 \equiv 0$, so the rank of the difference system is $T - 1 = 2$ instead of $3$; fixing the flow on any single wrap-around boundary—or parameterizing by total workforce $W = x_0 + x_1 + x_2$—restores the dropped degree of freedom and solves the cyclic schedule via convex MCMF in polynomial time!)*

---

### 11.6 Cross-Wave Synthesis Bridge: How Wave 3B Powers Wave 4 (Simulated Flow, Slope Trick, $L^\natural$-Convexity & Matroid Intersection)

The five reconciled iterations of **Wave 3B** form the direct mathematical foundation for **Part IV (Wave 4: Advanced Duality, Simulated Cost Flow, L-Convexity & Matroid Intersection)**:

1. **From Johnson Potentials $\pi(v)$ to Monotone Price-Function / Isotone Regression (`保序回归`, Wave 4)**:
   - In Section 2.2.C, the LP Dual of Min-Cost $b$-Flow optimized vertex potentials $\pi(v)$ subject to $\pi(v) - \pi(u) \le c_{uv}$.
   - When the residual cost on each edge is a convex function of potential difference $\Phi_{uv}(\pi(v) - \pi(u))$, the dual problem becomes the **Dual of Convex-Cost Tension / Isotone Regression** (`[国家集训队 2018] 保序回归`), solved by parallel binary search (`整体二分`) where each midpoint slice reduces to a Closure / Min-Cut problem!
2. **From Slope Convexity $C(f)$ to Slope Trick & Convex Hull Convolution (`Slope Trick`, Wave 4)**:
   - In Section 3.2, we proved that $C(f)$ is piecewise-linear and convex, with marginal slopes $\Delta C(k)$ stored implicitly as residual augmenting path costs.
   - When the underlying network is a tree or 1D series-parallel DAG (as in `Luogu P4546`, `CF 802O`, or `UOJ #455 雪灾与外卖`), maintaining the multiset of slope breakpoints $\Delta C(k)$ via mergeable heaps (`std::priority_queue` or leftist heaps) **is** the **Slope Trick**—computing the exact MCMF function $C_u(f)$ across all subtrees in $O(N \log N)$ without ever instantiating a flow graph!
3. **From Equation-Difference $\Delta E_t = E_t - E_{t-1}$ to Total Unimodularity & $M^\natural$-Concave Submodular Flow (Wave 4)**:
   - In Sections 6 and 7.2, we showed that Consecutive-Ones Matrices (`流守恒差分`) and Laminar/Tree-Path Matrices (`树上流守恒差分`) transform into Network Matrices (incidence matrices of directed graphs), which are **Totally Unimodular (TU)** and therefore guarantee integer optimal primal flows and integer dual potentials for any integer right-hand side $B_t$ and integer costs $c_j$.
   - Replacing the linear vertex conservation constraints $\nabla \cdot f = b$ with submodular base-polyhedron constraints $\nabla \cdot f \in \mathcal{B}(f_{\text{sub}})$ generalizes Equation-Difference MCMF directly to **Edmonds–Giles Submodular Flow** and **Weighted Matroid Intersection**!

| Wave 3B Foundation (Iterations 26–30 / 78–82) | Direct Wave 4 / Mastery Generalization | Governing Algebraic Bridge |
| :--- | :--- | :--- |
| **Johnson Potentials $\pi(v)$ & Complementary Slackness** | LP Dual Tension, Monotone Price Functions & Isotone Regression (`保序回归`) | $\pi(v) - \pi(u) \le c_{uv} \longleftrightarrow$ Lagrangian Dual of Flow Conservation |
| **Slope Convexity $\Delta C(1) \le \dots \le \Delta C(F)$ & WQS** | Simulated Cost Flow (`模拟费用流`), Regret Heaps & Slope Trick | Each heap pop/push = 1 SSP augmentation + residual edge reversal |
| **Convex Marginal Splitting $\Delta \phi(k)$ & Bit-Scaling** | $M^\natural$-Convex / $L^\natural$-Convex Discrete Minimization | Separable $\sum \phi_e(f_e)$ on a TU network preserves discrete convexity |
| **1D & Tree Equation-Difference ($\Delta E_t$, $\Delta^{\text{tree}} E_u$)** | Network Matrices, Total Unimodularity & Submodular Flow | Invertible row operations reducing path/interval LPs to $\text{Out}(v) - \text{In}(v) = \Delta B_v$ |
