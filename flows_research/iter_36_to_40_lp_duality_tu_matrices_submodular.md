# Cohort 1 — Wave 4B Research Monograph: Linear Programming Duality, Totally Unimodular (TU) Matrices, Submodular Function Minimization & Polymatroid Flows (Iterations 36–40)

> [!IMPORTANT]
> **Editorial & Pedagogical Contract (`Zero Magic Gadgets` Standard)**
> This monograph (`flows_research/iter_36_to_40_lp_duality_tu_matrices_submodular.md`) forms Wave 4B of the multi-cohort discovery and modelling corpus for the Network Flows, Minimum Cuts, Matching, and Non-Graph Modelling textbook. Every theoretical reduction, matrix theorem, and contest problem in this volume adheres strictly to the **4-Step English-to-Graph Compilation Standard**:
> 1. **Step 1 — Non-Graph Diagnostic Signal (Recognition)**: What structural clue in the raw problem statement and constraint bounds tells a solver to invoke Linear Programming Duality, Total Unimodularity, Submodular Minimization, or Matroid Intersection—and why greedy or dynamic programming fails.
> 2. **Step 2 — Algebraic / Logical Intermediate Representation**: Explicit primal/dual linear programs, matrix incidence equations, consecutive-ones transformations, or submodular set/Lovász extensions written before any graph is drawn.
> 3. **Step 3 — Reverse-Engineering Scratchpad (Mechanical Compilation)**: Step-by-step translation from each algebraic column or constraint into directed edges, capacities, lower bounds, and costs.
> 4. **Step 4 — Hand-Checkable Toy Trace & Broken Gadget Counterexamples**: Concrete small-scale numerical traces ($N \le 4$) coupled with explicit proofs of what fails when subtle orientation, slack, or integrality conditions are violated.

---

## Executive Overview: Why Wave 4B Is the Theoretical Keystone of Flow Modelling

In Waves 1A through 4A, we compiled a vast repertoire of combinatorially distinct problems—bipartite matchings, project closures, multi-state chain cuts (`[HNOI2013] 切糕`), Coarea level-set cuts (`CF 1427G`), and equation-difference networks (`[NOI2008] 志愿者招募`)—into maximum flows and minimum-cost circulations. Yet three fundamental questions remain unanswered until one ascends to the unifying vantage point of **Linear Programming (LP) Duality**, **Total Unimodularity (TU)**, and **Submodular Polyhedra**:

1. **When a problem's natural variables are *node potentials* or *modified weights* rather than flows, how do we compile it into a flow network?**
   In problems such as crashing DAG project schedules, modifying edge weights so a prescribed tree $T$ becomes a Minimum Spanning Tree (`[SHOI2004] 最小生成树` / `BZOJ 3118`), or optimizing prefix-sum potentials under interval lower bounds (`[ZJOI2013] 防守战线`), each constraint is a *difference inequality* $\pi_v - \pi_u \le c_{uv}$ (or an elastic variant $\pi_v - \pi_u - z_{uv} \le c_{uv}$). Directly encoding $\pi_v$ as flow fails because $\pi_v$ is a potential, not a conserved quantity. Taking the **Linear Programming Dual** transposes the constraint matrix $A \mapsto A^T$, turning difference rows with one $+1$ and one $-1$ into **columns** with one $+1$ and one $-1$—which is the exact node-arc incidence matrix of a directed Min-Cost Flow network!
2. **When does an Integer Linear Program (ILP) have zero integrality gap and compile into a network flow?**
   Not every integer linear program can be solved by flow. The **Hoffman–Kruskal Theorem (1956)** proves that an LP relaxation $\{x \ge 0 : Ax \le b\}$ has integral vertices for all integral $b$ if and only if $A$ is **Totally Unimodular (TU)**. Furthermore, the **Consecutive-Ones Property (`连续 1 性质`)** and **Ghouila–Houri's Theorem (1962)** provide a fast, mechanical test for when an interval, tree-path, or bipartite constraint matrix is TU and how unimodular row operations (such as multiplying by the upper bidiagonal difference matrix $D$) convert it into a directed graph incidence matrix.
3. **Where is the exact mathematical boundary between Min-Cut, Submodular Function Minimization (SFM), Matroid Intersection, and NP-Hardness?**
   Why can a pairwise binary penalty $\Phi(x_u, x_v)$ be modeled by an $s$-$t$ min-cut if and only if $\Phi(0,0) + \Phi(1,1) \le \Phi(0,1) + \Phi(1,0)$? Why does the Lovász extension $\hat{f}(x)$ bridge continuous convex optimization (`CF 1427G`, Isotonic Regression) with discrete cut nesting? And why does intersecting *two* matroids (Bipartite Matching, Rainbow Spanning Tree) remain polynomial, while a seemingly innocent modification—putting a shared entity on the side rather than the middle of a flow network—crosses into 3-Matroid Intersection and NP-completeness?

Wave 4B resolves all three questions with complete mathematical rigor and competitive programming practicality.

---

## Iteration 36: Explicit Linear Programming Primal–Dual Compilation (`线性规划对偶转网络流`)

### 36.1 Step 1 — The Non-Graph Diagnostic Signal (Recognition)

How do you recognize during a contest that a problem requires **Explicit LP Primal–Dual Compilation** into Min-Cost Max-Flow (MCMF), rather than direct flow conservation or min-cut?

Look for the following **Four Diagnostic Signatures**:

1. **Difference-of-Variables Constraints ($\pi_v - \pi_u \le c_{uv}$)**:
   The problem asks you to choose an array of numbers, timestamps, prefix sums, or vertex potentials $\pi_1, \pi_2, \dots, \pi_n$ satisfying pairwise difference bounds $\pi_v - \pi_u \ge d_{uv}$ (or $\pi_v - \pi_u \le c_{uv}$). If the problem merely asked for a *feasible* assignment, you would run Bellman–Ford (`差分约束系统`). However, the problem asks you to **optimize a linear objective** $\sum_v b_v \pi_v$ or **pay a linear penalty** $\sum_e w_e z_e$ to relax ("stretch" or "compress") the right-hand sides $c_{uv} + z_{uv}$.
2. **Inverse Optimization (`逆优化问题`)**:
   Instead of finding the shortest path, longest DAG path, or Minimum Spanning Tree (MST) in a fixed weighted graph, you are *given* a target structure (e.g., a specific spanning tree $T^*$, a shortest-path tree, or a target makespan $D$) and asked to **modify the original edge weights $w_e \mapsto w_e + \Delta w_e$ at minimum total linear cost $\sum_e c_e |\Delta w_e|$** so that the target structure becomes optimal.
3. **Dense Interval / Prefix-Sum Inequalities with Unbounded Multiplicity**:
   You must choose non-negative quantities $a_1, \dots, a_n$ at unit costs $c_i$ such that $m$ intervals $[l_j, r_j]$ each have sum $\sum_{i=l_j}^{r_j} a_i \ge d_j$. Substituting prefix sums $P_i = \sum_{k=1}^i a_k$ immediately turns every interval sum into a *two-variable difference* $P_{r_j} - P_{l_j - 1} \ge d_j$ and the objective into $\sum_{i=1}^n c_i (P_i - P_{i-1})$.
4. **Why Naive Greedy and DP Fail**:
   - *Greedy fails* because modifying a single potential $\pi_v$ or edge weight $w_e$ simultaneously tightens and loosens multiple overlapping cycles or paths; local greedy adjustments can later be invalidated, requiring "regret" (residual flow reversal).
   - *Dynamic Programming fails* because the difference constraints $\pi_v - \pi_u \le c_{uv}$ form an arbitrary directed graph or intersecting interval family with high treewidth, leaving no small state boundary to memoize potentials.

---

### 36.2 Step 2 — The Complete Self-Contained Primal–Dual Dictionary

To compile any linear program into a flow network without guesswork or sign errors, a competitive programmer needs a rock-solid, mechanical **Primal–Dual Dictionary**.

#### 1. Derivation from Lagrangian Multipliers (Why the Rules Work)

Suppose we wish to solve a **Primal Minimization LP** with $n$ variables $x \in \mathbb{R}^n$ and $m$ constraints:
$$\begin{aligned}
\text{Minimize} \quad & c^T x = \sum_{j=1}^n c_j x_j \\
\text{subject to} \quad & \sum_{j=1}^n A_{i,j} x_j \ge b_i \quad \forall i \in \{1, \dots, m\}, \\
& x_j \ge 0 \quad \forall j \in \{1, \dots, n\}.
\end{aligned}$$

How can we prove a lower bound on the minimum possible value of $c^T x$?
Assign a non-negative multiplier (dual variable) $y_i \ge 0$ to each constraint $i \in \{1, \dots, m\}$. Since $y_i \ge 0$ and $\sum_j A_{i,j} x_j \ge b_i$, taking the linear combination of all $m$ inequalities preserves the $\ge$ direction:
$$\sum_{i=1}^m y_i b_i \le \sum_{i=1}^m y_i \left(\sum_{j=1}^n A_{i,j} x_j\right) = \sum_{j=1}^n \left(\sum_{i=1}^m A_{i,j} y_i\right) x_j.$$
Now, because every primal variable satisfies $x_j \ge 0$, if we choose our multipliers $y_i \ge 0$ such that for every column $j$, the coefficient of $x_j$ satisfies
$$\sum_{i=1}^m A_{i,j} y_i \le c_j \quad \Longleftrightarrow \quad (A^T y)_j \le c_j,$$
then we obtain the universal chain of inequalities:
$$b^T y = \sum_{i=1}^m b_i y_i \le \sum_{j=1}^n (A^T y)_j x_j \le \sum_{j=1}^n c_j x_j = c^T x.$$
To get the *tightest possible lower bound*, we maximize $b^T y$ over all valid $y \ge 0$. This optimization problem is the **Dual Linear Program**:
$$\begin{aligned}
\text{Maximize} \quad & b^T y = \sum_{i=1}^m b_i y_i \\
\text{subject to} \quad & \sum_{i=1}^m A_{i,j} y_i \le c_j \quad \forall j \in \{1, \dots, n\}, \\
& y_i \ge 0 \quad \forall i \in \{1, \dots, m\}.
\end{aligned}$$

What if the $i$-th primal constraint was an **equality** $\sum_j A_{i,j} x_j = b_i$ instead of $\ge b_i$? Then multiplying by $y_i$ preserves equality regardless of the sign of $y_i$! Thus, an equality constraint in the Primal corresponds to an **unrestricted (free) variable** $y_i \in \mathbb{R}$ in the Dual. Symmetrically, if a primal variable $x_j \in \mathbb{R}$ is unrestricted in sign, then to prevent $x_j \to \pm\infty$ from breaking the bound $(A^T y)_j x_j \le c_j x_j$, we must force exact equality $(A^T y)_j = c_j$ in the Dual!

#### 2. The Master Primal–Dual Translation Table

The following table summarizes the exact bijection between a **Minimization Primal LP** and a **Maximization Dual LP** (and vice versa, since the dual of the dual is the primal):

| Primal LP (Minimize $c^T x$) | $\Longleftrightarrow$ | Dual LP (Maximize $b^T y$) | Intuition / Algebraic Reason |
| :--- | :---: | :--- | :--- |
| Objective vector $c \in \mathbb{R}^n$ | $\longleftrightarrow$ | Right-hand side vector $c \in \mathbb{R}^n$ | Primal costs bound dual column sums |
| Right-hand side vector $b \in \mathbb{R}^m$ | $\longleftrightarrow$ | Objective vector $b \in \mathbb{R}^m$ | Dual multipliers weight primal RHS |
| Constraint matrix $A \in \mathbb{R}^{m \times n}$ | $\longleftrightarrow$ | Transposed matrix $A^T \in \mathbb{R}^{n \times m}$ | Rows of Primal become Columns of Dual |
| $i$-th constraint is $\ge b_i$ ("natural") | $\longleftrightarrow$ | Dual variable $y_i \ge 0$ | Positive multiplier preserves $\ge$ |
| $i$-th constraint is $\le b_i$ ("reversed") | $\longleftrightarrow$ | Dual variable $y_i \le 0$ (or rewrite $-A_i x \ge -b_i$) | Negative multiplier flips $\le$ to $\ge$ |
| $i$-th constraint is $= b_i$ (equality) | $\longleftrightarrow$ | Dual variable $y_i \in \mathbb{R}$ (free / unrestricted) | Equality holds for any sign of $y_i$ |
| Primal variable $x_j \ge 0$ ("natural") | $\longleftrightarrow$ | $j$-th dual constraint is $\le c_j$ ("natural") | Since $x_j \ge 0$, need $(A^T y)_j \le c_j$ |
| Primal variable $x_j \le 0$ ("reversed") | $\longleftrightarrow$ | $j$-th dual constraint is $\ge c_j$ ("reversed") | Since $x_j \le 0$, need $(A^T y)_j \ge c_j$ |
| Primal variable $x_j \in \mathbb{R}$ (free) | $\longleftrightarrow$ | $j$-th dual constraint is $= c_j$ (equality) | Non-zero gap would allow $-\infty$ via $x_j$ |

> [!TIP]
> **The Golden Mnemonic for Sign Directions ("Sensible vs. Bizarre")**
> - In a **Minimization** problem, a lower bound constraint $a_i^T x \ge b_i$ and non-negative variable $x_j \ge 0$ are **sensible (natural)** because they prevent $x$ from trivially drifting to $-\infty$.
> - In a **Maximization** problem, an upper bound constraint $A_j^T y \le c_j$ and non-negative variable $y_i \ge 0$ are **sensible (natural)** because they prevent $y$ from trivially drifting to $+\infty$.
> - **Rule**: **Sensible $\leftrightarrow$ Sensible**, **Tight (Equality $= $) $\leftrightarrow$ Loose (Free $\in \mathbb{R}$)**! In competitive programming, to avoid sign mistakes, always convert all inequalities in a Minimization LP to $\ge$ (or in a Maximization LP to $\le$) before taking the dual, so every dual variable is simply $\ge 0$.

#### 3. Weak and Strong LP Duality Theorems

- **Weak Duality Theorem**: For any primal feasible solution $x$ and any dual feasible solution $y$,
  $$b^T y \le c^T x.$$
- **Strong Duality Theorem (von Neumann / Gale–Kuhn–Tucker)**: If both the Primal LP and Dual LP are feasible (or if one is feasible and bounded), then both possess optimal solutions $x^*$ and $y^*$, and their optimal objective values are **strictly equal**:
  $$\max_{y \text{ feasible}} b^T y = \min_{x \text{ feasible}} c^T x.$$
  Moreover, if the Primal LP is infeasible, the Dual LP is either unbounded or infeasible; if the Primal LP is unbounded, the Dual LP is infeasible.

---

### 36.3 Exact LP Duality Between Maximum Flow and Fractional Minimum Cut

Let $G = (V, E)$ be a directed network with source $s$, sink $t$, and edge capacities $u_{uv} \ge 0$ for $(u, v) \in E$. How does the Max-Flow Min-Cut Theorem emerge mechanically from the Primal–Dual Table?

To make the flow conservation equations completely symmetric at *every* vertex (including $s$ and $t$), introduce a **return edge** $(t, s)$ with capacity $u_{ts} = \infty$ and objective coefficient $1$. A circulation $f : E \cup \{(t,s)\} \to \mathbb{R}_{\ge 0}$ that maximizes $f_{ts}$ is equivalent to an $s$-$t$ flow of value $f_{ts}$.

#### 1. The Primal LP (Maximum Flow via Return Edge $f_{ts}$)

$$\begin{aligned}
\text{Maximize} \quad & f_{ts} \\
\text{subject to} \quad & \sum_{w : (w, v) \in E'} f_{wv} - \sum_{w : (v, w) \in E'} f_{vw} = 0 \quad && \forall v \in V \quad \text{(dual variable: } d_v \in \mathbb{R}\text{)}, \\
& f_{uv} \le u_{uv} \quad && \forall (u, v) \in E \quad \text{(dual variable: } y_{uv} \ge 0\text{)}, \\
& f_{uv} \ge 0 \quad && \forall (u, v) \in E' = E \cup \{(t, s)\}.
\end{aligned}$$

Notice the structure of the constraint matrix:
- For each vertex $v \in V$, we have an equality constraint ($= 0$), which spawns a **free dual potential** $d_v \in \mathbb{R}$.
- For each original edge $(u, v) \in E$, we have a capacity upper bound $f_{uv} \le u_{uv}$ (sensible for Maximization), which spawns a **non-negative dual edge variable** $y_{uv} \ge 0$.
- In the column corresponding to primal variable $f_{uv}$ (for $(u, v) \in E$), $f_{uv}$ appears with coefficient $-1$ in row $u$ (out-flow from $u$), $+1$ in row $v$ (in-flow to $v$), and $+1$ in its capacity row $f_{uv} \le u_{uv}$. Its objective coefficient in the Primal is $0$.
- In the column corresponding to the return edge $f_{ts}$, $f_{ts}$ appears with coefficient $-1$ in row $t$ and $+1$ in row $s$, has no capacity row, and has objective coefficient $+1$ in the Primal.

#### 2. Taking the Mechanical Dual (Fractional Minimum Cut)

Applying our table column by column (since $f_{uv} \ge 0$ is sensible in Maximization, every dual constraint is $\ge$ its primal objective coefficient):
$$\begin{aligned}
\text{Minimize} \quad & \sum_{(u, v) \in E} u_{uv} y_{uv} \\
\text{subject to} \quad & d_v - d_u + y_{uv} \ge 0 \quad && \forall (u, v) \in E \quad \text{(from column } f_{uv}\text{)}, \\
& d_s - d_t \ge 1 \quad && \text{(from column } f_{ts}\text{)}, \\
& y_{uv} \ge 0 \quad && \forall (u, v) \in E, \qquad d_v \in \mathbb{R} \quad \forall v \in V.
\end{aligned}$$

Let us interpret this Dual LP geometrically! Since the constraints only depend on differences of $d$, we can shift all potentials by a constant and set $d_t = 0$. The constraint $d_s - d_t \ge 1$ becomes $d_s \ge 1$ (and at optimum, $d_s = 1$). If we restrict $d_v \in \{0, 1\}$ and $y_{uv} \in \{0, 1\}$, then $S = \{v \in V : d_v = 1\}$ is a vertex subset containing $s$ ($d_s = 1$) and excluding $t$ ($d_t = 0$). For every directed edge $(u, v) \in E$ crossing the cut from $u \in S$ ($d_u = 1$) to $v \notin S$ ($d_v = 0$), the inequality
$$d_v - d_u + y_{uv} \ge 0 \implies 0 - 1 + y_{uv} \ge 0 \implies y_{uv} \ge 1$$
forces $y_{uv} = 1$, contributing $u_{uv}$ to the objective $\sum u_{uv} y_{uv}$!
Even better: as we will prove via Total Unimodularity in Iteration 38 (and via the Coarea Formula in Iteration 39), the fractional polytope $\{ (d, y) : d_v - d_u + y_{uv} \ge 0, d_s - d_t \ge 1, y \ge 0 \}$ always has an **integral optimal vertex** $d_v \in \{0, 1\}, y_{uv} \in \{0, 1\}$. Thus Strong LP Duality immediately yields the **Max-Flow Min-Cut Theorem**!

---

### 36.4 Exact LP Duality Between Min-Cost Circulation / MCMF and Elastic Difference Constraints

Now we state and prove the **most important duality bridge in Wave 4B**: the exact equivalence between **Min-Cost Flow (with vertex demands/supplies $b_v$)** and **Difference Constraints with Elastic Slacks**.

#### 1. The Primal LP: Minimum-Cost Flow with Demands $b_v$

Let $G = (V, E)$ be a directed graph where each edge $(u, v) \in E$ has capacity $u_{uv} \ge 0$ and unit cost $c_{uv} \in \mathbb{R}$, and each vertex $v \in V$ has net inflow demand $b_v \in \mathbb{R}$ (with $\sum_{v \in V} b_v = 0$; here $b_v > 0$ means $v$ is a sink/demand node requiring net inflow $b_v$, and $b_v < 0$ means $v$ is a source/supply node supplying $-b_v$ units of net outflow, or equivalently in out-minus-in convention $\text{out}(v) - \text{in}(v) = s_v$). Let us use the convention $\text{in}(v) - \text{out}(v) = b_v$:
$$\begin{aligned}
\text{Minimize} \quad & \sum_{(u, v) \in E} c_{uv} f_{uv} \\
\text{subject to} \quad & \sum_{w : (w, v) \in E} f_{wv} - \sum_{w : (v, w) \in E} f_{vw} = b_v \quad && \forall v \in V \quad \text{(dual variable: } \pi_v \in \mathbb{R}\text{)}, \\
& -f_{uv} \ge -u_{uv} \quad && \forall (u, v) \in E \quad \text{(dual variable: } z_{uv} \ge 0\text{)}, \\
& f_{uv} \ge 0 \quad && \forall (u, v) \in E.
\end{aligned}$$
*(Notice we wrote the capacity constraint $f_{uv} \le u_{uv}$ in standard Minimization $\ge$ form as $-f_{uv} \ge -u_{uv}$ so that its dual multiplier $z_{uv}$ is non-negative: $z_{uv} \ge 0$!)*

#### 2. The Dual LP: Potential Modification / Elastic Difference Constraints

Look at column $f_{uv}$ in the Primal LP:
- $f_{uv}$ appears in row $u$ with coefficient $-1$ (multiplier $\pi_u \in \mathbb{R}$).
- $f_{uv}$ appears in row $v$ with coefficient $+1$ (multiplier $\pi_v \in \mathbb{R}$).
- $f_{uv}$ appears in its capacity row with coefficient $-1$ (multiplier $z_{uv} \ge 0$).
- Since $f_{uv} \ge 0$, the dual constraint for $(u, v) \in E$ is:
  $$\pi_v - \pi_u - z_{uv} \le c_{uv}.$$
And what is the Dual Objective? It is the inner product of the right-hand sides $(b_v, -u_{uv})$ with the dual variables $(\pi_v, z_{uv})$:
$$\begin{aligned}
\text{Maximize} \quad & \sum_{v \in V} b_v \pi_v - \sum_{(u, v) \in E} u_{uv} z_{uv} \\
\text{subject to} \quad & \pi_v - \pi_u - z_{uv} \le c_{uv} \quad && \forall (u, v) \in E \quad \text{(primal variable: } f_{uv} \ge 0\text{)}, \\
& z_{uv} \ge 0 \quad && \forall (u, v) \in E, \qquad \pi_v \in \mathbb{R} \quad \forall v \in V.
\end{aligned}$$

> [!IMPORTANT]
> **The "Zero Magic Gadgets" Compilation Compiler (`LP Dual` $\leftrightarrow$ `MCMF`)**
> Memorize the structural meaning of every component in this Dual LP:
> 1. **Dual Potentials $\pi_v \in \mathbb{R}$ $\longleftrightarrow$ Graph Vertices $v \in V$**:
>    Whenever an algebraic problem has unrestricted (or prefix-sum) variables $\pi_1, \dots, \pi_n$ that appear in pairs as $\pi_v - \pi_u$, each variable $\pi_v$ **is a vertex $v$ in the flow network**!
>    *(What if a constraint only has a single variable, like $\pi_v \le c$ or $-\pi_u \le c$? Introduce a **dummy zero-potential vertex $\pi_0 = 0$**, and rewrite $\pi_v \le c$ as $\pi_v - \pi_0 \le c$!)*
> 2. **Elastic Slack $z_{uv} \ge 0$ in $\pi_v - \pi_u - z_{uv} \le c_{uv}$ with Objective Penalty $-u_{uv} z_{uv}$ $\longleftrightarrow$ Directed Edge $u \to v$ with Capacity $u_{uv}$ and Cost $c_{uv}$**:
>    - If the inequality is **hard** ($\pi_v - \pi_u \le c_{uv}$, no slack $z_{uv}$ allowed, which is equivalent to $u_{uv} = +\infty$ penalty for $z_{uv}$), it compiles into a directed edge $u \to v$ with **capacity $\infty$ and cost $c_{uv}$**.
>    - If the inequality is **soft / elastic** ($\pi_v - \pi_u \le c_{uv} + z_{uv}$, where increasing the bound by $z_{uv} \ge 0$ costs $u_{uv}$ per unit in a maximization objective, or $+u_{uv} z_{uv}$ in a minimization objective), it compiles into a directed edge $u \to v$ with **capacity $u_{uv}$ and cost $c_{uv}$**!
> 3. **Objective Coefficient $+b_v \pi_v$ $\longleftrightarrow$ Vertex Supply/Demand $\text{in}(v) - \text{out}(v) = b_v$**:
>    - If $b_v < 0$ (say $b_v = -S_v$ with $S_v > 0$), vertex $v$ has net outflow $\text{out}(v) - \text{in}(v) = S_v$, so connect the super-source $S_{\text{src}} \to v$ with capacity $S_v$ and cost $0$.
>    - If $b_v > 0$, vertex $v$ has net inflow $\text{in}(v) - \text{out}(v) = b_v$, so connect $v \to T_{\text{snk}}$ with capacity $b_v$ and cost $0$.
>    - Because adding a constant shift $\pi_v \gets \pi_v + \Delta$ to all vertices does not change any difference $\pi_v - \pi_u$, the dummy vertex $\pi_0 = 0$ simply absorbs whatever net imbalance remains so that $\sum_{v=0}^n b_v = 0$!

Let us verify the signs carefully when the original potential problem is a **Minimization** problem versus a **Maximization** problem:
- **Case A (Maximization of $\sum b_v \pi_v - \sum u_{uv} z_{uv}$ subject to $\pi_v - \pi_u - z_{uv} \le c_{uv}$)**:
  Its dual is **Minimum-Cost Circulation / Flow** ($\min \sum c_{uv} f_{uv}$) with $\text{in}(v) - \text{out}(v) = b_v$ and $0 \le f_{uv} \le u_{uv}$.
- **Case B (Minimization of $\sum d_v \pi_v + \sum u_{uv} z_{uv}$ subject to $\pi_v - \pi_u + z_{uv} \ge w_{uv}$)**:
  Multiply the objective by $-1$ (turning $\min \Phi$ into $-\max (-\Phi)$) or negate $\pi_v \gets -\pi_v$:
  $$\begin{aligned}
  \text{Minimize} \quad & \sum_{v \in V} d_v \pi_v + \sum_{(u, v) \in E} u_{uv} z_{uv} \\
  \text{subject to} \quad & \pi_v - \pi_u + z_{uv} \ge w_{uv}, \quad z_{uv} \ge 0
  \end{aligned}$$
  has the exact Dual LP:
  $$\begin{aligned}
  \text{Maximize} \quad & \sum_{(u, v) \in E} w_{uv} f_{uv} \\
  \text{subject to} \quad & \sum_{w : (w, v) \in E} f_{wv} - \sum_{w : (v, w) \in E} f_{vw} = d_v \quad \forall v \in V, \\
  & 0 \le f_{uv} \le u_{uv} \quad \forall (u, v) \in E.
  \end{aligned}$$
  This is a **Maximum-Cost Flow** (or equivalently, negate edge costs $c_{uv} = -w_{uv}$ and run **Minimum-Cost Flow**) with vertex demand $\text{in}(v) - \text{out}(v) = d_v$ and edge capacity $u_{uv}$!

---

### 36.5 Step 3 — Three Concrete Non-Graph / Potential-Modification Compilations

Let us apply our compiler to three flagship problems from `[ZH]`, `[JA]`, and `[EN]` competitive programming, deriving their exact flow networks without a single unmotivated step.

---

#### Compilation 1: `[ZJOI2013] 防守战线` (Luogu P3337 — Interval Tower Defense via Dual Prefix Potentials)

- **Problem Statement**: You have $n$ positions $1, \dots, n$ along a defense line ($n \le 1000$). Building a defense tower at position $i$ costs $c_i \ge 0$; you may build **at most $1$ tower** at each position $i$ (or in the generalized version, at most $u_i$ towers; in ZJOI 2013 each position can hold at most $1$ tower). You are given $m \le 10000$ interval requirements: interval $[l_j, r_j]$ must contain at least $d_j$ towers in total. Find the minimum total cost to satisfy all requirements.
- **Step 1 (Diagnostic Signal)**:
  In Wave 3B (Iteration 30), we solved `[NOI2008] 志愿者招募` by taking consecutive equation differences because the *variables* were intervals and the *constraints* were single positions ($N \le 1000$ positions, $M \le 10000$ interval variables). Here in `[ZJOI2013] 防守战线`, the roles are **transposed**: the *variables* are single positions ($n \le 1000$) and there are $m \le 10000$ interval *constraints*! If we tried to take consecutive differences of the $m = 10000$ interval constraints, it would fail completely because arbitrary intervals do not telescope when subtracted! Instead, taking the **LP Dual** (or substituting prefix sums) places the $n = 1000$ positions as vertices and the $m = 10000$ intervals as edges!
- **Step 2 (Intermediate Algebraic Representation)**:
  We present **two equivalent dual perspectives**—both compile to the exact same graph:
  - *Perspective A (Direct LP Dual of the Primal Tower LP)*:
    Let $x_i \in [0, 1]$ be the number of towers at position $i$:
    $$\begin{aligned}
    \text{Minimize} \quad & \sum_{i=1}^n c_i x_i \\
    \text{subject to} \quad & \sum_{i=l_j}^{r_j} x_i \ge d_j \quad && \forall j \in \{1, \dots, m\} \quad (\text{dual variable } f_j \ge 0), \\
    & -x_i \ge -1 \quad && \forall i \in \{1, \dots, n\} \quad (\text{dual variable } g_i \ge 0), \\
    & x_i \ge 0 \quad && \forall i \in \{1, \dots, n\}.
    \end{aligned}$$
    Take the mechanical Dual LP:
    $$\begin{aligned}
    \text{Maximize} \quad & \sum_{j=1}^m d_j f_j - \sum_{i=1}^n 1 \cdot g_i \\
    \text{subject to} \quad & \sum_{j : i \in [l_j, r_j]} f_j - g_i \le c_i \quad \forall i \in \{1, \dots, n\}, \\
    & f_j \ge 0, \quad g_i \ge 0.
    \end{aligned}$$
    Now notice: in the Dual LP, each variable $f_j$ appears in a **contiguous range of constraints** $i \in [l_j, r_j]$! By Wave 3B's equation-difference method (adding slack $s_i \ge 0$ so $\sum_{j : i \in [l_j, r_j]} f_j - g_i + s_i = c_i$ and subtracting row $i-1$ from row $i$), every $f_j$ appears $+1$ at $l_j$ and $-1$ at $r_j + 1$!
  - *Perspective B (Prefix-Sum Potential Formulation $\to$ Immediate LP Dual)*:
    Even faster! Define prefix-sum potentials $\pi_i = \sum_{k=1}^i x_k$ for $0 \le i \le n$, with $\pi_0 = 0$. Since $0 \le x_i = \pi_i - \pi_{i-1} \le 1$, we have:
    $$\begin{aligned}
    \text{Minimize} \quad & \sum_{i=1}^n c_i (\pi_i - \pi_{i-1}) = c_n \pi_n + \sum_{i=1}^{n-1} (c_i - c_{i+1}) \pi_i - c_1 \pi_0 \\
    \text{subject to} \quad & \pi_{r_j} - \pi_{l_j - 1} \ge d_j \quad && \forall j \in \{1, \dots, m\} \quad (\text{hard difference constraint } \implies f_j \ge 0), \\
    & \pi_i - \pi_{i-1} \ge 0 \quad && \forall i \in \{1, \dots, n\} \quad (\text{hard monotonicity } \implies s_i \ge 0), \\
    & \pi_{i-1} - \pi_i \ge -1 \quad && \forall i \in \{1, \dots, n\} \quad (\text{upper bound } x_i \le 1 \implies g_i \ge 0).
    \end{aligned}$$
    Wait: look at the Primal objective $\sum_{i=1}^n c_i (\pi_i - \pi_{i-1})$. Instead of expanding $\sum c_i (\pi_i - \pi_{i-1})$ into vertex supplies $c_i - c_{i+1}$, we can keep $x_i = \pi_i - \pi_{i-1} + \dots$ or read the dual directly from Perspective B! Let's check what happens when we take the Dual of Perspective B:
    - Each potential $\pi_i$ ($0 \le i \le n$) is a vertex $i$.
    - In the objective $\sum_{i=1}^n c_i (\pi_i - \pi_{i-1})$, the coefficient of $\pi_i$ is $d^{\text{obj}}_i = c_i - c_{i+1}$ (with $c_0 = c_{n+1} = 0$).
    - Or even simpler in Perspective A's difference equations: for each $i \in \{1, \dots, n\}$,
      $$\sum_{j : i \in [l_j, r_j]} f_j - g_i + s_i = c_i.$$
      Subtract equation $(i-1)$ from equation $i$ (for $i = 1, \dots, n+1$, with equation $0$ and $n+1$ being $0 = 0$):
      $$\sum_{j : l_j = i} f_j - \sum_{j : r_j + 1 = i} f_j + (s_i - g_i) - (s_{i-1} - g_{i-1}) = c_i - c_{i-1}.$$
- **Step 3 (Reverse-Engineering Scratchpad — Graph Compilation)**:
  From the difference equations at vertices $i \in \{1, \dots, n+1\}$ (where $\text{out}(i) - \text{in}(i) = c_i - c_{i-1}$ with $c_0 = c_{n+1} = 0$):
  1. **Vertices**: $1, 2, \dots, n+1$, plus super-source $S$ and super-sink $T$.
  2. **Interval Variables $f_j \ge 0$ (reward $+d_j f_j$ in Maximization $\leftrightarrow$ cost $-d_j f_j$ in Minimization)**:
     $f_j$ has $+1$ in equation $l_j$ (outflow) and $-1$ in equation $r_j + 1$ (inflow), with capacity $\infty$:
     $$\text{Directed edge } l_j \longrightarrow r_j + 1 \quad \text{with capacity } \infty, \text{ weight (reward) } +d_j \text{ (or cost } -d_j\text{)}.$$
  3. **Slack Variables $s_i \ge 0$ (reward $0$)**:
     $s_i$ has $+1$ in equation $i$ and $-1$ in equation $i+1$:
     $$\text{Directed edge } i \longrightarrow i + 1 \quad \text{with capacity } \infty, \text{ weight } 0.$$
  4. **Upper-Bound Dual Variables $g_i \ge 0$ (penalty $-1 \cdot g_i$ in Maximization)**:
     $g_i$ has $-1$ in equation $i$ and $+1$ in equation $i+1$:
     $$\text{Directed edge } i + 1 \longrightarrow i \quad \text{with capacity } \infty, \text{ weight } -1 \text{ (if } x_i \le 1\text{; omit if } x_i \text{ is unbounded!)}.$$
  5. **RHS Supply/Demand $b_i = c_i - c_{i-1}$**:
     - If $c_i - c_{i-1} > 0$, connect $S \to i$ with capacity $c_i - c_{i-1}$ and weight $0$.
     - If $c_i - c_{i-1} < 0$, connect $i \to T$ with capacity $c_{i-1} - c_i$ and weight $0$.
  Run Maximum-Cost Max-Flow from $S$ to $T$; the maximum cost is the exact minimum tower construction cost!

---

#### Compilation 2: DAG Longest-Path Crashing / Project Compression (`PERT/CPM 工期压缩`)

- **Problem Statement**: A project consists of $n$ milestones $1, \dots, n$ (with start milestone $1$ and completion milestone $n$) and $m$ directed tasks $(u, v) \in E$. Normally, task $(u, v)$ takes $w_{uv}$ days, meaning milestone timestamps $\pi_1, \dots, \pi_n$ must satisfy $\pi_v - \pi_u \ge w_{uv}$. You can pay $c_{uv}$ dollars per day to "crash" (shorten) task $(u, v)$ by $z_{uv} \in [0, d_{uv}]$ days, reducing its duration to $w_{uv} - z_{uv}$. What is the minimum total cost to finish the project within $T$ days ($\pi_n - \pi_1 \le T$)?
- **Step 1 (Diagnostic Signal)**:
  The decision variables are milestone completion times $\pi_v$ and task compression amounts $z_{uv}$, coupled by difference inequalities $\pi_v - \pi_u \ge w_{uv} - z_{uv}$.
- **Step 2 (Intermediate Algebraic Representation)**:
  Write the Primal LP in minimization form:
  $$\begin{aligned}
  \text{Minimize} \quad & \sum_{(u, v) \in E} c_{uv} z_{uv} \\
  \text{subject to} \quad & \pi_v - \pi_u + z_{uv} \ge w_{uv} \quad && \forall (u, v) \in E \quad (\text{dual flow variable } f_{uv} \ge 0), \\
  & \pi_1 - \pi_n \ge -T \quad && \text{(makespan bound } \pi_n - \pi_1 \le T \implies \text{dual variable } F \ge 0\text{)}, \\
  & -z_{uv} \ge -d_{uv} \quad && \forall (u, v) \in E \quad (\text{max compression bound } z_{uv} \le d_{uv} \implies \text{dual variable } y_{uv} \ge 0), \\
  & z_{uv} \ge 0, \quad \pi_v \in \mathbb{R}.
  \end{aligned}$$
  Take the Dual LP mechanically:
  - For each unrestricted variable $\pi_v \in \mathbb{R}$, its dual constraint is an **equality** ($= 0$, since $\pi_v$ has coefficient $0$ in the Primal objective):
    $$\begin{aligned}
    \sum_{u : (u, v) \in E} f_{uv} - \sum_{w : (v, w) \in E} f_{vw} &= \begin{cases} -F & \text{if } v = 1, \\ +F & \text{if } v = n, \\ 0 & \text{otherwise.} \end{cases}
    \end{aligned}$$
    That is literally **flow conservation for an $s$-$t$ flow of total volume $F$ from $1$ to $n$**!
  - For each non-negative variable $z_{uv} \ge 0$, its column has $+1$ in the $(u, v)$ row and $-1$ in the $-z_{uv} \ge -d_{uv}$ row, and objective coefficient $c_{uv}$:
    $$f_{uv} - y_{uv} \le c_{uv} \quad \Longleftrightarrow \quad y_{uv} \ge f_{uv} - c_{uv}.$$
  - The Dual Objective to **Maximize** is:
    $$\text{Maximize} \quad \sum_{(u, v) \in E} w_{uv} f_{uv} - T \cdot F - \sum_{(u, v) \in E} d_{uv} y_{uv}.$$
- **Step 3 (Reverse-Engineering Scratchpad — Splitting Dual Flow into Two Parallel Edges)**:
  Look closely at the constraint $y_{uv} \ge \max(0, f_{uv} - c_{uv})$ with penalty $-d_{uv} y_{uv}$ in the Dual Objective!
  For each task $(u, v) \in E$:
  - As long as the flow $f_{uv}$ on $(u, v)$ obeys $0 \le f_{uv} \le c_{uv}$, we can set $y_{uv} = 0$ and pay **zero** $d_{uv}$-penalty! Each unit of flow earns $+w_{uv}$.
  - Once $f_{uv} > c_{uv}$, each additional unit of flow $f^{(2)}_{uv} = f_{uv} - c_{uv} \ge 0$ forces $y_{uv}$ to increase by $1$, so its net reward per unit of flow drops from $w_{uv}$ to $w_{uv} - d_{uv}$!
  Therefore, we split each flow variable $f_{uv} = f^{(1)}_{uv} + f^{(2)}_{uv}$ into **two parallel directed edges from $u$ to $v$**:
  1. **Edge 1 (Crashable regime)**: $u \to v$ with **capacity $c_{uv}$** and **cost $-w_{uv}$** (reward $+w_{uv}$).
  2. **Edge 2 (Uncrashable / Rigid regime)**: $u \to v$ with **capacity $\infty$** and **cost $-(w_{uv} - d_{uv})$** (reward $+w_{uv} - d_{uv}$).
  3. **Return / Source-Sink limit**: Send flow $F \ge 0$ from $1$ to $n$ at per-unit cost $+T$ (i.e., add a return edge $n \to 1$ with capacity $\infty$ and cost $+T$, or stop SSP when the shortest augmenting path from $1$ to $n$ has cost $\ge -T$).
  Run **Min-Cost Circulation** (eliminating negative cycles, or since the task graph is a DAG, using topological potentials + SSP while path cost $< -T$); the negated min cost is the exact minimum crashing cost!

---

#### Compilation 3: Tree Edge-Weight Modification (`[SHOI2004] 最小生成树` / `Luogu P4412` / `BZOJ 3118 Orz the Immortal`)

- **Problem Statement**: Given an undirected connected graph $G = (V, E)$ with initial edge weights $w_e$ and modification costs $c_e$ (or separate costs $a_e$ to increase $w_e$ and $b_e$ to decrease $w_e$), and a designated spanning tree $T \subset E$. You may modify each edge's weight $w_e \mapsto w'_e$. Find the minimum total modification cost so that $T$ becomes a Minimum Spanning Tree of $G$ under $w'$.
- **Step 1 (Diagnostic Signal)**:
  By the **Cut/Cycle Optimality Criterion for MST**, a spanning tree $T$ is an MST under weights $w'$ if and only if for every non-tree edge $e_{\text{out}} = (u, v) \in E \setminus T$ and every tree edge $e_{\text{in}} \in P_T(u, v)$ on the unique path between $u$ and $v$ in $T$,
  $$w'(e_{\text{in}}) \le w'(e_{\text{out}}).$$
  Because it never helps to *increase* a tree edge's weight or *decrease* a non-tree edge's weight, we set:
  - $w'(e_{\text{in}}) = w(e_{\text{in}}) - x_{e_{\text{in}}}$ with $x_{e_{\text{in}}} \ge 0$ (cost $b_{e_{\text{in}}} x_{e_{\text{in}}}$ to decrease tree edge $e_{\text{in}}$),
  - $w'(e_{\text{out}}) = w(e_{\text{out}}) + x_{e_{\text{out}}}$ with $x_{e_{\text{out}}} \ge 0$ (cost $a_{e_{\text{out}}} x_{e_{\text{out}}}$ to increase non-tree edge $e_{\text{out}}$).
- **Step 2 (Intermediate Algebraic Representation)**:
  For every pair $(e_{\text{in}}, e_{\text{out}})$ where $e_{\text{in}} \in P_T(e_{\text{out}})$:
  $$w(e_{\text{in}}) - x_{e_{\text{in}}} \le w(e_{\text{out}}) + x_{e_{\text{out}}} \quad \Longleftrightarrow \quad x_{e_{\text{in}}} + x_{e_{\text{out}}} \ge w(e_{\text{in}}) - w(e_{\text{out}}).$$
  Define $D(e_{\text{in}}, e_{\text{out}}) = \max\big(0, w(e_{\text{in}}) - w(e_{\text{out}})\big)$. Our Primal LP is:
  $$\begin{aligned}
  \text{Minimize} \quad & \sum_{e_{\text{in}} \in T} b_{e_{\text{in}}} x_{e_{\text{in}}} + \sum_{e_{\text{out}} \notin T} a_{e_{\text{out}}} x_{e_{\text{out}}} \\
  \text{subject to} \quad & x_{e_{\text{in}}} + x_{e_{\text{out}}} \ge D(e_{\text{in}}, e_{\text{out}}) \quad \forall e_{\text{out}} \notin T, \; \forall e_{\text{in}} \in P_T(e_{\text{out}}), \\
  & x_e \ge 0 \quad \forall e \in E.
  \end{aligned}$$
  *(Notice that if we negate the non-tree variables $\pi_{e_{\text{out}}} = -x_{e_{\text{out}}} \le 0$ and keep $\pi_{e_{\text{in}}} = x_{e_{\text{in}}} \ge 0$, every constraint is a pure difference $\pi_{e_{\text{in}}} - \pi_{e_{\text{out}}} \ge D(e_{\text{in}}, e_{\text{out}})$ on a bipartite graph between $T$ and $E \setminus T$!)*
  Taking the Dual LP with dual variables $f(e_{\text{in}}, e_{\text{out}}) \ge 0$:
  $$\begin{aligned}
  \text{Maximize} \quad & \sum_{e_{\text{out}} \notin T} \sum_{e_{\text{in}} \in P_T(e_{\text{out}})} D(e_{\text{in}}, e_{\text{out}}) f(e_{\text{in}}, e_{\text{out}}) \\
  \text{subject to} \quad & \sum_{e_{\text{out}} : e_{\text{in}} \in P_T(e_{\text{out}})} f(e_{\text{in}}, e_{\text{out}}) \le b_{e_{\text{in}}} \quad && \forall e_{\text{in}} \in T, \\
  & \sum_{e_{\text{in}} \in P_T(e_{\text{out}})} f(e_{\text{in}}, e_{\text{out}}) \le a_{e_{\text{out}}} \quad && \forall e_{\text{out}} \in E \setminus T, \\
  & f(e_{\text{in}}, e_{\text{out}}) \ge 0.
  \end{aligned}$$
- **Step 3 (Reverse-Engineering Scratchpad — Bipartite Max-Cost Flow)**:
  The Dual LP is immediately a **Maximum-Weight Bipartite $b$-Matching / Max-Cost Flow**!
  1. **Left vertices**: Tree edges $e_{\text{in}} \in T$, with edges from super-source $S \to e_{\text{in}}$ of capacity $b_{e_{\text{in}}}$ and cost $0$.
  2. **Right vertices**: Non-tree edges $e_{\text{out}} \in E \setminus T$, with edges to super-sink $e_{\text{out}} \to T_{\text{snk}}$ of capacity $a_{e_{\text{out}}}$ and cost $0$.
  3. **Cross edges**: For each $e_{\text{out}} \in E \setminus T$ and each $e_{\text{in}} \in P_T(e_{\text{out}})$ with $w(e_{\text{in}}) > w(e_{\text{out}})$, add a directed edge $e_{\text{in}} \to e_{\text{out}}$ with capacity $\infty$ and cost $-\big(w(e_{\text{in}}) - w(e_{\text{out}})\big)$ (or reward $+D(e_{\text{in}}, e_{\text{out}})$).
  4. *(And if all modification costs are equal $a_e = b_e = 1$, capacity $1$ on both sides reduces the problem to standard **Bipartite Minimum Weighted Vertex Cover / Kuhn–Munkres Algorithm**!)*

---

### 36.6 Step 4 — Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### 1. Hand-Checkable Toy Trace (`[ZJOI2013] 防守战线` on $n = 3$)

Suppose $n = 3$ positions with tower costs $c = [4, 2, 5]$ (and $x_i \ge 0$ unbounded for simplicity).
We have $m = 2$ interval requirements:
- Interval $1$: $[1, 2]$ needs $d_1 = 3$ towers ($x_1 + x_2 \ge 3$).
- Interval $2$: $[2, 3]$ needs $d_2 = 4$ towers ($x_2 + x_3 \ge 4$).

Let us check the optimal primal solution by hand:
- Putting $x_2 = 4$ at position $2$ satisfies both intervals ($x_1 + x_2 = 4 \ge 3$ and $x_2 + x_3 = 4 \ge 4$) at total cost $4 \times c_2 = 4 \times 2 = 8$. Can we do better? Since $x_2 + x_3 \ge 4$ and $c_2 = 2 < c_3 = 5$, any feasible solution costs at least $2(x_2 + x_3) \ge 8$. So **$\text{OPT}_{\text{Primal}} = 8$**.

Now let us trace the **Dual MCMF Network** on vertices $\{1, 2, 3, 4\}$ with $c_0 = c_4 = 0$:
- RHS supplies $b_i = c_i - c_{i-1}$:
  - $b_1 = c_1 - c_0 = 4 - 0 = +4 \implies S \to 1$ with capacity $4$, cost $0$.
  - $b_2 = c_2 - c_1 = 2 - 4 = -2 \implies 2 \to T$ with capacity $2$, cost $0$.
  - $b_3 = c_3 - c_2 = 5 - 2 = +3 \implies S \to 3$ with capacity $3$, cost $0$.
  - $b_4 = c_4 - c_3 = 0 - 5 = -5 \implies 4 \to T$ with capacity $5$, cost $0$.
  *(Check balance: total supply from $S$ is $4 + 3 = 7$; total demand into $T$ is $2 + 5 = 7$!)*
- Slack edges $i \to i+1$ with capacity $\infty$, reward $0$: $1 \to 2$, $2 \to 3$, $3 \to 4$.
- Interval edges $l_j \to r_j + 1$ with capacity $\infty$, reward $+d_j$:
  - Interval $1$ ($[1, 2]$): edge $1 \to 3$ with reward $+3$.
  - Interval $2$ ($[2, 3]$): edge $2 \to 4$ with reward $+4$.

Let us find the Maximum-Reward Flow of volume $7$ from $S$ to $T$:
- Note that vertex $2$ receives at most $4$ units of flow from $1 \to 2$, and vertex $2 \to T$ must absorb $2$ units of flow if $2 \to 4$ is saturated! Wait: at vertex $1$, $4$ units arrive from $S$. If $1$ sends $2$ units to $2$ along $1 \to 2$ (reward $0$) and $2$ units to $2$ more along $1 \to 2$... wait: $1$ sends all $4$ units along $1 \to 2$ (reward $0$). At vertex $2$: $2$ units go to $T$ ($2 \to T$, cap $2$), and the remaining $2$ units go along $2 \to 4$ (Interval 2, reward $+4 \times 2 = 8$) or $2 \to 3$!
- Wait: what about the $3$ units entering vertex $3$ from $S \to 3$? Can they use Interval 2 ($2 \to 4$)? No, because Interval 2 starts at vertex $2$, not vertex $3$, and slack edges only go forward $2 \to 3$, not backward $3 \to 2$!
-Wait—why did $2 \to 4$ only get $2$ units of flow in that attempt? Because in our trace, $b_2 = c_2 - c_1 = -2$ went to $T$, leaving only $4 - 2 = 2$ units at vertex $2$! Wait: why did $2$ units go to $2 \to T$? Because $S \to 3$ supplied $3$ units at vertex $3$, which had to go $3 \to 4 \to T$ (reward $0$), leaving only $5 - 3 = 2$ units of capacity on $4 \to T$ for edge $2 \to 4$!
- **Wait a second!** Why did that give reward $4 \times 2 = 8$? Because $8$ **IS** the exact optimal value $\text{OPT}_{\text{Primal}} = 8$! Look at the dual variables: $f_1 = 0$ on $1 \to 3$, and $f_2 = 2$ on $2 \to 4$, giving total dual objective $d_1 f_1 + d_2 f_2 = 3(0) + 4(2) = 8 = \text{OPT}_{\text{Primal}}$! Every unit of flow and every capacity bound matched $\text{OPT} = 8$ to the last integer!

#### 2. Three Broken Gadget Counterexamples (What Fails When Rules Are Violated)

```
BROKEN GADGET 1: Omitting the Slack Edges i -> i+1 (or Monotonicity pi_i - pi_{i-1} >= 0)
  In the Toy Trace above, if we omit the zero-cost slack edge 1 -> 2, then flow entering
  at S -> 1 (4 units) is FORCED to take interval edge 1 -> 3, even when interval 1 is
  already satisfied by position 2! Algebraically, omitting s_i >= 0 turns the inequality
  sum_{j: i in [l_j, r_j]} f_j <= c_i into an EQUALITY = c_i, allowing primal variables
  x_i to become NEGATIVE (building -1 towers at position 1 to harvest $4 refund!).

BROKEN GADGET 2: Reversing the Interval Edge Orientation (r_j + 1 -> l_j instead of l_j -> r_j + 1)
  If you orient the interval edge backward (r_j + 1 -> l_j) while keeping b_i = c_i - c_{i-1},
  the column for f_j has -1 at l_j and +1 at r_j + 1, which corresponds to -f_j >= 0
  (i.e. f_j <= 0). Since interval edges have capacity infinity and positive reward +d_j,
  reversed edges create a POSITIVE-WEIGHT CYCLE 1 -> 2 -> 3 -> 1 with slack edges
  i -> i+1, driving the Dual LP to +infinity!

BROKEN GADGET 3: Mixing Min-Max Sign Conventions on Capacity Bounds (f_{uv} <= u_{uv})
  In Primal Minimization, an upper bound x_i <= 1 is -x_i >= -1, which contributes -1 * g_i
  (a PENALTY) to the Dual Maximization objective. A common contest bug is writing +1 * g_i
  in the Dual objective (edge cost +1 instead of -1 in Max-Cost Flow), which rewards
  violating the capacity bound and drives g_i -> +infinity!
```

---

## Iteration 37: Complementary Slackness (`互补松弛定理`) & Reconstructing Optimal Dual Potentials from Residual Graphs

### 37.1 Step 1 — The Non-Graph Diagnostic Signal (When You Need the Dual Variables Back)

In Iteration 36, we used Strong LP Duality ($\min c^T x = \max b^T y$) to compute the **optimal objective value** of a potential-modification or inverse optimization problem by running MCMF on its dual network.

However, a large class of advanced contest problems (`[SHOI2004] 最小生成树` output extension, Inverse Shortest Path problems, price-setting / toll-optimization problems, and `[省选联考 2020] 魔法商店`) go one crucial step further:
> **"Do not merely output the minimum total cost—output the explicit optimal potentials $\pi_1^*, \dots, \pi_n^*$ (or the explicit modified edge weights $w'_e$)!"**

At first glance, this looks terrifying: we never solved the Primal LP in variables $\pi_v$; we transformed the problem into a Dual MCMF network and found an optimal flow $f^*$! How do we recover the optimal variables $\pi^*$ of the original problem from the flow solver's residual network $G_{f^*}$?

The answer lies in the **Primal–Dual Complementary Slackness Theorem (`互补松弛定理`)** and the **Residual Shortest-Path Potential Theorem**.

---

### 37.2 Step 2 — Mathematical Statement & Proof of Complementary Slackness for MCMF

#### 1. General LP Complementary Slackness Theorem

Let $x \in \mathbb{R}^n$ be feasible for the Primal LP ($\min c^T x$ subject to $Ax \ge b, x \ge 0$) and $y \in \mathbb{R}^m$ be feasible for the Dual LP ($\max b^T y$ subject to $A^T y \le c, y \ge 0$). Recall the chain of inequalities from Section 36.2:
$$b^T y = \sum_{i=1}^m b_i y_i \le \sum_{i=1}^m \left(\sum_{j=1}^n A_{i,j} x_j\right) y_i = \sum_{j=1}^n \left(\sum_{i=1}^m A_{i,j} y_i\right) x_j \le \sum_{j=1}^n c_j x_j = c^T x.$$

**Theorem 37.1 (LP Complementary Slackness)**:
Feasible solutions $x$ and $y$ are both optimal ($c^T x = b^T y$) if and only if both inequalities in the chain hold with equality. Since every term $\big((Ax)_i - b_i\big) y_i \ge 0$ and $\big(c_j - (A^T y)_j\big) x_j \ge 0$ is non-negative, their sum is zero if and only if every individual product is zero:
1. **Primal Slackness**: For every $i \in \{1, \dots, m\}$,
   $$y_i > 0 \implies \sum_{j=1}^n A_{i,j} x_j = b_i \qquad \text{and} \qquad \sum_{j=1}^n A_{i,j} x_j > b_i \implies y_i = 0.$$
2. **Dual Slackness**: For every $j \in \{1, \dots, n\}$,
   $$x_j > 0 \implies \sum_{i=1}^m A_{i,j} y_i = c_j \qquad \text{and} \qquad \sum_{i=1}^m A_{i,j} y_i < c_j \implies x_j = 0.$$

In plain words: **whenever a variable in one LP is strictly positive, its corresponding inequality in the other LP must be tight (hold with exact equality); whenever an inequality in one LP is strictly loose (has positive slack), its corresponding dual variable in the other LP must be zero!**

#### 2. Specialization to Min-Cost Flow and Dual Potentials

Now apply Theorem 37.1 to the Primal–Dual pair from Section 36.4:
- **Primal (Min-Cost Flow)**: Minimize $\sum_{(u,v) \in E} c(u, v) f(u, v)$ subject to $\text{in}_f(v) - \text{out}_f(v) = b_v$ and $-f(u, v) \ge -u(u, v)$, $f(u, v) \ge 0$.
- **Dual (Elastic Potentials)**: Maximize $\sum_{v \in V} b_v \pi(v) - \sum_{(u,v) \in E} u(u, v) z(u, v)$ subject to $\pi(v) - \pi(u) - z(u, v) \le c(u, v)$ and $z(u, v) \ge 0$.

Define the **reduced cost (`残量网络约化费用`)** of edge $e = (u, v) \in E$ with respect to potentials $\pi : V \to \mathbb{R}$ as:
$$c_\pi(u, v) := c(u, v) + \pi(u) - \pi(v).$$
Notice that the dual constraint $\pi(v) - \pi(u) - z(u, v) \le c(u, v)$ together with $z(u, v) \ge 0$ can be written as:
$$z(u, v) \ge -c_\pi(u, v) \quad \text{and} \quad z(u, v) \ge 0 \quad \Longleftrightarrow \quad z(u, v) \ge \max\big(0, -c_\pi(u, v)\big).$$

Let us write out the two Complementary Slackness conditions for each edge $e = (u, v) \in E$:
1. **Dual Slackness on Primal Flow $f(u, v) \ge 0$**:
   $$f(u, v) > 0 \implies \pi(v) - \pi(u) - z(u, v) = c(u, v) \Longleftrightarrow z(u, v) = -c_\pi(u, v).$$
   Since $z(u, v) \ge 0$, having $f(u, v) > 0$ immediately requires $-c_\pi(u, v) \ge 0$, i.e., **$c_\pi(u, v) \le 0$**!
2. **Primal Slackness on Dual Elastic Variable $z(u, v) \ge 0$** (corresponding to $-f(u, v) \ge -u(u, v)$):
   $$f(u, v) < u(u, v) \implies z(u, v) = 0.$$
   Since $z(u, v) \ge -c_\pi(u, v)$, having $z(u, v) = 0$ immediately requires $-c_\pi(u, v) \le 0$, i.e., **$c_\pi(u, v) \ge 0$**!

Combining these two implications gives the fundamental **MCMF Complementary Slackness Theorem**:

> [!IMPORTANT]
> **Theorem 37.2 (MCMF Complementary Slackness & Reduced Cost Trichotomy)**
> A feasible flow $f$ and node potentials $\pi : V \to \mathbb{R}$ (with optimal elastic slacks $z(u, v) = \max(0, -c_\pi(u, v))$) are simultaneously optimal for the Primal MCMF and Dual Potential LP if and only if for every edge $e = (u, v) \in E$:
> 1. **Positive Flow Implies Non-Positive Reduced Cost**:
>    $$f(u, v) > 0 \implies c_\pi(u, v) = c(u, v) + \pi(u) - \pi(v) \le 0, \quad \text{and} \quad z(u, v) = -c_\pi(u, v).$$
> 2. **Unsaturated Capacity Implies Non-Negative Reduced Cost**:
>    $$f(u, v) < u(u, v) \implies c_\pi(u, v) = c(u, v) + \pi(u) - \pi(v) \ge 0, \quad \text{and} \quad z(u, v) = 0.$$
> 3. **Strictly Unsaturated Flow Implies Zero Reduced Cost**:
>    $$0 < f(u, v) < u(u, v) \implies c_\pi(u, v) = c(u, v) + \pi(u) - \pi(v) = 0, \quad \text{and} \quad z(u, v) = 0.$$

---

### 37.3 Step 3 — Practical CP Extraction Contract: Reconstructing $\pi^*(v)$ and $z^*(u, v)$ from the Final Residual Graph $G_f$

Why is Theorem 37.2 so easy to use in code? Let us look at the **residual network $G_f = (V, E_f)$** of an optimal flow $f$:
- Whenever $f(u, v) < u(u, v)$, the **forward residual edge** $u \to v$ is present in $E_f$ with residual cost $c_f(u, v) = +c(u, v)$. Condition 2 ($f(u,v) < u(u,v) \implies c(u,v) + \pi(u) - \pi(v) \ge 0$) is equivalent to:
  $$\pi(v) - \pi(u) \le c_f(u, v) \quad \text{for every forward residual edge } (u, v) \in E_f.$$
- Whenever $f(u, v) > 0$, the **reverse residual edge** $v \to u$ is present in $E_f$ with residual cost $c_f(v, u) = -c(u, v)$. Condition 1 ($f(u,v) > 0 \implies c(u,v) + \pi(u) - \pi(v) \le 0$) can be negated as $-c(u,v) + \pi(v) - \pi(u) \ge 0$, which is equivalent to:
  $$\pi(u) - \pi(v) \le c_f(v, u) \quad \text{for every reverse residual edge } (v, u) \in E_f.$$

Look at those two inequalities together:
$$\forall (x, y) \in E_f \quad (\text{both forward and reverse residual edges}): \qquad \pi(y) - \pi(x) \le c_f(x, y)!$$
That is the **triangle inequality for shortest-path distances in the final residual graph $G_f$**!

#### Algorithmic Contract: Reconstructing Optimal Integer Dual Variables

Assume you have solved the Dual MCMF problem and obtained the final residual network $G_f = (V, E_f)$ (which has no negative-cost directed cycles because $f$ is optimal):

1. **If your MCMF solver maintains Johnson potentials $\pi(v)$**:
   Wait—be careful! In Successive Shortest Path (SSP) with Dijkstra, you update $\pi(v) \gets \pi(v) + d_{G_f}(S, v)$ *before* pushing flow along the shortest path, and after the final augmentation you stop when $T$ is no longer reachable or when maximum flow is reached. At the moment the algorithm terminates, the last potential array $\pi(v)$ satisfies $\pi(y) - \pi(x) \le c_f(x, y)$ on all edges explored before the last augmentation, **except possibly the reverse edges newly created by the very last augmentation** if you didn't run one final distance update, or vertices unreachable from $S$ in $G_f$!
2. **The Foolproof Reconstruction Procedure (1-Run SPFA / Johnson Update on Final $G_f$)**:
   To guarantee that $\pi(y) - \pi(x) \le c_f(x, y)$ holds for **every** residual edge $(x, y) \in E_f$ across all connected components after the final flow augmentation:
   - Create a virtual super-node $Q$ connected to every vertex $v \in V$ with a zero-cost directed edge $Q \to v$ of cost $0$ (or simply initialize `dist[v] = 0` for all $v \in V$ and push all $v \in V$ into the SPFA queue on $G_f$, where an edge $(x, y) \in E_f$ is active iff its residual capacity is $> 0$).
   - Because $f$ is an optimal circulation/flow, $G_f$ has **zero negative cycles**, so SPFA terminates in $O(VE)$ and computes `dist[v]` satisfying `dist[y] - dist[x] <= c_f(x, y)` for every active residual edge $(x, y) \in E_f$.
   - If a specific reference vertex $\pi_0$ must equal $0$, shift all potentials by subtracting `dist[0]`:
     $$\pi^*(v) = \text{dist}[v] - \text{dist}[0].$$
   - Reconstruct every optimal elastic slack variable $z^*(u, v)$ directly from $\pi^*$:
     $$z^*(u, v) = \max\big(0, \pi^*(v) - \pi^*(u) - c(u, v)\big).$$
   - Because all initial edge costs $c(u, v)$ are integers, `dist[v]`, $\pi^*(v)$, and $z^*(u, v)$ are **guaranteed to be exact integers**!

---

### 37.4 Complete 4-Step Worked Reconstruction: Inverse MST (`[SHOI2004] 最小生成树` / `Luogu P4412`)

Let us demonstrate how Complementary Slackness reconstructs the exact modified edge weights $w'_e$ in the **Inverse MST problem** (`[SHOI2004] 最小生成树`, and its weighted generalization `[BZOJ 3118] Orz the Immortal`).

- **Problem Setup**: Given a connected graph $G = (V, E)$ with initial integer weights $w_e$ and modification cost $c_e$ per unit change, and a target spanning tree $T$. We want to find modified weights $w'_e$ minimizing $\sum_{e \in E} c_e |w'_e - w_e|$ such that $T$ is an MST under $w'$, and **output both the minimum cost and the modified weights $w'_e$**.
- **Step 1 (Primal & Dual Formulation)**:
  As derived in Section 36.5 (Compilation 3), we decrease tree edges $e_{\text{in}} \in T$ by $x_{e_{\text{in}}} \ge 0$ ($w'_{e_{\text{in}}} = w_{e_{\text{in}}} - x_{e_{\text{in}}}$) and increase non-tree edges $e_{\text{out}} \notin T$ by $x_{e_{\text{out}}} \ge 0$ ($w'_{e_{\text{out}}} = w_{e_{\text{out}}} + x_{e_{\text{out}}}$).
  Let us write this in our canonical difference-constraint form by setting:
  - For $e_{\text{in}} \in T$: $\pi(e_{\text{in}}) = -x_{e_{\text{in}}} \le 0$ (or equivalently, connect $S \to e_{\text{in}}$ with capacity $c_{e_{\text{in}}}$, cost $0$).
  - For $e_{\text{out}} \notin T$: $\pi(e_{\text{out}}) = +x_{e_{\text{out}}} \ge 0$ (connect $e_{\text{out}} \to T_{\text{snk}}$ with capacity $c_{e_{\text{out}}}$, cost $0$).
  Let us trace the exact residual edges in our Min-Cost Flow network (where we negate rewards so edge $e_{\text{in}} \to e_{\text{out}}$ has capacity $\infty$ and cost $-D(e_{\text{in}}, e_{\text{out}}) = -\max(0, w(e_{\text{in}}) - w(e_{\text{out}}))$, and we add a zero-cost edge $T_{\text{snk}} \to S$ of capacity $\infty$ to make it a Min-Cost Circulation):
  1. Edge $S \to e_{\text{in}}$ has capacity $c_{e_{\text{in}}}$ and cost $0$. Its elastic slack is $z(S, e_{\text{in}}) = x_{e_{\text{in}}} \ge 0$!
  2. Edge $e_{\text{out}} \to T_{\text{snk}}$ has capacity $c_{e_{\text{out}}}$ and cost $0$. Its elastic slack is $z(e_{\text{out}}, T_{\text{snk}}) = x_{e_{\text{out}}} \ge 0$!
  3. Edge $e_{\text{in}} \to e_{\text{out}}$ has capacity $\infty$ and cost $-D(e_{\text{in}}, e_{\text{out}})$. Since its capacity is $\infty$, its elastic slack $z(e_{\text{in}}, e_{\text{out}})$ must be $0$, which enforces:
     $$\pi(e_{\text{out}}) - \pi(e_{\text{in}}) \le -D(e_{\text{in}}, e_{\text{out}}) \quad \Longleftrightarrow \quad \pi(e_{\text{in}}) - \pi(e_{\text{out}}) \ge D(e_{\text{in}}, e_{\text{out}}).$$
- **Step 2 (Extracting $x^*_{e_{\text{in}}}$ and $x^*_{e_{\text{out}}}$ from Residual Potentials $\pi$)**:
  After finding the minimum-cost circulation (or running MCMF from $S$ to $T_{\text{snk}}$ while path cost $< 0$) and computing valid potentials $\pi$ on the final residual graph $G_f$ with $\pi(S) = \pi(T_{\text{snk}}) = 0$:
  - For each $e_{\text{in}} \in T$: since $(S, e_{\text{in}})$ has cost $0$, the elastic slack is $z(S, e_{\text{in}}) = \max(0, \pi(e_{\text{in}}) - \pi(S) - 0) = \max(0, \pi(e_{\text{in}}))$. Thus:
    $$x^*_{e_{\text{in}}} = \max\big(0, \pi(e_{\text{in}}) - \pi(S)\big), \qquad w'(e_{\text{in}}) = w(e_{\text{in}}) - x^*_{e_{\text{in}}}.$$
  - For each $e_{\text{out}} \notin T$: since $(e_{\text{out}}, T_{\text{snk}})$ has cost $0$, the elastic slack is $z(e_{\text{out}}, T_{\text{snk}}) = \max(0, \pi(T_{\text{snk}}) - \pi(e_{\text{out}}) - 0)$. Thus:
    $$x^*_{e_{\text{out}}} = \max\big(0, \pi(T_{\text{snk}}) - \pi(e_{\text{out}})\big), \qquad w'(e_{\text{out}}) = w(e_{\text{out}}) + x^*_{e_{\text{out}}}.$$
  - Let us double check! Since $e_{\text{in}} \to e_{\text{out}}$ has capacity $\infty$, it is never saturated, so the forward residual edge $e_{\text{in}} \to e_{\text{out}}$ of cost $-D(e_{\text{in}}, e_{\text{out}})$ is **always present** in $G_f$! Therefore, $\pi$ satisfies:
    $$\pi(e_{\text{out}}) - \pi(e_{\text{in}}) \le -D(e_{\text{in}}, e_{\text{out}}) \implies \big(\pi(e_{\text{in}}) - \pi(S)\big) + \big(\pi(T_{\text{snk}}) - \pi(e_{\text{out}})\big) \ge D(e_{\text{in}}, e_{\text{out}}) \quad (\text{when } \pi(S) = \pi(T_{\text{snk}})),$$
    which guarantees $x^*_{e_{\text{in}}} + x^*_{e_{\text{out}}} \ge D(e_{\text{in}}, e_{\text{out}})$ for every single pair!

---

### 37.5 Step 4 — Toy Trace & Failure Modes of Dual Reconstruction

#### 1. Hand-Checkable Toy Trace of Dual Reconstruction

Consider a triangle graph on $3$ vertices $\{1, 2, 3\}$:
- Tree $T$ consists of $e_1 = (1, 2)$ with weight $w(e_1) = 10$, cost $c(e_1) = 2$, and $e_2 = (2, 3)$ with weight $w(e_2) = 8$, cost $c(e_2) = 5$.
- Non-tree edge is $e_3 = (1, 3)$ with weight $w(e_3) = 6$, cost $c(e_3) = 3$.

Let us solve the Primal LP by hand first:
- $e_3$ forms a cycle with $e_1$ and $e_2$. We need:
  - $x_1 + x_3 \ge w(e_1) - w(e_3) = 10 - 6 = 4$,
  - $x_2 + x_3 \ge w(e_2) - w(e_3) = 8 - 6 = 2$,
  minimizing $2 x_1 + 5 x_2 + 3 x_3$.
- If we set $x_3 = 2$, then $x_2 \ge 0$ is satisfied ($x_2 = 0$), and we need $x_1 \ge 4 - 2 = 2$. Total cost: $2(2) + 5(0) + 3(2) = 4 + 0 + 6 = 10$.
- Can we do better? If $x_3 = 4, x_1 = x_2 = 0$, cost is $3(4) = 12$. If $x_3 = 0, x_1 = 4, x_2 = 2$, cost is $2(4) + 5(2) = 18$. So **$\text{OPT} = 10$ with $x^*_1 = 2, x^*_2 = 0, x^*_3 = 2$**, giving modified weights $w'(e_1) = 8, w'(e_2) = 8, w'(e_3) = 8$.

Now let us trace the **Dual MCMF Network & Residual Potential Reconstruction**:
- Capacities & costs:
  - $S \to e_1$ (cap $2$, cost $0$), $S \to e_2$ (cap $5$, cost $0$).
  - $e_3 \to T_{\text{snk}}$ (cap $3$, cost $0$).
  - $e_1 \to e_3$ (cap $\infty$, cost $-4$), $e_2 \to e_3$ (cap $\infty$, cost $-2$).
- **Optimal Flow**:
  - Push $2$ units along $S \to e_1 \to e_3 \to T_{\text{snk}}$ (cost $-4 \times 2 = -8$). Now $S \to e_1$ is saturated ($f = 2/2$).
  - Push $1$ unit along $S \to e_2 \to e_3 \to T_{\text{snk}}$ (cost $-2 \times 1 = -2$). Now $e_3 \to T_{\text{snk}}$ is saturated ($f = 3/3$), while $S \to e_2$ is **unsaturated** ($f = 1/5$).
  - Total min cost is $-8 - 2 = -10 \implies \text{OPT} = 10$.
- **Residual Graph $G_f$ Active Edges**:
  - From $S \to e_1$ (saturated $2/2$): only reverse edge $e_1 \to S$ (cost $0$).
  - From $S \to e_2$ (strictly unsaturated $1/5$): **both** forward $S \to e_2$ (cost $0$) and reverse $e_2 \to S$ (cost $0$)!
  - From $e_1 \to e_3$ (flow $2/\infty$): **both** forward $e_1 \to e_3$ (cost $-4$) and reverse $e_3 \to e_1$ (cost $+4$)!
  - From $e_2 \to e_3$ (flow $1/\infty$): **both** forward $e_2 \to e_3$ (cost $-2$) and reverse $e_3 \to e_2$ (cost $+2$)!
  - From $e_3 \to T_{\text{snk}}$ (saturated $3/3$): only reverse edge $T_{\text{snk}} \to e_3$ (cost $0$).
- **Evaluating Potentials $\pi$ via Tight 2-Way Residual Edges**:
  Set $\pi(S) = \pi(T_{\text{snk}}) = 0$.
  1. Since $S \leftrightarrow e_2$ has cost $0$ in both directions, Complementary Slackness forces $\pi(e_2) = \pi(S) = 0$!
  2. Since $e_2 \leftrightarrow e_3$ has cost $-2$ forward and $+2$ reverse, Complementary Slackness forces $\pi(e_3) = \pi(e_2) - 2 = -2$!
  3. Since $e_1 \leftrightarrow e_3$ has cost $-4$ forward and $+4$ reverse, Complementary Slackness forces $\pi(e_1) = \pi(e_3) + 4 = -2 + 4 = +2$!
- **Extracting $x^*$**:
  - $x^*_1 = \max(0, \pi(e_1) - \pi(S)) = \max(0, 2 - 0) = 2$.
  - $x^*_2 = \max(0, \pi(e_2) - \pi(S)) = \max(0, 0 - 0) = 0$.
  - $x^*_3 = \max(0, \pi(T_{\text{snk}}) - \pi(e_3)) = \max(0, 0 - (-2)) = 2$.
  The reconstructed primal variables $(x^*_1, x^*_2, x^*_3) = (2, 0, 2)$ match our hand calculation to perfection!

#### 2. Failure Modes in Dual Reconstruction

> [!WARNING]
> **Three Classic Pitfalls When Extracting Dual Potentials $\pi$ from MCMF**
> 1. **Using Pre-Augmentation Dijkstra Potentials Instead of Post-Augmentation Residual Distances**:
>    In standard SSP, you compute shortest paths `dist[v]` on $G_f$, and then push flow along a path $P$, which *saturates* at least one edge on $P$ and *creates new reverse edges*. If you stop immediately after pushing flow on the last augmenting path without running one final shortest-path / potential pass, the potentials from *before* the last augmentation might not reflect the newly created reverse edges if you stopped early! Always run one final SPFA / potential relaxation on $G_{f^*}$ after all flow augmentations are complete.
> 2. **Unreachable Vertices in $G_f$ (`dist[v] == INF`)**:
>    If you only run shortest paths from $S$ on $G_f$, any vertex $v$ separated from $S$ by a saturated cut will have `dist[v] = +INF`, which is NOT a valid finite potential! As specified in Section 37.3, either initialize `dist[v] = 0` for all $v \in V$ in a final SPFA pass, or add zero-cost edges from a super-root $Q \to v$ for all $v \in V$ so every vertex receives a finite integer potential satisfying all residual triangle inequalities.
> 3. **Forgetting to Tie $\pi(S) = \pi(T_{\text{snk}})$ When Stopping at Zero Cost**:
>    In problems like Inverse MST where we stop augmenting as soon as the shortest $S \to T_{\text{snk}}$ path has cost $\ge 0$ (equivalent to having an infinite-capacity return edge $T_{\text{snk}} \to S$ of cost $0$ and $S \to T_{\text{snk}}$ of cost $0$), you must include both zero-cost edges $S \leftrightarrow T_{\text{snk}}$ in $G_f$ when computing `dist[v]` so that $\pi(S) = \pi(T_{\text{snk}})$ holds!

---

## Iteration 38: Totally Unimodular (TU) Matrices, Hoffman–Kruskal Theorem & The Consecutive-Ones Property (`连续 1 性质`)

### 38.1 Step 1 — The Non-Graph Diagnostic Signal (When Does an ILP Compile to Flow?)

Every competitive programmer has experienced the following dilemma:
You translate a combinatorial optimization problem into an **Integer Linear Program (ILP)**:
$$\text{Minimize } c^T x \quad \text{subject to} \quad Ax \le b, \quad x \in \mathbb{Z}_{\ge 0}^n.$$
If you drop the integrality requirement $x \in \mathbb{Z}^n$ and solve the continuous LP relaxation (or map it to a flow network), two questions decide whether your solution gets `Accepted` or fails catastrophically:
1. **Zero Integrality Gap**: Does the continuous LP relaxation $\min \{c^T x : Ax \le b, x \ge 0\}$ guarantee an **exact integer optimal solution** $x^* \in \mathbb{Z}^n$ for every integer right-hand side $b \in \mathbb{Z}^m$ and every cost vector $c$?
2. **Mechanical Graph Compilation**: If the constraint matrix $A$ is not yet a directed graph incidence matrix (for instance, its entries are $0$ and $1$ representing intervals, grid lines, or tree paths), what exact matrix operation converts $Ax = b$ into a flow conservation system $M x = b'$ where every column of $M$ has at most one $+1$ and at most one $-1$?

The unified mathematical answer to both questions is the theory of **Totally Unimodular (TU) Matrices (`全幺模矩阵`)**.

---

### 38.2 Step 2 — Definitions, Closure Operations & The Hoffman–Kruskal Theorem

#### 1. Definition of Total Unimodularity

**Definition 38.1 (Totally Unimodular Matrix)**:
A matrix $A \in \mathbb{Z}^{m \times n}$ is **Totally Unimodular (TU)** if every square submatrix $B$ of $A$ (obtained by selecting any $k$ rows and any $k$ columns for any $1 \le k \le \min(m, n)$) has determinant
$$\det(B) \in \{-1, 0, +1\}.$$
*(In particular, taking $k = 1$ shows that every entry of a TU matrix must belong to $\{-1, 0, +1\}$.)*

#### 2. Algebraic Closure Properties of TU Matrices (The "TU Calculus")

How can we modify a TU matrix $A$ while preserving Total Unimodularity?
**Proposition 38.2 (TU Closure Operations)**: If $A$ is Totally Unimodular, then so are all of the following matrices:
1. **Transpose $A^T$**: Since $\det(B^T) = \det(B)$, **taking the LP Dual preserves Total Unimodularity**!
2. **Concatenation with Identity $[A \mid I_m]$ or $[A \mid -I_m]$**: Expanding the determinant along any column of $\pm I_m$ reduces the submatrix size by $1$ and multiplies the determinant by $\pm 1$. Consequently, **adding slack or surplus variables ($Ax + s = b$) or variable upper/lower bounds ($l \le x \le u$) preserves Total Unimodularity**!
3. **Multiplying any row or column by $-1$**: Changes the sign of $\det(B)$ by at most $\pm 1$.
4. **Permuting or duplicating any rows or columns**: Permuting changes signs by $\pm 1$; duplicating a row/column makes any submatrix containing both copies have $\det = 0$.
5. **Pivoting on any non-zero entry $\pm 1$**: Preserve unimodularity of basis determinants.

#### 3. Statement and Proof of the Hoffman–Kruskal Theorem (1956)

**Theorem 38.3 (Hoffman–Kruskal Theorem)**:
Let $A \in \mathbb{Z}^{m \times n}$ be an integral matrix. The following three statements are equivalent:
1. $A$ is Totally Unimodular ($\det(B) \in \{-1, 0, +1\}$ for every square submatrix $B$).
2. For every integral vector $b \in \mathbb{Z}^m$, the polyhedron $P(b) = \{x \in \mathbb{R}^n : Ax \le b, \; x \ge 0\}$ has **only integral vertices (extreme points)**.
3. For every integral vectors $b \in \mathbb{Z}^m$ and $l, u \in \mathbb{Z}^n$, the standard-form polyhedron $Q(b, l, u) = \{x \in \mathbb{R}^n : Ax = b, \; l \le x \le u\}$ has **only integral vertices**.

**Proof of $(1) \implies (2)$ and $(3)$ (The Sufficiency Direction Used in Contests)**:
Consider $Ax \le b, x \ge 0$ with $b \in \mathbb{Z}^m$. Introduce non-negative slack variables $s \in \mathbb{R}_{\ge 0}^m$ to obtain the standard equality system:
$$[A \mid I_m] \begin{pmatrix} x \\ s \end{pmatrix} = b, \qquad x \ge 0, \; s \ge 0.$$
By Proposition 38.2(2), since $A$ is TU, the augmented matrix $\tilde{A} = [A \mid I_m] \in \mathbb{Z}^{m \times (n+m)}$ is also TU, and has full row rank $m$.
By fundamental Linear Programming theory, every vertex (extreme point) of the polyhedron corresponds to a **basic feasible solution (BFS)**: partitioning the columns of $\tilde{A}$ into a nonsingular $m \times m$ basis matrix $B$ and non-basic columns $N$, setting the non-basic variables $z_N = 0$, and solving the $m \times m$ linear system
$$B z_B = b.$$
Since $B$ is a nonsingular $m \times m$ square submatrix of the TU matrix $\tilde{A}$, we have $\det(B) \in \{-1, +1\}$!
By **Cramer's Rule**, the $i$-th component of the basic variable vector $z_B = B^{-1} b$ is given by:
$$(z_B)_i = \frac{\det(B_i(b))}{\det(B)} = \pm \det(B_i(b)),$$
where $B_i(b)$ is obtained by replacing the $i$-th column of $B$ with the integer vector $b \in \mathbb{Z}^m$. Since $B$ and $b$ have exclusively integer entries, $\det(B_i(b)) \in \mathbb{Z}$, and dividing by $\det(B) = \pm 1$ proves that $(z_B)_i \in \mathbb{Z}$ for all $i$!
*(The converse $(2) \implies (1)$, proved by Hoffman and Kruskal and simplified by Veinott and Dantzig (1968), shows that if some square submatrix $B$ of $[A \mid I_m]$ has $|\det(B)| \ge 2$, then $B^{-1}$ contains a fractional entry; choosing an integer vector $y \ge 0$ plus a unit coordinate vector $e_i$ such that $b = B(y + e_i)$ makes $B^{-1} b = y + B^{-1} e_i$ a non-integral extreme point of $P(b)$.)* $\blacksquare$

---

### 38.3 The Ghouila–Houri Equitable Bicoloring Theorem (1962)

Testing $\det(B) \in \{-1, 0, +1\}$ across exponentially many square submatrices is impossible by hand. Fortunately, **Ghouila–Houri (1962)** discovered a clean combinatorial characterization of Total Unimodularity via **equitable row/column bicoloring (`行列二染色判定定理`)**.

**Theorem 38.4 (Ghouila–Houri Theorem)**:
A matrix $A \in \{-1, 0, +1\}^{m \times n}$ is Totally Unimodular if and only if for **every** subset of rows $R \subseteq \{1, \dots, m\}$ (or symmetrically, every subset of columns $C \subseteq \{1, \dots, n\}$), there exists a partition (2-coloring) of $R$ into two disjoint sets $R = R_+ \sqcup R_-$ (assigning signs $\sigma_i = +1$ for $i \in R_+$ and $\sigma_i = -1$ for $i \in R_-$) such that the signed row sum in every column $j \in \{1, \dots, n\}$ lies in $\{-1, 0, +1\}$:
$$\forall j \in \{1, \dots, n\}: \qquad \sum_{i \in R} \sigma_i A_{i,j} = \sum_{i \in R_+} A_{i,j} - \sum_{i \in R_-} A_{i,j} \in \{-1, 0, +1\}.$$
*(Note: In particular, if the sum of entries $\sum_{i \in R} |A_{i,j}|$ in column $j$ restricted to $R$ is even, then $\sum_{i \in R} \sigma_i A_{i,j}$ must be even and in $\{-1, 0, +1\}$, so it **must equal $0$**; if it is odd, it **must equal $\pm 1$**!)*

**Proof Sketch ($\implies$ and $\Longleftarrow$)**:
- *($\implies$ Necessity)*: Suppose $A$ is TU and let $R \subseteq \{1, \dots, m\}$ be any subset of rows. Let $A_R$ be the $|R| \times n$ submatrix of $A$ on rows $R$, and let $d = \mathbf{1}^T A_R$. Define the polytope of fractional row weightings $P = \{ y \in \mathbb{R}^{|R|} : -\mathbf{1} \le y \le \mathbf{1}, \; \lfloor d/2 \rfloor \le y^T A_R \le \lceil d/2 \rceil \}$ (or equivalently $z = (y + \mathbf{1})/2 \in [0, 1]^{|R|}$). Since $z = \frac{1}{2}\mathbf{1}$ satisfies $z^T A_R = \frac{1}{2} d$, which lies between $\lfloor d/2 \rfloor$ and $\lceil d/2 \rceil$, $P$ is non-empty! Because $A_R^T$ is TU, Hoffman–Kruskal guarantees an integral vertex $z^* \in \{0, 1\}^{|R|}$, so $\sigma = 2z^* - \mathbf{1} \in \{-1, +1\}^{|R|}$ satisfies $\frac{1}{2}(\sigma^T A_R + d) \in \{\lfloor d/2 \rfloor, \lceil d/2 \rceil\}$, meaning $\sigma^T A_R \in \{-1, 0, +1\}^n$!
- *($\Longleftarrow$ Sufficiency by Induction on Submatrix Size $k$)*: Suppose the bicoloring condition holds for all row subsets $R$. For $k = 1$, taking $|R| = 1$ gives $A_{i,j} \in \{-1, 0, +1\}$. Assume by induction that every $(k-1) \times (k-1)$ submatrix has determinant in $\{-1, 0, +1\}$, and let $B$ be a nonsingular $k \times k$ submatrix of $A$. By the induction hypothesis, the adjugate matrix $\text{adj}(B) = \det(B) B^{-1}$ has entries in $\{-1, 0, +1\}$. Let $r = |\det(B)| \ge 1$, and let $u = \text{adj}(B) e_1 \in \{-1, 0, +1\}^k$ be the first column of $\text{adj}(B)$, so $B^T u = \det(B) e_1 = (\pm r, 0, \dots, 0)^T$.
  Define the support row subset $R = \{i \in \{1, \dots, k\} : u_i \ne 0\} \ne \emptyset$. For every column $j \in \{2, \dots, k\}$, since $\sum_{i \in R} B_{i,j} u_i = 0$ and $u_i \in \{\pm 1\}$, the number of non-zero entries of column $j$ in $R$ is **even**; for column $1$, $\sum_{i \in R} B_{i,1} u_i = \pm r$.
  Now apply the Ghouila–Houri bicoloring to $R$: we obtain $\sigma \in \{-1, +1\}^R$ such that for $j \in \{2, \dots, k\}$ (even support), $\sum_{i \in R} \sigma_i B_{i,j} = 0$, and for $j = 1$, $\sum_{i \in R} \sigma_i B_{i,1} \in \{-1, 0, +1\}$.
  Extending $\sigma$ by $0$ outside $R$, we have $B^T \sigma = (\alpha, 0, \dots, 0)^T$ with $\alpha \in \{-1, 0, +1\}$. Since $B$ is nonsingular and $\sigma \ne 0$, we must have $\alpha = \pm 1$. Comparing $B^T u = (\pm r) e_1$ with $B^T \sigma = (\pm 1) e_1$ implies $u = \pm r \sigma$. Since both $u_i$ and $\sigma_i$ are in $\{\pm 1\}$ on $R$, we must have $r = |\det(B)| = 1$! $\blacksquare$

---

### 38.4 Step 3 — The Four Canonical TU Matrix Families in Competitive Programming

Using Theorem 38.4 and unimodular row operations, we can immediately classify the **four canonical families of Totally Unimodular matrices** that appear in competitive programming, and show how each compiles into a flow network!

---

#### Family 1: Directed Network Incidence Matrices (`有向图关联矩阵`)

- **Structure**: Every column $j$ of $A \in \{-1, 0, +1\}^{m \times n}$ contains **at most one $+1$ and at most one $-1$** (and all other entries in column $j$ are $0$).
- **Proof of Total Unimodularity (via Ghouila–Houri)**:
  For any subset of rows $R \subseteq \{1, \dots, m\}$, color every row in $R$ with the **same sign** $\sigma_i = +1$ ($R_+ = R, R_- = \emptyset$). Since each column $j$ has at most one $+1$ and at most one $-1$ in the entire matrix, the sum $\sum_{i \in R} (+1) A_{i,j}$ is automatically in $\{-1, 0, +1\}$!
- **Graph Compilation**:
  $A$ is **already** the vertex-arc incidence matrix of a directed graph $G = (V, E)$ on $m$ vertices (plus a dummy root vertex $0$ to absorb any column that has only a single $+1$ or only a single $-1$, so that every column has *exactly* one $+1$ and *exactly* one $-1$).
- **Dual Consequence**: By Proposition 38.2(1), the transpose $A^T$ (**Difference-Constraint Matrix**, where every *row* has at most one $+1$ and at most one $-1$, i.e., $\pi_v - \pi_u \le c_{uv}$) is also TU!

---

#### Family 2: Bipartite Undirected Incidence Matrices (`二分图无向关联矩阵`)

- **Structure**: $A \in \{0, 1\}^{m \times n}$ is the vertex-edge incidence matrix of an undirected graph $G = (V, E)$, where each column $j$ has two $+1$s corresponding to the endpoints $\{u, v\}$ of edge $e_j$.
- **Theorem 38.5**: The incidence matrix $A$ of an undirected graph $G$ is Totally Unimodular **if and only if $G$ is bipartite** (contains no odd cycles)!
- **Proof**:
  - *If $G = (L \sqcup R, E)$ is bipartite*: Multiply every row $i \in R$ by $-1$! Then every edge $e = (u, v)$ with $u \in L, v \in R$ now has $+1$ in row $u \in L$ and $-1$ in row $v \in R$. This reduces $A$ directly to **Family 1 (Directed Network Incidence Matrix)**!
  - *If $G$ contains an odd cycle $C_{2k+1} = (v_1, v_2, \dots, v_{2k+1})$*: Consider the $(2k+1) \times (2k+1)$ submatrix $B$ of $A$ formed by the vertices and edges of $C_{2k+1}$. Expanding $\det(B)$ along the first row gives two triangular submatrices whose determinants have the *same* sign for odd $2k+1$:
    $$\det\begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} = 1(1 - 0) + 1(1 - 0) = +2 \notin \{-1, 0, +1\}!$$
    And sure enough, on a triangle $C_3$, the Fractional Matching / Vertex Cover LP $\max \{x_1 + x_2 + x_3 : x_u + x_v \le 1\}$ has the unique fractional optimal vertex $x^* = (\frac{1}{2}, \frac{1}{2}, \frac{1}{2})$ of value $1.5$, whereas the integer maximum matching is $1$!

---

#### Family 3: Interval Matrices / The Consecutive-Ones Property (`连续 1 性质`)

- **Definition 38.6 (Consecutive-Ones Property)**:
  A $\{0, 1\}$-matrix $A \in \{0, 1\}^{m \times n}$ has the **Column Consecutive-Ones Property** if in every column $j \in \{1, \dots, n\}$, the $1$s appear in a **single contiguous interval of row indices** $[l_j, r_j]$:
  $$A_{i, j} = \begin{cases} 1 & \text{if } l_j \le i \le r_j, \\ 0 & \text{otherwise.} \end{cases}$$
  *(Symmetrically, $A$ has the **Row Consecutive-Ones Property** if $A^T$ has the Column Consecutive-Ones Property, i.e., in every row $i$, the $1$s appear in a contiguous interval of columns $[L_i, R_i]$.)*

> [!IMPORTANT]
> **Theorem 38.7 (Unimodular Compilation of Interval Matrices via the Difference Matrix $D$)**
> Every $\{0, 1\}$-matrix $A$ with the Column (or Row) Consecutive-Ones Property is **Totally Unimodular**, and any linear program with constraint matrix $A$ compiles mechanically into a **Min-Cost Flow network**!

**Proof & Mechanical Compilation into MCMF**:
1. Suppose $A \in \{0, 1\}^{m \times n}$ has the **Column Consecutive-Ones Property**, and consider the linear system (after adding slack/surplus variables $s \in \mathbb{R}_{\ge 0}^m$):
   $$A x - s = b \qquad (x \ge 0, \; s \ge 0).$$
   Append an $(m+1)$-th row of all zeros ($0 = 0$) at the bottom, and left-multiply the $(m+1)$-row system by the $(m+1) \times (m+1)$ lower bidiagonal **Consecutive-Difference Matrix $D$**:
   $$D = \begin{pmatrix}
   1 & 0 & 0 & \cdots & 0 \\
   -1 & 1 & 0 & \cdots & 0 \\
   0 & -1 & 1 & \cdots & 0 \\
   \vdots & \ddots & \ddots & \ddots & \vdots \\
   0 & \cdots & 0 & -1 & 1
   \end{pmatrix} \in \{-1, 0, +1\}^{(m+1) \times (m+1)}, \qquad \det(D) = 1.$$
   Look at what $D$ does to the $j$-th column of $A$ (which has $1$s on rows $l_j, l_j + 1, \dots, r_j$ and $0$s elsewhere):
   $$(DA)_{i, j} = A_{i, j} - A_{i-1, j} = \begin{cases}
   +1 & \text{if } i = l_j \quad (\text{where the } 1\text{s start}), \\
   -1 & \text{if } i = r_j + 1 \quad (\text{just after the } 1\text{s end}), \\
   0 & \text{for all other rows } i!
   \end{cases}$$
   Every interior $1$ at row $i \in [l_j + 1, r_j]$ cancels out ($1 - 1 = 0$)!
   Therefore, $DA$ has **exactly one $+1$ (at row $l_j$) and one $-1$ (at row $r_j + 1$)** in every column $j$—so $DA$ is a **Directed Network Incidence Matrix (Family 1)** on vertices $1, 2, \dots, m+1$, where column $j$ is the directed edge $l_j \to r_j + 1$!
   Since $\det(D) = 1$, $A$ is TU by Cauchy–Binet, and the system $D(Ax - s) = Db$ is literally the flow conservation system of Wave 3B's Equation-Difference Method (`[NOI2008] 志愿者招募`)!
2. What if $A \in \{0, 1\}^{m \times n}$ has the **Row Consecutive-Ones Property** instead (each constraint $i$ sums variables over an interval $[L_i, R_i]$, as in `[ZJOI2013] 防守战线`)?
   Take the **LP Dual**! Transposing $A \mapsto A^T$ turns Row Consecutive-Ones into **Column Consecutive-Ones**, which then compiles via $D A^T$ into a Directed Network Incidence Matrix! Or equivalently, substitute prefix sums $x_j = \pi_j - \pi_{j-1}$ (which is right-multiplication by $D^{-1}$) so $A D^{-1}$ has one $+1$ at $\pi_{R_i}$ and one $-1$ at $\pi_{L_i - 1}$ in each row! $\blacksquare$

> [!TIP]
> **Notice the Grand Unification!**
> - **Column Consecutive-Ones ($A$ has intervals in columns)** $\xrightarrow{\text{Left-multiply by } D}$ **Primal Equation-Difference Flow Network** (Iteration 30: `[NOI2008] 志愿者招募`).
> - **Row Consecutive-Ones ($A$ has intervals in rows)** $\xrightarrow{\text{Take LP Dual } A^T \text{ then } D}$ **Dual Potential Flow Network** (Iteration 36: `[ZJOI2013] 防守战线`).
> They are exact transpose duals of each other under Total Unimodularity!

---

#### Family 4: Directed Tree Path Incidence Matrices (`有向树链关联矩阵`)

What happens when we generalize from a 1D array of intervals $[l_j, r_j]$ to **paths on a tree $T = (V, E_T)$**?
This is one of the sharpest, most frequently tested boundary lines in competitive programming:

**Theorem 38.8 (Vertical / Directed Tree Paths vs. General Undirected Tree Paths)**:
Let $T$ be a rooted tree (with edges oriented from child to parent, or parent to child).
1. **Vertical (Ancestor–Descendant) Paths Are TU**:
   Let $A \in \{0, 1\}^{|E_T| \times m}$ be the edge-path incidence matrix where each column $j \in \{1, \dots, m\}$ is a **vertical path** from a descendant $u_j$ up to an ancestor $v_j$ (so $A_{e, j} = 1$ iff tree edge $e$ lies on the path $u_j \to v_j$). Then $A$ is **Totally Unimodular**, and left-multiplying by the **Tree Incidence Difference Matrix $D_T$** (subtracting from vertex $u$'s incoming parent-edge equation the sum of all child-edge equations $\sum_{c \in \text{child}(u)} E_c$) collapses every vertical path $u_j \to v_j$ into a single $+1$ at $u_j$ and a single $-1$ at $v_j$—a **Directed Network Incidence Matrix**!
   *(More generally, by a theorem of Tutte and Camion, the edge-path incidence matrix of a collection of directed paths in ANY directed tree—regardless of how the tree edges are oriented, provided each path follows the tree's edge orientations—is Totally Unimodular!)*
2. **General Undirected ("V-Shaped") Tree Paths Are NOT TU**:
   If columns of $A$ are general undirected paths in a tree $T$ (passing from $u_j$ up to $\text{LCA}(u_j, v_j)$ and back down to $v_j$), then $A$ is **NOT Totally Unimodular**!
   - **Explicit Counterexample ($K_{1,3}$ Star Tree)**:
     Let $T$ be a star with center $0$ and three leaves $1, 2, 3$, so $E_T = \{e_1, e_2, e_3\}$. Consider the three leaf-to-leaf paths $P_{12} = \{e_1, e_2\}$, $P_{23} = \{e_2, e_3\}$, and $P_{31} = \{e_3, e_1\}$. Their $3 \times 3$ edge-path incidence matrix is:
     $$A_{\text{star}} = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}, \qquad \det(A_{\text{star}}) = +2 \notin \{-1, 0, +1\}!$$
     Because of this $|\det| = 2$ obstruction, covering or packing general V-shaped paths on a tree with arbitrary capacities/costs cannot be reduced to standard flow via $D_T$ (unless the paths are vertical, or each edge capacity is $1$ where tree DP / matching applies).

---

### 38.5 Step 4 — Hand-Checkable Matrix Trace & Broken TU Counterexamples

#### 1. Explicit Matrix Multiplication Trace ($D \cdot A$ on $m = 3$ Rows)

Suppose we have $m = 3$ days and $n = 3$ interval variables:
- Variable $x_1$ covers $[1, 3]$, variable $x_2$ covers $[1, 2]$, variable $x_3$ covers $[2, 3]$.
The Column Consecutive-Ones matrix $A$ (padded with a 4th row of zeros) and the $4 \times 4$ difference matrix $D$ are:
$$D \cdot \begin{pmatrix} A \\ 0 \end{pmatrix} =
\begin{pmatrix}
1 & 0 & 0 & 0 \\
-1 & 1 & 0 & 0 \\
0 & -1 & 1 & 0 \\
0 & 0 & -1 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 1 & 0 \\
1 & 1 & 1 \\
1 & 0 & 1 \\
0 & 0 & 0
\end{pmatrix}
=
\begin{pmatrix}
+1 & +1 & 0 \\
0 & 0 & +1 \\
0 & -1 & 0 \\
-1 & 0 & -1
\end{pmatrix}.$$
Look at the product matrix on the right:
- Column 1 ($x_1$ on $[1, 3]$): $+1$ in Row 1, $-1$ in Row 4 $\implies$ directed edge $1 \to 4$.
- Column 2 ($x_2$ on $[1, 2]$): $+1$ in Row 1, $-1$ in Row 3 $\implies$ directed edge $1 \to 3$.
- Column 3 ($x_3$ on $[2, 3]$): $+1$ in Row 2, $-1$ in Row 4 $\implies$ directed edge $2 \to 4$.
Every single column has turned into a single directed edge!

#### 2. Broken TU Counterexamples (Why Non-Contiguous / Circular / 2D Intervals Break Flow)

```
BROKEN TU CASE 1: Split Intervals (A Variable with a "Gap" [1, 1] U [3, 3])
  Suppose variable x_j works on Day 1 and Day 3, skipping Day 2: column is (1, 0, 1)^T.
  When multiplied by D, it becomes (+1, -1, +1, -1)^T — it has TWO +1s and TWO -1s!
  One unit of flow on x_j would have to simultaneously traverse two separate edges (1 -> 2
  and 3 -> 4) in lockstep ("paired/equal flow on two edges"), which is NP-hard! Indeed,
  three gap columns (1,1,0)^T, (0,1,1)^T, (1,0,1)^T have det = 2, breaking TU!

BROKEN TU CASE 2: Circular Intervals (Wrap-Around Shifts on a 24-Hour Clock)
  Suppose shifts wrap around midnight: Shift 1 covers [1, 2], Shift 2 covers [2, 3],
  and Shift 3 wraps around to cover [3, 1]. Their incidence matrix is the exact 3x3 matrix
  with det = 2! WARNING: Circular Consecutive-Ones matrices are NOT Totally Unimodular!
  (However, if the number of wrap-around flow units F is fixed by binary search or WQS
  parametric search, removing F resets the matrix to linear Consecutive-Ones, which IS TU!)
```

---

## Iteration 39: Submodular Function Minimization (SFM), Lovász Extension & Polymatroid Flows

### 39.1 Step 1 — The Non-Graph Diagnostic Signal (Submodularity as the Soul of Cuts)

Why can some binary optimization problems $\min_{S \subseteq V} f(S)$ be solved via $s$-$t$ Minimum Cut (`燃やす埋める`), while others require general Submodular Function Minimization (SFM) or are NP-hard? And why do continuous convex minimization problems on graphs (`CF 1427G — One Billion Shades of Grey`, Isotonic Regression `保序回归`) decompose into decoupled binary min-cuts across threshold levels $\lambda$?

Look for these **Diagnostic Signals of Submodularity**:
1. **Diminishing Marginal Returns (`边际效益递减`)**: Adding an element $x$ to a larger set $B \supseteq A$ yields a smaller (or equal) marginal increase in cost than adding $x$ to $A$:
   $$f(A \cup \{x\}) - f(A) \ge f(B \cup \{x\}) - f(B) \quad \forall A \subseteq B \subseteq V \setminus \{x\}.$$
2. **Pairwise Cross-Penalty Attraction ($A + D \le B + C$)**: For binary choices $x_u, x_v \in \{0, 1\}$, disagreeing states $(0, 1)$ and $(1, 0)$ cost at least as much in total as agreeing states $(0, 0)$ and $(1, 1)$.
3. **Rank / Coverage / Cut Bound Constraints ($\sum_{i \in S} x_i \le f(S)$ for all $S \subseteq V$)**: Instead of simple box bounds $0 \le x_i \le u_i$, subsets of variables share submodular capacity caps (e.g., matroid rank $\text{rank}(S)$ or graph cut capacity $c(\delta^+(S))$).

---

### 39.2 Step 2 — Submodular Set Functions, Cut Submodularity & Pseudo-Boolean Representability

#### 1. Equivalent Definitions of Submodularity

**Definition 39.1 (Submodular Set Function)**:
Let $V$ be a finite ground set of size $n$. A set function $f : 2^V \to \mathbb{R}$ is **submodular (`劣模函数 / 劣モジュラ関数`)** if it satisfies any of the following three equivalent conditions:
1. **Uncrossing Inequality (`交叉不等式`)**: For all $A, B \subseteq V$,
   $$f(A) + f(B) \ge f(A \cup B) + f(A \cap B).$$
2. **Diminishing Marginal Returns**: For all $A \subseteq B \subseteq V$ and $x \in V \setminus B$,
   $$f(A \cup \{x\}) - f(A) \ge f(B \cup \{x\}) - f(B).$$
3. **Non-Positive Second Differences**: For all $A \subseteq V$ and distinct $x, y \in V \setminus A$,
   $$f(A \cup \{x, y\}) - f(A \cup \{x\}) - f(A \cup \{y\}) + f(A) \le 0.$$
*(A function $g : 2^V \to \mathbb{R}$ is **supermodular** if $-g$ is submodular, and **modular** if it is both submodular and supermodular, i.e., $f(S) = f(\emptyset) + \sum_{i \in S} w_i$.)*

#### 2. Proof That Directed Graph and Hypergraph Cut Functions Are Submodular

**Theorem 39.2 (Submodularity of Cut Capacity)**:
Let $G = (V, E)$ be a directed graph with non-negative edge capacities $c : E \to \mathbb{R}_{\ge 0}$. The directed cut capacity function
$$f(S) = c(\delta^+(S)) = \sum_{(u, v) \in E : u \in S, v \notin S} c(u, v)$$
is submodular on $2^V$.

**Proof (Edge-by-Edge Indicator Verification)**:
Since a non-negative linear combination of submodular functions is submodular, it suffices to prove that for a single directed edge $e = (u, v)$ of unit capacity, its cut indicator $f_e(S) = [u \in S \text{ and } v \notin S] = x_u (1 - x_v)$ satisfies $f_e(A) + f_e(B) \ge f_e(A \cup B) + f_e(A \cap B)$ for all $A, B \subseteq V$.
Suppose the RHS $f_e(A \cup B) + f_e(A \cap B)$ is positive:
- If $f_e(A \cup B) = 1$, then $u \in A \cup B$ and $v \notin A \cup B$. Thus $v \notin A$ and $v \notin B$, while $u \in A$ or $u \in B$, so $f_e(A) + f_e(B) \ge 1$.
- If $f_e(A \cap B) = 1$, then $u \in A \cap B$ and $v \notin A \cap B$. Thus $u \in A$ and $u \in B$, while $v \notin A$ or $v \notin B$, so again $f_e(A) + f_e(B) \ge 1$.
- Can both $f_e(A \cup B) = 1$ and $f_e(A \cap B) = 1$ hold simultaneously? If so, $u \in A \cap B$ (so $u \in A$ and $u \in B$) and $v \notin A \cup B$ (so $v \notin A$ and $v \notin B$), which means $f_e(A) = 1$ AND $f_e(B) = 1$, so $f_e(A) + f_e(B) = 2 = f_e(A \cup B) + f_e(A \cap B)$!
Thus $f_e(A) + f_e(B) \ge f_e(A \cup B) + f_e(A \cap B)$ holds in every case! $\blacksquare$

*(Note: By the exact same proof, for any hyperedge $H \subseteq V$ of weight $w_H \ge 0$, the hypergraph cut indicator $[H \cap S \ne \emptyset \text{ and } H \setminus S \ne \emptyset]$ is also submodular, and can be compiled into a directed graph cut using two auxiliary hub nodes $h_{\text{in}} \to h_{\text{out}}$ of capacity $w_H$, with $\infty$-edges $u \to h_{\text{in}}$ and $h_{\text{out}} \to u$ for all $u \in H$!)*

#### 3. Degree-2 Pseudo-Boolean Cut Representability Theorem (Kolmogorov & Zabih 2004)

Identify each subset $S \subseteq V$ with its binary indicator vector $x \in \{0, 1\}^n$ where $x_i = [i \in S]$ (so $x_i = 1$ means $i$ is on the $S$-side of an $s$-$t$ cut, where $x_s = 1, x_t = 0$).
Every function $f : \{0, 1\}^n \to \mathbb{R}$ can be uniquely written as a multilinear **Pseudo-Boolean Polynomial**:
$$f(x_1, \dots, x_n) = c_\emptyset + \sum_{i=1}^n c_i x_i + \sum_{1 \le i < j \le n} c_{i,j} x_i x_j + \sum_{1 \le i < j < k \le n} c_{i,j,k} x_i x_j x_k + \dots$$

**Theorem 39.3 (Quadratic Submodularity $\Longleftrightarrow$ Graph Cut Representability)**:
A quadratic (degree $\le 2$) pseudo-Boolean function $f(x_1, \dots, x_n)$ can be represented as the capacity of an $s$-$t$ cut in a directed network with non-negative edge capacities (plus a constant) **if and only if $f$ is submodular**, which is equivalent to requiring that every pairwise interaction term $\Phi_{ij}(x_i, x_j)$ with cost table
$$\Phi_{ij}(0, 0) = A, \quad \Phi_{ij}(0, 1) = B, \quad \Phi_{ij}(1, 0) = C, \quad \Phi_{ij}(1, 1) = D$$
satisfies the **Pairwise Submodularity Inequality**:
$$A + D \le B + C \quad \Longleftrightarrow \quad c_{i,j} = (A + D) - (B + C) \le 0!$$

**Proof & Explicit Algebraic-to-Edge Compilation**:
Rewrite any pairwise table $\Phi_{ij}(x_i, x_j)$ in terms of unary indicators $x_i, (1 - x_i)$ and the directed cut monomials $x_i(1 - x_j)$ and $x_j(1 - x_i)$:
$$\Phi_{ij}(x_i, x_j) = A + (C - A) x_i + (D - C) x_j + \underbrace{(B + C - A - D)}_{\ge 0} x_j (1 - x_i)$$
(or using $x_i(1 - x_j)$). Since $x_j(1 - x_i)$ is the cut indicator of a directed edge $j \to i$ of capacity $B + C - A - D \ge 0$, and unary terms $\alpha x_i = \alpha - \alpha(1 - x_i)$ compile into source edges $s \to i$ (if $\alpha < 0$) or sink edges $i \to t$ (if $\alpha > 0$, since $x_i(1 - x_t) = x_i$), every submodular quadratic function compiles into a non-negative graph cut! Conversely, by Theorem 39.2, any graph cut with non-negative capacities is submodular, so no function with $A + D > B + C$ can ever be represented without variable negation ($x_j \gets 1 - x_j$). $\blacksquare$

*(What about degree $\ge 3$ submodular functions? Interestingly, Zivný, Cohen, and Jeavons (2009) proved that **not all** cubic ($k = 3$) or quaternary ($k = 4$) submodular functions can be reduced to graph cuts even with auxiliary variables! Specifically, while a single conjunction $-w \prod_{i \in S} x_i$ or disjunction $+w(1 - \prod_{i \in S}(1 - x_i))$ with $w > 0$ IS graph-representable via one auxiliary hub node $z \in \{0, 1\}$, general submodular functions on $|V| \ge 4$ require general Submodular Function Minimization or Polymatroid Flows.)*

---

### 39.3 Step 3 — The Base Polyhedron $B(f)$, Edmonds' Greedy Algorithm & Polymatroid Flows

#### 1. Submodular Polyhedron $P(f)$ and Base Polyhedron $B(f)$

Let $f : 2^V \to \mathbb{R}$ be a submodular function with $f(\emptyset) = 0$. Associate with $f$ two fundamental polyhedra in $\mathbb{R}^V$:
- **Submodular Polyhedron**:
  $$P(f) := \left\{ x \in \mathbb{R}^V : \forall S \subseteq V, \; x(S) := \sum_{i \in S} x_i \le f(S) \right\}.$$
- **Base Polyhedron**:
  $$B(f) := \left\{ x \in P(f) : x(V) = f(V) \right\} = \left\{ x \in \mathbb{R}^V : \forall S \subsetneq V, \; x(S) \le f(S), \text{ and } x(V) = f(V) \right\}.$$
*(When $f$ is also monotone non-decreasing, $P_+(f) = P(f) \cap \mathbb{R}_{\ge 0}^V$ is called a **Polymatroid (`多拟阵`)**.)*

#### 2. Edmonds' Greedy Algorithm (1970) on the Base Polyhedron

Although $B(f)$ is defined by $2^n$ exponential inequalities $x(S) \le f(S)$, **Jack Edmonds (1970)** discovered that we can maximize any linear objective $w^T x = \sum_{i=1}^n w_i x_i$ over $x \in B(f)$ in $O(n \log n)$ time using a simple **Sorting Greedy Algorithm**!

**Theorem 39.4 (Edmonds' Polymatroid Greedy Theorem)**:
Given any weight vector $w \in \mathbb{R}^V$, sort the elements of $V = \{v_1, v_2, \dots, v_n\}$ in **non-increasing order of weight**:
$$w_{v_1} \ge w_{v_2} \ge \dots \ge w_{v_n}.$$
Define the nested chain of prefixes $\emptyset = S_0 \subset S_1 \subset S_2 \subset \dots \subset S_n = V$ where $S_k = \{v_1, \dots, v_k\}$, and define the vector $x^* \in \mathbb{R}^V$ by marginal differences:
$$x^*_{v_k} := f(S_k) - f(S_{k-1}) \quad \text{for } k = 1, 2, \dots, n.$$
Then:
1. $x^* \in B(f)$ is a valid vertex of the Base Polyhedron $B(f)$ (and is integral whenever $f$ is integer-valued!).
2. $x^*$ **maximizes** $w^T x$ over all $x \in B(f)$, with optimal value:
   $$\max_{x \in B(f)} \sum_{i \in V} w_i x_i = \sum_{k=1}^{n-1} (w_{v_k} - w_{v_{k+1}}) f(S_k) + w_{v_n} f(S_n).$$

**Proof (via LP Duality & Submodular Uncrossing)**:
First, let us prove $x^* \in B(f)$, i.e., $x^*(T) \le f(T)$ for all $T \subseteq V$. By induction on $k \in \{0, 1, \dots, n\}$, we claim $x^*(T \cap S_k) \le f(T \cap S_k)$. For $k = 0$ both sides are $0$. For the inductive step from $k-1$ to $k$:
- If $v_k \notin T$, then $T \cap S_k = T \cap S_{k-1}$, which holds by induction.
- If $v_k \in T$, then by the induction hypothesis and submodularity on $A = T \cap S_{k-1} \subseteq S_{k-1} = B$ with element $v_k$:
  $$x^*(T \cap S_k) = x^*(T \cap S_{k-1}) + x^*_{v_k} \le f(T \cap S_{k-1}) + \big(f(S_{k-1} \cup \{v_k\}) - f(S_{k-1})\big) \le f(T \cap S_k)!$$
Taking $k = n$ yields $x^*(T) \le f(T)$ for all $T \subseteq V$, and $x^*(V) = f(S_n) - f(S_0) = f(V)$, so $x^* \in B(f)$.
Second, why is $x^*$ optimal for $\max_{x \in B(f)} w^T x$? By Abel summation (summation by parts):
$$\text{For ANY } x \in B(f): \quad \sum_{k=1}^n w_{v_k} x_{v_k} = \sum_{k=1}^{n-1} \underbrace{(w_{v_k} - w_{v_{k+1}})}_{\ge 0} \underbrace{x(S_k)}_{\le f(S_k)} + w_{v_n} \underbrace{x(S_n)}_{= f(S_n)} \le \sum_{k=1}^{n-1} (w_{v_k} - w_{v_{k+1}}) f(S_k) + w_{v_n} f(S_n) = w^T x^*! \quad \blacksquare$$

---

### 39.4 Step 4 — The Lovász Extension $\hat{f}(x)$ & Unification with the Coarea Formula (`CF 1427G`)

Look closely at the formula in Theorem 39.4! It defines a function on arbitrary continuous vectors $w \in \mathbb{R}^V$, discovered by **László Lovász (1983)**:

**Definition 39.5 (The Lovász Extension `Lovász 延拓`)**:
For any set function $f : 2^V \to \mathbb{R}$ with $f(\emptyset) = 0$, its **Lovász extension** $\hat{f} : \mathbb{R}^V \to \mathbb{R}$ is defined for any continuous vector $x \in \mathbb{R}^V$ (sorted as $x_{v_1} \ge x_{v_2} \ge \dots \ge x_{v_n}$ with $S_k = \{v_1, \dots, v_k\}$) by:
$$\hat{f}(x) := \sum_{k=1}^n x_{v_k} \big(f(S_k) - f(S_{k-1})\big) = \sum_{k=1}^{n-1} (x_{v_k} - x_{v_{k+1}}) f(S_k) + x_{v_n} f(V).$$
Equivalently, if $x \in [0, M]^V$, writing $x$ as a continuous level-set integral gives:
$$\hat{f}(x) = \int_0^M f\big(\{i \in V : x_i \ge \lambda\}\big) \, d\lambda!$$

> [!IMPORTANT]
> **Theorem 39.6 (Lovász Convexity Theorem & The Coarea Unification)**
> 1. **Submodularity $\Longleftrightarrow$ Convexity**: A set function $f : 2^V \to \mathbb{R}$ is **submodular** if and only if its Lovász extension $\hat{f} : \mathbb{R}^V \to \mathbb{R}$ is a **convex function** on $\mathbb{R}^V$!
>    *(Proof: When $f$ is submodular, Theorem 39.4 proves that $\hat{f}(x) = \max_{y \in B(f)} x^T y$ is the pointwise maximum of linear functions $x \mapsto x^T y$, which is automatically convex!)*
> 2. **Exact Continuous-to-Discrete Integrity**: For any submodular function $f$, minimizing $f(S)$ over discrete subsets $S \subseteq V$ is **equivalent** to minimizing the continuous convex function $\hat{f}(x)$ over the hypercube $x \in [0, 1]^V$:
>    $$\min_{S \subseteq V} f(S) = \min_{x \in [0, 1]^V} \hat{f}(x)!$$
>    Why? Because for any $x \in [0, 1]^V$ with $1 \ge x_{v_1} \ge \dots \ge x_{v_n} \ge 0$, $\hat{f}(x)$ is a convex combination of $f(\emptyset), f(S_1), \dots, f(S_n)$ with non-negative weights summing to $1$, so at least one threshold set $S_k = \{i : x_i \ge \lambda_k\}$ satisfies $f(S_k) \le \hat{f}(x)$!
> 3. **Direct Bridge to `CF 1427G — One Billion Shades of Grey` and Isotonic Regression**:
>    Suppose $f(S) = c(\delta^+(S))$ is the directed cut capacity of a graph $G = (V, E)$. What is the Lovász extension $\hat{f}(h)$ of the cut function evaluated at continuous vertex heights $h \in \mathbb{R}^V$?
>    For a single directed edge $(u, v)$ of weight $w_{uv}$:
>    $$\hat{f}_{uv}(h) = \int_{-\infty}^{\infty} w_{uv} \big[h_u \ge \lambda \text{ and } h_v < \lambda\big] \, d\lambda = w_{uv} \max(0, h_u - h_v).$$
>    And for an undirected edge $\{u, v\}$ (modeled as a bidirectional pair $(u, v)$ and $(v, u)$):
>    $$\hat{f}_{\{u,v\}}(h) = w_{uv} |h_u - h_v| = \sum_{k} (\lambda_{k+1} - \lambda_k) w_{uv} \Big| [h_u > \lambda_k] - [h_v > \lambda_k] \Big|!$$
>    **The total variation $\sum w_{uv} |h_u - h_v|$ in `CF 1427G` is literally the Lovász extension $\hat{f}(h)$ of the graph cut function $f(S) = c(\delta(S))$!** Because $f(S)$ is submodular, the level sets $S(\lambda) = \{v : h^*_v > \lambda\}$ of the optimal continuous vector $h^*$ are **nested minimum cuts** $S(\lambda_1) \supseteq S(\lambda_2) \supseteq \dots$, allowing us to solve the continuous optimization problem by sweeping $\lambda$ across discrete cut thresholds!

#### Polymatroid Network Flows (Edmonds & Giles 1977)

In a **Polymatroid / Submodular Flow (`劣模流 / 多拟阵流`)**, instead of bounding vertex inflows/outflows at individual vertices, we require the net boundary vector $\partial f \in \mathbb{R}^V$ (where $(\partial f)_v = \text{in}_f(v) - \text{out}_f(v)$) to lie inside the Base Polyhedron $B(g)$ of a submodular function $g : 2^V \to \mathbb{R}$:
$$\forall S \subseteq V: \quad \sum_{v \in S} \big(\text{in}_f(v) - \text{out}_f(v)\big) \le g(S), \qquad l_e \le f_e \le u_e.$$
By **Edmonds–Giles Total Dual Integrality (1977)**, when $g$ is an integer-valued submodular function and $l, u \in \mathbb{Z}^E$, the Polymatroid Flow LP has **exact integer primal optimal flows and integer dual potentials**! In competitive programming, whenever $g(S)$ is the rank function of a partition or laminar matroid (a hierarchy of nested subsets $S_1 \subset S_2 \subset \dots$, such as a tree of subgroup quotas), the polymatroid constraint $\partial f \in B(g)$ compiles directly into a **tree of auxiliary flow edges** where each laminar set $S_k$ is represented by a subtree root node with capacity $g(S_k)$!

---

### 39.5 Toy Trace of Edmonds' Greedy & Lovász Extension

Suppose $V = \{1, 2\}$ with a submodular cut function $f(\emptyset) = 0, f(\{1\}) = 3, f(\{2\}) = 4, f(\{1, 2\}) = 5$ (check submodularity: $f(\{1\}) + f(\{2\}) = 7 \ge 5 + 0 = f(\{1,2\}) + f(\emptyset)$).
We want to evaluate the Lovász extension $\hat{f}(x)$ at $x = (2, 5)$, which equals $\max_{y \in B(f)} (2 y_1 + 5 y_2)$:
- Sort $V$ in non-increasing order of $x$: $x_2 = 5 \ge x_1 = 2$, so $v_1 = 2, v_2 = 1$.
- Prefix chain: $S_0 = \emptyset$, $S_1 = \{2\}$, $S_2 = \{1, 2\}$.
- Edmonds' greedy vertex $y^* \in B(f)$:
  - $y^*_2 = f(\{2\}) - f(\emptyset) = 4 - 0 = 4$.
  - $y^*_1 = f(\{1, 2\}) - f(\{2\}) = 5 - 4 = 1$.
  *(Check $y^* \in B(f)$: $y^*_1 = 1 \le 3$, $y^*_2 = 4 \le 4$, $y^*_1 + y^*_2 = 5 = f(V)$.)*
- Lovász extension value:
  $$\hat{f}(2, 5) = 2 y^*_1 + 5 y^*_2 = 2(1) + 5(4) = 22 = (5 - 2) f(\{2\}) + 2 f(\{1, 2\}) = 3(4) + 2(5) = 22.$$
Now contrast what happens if $f$ were **supermodular**, say $f(\{1\}) = 2, f(\{2\}) = 2, f(\{1, 2\}) = 6$:
Then Edmonds' greedy rule gives $y^*_2 = 2 - 0 = 2$ and $y^*_1 = 6 - 2 = 4$, which **violates** the constraint $y_1 \le f(\{1\}) = 2$! Thus $B(f)$ is empty and $\hat{f}(x)$ is concave rather than convex!

---

## Iteration 40: The Boundary Between Network Flow, Matroid Intersection & NP-Hardness

### 40.1 Step 1 — The Non-Graph Diagnostic Signal (Knowing When Flow Is Impossible)

In competitive programming, knowing **when a problem CANNOT be solved by Network Flow** is just as decisive as knowing how to build a flow graph. Countless hours are lost in ICPC and OI contests trying to force a 3-attribute matching problem, a rainbow spanning tree problem, or a 2-commodity routing problem into a Dinic or MCMF network by rearranging layers—only to discover on sample 3 that flow from two different sources "mixes" at an intermediate vertex and produces illegal combinations!

How do you diagnose whether a combinatorial constraint system belongs to:
1. **Standard Max-Flow / MCMF** (2 Partition/Laminar Matroids, or TU LP),
2. **Matroid Intersection** (2 general matroids, e.g., Graphic + Color Matroid, solvable in $O(r^2 m)$ or $O(r m^{1.5})$ via exchange-graph augmenting paths, but **not** reducible to Dinic!), or
3. **NP-Hardness** (3 Partition Matroids / 3D Matching, Integer 2-Commodity Flow, or Equal-Flow Paired Edges)?

The key lies in counting **how many independent matroid/submodular constraints simultaneously govern each atomic decision element**, and testing whether intermediate vertices suffer from **Flow Amnesia (`流量失忆 / 混流效应`)**.

---

### 40.2 Step 2 — Matroid Foundations & Edmonds' Matroid Intersection Duality

#### 1. Definition of a Matroid and Its Rank Function

**Definition 40.1 (Matroid `拟阵`)**:
A **matroid** $M = (E, \mathcal{I})$ consists of a finite ground set $E$ and a non-empty family of **independent subsets** $\mathcal{I} \subseteq 2^E$ satisfying:
1. **Hereditary Property**: If $I \in \mathcal{I}$ and $J \subseteq I$, then $J \in \mathcal{I}$.
2. **Augmentation / Exchange Axiom**: If $I, J \in \mathcal{I}$ with $|I| < |J|$, there exists an element $e \in J \setminus I$ such that $I \cup \{e\} \in \mathcal{I}$.

The **rank function** $r : 2^E \to \mathbb{Z}_{\ge 0}$ of a matroid $M$ is defined as $r(S) := \max \{ |I| : I \subseteq S, \; I \in \mathcal{I} \}$. Every matroid rank function satisfies $0 \le r(S) \le |S|$, monotonicity ($A \subseteq B \implies r(A) \le r(B)$), and **submodularity**:
$$r(A) + r(B) \ge r(A \cup B) + r(A \cap B) \quad \forall A, B \subseteq E.$$

#### 2. The Four Matroid Classes in Competitive Programming

1. **Partition Matroid (`划分拟阵`)**:
   $E$ is partitioned into disjoint blocks $E = B_1 \sqcup B_2 \sqcup \dots \sqcup B_k$ with capacities $d_1, \dots, d_k$, and $I \in \mathcal{I} \iff |I \cap B_i| \le d_i$ for all $i$. Its rank function is $r(S) = \sum_{i=1}^k \min(|S \cap B_i|, d_i)$.
2. **Laminar Matroid (`层状拟阵`)**:
   A family $\mathcal{F} \subseteq 2^E$ of subsets is **laminar (`层状/嵌套族`)** if for any $A, B \in \mathcal{F}$, either $A \subseteq B$, $B \subseteq A$, or $A \cap B = \emptyset$ (i.e., $\mathcal{F}$ forms a forest of nested sets under inclusion). Each $A \in \mathcal{F}$ has a capacity $d_A$, and $I \in \mathcal{I} \iff |I \cap A| \le d_A$ for all $A \in \mathcal{F}$.
3. **Graphic Matroid (`图拟阵 / 森林拟阵`)**:
   $E$ is the edge set of an undirected graph $G = (V, E)$, and $I \in \mathcal{I} \iff I$ is a **forest** (contains no cycles). Its rank function is $r(S) = |V| - c(V, S)$, where $c(V, S)$ is the number of connected components of the spanning subgraph $(V, S)$.
4. **Linear / Xor-Basis Matroid (`线性拟阵`)**:
   $E$ is a finite set of vectors in a vector space $\mathbb{F}^d$ (in CP, typically bitmasks in $\mathbb{F}_2^d$ maintained via an XOR linear basis `线性基`), and $I \in \mathcal{I} \iff I$ is linearly independent.

#### 3. Edmonds' Matroid Intersection Theorem (1970)

Given **two** matroids $M_1 = (E, \mathcal{I}_1)$ and $M_2 = (E, \mathcal{I}_2)$ on the **same** ground set $E$, the **Matroid Intersection Problem** asks for a maximum-cardinality (or maximum-weight) common independent set $I \in \mathcal{I}_1 \cap \mathcal{I}_2$.

**Theorem 40.2 (Edmonds' Matroid Intersection Min–Max Theorem)**:
For any two matroids $M_1 = (E, \mathcal{I}_1)$ and $M_2 = (E, \mathcal{I}_2)$ with rank functions $r_1, r_2$:
$$\max_{I \in \mathcal{I}_1 \cap \mathcal{I}_2} |I| = \min_{U \subseteq E} \Big( r_1(U) + r_2(E \setminus U) \Big).$$
Furthermore, the **Matroid Intersection Polytope** crosses the two submodular polyhedra $P_+(r_1)$ and $P_+(r_2)$:
$$P(M_1 \cap M_2) = \left\{ x \in \mathbb{R}_{\ge 0}^E : \forall S \subseteq E, \; x(S) \le r_1(S) \text{ and } x(S) \le r_2(S) \right\},$$
and by **Edmonds' Total Dual Integrality Theorem**, $P(M_1 \cap M_2)$ has **exclusively integral vertices** $\{0, 1\}^E$ corresponding to the common independent sets $I \in \mathcal{I}_1 \cap \mathcal{I}_2$!

---

### 40.3 Step 3 — The Four Boundary Lines Between Flow, Matroid Intersection & NP-Hardness

Let us now draw the exact mathematical boundaries that separate Max-Flow, Matroid Intersection, and NP-Hardness.

---

#### Boundary Line 1: Intersection of Two Partition (or Laminar) Matroids $\subset$ Max-Flow / MCMF

Why is **Bipartite Matching** (and more generally, **Laminar Quota Matching**) a special case of Max-Flow?
Let $G = (L \sqcup R, E)$ be a bipartite graph. The ground set of decisions is the **edge set $E$**.
- **Matroid $M_1$ (Left Endpoint Degree Constraint)**: Partition $E = \bigsqcup_{u \in L} \delta(u)$ by left endpoint; an edge subset $I \subseteq E$ satisfies $I \in \mathcal{I}_1 \iff |I \cap \delta(u)| \le 1$ for all $u \in L$. This is a **Partition Matroid**!
- **Matroid $M_2$ (Right Endpoint Degree Constraint)**: Partition $E = \bigsqcup_{v \in R} \delta(v)$ by right endpoint; $I \in \mathcal{I}_2 \iff |I \cap \delta(v)| \le 1$ for all $v \in R$. This is a second **Partition Matroid**!
- **Why It Compiles to $s$-$t$ Flow**:
  In the incidence matrix $\binom{A_1}{A_2} x \le \mathbf{1}$, each element $e = (u, v) \in E$ belongs to **one block $u \in L$ of $M_1$** and **one block $v \in R$ of $M_2$**. By negating the rows of $A_2$ (Bipartite Family 2 in Iteration 38!), every column $e = (u, v)$ has $+1$ at row $u$ and $-1$ at row $v$—so $e$ becomes a **directed edge $u \to v$ of capacity $1$** between the $M_1$-tree (rooted at $S$) and the $M_2$-tree (rooted at $T$)!
  Even more generally, if $M_1$ is a **Laminar Matroid** $\mathcal{F}_1$ (a tree of nested subgroup caps on the left) and $M_2$ is a **Laminar Matroid** $\mathcal{F}_2$ (a tree of nested subgroup caps on the right), building an out-tree from $S$ representing $\mathcal{F}_1$, an in-tree into $T$ representing $\mathcal{F}_2$, and connecting each $e \in E$ from its smallest containing set in $\mathcal{F}_1$ to its smallest containing set in $\mathcal{F}_2$ compiles **Laminar-Laminar Matroid Intersection** directly into **Max-Flow / MCMF**!
  And notice: for Bipartite Matching, Edmonds' Matroid Intersection Theorem $\min_{U \subseteq E} (r_1(U) + r_2(E \setminus U))$ reduces immediately to **König's Theorem** ($\text{Max Matching} = \text{Min Vertex Cover}$)!

---

#### Boundary Line 2: Graphic / Linear Matroid Intersection $\not\subset$ Max-Flow

What happens when one or both of the two matroids $M_1, M_2$ is **not** a Laminar/Partition matroid—for example:
- **Rainbow Spanning Forest (`彩虹生成树`)**: Given a graph $G = (V, E)$ where each edge $e \in E$ has a color $c(e) \in \{1, \dots, k\}$, find a maximum forest $I \subseteq E$ containing at most $1$ edge of each color.
  - Here $M_1 = \text{Graphic Matroid}$ ($I$ contains no cycles) and $M_2 = \text{Partition Matroid}$ (at most $1$ edge per color).
- **Bipartite Graphic + Linear Matroid (`[省选联考 2020] 魔法商店` / XOR Basis Intersection)**: Find a subset of items that is independent in two XOR bases or a graph + color system.
- **Degree-Constrained Spanning Tree (when degree-bounded vertices form an Independent Set $W \subseteq V$)**:
  - $M_1 = \text{Graphic Matroid}$ (spanning tree), $M_2 = \text{Partition Matroid}$ (at most $d_v$ edges incident to each $v \in W$; note that because $W$ is an independent set, no edge has *both* endpoints in $W$, so the sets $\delta(v)$ for $v \in W$ are disjoint and form a Partition Matroid!).

**Why Cannot Graphic Matroid Intersection Be Solved by a Fixed Static Flow Network?**
In a static flow network, flow conservation $\text{in}(v) - \text{out}(v) = 0$ can only enforce laminar/cut-type submodular bounds $r(S) = c(\delta^+(S))$. A Graphic Matroid enforces the **cycle-elimination bound** $|I \cap E(U)| \le |U| - 1$ for every induced vertex subset $U \subseteq V$, whose constraint matrix is **not** convertible to a fixed graph incidence matrix.
Instead, **Edmonds' Matroid Intersection Algorithm** rebuilds a dynamic **Bipartite Exchange Graph $G(I)$** after *every* single augmentation:
- Given the current common independent set $I \in \mathcal{I}_1 \cap \mathcal{I}_2$, partition $E = I \sqcup (E \setminus I)$.
- Define the source set $X_1 = \{y \in E \setminus I : I \cup \{y\} \in \mathcal{I}_1\}$ and sink set $X_2 = \{y \in E \setminus I : I \cup \{y\} \in \mathcal{I}_2\}$.
- For $x \in I$ and $y \in E \setminus I$:
  - Add directed edge $x \to y$ if $I \setminus \{x\} \cup \{y\} \in \mathcal{I}_1$ (in a Graphic Matroid, $x$ lies on the unique fundamental cycle of $y$ in $I$).
  - Add directed edge $y \to x$ if $I \setminus \{x\} \cup \{y\} \in \mathcal{I}_2$ (in a Color Partition Matroid, $x$ has the same color as $y$).
- Find a **shortest augmenting path** (fewest edges, or minimum weight with shortest tie-breaking!) $P = (y_0, x_1, y_1, \dots, x_k, y_k)$ from $X_1$ to $X_2$ in $G(I)$, and update $I \gets I \oplus V(P)$!
Notice the stunning parallel: when both $M_1$ and $M_2$ are Partition Matroids (Bipartite Matching), the Exchange Graph $G(I)$ is **isomorphic to the residual graph $G_f$ of Hopcroft–Karp / MCMF**! Matroid Intersection is simply "Residual Augmenting Paths where the residual graph depends on cycles/linear combinations rather than just vertex degrees"!

---

#### Boundary Line 3: Intersection of Three Partition Matroids $\implies$ NP-Hard (`三部图匹配与中间节点陷阱`)

Now we reach the **most dangerous trap in competitive programming flow modelling**:

> [!CAUTION]
> **Theorem 40.3 (3-Matroid Intersection Is NP-Hard)**
> Finding a maximum common independent set $I \in \mathcal{I}_1 \cap \mathcal{I}_2 \cap \mathcal{I}_3$ of **three** Partition Matroids is equivalent to **3-Dimensional Matching (`三维匹配 / 3DM`)**, one of Karp's 21 original **NP-complete** problems!
> Furthermore, if you attempt to model a 3-way matching of coupled triples $(a, x, b) \in \mathcal{T} \subseteq A \times X \times B$ as a layered flow network $S \to A \to X \to B \to T$, the network suffers from **Flow Amnesia (`流量失忆`)** and solves a **different (relaxed) problem**!

Let us dissect this trap with surgical precision. Suppose we have three sets of entities: Workers $A$, Machines $X$, and Tasks $B$, where each worker $a \in A$, machine $x \in X$, and task $b \in B$ can be used at most once.Compare **two superficially similar English problem statements**:

##### Case 3A (Polynomial Max-Flow — Decoupled Compatibility through Bottleneck $X$)

- **English Statement**: *"Each machine $x \in X$ is compatible with a subset of workers $A(x) \subseteq A$ and a subset of tasks $B(x) \subseteq B$. A triple $(a, x, b)$ is valid if and only if $a \in A(x)$ AND $b \in B(x)$."*
- **Why This IS Polynomial Max-Flow**:
  Notice that for a fixed machine $x \in X$, the choice of worker $a \in A(x)$ and the choice of task $b \in B(x)$ are **completely decoupled**! Any worker in $A(x)$ can be paired with any task in $B(x)$ as long as both pass through machine $x$.
- **Correct Graph Construction (`Put the Bottleneck Entity X in the MIDDLE`)**:
  $$S \xrightarrow{\text{cap } 1} a \xrightarrow{\text{cap } 1} x_{\text{in}} \xrightarrow{\text{cap } 1} x_{\text{out}} \xrightarrow{\text{cap } 1} b \xrightarrow{\text{cap } 1} T.$$
  Why does this work without flow mixing? Because the vertex-split edge $x_{\text{in}} \to x_{\text{out}}$ has **capacity $1$**! At most **one** unit of integer flow can pass through $x_{\text{in}} \to x_{\text{out}}$. Therefore, if $1$ unit of flow enters $x_{\text{in}}$ from some unique worker $a \in A(x)$ and exits $x_{\text{out}}$ to some unique task $b \in B(x)$, there is no second unit of flow inside $x$ that could "swap partners"!
- **Crucial Warning (`What Happens If You Put X on the Side: S -> X -> A -> B -> T?`)**:
  Even in Case 3A where the problem *is* solvable by flow, if you build the layers in the wrong order—say $S \to X \to A \to B \to T$—your solution will **fail**!
  Why? Suppose machine $x_1$ is compatible with worker $a_1$ and task $b_1$, while machine $x_2$ is compatible with worker $a_2$ and task $b_2$, and suppose worker $a_1$ also happens to appear in some other machine $x_3$'s compatibility with $b_2$ so edge $a_1 \to b_2$ exists in layer $A \to B$. Then flow from $x_1 \to a_1$ can cross over to $b_2$, forming the **illegal triple $(x_1, a_1, b_2)$** where $b_2 \notin B(x_1)$!
  **Golden Rule of 3-Layer Flow**: **The entity $X$ that defines the compatibility relation $(a \in A(x) \text{ and } b \in B(x))$ MUST be placed in the MIDDLE layer ($A \to X_{\text{in}} \to X_{\text{out}} \to B$) with unit vertex capacity!**

##### Case 3B (NP-Hard 3D Matching — Coupled Triples $(a, x, b) \in \mathcal{T}$)

- **English Statement**: *"You are given a list of valid triples $\mathcal{T} \subseteq A \times X \times B$ (for example, machine $x_1$ can do task $b_1$ ONLY if operated by worker $a_1$, OR can do task $b_2$ ONLY if operated by worker $a_2$). Choose the maximum number of disjoint triples."*
- **Why Any Flow Network Fails (The "Flow Amnesia" Counterexample)**:
  Suppose machine $x_1$ has two valid triples: $(a_1, x_1, b_1)$ and $(a_2, x_1, b_2)$.
  If we place $x_1$ in the middle ($A \to X \to B$), we must add edges $a_1 \to x_{1,\text{in}}$, $a_2 \to x_{1,\text{in}}$ and $x_{1,\text{out}} \to b_1$, $x_{1,\text{out}} \to b_2$.
  Once a unit of flow from $a_1$ arrives at $x_{1,\text{in}}$ and crosses $x_{1,\text{in}} \to x_{1,\text{out}}$, **the flow forgets that it came from $a_1$**! It can exit to $b_2$, forming the **invalid triple $(a_1, x_1, b_2) \notin \mathcal{T}$**!
  Wait—what if we create a separate node $t_{\text{in}} \to t_{\text{out}}$ for each valid triple $t = (a, x, b) \in \mathcal{T}$? Even then, each triple $t$ has **three** degree-1 constraints ($a \in A$, $x \in X$, $b \in B$), whereas a flow edge only has **two** endpoints (one tail $+1$ and one head $-1$)! In the constraint matrix $M x \le \mathbf{1}$ where each column $t = (a, x, b)$ has **three $1$s**, no row negation can reduce three $1$s per column to one $+1$ and one $-1$!

---

#### Boundary Line 4: Two-Commodity Flow & Paired Equal-Flow Edges $\implies$ NP-Hard

Another frequent trap is **Integer Two-Commodity Flow (`双物资整数流`)** or **Homologous / Paired Flow (`同源等流边`, requiring $f(e_1) = f(e_2)$ on two non-series edges)**:

**Theorem 40.4 (Even, Itai & Shamir 1976 — NP-Completeness of 2-Commodity Integer Flow)**:
Given a directed (or undirected) network $G = (V, E)$ with unit edge capacities and two source-sink pairs $(s_1, t_1)$ and $(s_2, t_2)$ requiring integer flows $F_1 = d_1$ and $F_2 = d_2$, deciding whether a feasible **integer** 2-commodity flow exists is **NP-complete** (even when $d_1 = d_2 = 1$, which is the **2-Disjoint Directed Paths Problem** on general directed graphs!).

---

### 40.4 Step 4 — Hand-Checkable Counterexamples & The "Flow Amnesia" Diagnostic Test

Let us write out the concrete $N = 4$ counterexample showing why **2-Commodity Flow** and **3-Matroid Intersection** have a strictly fractional LP relaxation ($\det = \pm 2$) and fail integer flow:

```
COUNTEREXAMPLE 1: The 2-Commodity Half-Integral Trap (det = 2)
  Consider an undirected 4-cycle 1 - 2 - 3 - 4 - 1 where every edge has capacity 1.
  Commodity 1 wants to send flow from s_1 = 1 to t_1 = 3.
  Commodity 2 wants to send flow from s_2 = 2 to t_2 = 4.
  - INTEGER OPTIMUM = 1: Any path from 1 to 3 (either 1-2-3 or 1-4-3) uses two edges and
    disconnects 2 from 4! So at most 1 unit of total integer flow can be routed.
  - FRACTIONAL LP OPTIMUM = 2: Send 0.5 units of Commodity 1 along 1-2-3 and 0.5 along 1-4-3;
    send 0.5 units of Commodity 2 along 2-3-4 and 0.5 along 2-1-4. Every edge carries
    0.5 + 0.5 = 1.0 unit of flow, achieving total fractional flow 1.0 + 1.0 = 2.0!
  - WHY? The path-edge incidence matrix of the 4 paths has determinant:
      det [ 1  0  1  0 ]
          [ 1  0  0  1 ]
          [ 0  1  0  1 ]
          [ 0  1  1  0 ] = -2 != {-1, 0, +1}!

COUNTEREXAMPLE 2: The "Wrong Layer Order" Trap in 3-Partite Flow
  Suppose Workers A = {a1, a2}, Machines X = {x1, x2}, Tasks B = {b1, b2}.
  - Machine x1 works with A(x1) = {a1} and B(x1) = {b1}  (only triple (a1, x1, b1) valid for x1).
  - Machine x2 works with A(x2) = {a1, a2} and B(x2) = {b2} (triples (a1, x2, b2), (a2, x2, b2)).
  Suppose b1 is NOT available (say capacity of b1 -> T is 0), and we want to know if we can
  run 1 task using ONLY Machine x1 (so S -> x1 has capacity 1, S -> x2 has capacity 0).
  - Real Answer: 0 (Machine x1 can ONLY do task b1, which has capacity 0).
  - Broken Graph (S -> X -> A -> B -> T):
    Since a1 in A(x2) and b2 in B(x2), the layer A -> B contains the edge a1 -> b2!
    Then 1 unit of flow travels: S -> x1 -> a1 -> b2 -> T!
    The flow used Machine x1 with Worker a1 to perform Task b2 (which only Machine x2 can do)!
```

---

## Master Recognition & Compilation Decision Table (Wave 4B Synthesis)

Use this rapid-lookup diagnostic matrix whenever an optimization problem resists direct flow conservation or standard project closure:

| Surface Problem Signature | Underlying Mathematical Structure | Integrality / Complexity Status | Exact Compilation Target |
| :--- | :--- | :--- | :--- |
| Optimize $\sum b_v \pi_v$ subject to hard difference constraints $\pi_v - \pi_u \le c_{uv}$ | Dual of Uncapacitated Min-Cost Circulation ($A^T$ of Family 1) | **TU ($\det \in \{0, \pm 1\}$)** — Exact Integer Potentials & Flows | Directed edge $u \to v$ with **capacity $\infty$, cost $c_{uv}$**; vertex supply $\text{in}(v) - \text{out}(v) = b_v$ |
| Elastic difference bounds $\pi_v - \pi_u - z_{uv} \le c_{uv}$ with penalty $+u_{uv} z_{uv}$ ($z_{uv} \ge 0$) | Dual of Capacitated Min-Cost Flow (Iteration 36.4) | **TU ($\det \in \{0, \pm 1\}$)** — Exact Integer Potentials & Flows | Directed edge $u \to v$ with **capacity $u_{uv}$, cost $c_{uv}$**; reconstruct $\pi^*(v) = \text{dist}_{G_f}(v)$ |
| Variables $x_j$ are intervals $[l_j, r_j]$ covering points $i \in \{1, \dots, m\}$ | **Column Consecutive-Ones Matrix** $A$ (Family 3) | **TU** ($D A$ has one $+1$ at $l_j$, one $-1$ at $r_j + 1$) | Left-multiply by difference matrix $D$ (`Equation-Difference Method`): edge $l_j \to r_j + 1$ |
| Constraints $j$ sum point variables $x_i$ over intervals $[l_j, r_j]$ (`[ZJOI2013] 防守战线`) | **Row Consecutive-Ones Matrix** $A$ ($A^T$ is Column Consecutive-Ones) | **TU** ($D A^T$ has one $+1$ at $l_j$, one $-1$ at $r_j + 1$) | Take **LP Dual** (or prefix sums $\pi_i = \sum_{k \le i} x_k$), then compile via $D A^T$: edge $l_j \to r_j + 1$ |
| Covering a rooted tree $T$ with **vertical (ancestor–descendant)** paths $u_j \to v_j$ | **Directed Tree Path Incidence Matrix** (Family 4A) | **TU** ($D_T A$ has $+1$ at $u_j$, $-1$ at $v_j$) | Subtract child-edge equations from parent-edge equation (`Tree Difference Flow`): edge $u_j \to v_j$ |
| Covering a tree $T$ with general **V-shaped (leaf-to-leaf)** paths | Undirected Tree Path Incidence Matrix (Family 4B) | **NOT TU** ($K_{1,3}$ star has $\det = 2$) | Cannot compile to flow via $D_T$; use Tree DP, Matching (if cap $1$), or LP if fractional |
| Minimize $\sum w_{uv} |h_u - h_v| + \sum g_v(h_v)$ over continuous/integer $h \in \mathbb{R}^V$ | **Lovász Extension $\hat{f}(h)$** of Submodular Graph Cut $f(S)$ | **Zero Integrality Gap** via Nested Level Cuts | Coarea Layer-Cake Decomposition (`CF 1427G`) or Parallel Binary Search (`保序回归`) |
| Maximize $\sum w_i x_i$ over Base Polyhedron $B(f)$ of submodular $f : 2^V \to \mathbb{R}$ | Single Polymatroid Optimization (Iteration 39.3) | **Exact Greedy Integrality** in $O(n \log n)$ | **Edmonds' Greedy Algorithm**: sort $w_{v_1} \ge \dots \ge w_{v_n}$, set $x^*_{v_k} = f(S_k) - f(S_{k-1})$ |
| Common independent set of **2 Partition / Laminar Matroids** $M_1 \cap M_2$ | Bipartite / Laminar Submodular Flow (Boundary 1) | **TU / TDI** — Solvable via Dinic / MCMF | Build $M_1$ out-tree from $S$, $M_2$ in-tree to $T$, connect each $e \in E$ from $M_1(e) \to M_2(e)$ |
| Common independent set of **Graphic + Color/Linear Matroids** $M_1 \cap M_2$ | General 2-Matroid Intersection (Boundary 2) | **TDI (Polynomial)**, but **NOT a Static Flow** | **Edmonds' Matroid Intersection Algorithm** on dynamic exchange graph $G(I)$ in $O(r^2 m)$ |
| 3-Attribute Matching where $a \in A(x)$ and $b \in B(x)$ are **independent given $x \in X$** | Two Partition Matroids coupled through bottleneck $X$ | **Polynomial Max-Flow** (ONLY if $X$ is in the middle!) | **Must place $X$ in the middle**: $S \to A \to X_{\text{in}} \to X_{\text{out}} \to B \to T$ |
| Coupled triples $(a, x, b) \in \mathcal{T}$ or 3 Partition Matroids $M_1 \cap M_2 \cap M_3$ | **3-Dimensional Matching (3DM)** (Boundary 3B) | **NP-Hard** ($\det \ge 2$, Flow Amnesia in $A \to X \to B$) | Exponential Bitmask DP, Meet-in-the-Middle, or Randomized Algebraic Pfaffian/Tutte (if special) |

---

## 4-Tier Curated Problem Bank (Part 1: Stepping Stone & Intermediate — Problems P01 to P10)

Every problem in this curated bank has been selected for its **non-template modelling depth** (all bare library verification problems are quarantined in the `R-XX` table at the end of Part 2). Each problem is presented with its full 4-Step "Zero Magic Gadgets" derivation and 3-tier progressive hints.

---

### Tier 1: Stepping Stone Problems (P01–P05)

---

#### Problem P01: `[USACO07OPEN] Dining G` (3-Attribute Bottleneck Placement vs. 3D Matching Trap)

- **Judge URL**: [Luogu P2891](https://www.luogu.com.cn/problem/P2891) / [POJ 3281](http://poj.org/problem?id=3281) (`[EN]` / `[ZH]`)
- **Constraints**: $N \le 100$ cows, $F \le 100$ foods, $D \le 100$ drinks. Each food and each drink can be consumed by at most $1$ cow. Each cow $i$ has a subset of acceptable foods $F_i \subseteq \{1, \dots, F\}$ and acceptable drinks $D_i \subseteq \{1, \dots, D\}$. Maximize the number of cows that receive both an acceptable food and an acceptable drink.
- **Step 1 — Non-Graph Diagnostic Signal**:
  We are matching triples $(\text{food } f, \text{cow } i, \text{drink } d)$ where each food, cow, and drink has capacity $1$. Why isn't this NP-hard 3-Dimensional Matching? Because for a given cow $i$, her food preference $f \in F_i$ and drink preference $d \in D_i$ are **decoupled**: $(f, i, d)$ is valid if and only if $f \in F_i$ AND $d \in D_i$! Thus cow $i$ acts as the single coupling bottleneck between two Partition Matroids ($F$ and $D$).
- **Step 2 — Intermediate Algebraic Representation**:
  Let $x_{f, i} \in \{0, 1\}$ indicate whether cow $i$ gets food $f \in F_i$, and $y_{i, d} \in \{0, 1\}$ indicate whether cow $i$ gets drink $d \in D_i$. A cow $i$ is satisfied ($z_i = 1$) iff:
  $$\sum_{f \in F_i} x_{f, i} \ge z_i, \qquad \sum_{d \in D_i} y_{i, d} \ge z_i, \qquad z_i \le 1,$$
  subject to $\sum_i x_{f, i} \le 1$ and $\sum_i y_{i, d} \le 1$. By setting $\sum_{f \in F_i} x_{f, i} = z_i = \sum_{d \in D_i} y_{i, d}$, we obtain exact flow conservation through cow $i$:
  $$\underbrace{\sum_{f \in F_i} x_{f, i}}_{\text{inflow to } i_{\text{in}}} = \underbrace{z_i}_{\text{flow on } i_{\text{in}} \to i_{\text{out}} \le 1} = \underbrace{\sum_{d \in D_i} y_{i, d}}_{\text{outflow from } i_{\text{out}}}.$$
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  1. **Source to Foods**: $S \to f$ with capacity $1$ for each $f \in \{1, \dots, F\}$.
  2. **Foods to Cow In-Nodes**: $f \to i_{\text{in}}$ with capacity $1$ for each $f \in F_i$.
  3. **Cow Bottleneck Split Edge (CRITICAL)**: $i_{\text{in}} \to i_{\text{out}}$ with capacity $1$ for each cow $i \in \{1, \dots, N\}$.
  4. **Cow Out-Nodes to Drinks**: $i_{\text{out}} \to d$ with capacity $1$ for each $d \in D_i$.
  5. **Drinks to Sink**: $d \to T$ with capacity $1$ for each $d \in \{1, \dots, D\}$.
  Since this is a unit-network with $V = F + 2N + D + 2 \le 402$, Dinic runs in $O(E \sqrt{V})$ time.

::: {.callout-tip collapse="true"}
##### Progressive Hints & Failure Mode Analysis (P01)
- **Hint 1 (Recognition)**: Notice that there are three disjoint sets of objects (Foods, Cows, Drinks), each with capacity $1$. Which of the three sets links the other two?
- **Hint 2 (Algebraic Model)**: Can a cow $i$ eat food $f_1 \in F_i$ and drink $d_2 \in D_i$ simultaneously even if $f_1$ and $d_2$ have no direct edge? Yes—all compatibility is mediated through cow $i$.
- **Hint 3 (Failure Mode — The Wrong Layer Order Trap)**:
  What breaks if you build $S \to \text{Cow} \to \text{Food} \to \text{Drink} \to T$? You would have to put edges between Food $f$ and Drink $d$ whenever *some* cow likes both $f$ and $d$; then Cow $1$ could send flow to Food $f_1 \in F_1$, which crosses to Drink $d_2 \in D_2 \setminus D_1$ via an edge created for Cow $2$! And what breaks if you don't split Cow $i$ into $i_{\text{in}} \to i_{\text{out}}$ of capacity $1$? Then Cow $i$ could absorb $2$ foods and $2$ drinks, counting as $2$ satisfied cows!
:::

---

#### Problem P02: `[NOI2008] 志愿者招募` (Dual Equivalence of Consecutive-Ones $DA$ vs. LP Dual Potentials)

- **Judge URL**: [Luogu P3980](https://www.luogu.com.cn/problem/P3980) / [LOJ 6008](https://loj.ac/p/6008) (`[ZH]`)
- **Constraints**: $n \le 1000$ days, $m \le 10000$ volunteer types. Day $i$ requires at least $a_i$ volunteers. Volunteer type $j$ works across contiguous days $[l_j, r_j]$ at cost $c_j$ per person (unlimited supply). Find the minimum total cost.
- **Step 1 — Non-Graph Diagnostic Signal**:
  We have an ILP $\min \sum_{j=1}^m c_j x_j$ subject to $Ax \ge a, x \ge 0$, where the $j$-th column of $A \in \{0, 1\}^{n \times m}$ has $1$s on the contiguous interval $[l_j, r_j]$. Thus $A$ has the **Column Consecutive-Ones Property** (Family 3 of Iteration 38) and is Totally Unimodular!
- **Step 2 — Dual Algebraic Perspectives (Comparing $DA$ vs. LP Dual)**:
  In Wave 3B we multiplied $Ax - s = a$ on the left by the difference matrix $D$. Now let us solve it via **Iteration 36's Explicit LP Dual** to see why both yield the exact same MCMF structure:
  - Write the Primal LP: $\min \sum_{j=1}^m c_j x_j$ subject to $\sum_{j : i \in [l_j, r_j]} x_j \ge a_i$ (dual variable $y_i \ge 0$).
  - Take the Dual LP:
    $$\text{Maximize } \sum_{i=1}^n a_i y_i \quad \text{subject to} \quad \sum_{i=l_j}^{r_j} y_i \le c_j \quad \forall j \in \{1, \dots, m\}, \quad y_i \ge 0.$$
  - Substitute **Dual Prefix-Sum Potentials** $\pi_i = \sum_{k=1}^i y_k$ (with $\pi_0 = 0$):
    Since $y_i = \pi_i - \pi_{i-1} \ge 0$ and $\sum_{i=l_j}^{r_j} y_i = \pi_{r_j} - \pi_{l_j - 1} \le c_j$, the Dual LP becomes:
    $$\begin{aligned}
    \text{Maximize} \quad & \sum_{i=1}^n a_i (\pi_i - \pi_{i-1}) = a_n \pi_n + \sum_{i=1}^{n-1} (a_i - a_{i+1}) \pi_i - a_1 \pi_0 \\
    \text{subject to} \quad & \pi_{r_j} - \pi_{l_j - 1} \le c_j \quad && \forall j \in \{1, \dots, m\} \quad (\text{hard difference constraint } \implies \text{edge } l_j - 1 \to r_j), \\
    & \pi_{i-1} - \pi_i \le 0 \quad && \forall i \in \{1, \dots, n\} \quad (\text{monotonicity } y_i \ge 0 \implies \text{edge } i \to i-1).
    \end{aligned}$$
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  Applying the Compiler from Section 36.4 to the Dual Potential LP on vertices $0, 1, \dots, n$:
  1. Each constraint $\pi_{r_j} - \pi_{l_j - 1} \le c_j$ compiles to a directed edge $l_j - 1 \to r_j$ with **capacity $\infty$ and cost $c_j$** (flow variable $x_j$!).
  2. Each constraint $\pi_{i-1} - \pi_i \le 0$ compiles to a directed edge $i \to i - 1$ with **capacity $\infty$ and cost $0$** (slack variable $s_i$!).
  3. Each objective term $(a_i - a_{i+1}) \pi_i$ (with $a_0 = a_{n+1} = 0$) sets the vertex demand $\text{in}(i) - \text{out}(i) = a_i - a_{i+1}$:
     - If $a_{i+1} - a_i > 0$, connect $S \to i$ with capacity $a_{i+1} - a_i$ and cost $0$.
     - If $a_i - a_{i+1} > 0$, connect $i \to T$ with capacity $a_i - a_{i+1}$ and cost $0$.
  *(Up to shifting vertex labels by $+1$, this Dual Potential compilation produces the exact same graph as multiplying the Primal by $D$!)*

::: {.callout-tip collapse="true"}
##### Progressive Hints (P02)
- **Hint 1**: Write the integer linear program for volunteer counts $x_j \ge 0$. Why is the constraint matrix Totally Unimodular?
- **Hint 2**: Either subtract day $(i-1)$'s equation from day $i$'s equation in the Primal, OR take the LP Dual and let $\pi_i = \sum_{k=1}^i y_k$ be prefix sums of the dual day prices $y_k$.
- **Hint 3**: Check how each interval $[l_j, r_j]$ becomes $\pi_{r_j} - \pi_{l_j - 1} \le c_j$, which is the dual of a single directed edge from $l_j - 1$ to $r_j$ of cost $c_j$ and capacity $\infty$.
:::

---

#### Problem P03: `[ZJOI2013] 防守战线` (Row Consecutive-Ones Matrix via LP Dual to Max-Cost Flow)

- **Judge URL**: [Luogu P3337](https://www.luogu.com.cn/problem/P3337) (`[ZH]`)
- **Constraints**: $n \le 1000$ positions, $m \le 10000$ interval demands $[l_j, r_j]$ requiring $\ge d_j$ towers. Position $i$ costs $c_i$ and can hold at most $1$ tower ($x_i \in \{0, 1\}$). Minimize total tower cost.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Here the constraint matrix $A \in \{0, 1\}^{m \times n}$ has $1$s on $[l_j, r_j]$ in **Row $j$** (**Row Consecutive-Ones Property**), with $m = 10000 \gg n = 1000$. Subtracting rows in the Primal fails because the rows are arbitrary intervals $[l_j, r_j]$. However, **transposing $A \mapsto A^T$ by taking the LP Dual** turns Row Consecutive-Ones into **Column Consecutive-Ones** on just $n + 1 = 1001$ vertices!
- **Step 2 — Intermediate Algebraic Representation**:
  As derived in Section 36.5 (Compilation 1), the Primal LP is $\min \sum_{i=1}^n c_i x_i$ subject to $\sum_{i=l_j}^{r_j} x_i \ge d_j$ ($f_j \ge 0$) and $-x_i \ge -1$ ($g_i \ge 0$). Its Dual LP is:
  $$\text{Maximize } \sum_{j=1}^m d_j f_j - \sum_{i=1}^n g_i \quad \text{subject to} \quad \sum_{j : i \in [l_j, r_j]} f_j - g_i + s_i = c_i \quad \forall i \in \{1, \dots, n\}.$$
  Left-multiplying by the $(n+1) \times (n+1)$ difference matrix $D$ gives at each vertex $i \in \{1, \dots, n+1\}$ (with $c_0 = c_{n+1} = 0$):
  $$\sum_{j : l_j = i} f_j - \sum_{j : r_j + 1 = i} f_j + (s_i - s_{i-1}) - (g_i - g_{i-1}) = c_i - c_{i-1}.$$
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  1. Vertices $1, \dots, n+1$, source $S$, sink $T$.
  2. For each interval $j \in \{1, \dots, m\}$: directed edge $l_j \to r_j + 1$ with capacity $\infty$, cost $-d_j$ (for Min-Cost Max-Flow; negate the final answer).
  3. For each position $i \in \{1, \dots, n\}$:
     - Slack $s_i$: directed edge $i \to i + 1$ with capacity $\infty$, cost $0$.
     - Upper bound $g_i$: directed edge $i + 1 \to i$ with capacity $\infty$, cost $+1$.
  4. Vertex supply $b_i = c_i - c_{i-1}$: if $b_i > 0$, edge $S \to i$ (cap $b_i$, cost $0$); if $b_i < 0$, edge $i \to T$ (cap $-b_i$, cost $0$).

::: {.callout-tip collapse="true"}
##### Progressive Hints (P03)
- **Hint 1**: Why can't you apply `[NOI2008] 志愿者招募`'s row-subtraction directly to the $m = 10000$ constraints? Because here the *rows* are intervals and the *columns* are single positions!
- **Hint 2**: Take the LP Dual (or substitute prefix sums $\pi_i = \sum_{k=1}^i x_k$ with $0 \le \pi_i - \pi_{i-1} \le 1$). What happens to the constraint matrix when you transpose it?
- **Hint 3**: Remember to include the $x_i \le 1$ upper-bound dual variable $g_i \ge 0$, which becomes a reverse edge $i+1 \to i$ of capacity $\infty$ and cost $+1$ (or reward $-1$).
:::

---

#### Problem P04: `Codeforces 362E — Petya and Pipes` (Elastic Cut Dual / Capacity Expansion under Budget $K$)

- **Judge URL**: [Codeforces 362E](https://codeforces.com/problemset/problem/362/E) (`[EN]`)
- **Constraints**: $n \le 50$ vertices, directed edges $(u, v)$ with initial capacity $u_{uv} \ge 0$. You can increase the capacity of any existing edge $(u, v)$ by any integer amount $z_{uv} \ge 0$ at cost $1$ per unit of increase, up to a total budget of $\sum_{(u,v) \in E} z_{uv} \le K$ ($K \le 1000$). Maximize the total flow from $1$ to $n$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Instead of fixed capacities, each edge $(u, v)$ has two regimes: using the first $u_{uv}$ units of capacity is **free** (cost $0$), and using additional capacity $z_{uv} \ge 0$ beyond $u_{uv}$ costs **$1$ per unit**, subject to a global cost budget $\le K$.
- **Step 2 — Intermediate Algebraic Representation**:
  Let $f_{uv} = f^{(0)}_{uv} + z_{uv}$ be the total flow on edge $(u, v)$, where $0 \le f^{(0)}_{uv} \le u_{uv}$ has cost $0$ and $z_{uv} \ge 0$ has cost $1$.
  For any target total flow $F$, the minimum expansion cost to achieve flow $F$ is the Primal MCMF LP:
  $$C(F) = \min \left\{ \sum_{(u,v) \in E} 1 \cdot z_{uv} : \text{flow conservation of volume } F, \; 0 \le f^{(0)}_{uv} \le u_{uv}, \; z_{uv} \ge 0 \right\}.$$
  And by LP Duality (compare Compilation 2 in Section 36.5!), this is dual to finding a fractional cut $d_v - d_u + y_{uv} \ge 0$ where $y_{uv} \le 1$. Since $C(F)$ is convex and piecewise-linear with integer slopes in $F$, we want the maximum $F$ such that $C(F) \le K$.
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  1. For each original directed edge $(u, v) \in E$ with capacity $u_{uv} > 0$:
     - Add **Free Edge**: $u \to v$ with capacity $u_{uv}$ and cost $0$.
     - Add **Expansion Edge**: $u \to v$ with capacity $\infty$ and cost $1$.
  2. Run Successive Shortest Path (SSP) from $1$ to $n$:
     - In each step, find the shortest augmenting path of per-unit cost $d(1, n)$ in the residual graph.
     - If $d(1, n) = 0$, push as much flow as possible (cost $0$).
     - If $d(1, n) > 0$, we can push at most $\lfloor K_{\text{rem}} / d(1, n) \rfloor$ additional units of flow before exhausting the remaining budget $K_{\text{rem}}$. Stop when $K_{\text{rem}} < d(1, n)$ or $n$ is unreachable.

::: {.callout-tip collapse="true"}
##### Progressive Hints (P04)
- **Hint 1**: Notice that an edge $(u, v)$ can carry up to $u_{uv}$ flow for cost $0$, and any amount of additional flow for cost $1$ per unit.
- **Hint 2**: How do you represent a convex piecewise-linear cost function on an edge in MCMF? Split it into two parallel edges!
- **Hint 3**: Only existing edges ($u_{uv} > 0$) may be expanded; do not add expansion edges between vertex pairs that had no pipe initially. When path cost $d(1, n) > 0$, clamp the augmented flow by $\lfloor K_{\text{rem}} / d(1, n) \rfloor$.
:::

---

#### Problem P05: `POJ 3680 — Intervals` / `Luogu SP3871` (Weighted Interval $k$-Packing via Consecutive-Ones TU Matrix)

- **Judge URL**: [POJ 3680](http://poj.org/problem?id=3680) / [Luogu SP3871](https://www.luogu.com.cn/problem/SP3871) (`[EN]` / `[ZH]`)
- **Constraints**: $N \le 200$ open intervals $(l_j, r_j)$ with positive weights $w_j \le 10^5$, and an integer capacity $K \le 1000$. Select a subset of intervals of **maximum total weight** such that no real number $x \in \mathbb{R}$ is covered by more than $K$ selected intervals.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Each decision variable $x_j \in \{0, 1\}$ is an interval $(l_j, r_j)$, and after coordinate compression of all endpoints into $1, 2, \dots, m$ ($m \le 2N$), each interval covers the contiguous range of elementary segments $[l_j, r_j - 1]$. Thus the constraint matrix $A \in \{0, 1\}^{(m-1) \times N}$ has the **Column Consecutive-Ones Property** and is Totally Unimodular!
- **Step 2 — Intermediate Algebraic Representation**:
  After coordinate compression to $1, \dots, m$, the Primal ILP is:
  $$\begin{aligned}
  \text{Maximize} \quad & \sum_{j=1}^N w_j x_j \\
  \text{subject to} \quad & \sum_{j : i \in [l_j, r_j - 1]} x_j + s_i = K \quad && \forall i \in \{1, \dots, m-1\}, \\
  & 0 \le x_j \le 1, \quad s_i \ge 0.
  \end{aligned}$$
  Left-multiply by the $m \times m$ difference matrix $D$ (subtracting equation $i-1$ from equation $i$ for $i = 1, \dots, m$, where equations $0$ and $m$ are $0 = 0$):
  $$\sum_{j : l_j = i} x_j - \sum_{j : r_j = i} x_j + (s_i - s_{i-1}) = \begin{cases} +K & \text{if } i = 1, \\ -K & \text{if } i = m, \\ 0 & \text{if } 2 \le i \le m-1. \end{cases}$$
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  Look at that equation—it is a pure $s$-$t$ flow of volume $K$ from vertex $1$ to vertex $m$!
  1. Vertices $1, 2, \dots, m$ (the coordinate-compressed endpoints), source $S \to 1$ of capacity $K$, sink $m \to T$ of capacity $K$.
  2. For each elementary segment $i \in \{1, \dots, m-1\}$, the slack variable $s_i \ge 0$ compiles to a directed edge $i \to i + 1$ with **capacity $\infty$ and cost $0$**.
  3. For each interval $j \in \{1, \dots, N\}$, the variable $x_j \in [0, 1]$ compiles to a directed edge $l_j \to r_j$ with **capacity $1$ and cost $-w_j$** (reward $+w_j$).
  Since the graph is a DAG on $1 < 2 < \dots < m$, we can initialize Johnson potentials $\pi(v)$ via a single $O(N + m)$ topological DP and run Dijkstra-SSP in $O(K N \log N)$!

::: {.callout-tip collapse="true"}
##### Progressive Hints (P05)
- **Hint 1**: Coordinate-compress the $2N$ endpoints into $m \le 400$ points. Notice that an open interval $(l_j, r_j)$ covers elementary segments $l_j, l_j+1, \dots, r_j-1$.
- **Hint 2**: Add slack $s_i \ge 0$ to turn $\le K$ into $= K$, and multiply by the difference matrix $D$ (subtract row $i-1$ from row $i$).
- **Hint 3**: Notice how every RHS cancels to $0$ except $+K$ at vertex $1$ and $-K$ at vertex $m$! So we simply send $K$ units of flow from $1$ to $m$.
:::

---

### Tier 2: Intermediate Problems (P06–P10)

---

#### Problem P06: `[SHOI2004] 最小生成树` (Inverse MST via LP Duality & Complementary Slackness)

- **Judge URL**: [Luogu P4412](https://www.luogu.com.cn/problem/P4412) (`[ZH]`)
- **Constraints**: $N \le 50$ vertices, $M \le 800$ undirected edges. Each edge $e$ has initial weight $w_e$ and unit modification cost $c_e = 1$ (or general $c_e$ in `[BZOJ 3118]`). Given a target spanning tree $T$, find the minimum total modification cost $\sum_{e \in E} |w'_e - w_e|$ so that $T$ is a Minimum Spanning Tree under $w'$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  This is an **Inverse Optimization Problem**: the spanning tree $T$ is already fixed, and the variables are the edge weight adjustments $x_e = |w'_e - w_e| \ge 0$.
- **Step 2 — Intermediate Algebraic Representation**:
  By the cycle optimality condition for MST, $T$ is an MST under $w'$ iff for every non-tree edge $e_{\text{out}} = (u, v) \notin T$ and every tree edge $e_{\text{in}} \in P_T(u, v)$ on the fundamental tree path between $u$ and $v$:
  $$w'(e_{\text{in}}) \le w'(e_{\text{out}}) \quad \Longleftrightarrow \quad x_{e_{\text{in}}} + x_{e_{\text{out}}} \ge \max\big(0, w(e_{\text{in}}) - w(e_{\text{out}})\big) =: D(e_{\text{in}}, e_{\text{out}}).$$
  The Primal LP $\min \sum_{e \in T} c_e x_e + \sum_{e \notin T} c_e x_e$ subject to $x_{e_{\text{in}}} + x_{e_{\text{out}}} \ge D(e_{\text{in}}, e_{\text{out}})$ is the **Minimum Weighted Vertex Cover / Dual of Maximum-Weight Bipartite $b$-Matching** on the bipartite graph between $T$ ($|T| = N-1$ edges) and $E \setminus T$ ($M - N + 1$ edges)!
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  1. Left bipartite side: tree edges $e_{\text{in}} \in T$, with $S \to e_{\text{in}}$ of capacity $c_{e_{\text{in}}}$ and cost $0$.
  2. Right bipartite side: non-tree edges $e_{\text{out}} \in E \setminus T$, with $e_{\text{out}} \to T_{\text{snk}}$ of capacity $c_{e_{\text{out}}}$ and cost $0$.
  3. For each $e_{\text{out}} = (u, v) \notin T$, traverse the tree path $P_T(u, v)$; for every $e_{\text{in}} \in P_T(u, v)$ with $w(e_{\text{in}}) > w(e_{\text{out}})$, add directed edge $e_{\text{in}} \to e_{\text{out}}$ with capacity $\infty$ and cost $-\big(w(e_{\text{in}}) - w(e_{\text{out}})\big)$.
  4. Run Min-Cost Flow from $S$ to $T_{\text{snk}}$ while the shortest augmenting path has strictly negative cost ($< 0$). Negate the minimum cost to get the answer; if the problem asks for $w'_e$, apply Section 37.4's Complementary Slackness formula $x^*_{e_{\text{in}}} = \max(0, \pi(e_{\text{in}}) - \pi(S))$ and $x^*_{e_{\text{out}}} = \max(0, \pi(T_{\text{snk}}) - \pi(e_{\text{out}}))$!

::: {.callout-tip collapse="true"}
##### Progressive Hints (P06)
- **Hint 1**: When is a given spanning tree $T$ an MST? When no non-tree edge $e_{\text{out}} \notin T$ is strictly lighter than any tree edge $e_{\text{in}}$ on its fundamental cycle!
- **Hint 2**: Would you ever increase a tree edge's weight or decrease a non-tree edge's weight? No! Write the linear inequalities for decreasing $e_{\text{in}} \in T$ by $x_{e_{\text{in}}} \ge 0$ and increasing $e_{\text{out}} \notin T$ by $x_{e_{\text{out}}} \ge 0$.
- **Hint 3**: Notice that every constraint involves one tree edge and one non-tree edge ($x_{e_{\text{in}}} + x_{e_{\text{out}}} \ge D$). Take the LP Dual (or recognize it as Bipartite Dual Kuhn–Munkres / MCMF)!
:::

---

#### Problem P07: `AtCoder ARC 085 E — MUL` (Submodular Function Minimization on the Divisibility Poset)

- **Judge URL**: [AtCoder ARC 085 E](https://atcoder.jp/contests/arc085/tasks/arc085_c) (`[JA]` / `[EN]`)
- **Constraints**: $N \le 100$ gems labeled $1, \dots, N$ with integer values $a_i \in [-10^9, 10^9]$. In one operation, you may choose an integer $x \in \{1, \dots, N\}$ and smash all gems whose indices are multiples of $x$ ($x \mid y$). Maximize the sum of remaining gems.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Let $x_i \in \{0, 1\}$ indicate whether gem $i$ is **kept** ($x_i = 1$) or **smashed** ($x_i = 0$). If we smash $i$ ($x_i = 0$), we are forced to smash every multiple $j = k \cdot i$ ($x_j = 0$). Equivalently, keeping $j$ ($x_j = 1$) requires keeping all its divisors $i \mid j$ ($x_i = 1$):
  $$i \mid j \implies x_j \le x_i \quad \Longleftrightarrow \quad x_j (1 - x_i) = 0.$$
  This is a submodular closure function on the divisibility lattice!
- **Step 2 — Intermediate Algebraic Representation (Primal–Dual Verification)**:
  Write the penalty minimization LP (starting from the optimistic sum $\sum_{a_i > 0} a_i$):
  $$\begin{aligned}
  \text{Minimize} \quad & \sum_{i : a_i > 0} a_i (1 - x_i) + \sum_{i : a_i < 0} (-a_i) x_i \\
  \text{subject to} \quad & x_j - x_i \le 0 \quad \forall i \mid j, \\
  & 0 \le x_i \le 1 \quad \forall i \in \{1, \dots, N\}.
  \end{aligned}$$
  Notice that the constraint matrix is the transpose of a **Directed Network Incidence Matrix** (Family 1 of Iteration 38)! Therefore, by the Hoffman–Kruskal Theorem and Strong LP Duality, the continuous LP relaxation has an exact integer optimum $x^* \in \{0, 1\}^N$ and is dual to an $s$-$t$ Maximum Flow!
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  Let $x_i = 1$ mean $i \in S$ (kept) and $x_i = 0$ mean $i \in T$ (smashed):
  1. For each $i$ with $a_i > 0$: penalty $a_i (1 - x_i) = a_i x_s (1 - x_i)$ compiles to edge $S \to i$ of capacity $a_i$.
  2. For each $i$ with $a_i < 0$: penalty $(-a_i) x_i = (-a_i) x_i (1 - x_t)$ compiles to edge $i \to T$ of capacity $-a_i$.
  3. For each pair $i \mid j$ ($i < j$): hard constraint $x_j (1 - x_i) = 0$ compiles to edge $j \to i$ of capacity $\infty$.
  Answer is $\sum_{a_i > 0} a_i - \text{MinCut}(S, T)$.

::: {.callout-tip collapse="true"}
##### Progressive Hints (P07)
- **Hint 1**: Notice that smashing $x$ smashes all multiples of $x$. Can you ever be forced to smash $y$ without smashing $y$'s multiples? No, because any multiple of $y$ is also a multiple of $x$!
- **Hint 2**: Thus a subset of smashed gems is valid if and only if it is closed under taking multiples: $x \text{ smashed and } x \mid y \implies y \text{ smashed}$.
- **Hint 3**: Formulate this as a submodular cut / closure problem with $\infty$-capacity edges for $i \mid j$.
:::

---

#### Problem P08: `[AHOI2014 / JSOI2014] 支线剧情` (DAG Edge-Coverage Lower Bounds $\leftrightarrow$ Dual Longest-Path Potentials)

- **Judge URL**: [Luogu P4043](https://www.luogu.com.cn/problem/P4043) (`[ZH]`)
- **Constraints**: A rooted DAG with $N \le 300$ vertices (root $1$) and $M \le 5000$ weighted directed edges $e = (u, v)$ of traversal time $w_e \ge 0$. Every playthrough starts at vertex $1$, follows a directed path, and can reset back to vertex $1$ from any vertex $v > 1$ at cost $0$. Find the minimum total time to traverse **every edge $e \in E$ at least once**.
- **Step 1 — Non-Graph Diagnostic Signal**:
  We can view this either as a **Min-Cost Circulation with Edge Lower Bounds** ($f_e \ge 1$ for all $e \in E$) OR via its **LP Dual**: assigning potentials $\pi_v$ to vertices to maximize the sum of lower-bound dual rewards! Let us examine both sides of the duality coin.
- **Step 2 — Intermediate Algebraic Representation**:
  Add a zero-cost return edge $(v, 1)$ of capacity $\infty$ and lower bound $0$ from every vertex $v > 1$ back to $1$.
  - **Primal LP (Circulation with Lower Bounds)**:
    $$\min \sum_{e \in E} w_e f_e \quad \text{subject to} \quad \text{in}_f(v) - \text{out}_f(v) = 0 \; \forall v \in V, \quad f_e \ge 1 \; \forall e \in E, \quad f_{(v,1)} \ge 0.$$
    Substitute $f_e = 1 + f'_e$ with $f'_e \ge 0$:
    $$\sum_{e \in E} w_e + \min \sum_{e \in E} w_e f'_e \quad \text{subject to} \quad \text{in}_{f'}(v) - \text{out}_{f'}(v) = \text{out}_{\text{deg}}(v) - \text{in}_{\text{deg}}(v) =: b_v, \quad f'_e \ge 0.$$
  - **Dual LP (Elastic Potential Modification)**:
    $$\sum_{e \in E} w_e + \max \left\{ \sum_{v \in V} b_v \pi_v : \pi_v - \pi_u \le w_e \; \forall (u,v) \in E, \; \pi_1 - \pi_v \le 0 \; \forall v > 1 \right\}.$$
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  From the substituted Primal LP (with base cost $\sum_{e \in E} w_e$):
  1. For each original edge $e = (u, v) \in E$: add directed edge $u \to v$ with capacity $\infty$ and cost $w_e$ (representing extra traversals $f'_e \ge 0$).
  2. For each $v \in \{2, \dots, N\}$: add return edge $v \to 1$ with capacity $\infty$ and cost $0$.
  3. For each $v \in \{1, \dots, N\}$, compute the mandatory net inflow $\Delta_v = \text{in}_{\text{deg}}(v) - \text{out}_{\text{deg}}(v)$:
     - If $\Delta_v > 0$, add edge $S_{\text{super}} \to v$ with capacity $\Delta_v$ and cost $0$.
     - If $\Delta_v < 0$, add edge $v \to T_{\text{super}}$ with capacity $-\Delta_v$ and cost $0$.
  4. Run Min-Cost Max-Flow from $S_{\text{super}}$ to $T_{\text{super}}$ and add $\sum_{e \in E} w_e$.

::: {.callout-tip collapse="true"}
##### Progressive Hints (P08)
- **Hint 1**: Restarting the game from any vertex $v > 1$ back to vertex $1$ at cost $0$ is equivalent to adding a directed edge $v \to 1$ with cost $0$ and capacity $\infty$.
- **Hint 2**: Every original edge $e \in E$ must carry flow $f_e \ge 1$. Substitute $f_e = 1 + f'_e$ ($f'_e \ge 0$) to absorb the lower bound!
- **Hint 3**: After pre-sending $1$ unit of flow on every edge $e \in E$, each vertex $v$ has a surplus/deficit $\Delta_v = \text{in}_{\text{deg}}(v) - \text{out}_{\text{deg}}(v)$. Balance these via $S_{\text{super}}$ and $T_{\text{super}}$ using Min-Cost Max-Flow!
:::

---

#### Problem P09: `Codeforces 1288F — Red-Blue Graph` (Bipartite Signed Incidence Matrix & Degree-Difference Bounds)

- **Judge URL**: [Codeforces 1288F](https://codeforces.com/problemset/problem/1288/F) (`[EN]`)
- **Constraints**: Bipartite graph $G = (L \sqcup R, E)$ with $|L|, |R|, |E| \le 200$. Each vertex is colored Red (`R`), Blue (`B`), or Uncolored (`U`). Each edge $e \in E$ can be colored Red (cost $r$), Blue (cost $b$), or left uncolored (cost $0$).
  - For every Red vertex $v$, strictly more incident edges must be Red than Blue: $\text{red}(v) - \text{blue}(v) \ge 1$.
  - For every Blue vertex $v$, strictly more incident edges must be Blue than Red: $\text{blue}(v) - \text{red}(v) \ge 1$.
  Find the minimum total cost and output the edge coloring, or report `-1`.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Each edge $e = (u, v)$ with $u \in L, v \in R$ has a **3-state net charge** $x_e \in \{-1, 0, +1\}$, where $x_e = +1$ means Red (cost $r$), $x_e = -1$ means Blue (cost $b$), and $x_e = 0$ means Uncolored (cost $0$). Because $G$ is **bipartite** (Family 2 of Iteration 38!), orienting all edges from $L$ to $R$ makes $x_e = f_{\text{red}}(e) - f_{\text{blue}}(e)$ the exact net flow from $u \in L$ to $v \in R$!
- **Step 2 — Intermediate Algebraic Representation**:
  For each edge $e = (u, v)$ ($u \in L, v \in R$), write $x_e = f^+_e - f^-_e$ where $f^+_e \in \{0, 1\}$ is flow on $u \to v$ (Red, cost $r$) and $f^-_e \in \{0, 1\}$ is flow on $v \to u$ (Blue, cost $b$).
  Then at any vertex $u \in L$, the net outflow is:
  $$\text{out}(u) - \text{in}(u) = \sum_{e \in \delta(u)} (f^+_e - f^-_e) = \text{red}(u) - \text{blue}(u)!$$
  And at any vertex $v \in R$, the net inflow is:
  $$\text{in}(v) - \text{out}(v) = \sum_{e \in \delta(v)} (f^+_e - f^-_e) = \text{red}(v) - \text{blue}(v)!$$
  Thus the Red/Blue vertex constraints are **pure vertex flow balance lower/upper bounds**!
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  Introduce source $S$ and sink $T$ with return edge $T \to S$ of capacity $[0, \infty]$ and cost $0$:
  1. **For each original edge $e = (u, v)$ ($u \in L, v \in R$)**:
     - Red choice: directed edge $u \to v$ with lower bound $0$, upper bound $1$, cost $r$.
     - Blue choice: directed edge $v \to u$ with lower bound $0$, upper bound $1$, cost $b$.
  2. **For each left vertex $u \in L$** (where net outflow from $u$ to $R$ is $\text{red}(u) - \text{blue}(u)$, which must equal inflow from $S \to u$ minus outflow $u \to T$):
     - If $u$ is `R` ($\text{red}(u) - \text{blue}(u) \ge 1$): add edge $S \to u$ with capacity $[1, \infty]$, cost $0$.
     - If $u$ is `B` ($\text{red}(u) - \text{blue}(u) \le -1$): add edge $u \to T$ with capacity $[1, \infty]$, cost $0$.
     - If $u$ is `U` ($-\infty < \text{red}(u) - \text{blue}(u) < \infty$): add both $S \to u$ and $u \to T$ with capacity $[0, \infty]$, cost $0$.
  3. **For each right vertex $v \in R$** (where net inflow from $L$ to $v$ is $\text{red}(v) - \text{blue}(v)$, which must equal outflow $v \to T$ minus inflow $S \to v$):
     - If $v$ is `R` ($\text{red}(v) - \text{blue}(v) \ge 1$): add edge $v \to T$ with capacity $[1, \infty]$, cost $0$.
     - If $v$ is `B` ($\text{red}(v) - \text{blue}(v) \le -1$): add edge $S \to v$ with capacity $[1, \infty]$, cost $0$.
     - If $v$ is `U`: add both $S \to v$ and $v \to T$ with capacity $[0, \infty]$, cost $0$.
  Resolve the lower bounds $[1, \infty]$ via $S_{\text{super}}, T_{\text{super}}$ and run MCMF!

::: {.callout-tip collapse="true"}
##### Progressive Hints (P09)
- **Hint 1**: Why is the graph guaranteed to be *bipartite*? What happens if you orient Red edges $L \to R$ and Blue edges $R \to L$?
- **Hint 2**: With that orientation, for $u \in L$, $\text{red}(u) - \text{blue}(u)$ is $\text{out}(u) - \text{in}(u)$; for $v \in R$, $\text{red}(v) - \text{blue}(v)$ is $\text{in}(v) - \text{out}(v)$!
- **Hint 3**: Can both $u \to v$ (cost $r > 0$) and $v \to u$ (cost $b > 0$) carry $1$ unit of flow in an optimal solution? No, because they form a positive-cost 2-cycle $u \to v \to u$ of cost $r + b > 0$, which MCMF never uses!
:::

---

#### Problem P10: `[BZOJ 1937]` / `Directed Tree Path Coverage` (Tree Incidence Difference Matrix $D_T$ Compilation)

- **Judge URL**: [Luogu P4412 Variant / BZOJ 1937](https://www.luogu.com.cn/problem/P4412) & [Codeforces 1051G / Tree Path LP Archetype](https://codeforces.com/problemset) (`[ZH]` / `[EN]`)
- **Constraints**: Given a rooted tree $T = (V, E_T)$ on $N \le 1000$ vertices (root $1$), where each tree edge $e = (p(u), u) \in E_T$ requires at least $b_u \ge 0$ units of coverage. You are given $M \le 10000$ vertical paths $(u_j, v_j)$, where $v_j$ is an ancestor of $u_j$, each usable up to $d_j$ times at unit cost $c_j \ge 0$. Find the minimum total cost to cover all tree edges.
- **Step 1 — Non-Graph Diagnostic Signal**:
  This is the exact 2D/Tree generalization of `[NOI2008] 志愿者招募`! Because every path $(u_j, v_j)$ goes strictly vertically from a descendant $u_j$ up to an ancestor $v_j$, the edge-path incidence matrix $A \in \{0, 1\}^{(N-1) \times M}$ belongs to **Family 4A (Directed Tree Path Incidence Matrices)** of Iteration 38 and is **Totally Unimodular**!
- **Step 2 — Intermediate Algebraic Representation (Tree Difference Matrix $D_T$)**:
  For each non-root vertex $u \in V \setminus \{1\}$, let $E_u$ be the equation for the tree edge $(p(u), u)$ above $u$:
  $$\sum_{j : (p(u), u) \in P(u_j, v_j)} x_j - s_u = b_u \qquad (0 \le x_j \le d_j, \; s_u \ge 0).$$
  For the root $1$, define the dummy equation $E_1 : 0 = 0$.
  Now apply the **Tree Difference Operator $D_T$**: for every vertex $w \in V$, subtract the sum of equations of all children $c \in \text{child}(w)$ from $E_w$:
  $$\Delta E_w := E_w - \sum_{c \in \text{child}(w)} E_c.$$
  Let us check the coefficient of variable $x_j$ (vertical path from $u_j$ up to ancestor $v_j$) in $\Delta E_w$:
  - If $w = u_j$: $x_j$ is in $E_{u_j}$ ($+1$) and in none of $u_j$'s children ($0$), so net coefficient is **$+1$**!
  - If $w$ is strictly between $u_j$ and $v_j$: $x_j$ is in $E_w$ ($+1$) and in exactly one child of $w$ ($-1$), so net coefficient is **$1 - 1 = 0$**!
  - If $w = v_j$: $x_j$ is not in $E_{v_j}$ ($0$) and is in the one child of $v_j$ on the path ($-1$), so net coefficient is **$-1$**!
  Every vertical path $(u_j, v_j)$ collapses to $+1$ at $u_j$ and $-1$ at $v_j$!
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  From $\Delta E_w = b_w - \sum_{c \in \text{child}(w)} b_c$ (with $b_1 = 0$):
  1. Vertices $1, 2, \dots, N$, plus super-source $S$ and super-sink $T$.
  2. **Vertical Path Variable $x_j \in [0, d_j]$**: has $+1$ at $u_j$ and $-1$ at $v_j \implies$ directed edge $u_j \to v_j$ with **capacity $d_j$ and cost $c_j$**.
  3. **Slack Variable $s_u \ge 0$** (for $u \ne 1$): has $-1$ in $E_u$ (hence $-1$ at $u$) and $+1$ in $\Delta E_{p(u)}$ (hence $+1$ at $p(u)$) $\implies$ directed edge $p(u) \to u$ with **capacity $\infty$ and cost $0$**!
  4. **Vertex Supply/Demand** $B_w = b_w - \sum_{c \in \text{child}(w)} b_c$:
     - If $B_w > 0$, connect $S \to w$ with capacity $B_w$ and cost $0$.
     - If $B_w < 0$, connect $w \to T$ with capacity $-B_w$ and cost $0$.
  Run Min-Cost Max-Flow from $S$ to $T$!

::: {.callout-tip collapse="true"}
##### Progressive Hints (P10)
- **Hint 1**: Why is a 1D array just a tree where every vertex has at most $1$ child? How do you generalize subtracting $E_{i-1}$ from $E_i$ to a branching tree?
- **Hint 2**: For each node $w$, subtract the sum of all its children's edge equations $\sum_{c \in \text{child}(w)} E_c$ from $w$'s parent-edge equation $E_w$!
- **Hint 3**: Verify that every vertical path $u_j \to v_j$ cancels out at all intermediate vertices and leaves $+1$ at $u_j$ and $-1$ at $v_j$. Why would this fail if a path went up to $\text{LCA}(u_j, v_j)$ and back down? (Because it would have $+1$ at both $u_j$ and $v_j$ and $-2$ at $\text{LCA}$!)
:::

---

## 4-Tier Curated Problem Bank (Part 2: Advanced & Mastery — Problems P11 to P20)

---

### Tier 3: Advanced Problems (P11–P15)

---

#### Problem P11: `[BZOJ 3118] Orz the Immortal` (Weighted Inverse MST with Asymmetric Increase/Decrease Costs & Dual LP)

- **Judge URL**: [Luogu P4412 Generalized / BZOJ 3118](https://darkbzoj.cc/problem/3118) (`[ZH]`)
- **Constraints**: $N \le 300$ vertices, $M \le 1000$ undirected edges. Each edge $e \in E$ has initial weight $w_e$, a status flag $t_e \in \{0, 1\}$ indicating whether $e$ belongs to the given spanning tree $T$, an increase cost $a_e$ per unit, and a decrease cost $b_e$ per unit. Modify edge weights $w_e \mapsto w'_e$ at minimum total cost so that $T$ is a Minimum Spanning Tree of $G$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  In this general weighted Inverse MST problem, tree edges $e_{\text{in}} \in T$ only ever need to be *decreased* by $x_{e_{\text{in}}} \ge 0$ (at unit cost $b_{e_{\text{in}}}$), and non-tree edges $e_{\text{out}} \notin T$ only ever need to be *increased* by $x_{e_{\text{out}}} \ge 0$ (at unit cost $a_{e_{\text{out}}}$). With $N \le 300$ and $M \le 1000$, the Primal LP has $M \le 1000$ variables and up to $O(N M)$ cycle constraints—far too many constraints for Simplex, but its **LP Dual** is a sparse bipartite MCMF network on $M$ vertices!
- **Step 2 — Intermediate Algebraic Representation**:
  Primal LP:
  $$\min \sum_{e_{\text{in}} \in T} b_{e_{\text{in}}} x_{e_{\text{in}}} + \sum_{e_{\text{out}} \notin T} a_{e_{\text{out}}} x_{e_{\text{out}}} \quad \text{s.t.} \quad x_{e_{\text{in}}} + x_{e_{\text{out}}} \ge w(e_{\text{in}}) - w(e_{\text{out}}) \quad \forall e_{\text{out}} \notin T, \; \forall e_{\text{in}} \in P_T(e_{\text{out}}), \quad x_e \ge 0.$$
  Dual LP (with flow variable $f(e_{\text{in}}, e_{\text{out}}) \ge 0$ for each conflicting pair):
  $$\begin{aligned}
  \text{Maximize} \quad & \sum_{e_{\text{out}} \notin T} \sum_{e_{\text{in}} \in P_T(e_{\text{out}})} \max\big(0, w(e_{\text{in}}) - w(e_{\text{out}})\big) f(e_{\text{in}}, e_{\text{out}}) \\
  \text{subject to} \quad & \sum_{e_{\text{out}} : e_{\text{in}} \in P_T(e_{\text{out}})} f(e_{\text{in}}, e_{\text{out}}) \le b_{e_{\text{in}}} \quad \forall e_{\text{in}} \in T, \\
  & \sum_{e_{\text{in}} \in P_T(e_{\text{out}})} f(e_{\text{in}}, e_{\text{out}}) \le a_{e_{\text{out}}} \quad \forall e_{\text{out}} \notin T, \quad f \ge 0.
  \end{aligned}$$
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  1. Left vertices: $N - 1$ tree edges $e_{\text{in}} \in T$, with $S \to e_{\text{in}}$ of capacity $b_{e_{\text{in}}}$ and cost $0$.
  2. Right vertices: $M - N + 1$ non-tree edges $e_{\text{out}} \notin T$, with $e_{\text{out}} \to T_{\text{snk}}$ of capacity $a_{e_{\text{out}}}$ and cost $0$.
  3. Cross edges: For each $e_{\text{out}} = (u, v) \notin T$, find the unique tree path $P_T(u, v)$ by DFS/LCA. For each $e_{\text{in}} \in P_T(u, v)$ with $w(e_{\text{in}}) > w(e_{\text{out}})$, add directed edge $e_{\text{in}} \to e_{\text{out}}$ with capacity $\infty$ and cost $-\big(w(e_{\text{in}}) - w(e_{\text{out}})\big)$.
  4. Run Min-Cost Flow from $S$ to $T_{\text{snk}}$, stopping as soon as the shortest path cost is $\ge 0$ (or add a bypassing edge $S \to T_{\text{snk}}$ of capacity $\infty$, cost $0$).

::: {.callout-tip collapse="true"}
##### Progressive Hints (P11)
- **Hint 1**: Notice that the $a_e$ cost for tree edges and the $b_e$ cost for non-tree edges are **red herrings**—increasing a tree edge or decreasing a non-tree edge only hurts $T$'s MST optimality!
- **Hint 2**: Formulate the Primal LP in $x_e \ge 0$ and take its mechanical LP Dual. Why do $b_{e_{\text{in}}}$ and $a_{e_{\text{out}}}$ become edge capacities in the Dual?
- **Hint 3**: Because Dual inequalities are $\le b_{e_{\text{in}}}$ and $\le a_{e_{\text{out}}}$ (rather than $= $), stop MCMF augmentation as soon as the shortest path from $S$ to $T_{\text{snk}}$ has cost $\ge 0$.
:::

---

#### Problem P12: `AtCoder ARC 107 F — Sum of Abs` (Submodular 3-State Sign Cut & Dual Potential Verification)

- **Judge URL**: [AtCoder ARC 107 F](https://atcoder.jp/contests/arc107/tasks/arc107_f) (`[JA]` / `[EN]`)
- **Constraints**: Undirected graph $G = (V, E)$ with $N, M \le 300$. Vertex $v$ has deletion cost $A_v \ge 0$ and signed weight $B_v \in \mathbb{Z}$. Delete a subset of vertices so that if $C_1, \dots, C_k$ are the remaining connected components, $\sum_{r=1}^k \left|\sum_{v \in C_r} B_v\right| - \sum_{v \text{ deleted}} A_v$ is maximized.
- **Step 1 — Non-Graph Diagnostic Signal**:
  For any connected component $C_r$, its absolute sum is $\left|\sum_{v \in C_r} B_v\right| = \max_{s_r \in \{-1, +1\}} \sum_{v \in C_r} s_r B_v$. Thus every vertex $v \in V$ chooses one of **3 ordered states**: state $+1$ (kept with positive sign), state $0$ (deleted at cost $A_v$), or state $-1$ (kept with negative sign), subject to the hard constraint that **no undirected edge $(u, v) \in E$ can connect a $+1$ vertex directly to a $-1$ vertex**!
- **Step 2 — Intermediate Algebraic Representation (2-Bit Unary Encoding & Submodularity)**:
  Encode $v$'s 3-state choice $\sigma_v \in \{-1, 0, +1\}$ using two ordered binary indicators $(x_{v,1}, x_{v,2}) \in \{0, 1\}^2$ with $x_{v,1} \ge x_{v,2}$:
  - State $+1$: $(1, 1)$ — reward $+B_v$.
  - State $0$ (Deleted): $(1, 0)$ — penalty $A_v$ (or loss $|B_v| + A_v$ relative to baseline $\sum |B_v|$).
  - State $-1$: $(0, 0)$ — reward $-B_v$.
  - Forbidden state $(0, 1)$: $x_{v,2}(1 - x_{v,1}) = 0 \implies$ edge $v_{\text{out}} \to v_{\text{in}}$ of capacity $\infty$!
  And for every edge $(u, v) \in E$, state $+1$ at $u$ ($x_{u,2} = 1$) cannot coexist with state $-1$ at $v$ ($x_{v,1} = 0$):
  $$x_{u,2} (1 - x_{v,1}) = 0 \quad \text{and} \quad x_{v,2} (1 - x_{u,1}) = 0.$$
  Every term is a pure submodular cut monomial $z_\alpha (1 - z_\beta)$, so its LP dual has an exact integer 3-state cut!
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  Start from optimistic baseline $W = \sum_{v=1}^N |B_v|$. Split each vertex $v$ into $v_{\text{in}}$ (indicator $x_{v,1}$) and $v_{\text{out}}$ (indicator $x_{v,2}$):
  1. **Deletion Edge**: $v_{\text{in}} \to v_{\text{out}}$ with capacity $A_v + |B_v|$ (severing this edge puts $x_{v,1} = 1, x_{v,2} = 0$, which is the Deleted state $0$, losing $|B_v|$ and paying $A_v$!). Also add reverse $v_{\text{out}} \to v_{\text{in}}$ of capacity $\infty$ if needed (though no paths enter $v_{\text{out}}$ without $v_{\text{in}}$).
  2. **Sign Penalty Edge**:
     - If $B_v > 0$: add $S \to v_{\text{in}}$ with capacity $2 B_v$ (choosing state $-1$, i.e. $x_{v,1} = x_{v,2} = 0$, severs $S \to v_{\text{in}}$ and loses $2 B_v$ from $+B_v$ to $-B_v$).
     - If $B_v < 0$: add $v_{\text{out}} \to T$ with capacity $2 |B_v|$ (choosing state $+1$, i.e. $x_{v,1} = x_{v,2} = 1$, severs $v_{\text{out}} \to T$ and loses $2 |B_v|$).
  3. **Graph Adjacency Prohibition ($(+1)$ cannot touch $(-1)$)**:
     For each undirected edge $\{u, v\} \in E$, add $u_{\text{out}} \to v_{\text{in}}$ (cap $\infty$) and $v_{\text{out}} \to u_{\text{in}}$ (cap $\infty$).
  Answer is $\sum_{v=1}^N |B_v| - \text{MinCut}(S, T)$.

::: {.callout-tip collapse="true"}
##### Progressive Hints (P12)
- **Hint 1**: Replace $\left|\sum_{v \in C} B_v\right|$ with $\max_{s \in \{-1, +1\}} \sum_{v \in C} s B_v$. Notice that all vertices in the same surviving component must pick the same sign $s \in \{-1, +1\}$!
- **Hint 2**: Equivalently, each vertex picks a state in $\{+1, 0 (\text{deleted}), -1\}$, and no edge $\{u, v\} \in E$ may have one endpoint in $+1$ and the other in $-1$.
- **Hint 3**: Model the 3 states as a 2-edge chain $S \to v_{\text{in}} \to v_{\text{out}} \to T$, where cutting $S \to v_{\text{in}}$ gives state $-1$, cutting $v_{\text{in}} \to v_{\text{out}}$ gives state $0$ (deleted), and cutting $v_{\text{out}} \to T$ gives state $+1$.
:::

---

#### Problem P13: `AtCoder AGC 038 F — Two Permutations` (Rescuing Supermodularity via Bipartite Variable Inversion)

- **Judge URL**: [AtCoder AGC 038 F](https://atcoder.jp/contests/agc038/tasks/agc038_f) (`[JA]` / `[EN]`)
- **Constraints**: $N \le 10^5$, two permutations $P, Q$ of $\{0, \dots, N-1\}$. You must construct two permutations $A, B$ such that for each $i$, either $A_i = i$ or $A_i = P_i$, and either $B_i = i$ or $B_i = Q_i$. Maximize the number of indices $i$ where $A_i \ne B_i$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Decompose $P$ into disjoint cycles $C_1, \dots, C_k$ and $Q$ into disjoint cycles $D_1, \dots, D_m$. Because $A$ must be a valid permutation, for each cycle $C_u$ of $P$, either **every** $i \in C_u$ sets $A_i = i$ (state $x_u = 0$) or **every** $i \in C_u$ sets $A_i = P_i$ (state $x_u = 1$). Similarly, each cycle $D_v$ of $Q$ has a single binary variable $y_v \in \{0, 1\}$.
- **Step 2 — Intermediate Algebraic Representation & Bipartite Flip**:
  Look at a single index $i$ belonging to cycle $u$ of $P$ and cycle $v$ of $Q$. We want to **minimize the number of indices where $A_i = B_i$**:
  - When $P_i \ne i$, $Q_i \ne i$, and $P_i = Q_i$: then $A_i = B_i$ happensboth when $(x_u, y_v) = (0, 0)$ ($A_i = B_i = i$) AND when $(x_u, y_v) = (1, 1)$ ($A_i = B_i = P_i$).
  Look at that penalty table $\Phi(x_u, y_v)$:
  $$\Phi(0, 0) = 1, \quad \Phi(0, 1) = 0, \quad \Phi(1, 0) = 0, \quad \Phi(1, 1) = 1 \implies A + D = 2 > 0 = B + C!$$
  The penalty is **strictly supermodular** ($A + D > B + C$)! By Theorem 39.3, it cannot be represented as a cut in $(x_u, y_v)$ directly.
  **How do we rescue it?** Every index $i$ pairs one $P$-cycle $u$ with one $Q$-cycle $v$—so the interaction graph between $P$-cycles and $Q$-cycles is **bipartite**! Apply **Bipartite Variable Inversion** to all $Q$-cycles: define $\bar{y}_v = 1 - y_v \in \{0, 1\}$ ($y_v = 0 \iff \bar{y}_v = 1$). Under $(x_u, \bar{y}_v)$, the states $(x_u, y_v) \in \{(0, 0), (1, 1)\}$ become $(x_u, \bar{y}_v) \in \{(0, 1), (1, 0)\}$—which satisfies $A' + D' = 0 \le 2 = B' + C'$ (**submodular**)!
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  With $x_u = 1 \iff u \in S$ (meaning $A_i = P_i$) and $\bar{y}_v = 1 \iff v \in S$ (meaning $B_i = i$!):
  For each index $i \in \{0, \dots, N-1\}$ in $P$-cycle $u$ and $Q$-cycle $v$, check the 5 cases of $(P_i \stackrel{?}{=} i, Q_i \stackrel{?}{=} i, P_i \stackrel{?}{=} Q_i)$:
  1. $P_i = i$ and $Q_i = i$: $A_i = B_i = i$ always; add $+1$ to unavoidable collisions.
  2. $P_i = i$ and $Q_i \ne i$: $A_i = B_i \iff B_i = i \iff \bar{y}_v = 1 \implies$ edge $v \to T$ of capacity $1$.
  3. $P_i \ne i$ and $Q_i = i$: $A_i = B_i \iff A_i = i \iff x_u = 0 \implies$ edge $S \to u$ of capacity $1$.
  4. $P_i \ne i, Q_i \ne i, P_i \ne Q_i$: $A_i = B_i \iff (x_u = 0 \land \bar{y}_v = 1) \implies$ directed edge $v \to u$ of capacity $1$.
  5. $P_i \ne i, Q_i \ne i, P_i = Q_i$: $A_i = B_i \iff (x_u \ne \bar{y}_v) \implies$ bidirectional edges $u \to v$ (cap $1$) and $v \to u$ (cap $1$).
  Since this is a unit-capacity network with $V, E \le 2 \times 10^5$, Dinic runs in $O(E \sqrt{V})$!

::: {.callout-tip collapse="true"}
##### Progressive Hints (P13)
- **Hint 1**: Why must all elements in the same cycle of $P$ make the exact same choice ($A_i = i$ vs. $A_i = P_i$)? Because $A$ must be a bijection (permutation)!
- **Hint 2**: Write the collision penalty $\Phi(x_u, y_v)$ for an index $i$ in $P$-cycle $u$ and $Q$-cycle $v$. Why does $P_i = Q_i \ne i$ give a supermodular table $\Phi(0,0) = \Phi(1,1) = 1$?
- **Hint 3**: Notice that every interaction is between a $P$-cycle and a $Q$-cycle (a bipartite graph!). Flip $\bar{y}_v = 1 - y_v$ on the $Q$-cycles so that $(x_u = 1 \iff A_i = P_i)$ and $(\bar{y}_v = 1 \iff B_i = i)$.
:::

---

#### Problem P14: `Codeforces 1556H — DIY Tree` (Weighted Graphic + Partition Matroid Intersection)

- **Judge URL**: [Codeforces 1556H](https://codeforces.com/problemset/problem/1556/H) (`[EN]`)
- **Constraints**: Complete undirected graph $K_n$ on $n \le 50$ vertices with edge weights $w_{uv} \le 100$. The first $k \le 5$ vertices have degree upper bounds $d_1, \dots, d_k$ in the spanning tree. Find the minimum weight of a spanning tree satisfying $\deg_T(i) \le d_i$ for all $1 \le i \le k$.
- **Step 1 — Non-Graph Diagnostic Signal (Boundary Line 2 of Iteration 40)**:
  General degree-bounded MST is NP-hard (since $d_v = 2$ for all $v$ is Hamiltonian Path!). Why is this problem solvable in polynomial time? Because **only $k \le 5$ vertices have degree bounds**!
  If there were *no* edges among $\{1, \dots, k\}$, then $\{1, \dots, k\}$ would be an **independent set**, so every remaining edge has **at most one endpoint in $\{1, \dots, k\}$**! Then:
  - $M_1 = \text{Graphic Matroid}$ (no cycles in $G$),
  - $M_2 = \text{Partition Matroid}$ (for each $i \in \{1, \dots, k\}$, at most $d_i$ edges incident to $i$).
  What about the $\binom{k}{2} \le \binom{5}{2} = 10$ edges **inside** $\{1, \dots, k\}$? Since $2^{10} = 1024$ is tiny, we simply **enumerate all $2^{\binom{k}{2}} \le 1024$ forest subsets $F_0$ of edges among $\{1, \dots, k\}$** (in fact, there are only $k^{k-2} \approx 200$ valid forests on $5$ vertices!), contract $F_0$, subtract their degrees from $d_1, \dots, d_k$, and solve **Weighted Matroid Intersection** on the remaining edges!
- **Step 2 — Intermediate Algebraic Representation**:
  Fix a forest $F_0$ on $\{1, \dots, k\}$ satisfying $\deg_{F_0}(i) \le d_i$. Let $E'$ be the edges with at least one endpoint in $\{k+1, \dots, n\}$ (keeping only the $n-1$ lightest edges inside $\{k+1, \dots, n\}$ that form a MST of $\{k+1, \dots, n\}$, so $|E'| \le k(n-k) + (n-1) \le 300$).
  Define on $E'$:
  - $M_1$: Contracted Graphic Matroid ($I \in \mathcal{I}_1 \iff I \cup F_0$ is acyclic).
  - $M_2$: Partition Matroid ($I \in \mathcal{I}_2 \iff |I \cap \delta(i)| \le d_i - \deg_{F_0}(i)$ for all $i \in \{1, \dots, k\}$).
- **Step 3 — Reverse-Engineering Scratchpad (Matroid Intersection Exchange Graph)**:
  Start with $I = \emptyset$ and augment $n - 1 - |F_0|$ times using **Edmonds' Weighted Matroid Intersection**:
  1. Build the Exchange Graph $G(I)$ on $E'$:
     - Source set $X_1 = \{y \in E' \setminus I : I \cup F_0 \cup \{y\} \text{ is acyclic}\}$.
     - Sink set $X_2 = \{y \in E' \setminus I : \text{adding } y \text{ respects } d_i - \deg_{F_0}(i)\}$.
     - For $x \in I, y \in E' \setminus I$: add $x \to y$ if $x$ lies on the fundamental cycle of $y$ in $I \cup F_0$; add $y \to x$ if $x$ and $y$ share the same saturated endpoint $i \in \{1, \dots, k\}$.
  2. Assign vertex weights $\tilde{w}(y) = +w_y$ for $y \notin I$ and $\tilde{w}(x) = -w_x$ for $x \in I$. Find the shortest path from $X_1$ to $X_2$ minimizing $(\text{total weight}, \text{number of edges})$ via SPFA/Bellman–Ford, and flip $I \gets I \oplus V(P)$!

::: {.callout-tip collapse="true"}
##### Progressive Hints (P14)
- **Hint 1**: Why does degree-constrained MST fail to be a Partition Matroid if an edge $e = (u, v)$ has *both* $u, v \in \{1, \dots, k\}$? Because $e$ would belong to two blocks $\delta(u)$ and $\delta(v)$ of the same matroid!
- **Hint 2**: How many edges have both endpoints in $\{1, \dots, k\}$ when $k \le 5$? At most $\binom{5}{2} = 10$! Brute-force which of those $10$ edges are in the tree (at most $292$ acyclic subsets on $5$ vertices).
- **Hint 3**: Before running Matroid Intersection, pre-filter the edges completely inside $\{k+1, \dots, n\}$ to only the $n - k - 1$ edges of the MST of $\{k+1, \dots, n\}$; this shrinks the ground set $|E'|$ from $1225$ to $\le 270$!
:::

---

#### Problem P15: `Codeforces 1284G — Seollal` (Graphic + Degree-2 Partition Matroid Intersection for Maze Generation)

- **Judge URL**: [Codeforces 1284G](https://codeforces.com/problemset/problem/1284/G) (`[EN]`)
- **Constraints**: An $n \times m$ grid ($n, m \le 20$) of open cells `'O'` and blocked cells `'X'`, with $(1, 1)$ open. Build a spanning tree of all open cells (by keeping a subset of grid adjacencies) such that in the resulting maze, **every $2 \times 2$ subgrid contains at least one cell that is NOT a leaf (degree $\ge 2$) or is blocked**; equivalently, no cell at $(i, j)$ with $i + j$ even (except $(1, 1)$) is a leaf!
- **Step 1 — Non-Graph Diagnostic Signal**:
  In the problem's exact characterization, every open cell $v \ne (1, 1)$ at an even chessboard parity $(r + c \equiv 0 \pmod 2)$ must have degree **at least $2$** in the spanning tree $T$!
  How do we turn a **lower bound** $\deg_T(v) \ge 2$ on a spanning tree into a **matroid upper bound** $\le d'_v$?
  **Complement the edge set**! Let $E$ be all grid edges between open cells. Instead of choosing tree edges $T \subseteq E$, choose the **deleted non-tree edges** $I = E \setminus T$! Or equivalently, in the primal Graphic Matroid $M_1$, require $|T \cap \delta(v)| \ge 2$ for every even cell $v \ne (1, 1)$ by finding a forest $I_0 \subseteq E$ of size $2 \times |\text{EvenCells}|$ where every even cell $v \ne (1, 1)$ has degree **at most $2$** (and hence **exactly $2$** when $|I_0| = 2 |\text{EvenCells}|$)!
- **Step 2 — Intermediate Algebraic Representation**:
  Because the even cells $\{v : r + c \equiv 0 \pmod 2, \; v \ne (1, 1)\}$ form an **independent set** in the grid graph, every grid edge $e \in E$ is incident to **at most one** constrained even cell $v$!
  Define two matroids on $E$:
  1. **$M_1$ (Graphic Matroid)**: $I \in \mathcal{I}_1 \iff I$ is a forest (acyclic).
  2. **$M_2$ (Partition Matroid on Even Cells)**: Partition $E$ by which even cell $v \ne (1, 1)$ each edge touches; $I \in \mathcal{I}_2 \iff |I \cap \delta(v)| \le 2$ for every even cell $v \ne (1, 1)$ (and edges touching $(1, 1)$ have no bound, or belong to a dummy block).
- **Step 3 — Reverse-Engineering Scratchpad (Compilation & Tree Completion)**:
  1. Run unweighted **Edmonds' Matroid Intersection** on $M_1 \cap M_2$ to find a maximum common independent set $I^* \in \mathcal{I}_1 \cap \mathcal{I}_2$ (restricting to edges incident to constrained even cells).
  2. Check if $|I^*| = 2 \times |\text{ConstrainedEvenCells}|$.
     - If $|I^*| < 2 \times |\text{ConstrainedEvenCells}|$ (or if the open cells are not connected), output `NO`.
     - If $|I^*| = 2 \times |\text{ConstrainedEvenCells}|$, then $I^*$ is a forest in which every constrained even cell already has degree $2$! Simply extend $I^*$ to a full spanning tree $T \supseteq I^*$ of all open cells using Kruskal's/DSU (since adding more edges can only *increase* degrees $\ge 2$)!

::: {.callout-tip collapse="true"}
##### Progressive Hints (P15)
- **Hint 1**: Notice that the constrained cells ($r + c$ even, $(r, c) \ne (1, 1)$) form a chessboard independent set—no grid edge connects two constrained cells!
- **Hint 2**: We need a spanning tree $T$ where every constrained cell $v$ has $\deg_T(v) \ge 2$. Since adding edges to a forest only increases vertex degrees, it suffices to find a **forest** $I \subseteq E$ in which every constrained cell has degree **exactly $2$**!
- **Hint 3**: Enforce $\deg_I(v) \le 2$ (Partition Matroid $M_2$) and $I$ acyclic (Graphic Matroid $M_1$), and test whether the maximum common independent set has size $2 \times |\text{ConstrainedEvenCells}|$.
:::

---

### Tier 4: Mastery Problems (P16–P20)

---

#### Problem P16: `Codeforces 1427G — One Billion Shades of Grey` (Lovász Extension Coarea Level-Set Cuts & Parametric Flow Rollback)

- **Judge URL**: [Codeforces 1427G](https://codeforces.com/problemset/problem/1427/G) (`[EN]`)
- **Constraints**: An $n \times n$ grid ($n \le 200$). Blocked cells have $a_{ij} = -1$; boundary cells have fixed heights $b_{ij} \in [1, 10^9]$; interior open cells have $a_{ij} = 0$ and must be assigned heights $h_{ij} \in \mathbb{Z}$. Minimize the total $\ell_1$ variation $\sum_{(u,v) \in E_{\text{grid}}} |h_u - h_v|$ over all adjacent non-blocked cell pairs.
- **Step 1 — Non-Graph Diagnostic Signal (Iteration 39.4 — Lovász Extension of Graph Cut)**:
  By Theorem 39.6, the objective $\hat{f}(h) = \sum_{(u,v) \in E} |h_u - h_v|$ is the **Lovász extension** of the undirected graph cut function $f(S) = |\delta(S)|$!
- **Step 2 — Intermediate Algebraic Representation (Coarea Formula)**:
  Sort the distinct fixed boundary values as $v_1 < v_2 < \dots < v_k$ ($k \le 4n \le 800$). By the discrete Coarea Formula (Definition 39.5), for any height assignment $h \in [v_1, v_k]^V$:
  $$\sum_{(u,v) \in E} |h_u - h_v| = \sum_{r=1}^{k-1} (v_{r+1} - v_r) \sum_{(u,v) \in E} \Big| [h_u > v_r] - [h_v > v_r] \Big|.$$
  Because $f(S) = |\delta(S)|$ is **submodular**, minimizing each level cut $C_r = \min_{S_r} |\delta(S_r)|$ (where boundary cells with $b_u > v_r$ are locked to $S$ and boundary cells with $b_u \le v_r$ are locked to $T$) produces a **nested chain of minimum cuts** $S_1 \supseteq S_2 \supseteq \dots \supseteq S_{k-1}$, which defines an optimal integer height $h^*_u = v_{\max \{r : u \in S_{r-1}\}}$!
- **Step 3 — Reverse-Engineering Scratchpad (Incremental Parametric Rollback)**:
  Instead of running Max-Flow $k \le 800$ times from scratch, observe what changes between threshold $v_{r-1}$ and $v_r$: only the boundary cells $u$ with $b_u = v_r$ switch from $u \in S$ ($S \to u$ of capacity $\infty$) to $u \in T$ ($u \to T$ of capacity $\infty$)!
  1. Initially at $r = 1$, connect all boundary cells with $b_u > v_1$ from $S \to u$ (cap $\infty$) and those with $b_u = v_1$ to $u \to T$ (cap $\infty$). Run Dinic/FF to get initial max flow $F_1$.
  2. When advancing from $r-1$ to $r$, for each boundary cell $u$ with $b_u = v_r$ that currently has $f(S, u) > 0$ units of flow on $S \to u$:
     - **Roll back** those $f(S, u) \le 4$ units of flow by finding paths from $u$ back to $S$ (or from $T$ to $u$) in the residual graph $G_f$, decrementing $F$ by $1$ per unit rolled back.
     - Delete edge $S \to u$, add edge $u \to T$ of capacity $\infty$, and run augmenting paths $S \to T$ in $G_f$ to restore maximum flow $F_r$.
  3. Since each boundary vertex has degree $\le 4$, across all $k$ steps at most $4 \times (4n) \le 3200$ units of flow are ever rolled back or re-augmented! Each augmenting path search takes $O(n^2)$, giving $O(n^3)$ total time!

::: {.callout-tip collapse="true"}
##### Progressive Hints (P16)
- **Hint 1**: Rewrite $|h_u - h_v| = \sum_{r=1}^{k-1} (v_{r+1} - v_r) |[h_u > v_r] - [h_v > v_r]|$ where $v_1 < \dots < v_k$ are the sorted boundary values.
- **Hint 2**: Why can you minimize the cut $|[h_u > v_r] - [h_v > v_r]|$ independently for each $r$ without violating $h_u$'s monotonicity $[h_u > v_1] \ge [h_u > v_2] \ge \dots$? Because cut capacity is submodular, so minimal cuts nest automatically!
- **Hint 3**: Each boundary vertex has at most $4$ grid neighbors, so its edge $S \to u$ carries at most $4$ units of flow. Roll back those $\le 4$ units via DFS on $G_f$ before flipping $u$ from $S$ to $T$.
:::

---

#### Problem P17: `[省选联考 2020 A 卷] 魔法商店` (Inverse Linear Matroid Basis via Exchange-Graph Poset & LP Dual Cut)

- **Judge URL**: [Luogu P6621](https://www.luogu.com.cn/problem/P6621) / [LOJ 3300](https://loj.ac/p/3300) (`[ZH]`)
- **Constraints**: $n \le 1000$ magic items with 64-bit integer XOR attributes $c_i \in [1, 2^{64})$ and initial prices $v_i \le 10^6$. A subset of $m \le 64$ items works iff their attributes $c_i$ are XOR-linearly independent (forming a basis of the Linear Matroid $M = (E, \mathcal{I})$). You are given two specific bases $A, B \subseteq \{1, \dots, n\}$ ($|A| = |B| = m$). Modify item prices $v_i \mapsto f_i \in \mathbb{R}$ at squared cost $\sum_{i=1}^n (f_i - v_i)^2$ so that $A$ becomes a **Minimum-Weight Basis** and $B$ becomes a **Maximum-Weight Basis** simultaneously!
- **Step 1 — Non-Graph Diagnostic Signal (Unifying Matroids, Inverse MST, and Isotonic Regression)**:
  By the **Matroid Basis Optimality Theorem** (generalizing the MST cycle condition of Problem P06!), a basis $A$ is a minimum-weight basis under prices $f$ if and only if for every $y \notin A$ and every $x \in A$ in the unique XOR basis representation of $c_y = \bigoplus_{x \in C_A(y)} c_x$, we have:
  $$f_x \le f_y \quad \forall y \notin A, \; \forall x \in C_A(y)!$$
  Symmetrically, $B$ is a maximum-weight basis under $f$ if and only if for every $y \notin B$ and every $x \in C_B(y)$ in the XOR representation of $c_y$ over $B$, we have:
  $$f_y \le f_x \quad \forall y \notin B, \; \forall x \in C_B(y)!$$
- **Step 2 — Intermediate Algebraic Representation ($L_2$ Isotonic Regression on the Exchange DAG)**:
  Look at those two families of inequalities: both have the exact form $f_u \le f_w$ on a directed comparison graph $G_{\text{poset}} = (V, E_{\text{ord}})$ with $|V| = n \le 1000$ and $|E_{\text{ord}}| \le 2 m n \le 1.28 \times 10^5$ edges!
  We want to solve the **$L_2$ Isotonic Regression Problem**:
  $$\text{Minimize } \sum_{i=1}^n (f_i - v_i)^2 \quad \text{subject to} \quad f_u \le f_w \quad \forall (u, w) \in E_{\text{ord}}.$$
  Because $(f_i - v_i)^2$ is strictly convex with derivative $2(f_i - v_i)$, its level-set / subgradient condition reduces via **Parallel Binary Search (`整体二分`)** to testing at midpoint $M$ whether each vertex $i$ prefers $f_i \le M$ or $f_i \ge M + 1$!
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation inside Parallel Binary Search)**:
  1. Insert $A$ into an XOR Linear Basis to find $C_A(y)$ for each $y \notin A$, adding order edges $x \to y$ for $x \in C_A(y)$.
  2. Insert $B$ into an XOR Linear Basis to find $C_B(y)$ for each $y \notin B$, adding order edges $y \to x$ for $x \in C_B(y)$.
  3. Run `solve(V_sub, L, R)`: at midpoint $M = \lfloor (L + R)/2 \rfloor$, compare choosing $f_i = M$ vs. $f_i = M + 1$:
     - Let $z_i \in \{0, 1\}$ indicate $[f_i \ge M + 1]$.
     - Marginal cost of setting $z_i = 1$ ($f_i = M+1$ instead of $M$) is $\Delta_i = (M + 1 - v_i)^2 - (M - v_i)^2 = 2(M - v_i) + 1$.
     - Order constraint $f_u \le f_w \implies z_u \le z_w \implies u \to w$ of capacity $\infty$!
     - Run Dinic on the active subset $V_{\text{sub}}$; vertices with $z_i = 0$ recurse on $[L, M]$ and vertices with $z_i = 1$ recurse on $[M+1, R]$!

::: {.callout-tip collapse="true"}
##### Progressive Hints (P17)
- **Hint 1**: How do you generalize the MST cycle optimality condition ($w(e_{\text{in}}) \le w(e_{\text{out}})$) from a Graphic Matroid to an XOR Linear Basis Matroid? Express each non-basis vector $c_y$ as a unique XOR combination of basis vectors!
- **Hint 2**: Why do both "A is a Min-Basis" and "B is a Max-Basis" compile into simple pairwise inequalities $f_u \le f_w$?
- **Hint 3**: Once you have $\min \sum (f_i - v_i)^2$ subject to $f_u \le f_w$, use Parallel Binary Search (`整体二分`) with Project Selection Min-Cut at each midpoint $M$!
:::

---

#### Problem P18: `[省选联考 2020 A 卷] 保序回归` (General $L_p$ Isotonic Regression via Submodular Level Cuts & Matroid Dual Reduction)

- **Judge URL**: [Luogu P6624](https://www.luogu.com.cn/problem/P6624) / [LOJ 3303](https://loj.ac/p/3303) (`[ZH]`)
- **Constraints**: Given arrays $y_1, \dots, y_n$ and weights $w_1, \dots, w_n$, a parameter $p \in \{1, 2, \dots\}$, and a partial order (obtained in the problem statement from a sequence of matroid / exchange conditions on subsets of size $k$ with $n \le 64$ or general DAG poset), find integer $f_1, \dots, f_n$ satisfying $u \preceq v \implies f_u \le f_v$ that minimizes $\sum_{i=1}^n w_i |f_i - y_i|^p$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  For any convex function $\phi_i(f_i) = w_i |f_i - y_i|^p$, we can write $\phi_i(f_i)$ over integer $f_i \in [L, R]$ via unary threshold variables $z_{i, \lambda} = [f_i > \lambda] \in \{0, 1\}$:
  $$\phi_i(f_i) = \phi_i(L) + \sum_{\lambda = L}^{R - 1} \Big( \phi_i(\lambda + 1) - \phi_i(\lambda) \Big) z_{i, \lambda}.$$
  And the partial order constraint $f_u \le f_v$ is equivalent to $z_{u, \lambda} \le z_{v, \lambda}$ for **every** threshold $\lambda$!
- **Step 2 — Intermediate Algebraic Representation (Why Level Cuts Nest by Convexity)**:
  For a fixed threshold $\lambda$, minimizing the $\lambda$-slice:
  $$\Phi_\lambda(z_{\cdot, \lambda}) = \sum_{i=1}^n \underbrace{w_i \big(|\lambda + 1 - y_i|^p - |\lambda - y_i|^p\big)}_{\Delta_{i, \lambda}} z_{i, \lambda} \quad \text{subject to} \quad z_{u, \lambda} (1 - z_{v, \lambda}) = 0 \; \forall u \preceq v$$
  is a pure **Maximum Weight Closure / Project Selection Min-Cut**!
  Even better: because $\phi_i$ is **convex**, the marginal cost $\Delta_{i, \lambda} = \phi_i(\lambda + 1) - \phi_i(\lambda)$ is **monotone non-decreasing in $\lambda$**! By submodular cut nesting (Iteration 39.4), if the minimal cut at threshold $\lambda$ sets $z^*_{i, \lambda} = 0$ ($f^*_i \le \lambda$), then for all $\lambda' > \lambda$ we also have $z^*_{i, \lambda'} = 0$, and if $z^*_{i, \lambda} = 1$ ($f^*_i \ge \lambda + 1$), then for all $\lambda' < \lambda$ we have $z^*_{i, \lambda'} = 1$!
- **Step 3 — Reverse-Engineering Scratchpad (Parallel Binary Search Compilation)**:
  1. Construct the poset DAG $G = (V, E_{\text{poset}})$ from the matroid exchange conditions.
  2. Define recursive `solve(U, L, R)` where $U \subseteq V$ is the set of vertices whose optimal value $f^*_i$ is proven to lie in $[L, R]$:
     - Base case: if $L = R$ or $U = \emptyset$, set $f^*_i = L$ for all $i \in U$ and return.
     - Let $M = \lfloor (L + R) / 2 \rfloor$. Build a flow network on $U$:
       - For each $i \in U$, compute $\Delta_i = w_i (|M + 1 - y_i|^p - |M - y_i|^p)$.
       - If $\Delta_i < 0$ (reward $-\Delta_i > 0$ for choosing $z_i = 1$): add edge $S \to i$ of capacity $-\Delta_i$.
       - If $\Delta_i > 0$ (cost $\Delta_i > 0$ for choosing $z_i = 1$): add edge $i \to T$ of capacity $+\Delta_i$.
       - For each $(u, v) \in E_{\text{poset}}$ with **both** $u, v \in U$: add edge $u \to v$ of capacity $\infty$ (since $z_u = 1 \implies z_v = 1$). *(Why can we ignore edges where one endpoint is outside $U$? Because any ancestor $a \notin U$ with $f^*_a \le L \le M$ already has $z_a = 0$, and any descendant $d \notin U$ with $f^*_d \ge R \ge M+1$ already has $z_d = 1$, neither of which constrains $U$!)*
     - Run Dinic, partition $U = U_0 \sqcup U_1$ ($U_1 = \text{reachable from } S \text{ in } G_f$), and recurse `solve(U_0, L, M)` and `solve(U_1, M+1, R)`.

::: {.callout-tip collapse="true"}
##### Progressive Hints (P18)
- **Hint 1**: Express $\sum w_i |f_i - y_i|^p$ as a sum over threshold cuts $z_{i, \lambda} = [f_i > \lambda]$. Why does $f_u \le f_v$ decouple into $z_{u, \lambda} \le z_{v, \lambda}$ at each threshold $\lambda$?
- **Hint 2**: Because $|f_i - y_i|^p$ is convex, the marginal derivative $\Delta_{i, \lambda}$ is increasing in $\lambda$, which guarantees that the optimal threshold cuts $S(\lambda)$ are nested ($S(\lambda + 1) \subseteq S(\lambda)$)!
- **Hint 3**: Use Parallel Binary Search (`整体二分`) over $[y_{\min}, y_{\max}]$ so the total size of all Dinic networks at each recursion depth sums to $O(N + M)$, giving $O(\text{Dinic}(N, M) \log(\max y))$ total time!
:::

---

#### Problem P19: `AtCoder ARC 142 E — Pairing Wizards` (Disjunctive OR-Thresholds via Unary Chains & Bipartite Inversion)

- **Judge URL**: [AtCoder ARC 142 E](https://atcoder.jp/contests/arc142/tasks/arc142_e) (`[JA]` / `[EN]`)
- **Constraints**: $N \le 100$ wizards, each with initial strength $a_i \le 100$ and target threshold $b_i \le 100$. You can increase any wizard's strength $a_i \mapsto x_i \ge a_i$ at cost $x_i - a_i$. For each of $M$ given pairs $(u, v)$, their final strengths must satisfy:
  $$\min(x_u, x_v) \ge \min(b_u, b_v) \quad \text{AND} \quad \max(x_u, x_v) \ge \max(b_u, b_v).$$
  Find the minimum total cost $\sum_{i=1}^N (x_i - a_i)$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  First, look at the $\min$ constraint: $\min(x_u, x_v) \ge \min(b_u, b_v) \iff x_u \ge \min(b_u, b_v) \text{ AND } x_v \ge \min(b_u, b_v)$. That is a purely **unary lower bound** on $x_u$ and $x_v$! So we can immediately raise $a_u \gets \max(a_u, \min(b_u, b_v))$ and $a_v \gets \max(a_v, \min(b_u, b_v))$ for all pairs $(u, v) \in E$ as a mandatory baseline cost!
  Now, what remains? After raising everyone to their mandatory baseline $L_i$, every remaining pair constraint is:
  $$\max(x_u, x_v) \ge M_{uv} := \max(b_u, b_v) \quad \Longleftrightarrow \quad (x_u \ge M_{uv}) \;\text{ OR }\; (x_v \ge M_{uv})!$$
  Crucial observation: If for a pair $(u, v)$, BOTH $b_u$ and $b_v$ were $\le \min(b_u, b_v)$, the condition is already met. Otherwise, assume without loss of generality $b_u < b_v = M_{uv}$. Then $L_v \ge \max_{w \in N(v)} \min(b_v, b_w) \ge b_u$... wait: EVEN BETTER! For any edge $(u, v)$ with $b_u < b_v$, we already raised $L_u \ge b_u$ AND $L_v \ge b_u$!
  Can a vertex $u$ ever need to be raised above $b_u$ to help some neighbor $v$ (so $x_u \ge b_v > b_u$), while Simultaneously some OTHER neighbor $w$ needs $u$ to satisfy $\max(x_u, x_w) \ge b_u$?
  **NO!** Because $L_u$ is ALREADY $\ge b_u$! Every vertex $u$ already satisfies $x_u \ge L_u \ge b_u$ at baseline!
  Therefore, every wizard $u$ naturally splits into **two disjoint roles**:
  - **Role 1 (Needs help at level $b_u$)**: Either $u$ itself reaches $x_u \ge b_u$ (only relevant if $L_u < b_u$), OR **every** neighbor $v \in N(u)$ with $b_v < b_u$ must reach $x_v \ge b_u$!
  - **Role 2 (Helps neighbors above $L_u$)**: Wizard $u$ can choose to raise $x_u \in [L_u, 100]$ to satisfy $x_u \ge b_w$ for neighbors $w$ that have $L_w < b_w$!
  Notice that if $L_w < b_w$, then for ALL neighbors $u \in N(w)$ we must have $\min(b_w, b_u) \le L_w < b_w \implies b_u \le L_w < b_w \implies L_u \ge \min(b_w, b_u) = b_u$!
  **Every edge with an active OR-constraint goes strictly between the set of vertices $W = \{w : L_w < b_w\}$ and the disjoint set $U = \{u : L_u \ge b_u\}$—the active interaction graph is BIPARTITE!**
- **Step 2 — Intermediate Algebraic Representation**:
  - For each $w \in W$ ($L_w < b_w$): $w$ only ever needs to choose between $x_w = L_w$ (binary state $y_w = 0$, cost $0$) and $x_w = b_w$ (binary state $y_w = 1$, cost $b_w - L_w$).
  - For each $u \in U$ ($L_u \ge b_u$): represent $x_u \in [L_u, 100]$ by unary threshold indicators $z_{u, t} = [x_u \ge t] \in \{0, 1\}$ for $t \in [L_u + 1, 100]$, each costing $1$, with $z_{u, L_u+1} \ge z_{u, L_u+2} \ge \dots \ge z_{u, 100}$.
  - For each edge $(w, u)$ with $w \in W$ and $u \in U$: we require $y_w = 1 \text{ OR } z_{u, b_w} = 1$, which is $(1 - y_w)(1 - z_{u, b_w}) = 0$.
  Flip $\bar{y}_w = 1 - y_w \in \{0, 1\}$ ($w \in S \iff \bar{y}_w = 1 \iff x_w = L_w$, and $u_t \in S \iff z_{u, t} = 1$): then $(1 - y_w)(1 - z_{u, b_w}) = \bar{y}_w (1 - z_{u, b_w}) = 0$!
- **Step 3 — Reverse-Engineering Scratchpad (Graph Compilation)**:
  1. Pre-raise $L_i = a_i$; for each edge $(u, v)$, update $L_u \gets \max(L_u, \min(b_u, b_v))$ and $L_v \gets \max(L_v, \min(b_u, b_v))$. Add $\sum_{i=1}^N (L_i - a_i)$ to baseline cost.
  2. For each $w \in W$ ($L_w < b_w$): add edge $S \to w$ with capacity $b_w - L_w$ (cutting $S \to w$ sets $\bar{y}_w = 0 \implies y_w = 1 \implies x_w = b_w$ at cost $b_w - L_w$).
  3. For each $u \in U$ ($L_u \ge b_u$) and each threshold $t \in [L_u + 1, 100]$:
     - Create node $(u, t)$ with edge $(u, t) \to T$ of capacity $1$ (keeping $(u, t) \in S$ means $z_{u, t} = 1$, cutting $(u, t) \to T$ at cost $1$).
     - Add chain monotonicity edge $(u, t) \to (u, t-1)$ of capacity $\infty$ for $t > L_u + 1$.
  4. For each edge $(w, u)$ with $w \in W$: add directed edge $w \to (u, b_w)$ of capacity $\infty$ (enforcing $\bar{y}_w = 1 \implies z_{u, b_w} = 1$).
  Total answer is $\sum_{i=1}^N (L_i - a_i) + \text{MinCut}(S, T)$.

::: {.callout-tip collapse="true"}
##### Progressive Hints (P19)
- **Hint 1**: First enforce $\min(x_u, x_v) \ge \min(b_u, b_v)$ greedily by setting $L_i = \max(\{a_i\} \cup \{\min(b_i, b_j) : j \in N(i)\})$. Why is this greedy step 100% mandatory?
- **Hint 2**: After raising everyone to $L_i$, Partition vertices into $W = \{w : L_w < b_w\}$ and $U = \{u : L_u \ge b_u\}$. Prove that no edge can connect two vertices in $W$!
- **Hint 3**: Because every remaining constraint $\max(x_w, x_u) \ge b_w$ connects $w \in W$ to $u \in U$, the active graph is bipartite! Use unary threshold chains on $U$ and invert the variable on $W$.
:::

---

#### Problem P20: `UOJ 455 — [WC2019] 雪灾与外卖` (1D Line Transportation LP Dual & Polymatroid Regret Simulation)

- **Judge URL**: [UOJ 455](https://uoj.ac/problem/455) / [Luogu P5470 / P6122 Archetype](https://www.luogu.com.cn/problem/P6122) (`[ZH]`)
- **Constraints**: $N \le 10^5$ delivery workers at coordinates $x_1 \le \dots \le x_N$ on a 1D line, and $M \le 10^5$ restaurants at coordinates $y_1 \le \dots \le y_M$, where restaurant $j$ has capacity $c_j$ and per-order cost $w_j$. Assign each worker $i$ to a restaurant $j$ to minimize $\sum_i (|x_i - y_{j(i)}| + w_{j(i)})$.
- **Step 1 — Non-Graph Diagnostic Signal (Direction B of `PLAN.md`: Flow $\to$ Non-Flow Fast Algorithm via Dual Potentials)**:
  At heart, this is a **Min-Cost Flow on a 1D Line** (or equivalently, its LP Dual $\pi_v - \pi_u \le |x_u - x_v|$ on a line, which is a Column/Row Consecutive-Ones TU system!). Because $N, M \le 10^5$, running SSP takes $O(N^2)$ and TLEs; instead, by Complementary Slackness (Iteration 37) and 1D Monge / Submodular Uncrossing, augmenting paths on a 1D line never cross in the same direction, allowing **Two-Heap Regret Greedy (`双堆反悔贪心 / 模拟费用流`)** in $O((N + M) \log(N + M))$!
- **Step 2 — Intermediate Algebraic Representation (Residual Cost Transformation)**:
  Sweep from left to right along sorted coordinates:
  - When a worker $i$ at $x_i$ matches with a previous restaurant $j$ ($y_j \le x_i$) of cost $(x_i - y_j) + w_j = x_i + (w_j - y_j)$, this creates a **reverse residual edge** allowing a future restaurant $j'$ ($y_{j'} \ge x_i$) to steal worker $i$ at marginal cost:
    $$\Delta_{\text{steal worker } i} = (y_{j'} - x_i + w_{j'}) - (x_i - y_j + w_j) = (y_{j'} + w_{j'}) + \big(-2 x_i + y_j - w_j\big).$$
  - Symmetrically, when a restaurant $j$ at $y_j$ steals a worker $i$ ($x_i \le y_j$), this creates a **reverse residual edge** allowing a future worker $i'$ ($x_{i'} \ge y_j$) to reclaim that restaurant slot at marginal cost:
    $$\Delta_{\text{reclaim slot at } j} = (x_{i'} - y_j) - (y_j - x_i) = x_{i'} + (-2 y_j + x_i).$$
- **Step 3 — Reverse-Engineering Scratchpad (Two-Heap Complementary Slackness Simulation)**:
  Maintain two min-heaps storing available residual transitions:
  - `Heap_Rest`: stores available restaurant slots (both fresh slots at $y_j$ with key $w_j - y_j$ and multiplicity $c_j$, and regret-reclaimable worker slots with key $-2 y_j + \dots$).
  - `Heap_Work`: stores workers $i$ (with multiplicity) that can be improved by a future restaurant at $y_{j'}$, keyed by $-2 x_i - \text{current\_cost}(i)$.
  Process events in increasing order of coordinate, matching workers immediately to the minimum key in `Heap_Rest`, and when a restaurant $j$ arrives, repeatedly augment with `Heap_Work` while $(y_j + w_j) + \text{Heap\_Work.top()} < 0$, pushing the corresponding reverse residual edges into the opposite heap!

::: {.callout-tip collapse="true"}
##### Progressive Hints (P20)
- **Hint 1**: Why is 1D Line Transportation a Totally Unimodular Min-Cost Flow problem? Because every edge along the line connects adjacent coordinates $k \leftrightarrow k+1$!
- **Hint 2**: Write down the exact cost of a residual augmenting path when sweeping left-to-right: if worker $i$ currently pays $C_i$, switching worker $i$ to restaurant $j$ at $y_j \ge x_i$ changes the total cost by $(y_j - x_i + w_j) - C_i = (y_j + w_j) - (x_i + C_i)$.
- **Hint 3**: Group identical-key residual edges with a multiplicity count `(key, count)` in the two priority queues so that a restaurant with capacity $c_j \le 10^9$ only performs amortized $O(1)$ heap pushes per split!
:::

---

## Quarantined Template Problems Table (`R-01` to `R-08`)

Per `AGENTS.md` and `flows_research/PLAN.md`, bare algorithm-verification or template problems are strictly excluded from the main 4-Tier Problem Bank and quarantined below for reference only:

| Quarantine ID | Problem Title & Judge Source | Reason for Quarantine |
| :--- | :--- | :--- |
| **`R-01`** | **Luogu P3381 — `【模板】最小费用最大流`** | Pure SSP / Primal–Dual MCMF template verification with zero modelling required. |
| **`R-02`** | **Library Checker — `Min Cost b-Flow`** (`https://judge.yosupo.jp/problem/min_cost_b_flow`) | Direct verification of Min-Cost Circulation and dual potential $\pi_v$ output. |
| **`R-03`** | **UOJ #179 — `线性规划`** (`https://uoj.ac/problem/179`) | Pure Simplex Method template verification without network/TU compilation. |
| **`R-04`** | **Library Checker — `Matroid Intersection`** | Bare unweighted matroid intersection oracle template. |
| **`R-05`** | **Library Checker — `Weighted Matroid Intersection`** | Bare weighted matroid intersection oracle template. |
| **`R-06`** | **Luogu P5960 — `【模板】差分约束`** | Pure Bellman–Ford feasibility check for $\pi_v - \pi_u \le c_{uv}$ without LP dual objective optimization. |
| **`R-07`** | **LOJ #102 — `最小费用流`** | Standard MCMF template benchmark. |
| **`R-08`** | **POJ 1275 — `Cashier Employment`** | Direct 24-hour circular difference-constraint / Bellman–Ford binary search template. |

---

## Multilingual Bibliography (`[EN]` / `[ZH]` / `[JA]`)

### `[EN]` Foundational Papers, Monographs & English Resources
1. **Hoffman, A. J., & Kruskal, J. B. (1956)**. *Integral boundary points of convex polyhedra*. In *Linear Inequalities and Related Systems*, Annals of Mathematics Studies, Vol. 38, pp. 223–246, Princeton University Press. (Proves the Hoffman–Kruskal Theorem equating integral polyhedral vertices with Total Unimodularity.)
2. **Ghouila-Houri, A. (1962)**. *Caractérisation des matrices totalement unimodulaires*. Comptes Rendus Hebdomadaires des Séances de l'Académie des Sciences, 254, 1192–1194. (Proves the equitable row/column bicoloring criterion for TU matrices.)
3. **Edmonds, J. (1970)**. *Submodular functions, matroids, and certain polyhedra*. In *Combinatorial Structures and Their Applications*, pp. 69–87, Gordon and Breach. (Introduces polymatroids, Base Polyhedra $B(f)$, Edmonds' Greedy Algorithm, and the Matroid Intersection Min–Max & Integrality Theorems.)
4. **Edmonds, J., & Giles, R. (1977)**. *A min-max relation for submodular functions on graphs*. Annals of Discrete Mathematics, 1, 185–204. (Introduces Polymatroid / Submodular Network Flows and Total Dual Integrality.)
5. **Lovász, L. (1983)**. *Submodular functions and convexity*. In *Mathematical Programming: The State of the Art*, pp. 235–257, Springer. (Defines the Lovász extension $\hat{f}(x)$ and proves $\hat{f}$ is convex iff $f$ is submodular.)
6. **Kolmogorov, V., & Zabih, R. (2004)**. *What energy functions can be minimized via graph cuts?* IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 26(2), 147–159. (Proves that a degree-2 pseudo-Boolean function is graph-cut representable iff every pairwise term satisfies $A + D \le B + C$.)
7. **Schrijver, A. (2003)**. *Combinatorial Optimization: Polyhedra and Efficiency* (Vols. A, B, C). Springer. (The definitive encyclopedia on TU matrices, network matrices, matroid intersection, and submodular flows.)
8. **Ahuja, R. K., Magnanti, T. L., & Orlin, J. B. (1993)**. *Network Flows: Theory, Algorithms, and Applications*. Prentice Hall. (Chapters 9–11 & 14 cover LP duality for MCMF, Complementary Slackness, and Inverse Network Optimization.)

### `[ZH]` Chinese National Team Papers (`国家集训队论文`) & Pedagogical Treatises
9. **胡伯涛 [Amber] (2007)**. 《最小割模型在信息学竞赛中的应用》 (*Applications of Minimum Cut Models in Olympiad in Informatics*). IOI 2007 Chinese National Training Team Paper (`国家集训队2007论文集`). (Foundational treatise on Maximum Weight Closure, 0-1 Fractional Programming cuts, and Maximum Density Subgraphs.)
10. **周冬 (2008) / NOI 2008 命题报告**. 《线性规划与网络流——谈 `[NOI2008] 志愿者招募` 的建模》 (*Linear Programming and Network Flows: Modelling `[NOI2008] Volunteer Recruitment`*). (Introduces the Equation-Difference Method and Consecutive-Ones LP-to-MCMF compilation to Chinese OI.)
11. **王yisong / 姜志豪 / 钟子谦 (2018–2020)**. 《保序回归问题及其在信息学竞赛中的应用》 (*Isotonic Regression and Its Applications in Competitive Programming*) & 《拟阵交算法及其应用》 (*Matroid Intersection Algorithms and Applications*). Chinese National Training Team Papers (`国家集训队论文集`, covering `[省选联考 2020] 保序回归` and `魔法商店`).
12. **刘汝佳, 陈锋 (2012)**. 《算法竞赛入门经典：训练指南》 & **OI-Wiki**. *线性规划对偶与费用流建模 / 全幺模矩阵与拟阵交*. (Systematic Chinese competitive programming references on Primal–Dual MCMF reductions.)

### `[JA]` Japanese Competitive Programming Treatises (`燃やす埋める` / `劣モジュラ` / `双対`)
13. **`noshi91` (2019–2021)**. *燃やす埋める問題と劣モジュラ関数の最小化* (*Project Selection / Burn-and-Bury Problems and Submodular Function Minimization*). Hatena Blog & AtCoder Editorial Series. (Rigorous classification of submodular binary and $k$-ary penalties and bipartite variable inversion.)
14. **`maspypy` (2020–2023)**. *線形計画法の双対と最小費用流・最大流* (*Linear Programming Duality and Min-Cost Flow / Max-Flow*). `maspyのHP` (`https://maspypy.com/`). (Demonstrates how writing the explicit Primal LP and taking the mechanical Dual eliminates ad-hoc gadget guessing in `AGC`/`ARC` problems.)
15. **`tatyam` & `hos` (2018–2022)**. *最小費用流の双対とポテンシャル復元 / マトロイド交差* (*Dual of Min-Cost Flow, Potential Reconstruction, and Matroid Intersection*). AtCoder Library (ACL) Notes & Competitive Programming Slide Decks.
