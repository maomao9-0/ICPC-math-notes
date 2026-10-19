# Wave 4A Research Monograph (Cohort 2 — Independent Investigation, Iterations 83–87): Min-Cost Max-Flow (MCMF) II — Cycle Covers, Dynamic Lazy Scheduling, Resource Reuse & Coordinate Rank Models

> [!IMPORTANT]
> **Cohort 2 Redundant Independence Verification**
> This monograph (`flows_research/cohort2_iter_83_to_87_mcmf_cycles_dynamic_scheduling_ranks.md`) is authored independently by Cohort 2 (`FlowDeepInvestigator`) covering **Iterations 83–87** of the Network Flows, Minimum Cuts, Matching, Duality & Non-Graph Modelling project. Every modelling paradigm, algebraic derivation, graph compilation scratchpad, failure mode, and curated problem solution follows the **4-Step "Zero Magic Gadgets" Compilation Standard** defined in `flows_research/PLAN.md`.

---

## Executive Overview: From Algebraic Flow Conservation to Combinatorial Decomposition & Geometric Linearization

In Wave 3B (Iterations 78–82), we studied how Min-Cost Max-Flow (MCMF) models arise from convex marginal edge splitting and consecutive equation differences ($E_t - E_{t-1}$). In **Wave 4A (Iterations 83–87)**, we investigate five deeper structural paradigms where the MCMF network is not merely a transcription of flow conservation equations, but the result of **combinatorial decomposition, backward index reversal, temporal inventory splitting, order-statistic translation, or geometric dual-norm linearization**:

1. **Iteration 83 — Min-Cost Disjoint Paths, Cycle Covers, $b$-Matchings & The Chinese Postman Family**:
   - How parallel internal vertex-split arcs $(1, -w_v) \parallel (k-1, 0)$ encode "collect-once, pass-many" rewards (`方格取数`), and why residual backward arcs automatically uncross intersecting paths into $k$ disjoint walks (Suurballe's theorem).
   - How splitting each vertex into $v_{\text{out}} \in L$ and $v_{\text{in}} \in R$ establishes an exact bijection between bipartite matchings of size $N - K$ and partitions of a DAG into $K$ paths (`星际竞速`, `营救皮卡丘`), and why cycles in the underlying graph corrupt path covers into disconnected cycle+path unions.
   - How Eulerian tour repair (Chinese Postman Problem on undirected, directed, and mixed graphs) compiles degree imbalances into min-cost circulations and $T$-joins.
2. **Iteration 84 — Dynamic Lazy Vertex Generation (`动态加点费用流` — `[SCOI2007] 修车` & `[NOI2012] 美食节`)**:
   - How reversing the time index on each machine ($r = 1$ for the *last* job, $r = 2$ for the *second-to-last* job, $\dots$) eliminates the dependence on total queue length $k_j$, turning a non-local scheduling problem into linear assignment costs $r \cdot t_{i,j}$.
   - Why dominance $r \cdot t_{i,j} < (r+1) \cdot t_{i,j}$ guarantees that Successive Shortest Path (SSP) explores slots strictly in order $r = 1, 2, \dots$, allowing **lazy on-demand vertex spawning** that shrinks the active graph from $O(MP)$ vertices to $O(N + M + P)$, and how to initialize the Johnson potential $\pi((j^*, r+1))$ in $O(N)$ time without SPFA.
3. **Iteration 85 — Resource Reuse, Inventory & Caching Networks (`餐巾计划问题` & $k$-Register Allocation)**:
   - A head-to-head mathematical comparison of the **Bipartite Day/Night Split** (decoupling morning consumption from evening dirty supply without lower bounds) and the **Lower-Bound Flow Spine** (where dirty napkins are literally the conserved flow emerging from mandatory morning edges), plus interval caching models (`CF 802 C`, `POJ 3680`).
4. **Iteration 86 — 2D Prefix/Suffix Coordinate Rank Translation (`AGC 031 E — Snuke the Phantom Thief`)**:
   - How cardinality bounds on half-planes ("at most $b$ stolen jewels have $x \le a$") translate into exact coordinate bounds on the **sorted order statistics** $x_{(1)} \le \dots \le x_{(K)}$ and $y_{(1)} \le \dots \le y_{(K)}$, reducing a non-local 2D subset selection problem to a 4-layer MCMF network.
5. **Iteration 87 — Linearizing Manhattan & Chebyshev Distances via Sign-Combination Hubs (`AGC 034 D — Manhattan Max Matching`)**:
   - How the dual-norm identity $|x_1 - x_2| + |y_1 - y_2| = \max_{s_x, s_y \in \{\pm 1\}} \big((s_x x_1 + s_y y_1) + (-s_x x_2 - s_y y_2)\big)$ compresses a complete $O(N^2)$ bipartite graph into **4 sign-combination hubs** ($O(N)$ edges), how it generalizes to $\ell_1^d$ and $\ell_\infty^2$, and why **minimizing** Manhattan distance fails catastrophically on the same 4-hub gadget.

---

## Iteration 83: Min-Cost Disjoint Paths, Cycle Covers, $b$-Matchings & The Chinese Postman Family

### 83.1 Suurballe's $k$-Disjoint Paths & Collect-Once Grid Walks (`方格取数` / `传纸条`)

#### Step 1: The Non-Graph / Path-Tuple Diagnostic Signal (Recognition)
You are asked to find $k$ paths (typically $k \in [2, 10]$) from a source $S$ to a sink $T$ in a directed graph or grid such that:
- **Hard Disjointness Variant (`[SDOI2009] 晨跑`, Suurballe's Problem)**: The $k$ paths must be internally vertex-disjoint (or edge-disjoint), minimizing total edge length $\sum_{p=1}^k \text{len}(P_p)$.
- **Soft "Collect-Once" Variant (`网络流24题：方格取数` / `NOIP2008 传纸条` / `POJ 3422 Kaka's Matrix Travels`)**: The $k$ walks may share vertices and edges, but each vertex $v$ carries a non-negative reward $w_v \ge 0$ that can be collected **at most once** regardless of how many walks pass through $v$. We want to maximize the total collected reward.

**Why Naive Greedy and Multi-Walker DP Fail**:
1. *Failure of Sequential Greedy ("Find best path $P_1$, delete/zero out its rewards, then find $P_2$")*: A single path $P_1$ can cut across the "waist" of the graph, either disconnecting $S$ from $T$ (in hard disjointness) or hogging bottleneck transitions so $P_2$ is forced onto a terrible detour, whereas two non-crossing paths $P'_1, P'_2$ that split the waist yield a strictly better sum.
2. *Failure of Multi-Walker DP*: Tracking $k$ simultaneous walkers along diagonal anti-layers requires state space $O(N^k)$ per step. For $k = 2$ and $N \le 50$, $O(N^3)$ DP works (`传纸条`), but as soon as $k \ge 4$ (`POJ 3422`, $k \le 10$) or the graph is not a layered grid DAG (`晨跑`), DP explodes exponentially while MCMF runs in polynomial time independent of $O(N^k)$.

#### Step 2: The Algebraic Intermediate Representation
Instead of tracking $k$ distinct labeled walks $(P_1, \dots, P_k)$, we aggregate them into an **integer flow vector** $f \in \mathbb{Z}_{\ge 0}^E$ satisfying:
1. **Total Fleet Size**: Net outflow from $S$ (and net inflow to $T$) is exactly $k$:
   $$\sum_{e \in \delta^+(S)} f_e - \sum_{e \in \delta^-(S)} f_e = k, \qquad \sum_{e \in \delta^-(T)} f_e - \sum_{e \in \delta^+(T)} f_e = k$$
2. **Flow Conservation at Every Vertex $v \in V \setminus \{S, T\}$**:
   $$\sum_{e \in \delta^-(v)} f_e = \sum_{e \in \delta^+(v)} f_e =: f_v$$
   where $f_v \in \{0, 1, \dots, k\}$ denotes the total number of walks passing through vertex $v$.
3. **Vertex Throughput & Reward Function**:
   - In **Hard Internally Vertex-Disjoint Paths**, each internal vertex $v \notin \{S, T\}$ obeys $f_v \le 1$ (and for $S, T$, $f_S = f_T = k$).
   - In **Collect-Once Grid Walks**, $f_v \in \{0, 1, \dots, k\}$ is unconstrained up to $k$, and the reward earned at vertex $v$ is a **concave saturating function** of the vertex throughput $f_v$:
     $$R_v(f_v) = w_v \cdot \min(f_v, 1) = \begin{cases} 0 & \text{if } f_v = 0, \\ w_v & \text{if } f_v \ge 1. \end{cases}$$
   Converting maximization of $\sum_v R_v(f_v)$ into minimization of cost $C_v(f_v) = -R_v(f_v)$, the marginal cost of the $r$-th unit of flow through $v$ is:
   $$\Delta C_v(r) = C_v(r) - C_v(r-1) = \begin{cases} -w_v & \text{for } r = 1, \\ 0 & \text{for } r \ge 2. \end{cases}$$
   Because $-w_v \le 0$ whenever $w_v \ge 0$, the marginal costs are **monotonically non-decreasing** ($-w_v \le 0 \le 0 \le \dots$), so $C_v(f_v)$ is a **convex cost function** of $f_v$!

#### Step 3: The Reverse-Engineering Scratchpad (Graph Compilation)
By the convex marginal splitting principle, we compile vertex throughput $f_v$ and its convex cost $C_v(f_v)$ by splitting each vertex $v \in V$ into an entry node $v_{\text{in}}$ and an exit node $v_{\text{out}}$:

| Algebraic Object / Constraint | Graph Gadget Compilation (`(capacity, cost)`) | Why This Exact Gadget is Forced |
| :--- | :--- | :--- |
| Vertex throughput variable $f_v = \sum_{e \in \delta^-(v)} f_e = \sum_{e \in \delta^+(v)} f_e$ | Split $v$ into $v_{\text{in}}$ and $v_{\text{out}}$; redirect all incoming edges $(u, v)$ to $u_{\text{out}} \to v_{\text{in}}$ and outgoing edges $(v, w)$ to $v_{\text{out}} \to w_{\text{in}}$ | Isolates the scalar quantity $f_v$ as the flow across the internal bridge $v_{\text{in}} \to v_{\text{out}}$. |
| Hard Vertex-Disjointness: $f_v \le 1$ with vertex traversal cost $c_v$ | Single internal directed edge $v_{\text{in}} \to v_{\text{out}}$ with $(\text{cap} = 1, \text{cost} = c_v)$ for $v \notin \{S, T\}$; $(\text{cap} = k, \text{cost} = 0)$ for $S, T$ | Caps total walks visiting $v$ at $1$. |
| Collect-Once Reward: $\Delta C_v(1) = -w_v$ and $\Delta C_v(r) = 0$ for $2 \le r \le k$ | Two **parallel** internal directed edges from $v_{\text{in}}$ to $v_{\text{out}}$:<br>1. **Reward edge**: $(\text{cap} = 1, \text{cost} = -w_v)$<br>2. **Bypass edge**: $(\text{cap} = k - 1 \text{ or } \infty, \text{cost} = 0)$ | Because $-w_v \le 0$, the first walk passing through $v$ greedily saturates the $(-w_v)$ edge; subsequent walks pass across the $0$-cost bypass edge without double-counting $w_v$. |
| Grid movement $(r, c) \to (r+1, c)$ and $(r, c) \to (r, c+1)$ | Directed edge $(r,c)_{\text{out}} \to (r+1,c)_{\text{in}}$ and $(r,c)_{\text{out}} \to (r,c+1)_{\text{in}}$ with $(\text{cap} = \infty, \text{cost} = 0)$ | Allows up to $k$ walks to share transition edges freely at zero transition cost. |

> [!TIP]
> **How Residual Augmentation Uncrosses Intersecting Paths (Suurballe's Uncrossing Mechanism)**
> Suppose in iteration $1$, SSP finds a shortest path $P_1 = S \to a \to u \to v \to d \to T$ that uses the bridge $u \to v$. In the residual network, the forward edge $u_{\text{out}} \to v_{\text{in}}$ is saturated, and a **residual backward edge** $v_{\text{in}} \to u_{\text{out}}$ (along with $v_{\text{out}} \to v_{\text{in}}$) becomes available.
> In iteration $2$, an augmenting path $P_{\text{aug}} = S \to c \to v \xrightarrow{\text{back}} u \to b \to T$ traverses the backward edge from $v$ to $u$. When we add $f_{P_1} + f_{P_{\text{aug}}}$, the $+1$ flow on $u \to v$ and $-1$ flow on $v \to u$ cancel out! The combined flow of volume $2$ decomposes into two **non-crossing, vertex-disjoint paths**:
> $$P'_1 = S \to a \to u \to b \to T, \qquad P'_2 = S \to c \to v \to d \to T.$$
> Thus, MCMF's residual backward arcs are the exact algebraic embodiment of path uncrossing!

#### Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

**Toy Trace ($3 \times 3$ Collect-Once Grid with $k = 2$ walks)**:
Consider a $3 \times 3$ grid with rewards:
$$W = \begin{bmatrix} 0 & 5 & 1 \\ 2 & 10 & 5 \\ 1 & 2 & 0 \end{bmatrix}$$
- **Naive Sequential Greedy**:
  - Walk 1 picks the maximum-weight path $(1,1) \to (1,2)[5] \to (2,2)[10] \to (2,3)[5] \to (3,3)$, collecting $5 + 10 + 5 = 20$.
  - After zeroing out $(1,2), (2,2), (2,3)$, Walk 2 can at best take $(1,1) \to (2,1)[2] \to (3,1)[1] \to (3,2)[2] \to (3,3)$, collecting $2 + 1 + 2 = 5$.
  - **Greedy Total**: $20 + 5 = 25$. (Wait: in fact, if Walk 1 was prohibited from sharing vertices as in `传纸条`, Walk 1 passing through $(1,2) \to (2,2) \to (2,3)$ doesn't block $(2,1) \to (3,1) \to (3,2)$, wait—what if $W_{2,1} = 8, W_{3,2} = 8, W_{1,3} = 0, W_{3,1} = 0$? Let's check!)
  - Modify $W$:
    $$W' = \begin{bmatrix} 0 & 5 & 0 \\ 8 & 10 & 5 \\ 0 & 8 & 0 \end{bmatrix}$$
  - **Sequential Greedy on $W'$**:
    - Walk 1 takes $(1,1) \to (2,1)[8] \to (2,2)[10] \to (3,2)[8] \to (3,3)$ with reward $8 + 10 + 8 = 26$.
    - Now $(2,1), (2,2), (3,2)$ are zeroed out (or blocked in `传纸条`). Walk 2 is forced along the upper boundary $(1,1) \to (1,2)[5] \to (1,3)[0] \to (2,3)[5] \to (3,3)$, getting $5 + 5 = 10$ (and if $(2,1)$ and $(3,2)$ are blocked, $(2,2)$ cannot be reached at all!).Wait: even with $26 + 10 = 36$, wait—can we get $8 + 10 + 8 + 5 + 5 = 36$ with two walks? Yes, Walk A takes $(1,1) \to (1,2)[5] \to (2,2)[10] \to (2,3)[5] \to (3,3)$ ($20$) and Walk B takes $(1,1) \to (2,1)[8] \to (3,1)[0] \to (3,2)[8] \to (3,3)$ ($16$), total $36$!
    - Why did Greedy get $36$ there? Because $(1,3)$ had $0$. Now set $W'_{1,3} = -\infty$ (an obstacle at $(1,3)$ and $(3,1)$)!
    - With obstacles at $(1,3)$ and $(3,1)$:
      - Walk 1 greedy takes $(1,1) \to (2,1)[8] \to (2,2)[10] \to (3,2)[8] \to (3,3)$ (reward $26$).
      - Because $(1,3)$ and $(3,1)$ are obstacles, **every** valid path from $(1,1)$ to $(3,3)$ must pass through $(2,2)$! And in `传纸条` (vertex-disjoint except if we allow $(2,2)$ or in a $3 \times 4$ waist), Walk 1 used **both** neighbors of $(2,2)$ along the anti-diagonal $(2,1)$ and $(3,2)$, blocking Walk 2 from either entering $(2,2)$ via $(2,1)$ or exiting $(2,2)$ via $(3,2)$ if vertex-disjoint!
      - In our MCMF network, Augmentation 1 sends flow along $(1,1) \to (2,1) \to (2,2) \to (3,2) \to (3,3)$ (cost $-26$). Augmentation 2 sends flow from $(1,1) \to (1,2) \to (2,2)_{\text{in}} \to (2,2)_{\text{out}} \to (2,3) \to (3,3)$ using the $0$-cost bypass edge at $(2,2)$ (or in a 4-column waist where $(2,2) \to (2,3)$ is a single bottleneck bridge, traverses the residual backward arc $(2,3)_{\text{in}} \to (2,2)_{\text{out}}$ to uncross the two walks into Upper Walk $(1,1) \to (1,2) \to (2,2) \to (2,3) \to (3,3)$ and Lower Walk $(1,1) \to (2,1) \to \dots \to (3,2) \to (3,3)$!).

**Broken Gadget Counterexamples**:
1. **Failure Mode 1 (Omitting Vertex Splitting and Putting Reward on Incoming Edges)**:
   Suppose a student avoids splitting $v$ into $v_{\text{in}}, v_{\text{out}}$ and instead places parallel edges $(1, -w_v) \parallel (k-1, 0)$ on *each* incoming grid edge $(r-1, c) \to (r, c)$ and $(r, c-1) \to (r, c)$.
   - *What breaks*: Walk 1 enters $(r, c)$ from above $(r-1, c) \to (r, c)$ and collects $w_{r,c}$. Walk 2 enters $(r, c)$ from the left $(r, c-1) \to (r, c)$ and **also** collects $w_{r,c}$! The reward $w_{r,c}$ is double-counted because the capacity-1 bottleneck was placed on the incoming edges rather than the vertex itself.
2. **Failure Mode 2 (Applying Parallel Edge Splitting to Negative Weights $w_v < 0$)**:
   Suppose a cell has a *penalty* ($w_v < 0$, so $-w_v > 0$) that is paid once if visited by at least one walk, and $0$ on subsequent visits.
   - *What breaks*: The marginal costs are $\Delta C_v(1) = |w_v| > 0$ and $\Delta C_v(2) = 0$. This is **concave** (decreasing marginal cost), not convex! If you put parallel edges $(1, |w_v|) \parallel (k-1, 0)$, the MCMF solver will simply route the *first* walk across the $(k-1, 0)$ bypass edge for free and never touch the $(1, |w_v|)$ penalty edge! Fixed-charge penalties ("pay once to unlock a vertex for $k$ walks") are NP-hard in general and cannot be modeled by parallel MCMF edges.

---

### 83.2 Min-Cost Directed Cycle Cover, $b$-Matchings & Path Cover with Fleet Size $K$ (`[SDOI2010] 星际竞速`, `[ZJOI2011] 营救皮卡丘`)

#### Step 1: The Diagnostic Signal (Recognition)
You are given $N$ vertices ($N \le 500$) and weighted directed edges $(u, v)$ with cost $c(u, v)$, and asked to cover all $N$ vertices using:
- **Directed Cycle Cover**: A collection of vertex-disjoint directed cycles covering every vertex $v \in V$ exactly once, minimizing total edge cost.
- **Min-Cost $K$-Path Cover on a DAG (`[SDOI2010] 星际竞速`, `[ZJOI2011] 营救皮卡丘`)**: At most $K$ vehicles/walkers start at a base (or teleport to any starting vertex at cost $A_v$), traverse vertex-disjoint directed paths, and collectively visit every vertex $v \in \{1, \dots, N\}$ exactly once at minimum total cost.

#### Step 2: The Algebraic Intermediate Representation
Let $x_{u,v} \in \{0, 1\}$ indicate whether directed edge $(u, v)$ is chosen in our cover.

1. **For a Directed Cycle Cover**:
   Every vertex $v \in V$ has exactly $1$ chosen outgoing edge and $1$ chosen incoming edge:
   $$\forall u \in V: \sum_{v \in V} x_{u,v} = 1, \qquad \forall v \in V: \sum_{u \in V} x_{u,v} = 1.$$
   Notice that these are the **exact equations of a Bipartite Perfect Matching** between $L = \{u_{\text{out}} : u \in V\}$ and $R = \{v_{\text{in}} : v \in V\}$! Any permutation $\sigma \in S_N$ with $x_{u, \sigma(u)} = 1$ decomposes uniquely into disjoint directed cycles.

2. **For a Directed Path Cover on a DAG**:
   Every vertex $v \in V$ has **at most $1$** chosen outgoing edge and **at most $1$** chosen incoming edge:
   $$\forall u \in V: \sum_{v \in V} x_{u,v} \le 1, \qquad \forall v \in V: \sum_{u \in V} x_{u,v} \le 1.$$
   **The Component-Merging Invariant**:
   Initially, before choosing any edges ($x = 0$), the $N$ vertices form $N$ trivial paths of length $0$ (each vertex is both the start and end of its own path). Because the graph is a **DAG** (no cycles can ever form), every chosen edge $x_{u,v} = 1$ merges the path ending at $u$ with the path starting at $v$, reducing the total number of paths by exactly $1$:
   $$\text{Number of Paths} = N - \sum_{(u,v) \in E} x_{u,v} = \sum_{v \in V} \left(1 - \sum_{u \in V} x_{u,v}\right).$$
   Here, the slack variable $s_v := 1 - \sum_{u \in V} x_{u,v} \in \{0, 1\}$ equals $1$ if and only if vertex $v$ has **no incoming edge** from another vertex—meaning $v$ is the **starting vertex** of a path (or is reached directly from the central starter hub / via a teleport jump)!
   Adding $s_v$ restores exact equality at every receiving vertex $v \in V$:
   $$\forall v \in V: \quad s_v + \sum_{u \in V} x_{u,v} = 1, \qquad \forall u \in V: \quad \sum_{v \in V} x_{u,v} \le 1, \qquad \sum_{v \in V} s_v \le K.$$

#### Step 3: The Reverse-Engineering Scratchpad (Graph Compilation)
Look at the restored equation $\forall v \in V: s_v + \sum_{u \in V} x_{u,v} = 1$:
- Every receiving node $v_{\text{in}} \in R$ demands **exactly $1$ unit of flow** (which we send to the sink $T$ via $v_{\text{in}} \to T$ of capacity $1$).
- That $1$ unit of flow into $v_{\text{in}}$ can come from **either**:
  1. An earlier vertex $u_{\text{out}} \in L$ via transition edge $u_{\text{out}} \to v_{\text{in}}$ ($x_{u,v} = 1$), where $u_{\text{out}}$ receives at most $1$ unit of flow from $S$ ($S \to u_{\text{out}}$ with capacity $1$), **OR**
  2. A **Starter / Fleet Hub $H_{\text{start}}$** via starter edge $H_{\text{start}} \to v_{\text{in}}$ ($s_v = 1$), where $S \to H_{\text{start}}$ has capacity $K$ (bounding total path starts $\sum_{v} s_v \le K$)!

Let us compile both variants cleanly:

```
          cap=1, cost=0               cap=1, cost=c(u,v)             cap=1, cost=0
     +------------------> u_out (L) -----------------------> v_in (R) ---------------+
     |                                                          ^                    |
     |                                                          |                    v
   [ S ]                                                        |                  [ T ]
     |                                                          |
     +------------------> H_start ------------------------------+
          cap=K, cost=0               cap=1, cost=start_cost(v)
```

| Problem Archetype | Edge $S \to H_{\text{start}}$ | Edge $H_{\text{start}} \to v_{\text{in}}$ | Edge $u_{\text{out}} \to v_{\text{in}}$ | Required Total Flow $F_{\text{req}}$ |
| :--- | :--- | :--- | :--- | :--- |
| **Directed Cycle Cover** | Capacity $0$ (omitted) | Omitted | $(\text{cap}=1, \text{cost}=c(u,v))$ | $F_{\text{req}} = N$ |
| **Unlimited Teleport + DAG Path Cover (`[SDOI2010] 星际竞速`)** | $(\text{cap}=\infty, \text{cost}=0)$ | $(\text{cap}=1, \text{cost}=A_v)$ (teleport cost to $v$) | $(\text{cap}=1, \text{cost}=c(u,v))$ for $u < v$ | $F_{\text{req}} = N$ |
| **$K$-Vehicle Precedence-Locked Path Cover (`[ZJOI2011] 营救皮卡丘`)** | $(\text{cap}=K, \text{cost}=0)$ | $(\text{cap}=1, \text{cost}=d_{\le v}(0, v))$ (start from base $0$) | $(\text{cap}=1, \text{cost}=d_{\le v}(u, v))$ for $1 \le u < v \le N$ | $F_{\text{req}} = N$ |

> [!IMPORTANT]
> **Subtlety in `[ZJOI2011] 营救皮卡丘` (Restricted-Intermediate Floyd–Warshall Preprocessing)**
> In `营救皮卡丘`, the underlying road network is an **undirected graph** where vertices $1, 2, \dots, N$ must be unlocked sequentially: you cannot pass through vertex $w$ until vertices $1, \dots, w-1$ have been destroyed/unlocked, and multiple walkers can pass through already-unlocked vertices freely!
> How do we reduce an undirected walk with sequential unlocking to our **Vertex-Disjoint DAG Path Cover**?
> - Each vertex $v \in \{1, \dots, N\}$ only needs to be visited **for the first time** (unlocked) by **one** of the $K$ walkers!
> - Suppose walker $p$ unlocked vertex $u$ and the **next new vertex** it unlocks is $v$ (with $u < v$). Between unlocking $u$ and unlocking $v$, vertices $1, \dots, v-1$ are already unlocked by the team, while vertices $v+1, \dots, N$ are still locked!
> - Therefore, the walker's physical travel from $u$ to $v$ can use any intermediate vertices in $\{0, 1, \dots, v-1\}$, and its minimum cost is the **restricted shortest path** $d_{\le v}(u, v)$ computed via Floyd–Warshall using only intermediate pivots $k \le \max(u, v)$!
> - Once we replace physical road steps with the macro-transition $u \to v$ ($u < v$) of cost $d_{\le v}(u, v)$, the macro-graph is a **strictly acyclic DAG** ($u < v$), and every vertex $v \in \{1, \dots, N\}$ must be unlocked as the endpoint of exactly one macro-step!

#### Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

**Toy Trace (`[SDOI2010] 星际竞速`, $N = 3$ planets)**:
- Teleport costs: $A_1 = 10, A_2 = 10, A_3 = 10$.
- Gravity flight edges ($u < v$): $c(1, 2) = 3$, $c(2, 3) = 4$, $c(1, 3) = 20$.
- Graph has $L = \{1_{\text{out}}, 2_{\text{out}}, 3_{\text{out}}\}$, $R = \{1_{\text{in}}, 2_{\text{in}}, 3_{\text{in}}\}$, and $H_{\text{start}}$.
- To supply $F_{\text{req}} = 3$ units to $T$ (via $1_{\text{in}}, 2_{\text{in}}, 3_{\text{in}}$):
  - Planet $1_{\text{in}}$ has no incoming flight edges ($u < 1$ is empty), so it must use $H_{\text{start}} \to 1_{\text{in}}$ (cost $A_1 = 10$).
  - Planet $2_{\text{in}}$ chooses between $H_{\text{start}} \to 2_{\text{in}}$ (cost $10$) and $1_{\text{out}} \to 2_{\text{in}}$ (cost $3$); it takes $1_{\text{out}} \to 2_{\text{in}}$ (cost $3$).
  - Planet $3_{\text{in}}$ chooses between $H_{\text{start}} \to 3_{\text{in}}$ (cost $10$), $1_{\text{out}} \to 3_{\text{in}}$ (already saturated $1_{\text{out}}$), and $2_{\text{out}} \to 3_{\text{in}}$ (cost $4$); it takes $2_{\text{out}} \to 3_{\text{in}}$ (cost $4$).
- Total cost: $10 + 3 + 4 = 17$, corresponding to $1$ teleport to Planet 1 followed by path $1 \to 2 \to 3$.

**Broken Gadget Counterexamples**:
1. **Failure Mode 1 (Running Bipartite Path Cover on a Non-DAG with Directed Cycles)**:
   Suppose $N = 4$, $K = 1$ (we want a **single Hamiltonian path** of minimum cost), and the graph is **not** a DAG: vertices $\{1, 2, 3\}$ form a directed 3-cycle $1 \to 2 \to 3 \to 1$ of cost $1 + 1 + 1 = 3$, and vertex $4$ is an isolated vertex (or connected only via cost-$100$ edges).
   - *What breaks*: In the bipartite $u_{\text{out}} \to v_{\text{in}}$ network, the solver selects $x_{1,2} = x_{2,3} = x_{3,1} = 1$ (3 matched edges!) and $s_4 = 1$ (1 starter edge to vertex 4).
   - It satisfies $\sum s_v = 1 \le K$ and $N - \sum x_{u,v} = 4 - 3 = 1$, claiming to have found "1 path" of cost $3$!
   - In reality, $x_{1,2} = x_{2,3} = x_{3,1} = 1$ is a **disconnected directed cycle** $(1 \to 2 \to 3 \to 1)$ plus a trivial path $(4)$! The formula $\text{Paths} = N - \sum x_{u,v}$ is **only valid on a DAG** because on a general graph, cycles absorb edges without reducing the number of path starts! (On general graphs, minimum Hamiltonian path is NP-hard.)
2. **Failure Mode 2 (Unrestricted Floyd–Warshall in `营救皮卡丘`)**:
   If you precompute all-pairs shortest paths $d(u, v)$ allowing *arbitrary* intermediate vertices $k \in \{1, \dots, N\}$ instead of restricting $k \le \max(u, v)$, then the macro-step $1 \to 2$ could secretly route through vertex $3$ ($1 \to 3 \to 2$) before vertex $2$ or $3$ has been unlocked, violating the problem's sequential unlocking rule!

---

### 83.3 The Chinese Postman Problem (CPP) Family — Undirected, Directed & Mixed Graphs

#### Step 1: The Diagnostic Signal (Recognition)
A snowplow, street sweeper, or robotic arm must traverse **every edge** of a strongly connected (or connected) graph $G = (V, E)$ **at least once** and return to its starting vertex, minimizing total traversal cost $\sum_{e \in E} k_e c_e$ (where $k_e \ge 1$ is the number of times edge $e$ is traversed).
- **Variant A (Directed CPP)**: Every edge $e = (u, v)$ is directed with cost $c_e \ge 0$.
- **Variant B (Undirected CPP)**: Every edge $e = \{u, v\}$ is undirected with cost $c_e \ge 0$.
- **Variant C (Mixed CPP & Windyman's Eulerian Orientation)**: $G$ contains both directed edges and undirected edges.
  - *Pure Orientation (`混合图欧拉回路`)*: Can we orient each undirected edge so the graph becomes Eulerian (every edge traversed **exactly once**)?
  - *Free-Duplication / Weighted Mixed CPP*: Can we orient and duplicate edges to form a min-cost closed walk covering every edge at least once?

#### Step 2: The Algebraic Intermediate Representation
By Euler's theorem, a multigraph has an Eulerian circuit if and only if it is connected (or strongly connected) and satisfies degree balance at every vertex. Instead of solving for total traversals $k_e \ge 1$, write $k_e = 1 + x_e$, where $x_e \in \mathbb{Z}_{\ge 0}$ is the number of **extra duplicate traversals** of edge $e$:
$$\text{Total Cost} = \underbrace{\sum_{e \in E} c_e}_{\text{mandatory base cost}} + \min \sum_{e \in E} c_e x_e.$$

1. **Directed CPP (Flow Imbalance Repair)**:
   Let $\text{imb}(v) := d_{\text{in}}(v) - d_{\text{out}}(v)$ be the initial degree imbalance at vertex $v$ when every edge is traversed once. Adding $x_{u,v} \ge 0$ duplicate copies of $(u, v)$ requires:
   $$\forall v \in V: \quad \sum_{e \in \delta^+(v)} x_e - \sum_{e \in \delta^-(v)} x_e = \text{imb}(v) = d_{\text{in}}(v) - d_{\text{out}}(v).$$
   This is literally the **Uncapacitated Min-Cost Flow (Circulation)** equation with supply $b(v) = d_{\text{in}}(v) - d_{\text{out}}(v)$!

2. **Undirected CPP (Odd-Degree Parity Repair / $T$-Join)**:
   In an undirected graph, every vertex $v$ needs even total degree: $d(v) + \sum_{e \in \delta(v)} x_e \equiv 0 \pmod 2$.
   Let $O = \{v \in V : d(v) \equiv 1 \pmod 2\}$ be the set of **odd-degree vertices** (note $|O|$ is always even by the handshaking lemma). The minimum-cost set of duplicate edges $x_e \in \{0, 1\}$ whose odd-degree vertices are exactly $O$ decomposes into $|O|/2$ edge-disjoint shortest paths pairing up the vertices of $O$. Thus Undirected CPP reduces to **Minimum-Weight Perfect Matching (Blossom Algorithm)** on the complete graph $K_{|O|}$ with shortest-path distances $d_G(u, v)$! (When $|O| \le 20$, bitmask DP in $O(2^{|O|} |O|)$ suffices.)

3. **Mixed Graph Eulerian Orientation & Cost-Symmetric Mixed CPP**:
   Suppose $G$ has directed edges $E_D$ and undirected edges $E_U$. First, arbitrarily orient every undirected edge $e = \{u, v\} \in E_U$ as a directed arc $u \to v$.
   Now let $\text{imb}(v) = d_{\text{in}}(v) - d_{\text{out}}(v)$ be the resulting net in-degree minus out-degree.
   - **Parity Necessary Condition**: Reversing the orientation of an edge $u \to v$ changes $d_{\text{in}}(u) - d_{\text{out}}(u)$ by $+2$ and $d_{\text{in}}(v) - d_{\text{out}}(v)$ by $-2$. Therefore, if **any** vertex $v$ has $\text{imb}(v) \equiv 1 \pmod 2$ (equivalently, total degree $d_D(v) + d_U(v)$ is odd) and no extra edge duplications are allowed, **no Eulerian orientation exists**!
   - When $\text{imb}(v)$ is even for all $v$, let $y_e \in \{0, 1\}$ indicate whether we reverse the initial orientation of $e = (u, v) \in E_U$. Each reversal $y_e = 1$ transfers $1$ unit of balance (representing a change of $2$ in $\text{imb}$), so dividing the balance equation by $2$:
     $$\forall v \in V: \quad \sum_{e \in \delta^+_U(v)} y_e - \sum_{e \in \delta^-_U(v)} y_e = -\frac{\text{imb}(v)}{2}.$$

#### Step 3: The Reverse-Engineering Scratchpad (Graph Compilation)

| Variant | Vertex Supply $b(v)$ | Edge Compilation (`(capacity, cost)`) | Solver Required |
| :--- | :--- | :--- | :--- |
| **Directed CPP** | $b(v) = d_{\text{in}}(v) - d_{\text{out}}(v)$ | For each $e = (u, v) \in E$: directed arc $u \to v$ with $(\text{cap} = \infty, \text{cost} = c_e)$ | Standard MCMF ($S \to v$ with cap $b(v)$ if $b(v) > 0$; $v \to T$ with cap $|b(v)|$ if $b(v) < 0$) |
| **Undirected CPP** | Odd-degree set $O = \{v : 2 \nmid d(v)\}$ | All-pairs shortest paths $d(u,v)$ on $O$; complete graph $K_{|O|}$ with weight $d(u,v)$ | General Min-Weight Perfect Matching (Blossom) or Bitmask DP if $|O| \le 20$ |
| **Weighted Mixed Eulerian Orientation** (orient $u \to v$ at cost $c^+_e$ or $v \to u$ at cost $c^-_e$, no duplicates) | Pre-orient $u \to v$ (base cost $\sum c^+_e$); if $2 \nmid \text{imb}(v)$ return impossible; else $b(v) = -\frac{\text{imb}(v)}{2}$ | For each $e = \{u, v\} \in E_U$: directed arc $v \to u$ with $(\text{cap} = 1, \text{cost} = c^-_e - c^+_e)$ | Max-Flow (if unweighted) or MCMF (check if full flow $\sum_{b(v)>0} b(v)$ is saturated) |

#### Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

**Toy Trace (Directed CPP on a 3-Vertex Graph)**:
Suppose $V = \{1, 2, 3\}$ with directed edges:
- $e_1 = (1, 2)$ of cost $2$,
- $e_2 = (2, 3)$ of cost $3$,
- $e_3 = (3, 1)$ of cost $10$,
- $e_4 = (1, 3)$ of cost $4$.
1. **Base Cost**: $\sum c_e = 2 + 3 + 10 + 4 = 19$.
2. **Degree Imbalances $b(v) = d_{\text{in}}(v) - d_{\text{out}}(v)$**:
   - $b(1) = 1 - 2 = -1$ (Sink demand: $1 \to T$ with capacity $1$),
   - $b(2) = 1 - 1 = 0$,
   - $b(3) = 2 - 1 = +1$ (Source supply: $S \to 3$ with capacity $1$).
3. **MCMF Augmentation**: We need $1$ unit of flow from $3$ to $1$.
   - Direct path $3 \to 1$ has cost $10$.
   - Total minimum cost: $19 + 10 = 29$ (edge $(3, 1)$ is traversed twice: $1 \to 2 \to 3 \to 1 \to 3 \to 1$).

**Broken Gadget Counterexample (Why General Mixed CPP with Edge Duplication is NP-Hard!)**:
A notorious trap is assuming that **Mixed CPP** (where both directed and undirected edges can be traversed $\ge 1$ times at cost $c_e > 0$) can be solved by just combining the Directed CPP MCMF gadget and the Mixed Eulerian Orientation gadget!
- *Why it fails*: Reversing an undirected edge $e = \{u, v\}$ changes $\text{imb}(u) - \text{imb}(v)$ by $2$ (an **even** jump at zero extra traversal cost if symmetric), whereas duplicating an edge changes $\text{imb}$ by $1$ (capable of fixing **odd** degree parities at cost $c_e > 0$). Because MCMF operates on conserved flow units of uniform scale ($1$ unit = $1$ degree change) and cannot enforce mod-2 parity constraints without fixing the orientation of undirected edges, general Mixed CPP is **NP-hard** (Papadimitriou 1976)! It only becomes polynomial-time solvable via MCMF when either (a) no extra duplications are allowed (Pure Eulerian Orientation, where $\div 2$ works), or (b) all vertex degrees are already even!

---

## Iteration 84: Dynamic Lazy Vertex Generation in MCMF (`动态加点费用流` — `[SCOI2007] 修车` & `[NOI2012] 美食节`)

### 84.1 The Backward Waiting-Time Algebra

#### Step 1: The Non-Graph Diagnostic Signal (Recognition)
Look for the following signature in scheduling problems (`[SCOI2007] 修车`, `[NOI2012] 美食节`, `UVa 10746 Crime Wave`):
- There are $N$ job types (with $p_i$ identical jobs of type $i$, total jobs $P = \sum_{i=1}^N p_i \le 800$) and $M$ parallel machines/chefs ($M \le 100$).
- Machine $j$ takes $t_{i,j} > 0$ time to process one job of type $i$, and processes its assigned jobs **sequentially one after another**.
- **Objective**: Minimize the **sum of completion times** (or average waiting + processing time) across all $P$ jobs.

**Why Forward Indexing Fails and Why Static MCMF TLEs**:
1. *Failure of Forward Indexing*: Suppose machine $j$ processes $k_j$ jobs in forward order $q_1, q_2, \dots, q_{k_j}$. The completion time of the $s$-th job is $C_s = t_{q_1, j} + t_{q_2, j} + \dots + t_{q_s, j}$. How much does the $s$-th job $q_s$ contribute to the **sum** of completion times $\sum_{s=1}^{k_j} C_s$? It delays itself and all subsequent jobs $q_{s+1}, \dots, q_{k_j}$, so its coefficient is $(k_j - s + 1) \cdot t_{q_s, j}$!
   In forward indexing, this coefficient depends on the unknown total number of jobs $k_j$ assigned to machine $j$, coupling all decisions on machine $j$!
2. *Failure of Static MCMF (`[NOI2012] 美食节`)*: Even after reversing the index, a static graph creates $P$ time-slot vertices for each of the $M$ machines: $V_{\text{slots}} = M \times P = 100 \times 800 = 80{,}000$ vertices and $E = N \times M \times P = 40 \times 80{,}000 = 3.2 \times 10^6$ edges! Running $P = 800$ iterations of SPFA or Dijkstra on $3.2 \times 10^6$ edges easily exceeds the $1$–$2$ second time limit.

#### Step 2: The Algebraic Intermediate Representation
Reverse the index of the queue on each machine $j$:
- Let $r = 1$ denote the **last** job processed by machine $j$,
- Let $r = 2$ denote the **second-to-last** job processed by machine $j$,
- In general, let $r \in \{1, 2, \dots, k_j\}$ denote the **$r$-th from last** job processed by machine $j$.

Now count how many jobs wait for the job placed in backward slot $(j, r)$:
- The job in slot $(j, r)$ delays **itself** ($1$ job) plus the **$r - 1$ jobs processed after it** (slots $r-1, r-2, \dots, 1$).
- Therefore, regardless of the total queue length $k_j$, a job of type $i$ placed in backward slot $(j, r)$ contributes **precisely**:
  $$\text{Contribution}(i \to (j, r)) = r \cdot t_{i,j}$$
  to the total sum of completion times!

Let $x_{i, j, r} \in \{0, 1\}$ indicate whether a job of type $i$ is assigned to machine $j$'s $r$-th-from-last slot $(j, r)$. The problem is now a pure linear assignment / transportation problem:
$$\min \sum_{i=1}^N \sum_{j=1}^M \sum_{r=1}^P \big(r \cdot t_{i,j}\big) x_{i, j, r}$$
subject to:
$$\forall i \in [1, N]: \sum_{j=1}^M \sum_{r=1}^P x_{i, j, r} = p_i, \qquad \forall j \in [1, M], r \in [1, P]: \sum_{i=1}^N x_{i, j, r} \le 1.$$

> [!NOTE]
> **Why Does an Arbitrary Subset of Slots Automatically Form a Contiguous Prefix $r \in \{1, 2, \dots, k_j\}$?**
> Notice that we relaxed the constraint "slots $1, 2, \dots, k_j$ must be contiguous" to simply $\sum_{i=1}^N x_{i,j,r} \le 1$ for all $r \in [1, P]$. Why can't the optimal solution leave a gap—say, filling slot $(j, 1)$ and slot $(j, 3)$ while leaving $(j, 2)$ empty?
> Because $t_{i,j} > 0$, we have $2 \cdot t_{i,j} < 3 \cdot t_{i,j}$ for every job $i$! Moving the job from $(j, 3)$ to the empty slot $(j, 2)$ strictly decreases the objective by $t_{i,j} > 0$. Thus any minimum-cost flow **automatically** fills a contiguous prefix of backward slots $r = 1, 2, \dots, k_j$ on each machine $j$!

---

### 84.2 Lazy On-Demand Vertex Spawning & Johnson Potential Maintenance

#### Step 3: The Reverse-Engineering Scratchpad (Lazy Graph Compilation)
Because slot $(j, r+1)$ has cost $(r+1) \cdot t_{i,j} > r \cdot t_{i,j}$ for every job type $i$, we can prove a stronger **Augmentation Monotonicity Invariant**:

**Theorem 84.1 (Frontier Slot Invariant for Lazy MCMF)**:
*In the Successive Shortest Path (SSP) algorithm, at any stage where slots $r = 1, 2, \dots, k_j$ of machine $j$ are already saturated ($\sum_i x_{i,j,r} = 1$) and slots $r > k_j$ are empty ($\sum_i x_{i,j,r} = 0$), no shortest augmenting path from $S$ to $T$ needs to visit any slot $(j, r)$ with $r \ge k_j + 2$.*

*Proof*:
Any empty slot $(j, r)$ ($r \ge k_j + 1$) has zero flow on its outgoing edge $(j, r) \to T$ and zero flow on all incoming edges $i \to (j, r)$. Consequently, in the residual network, $(j, r)$ has **no outgoing residual edges to any job vertex $i$**; its only outgoing residual edge is $(j, r) \to T$ of cost $0$. Thus, if an augmenting path visits an empty slot $(j, r)$, that slot must be the **final vertex before $T$**: $S \to \dots \to i \to (j, r) \to T$.
Comparing the last two steps for $r = k_j + 1$ versus any $r \ge k_j + 2$:
$$\text{cost}(i \to (j, k_j + 1) \to T) = (k_j + 1) \cdot t_{i,j} < r \cdot t_{i,j} = \text{cost}(i \to (j, r) \to T).$$
Therefore, $(j, k_j + 1)$ strictly dominates all $(j, r)$ with $r \ge k_j + 2$, so we only need **one active empty frontier slot $(j, k_j + 1)$ per machine $j$** in the graph at any time! $\blacksquare$

**The Dynamic Lazy Compilation Algorithm**:
1. **Initial Graph ($P = 0$ augmentations done)**:
   - Source $S$, Sink $T$, and $N$ job-type vertices $i \in \{1, \dots, N\}$ with $S \to i$ of $(\text{cap} = p_i, \text{cost} = 0)$.
   - Create **only slot $r = 1$** for each machine $j \in \{1, \dots, M\}$: add vertex $(j, 1)$, edge $(j, 1) \to T$ with $(\text{cap} = 1, \text{cost} = 0)$, and $N$ edges $i \to (j, 1)$ with $(\text{cap} = 1, \text{cost} = 1 \cdot t_{i,j})$.
   - Initial active vertices: $N + M + 2 \le 142$. Initial active edges: $N + M + NM \le 4{,}140$.
2. **After Each Unit Augmentation ($P$ times total)**:
   - Find the shortest $S \to T$ augmenting path and push $1$ unit of flow.
   - Let $(j^*, r)$ be the unique slot vertex whose edge $(j^*, r) \to T$ was just saturated by the final step of this augmenting path! (Note: intermediate backward/forward steps may rearrange jobs among already-saturated slots $(j', r')$, leaving them saturated; only the final vertex before $T$ transitions from empty to saturated!)
   - **Lazy Spawn**: Immediately allocate a single new vertex $(j^*, r + 1)$, add edge $(j^*, r + 1) \to T$ with $(\text{cap} = 1, \text{cost} = 0)$, and add $N$ edges $i \to (j^*, r + 1)$ for $i \in \{1, \dots, N\}$ with $(\text{cap} = 1, \text{cost} = (r + 1) \cdot t_{i, j^*})$.
3. **Final Graph Size after all $P$ augmentations**:
   - Total vertices ever created: $N + M + P + 2 \approx 40 + 100 + 800 + 2 = 942$ (down from $80{,}042$, an **$85\times$ reduction**!).
   - Total edges ever created: $N + (M + P)(N + 1) \approx 40 + 900 \times 41 = 36{,}940$ (down from $3.2 \times 10^6$, an **$86\times$ reduction**!).

> [!TIP]
> **Maintaining Johnson Potentials $\pi$ Under Lazy Vertex Spawning (Zero-SPFA Dijkstra!)**
> If you use Dijkstra with Johnson potentials $\pi(u)$ (where reduced cost $c_\pi(u, v) = c(u, v) + \pi(u) - \pi(v) \ge 0$ for every residual edge), what potential $\pi((j^*, r+1))$ should you assign to the newly spawned vertex $(j^*, r+1)$ after updating all existing potentials $\pi(u) \gets \pi(u) + d(u)$?
> - The newly spawned vertex $(j^*, r+1)$ has incoming residual edges from $i \in \{1, \dots, N\}$ of cost $(r+1) t_{i, j^*}$, and one outgoing residual edge to $T$ of cost $0$ (which has not yet been used, and need only satisfy reduced cost $\ge 0$ or be relaxed on the next Dijkstra run; in fact, in Dijkstra, $\pi(T)$ only appears on edges entering $T$).
> - Specifically, for every residual edge in the graph to have non-negative reduced cost **before** the next Dijkstra run, we need:
>   1. For every $i \in \{1, \dots, N\}$ with residual capacity on $i \to (j^*, r+1)$: $\pi((j^*, r+1)) \le \pi(i) + (r+1) t_{i, j^*}$.
>   2. For the edge $(j^*, r+1) \to T$: $\pi(T) \le \pi((j^*, r+1)) + 0 \iff \pi((j^*, r+1)) \ge \pi(T)$.
> - Setting:
>   $$\pi((j^*, r+1)) := \min_{i=1}^N \big(\pi(i) + (r+1) t_{i, j^*}\big)$$
>   computes $\pi((j^*, r+1))$ in $O(N)$ time! And why is $\pi((j^*, r+1)) \ge \pi(T)$ guaranteed? Because just before spawning $(j^*, r+1)$, slot $(j^*, r)$ was on the shortest path to $T$, meaning $\pi(T) = \pi((j^*, r)) = \min_{i} (\pi(i) + r \cdot t_{i, j^*}) < \min_{i} (\pi(i) + (r+1) \cdot t_{i, j^*}) = \pi((j^*, r+1))$!
> - Alternatively, if your implementation runs SPFA with SLF/LLL queue optimization, each of the $P = 800$ augmentations runs on $\le 36{,}940$ edges in $< 0.05$ seconds total.

#### Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

**Toy Trace (`[SCOI2007] 修车`, $N = 3$ cars, $M = 2$ technicians)**:
Suppose $p_1 = p_2 = p_3 = 1$ ($P = 3$ cars) and repair times $t_{i,j}$ are:
- Technician 1 ($j=1$): $t_{1,1} = 2, \; t_{2,1} = 10, \; t_{3,1} = 3$.
- Technician 2 ($j=2$): $t_{1,2} = 1, \; t_{2,2} = 2, \; t_{3,2} = 10$.

1. **Initial Graph**: Only slots $(1, 1)$ and $(2, 1)$ exist.
   - Edges to $(1, 1)$: costs $2, 10, 3$.
   - Edges to $(2, 1)$: costs $1, 2, 10$.
2. **Augmentation 1**: Shortest path is $S \to \text{Car } 1 \to (2, 1) \to T$ with cost $1$.
   - Slot $(2, 1)$ is saturated! **Lazily spawn $(2, 2)$** with edges from Cars $1, 2, 3$ of costs $2 \cdot (1, 2, 10) = (2, 4, 20)$.
3. **Augmentation 2**:
   - Candidate A: $S \to \text{Car } 3 \to (1, 1) \to T$ (cost $3$).
   - Candidate B: $S \to \text{Car } 2 \to (2, 1) \xrightarrow{\text{back}} \text{Car } 1 \to (1, 1) \to T$ (cost $2 - 1 + 2 = 3$).
   - Candidate C: $S \to \text{Car } 2 \to (2, 2) \to T$ (cost $4$).
   - Suppose it picks Candidate A: Car 3 goes to $(1, 1)$ (cost $3$, cumulative cost $1 + 3 = 4$).
   - Slot $(1, 1)$ is saturated! **Lazily spawn $(1, 2)$** with edges from Cars $1, 2, 3$ of costs $2 \cdot (2, 10, 3) = (4, 20, 6)$.
4. **Augmentation 3**:
   - Only Car 2 remains at $S$.
   - Direct to $(2, 2)$: $S \to \text{Car } 2 \to (2, 2) \to T$ has cost $4$.
   - Re-routing via residual backward arc $(2, 1) \to \text{Car } 1$:
     $$S \to \text{Car } 2 \xrightarrow{+2} (2, 1) \xrightarrow{-1} \text{Car } 1 \xrightarrow{+2} (2, 2) \to T$$
     Wait: look at that residual path! Car 2 takes slot $(2, 1)$ (last job on Tech 2, cost $+2$), pushing Car 1 out of $(2, 1)$ (cost $-1$) and moving Car 1 into slot $(2, 2)$ (second-to-last job on Tech 2, cost $+2 \cdot 1 = +2$)!
     Net cost of this augmentation: $2 - 1 + 2 = 3 < 4$!
   - Slot $(2, 2)$ is saturated! Cumulative minimum cost: $4 + 3 = 7$ (average $7 / 3 = 2.33$).
   - Verification of schedule: Tech 1 repairs Car 3 (completion time $3$). Tech 2 repairs Car 1 first (completion time $1$), then Car 2 second (completion time $1 + 2 = 3$). Sum of completion times: $3 + 1 + 3 = 7$. Notice how the residual backward arc $(2, 1) \to \text{Car } 1 \to (2, 2)$ **automatically reordered Tech 2's queue** so the faster job (Car 1, $t=1$) went ahead of the slower job (Car 2, $t=2$)!

**Broken Gadget Counterexamples**:
1. **Failure Mode 1 (Spawning New Slots for Every Intermediate Machine Visited on the Augmenting Path)**:
   In Augmentation 3 above, the path visited $(2, 1)$ and then ended at $(2, 2) \to T$. If a student spawns $(j, r+1)$ for *every* slot $(j, r)$ visited by the augmenting path, they would spawn $(2, 2)$ a second time when visiting $(2, 1)$!
   - *Rule*: Only the **single slot vertex $(j^*, r)$ immediately preceding $T$** on the augmenting path changes its saturation status from $0$ to $1$. You spawn **at most $1$ vertex per unit of flow**!
2. **Failure Mode 2 (Zero Processing Times $t_{i,j} = 0$)**:
   If $t_{i,j} = 0$ is allowed, then $r \cdot t_{i,j} = (r+1) \cdot t_{i,j} = 0$, so strict cost dominance no longer holds automatically—a tie-breaking rule (always preferring smaller $r$) is still preserved if $(j, r+1)$ is only spawned after $(j, r)$ is saturated, so lazy spawning **even fixes the tie-breaking order** for $t_{i,j} = 0$!

---

## Iteration 85: Resource Reuse, Inventory & Caching Networks (`餐巾计划问题` & $k$-Server / $k$-Register Allocation)

### 85.1 The Napkin Plan (`[网络流24题] 餐巾计划问题`) — Unifying the Bipartite Day/Night Split and the Lower-Bound Flow Spine

#### Step 1: The Non-Graph Diagnostic Signal (Recognition)
A restaurant operates over a horizon of $D$ days ($t = 1, 2, \dots, D$).
- On day $t$, the restaurant requires **exactly $r_t$ clean napkins**.
- Clean napkins can be acquired in three ways:
  1. **Bought fresh** on any morning at cost $p$ per napkin,
  2. **Carried over** (stored clean) from day $t - 1$ at cost $0$,
  3. **Returned from laundry**: after day $t$'s $r_t$ clean napkins are used, they become **$r_t$ dirty napkins** on evening $t$. Dirty napkins can be:
     - Stored dirty from evening $t$ to evening $t + 1$ at cost $0$,
     - Sent to the **fast laundry**, taking $m$ days and costing $f$ per napkin (arriving clean on morning $t + m$),
     - Sent to the **slow laundry**, taking $n$ days ($n > m$) and costing $s$ ($s < f$) per napkin (arriving clean on morning $t + n$).
- **Objective**: Satisfy all $D$ daily demands $r_1, \dots, r_D$ at minimum total cost.

**Why Greedy and Standard DP Fail**:
- Buying vs. fast washing vs. slow washing couples day $t$ with days $t + m$ and $t + n$.
- If $D \le 2000$, why can't we use a simple 1D DP? Because tracking the exact inventory vector of dirty napkins from recent days requires exponential state space.
- Why does a naive single-node-per-day flow graph fail? If day $t$ is a single vertex, flow entering day $t$ is clean napkins and flow leaving day $t$ is dirty napkins—but how do you force **exactly $r_t$ units of flow** to pass through vertex $t$ without lower bounds?

#### Step 2: The Algebraic Intermediate Representation & The Grand Unification
Let us write the physical conservation laws first (**Model B: Lower-Bound Flow Spine**), and then algebraically eliminate the lower bounds to derive **Model A: Bipartite Day/Night Split**! This eliminates the #1 pedagogical mystery in `餐巾计划问题`—namely, why editorials split each day into an isolated "Morning" sink node and an isolated "Evening" source node with no edge between them!

**Model B (Continuous Particle Spine with Mandatory Lower Bounds)**:
Split day $t$ into **Morning $M_t$** (clean napkin pool before use) and **Evening $E_t$** (dirty napkin pool after use):
1. **Usage on Day $t$**: Exactly $r_t$ clean napkins are used on day $t$ and become $r_t$ dirty napkins that evening. Thus, the directed edge $M_t \to E_t$ has **lower bound $L_t = r_t$, upper bound $U_t = r_t$, and cost $0$**:
   $$f(M_t \to E_t) = r_t.$$
2. **Clean Napkin Transitions (Entering/Leaving $M_t$)**:
   - Fresh purchase: $S_{\text{buy}} \to M_t$ with $(\text{cap} = \infty, \text{cost} = p)$,
   - Clean storage carryover (optional): $M_t \to M_{t+1}$ with $(\text{cap} = \infty, \text{cost} = 0)$,
   - Laundry arrivals: $E_{t-m} \to M_t$ (fast, cost $f$) and $E_{t-n} \to M_t$ (slow, cost $s$).
3. **Dirty Napkin Transitions (Leaving $E_t$)**:
   - Dirty storage carryover: $E_t \to E_{t+1}$ with $(\text{cap} = \infty, \text{cost} = 0)$,
   - Fast laundry: $E_t \to M_{t+m}$ with $(\text{cap} = \infty, \text{cost} = f)$,
   - Slow laundry: $E_t \to M_{t+n}$ with $(\text{cap} = \infty, \text{cost} = s)$,
   - Disposal at end of life (leftover dirty/clean napkins): $E_t \to T_{\text{dispose}}$ with $(\text{cap} = \infty, \text{cost} = 0)$.

Now apply the **Standard Lower-Bound Circulation Elimination** to the mandatory edge $M_t \xrightarrow{[r_t, r_t]} E_t$:
- An edge $u \xrightarrow{[L, U]} v$ with $L = U = r_t$ has residual capacity $U - L = 0$!
- Removing the fixed flow $f(M_t \to E_t) = r_t$ creates a **mandatory demand of $r_t$ at $M_t$** (compiled as $M_t \to T$ with capacity $r_t$) and a **mandatory supply of $r_t$ at $E_t$** (compiled as $S \to E_t$ with capacity $r_t$), while the edge $M_t \to E_t$ itself **vanishes completely** (since $U - L = 0$)!

> [!IMPORTANT]
> **Theorem 85.1 (Algebraic Equivalence of Day/Night Split and Lower-Bound Spine)**
> *The Bipartite Day/Night Split (`Model A`: $S \xrightarrow{r_t} E_t$ and $M_t \xrightarrow{r_t} T$ with no edge between $M_t$ and $E_t$) is not an ad-hoc trick—it is the **exact algebraic result** of eliminating the mandatory lower-bound usage edge $M_t \xrightarrow{[r_t, r_t]} E_t$ from the physical conservation network (`Model B`)!*
>
> **Addressing the Classic Student Objection**:
> *"Wait: in Model A, since $S \to E_t$ injects $r_t$ dirty napkins unconditionally from $S$, couldn't day $t$ send $r_t$ dirty napkins to day $t + m$ even if day $t$'s morning demand $M_t \to T$ was never satisfied?"*
> - **Answer**: In a valid maximum flow where all sink edges $M_t \to T$ (total capacity $\sum_{t=1}^D r_t$) are **saturated**, every morning $M_t$ receives exactly $r_t$ clean napkins. Moreover, because every laundry edge $E_t \to M_{t+\Delta}$ has strictly positive delay $\Delta \ge 1$, dirty napkins created on evening $t$ can only help mornings $t' > t$, which by strong induction on $t = 1, 2, \dots, D$ already had their earlier mornings $1, \dots, t$ fully supplied!

#### Step 3: The Reverse-Engineering Scratchpad (Head-to-Head Graph Compilation)

```
   [Model A: Bipartite Day/Night Split (Zero Lower Bounds)]

                  cap=r_t, cost=0                  cap=inf, cost=f (fast: +m days)
        +----------------------------> E_t (Dirty) -------------------------------+
        |                                |                                        |
        |                                | cap=inf, cost=0 (hold dirty)           |
        |                                v                                        v
      [ S ]                            E_{t+1}                                 M_{t+m} (Clean)
        |                                                                         |
        |         cap=inf, cost=p (buy fresh)                                     | cap=r_{t+m}, cost=0
        +------------------------------------------------------------------------>+-----------------> [ T ]
```

| Physical Action | Model A: Bipartite Day/Night Split (`(cap, cost)`) | Model B: Lower-Bound Spine (`([low, up], cost)`) |
| :--- | :--- | :--- |
| Daily usage of $r_t$ napkins on day $t$ | $S \to E_t$: $(r_t, 0)$ **and** $M_t \to T$: $(r_t, 0)$ | $M_t \to E_t$: $([r_t, r_t], 0)$ |
| Buy fresh clean napkins on day $t$ | $S \to M_t$: $(\infty, p)$ (or $S \to M_1$ only if $M_t \to M_{t+1}$ exists) | $S_{\text{real}} \to M_t$: $([0, \infty), p)$ |
| Store dirty napkin from day $t$ to $t+1$ | $E_t \to E_{t+1}$: $(\infty, 0)$ | $E_t \to E_{t+1}$: $([0, \infty), 0)$ |
| Store clean napkin from day $t$ to $t+1$ | $M_t \to M_{t+1}$: $(\infty, 0)$ (redundant if $E_t \to E_{t+1}$ & buy any day exist) | $M_t \to M_{t+1}$: $([0, \infty), 0)$ |
| Fast laundry ($m$ days, cost $f$) | $E_t \to M_{t+m}$: $(\infty, f)$ for $t + m \le D$ | $E_t \to M_{t+m}$: $([0, \infty), f)$ for $t + m \le D$ |
| Slow laundry ($n$ days, cost $s$) | $E_t \to M_{t+n}$: $(\infty, s)$ for $t + n \le D$ | $E_t \to M_{t+n}$: $([0, \infty), s)$ for $t + n \le D$ |
| Unused dirty napkins at end of horizon | Implicitly left unpushed at $S \to E_t$ (since $E_t$ has no forced outflow!) | $E_t \to T_{\text{real}}$: $([0, \infty), 0)$ |

> [!TIP]
> **Why Does $S \to E_t$ Not Need to Be Saturated in Model A?**
> Notice a crucial asymmetry in Model A:
> - Every morning edge $M_t \to T$ **must be saturated** (total flow into $T$ must equal $\sum_{t=1}^D r_t$), because $r_t$ clean napkins are needed on day $t$.
> - However, an evening edge $S \to E_t$ **does not need to be saturated**! If the restaurant uses $r_t$ napkins on day $t$ and simply throws $k$ of those dirty napkins into the trash at the end of day $t$ (never washing them again), those $k$ units correspond to unused capacity on $S \to E_t$! Thus, in Model A, the total max-flow from $S$ to $T$ is **exactly $\sum_{t=1}^D r_t$**: every unit entering $T$ comes either from $S \to M_t$ (a newly bought napkin) or from $S \to E_{t'} \to \dots \to M_t$ (a recycled napkin from an earlier day $t' < t$).

#### Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

**Toy Trace ($D = 3$ days, $r = [2, 3, 2]$, Buy $p = 10$, Fast $m = 1, f = 6$, Slow $n = 2, s = 3$)**:
- Total demand at $T$: $r_1 + r_2 + r_3 = 2 + 3 + 2 = 7$.
- **Day 1 ($M_1 \to T$, cap $2$)**: No laundry can arrive on Day 1. Must buy $2$ fresh napkins via $S \to M_1$ at cost $2 \times 10 = 20$.
- **Day 3 ($M_3 \to T$, cap $2$)**: Can receive slow laundry from $E_1 \to M_3$ at cost $s = 3$ per napkin! Since $S \to E_1$ has capacity $r_1 = 2$, we send $2$ units along $S \to E_1 \to M_3 \to T$ at cost $2 \times 3 = 6$.
- **Day 2 ($M_2 \to T$, cap $3$)**: Since $E_1$'s $2$ dirty napkins were already saved for Day 3's slow laundry (saving $10 - 3 = 7$ per napkin vs. $10 - 6 = 4$ on fast laundry), Day 2 buys $3$ fresh napkins via $S \to M_2$ at cost $3 \times 10 = 30$.
- Wait—can we do better by fast-washing $E_1 \to M_2$ and then fast-washing $E_2 \to M_3$?
  - Let's check! In our MCMF residual network, suppose $2$ units flow along $S \to E_1 \to M_2 \to T$ (cost $2 \times 6 = 12$) and $2$ units flow along $S \to E_2 \to M_3 \to T$ (cost $2 \times 6 = 12$). Total cost for those $4$ units is $24$.
  - Compare with sending $2$ units along $S \to E_1 \to M_3 \to T$ (cost $6$) and buying $2$ fresh on Day 2 (cost $20$), total $26$!
  - Even better: what if $E_1$ sends $2$ units to $M_3$ via slow wash (cost $6$), and on Day 2 we buy $3$ fresh (cost $30$, total $36$) vs. $E_1 \to M_2$ ($2$ fast, cost $12$) + $1$ fresh on Day 2 (cost $10$) + $E_2 \to M_3$ ($2$ fast, cost $12$), total $20 + 12 + 10 + 12 = 54$ vs $20 + 30 + 6 = 56$!
  - MCMF automatically compares the single-hop slow path $S \to E_1 \to M_3 \to T$ (cost $3$) against the two-hop fast-wash chain (saving $2 \times (10 - 6) = 8 > 10 - 3 = 7$) and selects the two-hop fast chain for optimal cost $54$!

**Broken Gadget Counterexamples**:
1. **Failure Mode 1 (Connecting $E_t \to T$ for Leftover Dirty Napkins in Model A)**:
   If a student adds disposal edges $E_t \to T$ of $(\text{cap} = \infty, \text{cost} = 0)$ in Model A, the solver will immediately send $\sum r_t$ flow along $S \to E_t \to T$ at **cost $0$**, bypassing all morning demands $M_t \to T$! In Model A, $T$ represents **only** satisfied morning demands; leftover dirty napkins are simply unpushed flow on $S \to E_t$.
2. **Failure Mode 2 (Adding $M_t \to E_t$ with Capacity $r_t$ and Cost $0$ Without Lower Bounds)**:
   If a student connects $S \xrightarrow{p} M_t \xrightarrow{r_t, 0} E_t \xrightarrow{f} M_{t+m} \to \dots \to T$, then because cost $p > 0, f > 0$, the minimum-cost flow is $f = 0$ (push nothing!), or if $T$ demands $\sum r_t$, a single napkin bought on Day 1 can only satisfy **one** edge to $T$ at the very end of its life instead of satisfying $M_1, M_{1+m}, M_{1+2m}$ along the way!

---

### 85.2 $k$-Register / $k$-Cache Interval Retention (`CF 802 C — Heidi and Library`, `POJ 3680 Intervals`, `ICPC WF 2015 Catering`)

#### Step 1: The Non-Graph Diagnostic Signal (Recognition)
A cache (or library bookshelf, or register file) can hold at most $K$ items simultaneously.
- We are given a sequence of $N$ daily requests $a_1, a_2, \dots, a_N$ ($N \le 80$ in `CF 802 C` Easy/Medium, $N \le 4000$ in Simulated MCMF variants).
- On day $t$, item $a_t$ must be present in the cache.
- If $a_t$ is not currently in the cache, we must fetch/buy it at cost $c_{a_t} > 0$ (evicting some existing item if the cache is full).
- If we keep $a_t$ in the cache from day $t$ until its next request on day $\text{next}(t) > t$, it occupies $1$ of the $K$ cache slots during the interval $[t + 1, \text{next}(t) - 1]$ (or $[t, \text{next}(t) - 1]$ depending on whether eviction happens at night), and we **save** the re-fetching cost $c_{a_t}$ on day $\text{next}(t)$!

**Why Belady's Farthest-in-Future Greedy Fails**:
When all fetching costs are uniform ($c_i = 1$), Belady's greedy algorithm (evict the item whose next appearance is farthest in the future) is optimal. When fetching costs $c_i$ are **heterogeneous**, a cheap item requested tomorrow may be better to evict than an ultra-expensive item requested 5 days from now!

#### Step 2: The Algebraic Intermediate Representation
There are two dual algebraic perspectives that compile into clean MCMF networks:

**Perspective 1 (Interval Selection / Complement Saving View — `POJ 3680` Style)**:
- If we never cache anything across days, we pay the baseline cost $\text{Base} = \sum_{t=1}^N c_{a_t}$ to buy $a_t$ on every single day $t$.
- For each occurrence $t$ of item $a_t$ that has a next occurrence $t' = \text{next}(t)$, let $x_t \in \{0, 1\}$ indicate whether we **retain** item $a_t$ in cache from the end of day $t$ to the start of day $t'$.
- Retaining $a_t$ ($x_t = 1$) saves $c_{a_t}$ (so its cost is $-c_{a_t}$), and consumes $1$ cache slot during the open time steps $s \in [t, t' - 1]$ (note: on day $t$ itself, $1$ slot is occupied by $a_t$ anyway, so at most $K - 1$ *other* items can be carried across day $t$!).
- Thus we want to minimize $\sum_t (-c_{a_t}) x_t$ subject to the interval overlap constraint:
  $$\forall s \in \{1, \dots, N\}: \quad \sum_{t \,:\, t < s < \text{next}(t)} x_t \le K - 1, \qquad x_t \in \{0, 1\}.$$

**Perspective 2 (Physical Cache-Token Trajectory View — Request Vertex Splitting)**:
- Split each day $t \in \{1, \dots, N\}$ into $t_{\text{in}}$ (start of day $t$, when $a_t$ is needed) and $t_{\text{out}}$ (end of day $t$, after $a_t$ is used).
- Exactly $1$ unit of flow must traverse $t_{\text{in}} \to t_{\text{out}}$ (representing the active item $a_t$ being read on day $t$).
- Meanwhile, the remaining $K - 1$ idle cache slots pass through day $t$ along the background timeline.

#### Step 3: The Reverse-Engineering Scratchpad (Graph Compilation)

Let us compile both perspectives side-by-side:

| Feature | Compilation 1: Timeline + Saving Chord (`POJ 3680` / Equation Diff) | Compilation 2: Split-Day Token Routing (`CF 802 C` Standard) |
| :--- | :--- | :--- |
| **Vertices** | Timeline nodes $1, 2, \dots, N$ | $S, T$, and split request nodes $t_{\text{in}}, t_{\text{out}}$ for $t \in [1, N]$ |
| **Mandatory Request Coverage** | Implicit in $\text{Base} = \sum_{t=1}^N c_{a_t}$ | $S \to t_{\text{out}}$: $(1, 0)$ and $t_{\text{in}} \to T$: $(1, 0)$ (Day/Night split!) or $t_{\text{in}} \xrightarrow{[1,1]} t_{\text{out}}$ |
| **Buy Item $a_t$ Fresh** | Paid in $\text{Base}$ when chord is not used | $S_{\text{cap } K} \to t_{\text{in}}$: $(1, c_{a_t})$ (buy into a free slot) or $s_{\text{out}} \to t_{\text{in}}$: $(1, c_{a_t})$ |
| **Carry Over Different Item** | Timeline backbone $s \to s + 1$: $(\text{cap} = K - 1, \text{cost} = 0)$ | Timeline $t_{\text{out}} \to (t+1)_{\text{out}}$: $(\infty, 0)$ and $t_{\text{out}} \to (t+1)_{\text{in}}$: $(1, c_{a_{t+1}})$ |
| **Retain Same Item $a_t$ to $t' = \text{next}(t)$** | Saving chord $(t+1) \to t'$: $(\text{cap} = 1, \text{cost} = -c_{a_t})$ (if $t' = t+1$, immediately subtract $c_{a_t}$ from $\text{Base}$!) | Zero-cost reuse chord $t_{\text{out}} \to (\text{next}(t))_{\text{in}}$: $(\text{cap} = 1, \text{cost} = 0)$ |

Let us verify **Compilation 1 (Timeline + Saving Chord)** in detail, as it has only $N$ vertices and $\le 2N$ edges!
1. Merge any adjacent identical requests $a_t = a_{t+1}$ first (keeping the item from $t$ to $t+1$ occupies $0$ intermediate days $s \in (t, t+1)$ and is always optimal at cost $0$).
2. Now every retention interval $[t, \text{next}(t)]$ has $\text{next}(t) \ge t + 2$, and occupies one of the $K - 1$ idle cache slots during days $s \in \{t + 1, \dots, \text{next}(t) - 1\}$, i.e., across the backbone edges $(t+1) \to (t+2) \to \dots \to \text{next}(t)$!
3. Send $K - 1$ units of flow from $S \to 1$ and from $N \to T$.
   - Add backbone edges $s \to s + 1$ with $(\text{cap} = K - 1, \text{cost} = 0)$ for $s = 1, \dots, N - 1$.
   - For each $t$ with $t' = \text{next}(t) \ge t + 2$, add the **retention chord** $(t + 1) \to t'$ with $(\text{cap} = 1, \text{cost} = -c_{a_t})$.
4. Every unit of flow diverted from the backbone onto the chord $(t + 1) \to t'$ reduces the available idle cache slots on edges $(t+1)\to(t+2), \dots, (t'-1)\to t'$ by $1$ and subtracts $c_{a_t}$ from $\text{Base} = \sum c_{a_t}$!

#### Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

**Toy Trace (`CF 802 C`, $N = 4$, $K = 2$ slots, sequence $a = [1, 2, 1, 2]$, costs $c_1 = 10, c_2 = 3$)**:
- Since $K = 2$, while $a_s$ is being read on day $s$, there is $K - 1 = 1$ idle slot available to hold another item across day $s$.
- Baseline cost (buy every day): $\text{Base} = 10 + 3 + 10 + 3 = 26$.
- Retention chords $(t + 1) \to \text{next}(t)$:
  - For $t = 1$ ($a_1 = 1, \text{next}(1) = 3$): chord $2 \to 3$ with $(\text{cap} = 1, \text{cost} = -10)$ (holds item $1$ in the idle slot during day $2$).
  - For $t = 2$ ($a_2 = 2, \text{next}(2) = 4$): chord $3 \to 4$ with $(\text{cap} = 1, \text{cost} = -3)$ (holds item $2$ in the idle slot during day $3$).
- With $K - 1 = 1$ unit of flow from $S \to 1$ to $4 \to T$:
  - The single unit of flow traverses $1 \to 2 \xrightarrow{\text{chord } -10} 3 \xrightarrow{\text{chord } -3} 4$!
  - Notice that chord $2 \to 3$ and chord $3 \to 4$ are **interior-disjoint** on the backbone: on day 2, item 2 is read while item 1 sits in the idle slot; on day 3, item 1 is read while item 2 sits in the idle slot!
  - Total cost: $\text{Base} + (-10 - 3) = 26 - 13 = 13$ (buy item 1 on day 1 and item 2 on day 2; never buy again!).

**Broken Gadget Counterexample (Wrong Chord Endpoints $t \to \text{next}(t)$ instead of $(t+1) \to \text{next}(t)$)**:
Suppose a student adds the retention chord from $t \to \text{next}(t)$ instead of $(t+1) \to \text{next}(t)$ on a backbone of capacity $K - 1$.
- *What breaks*: In our trace above ($K = 2$, so $K - 1 = 1$), chords $1 \to 3$ and $2 \to 4$ **overlap** on the edge $2 \to 3$, so a capacity-$1$ flow cannot take both chords! The student's graph would falsely claim that $K = 2$ slots cannot hold $\{1, 2\}$ across $[1, 2, 1, 2]$! Why? Because on day $t$, item $a_t$ is the *active* item (already accounted for by reducing $K$ to $K - 1$), so it only consumes an *idle* slot on days $s \in [t + 1, \text{next}(t) - 1]$, which corresponds to the backbone path from $t + 1$ to $\text{next}(t)$! (Equivalently, if you use chord $t \to \text{next}(t)$, the backbone capacity must be $K$ and every day $t \to t+1$ must have $1$ unit occupied by the active request.)

---

## Iteration 86: 2D Prefix/Suffix Coordinate Rank Translation — Independent Deep Dive into `AGC 031 E — Snuke the Phantom Thief`

### 86.1 Problem Statement & Step 1: The Non-Graph Diagnostic Signal

**Problem (`AtCoder Grand Contest 031 E — Snuke the Phantom Thief`)**:
There are $N$ jewels in the 2D plane ($N \le 80$). Jewel $i$ sits at integer coordinates $(x_i, y_i)$ ($1 \le x_i, y_i \le 100$) and has value $v_i \ge 1$ ($v_i \le 10^{15}$).
Snuke wants to steal a subset of jewels maximizing the sum of their values, subject to $M$ ($M \le 320$) security constraints of four types:
- `L(a, b)`: Among the stolen jewels, at most $b$ jewels have $x_i \le a$.
- `R(a, b)`: Among the stolen jewels, at most $b$ jewels have $x_i \ge a$.
- `D(a, b)`: Among the stolen jewels, at most $b$ jewels have $y_i \le a$.
- `U(a, b)`: Among the stolen jewels, at most $b$ jewels have $y_i \ge a$.

#### Step 1: The Non-Graph Diagnostic Signal (Recognition)
1. **Scale Clues**: $N \le 80$ and $M \le 320$. Whenever $N \le 80$ and weights are up to $10^{15}$, we have enough budget to run an $O(N^3)$ or $O(N^4)$ algorithm **up to $N$ times** (e.g., fixing an integer parameter $K \in \{1, \dots, N\}$ and running MCMF for each $K$).
2. **Why Standard DP and 1D Flow Fail**:
   - The constraints `L` and `R` act on $x$-coordinates, while `D` and `U` act on $y$-coordinates. A jewel $(x_i, y_i)$ simultaneously consumes quota in both $X$-constraints and $Y$-constraints, forming a **bipartite $X$-to-$Y$ coupling**.
   - However, unlike a simple degree-bounded bipartite graph, `L(a, b)` bounds the **prefix sum** $\sum_{x_i \le a} z_i \le b$, while `R(a, b)` bounds the **suffix sum** $\sum_{x_i \ge a} z_i \le b$ simultaneously! In a naive flow network over coordinates, prefix and suffix capacity bounds point in opposite directions and cannot both be represented as simple tree cuts without knowing the **total number of stolen jewels $K = \sum_{i=1}^N z_i$**!
3. **The Pivotal Insight**: Once we fix the **exact total number of stolen jewels $K \in \{1, \dots, N\}$**, a suffix constraint "at most $b$ stolen jewels have $x_i \ge a$" becomes a prefix constraint "at least $K - b$ stolen jewels have $x_i \le a - 1$"! And any prefix cardinality constraint on a set of $K$ numbers is equivalent to a **coordinate bound on the $p$-th smallest chosen number (the $p$-th order statistic)**!

---

### 86.2 Step 2: The Algebraic / Order-Statistic Intermediate Representation

Fix the total number of stolen jewels $K \in \{1, 2, \dots, N\}$.
Suppose we steal $K$ jewels, and let:
- $x_{(1)} \le x_{(2)} \le \dots \le x_{(K)}$ be their $x$-coordinates sorted in non-decreasing order,
- $y_{(1)} \le y_{(2)} \le \dots \le y_{(K)}$ be their $y$-coordinates sorted in non-decreasing order.

Now translate each of the four constraint types into an **exact point-wise inequality** on the order statistics $x_{(p)}$ and $y_{(q)}$:

**Lemma 86.1 (Prefix/Suffix Cardinality $\leftrightarrow$ Order-Statistic Duality)**:
*For any sorted sequence of $K$ integers $x_{(1)} \le x_{(2)} \le \dots \le x_{(K)}$:*
1. **Left Prefix Constraint `L(a, b)`**:
   $$\text{``At most } b \text{ elements satisfy } x \le a\text{''} \iff \begin{cases} \text{Always true} & \text{if } b \ge K, \\ x_{(b+1)} \ge a + 1 & \text{if } 0 \le b < K. \end{cases}$$
   *Proof*: In a sorted array, having $\le b$ elements with value $\le a$ holds if and only if the $(b+1)$-th element is strictly greater than $a$, i.e., $x_{(b+1)} \ge a + 1$.
2. **Right Suffix Constraint `R(a, b)`**:
   $$\text{``At most } b \text{ elements satisfy } x \ge a\text{''} \iff \begin{cases} \text{Always true} & \text{if } b \ge K, \\ x_{(K-b)} \le a - 1 & \text{if } 0 \le b < K. \end{cases}$$
   *Proof*: Among $K$ elements, having at most $b$ elements with $x \ge a$ is equivalent to having at least $K - b$ elements with $x \le a - 1$. In a sorted array, having at least $K - b$ elements $\le a - 1$ holds if and only if the $(K - b)$-th element satisfies $x_{(K-b)} \le a - 1$.
3. **Down / Up Constraints `D(a, b)` and `U(a, b)`**:
   By identical logic on $y_{(1)} \le \dots \le y_{(K)}$:
   $$\text{D}(a, b) \iff y_{(b+1)} \ge a + 1 \quad (b < K), \qquad \text{U}(a, b) \iff y_{(K-b)} \le a - 1 \quad (b < K). \quad \blacksquare$$

**Propagating Monotonicity Across Rank Slots $p \in \{1, \dots, K\}$**:
For each rank $p \in \{1, \dots, K\}$, collecting all `L` constraints with $b + 1 = p$ gives a lower bound $x_{(p)} \ge \max (a + 1)$, and collecting all `R` constraints with $K - b = p$ gives an upper bound $x_{(p)} \le \min (a - 1)$.
Furthermore, because $x_{(1)} \le x_{(2)} \le \dots \le x_{(K)}$, any lower bound on $x_{(p-1)}$ is also a valid lower bound on $x_{(p)}$, and any upper bound on $x_{(p+1)}$ is also a valid upper bound on $x_{(p)}$!
Define the **monotonized interval bounds** $[L_X(p), R_X(p)]$ for $p = 1, \dots, K$:
$$L_X(p) := \max\left( L_X(p-1), \; \max_{\text{L}(a, b) \,:\, b + 1 = p} (a + 1) \right) \quad (\text{with } L_X(0) = -\infty),$$
$$R_X(p) := \min\left( R_X(p+1), \; \min_{\text{R}(a, b) \,:\, K - b = p} (a - 1) \right) \quad (\text{with } R_X(K+1) = +\infty),$$
and analogously $[L_Y(q), R_Y(q)]$ for $q = 1, \dots, K$.
Note that by construction, both endpoints are **monotonically non-decreasing** in the rank index:
$$L_X(1) \le L_X(2) \le \dots \le L_X(K), \qquad R_X(1) \le R_X(2) \le \dots \le R_X(K).$$

Now comes the crucial question that separates a rigorous proof from hand-waving:
> **In a flow graph, if we match $K$ chosen jewels to $X$-slots $1, \dots, K$ via some arbitrary bijection $\pi$ (requiring $x_{\pi(p)} \in [L_X(p), R_X(p)]$) without explicitly adding constraints $x_{\pi(1)} \le x_{\pi(2)} \le \dots \le x_{\pi(K)}$, how do we know the flow won't assign jewels to slots out of sorted order?**

**Theorem 86.2 (The Monotone Interval Uncrossing Theorem)**:
*Suppose $[L_X(p), R_X(p)]$ satisfies $L_X(1) \le \dots \le L_X(K)$ and $R_X(1) \le \dots \le R_X(K)$. Let $S = \{j_1, \dots, j_K\}$ be any subset of $K$ jewels. Then $S$ can be matched to slots $1, \dots, K$ via **some** bijection $\pi$ satisfying $x_{\pi(p)} \in [L_X(p), R_X(p)]$ for all $p$ **if and only if** the sorted order $x_{(1)} \le x_{(2)} \le \dots \le x_{(K)}$ of $S$ satisfies $x_{(p)} \in [L_X(p), R_X(p)]$ for all $p$!*

*Proof*:
$(\Leftarrow)$ Immediate by taking $\pi$ to be the sorting permutation.
$(\Rightarrow)$ Suppose $\pi$ is a valid matching with $x_{\pi(p)} \in [L_X(p), R_X(p)]$ for all $p$, and suppose $\pi$ has an inversion: there exist $p_1 < p_2$ such that $x_{\pi(p_1)} > x_{\pi(p_2)}$.
Let $u = x_{\pi(p_2)}$ and $v = x_{\pi(p_1)}$, so $u < v$. By assumption:
- $v \in [L_X(p_1), R_X(p_1)] \implies L_X(p_1) \le v \le R_X(p_1)$,
- $u \in [L_X(p_2), R_X(p_2)] \implies L_X(p_2) \le u \le R_X(p_2)$.
Now use $u < v$ and the monotonicity $L_X(p_1) \le L_X(p_2)$ and $R_X(p_1) \le R_X(p_2)$:
- For $u$ in slot $p_1$: $L_X(p_1) \le L_X(p_2) \le u < v \le R_X(p_1) \implies u \in [L_X(p_1), R_X(p_1)]$!
- For $v$ in slot $p_2$: $L_X(p_2) \le u < v \le R_X(p_1) \le R_X(p_2) \implies v \in [L_X(p_2), R_X(p_2)]$!
Thus swapping $\pi(p_1)$ and $\pi(p_2)$ preserves feasibility while strictly reducing the number of inversions! Repeating until zero inversions remain yields the sorted sequence $x_{(1)} \le \dots \le x_{(K)}$ without ever changing the chosen subset $S$ of jewels or its total value! $\blacksquare$

---

### 86.3 Step 3: The Reverse-Engineering Scratchpad (4-Layer MCMF Compilation)

Thanks to Theorem 86.2, for a fixed $K \in \{1, \dots, N\}$, a subset $S$ of $K$ jewels is valid if and only if $S$ can be simultaneously matched to the $X$-rank slots $\{1, \dots, K\}$ and to the $Y$-rank slots $\{1, \dots, K\}$!

```
          (1, 0)              (1, 0) if x_i in [L_X(p), R_X(p)]          (1, -v_i)             (1, 0) if y_i in [L_Y(q), R_Y(q)]            (1, 0)
  [ S ] ---------> X-slot p -----------------------------------> J_in(i) ---------> J_out(i) -----------------------------------> Y-slot q ---------> [ T ]
       (p = 1..K)                                                                                                              (q = 1..K)
```

| Layer / Transition | Directed Edge | Capacity | Cost | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Source to $X$-Rank Slots** | $S \to X_p$ for $p \in \{1, \dots, K\}$ | $1$ | $0$ | Forces each of the $K$ sorted $X$-ranks to be filled by $1$ jewel |
| **$X$-Rank Compatibility** | $X_p \to J_{\text{in}}(i)$ if $L_X(p) \le x_i \le R_X(p)$ | $1$ | $0$ | Jewel $i$ can serve as the $p$-th stolen jewel in $X$-order |
| **Jewel Selection & Value** | $J_{\text{in}}(i) \to J_{\text{out}}(i)$ for $i \in \{1, \dots, N\}$ | $1$ | $-v_i$ | Ensures jewel $i$ is stolen at most once and collects value $v_i$ |
| **$Y$-Rank Compatibility** | $J_{\text{out}}(i) \to Y_q$ if $L_Y(q) \le y_i \le R_Y(q)$ | $1$ | $0$ | Jewel $i$ can serve as the $q$-th stolen jewel in $Y$-order |
| **$Y$-Rank Slots to Sink** | $Y_q \to T$ for $q \in \{1, \dots, K\}$ | $1$ | $0$ | Forces each of the $K$ sorted $Y$-ranks to be filled by $1$ jewel |

**Complexity Analysis**:
- For a fixed $K \in \{1, \dots, N\}$:
  - First check if $L_X(p) > R_X(p)$ or $L_Y(p) > R_Y(p)$ for any $p$; if so, $K$ is immediately infeasible.
  - Otherwise, the network has $V = 2K + 2N + 2 \le 322$ vertices and $E \le 2K + N + 2KN \le 13{,}040$ edges.
  - Pushing $K$ units of flow via SSP (using DAG topological DP for initial potentials $\pi$ in $O(E)$ time, followed by $K$ runs of $O(V^2 + E)$ dense Dijkstra) takes $O(K(V^2 + E)) \approx 80 \times 1.3 \times 10^4 \approx 10^6$ operations per $K$.
- Summing over all $K \in \{1, \dots, N\}$ takes $< 8 \times 10^7$ simple operations, running in $\approx 0.15$ seconds!

---

### 86.4 Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

**Toy Trace ($N = 3$ jewels, $K = 2$ stolen jewels)**:
Suppose the $3$ jewels are:
- Jewel 1: $(x_1, y_1) = (2, 8)$, value $v_1 = 100$,
- Jewel 2: $(x_2, y_2) = (5, 3)$, value $v_2 = 80$,
- Jewel 3: $(x_3, y_3) = (9, 9)$, value $v_3 = 90$.
Constraints for $K = 2$:
- `L(4, 1)`: At most $1$ jewel has $x \le 4 \implies x_{(2)} \ge 5$.
- `R(6, 0)`: At most $0$ jewels have $x \ge 6 \implies x_{(2)} \le 5$.
- `D(5, 0)`: At most $0$ jewels have $y \le 5 \implies y_{(1)} \ge 6$.
1. **Compute Intervals for $K = 2$**:
   - $X$-slots: $[L_X(1), R_X(1)] = [1, 5]$, $[L_X(2), R_X(2)] = [5, 5]$.
   - $Y$-slots: $[L_Y(1), R_Y(1)] = [6, 100]$, $[L_Y(2), R_Y(2)] = [6, 100]$.
2. **Compatibility Edges**:
   - $X_1 \in [1, 5]$ matches Jewel 1 ($x_1 = 2$) and Jewel 2 ($x_2 = 5$).
   - $X_2 \in [5, 5]$ matches **only** Jewel 2 ($x_2 = 5$). (Jewel 3 has $x_3 = 9 > 5$, excluded!)
   - $Y_1, Y_2 \in [6, 100]$ match Jewel 1 ($y_1 = 8$) and Jewel 3 ($y_3 = 9$), **excluding Jewel 2** ($y_2 = 3 < 6$)!
3. **MCMF Augmentation**:
   - $X_2$ can only reach $J_{\text{in}}(2)$, but $J_{\text{out}}(2)$ has **zero outgoing edges** to $Y_1$ or $Y_2$!
   - Thus maximum flow is $1 < K = 2$, correctly reporting that $K = 2$ is **infeasible**! (Whereas for $K = 1$, `L(4, 1)` is vacuous since $b = 1 \ge K$, `R(6, 0)` gives $x_{(1)} \le 5$, `D(5, 0)` gives $y_{(1)} \ge 6$, allowing Jewel 1 $(2, 8)$ to be stolen for value $100$!)

**Broken Gadget Counterexamples**:
1. **Failure Mode 1 (Omitting Jewel Vertex Splitting $J_{\text{in}}(i) \to J_{\text{out}}(i)$)**:
   If Jewel $i$ is a single unsplit vertex $J(i)$ with incoming capacity-$1$ edges from $X_1, \dots, X_K$ and outgoing capacity-$1$ edges to $Y_1, \dots, Y_K$, then up to $K$ units of flow could pass through the **same** jewel $J(i)$ (stealing Jewel $i$ $K$ times)! The internal bridge $J_{\text{in}}(i) \to J_{\text{out}}(i)$ of capacity $1$ is mandatory to enforce that each jewel is stolen at most once.
2. **Failure Mode 2 (Accepting Flow $< K$ When Evaluating Fixed $K$)**:
   Because the translation `R(a, b)` $\iff x_{(K-b)} \le a - 1$ explicitly depends on the total number of stolen jewels being **exactly $K$**, if the maximum flow for a given $K$ is strictly less than $K$, you **must discard** that run—its flow of size $f < K$ was constrained by intervals $[L_X(p), R_X(p)]$ computed under the false premise that $K$ jewels were stolen!

---

## Iteration 87: Linearizing Manhattan & Chebyshev Distances via Sign-Combination Hubs — Independent Deep Dive into `AGC 034 D — Manhattan Max Matching`

### 87.1 Problem Statement & Step 1: The Non-Graph / Geometric Diagnostic Signal

**Problem (`AtCoder Grand Contest 034 D — Manhattan Max Matching`)**:
In the 2D plane, you are given $N$ groups of Red points and $N$ groups of Blue points ($1 \le N \le 1000$).
- Red group $i$ consists of $RC_i$ identical points at $(RX_i, RY_i)$.
- Blue group $j$ consists of $BC_j$ identical points at $(BX_j, BY_j)$.
- It is guaranteed that $\sum_{i=1}^N RC_i = \sum_{j=1}^N BC_j =: F \le 10^4$, and $0 \le RX_i, RY_i, BX_j, BY_j \le 10^9$.
Pair every Red point with a Blue point (one-to-one) to **maximize** the sum of Manhattan distances:
$$\sum_{\text{matched } (i, j)} \big(|RX_i - BX_j| + |RY_i - BY_j|\big).$$

#### Step 1: The Non-Graph Diagnostic Signal (Recognition)
1. **Scale Clues**: $N \le 1000$ groups and total flow volume $F = \sum RC_i \le 10^4$.
   - A naive bipartite MCMF graph has $2N = 2000$ vertices and $N^2 = 10^6$ edges. Running $F \le 10^4$ shortest-path augmentations on $10^6$ edges requires $\sim 10^{10}$ operations—an immediate TLE!
   - Yet $F \le 10^4$ and $N \le 1000$ *would* easily pass MCMF if the number of edges could be compressed from $O(N^2)$ to $O(N)$!
2. **Why Greedy Sorting Fails in 2D**:
   - In 1D, maximizing $\sum |RX_i - BX_j|$ is solved in $O(N \log N)$ by sorting all points or matching the smallest values with the largest values.
   - In 2D, $|RX_i - BX_j| + |RY_i - BY_j|$ has **four possible sign regimes** depending on whether $RX_i \ge BX_j$ or $RX_i < BX_j$, and whether $RY_i \ge BY_j$ or $RY_i < BY_j$. A Red point cannot greedily commit to a quadrant without knowing the global supply of Blue points in all four quadrants.

---

### 87.2 Step 2: The Algebraic / Dual-Norm Intermediate Representation

How do we eliminate the absolute value bars $|RX_i - BX_j| + |RY_i - BY_j|$ and decouple $i$ from $j$?
Recall the fundamental dual-norm identity for $\ell_1$: for any real number $a \in \mathbb{R}$, $|a| = \max(a, -a) = \max_{s \in \{+1, -1\}} (s \cdot a)$. Applying this independently to $\Delta x = RX_i - BX_j$ and $\Delta y = RY_i - BY_j$:

$$|RX_i - BX_j| + |RY_i - BY_j| = \max_{s_x \in \{+1, -1\}} s_x(RX_i - BX_j) + \max_{s_y \in \{+1, -1\}} s_y(RY_i - BY_j)$$
$$= \max_{(s_x, s_y) \in \{+1, -1\}^2} \Big( \underbrace{(s_x RX_i + s_y RY_i)}_{\text{depends ONLY on Red } i} + \underbrace{(-s_x BX_j - s_y BY_j)}_{\text{depends ONLY on Blue } j} \Big).$$

Look closely at what just happened inside the $\max_{(s_x, s_y) \in \{\pm 1\}^2}$:
For each of the **4 fixed sign pairs** $(s_x, s_y) \in \{(+1, +1), (+1, -1), (-1, +1), (-1, -1)\}$, the cross-term between $i$ and $j$ has **completely factored into a sum of a Red-only weight and a Blue-only weight**!

Now substitute this identity into the global **Max-Weight Matching** objective:
$$\max_{\text{flow } f} \sum_{i=1}^N \sum_{j=1}^N f_{i,j} \big(|RX_i - BX_j| + |RY_i - BY_j|\big)$$
$$= \max_{\text{flow } f} \sum_{i=1}^N \sum_{j=1}^N f_{i,j} \max_{s \in \{\pm 1\}^2} \Big( \phi_s(i) + \psi_s(j) \Big),$$
where $\phi_s(i) := s_x RX_i + s_y RY_i$ and $\psi_s(j) := -s_x BX_j - s_y BY_j$.

**Theorem 87.1 (Why $\max$ Over Matchings and $\max$ Over Sign Hubs Commute)**:
*Decompose each matched flow variable $f_{i,j} = \sum_{s \in \{\pm 1\}^2} f_{i, s, j}$, where $f_{i, s, j} \ge 0$ is the number of pairs between Red group $i$ and Blue group $j$ assigned the sign pair $s = (s_x, s_y)$. Then:*
$$\max_{\text{flow } f_{i,j}} \sum_{i,j} f_{i,j} \big(|RX_i - BX_j| + |RY_i - BY_j|\big) = \max_{\text{flow } f_{i, s, j}} \sum_{s \in \{\pm 1\}^2} \left( \sum_{i=1}^N \phi_s(i) \sum_j f_{i,s,j} + \sum_{j=1}^N \psi_s(j) \sum_i f_{i,s,j} \right).$$
*Proof*:
1. $(\le)$ For any choice of $s \in \{\pm 1\}^2$, $\phi_s(i) + \psi_s(j) = s_x(RX_i - BX_j) + s_y(RY_i - BY_j) \le |RX_i - BX_j| + |RY_i - BY_j|$. Thus choosing a suboptimal sign pair $s$ can never overestimate the true Manhattan distance.
2. $(\ge)$ Conversely, for any pair $(i, j)$, choosing $s_x^* = \text{sgn}(RX_i - BX_j)$ and $s_y^* = \text{sgn}(RY_i - BY_j)$ achieves exact equality $\phi_{s^*}(i) + \psi_{s^*}(j) = |RX_i - BX_j| + |RY_i - BY_j|$. Since the outer problem is **maximization**, any optimal flow $f^*_{i, s, j}$ will automatically route every unit of flow between $i$ and $j$ through an optimal sign hub $s^*$! $\blacksquare$

---

### 87.3 Step 3: The Reverse-Engineering Scratchpad (4-Hub Graph Compilation & Generalizations)

In Theorem 87.1, notice that the index $j$ disappears from the Red sum $\sum_j f_{i, s, j} =: f(R_i \to H_s)$, and the index $i$ disappears from the Blue sum $\sum_i f_{i, s, j} =: f(H_s \to B_j)$!
By flow conservation at each of the **4 Sign-Combination Hubs** $H_{++}, H_{+-}, H_{-+}, H_{--}$:
$$\forall s \in \{+1, -1\}^2: \quad \sum_{i=1}^N f(R_i \to H_s) = \sum_{j=1}^N f(H_s \to B_j).$$

This compiles directly into a 3-layer MCMF network with **only $4$ hub vertices** between $R_1, \dots, R_N$ and $B_1, \dots, B_N$!
To convert **Max-Cost** Max-Flow into standard **Min-Cost** Max-Flow, we negate all edge costs:

```
                  (RC_i, 0)                      (inf, -s_x RX_i - s_y RY_i)                      (inf, +s_x BX_j + s_y BY_j)                      (BC_j, 0)
        +-------------------------> R_i (Red i) -----------------------------> H_{s_x, s_y} -----------------------------> B_j (Blue j) -------------------------+
        |                           (i = 1..N)                                (4 Sign Hubs)                                (j = 1..N)                            |
      [ S ]                                                                    H_++, H_+-                                                                      [ T ]
                                                                               H_-+, H_--
```

| Layer | Directed Edge | Capacity | Cost (for Min-Cost Max-Flow) | Count of Edges |
| :--- | :--- | :--- | :--- | :--- |
| **Source to Red Groups** | $S \to R_i$ | $RC_i$ | $0$ | $N$ |
| **Red Groups to 4 Sign Hubs** | $R_i \to H_{s_x, s_y}$ for $(s_x, s_y) \in \{\pm 1\}^2$ | $\infty$ | $-s_x RX_i - s_y RY_i$ | $4N$ |
| **4 Sign Hubs to Blue Groups** | $H_{s_x, s_y} \to B_j$ for $(s_x, s_y) \in \{\pm 1\}^2$ | $\infty$ | $+s_x BX_j + s_y BY_j$ | $4N$ |
| **Blue Groups to Sink** | $B_j \to T$ | $BC_j$ | $0$ | $N$ |

**Complexity & Zero-SPFA Potential Initialization**:
- Total vertices: $V = 2N + 6 \le 2006$. Total edges: $E = 10N \le 10{,}000$ (compressed from $N^2 = 10^6$ by **$100\times$**!).
- Because the initial network is a **4-layer DAG** ($S \to R \to H \to B \to T$), we can compute initial Johnson potentials $\pi(v)$ in $O(N)$ time by simple 4-layer DP (without running SPFA even once!):
  $$\pi(S) = 0, \qquad \pi(R_i) = 0, \qquad \pi(H_s) = \min_{i=1}^N (-s_x RX_i - s_y RY_i),$$
  $$\pi(B_j) = \min_{s \in \{\pm 1\}^2} \big(\pi(H_s) + s_x BX_j + s_y BY_j\big), \qquad \pi(T) = \min_{j=1}^N \pi(B_j).$$
- Alternatively, shifting all coordinates by $+C$ or adding a constant to each edge cost does not affect reduced costs once $\pi$ is initialized via the DAG DP above!

#### Generalizations to $\ell_1^d$ and $\ell_\infty^d$ (Chebyshev Distance)

| Distance Metric (Maximization) | Dual-Norm Linearization Formula | Number of Hubs | Hub Edge Costs ($R_i \to H$ and $H \to B_j$) |
| :--- | :--- | :--- | :--- |
| **2D Manhattan ($\ell_1^2$)**<br>$\|x_1 - x_2\| + \|y_1 - y_2\|$ | $\max_{s_x, s_y \in \{\pm 1\}} \big((s_x x_1 + s_y y_1) + (-s_x x_2 - s_y y_2)\big)$ | **$4$ hubs**<br>($2^2 = 4$) | $R_i \to H_{s_x, s_y}$: cost $-(s_x x_i + s_y y_i)$<br>$H_{s_x, s_y} \to B_j$: cost $+(s_x x_j + s_y y_j)$ |
| **$d$-D Manhattan ($\ell_1^d$)**<br>$\sum_{k=1}^d \|p_{i,k} - q_{j,k}\|$ | $\max_{s \in \{\pm 1\}^d} \big(\sum_{k=1}^d s_k p_{i,k} + \sum_{k=1}^d (-s_k) q_{j,k}\big)$ | **$2^d$ hubs** | $R_i \to H_s$: cost $-\sum_{k=1}^d s_k p_{i,k}$<br>$H_s \to B_j$: cost $+\sum_{k=1}^d s_k q_{j,k}$ |
| **$d$-D Chebyshev ($\ell_\infty^d$)**<br>$\max_{k=1}^d \|p_{i,k} - q_{j,k}\|$ | $\max_{k \in [1, d], \, s \in \{\pm 1\}} \big( s \cdot p_{i,k} + (-s) \cdot q_{j,k} \big)$ | **Only $2d$ hubs!**<br>(4 hubs in 2D) | For each axis $k \in [1, d]$ and sign $s \in \{\pm 1\}$:<br>$R_i \to H_{k, s}$: cost $-s \cdot p_{i,k}$<br>$H_{k, s} \to B_j$: cost $+s \cdot q_{j,k}$ |

> [!TIP]
> **Notice Why $d$-Dimensional Chebyshev ($\ell_\infty^d$) Uses Only $2d$ Hubs Instead of $2^d$ Hubs!**
> In $\ell_1^d$, the sum of $d$ absolute values expands into a maximum over $2^d$ sign combinations. In $\ell_\infty^d$, by contrast, $\max_{k=1}^d |p_{i,k} - q_{j,k}| = \max_{k=1}^d \max_{s \in \{\pm 1\}} s(p_{i,k} - q_{j,k})$ is already a maximum over **$2d$ single-coordinate terms**! Thus even for $d = 50$ dimensions, Maximum $\ell_\infty^d$ Bipartite Matching requires only $2d = 100$ hubs!

---

### 87.4 Step 4: Hand-Checkable Toy Trace & Proof of Why Minimizing Manhattan Distance CANNOT Use the 4-Hub Trick

**Toy Trace ($N = 1$ Red point $R_1 = (1, 5)$ and $N = 1$ Blue point $B_1 = (4, 2)$)**:
True Manhattan distance is $|1 - 4| + |5 - 2| = 3 + 3 = 6$.
Let us evaluate the negated cost of routing $1$ unit of flow from $R_1(1, 5)$ to $B_1(4, 2)$ through each of the 4 hubs $H_{s_x, s_y}$, where $\text{Cost}(R_1 \to H_{s_x, s_y} \to B_1) = -s_x(1 - 4) - s_y(5 - 2) = 3 s_x - 3 s_y$:
- Via $H_{++}$ ($s_x = +1, s_y = +1$): cost $= 3(1) - 3(1) = 0$ (represents $+(1-4) + (5-2) = 0$).
- Via $H_{+-}$ ($s_x = +1, s_y = -1$): cost $= 3(1) - 3(-1) = +6$ (represents $+(1-4) - (5-2) = -6$).
- Via $H_{-+}$ ($s_x = -1, s_y = +1$): cost $= 3(-1) - 3(1) = -6$ (represents $-(1-4) + (5-2) = +6$).
- Via $H_{--}$ ($s_x = -1, s_y = -1$): cost $= 3(-1) - 3(-1) = 0$ (represents $-(1-4) - (5-2) = 0$).
When we run **Min-Cost** Max-Flow on these negated costs, the shortest path picks $H_{-+}$ with cost $-6$, yielding Maximum Manhattan Distance $-(-6) = +6$!

> [!CAUTION]
> **Why Minimizing Manhattan Distance ($\min \sum |x_1 - x_2| + |y_1 - y_2|$) Fails Catastrophically on the 4-Hub Gadget!**
> Suppose a problem asks for the **Minimum-Weight** Manhattan Bipartite Matching:
> $$\min_{\text{matching } M} \sum_{(i, j) \in M} \big(|RX_i - BX_j| + |RY_i - BY_j|\big).$$
> A student tries to build the exact same 4-hub network *without* negating the edge costs: setting $\text{Cost}(R_i \to H_{s_x, s_y}) = +s_x RX_i + s_y RY_i$ and $\text{Cost}(H_{s_x, s_y} \to B_j) = -s_x BX_j - s_y BY_j$, so that path $R_i \to H_{s_x, s_y} \to B_j$ has cost $s_x(RX_i - BX_j) + s_y(RY_i - BY_j)$.
>
> **What Happens When You Run Min-Cost Max-Flow on That Graph?**
> Look at our Toy Trace above with $R_1 = (1, 5)$ and $B_1 = (4, 2)$:
> - The 4 hubs offer costs $\{0, -6, +6, 0\}$.
> - Because **Min-Cost** Max-Flow **minimizes** over all paths, it does **not** pick the hub $H_{-+}$ of cost $+6 = |1-4| + |5-2|$; instead, it greedily picks the hub $H_{+-}$ of cost **$-6 = -(|1-4| + |5-2|)$**!
> - Algebraically, because $|a| = \max_{s \in \{\pm 1\}} (s \cdot a)$, the Minimum Manhattan Matching problem is a **Min–Max saddle problem**:
>   $$\min_{\text{matching } M} \sum_{(i, j) \in M} \max_{s \in \{\pm 1\}^2} \big(s_x(RX_i - BX_j) + s_y(RY_i - BY_j)\big).$$
>   Replacing the inner $\max_s$ with a free routing choice in a **Min**-Cost Flow network turns $\min_M \max_s$ into $\min_M \min_s$:
>   $$\min_{s \in \{\pm 1\}^2} \big(s_x(RX_i - BX_j) + s_y(RY_i - BY_j)\big) = -\big(|RX_i - BX_j| + |RY_i - BY_j|\big)!$$
>   Thus, running Min-Cost Flow on the 4-hub network with un-negated costs **still computes the Maximum Manhattan Matching** (with a minus sign), and **never** the Minimum Manhattan Matching!
> - **Deep Geometric Reason**: The function $d(p, q) = \|p - q\|_1$ is a supremum ($\max$) of affine functions, not an infimum ($\min$) of affine functions. In a minimization flow network, parallel paths through hubs take the **point-wise minimum** ($\min_h (\text{cost}(u, h) + \text{cost}(h, v))$), so hubs can only represent functions expressible as a $\min$ of separable terms (or equivalently, $\max$ in a maximization problem)!

---

## Master Recognition & Compilation Decision Table (Wave 4A: Iterations 83–87)

| Modelling Archetype | Surface Signal in Problem Statement | Algebraic Intermediate Form | Canonical Graph Gadget | Fatal Trap / Broken Gadget |
| :--- | :--- | :--- | :--- | :--- |
| **Collect-Once $k$-Walks**<br>(`方格取数`, `POJ 3422`) | $k$ walks on grid/DAG; cell reward $w_v \ge 0$ collected **at most once** | Marginal cost $\Delta C_v(1) = -w_v$, $\Delta C_v(r) = 0$ ($r \ge 2$) | Split $v_{\text{in}} \to v_{\text{out}}$ into parallel arcs $(1, -w_v) \parallel (k-1, 0)$ | Putting $(1, -w_v)$ on incoming edges double-counts $w_v$; fails if $w_v < 0$ (concave cost) |
| **DAG $K$-Path / Cycle Cover**<br>(`星际竞速`, `营救皮卡丘`) | Cover all $N$ vertices with $\le K$ paths/vehicles minimizing transition cost | $\text{Paths} = N - \sum x_{u,v}$; slack $s_v = 1 - \sum_u x_{u,v}$ is path start | Bipartite $u_{\text{out}} \to v_{\text{in}}$ + starter hub $S \xrightarrow{K} H_{\text{start}} \to v_{\text{in}}$; demand $1$ at $v_{\text{in}} \to T$ | Running on non-DAG allows cheap disconnected cycles to masquerade as path merges! |
| **Chinese Postman (CPP)**<br>(Directed / Undirected / Mixed) | Traverse **every edge** $\ge 1$ times and return to start at min cost | Directed: $\sum_{e \in \delta^+} x_e - \sum_{e \in \delta^-} x_e = d_{\text{in}} - d_{\text{out}}$<br>Undirected: $T$-join on odd-degree vertices | Directed: MCMF with $b(v) = d_{\text{in}}(v) - d_{\text{out}}(v)$<br>Undirected: Min-Weight Perfect Matching on $K_{|O|}$ | Weighted Mixed CPP with edge duplication is **NP-hard** (parity vs. unit flow mismatch) |
| **Dynamic Lazy Scheduling**<br>(`修车`, `[NOI2012] 美食节`) | $P$ jobs on $M$ heterogeneous machines; minimize **sum of completion times** | Backward index $r = 1 \dots k_j$ from end: cost is $r \cdot t_{i,j}$ | Spawn slot $(j^*, r+1)$ **lazily** only after $(j^*, r) \to T$ saturates ($V = O(N+M+P)$) | Forward index depends on unknown $k_j$; static graph has $O(NMP)$ edges and TLEs |
| **Resource Reuse / Napkin Plan**<br>(`餐巾计划问题`) | Daily demand $r_t$; used items become dirty and return after $m$ or $n$ days | Lower-bound spine $M_t \xrightarrow{[r_t, r_t]} E_t$ $\equiv$ Day/Night split | $S \xrightarrow{r_t, 0} E_t$ (dirty) and $M_t \xrightarrow{r_t, 0} T$ (clean); laundry $E_t \to M_{t+\Delta}$ | Adding disposal edge $E_t \to T$ in Day/Night split lets flow bypass all morning demands! |
| **$k$-Cache Interval Retention**<br>(`CF 802 C`, `POJ 3680`) | Cache holds $K$ items; keeping $a_t$ until $\text{next}(t)$ saves $c_{a_t}$ | $\sum_{t < s < \text{next}(t)} x_t \le K - 1$ maximizing $\sum c_{a_t} x_t$ | Backbone $s \to s+1$ of cap $K-1$, cost $0$; saving chord $(t+1) \to \text{next}(t)$ of $(1, -c_{a_t})$ | Using chord $t \to \text{next}(t)$ instead of $(t+1) \to \text{next}(t)$ falsely charges an extra slot on day $t$ |
| **2D Prefix/Suffix Rank Slots**<br>(`AGC 031 E`) | Subset of points with "$\le b$ points have $x \le a$ / $x \ge a$" constraints | Fix size $K$; `L(a,b)` $\iff x_{(b+1)} \ge a+1$, `R(a,b)` $\iff x_{(K-b)} \le a-1$ | 4-layer MCMF: $S \to X_{1..K} \to J_{\text{in}}(i) \to J_{\text{out}}(i) \to Y_{1..K} \to T$ | Accepting flow $< K$ for a fixed-$K$ network violates `R`/`U` suffix-to-prefix rank indices |
| **Manhattan / Chebyshev Max**<br>(`AGC 034 D`) | **Maximize** $\sum (\|x_i - x_j\| + \|y_i - y_j\|)$ for $N \le 1000$ | $\|a\| + \|b\| = \max_{s_x, s_y \in \{\pm 1\}} \big((s_x x_i + s_y y_i) + (-s_x x_j - s_y y_j)\big)$ | 4 Sign Hubs $H_{++}, H_{+-}, H_{-+}, H_{--}$ ($O(N)$ edges total) | **Cannot** be used for **Minimum** Manhattan Matching ($\min \max \neq \min \min$) |

---

## 4-Tier Curated Problem Bank (Part 1: Stepping Stone & Intermediate Tiers)

Every problem below is self-contained and solved using the **4-Step "Zero Magic Gadgets" Compilation Standard**, followed by 3-tier progressive hints.

---

### Tier 1: Stepping Stone Problems (Problems 1–5)

#### Problem 1: Collect-Once Multi-Walker Grid (`[ZH]` Luogu P2045 `方格取数加强版` / `[EN]` POJ 3422 `Kaka's Matrix Travels`)
- **Judge URL**: [Luogu P2045](https://www.luogu.com.cn/problem/P2045) / [POJ 3422](http://poj.org/problem?id=3422)
- **Statement & Constraints**: Given an $N \times N$ grid ($1 \le N \le 50$) where cell $(r, c)$ contains a non-negative integer reward $w_{r,c} \in [0, 1000]$, send $K$ walkers ($1 \le K \le 10$) from $(1, 1)$ to $(N, N)$ moving only Right $(r, c+1)$ or Down $(r+1, c)$. When the first walker visits $(r, c)$, it collects $w_{r,c}$ and sets the cell's value to $0$ for all subsequent walkers. Maximize the total reward collected by the $K$ walkers.
- **Step 1 (Diagnostic Signal)**:
  - $K \le 10$ walkers immediately rules out simultaneous multi-walker DP ($O(N^{K+1}) \approx 50^{11}$ states).
  - The reward at cell $v = (r, c)$ as a function of total visits $f_v \in \{0, 1, \dots, K\}$ is $R_v(f_v) = w_v \cdot \min(f_v, 1)$, which is concave (marginal gains $w_v, 0, 0, \dots$ are non-increasing).
- **Step 2 (Algebraic Intermediate Form)**:
  Let $f_v \in [0, K]$ be the number of walkers passing through $v = (r, c)$. Flow conservation requires $\sum_{u \to v} f_{u,v} = f_v = \sum_{v \to w} f_{v,w}$ for $v \notin \{(1,1), (N,N)\}$, with $f_{(1,1)} = f_{(N,N)} = K$. We minimize $\sum_v C_v(f_v)$ where $\Delta C_v(1) = -w_v \le 0$ and $\Delta C_v(r) = 0$ for $r \ge 2$.
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Split each cell $v = (r, c)$ into $v_{\text{in}}$ and $v_{\text{out}}$ (total $2N^2 \le 5000$ vertices).
  - Connect $v_{\text{in}} \to v_{\text{out}}$ with two parallel edges: $(1, -w_v)$ and $(K - 1, 0)$.
  - For each valid step $v \to u$ (Right or Down), add $v_{\text{out}} \to u_{\text{in}}$ with $(K, 0)$.
  - Connect $S \to (1, 1)_{\text{in}}$ with $(K, 0)$ and $(N, N)_{\text{out}} \to T$ with $(K, 0)$.
- **Step 4 (Complete Solution & Failure Mode)**:
  - Run SSP for $K \le 10$ augmentations on $V = 2N^2 + 2 \le 5002$, $E \le 4N^2 \le 10{,}000$. Because the graph is initially a DAG, initialize Johnson potentials $\pi$ via topological DP in $O(N^2)$ and run $K$ Dijkstra passes in $O(K N^2 \log N) \approx 4 \times 10^5$ operations. Negate the minimum cost to obtain the maximum reward.
  - *Failure Mode*: Never place $(1, -w_v)$ on incoming grid edges $u \to v$, or two walkers entering $v$ from $(r-1, c)$ and $(r, c-1)$ will collect $w_v$ twice.
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Why can't we track $K$ walkers in a DP state when $K = 10$? Notice that walkers are indistinguishable—only the *number of times* each cell and edge is traversed matters.
  - *Hint 2 (Algebraic)*: Write the marginal cost of the $1$-st, $2$-nd, ..., $K$-th visit to cell $(r, c)$. Since $w_{r,c} \ge 0$, is this marginal cost sequence non-decreasing?
  - *Hint 3 (Compilation)*: Split each cell into $\text{in}$ and $\text{out}$ nodes connected by two parallel arcs: capacity $1$ with cost $-w_{r,c}$, and capacity $K-1$ with cost $0$.

---

#### Problem 2: Maximum Internally Vertex-Disjoint Shortest Paths (`[ZH]` Luogu P2153 `[SDOI2009] 晨跑`)
- **Judge URL**: [Luogu P2153](https://www.luogu.com.cn/problem/P2153)
- **Statement & Constraints**: Given a directed graph with $N$ intersections ($2 \le N \le 200$) and $M$ directed streets ($1 \le M \le 20{,}000$) where street $e = (u, v)$ has length $w_e \ge 1$, Elaxia wants to run from home (vertex $1$) to school (vertex $N$) for as many days $K$ as possible such that:
  1. No two daily routes share any intermediate intersection $v \in \{2, \dots, N-1\}$,
  2. No two daily routes share the same directed street $e$ (important if $(1, N)$ has direct edges!).
  Maximize the number of days $K$, and among all schedules with maximum $K$, minimize the total distance run across all $K$ days.
- **Step 1 (Diagnostic Signal)**:
  - Primary objective: maximize number of paths $K$ (= Max-Flow).
  - Secondary objective: minimize total edge length (= Min-Cost).
  - This is the textbook signature of **Min-Cost Max-Flow** with unit vertex capacities on $v \in \{2, \dots, N-1\}$.
- **Step 2 (Algebraic Intermediate Form)**:
  Let $f_e \in \{0, 1\}$ indicate whether street $e = (u, v)$ is used. Flow conservation at $v \in \{2, \dots, N-1\}$ gives $\sum_{e \in \delta^-(v)} f_e = \sum_{e \in \delta^+(v)} f_e = f_v \le 1$. We maximize $K = \sum_{e \in \delta^+(1)} f_e$ and secondary-minimize $\sum_{e \in E} w_e f_e$.
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Split every vertex $v \in \{1, \dots, N\}$ into $v_{\text{in}}$ and $v_{\text{out}}$.
  - For $v \in \{2, \dots, N-1\}$, add internal bridge $v_{\text{in}} \to v_{\text{out}}$ with $(\text{cap} = 1, \text{cost} = 0)$.
  - For $v \in \{1, N\}$, add $1_{\text{in}} \to 1_{\text{out}}$ and $N_{\text{in}} \to N_{\text{out}}$ with $(\text{cap} = \infty, \text{cost} = 0)$, and set $S = 1_{\text{in}}, T = N_{\text{out}}$.
  - For each street $e = (u, v)$ of length $w_e$, add $u_{\text{out}} \to v_{\text{in}}$ with $(\text{cap} = 1, \text{cost} = w_e)$.
- **Step 4 (Complete Solution & Failure Mode)**:
  - Run standard MCMF from $S = 1_{\text{in}}$ to $T = N_{\text{out}}$. Since $N \le 200$, the maximum possible flow is $K \le N \le 200$. Thus SSP terminates in at most $200$ augmentations, running in $O(K M \log N) \approx 4 \times 10^6$ operations. Output `(max_flow, min_cost)`.
  - *Failure Mode*: Giving street edges $u_{\text{out}} \to v_{\text{in}}$ capacity $\infty$ instead of $1$ fails when there is a direct edge $1 \to N$: since $1$ and $N$ have capacity $\infty$, capacity $\infty$ on $1_{\text{out}} \to N_{\text{in}}$ would send infinite flow across a single direct street $(1, N)$!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: "Maximize number of paths, then minimize total length" is literally the two-tuple output $(F_{\max}, C_{\min})$ of Min-Cost Max-Flow.
  - *Hint 2 (Algebraic)*: How do you cap total visits to an intermediate vertex $v \in \{2, \dots, N-1\}$ at $1$ while allowing $1$ and $N$ to be visited $K$ times?
  - *Hint 3 (Compilation)*: Split $v$ into $v_{\text{in}} \to v_{\text{out}}$ with capacity $1$ (for $2 \le v \le N-1$), and give every road edge $u_{\text{out}} \to v_{\text{in}}$ capacity $1$ and cost $w_e$.

---

#### Problem 3: DAG Path Cover with Arbitrary Teleport Resets (`[ZH]` Luogu P2469 `[SDOI2010] 星际竞速`)
- **Judge URL**: [Luogu P2469](https://www.luogu.com.cn/problem/P2469)
- **Statement & Constraints**: There are $N$ planets numbered $1, \dots, N$ ($1 \le N \le 800$) and $M$ directed gravity routes ($1 \le M \le 15{,}000$). Each gravity route goes from planet $u$ to planet $v$ with $u < v$ and takes time $w_{uv}$. Additionally, from any position (including the start), the spaceship can enter hyperspace and teleport directly to any planet $v$ in time $A_v$. Every planet $1, \dots, N$ must be visited **at least once**, and a planet cannot be visited more than once (so each planet is visited **exactly once**). Find the minimum total time to visit all $N$ planets.
- **Step 1 (Diagnostic Signal)**:
  - All gravity routes satisfy $u < v$, so the underlying graph is a **strictly acyclic DAG**!
  - Visiting every planet $v \in \{1, \dots, N\}$ exactly once using gravity edges $u \to v$ and teleport jumps (cost $A_v$ to start a new path at $v$) partitions the $N$ planets into a set of vertex-disjoint DAG paths, where starting a path at $v$ costs $A_v$ and continuing a path along $u \to v$ costs $w_{uv}$.
- **Step 2 (Algebraic Intermediate Form)**:
  For each planet $v \in \{1, \dots, N\}$, let $s_v \in \{0, 1\}$ indicate whether we teleport to $v$ (starting a new path at $v$), and let $x_{u,v} \in \{0, 1\}$ indicate whether we fly directly from $u$ to $v$ ($u < v$).
  Since every planet $v$ must be entered **exactly once** (either via teleport or from some $u < v$), and exited **at most once**:
  $$\forall v \in [1, N]: \quad s_v + \sum_{u < v} x_{u,v} = 1, \qquad \forall u \in [1, N]: \quad \sum_{v > u} x_{u,v} \le 1.$$
  We minimize $\sum_{v=1}^N A_v s_v + \sum_{u < v} w_{uv} x_{u,v}$.
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Create bipartite halves $L = \{u_{\text{out}} : 1 \le u \le N\}$ and $R = \{v_{\text{in}} : 1 \le v \le N\}$.
  - Add $v_{\text{in}} \to T$ with $(\text{cap} = 1, \text{cost} = 0)$ for each $v \in [1, N]$ (enforcing the $= 1$ RHS in $s_v + \sum_{u < v} x_{u,v} = 1$).
  - Add $S \to u_{\text{out}}$ with $(\text{cap} = 1, \text{cost} = 0)$ for each $u \in [1, N]$ (enforcing $\sum_{v > u} x_{u,v} \le 1$).
  - For each gravity route $(u, v)$ ($u < v$), add $u_{\text{out}} \to v_{\text{in}}$ with $(\text{cap} = 1, \text{cost} = w_{uv})$ (variable $x_{u,v}$).
  - For each planet $v \in [1, N]$, add teleport edge $S \to v_{\text{in}}$ with $(\text{cap} = 1, \text{cost} = A_v)$ (variable $s_v$).
- **Step 4 (Complete Solution & Failure Mode)**:
  - Run MCMF from $S$ to $T$. Because $S \to v_{\text{in}} \to T$ always exists for every $v$, the maximum flow is guaranteed to be $N$, and every unit of flow into $v_{\text{in}}$ picks the globally optimal combination of teleports $S \to v_{\text{in}}$ and gravity transitions $u_{\text{out}} \to v_{\text{in}}$.
  - *Failure Mode*: Notice why $u < v$ in the problem statement is **not** cosmetic: if $u > v$ edges were present, a cheap cycle $a \to b \to a$ could form without any teleport $s_a = s_b = 1$, violating the physical requirement that the ship starts from hyperspace!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Why does the problem specify $u < v$ for every gravity route? What happens to a ship's trajectory every time it uses hyperspace teleportation?
  - *Hint 2 (Algebraic)*: Every planet $v$ is entered exactly once—either by teleporting to $v$ at cost $A_v$, or by flying from some previous planet $u < v$ at cost $w_{uv}$ (where each $u$ can fly to at most one next planet $v$).
  - *Hint 3 (Compilation)*: Build a bipartite graph with $u_{\text{out}} \in L$ and $v_{\text{in}} \in R$. Demand $1$ unit at every $v_{\text{in}} \to T$, supply $\le 1$ unit at $S \to u_{\text{out}}$, connect $u_{\text{out}} \to v_{\text{in}}$ with cost $w_{uv}$, and connect $S \to v_{\text{in}}$ directly with cost $A_v$.

---

#### Problem 4: Multi-Speed Resource Refurbishment (`[ZH]` Luogu P1251 `[网络流24题] 餐巾计划问题`)
- **Judge URL**: [Luogu P1251](https://www.luogu.com.cn/problem/P1251)
- **Statement & Constraints**: Over $D$ days ($1 \le D \le 2000$), day $t$ requires $r_t$ clean napkins ($1 \le r_t \le 10^7$). Buying a new napkin costs $p$; fast laundry takes $m$ days and costs $f$; slow laundry takes $n$ days and costs $s$. Find the minimum total cost to satisfy all $D$ days. (Use 64-bit integers `long long` for capacities and costs!)
- **Step 1 (Diagnostic Signal)**:
  - Daily consumption $r_t$ transforms clean napkins into dirty napkins that reappear $m$ or $n$ days later.
  - As proved in Section 85.1, eliminating the mandatory lower-bound spine $M_t \xrightarrow{[r_t, r_t]} E_t$ yields the Bipartite Day/Night Split.
- **Step 2 (Algebraic Intermediate Form)**:
  Let $E_t$ be the dirty supply node on evening $t$ (supply $r_t$) and $M_t$ be the clean demand node on morning $t$ (demand $r_t$). Every unit of demand at $M_t$ must be met by either fresh purchase $S \to M_t$ (cost $p$), fast laundry $E_{t-m} \to M_t$ (cost $f$), or slow laundry $E_{t-n} \to M_t$ (cost $s$), with dirty inventory carryover $E_t \to E_{t+1}$ (cost $0$).
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Vertices: $S, T$, $E_1 \dots E_D$, $M_1 \dots M_D$ ($2D + 2 \le 4002$ vertices).
  - Edges:
    1. $S \to E_t$: $(\text{cap} = r_t, \text{cost} = 0)$ and $M_t \to T$: $(\text{cap} = r_t, \text{cost} = 0)$ for $t \in [1, D]$.
    2. $S \to M_t$: $(\text{cap} = \infty, \text{cost} = p)$ for $t \in [1, D]$.
    3. $E_t \to E_{t+1}$: $(\text{cap} = \infty, \text{cost} = 0)$ for $t \in [1, D-1]$.
    4. $E_t \to M_{t+m}$: $(\text{cap} = \infty, \text{cost} = f)$ for $t + m \le D$.
    5. $E_t \to M_{t+n}$: $(\text{cap} = \infty, \text{cost} = s)$ for $t + n \le D$.
- **Step 4 (Complete Solution & Failure Mode)**:
  - Total vertices $V \le 4002$, total edges $E \le 6D \le 12{,}000$, all initial costs $\ge 0$! Because all initial edge costs are non-negative ($p, f, s, 0 \ge 0$), initial Johnson potentials are simply $\pi(v) = 0$! Run Primal–Dual (Zkw MCMF or Dijkstra SSP with multi-push DFS) in $O(D^2 \log D)$ to get the exact 64-bit minimum cost.
  - *Failure Mode*: Overflowing 32-bit `int` ($D \cdot r_t \cdot p$ can reach $2000 \times 10^7 \times 10^4 = 2 \times 10^{14}$).
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Why can't we represent day $t$ as a single vertex without lower bounds? Split day $t$ into Morning (clean demand) and Evening (dirty supply).
  - *Hint 2 (Algebraic)*: Think of the $r_t$ used napkins as a mandatory flow $M_t \xrightarrow{[r_t, r_t]} E_t$. What happens when you replace a fixed flow $[r_t, r_t]$ with source/sink supply/demand edges?
  - *Hint 3 (Compilation)*: Connect $S \to E_t$ with $(r_t, 0)$, $M_t \to T$ with $(r_t, 0)$, $S \to M_t$ with $(\infty, p)$, $E_t \to E_{t+1}$ with $(\infty, 0)$, and laundry edges $E_t \to M_{t+m}$ and $E_t \to M_{t+n}$.

---

#### Problem 5: Weighted $K$-Slot Cache Retention (`[EN]` Codeforces 802 C `Heidi and Library (medium)`)
- **Judge URL**: [Codeforces 802 C](https://codeforces.com/problemset/problem/802/C)
- **Statement & Constraints**: A library can hold at most $K$ books ($1 \le K \le 80$). Over $N$ days ($1 \le N \le 80$), on day $t$ a reader requests book $a_t \in [1, N]$. If book $a_t$ is not in the library on morning $t$, Heidi must buy it for $c_{a_t}$ CHF ($1 \le c_i \le 10^6$), possibly discarding an existing book if the library already holds $K$ books. Find the minimum total cost to satisfy all $N$ requests.
- **Step 1 (Diagnostic Signal)**:
  - $N, K \le 80$ with heterogeneous book costs $c_i$.
  - Keeping book $a_t$ from day $t$ to its next request day $\text{next}(t)$ saves $c_{a_t}$ and consumes $1$ of the $K - 1$ idle library slots on days $t + 1, \dots, \text{next}(t) - 1$.
- **Step 2 (Algebraic Intermediate Form)**:
  First remove consecutive duplicate requests $a_t = a_{t+1}$ (keeping the book across adjacent days is always free and uses $0$ intermediate idle slots). Let $N'$ be the compressed length, and start with $\text{Base} = \sum_{t=1}^{N'} c_{a_t}$ (buying every day).
  For each $t \in [1, N']$ that has a next occurrence $t' = \text{next}(t) \ge t + 2$, let $x_t \in \{0, 1\}$ indicate whether we retain book $a_t$ across $[t+1, t'-1]$. We minimize $\text{Base} + \sum_t (-c_{a_t}) x_t$ subject to $\sum_{t < s < \text{next}(t)} x_t \le K - 1$ for all $s \in [1, N']$.
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Create timeline vertices $1, 2, \dots, N'$, source $S = 1$, sink $T = N'$.
  - Add backbone edges $s \to s + 1$ with $(\text{cap} = K - 1, \text{cost} = 0)$ for $s = 1, \dots, N' - 1$.
  - For each $t$ with $t' = \text{next}(t) \ge t + 2$, add chord $(t + 1) \to t'$ with $(\text{cap} = 1, \text{cost} = -c_{a_t})$.
- **Step 4 (Complete Solution & Failure Mode)**:
  - Push $K - 1$ units of flow from $1$ to $N'$ (using DAG DP for initial potentials since all edges go from smaller index to larger index!). Add the resulting (negative) min-cost to $\text{Base}$. Complexity: $O(K \cdot N^2) \approx 5 \times 10^5$ operations!
  - *Failure Mode*: Forgetting to compress adjacent identical requests $a_t = a_{t+1}$ (or adding a self-loop chord $(t+1) \to (t+1)$ when $\text{next}(t) = t + 1$).
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Suppose you start by paying $\sum_{t=1}^N c_{a_t}$ to buy a fresh copy on every single day, and then look for *rebates* when you keep book $a_t$ until its next occurrence $\text{next}(t)$.
  - *Hint 2 (Algebraic)*: On any day $s$, one of the $K$ slots is used by the book $a_s$ requested on day $s$. How many *other* books can be stored across day $s$?
  - *Hint 3 (Compilation)*: Build a timeline $1 \to 2 \to \dots \to N$ with backbone capacity $K - 1$ and cost $0$, and add rebate chords $(t + 1) \to \text{next}(t)$ with capacity $1$ and cost $-c_{a_t}$.

---

### Tier 2: Intermediate Problems (Problems 6–11)

#### Problem 6: Heterogeneous Parallel Machine Total Completion Time (`[ZH]` Luogu P2053 `[SCOI2007] 修车`)
- **Judge URL**: [Luogu P2053](https://www.luogu.com.cn/problem/P2053)
- **Statement & Constraints**: $N$ customers ($1 \le N \le 60$) bring their cars to a repair shop with $M$ technicians ($1 \le M \le 9$). Technician $j$ takes $t_{i,j}$ minutes ($1 \le t_{i,j} \le 1000$) to repair car $i$. Each technician repairs their assigned cars sequentially one at a time. A customer's waiting time is the time until their car's repair is completed. Minimize the average waiting time of the $N$ customers (output to 2 decimal places).
- **Step 1 (Diagnostic Signal)**:
  - Minimizing average waiting time $=$ minimizing the sum of completion times $\sum_{i=1}^N C_i$ divided by $N$.
  - $N \le 60, M \le 9$: total backward slots $M \times N \le 540$.
- **Step 2 (Algebraic Intermediate Form)**:
  By the Backward Waiting-Time Formula (Section 84.1), if car $i$ is placed in the $r$-th-from-last slot $(j, r)$ of technician $j$, it delays itself and the $r - 1$ subsequent cars on technician $j$, contributing $r \cdot t_{i,j}$ to the sum of completion times:
  $$\min \sum_{i=1}^N \sum_{j=1}^M \sum_{r=1}^N (r \cdot t_{i,j}) x_{i,j,r}.$$
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Left vertices: Cars $i \in \{1, \dots, N\}$ with $S \to i$ of $(\text{cap} = 1, \text{cost} = 0)$.
  - Right vertices: Slots $(j, r)$ for $j \in [1, M], r \in [1, N]$ with $(j, r) \to T$ of $(\text{cap} = 1, \text{cost} = 0)$.
  - Cross edges: $i \to (j, r)$ with $(\text{cap} = 1, \text{cost} = r \cdot t_{i,j})$. (Can be spawned lazily or built statically since $NM = 540$.)
- **Step 4 (Complete Solution & Failure Mode)**:
  - Run MCMF for $N \le 60$ units of flow and output $\text{min\_cost} / N$.
  - *Failure Mode*: Indexing $r$ from the *front* of the queue instead of from the *back* of the queue!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: If a technician repairs 3 cars with durations $a, b, c$ in that order, their completion times are $a$, $a+b$, and $a+b+c$, whose sum is $3a + 2b + 1c$.
  - *Hint 2 (Algebraic)*: Notice that the *last* car has coefficient $1$, the *second-to-last* car has coefficient $2$, and the $r$-th-from-last car has coefficient $r$, regardless of how many cars precedes it!
  - *Hint 3 (Compilation)*: Match the $N$ cars on the left to technician-slot pairs $(j, r) \in [1, M] \times [1, N]$ on the right with edge cost $r \cdot t_{i,j}$.

---

#### Problem 7: Maximum-Weight $K$-Overlap Interval Selection (`[EN]` POJ 3680 `Intervals`)
- **Judge URL**: [POJ 3680](http://poj.org/problem?id=3680)
- **Statement & Constraints**: Given $N$ open intervals $(a_i, b_i)$ ($1 \le N \le 200$, $1 \le a_i < b_i \le 10^5$) where interval $i$ has positive weight $w_i \in [1, 10^5]$, choose a subset of intervals of maximum total weight such that no point $x \in \mathbb{R}$ is covered by more than $K$ chosen intervals ($1 \le K \le N$).
- **Step 1 (Diagnostic Signal)**:
  - "Select weighted intervals $(a_i, b_i)$ so no point has overlap $> K$": this is the canonical **Interval Packing / $K$-Coloring of Interval Graphs** problem, solvable via either Timeline + Chord MCMF or Consecutive Equation Differences.
- **Step 2 (Algebraic Intermediate Form)**:
  Coordinate-compress the distinct endpoints $\{a_i, b_i\}$ into $1 < 2 < \dots < M$ ($M \le 2N \le 400$).
  Send $K$ units of flow along the timeline $1 \to 2 \to \dots \to M$. Each interval $i = (\text{id}(a_i), \text{id}(b_i))$ can divert at most $1$ unit of flow from $\text{id}(a_i)$ directly to $\text{id}(b_i)$ at cost $-w_i$, leaving the remaining flow on the timeline backbone $\text{id}(a_i) \to \dots \to \text{id}(b_i)$. Since total flow is $K$, at most $K$ intervals can bypass any elementary segment $s \to s + 1$!
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Vertices: Compressed coordinate points $1, 2, \dots, M$, plus $S$ and $T$.
  - $S \to 1$ with $(K, 0)$, and $M \to T$ with $(K, 0)$.
  - Timeline backbone: $s \to s + 1$ with $(K, 0)$ for $s = 1, \dots, M - 1$.
  - Interval chords: $\text{id}(a_i) \to \text{id}(b_i)$ with $(1, -w_i)$ for $i = 1, \dots, N$.
- **Step 4 (Complete Solution & Failure Mode)**:
  - Since all edges go from smaller index to larger index, compute initial Johnson potentials $\pi(1 \dots M)$ by DAG DP in $O(N + M)$ time, then run $K$ steps of Dijkstra in $O(K (M + N) \log M)$. Answer is $-\text{min\_cost}$.
  - *Failure Mode*: If the intervals were **closed** $[a_i, b_i]$ instead of open $(a_i, b_i)$, two intervals $[1, 3]$ and $[3, 5]$ overlap at point $3$! To handle closed intervals $[a_i, b_i]$, replace $[a_i, b_i]$ with the half-open interval $[a_i, b_i + 1)$ (or split each coordinate point into $x_{\text{in}} \to x_{\text{out}}$)!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Coordinate-compress all endpoints $a_i, b_i$ so there are at most $2N \le 400$ elementary segments $s \to s+1$.
  - *Hint 2 (Algebraic)*: Think of $K$ tokens walking from $x = 1$ to $x = M$. If an interval $(a_i, b_i)$ is selected, $1$ token jumps along the chord $a_i \to b_i$ instead of walking along the backbone $a_i \to \dots \to b_i$.
  - *Hint 3 (Compilation)*: Add backbone edges $s \to s+1$ of capacity $K$ and cost $0$, and interval chords $\text{id}(a_i) \to \text{id}(b_i)$ of capacity $1$ and cost $-w_i$.

---

#### Problem 8: Bitonic Round-Trip Max-Vertex Tour (`[ZH]` Luogu P2770 `[网络流24题] 航空路线问题`)
- **Judge URL**: [Luogu P2770](https://www.luogu.com.cn/problem/P2770)
- **Statement & Constraints**: Given $N$ cities ($2 \le N \le 100$) ordered from West ($1$) to East ($N$) and $M$ undirected flight routes, find a round-trip tour starting at city $1$, flying strictly West-to-East to city $N$, and then flying strictly East-to-West back to city $1$, such that no intermediate city $v \in \{2, \dots, N-1\}$ is visited more than once, maximizing the total number of cities visited. Output the maximum number of cities and the exact itinerary.
- **Step 1 (Diagnostic Signal)**:
  - Reversing the return trip $N \to \dots \to 1$ turns it into a **second West-to-East path** $1 \to \dots \to N$!
  - Therefore, a valid round-trip tour $1 \to \dots \to N \to \dots \to 1$ is in exact bijection with **two internally vertex-disjoint directed paths from $1$ to $N$** (where every flight edge $\{u, v\}$ with $u < v$ is oriented West-to-East $u \to v$), maximizing the total number of vertices visited!
- **Step 2 (Algebraic Intermediate Form)**:
  Send $K = 2$ units of flow from $1_{\text{in}}$ to $N_{\text{out}}$, where each intermediate vertex $v \in \{2, \dots, N-1\}$ has throughput $f_v \le 1$ and reward $+1$ (cost $-1$), and endpoints $1, N$ have throughput $2$ and reward $+1$ each.
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Split $v \in \{1, \dots, N\}$ into $v_{\text{in}} \to v_{\text{out}}$:
    - For $v \in \{2, \dots, N-1\}$: $(\text{cap} = 1, \text{cost} = -1)$.
    - For $v \in \{1, N\}$: $(\text{cap} = 2, \text{cost} = -1)$ (or cost $0$ and add $+2$ at the end).
  - For each undirected edge $\{u, v\}$ with $u < v$: add $u_{\text{out}} \to v_{\text{in}}$ with $(\text{cap} = 1, \text{cost} = 0)$ (Except if $u = 1$ and $v = N$: give $1_{\text{out}} \to N_{\text{in}}$ capacity $2$ so the degenerate $2$-city tour $1 \to N \to 1$ is allowed when only edge $(1, N)$ exists!).
- **Step 4 (Complete Solution & Failure Mode)**:
  - Run MCMF from $1_{\text{in}}$ to $N_{\text{out}}$.
  - If max-flow $= 2$, the max cities visited is $2 - \text{min\_cost}$ (if $1, N$ had cost $0$; note that for the degenerate $1 \to N \to 1$ case where $1_{\text{out}} \to N_{\text{in}}$ carries $2$ units, output $2$ cities). Reconstruct the two disjoint paths by following saturated edges $u_{\text{out}} \to v_{\text{in}}$: print Path 1 forward ($1 \to \dots \to N$) and Path 2 backward ($N \to \dots \to 1$).
  - *Failure Mode*: Giving $1_{\text{out}} \to N_{\text{in}}$ capacity $1$ instead of $2$ fails on the test case where $N = 2$ (or where $1$ and $N$ are connected only by the direct edge $(1, N)$), because the tour $1 \to N \to 1$ uses edge $(1, N)$ twice (once Eastbound, once Westbound)!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Instead of one path going East $1 \to N$ and one path going West $N \to 1$, reverse the Westbound path so both paths go West-to-East $1 \to N$.
  - *Hint 2 (Algebraic)*: How do you maximize the number of distinct internal vertices visited by $2$ vertex-disjoint paths from $1$ to $N$?
  - *Hint 3 (Compilation)*: Split $v_{\text{in}} \to v_{\text{out}}$ with $(\text{cap} = 1, \text{cost} = -1)$ for $2 \le v \le N-1$, and watch out for the direct edge $(1, N)$, which can be used in both directions (capacity $2$)!

---

#### Problem 9: Fleet Bounded-Start DAG Path Cover (`[EN]` ICPC World Finals 2015 Problem C `Catering`)
- **Judge URL**: [Kattis / ICPC WF 2015 C — Catering](https://open.kattis.com/problems/catering)
- **Statement & Constraints**: A catering company has $K$ equipment teams ($1 \le K \le 100$) initially at the company headquarters (location $1$). There are $N$ catering requests ($1 \le N \le 100$) numbered $2, 3, \dots, N + 1$ in chronological order. Moving a team from location $u$ to request $v$ ($1 \le u < v \le N + 1$) costs $c_{u,v} \ge 0$. Every request $2, \dots, N+1$ must be served by exactly one team, and each team can serve a sequence of requests $1 \to v_1 \to v_2 \to \dots$ with $1 < v_1 < v_2 < \dots$. Find the minimum total moving cost.
- **Step 1 (Diagnostic Signal)**:
  - All transitions satisfy $u < v$, forming a DAG on $\{2, \dots, N+1\}$ plus starter headquarters $1$.
  - Every request $v \in \{2, \dots, N+1\}$ must be visited **exactly once** by one of the $\le K$ paths starting at headquarters $1$.
  - This is a **Min-Cost DAG Path Cover with Fleet Size $\le K$** (Section 83.2).
- **Step 2 (Algebraic Intermediate Form)**:
  For each request $v \in \{2, \dots, N+1\}$, let $x_{1, v} \in \{0, 1\}$ indicate whether a team starts its first job at $v$ directly from headquarters $1$, and for $2 \le u < v \le N+1$, let $x_{u,v} \in \{0, 1\}$ indicate whether the team at $u$ moves next to $v$.
  Then:
  $$\forall v \in [2, N+1]: \quad x_{1,v} + \sum_{2 \le u < v} x_{u,v} = 1, \qquad \forall u \in [2, N+1]: \quad \sum_{v > u} x_{u,v} \le 1, \qquad \sum_{v=2}^{N+1} x_{1,v} \le K.$$
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Create headquarters node $H_1$ with $S \to H_1$ of $(\text{cap} = K, \text{cost} = 0)$.
  - For each request $u \in \{2, \dots, N+1\}$, create $u_{\text{out}} \in L$ with $S \to u_{\text{out}}$ of $(\text{cap} = 1, \text{cost} = 0)$ and $u_{\text{in}} \in R$ with $u_{\text{in}} \to T$ of $(\text{cap} = 1, \text{cost} = 0)$.
  - Add starter edges $H_1 \to v_{\text{in}}$ with $(\text{cap} = 1, \text{cost} = c_{1,v})$ for $v \in [2, N+1]$.
  - Add transition edges $u_{\text{out}} \to v_{\text{in}}$ with $(\text{cap} = 1, \text{cost} = c_{u,v})$ for $2 \le u < v \le N+1$.
- **Step 4 (Complete Solution & Failure Mode)**:
  - Push $F_{\text{req}} = N$ units of flow from $S$ to $T$. Since $N \ge 1$ and $K \ge 1$, all $N$ demands at $v_{\text{in}} \to T$ are always satisfiable (even $1$ team can visit $1 \to 2 \to 3 \to \dots \to N+1$). The minimum cost of the max-flow of value $N$ is the exact answer!
  - *Failure Mode*: Requiring $S \to H_1$ to send *exactly* $K$ units (instead of $\le K$ units) fails when using fewer than $K$ teams is cheaper than dispatching a new team from headquarters $1$! In our construction, $S \to H_1$ has capacity $K$ and cost $0$, and since total demand at $T$ is $N$ while $\sum_{u=2}^{N+1} \text{cap}(S \to u_{\text{out}}) = N$, any team not needed simply leaves residual capacity on $S \to H_1$!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Every event $v \in \{2, \dots, N+1\}$ has in-degree $1$ (either from HQ $1$ or from an earlier event $u < v$) and out-degree $\le 1$, and HQ $1$ has out-degree $\le K$.
  - *Hint 2 (Algebraic)*: Write the in-degree $= 1$ equation for each event $v$: $x_{1,v} + \sum_{2 \le u < v} x_{u,v} = 1$, subject to $\sum_v x_{1,v} \le K$ and $\sum_v x_{u,v} \le 1$.
  - *Hint 3 (Compilation)*: Build the bipartite path-cover network with a starter hub $H_1$ ($S \to H_1$ capacity $K$), $S \to u_{\text{out}}$ capacity $1$, and $v_{\text{in}} \to T$ capacity $1$.

---

#### Problem 10: Multi-Rover Collect-Once Grid & Flow Path Decomposition (`[ZH]` Luogu P3356 `[网络流24题] 火星探险问题`)
- **Judge URL**: [Luogu P3356](https://www.luogu.com.cn/problem/P3356)
- **Statement & Constraints**: $R$ rovers ($1 \le R \le 20$) land at $(1, 1)$ on a $Q \times P$ grid ($1 \le P, Q \le 35$) and must reach the recovery beacon at $(Q, P)$ moving only South $(r+1, c)$ or East $(r, c+1)$. Each cell is either `0` (flat ground), `1` (impassable obstacle), or `2` (rock sample, which can be collected at most once by the first rover visiting it). Maximize the total rock samples collected, and **print the exact step-by-step movements** (`0` for South, `1` for East) of each rover $1, \dots, R$.
- **Step 1 (Diagnostic Signal)**:
  - The maximization part is identical to Problem 1 (`方格取数`) with obstacles (`1` cells have $0$ capacity).
  - The new challenge is **Flow-to-Path Decomposition**: after MCMF finds the optimal integer flow $f$ on the grid edges, how do we extract $R$ individual rover trajectories?
- **Step 2 (Algebraic Intermediate Form)**:
  By the Flow Decomposition Theorem on a DAG, any integer $S$-$T$ flow of volume $R$ can be decomposed into $R$ unit $S$-$T$ paths by repeatedly tracing a path from $(1, 1)$ to $(Q, P)$ along edges with positive flow $f(u_{\text{out}} \to v_{\text{in}}) > 0$ and decrementing $f(u_{\text{out}} \to v_{\text{in}}) \gets f(u_{\text{out}} \to v_{\text{in}}) - 1$ at each step!
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - For each non-obstacle cell $v = (r, c)$:
    - If cell is `0`: add $v_{\text{in}} \to v_{\text{out}}$ with $(\text{cap} = \infty, \text{cost} = 0)$.
    - If cell is `2`: add parallel edges $(1, -1)$ and $(\infty, 0)$ from $v_{\text{in}}$ to $v_{\text{out}}$.
  - For each valid move $v \to u$ (South or East) between non-obstacle cells, add $v_{\text{out}} \to u_{\text{in}}$ with $(\text{cap} = \infty, \text{cost} = 0)$.
- **Step 4 (Complete Solution & Failure Mode)**:
  - Run MCMF with $S \to (1,1)_{\text{in}}$ of capacity $R$.
  - Then, for rover $id = 1, \dots, R$, start a simple DFS/walk at $v = (1, 1)$: while $v \neq (Q, P)$, find an outgoing transition edge $e = (v_{\text{out}} \to u_{\text{in}})$ that currently carries positive flow ($\text{flow}(e) > 0$, i.e., its reverse residual edge has capacity $> 0$), decrement $\text{flow}(e)$ by $1$, output the direction (`0` or `1`), and advance $v \gets u$.
  - *Failure Mode*: Inspecting the internal cell edge $v_{\text{in}} \to v_{\text{out}}$ instead of the transition edge $v_{\text{out}} \to u_{\text{in}}$ during path tracing.
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Once MCMF computes the net flow on every grid transition edge $(r, c) \to (r+1, c)$ and $(r, c) \to (r, c+1)$, does it matter which rover took which segment at an intersection?
  - *Hint 2 (Algebraic)*: Because flow conservation holds at every cell, any cell entered by a rover during greedy path extraction is guaranteed to have at least one outgoing edge with remaining positive flow!
  - *Hint 3 (Compilation)*: After running MCMF, run $R$ greedy walks from $(1, 1)$ to $(Q, P)$, decrementing the flow on each traversed grid edge by $1$.

---

#### Problem 11: Parametric All-$k$ Bipartite Matching Curve (`[JA]` AtCoder Beginner Contest 247 G `Dream Team`)
- **Judge URL**: [AtCoder ABC 247 G](https://atcoder.jp/contests/abc247/tasks/abc247_g)
- **Statement & Constraints**: There are $N$ competitive programmers ($1 \le N \le 3 \times 10^4$). Person $i$ belongs to university $A_i \in [1, 150]$, specializes in subject $B_i \in [1, 150]$, and has power $C_i \in [1, 10^9]$. A "Dream Team" of size $k$ consists of $k$ people whose universities $A_i$ are pairwise distinct and whose subjects $B_i$ are pairwise distinct. Find the maximum possible team size $K_{\max}$, and **for every $k = 1, 2, \dots, K_{\max}$**, output the maximum total power of a Dream Team of size $k$.
- **Step 1 (Diagnostic Signal)**:
  - Each person $i$ is an edge $(A_i, B_i)$ of weight $C_i$ in a bipartite graph with $150$ universities on the left and $150$ subjects on the right!
  - We need the **Maximum-Weight Bipartite Matching of exact size $k$** for **all $k = 1, 2, \dots, K_{\max}$** simultaneously!
  - By the **Convexity / Slope Property of SSP**, the $k$-th unit augmentation in Successive Shortest Path (with negated weights $-C_i$) finds the exact minimum-cost flow of volume $k$!
- **Step 2 (Algebraic Intermediate Form)**:
  First, if multiple people have the exact same pair $(A_i, B_i)$, at most one of them can ever be chosen in any valid Dream Team (since both $A_i$ and $B_i$ must be distinct). So for each pair $(u, v) \in [1, 150]^2$, keep **only the single person with the maximum $C_i$**! This compresses $N \le 3 \times 10^4$ edges down to at most $150^2 = 22{,}500$ edges!
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Left vertices $U_1, \dots, U_{150}$ with $S \to U_u$ of $(\text{cap} = 1, \text{cost} = 0)$.
  - Right vertices $V_1, \dots, V_{150}$ with $V_v \to T$ of $(\text{cap} = 1, \text{cost} = 0)$.
  - For each nonempty pair $(u, v)$ with max power $C^*_{u,v}$, add $U_u \to V_v$ with $(\text{cap} = 1, \text{cost} = -C^*_{u,v})$ (or shifted cost $10^9 - C^*_{u,v} \ge 0$ so all costs are non-negative!).
- **Step 4 (Complete Solution & Failure Mode)**:
  - Run SSP one unit of flow at a time! After the $k$-th unit augmentation ($k = 1, 2, \dots, K_{\max} \le 150$), record the cumulative flow cost $\text{Cost}(k)$; the answer for team size $k$ is $k \cdot 10^9 - \text{Cost}(k)$!
  - Total augmentations: $K_{\max} \le 150$, on $V = 302$ vertices, running in $< 50$ ms!
  - *Failure Mode*: Using a blocking-flow / multi-push Zkw step that pushes $f > 1$ units of equal shortest-path cost at once without recording the intermediate values for each integer $k \in [1, K_{\max}]$ (if a shortest path has capacity $\Delta f$, record the linear interpolation at each unit step!).
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Each person is a bipartite edge between University $A_i \in [1, 150]$ and Subject $B_i \in [1, 150]$. Why do we only ever need to keep the single strongest person for each $(A_i, B_i)$ pair?
  - *Hint 2 (Algebraic)*: What does the $k$-th augmentation step of the Successive Shortest Path algorithm compute?
  - *Hint 3 (Compilation)*: Shift edge costs to $10^9 - C_i \ge 0$, push flow $1$ unit at a time up to $K_{\max} \le 150$, and read off the answer for each $k$ after the $k$-th unit is pushed!

---

## 4-Tier Curated Problem Bank (Part 2: Advanced & Mastery Tiers)

---

### Tier 3: Advanced Problems (Problems 12–17)

#### Problem 12: Dynamic Lazy Vertex Spawning for Large-Scale Scheduling (`[ZH]` Luogu P2050 `[NOI2012] 美食节`)
- **Judge URL**: [Luogu P2050](https://www.luogu.com.cn/problem/P2050)
- **Statement & Constraints**: There are $N$ dish types ($1 \le N \le 40$) and $M$ chefs ($1 \le M \le 100$). Students order $p_i$ copies of dish $i$, with total dishes $P = \sum_{i=1}^N p_i \le 800$. Chef $j$ takes $t_{i,j}$ time ($1 \le t_{i,j} \le 1000$) to cook one copy of dish $i$. Minimize the sum of waiting times across all $P$ dishes.
- **Step 1 (Diagnostic Signal)**:
  - Identical mathematical objective to Problem 6 (`[SCOI2007] 修车`), except $M \le 100$ and $P \le 800$, so the static backward-slot graph has $M P = 80{,}000$ vertices and $N M P = 3.2 \times 10^6$ edges, which TLEs!
  - By Theorem 84.1, because $r \cdot t_{i,j} < (r+1) \cdot t_{i,j}$, SSP only ever needs **one active empty slot $(j, k_j + 1)$ per chef $j$**!
- **Step 2 (Algebraic Intermediate Form)**:
  $$\min \sum_{i=1}^N \sum_{j=1}^M \sum_{r=1}^P (r \cdot t_{i,j}) x_{i,j,r} \quad \text{s.t.} \quad \sum_{j, r} x_{i,j,r} = p_i, \quad \sum_i x_{i,j,r} \le 1.$$
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Initialize graph with $S, T$, dish nodes $i \in [1, N]$ ($S \to i$ of $(p_i, 0)$), and **only slot $r = 1$** for each chef $j \in [1, M]$ ($(j, 1) \to T$ of $(1, 0)$, and $i \to (j, 1)$ of $(1, 1 \cdot t_{i,j})$).
  - Run SSP $1$ unit at a time for $P$ iterations:
    - In iteration $s \in [1, P]$, find the shortest $S$-$T$ augmenting path and push $1$ unit of flow.
    - Let $u_{\text{last}} = (j^*, r)$ be the vertex immediately preceding $T$ on this augmenting path.
    - Allocate a new vertex $(j^*, r + 1)$, add edge $(j^*, r + 1) \to T$ with $(1, 0)$, and for each $i \in [1, N]$, add edge $i \to (j^*, r + 1)$ with $(1, (r + 1) \cdot t_{i, j^*})$.
    - If using Dijkstra with potentials $\pi$, set $\pi((j^*, r + 1)) := \min_{i=1}^N (\pi(i) + (r + 1) \cdot t_{i, j^*})$ in $O(N)$ time.
- **Step 4 (Complete Solution & Failure Mode)**:
  - Active vertices at termination: $N + M + P + 2 \le 942$. Active edges: $\le 37{,}000$. Total runtime drops from $> 5$ s (TLE) to $< 0.04$ s!
  - *Failure Mode*: Pushing $> 1$ unit of flow along a path before spawning the next slot, or spawning new vertices for intermediate slots $(j', r')$ visited via residual backward arcs instead of only the final slot $(j^*, r) \to T$.
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Why are almost all of the $M \times P = 80{,}000$ slot vertices useless during the early iterations of MCMF?
  - *Hint 2 (Algebraic)*: Prove that an empty slot $(j, r+1)$ can never be on a shortest augmenting path while $(j, r)$ is still empty.
  - *Hint 3 (Compilation)*: Start with only $M$ slot vertices $(j, 1)$. Whenever an augmenting path saturates $(j^*, r) \to T$, dynamically add vertex $(j^*, r+1)$ and its $N$ incoming dish edges.

---

#### Problem 13: Precedence-Locked Multi-Agent Shortest Path Cover (`[ZH]` Luogu P4542 `[ZJOI2011] 营救皮卡丘`)
- **Judge URL**: [Luogu P4542](https://www.luogu.com.cn/problem/P4542)
- **Statement & Constraints**: Given an undirected graph with $N + 1$ bases $0, 1, \dots, N$ ($1 \le N \le 150$) and $M$ bidirectional roads ($M \le 20{,}000$), at most $K$ teams ($1 \le K \le 10$) start at base $0$. Base $v \in [1, N]$ has a defensive barrier that is destroyed the moment a team visits $v$; crucially, **no team may pass through base $w$ until bases $1, 2, \dots, w - 1$ have all been destroyed**. Find the minimum total road length traveled by the $\le K$ teams to destroy all barriers $1, \dots, N$.
- **Step 1 (Diagnostic Signal)**:
  - Although teams walk on an undirected graph and can revisit already-unlocked vertices freely, each barrier $v \in \{1, \dots, N\}$ is **unlocked for the first time** by a single team arriving from the last barrier $u < v$ that *that* team unlocked!
  - Between a team unlocking $u$ and next unlocking $v$ ($u < v$), the set of globally unlocked vertices available as intermediate stepping stones is $\{0, 1, \dots, v - 1\}$.
- **Step 2 (Algebraic Intermediate Form)**:
  Precompute $d_{\le v}(u, v)$: the shortest path between $u$ and $v$ ($0 \le u < v \le N$) using only intermediate vertices $k \in \{0, 1, \dots, v - 1\}$.
  Once $d_{\le v}(u, v)$ is computed, the problem reduces to covering all vertices $v \in \{1, \dots, N\}$ with $\le K$ paths starting at $0$ on the strictly acyclic DAG $(u, v)$ ($u < v$)!
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - **Step 3a (Restricted Floyd–Warshall)**: Initialize `dist[u][v]` with road weights. For $k = 0, 1, \dots, N$: for $u = 0 \dots N$, for $v = 0 \dots N$: update `dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])`; immediately after finishing pivot $k$, for all $v = k + 1$ (or for all $u < v$ when $k = v - 1$), record $d_{\le v}(u, v) = \text{dist}[u][v]$ before pivots $\ge v$ are relaxed!
  - **Step 3b (DAG $K$-Path Cover Network)**:
    - Starter hub $0_{\text{out}}$ with $S \to 0_{\text{out}}$ of $(\text{cap} = K, \text{cost} = 0)$.
    - For $u \in [1, N]$: $S \to u_{\text{out}}$ with $(1, 0)$ and $u_{\text{in}} \to T$ with $(1, 0)$.
    - For $0 \le u < v \le N$: add $u_{\text{out}} \to v_{\text{in}}$ with $(\text{cap} = 1, \text{cost} = d_{\le v}(u, v))$.
- **Step 4 (Complete Solution & Failure Mode)**:
  - Push $N$ units of flow from $S$ to $T$; the min-cost of this max-flow is the exact answer. Complexity: $O(N^3)$ for Floyd–Warshall + $O(N^3)$ for MCMF on $V = 2N + 3 \le 303$ vertices.
  - *Failure Mode*: Recording `dist[u][v]` *after* all $N$ pivots of Floyd–Warshall finish—that allows a team traveling from $u$ to $v$ to pass through a locked vertex $w > v$!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Forget the physical steps between already-unlocked vertices; focus only on the sequence of *newly unlocked barriers* $0 \to v_1 \to v_2 \to \dots$ visited by each of the $K$ teams.
  - *Hint 2 (Algebraic)*: When a team moves from its previous unlocked barrier $u$ to its next unlocked barrier $v$ ($u < v$), which vertices are guaranteed to be unlocked and usable as intermediate vertices? Only $\{0, 1, \dots, v-1\}$!
  - *Hint 3 (Compilation)*: Record $d_{\le v}(u, v)$ right after pivot $k = v - 1$ in Floyd–Warshall, then run a $K$-vehicle DAG Path Cover on $\{1, \dots, N\}$.

---

#### Problem 14: Scaling Collect-Once $K$-Walks to $N = 2 \times 10^5$ via SCC Condensation (`[JA]` AtCoder Beginner Contest 214 H `Collecting`)
- **Judge URL**: [AtCoder ABC 214 H](https://atcoder.jp/contests/abc214/tasks/abc214_h)
- **Statement & Constraints**: Given a directed graph with $N$ vertices ($2 \le N \le 2 \times 10^5$) and $M$ directed edges ($1 \le M \le 2 \times 10^5$), where vertex $v$ holds $X_v \ge 1$ tokens ($X_v \le 10^9$), $K$ players ($1 \le K \le 10$) start at vertex $1$ and walk along directed edges (ending anywhere). Each vertex's $X_v$ tokens can be collected at most once (by the first player visiting $v$). Maximize the total tokens collected.
- **Step 1 (Diagnostic Signal)**:
  - $N, M \le 2 \times 10^5$ with general directed cycles, but $K \le 10$!
  - Any player entering a Strongly Connected Component (SCC) $C$ can traverse all vertices inside $C$, collect $\sum_{v \in C} X_v$, and exit $C$ from any vertex in $C$!
  - Once we contract every SCC $C$ into a single super-vertex with weight $W_C = \sum_{v \in C} X_v$, the contracted graph is a **DAG**!
  - However, standard MCMF with negative edge costs $-W_C$ cannot run SPFA on $N = 2 \times 10^5$ without TLE! How do we run pure $O(K (V + E) \log V)$ Dijkstra from iteration 1? By computing initial Johnson potentials $\pi(u)$ via **DAG Topological DP** (or by shifting edge costs using the topological height / potential)!
- **Step 2 (Algebraic Intermediate Form)**:
  Contract $G$ into its SCC DAG $\mathcal{D} = (\mathcal{C}, \mathcal{E})$ (filtering to only SCCs reachable from the SCC $C_1$ containing vertex $1$).
  For each SCC $C \in \mathcal{C}$, split $C$ into $C_{\text{in}} \to C_{\text{out}}$ with parallel edges $(1, -W_C) \parallel (K - 1, 0)$, and connect every $C_{\text{out}} \to T$ with $(K, 0)$ (since walkers can stop at any vertex!).
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - **Initial DAG Potentials**: In the split DAG, every edge $(u, v)$ goes forward in topological order with cost $c(u, v) \in \{-W_C, 0\}$. Compute shortest paths from $S = (C_1)_{\text{in}}$ to all nodes via linear-time topological DP:
    $$\pi(v) = \min_{u \to v} \big(\pi(u) + c(u, v)\big).$$
  - Now every edge in the initial network satisfies $c_\pi(u, v) = c(u, v) + \pi(u) - \pi(v) \ge 0$!
  - Run **exactly $K \le 10$ iterations of Dijkstra** ($O((V + E) \log V)$ per iteration), updating $\pi(v) \gets \pi(v) + \text{dist}(v)$ after each unit augmentation!
- **Step 4 (Complete Solution & Failure Mode)**:
  - Total runtime: $O(V + E)$ for Tarjan SCC + $O(V + E)$ for DAG DP + $10 \times O((V + E) \log V)$ for Dijkstra $\approx 0.25$ seconds for $N = 2 \times 10^5$!
  - *Failure Mode*: Calling SPFA instead of topological DP to initialize $\pi(v)$—on a deep chain DAG of length $2 \times 10^5$ with negative costs, SPFA can degrade to $O(V^2)$ and TLE!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: If a walker enters a Strongly Connected Component (SCC), how many tokens inside that SCC can it collect before leaving? All of them!
  - *Hint 2 (Algebraic)*: After contracting SCCs into a DAG and splitting each SCC into $C_{\text{in}} \to C_{\text{out}}$ with $(1, -W_C) \parallel (K-1, 0)$, why can we avoid SPFA completely despite the negative costs $-W_C$?
  - *Hint 3 (Compilation)*: Compute initial Johnson potentials $\pi$ in $O(V + E)$ by a single topological sweep on the SCC DAG, then run $K \le 10$ rounds of standard Dijkstra!

---

#### Problem 15: Next-Occurrence Hub Sparsification for $K$-Subsequence Cover (`[EN]` Codeforces 818 G `Four Melodies`)
- **Judge URL**: [Codeforces 818 G](https://codeforces.com/problemset/problem/818/G)
- **Statement & Constraints**: Given an array $a_1, a_2, \dots, a_N$ ($4 \le N \le 3000$, $1 \le a_i \le 10^5$), choose $K = 4$ disjoint subsequences (no index $i$ used in two subsequences) maximizing the sum of their lengths, such that any two adjacent elements $a_i, a_j$ ($i < j$) in the same subsequence satisfy $|a_i - a_j| = 1$ or $a_i \equiv a_j \pmod 7$.
- **Step 1 (Diagnostic Signal)**:
  - $K = 4$ disjoint DAG paths maximizing total visited vertices ($N \le 3000$).
  - A naive graph connects every $i < j$ with $|a_i - a_j| = 1$ or $a_i \equiv a_j \pmod 7$, creating $O(N^2) = 4.5 \times 10^6$ edges!
  - **Sparsification Insight**: Instead of connecting $i$ to *all* future $j > i$ with $a_j = v$ (or $a_j \equiv r \pmod 7$), create a **persistent relay chain** of value hubs $H^{\text{val}}_{i, v}$ and mod-7 hubs $H^{\text{mod}}_{i, r}$ that step forward from the first occurrence after $i$ to the next occurrence of the same value/residue!
- **Step 2 (Algebraic Intermediate Form)**:
  For each index $i \in [1, N]$, define:
  - $\text{next\_val}(i, v) := \min \{j > i : a_j = v\}$,
  - $\text{next\_mod}(i, r) := \min \{j > i : a_j \equiv r \pmod 7\}$.
  Instead of $i_{\text{out}}$ jumping directly to all $j > i$, $i_{\text{out}}$ connects only to the **single hub** at $j_1 = \text{next\_val}(i, a_i \pm 1)$ and $j_2 = \text{next\_mod}(i, a_i \bmod 7)$, and the hub at $j$ relays flow to both $j_{\text{in}}$ (to pick $a_j$) and the next hub of the same value/residue $\text{next\_val}(j, a_j)$ / $\text{next\_mod}(j, a_j \bmod 7)$!
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - For each $i \in [1, N]$, create 4 vertices:
    1. $i_{\text{in}}$ and $i_{\text{out}}$ with edge $i_{\text{in}} \to i_{\text{out}}$ of $(\text{cap} = 1, \text{cost} = -1)$.
    2. Value-relay hub $V_i$ (representing "looking for a future element with value $a_i$") and Mod-relay hub $M_i$ (representing "looking for a future element with $a_j \equiv a_i \pmod 7$").
  - Relay and acceptance edges at $i$:
    - $V_i \to i_{\text{in}}$: $(\text{cap} = 1, \text{cost} = 0)$ and $M_i \to i_{\text{in}}$: $(\text{cap} = 1, \text{cost} = 0)$.
    - If $j = \text{next\_val}(i, a_i)$ exists: $V_i \to V_j$ with $(\text{cap} = 4, \text{cost} = 0)$.
    - If $j = \text{next\_mod}(i, a_i \bmod 7)$ exists: $M_i \to M_j$ with $(\text{cap} = 4, \text{cost} = 0)$.
  - Outgoing transitions from $i_{\text{out}}$:
    - To $V_{\text{next\_val}(i, a_i - 1)}$, $V_{\text{next\_val}(i, a_i + 1)}$, and $M_{\text{next\_mod}(i, a_i \bmod 7)}$, each with $(\text{cap} = 1, \text{cost} = 0)$.
  - Starter and Sink edges: $S \to S_{\text{hub}}$ with $(4, 0)$; $S_{\text{hub}} \to i_{\text{in}}$ with $(1, 0)$ and $i_{\text{out}} \to T$ with $(1, 0)$ for all $i$.
- **Step 4 (Complete Solution & Failure Mode)**:
  - Total vertices: $4N + 3 \le 12{,}003$. Total edges: $\le 9N \le 27{,}000$ (down from $4.5 \times 10^6$!).
  - Initialize potentials $\pi$ via DAG DP in $O(N)$ time, then run $4$ Dijkstra augmentations in $O(N \log N)$ total!
  - *Failure Mode*: Forwarding directly from $i_{\text{in}} \to \text{next\_val}(i, a_i)_{\text{in}}$ without separate hub nodes $V_i, M_i$—if you use $i_{\text{in}}$ itself as the relay hub, then a subsequence looking for $a_k + 1 = a_i$ could enter $i_{\text{in}}$ and switch to looking for $a_j \equiv a_i \pmod 7$ **without actually picking $a_i$**! Separate relay hubs $V_i$ and $M_i$ keep value-chains and mod-7 chains completely isolated until an element is actually chosen via $V_i \to i_{\text{in}} \to i_{\text{out}}$!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Why can't we afford to add edges between all valid pairs $(i, j)$ when $N = 3000$? Notice that all elements with the same value $v$ (or the same $v \bmod 7$) form a single forward chain of occurrences!
  - *Hint 2 (Algebraic)*: Create two dedicated relay chains per index $i$: a value-relay node $V_i$ that forwards to the next occurrence of $a_i$, and a mod-7 relay node $M_i$ that forwards to the next occurrence of $a_i \bmod 7$.
  - *Hint 3 (Compilation)*: Connect $i_{\text{out}}$ only to the *first* future occurrences $V_{\text{next}(i, a_i \pm 1)}$ and $M_{\text{next}(i, a_i \bmod 7)}$ ($O(N)$ edges total), and run $K = 4$ augmentations.

---

#### Problem 16: 2D Dominance Poset Transitive Reduction for Collect-Once Walks (`[ZH]` BZOJ 1930 `[SHOI2003] 吃豆豆`)
- **Judge URL**: [Hydro / BZOJ 1930](https://hydro.ac/d/bzoj/p/1930)
- **Statement & Constraints**: There are $N$ beans ($1 \le N \le 2000$) at distinct integer coordinates $(x_i, y_i)$ in $[1, 10^6]^2$. Two Pac-Men ($K = 2$) start at $(0, 0)$ and move monotonically Right and Up ($\Delta x \ge 0, \Delta y \ge 0$) to $(10^6, 10^6)$. Each bean can be eaten at most once. Maximize the total number of beans eaten by the two Pac-Men.
- **Step 1 (Diagnostic Signal)**:
  - Bean $i$ can reach bean $j$ if and only if $x_i \le x_j$ and $y_i \le y_j$ (the 2D Dominance Poset).
  - With $N = 2000$, adding all dominance edges $(i, j)$ creates up to $N(N-1)/2 \approx 2 \times 10^6$ edges, which is too slow for MCMF.
  - **2D Dominance Sparsification (Hasse Diagram / Transitive Reduction)**: Suppose $i \prec k \prec j$ (i.e., $x_i \le x_k \le x_j$ and $y_i \le y_k \le y_j$). Because every bean $k$ has an **uncapacitated $0$-cost bypass arc** $k_{\text{in}} \to k_{\text{out}}$ of $(\text{cap} = \infty, \text{cost} = 0)$ alongside its $(1, -1)$ reward arc, any walk that would have used the direct edge $i_{\text{out}} \to j_{\text{in}}$ can instead route through $i_{\text{out}} \to k_{\text{in}} \xrightarrow{(\infty, 0)} k_{\text{out}} \to j_{\text{in}}$ without losing any capacity or paying any extra cost!
- **Step 2 (Algebraic Intermediate Form)**:
  Sort the beans lexicographically by $(x_i, y_i)$. For a fixed bean $i$, we only need to add edges $i_{\text{out}} \to j_{\text{in}}$ to beans $j > i$ with $y_j \ge y_i$ that are **not dominated by any intermediate bean $k \in (i, j)$**!
  As we scan $j = i + 1, i + 2, \dots, N$ in increasing $x$-order, let $Y_{\min}$ be the smallest $y_k \ge y_i$ seen so far. Bean $j$ is undominated relative to $i$ if and only if $y_i \le y_j < Y_{\min}$! Whenever $y_i \le y_j < Y_{\min}$, we add edge $i_{\text{out}} \to j_{\text{in}}$ and update $Y_{\min} \gets y_j$.
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Split each bean $i \in [1, N]$ into $i_{\text{in}} \to i_{\text{out}}$ with parallel arcs $(1, -1) \parallel (1, 0)$.
  - For each $i \in [1, N]$, scan $j = i + 1 \dots N$ maintaining $Y_{\min} = \infty$: if $y_i \le y_j < Y_{\min}$, add $i_{\text{out}} \to j_{\text{in}}$ with $(\text{cap} = 2, \text{cost} = 0)$ and set $Y_{\min} \gets y_j$.
  - Connect $S \to S_{\text{start}}$ with $(2, 0)$, $S_{\text{start}} \to i_{\text{in}}$ with $(2, 0)$ (or only to undominated minimal beans), and $i_{\text{out}} \to T$ with $(2, 0)$.
- **Step 4 (Complete Solution & Failure Mode)**:
  - The Hasse diagram of random/worst-case 2D points has far fewer active augmenting edges, and since $K = 2$, initializing potentials $\pi$ by DAG DP in $O(V + E)$ followed by **just $2$ runs of Dijkstra** finishes in $< 0.05$ seconds!
  - *Failure Mode*: Performing transitive reduction on a graph where intermediate vertices have **hard capacity $1$** (no bypass arc)—if vertices cannot be passed through a second time, deleting the direct shortcut $i \to j$ when $k$ is saturated would falsely block the second walker! Transitive reduction works here **precisely because** every vertex $k$ has the $(\infty, 0)$ bypass arc!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Why can we delete a direct transition edge $i \to j$ whenever there is an intermediate bean $k$ with $x_i \le x_k \le x_j$ and $y_i \le y_k \le y_j$?
  - *Hint 2 (Algebraic)*: Because bean $k$ has a free bypass edge $k_{\text{in}} \to k_{\text{out}}$ of capacity $\infty$ and cost $0$, routing $i \to k \to j$ is always at least as good as jumping $i \to j$ directly!
  - *Hint 3 (Compilation)*: Sort beans by $(x, y)$; for each $i$, scan $j > i$ maintaining the running minimum $Y_{\min}$ of $y_k \ge y_i$ and only connect $i_{\text{out}} \to j_{\text{in}}$ when $y_i \le y_j < Y_{\min}$.

---

#### Problem 17: Boolean Poset DAG Path Cover with Reset Transitions (`[EN]` Codeforces 1510 B `Button Lock`)
- **Judge URL**: [Codeforces 1510 B](https://codeforces.com/problemset/problem/1510/B)
- **Statement & Constraints**: A lock has $d$ binary toggle buttons ($1 \le d \le 10$, initially all `0`) and a `RESET` button `R` that resets all $d$ buttons to `0`. Pressing a toggle button $b \in [0, d-1]$ sets bit $b$ from `0` to `1` (you cannot toggle a single bit from `1` to `0` without pressing `R`). Given $N$ distinct nonzero target bitmasks ($1 \le N \le 2^d - 1 \le 1023$), find the shortest sequence of button presses (toggles + `R`) that visits every target bitmask at least once, and output the exact sequence of presses.
- **Step 1 (Diagnostic Signal)**:
  - Between two presses of `R`, the active bitmask can only grow monotonically along the Boolean subset poset $u \subsetneq v$ ($u \ \& \ v = u$).
  - Thus the trajectory is partitioned by `R` presses into $K$ chains $C_1, C_2, \dots, C_K$ in the subset DAG!
  - Since every target mask $v$ is a superset of its predecessor in the chain, every target mask $v$ only needs to be covered **once** as a chain vertex (a mask $u \subsetneq v$ visited along the way to $v$ is visited for free!).
- **Step 2 (Algebraic Intermediate Form)**:
  Suppose a chain ends at mask $w$. The number of toggle presses in that chain is $\text{popcount}(w)$, plus $1$ press of `R` after the chain (except the **very last** chain does not need a trailing `R`, saving $1$ press globally!).
  Equivalently:
  - If all $N$ masks were in separate chains of length $1$ (followed by `R`), the baseline cost would be $\text{Base} = \sum_{v} (\text{popcount}(v) + 1) - 1$.
  - Whenever we merge mask $u$ into a larger mask $v$ ($u \subsetneq v$, i.e., $x_{u,v} = 1$), we **eliminate** the chain end at $u$ (and its `R` press, plus the $\text{popcount}(u)$ toggles needed to rebuild $u$ from `0` at the start of $v$'s chain!), saving **exactly $\text{popcount}(u) + 1$** presses!
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - We want a matching $x_{u,v} \in \{0, 1\}$ ($u \subsetneq v$) in the bipartite DAG split $L = \{u_{\text{out}}\}, R = \{v_{\text{in}}\}$ that **maximizes** $\sum_{u \subsetneq v} (\text{popcount}(u) + 1) x_{u,v}$!
  - Connect $S \to u_{\text{out}}$ with $(\text{cap} = 1, \text{cost} = -(\text{popcount}(u) + 1))$.
  - Connect $u_{\text{out}} \to v_{\text{in}}$ with $(\text{cap} = 1, \text{cost} = 0)$ whenever $u \subsetneq v$.
  - Connect $v_{\text{in}} \to T$ with $(\text{cap} = 1, \text{cost} = 0)$ and also add a bypass $u_{\text{out}} \to T$ with $(\text{cap} = 1, \text{cost} = 0)$ (or stop augmenting when shortest path cost $\ge 0$).
- **Step 4 (Complete Solution & Failure Mode)**:
  - Notice that the cost $-(\text{popcount}(u) + 1)$ depends **only on the left vertex $u_{\text{out}}$**! Therefore, we can even solve this without general MCMF by sorting $u \in L$ in **decreasing order of $\text{popcount}(u)$** and running standard Kuhn's augmenting-path DFS (greedy Matroid/Kuhn matching), or running MCMF on $V \le 2050$, $E \le 3^d = 59{,}049$!
  - Reconstruct the chains by following matched edges $u \to v$, emitting the newly set bits of $v \setminus u$, and printing `R` between chains (omitting `R` after the final chain).
  - *Failure Mode*: Forgetting to subtract $1$ for the final chain (which does not need a trailing `R`), or forgetting that continuing $u \to v$ saves $\text{popcount}(u) + 1$ (both the $\text{popcount}(u)$ toggles and the $1$ `R` press!).
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Between two presses of `R`, the sequence of visited target masks forms a chain $u_1 \subsetneq u_2 \subsetneq \dots \subsetneq u_m$ in the subset DAG.
  - *Hint 2 (Algebraic)*: What is the total cost of a chain $u_1 \subsetneq \dots \subsetneq u_m$? It depends *only* on the last element $u_m$: $\text{popcount}(u_m) + 1$! So every matched edge $u \to v$ eliminates $u$ as a chain endpoint and saves $\text{popcount}(u) + 1$.
  - *Hint 3 (Compilation)*: Find a bipartite matching between $u_{\text{out}}$ and $v_{\text{in}}$ ($u \subsetneq v$) maximizing $\sum (\text{popcount}(u) + 1)$ over matched left vertices $u_{\text{out}}$.

---

### Tier 4: Mastery Problems (Problems 18–22)

#### Problem 18: 2D Prefix/Suffix Coordinate Rank Translation (`[JA]` AtCoder Grand Contest 031 E `Snuke the Phantom Thief`)
- **Judge URL**: [AtCoder AGC 031 E](https://atcoder.jp/contests/agc031/tasks/agc031_e)
- **Statement & Constraints**: Given $N \le 80$ jewels at $(x_i, y_i) \in [1, 100]^2$ with value $v_i \in [1, 10^{15}]$ and $M \le 320$ constraints of the form `L(a, b)` ($\le b$ stolen jewels have $x \le a$), `R(a, b)` ($\le b$ have $x \ge a$), `D(a, b)` ($\le b$ have $y \le a$), and `U(a, b)` ($\le b$ have $y \ge a$), find the maximum total value of stolen jewels.
- **Step 1 (Diagnostic Signal)**:
  - $N \le 80$ allows iterating over the exact number of stolen jewels $K \in \{1, \dots, N\}$.
  - Once $K$ is fixed, every prefix/suffix count constraint translates into a coordinate bound on a specific sorted order statistic $x_{(p)}$ or $y_{(q)}$ ($1 \le p, q \le K$).
- **Step 2 (Algebraic Intermediate Form)**:
  As derived in Iteration 86 (Lemma 86.1 & Theorem 86.2), for fixed $K$:
  - `L(a, b)` ($b < K$) $\implies L_X(b+1) \gets \max(L_X(b+1), a + 1)$,
  - `R(a, b)` ($b < K$) $\implies R_X(K-b) \gets \min(R_X(K-b), a - 1)$,
  - Propagate $L_X(p) \gets \max(L_X(p), L_X(p-1))$ and $R_X(p) \gets \min(R_X(p), R_X(p+1))$, and similarly for $[L_Y(q), R_Y(q)]$.
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Build the 4-layer MCMF network:
    - $S \to X_p$ with $(1, 0)$ for $p \in [1, K]$,
    - $X_p \to J_{\text{in}}(i)$ with $(1, 0)$ if $L_X(p) \le x_i \le R_X(p)$,
    - $J_{\text{in}}(i) \to J_{\text{out}}(i)$ with $(1, -v_i)$ for $i \in [1, N]$,
    - $J_{\text{out}}(i) \to Y_q$ with $(1, 0)$ if $L_Y(q) \le y_i \le R_Y(q)$,
    - $Y_q \to T$ with $(1, 0)$ for $q \in [1, K]$.
- **Step 4 (Complete Solution & Failure Mode)**:
  - For each $K \in [1, N]$, if max-flow equals **exactly $K$**, update the global answer with $-\text{min\_cost}$. Overall complexity: $O(N^2 (N + K) N) \approx 5 \times 10^7$ ops.
  - *Failure Mode*: Updating the answer when max-flow $< K$, or failing to propagate $L_X(p) \ge L_X(p-1)$ and $R_X(p) \le R_X(p+1)$ (which is required for the Monotone Interval Uncrossing Theorem 86.2 to hold!).
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Fix the total number of stolen jewels $K \in \{1, \dots, N\}$ and sort their $x$-coordinates as $x_{(1)} \le \dots \le x_{(K)}$.
  - *Hint 2 (Algebraic)*: Express "at most $b$ stolen jewels have $x \ge a$" as an upper bound on a single element $x_{(K-b)} \le a - 1$.
  - *Hint 3 (Compilation)*: Match $X$-slots $1 \dots K$ to jewels $i$ and jewels $i$ to $Y$-slots $1 \dots K$ in a 4-layer MCMF graph, accepting only runs where total flow reaches $K$.

---

#### Problem 19: 4-Hub Dual-Norm Manhattan Linearization (`[JA]` AtCoder Grand Contest 034 D `Manhattan Max Matching`)
- **Judge URL**: [AtCoder AGC 034 D](https://atcoder.jp/contests/agc034/tasks/agc034_d)
- **Statement & Constraints**: Given $N \le 1000$ Red groups $(RX_i, RY_i, RC_i)$ and $N \le 1000$ Blue groups $(BX_j, BY_j, BC_j)$ with $\sum RC_i = \sum BC_j = F \le 10^4$, pair all Red points with Blue points to **maximize** the sum of Manhattan distances $\sum (|RX_i - BX_j| + |RY_i - BY_j|)$.
- **Step 1 (Diagnostic Signal)**:
  - $N \le 1000$ makes the $O(N^2)$ bipartite graph too dense, but the objective is **maximization** of $\ell_1$ distance in $d = 2$ dimensions.
- **Step 2 (Algebraic Intermediate Form)**:
  $$|RX_i - BX_j| + |RY_i - BY_j| = \max_{s_x, s_y \in \{\pm 1\}} \big((s_x RX_i + s_y RY_i) + (-s_x BX_j - s_y BY_j)\big).$$
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Create 4 sign-combination hubs $H_{++}, H_{+-}, H_{-+}, H_{--}$.
  - $S \to R_i$: $(\text{cap} = RC_i, \text{cost} = 0)$.
  - $R_i \to H_{s_x, s_y}$: $(\text{cap} = \infty, \text{cost} = -s_x RX_i - s_y RY_i)$.
  - $H_{s_x, s_y} \to B_j$: $(\text{cap} = \infty, \text{cost} = +s_x BX_j + s_y BY_j)$.
  - $B_j \to T$: $(\text{cap} = BC_j, \text{cost} = 0)$.
- **Step 4 (Complete Solution & Failure Mode)**:
  - Initialize $\pi$ in $O(N)$ via the 4-layer DAG DP (Section 87.3), then run Dijkstra SSP (pushing multiple units along shortest paths) on $V \le 2006$, $E \le 10{,}000$. Answer is $-\text{min\_cost}$.
  - *Failure Mode*: Trying to use this 4-hub trick to **minimize** Manhattan distance (which fails because $\min \max \neq \min \min$).
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: How can we rewrite $|RX_i - BX_j| + |RY_i - BY_j|$ as the maximum of 4 linear expressions where $(RX_i, RY_i)$ and $(BX_j, BY_j)$ are separated?
  - *Hint 2 (Algebraic)*: Since both the outer matching objective and the inner absolute-value identity are $\max$, they commute into a single maximization over paths through 4 intermediate sign hubs!
  - *Hint 3 (Compilation)*: Connect every $R_i$ to 4 hubs $H_{\pm 1, \pm 1}$ and every hub to every $B_j$, reducing $N^2 = 10^6$ edges to $8N = 8000$ edges.

---

#### Problem 20: Parametric MCMF Slope Envelope & LP Duality (`[EN]` Codeforces 1307 G `Cow and Exercise`)
- **Judge URL**: [Codeforces 1307 G](https://codeforces.com/problemset/problem/1307/G)
- **Statement & Constraints**: Given a directed weighted graph with $N$ vertices ($2 \le N \le 50$) and $M$ directed edges ($1 \le M \le N(N-1)$) with weights $w_e \in [1, 10^5]$, you are given $Q$ independent queries ($1 \le Q \le 10^5$). In query $q$, you have a total budget $X_q \in [0, 10^5]$ to increase edge weights: increasing $w_e$ by $\delta_e \ge 0$ (where $\delta_e$ can be any real number) costs $\delta_e$. For each query $q$, find the **maximum possible shortest-path distance** from $1$ to $N$ achievable within budget $\sum_{e \in E} \delta_e \le X_q$.
- **Step 1 (Diagnostic Signal)**:
  - We want to **maximize the shortest path** (an $S$-$T$ distance $d_N - d_1$) by paying $\sum \delta_e \le X$.
  - This is the **LP Dual** of Min-Cost Flow!
- **Step 2 (Algebraic Intermediate Form — Explicit LP Dual Derivation)**:
  Write the Primal LP with distance potentials $d_v$ ($d_1 = 0$) and edge increases $\delta_e \ge 0$:
  $$\max \; d_N \quad \text{s.t.} \quad \begin{cases} d_v - d_u - \delta_e \le w_e & \forall e = (u, v) \in E \quad (\text{dual flow } f_e \ge 0), \\ \sum_{e \in E} \delta_e \le X & (\text{dual scalar } \lambda \ge 0). \end{cases}$$
  Taking the Linear Programming Dual (where $f_e \ge 0$ is the dual variable for edge $e$ and $\lambda \ge 0$ is the dual variable for the budget constraint):
  - Dual constraint for $d_v$: $f$ is a flow from $1$ to $N$ of total volume $F = 1$!
  - Dual constraint for $\delta_e$: $-f_e + \lambda \ge 0 \implies f_e \le \lambda$ for every edge $e \in E$!
  - Dual objective: $\min_{\lambda > 0, \, f} \left( \lambda X + \sum_{e \in E} w_e f_e \right)$.
  Now rescale the flow by $k := 1 / \lambda > 0$ (setting $\tilde{f}_e := f_e / \lambda \in [0, 1]$)! Then $\tilde{f}$ is a standard **unit-capacity flow** ($\tilde{f}_e \le 1$) from $1$ to $N$ of total volume $k = \text{val}(\tilde{f}) > 0$, and the Dual Objective becomes:
  $$\min_{k > 0} \frac{\text{MinCost}(k) + X}{k}!$$
  Furthermore, because $\text{MinCost}(k)$ is piecewise-linear with vertices at **integer flow volumes** $k \in \{1, 2, \dots, F_{\max}\}$, the minimum of the fractional linear function $\frac{\text{MinCost}(k) + X}{k}$ over all real $k > 0$ is always attained at an **integer flow volume $k \in \{1, 2, \dots, F_{\max}\}$**!
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Give every edge $e = (u, v) \in E$ capacity $1$ and cost $w_e$.
  - Run SSP from $1$ to $N$ one unit at a time, recording the cumulative minimum cost $C(k)$ after $k = 1, 2, \dots, F_{\max}$ units of flow ($F_{\max} \le N \le 50$).
  - For each query $X_q$, evaluate $\min_{1 \le k \le F_{\max}} \frac{C(k) + X_q}{k}$ in $O(F_{\max}) = O(N)$ time (or $O(\log N)$ via binary search on the lower hull)!
- **Step 4 (Complete Solution & Failure Mode)**:
  - Precomputation: at most $N = 50$ augmentations on $N = 50$ vertices ($< 5$ ms). Query time: $50$ divisions per query $\times 10^5 = 5 \times 10^6$ ops ($< 20$ ms)!
  - *Failure Mode*: Trying to binary search the answer $D$ and run Min-Cut per query ($Q = 10^5$ queries makes per-query flow impossible!). Recognizing the parametric slope curve $\min_{k \in \mathbb{Z}_{\ge 1}} \frac{C(k) + X}{k}$ decouples the flow precomputation from all $Q$ queries!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Write the problem of maximizing $d_N - d_1$ subject to $d_v - d_u - \delta_e \le w_e$ and $\sum \delta_e \le X$ as a Linear Program, and take its LP Dual!
  - *Hint 2 (Algebraic)*: After rescaling the dual variables so each edge has capacity $1$, show that the dual objective for flow volume $k$ is $\frac{\text{MinCost}(k) + X}{k}$.
  - *Hint 3 (Compilation)*: Run unit-capacity MCMF once from $1$ to $N$ to record $C(k)$ for all integer flow volumes $k = 1, \dots, F_{\max} \le 50$, then answer each query in $O(F_{\max})$ time.

---

#### Problem 21: Parity-Aware 3-Node Vertex Splitting for Endpoint vs. Transit Costs (`[ZH]` Luogu P3159 `[CQOI2012] 交换棋子`)
- **Judge URL**: [Luogu P3159](https://www.luogu.com.cn/problem/P3159)
- **Statement & Constraints**: On an $N \times M$ grid ($1 \le N, M \le 20$), each cell $(r, c)$ initially holds a `0` (white) or `1` (black) token and has a target state `0` or `1`. In one step, you can swap the tokens in two 8-adjacent cells, which uses $1$ swap durability from **both** cells. Cell $(r, c)$ can participate in **at most $m_{r,c}$ swaps** total. Minimize the total number of swaps to transform the initial board into the target board (or output `-1` if impossible).
- **Step 1 (Diagnostic Signal)**:
  - Swapping adjacent black and white tokens is equivalent to routing the initial black tokens along paths to the target black token positions!
  - Along a token's path $u_0 \to u_1 \to \dots \to u_k$:
    - The start cell $u_0$ participates in **1 swap** (exiting $u_0$).
    - The end cell $u_k$ participates in **1 swap** (entering $u_k$).
    - Every **intermediate** cell $u_i$ ($1 \le i < k$) participates in **2 swaps** (1 swap to enter $u_i$, and 1 swap to leave $u_i$)!
- **Step 2 (Algebraic Intermediate Form)**:
  Let $f_{\text{in}}(v)$ and $f_{\text{out}}(v)$ be the total number of token paths entering and leaving cell $v$.
  - If $v$ is balanced (initial = target, including `1` $\to$ `1` which needs $0$ net movement): $f_{\text{in}}(v) = f_{\text{out}}(v)$ and total swaps at $v$ is $f_{\text{in}}(v) + f_{\text{out}}(v) = 2 f_{\text{in}}(v) \le m_v \iff f_{\text{in}}(v) \le \lfloor m_v / 2 \rfloor$.
  - If $v$ starts with `1` and ends with `0` (Source of 1 black token): $f_{\text{out}}(v) = f_{\text{in}}(v) + 1$, and total swaps at $v$ is $f_{\text{in}}(v) + f_{\text{out}}(v) = 2 f_{\text{in}}(v) + 1 \le m_v \iff f_{\text{in}}(v) \le \lfloor (m_v - 1) / 2 \rfloor$ and $f_{\text{out}}(v) \le \lfloor (m_v + 1) / 2 \rfloor$!
  - If $v$ starts with `0` and ends with `1` (Sink of 1 black token): $f_{\text{in}}(v) = f_{\text{out}}(v) + 1$, and total swaps at $v$ is $2 f_{\text{out}}(v) + 1 \le m_v \iff f_{\text{in}}(v) \le \lfloor (m_v + 1) / 2 \rfloor$ and $f_{\text{out}}(v) \le \lfloor (m_v - 1) / 2 \rfloor$!
- **Step 3 (Reverse-Engineering Scratchpad — 3-Node Vertex Split)**:
  Split every cell $v$ into **three** nodes: $v_{\text{in}} \to v_{\text{mid}} \to v_{\text{out}}$!
  - The edge $v_{\text{in}} \to v_{\text{mid}}$ bounds $f_{\text{in}}(v)$, and the edge $v_{\text{mid}} \to v_{\text{out}}$ bounds $f_{\text{out}}(v)$!
  - Specifically, for each cell $v$:
    - If `init[v] == 1` and `target[v] == 0` (token source): connect $S \to v_{\text{mid}}$ with $(1, 0)$, set $\text{cap}(v_{\text{in}} \to v_{\text{mid}}) = \lfloor (m_v - 1)/2 \rfloor$, and $\text{cap}(v_{\text{mid}} \to v_{\text{out}}) = \lfloor (m_v + 1)/2 \rfloor$.
    - If `init[v] == 0` and `target[v] == 1` (token sink): connect $v_{\text{mid}} \to T$ with $(1, 0)$, set $\text{cap}(v_{\text{in}} \to v_{\text{mid}}) = \lfloor (m_v + 1)/2 \rfloor$, and $\text{cap}(v_{\text{mid}} \to v_{\text{out}}) = \lfloor (m_v - 1)/2 \rfloor$.
    - If `init[v] == target[v]`: set $\text{cap}(v_{\text{in}} \to v_{\text{mid}}) = \text{cap}(v_{\text{mid}} \to v_{\text{out}}) = \lfloor m_v / 2 \rfloor$.
  - For every 8-adjacent pair $(u, v)$, add $u_{\text{out}} \to v_{\text{in}}$ with $(\text{cap} = \infty, \text{cost} = 1)$.
- **Step 4 (Complete Solution & Failure Mode)**:
  - Check that total initial `1`s equals total target `1`s, and run MCMF. If max-flow equals the number of mismatched `1`s, return `min_cost`; else `-1`.
  - *Failure Mode*: Using a standard 2-node split $v_{\text{in}} \to v_{\text{out}}$ of capacity $\lfloor m_v / 2 \rfloor$—that fails whenever $m_v$ is **odd** (e.g., $m_v = 1$) at a source or sink cell, because $\lfloor 1 / 2 \rfloor = 0$ would falsely forbid a source cell with $m_v = 1$ from making its single outgoing swap! The 3-node split $v_{\text{in}} \to v_{\text{mid}} \to v_{\text{out}}$ cleanly separates $f_{\text{in}}(v)$ and $f_{\text{out}}(v)$!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: When a black token moves along a path $u_0 \to u_1 \to \dots \to u_k$, how many swaps occur at $u_0$ and $u_k$ versus at an intermediate cell $u_i$?
  - *Hint 2 (Algebraic)*: Express the total swaps at cell $v$ as $f_{\text{in}}(v) + f_{\text{out}}(v) \le m_v$, and use $f_{\text{out}}(v) - f_{\text{in}}(v) \in \{-1, 0, +1\}$ to solve for the exact upper bounds on $f_{\text{in}}(v)$ and $f_{\text{out}}(v)$.
  - *Hint 3 (Compilation)*: Split each cell into three nodes $v_{\text{in}} \to v_{\text{mid}} \to v_{\text{out}}$, connecting $S \to v_{\text{mid}}$ for sources and $v_{\text{mid}} \to T$ for sinks!

---

#### Problem 22: Direction B Bridge — Eliminating the 3-Group MCMF Graph via Prefix/Suffix Regret Heaps (`[JA]` AtCoder Grand Contest 018 C `Coins`)
- **Judge URL**: [AtCoder AGC 018 C](https://atcoder.jp/contests/agc018/tasks/agc018_c)
- **Statement & Constraints**: There are $N = X + Y + Z$ piles of coins ($1 \le X, Y, Z$ and $N \le 10^5$). Pile $i$ contains $A_i$ Gold coins, $B_i$ Silver coins, and $C_i$ Bronze coins ($1 \le A_i, B_i, C_i \le 10^9$). You must choose **exactly $X$ piles** to take Gold from, **exactly $Y$ piles** to take Silver from, and **exactly $Z$ piles** to take Bronze from (each pile used once). Maximize the total number of coins collected.
- **Step 1 (Diagnostic Signal — Direction B: Flow $\to$ Fast Non-Flow Elimination)**:
  - For $N \le 500$, this is a trivial 3-Hub Transportation MCMF problem: $S \to i$ with $(1, 0)$, $i \to H_G$ with $(1, -A_i)$, $i \to H_S$ with $(1, -B_i)$, $i \to H_B$ with $(1, -C_i)$, and $H_G \to T$ $(X, 0)$, $H_S \to T$ $(Y, 0)$, $H_B \to T$ $(Z, 0)$.
  - Since $N = X + Y + Z \le 10^5$, running general MCMF TLEs, so we apply **Direction B (Algebraic Reduction + Priority Queue Simulation)** to solve the exact same flow model in $O(N \log N)$!
- **Step 2 (Algebraic Intermediate Form)**:
  First, assign every pile $i$ to Bronze as a baseline (giving $\text{Base} = \sum_{i=1}^N C_i$), and subtract $C_i$ from $A_i$ and $B_i$:
  $$a_i := A_i - C_i, \qquad b_i := B_i - C_i.$$
  Now we only need to choose two disjoint subsets $I_G, I_S \subseteq \{1, \dots, N\}$ with $|I_G| = X$ and $|I_S| = Y$ maximizing $\sum_{i \in I_G} a_i + \sum_{j \in I_S} b_j$!
  Next, notice that for any pair $i \in I_G$ and $j \in I_S$, we Prefer $i \in I_G, j \in I_S$ over $j \in I_G, i \in I_S$ if and only if:
  $$a_i + b_j \ge a_j + b_i \iff a_i - b_i \ge a_j - b_j \iff A_i - B_i \ge A_j - B_j!$$
- **Step 3 (Reverse-Engineering Scratchpad — Split-Point Separating Theorem)**:
  - Sort all $N$ piles in **decreasing order of $A_i - B_i = a_i - b_i$**.
  - By the exchange inequality above, in the optimal solution, **every** pile in $I_G$ appears to the **left** of **every** pile in $I_S$!
  - Therefore, there exists a split index $k \in [X, N - Y]$ such that:
    - All $X$ Gold piles $I_G$ are chosen from the prefix $\{1, \dots, k\}$ (specifically, the $X$ piles in $\{1, \dots, k\}$ with the largest $a_i = A_i - C_i$!),
    - All $Y$ Silver piles $I_S$ are chosen from the suffix $\{k + 1, \dots, N\}$ (specifically, the $Y$ piles in $\{k + 1, \dots, N\}$ with the largest $b_i = B_i - C_i$!).
- **Step 4 (Complete Solution & Failure Mode)**:
  - Sort piles by $A_i - B_i$ descending in $O(N \log N)$.
  - Sweep $k$ from $X$ to $N - Y$ maintaining a min-heap of size $X$ for the top-$X$ values of $A_i - C_i$ in prefix $1 \dots k$ (computing $\text{Pref}[k]$), and sweep backward from $N - Y$ to $X$ maintaining a min-heap of size $Y$ for the top-$Y$ values of $B_i - C_i$ in suffix $k+1 \dots N$ (computing $\text{Suff}[k]$).
  - Return $\sum_{i=1}^N C_i + \max_{X \le k \le N - Y} (\text{Pref}[k] + \text{Suff}[k])$ in $O(N \log N)$ time!
  - *Failure Mode*: Sorting by $A_i - C_i$ instead of $A_i - B_i$ after eliminating $C_i$—the separating hyperplane between the two active choices $a_i$ and $b_i$ is always $a_i - b_i = (A_i - C_i) - (B_i - C_i) = A_i - B_i$!
- **3-Tier Progressive Hints**:
  - *Hint 1 (Recognition)*: Subtract $C_i$ from every pile (assuming all piles start as Bronze) so you only need to pick $X$ piles with gain $a_i = A_i - C_i$ and $Y$ disjoint piles with gain $b_i = B_i - C_i$.
  - *Hint 2 (Algebraic)*: If you already know which $X + Y$ piles are chosen for Gold $\cup$ Silver, how do you decide which $X$ get Gold and which $Y$ get Silver? Sort by $a_i - b_i = A_i - B_i$!
  - *Hint 3 (Compilation)*: Sort all $N$ piles by $A_i - B_i$ descending; use a prefix min-heap of size $X$ (on $A_i - C_i$) and a suffix min-heap of size $Y$ (on $B_i - C_i$) to test all split points $k \in [X, N - Y]$ in $O(N \log N)$.

---

## Quarantined Template Problems Table (`R-01` to `R-08`)

Per `AGENTS.md` and `flows_research/PLAN.md`, bare algorithm verification problems that require no structural modelling are strictly excluded from the main problem bank and quarantined below as library regression tests:

| Quarantine ID | Judge & Problem Title | Bare Algorithmic Task | Why Quarantined from Textbook Problem Ladders |
| :--- | :--- | :--- | :--- |
| **`R-01`** | Luogu P3381 `【模板】最小费用最大流` | Direct MCMF on given directed graph | Zero modelling; bare SSP / Primal–Dual template check |
| **`R-02`** | Library Checker `Min Cost b-Flow` | Direct $b$-flow with lower/upper bounds | Pure solver verification; no English-to-graph compilation |
| **`R-03`** | LOJ #102 `最小费用流` | Direct Min-Cost Max-Flow | Bare template check |
| **`R-04`** | Library Checker `Assignment Problem` | $N \times N$ Min-Weight Bipartite Perfect Matching | Pure Hungarian / bipartite SSP verification |
| **`R-05`** | Luogu P4014 `[网络流24题] 分配问题` | Bare $N \times N$ min/max bipartite assignment | Trivial 1-to-1 assignment without structural reduction |
| **`R-06`** | Luogu P4015 `[网络流24题] 运输问题` | Bare $M \times N$ Hitchcock transportation problem | Direct transcription of supply/demand matrix |
| **`R-07`** | POJ 2135 `Farm Tour` | $K = 2$ edge-disjoint shortest paths $1 \to N \to 1$ | Bare Suurballe / $K=2$ edge-disjoint MCMF verification |
| **`R-08`** | Luogu P6657 / UOJ #80 `二分图最大权匹配` | Direct Max-Weight Bipartite Matching | Pure Kuhn–Munkres template benchmark |

---

## Multilingual Bibliography (`[EN]` / `[ZH]` / `[JA]`)

1. **`[EN]` Suurballe (1974)** — J. W. Suurballe, *"Disjoint paths in a network"*, Networks, 4(2):125–145, 1974. Foundational theorem proving that $k$ edge/vertex-disjoint paths of minimum total cost can be found via successive shortest augmenting paths with Johnson vertex potentials and residual uncrossing.
2. **`[EN]` Edmonds & Johnson (1973)** — J. Edmonds and E. L. Johnson, *"Matching, Euler tours and the Chinese postman"*, Mathematical Programming, 5(1):88–124, 1973. Definitive treatment of Undirected, Directed, and Eulerian-Orientation Chinese Postman reductions to $T$-joins and Min-Cost Circulations.
3. **`[EN]` Papadimitriou (1976)** — C. H. Papadimitriou, *"On the complexity of edge traversing"*, Journal of the ACM, 23(3):544–554, 1976. Proves that the Mixed Chinese Postman Problem with arbitrary edge duplication is NP-complete, establishing the exact boundary of MCMF Eulerian repair.
4. **`[EN]` Ahuja, Magnanti & Orlin (1993)** — R. K. Ahuja, T. L. Magnanti, and J. B. Orlin, *Network Flows: Theory, Algorithms, and Applications*, Prentice Hall, 1993 (Chapters 9–11 & 14: Minimum Cost Flows, Convex Cost Splitting, and Crew/Napkin Scheduling).
5. **`[ZH]` 刘汝佳 & 陈锋 (2012)** — *《算法竞赛入门经典：训练指南》*, 清华大学出版社. Introduces the Bipartite Day/Night Split for `餐巾计划问题`, backward waiting-time coefficients for `[SCOI2007] 修车`, and flow conservation difference equations.
6. **`[ZH]` NOI 2012 命题报告 (`[NOI2012] 美食节`)** — *中国计算机学会 NOI 2012 试题分析*. Formalizes **Dynamic Lazy Vertex Generation (`动态加点费用流`)**, proving why only $M$ frontier slot nodes need to exist simultaneously in SSP.
7. **`[ZH]` 姜志豪 (2016 国家集训队论文)** — *《网络流的一些建模方法》*, IOI 中国国家候选队论文集, 2016. Systematic taxonomy of vertex splitting, DAG path cover with reset hubs (`星际竞速`, `营救皮卡丘`), parity-aware 3-node splitting (`交换棋子`), and dual-norm hub reductions.
8. **`[JA]` AtCoder AGC 031 E Editorial (`snuke` / `rng_58`, 2019)** — *AtCoder Grand Contest 031 Editorial: E — Snuke the Phantom Thief*. Introduces the 2D Prefix/Suffix Coordinate Rank Translation (`L/R/D/U` $\leftrightarrow$ sorted order statistics $x_{(p)}, y_{(q)}$) and the Monotone Interval Uncrossing Theorem.
9. **`[JA]` AtCoder AGC 034 D Editorial (`rng_58`, 2019)** — *AtCoder Grand Contest 034 Editorial: D — Manhattan Max Matching*. Derives the 4-Hub Sign-Combination Linearization for $\ell_1$ maximization and contrasts $\max\max$ (tractable via hubs) against $\min\max$ (intractable via hubs).
10. **`[JA]` `noshi91` & `maspypy` Flow Modelling Notes (2020–2023)** — *「最小費用流・燃やす埋める・双対性」*, Japanese competitive programming treatises on DAG potential initialization (`ABC 214 H`), parametric MCMF slope hulls (`ABC 247 G`, `CF 1307 G`), and priority-queue elimination (`AGC 018 C`).
