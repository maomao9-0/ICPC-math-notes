# Cohort 1 — Wave 3A Research Monograph: Fractional Programming Cuts, Maximum Density Subgraphs, Planar Graph Duality, Min-Cut DP & All-Pairs Cut Trees (Iterations 21–25)

> **Cohort & Wave Metadata**
> - **Cohort**: Cohort 1 (Iterations 21–25 of 115+ Redundant Discovery & Audit Pipeline)
> - **Wave**: Wave 3A — *Duality & Structural Cuts: Fractional Programming, Density Subgraphs, Planar Duals, Min-Cut DP & Cut Trees*
> - **Target File**: `flows_research/iter_21_to_25_density_planar_mincut_dp_gomory_hu.md`
> - **Pedagogical Standard**: Strictly follows the **4-Step "Zero Magic Gadgets" Compilation Standard** and **Bidirectional Duality (Direction A: Non-Graph $\to$ Flow; Direction B: Flow $\to$ Non-Flow Fast Algorithm)** defined in `flows_research/PLAN.md` and `AGENTS.md`.
> - **Multilingual Scope**: Exhaustive coverage across English (`[EN]`), Chinese (`[ZH]` — `国家集训队论文`, Amber/胡伯涛 2007, NOI/WC/Provincial Selection), and Japanese (`[JA]` — `燃やす埋める`, AtCoder `AGC`/`ARC`/`ABC`).

---

## Executive Overview: The Two Axes of Structural Cut Duality

Waves 2A and 2B established the core **Direction A (Non-Graph $\to$ Flow)** pipeline: compiling binary indicator choices $x_i \in \{0,1\}$, $k$-ary ordered threshold chains, and submodular penalties into standard $s$-$t$ minimum cuts. Wave 3A expands this theory along two orthogonal axes that separate routine flow practitioners from grandmaster problem solvers:

1. **Non-Linear & Multi-Query Cut Structures (Iterations 21, 22, 25)**:
   - What happens when the objective is not a linear sum $\sum c_e x_u(1 - x_v)$, but a **ratio of two cut/closure functions** $\frac{N(S)}{D(S)}$? **Iteration 21** develops **0-1 Fractional Programming over Minimum Cuts** via parametric linearization $h(\lambda) = \min_S (N(S) - \lambda D(S))$ and **Dinkelbach's Newton-Secant Iteration**.
   - What if we seek the **Maximum Density Subgraph** $\max_{\emptyset \neq S \subseteq V} \frac{|E(S)|}{|S|}$, where the naive closure graph has $O(|V| + |E|) = O(|V|^2)$ vertices? **Iteration 22** derives **Goldberg's (1984) and Amber's (2007) Degree-Identity Reduction**, using $2|E(S)| = \sum_{v \in S} \deg(v) - |\delta(S, \bar{S})|$ to eliminate all $|E|$ edge-nodes and compile the parametric cut onto **only $|V| + 2$ vertices**.
   - What if we need the minimum cut not for one fixed $(s, t)$ pair, but globally across the entire graph or across **all $\binom{N}{2}$ vertex pairs**? **Iteration 25** develops the **Stoer–Wagner Global Minimum Cut** algorithm ($O(VE + V^2 \log V)$ without flow) and **Gomory–Hu / Gusfield Cut Trees (`最小割树`)**, proving that all $\binom{N}{2}$ pairwise minimum cuts are encoded by a single weighted tree $T_{\text{GH}}$ constructed in just $N - 1$ invocations of Max-Flow.

2. **Direction B — Eliminating the Flow Solver via Duality (Iterations 23, 24)**:
   - When $V, E \le 10^6$ on a planar graph or grid, or when $N \le 10^5$ on a structured dense graph, running Dinic's algorithm is orders of magnitude too slow.
   - **Iteration 23** exploits **Planar Graph Duality ($G \leftrightarrow G^*$)**: an $s$-$t$ minimum cut in a primal planar graph is a minimum-weight cycle separating $s$ and $t$ in the dual graph $G^*$, which collapses to a single $O(V \log V)$ **Dijkstra Shortest Path** when $s$ and $t$ lie on the outer face (`[BJWC2006] 狼抓兔子`). Going one level deeper, we study **`[NOI2010] 海拔` (Altitude)**, where a continuous real-valued potential optimization problem on a directed grid is first reduced via the **Coarea Formula / LP Extreme-Point Theorem** to a binary $\{0,1\}$ $s$-$t$ planar minimum cut, and then solved via **Directed Dual Dijkstra**.
   - **Iteration 24** introduces **Solving Max-Flow via Min-Cut DP / Greedy (`最大流转最小割 DP`)**: when a problem is explicitly or implicitly a Max-Flow problem on $N \le 10^4\text{--}10^5$ vertices (such as `CF 724 E — Goods Transportation` or `[BZOJ 2039] 人员雇佣`), we invoke the Max-Flow Min-Cut Theorem not to build a flow network, but to rewrite the answer as a binary partition $x_i \in \{S, T\}$ and optimize that partition directly via **Dynamic Programming, Slope Trick, or Greedy** in $O(N^2)$ or $O(N \log N)$ time.

---

## Iteration 21: 0-1 Fractional Programming + Minimum Cut (`分数规划最小割` & Dinkelbach's Algorithm)

### 1. Step 1: The Non-Graph Diagnostic Signal (Recognition)

#### Surface Clues in Problem Statements
You are looking at a **0-1 Fractional Programming Minimum Cut (or Maximum Closure)** problem whenever the problem asks you to select a non-empty subset of items/vertices/projects $S \subseteq V$ (or an $s$-$t$ cut partition $(S, \bar{S})$) to **minimize or maximize a quotient**:
$$\min_{S \in \mathcal{F}} \frac{N(S)}{D(S)} \quad \text{or} \quad \max_{S \in \mathcal{F}} \frac{P(S)}{C(S)},$$
where:
- The denominator $D(S) > 0$ (or $C(S) > 0$) is a strictly positive modular or submodular weight function on the chosen set $S$ (e.g., $\sum_{v \in S} b_v + \sum_{e \in \delta(S)} d_e > 0$).
- If the numerator and denominator were combined *linearly* as $N(S) - \lambda D(S)$ for a fixed constant $\lambda \in \mathbb{R}$, the resulting optimization problem would be recognizable as an $s$-$t$ Minimum Cut, Maximum Weight Closure (`最大权闭合子图`), or Project Selection (`燃やす埋める`) problem.
- Typical constraint bounds are $N, M \le 500\text{--}2000$ (small enough for $O(\log(\frac{1}{\epsilon}))$ or $10\text{--}35$ calls to Dinic's algorithm).

#### Why Naive DP and Greedy Fail
1. **Failure of Greedy Ratio Sorting**: In unconstrained 0-1 fractional knapsack without dependencies, sorting items by individual ratio $p_i / c_i$ works. Here, items are coupled by **implication constraints** ($u \in S \implies v \in S$), **pairwise synergy/penalty edges** ($u, v \in S$ yields bonus $w_{uv}$, or $u \in S, v \notin S$ incurs cut penalty $c_{uv}$). A vertex $u$ may have a terrible standalone ratio $p_u / c_u = 0$, yet be a mandatory prerequisite for ten high-profit projects.
2. **Failure of Standard DP**: Even when we only want a subset $S$, the dependency graph may be an arbitrary DAG or general graph with high treewidth, and tracking both numerator $N(S)$ and denominator $D(S)$ in the DP state blows up the state space by $O(\sum b_v)$, which is infeasible when weights are up to $10^9$ or when the dependency graph is not a tree.

#### Crucial Contrast: Minimum Mean-Weight Cycle vs. Minimum Ratio Cut / Closure
Beginners frequently confuse two classic fractional graph problems. Distinguishing them immediately saves hours during a contest:

| Feature | Minimum Mean-Weight Directed Cycle (`[HNOI2009] 最小圈`) | Minimum Ratio Cut / Maximum Ratio Closure (`分数规划最小割`) |
| :--- | :--- | :--- |
| **Chosen Object** | A single simple directed cycle $C$ in a directed graph | A vertex subset $S \subseteq V$ (cut $(S, \bar{S})$ or closed set) |
| **Parametric Subproblem $w_\lambda(e) = w(e) - \lambda c(e)$** | Does $G$ contain a **negative-weight directed cycle**? | What is the **Minimum $s$-$t$ Cut** (or Max Weight Closure)? |
| **Subproblem Oracle** | Bellman–Ford / SPFA negative cycle detection or Karp's $O(VE)$ algorithm | Dinic's Max-Flow / Min-Cut algorithm |
| **Can $w_\lambda(e)$ be negative?** | Yes! Negative edge weights are native to Bellman–Ford. | **No!** Standard $s$-$t$ Min-Cut requires **non-negative edge capacities**. Negative vertex/edge terms must be algebraically shifted or split between source $s$ and sink $t$. |

---

### 2. Step 2: The Algebraic / Logical Intermediate Representation

Let $\mathcal{F}$ be a finite family of feasible binary indicator vectors $x \in \{0, 1\}^V$ (for instance, all valid $s$-$t$ cuts with $x_s = 1, x_t = 0$, or all non-empty subsets $S \neq \emptyset$). Suppose we wish to solve the **Min-Ratio Problem**:
$$\lambda^* = \min_{x \in \mathcal{F}} \frac{N(x)}{D(x)}, \quad \text{where } D(x) > 0 \text{ for all } x \in \mathcal{F}.$$
*(Note: A Max-Ratio problem $\max_{x \in \mathcal{F}} \frac{P(x)}{C(x)}$ with $C(x) > 0$ is identically handled either by defining $g(\lambda) = \max_{x \in \mathcal{F}} (P(x) - \lambda C(x))$ or by negating $N(x) = -P(x)$ to convert maximization into minimization: $\max_{x \in \mathcal{F}} (P(x) - \lambda C(x)) = -\min_{x \in \mathcal{F}} (\lambda C(x) - P(x))$.)*

For any real trial parameter $\lambda \in \mathbb{R}$, define the **Parametric Auxiliary Function**:
$$h(\lambda) := \min_{x \in \mathcal{F}} \big( N(x) - \lambda D(x) \big).$$

#### Theorem 21.1 (Structural Properties of the Parametric Function $h(\lambda)$)
Assume $\mathcal{F}$ is finite and non-empty, and $D(x) > 0$ for every $x \in \mathcal{F}$. Then:
1. **Piecewise-Linear, Continuous, and Concave**: For each fixed $x \in \mathcal{F}$, the map $\lambda \mapsto N(x) - \lambda D(x)$ is an affine line with strictly negative slope $-D(x) < 0$. Because $h(\lambda)$ is the pointwise minimum of finitely many affine functions, $h(\lambda)$ is continuous, concave, and piecewise-linear on $\mathbb{R}$.
2. **Strictly Decreasing**: If $\lambda_1 < \lambda_2$, let $x_1 \in \arg\min_{x \in \mathcal{F}} (N(x) - \lambda_1 D(x))$. Since $D(x_1) > 0$, we have:
   $$h(\lambda_2) = \min_{x \in \mathcal{F}} \big(N(x) - \lambda_2 D(x)\big) \le N(x_1) - \lambda_2 D(x_1) < N(x_1) - \lambda_1 D(x_1) = h(\lambda_1).$$
3. **Unique Root Equivalence (Dinkelbach's Criterion)**: Since $D(x) > 0$ for all $x \in \mathcal{F}$, for every $x \in \mathcal{F}$ we may divide $N(x) - \lambda D(x)$ by $D(x)$ without reversing the inequality sign:
   $$\begin{aligned}
   h(\lambda) \ge 0 &\iff \forall x \in \mathcal{F},\; N(x) - \lambda D(x) \ge 0 \iff \forall x \in \mathcal{F},\; \frac{N(x)}{D(x)} \ge \lambda \iff \lambda \le \lambda^*, \\
   h(\lambda) = 0 &\iff \min_{x \in \mathcal{F}} \big(N(x) - \lambda D(x)\big) = 0 \iff \lambda = \lambda^*, \\
   h(\lambda) < 0 &\iff \exists x \in \mathcal{F},\; N(x) - \lambda D(x) < 0 \iff \exists x \in \mathcal{F},\; \frac{N(x)}{D(x)} < \lambda \iff \lambda > \lambda^*.
   \end{aligned}$$

```
       h(λ)
        ^
        | \
        |   \   Slope = -D(x_1)
        |     \
        |       * (Corner where optimal cut x_1 transitions to x_2)
        |         \
  ------+-----------*---------------------> λ
        |           ^  \  Slope = -D(x_2)
        |         λ = λ* \
        |                  \
```

#### Exact Binary Search Termination Gap Analysis
When $N(x)$ and $D(x)$ are integers for all $x \in \mathcal{F}$, let $D_{\max} = \max_{x \in \mathcal{F}} D(x)$. Any two distinct candidate ratios $\frac{N(x_1)}{D(x_1)} \neq \frac{N(x_2)}{D(x_2)}$ are separated by at least:
$$\left| \frac{N(x_1)}{D(x_1)} - \frac{N(x_2)}{D(x_2)} \right| = \frac{|N(x_1) D(x_2) - N(x_2) D(x_1)|}{D(x_1) D(x_2)} \ge \frac{1}{D(x_1) D(x_2)} \ge \frac{1}{D_{\max}^2}.$$
- **Case 1: Only the floating-point value of $\lambda^*$ to precision $10^{-k}$ is required**: Binary search terminates in $\lceil \log_2((R - L) \cdot 10^k) \rceil$ iterations (typically $45\text{--}60$ iterations).
- **Case 2: The exact optimal subset $x^*$ or exact rational fraction $p/q$ is required**: Set the binary search tolerance to $\epsilon = \frac{1}{2 D_{\max}^2}$. If we test $\lambda$ and keep track of the best ratio $\frac{N(x)}{D(x)}$ found so far, or if we stop once $R - L < \frac{1}{D_{\max}^2}$, the unique rational with denominator $\le D_{\max}$ in the interval is guaranteed to be identified.

#### Dinkelbach's Algorithm (Newton-Raphson / Secant Iteration on $h(\lambda)$)
Instead of blind interval bisection, **Dinkelbach's algorithm (1967)** exploits the concavity of $h(\lambda)$ by applying Newton's method from the right ($\lambda_k \ge \lambda^*$).
1. Initialize with any feasible solution $x_0 \in \mathcal{F}$ and set $\lambda_0 = \frac{N(x_0)}{D(x_0)} \ge \lambda^*$.
2. In iteration $k = 0, 1, 2, \dots$:
   - Solve the parametric min-cut oracle to obtain an actual minimizer $x_{k+1} \in \arg\min_{x \in \mathcal{F}} \big(N(x) - \lambda_k D(x)\big)$.
   - Compute $h(\lambda_k) = N(x_{k+1}) - \lambda_k D(x_{k+1})$.
   - If $h(\lambda_k) = 0$ (or $|h(\lambda_k)| < \epsilon$), halt and return $\lambda_k$ and $x_k$.
   - Otherwise, $h(\lambda_k) < 0$. The supporting line to $h(\lambda)$ at $\lambda_k$ is $L_k(\lambda) = N(x_{k+1}) - \lambda D(x_{k+1})$, whose root $L_k(\lambda) = 0$ is precisely:
     $$\lambda_{k+1} := \frac{N(x_{k+1})}{D(x_{k+1})} = \lambda_k + \frac{h(\lambda_k)}{D(x_{k+1})} < \lambda_k.$$

**Proposition 21.2 (Superlinear Convergence of Dinkelbach's Iteration)**:
At every step $k$ before termination, $\lambda^* \le \lambda_{k+1} < \lambda_k$ and $D(x_{k+1}) \ge D(x^*)$ is not required—rather, because $h(\lambda^*) = 0 \le N(x_{k+1}) - \lambda^* D(x_{k+1})$ and $N(x^*) - \lambda_k D(x^*) \ge N(x_{k+1}) - \lambda_k D(x_{k+1})$, subtracting gives:
$$\frac{\lambda_{k+1} - \lambda^*}{\lambda_k - \lambda^*} = 1 - \frac{N(x_{k+1}) - \lambda_k D(x_{k+1})}{(\lambda^* - \lambda_k) D(x_{k+1})} \le 1 - \frac{D(x^*)}{D(x_{k+1})}.$$
Moreover, if $D(x)$ takes integer values in $\{1, \dots, D_{\max}\}$, $D(x_{k+1})$ is strictly increasing whenever $\lambda_{k+1}$ does not halve the gap, yielding **strongly polynomial termination** in $O(|V|^2 \log |V|)$ oracle calls (Radzik, 1998) and typically **5 to 12 Dinic calls** in practice—$5\times$ faster than binary search!

---

### 3. Step 3: The Reverse-Engineering Scratchpad (Graph Compilation)

Suppose we have fixed a trial parameter $\lambda \in \mathbb{R}$. How do we compile $h(\lambda) = \min_{x \in \mathcal{F}} \big(N(x) - \lambda D(x)\big)$ into a standard non-negative-capacity $s$-$t$ Min-Cut graph?

Let us write out the general Pseudo-Boolean polynomial for $N(x) - \lambda D(x)$ across the two most common competitive programming templates:

#### Archetype 21A: Minimum Ratio $s$-$t$ Cut (`最小比率割` — e.g., `[TJOI2012] 桥`)
We are given a directed or undirected graph $G = (V, E)$ with source $s$, sink $t$, edge cut penalty $a_e \ge 0$, and edge denominator weight $b_e > 0$. We want an $s$-$t$ cut $(S, \bar{S})$ minimizing:
$$\frac{\sum_{e \in \delta^+(S)} a_e}{\sum_{e \in \delta^+(S)} b_e}.$$
For a fixed $\lambda \ge 0$, each edge $e = (u, v)$ has parametric weight:
$$w_\lambda(e) = a_e - \lambda b_e.$$
**Wait!** What if $w_\lambda(e) < 0$ for some edge $e$? Can we pass a negative capacity to Dinic's algorithm? **Never!**
Here is the exact algebraic split (**"0-1 Cut Sign Splitting"**):
- If $w_\lambda(e) = a_e - \lambda b_e > 0$: We only pay $w_\lambda(e)$ if $e \in \delta^+(S)$ (i.e., $x_u = 1, x_v = 0$). So we add the directed edge $u \to v$ with capacity $c_\lambda(u \to v) = a_e - \lambda b_e > 0$.
- If $w_\lambda(e) = a_e - \lambda b_e \le 0$: Since any edge with negative weight is **beneficial** to cut, and any cycle-free / minimal cut can always include $e$ (or in undirected network cut reductions where any subset of negative edges can be severed to disconnect $G$, or if $e$ is a mandatory negative-weight cut edge), wait: in **Minimum Ratio Spanning / Network Disconnection** (often called `0-1 Fractional Cut` in Chinese contests), if cutting an edge $e$ is optional (any superset of an $s$-$t$ cut is allowed), then every edge with $w_\lambda(e) \le 0$ is **unconditionally cut**, contributing $w_\lambda(e)$ to a constant accumulator `neg_sum`, and its capacity in the graph is set to $0$!
- What if $e \in \delta^+(S)$ is strictly defined by vertex partition $x_u = 1, x_v = 0$ (you *cannot* cut an edge if both endpoints remain in $S$ or both in $\bar{S}$)? Then $w_\lambda(e) x_u (1 - x_v)$ with $w_\lambda(e) < 0$ is **supermodular**! Therefore, in strict vertex-partition $s$-$t$ ratio cut, either:
  1. The denominator lives on **vertices** $D(S) = \sum_{v \in S} b_v$ (so all cut edges $u \to v$ retain non-negative capacity $a_e \ge 0$), OR
  2. The denominator lives on cut edges, and the problem allows cutting any edge set $F \subseteq E$ that disconnects $s$ and $t$ (so negative edges $a_e - \lambda b_e \le 0$ are greedily severed).

#### Archetype 21B: Maximum Ratio Closure (`最大比率闭合子图` — Ratio Project Selection)
Each vertex $v \in V$ has profit $p_v \ge 0$ and cost $c_v \ge 0$ (not both zero), and dependencies $u \to v$ require $x_u \le x_v$ ($u \in S \implies v \in S$). We want to maximize $\frac{\sum_{v \in S} p_v}{\sum_{v \in S} c_v}$ over non-empty closed subsets $S \subseteq V$.
1. Fix $\lambda > 0$. Each vertex $v$ gets net parametric weight:
   $$w_v(\lambda) := p_v - \lambda c_v.$$
2. Notice that $w_v(\lambda)$ can change sign as $\lambda$ varies! We split vertices dynamically inside the oracle for each $\lambda$:
   - Let $V^+(\lambda) = \{ v \in V : w_v(\lambda) > 0 \}$ and $V^-(\lambda) = \{ v \in V : w_v(\lambda) \le 0 \}$.
   - Rewrite the maximization objective as a minimization cut polynomial ($x_v = 1 \iff v \in S$, $x_s = 1, x_t = 0$):
     $$\max_{x} \sum_{v \in V} w_v(\lambda) x_v = \sum_{v \in V^+(\lambda)} w_v(\lambda) - \min_{x} \left( \sum_{v \in V^+(\lambda)} w_v(\lambda) x_s(1 - x_v) + \sum_{v \in V^-(\lambda)} |w_v(\lambda)| x_v(1 - x_t) + \sum_{(u,v) \in E_{\text{dep}}} \infty \cdot x_u(1 - x_v) \right).$$
3. **Compiled Network for Trial $\lambda$**:
   - For each $v \in V$ with $p_v - \lambda c_v > 0$: add edge $s \to v$ with capacity $p_v - \lambda c_v$.
   - For each $v \in V$ with $p_v - \lambda c_v \le 0$: add edge $v \to t$ with capacity $\lambda c_v - p_v \ge 0$.
   - For each dependency $(u, v) \in E_{\text{dep}}$ ($u \in S \implies v \in S$): add edge $u \to v$ with capacity $\infty$.
   - Then $g(\lambda) = \max_{S} \sum_{v \in S} (p_v - \lambda c_v) = \sum_{v \in V^+(\lambda)} (p_v - \lambda c_v) - \text{MinCut}(\lambda)$.

---

### 4. Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Concrete Numerical Trace ($N = 3$ Projects with Dependencies)
Consider 3 vertices with profits $p = [10, 8, 2]$, costs $c = [2, 1, 5]$, and dependencies $1 \to 3$ and $2 \to 3$ (choosing project 1 or 2 requires paying for infrastructure 3).
- Valid non-empty closed sets $S$:
  - $S_1 = \{3\}$: ratio $\frac{2}{5} = 0.4$.
  - $S_2 = \{1, 3\}$: ratio $\frac{10+2}{2+5} = \frac{12}{7} \approx 1.714$.
  - $S_3 = \{2, 3\}$: ratio $\frac{8+2}{1+5} = \frac{10}{6} \approx 1.667$.
  - $S_4 = \{1, 2, 3\}$: ratio $\frac{10+8+2}{2+1+5} = \frac{20}{8} = 2.5$.
- **Trace of Dinkelbach's Algorithm**:
  - **Init**: Start with $S_0 = \{3\}$, so $\lambda_0 = \frac{2}{5} = 0.4$.
  - **Step 1 ($\lambda_0 = 0.4$)**:
    - Net weights $w(\lambda_0) = p - 0.4 c = [10 - 0.8, 8 - 0.4, 2 - 2.0] = [+9.2, +7.6, 0.0]$.
    - Graph capacities: $s \to 1$ ($9.2$), $s \to 2$ ($7.6$), $3 \to t$ ($0.0$), $1 \to 3$ ($\infty$), $2 \to 3$ ($\infty$).
    - Min-Cut severs $3 \to t$ with cost $0.0$, so $S^* = \{1, 2, 3\}$ and $g(0.4) = (9.2 + 7.6) - 0 = +16.8 > 0$.
    - Secant update: $\lambda_1 = \frac{p(S^*)}{c(S^*)} = \frac{20}{8} = 2.5$.
  - **Step 2 ($\lambda_1 = 2.5$)**:
    - Net weights $w(\lambda_1) = p - 2.5 c = [10 - 5, 8 - 2.5, 2 - 12.5] = [+5.0, +5.5, -10.5]$.
    - Graph capacities: $s \to 1$ ($5.0$), $s \to 2$ ($5.5$), $3 \to t$ ($10.5$), $1 \to 3$ ($\infty$), $2 \to 3$ ($\infty$).
    - Total positive weight $= 5.0 + 5.5 = 10.5$.
    - Min-Cut can either sever $(s \to 1, s \to 2)$ for $10.5$ or sever $(3 \to t)$ for $10.5$. Thus $\text{MinCut}(2.5) = 10.5$, and $g(2.5) = 10.5 - 10.5 = 0$!
    - **Terminated in 2 steps!** (Compare with 50 iterations of binary search.)

#### Broken Gadget Counterexamples & Subtle Traps
1. **The $S = \emptyset$ Zero-Over-Zero Trap**:
   In Archetype 21B, $S = \emptyset$ is always a valid closed set with $\sum_{v \in \emptyset} (p_v - \lambda c_v) = 0$.
   - *What breaks*: If the true maximum ratio over non-empty sets $S \neq \emptyset$ were negative (because all projects have $p_v < 0$), or if we test $\lambda > \lambda^*$, then for every non-empty closed set $S \neq \emptyset$ we have $P(S) - \lambda C(S) < 0$. The min-cut oracle will then sever all $s \to v$ edges, choosing $S = \emptyset$ and returning $g(\lambda) = 0$ instead of a negative number!
   - *How to handle it*: For $\lambda < \lambda^*$, there exists $S \neq \emptyset$ with $P(S) - \lambda C(S) > 0$, so $g(\lambda) > 0$ (strictly positive!). For $\lambda \ge \lambda^*$, $\max_{S \neq \emptyset} (P(S) - \lambda C(S)) \le 0$, so the oracle returns $g(\lambda) = 0$ (achieved by $S = \emptyset$). Thus the binary search predicate MUST be **`g(λ) > EPS`** (strictly positive), never `g(λ) >= 0`!
2. **Keeping Fixed $s \to v$ / $v \to t$ Edges Across $\lambda$**:
   - *What breaks*: A common mistake is to connect $s \to v$ with capacity $p_v$ and $v \to t$ with capacity $\lambda c_v$ simultaneously. If you put *both* $s \to v$ (cap $p_v$) and $v \to t$ (cap $\lambda c_v$) on vertex $v$, then every cut must sever at least one of them, paying $\min(p_v, \lambda c_v)$ unconditionally! That adds a spurious baseline $\sum_v \min(p_v, \lambda c_v)$ that you MUST subtract out—or, much cleaner, combine them into $w_v(\lambda) = p_v - \lambda c_v$ first and attach only one edge ($s \to v$ if $w_v > 0$, or $v \to t$ if $w_v < 0$).

---

## Iteration 22: Maximum Density Subgraph (`最大密度子图` — Goldberg's Reduction & Amber's 2007 Monograph)

### 1. Step 1: The Non-Graph Diagnostic Signal (Recognition)

#### Surface Clues in Problem Statements
Given an undirected graph $G = (V, E)$ (possibly with edge weights $w_e > 0$ and vertex weights/profits $p_v$ and vertex costs $c_v > 0$), find a **non-empty vertex subset** $\emptyset \neq S \subseteq V$ that maximizes the **induced density**:
$$D(S) = \frac{|E(S)|}{|S|} \quad \text{or more generally} \quad D(S) = \frac{\sum_{e \in E(S)} w_e + \sum_{v \in S} p_v}{\sum_{v \in S} c_v},$$
where $E(S) = \{ (u, v) \in E : u \in S \text{ and } v \in S \}$ is the set of edges with **both** endpoints inside $S$.
- **Disguised Non-Graph Forms**:
  - *"Select a non-empty group of employees $S$ to maximize average synergy $\frac{\sum_{\{u,v\} \subseteq S} s_{uv}}{|S|}$."*
  - *"Find a submatrix / subset of rows and columns maximizing ones per selected line."*
  - *"Test whether a graph is arboricity-bounded / $k$-forest decomposable"* (by Nash-Williams' Theorem, $G$ decomposes into $k$ forests iff $\max_{\emptyset \neq S \subseteq V, |S| \ge 2} \frac{|E(S)|}{|S| - 1} \le k$).

#### Why Greedy Peeling Fails (Charikar's 2-Approximation Counterexample)
A tempting greedy algorithm (Charikar, 2000) repeatedly deletes the vertex of minimum current degree in $S$ and records the best subgraph seen. While this is a famous $2$-approximation, it **fails to find the exact optimum**:
- **Counterexample**: Let $G$ be the disjoint union of $G_1 = K_{d, d}$ ($2d$ vertices, $d^2$ edges, every vertex has degree $d$, density $\frac{d^2}{2d} = \frac{d}{2}$) and $G_2 = K_{d+2}$ ($d+2$ vertices, $\binom{d+2}{2}$ edges, every vertex has degree $d+1$, density $\frac{d+1}{2}$). Now add a large star or slightly perturb weights so vertices of $G_2$ have lower total degree than vertices of $G_1$ connected to external leaves: greedy peeling peels away vertices of $G_2$ first because their initial degree is $d+1$, whereas vertices in $G_1$ have $d$ internal edges plus 2 pendant leaves (initial degree $d+2$, density $\frac{d^2 + 4d}{6d} \ll \frac{d+1}{2}$). Once a single vertex of $G_2 = K_{d+2}$ is peeled, $G_2$'s degrees drop to $d$ and the entire clique $K_{d+2}$ unravels and is destroyed before the leaves of $G_1$ are ever touched!

---

### 2. Step 2: The Algebraic / Logical Intermediate Representation

Applying Iteration 21 (0-1 Fractional Programming), we fix a trial density $\lambda \ge 0$ and ask whether there exists a non-empty subset $\emptyset \neq S \subseteq V$ such that:
$$f_\lambda(S) := \sum_{e=(u,v) \in E} w_e x_u x_v + \sum_{v \in V} p_v x_v - \lambda \sum_{v \in V} c_v x_v > 0,$$
where $x_v = [v \in S] \in \{0, 1\}$.

How do we maximize $f_\lambda(x)$ over $x \in \{0, 1\}^V$? There are **two fundamentally different algebraic compilations**, and understanding why the second is vastly superior when $|E| \gg |V|$ is the central lesson of **Goldberg (1984)** and **Amber / 胡伯涛's 2007 Chinese National Team Monograph (`《最小割模型在信息学竞赛中的应用》`)**.

#### Compilation Method 1: Bipartite Edge-Vertex Closure (`|V| + |E| + 2` Vertices)
Treat each edge $e = (u, v) \in E$ as a project with profit $+w_e > 0$ and indicator variable $y_e \in \{0, 1\}$, subject to the prerequisite constraints $y_e \le x_u$ and $y_e \le x_v$, while each vertex $v \in V$ has net cost $\lambda c_v - p_v$:
$$\max_{x, y} \left( \sum_{e \in E} w_e y_e - \sum_{v \in V} (\lambda c_v - p_v) x_v \right) \quad \text{s.t. } y_e (1 - x_u) = 0,\; y_e (1 - x_v) = 0.$$
- **Graph Size**: $|V| + |E| + 2$ vertices and $3|E| + |V|$ directed edges.
- **Bottleneck**: When $G$ is dense ($|E| = \Theta(|V|^2)$, e.g., $|V| = 1000, |E| = 5 \times 10^5$), the closure network has $5 \times 10^5$ vertices! Running Dinic 40 times on $5 \times 10^5$ vertices will TLE.

#### Compilation Method 2: Goldberg's Degree-Identity Reduction (`|V| + 2` Vertices Only!)
Can we eliminate the quadratic product $x_u x_v$ **without introducing any auxiliary edge-vertices $y_e$**?
Yes! Let $\deg_w(v) := \sum_{e \ni v} w_e$ be the weighted degree of vertex $v$ in $G$. Sum $\deg_w(v)$ over all $v \in S$:
- Every internal edge $e = (u, v) \in E(S)$ has *both* endpoints in $S$, so $w_e$ is counted **twice** in $\sum_{v \in S} \deg_w(v)$.
- Every boundary (cut) edge $e = (u, v) \in \delta(S, \bar{S})$ has *exactly one* endpoint in $S$, so $w_e$ is counted **once** in $\sum_{v \in S} \deg_w(v)$.
- Every external edge $e \in E(\bar{S})$ is counted **zero** times.

This yields **Goldberg's Fundamental Degree-Cut Identity**:
$$\sum_{v \in S} \deg_w(v) = 2 W(E(S)) + W(\delta(S, \bar{S})) \quad \Longleftrightarrow \quad W(E(S)) = \frac{1}{2} \sum_{v \in S} \deg_w(v) - \frac{1}{2} W(\delta(S, \bar{S})).$$
*(Algebraically, for every edge $(u,v)$, this is the identity $x_u x_v = \frac{1}{2} x_u + \frac{1}{2} x_v - \frac{1}{2}\big(x_u(1 - x_v) + x_v(1 - x_u)\big)$!)*

Now substitute this directly into $f_\lambda(S) = W(E(S)) + \sum_{v \in S} p_v - \lambda \sum_{v \in S} c_v$:
$$\begin{aligned}
f_\lambda(S) &= \frac{1}{2} \sum_{v \in S} \deg_w(v) - \frac{1}{2} W(\delta(S, \bar{S})) + \sum_{v \in S} p_v - \lambda \sum_{v \in S} c_v \\
&= -\frac{1}{2} \left( W(\delta(S, \bar{S})) + \sum_{v \in S} \big( 2\lambda c_v - 2p_v - \deg_w(v) \big) \right).
\end{aligned}$$
Therefore, **maximizing $f_\lambda(S)$ is equivalent to minimizing**:
$$J_\lambda(S) := -2 f_\lambda(S) = \underbrace{\sum_{(u,v) \in E} w_{uv} \big( x_u(1 - x_v) + x_v(1 - x_u) \big)}_{W(\delta(S, \bar{S}))} + \sum_{v \in V} \big( 2\lambda c_v - 2p_v - \deg_w(v) \big) x_v.$$
Look at $J_\lambda(S)$: the pairwise term $W(\delta(S, \bar{S}))$ uses **only the original vertices $V$ and original edges $E$**! Every auxiliary edge-vertex has vanished!

---

### 3. Step 3: The Reverse-Engineering Scratchpad (Graph Compilation & The $U$-Shift Trick)

To compile $\min_{S \subseteq V} J_\lambda(S)$ into an $s$-$t$ Min-Cut on vertex set $V \cup \{s, t\}$, let $x_v = 1$ mean $v \in S$ ($s$-side of the cut) and $x_v = 0$ mean $v \in \bar{S}$ ($t$-side of the cut).
Notice that the coefficient of $x_v$ in $J_\lambda(S)$ is:
$$\alpha_v(\lambda) := 2\lambda c_v - 2p_v - \deg_w(v),$$
which can be **negative** when $\lambda$ is small!
We have two equivalent ways to compile $\sum_{v \in V} \alpha_v(\lambda) x_v$ with non-negative capacities:

#### Approach 1: Amber's Uniform $U$-Shift Construction (Standard in `[ZH]` Literature)
Choose a constant $U$ large enough that $U + \alpha_v(\lambda) \ge 0$ for all $v \in V$; specifically:
$$U := \max_{v \in V} \big( \deg_w(v) + 2p_v \big).$$
Since $\lambda \ge 0$ and $c_v \ge 0$, we are guaranteed that $U + 2\lambda c_v - 2p_v - \deg_w(v) \ge 0$ for every $\lambda \ge 0$ and every $v \in V$!
Now add $U |V| = \sum_{v \in V} U (1 - x_v) + \sum_{v \in V} U x_v$ to $J_\lambda(S)$:
$$U |V| + J_\lambda(S) = \sum_{v \in V} \underbrace{U}_{c(s \to v)} x_s (1 - x_v) + \sum_{v \in V} \underbrace{\big( U + 2\lambda c_v - 2p_v - \deg_w(v) \big)}_{c(v \to t) \ge 0} x_v (1 - x_t) + \sum_{(u,v) \in E} \underbrace{w_{uv}}_{c(u \leftrightarrow v)} \big( x_u(1 - x_v) + x_v(1 - x_u) \big).$$

**Compiled Goldberg–Amber Network $G_\lambda = (V \cup \{s, t\}, E_\lambda)$**:
1. **Source-to-Vertex Edges**: For every $v \in V$, add a directed edge $s \to v$ with capacity $c(s \to v) = U$. (If $v \notin S$, i.e., $x_v = 0$, this edge is cut.)
2. **Vertex-to-Sink Edges**: For every $v \in V$, add a directed edge $v \to t$ with capacity $c(v \to t) = U + 2\lambda c_v - 2p_v - \deg_w(v) \ge 0$. (If $v \in S$, i.e., $x_v = 1$, this edge is cut.)
3. **Internal Undirected Graph Edges**: For every undirected edge $e = (u, v) \in E$, add two directed edges $u \to v$ and $v \to u$, each with capacity $w_e$. (Or a single undirected edge of capacity $w_e$ in Dinic.)

**Cut Capacity Verification**:
For any partition $(S \cup \{s\}, \bar{S} \cup \{t\})$, the capacity of the cut is:
$$\begin{aligned}
\text{Cap}_\lambda(S) &= \sum_{v \in \bar{S}} U + \sum_{v \in S} \big(U + 2\lambda c_v - 2p_v - \deg_w(v)\big) + W(\delta(S, \bar{S})) \\
&= U|V| + \sum_{v \in S} (2\lambda c_v - 2p_v) - \big( \sum_{v \in S} \deg_w(v) - W(\delta(S, \bar{S})) \big) \\
&= U|V| + 2\lambda C(S) - 2P(S) - 2W(E(S)) \\
&= U|V| - 2 \big( W(E(S)) + P(S) - \lambda C(S) \big).
\end{aligned}$$
Thus:
$$\max_{S \subseteq V} \big( W(E(S)) + P(S) - \lambda C(S) \big) = \frac{U|V| - \text{MinCut}(G_\lambda)}{2}.$$

```
                 c(s -> u) = U                      c(u -> t) = U + 2λc_u - 2p_u - deg(u)
              +-----------------> ( u ) ------------------------------------------------+
              |                    | ^                                                  |
              |           w_{uv}   | |  w_{uv}                                          v
          [ s ]                    v |                                                [ t ]
              |                   ( v ) ------------------------------------------------+
              +----------------->       c(v -> t) = U + 2λc_v - 2p_v - deg(v)
                 c(s -> v) = U
```

#### Defeating the Empty-Set Masking Trap ($S = \emptyset$)
Wait: the minimization in $\text{MinCut}(G_\lambda)$ ranges over **all** subsets $S \subseteq V$, *including the empty set $S = \emptyset$*!
For $S = \emptyset$, the cut severs all $s \to v$ edges, giving $\text{Cap}_\lambda(\emptyset) = U|V|$ and $f_\lambda(\emptyset) = \frac{U|V| - U|V|}{2} = 0$.
Does this break our binary search for $\lambda^* = \max_{\emptyset \neq S \subseteq V} \frac{W(E(S)) + P(S)}{C(S)}$?
Let us check the two regimes (assuming $\lambda^* \ge 0$, which always holds whenever $W(E) \ge 0, P \ge 0$):
1. **When $\lambda < \lambda^*$**: By definition of $\lambda^*$, there exists a **non-empty** subset $S^* \neq \emptyset$ with $\frac{W(E(S^*)) + P(S^*)}{C(S^*)} = \lambda^* > \lambda$, so $f_\lambda(S^*) > 0$. Therefore:
   $$\text{MinCut}(G_\lambda) \le U|V| - 2 f_\lambda(S^*) < U|V| \quad \Longleftrightarrow \quad \frac{U|V| - \text{MinCut}(G_\lambda)}{2} > 0,$$
   and any minimum cut $S$ achieving $\text{MinCut}(G_\lambda) < U|V|$ is **guaranteed to be non-empty ($S \neq \emptyset$)**!
2. **When $\lambda \ge \lambda^*$**: For every non-empty $S \neq \emptyset$, $f_\lambda(S) \le 0$, so $\text{Cap}_\lambda(S) \ge U|V| = \text{Cap}_\lambda(\emptyset)$. Thus $\text{MinCut}(G_\lambda) = U|V|$ and $\frac{U|V| - \text{MinCut}(G_\lambda)}{2} = 0$.

**Conclusion**: As long as $\lambda^* \ge 0$, the empty set $S = \emptyset$ merely clamps the negative branch of $h(\lambda)$ to $0$ for $\lambda \ge \lambda^*$, while preserving the exact strict positivity condition:
$$\lambda < \lambda^* \quad \Longleftrightarrow \quad U|V| - \text{MinCut}(G_\lambda) > \epsilon.$$
**How to Reconstruct the Optimal Non-Empty Subgraph $S^*$**:
When binary search terminates with interval $[L, R]$ of width $< \frac{1}{|V|^2}$ (for unweighted MDS where denominators are $1 \le |S| \le |V|$), we must run one final Min-Cut at the **left endpoint** $\lambda = L < \lambda^*$ (NOT at $\lambda = R > \lambda^*$!) and collect all vertices $v \in V$ reachable from $s$ in the final residual graph. If we ran it at $\lambda = R > \lambda^*$, the minimum cut would be $S = \emptyset$!

---

### 4. Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Concrete Numerical Trace: Unweighted "Paw" Graph ($|V| = 4, |E| = 4$)
Let $G$ have vertices $\{1, 2, 3, 4\}$ and unweighted edges $(1,2), (2,3), (3,1)$ (a triangle $K_3$) plus a pendant edge $(3,4)$.
- Degrees: $\deg(1) = 2, \deg(2) = 2, \deg(3) = 3, \deg(4) = 1$.
- Maximum degree: $U = \max_v \deg(v) = 3$, so $U|V| = 3 \times 4 = 12$.
- Candidate subgraphs:
  - $S = \{1, 2, 3\}$: $|E(S)| = 3, |S| = 3 \implies D(S) = \frac{3}{3} = 1.0$.
  - $S = \{1, 2, 3, 4\}$: $|E(S)| = 4, |S| = 4 \implies D(S) = \frac{4}{4} = 1.0$.
  - What if we weight the triangle edges by $w = 2$ and the pendant edge $(3,4)$ by $w = 1$?
    Then $\deg_w = [4, 4, 5, 1]$, $U = 5$, $U|V| = 20$:
    - $S = \{1, 2, 3\}$: $W(E(S)) = 6, |S| = 3 \implies D(\{1,2,3\}) = \frac{6}{3} = 2.0$.
    - $S = \{1, 2, 3, 4\}$: $W(E(S)) = 7, |S| = 4 \implies D(\{1,2,3,4\}) = \frac{7}{4} = 1.75$.
- **Trace of Goldberg's Network at $\lambda = 1.9 < \lambda^* = 2.0$**:
  - $c(s \to v) = U = 5$ for $v \in \{1, 2, 3, 4\}$.
  - $c(v \to t) = U + 2\lambda - \deg_w(v) = 5 + 3.8 - \deg_w(v) = 8.8 - \deg_w(v)$:
    - $c(1 \to t) = 8.8 - 4 = 4.8$
    - $c(2 \to t) = 8.8 - 4 = 4.8$
    - $c(3 \to t) = 8.8 - 5 = 3.8$
    - $c(4 \to t) = 8.8 - 1 = 7.8$
  - Compare cuts:
    - For $S = \emptyset$: $\text{Cap}(\emptyset) = 5 \times 4 = 20.0$.
    - For $S = \{1, 2, 3, 4\}$: $\text{Cap}(V) = 4.8 + 4.8 + 3.8 + 7.8 = 21.2 > 20$.
    - For $S = \{1, 2, 3\}$: sever $1 \to t$ ($4.8$), $2 \to t$ ($4.8$), $3 \to t$ ($3.8$), $s \to 4$ ($5.0$), and cut edge $3 \to 4$ ($1.0$):
      $$\text{Cap}(\{1,2,3\}) = 4.8 + 4.8 + 3.8 + 5.0 + 1.0 = 19.4 < 20.0!$$
      Formula check: $U|V| - 2(W(E(S)) - \lambda |S|) = 20 - 2(6 - 1.9 \times 3) = 20 - 2(0.3) = 19.4$.
  - Since $\text{MinCut} = 19.4 < 20$, we conclude $\lambda^* > 1.9$ and the residual $s$-reachable set is $S = \{1, 2, 3\}$!

#### Broken Gadget Counterexamples & Classic Bugs
1. **Forgetting the Factor of $2$ in $2\lambda - \deg(v)$**:
   - *Bug*: Setting $c(v \to t) = U + \lambda - \deg(v)$ instead of $U + 2\lambda - \deg(v)$.
   - *Why it fails*: In Goldberg's identity $2|E(S)| = \sum_{v \in S} \deg(v) - |\delta(S, \bar{S})|$, the internal edge count is multiplied by **2**! If you omit the factor of 2 on $\lambda$, you are actually maximizing $\frac{2|E(S)|}{|S|}$, overestimating the density by a factor of $2$.
2. **Using Directed instead of Bidirectional Edges for $e = (u, v) \in E$**:
   - *Bug*: Adding only a single directed edge $u \to v$ of capacity $w_e$ in $G_\lambda$.
   - *Why it fails*: The identity $\sum_{v \in S} \deg_w(v) - 2W(E(S)) = W(\delta(S, \bar{S}))$ requires that *every* undirected edge with one endpoint in $S$ and one in $\bar{S}$ contributes $w_e$ regardless of whether $u \in S, v \notin S$ or $v \in S, u \notin S$. Both directions $u \to v$ and $v \to u$ must have capacity $w_e$.
3. **Extracting the Subgraph $S$ at $\lambda = R$ instead of $\lambda = L$**:
   - *Bug*: After binary search converges to $[L, R]$, running Dinic at $\lambda = R$ (or reading the residual graph from the last iteration where `check(mid)` returned `false`).
   - *Why it fails*: Whenever $\lambda \ge \lambda^*$, $\text{Cap}_\lambda(\emptyset) = U|V|$ is a minimum cut, and the $S$-minimal cut returned by BFS from $s$ in the residual graph is $S = \emptyset$! You must always reconstruct $S$ at a value $\lambda = L \le \lambda^* - \epsilon$ where `check(L)` strictly succeeded.

---

## Iteration 23: Planar Graph Duality ($s$-$t$ Planar Min-Cut $\leftrightarrow$ Dual Dijkstra & `[NOI2010] 海拔`)

### 1. Step 1: The Non-Graph / Geometric Diagnostic Signal (Recognition)

#### Surface Clues in Problem Statements
Iteration 23 represents our first major **Direction B (Flow $\to$ Non-Flow Fast Algorithm)** breakthrough, often paired with a subtle **Direction A (Continuous Potential $\to$ Binary Cut)** front-end:
1. **Topological Signal**: The network is embedded on a **2D grid, triangulation, or planar graph** without crossing edges, and the source $s$ (e.g., top-left corner $(0,0)$) and sink $t$ (e.g., bottom-right corner $(N,M)$) lie on the boundary of the **outer (unbounded) face**.
2. **Scale Signal ($V, E \le 10^6$)**: Typical constraints are $N, M \le 500\text{--}1000$ (so $V = NM \approx 2.5 \times 10^5\text{--}10^6$ vertices and $E \approx 2\text{--}3 \times 10^6$ edges), as in `[BJWC2006] 狼抓兔子` ($N, M \le 1000$) or `[NOI2010] 海拔` ($N \le 500$). At $V \approx 10^6$, general Dinic's algorithm—even with planar performance—suffers from massive constant factors and recursion/BFS overhead, whereas a single heap-based **Dijkstra's Shortest Path** runs in $O(V \log V)$ with tiny constant factor.
3. **Disguised Continuous Potential Signal (`[NOI2010] 海拔` / Altitude)**:
   The problem does not mention cuts or flows at all! Instead, it asks you to assign a **real-valued altitude** $h_v \in \mathbb{R}$ (or $h_v \in [0, 1]$) to every grid intersection $v$, fixing $h_{0,0} = 0$ and $h_{N,N} = 1$, to minimize total uphill work:
   $$\min_{h : V \to \mathbb{R}} \sum_{(u \to v) \in E} w(u \to v) \cdot \max(0, h_v - h_u).$$

#### Why Naive DP and Continuous Optimization Fail
- **Why Grid Profile DP Fails**: On an $N \times N$ grid with $N = 500$, the boundary frontier has length $N = 500$, so profile DP requires $2^{500}$ states. Even if edges only went Right and Down, the cut boundary can snake Left and Up!
- **Why Continuous Gradient Descent / LP Solvers Fail**: With $2.5 \times 10^5$ continuous variables $h_{i,j}$, generic LP solvers TLE. We need a structural theorem showing that continuous altitudes $h_{i,j} \in \mathbb{R}$ collapse to binary indicators $h_{i,j} \in \{0, 1\}$.

---

### 2. Step 2: The Algebraic / Topological Intermediate Representation

#### Part A: Cycle–Cut Duality on Planar Graphs ($G \leftrightarrow G^*$)
Let $G = (V, E)$ be a connected plane graph (a planar graph with a fixed embedding in $\mathbb{R}^2$). Its **geometric dual graph** $G^* = (F, E^*)$ has:
- One dual vertex $f^* \in F$ for each face $f$ of $G$ (including the unbounded outer face $f_\infty$).
- For each primal edge $e \in E$ separating face $f_1$ and face $f_2$, a dual edge $e^* = (f_1^*, f_2^*) \in E^*$ of equal weight $w(e^*) = w(e)$.

**Theorem 23.1 (Planar Cut–Cycle Duality)**:
*A minimal edge cut $\delta(S, \bar{S})$ in a connected plane graph $G$ corresponds bijectively to a simple cycle $C^*$ in the dual graph $G^*$ that separates the vertices of $S$ (inside $C^*$) from the vertices of $\bar{S}$ (outside $C^*$). For directed plane graphs, a directed cut $\delta^+(S)$ corresponds to a consistently oriented simple cycle $C^*$ in $G^*$.*

**Corollary 23.2 ($s$-$t$ Planar Graphs — Hassin 1981)**:
Suppose $s$ and $t$ both lie on the boundary of the outer face $f_\infty$. Draw an artificial curve $e_\infty$ between $s$ and $t$ entirely inside the outer face $f_\infty$. This splits the outer face $f_\infty$ into two distinct faces:
- $s^*$ (say, the lower-left outer region bounded by the clockwise perimeter from $s$ to $t$ and $e_\infty$), and
- $t^*$ (the upper-right outer region bounded by the clockwise perimeter from $t$ to $s$ and $e_\infty$).

Every dual cycle $C^*$ separating $s$ from $t$ must use the dual edge $e_\infty^* = (t^*, s^*)$ exactly once. Removing $e_\infty^*$ turns $C^*$ into a **simple path from $s^*$ to $t^*$ in the split dual graph $G^* \setminus \{e_\infty^*\}$**! Thus:
$$\text{MinCut}_G(s, t) = \text{ShortestPath}_{G^* \setminus \{e_\infty^*\}}(s^* \to t^*).$$

```
               t* (Upper-Right Outer Face)
         +------------+------------+
         | \   f_1  / | \   f_3  / |
      s  |   *    *   |   *    *   |  t
     (0,0)  f_2  /    |    \  f_4  (N,M)
         +------------+------------+
               s* (Lower-Left Outer Face)

   Dual shortest path s* ---> f_2 ---> f_1 ---> f_3 ---> t*
   severs the exact primal edges crossed on the path!
```

#### Part B: The Two-Stage Reduction for `[NOI2010] 海拔` (Continuous Potential $\to$ Binary Cut $\to$ Dual Dijkstra)
In `[NOI2010] 海拔`, we are given a directed $(N+1) \times (N+1)$ grid graph $G = (V, E)$ where each adjacent pair $\{u, v\}$ has two **asymmetric** directed traffic counts $w(u \to v) \ge 0$ and $w(v \to u) \ge 0$. Moving along $u \to v$ consumes fuel equal to traffic $w(u \to v)$ times the uphill elevation gain $\max(0, h_v - h_u)$ (going downhill or flat costs $0$). Given $h_{0,0} = 0$ and $h_{N,N} = 1$, we want to minimize:
$$\Phi(h) := \sum_{(u \to v) \in E} w(u \to v) \cdot \max(0, h_v - h_u) \quad \text{over } h : V \to \mathbb{R}.$$

**Theorem 23.3 (Coarea / Level-Set Extreme-Point Theorem for Uphill Work)**:
*The continuous optimization problem $\inf_{h : V \to \mathbb{R},\, h_s = 0,\, h_t = 1} \Phi(h)$ attains its minimum at a **binary altitude assignment** $h_v \in \{0, 1\}$ for all $v \in V$, and its minimum value is equal to the Minimum Directed $s$-$t$ Cut in $G$ (with edge capacities $c(u \to v) = w(u \to v)$).*

**Proof (via the Coarea / Layer-Cake Integral)**:
1. **Clamping to $[0, 1]$**: For any real assignment $h : V \to \mathbb{R}$ with $h_s = 0, h_t = 1$, define $\tilde{h}_v := \min(1, \max(0, h_v)) \in [0, 1]$. Because clamping is a $1$-contraction ($\max(0, \tilde{h}_v - \tilde{h}_u) \le \max(0, h_v - h_u)$), we have $\Phi(\tilde{h}) \le \Phi(h)$. Thus we may restrict $h_v \in [0, 1]$.
2. **Level-Set Representation**: For any two reals $a, b \in [0, 1]$, we can write the ramp function $\max(0, b - a)$ as the Lebesgue integral of binary threshold indicators over $\lambda \in (0, 1)$:
   $$\max(0, b - a) = \int_0^1 [a \le \lambda < b] \, d\lambda = \int_0^1 [a \le \lambda] \big( 1 - [b \le \lambda] \big) \, d\lambda.$$
3. **Slicing into $s$-$t$ Cuts**: For each threshold $\lambda \in (0, 1)$, define the sublevel vertex set:
   $$S_\lambda := \{ v \in V : h_v \le \lambda \}.$$
   Since $h_s = 0 \le \lambda < 1 = h_t$, we have $s \in S_\lambda$ and $t \in \bar{S}_\lambda$ for every $\lambda \in (0, 1)$. That is, $(S_\lambda, \bar{S}_\lambda)$ is a valid $s$-$t$ cut in $G$!
4. **Swapping Sum and Integral**: Substitute the level-set integral into $\Phi(h)$:
   $$\begin{aligned}
   \Phi(h) &= \sum_{(u \to v) \in E} w(u \to v) \int_0^1 [h_u \le \lambda < h_v] \, d\lambda \\
   &= \int_0^1 \left( \sum_{(u \to v) \in E} w(u \to v) [u \in S_\lambda][v \in \bar{S}_\lambda] \right) d\lambda \\
   &= \int_0^1 \text{Cut}_G(S_\lambda, \bar{S}_\lambda) \, d\lambda.
   \end{aligned}$$
5. **Lower Bound & Binary Realizability**: Since $\text{Cut}_G(S_\lambda, \bar{S}_\lambda) \ge \text{MinCut}_G(s, t)$ for every $\lambda \in (0, 1)$, integrating over $\lambda \in (0, 1)$ yields:
   $$\Phi(h) \ge \int_0^1 \text{MinCut}_G(s, t) \, d\lambda = \text{MinCut}_G(s, t).$$
   Conversely, if $(S^*, \bar{S}^*)$ is an optimal $s$-$t$ min-cut in $G$, setting the binary altitude $h^*_v = 0$ for $v \in S^*$ and $h^*_v = 1$ for $v \in \bar{S}^*$ gives $\max(0, h^*_v - h^*_u) = [u \in S^* \text{ and } v \in \bar{S}^*]$, achieving $\Phi(h^*) = \text{MinCut}_G(s, t)$! $\blacksquare$

*(Note for Wave 4B connection: If we write $z_{uv} = \max(0, h_v - h_u)$, the LP $\min \sum w_{uv} z_{uv}$ s.t. $z_{uv} \ge h_v - h_u, z_{uv} \ge 0, h_t - h_s \ge 1$ is literally the **Linear Programming Dual of Maximum $s$-$t$ Flow**!)*

---

### 3. Step 3: The Reverse-Engineering Scratchpad (Directed Dual Compilation & The 90° Rotation Contract)

In `[NOI2010] 海拔`, notice a critical nuance:
- In standard Min-Cut, a cut edge $u \to v$ goes from $s$-side ($S$) to $t$-side ($\bar{S}$).
- In `[NOI2010] 海拔`, $h_s = 0$ ($s \in S^*$, low altitude $0$) and $h_t = 1$ ($t \in \bar{S}^*$, high altitude $1$). An edge $u \to v$ incurs uphill cost $w(u \to v) \max(0, h_v - h_u)$ precisely when **$u \in S^*$ (altitude $0$) and $v \in \bar{S}^*$ (altitude $1$)**!
- Thus, the primal capacity of the directed edge $u \to v$ is simply $c(u \to v) = w(u \to v)$.

Now, how do we orient the **directed dual edges** when converting a **directed** primal planar graph into $G^*$?
Let us establish the **Right-Hand / 90° Clockwise Rotation Contract**:
1. Place the grid so $(0, 0) = s$ is at the **top-left** and $(N, N) = t$ is at the **bottom-right**.
2. Split the outer face into:
   - **Dual Source $s^*$**: the **Lower-Left** boundary (comprising the Left border $y = 0$ and the Bottom border $x = N$).
   - **Dual Sink $t^*$**: the **Upper-Right** boundary (comprising the Top border $x = 0$ and the Right border $y = N$).
3. Imagine walking along the dual cut path from $s^*$ (Lower-Left) to $t^*$ (Upper-Right). As you walk along this dual path:
   - Everything to your **LEFT** (containing top-left corner $s = (0,0)$) belongs to $S^*$ (altitude $h = 0$).
   - Everything to your **RIGHT** (containing bottom-right corner $t = (N,N)$) belongs to $\bar{S}^*$ (altitude $h = 1$).
4. Therefore, a primal directed edge $u \to v$ goes from $S^*$ (altitude $0$, on your LEFT) to $\bar{S}^*$ (altitude $1$, on your RIGHT) if and only if $u \to v$ crosses your dual path **from Left to Right**!
5. Equivalently: **Rotate the primal directed vector $\vec{uv}$ by $90^\circ$ counter-clockwise (so Left-to-Right becomes Forward along the dual path)**—or if you walk from Upper-Right $t^*$ to Lower-Left $s^*$, rotate $90^\circ$ clockwise!

Let us write out the **exact, bug-free 4-direction Dual Edge Lookup Table** when **Dual Source $S^*$ is Lower-Left** and **Dual Sink $T^*$ is Upper-Right** (so $s=(0,0)$ is on the **Left** of the dual path $S^* \to T^*$, and $t=(N,N)$ is on the **Right** of the dual path $S^* \to T^*$):

| Primal Directed Edge $u \to v$ (from $S^* [h=0]$ to $\bar{S}^* [h=1]$) | Direction of Primal Arrow | Which side is $S^*$ ($h=0$)? | Resulting Directed Dual Edge $f_1 \to f_2$ | Dual Edge Weight |
| :--- | :--- | :--- | :--- | :--- |
| **East**: $(i, j) \to (i, j+1)$ | $\longrightarrow$ (Left to Right) | $(i, j)$ is Left ($S^*$), $(i, j+1)$ is Right ($\bar{S}^*$) | **North (Up)**: $\text{Face}(i, j) \to \text{Face}(i-1, j)$ | $w_{\text{East}}(i, j)$ |
| **West**: $(i, j+1) \to (i, j)$ | $\longleftarrow$ (Right to Left) | $(i, j+1)$ is Left ($S^*$), $(i, j)$ is Right ($\bar{S}^*$) | **South (Down)**: $\text{Face}(i-1, j) \to \text{Face}(i, j)$ | $w_{\text{West}}(i, j)$ |
| **South**: $(i, j) \to (i+1, j)$ | $\downarrow$ (Top to Bottom) | $(i, j)$ is Top ($S^*$), $(i+1, j)$ is Bottom ($\bar{S}^*$) | **East (Right)**: $\text{Face}(i, j-1) \to \text{Face}(i, j)$ | $w_{\text{South}}(i, j)$ |
| **North**: $(i+1, j) \to (i, j)$ | $\uparrow$ (Bottom to Top) | $(i+1, j)$ is Bottom ($S^*$), $(i, j)$ is Top ($\bar{S}^*$) | **West (Left)**: $\text{Face}(i, j) \to \text{Face}(i, j-1)$ | $w_{\text{North}}(i, j)$ |

*(Here $\text{Face}(i, j)$ for $0 \le i, j < N$ denotes the unit square $[i, i+1] \times [j, j+1]$; any $\text{Face}(i, j)$ with $i = N$ or $j = -1$ is merged into Dual Source $S^*$, and any $\text{Face}(i, j)$ with $i = -1$ or $j = N$ is merged into Dual Sink $T^*$!)*

#### Extension 1: General Planar $s$-$t$ Min-Cut (When $s$ and $t$ Are Not on the Same Face)
What if $s$ and $t$ are buried inside the interior of a planar graph $G$ and do **not** share a face?
- By Theorem 23.1, an $s$-$t$ cut in $G$ is a minimum-weight dual cycle $C^*$ in $G^*$ that **separates face/vertex $s$ from face/vertex $t$** (i.e., $C^*$ has odd winding number / intersection parity around $t$ relative to $s$).
- **Reif (1983) / Hassin & Johnson (1985) Divide-and-Conquer Reduction**:
  1. Find any shortest path $P = (v_0 = s, v_1, \dots, v_k = t)$ between $s$ and $t$ in the primal graph $G$ (in terms of hop count).
  2. Every dual cycle $C^*$ separating $s$ and $t$ must cross the primal path $P$ an **odd** number of times; for undirected planar graphs, there exists an optimal dual cycle $C^*$ that crosses $P$ **at most once** (through a single edge $e_i \in P$).
  3. Slice the planar surface open along the path $P$: each dual face incident to $P$ is duplicated into a "left of $P$" copy $f_i^L$ and a "right of $P$" copy $f_i^R$.
  4. Then $\text{MinCut}_G(s, t) = \min_{i=1}^k \text{ShortestPath}_{G^*_{\text{sliced}}}(f_i^L \to f_i^R)$, which can be solved in $O(V \log^2 V)$ via recursive midpoint divide-and-conquer along $P$!

#### Extension 2: Multi-Terminal Outerplanar Cuts (`[CSP-S 2021] 交通规划`)
What if $k$ terminals lie around the outer boundary of a planar grid, each colored either $0$ (Source) or $1$ (Sink)?
- Whenever two adjacent boundary terminals have the **same** color, no minimal cut needs to separate them, so their dual boundary segment stays merged.
- Only the $2m$ boundary intervals where the terminal color **flips** ($0 \to 1$ or $1 \to 0$) act as active dual terminals $b_1^*, b_2^*, \dots, b_{2m}^*$ in cyclic order around the perimeter!
- Any valid multi-terminal cut decomposes into $m$ non-crossing dual paths matching the $m$ "entry" boundary transitions ($0 \to 1$) to the $m$ "exit" boundary transitions ($1 \to 0$).
- After running $2m$ Dual Dijkstras from each active boundary transition $b_i^*$ in $O(k V \log V)$, the non-crossing matching on the circle is solved by standard **Circular Interval DP** in $O(m^3)$ time!

---

### 4. Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Concrete Numerical Trace: $1 \times 1$ Grid Cell ($N = 1$, $2 \times 2$ Vertices) in `[NOI2010] 海拔`
Let $N = 1$, so the vertices are $(0,0) = s$ (top-left), $(0,1)$ (top-right), $(1,0)$ (bottom-left), and $(1,1) = t$ (bottom-right), surrounding a single interior square face $F_{0,0}$.
Suppose the directed traffic weights are:
- Top horizontal edge: $w((0,0) \to (0,1)) = 10$ (East), $w((0,1) \to (0,0)) = 100$ (West).
- Bottom horizontal edge: $w((1,0) \to (1,1)) = 20$ (East), $w((1,1) \to (1,0)) = 100$ (West).
- Left vertical edge: $w((0,0) \to (1,0)) = 30$ (South), $w((1,0) \to (0,0)) = 100$ (North).
- Right vertical edge: $w((0,1) \to (1,1)) = 5$ (South), $w((1,1) \to (0,1)) = 2$ (North).
Let us trace the Dual Graph $G^*$ using our table (where $S^*$ is Lower-Left, $T^*$ is Upper-Right, and $F_{0,0}$ is the single central face):
1. **Top edge $(0,0) \leftrightarrow (0,1)$** separates $F_{0,0}$ from $T^*$:
   - East $(0,0) \to (0,1)$ gives dual edge North: $F_{0,0} \to T^*$ of weight $10$.
   - West $(0,1) \to (0,0)$ gives dual edge South: $T^* \to F_{0,0}$ of weight $100$.
2. **Bottom edge $(1,0) \leftrightarrow (1,1)$** separates $S^*$ from $F_{0,0}$:
   - East $(1,0) \to (1,1)$ gives dual edge North: $S^* \to F_{0,0}$ of weight $20$.
   - West $(1,1) \to (1,0)$ gives dual edge South: $F_{0,0} \to S^*$ of weight $100$.
3. **Left edge $(0,0) \leftrightarrow (1,0)$** separates $S^*$ from $F_{0,0}$:
   - South $(0,0) \to (1,0)$ gives dual edge East: $S^* \to F_{0,0}$ of weight $30$.
   - North $(1,0) \to (0,0)$ gives dual edge West: $F_{0,0} \to S^*$ of weight $100$.
4. **Right edge $(0,1) \leftrightarrow (1,1)$** separates $F_{0,0}$ from $T^*$:
   - South $(0,1) \to (1,1)$ gives dual edge East: $F_{0,0} \to T^*$ of weight $5$.
   - North $(1,1) \to (0,1)$ gives dual edge West: $T^* \to F_{0,0}$ of weight $2$.
- **Dual Shortest Path from $S^*$ to $T^*$**:
  - First step $S^* \to F_{0,0}$: $\min(20 \text{ [Bottom East]}, 30 \text{ [Left South]}) = 20$ (severing $(1,0) \to (1,1)$, so $(1,0) \in S^* [h=0]$).
  - Second step $F_{0,0} \to T^*$: $\min(10 \text{ [Top East]}, 5 \text{ [Right South]}) = 5$ (severing $(0,1) \to (1,1)$, so $(0,1) \in S^* [h=0]$).
  - Total Dual Shortest Path $= 20 + 5 = 25$, corresponding to setting $h_{0,0} = h_{1,0} = h_{0,1} = 0$ and $h_{1,1} = 1$!
  - Notice that if we instead tried a zig-zag cut where $h_{0,1} = 1$ and $h_{1,0} = 0$, the dual path would have to go $T^* \to F_{0,0}$ using North $(1,1) \to (0,1)$ of weight $2$, which goes backwards ($T^* \to S^*$) and is automatically forbidden by directed dual orientations!

#### Broken Gadget Counterexamples & Classic Bugs
1. **Reversing the 90° Rotation Rule (Computing $t$-$s$ Cut Instead of $s$-$t$ Cut)**:
   - *Bug*: Mapping East $(i, j) \to (i, j+1)$ to South $\text{Face}(i-1, j) \to \text{Face}(i, j)$ while keeping $S^*$ at Lower-Left and $T^*$ at Upper-Right.
   - *Why it fails*: This swaps the roles of $S^*$ and $\bar{S}^*$, computing the cost of assigning $h_{0,0} = 1$ and $h_{N,N} = 0$ (which uses the opposite traffic directions $w(v \to u)$ instead of $w(u \to v)$!). Always verify your rotation table on a $1 \times 1$ grid before submitting.
2. **Misindexing Triangulated Grid Faces (`[BJWC2006] 狼抓兔子`)**:
   - *Bug*: In `狼抓兔子`, each unit square $(i, j)$ is split by a diagonal from top-left $(i, j)$ to bottom-right $(i+1, j+1)$ into a Lower-Left triangle $T_{\text{lower}}(i, j)$ and an Upper-Right triangle $T_{\text{upper}}(i, j)$. Connecting the top horizontal edge of cell $(i, j)$ to $T_{\text{lower}}(i, j)$ instead of $T_{\text{upper}}(i, j)$ corrupts the dual adjacency.

---

## Iteration 24: Solving Max-Flow via Min-Cut DP / Greedy (`最大流转最小割 DP` — `CF 724 E`, `BZOJ 2039`, Tree Min-Cut DP)

### 1. Step 1: The Non-Graph Diagnostic Signal (Recognition)

#### Surface Clues in Problem Statements
How do you recognize a **Max-Flow to Min-Cut DP / Greedy (`最大流转最小割 DP`)** problem?
1. **Explicit or Immediate Flow Statement**: Either the problem is literally phrased as a maximum flow / transportation problem (e.g., `CF 724 E — Goods Transportation`: *"In city $i$, $p_i$ units of goods are produced, $s_i$ units can be sold, and between any pair $i < j$ at most $c$ units can be transported"*), OR it immediately translates via Wave 2A into a Project Selection / Min-Cut problem.
2. **Constraint Explosion ($N \le 10^4\text{--}2 \times 10^5$)**: The number of vertices is $N = 10,000$ to $200,000$, and the edge set is implicitly dense ($|E| = \binom{N}{2} \approx 5 \times 10^7\text{--}2 \times 10^{10}$). You cannot even allocate memory for the edges, let alone run Dinic's algorithm!
3. **Structured Cross-Edge Capacity Pattern**: The capacities $c(i \to j)$ between internal vertices are not arbitrary random numbers—they obey a strong structural law:
   - **Uniform Tournament / Complete DAG**: $c(i \to j) = c$ for all $1 \le i < j \le N$ (`CF 724 E`), or $c(i \to j)$ depends only on $i$ or $j$.
   - **Tree / Series-Parallel / Bounded Treewidth**: The internal edges form a tree or have bandwidth $\le k$ (`Tree Max-Flow`, `ABC 214 H` / `CF 1783 F` style).
   - **Coordinate / Bipartite Interval Structure**: Cross-edges connect $i$ to a contiguous interval $[L_i, R_i]$ (`AGC 031 E` / `ARC 076 F` variants).

#### Why Direct Greedy Simulation of Flow Fails
In `CF 724 E`, if you try to greedily push flow from $i$ to $j > i$, which $j$ should receive flow from $i$? Sending flow from $1 \to 2$ might block $2$'s sink capacity $s_2$, or might be suboptimal compared to sending $1 \to 3$ and $2 \to 4$. In the **Primal (Flow)** view, there are $\binom{N}{2}$ flow variables $f_{ij} \in [0, c]$ coupled by conservation constraints.
In the **Dual (Min-Cut)** view, by contrast, there are **only $N$ binary variables $x_1, \dots, x_N \in \{0, 1\}$**!

---

### 2. Step 2: The Algebraic / Logical Intermediate Representation

Let $G = (V \cup \{s, t\}, E)$ be any flow network where:
- Source $s$ has directed edge $s \to i$ of capacity $p_i \ge 0$ for each $i \in \{1, \dots, N\}$.
- Each $i \in \{1, \dots, N\}$ has directed edge $i \to t$ of capacity $s_i \ge 0$ to sink $t$.
- Between internal vertices, directed edge $i \to j$ has capacity $c_{ij} \ge 0$.

By the **Max-Flow Min-Cut Theorem**, the maximum $s$-$t$ flow in $G$ is equal to the minimum capacity of an $s$-$t$ cut $(S \cup \{s\}, T \cup \{t\})$.
Assign a binary indicator $x_i \in \{0, 1\}$ to each vertex $i \in \{1, \dots, N\}$:
- **$x_i = 1$ ($i \in S$, Source side)**: The edge $s \to i$ is NOT cut, but the edge $i \to t$ goes from $S$ to $T \cup \{t\}$ and **IS cut**, costing $s_i$.
- **$x_i = 0$ ($i \in T$, Sink side)**: The edge $i \to t$ is NOT cut, but the edge $s \to i$ goes from $S \cup \{s\}$ to $T$ and **IS cut**, costing $p_i$.
- **Internal Cross-Edges**: An internal edge $i \to j$ is cut if and only if $i \in S$ ($x_i = 1$) and $j \in T$ ($x_j = 0$), costing $c_{ij} x_i (1 - x_j)$.

This gives the **Master Min-Cut Pseudo-Boolean Objective**:
$$\text{MaxFlow}(G) = \min_{x \in \{0, 1\}^N} \left( \sum_{i=1}^N p_i (1 - x_i) + \sum_{i=1}^N s_i x_i + \sum_{i=1}^N \sum_{j=1}^N c_{ij} x_i (1 - x_j) \right).$$

Once this formula is written down, **we discard the flow graph completely** and optimize $x \in \{0, 1\}^N$ using Dynamic Programming or Greedy!

---

### 3. Step 3: The Reverse-Engineering Scratchpad (Three Canonical Compilations)

#### Model 24A: Complete DAG with Uniform Capacity (`CF 724 E — Goods Transportation`)
In `CF 724 E`, we have $N \le 10^4$ cities, source capacities $p_i$, sink capacities $s_i$, and $c_{ij} = c$ for all $1 \le i < j \le N$ (and $c_{ij} = 0$ for $i \ge j$).
Substituting $c_{ij} = c \cdot [i < j]$ into the Master Min-Cut Objective gives:
$$\text{MaxFlow} = \min_{x \in \{0, 1\}^N} \left( \sum_{i=1}^N p_i (1 - x_i) + \sum_{i=1}^N s_i x_i + \sum_{i=1}^N (1 - x_i) \cdot c \sum_{j < i} x_j \right).$$

Let us read the cost contribution of vertex $i$ as we scan $i = 1, 2, \dots, N$ from left to right, maintaining the count $k = \sum_{j < i} x_j$ of how many previous vertices $\{1, \dots, i-1\}$ were placed in $S$ ($x_j = 1$):
1. **If we place $i \in S$ ($x_i = 1$)**:
   - We sever $i \to t$, paying $s_i$.
   - No edge $j \to i$ ($j < i$) is severed because $i$ is also in $S$!
   - The count of $S$-vertices increases from $k$ to $k + 1$.
2. **If we place $i \in T$ ($x_i = 0$)**:
   - We sever $s \to i$, paying $p_i$.
   - In addition, **every** edge $j \to i$ from an earlier vertex $j < i$ with $x_j = 1$ goes from $S$ to $T$ and is severed! Since there are $k$ such vertices, this costs $k \cdot c$.
   - The count of $S$-vertices remains $k$.

**Level 1 Compilation — The $O(N^2)$ Dynamic Programming Recurrence**:
Define $dp[i][k]$ as the minimum cut cost for prefix $1 \dots i$ given that $\sum_{j=1}^i x_j = k$. Then:
$$dp[i][k] = \min \Big( \underbrace{dp[i-1][k] + p_i + k \cdot c}_{\text{place } i \in T \; (x_i = 0)}, \quad \underbrace{dp[i-1][k-1] + s_i}_{\text{place } i \in S \; (x_i = 1)} \Big).$$
With rolling arrays, this uses $O(N)$ memory and $O(N^2)$ time—already fast enough for $N = 10^4$!

**Level 2 Compilation — The $O(N \log N)$ Algebraic Decoupling & Greedy Sort**:
Can we go even further and solve `CF 724 E` in $O(N \log N)$ time (capable of handling $N \le 5 \times 10^5$)?
Look closely at the cross-edge term $\sum_{i < j} c \cdot x_i (1 - x_j)$. Let $S = \{ i : x_i = 1 \}$ be the set of vertices placed on the source side, and suppose $|S| = k$.
For each $i \in S$, how many vertices $j > i$ are in $T$ ($x_j = 0$)?
Total vertices after $i$ is $N - i$. Among those, the ones that are **not** in $T$ are precisely the elements of $S$ that are strictly greater than $i$:
$$\sum_{i \in S} \sum_{j > i, \, j \notin S} c = c \sum_{i \in S} (N - i) - c \sum_{i \in S} |\{ j \in S : j > i \}|.$$
Wait: what is $\sum_{i \in S} |\{ j \in S : j > i \}|$? Every pair of distinct elements $\{i, j\} \subseteq S$ has one smaller element and one larger element, so this sum is **always equal to $\binom{|S|}{2} = \frac{k(k-1)}{2}$**, regardless of which specific $k$ elements form $S$!
Substitute this back into the Master Min-Cut Objective:
$$\begin{aligned}
\text{Cut}(S) &= \sum_{i \notin S} p_i + \sum_{i \in S} s_i + c \sum_{i \in S} (N - i) - c \binom{|S|}{2} \\
&= \sum_{i=1}^N p_i + \sum_{i \in S} \underbrace{\big( s_i - p_i + (N - i) c \big)}_{\text{independent weight } w_i} - \binom{|S|}{2} c.
\end{aligned}$$
**Theorem 24.1 (Decoupled Greedy Theorem for `CF 724 E`)**:
*For any fixed cardinality $k = |S| \in \{0, 1, \dots, N\}$, the minimum cut with $|S| = k$ is obtained by picking the $k$ vertices with the smallest independent weights $w_i = s_i - p_i + (N - i) c$. Thus $\text{MaxFlow}$ can be computed in $O(N \log N)$ time purely by sorting $w_1, \dots, w_N$!*

#### Model 24B: Symmetric Pairwise Synergy Matrix (`[BZOJ 2039] 人员雇佣 / Employ`)
In `[BZOJ 2039]`, there are $N \le 1000$ employees. Hiring employee $i$ costs $A_i$. For every ordered pair $(i, j)$:
- If **both** $i$ and $j$ are hired ($x_i = 1, x_j = 1$), the company gains $2 E_{ij}$.
- If **$i$ is hired and $j$ is NOT hired** ($x_i = 1, x_j = 0$), the company **loses** $E_{ij}$ (so across the unordered pair $\{i, j\}$ with $E_{ij} = E_{ji}$, if both are hired we get $+2 E_{ij}$ from $(i,j)$ and $+2 E_{ji}$ from $(j,i)$, total $+4 E_{ij}$; if one is hired, we lose $2 E_{ij}$).
Let us write the net profit for indicator vector $x \in \{0, 1\}^N$:
$$\text{Profit}(x) = \sum_{i=1}^N \sum_{j=1}^N 2 E_{ij} x_i x_j - \sum_{i=1}^N \sum_{j=1}^N E_{ij} \big( x_i(1 - x_j) + x_j(1 - x_i) \big) - \sum_{i=1}^N A_i x_i.$$
Apply Goldberg's identity $x_i x_j = x_i - x_i(1 - x_j)$ (or $\frac{1}{2}(x_i + x_j) - \frac{1}{2}(x_i(1-x_j) + x_j(1-x_i))$):
$$2 E_{ij} x_i x_j = E_{ij} x_i + E_{ij} x_j - E_{ij} \big( x_i(1 - x_j) + x_j(1 - x_i) \big).$$
Summing over all $i, j$ and letting $D_i := \sum_{j=1}^N 2 E_{ij}$:
$$\text{Profit}(x) = \sum_{i=1}^N (D_i - A_i) x_i - \sum_{i=1}^N \sum_{j=1}^N 2 E_{ij} \cdot x_i(1 - x_j)!$$
Instead of $N + N^2 = 10^6$ vertices in a naive project selection graph, this has **only $N$ vertices** (and if $E_{ij}$ is uniform or rank-1, solves in $O(N \log N)$ via Model 24A without flow at all!).

#### Model 24C: Tree Max-Flow via Min-Cut Tree DP (`树上最大流转最小割 DP`)
Suppose the internal graph $G = (V, E)$ is a rooted **tree** (with directed or undirected capacities $c(u \to v)$ and $c(v \to u)$ between parent $u$ and child $v$), and each vertex $u \in V$ has source capacity $p_u = c(s \to u)$ and sink capacity $s_u = c(u \to t)$.
- Instead of running Dinic's algorithm, define a **Bottom-Up Tree DP** on the Min-Cut partition $x_u \in \{0, 1\}$ ($0 \iff u \in T$, $1 \iff u \in S$):
  - $dp[u][0]$ (cost in subtree of $u$ when $u \in T$, so $s \to u$ is cut):
    $$dp[u][0] = p_u + \sum_{v \in \text{children}(u)} \min \Big( dp[v][0], \; dp[v][1] + c(v \to u) \Big).$$
  - $dp[u][1]$ (cost in subtree of $u$ when $u \in S$, so $u \to t$ is cut):
    $$dp[u][1] = s_u + \sum_{v \in \text{children}(u)} \min \Big( dp[v][1], \; dp[v][0] + c(u \to v) \Big).$$
- **Complexity**: $O(N)$ linear time for a static tree, and $O(\log^2 N)$ per capacity modification using **Dynamic DP (DDP)** on Heavy-Light Decomposition!

---

### 4. Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Concrete Numerical Trace of `CF 724 E` ($N = 3, c = 2$)
Let $N = 3, c = 2$, source capacities $p = [5, 1, 6]$, and sink capacities $s = [2, 7, 3]$.
Let us evaluate all $2^3 = 8$ cuts $x = (x_1, x_2, x_3) \in \{0, 1\}^3$ and compare with our $O(N \log N)$ formula:
- Base cost (all in $T$, $x = (0,0,0)$): $\sum p_i = 5 + 1 + 6 = 12$.
- Independent weights $w_i = s_i - p_i + (N - i) c$:
  - $w_1 = 2 - 5 + (3 - 1) \times 2 = -3 + 4 = +1$.
  - $w_2 = 7 - 1 + (3 - 2) \times 2 = +6 + 2 = +8$.
  - $w_3 = 3 - 6 + (3 - 3) \times 2 = -3 + 0 = -3$.
- Sort $w$ ascending: $w_{(1)} = w_3 = -3$, $w_{(2)} = w_1 = +1$, $w_{(3)} = w_2 = +8$.
- Evaluate best cut for each cardinality $k = |S| \in \{0, 1, 2, 3\}$:
  - $k = 0$ ($S = \emptyset$): $\text{Cost} = 12$.
  - $k = 1$ ($S = \{3\}$): $\text{Cost} = 12 + (-3) - \binom{1}{2}(2) = 9$.
    *(Check: $1, 2 \in T$ pay $p_1 + p_2 = 5 + 1 = 6$; $3 \in S$ pays $s_3 = 3$; no cross-edges $i \to j$ have $i \in S, j \in T$ since $3$ is the last vertex! Total $= 6 + 3 = 9$.)*
  - $k = 2$ ($S = \{3, 1\}$): $\text{Cost} = 12 + (-3 + 1) - \binom{2}{2}(2) = 10 - 2 = 8$.
    *(Check: $1, 3 \in S$ pay $s_1 + s_3 = 2 + 3 = 5$; $2 \in T$ pays $p_2 = 1$; cross-edge $1 \to 2$ is severed ($c = 2$), while $1 \to 3$ is NOT severed since both $1, 3 \in S$! Total $= 5 + 1 + 2 = 8$.)*
  - $k = 3$ ($S = \{3, 1, 2\}$): $\text{Cost} = 12 + (-3 + 1 + 8) - \binom{3}{2}(2) = 18 - 6 = 12$.
    *(Check: all in $S$ pays $s_1 + s_2 + s_3 = 2 + 7 + 3 = 12$.)*
- Minimum Cut $=$ Maximum Flow $= \min(12, 9, 8, 12) = 8$.

#### Broken Gadget Counterexamples & Classic Bugs
1. **Confusing Which Edge Is Cut When $i \in S$ vs. $i \in T$**:
   - *Bug*: Writing that placing $i \in S$ costs $p_i$ and placing $i \in T$ costs $s_i$.
   - *Why it fails*: Remember that source $s \in S$ and sink $t \in T$. If $i \in S$, then $s$ and $i$ are on the **same side** of the cut, so $s \to i$ (capacity $p_i$) is intact, while $i \to t$ (capacity $s_i$) crosses from $S$ to $T$ and is **severed**!
2. **Applying the $\binom{k}{2} c$ Decoupling Trick When Edge Capacities $c_{ij}$ Are Non-Uniform**:
   - *Why it fails*: The identity $\sum_{i \in S} \sum_{j \in S, j > i} c_{ij} = \binom{|S|}{2} c$ holds **if and only if** $c_{ij} = c$ is constant across all pairs $i < j$ (or Separable $c_{ij}$). If $c_{ij}$ depends on $|i - j|$ or is non-uniform, you must use the $O(N^2)$ DP (or Slope Trick / Segment Tree DP if $c_{ij}$ is an interval function).

---

## Iteration 25: Global Minimum Cut (Stoer–Wagner) & All-Pairs Min-Cut Trees (Gomory–Hu / Gusfield `最小割树`)

### 1. Step 1: The Non-Graph / Multi-Query Diagnostic Signal (Recognition)

#### Surface Clues in Problem Statements
In standard $s$-$t$ Min-Cut problems, a single source $s$ and sink $t$ are fixed in advance. You need **Stoer–Wagner** or a **Gomory–Hu Cut Tree (`最小割树`)** when:
1. **Global Minimum Cut Signal (No fixed $s, t$)**: Given an undirected weighted graph $G = (V, E)$ with $N \le 600$, find a non-trivial partition $(S, \bar{S})$ ($\emptyset \subsetneq S \subsetneq V$) minimizing $w(\delta(S, \bar{S}))$ to disconnect $G$ into at least two components.
2. **All-Pairs / Multi-Query Min-Cut Signal (`[ZJOI2011] 最小割`, `[CQOI2016] 不同的最小割`, `CF 343 E`)**:
   - Given an undirected graph with $N \le 500, M \le 3000$, answer $Q \le 10^5$ queries of the form *"What is $\text{MinCut}_G(u, v)$?"* or *"How many pairs $\{u, v\}$ have $\text{MinCut}_G(u, v) \le X$?"*
   - Or: *"How many distinct values appear in the $N \times N$ matrix of all-pairs minimum cuts $\lambda_G(u, v)$?"* (`[CQOI2016]`).
   - Or: *"Arrange the $N$ vertices into a sequence $p_1, p_2, \dots, p_N$ to maximize $\sum_{i=1}^{N-1} \text{MinCut}_G(p_i, p_{i+1})$"* (`CF 343 E — Pumping Stations`).
   - Or: *"Given a matrix $A_{u,v}$, determine if there exists an undirected graph $G$ whose all-pairs minimum cuts equal $A_{u,v}$"* (Inverse Gomory–Hu / Ultrametric recognition).

#### Why Naive Pairwise Dinic Calls Fail
For $N = 500$, there are $\binom{N}{2} = 124,750$ pairs of vertices. Running Dinic $\binom{N}{2}$ times requires $\sim 1.25 \times 10^5$ max-flow computations, which TLEs by a factor of $200\times$.
The **Gomory–Hu Theorem (1961)** reveals a miraculous structural compression: all $\binom{N}{2}$ pairwise minimum cuts in an undirected graph are completely captured by a single weighted tree $T_{\text{GH}}$ on $N$ vertices, which can be constructed using **only $N - 1$ calls to Max-Flow**!

---

### 2. Step 2: The Algebraic / Structural Intermediate Representation

#### Part A: The Ultrametric Inequality of Undirected Pairwise Min-Cuts
For any pair of distinct vertices $u, v \in V$ in an undirected graph $G = (V, E)$ with edge weights $w_e \ge 0$, let $\lambda(u, v) := \text{MinCut}_G(u, v)$ denote the minimum weight of an edge cut separating $u$ and $v$.

**Theorem 25.1 (Ultrametric Triangle Inequality for Min-Cuts)**:
*For any three distinct vertices $u, v, w \in V$ in an undirected weighted graph $G$:*
$$\lambda(u, w) \ge \min \big( \lambda(u, v), \; \lambda(v, w) \big).$$
*Consequently, among the three values $\lambda(u, v), \lambda(v, w), \lambda(u, w)$, the **two smallest values must be equal**!*

**Proof**:
Let $(S, \bar{S})$ be an optimal $u$-$w$ minimum cut in $G$, with $u \in S$, $w \in \bar{S}$, and $w(\delta(S, \bar{S})) = \lambda(u, w)$. Consider the third vertex $v$:
- **Case 1 ($v \in S$)**: Then $(S, \bar{S})$ has $v \in S$ and $w \in \bar{S}$, so $(S, \bar{S})$ is a valid $v$-$w$ cut! By definition of minimum $v$-$w$ cut, $\lambda(u, w) = w(\delta(S, \bar{S})) \ge \lambda(v, w) \ge \min(\lambda(u, v), \lambda(v, w))$.
- **Case 2 ($v \in \bar{S}$)**: Then $(S, \bar{S})$ has $u \in S$ and $v \in \bar{S}$, so $(S, \bar{S})$ is a valid $u$-$v$ cut! Thus $\lambda(u, w) = w(\delta(S, \bar{S})) \ge \lambda(u, v) \ge \min(\lambda(u, v), \lambda(v, w))$. $\blacksquare$

**Immediate Consequence**: Across all $\binom{N}{2}$ vertex pairs, $\lambda(u, v)$ can take **at most $N - 1$ distinct numerical values**!

#### Part B: Stoer–Wagner Global Minimum Cut & The Phase-of-the-Moon Theorem
To find the global minimum cut $\min_{\emptyset \subsetneq S \subsetneq V} w(\delta(S, \bar{S}))$ without running flow, **Stoer & Wagner (1997)** (building on **Nagamochi & Ibaraki, 1992**) noticed that if we know the minimum $s$-$t$ cut for **any** single pair of vertices $s, t \in V$, then the global minimum cut of $G$ is either:
1. $\lambda_G(s, t)$ (if the global min-cut separates $s$ and $t$), OR
2. $\text{GlobalMinCut}(G / \{s, t\})$ (if $s$ and $t$ lie on the **same side** of the global min-cut, so contracting $s$ and $t$ into a single supernode preserves it!).

How do we find a pair $(s, t)$ and its exact minimum cut $\lambda_G(s, t)$ in $O(E + V \log V)$ time without flow? Via **Maximum Adjacency Search (MAS)**:
- Start with $A_1 = \{v_1\}$ for an arbitrary vertex $v_1 \in V$.
- For $i = 2, 3, \dots, n$: choose $v_i \in V \setminus A_{i-1}$ maximizing the connection weight to the already-visited set $A_{i-1}$:
  $$v_i := \arg\max_{v \in V \setminus A_{i-1}} w(A_{i-1}, v), \quad \text{and set } A_i := A_{i-1} \cup \{v_i\}.$$

**Theorem 25.2 (Stoer–Wagner / Nagamochi–Ibaraki Theorem)**:
*Let $v_1, v_2, \dots, v_{n-1}, v_n$ be any Maximum Adjacency Ordering of $G$. Then for the **last two vertices** $s = v_{n-1}$ and $t = v_n$, the singleton cut $(V \setminus \{t\}, \{t\})$ is a minimum $s$-$t$ cut in $G$:*
$$\lambda_G(v_{n-1}, v_n) = w(V \setminus \{v_n\}, v_n).$$

**Proof (via Active Vertices Induction)**:
Let $(C, \bar{C})$ be any $v_{n-1}$-$v_n$ cut in $G$ (with $v_{n-1} \in C, v_n \in \bar{C}$). We must prove that $w(C, \bar{C}) \ge w(V \setminus \{v_n\}, v_n)$.
Call a vertex $v_i$ ($i \ge 2$) **active** with respect to $(C, \bar{C})$ if $v_i$ and its immediate predecessor $v_{i-1}$ in the ordering lie on **opposite sides** of the cut $(C, \bar{C})$.
Let $A_{i-1} = \{v_1, \dots, v_{i-1}\}$ and let $C_i := A_i \cap C$ and $\bar{C}_i := A_i \cap \bar{C}$.
**Lemma**: *For every active vertex $v_i$, we have $w(A_{i-1}, v_i) \le w(C_i, \bar{C}_i)$.Since $v_n$ is active (as $v_{n-1} \in C$ and $v_n \in \bar{C}$), plugging in $i = n$ gives $w(V \setminus \{v_n\}, v_n) = w(A_{n-1}, v_n) \le w(C_n, \bar{C}_n) = w(C, \bar{C})$!*
*Proof of Lemma by Induction on Active Vertices*:
- **Base Case (first active vertex $v_i$)**: Since $v_i$ is the first active vertex, all vertices in $A_{i-1} = \{v_1, \dots, v_{i-1}\}$ lie on the **same side** of $(C, \bar{C})$ (say $C$), while $v_i \in \bar{C}$. Thus every edge between $A_{i-1}$ and $v_i$ crosses $(C_i, \bar{C}_i)$, so $w(A_{i-1}, v_i) = w(C_i, \bar{C}_i)$.
- **Inductive Step**: Let $v_i$ be an active vertex and $v_k$ ($k > i$) be the **next** active vertex. Because no vertex in $\{v_{i+1}, \dots, v_{k-1}\}$ is active, all of $\{v_i, v_{i+1}, \dots, v_{k-1}\}$ lie on the **same side** of $(C, \bar{C})$, whereas $v_k$ lies on the **opposite side**!
  Therefore, every edge between $v_k$ and $A_{k-1} \setminus A_{i-1} = \{v_i, \dots, v_{k-1}\}$ crosses $(C_k, \bar{C}_k)$ and is disjoint from $E(C_i, \bar{C}_i)$:
  $$w(C_k, \bar{C}_k) \ge w(C_i, \bar{C}_i) + w(A_{k-1} \setminus A_{i-1}, v_k).$$
  By the greedy MAS choice of $v_i$ at step $i$ (when $v_k \notin A_{i-1}$ was also available!), we have $w(A_{i-1}, v_i) \ge w(A_{i-1}, v_k)$. Combining this with the inductive hypothesis $w(C_i, \bar{C}_i) \ge w(A_{i-1}, v_i)$ gives:
  $$w(C_k, \bar{C}_k) \ge w(A_{i-1}, v_i) + w(A_{k-1} \setminus A_{i-1}, v_k) \ge w(A_{i-1}, v_k) + w(A_{k-1} \setminus A_{i-1}, v_k) = w(A_{k-1}, v_k). \quad \blacksquare$$

Using a binary heap (or $O(V^2)$ array for dense graphs), each of the $V - 1$ MAS phases + contractions takes $O(E + V \log V)$ (or $O(V^2)$), giving **$O(VE + V^2 \log V)$** (or **$O(V^3)$**) total time!

#### Part C: Gomory–Hu Cut Trees & Submodular Uncrossing
Why don't minimum cuts between different pairs $(u, v)$ and $(x, y)$ tangle up and cross each other in a way that prevents a tree representation?
Because the undirected cut function $c(S) := w(\delta(S, \bar{S}))$ is **symmetric and submodular**:
1. **Submodularity**: $c(A) + c(B) \ge c(A \cap B) + c(A \cup B)$ for all $A, B \subseteq V$.
2. **Posimodularity (by symmetry $c(S) = c(\bar{S})$)**: $c(A) + c(B) = c(A) + c(\bar{B}) \ge c(A \setminus B) + c(B \setminus A)$.

**Lemma 25.3 (The Uncrossing Lemma for Minimum Cuts)**:
*Let $(S, \bar{S})$ be a minimum $u$-$v$ cut ($u \in S, v \in \bar{S}$), and let $x, y \in S$ be any two vertices that both lie in $S$. Then there exists a minimum $x$-$y$ cut $(X, \bar{X})$ that **does not cross** $(S, \bar{S})$—specifically, $\bar{S}$ lies entirely on one side of $(X, \bar{X})$!*

**Proof**:
Let $(Y, \bar{Y})$ be any minimum $x$-$y$ cut with $x \in Y$ and $y \in \bar{Y}$. By symmetry of $x$ and $y$, suppose without loss of generality that $u \in Y$.
- **Subcase 1 ($v \in \bar{Y}$)**: Consider $Y \cap S$ (which contains $x$ and avoids $y \in \bar{Y}$) and $Y \cup S$ (which contains $u \in S$ and avoids $v \in \bar{S} \cap \bar{Y}$). By submodularity:
  $$c(Y) + c(S) \ge c(Y \cap S) + c(Y \cup S).$$
  Since $(S, \bar{S})$ is a minimum $u$-$v$ cut, $c(Y \cup S) \ge c(S)$, which forces $c(Y \cap S) \le c(Y)$. Thus $X = Y \cap S \subseteq S$ is a minimum $x$-$y$ cut that does not cross $S$!
- **Subcase 2 ($v \in Y$)**: Apply the identical argument to $\bar{Y} \cap S$ and $\bar{Y} \cup S$ (since $y \in \bar{Y} \cap S$ and $v \notin \bar{Y} \cup S$): $c(\bar{Y} \cap S) \le c(\bar{Y}) = c(Y)$, so $X = \bar{Y} \cap S \subseteq S$ is again a non-crossing minimum $x$-$y$ cut! $\blacksquare$

---

### 3. Step 3: The Reverse-Engineering Scratchpad (Recursive Gusfield Construction & `CF 343 E`)

#### Compilation 25A: Recursive Vertex-Bucket Gomory–Hu Construction (`最小割树` — Zero Graph Contraction!)
Because of Lemma 25.3, to build the Gomory–Hu tree $T_{\text{GH}}$ in competitive programming, **you never need to contract supernodes or modify the graph $G$**!
Instead, maintain a current vertex bucket $B \subseteq V$ (initially $B = V$):
1. **Base Case**: If $|B| \le 1$, return.
2. **Pick Pivots**: Pick any two distinct vertices $u = B[0]$ and $v = B[1]$ from the bucket $B$.
3. **Global Max-Flow Call**: Run Dinic's algorithm between $u$ and $v$ **on the entire original undirected graph $G = (V, E)$** (resetting all edge flows to $0$ before running!). Let $f = \text{MaxFlow}_G(u, v)$.
4. **Add Tree Edge**: Add an undirected edge $(u, v)$ of weight $f$ to $T_{\text{GH}}$.
5. **Partition Bucket $B$ by Residual Reachability**: In the residual graph of $G$, find the set $S \subseteq V$ of vertices reachable from $u$. Split the current bucket $B$ into:
   $$B_L = \{ x \in B : x \in S \} \quad \text{and} \quad B_R = \{ x \in B : x \notin S \}.$$
   *(Note: If you also need the tree edge $(u, v)$ removal to match the exact vertex cut partition of $G$ rather than just pairwise path-minima equivalence—i.e., strict Gomory–Hu Tree vs. Gusfield Cut-Equivalent Tree—for every $x \in V \setminus B$ that was previously attached to $u$ and now lies in $\bar{S}$, re-attach its tree edge from $u$ to $v$. For 99% of CP problems including `[ZJOI2011]`, `[CQOI2016]`, and `CF 343 E`, the simple recursive bucket split already satisfies $\lambda_G(x, y) = \min_{e \in \text{Path}_T(x, y)} w_T(e)$ for all $x, y \in V$!)*
6. **Recurse**: Call `build(B_L)` and `build(B_R)`.

**Why Does Partitioning $B$ Without Contracting $G$ Work?**:
By Lemma 25.3 (Uncrossing), for every pair $x, y \in B_L$, there is a minimum $x$-$y$ cut in $G$ that doesn't cross the minimum $u$-$v$ cut $(S, \bar{S})$. Running $\text{MaxFlow}_G(x, y)$ in the full uncontracted graph $G$ produces the exact same minimum cut capacity as running it in the contracted graph $G / \bar{S}$!
- **Total Calls to Dinic**: Since each step splits a bucket of size $\ge 2$ into two non-empty sub-buckets $B_L \ni u$ and $B_R \ni v$, there are **at most $N - 1$ internal recursion nodes**, hence **exactly $N - 1$ calls to Max-Flow**!

#### Compilation 25B: Optimal Permutation on Gomory–Hu Tree (`CF 343 E — Pumping Stations`)
In `CF 343 E`, we are given an undirected graph $G$ ($N \le 200, M \le 1000$) and asked to find a permutation $p_1, p_2, \dots, p_N$ of $V$ that **maximizes** the total adjacent pairwise flow:
$$\max_{p \in S_N} \sum_{i=1}^{N-1} \lambda_G(p_i, p_{i+1}).$$

Let us compile this using the Gomory–Hu tree $T_{\text{GH}}$:
1. **Step 1 (Upper Bound via Bottleneck Edges)**:
   In $T_{\text{GH}}$, every tree edge $e \in E(T_{\text{GH}})$ partitions $V$ into two non-empty subtrees $(T_1, T_2)$. Since the permutation $p_1, \dots, p_N$ visits all $N$ vertices, there must be at least one index $i_e$ where $p_{i_e}$ and $p_{i_e+1}$ lie on opposite sides of $e$, meaning $e \in \text{Path}_{T_{\text{GH}}}(p_{i_e}, p_{i_e+1})$ and hence $\lambda_G(p_{i_e}, p_{i_e+1}) \le w_T(e)$.
   More strongly, by Hall's Theorem / induction on the minimum-weight edge $e_{\min}$ of $T_{\text{GH}}$, no permutation can exceed the sum of all $N - 1$ tree edge weights:
   $$\sum_{i=1}^{N-1} \lambda_G(p_i, p_{i+1}) \le \sum_{e \in E(T_{\text{GH}})} w_T(e).$$
2. **Step 2 (Constructive Equality via Minimum-Edge Divide-and-Conquer)**:
   How do we order $p_1, \dots, p_N$ so that **every single transition** $\lambda_G(p_i, p_{i+1})$ equals a distinct edge of $T_{\text{GH}}$?
   - Given a subtree $T$, if $|V(T)| = 1$, return the single vertex $[v]$.
   - Otherwise, find the **minimum-weight edge** $e_{\min} = \arg\min_{e \in E(T)} w_T(e)$ inside $T$.
   - Removing $e_{\min}$ splits $T$ into two subtrees $T_L$ and $T_R$.
   - Recursively compute the optimal sequences $P(T_L)$ and $P(T_R)$, and concatenate them:
     $$P(T) := P(T_L) \;\|\; P(T_R).$$
   - **Why does the concatenation junction $(x, y) = (\text{last}(P(T_L)), \text{first}(P(T_R)))$ achieve $\lambda_G(x, y) = w_T(e_{\min})$?**
     Because $x \in T_L$ and $y \in T_R$, the unique path between $x$ and $y$ in $T_{\text{GH}}$ is contained **entirely inside $T$** and passes through $e_{\min}$. Since $e_{\min}$ was chosen as the **minimum-weight edge of the entire subtree $T$**, every other edge on $\text{Path}_T(x, y)$ has weight $\ge w_T(e_{\min})$! Therefore:
     $$\lambda_G(x, y) = \min_{e \in \text{Path}_T(x, y)} w_T(e) = w_T(e_{\min})!$$
   - Every one of the $N - 1$ tree edges is matched to a unique adjacent transition $(p_i, p_{i+1})$, achieving $\sum_{i=1}^{N-1} \lambda_G(p_i, p_{i+1}) = \sum_{e \in E(T_{\text{GH}})} w_T(e)$! (Can also be implemented bottom-up via DSU by sorting tree edges in **descending** order of weight and concatenating vertex lists!)

---

### 4. Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Concrete Numerical Trace ($N = 4$ Graph for Gomory–Hu & `CF 343 E`)
Consider an undirected graph on $V = \{1, 2, 3, 4\}$ with edges:
- $(1, 2)$ weight $10$, $(2, 3)$ weight $10$, $(1, 3)$ weight $5$ (triangle on $\{1, 2, 3\}$), and
- $(3, 4)$ weight $3$, $(2, 4)$ weight $1$.
Let us trace the recursive Gomory–Hu construction:
1. **Call 1 (`B = {1, 2, 3, 4}`, pivots $u = 1, v = 2$)**:
   - $\text{MaxFlow}_G(1, 2) = 15$ (path $1 \to 2$ [10] and $1 \to 3 \to 2$ [5]).
   - Residual reachable set from $1$ is $S = \{1\}$, and $\bar{S} = \{2, 3, 4\}$.
   - Add tree edge $(1, 2)$ of weight $15$.
   - Split bucket into $B_L = \{1\}$ (base case!) and $B_R = \{2, 3, 4\}$.
2. **Call 2 (`B = {2, 3, 4}`, pivots $u = 2, v = 3$)**:
   - Run $\text{MaxFlow}_G(2, 3)$ on the **full graph $G$**:
     - Path $2 \to 3$ [10], $2 \to 1 \to 3$ [5], $2 \to 4 \to 3$ [1] $\implies \text{MaxFlow}_G(2, 3) = 16$.
   - Residual reachable set from $2$ is $S = \{1, 2\}$, and $\bar{S} = \{3, 4\}$.
   - Add tree edge $(2, 3)$ of weight $16$.
   - Split bucket $B = \{2, 3, 4\}$ into $B_L = \{2\}$ and $B_R = \{3, 4\}$.
3. **Call 3 (`B = {3, 4}`, pivots $u = 3, v = 4$)**:
   - Run $\text{MaxFlow}_G(3, 4)$ on the **full graph $G$**:
     - Path $3 \to 4$ [3] and $3 \to 2 \to 4$ [1] $\implies \text{MaxFlow}_G(3, 4) = 4$.
   - Add tree edge $(3, 4)$ of weight $4$.
- **Resulting Gomory–Hu Tree $T_{\text{GH}}$**: A path $1 \stackrel{15}{\longleftrightarrow} 2 \stackrel{16}{\longleftrightarrow} 3 \stackrel{4}{\longleftrightarrow} 4$.
- **Trace of `CF 343 E` Optimal Permutation**:
  - Minimum edge of $T_{\text{GH}}$ is $(3, 4)$ of weight $4$, splitting $T_{\text{GH}}$ into $T_L = \{1, 2, 3\}$ and $T_R = \{4\}$.
  - Minimum edge of $T_L = \{1, 2, 3\}$ is $(1, 2)$ of weight $15$, splitting $T_L$ into $\{1\}$ and $\{2, 3\}$.
  - Minimum edge of $\{2, 3\}$ is $(2, 3)$ of weight $16$, giving $[2, 3]$.
  - Concatenating gives $P = [1, 2, 3, 4]$ (or $[2, 3, 1, 4]$), with adjacent min-cuts:
    $$\lambda(2, 3) + \lambda(3, 1) + \lambda(1, 4) = 16 + 15 + 4 = 35 = \sum_{e \in T_{\text{GH}}} w_T(e)!$$

#### Broken Gadget Counterexamples & Classic Bugs
1. **The #1 Fatal Gomory–Hu Bug: Running Max-Flow on the Induced Subgraph $G[B]$ Instead of $G$**:
   - *Bug*: When recursing on bucket $B = \{3, 4\}$ in Call 3 above, building the flow network using only vertices in $B = \{3, 4\}$.
   - *Why it fails*: In $G[\{3, 4\}]$, the only edge between $3$ and $4$ has weight $3$, missing the path $3 \to 2 \to 4$ of weight $1$ that routes through vertex $2 \notin B$! Every single Max-Flow call MUST be executed on the **entire original graph $G = (V, E)$**; the bucket $B$ only restricts which two pivots $(u, v)$ we test and which vertices we partition for future recursion.
2. **Attempting to Build a Gomory–Hu Tree on a Directed Graph**:
   - *Counterexample*: Consider the directed 3-cycle $1 \stackrel{10}{\longrightarrow} 2 \stackrel{10}{\longrightarrow} 3 \stackrel{10}{\longrightarrow} 1$. Here $\text{MinCut}(1 \to 2) = 10$, $\text{MinCut}(2 \to 1) = 10$, etc., if bidirectional? No: $\text{MinCut}(1 \to 2) = 10$, $\text{MinCut}(2 \to 3) = 10$, $\text{MinCut}(3 \to 1) = 10$. Even if you define symmetric capacity, directed cuts do not satisfy posimodularity $c(A) + c(B) \ge c(A \setminus B) + c(B \setminus A)$, so Lemma 25.3 (Uncrossing) fails on general directed graphs! (For directed graphs, Schnorr 1979 proved you need a directed cactus/cycle-tree of $O(N \log N)$ flows, not a simple Gomory–Hu tree.)

---

## Master Recognition & Compilation Decision Table (Iterations 21–25)

| Iteration & Archetype | Non-Graph / Surface Diagnostic Signal | Algebraic Intermediate Form | Compiled Graph / Non-Flow Target | Complexity | Primary Pitfall to Avoid |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Iter 21: 0-1 Fractional Cut / Closure**<br>(`分数规划最小割`) | Ratio objective $\min \frac{N(S)}{D(S)}$ or $\max \frac{P(S)}{C(S)}$ with $D(S) > 0$ and closure/cut constraints; $N \le 10^3$. | $h(\lambda) = \min_{S \in \mathcal{F}} \big(N(S) - \lambda D(S)\big)$; root $h(\lambda^*) = 0$. | Dynamic $s$-$t$ Min-Cut per $\lambda$; split net vertex weights $w_v(\lambda) = p_v - \lambda c_v$ by sign to $s$ or $t$; solve via Dinkelbach secant steps. | $O(\text{Dinic} \cdot \log(\frac{1}{\epsilon}))$ or $5\text{--}12$ Dinkelbach calls. | Failing to handle $S = \emptyset$ clamping $h(\lambda)$ to $0$; passing negative capacities $a_e - \lambda b_e < 0$ into Dinic. |
| **Iter 22: Maximum Density Subgraph**<br>(`最大密度子图` — Goldberg) | Maximize $\frac{W(E(S)) + P(S)}{|S|}$ over $\emptyset \neq S \subseteq V$; dense graph $|E| \gg |V|$. | $2W(E(S)) = \sum_{v \in S} \deg_w(v) - W(\delta(S, \bar{S}))$. | **$\|V\| + 2$ vertices only**: $c(s \to v) = U$, $c(v \to t) = U + 2\lambda c_v - 2p_v - \deg_w(v)$, $c(u \leftrightarrow v) = w_{uv}$. | $O(\text{Dinic}(\|V\|, \|E\|) \cdot \log \|V\|)$. | Omitting factor of $2$ on $\lambda$; extracting $S^*$ at $\lambda = R$ where $S^* = \emptyset$ instead of $\lambda = L$. |
| **Iter 23: Planar Dual Min-Cut**<br>(`平面图最小割转对偶最短路`) | Planar/grid graph with $N, M \le 1000$ ($V \le 10^6$), or continuous grid potential $\sum w_{uv}\max(0, h_v - h_u)$ (`[NOI2010] 海拔`). | Coarea integral $\int_0^1 \text{Cut}(S_\lambda) d\lambda$ reduces continuous $h \in [0, 1]$ to binary $h \in \{0, 1\}$; Cycle–Cut Duality $G \leftrightarrow G^*$. | Split outer face at $s, t$ into $S^*, T^*$; rotate directed primal edges $90^\circ$ to form $G^*$; run single Dijkstra $S^* \to T^*$. | $O(V \log V)$. | Rotating primal directed edges $90^\circ$ the wrong way (computing $t$-$s$ cut instead of $s$-$t$ cut). |
| **Iter 24: Max-Flow via Min-Cut DP / Greedy**<br>(`最大流转最小割 DP`) | Explicit/implicit Max-Flow on $N \le 10^4\text{--}10^5$ with structured cross-edges (complete DAG $i < j$, tree, intervals). | $\min_{x \in \{0,1\}^N} \sum p_i(1-x_i) + \sum s_i x_i + \sum c_{ij} x_i(1-x_j)$. | Discard flow graph; run $O(N^2)$ prefix DP, $O(N \log N)$ decoupled greedy sort (`CF 724 E`), or $O(N)$ Tree DP / $O(\log^2 N)$ DDP. | $O(N \log N)$ or $O(N^2)$ or $O(N)$. | Swapping $p_i$ and $s_i$ ($x_i = 1 \iff i \in S$ severs sink edge $s_i$, not source edge $p_i$). |
| **Iter 25: Stoer–Wagner & Gomory–Hu Tree**<br>(`全局最小割与最小割树`) | Global undirected min-cut, or $Q \le 10^5$ pairwise $\text{MinCut}(u, v)$ queries / permutation sum $\sum \lambda(p_i, p_{i+1})$ (`CF 343 E`). | Ultrametric $\lambda(u, w) \ge \min(\lambda(u, v), \lambda(v, w))$ & Submodular Uncrossing Lemma. | Stoer–Wagner MAS ($N-1$ phases), or Recursive Gusfield Tree ($N-1$ Dinic calls on full graph $G$). | $O(VE + V^2 \log V)$ or $(N-1) \cdot T_{\text{Dinic}}$. | Running Max-Flow on induced subgraph $G[B]$ of bucket $B$ instead of the full original graph $G$! |

---

## 4-Tier Curated Problem Bank (Part 1: Stepping Stone & Intermediate — 11 Fully Solved Problems)

> **Pedagogical Note**: Every problem below is a genuine non-template problem requiring structural recognition, algebraic transformation, or duality elimination. Bare template verification problems are quarantined at the end of the monograph.

---

### Tier 1: Stepping Stone Problems (Problems 1–5)

#### Problem 1: `[BJWC2006] 狼抓兔子` (Wolf Catches Rabbits)
- **Judge URL**: [Luogu P4001](https://www.luogu.com.cn/problem/P4001) / [BZOJ 1001](https://darkbzoj.cc/problem/1001) (`[ZH]`)
- **Archetype**: Undirected $s$-$t$ Planar Grid Min-Cut $\leftrightarrow$ Dual Graph Dijkstra (Iteration 23)
- **Problem Statement & Constraints**:
  An $N \times M$ grid of vertices ($1 \le N, M \le 1000$) has undirected weighted edges connecting:
  1. Horizontal neighbors $(i, j) \leftrightarrow (i, j+1)$,
  2. Vertical neighbors $(i, j) \leftrightarrow (i+1, j)$, and
  3. Diagonal neighbors $(i, j) \leftrightarrow (i+1, j+1)$ inside every unit cell.
  Find the minimum total weight of edges to block so that rabbits cannot travel from the top-left corner $s = (1, 1)$ to the bottom-right corner $t = (N, M)$ (or equivalently the maximum number of rabbits that can pass if edge weights are capacities).
- **Step 1: Non-Graph / Geometric Diagnostic Signal**:
  The problem asks for the Maximum Flow / Minimum $s$-$t$ Cut on a planar graph with $V = NM \le 10^6$ vertices and $E \approx 3 NM \le 3 \times 10^6$ edges. Dinic's algorithm can pass on loose time limits, but $V = 10^6$ is tailor-made for **$s$-$t$ Planar Dual Shortest Path** in $O(V \log V)$.
- **Step 2 & 3: Algebraic-to-Dual Compilation Scratchpad**:
  - Every unit square $[i, i+1] \times [j, j+1]$ ($1 \le i < N, 1 \le j < M$) is split by the diagonal $(i, j)\text{--}(i+1, j+1)$ into two triangular faces:
    - **Lower-Left Triangle** $F_{\text{low}}(i, j)$ with vertices $(i, j), (i+1, j), (i+1, j+1)$, and
    - **Upper-Right Triangle** $F_{\text{up}}(i, j)$ with vertices $(i, j), (i, j+1), (i+1, j+1)$.
  - Split the unbounded outer face at $s = (1, 1)$ and $t = (N, M)$ into:
    - **Dual Source $S^*$** (Lower-Left perimeter: left column $j = 1$ and bottom row $i = N$),
    - **Dual Sink $T^*$** (Upper-Right perimeter: top row $i = 1$ and right column $j = M$).
  - Connect dual vertices with undirected edges matching the primal edges they cross:
    - Diagonal $(i, j)\text{--}(i+1, j+1)$ connects $F_{\text{low}}(i, j) \leftrightarrow F_{\text{up}}(i, j)$.
    - Horizontal $(i, j)\text{--}(i, j+1)$ connects $F_{\text{up}}(i, j) \leftrightarrow F_{\text{low}}(i-1, j)$ (or $T^*$ if $i = 1$, $S^*$ if $i = N$).
    - Vertical $(i, j)\text{--}(i+1, j)$ connects $F_{\text{low}}(i, j) \leftrightarrow F_{\text{up}}(i, j-1)$ (or $S^*$ if $j = 1$, $T^*$ if $j = M$).
- **Step 4: Complete Solution & Degenerate Edge Case**:
  - **Crucial Edge Case ($N = 1$ or $M = 1$)**: When $N = 1$ or $M = 1$, there are $0$ interior triangles! The primal graph is just a single path of $\max(N, M) - 1$ edges, and the minimum cut is simply the minimum single edge weight $\min_e w_e$ along that path (or $0$ if $N = M = 1$).
  - For $N, M \ge 2$, the dual graph has $V^* = 2(N-1)(M-1) + 2 \le 2 \times 10^6$ vertices and $E^* \le 3 \times 10^6$ edges. Run a single Dijkstra from $S^*$ to $T^*$ in $O(NM \log(NM))$ time.

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 1
- **Hint 1 (Diagnostic)**: Running Max-Flow on $10^6$ vertices is risky. Notice that the graph has zero crossing edges and $s=(1,1), t=(N,M)$ lie on the outer perimeter.
- **Hint 2 (Compilation)**: Split each unit cell $(i, j)$ into two dual nodes (lower-left triangle and upper-right triangle). Which outer boundary belongs to $S^*$ and which to $T^*$?
- **Hint 3 (Edge Case)**: What happens to your dual graph indexing when $N = 1$ or $M = 1$? Handle $N=1$ or $M=1$ separately by taking the minimum edge weight!
:::

---

#### Problem 2: `UVa 1389 / POJ 3155 — Hard Life` (`最大密度子图` Flagship)
- **Judge URL**: [POJ 3155](http://poj.org/problem?id=3155) / [UVa 1389](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4135) (`[EN]` / `[ZH]` Amber 2007 Monograph Problem 1)
- **Archetype**: Unweighted Maximum Density Subgraph + Exact Vertex Set Reconstruction (Iteration 22)
- **Problem Statement & Constraints**:
  Given an undirected graph $G = (V, E)$ with $N \le 100$ employees and $M \le 1000$ conflict pairs, find a non-empty subset $\emptyset \neq S \subseteq V$ maximizing $\frac{|E(S)|}{|S|}$, and output the indices of the vertices in $S$ in sorted order.
- **Step 1: Non-Graph Diagnostic Signal**:
  Maximizing a ratio $\frac{|E(S)|}{|S|}$ over non-empty subsets $S \subseteq V$ is the canonical Maximum Density Subgraph problem.
- **Step 2 & 3: Algebraic-to-Graph Compilation Scratchpad**:
  - Using Goldberg's identity $2|E(S)| = \sum_{v \in S} \deg(v) - |\delta(S, \bar{S})|$, for trial $\lambda \ge 0$ we minimize $|\delta(S, \bar{S})| + \sum_{v \in S} (2\lambda - \deg(v))$.
  - Set $U = M$ (or $\max_v \deg(v)$). Build $G_\lambda$ on $N + 2$ vertices:
    - $c(s \to v) = U$ for all $v \in V$.
    - $c(v \to t) = U + 2\lambda - \deg(v)$ for all $v \in V$.
    - $c(u \to v) = c(v \to u) = 1$ for each $(u, v) \in E$.
  - Then $\max_{S \subseteq V} (|E(S)| - \lambda |S|) = \frac{UN - \text{MinCut}(G_\lambda)}{2}$.
- **Step 4: Complete Solution & Precision Contract**:
  - **Edge Case ($M = 0$)**: If $M = 0$, output a single vertex `{1}` immediately (density $0/1 = 0$).
  - **Binary Search Termination Gap**: Any two distinct rational ratios $\frac{e_1}{n_1} \neq \frac{e_2}{n_2}$ with $1 \le n_1, n_2 \le N$ differ by at least $\frac{1}{n_1 n_2} \ge \frac{1}{N(N-1)}$. Set `L = 0, R = M`, and bisect until $R - L < \frac{1}{N^2}$ ($\approx 10^{-4}$, about 25 iterations).
  - **Subgraph Extraction**: Run one final Dinic at $\lambda = L$ (NOT $R$!) and perform a DFS from $s$ in the residual network (following edges with residual capacity $> 10^{-8}$) to collect $S^*$. Total complexity: $O(\log N \cdot \text{Dinic}(N, N + M))$.

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 2
- **Hint 1 (Diagnostic)**: Binary search on the target density $\lambda$. How can you check if $\max_{S \neq \emptyset} (|E(S)| - \lambda |S|) > 0$ using a graph on only $N + 2$ vertices instead of $N + M + 2$?
- **Hint 2 (Compilation)**: Use $2|E(S)| = \sum_{v \in S} \deg(v) - |\delta(S, \bar{S})|$ and shift capacities by $U = M$ so $c(s \to v) = U$ and $c(v \to t) = U + 2\lambda - \deg(v) \ge 0$.
- **Hint 3 (Edge Cases)**: What is the minimum difference between two fractions with denominator $\le N$? And why must you reconstruct the reachable vertex set at $\lambda = L$ rather than $\lambda = R$?
:::

---

#### Problem 3: `[ZJOI2011] 最小割` (All-Pairs Min-Cut Threshold Queries)
- **Judge URL**: [Luogu P3329](https://www.luogu.com.cn/problem/P3329) / [BZOJ 2229](https://darkbzoj.cc/problem/2229) (`[ZH]`)
- **Archetype**: Gomory–Hu / Gusfield Cut Tree Construction + Bottleneck Queries (Iteration 25)
- **Problem Statement & Constraints**:
  Given an undirected weighted graph $G = (V, E)$ with $N \le 150$ vertices and $M \le 3000$ edges, answer $Q \le 30$ queries. Each query gives an integer $X$ and asks: how many unordered pairs $\{u, v\}$ ($1 \le u < v \le N$) have $\text{MinCut}_G(u, v) \le X$? ($T \le 10$ test cases.)
- **Step 1: Non-Graph Diagnostic Signal**:
  We need the values of $\text{MinCut}_G(u, v)$ for all $\binom{N}{2} = 11,175$ pairs across $T = 10$ test cases. Running $10 \times 11,175$ Max-Flows is impossible, so we need a **Gomory–Hu Cut Tree (`最小割树`)**.
- **Step 2 & 3: Algebraic-to-Tree Compilation Scratchpad**:
  - Construct the Gomory–Hu tree $T_{\text{GH}}$ recursively on vertex bucket $B$ (initially $\{1, \dots, N\}$) using $N - 1$ calls to Dinic on the **full original graph $G$**.
  - By Theorem 25.3, for every pair $u < v$, $\text{MinCut}_G(u, v) = \min_{e \in \text{Path}_{T_{\text{GH}}}(u, v)} w_T(e)$.
- **Step 4: Complete Solution & Complexity**:
  - Once $T_{\text{GH}}$ is built in $N - 1$ Max-Flow calls, run a simple $O(N)$ DFS from each root $u \in \{1, \dots, N\}$ on $T_{\text{GH}}$ to compute all $\binom{N}{2}$ path-minimum values in $O(N^2)$ time (or sort tree edges descending and merge with DSU in $O(N \log N)$).
  - Sort the $\binom{N}{2}$ values and answer each query $X$ in $O(\log N)$ via `std::upper_bound`. Total time per testcase: $(N - 1) \cdot T_{\text{Dinic}}(N, M) + O(N^2 \log N)$.

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 3
- **Hint 1 (Diagnostic)**: You cannot run Dinic $\binom{N}{2}$ times. How many Max-Flow calls are needed to encode all pairwise minimum cuts of an undirected graph into a tree?
- **Hint 2 (Compilation)**: Use recursive vertex-bucket partitioning `build(B)`: pick $u = B[0], v = B[1]$, run Max-Flow on the **entire graph $G$**, add tree edge $(u, v)$, and split $B$ by $s$-reachability in the residual graph.
- **Hint 3 (Edge Case)**: Remember to reset all edge flows to $0$ in $G$ before each of the $N - 1$ Dinic calls!
:::

---

#### Problem 4: `[CQOI2016] 不同的最小割` (Distinct Minimum Cut Values)
- **Judge URL**: [Luogu P4123](https://www.luogu.com.cn/problem/P4123) / [BZOJ 4519](https://darkbzoj.cc/problem/4519) (`[ZH]`)
- **Archetype**: Ultrametric Spectrum of Gomory–Hu Cut Trees (Iteration 25)
- **Problem Statement & Constraints**:
  Given an undirected weighted graph $G = (V, E)$ with $N \le 850$ vertices and $M \le 8500$ edges, count how many **distinct numerical values** appear among $\text{MinCut}_G(u, v)$ over all $\binom{N}{2}$ unordered pairs $\{u, v\}$.
- **Step 1: Non-Graph Diagnostic Signal**:
  Direct application of the Ultrametric Theorem (Theorem 25.1) and Gomory–Hu Trees.
- **Step 2 & 3: Algebraic-to-Tree Compilation Scratchpad**:
  - Every tree edge $e = (u, v) \in E(T_{\text{GH}})$ has weight $w_T(e) = \lambda_G(u, v)$, so every weight appearing on $T_{\text{GH}}$ is achieved by at least one pair $(u, v)$.
  - Conversely, for any pair $(x, y)$, $\lambda_G(x, y) = \min_{e \in \text{Path}_{T_{\text{GH}}}(x, y)} w_T(e)$ equals the weight of some edge $e \in E(T_{\text{GH}})$!
  - Therefore:
    $$\{\, \lambda_G(u, v) : 1 \le u < v \le N \,\} = \{\, w_T(e) : e \in E(T_{\text{GH}}) \,\}.$$
- **Step 4: Complete Solution & Complexity**:
  Run the recursive Gusfield / Gomory–Hu construction ($N - 1$ Dinic calls on $G$), insert the $N - 1$ resulting flows into a `std::set<long long>`, and print `set.size()`. Complexity: $(N - 1) \cdot T_{\text{Dinic}}(N, M)$.

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 4
- **Hint 1 (Diagnostic)**: By the ultrametric inequality $\lambda(u, w) \ge \min(\lambda(u, v), \lambda(v, w))$, how many distinct values can $\lambda(u, v)$ take at most?
- **Hint 2 (Compilation)**: In a Gomory–Hu tree $T_{\text{GH}}$, every path minimum is the weight of one of the $N - 1$ tree edges, and every tree edge weight is itself a pairwise min-cut!
- **Hint 3 (Conclusion)**: You don't even need to build the tree adjacency list—just record the $N - 1$ Max-Flow values produced during the recursive bucket splits and count how many are distinct!
:::

---

#### Problem 5: `[BZOJ 2039] 人员雇佣` (Employ — Pairwise Synergy Matrix)
- **Judge URL**: [Luogu P3973](https://www.luogu.com.cn/problem/P3973) / [BZOJ 2039](https://darkbzoj.cc/problem/2039) (`[ZH]`)
- **Archetype**: Goldberg Degree-Summation Eliminating $O(N^2)$ Auxiliary Closure Nodes (Iteration 22 / Iteration 24)
- **Problem Statement & Constraints**:
  A company can hire any subset $S \subseteq \{1, \dots, N\}$ of $N \le 1000$ candidates. Hiring candidate $i$ costs $A_i \ge 0$. For every ordered pair $(i, j)$ ($1 \le i, j \le N$), a synergy value $E_{ij} = E_{ji} \ge 0$ is given:
  - If both $i \in S$ and $j \in S$, the company gains $+2 E_{ij}$.
  - If $i \in S$ and $j \notin S$, the company pays a penalty of $-E_{ij}$.
  Find the maximum net profit over all subsets $S \subseteq \{1, \dots, N\}$.
- **Step 1: Non-Graph Diagnostic Signal**:
  This is a binary partitioning problem ($x_i \in \{0, 1\}$) with $N = 1000$ and a **dense $N \times N$ interaction matrix** $E_{ij}$. A naive Project Selection model introduces $N^2 = 10^6$ auxiliary vertices (one per pair $(i, j)$), causing MLE/TLE. We must apply Goldberg's degree-summation identity to collapse the graph to $N + 2$ vertices!
- **Step 2 & 3: Algebraic-to-Graph Compilation Scratchpad**:
  - Let $x_i = [i \in S] \in \{0, 1\}$. For each ordered pair $(i, j)$, if $x_i = 1$ and $x_j = 1$ the company gains $+E_{ij}$ (so an unordered pair $\{i, j\}$ with $i, j \in S$ contributes $E_{ij} + E_{ji} = 2 E_{ij}$), whereas if $x_i = 1$ and $x_j = 0$ the company pays a penalty of $-E_{ij}$ for that ordered pair (so if $i \in S, j \notin S$, both $(i, j)$ and $(j, i)$ are separated, losing $E_{ij}$ from $(i, j)$ and $E_{ji}$ from $(j, i)$).
  - Thus the net profit for indicator vector $x \in \{0, 1\}^N$ is:
    $$\text{Profit}(x) = \sum_{i=1}^N \sum_{j=1}^N E_{ij} x_i x_j - \sum_{i=1}^N \sum_{j=1}^N E_{ij} x_i(1 - x_j) - \sum_{i=1}^N A_i x_i.$$
  - Apply the algebraic identity $x_i x_j = x_i - x_i(1 - x_j)$ to eliminate every quadratic term $x_i x_j$:
    $$E_{ij} x_i x_j - E_{ij} x_i(1 - x_j) = E_{ij} x_i - 2 E_{ij} x_i(1 - x_j).$$
  - Define the row sum $D_i := \sum_{j=1}^N E_{ij}$. Summing over all $1 \le i, j \le N$ yields:
    $$\text{Profit}(x) = \sum_{i=1}^N D_i - \left( \sum_{i=1}^N D_i (1 - x_i) + \sum_{i=1}^N A_i x_i + \sum_{i=1}^N \sum_{j=1}^N 2 E_{ij} x_i(1 - x_j) \right)!$$
- **Step 4: Complete Graph Construction & Complexity**:
  - Build an $s$-$t$ network on **only $N + 2$ vertices**:
    - Edge $s \to i$ with capacity $D_i = \sum_{j=1}^N E_{ij}$ (cut if $x_i = 0$, forfeiting $D_i$).
    - Edge $i \to t$ with capacity $A_i$ (cut if $x_i = 1$, paying hiring cost $A_i$).
    - For every $i \neq j$, directed edge $i \to j$ with capacity $2 E_{ij}$ (or undirected edge of capacity $2 E_{ij}$ since $E_{ij} = E_{ji}$, cut if $x_i \neq x_j$).
  - Answer is $\sum_{i=1}^N D_i - \text{MinCut}(s, t)$. Running Dinic on $N = 1000, M = 10^6$ finishes in $< 0.2$s.

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 5
- **Hint 1 (Diagnostic)**: Creating a node for every pair $(i, j)$ gives $10^6$ vertices. How can you express $x_i x_j$ purely in terms of linear $x_i$ and cut terms $x_i(1 - x_j)$?
- **Hint 2 (Compilation)**: Use the identity $x_i x_j - x_i(1 - x_j) = x_i - 2 x_i(1 - x_j)$.
- **Hint 3 (Full Construction)**: Connect $s \to i$ with capacity $\sum_j E_{ij}$, $i \to t$ with capacity $A_i$, and $i \to j$ with capacity $2 E_{ij}$.
:::

---

### Tier 2: Intermediate Problems (Problems 6–11)

#### Problem 6: `[HNOI/TJOI] Minimum Ratio Network Cut` (UVa 1389 / POJ 2976 Network Variant)
- **Judge URL**: [Luogu P4322 / Ratio Cut Series](https://www.luogu.com.cn/problem/P3705) / `0-1 Fractional Cut` (`[ZH]` Amber 2007 Section 3)
- **Archetype**: 0-1 Fractional Programming on Edge Cuts with Negative-Weight Greedy Severing (Iteration 21)
- **Problem Statement & Constraints**:
  Given an undirected connected graph $G = (V, E)$ ($N \le 100, M \le 400$) with source $s$, sink $t$, and two positive weights $(a_e, b_e)$ on each edge $e \in E$, find an edge subset $C \subseteq E$ whose removal disconnects $s$ and $t$ and minimizes the ratio:
  $$\min_{C \subseteq E \text{ disconnects } s, t} \frac{\sum_{e \in C} a_e}{\sum_{e \in C} b_e}.$$
- **Step 1: Non-Graph Diagnostic Signal**:
  Minimizing a quotient of edge sums over all $s$-$t$ disconnecting edge sets $C \subseteq E$.
- **Step 2 & 3: Algebraic-to-Graph Compilation Scratchpad**:
  - For trial $\lambda > 0$, define $w_e(\lambda) := a_e - \lambda b_e$. We want to find $h(\lambda) = \min_{C} \sum_{e \in C} w_e(\lambda)$.
  - **Key Sign Split**: Because $C$ can be *any* edge subset whose removal disconnects $s$ and $t$ (not restricted to minimal cuts), any edge $e$ with $w_e(\lambda) \le 0$ decreases or leaves unchanged the sum $\sum_{e \in C} w_e(\lambda)$ and helps disconnect $s$ and $t$!
  - Therefore, partition $E$ into $E^-(\lambda) = \{ e \in E : w_e(\lambda) \le 0 \}$ and $E^+(\lambda) = \{ e \in E : w_e(\lambda) > 0 \}$:
    1. **Unconditionally sever all $e \in E^-(\lambda)$**: Add their negative weights to `neg_sum = \sum_{e \in E^-(\lambda)} (a_e - \lambda b_e)` and omit them from the flow graph.
    2. **Run Min-Cut on $E^+(\lambda)$**: Add each $e \in E^+(\lambda)$ to the flow network with positive capacity $a_e - \lambda b_e > 0$ and compute $\text{MinCut}(G^+_\lambda)$.
    3. Total parametric minimum is $h(\lambda) = \text{neg\_sum} + \text{MinCut}(G^+_\lambda)$.
- **Step 4: Complete Solution & Complexity**:
  Use Dinkelbach's algorithm or binary search on $\lambda \in [0, \max_e (a_e / b_e)]$: if $h(\lambda) < 0$, $\lambda$ is too large ($R = \lambda$); if $h(\lambda) > 0$, $\lambda$ is too small ($L = \lambda$). Runs in $O(\log(\frac{1}{\epsilon}) \cdot \text{Dinic}(N, M))$.

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 6
- **Hint 1 (Diagnostic)**: Apply 0-1 Fractional Programming: each edge gets weight $w_e(\lambda) = a_e - \lambda b_e$. What happens when $w_e(\lambda) < 0$?
- **Hint 2 (Compilation)**: Since cutting more edges never reconnects $s$ and $t$, any edge with $w_e(\lambda) \le 0$ should be cut immediately for free (negative cost)!
- **Hint 3 (Edge Case)**: Only edges with $w_e(\lambda) > 0$ are inserted into Dinic's graph; if $s$ and $t$ are already disconnected after removing $E^-(\lambda)$, $\text{MinCut}(G^+_\lambda) = 0$ and $h(\lambda) = \text{neg\_sum} \le 0$.
:::

---

#### Problem 7: `CF 847 J — Students Initiation` (Minimum Maximum Indegree Orientation $\leftrightarrow$ Pseudo-Arboricity & Maximum Density Subgraph)
- **Judge URL**: [Codeforces 847J](https://codeforces.com/problemset/problem/847/J) (`[EN]`)
- **Archetype**: Hakimi's Orientation Duality $\leftrightarrow$ Maximum Density Subgraph $\lceil \max_S \frac{|E(S)|}{|S|} \rceil$ (Iteration 22)
- **Problem Statement & Constraints**:
  Given an undirected graph $G = (V, E)$ with $N \le 5000$ vertices and $M \le 5000$ edges, orient every edge $e = (u, v)$ as either $u \to v$ or $v \to u$ so as to **minimize the maximum outdegree** (or indegree) of any vertex:
  $$k^* = \min_{\text{orientations}} \max_{v \in V} \text{outdeg}(v),$$
  and output both $k^*$ and the explicit orientation of all $M$ edges.
- **Step 1: Non-Graph Diagnostic Signal**:
  Minimizing the maximum load on endpoints when assigning each edge $e = (u, v)$ to one of its two endpoints $u$ or $v$.
- **Step 2 & 3: Algebraic Duality with Maximum Density Subgraph**:
  - **Theorem (Hakimi 1965 / Max-Flow Min-Cut Duality)**: *An undirected graph $G = (V, E)$ has an orientation with $\max_{v \in V} \text{outdeg}(v) \le k$ if and only if the Maximum Density Subgraph of $G$ has density at most $k$:*
    $$\max_{\emptyset \neq S \subseteq V} \frac{|E(S)|}{|S|} \le k \quad \Longleftrightarrow \quad k^* = \left\lceil \max_{\emptyset \neq S \subseteq V} \frac{|E(S)|}{|S|} \right\rceil.$$
  - *Proof via Bipartite / Goldberg Min-Cut*:
    For a trial integer $k$, each edge $e \in E$ must be assigned to one of its two endpoints, and each vertex $v \in V$ can accept at most $k$ incident edges.
    In Goldberg's $|V|+2$ formulation (or the bipartite edge-to-vertex network where $s \to e$ has capacity $1$, $e \to u, e \to v$ have capacity $1$, and $v \to t$ has capacity $k$), cutting $S \subseteq V$ on the sink side leaves $|E(S)|$ edges completely trapped inside $S$, which can absorb at most $k|S|$ units of flow into $t$. Thus the minimum cut is $M - \max_{S \subseteq V} (|E(S)| - k|S|)$, which equals $M$ iff $|E(S)| - k|S| \le 0$ for all $S$!
- **Step 4: Complete Solution & Complexity**:
  Binary search on integer $k \in [0, M]$ ($13$ steps). Since $N, M \le 5000$ and the bipartite graph has unit capacities on edges, Dinic runs in $O((N+M)\sqrt{N+M})$ per check, easily passing in $O(M \sqrt{N} \log M)$ time.

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 7
- **Hint 1 (Diagnostic)**: Directing $u \to v$ means vertex $u$ "pays" 1 unit of outdegree for edge $e = (u, v)$. Binary search on the maximum allowed outdegree $k$.
- **Hint 2 (Compilation)**: Build a bipartite flow network: source $s$ sends $1$ unit to each edge $e \in E$; $e$ connects to its two endpoints $u, v$ (cap $1$); each vertex $v$ connects to sink $t$ with capacity $k$.
- **Hint 3 (Duality Connection)**: Notice that all $M$ edges are saturated iff $\max_{S \subseteq V} (|E(S)| - k|S|) \le 0$, which is literally the integer decision version of Goldberg's Maximum Density Subgraph!
:::

---

#### Problem 8: `CF 724 E — Goods Transportation`
- **Judge URL**: [Codeforces 724E](https://codeforces.com/problemset/problem/724/E) (`[EN]`)
- **Archetype**: Solving Max-Flow via Min-Cut DP & $O(N \log N)$ Greedy Decoupling (Iteration 24)
- **Problem Statement & Constraints**:
  There are $N \le 10^4$ cities in a line $1, 2, \dots, N$. City $i$ produces $p_i$ units of goods and can sell at most $s_i$ units locally ($0 \le p_i, s_i \le 10^9$). For every pair of cities $(i, j)$ with $1 \le i < j \le N$, at most $c$ units of goods ($0 \le c \le 10^9$) can be transported from city $i$ to city $j$. Find the maximum total units of goods that can be sold across all cities.
- **Step 1: Non-Graph Diagnostic Signal**:
  This is explicitly a Maximum Flow problem with $N = 10^4$ vertices and $\binom{N}{2} \approx 5 \times 10^7$ internal edges. Dinic is impossible; we must invoke **Max-Flow = Min-Cut** and optimize the binary cut partition $x_i \in \{0, 1\}$.
- **Step 2 & 3: Algebraic-to-DP / Greedy Compilation Scratchpad**:
  - As derived in Iteration 24 (Model 24A), let $S = \{ i : x_i = 1 \}$ be the set of cities on the source side of the cut, with $|S| = k$:
    $$\text{MinCut} = \min_{S \subseteq \{1, \dots, N\}} \left( \sum_{i \notin S} p_i + \sum_{i \in S} s_i + \sum_{i \in S} \sum_{j > i, \, j \notin S} c \right).$$
  - Using $\sum_{i \in S} |\{ j > i : j \notin S \}| = \sum_{i \in S} (N - i) - \binom{|S|}{2}$, this rewrites to:
    $$\text{MinCut} = \sum_{i=1}^N p_i + \min_{0 \le k \le N} \left( -\binom{k}{2} c + \min_{|S| = k} \sum_{i \in S} \big( s_i - p_i + (N - i) c \big) \right).$$
- **Step 4: Complete Solution & Complexity**:
  - Compute $w_i = s_i - p_i + (N - i) c$ for $i = 1, \dots, N$.
  - Sort $w_1, \dots, w_N$ in ascending order in $O(N \log N)$ time.
  - Evaluate $\sum_{i=1}^N p_i + \sum_{r=1}^k w_{(r)} - \frac{k(k-1)}{2} c$ for each $k \in \{0, 1, \dots, N\}$ and take the minimum.
  - Time Complexity: $O(N \log N)$, Space Complexity: $O(N)$ (compared to $O(N^2)$ time for the prefix DP).

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 8
- **Hint 1 (Diagnostic)**: The problem literally asks for Max-Flow, but $N = 10^4$ and $|E| = \binom{N}{2}$. By Max-Flow Min-Cut Duality, each city $i$ is simply assigned to $S$ or $T$!
- **Hint 2 (Compilation)**: If $i \in S$, you cut $i \to t$ (cost $s_i$). If $i \in T$, you cut $s \to i$ (cost $p_i$) PLUS $c$ for every earlier city $j < i$ that was placed in $S$. This immediately gives an $O(N^2)$ DP `dp[i][k]`.
- **Hint 3 ($O(N \log N)$ Upgrade)**: Notice that for any subset $S$ of size $k$, the number of pairs $(i, j)$ with $i < j$ and both $i, j \in S$ is always $\binom{k}{2}$. Use this to decouple the cost of putting $i \in S$ into $w_i = s_i - p_i + (N-i)c$ and just sort $w_i$!
:::

---

#### Problem 9: `[NOI2006] 最大获利 — Ratio & Generalized Density Variant`
- **Judge URL**: [Luogu P4174](https://www.luogu.com.cn/problem/P4174) (Base) + Fractional Programming Extension (`[ZH]` Amber 2007 Section 4)
- **Archetype**: Generalized Vertex- & Edge-Weighted Maximum Density Subgraph via Goldberg + Dinkelbach (Iterations 21 & 22)
- **Problem Statement & Constraints**:
  Given $N \le 5000$ base stations (each with construction cost $c_v > 0$ and standalone municipal subsidy $p_v \ge 0$) and $M \le 50,000$ communication links $e = (u, v)$ (each generating profit $w_e > 0$ if **both** stations $u$ and $v$ are built), find a non-empty subset $\emptyset \neq S \subseteq V$ maximizing the return-on-investment ratio:
  $$\max_{\emptyset \neq S \subseteq V} \frac{\sum_{e \in E(S)} w_e + \sum_{v \in S} p_v}{\sum_{v \in S} c_v}.$$
- **Step 1: Non-Graph Diagnostic Signal**:
  Ratio maximization where the numerator has pairwise synergy $w_e x_u x_v$ and vertex profits $p_v x_v$, and the denominator has vertex costs $c_v x_v$.
- **Step 2 & 3: Algebraic-to-Graph Compilation Scratchpad**:
  - Using Goldberg's identity $2\sum_{e \in E(S)} w_e = \sum_{v \in S} \deg_w(v) - W(\delta(S, \bar{S}))$, for trial $\lambda > 0$:
    $$2\Big(W(E(S)) + P(S) - \lambda C(S)\Big) = \sum_{v \in S} \big(\deg_w(v) + 2p_v - 2\lambda c_v\big) - W(\delta(S, \bar{S})).$$
  - Rather than adding a uniform shift $U$ to all vertices, we can apply **Dynamic Sign Splitting (Iteration 21)** to keep capacities as small as possible for Dinic:
    - Let $\beta_v(\lambda) := \deg_w(v) + 2p_v - 2\lambda c_v$.
    - If $\beta_v(\lambda) > 0$: connect $s \to v$ with capacity $\beta_v(\lambda)$, and add $\beta_v(\lambda)$ to `pos_sum`.
    - If $\beta_v(\lambda) \le 0$: connect $v \to t$ with capacity $-\beta_v(\lambda) \ge 0$.
    - For each link $e = (u, v) \in E$, connect $u \leftrightarrow v$ with undirected capacity $w_e$.
  - Then $2 f(\lambda) = \text{pos\_sum} - \text{MinCut}(G_\lambda)$, using **only $N + 2 = 5002$ vertices** instead of $N + M + 2 = 55,002$ vertices!
- **Step 4: Complete Solution & Complexity**:
  Wrap the $5002$-vertex Goldberg oracle inside **Dinkelbach's secant iteration**: start with $\lambda_0 = \frac{W(E(V)) + P(V)}{C(V)}$, extract the $s$-reachable set $S_{k+1}$ Whenever $\text{pos\_sum} - \text{MinCut}(G_{\lambda_k}) > \epsilon$, and update $\lambda_{k+1} = \frac{W(E(S_{k+1})) + P(S_{k+1})}{C(S_{k+1})}$. Terminates in $6\text{--}10$ Dinic calls!

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 9
- **Hint 1 (Diagnostic)**: Standard `[NOI2006] 最大获利` builds $N + M + 2$ vertices. In a fractional programming loop that runs Dinic 10–40 times, can you eliminate the $M = 50,000$ link vertices?
- **Hint 2 (Compilation)**: Use Goldberg's identity $2 w_e x_u x_v = w_e(x_u + x_j) - w_e(x_u(1-x_v) + x_v(1-x_u))$.
- **Hint 3 (Optimization)**: Combine Dynamic Sign Splitting ($\beta_v(\lambda) = \deg_w(v) + 2p_v - 2\lambda c_v \gtrless 0$) with Dinkelbach's secant update to cut the number of Dinic calls from 50 to $\le 10$!
:::

---

#### Problem 10: `Dynamic Tree Max-Flow` (`树上动态最大流` / Luogu P4719 DDP Variant / CF 1783 F Style)
- **Judge URL**: [Luogu P4719 (Dynamic DP Framework)](https://www.luogu.com.cn/problem/P4719) / Tree Max-Flow Benchmark (`[ZH]` / `[EN]`)
- **Archetype**: Solving Dynamic Tree Max-Flow via Min-Cut Tree DP + Heavy-Light Decomposition $(\min, +)$ Matrices (Iteration 24)
- **Problem Statement & Constraints**:
  Given a rooted tree $T$ of $N \le 10^5$ vertices where each tree edge $(u, v)$ has capacity $c_{uv} \ge 0$, each vertex $u$ has a supply $p_u \ge 0$ (capacity from source $s \to u$) and a demand $s_u \ge 0$ (capacity to sink $u \to t$). Process $Q \le 10^5$ updates; each update modifies $p_u$ or $s_u$ of a vertex $u$, and asks for the new Maximum $s$-$t$ Flow in the network.
- **Step 1: Non-Graph Diagnostic Signal**:
  Running Max-Flow per query on $N = 10^5$ is hopeless. Because the internal network is a **tree**, we convert **Tree Max-Flow $\to$ Tree Min-Cut DP**, and maintain the DP dynamically via **Heavy-Light Decomposition (Dynamic DP)**.
- **Step 2 & 3: Algebraic-to-Matrix Compilation Scratchpad**:
  - Let $dp[u][0]$ ($u \in T$) and $dp[u][1]$ ($u \in S$) be the minimum cut in the subtree of $u$.
  - Let $h_u$ be the heavy child of $u$, and define the **light-children aggregated costs**:
    $$\begin{aligned}
    g[u][0] &:= p_u + \sum_{v \in \text{light}(u)} \min\big(dp[v][0], \; dp[v][1] + c(v \to u)\big), \\
    g[u][1] &:= s_u + \sum_{v \in \text{light}(u)} \min\big(dp[v][1], \; dp[v][0] + c(u \to v)\big).
    \end{aligned}$$
  - Then the transition from the heavy child $h_u$ to $u$ is a $2 \times 2$ tropical $(\min, +)$ matrix multiplication $(A \otimes B)_{ik} = \min_j (A_{ij} + B_{jk})$:
    $$\begin{bmatrix} dp[u][0] \\ dp[u][1] \end{bmatrix} = \begin{bmatrix} g[u][0] & g[u][0] + c(h_u \to u) \\ g[u][1] + c(u \to h_u) & g[u][1] \end{bmatrix} \otimes \begin{bmatrix} dp[h_u][0] \\ dp[h_u][1] \end{bmatrix}.$$
- **Step 4: Complete Solution & Complexity**:
  Maintain the $(\min, +)$ matrix product on each heavy chain using a Segment Tree. Each update to $p_u$ or $s_u$ climbs $O(\log N)$ heavy chains, updating $g[\text{top}(u)][0/1]$ at each chain head in $O(\log^2 N)$ time per query!

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 10
- **Hint 1 (Diagnostic)**: Convert Max-Flow on the tree into Min-Cut Tree DP with two states per vertex: $u \in S$ ($x_u = 1$) and $u \in T$ ($x_u = 0$).
- **Hint 2 (Compilation)**: Separate the contribution of the heavy child $h_u$ from the light children of $u$ so that moving up a heavy chain is a $2 \times 2$ $(\min, +)$ matrix product.
- **Hint 3 (Complexity)**: Maintain the heavy chain matrix products in a segment tree for $O(\log^2 N)$ per query (or $O(\log N)$ on a Link-Cut Tree / Global Biased Binary Tree).
:::

---

#### Problem 11: `POJ 2914 — Minimum Cut` (Global Minimum Cut via Stoer–Wagner)
- **Judge URL**: [POJ 2914](http://poj.org/problem?id=2914) (`[EN]`)
- **Archetype**: Global Undirected Minimum Cut via Stoer–Wagner Maximum Adjacency Search (Iteration 25)
- **Problem Statement & Constraints**:
  Given an undirected multigraph $G = (V, E)$ with $N \le 500$ vertices and $M$ weighted edges, find the minimum total weight of edges whose removal disconnects $G$ into at least two connected components.
- **Step 1: Non-Graph Diagnostic Signal**:
  Global Minimum Cut without a fixed source $s$ or sink $t$ on a dense undirected graph ($N \le 500$).
- **Step 2 & 3: Algebraic-to-Algorithmic Compilation Scratchpad**:
  - Accumulate parallel edges into an $N \times N$ symmetric adjacency matrix $W[u][v]$.
  - Run $N - 1$ phases of **Maximum Adjacency Search (MAS)**:
    - In each phase on the remaining $k$ uncontracted vertices, greedily pick the vertex $v$ with largest $w(A, v)$ in $O(k)$ time and update $w(A, u) \gets w(A, u) + W[v][u]$ for all unvisited $u$.
    - By Theorem 25.2, the last two vertices $s = v_{k-1}$ and $t = v_k$ satisfy $\lambda(s, t) = w(A_{k-1}, t)$. Update the global minimum `ans = min(ans, w(A_{k-1}, t))`.
    - Contract $t$ into $s$: for all remaining $u$, set $W[s][u] \gets W[s][u] + W[t][u]$ and $W[u][s] \gets W[s][u]$, and mark $t$ as deleted.
- **Step 4: Complete Solution & Complexity**:
  Each of the $N - 1$ MAS phases takes $O(N^2)$ with simple arrays (faster than a heap when the contracted graph becomes dense!), yielding $O(N^3)$ total time with a tiny constant factor ($\approx \frac{1}{6} N^3$ operations $\approx 2 \times 10^7$ ops for $N = 500$).

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 11
- **Hint 1 (Diagnostic)**: There is no fixed $(s, t)$. Running $N - 1$ Dinic calls on a dense graph takes $O(N^4)$ worst-case. Use Stoer–Wagner!
- **Hint 2 (Compilation)**: Since contracting supernodes makes the graph dense anyway, use an $N \times N$ adjacency matrix $W[u][v]$ and an $O(N^2)$ array scan per MAS phase instead of a priority queue.
- **Hint 3 (Edge Case)**: Sum parallel edges (`W[u][v] += c`) when reading input, and stop early if `ans == 0` (graph is already disconnected).
:::

---

## 4-Tier Curated Problem Bank (Part 2: Advanced & Mastery — Problems 12–22, Quarantined Templates & Bibliography)

---

### Tier 3: Advanced Problems (Problems 12–17)

#### Problem 12: `[NOI2010] 海拔` (Altitude)
- **Judge URL**: [Luogu P2046](https://www.luogu.com.cn/problem/P2046) / [BZOJ 2007](https://darkbzoj.cc/problem/2007) / [LOJ 2321](https://loj.ac/p/2321) (`[ZH]`)
- **Archetype**: Continuous-to-Binary Coarea Reduction + Directed $s$-$t$ Planar Dual Dijkstra (Iteration 23)
- **Problem Statement & Constraints**:
  An $(N+1) \times (N+1)$ grid of intersections ($1 \le N \le 500$) has top-left intersection $(0, 0)$ at altitude $h_{0,0} = 0$ and bottom-right intersection $(N, N)$ at altitude $h_{N,N} = 1$. For every pair of adjacent intersections $(u, v)$, you are given the directed pedestrian traffic $w(u \to v) \ge 0$ and $w(v \to u) \ge 0$. Moving along $u \to v$ consumes energy $w(u \to v) \cdot \max(0, h_v - h_u)$. Assign real altitudes $h_{i,j} \in \mathbb{R}$ to all intersections to minimize total energy consumption.
- **Step 1: Non-Graph / Continuous Diagnostic Signal**:
  First, recognize that $\max(0, h_v - h_u)$ is homogeneous of degree $1$ and convex. Second, $N = 500$ means $V = (N+1)^2 \approx 2.5 \times 10^5$ and $E \approx 10^6$, so even after reducing to Min-Cut, Dinic is too slow—we must use **Planar Dual Dijkstra**!
- **Step 2 & 3: Two-Stage Compilation Scratchpad**:
  - **Stage 1 (Continuous $h \in \mathbb{R} \to$ Binary $h \in \{0, 1\}$)**: By Theorem 23.3 (Coarea level-set integral $\max(0, h_v - h_u) = \int_0^1 [h_u \le \lambda < h_v] d\lambda$), the minimum over $h_{i,j} \in \mathbb{R}$ equals the minimum over binary assignments $h_{i,j} \in \{0, 1\}$, which is the Minimum Directed $s$-$t$ Cut where $s = (0,0)$ ($h_s = 0$), $t = (N,N)$ ($h_t = 1$), and $c(u \to v) = w(u \to v)$.
  - **Stage 2 (Directed Primal Grid $\to$ Directed Dual Graph $G^*$)**:
    - Define $N^2$ interior square faces $\text{Face}(i, j)$ ($0 \le i, j < N$), Dual Source $S^*$ (Left border $j = -1$ and Bottom border $i = N$), and Dual Sink $T^*$ (Top border $i = -1$ and Right border $j = N$).
    - Apply the $90^\circ$ CCW rotation table from Iteration 23:
      - East $(i, j) \to (i, j+1)$ $\implies$ North $\text{Face}(i, j) \to \text{Face}(i-1, j)$ with weight $w_{\text{East}}(i, j)$.
      - West $(i, j+1) \to (i, j)$ $\implies$ South $\text{Face}(i-1, j) \to \text{Face}(i, j)$ with weight $w_{\text{West}}(i, j)$.
      - South $(i, j) \to (i+1, j)$ $\implies$ East $\text{Face}(i, j-1) \to \text{Face}(i, j)$ with weight $w_{\text{South}}(i, j)$.
      - North $(i+1, j) \to (i, j)$ $\implies$ West $\text{Face}(i, j) \to \text{Face}(i, j-1)$ with weight $w_{\text{North}}(i, j)$.
- **Step 4: Complete Solution & Complexity**:
  Run a single Dijkstra from $S^*$ to $T^*$ on the $N^2 + 2$ dual vertices and $4N(N+1)$ directed dual edges. Time complexity: $O(N^2 \log N) \approx 4 \times 10^6$ operations, running in $< 0.15$s.

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 12
- **Hint 1 (Diagnostic)**: Prove that fractional altitudes $0 < h_v < 1$ are never needed: write $\max(0, h_v - h_u) = \int_0^1 [h_u \le \lambda < h_v] d\lambda$.
- **Hint 2 (Compilation)**: Once $h_v \in \{0, 1\}$, an edge $u \to v$ pays $w(u \to v)$ iff $h_u = 0$ ($s$-side) and $h_v = 1$ ($t$-side). That is a directed $s$-$t$ Min-Cut on a planar grid!
- **Hint 3 (Dual Orientation)**: Put $S^*$ on the lower-left perimeter and $T^*$ on the upper-right perimeter, and rotate every primal arrow $90^\circ$ counter-clockwise to orient the dual edge.
:::

---

#### Problem 13: `CF 343 E — Pumping Stations`
- **Judge URL**: [Codeforces 343E](https://codeforces.com/problemset/problem/343/E) (`[EN]`)
- **Archetype**: Gomory–Hu Cut Tree + Minimum-Edge Divide-and-Conquer Permutation (Iteration 25)
- **Problem Statement & Constraints**:
  Given an undirected weighted graph $G = (V, E)$ with $N \le 200$ vertices and $M \le 1000$ edges, find both the maximum possible value of $\sum_{i=1}^{N-1} \text{MaxFlow}_G(p_i, p_{i+1})$ over all permutations $p$ of $\{1, \dots, N\}$ and an explicit permutation $p_1, \dots, p_N$ achieving this maximum.
- **Step 1: Non-Graph Diagnostic Signal**:
  Optimizing a Hamiltonian path objective where edge weights are pairwise $\text{MaxFlow}_G(u, v) = \text{MinCut}_G(u, v)$ values.
- **Step 2 & 3: Algebraic-to-Tree Compilation Scratchpad**:
  - Build the Gomory–Hu tree $T_{\text{GH}}$ in $N - 1$ calls to Dinic on $G$.
  - By Compilation 25B, no permutation can exceed $\sum_{e \in E(T_{\text{GH}})} w_T(e)$, and we can achieve this upper bound with equality by recursively splitting $T_{\text{GH}}$ at its **minimum-weight edge** $e_{\min} = (u, v)$ and concatenating the permutations of the two resulting subtrees!
- **Step 4: Complete Solution & Bottom-Up DSU Shortcut**:
  - **Bottom-Up DSU Implementation (Even Simpler than Recursion!)**:
    Sort the $N - 1$ edges of $T_{\text{GH}}$ in **descending** order of weight $w_T(e_1) \ge w_T(e_2) \ge \dots \ge w_T(e_{N-1})$. Maintain for each DSU component an ordered list of vertices (initially `[v]` for each $v \in V$). When processing edge $(u, v)$, simply append `list[find(v)]` to the end of `list[find(u)]`! Because all previously merged edges inside both components have weight $\ge w_T(u, v)$, the junction between the last vertex of `find(u)` and the first vertex of `find(v)` has path-minimum equal to $w_T(u, v)$!
  - Complexity: $(N - 1) \cdot T_{\text{Dinic}}(N, M) + O(N \log N)$.

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 13
- **Hint 1 (Diagnostic)**: Build the Gomory–Hu tree $T_{\text{GH}}$ first. Why is the answer at most the sum of all $N - 1$ edge weights of $T_{\text{GH}}$?
- **Hint 2 (Compilation)**: Consider the minimum-weight edge $e_{\min}$ of $T_{\text{GH}}$. Any tour must cross $e_{\min}$ at least once. What if we visit all vertices on one side of $e_{\min}$ before crossing $e_{\min}$ to the other side?
- **Hint 3 (DSU Trick)**: Sort the edges of $T_{\text{GH}}$ in descending order of weight and concatenate the vertex lists of the two components as you union them!
:::

---

#### Problem 14: `CF 1919 F2 — Wine Factory (Hard Version)`
- **Judge URL**: [Codeforces 1919F2](https://codeforces.com/problemset/problem/1919/F2) (`[EN]`)
- **Archetype**: Dynamic Pipeline Max-Flow via Min-Cut DP + Segment Tree $(\min, +)$ Matrices (Iteration 24)
- **Problem Statement & Constraints**:
  There are $N \le 5 \times 10^5$ water towers in a line. Tower $i$ receives $a_i$ liters of water, has a wizard who can turn at most $b_i$ liters of water into wine, and has a pipe of capacity $c_i$ from tower $i$ to tower $i + 1$ ($c_N = 0$). Process $Q \le 5 \times 10^5$ point updates to $(a_i, b_i, c_i)$, outputting the total wine produced after each update.
- **Step 1: Non-Graph Diagnostic Signal**:
  Although phrased as a greedy simulation of water flowing rightwards, this is literally an $s$-$t$ Maximum Flow problem on a path: $s \to i$ has capacity $a_i$, $i \to t$ has capacity $b_i$, and $i \to i+1$ has capacity $c_i$. With $N, Q = 5 \times 10^5$, we convert **Max-Flow $\to$ Min-Cut DP** and maintain the DP in a **Segment Tree**!
- **Step 2 & 3: Algebraic-to-Matrix Compilation Scratchpad**:
  - In an $s$-$t$ cut $x \in \{0, 1\}^N$ ($x_i = 0 \iff i \in T$, $x_i = 1 \iff i \in S$):
    - Placing $i \in T$ ($x_i = 0$) severs $s \to i$, costing $a_i$.
    - Placing $i \in S$ ($x_i = 1$) severs $i \to t$, costing $b_i$.
    - Transitioning from $x_i = 1$ ($i \in S$) to $x_{i+1} = 0$ ($i+1 \in T$) severs the pipe $i \to i+1$, costing $c_i$! (Note: $x_i = 0, x_{i+1} = 1$ costs $0$ because the pipe is directed $i \to i+1$!)
  - Therefore, each tower $i$ is represented by the $2 \times 2$ $(\min, +)$ transition matrix $M_i$ where row $u = x_i \in \{0, 1\}$ and column $v = x_{i+1} \in \{0, 1\}$ charge the cut cost of vertex $i$ plus the outgoing pipe $i \to i+1$:
    $$M_i = \begin{bmatrix} a_i & a_i \\ b_i + c_i & b_i \end{bmatrix}.$$
    Specifically: if $x_i = 0$ ($i \in T$), we pay $a_i$ regardless of $x_{i+1}$; if $x_i = 1$ ($i \in S$) and $x_{i+1} = 0$ ($i+1 \in T$), we pay $b_i + c_i$; if $x_i = 1$ and $x_{i+1} = 1$, we pay $b_i$.
- **Step 4: Complete Solution & Complexity**:
  Build a Segment Tree over $M_1, M_2, \dots, M_N$ with $(\min, +)$ matrix multiplication. Since $c_N = 0$, the global Min-Cut (= Max-Flow) is simply $\min_{u, v \in \{0,1\}} (M_1 \otimes \dots \otimes M_N)[u][v]$! Each update modifies a single matrix $M_i$ in $O(\log N)$ time. Total time: $O((N + Q) \log N)$.

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 14
- **Hint 1 (Diagnostic)**: Model the water towers as an $s$-$t$ flow network: $s \to i$ (cap $a_i$), $i \to t$ (cap $b_i$), $i \to i+1$ (cap $c_i$). Now apply Max-Flow = Min-Cut!
- **Hint 2 (Compilation)**: In the Min-Cut, each vertex $i$ has state $x_i \in \{0, 1\}$. When is the directed pipe $i \to i+1$ cut? Only when $x_i = 1$ and $x_{i+1} = 0$!
- **Hint 3 (Matrix Form)**: Encode each index $i$ as the $2 \times 2$ $(\min, +)$ matrix $\begin{bmatrix} a_i & a_i \\ b_i + c_i & b_i \end{bmatrix}$ and maintain the product in a Segment Tree!
:::

---

#### Problem 15: `AtCoder ARC 125 E — Snack`
- **Judge URL**: [AtCoder arc125_e](https://atcoder.jp/contests/arc125/tasks/arc125_e) (`[JA]` / `[EN]`)
- **Archetype**: Complete Bipartite Max-Flow $K_{N, M}$ Solved in $O((N + M) \log(N + M))$ via Min-Cut Sorting (Iteration 24)
- **Problem Statement & Constraints**:
  There are $N \le 2 \times 10^5$ types of snacks (snack $i$ has $A_i \le 10^{12}$ pieces) and $M \le 2 \times 10^5$ children. Child $j$ can receive at most $C_j \le 10^{12}$ snacks in total, and at most $B_j \le 10^{12}$ snacks of each individual type $i$. Find the maximum total number of snacks that can be distributed.
- **Step 1: Non-Graph Diagnostic Signal**:
  This is a Maximum Flow problem on a complete bipartite graph $K_{N, M}$:
  - $s \to \text{Snack } i$ has capacity $A_i$.
  - $\text{Snack } i \to \text{Child } j$ has capacity $B_j$ (for all $1 \le i \le N, 1 \le j \le M$).
  - $\text{Child } j \to t$ has capacity $C_j$.
  Since $N, M = 2 \times 10^5$, we invoke **Max-Flow = Min-Cut** and eliminate the graph!
- **Step 2 & 3: Algebraic-to-Greedy Compilation Scratchpad**:
  - Suppose in our $s$-$t$ cut we place exactly $k \in \{0, 1, \dots, N\}$ snacks on the source side $S$ (so $N - k$ snacks are placed in $T$, severing their $s \to i$ edges of capacity $A_i$).
  - **Observation 1 (Which $k$ snacks go into $S$?)**: Because the cross-edge capacity $c(i \to j) = B_j$ depends **only on $j$, not on $i$**, every snack in $S$ has the exact same impact on the children! Therefore, to minimize the severed $A_i$ capacities of the $N - k$ snacks in $T$, we should greedily place the $k$ snacks with the **largest** $A_i$ into $S$ (cutting the $N - k$ smallest $A_i$)!
  - **Observation 2 (How should each child $j$ be placed once $k$ is fixed?)**:
    For each child $j \in \{1, \dots, M\}$:
    - If we place child $j \in S$, we sever $j \to t$, paying $C_j$ (and $0$ cross-edges).
    - If we place child $j \in T$, we do not sever $j \to t$, but we sever all $k$ cross-edges from the $k$ snacks in $S$ to child $j$, paying $k \cdot B_j$!
    - Thus, for fixed $k$, child $j$ independently contributes $\min(C_j, k \cdot B_j)$!
  - **Master Formula**:
    $$\text{MaxFlow} = \min_{0 \le k \le N} \left( \sum_{r=1}^{N-k} A_{(r)} + \sum_{j=1}^M \min(C_j, \; k \cdot B_j) \right).$$
- **Step 4: Complete Solution & Complexity**:
  - Sort $A_1 \le A_2 \le \dots \le A_N$.
  - Notice that $k \cdot B_j \le C_j \iff k \le \lfloor C_j / B_j \rfloor$. Sort the children by threshold $\lfloor C_j / B_j \rfloor$ (or bucket them into $k \in \{0, \dots, N\}$) and maintain prefix sums of $B_j$ and suffix sums of $C_j$.
  - Sweep $k = 0, 1, \dots, N$ in $O(1)$ per step after sorting! Total complexity: $O((N + M) \log(N + M))$.

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 15
- **Hint 1 (Diagnostic)**: Formulate as Max-Flow on $K_{N, M}$: $s \to i$ (cap $A_i$), $i \to j$ (cap $B_j$), $j \to t$ (cap $C_j$). Now switch to Min-Cut!
- **Hint 2 (Compilation)**: Fix the number of snacks $k = |S \cap L|$ placed on the $s$-side of the cut. Since $c(i \to j) = B_j$ is independent of $i$, which $N - k$ snacks should be placed in $T$?
- **Hint 3 (Two-Pointer Sweep)**: Once $k$ snacks are in $S$, each child $j$ independently pays $\min(C_j, k \cdot B_j)$. Sort children by $C_j / B_j$ to evaluate $\sum_j \min(C_j, k \cdot B_j)$ for all $k = 0 \dots N$ in linear time!
:::

---

#### Problem 16: `Inverse Gomory–Hu Tree / Realizable All-Pairs Min-Cut Matrix` (`CF 1053 E / GYM 102900 / Ultrametric Network Synthesis`)
- **Judge URL**: [Codeforces / ICPC Regional Ultrametric Cut Synthesis](https://codeforces.com/problemset/problem/472/D) (`[EN]` Gomory & Hu 1961 Section 4)
- **Archetype**: Necessary & Sufficient Ultrametric Conditions for an All-Pairs Min-Cut Matrix via Maximum Spanning Tree (Iteration 25)
- **Problem Statement & Constraints**:
  You are given an $N \times N$ symmetric matrix $A$ ($N \le 2000$) of non-negative integers. Determine whether there exists an undirected weighted graph $G = (V, E)$ on $N$ vertices such that $\text{MinCut}_G(u, v) = A_{u,v}$ for all $1 \le u < v \le N$, and if so, output such a graph $G$ with the minimum possible total edge weight $\sum_{e \in E} w_e$.
- **Step 1: Non-Graph Diagnostic Signal**:
  Instead of computing cuts from a graph, we are asked to **invert** the Gomory–Hu map: given all $\binom{N}{2}$ pairwise minimum cuts, reconstruct $G$.
- **Step 2 & 3: Algebraic-to-Tree Compilation Scratchpad**:
  - **Theorem (Gomory & Hu 1961 — Synthesis of Multi-Terminal Networks)**:
    1. A symmetric matrix $A$ is the all-pairs min-cut matrix of some undirected graph $G$ **if and only if** $A$ satisfies the ultrametric inequality $A_{u,w} \ge \min(A_{u,v}, A_{v,w})$ for all $u, v, w$.
    2. Even better: if $A$ is realizable by *any* graph $G$, it is realizable by a **tree** $T$, and that tree $T$ is necessarily a **Maximum Spanning Tree (MaxST)** of the complete graph with edge weights $A_{u,v}$!
    3. Moreover, if we want the **minimum total edge weight** $\sum_{e \in E(G)} w(e)$ among all graphs (not just trees!) realizing $A$, Gomory & Hu proved that decomposing each uniform component of $T$ into a **single cycle** of weight $\frac{1}{2} w_T(e)$ achieves half the weight of the tree (and if restricted to a tree, $T$ itself is optimal).
- **Step 4: Complete Solution & Complexity**:
  1. Run Prim's or Kruskal's algorithm in $O(N^2)$ time to find a **Maximum Spanning Tree** $T$ of the matrix $A$.
  2. Run a simple $O(N)$ DFS from each vertex $u \in \{1, \dots, N\}$ on $T$ to compute the path-bottleneck matrix $B_{u,v} = \min_{e \in \text{Path}_T(u, v)} w_T(e)$.
  3. Check if $B_{u,v} == A_{u,v}$ for all $1 \le u < v \le N$. If yes, $T$ is the exact Gomory–Hu tree realizing $A$; if no, no undirected graph exists! Total complexity: $O(N^2)$.

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 16
- **Hint 1 (Diagnostic)**: By Theorem 25.3, every undirected graph has a Gomory–Hu tree $T_{\text{GH}}$ with the exact same pairwise min-cuts! So if any graph $G$ realizes $A$, a **tree** $T$ also realizes $A$.
- **Hint 2 (Compilation)**: Since $A_{u,v} = \min_{e \in \text{Path}_T(u, v)} w_T(e) \le w_T(u, v)$ for every tree edge, $T$ must be a **Maximum Spanning Tree** of the complete graph with weights $A_{u,v}$!
- **Hint 3 (Verification)**: Build the Maximum Spanning Tree $T$ using Prim's $O(N^2)$ algorithm, and verify in $O(N^2)$ via $N$ DFS runs whether $\min_{e \in \text{Path}_T(u,v)} w_T(e) == A_{u,v}$ for all pairs.
:::

---

#### Problem 17: `Nash-Williams Arboricity & Forest Decomposition via Rooted Goldberg Density` (`[WC/CTS] / Matroid-Flow Synthesis`)
- **Judge URL**: [Luogu P5155 / Arboricity & Dense Subgraph Series](https://www.luogu.com.cn/problem/P4174) / Nash-Williams Exact Arboricity Test (`[EN]` / `[ZH]`)
- **Archetype**: Testing $k$-Forest Decomposability $\max_{|S| \ge 2} \frac{|E(S)|}{|S| - 1} \le k$ via Rooted Goldberg Min-Cut (Iteration 22)
- **Problem Statement & Constraints**:
  Given an undirected graph $G = (V, E)$ with $N \le 300$ vertices and $M \le 2000$ edges, find the **arboricity** of $G$—the minimum number of edge-disjoint forests needed to cover all edges of $G$.
- **Step 1: Non-Graph Diagnostic Signal**:
  By **Nash-Williams' Forest Decomposition Theorem (1964)**, $E(G)$ can be partitioned into $k$ forests if and only if no induced subgraph $S \subseteq V$ of size $|S| \ge 2$ has more edges than $k$ spanning trees can hold:
  $$|E(S)| \le k(|S| - 1) \quad \forall S \subseteq V \text{ with } |S| \ge 2 \quad \Longleftrightarrow \quad k \ge \max_{|S| \ge 2} \left\lceil \frac{|E(S)|}{|S| - 1} \right\rceil.$$
- **Step 2 & 3: Algebraic-to-Graph Compilation Scratchpad (Defeating the $|S| = 0$ and $|S| = 1$ Traps!)**:
  - For a fixed integer $k \ge 1$, we want to check whether $\max_{|S| \ge 2} \big(|E(S)| - k|S| + k\big) \le 0$, or equivalently whether:
    $$\max_{\emptyset \neq S \subseteq V} \big(|E(S)| - k|S|\big) \le -k!$$
  - **Wait!** Look at what happens in standard Goldberg MDS if we evaluate $|E(S)| - k|S|$ for $S = \emptyset$ and for a singleton $S = \{v\}$:
    - For $S = \emptyset$: $|E(\emptyset)| - k|\emptyset| = 0 - 0 = 0 > -k$!
    - For $S = \{v\}$: $|E(\{v\})| - k|\{v\}| = 0 - k = -k$, which ties the threshold $-k$!
    So if we run unrooted Goldberg Min-Cut, the empty set $S = \emptyset$ will **always** give objective $0 > -k$, masking whether any set with $|S| \ge 2$ violates $|E(S)| - k|S| > -k$!
  - **How to Force $S \neq \emptyset$**:
    Every non-empty set $S \neq \emptyset$ contains at least one vertex $r \in V$. Or even faster: instead of running $N$ separate flows forcing each $r \in S$ ($c(s \to r) = \infty$), notice that for any non-empty $S \neq \emptyset$, if we pick a root $r \in S$, the remaining vertices $S \setminus \{r\}$ pay $k(|S| - 1)$ while $r$ itself pays $0$!
    Specifically, in Goldberg's network $G_k$:
    - Set $c(s \to v) = U = M$, $c(v \to t) = U + 2k - \deg(v)$ for all $v \in V$, and $c(u \leftrightarrow v) = 1$.
    - To force $r \in S$ (and waive $r$'s $-k$ vertex cost so $S$ only pays $k(|S|-1)$!), simply change $r$'s edges so $c(s \to r) = \infty$ and $c(r \to t) = U - \deg(r)$!
    - Then for any $S \ni r$, $\text{Cap}(S) = UN - 2\big(|E(S)| - k(|S| - 1)\big)$!
- **Step 4: Complete Solution & Incremental Root Trick**:
  For a fixed $k$, we test $r = 1, 2, \dots, N$ sequentially: after testing $r$ (which checks all $S \ni r$), if no violating $S \ni r$ exists, we can permanently force $r \in \bar{S}$ ($r \to t$ capacity $\infty$) and **reuse the residual graph** via rollback/incremental flow, checking all $N$ roots in time proportional to $O(1\text{--}\log N)$ max-flows!

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 17
- **Hint 1 (Diagnostic)**: By Nash-Williams' Theorem, $G$ decomposes into $k$ forests iff $|E(S)| - k(|S| - 1) \le 0$ for all $S \neq \emptyset$.
- **Hint 2 (The $S = \emptyset$ Trap)**: Why does standard Goldberg fail on $|E(S)| - k(|S|-1)$? Because $S = \emptyset$ gives $0 - k(0 - 1) = +k > 0$!
- **Hint 3 (Rooted Fix)**: Force a root vertex $r \in S$ ($c(s \to r) = \infty$) and set $c(r \to t) = U - \deg(r)$ (without the $+2k$ term!). Then for every $S \ni r$, the cut capacity is exactly $UN - 2(|E(S)| - k(|S|-1))$.
:::

---

### Tier 4: Mastery & Grandmaster Synthesis Problems (Problems 18–22)

#### Problem 18: `[CSP-S 2021] 交通规划` (Traffic Planning — Multi-Terminal Outerplanar Min-Cut)
- **Judge URL**: [Luogu P7916](https://www.luogu.com.cn/problem/P7916) / [LOJ 3544](https://loj.ac/p/3544) (`[ZH]`)
- **Archetype**: Multi-Terminal Outerplanar Min-Cut $\leftrightarrow$ Dual Boundary Color-Transition Splitting + Multiple Dual Dijkstras + Circular Interval DP (Iteration 23)
- **Problem Statement & Constraints**:
  Given an $N \times M$ undirected weighted grid ($2 \le N, M \le 500$), answer $T \le 50$ independent queries. In each query, $k \le 50$ additional boundary terminals are attached to specific perimeter nodes around the outside of the grid, each with a connecting edge weight and a color $col_i \in \{0, 1\}$. You may color each of the $NM$ interior grid vertices $0$ or $1$; an edge $(u, v)$ pays its weight if $col_u \neq col_v$. Find the minimum total cost for each query.
- **Step 1: Non-Graph Diagnostic Signal**:
  For each query, we want a multi-terminal minimum cut separating all $0$-colored boundary terminals from all $1$-colored boundary terminals on a planar grid of size $V = 2.5 \times 10^5$. Running Dinic $T = 50$ times on $2.5 \times 10^5$ vertices is $50\times$ TLE. We must generalize **Planar Dual Dijkstra** from $2$ terminals ($s, t$) to $k \le 50$ boundary terminals!
- **Step 2 & 3: Algebraic-to-Dual & Interval DP Compilation Scratchpad**:
  - **Step 2A (Outer Face Perimeter Splitting)**:
    Walk clockwise around the perimeter of the grid, listing the $k$ terminals $p_1, p_2, \dots, p_k$ in clockwise cyclic order. These $k$ terminals divide the unbounded outer face $f_\infty$ into $k$ boundary segments $B_1, B_2, \dots, B_k$ (where $B_r$ lies between $p_r$ and $p_{r+1}$).
  - **Step 2B (Coalescing Same-Color Intervals)**:
    Suppose $p_r$ and $p_{r+1}$ have the **same color** ($col(p_r) = col(p_{r+1})$). Does an optimal cut curve ever need to enter or exit the boundary segment $B_r$? No! Only the boundary segments $B_r$ where $col(p_r) \neq col(p_{r+1})$ must have an odd number (hence exactly $1$) of cut curves terminating in them!
    Because the colors alternate $0 \to 1$ and $1 \to 0$ around a closed circle, the number of active boundary transitions $2m \le k$ is **always even**!
  - **Step 2C (Pairwise Dual Dijkstra)**:
    Label the $2m$ active dual boundary nodes $D_1, D_2, \dots, D_{2m}$ in clockwise order. Run Dijkstra $2m$ times on the dual graph $G^*$ (of size $(N-1)(M-1) + k$) to compute the all-pairs shortest path distances $\text{dist}(D_a, D_b)$ between the $2m$ active boundary nodes.
  - **Step 2D (Non-Crossing Circular Matching via Interval DP)**:
    In a planar graph, minimal cut curves separating alternating $0/1$ boundary intervals never cross one another—they form a **non-crossing perfect matching** of $D_1, \dots, D_{2m}$ on the circle (where each $0 \to 1$ transition matches to a $1 \to 0$ transition)!
    Duplicate the cyclic sequence to length $4m$ and solve via standard **Interval DP** over even-length intervals $[l, r]$:
    $$dp[l][r] = \min \left( dp[l+1][r-1] + \text{dist}(D_l, D_r), \quad \min_{p = l+1, l+3, \dots, r-2} \big( dp[l][p] + dp[p+1][r] \big) \right).$$
- **Step 4: Complete Solution & Complexity**:
  - Pre-build the $(N-1)(M-1)$ interior dual grid once.
  - For each query, temporarily attach the $k$ perimeter edges and $2m \le k$ active outer dual nodes, run $2m$ Dijkstras in $O(k NM \log(NM))$, and run the $O(k^3)$ Interval DP.
  - Total complexity across $T$ queries: $O(\sum k \cdot NM \log(NM) + \sum k^3)$, comfortably passing within 3 seconds!

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 18
- **Hint 1 (Diagnostic)**: When $k = 2$ (one `0` terminal and one `1` terminal), this is just `狼抓兔子` ($S^* \to T^*$ Dual Dijkstra). What happens to the outer face when there are $k \le 50$ terminals around the perimeter?
- **Hint 2 (Compilation)**: The $k$ perimeter terminals split the outer face into $k$ boundary segments. Notice that a cut curve only needs to touch a boundary segment if the two adjacent terminals have **different** colors ($0 \to 1$ or $1 \to 0$)!
- **Hint 3 (Interval DP)**: There are an even number $2m \le k$ of active boundary segments, and optimal dual cut paths cannot cross! Run $2m$ Dijkstras on the dual graph and use $O(m^3)$ Circular Interval DP to find the minimum-weight non-crossing matching!
:::

---

#### Problem 19: `CF 1383 F — Special Edges`
- **Judge URL**: [Codeforces 1383F](https://codeforces.com/problemset/problem/1383/F) (`[EN]`)
- **Archetype**: Multi-Query Parametric Max-Flow via $2^K$ Partial Min-Cut Precomputation (Iteration 24)
- **Problem Statement & Constraints**:
  You are given a directed graph $G = (V, E)$ with $N, M \le 10^4$, where edge capacities are small integers in $[0, 25]$. The first $K \le 10$ edges $e_1, \dots, e_K$ are **special**. You must answer $Q \le 2 \times 10^5$ queries; each query specifies $K$ new capacities $w_1, \dots, w_K \in [0, 25]$ for the $K$ special edges and asks for the Maximum Flow from $1$ to $N$.
- **Step 1: Non-Graph Diagnostic Signal**:
  With $Q = 2 \times 10^5$ queries, we cannot run flow per query. Because $K \le 10$ is tiny ($2^K = 1024$), we invoke **Max-Flow = Min-Cut** to decouple the $K$ special edges from the rest of the graph!
- **Step 2 & 3: Algebraic-to-Bitmask Cut Compilation Scratchpad**:
  - Any $1$-$N$ cut $(S, \bar{S})$ in $G$ is determined by which subset $mask \subseteq \{1, \dots, K\}$ of the $K$ special edges crosses from $S$ to $\bar{S}$!
  - Wait: do we need to enforce that special edges NOT in $mask$ do NOT cross from $S$ to $\bar{S}$?
    Yes! If we set the capacity of every special edge $i \in mask$ to $0$ (pretending it is already cut and paying $w_i$ separately) and set the capacity of every special edge $i \notin mask$ to $\infty$ (forbidding the cut from severing $e_i$), let `base_cut[mask]` be the resulting Minimum Cut of the network!
  - Then for **any** query capacities $(w_1, \dots, w_K)$:
    $$\text{MaxFlow}(w_1, \dots, w_K) = \min_{mask \in \{0, \dots, 2^K - 1\}} \left( \text{base\_cut}[mask] + \sum_{i \in mask} w_i \right)!$$
- **Step 4: Complete Solution & Incremental DFS Precomputation**:
  - How do we compute `base_cut[mask]` for all $2^K = 1024$ masks fast?
    Start at `mask = (1<<K) - 1` (all $K$ special edges have capacity $0$) and run Dinic once to get `base_cut[(1<<K)-1]`.
    Then traverse the $2^K$ masks in a recursion tree (changing one special edge $e_i$ from capacity $0$ to capacity $\infty$, which has effective max-flow increase at most $25$!): each step pushes at most $25$ units of augmenting paths using simple Ford–Fulkerson / BFS on the residual graph!
  - Precomputation takes $O(2^K \cdot 25 \cdot M)$ time, and each of the $Q = 2 \times 10^5$ queries takes $O(2^K)$ with fast subset-sum DP (`sum_w[mask] = sum_w[mask ^ lsb] + w[ctz(mask)]`).

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 19
- **Hint 1 (Diagnostic)**: You have $Q = 2 \times 10^5$ queries and only $K = 10$ changing edges. Switch from Max-Flow to Min-Cut!
- **Hint 2 (Compilation)**: An $s$-$t$ cut is a union of a subset $mask \subseteq \{1, \dots, K\}$ of special edges plus some normal edges. If you set $c(e_i) = 0$ for $i \in mask$ and $c(e_i) = \infty$ for $i \notin mask$, the min-cut `base_cut[mask]` is independent of the query weights $w_i$!
- **Hint 3 (Incremental Residual Tree)**: Don't run Dinic $2^{10} = 1024$ times from scratch! Start with all special edges at cap $0$, run Dinic once, and do a DFS over the $K$ bits, pushing at most $25$ units of flow when setting $c(e_i) = \infty$.
:::

---

#### Problem 20: `AtCoder AGC 031 E — Snuke the Phantom Thief` (1D/2D Coordinate Rank Prefix/Suffix Cut-Flow Duality)
- **Judge URL**: [AtCoder agc031_e](https://atcoder.jp/contests/agc031/tasks/agc031_e) (`[JA]` / `[EN]`)
- **Archetype**: Translating Coordinate Threshold Constraints ("At Most $b_i$ Points Have $x \le a_i$") into Sorted Index Slots + Min-Cut / MCMF Duality (Iteration 24 & Wave 4A Bridge)
- **Problem Statement & Constraints**:
  There are $N \le 80$ jewels at $(x_i, y_i)$ with values $v_i \le 10^{15}$. You are given $M \le 320$ constraints of four types:
  - `'L' a b`: at most $b$ stolen jewels have $x_i \le a$.
  - `'R' a b`: at most $b$ stolen jewels have $x_i \ge a$.
  - `'D' a b`: at most $b$ stolen jewels have $y_i \le a$.
  - `'U' a b`: at most $b$ stolen jewels have $y_i \ge a$.
  Find the maximum total value of stolen jewels.
- **Step 1: Non-Graph Diagnostic Signal**:
  First, examine the **1D Version** (where only `'L'` and `'R'` constraints exist, which can have $N \le 10^5$ in 1D variants): how do you encode *"at most $b$ chosen items have $x_i \le a$"*?
- **Step 2 & 3: Algebraic Compilation via Fixed Cardinality $k$ (The Rank-Slot Transformation)**:
  - Fix the **total number of stolen jewels** $k \in \{1, 2, \dots, N\}$, and sort the $k$ stolen jewels by their $x$-coordinates as $x_{(1)} \le x_{(2)} \le \dots \le x_{(k)}$.
  - Now translate the two cardinality constraints into **pointwise bounds on each rank slot $r \in \{1, \dots, k\}$**:
    1. *"At most $b$ stolen jewels have $x \le a$"* $\iff$ the $(b+1)$-th stolen jewel from the left MUST have $x_{(b+1)} > a$, i.e., for all $r \ge b + 1$, $x_{(r)} \ge a + 1$!
    2. *"At most $b$ stolen jewels have $x \ge a$"* $\iff$ the $(b+1)$-th stolen jewel from the right (which is rank $k - b$) MUST have $x_{(k-b)} < a$, i.e., for all $r \le k - b$, $x_{(r)} \le a - 1$!
  - Intersecting all constraints gives each rank slot $r \in \{1, \dots, k\}$ an exact allowed interval $x_{(r)} \in [L_r^x, R_r^x]$ (and similarly for $y$-ranks $c \in \{1, \dots, k\}$, $y_{(c)} \in [L_c^y, R_c^y]$)!
- **Step 4: Complete Solution & 1D vs. 2D Duality**:
  - **In 1D**: Since $[L_r^x, R_r^x]$ satisfies $L_1^x \le \dots \le L_k^x$ and $R_1^x \le \dots \le R_k^x$, any matching of $k$ jewels to the $k$ intervals can be uncrossed to be sorted, so it reduces to maximum weight interval matching (or Hall's Theorem / Min-Cut DP in $O(N \log N)$)!
  - **In 2D (`AGC 031 E`)**: Build a network for each $k = 1 \dots N$: $s \to x\text{-slot } r$ (cap $1$), $x\text{-slot } r \to \text{Jewel } i_{\text{in}}$ (if $x_i \in [L_r^x, R_r^x]$), $\text{Jewel } i_{\text{in}} \to i_{\text{out}}$ (cap $1$, cost $-v_i$), $i_{\text{out}} \to y\text{-slot } c$ (if $y_i \in [L_c^y, R_c^y]$), $y\text{-slot } c \to t$ (cap $1$), and run Min-Cost Flow of volume $k$.

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 20
- **Hint 1 (Diagnostic)**: A constraint "at most $b$ chosen points have $x \le a$" couples all points globally. What happens if you fix the **exact total number** $k$ of chosen points first?
- **Hint 2 (Compilation)**: Once $k$ is fixed and the $k$ chosen points are sorted as $x_{(1)} \le \dots \le x_{(k)}$, "at most $b$ points have $x \le a$" is equivalent to $x_{(b+1)} \ge a + 1$!
- **Hint 3 (Full Construction)**: Intersect all bounds to get allowed intervals $[L_r^x, R_r^x]$ for each $x$-rank $r \in \{1, \dots, k\}$ and $[L_c^y, R_c^y]$ for each $y$-rank $c \in \{1, \dots, k\}$, then match jewels to $(x\text{-rank}, y\text{-rank})$ pairs via flow!
:::

---

#### Problem 21: `Interior Planar $s$-$t$ Minimum Cut` (Hassin–Johnson / Reif Path-Slicing Algorithm — `CF 1765 I` / `[SDOI] Planar Cut`)
- **Judge URL**: [Codeforces / Planar Interior Min-Cut Series](https://codeforces.com/problemset/problem/1765/I) (`[EN]` Reif 1983; Hassin & Johnson 1985)
- **Archetype**: General Planar $s$-$t$ Min-Cut (when $s$ and $t$ Are NOT on the Same Face) via Primal Path Slicing + Divide-and-Conquer Dual Dijkstra (Iteration 23)
- **Problem Statement & Constraints**:
  Given an undirected weighted planar graph $G = (V, E)$ with $V, E \le 10^5$ embedded in the plane, and two arbitrary vertices $s, t \in V$ (which do NOT necessarily lie on the outer face), compute $\text{MinCut}_G(s, t)$ in $O(V \log^2 V)$ time without running Max-Flow.
- **Step 1: Non-Graph / Geometric Diagnostic Signal**:
  When $s$ and $t$ lie on different faces deep inside a planar graph, adding an edge $(s, t)$ crosses existing edges and destroys planarity! We must find the **minimum-weight dual cycle $C^*$ in $G^*$ that separates face/vertex $s$ from face/vertex $t$**.
- **Step 2 & 3: Algebraic-to-Topological Compilation Scratchpad (Reif's Path-Slicing Reduction)**:
  1. **Find a Shortest Primal $s$-$t$ Path $P$**: Run unweighted BFS in the primal graph $G$ to find a shortest path $P = (v_0 = s, v_1, \dots, v_k = t)$ of $k$ edges $e_1, \dots, e_k$.
  2. **Single-Crossing Property**: Because $P$ is a shortest (or simple) path between $s$ and $t$, any dual cycle $C^*$ separating $s$ and $t$ must cross $P$ an odd number of times. Moreover, by uncrossing subpaths against $P$, there exists a minimum-weight separating dual cycle $C^*$ that crosses $P$ **exactly once** (at some single dual edge $e_i^*$ corresponding to $e_i \in P$)!
  3. **Slice the Dual Graph Along $P$**: Cut the planar surface open along the path $P$. Each dual edge $e_i^*$ crossing $P$ is split into a left endpoint $l_i$ (on the left bank of the cut) and a right endpoint $r_i$ (on the right bank of the cut).
  4. Then the minimum separating dual cycle is:
     $$\text{MinCut}_G(s, t) = \min_{1 \le i \le k} \left( w(e_i) + \text{ShortestPath}_{G^*_{\text{sliced}}}(l_i \to r_i) \right).$$
- **Step 4: Complete Divide-and-Conquer Solution & Complexity**:
  Because shortest paths $Q_i$ from $l_i$ to $r_i$ in the planar graph $G^*_{\text{sliced}}$ can be chosen to be **mutually non-crossing** (if $i < j$, $Q_i$ does not cross $Q_j$), we use **Divide and Conquer on the interval $[1, k]$**:
  - Pick the midpoint $m = \lfloor (1 + k)/2 \rfloor$, run a single Dijkstra from $l_m$ to $r_m$ in the current region to find the shortest path $Q_m$.
  - Slice the current region along $Q_m$ into two smaller subregions (one containing $\{l_1, \dots, l_{m-1}\}$ and one containing $\{l_{m+1}, \dots, l_k\}$) and recurse!
  - Since each dual face appears in at most $2$ subproblems per recursion level, each of the $O(\log k)$ recursion levels runs Dijkstra on total size $O(V)$, achieving **$O(V \log^2 V)$** total time!

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 21
- **Hint 1 (Diagnostic)**: When $s$ and $t$ are not on the outer face, an $s$-$t$ cut in $G$ is a dual cycle $C^*$ in $G^*$ that encloses $t$ and excludes $s$.
- **Hint 2 (Compilation)**: Take any shortest path $P = (e_1, \dots, e_k)$ from $s$ to $t$ in $G$. Every separating dual cycle must cross $P$ an odd number of times, and the optimal one crosses $P$ at a single edge $e_i \in P$!
- **Hint 3 (Divide & Conquer)**: Cut the dual graph open along $P$ so $e_i^*$ splits into $l_i$ and $r_i$. Since the shortest paths $l_i \to r_i$ do not cross each other, find the path for midpoint $m = k/2$, split the graph along that path, and recurse in $O(V \log^2 V)$!
:::

---

#### Problem 22: `All-$\lambda$ Parametric Maximum Density Decomposition` (Gallo–Grigoriadis–Tarjan Nested Density Cuts — `CF 1034 D` / Dense Subgraph Hierarchy)
- **Judge URL**: [Codeforces / Parametric Density Hierarchy Benchmark](https://codeforces.com/problemset/problem/1063/F) (`[EN]` Gallo, Grigoriadis & Tarjan 1989; `[ZH]` Amber 2007 Section 5)
- **Archetype**: Parametric Goldberg Density Network + Nested Submodular Cut Monotonicity $S^*(\lambda_1) \supseteq S^*(\lambda_2)$ (Iterations 21 & 22 Synthesis)
- **Problem Statement & Constraints**:
  Given an undirected edge-weighted graph $G = (V, E)$ with $N \le 1500, M \le 5000$, answer $Q \le 2 \times 10^5$ queries. Each query gives a penalty $\lambda > 0$ and asks for the value of $\max_{S \subseteq V} \big( W(E(S)) - \lambda |S| \big)$ (the full piecewise-linear upper envelope of subgraph densities across all $\lambda \in [0, \infty)$).
- **Step 1: Non-Graph Diagnostic Signal**:
  Instead of finding the single maximum density $\lambda^*$, we must construct the **entire concave piecewise-linear curve** $g(\lambda) = \max_{S \subseteq V} \big(W(E(S)) - \lambda |S|\big)$ across all $\lambda \ge 0$ to answer $Q = 2 \times 10^5$ queries in $O(\log N)$ per query!
- **Step 2 & 3: Algebraic Nesting Theorem & Divide-and-Conquer Compilation**:
  - **Theorem (Nested Monotonicity of Goldberg Density Cuts)**:
    In Goldberg's network $G_\lambda$, source capacities $c(s \to v) = U$ and internal capacities $c(u \leftrightarrow v) = w_{uv}$ are **independent of $\lambda$**, while sink capacities $c_\lambda(v \to t) = U + 2\lambda - \deg_w(v)$ are **strictly increasing in $\lambda$**.
    By submodularity of cuts, the $S$-minimal optimal subgraphs $S^*(\lambda)$ are **monotonically nested**:
    $$0 \le \lambda_1 < \lambda_2 \implies V \supseteq S^*(\lambda_1) \supseteq S^*(\lambda_2) \supseteq \emptyset!$$
  - **Consequence**: Because a chain of nested subsets $V \supseteq S_1 \supsetneq S_2 \supsetneq \dots \supsetneq S_k = \emptyset$ has length **at most $N$**, the piecewise-linear curve $g(\lambda)$ has **at most $N$ linear segments and at most $N - 1$ breakpoints**!
- **Step 4: Complete Divide-and-Conquer Parametric Algorithm**:
  - Define `solve(L, R, V_active, E_active)` where all vertices in `V_active` are known to stay in $S^*(L)$ and leave by $S^*(R)$:
    1. Let $\lambda_{\text{mid}}$ be the intersection point of the line for $S^*(L)$ and the line for $S^*(R)$:
       $$\lambda_{\text{mid}} = \frac{W(E(S^*(L))) - W(E(S^*(R)))}{|S^*(L)| - |S^*(R)|}.$$
    2. Build Goldberg's network on `V_active` (with vertices already fixed in $S^*(R)$ contracted into $s$, and vertices outside $S^*(L)$ contracted into $t$) at $\lambda = \lambda_{\text{mid}}$, and run Dinic to find $S^*(\lambda_{\text{mid}})$.
    3. If $W(E(S^*(\lambda_{\text{mid}}))) - \lambda_{\text{mid}} |S^*(\lambda_{\text{mid}})|$ lies strictly above the intersection of the two lines, record $S^*(\lambda_{\text{mid}})$ on the hull and recurse on `(L, mid, V_active \ S*(mid))` and `(mid, R, S*(mid))`!
  - Because each vertex $v \in V$ goes into either the left subproblem or the right subproblem at every recursion level, the total size of all graphs at each recursion depth is $O(N + M)$, finding all $\le N$ breakpoints in $O(\log N)$ layers of Dinic! Each of the $Q = 2 \times 10^5$ queries is then answered in $O(\log N)$ via binary search on the hull!

::: {.callout-tip collapse="true"}
##### Progressive Hints for Problem 22
- **Hint 1 (Diagnostic)**: Why does $g(\lambda) = \max_{S \subseteq V} (W(E(S)) - \lambda |S|)$ have at most $N$ linear pieces instead of $2^N$?
- **Hint 2 (Nesting Property)**: In Goldberg's network, increasing $\lambda$ only increases the $v \to t$ capacities, pulling vertices from $S$ into $T$. Thus $\lambda_1 < \lambda_2 \implies S^*(\lambda_1) \supseteq S^*(\lambda_2)$!
- **Hint 3 (Divide & Conquer)**: Given two optimal sets $S_L \supsetneq S_R$, test their line intersection $\lambda_{\text{mid}} = \frac{W(E(S_L)) - W(E(S_R))}{|S_L| - |S_R|}$. Partition the active vertices into $S(\lambda_{\text{mid}})$ (contracted into $s$ for the left call) and $S_L \setminus S(\lambda_{\text{mid}})$ (contracted into $t$ for the right call)!
:::

---

## Quarantined Template Problems Table (`R-01`–`R-08`)

Per `AGENTS.md` and `flows_research/PLAN.md`, bare template verification problems whose sole task is copying a standard library routine are excluded from the 4-Tier Curated Problem Bank and quarantined below as verification references:

| Quarantine ID | Problem Title & Judge URL | Underlying Routine | Reason for Quarantine |
| :--- | :--- | :--- | :--- |
| **`R-01`** | [Luogu P3376 — 【模板】网络最大流](https://www.luogu.com.cn/problem/P3376) | Standard Dinic Max-Flow | Direct template verification; zero modelling. |
| **`R-02`** | [Luogu P4897 — 【模板】最小割树 (Gomory-Hu Tree)](https://www.luogu.com.cn/problem/P4897) | Gusfield / Gomory–Hu Cut Tree | Explicitly named template problem for pairwise min-cut queries. |
| **`R-03`** | [Luogu P5632 — 【模板】Stoer-Wagner](https://www.luogu.com.cn/problem/P5632) | Stoer–Wagner Global Minimum Cut | Explicitly named template verification for global undirected min-cut. |
| **`R-04`** | [LOJ 104 / Library Checker — Global Minimum Cut of Dynamic Star Augmented Graph](https://judge.yosupo.jp/) | Stoer–Wagner / Matroid Cut | Library verification benchmark. |
| **`R-05`** | [POJ 2976 — Dropping Tests](http://poj.org/problem?id=2976) | 0-1 Fractional Programming (Greedy Sort) | No graph/cut dependencies; solvable by sorting $a_i - \lambda b_i$. |
| **`R-06`** | [Luogu P3199 — [HNOI2009] 最小圈](https://www.luogu.com.cn/problem/P3199) | Minimum Mean Cycle (Bellman–Ford / SPFA) | Uses fractional programming + SPFA negative cycle detection rather than Min-Cut (included in Iteration 21 Table for contrast). |
| **`R-07`** | [Luogu P4174 — [NOI2006] 最大获利](https://www.luogu.com.cn/problem/P4174) | Base Bipartite Project Selection | Standard Wave 2A closure; only its ratio/Goldberg extension (Problem 9) belongs to Wave 3A. |
| **`R-08`** | [Luogu P4719 — 【模板】"动态 DP"&动态树分治](https://www.luogu.com.cn/problem/P4719) | Dynamic Tree Independent Set | Base DDP template; Problem 10 adapts this framework to Dynamic Tree Max-Flow. |

---

## Multilingual Bibliography & Seminal References (`[EN]` / `[ZH]` / `[JA]`)

### 1. English (`[EN]`) Seminal Papers & Monographs
- **`[EN-Dinkelbach67]`** Werner Dinkelbach (1967), *"On Nonlinear Fractional Programming"*, Management Science 13(7), 492–498. — Introduces the parametric auxiliary function $h(\lambda) = \min_{x \in \mathcal{F}} (N(x) - \lambda D(x))$ and proves superlinear convergence of the Newton-secant update $\lambda_{k+1} = N(x_{k+1}) / D(x_{k+1})$.
- **`[EN-Radzik98]`** Tomasz Radzik (1998), *"Fractional Combinatorial Optimization"*, in *Handbook of Combinatorial Optimization*, Vol. 1, 429–478, Springer. — Proves strongly polynomial bounds $O(|V|^2 \log |V|)$ for Dinkelbach's algorithm on integer 0-1 fractional network problems.
- **`[EN-Goldberg84]`** Andrew V. Goldberg (1984), *"Finding a Maximum Density Subgraph"*, Technical Report UCB/CSD-84-171, University of California, Berkeley. — Originates the $|V|+2$ vertex degree-identity reduction $2|E(S)| = \sum_{v \in S} \deg(v) - |\delta(S, \bar{S})|$ for Maximum Density Subgraph.
- **`[EN-GGT89]`** Giorgio Gallo, Michael D. Grigoriadis, and Robert E. Tarjan (1989), *"A Fast Parametric Maximum Flow Algorithm and Applications"*, SIAM Journal on Computing 18(1), 30–55. — Proves nested cut monotonicity $S^*(\lambda_1) \supseteq S^*(\lambda_2)$ and computes all critical breakpoints of parametric flow/density networks in the asymptotic time of a single preflow-push call.
- **`[EN-Hassin81]`** Refael Hassin (1981), *"Maximum Flow in $(s, t)$ Planar Networks"*, Information Processing Letters 13(3), 107. — Establishes the reduction of outer-face $s$-$t$ planar minimum cut to a single dual shortest path computation.
- **`[EN-Reif83]`** John H. Reif (1983), *"Minimum $s$-$t$ Cut of a Planar Undirected Network in $O(n \log^2 n)$ Time"*, SIAM Journal on Computing 12(1), 71–81. — Introduces primal shortest-path slicing and divide-and-conquer dual Dijkstra for interior $s$-$t$ planar minimum cuts.
- **`[EN-GH61]`** Ralph E. Gomory and T. C. Hu (1961), *"Multi-Terminal Network Flows"*, Journal of the Society for Industrial and Applied Mathematics 9(4), 551–570. — Proves the submodular uncrossing lemma and constructs the $N-1$ Max-Flow Cut Tree $T_{\text{GH}}$.
- **`[EN-Gusfield90]`** Dan Gusfield (1990), *"Very Simple Methods for All Pairs Network Flow Analysis"*, SIAM Journal on Computing 19(1), 143–155. — Eliminates graph contraction from Gomory–Hu tree construction, enabling 15-line competitive programming implementations on the unmodified graph $G$.
- **`[EN-SW97]`** Mechthild Stoer and Frank Wagner (1997), *"A Simple Min-Cut Algorithm"*, Journal of the ACM 44(4), 585–591 (and Hiroshi Nagamochi & Toshihide Ibaraki, 1992). — Proves the Maximum Adjacency Ordering theorem $\lambda_G(v_{n-1}, v_n) = w(V \setminus \{v_n\}, v_n)$.

### 2. Chinese (`[ZH]`) National Team Papers (`国家集训队论文`) & Archives
- **`[ZH-Amber07]`** 胡伯涛 (Amber / Hu Botao, 2007), *《最小割模型在信息学竞赛中的应用》* (*Applications of Minimum Cut Models in Olympiad in Informatics*), 2007 国家集训队论文. — The foundational Chinese monograph systematizing 0-1 Fractional Programming Cuts (`分数规划最小割`), Goldberg's Maximum Density Subgraph (`最大密度子图` with the $U$-shift trick and $1/N^2$ gap analysis), and Vertex/Edge-Weighted Density Subgraphs (`POJ 3155 Hard Life`, `[NOI2006] 最大获利` extensions).
- **`[ZH-ZhouDong09]`** 周冬 (Zhou Dong, 2009), *《浅析最大最小定理在信息学竞赛中的应用》* (*On the Application of Max-Min Duality Theorems in OI*), 2009 国家集训队论文. — Comprehensive treatment of Planar Graph Cut–Cycle Duality (`[BJWC2006] 狼抓兔子`, `[NOI2010] 海拔` precursor models) and converting intractable Max-Flow problems into Min-Cut DP.
- **`[ZH-NOI2010-Alt]`** `[NOI2010] 海拔` Official Editorial & Coarea Proof Archive (Luogu P2046 / UOJ / LOJ). — Establishes the two-stage reduction from continuous potential differences $\max(0, h_v - h_u)$ to binary $\{0, 1\}$ cuts and $90^\circ$-rotated Directed Dual Dijkstra.
- **`[ZH-CSP2021-Traffic]`** `[CSP-S 2021] 交通规划` Official Solution & Multi-Terminal Outerplanar Cut Treatise (Luogu P7916). — Generalizes outer-face planar dual shortest path to $k$ alternating boundary terminals via Circular Non-Crossing Interval DP.

### 3. Japanese (`[JA]`) Competitive Programming Treatises & AtCoder Archives
- **`[JA-noshi91]`** `noshi91`, *「燃やす埋める問題と劣モジュラ関数」* (*Project Selection / Burn-or-Bury Problems and Submodular Functions*). — Algebraic treatment of pairwise quadratic terms $x_u x_v$ and degree-summation reductions eliminating auxiliary edge vertices.
- **`[JA-maspypy]`** `maspypy`, *「最大流・最小カットの双対性と DP への帰着」* (*Max-Flow Min-Cut Duality and Reduction to Dynamic Programming*, AtCoder `ARC 125 E`, `AGC 031 E` editorials). — Systematizes Direction B (`Flow $\to$ Min-Cut DP / Greedy`) for complete bipartite and coordinate-rank networks where $N \le 2 \times 10^5$.
- **`[JA-tatyam]`** `tatyam`, *「平面グラフの最小カットと双対グラフ最短路」* (*Minimum Cuts on Planar Graphs and Dual Shortest Paths*). — Clean geometric orientation contracts (Right-Hand Rule / $90^\circ$ rotation) for directed planar dual graphs.
