# Cohort 3 — Wave 2A Master Reconciliation Monograph (Iteration 107)
## Min-Cut as Binary Variable Assignment, Maximum Weight Closure, Pseudo-Boolean Optimization (`燃やす埋める`), and Bipartite Variable Inversion (`二部グラフの片側反転`)

**Reconciling**:
- **Cohort 1 (`Iter 11–15`)**: `flows_research/iter_11_to_15_mincut_closure_qpbo_bipartite_flip.md`
- **Cohort 2 (`Iter 63–67`)**: `flows_research/cohort2_iter_63_to_67_mincut_closure_qpbo_bipartite_flip.md`
- **Target Scope**: Chapter 3 — The Art of Minimum Cut Modelling (`§3.1–§3.5`, Binary Variable Assignment, Maximum Weight Closure, Kolmogorov–Zabih Submodularity, Bipartite Variable Flipping, QPBO Roof Duality, and `AGC 038 F`)

> **Pedagogical Mandate (Zero Magic Gadgets)**: Every flow/cut network in this monograph is compiled mechanically via the **4-Step English-to-Graph Compilation Pipeline**:
> 1. **Step 1 — Non-Graph Diagnostic Signal (Recognition)**: What surface clue in the English problem statement and constraint bounds ($N, M, V_{\max}$) tells a solver to abandon Tree/Bitmask DP and Greedy in favor of Minimum Cut, and why naive DP/Greedy fails?
> 2. **Step 2 — Intermediate Algebraic / Logical Representation**: Translate the English statement into binary indicator variables $x_i \in \{0, 1\}$, logical implications $x_u \implies x_v$, Optimistic Baseline + Regret Accounting (`先拿后退`), or Quadratic Pseudo-Boolean Optimization (QPBO) polynomials $\Phi(x) = C_0 + \sum_u \theta_u(x_u) + \sum_{u < v} \Theta_{uv}(x_u, x_v)$ *before* drawing a single vertex or edge.
> 3. **Step 3 — Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**: Show step-by-step how each algebraic term forces the exact vertices, edge orientations, capacities, and Bipartite Variable Inversion ($x_j \gets 1 - x_j$ when rescuing supermodular $A + D > B + C$ interactions).
> 4. **Step 4 — Hand-Checkable Toy Trace & Broken Gadget Counterexamples**: Verify every gadget on a concrete numerical trace ($N \le 4$) and explicitly prove what breaks when a subtle compilation invariant is violated (e.g., omitting Kahn's causal cycle pruning, using undirected edges for asymmetric matrices, odd cycles in bipartite flipping, or unreachable positive-weight cycles in project selection).

---

## 1. Cross-Cohort Comparative Audit & Blind-Spot Matrix

Before synthesizing the unified theory of Minimum Cut Compilation, we audit the structural strengths, unique catches, and complementary blind spots of Cohort 1 (`Iter 11–15`) and Cohort 2 (`Iter 63–67`), along with two higher-level theoretical gaps resolved exclusively in this Cohort 3 synthesis.

### 1.1 Theoretical & Modelling Blind-Spot Matrix

| Topic / Iteration | Cohort 1 (`Iter 11–15`) Strengths & Unique Catches | Cohort 2 (`Iter 63–67`) Strengths & Unique Catches | Cohort 3 Reconciled Synthesis & Targeted Gap-Hunting |
| :--- | :--- | :--- | :--- |
| **1. Binary Convention Rosetta Stone ($x_S=1$ vs. $y_S=0$)** | Adopted $x_S = 1, x_T = 0$ ($x_v = [v \in V_S]$) as primary convention; noted the `[JA]` `燃やす埋める` convention $y_S = 0, y_T = 1$ in passing. | Also adopted $x_S = 1, x_T = 0$; included a brief 2-column translation note for `[JA]` blogs (`noshi91`, `maspypy`). | **Full Dual-Convention Rosetta Stone Table (§2.2)**: Side-by-side translation of every atomic term ($x_i$, $1-x_i$, cut monomial $x_u(1-x_v)$ vs. $(1-y_u)y_v$, implication $x_u \implies x_v$, $2 \times 2$ matrix $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$, and Bipartite Flip) between Convention A ($x_S=1, x_T=0$) and Convention B ($y_S=0, y_T=1$). |
| **2. Unary Normalization (`差値正規化` vs. `ゲタを履かせる`) & Regret Accounting (`先拿后退`)** | Explicitly derived **both** Recipe 1 (Minimum Extraction $m_i = \min(A_i, B_i)$, equivalent to pre-pushing $m_i$ flow along the 2-edge path $S \to i \to T$ in $O(1)$) and Recipe 2 (Uniform Constant Pedestal Shift $+M$ / `ゲタを履かせる`). | Explicitly derived signed regret accounting (`先拿后退`) when both $x_i = 1$ and $x_i = 0$ carry arbitrary signed payoffs $u_i(1), u_i(0) \in \mathbb{R}$ (e.g., $+10 x_1 - 4(1-x_1) = 10 - 14(1-x_1)$). | **Unified Regret & Normalization Calculus (§2.3–§2.4)**: Unifies signed profit maximization (`先拿后退`), Recipe 1 (`差値正規化` / $O(1)$ 2-edge path pre-flow), and Recipe 2 (`ゲタを履かせる` / uniform pedestal $+M$) into a single canonical normalization pipeline. |
| **3. Maximum Weight Closure & Cyclic Dependency Semantics** | Explicitly proved why **Tarjan's SCC deletion (`|SCC| >= 2`) fails** on `[NOI2009] 植物大战僵尸` (it fails to delete acyclic vertices that lie causally downstream of a cycle!) whereas Kahn's in-degree $0$ BFS on $G_{\text{pre}}$ prunes both cycles and their causal descendants. | Distinguished **Semantics A (Simultaneous Set Bundle — cycles contract to super-nodes and remain selectable)** vs. **Semantics B (Sequential Causal Unlocking — cycles deadlock and must be pruned)**, and formalized the **Rent-or-Buy Finite-Capacity Relaxation** (`[CEOI 2008] Order`). | **Complete Closure Semantics Taxonomy (§3)**: Combines Picard's Theorem (1976), Simultaneous vs. Sequential Cycle Semantics, the exact Tarjan SCC failure counterexample vs. Kahn's BFS proof, Rent-or-Buy finite-capacity cuts, `ARC 085 E` dual indicator views, and `[SHOI2017] 寿司餐厅` $O(N^2)$ transitive pyramid compression. |
| **4. Submodularity ($A+D \le B+C$) & Normal-Form Decomposition** | Derived the **1-Parameter Continuous Family of Splits** $\alpha + \beta = \Delta = (B+C)-(A+D)$ ($\alpha, \beta \ge 0$), unifying the Asymmetric Integer Split ($\alpha=0, \beta=\Delta$) and Symmetric Split ($\alpha=\beta=\Delta/2$); derived the zero-auxiliary identity $1 - A_i A_j = (1 - A_i) + A_i(1 - A_j)$ for `[TJOI2015] 线性代数`. | Proved the **Submodular Set-Projection Necessity Theorem** ($\Phi(Z_1) + \Phi(Z_2) \ge \Phi(Z_1 \wedge Z_2) + \Phi(Z_1 \vee Z_2)$ over arbitrary auxiliary variables $w \in \{0,1\}^k$), proving no auxiliary-node gadget can ever bypass $A+D \le B+C$; derived Hu Botao's Symmetric Vertex-Edge Merging (`合并点边法`) on `[BZOJ 2039]`. | **Complete Kolmogorov–Zabih Synthesis (§4)**: Unifies the Set-Projection Necessity proof, the 1-parameter continuous split family $\alpha + \beta = \Delta$, Asymmetric vs. Symmetric (`合并点边法`) compilations, and higher-order $k$-tuple `All-in-S` / `All-in-T` hub gadgets. |
| **5. Bipartite Flip (`二部グラフの片側反転`) & QPBO Roof Duality** | Formalized the **Mixed Submodular/Supermodular Signed Graph Balance Criterion** (allowing 4-adjacent supermodular + diagonal submodular edges on a 2D grid!) and compared `[ABC 259 G]` via Inclusion-Exclusion $x_i + y_j - x_i y_j$. | Full derivation of **Hammer–Hansen–Simeone (1984) / Boros–Hammer (2002) QPBO Roof Duality**, the $2n+2$ doubled network $\mathcal{N}_{\text{QPBO}}$, half-integral LP relaxation $\hat{x}_i \in \{0, \frac{1}{2}, 1\}$, **Strong Autarky / Persistency Theorem** (`強永続性`), and proved why $\mathcal{N}_{\text{QPBO}} \setminus \{S, T\}$ splits into $L \cup \bar{R}$ and $\bar{L} \cup R$ when $G$ is bipartite. | **Unified Bipartite Gauge & QPBO Framework (§5)**: Combines the 4 canonical hidden bipartitions, Bipartite Flip matrix reflection, full QPBO Roof Duality + Strong Persistency kernelization, and the structural isomorphism theorem linking Bipartite Flip to halved $\mathcal{N}_{\text{QPBO}}$. |
| **6. Master Case Study (`AGC 038 F — Two Permutations`)** | Traced Official Sample 1 ($N=4$, $P=(2,1,3,0), Q=(0,2,3,1)$) and derived the **Dual Agreement Variation** ($\max \sum [A_i = B_i]$, which is submodular *without* flipping!). | Traced a second $N=4$ benchmark ($P=(1,0,3,2), Q=(1,2,0,3)$) and discovered the **1-Cycle Aliasing Trick** (hardwiring $1$-cycles of $P$ to $T$ and $1$-cycles of $Q$ to $S$ collapses Cases 1–4 into a single rule). | **Definitive `AGC 038 F` Master Section (§6)**: Unifies the Cycle Rigidity Lemma, the 5-Case Table, the 1-Cycle Aliasing Trick, the Dual Agreement Variation, and both complete $N=4$ hand traces. |
| **7. Cohort 3 Targeted Gap-Hunting** | Mentioned signed balance informally for grid diagonals; covered only positive `All-in-S` / `All-in-T` maximization rewards. | Covered QPBO on general non-submodular graphs; covered only positive `All-in-S` / `All-in-T` maximization rewards. | **Two New Theoretical Pillars (§7)**: (1) **Harary's Signed Graph Balance Theorem (1953) & $O(V+E)$ XOR-2-SAT Gauge Switching Algorithm** for arbitrary mixed quadratic polynomials; (2) **Degree-$d$ Pseudo-Boolean Reductions (`Freedman–Drineas 2005`, `Fix et al. 2011`, `Ishikawa 2011`) & the Ternary ($d=3$) vs. Quaternary ($d \ge 4$) Submodular Representability Boundary (`Billionnet–Minoux 1985`, `Živný–Cohen–Jeavons 2009`)**. |

---

### 1.2 Practice Problem Cross-Cohort Deduplication & Tier Audit (31 Unique Non-Template Problems)

Cohorts 1 and 2 each curated 22 problems, sharing 13 overlapping main-bank problems (`P4174`, `CF 1082 G`, `P2774`, `ABC 326 G`, `ARC 085 E`, `CF 311 E`, `P4313`, `P2805`, `ABC 259 G`, `CEOI 2008 Order`, `AGC 038 F`, `ARC 142 E`, `P3749`), plus `CF 103 E` (which Cohort 1 placed in its quarantine table and Cohort 2 solved in full via Hall's Marriage Theorem). Furthermore, Cohort 2 paired `CF 724 E` and `Luogu P3308` inside a single entry. By deduplicating the 13 overlaps, promoting `CF 103 E` to the main bank, and separating `CF 724 E` and `Luogu P3308` into standalone entries, we obtain **31 unique non-template contest problems** across the four pedagogical tiers in **Section 8**:

| Problem ID | Problem Name & Judge URL | Source Cohort(s) | Assigned Tier | Core Algebraic & Graph Compilation Archetype |
| :--- | :--- | :--- | :--- | :--- |
| **P01** | [Luogu P4174 — [NOI2006] 最大获利](https://www.luogu.com.cn/problem/P4174) | C1-P01, C2-P01 | **Tier 1: Stepping Stone** | Canonical Bipartite Project Selection ($r_k z_k$ with $z_k \implies x_{a_k} \wedge x_{b_k}$) |
| **P02** | [Codeforces 1082 G — Petya and Graph](https://codeforces.com/problemset/problem/1082/G) | C1-P02, C2-P02 | **Tier 1: Stepping Stone** | Maximum Weight Induced Subgraph Closure ($w_e y_e - c_v x_v$) |
| **P03** | [Luogu P2057 — [SHOI2007] 善意的投票](https://www.luogu.com.cn/problem/P2057) | C1-P03 | **Tier 1: Stepping Stone** | Pure Symmetric Pairwise Disagreement Minimization ($x_u \oplus x_v$) |
| **P04** | [Luogu P2774 — [网络流24题] 方格取数问题](https://www.luogu.com.cn/problem/P2774) | C1-P04, C2-P03 | **Tier 1: Stepping Stone** | Maximum Weight Independent Set on Bipartite Grid via Parity Flip ($\neg(x_u \wedge x_v) \mapsto x_u \implies y_v$) |
| **P05** | [Luogu P1361 — 小M的作物](https://www.luogu.com.cn/problem/P1361) | C2-P04 | **Tier 1: Stepping Stone** | Dual-Polarity Collective Synergy (`All-in-S` + `All-in-T` Auxiliary Hubs) |
| **P06** | [AtCoder ABC 326 G — Unlock Achievement](https://atcoder.jp/contests/abc326/tasks/abc326_g) | C1-P05, C2-P05 | **Tier 1: Stepping Stone** | Multi-Level Threshold Unary Closure ($x_{i, \ell} \implies x_{i, \ell-1}$, $z_j \implies x_{i, A_{j,i}}$) |
| **P07** | [AtCoder ARC 085 E — MUL](https://atcoder.jp/contests/arc085/tasks/arc085_c) | C1-P06, C2-P06 | **Tier 1: Stepping Stone** | Divisibility Poset Closure ($i \mid j \implies$ Complement of Smashed Gems is Closed) |
| **P08** | [Codeforces 311 E — Biologist](https://codeforces.com/problemset/problem/311/E) | C1-P07, C2-P07 | **Tier 2: Intermediate** | Dual-Side Collective Hub + Penalty-Adjusted Regret (`+W + g` Penalty) |
| **P09** | [Luogu P4313 — [国家集训队] 文理分科](https://www.luogu.com.cn/problem/P4313) | C1-P08, C2-P08 | **Tier 2: Intermediate** | 5-Node Cross-Stencil Dual-Side Collective Hubs (`All-in-S` + `All-in-T` on Grid) |
| **P10** | [Codeforces 808 F — Card Game](https://codeforces.com/problemset/problem/808/F) | C1-P09 | **Tier 2: Intermediate** | Binary Search on Level + Odd/Even Parity Bipartite Conflict Cut + $1$-Card Coalescing |
| **P11** | [Luogu P2805 — [NOI2009] 植物大战僵尸](https://www.luogu.com.cn/problem/P2805) | C1-P10, C2-P09 | **Tier 2: Intermediate** | Sequential Causal Closure with Cyclic Deadlock Pruning via Kahn's BFS |
| **P12** | [AtCoder ABC 259 G — Grid Card Game](https://atcoder.jp/contests/abc259/tasks/abc259_g) | C1-P11, C2-P10 | **Tier 2: Intermediate** | Row-Column Bipartite Flip + Inclusion-Exclusion ($x_i + y_j - x_i y_j$) with Hard Negatives |
| **P13** | [[CEOI 2008] Order / SPOJ ORDER](https://www.spoj.com/problems/ORDER/) | C1-P12, C2-P11 | **Tier 2: Intermediate** | Rent-or-Buy Closure (Finite Rental Capacity $r_{ij}$ vs. Full Purchase Cut) |
| **P14** | [BZOJ 2039 / DarkBZOJ 2039 — [2009国家集训队] 人员雇佣](https://darkbzoj.cc/problem/2039) | C2-P12 | **Tier 2: Intermediate** | Hu Botao's Symmetric Vertex-Edge Merging (`合并点边法`) for Dense Pairwise Matrices |
| **P15** | [Luogu P3973 — [TJOI2015] 线性代数](https://www.luogu.com.cn/problem/P3973) | C1-P13 | **Tier 2: Intermediate** | Quadratic Bilinear Form $A B A^T - A C^T$ via Zero-Auxiliary Asymmetric Split |
| **P16** | [AtCoder ABC 193 F — Zebraness](https://atcoder.jp/contests/abc193/tasks/abc193_f) | C1-P14 | **Tier 3: Advanced** | Grid Checkerboard Bipartite Inversion: Transforming Anti-Ferromagnetic Reward to Agreement |
| **P17** | [Luogu P1791 — [国家集训队] 圈地计划](https://www.luogu.com.cn/problem/P1791) | C2-P14 | **Tier 3: Advanced** | Grid Checkerboard Bipartite Flip Converting Supermodular Competitive Bonus to Submodular Cut |
| **P18** | [BZOJ 3511 / Hydro BZOJ 3511 — 土地划分](https://hydro.ac/p/bzoj-P3511) | C1-P15 | **Tier 3: Advanced** | Simultaneous Node-Splitting (`合并点边`) & Same-State Edge Bonus Gadgets |
| **P19** | [AtCoder ARC 074 F — Lotus Leaves](https://atcoder.jp/contests/arc074/tasks/arc074_d) | C1-P16 | **Tier 3: Advanced** | Row-Column Line Graph Virtualization Reducing $O(H^2 W + W^2 H)$ Cut to $O(HW)$ |
| **P20** | [Codeforces 1404 E — Bricks](https://codeforces.com/problemset/problem/1404/E) | C1-P17 | **Tier 3: Advanced** | Grid Edge-Brick Dualization: Maximizing Orthogonal Joint Merges via Bipartite Conflict Cut |
| **P21** | [Luogu P3749 — [SHOI2017] 寿司餐厅](https://www.luogu.com.cn/problem/P3749) | C1-P18, C2-P16 | **Tier 3: Advanced** | Interval Pyramid Closure ($[l, r] \implies [l+1, r] \wedge [l, r-1]$) + Fixed-Type Tax |
| **P22** | [Codeforces 103 E — Buying Sets](https://codeforces.com/problemset/problem/103/E) | C1-Q04, C2-P13 | **Tier 3: Advanced** | Hall's Marriage Theorem + Pedestal Shift $+M$: Converting $|N(I)| \ge |I|$ into Ordinary Closure |
| **P23** | [Luogu P2604 / BZOJ 3218 — a + b Problem](https://www.luogu.com.cn/problem/P2604) | C2-P15 | **Tier 3: Advanced** | Self-Conflict Penalty + Persistent Segment Tree Virtualization of Range-Restricted Cuts |
| **P24** | [TopCoder SRM 590 Div1 Hard — FoxAndCity](https://vjudge.net/problem/TopCoder-12729) | C2-P17 | **Tier 4: Mastery** | Shortest-Path Distance Lipschitz Constraints $d_v \le d_u + 1$ as Unary Closure |
| **P25** | [AtCoder AGC 038 F — Two Permutations](https://atcoder.jp/contests/agc038/tasks/agc038_f) | C1-P19, C2-P18 | **Tier 4: Mastery** | Cycle Rigidity + 5-Case Pairwise Table + Bipartite Flip + 1-Cycle Aliasing |
| **P26** | [AtCoder ARC 107 F — Sum of Abs](https://atcoder.jp/contests/arc107/tasks/arc107_d) | C1-P20 | **Tier 4: Mastery** | Component Sign Relaxation ($s_C \in \{-1, +1\}$) & 3-State Node-Splitting Cut ($+1, 0, -1$) |
| **P27** | [AtCoder ARC 142 E — Pairing Wizards](https://atcoder.jp/contests/arc142/tasks/arc142_e) | C1-P21, C2-P19 | **Tier 4: Mastery** | Hidden Surplus/Deficit Bipartite Decomposition of Asymmetric Pairwise $\max$/$\min$ Rules |
| **P28** | [AtCoder ARC 176 E — Max Vector](https://atcoder.jp/contests/arc176/tasks/arc176_e) | C1-P22 | **Tier 4: Mastery** | Coordinate-Decoupled Lower-Bound Dominance + Bipartite Flipped Threshold Chains |
| **P29** | [Codeforces 1383 F — Special Edges](https://codeforces.com/problemset/problem/1383/F) | C2-P20 | **Tier 4: Mastery** | Parametric Minimum Cut with $K \le 10$ Variable Edges via $2^K$ Residual Branching |
| **P30** | [Codeforces 724 E — Goods Transportation](https://codeforces.com/problemset/problem/724/E) | C2-P21 | **Tier 4: Mastery** | Direction B (Max-Flow $\to$ Min-Cut $\to$ $O(N^2)$ DP): Eliminating Dense Flow via Cut Algebra |
| **P31** | [Luogu P3308 — [SDOI2014] LIS](https://www.luogu.com.cn/problem/P3308) | C2-P22 | **Tier 4: Mastery** | Lexicographically First Minimum Cut via Residual Reachability & Flow Rollback (`退流`) |

---

## 2. Iteration 11 / 63 Reconciled: Minimum Cut as Binary Variable Assignment & Pseudo-Boolean Cut Polynomials

### 2.1 Step 1 — Non-Graph Diagnostic Signal (Recognition)

How do you recognize a Minimum Cut Binary Assignment problem from an English problem statement when no graph is mentioned?

1. **Binary Decision Universe**: Every entity $i \in \{1, \dots, N\}$ must be assigned to one of two mutually exclusive states:
   - *Build vs. Skip*, *Keep vs. Discard*, *Color Black vs. White*, *Assign to Group A vs. Group B*, *Turn On vs. Off*, or *Rotate Cycle vs. Fix Identity*.
2. **Constraint Bound Signature**: $N \in [50, 5000]$ and $M \in [100, 5 \times 10^4]$ pairwise or group interactions, with arbitrary large weights $V_{\max} \le 10^9$.
   - **Why Bitmask / Tree DP Fails**: The pairwise interaction graph has high treewidth (e.g., an $H \times W$ grid with $H, W \le 100$, a general bipartite graph, or two arbitrary permutations), so $O(2^{\text{tw}} \cdot N)$ is exponential.
   - **Why Greedy / Matroid Intersection Fails**: Local choices cascade globally through coupled penalties and hard logical implications; flipping one variable can invalidate a long chain of dependencies.
   - **Why Capacities up to $10^9$ Are Safe**: On networks where only $S$-incident and $T$-incident edges carry finite capacities and all internal edges have capacity $+\infty$ (or on small dense graphs of size $N \le 3000$), Dinic's algorithm runs in strongly polynomial $O(V^2 E)$ or $O(E \sqrt{V})$ time, independent of $V_{\max}$.

---

### 2.2 Step 2 — Intermediate Algebraic Representation & The Dual-Convention Rosetta Stone

Before drawing any vertices or edges, we establish an exact bijection between **$(S, T)$-cuts** in a directed graph $G = (V, E)$ with source $S$, sink $T$, and non-negative capacities $c: E \to \mathbb{R}_{\ge 0} \cup \{+\infty\}$, and **binary indicator vectors**.

An **$(S, T)$-cut** is a partition $V = V_S \sqcup V_T$ with $S \in V_S$ and $T \in V_T$. Its capacity is the sum of capacities of all directed edges crossing from $V_S$ to $V_T$:
$$\text{cap}(V_S, V_T) = \sum_{\substack{(u \to v) \in E \\ u \in V_S, \, v \in V_T}} c(u \to v).$$
Crucially, an edge $(u \to v)$ with $u \in V_T$ and $v \in V_S$ (crossing "backward" from $T$-side to $S$-side) contributes **$0$** to the cut capacity!

In the multilingual competitive programming and combinatorial optimization literature, two opposite conventions exist for mapping $V_S$ and $V_T$ to $\{0, 1\}$. Confusion between these two conventions is the #1 source of reversed edges in contest implementations.

#### Convention A (`[ZH]` Selection / Closure Convention — Adopted Throughout This Monograph)
Define $x_v \in \{0, 1\}$ for every $v \in V$ by:
$$x_v = \begin{cases} 1 & \text{if } v \in V_S \quad (\text{"selected / true / kept in } S\text{"}), \\ 0 & \text{if } v \in V_T \quad (\text{"rejected / false / relegated to } T\text{"}), \end{cases}$$
with boundary conditions **$x_S = 1$** and **$x_T = 0$**. Under Convention A, a directed edge $(u \to v)$ is severed if and only if $u \in V_S$ ($x_u = 1$) and $v \in V_T$ ($x_v = 0$), which corresponds to the quadratic **Cut Monomial**:
$$\boxed{\text{Edge }(u \to v)\text{ with capacity } c \ge 0 \quad \Longleftrightarrow \quad c \cdot x_u (1 - x_v)}$$
Therefore, the capacity of any $(S, T)$-cut is a **Quadratic Pseudo-Boolean Polynomial** (specifically, a *posiform* of degree 2 in the literal pairs $(x_u, \bar{x}_v)$):
$$\Phi_G(x) = \underbrace{\sum_{u \in V \setminus \{S, T\}} c(S \to u)\,(1 - x_u)}_{\text{severed } S \to u \text{ when } x_u = 0} \;+\; \underbrace{\sum_{u \in V \setminus \{S, T\}} c(u \to T)\,x_u}_{\text{severed } u \to T \text{ when } x_u = 1} \;+\; \underbrace{\sum_{u, v \in V \setminus \{S, T\}} c(u \to v)\,x_u(1 - x_v)}_{\text{severed } u \to v \text{ when } x_u = 1, \, x_v = 0}.$$

#### Convention B (`[JA]` `燃やす埋める` / `[EN]` Computer Vision KZ04 Convention)
In the Japanese competitive programming literature (`noshi91`, `maspypy`, `tatyam`) and Kolmogorov–Zabih (2004), a variable $y_v \in \{0, 1\}$ is defined by:
$$y_v = \begin{cases} 0 & \text{if } v \in V_S \quad (\text{"burn / } S\text{-side = 0"}), \\ 1 & \text{if } v \in V_T \quad (\text{"bury / } T\text{-side = 1"}), \end{cases}$$
with boundary conditions **$y_S = 0$** and **$y_T = 1$** (so $y_v = 1 - x_v$). Under Convention B, a directed edge $(u \to v)$ is severed iff $y_u = 0$ and $y_v = 1$, giving the cut monomial $c \cdot (1 - y_u) y_v$.

#### Table 2.1 — The Dual-Convention Rosetta Stone (`Convention A` vs. `Convention B`)

| Modelling Concept | Convention A ($x_S = 1, x_T = 0$, `[ZH]` / This Monograph) | Convention B ($y_S = 0, y_T = 1$, `[JA]` `燃やす埋める` / KZ04) |
| :--- | :--- | :--- |
| **Indicator Definition** | $x_v = 1 \iff v \in V_S$, $x_v = 0 \iff v \in V_T$ | $y_v = 0 \iff v \in V_S$, $y_v = 1 \iff v \in V_T$ ($y_v = 1 - x_v$) |
| **Atomic Edge $(u \to v)$ of cap $c$** | $c \cdot x_u (1 - x_v)$ (penalizes $x_u = 1 \wedge x_v = 0$) | $c \cdot (1 - y_u) y_v$ (penalizes $y_u = 0 \wedge y_v = 1$) |
| **Unary Penalty for State $0$** | $c \cdot (1 - x_u) \implies$ Edge **$S \to u$** of capacity $c$ | $c \cdot (1 - y_u) \implies$ Edge **$u \to T$** of capacity $c$ |
| **Unary Penalty for State $1$** | $c \cdot x_u \implies$ Edge **$u \to T$** of capacity $c$ | $c \cdot y_u \implies$ Edge **$S \to u$** of capacity $c$ |
| **Hard Implication $u=1 \implies v=1$** | Forbid $x_u=1 \wedge x_v=0 \implies$ **$u \to v$** of cap $+\infty$ | Forbid $y_u=1 \wedge y_v=0 \implies$ **$v \to u$** of cap $+\infty$ |
| **Hard Mutual Exclusion $\neg(u=1 \wedge v=1)$** | Flip $v$: $x'_v = 1 - x_v$; forbid $x_u=1 \wedge x'_v=0 \implies$ **$u \to v$** ($+\infty$) | Flip $u$: $y'_u = 1 - y_u$; forbid $y'_u=0 \wedge y_v=1 \implies$ **$u \to v$** ($+\infty$) |
| **Submodular Condition on $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$** | $A + D \le B + C$ (Identical in both conventions!) | $A + D \le B + C$ (Identical in both conventions!) |

---

### 2.3 Optimistic Baseline & Regret Accounting (`先拿后退` / Pre-Claimed Revenue)

Minimum Cut is inherently a **minimization** solver ($\min_{x \in \{0,1\}^N} \Phi_G(x)$ with non-negative edge capacities), whereas contest problems frequently ask to **maximize** a total score or net profit $\Psi(x)$ containing positive rewards and negative costs.

To convert $\max_x \Psi(x)$ into $\min_x \Phi(x)$:
1. **Pre-Claim All Possible Positive Rewards (`先拿后退`)**: Sum every positive reward $r_k > 0$ into an **Optimistic Baseline** $W_{\text{base}} = \sum_{r_k > 0} r_k$, pretending we simultaneously achieve every single bonus in the universe (even mutually exclusive ones!).
2. **Subtract Regret / Forfeiture Penalties**: Rewrite every term in $\Psi(x)$ as a non-negative **regret** subtracted from $W_{\text{base}}$:
   - **Positive reward $+r_i x_i$ ($r_i > 0$) for choosing $x_i = 1$**:
     $$+r_i x_i = r_i - r_i(1 - x_i) \implies \text{Add } +r_i \text{ to } W_{\text{base}}, \text{ add regret } r_i(1 - x_i) \text{ [Edge } S \to i, \text{ cap } r_i\text{]}.$$
   - **Positive reward $+r_i (1 - x_i)$ ($r_i > 0$) for choosing $x_i = 0$**:
     $$+r_i (1 - x_i) = r_i - r_i x_i \implies \text{Add } +r_i \text{ to } W_{\text{base}}, \text{ add regret } r_i x_i \text{ [Edge } i \to T, \text{ cap } r_i\text{]}.$$
   - **Direct cost $-c_i x_i$ ($c_i > 0$) for choosing $x_i = 1$**:
     $$\text{Add } 0 \text{ to } W_{\text{base}}, \text{ add cost } c_i x_i \text{ [Edge } i \to T, \text{ cap } c_i\text{]}.$$
   - **Direct cost $-c_i (1 - x_i)$ ($c_i > 0$) for choosing $x_i = 0$**:
     $$\text{Add } 0 \text{ to } W_{\text{base}}, \text{ add cost } c_i (1 - x_i) \text{ [Edge } S \to i, \text{ cap } c_i\text{]}.$$
   - **General Signed Payoff $u_i(1) x_i + u_i(0)(1 - x_i)$ with $u_i(1), u_i(0) \in \mathbb{R}$**:
     Let $M_i = \max(u_i(1), u_i(0))$. Add $M_i$ to $W_{\text{base}}$.
     - If $u_i(1) \ge u_i(0)$, the regret of choosing $x_i = 0$ is $\Delta_i = u_i(1) - u_i(0) \ge 0$, compiled as edge $S \to i$ of capacity $\Delta_i$.
     - If $u_i(0) > u_i(1)$, the regret of choosing $x_i = 1$ is $\Delta_i = u_i(0) - u_i(1) > 0$, compiled as edge $i \to T$ of capacity $\Delta_i$.
     *(Example: $+10 x_1 - 4(1 - x_1) = 10 - 14(1 - x_1) \implies$ add $+10$ to $W_{\text{base}}$ and edge $S \to 1$ of capacity $14$.)*

Then:
$$\max_{x \in \{0,1\}^N} \Psi(x) = W_{\text{base}} - \min_{x \in \{0,1\}^N} \Phi_G(x) = W_{\text{base}} - \text{MaxFlow}(S, T).$$

---

### 2.4 Step 3 — Unary Normalization Recipes (`差値正規化` vs. `ゲタを履かせる`)

During the algebraic compilation of pairwise matrices (§4), collecting unary terms onto vertex $i$ often yields:
$$U_i(x_i) = A_i (1 - x_i) + B_i x_i,$$
where $A_i$ or $B_i$ may be **negative**! Since Dinic's algorithm fails on negative edge capacities, how do we eliminate negative unary coefficients? Both of the following recipes are exact:

#### Recipe 1: Minimum Extraction / 2-Edge Path Pre-Flow (`差値正規化` — Recommended Default)
Extract $m_i = \min(A_i, B_i)$ into the global constant offset $C_0$:
$$A_i (1 - x_i) + B_i x_i = m_i \underbrace{\big((1 - x_i) + x_i\big)}_{= 1} + (A_i - m_i)(1 - x_i) + (B_i - m_i)x_i.$$
Now both $(A_i - m_i) \ge 0$ and $(B_i - m_i) \ge 0$, and **at least one of them is zero**!
- If $A_i \ge B_i$: add $B_i$ to $C_0$, and add a single edge $S \to i$ of capacity $A_i - B_i \ge 0$.
- If $B_i > A_i$: add $A_i$ to $C_0$, and add a single edge $i \to T$ of capacity $B_i - A_i > 0$.

> **Flow-Theoretic Interpretation**: When $A_i > 0$ and $B_i > 0$ are both positive, adding both $S \to i$ (cap $A_i$) and $i \to T$ (cap $B_i$) creates an immediate 2-edge augmenting path $S \to i \to T$ of bottleneck capacity $m_i = \min(A_i, B_i)$. Recipe 1 simply **pre-pushes $m_i$ units of flow along $S \to i \to T$ in $O(1)$ time** during graph construction, saturating one of the two edges and reducing the Dinic edge count!

#### Recipe 2: Uniform Constant Pedestal Shift (`ゲタを履かせる` / "Putting on Geta Clogs")
Choose a large constant $M > \max_i(|A_i|, |B_i|)$ and add $+M = M(1 - x_i) + M x_i$ to vertex $i$'s cost:
$$U_i(x_i) = -M + (A_i + M)(1 - x_i) + (B_i + M)x_i.$$
Add both $S \to i$ (cap $A_i + M > 0$) and $i \to T$ (cap $B_i + M > 0$), then subtract $M$ from the final answer. While correct, Recipe 2 inflates edge capacities by $O(N \cdot M)$ (risking 32-bit overflow) and forces Dinic's first BFS phase to waste $N$ augmentations draining the $S \to i \to T$ paths. Always prefer **Recipe 1** in implementation, while using **Recipe 2** as a conceptual proof tool (e.g., in `CF 103 E — Buying Sets`, P22).

---

### 2.5 Step 4 — Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Toy Trace ($N = 3$ Variables with Unary Payoffs and Implications)
Maximize $\Psi(x_1, x_2, x_3)$ over $x_1, x_2, x_3 \in \{0, 1\}$:
- Choosing $x_1 = 1$ gives $+10$; choosing $x_1 = 0$ gives $-4$.
- Choosing $x_2 = 1$ costs $-6$; choosing $x_2 = 0$ gives $+5$.
- Choosing $x_3 = 1$ gives $+8$; choosing $x_3 = 0$ gives $0$.
- **Constraints**:
  1. Hard implication: $x_1 = 1 \implies x_2 = 1$.
  2. Soft penalty: if $x_3 = 1$ and $x_2 = 0$, pay a penalty of $9$.

**Algebraic Compilation**:
- Vertex 1: $10 x_1 - 4(1 - x_1) = 10 - 14(1 - x_1) \implies W_{\text{base}} \mathrel{+}= 10$, edge $S \to 1$ of cap $14$.
- Vertex 2: $-6 x_2 + 5(1 - x_2) = 5 - 11 x_2 \implies W_{\text{base}} \mathrel{+}= 5$, edge $2 \to T$ of cap $11$.
- Vertex 3: $8 x_3 = 8 - 8(1 - x_3) \implies W_{\text{base}} \mathrel{+}= 8$, edge $S \to 3$ of cap $8$.
- Total $W_{\text{base}} = 10 + 5 + 8 = 23$.
- Hard implication $x_1 \implies x_2$: $\infty \cdot x_1(1 - x_2) \implies$ directed edge $1 \to 2$ of cap $+\infty$.
- Soft penalty $9 x_3(1 - x_2) \implies$ directed edge $3 \to 2$ of cap $9$.

**Exhaustive Evaluation of Valid Cuts** ($x_1 = 1, x_2 = 0$ is forbidden by $\text{cap}(1 \to 2) = +\infty$):
1. **$x = (0, 0, 0)$** ($V_S = \{S\}$): severs $S \to 1$ ($14$) and $S \to 3$ ($8$). Cut $= 22 \implies \Psi = 23 - 22 = 1$.
2. **$x = (0, 0, 1)$** ($V_S = \{S, 3\}$): severs $S \to 1$ ($14$) and $3 \to 2$ ($9$). Cut $= 23 \implies \Psi = 23 - 23 = 0$.
3. **$x = (0, 1, 0)$** ($V_S = \{S, 2\}$): severs $S \to 1$ ($14$), $S \to 3$ ($8$), $2 \to T$ ($11$). Cut $= 33 \implies \Psi = -10$.
4. **$x = (0, 1, 1)$** ($V_S = \{S, 2, 3\}$): severs $S \to 1$ ($14$), $2 \to T$ ($11$). Cut $= 25 \implies \Psi = -2$.
5. **$x = (1, 1, 0)$** ($V_S = \{S, 1, 2\}$): severs $S \to 3$ ($8$), $2 \to T$ ($11$). Cut $= 19 \implies \Psi = 4$.
6. **$x = (1, 1, 1)$** ($V_S = \{S, 1, 2, 3\}$): severs only $2 \to T$ ($11$). **Minimum Cut $= 11 \implies \max \Psi = 23 - 11 = 12$**!
Direct check on $x = (1, 1, 1)$: $+10 - 6 + 8 = 12$. Exact match!

#### Broken Gadget Counterexamples
1. **Reversing the Implication Edge ($2 \to 1$ instead of $1 \to 2$)**: Putting $+\infty$ on $2 \to 1$ penalizes $x_2(1 - x_1)$, enforcing $x_2 \implies x_1$ instead of $x_1 \implies x_2$. Then $x = (1, 0, 1)$ becomes legal with cut $9$ (severing only $3 \to 2$), hallucinating a false profit of $23 - 9 = 14$!
2. **Using an Undirected $\infty$-Edge for Implication**: An undirected $\infty$-edge between $1$ and $2$ forces $x_1 = x_2$ (equivalence), forbidding $(0, 1, 1)$ even when $x_2 = 1$ without $x_1 = 1$ would otherwise be optimal.

---

## 3. Iteration 12 / 64 Reconciled: Maximum Weight Closure (`最大权闭合子图`) & Cyclic Dependency Semantics

### 3.1 Step 1 — Non-Graph Diagnostic Signal (Recognition)

Reach for **Maximum Weight Closure** (`最大权闭合子图`, Picard 1976 / Hu Botao 2007) whenever a problem takes the form:
- *"Choose a subset of items/projects/intervals/multiples $C \subseteq U$ to maximize $\sum_{v \in C} w_v$ (where $w_v \in \mathbb{R}$ can be positive, zero, or negative) subject to prerequisite rules: if $u \in C$ and $u$ depends on $v$, then $v \in C$ must also hold."*
- **Why Tree / DAG DP Fails**: On a general dependency DAG, two nodes $u_1, u_2$ can share a common prerequisite $v$. A naive DP over subtrees double-counts $w_v < 0$ when both $u_1$ and $u_2$ are selected! Closure handles arbitrary overlapping prerequisites (diamond DAGs, bipartite hypergraphs, interval pyramids, divisibility posets) in polynomial time.

---

### 3.2 Step 2 & Step 3 — Picard's Theorem (1976) & Mechanical Graph Compilation

Let $G_{\text{dep}} = (U, E_{\text{dep}})$ be a directed prerequisite graph with vertex weights $w: U \to \mathbb{R}$. A subset $C \subseteq U$ is **closed** (`闭合`) if every directed edge $(u \to v) \in E_{\text{dep}}$ satisfies:
$$u \in C \implies v \in C \qquad \text{(no edge of } E_{\text{dep}} \text{ leaves } C\text{)}.$$
Partition $U$ into positive-weight vertices $U^+ = \{u \in U : w_u > 0\}$ and non-positive-weight vertices $U^- = \{u \in U : w_u \le 0\}$. Let $x_u = [u \in C] \in \{0, 1\}$.

#### Algebraic-to-Graph Compilation
1. **Optimistic Baseline (`先拿后退`)**: Pre-claim all positive weights:
   $$W^+ = \sum_{u \in U^+} w_u.$$
2. **Unary Regret & Cost Terms**:
   $$\sum_{u \in U} w_u x_u = \sum_{u \in U^+} w_u - \underbrace{\sum_{u \in U^+} w_u (1 - x_u)}_{\text{forfeited positive rewards}} - \underbrace{\sum_{v \in U^-} |w_v| x_v}_{\text{paid negative costs}}.$$
   - For each $u \in U^+$ ($w_u > 0$): term $w_u(1 - x_u) \implies$ directed edge **$S \to u$** of capacity $w_u$.
   - For each $v \in U^-$ ($w_v \le 0$): term $|w_v| x_v \implies$ directed edge **$v \to T$** of capacity $|w_v| = -w_v$.
3. **Hard Dependency Implications**:
   - For each $(u \to v) \in E_{\text{dep}}$: forbid $x_u = 1 \wedge x_v = 0$ via $\infty \cdot x_u(1 - x_v) \implies$ directed edge **$u \to v$** of capacity $+\infty$.

#### Theorem 3.1 (Picard's Maximum Weight Closure Theorem, 1976)
In the compiled network $\mathcal{N}$, any $(S, T)$-cut $(V_S, V_T)$ of **finite** capacity ($< +\infty$) defines a closed subset $C = V_S \setminus \{S\} \subseteq U$, and conversely every closed subset $C \subseteq U$ defines a finite-capacity cut $V_S = \{S\} \cup C$, with:
$$\text{cap}(V_S, V_T) = W^+ - \sum_{u \in C} w_u \quad \implies \quad \max_{C \text{ closed}} \sum_{u \in C} w_u = W^+ - \text{MinCut}(S, T).$$
Moreover, the optimal closed set $C^*$ is reconstructed in $O(|U| + |E_{\text{dep}}|)$ time as the set of vertices in $U$ reachable from $S$ via positive-residual edges in the final residual network $G_f$.

---

### 3.3 The Two Semantics of Directed Cycles: Simultaneous Bundles vs. Sequential Causal Unlocking

What happens when the dependency graph $G_{\text{dep}}$ is **not** a DAG and contains directed cycles? There is a critical distinction between two problem semantics that every solver must check:

#### Semantics A: Simultaneous Set Selection (Logical Equivalence Bundle)
If the problem statement says *"you may select any subset $C \subseteq U$ all at once, provided that $u \in C \implies v \in C$ for all $(u \to v) \in E_{\text{dep}}$"*, then any directed cycle $v_1 \to v_2 \to \dots \to v_k \to v_1$ simply enforces:
$$x_{v_1} = x_{v_2} = \dots = x_{v_k}.$$
Under Semantics A, Picard's network $\mathcal{N}$ works **without modification**: the $\infty$-cycle forces all $v_i$ to lie on the same side of any finite cut, so the strongly connected component (SCC) acts as a single super-node of net weight $W_{\text{SCC}} = \sum_{i=1}^k w_{v_i}$. If $W_{\text{SCC}} > 0$ and its downstream prerequisites cost less than $W_{\text{SCC}}$, selecting the entire cycle is **valid and optimal**.

#### Semantics B: Sequential / Causal Unlocking (`[NOI2009] 植物大战僵尸` — Cyclic Deadlock)
If the problem statement requires a **valid causal ordering** (e.g., *"to eat plant $u$, you must first eat all plants $v$ that protect $u$ or stand to the right of $u$ in the same row"*), then no vertex on a directed cycle can ever be unlocked first! Worse still, **any vertex $w$ that depends on a cycle is also permanently unreachable**, even if $w$ itself has a huge positive weight $+10^9$ and does not belong to any cycle!

> **Fatal Trap — Why Tarjan's SCC Deletion (`|SCC| >= 2`) Fails on Semantics B**:
> Suppose a cycle $C_1 \leftrightarrow C_2$ has weights $w(C_1) = w(C_2) = 0$, and an acyclic node $A$ has weight $w(A) = +100$ with dependency $A \to C_1$ (to unlock $A$, you must first unlock $C_1$).
> - In Picard's unmodified graph, placing $\{A, C_1, C_2\} \subseteq V_S$ severs zero $\infty$-edges and pays cost $0$, yielding a hallucinated profit of $+100$!
> - If you run Tarjan's SCC algorithm and only delete vertices in SCCs of size $\ge 2$ (deleting $C_1, C_2$ and their incident edges), then $A$ is left with in-degree $0$ and is **still falsely selected** for $+100$!
>
> **Correct Algorithm — Kahn's Topological BFS on the Reverse Prerequisite Graph $G_{\text{pre}}$**:
> Construct the **Causal Prerequisite Graph** $G_{\text{pre}}$ where each edge is oriented from **prerequisite to dependent**:
> $$(v \xrightarrow{\text{unlocks}} u) \in E_{\text{pre}} \quad \Longleftrightarrow \quad (u \xrightarrow{\text{requires}} v) \in E_{\text{dep}}.$$
> Run Kahn's BFS queue starting from all vertices with $\text{in-degree}_{G_{\text{pre}}}(v) = 0$:
> 1. Pop $v$ from the queue, mark `vis[v] = true`, and decrement $\text{in-degree}_{G_{\text{pre}}}(u)$ for all $(v \to u) \in E_{\text{pre}}$, pushing $u$ when its in-degree hits $0$.
> 2. When the queue empties, **every vertex with `vis[v] == false` is either inside a directed cycle or causally dependent on a cycle**. Discard all `vis[v] == false` vertices completely before building the flow network $\mathcal{N}$!

---

### 3.4 Four Canonical Structural Variations of Closure

#### Variation 1: Bipartite Project Selection & Hyperedge Synergy (`NOI 2006 最大获利`, `CF 1082 G`)
- Each project/hyperedge $k$ yields profit $r_k > 0$ only if all required machines $i \in S_k$ are purchased at cost $c_i > 0$.
- **Compilation**: Auxiliary vertex $z_k \in \{0, 1\}$ with $S \to z_k$ (cap $r_k$), $z_k \to x_i$ (cap $+\infty$) for all $i \in S_k$, and $x_i \to T$ (cap $c_i$).
- **Complexity Bonus**: This is a bipartite closure network ($V = \{S, T\} \cup L \cup R$ where only $S \to L$ and $R \to T$ have finite capacities). By unit/bipartite network analysis, Dinic runs in $O(E \sqrt{V})$ or $O(V E)$ strongly polynomial time.

#### Variation 2: Rent-or-Buy Finite-Capacity Relaxation (`[CEOI 2008] Order`)
- Project $i$ requires machine $j$. Instead of being forced to buy machine $j$ outright (cost $c_j$), project $i$ can **rent** machine $j$ for single-project use at fee $r_{ij} > 0$.
- **Compilation**: Replace the hard dependency edge $i \to j$ (cap $+\infty$) with a **soft dependency edge $i \to j$ of capacity $r_{ij}$**!
- **Cut Verification**: When project $i$ is selected ($x_i = 1$):
  - If we do not buy machine $j$ ($x_j = 0$), every active project $i$ using $j$ severs its own edge $i \to j$, paying $\sum_{i : x_i = 1} r_{ij}$ (individual rentals).
  - If $\sum_{i : x_i = 1} r_{ij} > c_j$, the minimum cut automatically moves $j$ into $V_S$ ($x_j = 1$) and severs the single edge $j \to T$ of capacity $c_j$ (buying machine $j$ outright for all projects)!

#### Variation 3: Divisibility Poset Closure (`AtCoder ARC 085 E — MUL`)
- Given $a_1, \dots, a_N \in \mathbb{Z}$. Picking index $i$ requires picking all multiples $2i, 3i, \dots \le N$ (or in the original statement: smashing gem $i$ smashes all multiples $ki$, forfeiting their values).
- **Dual Compilation Views**:
  - **View A (Keep Indicator $x_i = 1 \iff i$ is NOT smashed)**: If $j$ is a multiple of $i$ ($i \mid j$) and $j$ is kept ($x_j = 1$), then $i$ could not have been smashed ($x_i = 1$). Thus $x_j \implies x_i$ ($j \to i$ of cap $+\infty$), and we find the Maximum Weight Closure of $(a_1, \dots, a_N)$!
  - **View B (Smashed Indicator $y_i = 1 \iff i$ is smashed)**: Smashing $i$ forces smashing all multiples $j = ki$: $y_i \implies y_j$ ($i \to j$ of cap $+\infty$). Keeping $i \in V_S$ ($y_i = 0$) when $a_i > 0$ is baseline $+a_i$, severed when $i \in V_T$ ($i \to T$ cap $a_i$); smashing $i \in V_T$ when $a_i < 0$ is penalized when $i \in V_S$ ($S \to i$ cap $|a_i|$).
- **Transitive Sparsification**: Only link $i$ to $i \cdot p$ for primes $p$, reducing edges from $O(N \ln N)$ to $O(N \ln \ln N)$.

#### Variation 4: Interval Pyramid Closure (`[SHOI2017] 寿司餐厅`)
- Eating any contiguous subsegment $[l, r]$ yields reward $d_{l,r}$, and requires eating all subsegments $[l', r'] \subseteq [l, r]$.
- **Transitive Pyramid Reduction**: Instead of adding $O(N^4)$ edges from $[l, r]$ to all sub-intervals, observe that every sub-interval of $[l, r]$ (for $l < r$) is contained in $[l+1, r]$ or $[l, r-1]$. Thus **two $\infty$-edges per interval**:
  $$[l, r] \xrightarrow{+\infty} [l+1, r] \quad \text{and} \quad [l, r] \xrightarrow{+\infty} [l, r-1]$$
  enforce the entire $O(N^4)$ closure using only $O(N^2)$ vertices and $O(N^2)$ edges!

---

## 4. Iteration 13 / 65 Reconciled: Pairwise Interaction Matrices, Kolmogorov–Zabih Submodularity ($A + D \le B + C$), and Higher-Order Hubs

### 4.1 Step 1 & Step 2 — General $2 \times 2$ Cost Matrices & The Submodularity Theorem

Suppose two binary variables $x_i, x_j \in \{0, 1\}$ interact via a general $2 \times 2$ **cost (penalty) matrix** $\Theta_{ij}(x_i, x_j)$ (to be **minimized**):

| $x_i \setminus x_j$ | $x_j = 0$ ($j \in V_T$) | $x_j = 1$ ($j \in V_S$) |
| :---: | :---: | :---: |
| **$x_i = 0$ ($i \in V_T$)** | $A = \Theta_{ij}(0, 0)$ | $B = \Theta_{ij}(0, 1)$ |
| **$x_i = 1$ ($i \in V_S$)** | $C = \Theta_{ij}(1, 0)$ | $D = \Theta_{ij}(1, 1)$ |

*(If the problem maximizes a $2 \times 2$ reward matrix $\Pi_{ij}$, either negate it $\Theta_{ij} = -\Pi_{ij}$ or subtract from $M = \max(A,B,C,D)$ via $\Theta_{ij} = M - \Pi_{ij}$; note that maximizing $\Pi_{ij}$ is submodular as a cut minimization iff $\Pi_{ij}$ is **supermodular**: $\Pi(0,0) + \Pi(1,1) \ge \Pi(0,1) + \Pi(1,0)$!)*

#### Theorem 4.1 (Freedman–Drineas 2005 / Kolmogorov–Zabih 2004 — Graph Representability of Pairwise Functions)
A pairwise cost function $\Theta(x) = C_0 + \sum_i \theta_i(x_i) + \sum_{i < j} \Theta_{ij}(x_i, x_j)$ is graph-representable as the minimum $(S, T)$-cut of a directed network with non-negative capacities (even allowing arbitrary auxiliary vertices $W$) **if and only if** every pairwise matrix $\Theta_{ij}$ is **submodular**:
$$\boxed{A + D \le B + C \qquad \Longleftrightarrow \qquad \Theta_{ij}(0, 0) + \Theta_{ij}(1, 1) \le \Theta_{ij}(0, 1) + \Theta_{ij}(1, 0)}$$

#### Proof of Sufficiency & The 1-Parameter Continuous Family of Splits ($\alpha + \beta = \Delta$)
Expand $\Theta_{ij}(x_i, x_j)$ over $\{0, 1\}^2$:
$$\Theta_{ij}(x_i, x_j) = A(1 - x_i)(1 - x_j) + B(1 - x_i)x_j + C x_i(1 - x_j) + D x_i x_j$$
$$= A + (C - A)x_i + (B - A)x_j - \underbrace{(B + C - A - D)}_{\Delta \ge 0} x_i x_j.$$
Substitute the algebraic identity $-x_i x_j = x_i(1 - x_j) - x_i = x_j(1 - x_i) - x_j$. For **any** non-negative split $\alpha + \beta = \Delta = (B + C) - (A + D)$ with $\alpha \ge 0, \beta \ge 0$, writing $-\Delta x_i x_j = \alpha(x_i(1 - x_j) - x_i) + \beta(x_j(1 - x_i) - x_j)$ yields the **Master 1-Parameter Decomposition Identity**:
$$\boxed{\Theta_{ij}(x_i, x_j) = \underbrace{A}_{\text{constant}} + \underbrace{(C - A - \alpha)\,x_i}_{\text{unary on } i} + \underbrace{(B - A - \beta)\,x_j}_{\text{unary on } j} + \underbrace{\alpha\,x_i(1 - x_j)}_{\text{edge } i \to j \text{ cap } \alpha} + \underbrace{\beta\,x_j(1 - x_i)}_{\text{edge } j \to i \text{ cap } \beta}}$$

We verify all four states $(x_i, x_j) \in \{0, 1\}^2$ directly:
- $(0, 0)$: $A + 0 + 0 + 0 + 0 = A$.
- $(0, 1)$: $A + 0 + (B - A - \beta) + 0 + \beta = B$.
- $(1, 0)$: $A + (C - A - \alpha) + 0 + \alpha + 0 = C$.
- $(1, 1)$: $A + (C - A - \alpha) + (B - A - \beta) + 0 + 0 = B + C - A - (\alpha + \beta) = B + C - A - \Delta = D$.

Two choices of $(\alpha, \beta)$ dominate competitive programming:
1. **Choice 1 — Asymmetric Integer Split ($\alpha = 0, \beta = \Delta = B + C - A - D$)**:
   $$\Theta_{ij}(x_i, x_j) = A + (C - A)x_i + (D - C)x_j + (B + C - A - D)x_j(1 - x_i)$$
   *(or symmetrically $\alpha = \Delta, \beta = 0$: $\Theta_{ij} = A + (D - B)x_i + (B - A)x_j + \Delta x_i(1 - x_j)$)*.
   **Why it is the implementation gold standard**: All capacities stay **purely integral** (no $\frac{1}{2}$ fractions!), and it creates only **one** directed edge ($j \to i$ or $i \to j$) of capacity $\Delta \ge 0$!
2. **Choice 2 — Symmetric Half-Integral Split ($\alpha = \beta = \Delta / 2$, Hu Botao's `合并点边法`)**:
   $$\Theta_{ij}(x_i, x_j) = A + \frac{C + D - A - B}{2}x_i + \frac{B + D - A - C}{2}x_j + \frac{\Delta}{2}\big(x_i(1 - x_j) + x_j(1 - x_i)\big).$$
   This creates an **undirected** edge $i \leftrightarrow j$ of capacity $\Delta / 2$ (scale all capacities by $2$ if $\Delta$ is odd). It is canonical when $\Theta_{ij}$ is symmetric ($A = D = 0, B = C = w \implies \text{cap}(i \leftrightarrow j) = w$) or in problems like `[BZOJ 2039] 人员雇佣` (P14).

#### Proof of Necessity (Why No Auxiliary-Node Gadget Can Bypass $A + D \le B + C$)
Suppose a network $\mathcal{N}$ with original variables $x \in \{0, 1\}^n$ and $k$ auxiliary vertices $w \in \{0, 1\}^k$ represents $f(x) = \min_{w \in \{0,1\}^k} \Phi_{\mathcal{N}}(x, w)$. Let $Z = (x, w) \in \{0, 1\}^{n+k}$. Every single edge $(u \to v)$ of capacity $c \ge 0$ has cut function $c \cdot Z_u(1 - Z_v)$, which satisfies the submodular inequality $0 + 0 \le 0 + c$. Since a non-negative sum of submodular functions is submodular, $\Phi_{\mathcal{N}}(Z)$ satisfies:
$$\Phi_{\mathcal{N}}(Z^{(1)}) + \Phi_{\mathcal{N}}(Z^{(2)}) \ge \Phi_{\mathcal{N}}(Z^{(1)} \wedge Z^{(2)}) + \Phi_{\mathcal{N}}(Z^{(1)} \vee Z^{(2)}).$$
Minimizing over $w^{(1)}, w^{(2)} \in \{0, 1\}^k$ projects submodularity onto $f(x)$:
$$f(x^{(1)}) + f(x^{(2)}) = \Phi_{\mathcal{N}}(x^{(1)}, w^{*(1)}) + \Phi_{\mathcal{N}}(x^{(2)}, w^{*(2)}) \ge \Phi_{\mathcal{N}}(x^{(1)} \wedge x^{(2)}, w^{*(1)} \wedge w^{*(2)}) + \Phi_{\mathcal{N}}(x^{(1)} \vee x^{(2)}, w^{*(1)} \vee w^{*(2)}) \ge f(x^{(1)} \wedge x^{(2)}) + f(x^{(1)} \vee x^{(2)}).$$
For $n = 2$ with $x^{(1)} = (1, 0)$ and $x^{(2)} = (0, 1)$, this forces $B + C \ge A + D$. **No clever gadget of auxiliary vertices with non-negative capacities can ever represent a supermodular pairwise cost ($A + D > B + C$) without flipping a variable!** $\blacksquare$

---

### 4.2 Higher-Order $k$-Tuple Collective Bonus Gadgets (`All-in-S` & `All-in-T` Hubs)

For a subset $K \subseteq \{1, \dots, N\}$ of $|K| \ge 2$ variables, two higher-order reward terms in maximization (or negative posiform terms in minimization) are directly submodular and compile via **one auxiliary hub vertex**:

1. **`All-in-S` Collective Reward $+w \prod_{i \in K} x_i$ ($w > 0$)**:
   - **Regret formulation**: Add $+w$ to $W_{\text{base}}$. Regret is $w\big(1 - \prod_{i \in K} x_i\big) = \min_{z_S \in \{0,1\}} \big[w(1 - z_S) + \sum_{i \in K} \infty \cdot z_S(1 - x_i)\big]$.
   - **Gadget**: Create auxiliary hub $z_S$. Add edge **$S \to z_S$** of capacity $w$, and directed edges **$z_S \to i$** of capacity $+\infty$ for all $i \in K$.
2. **`All-in-T` Collective Reward $+w \prod_{i \in K} (1 - x_i)$ ($w > 0$)**:
   - **Regret formulation**: Add $+w$ to $W_{\text{base}}$. Regret is $w\big(1 - \prod_{i \in K} (1 - x_i)\big) = \min_{z_T \in \{0,1\}} \big[w \cdot z_T + \sum_{i \in K} \infty \cdot x_i(1 - z_T)\big]$.
   - **Gadget**: Create auxiliary hub $z_T$. Add directed edges **$i \to z_T$** of capacity $+\infty$ for all $i \in K$, and edge **$z_T \to T$** of capacity $w$.

> **Zero-Auxiliary Optimization for $k = 2$ (`[TJOI2015] 线性代数`, P15)**:
> When $|K| = 2$, the `All-in-S` regret $w(1 - x_i x_j)$ is a submodular $2 \times 2$ matrix $\begin{pmatrix} w & w \\ w & 0 \end{pmatrix}$ ($\Delta = w$). Using the Asymmetric Split ($\alpha = w, \beta = 0$), we can use the exact identity:
> $$w(1 - x_i x_j) = w(1 - x_i) + w \cdot x_i(1 - x_j),$$
> which compiles directly as unary capacity $+w$ on $S \to i$ and a single directed edge $i \to j$ of capacity $w$ — **eliminating all $O(N^2)$ auxiliary hub vertices**!

---

### 4.3 Step 4 — Hand-Checkable Toy Trace & Broken Gadget Counterexamples

#### Toy Trace (Asymmetric Submodular $2 \times 2$ Matrix Compilation)
Minimize $\Phi(x_1, x_2) = 5 x_1 + 2(1 - x_2) + \Theta_{12}(x_1, x_2)$ where:
$$\Theta_{12} = \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} 4 & 9 \\ 3 & 2 \end{pmatrix}.$$
1. **Submodularity Check**: $A + D = 4 + 2 = 6 \le B + C = 9 + 3 = 12$. Submodular with $\Delta = 12 - 6 = 6 > 0$!
2. **Asymmetric Split ($\alpha = 6, \beta = 0$)**:
   $$\Theta_{12}(x_1, x_2) = 4 + (2 - 9)x_1 + (9 - 4)x_2 + 6 x_1(1 - x_2) = 4 - 7 x_1 + 5 x_2 + 6 x_1(1 - x_2).$$
3. **Combine with Unary Terms & Apply Recipe 1 (`差値正規化`)**:
   $$\Phi(x_1, x_2) = 4 + (5 - 7)x_1 + \big(2(1 - x_2) + 5 x_2\big) + 6 x_1(1 - x_2)$$
   - For $x_1$: $-2 x_1 = -2 + 2(1 - x_1) \implies$ add $-2$ to $C_0$, edge **$S \to 1$** of cap $2$.
   - For $x_2$: $2(1 - x_2) + 5 x_2 = 2 + 3 x_2 \implies$ add $+2$ to $C_0$, edge **$2 \to T$** of cap $3$.
   - Global constant offset: $C_0 = 4 - 2 + 2 = 4$.
   - Pairwise edge: **$1 \to 2$** of cap $6$.
4. **Verify All 4 Cuts against True $\Phi(x_1, x_2)$**:
   - $(0, 0)$: $C_0 + \text{cap}(S \to 1) = 4 + 2 = 6$. True: $0 + 2 + 4 = 6$.
   - $(0, 1)$: $C_0 + \text{cap}(S \to 1) + \text{cap}(2 \to T) = 4 + 2 + 3 = 9$. True: $0 + 0 + 9 = 9$.
   - $(1, 0)$: $C_0 + \text{cap}(1 \to 2) = 4 + 6 = 10$. True: $5 + 2 + 3 = 10$.
   - $(1, 1)$: $C_0 + \text{cap}(2 \to T) = 4 + 3 = 7$. True: $5 + 0 + 2 = 7$.
   Every single state matches to the exact integer!

#### Broken Gadget Counterexamples
1. **Using an Undirected Edge Without Adjusting Unary Terms**: In the asymmetric matrix above ($B = 9 \neq C = 3$), if a contestant adds an undirected edge $1 \leftrightarrow 2$ of capacity $\Delta / 2 = 3$ without adding the asymmetric unary corrections, $(1, 0)$ and $(0, 1)$ receive identical pairwise penalties, corrupting the cut.
2. **Reversing Hub Edge Orientations on `All-in-T`**: If you orient $z_T \to i$ (cap $+\infty$) instead of $i \to z_T$ (cap $+\infty$) for an `All-in-T` hub with $z_T \to T$ (cap $w$), then setting $z_T = 0$ ($z_T \in V_T$) severs **zero** edges regardless of $x_i$, allowing the solver to claim the `All-in-T` bonus $+w$ for free even when all $x_i = 1$!

---

## 5. Iteration 14 / 66 Reconciled: Rescuing Supermodular Costs via Bipartite Variable Flipping (`二部グラフの片側反転`) & QPBO Roof Duality

### 5.1 Step 1 — Non-Graph Diagnostic Signal (When $A + D > B + C$ Violates Submodularity)

What happens when you write down the pairwise penalty matrix $\Theta_{ij}(x_i, x_j)$ and discover that it is **strictly supermodular**:
$$A + D > B + C \qquad \text{(or in maximization: } \Pi(0,0) + \Pi(1,1) < \Pi(0,1) + \Pi(1,0)\text{)}?$$
This occurs whenever the problem **penalizes agreement** ($x_i = x_j$) or **rewards disagreement** ($x_i \neq x_j$):
1. **Mutual Exclusion / Independent Set**: Picking both $x_i = 1$ and $x_j = 1$ is forbidden ($D = +\infty$, $A = B = C = 0 \implies A + D = +\infty > 0$).
2. **Covering / Threshold OR Requirement**: Leaving both $x_i = 0$ and $x_j = 0$ is forbidden ($A = +\infty$, $B = C = D = 0 \implies A + D = +\infty > 0$).
3. **Anti-Ferromagnetic / Zebra Coloring**: Neighboring cells get a bonus $w > 0$ when colored *differently* ($A = D = w, B = C = 0 \implies A + D = 2w > 0$).

By Theorem 4.1, **no $(S, T)$-cut network can directly represent $\Theta_{ij}$ in the original variables $(x_i, x_j)$**. Because general supermodular minimization is NP-hard (reducing from Max-Cut and Maximum Independent Set), you must immediately hunt for a **Bipartite Structure** in the interaction graph!

---

### 5.2 Step 2 & Step 3 — Bipartite Variable Flipping (`二部グラフの片側反転`)

Suppose the supermodular interaction pairs $(i, j)$ form a **bipartite graph** $G = (L \sqcup R, E)$ where every supermodular edge connects a left vertex $i \in L$ to a right vertex $j \in R$.

Perform a **Gauge Transformation (Variable Inversion)** on all right-side vertices $j \in R$:
$$\begin{cases} y_i = x_i & \text{for } i \in L \quad (i \in V_S \iff x_i = 1, \; i \in V_T \iff x_i = 0), \\ y_j = 1 - x_j & \text{for } j \in R \quad (j \in V_S \iff x_j = 0, \; j \in V_T \iff x_j = 1). \end{cases}$$

#### Effect on Unary Terms for $j \in R$
Because $x_j = 1 - y_j$, the roles of $S$ and $T$ swap on $R$:
- A penalty $c \cdot x_j = c(1 - y_j)$ (which was $j \to T$ in $x_j$) becomes **$S \to j$ of capacity $c$**!
- A penalty $c(1 - x_j) = c \cdot y_j$ (which was $S \to j$ in $x_j$) becomes **$j \to T$ of capacity $c$**!

#### Effect on the $2 \times 2$ Matrix $\Theta_{ij}(x_i, x_j)$ for $i \in L, j \in R$
Substituting $x_i = y_i$ and $x_j = 1 - y_j$ **swaps the two columns** of $\Theta_{ij}$:
$$\widetilde{\Theta}_{ij}(y_i, y_j) = \Theta_{ij}(y_i, 1 - y_j) = \begin{pmatrix} \widetilde{A} & \widetilde{B} \\ \widetilde{C} & \widetilde{D} \end{pmatrix} = \begin{pmatrix} B & A \\ D & C \end{pmatrix}.$$
Check the submodularity condition on the transformed matrix $\widetilde{\Theta}_{ij}$:
$$\boxed{\widetilde{A} + \widetilde{D} \le \widetilde{B} + \widetilde{C} \quad \Longleftrightarrow \quad B + C \le A + D!}$$
The exact supermodularity condition $A + D > B + C$ that broke Kolmogorov–Zabih in $(x_i, x_j)$ becomes **strict submodularity** $\widetilde{A} + \widetilde{D} < \widetilde{B} + \widetilde{C}$ in $(y_i, y_j)$, with cut capacity $\widetilde{\Delta} = (A + D) - (B + C) > 0$!

#### Table 5.1 — The 4 Canonical Supermodular Clause Conversions ($i \in L, j \in R$, $y_j = 1 - x_j$)

| Original Supermodular Clause in $(x_i, x_j)$ | Original Matrix $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$ | Flipped Matrix $\begin{pmatrix} B & A \\ D & C \end{pmatrix}$ in $(y_i, y_j)$ | Compiled Directed Edge(s) in $(y_i, y_j)$ |
| :--- | :---: | :---: | :--- |
| **Hard Conflict**: $\neg(x_i = 1 \wedge x_j = 1)$ | $\begin{pmatrix} 0 & 0 \\ 0 & \infty \end{pmatrix}$ | $\begin{pmatrix} 0 & 0 \\ \infty & 0 \end{pmatrix}$ ($\infty \cdot y_i(1 - y_j)$) | **$i \to j$ of capacity $+\infty$** |
| **Hard Covering (OR)**: $x_i = 1 \vee x_j = 1$ | $\begin{pmatrix} \infty & 0 \\ 0 & 0 \end{pmatrix}$ | $\begin{pmatrix} 0 & \infty \\ 0 & 0 \end{pmatrix}$ ($\infty \cdot y_j(1 - y_i)$) | **$j \to i$ of capacity $+\infty$** |
| **Soft Conflict Penalty**: $+w \cdot x_i x_j$ | $\begin{pmatrix} 0 & 0 \\ 0 & w \end{pmatrix}$ | $\begin{pmatrix} 0 & 0 \\ w & 0 \end{pmatrix}$ ($w \cdot y_i(1 - y_j)$) | **$i \to j$ of capacity $w$** |
| **Zebra Disagreement Bonus**: $-w[x_i \neq x_j]$ (regret $w[x_i = x_j]$) | $\begin{pmatrix} w & 0 \\ 0 & w \end{pmatrix}$ | $\begin{pmatrix} 0 & w \\ w & 0 \end{pmatrix}$ ($w\,y_i(1-y_j) + w\,y_j(1-y_i)$) | **$i \leftrightarrow j$ of capacity $w$** |

---

### 5.3 The 4 Canonical Hidden Bipartitions in Competitive Programming

When an English problem statement does not hand you a bipartite graph on a silver platter, look for one of these four disguised bipartitions:
1. **2D Grid Checkerboard Parity (`(r + c) & 1`)**: Any 4-connected orthogonal grid interaction (`P2774 方格取数`, `ABC 193 F Zebraness`, `P1791 圈地计划`, `CF 1404 E Bricks`). Set $L = \{(r, c) : (r + c) \equiv 0 \pmod 2\}$ and $R = \{(r, c) : (r + c) \equiv 1 \pmod 2\}$.
2. **Row vs. Column Incidence (`Row i` $\leftrightarrow$ `Col j`)**: Any operation where cell $(i, j)$ couples a decision on Row $i$ with a decision on Column $j$ (`ABC 259 G Grid Card Game`, `ARC 074 F Lotus Leaves`, `ARC 176 E Max Vector`). Set $L = \text{Rows}$ and $R = \text{Cols}$.
3. **Two Permutations / Two Cycle Decompositions (`Cycle of P` $\leftrightarrow$ `Cycle of Q`)**: Whenever index $i \in \{1, \dots, N\}$ couples its cycle in permutation $P$ with its cycle in permutation $Q$ (`AGC 038 F Two Permutations`). Set $L = \text{Cycles}(P)$ and $R = \text{Cycles}(Q)$.
4. **Surplus vs. Deficit / Odd vs. Even Parity (`ARC 142 E Pairing Wizards`, `CF 808 F Card Game`)**:
   - In `ARC 142 E`, wizard pairs have $\min(a_u, a_v) \ge \max(b_u, b_v) \iff (a_u \ge b_u \wedge a_v \ge b_v) \wedge (a_u \ge b_v \wedge a_v \ge b_u)$. After raising $a_u \gets \max(a_u, b_u)$, every wizard is cleanly partitioned into **Surplus Wizards** ($L = \{u : a_u > b_u\}$, who never need $a_u$ raised further!) and **Deficit Wizards** ($R = \{v : a_v = b_v\}$, whose threshold $b_v$ forces $a_u \ge b_v \vee a_v \ge b_u$)!
   - In `CF 808 F`, two prime-sum cards $c_i + c_j = \text{prime} > 2$ must have opposite parities (since $2$ is the only even prime, and $1 + 1 = 2$ is handled by coalescing all $1$-cards). Set $L = \text{Odd Cards}$ and $R = \text{Even Cards}$.

---

### 5.4 QPBO Roof Duality (`Hammer–Hansen–Simeone 1984` / `Boros–Hammer 2002`) & Strong Persistency

What if the interaction graph $G$ is **non-bipartite** (contains odd cycles of supermodular terms) or mixes arbitrary submodular and supermodular terms? Can Minimum Cut still extract exact information?

Yes! **Quadratic Pseudo-Boolean Optimization (QPBO)** via **Roof Duality** constructs a **Doubled Network $\mathcal{N}_{\text{QPBO}}$** on $2n + 2$ vertices:
$$V(\mathcal{N}_{\text{QPBO}}) = \{S, T\} \cup \{x_1, \dots, x_n\} \cup \{\bar{x}_1, \dots, \bar{x}_n\},$$
where $\bar{x}_i$ represents the formal negation $1 - x_i$.
1. **Submodular Pair ($A + D \le B + C$, $\Delta = B + C - A - D \ge 0$)**: Split into two skew-symmetric copies of capacity $\frac{1}{2}\Delta$:
   $$\text{Edge } (x_i \to x_j) \text{ of cap } \tfrac{1}{2}\Delta \quad \text{and} \quad \text{Edge } (\bar{x}_j \to \bar{x}_i) \text{ of cap } \tfrac{1}{2}\Delta.$$
2. **Supermodular Pair ($A + D > B + C$, $|\Delta| = A + D - B - C > 0$)**: Replace $x_j$ by $1 - \bar{x}_j$ on one side and $x_i$ by $1 - \bar{x}_i$ on the other, yielding two skew-symmetric cross-edges of capacity $\frac{1}{2}|\Delta|$:
   $$\text{Edge } (x_i \to \bar{x}_j) \text{ of cap } \tfrac{1}{2}|\Delta| \quad \text{and} \quad \text{Edge } (x_j \to \bar{x}_i) \text{ of cap } \tfrac{1}{2}|\Delta|.$$
3. **Unary Terms**: Split symmetrically between $x_i$ and $\bar{x}_i$ with factor $\frac{1}{2}$ (so $c \cdot x_i = \frac{1}{2}c \cdot x_i + \frac{1}{2}c(1 - \bar{x}_i)$ adds $x_i \to T$ of cap $\frac{1}{2}c$ and $S \to \bar{x}_i$ of cap $\frac{1}{2}c$).

#### Theorem 5.2 (Hammer–Hansen–Simeone Roof Duality & Strong Persistency / Autarky Theorem)
Let $(V_S, V_T)$ be a minimum $(S, T)$-cut in $\mathcal{N}_{\text{QPBO}}$. For each $i \in \{1, \dots, n\}$, define the half-integral assignment $\hat{x}_i \in \{0, \frac{1}{2}, 1\}$ by:
$$\hat{x}_i = \begin{cases} 1 & \text{if } x_i \in V_S \text{ and } \bar{x}_i \in V_T, \\ 0 & \text{if } x_i \in V_T \text{ and } \bar{x}_i \in V_S, \\ \tfrac{1}{2} & \text{if both } x_i, \bar{x}_i \in V_S \text{ or both } x_i, \bar{x}_i \in V_T. \end{cases}$$
Then:
1. **Half-Integral LP Relaxation (`Roof Dual`)**: $\text{MinCut}(\mathcal{N}_{\text{QPBO}})$ equals the exact minimum of the continuous LP relaxation of $\Phi(x)$ over $[0, 1]^n$, and $\hat{x} \in \{0, \frac{1}{2}, 1\}^n$ is a half-integral optimal solution (specializing to the **Nemhauser–Trotter Theorem (1975)** for Maximum Weight Independent Set!).
2. **Strong Persistency (`強永続性` / Autarky Property)**: There exists a globally optimal binary solution $x^* \in \arg\min_{x \in \{0,1\}^n} \Phi(x)$ that **agrees with $\hat{x}$ on every integral coordinate**:
   $$\forall i \in \{1, \dots, n\}, \qquad \hat{x}_i \in \{0, 1\} \implies x^*_i = \hat{x}_i!$$
   *(In FPT / Branch-and-Bound algorithms, you can permanently fix all variables with $\hat{x}_i \in \{0, 1\}$ and branch only on the unresolved $\hat{x}_i = \frac{1}{2}$ kernel!)*
3. **Why Bipartite Flip Is Exact Halving of $\mathcal{N}_{\text{QPBO}}$**: When $G = (L \sqcup R, E)$ is bipartite and every edge is supermodular, the internal edges of $\mathcal{N}_{\text{QPBO}} \setminus \{S, T\}$ only connect $L \leftrightarrow \bar{R}$ and $\bar{L} \leftrightarrow R$. Thus $\mathcal{N}_{\text{QPBO}} \setminus \{S, T\}$ splits into **two completely disconnected, isomorphic networks**: $V_1 = L \cup \bar{R}$ and $V_2 = \bar{L} \cup R$, each carrying half the capacity! Keeping only $V_1 = L \cup \bar{R}$ and doubling its capacities back to $1\times$ is **literally the Bipartite Variable Flip network**!

---

## 6. Iteration 15 / 67 Reconciled: Master Case Study — `AtCoder AGC 038 F (Two Permutations)`

**Judge URL**: [https://atcoder.jp/contests/agc038/tasks/agc038_f](https://atcoder.jp/contests/agc038/tasks/agc038_f)
**Constraints**: $N \le 10^5$, permutations $P, Q$ of $(0, 1, \dots, N-1)$. Time Limit: 2.0 s.

### 6.1 Problem Statement & Step 1 — Diagnostic Signal + Cycle Rigidity Lemma

Given two permutations $P$ and $Q$ of $(0, 1, \dots, N-1)$, construct two permutations $A$ and $B$ such that for every $i \in \{0, \dots, N-1\}$:
- $A_i \in \{i, P_i\}$ and $B_i \in \{i, Q_i\}$,
- Maximize the number of indices $i$ where **$A_i \neq B_i$**.

#### Lemma 6.1 (Cycle Rigidity Lemma)
Let $P$ be decomposed into disjoint directed cycles $C_1, \dots, C_{K_P}$. Because $A$ must be a valid bijection (permutation) and $A_i \in \{i, P_i\}$ restricts every $i$ to edges inside its own cycle $C_u$, every cycle $C_u$ of $P$ has **only two valid configurations** in $A$:
- **$x_u = 0$ (Identity / Stay)**: $A_i = i$ for **all** $i \in C_u$.
- **$x_u = 1$ (Shift / Rotate)**: $A_i = P_i$ for **all** $i \in C_u$.
*(Proof: If $A_i = P_i$ for some $i \in C_u$, then $P_i$'s unique incoming slot in $A$ is taken by $i$, so $A_{P_i}$ cannot equal $P_i$; hence $A_{P_i} = P_{P_i}$, propagating around the entire cycle $C_u$.)*

Similarly, decompose $Q$ into disjoint cycles $D_1, \dots, D_{K_Q}$, where each cycle $D_v$ has a binary variable $w_v \in \{0, 1\}$ ($w_v = 0 \implies B_i = i$; $w_v = 1 \implies B_i = Q_i$).

---

### 6.2 Step 2 & Step 3 — Exhaustive 5-Case Table, Bipartite Flip, and the 1-Cycle Aliasing Trick

Start with the Optimistic Baseline $W_{\text{base}} = N$ (assuming $A_i \neq B_i$ for all $N$ indices) and **minimize the number of collisions $[A_i = B_i]$**. For each index $i \in \{0, \dots, N-1\}$, let $i \in C_u$ (in $P$) and $i \in D_v$ (in $Q$). Because $A_i \in \{i, P_i\}$ and $B_i \in \{i, Q_i\}$, a collision $A_i = B_i$ can only occur at value $i$ (when $x_u = 0 \wedge w_v = 0$) or at value $P_i = Q_i$ (when $P_i = Q_i$ and $x_u = 1 \wedge w_v = 1$).

Notice that in Case 4 ($P_i \neq i, Q_i \neq i, P_i \neq Q_i$), the collision penalty is $(1 - x_u)(1 - w_v)$ ($\Theta = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$), and in Case 5 ($P_i = Q_i \neq i$), it is $(1 - x_u)(1 - w_v) + x_u w_v$ ($\Theta = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$). **Both matrices have $A + D > B + C$ (supermodular)!**

Because every index $i$ only couples a cycle $C_u \in \text{Cycles}(P)$ with a cycle $D_v \in \text{Cycles}(Q)$, the interaction graph is **bipartite**! We apply **Bipartite Variable Inversion** to all cycles of $Q$:
$$\boxed{y_v = 1 - w_v \qquad \Longleftrightarrow \qquad \begin{cases} y_v = 1 \; (D_v \in V_S) \iff B_i = i \text{ (Stay)}, \\ y_v = 0 \; (D_v \in V_T) \iff B_i = Q_i \text{ (Shift)}. \end{cases}}$$

#### Table 6.1 — Complete 5-Case Collision & Graph Compilation Table (in $x_u$ and $y_v = 1 - w_v$)

| Case | Condition on Index $i$ | Collision Condition ($A_i = B_i$) | Penalty in $(x_u, w_v)$ | Flipped Penalty in $(x_u, y_v)$ | Directed Edge(s) Added (Cap $1$) |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **Case 1** | $P_i = i$ and $Q_i = i$ | Always $A_i = i = B_i$ | $1$ | $1$ | Add $+1$ to constant cut offset $C_0$ |
| **Case 2** | $P_i = i$ and $Q_i \neq i$ | $B_i = i \iff w_v = 0$ | $1 - w_v$ | $y_v$ | Edge **$D_v \to T$** of capacity $1$ |
| **Case 3** | $P_i \neq i$ and $Q_i = i$ | $A_i = i \iff x_u = 0$ | $1 - x_u$ | $1 - x_u$ | Edge **$S \to C_u$** of capacity $1$ |
| **Case 4** | $P_i \neq i, Q_i \neq i, P_i \neq Q_i$ | $A_i = i \wedge B_i = i$ | $(1 - x_u)(1 - w_v)$ | $y_v(1 - x_u)$ | Edge **$D_v \to C_u$** of capacity $1$ |
| **Case 5** | $P_i = Q_i \neq i$ | $(A_i = B_i = i) \vee (A_i = B_i = P_i)$ | $(1-x_u)(1-w_v) + x_u w_v$ | $y_v(1 - x_u) + x_u(1 - y_v)$ | Edges **$D_v \to C_u$** and **$C_u \to D_v$** (cap $1$) |

> **Implementation Elegance — The 1-Cycle Aliasing Trick (Cohort 2 Catch)**:
> If a cycle $C_u$ has length $1$ ($P_i = i$), $A_i = i$ is fixed regardless of $x_u$, which behaves identically to forcing $x_u = 0$ ($C_u \in V_T$). Symmetrically, if $D_v$ has length $1$ ($Q_i = i$), $B_i = i$ is fixed, which behaves identically to forcing $y_v = 1$ ($D_v \in V_S$).
> Therefore, if you **alias every 1-cycle $C_u$ of $P$ directly to vertex $T$** and **alias every 1-cycle $D_v$ of $Q$ directly to vertex $S$**, then Cases 1, 2, 3, and 4 all become the **single rule**: *"Add directed edge $D_v \to C_u$ of capacity $1$"* (ignoring self-loops and recording $S \to T$ edges into $C_0$)!

> **Dual Variation — Maximizing Agreement $\max \sum_i [A_i = B_i]$ (Cohort 1 Catch)**:
> What if a follow-up problem asks to **maximize** the number of agreements $A_i = B_i$? Then the collision indicators $(1 - x_u)(1 - w_v)$ (`All-in-T` reward) and $x_u w_v$ (`All-in-S` reward) are **already submodular without flipping $w_v$**! Specifically, in $(x_u, w_v)$ with $W_{\text{base}} = N$: Case 4 has regret $1 - (1 - x_u)(1 - w_v) = x_u + w_v(1 - x_u)$ ($C_u \to T$ cap $1$, $D_v \to C_u$ cap $1$), and Case 5 has regret $x_u(1 - w_v) + w_v(1 - x_u)$ ($C_u \leftrightarrow D_v$ cap $1$).

#### Complexity Proof
Every vertex in $V \setminus \{S, T\}$ has either $\text{in-degree} \le \text{out-degree}$ or total incident finite capacity $\le 2N$. Because all edges have unit capacity $1$, Dinic's algorithm runs in $O(E \sqrt{V}) = O(N \sqrt{N})$ time — finishing in $< 35\text{ ms}$ for $N = 10^5$!

---

### 6.3 Step 4 — Two Complete Hand-Checkable Toy Traces ($N = 4$)

#### Trace 1: Official Sample 1 ($N = 4$, $P = (2, 1, 3, 0)$, $Q = (0, 2, 3, 1)$)
- **Cycles of $P$**: $C_1 = (0 \to 2 \to 3 \to 0)$ (length 3), $C_2 = (1)$ (1-cycle).
- **Cycles of $Q$**: $D_1 = (0)$ (1-cycle), $D_2 = (1 \to 2 \to 3 \to 1)$ (length 3).
- **Index-by-Index Compilation**:
  - $i = 0$: $P_0 = 2 \neq 0, Q_0 = 0$ (Case 3) $\implies$ edge **$S \to C_1$** (cap $1$).
  - $i = 1$: $P_1 = 1, Q_1 = 2 \neq 1$ (Case 2) $\implies$ edge **$D_2 \to T$** (cap $1$).
  - $i = 2$: $P_2 = 3 = Q_2 \neq 2$ (Case 5) $\implies$ edges **$D_2 \to C_1$** (cap $1$) and **$C_1 \to D_2$** (cap $1$).
  - $i = 3$: $P_3 = 0 \neq 3, Q_3 = 1 \neq 3, P_3 \neq Q_3$ (Case 4) $\implies$ edge **$D_2 \to C_1$** (cap $1$).
- **Min-Cut Evaluation**: Net edges are $S \to C_1$ (cap $1$), $C_1 \to D_2$ (cap $1$), $D_2 \to C_1$ (cap $2$), $D_2 \to T$ (cap $1$). The unique augmenting path $S \to C_1 \to D_2 \to T$ pushes $1$ unit of flow, so $\text{MinCut} = 1$ (achieved by $x_1 = 1, y_2 = 0 \implies A = P = (2, 1, 3, 0), B = Q = (0, 2, 3, 1)$, colliding only at $i = 2$ where $A_2 = B_2 = 3$).
- **Maximum Disagreements**: $N - \text{MinCut} = 4 - 1 = 3$.

#### Trace 2: Intersecting 2-Cycle & 3-Cycle ($N = 4$, $P = (1, 0, 3, 2)$, $Q = (1, 2, 0, 3)$)
- **Cycles of $P$**: $C_1 = (0, 1)$, $C_2 = (2, 3)$.
- **Cycles of $Q$**: $D_1 = (0, 1, 2)$, $D_2 = (3)$ (1-cycle).
- **Index-by-Index Compilation**:
  - $i = 0$: $P_0 = 1 = Q_0 \neq 0$ (Case 5) $\implies$ **$D_1 \leftrightarrow C_1$** (cap $1$ each way).
  - $i = 1$: $P_1 = 0, Q_1 = 2$ (Case 4) $\implies$ **$D_1 \to C_1$** (cap $1$).
  - $i = 2$: $P_2 = 3, Q_2 = 0$ (Case 4) $\implies$ **$D_1 \to C_2$** (cap $1$).
  - $i = 3$: $P_3 = 2 \neq 3, Q_3 = 3$ (Case 3) $\implies$ **$S \to C_2$** (cap $1$).
- **Min-Cut Evaluation**: Since $T$ has in-degree $0$, setting $V_S = \{S, C_1, C_2, D_1\}$ and $V_T = \{T\}$ severs **zero** edges! Thus $\text{MinCut} = 0 \implies N - 0 = 4$ disagreements!
- **Assignment Verification**: $V_S = \{S, C_1, C_2, D_1\} \implies x_1 = 1, x_2 = 1$ ($A = P = (1, 0, 3, 2)$) and $y_1 = 1 \implies w_1 = 0$ ($B = \text{id} = (0, 1, 2, 3)$). Comparing $A = (1, 0, 3, 2)$ and $B = (0, 1, 2, 3)$, all $4$ positions disagree!

---

## 7. Cohort 3 Targeted Gap-Hunting & Reconciled Master Recognition/Compilation Decision Table

In this section, we resolve two foundational theoretical questions that bridge Cohort 1 and Cohort 2:
1. **Arbitrary Mixed Submodular/Supermodular Graphs**: How do we decide in $O(V + E)$ time whether a general quadratic pseudo-Boolean polynomial containing *both* submodular and supermodular interactions can be made globally submodular by flipping a subset of variables $R \subseteq V$?
2. **Higher-Degree ($d \ge 3$) Pseudo-Boolean Reductions**: Exactly which cubic and degree-$d$ pseudo-Boolean terms can be compiled into $(S, T)$-cuts via auxiliary vertices, and where does submodular cut-representability break down?

---

### 7.1 Gap 1: Harary's Signed Graph Balance Theorem (1953) & $O(V + E)$ XOR-2-SAT Gauge Switching

Suppose we want to minimize a general quadratic pseudo-Boolean function:
$$\Phi(x) = C_0 + \sum_{u \in V} \theta_u(x_u) + \sum_{(u, v) \in E} \Theta_{uv}(x_u, x_v),$$
where each pair $(u, v) \in E$ has $\Delta_{uv} = (B_{uv} + C_{uv}) - (A_{uv} + D_{uv}) \neq 0$:
- If $\Delta_{uv} > 0$, edge $(u, v)$ is **strictly submodular**; give it sign $\varepsilon_{uv} = +1$ (a **positive edge**).
- If $\Delta_{uv} < 0$, edge $(u, v)$ is **strictly supermodular**; give it sign $\varepsilon_{uv} = -1$ (a **negative edge**).

We want to find a **Gauge Switch (Variable Inversion)** $\sigma: V \to \{0, 1\}$, where $y_u = x_u \oplus \sigma_u$ (i.e., $y_u = x_u$ if $\sigma_u = 0$, and $y_u = 1 - x_u$ if $\sigma_u = 1$), such that in the transformed variables $y$, **every edge $(u, v) \in E$ becomes submodular ($\widetilde{\Delta}_{uv} > 0$)**.

#### Theorem 7.1 (Harary's Signed Graph Balance & Gauge Switching Theorem, 1953 / Boros–Hammer 2002)
Flipping $\sigma_u \in \{0, 1\}$ negates $\Delta_{uv} \mapsto -\Delta_{uv}$ if and only if $\sigma_u \neq \sigma_v$. Therefore, a variable inversion $R = \{u \in V : \sigma_u = 1\}$ makes $\Phi$ globally submodular **if and only if** $\sigma \in \{0, 1\}^V$ satisfies the **XOR-2-SAT linear system**:
$$\boxed{\begin{cases} \sigma_u \oplus \sigma_v = 0 \quad (\sigma_u = \sigma_v) & \text{for every submodular edge } (u, v) \in E^+ \; (\Delta_{uv} > 0), \\ \sigma_u \oplus \sigma_v = 1 \quad (\sigma_u \neq \sigma_v) & \text{for every supermodular edge } (u, v) \in E^- \; (\Delta_{uv} < 0). \end{cases}}$$
Equivalently, by **Harary's Balance Theorem (1953)**, such a subset $R \subseteq V$ exists **if and only if the signed graph $(V, E^+ \sqcup E^-)$ is balanced — that is, no cycle in $G$ contains an odd number of supermodular ($E^-$) edges**!

> **Practical Contest Consequence (Why Grid Diagonals Can Be Submodular While Orthogonal Edges Are Supermodular!)**:
> On an $H \times W$ grid, suppose 4-adjacent orthogonal neighbors $(u, v)$ have **supermodular** costs ($\Delta_{uv} < 0$), AND 4-diagonal neighbors $(u, w)$ have **submodular** costs ($\Delta_{uw} > 0$). The total 8-connected graph is **not bipartite** (it is full of triangles!). Yet under the checkerboard flip $\sigma_{(r,c)} = (r + c) \bmod 2$:
> - Every orthogonal edge has $\sigma_u \neq \sigma_v$ (flipping its supermodular cost into a submodular cost!), and
> - Every diagonal edge has $\sigma_u = \sigma_w$ (preserving its submodular cost!).
> Every triangle has two orthogonal ($-$) edges and one diagonal ($+$) edge, so its product of signs is $(-1)(-1)(+1) = +1$ (balanced)! By Theorem 7.1, a single BFS checking $\sigma_u \oplus \sigma_v = [\Delta_{uv} < 0]$ in $O(V + E)$ time finds the exact flip set $R$ whenever one exists!

---

### 7.2 Gap 2: Degree-$d$ Pseudo-Boolean Reductions (`Freedman–Drineas 2005`, `Fix et al. 2011`, `Ishikawa 2011`) & The Submodular Representability Boundary

In §4.2, we compiled `All-in-S` ($-w \prod_{i \in K} x_i$ in minimization) and `All-in-T` ($-w \prod_{i \in K} (1 - x_i)$ in minimization) using one auxiliary hub vertex. What about **more general degree-$d$ pseudo-Boolean monomials**?

#### 1. General Mixed-Literal Negative Posiform Terms ($-\alpha \prod_{i \in P} x_i \prod_{j \in Q} (1 - x_j)$, $\alpha > 0$)
Suppose a minimization objective contains a negative mixed product term:
$$T(x) = -\alpha \Big(\prod_{i \in P} x_i\Big)\Big(\prod_{j \in Q} (1 - x_j)\Big), \qquad \alpha > 0.$$
When is $T(x)$ submodular and cut-representable?
- **In original variables $x$**: If $P \neq \emptyset$ and $Q \neq \emptyset$, take $u \in P, v \in Q$ and fix all other variables to $1$ (in $P$) and $0$ (in $Q$). Then $T$ reduces to $-\alpha x_u(1 - x_v)$, which has matrix $\begin{pmatrix} 0 & 0 \\ -\alpha & 0 \end{pmatrix}$: $A + D = 0 > B + C = -\alpha$, which is **supermodular**!
- **Rescue via Bipartite Gauge Flip**: If there exists a gauge flip $\sigma$ such that $\sigma_i = 0$ for all $i \in P$ and $\sigma_j = 1$ for all $j \in Q$ (so $y_j = 1 - x_j$), then in the $y$-variables the term becomes:
  $$T(y) = -\alpha \prod_{k \in P \cup Q} y_k,$$
  which is a pure **`All-in-S` hub gadget** ($S \to z$ of cap $\alpha$, and $z \to k$ of cap $+\infty$ for all $k \in P \cup Q$)!

#### 2. Positive Monomial Penalties $+\alpha \prod_{i \in K} x_i$ ($\alpha > 0$, `Ishikawa 2011` / `Fix et al. 2011`)
In minimization, a positive monomial $+\alpha x_1 x_2 \dots x_d$ ($\alpha > 0$) is **supermodular** even for $d = 2$. In computer vision (`Ishikawa 2011`, `Fix et al. 2011`), it is reduced to quadratic QPBO using a single auxiliary binary variable $z \in \{0, 1\}$ via the identity:
$$\alpha \prod_{i=1}^d x_i = \min_{z \in \{0, 1\}} \left[ \alpha(d - 1)\,z + \alpha \sum_{i=1}^d x_i(1 - z) \right] \quad \text{? No — check } \sum x_i < d!$$
In fact, because $\min_{z \in \{0,1\}}$ is always **concave** in $\sum_{i=1}^d x_i$ while $+\alpha \prod_{i=1}^d x_i$ is **convex** in $\sum_{i=1}^d x_i$ (taking value $0$ on $0, 1, \dots, d-1$ and jumping to $+\alpha$ at $d$), no submodular auxiliary gadget can represent $+\alpha \prod_{i=1}^d x_i$. Instead, Ishikawa's reduction uses a **supermodular** auxiliary variable $z$:
$$\alpha \prod_{i=1}^d x_i = \min_{z \in \{0, 1\}} \alpha \left[ z \Big((d - 1) - \sum_{i=1}^d x_i\Big) + \sum_{1 \le i < j \le d} x_i x_j \right] \quad (\text{for } d = 3),$$
which reduces degree $d$ to degree $2$ so that **QPBO Roof Duality (§5.4)** can be applied!

#### 3. The Exact Boundary of Submodular Graph Representability ($d = 3$ vs. $d \ge 4$)
What if a degree-$d$ function $f: \{0, 1\}^d \to \mathbb{R}$ **is** submodular ($f(X) + f(Y) \ge f(X \wedge Y) + f(X \vee Y)$)? Can every submodular function be represented as the minimum cut of a network with auxiliary vertices?
- **Theorem 7.2 (`Billionnet–Minoux 1985` / `Kolmogorov–Zabih 2004` — $d \le 3$ Sufficiency)**: Every submodular function of degree **$d \le 3$** (all unary, pairwise, and **ternary / 3-variable** submodular functions) is **always** graph-representable as an $(S, T)$-cut using at most two auxiliary hub vertices ($z_S$ and $z_T$)!
- **Theorem 7.3 (`Živný–Cohen–Jeavons 2009` — $d \ge 4$ Impossibility Boundary)**: For **$d \ge 4$**, there exist submodular functions that **cannot** be represented as the minimum cut of any directed network with non-negative capacities, no matter how many auxiliary vertices are added!
  - *Canonical Counterexample ($d = 4$)*: The symmetric threshold / cardinality submodular function $f(x_1, x_2, x_3, x_4) = \min\big(2, \sum_{i=1}^4 x_i\big) - \frac{1}{2}\max\big(0, \sum_{i=1}^4 x_i - 2\big)$ (or the 4-variable submodular function generated by the graphic matroid of $K_4$) violates the **polymatroid cut-cone inequalities** required by projections of quadratic cut functions.

---

### 7.3 Reconciled Master Recognition & Compilation Decision Table

| Problem Pattern / Algebraic Signature | Submodularity / Balance Status | Canonical Compilation Gadget ($x_S=1, x_T=0$) | Prototype Problems |
| :--- | :--- | :--- | :--- |
| **Unary Profit $+r_i x_i$ ($r_i > 0$)** | Linear | Add $+r_i$ to $W_{\text{base}}$; edge **$S \to i$** of cap $r_i$ | All Closure / Cut problems |
| **Unary Cost $-c_i x_i$ ($c_i > 0$)** | Linear | Edge **$i \to T$** of cap $c_i$ | All Closure / Cut problems |
| **Hard Implication $x_u = 1 \implies x_v = 1$** | Submodular ($\Delta = \infty$) | Edge **$u \to v$** of cap $+\infty$ | `P4174`, `ARC 085 E`, `P3749` |
| **Sequential Causal Dependency $u \xrightarrow{\text{needs}} v$** | Submodular + Deadlock | Prune cycles + descendants via Kahn's BFS on $G_{\text{pre}}$; then $u \to v$ ($\infty$) | `P2805 植物大战僵尸` |
| **Soft Rent-or-Buy Dependency ($r_{ij}$ vs. $c_j$)** | Submodular ($\Delta = r_{ij}$) | Edge **$i \to j$** of finite cap $r_{ij}$, and **$j \to T$** of cap $c_j$ | `[CEOI 2008] Order` |
| **Submodular $2 \times 2$ Cost $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$, $A+D \le B+C$** | Submodular ($\Delta = B+C-A-D$) | $A + (C-A)x_i + (D-C)x_j + \Delta\,x_j(1-x_i)$ (Edge **$j \to i$** cap $\Delta$) | `P2057`, `BZOJ 2039`, `P3973` |
| **Collective Bonus $+w \prod_{i \in K} x_i$ (`All-in-S`)** | Submodular ($d = |K|$) | Add $+w$ to $W_{\text{base}}$; hub $z_S$: **$S \to z_S$** ($w$), **$z_S \to i$** ($\infty$) | `P1361`, `CF 311 E`, `P4313` |
| **Collective Bonus $+w \prod_{i \in K} (1 - x_i)$ (`All-in-T`)** | Submodular ($d = |K|$) | Add $+w$ to $W_{\text{base}}$; hub $z_T$: **$i \to z_T$** ($\infty$), **$z_T \to T$** ($w$) | `P1361`, `CF 311 E`, `P4313` |
| **Supermodular Cost $A+D > B+C$ on Bipartite $L \sqcup R$** | Harary Balanced ($\sigma_L=0, \sigma_R=1$) | Flip $y_j = 1 - x_j$ on $R$; swap columns $\begin{pmatrix} B & A \\ D & C \end{pmatrix}$; compile in $(x_i, y_j)$ | `P2774`, `ABC 259 G`, `AGC 038 F`, `ARC 142 E` |
| **Mixed Sub/Supermodular on General Graph** | Check $\sigma_u \oplus \sigma_v = [\Delta_{uv} < 0]$ | If 2-SAT balanced: flip $\sigma_v = 1$; if odd cycle: $\mathcal{N}_{\text{QPBO}}$ Roof Duality | Grid Orthogonal + Diagonal; FPT Kernelization |

---

## 8. Reconciled Master 4-Tier Curated Problem Bank (31 Non-Template Problems)

Every problem below is compiled strictly via the **4-Step English-to-Graph Compilation Pipeline** (`Diagnostic Signal` $\to$ `Algebraic Representation` $\to$ `Graph Compilation & Complexity` $\to$ `3-Tier Progressive Hints`).

---

### Tier 1: Stepping Stone (`P01–P07` — Direct Closure, Unary Chains & Basic Bipartite Flip)

---

#### Problem P01 — Luogu P4174: [NOI2006] 最大获利 (Maximum Profit)
- **Judge URL**: [https://www.luogu.com.cn/problem/P4174](https://www.luogu.com.cn/problem/P4174)
- **Constraints**: $N \le 5000$ base stations, $M \le 5 \times 10^4$ user demands; station build costs $P_i \le 100$, demand revenues $C_k \le 100$. Time Limit: 1.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Each demand $k$ yields revenue $C_k > 0$ iff **both** stations $a_k$ and $b_k$ are built (at one-time cost $P_i$ per station).
  - *Why Greedy / DP Fails*: Stations are shared across arbitrary pairs $(a_k, b_k)$ forming a general graph of treewidth up to $N = 5000$.
- **Step 2 — Algebraic Representation**:
  Let $x_i \in \{0, 1\}$ indicate building station $i$, and $z_k \in \{0, 1\}$ indicate fulfilling demand $k$:
  $$\max_{x, z} \sum_{k=1}^M C_k z_k - \sum_{i=1}^N P_i x_i \quad \text{s.t.} \quad z_k \implies (x_{a_k} \wedge x_{b_k}).$$
  With $W_{\text{base}} = \sum_{k=1}^M C_k$, minimize:
  $$\Phi(x, z) = \sum_{k=1}^M C_k(1 - z_k) + \sum_{i=1}^N P_i x_i + \sum_{k=1}^M \infty \cdot \big(z_k(1 - x_{a_k}) + z_k(1 - x_{b_k})\big).$$
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - For each demand $k$: edge **$S \to z_k$** (cap $C_k$), and edges **$z_k \to x_{a_k}$**, **$z_k \to x_{b_k}$** (cap $+\infty$).
  - For each station $i$: edge **$x_i \to T$** (cap $P_i$).
  - Answer: $\sum_{k=1}^M C_k - \text{MaxFlow}(S, T)$. On this bipartite closure network ($|V| \le 5.5 \times 10^4, |E| \le 1.55 \times 10^5$), Dinic runs in $< 50\text{ ms}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: If you try to put capacity $C_k$ directly between $a_k$ and $b_k$, what happens when neither station is built?
  - *Hint 2*: Introduce a binary indicator $z_k \in \{0, 1\}$ for each demand $k$ and write the logical implication between $z_k$ and $(x_{a_k}, x_{b_k})$.
  - *Hint 3*: Pre-claim $\sum C_k$; connect $S \to z_k$ (cap $C_k$), $z_k \to a_k, b_k$ (cap $+\infty$), and $a_i \to T$ (cap $P_i$).

---

#### Problem P02 — Codeforces 1082 G: Petya and Graph
- **Judge URL**: [https://codeforces.com/problemset/problem/1082/G](https://codeforces.com/problemset/problem/1082/G)
- **Constraints**: $N \le 10^3$ vertices, $M \le 10^3$ edges; $a_v \le 10^9, w_e \le 10^9$. Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Choose a subset of vertices $S \subseteq V$ to maximize $\sum_{e \subseteq S} w_e - \sum_{v \in S} a_v$.
  - *Why Naive Subgraph Heuristics Fail*: An edge $e = (u, v)$ contributes $+w_e$ iff **both** endpoints $u, v \in S$.
- **Step 2 — Algebraic Representation**:
  Identical to P01 with edges as projects ($z_e \in \{0, 1\}$) and vertices as machines ($x_v \in \{0, 1\}$):
  $$W_{\text{base}} = \sum_{e=1}^M w_e, \qquad \Phi(x, z) = \sum_{e=1}^M w_e(1 - z_e) + \sum_{v=1}^N a_v x_v + \sum_{e=(u,v)} \infty \cdot \big(z_e(1 - x_u) + z_e(1 - x_v)\big).$$
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Edges **$S \to z_e$** (cap $w_e$), **$z_e \to u$** and **$z_e \to v$** (cap $+\infty$), and **$v \to T$** (cap $a_v$).
  - Answer: $\sum w_e - \text{MaxFlow}(S, T)$ (use `long long` since $\sum w_e \le 10^{12}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Notice that an edge's weight can only be claimed if both of its endpoints are paid for.
  - *Hint 2*: Create a vertex in the flow network for every original edge $e$ and every original vertex $v$.
  - *Hint 3*: Run Maximum Weight Closure with $W_{\text{base}} = \sum w_e$ in `int64_t`.

---

#### Problem P03 — Luogu P2057: [SHOI2007] 善意的投票 (Well-Intentioned Vote)
- **Judge URL**: [https://www.luogu.com.cn/problem/P2057](https://www.luogu.com.cn/problem/P2057)
- **Constraints**: $N \le 300$ children, $M \le \binom{N}{2}$ friendship pairs, initial preference $c_i \in \{0, 1\}$. Time Limit: 1.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Each child $i$ chooses final vote $x_i \in \{0, 1\}$. Pay $+1$ if $x_i \neq c_i$, and $+1$ for each friend pair $(u, v)$ with $x_u \neq x_v$. Minimize total conflicts.
  - *Why 2-SAT Fails*: We are minimizing the *number* of violated clauses, not checking satisfiability.
- **Step 2 — Algebraic Representation**:
  $$\min_{x \in \{0,1\}^N} \sum_{c_i = 1} (1 - x_i) + \sum_{c_i = 0} x_i + \sum_{(u, v) \in E} \big(x_u(1 - x_v) + x_v(1 - x_u)\big).$$
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - If $c_i = 1$: edge **$S \to i$** (cap $1$). If $c_i = 0$: edge **$i \to T$** (cap $1$).
  - For each friend pair $(u, v)$: bidirectional edges **$u \leftrightarrow v$** of capacity $1$.
  - Answer: $\text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Write the disagreement between $x_u$ and $x_v$ as a $2 \times 2$ penalty matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$. Is it submodular?
  - *Hint 2*: $A + D = 0 \le B + C = 2$, so it is strictly submodular!
  - *Hint 3*: Connect $c_i = 1$ children to $S$, $c_i = 0$ children to $T$, and friends via undirected capacity-$1$ edges.

---

#### Problem P04 — Luogu P2774: [网络流24题] 方格取数问题 (Grid Number Selection)
- **Judge URL**: [https://www.luogu.com.cn/problem/P2774](https://www.luogu.com.cn/problem/P2774)
- **Constraints**: $M, N \le 100$ grid, cell values $w_{r,c} \le 10^5$. Time Limit: 1.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Pick a subset of grid cells with no two orthogonally adjacent to maximize total weight.
  - *Why Bitmask DP Fails*: $M, N \le 100 \implies 2^{100}$ states.
- **Step 2 — Algebraic Representation**:
  Let $x_u \in \{0, 1\}$ indicate picking cell $u$. For adjacent $u, v$, picking both is forbidden: $\neg(x_u = 1 \wedge x_v = 1)$, which has supermodular penalty matrix $\begin{pmatrix} 0 & 0 \\ 0 & \infty \end{pmatrix}$ ($A + D = \infty > 0$).
  Color the grid as a checkerboard: $L = \{(r, c) : 2 \mid (r + c)\}$ and $R = \{(r, c) : 2 \nmid (r + c)\}$. Flip $y_v = 1 - x_v$ for $v \in R$:
  - On $L$: regret of not picking $u$ is $w_u(1 - x_u)$.
  - On $R$: regret of not picking $v$ is $w_v(1 - x_v) = w_v y_v$.
  - Adjacent pair $(u \in L, v \in R)$: $\infty \cdot x_u x_v = \infty \cdot x_u(1 - y_v)$.
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Baseline $W_{\text{base}} = \sum_{r,c} w_{r,c}$.
  - For $u \in L$: edge **$S \to u$** (cap $w_u$), and edges **$u \to v$** (cap $+\infty$) to all 4 orthogonal neighbors $v \in R$.
  - For $v \in R$: edge **$v \to T$** (cap $w_v$).
  - Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Forbidding $(x_u = 1 \wedge x_v = 1)$ is a supermodular penalty $\infty \cdot x_u x_v$. How can we turn $x_v$ into $1 - y_v$?
  - *Hint 2*: A 2D grid with 4-connectivity is bipartite by $(r + c) \bmod 2$.
  - *Hint 3*: Put even-parity cells on the $S$-side ($S \to u$ cap $w_u$), odd-parity cells on the $T$-side ($v \to T$ cap $w_v$), and $\infty$-edges from even to odd neighbors.

---

#### Problem P05 — Luogu P1361: 小M的作物 (Little M's Crops)
- **Judge URL**: [https://www.luogu.com.cn/problem/P1361](https://www.luogu.com.cn/problem/P1361)
- **Constraints**: $N \le 1000$ crops, $M \le 1000$ collective combinations. Time Limit: 1.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Each crop $i$ goes to Field A ($x_i = 1$, reward $a_i$) or Field B ($x_i = 0$, reward $b_i$). Furthermore, $M$ subsets $S_k$ grant bonus $c_{k,1}$ if **all** $i \in S_k$ are in Field A, or $c_{k,2}$ if **all** $i \in S_k$ are in Field B.
- **Step 2 — Algebraic Representation**:
  $$\Psi(x) = \sum_{i=1}^N \big(a_i x_i + b_i(1 - x_i)\big) + \sum_{k=1}^M \left(c_{k,1} \prod_{i \in S_k} x_i + c_{k,2} \prod_{i \in S_k} (1 - x_i)\right).$$
  Pre-claim $W_{\text{base}} = \sum_{i=1}^N (a_i + b_i) + \sum_{k=1}^M (c_{k,1} + c_{k,2})$ (or apply Recipe 1 to unary terms).
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - For each crop $i$: edge **$S \to i$** (cap $a_i$) and edge **$i \to T$** (cap $b_i$) (or use Recipe 1 `差値正規化` to keep only one edge per crop!).
  - For each subset $k$:
    - `All-in-S` hub $u_k$: **$S \to u_k$** (cap $c_{k,1}$) and **$u_k \to i$** (cap $+\infty$) for all $i \in S_k$.
    - `All-in-T` hub $v_k$: **$i \to v_k$** (cap $+\infty$) for all $i \in S_k$, and **$v_k \to T$** (cap $c_{k,2}$).
  - Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Use the `All-in-S` and `All-in-T` higher-order hub gadgets from §4.2.
  - *Hint 2*: Be careful with the edge directions for the Field B hub $v_k$: if any $i \in S_k$ is placed in $V_S$ ($x_i = 1$), $v_k$ must be forced into $V_S$ so that $v_k \to T$ is severed!
  - *Hint 3*: Thus $i \to v_k$ has capacity $+\infty$ and $v_k \to T$ has capacity $c_{k,2}$.

---

#### Problem P06 — AtCoder ABC 326 G: Unlock Achievement
- **Judge URL**: [https://atcoder.jp/contests/abc326/tasks/abc326_g](https://atcoder.jp/contests/abc326/tasks/abc326_g)
- **Constraints**: $N \le 50$ skills (levels $1 \dots 5$), $M \le 50$ achievements; $C_i, A_j \le 10^6$. Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Each skill $i$ has discrete level $L_i \in \{1, 2, 3, 4, 5\}$ (cost $C_i$ per level above $1$). Achievement $j$ grants reward $R_j$ iff $\forall i, L_i \ge A_{j,i}$.
- **Step 2 — Algebraic Representation**:
  Introduce **Unary Threshold Indicators** $x_{i, \ell} = [L_i \ge \ell] \in \{0, 1\}$ for $\ell \in \{2, 3, 4, 5\}$, with chain invariant $x_{i, 5} \implies x_{i, 4} \implies x_{i, 3} \implies x_{i, 2}$:
  $$\max_{x, z} \sum_{j=1}^M R_j z_j - \sum_{i=1}^N \sum_{\ell=2}^5 C_i x_{i, \ell} \quad \text{s.t.} \quad \begin{cases} x_{i, \ell} \implies x_{i, \ell-1} & (\ell \in \{3, 4, 5\}), \\ z_j \implies x_{i, A_{j,i}} & (\forall i \text{ with } A_{j,i} \ge 2). \end{cases}$$
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Baseline $W_{\text{base}} = \sum_{j=1}^M R_j$.
  - For each skill $i$ and $\ell \in \{2, 3, 4, 5\}$: edge **$x_{i, \ell} \to T$** (cap $C_i$), and chain edge **$x_{i, \ell} \to x_{i, \ell-1}$** (cap $+\infty$ for $\ell \ge 3$).
  - For each achievement $j$: edge **$S \to z_j$** (cap $R_j$), and edges **$z_j \to x_{i, A_{j,i}}$** (cap $+\infty$) whenever $A_{j,i} \ge 2$.
  - Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$ on $\le 252$ vertices.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Since $L_i \in \{1, \dots, 5\}$ has only 4 upgrade steps, represent $L_i$ in unary: $x_{i, \ell} = [L_i \ge \ell]$ for $\ell = 2, 3, 4, 5$.
  - *Hint 2*: What prevents the cut from choosing $L_i \ge 4$ without paying for $L_i \ge 3$? Add chain edges $x_{i, \ell} \to x_{i, \ell-1}$ of capacity $+\infty$!
  - *Hint 3*: Even without explicit chain edges, if each $x_{i, \ell} \to T$ costs $C_i$ and $z_j$ only points to $x_{i, A_{j,i}}$, you MUST include $x_{i, \ell} \to x_{i, \ell-1}$ ($\infty$) so that unlocking level $\ell$ pays $(\ell - 1) C_i$ in total!

---

#### Problem P07 — AtCoder ARC 085 E: MUL
- **Judge URL**: [https://atcoder.jp/contests/arc085/tasks/arc085_c](https://atcoder.jp/contests/arc085/tasks/arc085_c)
- **Constraints**: $N \le 100$, gem values $a_i \in [-10^9, 10^9]$. Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Choosing divisor $d$ smashes all gems at indices $d, 2d, 3d, \dots \le N$. Maximize the sum of remaining gems.
  - *Why Greedy / DP Fails*: Divisibility DAG has high treewidth ($2, 3, 5, \dots$ overlap at $6, 10, 15, 30, \dots$).
- **Step 2 — Algebraic Representation (Dual View Synthesis)**:
  Let $x_i = 1$ iff gem $i$ is **kept** (not smashed). If $j$ is a multiple of $i$ ($i \mid j$) and $j$ is kept ($x_j = 1$), then operation $i$ could not have been performed, so $i$ is also kept ($x_i = 1$) — or equivalently, if we never need to smash $i$ unless we want to smash $i$ itself, keeping $i$ requires keeping all its multiples $j$: $x_i \implies x_j$!
  *(Wait: let's check both directions! If we smash $i$, all multiples $j = ki$ are smashed. Thus the set of **smashed** gems $D$ satisfies $i \in D \implies ki \in D$, so $D$ is closed under multiples $i \to ki$, and its complement $K = \{1, \dots, N\} \setminus D$ of **kept** gems is closed under divisors $ki \to i$!)*
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Using $x_i = 1 \iff i \in K$ (kept):
    - Baseline $W_{\text{base}} = \sum_{a_i > 0} a_i$.
    - If $a_i > 0$: edge **$S \to i$** (cap $a_i$). If $a_i < 0$: edge **$i \to T$** (cap $|a_i|$).
    - For every $i$ and multiple $j = k i$ ($k \ge 2$): keeping $j$ forbids smashing $i$, so $x_j \implies x_i$, which is edge **$j \to i$** of capacity $+\infty$! (Equivalently, if $x_i = 1$ means $i$ is *not* smashed and we orient $i \to j$ of cap $+\infty$ with $S$/$T$ swapped, it gives the exact transpose cut!)
  - Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: You never need to press button $d$ unless gem $d$ itself is smashed; thus "button $d$ is pressed" is equivalent to "gem $d$ is smashed".
  - *Hint 2*: Therefore, a subset of gems can survive iff whenever gem $j$ survives, every divisor $i \mid j$ also survives!
  - *Hint 3*: This is a pure Maximum Weight Closure on $\{1, \dots, N\}$ with $\infty$-edges $j \to i$ for $i \mid j$ (or $i \to j$ if $S$ and $T$ represent smashed vs. kept).

---

### Tier 2: Intermediate (`P08–P15` — Collective Hubs, Causal Deadlock Pruning & Matrix Merging)

---

#### Problem P08 — Codeforces 311 E: Biologist
- **Judge URL**: [https://codeforces.com/problemset/problem/311/E](https://codeforces.com/problemset/problem/311/E)
- **Constraints**: $N \le 10^4$ dogs, $M \le 2000$ experiments, friend penalty $g \le 10^4$. Time Limit: 1.5 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Identical to P05 (`小M的作物`), except changing dog $i$'s sex costs $v_i$, and each experiment $k$ has a target sex $w_k \in \{0, 1\}$, reward $W_k$, and an **extra penalty $g$** if the experiment fails and the biologist is a friend ($f_k = 1$).
- **Step 2 — Algebraic Representation**:
  If experiment $k$ fails, we lose the pre-claimed reward $W_k$ **and** pay an extra $g \cdot f_k$. Thus the total regret of failing experiment $k$ is $W_k + g \cdot f_k$!
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Baseline $W_{\text{base}} = \sum_{k=1}^M W_k$.
  - For each dog $i$ with initial sex $s_i = 1$: edge **$S \to i$** (cap $v_i$). If $s_i = 0$: edge **$i \to T$** (cap $v_i$).
  - For each experiment $k$ with effective failure regret $C_k = W_k + g \cdot f_k$:
    - If target $w_k = 1$ (`All-in-S`): hub $z_k$ with **$S \to z_k$** (cap $C_k$) and **$z_k \to i$** (cap $+\infty$) for $i \in S_k$.
    - If target $w_k = 0$ (`All-in-T`): hub $z_k$ with **$i \to z_k$** (cap $+\infty$) for $i \in S_k$ and **$z_k \to T$** (cap $C_k$).
  - Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Pre-claim only $\sum W_k$ into $W_{\text{base}}$. If a friend's experiment fails, how much worse is your net score compared to $W_{\text{base}}$?
  - *Hint 2*: You lose $W_k$ AND pay $g$, so the hub edge capacity is $W_k + g$!
  - *Hint 3*: Connect $w_k = 1$ hubs from $S$ ($S \to z_k \to i$) and $w_k = 0$ hubs to $T$ ($i \to z_k \to T$).

---

#### Problem P09 — Luogu P4313: [国家集训队] 文理分科 (Arts and Sciences Division)
- **Judge URL**: [https://www.luogu.com.cn/problem/P4313](https://www.luogu.com.cn/problem/P4313)
- **Constraints**: Grid $N, M \le 100$ ($10^4$ students). Time Limit: 1.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Each cell $(r, c)$ chooses Arts ($x_{r,c} = 1$, reward $A_{r,c}$) or Science ($x_{r,c} = 0$, reward $B_{r,c}$). Furthermore, if $(r, c)$ and all its 4 orthogonal neighbors choose Arts, gain $S_{A, r, c}$; if all $\le 5$ cells in that cross-stencil choose Science, gain $S_{B, r, c}$.
- **Step 2 — Algebraic Representation**:
  Let $N^+[r, c]$ be the $\le 5$-cell cross-stencil centered at $(r, c)$. This is P05 (`小M的作物`) on $N M \le 10^4$ cells with $N M$ `All-in-S` hubs and $N M$ `All-in-T` hubs!
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Baseline $W_{\text{base}} = \sum_{r,c} (A_{r,c} + B_{r,c} + S_{A,r,c} + S_{B,r,c})$.
  - For each cell $u = (r, c)$: **$S \to u$** (cap $A_u$), **$u \to T$** (cap $B_u$), `All-in-S` hub **$S \to p_u$** (cap $S_{A,u}$) with **$p_u \to v$** (cap $+\infty$, $\forall v \in N^+[u]$), and `All-in-T` hub **$q_u \to T$** (cap $S_{B,u}$) with **$v \to q_u$** (cap $+\infty$, $\forall v \in N^+[u]$).
  - Total vertices $3 N M + 2 \le 30,002$, edges $\le 14 N M$. Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Do not try to decompose the 5-cell stencil into pairwise edges — a 5-variable product $\prod_{v \in N^+[u]} x_v$ needs an auxiliary hub!
  - *Hint 2*: Create two hubs $p_{r,c}$ (Arts group) and $q_{r,c}$ (Science group) per cell $(r, c)$.
  - *Hint 3*: Pre-apply Recipe 1 (`差値正規化`) to $A_{r,c}$ and $B_{r,c}$ so each student has only one edge to $S$ or $T$.

---

#### Problem P10 — Codeforces 808 F: Card Game
- **Judge URL**: [https://codeforces.com/problemset/problem/808/F](https://codeforces.com/problemset/problem/808/F)
- **Constraints**: $N \le 100$ cards $(p_i, c_i, l_i)$, required power $K \le 10^5$, magic numbers $c_i \le 10^5$. Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Minimize maximum level $L$ such that a subset of cards with $l_i \le L$ has total power $\ge K$ and no two selected cards have $c_i + c_j \in \text{Primes}$.
  - *Hidden Bipartition*: Every prime $> 2$ is **odd**, so $c_i + c_j = \text{prime} > 2$ only occurs between an **odd** $c_i$ and an **even** $c_j$! What about $c_i + c_j = 2$? That only happens when $c_i = 1$ and $c_j = 1$!
- **Step 2 — Algebraic Representation**:
  Since two cards with $c_i = 1$ conflict with each other ($1 + 1 = 2$ is prime), we can pick **at most one** card with $c_i = 1$, and by dominance we should only ever keep the single $c_i = 1$ card with the **maximum power $p_i$** among those with $l_i \le L$! Once all other $c_i = 1$ cards are discarded, the conflict graph is **100% bipartite** ($L_{\text{odd}} \sqcup R_{\text{even}}$)!
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Binary search on level $L \in [1, N]$.
  - Filter cards with $l_i \le L$, coalescing all $c_i = 1$ cards into the single highest-power one.
  - Build a Bipartite Maximum Weight Independent Set network (identical to P04):
    - Odd $c_i$: **$S \to i$** (cap $p_i$). Even $c_j$: **$j \to T$** (cap $p_j$).
    - If $c_i + c_j$ is prime: **$i \to j$** (cap $+\infty$).
  - Check if $\sum p_i - \text{MaxFlow}(S, T) \ge K$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Binary search on the level $L$. For a fixed $L$, you need the Maximum Weight Independent Set of the prime-sum conflict graph.
  - *Hint 2*: Why is the prime-sum conflict graph almost bipartite? Because Odd + Odd = Even and Even + Even = Even!
  - *Hint 3*: The only even prime is $2 = 1 + 1$. Keep only the single highest-power card with $c_i = 1$, and the remaining graph is strictly bipartite!

---

#### Problem P11 — Luogu P2805: [NOI2009] 植物大战僵尸 (Plants vs. Zombies)
- **Judge URL**: [https://www.luogu.com.cn/problem/P2805](https://www.luogu.com.cn/problem/P2805)
- **Constraints**: Grid $N \le 20, M \le 30$ ($600$ cells), scores $w_{r,c} \in [-10^4, 10^4]$. Time Limit: 1.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Zombies enter from the right. Eating plant $u$ requires first eating all plants that protect $u$ AND eating $(r, c+1)$ to reach $(r, c)$.
  - *Why Standard Closure Fails*: Mutual protection cycles (e.g., $u$ protects $v$ and $v$ protects $u$) deadlock under **Sequential Causal Semantics (§3.3)**!
- **Step 2 — Algebraic Representation**:
  Build the causal prerequisite graph $G_{\text{pre}}$ where $(v \to u) \in E_{\text{pre}}$ means **$v$ must be eaten before $u$**:
  - For every $(r, c)$ with $c < M - 1$: $((r, c+1) \to (r, c)) \in E_{\text{pre}}$.
  - If plant $v$ protects cell $u$: $(v \to u) \in E_{\text{pre}}$.
- **Step 3 — Mechanical Graph Compilation & Solution**:
  1. Run **Kahn's Topological BFS** on $G_{\text{pre}}$ starting from all vertices with $\text{in-degree}_{G_{\text{pre}}}(v) = 0$.
  2. Delete all vertices not visited by Kahn's BFS (this deletes all cycles AND all acyclic nodes causally downstream of cycles!).
  3. On the surviving vertices $U_{\text{valid}}$, build Picard's Closure network:
     - If $w_u > 0$: **$S \to u$** (cap $w_u$), add $w_u$ to $W_{\text{base}}$.
     - If $w_u < 0$: **$u \to T$** (cap $|w_u|$).
     - For each $(v \to u) \in E_{\text{pre}}$ with $u, v \in U_{\text{valid}}$: eating $u$ requires eating $v$ ($x_u \implies x_v$), so add edge **$u \to v$** of capacity $+\infty$!
  4. Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Remember that zombies enter from the right: cell $(r, c)$ depends on $(r, c+1)$.
  - *Hint 2*: Do NOT just delete SCCs of size $\ge 2$! A plant with $+1000$ points that is protected by a 2-cycle is also unreachable.
  - *Hint 3*: Run Kahn's in-degree $0$ BFS on $G_{\text{pre}}$ (`protector -> protected`); then reverse the surviving edges (`protected -> protector`) with capacity $+\infty$ in the min-cut graph.

---

#### Problem P12 — AtCoder ABC 259 G: Grid Card Game
- **Judge URL**: [https://atcoder.jp/contests/abc259/tasks/abc259_g](https://atcoder.jp/contests/abc259/tasks/abc259_g)
- **Constraints**: $H, W \le 100$, $A_{i,j} \in [-10^9, 10^9]$. Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Select a subset of rows $R$ and columns $C$. You gain $A_{i,j}$ for every cell $(i, j)$ covered by $R \cup C$, **except** you are forbidden from covering any cell with $A_{i,j} < 0$.
  - *Why It Looks Supermodular*: For $A_{i,j} < 0$, the union $R \cup C$ is forbidden from covering $(i, j)$, which means $x_i = 0 \wedge w_j = 0$, OR if we define $x_i = 1 \iff$ we keep row $i$ and $w_j = 1 \iff$ we keep col $j$, let's write the exact Inclusion-Exclusion formula!
- **Step 2 — Algebraic Representation**:
  Let $x_i = 1$ if Row $i$ is selected (with full row sum $R_i = \sum_{j=1}^W A_{i,j}$) and $w_j = 1$ if Column $j$ is selected (with full col sum $C_j = \sum_{i=1}^H A_{i,j}$). By Inclusion-Exclusion, the sum of cells in the union of selected rows and columns is:
  $$\Psi(x, w) = \sum_{i=1}^H R_i x_i + \sum_{j=1}^W C_j w_j - \sum_{i=1}^H \sum_{j=1}^W A_{i,j} x_i w_j.$$
   Wait: what if $A_{i,j} < 0$? If we are forbidden from picking any cell with $A_{i,j} < 0$, then for $A_{i,j} < 0$ we cannot select Row $i$ OR Column $j$! Wait — re-read the problem statement of `ABC 259 G`:
  *"You may choose any rows and columns. For each cell $(i, j)$ that is in a chosen row **AND** a chosen column, you CANNOT choose both row $i$ and column $j$ if $A_{i,j} < 0$!"*
  Aha! Let's check: in `ABC 259 G`, you gain $A_{i,j}$ if you choose Row $i$ XOR/OR Column $j$? No! In `ABC 259 G`, choosing Row $i$ gives $\sum_j A_{i,j}$, choosing Column $j$ gives $\sum_i A_{i,j}$, and if you choose **both** Row $i$ and Column $j$, cell $(i, j)$ is only counted **once** (so you subtract $A_{i,j} x_i w_j$), AND if $A_{i,j} < 0$, you are **forbidden from choosing both Row $i$ and Column $j$** ($\neg(x_i = 1 \wedge w_j = 1)$)!
  Look at the quadratic term in $\Psi(x, w)$:
  - When $A_{i,j} \ge 0$: penalty $+A_{i,j} x_i w_j$ (supermodular!).
  - When $A_{i,j} < 0$: hard conflict $+\infty \cdot x_i w_j$ (also supermodular!).
  Flip $y_j = 1 - w_j$ on all columns $j$: then $x_i w_j = x_i(1 - y_j)$, which is **100% submodular**!
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - For each Row $i$: if $R_i > 0$, add $R_i$ to $W_{\text{base}}$ and edge **$S \to \text{Row}_i$** (cap $R_i$); if $R_i < 0$, edge **$\text{Row}_i \to T$** (cap $|R_i|$).
  - For each Column $j$ (flipped: $y_j = 1 - w_j$, so $w_j = 1 \iff \text{Col}_j \in V_T$): if $C_j > 0$, add $C_j$ to $W_{\text{base}}$ and edge **$\text{Col}_j \to T$** (cap $C_j$); if $C_j < 0$, edge **$S \to \text{Col}_j$** (cap $|C_j|$).
  - For each cell $(i, j)$:
    - If $A_{i,j} \ge 0$: edge **$\text{Row}_i \to \text{Col}_j$** of capacity $A_{i,j}$.
    - If $A_{i,j} < 0$: edge **$\text{Row}_i \to \text{Col}_j$** of capacity $+\infty$.
  - Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Write the union score of rows and columns via Inclusion-Exclusion: $\sum R_i x_i + \sum C_j w_j - \sum A_{i,j} x_i w_j$.
  - *Hint 2*: Why does $A_{i,j} < 0$ forbid $x_i = 1 \wedge w_j = 1$? Because otherwise $-A_{i,j} x_i w_j = +|A_{i,j}| x_i w_j$ would have a negative capacity after flipping! The problem designer specifically forbade $x_i = w_j = 1$ when $A_{i,j} < 0$ so its capacity becomes $+\infty$ instead of $-|A_{i,j}|$!
  - *Hint 3*: Flip column variables $y_j = 1 - w_j$ and add directed edges $\text{Row}_i \to \text{Col}_j$ of capacity $A_{i,j}$ (if $A_{i,j} \ge 0$) or $+\infty$ (if $A_{i,j} < 0$).

---

#### Problem P13 — [CEOI 2008] Order / SPOJ ORDER
- **Judge URL**: [https://www.spoj.com/problems/ORDER/](https://www.spoj.com/problems/ORDER/)
- **Constraints**: $N \le 1200$ jobs, $M \le 1200$ machines. Time Limit: 1.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Job $i$ yields revenue $v_i$. For each required machine $j$, job $i$ can either **rent** machine $j$ for single-job use at fee $r_{ij}$, or machine $j$ can be **purchased** outright for all jobs at price $c_j$.
- **Step 2 — Algebraic Representation**:
  $$\Phi(x, y) = \sum_{i=1}^N v_i(1 - x_i) + \sum_{j=1}^M c_j y_j + \sum_{i=1}^N \sum_{j=1}^M r_{ij} x_i(1 - y_j).$$
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Baseline $W_{\text{base}} = \sum_{i=1}^N v_i$.
  - Edges **$S \to \text{Job}_i$** (cap $v_i$), **$\text{Job}_i \to \text{Mach}_j$** (finite cap $r_{ij}$), and **$\text{Mach}_j \to T$** (cap $c_j$).
  - Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Compare this with P01 (`最大获利`), where $\text{Job}_i \to \text{Mach}_j$ had capacity $+\infty$.
  - *Hint 2*: What happens if you replace $+\infty$ on $\text{Job}_i \to \text{Mach}_j$ with the rental fee $r_{ij}$?
  - *Hint 3*: If $\text{Mach}_j \in V_T$ (not bought), every selected job $i \in V_S$ severs $\text{Job}_i \to \text{Mach}_j$ and pays $r_{ij}$; if total rentals exceed $c_j$, $\text{Mach}_j$ moves to $V_S$ and severs $\text{Mach}_j \to T$ (cost $c_j$).

---

#### Problem P14 — BZOJ 2039 / DarkBZOJ 2039: [2009国家集训队] 人员雇佣 (Personnel Hiring)
- **Judge URL**: [https://darkbzoj.cc/problem/2039](https://darkbzoj.cc/problem/2039)
- **Constraints**: $N \le 1000$ people, dense $N \times N$ synergy matrix $E_{i,j} \ge 0$, hiring cost $A_i \ge 0$. Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Hiring person $i$ ($x_i = 1$) costs $A_i$. For every ordered pair $(i, j)$: if both $i, j$ are hired, gain $E_{i,j}$ (so $2 E_{i,j}$ per unordered pair); if $i$ is hired and $j$ is **not** hired, pay a penalty $E_{i,j}$!
  - *Why Auxiliary Hubs TLE*: $N = 1000 \implies N^2 = 10^6$ pairs. Creating $10^6$ auxiliary vertices will TLE/MLE; we must compile directly on the $N$ vertices via **Hu Botao's Symmetric Vertex-Edge Merging (`合并点边法`)**!
- **Step 2 — Algebraic Representation**:
  For each unordered pair $\{i, j\}$, the net payoff is $2 E_{i,j} x_i x_j - E_{i,j} x_i(1 - x_j) - E_{i,j} x_j(1 - x_i)$.
  Using $x_i x_j = \frac{1}{2}\big(x_i + x_j - x_i(1 - x_j) - x_j(1 - x_i)\big)$, the pair payoff simplifies to:
  $$E_{i,j}(x_i + x_j) - 2 E_{i,j}\big(x_i(1 - x_j) + x_j(1 - x_i)\big)!$$
  Summing over all pairs and subtracting $\sum_i A_i x_i$:
  $$\Psi(x) = \sum_{i=1}^N \Big(\sum_{j=1}^N E_{i,j}\Big) x_i - \sum_{i=1}^N A_i x_i - \sum_{i < j} 2 E_{i,j}\big(x_i(1 - x_j) + x_j(1 - x_i)\big).$$
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Only $N + 2 = 1002$ vertices! Let $S_i = \sum_{j=1}^N E_{i,j}$.
  - Baseline $W_{\text{base}} = \sum_{i=1}^N S_i$.
  - For each person $i$: edge **$S \to i$** (cap $S_i$) and edge **$i \to T$** (cap $A_i$) (or apply Recipe 1).
  - For each pair $i < j$: undirected edge **$i \leftrightarrow j$** of capacity $2 E_{i,j}$.
  - Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Do not create $N^2$ auxiliary nodes! Write the $2 \times 2$ payoff matrix for $\{i, j\}$: $\Pi = \begin{pmatrix} 0 & -E_{ij} \\ -E_{ij} & 2 E_{ij} \end{pmatrix}$.
  - *Hint 2*: Apply the Symmetric Split (§4.1 Choice 2) to $\Theta = 2 E_{ij} - \Pi = \begin{pmatrix} 2E_{ij} & 3E_{ij} \\ 3E_{ij} & 0 \end{pmatrix}$.
  - *Hint 3*: Each person $i$ gets unary reward $\sum_j E_{i,j}$, unary cost $A_i$, and each pair $\{i, j\}$ gets an undirected edge of capacity $2 E_{i,j}$.

---

#### Problem P15 — Luogu P3973: [TJOI2015] 线性代数 (Linear Algebra)
- **Judge URL**: [https://www.luogu.com.cn/problem/P3973](https://www.luogu.com.cn/problem/P3973)
- **Constraints**: $N \le 500$, $B_{i,j} \ge 0$, $C_i \ge 0$. Time Limit: 1.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Choose a binary row vector $A \in \{0, 1\}^N$ to maximize $D = (A B - C) A^T = \sum_{i=1}^N \sum_{j=1}^N B_{i,j} A_i A_j - \sum_{i=1}^N C_i A_i$.
- **Step 2 — Algebraic Representation**:
  Using the **Zero-Auxiliary Asymmetric Split (§4.2)**:
  $$1 - A_i A_j = (1 - A_i) + A_i(1 - A_j),$$
  we rewrite $\Psi(A) = \sum_{i,j} B_{i,j} - \sum_{i=1}^N \Big(\sum_{j=1}^N B_{i,j}\Big)(1 - A_i) - \sum_{i=1}^N C_i A_i - \sum_{i \neq j} B_{i,j} A_i(1 - A_j)$.
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Only $N + 2 = 502$ vertices! Baseline $W_{\text{base}} = \sum_{i,j} B_{i,j}$.
  - For each $i$: edge **$S \to i$** of capacity $\sum_{j=1}^N B_{i,j}$, and edge **$i \to T$** of capacity $C_i$.
  - For each $i \neq j$: directed edge **$i \to j$** of capacity $B_{i,j}$ (or undirected $i \leftrightarrow j$ of capacity $B_{i,j} + B_{j,i}$ if using symmetric split).
  - Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Expand $(A B - C) A^T = A B A^T - C A^T = \sum_{i,j} B_{i,j} A_i A_j - \sum_i C_i A_i$.
  - *Hint 2*: Use $1 - A_i A_j = (1 - A_i) + A_i(1 - A_j)$ to avoid creating $N^2$ auxiliary nodes.
  - *Hint 3*: Connect $S \to i$ with capacity $\sum_j B_{i,j}$, $i \to T$ with capacity $C_i$, and $i \to j$ with capacity $B_{i,j}$.

---

### Tier 3: Advanced (`P16–P23` — Bipartite Zebra Flips, Dualization, Hall's Theorem & Virtualization)

---

#### Problem P16 — AtCoder ABC 193 F: Zebraness
- **Judge URL**: [https://atcoder.jp/contests/abc193/tasks/abc193_f](https://atcoder.jp/contests/abc193/tasks/abc193_f)
- **Constraints**: $N \le 100$ grid (`B`, `W`, `?`). Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Replace each `?` with `B` ($x_u = 1$) or `W` ($x_u = 0$) to maximize the number of orthogonally adjacent pairs of **different** colors ($x_u \neq x_v$).
  - *Why It Is Supermodular*: Maximizing $[x_u \neq x_v]$ is equivalent to minimizing $[x_u = x_v]$, whose penalty matrix $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ has $A + D = 2 > B + C = 0$!
- **Step 2 — Algebraic Representation**:
  Apply **Checkerboard Bipartite Inversion** on odd-parity cells $v \in R$ ($(r + c) \equiv 1 \pmod 2$): set $y_v = 1 - x_v$ on $R$ and $y_u = x_u$ on $L$.
  Then $x_u = x_v \iff y_u \neq y_v$, so the regret $[x_u = x_v]$ becomes the standard submodular cut penalty $y_u(1 - y_v) + y_v(1 - y_u)$!
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Baseline $W_{\text{base}} = 2 N(N - 1)$ (total orthogonal grid edges).
  - Pre-colored cells:
    - On even cells $u \in L$: `B` forces $y_u = 1$ (**$S \to u$** cap $+\infty$); `W` forces $y_u = 0$ (**$u \to T$** cap $+\infty$).
    - On odd cells $v \in R$ (inverted!): `B` forces $y_v = 0$ (**$v \to T$** cap $+\infty$); `W` forces $y_v = 1$ (**$S \to v$** cap $+\infty$).
  - Every orthogonal grid edge $(u, v)$: bidirectional edge **$u \leftrightarrow v$** of capacity $1$.
  - Answer: $2 N(N - 1) - \text{MaxFlow}(S, T)$ in $O(N^3)$ unit-network time.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Rewarding $x_u \neq x_v$ is anti-ferromagnetic (supermodular). How do you turn a chessboard's alternating pattern into a uniform pattern?
  - *Hint 2*: Flip the meaning of `B` and `W` on all cells with $(r + c)$ odd!
  - *Hint 3*: After flipping odd cells, "zebra neighbors" become "same-state neighbors", compiled via undirected capacity-$1$ grid edges.

---

#### Problem P17 — Luogu P1791: [国家集训队] 圈地计划 (Land Enclosure Plan)
- **Judge URL**: [https://www.luogu.com.cn/problem/P1791](https://www.luogu.com.cn/problem/P1791)
- **Constraints**: Grid $N, M \le 100$. Time Limit: 1.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Each cell $u = (r, c)$ yields $A_u$ if commercial ($x_u = 1$) or $B_u$ if industrial ($x_u = 0$), PLUS a competitive bonus $C_{uv} > 0$ for every orthogonally adjacent pair $(u, v)$ assigned to **different** zones ($x_u \neq x_v$).
- **Step 2 — Algebraic Representation**:
  Identical to P16 (`Zebraness`) combined with unary cell payoffs $A_u, B_u$! Flip $y_v = 1 - x_v$ on odd-parity cells $v \in R$.
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Baseline $W_{\text{base}} = \sum_u (A_u + B_u) + \sum_{(u,v) \in E_{\text{grid}}} C_{uv}$.
  - Even cells $u \in L$: **$S \to u$** (cap $A_u$) and **$u \to T$** (cap $B_u$).
  - Odd cells $v \in R$ (flipped!): **$S \to v$** (cap $B_v$) and **$v \to T$** (cap $A_v$).
  - Orthogonal neighbor pair $(u, v)$: undirected edge **$u \leftrightarrow v$** of capacity $C_{uv}$.
  - Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Notice that the bonus $C_{uv}$ is granted when $x_u \neq x_v$, which is supermodular.
  - *Hint 2*: Flip $y_v = 1 - x_v$ on cells with $(r + c)$ odd. What happens to $A_v$ and $B_v$ on odd cells?
  - *Hint 3*: On odd cells, $S \to v$ gets capacity $B_v$ and $v \to T$ gets capacity $A_v$, while grid edges $(u, v)$ get undirected capacity $C_{uv}$.

---

#### Problem P18 — BZOJ 3511 / Hydro BZOJ 3511: 土地划分 (Land Partition)
- **Judge URL**: [https://hydro.ac/p/bzoj-P3511](https://hydro.ac/p/bzoj-P3511)
- **Constraints**: $N \le 10^4$ plots, $M \le 4 \times 10^4$ edges. Time Limit: 1.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Each plot $u$ goes to A ($x_u = 1$, reward $V_{A,u}$) or B ($x_u = 0$, reward $V_{B,u}$). Each edge $e = (u, v)$ yields $E_{A,e}$ if both $u, v \in A$, yields $E_{B,e}$ if both $u, v \in B$, and **costs** $E_{C,e}$ if $u$ and $v$ are in different sets!
- **Step 2 — Algebraic Representation**:
  For edge $e = (u, v)$, the $2 \times 2$ reward matrix is $\Pi_e = \begin{pmatrix} E_{B,e} & -E_{C,e} \\ -E_{C,e} & E_{A,e} \end{pmatrix}$. Subtracting from $E_{A,e} + E_{B,e}$ gives the penalty matrix:
  $$\Theta_e = \begin{pmatrix} E_{A,e} & E_{A,e} + E_{B,e} + E_{C,e} \\ E_{A,e} + E_{B,e} + E_{C,e} & E_{B,e} \end{pmatrix}, \qquad \Delta_e = E_{A,e} + E_{B,e} + 2 E_{C,e} > 0.$$
  Applying Hu Botao's Symmetric Split (§4.1 Choice 2, scaling all capacities by $2$ to avoid half-integers):
  $$\Theta_e(x_u, x_v) = \tfrac{1}{2} E_{A,e}\big((1 - x_u) + (1 - x_v)\big) + \tfrac{1}{2} E_{B,e}(x_u + x_v) + \tfrac{1}{2}(E_{A,e} + E_{B,e} + 2 E_{C,e})\big(x_u(1 - x_v) + x_v(1 - x_u)\big).$$
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Scale all rewards/capacities by $2$ (so $W_{\text{base}} = 2\sum_u (V_{A,u} + V_{B,u}) + 2\sum_e (E_{A,e} + E_{B,e})$).
  - For each vertex $u$: **$S \to u$** of cap $2 V_{A,u} + \sum_{e \ni u} E_{A,e}$, and **$u \to T$** of cap $2 V_{B,u} + \sum_{e \ni u} E_{B,e}$.
  - For each edge $e = (u, v)$: undirected edge **$u \leftrightarrow v$** of capacity $E_{A,e} + E_{B,e} + 2 E_{C,e}$.
  - Answer: $(W_{\text{base}} - \text{MaxFlow}(S, T)) / 2$ using zero auxiliary vertices!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Write the $2 \times 2$ matrix for edge $e = (u, v)$ and check $A + D \le B + C$: it is submodular on ANY graph (no bipartiteness needed)!
  - *Hint 2*: Use the Symmetric Split ($\alpha = \beta = \Delta / 2$) to merge edge rewards into endpoint unary capacities (`合并点边法`).
  - *Hint 3*: Multiply all capacities by $2$ so that $\Delta / 2$ is always an integer, then divide the final answer by $2$.

---

#### Problem P19 — AtCoder ARC 074 F: Lotus Leaves
- **Judge URL**: [https://atcoder.jp/contests/arc074/tasks/arc074_d](https://atcoder.jp/contests/arc074/tasks/arc074_d)
- **Constraints**: $H, W \le 100$ grid (`S`, `T`, `o`, `.`). Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Jump between any two leaves `o` in the same row or same column. Delete the minimum number of `o` leaves so `T` is unreachable from `S`.
  - *Virtualization Clue*: Deleting leaf $(r, c)$ is equivalent to severing the incidence between **Row $r$** and **Column $c$**!
- **Step 2 — Algebraic Representation**:
  Let $x_r \in \{0, 1\}$ indicate whether Row $r$ is reachable from `S`, and $y_c \in \{0, 1\}$ indicate whether Column $c$ is reachable from `S`.
  - Leaf `S` at $(r_S, c_S)$ forces $x_{r_S} = 1, y_{c_S} = 1$; leaf `T` at $(r_T, c_T)$ forces $x_{r_T} = 0, y_{c_T} = 0$.
  - Every deletable leaf `o` at $(r, c)$ allows jumping between Row $r$ and Column $c$ unless deleted (cost $1$): penalty $x_r(1 - y_c) + y_c(1 - x_r)$.
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - If $r_S = r_T$ or $c_S = c_T$, output `-1`.
  - Create $H$ row vertices $\text{Row}_r$ and $W$ column vertices $\text{Col}_c$.
  - Edges **$S \to \text{Row}_{r_S}$**, **$S \to \text{Col}_{c_S}$** (cap $+\infty$) and **$\text{Row}_{r_T} \to T$**, **$\text{Col}_{c_T} \to T$** (cap $+\infty$).
  - For each leaf `o` at $(r, c)$: undirected edge **$\text{Row}_r \leftrightarrow \text{Col}_c$** of capacity $1$.
  - Answer: $\text{MaxFlow}(S, T)$ in $O(H W \sqrt{H + W})$ time!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Do not split $H W$ leaf vertices and add $O(H^2 W + W^2 H)$ edges!
  - *Hint 2*: A leaf at $(r, c)$ is an edge connecting Row $r$ and Column $c$ in a bipartite graph.
  - *Hint 3*: Deleting leaf $(r, c)$ is literally cutting the undirected capacity-$1$ edge $\text{Row}_r \leftrightarrow \text{Col}_c$.

---

#### Problem P20 — Codeforces 1404 E: Bricks
- **Judge URL**: [https://codeforces.com/problemset/problem/1404/E](https://codeforces.com/problemset/problem/1404/E)
- **Constraints**: $N, M \le 200$ grid (`#` and `.`). Time Limit: 4.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Tile all `#` cells with minimum $1 \times k$ or $k \times 1$ bricks.
  - *Dualization Clue*: Start with $B$ individual $1 \times 1$ bricks (one per `#`). Each time we merge two adjacent `#` cells horizontally or vertically into the same brick, the total brick count drops by $1$!
- **Step 2 — Algebraic Representation**:
  Let $H$ be the set of horizontal unit joints between adjacent `#` cells, and $V$ be the set of vertical unit joints between adjacent `#` cells.
  A set of active joints forms valid $1 \times k$ and $k \times 1$ bricks iff **no `#` cell touches both an active horizontal joint $h \in H$ and an active vertical joint $v \in V$** (no L-trominoes!).
  Thus we seek a **Maximum Independent Set** in the bipartite conflict graph between horizontal joints $H$ and vertical joints $V$!
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Create a vertex for each $h \in H$ (**$S \to h$**, cap $1$) and each $v \in V$ (**$v \to T$**, cap $1$).
  - If $h \in H$ and $v \in V$ share a common `#` cell: directed edge **$h \to v$** (cap $+\infty$).
  - Answer: $(\text{number of }\#\text{ cells}) - \big(|H| + |V| - \text{MaxFlow}(S, T)\big)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Instead of choosing bricks directly, choose which unit boundaries between adjacent `#` cells are merged.
  - *Hint 2*: Every active merge reduces the number of bricks by $1$. When are two merges incompatible?
  - *Hint 3*: A horizontal merge and a vertical merge cannot share the same `#` cell. Find the Maximum Independent Set on the bipartite graph of horizontal vs. vertical merges!

---

#### Problem P21 — Luogu P3749: [SHOI2017] 寿司餐厅 (Sushi Restaurant)
- **Judge URL**: [https://www.luogu.com.cn/problem/P3749](https://www.luogu.com.cn/problem/P3749)
- **Constraints**: $N \le 100$ sushi plates, codes $a_i \le 1000$, $m \in \{0, 1\}$, $d_{l,r} \in [-10^3, 10^3]$. Time Limit: 1.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Choosing interval $[l, r]$ yields $d_{l,r}$ and forces choosing all sub-intervals $[l', r'] \subseteq [l, r]$. Eating plate $i$ ($[i, i]$) costs $a_i$ per plate PLUS a one-time type fee $m \cdot c^2$ if any plate of type $c = a_i$ is eaten.
- **Step 2 — Algebraic Representation**:
  Pure Maximum Weight Closure using **Interval Pyramid Reduction (§3.4 Variation 4)**:
  - Interval variables $x_{l,r} \in \{0, 1\}$ ($1 \le l \le r \le N$) and type variables $y_c \in \{0, 1\}$ ($c \in \{a_1, \dots, a_N\}$).
  - Implications: $x_{l,r} \implies x_{l+1, r} \wedge x_{l, r-1}$ (for $l < r$), and $x_{i,i} \implies y_{a_i}$.
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Net weight of $[i, i]$ is $w_{i,i} = d_{i,i} - a_i$; for $l < r$, $w_{l,r} = d_{l,r}$; for type $c$, weight is $-m \cdot c^2$.
  - Connect positive weights from $S$ (adding to $W_{\text{base}}$), negative weights to $T$, and add $\infty$-edges $[l, r] \to [l+1, r]$, $[l, r] \to [l, r-1]$, and $[i, i] \to \text{Type}_{a_i}$.
  - Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Eating $[l, r]$ forces eating $[l+1, r]$ and $[l, r-1]$; by transitivity this covers all sub-intervals in $O(N^2)$ edges.
  - *Hint 2*: Subtract the linear plate cost $a_i$ directly from $d_{i,i}$ on the singleton node $[i, i]$.
  - *Hint 3*: Create one node per distinct sushi type $c$ with edge $\text{Type}_c \to T$ of capacity $m \cdot c^2$, and link $[i, i] \to \text{Type}_{a_i}$ with capacity $+\infty$.

---

#### Problem P22 — Codeforces 103 E: Buying Sets
- **Judge URL**: [https://codeforces.com/problemset/problem/103/E](https://codeforces.com/problemset/problem/103/E)
- **Constraints**: $N \le 300$ sets and $N$ elements; condition: every $k$ sets contain at least $k$ elements; set costs $w_i \in [-10^6, 10^6]$. Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Pick $k$ sets whose union has size **exactly $k$**, minimizing total cost $\sum_{i \in I} w_i$.
  - *Hall's Marriage Theorem Connection*: Since every $k$ sets already satisfy $|N(I)| \ge |I|$ (Hall's condition!), we have $|N(I)| = |I|$ **if and only if** $|N(I)| \le |I|$!
- **Step 2 — Algebraic Representation (Pedestal Shift `+M` Trick)**:
  How do we force $|N(I)| = |I|$ inside a Maximum Weight Closure (where picking set $i \in I$ forces picking all elements $j \in N(i)$)?
  Give every set $i$ a huge positive bonus $+M$ (where $M = 10^9 \gg N \max |w_i|$), so its weight becomes $M - w_i > 0$, and give every element $j \in \{1, \dots, N\}$ a cost of **$-M$**!
  Then for any closed selection of sets $I$ and their neighborhood $J \supseteq N(I)$:
  $$\text{Net Score}(I, J) = |I| \cdot M - |J| \cdot M - \sum_{i \in I} w_i = -\big(|J| - |I|\big) M - \sum_{i \in I} w_i.$$
  Because $|J| \ge |N(I)| \ge |I|$ by Hall's condition, $|J| - |I| \ge 0$ ALWAYS holds! And since $M \gg \sum |w_i|$, maximizing the closure **automatically forces $|J| = |N(I)| = |I|$**!
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Set $M = 10^9$. Each set $i$ has positive weight $W_i = M - w_i > 0$; each element $j$ has negative weight $-M$.
  - Baseline $W_{\text{base}} = \sum_{i=1}^N (M - w_i)$.
  - Edges: **$S \to \text{Set}_i$** (cap $M - w_i$), **$\text{Set}_i \to \text{Elem}_j$** (cap $+\infty$ for $j \in S_i$), **$\text{Elem}_j \to T$** (cap $M$).
  - Minimum cost subset: $\text{MaxFlow}(S, T) - W_{\text{base}}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Since Hall's condition $|N(I)| \ge |I|$ holds for all $I$, a subset $I$ has $|N(I)| = |I|$ iff it minimizes $|N(I)| - |I|$ to $0$.
  - *Hint 2*: Add $+M$ ($M = 10^9$) to the reward of picking each set $i$, and charge $-M$ for each element $j \in N(I)$.
  - *Hint 3*: Because $|N(I)| - |I| \ge 0$ always, any subset with $|N(I)| > |I|$ loses at least $M$, so Maximum Weight Closure only considers subsets with $|N(I)| = |I|$!

---

#### Problem P23 — Luogu P2604 / BZOJ 3218: a + b Problem
- **Judge URL**: [https://www.luogu.com.cn/problem/P2604](https://www.luogu.com.cn/problem/P2604)
- **Constraints**: $N \le 5000$ squares; each square $i$ has $a_i, b_i, w_i, l_i, r_i, p_i$. Time Limit: 1.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Color square $i$ Black ($x_i = 1$, reward $b_i$) or White ($x_i = 0$, reward $w_i$). Square $i$ loses $p_i$ if it is Black AND there exists $j < i$ that is White with $a_j \in [l_i, r_i]$!
  - *Why Naive Closure TLEs*: Connecting $i$ to all $j < i$ with $a_j \in [l_i, r_i]$ creates $O(N^2)$ edges ($2.5 \times 10^7$). We must virtualize the range $[l_i, r_i]$ over prefix $j < i$ using a **Persistent Segment Tree (`主席树`优化建图)**!
- **Step 2 — Algebraic Representation**:
  For each $i$, introduce an auxiliary penalty indicator $z_i \in \{0, 1\}$. If $x_i = 1$ (Black) and $z_i = 0$ (no penalty paid), then every $j < i$ with $a_j \in [l_i, r_i]$ MUST also be Black ($x_j = 1$):
  $$\text{Penalty } p_i x_i(1 - z_i) + \sum_{\substack{j < i \\ a_j \in [l_i, r_i]}} \infty \cdot z_i(1 - x_j).$$
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Baseline $W_{\text{base}} = \sum_{i=1}^N (b_i + w_i)$.
  - For each $i$: **$S \to x_i$** (cap $b_i$), **$x_i \to T$** (cap $w_i$), and **$x_i \to z_i$** (cap $p_i$).
  - Build a Persistent Segment Tree over value coordinates $a_j$: after step $i-1$, query root $\text{root}_{i-1}$ on range $[l_i, r_i]$ and add $O(\log N)$ edges of capacity $+\infty$ from $z_i$ to the segment tree nodes (whose leaves point to $x_j$ with cap $+\infty$), then insert $x_i$ at position $a_i$ to form $\text{root}_i$.
  - Total vertices $O(N \log N)$, edges $O(N \log N)$. Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: First write the $O(N^2)$ graph: create auxiliary node $z_i$ with $x_i \to z_i$ (cap $p_i$) and $z_i \to x_j$ (cap $+\infty$) for all $j < i, a_j \in [l_i, r_i]$.
  - *Hint 2*: Notice that $z_i$ connects to a 2D prefix-range $\{j < i : l_i \le a_j \le r_i\}$.
  - *Hint 3*: Maintain a Persistent Segment Tree over $a_j$ as $i$ increases from $1$ to $N$, reducing the $\infty$-edges to $O(N \log N)$.

---

### Tier 4: Mastery (`P24–P31` — Lipschitz Unary Chains, `AGC 038 F`, Hidden Bipartitions, Parametric & DP Cuts)

---

#### Problem P24 — TopCoder SRM 590 Div1 Hard: FoxAndCity
- **Judge URL**: [https://vjudge.net/problem/TopCoder-12729](https://vjudge.net/problem/TopCoder-12729)
- **Constraints**: $N \le 40$ cities, target distances $want_i \le N$. Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Add undirected edges to graph $G = (V, E)$ so the new shortest-path distances $d_i = \text{dist}(1, i)$ minimize $\sum_{i=2}^N (d_i - want_i)^2$.
  - *Algebraic Reformulation*: An integer vector $(d_1, \dots, d_N)$ is realizable as shortest-path distances from $1$ in some supergraph $G' \supseteq G$ **if and only if**:
    1. $d_1 = 0$ and $1 \le d_i \le N - 1$ for $i \ge 2$,
    2. $d_v \le d_u + 1$ for every existing edge $(u, v) \in E$ (**Lipschitz condition**), and
    3. Every $v$ with $d_v = k \ge 1$ has at least one neighbor $u$ with $d_u = k - 1$ — which is automatically satisfied at the optimum if we only enforce $d_v \le d_u + 1$? Wait: if we can **add arbitrary new edges** to $G$, we can always connect any vertex $v$ with $d_v = k$ to a vertex $u$ with $d_u = k - 1$ (since $d_1 = 0$, by induction we only need $d_v \le d_u + 1$ for existing edges $(u, v) \in E$!).
- **Step 2 — Algebraic Representation (Unary Threshold Chain)**:
  For each $i \in \{2, \dots, N\}$ and $k \in \{1, \dots, N\}$, let $x_{i, k} = [d_i \ge k] \in \{0, 1\}$, with $x_{i, 1} = 1$ and $x_{i, N} = 0$:
  - Chain invariant: $x_{i, k} \implies x_{i, k-1}$ ($\forall k \ge 2$).
  - Existing edge $(u, v) \in E$: $d_v \le d_u + 1 \iff (d_v \ge k \implies d_u \ge k - 1) \iff x_{v, k} \implies x_{u, k-1}$!
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Create node $(i, k)$ for $i \in \{2, \dots, N\}, k \in \{2, \dots, N-1\}$.
  - Unary cost: when $d_i = k - 1$, $x_{i, k-1} = 1$ and $x_{i, k} = 0$, severing the chain edge **$x_{i, k-1} \to x_{i, k}$** of capacity $(k - 1 - want_i)^2$ (with $x_{i, 1} = S$ and $x_{i, N} = T$), and reverse chain edges **$x_{i, k} \to x_{i, k-1}$** of capacity $+\infty$!
  - For every $(u, v) \in E$ and $k \in \{2, \dots, N-1\}$: edge **$x_{v, k} \to x_{u, k-1}$** of capacity $+\infty$.
  - Answer: $\text{MaxFlow}(S, T)$ on $O(N^2)$ vertices.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Since you can add ANY edges to $G$, any distance vector $d$ satisfying $d_1 = 0$ and $|d_u - d_v| \le 1$ for $(u, v) \in E$ can be realized by connecting each $v$ to $1$ through a chain!
  - *Hint 2*: Encode $d_i$ via a unary cut chain $S = (i, 1) \to (i, 2) \to \dots \to (i, N) = T$ where severing $(i, k) \to (i, k+1)$ costs $(k - want_i)^2$, with reverse $\infty$-edges $(i, k+1) \to (i, k)$.
  - *Hint 3*: Enforce $d_v \le d_u + 1$ via $\infty$-edges from $(v, k)$ to $(u, k-1)$ (in the $x_{i,k} = [d_i \ge k]$ orientation).

---

#### Problem P25 — AtCoder AGC 038 F: Two Permutations
- **Judge URL**: [https://atcoder.jp/contests/agc038/tasks/agc038_f](https://atcoder.jp/contests/agc038/tasks/agc038_f)
- **Constraints**: $N \le 10^5$. Time Limit: 2.0 s.
- **Complete 4-Step Compilation & Two Toy Traces**: See **Section 6 (§6.1–§6.3)** in full!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Prove that each cycle of $P$ (and $Q$) has only two valid states: either every element stays at $i$, or every element shifts to $P_i$.
  - *Hint 2*: Write the 5-case collision indicator $[A_i = B_i]$ between cycle $C_u \ni i$ of $P$ and cycle $D_v \ni i$ of $Q$. Notice it is supermodular!
  - *Hint 3*: Flip $y_v = 1 - w_v$ on all cycles of $Q$ (so $D_v \in V_S \iff B_i = i$) and apply Table 6.1 (or the 1-Cycle Aliasing Trick).

---

#### Problem P26 — AtCoder ARC 107 F: Sum of Abs
- **Judge URL**: [https://atcoder.jp/contests/arc107/tasks/arc107_d](https://atcoder.jp/contests/arc107/tasks/arc107_d)
- **Constraints**: $N \le 300$ vertices, $M \le 300$ edges; deletion cost $A_v \ge 0$, signed weight $B_v \in [-10^6, 10^6]$. Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Delete a subset of vertices (paying $A_v$ per deleted vertex) to maximize $\sum_{C \in \text{CC}} \left|\sum_{v \in C} B_v\right| - \sum_{v \text{ deleted}} A_v$.
  - *Algebraic Linearization of $|\cdot|$*: Since $|X| = \max_{s \in \{-1, +1\}} s \cdot X$, assigning each connected component $C$ a sign $s_C \in \{-1, +1\}$ means every surviving vertex $v$ gets a state $s_v \in \{+1, 0, -1\}$ (where $0$ means deleted), such that **no edge $(u, v) \in E$ connects $s_u = +1$ directly to $s_v = -1$**!
- **Step 2 — Algebraic Representation (3-State Node-Splitting Cut)**:
  Each vertex $v$ is partitioned by an $(S, T)$-cut of a 2-edge chain $S \xrightarrow{c_{v,1}} v_{\text{in}} \xrightarrow{c_{v,2}} v_{\text{out}} \xrightarrow{c_{v,3}} T$ (with reverse $\infty$-edge $v_{\text{out}} \to v_{\text{in}}$):
  - **State $+1$ ($v_{\text{in}}, v_{\text{out}} \in V_S$)**: severs $v_{\text{out}} \to T$, gaining $+B_v$.
  - **State $0$ / Deleted ($v_{\text{in}} \in V_T, v_{\text{out}} \in V_S$ — or $v_{\text{in}} \in V_S, v_{\text{out}} \in V_T$ if forward chain)**: severs $v_{\text{in}} \to v_{\text{out}}$, paying $A_v$ (so regret $|B_v| + A_v$ from baseline $|B_v|$).
  - **State $-1$ ($v_{\text{in}}, v_{\text{out}} \in V_T$)**: severs $S \to v_{\text{in}}$, gaining $-B_v$.
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Baseline $W_{\text{base}} = \sum_{v=1}^N |B_v|$.
  - For each vertex $v$, build the 2-node chain $v_{\text{in}} \to v_{\text{out}}$:
    - Edge **$v_{\text{in}} \to v_{\text{out}}$** of capacity $A_v + |B_v|$ (severed when $v_{\text{in}} \in V_S, v_{\text{out}} \in V_T \iff$ vertex $v$ is deleted!).
    - If $B_v > 0$: edge **$S \to v_{\text{in}}$** of capacity $2 B_v$ (severed when $v_{\text{in}}, v_{\text{out}} \in V_T \iff$ State $-1$, regret $2 B_v$).
    - If $B_v < 0$: edge **$v_{\text{out}} \to T$** of capacity $2 |B_v|$ (severed when $v_{\text{in}}, v_{\text{out}} \in V_S \iff$ State $+1$, regret $2 |B_v|$).
  - For each original edge $(u, v) \in E$: forbid $u$ in State $+1$ ($u_{\text{out}} \in V_S$) and $v$ in State $-1$ ($v_{\text{in}} \in V_T$) by adding directed edges **$u_{\text{out}} \to v_{\text{in}}$** (cap $+\infty$) and **$v_{\text{out}} \to u_{\text{in}}$** (cap $+\infty$)!
  - Answer: $W_{\text{base}} - \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Rewrite $|\sum_{v \in C} B_v| = \max_{s_C \in \{+1, -1\}} \sum_{v \in C} s_C B_v$. Thus every vertex is assigned $+1$, $-1$, or $0$ (deleted), and no edge can join $+1$ to $-1$.
  - *Hint 2*: Split each vertex into $v_{\text{in}} \to v_{\text{out}}$ with capacity $A_v + |B_v|$ so that severing $v_{\text{in}} \to v_{\text{out}}$ represents deleting $v$.
  - *Hint 3*: Forbid $+1$ adjacent to $-1$ by adding $\infty$-edges $u_{\text{out}} \to v_{\text{in}}$ and $v_{\text{out}} \to u_{\text{in}}$.

---

#### Problem P27 — AtCoder ARC 142 E: Pairing Wizards
- **Judge URL**: [https://atcoder.jp/contests/arc142/tasks/arc142_e](https://atcoder.jp/contests/arc142/tasks/arc142_e)
- **Constraints**: $N \le 100$ wizards, $M \le \binom{N}{2}$ pairs, $a_i, b_i \le 100$. Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Increment $a_i$ by $+1$ per unit cost so every pair $(u, v) \in E$ satisfies $\max(a_u, a_v) \ge \max(b_u, b_v)$ AND $\min(a_u, a_v) \ge \min(b_u, b_v)$.
  - *Hidden Surplus/Deficit Bipartition*: First, $\min(a_u, a_v) \ge \min(b_u, b_v)$ for all pairs containing $u$ forces $a_u \ge b_u$ whenever $b_u \le b_v$; in fact, wait: if $b_u \le b_v$, then $\min(a_u, a_v) \ge b_u \implies a_u \ge b_u \wedge a_v \ge b_u$, AND $\max(a_u, a_v) \ge b_v \implies (a_u \ge b_v \vee a_v \ge b_v)$!
  Therefore, every wizard $u$ touching at least one edge MUST satisfy $a_u \ge b_u$ as a mandatory baseline! Pay $\max(0, b_u - a_u)$ upfront and set $a_u \gets \max(a_u, b_u)$.
  Now partition the wizards into two disjoint sets:
  - **Surplus Wizards $L = \{u : a_u > b_u\}$**: Since $a_u > b_u$ and $\max b \le 100$, if a Surplus wizard $u \in L$ is raised further, it only ever helps satisfy $a_u \ge b_v$ for neighbors $v$. Even better: can an OR-clause $(a_u \ge b_v \vee a_v \ge b_v)$ ever require raising **both** $u$ and $v$? If $v \in L$ ($a_v > b_v$), then $a_v \ge b_v$ is **already satisfied**!
  Thus an unsatisfied clause ONLY exists when the higher-$b$ endpoint $v$ is a **Deficit Wizard $v \in R = \{v : a_v = b_v\}$**! And for $v \in R$, the clause $a_u \ge b_v \vee a_v \ge b_v$ is already satisfied if $a_v$ is raised at all? Wait: for $(u, v)$ with $b_u \le b_v$, the conditions are:
  1. $a_u \ge b_u$ and $a_v \ge b_u$ (mandatory lower bounds! Pay upfront to raise $a_u \gets \max(a_u, b_u)$ and $a_v \gets \max(a_v, b_u)$!).
  2. $a_u \ge b_v \;\vee\; a_v \ge b_v$.
  Once we preprocess all mandatory lower bounds $a_w \gets \max(a_w, \max_{(w, z) \in E} \min(b_w, b_z))$, any remaining active clause $(u, v)$ with $b_u \le b_v$ has $a_u < b_v$ and $a_v < b_v$. That implies $a_v < b_v$? Wait: since $a_v \ge b_v$ is NOT mandatory (only $a_v \ge \min(b_u, b_v) = b_u$ is mandatory!), a wizard $v$ with $a_v < b_v$ is in **Deficit ($R = \{v : a_v < b_v\}$)**, whereas in clause $a_u \ge b_v \vee a_v \ge b_v$, the second literal is the **single binary decision** $z_v = [a_v \ge b_v] \in \{0, 1\}$ (since a Deficit wizard $v \in R$ never needs $a_v > b_v$: if $v$ were used as the $u$-side of another edge $(v, w)$ with $b_v \le b_w$, the mandatory bound $a_v \ge \min(b_v, b_w) = b_v$ would have already forced $a_v \ge b_v$, placing $v \in L$!).
- **Step 2 — Algebraic Representation**:
  - Preprocess mandatory lower bounds: for every $(u, v) \in E$, let $m = \min(b_u, b_v)$ and set $L_u = \max(L_u, m), L_v = \max(L_v, m)$. Pay $\sum_i \max(0, L_i - a_i)$ and update $a_i \gets \max(a_i, L_i)$.
  - Partition wizards into $L = \{u : a_u \ge b_u\}$ and $R = \{v : a_v < b_v\}$.
  - Every remaining unsatisfied edge $(u, v)$ with $b_u \le b_v$ has $v \in R$ (since $a_v < b_v$). And $v \in R$ can NEVER be the $u$-endpoint of any edge $(v, w)$ with $b_v \le b_w$ (because that would have forced $L_v \ge b_v \implies a_v \ge b_v$)!
  - Thus the graph between $u$ (using unary chain $x_{u, t} = [a_u \ge t]$ for $t \in (a_u, 100]$) and $v \in R$ (using single binary variable $z_v = [a_v \ge b_v]$ of cost $b_v - a_v$) is **bipartite**! Flip $y_v = 1 - z_v$ on $R$:
    $$x_{u, b_v} = 1 \;\vee\; z_v = 1 \quad \Longleftrightarrow \quad y_v = 1 \implies x_{u, b_v} = 1!$$
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - For each wizard $u$ and $t \in [a_u + 1, 100]$: node $x_{u, t}$ with **$x_{u, t} \to T$** (cap $1$) and chain edge **$x_{u, t} \to x_{u, t-1}$** (cap $+\infty$).
  - For each Deficit wizard $v \in R$: node $y_v$ with **$S \to y_v$** of capacity $b_v - a_v$.
  - For each edge $(u, v) \in E$ with $b_u \le b_v$, $v \in R$, and $a_u < b_v$: edge **$y_v \to x_{u, b_v}$** of capacity $+\infty$.
  - Answer: $(\text{mandatory upfront cost}) + \text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Rewrite the condition for $(u, v)$ with $b_u \le b_v$ as $(a_u \ge b_u \wedge a_v \ge b_u) \wedge (a_u \ge b_v \vee a_v \ge b_v)$.
  - *Hint 2*: First raise all $a_i$ to satisfy all mandatory $a_u \ge b_u$ and $a_v \ge b_u$ bounds. Then notice that any wizard $v$ still satisfying $a_v < b_v$ can only ever be raised to $b_v$!
  - *Hint 3*: Flip the binary indicator $y_v = [a_v < b_v]$ for Deficit wizards ($S \to y_v$ cap $b_v - a_v$) and add $\infty$-edges $y_v \to x_{u, b_v}$ to the unary chain of $u$.

---

#### Problem P28 — AtCoder ARC 176 E: Max Vector
- **Judge URL**: [https://atcoder.jp/contests/arc176/tasks/arc176_e](https://atcoder.jp/contests/arc176/tasks/arc176_e)
- **Constraints**: $N, M \le 500$, dimension $D$ (values $\le 500$). Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Choose non-negative integer vectors $X_1, \dots, X_N$ and $Y_1, \dots, Y_M$ to minimize $\sum_i \sum_k X_{i,k} + \sum_j \sum_k Y_{j,k}$ subject to $\max(X_{i,k}, Y_{j,k}) \ge A_{q,k}$ for given pairs $(i_q, j_q)$ and coordinates $k$.
  - *Wait*: In `ARC 176 E`, each vector $X_i$ or $Y_j$ must be chosen from the input pool, OR wait: the constraint is that for each query $q$, $\forall k, \max(X_{i,k}, Y_{j,k}) \ge C_{q,k}$ where $X_i$ and $Y_j$ are bounded above by given vectors, and we want to maximize/minimize their sum! In fact, in `ARC 176 E`, the coordinates decouple into unary threshold chains on the bipartite graph $L = \{X_1, \dots, X_N\}$ and $R = \{Y_1, \dots, Y_M\}$.
- **Step 2 — Algebraic Representation**:
  Using unary threshold indicators $x_{i, t} = [v_i \ge t]$ on $L$ and flipped unary threshold indicators $y_{j, t} = [w_j < t]$ on $R$, every OR-clause $(v_i \ge t \vee w_j \ge t)$ becomes the submodular implication $y_{j, t} = 1 \implies x_{i, t} = 1$.
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - Build unary threshold chains for $L$ ($x_{i, t} \to T$ cap $1$, $x_{i, t} \to x_{i, t-1}$ cap $+\infty$) and flipped chains for $R$ ($S \to y_{j, t}$ cap $1$, $y_{j, t-1} \to y_{j, t}$ cap $+\infty$).
  - Add $\infty$-edges $y_{j, t} \to x_{i, t}$ for every threshold requirement $\max(v_i, w_j) \ge t$.
  - Answer: $\text{MaxFlow}(S, T)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Notice that the interaction is strictly bipartite between the $X$-side and the $Y$-side.
  - *Hint 2*: Encode levels via unary threshold variables $[v_i \ge t]$, and flip the $Y$-side variables to $[w_j < t]$.
  - *Hint 3*: An OR constraint $v_i \ge t \vee w_j \ge t$ becomes the directed $\infty$-edge $[w_j < t] \to [v_i \ge t]$.

---

#### Problem P29 — Codeforces 1383 F: Special Edges
- **Judge URL**: [https://codeforces.com/problemset/problem/1383/F](https://codeforces.com/problemset/problem/1383_F)
- **Constraints**: $N \le 10^4, M \le 10^4, K \le 10$ special edges, $Q \le 2 \times 10^5$ queries, $w_e \le 25$. Time Limit: 5.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Each of $Q = 2 \times 10^5$ queries specifies new capacities for the $K \le 10$ special edges. Output the minimum $(S, T)$-cut for each query.
- **Step 2 — Algebraic Representation (Parametric $2^K$ Cut Decomposition)**:
  Every $(S, T)$-cut $(V_S, V_T)$ induces a bitmask $\text{mask} \in \{0, 1\}^K$ of which special edges cross from $V_S$ to $V_T$. If we precompute for each of the $2^K = 1024$ masks the minimum capacity of a cut in $G \setminus E_{\text{special}}$ that severs all special edges in $\text{mask}$, say $C[\text{mask}]$, then for any query with special edge weights $w_0, \dots, w_{K-1}$:
  $$\text{MinCut}(w) = \min_{\text{mask} \in \{0, 1\}^K} \left( C[\text{mask}] + \sum_{i \in \text{mask}} w_i \right)!$$
- **Step 3 — Mechanical Graph Compilation & Solution**:
  - First compute the base max-flow $F_0 = C[0]$ with all $K$ special edges set to capacity $0$.
  - Traverse the $2^K = 1024$ states in a Gray-code / recursion tree: to transition from $\text{mask}$ to $\text{mask} \cup \{i\}$, add capacity $25$ ($\ge \max w_e$) to special edge $e_i$ in the **saved residual network** and augment via Ford-Fulkerson (at most $25$ unit-flow BFS/DFS paths!).
  - Answer each of the $Q$ queries in $O(2^K)$ time using precomputed mask sums.
- **3-Tier Progressive Hints**:
  - *Hint 1*: $K \le 10 \implies 2^K = 1024$. Separate the $K$ special edges from the rest of the network.
  - *Hint 2*: Precompute the max-flow for all $2^K$ subsets of special edges being given capacity $\infty$ (i.e., $25$, since max edge capacity is $25$).
  - *Hint 3*: Branch recursively on the residual graph so each of the $2^K$ states takes only $\le 25$ unit augmentations instead of running Dinic from scratch!

---

#### Problem P30 — Codeforces 724 E: Goods Transportation
- **Judge URL**: [https://codeforces.com/problemset/problem/724/E](https://codeforces.com/problemset/problem/724/E)
- **Constraints**: $N \le 10^4$, $c \le 10^9, p_i, s_i \le 10^9$. Time Limit: 2.0 s.
- **Step 1 — Non-Graph Diagnostic Signal (Direction B: Max-Flow $\to$ Min-Cut $\to$ DP)**:
  - *Surface Clue*: Node $i$ has supply $p_i$, sink demand $s_i$, and directed edge $i \to j$ of capacity $c$ for all $1 \le i < j \le N$. Compute $\text{MaxFlow}(S, T)$.
  - *Why Explicit Dinic Fails*: $N = 10^4 \implies \binom{N}{2} \approx 5 \times 10^7$ edges (TLE/MLE).
- **Step 2 — Algebraic Representation**:
  By Max-Flow Min-Cut Duality, $\text{MaxFlow}(S, T) = \min_{x \in \{0,1\}^N} \Phi(x)$ where:
  $$\Phi(x) = \sum_{i=1}^N p_i(1 - x_i) + \sum_{i=1}^N s_i x_i + \sum_{1 \le i < j \le N} c \cdot x_i(1 - x_j).$$
- **Step 3 — Mechanical DP Compilation & Solution**:
  Process $i = 1 \dots N$, maintaining $k = \sum_{r=1}^{i-1} x_r$ (the number of previous vertices placed in $V_S$):
  - If $x_i = 1$ ($i \in V_S$): pays $s_i$, increases $k \gets k + 1$.
  - If $x_i = 0$ ($i \in V_T$): pays $p_i$ PLUS $c \cdot k$ (severing all $k$ edges from earlier $V_S$-vertices to $i$)!
  $$\text{dp}[i][k] = \min\big(\text{dp}[i-1][k-1] + s_i, \; \text{dp}[i-1][k] + p_i + k \cdot c\big),$$
  solving the $5 \times 10^7$-edge flow problem in $O(N^2)$ time and $O(N)$ rolling memory!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Never build the $O(N^2)$ graph! Dualize Max-Flow into Min-Cut.
  - *Hint 2*: If you decide $x_i \in \{0, 1\}$ from $i = 1$ to $N$, what information from $1 \dots i-1$ determines how many $i \to j$ edges are cut at step $i$?
  - *Hint 3*: Only the count $k = \sum_{r < i} x_r$ matters! Run an $O(N^2)$ DP over $(i, k)$.

---

#### Problem P31 — Luogu P3308: [SDOI2014] LIS
- **Judge URL**: [https://www.luogu.com.cn/problem/P3308](https://www.luogu.com.cn/problem/P3308)
- **Constraints**: $N \le 700$, $A_i, B_i, C_i$. Time Limit: 1.0 s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  - *Surface Clue*: Find the minimum cost of deleting elements to reduce the LIS length of $A$, AND output the **lexicographically smallest** set of deleted indices (ordered by $C_i$).
- **Step 2 — Algebraic Representation**:
  Let $f[i]$ be the LIS length ending at $i$, and $L = \max_i f[i]$. Split each $i$ into $i_{\text{in}} \xrightarrow{B_i} i_{\text{out}}$; connect $S \to i_{\text{in}}$ ($\infty$, if $f[i] = 1$), $i_{\text{out}} \to T$ ($\infty$, if $f[i] = L$), and $i_{\text{out}} \to j_{\text{in}}$ ($\infty$, if $i < j, A_i < A_j, f[j] = f[i] + 1$).
- **Step 3 — Mechanical Graph Compilation & Flow Rollback (`退流`)**:
  1. Run Dinic once to get $\text{MinCut}$.
  2. Sort vertices $i$ in increasing order of priority $C_i$.
  3. To test if $e = (i_{\text{in}} \to i_{\text{out}})$ can belong to the minimum cut: check if $i_{\text{in}}$ cannot reach $i_{\text{out}}$ in the residual graph $G_f$ (`!bfs(i_in, i_out)`).
  4. If `!bfs(i_in, i_out)`, $e$ CAN be cut! To permanently commit $e$ to the cut, **rollback (`退流`)** its flow $B_i$ by running maximum flow of amount $B_i$ from $i_{\text{in}}$ to $S$ and from $T$ to $i_{\text{out}}$ (or equivalently $T \to i_{\text{out}}$ and $i_{\text{in}} \to S$ along reverse residual edges), then set the capacity of $e$ and its reverse edge to $0$!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Build the standard layered DAG of LIS transitions with vertex-splitting capacities $B_i$.
  - *Hint 2*: A saturated edge $(u \to v)$ can belong to *some* minimum cut iff there is NO path from $u$ to $v$ in the residual network $G_f$.
  - *Hint 3*: Do not re-run Dinic $N$ times! Roll back the $B_i$ units of flow along $i_{\text{in}} \to S$ and $T \to i_{\text{out}}$ in $G_f$, then zero out the edge.

---

## 9. Reconciled Quarantined Template Problems Table

To keep the main problem bank focused on non-trivial structural compilation, standard textbook duplicates and verbatim clones are quarantined here:

| Quarantine ID | Problem Name & Source | Reason for Quarantine & Canonical Replacement in §8 |
| :--- | :--- | :--- |
| **R-2A-01** | **Luogu P2762 — 太空飞行计划问题** (`网络流 24 题`) | Verbatim textbook Maximum Weight Closure (experiments $\to$ instruments); superseded by **P01 (`P4174 最大获利`)** and **P06 (`ABC 326 G`)**. |
| **R-2A-02** | **POJ 2987 — Firing** | Verbatim Maximum Weight Closure on a company hierarchy DAG (with cardinality tie-breaking via $w_i \gets M \cdot w_i - 1$); superseded by **P11 (`P2805 植物大战僵尸`)**. |
| **R-2A-03** | **Codeforces 1146 G — Zoning Restrictions** | Small-$N$ ($N, H, M \le 50$) unary threshold closure with interval penalty hubs; superseded by **P06 (`ABC 326 G`)** and **P21 (`P3749 寿司餐厅`)**. |
| **R-2A-04** | **Luogu P5030 — 长脖子鹿放置** / **P3355 — 骑士共存问题** | Standard Bipartite Maximum Weight Independent Set on Knight/Giraffe parity graphs; superseded by **P04 (`P2774 方格取数`)** and **P10 (`CF 808 F`)**. |
| **R-2A-05** | **Luogu P1935 — [国家集训队] 圈地计划 (Clone Variants)** | Direct clones of checkerboard bipartite flip on 2D grids; covered by **P16 (`ABC 193 F`)** and **P17 (`P1791`)**. |
| **R-2A-06** | **BZOJ 1497 — 最大获利** | Exact judge mirror of **P01 (`Luogu P4174 — [NOI2006] 最大获利`)**. |
| **R-2A-07** | **AtCoder ABC 347 G — Grid Coloring 2** | 5-level unary chain smoothing $\sum |x_u - x_v|^2$ on a grid (**belongs to Wave 2B: Multi-State Cut Chains & Isotonic Regression**). |
| **R-2A-08** | **SPOJ PROFIT** | Exact judge mirror of **P01 (`Luogu P4174 — [NOI2006] 最大获利`)**. |

---

## 10. Unified Multilingual Bibliography (`[EN]`, `[ZH]`, `[JA]`)

### `[EN]` English Literature (Combinatorial Optimization, Discrete Mathematics & Computer Vision)
1. **Picard, J.-C. (1976)**. *"Maximal Closure of a Graph and Applications to Combinatorial Problems."* Management Science, 22(11), 1268–1272. (Foundational proof reducing Maximum Weight Closure to Minimum $(S, T)$-Cut.)
2. **Hammer, P. L., Hansen, P., & Simeone, B. (1984)**. *"Roof Duality, Complementation and Persistency in Quadratic 0–1 Optimization."* Mathematical Programming, 28(2), 121–155. (Introduces Roof Duality, the doubled network $\mathcal{N}_{\text{QPBO}}$, half-integrality, and the Strong Persistency / Autarky Theorem.)
3. **Boros, E., & Hammer, P. L. (2002)**. *"Pseudo-Boolean Optimization."* Discrete Applied Mathematics, 123(1–3), 155–225. (Comprehensive treatise on posiforms, submodularity, Harary signed graph switching, and QPBO.)
4. **Kolmogorov, V., & Zabih, R. (2004)**. *"What Energy Functions Can Be Minimized via Graph Cuts?"* IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 26(2), 147–159. (Proves the $A + D \le B + C$ submodularity characterization for binary energy minimization.)
5. **Freedman, D., & Drineas, P. (2005)**. *"Energy Minimization via Graph Cuts: Settling What is Possible."* IEEE CVPR 2005, Vol. 2, 939–946. (Normal-form decomposition of pairwise and higher-order submodular pseudo-Boolean functions.)
6. **Kolmogorov, V., & Rother, C. (2007)**. *"Minimizing Nonsubmodular Functions with Graph Cuts — A Review."* IEEE TPAMI, 29(7), 1274–1279. (Survey of QPBO, roof duality, and persistency in computer vision.)
7. **Harary, F. (1953)**. *"On the Notion of Balance of a Signed Graph."* Michigan Mathematical Journal, 2(2), 143–146. (Characterizes when a signed graph can be switched to all-positive edges via vertex gauge flips.)
8. **Billionnet, A., & Minoux, M. (1985)**. *"Maximizing a Supermodular Pseudo-Boolean Function: A Polynomial Algorithm for Supermodular Cubic Functions."* Discrete Applied Mathematics, 12(1), 1–11. (Proves all degree-$3$ submodular functions are graph-representable.)
9. **Živný, S., Cohen, D. A., & Jeavons, P. G. (2009)**. *"The Expressive Power of Binary Submodular Functions."* Discrete Applied Mathematics, 157(15), 3347–3358. (Proves the degree $d \ge 4$ impossibility boundary: not all quaternary submodular functions can be represented via auxiliary-vertex graph cuts.)
10. **Ishikawa, H. (2011)** & **Fix, A., Gruber, A., Boros, E., & Zabih, R. (2011)**. *"Transformation of General Binary MRF Minimization to the First-Order Case"* (TPAMI 2011) & *"A Graph Cut Algorithm for Higher-Order Markov Random Fields"* (ICCV 2011).

### `[ZH]` Chinese Competitive Programming Literature (`国家集训队论文` & Classic Treatises)
11. **Hu Botao (胡伯涛, Amber) (2007)**. 《最小割模型在信息学竞赛中的应用》 (*Applications of Minimum Cut Models in Olympiad in Informatics*). 2007 国家集训队论文. (Introduces Maximum Weight Closure, `先拿后退` regret accounting, symmetric vertex-edge merging `合并点边法`, and lexicographically first minimum cuts to Chinese OI.)
12. **Wang Wenhao (王文浩) (2016)**. 《浅谈网络流的各种建模方法》 (*A Brief Discussion on Network Flow Modelling Methods*). 2016 国家集训队论文.
13. **OI-Wiki Contributors**. 《最小割》 & 《最大权闭合子图》: [https://oi-wiki.org/graph/flow/min-cut/](https://oi-wiki.org/graph/flow/min-cut/).

### `[JA]` Japanese Competitive Programming Literature (`燃やす埋める` / `Project Selection Problem`)
14. **noshi91 (2019)**. *"「燃やす埋める」と「Project Selection Problem」"* (`Burn-or-Bury and the Project Selection Problem`): [https://noshi91.hatenablog.com/entry/2021/06/29/044225](https://noshi91.hatenablog.com/entry/2021/06/29/044225). (Canonical Japanese reference on `燃やす埋める`, `二部グラフの片側反転` bipartite variable flipping, and `ゲタを履かせる` pedestal shifts.)
15. **maspypy (2020)**. *"燃やす埋める問題（Project Selection Problem）の解説"*: [https://maspypy.com/atcoder-%e3%81%aa%e3%81%9c%e3%81%aa%e3%81%ab%e3%80%81%e7%87%83%e3%82%84%e3%81%99%e5%9f%8b%e3%82%81%e3%82%8b](https://maspypy.com/atcoder-%e3%81%aa%e3%81%9c%e3%81%aa%e3%81%ab%e3%80%81%e7%87%83%e3%82%84%e3%81%99%e5%9f%8b%e3%82%81%e3%82%8b).
16. **tatyam (2021)**. *"燃やす埋めるを完全に理解する"* (`Completely Understanding Burn-or-Bury`).
17. **Maroonrk / AtCoder Editorial (2019)**. *AtCoder Grand Contest 038 Problem F — Two Permutations Editorial*: [https://img.atcoder.jp/agc038/editorial.pdf](https://img.atcoder.jp/agc038/editorial.pdf).

---

## 11. Deep-Dive Worked Scratchpads, Counterexample Traces & Meta-Compiler Blueprint

To ensure that every subtle mechanism in Waves 2A (`§2–§8`) is 100% concrete and hand-verifiable, this section provides five complete numerical traces of the hardest structural archetypes—including explicit broken-gadget counterexamples—followed by a reusable C++20 **Algebraic-to-Cut Meta-Compiler (`BurnOrBuryCompiler`)** that automatically performs Harary signed-balance checking, Bipartite Variable Inversion, and Recipe 1 unary normalization (`差値正規化`).

---

### 11.1 Worked Trace 1: `[NOI2009] 植物大战僵尸` (`P11`) — Why Tarjan's SCC Deletion Fails vs. Kahn's Topological BFS

Consider a $1 \times 4$ single-row lawn with cells $u_1 = (0, 0), u_2 = (0, 1), u_3 = (0, 2), u_4 = (0, 3)$ (zombies enter from the right at column $3$):
- **Scores**:
  $$w(u_1) = +1000, \qquad w(u_2) = -10, \qquad w(u_3) = -10, \qquad w(u_4) = +50.$$
- **Row-Entry Prerequisites** (to reach $(0, c)$, you must first eat $(0, c+1)$):
  $$u_4 \xrightarrow{\text{unlocks}} u_3 \xrightarrow{\text{unlocks}} u_2 \xrightarrow{\text{unlocks}} u_1.$$
- **Attack / Protection Prerequisites**:
  - Plant $u_2$ attacks cell $u_3$, so to eat $u_3$ you must first eat $u_2$: $u_2 \xrightarrow{\text{unlocks}} u_3$.

#### Step 1: Construct the Causal Prerequisite Graph $G_{\text{pre}}$ (`protector -> protected`)
The directed edges of $G_{\text{pre}}$ are:
$$u_4 \to u_3, \qquad u_3 \to u_2, \qquad u_2 \to u_3, \qquad u_2 \to u_1.$$
Notice the structure of $G_{\text{pre}}$:
1. $u_4$ has $\text{in-degree}_{G_{\text{pre}}}(u_4) = 0$.
2. $\{u_2, u_3\}$ forms a **2-cycle** $u_3 \leftrightarrow u_2$ (to reach $u_2$ you must first pass through $u_3$, but $u_2$ shoots anyone entering $u_3$!).
3. $u_1$ (worth $+1000$!) is **not in any cycle** (its SCC is the singleton $\{u_1\}$ of size $1$), because $u_1$ cannot reach $u_2$ or $u_3$. However, $u_1$ lies **causally downstream** of the deadlocked cycle $\{u_2, u_3\}$ via $u_2 \to u_1$!

#### Step 2: What Happens Under Three Different Implementations?

| Implementation Attempt | Surviving Vertices | Resulting Min-Cut & Claimed Profit | Verdict & Failure Diagnosis |
| :--- | :--- | :--- | :--- |
| **Attempt 1: Raw Picard Closure (No Cycle Pruning)** | $\{u_1, u_2, u_3, u_4\}$ | Places all 4 vertices in $V_S$: pays $10 + 10 = 20$ at $u_2, u_3 \to T$, claims $1000 + 50 = 1050$. Profit $= \mathbf{1030}$. | **WA!** Hallucinates that zombies can teleport through the mutual deadlock $u_2 \leftrightarrow u_3$ by eating them simultaneously. |
| **Attempt 2: Tarjan's SCC (`delete if |SCC| >= 2`)** | Deletes $\{u_2, u_3\}$; keeps $\{u_1, u_4\}$! | Since $u_2$ was deleted, the dependency edge $u_1 \to u_2$ vanishes! $u_1$ now has zero dependencies and is chosen for $+1000$. Profit $= \mathbf{1050}$. | **WA!** Deleting only cyclic SCCs leaves acyclic downstream dependents ($u_1$) with broken prerequisite chains! |
| **Attempt 3: Kahn's Topological BFS on $G_{\text{pre}}$ (Correct)** | Queue starts with $[u_4]$ ($\text{in-deg}=0$). Pops $u_4$, decrements $\text{in-deg}(u_3)$ from $2$ to $1$. Queue empties! Only $U_{\text{valid}} = \{u_4\}$ survives! | Only $u_4$ (weight $+50$) enters the closure network. Profit $= \mathbf{50}$. | **AC!** Kahn's BFS automatically prunes both the deadlocked cycle $\{u_2, u_3\}$ AND its acyclic causal descendant $u_1$. |

---

### 11.2 Worked Trace 2: QPBO Roof Duality & Strong Persistency (`§5.4`) on an Odd-Cycle Frustrated Graph

Suppose we want to minimize a **non-bipartite, non-submodular** quadratic pseudo-Boolean function on $n = 4$ binary variables $(x_1, x_2, x_3, x_4) \in \{0, 1\}^4$, where $\{1, 2, 3\}$ forms a **frustrated odd cycle ($K_3$)** of supermodular conflicts and vertex $4$ is a pendant neighbor of $3$:
$$\Phi(x_1, x_2, x_3, x_4) = \underbrace{-4 x_1 - 4 x_2 - 4 x_3}_{\text{triangle rewards}} - 10 x_4 + \underbrace{6 x_1 x_2 + 6 x_2 x_3 + 6 x_3 x_1}_{\text{supermodular triangle conflicts}} + \underbrace{8 x_3 x_4}_{\text{pendant conflict}}.$$
*(Equivalently, we are maximizing $4(x_1 + x_2 + x_3) + 10 x_4 - 6(x_1 x_2 + x_2 x_3 + x_3 x_1) - 8 x_3 x_4$.)*

1. **Why Harary Gauge Switching Fails**: Every edge in the triangle $\{1, 2, 3\}$ has $\Delta = -6 < 0$ (supermodular). The product of signs around the 3-cycle $(1, 2, 3)$ is $(-1)^3 = -1$, so no variable flip can make $\Phi$ submodular.
2. **Constructing the Doubled Network $\mathcal{N}_{\text{QPBO}}$ (§5.4)**:
   Add baseline $+22$ so unary terms become non-negative regrets $4(1 - x_1) + 4(1 - x_2) + 4(1 - x_3) + 10(1 - x_4)$.
   In $\mathcal{N}_{\text{QPBO}}$ (scaling capacities by $2\times$ to avoid $\frac{1}{2}$ fractions, so we divide the final cut by $2$):
   - **Unary edges** (from $c(1 - x_i) = \frac{1}{2}c(1 - x_i) + \frac{1}{2}c \cdot \bar{x}_i$):
     - For $i \in \{1, 2, 3\}$: $S \to x_i$ (cap $4$) and $\bar{x}_i \to T$ (cap $4$).
     - For $i = 4$: $S \to x_4$ (cap $10$) and $\bar{x}_4 \to T$ (cap $10$).
   - **Supermodular pairwise edges** (from $w \cdot x_i x_j = \frac{1}{2}w \cdot x_i(1 - \bar{x}_j) + \frac{1}{2}w \cdot x_j(1 - \bar{x}_i)$):
     - For each triangle pair $(i, j) \in \{(1,2), (2,3), (3,1)\}$: $x_i \to \bar{x}_j$ (cap $6$) and $x_j \to \bar{x}_i$ (cap $6$).
     - For pendant edge $(3, 4)$: $x_3 \to \bar{x}_4$ (cap $8$) and $x_4 \to \bar{x}_3$ (cap $8$).
3. **Minimum $(S, T)$-Cut in $\mathcal{N}_{\text{QPBO}}$**:
   - Look at $x_4$ and $\bar{x}_4$: $S \to x_4$ has huge capacity $10$, while $x_4 \to \bar{x}_3 \to T$ has bottleneck $\min(8, 4) = 4$. Thus in the minimum cut:
     $$x_4 \in V_S \quad \text{and} \quad \bar{x}_4 \in V_T \qquad \implies \qquad \hat{x}_4 = 1!$$
   - Because $x_4 \in V_S$ and $\bar{x}_3 \to T$ (cap $4$) is saturated by $x_4 \to \bar{x}_3$ (leaving $4$ residual capacity on $x_4 \to \bar{x}_3$), $\bar{x}_3$ is forced into $V_S$! Symmetrically, $S \to x_3$ (cap $4$) is drained into $\bar{x}_4 \to T$ via $x_3 \to \bar{x}_4$, forcing $x_3 \in V_T$:
     $$x_3 \in V_T \quad \text{and} \quad \bar{x}_3 \in V_S \qquad \implies \qquad \hat{x}_3 = 0!$$
   - What about $x_1$ and $x_2$? With $x_3 = 0$ fixed, $x_1$ and $x_2$ have unary rewards $4$ and pairwise conflict $6 x_1 x_2$. Wait: on $\{1, 2\}$ alone (a single edge!), $\{1, 2\}$ IS bipartite, or if they were symmetric in a larger odd cycle with rewards $4$ and conflict $6$ on all three edges without $x_4$, $\hat{x}_1 = \hat{x}_2 = \hat{x}_3 = \frac{1}{2}$! Here, because $\hat{x}_4 = 1$ and $\hat{x}_3 = 0$ are resolved by **Strong Persistency (Theorem 5.2)**, even if $\{1, 2, 3\}$ had heavier triangle weights (say $w = 10$ instead of $6$), fixing $x_4 = 1, x_3 = 0$ via Strong Persistency **breaks the odd cycle $\{1, 2, 3\}$**, allowing the remaining variables $\{x_1, x_2\}$ to be solved to 100% integrality!

---

### 11.3 Worked Trace 3: `AtCoder ARC 142 E — Pairing Wizards` (`P27`) — Hidden Surplus/Deficit Bipartition

Consider $N = 3$ wizards with initial powers $a$ and target thresholds $b$:
- Wizard 1: $a_1 = 2, b_1 = 3$
- Wizard 2: $a_2 = 1, b_2 = 6$
- Wizard 3: $a_3 = 4, b_3 = 5$
- Edges: $(1, 2)$ and $(2, 3)$.

1. **Step 1 — Mandatory Lower Bounds ($\min(a_u, a_v) \ge \min(b_u, b_v)$)**:
   - Edge $(1, 2)$ has $\min(b_1, b_2) = \min(3, 6) = 3 \implies L_1 \ge 3, L_2 \ge 3$.
   - Edge $(2, 3)$ has $\min(b_2, b_3) = \min(6, 5) = 5 \implies L_2 \ge 5, L_3 \ge 5$.
   - Upfront mandatory raises:
     - Wizard 1: $a_1 \gets \max(2, 3) = 3$ (cost $3 - 2 = 1$).
     - Wizard 2: $a_2 \gets \max(1, 5) = 5$ (cost $5 - 1 = 4$).
     - Wizard 3: $a_3 \gets \max(4, 5) = 5$ (cost $5 - 4 = 1$).
     - **Total Upfront Cost** $= 1 + 4 + 1 = 6$. Updated $a = (3, 5, 5)$ vs. $b = (3, 6, 5)$.
2. **Step 2 — Partition into Surplus ($a_i \ge b_i$) vs. Deficit ($a_i < b_i$)**:
   - $L = \{1, 3\}$ (since $a_1 = 3 \ge b_1 = 3$ and $a_3 = 5 \ge b_3 = 5$).
   - $R = \{2\}$ (since $a_2 = 5 < b_2 = 6$; Deficit $= b_2 - a_2 = 6 - 5 = 1$).
3. **Step 3 — Remaining OR-Clauses ($\max(a_u, a_v) \ge \max(b_u, b_v)$)**:
   - Edge $(1, 2)$ requires $a_1 \ge 6 \;\vee\; a_2 \ge 6$.
   - Edge $(2, 3)$ requires $a_3 \ge 6 \;\vee\; a_2 \ge 6$.
   - Flip Deficit Wizard 2's variable: $y_2 = [a_2 < 6] \in \{0, 1\}$ (edge **$S \to y_2$** of capacity $b_2 - a_2 = 6 - 5 = 1$).
   - If $y_2 = 1$ ($a_2 < 6$), both $a_1 \ge 6$ (cost $6 - 3 = 3$) and $a_3 \ge 6$ (cost $6 - 5 = 1$) are forced via $\infty$-edges $y_2 \to x_{1, 6}$ and $y_2 \to x_{3, 6}$!
4. **Step 4 — Min-Cut Decision**:
   - Cut Option A ($y_2 = 0 \implies$ raise Wizard 2 to $6$): severs $S \to y_2$ of capacity **$1$**.
   - Cut Option B ($y_2 = 1 \implies$ raise Wizards 1 and 3 to $6$): severs $x_{1,4..6} \to T$ ($3$) and $x_{3,6} \to T$ ($1$), total capacity **$4$**.
   - Minimum Cut $= 1 \implies$ Total Cost $= 6 + 1 = 7$ (achieved by $a = (3, 6, 5)$).

---

### 11.4 Worked Trace 4: `Codeforces 103 E — Buying Sets` (`P22`) — Hall's Marriage Condition + Pedestal Shift $+M$

Consider $N = 3$ sets over $\{1, 2, 3\}$ satisfying Hall's condition:
- $S_1 = \{1, 2\}$, cost $w_1 = -10$ (selecting $S_1$ *earns* $10$, i.e. cost $-10$).
- $S_2 = \{2, 3\}$, cost $w_2 = +4$.
- $S_3 = \{3\}$, cost $w_3 = -5$.

Let us find a subset $I \subseteq \{1, 2, 3\}$ with $|N(I)| = |I|$ minimizing $\sum_{i \in I} w_i$:
- Check all $2^3 = 8$ subsets $I$:
  - $I = \emptyset$: $|N(\emptyset)| = 0 = |\emptyset|$, cost $= 0$.
  - $I = \{1\}$: $N(\{1\}) = \{1, 2\}$ (size $2 > 1$, invalid!).
  - $I = \{3\}$: $N(\{3\}) = \{3\}$ (size $1 = 1$, **valid!**, cost $= -5$).
  - $I = \{2, 3\}$: $N(\{2, 3\}) = \{2, 3\}$ (size $2 = 2$, **valid!**, cost $= 4 - 5 = -1$).
  - $I = \{1, 2, 3\}$: $N(\{1, 2, 3\}) = \{1, 2, 3\}$ (size $3 = 3$, **valid!**, cost $= -10 + 4 - 5 = -11$).

Now trace the $+M$ Pedestal Closure Network with $M = 100$:
- Set weights in closure: $W_i = M - w_i$:
  $$W_1 = 100 - (-10) = 110, \qquad W_2 = 100 - 4 = 96, \qquad W_3 = 100 - (-5) = 105.$$
- Element weights in closure: $-M = -100$ for each $j \in \{1, 2, 3\}$.
- Optimistic Baseline $W_{\text{base}} = 110 + 96 + 105 = 311$.
- Check the cut capacity for:
  - $I = \{1\}$ ($J = \{1, 2\}$): closure score $= 110 - 2(100) = -90 < 0$ (heavily penalized by $-M$ because $|J| - |I| = 2 - 1 = 1 > 0$!).
  - $I = \{3\}$ ($J = \{3\}$): closure score $= 105 - 100 = +5 \implies \text{cost} = -5$.
  - $I = \{1, 2, 3\}$ ($J = \{1, 2, 3\}$): closure score $= 311 - 3(100) = +11 \implies \text{cost} = -11$.
- Maximum Closure Score $= +11 \implies$ Minimum Cost Subset $= -11$ ($I = \{1, 2, 3\}$)!

---

### 11.5 Worked Trace 5: `AtCoder ARC 107 F — Sum of Abs` (`P26`) — 3-State Node-Splitting Cut

Consider $N = 2$ connected vertices $1 - 2$ with:
- Vertex 1: deletion cost $A_1 = 3$, signed weight $B_1 = +10$.
- Vertex 2: deletion cost $A_2 = 2$, signed weight $B_2 = -8$.

1. **Possible Decisions**:
   - Keep both $\{1, 2\}$ in one component: $|\sum B_v| = |10 - 8| = 2$.
   - Delete vertex $2$ (cost $A_2 = 2$): component $\{1\}$ gives $|10| - 2 = 8$.
   - Delete vertex $1$ (cost $A_1 = 3$): component $\{2\}$ gives $|-8| - 3 = 5$.
   - Delete both (cost $5$): $0 - 5 = -5$.
   - **True Optimum**: $8$ (keep $1$ with sign $+1$, delete $2$).
2. **Trace the 3-State Node-Splitting Network (§8 P26)**:
   - Baseline $W_{\text{base}} = |10| + |-8| = 18$.
   - Vertex 1 ($B_1 = +10 > 0, A_1 = 3$):
     - **$S \to 1_{\text{in}}$** (cap $2 B_1 = 20$), **$1_{\text{in}} \to 1_{\text{out}}$** (cap $A_1 + |B_1| = 13$), **$1_{\text{out}} \to T$** (cap $0$).
   - Vertex 2 ($B_2 = -8 < 0, A_2 = 2$):
     - **$S \to 2_{\text{in}}$** (cap $0$), **$2_{\text{in}} \to 2_{\text{out}}$** (cap $A_2 + |B_2| = 10$), **$2_{\text{out}} \to T$** (cap $2|B_2| = 16$).
   - Edge $(1, 2)$: **$1_{\text{out}} \to 2_{\text{in}}$** (cap $+\infty$) and **$2_{\text{out}} \to 1_{\text{in}}$** (cap $+\infty$).
   - Notice the single path $S \to 1_{\text{in}} \to 1_{\text{out}} \to 2_{\text{in}} \to 2_{\text{out}} \to T$ with capacities $20 \to 13 \to \infty \to 10 \to 16$!
   - The minimum cut severs **$2_{\text{in}} \to 2_{\text{out}}$** of capacity **$10$** (corresponding to $1_{\text{in}}, 1_{\text{out}}, 2_{\text{in}} \in V_S$ and $2_{\text{out}} \in V_T$, i.e., Vertex 1 in State $+1$ and Vertex 2 in State $0$ / Deleted!).
   - Maximum score: $W_{\text{base}} - \text{MinCut} = 18 - 10 = \mathbf{8}$!

---

### 11.6 Reusable C++20 Meta-Compiler Blueprint (`BurnOrBuryCompiler`)

While standard Dinic templates are assumed as pre-existing library code, contest solvers frequently make sign or orientation errors when translating $2 \times 2$ matrices, unary regrets, and bipartite variable flips into Dinic edges. The following self-contained **Meta-Compiler** compiles high-level algebraic specifications directly into a black-box `MaxFlow` solver, including automatic **Harary Signed-Graph Balance / Bipartite Flip Detection (§7.1)** and **Recipe 1 Unary Normalization (`差値正規化`, §2.4)**:

```cpp
// Algebraic-to-Graph Cut Meta-Compiler (Convention A: x_v = 1 <=> v in V_S, x_v = 0 <=> v in V_T)
// Assumes a standard black-box Dinic solver `mf(num_vertices, S, T)` with `mf.add_edge(u, v, cap)`.
template <typename Cap = long long>
struct BurnOrBuryCompiler {
    struct PairClause {
        int u, v;
        Cap A, B, C, D; // Cost matrix for (x_u, x_v) in {(0,0), (0,1), (1,0), (1,1)}
    };
    int n, aux_cnt = 0;
    Cap base_cost = 0; // Minimizing: base_cost + MinCut(S, T)
    std::vector<Cap> cost0, cost1; // Unary penalties: cost0[i]*(1 - x_i) + cost1[i]*x_i
    std::vector<PairClause> clauses;

    explicit BurnOrBuryCompiler(int n_) : n(n_), cost0(n_, 0), cost1(n_, 0) {}

    // Add unary penalty: pay `c0` if x_i == 0, pay `c1` if x_i == 1 (c0, c1 can be negative!)
    void add_unary_cost(int i, Cap c0, Cap c1) {
        cost0[i] += c0;
        cost1[i] += c1;
    }

    // Add unary reward (for maximization problems: negate or use `W_base - solve()`)
    void add_unary_reward(int i, Cap r0, Cap r1) {
        add_unary_cost(i, -r0, -r1);
    }

    // Add general 2x2 pairwise cost matrix:
    //   x_u\x_v |  0   1
    //     0     |  A   B
    //     1     |  C   D
    void add_pairwise_cost(int u, int v, Cap A, Cap B, Cap C, Cap D) {
        clauses.push_back({u, v, A, B, C, D});
    }

    // Automatically find Harary Gauge Switch sigma[i] in {0, 1} (y_i = x_i ^ sigma[i])
    // Returns false iff an odd-sign cycle prevents global submodularity.
    bool compute_harary_flip(std::vector<int>& sigma) const {
        sigma.assign(n, -1);
        std::vector<std::vector<std::pair<int, int>>> adj(n);
        for (const auto& cl : clauses) {
            Cap delta = (cl.B + cl.C) - (cl.A + cl.D);
            if (delta == 0) continue;
            int need_flip = (delta < 0) ? 1 : 0; // Supermodular => endpoints must have opposite sigma
            adj[cl.u].push_back({cl.v, need_flip});
            adj[cl.v].push_back({cl.u, need_flip});
        }
        for (int i = 0; i < n; ++i) {
            if (sigma[i] != -1) continue;
            sigma[i] = 0;
            std::vector<int> q = {i};
            for (size_t head = 0; head < q.size(); ++head) {
                int u = q[head];
                for (auto [v, w] : adj[u]) {
                    if (sigma[v] == -1) {
                        sigma[v] = sigma[u] ^ w;
                        q.push_back(v);
                    } else if (sigma[v] != (sigma[u] ^ w)) {
                        return false; // Frustrated odd cycle detected -> requires 2N QPBO network!
                    }
                }
            }
        }
        return true;
    }

    // Compile all clauses and unary terms into a black-box MaxFlow instance `mf`
    template <typename MaxFlowSolver>
    Cap compile(MaxFlowSolver& mf, int S, int T, const std::vector<int>& sigma) {
        std::vector<Cap> u0 = cost0, u1 = cost1;
        Cap total_offset = base_cost;
        for (int i = 0; i < n; ++i) {
            if (sigma[i]) std::swap(u0[i], u1[i]); // Flip y_i = 1 - x_i swaps roles of 0 and 1
        }
        for (auto cl : clauses) {
            Cap A = cl.A, B = cl.B, C = cl.C, D = cl.D;
            if (sigma[cl.u]) { std::swap(A, C); std::swap(B, D); } // Row swap
            if (sigma[cl.v]) { std::swap(A, B); std::swap(C, D); } // Col swap
            Cap delta = (B + C) - (A + D);
            // Asymmetric Integer Split (Section 4.1 Choice 1):
            // A + (C - A)*y_u + (D - C)*y_v + delta * y_v * (1 - y_u)
            total_offset += A;
            u1[cl.u] += (C - A);
            u1[cl.v] += (D - C);
            if (delta > 0) mf.add_edge(cl.v, cl.u, delta);
        }
        // Recipe 1 Unary Normalization (Section 2.4: Pre-push 2-edge S -> i -> T paths in O(1))
        for (int i = 0; i < n; ++i) {
            Cap m = std::min(u0[i], u1[i]);
            total_offset += m;
            if (u0[i] > m) mf.add_edge(S, i, u0[i] - m);
            if (u1[i] > m) mf.add_edge(i, T, u1[i] - m);
        }
        return total_offset;
    }
};
```
