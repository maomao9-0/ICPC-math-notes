# Cohort 1 — Wave 2A (Iterations 11–15): Minimum Cut Modelling I — Binary Partitioning, Project Selection, Pseudo-Boolean Optimization (`燃やす埋める`) & Bipartite Variable Flipping

> [!IMPORTANT]
> **Editorial Policy & The "Zero Magic Gadgets" Compilation Mandate**
> This research monograph is part of the Network Flows, Minimum Cuts, Matching, MCMF, and LP Duality textbook project (`flows_research/PLAN.md`). In accordance with `AGENTS.md`, standard maximum-flow library templates (such as Dinic's algorithm or Push-Relabel) are assumed to reside in the reader's personal library and are omitted. Instead, 100% of our focus is devoted to **recognition from non-graph problem statements**, **algebraic compilation via pseudo-Boolean polynomials**, **structural invariants**, **broken-gadget counterexamples**, and **complete problem derivations**.

---

## Executive Overview: Why Minimum Cut Is a Binary Optimization Compiler

Among all topics in competitive programming, **Minimum Cut Modelling**—known in the Chinese literature (`[ZH]`) as **二元关系最小割 / 最大权闭合子图** (following Hu Botao / Amber's seminal 2007 National Team monograph), in the Japanese literature (`[JA]`) as **燃やす埋める (Burn-or-Bury) / Project Selection Problem (PSP)** (systematized by `noshi91`, `maspypy`, `tatyam`, and `snuke`), and in operations research / computer vision (`[EN]`) as **Quadratic Pseudo-Boolean Optimization (QPBO)** (Picard 1976; Kolmogorov & Zabih 2004)—suffers the most from "magic gadget" pedagogy.

A typical contest editorial for a difficult non-graph problem will abruptly announce:
> *"Construct a flow network with source $S$ and sink $T$. For each item $i$, add an edge $S \to i$ of capacity $A_i$. For each pair $(i, j)$ in opposite parities, flip the edges of $j$, add an edge $i \to j$ of capacity $C_{ij}$, and output $\sum A_i - \text{MaxFlow}(S, T)$."*

To a student who does not already know the compilation theory, such an explanation is completely unproducible under contest pressure. Why did a problem about permutations, divisibility, or grid cells turn into an $S$-$T$ cut? Why is the answer $\text{Total} - \text{MinCut}$? Why must some edges have capacity $\infty$ while others have capacity $C_{ij}$? Why did we flip the meaning of $S$ and $T$ on half the vertices, and why does that trick fail the moment the graph contains a triangle?

This monograph eliminates all guesswork by establishing a strict **four-stage algebraic compiler** from raw English problem statements to directed flow networks:

$$\begin{array}{c}
\textbf{Stage 1: Non-Graph Recognition} \\
\text{(2-state choices, } N \le 5000\text{, cyclic/high-treewidth coupling)}
\end{array}
\;\longrightarrow\;
\begin{array}{c}
\textbf{Stage 2: Pseudo-Boolean Polynomial} \\
\min_{x \in \{0,1\}^n} C_0 + \sum_i c_i x_i + \sum_i d_i \bar{x}_i + \sum_{u,v} c_{uv} x_u \bar{x}_v
\end{array}$$

$$\longrightarrow\;
\begin{array}{c}
\textbf{Stage 3: Submodularity & Bipartite Flip} \\
\text{Check } A+D \le B+C\text{; if } A+D > B+C\text{ on bipartite } L \cup R\text{, set } \tilde{x}_j = 1 - x_j
\end{array}
\;\longrightarrow\;
\begin{array}{c}
\textbf{Stage 4: Directed Network Compilation} \\
c_{uv} x_u(1-x_v) \iff u \xrightarrow{c_{uv}} v \text{ with } c_{uv} \ge 0
\end{array}$$

### Summary of Wave 2A Iterations (11–15)

| Iteration | Core Theoretical Pillar | Key Algebraic Identity / Theorem | Canonical Benchmark Problems |
| :--- | :--- | :--- | :--- |
| **Iteration 11** | **Min-Cut as Binary Variable Assignment & Pseudo-Boolean Polynomials** | $\text{cap}(S, T) = \sum_{(u,v) \in E} c(u,v)\, x_u(1 - x_v)$ with $x_S = 1, x_T = 0$ | Basic 2-state partitioning, unary shift normalization |
| **Iteration 12** | **Maximum Weight Closure (`最大权闭合子图`) & Cyclic Pruning** | $\max_{C \text{ closed}} \sum_{v \in C} w_v = \sum_{w_v > 0} w_v - \min_{x} \big(\text{lost } w^+ + \text{paid } |w^-| + \infty \sum x_u\bar{x}_v\big)$ | `[NOI2009] 植物大战僵尸`, `ARC 085 E — MUL`, `[NOI2006] 最大获利` |
| **Iteration 13** | **Pairwise $2 \times 2$ Relations, Submodularity & Higher-Order Clauses** | $2 \times 2$ penalty $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$ is cut-representable $\iff A + D \le B + C$ | `CF 1082 G`, `[国家集训队] 文理分科`, `CF 311 E — Biologist` |
| **Iteration 14** | **Rescuing Supermodular Costs ($A + D > B + C$) via Bipartite Variable Flipping** | Substituting $\tilde{x}_j = 1 - x_j$ for $j \in R$ swaps columns $\begin{pmatrix} A & B \\ C & D \end{pmatrix} \mapsto \begin{pmatrix} B & A \\ D & C \end{pmatrix}$, turning $A+D > B+C$ into $B+C < A+D$ | `[网络流24题] 方格取数`, `ABC 193 F — Zebraness`, `ARC 107 D/F` |
| **Iteration 15** | **Deep Case Study: Cycle-Pair Bipartite Cut Compilation** | Full 4-step derivation of **`AGC 038 F — Two Permutations`** from cycle stiffness to bipartite variable inversion | **`AGC 038 F — Two Permutations`** |

---

## Iteration 11: Min-Cut as Binary Variable Assignment ($x_i \in \{0, 1\}$) & Pseudo-Boolean Cut Polynomials (`燃やす埋める` Foundations)

### 11.1 Step 1: The Non-Graph Diagnostic Signal (Recognition)

How do you recognize that a problem with **no graphs mentioned in the statement** is secretly a Minimum Cut problem? Look for the following confluence of three structural clues:

1. **Binary State Per Elementary Entity**:
   Every decision object $i \in \{1, \dots, n\}$—whether it is an array element, a project, a grid cell, a student, or a permutation cycle—must ultimately be assigned to one of **two mutually exclusive states** (e.g., *Discard vs. Keep*, *Class A vs. Class B*, *Flip vs. Don't Flip*, *Burn vs. Bury*).
2. **Coupled Pairwise or Group Rules with Arbitrary Topology**:
   - Why **Greedy** fails: Choosing state $1$ for item $i$ cascades through a chain of prerequisites or penalties to items $j, k, \dots$, creating non-local trade-offs where locally unprofitable items unlock globally massive rewards.
   - Why **Dynamic Programming** fails: The dependency structure among the $n$ binary variables is not a tree, sequence, or bounded-treewidth graph, and $n$ is far too large for bitmask DP ($n \in [100, 5000]$ rather than $n \le 20$).
3. **Linear / Quadratic Cost Structure with Moderate Bounds**:
   The objective function is an additive sum of individual state rewards/costs and pairwise (or small-subset) interaction terms, and the total number of variables plus interaction clauses satisfies $V \le 10^4, E \le 10^5$—the exact sweet spot where Dinic's algorithm runs in milliseconds.

---

### 11.2 Step 2: Intermediate Algebraic Representation — Pseudo-Boolean Cut Polynomials

Before drawing a single vertex or arrow, we establish the exact algebraic isomorphism between **$S$-$T$ cuts in a directed network** and **quadratic pseudo-Boolean polynomials**.

#### Definition 11.1 ($S$-$T$ Cut as a Binary Indicator Vector)

Let $G = (V, E, c)$ be a directed flow network with source $S \in V$, sink $T \in V$ ($S \neq T$), and non-negative edge capacities $c: E \to \mathbb{R}_{\ge 0}$. An **$S$-$T$ cut** is a partition of the vertex set $V = V_S \sqcup V_T$ such that $S \in V_S$ and $T \in V_T$.

We encode any partition $(V_S, V_T)$ by associating each vertex $v \in V$ with a binary decision variable $x_v \in \{0, 1\}$ defined by:

$$x_v = \begin{cases} 1, & \text{if } v \in V_S \quad (\text{assigned to the Source side } S), \\ 0, & \text{if } v \in V_T \quad (\text{assigned to the Sink side } T). \end{cases}$$

Under this encoding, the source and sink are simply **clamped boundary variables**:

$$x_S = 1, \qquad x_T = 0.$$

Conversely, any binary assignment $x \in \{0, 1\}^V$ satisfying $x_S = 1$ and $x_T = 0$ uniquely defines the $S$-$T$ cut $V_S = \{v \in V : x_v = 1\}$ and $V_T = \{v \in V : x_v = 0\}$.

#### Proposition 11.2 (The Fundamental Edge-Cut Monomial)

In a directed network $G = (V, E, c)$, a directed edge $(u \to v) \in E$ contributes its capacity $c(u, v)$ to the cut capacity $\text{cap}(V_S, V_T)$ **if and only if** the edge starts in $V_S$ and ends in $V_T$—that is, $u \in V_S$ ($x_u = 1$) and $v \in V_T$ ($x_v = 0$).

For binary variables $x_u, x_v \in \{0, 1\}$, the logical predicate $[x_u = 1 \land x_v = 0]$ equals the quadratic monomial $x_u(1 - x_v)$:

$$\begin{array}{c|cc|c}
(x_u, x_v) & u \text{ side} & v \text{ side} & \text{Does } (u \to v) \text{ cross } V_S \to V_T\text{?} \quad x_u(1 - x_v) \\
\hline
(0, 0) & V_T & V_T & 0 \cdot (1 - 0) = 0 \quad (\text{No: internal to } V_T) \\
(0, 1) & V_T & V_S & 0 \cdot (1 - 1) = 0 \quad (\text{No: backward } V_T \to V_S \text{ is free!}) \\
(1, 0) & V_S & V_T & 1 \cdot (1 - 0) = 1 \quad (\textbf{Yes: severed by the cut!}) \\
(1, 1) & V_S & V_S & 1 \cdot (1 - 1) = 0 \quad (\text{No: internal to } V_S)
\end{array}$$

Summing over all directed edges $(u \to v) \in E$, the capacity of the cut $x$ is the **Pseudo-Boolean Cut Polynomial**:

$$\text{cap}(x) = \sum_{(u \to v) \in E} c(u, v)\, x_u (1 - x_v).$$

Therefore, by the Max-Flow Min-Cut Theorem, finding a minimum $S$-$T$ cut in $G$ is **identical** to solving the discrete optimization problem:

$$\min_{\substack{x \in \{0, 1\}^V \\ x_S = 1,\, x_T = 0}} \sum_{(u \to v) \in E} c(u, v)\, x_u (1 - x_v), \qquad c(u, v) \ge 0.$$

> [!NOTE]
> **Convention Translation Box: Source-is-1 (`[ZH]`/`[EN]`) vs. Sink-is-1 (`[JA]` `燃やす埋める`)**
> Across the global literature, two mirror-image conventions exist for mapping $\{0, 1\}$ to $\{V_S, V_T\}$:
> 1. **Convention A — Source-is-1 ($x_S = 1, x_T = 0$, used throughout this monograph)**:
>    - $x_v = 1 \iff v \in V_S$ ("Selected / True / State 1"), $x_v = 0 \iff v \in V_T$ ("Unselected / False / State 0").
>    - Directed edge $u \xrightarrow{c} v$ compiles the monomial $c \cdot x_u(1 - x_v)$ (penalizing $x_u = 1, x_v = 0$).
>    - Unary edge $S \xrightarrow{c} v$ compiles $c \cdot x_S(1 - x_v) = c(1 - x_v)$ (penalizing $x_v = 0$).
>    - Unary edge $v \xrightarrow{c} T$ compiles $c \cdot x_v(1 - x_T) = c x_v$ (penalizing $x_v = 1$).
>    - *Why we use Convention A*: In Project Selection (`最大权闭合子图`), "choosing project $u$" naturally corresponds to $x_u = 1$ ($u \in V_S$), and the implication $u \text{ chosen} \implies v \text{ chosen}$ ($x_u = 1 \implies x_v = 1$) compiles directly to $u \xrightarrow{\infty} v$ without reversing all dependency arrows.
> 2. **Convention B — Sink-is-1 ($y_S = 0, y_T = 1$, common in Japanese `燃やす埋める` blogs)**:
>    - $y_v = 0 \iff v \in V_S$ ("Burn"), $y_v = 1 \iff v \in V_T$ ("Bury").
>    - Under the substitution $y_v = 1 - x_v$, a directed edge $u \xrightarrow{c} v$ is cut when $y_u = 0 \land y_v = 1$, compiling the monomial $c \cdot (1 - y_u) y_v$.
>    - Both conventions produce isomorphic graphs (up to $S \leftrightarrow T$ edge reversal). We state Convention A ($x_S = 1, x_T = 0$) once and maintain it with **100% consistency** across every derivation in this monograph.

---

### 11.3 Converting Maximization into Minimization: The Optimistic Baseline Principle

Why can we not simply solve $\max_x \text{Profit}(x)$ by finding a *maximum* $S$-$T$ cut? Because **Maximum Cut is NP-hard** even on unweighted graphs (Karp 1972); the linear programming relaxation of Max-Flow dualizes only to **Minimum Cut** ($\min_x \text{cap}(x)$ with $c(u, v) \ge 0$).

Consequently, whenever a problem asks to **maximize** a total score or profit:

$$\max_{x \in \{0, 1\}^n} \text{Score}(x),$$

we must algebraically convert it into a **minimization of lost rewards plus incurred penalties**.

#### The Optimistic Baseline Transformation (`收益转代价` / `理想総利益 - 最小損失`)

Suppose the objective function is a sum of terms $f_\alpha(x)$, where some terms are **rewards** $R_\alpha(x) \ge 0$ (which we want to collect) and others are **penalties** $P_\beta(x) \ge 0$ (which we must pay):

$$\text{Score}(x) = \sum_{\alpha} R_\alpha(x) - \sum_{\beta} P_\beta(x).$$

For each reward term $R_\alpha(x)$, let $M_\alpha = \max_{x \in \{0,1\}^n} R_\alpha(x)$ be the **maximum possible value** that $R_\alpha$ could ever attain (the "Optimistic Baseline" or "Heavenly Payout" assuming all wishes come true simultaneously). Define the **Lost Reward** (or **Regret**) of term $\alpha$ as:

$$\text{Loss}_\alpha(x) := M_\alpha - R_\alpha(x) \ge 0.$$

Substituting $R_\alpha(x) = M_\alpha - \text{Loss}_\alpha(x)$ into the objective gives:

$$\max_{x \in \{0, 1\}^n} \text{Score}(x) = \max_{x \in \{0, 1\}^n} \left( \sum_{\alpha} M_\alpha - \sum_{\alpha} \text{Loss}_\alpha(x) - \sum_{\beta} P_\beta(x) \right)$$

$$\boxed{\max_{x \in \{0, 1\}^n} \text{Score}(x) = \underbrace{\sum_{\alpha} M_\alpha}_{\text{Constant } R_{\max}} - \min_{x \in \{0, 1\}^n} \underbrace{\left( \sum_{\alpha} \text{Loss}_\alpha(x) + \sum_{\beta} P_\beta(x) \right)}_{\text{Total Cut Penalty } E(x) \ge 0}.}$$

Notice what this achieves:
1. Every term inside the minimization $E(x)$ is now **non-negative** ($\text{Loss}_\alpha(x) \ge 0$ and $P_\beta(x) \ge 0$).
2. Maximizing $\text{Score}(x)$ is reduced to **minimizing** $E(x)$ via an $S$-$T$ minimum cut!

---

### 11.4 Step 3: Reverse-Engineering Scratchpad — Unary Cost Compilation & Normalization

Let us compile all single-variable (unary) terms into network edges and resolve the issue of negative costs.

#### 1. Basic Unary Term Compilation

Because $x_S = 1$ and $x_T = 0$, the two linear basis functions of a single binary variable $x_i \in \{0, 1\}$ are special cases of the quadratic cut monomial $x_u(1 - x_v)$ when one endpoint is $S$ or $T$:

- **Penalty $p_i \ge 0$ paid when $x_i = 1$ ($i \in V_S$)**:
  Write $p_i x_i = p_i x_i (1 - x_T)$. This is compiled by a directed edge from $i$ to the sink $T$:
  $$i \xrightarrow{\; p_i \;} T \qquad \Longleftrightarrow \qquad \text{cost } p_i x_i.$$
- **Penalty $q_i \ge 0$ paid when $x_i = 0$ ($i \in V_T$)**:
  Write $q_i (1 - x_i) = q_i x_S (1 - x_i)$. This is compiled by a directed edge from the source $S$ to $i$:
  $$S \xrightarrow{\; q_i \;} i \qquad \Longleftrightarrow \qquad \text{cost } q_i (1 - x_i).$$

```
        q_i (cut if x_i = 0)            p_i (cut if x_i = 1)
   (S) ----------------------> ( i ) ----------------------> (T)
  x_S=1                       x_i in {0,1}                  x_T=0
```

Look at this diagram visually:
- Since $S \in V_S$ and $T \in V_T$, the two-edge path $S \xrightarrow{q_i} i \xrightarrow{p_i} T$ connects $S$ to $T$.
- Any $S$-$T$ cut must place $i$ either in $V_T$ ($x_i = 0$, severing $S \to i$ of cost $q_i$) or in $V_S$ ($x_i = 1$, severing $i \to T$ of cost $p_i$).

#### 2. Why Negative Edge Capacities Are Strictly Forbidden

What happens if an intermediate algebraic derivation produces a unary term $p_i x_i$ with $p_i < 0$ (or a pairwise term $c_{uv} x_u(1 - x_v)$ with $c_{uv} < 0$), and a naive programmer feeds an edge of negative capacity into Dinic's algorithm?

1. **Algorithmic Breakdown**: Augmenting-path and preflow-push algorithms require residual capacities $c_f(u, v) \ge 0$ as their feasibility invariant. An edge with initial capacity $c(u, v) < 0$ violates feasibility before a single unit of flow is sent; attempting to "push negative flow" creates infinite loops around residual 2-cycles $(u \to v \to u)$.
2. **Polyhedral Breakdown**: The Max-Flow Min-Cut Theorem relies on the total unimodularity and non-negativity of the cut function. When $c(u, v) < 0$, the cut capacity function $\text{cap}(S, T)$ ceases to be submodular, and minimizing it becomes NP-hard in general.

#### 3. Two Exact Normalization Recipes for Arbitrary Unary Costs

Fortunately, **any** unary cost table on a single variable $x_i \in \{0, 1\}$—even one containing negative numbers—can always be normalized to have **non-negative capacities**, and in fact requires **at most one edge** incident to $i$!

Suppose choosing $x_i = 0$ incurs cost $A_i \in \mathbb{R}$ and choosing $x_i = 1$ incurs cost $B_i \in \mathbb{R}$ (where $A_i, B_i$ may be positive, zero, or negative). The unary function is:

$$U_i(x_i) = A_i (1 - x_i) + B_i x_i.$$

##### Recipe 1: Minimum Extraction / Cancellation (`差値正規化`)
Since $(1 - x_i) + x_i = 1$ holds identically for all $x_i \in \{0, 1\}$, define $m_i = \min(A_i, B_i)$. We can extract $m_i = m_i(1 - x_i) + m_i x_i$ as a constant outside the cut:

$$U_i(x_i) = m_i + (A_i - m_i)(1 - x_i) + (B_i - m_i) x_i.$$

Because $m_i = \min(A_i, B_i)$, both $(A_i - m_i) \ge 0$ and $(B_i - m_i) \ge 0$, and **at least one of them is zero**:
- **Case 1 ($A_i \le B_i$)**: $m_i = A_i$, so $U_i(x_i) = A_i + (B_i - A_i) x_i$. Add $A_i$ to the constant baseline $C_0$, and add a single edge $i \xrightarrow{B_i - A_i} T$ (capacity $\ge 0$).
- **Case 2 ($B_i < A_i$)**: $m_i = B_i$, so $U_i(x_i) = B_i + (A_i - B_i)(1 - x_i)$. Add $B_i$ to the constant baseline $C_0$, and add a single edge $S \xrightarrow{A_i - B_i} i$ (capacity $> 0$).

> [!TIP]
> **Performance Bonus of Recipe 1**: Notice that if you initially added both $S \xrightarrow{A_i} i$ and $i \xrightarrow{B_i} T$ with $A_i, B_i > 0$, Dinic's very first blocking flow would immediately push $\min(A_i, B_i)$ units of flow along the 2-edge path $S \to i \to T$, saturating the smaller edge! Applying Recipe 1 algebraically before building the graph **pre-pushes all trivial 2-edge $S \to i \to T$ flows in $O(1)$ time**, shrinking the edge count and speeding up Dinic!

##### Recipe 2: Uniform Constant Shift (`ゲタを履かせる` / Pedestal Shift)
Alternatively, choose a large constant $M \ge \max(-A_i, -B_i, 0)$ and rewrite:

$$U_i(x_i) = -M + (A_i + M)(1 - x_i) + (B_i + M) x_i.$$

Since $A_i + M \ge 0$ and $B_i + M \ge 0$, both $S \xrightarrow{A_i + M} i$ and $i \xrightarrow{B_i + M} T$ have non-negative capacities, and we subtract $M$ from the final answer after computing the min-cut.

---

### 11.5 Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Worked Toy Trace ($N = 3$ Binary Assignment)

**Problem**: We have $3$ items $i \in \{1, 2, 3\}$, each assigned $x_i \in \{0, 1\}$.
- Item rewards for choosing $x_i = 1$: $w = (+10, -4, +6)$.
- Pairwise penalties:
  - If $x_1 = 1$ and $x_2 = 0$, we pay a penalty of $7$.
  - If $x_3 = 1$ and $x_2 = 0$, it is **strictly forbidden** (cost $\infty$).
Find $\max_{x \in \{0,1\}^3} \text{Score}(x)$.

**Algebraic Compilation**:
1. Write the score polynomial:
   $$\text{Score}(x) = 10 x_1 - 4 x_2 + 6 x_3 - 7 x_1(1 - x_2) - \infty x_3(1 - x_2).$$
2. Extract the optimistic baseline from positive rewards ($10$ from $x_1 = 1$ and $6$ from $x_3 = 1$, so $R_{\max} = 10 + 6 = 16$) by substituting $x_1 = 1 - (1 - x_1)$ and $x_3 = 1 - (1 - x_3)$:
   $$\text{Score}(x) = 16 - \underbrace{\Big[ 10(1 - x_1) + 4 x_2 + 6(1 - x_3) + 7 x_1(1 - x_2) + \infty x_3(1 - x_2) \Big]}_{E(x)}.$$
3. Compile each term of $E(x)$ into a directed edge:
   - $10(1 - x_1) \implies S \xrightarrow{10} 1$
   - $4 x_2 \implies 2 \xrightarrow{4} T$
   - $6(1 - x_3) \implies S \xrightarrow{6} 3$
   - $7 x_1(1 - x_2) \implies 1 \xrightarrow{7} 2$
   - $\infty x_3(1 - x_2) \implies 3 \xrightarrow{\infty} 2$

**Exhaustive Cut Verification Table**:
Let us check all $2^3 = 8$ assignments $x = (x_1, x_2, x_3)$:

| $(x_1, x_2, x_3)$ | Severed Edges Crossed from $V_S$ ($x=1$) to $V_T$ ($x=0$) | Cut Cost $E(x)$ | $\text{Score}(x) = 16 - E(x)$ |
| :---: | :--- | :---: | :---: |
| $(0, 0, 0)$ | $S \to 1 \;(10),\; S \to 3 \;(6)$ | $16$ | $0$ |
| $(0, 0, 1)$ | $S \to 1 \;(10),\; 3 \to 2 \;(\infty)$ | $\infty$ | $-\infty$ (Invalid) |
| $(0, 1, 0)$ | $S \to 1 \;(10),\; S \to 3 \;(6),\; 2 \to T \;(4)$ | $20$ | $-4$ |
| $(0, 1, 1)$ | $S \to 1 \;(10),\; 2 \to T \;(4)$ | $14$ | $+2$ |
| $(1, 0, 0)$ | $1 \to 2 \;(7),\; S \to 3 \;(6)$ | $13$ | $+3$ |
| $(1, 0, 1)$ | $1 \to 2 \;(7),\; 3 \to 2 \;(\infty)$ | $\infty$ | $-\infty$ (Invalid) |
| $(1, 1, 0)$ | $2 \to T \;(4),\; S \to 3 \;(6)$ | $10$ | $+6$ |
| **$(1, 1, 1)$** | **$2 \to T \;(4)$** | **$4$ (Min-Cut)** | **$16 - 4 = +12$ (Max)** |

The minimum cut is $E(1, 1, 1) = 4$ (severing only $2 \xrightarrow{4} T$), giving the maximum score $16 - 4 = 12$. Notice why $(1, 0, 0)$ is suboptimal ($+3$) even though item $2$ has a negative weight ($-4$): paying $4$ to set $x_2 = 1$ unlocks $+6$ from item $3$ and saves the $7$ penalty from item $1$, for a net gain of $+6 + 7 - 4 = +9$!

#### Broken Gadget Counterexamples

- **Counterexample 11.A (Using an Undirected Edge for an Asymmetric Implication)**:
  Suppose a student replaces the directed edge $3 \xrightarrow{\infty} 2$ with an **undirected** edge $3 \stackrel{\infty}{\longleftrightarrow} 2$ (both $3 \to 2$ and $2 \to 3$ with capacity $\infty$). Then the polynomial gains an extra term $\infty x_2(1 - x_3)$, which forbids $(x_2 = 1, x_3 = 0)$! That would falsely require "choosing item 2 forces choosing item 3", destroying valid states like $(1, 1, 0)$ if $w_3$ were negative.
- **Counterexample 11.B (Reversing Source/Sink Unary Edges)**:
  Suppose a student connects positive-reward items to $T$ ($1 \xrightarrow{10} T, 3 \xrightarrow{6} T$) and negative-cost items to $S$ ($S \xrightarrow{4} 2$) while keeping $1 \xrightarrow{7} 2$ and $3 \xrightarrow{\infty} 2$. Then when $x_3 = 1$ ($3 \in V_S$) and $x_2 = 0$ ($2 \in V_T$), $3 \to T$ is cut (meaning item 3 is *chosen*), and $3 \to 2$ is ALSO cut! Thus choosing item 3 and NOT choosing item 2 would cost $\infty$, which happens to match the implication, **except** that now $x_3 = 1$ pays $6$ instead of $x_3 = 0$ paying $6$! In other words, the student inverted the meaning of $x_i$ on the unary edges without inverting the direction of the dependency edges $3 \to 2 \implies 2 \to 3$. This is why fixing $x_S = 1, x_T = 0$ and writing $x_u(1 - x_v)$ algebraically prevents all orientation bugs.

---

## Iteration 12: Maximum Weight Closure of a Graph (`最大权闭合子图` / Picard's Project Selection) & Cyclic Dependency Pruning

### 12.1 Step 1: The Non-Graph Diagnostic Signal (Recognition)

The **Maximum Weight Closure Problem** (introduced by Jean-Claude Picard in 1976 as the *Maximal Closure of a Graph* and popularized in Chinese competitive programming by Hu Botao's 2007 monograph) is the single most frequent Minimum Cut archetype.

**Diagnostic Signal**:
1. We have a universe of items/events/decisions $V$, each carrying a **signed weight** $w_v \in \mathbb{R}$:
   - $w_v > 0$: a profitable project, a reward clause, a customer demand, or a target cell.
   - $w_v < 0$: a prerequisite tool, a tax, an infrastructure cost, or a defensive obstacle.
2. The decisions are governed by **pure one-way implications (prerequisites)**:
   $$\text{"If we select } u\text{, we MUST also select } v\text{"} \qquad (u \in C \implies v \in C).$$
3. Once a prerequisite $v$ is paid for ($v \in C$), it can satisfy the requirements of **arbitrarily many** dependents $u_1, u_2, \dots, u_k$ at no additional cost! (This shared-cost reuse is why neither greedy nor independent bipartite matching works.)

---

### 12.2 Step 2: Intermediate Algebraic Representation — Picard's Closure Theorem

#### Definition 12.1 (Closed Subgraph / Closure)

Let $G_{\text{dep}} = (V, E_{\text{dep}})$ be a directed dependency graph with vertex weights $w: V \to \mathbb{R}$, where a directed edge $(u \to v) \in E_{\text{dep}}$ means *"selecting $u$ requires selecting $v$"*. A subset $C \subseteq V$ is called a **closure** (or **closed vertex set**, `闭合子图`) if no dependency edge leaves $C$:

$$\forall (u \to v) \in E_{\text{dep}}, \qquad u \in C \implies v \in C.$$

Our goal is to find a closure $C \subseteq V$ maximizing total weight $W(C) = \sum_{v \in C} w_v$.

#### Theorem 12.2 (Picard 1976 — Exact Compilation of Maximum Weight Closure to Min-Cut)

Partition $V$ into positive-weight vertices $V^+ = \{v \in V : w_v > 0\}$ and non-positive-weight vertices $V^- = \{v \in V : w_v \le 0\}$. Construct a flow network $\mathcal{N} = (V \cup \{S, T\}, E_{\mathcal{N}}, c)$ as follows:
1. For every $v \in V^+$, add a directed edge $S \xrightarrow{\; w_v \;} v$.
2. For every $v \in V^-$, add a directed edge $v \xrightarrow{\; |w_v| \;} T$ (where $|w_v| = -w_v \ge 0$).
3. For every dependency $(u \to v) \in E_{\text{dep}}$, add a directed edge $u \xrightarrow{\; \infty \;} v$.

Then the maximum weight of any closure $C \subseteq V$ is given by:

$$\max_{C \text{ closed}} \sum_{v \in C} w_v = \sum_{v \in V^+} w_v - \text{MinCut}(\mathcal{N}),$$

and the optimal closure is recovered constructively from the minimum cut $(V_S, V_T)$ as $C^* = V_S \setminus \{S\} = \{v \in V : v \text{ is reachable from } S \text{ in the residual graph } \mathcal{N}_f\}$.

#### Proof (Via Pseudo-Boolean Polynomial Compilation)

Encode any subset $C \subseteq V$ by indicator variables $x_v = [v \in C] \in \{0, 1\}$.
1. **Hard Prerequisite Constraints**:
   The closure condition $u \in C \implies v \in C$ is equivalent to forbidding $(x_u = 1, x_v = 0)$, i.e., $x_u(1 - x_v) = 0$. In a minimization objective bounded above by $\sum_{v \in V^+} w_v < \infty$, this hard constraint is enforced exactly by adding the penalty term:
   $$\sum_{(u \to v) \in E_{\text{dep}}} \infty \cdot x_u (1 - x_v).$$
2. **Objective Decomposition**:
   Split the linear objective $\sum_{v \in V} w_v x_v$ across $V^+$ and $V^-$, and apply the Optimistic Baseline substitution $x_v = 1 - (1 - x_v)$ on $V^+$:
   $$\begin{aligned}
   \sum_{v \in V} w_v x_v &= \sum_{v \in V^+} w_v x_v - \sum_{v \in V^-} |w_v| x_v \\
   &= \sum_{v \in V^+} w_v \big(1 - (1 - x_v)\big) - \sum_{v \in V^-} |w_v| x_v \\
   &= \underbrace{\sum_{v \in V^+} w_v}_{\text{Optimistic Baseline}} - \left( \sum_{v \in V^+} w_v (1 - x_v) + \sum_{v \in V^-} |w_v| x_v \right).
   \end{aligned}$$
3. **Unconstrained Cut Minimization**:
   Combining the objective loss and the prerequisite penalties yields:
   $$\max_{C \text{ closed}} \sum_{v \in C} w_v = \sum_{v \in V^+} w_v - \min_{\substack{x \in \{0,1\}^V \\ x_S=1,\, x_T=0}} \left( \sum_{v \in V^+} w_v x_S(1 - x_v) + \sum_{v \in V^-} |w_v| x_v(1 - x_T) + \sum_{(u \to v) \in E_{\text{dep}}} \infty \cdot x_u(1 - x_v) \right).$$
   By Proposition 11.2, the expression inside $\min_x(\cdots)$ is literally the cut capacity $\text{cap}(V_S, V_T)$ of $\mathcal{N}$! Since the trivial cut $V_S = \{S\}, V_T = V \cup \{T\}$ (corresponding to $C = \emptyset$) has finite capacity $\sum_{v \in V^+} w_v < \infty$, any minimum cut has finite capacity and therefore cannot sever any $\infty$-capacity edge $(u \to v) \in E_{\text{dep}}$, guaranteeing that $C^* = V_S \setminus \{S\}$ is a valid closure. $\blacksquare$

---

### 12.3 Step 3: Reverse-Engineering Scratchpad — Three Canonical Non-Graph Closure Archetypes

In actual contests, the dependency graph $G_{\text{dep}}$ is rarely given explicitly as a list of projects and tools. Instead, it is hidden inside **bipartite hyperedges**, **interval inclusion pyramids**, or **number-theoretic divisibility lattices**. Let us compile all three.

#### Archetype 12.A: Bipartite Project–Tool / Hyperedge Reward Closure (`太空飞行计划`, `[NOI2006] 最大获利`, `CF 1082 G`)

- **Surface Statement**: We can buy base elements $i \in \{1, \dots, n\}$ at cost $c_i \ge 0$. We are also given $m$ subsets (or pairs) $S_1, \dots, S_m \subseteq \{1, \dots, n\}$; if we buy **all** elements in $S_j$, we earn a bonus reward $r_j > 0$.
- **Algebraic Formulation**:
  Introduce binary variables $x_i \in \{0, 1\}$ for buying base element $i$, and auxiliary binary variables $y_j \in \{0, 1\}$ for claiming bonus $S_j$.
  Claiming bonus $j$ ($y_j = 1$) is valid if and only if $x_i = 1$ for every $i \in S_j$:
  $$y_j = 1 \implies x_i = 1 \quad (\forall i \in S_j) \qquad \Longleftrightarrow \qquad \infty \cdot y_j (1 - x_i).$$
  The objective is $\max_{x, y} \sum_{j=1}^m r_j y_j - \sum_{i=1}^n c_i x_i$, which is a pure Maximum Weight Closure with positive nodes $y_j$ ($w_{y_j} = +r_j$), negative nodes $x_i$ ($w_{x_i} = -c_i$), and prerequisite edges $y_j \xrightarrow{\infty} x_i$ for all $i \in S_j$.
- **Graph Size**: $V = n + m + 2$ vertices and $E = n + m + \sum_{j=1}^m |S_j|$ edges. When each $S_j$ is a pair $\{u_j, v_j\}$ (as in `[NOI2006] 最大获利` and `CF 1082 G`), $V = n + m + 2$ and $E = n + 3m$.

#### Archetype 12.B: Contiguous Interval Pyramid Closure (`区间金字塔闭合` — `[CEOI 2008] Order`, Sushi / Subarray Closures)

- **Surface Statement**: We have $N \le 100$ array positions, and for every contiguous subarray $[l, r]$ ($1 \le l \le r \le N$), there is a signed reward/cost $w_{l, r} \in \mathbb{R}$ earned if we select the subarray $[l, r]$. Moreover, selecting a larger interval $[l, r]$ automatically encompasses (requires) selecting all its sub-intervals $[l', r'] \subseteq [l, r]$ (or all individual elements $k \in [l, r]$).
- **Naive Compilation Trap**: If each interval node $I_{l, r}$ ($O(N^2)$ nodes) adds a direct $\infty$-edge to every sub-interval $I_{l', r'} \subseteq I_{l, r}$ (or every element $k \in [l, r]$), the graph has $\Theta(N^4)$ (or $\Theta(N^3)$) edges!
- **Transitive Reduction (The Pyramid Trick)**:
  Because logical implication $\implies$ is **transitive** ($x_A \implies x_B$ and $x_B \implies x_C$ automatically forces $x_A \implies x_C$ via the 2-edge path $A \xrightarrow{\infty} B \xrightarrow{\infty} C$), each interval node $I_{l, r}$ with $l < r$ only needs **two** outgoing $\infty$-edges to its immediate length-$(r-l)$ children:
  $$I_{l, r} \xrightarrow{\; \infty \;} I_{l+1, r}, \qquad I_{l, r} \xrightarrow{\; \infty \;} I_{l, r-1}.$$

```
                       [1, 3]
                      /      \
                 inf /        \ inf
                    v          v
                 [1, 2]      [2, 3]
                 /    \      /    \
            inf /  inf \    / inf  \ inf
               v        v  v        v
            [1, 1]     [2, 2]     [3, 3]
```

  By induction on interval length $len = r - l + 1$, $I_{l, r}$ can reach $I_{l', r'}$ via $\infty$-edges if and only if $[l', r'] \subseteq [l, r]$!
  - **Complexity Gain**: Each of the $\binom{N+1}{2}$ interval vertices has out-degree at most $2$ in $E_{\text{dep}}$, slashing the dependency edge count from $O(N^4)$ down to **$2 \binom{N}{2} = N(N-1) = O(N^2)$**!

#### Archetype 12.C: Divisibility Poset Closure (`ARC 085 E — MUL`)

- **Surface Statement (`[AtCoder ARC 085 E — MUL]`)**: We have $N \le 100$ gems numbered $1, \dots, N$ with signed values $a_1, \dots, a_N \in \mathbb{Z}$. For any integer $k \in \{1, \dots, N\}$, we may perform the operation "smash all gems whose index is a multiple of $k$ ($k, 2k, 3k, \dots$)". Maximize the sum of values of the **remaining (unsmashed)** gems.
- **Step 1 (Recognition)**: $N \le 100$, each gem $i$ is either *Kept* or *Smashed*, and $a_i$ can be positive or negative. Inclusion-exclusion over primes fails because $k$ can be composite and subsets overlap arbitrarily.
- **Step 2 (Algebraic Closure Reduction)**:
  Wait—whichsubsets of gems can remain unsmashed?
  - Suppose we decide to **smash** index $i$. We can accomplish this by smashing $k = i$, which simultaneously smashes all multiples $2i, 3i, \dots, m \cdot i$.
  - Conversely, if we do *not* smash $i$, could $i$ still be smashed by some divisor $d \mid i$? If it were, then $i$ would be smashed anyway! Thus, without loss of generality, the set of smashed indices $D \subseteq \{1, \dots, N\}$ is achievable **if and only if** $D$ is closed under taking multiples:
    $$i \in D \implies (j \in D \quad \forall j \text{ with } i \mid j).$$
  - Now translate this into our **Kept** indicator variable $x_i \in \{0, 1\}$, where $x_i = 1$ means gem $i$ is **kept** ($i \notin D$) and $x_i = 0$ means gem $i$ is **smashed** ($i \in D$):
    $$i \text{ smashed } (x_i = 0) \implies j \text{ smashed } (x_j = 0) \quad \forall i \mid j.$$
    Taking the contrapositive ($P \implies Q \iff \neg Q \implies \neg P$):
    $$\boxed{j \text{ kept } (x_j = 1) \implies i \text{ kept } (x_i = 1) \quad \forall i \mid j.}$$
    In plain English: **Keeping a multiple $j$ forces us to keep all of its divisors $i \mid j$!** (Because if any divisor $i \mid j$ were smashed by an operation at $i$, its multiple $j$ would have been obliterated along with it!)
- **Step 3 (Graph Compilation)**:
  This is a pure Maximum Weight Closure on $\{1, \dots, N\}$:
  - Weight of vertex $i$ is $w_i = a_i$.
  - If $a_i > 0$, add $S \xrightarrow{a_i} i$ and add $a_i$ to $R_{\max}$.
  - If $a_i < 0$, add $i \xrightarrow{|a_i|} T$.
  - For every $j$ and every divisor $i \mid j$ (or even simpler, only for $j = p \cdot i$ where $p$ is prime, by transitivity of divisibility!), add $j \xrightarrow{\infty} i$ (or keep $x_i = 1 \iff i \text{ smashed}$ and add $i \xrightarrow{\infty} j$; both give the exact same cut!).

---

### 12.4 Step 4: Broken Gadget / Failure Mode — Unreachable Positive Cycles (`[NOI2009] 植物大战僵尸`)

There is a famous, lethal failure mode in Maximum Weight Closure modelling that traps programmers who treat closure constraints $x_u = 1 \implies x_v = 1$ as equivalent to **sequential reachability**. Its canonical showcase is **`[NOI2009] 植物大战僵尸` (Plants vs. Zombies)**.

#### The Problem Setup (`[NOI2009] 植物大战僵尸`, Luogu P2805)

On an $N \times M$ lawn ($N \le 20, M \le 30$), each cell $(r, c)$ contains a plant with a signed score $w_{r, c} \in [-10^4, 10^4]$.
1. Zombies enter from the **right boundary** of each row and walk left: to eat plant $(r, c)$, zombies must first eat $(r, c+1)$ (unless $c = M$).
2. Each plant $u$ also has an attack list $A(u)$ of cells it shoots at: while plant $u$ is alive, any zombie stepping onto a cell $v \in A(u)$ is instantly destroyed. Therefore, to eat plant $v$, we must **first** eat plant $u$!

In short, eating $v$ requires having already eaten $u$:
$$v \text{ eaten} \implies u \text{ eaten} \qquad \big((v \to u) \in E_{\text{dep}}\big).$$

#### The Broken Gadget: Why Raw Max-Weight Closure Fails on Cycles!

Suppose we directly build the Max-Weight Closure flow network on all $NM$ plants using $E_{\text{dep}}$ and run Dinic's algorithm. **Why does this get Wrong Answer?**

Consider a tiny $4$-plant toy instance:
- Plant $1$ has weight $w_1 = +100$ and requires eating Plant $2$ first ($1 \to 2 \in E_{\text{dep}}$).
- Plant $2$ has weight $w_2 = -10$ and requires eating Plant $1$ first ($2 \to 1 \in E_{\text{dep}}$) because they mutually protect each other!
- Plant $3$ has weight $w_3 = +50$ and requires eating Plant $1$ first ($3 \to 1 \in E_{\text{dep}}$).
- Plant $4$ has weight $w_4 = +20$ and has no prerequisites ($E_{\text{dep}}$ out-degree $0$).

```
      +50            +100          -10
    (Plant 3) ===> (Plant 1) <===> (Plant 2)       (Plant 4: +20, no prereqs)
                  [Mutual Protection Cycle!]
```

1. **What happens in the real game (Sequential Eating)**:
   - Can we eat Plant $4$? Yes, it has no prerequisites, earning $+20$.
   - Can we eat Plant $1$, $2$, or $3$? **NO!** To eat Plant $1$, we must *first* eat Plant $2$; to eat Plant $2$, we must *first* eat Plant $1$. Neither can be eaten first! And because Plant $1$ can never be eaten, Plant $3$ (which depends on Plant $1$) can never be eaten either!
   - True maximum score: **$+20$** (eating only Plant $4$).

2. **What the Raw Max-Weight Closure Network Computes (Simultaneous Set Closure)**:
   Look at the algebraic closure constraint for the cycle $1 \leftrightarrows 2$:
   $$\infty \cdot x_1(1 - x_2) + \infty \cdot x_2(1 - x_1).$$
   If the solver sets $x_1 = 1, x_2 = 1, x_3 = 1, x_4 = 1$, what is the value of $\infty \cdot x_1(1 - x_2) + \infty \cdot x_2(1 - x_1)$?
   $$\infty \cdot 1 \cdot (1 - 1) + \infty \cdot 1 \cdot (1 - 1) = 0!$$
   Because the subset $C = \{1, 2, 3, 4\}$ is **closed as a static set** ($1 \in C \implies 2 \in C$ and $2 \in C \implies 1 \in C$ are both vacuously true when *both* are in $C$!), the Min-Cut solver gladly places $\{1, 2, 3, 4\} \subseteq V_S$, pays only $|w_2| = 10$ on edge $2 \xrightarrow{10} T$, and reports a bogus score of:
   $$(+100 - 10 + 50 + 20) = +160 \neq +20!$$

#### Theorem 12.3 (Topological Reachability Pruning for Sequential Closures)

When a problem requires selecting a subset of actions $C \subseteq V$ that can be executed **sequentially one by one** such that all prerequisites of $v$ are executed strictly before $v$ (i.e., $(v \to u) \in E_{\text{dep}}$ means $u$ must precede $v$ in time), a subset $C \subseteq V$ is achievable if and only if:
1. $C$ is closed under $E_{\text{dep}}$, **AND**
2. Every vertex $v \in C$ is contained in the **maximally topologically valid subset** $V_{\text{valid}} \subseteq V$, found by running **Kahn's Topological Sort (BFS queue)** on the reversed graph $G_{\text{prot}} = (V, E_{\text{prot}})$ where $(u \to v) \in E_{\text{prot}} \iff (v \to u) \in E_{\text{dep}}$:
   - Initialize queue $Q$ with all vertices $u \in V$ having $\text{indeg}_{\text{prot}}(u) = 0$ (zero prerequisites).
   - Repeatedly pop $u \in Q$, mark $u \in V_{\text{valid}}$, and decrement $\text{indeg}_{\text{prot}}(v)$ for all $(u \to v) \in E_{\text{prot}}$, pushing $v$ into $Q$ when $\text{indeg}_{\text{prot}}(v) = 0$.

Any vertex $v \notin V_{\text{valid}}$ either lies on a directed cycle in $G_{\text{dep}}$ or depends (directly or indirectly) on a directed cycle in $G_{\text{dep}}$, and can **never** be executed. Once $V \setminus V_{\text{valid}}$ is pruned, the induced subgraph $G_{\text{dep}}[V_{\text{valid}}]$ is a DAG, on which static closure and sequential executability are **100% equivalent**!

> [!CAUTION]
> **Diagnostic Checklist for Closure Cycles**:
> Always ask yourself: *"Does the problem allow selecting a closed cycle of items simultaneously, or must items be unlocked one by one in a valid time order?"*
> - **Simultaneous Closure (Cycles Allowed)**: In `ARC 085 E — MUL` or `[NOI2006] 最大获利`, states are chosen simultaneously (and the dependency graph is naturally a DAG anyway). Even if a simultaneous-selection problem has a cycle $u \leftrightarrows v$, choosing $\{u, v\}$ together is legal and the cycle simply contracts into a single super-node of weight $w_u + w_v$.
> - **Sequential Unlocking (Cycles Forbidden)**: In `[NOI2009] 植物大战僵尸`, eating $u$ requires eating $v$ *earlier in time*. Directed cycles are deadlocks and **must** be stripped via Kahn's topological sort before constructing the flow network!


---

## Iteration 13: Pairwise Binary Relations, Submodularity ($A + D \le B + C$), and Higher-Order Clause Gadgets

### 13.1 Step 1: The Non-Graph Diagnostic Signal (Recognition)

In Iteration 12, every pairwise interaction had the rigid form $\infty \cdot x_u(1 - x_v)$ ("selecting $u$ forces selecting $v$"). In a broader class of problems, entities $i$ and $j$ interact through **soft penalties, correlation bonuses, or general $2 \times 2$ payoff tables**, and subsets of $k \ge 3$ entities may share **all-or-nothing group bonuses**:

1. **General $2 \times 2$ Pairwise Payoff Tables**:
   For each interacting pair $(i, j)$, the problem specifies four numbers—the costs (or rewards) incurred under all four state combinations $(x_i, x_j) \in \{(0,0), (0,1), (1,0), (1,1)\}$.
2. **Same-Group / Correlation Bonuses (`文理分科` / Image Segmentation / Markov Random Fields)**:
   - Choosing the same state for $i$ and $j$ earns a bonus (or choosing different states incurs a boundary penalty $w_{ij} |x_i - x_j|$).
   - Choosing state $1$ for **all** members of a club/neighborhood $I = \{u_1, \dots, u_k\}$ earns a synergy bonus $W_I > 0$.
3. **Why DP and Greedy Fail**:
   The interaction pairs $(i, j)$ and subsets $I$ form a 2D grid or an arbitrary general graph/hypergraph with $N \le 10^3$–$10^4$, ruling out tree DP, profile DP ($N, M \le 100$ is too wide for $O(2^{\min(N,M)})$), and greedy local swaps.

---

### 13.2 Step 2: Intermediate Algebraic Representation — The Submodularity Theorem ($A + D \le B + C$)

Consider any two binary variables $x_i, x_j \in \{0, 1\}$. After converting rewards to penalties via the Optimistic Baseline Principle (Section 11.3), any pairwise interaction between $x_i$ and $x_j$ is completely specified by a $2 \times 2$ penalty matrix:

$$\Theta_{ij}(x_i, x_j) = \begin{array}{c|cc}
x_i \setminus x_j & x_j = 0 & x_j = 1 \\
\hline
x_i = 0 & A & B \\
x_i = 1 & C & D
\end{array}
\quad = \quad
\begin{pmatrix} A & B \\ C & D \end{pmatrix},$$

where:
- $A = \Theta_{ij}(0, 0)$ is the penalty when both $i, j \in V_T$,
- $B = \Theta_{ij}(0, 1)$ is the penalty when $i \in V_T, j \in V_S$,
- $C = \Theta_{ij}(1, 0)$ is the penalty when $i \in V_S, j \in V_T$,
- $D = \Theta_{ij}(1, 1)$ is the penalty when both $i, j \in V_S$.

**Fundamental Question**: *Which $2 \times 2$ penalty matrices $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$ can be compiled into non-negative directed cut edges on $\{S, T, i, j\}$?*

#### Theorem 13.1 (The Submodularity Characterization Theorem — Kolmogorov & Zabih 2004)

A $2 \times 2$ pairwise penalty matrix $\Theta_{ij} = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ can be represented as a constant plus a non-negative linear combination of unary cut terms ($x_i, 1-x_i, x_j, 1-x_j$) and pairwise directed cut edges ($x_i(1 - x_j)$ and $x_j(1 - x_i)$) **if and only if** it satisfies the **Submodularity Inequality**:

$$\boxed{A + D \le B + C \qquad \Longleftrightarrow \qquad \Theta_{ij}(0, 0) + \Theta_{ij}(1, 1) \le \Theta_{ij}(0, 1) + \Theta_{ij}(1, 0).}$$

In plain English: **The sum of penalties on the main diagonal (agreeing states $x_i = x_j$) must not exceed the sum of penalties on the anti-diagonal (disagreeing states $x_i \neq x_j$).**

Furthermore, whenever $A + D \le B + C$ holds, let $\Delta := (B + C) - (A + D) \ge 0$ be the **submodular excess**. For any non-negative split $\alpha, \beta \ge 0$ satisfying $\alpha + \beta = \Delta$, the matrix $\Theta_{ij}(x_i, x_j)$ admits the **exact algebraic identity**:

$$\Theta_{ij}(x_i, x_j) = \underbrace{A}_{\text{constant}} + \underbrace{(C - A - \alpha) x_i}_{\text{unary on } i} + \underbrace{(B - A - \beta) x_j}_{\text{unary on } j} + \underbrace{\alpha\, x_i(1 - x_j)}_{\text{edge } i \xrightarrow{\alpha} j} + \underbrace{\beta\, x_j(1 - x_i)}_{\text{edge } j \xrightarrow{\beta} i}.$$

In particular, choosing the asymmetric canonical split $\alpha = 0, \beta = (B + C) - (A + D) \ge 0$ (or $\alpha = (B + C) - (A + D), \beta = 0$) requires **only a single directed edge** between $i$ and $j$:

$$\boxed{\Theta_{ij}(x_i, x_j) = A + (C - A) x_i + (D - C) x_j + \big[(B + C) - (A + D)\big] (1 - x_i) x_j.}$$

#### Proof (Both Directions + Mechanical Verification)

1. **Proof of Necessity ($\implies$)**:
   Define the linear functional $\mathcal{L}(\Phi) := \Phi(0, 0) + \Phi(1, 1) - \Phi(0, 1) - \Phi(1, 0)$ on functions $\Phi: \{0, 1\}^2 \to \mathbb{R}$. Let us evaluate $\mathcal{L}$ on every building block available in a directed flow network on $\{S, T, i, j\}$:
   - Constant $1$: $\mathcal{L}(1) = 1 + 1 - 1 - 1 = 0$.
   - Unary functions of $x_i$: $\mathcal{L}(x_i) = 0 + 1 - 0 - 1 = 0$, and $\mathcal{L}(1 - x_i) = 1 + 0 - 1 - 0 = 0$.
   - Unary functions of $x_j$: $\mathcal{L}(x_j) = 0 + 1 - 1 - 0 = 0$, and $\mathcal{L}(1 - x_j) = 1 + 0 - 0 - 1 = 0$.
   - Directed cut edge $i \xrightarrow{\alpha} j$, which contributes $\alpha x_i(1 - x_j)$ with $\alpha \ge 0$:
     $$\mathcal{L}\big(\alpha x_i(1 - x_j)\big) = 0 + 0 - 0 - \alpha = -\alpha \le 0.$$
   - Directed cut edge $j \xrightarrow{\beta} i$, which contributes $\beta x_j(1 - x_i)$ with $\beta \ge 0$:
     $$\mathcal{L}\big(\beta x_j(1 - x_i)\big) = 0 + 0 - \beta - 0 = -\beta \le 0.$$
   Even if auxiliary intermediate vertices $z_1, \dots, z_k \in \{0, 1\}$ are introduced, the minimum of a sum of submodular functions over auxiliary binary variables preserves submodularity (since the cut capacity function of any non-negative network is submodular). Hence any cut-representable $\Theta_{ij}$ must satisfy:
   $$\mathcal{L}(\Theta_{ij}) = (A + D) - (B + C) = -(\alpha + \beta) \le 0 \quad \Longleftrightarrow \quad A + D \le B + C.$$

2. **Proof of Sufficiency ($\Longleftarrow$) via Exact Polynomial Expansion**:
   Any function $\Theta_{ij}: \{0, 1\}^2 \to \mathbb{R}$ equals its Lagrange interpolation polynomial over $\{0, 1\}^2$:
   $$\Theta_{ij}(x_i, x_j) = A(1 - x_i)(1 - x_j) + B(1 - x_i)x_j + C x_i(1 - x_j) + D x_i x_j.$$
   Notice that $B(1 - x_i)x_j$ and $C x_i(1 - x_j)$ are already valid cut monomials, whereas $A(1 - x_i)(1 - x_j)$ and $D x_i x_j$ are "same-side" products. We eliminate the same-side products using the elementary identities:
   $$(1 - x_i)(1 - x_j) = 1 - x_i - x_j + x_i x_j,$$
   $$x_i x_j = x_i - x_i(1 - x_j) = x_j - (1 - x_i)x_j.$$
   For any $\alpha, \beta \ge 0$ with $\alpha + \beta = (B + C) - (A + D)$, let us evaluate the right-hand side of our theorem's formula at all four corners $(x_i, x_j) \in \{0, 1\}^2$:
   - At $(0, 0)$: $A + 0 + 0 + 0 + 0 = A$.
   - At $(1, 0)$: $A + (C - A - \alpha)(1) + 0 + \alpha(1)(1) + 0 = C$.
   - At $(0, 1)$: $A + 0 + (B - A - \beta)(1) + 0 + \beta(1)(1) = B$.
   - At $(1, 1)$: $A + (C - A - \alpha)(1) + (B - A - \beta)(1) + 0 + 0 = B + C - A - (\alpha + \beta) = B + C - A - (B + C - A - D) = D$.
   Since two polynomials on $\{0, 1\}^2$ that agree at all $4$ points are identical, the decomposition holds identically! Finally, after summing the unary coefficients of $x_i$ and $x_j$ across all pairs in the problem, we normalize the accumulated unary coefficient of each vertex $i$ using Recipe 1 of Iteration 11 so that all unary edges $S \to i$ and $i \to T$ also have non-negative capacities. $\blacksquare$

---

### 13.3 Step 3: Reverse-Engineering Scratchpad — Pairwise Splits & Higher-Order ($k$-Tuple) Hub Gadgets

#### 1. Choosing the Best Split $(\alpha, \beta)$ for $\Delta = (B + C) - (A + D)$

Theorem 13.1 gives us a 1-parameter family of valid edge capacities $\alpha, \beta \ge 0$ with $\alpha + \beta = \Delta$. Two choices are especially useful in practice:

- **Choice A: Single-Directed-Edge Split ($\alpha = \Delta, \beta = 0$ or $\alpha = 0, \beta = \Delta$)**:
  Adds only **one** directed edge between $i$ and $j$ ($i \xrightarrow{\Delta} j$ or $j \xrightarrow{\Delta} i$).
- **Choice B: Symmetric / Half-Edge Split (`合并点边法` — $\alpha = \beta = \Delta / 2$)**:
  Suppose $i$ and $j$ earn a bonus $W$ when $x_i = x_j = 1$ and another bonus $W'$ when $x_i = x_j = 0$. Converting to lost reward gives $A = W, B = W + W', C = W + W', D = W'$, so $\Delta = (B + C) - (A + D) = (2W + 2W') - (W + W') = W + W'$.
  Setting $\alpha = \beta = \frac{W + W'}{2}$ creates a symmetric undirected pair of edges $i \stackrel{(W+W')/2}{\longleftrightarrow} j$, and adds $\frac{W}{2}$ to the $S$-unary edge and $\frac{W'}{2}$ to the $T$-unary edge of both $i$ and $j$—requiring **zero auxiliary vertices**! (To avoid half-integers when $W + W'$ is odd, either double all capacities or use Choice A!)

#### 2. Compiling Higher-Order ($k$-Tuple) Synergy Clauses (`[国家集训队] 文理分科`, `CF 1082 G`, `CF 311 E`)

What if a reward $W > 0$ is earned only when **all $k$ variables** in a subset $I = \{u_1, u_2, \dots, u_k\}$ ($k \ge 2$) simultaneously take the same state?

In polynomial terms, an all-$1$ bonus is $W \prod_{u \in I} x_u$, and an all-$0$ bonus is $W' \prod_{u \in I} (1 - x_u)$. For $k \ge 3$, these are **degree-$k$ polynomials**! Because every edge in a flow network $u \to v$ only generates a **degree-$2$** monomial $x_u(1 - x_v)$, it is algebraically impossible to represent a degree-$k$ ($k \ge 3$) clause using edges among $\{u_1, \dots, u_k\}$ alone. We **must** introduce an auxiliary binary variable (a hub vertex) to degree-reduce the product!

##### Gadget 13.A: The All-1 AND Clause Hub ($W \prod_{u \in I} x_u$)
- **English Rule**: "If every $u \in I$ has $x_u = 1$ ($u \in V_S$), we gain reward $W > 0$ (equivalently, if at least one $u \in I$ has $x_u = 0$, we lose $W$)."
- **Algebraic Degree Reduction**:
  Add $W$ to the Optimistic Baseline $R_{\max}$. We need to represent the penalty function:
  $$P_{\text{AND}}(x_I) = W \left(1 - \prod_{u \in I} x_u\right) = \begin{cases} 0, & \text{if } x_u = 1 \text{ for all } u \in I, \\ W, & \text{if } \exists u \in I \text{ with } x_u = 0. \end{cases}$$
  Introduce a new binary hub variable $z_I \in \{0, 1\}$ ("do we claim the clause-$I$ bonus?") and consider the quadratic cut polynomial:
  $$\Phi_{\text{AND}}(x_I, z_I) = W(1 - z_I) + \sum_{u \in I} \infty \cdot z_I (1 - x_u).$$
  Let us minimize $\Phi_{\text{AND}}(x_I, z_I)$ over $z_I \in \{0, 1\}$ for fixed $x_I$:
  - If $x_u = 1$ for all $u \in I$: setting $z_I = 1$ gives $\Phi_{\text{AND}} = W(0) + \sum \infty \cdot 1 \cdot 0 = 0$.
  - If $\exists u \in I$ with $x_u = 0$: setting $z_I = 1$ costs $\infty$, so the minimization is forced to set $z_I = 0$, giving $\Phi_{\text{AND}} = W(1 - 0) + 0 = W$!
  Hence $\min_{z_I \in \{0,1\}} \Phi_{\text{AND}}(x_I, z_I) = P_{\text{AND}}(x_I)$ holds **identically**!
- **Graph Compilation**:
  Create hub vertex $z_I$, add edge $S \xrightarrow{\; W \;} z_I$, and add edges $z_I \xrightarrow{\; \infty \;} u$ for all $u \in I$.

##### Gadget 13.B: The All-0 NOR Clause Hub ($W' \prod_{u \in I} (1 - x_u)$)
- **English Rule**: "If every $u \in I$ has $x_u = 0$ ($u \in V_T$), we gain reward $W' > 0$ (equivalently, if at least one $u \in I$ has $x_u = 1$, we lose $W'$)."
- **Algebraic Degree Reduction**:
  Add $W'$ to $R_{\max}$. We need to represent the penalty function:
  $$P_{\text{NOR}}(x_I) = W' \left(1 - \prod_{u \in I} (1 - x_u)\right) = \begin{cases} 0, & \text{if } x_u = 0 \text{ for all } u \in I, \\ W', & \text{if } \exists u \in I \text{ with } x_u = 1. \end{cases}$$
  Introduce a new binary hub variable $w_I \in \{0, 1\}$ (where $w_I = 0$ means we successfully claim the all-$0$ bonus, and $w_I = 1$ means we forfeit it!) and write:
  $$\Phi_{\text{NOR}}(x_I, w_I) = W' w_I + \sum_{u \in I} \infty \cdot x_u (1 - w_I).$$
  Let us minimize $\Phi_{\text{NOR}}(x_I, w_I)$ over $w_I \in \{0, 1\}$ for fixed $x_I$:
  - If $x_u = 0$ for all $u \in I$: setting $w_I = 0$ gives $\Phi_{\text{NOR}} = W'(0) + \sum \infty \cdot 0 \cdot 1 = 0$.
  - If $\exists u \in I$ with $x_u = 1$: setting $w_I = 0$ costs $\infty \cdot 1 \cdot (1 - 0) = \infty$, forcing the min-cut to set $w_I = 1$ and pay $W' w_I = W'$!
  Hence $\min_{w_I \in \{0,1\}} \Phi_{\text{NOR}}(x_I, w_I) = P_{\text{NOR}}(x_I)$ holds **identically**!
- **Graph Compilation**:
  Create hub vertex $w_I$, add edge $w_I \xrightarrow{\; W' \;} T$, and add edges $u \xrightarrow{\; \infty \;} w_I$ for all $u \in I$.

```
    [Gadget 13.A: All-1 Bonus W]                  [Gadget 13.B: All-0 Bonus W']
                 ---> (u_1)                                   (u_1) ---
        W       / inf                                                  \ inf   W'
   (S) ---> (z_I) ---> (u_2)                                  (u_2) ---> (w_I) ---> (T)
                \ inf                                                  / inf
                 ---> (u_k)                                   (u_k) ---
```

> [!TIP]
> **Soft Violation Penalty (`CF 311 E — Biologist`)**:
> What if failing an All-1 (or All-0) clause not only forfeits the reward $W$, but also incurs an **additional penalty $g > 0$** (for a total loss of $W + g$ when failed, while the optimistic baseline still only adds $W$)?
> Look at $\Phi_{\text{AND}}(x_I, z_I)$: the edge $S \to z_I$ is cut precisely when the clause fails ($z_I = 0$)! Therefore, we simply add **only $W$** to the optimistic baseline $R_{\max}$, but set the capacity of the hub edge $S \to z_I$ (or $w_I \to T$) to **$W + g$**!

---

### 13.4 Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Worked Toy Trace (Compiling a General $2 \times 2$ Penalty Table)

Suppose two variables $x_1, x_2 \in \{0, 1\}$ have unary penalties $U_1(x_1) = 5(1 - x_1)$, $U_2(x_2) = 8 x_2$, and the following $2 \times 2$ pairwise penalty matrix:

$$\Theta_{12}(x_1, x_2) = \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} 4 & 9 \\ 7 & 2 \end{pmatrix}.$$

1. **Step 1 (Submodularity Check)**:
   $$A + D = 4 + 2 = 6 \le 16 = 9 + 7 = B + C.$$
   The matrix is strictly submodular with excess $\Delta = (B + C) - (A + D) = 16 - 6 = 10 > 0$.
2. **Step 2 (Apply Canonical Formula with $\alpha = 0, \beta = 10$)**:
   $$\Theta_{12}(x_1, x_2) = 4 + (7 - 4)x_1 + (2 - 7)x_2 + 10(1 - x_1)x_2 = 4 + 3 x_1 - 5 x_2 + 10 x_2(1 - x_1).$$
3. **Step 3 (Combine with Unary Penalties & Normalize via Recipe 1)**:
   Total objective:
   $$\begin{aligned}
   E(x_1, x_2) &= 5(1 - x_1) + 8 x_2 + \big[ 4 + 3 x_1 - 5 x_2 + 10 x_2(1 - x_1) \big] \\
   &= 4 + \big[ 5(1 - x_1) + 3 x_1 \big] + 3 x_2 + 10 x_2(1 - x_1).
   \end{aligned}$$
   Normalize $\big[5(1 - x_1) + 3 x_1\big]$ using $\min(5, 3) = 3 = 3(1 - x_1) + 3 x_1$:
   $$5(1 - x_1) + 3 x_1 = 3 + 2(1 - x_1).$$
   Thus the fully normalized cut polynomial is:
   $$E(x_1, x_2) = \underbrace{7}_{\text{constant } C_0} + \underbrace{2(1 - x_1)}_{S \xrightarrow{2} 1} + \underbrace{3 x_2}_{2 \xrightarrow{3} T} + \underbrace{10 x_2(1 - x_1)}_{2 \xrightarrow{10} 1}.$$
4. **Step 4 (Verify All 4 States)**:
   - $(0, 0)$: $U_1(0) + U_2(0) + \Theta_{12}(0, 0) = 5 + 0 + 4 = 9$. Cut polynomial: $7 + 2(1) + 3(0) + 10(0) = 9$. $\checkmark$
   - $(0, 1)$: $5 + 8 + 9 = 22$. Cut polynomial: $7 + 2(1) + 3(1) + 10(1)(1) = 22$. $\checkmark$
   - $(1, 0)$: $0 + 0 + 7 = 7$. Cut polynomial: $7 + 2(0) + 3(0) + 10(0)(0) = 7$. $\checkmark$
   - $(1, 1)$: $0 + 8 + 2 = 10$. Cut polynomial: $7 + 2(0) + 3(1) + 10(1)(0) = 10$. $\checkmark$

#### Broken Gadget Counterexample (Misorienting the All-0 Hub $\infty$-Edges)

Suppose that in Gadget 13.B (All-0 NOR Clause Hub $w_I$), a programmer accidentally points the $\infty$-edges **from** $w_I$ **to** $u \in I$ ($w_I \xrightarrow{\infty} u$) instead of $u \xrightarrow{\infty} w_I$, while keeping $w_I \xrightarrow{W'} T$.
- Then the polynomial becomes $W' w_I + \sum_{u \in I} \infty \cdot w_I(1 - x_u)$.
- Regardless of what $x_u \in \{0, 1\}$ are, setting $w_I = 0$ (putting $w_I \in V_T$) makes **both** $W' w_I = 0$ and $\infty \cdot w_I(1 - x_u) = 0$!
- Thus the min-cut is $0$ for **every** assignment $x_I$, and the solver collects the bonus $W'$ for free even when $x_u = 1$! Remember the rule: **an $\infty$-edge $A \xrightarrow{\infty} B$ must always lie on a directed path from $S$ to $T$** ($S \to \dots \to A \xrightarrow{\infty} B \to \dots \to T$); an $\infty$-edge pointing backward from a $T$-hub to a vertex $u$ can never sit on an $S$-$T$ simple path unless $w_I$ has an incoming edge from $S$.

---

## Iteration 14: Rescuing Supermodular Costs ($A + D > B + C$) via Bipartite Variable Flipping (`二部グラフの片側反転` / `反転燃やす埋める`)

### 14.1 Step 1: The Non-Graph Diagnostic Signal (Recognition)

What happens when we write down the $2 \times 2$ penalty matrix $\Theta_{ij} = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ for a problem and discover that **it violates Theorem 13.1**:

$$A + D > B + C \qquad (\text{Strict Supermodularity})?$$

When does $A + D > B + C$ arise in competitive programming? Whenever two variables $x_i, x_j$ are **penalized for agreeing ($x_i = x_j$)** or **rewarded for disagreeing ($x_i \neq x_j$)**, or when a cross-class interaction rewards a single specific corner such as $(x_i = 0, y_j = 0)$:

1. **Mutual Exclusion / Independent Set Constraints ($x_i + x_j \le 1$)**:
   "We cannot select both $i$ and $j$."
   Here $(x_i = 1, x_j = 1)$ costs $D = \infty$, while $A = B = C = 0$. Thus $A + D = \infty > 0 = B + C$!
2. **Mandatory Coverage / Vertex Cover Constraints ($x_i + x_j \ge 1$)**:
   "We must select at least one of $i$ and $j$."
   Here $(x_i = 0, x_j = 0)$ costs $A = \infty$, while $B = C = D = 0$. Again $A + D = \infty > 0 = B + C$!
3. **Antiferromagnetic / Zebra Boundary Rewards (`ABC 193 F — Zebraness`)**:
   "We gain $+1$ whenever adjacent cells $i$ and $j$ are painted **opposite** colors ($x_i \neq x_j$)."
   In loss terms, agreeing states $(0, 0)$ and $(1, 1)$ lose $A = 1, D = 1$, while disagreeing states $(0, 1)$ and $(1, 0)$ lose $B = 0, C = 0$. Thus $A + D = 2 > 0 = B + C$!
4. **Same-State Corner Rewards Across Two Families (`AGC 038 F — Two Permutations`)**:
   "We gain $+1$ if variable $x_i$ from Family 1 and variable $y_j$ from Family 2 are both $0$ ($(x_i, y_j) = (0, 0)$)."
   In loss terms, $A = 0$ (no loss at $(0,0)$), while $B = C = D = 1$ (loss $1$ everywhere else). Wait: $A + D = 0 + 1 = 1$, while $B + C = 1 + 1 = 2$? Hold on! At $(0, 0)$ the reward is $+1$, so the loss is $0$ at $(0, 0)$ and $1$ at $(0,1), (1,0), (1,1)$? Wait: if $A = 0$ and $B = C = D = 1$, then $A + D = 1 \le 2 = B + C$? NO! Look at $(0, 0)$: if $(0,0)$ gets reward $+1$, then $A = 0, B = 1, C = 1, D = 1$ has $A + D = 1 < 2 = B + C$, which IS submodular! When is it supermodular? When $(0, 1)$ or $(1, 0)$ is the rewarded state ($B = 0$ and $A = C = D = 1 \implies A + D = 2 > 1 = B + C$), OR when **both** $(0, 0)$ and $(1, 1)$ are rewarded unevenly, OR when $(x_i = 0 \land y_j = 1)$ is rewarded! We will examine the exact 5 cases of `AGC 038 F` in Iteration 15!

#### Why Supermodular Minimization Is NP-Hard on General Graphs

By Theorem 13.1, no non-negative directed flow network can directly represent a pair $(i, j)$ with $A + D > B + C$. Indeed, if we could minimize $\sum_{(i,j) \in E} \Theta_{ij}(x_i, x_j)$ with $A = D = 1, B = C = 0$ on an arbitrary graph $G = (V, E)$, we would be minimizing the number of monochromatic edges—which is equivalent to **Maximum Cut** (NP-hard)! Similarly, minimizing $\sum \infty \cdot x_i x_j - \sum w_i x_i$ on a general graph is **Maximum Weight Independent Set** (NP-hard)!

#### The Bipartite Rescue Signal

Whenever $A + D > B + C$ appears, immediately inspect the **Supermodular Interaction Graph** $G_{\text{sup}} = (V, E_{\text{sup}})$, whose edges are the pairs $(i, j)$ satisfying $A_{ij} + D_{ij} > B_{ij} + C_{ij}$.
- If $G_{\text{sup}}$ is **bipartite** ($V = L \sqcup R$ with all supermodular edges crossing between $L$ and $R$, and all edges internal to $L$ or internal to $R$ being submodular), the problem can be **completely rescued into a standard polynomial-time Minimum Cut**!

---

### 14.2 Step 2: Intermediate Algebraic Representation — The Bipartite Variable Inversion Theorem

#### Theorem 14.1 (Bipartite Variable Inversion / `二部グラフの片側反転`)

Let $V = L \sqcup R$ be a bipartition of the variable set $V$. Define the **bipartite-flipped binary variables** $\tilde{x} \in \{0, 1\}^V$ by keeping variables in $L$ unchanged and complementing variables in $R$:

$$\tilde{x}_i = x_i \quad (\forall i \in L), \qquad \tilde{x}_j = 1 - x_j \quad (\forall j \in R).$$

Geometrically, for vertices $i \in L$, $\tilde{x}_i = 1$ still means $i \in V_S$ and $\tilde{x}_i = 0$ means $i \in V_T$; whereas for vertices $j \in R$, the meaning of $V_S$ and $V_T$ is **inverted**:
- $j \in V_S \iff \tilde{x}_j = 1 \iff x_j = 0$,
- $j \in V_T \iff \tilde{x}_j = 0 \iff x_j = 1$.

Under the substitution $x_j = 1 - \tilde{x}_j$ ($\forall j \in R$), every term in the pseudo-Boolean objective $E(x)$ transforms as follows:

1. **Cross-Bipartition Pairwise Terms ($i \in L, j \in R$)**:
   Substituting $x_i = \tilde{x}_i$ and $x_j = 1 - \tilde{x}_j$ into $\Theta_{ij}(x_i, x_j) = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ **swaps the two columns** of the $2 \times 2$ matrix:
   $$\tilde{\Theta}_{ij}(\tilde{x}_i, \tilde{x}_j) := \Theta_{ij}(\tilde{x}_i, 1 - \tilde{x}_j) = \begin{array}{c|cc}
   \tilde{x}_i \setminus \tilde{x}_j & \tilde{x}_j = 0 \;(x_j=1) & \tilde{x}_j = 1 \;(x_j=0) \\
   \hline
   \tilde{x}_i = 0 \;(x_i=0) & B & A \\
   \tilde{x}_i = 1 \;(x_i=1) & D & C
   \end{array} = \begin{pmatrix} B & A \\ D & C \end{pmatrix} =: \begin{pmatrix} \tilde{A} & \tilde{B} \\ \tilde{C} & \tilde{D} \end{pmatrix}.$$
   Consequently, the submodularity condition in the flipped variables $(\tilde{x}_i, \tilde{x}_j)$ becomes:
   $$\boxed{\tilde{A} + \tilde{D} \le \tilde{B} + \tilde{C} \quad \Longleftrightarrow \quad B + C \le A + D!}$$
   **Every supermodular cross-edge ($A + D \ge B + C$) is transformed into a submodular cut edge ($\tilde{A} + \tilde{D} \le \tilde{B} + \tilde{C}$) with excess $\tilde{\Delta} = (A + D) - (B + C) \ge 0$!**

2. **Same-Side Pairwise Terms ($j, j' \in R$)**:
   If both $j, j' \in R$, substituting $x_j = 1 - \tilde{x}_j$ and $x_{j'} = 1 - \tilde{x}_{j'}$ swaps **both** the rows and the columns:
   $$\tilde{\Theta}_{jj'}(\tilde{x}_j, \tilde{x}_{j'}) = \Theta_{jj'}(1 - \tilde{x}_j, 1 - \tilde{x}_{j'}) = \begin{pmatrix} D & C \\ B & A \end{pmatrix},$$
   which preserves the sum of the diagonals: $\tilde{A} + \tilde{D} = D + A$ and $\tilde{B} + \tilde{C} = C + B$. Thus submodular edges within $R \times R$ (and trivially within $L \times L$) remain submodular!

3. **Unary Terms on $R$ ($j \in R$)**:
   A unary penalty $p_j x_j + q_j(1 - x_j)$ becomes:
   $$p_j(1 - \tilde{x}_j) + q_j \tilde{x}_j,$$
   so the capacities of $S \to j$ and $j \to T$ simply **swap** ($S \xrightarrow{p_j} j$ and $j \xrightarrow{q_j} T$)!

---

### 14.3 Step 3: Reverse-Engineering Scratchpad — Instant Dictionary of Flipped Gadgets

With Theorem 14.1 in hand, we never need to memorize "flipped graph rules". Whenever $i \in L$ and $j \in R$ (with $\tilde{x}_i = x_i$ and $\tilde{x}_j = 1 - x_j$), we simply substitute $x_j = 1 - \tilde{x}_j$ directly into the algebraic polynomial! Look how effortlessly the four classic conflict/agreement rules compile:

| English Rule Between $i \in L$ and $j \in R$ | Original Monomial in $(x_i, x_j)$ | Substitute $x_i = \tilde{x}_i,\, x_j = 1 - \tilde{x}_j$ | Exact Directed Cut Edge in $(\tilde{x}_i, \tilde{x}_j)$ |
| :--- | :---: | :---: | :---: |
| **Mutual Exclusion** ($x_i = 1 \land x_j = 1$ costs $c$) | $c \cdot x_i x_j$ | $c \cdot \tilde{x}_i (1 - \tilde{x}_j)$ | $i \xrightarrow{\; c \;} j$ |
| **Both-Zero Penalty** ($x_i = 0 \land x_j = 0$ costs $c$) | $c \cdot (1 - x_i)(1 - x_j)$ | $c \cdot (1 - \tilde{x}_i) \tilde{x}_j = c \cdot \tilde{x}_j(1 - \tilde{x}_i)$ | $j \xrightarrow{\; c \;} i$ |
| **Same-State Penalty** ($x_i = x_j$ costs $c$) | $c \big(x_i x_j + (1-x_i)(1-x_j)\big)$ | $c \big(\tilde{x}_i(1 - \tilde{x}_j) + \tilde{x}_j(1 - \tilde{x}_i)\big)$ | $i \stackrel{\; c \;}{\longleftrightarrow} j$ (both ways) |
| **Implication** ($x_i = 1 \implies x_j = 1$, cost $\infty$) | $\infty \cdot x_i(1 - x_j)$ | $\infty \cdot \tilde{x}_i \tilde{x}_j \quad (\text{Supermodular in }\tilde{x}\text{!})$ | *(Cannot cross $L \times R$; must stay in $L \times L$ or $R \times R$!)* |

Look at the fourth row of that table—it reveals a crucial structural insight:
- Flipping $j \in R$ turns **same-state penalties** ($x_i x_j$ and $(1 - x_i)(1 - x_j)$) into **valid cut edges** ($\tilde{x}_i(1 - \tilde{x}_j)$ and $\tilde{x}_j(1 - \tilde{x}_i)$),
- AND simultaneously turns **different-state penalties** ($x_i(1 - x_j)$) into **invalid supermodular products** ($\tilde{x}_i \tilde{x}_j$)!
- Therefore, for a problem to be compilable via variable flipping, the graph of all interactions must admit a 2-coloring (or signed-graph balance) $\sigma: V \to \{0, 1\}$ such that:
  - Every **supermodular** pair $(u, v)$ ($A + D > B + C$) has $\sigma(u) \neq \sigma(v)$ (bipartite / opposite sides), AND
  - Every **submodular** pair $(u, v)$ ($A + D < B + C$) has $\sigma(u) = \sigma(v)$ (same side)!

#### Three Canonical Bipartitions in Competitive Programming

1. **Chessboard Grid Bipartition (`(r + c) mod 2` — `[网络流24题] 方格取数`, `ABC 193 F — Zebraness`)**:
   On any 2D grid where interactions occur between 4-adjacent cells $(r, c)$ and $(r', c')$ with $|r - r'| + |c - c'| = 1$, define:
   $$L = \{(r, c) : (r + c) \equiv 0 \pmod 2\}, \qquad R = \{(r, c) : (r + c) \equiv 1 \pmod 2\}.$$
   Every 4-neighbor interaction crosses between $L$ and $R$, whereas every diagonal or distance-2 interaction $(r \pm 1, c \pm 1)$ stays within $L \times L$ or $R \times R$!
   - *Bonus insight*: This means a 2D grid problem can simultaneously have **supermodular** penalties between 4-adjacent neighbors (e.g., cannot pick two orthogonal neighbors) AND **submodular** penalties between diagonal/distance-2 neighbors (e.g., picking $(r, c)$ forces picking $(r+1, c+1)$)!

2. **Two-Family Entity Bipartition (`AGC 038 F`, `ARC 142 E`, Row-vs-Column Operations)**:
   When the problem has two distinct classes of variables—such as **Row operations $L = \{r_1, \dots, r_H\}$** vs. **Column operations $R = \{c_1, \dots, c_W\}$**, or **Cycles of permutation $P$** vs. **Cycles of permutation $Q$**—where every cell $(r, c)$ or index $i$ couples one variable in $L$ with one variable in $R$, the interaction graph is automatically bipartite!

3. **Arithmetic Parity / Bitmask Popcount Bipartition (`CF 808 F`, `ARC 107 D`, Prime-Sum Conflicts)**:
   - If two numbers $a_i, a_j$ conflict whenever $a_i + a_j$ is an odd prime $p > 2$, then $a_i$ and $a_j$ must have opposite parity ($a_i \not\equiv a_j \pmod 2$), so $L = \{\text{even}\}, R = \{\text{odd}\}$ is a valid bipartition!
   - If two bitmasks $m_i, m_j$ conflict whenever they differ in exactly one bit ($m_i \oplus m_j = 2^k$), then $\text{popcount}(m_i) \not\equiv \text{popcount}(m_j) \pmod 2$, so $L = \{\text{even popcount}\}, R = \{\text{odd popcount}\}$ is a valid bipartition!

---

### 14.4 Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Worked Toy Trace (`[网络流24题] 方格取数` on a $2 \times 2$ Grid)

**Problem**: Given a $2 \times 2$ grid of positive integers:
$$\begin{pmatrix} w_{1,1} & w_{1,2} \\ w_{2,1} & w_{2,2} \end{pmatrix} = \begin{pmatrix} 10 & 8 \\ 7 & 12 \end{pmatrix},$$
select a subset of cells with no two 4-adjacent cells both selected, maximizing the sum of selected cells.

1. **Step 1 (Algebraic Model in Original Variables $x_{r,c} \in \{0, 1\}$)**:
   Optimistic baseline: $R_{\max} = 10 + 8 + 7 + 12 = 37$.
   Loss polynomial in $x_{r,c}$ ($x_{r,c} = 1 \iff$ cell selected):
   $$E(x) = 10(1 - x_{1,1}) + 8(1 - x_{1,2}) + 7(1 - x_{2,1}) + 12(1 - x_{2,2}) + \infty(x_{1,1}x_{1,2} + x_{1,1}x_{2,1} + x_{2,2}x_{1,2} + x_{2,2}x_{2,1}).$$
2. **Step 2 (Bipartite Variable Flip on Odd-Parity Cells)**:
   Partition $L = \{(1,1), (2,2)\}$ (even $r+c$) and $R = \{(1,2), (2,1)\}$ (odd $r+c$).
   Set $\tilde{x}_{1,1} = x_{1,1},\; \tilde{x}_{2,2} = x_{2,2}$ and $\tilde{x}_{1,2} = 1 - x_{1,2},\; \tilde{x}_{2,1} = 1 - x_{2,1}$ (so $1 - x_{1,2} = \tilde{x}_{1,2}$ and $x_{1,2} = 1 - \tilde{x}_{1,2}$):
   $$E(\tilde{x}) = \underbrace{10(1 - \tilde{x}_{1,1})}_{S \xrightarrow{10} (1,1)} + \underbrace{12(1 - \tilde{x}_{2,2})}_{S \xrightarrow{12} (2,2)} + \underbrace{8 \tilde{x}_{1,2}}_{(1,2) \xrightarrow{8} T} + \underbrace{7 \tilde{x}_{2,1}}_{(2,1) \xrightarrow{7} T} + \infty \Big[ \tilde{x}_{1,1}(1 - \tilde{x}_{1,2}) + \tilde{x}_{1,1}(1 - \tilde{x}_{2,1}) + \tilde{x}_{2,2}(1 - \tilde{x}_{1,2}) + \tilde{x}_{2,2}(1 - \tilde{x}_{2,1}) \Big].$$
3. **Step 3 (Read Off the Flow Network & Min-Cut)**:
   - Edges from $S$: $S \xrightarrow{10} (1,1)$ and $S \xrightarrow{12} (2,2)$.
   - Edges to $T$: $(1,2) \xrightarrow{8} T$ and $(2,1) \xrightarrow{7} T$.
   - Infinite cross-edges from $L$ to $R$: $(1,1) \xrightarrow{\infty} (1,2),\; (1,1) \xrightarrow{\infty} (2,1),\; (2,2) \xrightarrow{\infty} (1,2),\; (2,2) \xrightarrow{\infty} (2,1)$.
   - Minimum Cut: Compare cutting $L$-edges ($10 + 12 = 22$) vs. cutting $R$-edges ($8 + 7 = 15$). The min-cut is $15$, achieved by $\tilde{x}_{1,1} = \tilde{x}_{2,2} = \tilde{x}_{1,2} = \tilde{x}_{2,1} = 1$ (all four vertices in $V_S$).
   - **Recovering Original Variables**:
     - For $(1,1), (2,2) \in L$: $x_{1,1} = \tilde{x}_{1,1} = 1$, $x_{2,2} = \tilde{x}_{2,2} = 1$ (Selected!).
     - For $(1,2), (2,1) \in R$: $x_{1,2} = 1 - \tilde{x}_{1,2} = 0$, $x_{2,1} = 1 - \tilde{x}_{2,1} = 0$ (Not selected!).
   - Maximum weight: $37 - 15 = 22 = 10 + 12$.

#### Broken Gadget Counterexample: The Odd Cycle Frustration Barrier

What happens if we try to apply Bipartite Variable Inversion when the supermodular conflict graph contains an **odd cycle**—for example, a triangle on $\{1, 2, 3\}$ with mutual exclusion penalty $\infty(x_1 x_2 + x_2 x_3 + x_3 x_1)$?

- Suppose we assign each vertex $i \in \{1, 2, 3\}$ a flip bit $\sigma_i \in \{0, 1\}$, setting $\tilde{x}_i = x_i$ if $\sigma_i = 0$ and $\tilde{x}_i = 1 - x_i$ if $\sigma_i = 1$.
- By the **Pigeonhole Principle**, among the three bits $\sigma_1, \sigma_2, \sigma_3 \in \{0, 1\}$, at least two must be equal! Without loss of generality, suppose $\sigma_1 = \sigma_2$.
  - If $\sigma_1 = \sigma_2 = 0$: the term $\infty x_1 x_2$ remains $\infty \tilde{x}_1 \tilde{x}_2$, which has $\tilde{A} + \tilde{D} = 0 + \infty = \infty > 0 = \tilde{B} + \tilde{C}$ (still supermodular!).
  - If $\sigma_1 = \sigma_2 = 1$: the term $\infty x_1 x_2$ becomes $\infty(1 - \tilde{x}_1)(1 - \tilde{x}_2)$, which has $\tilde{A} + \tilde{D} = \infty + 0 = \infty > 0 = \tilde{B} + \tilde{C}$ (still supermodular!).
- Thus **no variable substitution can make all three edges of a triangle submodular simultaneously**!

> [!NOTE]
> **Theoretical Bridge — What Does the Doubled Bipartite Network Compute on Non-Bipartite Graphs? (Roof Duality / QPBO)**
> In operations research and computer vision (Boros & Hammer 2002; Rother et al. 2007), if a polynomial $E(x)$ is non-submodular on a general graph, one can create **two** vertices per variable ($x_i \in L$ and $\bar{x}_i \in R$) without enforcing $\bar{x}_i = 1 - x_i$, and solve the resulting bipartite min-cut. By the **Nemhauser–Trotter / Roof Duality Theorem**, this doubled min-cut computes the exact **half-integral LP relaxation** $x_i \in \{0, \frac{1}{2}, 1\}$, and displays the **Strong Persistency Property**: every variable where the doubled cut assigns consistent binary values ($x_i = 1 - \bar{x}_i \in \{0, 1\}$) is guaranteed to take that exact value in at least one global integer optimum! In competitive programming, however, whenever a problem requires the exact integer optimum in polynomial time via Min-Cut, the problem setter has guaranteed that the supermodular interaction graph is bipartite (or signed-balanced).


---

## Iteration 15: Deep Case Study — User Benchmark Problem `AGC 038 F — Two Permutations` & Cycle-Pair Bipartite Cut Compilation

We now bring together all four theoretical pillars of Wave 2A (Iterations 11–14) to perform a complete, zero-magic-gadgets derivation of one of the most celebrated non-graph Minimum Cut problems in modern competitive programming: **`AtCoder Grand Contest 038, Problem F — Two Permutations`**.

### Problem Statement (`[AtCoder AGC 038 F — Two Permutations]`)

- **Judge URL**: [https://atcoder.jp/contests/agc038/tasks/agc038_f](https://atcoder.jp/contests/agc038/tasks/agc038_f)
- **Statement**: Snuke has two permutations $P = (P_0, P_1, \dots, P_{N-1})$ and $Q = (Q_0, Q_1, \dots, Q_{N-1})$ of $(0, 1, \dots, N-1)$. He wants to construct two new permutations $A = (A_0, \dots, A_{N-1})$ and $B = (B_0, \dots, B_{N-1})$ of $(0, 1, \dots, N-1)$ satisfying:
  - For every $i \in \{0, \dots, N-1\}$, $A_i \in \{i, P_i\}$.
  - For every $i \in \{0, \dots, N-1\}$, $B_i \in \{i, Q_i\}$.
  The **distance** between permutations $A$ and $B$ is defined as the number of indices $i \in \{0, \dots, N-1\}$ such that $A_i \neq B_i$. Find the **maximum possible distance** between $A$ and $B$.
- **Constraints**: $1 \le N \le 10^5$, $P$ and $Q$ are permutations of $(0, 1, \dots, N-1)$. Time Limit: 8.0 seconds.

---

### 15.1 Step 1: The Non-Graph Diagnostic Signal (Recognition & Cycle Rigidity)

At first glance, the problem statement does not mention graphs, flows, or cuts anywhere—only two permutations $P$ and $Q$. Why can we not simply choose $(A_i, B_i) \in \{i, P_i\} \times \{i, Q_i\}$ greedily for each index $i$ to make $A_i \neq B_i$?

Because **$A$ and $B$ must themselves be valid permutations (bijections) of $\{0, 1, \dots, N-1\}$**!

Let us analyze what the permutation constraint forces on $A$. Decompose the permutation $P$ into its disjoint directed cycles $C_1, C_2, \dots, C_k$, where each cycle $C = (v_0 \to v_1 \to \dots \to v_{\ell-1} \to v_0)$ satisfies $P_{v_r} = v_{(r+1) \bmod \ell}$.

#### Lemma 15.1 (The Cycle Rigidity Lemma)

A function $A: \{0, \dots, N-1\} \to \{0, \dots, N-1\}$ satisfying $A_i \in \{i, P_i\}$ for all $i$ is a valid permutation **if and only if**, on every cycle $C$ of $P$, **either**:
1. **Identity State ($x_C = 0$)**: $A_i = i$ for **all** $i \in C$, **OR**
2. **Shifted State ($x_C = 1$)**: $A_i = P_i$ for **all** $i \in C$.

*(Proof)*: Since $i \in C$ and $P_i \in C$, the image $A(C)$ is a subset of $C$, and because $A$ is a bijection on a finite set, $A|_C: C \to C$ must be a bijection on each cycle $C$ independently. For a cycle $C = (v_0 \to v_1 \to \dots \to v_{\ell-1} \to v_0)$ of length $\ell \ge 2$, suppose $A_{v_r} = v_r$ for some $v_r \in C$. Since the value $v_r$ is now already taken by $A_{v_r}$, its cycle predecessor $v_{r-1}$ (whose only options are $\{v_{r-1}, P_{v_{r-1}}\} = \{v_{r-1}, v_r\}$) cannot choose $v_r$ and is forced to choose $A_{v_{r-1}} = v_{r-1}$. By induction around the cycle, $A_v = v$ for all $v \in C$. Conversely, if $A_{v_r} = P_{v_r} = v_{r+1}$, then $v_{r+1}$ is taken, forcing $A_{v_{r+1}} = P_{v_{r+1}}$, and by induction $A_v = P_v$ for all $v \in C$. (For a fixed point $\ell = 1$ with $P_i = i$, both states yield $A_i = i$.) $\blacksquare$

By the exact same lemma applied to $Q$ (decomposed into disjoint cycles $D_1, D_2, \dots, D_m$), each cycle $D$ of $Q$ has a single binary decision variable $y_D \in \{0, 1\}$:
- **Identity State ($y_D = 0$)**: $B_i = i$ for all $i \in D$.
- **Shifted State ($y_D = 1$)**: $B_i = Q_i$ for all $i \in D$.

#### The Recognition Moment
Look at what Lemma 15.1 has revealed:
1. **Hidden Binary Variables**: The actual decision variables are not the $N$ array indices, but the **$P$-cycles $x_C \in \{0, 1\}$** and the **$Q$-cycles $y_D \in \{0, 1\}$**!
2. **Pairwise Bipartite Coupling**: Every index $i \in \{0, \dots, N-1\}$ belongs to **one** $P$-cycle $C(i)$ and **one** $Q$-cycle $D(i)$. Thus each index $i$ creates a pairwise interaction between $x_{C(i)}$ and $y_{D(i)}$!
3. **Why DP Fails & Why Dinic Succeeds at $N = 10^5$**: The bipartite multigraph between $P$-cycles and $Q$-cycles can have arbitrary topology (arbitrary cycles and high treewidth), so DP is impossible. However, the flow network will have at most $2N + 2$ vertices and $2N$ **unit-capacity** edges! On a unit-capacity network (or a bipartite network where every vertex has unit capacity on one side), Dinic's algorithm runs in $O(E\sqrt{V}) = O(N\sqrt{N})$ worst-case time (and practically $O(N)$ on cycle graphs), easily passing well within the 8-second limit!

---

### 15.2 Step 2: Intermediate Algebraic Representation — The 5 Cases & Why Direct Cut Fails

We want to **maximize** the distance $\sum_{i=0}^{N-1} [A_i \neq B_i]$.
Applying the Optimistic Baseline Principle (Section 11.3) with maximum possible distance $R_{\max} = N$ (every index $i$ having $A_i \neq B_i$):

$$\max_{x, y} \sum_{i=0}^{N-1} [A_i \neq B_i] = N - \min_{x, y} \sum_{i=0}^{N-1} \underbrace{[A_i = B_i]}_{\text{Penalty } \Theta_i(x_{C(i)}, y_{D(i)})}.$$

That is, **each index $i$ incurs a penalty of $+1$ whenever $A_i = B_i$**!

Let $c = C(i)$ be the $P$-cycle containing $i$, and $d = D(i)$ be the $Q$-cycle containing $i$. Recall the four possible outcome pairs $(A_i, B_i)$ under $(x_c, y_d) \in \{0, 1\}^2$:

$$\begin{array}{c|cc}
x_c \setminus y_d & y_d = 0 \;(B_i = i) & y_d = 1 \;(B_i = Q_i) \\
\hline
x_c = 0 \;(A_i = i) & (i,\, i) & (i,\, Q_i) \\
x_c = 1 \;(A_i = P_i) & (P_i,\, i) & (P_i,\, Q_i)
\end{array}$$

Depending on whether $P_i = i$, $Q_i = i$, and $P_i = Q_i$, there are **five mutually exclusive cases** for index $i$. Let us write down the $2 \times 2$ Penalty Matrix $\Theta_i(x_c, y_d) = [A_i = B_i]$ for each case and test Theorem 13.1 ($A + D \le B + C$):

1. **Case 1 ($P_i = i$ and $Q_i = i$)**:
   In all four states, $A_i = i$ and $B_i = i$, so $A_i = B_i$ **always** holds!
   $$\Theta_i(x_c, y_d) = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = 1 \qquad (\text{Unavoidable constant penalty } +1).$$

2. **Case 2 ($P_i = i$ and $Q_i \neq i$)**:
   Here $A_i = i$ always, while $B_i = i$ when $y_d = 0$ and $B_i = Q_i \neq i$ when $y_d = 1$. Thus $A_i = B_i \iff y_d = 0$:
   $$\Theta_i(x_c, y_d) = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} = 1 - y_d \qquad (\text{Pure unary penalty on } y_d).$$

3. **Case 3 ($P_i \neq i$ and $Q_i = i$)**:
   Here $B_i = i$ always, while $A_i = i$ when $x_c = 0$ and $A_i = P_i \neq i$ when $x_c = 1$. Thus $A_i = B_i \iff x_c = 0$:
   $$\Theta_i(x_c, y_d) = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} = 1 - x_c \qquad (\text{Pure unary penalty on } x_c).$$

4. **Case 4 ($P_i \neq i$, $Q_i \neq i$, and $P_i \neq Q_i$)**:
   Since $i, P_i, Q_i$ are three **distinct** values:
   - At $(0, 0)$: $(A_i, B_i) = (i, i) \implies A_i = B_i$ (**Penalty $1$**).
   - At $(0, 1)$: $(A_i, B_i) = (i, Q_i) \implies A_i \neq B_i$ (Penalty $0$).
   - At $(1, 0)$: $(A_i, B_i) = (P_i, i) \implies A_i \neq B_i$ (Penalty $0$).
   - At $(1, 1)$: $(A_i, B_i) = (P_i, Q_i) \implies A_i \neq B_i$ (Penalty $0$).
   Thus the $2 \times 2$ penalty matrix is:
   $$\Theta_i(x_c, y_d) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = (1 - x_c)(1 - y_d).$$
   **Submodularity Check**:
   $$A + D = 1 + 0 = 1 \;>\; 0 = 0 + 0 = B + C \qquad (\textbf{STRICTLY SUPERMODULAR — Direct Cut Fails!})$$

5. **Case 5 ($P_i \neq i$, $Q_i \neq i$, and $P_i = Q_i$)**:
   Since $P_i = Q_i \neq i$:
   - At $(0, 0)$: $(A_i, B_i) = (i, i) \implies A_i = B_i$ (**Penalty $1$**).
   - At $(0, 1)$: $(A_i, B_i) = (i, Q_i) \implies A_i \neq B_i$ (Penalty $0$).
   - At $(1, 0)$: $(A_i, B_i) = (P_i, i) \implies A_i \neq B_i$ (Penalty $0$).
   - At $(1, 1)$: $(A_i, B_i) = (P_i, Q_i) = (P_i, P_i) \implies A_i = B_i$ (**Penalty $1$**).
   Thus the $2 \times 2$ penalty matrix is:
   $$\Theta_i(x_c, y_d) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = (1 - x_c)(1 - y_d) + x_c y_d.$$
   **Submodularity Check**:
   $$A + D = 1 + 1 = 2 \;>\; 0 = 0 + 0 = B + C \qquad (\textbf{STRICTLY SUPERMODULAR — Direct Cut Fails!})$$

Look at why a direct cut in $(x_c, y_d)$ fails: in Cases 4 and 5, collision $A_i = B_i$ occurs when $x_c$ and $y_d$ **agree** ($(0, 0)$ and $(1, 1)$), making the penalty matrices **supermodular** ($A + D > B + C$)!

---

### 15.3 Step 3: Reverse-Engineering Scratchpad — The Bipartite Variable Flip Rescue

How do we rescue the supermodular penalty matrices in Cases 4 and 5?
Observe the **Supermodular Interaction Graph**:
- The left vertex set $L$ is the set of all **$P$-cycles** $\{C_1, \dots, C_k\}$.
- The right vertex set $R$ is the set of all **$Q$-cycles** $\{D_1, \dots, D_m\}$.
- Every index $i \in \{0, \dots, N-1\}$ creates an interaction **strictly between $c = C(i) \in L$ and $d = D(i) \in R$**! There are **zero** edges within $L \times L$ and **zero** edges within $R \times R$!

Therefore, the interaction graph is **100% bipartite**! By **Theorem 14.1 (Bipartite Variable Inversion)**, we flip all right-shore variables ($Q$-cycles $d \in R$) by defining:

$$z_d := 1 - y_d \in \{0, 1\} \qquad \Longleftrightarrow \qquad y_d = 1 - z_d, \quad 1 - y_d = z_d.$$

In terms of our canonical cut convention ($V_S \iff 1$, $V_T \iff 0$):
- For a **$P$-cycle $c \in L$**:
  - $c \in V_S \iff x_c = 1 \iff A_i = P_i$ (Shift $P$),
  - $c \in V_T \iff x_c = 0 \iff A_i = i$ (Identity $P$).
- For a **$Q$-cycle $d \in R$** *(Flipped!)*:
  - $d \in V_S \iff z_d = 1 \iff y_d = 0 \iff B_i = i$ (Identity $Q$),
  - $d \in V_T \iff z_d = 0 \iff y_d = 1 \iff B_i = Q_i$ (Shift $Q$).

Now substitute $1 - y_d = z_d$ and $y_d = 1 - z_d$ into all five cases! Every single supermodular product transforms into a pure directed cut monomial:

| Case | Condition on $P_i, Q_i, i$ | Penalty in $(x_c, y_d)$ | Substitute $1 - y_d = z_d$ | Exact Cut Edge in Network $\mathcal{N}$ |
| :---: | :--- | :---: | :---: | :--- |
| **1** | $P_i = i \;\land\; Q_i = i$ | $1$ | $1$ | Add $+1$ to unavoidable base loss $C_0$ |
| **2** | $P_i = i \;\land\; Q_i \neq i$ | $1 - y_d$ | $z_d = z_d(1 - x_T)$ | $D(i) \xrightarrow{\; 1 \;} T$ |
| **3** | $P_i \neq i \;\land\; Q_i = i$ | $1 - x_c$ | $1 - x_c = x_S(1 - x_c)$ | $S \xrightarrow{\; 1 \;} C(i)$ |
| **4** | $P_i \neq i,\; Q_i \neq i,\; P_i \neq Q_i$ | $(1 - x_c)(1 - y_d)$ | $z_d(1 - x_c)$ | $D(i) \xrightarrow{\; 1 \;} C(i)$ |
| **5** | $P_i = Q_i \neq i$ | $(1 - x_c)(1 - y_d) + x_c y_d$ | $z_d(1 - x_c) + x_c(1 - z_d)$ | $D(i) \xrightarrow{\; 1 \;} C(i)$ **and** $C(i) \xrightarrow{\; 1 \;} D(i)$ |

Look at that table:
- There are **zero** negative numbers, **zero** auxiliary hub nodes, and **zero** unary cancellation shifts needed!
- Every index $i \in \{0, \dots, N-1\}$ simply drops $0, 1,$ or $2$ unit-capacity directed edges into the graph, and the final answer is:
  $$\boxed{\text{MaxDistance}(A, B) = N - C_0 - \text{MinCut}(S, T).}$$

---

### 15.4 Step 4: Hand-Checkable Toy Trace on AtCoder Sample 1 ($N = 4$)

Let us trace **Sample 1** of `AGC 038 F` by hand to verify every step of our compilation:
- $N = 4$
- $P = (2, 1, 3, 0)$
- $Q = (0, 2, 3, 1)$

1. **Cycle Decomposition**:
   - Cycles of $P$:
     - $C_0 = (0 \to 2 \to 3 \to 0)$ (length $3$, variable $x_{C_0} \in \{0, 1\}$),
     - $C_1 = (1 \to 1)$ (fixed point, length $1$, variable $x_{C_1} \in \{0, 1\}$).
   - Cycles of $Q$:
     - $D_0 = (0 \to 0)$ (fixed point, length $1$, flipped variable $z_{D_0} \in \{0, 1\}$),
     - $D_1 = (1 \to 2 \to 3 \to 1)$ (length $3$, flipped variable $z_{D_1} \in \{0, 1\}$).

2. **Index-by-Index Compilation ($i = 0, 1, 2, 3$)**:
   - **$i = 0$**: $P_0 = 2 \neq 0$, $Q_0 = 0 = 0$.
     Falls into **Case 3** ($P_i \neq i \land Q_i = i$).
     Penalty: $1 - x_{C_0} \implies$ add edge **$S \xrightarrow{1} C_0$**.
   - **$i = 1$**: $P_1 = 1 = 1$, $Q_1 = 2 \neq 1$.
     Falls into **Case 2** ($P_i = i \land Q_i \neq i$).
     Penalty: $z_{D_1} \implies$ add edge **$D_1 \xrightarrow{1} T$**.
   - **$i = 2$**: $P_2 = 3 \neq 2$, $Q_2 = 3 \neq 2$, and $P_2 = Q_2 = 3$.
     Falls into **Case 5** ($P_i = Q_i \neq i$).
     Penalty: $z_{D_1}(1 - x_{C_0}) + x_{C_0}(1 - z_{D_1}) \implies$ add edges **$D_1 \xrightarrow{1} C_0$** and **$C_0 \xrightarrow{1} D_1$**.
   - **$i = 3$**: $P_3 = 0 \neq 3$, $Q_3 = 1 \neq 3$, and $P_3 \neq Q_3$.
     Falls into **Case 4** ($P_i \neq i, Q_i \neq i, P_i \neq Q_i$).
     Penalty: $z_{D_1}(1 - x_{C_0}) \implies$ add edge **$D_1 \xrightarrow{1} C_0$**.

3. **Resulting Network & Minimum Cut**:
   Combining parallel edges ($D_1 \to C_0$ appears in $i=2$ and $i=3$), the entire network on $\{S, C_0, D_1, T\}$ has:
   - $S \xrightarrow{\; 1 \;} C_0$
   - $C_0 \xrightarrow{\; 1 \;} D_1$
   - $D_1 \xrightarrow{\; 2 \;} C_0$
   - $D_1 \xrightarrow{\; 1 \;} T$
   - Base loss $C_0 = 0$.

   What is the maximum flow from $S$ to $T$?
   There is a single augmenting path $S \xrightarrow{1} C_0 \xrightarrow{1} D_1 \xrightarrow{1} T$ of capacity **$1$**!
   Hence $\text{MinCut}(S, T) = 1$, achieved for example by cutting $S \xrightarrow{1} C_0$ (setting $x_{C_0} = 0, z_{D_1} = 0$).
   - **Recovering $A$ and $B$ from $(x_{C_0} = 0, z_{D_1} = 0)$**:
     - $x_{C_0} = 0 \implies C_0$ uses Identity: $A = (0, 1, 2, 3)$.
     - $z_{D_1} = 0 \implies y_{D_1} = 1 - z_{D_1} = 1 \implies D_1$ uses Shift $Q$: $B = (0, 2, 3, 1)$.
   - **Check Distance**:
     Comparing $A = (0, 1, 2, 3)$ and $B = (0, 2, 3, 1)$, they differ at $i \in \{1, 2, 3\}$ ($3$ positions) and agree only at $i = 0$.
     Our formula gives:
     $$\text{Ans} = N - C_0 - \text{MinCut}(S, T) = 4 - 0 - 1 = 3. \quad \checkmark$$

---

## Master Recognition & Compilation Decision Table (Wave 2A Synthesis)

Before moving to the 22 curated problems, use this master reference table to compile any binary decision pattern into its exact cut gadget under our canonical convention ($x_S = 1, x_T = 0$; $x_i = 1 \iff i \in V_S$, $x_i = 0 \iff i \in V_T$).

| Modelling Pattern / English Clause | Algebraic Loss Term $E(x)$ | Submodular Check | Auxiliary Nodes | Exact Directed Edges Compiled |
| :--- | :--- | :---: | :---: | :--- |
| **Unary Penalty on State $1$** | $p_i x_i \;(p_i \ge 0)$ | Always | $0$ | $i \xrightarrow{\; p_i \;} T$ |
| **Unary Penalty on State $0$** | $q_i(1 - x_i) \;(q_i \ge 0)$ | Always | $0$ | $S \xrightarrow{\; q_i \;} i$ |
| **Arbitrary Signed Unary $A_i \bar{x}_i + B_i x_i$** | $m_i + (A_i - m_i)\bar{x}_i + (B_i - m_i)x_i$<br>where $m_i = \min(A_i, B_i)$ | Always | $0$ | Add $m_i$ to base loss $C_0$; add $S \xrightarrow{A_i - B_i} i$ if $A_i > B_i$, else $i \xrightarrow{B_i - A_i} T$ |
| **Hard Prerequisite ($u \implies v$)** | $\infty \cdot x_u(1 - x_v)$ | $A+D = 0 \le \infty$ | $0$ | $u \xrightarrow{\; \infty \;} v$ |
| **Soft Implication Penalty** | $c \cdot x_u(1 - x_v) \;(c \ge 0)$ | $A+D = 0 \le c$ | $0$ | $u \xrightarrow{\; c \;} v$ |
| **Symmetric Disagreement Penalty ($x_u \neq x_v$)** | $c\big(x_u(1-x_v) + x_v(1-x_u)\big)$ | $0 \le 2c$ | $0$ | $u \stackrel{\; c \;}{\longleftrightarrow} v$ (both $u \to v$ and $v \to u$) |
| **General Submodular $2 \times 2$ Matrix $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$** | $A + (C-A)x_u + (D-C)x_v + \Delta \bar{x}_u x_v$<br>where $\Delta = (B+C)-(A+D) \ge 0$ | $A + D \le B + C$ | $0$ | Accumulate $A$ into $C_0$, $(C-A)x_u$, $(D-C)x_v$, and add $v \xrightarrow{\; \Delta \;} u$ |
| **All-1 Synergy Bonus $W \prod_{u \in I} x_u$** | $W(1 - z_I) + \sum_{u \in I} \infty \cdot z_I(1 - x_u)$ | Submodular in $(x, z_I)$ | $1$ hub $z_I$ | Add $W$ to $R_{\max}$; $S \xrightarrow{W} z_I$; $z_I \xrightarrow{\infty} u \;(\forall u \in I)$ |
| **All-0 Synergy Bonus $W' \prod_{u \in I} \bar{x}_u$** | $W' w_I + \sum_{u \in I} \infty \cdot x_u(1 - w_I)$ | Submodular in $(x, w_I)$ | $1$ hub $w_I$ | Add $W'$ to $R_{\max}$; $w_I \xrightarrow{W'} T$; $u \xrightarrow{\infty} w_I \;(\forall u \in I)$ |
| **Bipartite Conflict ($x_i = 1 \land x_j = 1$ costs $c$, $i \in L, j \in R$)** | $c \cdot x_i x_j = c \cdot \tilde{x}_i(1 - \tilde{x}_j)$<br>with $\tilde{x}_j = 1 - x_j$ | Supermodular in $x$;<br>Submodular in $\tilde{x}$ | $0$ | Flip $R$ unary edges ($S \leftrightarrow T$); add $i \xrightarrow{\; c \;} j$ |
| **Bipartite Both-Zero ($x_i = 0 \land x_j = 0$ costs $c$, $i \in L, j \in R$)** | $c \cdot \bar{x}_i \bar{x}_j = c \cdot \tilde{x}_j(1 - \tilde{x}_i)$<br>with $\tilde{x}_j = 1 - x_j$ | Supermodular in $x$;<br>Submodular in $\tilde{x}$ | $0$ | Flip $R$ unary edges ($S \leftrightarrow T$); add $j \xrightarrow{\; c \;} i$ |
| **Bipartite Agreement Penalty ($x_i = x_j$ costs $c$, $i \in L, j \in R$)** | $c(\tilde{x}_i(1-\tilde{x}_j) + \tilde{x}_j(1-\tilde{x}_i))$<br>with $\tilde{x}_j = 1 - x_j$ | Supermodular in $x$;<br>Submodular in $\tilde{x}$ | $0$ | Flip $R$ unary edges ($S \leftrightarrow T$); add $i \stackrel{\; c \;}{\longleftrightarrow} j$ |
| **Sequential Prerequisite Closure with Possible Cycles** | $\infty \cdot x_u(1 - x_v)$ on DAG $V_{\text{valid}}$ | Prune cycles first! | $0$ | Run Kahn's BFS on $G_{\text{prot}}$ to delete all cycle-dependent nodes before building $\mathcal{N}$ |


---

## 4-Tier Curated Problem Bank (Part 1: Stepping Stone & Intermediate — Problems P01 to P11)

Every problem in this curated bank is a non-template modelling problem solved via our **4-Step "Zero Magic Gadgets" Compilation Standard**:
1. **Non-Graph Diagnostic Signal (Recognition)**
2. **Intermediate Algebraic Representation (Pseudo-Boolean Cut Polynomial)**
3. **Reverse-Engineering Scratchpad (Graph Compilation & Complexity)**
4. **Progressive 3-Tier Hints & Failure Mode Warning**

---

### Tier 1: Stepping Stone (Problems P01–P05)

---

#### Problem P01 — `[NOI2006] 最大获利` (Maximum Profit) `[ZH]`

- **Judge URL**: [https://www.luogu.com.cn/problem/P4174](https://www.luogu.com.cn/problem/P4174)
- **Statement**: A telecom company can build $N$ base stations ($1 \le N \le 5000$), where station $i$ costs $P_i \ge 0$ to construct. There are $M$ customer groups ($1 \le M \le 50000$); group $j$ generates revenue $C_j > 0$ if and only if **both** base stations $A_j$ and $B_j$ are constructed. Find the maximum net profit (total revenue minus total construction cost).

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Each station $i$ has a binary choice $x_i \in \{0, 1\}$ (build or not), and each customer group $j$ is earned iff $x_{A_j} = 1 \land x_{B_j} = 1$.
   - Why greedy/DP fail: The pairs $(A_j, B_j)$ form an arbitrary general graph on $N = 5000$ vertices; stations share costs across arbitrarily many overlapping customer groups.
2. **Step 2: Intermediate Algebraic Representation**:
   Introduce binary variable $y_j \in \{0, 1\}$ for serving customer group $j$, with hard prerequisite constraints $y_j = 1 \implies x_{A_j} = 1$ and $y_j = 1 \implies x_{B_j} = 1$.
   $$\begin{aligned}
   \max_{x, y} \left( \sum_{j=1}^M C_j y_j - \sum_{i=1}^N P_i x_i \right)
   &= \sum_{j=1}^M C_j - \min_{x, y} \Bigg( \sum_{j=1}^M C_j (1 - y_j) + \sum_{i=1}^N P_i x_i \\
   &\qquad\qquad\qquad\qquad + \sum_{j=1}^M \infty \cdot y_j(1 - x_{A_j}) + \sum_{j=1}^M \infty \cdot y_j(1 - x_{B_j}) \Bigg).
   \end{aligned}$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Optimistic baseline: $R_{\max} = \sum_{j=1}^M C_j$.
   - For each customer group $j \in \{1, \dots, M\}$: add edge $S \xrightarrow{\; C_j \;} y_j$, and add prerequisite edges $y_j \xrightarrow{\; \infty \;} x_{A_j}$ and $y_j \xrightarrow{\; \infty \;} x_{B_j}$.
   - For each base station $i \in \{1, \dots, N\}$: add edge $x_i \xrightarrow{\; P_i \;} T$.
   - **Alternative Zero-Auxiliary Compilation (`合并点边法`)**: Since each group $j$ involves only $2$ variables $(x_{A_j}, x_{B_j})$, we can also eliminate $y_j$ by writing $C_j(1 - x_{A_j} x_{B_j}) = \frac{C_j}{2}(1 - x_{A_j}) + \frac{C_j}{2}(1 - x_{B_j}) + \frac{C_j}{2}\big(x_{A_j}(1 - x_{B_j}) + x_{B_j}(1 - x_{A_j})\big)$, reducing the vertex count from $N + M + 2 = 55002$ down to **$N + 2 = 5002$**!
   - **Complexity**: $V = N + M + 2$, $E = N + 3M$ (or $V = N + 2, E = 2N + 2M$ with merged edges); Dinic runs in $< 50\text{ ms}$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Treat both base stations and customer groups as binary decision variables in $\{0, 1\}$.
   - *Hint 2*: What implication links customer group $j$ to stations $A_j$ and $B_j$? Write it as $\infty \cdot y_j(1 - x_{A_j})$.
   - *Hint 3*: Alternatively, expand the $2 \times 2$ loss matrix $\begin{pmatrix} C_j & C_j \\ C_j & 0 \end{pmatrix}$ directly on $(x_{A_j}, x_{B_j})$ using Theorem 13.1 to avoid creating $M$ auxiliary vertices.
   - *Failure Mode*: Using undirected $\infty$-edges between $y_j$ and $x_{A_j}$ falsely forces $x_{A_j} = 1 \implies y_j = 1$.

---

#### Problem P02 — `Codeforces 1082 G — Petya and Graph` `[EN]`

- **Judge URL**: [https://codeforces.com/problemset/problem/1082/G](https://codeforces.com/problemset/problem/1082/G)
- **Statement**: Given an undirected graph $G = (V, E)$ with $|V| = n \le 1000$, $|E| = m \le 1000$, positive vertex weights $a_v \in [1, 10^9]$, and positive edge weights $w_e \in [1, 10^9]$, define the weight of an induced subgraph $G[S]$ ($S \subseteq V$) as $\sum_{e \in E(S)} w_e - \sum_{v \in S} a_v$. Find the maximum weight of any induced subgraph (possibly $S = \emptyset$ with weight $0$).

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Despite mentioning a graph $G$, $G$ is the **problem object**, not the flow network! We are choosing a subset of vertices $S \subseteq V$ ($x_v \in \{0, 1\}$), and an edge $e = (u, v)$ contributes $+w_e$ iff $x_u = 1 \land x_v = 1$.
2. **Step 2: Intermediate Algebraic Representation**:
   $$\max_{x, y} \left( \sum_{e=(u,v) \in E} w_e y_e - \sum_{v \in V} a_v x_v \right) = \sum_{e \in E} w_e - \min_{x, y} \left( \sum_{e \in E} w_e(1 - y_e) + \sum_{v \in V} a_v x_v + \sum_{e=(u,v)} \infty \big(y_e(1 - x_u) + y_e(1 - x_v)\big) \right).$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Optimistic baseline: $R_{\max} = \sum_{e \in E} w_e$ (use 64-bit `long long`!).
   - Edges: $S \xrightarrow{w_e} y_e$, $y_e \xrightarrow{\infty} u$, $y_e \xrightarrow{\infty} v$, and $v \xrightarrow{a_v} T$.
   - Answer: $R_{\max} - \text{MinCut}(S, T)$.
   - **Complexity**: $V = n + m + 2 \le 2002$, $E = n + 3m \le 4000$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Can an edge $e = (u, v)$ with $w_e > 0$ ever hurt us if both $u$ and $v$ are already chosen? No—so we can treat $y_e \in \{0, 1\}$ as a free choice subject to $y_e \le x_u$ and $y_e \le x_v$.
   - *Hint 2*: Apply Picard's Maximum Weight Closure (Theorem 12.2) with positive weights $w_e$ on edges and negative weights $-a_v$ on vertices.
   - *Hint 3*: Ensure $\infty > \sum_{e \in E} w_e \approx 10^{12}$ (`1e18` in 64-bit integers).
   - *Failure Mode*: Using 32-bit `INF = 1e9` causes Dinic to cut the "infinite" prerequisite edges $y_e \to u$ when $w_e = 10^9$!

---

#### Problem P03 — `[SHOI2007] 善意的投票` (Kindhearted Voting) `[ZH]`

- **Judge URL**: [https://www.luogu.com.cn/problem/P2057](https://www.luogu.com.cn/problem/P2057)
- **Statement**: $N \le 300$ kindergarten children vote $x_i \in \{0, 1\}$ on whether to take a nap. Each child $i$ has an initial preference $s_i \in \{0, 1\}$. A conflict occurs whenever (a) a child votes against their own initial preference ($x_i \neq s_i$), or (b) a pair of friends $(u, v) \in F$ ($|F| = M \le \binom{N}{2}$) cast different votes ($x_u \neq x_v$). Minimize the total number of conflicts.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Binary state $x_i \in \{0, 1\}$ per child; unary penalty for $x_i \neq s_i$ and pairwise penalty for $x_u \neq x_v$.
2. **Step 2: Intermediate Algebraic Representation**:
   - Unary penalty for child $i$: if $s_i = 1$, penalty is $1 - x_i$; if $s_i = 0$, penalty is $x_i$.
   - Pairwise penalty for friend pair $(u, v) \in F$:
     $$[x_u \neq x_v] = x_u(1 - x_v) + x_v(1 - x_u).$$
   - Total objective to minimize:
     $$E(x) = \sum_{i : s_i = 1} (1 - x_i) + \sum_{i : s_i = 0} x_i + \sum_{(u, v) \in F} \big( x_u(1 - x_v) + x_v(1 - x_u) \big).$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - For each child $i$ with $s_i = 1$: add $S \xrightarrow{\; 1 \;} i$.
   - For each child $i$ with $s_i = 0$: add $i \xrightarrow{\; 1 \;} T$.
   - For each friend pair $(u, v) \in F$: add **bidirectional** unit edges $u \xrightarrow{\; 1 \;} v$ and $v \xrightarrow{\; 1 \;} u$.
   - Answer: $\text{MinCut}(S, T)$.
   - **Complexity**: Unit-capacity network with $V = N + 2 \le 302, E \le N + 2M$; Dinic runs in $O(E \sqrt{V})$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: There are no rewards to maximize here—we are directly minimizing conflicts!
   - *Hint 2*: How do you penalize both $(x_u = 1, x_v = 0)$ and $(x_u = 0, x_v = 1)$?
   - *Hint 3*: Add directed edges of capacity $1$ in both directions between $u$ and $v$.
   - *Failure Mode*: Adding only a single directed edge $u \to v$ allows $x_u = 0, x_v = 1$ with zero penalty.

---

#### Problem P04 — `[网络流24题] 方格取数问题` (Grid Number Selection) `[ZH]`

- **Judge URL**: [https://www.luogu.com.cn/problem/P2774](https://www.luogu.com.cn/problem/P2774)
- **Statement**: Given an $M \times N$ grid ($1 \le M, N \le 100$) of non-negative integers $w_{r, c} \ge 0$, select a subset of cells such that no two selected cells share a common side (4-adjacent), maximizing the sum of values of the selected cells.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Binary choice $x_{r,c} \in \{0, 1\}$ per cell; $M, N \le 100$ is too large for $O(2^{\min(M,N)})$ profile DP.
   - Mutual exclusion $x_u = 1 \land x_v = 1$ is supermodular ($\infty \cdot x_u x_v$), but the 2D grid graph is **bipartite** under chessboard parity $(r + c) \bmod 2$!
2. **Step 2: Intermediate Algebraic Representation**:
   Partition cells into $L = \{(r, c) : (r + c) \text{ is even}\}$ and $R = \{(r, c) : (r + c) \text{ is odd}\}$.
   Apply Bipartite Variable Inversion (Theorem 14.1): $\tilde{x}_u = x_u$ for $u \in L$, and $\tilde{x}_v = 1 - x_v$ for $v \in R$.
   $$\max_{x} \sum_{w} w_u x_u = \sum_{u \in L \cup R} w_u - \min_{\tilde{x}} \left( \sum_{u \in L} w_u(1 - \tilde{x}_u) + \sum_{v \in R} w_v \tilde{x}_v + \sum_{\substack{u \in L, v \in R \\ u \sim v}} \infty \cdot \tilde{x}_u(1 - \tilde{x}_v) \right).$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Optimistic baseline: $R_{\max} = \sum_{r, c} w_{r, c}$.
   - For $u \in L$ (even parity): add $S \xrightarrow{w_u} u$, and for each 4-neighbor $v \in R$, add $u \xrightarrow{\infty} v$.
   - For $v \in R$ (odd parity): add $v \xrightarrow{w_v} T$.
   - Answer: $R_{\max} - \text{MinCut}(S, T)$.
   - **Complexity**: $V = MN + 2 \le 10002$, $E \le 5MN \le 50000$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Color the grid like a chessboard. Every 4-adjacent pair connects a black cell to a white cell.
   - *Hint 2*: Flip the binary indicator on white cells ($\tilde{x}_v = 1 - x_v$) so that $x_u x_v$ becomes $\tilde{x}_u(1 - \tilde{x}_v)$.
   - *Hint 3*: Connect $S \to \text{Black} \xrightarrow{\infty} \text{White} \to T$ and subtract the min-cut from the sum of all cells.
   - *Failure Mode*: If the problem also forbade **8-adjacent (diagonal)** neighbors, diagonal neighbors have the **same** parity of $r + c$, creating odd cycles (triangles) and making the problem NP-hard!

---

#### Problem P05 — `AtCoder Beginner Contest 326, Problem G — Unlock Achievement` `[JA]`

- **Judge URL**: [https://atcoder.jp/contests/abc326/tasks/abc326_g](https://atcoder.jp/contests/abc326/tasks/abc326_g)
- **Statement**: There are $N \le 50$ skills, all initially at level $1$, and $M \le 50$ achievements. Raising skill $i$ by $1$ level (up to level $5$) costs $C_i \ge 0$ per level. Achievement $j$ grants reward $A_j > 0$ if and only if skill $i$ has reached at least level $L_{j, i} \in \{1, \dots, 5\}$ for **every** $i \in \{1, \dots, N\}$. Maximize (total achievement rewards minus total level-up costs).

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Although each skill has $5$ levels $\{1, 2, 3, 4, 5\}$, the condition for achievement $j$ is a conjunction of **threshold predicates** $[\text{level}_i \ge \ell]$!
   - By introducing $4$ unary threshold variables per skill ($x_{i, \ell} = [\text{level}_i \ge \ell]$ for $\ell \in \{2, 3, 4, 5\}$), the problem reduces immediately to a pure binary Maximum Weight Closure!
2. **Step 2: Intermediate Algebraic Representation**:
   Define binary variables $x_{i, \ell} \in \{0, 1\}$ for $i \in \{1, \dots, N\}, \ell \in \{2, 3, 4, 5\}$, and $y_j \in \{0, 1\}$ for achievement $j \in \{1, \dots, M\}$:
   - **Monotonicity of thresholds**: Reaching level $\ge \ell$ requires having reached level $\ge \ell - 1$:
     $$x_{i, \ell} = 1 \implies x_{i, \ell - 1} = 1 \qquad \Longleftrightarrow \qquad \infty \cdot x_{i, \ell}(1 - x_{i, \ell - 1}).$$
   - **Linear level-up cost**: Since $\text{level}_i = 1 + \sum_{\ell=2}^5 x_{i, \ell}$, each variable $x_{i, \ell} = 1$ costs exactly $C_i$!
   - **Achievement prerequisite**: Claiming $y_j = 1$ requires $x_{i, L_{j,i}} = 1$ for all $i$ with $L_{j,i} \ge 2$:
     $$y_j = 1 \implies x_{i, L_{j,i}} = 1 \qquad \Longleftrightarrow \qquad \infty \cdot y_j(1 - x_{i, L_{j,i}}).$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Optimistic baseline: $R_{\max} = \sum_{j=1}^M A_j$.
   - For each skill $i$ and $\ell \in \{2, 3, 4, 5\}$: add $x_{i, \ell} \xrightarrow{C_i} T$; if $\ell \ge 3$, add $x_{i, \ell} \xrightarrow{\infty} x_{i, \ell-1}$.
   - For each achievement $j$: add $S \xrightarrow{A_j} y_j$, and for each $i$ with $L_{j,i} \ge 2$, add $y_j \xrightarrow{\infty} x_{i, L_{j,i}}$.
   - **Complexity**: $V = 4N + M + 2 \le 252$, $E \le 7N + M(N + 1) \le 3000$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Decompose $\text{level}_i \in \{1, 2, 3, 4, 5\}$ into four binary indicator variables $x_{i, 2}, x_{i, 3}, x_{i, 4}, x_{i, 5} \in \{0, 1\}$ where $x_{i, \ell} = [\text{level}_i \ge \ell]$.
   - *Hint 2*: What constraint prevents the solver from buying $x_{i, 5} = 1$ without paying for $x_{i, 2}, x_{i, 3}, x_{i, 4}$?
   - *Hint 3*: Add chain implication edges $x_{i, \ell} \xrightarrow{\infty} x_{i, \ell-1}$ (or simply point $y_j \xrightarrow{\infty} x_{i, \ell}$ for all $\ell \le L_{j,i}$).
   - *Failure Mode*: Forgetting the chain edges $x_{i, \ell} \xrightarrow{\infty} x_{i, \ell-1}$ allows the solver to pay $1 \times C_i$ for level 5 instead of $4 \times C_i$!

---

### Tier 2: Intermediate (Problems P06–P11)

---

#### Problem P06 — `AtCoder Regular Contest 085, Problem E — MUL` `[JA]`

- **Judge URL**: [https://atcoder.jp/contests/arc085/tasks/arc085_c](https://atcoder.jp/contests/arc085/tasks/arc085_c)
- **Statement**: Given $N \le 100$ gems indexed $1, \dots, N$ with signed integer values $a_1, \dots, a_N \in [-10^9, 10^9]$, you may repeatedly choose any integer $k \in \{1, \dots, N\}$ and smash all gems whose index is a multiple of $k$. Find the maximum possible sum of values of the unsmashed gems.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - $N \le 100$, binary outcome per gem ($x_i = 1$ kept, $x_i = 0$ smashed), signed weights $a_i \in \mathbb{Z}$.
   - Smashing $i$ forces smashing all multiples $j = m \cdot i$. By contrapositive, **keeping $j$ forces keeping all divisors $i \mid j$**!
2. **Step 2: Intermediate Algebraic Representation**:
   $$\max_{x \in \{0,1\}^N} \sum_{i=1}^N a_i x_i \quad \text{s.t.} \quad x_j = 1 \implies x_i = 1 \;\;(\forall i \mid j)$$
   $$= \sum_{a_i > 0} a_i - \min_{x} \left( \sum_{a_i > 0} a_i(1 - x_i) + \sum_{a_i < 0} |a_i| x_i + \sum_{i \mid j} \infty \cdot x_j(1 - x_i) \right).$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Optimistic baseline: $R_{\max} = \sum_{a_i > 0} a_i$.
   - For each $i \in \{1, \dots, N\}$: if $a_i > 0$, add $S \xrightarrow{a_i} i$; if $a_i < 0$, add $i \xrightarrow{|a_i|} T$.
   - For each $i \in \{1, \dots, N\}$ and each multiple $j = 2i, 3i, \dots \le N$: add $j \xrightarrow{\infty} i$.
   - **Complexity**: $V = N + 2 = 102$, $E = N + \sum_{i=1}^N \lfloor N/i \rfloor = O(N \log N) \approx 500$ edges.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Forget the sequence of operations and characterize which subsets of gems can remain at the end.
   - *Hint 2*: A subset of kept gems is valid iff whenever gem $j$ is kept, none of its divisors $i \mid j$ were smashed.
   - *Hint 3*: Model this as Maximum Weight Closure on the divisibility poset.
   - *Failure Mode*: Using 32-bit integers overflows since $\sum a_i$ can reach $100 \times 10^9 = 10^{11}$.

---

#### Problem P07 — `Codeforces 311 E — Biologist` `[EN]`

- **Judge URL**: [https://codeforces.com/problemset/problem/311/E](https://codeforces.com/problemset/problem/311/E)
- **Statement**: There are $N \le 10^4$ dogs, each initially of sex $s_i \in \{0, 1\}$. Changing the sex of dog $i$ costs $v_i \ge 0$. There are $M \le 2000$ experiments. Experiment $j$ specifies a target sex $t_j \in \{0, 1\}$, a subset $I_j$ of $k_j \le 10$ dogs, a reward $w_j \ge 0$, and a boolean flag $f_j \in \{0, 1\}$. If all dogs in $I_j$ have sex $t_j$, you earn $+w_j$; otherwise, if $f_j = 1$, you must pay a penalty of $g \ge 0$ to the sponsor. Maximize net profit.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Binary state $x_i \in \{0, 1\}$ per dog; higher-order $k_j$-tuple clauses ($k_j \le 10$) of both All-1 type ($t_j = 1$) and All-0 type ($t_j = 0$) with soft violation penalty $g$.
2. **Step 2: Intermediate Algebraic Representation**:
   - Optimistic baseline: $R_{\max} = \sum_{j=1}^M w_j$ (notice $g$ is **not** added to $R_{\max}$!).
   - If experiment $j$ fails, we lose the optimistic reward $w_j$ AND (if $f_j = 1$) pay an extra penalty $g$, so the total loss when experiment $j$ fails is $W_j := w_j + f_j \cdot g$!
   - Apply Gadget 13.A for $t_j = 1$ (hub $z_j$ with $W_j(1 - z_j) + \sum_{u \in I_j} \infty z_j(1 - x_u)$) and Gadget 13.B for $t_j = 0$ (hub $w_j$ with $W_j w_j + \sum_{u \in I_j} \infty x_u(1 - w_j)$).
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - For each dog $i$: if $s_i = 1$, changing to $0$ costs $v_i(1 - x_i) \implies S \xrightarrow{v_i} i$; if $s_i = 0$, changing to $1$ costs $v_i x_i \implies i \xrightarrow{v_i} T$.
   - For each experiment $j$ with $W_j = w_j + f_j \cdot g$:
     - If $t_j = 1$: add $S \xrightarrow{W_j} z_j$ and $z_j \xrightarrow{\infty} u$ for all $u \in I_j$.
     - If $t_j = 0$: add $w_j \xrightarrow{W_j} T$ and $u \xrightarrow{\infty} w_j$ for all $u \in I_j$.
   - Answer: $\sum_{j=1}^M w_j - \text{MinCut}(S, T)$.
   - **Complexity**: $V = N + M + 2 \le 12002$, $E \le N + M + \sum k_j \le 3.4 \times 10^4$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Distinguish between $t_j = 1$ (All-1 AND hub connected to $S$) and $t_j = 0$ (All-0 NOR hub connected to $T$).
   - *Hint 2*: When an experiment with $f_j = 1$ fails, the difference between succeeding ($+w_j$) and failing ($-g$) is $w_j + g$.
   - *Hint 3*: Set the hub edge capacity to $w_j + f_j \cdot g$, while adding only $w_j$ to the optimistic baseline.
   - *Failure Mode*: Adding $w_j + g$ to the optimistic baseline overcounts the final answer by $g$ per $f_j = 1$ experiment!

---

#### Problem P08 — `[国家集训队] 文理分科` (Arts vs. Science Partitioning) `[ZH]`

- **Judge URL**: [https://www.luogu.com.cn/problem/P4313](https://www.luogu.com.cn/problem/P4313)
- **Statement**: In an $N \times M$ classroom ($N, M \le 100$), student $(r, c)$ chooses either Arts ($x_{r,c} = 1$) or Science ($x_{r,c} = 0$), gaining individual happiness $A_{r,c}$ (if Arts) or $B_{r,c}$ (if Science). Additionally, let $N_{r,c}$ be the set containing $(r, c)$ and its 4-adjacent neighbors (up to $5$ students). If **all** students in $N_{r,c}$ choose Arts, they gain an extra bonus $SA_{r,c}$; if **all** students in $N_{r,c}$ choose Science, they gain an extra bonus $SB_{r,c}$. Maximize total happiness.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - $N, M \le 100$ ($10^4$ students), binary state $x_{r,c} \in \{0, 1\}$, and each cell defines both a 5-variable All-1 AND clause ($SA_{r,c}$) and a 5-variable All-0 NOR clause ($SB_{r,c}$).
2. **Step 2: Intermediate Algebraic Representation**:
   $$R_{\max} = \sum_{r,c} \big( A_{r,c} + B_{r,c} + SA_{r,c} + SB_{r,c} \big).$$
   $$E(x, z, w) = \sum_{r,c} \Big[ A_{r,c}(1 - x_{r,c}) + B_{r,c} x_{r,c} + SA_{r,c}(1 - z_{r,c}) + SB_{r,c} w_{r,c} + \sum_{u \in N_{r,c}} \infty \big( z_{r,c}(1 - x_u) + x_u(1 - w_{r,c}) \big) \Big].$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - For each cell $v = (r, c)$:
     - Normalize unary edges $A_v(1 - x_v) + B_v x_v$ via Recipe 1 (or add $S \xrightarrow{A_v} v$ and $v \xrightarrow{B_v} T$).
     - Create Arts-hub $z_v$: add $S \xrightarrow{SA_v} z_v$ and $z_v \xrightarrow{\infty} u$ for all $u \in N_v$.
     - Create Science-hub $w_v$: add $w_v \xrightarrow{SB_v} T$ and $u \xrightarrow{\infty} w_v$ for all $u \in N_v$.
   - **Complexity**: $V = 3NM + 2 \le 30002$, $E \le 14NM \le 1.4 \times 10^5$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Do not try to flip variables here—the bonus is for **agreeing** states ($x_u = x_v$), which is already submodular!
   - *Hint 2*: Because $|N_{r,c}| = 5 \ge 3$, use Gadget 13.A for $SA_{r,c}$ and Gadget 13.B for $SB_{r,c}$.
   - *Hint 3*: Apply Recipe 1 normalization on $A_v(1 - x_v) + B_v x_v$ to cut Dinic's initial work in half.
   - *Failure Mode*: Confusing `[国家集训队] 文理分科` (same-state bonus $\implies$ submodular, no flip) with `方格取数` (same-state conflict $\implies$ supermodular, chessboard flip)!

---

#### Problem P09 — `Codeforces 808 F — Card Game` `[EN]`

- **Judge URL**: [https://codeforces.com/problemset/problem/808/F](https://codeforces.com/problemset/problem/808/F)
- **Statement**: You have $N \le 100$ cards; card $i$ has power $p_i$, magic number $c_i \le 10^5$, and level $l_i \le N$. You cannot simultaneously include two cards $i, j$ in your deck if $c_i + c_j$ is a **prime number**. Find the minimum level $L$ such that using only cards with $l_i \le L$, you can build a valid deck with total power $\ge K$ (or output $-1$).

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Monotonic feasibility in $L \implies$ binary search on $L \in [1, N]$.
   - For fixed $L$, we want the **Maximum Weight Independent Set** where $(i, j)$ conflict if $c_i + c_j$ is prime.
   - **Why is the conflict graph bipartite?** Every prime $> 2$ is **odd**, and $c_i + c_j$ is odd only if $c_i$ and $c_j$ have **opposite parity** ($c_i \not\equiv c_j \pmod 2$)!
   - **What about the even prime $2$?** $c_i + c_j = 2$ occurs **only** when $c_i = 1$ and $c_j = 1$! Among all cards with $c_i = 1$, we can never pick more than **one** card, so we simply keep only the single $c_i = 1$ card with the **largest $p_i$** and discard all other $c_i = 1$ cards!
2. **Step 2: Intermediate Algebraic Representation**:
   After deduplicating $c_i = 1$ cards to at most one card, partition the remaining cards into $L_{\text{odd}} = \{i : c_i \text{ odd}\}$ and $R_{\text{even}} = \{j : c_j \text{ even}\}$.
   Flip $\tilde{x}_j = 1 - x_j$ for $j \in R_{\text{even}}$:
   $$\text{MaxPower}(L) = \sum_{l_i \le L} p_i - \min_{\tilde{x}} \left( \sum_{i \in L_{\text{odd}}} p_i(1 - \tilde{x}_i) + \sum_{j \in R_{\text{even}}} p_j \tilde{x}_j + \sum_{\substack{i \in L_{\text{odd}}, j \in R_{\text{even}} \\ c_i + c_j \text{ prime}}} \infty \cdot \tilde{x}_i(1 - \tilde{x}_j) \right).$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Precompute primes up to $2 \times 10^5$ via a sieve.
   - Binary search $L \in [1, N]$. For a fixed $L$, filter cards with $l_i \le L$ and keep only the max-$p_i$ card among those with $c_i = 1$.
   - Build bipartite conflict network $S \xrightarrow{p_i} L_{\text{odd}} \xrightarrow{\infty} R_{\text{even}} \xrightarrow{p_j} T$ and check if $\sum p - \text{MinCut} \ge K$.
   - **Complexity**: $O(\log N)$ binary search steps $\times$ Dinic on $V \le 102, E \le 2600$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Binary search on the level $L$. For a fixed $L$, when can two cards $i, j$ sum to a prime?
   - *Hint 2*: All primes except $2$ are odd, so odd + even is bipartite!
   - *Hint 3*: How can two cards sum to $2$? Only $1 + 1 = 2$! Since all $c_i = 1$ cards have identical conflict neighborhoods, greedily keep only the one with the largest $p_i$.
   - *Failure Mode*: Keeping multiple $c_i = 1$ cards creates edges inside $L_{\text{odd}} \times L_{\text{odd}}$ (triangles with an even $c_j$ where $1 + c_j$ is prime), breaking bipartiteness!

---

#### Problem P10 — `[NOI2009] 植物大战僵尸` (Plants vs. Zombies) `[ZH]`

- **Judge URL**: [https://www.luogu.com.cn/problem/P2805](https://www.luogu.com.cn/problem/P2805)
- **Statement**: Detailed in Section 12.4. Given an $N \times M$ lawn ($N \le 20, M \le 30$) where each plant $u$ has signed score $w_u \in [-10^4, 10^4]$ and protects a list of cells $A(u)$ (plus every plant $(r, c)$ protects $(r, c-1)$ directly to its left), find the maximum score of a valid sequential zombie attack.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Eating $v$ requires eating all $u$ that protect $v$ ($x_v = 1 \implies x_u = 1$).
   - **Sequential Unlocking Trap**: Because plants must be eaten in a valid sequential order, directed cycles in the protection graph are unreachable deadlocks!
2. **Step 2: Intermediate Algebraic Representation**:
   - First compute $V_{\text{valid}} \subseteq V$ via Kahn's topological sort on $G_{\text{prot}}$ (where $u \to v \in E_{\text{prot}}$ means $u$ protects $v$).
   - Then solve Maximum Weight Closure restricted to $V_{\text{valid}}$:
     $$\text{Ans} = \sum_{\substack{u \in V_{\text{valid}} \\ w_u > 0}} w_u - \min_{x \in \{0,1\}^{V_{\text{valid}}}} \left( \sum_{w_u > 0} w_u(1 - x_u) + \sum_{w_u < 0} |w_u| x_u + \sum_{\substack{u, v \in V_{\text{valid}} \\ (u \to v) \in E_{\text{prot}}}} \infty \cdot x_v(1 - x_u) \right).$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Build $G_{\text{prot}}$: for each $(r, c)$, add $(r, c) \to (r, c-1)$ (if $c > 1$) and $(r, c) \to v$ for all $v \in A(r, c)$.
   - Run Kahn's BFS queue starting from $\text{indeg}_{\text{prot}}(u) = 0$ to find $V_{\text{valid}}$.
   - For $u \in V_{\text{valid}}$: add $S \xrightarrow{w_u} u$ (if $w_u > 0$) or $u \xrightarrow{|w_u|} T$ (if $w_u < 0$).
   - For $(u \to v) \in E_{\text{prot}}$ with $u, v \in V_{\text{valid}}$: add **$v \xrightarrow{\infty} u$** (since eating $v$ requires eating $u$!).
   - **Complexity**: $V \le 602, E \le 3.6 \times 10^5$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Be careful with edge directions: in $G_{\text{prot}}$ (Kahn's BFS), edges go from protector $u$ to protected $v$; in the closure network $\mathcal{N}$, $\infty$-edges go from dependent $v$ to prerequisite $u$!
   - *Hint 2*: Why can a vertex outside the cycle also be invalid? Because if $v$ is protected by $u$ and $u$ is in a cycle, $v$ can never be unlocked either—Kahn's BFS automatically prunes both cycles and their downstream dependents!
   - *Hint 3*: Run Dinic only on $V_{\text{valid}}$.
   - *Failure Mode*: Using Tarjan's SCC to delete only vertices with $|\text{SCC}| \ge 2$ fails to delete vertices in $V \setminus V_{\text{valid}}$ that have $|\text{SCC}| = 1$ but are reachable *from* a cycle in $G_{\text{prot}}$! Always use Kahn's in-degree queue!

---

#### Problem P11 — `AtCoder Beginner Contest 259, Problem G — Grid Card Game` `[JA]`

- **Judge URL**: [https://atcoder.jp/contests/abc259/tasks/abc259_g](https://atcoder.jp/contests/abc259/tasks/abc259_g)
- **Statement**: Given an $H \times W$ grid ($H, W \le 100$) with signed values $A_{i, j} \in [-10^9, 10^9]$, you choose a subset of rows $R_{\text{sel}} \subseteq \{1, \dots, H\}$ and a subset of columns $C_{\text{sel}} \subseteq \{1, \dots, W\}$ such that you **never** simultaneously choose row $i$ and column $j$ if $A_{i, j} < 0$. Your score is the sum of $A_{i, j}$ over all cells $(i, j)$ such that $i \in R_{\text{sel}}$ **or** $j \in C_{\text{sel}}$. Maximize your score.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - The decision variables are the $H$ rows $x_i \in \{0, 1\}$ and the $W$ columns $y_j \in \{0, 1\}$ ($H + W \le 200$ variables!).
   - Every cell $(i, j)$ creates a pairwise interaction strictly between row $i$ and column $j$, so the interaction graph between rows and columns is **bipartite**!
2. **Step 2: Intermediate Algebraic Representation**:
   Let $R_i = \sum_{j=1}^W A_{i, j}$ be the full sum of row $i$, and $C_j = \sum_{i=1}^H A_{i, j}$ be the full sum of column $j$.
   By Inclusion-Exclusion on $[x_i = 1 \lor y_j = 1] = x_i + y_j - x_i y_j$, if $(x, y)$ avoids all $(x_i = 1, y_j = 1)$ with $A_{i, j} < 0$, the exact score is:
   $$\text{Score}(x, y) = \sum_{i=1}^H R_i x_i + \sum_{j=1}^W C_j y_j - \sum_{A_{i,j} \ge 0} A_{i, j} x_i y_j - \sum_{A_{i,j} < 0} \infty \cdot x_i y_j.$$
   Notice that every quadratic penalty term is a multiple of $x_i y_j$ (**supermodular**!).
   Apply Bipartite Variable Inversion (Theorem 14.1) on the columns by setting $\tilde{y}_j = 1 - y_j$ (so $y_j = 1 - \tilde{y}_j$):
   $$\text{Score}(x, \tilde{y}) = \sum_{i=1}^H R_i x_i + \sum_{j=1}^W C_j (1 - \tilde{y}_j) - \sum_{A_{i,j} \ge 0} A_{i, j} x_i(1 - \tilde{y}_j) - \sum_{A_{i,j} < 0} \infty \cdot x_i(1 - \tilde{y}_j)!$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Normalize the unary terms for each row $i$:
     - If $R_i > 0$: add $R_i$ to $R_{\max}$ and add $S \xrightarrow{R_i} \text{Row}_i$ (cost $R_i(1 - x_i)$).
     - If $R_i < 0$: add $\text{Row}_i \xrightarrow{|R_i|} T$ (cost $|R_i| x_i$).
   - Normalize the unary terms for each column $j$ (in flipped variable $\tilde{y}_j$):
     - If $C_j > 0$: add $C_j$ to $R_{\max}$ and add $\text{Col}_j \xrightarrow{C_j} T$ (cost $C_j \tilde{y}_j = C_j(1 - y_j)$).
     - If $C_j < 0$: add $S \xrightarrow{|C_j|} \text{Col}_j$ (cost $|C_j|(1 - \tilde{y}_j) = |C_j| y_j$).
   - For each cell $(i, j)$:
     - If $A_{i, j} \ge 0$: add $\text{Row}_i \xrightarrow{\; A_{i,j} \;} \text{Col}_j$.
     - If $A_{i, j} < 0$: add $\text{Row}_i \xrightarrow{\; \infty \;} \text{Col}_j$.
   - **Complexity**: $V = H + W + 2 \le 202$ vertices (not $HW$!), $E = H + W + HW \le 10200$ edges!
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Do NOT create a vertex for each of the $HW$ cells—create vertices only for the $H$ rows and $W$ columns!
   - *Hint 2*: Use Inclusion-Exclusion $[x_i = 1 \lor y_j = 1] = x_i + y_j - x_i y_j$ to write the score as row sums + column sums minus double-counted intersections $A_{i, j} x_i y_j$.
   - *Hint 3*: Flip $\tilde{y}_j = 1 - y_j$ on the columns so that $x_i y_j = x_i(1 - \tilde{y}_j)$ compiles to a single directed edge $\text{Row}_i \to \text{Col}_j$.
   - *Failure Mode*: Creating $HW$ auxiliary cell vertices works if $A_{i, j}$ is handled carefully, but increases the vertex count $50\times$ from $202$ to $10202$; the algebraic Inclusion-Exclusion + Bipartite Flip compilation uses zero cell vertices!


---

## 4-Tier Curated Problem Bank (Part 2: Advanced & Mastery — Problems P12 to P22)

---

### Tier 3: Advanced (Problems P12–P17)

---

#### Problem P12 — `AtCoder Beginner Contest 193, Problem F — Zebraness` `[JA]`

- **Judge URL**: [https://atcoder.jp/contests/abc193/tasks/abc193_f](https://atcoder.jp/contests/abc193/tasks/abc193_f)
- **Statement**: Given an $N \times N$ grid ($1 \le N \le 100$) where each cell is `'B'` (Black), `'W'` (White), or `'?'` (uncolored), replace each `'?'` with `'B'` or `'W'` to maximize the **Zebraness**—defined as the number of 4-adjacent cell pairs $\{u, v\}$ that have **different** colors.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Each cell $u = (r, c)$ has a binary color $x_u \in \{0, 1\}$ ($1$ = Black, $0$ = White; pre-colored cells have $x_u$ clamped via $\infty$ unary edges).
   - We want to **maximize** $\sum_{u \sim v} [x_u \neq x_v]$, which is equivalent to $R_{\max} - \min_x \sum_{u \sim v} [x_u = x_v]$ where $R_{\max} = 2N(N - 1)$ is the total number of 4-adjacent grid edges.
   - Penalizing $[x_u = x_v] = x_u x_v + (1 - x_u)(1 - x_v)$ has $A = 1, D = 1, B = 0, C = 0 \implies A + D = 2 > 0 = B + C$ (**strictly supermodular**!).
   - Because the 2D grid is **bipartite** under chessboard parity $(r + c) \bmod 2$, Theorem 14.1 rescues the entire problem!
2. **Step 2: Intermediate Algebraic Representation**:
   Partition the grid into $L = \{(r, c) : r + c \text{ even}\}$ and $R = \{(r, c) : r + c \text{ odd}\}$.
   Define flipped variables $\tilde{x}_u = x_u$ for $u \in L$ and $\tilde{x}_v = 1 - x_v$ for $v \in R$:
   $$[x_u = x_v] = [\tilde{x}_u \neq \tilde{x}_v] = \tilde{x}_u(1 - \tilde{x}_v) + \tilde{x}_v(1 - \tilde{x}_u)!$$
   And for clamped cells:
   - If $u \in L$ is `'B'` ($x_u = 1 \iff \tilde{x}_u = 1$) or $v \in R$ is `'W'` ($x_v = 0 \iff \tilde{x}_v = 1$): forbid $\tilde{x} = 0$ via $\infty(1 - \tilde{x})$.
   - If $u \in L$ is `'W'` ($x_u = 0 \iff \tilde{x}_u = 0$) or $v \in R$ is `'B'` ($x_v = 1 \iff \tilde{x}_v = 0$): forbid $\tilde{x} = 1$ via $\infty \tilde{x}$.
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Optimistic baseline: $R_{\max} = 2N(N - 1)$.
   - For each cell $w = (r, c)$:
     - If $(w \in L \text{ and color is 'B'})$ or $(w \in R \text{ and color is 'W'})$: add $S \xrightarrow{\infty} w$.
     - If $(w \in L \text{ and color is 'W'})$ or $(w \in R \text{ and color is 'B'})$: add $w \xrightarrow{\infty} T$.
   - For each 4-adjacent pair $(u, v)$: add bidirectional unit edges $u \xrightarrow{1} v$ and $v \xrightarrow{1} u$.
   - Answer: $2N(N - 1) - \text{MinCut}(S, T)$.
   - **Complexity**: $V = N^2 + 2 \le 10002$, $E \le 5N^2 \le 50000$; unit internal capacities guarantee $O(E \sqrt{V})$ Dinic runtime.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Maximizing bichromatic edges is Max-Cut, which is NP-hard on general graphs—why is it polynomial on a grid?
   - *Hint 2*: Flip the meaning of Black and White on all cells with $(r + c)$ odd!
   - *Hint 3*: After flipping odd cells, "opposite original colors" becomes "same flipped state", so disagreeing flipped states pay $1$ via bidirectional unit edges $u \stackrel{1}{\longleftrightarrow} v$.
   - *Failure Mode*: Forgetting to flip the `'B'`/`'W'` clamping condition on odd-parity cells $v \in R$.

---

#### Problem P13 — `[TJOI2015] 线性代数` (Linear Algebra) `[ZH]`

- **Judge URL**: [https://www.luogu.com.cn/problem/P3973](https://www.luogu.com.cn/problem/P3973)
- **Statement**: Given an $N \times N$ non-negative matrix $B_{i, j} \ge 0$ and a $1 \times N$ non-negative row vector $C_i \ge 0$ ($1 \le N \le 500$), find a binary vector $A \in \{0, 1\}^{1 \times N}$ maximizing the scalar:
  $$D = (A \cdot B - C) \cdot A^T.$$

1. **Step 1: Non-Graph Diagnostic Signal**:
   - The linear-algebraic disguise $(A \cdot B - C) \cdot A^T$ is a quadratic form over $A \in \{0, 1\}^N$!
   - Since $A_i \in \{0, 1\}$ satisfies $A_i^2 = A_i$, expanding the matrix multiplication reveals a pure quadratic pseudo-Boolean maximization problem!
2. **Step 2: Intermediate Algebraic Representation**:
   Expand $D$ entry by entry:
   $$D(A) = \sum_{i=1}^N \left( \sum_{j=1}^N A_j B_{j, i} - C_i \right) A_i = \sum_{i=1}^N \sum_{j=1}^N B_{i, j} A_i A_j - \sum_{i=1}^N C_i A_i.$$
   Using Theorem 13.1's symmetric half-edge identity $A_i A_j = \frac{1}{2} A_i + \frac{1}{2} A_j - \frac{1}{2}\big(A_i(1 - A_j) + A_j(1 - A_i)\big)$, or using $1 - A_i A_j = (1 - A_i) + A_i(1 - A_j)$:
   $$D(A) = \sum_{i=1}^N \sum_{j=1}^N B_{i, j} - \min_{A \in \{0,1\}^N} \left( \sum_{i=1}^N \left(\sum_{j=1}^N B_{i, j}\right)(1 - A_i) + \sum_{i=1}^N C_i A_i + \sum_{i=1}^N \sum_{j=1}^N B_{i, j} A_i(1 - A_j) \right)!$$
   Let us verify that identity! For any $(A_i, A_j) \in \{0, 1\}^2$:
   $$1 - A_i A_j = (1 - A_i) + A_i(1 - A_j).$$
   Multiplying by $B_{i, j}$ and summing over all $i, j \in \{1, \dots, N\}$ gives the exact formula above with **zero auxiliary vertices** and **no half-integers**!
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Optimistic baseline: $R_{\max} = \sum_{i=1}^N \sum_{j=1}^N B_{i, j}$.
   - For each $i \in \{1, \dots, N\}$:
     - Add $S \xrightarrow{\; \sum_{j=1}^N B_{i, j} \;} i$ (representing $\sum_j B_{i, j}(1 - A_i)$).
     - Add $i \xrightarrow{\; C_i \;} T$ (representing $C_i A_i$).
   - For each pair $i \neq j$: add directed edge $i \xrightarrow{\; B_{i, j} \;} j$ (or combine $i \to j$ and $j \to i$).
   - Answer: $R_{\max} - \text{MinCut}(S, T)$.
   - **Complexity**: Creating $N^2$ auxiliary hub nodes would give $V = 2.5 \times 10^5$ vertices (TLE/MLE), whereas our algebraic identity $1 - A_i A_j = (1 - A_i) + A_i(1 - A_j)$ uses only **$V = N + 2 = 502$ vertices** and $E = N^2 + 2N$ edges!
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Expand $(A B - C) A^T = \sum_{i,j} B_{i,j} A_i A_j - \sum_i C_i A_i$.
   - *Hint 2*: Creating a vertex for every pair $(i, j)$ creates $500^2 = 250,000$ vertices—too slow!
   - *Hint 3*: Use the exact identity $B_{i,j}(1 - A_i A_j) = B_{i,j}(1 - A_i) + B_{i,j} A_i(1 - A_j)$ to compile the entire quadratic form on just $N$ vertices!
   - *Failure Mode*: Building $N^2$ auxiliary vertices causes Memory/Time Limit Exceeded for $N = 500$.

---

#### Problem P14 — `[CEOI 2008] Order` (Job–Machine Rental vs. Purchase) `[EN]`

- **Judge URL**: [https://oj.uz/problem/view/CEOI08_order](https://oj.uz/problem/view/CEOI08_order) / [https://www.luogu.com.cn/problem/P4177](https://www.luogu.com.cn/problem/P4177)
- **Statement**: A factory has $N \le 1200$ potential orders and $M \le 1200$ machines. Accepting order $i$ earns profit $v_i \ge 0$, but requires a subset of machines $M_i \subseteq \{1, \dots, M\}$. Each machine $j$ can be **purchased permanently** at cost $c_j \ge 0$ (usable by all orders), OR **rented specifically for order $i$** at rental fee $r_{i, j} \ge 0$. Maximize net profit.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Each order $i$ is a binary choice $x_i \in \{0, 1\}$, and each machine $j$ has a permanent purchase choice $y_j \in \{0, 1\}$.
   - What if order $i$ is accepted ($x_i = 1$) but machine $j \in M_i$ is **not** purchased permanently ($y_j = 0$)? Instead of being forbidden ($\infty$), we simply pay the **rental fee $r_{i, j}$**!
2. **Step 2: Intermediate Algebraic Representation**:
   $$\max_{x, y} \left( \sum_{i=1}^N v_i x_i - \sum_{j=1}^M c_j y_j - \sum_{i=1}^N \sum_{j \in M_i} r_{i, j} x_i(1 - y_j) \right)$$
   $$= \sum_{i=1}^N v_i - \min_{x, y} \left( \sum_{i=1}^N v_i(1 - x_i) + \sum_{j=1}^M c_j y_j + \sum_{i=1}^N \sum_{j \in M_i} r_{i, j} x_i(1 - y_j) \right).$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Optimistic baseline: $R_{\max} = \sum_{i=1}^N v_i$.
   - For each order $i$: add $S \xrightarrow{v_i} x_i$.
   - For each machine $j$: add $y_j \xrightarrow{c_j} T$.
   - For each requirement $j \in M_i$: add **finite-capacity** directed edge $x_i \xrightarrow{\; r_{i,j} \;} y_j$.
   - **Complexity**: $V = N + M + 2 \le 2402$, $E \le N + M + NM \le 1.44 \times 10^6$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: How does renting machine $j$ for order $i$ differ from standard Project Selection?
   - *Hint 2*: You only pay the rental fee $r_{i, j}$ when $x_i = 1$ (order accepted) AND $y_j = 0$ (machine not bought).
   - *Hint 3*: That condition is literally the cut monomial $r_{i, j} x_i(1 - y_j)$, so replace $\infty$ with $r_{i, j}$!
   - *Failure Mode*: Creating separate vertices for rentals instead of simply lowering the prerequisite edge capacity from $\infty$ to $r_{i, j}$.

---

#### Problem P15 — `AtCoder Regular Contest 074, Problem F — Lotus Leaves` `[JA]`

- **Judge URL**: [https://atcoder.jp/contests/arc074/tasks/arc074_d](https://atcoder.jp/contests/arc074/tasks/arc074_d)
- **Statement**: On an $H \times W$ grid ($H, W \le 100$), some cells contain lotus leaves `'o'`, a start leaf `'S'`, and a target leaf `'T'`. A frog can jump between any two leaves in the **same row** or the **same column**. Find the minimum number of `'o'` leaves to delete so that `'T'` becomes unreachable from `'S'` (or output $-1$ if `'S'` and `'T'` share a row or column).

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Deleting a leaf $(r, c)$ severs the connection between **Row $r$** and **Column $c$**!
   - Thus the actual vertices of the reachability state space are the $H$ rows and $W$ columns, and each leaf $(r, c)$ is an **undirected unit-capacity bridge** between Row $r$ and Column $c$!
2. **Step 2: Intermediate Algebraic Representation**:
   Assign binary variable $x_r \in \{0, 1\}$ to each row $r$ ($1$ if reachable from $S$) and $y_c \in \{0, 1\}$ to each column $c$ ($1$ if reachable from $S$).
   - Clamped source/sink: $x_{r_S} = 1, y_{c_S} = 1$ ($S \xrightarrow{\infty} R_{r_S}, C_{c_S}$) and $x_{r_T} = 0, y_{c_T} = 0$ ($R_{r_T}, C_{c_T} \xrightarrow{\infty} T$).
   - If Row $r$ and Column $c$ have different reachability states ($x_r \neq y_c$) and cell $(r, c)$ has a leaf `'o'`, that leaf **must** be deleted (cost $x_r(1 - y_c) + y_c(1 - x_r)$).
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - If $r_S = r_T$ or $c_S = c_T$, output $-1$.
   - Add $S \xrightarrow{\infty} R_{r_S}$, $S \xrightarrow{\infty} C_{c_S}$, $R_{r_T} \xrightarrow{\infty} T$, $C_{c_T} \xrightarrow{\infty} T$.
   - For every leaf `'o'` at $(r, c)$: add $R_r \xrightarrow{1} C_c$ and $C_c \xrightarrow{1} R_r$.
   - Output $\text{MinCut}(S, T)$.
   - **Complexity**: $V = H + W + 2 \le 202$, $E \le 2HW + 4 \le 20004$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Instead of making leaves vertices and jumps edges, invert the roles: make rows and columns vertices, and make leaves edges!
   - *Hint 2*: A leaf at $(r, c)$ allows moving from row $r$ to column $c$ and from column $c$ to row $r$.
   - *Hint 3*: Deleting leaf $(r, c)$ corresponds to cutting the bidirectional unit edge $R_r \stackrel{1}{\longleftrightarrow} C_c$.
   - *Failure Mode*: Using only a one-way edge $R_r \to C_c$ fails because a frog can jump from column $c$ into row $r$ via leaf $(r, c)$!

---

#### Problem P16 — `[BZOJ 3511] 土地划分` (Land Partitioning — Complete $2 \times 2$ Edge Merging) `[ZH]`

- **Judge URL**: [https://hydro.ac/d/bzoj/p/3511](https://hydro.ac/d/bzoj/p/3511)
- **Statement**: $N \le 10^4$ plots of land and $M \le 4 \times 10^4$ roads are divided between two brothers $A$ ($x_i = 1$) and $B$ ($x_i = 0$). Plot $i$ yields $V_{A, i}$ if given to $A$, or $V_{B, i}$ if given to $B$ (some plots are pre-assigned to $A$ or $B$). For each road $e = (u, v)$: if both $u, v$ go to $A$, they gain $E_{A, e}$; if both go to $B$, they gain $E_{B, e}$; if one goes to $A$ and the other to $B$, they pay a fence penalty $E_{C, e}$. Maximize total value.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Every road $e = (u, v)$ defines a general $2 \times 2$ payoff table with **all three effects**: all-1 bonus $E_A$, all-0 bonus $E_B$, and disagreement penalty $E_C$!
   - With $M = 4 \times 10^4$, creating $2M = 8 \times 10^4$ auxiliary hub vertices slows down Dinic; Theorem 13.1's zero-auxiliary decomposition compiles every road directly onto $(u, v)$!
2. **Step 2: Intermediate Algebraic Representation**:
   For a road $e = (u, v)$, add $E_A + E_B$ to the optimistic baseline $R_{\max}$. The $2 \times 2$ loss matrix $\Theta_e(x_u, x_v)$ is:
   $$\Theta_e(x_u, x_v) = \begin{array}{c|cc}
   x_u \setminus x_v & 0 \;(B) & 1 \;(A) \\
   \hline
   0 \;(B) & E_A & E_A + E_B + E_C \\
   1 \;(A) & E_A + E_B + E_C & E_B
   \end{array}.$$
   Check submodularity: $(E_A + E_B) \le 2(E_A + E_B + E_C)$ with excess $\Delta = E_A + E_B + 2E_C \ge 0$.
   Using the symmetric split $\alpha = \beta = \frac{E_A + E_B}{2} + E_C$ (doubling all weights by $2$ to keep integers!):
   $$\Theta_e(x_u, x_v) = E_A(1 - x_u)x_u\text{-free} \implies \frac{E_A}{2}(1 - x_u) + \frac{E_A}{2}(1 - x_v) + \frac{E_B}{2}x_u + \frac{E_B}{2}x_v + \left(\frac{E_A + E_B}{2} + E_C\right)\big(x_u(1 - x_v) + x_v(1 - x_u)\big)!$$
   *(Or using the integer asymmetric split $\alpha = 0, \beta = \Delta$ from Theorem 13.1 without doubling!)*
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Accumulate all unary coefficients for each vertex $u \in \{1, \dots, N\}$, normalize via Recipe 1, and add directed road edges of capacity $\Delta_e$.
   - **Complexity**: $V = N + 2 = 10002$ vertices, $E = N + 2M \le 90000$ edges.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Write down the $2 \times 2$ loss table $\Theta_e(x_u, x_v)$ relative to the optimistic reward $E_A + E_B$.
   - *Hint 2*: Compute $\Delta = (B + C) - (A + D) = E_A + E_B + 2E_C$.
   - *Hint 3*: Either double all capacities by $2$ and use symmetric edges $\Delta/2$, or use Theorem 13.1's exact integer formula without doubling!
   - *Failure Mode*: Integer division `E_A / 2` truncating odd numbers when using the symmetric split without multiplying all capacities by $2$.

---

#### Problem P17 — `Codeforces 1404 E — Bricks` `[EN]`

- **Judge URL**: [https://codeforces.com/problemset/problem/1404/E](https://codeforces.com/problemset/problem/1404/E)
- **Statement**: Given an $N \times M$ grid ($N, M \le 200$) of black (`'#'`) and white (`'.'`) cells, cover all black cells with the minimum number of non-overlapping $1 \times k$ (horizontal) or $k \times 1$ (vertical) bricks ($k \ge 1$). Bricks cannot cover white cells.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Any valid brick tiling is formed by starting with $|\mathcal{B}|$ unit $1 \times 1$ bricks (one per black cell) and **gluing** adjacent black cells either horizontally (across a shared vertical boundary $h \in \mathcal{H}$) or vertically (across a shared horizontal boundary $v \in \mathcal{V}$).
   - Every glue operation reduces the total number of bricks by **exactly $1$**!
   - When is a set of glue operations valid? If and only if **no black cell is simultaneously glued horizontally AND glued vertically** (since that would create an L-shaped or cross-shaped brick)!
   - Therefore, we want to select the **maximum number of glue boundaries** from $\mathcal{H} \sqcup \mathcal{V}$ such that no $h \in \mathcal{H}$ and $v \in \mathcal{V}$ share a common black cell!
2. **Step 2: Intermediate Algebraic Representation**:
   - Left shore $L = \mathcal{H}$ (horizontal glues between $(r, c)$ and $(r, c+1)$), binary variable $x_h \in \{0, 1\}$.
   - Right shore $R = \mathcal{V}$ (vertical glues between $(r, c)$ and $(r+1, c)$), binary variable $y_v \in \{0, 1\}$.
   - Conflict: if $h \in \mathcal{H}$ and $v \in \mathcal{V}$ touch the same black cell $(r, c)$, we cannot pick both ($\infty \cdot x_h y_v$).
   - Flip $\tilde{y}_v = 1 - y_v$ for $v \in \mathcal{V}$:
     $$\text{MaxGlues} = |\mathcal{H}| + |\mathcal{V}| - \min_{x, \tilde{y}} \left( \sum_{h \in \mathcal{H}} (1 - x_h) + \sum_{v \in \mathcal{V}} \tilde{y}_v + \sum_{h \cap v \neq \emptyset} \infty \cdot x_h(1 - \tilde{y}_v) \right).$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Create a vertex for each horizontal pair $h \in \mathcal{H}$ of adjacent `'#'` cells ($S \xrightarrow{1} h$) and each vertical pair $v \in \mathcal{V}$ of adjacent `'#'` cells ($v \xrightarrow{1} T$).
   - For each black cell $(r, c)$, add $\infty$-edges from its incident horizontal pairs (left/right) to its incident vertical pairs (up/down) ($h \xrightarrow{\infty} v$).
   - Final answer: $|\mathcal{B}| - \big(|\mathcal{H}| + |\mathcal{V}| - \text{MinCut}(S, T)\big)$.
   - **Complexity**: Unit-vertex bipartite network (Maximum Independent Set on bipartite graph $L \cup R$) with $V \le 2NM \le 8 \times 10^4$, $E \le 6NM$; Dinic runs in $O(E \sqrt{V})$ time ($\approx 40\text{ ms}$).
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Count bricks via Euler's formula on trees/paths: `#Bricks = #BlackCells - #GlueBoundaries`.
   - *Hint 2*: Notice that two horizontal glues sharing a cell $(r, c-1)-(r, c)-(r, c+1)$ do NOT conflict—they just form a $1 \times 3$ brick! Conflicts ONLY occur between a horizontal glue and a vertical glue!
   - *Hint 3*: Find the Maximum Independent Set on the bipartite graph of Horizontal Glues vs. Vertical Glues via Bipartite Variable Inversion.
   - *Failure Mode*: Adding conflict edges between two horizontal glues (or two vertical glues) restricts bricks to length $\le 2$ instead of arbitrary length $k$!

---

### Tier 4: Mastery (Problems P18–P22)

---

#### Problem P18 — `AtCoder Grand Contest 038, Problem F — Two Permutations` `[JA]`

- **Judge URL**: [https://atcoder.jp/contests/agc038/tasks/agc038_f](https://atcoder.jp/contests/agc038/tasks/agc038_f)
- **Statement & Complete 4-Step Derivation**: Fully derived and hand-traced in **Iteration 15 (Sections 15.1–15.4)**.
- **Bonus Dual Variation (Maximizing Agreement $|\{i : A_i = B_i\}|$)**:
  What if the problem instead asked to **maximize** $|\{i : A_i = B_i\}| = N - \min |\{i : A_i \neq B_i\}|$?
  Then the penalty at index $i$ is $\Theta_i(x_c, y_d) = [A_i \neq B_i]$:
  - In Case 4 ($P_i \neq Q_i$), $\Theta_i(x_c, y_d) = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$, which satisfies $A + D = 1 \le 2 = B + C$ (**already submodular in unflipped $(x_c, y_d)$**!) and compiles by Theorem 13.1 into $x_c + y_d(1 - x_c)$ ($c \xrightarrow{1} T$ and $d \xrightarrow{1} c$).
  - In Case 5 ($P_i = Q_i \neq i$), $\Theta_i(x_c, y_d) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, which is also **submodular in unflipped $(x_c, y_d)$** and compiles into $c \stackrel{1}{\longleftrightarrow} d$!
  Thus both maximization of $|\{i : A_i \neq B_i\}|$ (via Bipartite Variable Flip) and maximization of $|\{i : A_i = B_i\}|$ (via Direct Submodular Cut) are solvable in $O(N\sqrt{N})$ time!

---

#### Problem P19 — `AtCoder Regular Contest 107, Problem F — Sum of Abs` `[JA]`

- **Judge URL**: [https://atcoder.jp/contests/arc107/tasks/arc107_f](https://atcoder.jp/contests/arc107/tasks/arc107_f)
- **Statement**: Given an undirected graph $G = (V, E)$ with $N \le 300, M \le 300$, vertex deletion costs $A_v \ge 0$, and signed vertex weights $B_v \in [-10^6, 10^6]$. Deleting a subset $D \subseteq V$ costs $\sum_{v \in D} A_v$, and each connected component $C$ of $G[V \setminus D]$ gives a score of $\left|\sum_{v \in C} B_v\right|$. Maximize $\sum_{C} \left|\sum_{v \in C} B_v\right| - \sum_{v \in D} A_v$.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - The non-linear absolute value $|S_C| = \max(+S_C, -S_C)$ means that for each surviving component $C$, we can **choose a sign $s_C \in \{+1, -1\}$**, and every vertex $v \in C$ contributes $s_C B_v$!
   - Since two vertices in different components are separated by deleted vertices, this is equivalent to assigning **every vertex $v \in V$ one of three states**:
     $$\sigma_v \in \{+1 \text{ (kept as } +\text{)},\; 0 \text{ (deleted)},\; -1 \text{ (kept as } -\text{)}\},$$
     subject to the **single local rule**: no edge $(u, v) \in E$ may have $\sigma_u = +1$ and $\sigma_v = -1$!
2. **Step 2: Intermediate Algebraic Representation**:
   Encode the $3$ ordered states $\{+1, 0, -1\}$ of vertex $v$ using two ordered binary variables $(x_{v,1}, x_{v,2}) \in \{(1,1), (1,0), (0,0)\}$ enforced by the monotonicity constraint $x_{v,2} = 1 \implies x_{v,1} = 1$ ($\infty \cdot x_{v,2}(1 - x_{v,1})$):
   - $\sigma_v = +1 \iff (x_{v,1}, x_{v,2}) = (1, 1)$: reward $+B_v$.
   - $\sigma_v = 0 \text{ (Deleted)} \iff (x_{v,1}, x_{v,2}) = (1, 0)$: reward $-A_v$.
   - $\sigma_v = -1 \iff (x_{v,1}, x_{v,2}) = (0, 0)$: reward $-B_v$.
   - Optimistic baseline per vertex: $M_v = |B_v|$.
     - If $B_v \ge 0$: losses at $+1, 0, -1$ are $0,\; B_v + A_v,\; 2B_v$, represented by:
       $$B_v(1 - x_{v,1}) + (B_v + A_v) x_{v,1}(1 - x_{v,2}) + B_v(1 - x_{v,2})!$$
     - If $B_v < 0$: losses at $+1, 0, -1$ are $2|B_v|,\; |B_v| + A_v,\; 0$, represented by:
       $$|B_v| x_{v,1} + (|B_v| + A_v) x_{v,1}(1 - x_{v,2}) + |B_v| x_{v,2}!$$
   - Forbidden adjacency $(\sigma_u = +1 \land \sigma_v = -1) \iff (x_{u,2} = 1 \land x_{v,1} = 0)$:
     $$\infty \cdot x_{u,2}(1 - x_{v,1}) + \infty \cdot x_{v,2}(1 - x_{u,1}).$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Optimistic baseline: $R_{\max} = \sum_{v=1}^N |B_v|$.
   - For each vertex $v \in V$, create two nodes $v_1, v_2$ with $v_1 \xrightarrow{|B_v| + A_v} v_2$ and $v_2 \xrightarrow{\infty} v_1$:
     - If $B_v > 0$: add $S \xrightarrow{B_v} v_1$ and $S \xrightarrow{B_v} v_2$ (or simply $S \xrightarrow{2B_v} v_1$ since $x_{v,2} \le x_{v,1}$ implies $(1 - x_{v,2}) = (1 - x_{v,1}) + x_{v,1}(1 - x_{v,2})$!).
     - Let us verify that simplification! Since $1 - x_{v,2} = (1 - x_{v,1}) + x_{v,1}(1 - x_{v,2})$, the loss for $B_v \ge 0$ simplifies to **$2B_v(1 - x_{v,1}) + (2B_v + A_v) x_{v,1}(1 - x_{v,2})$**, and for $B_v < 0$ simplifies to **$2|B_v| x_{v,2} + (2|B_v| + A_v) x_{v,1}(1 - x_{v,2})$**!
   - For each undirected edge $(u, v) \in E$: add $u_2 \xrightarrow{\infty} v_1$ and $v_2 \xrightarrow{\infty} u_1$.
   - **Complexity**: $V = 2N + 2 \le 602$, $E = 3N + 2M \le 1500$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Replace $|\sum_{v \in C} B_v|$ with $\max_{s_C \in \{\pm 1\}} \sum_{v \in C} s_C B_v$.
   - *Hint 2*: Each vertex now has 3 states $\{+1, \text{Deleted}, -1\}$, and no $+1$ vertex can touch a $-1$ vertex.
   - *Hint 3*: Split each vertex into a 2-edge chain $S \to v_1 \to v_2 \to T$ (with $v_2 \xrightarrow{\infty} v_1$) and add $u_2 \xrightarrow{\infty} v_1, v_2 \xrightarrow{\infty} u_1$ for each edge $(u, v) \in E$.
   - *Failure Mode*: Omitting the reverse edge $v_2 \xrightarrow{\infty} v_1$ allows the cut to sever both $S \to v_1$ and $v_2 \to T$ simultaneously (the invalid 4th state $(x_{v,1}=0, x_{v,2}=1)$).

---

#### Problem P20 — `AtCoder Regular Contest 142, Problem E — Pairing Wizards` `[JA]`

- **Judge URL**: [https://atcoder.jp/contests/arc142/tasks/arc142_e](https://atcoder.jp/contests/arc142/tasks/arc142_e)
- **Statement**: $N \le 100$ wizards have initial strength $a_i \in [1, 100]$ and target attribute $b_i \in [1, 100]$. Raising $a_i$ by $1$ costs $1$. Given $M$ pairs $(x_k, y_k)$, each pair requires $\min(a'_{x_k}, a'_{y_k}) \ge \min(b_{x_k}, b_{y_k})$ and $\max(a'_{x_k}, a'_{y_k}) \ge \max(b_{x_k}, b_{y_k})$. Find the minimum total cost $\sum_{i=1}^N (a'_i - a_i)$.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - First, $\min(a'_x, a'_y) \ge \min(b_x, b_y)$ is a deterministic floor: for each pair $(x, y)$, immediately update $a_x \gets \max(a_x, \min(b_x, b_y))$ and $a_y \gets \max(a_y, \min(b_x, b_y))$ and add this mandatory cost to the base answer!
   - Now, for every pair $(x, y)$ with $b_x \le b_y$, we already have $a'_x, a'_y \ge b_x$. The remaining condition is $\max(a'_x, a'_y) \ge b_y$, which is satisfied iff:
     $$a'_y \ge b_y \quad \lor \quad a'_x \ge b_y!$$
   - **Hidden Bipartition Discovery**:
     Classify each wizard $i$ by whether its final value satisfies $a'_i \ge b_i$ or $a'_i < b_i$:
     - Suppose a wizard $y$ ends up with **$a'_y < b_y$** (a "Deficit Wizard"). Then for every neighbor $x$ of $y$ with $b_x \le b_y$, $x$ is **forced** to satisfy $a'_x \ge b_y \ge b_x$!
     - In particular, **two Deficit Wizards can NEVER be adjacent**, and any wizard $x$ that helps a Deficit Wizard $y$ must have $a'_x \ge b_y \ge b_x$ (so $x$ is a "Surplus Wizard" with $a'_x \ge b_x$)!
2. **Step 2: Intermediate Algebraic Representation**:
   For each wizard $i$ and each threshold $t \in \{a_i + 1, \dots, 100\}$:
   - For the **Surplus Range** $t \in [b_i + 1, 100]$, define binary indicator $u_{i, t} = [a'_i \ge t] \in \{0, 1\}$ (cost $1 \cdot u_{i, t}$, chain prerequisite $u_{i, t} \implies u_{i, t-1}$).
   - For the **Deficit Range** $t \in [a_i + 1, b_i]$, define the **flipped** indicator $v_{i, t} = [a'_i < t] = 1 - [a'_i \ge t] \in \{0, 1\}$!
     - Base cost: assume initially every wizard $i$ is raised to at least $\max(a_i, b_i)$ (cost $\max(0, b_i - a_i)$), and for each $t \in [a_i + 1, b_i]$, setting $v_{i, t} = 1$ ($a'_i < t$) **saves $1$ unit of cost** (reward $+1$)!
     - Chain monotonicity: $a'_i < t \implies a'_i < t + 1$, so $v_{i, t} = 1 \implies v_{i, t+1} = 1$ ($\infty \cdot v_{i, t}(1 - v_{i, t+1})$).
     - **Pairwise OR-Constraint**: For an edge $(x, y)$ with $b_x \le b_y$, we cannot have $a'_y < b_y$ ($v_{y, b_y} = 1$) AND $a'_x < b_y$ ($u_{x, b_y} = 0$)!
       In our variables $(v_{y, b_y}, u_{x, b_y})$, the forbidden state is $(v_{y, b_y} = 1 \land u_{x, b_y} = 0)$, which is the pure cut monomial:
       $$\infty \cdot v_{y, b_y}(1 - u_{x, b_y})!$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Preprocess mandatory floors $a_i \gets \max(a_i, \min(b_x, b_y))$.
   - Add $\sum_i \max(0, b_i - a_i)$ to the base cost (pretending every wizard reaches $\max(a_i, b_i)$).
   - For each wizard $i$:
     - Deficit variables $v_{i, t}$ ($a_i < t \le b_i$): add $S \xrightarrow{1} v_{i, t}$ (saving $1$ if $v_{i, t} = 1$), and $v_{i, t} \xrightarrow{\infty} v_{i, t+1}$.
     - Surplus variables $u_{i, t}$ ($\max(a_i, b_i) < t \le 100$): add $u_{i, t} \xrightarrow{1} T$ (paying $1$ if $u_{i, t} = 1$), and $u_{i, t} \xrightarrow{\infty} u_{i, t-1}$.
     - Also if $a_i < b_i$, paying to raise $x$ above $b_x$ requires first reaching $b_x$, so $u_{x, b_x + 1}$ cannot be $1$ if $v_{x, b_x} = 1$: add $v_{x, b_x} \xrightarrow{\infty} u_{x, b_x + 1}$? Wait: if $v_{x, b_x} = 1$ ($a'_x < b_x$) and $u_{x, b_x + 1} = 1$ ($a'_x \ge b_x + 1$), that is $(v = 1, u = 1)$, which is prevented automatically because $u_{x, t}$ is only forced to $1$ when a neighbor has $v_{y, b_y} = 1$, and if $x$ helps $y$ ($b_y \ge b_x$), then $x$ and $y$ also require $\max(a'_x, a'_y) \ge b_y$, so $v_{x, b_x}$ is simultaneously forced to $0$ by adding $v_{y, b_y} \xrightarrow{\infty} T$ if $a'_x < b_x$? Even simpler: for any edge $(x, y)$ with $b_x \le b_y$, having $v_{y, b_y} = 1$ forces $a'_x \ge b_y \ge b_x$, so it forces $v_{x, b_x} = 0$ (which would be $v_{y, b_y} = 1 \land v_{x, b_x} = 1$, impossible since if $v_{y, b_y} = 1$, then $a'_y < b_y$; if $b_x = b_y$, we just add $v_{y, b_y} \to u_{x, b_y}$ where $u_{x, b_x} = 1 - v_{x, b_x}$!).
     - Even cleaner unified indexing: for every wizard $i$ and $t \in [a_i + 1, 100]$, if we never allow two adjacent wizards to both drop below $\max(b_x, b_y)$, then for $(x, y)$ with $b_x \le b_y$:
       - If $a_y < b_y$, having $v_{y, b_y} = 1$ forces $a'_x \ge b_y$, which means $u_{x, b_y} = 1$ (edge $v_{y, b_y} \xrightarrow{\infty} u_{x, b_y}$) AND if $a_x < b_x$, it also forbids $v_{x, b_x} = 1$—wait: since $\min(a'_x, a'_y) \ge \min(b_x, b_y) = b_x$ was **already enforced in Step 1**, we ALREADY have $a_x \ge b_x$ and $a_y \ge b_x$ for every edge $(x, y)$!
       - **READ THAT AGAIN!** Because Step 1 already updated $a_x \gets \max(a_x, \min(b_x, b_y))$ and $a_y \gets \max(a_y, \min(b_x, b_y))$, for every edge $(x, y)$ with $b_x \le b_y$, wizard $x$ **ALREADY satisfies $a_x \ge b_x$**! Thus $x$ has **ZERO** deficit variables $v_{x, t}$! Every wizard $i$ has **either** only deficit variables ($a_i < b_i$, when all its neighbors have $b_j \le a_i < b_i$) **or** only surplus variables ($a_i \ge b_i$)!
   - **Complexity**: $V \le 100 N + 2 \le 10002$, $E \le 100 N + M \le 15000$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Enforce $\min(a'_x, a'_y) \ge \min(b_x, b_y)$ greedily up front by raising $a_x$ and $a_y$ to $\min(b_x, b_y)$.
   - *Hint 2*: After this preprocessing, for any edge $(x, y)$ with $b_x \le b_y$, we already have $a_x \ge b_x$! So $x$ can only go *up* from $b_x$ (surplus), while $y$ decides whether to stop below $b_y$ (deficit) or reach $b_y$!
   - *Hint 3*: Flip the deficit thresholds $v_{y, t} = [a'_y < t]$ so that the OR-clause $a'_y \ge b_y \lor a'_x \ge b_y$ compiles to $v_{y, b_y} \xrightarrow{\infty} u_{x, b_y}$.
   - *Failure Mode*: Skipping the initial $a_i \gets \max(a_i, \min(b_x, b_y))$ preprocessing leaves both deficit and surplus variables active on the same edge, breaking bipartiteness when $b_x = b_y$.

---

#### Problem P21 — `[省选联考 2017] 寿司餐厅` (Sushi Restaurant) `[ZH]`

- **Judge URL**: [https://www.luogu.com.cn/problem/P3749](https://www.luogu.com.cn/problem/P3749) / [https://loj.ac/p/2146](https://loj.ac/p/2146)
- **Statement**: Given $N \le 100$ sushi plates with types $a_1, \dots, a_N \in [1, 1000]$, a binary parameter $m \in \{0, 1\}$, and an upper-triangular matrix of signed scores $d_{l, r} \in [-1000, 1000]$ ($1 \le l \le r \le N$). Selecting interval $[l, r]$ earns $d_{l, r}$ and forces selecting all sub-intervals $[l', r'] \subseteq [l, r]$. Selecting the single plate $[i, i]$ of type $x = a_i$ incurs a per-plate cost of $x$, and if at least one plate of type $x$ is selected, you must also pay a one-time type tax of $m \cdot x^2$. Maximize total net profit.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Combines **Archetype 12.B (Contiguous Interval Pyramid Closure)** on the $\binom{N+1}{2}$ intervals $[l, r]$ with **Archetype 12.A (Shared Infrastructure Closure)** on the distinct sushi types $x \in \{1, \dots, 1000\}$.
2. **Step 2: Intermediate Algebraic Representation**:
   - Binary variable $x_{l, r} \in \{0, 1\}$ for each interval $1 \le l \le r \le N$, with weight $w_{l, r} = d_{l, r}$ (if $l < r$) and $w_{i, i} = d_{i, i} - a_i$ (absorbing the per-plate cost $a_i$ directly into the leaf interval $[i, i]$!).
   - Binary variable $y_c \in \{0, 1\}$ for each sushi type $c \in \{a_1, \dots, a_N\}$, with weight $w_{\text{type}}(c) = -m \cdot c^2$.
   - Pyramid prerequisites: $x_{l, r} = 1 \implies x_{l+1, r} = 1 \land x_{l, r-1} = 1$ (for $l < r$).
   - Type-tax prerequisites: $x_{i, i} = 1 \implies y_{a_i} = 1$.
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Apply Picard's Theorem (Theorem 12.2) to the $\binom{N+1}{2} + |\text{Types}|$ vertices:
     - Positive $w_{l, r} > 0$: add to $R_{\max}$ and add $S \xrightarrow{w_{l,r}} I_{l,r}$.
     - Negative $w_{l, r} < 0$: add $I_{l,r} \xrightarrow{|w_{l,r}|} T$.
     - Pyramid edges ($l < r$): $I_{l, r} \xrightarrow{\infty} I_{l+1, r}$ and $I_{l, r} \xrightarrow{\infty} I_{l, r-1}$.
     - Type-tax edges: $I_{i, i} \xrightarrow{\infty} \text{Type}_{a_i}$ and $\text{Type}_c \xrightarrow{m \cdot c^2} T$.
   - **Complexity**: $V \le 5050 + 1000 + 2 = 6052$, $E \le 3 \times 5050 + 1000 \approx 1.6 \times 10^4$.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: Absorb the linear per-plate cost $-a_i$ directly into the weight of the length-$1$ interval $[i, i]$ ($w_{i,i} = d_{i,i} - a_i$).
   - *Hint 2*: Use the Pyramid Trick ($[l, r] \to [l+1, r]$ and $[l, r] \to [l, r-1]$) so each interval has out-degree $2$ instead of $O(N^2)$.
   - *Hint 3*: Create one node per sushi type $c$ with edge $\text{Type}_c \xrightarrow{m c^2} T$, and point $I_{i, i} \xrightarrow{\infty} \text{Type}_{a_i}$.
   - *Failure Mode*: Subtracting $m \cdot a_i^2$ from every $I_{i, i}$ instead of creating a shared $\text{Type}_c$ node charges the one-time type tax multiple times when several plates have the same type $a_i$!

---

#### Problem P22 — `AtCoder Regular Contest 176, Problem E — Max Vector` `[JA]`

- **Judge URL**: [https://atcoder.jp/contests/arc176/tasks/arc176_e](https://atcoder.jp/contests/arc176/tasks/arc176_e)
- **Statement**: We want to construct $N$ vectors $X_1, \dots, X_N \in \{1, \dots, M\}^D$ and $N$ vectors $Y_1, \dots, Y_N \in \{1, \dots, M\}^D$ ($N, M \le 100$ or general $K$-dimensional coordinates decouple coordinate-by-coordinate!) minimizing the sum of all coordinates of all $X_i$ and $Y_j$, subject to $Q$ constraints of the form: for every coordinate $p$, $\max(X_{i_q, p}, Y_{j_q, p}) \ge A_{q, p}$.

1. **Step 1: Non-Graph Diagnostic Signal**:
   - Notice that both the objective (sum of coordinates) and the constraints ($\max(X_{i, p}, Y_{j, p}) \ge A_{q, p}$ for each coordinate $p$) **decouple completely across the coordinates $p$**!
   - Within a single coordinate (or when vectors are chosen from a finite pool), we have two families of variables—the **$X$-variables ($L$)** and the **$Y$-variables ($R$)**—coupled by disjunctive threshold clauses:
     $$X_i \ge v \quad \lor \quad Y_j \ge v!$$
2. **Step 2: Intermediate Algebraic Representation**:
   - Encode $X_i \in \{1, \dots, M\}$ via unary thresholds $x_{i, v} = [X_i \ge v] \in \{0, 1\}$ for $v \in \{2, \dots, M\}$, with cost $1 \cdot x_{i, v}$ and chain prerequisite $x_{i, v} \implies x_{i, v-1}$ ($\infty \cdot x_{i, v}(1 - x_{i, v-1})$).
   - Encode $Y_j \in \{1, \dots, M\}$ via **bipartite-flipped** unary thresholds $\tilde{y}_{j, v} = [Y_j < v] = 1 - [Y_j \ge v] \in \{0, 1\}$ for $v \in \{2, \dots, M\}$!
     - Cost of $Y_j$: since $Y_j = M - \sum_{v=2}^M \tilde{y}_{j, v}$, paying $1$ when $Y_j \ge v$ ($\tilde{y}_{j, v} = 0$) is literally the unary cut term $1 \cdot (1 - \tilde{y}_{j, v})$ ($S \xrightarrow{1} \tilde{y}_{j, v}$)!
     - Chain monotonicity: $Y_j < v \implies Y_j < v + 1$, so $\tilde{y}_{j, v} \implies \tilde{y}_{j, v+1}$ ($\infty \cdot \tilde{y}_{j, v}(1 - \tilde{y}_{j, v+1})$).
   - **Disjunctive Clause Compilation**:
     The constraint $\max(X_i, Y_j) \ge v$ forbids $(X_i < v \land Y_j < v)$, which in our variables $(x_{i, v}, \tilde{y}_{j, v})$ is $(\tilde{y}_{j, v} = 1 \land x_{i, v} = 0)$, compiled by the single directed cut monomial:
     $$\infty \cdot \tilde{y}_{j, v}(1 - x_{i, v})!$$
3. **Step 3: Reverse-Engineering Scratchpad (Graph Compilation)**:
   - Base cost: $2N \times 1$ (since every entry is $\ge 1$).
   - For each $X_i$ and $v \in \{2, \dots, M\}$: add $x_{i, v} \xrightarrow{1} T$, and $x_{i, v} \xrightarrow{\infty} x_{i, v-1}$.
   - For each $Y_j$ and $v \in \{2, \dots, M\}$: add $S \xrightarrow{1} \tilde{y}_{j, v}$, and $\tilde{y}_{j, v} \xrightarrow{\infty} \tilde{y}_{j, v+1}$.
   - For each constraint $\max(X_i, Y_j) \ge v$ ($v \ge 2$): add $\tilde{y}_{j, v} \xrightarrow{\infty} x_{i, v}$.
   - **Complexity**: $V = 2N(M - 1) + 2$, $E = 4N(M - 1) + Q$; Dinic runs in milliseconds.
4. **Step 4: Progressive 3-Tier Hints & Failure Mode**:
   - *Hint 1*: For two variables $X_i \in L$ and $Y_j \in R$, how do you express $[X_i \ge v \lor Y_j \ge v]$? Its negation is $[X_i < v \land Y_j < v]$.
   - *Hint 2*: Use standard threshold variables $x_{i, v} = [X_i \ge v]$ for $X_i$, and flipped threshold variables $\tilde{y}_{j, v} = [Y_j < v]$ for $Y_j$.
   - *Hint 3*: Watch the chain edge direction on the flipped variables: $[Y_j < v] \implies [Y_j < v + 1]$ points from $v$ to $v + 1$, whereas $[X_i \ge v] \implies [X_i \ge v - 1]$ points from $v$ to $v - 1$!
   - *Failure Mode*: Pointing the chain edges on $\tilde{y}_{j, v}$ from $v$ to $v - 1$ instead of $v \to v + 1$ inverts the monotonicity of $Y_j$!

---

## Quarantined Template Problems Table (`R-01` to `R-08`)

In accordance with `AGENTS.md` and `flows_research/PLAN.md`, bare template verification problems whose sole task is copying a standard Max-Flow / Project Selection routine without non-trivial modelling or algebraic derivation are quarantined from the main practice ladder into the reference table below:

| Quarantine ID | Problem Title & Judge URL | Why Quarantined (Template Classification) |
| :---: | :--- | :--- |
| **`R-01`** | **Library Checker — Project Selection Problem (`燃やす埋める`)** | Direct specification of unary and pairwise submodular tables; pure template verification. |
| **`R-02`** | **Luogu P2762 — `[网络流24题] 太空飞行计划问题` (Space Flight Plan)** | Literal restatement of Picard's bipartite experiment–instrument closure + residual reachability printing. |
| **`R-03`** | **SPOJ `PROFIT` — Maximum Profit** | Identical bare clone of `[NOI2006] 最大获利` (Problem P01) without additional modelling twists. |
| **`R-04`** | **POJ 2987 — `Firing`** | Direct vertex-weighted DAG closure (`最大权闭合子图`) asking for max weight and minimum number of vertices ($S$-minimal cut via scaling $w_v \gets M w_v - 1$). |
| **`R-05`** | **UVa 1389 / LA 3713 — `Hard Life` (Base Closure Step)** | Basic closure subroutine inside Goldberg's Maximum Density Subgraph (covered in full depth in Wave 3A). |
| **`R-06`** | **HDU 3879 — `Base Station`** | Direct translation clone of `[NOI2006] 最大获利`. |
| **`R-07`** | **Luogu P3410 — `拍照` (Taking Photos)** | Isomorphic bipartite project-tool closure clone of `太空飞行计划问题`. |
| **`R-08`** | **Codeforces 103 E — `Buying Sets`** | Direct Max-Weight Closure where $N$ subsets have $|S_i|$ guarantees enabling Hall's Theorem / closure without cycle complications. |

---

## Multilingual `[EN]` / `[ZH]` / `[JA]` Bibliography & Primary Sources

### 1. English (`[EN]`) Combinatorial Optimization & Competitive Programming Sources
1. **Picard, J.-C. (1976)**. *"Maximal Closure of a Graph and Applications to Combinatorial Problems."* Management Science, 22(11), 1268–1272. (The foundational paper proving Theorem 12.2 reducing Maximum Weight Closure / Project Selection to Minimum $S$-$T$ Cut.)
2. **Kolmogorov, V., & Zabih, R. (2004)**. *"What Energy Functions Can Be Minimized via Graph Cuts?"* IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 26(2), 147–159. (Proves the Submodularity Characterization Theorem $A + D \le B + C$ for binary energy functions — Theorem 13.1.)
3. **Boros, E., & Hammer, P. L. (2002)**. *"Pseudo-Boolean Optimization."* Discrete Applied Mathematics, 123(1–3), 155–225. (Comprehensive treatise on quadratic pseudo-Boolean polynomials, roof duality, and bipartite variable transformations.)
4. **Rother, C., Kolmogorov, V., Lempitsky, V., & Szummer, M. (2007)**. *"Optimizing Binary MRFs via Extended Roof Duality (QPBO)."* CVPR 2007. (Establishes the doubled bipartite network for non-submodular functions and strong persistency.)
5. **AtCoder Grand Contest 038 Official English Editorial (2019)**. *"Problem F — Two Permutations."* [https://img.atcoder.jp/agc038/editorial.pdf](https://img.atcoder.jp/agc038/editorial.pdf).

### 2. Chinese (`[ZH]`) National Team Papers (`国家集训队论文`) & Monographs
6. **Hu Botao / 胡伯涛 (Amber, 2007)**. *《最小割模型在信息学竞赛中的应用》 (Applications of Minimum Cut Models in Olympiad in Informatics)*. 2007 Chinese IOI National Training Team Papers (`2007年国家集训队论文`). (The landmark Chinese monograph introducing `最大权闭合子图`, `二元关系最小割`, and zero-auxiliary edge-merging `合并点边法`.)
7. **Wang Wenpeng / 王文鹏 (2016)**. *《浅谈网络流的各种建模方法》 (On Various Network Flow Modelling Methods)*. Chinese National Team / Provincial Selection Lecture Notes.
8. **OI-Wiki Collective (2024)**. *《最小割 / 最大权闭合子图 / 二元关系最小割》*. [https://oi-wiki.org/graph/flow/min-cut/](https://oi-wiki.org/graph/flow/min-cut/).

### 3. Japanese (`[JA]`) `燃やす埋める` / `Project Selection Problem` Treatises
9. **`noshi91` (2021)**. *「燃やす埋める問題について」 (On the Burn-or-Bury Problem).* Hatena Blog, [https://noshi91.hatenablog.com/entry/2021/06/29/044225](https://noshi91.hatenablog.com/entry/2021/06/29/044225). (Systematizes the submodular inequality $A + D \le B + C$, `二部グラフの片側反転` bipartite variable flipping, and $K$-valued extensions.)
10. **`maspypy` (2020–2023)**. *「Project Selection Problem (燃やす埋める) の整理」 & AtCoder AGC038F / ARC107F / ARC142E Editorials.* [https://maspypy.com/](https://maspypy.com/).
11. **`tatyam` (2022)**. *「燃やす埋めるを完全に理解する」 (Completely Understanding Burn-or-Bury).* Qiita / Hatena Blog lecture notes on pseudo-Boolean cut compilation.
12. **`snuke` (Sugim48 / 2019)**. *AtCoder Grand Contest 038 Commentary Broadcast (YouTube).* Live derivation of cycle rigidity and bipartite cut construction for `AGC 038 F — Two Permutations`.
