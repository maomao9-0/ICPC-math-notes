# Wave 4B Research Monograph (Cohort 2: Iterations 88–92)
## Linear Programming Duality, Totally Unimodular (TU) Matrices, Complementary Slackness & Submodular / Polymatroid Flows

> [!IMPORTANT]
> **Cohort 2 Independent Redundant Research Mandate**
> This monograph is authored independently under Cohort 2 (Iterations 88–92) of the `flows_research` multi-cohort discovery pipeline. Every modelling reduction, duality transformation, polyhedral theorem, and curated problem strictly follows the **4-Step "Zero Magic Gadgets" Compilation Standard**: (1) Non-Graph Diagnostic Signal, (2) Algebraic / Logical Intermediate Representation, (3) Reverse-Engineering Scratchpad (Mechanical Graph Compilation), and (4) Hand-Checkable Toy Trace & Broken Gadget Counterexamples.

---

## Executive Overview: Why Polyhedral Duality & Submodularity Are the True Compiler of Network Flows

Across competitive programming, the vast majority of "unintuitive" flow and minimum-cut problems are not born as graph problems. Instead, they originate in one of three disguised mathematical forms:

1. **Continuous or Integer Linear Inequality Systems**: Problems asking to modify array elements, adjust edge lengths on shortest/longest paths, schedule overlapping intervals, or perturb spanning tree weights at minimum linear cost (`[ZJOI2013] 防守战线`, `[SHOI2004] 最小生成树`, `[NOI2008] 志愿者招募`, Project Crashing). Attempting to guess a flow network directly from the English statement feels like black magic because the problem variables represent **potentials** (timestamps, prefix sums, node prices) rather than **flows**.
2. **Structured $0$-$1$ Integer Linear Programs ($A x \le b$)**: Problems where choices are discrete, yet the constraint matrix $A$ secretly possesses **Total Unimodularity (TU)**—via the **Consecutive-Ones Property (`连续 1 性质`)**, **Ghouila–Houri Equitable Bicoloring**, or **Rooted Tree-Path Incidence**—guaranteeing that the continuous LP relaxation has an exact integer optimum and compiles mechanically into a network circulation.
3. **Submodular Energy & Level-Set Minimization**: Problems over binary partitions $S \subseteq V$ or multi-state integer arrays $h \in \mathbb{Z}^V$ whose penalty function satisfies the diminishing-returns inequality $f(A) + f(B) \ge f(A \cup B) + f(A \cap B)$, or whose continuous **Lovász Extension** $\hat{f}(x)$ decomposes into independent binary threshold cuts (`CF 1427G — One Billion Shades of Grey`, `[省选联考 2020] 保序回归`).

This monograph unifies these three pillars across five deep iterations:

- **Iteration 88** constructs a mechanical **LP Primal–Dual Compiler**: write the natural inequality system as a Primal LP, apply the Lagrangian transpose dictionary, and watch the dual variables automatically acquire the flow-conservation signature (one $+1$ and one $-1$ per column).
- **Iteration 89** establishes **Complementary Slackness (`互补松弛定理`)** as a constructive two-way bridge, proving how to recover explicit primal potentials $\pi^*(v)$ and optimal weight perturbations $\Delta^*(e)$ directly from shortest-path distances in the final residual network $G_{f^*}$.
- **Iteration 90** proves the **Hoffman–Kruskal Theorem** and **Ghouila–Houri Theorem**, shows why the **Consecutive-Ones Property** is transpose-invariant and why multiplying by the upper-bidiagonal difference matrix $D$ converts interval matrices into directed graph incidence matrices, and pinpoints the exact boundary between TU vertical tree paths and non-TU undirected star paths ($\det = \pm 2$).
- **Iteration 91** develops **Submodular Function Minimization (SFM)**, **Polymatroids**, **Edmonds' Greedy Algorithm**, and the **Lovász Extension**, proving why convex total-variation energies decouple across level sets.
- **Iteration 92** maps the exact computational frontier separating **Network Flows** (intersection of two partition/laminar matroids), **General Matroid Intersection** (graphic $\cap$ partition matroids), **Polynomial Middle-Vertex Split 3-Entity Matching**, and **NP-Hard 3D Matching / Integer 2-Commodity Flow**.

---

## Iteration 88: Explicit Linear Programming Primal–Dual Compilation (`线性规划对偶转网络流`)

### 88.1 The Universal Mechanical Dualization Recipe (The "Sign-to-Orientation" Compiler)

When a problem asks to choose values $y_1, y_2, \dots, y_m$ satisfying pairwise difference inequalities $y_v - y_u \ge d_{uv}$ or interval sum bounds $\sum_{k=l_i}^{r_i} a_k \ge C_i$, the natural variables $y_u$ do not conserve flow—they are **node potentials**. Rather than guessing a flow graph, we write the **Primal Linear Program** in the natural variables $y$ and mechanically take its **Dual Linear Program** in multiplier variables $f$.

#### The Lagrangian Derivation (Zero Memorization Required)

Suppose we wish to solve a Primal minimization problem over variables $y \in \mathbb{R}^m$:
$$\text{Primal (P):} \quad \min_{y} \; b^\top y \quad \text{subject to} \quad A^\top y \ge c,$$
where $A$ is an $m \times k$ matrix, $b \in \mathbb{R}^m$, and $c \in \mathbb{R}^k$. To bound the minimum from below, introduce a vector of non-negative **Lagrange multipliers (dual flow variables)** $f \in \mathbb{R}_{\ge 0}^k$, one for each inequality in $A^\top y \ge c$. Since $f \ge 0$ and $A^\top y - c \ge 0$, their inner product is non-negative:
$$b^\top y \ge b^\top y - f^\top (A^\top y - c) = c^\top f + (b - A f)^\top y.$$
For the lower bound $c^\top f$ to remain finite (not $-\infty$) as $y$ varies over its allowed domain, the coefficient vector $(b - A f)$ multiplying $y$ must satisfy sign constraints dual to the domain of $y$:

- If $y_u \in \mathbb{R}$ is a **free (unrestricted) potential**, any non-zero coefficient $(b - Af)_u \neq 0$ would allow $y_u \to \pm \infty$ to send the bound to $-\infty$. Thus we are forced to require exact equality:
  $$(A f)_u = b_u \quad \Longleftrightarrow \quad \sum_{e \in \delta^+(u)} f_e - \sum_{e \in \delta^-(u)} f_e = b_u.$$
- If $y_u \ge 0$ is restricted to be **non-negative**, then to avoid $(b - Af)_u y_u \to -\infty$ as $y_u \to +\infty$, we require $(b - Af)_u \ge 0$, i.e., $(Af)_u \le b_u$.

This yields the **Master Primal–Dual Compilation Dictionary**:

| Primal Minimization ($\min b^\top y$) | Dual Maximization ($\max c^\top f$) | Network Flow Interpretation |
| :--- | :--- | :--- |
| **Free variable** $y_u \in \mathbb{R}$ | **Equality constraint** $(Af)_u = b_u$ | **Vertex $u$** with net flow demand/supply $b_u$ ($\text{out} - \text{in} = b_u$) |
| **Non-negative variable** $y_u \ge 0$ | **Inequality constraint** $(Af)_u \le b_u$ | **Vertex $u$** with slack edge to ground/sink, or **Edge capacity** upper bound |
| **Difference constraint** $y_v - y_u \ge c_e$ | **Non-negative variable** $f_e \ge 0$ | **Directed edge** $e = (u \to v)$ carrying flow $f_e \ge 0$ with unit benefit $c_e$ |
| **Bounded variable** $0 \le \Delta_e \le u_e$ | **Split constraint** with capacity dual $z_e \ge 0$ | **Capacitated edge** $f_e \le u_e$ (after eliminating $z_e = \max(0, f_e - w_e)$) |

> [!TIP]
> **The Column-Incidence Recognition Theorem (Why the Dual is a Flow Network)**
> Suppose every inequality $e \in \{1, \dots, k\}$ in the Primal LP has the difference form $y_{\text{head}(e)} - y_{\text{tail}(e)} \ge c_e$ (or single-variable form $\pm y_u \ge c_e$). Then in the transposed dual matrix $A$, the $e$-th column has **at most one $+1$** (at row $\text{head}(e)$) and **at most one $-1$** (at row $\text{tail}(e)$).
> By adding one redundant ground equation $r_0 = -\sum_{u=1}^m r_u$ (representing a reference node $v_0$ with potential $y_0 = 0$), **every single column of $A$ has exactly one $+1$ and one $-1$**. Thus $A f = b$ is literally the **Kirchhoff flow-conservation system** of a directed graph $G = (V \cup \{v_0\}, E)$!

---

### 88.2 Archetype 1: Potential Difference & Project Crashing Problems (`工期压缩 / 最短路与最长路边权修改`)

Let us apply the 4-Step Compilation Standard to one of the most frequent disguises of LP duality: modifying edge weights or array elements so that shortest paths, longest DAG paths, or interval sums satisfy global thresholds.

#### Step 1: The Non-Graph Diagnostic Signal (Recognition)

You are given either:
- **Project Crashing / DAG Critical Path Compression**: A DAG $G = (V, E)$ representing tasks where edge $e = (u, v)$ has base duration $d_e$. You can pay $c_e$ per unit to compress ("crash") the duration of edge $e$ by $\Delta_e \in [0, b_e]$, reducing its length to $d_e - \Delta_e$, or pay to extend it. You want all $s$-$t$ paths to have total length $\le T$ (so the project finishes by deadline $T$) at minimum total cost $\sum_e c_e \Delta_e$.
- **Prefix-Sum / Interval Coverage Modification (`[ZJOI2013] 防守战线`)**: Choose non-negative values $a_1, \dots, a_n$ at unit cost $C_i$ per unit of $a_i$ (with upper bound $a_i \le 1$ or $a_i \le u_i$) such that every required interval $[l_j, r_j]$ has sum $\sum_{k=l_j}^{r_j} a_k \ge d_j$.

**Why Naive DP and Direct Cut Intuition Fail**:
1. In Project Crashing, a single edge $e$ may belong to exponentially many $s$-$t$ paths, and compressing $e$ simultaneously shortens all of them. Unlike standard Shortest-Path Blocking (where increasing edge weights to make *all* paths $\ge T$ reduces to standard $s$-$t$ Min-Cut), **decreasing** edge weights to make *all* paths $\le T$ (i.e., reducing the *maximum* path length) is **not** a simple $s$-$t$ cut in the original graph!
2. In `[ZJOI2013] 防守战线`, intervals overlap arbitrarily, breaking DP state sizes unless we rewrite interval sums as potential differences $S_{r_j} - S_{l_j-1} \ge d_j$.

#### Step 2: The Algebraic / Logical Intermediate Representation

Instead of writing one constraint per $s$-$t$ path (which would create exponentially many rows), we introduce **node potentials (completion timestamps)** $\pi_v \in \mathbb{R}$ for each $v \in V$:

- Every edge $e = (u, v) \in E$ has effective duration $d_e - \Delta_e$, so vertex $v$ cannot complete before $\pi_u + d_e - \Delta_e$:
  $$\pi_v - \pi_u + \Delta_e \ge d_e \quad \forall e = (u, v) \in E.$$
- The total project duration from source $s$ to sink $t$ must not exceed $T$:
  $$\pi_t - \pi_s \le T \quad \Longleftrightarrow \quad \pi_s - \pi_t \ge -T.$$
- Each compression variable satisfies $0 \le \Delta_e \le b_e$, which we write in standard minimization form as $\Delta_e \ge 0$ and $-\Delta_e \ge -b_e$.

This gives the compact **Primal LP**:
$$\begin{aligned}
\min_{\pi, \Delta} \quad & \sum_{e \in E} c_e \Delta_e \\
\text{s.t.} \quad & \pi_v - \pi_u + \Delta_e \ge d_e && \forall e = (u,v) \in E && \text{[dual variable } f_e \ge 0\text{]} \\
& \pi_s - \pi_t \ge -T && && \text{[dual variable } F \ge 0\text{]} \\
& -\Delta_e \ge -b_e && \forall e \in E && \text{[dual variable } z_e \ge 0\text{]} \\
& \pi_v \in \mathbb{R} \text{ free}, \quad \Delta_e \ge 0.
\end{aligned}$$

#### Step 3: The Reverse-Engineering Scratchpad (Mechanical Graph Compilation)

Now we apply the Lagrangian Dual Dictionary mechanically:

1. **Dual Objective**: Multiply each right-hand side by its dual variable and maximize:
   $$\max_{f, F, z \ge 0} \; \sum_{e \in E} d_e f_e - T \cdot F - \sum_{e \in E} b_e z_e.$$
2. **Dual Constraints from Free Potentials $\pi_v \in \mathbb{R}$**:
   In the Primal constraints, $\pi_v$ appears with $+1$ whenever $v$ is the head of an edge $e = (u, v)$ (or $v=s$ in $\pi_s - \pi_t \ge -T$), and with $-1$ whenever $v$ is the tail of an edge $e = (v, w)$ (or $v=t$ in $\pi_s - \pi_t \ge -T$). Since $\pi_v$ has coefficient $0$ in the Primal objective and is unconstrained in sign, its dual constraint is an **exact flow-conservation equation**:
   $$\sum_{e \in \delta^-(v)} f_e - \sum_{e \in \delta^+(v)} f_e = \begin{cases} -F & \text{if } v = s, \\ +F & \text{if } v = t, \\ 0 & \text{if } v \notin \{s, t\}. \end{cases}$$
   Look at what just happened: the dual variables $f_e \ge 0$ form an **$s$-$t$ flow of total volume $F$** on the original directed graph $G = (V, E)$, with a return edge $(t \to s)$ carrying flow $F$!
3. **Dual Constraints from Compression Variables $\Delta_e \ge 0$**:
   In the Primal LP, $\Delta_e$ has objective coefficient $c_e$, appears with $+1$ in the edge constraint $f_e$, and appears with $-1$ in the capacity constraint $z_e$. Since $\Delta_e \ge 0$, the dual constraint is:
   $$f_e - z_e \le c_e \quad \Longleftrightarrow \quad z_e \ge f_e - c_e.$$
   Since $z_e \ge 0$ has a negative coefficient $-b_e \le 0$ in the dual maximization objective, an optimal dual solution always sets $z_e = \max(0, f_e - c_e)$.
4. **Splitting Flow $f_e$ into Two Parallel Edges**:
   How do we represent the concave piecewise-linear reward $d_e f_e - b_e \max(0, f_e - c_e)$ as a standard network flow?
   Split the flow $f_e$ on edge $e = (u, v)$ into two parallel directed edges $f_e = f_{e,1} + f_{e,2}$:
   - **Edge 1 (Normal Regime $f_e \le c_e$)**: Directed edge $u \to v$ with **capacity $c_e$** and **unit cost $-d_e$** (in Min-Cost Circulation form,since $\max \sum d_e f_e \iff \min \sum (-d_e) f_e$).
   - **Edge 2 (Crashed Regime $f_e > c_e$)**: Directed edge $u \to v$ with **capacity $\infty$** and **unit cost $-(d_e - b_e)$**!
   - **Return Edge**: Directed edge $t \to s$ with **capacity $\infty$** and **unit cost $+T$**.

> [!IMPORTANT]
> **Role Reversal in Project Crashing Duals!**
> Notice the astonishing role reversal produced by LP Duality:
> - The Primal **money cost** $c_e$ became the Dual **edge capacity** on the first parallel edge!
> - The Primal **base duration** $d_e$ and **crashing limit** $b_e$ became the Dual **edge costs** $-d_e$ and $-(d_e - b_e)$!
> Nobody could guess that "money cost = capacity" and "time = cost" by staring at the graph without writing the LP Dual!

```
Primal Edge e = (u -> v): duration d_e - \Delta_e, \Delta_e in [0, b_e], unit crashing cost c_e
                                      ||
                          [Mechanical LP Dualization]
                                      ||
                                      \/
                      cap = c_e, cost = -d_e
                   .-------------------------->.
                  /                             \
            ( u )                                 ( v )
                  \                             /
                   '-------------------------->'
                      cap = inf, cost = -(d_e - b_e)
```

#### Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

**Toy Trace ($N = 3$ DAG)**:
Let $V = \{1, 2, 3\}$ with $s = 1, t = 3$, target deadline $T = 4$, and three edges:
- $e_1 = (1 \to 2)$: duration $d_1 = 3$, max crash $b_1 = 2$, unit crash cost $c_1 = 5$.
- $e_2 = (2 \to 3)$: duration $d_2 = 3$, max crash $b_2 = 2$, unit crash cost $c_2 = 2$.
- $e_3 = (1 \to 3)$: duration $d_3 = 5$, max crash $b_3 = 2$, unit crash cost $c_3 = 4$.

1. **Primal Inspection**: Path $1 \to 2 \to 3$ has length $3 + 3 = 6$ (needs $2$ units of crashing to reach $T = 4$). Path $1 \to 3$ has length $5$ (needs $1$ unit of crashing to reach $T = 4$).
   Cheapest Primal crash: crash $e_2$ by $\Delta_2 = 2$ (cost $2 \times 2 = 4$) and crash $e_3$ by $\Delta_3 = 1$ (cost $1 \times 4 = 4$). Total Primal cost $= 4 + 4 = 8$, with potentials $\pi_1 = 0, \pi_2 = 3, \pi_3 = 4$.
2. **Dual Network Verification**:
   - Send flow $f_{e_2} = 2$ along path $1 \to 2 \to 3$ (bottlenecked by $\min(c_1, c_2) = \min(5, 2) = 2$ on the first parallel edges) and $f_{e_3} = 4$ along $1 \to 3$? Wait: along $1 \to 3$, the first edge has cost $-d_3 = -5$ and return edge $3 \to 1$ has cost $+T = +4$, so net cycle cost is $-5 + 4 = -1 < 0$! Thus we saturate the first parallel edge of $1 \to 3$ up to capacity $c_3 = 4$, gaining $4 \times (5 - 4) = 4$.
   - Along $1 \to 2 \to 3 \to 1$, the first parallel edges have cycle cost $-d_1 - d_2 + T = -3 - 3 + 4 = -2 < 0$, and capacity $\min(c_1, c_2) = 2$, gaining $2 \times (6 - 4) = 4$.
   - Any further flow on $1 \to 2 \to 3$ must use the second parallel edge of $e_2$, which has cost $-(d_2 - b_2) = -(3 - 2) = -1$, making the cycle cost $-3 - 1 + 4 = 0$ (no further negative cycle).
   - Total Dual Max Objective $= -\text{MinCostCirculation} = 4 + 4 = 8$. Exact match!

**Broken Gadget Counterexamples**:
1. **Failure Mode A — Confusing Shortest-Path Extension with Longest-Path Compression**:
   Suppose instead the problem asks to *increase* edge lengths $d_e \gets d_e + \Delta_e$ so the **shortest** $s$-$t$ path is $\ge T$. Then the Primal constraints are $\pi_v - \pi_u - \Delta_e \le d_e$ with $\pi_t - \pi_s \ge T$. Dualizing gives $\sum_{e} d_e f_e$ *minimized* subject to $0 \le f_e \le c_e$ and $F = 1$ unit of flow—or if $d_e = 0$ and we want to block all zero-length paths, a standard $s$-$t$ Min-Cut! Reversing the inequality direction flips $\min \leftrightarrow \max$ on the path lengths and completely changes whether $c_e$ is a capacity or a cost.
2. **Failure Mode B — Omitting the Crashed-Regime Parallel Edge ($z_e$ omission)**:
   If an edge has finite maximum crash $b_e < \infty$ and you omit the second parallel edge of cost $-(d_e - b_e)$ and capacity $\infty$, you are implicitly setting $b_e = \infty$ (unbounded crashing). For our toy trace, if $b_2 = 1$ instead of $2$, the second parallel edge on $e_2$ has cost $-(3 - 1) = -2$, so the cycle $1 \to 2 \to 3 \to 1$ still has negative cost $-3 - 2 + 4 = -1 < 0$ and routes $3$ more units of flow (bottlenecked by $c_1 - 2 = 3$ on $e_1$), increasing the optimal cost from $8$ to $4 + 4 + 3(1) = 11$ (corresponding to crashing $e_2$ by $b_2 = 1$ at cost $2$, $e_1$ by $1$ at cost $5$, and $e_3$ by $1$ at cost $4$: $2 + 5 + 4 = 11$).

---

### 88.3 Archetype 2: Inverse MST & Inverse Matroid Basis (`[SHOI2004] 最小生成树`, `[BZOJ 3118] Orz the Immortal`)

#### Step 1: The Non-Graph Diagnostic Signal (Recognition)

You are given an undirected connected graph $G = (V, E)$ with initial edge weights $w_e$, and a designated spanning tree $T^* \subseteq E$ (or edge $e^*$ that must appear in an MST). You may modify each edge's weight to $w'_e = w_e + \Delta_e$ at cost $c_e |\Delta_e|$. Find the minimum total modification cost so that $T^*$ becomes a Minimum Spanning Tree of $G$ under $w'$.

**Why Greedy and Standard Cut Reductions Fail**:
If you only needed a *single* edge $e^* = (u, v)$ to belong to some MST, you would simply cut all edges with $w_e < w_{e^*}$ so $u$ and $v$ become disconnected (a single Min-Cut). When an **entire spanning tree $T^*$** of $N - 1$ edges is fixed, lowering the weight of a single tree edge $e \in T^*$ simultaneously helps satisfy the MST condition for *every* non-tree edge $f \notin T^*$ whose fundamental cycle contains $e$.

#### Step 2: The Algebraic / Logical Intermediate Representation

By the **Fundamental Cycle Optimality Condition** of matroids and spanning trees, $T^*$ is a Minimum Spanning Tree with respect to $w'$ if and only if for every non-tree edge $f = (u, v) \notin T^*$ and every tree edge $e \in P_{T^*}(f)$ on the unique path between $u$ and $v$ in $T^*$, we have:
$$w'_e \le w'_f.$$
To minimize modification cost, we never increase the weight of a tree edge $e \in T^*$ and never decrease the weight of a non-tree edge $f \notin T^*$. Thus we set:
- $w'_e = w_e - \delta_e$ with $\delta_e \ge 0$ for each tree edge $e \in T^*$,
- $w'_f = w_f + \delta_f$ with $\delta_f \ge 0$ for each non-tree edge $f \notin T^*$.

The optimality condition $w_e - \delta_e \le w_f + \delta_f$ becomes:
$$\delta_e + \delta_f \ge w_e - w_f \quad \forall f \notin T^*, \; \forall e \in P_{T^*}(f).$$
Define $D_{e,f} = \max(0, w_e - w_f)$ as the **excess violation** of the pair $(e, f)$. The **Primal LP** is:
$$\begin{aligned}
\min_{\delta \ge 0} \quad & \sum_{e \in T^*} c_e \delta_e + \sum_{f \notin T^*} c_f \delta_f \\
\text{s.t.} \quad & \delta_e + \delta_f \ge D_{e,f} \quad \forall f \notin T^*, \; \forall e \in P_{T^*}(f).
\end{aligned}$$

#### Step 3: The Reverse-Engineering Scratchpad (Mechanical Graph Compilation)

Observe that the Primal LP is a **weighted bipartite vertex cover / potential problem** where every constraint connects one tree edge $e \in T^*$ and one non-tree edge $f \notin T^*$:

1. Introduce a non-negative dual flow variable $x_{e,f} \ge 0$ for each pair $(e, f)$ with $e \in P_{T^*}(f)$ and $D_{e,f} > 0$.
2. Taking the mechanical LP Dual gives:
   $$\begin{aligned}
   \max_{x \ge 0} \quad & \sum_{f \notin T^*} \sum_{e \in P_{T^*}(f)} D_{e,f} \, x_{e,f} \\
   \text{s.t.} \quad & \sum_{f \notin T^* : e \in P_{T^*}(f)} x_{e,f} \le c_e \quad \forall e \in T^*, \\
   & \sum_{e \in P_{T^*}(f)} x_{e,f} \le c_f \quad \forall f \notin T^*.
   \end{aligned}$$
3. **Graph Compilation**:
   - Construct a **Bipartite Network** with left part $L = T^*$ ($|L| = N - 1$ tree edges) and right part $R = E \setminus T^*$ ($|R| = M - N + 1$ non-tree edges).
   - Add directed edges from Source $S \to e$ with **capacity $c_e$** and **cost $0$** for each $e \in T^*$.
   - Add directed edges from $f \to T$ with **capacity $c_f$** and **cost $0$** for each $f \notin T^*$.
   - For each pair $(e, f)$ with $e \in P_{T^*}(f)$ and $w_e > w_f$, add a directed edge $e \to f$ with **capacity $\infty$** and **cost $-D_{e,f} = -(w_e - w_f)$** (for Min-Cost Flow).
   - In the special case where unit modification costs are uniform ($c_e = c_f = 1$, as in `[SHOI2004] 最小生成树`), the dual is literally **Maximum Weight Bipartite Matching** (solvable in $O(\max(|L|, |R|)^3)$ via the Kuhn–Munkres / Hungarian algorithm), and the primal optimal weight adjustments $(\delta^*_e, \delta^*_f)$ are the **optimal Kuhn–Munkres vertex labels (potentials)**!

#### Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

**Toy Trace ($N = 4$ Diamond Graph, Uniform Cost $c = 1$)**:
Let $V = \{1, 2, 3, 4\}$, $T^* = \{e_1=(1,2), e_2=(2,3), e_3=(3,4)\}$ with weights $w_{e_1} = 10, w_{e_2} = 8, w_{e_3} = 9$.
Non-tree edges: $f_1 = (1,3)$ with $w_{f_1} = 6$ (path $P_{T^*}(f_1) = \{e_1, e_2\}$) and $f_2 = (2,4)$ with $w_{f_2} = 5$ (path $P_{T^*}(f_2) = \{e_2, e_3\}$).
Violations $D_{e,f} = \max(0, w_e - w_f)$:
- For $f_1$: $D_{e_1, f_1} = 10 - 6 = 4$, $D_{e_2, f_1} = 8 - 6 = 2$.
- For $f_2$: $D_{e_2, f_2} = 8 - 5 = 3$, $D_{e_3, f_2} = 9 - 5 = 4$.
In the bipartite graph between $\{e_1, e_2, e_3\}$ and $\{f_1, f_2\}$, the maximum weight matching picks $(e_1, f_1)$ of weight $4$ and $(e_3, f_2)$ of weight $4$, giving total Dual weight $4 + 4 = 8$.
Corresponding Primal potentials: $\delta_{f_1} = 4, \delta_{f_2} = 4, \delta_{e_1} = \delta_{e_2} = \delta_{e_3} = 0$ (increase $f_1$ from $6$ to $10$ and $f_2$ from $5$ to $9$, total cost $4 + 4 = 8$).

**Broken Gadget Counterexample**:
What if the problem also restricts $0 \le \delta_e \le b_e$ (maximum allowed weight reduction per edge)? If you omit the upper bound dual variables on $\delta_e \le b_e$, the Primal LP may assign $\delta_e > b_e$. In the Dual network, an upper bound $\delta_e \le b_e$ adds a direct overflow edge $e \to T$ (or modifies the Dual objective with $-b_e z_e$), ensuring that if no feasible modification exists within $[0, b_e]$, the Dual objective becomes unbounded!

---

### 88.4 Archetype 3: Dualizing Row-Consecutive Interval Covering into Column-Consecutive Flow

In Wave 3B (`[NOI2008] 志愿者招募`), we saw the **Primal Equation-Difference Method**: given interval variables $x_i \ge 0$ covering time steps $t \in [l_i, r_i]$ with demand $\sum_{i: t \in [l_i, r_i]} x_i \ge A_t$, subtracting equation $(t-1)$ from equation $t$ after introducing surplus $y_t \ge 0$ turns each column into one $+1$ at row $l_i$ and one $-1$ at row $r_i + 1$.

Now let us view the exact same problem through **Iteration 88's LP Dual Compiler**:
1. **Primal Covering LP**:
   $$\min_{x \ge 0} \sum_{i=1}^m c_i x_i \quad \text{s.t.} \quad \sum_{i : t \in [l_i, r_i]} x_i \ge A_t \quad (t = 1, \dots, n).$$
2. **Mechanical Dual LP**: Let $p_t \ge 0$ be the dual variable for day $t$:
   $$\max_{p \ge 0} \sum_{t=1}^n A_t p_t \quad \text{s.t.} \quad \sum_{t=l_i}^{r_i} p_t \le c_i \quad (i = 1, \dots, m).$$
3. **Prefix-Sum Potential Substitution in the Dual**:
   Define cumulative dual potentials $\pi_t = \sum_{k=1}^t p_k$ with $\pi_0 = 0$. Since $p_t = \pi_t - \pi_{t-1} \ge 0$ and $\sum_{t=l_i}^{r_i} p_t = \pi_{r_i} - \pi_{l_i - 1} \le c_i$, the Dual LP becomes a **Pure Potential Difference LP**:
   $$\max_{\pi} \sum_{t=1}^n A_t (\pi_t - \pi_{t-1}) \quad \text{s.t.} \quad \pi_{t-1} - \pi_t \le 0, \quad \pi_{r_i} - \pi_{l_i-1} \le c_i.$$
   Dualizing this potential-difference LP back (or recognizing that $\pi_{r_i} - \pi_{l_i-1} \le c_i$ is the dual reduced-cost inequality $c_i + \pi_{l_i-1} - \pi_{r_i} \ge 0$ of a directed edge $l_i - 1 \to r_i$ of cost $c_i$!) shows a profound identity:

> [!NOTE]
> **The Fundamental Duality Identity of Interval Networks**
> **Subtracting consecutive equations ($E_t - E_{t-1}$) in the Primal flow space is algebraically identical to substituting consecutive potential differences ($p_t = \pi_t - \pi_{t-1}$) in the Dual potential space.**

---

## Iteration 89: Complementary Slackness (`互补松弛定理`) & Reconstructing Optimal Dual Potentials/Cuts from Residual Networks

Solving the Dual MCMF network gives the optimal **objective value** (minimum modification cost). However, many competitive programming problems (`[SHOI2004] 最小生成树`, `[WC2007] 剪刀石头布`, market-clearing equilibrium problems, and project crashing schedules) require you to **output the explicit optimal Primal variables $\pi^*_u$ or $\Delta^*_e$**! How do we reconstruct Primal potentials from a Dual flow solver? The answer is **Complementary Slackness (`互补松弛定理`)**.

### 89.1 Primal–Dual LP Formulation of Bounded Min-Cost Circulation

Consider a directed network $G = (V, E)$ where each edge $e = (u, v) \in E$ has capacity $u(e) > 0$, lower bound $0$, and unit cost $c(u, v) \in \mathbb{R}$. The **Bounded Min-Cost Circulation LP** and its **Dual LP** are:

$$\begin{aligned}
\textbf{Circulation Primal (F):} \quad \min_{f} \quad & \sum_{(u,v) \in E} c(u,v) f(u,v) \\
\text{s.t.} \quad & \sum_{v: (v,u) \in E} f(v,u) - \sum_{v: (u,v) \in E} f(u,v) = 0 && \forall u \in V && \text{[potential } \pi(u) \in \mathbb{R}\text{]} \\
& -f(u,v) \ge -u(u,v) && \forall (u,v) \in E && \text{[dual } \gamma(u,v) \ge 0\text{]} \\
& f(u,v) \ge 0.
\end{aligned}$$

Applying our Lagrangian Dual Dictionary from Section 88.1, the **Dual Potential LP (P)** is:
$$\begin{aligned}
\textbf{Potential Dual (P):} \quad \max_{\pi, \gamma} \quad & -\sum_{(u,v) \in E} u(u,v) \gamma(u,v) \\
\text{s.t.} \quad & \pi(v) - \pi(u) - \gamma(u,v) \le c(u,v) && \forall (u,v) \in E \\
& \pi(u) \in \mathbb{R} \text{ free}, \quad \gamma(u,v) \ge 0.
\end{aligned}$$

Define the **reduced cost (`归约费用`)** of directed edge $(u, v)$ with respect to potential $\pi : V \to \mathbb{R}$ as:
$$c_\pi(u, v) := c(u, v) + \pi(u) - \pi(v).$$
Then the dual constraint $\pi(v) - \pi(u) - \gamma(u,v) \le c(u,v)$ rearranges to:
$$\gamma(u, v) \ge -c_\pi(u, v).$$
Since $\gamma(u, v) \ge 0$ has a negative coefficient $-u(u, v) < 0$ in the Dual maximization objective, for any fixed $\pi$ the optimal choice of $\gamma(u, v)$ is:
$$\gamma^*(u, v) = \max\big(0, \, -c_\pi(u, v)\big).$$

---

### 89.2 Rigorous Proof of the Network Complementary Slackness Theorem

**Theorem 89.1 (Network Complementary Slackness & Residual Optimality Theorem)**.
Let $f^*$ be a feasible circulation in $G = (V, E)$ ($0 \le f^*(e) \le u(e)$ and flow conservation holds at every $v \in V$), and let $\pi^* : V \to \mathbb{R}$ be a vertex potential function with $\gamma^*(u, v) = \max(0, -c_{\pi^*}(u, v))$. Then the following four statements are equivalent:

1. **(Joint Primal–Dual Optimality)** $f^*$ is a minimum-cost circulation and $(\pi^*, \gamma^*)$ is an optimal dual solution, with strong duality $\sum_{e \in E} c(e) f^*(e) = -\sum_{e \in E} u(e) \gamma^*(e)$.
2. **(Complementary Slackness on Edges)** For every edge $e = (u, v) \in E$:
   $$\begin{aligned}
   f^*(u, v) > 0 &\implies c_{\pi^*}(u, v) = c(u, v) + \pi^*(u) - \pi^*(v) \le 0, \\
   f^*(u, v) < u(u, v) &\implies c_{\pi^*}(u, v) = c(u, v) + \pi^*(u) - \pi^*(v) \ge 0.
   \end{aligned}$$
   In particular, if an edge is **strictly partially saturated** ($0 < f^*(u, v) < u(u, v)$), its reduced cost must be **identically zero**: $c_{\pi^*}(u, v) = 0$.
3. **(Non-Negative Residual Reduced Costs)** In the residual network $G_{f^*}$, every residual edge $e_{\text{res}} = (x, y) \in E(G_{f^*})$ (with residual capacity $u_{f^*}(x, y) > 0$) has non-negative reduced cost:
   $$c_{\pi^*}(x, y) = c_{\text{res}}(x, y) + \pi^*(x) - \pi^*(y) \ge 0.$$
4. **(No Negative-Cost Residual Cycles)** The residual network $G_{f^*}$ contains no directed cycle of strictly negative total cost.

#### Complete Algebraic Proof

**$(1) \Longleftrightarrow (2)$ via the Duality Gap Decomposition**:
Because $f^*$ satisfies flow conservation $\sum_{v} f^*(v, u) - \sum_{v} f^*(u, v) = 0$ at every vertex $u \in V$, the sum of $\big(\pi^*(u) - \pi^*(v)\big) f^*(u, v)$ over all edges telescopes to zero:
$$\sum_{(u,v) \in E} c(u,v) f^*(u,v) = \sum_{(u,v) \in E} \big(c(u,v) + \pi^*(u) - \pi^*(v)\big) f^*(u,v) = \sum_{(u,v) \in E} c_{\pi^*}(u,v) f^*(u,v).$$
Now compute the **Primal–Dual Duality Gap** $\text{Gap}(f^*, \pi^*)$:
$$\begin{aligned}
\text{Gap}(f^*, \pi^*) &= \sum_{e \in E} c(e) f^*(e) - \left(-\sum_{e \in E} u(e) \gamma^*(e)\right) \\
&= \sum_{e \in E} \Big[ c_{\pi^*}(e) f^*(e) + u(e) \gamma^*(e) \Big] \\
&= \sum_{e \in E} \Big[ \big(c_{\pi^*}(e) + \gamma^*(e)\big) f^*(e) + \big(u(e) - f^*(e)\big) \gamma^*(e) \Big].
\end{aligned}$$
By feasibility, $f^*(e) \ge 0$, $u(e) - f^*(e) \ge 0$, $\gamma^*(e) \ge 0$, and $c_{\pi^*}(e) + \gamma^*(e) \ge 0$. Thus every edge contributes two non-negative products to $\text{Gap}(f^*, \pi^*)$!
Therefore, $\text{Gap}(f^*, \pi^*) = 0$ if and only if for every edge $e = (u, v) \in E$, both products vanish:
- **First product vanishes**: $f^*(e) > 0 \implies c_{\pi^*}(e) + \gamma^*(e) = 0 \implies c_{\pi^*}(e) = -\gamma^*(e) \le 0$.
- **Second product vanishes**: $f^*(e) < u(e) \implies \gamma^*(e) = 0 \implies c_{\pi^*}(e) \ge -\gamma^*(e) = 0$.
This proves $(1) \Longleftrightarrow (2)$.

**$(2) \Longleftrightarrow (3)$ via Residual Edge Anatomy**:
Recall that $E(G_{f^*})$ consists of two types of residual edges:
- **Forward residual edges** $(u, v)$ whenever $f^*(u, v) < u(u, v)$, with cost $c_{\text{res}}(u, v) = c(u, v)$. Condition (2) states $f^*(u, v) < u(u, v) \implies c_{\pi^*}(u, v) \ge 0$.
- **Backward residual edges** $(v, u)$ whenever $f^*(u, v) > 0$, with cost $c_{\text{res}}(v, u) = -c(u, v)$. Its reduced cost is $c_{\pi^*}(v, u) = -c(u, v) + \pi^*(v) - \pi^*(u) = -c_{\pi^*}(u, v)$. Condition (2) states $f^*(u, v) > 0 \implies c_{\pi^*}(u, v) \le 0 \Longleftrightarrow c_{\pi^*}(v, u) \ge 0$.
Thus (2) and (3) are identical.

**$(3) \Longleftrightarrow (4)$ via Shortest-Path Potentials on $G_{f^*}$**:
If (3) holds, then around any directed cycle $C$ in $G_{f^*}$, $\sum_{e \in C} c_{\text{res}}(e) = \sum_{e \in C} c_{\pi^*}(e) \ge 0$, so (4) holds. Conversely, if $G_{f^*}$ has no negative-cost directed cycle, attach a virtual super-source $s_0$ with zero-cost directed edges $(s_0, v)$ of residual capacity $\infty$ to every $v \in V$. Then shortest-path distances $d(v) = \text{dist}_{G_{f^*}}(s_0, v)$ are well-defined and finite, and satisfy the triangle inequality:
$$d(y) \le d(x) + c_{\text{res}}(x, y) \quad \forall (x, y) \in E(G_{f^*}).$$
Setting $\pi^*(v) = d(v)$ gives $c_{\pi^*}(x, y) = c_{\text{res}}(x, y) + d(x) - d(y) \ge 0$ for every residual edge $(x, y) \in E(G_{f^*})$, proving (3). $\blacksquare$

#### Special Case: Max-Flow / Min-Cut Complementary Slackness

Cast $s$-$t$ Max-Flow as a Min-Cost Circulation by giving all original edges cost $0$ and adding a return edge $(t \to s)$ of capacity $\infty$ and cost $-1$. An optimal dual potential assigns $\pi^*(v) = 1$ for $v \in S$ and $\pi^*(v) = 0$ for $v \in T = V \setminus S$ (an $s$-$t$ cut $(S, T)$). Complementary Slackness immediately yields the two golden rules of **Min-Cut Reconstruction**:
1. Every forward cut edge $e = (u, v) \in \delta^+(S)$ has $c_{\pi^*}(u, v) = 0 + 1 - 0 = +1 > 0$? Wait: with $\pi^*(s) = 0, \pi^*(t) = 1$ (so the return edge $t \to s$ of cost $-1$ has reduced cost $-1 + 1 - 0 = 0$), any forward edge $u \to v$ from $S$ ($\pi^*=0$) to $T$ ($\pi^*=1$) has $c_{\pi^*}(u, v) = 0 + 0 - 1 = -1 < 0$, which by Condition (2) forces **$f^*(u, v) = u(u, v)$ (every forward cut edge is completely saturated)**!
2. Any backward edge $v \to u$ from $T$ ($\pi^*=1$) to $S$ ($\pi^*=0$) has $c_{\pi^*}(v, u) = 0 + 1 - 0 = +1 > 0$, which by Condition (2) forces **$f^*(v, u) = 0$ (every backward cut edge is completely empty)**!

---

### 89.3 The Residual Potential Recovery Algorithm (Constructing Explicit $\pi^*(v)$ and $\Delta^*(e)$)

Suppose you solved a Primal potential/modification problem by compiling its Dual into a Min-Cost Circulation / MCMF network, and now the judge asks you to print the explicit Primal variables $\pi^*(v)$ and $\Delta^*(e)$.

#### Algorithmic Contract: Exact Potential & Perturbation Recovery

1. **Solve Dual MCMF**: Run your Min-Cost Circulation / SSP solver to obtain the optimal flow $f^*$ and the final residual graph $G_{f^*}$ (keeping only edges with residual capacity $u_{f^*}(x, y) > 0$).
2. **Compute Residual Shortest-Path Potentials**:
   - If your SSP solver maintained Johnson potentials $\pi(v)$ across all augmentations and no negative edges remain among unsaturated edges, $\pi^*(v) = \pi(v)$ is already valid for the $s$-$t$ reachable subgraph.
   - In general (especially for circulations or when vertices may be unreachable from $s$), run Bellman–Ford / SPFA on $G_{f^*}$ initialized with $\text{dist}[v] = 0$ for all $v \in V$ (equivalent to adding a super-source $s_0$ with $0$-cost edges to all vertices) and relax along all residual edges $(x, y) \in E(G_{f^*})$:
     $$\text{dist}[y] \gets \min\big(\text{dist}[y], \; \text{dist}[x] + c_{\text{res}}(x, y)\big).$$
   - Set the canonical network potential:
     $$\pi^*(v) := \text{dist}[v] \quad \forall v \in V.$$
   - **Sign Convention Check**: Because $\text{dist}[y] \le \text{dist}[x] + c_{\text{res}}(x, y)$, this $\pi^*$ satisfies:
     $$\pi^*(y) - \pi^*(x) \le c_{\text{res}}(x, y) \quad \forall (x, y) \in E(G_{f^*}).$$
3. **Map Back to Problem Primal Variables**:
   - If your Primal LP constraint was written as $\text{ PrPot}(v) - \text{PrPot}(u) \le c(u, v)$ (minimization dualized to circulation), set $\text{PrPot}^*(v) = \pi^*(v) - \pi^*(s)$.
   - If your Primal LP constraint was written as $\text{PrPot}(v) - \text{PrPot}(u) + \Delta_{uv} \ge d_{uv}$ (as in Project Crashing where we negated durations to $c(u, v) = -d_{uv}$), then on the first parallel edge $(u, v)$ with $c(u, v) = -d_{uv}$, $\pi^*(v) - \pi^*(u) \le -d_{uv} + \gamma^*(u, v)$ gives:
     $$t^*(v) := -\pi^*(v) + \pi^*(s), \qquad \Delta^*_{uv} := \max\big(0, \; d_{uv} - (t^*(v) - t^*(u))\big) = \gamma^*(u, v).$$
   - For **Bipartite Inverse MST** (`[SHOI2004] 最小生成树`) where $e \in T^*$ and $f \notin T^*$ are linked by edge $e \to f$ of cost $-D_{e,f}$:
     In $G_{f^*}$, every residual edge goes from $e \to f$ with cost $-D_{e,f}$ (if unsaturated) or $f \to e$ with cost $+D_{e,f}$ (if $x^*_{e,f} > 0$), plus $S \to e$ (cost $0$ if $x^*(S, e) < c_e$, or $e \to S$ cost $0$ if $x^*(S, e) > 0$) and $f \to T$ (cost $0$ if $x^*(f, T) < c_f$, or $T \to f$ cost $0$ if $x^*(f, T) > 0$).
     Fixing $\pi^*(S) = \pi^*(T) = 0$ (since $T \to S$ has cost $0$ in max-weight matching where we stop when shortest path cost $\ge 0$), the residual inequalities $\pi^*(y) - \pi^*(x) \le c_{\text{res}}(x, y)$ give:
     $$\delta^*_e := -\pi^*(e) \ge 0 \quad (e \in T^*), \qquad \delta^*_f := +\pi^*(f) \ge 0 \quad (f \notin T^*),$$
     which automatically satisfy $\delta^*_e + \delta^*_f = \pi^*(f) - \pi^*(e) \ge D_{e,f}$ for every $(e, f)$!

#### Hand-Checkable Numerical Trace of Potential Recovery

Return to our Project Crashing toy example from Section 88.2 ($V = \{1, 2, 3\}$, $T = 4$, $e_1=(1,2)$ with $d_1=3, c_1=5$, $e_2=(2,3)$ with $d_2=3, c_2=2$, $e_3=(1,3)$ with $d_3=5, c_3=4$).
At the optimal circulation $f^*$:
- $f^*_{e_1, 1} = 2 < c_1 = 5$. Since $0 < f^*_{e_1, 1} < 5$, both forward edge $(1 \to 2)$ of cost $-3$ and backward edge $(2 \to 1)$ of cost $+3$ exist in $G_{f^*}$! Complementary Slackness forces:
  $$\pi^*(2) - \pi^*(1) = -3.$$
- $f^*_{e_2, 1} = 2 = c_2$ (saturated), and $f^*_{e_2, 2} = 0 < \infty$ (second parallel edge has cost $-(d_2 - b_2) = -1$). Thus in $G_{f^*}$ we have backward edge $(3 \to 2)$ of cost $+3$ and forward edge $(2 \to 3)$ of cost $-1$:
  $$-3 \le \pi^*(3) - \pi^*(2) \le -1.$$
- Return edge $(3 \to 1)$ has flow $F^* = 6 > 0$ and capacity $\infty$, so both $(3 \to 1)$ of cost $+4$ and $(1 \to 3)$ of cost $-4$ exist in $G_{f^*}$! This forces:
  $$\pi^*(1) - \pi^*(3) = 4 \quad \Longleftrightarrow \quad \pi^*(3) - \pi^*(1) = -4.$$
Combining $\pi^*(2) - \pi^*(1) = -3$ and $\pi^*(3) - \pi^*(1) = -4$ with $\pi^*(1) = 0$ gives:
$$\pi^*(1) = 0, \quad \pi^*(2) = -3, \quad \pi^*(3) = -4.$$
Converting to timestamps $t^*(v) = -\pi^*(v)$:
$$t^*(1) = 0, \quad t^*(2) = 3, \quad t^*(3) = 4,$$
and the optimal crashing amounts are immediately recovered as $\Delta^*_e = \max(0, d_e - (t^*(v) - t^*(u)))$:
$$\Delta^*_1 = \max(0, 3 - 3) = 0, \quad \Delta^*_2 = \max(0, 3 - 1) = 2, \quad \Delta^*_3 = \max(0, 5 - 4) = 1.$$
Every single primal timestamp and edge crash is recovered with zero guesswork!

---

## Iteration 90: Totally Unimodular (TU) Matrices, Hoffman–Kruskal Theorem, Ghouila–Houri Bicoloring & Consecutive-Ones Matrices (`连续 1 性质`)

Why does an Integer Linear Program (ILP) such as Bipartite Matching, Interval Covering (`[NOI2008] 志愿者招募`), or Ancestor-to-Descendant Tree Path Covering have **zero integrality gap**—meaning its continuous Linear Programming relaxation automatically finds an exact integer optimum—while a tiny change in the problem statement (such as allowing general undirected tree paths or odd cycles) introduces fractional $1/2$-optima and NP-hardness? The mathematical boundary is governed by **Total Unimodularity (`全幺模矩阵`)**.

### 90.1 Definition & Closure Properties of Totally Unimodular (TU) Matrices

**Definition 90.1 (Totally Unimodular Matrix)**.
A matrix $A \in \mathbb{R}^{m \times n}$ is **Totally Unimodular (TU)** if every square submatrix $B$ of $A$ (obtained by selecting any $k$ rows and any $k$ columns of $A$, for any $1 \le k \le \min(m, n)$) has determinant
$$\det(B) \in \{-1, 0, +1\}.$$
In particular, taking $1 \times 1$ submatrices shows that every entry of a TU matrix must belong to $\{-1, 0, +1\}$.

**Lemma 90.1 (Fundamental Closure Operations Preserving Total Unimodularity)**.
If $A \in \{-1, 0, +1\}^{m \times n}$ is Totally Unimodular, then every matrix obtained from $A$ by any sequence of the following seven operations is also Totally Unimodular:
1. **Transposition**: $A \gets A^\top$ (since $\det(B^\top) = \det(B)$).
2. **Row or Column Sign Flip**: Multiplying any row or column of $A$ by $-1$ (flips the sign of $\det(B)$).
3. **Row or Column Permutation**: Swapping any two rows or columns of $A$.
4. **Row or Column Deletion / Duplication**: Deleting a row/column, or duplicating an existing row/column (any square submatrix containing two identical rows/columns has $\det = 0$).
5. **Appending a Standard Basis Vector / Identity Matrix**: Appending a unit row/column $e_i$, so $\begin{bmatrix} A & I_m \end{bmatrix}$ and $\begin{bmatrix} A \\ I_n \end{bmatrix}$ are TU (expanding any submatrix determinant along the unit column reduces to a $(k-1) \times (k-1)$ submatrix of $A$).
6. **Gaussian Pivot on a $\pm 1$ Entry**: Pivoting on a non-zero entry $A_{r,c} \in \{-1, +1\}$ (Schur complement preserves subdeterminants up to sign).

---

### 90.2 The Hoffman–Kruskal Theorem (1956) — Complete Proof

**Theorem 90.1 (Hoffman–Kruskal Polyhedral Integrality Theorem, 1956)**.
Let $A \in \mathbb{Z}^{m \times n}$ be an integral matrix. The following two statements are equivalent:
1. $A$ is **Totally Unimodular**.
2. For **every** quartet of integral bound vectors $a, b \in (\mathbb{Z} \cup \{\pm\infty\})^m$ and $l, u \in (\mathbb{Z} \cup \{\pm\infty\})^n$, every extreme point (vertex) of the polyhedron
   $$P(a, b, l, u) := \big\{ x \in \mathbb{R}^n : a \le A x \le b, \; l \le x \le u \big\}$$
   is an **integer vector** $x^* \in \mathbb{Z}^n$.

#### Complete Proof

**$(1) \implies (2)$ (Cramer's Rule on Active Basis Subsystems)**:
Assume $A$ is TU, and let $x^* \in \mathbb{R}^n$ be an extreme point (vertex) of $P(a, b, l, u)$. By Lemma 90.1(5), the stacked constraint matrix $M = \begin{bmatrix} A \\ I_n \end{bmatrix} \in \{-1, 0, +1\}^{(m+n) \times n}$ is also Totally Unimodular, and $P(a, b, l, u) = \{x \in \mathbb{R}^n : \tilde{a} \le M x \le \tilde{b}\}$ where $\tilde{a} = (a, l)$ and $\tilde{b} = (b, u)$ are integral.
By polyhedral theory, $x^*$ is a vertex of $P(a, b, l, u)$ if and only if there exist $n$ linearly independent rows of $M$—forming an invertible $n \times n$ submatrix $B$ of $M$—whose corresponding inequalities hold with tight equality at $x^*$:
$$B x^* = d,$$
where each component $d_i \in \mathbb{Z}$ is the corresponding tight lower or upper bound from $\tilde{a}$ or $\tilde{b}$.
Since $B$ is a nonsingular $n \times n$ submatrix of the TU matrix $M$, we have $\det(B) \neq 0$ and $\det(B) \in \{-1, 0, +1\}$, which forces $\det(B) = \pm 1$. By **Cramer's Rule**, for each coordinate $j \in \{1, \dots, n\}$:
$$x^*_j = \frac{\det(B_j(d))}{\det(B)} = \pm \det(B_j(d)),$$
where $B_j(d)$ is obtained from $B$ by replacing column $j$ with the integer vector $d \in \mathbb{Z}^n$. Since both $B$ and $d$ have exclusively integer entries, $\det(B_j(d)) \in \mathbb{Z}$, so $x^*_j \in \mathbb{Z}$ for all $j$.

**$(2) \implies (1)$ (Veinott–Dantzig Constructive Fractional Vertex Proof)**:
Suppose conversely that every polyhedron $P(a, b, l, u)$ with integral bounds has integral vertices, and let $B$ be any nonsingular $k \times k$ square submatrix of $A$. By appending $I_m$ and setting $a = b$ on the rows of $B$, $l = u = 0$ on the $n - k$ columns outside $B$, and $l = -\infty, u = +\infty$ on the $k$ columns of $B$, any integral right-hand side $d \in \mathbb{Z}^k$ defines a zero-dimensional polyhedron whose unique vertex $x^*_B = B^{-1} d$ must be integral!
Thus $B^{-1} d \in \mathbb{Z}^k$ for *every* $d \in \mathbb{Z}^k$. Choosing $d = e_1, e_2, \dots, e_k$ (the standard basis vectors of $\mathbb{Z}^k$) proves that every column of $B^{-1}$ is integral, so $B^{-1} \in \mathbb{Z}^{k \times k}$.
Consequently, both $\det(B)$ and $\det(B^{-1})$ are integers satisfying $\det(B) \cdot \det(B^{-1}) = \det(I_k) = 1$, which forces $\det(B) \in \{-1, +1\}$. Hence $A$ is Totally Unimodular. $\blacksquare$

---

### 90.3 Ghouila–Houri's Equitable Bicoloring Characterization (1962)

Checking $\det(B) \in \{-1, 0, +1\}$ directly for all $\sum_k \binom{m}{k}\binom{n}{k}$ square submatrices is exponential. How do we prove in $30$ seconds of paper-and-pencil work that a matrix $A$ is TU? We use **Ghouila–Houri's Equitable Bicoloring Theorem**.

**Theorem 90.2 (Ghouila–Houri Theorem, 1962)**.
A matrix $A \in \{-1, 0, +1\}^{m \times n}$ is **Totally Unimodular** if and only if for **every** subset of rows $R \subseteq \{1, \dots, m\}$ (or symmetrically, every subset of columns $C \subseteq \{1, \dots, n\}$), there exists a sign assignment (bicoloring) $\sigma : R \to \{-1, +1\}$ such that the weighted row sum in every column belongs to $\{-1, 0, +1\}$:
$$\sum_{i \in R} \sigma(i) A_{i, j} \in \{-1, 0, +1\} \quad \forall j \in \{1, \dots, n\}.$$
Equivalently, every subset $R$ of rows can be partitioned into two parts $R = R^+ \sqcup R^-$ such that in every column $j$, the sum of entries in $R^+$ and the sum of entries in $R^-$ differ by at most $1$.

#### Complete Proof

**$(\implies)$ Necessary Condition**:
Suppose $A$ is TU and let $R \subseteq \{1, \dots, m\}$ be any subset of rows. Let $\mathbf{1}_R \in \{0, 1\}^m$ be the indicator row vector of $R$, and consider the vector $s = \mathbf{1}_R^\top A \in \mathbb{Z}^n$ whose $j$-th entry is $s_j = \sum_{i \in R} A_{i, j}$. Define the non-empty bounded polyhedron:
$$Q := \left\{ z \in \mathbb{R}^m \;:\; 0 \le z_i \le 1 \;\; (\forall i \in R), \quad z_i = 0 \;\; (\forall i \notin R), \quad \left\lfloor \frac{s_j}{2} \right\rfloor \le (z^\top A)_j \le \left\lceil \frac{s_j}{2} \right\rceil \;\; (\forall j \in \{1, \dots, n\}) \right\}.$$
Notice that $z = \frac{1}{2} \mathbf{1}_R \in Q$ because $(z^\top A)_j = \frac{s_j}{2} \in \big[\lfloor s_j / 2 \rfloor, \lceil s_j / 2 \rceil\big]$. Thus $Q \neq \emptyset$.
Since $A^\top$ is TU and all bounds $\lfloor s_j/2 \rfloor, \lceil s_j/2 \rceil, 0, 1$ are integers, the **Hoffman–Kruskal Theorem** guarantees that $Q$ has an **integral vertex** $z^* \in \{0, 1\}^m$!
Define $\sigma(i) = 2 z^*_i - 1 \in \{-1, +1\}$ for each $i \in R$. Then for every column $j$:
$$\sum_{i \in R} \sigma(i) A_{i, j} = 2 (z^{*\top} A)_j - s_j \in \Big[ 2\left\lfloor \frac{s_j}{2} \right\rfloor - s_j, \; 2\left\lceil \frac{s_j}{2} \right\rceil - s_j \Big] \subseteq \{-1, 0, +1\}.$$

**$(\Longleftarrow)$ Sufficient Condition (Induction on Submatrix Size $k$)**:
Assume the equitable bicoloring property holds for all $R \subseteq \{1, \dots, m\}$ (and hence holds for every submatrix of $A$). We prove by induction on $k$ that every $k \times k$ submatrix $B$ of $A$ has $\det(B) \in \{-1, 0, +1\}$.
The base case $k = 1$ holds because taking $R = \{i\}$ forces $A_{i, j} \in \{-1, 0, +1\}$.
For the inductive step, let $B$ be a nonsingular $k \times k$ submatrix of $A$ whose $(k-1) \times (k-1)$ minors all lie in $\{-1, 0, +1\}$, and let $d = |\det(B)| \ge 1$. We must show $d = 1$.
By Cramer's rule and the inductive hypothesis on $(k-1) \times (k-1)$ cofactors, the adjugate matrix $B^* = d \cdot B^{-1}$ has entries strictly in $\{-1, 0, +1\}$. Let $u^\top$ be the first row of $B^*$, so:
$$u^\top B = d \cdot e_1^\top = (d, 0, 0, \dots, 0), \quad \text{with } u_i \in \{-1, 0, +1\}.$$
Let $R = \{i \in \{1, \dots, k\} : u_i \neq 0\} = \{i : u_i \equiv 1 \pmod 2\}$ be the non-empty support of $u$. Modulo $2$, $u_i \equiv 1 \pmod 2$ for $i \in R$, so for every column $j \ge 2$:
$$\sum_{i \in R} B_{i, j} \equiv \sum_{i=1}^k u_i B_{i, j} = (u^\top B)_j = 0 \pmod 2.$$
Apply Ghouila–Houri to $R$ to obtain signs $\sigma : R \to \{-1, +1\}$ such that $w_j := \sum_{i \in R} \sigma(i) B_{i, j} \in \{-1, 0, +1\}$ for all $j \in \{1, \dots, k\}$. Since $\sigma(i) \equiv 1 \pmod 2$, we have $w_j \equiv \sum_{i \in R} B_{i, j} \pmod 2$:
- For every $j \in \{2, \dots, k\}$, $w_j$ is an **even integer** in $\{-1, 0, +1\}$, which forces $w_j = 0$!
- If $d$ were even, then $(u^\top B)_1 = d \equiv 0 \pmod 2$ would also force $w_1 = 0$, meaning $\sum_{i \in R} \sigma(i) B_{i, \cdot} = 0^\top$, contradicting that the rows of $B$ are linearly independent!
- Thus $d$ is odd and $w_1 \in \{-1, +1\}$. Replacing $\sigma$ with $-\sigma$ if needed, we get $\sigma^\top B = e_1^\top = \frac{1}{d} u^\top B$. Since $B$ is invertible, $\sigma_i = \frac{u_i}{d}$ for all $i \in R$. Since $\sigma_i, u_i \in \{-1, +1\}$ and $R \neq \emptyset$, we conclude $d = 1$! $\blacksquare$

#### Immediate Corollaries via Ghouila–Houri

1. **Directed Graph Incidence Matrices**: Each column $e = (u \to v)$ has one $-1$ at row $u$ and one $+1$ at row $v$. For any row subset $R \subseteq V$, simply choose **uniform signs** $\sigma(i) = +1$ for all $i \in R$! Then $\sum_{i \in R} A_{i, e} \in \{-1, 0, +1\}$ automatically.
2. **Bipartite Undirected Incidence Matrices**: Each column $e = \{u, v\}$ with $u \in L, v \in R_{\text{bip}}$ has two $+1$s (at row $u$ and row $v$). For any subset of vertices $S \subseteq L \sqcup R_{\text{bip}}$, assign $\sigma(u) = +1$ for $u \in S \cap L$ and $\sigma(v) = -1$ for $v \in S \cap R_{\text{bip}}$! Then every column sum is in $\{-1, 0, +1\}$. (By contrast, an odd cycle $C_{2k+1}$ has determinant $\pm 2$, violating Ghouila–Houri on $R = V(C_{2k+1})$).

---

### 90.4 The Consecutive-Ones Property (`连续 1 性质`) & The Upper-Bidiagonal Difference Matrix $D$

**Definition 90.2 (Consecutive-Ones Matrix)**.
A $0$-$1$ matrix $A \in \{0, 1\}^{m \times n}$ has the:
- **Column-Consecutive-Ones Property** if in every column $j \in \{1, \dots, n\}$, the entries equal to $1$ appear in a single contiguous block of rows $[a_j, b_j] = \{a_j, a_j + 1, \dots, b_j\}$.
- **Row-Consecutive-Ones Property** if in every row $i \in \{1, \dots, m\}$, the entries equal to $1$ appear in a single contiguous block of columns $[l_i, r_i] = \{l_i, l_i + 1, \dots, r_i\}$.

**Theorem 90.3 (Difference Matrix Compilation of Consecutive-Ones Matrices)**.
Every Column-Consecutive-Ones matrix $A \in \{0, 1\}^{m \times n}$ and every Row-Consecutive-Ones matrix $B \in \{0, 1\}^{m \times n}$ is **Totally Unimodular**, and any LP or ILP over them compiles directly into a **Min-Cost Circulation / Network Flow** problem via the **Upper-Bidiagonal Difference Matrix $D$**.

#### Proof & Exact Algebraic Compilation

1. **Case 1: Column-Consecutive-Ones Matrix $A$ (Direct Primal Equation-Difference Compilation)**:
   Define the $(m+1) \times m$ **Equation-Difference Matrix** $D$:
   $$D = \begin{bmatrix}
   1 & 0 & 0 & \cdots & 0 \\
   -1 & 1 & 0 & \cdots & 0 \\
   0 & -1 & 1 & \cdots & 0 \\
   \vdots & \vdots & \ddots & \ddots & \vdots \\
   0 & 0 & \cdots & -1 & 1 \\
   0 & 0 & \cdots & 0 & -1
   \end{bmatrix} \in \{-1, 0, +1\}^{(m+1) \times m}.$$
   Notice that the top $m \times m$ block of $D$ is lower-triangular with $1$s on the main diagonal, so it is unimodular ($\det = 1$) with inverse $L_{i,k} = \mathbf{1}_{i \ge k}$.
   Now multiply $D$ on the left of a Column-Consecutive-Ones matrix $A$ whose $j$-th column is the indicator vector of the contiguous row interval $[a_j, b_j]$:
   $$(D A)_{i, j} = A_{i, j} - A_{i-1, j} = \begin{cases}
   +1 & \text{if } i = a_j, \\
   -1 & \text{if } i = b_j + 1, \\
   0 & \text{otherwise}
   \end{cases} \qquad (\text{where } A_{0, j} = A_{m+1, j} := 0).$$
   Every column $j$ of $D A$ has **exactly one $+1$** (at row $a_j$) and **exactly one $-1$** (at row $b_j + 1$)!
   Therefore:
   - $D A$ is the **node-arc incidence matrix of a directed graph** on $m + 1$ vertices $\{1, 2, \dots, m + 1\}$, where column $j$ is a directed edge $a_j \to (b_j + 1)$!
   - For any equality system $A x + s = b$ (after adding slack/surplus variables $s_i$ which are unit vectors $e_i$, also interval-consecutive of length $1$!), multiplying on the left by $D$ gives the exact Kirchhoff flow conservation system:
     $$(D A) x + (D I_m) s = D b,$$
     where $s_i$ becomes a step edge $i \to (i+1)$ and $(Db)_i = b_i - b_{i-1}$ is the net supply/demand at vertex $i$!
   - Furthermore, Ghouila–Houri holds immediately for $A$: for any subset of rows $R = \{i_1 < i_2 < \dots < i_k\}$, simply assign alternating signs $\sigma(i_r) = (-1)^{r-1}$ ($+1, -1, +1, -1, \dots$)! Since every column $j$ intersects $R$ in a contiguous subsequence of indices, the alternating sum of $+1$s and $-1$s over a contiguous subsequence is always in $\{0, +1\}$ (if it starts with $+1$) or $\{-1, 0\}$ (if it starts with $-1$). Thus $A$ is TU!

2. **Case 2: Row-Consecutive-Ones Matrix $B$ (Transpose Invariance & Dual Compilation)**:
   Suppose $B \in \{0, 1\}^{m \times n}$ has the **Row-Consecutive-Ones Property** (each row $i$ is an interval $[l_i, r_i]$ of columns, e.g., $x_j$ are point variables and each constraint $i$ bounds the sum over interval $[l_i, r_i]$).
   Notice a crucial trap: **$B$ does NOT necessarily have the Column-Consecutive-Ones Property!** For example:
   $$B = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}$$
   is Row-Consecutive-Ones, but columns $1$ and $3$ have $1$s at rows $1$ and $3$ with a $0$ at row $2$! So you *cannot* blindly multiply $B$ on the left by $D$.
   Instead, by Lemma 90.1(1), **Total Unimodularity is invariant under transposition**: since $B$ is Row-Consecutive-Ones, its transpose $A = B^\top$ is **Column-Consecutive-Ones**, so $B$ is guaranteed to be TU!
   How do we compile an LP over a Row-Consecutive-Ones matrix $B$ into a flow network? We have **two clean methods**:
   - **Method A (Prefix-Sum Variable Substitution)**: Substitute $x_j = S_j - S_{j-1}$ with $S_0 = 0$. Then every row sum $\sum_{j=l_i}^{r_i} x_j = S_{r_i} - S_{l_i-1}$ becomes a pure **Potential Difference** constraint, which compiles to MCMF via Iteration 88!
   - **Method B (Mechanical LP Dualization)**: Take the LP Dual of the primal problem over $B$. The dual constraint matrix is $B^\top$, which **is** Column-Consecutive-Ones, and then multiply the Dual by $D$!

---

### 90.5 Tree-Path Incidence Matrices & Network Matrices (`树路径关联矩阵与网络矩阵`)

Intervals $[l, r]$ on a line are just paths on a **path graph** $1 - 2 - \dots - n$. What happens when we generalize from paths on a line to **paths on a tree $T = (V, E_T)$**? Here lies one of the sharpest, most instructive boundaries in combinatorial optimization.

#### Step 1: The Non-Graph / Tree Diagnostic Signal

You are given a tree $T = (V, E_T)$ of $N$ vertices and a family of $M$ tree paths $\mathcal{P} = \{P_1, \dots, P_M\}$, each with weight/cost $c_j$. You want to pack or cover vertices/edges of $T$ using paths from $\mathcal{P}$ (e.g., select paths so each vertex $v$ or tree edge $e$ is covered at least/at most $b_v$ times at minimum cost).
**Crucial Question**: When is the Tree-Path Incidence Matrix $M$ Totally Unimodular (and thus compilable to MCMF), and when does it fail?

#### Step 2: The Algebraic / Polyhedral Distinction — Vertical vs. Undirected Paths

Root the tree $T$ arbitrarily at a vertex $r \in V$.
- A path $P_j$ is called **vertical (monotone ancestor-to-descendant)** if one endpoint $u_j$ is an ancestor of the other endpoint $v_j$ in the rooted tree $T$.
- A path $P_j$ is **general (undirected / V-shaped)** if it goes up from $v_j$ to $\text{LCA}(u_j, v_j)$ and then down to $u_j$.

**Theorem 90.4 (Tutte Network Matrix Theorem & Vertical Tree-Path TU Theorem)**.
1. **(Edge-Path Incidence of Directed/Vertical Tree Paths)**: For *any* orientation of the edges of a tree $T$ and any directed non-tree arc $f = (u \to v)$, define the signed incidence matrix $N_{e, f} \in \{-1, 0, +1\}$ where $N_{e, f} = +1$ if the unique $u \to v$ path in $T$ traverses $e$ forward, $-1$ if backward, and $0$ if $e \notin P_T(u, v)$. Such a matrix $N$ is called a **Network Matrix** and is **always Totally Unimodular**.
   In particular, if $T$ is rooted at $r$ with all tree edges oriented toward the root ($v \to \text{parent}(v)$), and every path $P_j$ goes from a descendant $v_j$ up to an ancestor $u_j$, then the $0$-$1$ **Edge-Path Incidence Matrix** (and the **Vertex-Path Incidence Matrix**) of vertical paths is a Network Matrix and is **Totally Unimodular**!
2. **(Failure of General Undirected Tree Paths)**: The $0$-$1$ Edge-Path (or Vertex-Path) Incidence Matrix of **general undirected paths on a tree** is **NOT** Totally Unimodular, even on a 4-vertex star graph $K_{1,3}$!

#### Step 3: Reverse-Engineering Scratchpad (Tree Parent-Child Equation Difference)

How do we mechanically compile a covering/packing system over **vertical (ancestor-to-descendant) tree paths** into a flow network?
Suppose each vertical path $P_j$ covers all vertices on the tree path from ancestor $u_j$ down to descendant $v_j$, and each vertex $v \in V$ has an equation (after adding slack/surplus $s_v \ge 0$):
$$E_v : \quad \sum_{j : v \in P_j} x_j \pm s_v = b_v.$$
Generalizing the 1D Equation-Difference operator $E_t - E_{t-1}$, we define the **Rooted Tree Parent-Child Difference Operator**: for every vertex $v \in V \cup \{0\}$ (where $0 := \text{parent}(r)$ is a virtual super-root with $E_0 : 0 = 0$), replace equation $E_v$ by:
$$E'_v := E_v - \sum_{w \in \text{child}(v)} E_w.$$
Let us inspect the coefficient of each vertical path variable $x_j$ (covering the chain $u_j = w_0 \to w_1 \to \dots \to w_k = v_j$) in $E'_v$:
- At $v = v_j$ (the bottom endpoint of $P_j$), $v_j \in P_j$ has $+1$ in $E_{v_j}$, and **none of the children of $v_j$ belong to $P_j$**! Thus $x_j$ has coefficient **$+1$ at $E'_{v_j}$**.
- At every intermediate vertex $w_r$ ($0 \le r < k$), both $w_r \in P_j$ and its unique child $w_{r+1} \in P_j$, so $+1 - 1 = 0$ cancels completely!
- At $v = \text{parent}(u_j)$ (the parent of the top endpoint of $P_j$), $\text{parent}(u_j) \notin P_j$ ($0$), while its child $u_j \in P_j$ ($-1$). Thus $x_j$ has coefficient **$-1$ at $E'_{\text{parent}(u_j)}$**!
- At every other vertex, $x_j$ has coefficient $0$.
- Meanwhile, each slack variable $s_v$ appears with $\pm 1$ in $E'_v$ and $\mp 1$ in $E'_{\text{parent}(v)}$.

**Exact Compiled Flow Graph**:
Every vertical path $P_j = (u_j \text{ down to } v_j)$ compiles into a single directed edge:
$$v_j \longrightarrow \text{parent}(u_j) \quad \text{with flow } x_j \text{ and cost } c_j,$$
and every vertex slack $s_v$ compiles into a tree edge between $v$ and $\text{parent}(v)$!

```
Rooted Tree Vertical Path P_j (from ancestor u_j down to descendant v_j):
       [ parent(u_j) ]  <--- (-1 in E'_{parent(u_j)})
             |
          [ u_j ]       <--- (+1 - 1 = 0 cancels!)
             |
            ...
             |
          [ v_j ]       <--- (+1 in E'_{v_j}, no child in P_j)
       /           \
  [child 1]     [child 2]

Compiled Flow Edge for x_j:   v_j  ------------------>  parent(u_j)   (cost c_j)
```

#### Step 4: Broken Gadget Counterexample — The Star Graph $K_{1,3}$ Determinant $\pm 2$ Failure

What happens if a path $P_j$ is **not vertical**, i.e., it goes up from $a_j$ to $l = \text{LCA}(a_j, b_j)$ and then down to $b_j$?
In the tree difference operator $E'_v = E_v - \sum_{w \in \text{child}(v)} E_w$:
- $x_j$ gets $+1$ at $a_j$ and $+1$ at $b_j$ (two $+1$s!),
- At $l = \text{LCA}(a_j, b_j)$, $l \in P_j$ ($+1$) and **two** of $l$'s children belong to $P_j$ ($-2$), so $x_j$ gets $1 - 2 = -1$ at $E'_l$,
- And at $\text{parent}(l)$, $x_j$ gets $-1$ at $E'_{\text{parent}(l)}$ (two $-1$s!).
Having **two $+1$s and two $-1$s** in a column breaks the directed graph incidence property!

Let us verify on the smallest possible counterexample that this is not merely a limitation of our difference operator, but a fundamental failure of Total Unimodularity:
Consider the **Star Graph $K_{1,3}$** with center $0$ and three leaves $1, 2, 3$, and tree edges $e_1 = (0,1), e_2 = (0,2), e_3 = (0,3)$. Take the three undirected leaf-to-leaf paths $P_{12} = \{e_1, e_2\}$, $P_{23} = \{e_2, e_3\}$, and $P_{31} = \{e_3, e_1\}$. The $3 \times 3$ Edge-Path Incidence Matrix is:
$$B_{K_{1,3}} = \begin{array}{c|ccc}
 & P_{12} & P_{23} & P_{31} \\ \hline
e_1 & 1 & 0 & 1 \\
e_2 & 1 & 1 & 0 \\
e_3 & 0 & 1 & 1
\end{array} \quad \implies \quad \det(B_{K_{1,3}}) = 1(1 - 0) - 0 + 1(1 - 0) = +2 \notin \{-1, 0, +1\}!$$
If each tree edge $e_1, e_2, e_3$ has capacity $1$ and we want to maximize the number of packed paths $\max (x_{12} + x_{23} + x_{31})$ subject to $B_{K_{1,3}} x \le \mathbf{1}$:
- The **LP Relaxation (and Continuous Multi-Commodity Flow)** sets $x_{12} = x_{23} = x_{31} = \frac{1}{2}$, achieving objective $\frac{3}{2} = 1.5$.
- The **True Integer Optimum** can select at most **1 path** (since any two paths share at least one star edge), achieving objective $1 \neq 1.5$!

---

## Iteration 91: Submodular Function Minimization (SFM), Polymatroids & The Lovász Extension

In Waves 2A and 2B, we saw that binary pairwise energies $\sum c_{uv} x_u (1 - x_v)$ can be represented as an $s$-$t$ Min-Cut whenever each $2 \times 2$ interaction table satisfies $A + D \le B + C$. Why is that condition called **submodularity**, how does it generalize to arbitrary set functions $f : 2^V \to \mathbb{R}$ and continuous convex functions via the **Lovász Extension**, and why does **Edmonds' Greedy Algorithm** solve optimization over polymatroids in $O(N \log N)$ time?

### 91.1 Submodular Set Functions: Equivalent Definitions & Cut Submodularity Proofs

**Definition 91.1 (Submodular Set Function)**.
Let $V$ be a finite ground set of size $n = |V|$. A set function $f : 2^V \to \mathbb{R}$ is **submodular (`次模函数`)** if for every pair of subsets $A, B \subseteq V$:
$$f(A) + f(B) \ge f(A \cup B) + f(A \cap B).$$
A function $g : 2^V \to \mathbb{R}$ is **supermodular (`超模函数`)** if $-g$ is submodular ($g(A) + g(B) \le g(A \cup B) + g(A \cap B)$), and **modular (`模函数`)** if the inequality holds with equality for all $A, B \subseteq V$ (i.e., $f(S) = f(\emptyset) + \sum_{v \in S} w_v$).

**Theorem 91.1 (Equivalence of Lattice Submodularity & Diminishing Marginal Returns)**.
For any set function $f : 2^V \to \mathbb{R}$, define the discrete marginal derivative $\Delta_f(v \mid S) := f(S \cup \{v\}) - f(S)$. The following three conditions are equivalent:
1. **(Lattice Inequality)** $f(A) + f(B) \ge f(A \cup B) + f(A \cap B)$ for all $A, B \subseteq V$.
2. **(Diminishing Marginal Returns on Arbitrary Subsets)** For all $S \subseteq T \subseteq V$ and $v \in V \setminus T$:
   $$\Delta_f(v \mid S) \ge \Delta_f(v \mid T).$$
3. **(Local Pairwise Second-Difference Inequality)** For all $S \subseteq V$ and distinct $u, v \in V \setminus S$:
   $$f(S \cup \{u\}) + f(S \cup \{v\}) \ge f(S \cup \{u, v\}) + f(S).$$

#### Proof
- $(1) \implies (3)$: Set $A = S \cup \{u\}$ and $B = S \cup \{v\}$; then $A \cup B = S \cup \{u, v\}$ and $A \cap B = S$.
- $(3) \implies (2)$: Write $T \setminus S = \{u_1, \dots, u_k\}$ and telescope $\Delta_f(v \mid S \cup \{u_1, \dots, u_{r-1}\}) \ge \Delta_f(v \mid S \cup \{u_1, \dots, u_r\})$ for $r = 1, \dots, k$.
- $(2) \implies (1)$: Write $A \setminus B = \{a_1, \dots, a_m\}$ and telescope:
  $$f(A) - f(A \cap B) = \sum_{r=1}^m \Delta_f\big(a_r \;\big|\; (A \cap B) \cup \{a_1, \dots, a_{r-1}\}\big) \ge \sum_{r=1}^m \Delta_f\big(a_r \;\big|\; B \cup \{a_1, \dots, a_{r-1}\}\big) = f(A \cup B) - f(B). \quad \blacksquare$$

**Lemma 91.1 (Cut Capacity Submodularity via Double Counting)**.
In any directed graph $G = (V, E)$ with non-negative edge capacities $c : E \to \mathbb{R}_{\ge 0}$, the directed cut capacity function $f(S) := c(\delta^+(S)) = \sum_{(u, v) \in E : u \in S, v \notin S} c(u, v)$ is **submodular**.
*Proof*: Since a positive linear combination of submodular functions is submodular, it suffices to check a single directed edge $e = (u \to v)$ of capacity $1$, for which $f_e(S) = \mathbf{1}_{u \in S, v \notin S}$. For any $A, B \subseteq V$:
- The right-hand side $f_e(A \cup B) + f_e(A \cap B)$ can equal $2$ only if $u \in A \cap B$ and $v \notin A \cup B$, in which case $u \in A, v \notin A$ and $u \in B, v \notin B$, so the left-hand side $f_e(A) + f_e(B)$ also equals $2$.
- The right-hand side equals $1$ only if either ($u \in A \cup B$ and $v \notin A \cup B$) or ($u \in A \cap B$ and $v \notin A \cap B$); in both cases at least one of $A$ or $B$ contains $u$ and excludes $v$, so $f_e(A) + f_e(B) \ge 1$.
Wait—even better: notice that $f_e(A) + f_e(B) - f_e(A \cup B) - f_e(A \cap B)$ equals $+1$ precisely when $(u \in A \setminus B \text{ and } v \in B \setminus A)$ or $(u \in B \setminus A \text{ and } v \in A \setminus B)$ (edges crossing between $A \setminus B$ and $B \setminus A$), and $0$ otherwise! Thus for any graph $G$:
$$c(\delta^+(A)) + c(\delta^+(B)) = c(\delta^+(A \cup B)) + c(\delta^+(A \cap B)) + c(A \setminus B, B \setminus A) + c(B \setminus A, A \setminus B) \ge c(\delta^+(A \cup B)) + c(\delta^+(A \cap B)). \quad \blacksquare$$

---

### 91.2 Submodular Polyhedra $P(f)$, Base Polyhedra $B(f)$ & Edmonds' Greedy Algorithm (1970)

Given any submodular function $f : 2^V \to \mathbb{R}$ normalized so that $f(\emptyset) = 0$, Jack Edmonds (1970) introduced two fundamental polyhedra:

1. **The Submodular Polyhedron**:
   $$P(f) := \left\{ x \in \mathbb{R}^V \;:\; x(S) := \sum_{v \in S} x_v \le f(S) \quad \forall S \subseteq V \right\}.$$
2. **The Base Polyhedron**:
   $$B(f) := \big\{ x \in P(f) \;:\; x(V) = f(V) \big\}.$$
   (When $f$ is also monotone non-decreasing, $P_+(f) = P(f) \cap \mathbb{R}_{\ge 0}^V$ is called a **Polymatroid**.)

Although $B(f)$ is defined by $2^n$ linear inequalities, **maximizing any linear objective $w^\top x$ over $B(f)$ takes only $O(n \log n)$ time via sorting**!

**Theorem 91.2 (Edmonds' Greedy Algorithm for Base Polyhedra, 1970)**.
Let $f : 2^V \to \mathbb{R}$ be submodular with $f(\emptyset) = 0$, and let $w \in \mathbb{R}^V$ be any weight vector. Sort the elements of $V$ in non-increasing order of weight:
$$w_{\sigma(1)} \ge w_{\sigma(2)} \ge \dots \ge w_{\sigma(n)},$$
and define the nested chain of prefixes $S_k := \{\sigma(1), \sigma(2), \dots, \sigma(k)\}$ with $S_0 := \emptyset$. Then the **marginal greedy vector** $x^\sigma \in \mathbb{R}^V$ defined by
$$x^\sigma_{\sigma(k)} := f(S_k) - f(S_{k-1}) \quad (k = 1, \dots, n)$$
is an **extreme point of $B(f)$** and is an **optimal solution** to the linear program $\max_{x \in B(f)} w^\top x$. Conversely, if a set function $f$ with $f(\emptyset) = 0$ has the property that $x^\sigma \in P(f)$ for every permutation $\sigma$, then $f$ is submodular!

#### Complete Proof via Dual Uncrossing (`LP 对偶交叉去重法`)

1. **Primal Feasibility ($x^\sigma \in B(f)$)**:
   By telescoping, $x^\sigma(V) = \sum_{k=1}^n \big(f(S_k) - f(S_{k-1})\big) = f(S_n) - f(S_0) = f(V)$.
   To prove $x^\sigma(A) \le f(A)$ for every $A \subseteq V$, write $A = \{\sigma(i_1), \dots, \sigma(i_m)\}$ with $i_1 < i_2 < \dots < i_m$. Since $\{ \sigma(i_1), \dots, \sigma(i_{r-1}) \} \subseteq S_{i_r - 1}$, Diminishing Marginal Returns (Theorem 91.1(2)) gives:
   $$x^\sigma_{\sigma(i_r)} = \Delta_f\big(\sigma(i_r) \;\big|\; S_{i_r - 1}\big) \le \Delta_f\big(\sigma(i_r) \;\big|\; \{\sigma(i_1), \dots, \sigma(i_{r-1})\}\big).$$
   Summing over $r = 1, \dots, m$ telescopes the right-hand side to $f(A) - f(\emptyset) = f(A)$, proving $x^\sigma(A) \le f(A)$.

2. **Dual Optimality via Uncrossing**:
   The Dual LP of $\max \{ w^\top x : x(S) \le f(S) \; (\forall S \subset V), \; x(V) = f(V) \}$ introduces dual variables $y_S \ge 0$ for $\emptyset \neq S \subset V$ and a free variable $y_V \in \mathbb{R}$:
   $$\min_{y} \sum_{S \subseteq V} y_S f(S) \quad \text{s.t.} \quad \sum_{S \subseteq V : v \in S} y_S = w_v \quad \forall v \in V.$$
   Set the **Chain Dual Solution** $y^\sigma$:
   $$y^\sigma_{S_k} := w_{\sigma(k)} - w_{\sigma(k+1)} \ge 0 \quad (k = 1, \dots, n-1), \qquad y^\sigma_{S_n} := w_{\sigma(n)} \in \mathbb{R},$$
   and $y^\sigma_S := 0$ for all $S \notin \{S_1, \dots, S_n\}$.
   For each element $\sigma(j)$, the sets in the chain containing $\sigma(j)$ are precisely $S_j, S_{j+1}, \dots, S_n$, whose dual variables telescope to:
   $$\sum_{k=j}^n y^\sigma_{S_k} = \sum_{k=j}^{n-1} (w_{\sigma(k)} - w_{\sigma(k+1)}) + w_{\sigma(n)} = w_{\sigma(j)}.$$
   Thus $y^\sigma$ is dual feasible! Furthermore, by Abel summation (summation by parts), its dual objective equals the primal objective of $x^\sigma$:
   $$\sum_{k=1}^n y^\sigma_{S_k} f(S_k) = \sum_{k=1}^{n-1} (w_{\sigma(k)} - w_{\sigma(k+1)}) f(S_k) + w_{\sigma(n)} f(S_n) = \sum_{k=1}^n w_{\sigma(k)} \big(f(S_k) - f(S_{k-1})\big) = w^\top x^\sigma.$$
   By Strong LP Duality, $x^\sigma$ is optimal! $\blacksquare$

---

### 91.3 The Lovász Extension $\hat{f}(x)$ & Level-Set Coarea Equivalence

How do we pass between discrete binary set optimization $\min_{S \subseteq V} f(S)$ and continuous convex optimization $\min_{x \in [0, 1]^V} \hat{f}(x)$? László Lovász (1983) discovered that Edmonds' greedy value $\max_{z \in B(f)} z^\top x$, viewed as a function of the weight vector $x \in \mathbb{R}^V$, defines the exact canonical continuous extension of $f$.

**Definition 91.2 (The Lovász Extension)**.
For any set function $f : 2^V \to \mathbb{R}$ with $f(\emptyset) = 0$, its **Lovász Extension** $\hat{f} : \mathbb{R}^V \to \mathbb{R}$ is defined for any $x \in \mathbb{R}^V$ by sorting its coordinates $x_{\sigma(1)} \ge x_{\sigma(2)} \ge \dots \ge x_{\sigma(n)}$ and setting:
$$\hat{f}(x) := \sum_{k=1}^{n-1} \big(x_{\sigma(k)} - x_{\sigma(k+1)}\big) f(S_k) + x_{\sigma(n)} f(V) = \sum_{k=1}^n x_{\sigma(k)} \big(f(S_k) - f(S_{k-1})\big),$$
where $S_k = \{\sigma(1), \dots, \sigma(k)\}$. Equivalently, for any $x \in [a, b]^V$, $\hat{f}(x)$ is given by the **Coarea (Layer-Cake) Level-Set Integral**:
$$\hat{f}(x) = a f(V) + \int_a^b f\big(\{v \in V : x_v \ge \lambda\}\big) \, d\lambda.$$

**Theorem 91.3 (Lovász Convexity & Exact Relaxation Theorem, 1983)**.
Let $f : 2^V \to \mathbb{R}$ satisfy $f(\emptyset) = 0$.
1. **(Extension & Positive Homogeneity)** For every subset $S \subseteq V$, $\hat{f}(\mathbf{1}_S) = f(S)$, and $\hat{f}(\alpha x) = \alpha \hat{f}(x)$ for all $\alpha \ge 0$.
2. **(Convexity $\Longleftrightarrow$ Submodularity)** The Lovász extension $\hat{f} : \mathbb{R}^V \to \mathbb{R}$ is a **convex function** on $\mathbb{R}^V$ if and only if $f$ is **submodular**.
3. **(Zero Integrality Gap on $[0, 1]^V$)** For any set function $f$, minimizing $f(S)$ over discrete subsets $S \subseteq V$ is equivalent to minimizing its Lovász extension $\hat{f}(x)$ over the continuous hypercube $[0, 1]^V$:
   $$\min_{S \subseteq V} f(S) = \min_{x \in [0, 1]^V} \hat{f}(x),$$
   and for any $x \in [0, 1]^V$, at least one super-level set $S_\lambda = \{v \in V : x_v \ge \lambda\}$ satisfies $f(S_\lambda) \le \hat{f}(x)$.

#### Proof of Theorem 91.3
1. For $x = \mathbf{1}_S$, sorting puts the $|S|$ ones first ($x_{\sigma(1)} = \dots = x_{\sigma(|S|)} = 1$) and the zeros last ($x_{\sigma(|S|+1)} = \dots = 0$), so only the term $k = |S|$ with $x_{\sigma(|S|)} - x_{\sigma(|S|+1)} = 1$ survives, giving $\hat{f}(\mathbf{1}_S) = f(S_{|S|}) = f(S)$.
2. **$f$ submodular $\implies \hat{f}$ convex**: By Edmonds' Greedy Theorem (Theorem 91.2), when $f$ is submodular,
   $$\hat{f}(x) = \max_{z \in B(f)} z^\top x \quad \forall x \in \mathbb{R}^V.$$
   Since $\hat{f}(x)$ is the pointwise supremum of a family of linear functions $\{x \mapsto z^\top x\}_{z \in B(f)}$, $\hat{f}$ is automatically convex!
   **$\hat{f}$ convex $\implies f$ submodular**: For any $A, B \subseteq V$, notice that $\mathbf{1}_A + \mathbf{1}_B = \mathbf{1}_{A \cup B} + \mathbf{1}_{A \cap B}$. Notice also that $A \cap B \subseteq A \cup B$, so the sorted order of $\mathbf{1}_{A \cup B} + \mathbf{1}_{A \cap B}$ puts $A \cap B$ first (value $2$), then $(A \cup B) \setminus (A \cap B)$ (value $1$), then $V \setminus (A \cup B)$ (value $0$). By the definition of the Lovász extension on a nested chain, $\hat{f}(\mathbf{1}_{A \cup B} + \mathbf{1}_{A \cap B}) = (2 - 1) f(A \cap B) + (1 - 0) f(A \cup B) = f(A \cup B) + f(A \cap B)$. By convexity and positive homogeneity of $\hat{f}$:
   $$f(A) + f(B) = \hat{f}(\mathbf{1}_A) + \hat{f}(\mathbf{1}_B) \ge \hat{f}(\mathbf{1}_A + \mathbf{1}_B) = \hat{f}(\mathbf{1}_{A \cup B} + \mathbf{1}_{A \cap B}) = f(A \cup B) + f(A \cap B).$$
3. For any $x \in [0, 1]^V$, $f(\emptyset) = 0$ and the Coarea formula gives $\hat{f}(x) = \int_0^1 f(\{v : x_v \ge \lambda\}) \, d\lambda \ge \min_{\lambda \in [0, 1]} f(S_\lambda) \ge \min_{S \subseteq V} f(S)$. Conversely, restricting $x \in \{0, 1\}^V$ gives $\min_{x \in [0, 1]^V} \hat{f}(x) \le \min_{S \subseteq V} f(S)$. $\blacksquare$

#### The Competitive Programming Compiler: Why Total Variation & Isotonic Regression Decouple into Threshold Cuts

Let us see what the Lovász Extension of standard graph cut functions looks like:
1. **Undirected Cut Function**: Let $f(S) = \sum_{\{u, v\} \in E} w_{uv} |\mathbf{1}_{u \in S} - \mathbf{1}_{v \in S}|$. For any vector $x \in \mathbb{R}^V$, what is its Lovász extension $\hat{f}(x)$?
   By the Coarea integral:
   $$\hat{f}(x) = \sum_{\{u, v\} \in E} w_{uv} \int_{-\infty}^{\infty} \big| \mathbf{1}_{x_u \ge \lambda} - \mathbf{1}_{x_v \ge \lambda} \big| \, d\lambda = \sum_{\{u, v\} \in E} w_{uv} |x_u - x_v|!$$
   **The $\ell_1$ Total Variation penalty $\sum w_{uv} |x_u - x_v|$ is literally the Lovász Extension of the Undirected Graph Cut function!**
2. **Directed Cut Function**: Let $f(S) = \sum_{(u, v) \in E} w_{uv} \max(0, \mathbf{1}_{u \in S} - \mathbf{1}_{v \in S}) = c(\delta^+(S))$. Its Lovász extension is:
   $$\hat{f}(x) = \sum_{(u, v) \in E} w_{uv} \max(0, x_u - x_v)!$$
   In particular, taking $w_{uv} = +\infty$ enforces the hard **Isotonic Partial Order Constraint** $x_u \le x_v$ (`[省选联考 2020] 保序回归`)!
3. **Separable Unary Costs**: For any unary function $\sum_{v \in V} g_v(x_v)$ on integer or real values $x_v \in [L, R]$, writing $g_v(x_v) = g_v(L) + \int_L^R g'_v(\lambda) \, \mathbf{1}_{x_v > \lambda} \, d\lambda$ decomposes the entire problem:
   $$\min_{x \in [L, R]^V} \left( \sum_{v \in V} g_v(x_v) + \sum_{(u, v) \in E} w_{uv} \max(0, x_u - x_v) \right) = \sum_{v \in V} g_v(L) + \int_L^R \min_{S_\lambda \subseteq V} \left( \sum_{v \in S_\lambda} g'_v(\lambda) + c(\delta^+(S_\lambda)) \right) d\lambda.$$
   When each $g_v$ is **convex**, its marginal derivative $g'_v(\lambda)$ is **monotone non-decreasing** in $\lambda$. By Submodularity and Topkis's Monotonicity Theorem, the optimal binary threshold cuts $S^*_\lambda = \{v : x^*_v > \lambda\}$ automatically satisfy the **Nesting Invariant** $S^*_{\lambda_1} \supseteq S^*_{\lambda_2}$ for $\lambda_1 < \lambda_2$! Thus solving the binary Min-Cut at each threshold $\lambda$ (either explicitly across $O(N)$ distinct values as in `CF 1427G`, or via Parallel Binary Search `整体二分` in $O(\log U)$ layers as in `[省选联考 2020] 保序回归`) reconstructs the exact global continuous/integer optimum $x^*_v$!

---

## Iteration 92: The Boundary Between Network Flow, Matroid Intersection & NP-Hardness

One of the highest-value skills for an ICPC World Finals or Div1 Grandmaster contestant is knowing **instantly** whether a combinatorial constraint system can be compiled into a **Network Flow** graph, requires **Polynomial Matroid Intersection**, or crosses the cliff into **NP-Hardness** (forcing $2^K$ parameterized enumeration + Flow/Matroid Intersection, as in `CF 1556H — DIY Tree`).

### 92.1 The Structural Hierarchy of Combinatorial Optimization

Every subset selection problem $\max_{I \subseteq E} w(I)$ subject to independence constraints falls into one of four polyhedral regimes:

| Regime | Mathematical Structure | Polyhedral Property | Exact Algorithmic Engine |
| :--- | :--- | :--- | :--- |
| **Level 1: Single Matroid** | $I \in \mathcal{I}_1$ (e.g., Spanning Tree, Linear Basis, Single Laminar Family) | Base Polyhedron $B(r_1)$ has integral vertices; greedy chain is optimal | **Kruskal / Edmonds Greedy** in $O(\|E\| \log \|E\|)$ |
| **Level 2: Two Partition or Laminar Matroids** | $I \in \mathcal{I}_1 \cap \mathcal{I}_2$ where $\mathcal{M}_1, \mathcal{M}_2$ are Partition or Laminar Matroids | Stacked constraint matrix $\begin{bmatrix} A_1 \\ A_2 \end{bmatrix}$ is **Totally Unimodular (TU)** | **Standard Network Flow / MCMF** (`Hasse Out-Tree` $\to E \to$ `Hasse In-Tree`) |
| **Level 3: Two General Matroids** | $I \in \mathcal{I}_1 \cap \mathcal{I}_2$ (e.g., Graphic $\cap$ Partition, Graphic $\cap$ Cographic, Linear $\cap$ Partition) | Constraint matrix is **not** TU, but $P(r_1) \cap P(r_2)$ is **Totally Dual Integral (TDI)** | **Edmonds' Matroid Intersection** (Shortest Augmenting Paths in Exchange Graph) |
| **Level 4: Three Matroids / 2-Commodity Flow** | $I \in \mathcal{I}_1 \cap \mathcal{I}_2 \cap \mathcal{I}_3$ (e.g., 3D Matching, Directed Hamiltonian Path, Degree-$\le 2$ MST) | Polytope has **fractional vertices** (e.g., $x = \frac{1}{2} \mathbf{1}$); **Non-Zero Integrality Gap** | **NP-Hard** (requires $O(2^K)$ FPT branching, color-coding, or algebraic matroid parity) |

---

### 92.2 Why Two Laminar Matroids Compile to Network Flow (The In-Tree + Out-Tree Construction)

#### Step 1: The Non-Graph Diagnostic Signal (Recognition)

You must select a subset of elements $x_e \in \{0, 1\}$ (or bounded integers $x_e \in [0, c_e]$) for $e \in E$ to maximize/minimize $\sum_{e \in E} w_e x_e$, subject to **two families of subset capacity bounds**:
- Family 1 ($\mathcal{L}_1$): For each $A \in \mathcal{L}_1$, $l_A \le \sum_{e \in A} x_e \le u_A$.
- Family 2 ($\mathcal{L}_2$): For each $B \in \mathcal{L}_2$, $l'_B \le \sum_{e \in B} x_e \le u'_B$.
Crucially, within each family $\mathcal{L}_k$ ($k \in \{1, 2\}$), **no two sets partially overlap**: for any $X, Y \in \mathcal{L}_k$, either $X \subseteq Y$, $Y \subseteq X$, or $X \cap Y = \emptyset$. Such a family is called a **Laminar Family (`层状族`)**.
*(Common disguises of Laminar Families: Partition matroids where sets are disjoint; Prefix/Suffix nested chains; Subtrees of two different rooted trees $T_1$ and $T_2$ on the same leaf set $E$, as in `CF 1067E` / Dual-Tree Subtree Demand problems; Row/Column hierarchical groups in `CF 704D — Captain America`.)*

#### Step 2: The Algebraic / Polyhedral Intermediate Representation

Because $\mathcal{L}_1$ is laminar, its inclusion Hasse diagram is a **rooted forest $F_1$** (by adding $E$ at the top if not present, a single **rooted tree $T_1$**). Every element $e \in E$ belongs to a unique minimal set $A_{\min}(e) \in \mathcal{L}_1$, and the sets in $\mathcal{L}_1$ containing $e$ are precisely the **ancestors of $A_{\min}(e)$ in $T_1$**!
Symmetrically, $\mathcal{L}_2$ forms a rooted tree $T_2$, and the sets in $\mathcal{L}_2$ containing $e$ are the **ancestors of $B_{\min}(e)$ in $T_2$**.

Why is the combined constraint matrix $\begin{bmatrix} M(\mathcal{L}_1) \\ M(\mathcal{L}_2) \end{bmatrix}$ Totally Unimodular?
Apply the **Rooted Tree Parent-Child Difference Operator** from Section 90.5 independently to $T_1$ and $T_2$, and negate all rows of $T_2$:
- In $T_1$'s differenced rows, each variable $x_e$ has a single **$+1$** at row $A_{\min}(e)$ (and $-1$ at the super-root of $T_1$).
- In $T_2$'s negated differenced rows, each variable $x_e$ has a single **$-1$** at row $B_{\min}(e)$ (and $+1$ at the super-root of $T_2$).
Every column has one $+1$ and one $-1$!

#### Step 3: The Reverse-Engineering Scratchpad (Hasse Out-Tree + In-Tree Graph Compilation)

We can read off the flow network directly without even performing row reductions:
1. **Left Laminar Tree $T_1$ (Hasse Out-Tree from Source $S$)**:
   - Create a vertex for each set $A \in \mathcal{L}_1$. Connect Source $S \to \text{root}(T_1)$ with capacity $[l_E, u_E]$.
   - For every parent-child pair $(P, C)$ in $T_1$, add a directed edge $P \to C$ with lower bound $l_C$, upper bound $u_C$, and cost $0$.
2. **Right Laminar Tree $T_2$ (Hasse In-Tree into Sink $T$)**:
   - Create a vertex for each set $B \in \mathcal{L}_2$. Connect $\text{root}(T_2) \to T$ with capacity $[l'_E, u'_E]$.
   - For every parent-child pair $(P', C')$ in $T_2$, add a directed edge $C' \to P'$ (from child to parent!) with lower bound $l'_{C'}$, upper bound $u'_{C'}$, and cost $0$.
3. **Ground Element Bridges ($E$)**:
   - For each element $e \in E$, add a directed edge from its minimal set in $\mathcal{L}_1$ to its minimal set in $\mathcal{L}_2$:
     $$A_{\min}(e) \longrightarrow B_{\min}(e) \quad \text{with capacity } [0, c_e] \text{ and cost } w_e.$$

```
Source S ---> [Root A_0] ---> [Child A_1] ---> [Leaf A_min(e)]
                                                      |
                                                      |  e in E (cap [0, c_e], cost w_e)
                                                      v
  Sink T <--- [Root B_0] <--- [Child B_1] <--- [Leaf B_min(e)]
```

**Flow Conservation Invariant**:
Because $T_1$ is an out-tree and $T_2$ is an in-tree, any flow $x_e$ crossing the bridge edge $A_{\min}(e) \to B_{\min}(e)$ is forced by flow conservation to pass through **every ancestor $A \supseteq A_{\min}(e)$ in $T_1$** on its way from $S$, and through **every ancestor $B \supseteq B_{\min}(e)$ in $T_2$** on its way to $T$! Therefore, the total flow on tree edge $\text{parent}(A) \to A$ is literally $\sum_{e \in A} x_e$, and the total flow on tree edge $B \to \text{parent}(B)$ is literally $\sum_{e \in B} x_e$.

---

### 92.3 The "Three Entities" Paradox: NP-Hard 3D Matching vs. Polynomial Middle-Vertex Split (`[USACO07OPEN] Dining G`)

A classic point of confusion in competitive programming arises when a problem involves **three classes of objects**, say Foods $F$, Cows $C$, and Drinks $D$, and we want to form valid triples $(f, c, d) \in F \times C \times D$ such that each food, cow, and drink is used at most once. Why is `[USACO07OPEN] Dining G` solvable in polynomial time by Dinic's algorithm, whereas **3-Dimensional Matching (3DM)** is one of Karp's 21 NP-Complete problems?

#### The Exact Structural Criterion: Star Factored Compatibility vs. Coupled Hyperedges

1. **Factored Star Compatibility (`[USACO07OPEN] Dining G` — Polynomial via Middle-Vertex Split)**:
   Suppose a triple $(f, c, d)$ is valid if and only if $f \in F_c$ (cow $c$ likes food $f$) **and** $d \in D_c$ (cow $c$ likes drink $d$). Notice that **food $f$ and drink $d$ do not interact directly**: cow $c$ is the central hub of a 3-vertex star $f - c - d$.
   - **Algebraic Flow Model**: For each cow $c \in C$, we need:
     $$\sum_{f \in F_c} x_{f, c} = y_c = \sum_{d \in D_c} z_{c, d}, \quad y_c \in \{0, 1\},$$
     subject to $\sum_{c} x_{f,c} \le 1$ and $\sum_{c} z_{c,d} \le 1$.
   - **Graph Compilation (The Middle-Vertex Split Rule)**:
     Put the **hub entity $C$ in the middle**! Split each cow $c \in C$ into $c_{\text{in}} \to c_{\text{out}}$ with capacity $1$, put $F$ on the left ($S \to f \to c_{\text{in}}$), and put $D$ on the right ($c_{\text{out}} \to d \to T$):
     $$S \xrightarrow{1} f \xrightarrow{1} c_{\text{in}} \xrightarrow{1} c_{\text{out}} \xrightarrow{1} d \xrightarrow{1} T.$$
     Because any food $f \in F_c$ can be paired with *any* drink $d \in D_c$ once it passes through $c_{\text{in}} \to c_{\text{out}}$, the network is $100\%$ exact!

2. **Coupled Triangle / Hyperedge Compatibility (3D Matching — NP-Hard)**:
   Now suppose cow $c_1$ only drinks *coffee* ($d_1$) if she eats *bagels* ($f_1$), and only drinks *tea* ($d_2$) if she eats *cereal* ($f_2$). That is, the valid triples are $H = \{(f_1, c_1, d_1), (f_2, c_1, d_2), \dots\}$.

#### Step 4: Broken Gadget Counterexample — The Cross-Routing (Chimera Triple) Bug

What happens if a contestant tries to solve coupled 3D Matching $H \subseteq F \times C \times D$ using a flow network?
- **Attempt 1 (Merging at $c_{1,\text{in}} \to c_{1,\text{out}}$)**:
  If you add edges $f_1 \to c_{1,\text{in}}$, $f_2 \to c_{1,\text{in}}$ and $c_{1,\text{out}} \to d_1$, $c_{1,\text{out}} \to d_2$, then a unit of flow can travel along the path:
  $$S \to f_1 \to c_{1,\text{in}} \to c_{1,\text{out}} \to d_2 \to T,$$
  fabricating the **chimera triple** $(f_1, c_1, d_2) \notin H$!
- **Attempt 2 (Creating Separate Mid-Nodes per Triple)**:
  If you create separate gadget nodes for $t_1 = (f_1, c_1, d_1)$ and $t_2 = (f_2, c_1, d_2)$ to prevent $f_1$ from cross-routing to $d_2$, how do you enforce that cow $c_1$ is used at most once ($x_{t_1} + x_{t_2} \le 1$) while *also* enforcing that $f$ and $d$ are used at most once? A single flow particle has only **one entry (head)** and **one exit (tail)**—it can enforce capacity at most once on entry ($F$), once in the middle ($C$), and once on exit ($D$). It **cannot** simultaneously remember its origin $f_1$ while passing through a shared bottleneck $c_{1,\text{in}} \to c_{1,\text{out}}$!
- **Polyhedral Proof of Failure**: Take $3$ foods, $3$ cows, $3$ drinks, and $4$ triples sharing pairs so that the incidence matrix contains the $3 \times 3$ odd-cycle submatrix $\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{bmatrix}$ of determinant $+2$. No unimodular transformation can ever turn it into a network matrix.

---

### 92.4 Graphic / Linear Matroid $\cap$ Partition Matroid (`CF 1556H — DIY Tree`, `CF 1284G — Seollal`)

When does a graph problem cross from **Level 2 (Network Flow)** to **Level 3 (General Matroid Intersection)**?

#### Diagnostic Signal for Matroid Intersection
Look for the simultaneous presence of:
1. **A Global Acyclicity / Connectivity / Spanning Forest Constraint** ($\mathcal{M}_1 =$ Graphic Matroid on $G = (V, E)$, where $I \subseteq E$ is independent iff $(V, I)$ contains no cycle) or **Linear / XOR Independence** ($\mathcal{M}_1 =$ Linear Matroid over $\mathbb{F}_2$ or $\mathbb{F}_p$), **AND**
2. **A Color Budget / Degree Bound on an Independent Set of Vertices** ($\mathcal{M}_2 =$ Partition Matroid, where edges are partitioned into disjoint color classes $E = E_1 \sqcup \dots \sqcup E_k$ and at most $d_i$ edges can be chosen from $E_i$).

> [!WARNING]
> **Why Degree Bounds on ALL Vertices Are NP-Hard, While Degree Bounds on an Independent Set $K \subseteq V$ Are a Single Partition Matroid!**
> Each edge $e = (u, v)$ has **two** endpoints. If we impose degree bounds $\deg_T(v) \le d_v$ on *all* vertices $v \in V$:
> - On a bipartite graph $V = L \sqcup R$, the degree bounds split into **two** partition matroids ($\mathcal{M}_L$ for left endpoints and $\mathcal{M}_R$ for right endpoints). Together with the Graphic Matroid $\mathcal{M}_{\text{graphic}}$, that is **THREE Matroids ($\mathcal{M}_{\text{graphic}} \cap \mathcal{M}_L \cap \mathcal{M}_R$)** $\implies$ **NP-Hard** (includes Hamiltonian Path when $d_v \le 2$)!
> - However, if degree bounds are only imposed on a subset of vertices $K \subseteq V$ that forms an **Independent Set** (no edge has both endpoints in $K$, as in `CF 1284G — Seollal` where constrained cells on a chessboard all have the same parity, or `CF 1556H — DIY Tree` after brute-forcing the $\binom{5}{2} = 10$ edges inside the $K \le 5$ constrained vertices in $2^{10}$ ways!), then **every remaining edge $e$ is incident to at most ONE vertex in $K$**!
> Thus the sets of edges incident to $v \in K$ are **pairwise disjoint**, forming a **SINGLE Partition Matroid $\mathcal{M}_2$**! Intersecting $\mathcal{M}_{\text{graphic}} \cap \mathcal{M}_2$ is then a **2-Matroid Intersection** problem, solvable in polynomial time!

#### The Weighted Matroid Intersection Exchange Graph (Generalizing SSP to Matroids)

Given $\mathcal{M}_1 = (E, \mathcal{I}_1)$ and $\mathcal{M}_2 = (E, \mathcal{I}_2)$ and a current common independent set $I \in \mathcal{I}_1 \cap \mathcal{I}_2$, how do we augment $I$ to $I'$ of size $|I| + 1$ at minimum cost?
Build the **Directed Bipartite Exchange Graph $D(I)$** with bipartition $I \sqcup (E \setminus I)$:
- **Source Set $X_1$**: $X_1 = \{y \in E \setminus I : I \cup \{y\} \in \mathcal{I}_1\}$ (elements that can be added to $I$ without breaking $\mathcal{M}_1$).
- **Sink Set $X_2$**: $X_2 = \{y \in E \setminus I : I \cup \{y\} \in \mathcal{I}_2\}$ (elements that can be added to $I$ without breaking $\mathcal{M}_2$).
- **Exchange Edges for $\mathcal{M}_1$ ($x \in I \longrightarrow y \in E \setminus I$)**: If $I \cup \{y\} \notin \mathcal{I}_1$, add a directed edge $x \to y$ for every $x \in C_1(I, y) \setminus \{y\}$ on the fundamental circuit of $y$ in $\mathcal{M}_1$ (so $(I \setminus \{x\}) \cup \{y\} \in \mathcal{I}_1$).
- **Exchange Edges for $\mathcal{M}_2$ ($y \in E \setminus I \longrightarrow x \in I$)**: If $I \cup \{y\} \notin \mathcal{I}_2$, add a directed edge $y \to x$ for every $x \in C_2(I, y) \setminus \{y\}$ on the fundamental circuit of $y$ in $\mathcal{M}_2$ (so $(I \setminus \{x\}) \cup \{y\} \in \mathcal{I}_2$).
- **Vertex Weights**: Assign weight $w(y) = +c_y$ for $y \in E \setminus I$ (cost of adding $y$) and $w(x) = -c_x$ for $x \in I$ (refund from removing $x$).
- **Shortest Augmenting Path Lemma (Edmonds–Lawler)**: Let $P$ be a path from $X_1$ to $X_2$ in $D(I)$ minimizing the primary key $(\text{Total Path Weight } w(P), \; \text{Number of Edges } |P|)$ (breaking weight ties by **fewest edges** so no chord shortcuts exist!). Then the symmetric difference $I' = I \triangle V(P)$ satisfies $I' \in \mathcal{I}_1 \cap \mathcal{I}_2$ with $|I'| = |I| + 1$ and minimum cost!

---

### 92.5 Multi-Commodity Flow ($K = 2$) & The Half-Integral Planar Grid Counterexample

In a standard single-commodity network, any flow from $s_1$ or $s_2$ can end at $t_1$ or $t_2$ indiscriminately. In a **$K$-Commodity Flow (`多商品流`)** problem, flow entering from $s_k$ **must** exit at its matching sink $t_k$. Even for $K = 2$ commodities with unit edge capacities on a tiny planar graph, **Integral Multi-Commodity Flow is NP-Hard** (when $G$ is directed, or when demands are arbitrary) and **Max Integral 2-Commodity Flow $\neq$ Min 2-Commodity Cut**!

#### Concrete Half-Integral Counterexample ($V = 6$ Crossed Grid / Wheel)

Consider an undirected graph $G$ with $6$ vertices $\{s_1, s_2, t_1, t_2, u, v\}$ arranged around a planar boundary in cyclic order $s_1 - s_2 - t_1 - t_2$, with two internal hub vertices $u, v$ connected by a central bridge $(u, v)$ of capacity $1$, and boundary/spoke edges of capacity $1$:
- Even simpler: consider the $4$-cycle $s_1 - s_2 - t_1 - t_2 - s_1$ where each of the $4$ cycle edges has **capacity $1/2$** (or scale by $2$: each of the $4$ cycle edges has **capacity $1$**, and we require routing $d_1 = 1$ unit of Commodity 1 from $s_1$ to $t_1$ AND $d_2 = 1$ unit of Commodity 2 from $s_2$ to $t_2$):

```
                s_2
              /     \
     cap = 1 /       \ cap = 1
            /         \
          s_1         t_1
            \         /
     cap = 1 \       / cap = 1
              \     /
                t_2
```

1. **Continuous / Half-Integral 2-Commodity Flow ($f_1 + f_2 = 2$ — FEASIBLE)**:
   - Route $1/2$ unit of Commodity 1 along the top path $s_1 \to s_2 \to t_1$ and $1/2$ unit along the bottom path $s_1 \to t_2 \to t_1$ (total $f_1 = 1$).
   - Route $1/2$ unit of Commodity 2 along the left path $s_2 \to s_1 \to t_2$ and $1/2$ unit along the right path $s_2 \to t_1 \to t_2$ (total $f_2 = 1$).
   - Total flow on each of the $4$ edges is $\frac{1}{2} + \frac{1}{2} = 1 \le 1$! And every cut separating $s_1$ from $t_1$ or $s_2$ from $t_2$ has capacity $1 + 1 = 2 \ge d_1 + d_2$.
2. **Integer 2-Commodity Flow ($f_1, f_2 \in \mathbb{Z}_{\ge 0}$ — INFEASIBLE / MAX = 1)**:
   - Any integer unit path from $s_1$ to $t_1$ uses either both top edges $\{ (s_1, s_2), (s_2, t_1) \}$ or both bottom edges $\{ (s_1, t_2), (t_2, t_1) \}$, completely disconnecting $s_2$ from $t_2$ in the remaining graph!
   - Thus the maximum total integer 2-commodity flow is **$1$**, whereas the fractional optimum (and minimum cut) is **$2$**!

---

## Master Recognition & Compilation Decision Table (Wave 4B Synthesis)

Use this diagnostic table during contests to translate any inequality, matrix, or submodular optimization problem into its exact algorithmic engine:

| Surface Problem Signal & Constraints | Intermediate Algebraic / Polyhedral Model | TU / Submodular Mechanism | Compiled Graph / Algorithmic Engine | Complexity & Key Pitfall |
| :--- | :--- | :--- | :--- | :--- |
| **Modify edge weights $d_e \pm \Delta_e$** so all $s$-$t$ paths have length $\le T$ (or $\ge T$) at min cost $\sum c_e \Delta_e$ | Primal LP over node timestamps $\pi_v$: $\pi_v - \pi_u + \Delta_e \ge d_e$, $\pi_t - \pi_s \le T$ | Dual constraint matrix is Directed Incidence Matrix ($\pi_v$ free $\implies$ flow conservation) | **Min-Cost Circulation**: parallel edges $u \to v$ of $(\text{cap } c_e, \text{cost } -d_e)$ and $(\text{cap } \infty, \text{cost } -(d_e-b_e))$; return $t \to s$ of cost $+T$ | MCMF; **Role Reversal**: Primal money cost $c_e =$ Dual capacity; Primal duration $d_e =$ Dual cost! |
| **Modify graph weights $w_e \pm \delta_e$** so fixed tree $T^*$ becomes an MST (`[SHOI2004] 最小生成树`) | $\delta_e + \delta_f \ge w_e - w_f$ for all $f \notin T^*$ and $e \in P_{T^*}(f)$ | Bipartite incidence matrix between $T^*$ and $E \setminus T^*$ is TU (Ghouila–Houri) | **Bipartite Max-Weight Matching / MCMF**: $S \to e \to f \to T$ with cost $-(w_e - w_f)$ | Kuhn–Munkres $O(M^3)$ if $c_e=1$; recover $\delta^*_e, \delta^*_f$ from residual potentials $\pi^*(v)$ |
| **Select intervals $[l_i, r_i]$** covering each point $t$ at least/at most $A_t$ times (`[NOI2008] 志愿者招募`) | Column-Consecutive-Ones system $\sum_{i: t \in [l_i, r_i]} x_i - y_t = A_t$ | Left-multiply by Upper-Bidiagonal Difference Matrix $D$ ($E_t - E_{t-1}$) | **Min-Cost Flow on Line**: interval $i$ becomes edge $l_i \to r_i + 1$ of cost $c_i$; slack $y_t$ becomes $t+1 \to t$ | MCMF; for **Row-Consecutive-Ones**, substitute $x_j = S_j - S_{j-1}$ or take LP Dual first! |
| **Circular / Wrap-around Intervals** on a clock of length $N$ (`Cyclic Consecutive-Ones`) | $\sum_{i \in C_t} x_i \ge A_t$ where intervals wrap past $N \to 1$ | Not TU directly ($\det = 2$ on odd cycles), **but TU once total count $K = \sum x_i$ is fixed!** | Fix/Binary-search $K = \sum x_i$ (or parametric flow); replace wrap-around $[l_i, N] \cup [1, r_i]$ with complement $[r_i+1, l_i-1]$ of sign $-1$ | $O(\log (\sum u_i)) \times \text{MCMF}$ via convexity of $C(K)$ |
| **Cover / Pack Rooted Tree** using **Vertical (Ancestor-to-Descendant) Paths** $u_j \to v_j$ | Tree-Vertex Incidence system $E_v : \sum_{j : v \in P_j} x_j \pm s_v = b_v$ | Rooted Tree Parent-Child Difference $E'_v = E_v - \sum_{w \in \text{child}(v)} E_w$ | **Min-Cost Circulation on Tree**: path $P_j$ becomes edge $v_j \to \text{parent}(u_j)$; slack $s_v$ becomes edge between $v$ and $\text{parent}(v)$ | MCMF; **Fails on V-shaped undirected tree paths** ($K_{1,3}$ has $\det = 2$) |
| **Minimize $\sum g_v(x_v) + \sum w_{uv} \|x_u - x_v\|$** or Isotonic $x_u \le x_v$ (`CF 1427G`, `保序回归`) | Lovász Extension $\hat{f}(x) = \int \big(\sum_{v \in S_\lambda} g'_v(\lambda) + c(\delta^+(S_\lambda))\big) d\lambda$ | Convexity of $g_v \implies$ monotone $g'_v(\lambda) \implies$ Nested Optimal Cuts $S^*_{\lambda_1} \supseteq S^*_{\lambda_2}$ | **Parametric Incremental Min-Cut** (`CF 1427G`) or **Parallel Binary Search (`整体二分`) + Project Selection** (`保序回归`) | $O(N \cdot \text{MaxFlow})$ via residual rollback or $O(\log U \cdot \text{MaxFlow})$ |
| **Two Hierarchical / Subtree Bounds** on two trees $T_1, T_2$ (`Two Laminar Matroids`) | $l_A \le \sum_{e \in A} x_e \le u_A$ for $A \in \mathcal{L}_1, \mathcal{L}_2$ | Laminar $\implies$ Hasse Forest $\implies$ Tree-Differenced matrix is TU | **Hasse Out-Tree $T_1 \to$ Elements $E \to$ Hasse In-Tree $T_2$** with lower/upper bounds | Bounded Circulation / MCMF |
| **Spanning Tree + Color Budget or Independent-Set Degree Bounds** (`CF 1556H`, `CF 1284G`) | $I \in \mathcal{M}_{\text{graphic}} \cap \mathcal{M}_{\text{partition}}$ | Not TU, but **2-Matroid Intersection is TDI** | **Edmonds' Weighted Matroid Intersection** (if $K \le 5$ vertices aren't independent, brute-force $2^{\binom{K}{2}}$ internal edges first!) | $O(2^{\binom{K}{2}} \cdot N^3 M)$ |

---

## 4-Tier Curated Problem Bank (Part 1: Stepping Stone & Intermediate — Problems P1–P11)

Every problem below is a non-template contest problem requiring structural recognition, algebraic/LP intermediate formulation, and mechanical compilation into a flow, cut, or matroid network.

---

### Tier 1: Stepping Stone (Problems P1–P5)

#### Problem P1: `[USACO07OPEN] Dining G` (3-Entity Star Compatibility vs. 3D Matching)
- **Judge URL**: [Luogu P2891](https://www.luogu.com.cn/problem/P2891)
- **Constraints**: $N \le 100$ cows, $F \le 100$ foods, $D \le 100$ drinks. Each food and each drink can be consumed by at most $1$ cow. Each cow $i$ has a list of acceptable foods $F_i \subseteq \{1, \dots, F\}$ and acceptable drinks $D_i \subseteq \{1, \dots, D\}$. Maximize the number of cows receiving both an acceptable food and an acceptable drink.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   The statement involves **three classes of entities** (Foods, Cows, Drinks) with unit capacities, tempting beginners to fear NP-hard 3D Matching. However, cow $i$'s preference is **factored (star-shaped)**: whether cow $i$ likes drink $d \in D_i$ is completely independent of *which* food $f \in F_i$ she ate.
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   Introduce binary flow variables $x_{f, i} \in \{0, 1\}$ ($f \in F_i$), $z_{i, d} \in \{0, 1\}$ ($d \in D_i$), and cow satisfaction indicator $y_i \in \{0, 1\}$:
   $$\max \sum_{i=1}^N y_i \quad \text{s.t.} \quad \sum_{f \in F_i} x_{f, i} = y_i = \sum_{d \in D_i} z_{i, d}, \quad \sum_{i} x_{f, i} \le 1, \quad \sum_{i} z_{i, d} \le 1, \quad y_i \le 1.$$
   This is the intersection of two bipartite matchings sharing the middle degree vector $y \in \{0, 1\}^N$ (a TU network system).
3. **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Place the central hub entity (**Cows**) in the middle, splitting each cow $i$ into $i_{\text{in}} \to i_{\text{out}}$ with capacity $1$ (enforcing $y_i \le 1$).
   - Place **Foods** on the left: $S \to f$ (capacity $1$) and $f \to i_{\text{in}}$ (capacity $1$) for $f \in F_i$.
   - Place **Drinks** on the right: $i_{\text{out}} \to d$ (capacity $1$) and $d \to T$ (capacity $1$) for $d \in D_i$.
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: Unit network with $V = F + 2N + D + 2 \le 402$ vertices and $E \le 20300$ edges; Dinic's algorithm runs in $O(E \sqrt{V}) \approx 4 \times 10^5$ operations.
   - **Broken Gadget Failure Mode**:
     - *Mistake 1*: Putting Cows on the left ($S \to i \to f \to d \to T$) connects *every* $f \in F_i$ to *every* $d \in D_i$, allowing cow $j$'s food $f \in F_j$ to transition to cow $i$'s drink $d \in D_i \setminus D_j$!
     - *Mistake 2*: Not splitting cow $i$ into $i_{\text{in}} \to i_{\text{out}}$ allows cow $i$ to consume $2$ foods and $2$ drinks simultaneously while counting as $2$ satisfied cows.

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P1
- **Hint 1 (Recognition)**: Which of the three sets (Foods, Cows, Drinks) acts as the central hub connecting the other two?
- **Hint 2 (Algebraic Model)**: Write flow conservation so that a unit of flow enters cow $i$ from a food $f \in F_i$ and exits cow $i$ to a drink $d \in D_i$.
- **Hint 3 (Graph & Pitfall)**: Why must cow $i$ be split into two vertices $i_{\text{in}} \to i_{\text{out}}$ of capacity $1$ even though foods and drinks are not split?
:::

---

#### Problem P2: `[NOI2008] 志愿者招募` (Volunteer Recruitment — Column-Consecutive-Ones & Difference Matrix $D$)
- **Judge URL**: [Luogu P3980](https://www.luogu.com.cn/problem/P3980)
- **Constraints**: $N \le 1000$ days, $M \le 10000$ volunteer types. Day $t \in \{1, \dots, N\}$ requires at least $A_t$ volunteers. Type $i$ works across the contiguous interval of days $[l_i, r_i]$ and costs $c_i$ per volunteer (unbounded supply). Find the minimum total cost.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   There is no graph in the problem statement—only intervals $[l_i, r_i]$ covering points $t \in \{1, \dots, N\}$. Greedy fails because overlapping intervals can substitute for one another, and DP fails because $M \le 10000$ intervals can overlap arbitrarily at any day $t$. The key structural clue is that every variable $x_i$ covers a **contiguous interval** $[l_i, r_i]$ of rows (**Column-Consecutive-Ones Property**).
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   Introduce $x_i \ge 0$ (number of type-$i$ volunteers) and surplus variable $y_t \ge 0$ on day $t$:
   $$E_t : \quad \sum_{i : t \in [l_i, r_i]} x_i - y_t = A_t \quad (t = 1, \dots, N).$$
   Left-multiply the system by the $(N+1) \times N$ Upper-Bidiagonal Difference Matrix $D$ (i.e., subtract $E_{t-1}$ from $E_t$ for $t = 1, \dots, N+1$, with $E_0 = E_{N+1} := 0$):
   $$E'_t = E_t - E_{t-1} : \quad \sum_{i : l_i = t} x_i - \sum_{i : r_i + 1 = t} x_i - y_t + y_{t-1} = A_t - A_{t-1}.$$
3. **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
   In the differenced system $\sum_{t=1}^{N+1} E'_t$, every variable appears once with $+1$ (out-flow) and once with $-1$ (in-flow) on vertices $\{1, 2, \dots, N+1\}$:
   - **Volunteer variable $x_i \ge 0$**: $+1$ at $l_i$ and $-1$ at $r_i + 1 \implies$ directed edge $l_i \longrightarrow r_i + 1$ with **capacity $\infty$** and **cost $c_i$**.
   - **Surplus variable $y_t \ge 0$**: $-1$ at $t$ and $+1$ at $t + 1 \implies$ directed edge $t + 1 \longrightarrow t$ with **capacity $\infty$** and **cost $0$** (or orient $t \to t+1$ with lower bound $A_t$).
   - **Right-hand side $b_t = A_t - A_{t-1}$**: If $b_t > 0$, connect Source $S \longrightarrow t$ with capacity $b_t$ and cost $0$; if $b_t < 0$, connect $t \longrightarrow T$ with capacity $-b_t$ and cost $0$.
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: $V = N + 3 \le 1003$, $E = M + 2N + 1 \le 12001$, all edge costs $c_i \ge 0$ and the zero-cost edges $t+1 \to t$ form a DAG, so SSP with Dijkstra potentials runs in $O(F \cdot E \log V)$.
   - **Broken Gadget Failure Mode**: Omitting the boundary equation $E'_{N+1} = -E_N$ loses the $-1$ endpoint for intervals ending at $r_i = N$ and violates global flow balance $\sum_{t=1}^{N+1} (A_t - A_{t-1}) = 0$.

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P2
- **Hint 1 (Recognition)**: Write the coverage inequality for each day $t$, convert it to an equality with a surplus variable $y_t \ge 0$, and look at the column of each volunteer variable $x_i$.
- **Hint 2 (Algebraic Model)**: What happens to a column of consecutive $1$s on rows $[l_i, r_i]$ when you subtract row $t-1$ from row $t$ for all $t \in \{1, \dots, N+1\}$?
- **Hint 3 (Graph & Pitfall)**: Be careful with the direction of the surplus variable $y_t$: it has $-1$ in $E'_t$ and $+1$ in $E'_{t+1}$, which is an edge $t+1 \to t$ of cost $0$.
:::

---

#### Problem P3: `[ZJOI2013] 防守战线` (Defense Line — Row-Consecutive-Ones & Potential LP Dual)
- **Judge URL**: [Luogu P3337](https://www.luogu.com.cn/problem/P3337)
- **Constraints**: $N \le 1000$ positions, $M \le 10000$ intervals. At position $i \in \{1, \dots, N\}$, you can build at most $1$ tower ($a_i \in [0, 1]$) at cost $C_i$. Each interval $[l_j, r_j]$ must contain at least $d_j$ towers ($\sum_{i=l_j}^{r_j} a_i \ge d_j$). Minimize $\sum_{i=1}^N C_i a_i$.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   Unlike `[NOI2008] 志愿者招募` (where variables were intervals covering points), here **variables $a_i$ are points** and **constraints $[l_j, r_j]$ are intervals**! Thus the constraint matrix $B$ has the **Row-Consecutive-Ones Property**, not the Column-Consecutive-Ones Property.
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   Apply **Iteration 88's LP Dual Compiler**:
   $$\text{Primal:} \quad \min_{a \ge 0} \sum_{i=1}^N C_i a_i \quad \text{s.t.} \quad \sum_{i=l_j}^{r_j} a_i \ge d_j \;\; (\text{dual } f_j \ge 0), \quad -a_i \ge -1 \;\; (\text{dual } z_i \ge 0).$$
   The Dual LP is:
   $$\max_{f, z \ge 0} \sum_{j=1}^M d_j f_j - \sum_{i=1}^N z_i \quad \text{s.t.} \quad \sum_{j : i \in [l_j, r_j]} f_j - z_i \le C_i \quad (i = 1, \dots, N).$$
   Notice that the Dual constraint matrix $B^\top$ has the **Column-Consecutive-Ones Property**! Introduce slack $s_i \ge 0$ so $\sum_{j : i \in [l_j, r_j]} f_j - z_i + s_i = C_i$, and subtract equation $i-1$ from equation $i$ ($i = 1, \dots, N+1$):
   $$\sum_{j : l_j = i} f_j - \sum_{j : r_j + 1 = i} f_j + (s_i - z_i) - (s_{i-1} - z_{i-1}) = C_i - C_{i-1}.$$
3. **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
   - **Interval Dual Flow $f_j \ge 0$**: Directed edge $l_j \longrightarrow r_j + 1$ with **capacity $\infty$** and **cost $-d_j$** (in Min-Cost Flow form).
   - **Point Slack $s_i \ge 0$**: Directed edge $i \longrightarrow i + 1$ with **capacity $\infty$** and **cost $0$**.
   - **Point Upper-Bound Dual $z_i \ge 0$**: Directed edge $i + 1 \longrightarrow i$ with **capacity $\infty$** and **cost $+1$**.
   - **Supply / Demand $b_i = C_i - C_{i-1}$**: Connect $S \to i$ (cap $b_i$, cost $0$) if $b_i > 0$, or $i \to T$ (cap $-b_i$, cost $0$) if $b_i < 0$.
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: Notice that all negative-cost edges $l_j \to r_j + 1$ go strictly **left-to-right**, and only positive-cost edges $i+1 \to i$ (cost $+1$) go right-to-left. Any directed cycle must step right from $l_j$ to $r_j + 1$ (cost $-d_j$) and step left $r_j - l_j + 1$ times (cost $+(r_j - l_j + 1) \ge d_j$), so **no negative-cost cycles exist** as long as $d_j \le r_j - l_j + 1$!
   - **Broken Gadget Failure Mode**: If you run naive SPFA on this graph without careful potential initialization, the dense forward DAG edges of cost $-d_j$ can cause SPFA to take $O(V E)$ time. Instead, since all negative edges go $u \to v$ with $u < v$, initialize potentials or scale/Simplex, or compute initial potentials recognizing the constraint structure.

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P3
- **Hint 1 (Recognition)**: Why can't you directly subtract row $j-1$ from row $j$ in the Primal LP of `[ZJOI2013] 防守战线`?
- **Hint 2 (Algebraic Model)**: Take the LP Dual (or substitute prefix sums $S_i = \sum_{k=1}^i a_k$ with $0 \le S_i - S_{i-1} \le 1$). What does the dual constraint matrix look like?
- **Hint 3 (Graph & Pitfall)**: Why does the upper bound $a_i \le 1$ create a backward edge $i+1 \to i$ of cost $+1$, and why does $d_j \le r_j - l_j + 1$ guarantee the absence of negative cycles?
:::

---

#### Problem P4: `[SHOI2004] 最小生成树` (Inverse MST & Residual Potential Reconstruction)
- **Judge URL**: [Luogu P2512 / BZOJ 1937](https://www.luogu.com.cn/problem/P4412)
- **Constraints**: $N \le 50$ vertices, $M \le 1000$ undirected edges with weights $w_e$, and a designated spanning tree $T^*$. Modifying edge $e$'s weight by $\Delta_e$ costs $|\Delta_e|$. Find the minimum total modification cost so that $T^*$ becomes an MST.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   We are modifying edge weights $w_e \gets w_e \pm \delta_e$ to make $T^*$ an MST. Because a tree edge $e \in T^*$ lies on the fundamental cycle of multiple non-tree edges $f \notin T^*$, greedily adjusting each cycle independently is suboptimal.
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   By Section 88.3, $T^*$ is an MST iff $w_e - \delta_e \le w_f + \delta_f$ for every non-tree edge $f \notin T^*$ and every tree edge $e \in P_{T^*}(f)$ on the fundamental tree path between endpoints of $f$:
   $$\min_{\delta \ge 0} \sum_{e \in T^*} \delta_e + \sum_{f \notin T^*} \delta_f \quad \text{s.t.} \quad \delta_e + \delta_f \ge \max(0, w_e - w_f) \quad \forall f \notin T^*, \; e \in P_{T^*}(f).$$
3. **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Dualizing $\delta_e + \delta_f \ge D_{e,f}$ with $\delta_e, \delta_f$ having objective coefficient $1$ yields the **Bipartite Max-Weight Matching** problem between left vertices $L = T^*$ ($|L| = N - 1$) and right vertices $R = E \setminus T^*$ ($|R| = M - N + 1$), with edge weight $D_{e,f} = \max(0, w_e - w_f)$ for each $e \in P_{T^*}(f)$.
   - By **Iteration 89 (Complementary Slackness)**, if the problem also asks for the modified weights $w'_e = w_e - \delta^*_e$ and $w'_f = w_f + \delta^*_f$, they are directly the **optimal Kuhn–Munkres vertex labels (dual potentials)** $(\delta^*_e, \delta^*_f)$!
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: $|L| = N - 1 \le 49$, $|R| \le 1000$. Rectangular Kuhn–Munkres (or MCMF) runs in $O(|L|^2 |R|) \approx 2.5 \times 10^6$ operations.
   - **Broken Gadget Failure Mode**: Adding edges $(e, f)$ with negative weight $w_e - w_f < 0$ without clamping to $\max(0, w_e - w_f)$ can corrupt Kuhn–Munkres if you force a perfect matching instead of a maximum-weight matching with zero-weight dummy edges.

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P4
- **Hint 1 (Recognition)**: What is the necessary and sufficient condition for a spanning tree $T^*$ to be a Minimum Spanning Tree in terms of its fundamental cycles?
- **Hint 2 (Algebraic Model)**: Why do we only ever decrease weights of $e \in T^*$ ($\delta_e \ge 0$) and increase weights of $f \notin T^*$ ($\delta_f \ge 0$)? Write the linear inequality for each pair $(e, f)$ with $e \in P_{T^*}(f)$.
- **Hint 3 (Graph & Pitfall)**: Recognize $\min \sum \delta_e + \sum \delta_f$ subject to $\delta_e + \delta_f \ge D_{e,f}$ as the Dual LP of Maximum Weight Bipartite Matching!
:::

---

#### Problem P5: `CF 704D — Captain America` (Two Partition Matroids / Bounded Bipartite Flow)
- **Judge URL**: [Codeforces 704D](https://codeforces.com/problemset/problem/704/D)
- **Constraints**: $N \le 10^5$ points $(x_i, y_i)$ in the plane, $M \le 10^5$ constraints. Painting a point red costs $r$, blue costs $b$. Each constraint specifies a horizontal line $y = y_0$ or vertical line $x = x_0$ and requires that the absolute difference between the number of red and blue points on that line is at most $d$. Output the minimum total cost and the color assignment, or `-1`.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   Each point $i$ belongs to **one horizontal line** (a partition of points by $y$-coordinate) and **one vertical line** (a partition of points by $x$-coordinate). Thus the line constraints form **two Partition Matroids / Bounded Degree Families**, whose stacked incidence matrix is a **Bipartite Incidence Matrix** (Totally Unimodular by Ghouila–Houri!).
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   Assume WLOG $r \le b$ (otherwise swap colors), so we want to **maximize the number of red points** $\sum_{i=1}^N z_i$ ($z_i \in \{0, 1\}$).
   If a line $L$ contains $cnt_L$ points and requires $|(\text{red}_L) - (\text{blue}_L)| = |2 \sum_{i \in L} z_i - cnt_L| \le d_L$, then the number of red points on line $L$ must lie in the integer interval:
   $$\left\lceil \frac{cnt_L - d_L}{2} \right\rceil \le \sum_{i \in L} z_i \le \left\lfloor \frac{cnt_L + d_L}{2} \right\rfloor.$$
   If multiple constraints apply to the same line $L$, take the minimum $d_L$. If any line has $l_L > u_L$, output `-1` immediately.
3. **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Create a left vertex for each active $x$-line and a right vertex for each active $y$-line.
   - Connect Source $S \longrightarrow x_k$ with **lower bound $l_{x_k}$ and upper bound $u_{x_k}$**.
   - Connect $y_m \longrightarrow T$ with **lower bound $l_{y_m}$ and upper bound $u_{y_m}$**.
   - Each point $i = (x_i, y_i)$ is a directed edge $x_i \longrightarrow y_i$ with lower bound $0$ and upper bound $1$.
   - Solve **Maximum $S$-$T$ Flow with Lower Bounds (`有源汇上下界最大流`)**! If feasible with max flow $F^*$, the minimum cost is $F^* \cdot r + (N - F^*) \cdot b$, and point $i$ is colored red iff $f^*(x_i \to y_i) = 1$.
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: Coordinate compression leaves at most $2N$ vertices and $3N$ edges. Because all middle edges have unit capacity, Dinic runs in $O(N \sqrt{N})$ time.
   - **Broken Gadget Failure Mode**: Forgetting that unconstrained lines still have trivial bounds $[0, cnt_L]$, or forgetting to take the tightest $d_L = \min d$ when the input gives multiple constraints for the same coordinate line.

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P5
- **Hint 1 (Recognition)**: Rewrite $|R_L - B_L| \le d_L$ using $R_L + B_L = cnt_L$ so that it becomes a lower and upper bound on $R_L$ alone.
- **Hint 2 (Algebraic Model)**: Why do constraints on $x$-lines and $y$-lines form a Totally Unimodular bipartite system?
- **Hint 3 (Graph & Pitfall)**: Model each point $(x_i, y_i)$ as a unit-capacity edge $x_i \to y_i$ and solve Max-Flow with edge lower and upper bounds.
:::

---

### Tier 2: Intermediate (Problems P6–P11)

#### Problem P6: `[BZOJ 3118] Orz the Immortal` (Weighted Inverse MST with Distinct Increment/Decrement Costs)
- **Judge URL**: [DarkBZOJ 3118 / Hydro BZOJ 3118](https://darkbzoj.cc/problem/3118)
- **Constraints**: $N \le 300$ vertices, $M \le 1000$ undirected edges. Each edge $e$ has weight $w_e$, a flag indicating whether $e \in T^*$ (a given spanning tree), cost $a_e$ to increase $w_e$ by $1$, and cost $b_e$ to decrease $w_e$ by $1$. Find the minimum total cost to make $T^*$ an MST.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   This generalizes Problem P4 (`[SHOI2004] 最小生成树`) from unit costs ($c_e = 1$) to arbitrary edge-dependent modification costs: decreasing tree edge $e \in T^*$ by $\delta_e \ge 0$ costs $b_e \delta_e$, and increasing non-tree edge $f \notin T^*$ by $\delta_f \ge 0$ costs $a_f \delta_f$.
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   The Primal LP is:
   $$\min_{\delta \ge 0} \sum_{e \in T^*} b_e \delta_e + \sum_{f \notin T^*} a_f \delta_f \quad \text{s.t.} \quad \delta_e + \delta_f \ge \max(0, w_e - w_f) \quad \forall f \notin T^*, \; e \in P_{T^*}(f).$$
   Applying **Iteration 88's Mechanical LP Dual Compiler** with dual variables $x_{e,f} \ge 0$:
   $$\max_{x \ge 0} \sum_{f \notin T^*} \sum_{e \in P_{T^*}(f)} \max(0, w_e - w_f) x_{e,f} \quad \text{s.t.} \quad \sum_{f: e \in P_{T^*}(f)} x_{e,f} \le b_e, \quad \sum_{e \in P_{T^*}(f)} x_{e,f} \le a_f.$$
3. **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Build a Bipartite Min-Cost Flow network with left part $T^*$ ($|T^*| = N - 1$) and right part $E \setminus T^*$:
   - Directed edge $S \longrightarrow e$ with **capacity $b_e$** and **cost $0$** for each $e \in T^*$.
   - Directed edge $f \longrightarrow T$ with **capacity $a_f$** and **cost $0$** for each $f \notin T^*$.
   - For each $f \notin T^*$ and $e \in P_{T^*}(f)$ with $w_e > w_f$, add directed edge $e \longrightarrow f$ with **capacity $\infty$** and **cost $-(w_e - w_f)$**.
   - Find the **Minimum-Cost Feasible Flow** (stopping SSP as soon as the shortest $S$-$T$ augmenting path has reduced cost $\ge 0$!). The answer is $-\text{MinCost}$.
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: $V \le 1002$ vertices, $E \le N \cdot M \le 3 \times 10^5$ edges (or $O(M \log N)$ edges using Heavy-Light Decomposition if needed, though here $\sum |P_{T^*}(f)|$ is small enough for direct MCMF).
   - **Broken Gadget Failure Mode**: Forcing *maximum* flow instead of *minimum-cost flow* (stopping when shortest path cost $\ge 0$) would route flow along zero-cost dummy paths or non-profitable edges if you included $w_e < w_f$ edges!

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P6
- **Hint 1 (Recognition)**: How do the non-uniform modification costs $b_e$ (for $e \in T^*$) and $a_f$ (for $f \notin T^*$) change the Primal LP compared to `[SHOI2004] 最小生成树`?
- **Hint 2 (Algebraic Model)**: Take the LP Dual of $\min \sum b_e \delta_e + \sum a_f \delta_f$ s.t. $\delta_e + \delta_f \ge w_e - w_f$. Where do $b_e$ and $a_f$ move in the Dual?
- **Hint 3 (Graph & Pitfall)**: $b_e$ and $a_f$ become capacities on $S \to e$ and $f \to T$! Why is the capacity on the middle edge $e \to f$ equal to $\infty$?
:::

---

#### Problem P7: `[AHOI2014 / JSOI2014] 支线剧情` (Story Branches — Rooted DAG Vertical Path Covering)
- **Judge URL**: [Luogu P4043](https://www.luogu.com.cn/problem/P4043)
- **Constraints**: $N \le 300$ vertices in a rooted DAG (rooted at vertex $1$). Each playthrough starts at vertex $1$ and follows a directed path to some terminal vertex. Traversing edge $e = (u, v)$ takes time $t_e \ge 0$. Find the minimum total time to traverse every edge $e \in E$ at least once.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   We must cover every edge $e \in E$ at least once using directed paths starting at root $1$. This can be viewed through **two dual lenses**:
   - *Lens A*: **Min-Cost Flow with Edge Lower Bounds $[1, \infty)$**.
   - *Lens B (Iteration 90/88)*: **LP Dual of DAG Path Covering** (or DAG Flow Conservation where every path variable $P$ starts at $1$).
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   Let $f_e \ge 1$ be the number of times edge $e = (u, v)$ is traversed. Since every playthrough starts at root $1$ and ends at some vertex $v$ (which we connect back to $1$ via a zero-cost return edge $v \to 1$), $f$ is a **circulation** on $G$ with return edges $v \to 1$:
   $$\min \sum_{e \in E} t_e f_e \quad \text{s.t.} \quad \sum_{e \in \delta^-(v)} f_e - \sum_{e \in \delta^+(v)} f_e - r_v = 0 \;\; (\forall v > 1), \quad f_e \ge 1, \quad r_v \ge 0.$$
   Write $f_e = 1 + f'_e$ with $f'_e \ge 0$ to eliminate the lower bound!
3. **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Pre-pay the mandatory base cost $\sum_{e \in E} t_e$ for the $1$ unit of mandatory flow on every edge $e = (u, v)$.
   - For each original edge $e = (u, v)$, add a directed edge $u \longrightarrow v$ with **capacity $\infty$** and **cost $t_e$** (representing $f'_e \ge 0$).
   - For each vertex $v > 1$ with out-edges or in-edges, add a return edge $v \longrightarrow 1$ with **capacity $\infty$** and **cost $0$** (representing ending a playthrough at $v$ and restarting at $1$).
   - Balance the mandatory $1$-unit flows at each vertex $v \in \{1, \dots, N\}$: let $\text{bal}(v) = \text{deg}^-(v) - \text{deg}^+(v)$. Connect $S_{\text{sup}} \to v$ with capacity $\text{bal}(v)$ if $\text{bal}(v) > 0$, and $v \to T_{\text{sup}}$ with capacity $-\text{bal}(v)$ if $\text{bal}(v) < 0$. Run standard MCMF from $S_{\text{sup}}$ to $T_{\text{sup}}$!
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: $V = N + 2 \le 302$, $E \le 6000$; since the graph is a DAG (except for return edges to $1$) with $t_e \ge 0$, there are no negative cycles and SSP runs in < 20 ms.
   - **Broken Gadget Failure Mode**: Only adding return edges $v \to 1$ from *sink* vertices ($\deg^+(v) = 0$) fails if the problem statement allows stopping a playthrough at any non-root vertex, or conversely adding $v \to 1$ from all vertices when playthroughs must reach a leaf. Here playthroughs end only at vertices with $\deg^+(v) = 0$ (or any vertex if allowed—check statement: in `支线剧情`, any vertex can return to $1$ except $1$).

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P7
- **Hint 1 (Recognition)**: Each playthrough is a path $1 \to \dots \to v$, which becomes a cycle if you add a zero-cost edge $v \to 1$.
- **Hint 2 (Algebraic Model)**: Substitute $f_e = 1 + f'_e$ ($f'_e \ge 0$) into the flow-conservation equations to absorb the lower bound $f_e \ge 1$.
- **Hint 3 (Graph & Pitfall)**: Why is this equivalent to the LP Dual of finding a potential $\pi_v$ after mandatory saturation?
:::

---

#### Problem P8: `CF 1288F — Red-Blue Graph` (TU Bipartite Edge Coloring with Lower/Upper Degree Penalties)
- **Judge URL**: [Codeforces 1288F](https://codeforces.com/problemset/problem/1288/F)
- **Constraints**: Bipartite graph with $N_1, N_2 \le 200$ vertices and $M \le 200$ undirected edges. Each edge $e$ can be colored Red (cost $R$), Blue (cost $B$), or left Uncolored (cost $0$). Each vertex $v$ has a color `'R'` (must have strictly more Red incident edges than Blue: $r_v - b_v \ge 1$), `'B'` (must have strictly more Blue than Red: $b_v - r_v \ge 1$), or `'U'` (unconstrained). Minimize total coloring cost.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   Each edge $e = (u, v)$ with $u \in V_1, v \in V_2$ can be given signed value $\Delta_e \in \{-1, 0, +1\}$ ($+1$ for Red, $-1$ for Blue, $0$ for Uncolored). Because the graph is **bipartite**, a signed choice on edge $e = (u, v)$ is literally a **unit of flow** moving either $u \to v$ (Red, $+1$ out of $u$ and $+1$ into $v$) or $v \to u$ (Blue, $+1$ out of $v$ and $+1$ into $u$)!
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   For each edge $e = (u, v)$ with $u \in V_1, v \in V_2$, introduce two binary variables $x_e \in \{0, 1\}$ (Red) and $y_e \in \{0, 1\}$ (Blue). Notice we do not even need the constraint $x_e + y_e \le 1$ because $R, B > 0$, so setting both $x_e = 1$ and $y_e = 1$ cancels their net degree contribution $(x_e - y_e = 0)$ at strictly positive cost $R + B > 0$!
   The net outflow at $u \in V_1$ is $\sum_{e \ni u} (x_e - y_e)$, which must lie in:
   - $[1, +\infty)$ if $u$ is `'R'`,
   - $(-\infty, -1]$ if $u$ is `'B'`,
   - $(-\infty, +\infty)$ if $u$ is `'U'`.
   Symmetrically, the net inflow at $v \in V_2$ is $\sum_{e \ni v} (x_e - y_e)$, with the same bounds!
3. **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
   - For each bipartite edge $e = (u, v)$ ($u \in V_1, v \in V_2$):
     - Add directed edge $u \longrightarrow v$ with **capacity $1$** and **cost $R$** (representing $x_e = 1$, Red).
     - Add directed edge $v \longrightarrow u$ with **capacity $1$** and **cost $B$** (representing $y_e = 1$, Blue).
   - For each vertex $u \in V_1$ and $v \in V_2$, connect to Source $S$ and Sink $T$ with **lower and upper bounds** $[l, u]$ and cost $0$:
     - For $u \in V_1$: `'R'` $\implies S \to u$ with $[1, \infty)$; `'B'` $\implies u \to T$ with $[1, \infty)$; `'U'` $\implies S \to u$ with $[0, \infty)$ and $u \to T$ with $[0, \infty)$.
     - For $v \in V_2$: `'R'` $\implies v \to T$ with $[1, \infty)$; `'B'` $\implies S \to v$ with $[1, \infty)$; `'U'` $\implies S \to v$ and $v \to T$ with $[0, \infty)$.
   - Add return edge $T \to S$ with $[0, \infty)$ and cost $0$, and solve **Bounded Min-Cost Circulation**!
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: $V \le 404$, $E \le 1200$, total mandatory lower-bound demand $\le 400$; SSP runs in $O(V E \log V) < 10$ ms.
   - **Broken Gadget Failure Mode**: What if the input graph were **not bipartite** (contained an odd cycle)? Then $x_e - y_e$ cannot be oriented so that Red is out-flow on one side and in-flow on the other—in fact, on a general graph, this is a **Bidirected Flow / General $b$-Matching** problem, which is NOT a standard network flow! Bipartiteness (Ghouila–Houri bicoloring $+1$ on $V_1$, $-1$ on $V_2$) is what makes the matrix TU.

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P8
- **Hint 1 (Recognition)**: On a bipartite graph $V_1 \sqcup V_2$, how can you interpret "coloring edge $(u, v)$ Red vs. Blue" as sending 1 unit of flow $u \to v$ vs. $v \to u$?
- **Hint 2 (Algebraic Model)**: Why don't you need a capacity gadget to prevent both $u \to v$ (Red) and $v \to u$ (Blue) from carrying flow simultaneously?
- **Hint 3 (Graph & Pitfall)**: Notice that for $u \in V_1$, Red edges leave $u$ ($+1$ outflow), whereas for $v \in V_2$, Red edges enter $v$ ($+1$ inflow). Swap the roles of $S \to v$ and $v \to T$ between $V_1$ and $V_2$!
:::

---

#### Problem P9: `[BZOJ 1283] 序列` (Sequence — Sliding Window Consecutive-Ones Packing)
- **Judge URL**: [Luogu P3980 Variant / Hydro BZOJ 1283](https://hydro.ac/p/bzoj-P1283)
- **Constraints**: Array $c_1, \dots, c_N$ ($N \le 1000, c_i \ge 0$), window length $K$, and limit $M$. Select a subset of indices $x_i \in \{0, 1\}$ to maximize $\sum_{i=1}^N c_i x_i$ such that every contiguous subarray of length $K$ contains at most $M$ selected elements: $\sum_{j=t}^{t+K-1} x_j \le M$ for all $1 \le t \le N - K + 1$.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   Each variable $x_i \in \{0, 1\}$ participates in all sliding windows $t$ such that $t \le i \le t + K - 1 \iff i - K + 1 \le t \le i$. Thus the constraint matrix is **both Row-Consecutive-Ones and Column-Consecutive-Ones** (a Toeplitz band matrix of $1$s)!
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   View each variable $x_i \in [0, 1]$ as an **interval of length $K$** covering positions $[i, i + K - 1]$ (so at any position $t$, at most $M$ active intervals overlap). Adding slack variable $s_t \ge 0$ at each position $t \in \{1, \dots, N\}$ gives:
   $$E_t : \quad \sum_{i : t \in [i, i+K-1]} x_i + s_t = M \quad (t = 1, \dots, N).$$
   Left-multiply by the Difference Matrix $D$ ($E'_t = E_t - E_{t-1}$ for $t = 1, \dots, N+1$):
   - Variable $x_i \in [0, 1]$ has $+1$ at row $i$ and $-1$ at row $\min(i + K, N + 1)$.
   - Slack $s_t \ge 0$ has $+1$ at row $t$ and $-1$ at row $t + 1$.
   - Right-hand side has $+M$ at row $1$ and $-M$ at row $N + 1$ (and $0$ everywhere else!).
3. **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Vertices: $1, 2, \dots, N + 1$, with Source $S \to 1$ (capacity $M$, cost $0$) and $N + 1 \to T$ (capacity $M$, cost $0$).
   - **Slack edge $s_t$**: Directed edge $t \longrightarrow t + 1$ with **capacity $M$ (or $\infty$)** and **cost $0$**.
   - **Selection edge $x_i$**: Directed edge $i \longrightarrow \min(i + K, N + 1)$ with **capacity $1$** and **cost $-c_i$** (for Min-Cost Max-Flow).
   - Send $M$ units of flow from $S$ to $T$; the maximum weight is $-\text{MinCost}$!
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: All edges go strictly left-to-right ($u < v$) on a DAG of $N + 1$ vertices! Initialize Johnson potentials in $O(N)$ by simple DAG DP $\pi(v) = \min_{u \to v} (\pi(u) + \text{cost}(u,v))$, and run $M$ Dijkstra augmentations in $O(M \cdot N \log N)$ time!
   - **Broken Gadget Failure Mode**: Forgetting that $x_i \le 1$ requires **capacity $1$** on the jump edge $i \to i + K$ (unlike `[NOI2008] 志愿者招募` where $x_i$ was unbounded so capacity was $\infty$).

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P9
- **Hint 1 (Recognition)**: Instead of thinking "window $t$ covers indices $[t, t+K-1]$", think "choosing index $i$ occupies $1$ slot across time $[i, i+K-1]$ out of $M$ parallel machines"!
- **Hint 2 (Algebraic Model)**: Subtract consecutive equations $E_t - E_{t-1}$. Why does the right-hand side $M - M = 0$ vanish at every internal vertex $2 \le t \le N$?
- **Hint 3 (Graph & Pitfall)**: Why is this equivalent to routing $M$ unit flows from $1$ to $N+1$ where each jump $i \to i+K$ has capacity $1$ and reward $c_i$?
:::

---

#### Problem P10: `[WC2007] 剪刀石头布` (Rock-Paper-Scissors — Landau's Theorem, Convex Marginal Splitting & Explicit Matrix Reconstruction)
- **Judge URL**: [Luogu P4249](https://www.luogu.com.cn/problem/P4249)
- **Constraints**: Tournament on $N \le 100$ players. Some match outcomes are already fixed, while others are undecided. Complete the tournament orientations to **maximize the number of cyclic triples (3-cycles)**, and **output the explicit $N \times N$ tournament adjacency matrix**.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   Directly counting 3-cycles $\{u \to v \to w \to u\}$ is a cubic $3$-variable interaction. The breakthrough is **Complementary Counting**: three vertices $\{u, v, w\}$ fail to form a 3-cycle iff one vertex beats the other two! Thus:
   $$\#(\text{3-Cycles}) = \binom{N}{3} - \sum_{v=1}^N \binom{\text{deg}^+(v)}{2}.$$
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   Let $d_v = \text{deg}^+(v)$ be the out-degree of player $v$. Each undecided match $e = \{u, v\}$ must assign $1$ win to either $u$ or $v$, and we want to **minimize the convex separable function** $\sum_{v=1}^N \binom{d_v}{2}$, where $\binom{d}{2}$ has strictly increasing marginal differences:
   $$\Delta \binom{d}{2} = \binom{d}{2} - \binom{d-1}{2} = d - 1 \quad (d = 1, 2, \dots, N-1).$$
   By Landau's Theorem / Polymatroid Base Polyhedron theory (Iteration 91), the out-degree vectors of tournaments form the Base Polyhedron $B(f)$ of the supermodular function $\binom{|S|}{2}$, and its bipartite incidence encoding is Totally Unimodular!
3. **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
   - For each undecided match $e = \{u, v\}$, create a match vertex $e$ with edge $S \longrightarrow e$ (capacity $1$, cost $0$), and two choice edges $e \longrightarrow u$ and $e \longrightarrow v$ (each capacity $1$, cost $0$).
   - If player $v$ already has $d_{v, 0}$ fixed wins and $rem_v$ undecided matches, pre-add $\binom{d_{v, 0}}{2}$ to the cost, and add $rem_v$ **parallel unit-capacity edges** from $v \longrightarrow T$ with marginal costs:
     $$d_{v, 0}, \; d_{v, 0} + 1, \; \dots, \; d_{v, 0} + rem_v - 1.$$
   - **Explicit Reconstruction**: After solving MCMF, for each undecided match $e = \{u, v\}$, inspect the residual/flow values: if $f^*(e \to u) = 1$, orient $u \to v$ ($u$ beats $v$); otherwise orient $v \to u$!
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: $V \le \binom{100}{2} + 102 \approx 5050$, $E \approx 2.5 \times 10^4$, all costs $\ge 0$; SSP runs in $\approx 50$ ms.
   - **Broken Gadget Failure Mode**: Using non-convex marginal costs (e.g., if the problem asked to *minimize* 3-cycles, so we had to *maximize* $\sum \binom{d_v}{2}$, making marginal costs $-d + 1$ decreasing!) breaks convex marginal splitting because MCMF would greedily pick the highest-index parallel edge $(N-2)$ before the lower-index edges $(0, 1, \dots)$.

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P10
- **Hint 1 (Recognition)**: Instead of counting cyclic triples $\{u \to v \to w \to u\}$, count **non-cyclic (transitive) triples**. How many transitive triples does a vertex $v$ with out-degree $d_v$ uniquely determine?
- **Hint 2 (Algebraic Model)**: Express $\binom{d_v}{2}$ as the sum of marginal increments $\sum_{k=1}^{d_v} (k - 1)$. Why is convexity essential here?
- **Hint 3 (Graph & Pitfall)**: How do you read off the winner of each undecided match $\{u, v\}$ from the optimal flow $f^*$?
:::

---

#### Problem P11: `[ONTAK 2010 / Luogu P6967] Vacation` (Multi-Category Consecutive-Ones Interval Equation-Difference)
- **Judge URL**: [Luogu P6967](https://www.luogu.com.cn/problem/P6967)
- **Constraints**: $N \le 1000$ days. On each day $i \in \{1, \dots, N\}$, doing activity E (eating) gives reward $e_i$ and activity S (sleeping) gives reward $s_i$ (you must choose exactly one of E or S each day). In every contiguous window of length $K$ ($[t, t+K-1]$ for $1 \le t \le N - K + 1$), you must choose E at least $m_E$ times and S at least $m_S$ times. Maximize total reward.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   This combines **Binary Choice per Day** ($x_i \in \{0, 1\}$ where $x_i = 1$ means E and $x_i = 0$ means S) with **both lower and upper bounds on every length-$K$ sliding window**!
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   Base reward if we choose S every day is $\sum_{i=1}^N s_i$. Switching day $i$ from S to E ($x_i = 1$) gives net reward $c_i = e_i - s_i$ (which may be positive or negative!).
   In every window $[t, t + K - 1]$ of length $K$, we need at least $m_E$ days of E and at least $m_S$ days of S (which means at most $K - m_S$ days of E):
   $$m_E \le \sum_{i=t}^{t+K-1} x_i \le K - m_S \quad (t = 1, \dots, N - K + 1).$$
   Introduce slack variable $y_t \in [0, (K - m_S) - m_E]$ for each window $t \in \{1, \dots, N - K + 1\}$:
   $$E_t : \quad \sum_{i=t}^{t+K-1} x_i + y_t = K - m_S.$$
   Notice that $E_t$ has the **Row-Consecutive-Ones Property** AND the **Column-Consecutive-Ones Property**! Subtract $E_{t-1}$ from $E_t$ for $t = 1, \dots, N - K + 2$:
   - For $t = 1$: $\sum_{i=1}^K x_i + y_1 = K - m_S$.
   - For $2 \le t \le N - K + 1$: $x_{t+K-1} - x_{t-1} + y_t - y_{t-1} = 0$.
   - For $t = N - K + 2$: $-\sum_{i=N-K+1}^N x_i - y_{N-K+1} = -(K - m_S)$.
3. **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Vertices: $1, 2, \dots, N - K + 2$.
   - Connect Source $S \longrightarrow 1$ with **capacity $K - m_S$** and cost $0$, and $(N - K + 2) \longrightarrow T$ with **capacity $K - m_S$** and cost $0$.
   - **Window Slack $y_t$ ($1 \le t \le N - K + 1$)**: Directed edge $t \longrightarrow t + 1$ with **capacity $(K - m_S) - m_E$** and **cost $0$**! (This bounded slack capacity is the exact compilation of the two-sided inequality $m_E \le \text{sum} \le K - m_S$!)
   - **Day Choice $x_i \in [0, 1]$ ($1 \le i \le N$)**:
     In the original equations, $x_i$ appears in windows $t \in [\max(1, i - K + 1), \; \min(i, N - K + 1)]$.
     Therefore, in the differenced equations, $x_i$ has $+1$ at $L_i = \max(1, i - K + 1)$ and $-1$ at $R_i = \min(i, N - K + 1) + 1$!
     Add a directed edge $L_i \longrightarrow R_i$ with **capacity $1$** and **cost $-(e_i - s_i)$**!
   - Find the Min-Cost Max-Flow of volume $K - m_S$ from $S$ to $T$; the answer is $\sum_{i=1}^N s_i - \text{MinCost}$!
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: $V = N - K + 4 \le 1004$, $E = 2N - K + 3 \le 2003$, DAG structure ($L_i < R_i$); SSP with DAG potential initialization runs in $O(K \cdot E \log V) < 15$ ms.
   - **Broken Gadget Failure Mode**: Notice how $y_t \in [0, K - m_S - m_E]$ effortlessly enforces **both** the lower bound $m_E$ and the upper bound $K - m_S$ using only **standard upper-capacitated edges** $t \to t+1$ of capacity $K - m_S - m_E$, without needing lower-bound circulation machinery! If you set the capacity of $t \to t+1$ to $\infty$ (as in P9), you lose the lower bound $m_E$!

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P11
- **Hint 1 (Recognition)**: Rewrite "at least $m_E$ of E and at least $m_S$ of S in every window of size $K$" as a two-sided bound $m_E \le \sum_{i=t}^{t+K-1} x_i \le K - m_S$.
- **Hint 2 (Algebraic Model)**: How can you convert a two-sided inequality $A \le \text{sum} \le B$ into an equation $\text{sum} + y_t = B$ using a **bounded slack variable** $0 \le y_t \le B - A$?
- **Hint 3 (Graph & Pitfall)**: Subtract $E_{t-1}$ from $E_t$. Notice that $y_t$ becomes an edge $t \to t+1$ of capacity $B - A = K - m_S - m_E$ and cost $0$!
:::

---

## 4-Tier Curated Problem Bank (Part 2: Advanced & Mastery — Problems P12–P22)

### Tier 3: Advanced (Problems P12–P17)

#### Problem P12: `[NOI2010] 海拔` (Altitude — Lovász Extension Coarea Reduction & Planar Dual Shortest Path)
- **Judge URL**: [Luogu P2046](https://www.luogu.com.cn/problem/P2046)
- **Constraints**: $(N+1) \times (N+1)$ directed grid ($N \le 500$). The northwest corner $(0, 0)$ has altitude $h_{0,0} = 0$ and the southeast corner $(N, N)$ has altitude $h_{N,N} = 1$. Every other vertex $(i, j)$ can be assigned **any real altitude** $h_{i,j} \in \mathbb{R}$. Moving uphill from $u$ to $v$ along directed edge $(u, v)$ with traffic $w_{uv} \ge 0$ consumes energy $w_{uv} \max(0, h_v - h_u)$ (moving downhill or flat consumes $0$ energy). Minimize total energy consumption.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph / Continuous Diagnostic Signal**:
   The problem asks to optimize over **continuous real altitudes** $h_{i,j} \in \mathbb{R}$ (not even restricted to $\{0, 1\}$!). Why on earth can we restrict $h_{i,j} \in \{0, 1\}$ without losing optimality?
2. **Step 2 — Algebraic / Lovász Extension Intermediate Representation**:
   First, clamping any $h_v < 0$ to $0$ and any $h_v > 1$ to $1$ never increases $\max(0, h_v - h_u)$, so $h \in [0, 1]^V$.
   Second, by **Iteration 91 (Theorem 91.3 — The Lovász Extension Coarea Formula)**, the objective function
   $$\hat{f}(h) = \sum_{(u, v) \in E} w_{uv} \max(0, h_v - h_u)$$
   is literally the **Lovász Extension** of the directed cut capacity function $f(T) = \sum_{(u,v) \in E} w_{uv} \mathbf{1}_{u \notin T, v \in T} = c(\delta^+(V \setminus T))$!
   By the Coarea Integral over $\lambda \in [0, 1]$:
   $$\hat{f}(h) = \int_0^1 \left( \sum_{(u,v) \in E} w_{uv} \mathbf{1}_{h_u < \lambda \le h_v} \right) d\lambda \ge \min_{S \subseteq V : (0,0) \in S, (N,N) \notin S} c(\delta^+(S)).$$
   And setting $h_v = 0$ for $v \in S^*$ and $h_v = 1$ for $v \notin S^*$ achieves this exact lower bound! Thus the continuous real optimization problem reduces with **zero gap** to a single binary **$s$-$t$ Minimum Cut** on the $(N+1) \times (N+1)$ planar grid!
3. **Step 3 — Reverse-Engineering Scratchpad (Planar Dual Graph Compilation)**:
   - Since $V = (N+1)^2 \approx 2.5 \times 10^5$, running Dinic directly is slow, and the graph is an **$s$-$t$ Planar Graph** ($s = (0,0)$ and $t = (N,N)$ both lie on the outer boundary!).
   - Place a Dual Source $S_{\text{dual}}$ in the bottom-left outer face and a Dual Sink $T_{\text{dual}}$ in the top-right outer face.
   - Each square cell is split or kept as a dual face node; each primal directed edge $u \to v$ of capacity $w_{uv}$ becomes a **directed dual edge** crossing $u \to v$ from left-to-right (when $u \in S$ is on the left and $v \in T$ is on the right) of length $w_{uv}$!
   - Run **Dijkstra's Algorithm** from $S_{\text{dual}}$ to $T_{\text{dual}}$.
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: $V_{\text{dual}} = N^2 + 2 \le 250002$ vertices, $E_{\text{dual}} = 4N(N+1) \le 10^6$ edges; Dijkstra runs in $O(N^2 \log N) \approx 0.15$ s.
   - **Broken Gadget Failure Mode**: Confusing the orientation of dual edges! Because the primal penalty is asymmetric ($w_{uv} \max(0, h_v - h_u)$ pays only when $h_u = 0 \in S$ and $h_v = 1 \in T$), the dual edge going one way across $(u, v)$ has weight $w_{uv}$ while the reverse dual edge has weight $w_{vu}$. Swapping clockwise vs. counterclockwise dual orientation transposes $w_{uv} \leftrightarrow w_{vu}$ and gives the wrong answer on directed grids!

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P12
- **Hint 1 (Recognition)**: Write $\max(0, h_v - h_u) = \int_0^1 \mathbf{1}_{h_u < \lambda \le h_v} \, d\lambda$. Why does this prove that an optimal altitude assignment only uses values $0$ and $1$?
- **Hint 2 (Algebraic Model)**: Once $h_v \in \{0, 1\}$, what graph problem is $\min \sum w_{uv} \mathbf{1}_{h_u = 0, h_v = 1}$ with $h_{0,0} = 0, h_{N,N} = 1$?
- **Hint 3 (Graph & Pitfall)**: Use $s$-$t$ Planar Duality to convert the directed grid Min-Cut into a single Dijkstra shortest path from the bottom-left boundary to the top-right boundary.
:::

---

#### Problem P13: `CF 1427G — One Billion Shades of Grey` (Lovász Extension Coarea Level-Set Cuts & Incremental Residual Rollback)
- **Judge URL**: [Codeforces 1427G](https://codeforces.com/problemset/problem/1427/G)
- **Constraints**: $N \times N$ grid ($N \le 200$). Border cells have fixed integer values $a_{i,j} \in [1, 10^9]$; some cells are blocked (`-1`); internal cells have free integer values $x_{i,j} \in \mathbb{Z}$. Minimize the sum of $|x_u - x_v|$ over all adjacent unblocked cell pairs $\{u, v\}$.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   The domain of each cell is $[1, 10^9]$ ($10^9$ states!), so multi-state chain cuts (`[HNOI2013] 切糕`) would require $200^2 \times 10^9$ vertices—impossible! However, the objective $\sum_{\{u,v\} \in E} |x_u - x_v|$ is a pure **$\ell_1$ Total Variation / Lovász Extension** with **no non-boundary unary terms**!
2. **Step 2 — Algebraic / Lovász Extension Intermediate Representation**:
   Let $v_1 < v_2 < \dots < v_K$ ($K \le 4N \le 800$) be the sorted distinct fixed values on the grid boundary. By the **Discrete Coarea Formula (Iteration 91, Theorem 91.3)**:
   $$|x_u - x_v| = \sum_{k=1}^{K-1} (v_{k+1} - v_k) \cdot \big| \mathbf{1}_{x_u > v_k} - \mathbf{1}_{x_v > v_k} \big|.$$
   Summing over all grid edges $\{u, v\} \in E$ decouples the problem into $K - 1$ **independent binary $s$-$t$ Min-Cut problems**:
   $$\min_x \sum_{\{u,v\} \in E} |x_u - x_v| = \sum_{k=1}^{K-1} (v_{k+1} - v_k) \cdot \min_{z^{(k)} \in \{0, 1\}^V} \sum_{\{u,v\} \in E} \big| z^{(k)}_u - z^{(k)}_v \big|,$$
   subject to $z^{(k)}_b = 1$ if $a_b > v_k$ (connected to Source $S$) and $z^{(k)}_b = 0$ if $a_b \le v_k$ (connected to Sink $T$)!
   Because the function is submodular and boundary conditions move monotonically from $S$ to $T$ as $k$ increases, the optimal binary cuts $S^*_k = \{u : z^{(k)}_u = 1\}$ satisfy the **Nesting Invariant** $S^*_1 \supseteq S^*_2 \supseteq \dots \supseteq S^*_{K-1}$, so $x^*_u = v_1 + \sum_{k=1}^{K-1} (v_{k+1} - v_k) z^{(k)}_u$ is automatically a valid single integer assignment!
3. **Step 3 — Reverse-Engineering Scratchpad (Incremental Residual Graph Rollback)**:
   - Even solving $K \le 800$ independent Max-Flows from scratch on $40000$ vertices is too slow.
   - Notice that when stepping from threshold $v_{k-1}$ to $v_k$, only the boundary cells $b$ with $a_b = v_k$ change their attachment from $S \to b$ (cap $\infty$) to $b \to T$ (cap $\infty$)!
   - **Incremental Rollback Contract**:
     1. At $k = 1$, attach all boundary cells with $a_b > v_1$ to $S$ and $a_b = v_1$ to $T$, and compute initial Max-Flow $F_1$.
     2. To transition from $k-1$ to $k$: for each boundary cell $b$ with $a_b = v_k$, let $f_{\text{used}}$ be the flow currently passing through $S \to b$. Since $b$ sits on the outer boundary, $f_{\text{used}} \le 4$! Roll back $f_{\text{used}}$ units of flow by running up to $4$ augmenting paths from $T$ to $b$ (or $b$ to $S$) in the residual graph, delete edge $S \to b$, add edge $b \to T$ of capacity $\infty$, and augment from $S$ to $T$!
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: Each of the $4N$ boundary cells changes from $S$ to $T$ **exactly once**, rolling back at most $4$ units of flow! Total number of augmenting paths across all $K$ thresholds is $O(N)$! Each DFS/BFS takes $O(N^2)$ time, giving $O(N^3) \approx 8 \times 10^6$ total operations!
   - **Broken Gadget Failure Mode**: Attempting to delete $S \to b$ without first pushing its active flow $f(S \to b)$ back to $S$ (or pulling from $T$ to $b$) violates Kirchhoff flow conservation at $b$ and corrupts all subsequent residual capacities!

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P13
- **Hint 1 (Recognition)**: Use the Coarea Formula $|x_u - x_v| = \int_{-\infty}^\infty |\mathbf{1}_{x_u > \lambda} - \mathbf{1}_{x_v > \lambda}| d\lambda$ to eliminate the $10^9$ value range.
- **Hint 2 (Algebraic Model)**: Why do you only need to evaluate the binary Min-Cut at the $K \le 4N$ distinct boundary values $v_1 < \dots < v_K$?
- **Hint 3 (Graph & Pitfall)**: When a boundary cell $b$ switches from $S \to b$ to $b \to T$, how much flow could $S \to b$ possibly carry, and how do you safely roll it back in the residual network?
:::

---

#### Problem P14: `[LOJ 6079 / BZOJ 4842] Delight for a Cat` (Sliding-Window Consecutive-Ones & Explicit Binary Schedule Reconstruction)
- **Judge URL**: [LOJ 6079](https://loj.ac/p/6079) / [Luogu P4001 Variant](https://www.luogu.com.cn/problem/P6967)
- **Constraints**: $N \le 1000$ hours, window length $K \le N$. In hour $i$, sleeping gives $s_i$ delight and eating gives $e_i$ delight. Every window of $K$ consecutive hours must have at least $m_s$ hours of sleeping and at least $m_e$ hours of eating. Maximize total delight and **output the explicit length-$N$ string of `'S'` and `'E'` choices**.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   The mathematical core is identical to Problem P11, plus **explicit primal variable reconstruction** ($x^*_i \in \{0, 1\}$ for each hour $i = 1, \dots, N$).
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   As derived in P11, let $x_i \in \{0, 1\}$ be the indicator of eating in hour $i$, so each window $t \in \{1, \dots, N - K + 1\}$ satisfies:
   $$\sum_{i=t}^{t+K-1} x_i + y_t = K - m_s, \quad 0 \le y_t \le K - m_s - m_e.$$
   Applying the Upper-Bidiagonal Difference Matrix $D$ ($E'_t = E_t - E_{t-1}$) turns every variable $x_i$ into a jump edge $L_i \to R_i$ of capacity $1$ and cost $-(e_i - s_i)$, and every slack $y_t$ into a step edge $t \to t+1$ of capacity $K - m_s - m_e$ and cost $0$.
3. **Step 3 — Reverse-Engineering Scratchpad (Explicit Solution Extraction)**:
   - Store the edge index `edge_id[i]` for each day $i$'s jump edge $L_i \longrightarrow R_i$ ($i = 1, \dots, N$).
   - Because the constraint matrix is Totally Unimodular (by the Consecutive-Ones Theorem 90.3) and all capacities $1$ and $K - m_s - m_e$ are integers, the optimal flow $f^*$ computed by MCMF is guaranteed to be $0$-$1$ integral on every jump edge!
   - After running MCMF of volume $K - m_s$ from $S$ to $T$, inspect `edge_id[i]`: if its flow is $1$ (equivalently, residual capacity of the forward edge is $0$), output `'E'`; otherwise output `'S'`.
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: $O(K \cdot N \log N)$ via DAG potential initialization + Dijkstra SSP.
   - **Broken Gadget Failure Mode**: Because $e_i - s_i$ can be **negative** (when sleeping is better than eating, so $-\Delta_i = s_i - e_i > 0$) or **positive** ($-\Delta_i < 0$), the graph has negative-cost edges! However, since all jump edges go from $L_i$ to $R_i$ with $L_i < R_i$, the initial network is a **DAG**, so you must still send the full mandatory flow volume $K - m_s$ from $S$ to $T$ (do NOT early-stop when shortest path cost $> 0$, because $K - m_s$ is the fixed right-hand side of equation $E'_1$!).

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P14
- **Hint 1 (Recognition)**: Formulate the two-sided window inequality $m_e \le \sum_{i=t}^{t+K-1} x_i \le K - m_s$ using a bounded slack variable $y_t \in [0, K - m_s - m_e]$.
- **Hint 2 (Algebraic Model)**: Why must you send the *exact* flow volume $K - m_s$ from $S$ to $T$ even if later augmenting paths have positive cost?
- **Hint 3 (Graph & Pitfall)**: Store the edge pointer for each day $i$'s jump edge $L_i \to R_i$ so you can read off $x^*_i = f^*(L_i \to R_i) \in \{0, 1\}$ in $O(1)$ time.
:::

---

#### Problem P15: `[ICPC / UOJ / QOJ] Cyclic Volunteer Recruitment` (Circular-Ones Matrix via Total-Flow Parametric Binary Search)
- **Judge URL**: [UVa 1406 / POJ 1275 Cashier Employment](http://poj.org/problem?id=1275) & Weighted Cyclic Generalization
- **Constraints**: A 24-hour (or $N$-hour, $N \le 500$) cyclic clock where hour $t \in \{1, \dots, N\}$ requires at least $R_t$ workers. There are $M \le 2000$ shift types; shift $i$ covers a **cyclic contiguous interval** $[l_i, r_i]$ (if $l_i \le r_i$, it covers $[l_i, r_i]$; if $l_i > r_i$, it **wraps around midnight**, covering $[l_i, N] \cup [1, r_i]$!), has upper bound $u_i$ workers, and costs $c_i \ge 0$ per worker. Minimize total cost.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   In a standard linear interval covering problem (`[NOI2008] 志愿者招募`), every column has consecutive $1$s. Here, wrap-around shifts ($l_i > r_i$) have $1$s on $[1, r_i]$ and $[l_i, N]$ with **$0$s in the middle** $[r_i + 1, l_i - 1]$!
   If you naively apply $E'_t = E_t - E_{t-1}$, a wrap-around shift $x_i$ gets $+1$ at row $1$, $-1$ at row $r_i + 1$, $+1$ at row $l_i$, and $-1$ at row $N + 1$ (**two $+1$s and two $-1$s**!). Even worse, as shown in Iteration 90, a general Circular-Ones matrix can have determinant $\pm 2$. How do we rescue Total Unimodularity?
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   Suppose we **fix (or parameterize) the total number of wrap-around workers** $K := \sum_{i \in W} x_i$ (where $W = \{i : l_i > r_i\}$ is the set of wrap-around shifts)!
   Notice the algebraic miracle: for any wrap-around shift $i \in W$, its indicator on $[1, N]$ is the **complement** of the contiguous interval $[r_i + 1, l_i - 1]$:
   $$\mathbf{1}_{t \in [l_i, N] \cup [1, r_i]} = 1 - \mathbf{1}_{t \in [r_i + 1, l_i - 1]}!$$
   Substituting this into day $t$'s coverage constraint $\sum_{i \notin W : t \in [l_i, r_i]} x_i + \sum_{i \in W : t \in [l_i, N] \cup [1, r_i]} x_i \ge R_t$ gives:
   $$\sum_{i \notin W : t \in [l_i, r_i]} x_i + K - \sum_{i \in W : t \in [r_i + 1, l_i - 1]} x_i - y_t = R_t \quad (t = 1, \dots, N)!$$
   Look at the matrix now: **every single shift $i$ (both normal and wrap-around!) is now a single contiguous interval on $[1, N]$**, plus one global equation $\sum_{i \in W} x_i = K$!
3. **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation for Fixed $K$)**:
   Subtract $E_{t-1}$ from $E_t$ for $t = 1, \dots, N+1$ (where $E_0 : \sum_{i \in W} x_i = K$ and $E_{N+1} : 0 = 0$):
   - **Normal shift $i \notin W$ ($l_i \le r_i$)**: Directed edge $l_i \longrightarrow r_i + 1$ with capacity $u_i$ and cost $c_i$.
   - **Wrap-around shift $i \in W$ ($l_i > r_i$)**: In $E_t$ ($t \in [r_i+1, l_i-1]$) it has coefficient $-1$, and in $E_0$ (or by wrapping $l_i \to N+1 \equiv 1 \to r_i + 1$) it has $+1$ at $l_i$ and $-1$ at $r_i + 1$ with $K$ units routed across the midnight bridge $(N+1) \longrightarrow 1$!
   - **Convexity of $C(K)$**: Because the LP relaxation for fixed $K$ is a parametric linear program with $K$ in the right-hand side (represented by a midnight return edge $(N+1) \longrightarrow 1$ with fixed flow $K$), the optimal cost $C(K)$ is a **convex function of $K$**!
   - Thus we find the optimal integer $K^* \in [0, \sum_{i \in W} u_i]$ by **Ternary Search / WQS-style Slope Binary Search** in $O(\log (\sum u_i))$ MCMF calls (or for feasibility when $c_i = 1$, binary search on total workers via Bellman–Ford difference constraints $\pi_t - \pi_{t-1}$)!
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: $O(\log(\sum u_i) \cdot \text{MCMF}(N, M))$.
   - **Broken Gadget Failure Mode**: If you simply add an unconstrained return edge $(N+1) \to 1$ of cost $0$ and capacity $\infty$ without coupling it to the wrap-around shifts $l_i \to r_i + 1$, a normal shift $2 \to 5$ could route flow backward through $(N+1) \to 1$ or a wrap-around shift $l_i \to r_i + 1$ could send flow *without* paying for the $[l_i, N]$ and $[1, r_i]$ coverage simultaneously! Fixing the flow on the wrap-around midnight bridge to equal $\sum_{i \in W} x_i = K$ is what prevents illegal circulation shortcuts.

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P15
- **Hint 1 (Recognition)**: Why does a wrap-around shift $[l_i, N] \cup [1, r_i]$ break the Column-Consecutive-Ones Property?
- **Hint 2 (Algebraic Model)**: Rewrite $\mathbf{1}_{t \in [l_i, N] \cup [1, r_i]} = 1 - \mathbf{1}_{t \in [r_i+1, l_i-1]}$. If you fix $K = \sum_{i \in W} x_i$, why does the matrix become Totally Unimodular?
- **Hint 3 (Graph & Pitfall)**: Why is the minimum cost $C(K)$ a convex function of $K$, allowing ternary/binary search over $K$?
:::

---

#### Problem P16: `[QOJ / ICPC Regional / CF 1067E Dual] Two-Tree Subtree Laminar Matroid Selection`
- **Judge URL**: [AtCoder ABC 263 Ex / JOISC / Codeforces Gym Two-Tree Subtree Bounds Archetype](https://codeforces.com/problemset/problem/704/D)
- **Constraints**: Two rooted trees $T_1$ and $T_2$ on the same vertex set $V = \{1, \dots, N\}$ ($N \le 500$). Choosing vertex $v \in V$ yields profit $w_v$ (can be chosen at most once, $x_v \in \{0, 1\}$). For each node $u$ in $T_1$, the number of chosen vertices in $u$'s subtree $Sub_{T_1}(u)$ must lie in $[l^{(1)}_u, r^{(1)}_u]$. For each node $v$ in $T_2$, the number of chosen vertices in $v$'s subtree $Sub_{T_2}(v)$ must lie in $[l^{(2)}_v, r^{(2)}_v]$. Maximize total profit $\sum_{v \in V} w_v x_v$.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   We have $2N$ subset capacity constraints on $x \in \{0, 1\}^V$. Why isn't this NP-hard Set Packing? Because in any rooted tree $T_k$, two subtrees $Sub_{T_k}(a)$ and $Sub_{T_k}(b)$ are either **disjoint** or **one is contained in the other**! Thus $\mathcal{L}_1 = \{Sub_{T_1}(u)\}_{u \in V}$ and $\mathcal{L}_2 = \{Sub_{T_2}(v)\}_{v \in V}$ are **Two Laminar Families** (Iteration 92.2)!
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   By Section 92.2, the Hasse diagram of $\mathcal{L}_1$ is literally the tree $T_1$ itself, and the Hasse diagram of $\mathcal{L}_2$ is the tree $T_2$ itself!
   For any vertex $w \in V$, the subtrees in $T_1$ containing $w$ are the ancestors of $w$ in $T_1$, and the subtrees in $T_2$ containing $w$ are the ancestors of $w$ in $T_2$.
3. **Step 3 — Reverse-Engineering Scratchpad (Hasse Out-Tree + In-Tree Graph Compilation)**:
   - Create two copies of the vertex set: $V^{(1)} = \{1^{(1)}, \dots, N^{(1)}\}$ for $T_1$, and $V^{(2)} = \{1^{(2)}, \dots, N^{(2)}\}$ for $T_2$.
   - **Out-Tree on $T_1$**:
     - Connect Source $S \longrightarrow \text{root}(T_1)^{(1)}$ with lower/upper bound $[l^{(1)}_{\text{root}}, r^{(1)}_{\text{root}}]$ and cost $0$.
     - For every directed edge $p \to c$ in $T_1$ (from parent to child), add directed edge $p^{(1)} \longrightarrow c^{(1)}$ with lower/upper bound $[l^{(1)}_c, r^{(1)}_c]$ and cost $0$.
   - **In-Tree on $T_2$**:
     - Connect $\text{root}(T_2)^{(2)} \longrightarrow T$ with lower/upper bound $[l^{(2)}_{\text{root}}, r^{(2)}_{\text{root}}]$ and cost $0$.
     - For every parent-child pair $(p', c')$ in $T_2$, add directed edge $c'^{(2)} \longrightarrow p'^{(2)}$ (from child to parent!) with lower/upper bound $[l^{(2)}_{c'}, r^{(2)}_{c'}]$ and cost $0$.
   - **Vertex Selection Bridges**:
     - For each $v \in \{1, \dots, N\}$, add directed edge $v^{(1)} \longrightarrow v^{(2)}$ with lower/upper bound $[0, 1]$ and cost $-w_v$.
   - Solve **Bounded Min-Cost Feasible Circulation** (with return edge $T \to S$ of bound $[0, N]$ and cost $0$)!
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: $V_{\text{flow}} = 2N + 2 \le 1002$ vertices and $E_{\text{flow}} = 3N + 1 \le 1501$ edges! Sparse bounded MCMF runs in $O(N^2 \log N)$.
   - **Broken Gadget Failure Mode**: Orienting $T_2$'s edges from parent to child instead of child to parent breaks flow conservation (flow entering $v^{(2)}$ would go down to $v$'s descendants instead of aggregating $Sub_{T_2}(v)$ up to $v^{(2)} \to \text{parent}(v)^{(2)}$!).

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P16
- **Hint 1 (Recognition)**: Verify that the family of all subtrees $\{Sub_T(u) : u \in V\}$ of a rooted tree $T$ is a **Laminar Family**.
- **Hint 2 (Algebraic Model)**: If you orient $T_1$ top-down (root to leaves) and $T_2$ bottom-up (leaves to root) and connect each $v^{(1)} \to v^{(2)}$ with flow $x_v \in \{0, 1\}$, what is the total flow passing through tree edge $\text{parent}(u)^{(1)} \to u^{(1)}$?
- **Hint 3 (Graph & Pitfall)**: Why does $v^{(1)}$ need to be placed at node $v$ itself in $T_1$ (not just at leaves), so that $x_v$ contributes to $u$'s subtree iff $u$ is an ancestor of $v$?
:::

---

#### Problem P17: `[CTSC / Project Crashing LP Dual Archetype] Critical Path Compression with Piecewise Linear Costs`
- **Judge URL**: [Luogu P3337 / POJ 3680 / Project Crashing LP Dual](https://www.luogu.com.cn/problem/P3337)
- **Constraints**: A project DAG $G = (V, E)$ with $N \le 300$ milestone vertices ($s = 1, t = N$) and $M \le 2000$ task edges. Task $e = (u, v)$ has normal duration $d_e$, minimum crashed duration $d_e - b_e$, and unit crashing cost $c_e$. Find the minimum crashing cost so all $1 \to N$ paths have length $\le T$, and **output both the optimal milestone timestamps $\pi^*_v$ and the optimal crash amount $\Delta^*_e$ for every edge**.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   As established in Iteration 88.2, compressing edge lengths to bound the **longest** path $\le T$ is a Primal Potential LP whose Dual is a Min-Cost Circulation, and recovering the timestamps $\pi^*_v$ requires **Iteration 89's Complementary Slackness Residual Potential Recovery**.
2. **Step 2 — Algebraic / Polyhedral Intermediate Representation**:
   Primal LP:
   $$\min_{\pi, \Delta \ge 0} \sum_{e \in E} c_e \Delta_e \quad \text{s.t.} \quad \pi_v - \pi_u + \Delta_e \ge d_e, \quad \pi_1 - \pi_N \ge -T, \quad -\Delta_e \ge -b_e.$$
   Dual LP:
   $$\min_{f_1, f_2, F \ge 0} \sum_{e \in E} (-d_e f_{e,1} - (d_e - b_e) f_{e,2}) + T \cdot F \quad \text{s.t. flow conservation, } f_{e,1} \le c_e.$$
3. **Step 3 — Reverse-Engineering Scratchpad (Dual Compilation + Residual Potential Extraction)**:
   - For each DAG edge $e = (u, v) \in E$, add two parallel directed edges $u \longrightarrow v$:
     - $e_1$: capacity $c_e$, cost $-d_e$.
     - $e_2$: capacity $\infty$, cost $-(d_e - b_e)$.
   - Add return edge $N \longrightarrow 1$ with capacity $\infty$ and cost $+T$.
   - Eliminate negative cycles (or since $G$ is a DAG, only cycles passing through $N \to 1$ can have negative cost! Equivalently, disconnect $N \to 1$ and repeatedly find shortest $1 \to N$ paths in $G_f$ as long as $\text{dist}_{G_f}(1, N) < -T$, augmenting flow along them!).
   - Once $\text{dist}_{G_{f^*}}(1, N) \ge -T$, run single-source shortest paths from $1$ in $G_{f^*}$ to get $\text{dist}[v] = \text{dist}_{G_{f^*}}(1, v)$, and set:
     $$t^*_v := -\text{dist}[v], \qquad \Delta^*_e := \max\big(0, \; d_e - (t^*_v - t^*_u)\big)!$$
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: Notice how removing the return edge $N \to 1$ and augmenting $1 \to N$ paths while $\text{dist}(1, N) < -T$ turns a general negative-cycle circulation problem into a **standard $1 \to N$ SSP problem on a DAG** where initial potentials $\pi_0(v)$ can be computed in $O(N + M)$ by topological sort!
   - **Broken Gadget Failure Mode**: If the input is infeasible (even crashing every edge by its maximum $b_e$, the longest $1 \to N$ path still exceeds $T$), then in the Dual network there is a $1 \to N$ path using only $e_2$ edges (capacity $\infty$) of cost $< -T$, so the flow becomes **unbounded ($\infty$)**. Check feasibility in $O(N + M)$ via DAG longest path on $d_e - b_e$ before running MCMF!

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P17
- **Hint 1 (Recognition)**: Before building any graph, check in $O(N+M)$ whether setting $\Delta_e = b_e$ for all $e$ makes the longest $1 \to N$ path $\le T$. What does infeasibility correspond to in the Dual LP?
- **Hint 2 (Algebraic Model)**: Why can you replace "eliminate all negative cycles containing $N \to 1$ (cost $+T$)" with "repeatedly augment shortest $1 \to N$ paths while path cost $< -T$"?
- **Hint 3 (Graph & Pitfall)**: Use Complementary Slackness on $G_{f^*}$: set $t^*_v = -\text{dist}_{G_{f^*}}(1, v)$ and $\Delta^*_e = \max(0, d_e - (t^*_v - t^*_u))$.
:::

---

### Tier 4: Mastery (Problems P18–P22)

#### Problem P18: `CF 1284G — Seollal` (Chessboard Independent-Set Degree Bounds $\implies$ Graphic $\cap$ Partition Matroid Intersection)
- **Judge URL**: [Codeforces 1284G](https://codeforces.com/problemset/problem/1284/G)
- **Constraints**: $N \times M$ grid ($N, M \le 20$) of `'O'` (open) and `'X'` (blocked) cells. Construct a **spanning tree** on all `'O'` cells such that every open cell $(i, j)$ with $i + j \equiv 0 \pmod 2$ (except $(1, 1)$) IS NOT A LEAF (i.e., has degree $\ge 2$ in the spanning tree), or report `NO`.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph / Matroid Diagnostic Signal**:
   We need a spanning tree $T$ on the open grid cells where specified vertices have $\deg_T(v) \ge 2$.
   Wait: why isn't this NP-hard (since degree-bounded spanning tree is NP-hard in general)?
   Look at the condition: the constrained vertices $B = \{(i, j) \neq (1,1) : (i+j) \text{ is even}\}$ all have the **same chessboard parity**! In a grid graph, every edge connects an even cell to an odd cell, so **no edge has both endpoints in $B$**—$B$ is an **Independent Set**!
2. **Step 2 — Algebraic / Matroid Intermediate Representation**:
   Instead of choosing tree edges $T \subseteq E$ with $\deg_T(v) \ge 2$ (lower bounds), pass to the **complement edge set** $I = E \setminus T$ (or dualize: choose a spanning forest / tree $T$? Wait: in a tree $T$, $\deg_T(v) \ge 2$ is a *lower* bound, whereas matroids enforce *upper* bounds!).
   How do we convert a degree **lower** bound $\deg_T(v) \ge 2$ into a Matroid **upper** bound?
   **Dualize to the Cographic Matroid** $\mathcal{M}^*(G)$, OR build from $B$ outward!
   - **Method A (Cographic $\cap$ Partition Matroid on Deleted Edges $I = E \setminus T$)**:
     Deleting $I \subseteq E$ leaves a connected graph iff $I$ is independent in the **Cographic Matroid** $\mathcal{M}_1 = \mathcal{M}^*(G)$ (rank $|E| - |V| + 1$), and leaves $\deg_{E \setminus I}(v) \ge 2$ iff at most $\deg_G(v) - 2$ edges incident to $v \in B$ are deleted ($\mathcal{M}_2 =$ **Partition Matroid** on the disjoint stars $\delta(v)$ for $v \in B$)!
   - **Method B (Direct Graphic $\cap$ Partition Matroid on $2|B|$ Incident Edges)**:
     Every vertex $v \in B$ must pick **2 incident edges** $I_v \subseteq \delta(v)$ ($|I_v| = 2$, total $2|B|$ edges) such that the union $I = \bigcup_{v \in B} I_v$ contains **no cycle** (independent in the **Graphic Matroid** $\mathcal{M}_1 = \mathcal{M}(G)$)! Once we find an acyclic set $I$ of size $2|B|$ where each $v \in B$ has degree $2$, we simply greedily extend $I$ to a full spanning tree $T \supseteq I$ using Kruskal/DSU—extending $I$ can only *increase* degrees of $v \in B$, keeping $\deg_T(v) \ge 2$!
3. **Step 3 — Reverse-Engineering Scratchpad (Matroid Intersection Compilation)**:
   Method B is breathtakingly clean:
   - Restrict the ground set of edges to $E_B = \{e \in E : e \text{ is incident to some } v \in B\}$. Since $B$ is an independent set, $E_B = \bigsqcup_{v \in B} \delta(v)$ is a **disjoint partition** of $E_B$!
   - **Matroid 1 ($\mathcal{M}_1 =$ Graphic Matroid on $G$)**: $I \subseteq E_B$ is independent iff $(V, I)$ is a forest (no cycles).
   - **Matroid 2 ($\mathcal{M}_2 =$ Partition Matroid on $E_B$)**: $I \subseteq E_B$ is independent iff $|I \cap \delta(v)| \le 2$ for every $v \in B$.
   - Run **Unweighted Matroid Intersection** to find the maximum common independent set $I^* \in \mathcal{I}_1 \cap \mathcal{I}_2$.
   - Check if $|I^*| == 2|B|$ and whether $G$ is connected. If yes, extend $I^*$ to a spanning tree using any remaining edges via DSU and print the grid!
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: $|V| \le 400$, $|E_B| \le 800$, target rank $r = 2|B| \le 400$. Matroid Intersection takes at most $r$ augmentations, each BFS on $|E_B|$ vertices taking $O(|E_B|^2)$ time $\implies O(|V|^3)$ total ($\approx 30$ ms).
   - **Broken Gadget Failure Mode**: Forgetting to check whether the entire open grid `'O'` is connected in the first place! Even if $|I^*| = 2|B|$, if some `'O'` cell is isolated in a separate connected component from $(1,1)$, no spanning tree exists.

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P18
- **Hint 1 (Recognition)**: Why is the set of constrained cells $B = \{(i, j) \neq (1,1) : i + j \equiv 0 \pmod 2\}$ an **Independent Set** in the grid graph?
- **Hint 2 (Algebraic Model)**: If you select $2$ incident edges for each $v \in B$ ($2|B|$ edges total) such that they form no cycle, why can this forest always be extended to a valid spanning tree (assuming $G$ is connected)?
- **Hint 3 (Graph & Pitfall)**: Formulate "select $2|B|$ edges with $\le 2$ per $v \in B$ and no cycles" as the intersection of a **Partition Matroid** and a **Graphic Matroid**.
:::

---

#### Problem P19: `CF 1556H — DIY Tree` (FPT $2^{\binom{K}{2}}$ Enumeration + Weighted Graphic $\cap$ Partition Matroid Intersection)
- **Judge URL**: [Codeforces 1556H](https://codeforces.com/problemset/problem/1556/H)
- **Constraints**: Complete weighted graph $K_N$ ($N \le 50$) with edge weights $w_{uv}$. Find the **Minimum Weight Spanning Tree** subject to degree bounds $\deg_T(i) \le d_i$ for the first $K$ vertices $i \in \{1, \dots, K\}$, where **$K \le 5$**.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph / FPT + Matroid Diagnostic Signal**:
   We want a Minimum Weight Spanning Tree with degree bounds $\deg_T(i) \le d_i$ on $S_{\text{con}} = \{1, \dots, K\}$ ($K \le 5$).
   Why can't we immediately apply Partition $\cap$ Graphic Matroid Intersection like in P18?
   Because in P18, the constrained vertices formed an independent set! Here, $G = K_N$ contains the $\binom{K}{2} \le \binom{5}{2} = 10$ **internal edges** $E_{\text{in}} = \{(u, v) : 1 \le u < v \le K\}$, each of which touches **TWO** constrained vertices in $\{1, \dots, K\}$!
2. **Step 2 — Algebraic / Hybrid FPT + Matroid Representation**:
   Partition the edge set of $K_N$ into three disjoint parts:
   - $E_{\text{in}}$: edges with **both** endpoints in $\{1, \dots, K\}$ ($|E_{\text{in}}| = \binom{K}{2} \le 10$).
   - $E_{\text{cross}}$: edges with **one** endpoint in $\{1, \dots, K\}$ and one endpoint in $\{K+1, \dots, N\}$.
   - $E_{\text{out}}$: edges with **both** endpoints in $\{K+1, \dots, N\}$ (unconstrained endpoints!).
    First, notice that among $E_{\text{out}}$, only the Minimum Spanning Forest $T_{\text{out}}$ of $\{K+1, \dots, N\}$ (at most $N - K - 1 \le 44$ edges, found once by Kruskal's algorithm!) could ever be needed in an optimal tree!
   Second, **brute-force all $2^{\binom{K}{2}} \le 1024$ subsets** $F_{\text{in}} \subseteq E_{\text{in}}$ that are acyclic and obey $\deg_{F_{\text{in}}}(i) \le d_i$!
   Once $F_{\text{in}}$ is fixed (contracting its connected components), every remaining edge in $E' = E_{\text{cross}} \cup T_{\text{out}}$ touches **at most ONE vertex in $\{1, \dots, K\}$**!
3. **Step 3 — Reverse-Engineering Scratchpad (Weighted Matroid Intersection)**:
   For each valid forest $F_{\text{in}} \subseteq E_{\text{in}}$ (with $|F_{\text{in}}|$ edges):
   - We must select $N - 1 - |F_{\text{in}}|$ edges from $E' = E_{\text{cross}} \cup T_{\text{out}}$ of minimum total weight such that:
     - **Matroid 1 ($\mathcal{M}_1 =$ Contracted Graphic Matroid $\mathcal{M}(G / F_{\text{in}})$)**: $I \cup F_{\text{in}}$ contains no cycle.
     - **Matroid 2 ($\mathcal{M}_2 =$ Partition Matroid on $E'$)**: For each $i \in \{1, \dots, K\}$, at most $d_i - \deg_{F_{\text{in}}}(i)$ edges incident to $i$ are chosen from $E_{\text{cross}}$ (and no limit on $T_{\text{out}}$).
   - Run **Weighted Matroid Intersection** (SPFA / Bellman–Ford on the bipartite exchange graph of size $|E'| \le 5 \times 45 + 44 = 269$).
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: Pre-filtering $E_{\text{out}}$ to $T_{\text{out}}$ reduces $|E'|$ from $\binom{50}{2} = 1225$ to $\le 269$! Also, only forests $F_{\text{in}}$ on $K=5$ vertices need to be checked (there are only $292$ labeled forests on $5$ vertices, not even $1024$!). $292$ calls to Weighted Matroid Intersection on $269$ elements with rank $\le 49$ runs in $\approx 0.4$ seconds!
   - **Broken Gadget Failure Mode**:
     1. Failing to pre-reduce $E_{\text{out}}$ to its MST $T_{\text{out}}$ leaves $|E'| = 1215$, making Weighted Matroid Intersection $20\times$ slower and causing TLE!
     2. When finding shortest augmenting paths in the Weighted Exchange Graph, failing to break weight ties by **minimum number of hops (edges)** allows chord shortcuts that violate independence in $I \triangle V(P)$!

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P19
- **Hint 1 (Recognition)**: Why do the $\binom{K}{2} \le 10$ edges inside $\{1, \dots, K\}$ prevent the degree constraints from forming a Partition Matroid, and how does $K \le 5$ let you eliminate them?
- **Hint 2 (Algebraic Model)**: Why can you throw away all edges inside $\{K+1, \dots, N\}$ except the $N - K - 1$ edges of their Minimum Spanning Tree $T_{\text{out}}$?
- **Hint 3 (Graph & Pitfall)**: For each of the $292$ forests $F_{\text{in}}$ on $\{1, \dots, K\}$, run Weighted Matroid Intersection on $E_{\text{cross}} \cup T_{\text{out}}$ (at most $269$ edges), breaking shortest-path ties by fewest hops.
:::

---

#### Problem P20: `[省选联考 2020 A 卷] 保序回归` ($L_p$ Isotonic Regression via Lovász Extension & Parallel Binary Search)
- **Judge URL**: [Luogu P6621](https://www.luogu.com.cn/problem/P6621)
- **Constraints**: $N \le 1000$ elements, $M$ partial-order relations $u \preceq v$ (derived from linear basis exchange), target values $y_v$, weights $w_v > 0$, and norm $p \in [1, 10^9]$. Find integer values $f_v \in \mathbb{Z}$ satisfying $u \preceq v \implies f_u \le f_v$ minimizing $\sum_{v=1}^N w_v |f_v - y_v|^p$.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph / Convex Duality Diagnostic Signal**:
   We are minimizing a separable convex objective $\sum_{v \in V} g_v(f_v)$ where $g_v(x) = w_v |x - y_v|^p$, subject to DAG partial-order inequalities $f_u \le f_v$ for $(u, v) \in E$.
2. **Step 2 — Algebraic / Lovász Extension Intermediate Representation**:
   By **Iteration 91 (Section 91.3 — The Lovász Extension Coarea Theorem)**:
   - Each convex unary function writes as $g_v(f_v) = g_v(L) + \sum_{\lambda = L}^{R - 1} \Delta g_v(\lambda) \cdot \mathbf{1}_{f_v > \lambda}$, where $\Delta g_v(\lambda) = g_v(\lambda + 1) - g_v(\lambda)$.
   - Each hard partial-order constraint $f_u \le f_v$ is the Lovász extension of the $\infty$-capacity directed cut penalty $\infty \cdot \max(0, f_u - f_v) = \sum_{\lambda = L}^{R-1} \infty \cdot \mathbf{1}_{f_u > \lambda \ge f_v}$.
   Therefore, the entire $L_p$ Isotonic Regression problem decouples across all integer thresholds $\lambda \in [L, R-1]$ into **independent Binary Project Selection (Minimum-Weight Closure) problems**:
   $$S^*_\lambda = \arg\min_{S \subseteq V : u \in S, (u,v) \in E \implies v \in S} \sum_{v \in S} \big(g_v(\lambda + 1) - g_v(\lambda)\big)!$$
   And because $g_v$ is convex, $\Delta g_v(\lambda)$ is monotone non-decreasing in $\lambda$, which by Submodularity guarantees the **Nesting Invariant** $S^*_L \supseteq S^*_{L+1} \supseteq \dots \supseteq S^*_{R-1}$!
3. **Step 3 — Reverse-Engineering Scratchpad (Parallel Binary Search `整体二分` + Closure Min-Cut)**:
   Instead of solving $R - L \approx 10^9$ Min-Cuts, use **Parallel Binary Search (`整体二分`)** `solve(V_sub, low, high)`:
   - If `low == high`, set $f^*_v = \text{low}$ for all $v \in V_{\text{sub}}$ and return.
   - Let $\text{mid} = \lfloor (\text{low} + \text{high}) / 2 \rfloor$. We want to determine for all $v \in V_{\text{sub}}$ whether $f^*_v > \text{mid}$ ($v \in S^*_{\text{mid}}$) or $f^*_v \le \text{mid}$ ($v \notin S^*_{\text{mid}}$).
   - Build the **Closure Min-Cut Graph** restricted to $V_{\text{sub}}$:
     - For each $v \in V_{\text{sub}}$, let $\Delta_v = g_v(\text{mid} + 1) - g_v(\text{mid})$.
     - If $\Delta_v < 0$ (moving from $\text{mid}$ to $\text{mid}+1$ *decreases* cost, i.e., positive profit $-\Delta_v > 0$), add edge $S \longrightarrow v$ of capacity $-\Delta_v$.
     - If $\Delta_v > 0$ (moving to $\text{mid}+1$ *increases* cost), add edge $v \longrightarrow T$ of capacity $+\Delta_v$.
     - For each partial-order relation $(u, v) \in E$ with **both** $u, v \in V_{\text{sub}}$, add edge $u \longrightarrow v$ of capacity $\infty$ ($u \in S \implies v \in S$).
   - Run Dinic's algorithm! Let $V_{\text{right}} = \{v \in V_{\text{sub}} : v \text{ is reachable from } S \text{ in } G_f\}$ ($f^*_v \ge \text{mid} + 1$) and $V_{\text{left}} = V_{\text{sub}} \setminus V_{\text{right}}$ ($f^*_v \le \text{mid}$).
   - Recurse on `solve(V_left, low, mid)` and `solve(V_right, mid + 1, high)`!
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: At each of the $O(\log (\max y_v))$ recursion levels, the vertex sets $V_{\text{sub}}$ form a **disjoint partition** of $V$, so the sum of Dinic runtimes across each depth level is bounded by a single Max-Flow on $(N, M)$! Total time: $O(\log U \cdot \text{MaxFlow}(N, M))$.
   - **Broken Gadget Failure Mode**: Including edges $(u, v) \in E$ where $u$ and $v$ have already been separated into different recursion branches ($u \in V_{\text{left}}, v \in V_{\text{right}}$)! Because the Nesting Invariant guarantees $f^*_u \le \text{mid} < \text{mid} + 1 \le f^*_v$ is *already satisfied* across branches, cross-branch edges are automatically satisfied and must be dropped so each recursive subproblem has size $|V_{\text{sub}}|$.

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P20
- **Hint 1 (Recognition)**: Express the convex penalty $g_v(f_v) = w_v |f_v - y_v|^p$ as a sum of marginal steps $\sum_{\lambda} (g_v(\lambda+1) - g_v(\lambda)) \mathbf{1}_{f_v > \lambda}$.
- **Hint 2 (Algebraic Model)**: For a single threshold $\lambda = \text{mid}$, how do you decide which vertices have $f^*_v \ge \text{mid} + 1$ vs. $f^*_v \le \text{mid}$ using a Minimum-Weight Closure cut?
- **Hint 3 (Graph & Pitfall)**: Use Parallel Binary Search (`整体二分`) so that at each depth of the recursion tree, the total number of vertices across all Min-Cut instances is $N$.
:::

---

#### Problem P21: `AGC 031 E — Snuke the Phantom Thief` (2D Coordinate Prefix/Suffix Ranks $\implies$ Two Laminar Slot Chains)
- **Judge URL**: [AtCoder AGC 031 E](https://atcoder.jp/contests/agc031/tasks/agc031_e)
- **Constraints**: $N \le 80$ jewels at $(x_i, y_i)$ with values $v_i \le 10^{15}$. $M \le 320$ constraints of 4 types:
  - `'L' a b`: at most $b$ stolen jewels have $x_i \le a$.
  - `'R' a b`: at most $b$ stolen jewels have $x_i \ge a$.
  - `'D' a b`: at most $b$ stolen jewels have $y_i \le a$.
  - `'U' a b`: at most $b$ stolen jewels have $y_i \ge a$.
  Maximize the total value of stolen jewels.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph Diagnostic Signal**:
   Notice that `'L'` and `'R'` constraints bound the $x$-coordinates of the chosen subset, while `'D'` and `'U'` constraints bound the $y$-coordinates. However, a `'R'` constraint ("at most $b$ jewels have $x_i \ge a$") is a **suffix** bound, while `'L'` ("at most $b$ jewels have $x_i \le a$") is a **prefix** bound—unless we know the **total number of stolen jewels $K \in \{1, \dots, N\}$**!
2. **Step 2 — Algebraic / Slot-Matching Intermediate Representation**:
   Fix the total number of stolen jewels $K \in \{1, \dots, N\}$ (since $N \le 80$, we can iterate over all $K = 1, \dots, N$!).
   Suppose we sort the $K$ stolen jewels by $x$-coordinate as $x_{p_1} \le x_{p_2} \le \dots \le x_{p_K}$, and by $y$-coordinate as $y_{q_1} \le y_{q_2} \le \dots \le y_{q_K}$:
   - **"At most $b$ stolen jewels have $x_i \le a$"** $\Longleftrightarrow$ the $(b+1)$-th stolen jewel from the left must satisfy $x_{p_{b+1}} \ge a + 1$ (and hence for all $r \ge b + 1$, $x_{p_r} \ge a + 1$)!
   - **"At most $b$ stolen jewels have $x_i \ge a$"** $\Longleftrightarrow$ the $(K - b)$-th stolen jewel from the left must satisfy $x_{p_{K-b}} \le a - 1$ (and hence for all $r \le K - b$, $x_{p_r} \le a - 1$)!
   Thus, once $K$ is fixed, every $x$-rank slot $r \in \{1, \dots, K\}$ acquires an exact allowed interval $[L^{(x)}_r, R^{(x)}_r]$, and every $y$-rank slot $c \in \{1, \dots, K\}$ acquires an exact allowed interval $[L^{(y)}_c, R^{(y)}_c]$!
3. **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation for Fixed $K$)**:
   - Build a network with **Left $X$-Slots** $\{1^{(x)}, \dots, K^{(x)}\}$, **Middle Jewels** $\{j_{\text{in}} \to j_{\text{out}}\}_{j=1}^N$, and **Right $Y$-Slots** $\{1^{(y)}, \dots, K^{(y)}\}$:
   - Connect $S \longrightarrow r^{(x)}$ (capacity $1$, cost $0$) for $r = 1, \dots, K$.
   - Connect $c^{(y)} \longrightarrow T$ (capacity $1$, cost $0$) for $c = 1, \dots, K$.
   - For each jewel $j \in \{1, \dots, N\}$, add vertex-split edge $j_{\text{in}} \longrightarrow j_{\text{out}}$ with **capacity $1$** and **cost $-v_j$**.
   - Connect $r^{(x)} \longrightarrow j_{\text{in}}$ (capacity $1$, cost $0$) iff $x_j \in [L^{(x)}_r, R^{(x)}_r]$.
   - Connect $j_{\text{out}} \longrightarrow c^{(y)}$ (capacity $1$, cost $0$) iff $y_j \in [L^{(y)}_c, R^{(y)}_c]$.
   - If the max flow from $S$ to $T$ equals $K$, update the global answer with $-\text{MinCost}(K)$!
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: $80$ iterations of $K$; each MCMF has $V \le 322$, $E \le 13000$, flow $K \le 80$ $\implies$ total time $\approx 0.25$ s.
   - **Broken Gadget Failure Mode**: What if the MCMF assigns jewel $j_1$ (with $x_{j_1} = 10$) to slot $1^{(x)}$ and jewel $j_2$ (with $x_{j_2} = 5$) to slot $2^{(x)}$ (out of sorted order)? Because we enforced monotonically nested intervals $L^{(x)}_1 \le L^{(x)}_2 \le \dots \le L^{(x)}_K$ and $R^{(x)}_1 \le R^{(x)}_2 \le \dots \le R^{(x)}_K$ via prefix/suffix max/min, **Hall's / Interval Uncrossing Lemma** guarantees that if $(j_1, j_2)$ can be matched to $(1^{(x)}, 2^{(x)})$, then swapping them into sorted order $(j_2 \to 1^{(x)}, j_1 \to 2^{(x)})$ is ALSO valid! If you forget to propagate $L^{(x)}_r = \max(L^{(x)}_r, L^{(x)}_{r-1})$ and $R^{(x)}_r = \min(R^{(x)}_r, R^{(x)}_{r+1})$, this uncrossing invariant breaks!

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P21
- **Hint 1 (Recognition)**: Fix the total number of stolen jewels $K \in \{1, \dots, N\}$. Why does fixing $K$ allow you to translate both `'L'` (prefix) and `'R'` (suffix) constraints into bounds on the $r$-th smallest $x$-coordinate?
- **Hint 2 (Algebraic Model)**: Compute the valid coordinate interval $[L^{(x)}_r, R^{(x)}_r]$ for each sorted $X$-rank $r \in \{1, \dots, K\}$ and $[L^{(y)}_c, R^{(y)}_c]$ for each sorted $Y$-rank $c \in \{1, \dots, K\}$.
- **Hint 3 (Graph & Pitfall)**: Use the Middle-Vertex Split pattern ($X\text{-Slots} \to \text{Jewel}_{\text{in}} \to \text{Jewel}_{\text{out}} \to Y\text{-Slots}$), and remember to enforce monotonicity $L_r \ge L_{r-1}$ and $R_r \le R_{r+1}$ across slots!
:::

---

#### Problem P22: `[NOI2019] 序列` (Sequence — LP Duality, Complementary Slackness & Simulated MCMF Residual Anatomy)
- **Judge URL**: [Luogu P5470](https://www.luogu.com.cn/problem/P5470)
- **Constraints**: Two arrays $a_1, \dots, a_N$ and $b_1, \dots, b_N$ ($N \le 2 \times 10^5, a_i, b_i \ge 1$). Select $K$ indices $I \subseteq \{1, \dots, N\}$ ($|I| = K$) and $K$ indices $J \subseteq \{1, \dots, N\}$ ($|J| = K$) such that **at least $L$ indices are shared** ($|I \cap J| \ge L$). Maximize $\sum_{i \in I} a_i + \sum_{j \in J} b_j$.

##### 4-Step "Zero Magic Gadgets" Compilation
1. **Step 1 — Non-Graph / Duality Diagnostic Signal**:
   Without the coupling constraint $|I \cap J| \ge L$, we would simply pick the $K$ largest $a_i$'s and $K$ largest $b_j$'s. Requiring $|I \cap J| \ge L$ means at most $K - L$ elements of $I$ can be paired with *distinct* elements of $J$ ($i \neq j$), while the remaining $L$ elements must be paired with the *same* index ($i = j$).
2. **Step 2 — Algebraic / LP Dual & Network Representation**:
   Introduce binary variables $x_i \in \{0, 1\}$ ($i \in I$) and $y_j \in \{0, 1\}$ ($j \in J$), decompose each chosen pair into either:
   - **Matched same-index pair** ($i = j$), or
   - **Free cross-index pair** ($i \neq j$), at most $K - L$ of which are allowed!
   This compiles directly into a compact **Min-Cost Max-Flow** network of volume $K$:
   - For each $i \in \{1, \dots, N\}$:
     - $S \longrightarrow i_A$ (capacity $1$, cost $-a_i$) and $i_B \longrightarrow T$ (capacity $1$, cost $-b_i$).
     - **Direct coupled edge**: $i_A \longrightarrow i_B$ (capacity $1$, cost $0$).
     - **Free decoupled hub $H_{\text{in}} \longrightarrow H_{\text{out}}$**: edge $i_A \longrightarrow H_{\text{in}}$ (cap $1$, cost $0$), bottleneck edge $H_{\text{in}} \longrightarrow H_{\text{out}}$ of **capacity $K - L$** and cost $0$, and edge $H_{\text{out}} \longrightarrow j_B$ (cap $1$, cost $0$).
3. **Step 3 — Reverse-Engineering Scratchpad (Complementary Slackness & 5-Candidate Simulated Augmentation)**:
   Because $N \le 2 \times 10^5$, we cannot run standard SSP directly; we use **Complementary Slackness / Residual Path Enumeration (`模拟费用流`)** to simulate each of the $K$ unit augmentations in $O(\log N)$ time using $5$ priority queues!
   At any step, what are the possible shortest $S \to T$ augmenting paths in $G_f$?
   Every vertex $i \in \{1, \dots, N\}$ is in one of $4$ states $(x_i, y_i) \in \{0, 1\}^2$. An augmenting path from $S$ to $T$ either:
   - **Case 1 (Uses $ +1$ unit of free hub capacity $H_{\text{in}} \to H_{\text{out}}$)**: Picks the largest unused $a_i$ ($x_i = 0$) and largest unused $b_j$ ($y_j = 0$).
   - **Case 2 (Does not change hub flow)**: Picks an unused pair $i = j$ ($x_i = y_i = 0$, gain $a_i + b_i$); OR picks unused $a_i$ ($x_i = 0$) and pairs it with $b_j$ where $x_j = 1, y_j = 0$ (completing $j$'s direct edge $j_A \to j_B$ and rerouting $j_A$'s old hub flow to $i_A$, gain $a_i + b_j$); OR symmetrically picks unused $b_j$ ($y_j = 0$) with $x_i = 0, y_i = 1$ (gain $a_i + b_j$).
   - **Case 3 (Pushes $1$ unit of flow BACKWARD through $H_{\text{out}} \to H_{\text{in}}$, freeing $1$ hub slot!)**: Picks $i$ with $x_i = 0, y_i = 1$ and $j$ with $x_j = 1, y_j = 0$, activating both direct edges $i_A \to i_B$ and $j_A \to j_B$ while cancelling $1$ unit on $H_{\text{in}} \to H_{\text{out}}$ (gain $a_i + b_j$)!
4. **Step 4 — Complexity & Broken Gadget Failure Mode**:
   - **Complexity**: Maintaining the $5$ priority queues (`Q_a[0][0]`, `Q_b[0][0]`, `Q_ab[0][0]`, `Q_a[0][1]`, `Q_b[1][0]`) with lazy deletion simulates each of the $K$ augmentations in $O(\log N)$ time $\implies O(N \log N)$ total!
   - **Alternative WQS / LP Dual Perspective**: You can also binary search the Lagrange multiplier $\lambda \ge 0$ on the capacity of $H_{\text{in}} \to H_{\text{out}}$ (WQS Binary Search on $|I \cap J| \ge L$), solving each fixed-$\lambda$ subproblem in $O(N)$!
   - **Broken Gadget Failure Mode**: Omitting Case 3 (the backward residual augmentation across $H_{\text{out}} \to H_{\text{in}}$ that merges two half-used indices $(0,1)$ and $(1,0)$ into two fully matched pairs $(1,1)$ and $(1,1)$ while refunding $1$ unit of free hub capacity)! Without Case 3, the greedy simulation gets stuck whenever the free hub capacity $K - L$ is saturated early.

::: {.callout-tip collapse="true"}
##### 3-Tier Progressive Hints for P22
- **Hint 1 (Recognition)**: Rephrase "$|I| = |J| = K$ and $|I \cap J| \ge L$" as: "form $K$ pairs $(i, j)$, where at most $K - L$ pairs are allowed to have $i \neq j$".
- **Hint 2 (Algebraic Model)**: Build the compact flow graph with a single bottleneck edge $H_{\text{in}} \to H_{\text{out}}$ of capacity $K - L$ for all $i \neq j$ transitions, and direct edges $i_A \to i_B$ for $i = j$ transitions.
- **Hint 3 (Graph & Pitfall)**: Classify all possible $S \to T$ augmenting paths in the residual network according to whether they change the flow on $H_{\text{in}} \to H_{\text{out}}$ by $+1$, $0$, or $-1$, and maintain the candidates with $5$ heaps!
:::

---

## Quarantined Template Problems Table (`R-01`–`R-08`)

In accordance with `AGENTS.md` and `flows_research/PLAN.md`, bare algorithm-verification or pure template problems are quarantined from the main 4-Tier Problem Bank and cataloged here as implementation verification references:

| Quarantine ID | Problem Name & Source | Underlying Standard Machinery | Why Quarantined |
| :--- | :--- | :--- | :--- |
| **`R-01`** | **Luogu P3381 — `【模板】最小费用最大流`** | Standard SSP / Primal–Dual MCMF | Pure black-box MCMF template verification with no modelling step. |
| **`R-02`** | **Library Checker — `Minimum Cost b-Flow`** | Bounded Min-Cost Circulation + Potential Output | Direct verification of primal circulation $f^*$ and dual potential $\pi^*$ output. |
| **`R-03`** | **Luogu P5960 — `【模板】差分约束`** | Bellman–Ford Shortest-Path Potentials ($\pi_v - \pi_u \le c_{uv}$) | Pure feasibility of difference constraints without cost optimization or LP dualization. |
| **`R-04`** | **UOJ #80 — `【模板】二分图最大权匹配`** | Kuhn–Munkres $O(N^3)$ Primal–Dual Labeling | Pure bipartite assignment template; used as a black-box subroutine in P4 (`[SHOI2004] 最小生成树`). |
| **`R-05`** | **Library Checker — `Assignment Problem`** | Kuhn–Munkres with explicit dual potential output | Pure template verification of Complementary Slackness vertex potentials on $K_{N,N}$. |
| **`R-06`** | **Luogu P3980 (Bare LP Form) / LOJ #117 — `有源汇上下界最小流`** | Feasible / Min Flow with Edge Lower Bounds | Standard lower-bound circulation reduction template. |
| **`R-07`** | **Codeforces Gym 102156D / Luogu P4208 — `Matroid Intersection Template`** | Unweighted Linear $\cap$ Partition Matroid Intersection | Direct verification of Edmonds' Exchange Graph BFS without structural reduction. |
| **`R-08`** | **Luogu P4722 — `【模板】最大流 加强版 (HLPP)`** | Highest-Label Preflow-Push / Dinic | Pure solver speed benchmark. |

---

## Multilingual (`[EN]` / `[ZH]` / `[JA]`) Master Bibliography for Wave 4B

### 1. English (`[EN]`) Monographic & Polyhedral Sources
- **[EN-1] Hoffman, A. J., & Kruskal, J. B. (1956)**. *Integral boundary points of convex polyhedra*. In *Linear Inequalities and Related Systems* (Annals of Mathematics Studies, Vol. 38, pp. 223–246). Princeton University Press. (The foundational theorem proving that $P(A, b)$ is integral for all integral $b$ iff $A$ is Totally Unimodular.)
- **[EN-2] Ghouila-Houri, A. (1962)**. *Caractérisation des matrices totalement unimodulaires*. *Comptes Rendus Hebdomadaires des Séances de l'Académie des Sciences*, 254, 1192–1194. (Proves the equitable row/column $\pm 1$ bicoloring characterization of TU matrices.)
- **[EN-3] Edmonds, J. (1970)**. *Submodular functions, matroids, and certain polyhedra*. In *Combinatorial Structures and Their Applications* (pp. 69–87). Gordon and Breach. (Introduces polymatroids, base polyhedra $B(f)$, Edmonds' greedy chain algorithm, and the Matroid Intersection Theorem.)
- **[EN-4] Lovász, L. (1983)**. *Submodular functions and convexity*. In *Mathematical Programming: The State of the Art* (pp. 235–257). Springer. (Introduces the Lovász extension $\hat{f}(x)$ and proves $\hat{f}$ is convex iff $f$ is submodular.)
- **[EN-5] Schrijver, A. (2003)**. *Combinatorial Optimization: Polyhedra and Efficiency* (3 Volumes: Vol. A *Paths, Flows, Matchings*; Vol. B *Matroids, Trees, Stable Sets*). Springer. (Chapters 13, 19–21, 41, and 44–49 cover Network Matrices, TU characterizations, Complementary Slackness, Matroid Intersection, and Submodular Flows.)
- **[EN-6] Ahuja, R. K., Magnanti, T. L., & Orlin, J. B. (1993)**. *Network Flows: Theory, Algorithms, and Applications*. Prentice Hall. (Chapter 9: *Minimum Cost Flows: Optimality Conditions and Complementary Slackness*; Chapter 19: *Convex Cost Flows and Lagrangian Relaxation*.)

### 2. Chinese (`[ZH]`) National Team Papers (`国家集训队论文`) & Treatises
- **[ZH-1] 胡伯涛 (Amber, 2007)**. 《最小割模型在信息学竞赛中的应用》 (*Applications of Minimum Cut Models in Olympiad in Informatics*). 2007 年信息学奥林匹克中国国家集训队论文. (Establishes the pseudo-Boolean cut polynomial framework, complementary slackness cut reconstruction, and maximum density subgraph duality.)
- **[ZH-2] 戴文渊 (Dai Wenyuan, 2009) & 姜志豪 (Jiang Zhihao, 2016)**. 《浅谈线性规划与网络流》 / 《网络流的一些建模方法》. 中国国家集训队论文 & WC 讲义. (Systematizes the Equation-Difference Method `流守恒差分建模法`, Consecutive-Ones matrices `连续 1 性质`, and explicit LP Primal–Dual compilation for `[NOI2008] 志愿者招募` and `[ZJOI2013] 防守战线`.)
- **[ZH-3] 高睿泉 (Gao Ruiquan, 2020)**. 《保序回归问题浅谈》 (*A Brief Discussion on Isotonic Regression Problems*). 2020 年信息学奥林匹克中国国家集训队论文, 配套 `[省选联考 2020 A 卷] 保序回归`. (Introduces $L_p$ isotonic regression via level-set threshold cuts and Parallel Binary Search `整体二分` to Chinese OI.)
- **[ZH-4] 钟子谦 (Zhong Ziqian, 2019)**. 《浅谈拟阵的一些拓展及其应用》 (*Extensions and Applications of Matroids*). 2019 年信息学奥林匹克中国国家集训队论文. (Covers Graphic/Linear/Partition Matroid Intersection, weighted exchange graphs, and the boundary between Network Flow and Matroid Intersection.)
- **[ZH-5] 王钦石 (Wang Qinshi, 2012) & 陈立杰 (WJMZBMR)**. 《浅谈费用流与线性规划对偶》 / 《模拟费用流问题》. WC / 集训队作业专刊. (Analyzes Complementary Slackness potential recovery and residual path anatomy in `[NOI2019] 序列`.)

### 3. Japanese (`[JA]`) Competitive Programming Treatises (`燃やす埋める` & Matroid / LP Duality)
- **[JA-1] noshi91 (2019–2021)**. *燃やす埋める問題と劣モジュラ関数・Lovász拡張* (*Project Selection / Burn-or-Bury Problems, Submodular Functions, and the Lovász Extension*). Noshi91 Blog & Library Notes. (Explains `燃やす埋める` directly as Cut-Representable Submodular Function Minimization and derives Coarea level-set cuts for `CF 1427G` and `ARC 107 F`.)
- **[JA-2] maspypy (2020–2023)**. *線形計画問題の双対と最小費用流 (LP Duality and Minimum Cost Flow)* & *マトロイド交差 (Matroid Intersection)*. Maspy's HP (`maspypy.com`). (Provides systematic Primal–Dual matrix transposition tables for AtCoder `AGC`/`ARC` flow problems and weighted matroid intersection tutorials.)
- **[JA-3] tatyam & snuke (AtCoder Editorial Corpus)**. Official editorials for `AGC 031 E — Snuke the Phantom Thief`, `AGC 034 D — Manhattan Max Matching`, `AGC 038 F — Two Permutations`, and `ARC 142 E — Pairing Wizards`. (Demonstrates slot-rank decomposition, submodular threshold cuts, and LP duality in modern Grand Contest problem setting.)
- **[JA-4] Murota, K. (室田一雄, 2001/2003)**. 『離散凸解析』 (*Discrete Convex Analysis*). Kyoritsu Shuppan / SIAM Monographs on Discrete Mathematics and Applications. (Unifies $L$-convex functions [Lovász extensions of submodular functions / potential duals] and $M$-convex functions [matroid base polyhedra / flow conservation primals] under discrete Legendre–Fenchel duality.)
