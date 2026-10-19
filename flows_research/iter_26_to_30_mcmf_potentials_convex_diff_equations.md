# Cohort 1 — Wave 3B (Iterations 26–30): Min-Cost Max-Flow (MCMF) I — Potentials, Slope Convexity, Marginal Splitting & Equation-Difference Compilation

> [!IMPORTANT]
> **Cohort & Wave Metadata**
> - **Cohort**: Cohort 1 (Iterations 26–30 of 01–52)
> - **Wave**: Wave 3B — Min-Cost Max-Flow (MCMF) I: Potentials, Slope Convexity, Lower-Bound & Negative-Cycle Elimination, Convex Marginal Splitting, and The Algebraic Equation-Difference Method (`流守恒差分建模法`)
> - **Target Textbook Scope**: Part III (Min-Cost Flows, Convexity & Algebraic Inequality Compilation)
> - **Pedagogical Standard**: Strict compliance with `AGENTS.md` and `flows_research/PLAN.md` **4-Step "Zero Magic Gadgets" Compilation Mandate** (Step 1: Non-Graph Diagnostic Signal $\to$ Step 2: Algebraic / Logical Intermediate Representation $\to$ Step 3: Reverse-Engineering Graph Compilation $\to$ Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples). Zero boilerplate solver dumps; 100% mathematical derivations, algorithmic invariants, complexity contracts, and deep multilingual (`[EN]`, `[ZH]`, `[JA]`) problem modelling.

---

## Executive Overview: Why MCMF Requires an Algebraic-First Architecture

In competitive programming, the transition from Maximum Flow / Minimum Cut (Waves 1A–3A) to **Minimum-Cost Maximum-Flow (MCMF)** introduces a second dimension to every edge: alongside capacity $u(e)$, each edge carries a per-unit linear cost $c(e) \in \mathbb{R}$. While the algorithmic engine appears to be a simple marriage of Ford–Fulkerson augmentation and shortest paths, four profound structural shifts occur:

1. **Optimality is Governed by Residual Cycles, Not Just Residual Paths**:
   In Maximum Flow, a flow $f$ is optimal iff the residual network $G_f$ contains no $s \to t$ path. In Min-Cost Flow, a flow $f$ of volume $|f|$ is cost-optimal among all flows of the same volume iff $G_f$ contains **no directed cycle of strictly negative total cost** (**Iteration 26**). Maintaining this invariant across augmentations via **Johnson Node Potentials $\pi(v)$** is the difference between a provably fast $O(F E \log V)$ Dijkstra engine and an exponential-time SPFA TLE trap.
2. **The Cost Function $C(f)$ is Piecewise-Linear and Convex in Flow Volume $f$**:
   Because successive augmenting paths in the Successive Shortest Path (SSP) algorithm have monotonically non-decreasing costs $d_1 \le d_2 \le \dots \le d_{F_{\max}}$, the minimum cost $C(f)$ as a function of flow volume $f \in [0, F_{\max}]$ is **discrete convex** (**Iteration 27**). This single theorem unlocks two major paradigms:
   - **Min-Cost Feasible Flow (Early Stopping)**: When flow volume is not fixed, stop augmenting the instant the shortest $s \to t$ path cost reaches $\ge 0$.
   - **WQS Binary Search (Aliens Trick) on Flow Volume**: When $N \le 10^5$ and we need the exact $K$-unit min-cost flow $C(K)$, we can binary search a Lagrangian slope penalty $\lambda$ on the source edge and solve an unconstrained min-cost flow via DP or greedy priority queues!
3. **Negative Cycles and Separable Convex Costs Compile to Standard Linear MCMF**:
   - Any network with negative-cost edges or negative-cost cycles can be purified **before** running a single shortest-path query via **Mandatory Initial Saturation (`负权边强制满流消圈法`)** (**Iteration 28**): force every negative edge $(u \to v, [0, u_e], c_e < 0)$ to full capacity $f(e) = u_e$, leaving only its positive-cost residual reversal $(v \to u, [0, u_e], -c_e > 0)$, and repair the resulting node imbalances via the Lower-Bound Circulation engine ($S^*, T^*$).
   - Any separable convex integer cost $g(f_e)$ with non-decreasing first differences $\Delta g(1) \le \Delta g(2) \le \dots \le \Delta g(U)$ compiles into $U$ parallel unit-capacity edges (**Iteration 29**, `凸费用拆边`), turning non-graph combinatorial counting problems like **Maximizing 3-Cycles in a Tournament (`[WC2007] 剪刀石头布`)** into linear MCMF.
4. **Linear Inequality Systems Compile Mechanically into Flow Conservation via Consecutive Equation Differencing (`流守恒差分建模法`)**:
   The hardest non-graph MCMF problems—epitomized by **`[NOI2008] 志愿者招募`** and **`[ICPC NEERC 2016] Delight for a Cat`**—contain no graphs at all, only interval coverage inequalities $\sum_{i : t \in [l_i, r_i]} x_i \ge A_t$. **Iteration 30** eliminates all guesswork: convert inequalities to equations with slack variables $y_t \ge 0$, subtract equation $(t-1)$ from equation $(t)$ ($\Delta E_t = E_t - E_{t-1}$), and watch every contiguous interval variable $x_i$ and slack variable $y_t$ collapse into a single $+1$ (out-flow) and a single $-1$ (in-flow)—reading off the exact MCMF network straight from the algebra!

---

## Iteration 26: Min-Cost Max-Flow (MCMF) Foundations, Negative-Cycle Optimality, Johnson Potentials & Zkw Primal–Dual

### 26.1 Formal Setup & Skew-Symmetric Residual Network

Let $G = (V, E)$ be a directed network with source $s \in V$, sink $t \in V$, integer capacities $u : E \to \mathbb{Z}_{\ge 0}$, and unit shipping costs $c : E \to \mathbb{R}$. A feasible $s$-$t$ flow of volume $|f|$ is a function $f : E \to \mathbb{R}_{\ge 0}$ satisfying:

1. **Capacity Constraint**: $0 \le f(e) \le u(e)$ for all $e \in E$.
2. **Flow Conservation**: For every vertex $v \in V \setminus \{s, t\}$,
   $$\sum_{e \in \delta^+(v)} f(e) - \sum_{e \in \delta^-(v)} f(e) = 0,$$
   while the net outflow at $s$ (and net inflow at $t$) equals $|f|$.

The **total cost** of flow $f$ is the linear functional:
$$C(f) = \sum_{e \in E} c(e) f(e).$$

#### Definition 26.1 (Cost-Augmented Residual Network $G_f$)
Given a feasible flow $f$, each original directed edge $e = (u \to v)$ with capacity $u(e)$ and cost $c(e)$ generates up to two residual arcs in $G_f = (V, E_f)$:
- **Forward Residual Arc** $e^+ = (u \to v)$ with residual capacity $u_f(e^+) = u(e) - f(e)$ and cost $c_f(e^+) = +c(e)$, present whenever $f(e) < u(e)$.
- **Backward (Undo) Residual Arc** $e^- = (v \to u)$ with residual capacity $u_f(e^-) = f(e)$ and **negated cost** $c_f(e^-) = -c(e)$, present whenever $f(e) > 0$.

Why is the backward cost negated? Sending $1$ unit of flow along $e^- = (v \to u)$ physically represents **canceling** $1$ unit of previously committed flow on $e = (u \to v)$, which refunds $c(e)$ dollars—an incremental cost change of $-c(e)$.

---

### 26.2 The Negative-Cycle Optimality Theorem

Before designing any MCMF algorithm, we need a purely local certificate that tells us when a flow $f$ has achieved the minimum possible cost among all flows of the same volume $|f|$.

#### Lemma 26.2 (Circulation Decomposition of Flow Differences)
Let $f$ and $f'$ be two feasible $s$-$t$ flows of the ** exact same volume** $|f| = |f'|$. Define the difference flow $\Delta f$ in the residual network $G_f$ as follows: for each original edge $e = (u \to v)$,
- If $f'(e) > f(e)$, place $\Delta f(e^+) = f'(e) - f(e) > 0$ on the forward residual arc $e^+ = (u \to v) \in E_f$.
- If $f'(e) < f(e)$, place $\Delta f(e^-) = f(e) - f'(e) > 0$ on the backward residual arc $e^- = (v \to u) \in E_f$.

Then $\Delta f$ is a feasible **circulation** in $G_f$ (i.e., $0 \le \Delta f(a) \le u_f(a)$ for all $a \in E_f$, and net outflow is $0$ at every vertex $v \in V$, including $s$ and $t$). Consequently, $\Delta f$ decomposes into a finite collection of directed simple cycles $C_1, C_2, \dots, C_k$ in $G_f$ with positive weights $\gamma_1, \dots, \gamma_k > 0$ ($k \le |E_f|$) such that:
$$C(f') - C(f) = \sum_{a \in E_f} c_f(a) \Delta f(a) = \sum_{i=1}^k \gamma_i \, c_f(C_i),$$
where $c_f(C_i) = \sum_{a \in C_i} c_f(a)$ is the total residual cost around cycle $C_i$.

*Proof.* At every vertex $v \in V$, both $f'$ and $f$ have identical net outflow ($|f|$ at $s$, $-|f|$ at $t$, $0$ elsewhere). Subtracting the two conservation equations gives net outflow $0$ for $\Delta f$ at every $v \in V$. Since $0 \le f'(e) \le u(e)$, we have $f'(e) - f(e) \le u(e) - f(e) = u_f(e^+)$ when $f'(e) > f(e)$, and $f(e) - f'(e) \le f(e) = u_f(e^-)$ when $f'(e) < f(e)$. By standard circulation decomposition (peeling off directed cycles one by one using the minimum residual flow around each cycle), $\Delta f = \sum_{i=1}^k \gamma_i \mathbb{I}_{C_i}$, and linearity of cost yields $C(f') - C(f) = \sum_{i=1}^k \gamma_i c_f(C_i)$. $\blacksquare$

#### Theorem 26.3 (Negative-Cycle Optimality Theorem — Klein 1967)
A feasible $s$-$t$ flow $f$ has minimum cost among all feasible $s$-$t$ flows of volume $|f|$ if and only if the residual network $G_f$ contains **no directed cycle of strictly negative total cost**.

*Proof.*
- **($\implies$ Necessity)**: Suppose $G_f$ contains a directed cycle $C$ with $c_f(C) < 0$. Let $\delta = \min_{a \in C} u_f(a) > 0$ be the bottleneck residual capacity of $C$. Augmenting $f$ by $\delta$ units along $C$ produces a new flow $f'$ that still satisfies capacity constraints, preserves net outflow at every vertex (so $|f'| = |f|$), and has total cost:
  $$C(f') = C(f) + \delta \cdot c_f(C) < C(f),$$
  contradicting the cost-optimality of $f$.
- **($\impliedby$ Sufficiency)**: Suppose $c_f(C) \ge 0$ for every directed cycle $C$ in $G_f$. Let $f'$ be any other feasible flow with $|f'| = |f|$. By Lemma 26.2,
  $$C(f') - C(f) = \sum_{i=1}^k \gamma_i \, c_f(C_i).$$
  Since $\gamma_i > 0$ and $c_f(C_i) \ge 0$ for every $i$, we have $C(f') - C(f) \ge 0$, so $C(f) \le C(f')$. Thus $f$ is globally cost-optimal for volume $|f|$. $\blacksquare$

#### Corollary 26.4 (Preservation of Optimality Along Shortest Augmenting Paths)
Suppose $f$ is a cost-optimal flow of volume $|f|$ (so $G_f$ has no negative cycles), and let $P$ be a **shortest** (minimum-cost) directed path from $s$ to $t$ in $G_f$ with respect to edge costs $c_f$. If we augment $f$ along $P$ by $\delta \in (0, u_f(P)]$ units to obtain $f'$, then $f'$ is a cost-optimal flow of volume $|f| + \delta$.

*Proof.* We will prove this directly in Section 26.3 using **Johnson Node Potentials**, which simultaneously give both the shortest-path optimality proof and the $O(E \log V)$ algorithmic acceleration!

---

### 26.3 Successive Shortest Path (SSP) & Johnson Node Potentials $\pi(v)$

#### The Algorithmic Bottleneck of Naive SSP (SPFA in a Loop)
Even if the original network $G$ has strictly positive edge costs $c(e) > 0$, the very first augmentation along an $s \to t$ path $P$ activates backward residual edges $e^- = (v \to u)$ with **negative costs** $c_f(e^-) = -c(e) < 0$.
Because $G_f$ now has negative-cost edges, naive implementations run the Bellman–Ford / SPFA shortest-path algorithm inside each augmentation step.
> [!WARNING]
> **Why SPFA-Based MCMF is a Mortal Danger on Modern Judges**
> On grid graphs, layered DAGs, and dense bipartite networks, SPFA takes $\Theta(V E)$ time per augmentation in the worst case, degrading total MCMF runtime to $O(F V E)$. Competitive programming problem setters routinely include anti-SPFA test cases (e.g., `CF 164 C`, `LOJ #102`, `QOJ` flow benchmarks). Worse, **we never need SPFA inside the augmentation loop**: by maintaining **Johnson Node Potentials** $\pi : V \to \mathbb{R}$, we can transform all residual edge costs into non-negative **reduced costs** $c_\pi(u,v) \ge 0$ and run **Dijkstra's Algorithm** in $O(E \log V)$ (or $O(V^2)$ for dense graphs) at every single augmentation step!

#### Definition 26.5 (Node Potentials and Reduced Costs)
Let $\pi : V \to \mathbb{R}$ be an arbitrary real-valued function on the vertices, called a **node potential** (or dual variable). For any directed arc $a = (u \to v) \in E_f$ with residual cost $c_f(u,v)$, define its **reduced cost** with respect to $\pi$ as:
$$c_\pi(u, v) := c_f(u, v) + \pi(u) - \pi(v).$$

#### Lemma 26.6 (Telescoping Invariance of Paths and Cycles)
1. **Path Telescoping**: For any directed path $P = (v_0 \to v_1 \to \dots \to v_k)$ from $v_0$ to $v_k$ in $G_f$, the reduced cost of $P$ differs from its true cost $c_f(P)$ only by a constant depending on the endpoints $v_0$ and $v_k$:
   $$c_\pi(P) = \sum_{i=0}^{k-1} \big(c_f(v_i, v_{i+1}) + \pi(v_i) - \pi(v_{i+1})\big) = c_f(P) + \pi(v_0) - \pi(v_k).$$
   In particular, for all $s \to t$ paths $P$, $c_\pi(P)$ and $c_f(P)$ differ by the fixed constant $\pi(s) - \pi(t)$. **Therefore, a path $P$ is a shortest $s \to t$ path under $c_\pi$ if and only if it is a shortest $s \to t$ path under $c_f$!**
2. **Cycle Invariance**: For any directed cycle $C = (v_0 \to v_1 \to \dots \to v_k = v_0)$ in $G_f$, the potentials telescope completely to zero:
   $$c_\pi(C) = c_f(C) + \pi(v_0) - \pi(v_0) = c_f(C).$$
   Consequently, if there exists a potential function $\pi$ such that $c_\pi(u, v) \ge 0$ for all $(u, v) \in E_f$, then $c_f(C) = c_\pi(C) \ge 0$ for every cycle $C$ in $G_f$, immediately certifying by Theorem 26.3 that $f$ is cost-optimal!
3. **Skew-Symmetry Preservation**: For any residual pair $(u \to v)$ and $(v \to u)$,
   $$c_\pi(v, u) = c_f(v, u) + \pi(v) - \pi(u) = -\big(c_f(u, v) + \pi(u) - \pi(v)\big) = -c_\pi(u, v).$$

#### Theorem 26.7 (Potential Update Invariant After Dijkstra Augmentation)
Suppose at step $k$ we have a feasible flow $f$ and a valid node potential $\pi : V \to \mathbb{R}$ satisfying $c_\pi(u,v) \ge 0$ for all $(u,v) \in E_f$.
Let $d_\pi(s, v)$ be the shortest-path distance from $s$ to $v$ in $G_f$ using the non-negative edge weights $c_\pi(u,v) \ge 0$ (computed via Dijkstra's algorithm). Define the updated node potential $\pi' : V \to \mathbb{R}$ for all vertices $v$ reachable from $s$ in $G_f$ by:
$$\pi'(v) := \pi(v) + d_\pi(s, v).$$
Now augment $f$ along any shortest $s \to t$ path $P$ in $G_f$ to obtain $f'$. Then in the new residual network $G_{f'}$, **every residual arc $(u \to v) \in E_{f'}$ satisfies $c_{\pi'}(u, v) \ge 0$**!

*Proof.* Every arc in $E_{f'}$ is either (Case 1) an arc that already existed in $E_f$, or (Case 2) a newly created backward arc $(v \to u)$ where $(u \to v) \in P$ was traversed by the shortest augmenting path $P$.
- **Case 1: $(u \to v) \in E_f$**. By the triangle inequality of shortest-path distances $d_\pi(s, \cdot)$ in $G_f$:
  $$d_\pi(s, v) \le d_\pi(s, u) + c_\pi(u, v).$$
  Rearranging and expanding $c_\pi(u,v) = c_f(u,v) + \pi(u) - \pi(v)$ gives:
  $$0 \le c_\pi(u, v) + d_\pi(s, u) - d_\pi(s, v) = c_f(u, v) + \big(\pi(u) + d_\pi(s, u)\big) - \big(\pi(v) + d_\pi(s, v)\big) = c_{\pi'}(u, v).$$
- **Case 2: $(v \to u) \in E_{f'} \setminus E_f$ is a newly activated backward arc**. Then its forward arc $(u \to v)$ belongs to the shortest $s \to t$ path $P$. Along any shortest path from $s$, the triangle inequality holds with **strict equality**:
  $$d_\pi(s, v) = d_\pi(s, u) + c_\pi(u, v) \implies c_{\pi'}(u, v) = 0.$$
  By skew-symmetry (Lemma 26.6(3)), the newly created backward arc $(v \to u)$ has reduced cost:
  $$c_{\pi'}(v, u) = -c_{\pi'}(u, v) = 0 \ge 0.$$
Thus $c_{\pi'}(a) \ge 0$ holds for every arc $a \in E_{f'}$. By Lemma 26.6(2) and Theorem 26.3, $f'$ contains no negative cycles and is therefore cost-optimal! *(Notice how this simultaneously proves Corollary 26.4 in five lines of algebra!)* $\blacksquare$

#### Recovering the True Augmenting Path Cost from $d_\pi(s, t)$
After running Dijkstra on $c_\pi \ge 0$, what is the true unit cost $c_f(P)$ of the shortest $s \to t$ path $P$? By Lemma 26.6(1):
$$d_\pi(s, t) = c_\pi(P) = c_f(P) + \pi(s) - \pi(t) \implies c_f(P) = d_\pi(s, t) - \pi(s) + \pi(t) = \pi'(t) - \pi'(s).$$
Since $\pi(s) = 0$ and $d_\pi(s, s) = 0$ at every step, $\pi'(s)$ remains identically $0$ throughout the entire algorithm! Thus, **the true unit cost of the shortest augmenting path at step $k$ is simply the updated sink potential $\pi'(t) = \pi(t) + d_\pi(s, t)$!**

---

### 26.4 Initial Potential Computation: Why You Should Almost Never Run SPFA

At the very start of the algorithm ($f_0 = 0$), $E_{f_0} = E$ consists solely of the original forward edges with their given costs $c(u,v)$. To start the Dijkstra loop, we need an initial potential $\pi_0 : V \to \mathbb{R}$ such that for every original edge $(u \to v) \in E$ with $u(e) > 0$:
$$c_{\pi_0}(u, v) = c(u, v) + \pi_0(u) - \pi_0(v) \ge 0 \iff \pi_0(v) \le \pi_0(u) + c(u, v).$$
This condition $\pi_0(v) \le \pi_0(u) + c(u, v)$ is literally the triangle inequality for shortest paths from $s$ in the initial graph $G$! There are **four exhaustive regimes** for initializing $\pi_0$:

| Regime | Condition on Initial Network $G = (V, E)$ | Initialization Method for $\pi_0(v)$ | Initialization Time | SPFA Needed? |
| :--- | :--- | :--- | :--- | :--- |
| **Regime 1: Non-Negative Costs** | $c(u,v) \ge 0$ for all $e \in E$ | Set $\pi_0(v) = 0$ for all $v \in V$. | $O(V)$ | **Never** |
| **Regime 2: Acyclic Network (DAG) with Negative Costs** | $G$ has edges with $c(u,v) < 0$, but the subgraph of positive-capacity edges is a **DAG** (e.g., Bipartite Matching, Interval Graphs, Coordinate/Time-Layered DAGs) | Compute shortest paths from $s$ via **Topological Sort + DAG DP** in topological order $u_1, \dots, u_{|V|}$:<br>$\pi_0(v) = \min_{(u,v) \in E} (\pi_0(u) + c(u,v))$. | $O(V + E)$ | **Never** |
| **Regime 3: Cyclic Network with Negative Edges, No Negative Cycles** | $G$ has directed cycles and negative-cost edges, but no negative-cost cycles | Run a **single** Bellman–Ford / SPFA pass **once** before the loop to set $\pi_0(v) = \text{dist}(s, v)$, or use Regime 4. | $O(V E)$ once | Once before loop (or eliminated via Regime 4) |
| **Regime 4: Network with Negative Cycles (or Arbitrary Negative Edges)** | $G$ contains negative-cost cycles (or we want to avoid SPFA in Regime 3 completely) | **Mandatory Initial Saturation (`负权边强制满流消圈法`, Iteration 28)**: Pre-saturate all $c(e) < 0$ edges so all residual costs become $\ge 0$, then set $\pi_0(v) = 0$! | $O(V + E)$ setup | **Never** |

> [!TIP]
> **The Golden Rule of DAG Potential Initialization (Regime 2)**
> Over 80% of competitive programming MCMF problems with negative edge costs (such as Maximum-Weight Bipartite Matching where weights are negated to $-w_{ij} < 0$, or interval packing problems like `CF 164 C — Machine Programming` and `Luogu P3358`) are **DAGs** in their initial state ($f_0 = 0$) before any backward residual arcs exist!
> On a DAG, shortest paths with negative edge weights can be computed in **strict $O(V + E)$ linear time** via Kahn's topological sort + DP:
> $$\pi_0(s) = 0, \qquad \pi_0(v) = \min_{(u \to v) \in E} \big(\pi_0(u) + c(u, v)\big).$$
> Combined with Dijkstra for each subsequent augmentation, your MCMF solver is **100% immune to anti-SPFA test cases** and runs in deterministic $O(V + E + F E \log V)$ (or $O(F V^2)$ for dense graphs)!

---

### 26.5 SSP vs. Zkw Primal–Dual (Multi-Path Blocking Flow on Tight Edges)

Can we combine Johnson potentials with Dinic's multi-path blocking-flow DFS? Yes—this is the **Primal–Dual Algorithm** (popularized in `[ZH]` competitive programming by **Zkw / 张昆玮** as the **Zkw Cost Flow `zkw费用流`**).

#### How Zkw Primal–Dual Works
At each phase, given valid potentials $\pi$ with $c_\pi(u,v) \ge 0$:
1. **Tight (Admissible) Subgraph $E_0$**: Define the subgraph of zero-reduced-cost edges:
   $$E_0 = \big\{(u \to v) \in E_f : u_f(u,v) > 0 \text{ and } c_\pi(u, v) = 0\big\}.$$
   Any $s \to t$ path composed entirely of edges in $E_0$ has reduced cost $c_\pi(P) = 0$, so by Lemma 26.6(1) it is a shortest augmenting path of true cost $\pi(t) - \pi(s)$!
2. **Blocking-Flow DFS Phase**: Just like Dinic's algorithm, run multi-path DFS (with `vis[u]` flags to prevent looping on zero-reduced-cost cycles!) to push a maximal blocking flow from $s$ to $t$ using only edges in $E_0$. Notice that augmenting along edges with $c_\pi(u,v) = 0$ creates backward edges $(v \to u)$ with $c_\pi(v, u) = -0 = 0$, so **potentials $\pi$ do not need to be updated during the entire DFS phase**!
3. **Relabel / Dijkstra Phase**: Once $t$ is no longer reachable from $s$ in $E_0$, run Dijkstra (or a single-step cut relabeling $\Delta = \min_{u \in S, v \notin S} c_\pi(u,v)$) to update potentials $\pi'(v) = \pi(v) + d_\pi(s, v)$, bringing new edges into $E_0$ for the next blocking-flow DFS phase.

#### Architectural Comparison: When to Use SSP+Dijkstra vs. Zkw Primal–Dual

| Feature | SSP + Dijkstra (Single Shortest Path per Step) | Zkw Primal–Dual (Dinic Blocking DFS on $c_\pi = 0$) |
| :--- | :--- | :--- |
| **Best-Case Regime** | Sparse graphs with small total flow $F$, or networks where each shortest path has a distinct cost (so $E_0$ only ever has $1$ path per cost level). | **Dense graphs with large capacities / many tied-cost paths and short $s$-$t$ distances** (e.g., convex marginal splitting `[WC2007] 剪刀石头布`, bipartite degree matching). |
| **Per-Augmentation Cost** | One Dijkstra call $O(E \log V)$ (or $O(V^2)$) per augmenting path. | Multiple paths sharing the same cost $\pi(t)$ are augmented in a single DFS pass without re-running Dijkstra! |
| **Early Stopping & Slope Tracking ($C(f)$)** | **Exact unit-by-unit / path-by-path slope profile** $d_1 \le d_2 \le \dots \le d_K$ immediately available. | Naturally groups augmentations by distinct cost plateaus $\pi(t)$; still gives exact breakpoints of $C(f)$. |
| **Fatal Failure Mode / Trap** | If $F$ is huge ($F \ge 10^5$) and capacities are $1$ with identical costs, running Dijkstra $F$ times costs $O(F E \log V)$ instead of pushing all tied paths at once. | **The Exponential Zero-Cost DAG Trap**: Because $E_0$ can contain zero-cost cycles (unlike Dinic's strict level graph $d(v) = d(u)+1$), Zkw uses a boolean `vis[u]` array during DFS. If `vis[u]` is cleared on backtrack (or if $E_0$ is a long diamond DAG with zero-cost paths of varying lengths), DFS can re-explore dead-end branches exponentially many times unless dead-end vertices keep `vis[u] = true` for the entire phase! |

> [!CAUTION]
> **Implementation Contract for Zkw DFS (`vis[u]` Retention Rule)**
> In Zkw Primal–Dual, when a DFS call `dfs(u, pushed)` finishes exploring vertex $u$ and fails to saturate `pushed` (i.e., $u$ cannot push any more flow to $t$ in $E_0$), you **MUST NOT** reset `vis[u] = false` (or you must advance `cur[u]` current-arc pointers to the end)! Resetting `vis[u] = false` on a dead-end vertex in a DAG of zero-reduced-cost edges causes $O(2^{V})$ exponential blowup on simple diamond chains. Only vertices that still have remaining outgoing capacity to $t$ may be revisited in the same phase.

---

### 26.6 4-Step Compilation, Hand-Checkable Trace & Broken Gadget Counterexamples

#### Step-by-Step Numerical Trace: DAG Topological Potentials + Dijkstra Augmentation
Consider a 4-vertex DAG with $V = \{s, a, b, t\}$ and 5 edges (written as $(u \to v, \text{cap}, \text{cost})$):
- $e_1 = (s \to a, 2, -5)$
- $e_2 = (s \to b, 2, -2)$
- $e_3 = (a \to b, 1, +1)$
- $e_4 = (a \to t, 1, +4)$
- $e_5 = (b \to t, 2, +2)$

Notice that $e_1$ and $e_2$ have **negative costs**, so naive Dijkstra at $f_0 = 0$ with $\pi_0 = 0$ is illegal. However, $G$ is a DAG with topological order $(s, a, b, t)$!

1. **Initial Potential Computation via DAG DP ($O(V+E)$, zero SPFA)**:
   - $\pi_0(s) = 0$
   - $\pi_0(a) = \pi_0(s) + c(s, a) = 0 + (-5) = -5$
   - $\pi_0(b) = \min\big(\pi_0(s) + c(s, b),\; \pi_0(a) + c(a, b)\big) = \min(0 - 2,\; -5 + 1) = \min(-2, -4) = -4$
   - $\pi_0(t) = \min\big(\pi_0(a) + c(a, t),\; \pi_0(b) + c(b, t)\big) = \min(-5 + 4,\; -4 + 2) = \min(-1, -2) = -2$

   Let us check all initial reduced costs $c_{\pi_0}(u,v) = c(u,v) + \pi_0(u) - \pi_0(v)$:
   - $c_{\pi_0}(s, a) = -5 + 0 - (-5) = 0 \ge 0$
   - $c_{\pi_0}(s, b) = -2 + 0 - (-4) = +2 \ge 0$
   - $c_{\pi_0}(a, b) = +1 + (-5) - (-4) = 0 \ge 0$
   - $c_{\pi_0}(a, t) = +4 + (-5) - (-2) = +1 \ge 0$
   - $c_{\pi_0}(b, t) = +2 + (-4) - (-2) = 0 \ge 0$
   Every single reduced cost is non-negative!

2. **Augmentation 1 (Dijkstra on $c_{\pi_0} \ge 0$)**:
   - Shortest distances $d_{\pi_0}(s, \cdot)$: $d_{\pi_0}(s, s) = 0$, $d_{\pi_0}(s, a) = 0$, $d_{\pi_0}(s, b) = 0$ (via $s \to a \to b$), $d_{\pi_0}(s, t) = 0$ (via $P_1 = s \to a \to b \to t$).
   - Update potentials: $\pi_1(v) = \pi_0(v) + d_{\pi_0}(s, v) = (0, -5, -4, -2)$.
   - True path cost of $P_1$: $\pi_1(t) - \pi_1(s) = -2$ (check: $-5 + 1 + 2 = -2$).
   - Bottleneck capacity of $P_1$: $\min(2, 1, 2) = 1$. Push $\delta_1 = 1$ unit along $s \to a \to b \to t$. Total flow $|f| = 1$, cost $C(1) = -2$.
   - In $G_{f_1}$, edge $(a \to b)$ is saturated and replaced by backward edge $(b \to a, \text{cap } 1, \text{cost } -1)$, whose reduced cost under $\pi_1$ is $c_{\pi_1}(b, a) = -1 + (-4) - (-5) = 0 \ge 0$.

3. **Augmentation 2 (Dijkstra on $c_{\pi_1} \ge 0$)**:
   - Residual forward arcs from $s$: $(s \to a, \text{cap } 1, c_{\pi_1}=0)$ and $(s \to b, \text{cap } 2, c_{\pi_1}=2)$.
   - From $a$: only $(a \to t, \text{cap } 1, c_{\pi_1}=1)$ remains.
   - From $b$: $(b \to t, \text{cap } 1, c_{\pi_1}=0)$ and $(b \to a, \text{cap } 1, c_{\pi_1}=0)$.
   - Dijkstra distances $d_{\pi_1}(s, \cdot)$:
     $d_{\pi_1}(s, s) = 0$, $d_{\pi_1}(s, a) = 0$, $d_{\pi_1}(s, t) = 0 + 1 = 1$ (via $P_2 = s \to a \to t$), $d_{\pi_1}(s, b) = 2$ (via $s \to b$).
   - Update potentials: $\pi_2(v) = \pi_1(v) + d_{\pi_1}(s, v) = (0 + 0,\; -5 + 0,\; -4 + 2,\; -2 + 1) = (0, -5, -2, -1)$.
   - True path cost of $P_2$: $\pi_2(t) = -1$ (check: $-5 + 4 = -1$).
   - Push $\delta_2 = 1$ unit along $P_2 = s \to a \to t$. Total flow $|f| = 2$, cost $C(2) = -2 + (-1) = -3$.

4. **Augmentation 3 (Dijkstra on $c_{\pi_2} \ge 0$)**:
   - Under $\pi_2 = (0, -5, -2, -1)$, check the reduced cost of $(s \to b)$: $c_{\pi_2}(s, b) = -2 + 0 - (-2) = 0$, and $(b \to t)$: $c_{\pi_2}(b, t) = +2 + (-2) - (-1) = +1$, while backward $(b \to a)$ has $c_{\pi_2}(b, a) = -1 + (-2) - (-5) = +2 \ge 0$!
   - Shortest path is $P_3 = s \to b \to t$ with $d_{\pi_2}(s, t) = 0 + 1 = 1$, true cost $\pi_3(t) = -1 + 1 = 0$ (check: $-2 + 2 = 0$).
   - Push $\delta_3 = 1$ unit along $P_3 = s \to b \to t$. Total flow $|f| = 3$ (Max Flow!), total cost $C(3) = -3 + 0 = -3$.

#### Three Classic Broken-Gadget Counterexamples in Iteration 26
1. **Broken Gadget A — Updating $\pi(v)$ Only Along the Augmenting Path $P$ Instead of All Reachable Vertices**:
   Suppose in Augmentation 2 above, a programmer only updates $\pi_2(v) \gets \pi_1(v) + d_{\pi_1}(s, v)$ for vertices $v \in P_2 = \{s, a, t\}$, leaving $\pi_2(b) = \pi_1(b) = -4$. Then on the backward edge $(t \to b)$ (created when $b \to t$ had flow $1$), its reduced cost becomes:
   $$c_{\pi_2}(t, b) = -2 + \pi_2(t) - \pi_2(b) = -2 + (-1) - (-4) = +1,$$
   while on $(b \to t)$ it is $c_{\pi_2}(b, t) = +2 + (-4) - (-1) = -1 < 0$! A **negative reduced cost $-1$** appears on $(b \to t)$, corrupting Dijkstra in Augmentation 3! **Rule**: You MUST update $\pi'(v) = \pi(v) + d_\pi(s, v)$ for **every vertex $v$ reached by Dijkstra**, not just vertices on the chosen $s \to t$ path.
2. **Broken Gadget B — Setting Backward Edge Cost to $+c(e)$ or $0$ Instead of $-c(e)$**:
   If $c_f(e^-)$ is set to $0$ instead of $-c(e)$, the solver cannot refund expensive edges when rerouting flow around a newly discovered shortcut (Suurballe / negative-cost cancellation fails). For example, if $P_1$ uses an edge of cost $+10$ and a later augmenting path traverses its reverse arc to split $P_1$ into two disjoint paths of total cost $4$, setting $c_f(e^-) = 0$ charges $10 + 4 = 14$ instead of $10 - 10 + 4 = 4$.
3. **Broken Gadget C — Adding Parallel Reverse Edges in Undirected Min-Cost Flow**:
   To model an **undirected** edge $\{u, v\}$ with capacity $U$ and traversal cost $c \ge 0$ in MCMF, you **cannot** combine $(u \to v)$ and $(v \to u)$ into a single adjacency pair where the initial backward capacity is $U$ with cost $-c$! Doing so creates an immediate negative cycle $u \to v \to u$ of cost $c + (-c) = 0$ or $-2c < 0$. Instead, an undirected edge of capacity $U$ and cost $c \ge 0$ MUST be compiled into **two independent directed edges** $(u \to v, \text{cap } U, \text{cost } +c)$ and $(v \to u, \text{cap } U, \text{cost } +c)$, each with its own initially zero-capacity backward residual arc of cost $-c$. (Why doesn't the solver send flow on both $(u \to v)$ and $(v \to u)$ simultaneously? Because if $c > 0$, pushing flow on both creates a negative cycle of cost $-2c$ in the residual graph, which SSP never does!)

---

## Iteration 27: Slope Convexity of $C(f)$, Min-Cost Feasible Flow (Variable Flow Volume), & WQS Binary Search on Flow

### 27.1 The Slope Convexity Theorem for Minimum-Cost Flows

Let $F_{\max}$ be the maximum $s$-$t$ flow value in network $G$. For every flow volume $f \in [0, F_{\max}]$, define the **minimum-cost flow profile function**:
$$C(f) := \min\Big\{ \sum_{e \in E} c(e) \phi(e) \;\Big|\; \phi \text{ is a feasible } s\text{-}t \text{ flow of volume } |\phi| = f \Big\}.$$

#### Theorem 27.1 (Monotonicity of Augmenting Path Costs & Convexity of $C(f)$)
Suppose the initial network $G$ contains no negative-cost cycles (so $f_0 = 0$ is optimal for volume $0$). Let $P_1, P_2, \dots, P_K$ be the sequence of shortest augmenting paths found by the Successive Shortest Path (SSP) algorithm, with unit path costs $d_1, d_2, \dots, d_K$ and bottleneck capacities $\delta_1, \delta_2, \dots, \delta_K$. Then:
1. **Slope Monotonicity**: The unit augmenting path costs are monotonically non-decreasing:
   $$d_1 \le d_2 \le \dots \le d_K.$$
2. **Piecewise-Linear Convexity**: The function $C : [0, F_{\max}] \to \mathbb{R}$ is continuous, piecewise-linear, and **convex** on $[0, F_{\max}]$, with slope equal to $d_k$ on the $k$-th flow interval $\big[\sum_{j < k} \delta_j,\; \sum_{j \le k} \delta_j\big]$.

We provide **two independent proofs**—one via Johnson potentials (analytic) and one via flow difference decomposition (combinatorial)—because each proof illuminates a different facet of MCMF structure.

*Proof 1 (Via Johnson Potentials — 3 Lines).*
At the beginning of step $k$, we hold a valid potential $\pi_{k-1}$ with $\pi_{k-1}(s) = 0$ and $\pi_{k-1}(t) = d_{k-1}$ (as shown in Section 26.3, the true cost of path $P_{k-1}$ equals the updated sink potential $\pi_{k-1}(t)$), and all residual edges in $G_{f_{k-1}}$ have non-negative reduced costs $c_{\pi_{k-1}}(u,v) \ge 0$.
In step $k$, Dijkstra computes the shortest reduced-cost distance $d_{\pi_{k-1}}(s, t)$ on non-negative weights $c_{\pi_{k-1}} \ge 0$, which must therefore satisfy:
$$d_{\pi_{k-1}}(s, t) \ge 0.$$
The true cost $d_k$ of the new shortest path $P_k$ is:
$$d_k = \pi_k(t) = \pi_{k-1}(t) + d_{\pi_{k-1}}(s, t) = d_{k-1} + d_{\pi_{k-1}}(s, t) \ge d_{k-1}.$$
Since the marginal derivative $C'(f) = d_k$ is non-decreasing across successive intervals, $C(f)$ is piecewise-linear and convex! $\blacksquare$

*Proof 2 (Via Symmetric Difference of Optimal Integer Flows).*
For any integer $v \in \{1, \dots, F_{\max} - 1\}$, let $\phi_{v-1}, \phi_v, \phi_{v+1}$ be cost-optimal flows of volumes $v-1, v, v+1$. Consider the residual difference $\Delta^+ = \phi_{v+1} - \phi_v$ (which has net outflow $+1$ at $s$ and $-1$ at $t$ in $G_{\phi_v}$) and the reversed difference $\Delta^- = \phi_{v-1} - \phi_v$ (which has net outflow $-1$ at $s$ and $+1$ at $t$ in $G_{\phi_v}$, or equivalently is a $t \to s$ flow of volume $1$ in $G_{\phi_v}$).
Wait—even simpler: compare the midpoint sum $\phi_{v+1} + \phi_{v-1}$ against $2 \phi_v$. In the superposition of $\phi_{v+1}$ and $\phi_{v-1}$, the total flow volume is $(v+1) + (v-1) = 2v$. By flow decomposition on $\phi_{v+1} - \phi_{v-1}$ (which is a valid flow of volume $2$ in $G_{\phi_{v-1}}$), we can decompose $\phi_{v+1} - \phi_{v-1}$ into **two** unit $s \to t$ paths $Q_1, Q_2$ plus a circulation $W$ in $G_{\phi_{v-1}}$. Since $\phi_{v+1}$ is optimal, $W$ has non-negative cost (otherwise removing $W$ from $\phi_{v+1}$ improves $\phi_{v+1}$). Adding $Q_1$ alone to $\phi_{v-1}$ gives a valid flow $\psi_1 = \phi_{v-1} + Q_1$ of volume $v$, and subtracting $Q_1$ from $\phi_{v+1}$ gives a valid flow $\psi_2 = \phi_{v+1} - Q_1$ of volume $v$. By optimality of $\phi_v$ for volume $v$:
$$2 C(v) \le C(\psi_1) + C(\psi_2) = C(\phi_{v-1} + Q_1) + C(\phi_{v+1} - Q_1) = C(v-1) + C(v+1),$$
which is the exact discrete convexity inequality $C(v+1) - C(v) \ge C(v) - C(v-1)$! $\blacksquare$

---

### 27.2 Min-Cost Feasible Flow (Variable Flow Volume / Maximum-Profit Flow)

#### 1. The Non-Graph Diagnostic Signal
In many problems, we are **not** required to route the maximum possible flow $F_{\max}$. Instead:
- Each matched pair / routed unit of flow generates a **profit** $w_i > 0$ (which we negate to a negative cost $-w_i < 0$) and incurs downstream operational costs $+c_j > 0$.
- We want to choose **how many units of flow $f \in [0, F_{\max}]$ to route** so as to **minimize $C(f)$** (equivalently, maximize net profit $-C(f)$) over all $f \in [0, F_{\max}]$.

#### 2. The Algebraic & Algorithmic Consequence of Convexity
Because $C(f)$ is convex with slopes $d_1 \le d_2 \le \dots \le d_K$:
- As long as $d_k < 0$, every additional unit of flow **strictly decreases** the total cost $C(f)$.
- The very first time an augmenting path has $d_k \ge 0$, Theorem 27.1 guarantees that **every future augmenting path $P_{k+1}, P_{k+2}, \dots$ will also have cost $d_j \ge d_k \ge 0$**!
- Therefore, the global minimum of $C(f)$ over $f \in [0, F_{\max}]$ is achieved by **stopping the SSP loop immediately** as soon as the shortest $s \to t$ path cost $d_k = \pi'(t) - \pi'(s)$ satisfies:
  - $d_k \ge 0$ (if we want the **minimum-volume** flow among all global cost-minimizers), or
  - $d_k > 0$ (if we want the **maximum-volume** flow among all global cost-minimizers, e.g., when problem statements ask to "maximize total profit, and break ties by maximizing the number of matched pairs").

#### 3. Structural Equivalence to a Free Bypass Edge $s \to t$
What if you only have a black-box solver that computes fixed-volume Min-Cost Max-Flow? You can still reduce Variable-Volume Min-Cost Flow to fixed-volume MCMF:
Add a direct **bypass edge** $(s \to t)$ with capacity $U_{\text{max}}$ and cost $0$, and attach a super-source $S_0 \to s$ with capacity $U_{\text{max}}$ and cost $0$. Any flow unit that would have cost $> 0$ in the main network will instead route along the $0$-cost bypass edge $(s \to t)$! However, **early stopping inside SSP** ($d_k \ge 0$) is strictly faster because it avoids all positive-cost augmentations completely.

#### 4. The Fractional / Threshold-Constrained Stopping Variant (`[SDOI2016] 数字配对`)
A subtle cousin of Min-Cost Feasible Flow occurs when the problem asks to **maximize the flow volume $f$** subject to a **budget constraint** on the total cost:
$$\text{maximize } f \quad \text{subject to} \quad C(f) \le 0.$$
Notice the difference!
- Here, we do **not** stop when the marginal slope $d_k > 0$. Instead, we first accumulate all negative-cost paths ($d_k \le 0$), building up a large negative cost reserve ("profit buffer") $C_{\text{cur}} \le 0$.
- Then, as we continue augmenting along positive-cost paths ($d_k > 0$), $C_{\text{cur}}$ increases toward $0$. Since $d_k$ is non-decreasing, we greedily take positive-cost shortest paths in order of SSP until the next path $P_k$ of bottleneck $\delta_k$ and unit cost $d_k > 0$ would push $C_{\text{cur}} + \delta_k d_k > 0$.
- On that final threshold path $P_k$, we take only the maximum affordable integer units:
  $$\Delta f_{\text{final}} = \left\lfloor \frac{-C_{\text{cur}}}{d_k} \right\rfloor,$$
  and terminate! Convexity of $C(f)$ guarantees that this greedy SSP prefix achieves the exact global maximum flow volume satisfying $C(f) \le 0$.

---

### 27.3 WQS Binary Search (Aliens Trick / Lagrangian Duality) on Flow Volume $f$

#### Direction B Paradigm: Eliminating the Capacity Constraint $f = K$ via Convexity
Suppose a problem asks for the minimum cost $C(K)$ of routing **exactly $K$ units of flow** (e.g., selecting $K$ disjoint paths in a tree `[八省联考 2018] 林克卡特树`, matching $K$ intervals/tasks `CF 802 O — April Fools' Problem (hard)`, or throwing $A$ Pokéballs and $B$ Ultraballs `CF 739 E — Gosha is hunting`), where $N \le 10^5$ is too large to run $K$ steps of SSP!

Because Theorem 27.1 proves that $C(f)$ is convex on $f \in [0, F_{\max}]$, the graph of $(f, C(f))$ has a supporting hyperplane at every integer $K \in [0, F_{\max}]$.

```
Cost C(f)
  ^
  |                        /  slope d_4
  |                       o
  |                      /  slope d_3
  |                o----o  <-- collinear plateau (d_2 = d_3 = lambda*)
  |       slope d_1 \
  |        o         o
  +-----------------------------> Flow volume f
           0   1   2    3   4
```

#### Theorem 27.2 (Lagrangian Supporting Hyperplane / WQS Duality on Flow Volume)
For any slope penalty $\lambda \in \mathbb{R}$, define the unconstrained Lagrangian minimum:
$$g(\lambda) := \min_{f \in [0, F_{\max}]} \big( C(f) - \lambda f \big).$$
In flow terms, subtracting $\lambda f$ is equivalent to **adding $-\lambda$ to the cost of every edge leaving the source $s$** (or adding a super-source edge $S_0 \to s$ with capacity $\infty$ and unit cost $-\lambda$), and solving the **unconstrained Variable-Volume Min-Cost Feasible Flow** problem (where we take all augmenting paths with original cost $d_k \le \lambda$, i.e., shifted cost $d_k - \lambda \le 0$)!
1. **Monotonicity of Optimal Flow Volume**: Let $f_{\min}(\lambda)$ and $f_{\max}(\lambda)$ denote the minimum and maximum flow volumes $f$ that achieve the minimum in $g(\lambda)$:
   - $f_{\min}(\lambda) = \text{total flow of all augmenting paths with } d_k < \lambda$ (strict inequality: stop when $d_k - \lambda \ge 0$),
   - $f_{\max}(\lambda) = \text{total flow of all augmenting paths with } d_k \le \lambda$ (weak inequality: stop when $d_k - \lambda > 0$).
   Both $f_{\min}(\lambda)$ and $f_{\max}(\lambda)$ are **monotonically non-decreasing** functions of $\lambda$.
2. **Exact Recovery at Target Volume $K$**: For any target volume $K \in [0, F_{\max}]$, there exists an optimal slope $\lambda^* = d_k$ (specifically, the slope of the segment containing $K$) such that:
   $$f_{\min}(\lambda^*) \le K \le f_{\max}(\lambda^*).$$
   For this $\lambda^*$, every integer $f \in [f_{\min}(\lambda^*), f_{\max}(\lambda^*)]$ lies on the same collinear segment of slope $\lambda^*$ on the convex hull of $C(f)$, so:
   $$C(K) = g(\lambda^*) + \lambda^* \cdot K.$$

#### Handling Collinear Segments (The Classic WQS Tie-Breaking Contract)
What happens if multiple augmenting paths have the **exact same cost** $d_k = d_{k+1} = \dots = d_r = \lambda^*$?
Then at $\lambda = \lambda^*$, the shifted costs of these paths are all $d_j - \lambda^* = 0$.
- If our unconstrained solver breaks $0$-cost ties by **maximizing** the number of flow units taken (i.e., computing $f_{\max}(\lambda)$), we binary search for the **smallest** $\lambda$ such that $f_{\max}(\lambda) \ge K$.
- At that critical $\lambda^*$, even if $f_{\max}(\lambda^*) > K$, we must **NOT** compute $C(K)$ as $\text{TrueCost}(f_{\max}(\lambda^*))$! Instead, we record the penalized optimum $g(\lambda^*) = C(f_{\max}(\lambda^*)) - \lambda^* f_{\max}(\lambda^*)$ and recover:
  $$C(K) = g(\lambda^*) + \lambda^* \cdot K = C(f_{\max}(\lambda^*)) - \lambda^* \big(f_{\max}(\lambda^*) - K\big).$$
  Because every unit of flow between $f_{\min}(\lambda^*)$ and $f_{\max}(\lambda^*)$ has marginal cost exactly $\lambda^*$, subtracting $\lambda^*(f_{\max}(\lambda^*) - K)$ removes the excess $(f_{\max}(\lambda^*) - K)$ collinear flow units without needing to reconstruct which subset of tied paths to drop!

---

### 27.4 4-Step Compilation, Hand-Checkable Trace & Broken Gadget Counterexamples

#### Hand-Checkable Trace of $C(f)$, Early Stopping, and Collinear WQS Recovery
Suppose an MCMF network has maximum flow $F_{\max} = 5$, and its 5 unit-capacity augmenting paths have costs:
$$(d_1, d_2, d_3, d_4, d_5) = (-6, -2, +3, +3, +7).$$
Let us trace all three algorithms on this profile:

1. **Full Convex Cost Profile $C(f)$**:
   - $C(0) = 0$
   - $C(1) = -6$ (slope $d_1 = -6$)
   - $C(2) = -6 + (-2) = -8$ (slope $d_2 = -2$)
   - $C(3) = -8 + 3 = -5$ (slope $d_3 = +3$)
   - $C(4) = -5 + 3 = -2$ (slope $d_4 = +3$)
   - $C(5) = -2 + 7 = +5$ (slope $d_5 = +7$)
   Notice the collinear plateau on $f \in [2, 4]$ where the slope is $d_3 = d_4 = +3$.

2. **Min-Cost Feasible Flow (Unconstrained Volume)**:
   - Step 1: $d_1 = -6 < 0 \implies$ augment! ($f = 1, C = -6$).
   - Step 2: $d_2 = -2 < 0 \implies$ augment! ($f = 2, C = -8$).
   - Step 3: $d_3 = +3 \ge 0 \implies$ **STOP IMMEDIATELY!**
   - Output minimum possible cost $C_{\min} = -8$ at optimal volume $f^* = 2$. (Had we blindly run Min-Cost **Max**-Flow to $f = 5$, we would have output $C(5) = +5$, missing the optimum $-8$ by $13$ units!)

3. **WQS Binary Search for Target Volume $K = 3$**:
   - Notice $K = 3$ lies in the interior of the collinear segment $[2, 4]$ of slope $\lambda^* = +3$.
   - For $\lambda = 2$: shifted path costs are $(-8, -4, +1, +1, +5)$, so $f_{\max}(2) = 2 < K$.
   - For $\lambda = 3$: shifted path costs are $(-9, -5, 0, 0, +4)$.
     - Strict solver ($d_k - \lambda < 0$) takes 2 paths: $f_{\min}(3) = 2$, $g(3) = -9 + (-5) = -14$.
     - Weak solver ($d_k - \lambda \le 0$) takes 4 paths: $f_{\max}(3) = 4$, $g(3) = -9 + (-5) + 0 + 0 = -14$.
   - Since $K = 3 \in [f_{\min}(3), f_{\max}(3)] = [2, 4]$, $\lambda^* = 3$ is optimal!
   - Recover $C(3)$ from the weak solver's output $(f_{\max}(3) = 4, g(3) = -14)$:
     $$C(3) = g(3) + 3 \cdot K = -14 + 3 \times 3 = -5,$$
     which matches the exact table value $C(3) = -5$ even though the weak solver never stopped at $f = 3$!

#### Two Classic Failure Modes in Iteration 27
1. **Broken Gadget A — Using `C_true(f_max(lambda*))` Instead of `g(lambda*) + lambda* * K` on Collinear Plateaus**:
   In the trace above at $\lambda^* = 3$ and $K = 3$, if a programmer tracks the unpenalized cost $\text{TrueCost}(f_{\max}(3)) = C(4) = -2$ and outputs $-2$ when the binary search terminates, the answer is wrong ($-2 \ne -5$) because $f_{\max}(3) = 4 \ne 3$ included an extra path of true cost $+3$! Always recover $C(K) = g(\lambda^*) + \lambda^* K$.
2. **Broken Gadget B — Applying WQS Binary Search When Initial $G$ Has Negative Cycles**:
   Theorem 27.1 ($d_1 \le d_2 \le \dots \le d_K$) holds on $f \in [0, F_{\max}]$ **only if $f_0 = 0$ is already cost-optimal for volume $f = 0$** (i.e., $G$ has no negative-cost cycles). If $G$ has a negative-cost circulation that is only unlocked after 1 unit of $s \to t$ flow opens a residual gate, $C(1) - C(0)$ can be smaller than $C(0)$. Thus, before relying on slope convexity, always ensure negative cycles are absent or eliminated via Iteration 28!

---

## Iteration 28: Eliminating Negative Cycles & Min-Cost Flow with Lower Bounds (`上下界最小费用可行流/最大流`)

### 28.1 Min-Cost Flow with Demand Lower Bounds (`上下界最小费用流`)

#### Step 1: The Non-Graph Diagnostic Signal
When a problem specifies that each transition, path segment, or resource allocation $e = (u \to v)$ must carry **at least $l_e$ and at most $u_e$ units** ($l_e \le f(e) \le u_e$) at unit cost $c_e$—for example, "every storyline branch must be played at least once (`[AHOI2014] 支线剧情`)", "every city must be visited exactly $V_i$ times (`[Luogu P4553] 80人环游世界`)", or "every red vertex must have strictly more red incident edges than blue incident edges (`CF 1288 F — Red-Blue Graph`)"—we have a **Lower-Bound Min-Cost Flow** problem.

#### Step 2: The Algebraic Intermediate Representation (Variable Substitution)
Never try to enforce $f(e) \ge l_e$ inside Dijkstra or DFS directly! Instead, perform the linear variable shift:
$$f(e) = l_e + f'(e), \qquad \text{where } 0 \le f'(e) \le u_e - l_e.$$
Substitute $f(e) = l_e + f'(e)$ into the **Total Cost** and the **Flow Conservation Equations**:

1. **Cost Decomposition**:
   $$C(f) = \sum_{e \in E} c_e \big(l_e + f'(e)\big) = \underbrace{\sum_{e \in E} l_e c_e}_{\text{Fixed Base Cost } C_{\text{base}}} + \sum_{e \in E} c_e f'(e).$$
   Notice that $C_{\text{base}} = \sum_{e \in E} l_e c_e$ is a constant independent of $f'$ that we simply add to the answer at the very beginning!
2. **Flow Conservation Transformation (Circulation Form)**:
   For any vertex $v \in V$ where flow is conserved ($\sum_{e \in \delta^-(v)} f(e) - \sum_{e \in \delta^+(v)} f(e) = 0$):
   $$\sum_{e \in \delta^-(v)} \big(l_e + f'(e)\big) - \sum_{e \in \delta^+(v)} \big(l_e + f'(e)\big) = 0.$$
   Move all constants $l_e$ to the right-hand side and define the **net lower-bound inflow excess (imbalance)** $M(v)$ at vertex $v$:
   $$M(v) := \sum_{e \in \delta^-(v)} l_e - \sum_{e \in \delta^+(v)} l_e.$$
   Then the shifted flow $f'$ must satisfy the **Non-Zero Demand Conservation Law**:
   $$\sum_{e \in \delta^+(v)} f'(e) - \sum_{e \in \delta^-(v)} f'(e) = M(v) \qquad (\forall v \in V).$$
    Intuitively, $l_e$ units of mandatory flow have already been pre-injected into the network: if $M(v) > 0$, vertex $v$ receives $M(v)$ more mandatory inflow than outflow, so the free flow $f'(e)$ must carry a net **outflow** of $M(v)$ away from $v$ to restore conservation!

#### Step 3: Mechanical Graph Compilation (The 3 Canonical Engines)

To enforce $\text{OutFlow}_{f'}(v) - \text{InFlow}_{f'}(v) = M(v)$ using a standard single-source single-sink MCMF solver, introduce a **super-source $S^*$** and a **super-sink $T^*$**:
- For every original edge $e = (u \to v, [l_e, u_e], \text{cost } c_e)$, add the shifted edge $(u \to v, \text{cap } u_e - l_e, \text{cost } c_e)$, and accumulate $C_{\text{base}} \gets C_{\text{base}} + l_e c_e$, $M(v) \gets M(v) + l_e$, $M(u) \gets M(u) - l_e$.
- For every vertex $v \in V$:
  - If $M(v) > 0$: add a supply edge $(S^* \to v, \text{cap } M(v), \text{cost } 0)$.
  - If $M(v) < 0$: add a demand edge $(v \to T^*, \text{cap } -M(v), \text{cost } 0)$.

Note that $\sum_{v \in V} M(v) = 0$, so the total capacity leaving $S^*$ equals the total capacity entering $T^*$:
$$D_{\text{total}} = \sum_{v : M(v) > 0} M(v) = \sum_{v : M(v) < 0} (-M(v)).$$
Every edge from $S^*$ and to $T^*$ must be **completely saturated** for $f'$ to satisfy $\text{OutFlow}_{f'}(v) - \text{InFlow}_{f'}(v) = M(v)$!

Now we obtain the three canonical Lower-Bound MCMF engines:

1. **Engine 28A: Source-Sink-Free Min-Cost Circulation (`无源汇上下界最小费用可行流`)**
   - **Setup**: Build the $(S^*, T^*)$ network as above.
   - **Execution**: Run standard MCMF from $S^*$ to $T^*$, obtaining flow volume $F^*$ and cost $C^*$.
   - **Feasibility & Output**: If $F^* < D_{\text{total}}$, **no feasible circulation exists**. Otherwise, the minimum-cost circulation has cost $C_{\text{total}} = C_{\text{base}} + C^*$, and the flow on each original edge $e$ is $f(e) = l_e + f'(e)$.

2. **Engine 28B: $s$-$t$ Min-Cost Feasible Flow with Lower Bounds (`有源汇上下界最小费用可行流`)**
   - **Setup**: In an $s$-$t$ flow network, $s$ and $t$ do not conserve flow individually, Automatic conversion to a circulation: add one **feedback edge**
     $$e_{t \to s} = (t \to s, \quad \text{cap } [0, \infty), \quad \text{cost } 0).$$
     Now $s$ and $t$ also conserve flow!
   - **Execution**: Run Engine 28A on $(S^*, T^*)$ (including the feedback edge $t \to s$).
   - **Output**: If $F^* = D_{\text{total}}$, a feasible $s$-$t$ flow exists with minimum cost $C_{\text{base}} + C^*$, and its $s$-$t$ flow volume equals the flow $f'(t \to s)$ carried by the feedback edge!

3. **Engine 28C: $s$-$t$ Min-Cost Max-Flow with Lower Bounds (`有源汇上下界最小费用最大流`)**
   - **Phase 1 (Feasible Base Flow)**: Run Engine 28B from $S^*$ to $T^*$ (with the feedback edge $t \to s$ of capacity $\infty$ and cost $0$). If $F^* < D_{\text{total}}$, return infeasible. Let $f_1 = f'(t \to s)$ and $C_1 = C_{\text{base}} + C^*$ be the volume and cost of the minimum-cost feasible flow found in Phase 1.
   - **Phase 2 (Augmenting to Maximum Flow)**: Delete $S^*$, $T^*$ (and their incident edges), and **delete the feedback edge $(t \to s)$ and its residual $(s \to t)$**. On the remaining residual network $G_{f'}$, run standard MCMF from the **original source $s$** to the **original sink $t$**, obtaining additional flow $f_2$ and additional cost $C_2$.
   - **Output**: Total maximum flow $F_{\max} = f_1 + f_2$, and minimum cost among all maximum flows $C_{\text{min}} = C_1 + C_2$.

#### Theorem 28.1 (Why Phase 2 of Engine 28C Preserves Global Cost-Optimality)
Why does starting Phase 2 from the Phase-1 residual network $G_{f'}$ guarantee that the final maximum flow is cost-optimal?
*Proof.* At the end of Phase 1, $f'$ is a minimum-cost maximum flow from $S^*$ to $T^*$. By the Negative-Cycle Optimality Theorem (Theorem 26.3), the residual network $G_{f'}$ contains **no negative-cost directed cycles**. When we delete $S^*$, $T^*$, and the feedback edge $(t \to s)$, we only **remove** arcs from $G_{f'}$—which cannot create any new negative-cost cycle! Thus the starting flow $f_1$ at the beginning of Phase 2 has a negative-cycle-free residual network, meaning $f_1$ is already a cost-optimal $s$-$t$ flow of volume $f_1$. By Corollary 26.4, successive shortest paths from $s$ to $t$ in Phase 2 preserve negative-cycle optimality all the way to $F_{\max}$! $\blacksquare$

---

### 28.2 Mandatory Initial Saturation (`负权边强制满流消圈法`): Eliminating Negative Edges & Negative Cycles Before Running MCMF

#### 1. The Crisis: Negative Cycles in the Initial Network $G$
Suppose a problem produces a network $G$ that contains **negative-cost directed cycles** (or contains negative-cost edges on a non-DAG where we refuse to run $O(VE)$ Bellman–Ford/SPFA or $O(V^2 E^2)$ Cycle Canceling).
If $G$ has a negative cycle, the zero flow $f_0 = 0$ violates Theorem 26.3 right out of the gate: $f_0 = 0$ is **not** cost-optimal for volume $0$, Johnson potentials $\pi_0$ do not exist (shortest paths are $-\infty$), and SSP / SPFA loops forever around the negative cycle!

#### 2. The Algebraic Cure: Reversing Negative Edges via Full Pre-Saturation (`强制满流`)
Consider any edge $e = (u \to v)$ with capacity $[0, u_e]$ and strictly **negative cost** $c_e < 0$.
Why does the solver want to use $e$? Because $c_e < 0$ rewards us for sending flow along $u \to v$.
So **give the solver all $u_e$ units of flow on $e$ right at the start!**
Formally, perform the variable substitution on every negative-cost edge $e = (u \to v)$ ($c_e < 0$):
$$f(e) := u_e - \bar{f}(e), \qquad \text{where } 0 \le \bar{f}(e) \le u_e.$$
Here $\bar{f}(e) \in [0, u_e]$ represents the amount of pre-saturated flow on $u \to v$ that we **cancel (send backward from $v$ to $u$)**!
Let us substitute $f(e) = u_e - \bar{f}(e)$ into the cost function and flow conservation equations:

1. **Cost Transformation**:
   $$c_e f(e) = c_e \big(u_e - \bar{f}(e)\big) = \underbrace{u_e c_e}_{\text{Fixed Negative Base Cost}} + \underbrace{(-c_e)}_{> 0} \bar{f}(e).$$
   Because $c_e < 0$, the coefficient of the reversal variable $\bar{f}(e)$ is **strictly positive**: $-c_e = |c_e| > 0$!
2. **Flow Conservation Transformation**:
   At vertex $u$, sending $f(e) = u_e - \bar{f}(e)$ units out along $u \to v$ is algebraically identical to:
   - A fixed mandatory outflow of $u_e$ from $u$ to $v$ (contributing $-u_e$ to $M(u)$ and $+u_e$ to $M(v)$), PLUS
   - An ordinary directed edge **in the reverse direction** $\bar{e} = (v \to u)$ carrying flow $\bar{f}(e) \in [0, u_e]$ at positive unit cost $-c_e > 0$!

```
Original Negative Edge:          Pre-Saturated Positive Reversal Gadget:
      cap [0, u_e], cost c_e < 0         1. Base cost += u_e * c_e (< 0)
  (u) -------------------------> (v)     2. Imbalance: M(u) -= u_e, M(v) += u_e
                                         3. Add reverse edge:
                                            (u) <------------------------- (v)
                                                cap [0, u_e], cost -c_e > 0
```

#### Theorem 28.2 (Complete Elimination of Negative Edges & Negative Cycles)
Applying Mandatory Initial Saturation to every negative-cost edge $e \in E$ ($c_e < 0$) transforms an arbitrary network $G = (V, E, [l_e, u_e], c_e)$ (even one containing negative-cost cycles!) into an equivalent Lower-Bound Min-Cost Flow network $\widehat{G}$ in which **every edge has strictly non-negative cost $\hat{c}_e \ge 0$**.
Consequently:
1. $\widehat{G}$ contains **zero negative-cost edges and zero negative-cost cycles** at initialization.
2. Initial Johnson potentials can be set to $\pi_0(v) = 0$ for all $v \in V$ in $O(V)$ time (**zero Bellman–Ford or SPFA calls required!**), and both Phase 1 ($S^* \to T^*$) and Phase 2 ($s \to t$) run purely with Dijkstra!
3. If an original edge $e = (u \to v)$ belongs to a genuine negative-cost cycle $C$ in $G$, the pre-saturated flow $u_e$ around $C$ already satisfies flow conservation at every vertex of $C$ ($\Delta M(v) = u_e - u_e = 0$), so $C$ stays saturated in the final flow automatically without ever needing cycle-canceling! If $e$ does NOT belong to a feasible circulation, Phase 1 from $S^*$ to $T^*$ routes flow along the reversal edge $\bar{e} = (v \to u, \text{cost } -c_e > 0)$ to smoothly cancel the unachievable portion of $f(e)$ at minimum cost!

> [!IMPORTANT]
> **Summary Recipe for `负权边强制满流消圈法` (Combined with Lower Bounds $[l_e, u_e]$)**
> For each edge $e = (u \to v, [l_e, u_e], c_e)$:
> - **If $c_e \ge 0$**:
>   - Add $l_e c_e$ to $C_{\text{base}}$; update $M(u) \gets M(u) - l_e$, $M(v) \gets M(v) + l_e$.
>   - Add edge $(u \to v, \text{cap } u_e - l_e, \text{cost } c_e \ge 0)$.
> - **If $c_e < 0$**:
>   - Pre-saturate $f(e) = u_e$: add $u_e c_e$ to $C_{\text{base}}$; update $M(u) \gets M(u) - u_e$, $M(v) \gets M(v) + u_e$.
>   - Add **reverse** edge $(v \to u, \text{cap } u_e - l_e, \text{cost } -c_e > 0)$. (Here $\bar{f}(e) \in [0, u_e - l_e]$ ensures $f(e) = u_e - \bar{f}(e) \in [l_e, u_e]$!)
> Then attach $S^*, T^*$ according to $M(v)$ and run pure non-negative Dijkstra MCMF!

---

### 28.3 Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Toy Trace: Resolving a Graph with a Negative Cycle via Mandatory Initial Saturation
Consider a 3-vertex circulation network $V = \{1, 2, 3\}$ with 3 directed edges (no source or sink; we want the **Minimum-Cost Circulation**):
- $e_1 = (1 \to 2, [0, 3], \text{cost } -4)$  *(negative cost!)*
- $e_2 = (2 \to 3, [0, 2], \text{cost } +1)$
- $e_3 = (3 \to 1, [0, 5], \text{cost } +1)$

Notice that $1 \to 2 \to 3 \to 1$ is a **negative-cost cycle** of unit cost $-4 + 1 + 1 = -2 < 0$ and bottleneck capacity $\min(3, 2, 5) = 2$. Thus the optimal circulation should send $2$ units around $1 \to 2 \to 3 \to 1$ for a total cost of $2 \times (-2) = -4$. Let us watch Mandatory Initial Saturation find this without ever running cycle-canceling or SPFA:

1. **Pre-Saturate Negative Edge $e_1 = (1 \to 2, [0, 3], -4)$**:
   - $C_{\text{base}} = 3 \times (-4) = -12$.
   - $M(1) = -3$, $M(2) = +3$, $M(3) = 0$.
   - Replace $e_1$ with reverse edge $\bar{e}_1 = (2 \to 1, \text{cap } 3, \text{cost } +4)$.
   - Keep $e_2 = (2 \to 3, \text{cap } 2, \text{cost } +1)$ and $e_3 = (3 \to 1, \text{cap } 5, \text{cost } +1)$.
2. **Build $(S^*, T^*)$ Network**:
   - Since $M(2) = +3 > 0$, add $(S^* \to 2, \text{cap } 3, \text{cost } 0)$.
   - Since $M(1) = -3 < 0$, add $(1 \to T^*, \text{cap } 3, \text{cost } 0)$.
   - All edge costs in $\widehat{G}$ are non-negative ($\ge 0$)! Set $\pi_0 = 0$.
3. **Run Dijkstra MCMF from $S^*$ to $T^*$ (Need $D_{\text{total}} = 3$ units of flow)**:
   - **Path 1**: $S^* \to 2 \xrightarrow{e_2} 3 \xrightarrow{e_3} 1 \to T^*$ has cost $0 + 1 + 1 + 0 = +2$ and bottleneck $\min(3, 2, 5, 3) = 2$. Push $2$ units! Cost increases by $2 \times 2 = +4$.
   - **Path 2**: Now $e_2 = (2 \to 3)$ is full; the remaining $1$ unit from $S^* \to 2$ must use the reversal edge $\bar{e}_1 = (2 \to 1, \text{cost } +4)$: $S^* \to 2 \xrightarrow{\bar{e}_1} 1 \to T^*$ of cost $+4$ and bottleneck $1$. Push $1$ unit! Cost increases by $1 \times 4 = +4$.
4. **Recover Optimal Circulation**:
   - Total flow from $S^*$ to $T^*$ is $2 + 1 = 3 = D_{\text{total}}$ (feasible!).
   - Total minimum cost: $C_{\text{total}} = C_{\text{base}} + C^* = -12 + (4 + 4) = -4$.
   - Edge flows: $f(e_1) = u_{e_1} - \bar{f}(e_1) = 3 - 1 = 2$, $f(e_2) = 2$, $f(e_3) = 2$.
   - That's $2$ units around the negative cycle, found in two pure Dijkstra calls with $\pi_0 = 0$!

#### Three Classic Broken-Gadget Counterexamples in Iteration 28
1. **Broken Gadget A — Leaving $(t \to s, \infty, 0)$ in the Graph During Phase 2 of Engine 28C**:
   If you forget to delete the feedback edge $(t \to s)$ (and its residual arc $(s \to t)$) before running Phase 2 ($s \to t$ MCMF), the residual arc $(s \to t)$ (or a cycle using $t \to s$) allows infinite loop flow or corrupts the true $s$-$t$ flow volume! Always zero out the capacities of both $e_{t \to s}$ and $e_{t \to s}^-$ before Phase 2.
2. **Broken Gadget B — Using Mandatory Initial Saturation on an Infinite-Capacity Negative Edge ($u_e = \infty, c_e < 0$)**:
   If an edge has $u_e = \infty$ and $c_e < 0$, pre-saturating $f(e) = u_e$ overflows integer arithmetic (and if it lies on a cycle, the minimum cost is genuinely $-\infty$). Before pre-saturating a negative edge, bound its capacity $u_e$ by the true physical maximum possible flow in the problem (e.g., $\min(\text{total supply}, K)$).
3. **Broken Gadget C — Confusing `有源汇上下界最小费用可行流` with `有源汇上下界最小费用最大流`**:
   Many problems (such as `[AHOI2014] 支线剧情` and `[Luogu P4553] 80人环游世界`) ask for the **minimum cost to satisfy all lower bounds**, NOT the maximum flow! In those problems, you **stop after Phase 1** ($S^* \to T^*$ with feedback edge $t \to s$). Running Phase 2 ($s \to t$ max flow) will push extra unnecessary paths through the graph and inflate the cost!

---

## Iteration 29: Convex Marginal Edge Splitting (`凸费用拆边`) & Quadratic/Tournament Counting Reductions

### 29.1 Separable Convex Edge Costs & Marginal Splitting

#### 1. The Mathematical Model
In standard MCMF, the cost on edge $e$ is linear: $c_e \cdot f(e)$. What if sending $f_e \in \{0, 1, \dots, U\}$ integer units of flow along edge $e = (u \to v)$ costs a **non-linear function** $g(f_e)$ (with $g(0) = 0$), such as $g(f_e) = a f_e^2 + b f_e$ or $g(f_e) = \binom{f_e}{2}$?

Define the **$k$-th marginal cost (first forward difference)** for each unit $k \in \{1, 2, \dots, U\}$:
$$\Delta g(k) := g(k) - g(k - 1) \qquad (1 \le k \le U).$$
By telescoping, for any integer flow $f_e \in \{0, 1, \dots, U\}$:
$$g(f_e) = g(0) + \sum_{k=1}^{f_e} \big(g(k) - g(k - 1)\big) = \sum_{k=1}^{f_e} \Delta g(k).$$

#### Definition 29.1 (Discrete Convexity)
A function $g : \{0, 1, \dots, U\} \to \mathbb{R}$ is **discrete convex** on $\{0, 1, \dots, U\}$ if its marginal costs are monotonically non-decreasing (equivalently, its second difference $\Delta^2 g(k) = \Delta g(k+1) - \Delta g(k) \ge 0$ is non-negative):
$$\Delta g(1) \le \Delta g(2) \le \dots \le \Delta g(U).$$

#### Theorem 29.2 (Convex Marginal Edge Splitting Compilation `凸费用拆边定理`)
If $g : \{0, 1, \dots, U\} \to \mathbb{R}$ is discrete convex with $g(0) = 0$, replace the single non-linear edge $e = (u \to v, [0, U], \text{cost } g(f_e))$ with **$U$ parallel unit-capacity linear edges** $e_1, e_2, \dots, e_U$ from $u$ to $v$:
$$e_k = \big(u \to v, \quad \text{cap } 1, \quad \text{cost } \Delta g(k)\big) \qquad \text{for } k = 1, 2, \dots, U.$$
Then in any minimum-cost integer flow $\phi$, if the total flow routed from $u$ to $v$ across the bundle $\{e_1, \dots, e_U\}$ is $f_e = \sum_{k=1}^U \phi(e_k)$, the minimum cost achieved by the parallel bundle is **identically equal to $g(f_e)$**!

```
Non-Linear Convex Edge:                Compiled Parallel Unit-Edge Bundle:
                                             e_1: cap 1, cost \Delta g(1)
     f_e \in [0, U]                        /-----------------------------\
(u) ----------------> (v)     ===>    (u)  --- e_2: cap 1, cost \Delta g(2) ---> (v)
     cost g(f_e)                           \         ...                 /
                                             e_U: cap 1, cost \Delta g(U)
```

*Proof (Via Negative-Cycle Optimality).*
To send $f_e$ units of flow across the parallel bundle $\{e_1, \dots, e_U\}$, the solver must pick $f_e$ distinct edges from $\{e_1, \dots, e_U\}$. Suppose for contradiction that an optimal flow $\phi$ picks some edge $e_k$ ($\phi(e_k) = 1$) while leaving an earlier, strictly cheaper edge $e_j$ ($j < k, \Delta g(j) < \Delta g(k)$) empty ($\phi(e_j) = 0$).
Then in the residual network $G_\phi$:
- Forward edge $e_j = (u \to v)$ is available with residual cost $+\Delta g(j)$.
- Backward edge $e_k^- = (v \to u)$ is available with residual cost $-\Delta g(k)$.
Together, $u \xrightarrow{e_j} v \xrightarrow{e_k^-} u$ forms a **directed cycle of length 2 in $G_\phi$ with strictly negative cost** $\Delta g(j) - \Delta g(k) < 0$, contradicting Theorem 26.3!
Thus, any optimal flow saturates the cheapest $f_e$ edges $\Delta g(1), \Delta g(2), \dots, \Delta g(f_e)$ in strictly increasing order, paying $\sum_{k=1}^{f_e} \Delta g(k) = g(f_e)$. $\blacksquare$

#### Why Concave Edge Costs ($\Delta g(1) > \Delta g(2)$) Fail Utterly
What if $g$ is **concave**—for instance, a fixed setup cost $g(0) = 0, g(1) = 10, g(2) = 12$, so $\Delta g(1) = 10 > \Delta g(2) = 2$?
If we create parallel edges $e_1 = (\text{cap } 1, \text{cost } 10)$ and $e_2 = (\text{cap } 1, \text{cost } 2)$, then when routing $f_e = 1$ unit of flow, the MCMF solver **greedily picks $e_2$ first**, paying $\Delta g(2) = 2$ instead of $g(1) = 10$!
Indeed, Minimum-Cost Flow with concave costs (Fixed-Charge Network Flow) is **strongly NP-hard** (containing Minimum Steiner Tree and Set Cover as special cases). **Never split an edge into marginal unit edges without first verifying $\Delta^2 g(k) = \Delta g(k+1) - \Delta g(k) \ge 0$!**

---

### 29.2 Flagship Non-Graph Application 1: Maximizing 3-Cycles in a Tournament (`[WC2007] 剪刀石头布`)

Let us apply the **4-Step "Zero Magic Gadgets" Compilation** to one of the most celebrated problems in Chinese Olympiad history: **`[WC2007 / Luogu P4249] 剪刀石头布` (Rock-Paper-Scissors)**.

#### Problem Statement
In a round-robin tournament of $n \le 100$ players, every pair of distinct players $\{u, v\}$ plays exactly one match, which has a decisive winner ($u \to v$ or $v \to u$). Some match outcomes are already fixed; the remaining matches are undecided. Complete all undecided match orientations to **maximize the number of directed 3-cycles** (triples $\{u, v, w\}$ such that $u \to v \to w \to u$ or $u \to w \to v \to u$).

#### Step 1: Non-Graph Diagnostic Signal (Why Direct Counting Fails & Why Complement Counting Unlocks MCMF)
- A directed 3-cycle $u \to v \to w \to u$ is a **3-variable interaction** coupling edges $(u,v), (v,w), (w,u)$. Neither Min-Cut (which handles pairwise submodular relations) nor standard matching can directly count 3-cycles!
- **The Combinatorial Breakthrough (Complement Counting)**: What does a triple of vertices $\{u, v, w\}$ look like if it is **NOT** a directed 3-cycle?
  In any tournament on 3 vertices, the out-degrees inside $\{u, v, w\}$ are either $(1, 1, 1)$ (a directed 3-cycle!) or $(2, 1, 0)$ (a **transitive triple**, where one vertex beats both of the other two!).
- Notice the miracle: in a transitive triple, there is **a unique vertex with out-degree $2$** (and no vertex in a 3-cycle has out-degree $2$). Therefore, across the entire tournament, a vertex $v$ with total out-degree $d^+(v)$ is the dominator of **exactly $\binom{d^+(v)}{2}$ transitive triples**!

#### Step 2: Algebraic Intermediate Representation
Summing over all $v \in \{1, \dots, n\}$ counts every non-3-cycle triple $\{u, v, w\}$ **exactly once** (at its unique dominator). Hence the exact number of directed 3-cycles in any tournament $T$ is:
$$\#(\text{3-cycles}) = \binom{n}{3} - \sum_{v=1}^n \binom{d^+(v)}{2}.$$
Because $\binom{n}{3}$ is a constant, **maximizing the number of 3-cycles is 100% equivalent to minimizing the separable sum of binomial coefficients**:
$$\min \sum_{v=1}^n \binom{d^+(v)}{2}$$
subject to the constraint that for every match $e = \{u, v\}$, exactly one of $u$ or $v$ wins (contributing $+1$ to $d^+(u)$ or $+1$ to $d^+(v)$)!
Let us check the convexity of $g(k) = \binom{k}{2} = \frac{k(k-1)}{2}$ for $k = 0, 1, \dots, n-1$:
$$\Delta g(k) = \binom{k}{2} - \binom{k-1}{2} = k - 1 \qquad (k = 1, 2, \dots, n-1).$$
The marginal costs for the $1\text{st}, 2\text{nd}, 3\text{rd}, \dots, (n-1)\text{-th}$ win of player $v$ are:
$$0, \; 1, \; 2, \; 3, \; \dots, \; n - 2.$$
Since $0 < 1 < 2 < \dots < n-2$ is strictly increasing, $g(k) = \binom{k}{2}$ is **strictly discrete convex**!

#### Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)
Let $w_0(v)$ be the number of already-fixed wins of player $v$, and let $E_{\text{free}}$ be the set of undecided matches $e = \{u, v\}$.
We can either include the fixed matches as vertices or pre-assign $w_0(v)$:
- **Source $S$ to Undecided Matches**: For each undecided match $e = \{u, v\} \in E_{\text{free}}$, create a match vertex $m_e$ and add:
  - $(S \to m_e, \text{cap } 1, \text{cost } 0)$: match $e$ must produce $1$ winner.
  - $(m_e \to u, \text{cap } 1, \text{cost } 0)$ and $(m_e \to v, \text{cap } 1, \text{cost } 0)$: the $1$ unit of flow goes to whichever player ($u$ or $v$) wins match $e$!
- **Player Vertices $v \in \{1, \dots, n\}$ to Sink $T$ (Marginal Win Edges)**:
  Player $v$ already has $w_0(v)$ fixed wins, contributing a fixed base cost $\binom{w_0(v)}{2}$. If $v$ wins additional undecided matches, its degree steps from $k-1$ to $k$ for $k = w_0(v) + 1, \dots, w_0(v) + \text{free}(v)$, with marginal cost $\Delta g(k) = k - 1$.
  Thus, from $v$ to $T$, add parallel unit-capacity edges with costs:
  $$w_0(v), \quad w_0(v) + 1, \quad w_0(v) + 2, \quad \dots, \quad w_0(v) + \text{free}(v) - 1.$$
- **Answer Recovery**: Run MCMF from $S$ to $T$ (where $|f| = |E_{\text{free}}|$), obtaining minimum additional cost $C^*$. Then:
  $$\max \#(\text{3-cycles}) = \binom{n}{3} - \sum_{v=1}^n \binom{w_0(v)}{2} - C^*.$$
  To reconstruct the tournament matrix, for each undecided match $e = \{u, v\}$, if the edge $(m_e \to u)$ carries flow $1$, $u$ beats $v$; otherwise $v$ beats $u$.

---

### 29.3 Flagship Non-Graph Application 2: Coupled Win/Loss Quadratic Budgets (`[JSOI2009] 球队收益`)

#### Step 1: Diagnostic Signal
In `[JSOI2009 / Luogu P4307] 球队收益 / 球队预算`, team $i$ starts with $w_i$ wins and $l_i$ losses, and has $rem_i$ remaining matches to play. At the end of the season, if team $i$ finishes with $W_i$ total wins and $L_i$ total losses, its cost is:
$$\text{Cost}_i(W_i, L_i) = C_i W_i^2 + D_i L_i^2 \qquad (C_i, D_i \ge 0).$$
At first glance, $\text{Cost}_i(W_i, L_i)$ depends on **two** variables ($W_i$ and $L_i$), whereas flow into vertex $i$ only counts one quantity (say, wins $W_i$)!

#### Step 2: Algebraic Intermediate Representation (Invariant Elimination of $L_i$)
Every match played by team $i$ ends in either a win or a loss! Therefore, the **final total number of matches** played by team $i$ is a known constant $T_i = w_i + l_i + rem_i$:
$$W_i + L_i = T_i \implies L_i = T_i - W_i.$$
Substitute $L_i = T_i - W_i$ into $\text{Cost}_i(W_i, L_i)$ to eliminate $L_i$ completely:
$$g_i(W_i) = C_i W_i^2 + D_i (T_i - W_i)^2.$$
Now $g_i(W_i)$ is a univariate function of $W_i \in \{w_i, w_i + 1, \dots, w_i + rem_i\}$ alone!
Let us compute the marginal cost of team $i$'s $k$-th win (increasing wins from $k-1$ to $k$, which simultaneously decreases final losses from $T_i - k + 1$ to $T_i - k$):
$$\Delta g_i(k) = g_i(k) - g_i(k-1) = C_i\big(k^2 - (k-1)^2\big) + D_i\big((T_i - k)^2 - (T_i - k + 1)^2\big)$$
$$\Delta g_i(k) = C_i(2k - 1) - D_i\big(2(T_i - k) + 1\big) = 2(C_i + D_i)k - (C_i + D_i + 2 D_i T_i).$$
Since $C_i, D_i \ge 0$, the second difference is $\Delta^2 g_i(k) = 2(C_i + D_i) \ge 0$, so $\Delta g_i(k)$ is monotonically non-decreasing in $k$!

#### Step 3 & Step 4: Graph Compilation & Negative-Marginal-Cost Caveat
- Add base cost $\sum_{i=1}^n g_i(w_i)$ (assuming team $i$ loses all remaining matches: $W_i = w_i, L_i = T_i - w_i$).
- For each remaining match $e = \{u, v\}$, add $(S \to m_e, 1, 0)$ and $(m_e \to u, 1, 0), (m_e \to v, 1, 0)$.
- For each team $i$, add $rem_i$ parallel unit-capacity edges from $i$ to $T$ with costs $\Delta g_i(w_i + 1), \Delta g_i(w_i + 2), \dots, \Delta g_i(w_i + rem_i)$.
- **Critical Caveat**: Notice that when $D_i T_i$ is large, $\Delta g_i(k)$ can be **negative** for small $k$ (winning a match avoids a massive loss penalty $D_i L_i^2$)! However, the network $S \to m_e \to i \to T$ is a **3-layer DAG**, so by Iteration 26 (Regime 2), we initialize $\pi_0$ in $O(V+E)$ via DAG DP (or simply observe that every path $S \to m_e \to i \to T$ has length 3) without SPFA!

---

### 29.4 Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Hand-Checkable $n = 4$ Trace of `[WC2007] 剪刀石头布`
Suppose $n = 4$ players ($\binom{4}{3} = 4$ total triples). Five of the $\binom{4}{2} = 6$ matches are already decided:
- $1 \to 2$, $1 \to 3$, $2 \to 3$, $3 \to 4$, $4 \to 1$.
- Only one match is undecided: $e = \{2, 4\}$.
Let us find the optimal orientation of $\{2, 4\}$ via Iteration 29:
1. **Current Fixed Wins $w_0(v)$**:
   - $w_0(1) = 2$ (beats $2, 3$), base cost $\binom{2}{2} = 1$.
   - $w_0(2) = 1$ (beats $3$), base cost $\binom{1}{2} = 0$.
   - $w_0(3) = 1$ (beats $4$), base cost $\binom{1}{2} = 0$.
   - $w_0(4) = 1$ (beats $1$), base cost $\binom{1}{2} = 0$.
   - Total base cost $= 1 + 0 + 0 + 0 = 1$.
2. **Marginal Edges for Undecided Match $\{2, 4\}$**:
   - If $2$ wins $\{2, 4\}$, $d^+(2)$ increases from $1$ to $2$ at marginal cost $\Delta g(2) = w_0(2) = 1$.
   - If $4$ wins $\{2, 4\}$, $d^+(4)$ increases from $1$ to $2$ at marginal cost $\Delta g(2) = w_0(4) = 1$.
   - Both paths $S \to m_{\{2,4\}} \to 2 \to T$ and $S \to m_{\{2,4\}} \to 4 \to T$ have cost $1$, so $C^* = 1$.
3. **Total 3-Cycles**:
   - $\#(\text{3-cycles}) = \binom{4}{3} - (\text{base} + C^*) = 4 - (1 + 1) = 2$.
   - Check: If $4 \to 2$, the 3-cycles are $(1 \to 2 \to 3 \to 4 \to 1)$ wait: $(1 \to 3 \to 4 \to 1)$ and $(2 \to 3 \to 4 \to 2)$—exactly $2$ directed 3-cycles!

#### Two Classic Broken-Gadget Counterexamples in Iteration 29
1. **Broken Gadget A — Indexing Off-By-One in $\Delta \binom{k}{2}$**:
   The marginal cost of going from $k-1$ wins to $k$ wins is $\binom{k}{2} - \binom{k-1}{2} = k - 1$ (so the 1st win costs $0$, the 2nd costs $1$, the 3rd costs $2$). A common bug is assigning costs $1, 2, 3, \dots$, which shifts every marginal cost by $+1$ (computing $\binom{d^+(v)+1}{2}$ instead of $\binom{d^+(v)}{2}$). While a uniform $+1$ shift across all vertices only adds $|E|$ to the total cost when every match has 1 winner, it **breaks completely** when vertices have different numbers of already-fixed wins $w_0(v)$ or when flow volume is variable!
2. **Broken Gadget B — Splitting $U \le 10^9$ Parallel Edges Without Capacity Scaling / WQS**:
   Theorem 29.2 creates $U$ parallel unit edges. When $U \le n \le 100$ (as in `[WC2007] 剪刀石头布` and `[JSOI2009] 球队收益`), $O(n^2)$ edges is tiny. However, if $U \le 10^6$, explicitly creating $U$ parallel edges causes MLE/TLE! Instead, when $U$ is large, either:
   - **Dynamic Lazy Edge Insertion (Wave 4A)**: Only insert the $(k+1)$-th marginal edge $(u \to v, 1, \Delta g(k+1))$ **after** the $k$-th edge is saturated during SSP!
   - **Piecewise-Linear Segment Bundling (`CF 708 D`)**: If $g(f)$ is piecewise-linear with only $O(1)$ linear pieces (e.g., slope $1$ on $[0, c_e]$ and slope $2$ on $[c_e, \infty)$), bundle each constant-slope piece into a **single** edge of capacity equal to the interval width!

---

## Iteration 30: Interval $k$-Coverage & The Algebraic Equation-Difference Method (`流守恒差分建模法` — `[NOI2008] 志愿者招募`)

### 30.1 Why Interval Coverage Is the Ultimate Test of the "Zero Magic Gadgets" Mandate

Open almost any traditional editorial for **`[NOI2008 / Luogu P3980] 志愿者招募` (Volunteer Recruitment)** and you will read a baffling prescription:
> *"Create $n+1$ vertices $1, 2, \dots, n+1$. Add an edge $(t \to t+1)$ with capacity $\infty - A_t$ and cost $0$, or add an edge $(t+1 \to t)$ with capacity $\infty$ and cost $0$ and connect $S, T$ based on $A_t - A_{t-1}$. For each volunteer $[l_i, r_i]$, add $(l_i \to r_i + 1)$ with capacity $\infty$ and cost $c_i$. Run MCMF."*

A student reading that for the first time asks three completely reasonable questions:
1. **Why are there $n+1$ vertices instead of $n$?**
2. **Where on earth did $A_t - A_{t-1}$ come from?**
3. **Why does the free edge go backward from $t+1 \to t$ in lower-bound coverage, but forward from $t \to t+1$ in upper-bound packing?**

The answer is **not** a clever geometric picture—it is **pure linear algebra**! Specifically, a linear program compiles into a network flow problem whenever every variable appears in the constraint matrix with **at most one $+1$ coefficient (outflow from vertex $u$) and at most one $-1$ coefficient (inflow to vertex $v$)**.
In an interval coverage problem, a variable $x_i$ covers a contiguous range of days $t \in [l_i, r_i]$, so in the raw constraint matrix, the column for $x_i$ is a **contiguous block of $1$s** from row $l_i$ to row $r_i$.
How do you turn a contiguous block of $1$s $(0, \dots, 0, 1, 1, \dots, 1, 0, \dots, 0)^T$ into a column with a single $+1$ and a single $-1$?
**You subtract each row from the row below it ($\Delta E_t = E_t - E_{t-1}$)!**

---

### 30.2 The 4-Step Equation-Difference Compilation Engine (`流守恒差分建模法`)

Let us derive the exact MCMF network for **`[NOI2008] 志愿者招募`** from scratch using the **4-Step Equation-Difference Method**.

#### Problem Statement (`[NOI2008] 志愿者招募`)
A project runs for $n$ days ($t = 1, 2, \dots, n$). Day $t$ requires at least $A_t \ge 0$ active volunteers. There are $m$ types of volunteers; each volunteer of type $i \in \{1, \dots, m\}$ works across the contiguous interval of days $[l_i, r_i]$ ($1 \le l_i \le r_i \le n$) and costs $c_i \ge 0$ per person hired (with unlimited supply of each type). Find the minimum total cost to satisfy all $n$ daily requirements.

#### Step 1: Write the Raw Linear Inequalities
Let $x_i \in \mathbb{Z}_{\ge 0}$ be the number of volunteers of type $i$ hired. The problem is the Integer Linear Program:
$$\min \sum_{i=1}^m c_i x_i$$
subject to:
$$\sum_{i \,:\, t \in [l_i, r_i]} x_i \ge A_t \qquad \text{for each day } t = 1, 2, \dots, n,$$
$$x_i \ge 0 \qquad (i = 1, \dots, m).$$

#### Step 2: Convert Inequalities to Equations via Non-Negative Slack Variables
An inequality $\ge A_t$ cannot be differenced directly (subtracting two inequalities $\ge$ goes the wrong way!). To turn each inequality into an **exact equation**, introduce a non-negative **surplus (slack) variable** $y_t \ge 0$ for each day $t \in \{1, \dots, n\}$, representing the number of **extra volunteers** working on day $t$ beyond the minimum requirement $A_t$:
$$E_t : \quad \sum_{i \,:\, l_i \le t \le r_i} x_i - y_t = A_t \qquad (t = 1, 2, \dots, n), \quad y_t \ge 0.$$
To capture both endpoints of every interval $[l_i, r_i]$ cleanly when taking differences, pad the system at the top and bottom with two trivial zero equations (setting $A_0 := 0$ and $A_{n+1} := 0$):
$$E_0 : \quad 0 = 0, \qquad\qquad E_{n+1} : \quad 0 = 0.$$

#### Step 3: Subtract Consecutive Equations ($\Delta E_t := E_t - E_{t-1}$ for $t = 1, 2, \dots, n+1$)
Replace the system $(E_1, \dots, E_n, E_{n+1})$ by the equivalent invertible triangular difference system:
$$\Delta E_t := E_t - E_{t-1} \qquad \text{for } t = 1, 2, \dots, n + 1.$$
Let us inspect what happens to **every variable** across the $n+1$ difference equations $\Delta E_1, \Delta E_2, \dots, \Delta E_{n+1}$:

1. **Interval Variable $x_i$ (active in $E_{l_i}, E_{l_i+1}, \dots, E_{r_i}$)**:
   - For $t < l_i$: $x_i$ is in neither $E_t$ nor $E_{t-1} \implies$ coefficient is $0 - 0 = 0$.
   - At $t = l_i$: $x_i$ is in $E_{l_i}$ ($+1$) but **not** in $E_{l_i - 1}$ ($0$) $\implies$ coefficient in $\Delta E_{l_i}$ is **$+1$**!
   - For $l_i < t \le r_i$: $x_i$ is in both $E_t$ ($+1$) and $E_{t-1}$ ($+1$) $\implies$ coefficient in $\Delta E_t$ is $1 - 1 = 0$!
   - At $t = r_i + 1$: $x_i$ is **not** in $E_{r_i + 1}$ ($0$) but **is** in $E_{r_i}$ ($+1$) $\implies$ coefficient in $\Delta E_{r_i + 1}$ is $0 - 1 =$ **$-1$**!
   - For $t > r_i + 1$: $x_i$ is in neither $\implies$ coefficient is $0$.
   > **Result for $x_i$**: Across all $n+1$ equations $\Delta E_1, \dots, \Delta E_{n+1}$, variable $x_i$ appears **only twice**: with **$+1$ in $\Delta E_{l_i}$** and with **$-1$ in $\Delta E_{r_i + 1}$**! *(This also explains why there are $n+1$ vertices: an interval ending on day $r_i = n$ exits in equation $\Delta E_{n+1}$!)*

2. **Slack Variable $y_t$ ($1 \le t \le n$, present only in $E_t$ with coefficient $-1$)**:
   - In $\Delta E_t = E_t - E_{t-1}$: $y_t$ appears with coefficient **$-1$**.
   - In $\Delta E_{t+1} = E_{t+1} - E_t$: $y_t$ appears with coefficient $-(-1) =$ **$+1$**.
   - In all other $\Delta E_k$: $y_t$ has coefficient $0$.
   > **Result for $y_t$**: Across all $n+1$ equations, slack variable $y_t$ appears **only twice**: with **$+1$ in $\Delta E_{t+1}$** and with **$-1$ in $\Delta E_t$**!

3. **Right-Hand Side Constant $b_t$**:
   - In $\Delta E_t = E_t - E_{t-1}$, the right-hand side is:
     $$b_t := A_t - A_{t-1} \qquad (t = 1, 2, \dots, n+1, \text{ where } A_0 = A_{n+1} = 0).$$
   - Notice that the sum of all right-hand sides telescopes identically to zero:
     $$\sum_{t=1}^{n+1} b_t = \sum_{t=1}^{n+1} (A_t - A_{t-1}) = A_{n+1} - A_0 = 0.$$

Writing out the complete differenced system $\Delta E_t$ ($t = 1, \dots, n+1$):
$$\Delta E_t : \quad \underbrace{\left( \sum_{i \,:\, l_i = t} x_i + y_{t-1} \right)}_{\text{Variables with }+1\text{ at }t\text{ (Outflow)}} - \underbrace{\left( \sum_{i \,:\, r_i + 1 = t} x_i + y_t \right)}_{\text{Variables with }-1\text{ at }t\text{ (Inflow)}} = A_t - A_{t-1},$$
where $y_0 \equiv 0$ and $y_{n+1} \equiv 0$.

#### Step 4: Read Off the Flow Graph Directly from $\Delta E_t$
Create $n+1$ vertices $V = \{1, 2, \dots, n+1\}$, one for each equation $\Delta E_t$. Interpret $\Delta E_t$ as the **Flow Conservation Equation at vertex $t$**:
$$\text{OutFlow}(t) - \text{InFlow}(t) = A_t - A_{t-1}.$$
Under this convention (**$+1 = \text{OutFlow from } u$**, **$-1 = \text{InFlow to } v$**), any non-negative variable $z \ge 0$ with $+1$ in $\Delta E_u$, $-1$ in $\Delta E_v$, upper bound $U$, and objective cost $c$ is **literally a directed edge $u \to v$ with capacity $U$ and unit cost $c$**!

| Algebraic Object in $\Delta E_t$ | $+1$ Row (Tail $u$) | $-1$ Row (Head $v$) | Compiled Directed Edge $(u \to v)$ | Capacity | Unit Cost |
| :--- | :---: | :---: | :--- | :---: | :---: |
| **Volunteer Variable $x_i \ge 0$** | $\Delta E_{l_i}$ | $\Delta E_{r_i + 1}$ | $l_i \longrightarrow (r_i + 1)$ | $\infty$ | $+c_i$ |
| **Surplus Slack $y_t \ge 0$** ($1 \le t \le n$) | $\Delta E_{t+1}$ | $\Delta E_t$ | $(t + 1) \longrightarrow t$ *(backward!)* | $\infty$ | $0$ |
| **RHS Supply $b_t = A_t - A_{t-1} > 0$** | External Inflow | $\Delta E_t$ | $S^* \longrightarrow t$ | $A_t - A_{t-1}$ | $0$ |
| **RHS Demand $b_t = A_t - A_{t-1} < 0$** | $\Delta E_t$ | External Outflow | $t \longrightarrow T^*$ | $A_{t-1} - A_t$ | $0$ |

Run standard non-negative Dijkstra MCMF from $S^*$ to $T^*$! Because every $b_t$ is matched and all costs $c_i \ge 0$, the minimum cost of the maximum flow from $S^*$ to $T^*$ is the exact optimal answer to `[NOI2008] 志愿者招募`!

```
          x_i: cap \infty, cost c_i (l_i ---> r_i + 1)
       /-----------------------------------------------\
      /                                                 v
   ( 1 ) <======= ( 2 ) <======= ( 3 ) <======= ... <== (n+1)
          y_1: 0         y_2: 0         y_3: 0           y_n: 0
          (backward slack edges t+1 ---> t, cap \infty, cost 0)
```

---

### 30.3 Complete Hand-Checkable $n = 3$ Numerical Trace of `[NOI2008] 志愿者招募`

Let us trace a concrete $n = 3$ day instance from raw inequalities to final primal variables to see every equation in action.
- **Days $n = 3$** with daily demands: $A_1 = 2, \; A_2 = 3, \; A_3 = 1$ (and boundary $A_0 = 0, \; A_4 = 0$).
- **Volunteer Types $m = 3$**:
  - Type 1: $[l_1, r_1] = [1, 2]$, cost $c_1 = 4$ (variable $x_1$).
  - Type 2: $[l_2, r_2] = [2, 3]$, cost $c_2 = 5$ (variable $x_2$).
  - Type 3: $[l_3, r_3] = [1, 3]$, cost $c_3 = 7$ (variable $x_3$).

1. **Step 1 & 2 — Slack Equations $E_0, \dots, E_4$**:
   $$\begin{aligned}
   E_0 &: & 0 &= 0 \\
   E_1 &: & x_1 + x_3 - y_1 &= 2 \\
   E_2 &: & x_1 + x_2 + x_3 - y_2 &= 3 \\
   E_3 &: & x_2 + x_3 - y_3 &= 1 \\
   E_4 &: & 0 &= 0
   \end{aligned}$$

2. **Step 3 — Consecutive Differences $\Delta E_t = E_t - E_{t-1}$ ($t = 1, 2, 3, 4$)**:
   $$\begin{aligned}
   \Delta E_1 = E_1 - E_0 &: & +x_1 + x_3 - y_1 &= 2 - 0 = +2 \\
   \Delta E_2 = E_2 - E_1 &: & +x_2 + y_1 - y_2 &= 3 - 2 = +1 \\
   \Delta E_3 = E_3 - E_2 &: & -x_1 + y_2 - y_3 &= 1 - 3 = -2 \\
   \Delta E_4 = E_4 - E_3 &: & -x_2 - x_3 + y_3 &= 0 - 1 = -1
   \end{aligned}$$
   Look at the columns of $\Delta E_1, \dots, \Delta E_4$:
   - $x_1$: $+1$ in $\Delta E_1$, $-1$ in $\Delta E_3 \implies$ edge $1 \to 3$, cost $4$.
   - $x_2$: $+1$ in $\Delta E_2$, $-1$ in $\Delta E_4 \implies$ edge $2 \to 4$, cost $5$.
   - $x_3$: $+1$ in $\Delta E_1$, $-1$ in $\Delta E_4 \implies$ edge $1 \to 4$, cost $7$.
   - $y_1$: $+1$ in $\Delta E_2$, $-1$ in $\Delta E_1 \implies$ edge $2 \to 1$, cost $0$.
   - $y_2$: $+1$ in $\Delta E_3$, $-1$ in $\Delta E_2 \implies$ edge $3 \to 2$, cost $0$.
   - $y_3$: $+1$ in $\Delta E_4$, $-1$ in $\Delta E_3 \implies$ edge $4 \to 3$, cost $0$.
   - RHS $b = (+2, +1, -2, -1) \implies$ supply edges $(S^* \to 1, \text{cap } 2, \text{cost } 0)$ and $(S^* \to 2, \text{cap } 1, \text{cost } 0)$; demand edges $(3 \to T^*, \text{cap } 2, \text{cost } 0)$ and $(4 \to T^*, \text{cap } 1, \text{cost } 0)$.

3. **Step 4 — Run MCMF from $S^*$ to $T^*$ (Total supply $D_{\text{total}} = 2 + 1 = 3$)**:
   - **Path 1**: $S^* \to 1 \xrightarrow{x_1} 3 \to T^*$ has cost $4$ and bottleneck $2$. Push $2$ units! ($x_1 = 2$, cost $= 8$). Now $S^* \to 1$ and $3 \to T^*$ are completely saturated!
   - **Path 2**: We still need $1$ unit from $S^* \to 2$ to reach $4 \to T^*$. Compare:
     - Direct edge $2 \xrightarrow{x_2} 4$ costs $5$.
     - Indirect path $2 \xrightarrow{y_1} 1 \xrightarrow{x_3} 4$ costs $0 + 7 = 7$.
     - Indirect path using residual of $x_1$ ($3 \to 1$, cost $-4$): $2 \xrightarrow{y_1} 1$ doesn't use it, what about $S^* \to 2 \xrightarrow{x_2} 4 \to T^*$? Cost is $5$. What about rerouting 1 unit of $x_1$: $S^* \to 2 \xrightarrow{x_2} 4 \xrightarrow{y_3} 3$? Wait: in $G_{f_1}$, edge $x_1 = (1 \to 3)$ has backward residual arc $x_1^- = (3 \to 1, \text{cap } 2, \text{cost } -4)$!
     - Let's check the path $S^* \to 2 \xrightarrow{y_1=0}$ no, from $2$ can we reach $3$? Only $3 \xrightarrow{y_2} 2$ goes from $3$ to $2$. So from $2$, the shortest path to $4 \to T^*$ is $S^* \to 2 \xrightarrow{x_2} 4 \to T^*$ of cost $5$!
   - Wait: can we do better than $8 + 5 = 13$? Let's check! If we hire $x_1 = 2$ (cost $8$) and $x_2 = 1$ (cost $5$), total cost is $13$:
     - Day 1: $x_1 = 2 \ge 2$ ($y_1 = 0$).
     - Day 2: $x_1 + x_2 = 2 + 1 = 3 \ge 3$ ($y_2 = 0$).
     - Day 3: $x_2 = 1 \ge 1$ ($y_3 = 0$).
     What if we hired $x_3 = 1$ (cost $7$) and $x_1 = 1$ (cost $4$) and $x_2 = 1$ (cost $5$)? That costs $16 > 13$. What if $x_3 = 3$? Cost $21$. So $(x_1, x_2, x_3) = (2, 1, 0)$ with $(y_1, y_2, y_3) = (0, 0, 0)$ and total cost $13$ is uniquely optimal!
   - What if instead $c_3 = 6$ (so hiring 1 full-span volunteer $x_3$ + 1 of $x_1$ + 0 of $x_2$ wouldn't cover day 2=3, wait: $x_3 = 1, x_1 = 1, x_2 = 1$ covers $2, 3, 2$). What if $A = (1, 1, 1)$? Then $b = (+1, 0, 0, -1)$: Path 1 sends $1$ unit along $1 \xrightarrow{x_1} 3 \xrightarrow{y_2} 2 \xrightarrow{x_2} 4$ (cost $4 + 0 + 5 = 9$, hiring $x_1=1, x_2=1$, giving surplus $y_2 = 1$ on Day 2!) vs. $1 \xrightarrow{x_3} 4$ (cost $7$, hiring $x_3=1$)! Notice how a path traversing the backward slack edge $3 \xrightarrow{y_2} 2$ physically represents **overlapping $x_1$ and $x_2$ on Day 2**, generating $y_2 = 1$ unit of surplus volunteer on Day 2!

---

### 30.4 Four Structural Archetypes of the Equation-Difference Method

The Equation-Difference Method is not a one-problem trick; it is a general compiler for any linear program whose constraint matrix has the **Consecutive-Ones Property (`连续 1 性质`)**. Let us catalog its four principal variations:

#### Archetype 30A: Interval Lower-Bound Coverage ($\sum_{i \ni t} x_i \ge A_t$, Minimize Cost)
- **Equation**: $\sum_{i : t \in [l_i, r_i]} x_i - y_t = A_t$ ($y_t \ge 0$).
- **Slack Edge Direction**: **Backward** $(t+1 \to t, \text{cap } \infty, \text{cost } 0)$ because $-y_t$ has $-1$ in $\Delta E_t$ and $+1$ in $\Delta E_{t+1}$.
- **Capacity on $x_i$**: If volunteer type $i$ has at most $u_i$ available people ($0 \le x_i \le u_i$), simply change the capacity of edge $(l_i \to r_i + 1)$ from $\infty$ to $u_i$!

#### Archetype 30B: Interval Upper-Bound Packing ($\sum_{i \ni t} x_i \le K_t$, Maximize Profit)
- **Canonical Problems**: `[Luogu P3358] 最长k可重区间集问题`, `CF 164 C — Machine Programming`, `CF 717 G — Underfail`.
- **Equation**: Each interval $i$ can be chosen at most once ($x_i \in [0, 1]$) with profit $w_i > 0$ (cost $-w_i$), and at most $K_t$ intervals can cover point $t$. Add a non-negative slack variable $+y_t \ge 0$ (representing **unused capacity** at time $t$):
  $$E_t : \quad \sum_{i \,:\, l_i \le t \le r_i} x_i + y_t = K_t \qquad (t = 1, \dots, n), \quad x_i \in [0, 1], \; y_t \ge 0.$$
- **Consecutive Difference $\Delta E_t = E_t - E_{t-1}$**:
  - Interval $x_i \in [0, 1]$: $+1$ in $\Delta E_{l_i}$ and $-1$ in $\Delta E_{r_i + 1} \implies$ edge $(l_i \to r_i + 1, \text{cap } 1, \text{cost } -w_i)$.
  - Slack $+y_t \ge 0$: **$+1$ in $\Delta E_t$ and $-1$ in $\Delta E_{t+1}$** $\implies$ **Forward slack edge** $(t \to t+1, \text{cap } \infty, \text{cost } 0)$!
  - RHS $b_t = K_t - K_{t-1}$: When $K_t = K$ is a constant for all $t \in \{1, \dots, n\}$, notice that $b_1 = K - 0 = +K$, $b_2 = \dots = b_n = 0$, and $b_{n+1} = 0 - K = -K$!
    So $S^*$ **only connects to vertex $1$ with capacity $K$**, and **only vertex $n+1$ connects to $T^*$ with capacity $K$**, while the entire graph is a **DAG** $1 \to 2 \to \dots \to n+1$!
  > **Unification Insight**: This explains why the classic "send $K$ units of flow from $1$ to $n+1$ along a chain of forward edges $t \to t+1$ and interval jumps $l_i \to r_i + 1$" works—it is literally the Equation-Difference compilation of $\sum_{i \ni t} x_i + y_t = K$!

#### Archetype 30C: Two-Sided Bounded Interval / Sliding-Window Coverage ($L_t \le \sum_{i \ni t} x_i \le R_t$)
- **Canonical Problems**: `[ICPC NEERC 2016 D / Luogu P6967] Delight for a Cat`, `BZOJ 1283 序列`.
- **Equation**: Suppose the sum of active variables at time $t$ must lie in a closed interval $[L_t, R_t]$:
  $$L_t \le \sum_{i \,:\, l_i \le t \le r_i} x_i \le R_t.$$
  How do we write both bounds with a **single** slack variable $y_t$?
  Write $\sum_{i \ni t} x_i - y_t = L_t$, and restrict the surplus $y_t$ to the **bounded capacity interval**:
  $$0 \le y_t \le R_t - L_t!$$
- **Compiled Graph**: Everything is identical to Archetype 30A ($b_t = L_t - L_{t-1}$), **except** the backward slack edge $y_t = (t+1 \to t, \text{cost } 0)$ now has **finite upper capacity $u(y_t) = R_t - L_t$** instead of $\infty$!
  *(Alternatively, write $\sum_{i \ni t} x_i + z_t = R_t$ with $0 \le z_t \le R_t - L_t$, which gives $b_t = R_t - R_{t-1}$ and a forward slack edge $t \to t+1$ of capacity $R_t - L_t$—and when $R_t = R$ is constant, $S^*$ only connects to $1$ and $n+1$ only connects to $T^*$!)*
- **Sliding-Window Translation**: What if the variables are point decisions $x_1, x_2, \dots, x_n \in \{0, 1\}$ and every sliding window of length $K$ satisfies $L_t \le \sum_{j=t}^{t+K-1} x_j \le R_t$ (for $t = 1, \dots, n - K + 1$)?
  Look at variable $x_j$: which window equations $E_t$ contain $x_j$?
  Window $E_t$ contains $x_j \iff t \le j \le t + K - 1 \iff j - K + 1 \le t \le j$!
  Thus, **each point variable $x_j$ covers the contiguous interval of window indices $\big[\max(1, j - K + 1),\; \min(n - K + 1, j)\big]$**! In the differenced system $\Delta E_t$, $x_j$ is simply a directed edge from $\max(1, j - K + 1)$ to $\min(n - K + 1, j) + 1$!

#### Archetype 30D: When Equation-Difference Fails (The Non-Contiguous Boundary)
What if variable $x_i$ covers **two disjoint intervals** of constraints, say $[1, 2] \cup [4, 5]$?
Then in the differenced system $\Delta E_t = E_t - E_{t-1}$, variable $x_i$ has:
- $+1$ in $\Delta E_1$, $-1$ in $\Delta E_3$, AND
- $+1$ in $\Delta E_4$, $-1$ in $\Delta E_6$!
Because $x_i$ appears with **two $+1$s and two $-1$s**, it would require two distinct edges $(1 \to 3)$ and $(4 \to 6)$ to carry the **exact same flow value** $f(1 \to 3) = f(4 \to 6) = x_i$ ("Equal-Flow / Coupled-Edge Problem"), which is **NP-hard** (reducible from 3-SAT and Exact Cover)!
> **Diagnostic Takeaway**: Before applying Equation-Difference, verify that in your ordering of the constraints $E_1, \dots, E_n$, every variable $x_i$ appears with coefficient $1$ in a **single contiguous range of equations $[l_i, r_i]$** (the **Consecutive-Ones Property**).

---

### 30.5 Master Recognition & Compilation Decision Table for Wave 3B (Iterations 26–30)

| Non-Graph Surface Signal in Problem Statement | Underlying Wave 3B Archetype | Intermediate Algebraic Model | Compiled MCMF Gadget & Potential Strategy | Complexity & Critical Pitfall |
| :--- | :--- | :--- | :--- | :--- |
| **"Maximize weight of $k$-overlap intervals / DAG paths"** ($N \le 2000$, negative costs $-w_i$) | **Iter 26 (Regime 2)** + **Iter 30B**: DAG Potential Initialization | $\sum_{i \ni t} x_i + y_t = K$, $x_i \in [0, 1]$ | Forward chain $t \to t+1$ (cap $\infty$, cost $0$), jump $l_i \to r_i+1$ (cap $1$, cost $-w_i$). **Initialize $\pi_0$ via $O(V+E)$ DAG DP**, then Dijkstra! | $O(V + E + K E \log V)$. **Pitfall**: Running SPFA inside the loop TLEs on dense interval tests (`CF 164 C`). |
| **"Choose any number of pairs/paths to maximize net profit"** or **"Output optimal cost for every $k = 1 \dots K$"** | **Iter 27**: Slope Convexity of $C(f)$ & Min-Cost Feasible Flow | $C(f)$ has non-decreasing marginal slopes $d_1 \le d_2 \le \dots \le d_F$ | Run SSP and record $C(k) = C(k-1) + d_k$ after each unit augmentation. For unconstrained max profit, **stop as soon as $d_k \ge 0$**. | $O(F^* E \log V)$. **Pitfall**: Running all the way to $F_{\max}$ forces unprofitable positive-cost paths. |
| **"Maximize number of pairs subject to total cost $\le 0$ (or total profit $\ge 0$)"** (`[SDOI2016] 数字配对`) | **Iter 27.2**: Budget-Threshold Prefix of Convex $C(f)$ | Maximize $f$ s.t. $\sum_{j \le f} d_j \le 0$ | Push all $d_k \le 0$ paths first; then push $d_k > 0$ paths in SSP order until $C_{\text{cur}} + \delta_k d_k > 0$, taking $\lfloor -C_{\text{cur}} / d_k \rfloor$ on the last path. | **Pitfall**: Stopping at $d_k > 0$ stops too early; must spend the accumulated negative-cost buffer! |
| **"Exactly $K$ paths/items when $N \le 10^5$ and graph is a tree or 1D array"** (`CF 802 O`, `CF 739 E`) | **Iter 27.3**: WQS Binary Search (Aliens Trick) on Flow Volume $f$ | $g(\lambda) = \min_f (C(f) - \lambda f)$; $C(K) = g(\lambda^*) + \lambda^* K$ | Attach penalty $-\lambda$ per unit of flow leaving $s$; solve unconstrained min-cost flow via Tree DP or Regret Heap in $O(N \log N)$. | $O(N \log N \log C)$. **Pitfall**: On collinear plateaus, must recover $g(\lambda^*) + \lambda^* K$, NOT $\text{TrueCost}(f(\lambda^*))$. |
| **"Every edge/vertex $e$ must be traversed at least $l_e$ and at most $u_e$ times at minimum cost"** (`[AHOI2014] 支线剧情`) | **Iter 28.1**: Lower-Bound Min-Cost Feasible/Max Flow (`上下界最小费用流`) | $f(e) = l_e + f'(e)$, $M(v) = \sum_{\delta^-(v)} l_e - \sum_{\delta^+(v)} l_e$ | Add $C_{\text{base}} = \sum l_e c_e$; connect $S^* \to v$ ($M(v)>0$) and $v \to T^*$ ($M(v)<0$); add $(t \to s, \infty, 0)$. Run MCMF $S^* \to T^*$. | **Pitfall**: Do not run Phase 2 ($s \to t$) if the problem wants minimum-cost feasible cover rather than max flow! |
| **"Graph has negative-cost cycles"** or **"Edge modification with $f_e > c_e$ (`CF 708 D`)"** | **Iter 28.2**: Mandatory Initial Saturation (`负权边强制满流消圈法`) | For $c_e < 0$, set $f(e) = u_e - \bar{f}(e)$ with $\bar{f}(e) \in [0, u_e - l_e]$ | Add $u_e c_e$ to $C_{\text{base}}$, update $M(u) \mathrel{-}= u_e, M(v) \mathrel{+}= u_e$, and add **reverse edge** $(v \to u, \text{cap } u_e - l_e, \text{cost } -c_e > 0)$. Then $\pi_0 = 0$! | Eliminates all negative cycles & SPFA in $O(V+E)$ setup! **Pitfall**: Never pre-saturate an edge with $u_e = \infty$. |
| **"Maximize 3-cycles in tournament (`[WC2007] 剪刀石头布`)"** or **"Cost is $\sum a_i d_i^2$ / $\sum (C_i W_i^2 + D_i L_i^2)$"** | **Iter 29**: Convex Marginal Edge Splitting (`凸费用拆边`) | $\binom{n}{3} - \sum_v \binom{d^+(v)}{2}$; $g(f_e) = \sum_{k=1}^{f_e} \Delta g(k)$ with $\Delta^2 g \ge 0$ | Replace $e$ by $U$ parallel unit edges of cost $\Delta g(1) \le \Delta g(2) \le \dots \le \Delta g(U)$. Eliminate coupled $L_i = T_i - W_i$ first! | **Pitfall**: Fails completely if $g$ is concave ($\Delta g(1) > \Delta g(2)$). Watch $0$-indexed marginal $\Delta \binom{k}{2} = k-1$. |
| **"Hire intervals $[l_i, r_i]$ at cost $c_i$ so every day $t$ has $\ge A_t$ (or $\in [L_t, R_t]$) coverage"** (`[NOI2008] 志愿者招募`, `NEERC 2016 D`) | **Iter 30**: Consecutive Equation-Difference Method (`流守恒差分建模法`) | $E_t : \sum_{i \ni t} x_i - y_t = L_t$ ($0 \le y_t \le R_t - L_t$); take $\Delta E_t = E_t - E_{t-1}$ | Vertices $1 \dots n+1$; $x_i$ is edge $(l_i \to r_i+1, \infty, c_i)$; slack $y_t$ is backward edge $(t+1 \to t, \text{cap } R_t - L_t, \text{cost } 0)$; $b_t = L_t - L_{t-1}$. | **Pitfall**: Pad with $E_{n+1} : 0 = 0$ (need $n+1$ vertices!). Requires contiguous intervals (Consecutive-Ones Property). |

---

## 4-Tier Curated Problem Bank (Part 1: Stepping Stone & Intermediate — 11 Fully Solved Problems)

> [!NOTE]
> **Problem Bank Structure & Pedagogical Contract**
> Every problem below is a non-template modelling problem (bare templates are quarantined at the end of the monograph in `R-26..R-33`). Each entry explicitly executes the **4-Step "Zero Magic Gadgets" Compilation** (Step 1: Non-Graph Diagnostic Signal $\to$ Step 2: Algebraic Intermediate Representation $\to$ Step 3: Mechanical Graph Compilation $\to$ Step 4: Failure Mode / Direction B Comparison) followed by **3-Tier Progressive Hints**.

---

### Tier 1: Stepping Stone (5 Problems)

---

#### Problem 1.1 — Circular Warehouse Load Balancing (`[Luogu P4016 / 网络流24题] 负载平衡问题`)
- **Judge & URL**: [Luogu P4016](https://www.luogu.com.cn/problem/P4016) (`[ZH]` 网络流 24 题 — 负载平衡问题)
- **Inline Statement & Constraints**:
  $n$ ($1 \le n \le 100$) warehouses are arranged in a circle ($1$ adjacent to $2$, $\dots$, $n$ adjacent to $1$). Warehouse $i$ initially holds $a_i \in \mathbb{Z}_{\ge 0}$ boxes, where $\bar{a} = \frac{1}{n}\sum_{i=1}^n a_i$ is guaranteed to be an integer. Moving $1$ box between adjacent warehouses $i$ and $(i \bmod n) + 1$ costs $1$. Find the minimum total cost so that every warehouse ends with exactly $\bar{a}$ boxes.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Non-Graph Diagnostic Signal)**:
     We have conservation of mass on a ring with linear per-unit transport cost $1$. While the 1D ring case can also be solved in $O(n \log n)$ via median math (Direction B), its algebraic formulation is the cleanest introductory example of reading flow conservation directly from net balance equations $a_i - \bar{a}$.
  2. **Step 2 (Algebraic Intermediate Representation)**:
     Let $f_{i, i+1} \ge 0$ and $f_{i+1, i} \ge 0$ denote the number of boxes shipped clockwise ($i \to i+1$) and counter-clockwise ($i+1 \to i$). At each warehouse $i \in \{1, \dots, n\}$, total boxes leaving minus total boxes entering must equal the initial surplus $b_i := a_i - \bar{a}$:
     $$(f_{i, i+1} + f_{i, i-1}) - (f_{i-1, i} + f_{i+1, i}) = a_i - \bar{a} =: b_i,$$
     minimizing $\sum_{i=1}^n (f_{i, i+1} + f_{i+1, i})$.
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Create vertices $1, \dots, n$ plus super-source $S$ and super-sink $T$.
     - For each $i \in \{1, \dots, n\}$:
       - If $b_i = a_i - \bar{a} > 0$ (surplus): add $(S \to i, \text{cap } b_i, \text{cost } 0)$.
       - If $b_i = a_i - \bar{a} < 0$ (deficit): add $(i \to T, \text{cap } -b_i, \text{cost } 0)$.
     - For each adjacent pair $(i, i+1)$ (wrapping $n+1 \equiv 1$), add two independent directed edges $(i \to i+1, \text{cap } \infty, \text{cost } 1)$ and $(i+1 \to i, \text{cap } \infty, \text{cost } 1)$.
     - All costs are $\ge 0$, so initialize $\pi_0 = 0$ and run Dijkstra MCMF in $O(n^2 \log n)$.
  4. **Step 4 (Direction B Comparison & Failure Mode)**:
     - **Direction B ($O(n \log n)$ Median Elimination)**: Setting $x_i = f_{i, i+1} - f_{i+1, i}$ gives $x_i - x_{i-1} = b_i \implies x_i = x_n + \sum_{j=1}^i b_j = x_n + S_i$, minimizing $\sum_{i=1}^n |x_n + S_i|$, which is minimized when $-x_n$ is the median of the prefix sums $\{S_1, \dots, S_n\}$! However, the MCMF formulation generalizes immediately to arbitrary graphs where no 1D prefix-sum parametrization exists.
     - **Failure Mode**: Never merge $(i \to i+1, \infty, 1)$ and $(i+1 \to i, \infty, 1)$ into a single residual edge pair where the reverse arc starts with capacity $\infty$ and cost $-1$!

- **3-Tier Progressive Hints**:
  - *Hint 1*: Write the conservation equation at warehouse $i$: what must $\text{OutFlow}(i) - \text{InFlow}(i)$ equal so that warehouse $i$ ends with $\bar{a}$ boxes?
  - *Hint 2*: Separate warehouses with $a_i > \bar{a}$ (sources of excess boxes) from warehouses with $a_i < \bar{a}$ (sinks of needed boxes).
  - *Hint 3*: Connect $S \to i$ with capacity $a_i - \bar{a}$ when $a_i > \bar{a}$, connect $i \to T$ with capacity $\bar{a} - a_i$ when $a_i < \bar{a}$, and add unit-cost $\infty$-capacity directed edges in both directions around the cycle.

---

#### Problem 1.2 — $K$-Path Grid Collection (`[POJ 3422 / Luogu P2045] Kaka's Matrix Travels / 方格取数加强版`)
- **Judge & URL**: [Luogu P2045](https://www.luogu.com.cn/problem/P2045) / POJ 3422
- **Inline Statement & Constraints**:
  Given an $n \times n$ grid ($1 \le n \le 50$) of non-negative integers $A_{i,j} \ge 0$, walk $K$ times ($1 \le K \le 10$) from $(1, 1)$ to $(n, n)$ moving only right $(i, j+1)$ or down $(i+1, j)$. When a cell $(i, j)$ is visited for the **first** time, you collect $A_{i,j}$ points and the cell's value becomes $0$ for all subsequent visits. Maximize the total points collected across the $K$ paths.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Non-Graph Diagnostic Signal)**:
     With $K=1$ this is trivial grid DP; with $K=2$ it is $O(n^3)$ two-walker DP; with $K=10$, DP requires $O(n^{K+1})$ states! However, the reward at cell $(i, j)$ as a function of visit count $v_{i,j} \in \{0, 1, \dots, K\}$ is **concave reward** $R(v) = A_{i,j} \cdot \min(v, 1)$, which when negated for minimization becomes a **piecewise-linear convex cost** $g(v) = -A_{i,j} \cdot \min(v, 1)$ with marginal increments $\Delta g(1) = -A_{i,j} \le \Delta g(2) = 0 = \dots = \Delta g(K)$!
  2. **Step 2 (Algebraic Intermediate Representation)**:
     Let $v_{i,j} \in \{0, 1, \dots, K\}$ be the number of paths passing through cell $(i, j)$. By Iteration 29, the convex vertex cost $g(v_{i,j})$ splits into two marginal segments:
     - First visit ($k = 1$): capacity $1$, cost $\Delta g(1) = -A_{i,j}$.
     - Remaining $K-1$ visits ($k = 2 \dots K$, identical slope $0$): bundled into a single edge of capacity $K-1$ and cost $0$!
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Split each cell $(i, j)$ into $(i, j)_{\text{in}}$ and $(i, j)_{\text{out}}$.
     - Add **two parallel edges** from $(i, j)_{\text{in}}$ to $(i, j)_{\text{out}}$:
       $$e_1 = \big(\text{cap } 1, \text{cost } -A_{i,j}\big), \qquad e_2 = \big(\text{cap } K - 1, \text{cost } 0\big).$$
     - From $(i, j)_{\text{out}}$, add movement edges to $(i+1, j)_{\text{in}}$ and $(i, j+1)_{\text{in}}$ with capacity $K$ and cost $0$.
     - Set $S = (1, 1)_{\text{in}}$, $T = (n, n)_{\text{out}}$. Because the grid moves only right and down, the initial network is a **DAG**! Initialize Johnson potentials $\pi_0$ via $O(n^2)$ grid DP in row-major order $(i = 1 \dots n, j = 1 \dots n)$, then run $K$ steps of Dijkstra in $O(K n^2 \log n)$.
  4. **Step 4 (Failure Mode)**:
     If a programmer puts only a single edge of capacity $1$ between $(i, j)_{\text{in}}$ and $(i, j)_{\text{out}}$, paths become strictly vertex-disjoint and cannot even exit $(1, 1)$ or enter $(n, n)$ for $K \ge 3$! The second parallel edge $(K-1, 0)$ is essential to allow paths to share cells without double-counting $A_{i,j}$.

- **3-Tier Progressive Hints**:
  - *Hint 1*: How does the marginal reward of visiting cell $(i, j)$ change from the 1st visit to the 2nd, 3rd, $\dots, K$-th visit?
  - *Hint 2*: Split each vertex into `in` and `out` and apply Iteration 29 (Convex Marginal Edge Splitting) to the visit count $v_{i,j} \in [0, K]$.
  - *Hint 3*: Combine the $K-1$ zero-cost marginal edges into a single edge of capacity $K-1$ and cost $0$ alongside the $(1, -A_{i,j})$ edge, and compute initial potentials $\pi_0$ by simple row-by-row grid DP.

---

#### Problem 1.3 — Maximum-Weight $k$-Overlap Interval Packing (`[Luogu P3358 / 网络流24题] 最长k可重区间集问题`)
- **Judge & URL**: [Luogu P3358](https://www.luogu.com.cn/problem/P3358) (`[ZH]` 网络流 24 题 — 最长 $k$ 可重区间集问题)
- **Inline Statement & Constraints**:
  Given $n \le 500$ open intervals $(l_i, r_i)$ on the real line with weight $w_i = r_i - l_i > 0$ (or arbitrary $w_i > 0$) and an integer $k \le 10$, select a subset of intervals of maximum total weight such that no point $x \in \mathbb{R}$ is covered by more than $k$ selected intervals.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Non-Graph Diagnostic Signal)**:
     For $k = 1$, this is weighted interval scheduling ($O(n \log n)$ DP). For $k \ge 2$, DP must remember the right endpoints of all $k$ currently active intervals ($O(n^k)$ states!). This is **Archetype 30B (Interval Upper-Bound Packing)**: $\sum_{i : t \in [l_i, r_i-1]} x_i \le k$.
  2. **Step 2 (Algebraic Intermediate Representation)**:
     Coordinate-compress the $2n$ distinct endpoints into $m \le 2n$ sorted positions $1 < 2 < \dots < m$, so each open interval $(l_i, r_i)$ covers the elementary segments $t \in [L_i, R_i - 1]$ ($1 \le L_i < R_i \le m$). Adding slack $y_t \ge 0$ for each segment $t \in \{1, \dots, m-1\}$:
     $$E_t : \quad \sum_{i \,:\, L_i \le t \le R_i - 1} x_i + y_t = k \qquad (t = 1, \dots, m-1), \quad x_i \in [0, 1].$$
     Taking $\Delta E_t = E_t - E_{t-1}$ ($t = 1, \dots, m$, with $E_0 = E_m = 0$) gives:
     - $x_i$: $+1$ at $L_i$, $-1$ at $R_i$, cost $-w_i$, capacity $1$.
     - $y_t$: $+1$ at $t$, $-1$ at $t+1$, cost $0$, capacity $\infty$.
     - RHS: $+k$ at $t = 1$, $-k$ at $t = m$, and $0$ everywhere else!
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Create vertices $1, 2, \dots, m$, source $S$, sink $T$.
     - Add $(S \to 1, \text{cap } k, \text{cost } 0)$ and $(m \to T, \text{cap } k, \text{cost } 0)$.
     - For $t = 1, \dots, m-1$, add forward slack edge $(t \to t+1, \text{cap } \infty, \text{cost } 0)$.
     - For each interval $i$, add jump edge $(L_i \to R_i, \text{cap } 1, \text{cost } -w_i)$.
     - Since every edge goes strictly from a smaller index to a larger index ($u < v$), the graph is a **topological DAG** $(1, 2, \dots, m)$! Compute $\pi_0(v) = \min_{u < v} (\pi_0(u) + c(u,v))$ for $v = 1 \dots m$ in $O(n + m)$ time, then run $k$ steps of Dijkstra in $O(k(n + m) \log m)$!
  4. **Step 4 (Failure Mode — Open vs. Closed Intervals)**:
     If intervals are **open** $(l_i, r_i)$, two intervals $(1, 3)$ and $(3, 5)$ do **not** overlap at $3$, so the jump edge goes directly from compressed coordinate $L_i$ to $R_i$. If a problem specifies **closed** intervals $[l_i, r_i]$ where $[1, 3]$ and $[3, 5]$ **do** overlap at $3$, either replace $[l_i, r_i]$ by $[l_i, r_i + 1)$ before coordinate compression, or connect $L_i \to R_i + 1$!

- **3-Tier Progressive Hints**:
  - *Hint 1*: Coordinate-compress all endpoints into $m \le 2n$ indices and write the overlap constraint on each elementary interval $[t, t+1)$.
  - *Hint 2*: Apply Iteration 30B ($\sum_{i \ni t} x_i + y_t = k$ and $\Delta E_t = E_t - E_{t-1}$) to compile intervals into jump edges $L_i \to R_i$ and slack variables into chain edges $t \to t+1$.
  - *Hint 3*: Because $L_i < R_i$ and $t < t+1$, the initial network is already topologically sorted! Compute $\pi_0$ by a simple forward loop $t = 1 \dots m$ and run Dijkstra $k$ times.

---

#### Problem 1.4 — Exact Vertex Visit Lower Bounds (`[Luogu P4553] 80人环游世界`)
- **Judge & URL**: [Luogu P4553](https://www.luogu.com.cn/problem/P4553) (`[ZH]` 80人环游世界)
- **Inline Statement & Constraints**:
  There are $n \le 100$ cities arranged in a topological order, and $m \le 80$ travelers. Each traveler can start at any city, travel along directed flights $(u \to v)$ ($u < v$) of cost $c(u, v) \ge 0$, and stop at any city (or not travel at all). City $i$ must be visited by **exactly $V_i$** travelers in total. Find the minimum total flight cost.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Non-Graph Diagnostic Signal)**:
     "At most $m$ paths in a DAG such that vertex $i$ is covered **exactly $V_i$ times** at minimum cost." This is an exact **Lower- and Upper-Bound Min-Cost Feasible Flow** (`有源汇上下界最小费用可行流`, Iteration 28, Engine 28B).
  2. **Step 2 (Algebraic Intermediate Representation)**:
     Split each city $i$ into $i_{\text{in}} \to i_{\text{out}}$ with lower bound $l_i = V_i$, upper bound $u_i = V_i$, and cost $0$:
     $$V_i \le f(i_{\text{in}} \to i_{\text{out}}) \le V_i.$$
     Notice $u_i - l_i = 0$! That means in the shifted flow $f'(e) = f(e) - l_e$, the edge $(i_{\text{in}} \to i_{\text{out}})$ has free capacity $0$ and simply injects a fixed imbalance $M(i_{\text{out}}) = +V_i$ and $M(i_{\text{in}}) = -V_i$!
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Create source $s_0$, sink $t$, and an intermediate dispatch hub $s$ with edge $(s_0 \to s, \text{cap } [0, m], \text{cost } 0)$ to cap the total number of travelers at $m$.
     - From $s$, add $(s \to i_{\text{in}}, [0, \infty), \text{cost } 0)$ (traveler starts at $i$); from $i_{\text{out}}$, add $(i_{\text{out}} \to t, [0, \infty), \text{cost } 0)$ (traveler ends at $i$).
     - For each flight $(u \to v)$, add $(u_{\text{out}} \to v_{\text{in}}, [0, \infty), \text{cost } c(u, v))$.
     - For each city $i$, the exact bound $[V_i, V_i]$ on $i_{\text{in}} \to i_{\text{out}}$ sets $M(i_{\text{out}}) = +V_i$ (add $S^* \to i_{\text{out}}$ of cap $V_i, \text{cost } 0$) and $M(i_{\text{in}}) = -V_i$ (add $i_{\text{in}} \to T^*$ of cap $V_i, \text{cost } 0$).
     - Add the circulation feedback edge $(t \to s_0, [0, \infty), \text{cost } 0)$ and run **Engine 28B (Phase 1 only!)** from $S^*$ to $T^*$. The minimum cost of the $S^* \to T^*$ max flow is the answer!
  4. **Step 4 (Failure Mode)**:
     Do **NOT** run Phase 2 ($s_0 \to t$ max flow)! The problem requires at most $m$ travelers (not necessarily all $m$ travelers if fewer can cover all $V_i$), and since $u_i - l_i = 0$ on every city vertex, no further $s_0 \to t$ flow can pass through the cities anyway.

- **3-Tier Progressive Hints**:
  - *Hint 1*: How do you enforce that a vertex $i$ is visited at least $V_i$ and at most $V_i$ times? Split $i$ into $i_{\text{in}} \to i_{\text{out}}$ with capacity interval $[V_i, V_i]$.
  - *Hint 2*: Apply Iteration 28 (`有源汇上下界最小费用可行流`): how do you cap the total number of travelers at $m$ using a bottleneck edge $(s_0 \to s, [0, m], 0)$?
  - *Hint 3*: Notice that $u_e - l_e = V_i - V_i = 0$ on $(i_{\text{in}} \to i_{\text{out}})$, so you only need $(S^* \to i_{\text{out}}, V_i, 0)$, $(i_{\text{in}} \to T^*, V_i, 0)$, and $(t \to s_0, \infty, 0)$, then run a single MCMF from $S^*$ to $T^*$.

---

#### Problem 1.5 — Full Convex Slope Profile of Team Size (`[AtCoder ABC 247 G] Dream Team`)
- **Judge & URL**: [AtCoder ABC 247 G — Dream Team](https://atcoder.jp/contests/abc247/tasks/abc247_g) (`[JA]`)
- **Inline Statement & Constraints**:
  There are $N \le 3 \times 10^4$ candidates. Candidate $i$ belongs to university $A_i \in \{1, \dots, 150\}$, specializes in subject $B_i \in \{1, \dots, 150\}$, and has power $C_i \in [1, 10^9]$. You want to form a team where no two members share the same university and no two members share the same subject. Let $K_{\max} \le 150$ be the maximum possible team size. **For every integer $k = 1, 2, \dots, K_{\max}$**, find the maximum total power of a valid team of size **exactly $k$**.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Non-Graph Diagnostic Signal)**:
     "No two share $A_i$ and no two share $B_i$" is bipartite matching between universities $L = \{1, \dots, 150\}$ and subjects $R = \{1, \dots, 150\}$. Asking for the optimum for **every** cardinality $k = 1, 2, \dots, K_{\max}$ is the signature application of **Iteration 27 (Theorem 27.1: Slope Convexity of $C(f)$ via SSP)**: each unit augmentation step $k$ of SSP produces the exact global optimum for flow volume $k$!
  2. **Step 2 (Algebraic Intermediate Representation)**:
     For each pair $(u, v) \in \{1, \dots, 150\}^2$, at most $1$ candidate with $(A_i, B_i) = (u, v)$ can ever be chosen, so we pre-filter to keep only the single maximum-power candidate $C_{\max}(u, v)$ for each pair $(u, v)$. Negate costs to $c(u, v) = -C_{\max}(u, v)$ (or shift by $M - C_{\max}(u, v) \ge 0$ where $M = 10^9$ so all costs are non-negative!).
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Create $S$, left vertices $L_1 \dots L_{150}$, right vertices $R_1 \dots R_{150}$, and $T$.
     - Add $(S \to L_u, \text{cap } 1, \text{cost } 0)$ and $(R_v \to T, \text{cap } 1, \text{cost } 0)$.
     - For each occupied pair $(u, v)$, add $(L_u \to R_v, \text{cap } 1, \text{cost } M - C_{\max}(u, v) \ge 0)$.
     - Run SSP + Dijkstra one unit at a time! After the $k$-th unit augmentation (with total shifted cost $C_{\text{shifted}}(k)$), the maximum team power for size $k$ is:
       $$\text{Ans}(k) = k \cdot M - C_{\text{shifted}}(k).$$
     - Since $|V| \le 302$ and $K_{\max} \le 150$, running 150 Dijkstra calls takes $< 5\text{ ms}$!
  4. **Step 4 (Failure Mode)**:
     If you use Zkw Primal–Dual or push multiple flow units in a single step without unrolling them one by one, you must interpolate the linear segment of slope $d_k$ between flow $f_{\text{prev}}$ and $f_{\text{prev}} + \delta_k$: for each $j \in [1, \delta_k]$, $C(f_{\text{prev}} + j) = C(f_{\text{prev}}) + j \cdot d_k$.

- **3-Tier Progressive Hints**:
  - *Hint 1*: Model universities as left vertices $L_1 \dots L_{150}$ and subjects as right vertices $R_1 \dots R_{150}$ in a bipartite graph.
  - *Hint 2*: Why do you not need to re-run MCMF $150$ separate times for $k = 1, 2, \dots, K_{\max}$? Recall Corollary 26.4 and Theorem 27.1.
  - *Hint 3*: Shift edge costs to $10^9 - C_i \ge 0$ so $\pi_0 = 0$, run SSP with Dijkstra, and read off $\text{Ans}(k) = k \cdot 10^9 - C(k)$ after the $k$-th unit of flow reaches $T$.

---

### Tier 2: Intermediate (6 Problems)

---

#### Problem 2.1 — Tournament 3-Cycle Maximization (`[WC2007 / Luogu P4249] 剪刀石头布`)
- **Judge & URL**: [Luogu P4249](https://www.luogu.com.cn/problem/P4249) (`[ZH]` WC2007 剪刀石头布)
- **Inline Statement & Constraints**:
  Given an $n \times n$ ($n \le 100$) tournament matrix where some match outcomes between $\{u, v\}$ are fixed ($u \to v$ or $v \to u$) and others are undecided ($A_{u,v} = 2$), orient all undecided matches to maximize the total number of directed 3-cycles, and output both the maximum count and the completed $n \times n$ matrix.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal)**:
     Direct 3-cycle counting couples 3 edges; complement counting (Section 29.2) notes that a triple $\{u, v, w\}$ fails to form a 3-cycle iff one vertex beats the other two, contributing $\binom{d^+(v)}{2}$ transitive triples.
  2. **Step 2 (Algebraic Intermediate)**:
     $$\max \#(\text{3-cycles}) = \binom{n}{3} - \min \sum_{v=1}^n \binom{d^+(v)}{2}, \qquad \Delta \binom{k}{2} = k - 1 \quad (k = 1, \dots, n-1).$$
  3. **Step 3 (Mechanical Graph Compilation)**:
     - For every undecided match $e = \{u, v\}$ ($u < v$), create vertex $m_e$ with $(S \to m_e, 1, 0)$, $(m_e \to u, 1, 0)$, $(m_e \to v, 1, 0)$.
     - For every player $v \in \{1, \dots, n\}$ with $w_0(v)$ already-fixed wins and $\text{free}(v)$ undecided matches, add $\text{free}(v)$ parallel unit-capacity edges from $v$ to $T$ with costs $w_0(v), w_0(v)+1, \dots, w_0(v) + \text{free}(v) - 1$.
     - Since all costs are $\ge 0$, set $\pi_0 = 0$ and run Zkw Primal–Dual or SSP+Dijkstra. Check which of $(m_e \to u)$ or $(m_e \to v)$ is saturated to output the completed matrix.
  4. **Step 4 (Complexity & Zkw Advantage)**:
     Here $|V| \le \binom{100}{2} + 102 \approx 5052$, $F \le 4950$, and all paths have length $3$ with small integer costs in $[0, 98]$. Because many paths share identical marginal costs, Zkw Primal–Dual pushes dozens of paths per phase and finishes in $< 20\text{ ms}$.

- **3-Tier Progressive Hints**:
  - *Hint 1*: Instead of counting 3-cycles directly, count triples $\{u, v, w\}$ that do **not** form a 3-cycle. How many outgoing edges inside $\{u, v, w\}$ do the three vertices have in a non-cycle?
  - *Hint 2*: Express the total number of non-3-cycles purely in terms of the out-degrees $d^+(v)$ of the $n$ vertices: $\sum_{v=1}^n \binom{d^+(v)}{2}$.
  - *Hint 3*: Apply Iteration 29 (Convex Marginal Edge Splitting): since $\binom{k}{2} - \binom{k-1}{2} = k-1$, split each player's out-degree into parallel unit edges of cost $0, 1, 2, \dots, n-2$.

---

#### Problem 2.2 — Coupled Win/Loss Sports League Budgets (`[JSOI2009 / Luogu P4307] 球队收益 / 球队预算`)
- **Judge & URL**: [Luogu P4307](https://www.luogu.com.cn/problem/P4307) (`[ZH]` JSOI2009 球队收益 / 球队预算)
- **Inline Statement & Constraints**:
  In a league of $n \le 5000$ teams and $m \le 1000$ remaining matches, team $i$ currently has $w_i$ wins and $l_i$ losses. If team $i$ finishes the season with $W_i$ wins and $L_i$ losses, its expenditure is $C_i W_i^2 + D_i L_i^2$ ($C_i, D_i \ge 0$). Orient the $m$ remaining matches to minimize total league expenditure.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal)**:
     Each remaining match $e = \{u, v\}$ assigns $+1$ win to one team and $+1$ loss to the other. A naive graph cannot track wins and losses simultaneously on separate edges because every match couples $+1$ win at $u$ with $+1$ loss at $v$.
  2. **Step 2 (Algebraic Intermediate — Invariant Elimination)**:
     As derived in Section 29.3, let $rem_i$ be the number of remaining matches involving team $i$. Then $T_i = w_i + l_i + rem_i = W_i + L_i$ is constant! Substituting $L_i = T_i - W_i$ makes the cost of team $i$ a function of $W_i$ alone:
     $$g_i(W_i) = C_i W_i^2 + D_i(T_i - W_i)^2, \qquad \Delta g_i(k) = 2(C_i + D_i)k - C_i - D_i - 2 D_i T_i.$$
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Initialize base cost assuming all remaining matches are losses for both sides (wait: assuming $W_i = w_i$ and $L_i = T_i - w_i = l_i + rem_i$ for every team $i$):
       $$\text{Base} = \sum_{i=1}^n \big(C_i w_i^2 + D_i (l_i + rem_i)^2\big).$$
     - For each remaining match $e = \{u, v\}$, add $(S \to m_e, 1, 0)$, $(m_e \to u, 1, 0)$, $(m_e \to v, 1, 0)$.
     - For each team $i$, for $k = w_i + 1, \dots, w_i + rem_i$, add unit edge $(i \to T, \text{cap } 1, \text{cost } \Delta g_i(k))$.
     - Run MCMF of volume $m$ (using DAG DP for $\pi_0$: $\pi_0(S)=\pi_0(m_e)=\pi_0(i)=0$ and $\pi_0(T) = \min_{i, k} \Delta g_i(k)$!).
  4. **Step 4 (Failure Mode)**:
     Make sure $\text{Base}$ initializes each team's losses to $L_i^{\text{init}} = l_i + rem_i$ (not $l_i$!), because $W_i = w_i$ corresponds to losing all $rem_i$ remaining matches ($L_i = T_i - w_i = l_i + rem_i$). Every unit of flow into team $i$ then converts one of those pre-assumed losses into a win!

- **3-Tier Progressive Hints**:
  - *Hint 1*: For a fixed team $i$, what is the sum $W_i + L_i$ at the end of the season? Notice that it does not depend on the match outcomes!
  - *Hint 2*: Substitute $L_i = (w_i + l_i + rem_i) - W_i$ into $C_i W_i^2 + D_i L_i^2$ so that team $i$'s cost depends only on its final wins $W_i$.
  - *Hint 3*: Pre-assume every team loses all $rem_i$ remaining matches for the base cost, and for each team $i$ add $rem_i$ parallel edges to $T$ with marginal cost $g_i(k) - g_i(k-1)$ for $k = w_i + 1 \dots w_i + rem_i$.

---

#### Problem 2.3 — Interval Packing with Anti-SPFA Tests (`[Codeforces 164 C] Machine Programming`)
- **Judge & URL**: [Codeforces 164C — Machine Programming](https://codeforces.com/problemset/problem/164/C) (`[EN]`)
- **Inline Statement & Constraints**:
  There are $n \le 1000$ tasks and $k \le 50$ identical machines. Task $i$ starts at time $s_i$, lasts $t_i$ seconds (occupying $[s_i, s_i + t_i - 1]$), and yields profit $c_i \in [1, 10^6]$. Each machine can process at most one task at a time. Select a subset of tasks to maximize total profit, and output the $0/1$ indicator vector of chosen tasks.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal)**:
     Identical mathematical model to Problem 1.3 (`Luogu P3358`), except $n = 1000, k = 50$, and Codeforces System Tests include dense nested interval configurations specifically engineered to make SPFA-based MCMF exceed the time limit! This problem tests **Iteration 26 (Regime 2: DAG Topological DP Potential Initialization)** + **Iteration 30B (Equation-Difference)**.
  2. **Step 2 (Algebraic Intermediate)**:
     Coordinate-compress all $s_i$ and $s_i + t_i$ into $m \le 2n$ sorted time points $1 < 2 < \dots < m$. Equation-Difference on $\sum_{i : L_i \le t < R_i} x_i + y_t = k$ yields jump edges $(L_i \to R_i, \text{cap } 1, \text{cost } -c_i)$ and chain edges $(t \to t+1, \text{cap } \infty, \text{cost } 0)$.
  3. **Step 3 (Mechanical Graph Compilation & DAG DP)**:
     - Build the DAG on vertices $1 \dots m$ with $S = 1, T = m$ (limiting total flow to $k$ via a source gate $S_0 \to 1$ of capacity $k$).
     - **Initialize $\pi_0$ via $O(n + m)$ forward DP**:
       $$\pi_0(1) = 0; \qquad \text{for } u = 1 \dots m-1: \quad \pi_0(u+1) \gets \min\big(\pi_0(u+1), \pi_0(u)\big),$$
       and for each task $i$ starting at $L_i = u$: $\pi_0(R_i) \gets \min\big(\pi_0(R_i), \pi_0(L_i) - c_i\big)$.
     - Run $k \le 50$ iterations of $O(m^2)$ or $O((n+m)\log m)$ Dijkstra! Total operations: $\approx 50 \times 3000 \log_2(2000) \approx 1.5 \times 10^6$, running in $15\text{ ms}$!
  4. **Step 4 (Primal Variable Recovery)**:
     Store the edge index `edge_id[i]` for each task $i$'s jump edge $(L_i \to R_i)$. After MCMF terminates, task $i$ is selected iff its jump edge has residual capacity $0$ (i.e., `flow(edge_id[i]) == 1`).

- **3-Tier Progressive Hints**:
  - *Hint 1*: Model the $k$ machines using Iteration 30B on the coordinate-compressed intervals $[s_i, s_i + t_i)$.
  - *Hint 2*: Why does SPFA TLE on $n = 1000, k = 50$? Notice that before any flow is pushed, all edges go from smaller time coordinates to larger time coordinates!
  - *Hint 3*: Compute initial potentials $\pi_0(1 \dots m)$ in $O(n + m)$ via a single forward pass over the sorted time points, then use Dijkstra for all $k$ augmentations.

---

#### Problem 2.4 — Minimum-Cost DAG Edge Cover (`[AHOI2014 / JSOI2014 / Luogu P4043] 支线剧情`)
- **Judge & URL**: [Luogu P4043](https://www.luogu.com.cn/problem/P4043) (`[ZH]` AHOI2014 / JSOI2014 支线剧情)
- **Inline Statement & Constraints**:
  A video game has $n \le 300$ plot nodes ($1$ is the starting node). From node $u$, there are $K_u$ outgoing storyline branches; branch $j$ leads to node $v_{u,j}$ ($v_{u,j} > u$) and takes $t_{u,j} \ge 0$ minutes to play. Starting a new playthrough always begins at node $1$, and a playthrough can be ended at any node $u \ge 2$ at cost $0$. Find the minimum total time required to experience **every storyline branch at least once**.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal)**:
     "Cover every directed edge $e = (u \to v)$ at least once ($l_e = 1, u_e = \infty$) using paths starting at $1$ and ending anywhere, minimizing total edge cost." This is the textbook archetype of **Iteration 28, Engine 28B (`有源汇上下界最小费用可行流`)**.
  2. **Step 2 (Algebraic Intermediate)**:
     Each storyline edge $e = (u \to v)$ has lower bound $l_e = 1$, upper bound $u_e = \infty$, and cost $t_e$. A playthrough can end at any node $u \ge 2$, which corresponds to an edge $(u \to T, \text{cap } [0, \infty), \text{cost } 0)$ from every node $u \ge 2$ to the sink $T$, with source $S = 1$.
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Set source $s = 1$, sink $t = n + 1$.
     - For every storyline branch $e = (u \to v, \text{time } t_e)$:
       - Base cost $C_{\text{base}} \mathrel{+}= 1 \cdot t_e$; imbalance $M(u) \mathrel{-}= 1$, $M(v) \mathrel{+}= 1$.
       - Add free-flow edge $(u \to v, \text{cap } \infty, \text{cost } t_e)$.
     - For every node $u \in \{2, \dots, n\}$, add $(u \to t, \text{cap } \infty, \text{cost } 0)$ (ending a game at $u$).
     - Add the circulation feedback edge $(t \to s, \text{cap } \infty, \text{cost } 0)$.
     - Connect $S^* \to v$ (for $M(v) > 0$) and $u \to T^*$ (for $M(u) < 0$), and run a single MCMF from $S^*$ to $T^*$! Output $C_{\text{base}} + C^*$.
  4. **Step 4 (Failure Mode)**:
     Remember Broken Gadget 28C: **do NOT run Phase 2 ($s \to t$ max flow)**! We want the minimum-cost feasible flow that satisfies all $l_e \ge 1$, which is already complete at the end of Phase 1 ($S^* \to T^*$).

- **3-Tier Progressive Hints**:
  - *Hint 1*: Every storyline branch is a directed edge $(u \to v)$ with flow lower bound $l_e = 1$ and upper bound $u_e = \infty$.
  - *Hint 2*: Since a playthrough can stop at any node $u \ge 2$, add a $0$-cost edge $(u \to t, [0, \infty), 0)$ from each node $u$ to an artificial sink $t$, and a feedback edge $(t \to 1, [0, \infty), 0)$.
  - *Hint 3*: Compute $M(u) = \text{in\_deg}(u) - \text{out\_deg}(u)$, connect $S^*$ and $T^*$, and add the MCMF cost from $S^*$ to $T^*$ to the sum of all branch times $\sum_e t_e$.

---

#### Problem 2.5 — Degree-Constrained Planar Arborescence (`[Codeforces 277 E] Binary Tree on Plane`)
- **Judge & URL**: [Codeforces 277E — Binary Tree on Plane](https://codeforces.com/problemset/problem/277/E) (`[EN]`)
- **Inline Statement & Constraints**:
  Given $n \le 400$ points $(x_i, y_i)$ in the 2D plane, build a rooted binary tree whose vertices are the $n$ points such that every parent $u$ has a **strictly larger $y$-coordinate** than its children $v$ ($y_u > y_v$), each vertex has at most $2$ children, and the total Euclidean length of the $n-1$ edges is minimized (or output `-1` if impossible).

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal)**:
     Normally, minimum-weight directed spanning tree (arborescence) requires Edmonds' Chu–Liu algorithm because cycle constraints are global. Why does MCMF work here?! Because the condition $y_u > y_v$ forces the allowed edges to form a **strict DAG**! On a DAG, a subgraph has no directed cycles automatically, so a spanning binary tree is **purely characterized by local vertex degrees**:
     - Every vertex $v$ except the root has in-degree $= 1$ (and the root has in-degree $= 0$), totaling $n - 1$ edges.
     - Every vertex $u$ has out-degree $\le 2$.
  2. **Step 2 (Algebraic Intermediate)**:
     Let $x_{u,v} \in \{0, 1\}$ ($y_u > y_v$) indicate whether $u$ is the parent of $v$. Then:
     $$\sum_{v : y_u > y_v} x_{u,v} \le 2 \quad (\forall u), \qquad \sum_{u : y_u > y_v} x_{u,v} \le 1 \quad (\forall v), \qquad \sum_{u, v} x_{u,v} = n - 1.$$
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Bipartite degree network: split each point $i$ into a parent role $L_i$ and a child role $R_i$.
     - Add $(S \to L_u, \text{cap } 2, \text{cost } 0)$ (at most $2$ children) and $(R_v \to T, \text{cap } 1, \text{cost } 0)$ (at most $1$ parent).
     - For every pair $(u, v)$ with $y_u > y_v$, add $(L_u \to R_v, \text{cap } 1, \text{cost } \sqrt{(x_u - x_v)^2 + (y_u - y_v)^2})$.
     - Run MCMF from $S$ to $T$. If maximum flow $|f| < n - 1$ (e.g., two points tie for the maximum $y$-coordinate so neither can have a parent!), output `-1`; otherwise output the minimum cost!
  4. **Step 4 (Floating-Point Johnson Potential Contract)**:
     Because edge costs are `double` Euclidean distances, when running Dijkstra with Johnson potentials $\pi(v)$, floating-point rounding can produce $c_\pi(u, v) = -10^{-15}$. Always relax Dijkstra edges using an epsilon tolerance `if (dist[v] > dist[u] + w + 1e-9)` and clamp `w = max(0.0, c[e] + pi[u] - pi[v])`!

- **3-Tier Progressive Hints**:
  - *Hint 1*: Why can a set of $n-1$ edges with $y_u > y_v$, in-degree $\le 1$, and out-degree $\le 2$ never form a cycle?
  - *Hint 2*: Since $y_u > y_v$ eliminates cycles automatically, the problem reduces to a bipartite $b$-matching between parent slots (capacity $2$) and child slots (capacity $1$).
  - *Hint 3*: Check whether the maximum flow reaches $n - 1$; if so, the unique vertex whose $R_v \to T$ edge is unsaturated is the root of the binary tree!

---

#### Problem 2.6 — Sliding-Window Subsequence Packing (`[BZOJ 1283] 序列`)
- **Judge & URL**: BZOJ 1283 / Hydro BZOJ 1283 (`[ZH]` 序列)
- **Inline Statement & Constraints**:
  Given an array of $n \le 1000$ positive integers $c_1, c_2, \dots, c_n$ and two integers $m, K$ ($1 \le K \le m \le n$), select a subsequence of indices ($x_j \in \{0, 1\}$ for $j = 1 \dots n$) to maximize $\sum_{j=1}^n c_j x_j$ such that **every contiguous subarray (sliding window) of length $m$ contains at most $K$ selected elements**.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal)**:
     For $m \le 20$, bitmask DP works in $O(n 2^m)$. For $m \le 1000$, bitmask DP is impossible, and every sliding window $[t, t+m-1]$ imposes a linear inequality $\sum_{j=t}^{t+m-1} x_j \le K$. This is **Iteration 30C (Sliding-Window Equation-Difference)**!
  2. **Step 2 (Algebraic Intermediate)**:
     There are $W = n - m + 1$ window constraints $E_1, E_2, \dots, E_W$:
     $$E_t : \quad \sum_{j=t}^{t+m-1} x_j + y_t = K \qquad (t = 1, 2, \dots, W), \quad x_j \in [0, 1], \; y_t \ge 0.$$
     Which equations $E_t$ contain variable $x_j$?
     $$t \le j \le t + m - 1 \iff \max(1, j - m + 1) \le t \le \min(W, j).$$
     Let $L_j := \max(1, j - m + 1)$ and $R_j := \min(W, j)$. Then $x_j$ appears in the contiguous range of equations $E_{L_j}, \dots, E_{R_j}$!
     Taking $\Delta E_t = E_t - E_{t-1}$ ($t = 1, \dots, W+1$, with $E_0 = E_{W+1} = 0$):
     - $x_j \in [0, 1]$ has $+1$ in $\Delta E_{L_j}$ and $-1$ in $\Delta E_{R_j + 1}$!
     - $y_t \ge 0$ has $+1$ in $\Delta E_t$ and $-1$ in $\Delta E_{t+1}$!
     - RHS is $+K$ at $t = 1$ and $-K$ at $t = W+1$.
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Create vertices $1, 2, \dots, W+1$. Add $(S \to 1, \text{cap } K, \text{cost } 0)$ and $(W+1 \to T, \text{cap } K, \text{cost } 0)$.
     - For each $t = 1 \dots W$, add forward slack edge $(t \to t+1, \text{cap } \infty, \text{cost } 0)$.
     - For each array element $j = 1 \dots n$, add $(L_j \to R_j + 1, \text{cap } 1, \text{cost } -c_j)$.
     - Initialize $\pi_0$ via $O(n)$ DAG DP on $1 \dots W+1$ and run $K$ steps of Dijkstra!
  4. **Step 4 (Alternative Primal View)**:
     Notice you can also view each selected element $x_j = 1$ as blocking its own capacity for $m$ steps, i.e., jumping from $j \to \min(n+1, j + m)$ on a chain of $n+1$ vertices! Both graphs are isomorphic after contracting degree-2 vertices.

- **3-Tier Progressive Hints**:
  - *Hint 1*: Write the $W = n - m + 1$ window inequalities $E_t : \sum_{j=t}^{t+m-1} x_j + y_t = K$ and identify which range of windows $[L_j, R_j]$ contains a given index $j$.
  - *Hint 2*: Subtract $\Delta E_t = E_t - E_{t-1}$ for $t = 1 \dots W+1$: where do the $+1$ and $-1$ coefficients of $x_j$ land?
  - *Hint 3*: Add $(L_j \to R_j + 1, \text{cap } 1, \text{cost } -c_j)$ and $(t \to t+1, \text{cap } \infty, \text{cost } 0)$, and route $K$ units of flow from $1$ to $W+1$.

---

## 4-Tier Curated Problem Bank (Part 2: Advanced & Mastery — 11 Fully Solved Problems)

---

### Tier 3: Advanced (6 Problems)

---

#### Problem 3.1 — Interval Lower-Bound Coverage Flagship (`[NOI2008 / Luogu P3980] 志愿者招募`)
- **Judge & URL**: [Luogu P3980](https://www.luogu.com.cn/problem/P3980) / LOJ #102 / BZOJ 1061 (`[ZH]` NOI2008 志愿者招募)
- **Inline Statement & Constraints**:
  A project runs for $n \le 1000$ days; day $t$ requires at least $A_t \ge 0$ volunteers. There are $m \le 10000$ volunteer types; type $i$ works across days $[l_i, r_i]$ ($1 \le l_i \le r_i \le n$) at cost $c_i \ge 0$ per person, with unlimited headcount per type. Find the minimum total cost to satisfy all $n$ daily demands.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal)**:
     Intervals $[l_i, r_i]$ can overlap arbitrarily ($m \le 10^4, n \le 10^3$), and we have a pure linear inequality system $\sum_{i : t \in [l_i, r_i]} x_i \ge A_t$ with zero graph mentioned in the statement. Because each volunteer works on a **contiguous interval** $[l_i, r_i]$, the constraint matrix satisfies the Consecutive-Ones Property and compiles via **Iteration 30 (Archetype 30A: Equation-Difference Method)**.
  2. **Step 2 (Algebraic Intermediate)**:
     Introduce daily surplus slack $y_t \ge 0$ ($1 \le t \le n$) and pad with $E_0 : 0 = 0, E_{n+1} : 0 = 0$:
     $$E_t : \quad \sum_{i : l_i \le t \le r_i} x_i - y_t = A_t \implies \Delta E_t = E_t - E_{t-1} : \quad \sum_{i : l_i = t} x_i - \sum_{i : r_i + 1 = t} x_i + y_{t-1} - y_t = A_t - A_{t-1}.$$
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Create $n+1$ vertices $1, 2, \dots, n+1$, super-source $S^*$, super-sink $T^*$.
     - Set $A_0 = A_{n+1} = 0$. For $t = 1, \dots, n+1$, let $b_t = A_t - A_{t-1}$:
       - If $b_t > 0$, add $(S^* \to t, \text{cap } b_t, \text{cost } 0)$.
       - If $b_t < 0$, add $(t \to T^*, \text{cap } -b_t, \text{cost } 0)$.
     - For each day $t = 1, \dots, n$, add backward slack edge $(t+1 \to t, \text{cap } \infty, \text{cost } 0)$.
     - For each volunteer type $i = 1, \dots, m$, add forward jump edge $(l_i \to r_i + 1, \text{cap } \infty, \text{cost } c_i)$.
     - All costs are $\ge 0$, so set $\pi_0 = 0$ and run SSP + Dijkstra from $S^*$ to $T^*$!
  4. **Step 4 (Broken Gadget Counterexample)**:
     - **What if you use $n$ vertices instead of $n+1$?** Then any volunteer whose interval ends on the last day ($r_i = n$) has its $-1$ coefficient in $\Delta E_{n+1}$ discarded, turning $x_i$ into a half-edge with $+1$ at $l_i$ and no head vertex!
     - **What if you direct the slack edge forward $(t \to t+1)$ instead of backward $(t+1 \to t)$?** A forward edge $(t \to t+1)$ corresponds to $+y_t$ in $E_t$ ($\sum x_i + y_t = A_t \iff \sum x_i \le A_t$), which solves upper-bound packing instead of lower-bound coverage!

- **3-Tier Progressive Hints**:
  - *Hint 1*: Write the $n$ daily inequalities $\sum_{i \ni t} x_i \ge A_t$ as exact equations by subtracting a non-negative surplus variable $y_t \ge 0$.
  - *Hint 2*: Pad with $E_0 : 0 = 0$ and $E_{n+1} : 0 = 0$, and compute $\Delta E_t = E_t - E_{t-1}$ for $t = 1, \dots, n+1$.
  - *Hint 3*: Interpret $+1$ in $\Delta E_u$ and $-1$ in $\Delta E_v$ as a directed edge $u \to v$: $x_i$ becomes $(l_i \to r_i + 1, \infty, c_i)$ and $y_t$ becomes $(t+1 \to t, \infty, 0)$.

---

#### Problem 3.2 — Prime-Parity Bipartite Matching with Budget-Threshold Stopping (`[SDOI2016 / Luogu P3705] 数字配对`)
- **Judge & URL**: [Luogu P3705](https://www.luogu.com.cn/problem/P3705) (`[ZH]` SDOI2016 数字配对)
- **Inline Statement & Constraints**:
  There are $n \le 200$ types of numbers; type $i$ has value $a_i \in [1, 10^9]$, count $b_i \in [1, 10^5]$, and weight $c_i \in [-10^5, 10^5]$. Two numbers of types $i$ and $j$ can be paired iff $a_i / a_j$ or $a_j / a_i$ is a **prime number**, yielding a pair value of $c_i \cdot c_j$ (note: $c_i c_j$ can be positive or negative!). Maximize the **total number of pairs** formed subject to the constraint that the **sum of values of all chosen pairs is $\ge 0$**.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal)**:
     - First, why is the divisibility graph bipartite? Let $\Omega(x)$ be the total number of prime factors of $x$ counted with multiplicity. Then $a_i / a_j = p$ (prime) implies $\Omega(a_i) = \Omega(a_j) + 1$, which changes the parity of $\Omega(a_i) \bmod 2$! Thus the graph is **bipartite**, partitioned by $\Omega(a_i) \bmod 2 \in \{0, 1\}$!
     - Second, we want to **maximize flow volume $f$** subject to $\text{TotalProfit}(f) \ge 0 \iff C(f) \le 0$ (where edge cost is $-c_i c_j$). This is the exact **Budget-Threshold Prefix of Convex $C(f)$** from **Section 27.2(4)**!
  2. **Step 2 (Algebraic Intermediate)**:
     Let $L = \{i : \Omega(a_i) \equiv 1 \pmod 2\}$ and $R = \{j : \Omega(a_j) \equiv 0 \pmod 2\}$. Negate pair values to costs $w_{ij} = -c_i c_j$. By Theorem 27.1, the SSP path costs $d_1 \le d_2 \le \dots \le d_K$ are monotonically non-decreasing, so $C(f)$ is convex. To maximize $f$ subject to $C(f) \le 0$, we greedily augment along shortest paths in SSP order!
  3. **Step 3 (Mechanical Graph Compilation & Threshold Stopping)**:
     - Add $(S \to i, \text{cap } b_i, \text{cost } 0)$ for $i \in L$, and $(j \to T, \text{cap } b_j, \text{cost } 0)$ for $j \in R$.
     - For $i \in L, j \in R$ where $a_i / a_j$ or $a_j / a_i$ is prime, add $(i \to j, \text{cap } \infty, \text{cost } -c_i c_j)$.
     - Since $S \to L \to R \to T$ is a 3-layer DAG, initialize $\pi_0$ via $O(n^2)$ DAG DP.
     - Run SSP + Dijkstra: let $C_{\text{cur}} \le 0$ be the current cumulative cost, and let the current shortest path $P_k$ have bottleneck $\delta_k$ and unit cost $d_k$:
       - If $C_{\text{cur}} + \delta_k \cdot d_k \le 0$: push all $\delta_k$ units ($f \mathrel{+}= \delta_k$, $C_{\text{cur}} \mathrel{+}= \delta_k d_k$).
       - If $C_{\text{cur}} + \delta_k \cdot d_k > 0$ (which implies $d_k > 0$): we can only afford $\Delta f = \lfloor -C_{\text{cur}} / d_k \rfloor$ units! Add $\Delta f$ to $f$ and **break immediately**!
  4. **Step 4 (Failure Mode — Using 64-bit Integers for $c_i c_j$ and $\delta_k d_k$)**:
     Since $|c_i| \le 10^5$, $|d_k| \le 10^{10}$ and $\delta_k \le 10^5$, so $\delta_k d_k$ reaches $10^{15}$ (`long long`). Furthermore, never stop at $d_k > 0$ while $C_{\text{cur}} < 0$: the negative cost accumulated from earlier profitable pairs is meant to subsidize later unprofitable pairs!

- **3-Tier Progressive Hints**:
  - *Hint 1*: Count the total prime factors $\Omega(a_i)$ with multiplicity: why can two numbers $a_i, a_j$ with $\Omega(a_i) \equiv \Omega(a_j) \pmod 2$ never have a prime ratio?
  - *Hint 2*: Negate pair profits to costs $-c_i c_j$ on the bipartite graph $(\Omega \text{ odd}) \to (\Omega \text{ even})$. Why does SSP visit paths in non-decreasing order of cost $d_1 \le d_2 \le \dots$?
  - *Hint 3*: Keep augmenting even when $d_k > 0$ as long as the cumulative cost $C_{\text{cur}}$ stays $\le 0$; on the first path where $C_{\text{cur}} + \delta_k d_k > 0$, take $\lfloor -C_{\text{cur}} / d_k \rfloor$ units and stop.

---

#### Problem 3.3 — String Occurrence Packing with Character Capacities (`[Codeforces 717 G] Underfail`)
- **Judge & URL**: [Codeforces 717G — Underfail](https://codeforces.com/problemset/problem/717/G) (`[EN]`)
- **Inline Statement & Constraints**:
  Given a string $S$ of length $n \le 500$, a dictionary of $m \le 100$ words $(p_j, w_j)$ (each with positive score $w_j$), and an integer $x \le 100$, you may highlight occurrences of dictionary words in $S$ (each specific occurrence $[i, i + |p_j| - 1]$ can be highlighted at most once) such that **each character $S[t]$ ($1 \le t \le n$) belongs to at most $x$ highlighted occurrences**. Maximize the total score.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal)**:
     Find all valid occurrences of every pattern $p_j$ in $S$. An occurrence of $p_j$ starting at index $i$ covers the contiguous range of character positions $[i, i + |p_j| - 1]$ and yields score $w_j$, and each character position $t \in \{1, \dots, n\}$ can be covered at most $x$ times. This reduces 100% to **Iteration 30B (Interval Upper-Bound Packing)**!
  2. **Step 2 (Algebraic Intermediate)**:
     Let $\mathcal{O}$ be the set of all occurrences $o = (l_o, r_o, w_o)$ where $S[l_o \dots r_o] = p_j$. For each character $t \in \{1, \dots, n\}$,
     $$\sum_{o \in \mathcal{O} : l_o \le t \le r_o} z_o + y_t = x, \qquad z_o \in [0, 1], \; y_t \ge 0.$$
     Differencing $\Delta E_t = E_t - E_{t-1}$ ($t = 1 \dots n+1$) compiles each occurrence $o$ into $(l_o \to r_o + 1, \text{cap } 1, \text{cost } -w_o)$ and each slack $y_t$ into $(t \to t+1, \text{cap } \infty, \text{cost } 0)$.
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Create vertices $1, 2, \dots, n+1$, with $(S_0 \to 1, \text{cap } x, \text{cost } 0)$ and $(n+1 \to T_0, \text{cap } x, \text{cost } 0)$.
     - Add chain edges $(t \to t+1, \text{cap } \infty, \text{cost } 0)$ for $t = 1 \dots n$.
     - For each occurrence $S[i \dots i + |p_j| - 1] = p_j$, add jump edge $(i \to i + |p_j|, \text{cap } 1, \text{cost } -w_j)$.
     - Compute $\pi_0$ via $O(n + |\mathcal{O}|)$ DAG DP on $1 \dots n+1$ and run $x$ steps of Dijkstra!
  4. **Step 4 (Failure Mode — Distinct Words matching the Same Substring)**:
     Two different dictionary entries $j_1 \ne j_2$ may have the **exact same string** $p_{j_1} = p_{j_2}$, and both can be highlighted at the same starting position $i$! Therefore, add a separate unit-capacity jump edge $(i \to i + |p_j|, \text{cap } 1, \text{cost } -w_j)$ for each matching dictionary entry $j$, rather than overwriting parallel edges.

- **3-Tier Progressive Hints**:
  - *Hint 1*: Every occurrence of word $p_j$ at index $i$ in $S$ is simply an interval $[i, i + |p_j| - 1]$ of weight $w_j$.
  - *Hint 2*: Apply Iteration 30B to enforce that each position $t \in [1, n]$ is covered by at most $x$ intervals.
  - *Hint 3*: Route $x$ units of flow from $1$ to $n+1$ with chain edges $(t \to t+1, \infty, 0)$ and occurrence edges $(i \to i + |p_j|, 1, -w_j)$.

---

#### Problem 3.4 — Bipartite Majority Edge Coloring (`[Codeforces 1288 F] Red-Blue Graph`)
- **Judge & URL**: [Codeforces 1288F — Red-Blue Graph](https://codeforces.com/problemset/problem/1288/F) (`[EN]`)
- **Inline Statement & Constraints**:
  Given a bipartite graph with $n_1, n_2 \le 200$ vertices and $m \le 200$ edges, each vertex is colored Red (`R`), Blue (`B`), or Uncolored (`U`). You must color each edge Red (cost $r$), Blue (cost $b$), or leave it Uncolored (cost $0$) such that:
  - For every Red vertex, strictly more incident edges are Red than Blue ($d_R(v) - d_B(v) \ge 1$).
  - For every Blue vertex, strictly more incident edges are Blue than Red ($d_B(v) - d_R(v) \ge 1$).
  Find the minimum cost coloring, or output `-1` if impossible.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal)**:
     Look at the quantity $d_R(v) - d_B(v)$: one choice (Red) contributes $+1$, the opposite choice (Blue) contributes $-1$, and Uncolored contributes $0$! In a bipartite graph $L \cup R$, if we interpret a Red edge on $(u, v) \in L \times R$ as **sending $1$ unit of flow from $u \to v$** and a Blue edge as **sending $1$ unit of flow in the opposite direction $v \to u$**, then for any $u \in L$:
     $$\text{NetOutFlow}(u) = \text{OutFlow}(u) - \text{InFlow}(u) = d_R(u) - d_B(u)!$$
     And for any $v \in R$:
     $$\text{NetInFlow}(v) = \text{InFlow}(v) - \text{OutFlow}(v) = d_R(v) - d_B(v)!$$
     This turns the entire problem into **Iteration 28, Engine 28B (`有源汇上下界最小费用可行流`)**!
  2. **Step 2 (Algebraic Intermediate)**:
     For each graph edge $e = (u, v) \in L \times R$, introduce two flow variables: $f_R(e) \in [0, 1]$ on $(u \to v)$ at cost $r$, and $f_B(e) \in [0, 1]$ on $(v \to u)$ at cost $b$. (Since $r, b > 0$, the solver will never set both $f_R(e) = 1$ and $f_B(e) = 1$ because $(u \to v \to u)$ is a positive-cost 2-cycle of cost $r + b > 0$!).
     The degree constraints become lower/upper bounds on the net flow between $S$, $L$, $R$, and $T$:
     - For $u \in L$:
       - If $u$ is `R`: $d_R(u) - d_B(u) \in [1, \infty) \implies$ edge $(S \to u, \text{cap } [1, \infty), \text{cost } 0)$.
       - If $u$ is `B`: $d_B(u) - d_R(u) \in [1, \infty) \implies$ edge $(u \to T, \text{cap } [1, \infty), \text{cost } 0)$.
       - If $u$ is `U`: no constraint $\implies$ add $(S \to u, [0, \infty), 0)$ and $(u \to T, [0, \infty), 0)$.
     - For $v \in R$ (where Red enters $v$ and Blue leaves $v$, so the roles of $S$ and $T$ flip!):
       - If $v$ is `R`: $d_R(v) - d_B(v) = \text{In}(v) - \text{Out}(v) \in [1, \infty) \implies$ edge $(v \to T, \text{cap } [1, \infty), \text{cost } 0)$.
       - If $v$ is `B`: $d_B(v) - d_R(v) = \text{Out}(v) - \text{In}(v) \in [1, \infty) \implies$ edge $(S \to v, \text{cap } [1, \infty), \text{cost } 0)$.
       - If $v$ is `U`: add $(S \to v, [0, \infty), 0)$ and $(v \to T, [0, \infty), 0)$.
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Add all vertex-to-$S/T$ edges with their $[l, u]$ bounds and cost $0$.
     - For each edge $e = (u, v) \in L \times R$, add $(u \to v, [0, 1], \text{cost } r)$ and $(v \to u, [0, 1], \text{cost } b)$.
     - Add circulation feedback edge $(T \to S, [0, \infty), \text{cost } 0)$.
     - Build $(S^*, T^*)$ for all edges with $l_e = 1$ and run **Engine 28B (Phase 1 only)** from $S^*$ to $T^*$!
     - If $F^* < D_{\text{total}}$, output `-1`. Otherwise, edge $e$ is `R` if $f_R(e)=1$ (and $f_B(e)=0$), `B` if $f_B(e)=1$ (and $f_R(e)=0$), and `U` if $f_R(e) = f_B(e)$!
  4. **Step 4 (Failure Mode)**:
     Remember that for right-side vertices $v \in R$, a Red edge $(u \to v)$ **enters** $v$ whereas for left-side vertices $u \in L$ it **leaves** $u$! Forgetting to swap $S$ and $T$ for `R`/`B` vertices on the right side $R$ reverses their color majority requirements.

- **3-Tier Progressive Hints**:
  - *Hint 1*: For an edge $(u, v) \in L \times R$, model coloring it Red as 1 unit of flow $u \to v$ (cost $r$) and coloring it Blue as 1 unit of flow $v \to u$ (cost $b$).
  - *Hint 2*: Under this convention, what does $\text{OutFlow}(u) - \text{InFlow}(u)$ represent for $u \in L$, and what does $\text{InFlow}(v) - \text{OutFlow}(v)$ represent for $v \in R$?
  - *Hint 3*: Express $d_R - d_B \ge 1$ and $d_B - d_R \ge 1$ as lower-bound edges $[1, \infty)$ from $S$ or to $T$, and solve via `有源汇上下界最小费用可行流` (Engine 28B).

---

#### Problem 3.5 — Two-Sided Bounded Sliding-Window Coverage (`[ICPC NEERC 2016 D / Luogu P6967] Delight for a Cat`)
- **Judge & URL**: [Luogu P6967](https://www.luogu.com.cn/problem/P6967) / [Codeforces Gym 101190 D](https://codeforces.com/gym/101190) (`[EN]` NEERC 2016 — Delight for a Cat)
- **Inline Statement & Constraints**:
  A cat's schedule has $n \le 1000$ hours. During hour $j \in \{1, \dots, n\}$, sleeping gives $s_j$ happiness and eating gives $e_j$ happiness. In **every contiguous window of $k$ hours** ($[t, t+k-1]$ for $t = 1, \dots, n-k+1$), the cat must sleep for at least $m_s$ hours and eat for at least $m_e$ hours. Maximize total happiness and output the `S`/`E` string.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal)**:
     Let $x_j \in \{0, 1\}$ indicate whether the cat **sleeps** during hour $j$ (so eating is $1 - x_j$). Then in every sliding window $[t, t+k-1]$ of length $k$, sleeping at least $m_s$ hours and eating at least $m_e$ hours means the number of sleeping hours lies in the **two-sided closed interval** $[L, R] := [m_s, \; k - m_e]$! This is **Archetype 30C (Two-Sided Bounded Sliding-Window Equation-Difference)**!
  2. **Step 2 (Algebraic Intermediate)**:
     Baseline happiness (all eating, $x_j = 0$) is $\text{Base} = \sum_{j=1}^n e_j$, and sleeping in hour $j$ adds net gain $w_j = s_j - e_j$ (cost $-w_j$).
     For each window $t \in \{1, \dots, W\}$ (where $W = n - k + 1$), the inequality $L \le \sum_{j=t}^{t+k-1} x_j \le R$ becomes an exact equation with a **bounded slack variable** $y_t \in [0, R - L]$:
     $$E_t : \quad \sum_{j=t}^{t+k-1} x_j + y_t = R, \qquad x_j \in [0, 1], \quad 0 \le y_t \le R - L.$$
     Why did we write $+y_t = R$ instead of $-y_t = L$? Because $R = k - m_e$ is **constant** across all $t = 1 \dots W$! Thus when we take $\Delta E_t = E_t - E_{t-1}$ ($t = 1 \dots W+1$, with $E_0 = E_{W+1} = 0$):
     - The right-hand side is $b_1 = +R$, $b_{W+1} = -R$, and $b_2 = \dots = b_W = 0$!
     - Each hour variable $x_j \in [0, 1]$ appears in windows $t \in [\max(1, j-k+1), \; \min(W, j)]$, so in $\Delta E_t$ it has $+1$ at $u_j = \max(1, j-k+1)$ and $-1$ at $v_j = \min(W, j) + 1$!
     - Each slack variable $y_t \in [0, R - L]$ has $+1$ in $\Delta E_t$ and $-1$ in $\Delta E_{t+1}$!
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Create vertices $1, 2, \dots, W+1$, with source $S = 1$ (injecting $R$ units of flow) and sink $T = W+1$ (absorbing $R$ units of flow).
     - For each $t = 1, \dots, W$, add forward slack edge $(t \to t+1, \text{cap } R - L, \text{cost } 0)$.
     - For each hour $j = 1, \dots, n$, add jump edge $\big(\max(1, j-k+1) \to \min(W, j) + 1, \; \text{cap } 1, \; \text{cost } -(s_j - e_j)\big)$.
     - Wait: can $-w_j = -(s_j - e_j)$ be negative while $(t \to t+1)$ has finite capacity $R - L$? Notice the graph is STILL a **strict DAG** ($u_j < v_j$ and $t < t+1$)! However, because $(t \to t+1)$ has finite capacity $R - L < R$, **not every vertex is guaranteed to have capacity $R$ along the chain alone**, or you can use **Mandatory Initial Saturation (Iteration 28.2)** on $w_j > 0$ edges (or DAG DP for $\pi_0$) and run $R$ steps of Dijkstra!
  4. **Step 4 (Why $+y_t = R$ Beats $-y_t = L$ Here)**:
     Had we written $\sum x_j - y_t = L$, the slack edges $(t+1 \to t)$ would point backward, destroying the DAG property! Writing $\sum x_j + y_t = R$ with $0 \le y_t \le R - L$ keeps all slack edges pointing **forward** $(t \to t+1)$, preserving the topological DAG $1 \to 2 \to \dots \to W+1$!

- **3-Tier Progressive Hints**:
  - *Hint 1*: Express the window constraints in terms of $x_j \in \{0, 1\}$ (1 if sleeping at hour $j$): $m_s \le \sum_{j=t}^{t+k-1} x_j \le k - m_e$.
  - *Hint 2*: Set $L = m_s$ and $R = k - m_e$, and write $E_t : \sum_{j=t}^{t+k-1} x_j + y_t = R$ where the slack variable $y_t$ is bounded by $0 \le y_t \le R - L$.
  - *Hint 3*: Take $\Delta E_t = E_t - E_{t-1}$: notice that all edges go strictly forward on $1 \dots W+1$, and route $R$ units of flow from $1$ to $W+1$.

---

#### Problem 3.6 — 3-Group Partition MCMF vs. Priority-Queue Simulation (`[AtCoder AGC 018 C] Coins`)
- **Judge & URL**: [AtCoder AGC 018 C — Coins](https://atcoder.jp/contests/agc018/tasks/agc018_c) (`[JA]`)
- **Inline Statement & Constraints**:
  There are $N = X + Y + Z \le 10^5$ people. Person $i$ holds $A_i$ gold, $B_i$ silver, and $C_i$ bronze coins. Partition the $N$ people into three disjoint groups of exact sizes $X, Y, Z$ so that the $X$ people give their gold coins, the $Y$ people give their silver coins, and the $Z$ people give their bronze coins, maximizing the total number of coins collected.

- **4-Step "Zero Magic Gadgets" Compilation (Direction A $\to$ Direction B Bridge)**:
  1. **Step 1 (Diagnostic Signal)**:
     Assigning $N$ people to 3 buckets of capacities $(X, Y, Z)$ is a textbook **Minimum-Cost Bipartite $b$-Matching (Transportation)** problem with $N$ left nodes and $3$ right nodes! Because $N \le 10^5$, running black-box MCMF directly is too slow, making this our first **Direction B Bridge**: build the MCMF model, then simplify it via variable subtraction and simulate its residual network with priority queues in $O(N \log N)$!
  2. **Step 2 (Algebraic Intermediate — Eliminating the 3rd Choice)**:
     Pre-assign every person $i$ to Bronze (`Z`), giving base sum $\text{Base} = \sum_{i=1}^N C_i$, and replace each person's values by the relative gains $(a_i, b_i, 0) := (A_i - C_i, \; B_i - C_i, \; 0)$.
     Now we only need to pick $X$ people for Gold (gain $a_i$) and $Y$ people for Silver (gain $b_i$). Even better: sort all $N$ people by $a_i - b_i = A_i - B_i$ in descending order!
  3. **Step 3 (From Residual Graph to Split-Point Priority Queue)**:
     - **Why sorting by $a_i - b_i$ eliminates crossing residual cycles**: Suppose person $i$ is assigned to Gold and person $j$ is assigned to Silver. In the MCMF residual graph, swapping their roles ($i \to \text{Silver}, j \to \text{Gold}$) changes total profit by $(b_i + a_j) - (a_i + b_j) = (a_j - b_j) - (a_i - b_i)$. By Negative-Cycle Optimality (Theorem 26.3), in an optimal flow we can never have $a_j - b_j > a_i - b_i$!
     - Therefore, in sorted order of $a_i - b_i$ (descending), **there exists a split index $k \in [X, N - Y]$ such that all $X$ Gold people lie in prefix $1 \dots k$ and all $Y$ Silver people lie in suffix $k+1 \dots N$!**
     - For each split $k$, the best $X$ people in $1 \dots k$ (maximizing $\sum a_i$) and the best $Y$ people in $k+1 \dots N$ (maximizing $\sum b_i$) are maintained in $O(N \log N)$ using two min-heaps!
  4. **Step 4 (Alternative Simulated MCMF View — Wave 5A Preview)**:
     You can also simulate augmenting paths directly on the 3-hub residual graph $\{G, S, B\}$ using 6 priority queues of residual edges $(u \to v)$, which runs in $O(N \log N)$ without even needing the $a_i - b_i$ sorting property (and generalizes to $K=4$ groups!).

- **3-Tier Progressive Hints**:
  - *Hint 1*: Subtract $C_i$ from each person so Bronze gives $0$, Gold gives $a_i = A_i - C_i$, and Silver gives $b_i = B_i - C_i$.
  - *Hint 2*: Use the Negative-Cycle Optimality condition on a 2-person swap between Gold and Silver: if $i \in \text{Gold}$ and $j \in \text{Silver}$, what inequality must hold between $a_i - b_i$ and $a_j - b_j$?
  - *Hint 3*: Sort by $a_i - b_i$ descending so all Gold choices precede all Silver choices, then sweep the partition point $k \in [X, N-Y]$ using a prefix heap of size $X$ and a suffix heap of size $Y$.

---

### Tier 4: Mastery (5 Problems)

---

#### Problem 4.1 — Equation-Difference + LP Dual Transposition (`[ZJOI2013 / Luogu P3337] 防守战线`)
- **Judge & URL**: [Luogu P3337](https://www.luogu.com.cn/problem/P3337) (`[ZH]` ZJOI2013 防守战线)
- **Inline Statement & Constraints**:
  Along a defense line of $n \le 1000$ positions, placing a tower at position $j \in \{1, \dots, n\}$ (at most $1$ tower per position: $x_j \in [0, 1]$) costs $c_j \ge 0$. There are $m \le 10000$ intelligence requirements: requirement $i$ demands that the interval $[l_i, r_i]$ contain at least $d_i$ towers. Find the minimum total cost to satisfy all $m$ requirements.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal — The Asymmetric Dimension Trap $n = 1000 \ll m = 10000$)**:
     Look closely at the roles of $n$ and $m$ compared to `[NOI2008] 志愿者招募` (Problem 3.1):
     - In `志愿者招募`, we had $n = 1000$ point constraints and $m = 10000$ interval variables $\implies$ Equation-Difference gave $n+1 = 1001$ vertices and $m = 10000$ edges!
     - Here in `防守战线`, we have **$n = 1000$ point variables $x_j \in [0, 1]$** and **$m = 10000$ interval constraints** $\sum_{j=l_i}^{r_i} x_j \ge d_i$!
     If you apply Equation-Difference directly to the $m = 10000$ interval constraints, they are NOT sliding windows of equal length—a point $j$ is covered by an arbitrary subset of intervals, NOT a contiguous range of interval indices! And how do we get $n+1 = 1001$ vertices and $m = 10000$ edges instead? **By taking the Linear Programming Dual (or Prefix-Sum Difference Substitution)!**
  2. **Step 2 (Algebraic Intermediate — Dualizing Point Variables vs. Interval Constraints)**:
     Let us take the **LP Dual** of the primal LP:
     $$\text{Primal: } \min \sum_{j=1}^n c_j x_j \quad \text{s.t.} \quad \sum_{j=l_i}^{r_i} x_j \ge d_i \; (\text{dual } u_i \ge 0), \quad -x_j \ge -1 \; (\text{dual } v_j \ge 0), \quad x_j \ge 0.$$
     By LP Duality (previewing Wave 4B), the dual problem has **interval variables $u_i \ge 0$ ($i = 1 \dots m$)** and **point constraints ($j = 1 \dots n$)**:
     $$\text{Dual: } \max \sum_{i=1}^m d_i u_i - \sum_{j=1}^n v_j \quad \text{s.t.} \quad \sum_{i \,:\, l_i \le j \le r_i} u_i - v_j \le c_j \quad (j = 1, \dots, n), \quad u_i, v_j \ge 0!$$
     Look at that Dual LP: for each position $j \in \{1, \dots, n\}$, the interval variables $u_i$ covering position $j$ satisfy a **point inequality** $\sum_{i : j \in [l_i, r_i]} u_i - v_j + y_j = c_j$ ($y_j \ge 0$)!
     Now every interval variable $u_i$ covers the **contiguous range of positions $[l_i, r_i] \subseteq \{1, \dots, n\}$**!
  3. **Step 3 (Mechanical Graph Compilation via Equation-Difference on the Dual LP!)**:
     Apply **Iteration 30** ($\Delta E_j = E_j - E_{j-1}$ for $j = 1, \dots, n+1$, with $c_0 = c_{n+1} = 0$) to the Dual equations $E_j : \sum_{i \ni j} u_i - v_j + y_j = c_j$:
     - Create **$n+1 \le 1001$ vertices** $1, 2, \dots, n+1$, source $S^*$, sink $T^*$.
     - RHS $b_j = c_j - c_{j-1}$: connect $S^* \to j$ if $b_j > 0$, and $j \to T^*$ if $b_j < 0$.
     - For each Dual interval variable $u_i \ge 0$ (which has $+1$ in $\Delta E_{l_i}$, $-1$ in $\Delta E_{r_i + 1}$, and reward $+d_i$, i.e., cost $-d_i$): add edge $(l_i \to r_i + 1, \text{cap } \infty, \text{cost } -d_i)$!
     - For each Dual slack $+y_j \ge 0$ ($+1$ in $\Delta E_j$, $-1$ in $\Delta E_{j+1}$, cost $0$): add forward edge $(j \to j+1, \text{cap } \infty, \text{cost } 0)$!
     - For each Dual cap variable $-v_j \le 0$ ($-1$ in $\Delta E_j$, $+1$ in $\Delta E_{j+1}$, reward $-1$, i.e., cost $+1$): add backward edge $(j+1 \to j, \text{cap } \infty, \text{cost } +1)$!
  4. **Step 4 (Complexity & Structural Insight)**:
     By dualizing first and then applying Equation-Difference, the network has only $n+1 \le 1001$ vertices instead of $m = 10000$ constraints!

- **3-Tier Progressive Hints**:
  - *Hint 1*: Why can you not apply Equation-Difference directly to the $m = 10000$ interval constraints $\sum_{j=l_i}^{r_i} x_j \ge d_i$? Because the intervals are arbitrary, not sliding windows of fixed length!
  - *Hint 2*: Take the Linear Programming Dual (assigning dual variable $u_i \ge 0$ to interval $[l_i, r_i]$ and $v_j \ge 0$ to $x_j \le 1$): now the constraints are indexed by positions $j = 1 \dots n$!
  - *Hint 3*: Apply Iteration 30 ($\Delta E_j = E_j - E_{j-1}$) to the $n$ dual equations $E_j : \sum_{i \ni j} u_i - v_j + y_j = c_j$ on $n+1$ vertices.

---

#### Problem 4.2 — Convexity + WQS Binary Search + Regret Heap (`[Codeforces 802 O] April Fools' Problem (hard)`)
- **Judge & URL**: [Codeforces 802O — April Fools' Problem (hard)](https://codeforces.com/problemset/problem/802/O) (`[EN]`)
- **Inline Statement & Constraints**:
  Over $n \le 5 \times 10^5$ days, preparing a problem on day $i$ costs $a_i \ge 1$ (at most 1 prepared per day), and printing a problem on day $j$ costs $b_j \ge 1$ (at most 1 printed per day). A problem prepared on day $i$ can be printed on any day $j \ge i$. Prepare and print **exactly $k$ problems** ($1 \le k \le n$) at minimum total cost.

- **4-Step "Zero Magic Gadgets" Compilation (Direction B Flagship)**:
  1. **Step 1 (Diagnostic Signal)**:
     First, recognize the hidden MCMF graph: vertices $1, 2, \dots, n$, where day $t$ receives $(S \to t, \text{cap } 1, \text{cost } a_t)$, passes unprinted problems forward via $(t \to t+1, \text{cap } \infty, \text{cost } 0)$, and prints via $(t \to T, \text{cap } 1, \text{cost } b_t)$. We want the minimum cost of **exactly $k$ units of flow** $C(k)$!
     With $n = 5 \times 10^5$, running $k$ steps of Dijkstra takes $O(k n \log n) = O(n^2 \log n)$ (TLE).
     How do we drop $O(n^2 \log n)$ to $O(n \log n \log C)$? **By Theorem 27.1 ($C(k)$ is convex in flow volume $k$) + Section 27.3 (WQS Binary Search on $k$)**!
  2. **Step 2 (Algebraic Intermediate — WQS Penalty $\lambda$)**:
     By Theorem 27.2, subtract a reward $\lambda$ per printed problem (i.e., change each printing edge cost from $b_t$ to $b_t - \lambda$) and solve the **Unconstrained Variable-Volume Min-Cost Feasible Flow** problem:
     $$g(\lambda) = \min_{f \in [0, n]} \big(C(f) - \lambda f\big).$$
  3. **Step 3 (Solving Unconstrained Min-Cost Feasible Flow in $O(n \log n)$ via Regret Priority Queue)**:
     With flow volume unconstrained, we simply want to take all negative-cost paths $i \to j$ ($i \le j$) with cost $a_i + (b_j - \lambda) \le 0$!
     Sweep $j = 1, 2, \dots, n$ from left to right, maintaining a min-heap of available options at $i \le j$:
     - Insert candidate preparation `(a[j], UNMATCHED)` into the min-heap.
     - Let `(best_v, type)` be the minimum element in the heap. If `best_v + (b[j] - lambda) <= 0`:
       - Match it with $b_j - \lambda$: add `best_v + b[j] - lambda` to $g(\lambda)$, pop `best_v`, and if `type == UNMATCHED`, increment total matched count $f(\lambda) \mathrel{+}= 1$.
       - **Residual Regret Arc**: If a later printing day $j' > j$ wants to steal the preparation matched to $j$ (canceling $b_j - \lambda$), the marginal cost of doing so is $-(b_j - \lambda)$! So push `(-(b[j] - lambda), MATCHED_B)` into the heap! (Notice that if a `MATCHED_B` element is popped, it replaces $b_j$ with $b_{j'}$ without changing the total flow volume $f(\lambda)$!)
     - Binary search $\lambda \in [0, 2 \times 10^9]$ until $f_{\max}(\lambda^*) \ge k$, and output $C(k) = g(\lambda^*) + \lambda^* \cdot k$!
  4. **Step 4 (Collinear Tie-Breaking Contract)**:
     When `best_v + b[j] - lambda == 0`, prioritize popping `UNMATCHED` elements over `MATCHED_B` elements so that the inner loop computes $f_{\max}(\lambda)$ (maximizing flow count among tied minimum-cost flows), and recover $g(\lambda^*) + \lambda^* k$.

- **3-Tier Progressive Hints**:
  - *Hint 1*: Model the problem as an $n$-vertex line MCMF network: why does Iteration 27 guarantee that the minimum cost $C(k)$ is a convex function of $k$?
  - *Hint 2*: Apply WQS binary search on $k$: subtract $\lambda$ from every $b_j$ so the inner problem asks for the minimum-cost flow of **any** volume.
  - *Hint 3*: Solve the unconstrained 1D min-cost flow in $O(n \log n)$ by sweeping $j = 1 \dots n$ with a regret min-heap that stores both unused $a_i$ (which increase flow count by $+1$) and matched $-(b_j - \lambda)$ (which swap a print day without changing flow count).

---

#### Problem 4.3 — 2D Convexity of Two-Commodity MCMF (`[Codeforces 739 E] Gosha is Hunting`)
- **Judge & URL**: [Codeforces 739E — Gosha is hunting](https://codeforces.com/problemset/problem/739/E) (`[EN]`)
- **Inline Statement & Constraints**:
  There are $n \le 2000$ Pokémon, $a$ Pokéballs, and $b$ Ultraballs. For Pokémon $i$, a Pokéball catches it with probability $p_i \in [0, 1]$, an Ultraball catches it with probability $u_i \in [0, 1]$, and throwing both (at most 1 of each per Pokémon) catches it with probability $1 - (1 - p_i)(1 - u_i) = p_i + u_i - p_i u_i$. Maximize the expected number of Pokémon caught.

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal)**:
     Why is this problem in an MCMF chapter?! Look at the reward of throwing $0$, $1$ ($p_i$ or $u_i$), or $2$ ($p_i + u_i - p_i u_i$) balls at Pokémon $i$:
     Because $p_i u_i \ge 0$, the marginal gain of adding the second ball after the first is $(p_i + u_i - p_i u_i) - p_i = u_i - p_i u_i \le u_i$!
     Therefore, **every Pokémon $i$ can be modeled as a convex marginal vertexgadget in an MCMF network** where Source $S$ supplies $a$ units to Hub $A$ (Pokéballs) and $b$ units to Hub $B$ (Ultraballs), and each Pokémon $i$ drains to Sink $T$ via two parallel unit-capacity edges (first edge cost $0$, second edge cost $+p_i u_i \ge 0$ to subtract the overlap $p_i u_i$ when both balls hit $i$)!
  2. **Step 2 (Algebraic Intermediate — 2D Joint Convexity of $C(a, b)$)**:
     Because the entire problem is a valid linear MCMF network with supplies $(a, b)$, **Iteration 27** proves that the optimal expected value $F(a, b)$ is **jointly concave** in $(a, b)$!
     - Removing $b$ via 1D WQS binary search on penalty $\lambda_B \in [0, 1]$ drops the state space from $O(n a b) = O(n^3)$ to $O(n^2 \log(1/\epsilon))$.
     - Removing **both** $a$ and $b$ via **Nested 2D WQS Binary Search** on $(\lambda_A, \lambda_B) \in [0, 1]^2$ drops the inner check to $O(n)$ greedy: for each Pokémon $i$, independently pick the best of the 4 options:
       $$\max\Big(0, \quad p_i - \lambda_A, \quad u_i - \lambda_B, \quad p_i + u_i - p_i u_i - \lambda_A - \lambda_B\Big)!$$
  3. **Step 3 (Algorithmic Execution)**:
     - Outer binary search (50 iterations) on $\lambda_A \in [0, 1]$; inner binary search (50 iterations) on $\lambda_B \in [0, 1]$.
     - Inside the $O(n)$ check, each Pokémon $i$ chooses the maximum of the 4 expressions above, recording the total number of $A$-balls used $cnt_A$ and $B$-balls used $cnt_B$.
     - Total runtime: $50 \times 50 \times 2000 = 5 \times 10^6$ operations ($\approx 15\text{ ms}$, vs. TLE for $O(n^3)$ DP or MCMF)!
  4. **Step 4 (Why the MCMF Proof of Concavity Is Essential)**:
     Without constructing the MCMF network (Hubs $A, B \to i$, with parallel drain edges of cost $0$ and $+p_i u_i \ge 0$ from $i \to T$), proving that the 2-commodity value function $F(a, b)$ is concave in both $a$ and $b$ requires tedious exchange-argument casework. With Iteration 27 + Iteration 29, concavity is an **immediate 1-line corollary** of the fact that $+p_i u_i \ge 0$ is a valid convex marginal edge split!

- **3-Tier Progressive Hints**:
  - *Hint 1*: Build an MCMF network with Pokéball hub $A$ (supply $a$), Ultraball hub $B$ (supply $b$), edges $(A \to i, 1, -p_i)$ and $(B \to i, 1, -u_i)$, and two parallel edges from $i \to T$ of capacity $1$ and costs $0$ and $+p_i u_i \ge 0$.
  - *Hint 2*: Since $+p_i u_i \ge 0 \ge 0$, Iteration 29 and Iteration 27 guarantee that the optimal answer $F(a, b)$ is concave in both $a$ and $b$!
  - *Hint 3*: Run nested WQS binary search on the penalties $\lambda_A, \lambda_B \in [0, 1]$; for fixed $(\lambda_A, \lambda_B)$, each Pokémon $i$ independently selects $\max(0, p_i - \lambda_A, u_i - \lambda_B, p_i + u_i - p_i u_i - \lambda_A - \lambda_B)$ in $O(1)$ time.

---

#### Problem 4.4 — Toroidal Grid Cycle Cover (`[TJOI2013 / Luogu P3965 / BZOJ 3171] 循环格`)
- **Judge & URL**: [Luogu P3965](https://www.luogu.com.cn/problem/P3965) (`[ZH]` TJOI2013 循环格)
- **Inline Statement & Constraints**:
  Given an $R \times C$ toroidal grid ($R, C \le 15$, where row $R$ wraps to $1$ and column $C$ wraps to $1$), each cell $(i, j)$ contains an arrow `U`, `D`, `L`, or `R` pointing to one of its 4 neighbors. Changing a cell's arrow costs $1$. Find the minimum number of arrow changes so that every cell has **in-degree $1$ and out-degree $1$** (i.e., the arrows partition the grid into vertex-disjoint directed cycles).

- **4-Step "Zero Magic Gadgets" Compilation**:
  1. **Step 1 (Diagnostic Signal)**:
     A directed graph has in-degree $1$ and out-degree $1$ at every vertex iff it is a collection of vertex-disjoint directed cycles, which is equivalent to a **perfect bipartite matching** between Out-ports $u_{\text{out}}$ and In-ports $v_{\text{in}}$!
  2. **Step 2 (Algebraic Intermediate)**:
     Let $x_{u, v} \in \{0, 1\}$ indicate whether cell $u$'s arrow points to neighbor $v \in N(u)$, with cost $c(u, v) = 0$ if $v$ is the original arrow direction of $u$, and $c(u, v) = 1$ otherwise.
     $$\min \sum_{u} \sum_{v \in N(u)} c(u, v) x_{u, v} \quad \text{s.t.} \quad \sum_{v \in N(u)} x_{u, v} = 1 \; (\forall u), \quad \sum_{u \in N(v)} x_{u, v} = 1 \; (\forall v).$$
  3. **Step 3 (Mechanical Graph Compilation)**:
     - Create $S$, $T$, and for each cell $u \in \{1, \dots, R\} \times \{1, \dots, C\}$, create $u_{\text{out}}$ and $u_{\text{in}}$.
     - Add $(S \to u_{\text{out}}, \text{cap } 1, \text{cost } 0)$ and $(u_{\text{in}} \to T, \text{cap } 1, \text{cost } 0)$.
     - For each of the 4 toroidal neighbors $v$ of $u$, add $(u_{\text{out}} \to v_{\text{in}}, \text{cap } 1, \text{cost } [v \ne \text{dir}(u)])$.
     - Since all costs are in $\{0, 1\} \ge 0$, initialize $\pi_0 = 0$ and run MCMF (or Zkw Primal–Dual) of volume $R \times C$!
  4. **Step 4 (Connection to Mandatory Initial Saturation)**:
     Notice what happens if you apply **Iteration 28.2 (Mandatory Initial Saturation)** to the $0$-cost original arrow edges (or think of them as cost $-1$ rewards relative to a base cost of $R \cdot C$): pre-saturating every cell's original arrow $(u \to \text{dir}(u))$ leaves node imbalances $M(v) = \text{in\_deg}_0(v) - 1$, and we simply route flow from cells with $\text{in\_deg}_0 > 1$ to cells with $\text{in\_deg}_0 = 0$ along the grid!

- **3-Tier Progressive Hints**:
  - *Hint 1*: What local degree condition on a directed graph is necessary and sufficient for the graph to be a union of vertex-disjoint directed cycles?
  - *Hint 2*: Split each grid cell $u$ into an out-port $u_{\text{out}}$ (connected from $S$ with capacity $1$) and an in-port $u_{\text{in}}$ (connected to $T$ with capacity $1$).
  - *Hint 3*: Connect $u_{\text{out}} \to v_{\text{in}}$ for all 4 toroidal neighbors $v$ with cost $0$ in the original arrow direction and cost $1$ in the other 3 directions, and run MCMF.

---

#### Problem 4.5 — The Grandmaster Wave 3B Capstone Synthesis (`[Codeforces 708 D] Incorrect Flow`)
- **Judge & URL**: [Codeforces 708D — Incorrect Flow](https://codeforces.com/problemset/problem/708/D) (`[EN]`)
- **Inline Statement & Constraints**:
  You are given a directed network $G = (V, E)$ ($n \le 100, m \le 100$) with source $1$ and sink $n$. Each edge $e = (u \to v)$ currently has capacity $c_e \ge 0$ and an alleged flow value $f_e \ge 0$. However, the given $(c_e, f_e)$ may be **completely invalid**: we might have $f_e > c_e$ on some edges, and flow conservation at vertices $v \in \{2, \dots, n-1\}$ might be violated! In $1$ operation (cost $1$), you can increment or decrement any $f_e$ by $1$ (keeping $f_e \ge 0$) or increment or decrement any $c_e$ by $1$ (keeping $c_e \ge 0$). Find the minimum total operations to make $(c'_e, f'_e)$ a valid $1$-$n$ flow where $0 \le f'_e \le c'_e$ on all edges and flow is conserved at all $v \in \{2, \dots, n-1\}$.

- **4-Step "Zero Magic Gadgets" Compilation (Synthesizing Iterations 26, 28, and 29!)**:
  1. **Step 1 (Non-Graph Diagnostic Signal)**:
     For a single edge $e = (u \to v)$ with initial $(c_e, f_e)$, if we choose its final flow to be $f'_e \ge 0$, we will obviously set its final capacity to $c'_e = \max(c_e, f'_e)$ (we never need to lower $c_e$, and if $f'_e > c_e$ we must raise $c'_e$ to $f'_e$).
     Thus, the minimum cost to adjust edge $e$ to carry final flow $f'_e \ge 0$ is a **univariate piecewise-linear convex function** $g_e(f'_e)$:
     $$g_e(f'_e) = |f'_e - f_e| + \max(0, \; f'_e - c_e)!$$
     Look at that formula: it combines **Iteration 29 (Piecewise-Linear Convex Marginal Splitting)** with **Iteration 28 (Lower-Bound Circulation + Mandatory Initial Saturation)**!
  2. **Step 2 (Algebraic Intermediate — Splitting $g_e(f'_e)$ relative to the Initial Flow $f_e$)**:
     Instead of starting from $0$ flow, **pre-inject the initial flow $f_e$ on every edge $e = (u \to v)$** (contributing $-f_e$ to $M(u)$ and $+f_e$ to $M(v)$), and analyze the marginal cost of **decreasing** $f'_e$ below $f_e$ (sending flow backward $v \to u$) or **increasing** $f'_e$ above $f_e$ (sending flow forward $u \to v$) in the two cases $f_e \le c_e$ vs. $f_e > c_e$:

     - **Case A: $f_e \le c_e$ (Initially within capacity; base cost $= 0$)**:
       - **Decreasing $f'_e$ on $[0, f_e]$**: Sending $1$ unit backward along $(v \to u)$ decreases $|f'_e - f_e|$ by $+1 \implies$ add backward edge $(v \to u, \text{cap } f_e, \text{cost } 1)$.
       - **Increasing $f'_e$ on $[f_e, c_e]$**: Sending $1$ unit forward along $(u \to v)$ up to $c_e$ costs $+1$ (only $f'_e$ increases) $\implies$ add forward edge $(u \to v, \text{cap } c_e - f_e, \text{cost } 1)$.
       - **Increasing $f'_e$ on $[c_e, \infty)$**: Above $c_e$, both $f'_e$ and $c'_e$ must increase together, costing $+2$ per unit $\implies$ add forward edge $(u \to v, \text{cap } \infty, \text{cost } 2)$.
       *(Check convexity of slopes on $[0, \infty)$: $-1 \le +1 \le +2$ — strictly convex!)*

     - **Case B: $f_e > c_e$ (Initially overflowing capacity by $f_e - c_e$!)**:
       - Even if we leave $f'_e = f_e$ unchanged, we must pay a mandatory base cost of $f_e - c_e$ to raise $c'_e$ up to $f_e$! So add $f_e - c_e$ to $C_{\text{base}}$.
       - Now look at the marginal cost relative to $f'_e = f_e$:
         - **Decreasing $f'_e$ on $[c_e, f_e]$**: When we reduce $f'_e$ by $1$ unit in $[c_e, f_e]$, we pay $+1$ to reduce $f'_e$, **and we save $-1$ on raising $c'_e$**! Net marginal cost: $+1 - 1 = 0$! $\implies$ add backward edge $(v \to u, \text{cap } f_e - c_e, \text{cost } 0)$!
         - **Decreasing $f'_e$ on $[0, c_e]$**: Below $c_e$, reducing $f'_e$ no longer saves on $c'_e$, so it costs $+1$ per unit $\implies$ add backward edge $(v \to u, \text{cap } c_e, \text{cost } 1)$.
         - **Increasing $f'_e$ on $[f_e, \infty)$**: Above $f_e > c_e$, both $f'_e$ and $c'_e$ increase together, costing $+2$ per unit $\implies$ add forward edge $(u \to v, \text{cap } \infty, \text{cost } 2)$.
       *(Check convexity of slopes on $[0, \infty)$: $-1 \le 0 \le +2$ — strictly convex, and relative to $f_e$ all forward/backward edge costs are $\ge 0$!)*

  3. **Step 3 (Mechanical Graph Compilation)**:
     - Pre-inject $f_e$ on every edge $e = (u \to v)$: update $M(u) \mathrel{-}= f_e$, $M(v) \mathrel{+}= f_e$.
     - Add the 3 linear segment edges for each $e$ according to Case A ($f_e \le c_e$) or Case B ($f_e > c_e$).
     - Add the circulation feedback edge $(n \to 1, \text{cap } \infty, \text{cost } 0)$ so $1$ and $n$ can have any valid net $1$-$n$ flow.
     - Connect $S^* \to v$ (for $M(v) > 0$) and $u \to T^*$ (for $M(u) < 0$), set $\pi_0 = 0$ (all compiled edge costs are in $\{0, 1, 2\} \ge 0$!), and run a single Dijkstra MCMF from $S^*$ to $T^*$! Output $C_{\text{base}} + C^*$.
  4. **Step 4 (Why Pre-Injecting $f_e$ Saved Us from Negative Edges)**:
     Had we measured flow from $0$ instead of $f_e$, decreasing $f'_e$ from $f_e$ down to $0$ would have been represented as a forward edge on $[0, f_e]$ with **negative marginal slope $-1$** (in Case A) and **$0$** (on $[c_e, f_e]$ in Case B), which by Iteration 28.2 (`负权边强制满流消圈法`) would be pre-saturated to $f_e$ and flipped into the exact backward edges $(v \to u)$ we just derived! Thus our expansion around $f_e$ is literally the combined application of Iteration 28.2 and Iteration 29!

- **3-Tier Progressive Hints**:
  - *Hint 1*: For a single edge with initial $(c_e, f_e)$, write the cost of setting its final flow to $f'_e \ge 0$ as $g_e(f'_e) = |f'_e - f_e| + \max(0, f'_e - c_e)$ and check its slopes on $[0, \min(f_e, c_e)]$, $[\min(f_e, c_e), \max(f_e, c_e)]$, and $[\max(f_e, c_e), \infty)$.
  - *Hint 2*: Pre-inject the initial flow $f_e$ on every edge $u \to v$ (updating $M(u) \mathrel{-}= f_e, M(v) \mathrel{+}= f_e$) and express changes $f'_e - f_e$ as forward edges $(u \to v)$ and backward edges $(v \to u)$ of non-negative cost!
  - *Hint 3*: Add the circulation edge $(n \to 1, \infty, 0)$, connect $S^*, T^*$ according to $M(v)$, and run Engine 28B from $S^*$ to $T^*$.

---

## Quarantined Pure Template Problems (`R-26` to `R-33`)

Per `AGENTS.md` and `flows_research/PLAN.md`, pure algorithm-verification problems that require zero modelling beyond copying a library routine are quarantined from the main problem ladders and indexed here for baseline reference only:

| Quarantine ID | Judge & Problem Title | Underlying Engine Tested | Why Quarantined |
| :--- | :--- | :--- | :--- |
| **`R-26`** | [Luogu P3381 — 【模板】最小费用最大流](https://www.luogu.com.cn/problem/P3381) | Standard SSP / Zkw MCMF | Bare template: given $(u, v, w, c)$, output max flow and min cost. |
| **`R-27`** | [LOJ #102 — 最小费用流](https://loj.ac/p/102) | SSP with Johnson Potentials / Zkw | Bare MCMF benchmark ($N \le 400, M \le 15000$). |
| **`R-28`** | [Library Checker — Minimum Cost $b$-Flow](https://judge.yosupo.jp/problem/min_cost_b_flow) | Lower-Bound MCMF + Negative Cycle Elimination (Iter 28) | Raw mathematical specification of $b$-flow with $[l_e, u_e]$ and negative costs; no English-to-graph modelling. |
| **`R-29`** | [Library Checker — Assignment Problem](https://judge.yosupo.jp/problem/assignment) | Dense Bipartite Min-Cost Matching ($O(N^3)$ Dijkstra / Hungarian) | Direct $N \times N$ matrix input. |
| **`R-30`** | [UOJ #487 / Luogu P7173 — 【模板】有负圈的费用流](https://www.luogu.com.cn/problem/P7173) | Mandatory Initial Saturation (`负权边强制满流消圈法`, Iter 28.2) | Bare verification template for negative-cycle MCMF. |
| **`R-31`** | [Aizu GRL_6_B — Minimum Cost Flow](https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B) | Fixed-Volume SSP + Dijkstra | Direct graph input. |
| **`R-32`** | [CSES 2129 — Task Assignment](https://cses.fi/problemset/task/2129) | Bipartite Min-Cost Matching | Bare textbook assignment problem. |
| **`R-33`** | [CSES 2130 — Distinct Routes II](https://cses.fi/problemset/task/2130) | $K$-Edge-Disjoint Shortest Paths | Direct unit-capacity MCMF of volume $K$. |

---

## Multilingual (`[EN]` / `[ZH]` / `[JA]`) Bibliography & Sources for Wave 3B

### 1. English (`[EN]`) Textbooks, Seminal Papers & Tutorials
- **[Ahuja-Magnanti-Orlin 1993]** Ravindra K. Ahuja, Thomas L. Magnanti, and James B. Orlin, *Network Flows: Theory, Algorithms, and Applications*, Prentice Hall, 1993 — Chapters 9–11 (Negative-Cycle Optimality Theorem, Successive Shortest Path, Reduced Costs & Node Potentials, Cycle Canceling) and Chapter 14 (Convex Cost Flows & Piecewise-Linear Separable Convex Transformation).
- **[Klein 1967]** Morton Klein, *"A primal method for minimal cost flows with applications to the assignment and transportation problems"*, Management Science 14(3):205–220, 1967 — Original negative-cycle optimality characterization.
- **[Edmonds-Karp 1972]** Jack Edmonds and Richard M. Karp, *"Theoretical improvements in algorithmic efficiency for network flow problems"*, JACM 19(2):248–264, 1972 — Introducing Johnson/Edmonds–Karp node potential scaling to eliminate negative-weight shortest path searches in MCMF.
- **[CP-Algorithms MCMF]** *Minimum-cost flow — Successive shortest path algorithm with potentials*, `cp-algorithms.com/graph/min_cost_flow.html`.

### 2. Chinese (`[ZH]`) National Team Papers (`国家集训队论文`) & Treatises
- **[Zkw / 张昆玮 2009–2011]** 张昆玮 (Tsinghua University), *《统计的力量——线段树全接触》 & Zkw Primal–Dual Cost Flow Lecture Notes (`zkw费用流`)* — Introducing the multi-path blocking-flow Primal–Dual algorithm to Chinese competitive programming and analyzing its speed on short dense graphs vs. zero-cost DAG traps.
- **[陈丹琦 / 国家集训队 2008–2012]** NOI2008 `志愿者招募` & WC2007 `剪刀石头布` official editorials and National Team lectures on **The Equation-Difference Method (`流守恒方程差分建模法` / `不等式转等式差分构图`)** and **Complement Counting + Convex Edge Splitting (`补集转化与凸费用拆边`)**.
- **[姜志豪 2016]** 姜志豪, *《网络流的一些建模方法》*, IOI 2016 Chinese National Team Paper (`国家集训队2016论文集`) — Systematic taxonomy of convex marginal edge splitting, equation-difference compilation, and degree-constrained flow reductions.
- **[王우선 / 模拟费用流与凸性 2018]** IOI 2018 Chinese National Team Paper on slope convexity of $C(f)$, WQS binary search on flow volume, and simulated cost flow (`模拟费用流`).
- **[OI-Wiki MCMF & Upper-Lower Bounds]** *OI-Wiki: 最小费用最大流 & 上下界网络流 (含负圈消除)*, `oi-wiki.org/graph/flow/min-cost/` and `oi-wiki.org/graph/flow/bound/`.

### 3. Japanese (`[JA]`) Algorithmic Treatises & AtCoder Archives
- **[snuke / rng_58 AtCoder AGC & ABC Editorials]** AtCoder Grand Contest `AGC 018 C — Coins`, `ABC 247 G — Dream Team`, and `ABC 214` editorials on MCMF slope convexity $C(f)$ (`流量に関する下に凸性`), potential initialization on DAGs (`DAG上のポテンシャル初期化`), and priority-queue residual simulation.
- **[tatyam / maspypy / noshi91 Flow Notes]** Japanese competitive programming treatises on `最小費用流 (Min-Cost Flow)` with negative edges (`負辺除去 / 最小費用循環流`), convex edge splitting (`下に凸なコスト関数の辺分割`), and LP duality bridges (`双対問題と最小費用流`).
