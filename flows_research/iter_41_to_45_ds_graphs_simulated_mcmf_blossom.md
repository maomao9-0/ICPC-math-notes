# Wave 5A Research Monograph: Data-Structure Graph Sparsification, Simulated Min-Cost Flow (`模拟费用流`), & General Graph Matching (Iterations 41–45)

> [!IMPORTANT]
> **Cohort 1 — Wave 5A Discovery & Modelling Monograph (`FlowDeepInvestigator`)**
> This monograph covers **Iterations 41 through 45** of the Phase 1 Multi-Cohort Research Schedule (`flows_research/PLAN.md`). Every modelling archetype, data-structure reduction, residual heap simulation, and non-bipartite blossom transformation strictly adheres to the **4-Step "Zero Magic Gadgets" Compilation Standard**:
> 1. **Step 1: Non-Graph Diagnostic Signal (Recognition)** — What exact constraint scale ($N \le 5 \cdot 10^4$ vs. $N \le 5 \cdot 10^5$), structural topology (1D intervals, 2D prefix dominance, trees, general non-bipartite graphs), and failure of naive DP/greedy forces a sparse flow graph, a simulated residual heap, or Edmonds' blossom contraction.
> 2. **Step 2: Algebraic / Logical Intermediate Representation** — Formulating the problem via pseudo-Boolean cut polynomials $\sum c_{uv} x_u (1 - x_v)$, flow conservation equations, LP dual potentials $\pi_v - \pi_u \le c(u, v)$, or skew-symmetric Tutte polynomial ranks *before* introducing vertices, priority queues, or blossoms.
> 3. **Step 3: Reverse-Engineering Scratchpad (Mechanical Compilation)** — Deriving the exact auxiliary tree topologies, heap regret values ($-2x_i - v$), segment tree residual counters, multi-queue state machines, or blossom contraction invariants from the algebraic equations.
> 4. **Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples** — Concrete $N \le 4$ traces alongside explicit proofs of what breaks when subtle edges, version links, or regret tokens are omitted.

---

## Executive Overview: The Three Scaling & Structural Frontiers of Network Flows

In Waves 1A through 4B, we established how to compile non-graph combinatorial optimization problems into explicit Maximum Flow, Minimum Cut, Bipartite Matching, or Min-Cost Max-Flow (MCMF) networks. However, three fundamental barriers arise in advanced competitive programming when moving from textbook models to Grandmaster-level problems:

1. **The Dense Edge Barrier ($V \le 5 \cdot 10^4$, Naive $E = \Theta(V^2)$) $\implies$ Data-Structure Graph Sparsification (`数据结构优化建图`, Iteration 41)**:
   - *Symptom*: The vertex count $N \le 5 \cdot 10^4$ is small enough for Dinic's algorithm or SSP MCMF, and the true capacity bottlenecks sit on the $O(N)$ source/sink/item edges, **but** the transition rules connect each vertex $i$ to an entire 1D interval $[L_i, R_i]$, a 2D prefix rectangle $(j < i, L_i \le a_j \le R_i)$, a tree path, a XOR prefix subtree, or a 2D bounding box.
   - *Resolution*: Because any biclique $A \times B$ of capacity $\infty$ and additive cost $c(u, v) = c_1(u) + c_2(v)$ is cut-equivalent and flow-equivalent to routing through a single intermediate hub vertex $h$, we embed standard data structures (**Segment Trees, Persistent Segment Trees, CDQ Divide-and-Conquer Chains, 0-1 Tries, Heavy-Light Decompositions, and 2D KD-Trees**) directly inside the flow network as $\infty$-capacity routing backbones, compressing $\Theta(N^2)$ edges to $O(N \log N)$ or $O(N \log^2 N)$.

2. **The Asymptotic Solver Barrier ($N \le 10^5$–$5 \cdot 10^5$) $\implies$ Simulated Min-Cost Flow (`模拟费用流`, Iterations 42–43)**:
   - *Symptom*: The problem is 100% equivalent to an MCMF network (and greedy or standard DP fails because earlier decisions must be *revoked* or *rerouted*), **but** $N \ge 10^5$ forbids running any explicit graph algorithm.
   - *Resolution (Direction B: Flow $\to$ Non-Flow Fast Algorithm)*: When the underlying flow graph is a 1D line, a tree, a $k$-disjoint interval DAG, or a coupled bipartite hub network with $O(1)$ internal states, the Successive Shortest Path (SSP) / Negative Cycle Cancellation algorithm has only a small, structured family of possible augmenting paths. Instead of building adjacency lists, we maintain the **active residual edges implicitly** in Priority Queues (`反悔贪心`), Mergeable Heaps / Slope Trick (`树上模拟费用流`), Dynamic Segment Trees (`线段树维护增广路`), or Multi-Heap Finite State Machines (`多堆状态自动机`), executing each augmentation in $O(\log N)$ time!

3. **The Odd-Cycle Parity Barrier ($V \le 500$, Non-Bipartite Compatibility) $\implies$ General Graph Matching (`带花树` & Algebraic Matching, Iterations 44–45)**:
   - *Symptom*: We must pair items under arbitrary symmetric compatibility where the interaction graph contains **odd cycles**, destroying Total Unimodularity (TU), bipartite two-coloring, and König/Hall dualities as stated.
   - *Resolution*: We study **Edmonds' Blossom Algorithm (`带花树`)**, the **Tutte–Berge Formula** (the exact non-bipartite generalization of Hall's theorem), the **Gallai–Edmonds Decomposition** (the non-bipartite generalization of Dulmage–Mendelsohn for 2-player walk games), and the **Skew-Symmetric Tutte Matrix** (which reduces general matching rank and matroid intersection queries to $O(V^3)$ randomized Gaussian elimination via the Schwartz–Zippel lemma), concluding with a sharp boundary comparison between **Lindström–Gessel–Viennot (LGV)** and **MCMF** for vertex-disjoint paths.

---

## Iteration 41: Data-Structure-Accelerated Flow Graphs (`数据结构优化建图`)

### 1. Step 1: The Non-Graph Diagnostic Signal (Recognition)

How do you recognize that a problem requires Data-Structure-Accelerated Flow Graph Construction (`数据结构优化建图`)?

- **Constraint Signature**: $N, M \le 10^4 \text{ to } 5 \cdot 10^4$ (occasionally $10^5$ for pure unit-capacity or small-flow networks), and time limit $1.0\text{s}$–$3.0\text{s}$.
- **Structural Clues in the Statement**:
  1. The problem has an unmistakable Min-Cut (Project Selection / `燃やす埋める`), Bipartite Matching, or MCMF core (e.g., "select a subset of items to maximize profit minus penalty", "assign each element to at most one predecessor", or "route $K$ units of supply").
  2. However, the dependency or transition relation is **bulk-geometric** rather than explicit:
     - *"If you choose item $i$, you must also choose all items $j$ in index range $[L_i, R_i]$"* (1D Interval Dependency).
     - *"If you choose item $i$ in state White, and any earlier item $j < i$ with value $a_j \in [L_i, R_i]$ is in state Black, you pay penalty $p_i$"* (`BZOJ 3218 a + b Problem` — 2D Prefix-Range Dominance).
     - *"Each node $i$ can connect to any earlier node $j < i$ at cost $|a_i - a_j|$"* (`[省选联考 2019] 通信` — 2D Prefix + Absolute Value Cost).
     - *"If you activate node $u$, all nodes $v$ on the tree path $u \leftrightarrow w$ (or in $u$'s subtree) are affected"* (Tree Path/Subtree Dependency).
     - *"Node $i$ can transition to any node $j$ inside rectangle $[x_1, x_2] \times [y_1, y_2]$"* (`[NOI2019] 弹跳` — 2D Orthogonal Range).
- **Why Naive Approaches Fail**:
  - **Naive Graph Construction**: Explicitly adding an edge $(i, j)$ for every valid pair creates $\Theta(N^2)$ edges ($2.5 \times 10^9$ edges for $N = 5 \cdot 10^4$), causing immediate Memory Limit Exceeded (MLE) and Time Limit Exceeded (TLE).
  - **Pure Data Structures / DP**: Because the problem involves global cyclic implications, arbitrary $S$-$T$ min-cuts, or multi-step flow conservation with capacities, greedy and DP cannot resolve the global bottlenecks without a flow/cut engine.

---

### 2. Step 2: Algebraic / Logical Intermediate Representation (The Biclique Hub Theorem)

Before introducing segment trees or CDQ divide-and-conquer, let us prove algebraically why bulk edges can be factored through intermediate vertices.

#### Theorem 41.1 (Biclique Cut & Flow Factorization)
Suppose a subset of vertices $A$ must be connected to a subset of vertices $B$:

1. **Min-Cut (`燃やす埋める`) Perspective**:
   Suppose choosing any $u \in A$ on the $S$-side ($x_u = 1$) while leaving any $v \in B$ on the $T$-side ($x_v = 0$) is forbidden (infinite penalty). In pseudo-Boolean cut polynomial form, this constraint is:
   $$\Phi_{A \to B}(x) = \sum_{u \in A} \sum_{v \in B} \infty \cdot x_u (1 - x_v).$$
   Introduce a single auxiliary binary variable $x_h \in \{0, 1\}$ (a virtual hub vertex $h$) and consider the factored polynomial:
   $$\widehat{\Phi}_{A \to h \to B}(x, x_h) = \sum_{u \in A} \infty \cdot x_u (1 - x_h) + \sum_{v \in B} \infty \cdot x_h (1 - x_v).$$
   Taking the minimum over $x_h \in \{0, 1\}$ for any fixed assignment of $x$:
   $$\min_{x_h \in \{0, 1\}} \widehat{\Phi}_{A \to h \to B}(x, x_h) = \begin{cases} 0 & \text{if } (\forall u \in A, x_u = 0) \text{ or } (\forall v \in B, x_v = 1), \\ \infty & \text{if } (\exists u \in A, x_u = 1) \text{ and } (\exists v \in B, x_v = 0). \end{cases}$$
   Thus $\min_{x_h} \widehat{\Phi}_{A \to h \to B}(x, x_h) = \Phi_{A \to B}(x)$ identically! Replacing $|A| \cdot |B|$ direct $\infty$-edges with $|A| + |B|$ edges through $h$ preserves the exact capacity of every finite $S$-$T$ cut.

2. **Separable-Cost MCMF Perspective**:
   Suppose every $(u, v) \in A \times B$ has an uncapacitated directed edge $u \to v$ of cost $c(u, v) = c_{\text{out}}(u) + c_{\text{in}}(v)$. Let $f_{u,v} \ge 0$ be the flow on $(u, v)$. The total cost is:
   $$\sum_{u \in A} \sum_{v \in B} f_{u,v} \big(c_{\text{out}}(u) + c_{\text{in}}(v)\big) = \sum_{u \in A} c_{\text{out}}(u) \underbrace{\left(\sum_{v \in B} f_{u,v}\right)}_{f_{u \to h}} + \sum_{v \in B} c_{\text{in}}(v) \underbrace{\left(\sum_{u \in A} f_{u,v}\right)}_{f_{h \to v}},$$
   subject to flow conservation $\sum_{u \in A} f_{u \to h} = \sum_{v \in B} f_{h \to v}$ at hub $h$. By flow decomposition, any flow routing through $h$ decomposes into $(u, v)$ paths of exact cost $c_{\text{out}}(u) + c_{\text{in}}(v)$.

> [!IMPORTANT]
> **The Fundamental Requirement for Data-Structure Sparsification**:
> You can factor a dense edge set $E' \subseteq A \times B$ through an auxiliary DAG of hubs **if and only if**:
> 1. Each internal edge $(u, v) \in E'$ has **infinite capacity** ($\text{cap}(u, v) = \infty$), while finite capacities are attached only to the entry edges into $A$ or exit edges out of $B$; AND
> 2. In MCMF, the cost $c(u, v)$ decomposes additively along the paths of the auxiliary DAG!

---

### 3. Step 3: Reverse-Engineering Scratchpad — The 5 Canonical Sparsification Architectures

#### Architecture 41.1: 1D Segment Tree In-Tree & Out-Tree (`线段树优化建图`)
Suppose we have $N$ base vertices $1, \dots, N$ and operations connecting a vertex $u$ to all $v \in [L, R]$, all $u \in [L, R]$ to $v$, or all $u \in [L_1, R_1]$ to all $v \in [L_2, R_2]$ with capacity $C$ and cost $W$.

- **Decomposition**: A standard segment tree over $[1, N]$ partitions any query interval $[L, R]$ into $O(\log N)$ canonical dyadic intervals $I_1, I_2, \dots, I_k$.
- **Why Two Trees Are Needed**:
  - **Out-Tree (`出树` — Distributing Flow from an Interval Node to its Leaves)**:
    Each segment tree node $p$ has directed edges to its children:
    $$\text{Out}(p) \xrightarrow{\text{cap} = \infty, \text{cost} = 0} \text{Out}(\text{lc}(p)), \qquad \text{Out}(p) \xrightarrow{\text{cap} = \infty, \text{cost} = 0} \text{Out}(\text{rc}(p)).$$
    To connect $u \to [L, R]$ with total capacity $C$ and cost $W$:
    - *If each $v \in [L, R]$ can receive unlimited flow from $u$, or the bottleneck $C$ is shared across the whole bundle $u \to [L, R]$*: Create a virtual bridge vertex $b$ (or connect directly from $u$ if $C = \infty$), add $u \xrightarrow{\text{cap}=C, \text{cost}=W} b$, and connect $b \xrightarrow{\text{cap}=\infty, \text{cost}=0} \text{Out}(p_r)$ for each of the $O(\log N)$ canonical nodes $p_r$ covering $[L, R]$.
  - **In-Tree (`入树` — Collecting Flow from Leaves into an Interval Node)**:
    Each segment tree node $p$ receives directed edges from its children:
    $$\text{In}(\text{lc}(p)) \xrightarrow{\text{cap} = \infty, \text{cost} = 0} \text{In}(p), \qquad \text{In}(\text{rc}(p)) \xrightarrow{\text{cap} = \infty, \text{cost} = 0} \text{In}(p).$$
    To connect $[L, R] \to v$ with shared bundle capacity $C$ and cost $W$: create bridge $b$, connect $\text{In}(p_r) \xrightarrow{\text{cap}=\infty, \text{cost}=0} b$ for each canonical node $p_r \subseteq [L, R]$, and add $b \xrightarrow{\text{cap}=C, \text{cost}=W} v$.
  - **Leaf Identification**: At the leaves ($L = R = i$), $\text{Out}(\text{leaf}(i))$ and $\text{In}(\text{leaf}(i))$ are identified directly with the original vertex $i$ (saving $2N$ vertices).
  - **Interval-to-Interval ($[L_1, R_1] \to [L_2, R_2]$)**: Never add $O(\log^2 N)$ pairwise edges between the two canonical sets! Create a **single virtual bridge vertex** $b$, connect the $O(\log N)$ nodes of $\text{In}([L_1, R_1])$ to $b$ ($\text{cap}=\infty, \text{cost}=0$), and from $b$ (or across a split bridge $b_{\text{in}} \xrightarrow{\text{cap}=C, \text{cost}=W} b_{\text{out}}$) connect to the $O(\log N)$ nodes of $\text{Out}([L_2, R_2])$. Total edges per interval-to-interval rule: $O(\log N)$.

```
        In-Tree (Collects upward)              Bridge               Out-Tree (Distributes downward)
   [1]   [2]   [3]           [1..2] [3]                             [2..3]          [2]   [3]   [4]
    \     /     |               \    /                                |              \     /     |
    In[1..2]  In[3]              \  /                                 v               \   /      |
        \      /                  v                                Out[2..3]         Out[2..3] Out[4]
         v    v                 (b_in) --(cap=C, cost=W)--> (b_out) /     \
        In[1..3]                                                   v       v
                                                                 [2]       [3]
```

---

#### Architecture 41.2: Persistent Segment Tree Prefix-Range Sparsification (`可持久化线段树优化建图` — `BZOJ 3218 a + b Problem`)
Suppose each vertex $i \in \{1, \dots, N\}$ has a value $a_i$ and wants to connect to all **earlier** vertices $j < i$ whose values satisfy $L_i \le a_j \le R_i$.

- **Why a Static 1D Segment Tree Fails**: The condition has *two* orthogonal inequalities: index order $j < i$ and value interval $L_i \le a_j \le R_i$. A 2D Segment Tree would work in $O(N \log^2 N)$ vertices/edges, which is often too heavy for Dinic/MCMF in $1\text{s}$.
- **How Persistence Eliminates the Time Dimension**:
  1. Discretize all values $a_1, \dots, a_N$ into $\{1, \dots, U\}$ where $U \le N$.
  2. Maintain a **Persistent Out-Tree** over the value domain $[1, U]$. Version $i$ (`root[i]`) contains only the vertices $\{1, 2, \dots, i\}$.
  3. At step $i = 1, 2, \dots, N$:
     - **Query first (strictly $j < i$)**: Decompose $[L_i, R_i]$ in **Version $i-1$** (`root[i-1]`) into $O(\log U)$ persistent segment tree nodes, and add edges from $i$ (or $i$'s auxiliary penalty node $i'$) to those $O(\log U)$ nodes with capacity $\infty$. Because `root[i-1]` only contains $j \in \{1, \dots, i-1\}$, vertex $i$ can never reach $j \ge i$!
     - **Insert $i$ to form Version $i$**: Allocate $O(\log U)$ new nodes along the path from the root to leaf $a_i$. For each newly created internal node $p_{\text{new}}$ (copied from $p_{\text{old}}$), connect:
       $$p_{\text{new}} \xrightarrow{\infty} \text{lc}(p_{\text{new}}), \qquad p_{\text{new}} \xrightarrow{\infty} \text{rc}(p_{\text{new}}).$$
     - **Crucial Leaf Chaining Rule**: At the leaf for value $a_i$, create a new leaf node $p_{\text{new}}$, connect $p_{\text{new}} \xrightarrow{\infty} i$, **and if $p_{\text{old}}$ existed at this leaf in version $i-1$, also connect $p_{\text{new}} \xrightarrow{\infty} p_{\text{old}}$**! (Equivalently, for every new node $p_{\text{new}}$ along the path, connecting $p_{\text{new}} \xrightarrow{\infty} p_{\text{old}}$ automatically preserves reachability to all earlier elements $j < i$ that shared the same coordinate $a_j = a_i$).
  4. **Complexity**: $O(N \log N)$ vertices and $O(N \log N)$ edges — a full $\log N$ factor smaller than a 2D segment tree!

---

#### Architecture 41.3: CDQ Divide-and-Conquer Graph Sparsification (`CDQ 分治优化建图` — `[省选联考 2019] 通信`)
Suppose vertex $i$ can connect to any $j < i$ at cost $|a_i - a_j|$ (or any cost function depending on coordinate order after splitting into $a_j \le a_i$ and $a_j > a_i$).

- **Why Persistent Segment Tree Is Suboptimal Here**:
  In a segment tree, the distance $|a_i - a_j|$ is not constant across a canonical interval unless we maintain separate trees for $a_j \le a_i$ (cost $a_i - a_j$, pushing $+a_i$ on entry and $-a_j$ on exit) and $a_j > a_i$ (cost $a_j - a_i$, pushing $-a_i$ on entry and $+a_j$ on exit). Even better, **CDQ Divide-and-Conquer** handles both directions simultaneously with a simple 1D chain!
- **Mechanical Construction of `CDQ_Build(L, R)`**:
  To encode all directed transitions $j \leftarrow i$ (or $j \to i$) for $j \in [L, M]$ and $i \in [M+1, R]$ where $M = \lfloor (L+R)/2 \rfloor$:
  1. Recursively call `CDQ_Build(L, M)` and `CDQ_Build(M+1, R)`.
  2. Collect all distinct values $\{v_1 < v_2 < \dots < v_k\}$ among $\{a_t : t \in [L, R]\}$, where $k \le R - L + 1$.
  3. Create $k$ auxiliary **chain hub vertices** $h_1, h_2, \dots, h_k$ and link adjacent hubs bidirectionally with edge cost equal to the coordinate gap:
     $$h_r \xrightarrow{\text{cap} = \infty, \text{cost} = v_{r+1} - v_r} h_{r+1}, \qquad h_{r+1} \xrightarrow{\text{cap} = \infty, \text{cost} = v_{r+1} - v_r} h_r \quad (1 \le r < k).$$
  4. For every **right-half** index $i \in [M+1, R]$ with $a_i = v_r$, add an entry edge into the chain:
     $$i_{\text{out}} \xrightarrow{\text{cap} = \infty, \text{cost} = 0} h_r.$$
  5. For every **left-half** index $j \in [L, M]$ with $a_j = v_s$, add an exit edge out of the chain:
     $$h_s \xrightarrow{\text{cap} = \infty, \text{cost} = 0} j_{\text{in}}.$$
- **Why It Works**: Any path from $i_{\text{out}}$ ($i \in [M+1, R]$) to $j_{\text{in}}$ ($j \in [L, M]$) inside this layer enters at $h_r$ ($v_r = a_i$), walks along the 1D chain to $h_s$ ($v_s = a_j$), and exits to $j_{\text{in}}$. The shortest path along the chain has cost $\sum |v_{t+1} - v_t| = |v_r - v_s| = |a_i - a_j|$! Moreover, because only right-half vertices enter the chain and only left-half vertices exit the chain, **every valid path strictly respects $j \le M < i$ ($j < i$)**!
- **Complexity**: At each of the $\log_2 N$ recursion levels, the sum of $k$ across all intervals is $\le N$, adding at most $N$ hub vertices and $4N$ directed edges per level. Total size: **$N \log_2 N$ auxiliary vertices and $4 N \log_2 N$ edges**!

---

#### Architecture 41.4: HLD, 0-1 Trie, and 2D KD-Tree Sparsification
The exact same Biclique Hub Theorem compiles three additional geometric domains:

| Domain & Constraint Type | Decomposition Backbone | Auxiliary Vertices | Auxiliary Edges |
| :--- | :--- | :--- | :--- |
| **Tree Subtree** ($u$ connects to all $v \in \text{subtree}(w)$) | DFS Euler Tour (`dfn[w] .. dfn[w] + sz[w] - 1`) + 1D SegTree | $O(N)$ | $O(N + M \log N)$ |
| **Tree Path** ($u$ connects to all $v$ on path $x \leftrightarrow y$) | **Heavy-Light Decomposition (`树剖`)** ($O(\log N)$ heavy-path intervals) + 1D SegTree (or prefix nodes on heavy chains) | $O(N)$ | $O(N + M \log^2 N)$ (or $O(M \log N)$ with prefix hubs) |
| **Bitwise XOR Bound** ($u$ connects to all $v$ with $a_u \oplus a_v \le K$) | **0-1 Binary Trie** over $B$-bit integers: matching prefixes of $a_u \oplus K$ branch into $\le B$ full Trie subtrees where $a_u \oplus a_v < K$ | $O(N B)$ | $O(N B)$ |
| **2D Orthogonal Range** ($u$ connects to all $v$ with $(x_v, y_v) \in [x_1, x_2] \times [y_1, y_2]$) | **2D KD-Tree** (`[NOI2019] 弹跳`): each KD-Tree node stores its bounding box $[X_{\min}, X_{\max}] \times [Y_{\min}, Y_{\max}]$; query connects to $O(\sqrt{N})$ canonical subtrees | $O(N)$ | $O(M \sqrt{N})$ (or implicit in Dijkstra) |

---

### 4. Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Concrete Toy Trace: CDQ Sparsification on $N = 4$ with $a = [10, 30, 20, 40]$
Suppose each $i \in \{1, 2, 3, 4\}$ can match to an earlier $j < i$ at cost $|a_i - a_j|$. Consider the top-level CDQ split $[1, 4]$ with $M = 2$:
- Left half $j \in \{1, 2\}$ has values $a_1 = 10, a_2 = 30$.
- Right half $i \in \{3, 4\}$ has values $a_3 = 20, a_4 = 40$.
- Sorted coordinates in $[1, 4]$: $v_1 = 10, v_2 = 20, v_3 = 30, v_4 = 40$ with hubs $h_1, h_2, h_3, h_4$.
- Chain edges: $h_1 \leftrightarrow h_2$ (cost $10$), $h_2 \leftrightarrow h_3$ (cost $10$), $h_3 \leftrightarrow h_4$ (cost $10$).
- Entry edges from right half: $3_{\text{out}} \xrightarrow{0} h_2$ ($a_3 = 20$), $4_{\text{out}} \xrightarrow{0} h_4$ ($a_4 = 40$).
- Exit edges to left half: $h_1 \xrightarrow{0} 1_{\text{in}}$ ($a_1 = 10$), $h_3 \xrightarrow{0} 2_{\text{in}}$ ($a_2 = 30$).
- Let us check all 4 cross-half pairs $(i \in \{3, 4\}, j \in \{1, 2\})$:
  - $3_{\text{out}} \to h_2 \to h_1 \to 1_{\text{in}}$ has cost $0 + 10 + 0 = 10 = |20 - 10|$.
  - $3_{\text{out}} \to h_2 \to h_3 \to 2_{\text{in}}$ has cost $0 + 10 + 0 = 10 = |20 - 30|$.
  - $4_{\text{out}} \to h_4 \to h_3 \to 2_{\text{in}}$ has cost $0 + 10 + 0 = 10 = |40 - 30|$.
  - $4_{\text{out}} \to h_4 \to h_3 \to h_2 \to h_1 \to 1_{\text{in}}$ has cost $0 + 10 + 10 + 10 + 0 = 30 = |40 - 10|$.
  - Can $3_{\text{out}}$ reach $4_{\text{in}}$? No! $4_{\text{in}}$ has no exit edge from this layer's chain ($4 \notin [1, 2]$). Thus $j < i$ and $|a_i - a_j|$ are both enforced with 100% precision!

#### Four Fatal Broken Gadget Counterexamples

> [!WARNING]
> **Broken Gadget 1: Omitting `new_node -> old_node` in Persistent Segment Tree (`BZOJ 3218`)**
> Suppose $a_1 = 5$ and $a_2 = 5$ (duplicate coordinates), and $i = 3$ queries $[4, 6]$ in Version 2. When inserting $a_2 = 5$ to create Version 2, if the new leaf node $\text{leaf}_2(5)$ only connects to vertex $2$ ($\text{leaf}_2(5) \to 2$) and **forgets** to connect $\text{leaf}_2(5) \xrightarrow{\infty} \text{leaf}_1(5)$, then querying Version 2 at coordinate $5$ only reaches vertex $2$ and **loses the dependency on vertex $1$**! A valid cut could then set $x_3 = 1, x_2 = 1, x_1 = 0$ with zero penalty, violating the problem statement. Always add $p_{\text{new}} \xrightarrow{\infty} p_{\text{old}}$ at every modified node during persistent insertion.
>
> **Broken Gadget 2: Using a Single Undirected/Bidirectional Segment Tree Instead of Separate In-Tree & Out-Tree**
> If you merge $\text{In}(p)$ and $\text{Out}(p)$ into a single node $p$ with bidirectional $\infty$-edges $p \leftrightarrow \text{lc}(p), \text{rc}(p)$, then every leaf $i$ can reach every other leaf $j$ through the root with capacity $\infty$, collapsing the entire graph into a single connected component of $\infty$-capacity!
>
> **Broken Gadget 3: Placing Finite Capacity $C$ on Internal Segment Tree Edges**
> Internal edges of the In-Tree and Out-Tree are shared by *all* queries. They must always have $\text{cap} = \infty, \text{cost} = 0$. The query-specific capacity $C$ and cost $W$ must be placed on the dedicated virtual bridge edge $u \to b$ (or $b_{\text{in}} \to b_{\text{out}}$) created for that specific query.
>
> **Broken Gadget 4: Merging Right-Half Entries and Left-Half Exits across All Indices in One Global Chain without CDQ**
> If you build a single global 1D value chain $h_1 \leftrightarrow h_2 \leftrightarrow \dots \leftrightarrow h_N$ and let every $i$ both enter and exit the chain, then $i = 1$ can reach $j = 4$ ($j > i$), violating the DAG time order $j < i$ and creating 0-cycles! The CDQ recursion is what separates "sources" ($i \in [M+1, R]$) from "sinks" ($j \in [L, M]$).

---

## Iteration 42: Simulated Min-Cost Flow I (`模拟费用流` I) — Regret Greedy (`反悔贪心`), 1D Line Matching & Tree Slope Trick

### 1. Step 1: The Non-Graph Diagnostic Signal (Recognition)

How do you recognize a Simulated Min-Cost Flow (`模拟费用流`) problem?

- **Constraint Signature**: $N, M \le 10^5 \text{ to } 5 \cdot 10^5$ (or total supply $\sum c_i \le 10^{12}$). Explicit MCMF is impossible ($O(N^2)$ or $O(N F)$ TLEs immediately), yet $O(N \log N)$ or $O(N \log^2 N)$ passes easily.
- **Structural Clues in the Statement**:
  1. If $N$ were $500$, you would immediately solve the problem using **Min-Cost Max-Flow (MCMF)**: matching supplies to demands over time ($t_1 < t_2$), along a 1D coordinate line (cost $|x_i - y_j|$), or on a weighted tree (cost $\text{dist}(u, v)$).
  2. Naive greedy fails because a locally optimal pairing $(i, j)$ made at step $j$ may need to be **undone ("regretted")** when a better partner $k$ arrives later!
  3. Crucially, the graph topology is highly restricted: a 1D chain/DAG (`CF 865 D`), a 1D geometric line (`UOJ #455 雪灾与外卖`), or a tree (`[ICPC WF 2018] Conquer the World`).

---

### 2. Step 2: Algebraic / Logical Intermediate Representation (Residual Augmentation $\leftrightarrow$ Heap Regret)

What *is* Simulated Min-Cost Flow mathematically?

In the **Successive Shortest Path (SSP)** algorithm (or **Klein's Negative Cycle Cancellation**), we start from a flow $f$ of volume $k-1$ and transition to a min-cost flow $f'$ of volume $k$ by pushing $1$ unit of flow along a minimum-cost $S \to T$ path $P$ in the **residual network** $G_f$:
- If $P$ uses only **forward edges** $(u \to v)$ of original cost $+c(u, v)$, we are making a **direct greedy choice**.
- If $P$ traverses a **reverse residual edge** $(v \to u)$ of cost $-c(u, v)$ (which exists in $G_f$ *if and only if* $(u \to v)$ currently carries positive flow $f(u, v) > 0$), pushing $1$ unit of flow along $(v \to u)$ decreases $f(u, v)$ by $1$ — **canceling ("regretting") the previous greedy pairing $(u, v)$** and rerouting its endpoints!

> [!IMPORTANT]
> **The Core Principle of `模拟费用流` (Direction B: Flow $\to$ Non-Flow Fast Algorithm)**:
> Every item pushed into a Priority Queue in a "Regret Greedy" (`反悔贪心`) algorithm is **literally a residual path prefix** in $G_f$. Whenever we match $u$ and $v$ with cost $c(u, v)$, the residual graph $G_f$ gains the reverse edge $v \to u$ of cost $-c(u, v)$. By inserting a "regret token" with modified weight into our priority queue, we allow a future element $w$ to traverse the residual path $u \leftarrow v \to w$ in $O(\log N)$ time without ever building the graph!

---

### 3. Step 3: Reverse-Engineering Scratchpad — Three Foundational Simulation Models

#### Model 42.1: 1-Step Residual Regret (`CF 865 D — Buy Low Sell High`)
- **Problem**: Given stock prices $p_1, p_2, \dots, p_N$ over $N \le 3 \cdot 10^5$ days, on each day you can buy 1 share, sell 1 share you own, or do nothing. Maximize total profit.
- **Explicit MCMF Formulation (Minimize Cost = $-$Profit)**:
  For each day $i \in \{1, \dots, N\}$ with timeline edge $i \xrightarrow{\text{cap}=\infty, \text{cost}=0} i+1$:
  - Buying on day $i$: edge $S \to i$ with $\text{cap} = 1, \text{cost} = +p_i$.
  - Selling on day $j$: edge $j \to T$ with $\text{cap} = 1, \text{cost} = -p_j$.
- **Compiling the Residual Graph into a Single Min-Heap**:
  Suppose we sweep $j = 1, 2, \dots, N$ and maintain a min-heap $Q$ of available "effective buy prices" to pair with a sell on day $j$:
  1. On day $j$, we can always buy a fresh share at cost $+p_j$ (the edge $S \to j$). Push $p_j$ into $Q$.
  2. If the minimum element $x = Q.\text{top}()$ satisfies $p_j - x > 0$ (i.e., residual augmenting cycle cost $x - p_j < 0$), we greedily pair $x$ with a sell on day $j$, gaining profit $\Delta = p_j - x$, and pop $x$ from $Q$.
  3. **What changes in the residual graph $G_f$ when we sell on day $j$?**
     Two new residual possibilities open up for a future sell day $k > j$:
     - **(Option A — Cancel the sell on day $j$, routing the share from $x$ onwards to day $k$)**:
       In $G_f$, the edge $j \to T$ (cost $-p_j$) now has flow $1$, so its reverse edge $T \to j$ has cost $+p_j$. Canceling the sell on day $j$ and selling on day $k$ instead changes profit by:
       $$(p_k - x) - (p_j - x) = p_k - p_j.$$
     - **(Option B — Keep the sell on day $j$, AND also buy a share on day $j$ if day $j$ hadn't bought yet!)**:
       Note that Option A already acted as if we bought at $p_j$. Wait: in Step 1 we pushed one copy of $p_j$ (for the edge $S \to j$). When day $j$ sells a share bought at $x < p_j$, the copy of $p_j$ from Step 1 is *still in $Q$* (representing the unused edge $S \to j$), AND Option A (the reverse edge $T \to j$ of effective buy price $+p_j$) adds a **second copy of $p_j$** into $Q$!
     Therefore, when $x < p_j$ is popped and matched with day $j$:
     - We already pushed **one** $p_j$ in Step 1 (for $S \to j$),
     - We push a **second** $p_j$ into $Q$ (for the reverse residual edge $T \to j$ of canceling the sell at $j$)!
     - Total code inside the loop: `Q.push(p[j]); if (Q.top() < p[j]) { ans += p[j] - Q.top(); Q.pop(); Q.push(p[j]); }`. Six lines of $O(N \log N)$ code, 100% isomorphic to MCMF!

---

#### Model 42.2: 1D Line Mouse-to-Hole MCMF (`老鼠进洞` — `UOJ #455 雪灾与外卖`)
- **Problem**: $N$ mice at sorted positions $x_1 \le \dots \le x_N$ and $M$ holes at sorted positions $y_1 \le \dots \le y_M$. Hole $j$ has capacity $c_j$ and per-mouse entry cost $w_j$. Connecting mouse $i$ to hole $j$ costs $|x_i - y_j| + w_j$. Find the minimum cost to send all $N$ mice into holes ($N, M \le 10^5$, $c_j \le 10^9$).
- **Key Structural Lemma (Non-Crossing 1D Residual Paths)**:
  Sweep both mice and holes from left to right by coordinate. When a new element arrives at coordinate $z$, its distance to any already-visited coordinate $p \le z$ is simply $z - p$ (dropping the absolute value!).
- **Two-Heap Residual State Compilation (`MouseHeap` $Q_M$ and `HoleHeap` $Q_H$)**:
  Because every mouse *must* be matched (mandatory flow $= N$), we either add $-\infty$ (`-INF`) to mouse creation or force every mouse to match with the best available hole on arrival (if no hole exists yet, push a virtual hole at $-\infty$ with cost $+\infty$). Let us write the exact residual transitions at coordinate $z$:

  1. **Event Type 1: A Mouse Arrives at Coordinate $x$**:
     - We query the best available hole in $Q_H$, which stores keys $v_H$ such that matching with a mouse at $x \ge y$ costs $x + v_H$ (for a fresh hole at $y$ with entry cost $w$, its initial key is $v_H = -y + w$, giving cost $x - y + w$).
     - Let $v_H = Q_H.\text{top}()$. We pop $v_H$ and pay $\Delta = x + v_H$, adding $\Delta$ to `total_cost`.
     - **Residual Regret Token (`MouseHeap` $Q_M$)**:
       What if a future hole at $y' \ge x$ with cost $w'$ wants to **steal this mouse** (or equivalently, reverse the mouse's move to the left and send it right to $y'$)?
       - Currently this mouse contributed $\Delta = x + v_H$ to `total_cost`.
       - If it instead matches to a future hole at $y' \ge x$ (cost $y' - x + w'$), the net change in `total_cost` is:
         $$(y' - x + w') - \Delta = (y' + w') + (-x - \Delta) = (y' + w') + (-2x - v_H).$$
       - Therefore, we push a mouse-regret token into $Q_M$ with key:
         $$v_M = -x - \Delta = -2x - v_H.$$

  2. **Event Type 2: A Hole Arrives at Coordinate $y$ with Cost $w$ and Capacity $c$**:
     - First, this hole can be used by *future* mice ($x' \ge y$) as a fresh hole, which would have key $v_H = -y + w$ and multiplicity $c$.
     - Second, this hole can immediately augment by matching with an already-visited mouse token $v_M \in Q_M$ ($x \le y$) whenever the net change in cost is strictly negative:
       $$\Delta = (y + w) + v_M < 0.$$
     - Suppose $k$ mice in $Q_M$ with key $v_M$ are matched with this hole (consuming $k$ units of $c$ and adding $k \cdot \Delta$ to `total_cost`). **Two** residual edges are created in $G_f$:
       - **(Reverse Edge A — Future Mouse Steals This Hole)**:
         If a future mouse at $x' \ge y$ steals one of these $k$ slots in hole $y$ (pushing the old mouse back to its previous state before matching with $y$), the net cost change for $x'$ is:
         $$(x' - y + w) - \Delta = x' + \big(-y + w - (y + w + v_M)\big) = x' + (-2y - v_M).$$
         Thus we push $k$ tokens into $Q_H$ with key:
         $$v_H^{\text{regret}} = -2y - v_M.$$
       - **(Reverse Edge B — Future Hole $y'' \ge y$ Steals the Mouse That Just Entered Hole $y$)**:
         The mouse is now sitting inside hole $y$ (having paid $w$ at coordinate $y$). If a future hole $y'' \ge y$ with cost $w''$ takes this mouse instead of hole $y$, we save $w$, lose $w''$, and extend the mouse's rightward walk from $y$ to $y''$ by $y'' - y$:
         $$\text{Net change} = (y'' - y) + w'' - w = (y'' + w'') + (-y - w).$$
         Notice that if $c_{\text{rem}}$ unused slots remain in hole $y$, they *also* wait for future mice in $Q_H$ with key $-y + w$, while all $k$ used slots push a single batch of $k$ tokens into $Q_M$ with key:
         $$v_M^{\text{re-steal}} = -y - w!$$

- **Why Multiplicity Batching Achieves $O((N + M) \log(N + M))$**:
  Even when $c_j \le 10^9$, all $k$ mice popped with the same key $v_M$ generate identical tokens, and all $k$ mice entering hole $y$ share the exact same re-steal key $v_M^{\text{re-steal}} = -y - w$! Using `(key, count)` pairs in `std::priority_queue`, the amortized number of heap operations is $O(N + M)$.

---

#### Model 42.3: Tree MCMF via Mergeable Heaps & LCA Potential (`[ICPC WF 2018] Conquer the World`)
- **Problem**: Given a weighted tree with $N \le 2.5 \cdot 10^5$ vertices, vertex $u$ starts with $x_u$ armies and needs at least $y_u$ armies. Moving 1 army along edge $e$ costs $w_e$. Find the minimum cost to satisfy all demands.
- **Step 2 & 3 Compilation**:
  1. Root the tree arbitrarily at $1$, and let $d(u)$ be the weighted distance from root $1$ to $u$. For any pair $(u, v)$ whose lowest common ancestor is $L = \text{lca}(u, v)$:
     $$\text{dist}(u, v) = d(u) + d(v) - 2 d(L).$$
  2. Perform a bottom-up DFS. At each vertex $L$, maintain two **mergeable min-heaps** (e.g., Leftist Heaps / Skew Heaps or small-to-large `std::priority_queue`):
     - $Q_{\text{sup}}(L)$: available supply tokens (excess armies $x_u - y_u > 0$) in $L$'s subtree, initially pushed at $u$ with key $v_S = +d(u)$.
     - $Q_{\text{dem}}(L)$: unsatisfied demand tokens ($y_v - x_v > 0$) in $L$'s subtree, initially pushed at $v$ with key $v_D = +d(v) - M$ (where $M = 10^{12}$ is the mandatory demand penalty).
  3. After merging all children's heaps into $L$'s heaps, while $Q_{\text{sup}}(L)$ and $Q_{\text{dem}}(L)$ are non-empty and their top keys $v_S, v_D$ satisfy:
     $$\Delta = v_S + v_D - 2 d(L) < 0,$$
     we match $k = \min(\text{cnt}_S, \text{cnt}_D)$ units at LCA $L$, add $k \cdot \Delta$ to `total_cost`, and push **symmetric regret tokens** into both heaps so an ancestor $L'$ of $L$ can later break this match:
     $$v_S^{\text{regret}} = 2 d(L) - v_D, \qquad v_D^{\text{regret}} = 2 d(L) - v_S.$$
     Why? Check the algebraic telescoping: if a future demand $v'_{D}$ matches with $v_S^{\text{regret}}$ at an ancestor $L'$, the new cost added is $v_S^{\text{regret}} + v'_D - 2 d(L') = (2 d(L) - v_D) + v'_D - 2 d(L')$. Adding the previous $\Delta = v_S + v_D - 2 d(L)$ yields:
     $$\Delta + (2 d(L) - v_D + v'_D - 2 d(L')) = v_S + v'_D - 2 d(L'),$$
     the exact distance between the original supply $u$ and the new demand $v'$ through their true LCA $L'$!

---

### 4. Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Concrete Toy Trace: 1D Mice & Holes (`Model 42.2`)
Consider 2 mice at $x_1 = 2, x_2 = 5$ and 2 unit-capacity holes at $y_1 = 0$ ($w_1 = 0$), $y_2 = 6$ ($w_2 = 0$):
1. **Hole 1 at $y_1 = 0$**: Push $v_H = -0 + 0 = 0$ into $Q_H$. (`total_cost = 0`).
2. **Mouse 1 at $x_1 = 2$**: Matches with $v_H = 0 \in Q_H$. Cost $\Delta_1 = 2 + 0 = 2$ (`total_cost = 2`). Push mouse regret token $v_M = -2(2) - 0 = -4$ into $Q_M$.
3. **Mouse 2 at $x_2 = 5$**: $Q_H$ is empty (or contains virtual hole at $+\infty$, say $v_H = +1000$). Matches with $+1000$: $\Delta_2 = 5 + 1000 = 1005$ (`total_cost = 1007`). Push $v_M = -2(5) - 1000 = -1010$ into $Q_M$.
4. **Hole 2 at $y_2 = 6$ ($c_2 = 1$)**:
   - $Q_M$ has top $v_M = -1010$ (from Mouse 2), with $v_M = -4$ (from Mouse 1) below it.
   - Match Hole 2 with $v_M = -1010$: $\Delta_3 = 6 + (-1010) = -1004 < 0$ (`total_cost = 1007 - 1004 = 3`).
   - True optimal matching: Mouse 1 ($2$) $\to$ Hole 1 ($0$, cost $2$) and Mouse 2 ($5$) $\to$ Hole 2 ($6$, cost $1$), total cost $2 + 1 = 3$.
   - What if Mouse 2 wasn't there, and only Mouse 1 ($x_1 = 4$) was between $y_1 = 0$ and $y_2 = 5$? At $x_1 = 4$, $\Delta_1 = 4$, $v_M = -2(4) - 0 = -8$. At $y_2 = 5$, $\Delta_2 = 5 + (-8) = -3 < 0$, updating `total_cost = 4 - 3 = 1 = |5 - 4|`!

#### Three Fatal Broken Gadget Counterexamples

> [!WARNING]
> **Broken Gadget 1: Using `-x` Instead of `-2x - v_H` for the Mouse Regret Key**
> A common beginner bug is pushing $-x$ into $Q_M$ when Mouse $x$ matches with Hole $y$ ($v_H = -y$). That only subtracts $x$ for the *new* rightward segment $y' - x$, completely forgetting to refund the cost $\Delta = x - y$ already paid for the leftward segment $[y, x]$! The factor of $-2x$ comes from $-x$ (start of new rightward path) minus $+x$ (refund of old leftward path).
>
> **Broken Gadget 2: Omitting the Re-Steal Token $v_M^{\text{re-steal}} = -y - w$ in Multi-Capacity Holes (`UOJ #455`)**
> When Hole $y$ matches with $k$ mice from $Q_M$, if you only push $v_H^{\text{regret}} = -2y - v_M$ into $Q_H$ and forget to push $v_M^{\text{re-steal}} = -y - w$ into $Q_M$, then a future hole $y'' > y$ with a much cheaper entry fee $w'' \ll w$ cannot steal the mice currently assigned to Hole $y$!
>
> **Broken Gadget 3: Choosing Mandatory Penalty $M$ Too Small in Tree MCMF (`Conquer the World`)**
> Each mandatory demand carries $-M$. If $M \le \max_{u,v} \text{dist}(u, v)$, then the algorithm may prefer leaving two distant vertices unmatched rather than paying $\text{dist}(u, v) > M$. Conversely, if $K \cdot M > 2^{63}-1$, `int64_t` overflows! Always set $M > \sum w_e$ and use `__int128_t` for the accumulated cost before adding back $K_{\text{total}} \cdot M$.

---

## Iteration 43: Simulated Min-Cost Flow II (`模拟费用流` II) — Segment Tree Residual Maintenance & Multi-Queue Coupled Bipartite Simulation

### 1. Step 1: The Non-Graph Diagnostic Signal (Recognition)

When does a Simulated Min-Cost Flow problem go beyond simple 1D/Tree mergeable heaps and require **Dynamic Segment Tree Residual Maintenance** (`线段树维护增广路`) or **Multi-Queue Coupled State Machines** (`多堆状态自动机`)?

- **Diagnostic Signal A — $k$ Augmentations on a 1D Timeline with Forward/Reverse Bottlenecks (`CF 802 O`, `CF 280 D`)**:
  - You must select $k$ pairs $(i_r \le j_r)$ (or $k$ disjoint subarrays $[l_r, r_r]$) on an array of length $N \le 5 \cdot 10^5$ (with either small $k \le 20$ or arbitrary $k \le N$ combined with WQS binary search / direct $K$-step augmentation for $K \le 5 \cdot 10^4$).
  - Unlike `CF 865 D` (where we sweep $j = 1 \dots N$ once and take *all* profitable pairs), here we must find the **global shortest $S \to T$ augmenting path across the entire array $[1, N]$ at each step**, and each augmentation increments or decrements the residual flow $f_t$ along the interval $[i^*, j^* - 1]$.
- **Diagnostic Signal B — Coupled Bipartite Selection with Global Cardinality / Overlap Bounds (`[NOI2019] 序列`, `AGC 018 C`)**:
  - You have $N \le 2 \cdot 10^5$ items, each possessing $2$ or $3$ attributes $(a_i, b_i)$ or $(a_i, b_i, c_i)$, and must pick $K$ items of each type subject to a global coupling constraint such as *"at least $L$ indices are chosen in both $A$ and $B$"*.
  - The MCMF network has $N$ parallel item gadgets connected through **$O(1)$ shared global bottleneck hubs**.

---

### 2. Archetype 43.1: Dynamic Segment Tree Residual Augmentation (`CF 802 O` & `CF 280 D`)

#### Step 2: Algebraic & Residual Network Formulation (`CF 802 O — April Fools' Problem (hard)`)
We have $N$ days. Preparing a problem on day $i$ costs $a_i$ (at most 1 per day); printing it on day $j \ge i$ costs $b_j$ (at most 1 per day). We must prepare and print $k$ problems at minimum total cost.

In the explicit MCMF network:
- Source $S \to i$ with $\text{cap} = 1, \text{cost} = a_i$.
- Timeline edges $t \to t+1$ ($1 \le t < N$) with $\text{cap} = \infty, \text{cost} = 0$. Let $f_t \ge 0$ denote the current flow on $(t \to t+1)$.
- Sink edges $j \to T$ with $\text{cap} = 1, \text{cost} = b_j$.

When we push $1$ unit of flow from $S$ to $T$ along the shortest augmenting path $(S \to i^* \leadsto j^* \to T)$, there are exactly **two topological types of paths**:

1. **Forward Path ($i^* \le j^*$)**:
   Flow enters at $i^*$, travels right along $i^* \to i^* + 1 \to \dots \to j^*$, and exits at $j^*$.
   - *Feasibility*: Because forward edges $(t \to t+1)$ have capacity $\infty$, a forward path $i^* \le j^*$ is **always legal** for any unused $i^*$ and unused $j^* \ge i^*$.
   - *Residual Update*: For all $t \in [i^*, j^* - 1]$, $f_t \gets f_t + 1$. Since $S \to i^*$ and $j^* \to T$ are now saturated, we set $a_{i^*} \gets +\infty$ and $b_{j^*} \gets +\infty$.

2. **Reverse Path ($j^* < i^*$)**:
   Flow enters at $i^*$, travels **left** along reverse residual edges $i^* \to i^* - 1 \to \dots \to j^*$, and exits at $j^*$.
   - *Feasibility*: In the residual network $G_f$, the reverse edge $(t+1 \to t)$ has positive residual capacity **if and only if $f_t > 0$**! Therefore, a reverse path from $i^*$ down to $j^*$ ($j^* < i^*$) is legal **if and only if**:
     $$\min_{t \in [j^*, i^* - 1]} f_t > 0.$$
   - *Residual Update*: For all $t \in [j^*, i^* - 1]$, pushing $1$ unit along the reverse edge decrements the forward flow: $f_t \gets f_t - 1$. And $a_{i^*} \gets +\infty, b_{j^*} \gets +\infty$.

#### Step 3: Reverse-Engineering the Segment Tree State (`pushup` Invariant)
How can a Segment Tree over $[1, N]$ find the minimum of $a_i + b_j$ across both valid forward pairs ($i \le j$) and valid reverse pairs ($j < i$ with $\min_{t \in [j, i-1]} f_t > 0$) in $O(1)$ at the root, while supporting range addition $f_t \gets f_t \pm 1$ in $O(\log N)$?

The trick is **Minimal-Flow Splitting**:
- Because $f_t \ge 0$ always holds, a range $[j, i-1]$ contains a zero ($f_t = 0$) if and only if it contains a **global minimum of $f$** when that minimum is $0$.
- More generally, inside any segment tree node $p$ covering $[L, R]$, let $m_p = \min_{t \in [L, R]} f_t$ be the minimum flow on edges in $[L, R]$.
- Suppose we require that any reverse pair $(j < i)$ inside $[L, R]$ must **never cross an edge $t \in [j, i-1]$ where $f_t = m_p$** (unless $m_p > 0$, in which case no edge in $[L, R]$ has $f_t = 0$!).
- Wait: at the root $[1, N]$, if we pad a dummy edge $f_N = 0$ (or simply note that whenever any $f_t = 0$ exists in $[L, R]$, the minimum $m_p$ *is* $0$), forbidding $(j, i)$ from crossing any edge with $f_t = m_p$ inside a node where $m_p = 0$ is **100% equivalent to $\min_{t \in [j, i-1]} f_t > 0$**!
- Even better, we don't even need to check whether $m_p = 0$ inside `pushup(p)`:
  For every node $p$ covering $[L, R]$ with children `lc` and `rc`:
  1. `min_f[p] = min(min_f[lc], min_f[rc])` (the minimum flow value on $[L, R]$).
  2. `min_a[p]` and `min_b[p]`: the minimum $a_i$ and minimum $b_j$ in $[L, R]$.
  3. `best_fwd[p]`: minimum $a_i + b_j$ with $L \le i \le j \le R$:
     $$\text{best\_fwd}[p] = \min\Big(\text{best\_fwd}[\text{lc}],\; \text{best\_fwd}[\text{rc}],\; \text{min\_a}[\text{lc}] + \text{min\_b}[\text{rc}]\Big).$$
  4. To maintain reverse pairs $L \le j < i \le R$ that never cross an edge $t$ with $f_t = \text{min\_f}[p]$, we maintain three auxiliary values on every node $p$:
     - `best_rev[p]`: best $a_i + b_j$ ($L \le j < i \le R$) not crossing any edge with $f_t = \text{min\_f}[p]$.
     - `min_a_R[p]`: minimum $a_i$ ($i \in [L, R]$) located **to the right of all edges $t \in [L, R]$ having $f_t = \text{min\_f}[p]$**.
     - `min_b_L[p]`: minimum $b_j$ ($j \in [L, R]$) located **to the left of all edges $t \in [L, R]$ having $f_t = \text{min\_f}[p]$**.
  5. Now see how cleanly `pushup(p)` merges `lc` and `rc` across the three cases for $\text{min\_f}[\text{lc}]$ vs. $\text{min\_f}[\text{rc}]$:
     - **Case 1 ($\text{min\_f}[\text{lc}] < \text{min\_f}[\text{rc}]$)**: The minimum $\text{min\_f}[p]$ occurs **only in `lc`**. Thus inside `rc`, *no* edge has $f_t = \text{min\_f}[p]$!
       - `min_b_L[p] = min_b_L[lc]`
       - `min_a_R[p] = min(min_a_R[lc], min_a[rc])`
       - `best_rev[p] = min({ best_rev[lc], best_full_rev[rc], min_b_L[lc] + min_a[rc] })` (wait: any reverse pair inside `rc` is unrestricted because $\text{min\_f}[\text{rc}] > \text{min\_f}[p]$! Wait: what if `best_rev[rc]` was restricted by $\text{min\_f}[\text{rc}] > 0$? That's why we decompose by the canonical intervals where $\text{min\_f} > 0$, or even simpler: in `CF 280 D` / `CF 802 O`, we store at each node the unconstrained `best_rev_any[p]` = $\min_{j < i} (b_j + a_i)$ when $\text{min\_f}[p] > 0$!).
       Let us state the **Exact 2-Line Canonical Decomposition** used in `CF 802 O`:
       Actually, at the root $[1, N]$, the edges with $f_t = 0$ partition $[1, N]$ into maximal contiguous blocks where $f_t > 0$. Inside each block, *every* $j < i$ is valid! Across two different blocks separated by an edge $f_t = 0$, *no* $j < i$ is valid!
       Because $f_t \ge 0$ everywhere, any node $p$ has $\text{min\_f}[p] \ge 0$:
       - If $\text{min\_f}[\text{lc}] == \text{min\_f}[\text{rc}]$, both children contain the minimum:
         - `min_b_L[p] = min_b_L[lc]`, `min_a_R[p] = min_a_R[rc]`,
         - `best_rev[p] = min({ best_rev[lc], best_rev[rc], min_b_L[rc] + min_a_R[lc] })`! (Notice that a pair between the right of the last minimum in `lc` and the left of the first minimum in `rc` crosses **zero** minimums!).
       - If $\text{min\_f}[\text{lc}] < \text{min\_f}[\text{rc}]$, `rc` has **no** minimums of $p$, so the entire `rc` lies to the right of the last minimum in `lc`! Thus:
         - `min_b_L[p] = min_b_L[lc]`,
         - `min_a_R[p] = min(min_a_R[lc], min_a[rc])`,
         - `best_rev[p] = min({ best_rev[lc], best_rev_all[rc], min_b[rc] + min_a_R[lc] })`, where `best_rev_all[rc]` is simply $\min_{L \le j < i \le R} (b_j + a_i)$!
       - Symmetrically if $\text{min\_f}[\text{lc}] > \text{min\_f}[\text{rc}]$, `lc` has no minimums of $p$!
       By putting a sentinel $f_N = 0$ at the right end of `[1, N]`, $\text{min\_f}[\text{root}]$ is **guaranteed to equal $0$**, so `best_rev[root]` is 100% exact at all times!

---

### 3. Archetype 43.2: Multi-Queue Coupled Bipartite Simulation (`[NOI2019] 序列` / `Luogu P5470`)

#### Step 1: Non-Graph Diagnostic Signal
We are given two arrays $a_1, \dots, a_N$ and $b_1, \dots, b_N$ ($N \le 2 \cdot 10^5$, $a_i, b_i \ge 1$). We must choose a subset $I \subseteq \{1, \dots, N\}$ of size $|I| = K$ and a subset $J \subseteq \{1, \dots, N\}$ of size $|J| = K$ such that $|I \cap J| \ge L$, maximizing $\sum_{i \in I} a_i + \sum_{j \in J} b_j$.
- Why DP/Greedy fails: Choosing $a_i$ and $b_j$ ($i \neq j$) consumes $1$ unit of the $(K - L)$ "free mismatch budget", whereas choosing $a_i$ and $b_i$ (same index) consumes $0$ units, and choosing $a_i$ when $b_i$ was *already* chosen as a mismatch actually **refunds 1 unit of the mismatch budget**!
- Because $N \le 2 \cdot 10^5$, explicit MCMF is too slow, so we compile the MCMF residual graph into a Multi-Heap State Machine.

#### Step 2: Intermediate Algebraic & Exact MCMF Network
Rewriting $|I| = K, |J| = K, |I \cap J| \ge L$: the number of indices $i \in I \setminus J$ is at most $K - L$.
Construct the exact Max-Cost Flow network to send $K$ units of flow from $S$ to $T$:
- For each $i \in \{1, \dots, N\}$:
  - $S \to u_i$ with $\text{cap} = 1, \text{cost} = a_i$.
  - $v_i \to T$ with $\text{cap} = 1, \text{cost} = b_i$.
  - **Coupled Same-Index Edge**: $u_i \to v_i$ with $\text{cap} = 1, \text{cost} = 0$.
- **Free Mismatch Hub Edge ($P \to Q$)**:
  - Two global hub vertices $P$ and $Q$ connected by a single bridge edge $P \to Q$ with $\text{cap} = K - L$ and $\text{cost} = 0$.
  - For every $i$: $u_i \to P$ ($\text{cap} = 1, \text{cost} = 0$) and $Q \to v_i$ ($\text{cap} = 1, \text{cost} = 0$).

```
                 +---(cap=1, cost=0)---> v_i ---(cap=1, cost=b_i)---+
                /                         ^                          \
S --(1, a_i)-> u_i                        | (1, 0)                    v
                \                         |                           T
                 +---(1, 0)--> [ P ] --(K-L, 0)--> [ Q ]
```

 Verify that this network is 100% equivalent to the problem:
- Any unit of flow routed directly along $u_i \to v_i$ selects both $a_i$ and $b_i$ ($i \in I \cap J$).
- Any unit of flow routed through $u_i \to P \to Q \to v_j$ selects $a_i$ and $b_j$ separately, consuming $1$ unit of capacity on $P \to Q$. Since $\text{cap}(P \to Q) = K - L$, at least $K - (K - L) = L$ units of flow must use the direct edges $u_i \to v_i$!

#### Step 3: Reverse-Engineering the 5 Residual Augmenting Paths & 5 Priority Queues
Let `free_cap` denote the remaining residual capacity on the bridge edge $P \to Q$ (initially `free_cap = K - L`).
At any moment, each index $i \in \{1, \dots, N\}$ is in one of four selection states $(x_i, y_i) \in \{0, 1\}^2$:
- State `00`: neither $a_i$ nor $b_i$ is selected.
- State `10`: $a_i$ is selected ($S \to u_i \to P$ saturated), $b_i$ is not ($v_i \to T$ empty).
- State `01`: $b_i$ is selected ($Q \to v_i \to T$ saturated), $a_i$ is not ($S \to u_i$ empty).
- State `11`: both $a_i$ and $b_i$ are selected (we may always assume flow goes via $u_i \to v_i$).

Maintain **5 Max-Heaps** (with lazy deletion checking `state[i]` on pop):
1. $H_{a0}$: indices in State `00`, keyed by $a_i$.
2. $H_{b0}$: indices in State `00`, keyed by $b_i$.
3. $H_{ab}$: indices in State `00`, keyed by $a_i + b_i$.
4. $H_{a1}$: indices in State `01` ($b_i$ already chosen!), keyed by $a_i$.
5. $H_{b1}$: indices in State `10` ($a_i$ already chosen!), keyed by $b_i$.

Now let us list **every possible simple $S \to T$ augmenting path** in the residual network of our gadget at each of the $K$ augmentations:

| Path ID | Residual Path in $G_f$ | State Transitions | Effect on `free_cap` ($P \to Q$) | Net Gain |
| :--- | :--- | :--- | :--- | :--- |
| **Cand 1** | $S \to u_i \to P \to Q \to v_j \to T$<br>*(Requires `free_cap > 0`)* | $i: \text{00} \to \text{10}$<br>$j: \text{00} \to \text{01}$<br>*(if $i=j$, $i: \text{00} \to \text{11}$, `free_cap` unchanged)* | `free_cap -= 1` | $H_{a0}.\text{top}() + H_{b0}.\text{top}()$ |
| **Cand 2** | $S \to u_i \to v_i \to T$ | $i: \text{00} \to \text{11}$ | `0` (uses $u_i \to v_i$) | $H_{ab}.\text{top}()$ |
| **Cand 3** | $S \to u_i \to v_i \gets Q \to v_j \to T$<br>*(Since $i \in \text{01}$, edge $Q \to v_i$ is full, so $v_i \to Q$ is open!)* | $i: \text{01} \to \text{11}$<br>$j: \text{00} \to \text{01}$ | `0` ($v_i \to Q \to v_j$ bypasses $P \to Q$!) | $H_{a1}.\text{top}() + H_{b0}.\text{top}()$ |
| **Cand 4** | $S \to u_i \to P \gets u_j \to v_j \to T$<br>*(Since $j \in \text{10}$, edge $u_j \to P$ is full, so $P \to u_j$ is open!)* | $i: \text{00} \to \text{10}$<br>$j: \text{10} \to \text{11}$ | `0` ($u_i \to P \to u_j$ bypasses $P \to Q$!) | $H_{a0}.\text{top}() + H_{b1}.\text{top}()$ |
| **Cand 5** | $S \to u_i \to v_i \gets Q \gets P \gets u_j \to v_j \to T$<br>*(Uses reverse edge $Q \to P$, **refunding** 1 unit of `free_cap`!)* | $i: \text{01} \to \text{11}$<br>$j: \text{10} \to \text{11}$ | `free_cap += 1`! | $H_{a1}.\text{top}() + H_{b1}.\text{top}()$ |

> [!TIP]
> **Look at Candidate 5 (`free_cap += 1`)!**
> Without the residual graph derivation, who would ever guess that you need a transition picking $a_i$ from State `01` ($H_{a1}$) and $b_j$ from State `10` ($H_{b1}$) that **increases** the remaining mismatch budget `free_cap` by $1$? Yet in the residual network, it is simply the path $S \to u_i \to v_i \to Q \to P \to u_j \to v_j \to T$ pushing 1 unit of flow **backwards** across $P \to Q$!
> At each of the $K$ iterations, we simply evaluate the 5 candidates (enabling Cand 1 only when `free_cap > 0`), pick the maximum-gain candidate, update the states of the 1 or 2 affected indices, and push their new states into the corresponding heaps. Total time: $O((N + K) \log N)$!

---

### 4. Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples (`[NOI2019] 序列`)

#### Concrete Toy Trace showing Why Candidate 5 (`free_cap += 1`) Is Mandatory
Let $N = 3, K = 2, L = 1$ (so `free_cap = K - L = 1`):
- Index 1: $a_1 = 10, b_1 = 9$ ($a_1 + b_1 = 19$)
- Index 2: $a_2 = 1, b_2 = 10$ ($a_2 + b_2 = 11$)
- Index 3: $a_3 = 9, b_3 = 1$ ($a_3 + b_3 = 10$)

Trace the $K = 2$ augmentations:
- **Step 1 (`free_cap = 1`)**:
  - Cand 1 ($H_{a0} + H_{b0}$): pick $a_1 = 10$ and $b_2 = 10 \implies$ gain $20$. Since $1 \neq 2$, `free_cap` drops to $0$. Now `state[1] = 10` (pushed to $H_{b1}$ with $b_1 = 9$), `state[2] = 01` (pushed to $H_{a1}$ with $a_2 = 1$).
- **Step 2 (`free_cap = 0`, so Cand 1 is disabled)**:
  - Cand 2 ($H_{ab}$): only index 3 is in `00`, giving $a_3 + b_3 = 10$.
  - Cand 3 ($H_{a1} + H_{b0}$): $a_2 + b_3 = 1 + 1 = 2$.
  - Cand 4 ($H_{a0} + H_{b1}$): $a_3 + b_1 = 9 + 9 = 18$!
  - Cand 5 ($H_{a1} + H_{b1}$): $a_2 + b_1 = 1 + 9 = 10$.
  - Here Cand 4 wins with gain $18$ (`total = 20 + 18 = 38`), transitioning $1: \text{10} \to \text{11}$ and $3: \text{00} \to \text{10}$, choosing $I = \{1, 3\}, J = \{1, 2\}$ ($|I \cap J| = |\{1\}| = 1 \ge L$).
- **Now suppose $K = 3, L = 2$ (still `free_cap = 1`) and we add Index 4 with $a_4 = 8, b_4 = 8$, while modifying $a_2 = 9, b_1 = 9$**:
  If Step 1 uses `free_cap` on $(a_1, b_2)$, and Step 2 uses Cand 5 ($a_2 \in H_{a1}$ and $b_1 \in H_{b1}$), both Index 1 and Index 2 become `11` (coupled!), **refunding `free_cap` from $0$ back to $1$**, which allows Step 3 to make a new uncoupled choice $(a_3, b_4)$!

> [!WARNING]
> **Broken Gadget Counterexample: Omitting Candidate 3, 4, or 5 in `[NOI2019] 序列`**
> Many contestants try a greedy algorithm that first picks $K - L$ independent pairs $(a_i, b_j)$ and then picks $L$ coupled pairs. That fails completely on the trace above because $a_1 = 10$ and $b_2 = 10$ are initially chosen as the $(K - L)$ mismatch, and later $b_1 = 9$ must pair with $a_1$ to turn Index 1 into a *coupled* pair while handing the mismatch token over to $a_3 = 9$ and $b_2 = 10$! Only the complete 5-path residual transition set guarantees exact MCMF optimality.

---

## Iteration 44: General Non-Bipartite Graph Matching I — Edmonds' Blossom Algorithm (`带花树`), Tutte–Berge Formula & Gallai–Edmonds Decomposition

### 1. Step 1: The Non-Graph Diagnostic Signal (Recognition)

How do you recognize a General Non-Bipartite Graph Matching problem?

- **Constraint Signature**: $V \le 500$ (or up to $V \le 1000$), $E \le V^2 / 2$.
- **Structural Clues in the Statement**:
  1. You must pair elements into disjoint 2-element sets (or assign capacity-2 bins, dominoes on non-bipartite surfaces, or 2-player walk games on arbitrary undirected graphs).
  2. The compatibility relation is **symmetric** (undirected edges) and **contains odd cycles**: e.g., three items $A, B, C$ can all pairwise match with each other ($K_3$ triangle), so no 2-coloring exists.
- **Why Bipartite Algorithms & Standard Max-Flow Fail**:
  - Converting an undirected graph into a directed flow network $S \to V_{\text{left}} \to V_{\text{right}} \to T$ on a non-bipartite graph allows **half-integral 2-cycles** (e.g., on a triangle $1 - 2 - 3 - 1$, sending $0.5$ flow along $1 \to 2, 2 \to 3, 3 \to 1$ gives flow $3$, corresponding to a fractional matching of size $1.5$, whereas the maximum integral matching on a triangle has size $1$!).
  - Standard Bipartite Alternating BFS fails because an odd cycle allows an alternating walk from the unmatched root $r$ to enter a vertex $v$ at **both even distance and odd distance**, causing the BFS to either miss an augmenting path (if $v$ is visited only once in the wrong parity) or report a self-intersecting walk that uses a vertex twice!

---

### 2. Step 2: Intermediate Structural Representation — Alternating Trees, Blossoms & The Tutte–Berge Duality

Let $G = (V, E)$ be an undirected graph and $M \subseteq E$ be a matching.
- A vertex $v$ is **exposed (unmatched)** if no edge of $M$ is incident to $v$.
- An **$M$-alternating path** is a simple path whose edges alternate between $E \setminus M$ and $M$.
- An **$M$-augmenting path** is an $M$-alternating path between two distinct exposed vertices. By Berge's Theorem (1957), $M$ is a maximum matching if and only if $G$ contains no $M$-augmenting path.

#### Definition 44.1 (Blossom / `花`)
Suppose we grow an alternating tree $T$ rooted at an exposed vertex $r$, labeling vertices at even distance from $r$ (reached via $M$) as **Outer (`Type 1` / $S$-vertices)** and vertices at odd distance from $r$ (reached via $E \setminus M$) as **Inner (`Type 2` / $T$-vertices)**.
If we scan an unmatched edge $e = (u, v) \in E \setminus M$ where **both $u$ and $v$ are Outer (`Type 1`) vertices** in the same alternating tree, let $b = \text{lca}_T(u, v)$ be their lowest common ancestor in $T$.
- Because $u$ and $v$ are both at even distance from $r$, their LCA $b$ is also an **Outer (`Type 1`)** vertex!
- The unique tree paths $b \leadsto u$ and $b \leadsto v$ plus the edge $(u, v)$ form an **odd cycle $B$ of length $2k + 1$ containing $k$ matched edges**, such that $b$ (the **base / `花托`** of the blossom) is the only vertex of $B$ not matched within $B$ (it is either exposed if $b = r$, or matched to its parent $p(b) \notin B$ via the **stem** $r \leadsto b$).

```
                        r (Exposed Root, Type 1)
                        |  (unmatched)
                        o  (Type 2)
                        || (matched)
                        b  (Blossom Base, Type 1)
                       / \ (unmatched)
             (Type 2) o   o (Type 2)
             (matched)|| || (matched)
             (Type 1) u---v (Type 1)  <-- Cross edge (u, v) closes odd cycle B!
```

#### Theorem 44.2 (Edmonds' Blossom Contraction Theorem, 1965)
Let $B$ be a blossom in $G$ with base $b$ reached via an even-length alternating stem from an exposed root $r$. Let $G / B$ be the graph obtained by contracting all vertices of $B$ into a single outer vertex $v_B$, and let $M / B = M \setminus E(B)$ be the induced matching in $G / B$. Then:
$$\text{$G$ contains an $M$-augmenting path} \iff \text{$G / B$ contains an $(M / B)$-augmenting path.}$$

*Proof (Both Directions)*:
By modifying $M$ along the even stem $r \leadsto b$ ($M' = M \oplus E(r \leadsto b)$, which preserves the size $|M'| = |M|$ and preserves the existence of augmenting paths), we reduce to the case where the base $b$ is itself an **exposed vertex** ($b = r$).
1. **($\Longleftarrow$ Lifting an Augmenting Path from $G / B$ to $G$)**:
   Suppose $P'$ is an $(M / B)$-augmenting path in $G / B$. If $P'$ does not visit $v_B$, then $P'$ is already an $M$-augmenting path in $G$.
   If $P'$ visits $v_B$, since $v_B$ is exposed in $G / B$, $v_B$ must be one of the endpoints of $P'$! Let $P'$ start at $v_B$ and leave $v_B$ via an unmatched edge $(w, x)$ where $w \in B$ and $x \notin B$.
   Because $B$ is an odd cycle of length $2k+1$ whose edges alternate around $B$ except at the base $b$ (where both incident cycle edges are unmatched), for **every** vertex $w \in B$, one of the two cycle arcs between $b$ and $w$ has **even length** (ending at $w$ with a matched edge) and the other has **odd length** (ending at $w$ with an unmatched edge).
   Take the **even-length alternating arc** $P_B(b \leadsto w)$ inside $B$ and concatenate it with $(w, x)$ and the rest of $P'$. Because $P_B(b \leadsto w)$ arrives at $w$ via a matched edge of $B$ and exits $w$ via the unmatched edge $(w, x) \notin B$, the combined path $P = P_B(b \leadsto w) \circ (w, x) \circ P'_{x \leadsto r'}$ is a valid simple $M$-augmenting path in $G$!
2. **($\implies$ Projecting an Augmenting Path from $G$ to $G / B$)**:
   Suppose $P$ is an $M$-augmenting path in $G$ between two exposed vertices $r_1, r_2$. Since $b$ is exposed in $G$, if neither endpoint is $b$, let $u \in B$ be the first vertex of $P$ that enters $B$ (say from $r_1$). Then the prefix $r_1 \leadsto u$ projects to an alternating path from $r_1$ to the exposed vertex $v_B$ in $G / B$—which is an $(M / B)$-augmenting path! If $r_1 = b$, let $w \in B$ be the *last* vertex of $P$ in $B$; then the suffix of $P$ after $w$ combined with $v_B$ forms an $(M / B)$-augmenting path from $v_B$ to $r_2$. $\blacksquare$

---

### 3. Step 3: Reverse-Engineering Scratchpad — DSU Lazy Blossom Contraction & The Tutte–Berge / Gallai–Edmonds Duals

#### 1. How $O(V E \alpha(V))$ DSU Blossom Contraction Works Without Copying Graphs
Instead of physically contracting $G$ into $G / B$, we run a single BFS from each unmatched vertex $r$, maintaining:
- `match[u]`: current matched partner of $u$ ($0$ if unmatched).
- `pre[u]`: the predecessor of an Inner (`Type 2`) vertex $u$ along the unmatched tree edge that discovered $u$ (or the cross-bridge of a blossom!).
- `tp[u]`: `0` = unvisited, `1` = Outer ($S$-vertex), `2` = Inner ($T$-vertex).
- `dsu[u]`: Disjoint Set Union representative of the highest contracted blossom containing $u$ (always pointing to the **base** $b$ of that blossom!).

When scanning edges from an Outer vertex $u$ (`tp[u] == 1`) in the BFS queue:
- **Case 1 (`tp[v] == 0` — Unvisited Vertex)**:
  - Set `pre[v] = u`, `tp[v] = 2`.
  - If `match[v] == 0`, we found an augmenting path! Walk backwards from $v$ to $r$ flipping `match[v] = u, match[u] = v` via the helper `aug(v)`:
    ```cpp
    for (int cur = v, nxt; cur; cur = nxt) {
        int p = pre[cur];
        nxt = match[p];
        match[cur] = p;
        match[p] = cur;
    }
    ```
  - Otherwise, set `tp[match[v]] = 1` and push `match[v]` into the BFS queue.
- **Case 2 (`tp[v] == 1` and `find(u) != find(v)` — Blossom Detected!)**:
  - Find the blossom base $b = \text{lca}(u, v)$ by alternatingly climbing `u = find(pre[match[u]])` and `v = find(pre[match[v]])` (marking visited DSU roots with a timestamp `dfn[u] = ++timer` in $O(|B|)$ steps).
  - Call `contract(u, v, b)` and `contract(v, u, b)` to contract both sides of the cycle up to $b$:
    ```cpp
    void contract(int x, int y, int b) {
        for (int i = find(x); i != b; i = find(pre[y])) {
            pre[x] = y; // Bridge link so aug() can walk the other way around B!
            y = match[i];
            if (tp[y] == 2) { tp[y] = 1; q.push(y); } // Inner -> Outer!
            dsu[find(i)] = b;
            dsu[find(y)] = b;
            x = pre[y];
        }
    }
    ```
  - Look at the line `pre[x] = y;`: why does that one pointer assignment magically allow `aug()` to traverse the even-length arc of $B$ without recursive lifting?
    Because inside the blossom $B$, `y = match[i]` was originally an **Inner (`Type 2`)** vertex (entered via `pre[y]` from $b$'s side and exiting via `match[i] = y` toward $x$). When $y$ is flipped to an **Outer (`Type 1`)** vertex and a future augmenting path leaves $y$ via an unmatched edge, the path must reach $y$ from $b$ via the **other arc** of $B$ (entering $x$ from $v$, then walking *down* the old tree edges from $x$ to $y$!). Setting `pre[x] = y` links the two sides of the bridge $(u, v)$ and reverses the `pre` pointers along the cycle so the standard `aug()` loop walks right around the blossom!

#### 2. The Tutte–Berge Formula & Gallai–Edmonds Decomposition
Suppose we initialize the BFS by setting **every exposed vertex $r \in V$ to `tp[r] = 1`** simultaneously and growing the maximum alternating forest until no further edges or blossoms can be added. Let us partition $V$ according to the final vertex types:
- **$D(G)$ (Outer / `Type 1` Vertices)**: All vertices with `tp[v] == 1` (including all vertices inside contracted blossoms!).
  - *Property*: Every vertex $v \in D(G)$ can reach an exposed root via an even-length alternating path, so flipping that path yields a maximum matching **missing $v$**! Thus $D(G)$ is the exact set of **non-essential vertices** (vertices missed by at least one maximum matching).
- **$A(G)$ (Inner / `Type 2` Vertices)**: All vertices with `tp[v] == 2`, which form the exact neighborhood $N(D(G)) \setminus D(G)$.
- **$C(G)$ (Unvisited / `Type 0` Vertices)**: All vertices with `tp[v] == 0`.

Look at the connected components of $G \setminus A(G)$:
1. Every component inside $C(G)$ is **perfectly matched** internally (size $2k$, even).
2. Every component inside $D(G)$ is a single contracted blossom (or singleton outer vertex) of **odd size $2k+1$**, which has $k$ internal matched edges and at most $1$ matched edge connecting its base to $A(G)$!
3. Every vertex in $A(G)$ is matched to the base of a distinct odd component of $D(G)$.
Therefore, the number of unmatched vertices in $G$ is $\text{odd}(G \setminus A(G)) - |A(G)|$, which proves both the **Tutte–Berge Formula** and the **Gallai–Edmonds Structure Theorem**:

$$\nu(G) = \frac{1}{2} \min_{U \subseteq V} \Big(|V| + |U| - \text{odd}(G \setminus U)\Big),$$

where $\text{odd}(G \setminus U)$ is the number of connected components of $G \setminus U$ having an odd number of vertices, and the minimum is achieved at $U = A(G)$!

> [!IMPORTANT]
> **Application to 2-Player Non-Bipartite Walk Games**:
> A token starts at vertex $s \in V$ of a general undirected graph $G$. Two players alternately move the token to an adjacent unvisited vertex; the last player to move wins.
> **Theorem**: The first player (Alice) has a winning strategy from starting vertex $s$ **if and only if $s$ belongs to EVERY maximum matching of $G$** — i.e., $s \notin D(G)$!
> *Fast Check in $O(VE)$*: Either run Edmonds' Blossom to find one maximum matching $M$, and then run a single alternating BFS starting simultaneously from all $M$-exposed vertices; the set of reached `Type 1` vertices is $D(G)$! Alice wins from $s \iff \text{tp}[s] \neq 1$.

---

### 4. Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Concrete Toy Trace: Augmenting Through a 5-Cycle Blossom
Consider a 6-vertex graph with path $1 - 2$ and pentagon $2 - 3 - 4 - 5 - 6 - 2$, plus edge $4 - 7$, where current matching is $M = \{(2, 3), (4, 5)\}$ (vertices $1, 6, 7$ are exposed; $|M| = 2$):
1. Start BFS from exposed root $1$ (`tp[1] = 1`):
   - Scan $(1, 2)$: `tp[2] = 2, pre[2] = 1`, `tp[3] = 1` (since `match[2] = 3`).
   - Scan $(3, 4)$: `tp[4] = 2, pre[4] = 3`, `tp[5] = 1` (since `match[4] = 5`).
   - Notice: vertex $4$ is currently **Inner (`tp[4] = 2`)**, so we **do NOT scan unmatched edges out of $4$**! Thus the edge $(4, 7)$ to exposed vertex $7$ cannot be used yet because $1 - 2 = 3 - 4 - 7$ has two consecutive unmatched edges $(3, 4)$ and $(4, 7)$!
2. Continue along the pentagon from $1 \to 2$ or $5$:
   - Suppose $6$ was instead matched to $8$ (`match[6] = 8`) so $2 - 3 - 4 - 5 - 2$ is a 3-cycle $2 - 3 - 4 - 2$ with $M = \{(2, 3)\}$ and edge $(3, 4)$ and $(4, 2)$, and exposed $7$ connected to $2$? Even simpler: in our pentagon $2 - 3 - 4 - 5 - 6 - 2$ with $M = \{(2, 3), (5, 6)\}$ (exposed $1, 4$? No, let $M = \{(2, 3), (4, 5)\}$ and add edge $(5, 2)$ so $2 - 3 - 4 - 5 - 2$ has even length, or edge $(5, 3)$ so $3 - 4 - 5 - 3$ is a triangle!).
   - With triangle $3 - 4 - 5 - 3$: `tp[3] = 1` and `tp[5] = 1`. Scanning $(5, 3)$ detects a blossom with base $b = \text{lca}(5, 3) = 3$!
   - `contract(5, 3, 3)` sets `pre[5] = 3`, flips `tp[4]` from `2` (Inner) to `1` (Outer!), and pushes $4$ into the BFS queue!
   - Now $4$ is **Outer (`tp[4] = 1`)**! When $4$ is popped from the queue, it scans $(4, 7)$ to exposed vertex $7$!
   - `aug(7)` traces: $7 \xleftarrow{\text{pre}} 4 \xlongequal{\text{match}} 5 \xleftarrow{\text{pre}} 3 \xlongequal{\text{match}} 2 \xleftarrow{\text{pre}} 1$, yielding the valid augmenting path $1 - 2 = 3 - 5 = 4 - 7$ of size $3$!

#### Three Fatal Broken Gadget Counterexamples in Blossom Implementation

> [!WARNING]
> **Broken Gadget 1: Contracting `(u, v)` in Only One Direction Instead of Calling Both `contract(u, v, b)` and `contract(v, u, b)`**
> Both $u \leadsto b$ and $v \leadsto b$ contain Inner (`Type 2`) vertices that must be flipped to Outer (`Type 1`), and the bridge edge $(u, v)$ must set `pre[u] = v` on one side and `pre[v] = u` on the other (before overwriting along the chain). Calling `contract` on only one side leaves half the blossom stuck as `Type 2`!
>
> **Broken Gadget 2: Using Raw Vertex IDs Instead of `find(u)` When Computing `lca(u, v)`**
> Blossoms can **nest** inside larger blossoms! When climbing from $u$ and $v$ to find their LCA, you must jump to `u = find(pre[match[u]])` at every step; using raw `u = pre[match[u]]` walks into already-contracted sub-blossoms whose `pre` pointers were reversed by earlier `contract` calls, causing an infinite loop!
>
> **Broken Gadget 3: Assuming Minimum Vertex Cover = Maximum Matching on Non-Bipartite Graphs**
> König's Theorem ($\tau(G) = \nu(G)$) holds **only** on bipartite graphs. On a triangle $K_3$, $\nu(K_3) = 1$, whereas the Minimum Vertex Cover has size $\tau(K_3) = 2$ (and Maximum Independent Set has size $\alpha(K_3) = 1$). Never reduce general-graph Independent Set or Vertex Cover to Edmonds' Blossom unless the graph has been proven bipartite or is a line graph / claw-free graph!

---

## Iteration 45: General Graph Matching II — Non-Bipartite Gadget Modelling, Weighted Blossom LP, Algebraic Tutte Matrix & LGV Bridges

### 1. Step 1: The Non-Graph Diagnostic Signal (Recognition)

In Iteration 45, we investigate three high-level bridges surrounding General Graph Matching:
1. **Non-Bipartite Capacity & Threshold Gadgets (`[WC2016] 挑战 NPC` — Triangle Bin Splitting)**: How do you recognize when a packing/bin-assignment problem with capacity $3$ and a non-linear reward ("count bins with $\le 1$ ball") compiles into unweighted General Graph Matching?
2. **Algebraic Tutte Matrix (`Tutte 矩阵`)**: When $V \le 500$ and the problem asks for **lexicographically first maximum matchings**, **matroid basis over matchable vertex subsets**, **dynamic vertex/edge updates**, or **counting/checking matchability**, randomized linear algebra over $\mathbb{F}_{998244353}$ via the skew-symmetric Tutte Matrix is often simpler and faster ($O(V^3)$ with tiny constant or $O(V^2)$ per rank update) than repeated Blossom runs!
3. **LGV Lemma vs. MCMF Disjoint Paths**: Recognizing whether a $K$-disjoint-paths problem on a DAG admits a topological non-crossing invariant ($\implies$ $O(K^3)$ LGV determinant) or allows arbitrary path permutations and capacities ($\implies$ MCMF).

---

### 2. Archetype 45.1: Non-Bipartite Gadget Modelling (`[WC2016] 挑战 NPC` & Tutte $b$-Matching)

#### Complete 4-Step Compilation of `[WC2016] 挑战 NPC` (`Luogu P4258`)
- **Problem Statement**: There are $N$ balls and $M$ bins ($N + 3M \le 600$). Each bin can hold **at most 3 balls**. We are given which balls are allowed to go into which bins. Every ball *must* be placed into some compatible bin. A bin is called "half-empty" (good) if it ends up containing **at most 1 ball** ($0$ or $1$ ball). Maximize the number of good bins (and construct the assignment).
- **Step 1 (Diagnostic Signal)**:
  - Why Bipartite Flow/MCMF Fails! Suppose we try to model this with Min-Cost Max-Flow where bin $j$ has capacity $3$ and we put costs on the 1st, 2nd, and 3rd unit of flow into bin $j$:
    - Load $0 \implies$ reward $1$ (good)
    - Load $1 \implies$ reward $1$ (good)
    - Load $2 \implies$ reward $0$ (not good)
    - Load $3 \implies$ reward $0$ (not good)
    Look at the marginal reward differences $\Delta R(k) = R(k) - R(k-1)$ for the 1st, 2nd, and 3rd ball entering bin $j$:
    $$\Delta R(1) = 0, \qquad \Delta R(2) = -1, \qquad \Delta R(3) = 0.$$
    Wait: for Max-Reward (Min-Cost) Flow to work with parallel edges, marginal rewards must be **concave (non-increasing)**: $\Delta R(1) \ge \Delta R(2) \ge \Delta R(3)$. Here $0 > -1 < 0$ is **NOT concave**! If you put parallel edges of cost $(0, +1, 0)$ for the 1st, 2nd, and 3rd ball, MCMF will greedily take the 1st ball (cost $0$) and the **3rd ball (cost $0$)** while skipping the 2nd ball (cost $+1$), illegally claiming that a bin with $2$ balls costs $0 + 0 = 0$!
  - Because the non-concave step occurs between load $1$ and load $2$ (a parity pair!), **General Non-Bipartite Matching** can enforce it exactly!

- **Step 2 & 3 (Algebraic & Mechanical Compilation — The 3-Vertex Triangle Bin Gadget)**:
  For each bin $j \in \{1, \dots, M\}$, create **three vertices** $b_{j,1}, b_{j,2}, b_{j,3}$:
  1. Connect the first two vertices of bin $j$ to each other with an **internal bin edge**:
     $$e_j^{\text{int}} = (b_{j,1}, b_{j,2}).$$
  2. If ball $i \in \{1, \dots, N\}$ is allowed to enter bin $j$, add **three compatibility edges**:
     $$(i, b_{j,1}), \quad (i, b_{j,2}), \quad (i, b_{j,3}).$$

```
                   Ball i
                  /  |   \
                 /   |    \
                v    v     v
            (b_j,1)===(b_j,2)   (b_j,3)   <-- Bin j's 3-vertex gadget!
             Internal edge e_j
```

  Now let $k_j \in \{0, 1, 2, 3\}$ be the number of balls matched to $\{b_{j,1}, b_{j,2}, b_{j,3}\}$ in a valid matching where all $N$ balls are matched:
  - **If $k_j = 0$**: Neither $b_{j,1}$ nor $b_{j,2}$ is matched to a ball, so we can match $(b_{j,1}, b_{j,2}) \in M$. Contribution to $|M|$ beyond balls: **$+1$**.
  - **If $k_j = 1$**: Match the single ball to $b_{j,3}$; then $b_{j,1}$ and $b_{j,2}$ are still free and match via $(b_{j,1}, b_{j,2}) \in M$! Contribution to $|M|$ beyond balls: **$+1$**.
  - **If $k_j = 2$**: Two vertices among $\{b_{j,1}, b_{j,2}, b_{j,3}\}$ are matched to balls, leaving only $3 - 2 = 1$ vertex free inside bin $j$. Thus $(b_{j,1}, b_{j,2})$ **cannot** be in $M$! Contribution to $|M|$ beyond balls: **$0$**.
  - **If $k_j = 3$**: All three vertices of bin $j$ are matched to balls. Contribution to $|M|$ beyond balls: **$0$**.

  Every ball must be matched! Wait: what if a maximum matching leaves a ball unmatched in order to match two internal bin edges?
  Look at any augmenting path or check: matching a ball $i$ to bin $j$ breaks at most **one** internal edge $(b_{j,1}, b_{j,2})$, which never decreases $|M|$ ($+1 - 1 = 0$). Even simpler: if we first match all $N$ balls into the bins (or start the Blossom algorithm by augmenting from the $N$ ball vertices $1, \dots, N$ FIRST, and only afterwards augment from the bin vertices $b_{j,1}$), since augmenting paths never unmatch an already-matched vertex, if all $N$ balls can be matched after Phase 1, they remain 100% matched after Phase 2!
  Then:
  $$\text{Maximum Number of Good Bins ($\le 1$ ball)} = |M_{\max}| - N!$$

---

### 3. Archetype 45.2: Weighted Blossom LP Duality & The Odd-Set Inequalities

When edges have weights $w(e)$ and we want a **Maximum Weight General Graph Matching**, why can't we just use the bipartite Kuhn–Munkres dual LP $\min \sum_{v \in V} y_v \text{ s.t. } y_u + y_v \ge w(u, v)$?

#### The Triangle Integrality Gap & Edmonds' Blossom Polytope (1965)
Consider $K_3$ on $\{1, 2, 3\}$ with $w(1, 2) = w(2, 3) = w(3, 1) = 2$:
- Bipartite LP relaxation: setting $x_{12} = x_{23} = x_{31} = 1/2$ satisfies $\sum_{e \ni v} x_e = 1$ and gives objective $3$, with dual potentials $y_1 = y_2 = y_3 = 1$ ($\sum y_v = 3$).
- Yet any integral matching on $K_3$ has at most $\lfloor 3/2 \rfloor = 1$ edge, so the true maximum weight is $2$!

**Theorem 45.1 (Edmonds' Matching Polytope Theorem)**:
The convex hull of indicator vectors $x \in \{0, 1\}^E$ of matchings in ANY undirected graph $G = (V, E)$ is completely defined by:
1. $x_e \ge 0$ for all $e \in E$,
2. $\sum_{e \in \delta(v)} x_e \le 1$ for all $v \in V$ (Degree constraints, dual variable $y_v \ge 0$),
3. **Odd-Set (Blossom) Inequalities**: For every odd-sized subset $B \subseteq V$ with $|B| = 2k + 1 \ge 3$, the number of matched edges with *both* endpoints inside $B$ cannot exceed $k$:
   $$\sum_{e \in E(B)} x_e \le \frac{|B| - 1}{2} \quad \text{(dual variable $z_B \ge 0$)}.$$

Taking the Linear Programming Dual gives the exact primal-dual invariant maintained by the $O(V^3)$ Weighted Blossom algorithm (`带权带花树`):
$$\min_{y_v \ge 0, z_B \ge 0} \left( \sum_{v \in V} y_v + \sum_{|B| \ge 3 \text{ odd}} \frac{|B|-1}{2} z_B \right) \quad \text{subject to} \quad y_u + y_v + \sum_{\substack{B \text{ odd} \\ u, v \in B}} z_B \ge w(u, v) \;\;\forall (u, v) \in E.$$
By Complementary Slackness:
- Every matched edge $(u, v) \in M$ must be tight ($y_u + y_v + \sum_{B \ni u,v} z_B = w(u, v)$).
- Every active blossom $B$ with $z_B > 0$ must be **full** ($\sum_{e \in E(B)} x_e = (|B|-1)/2$ and its base is matched or exposed according to tightness).

---

### 4. Archetype 45.3: The Skew-Symmetric Tutte Matrix (`Tutte 矩阵`) & Algebraic Matching

When $V \le 500$, there is an astonishing algebraic bridge between General Graph Matching and Linear Algebra over a finite field $\mathbb{F}_p$ (such as $p = 998244353$).

#### Definition 45.2 (The Tutte Matrix $T(x)$)
Given an undirected graph $G = (V, E)$ on $V = \{1, \dots, n\}$, introduce an independent variable $x_{u,v}$ for each edge $(u, v) \in E$ ($u < v$), and define the $n \times n$ **skew-symmetric Tutte matrix** $T(x)$ ($T^T = -T$) by:
$$T_{u,v} = \begin{cases} +x_{u,v} & \text{if } (u, v) \in E \text{ and } u < v, \\ -x_{v,u} & \text{if } (u, v) \in E \text{ and } u > v, \\ 0 & \text{if } (u, v) \notin E. \end{cases}$$

#### Theorem 45.3 (Tutte 1947, Lovász 1979, Rabin–Vazirani 1989)
1. **Perfect Matching Criterion**: $\det T(x) \neq 0$ (as a polynomial in $\mathbb{Z}[x]$) **if and only if** $G$ has a perfect matching!
2. **Maximum Matching Size Formula**: For ANY graph $G$, the maximum matching size $\nu(G)$ satisfies:
   $$\text{rank}\big(T(x)\big) = 2 \nu(G).$$
3. **Randomized Evaluation (Schwartz–Zippel Lemma)**: If each $x_{u,v}$ is chosen independently and uniformly at random from $\{1, 2, \dots, p-1\}$ modulo a prime $p$ (e.g., $p = 998244353$), then:
   $$\Pr\Big[\text{rank}_{\mathbb{F}_p}(T) = 2 \nu(G)\Big] \ge 1 - \frac{n}{p}.$$
4. **Matroid / Submatrix Rank & Lexicographical Basis**:
   A subset of vertices $S \subseteq V$ can be simultaneously saturated by some matching in $G$ **if and only if** the rows of $T$ indexed by $S$ are linearly independent! Consequently, running a single pass of Gaussian elimination on the rows of $T$ in a priority order $v_1, v_2, \dots, v_n$ finds the **lexicographically first (or maximum-weight vertex-subset) matchable set** in $O(n^3)$ time!

*Proof of why Odd Cycles Cancel and Even Cycles Survive in $\det T(x)$*:
Expand $\det T(x) = \sum_{\pi \in S_n} \text{sgn}(\pi) \prod_{i=1}^n T_{i, \pi(i)}$. Every permutation $\pi$ with non-zero product decomposes into disjoint directed cycles on $G$.
- Suppose $\pi$ contains at least one **odd-length cycle** (including 1-cycles since $T_{i,i} = 0$). Pick the odd cycle $C = (v_1 \to v_2 \to \dots \to v_{2k+1} \to v_1)$ containing the smallest vertex label, and let $\pi'$ be the permutation obtained by **reversing $C$** ($v_1 \to v_{2k+1} \to \dots \to v_2 \to v_1$).
- Reversing a cycle of length $2k+1$ preserves its parity, so $\text{sgn}(\pi') = \text{sgn}(\pi)$.
- However, because $T$ is skew-symmetric ($T_{v,u} = -T_{u,v}$), reversing all $2k+1$ directed edges of $C$ multiplies the weight of $C$ by $(-1)^{2k+1} = -1$!
- Thus the terms for $\pi$ and $\pi'$ cancel out identically ($\text{term}(\pi) + \text{term}(\pi') = 0$).
- Remaining permutations consist exclusively of **even-length cycles**. If $G$ has a perfect matching $M = \{(u_1, v_1), \dots, (u_{n/2}, v_{n/2})\}$, the 2-cycle permutation $\pi_M$ swapping each $u_r \leftrightarrow v_r$ produces the unique monomial $\prod_{r=1}^{n/2} x_{u_r, v_r}^2$, which cannot be canceled by any other permutation! $\blacksquare$

---

### 5. Archetype 45.4: Sharp Boundary Contrast — Lindström–Gessel–Viennot (LGV) Lemma vs. Flow / MCMF

A classic diagnostic trap in competitive programming is confusing **Counting Non-Intersecting DAG Paths (LGV Lemma)** with **Finding/Routing $K$ Vertex-Disjoint Paths (Max-Flow / MCMF)**. Let us establish the exact boundary:

#### Theorem 45.4 (Lindström–Gessel–Viennot Lemma)
In a finite Directed Acyclic Graph (DAG), let $A = \{s_1, \dots, s_K\}$ be $K$ sources and $B = \{t_1, \dots, t_K\}$ be $K$ sinks, and let $e(s_i, t_j)$ be the number (or generating function sum) of directed paths from $s_i$ to $t_j$. Define the $K \times K$ path matrix $M_{i,j} = e(s_i, t_j)$. Then:
$$\det(M) = \sum_{\sigma \in S_K} \text{sgn}(\sigma) \sum_{\substack{P_1: s_1 \leadsto t_{\sigma(1)}, \dots, P_K: s_K \leadsto t_{\sigma(K)} \\ P_1, \dots, P_K \text{ vertex-disjoint}}} \prod_{r=1}^K w(P_r).$$

| Feature / Question | **LGV Lemma ($\det M$)** | **Max-Flow / MCMF (Vertex-Split Network)** |
| :--- | :--- | :--- |
| **Primary Task** | **Counting** tuples of vertex-disjoint paths (modulo $p$) | **Existence / Max-Count / Min-Cost** of $K$ disjoint paths |
| **Topological Requirement** | Must be a **DAG**, AND for Counting to be exact, **only the identity permutation $\sigma = \text{id}$** may admit non-intersecting paths (planar non-crossing layout, e.g., grid boundaries `CF 348 D`)! | Works on **ANY directed or undirected graph** (even with cycles, capacities, and arbitrary $s_i \to t_{\sigma(i)}$ permutations!) |
| **What Happens if $\sigma \neq \text{id}$ Can Be Disjoint?** | **Catastrophic Cancellation!** An odd permutation $\sigma$ with $\text{sgn}(\sigma) = -1$ subtracts from $\det(M)$; e.g., if 1 disjoint tuple has $\sigma = (1, 2)$ and 1 disjoint tuple has $\sigma = (2, 1)$, $\det(M) = 1 - 1 = 0$ even though disjoint paths exist! | **Zero Cancellation**: Flow routes to $T$ regardless of which $s_i$ connects to which $t_{\sigma(i)}$. (Can assign random weights $w(e)$ in LGV to test existence with high probability on DAGs!). |
| **Complexity** | $O(K \cdot (V + E) + K^3)$ via DAG DP + Gaussian Elimination | $O(K \cdot E \log V)$ via SSP MCMF or $O(E \sqrt{V})$ via Dinic |

---

## Master Recognition & Compilation Decision Table (Wave 5A)

| Non-Graph / Surface Problem Signal | Bottleneck / Scale | Underlying Flow / Matching Structure | Compiled Fast Architecture | Time & Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| $i$ connects to all $j \in [L_i, R_i]$ | $N \le 5 \cdot 10^4$ | 1D Interval Biclique | **1D Segment Tree (`入树` + `出树`)** | $O(N \log N)$ size + Dinic/MCMF |
| $i$ connects to $j < i$ with $a_j \in [L_i, R_i]$ | $N \le 5 \cdot 10^4$ | 2D Prefix-Range Dominance | **Persistent SegTree** (`root[i-1]` query + `new -> old` link) | $O(N \log N)$ size + Dinic/MCMF |
| $i$ connects to $j < i$ with cost $\|a_i - a_j\|$ | $N \le 2 \cdot 10^4$ | 2D Prefix + $\ell_1$ Distance | **CDQ Divide-and-Conquer** sorted value chain | $O(N \log N)$ size + MCMF |
| 1D sequential buy/sell or prefix pairing | $N \le 5 \cdot 10^5$ | 1D Chain MCMF | **1-Heap Regret Greedy** (`push(p_j)` twice on match) | $O(N \log N)$ time, $O(N)$ space |
| 1D mice $x_i$ & holes $(y_j, c_j, w_j)$, cost $\|x_i - y_j\| + w_j$ | $N, M \le 10^5$, $c_j \le 10^9$ | 1D Geometric MCMF | **2-Heap Simulated MCMF** (`-2x - v_H`, `-2y - v_M`, `-y - w`) | $O((N+M)\log(N+M))$ |
| Tree supplies/demands, cost $\text{dist}(u, v)$ | $N \le 2.5 \cdot 10^5$ | Tree MCMF | **Mergeable Heaps + LCA shift** (`2*d(L) - v`) | $O(N \log^2 N)$ or $O(N \log N)$ |
| Global $k$-step 1D pairing ($i \le j$) or $k$ subarrays | $N \le 5 \cdot 10^5$ | 1D Timeline Residual Graph | **Dynamic Segment Tree** tracking `min_f` & reverse pairs | $O((N + K) \log N)$ |
| Pick $K$ from $A$, $K$ from $B$ with $\|I \cap J\| \ge L$ | $N \le 2 \cdot 10^5$ | Coupled Bipartite + Bridge $P \to Q$ | **5-Heap State Automaton** (Cand 1–5 with `free_cap` $\pm 1$) | $O((N + K) \log N)$ |
| Symmetric compatibility with odd cycles / 2-player game | $V \le 500$ | Non-Bipartite Matching / Gallai–Edmonds | **Edmonds' Blossom (`带花树`)** / Alternating Forest $D(G)$ | $O(V E \alpha(V))$ |
| Submatrix matching rank / dynamic edges / lex-first | $V \le 500$ | Skew-Symmetric Pfaffian | **Tutte Matrix** $T_{u,v} = \pm x_{u,v} \pmod p$ | $O(V^3)$ Gaussian / $O(V^2)$ update |

---

## 4-Tier Curated Problem Bank (Part 1: Stepping Stone & Intermediate — 10 Problems)

> [!NOTE]
> Every problem below is a non-template contest problem solved using the **4-Step "Zero Magic Gadgets" Compilation Standard**: (1) Diagnostic Signal, (2) Algebraic / Logical Intermediate Model, (3) Reverse-Engineering Scratchpad, and (4) Complete Solution & 3-Tier Progressive Hints.

---

### Tier 1: Stepping Stone (`P01`–`P05`)

#### P01 — Codeforces 786 B: Legacy (`[EN]` — 1D Segment Tree In-Tree & Out-Tree Sparsification)
- **Judge URL**: [https://codeforces.com/problemset/problem/786/B](https://codeforces.com/problemset/problem/786/B)
- **Inline Statement & Constraints**:
  Given $N$ planets ($1 \le N \le 10^5$), starting planet $s$, and $Q$ ($1 \le Q \le 10^5$) directed teleporter plans of three types:
  - Type 1: from planet $u$ to planet $v$ with cost $w$.
  - Type 2: from planet $u$ to **any** planet in interval $[L, R]$ with cost $w$.
  - Type 3: from **any** planet in interval $[L, R]$ to planet $v$ with cost $w$.
  Find the minimum cost from $s$ to every planet $1, \dots, N$ (and in the flow variant, find the Max-Flow / Min-Cost Flow when each teleporter plan also has a bundle capacity $c$).
- **Step 1 (Diagnostic Signal)**:
  - Explicit graph construction adds $O(N)$ edges per Type 2/3 plan, yielding $O(N Q) = 10^{10}$ edges (MLE/TLE).
  - Because every planet $x \in [L, R]$ in a Type 2/3 plan shares the exact same transition cost $w$ (and shared bundle capacity $c$), the interval $[L, R]$ acts as a 1D biclique that factors through $O(\log N)$ canonical dyadic intervals.
- **Step 2 (Algebraic / Logical Intermediate Representation)**:
  For shortest paths (the dual of unit-flow MCMF), the Bellman–Ford / LP dual potential inequalities for Type 2 ($u \to [L, R]$) and Type 3 ($[L, R] \to v$) are:
  $$\forall x \in [L, R]: d(x) \le d(u) + w \iff \forall r \in \text{Decomp}(L, R): d_{\text{Out}}(p_r) \le d(u) + w, \;\; \forall x \in I(p_r): d(x) \le d_{\text{Out}}(p_r),$$
  $$\forall x \in [L, R]: d(v) \le d(x) + w \iff d(v) \le \min_{r \in \text{Decomp}(L, R)} d_{\text{In}}(p_r) + w, \;\; d_{\text{In}}(p_r) = \min_{x \in I(p_r)} d(x).$$
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Build two segment trees over $[1, N]$:
    1. `Out[p]`: parent $\to$ children with cost $0$ (distributes down to leaves).
    2. `In[p]`: children $\to$ parent with cost $0$ (collects up from leaves).
  - Identify `Out[leaf(i)] = In[leaf(i)] = i` (total vertices $\le 5N$ or $3N$ with heap indexing).
  - Type 2 ($u \to [L, R]$): add $u \xrightarrow{w} \text{Out}[p_r]$ for each of the $O(\log N)$ canonical nodes $p_r$.
  - Type 3 ($[L, R] \to v$): add $\text{In}[p_r] \xrightarrow{w} v$ for each canonical node $p_r$.
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Decompose $[L, R]$ into $O(\log N)$ segment tree intervals. Why does a single tree with undirected 0-cost edges fail?
  - *Hint 2*: Separate "pushing down to leaves" (`Out-Tree`) from "pulling up from leaves" (`In-Tree`).
  - *Hint 3*: Share the leaf vertices between the two trees so flow/paths arriving at a leaf in `Out-Tree` can immediately climb `In-Tree`. Run Dijkstra in $O((N + Q \log N) \log N)$.

---

#### P02 — Codeforces 865 D: Buy Low Sell High (`[EN]` — 1-Heap Simulated MCMF / Regret Greedy)
- **Judge URL**: [https://codeforces.com/problemset/problem/865/D](https://codeforces.com/problemset/problem/865/D)
- **Inline Statement & Constraints**:
  Over $N$ days ($1 \le N \le 3 \cdot 10^5$), the stock price on day $i$ is $p_i$ ($1 \le p_i \le 10^6$). Each day you may buy at most 1 share, sell at most 1 share you currently hold, or do nothing. Starting with 0 shares, maximize total profit.
- **Step 1 (Diagnostic Signal)**:
  - $N = 3 \cdot 10^5$ rules out $O(N^2)$ DP (where state is number of shares held) and explicit MCMF.
  - Because stock units are indistinguishable and any buy at $i$ can match with any later sell at $j > i$, this is a 1D chain Max-Cost Flow problem.
- **Step 2 (Algebraic / Residual Formulation)**:
  Pairing a buy at $i$ with a sell at $j$ earns $p_j - p_i$. If a later day $k > j$ wants to replace $j$ as the sell partner of $i$, the algebraic identity:
  $$p_k - p_i = (p_j - p_i) + (p_k - p_j)$$
  shows that canceling the sell at $j$ is algebraically identical to offering a virtual share at price $p_j$!
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Maintain a min-heap $Q$ of available buy prices.
  - On day $j$:
    1. Push $p_j$ into $Q$ (representing the fresh edge $S \to j$ of buying a share on day $j$).
    2. If $Q.\text{top}() < p_j$, match day $j$ as a sell with $x = Q.\text{top}()$, add $p_j - x$ to `ans`, pop $x$, and **push a second copy of $p_j$ into $Q$** (representing the reverse residual edge $T \to j$ that cancels the sell at $j$).
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Write the telescopy $(p_k - p_i) = (p_j - p_i) + (p_k - p_j)$. What does selecting the second term correspond to in the residual graph?
  - *Hint 2*: Notice that day $j$ can either: (a) remain a sell day, (b) have its sell canceled so day $j$ does nothing, or (c) have its sell canceled AND buy a share on day $j$!
  - *Hint 3*: Pushing $p_j$ once unconditionally and pushing $p_j$ a second time when a match occurs provides both tokens (one for canceling the sell at $j$, one for buying at $j$). Complexity: $O(N \log N)$.

---

#### P03 — Codeforces 730 I: Olympiad in Programming and Sports (`[EN]` — 3-Heap Coupled Bipartite Simulation)
- **Judge URL**: [https://codeforces.com/problemset/problem/730/I](https://codeforces.com/problemset/problem/730/I)
- **Inline Statement & Constraints**:
  There are $N$ students ($2 \le p + s \le N \le 3000$, solvable in $O(N \log N)$ for $N \le 3 \cdot 10^5$). Student $i$ has programming skill $a_i$ and sports skill $b_i$. Choose $p$ students for the programming team $P$ and $s$ disjoint students for the sports team $B$ ($P \cap B = \emptyset$) to maximize $\sum_{i \in P} a_i + \sum_{j \in B} b_j$.
- **Step 1 (Diagnostic Signal)**:
  - Selecting $p$ items for $A$ and $s$ items for $B$ with disjointness $P \cap B = \emptyset$ is the textbook $K$-unit Bipartite Max-Cost Flow network ($S \to i$ cap $1$ cost $0$; $i \to T_A$ cost $a_i$; $i \to T_B$ cost $b_i$; $T_A \to T$ cap $p$; $T_B \to T$ cap $s$).
- **Step 2 (Algebraic / Residual Formulation)**:
  Suppose we first greedily pick the $p$ students with the largest $a_i$ into team $P$. Now we must augment $s$ times from $S$ to $T_B$ in the residual network!
  For each augmentation to $T_B$, there are only **two** simple residual paths from $S$ to $T_B$:
  - **Path 1 (Direct Unassigned $\to B$)**: Pick an unassigned student $j \notin P \cup B$ and put $j \in B$. Gain: $+b_j$.
  - **Path 2 (Transfer $i \in P \to B$ and Replace $i$ in $P$ with Unassigned $j \notin P \cup B$)**: Move $i \in P$ to $B$ (net change $b_i - a_i$) and put unassigned $j$ into $P$ (gain $+a_j$). Total gain: $(b_i - a_i) + a_j$.
- **Step 3 (Reverse-Engineering Scratchpad)**:
  Maintain 3 max-heaps:
  - $Q_A$: unassigned students $j \notin P \cup B$, keyed by $a_j$.
  - $Q_B$: unassigned students $j \notin P \cup B$, keyed by $b_j$.
  - $Q_{AB}$: students currently in $P$, keyed by $b_i - a_i$.
  Initialize by putting the top $p$ students by $a_i$ into $P$ (and pushing them into $Q_{AB}$), and the remaining $N - p$ students into $Q_A$ and $Q_B$. Then repeat $s$ times: compare `Q_B.top()` (Path 1) against `Q_AB.top() + Q_A.top()` (Path 2), execute the better transition, and update the heaps!
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: After picking the best $p$ students for Programming, what happens if one of those $p$ students is desperately needed for Sports?
  - *Hint 2*: Draw the residual graph after saturating $T_A \to T$ with $p$ units of flow. List all augmenting paths to $T_B$.
  - *Hint 3*: Path 1 has gain $b_j$; Path 2 has gain $(b_i - a_i) + a_j$. Track them with 3 priority queues in $O((N + s) \log N)$ time.

---

#### P04 — Codeforces 1045 A: Last Chance (`[EN]` — 1D SegTree Out-Tree + Degree-2 Parity Adjustment)
- **Judge URL**: [https://codeforces.com/problemset/problem/1045/A](https://codeforces.com/problemset/problem/1045/A)
- **Inline Statement & Constraints**:
  $N$ weapons ($1 \le N \le 5000$) and $M$ enemy spaceships ($1 \le M \le 5000$). Each spaceship can be destroyed by at most 1 weapon. There are 3 types of weapons:
  - Type 0: can destroy 1 spaceship from a given subset $S_i$.
  - Type 1: can destroy 1 spaceship in a contiguous interval $[L_i, R_i]$.
  - Type 2 (`SQL rocket`): gives you a triple $\{a_i, b_i, c_i\}$ of spaceships (which is guaranteed to be **disjoint** from all other Type 2 triples) and must destroy **either 0 or 2** of them!
  Maximize the number of destroyed spaceships and output the weapon-to-spaceship pairs.
- **Step 1 (Diagnostic Signal)**:
  - Type 1 weapons require **1D Segment Tree Out-Tree Sparsification** ($N, M \le 5000$).
  - Type 2 weapons appear to require parity-2 matching ("0 or 2"), which normally breaks Max-Flow! Why does Max-Flow work here? Because the problem guarantees that if a spaceship is in a Type 2 triple, any Type 0/1 weapon can just drop that spaceship without penalty!
- **Step 2 & 3 (Algebraic & Mechanical Compilation)**:
  - Give each Type 0 and Type 1 weapon an edge from $S$ of capacity $1$, and each Type 2 weapon an edge from $S$ of capacity $2$ connecting to $\{a_i, b_i, c_i\}$.
  - Why is the Maximum Flow of this network **always achievable** while satisfying the "0 or 2" rule for every Type 2 weapon?
    Suppose after running Dinic's algorithm, some Type 2 weapon $w$ only carries **1 unit of flow** (say destroying $a_i$, while $b_i$ and $c_i$ do not receive flow from $w$).
    - If either $b_i$ or $c_i$ is currently **unmatched** (not destroyed by any weapon), we could have sent a 2nd unit of flow $S \to w \to b_i \to T$, contradicting that Dinic found a **maximum** flow!
    - Therefore, both $b_i$ and $c_i$ **must already be destroyed by some other weapons**! Since Type 2 triples are pairwise disjoint, the weapon $w'$ currently destroying $b_i$ is of **Type 0 or Type 1** (which is allowed to destroy 0 spaceships!).
    - Simply reassign $b_i$ from $w'$ to $w$! Now $w$ destroys $\{a_i, b_i\}$ (2 spaceships!) and $w'$ destroys $0$ spaceships, preserving the exact total number of destroyed spaceships!
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Build a Segment Tree Out-Tree for $[1, M]$ to handle Type 1 weapons in $O(N \log M)$ edges.
  - *Hint 2*: Relax Type 2 weapons to capacity $\le 2$ ($S \to w$ with $\text{cap} = 2$) and run Dinic. What if a Type 2 weapon ends up with flow $1$?
  - *Hint 3*: By maximality of flow, if a Type 2 weapon has flow $1$, both of its other two targets $\{b_i, c_i\}$ must be matched by Type 0/1 weapons. Steal $b_i$ from its Type 0/1 weapon after decomposing the flow on the Segment Tree!

---

#### P05 — Luogu P4258 / UOJ #171: `[WC2016] 挑战 NPC` (`[ZH]` — 3-Vertex Triangle Bin Gadget via Blossom)
- **Judge URL**: [https://uoj.ac/problem/171](https://uoj.ac/problem/171) / [https://www.luogu.com.cn/problem/P4258](https://www.luogu.com.cn/problem/P4258)
- **Inline Statement & Constraints**:
  Given $N$ balls and $M$ bins ($N + 3M \le 600$, $E$ compatibility relations). Each bin holds at most $3$ balls. Every ball must be placed into a compatible bin. Maximize the number of bins that contain **at most $1$ ball**, and output the bin assigned to each ball.
- **Step 1 (Diagnostic Signal)**:
  - As proven in Iteration 45, the reward function $R(k) = \mathbb{I}[k \le 1]$ for $k \in \{0, 1, 2, 3\}$ has marginal differences $\Delta R = (0, -1, 0)$, which is **non-concave**, causing Min-Cost Flow to fail.
  - The vertex bound $N + 3M \le 600$ is the classic signature of $O(V^3)$ Edmonds' Blossom!
- **Step 2 & 3 (Algebraic & Mechanical Compilation)**:
  - Split each bin $j \in \{1, \dots, M\}$ into three vertices $b_{j,1}, b_{j,2}, b_{j,3}$ and add the internal edge $(b_{j,1}, b_{j,2})$.
  - For each compatible pair $(i, j)$, connect ball $i$ to $b_{j,1}, b_{j,2}, b_{j,3}$.
  - **Ordering Rule**: In Edmonds' Blossom, augment from all ball vertices $1, \dots, N$ **first** (if any ball fails to match, output `0` — impossible), and then augment from all $b_{j,1}$ ($j = 1, \dots, M$).
  - Answer is $|M_{\max}| - N$, and each ball $i$ goes into the bin $j$ of its matched partner `match[i]`.
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Why does standard MCMF fail when rewarding bins with $\le 1$ ball out of capacity $3$?
  - *Hint 2*: Split each bin into 3 vertices. How can you add internal edges inside those 3 vertices so that an extra matched edge appears if and only if at most 1 vertex of the bin is matched to a ball?
  - *Hint 3*: Add a single edge $(b_{j,1}, b_{j,2})$ leaving $b_{j,3}$ isolated inside the bin. Augment balls first, then bin vertices, using Edmonds' Blossom in $O((N+3M) E \alpha(V))$.

---

### Tier 2: Intermediate (`P06`–`P10`)

#### P06 — BZOJ 3218 / Luogu P4318: `a + b Problem` (`[ZH]` — Project Selection Min-Cut + Persistent SegTree)
- **Judge URL**: [https://www.luogu.com.cn/problem/P3218](https://www.luogu.com.cn/problem/P3218) (BZOJ 3218)
- **Inline Statement & Constraints**:
  Given $N$ cells ($1 \le N \le 5000$). Cell $i$ has value $a_i$, white profit $w_i$, black profit $b_i$, penalty $p_i$, and range $[L_i, R_i]$ ($0 \le a_i, L_i, R_i \le 10^9$, $0 \le w_i, b_i, p_i \le 10^5$). Color each cell White or Black. Cell $i$ gets $w_i$ if White, $b_i$ if Black, **minus $p_i$** if cell $i$ is Black AND there exists at least one $j < i$ such that cell $j$ is White and $L_i \le a_j \le R_i$. Maximize total score.
- **Step 1 (Diagnostic Signal)**:
  - Binary choice (White vs. Black) with pairwise implication penalty ("$i$ is Black and $j$ is White $\implies$ lose $p_i$ paid at most once per $i$") is a **Project Selection Min-Cut (`燃やす埋める`)** model.
  - Because the condition is $j < i$ and $a_j \in [L_i, R_i]$, naive graph building creates $O(N^2)$ edges. We compress it with a **Persistent Segment Tree** (`Architecture 41.2`).
- **Step 2 (Algebraic Cut Polynomial)**:
  Let $x_i = 1$ if cell $i$ is Black ($S$-side) and $x_i = 0$ if cell $i$ is White ($T$-side). Introduce auxiliary binary indicator $y_i \in \{0, 1\}$ ($y_i = 0$ means cell $i$ pays the penalty $p_i$). We minimize the cut cost subtracted from $\sum_{i=1}^N (w_i + b_i)$:
  $$\min_{x, y \in \{0,1\}^N} \sum_{i=1}^N \left( w_i x_i + b_i (1 - x_i) + p_i x_i (1 - y_i) + \sum_{\substack{j < i \\ L_i \le a_j \le R_i}} \infty \cdot y_i (1 - x_j) \right).$$
  Check: if $x_i = 1$ (Black) and any valid $j < i$ has $x_j = 0$ (White), then to avoid paying $\infty$ on $y_i(1 - x_j)$, we are forced to set $y_i = 0$, which pays $p_i x_i (1 - y_i) = p_i$!
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Discretize $\{a_i\}$ to $[1, U]$ ($U \le N$).
  - For each $i \in \{1, \dots, N\}$:
    - $S \xrightarrow{b_i} i$ and $i \xrightarrow{w_i} T$.
    - Create auxiliary vertex $i'$ representing $y_i$: add $i \xrightarrow{p_i} i'$.
    - Query Version $i-1$ (`root[i-1]`) of the Persistent Out-Tree on $[L_i, R_i]$, adding $i' \xrightarrow{\infty} u_{\text{seg}}$ for each canonical node.
    - Insert $i$ at coordinate $a_i$ to create `root[i]`, connecting the new leaf to $i$ ($\text{leaf}_{\text{new}} \xrightarrow{\infty} i$) and linking every new node to its previous version ($p_{\text{new}} \xrightarrow{\infty} p_{\text{old}}$).
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Since $p_i$ is paid at most once even if multiple $j < i$ are White, introduce an auxiliary vertex $i'$ with edge $i \xrightarrow{p_i} i'$.
  - *Hint 2*: How do you connect $i'$ to all $j < i$ with $a_j \in [L_i, R_i]$ using only $O(\log N)$ edges?
  - *Hint 3*: Query `root[i-1]` of a Persistent Segment Tree before inserting $a_i$ into `root[i]`. Don't forget $p_{\text{new}} \xrightarrow{\infty} p_{\text{old}}$ when duplicate values $a_j$ occur!

---

#### P07 — Luogu P5331: `[SNOI2019] 通信` (`[ZH]` — Min-Cost Flow + CDQ Divide-and-Conquer Sparsification)
- **Judge URL**: [https://www.luogu.com.cn/problem/P5331](https://www.luogu.com.cn/problem/P5331)
- **Inline Statement & Constraints**:
  $N$ signal stations ($1 \le N \le 1000$, $a_i \le 10^9$). Station $i$ can either connect directly to the control center at cost $W$, or connect to a single earlier station $j < i$ at cost $|a_i - a_j|$. Each earlier station $j$ can be connected to by **at most one** later station $i$. Minimize the total cost to connect all $N$ stations.
- **Step 1 (Diagnostic Signal)**:
  - Each station $i$ has in-degree $1$ (either from Center at cost $W$ or from a unique $j < i$ at cost $|a_i - a_j|$). This is a **Minimum-Cost Bipartite Matching / DAG Path Cover** problem.
  - Because $O(N^2)$ edges with $|a_i - a_j|$ costs are too dense for MCMF, we use **CDQ Divide-and-Conquer Sparsification** (`Architecture 41.3`).
- **Step 2 & 3 (Algebraic & Mechanical Compilation)**:
  - Split each station $i$ into $i_{\text{out}}$ (needs to connect to $j < i$ or Center) and $j_{\text{in}}$ (can accept at most 1 connection from $i > j$):
    - $S \xrightarrow{\text{cap}=1, \text{cost}=0} i_{\text{out}}$ for all $i$.
    - $i_{\text{out}} \xrightarrow{\text{cap}=1, \text{cost}=W} T$ (connect directly to Center).
    - $j_{\text{in}} \xrightarrow{\text{cap}=1, \text{cost}=0} T$ for all $j$.
  - Run `CDQ_Build(1, N)` (`Architecture 41.3`): at interval $[L, R]$ with midpoint $M$, sort the unique values $v_1 < \dots < v_k$ in $[L, R]$, build the bidirectional chain $h_r \leftrightarrow h_{r+1}$ with $\text{cap} = \infty, \text{cost} = v_{r+1} - v_r$, connect $i_{\text{out}} \xrightarrow{\infty, 0} h_{\text{idx}(a_i)}$ for $i \in [M+1, R]$, and connect $h_{\text{idx}(a_j)} \xrightarrow{\infty, 0} j_{\text{in}}$ for $j \in [L, M]$.
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Model the "at most one successor" rule as bipartite matching between $i_{\text{out}}$ and $j_{\text{in}}$ ($j < i$), with fallback $i_{\text{out}} \to T$ of cost $W$.
  - *Hint 2*: How can you represent $|a_i - a_j|$ as shortest-path distance on a sparse graph while strictly enforcing $j < i$?
  - *Hint 3*: Apply CDQ divide-and-conquer on $[1, N]$: in each split $[L, M]$ vs. $[M+1, R]$, sort the coordinates to build a 1D chain of size $O(R - L)$ where right-half nodes enter and left-half nodes exit. Total edges: $O(N \log N)$.

---

#### P08 — AtCoder AGC 018 C: Coins (`[JA]` — 3-Group Partition via Simulated MCMF / Split Sweep)
- **Judge URL**: [https://atcoder.jp/contests/agc018/tasks/agc018_c](https://atcoder.jp/contests/agc018/tasks/agc018_c)
- **Inline Statement & Constraints**:
  There are $N = X + Y + Z$ people ($1 \le X, Y, Z$ and $N \le 10^5$). Person $i$ has $A_i$ gold, $B_i$ silver, and $C_i$ bronze coins ($1 \le A_i, B_i, C_i \le 10^9$). Partition the $N$ people into disjoint sets of size $X, Y, Z$ contributing gold, silver, and bronze respectively, maximizing total coins.
- **Step 1 (Diagnostic Signal)**:
  - Exact 3-way generalization of `CF 730 I` (`P03`), with $N = 10^5$ and $X + Y + Z = N$ (every person must be assigned to one of the 3 groups).
- **Step 2 (Algebraic Reduction — Eliminating One Dimension)**:
  Since every person $i$ is assigned to exactly one of $\{A, B, C\}$, initially assign **everyone** to Bronze ($C$), giving base sum $S_0 = \sum_{i=1}^N C_i$.
  Now person $i$ has two modified values:
  $$a'_i = A_i - C_i, \qquad b'_i = B_i - C_i,$$
  and we must choose $X$ people for $A'$ and $Y$ disjoint people for $B'$!
  What if we sort all $N$ people by $a'_i - b'_i = A_i - B_i$ in decreasing order?
  **Lemma (Potentials / Exchange Argument)**: In the optimal assignment, every person $i \in X$ and every person $j \in Y$ can be separated by a split index $k \in [X, N - Y]$ after sorting by $A_i - B_i$ descending! Why? Because if $i \in X$ appeared to the right of $j \in Y$, swapping their roles ($i \leftrightarrow j$) would change the objective by $(a'_j + b'_i) - (a'_i + b'_j) = (a'_j - b'_j) - (a'_i - b'_i) \ge 0$!
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - **Method A (1D Split-Point Heap Sweep)**: Sort by $A_i - B_i$ descending. For each prefix $[1, k]$ ($X \le k \le N - Y$), we must pick $X$ people for $A$ and $k - X$ people for $C$ (maintained by a min-heap of $A_i - C_i$ of size $X$!). For each suffix $[k+1, N]$, we must pick $Y$ people for $B$ and $(N - k) - Y$ people for $C$ (maintained by a min-heap of $B_i - C_i$ of size $Y$!). Take $\max_{k} (\text{Pref}[k] + \text{Suff}[k+1])$.
  - **Method B (Direct 3-Heap Simulated MCMF from `P03`)**: Apply the exact 3-heap algorithm of `P03` (`CF 730 I`) to $(a'_i, b'_i)$ with capacities $X$ and $Y$! Both methods run in $O(N \log N)$!
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Subtract $C_i$ from both $A_i$ and $B_i$ so the problem becomes choosing $X$ items for $A'$ and $Y$ disjoint items for $B'$ out of $N$.
  - *Hint 2*: Notice this reduced problem is 100% identical to `CF 730 I` (`P03`)!
  - *Hint 3*: Either run the 3-heap simulated MCMF of `P03` on $(A_i - C_i, B_i - C_i)$, or sort by $A_i - B_i$ and sweep the partition point $k \in [X, N - Y]$ with two priority queues in $O(N \log N)$.

---

#### P09 — Codeforces 802 O: April Fools' Problem (hard) (`[EN]` — WQS Binary Search + 1-Heap Simulated MCMF)
- **Judge URL**: [https://codeforces.com/problemset/problem/802/O](https://codeforces.com/problemset/problem/802/O)
- **Inline Statement & Constraints**:
  Given $N$ days ($1 \le K \le N \le 5 \cdot 10^5$), preparation costs $a_1, \dots, a_N$, and printing costs $b_1, \dots, b_N$ ($1 \le a_i, b_i \le 10^9$). Choose $K$ pairs $(i_r, j_r)$ with $i_r \le j_r$ (all $i_r$ distinct, all $j_r$ distinct) to minimize $\sum_{r=1}^K (a_{i_r} + b_{j_r})$.
- **Step 1 (Diagnostic Signal)**:
  - For $K \le 5 \cdot 10^4$, the Segment Tree Residual Augmentation of `Archetype 43.1` works in $O(K \log N)$ directly.
  - Here $K \le 5 \cdot 10^5$, so $K$ steps of global augmentation would take $O(N \log N)$, OR even simpler: since this is a Min-Cost Flow problem where the minimum cost $C(k)$ is a **convex function** of flow volume $k \in [0, N]$, we can apply **WQS Binary Search (Aliens Trick)** to remove the cardinality constraint $k = K$, and then solve the unconstrained problem in $O(N \log N)$ using a **single Min-Heap (`CF 865 D` style)**!
- **Step 2 (Algebraic WQS + 1-Heap Residual Compilation)**:
  Binary search a Lagrange multiplier $\lambda \ge 0$ subtracted from every matched pair: $\tilde{a}_i = a_i - \lambda$. Now we want to pick **any number** of pairs $(i \le j)$ to minimize $\sum (\tilde{a}_i + b_j)$ (taking all negative-cost pairs!).
  Sweep $j = 1, 2, \dots, N$ maintaining a min-heap $Q$ of available tokens:
  1. Push $(\tilde{a}_j, \text{type} = \text{FRESH})$ into $Q$ (representing $S \to j$).
  2. Look at the minimum key $v = Q.\text{top}()$. If $v + b_j < 0$, we match $v$ with $b_j$:
     - Add $v + b_j$ to `total_cost`.
     - If $v$ had `type == FRESH` (we matched a fresh $a_i$ with $b_j$), we increment `matched_count += 1`.
     - What if a later $b_k$ ($k > j$) wants to **steal $a_i$ from $b_j$**?
       $$(a_i - \lambda + b_k) - (a_i - \lambda + b_j) = b_k + (-b_j)!$$
       Notice that stealing $a_i$ from $b_j$ replaces $(i, j)$ with $(i, k)$, which **does NOT change the number of matched pairs (`matched_count += 0`)**!
     - Therefore, we push a regret token $(-b_j, \text{type} = \text{REGRET})$ into $Q$!
- **Step 3 & 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Because minimum cost $C(k)$ is convex in the flow volume $k$, penalize each pair by $-\lambda$ via WQS binary search.
  - *Hint 2*: Once $K$ is relaxed, sweep $j = 1 \dots N$ like `CF 865 D`. When $a_i - \lambda$ matches with $b_j$, what regret key allows a future $b_k$ ($k > j$) to replace $b_j$?
  - *Hint 3*: Push $(-b_j, \text{REGRET})$ into the min-heap! Only `FRESH` tokens increment the pair count $k(\lambda)$ when matched; `REGRET` tokens swap $b_j \to b_k$ with $\Delta k = 0$. Complexity: $O(N \log N \log(\max(a_i + b_j)))$.

---

#### P10 — Codeforces 348 D: Turtles (`[EN]` — LGV Lemma Non-Intersecting DAG Paths)
- **Judge URL**: [https://codeforces.com/problemset/problem/348/D](https://codeforces.com/problemset/problem/348/D)
- **Inline Statement & Constraints**:
  Given an $N \times M$ grid ($2 \le N, M \le 3000$) with passable (`.`) and blocked (`#`) cells. Two turtles start at $(1, 1)$ and walk to $(N, M)$ moving only right or down. Count the number of pairs of paths that never share any intermediate cell, modulo $10^9 + 7$.
- **Step 1 (Diagnostic Signal)**:
  - We are **counting** vertex-disjoint path pairs on a planar grid DAG, not finding a single pair (which would be 2-unit Max-Flow). This is the canonical domain of the **Lindström–Gessel–Viennot (LGV) Lemma** (`Archetype 45.4`).
- **Step 2 & 3 (Algebraic & Mechanical Compilation)**:
  - The upper-left turtle must step from $(1, 1)$ to $s_1 = (1, 2)$ and enter $(N, M)$ from $t_1 = (N - 1, M)$.
  - The lower-right turtle must step from $(1, 1)$ to $s_2 = (2, 1)$ and enter $(N, M)$ from $t_2 = (N, M - 1)$.
  - By planarity of the grid, any path $s_1 \leadsto t_2$ and any path $s_2 \leadsto t_1$ **must cross at least once**! Thus the twisted permutation $\sigma = (2, 1)$ has **zero** vertex-disjoint path pairs.
  - By the LGV Lemma, the number of vertex-disjoint path pairs $(P_1: s_1 \leadsto t_1, P_2: s_2 \leadsto t_2)$ is the $2 \times 2$ determinant:
    $$\det \begin{pmatrix} e(s_1, t_1) & e(s_1, t_2) \\ e(s_2, t_1) & e(s_2, t_2) \end{pmatrix} = e(s_1, t_1) e(s_2, t_2) - e(s_1, t_2) e(s_2, t_1) \pmod{10^9 + 7}.$$
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Fix the first step of both paths out of $(1, 1)$ as $s_1 = (1, 2), s_2 = (2, 1)$ and the last step before $(N, M)$ as $t_1 = (N-1, M), t_2 = (N, M-1)$.
  - *Hint 2*: Why is it impossible for a path $s_1 \leadsto t_2$ and a path $s_2 \leadsto t_1$ to be vertex-disjoint on a grid?
  - *Hint 3*: Run $O(NM)$ grid DP from $s_1$ and from $s_2$ to compute the four path counts $e(s_i, t_j)$ and output $e(s_1, t_1) e(s_2, t_2) - e(s_1, t_2) e(s_2, t_1) \pmod{10^9 + 7}$.

---

## 4-Tier Curated Problem Bank (Part 2: Advanced & Mastery — 10 Problems, Quarantined Templates & Multilingual Bibliography)

---

### Tier 3: Advanced (`P11`–`P15`)

#### P11 — Codeforces 280 D: k-Maximum Subsequence Sum (`[EN]` — Dynamic Segment Tree Residual Sign-Flipping MCMF)
- **Judge URL**: [https://codeforces.com/problemset/problem/280/D](https://codeforces.com/problemset/problem/280/D)
- **Inline Statement & Constraints**:
  Given an integer array $a_1, \dots, a_N$ ($1 \le N \le 10^5$, $|a_i| \le 5000$) and $M \le 10^5$ operations:
  - Type 0 (`i v`): point update $a_i \gets v$.
  - Type 1 (`L R k`): choose **at most $k$** ($1 \le k \le 20$) disjoint contiguous subarrays inside $[L, R]$ to maximize the sum of their elements.
- **Step 1 (Diagnostic Signal)**:
  - Choosing at most $k$ disjoint subarrays in $[L, R]$ is equivalent to sending at most $k$ units of flow from $S$ to $T$ in a chain network where each element $i$ is an edge $i \to i+1$ with **capacity $1$** and reward $+a_i$ (and $S \to i$ cap $1$ cost $0$, $i \to T$ cap $1$ cost $0$).
  - Because $k \le 20$ is tiny while $N, M \le 10^5$, running $k$ steps of **Successive Shortest (Maximum-Reward) Path** using a Segment Tree takes $O(k \log N)$ per query!
- **Step 2 (Algebraic / Residual Formulation)**:
  Suppose we augment 1 unit of flow along the subarray $[l^*, r^*] \subseteq [L, R]$ (choosing all elements $i \in [l^*, r^*]$).
  Because each element edge $(i \to i+1)$ has **capacity $1$**:
  - Once saturated, the forward edge $(i \to i+1)$ (reward $+a_i$) **disappears** from the residual network $G_f$!
  - In its place, the reverse residual edge $(i+1 \to i)$ (reward $-a_i$) **appears** with capacity $1$!
  - And what does traversing $(i+1 \to i)$ in a subsequent augmentation correspond to combinatorially? It **deselects (splits)** the middle of $[l^*, r^*]$, turning one subarray $[l^*, r^*]$ into two disjoint subarrays $[l^*, l' - 1]$ and $[r' + 1, r^*]$!
  Therefore, in the residual network, augmenting along $[l^*, r^*]$ is 100% equivalent to **multiplying every $a_i$ ($i \in [l^*, r^*]$) by $-1$**!
- **Step 3 (Reverse-Engineering Scratchpad)**:
  - Build a Segment Tree over $[1, N]$ where each node stores:
    - Both the **maximum subarray sum** `(max_sum, l, r)` (along with max prefix and max suffix) AND the **minimum subarray sum** `(min_sum, l, r)` (along with min prefix and min suffix), plus their exact endpoints!
    - A lazy boolean tag `flip` that negates `sum`, swaps `(max_sum, min_sum)` (with negated values and preserved endpoints), and swaps `(max_pref, min_pref)` and `(max_suff, min_suff)` in $O(1)$!
  - To answer Query `(L, R, k)`:
    - Repeat up to $k$ times: query the maximum subarray `(val, l*, r*)` in $[L, R]$. If `val <= 0`, break! Otherwise add `val` to `ans`, record $[l^*, r^*]$ on a stack, and apply `range_flip(l*, r*)`.
    - After the loop, pop all recorded intervals $[l^*, r^*]$ and apply `range_flip(l*, r*)` again to restore the Segment Tree!
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Model $k$ disjoint subarrays as $k$ units of flow on a 1D chain where each element $i$ has capacity $1$ and weight $a_i$.
  - *Hint 2*: Since capacity is $1$, saturating $[l^*, r^*]$ removes $+a_i$ and inserts $-a_i$. Why does that mean we don't even need to track flow values $f_t$ like in `CF 802 O`?
  - *Hint 3*: Maintain max/min subarray sums with endpoints in a Segment Tree supporting range multiplication by $-1$. Run $\le k$ augmentations and roll back the flips afterward in $O(k \log N)$.

---

#### P12 — Luogu P5471 / LibreOJ #3159: `[NOI2019] 弹跳` (`[ZH]` — 2D KD-Tree Implicit Out-Tree Sparsification)
- **Judge URL**: [https://loj.ac/p/3159](https://loj.ac/p/3159) / [https://www.luogu.com.cn/problem/P5471](https://www.luogu.com.cn/problem/P5471)
- **Inline Statement & Constraints**:
  There are $N$ cities ($1 \le N \le 7 \cdot 10^4$) at 2D points $(x_i, y_i)$ and $M$ jump devices ($1 \le M \le 1.5 \cdot 10^5$). Device $j$ is located at city $p_j$ and can reach **every** city inside the 2D rectangle $[L_j, R_j] \times [D_j, U_j]$ in time $t_j$. Find the shortest time from city $1$ to all cities $2, \dots, N$. Memory Limit: **128 MB**.
- **Step 1 (Diagnostic Signal)**:
  - 2D orthogonal range transitions $p_j \to [L_j, R_j] \times [D_j, U_j]$ with tight memory (`128 MB`).
  - A 2D Segment Tree Out-Tree creates $O(M \log^2 N)$ edges ($\approx 4 \cdot 10^7$ edges), exceeding `128 MB`!
  - Instead, a **2D KD-Tree** uses only $2N$ nodes (`O(N)` memory!), and by running Dijkstra directly on the KD-Tree nodes without materializing the query edges in an adjacency list, memory drops to $O(N + M)$!
- **Step 2 & 3 (Algebraic & Mechanical Compilation)**:
  - Build a 2D KD-Tree over the $N$ cities, alternating splits on $x$ and $y$ medians (`std::nth_element`). Each KD-Tree node $u$ stores its bounding box $[X_{\min}(u), X_{\max}(u)] \times [Y_{\min}(u), Y_{\max}(u)]$ and a distance upper bound `dist_box[u]` (initially $+\infty$).
  - Priority queue $Q$ stores two types of events ordered by time $d$:
    1. `(d, DEVICE_j)`: jump device $j$ fires at time $d = \text{dist}[p_j] + t_j$.
    2. `(d, KD_NODE_u)`: an entire KD-Tree subtree $u$ is reached at time $d$.
  - When `(d, DEVICE_j)` is popped, traverse the KD-Tree with rectangle $R_j = [L_j, R_j] \times [D_j, U_j]$:
    - **Pruning 1 (Disjoint)**: If $\text{Box}(u) \cap R_j = \emptyset$, return.
    - **Pruning 2 (Already Relaxed!)**: If $d \ge \text{dist\_box}[u]$, return! Because all cities in $u$'s subtree were already queued at time $\le d$!
    - **Full Cover**: If $\text{Box}(u) \subseteq R_j$, set $\text{dist\_box}[u] = d$ and push `(d, KD_NODE_u)` into $Q$; return!
  - When `(d, KD_NODE_u)` is popped (for the first time!):
    - If $u$ is a leaf (city $i$), relax $\text{dist}[i] = d$ and push all devices $j$ at city $i$ with `(d + t_j, DEVICE_j)`.
    - Otherwise, push `(d, lc(u))` and `(d, rc(u))` if $d < \text{dist\_box}[\text{child}]$.
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Why does a 2D Segment Tree exceed the 128 MB memory limit?
  - *Hint 2*: Build a 2D KD-Tree ($O(N)$ space) as an Out-Tree. How can you avoid storing the $O(M \sqrt{N})$ edges from devices to KD-Tree nodes?
  - *Hint 3*: Execute the KD-Tree range query *lazily* when the device is popped from Dijkstra's heap, and prune any KD-Tree node whose `dist_box[u]` has already been relaxed! Complexity: $O(N \log N + M \sqrt{N})$ time, $O(N + M)$ space.

---

#### P13 — Luogu P3826 / UOJ #310: `[NOI2017] 蔬菜` (`[ZH]` — Time-Reversed Simulated MCMF + Backward Flow Decrement)
- **Judge URL**: [https://uoj.ac/problem/310](https://uoj.ac/problem/310) / [https://www.luogu.com.cn/problem/P3826](https://www.luogu.com.cn/problem/P3826)
- **Inline Statement & Constraints**:
  There are $N$ types of vegetables ($1 \le N \le 10^5$). Type $i$ has per-unit value $a_i$, first-unit bonus $s_i$, initial stock $c_i$, and daily decay $x_i$ ($x_i$ units spoil at the end of each day). You can sell at most $M$ ($1 \le M \le 10$) units of vegetables per day. Given $Q \le 10^5$ independent queries $p_1, \dots, p_Q$ ($1 \le p_j \le 10^5$), find the maximum revenue over $p_j$ days for each query.
- **Step 1 (Diagnostic Signal)**:
  - Each vegetable unit of type $i$ has a **deadline day** $d \le \lceil c_i / x_i \rceil$ before which it must be sold, and each day $t \in [1, p]$ can sell at most $M$ units.
  - Because $C(f)$ is concave in the number of sold units and matching items to deadlines on a 1D timeline is a matroid / MCMF problem without cross-reversal needed when swept **backwards in time**, we can compute the optimal schedule for $P_{\max} = 10^5$ days first and then **decrement flow from $T \to S$** for smaller $p < P_{\max}$!
- **Step 2 & 3 (Algebraic & Mechanical Compilation)**:
  - **Step A (Reverse Time from Day $P_{\max} = 10^5$ down to Day $1$)**:
    Instead of vegetables *decaying* as time moves $1 \to P_{\max}$, sweep $t = P_{\max}$ down to $1$:
    - A vegetable unit whose deadline is day $d$ **arrives (becomes available)** on day $d$ as we walk backwards from $P_{\max}$ to $1$, and once available, it **never expires** for earlier days $t \le d$!
    - Maintain a max-heap $H_{\text{avail}}$ of currently available vegetables. At day $t = P_{\max}, \dots, 1$:
      1. Push all vegetables whose deadline is $\ge t$ (for the first time) into $H_{\text{avail}}$.
      2. Pop up to $M$ highest-value units from $H_{\text{avail}}$ (splitting the first unit of type $i$ with value $a_i + s_i$ from the remaining $c_i - 1$ units with value $a_i$).
  - **Step B (Answering All $p < P_{\max}$ by Reverse Residual Augmentation $T \to S$)**:
    Suppose we sold a multiset $S(P_{\max})$ of total units over $P_{\max}$ days. In the MCMF network, reducing the number of days from $p$ to $p - 1$ reduces total sink capacity from $p \cdot M$ to $(p - 1) \cdot M$!
    By the matroid greedy property of deadline scheduling, the optimal multiset of sold vegetables for $p - 1$ days is obtained from $p$ days simply by **discarding the $\max(0, |S(p)| - (p-1)M)$ cheapest sold vegetable units** using a min-heap $H_{\text{sold}}$!
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Why is moving forward in time ($t = 1 \to P_{\max}$) hard? Because you don't know which decaying vegetables to save for later days. What happens if you sweep backwards ($t = P_{\max} \to 1$)?
  - *Hint 2*: Going backwards, a vegetable with deadline $d$ becomes available at step $d$ and never expires! Run a max-heap greedy for $P_{\max} = 10^5$ days.
  - *Hint 3*: To transition from $p$ days to $p-1$ days, push all selected units into a min-heap and pop the smallest units until at most $(p-1)M$ units remain! Complexity: $O((N + P_{\max} M) \log N + Q)$.

---

#### P14 — UOJ #455: `雪灾与外卖` (`[ZH]` — 1D Line Mice & Capacitated Holes with Multiplicity Batching)
- **Judge URL**: [https://uoj.ac/problem/455](https://uoj.ac/problem/455)
- **Inline Statement & Constraints**:
  $N$ deliverymen (mice) at sorted coordinates $x_1 \le \dots \le x_N$ and $M$ restaurants (holes) at sorted coordinates $y_1 \le \dots \le y_M$ ($1 \le N, M \le 10^5$). Restaurant $j$ has capacity $c_j$ ($1 \le c_j \le 10^9$) and per-order cost $w_j$ ($0 \le w_j \le 10^9$). Sending deliveryman $i$ to restaurant $j$ costs $|x_i - y_j| + w_j$. Find the minimum total cost to match all $N$ deliverymen.
- **Step 1 (Diagnostic Signal)**:
  - Exact 1D Line Mouse-to-Hole MCMF (`Model 42.2`) with $N, M \le 10^5$ and huge hole capacities $c_j \le 10^9$.
- **Step 2 & 3 (Algebraic & Mechanical Compilation)**:
  - Apply the exact two-heap algorithm of `Model 42.2`:
    - `HoleHeap` $Q_H$ stores `(key, count)`.
    - `MouseHeap` $Q_M$ stores `(key, count)`.
  - **Mouse at $x$**:
    - Pop 1 unit of minimum key $v_H$ from $Q_H$ (if $\sum c_j < N$, return `-1`; initialize $Q_H$ with $(+\infty, N)$ for unmatched mice).
    - `ans += x + v_H`.
    - Push `(-2*x - v_H, 1)` into $Q_M$.
  - **Hole at $(y, w, c)$**:
    - Let `used = 0`. While $c - \text{used} > 0$ and `!Q_M.empty()` and $Q_M.\text{top}().\text{key} + y + w < 0$:
      - Pop `(v_M, cnt)` from $Q_M$; take $k = \min(c - \text{used}, \text{cnt})$.
      - `ans += k * (v_M + y + w)`, `used += k`.
      - Push `(-2*y - v_M, k)` into $Q_H$ (Reverse Edge A: future mouse steals this hole).
    - If `c - used > 0`: push `(-y + w, c - used)` into $Q_H$ (fresh hole capacity).
    - If `used > 0`: push `(-y - w, used)` into $Q_M$ (**all `used` mice merge into ONE single batch token!**).
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Sweep mice and holes left-to-right. Write the residual cost change when a mouse at $x$ switches from an old hole $v_H$ to a new hole at $y' \ge x$.
  - *Hint 2*: Why could a naive loop over $c_j \le 10^9$ TLE, and how do we compress it?
  - *Hint 3*: Every mouse that enters Hole $y$ receives the **exact same** re-steal key $-y - w$ regardless of its previous history! Merging all `used` mice at Hole $y$ into a single `(key = -y - w, count = used)` pair bounds total heap pushes by $O(N + M)$.

---

#### P15 — Codeforces 1089 B: Chattering (`[EN]` — General Non-Bipartite Matching Capacity-2 Student Gadget)
- **Judge URL**: [https://codeforces.com/problemset/problem/1089/B](https://codeforces.com/problemset/problem/1089/B)
- **Inline Statement & Constraints**:
  Given $N$ students and $M$ benches ($1 \le N, M \le 150$) with a bipartite adjacency matrix between students and benches. Connect pairs of vertices using edges of the graph such that each bench has degree $\le 1$, each student has degree $\le 2$, and the graph is decomposed into the maximum number of connected components of size $\ge 2$ (equivalently: each component can be reduced to either a single edge `(student, bench)` or a 3-vertex path `(bench 1 - student - bench 2)` where **only the two benches count as a matched pair**, wait: in `CF 1089 B`, we want to pair up vertices into disjoint paths of length 1 or 2? No: in `CF 1089 B`, two people can "chatter" either if they are in the same row/column; specifically, vertices in set $A$ (size $N$) have capacity $2$ and can match with each other via an internal edge, while vertices in set $B$ (size $M$) have capacity $1$!).
  Let us state the exact mathematical model of `CF 1089 B`:
  - Each of the $N$ rows (students) has **two seats** $u_{i,1}, u_{i,2}$ that can talk to each other: edge $(u_{i,1}, u_{i,2})$.
  - Each of the $M$ columns (benches) has **one vertex** $v_j$.
  - If row $i$ and column $j$ are connected, add edges $(u_{i,1}, v_j)$ and $(u_{i,2}, v_j)$.
  - Find the **Maximum Matching** in this $(2N + M)$-vertex non-bipartite graph, and output $|M_{\max}| - N$!
- **Step 1, 2 & 3 (Diagnostic Signal & Compilation)**:
  - Why does $|M_{\max}| - N$ count the maximum number of column-pairs plus unmatched row-pairs?
    In row $i$, the two vertices $u_{i,1}, u_{i,2}$ are connected by $(u_{i,1}, u_{i,2})$:
    - If $0$ columns match with row $i$: $(u_{i,1}, u_{i,2})$ is matched $\implies$ row $i$ contributes **$1$** edge.
    - If $1$ column matches with row $i$: one of $u_{i,1}, u_{i,2}$ matches with the column and the other stays exposed $\implies$ row $i$ still contributes **$1$** edge!
    - If $2$ columns match with row $i$: both $u_{i,1}$ and $u_{i,2}$ match with columns $\implies$ row $i$ contributes **$2$** edges!
    Thus each row always contributes at least $1$ edge, and contributes $+1$ extra edge **if and only if it pairs two distinct columns together**!
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Split each row $i$ into two vertices $u_{i,1}, u_{i,2}$. How do you ensure that matching only 1 column to row $i$ gives zero net gain over matching 0 columns to row $i$?
  - *Hint 2*: Add the edge $(u_{i,1}, u_{i,2})$ between the two copies of row $i$!
  - *Hint 3*: Run Edmonds' Blossom on the $2N + M \le 450$ vertices and output $|M_{\max}| - N$.

---

### Tier 4: Mastery (`P16`–`P20`)

#### P16 — ICPC World Finals 2018 C / Luogu P6943: Conquer the World (`[EN]` — Tree MCMF via Mergeable Heaps)
- **Judge URL**: [https://www.luogu.com.cn/problem/P6943](https://www.luogu.com.cn/problem/P6943) / [https://open.kattis.com/problems/conquertheworld](https://open.kattis.com/problems/conquertheworld)
- **Inline Statement & Constraints**:
  Given a weighted tree with $N$ vertices ($1 \le N \le 2.5 \cdot 10^5$, edge weights $1 \le w_e \le 10^6$). Vertex $u$ currently has $x_u$ armies and requires at least $y_u$ armies ($\sum y_u \le 10^6$). Moving 1 army across edge $e$ costs $w_e$. Find the minimum total cost to satisfy all vertex requirements.
- **Step 1 (Diagnostic Signal)**:
  - Minimum-cost flow on a tree with $N = 2.5 \cdot 10^5$. Explicit MCMF is $O(N^2)$, so we must use **Tree Simulated MCMF via Mergeable Heaps** (`Model 42.3`).
- **Step 2 & 3 (Algebraic & Mechanical Compilation)**:
  - Root the tree at $1$ and compute root distances $d(u)$.
  - For each vertex $u$:
    - If $x_u > y_u$: push $x_u - y_u$ units of supply into $Q_{\text{sup}}(u)$ with key $v_S = d(u)$.
    - If $y_u > x_u$: push $y_u - x_u$ units of mandatory demand into $Q_{\text{dem}}(u)$ with key $v_D = d(u) - M$ (where $M = 10^{12}$).
  - In post-order DFS at $L$:
    1. Merge children's Leftist Heaps (or small-to-large `std::priority_queue` with multiplicity batching) into $Q_{\text{sup}}(L)$ and $Q_{\text{dem}}(L)$.
    2. While both heaps are non-empty and $v_S + v_D - 2 d(L) < 0$:
       - Match $k = \min(\text{cnt}_S, \text{cnt}_D)$ units, adding $k \cdot (v_S + v_D - 2 d(L))$ to `total_cost`.
       - Push $k$ supply-regret tokens with key $2 d(L) - v_D$ into $Q_{\text{sup}}(L)$.
       - Push $k$ demand-regret tokens with key $2 d(L) - v_S$ into $Q_{\text{dem}}(L)$.
  - Final answer: `total_cost + M * sum_of_positive(y_u - x_u)`.
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Rewrite tree distance as $\text{dist}(u, v) = d(u) + d(v) - 2 d(\text{lca}(u, v))$ and penalize every unsatisfied demand by $-M$ ($M = 10^{12}$).
  - *Hint 2*: When $v_S$ and $v_D$ match at LCA $L$ with cost $\Delta = v_S + v_D - 2d(L)$, what regret key allows an ancestor $L'$ of $L$ to re-match $v_S$ with a new demand $v'_D$ at total cost $v_S + v'_D - 2d(L')$?
  - *Hint 3*: Push $2d(L) - v_D$ into $Q_{\text{sup}}(L)$ and $2d(L) - v_S$ into $Q_{\text{dem}}(L)$! Use `__int128_t` for `total_cost` to avoid 64-bit overflow when multiplying $M = 10^{12}$ by $\sum y_u = 10^6$.

---

#### P17 — Luogu P5470 / LibreOJ #3158: `[NOI2019] 序列` (`[ZH]` — 5-Heap Coupled Bipartite State Automaton)
- **Judge URL**: [https://loj.ac/p/3158](https://loj.ac/p/3158) / [https://www.luogu.com.cn/problem/P5470](https://www.luogu.com.cn/problem/P5470)
- **Inline Statement & Constraints**:
  Given two positive integer arrays $a_1, \dots, a_N$ and $b_1, \dots, b_N$ ($1 \le L \le K \le N \le 2 \cdot 10^5$, $1 \le a_i, b_i \le 10^9$) across $T$ test cases ($\sum N \le 10^6$). Choose $I, J \subseteq \{1, \dots, N\}$ with $|I| = |J| = K$ and $|I \cap J| \ge L$ to maximize $\sum_{i \in I} a_i + \sum_{j \in J} b_j$.
- **Step 1, 2 & 3 (Diagnostic Signal & Compilation)**:
  - Follow the complete 4-Step derivation of `Archetype 43.2`:
    - Build the 5 max-heaps $H_{a0}, H_{b0}, H_{ab}, H_{a1}, H_{b1}$ and set `free_cap = K - L`.
    - For each of the $K$ augmentations, evaluate the 5 residual paths (Cand 1 enabled iff `free_cap > 0`), take the maximum gain, update the 2-bit state `st[i] \in {0, 1, 2, 3}` of the affected index/indices, adjust `free_cap` (`-1` if Cand 1 with $i \neq j$; `+1` if Cand 5; `0` otherwise), and push updated states into the heaps!
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Model $|I \cap J| \ge L$ as a bridge $P \to Q$ of capacity $K - L$ for uncoupled pairs, alongside direct edges $u_i \to v_i$ of capacity $1$ for coupled pairs.
  - *Hint 2*: Classify every index into 4 states `(0,0), (1,0), (0,1), (1,1)` and list all simple $S \to T$ paths in the residual network.
  - *Hint 3*: Don't forget Candidate 5 (matching $a_i$ from state `01` with $b_j$ from state `10`), which pushes flow backwards across $Q \to P$ and increments `free_cap += 1`! Complexity: $O(N \log N)$.

---

#### P18 — Gallai–Edmonds Non-Bipartite Walk Game (`[EN]`/`[ZH]` — `JSOI2009 游戏` on General Graphs / `CF Gym 101981`)
- **Judge / Benchmark Reference**: Non-Bipartite Generalization of `Luogu P4055 [JSOI2009] 游戏` & `AtCoder ABC 354 G` on General Undirected Graphs ($V \le 500, E \le V^2/2$).
- **Inline Statement & Constraints**:
  Given a general undirected graph $G = (V, E)$ with $V \le 500$ vertices (which may contain odd cycles). Two players (Alice and Bob) play a game: Alice places a token on a starting vertex $s \in V$, and then Bob and Alice alternately move the token along an edge to a previously unvisited vertex. The player who cannot make a move loses. Find **all** starting vertices $s \in V$ for which Alice (the player who chooses $s$, i.e., Bob moves first from $s$) wins!
- **Step 1 (Diagnostic Signal)**:
  - On bipartite graphs, Dulmage–Mendelsohn decomposition finds all vertices in $D(G)$ (missed by some maximum matching) via alternating BFS.
  - On general graphs with odd cycles, running Edmonds' Blossom $V$ separate times on $G \setminus \{s\}$ takes $O(V^2 E \alpha(V))$, whereas **one single Gallai–Edmonds Alternating Forest pass** after finding $M_{\max}$ takes $O(V E \alpha(V))$!
- **Step 2 & 3 (Algebraic & Mechanical Compilation)**:
  1. Run Edmonds' Blossom algorithm once to compute a maximum matching $M_{\max}$ of $G$.
  2. Reset `tp[1..V] = 0`, `pre[1..V] = 0`, `dsu[i] = i`, and empty the queue $Q$.
  3. **Simultaneous Multi-Source Blossom Forest**: For **every** currently exposed vertex $r$ (`match[r] == 0`), set `tp[r] = 1` (Outer) and push $r$ into $Q$!
  4. Run the exact same Blossom BFS loop (contracting blossoms via `contract(u, v, b)` whenever an edge $(u, v)$ connects two `Type 1` vertices with `find(u) != find(v)`, and advancing through `tp[v] = 2 -> tp[match[v]] = 1`). Since $M_{\max}$ is already maximum, no augmenting path will be found!
  5. When the queue empties, the set of vertices with `tp[s] == 1` is **precisely the Gallai–Edmonds set $D(G)$** (vertices missed by at least one maximum matching)!
     - Bob (who moves first from $s$) wins $\iff s \notin D(G) \iff \text{tp}[s] \neq 1$.
     - Alice (who wants Bob to have no winning response from $s$) wins $\iff s \in D(G) \iff \text{tp}[s] == 1$.
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: A starting vertex $s$ is a losing position for the player moving out of $s$ if and only if $G$ has a maximum matching that leaves $s$ unmatched ($s \in D(G)$).
  - *Hint 2*: How does a vertex $s$ get left unmatched by some maximum matching $M'$? By lying at the end of an even-length $M_{\max}$-alternating path from an $M_{\max}$-exposed vertex!
  - *Hint 3*: After finding one maximum matching $M_{\max}$, push ALL exposed vertices into the Blossom BFS queue as `Type 1` roots simultaneously and contract blossoms as usual. Every vertex ending with `tp[s] == 1` belongs to $D(G)$!

---

#### P19 — Tree Path Project Selection via Heavy-Light Decomposition + Prefix Hub Sparsification (`[ZH]`/`[EN]` — `HLD + Min-Cut`)
- **Judge / Benchmark Reference**: Tree Path Maximum Weight Closure (`CF Gym 102483` / `Luogu P4092` + `Project Selection` / `BZOJ 4873` Tree Path Variant).
- **Inline Statement & Constraints**:
  Given a tree $T$ with $N \le 2 \cdot 10^4$ vertices where activating vertex $u$ costs $c_u \ge 0$, and $M \le 2 \cdot 10^4$ projects where project $i$ yields profit $w_i \ge 0$ if and only if **every vertex on the simple tree path $u_i \leftrightarrow v_i$ is activated**. Find the maximum net profit.
- **Step 1 (Diagnostic Signal)**:
  - Maximum Weight Closure (`最大权闭合子图`): $S \xrightarrow{w_i} P_i$, $u \xrightarrow{c_u} T$, and $P_i \xrightarrow{\infty} x$ for all $x \in \text{path}(u_i, v_i)$.
  - Using naive Heavy-Light Decomposition (`树剖`) + Segment Tree Out-Tree creates $O(M \log^2 N)$ edges because each path splits into $O(\log N)$ heavy-chain intervals and each interval splits into $O(\log N)$ segment tree nodes.
  - Can we shave a full $\log N$ factor down to $O(N \log N + M \log N)$ edges? **Yes — via Heavy-Chain Prefix + Sparse Table / SegTree!**
- **Step 2 & 3 (Algebraic & Mechanical Compilation)**:
  - Observe that in HLD, a tree path $u_i \leftrightarrow v_i$ consists of:
    1. At most $O(\log N)$ **prefix intervals** $[\text{dfn}[\text{top}[x]], \text{dfn}[x]]$ starting at the **top of a heavy chain**!
    2. At most **one** general interval $[\text{dfn}[x], \text{dfn}[y]]$ at the LCA heavy chain that does *not* start at the chain top!
  - Therefore:
    - Along each heavy chain with top $h$, build a simple **1D Prefix Out-Chain**: $\text{Pref}(p) \xrightarrow{\infty} \text{Pref}(p-1)$ and $\text{Pref}(p) \xrightarrow{\infty} p$. Now any prefix $[\text{dfn}[h], \text{dfn}[x]]$ is covered by **a single edge** $P_i \xrightarrow{\infty} \text{Pref}(\text{dfn}[x])$ ($O(1)$ per heavy step instead of $O(\log N)$!)
    - For the single final LCA interval $[\text{dfn}[x], \text{dfn}[y]]$, decompose it in the global 1D Segment Tree Out-Tree using $O(\log N)$ edges!
  - Total vertices: $3N$. Total edges per project: **$O(\log N)$ instead of $O(\log^2 N)$**!
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Standard HLD splits a path into $O(\log N)$ intervals, and a Segment Tree splits each interval into $O(\log N)$ nodes, giving $O(M \log^2 N)$ edges. Look closer at the $O(\log N)$ HLD intervals: what do all but one of them have in common?
  - *Hint 2*: Every HLD interval except the last LCA interval is a **prefix of a heavy chain** starting at `top[x]`!
  - *Hint 3*: Build prefix hub nodes along each heavy chain ($O(N)$ vertices/edges total) so each heavy-chain climb adds only $1$ edge, and use the Segment Tree Out-Tree only once for the final LCA segment! Total edges: $O((N + M) \log N)$.

---

#### P20 — Maximum-Weight Matchable Vertex Subset via Randomized Tutte Matrix Basis (`[EN]`/`[ZH]` — `CF Gym 102155 J` / Algebraic Matching Matroid)
- **Judge URL**: [https://codeforces.com/gym/102155/problem/J](https://codeforces.com/gym/102155/problem/J) (Petrozavodsk / Algebraic General Matching Benchmark)
- **Inline Statement & Constraints**:
  Given a general undirected graph $G = (V, E)$ ($1 \le V \le 500$) where each vertex $v \in V$ has a non-negative weight $w_v$. A subset $S \subseteq V$ is called **matchable** if there exists a matching $M \subseteq E$ in $G$ that covers every vertex in $S$ (note: edges in $M$ may have one endpoint in $S$ and the other endpoint in $V \setminus S$). Find the maximum possible weight $\sum_{v \in S} w_v$ of a matchable subset $S$ (and construct $S$).
- **Step 1 (Diagnostic Signal)**:
  - By a classic theorem of Edmonds & Fulkerson (1965), the family of matchable vertex subsets $\mathcal{I} = \{S \subseteq V : S \text{ is covered by some matching in } G\}$ forms a **Matroid** (a **Matching Matroid**)!
  - Therefore, the greedy algorithm works: sort vertices $v_1, v_2, \dots, v_V$ in decreasing order of weight $w_v$, maintain $S$, and add $v_k$ to $S$ if $S \cup \{v_k\}$ is still covered by some matching.
  - How do we test whether $S \cup \{v_k\}$ is covered by a matching across all $V$ steps in $O(V^3)$ total time? Via **Gaussian Elimination on the rows of the Skew-Symmetric Tutte Matrix $T(x)$** (`Theorem 45.3`)!
- **Step 2 & 3 (Algebraic & Mechanical Compilation)**:
  1. Construct the $V \times V$ Tutte matrix $T$ over $\mathbb{F}_p$ ($p = 998244353$): for each $(u, v) \in E$ with $u < v$, pick $x_{u,v} \in [1, p-1]$ uniformly at random and set $T_{u,v} = x_{u,v}, T_{v,u} = p - x_{u,v}$.
  2. By **Theorem 45.3(4)** (Lovász 1979), a subset $S \subseteq V$ is covered by some matching in $G$ **if and only if the rows $\{T_{u, *} : u \in S\}$ are linearly independent over $\mathbb{F}_p$** (with probability $\ge 1 - V/p$)!
     *Why?* Because if $M$ covers $S$, restricting $T$ to the $2|M| \times 2|M|$ principal submatrix $T[V(M), V(M)]$ gives an invertible matrix of full rank $2|M|$, so all $2|M|$ of its rows—and in particular the $|S|$ rows indexed by $S \subseteq V(M)$—are linearly independent!
  3. Sort vertices $v_1, \dots, v_V$ so $w_{v_1} \ge w_{v_2} \ge \dots \ge w_{v_V}$.
  4. Maintain a standard **Linear Basis** `basis[1..V]` of row vectors of length $V$ over $\mathbb{F}_p$. For each $v_k$ in sorted order, attempt to insert row $T_{v_k, *}$ into the linear basis (`O(V^2)` per vertex). If it is linearly independent of the current basis, add $v_k$ to $S$ and add $w_{v_k}$ to the answer!
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Matchable vertex subsets form a Matroid, so you can greedily insert vertices in decreasing order of $w_v$.
  - *Hint 2*: How does the Skew-Symmetric Tutte Matrix $T(x)$ characterize whether a subset of vertices $S \subseteq V$ can be simultaneously covered by a matching?
  - *Hint 3*: $S$ is matchable if and only if the rows of $T(x)$ indexed by $S$ are linearly independent! Run a single $O(V^3)$ Gaussian elimination basis pass over $\mathbb{F}_{998244353}$ in decreasing order of $w_v$.

---

## Quarantined Bare-Template Problems (`R-41`–`R-48`)

Per `flows_research/PLAN.md` Section 1.2, bare template verification problems that require zero non-graph modelling are quarantined from the main problem ladder into the reference table below:

| Quarantine ID | Problem Name & Judge URL | Template Category | Reason for Quarantine |
| :--- | :--- | :--- | :--- |
| **`R-41`** | [Luogu P6123 — 【模板】一般图最大匹配](https://www.luogu.com.cn/problem/P6123) | Unweighted Edmonds' Blossom (`带花树`) | Direct textbook call to unweighted Blossom solver on an explicit undirected graph. |
| **`R-42`** | [Library Checker — Matching on General Graph](https://judge.yosupo.jp/problem/general_matching) | Unweighted Edmonds' Blossom / Tutte Matrix | Explicit graph input ($N \le 500$); zero modelling required. |
| **`R-43`** | [UOJ #79 — 一般图最大匹配](https://uoj.ac/problem/79) | Unweighted Edmonds' Blossom (`带花树`) | Standard benchmark template for $O(VE \alpha(V))$ Blossom verification. |
| **`R-44`** | [Luogu P6699 / UOJ #81 — 一般图最大权匹配](https://uoj.ac/problem/81) | Weighted Edmonds' Blossom (`带权带花树`) | Direct verification of $O(V^3)$ primal–dual weighted Blossom template. |
| **`R-45`** | [Library Checker — Maximum Weight Matching](https://judge.yosupo.jp/problem/general_weighted_matching) | Weighted Edmonds' Blossom | Bare template verification for general weighted matching. |
| **`R-46`** | [LGV Lemma Template — Luogu P7736 `[NOI2021] 路径交点`](https://www.luogu.com.cn/problem/P7736) | Layered LGV Determinant Parity | Direct parity determinant $\prod \det(M_k)$ across layered bipartite graphs. |
| **`R-47`** | [Luogu P6577 — 【模板】二分图最大权完美匹配](https://www.luogu.com.cn/problem/P6577) | Kuhn–Munkres (`KM`) | Standard bipartite weighted matching template. |
| **`R-48`** | [BZOJ 4152 / Simple 1D Prefix Graph Template](https://www.luogu.com.cn/problem/P4152) | 1D Coordinate Sorting Shortest Path | Direct sorting along $x$ and $y$ axes without flow/cut interaction. |

---

## Multilingual Bibliography & Seminal References (`[EN]` / `[ZH]` / `[JA]`)

### 1. English Sources (`[EN]`)
- **[Edmonds 1965a]** Jack Edmonds, *"Paths, trees, and flowers"*, Canadian Journal of Mathematics, 17: 449–467, 1965. (The foundational paper introducing the Blossom Contraction Algorithm and the polynomial-time barrier ("good algorithms")).
- **[Edmonds 1965b]** Jack Edmonds, *"Maximum matching and a polyhedron with 0,1-vertices"*, Journal of Research of the National Bureau of Standards, 69B: 125–130, 1965. (Establishes the Odd-Set Blossom Inequalities and LP duality for weighted non-bipartite matching).
- **[Tutte 1947]** W. T. Tutte, *"The factorization of linear graphs"*, Journal of the London Mathematical Society, 22: 107–111, 1947. (Introduces the Skew-Symmetric Tutte Matrix $T(x)$ and the Tutte 1-Factor Theorem).
- **[Lovász 1979]** László Lovász, *"On determinants, matchings, and random algorithms"*, Fundamentals of Computation Theory (FCT), 1979. (Proves $\text{rank}(T(x)) = 2 \nu(G)$ and the randomized polynomial identity testing algorithm for matching rank).
- **[Rabin & Vazirani 1989]** Michael O. Rabin and Vijay V. Vazirani, *"Maximum matchings in general graphs through randomization"*, Journal of Algorithms, 10(4): 557–567, 1989. (Shows how $T^{-1}$ identifies allowed edges and constructs perfect matchings in $O(V^3)$ randomized algebraic time).
- **[Lindström 1973 / Gessel–Viennot 1985]** Bernt Lindström (1973) and Ira Gessel & Xavier Gérard Viennot, *"Binomial determinants, paths, and hook length formulae"*, Advances in Mathematics, 58(3): 300–321, 1985. (The LGV Lemma for non-intersecting DAG paths).
- **[Gabow 1976 / Tarjan 1983]** Harold N. Gabow, *"An efficient implementation of Edmonds' algorithm for maximum matching on graphs"*, JACM, 1976; Robert E. Tarjan, *Data Structures and Network Algorithms*, SIAM, 1983 (DSU-accelerated $O(VE \alpha(V))$ blossom contraction).

### 2. Chinese Competitive Programming Treatises (`[ZH]`)
- **[国家集训队论文 2018 — 模拟费用流]** 陈胤伯 (Yinbo Chen) / 姜志豪 / 王修涵, *《浅谈模拟费用流问题》 (On Simulated Min-Cost Flow Problems)*, IOI China National Training Team Monograph (`国家集训队论文`), 2017–2019. (Systematizes 1D Mouse-to-Hole heaps, Tree LCA mergeable heaps, Segment Tree residual maintenance, and Multi-Queue Coupled State Automata).
- **[国家集训队论文 2016–2019 — 数据结构优化建图]** *《数据结构优化建图在网络流中的应用》*, Chinese National Team & Winter Camp (`WC`) Lecture Notes. (Covers Segment Tree In/Out-Trees, Persistent Segment Tree prefix dominance `BZOJ 3218`, CDQ Divide-and-Conquer value chains `[SNOI2019] 通信`, and KD-Tree pruning `[NOI2019] 弹跳`).
- **[WC2016 — 带花树与一般图匹配]** 陈松扬 (Songyang Chen) & UOJ Community, *《一般图匹配及其应用（带花树与 Tutte 矩阵）》*, Winter Camp 2016 (`[WC2016] 挑战 NPC` official analysis and DSU blossom implementation guide).

### 3. Japanese Competitive Programming Treatises (`[JA]`)
- **[noshi91 — 燃やす埋める & データ構造による辺数削減]** `noshi91`, *"区間への辺張りと燃やす埋める (Segment Tree Edge Compression in Project Selection Min-Cut)"*, 2019–2021.
- **[maspypy — 模擬最小費用流 / 反悔貪欲]** `maspypy`, *"最小費用流のシミュレーションと Slope Trick (Simulated Min-Cost Flow, Regret Greedy, and Slope Trick on Trees)"*, maspy's HP, 2020–2023.
- **[tatyam / snuke — 一般マッチングと Tutte 行列]** `tatyam` & `snuke`, *"Tutte 行列を用いた一般グラフマッチングとマトロイド基底 (General Graph Matching and Matroid Bases via the Tutte Matrix)"*, AtCoder Editorial & Kyopro Encyclopedia.


---

## Appendix A: Additional Synthesis Problems (`P21`–`P22`)

#### P21 — Luogu P4098 / 0-1 Trie + Flow Synthesis: XOR-Bounded Bipartite Assignment (`[ZH]`/`[EN]` — 0-1 Binary Trie Out-Tree Sparsification)
- **Judge / Benchmark Reference**: 0-1 Trie Graph Sparsification Archetype (`Architecture 41.4`, generalizing `Luogu P4098 [HEOI2013] ALO` / `CF 888 G` to Capacitated Flow / Min-Cut).
- **Inline Statement & Constraints**:
  Given $N$ left items with $B$-bit integer keys $a_1, \dots, a_N$ and $N$ right items with $B$-bit integer keys $b_1, \dots, b_N$ ($1 \le N \le 2 \cdot 10^4, B = 30$), plus an integer threshold $K$. Left item $i$ (supply $c_i$, profit $w_i$) can match with right item $j$ (capacity $d_j$) **if and only if $(a_i \oplus b_j) \le K$**. Maximize the total matched profit (or compute the Minimum Cut when each chosen $i$ forces all $j$ with $a_i \oplus b_j \le K$ to be chosen).
- **Step 1 (Diagnostic Signal)**:
  - The condition $(a_i \oplus b_j) \le K$ defines a subset of right items $j$ for each $i$, creating $\Theta(N^2)$ edges naively.
  - Because bitwise XOR comparison $(a_i \oplus b_j) \le K$ branches on the first bit position $t \in \{B-1, \dots, 0\}$ where $(a_i \oplus b_j)$ is strictly less than $K$, the set of valid $b_j$ is a disjoint union of **at most $B + 1$ complete subtrees of a 0-1 Binary Trie**!
- **Step 2 & 3 (Algebraic & Mechanical Compilation)**:
  1. Insert all right keys $b_1, \dots, b_N$ into a **0-1 Binary Trie** of depth $B = 30$.
  2. Convert the Trie into an **Out-Tree**: for every internal Trie node $p$ and bit $c \in \{0, 1\}$, add directed edge:
     $$\text{Trie}(p) \xrightarrow{\text{cap} = \infty, \text{cost} = 0} \text{Trie}(\text{ch}[p][c]).$$
     At each leaf corresponding to value $b_j$, add $\text{Trie}(\text{leaf}(b_j)) \xrightarrow{\text{cap} = \infty, \text{cost} = 0} j_{\text{right}}$.
  3. For each left item $i$, walk down the Trie from the root for bit $t = B-1$ down to $0$:
     - Let $\text{bit}_t(a_i) \in \{0, 1\}$ and $\text{bit}_t(K) \in \{0, 1\}$.
     - **If $\text{bit}_t(K) == 1$**:
       - Any $b_j$ that takes branch $c = \text{bit}_t(a_i)$ has $(a_i \oplus b_j)$ bit $t$ equal to $0 < 1 = \text{bit}_t(K)$, so **every element in the subtree $\text{ch}[p][\text{bit}_t(a_i)]$ satisfies $a_i \oplus b_j < K$**! Add a single directed edge:
         $$i_{\text{left}} \xrightarrow{\text{cap} = \infty, \text{cost} = 0} \text{Trie}\big(\text{ch}[p][\text{bit}_t(a_i)]\big).$$
       - Then continue walking down $p \gets \text{ch}[p][\text{bit}_t(a_i) \oplus 1]$ (where bit $t$ of $a_i \oplus b_j$ equals $1 = \text{bit}_t(K)$).
     - **If $\text{bit}_t(K) == 0$**:
       - We are forced to match bit $t$: move $p \gets \text{ch}[p][\text{bit}_t(a_i)]$.
     - If $p$ reaches a leaf at $t = 0$ (meaning $a_i \oplus b_j = K$), add $i_{\text{left}} \xrightarrow{\infty, 0} \text{Trie}(p)$.
  - Total vertices: $\le N B = 6 \cdot 10^5$. Total edges: $\le 2 N B = 1.2 \cdot 10^6$.
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: How do you count elements $b_j$ with $a_i \oplus b_j \le K$ using a 0-1 Trie?
  - *Hint 2*: Notice that the $O(\log V)$ Trie subtrees summed during a standard XOR-range query are static subtrees of the Trie!
  - *Hint 3*: Turn the 0-1 Trie into an Out-Tree ($\text{parent} \xrightarrow{\infty} \text{child}$) and connect each $i$ to the $O(\log V)$ subtree roots where $a_i \oplus b_j \le K$.

---

#### P22 — Tutte's General $b$-Matching & Degree-Interval Subgraph Gadget (`[EN]`/`[ZH]` — `UOJ / CF 1510 H / General Degree-Constrained Subgraph`)
- **Judge / Benchmark Reference**: Tutte's Reduction of General Capacitated $[l_v, r_v]$-Factor to Unweighted 1-Matching (`Edmonds' Blossom` / `Tutte 1954`).
- **Inline Statement & Constraints**:
  Given a general undirected graph $G = (V, E)$ ($V \le 100, E \le 400$) and degree bounds $[l_v, r_v]$ for each vertex $v \in V$ ($\sum r_v \le 500$). Determine whether $G$ has a spanning subgraph $H = (V, F)$ ($F \subseteq E$) such that every vertex $v$ has degree $d_H(v) \in [l_v, r_v]$ (and find one if it exists, or maximize $\sum_{v} d_H(v)$ subject to $d_H(v) \le r_v$).
- **Step 1 (Diagnostic Signal)**:
  - Because $G$ is non-bipartite, degree-bounded subgraph (`b-matching`) cannot be solved with circulation with lower bounds (`上下界网络流`) — a directed circulation would send $0.5$ flow around odd cycles!
  - We must reduce general $[l_v, r_v]$-factor to **Standard Unweighted 1-Matching (`Edmonds' Blossom`)** via **Tutte's Vertex-Edge Splitting Gadget**!
- **Step 2 & 3 (Algebraic & Mechanical Compilation)**:
  1. **Splitting Edges**: Every original edge $e = (u, v) \in E$ is split into **two half-edges** $e_u$ and $e_v$ connected by an edge $(e_u, e_v)$:
     - If $e \in F$ (chosen in the subgraph), then $e_u$ matches with a slot of $u$ and $e_v$ matches with a slot of $v$.
     - If $e \notin F$ (not chosen in the subgraph), then $e_u$ and $e_v$ **match with each other** via $(e_u, e_v)$!
  2. **Splitting Vertices with Degree Bound $d_H(v) \in [l_v, r_v]$**:
     Create $r_v$ slot vertices $s_{v,1}, s_{v,2}, \dots, s_{v,r_v}$ for vertex $v$, and connect every slot $s_{v,k}$ ($1 \le k \le r_v$) to all incident half-edges $\{e_v : e \in \delta(v)\}$.
     Now: how do we allow $r_v - l_v$ of these slots to remain unused (so $d_H(v)$ can be anything between $l_v$ and $r_v$) while requiring a **Perfect Matching** on the constructed graph?
     - Add $r_v - l_v$ **absorber vertices** $a_{v,1}, \dots, a_{v, r_v - l_v}$ connected to all $r_v$ slots of $v$ (if $r_v - d_H(v)$ must have the same parity, connect internal edges $(s_{v, 2t-1}, s_{v, 2t})$ on the last $\lfloor (r_v - l_v)/2 \rfloor$ pairs; if arbitrary parity is allowed across all vertices, connect a global parity pad or split each absorber!).
     - Even simpler, if we want **Maximum $b$-Matching** ($0 \le d_H(v) \le r_v$ maximizing $|F|$): we don't even need edge-splitting when $E$ is small, OR with edge-splitting $(e_u, e_v)$ and $r_v$ slots per vertex (no absorbers needed!), look at any matching $M$ that saturates all half-edges: wait — each edge $e = (u, v)$ contributes **1** matched edge $(e_u, e_v)$ if $e \notin F$, and **2** matched edges ($(u\text{-slot}, e_u)$ and $(v\text{-slot}, e_v)$) if $e \in F$!
     - Therefore, the maximum number of edges in a valid $b$-matching ($d_H(v) \le r_v$) is **literally $|M_{\max}| - |E|$**!
- **Step 4 (Complete Solution & 3-Tier Hints)**:
  - *Hint 1*: Split each edge $e = (u, v)$ into two vertices $e_u, e_v$ connected by $(e_u, e_v)$.
  - *Hint 2*: Create $r_v$ copies of each vertex $v$, all connected to $e_v$ for $e \in \delta(v)$. Compare the number of matched edges contributed by $e$ when $e \notin F$ vs. when $e \in F$.
  - *Hint 3*: When $e \notin F$, $(e_u, e_v)$ contributes $1$ to $|M|$. When $e \in F$, both $e_u$ and $e_v$ match to vertex slots, contributing $2$ to $|M|$! Thus $|F_{\max}| = |M_{\max}| - |E|$.

---

## Appendix B: Self-Contained Algorithmic Contracts & Verification Blueprints

Per `AGENTS.md`, we omit boilerplate Dinic/SSP templates and provide the **non-standard structural compilation contracts** for the five core mechanisms of Wave 5A.

### Contract 1: Persistent Segment Tree Out-Tree Sparsification (`BZOJ 3218`)
```cpp
// Invariant: root[i] is an Out-Tree over value domain [1, U] containing {1..i}.
// Every new node p_new links to p_old so duplicate values a_j = a_i remain reachable!
int insert_pst(int p_old, int L, int R, int pos, int vertex_id) {
    int p_new = ++tot_nodes;
    lc[p_new] = lc[p_old];
    rc[p_new] = rc[p_old];
    if (p_old) add_edge(p_new, p_old, INF); // CRITICAL: preserves reachability to older versions!
    if (L == R) {
        add_edge(p_new, vertex_id, INF);
        return p_new;
    }
    int mid = (L + R) >> 1;
    if (pos <= mid) {
        lc[p_new] = insert_pst(lc[p_old], L, mid, pos, vertex_id);
        add_edge(p_new, lc[p_new], INF);
    } else {
        rc[p_new] = insert_pst(rc[p_old], mid + 1, R, pos, vertex_id);
        add_edge(p_new, rc[p_new], INF);
    }
    return p_new;
}
```

### Contract 2: 1D Line Mice & Capacitated Holes Two-Heap Simulation (`UOJ #455`)
```cpp
// Q_H, Q_M: min-heaps of pair<long long, long long> (key, multiplicity).
void process_mouse(long long x) {
    auto [v_H, cnt] = Q_H.top(); Q_H.pop();
    if (cnt > 1) Q_H.push({v_H, cnt - 1});
    total_cost += x + v_H;
    Q_M.push({-2LL * x - v_H, 1}); // Mouse regret key: -x - (x + v_H) = -2x - v_H
}

void process_hole(long long y, long long w, long long cap) {
    long long used = 0;
    while (used < cap && !Q_M.empty() && Q_M.top().first + y + w < 0) {
        auto [v_M, cnt] = Q_M.top(); Q_M.pop();
        long long k = min(cap - used, cnt);
        if (cnt > k) Q_M.push({v_M, cnt - k});
        total_cost += (__int128)k * (v_M + y + w);
        used += k;
        Q_H.push({-2LL * y - v_M, k}); // Reverse Edge A: future mouse steals this hole
    }
    if (cap > used) Q_H.push({-y + w, cap - used}); // Unused fresh hole capacity
    if (used > 0)   Q_M.push({-y - w, used});       // Reverse Edge B: batch re-steal token!
}
```

### Contract 3: DSU Lazy Blossom Contraction & Gallai–Edmonds $D(G)$ Extraction
```cpp
int lca(int u, int v) {
    ++timer;
    for (u = find(u), v = find(v); dfn[u] != timer; ) {
        dfn[u] = timer;
        u = find(pre[match[u]]);
        if (v) swap(u, v);
    }
    return u;
}

void contract(int x, int y, int b) {
    for (int i = find(x); i != b; i = find(pre[y])) {
        pre[x] = y;
        y = match[i];
        if (tp[y] == 2) { tp[y] = 1; q.push(y); }
        dsu[find(i)] = b;
        dsu[find(y)] = b;
        x = pre[y];
    }
}
// Gallai-Edmonds Decomposition D(G): after finding max matching M,
// clear tp/pre/dsu, push ALL exposed vertices u (match[u] == 0) with tp[u] = 1,
// and run the exact same BFS + contract() loop. Final {v : tp[v] == 1} == D(G)!
```

---

## Wave 5A Checklist & Verification Summary

- [x] **Iteration 41**: Covered 1D Segment Tree (`入树`/`出树`), Persistent Segment Tree (`BZOJ 3218`), CDQ Divide-and-Conquer (`[SNOI2019] 通信`), HLD + Prefix Chain (`P19`), 0-1 Trie (`P21`), and 2D KD-Tree (`[NOI2019] 弹跳`) with full Biclique Cut/Flow Factorization proofs and 4 broken-gadget counterexamples.
- [x] **Iteration 42**: Derived 1-Heap Regret Greedy (`CF 865 D`), 1D Mouse-to-Hole 2-Heap Simulation with Multiplicity Batching (`UOJ #455`), and Tree MCMF via Mergeable Heaps & LCA Potentials (`[ICPC WF 2018] Conquer the World`).
- [x] **Iteration 43**: Derived Dynamic Segment Tree Residual Maintenance (`CF 802 O` minimal-flow splitting & `CF 280 D` sign-flipping) and the complete 5-Heap Coupled Bipartite State Automaton (`[NOI2019] 序列` with `free_cap` refund path Cand 5).
- [x] **Iteration 44**: Proved Edmonds' Blossom Contraction Theorem ($\iff$), DSU lazy contraction pointer reversal, the Tutte–Berge Formula, and the Gallai–Edmonds Decomposition $V = D(G) \sqcup A(G) \sqcup C(G)$ for general 2-player walk games.
- [x] **Iteration 45**: Established the 3-Vertex Triangle Bin Gadget (`[WC2016] 挑战 NPC`), Tutte's $b$-Matching Edge/Vertex Split, Edmonds' Odd-Set Blossom LP Polytope, the Skew-Symmetric Tutte Matrix ($\text{rank}(T) = 2\nu(G)$ & Matroid Basis), and the sharp boundary between the LGV Lemma and MCMF.
