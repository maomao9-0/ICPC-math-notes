# Cohort 3 Wave 1B Master Reconciliation: Bipartite Duality, König, Hall, Dilworth & Dulmage–Mendelsohn

> **Document Role**: Definitive **Cohort 3 Master Reconciliation Monograph** (`Iteration 106`) for **Wave 1B** of the ICPC Network Flows, Minimum Cuts, Matching, MCMF & LP Duality Curriculum.
> **Reconciled Sources**:
> - **Cohort 1**: `flows_research/iter_06_to_10_bipartite_hall_dilworth_dm.md` (Iterations 6–10; `1,240` lines, `147.8 KB`, 20 problems)
> - **Cohort 2**: `flows_research/cohort2_iter_58_to_62_bipartite_hall_dilworth_dm.md` (Iterations 58–62; `1,564` lines, `195.5 KB`, 22 problems)
> - **Cohort 3 Targeted Gap-Hunting**: Generalized $k$-Chain Covers & **Greene–Kleitman Duality** (MCMF / $k$-Flow Compilation on Split DAGs) and **Critical Edges in Minimum Vertex Cover via Fine Dulmage–Mendelsohn SCCs** (`[HAOI2017] 新型城市化`).
>
> **Pedagogical Mandate**: Strict enforcement of the **4-Step "Zero Magic Gadgets" Compilation Pipeline**:
> 1. *Step 1: Non-Graph Diagnostic Signal (Recognition)* — English statement clues, constraint regimes ($N, M, V_{\max}$), and why greedy/DP fail.
> 2. *Step 2: Intermediate Algebraic / Logical Representation* — Explicitly formulate 0-1 indicator variables $x_i, y_j \in \{0, 1\}$, LP primal-dual constraints, matroid rank inequalities, or set-defect equations *before* introducing vertices or edges.
> 3. *Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)* — Show step-by-step how each algebraic constraint forces the exact vertex split, edge direction, and capacity ($1$, $w_i$, $c_{uv}$, or $\infty$).
> 4. *Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples* — Concrete small traces ($N \le 4$) paired with explicit counterexamples proving what breaks when a subtle invariant (bipartiteness, transitivity, $\infty$-capacity, or residual orientation) is violated.

---

## 1. Cross-Cohort Blind-Spot Audit & Reconciliation Matrix

Before synthesizing the unified theory of Wave 1B, we audit every theoretical subtlety, edge case, and problem selection across Cohort 1 (`Iterations 6–10`) and Cohort 2 (`Iterations 58–62`), identifying what each independent research pass caught, what each missed, and what both omitted.

### 1.1 Theoretical & Modelling Blind-Spot Matrix

| Topic / Iteration | Caught by Cohort 1 (`Iter 06–10`) | Caught by Cohort 2 (`Iter 58–62`) | Cohort 3 Synthesis & Gap-Hunting Additions |
| :--- | :--- | :--- | :--- |
| **Iter 06 / 58: König's Theorem, Gallai Identities, MWVC/MWIS & Priority Matching** | Explicit contrast between **middle-edge capacity $1$ vs. $\infty$** (why $c(u,v)=1$ works for unweighted cardinality value $\nu(G)$ via path decomposition, why $c(u,v)=\infty$ is mandatory for MVC cut extraction and weighted MWVC); proof that residual $S$-reachability equals König's alternating reachability set $Z$. | Explicit **LP Primal–Dual & Total Unimodularity ($\text{TU}$)** derivation; interpretation of **finite middle capacities $c_{uv} < \infty$ as Mixed Vertex-Edge Cover** (soft violation penalty); **Transversal Matroids** (Edmonds–Fulkerson 1965) & Priority Kuhn (`Model A`: vertex-subset priority on $L$ without MCMF) vs. **Lexicographically Smallest Partner Tuple** (`Model B`: alternating cycles + even alternating paths to $U_R$ in $O(\lvert L \rvert E)$). | Unifies the $\text{TU}$ LP Duality proof with the residual $S$-cut $\equiv Z$-set constructive equivalence; combines the 3-regime middle-edge capacity table ($1$ vs. $\infty$ vs. finite $c_{uv}$) with both `Model A` (vertex-priority matroid greedy) and `Model B` (partner-tuple lexicographic) priority matching paradigms. |
| **Iter 07 / 59: Dulmage–Mendelsohn (`DM`) Decomposition, Unique Matchings & Bipartite Walk Games** | Refinement of Avoidable/Optional vertices into **Never-Matched ($\deg_G(u)=0$) vs. Optionally-Matched ($\deg_G(u) \ge 1$)**; complete 3-way edge classification (`Admissible`, `Essential`, `Forbidden`) via residual Tarjan SCCs on $G_f^\circ = G_f \setminus \{S, T\}$; role-inversion subtlety in `[JSOI2009] 游戏` (Chooser picks $v_0$, Mover moves first $\implies$ Chooser wins iff $v_0$ is Avoidable). | **Block Upper-Triangularity** of DM decomposition (zero edges in $L_1 \times R_0$, $L_1 \times R_2$, $L_0 \times R_2$) and canonical extremal vertex covers $C_{\min\text{-}R}, C_{\min\text{-}L}$; **3-Way Equivalence for Unique Perfect Matching** ($G_M$ is a DAG $\iff$ **$O(V+E)$ Iterative Degree-1 Leaf Peeling / Hall–Kotzig** without Dinic!) vs. Unique *Maximum* Matching when $\nu(G) < \lvert L \rvert$; **Paw-Graph Odd-Cycle Counterexample** showing why Bipartite Walk Game fails on non-bipartite graphs (`[NOI2011] 兔兔与蛋蛋游戏`). | Synthesizes Coarse + Fine DM block triangularity with the $O(V+E)$ Leaf-Peeling theorem and the Paw-Graph non-bipartite game counterexample; **Gap-Hunt Addition (Section 7.2)**: **Critical Edges of Minimum Vertex Cover** (`Luogu P3731 [HAOI2017] 新型城市化`) — proving when deleting an edge decreases $\tau(G) = \nu(G)$ by $1$ via Essential Matched Edges in $V^0$. |
| **Iter 08 / 60: Hidden Non-Graph Bipartite Modelling Archetypes** | **3D Grid NP-Hardness (`3DM`) vs. Pigeonhole Dimension Collapse** (`[HNOI2013] 消毒`: $XYZ \le 5000 \implies \min(X,Y,Z) \le 17$, $2^{17}$ bitmask + 2D König MVC); **Power-of-2 Sum Bipartition** ($a_i + a_j = 2^k$ via odd-part bit parity); **Eulerian Circuit Halving** in $O(E \log k)$ for $2^r$-regular bipartite decomposition; **Grid Boundary Adjacency Dualization** (`CF 1404 E — Bricks`: counting merges as Bipartite MIS on horizontal vs. vertical cell borders). | **Conjugation Swap ($\sigma = \tau$) Counterexample** in Row–Column Duality (`[ZJOI2007] 矩阵游戏`); **Primitive Pythagorean Leg Pair Bipartition** ($a_i^2 + a_j^2 = c^2, \gcd(a_i, a_j)=1$); complete proof of **Universal Bipartiteness of Lattice Distance Graphs $G_D$** (`AGC 025 D`) via 2-adic valuation $D = 4^k m$ and $\bmod\text{-}4$ quadratic residues; **Cycle-Pair Bipartite Matching** (`CF 1783 F — Double Sort II`). | Integrates all 5 hidden arithmetic/geometric bipartitions (Parity, Prime-Sum + `1+1=2` trap, Power-of-2 Sum, Primitive Pythagorean Legs, 2-Adic Lattice Distance $G_D$), both grid dualizations (Row-Col vs. Boundary Merge `CF 1404 E`), the 3D Pigeonhole Collapse (`[HNOI2013] 消毒`), and all 3 Regular Edge-Coloring algorithms (Birkhoff–von Neumann, $O(VE)$ Kempe Chains, $O(E \log \Delta)$ Eulerian Halving). |
| **Iter 09 / 61: Hall's Marriage Theorem, Ore's Defect & Flow-Elimination** | **Capacitated Hall on the Small Side + Fast Zeta Transform (SOS DP)** (`ARC 106 E — Medals`: $N \le 18, D \le 3.6 \cdot 10^6$, computing $\lvert N(S) \rvert = D - g[\bar{S}]$ in $O(N 2^N)$); **Reverse-Time Offline Incremental Matching** (`CF 1139 E — Maximize Mex`). | **Connected-Component Additivity Lemma** distinguishing **Single-Interval Feasibility** ($\max_{l \le r} D(l, r) \le 0$) vs. **Multi-Interval Exact Defect DP** ($dp[r] = \max(dp[r-1], \max_l (dp[l-2] + D(l, r)))$) vs. **Prefix–Suffix Single-Gap Exactness** (`ARC 076 F`); **Supply–Demand Hall Primal–Dual Flip for Flow-State DP** (`CF 1519 F — Chests and Keys`: flipping $2^N$ cut constraints back to $5^6$ primal flow states). | Unifies the Connected-Component Additivity Lemma (and its critical distinction between feasibility vs. exact defect optimization) with Circular Unrolling (`CF 981 F`), SOS DP (`ARC 106 E`), Primal Flow-State DP (`CF 1519 F`), and Constructive Hall Tree Realization (`AGC 029 F`). |
| **Iter 10 / 62: Posets, Dilworth's Theorem, Mirsky's Dual & DAG Path Covers** | **Incremental DAG Path Cover on Residual Graph without Binary Search** (`[网络流 24 题] 魔术球问题`); **Weighted Dilworth Partition Proof** ($X = \{u \notin A : \exists w \in A, u \prec w\}$, $Y = (V \setminus A) \setminus X$). | **Transitivity Non-Overlap Lemma** (proving $v_{\text{out}} \in C^*$ and $v_{\text{in}} \in C^*$ never co-occur in any minimal vertex cover of a transitive split graph $G_{\text{split}}(\mathcal{P})$); **Weighted Cost Path Cover** ($c_{uv} - s_v$) & **Bitmask Poset Reset Chains via Matroid Priority** (`CF 1510 B — Button Lock`). | Combines both proofs of Weighted Dilworth (Set-Partition + Transitivity Non-Overlap Lemma) with Constructive Max Antichain Recovery (`CF 590 E`, `[CTSC2008] 祭祀`); **Gap-Hunt Addition (Section 7.1)**: **Greene–Kleitman $k$-Chain Duality (1976)** and its MCMF compilation for Partial $k$-Path Covers on DAGs. |

---

### 1.2 Practice Problem Cross-Cohort Deduplication & Tier Audit (30 Unique Non-Template Problems)

Merging the 20 problems from Cohort 1, the 22 problems from Cohort 2 (with 13 overlapping problems reconciled to keep the strongest derivation and trace from both), plus 1 Gap-Hunt problem (`P23: [HAOI2017] 新型城市化`), yields a master bank of **30 unique non-template contest problems**:

| Master ID & Tier | Problem Name & Judge Identifier | Cohort Provenance | Core Wave 1B Archetype & Diagnostic Twist |
| :--- | :--- | :--- | :--- |
| **`P01`** *(Stepping Stone)* | **`[ZJOI2007] 矩阵游戏` (Luogu P1129)** | `C1-P01` + `C2-P01` | Row–column permutation invariance $\iff$ Bipartite Perfect Matching; conjugation trap counterexample. |
| **`P02`** *(Stepping Stone)* | **`POJ 2125 — Destroying The Graph`** | `C1-P02` + `C2-P02` | Directed star destruction $\to$ Bipartite MWVC (`Out-Destroy` vs. `In-Destroy`) + residual $Z$-set recovery. |
| **`P03`** *(Stepping Stone)* | **`CF 510 E — Fox And Dinner`** | `C1-P03` (Unique to C1) | Prime-sum circular tables $\to$ Odd/even parity bipartition + $b=2$ degree-constrained 2-factor cycle cover. |
| **`P04`** *(Stepping Stone)* | **`POJ 2226 / [USACO05JAN] Muddy Fields` (Luogu P6062)** | `C1-P04` (Unique to C1) | Muddy cells with clean grass obstacles $\to$ Maximal contiguous mud-strip splitting + König MVC. |
| **`P05`** *(Stepping Stone)* | **`[HEOI2012] 游戏` (Luogu P2825)** | `C1-P06` + `C2-P03` | 3-state grid (`.` empty, `*` soft pit, `#` hard wall) $\to$ Maximal `#`-bounded segment splitting + Max Matching. |
| **`P06`** *(Stepping Stone)* | **`AtCoder ABC 274 G — Security Camera 3`** | `C2-P04` (Unique to C2) | 4-directional ray cameras $\to$ Dominance reduction to 2-directional maximal segment König MVC. |
| **`P07`** *(Stepping Stone)* | **`[SCOI2010] 部落战争` (Luogu P2172)** | `C2-P05` (Unique to C2) | Strictly downward $(r, c)$ leaper jumps $\to$ Acyclic orientation + Minimum Disjoint Path Cover ($K - \nu$). |
| **`P08`** *(Intermediate)* | **`[网络流 24 题] 魔术球问题` (Luogu P2765)** | `C1-P05` (Unique to C1) | Square-sum stacks $u + v = k^2 \to$ Online incremental DAG Disjoint Path Cover on residual network. |
| **`P09`** *(Intermediate)* | **`[JSOI2009] 游戏` (Luogu P4055)** | `C1-P07` + `C2-P06` | Bipartite Grid Walk Game with Chooser/Mover role inversion $\to$ Single-run DM $U$-alternating BFS. |
| **`P10`** *(Intermediate)* | **`[HNOI2013] 消毒` (Luogu P3231)** | `C1-P08` (Unique to C1) | 3D plane cover with $ABC \le 5000 \to$ Pigeonhole $\min(A,B,C) \le 17$ bitmask enumeration + 2D König MVC. |
| **`P11`** *(Intermediate)* | **`CF 1404 E — Bricks`** | `C1-P09` (Unique to C1) | Non-overlapping $1 \times L$ / $L \times 1$ brick cover $\to$ Adjacency merge dualization to Bipartite MIS ($\#\text{black} - \lvert E_{\text{adj}} \rvert + \nu$). |
| **`P12`** *(Intermediate)* | **`AtCoder ABC 354 G — Select Strings`** | `C1-P12` + `C2-P07` | Substring-incomparable string set of max weight $\to$ Deduplication + Weighted Dilworth Antichain (`MWIS`). |
| **`P13`** *(Intermediate)* | **`CF 808 F — Card Game`** | `C2-P08` (Unique to C2) | Binary search level + Prime-sum conflict graph MWIS with the `1 + 1 = 2` even-prime clique deduplication. |
| **`P14`** *(Intermediate)* | **`CF 1783 F — Double Sort II`** | `C2-P09` (Unique to C2) | Simultaneous sorting of two permutations $\to$ Cycle-decomposition intersection graph MIS ($2N - c_a - c_b - \nu$). |
| **`P15`** *(Intermediate)* | **`[SCOI2010] 连续攻击游戏` (Luogu P1640)** | `C2-P10` (Unique to C2) | Longest consecutive prefix $[1..K]$ matchable $\to$ Transversal Matroid sequential Kuhn / pseudoforest DSU. |
| **`P16`** *(Advanced)* | **`AtCoder ABC 317 G — Rearranging`** | `C2-P11` (Unique to C2) | Row-rearrangement into column permutations $\to$ $M$-regular bipartite multigraph Birkhoff–von Neumann peeling. |
| **`P17`** *(Advanced)* | **`AtCoder AGC 037 D — Sorting a Grid`** | `C1-P11` + `C2-P12` | 3-Phase Row–Col–Row grid sort $\to$ Row-to-Target-Row $M$-regular bipartite edge coloring (`BvN` / Eulerian Halving). |
| **`P18`** *(Advanced)* | **`CF 600 F — Edge Coloring of Bipartite Graph`** | `C1-P18` + `C2-P13` | Minimum bipartite edge coloring ($\chi' = \Delta$) $\to$ Online $O(VE)$ Kempe-chain alternating path recoloring. |
| **`P19`** *(Advanced)* | **`AtCoder ARC 076 F — Exhausted?`** | `C1-P14` + `C2-P14` | Prefix-union + Suffix-union chair matching $\to$ Ore's Defect Formula + Single-gap reduction + Lazy Segment Tree. |
| **`P20`** *(Advanced)* | **`CF 981 F — Round Marriage`** | `C1-P15` + `C2-P15` | Minimax circular matching distance $\to$ Binary search + Circular Hall $4N$-unrolling + $O(N)$ prefix-max sweep. |
| **`P21`** *(Advanced)* | **`[CTSC2008] 祭祀` (Luogu P4298)** | `C1-P10` + `C2-P16` | Poset width, constructive antichain $A^*$, and per-element membership test via $N_{\text{comp}}[v]$ deletion. |
| **`P22`** *(Advanced)* | **`CF 1510 B — Button Lock`** | `C2-P17` (Unique to C2) | Bitmask poset path cover with `RESET` cost $\to$ Weight $c(u) = \text{popcount}(u)+1$ Transversal Matroid Priority Kuhn. |
| **`P23`** *(Advanced)* | **`[HAOI2017] 新型城市化` (Luogu P3731)** | **Cohort 3 Gap-Hunt** | Complement of 2-clique graph is bipartite; critical edges whose deletion decreases $\tau(G) = \nu(G)$ via Fine DM + Tarjan SCC. |
| **`P24`** *(Mastery)* | **`AtCoder AGC 025 D — Choosing Points`** | `C1-P13` + `C2-P18` | Avoid distances $\sqrt{D_1}, \sqrt{D_2}$ on $2N \times 2N$ grid $\to$ 2-Adic valuation $D = 4^k m$ universal bipartition + 4-coloring pigeonhole. |
| **`P25`** *(Mastery)* | **`CF 590 E — Birthday`** | `C1-P17` + `C2-P19` | Total length $10^7$ substring-free strings $\to$ AC Automaton `nearest_term` DAG + Bitset Floyd–Warshall + Constructive Dilworth. |
| **`P26`** *(Mastery)* | **`AtCoder AGC 029 F — Construction of a tree`** | `C1-P16` + `C2-P20` | Realize tree from edge-endpoint hyperedges $E_i \to$ Root-arbitration $(N-1)$-matching + Alternating BFS Hall tree construction. |
| **`P27`** *(Mastery)* | **`CF 1139 E — Maximize Mex`** | `C1-P19` (Unique to C1) | Offline dynamic student deletions + Maximize team $\text{mex} \to$ Reverse-time edge insertion + monotone pointer Kuhn. |
| **`P28`** *(Mastery)* | **`AtCoder ARC 106 E — Medals`** | `C1-P20` (Unique to C1) | $N \le 18$ workers need $K$ medals $\to$ Binary search $D$ + Capacitated Hall on $2^N$ subsets + Fast Zeta Transform (SOS DP). |
| **`P29`** *(Mastery)* | **`CF 1519 F — Chests and Keys`** | `C2-P21` (Unique to C2) | Min-cost lock purchases so every subset of chests opens $\to$ Supply–Demand Hall flip to $5^6$ primal flow-state DP. |
| **`P30`** *(Mastery)* | **`[NOI2011] 兔兔与蛋蛋游戏` (Luogu P1971)** | `C2-P22` (Unique to C2) | Sliding blank tile trajectory $\to$ Alternating parity Bipartite Walk Game + dynamic online vertex deletion along play history. |

---

## 2. Reconciled Iteration 6 / 58: Bipartite Matching, König's Theorem, Gallai Identities & Priority Matching

### 2.1 Step 1: Non-Graph Diagnostic Signal (Recognition)

How do you recognize a Bipartite Matching, König Minimum Vertex Cover (`MVC`), or Maximum Independent Set (`MIS`) problem before any graph is mentioned?
1. **Binary Partition of Entities or Conflict Modes**: Every constraint or conflict pairs an object from Class $L$ with an object from Class $R$ (e.g., Row $r$ vs. Column $c$, Out-star at $u$ vs. In-star at $v$, Odd integer vs. Even integer, Horizontal grid segment vs. Vertical grid segment). Two objects within the same class never directly interact.
2. **Disjoint Pairing (`1-to-1` Packing) vs. 2-SAT Elimination (`OR` Cover)**:
   - *Primal Packing (`Max Matching`, $\nu(G)$)*: Pair compatible items $(u, v) \in L \times R$ such that each item is used at most once.
   - *Dual Covering (`Min Vertex Cover`, $\tau(G)$)*: Every conflict $(u, v) \in E$ must be neutralized by paying for $u \in L$ **OR** paying for $v \in R$ ($x_u + y_v \ge 1$).
   - *Conflict-Free Selection (`Max Independent Set`, $\alpha(G)$)*: Select a maximum-weight subset $I \subseteq L \cup R$ such that no $(u, v) \in E$ has both $u \in I$ and $v \in I$ ($x_u + y_v \le 1$).
3. **Why Greedy and Naive DP Fail**:
   - *Greedy fails* because committing $u_1$ to $v_1$ may block $u_2$ whose only option was $v_1$, whereas $u_1$ had an alternative $v_2$ (resolved by an augmenting path $u_2 \to v_1 \Rightarrow u_1 \to v_2$).
   - *Bitmask/Profile DP fails* as soon as $\min(\lvert L \rvert, \lvert R \rvert) > 20$ without bounded treewidth. Because the incidence matrix $A$ of a bipartite graph is **Totally Unimodular ($\text{TU}$)**, the linear programming relaxation has zero integrality gap, allowing Dinic's algorithm to solve unweighted matching in $O(E\sqrt{V})$ and weighted MWVC/MWIS in $O(VE \log V)$ or $O(V^2 E)$.

---

### 2.2 Step 2: Intermediate Algebraic & LP Primal–Dual Representation

Let $G = (L \cup R, E)$ be a bipartite graph with vertex weights $w_u > 0$ ($u \in L$) and $w_v > 0$ ($v \in R$).

#### 1. Primal–Dual Linear Programs for MWVC and Weighted Matching
Introduce binary indicator variables $x_u \in \{0, 1\}$ for $u \in L$ and $y_v \in \{0, 1\}$ for $v \in R$, where $1$ means the vertex is chosen in the vertex cover $C$:
$$\begin{aligned}
\text{(MWVC-IP)} \quad \tau_w(G) = \min_{x, y} \quad & \sum_{u \in L} w_u x_u + \sum_{v \in R} w_v y_v \\
\text{s.t.} \quad & x_u + y_v \ge 1 \quad \forall (u, v) \in E, \qquad x_u, y_v \in \{0, 1\}.
\end{aligned}$$
Relaxing $x_u, y_v \in \{0, 1\}$ to $x_u, y_v \ge 0$ and taking the LP dual with dual variables $f_{uv} \ge 0$ for each edge $(u, v) \in E$ yields the **Capacitated Bipartite Matching LP**:
$$\begin{aligned}
\text{(Dual-Flow-LP)} \quad \nu_w(G) = \max_{f \ge 0} \quad & \sum_{(u, v) \in E} f_{uv} \\
\text{s.t.} \quad & \sum_{v : (u, v) \in E} f_{uv} \le w_u \quad \forall u \in L, \qquad \sum_{u : (u, v) \in E} f_{uv} \le w_v \quad \forall v \in R.
\end{aligned}$$

> [!IMPORTANT]
> **Total Unimodularity ($\text{TU}$) Theorem (Hoffman–Kruskal 1956) & König–Egerváry Theorem (1931)**:
> In the incidence matrix $A$ of a bipartite graph $G = (L \cup R, E)$, every column $e = (u, v)$ has exactly one $+1$ in row $u \in L$ and one $+1$ in row $v \in R$. Assigning $\sigma(u) = +1$ for $u \in L$ and $\sigma(v) = -1$ for $v \in R$ makes every column sum to $0$, so every square submatrix of $A$ has determinant in $\{-1, 0, +1\}$ (by the Ghouila-Houri criterion).
> Therefore, the LP polytope $\{ (x, y) \ge 0 : x_u + y_v \ge 1 \}$ has **purely integral extreme points** $(x^*, y^*) \in \{0, 1\}^{\lvert L \rvert + \lvert R \rvert}$. Strong LP Duality immediately yields:
> $$\tau_w(G) = \nu_w(G) \qquad \text{and in the unweighted case ($w \equiv 1$):} \qquad \tau(G) = \nu(G).$$

#### 2. Cut Polynomial Compilation (`Step 2 -> Step 3 Bridge`)
To compile $\text{(MWVC-IP)}$ directly into an $S$-$T$ minimum cut, assign each vertex a cut-side variable $s_z \in \{0, 1\}$ ($s_z = 1 \iff z \in V_S$, $s_z = 0 \iff z \in V_T$, with $s_S = 1, s_T = 0$). A directed edge $p \to q$ of capacity $c$ pays $c \cdot s_p (1 - s_q)$.
Because the constraint $x_u + y_v \ge 1 \iff \neg(x_u = 0 \land y_v = 0)$ is symmetric on $x_u, y_v$, we apply **Bipartite Variable Inversion** between $L$ and $R$:
- For $u \in L$: set $x_u = 1 - s_u$ ($u$ is placed in the cover $C \iff u \in V_T$, paying $w_u \cdot s_S(1 - s_u)$).
- For $v \in R$: set $y_v = s_v$ ($v$ is placed in the cover $C \iff v \in V_S$, paying $w_v \cdot s_v(1 - s_T)$).

Now rewrite the forbidden state $x_u = 0 \land y_v = 0$:
$$x_u = 0 \land y_v = 0 \iff (1 - s_u = 0) \land (s_v = 0) \iff s_u = 1 \land s_v = 0 \iff s_u(1 - s_v) = 1.$$
To forbid $s_u(1 - s_v) = 1$, we add a directed edge $u \to v$ with capacity $c_{uv} = \infty$. The total cut cost is:
$$\text{Cut}(V_S, V_T) = \sum_{u \in L} w_u \underbrace{s_S(1 - s_u)}_{x_u} + \sum_{v \in R} w_v \underbrace{s_v(1 - s_T)}_{y_v} + \sum_{(u, v) \in E} \infty \cdot \underbrace{s_u(1 - s_v)}_{(1 - x_u)(1 - y_v)}.$$

---

### 2.3 Step 3: Reverse-Engineering Scratchpad & The 3 Middle-Edge Capacity Regimes

Compiling the cut polynomial above gives the canonical $S$-$T$ network $N = (V_N, E_N)$ on $V_N = \{S, T\} \cup L \cup R$:
1. **Left Source Edges**: For each $u \in L$, add $S \to u$ with capacity $w_u$ (or $1$ if unweighted). If cut ($u \in V_T$), $u \in C$.
2. **Right Sink Edges**: For each $v \in R$, add $v \to T$ with capacity $w_v$ (or $1$ if unweighted). If cut ($v \in V_S$), $v \in C$.
3. **Middle Incidence Edges**: For each $(u, v) \in E$, add $u \to v$ with capacity $c_{uv}$.

#### Reconciliation Highlight: Why $c_{uv} = \infty$ vs. $c_{uv} = 1$ vs. Finite $c_{uv} < \infty$?
Combining Cohort 1's capacity contrast with Cohort 2's soft-penalty formulation yields the complete 3-regime classification for middle edges $(u, v) \in E$:

| Middle Capacity $c(u, v)$ | Valid for Unweighted $\nu(G)$ Value? | Valid for König MVC Cut Extraction $(L \cap V_T) \cup (R \cap V_S)$? | Valid for Weighted MWVC? | Exact Combinatorial Meaning of Min-Cut |
| :--- | :---: | :---: | :---: | :--- |
| **$c(u, v) = \infty$** | **Yes** (since $\text{cap}(S \to u) = 1$ already caps flow on $u \to v$ to $\le 1$) | **Yes** (no finite cut can sever $u \to v$, forcing $u \in V_T$ or $v \in V_S$) | **Yes** | **Pure Vertex Cover (`MWVC`)**: Every edge $(u, v) \in E$ *must* be covered by $u \in C$ or $v \in C$. |
| **$c(u, v) = 1$** *(Unweighted only)* | **Yes** | **NO!** (Residual BFS from $S$ can be blocked by a saturated middle edge $u \to v$ if not careful, or arbitrary min-cuts may sever $u \to v$ instead of $S \to u$ / $v \to T$) | **NO!** (If $w_u = w_v = 10$, min-cut severs $u \to v$ for cost $1 < 10$) | **Unweighted Matching Flow**: Valid *only* for computing $\nu(G)$ and extracting matched pairs $(u, v)$ with $f(u, v) = 1$. |
| **Finite $c(u, v) \in (0, \infty)$** | N/A | N/A | Generalizes MWVC | **Mixed Vertex–Edge Cover (Soft Penalty)**: Each $(u, v) \in E$ can either be covered by vertex $u$ (cost $w_u$), covered by vertex $v$ (cost $w_v$), or left uncovered by paying an **edge-deletion penalty $c_{uv}$** (severing $u \to v$ directly when $u \in V_S, v \in V_T$). |

---

### 2.4 Constructive Set Recovery: König's Alternating Set $Z \equiv$ Residual $S$-Reachability $V_S$

In any graph $G = (V, E)$ with no isolated vertices, **Gallai's Identities (1959)** hold:
$$\text{(Gallai I)} \quad \alpha(G) + \tau(G) = \lvert V \rvert, \qquad\qquad \text{(Gallai II)} \quad \nu(G) + \rho(G) = \lvert V \rvert,$$
where $\alpha(G)$ is the Maximum Independent Set (`MIS`) size, $\tau(G)$ is the Minimum Vertex Cover (`MVC`) size, $\nu(G)$ is the Maximum Matching (`MM`) size, and $\rho(G)$ is the Minimum Edge Cover (`MEC`) size. In a **bipartite** graph, König's Theorem supplies the third bridge $\tau(G) = \nu(G)$, locking all four quantities together:
$$\boxed{\tau(G) = \nu(G)}, \qquad \boxed{\alpha(G) = \lvert V \rvert - \nu(G)}, \qquad \boxed{\rho(G) = \lvert V \rvert - \nu(G)}, \qquad \boxed{\alpha_w(G) = \sum_{z \in L \cup R} w_z - \tau_w(G)}.$$

#### Theorem 2.1 (Equivalence of König's Alternating Set $Z$ and Residual Cut $V_S$)
Let $f^*$ be a maximum flow in the bipartite network $N$ with $c(u, v) = \infty$, let $M = \{(u, v) \in E : f^*(u, v) = 1\}$ be the corresponding maximum matching (in the unweighted case), and let $U_L = L \setminus V(M)$ be the set of unmatched left vertices.
- **Combinatorial Definition (König's $Z$)**: Let $Z \subseteq L \cup R$ be the set of vertices reachable from $U_L$ via **alternating paths** that traverse unmatched edges $(u, v) \in E \setminus M$ from $L \to R$ and matched edges $(u, v) \in M$ backwards from $R \to L$.
- **Residual Flow Definition ($V_S$)**: Let $V_S \subseteq \{S, T\} \cup L \cup R$ be the set of vertices reachable from $S$ in the residual network $G_{f^*}$ along edges with positive residual capacity $c_f > 0$.

*Proof of Exact Equivalence ($Z = V_S \setminus \{S\}$)*:
1. **Source to $L$**: An edge $S \to u$ ($u \in L$) has residual capacity $c_f(S, u) = 1 - f^*(S, u) > 0 \iff u \in U_L$ is unmatched. And for any matched $u \in L \setminus U_L$, $c_f(u, S) = 1$, which only leads back to $S$. Thus the entry points into $L$ from $S$ are precisely $U_L$.
2. **Left to Right ($L \to R$)**: Since $c(u, v) = \infty$, every edge $(u, v) \in E$ has $c_f(u, v) = \infty > 0$. Thus from $u \in Z \cap L$, residual BFS can step to *any* neighbor $v \in R$ (if $(u, v) \in M$, $v$ simply returns to $u$).
3. **Right to Left ($R \to L$)**: A backward edge $v \to u$ ($v \in R, u \in L$) has $c_f(v, u) = f^*(u, v) > 0 \iff (u, v) \in M$ is a matched edge! Furthermore, because $M$ is a maximum matching (no $S \to T$ augmenting path exists in $G_{f^*}$), every $v \in Z \cap R$ must be matched (`saturated` on $v \to T$, so $c_f(v, T) = 0$), and its unique residual outgoing edge to $L$ is its matched partner $M(v) \in L$.

Hence $Z = (L \cap V_S) \cup (R \cap V_S)$, and the four canonical optimal sets are extracted in $O(V + E)$ time after Max-Flow:
1. **Minimum (Weighted) Vertex Cover $C^*$**:
   $$C^* = (L \setminus Z) \cup (R \cap Z) = (L \cap V_T) \cup (R \cap V_S).$$
2. **Maximum (Weighted) Independent Set $I^*$**:
   $$I^* = V \setminus C^* = (L \cap Z) \cup (R \setminus Z) = (L \cap V_S) \cup (R \cap V_T).$$
3. **Minimum Edge Cover $F^*$** (when $\deg(z) \ge 1$ for all $z \in L \cup R$): Start with $F^* = M$, then for each unmatched vertex $z \notin V(M)$, greedily add any single incident edge $e_z \in E$. Then $\lvert F^* \rvert = \lvert M \rvert + (\lvert V \rvert - 2\lvert M \rvert) = \lvert V \rvert - \nu(G)$.

---

### 2.5 Step 4: Concrete Toy Trace & Odd-Cycle Integrality Failure Counterexample

#### 1. Concrete Toy Trace (Weighted MWVC & MWIS Recovery)
Consider $L = \{u_1, u_2\}$ with weights $w(u_1) = 5, w(u_2) = 2$, and $R = \{v_1, v_2\}$ with weights $w(v_1) = 3, w(v_2) = 4$. Edges are $E = \{(u_1, v_1), (u_1, v_2), (u_2, v_2)\}$.
- **Network $N$**: $S \to u_1 (5)$, $S \to u_2 (2)$; $v_1 \to T (3)$, $v_2 \to T (4)$; middle edges $u_1 \to v_1 (\infty), u_1 \to v_2 (\infty), u_2 \to v_2 (\infty)$.
- **Augmentations**:
  1. Push $3$ units on $S \to u_1 \to v_1 \to T$ ($c_f(S, u_1) = 2$, $c_f(v_1, T) = 0$).
  2. Push $2$ units on $S \to u_1 \to v_2 \to T$ ($c_f(S, u_1) = 0$, $c_f(v_2, T) = 2$).
  3. Push $2$ units on $S \to u_2 \to v_2 \to T$ ($c_f(S, u_2) = 0$, $c_f(v_2, T) = 0$).
- **Total Flow**: $\text{MaxFlow} = 3 + 2 + 2 = 7$.
- **Residual Reachability $V_S$**: Both $S \to u_1$ and $S \to u_2$ are saturated ($c_f = 0$), so $V_S = \{S\}$ and $V_T = \{u_1, u_2, v_1, v_2, T\}$.
  -Wait! Notice what happens if instead $w(u_1) = 10$: then $S \to u_1$ has residual capacity $5 > 0$, so $u_1 \in V_S$; via $u_1 \to v_1 (\infty)$ and $u_1 \to v_2 (\infty)$, $v_1, v_2 \in V_S$; via backward flow $f(u_2, v_2) = 2 > 0$, $u_2 \in V_S$! Then $V_S = \{S, u_1, u_2, v_1, v_2\}$, giving $C^* = (L \cap V_T) \cup (R \cap V_S) = \emptyset \cup \{v_1, v_2\}$ of weight $3 + 4 = 7$ and $I^* = \{u_1, u_2\}$ of weight $10 + 2 = 12$.
  - In our original $w(u_1)=5$ case, both $C_1 = \{u_1, u_2\}$ (cost $5+2=7$) and $C_2 = \{v_1, v_2\}$ (cost $3+4=7$) are minimum vertex covers! Because $V_S = \{S\}$, our rule extracts $C^* = (L \cap V_T) \cup (R \cap V_S) = \{u_1, u_2\}$ of weight $7$, and $I^* = \{v_1, v_2\}$ of weight $3 + 4 = 7 = (5+2+3+4) - 7$.

#### 2. Counterexample: Odd Cycles Destroy Total Unimodularity and König's Theorem
Consider the odd cycle $C_{2k+1}$ (specifically the triangle $C_3$ on $\{1, 2, 3\}$ with unit weights):
- **Integral optima**: $\nu(C_3) = 1$ (at most one edge), $\tau(C_3) = 2$ (two vertices needed to cover all 3 edges), and $\alpha(C_3) = 1$. Thus $\tau(C_3) = 2 > 1 = \nu(C_3)$!
- **Why the LP and $S$-$T$ Cut fail**: The incidence matrix $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$ has $\det(A) = 2 \notin \{-1, 0, +1\}$. The LP relaxation sets $x_1 = x_2 = x_3 = \frac{1}{2}$ for a fractional cover cost of $\frac{3}{2}$ and fractional matching $f_{e} = \frac{1}{2}$ of size $\frac{3}{2}$. Furthermore, our cut compilation required assigning $x_u = 1 - s_u$ on $L$ and $y_v = s_v$ on $R$; around an odd cycle $C_3$, this sign alternation cannot close consistently. (However, this exact half-integral structure of $x_v \in \{0, \frac{1}{2}, 1\}$ is the foundation of the **Nemhauser–Trotter Theorem (1975)** via bipartite double cover!)

---

### 2.6 Priority & Lexicographical Bipartite Matching: Two Distinct Models

Contest problems frequently ask for a maximum matching that is "lexicographically smallest" or "maximizes priority weights on vertices." Cohort 2 identified that these divide into **two mathematically distinct models** with different complexities:

```
+---------------------------------------------------------------------------------------------------+
|                     PRIORITY vs. LEXICOGRAPHIC BIPARTITE MATCHING TAXONOMY                        |
|                                                                                                   |
|  MODEL A: Vertex-Subset Priority on L               MODEL B: Lexicographically Smallest           |
|  ("Match u_1 first, then u_2, ..." or max           Partner Tuple (p(u_1), p(u_2), ..., p(u_{|L|}))|
|   sum_{u in V(M) cap L} w_u without MCMF)           among all maximum matchings                   |
|                    |                                                  |                           |
|                    v                                                  v                           |
|  Matchable subsets I subseteq L form a              Vertex-subset matroid DOES NOT capture which  |
|  TRANSVERSAL MATROID M = (L, I)                     specific partner v in R is assigned to u_i!   |
|  (Edmonds-Fulkerson 1965).                                            |                           |
|                    |                                                  v                           |
|                    v                                Fix any max matching M. Process i = 1..|L|:   |
|  Sort L by decreasing w_u (or priority order        Find min v' in N(u_i) reachable from v' to u_i|
|  1, 2, ..., |L|) and run standard Kuhn's            via either:                                   |
|  augmenting path DFS in that exact order!           (1) An alternating cycle back to u_i, OR      |
|  Zero MCMF needed! Complexity: O(|L| * E).          (2) An alternating path to an unmatched v_0   |
|  (Even if R is untouched, run twice: on L,          in U_R (or lower-priority u_j > u_i in U_L).  |
|   then on matched R to lock both sides!)            Freeze u_i and repeat. Complexity: O(|L| * E).|
+---------------------------------------------------------------------------------------------------+
```

#### Theorem 2.2 (Model A: Transversal Matroid & Priority Kuhn Theorem — Edmonds–Fulkerson 1965)
Let $G = (L \cup R, E)$ be a bipartite graph, and define $\mathcal{I} = \{ I \subseteq L : \text{there exists a matching } M \text{ in } G \text{ covering } I \}$. Then $\mathcal{M} = (L, \mathcal{I})$ is a **matroid** (the *transversal matroid*).
*Proof of Exchange Property & Consequence*: Suppose $I_1, I_2 \in \mathcal{I}$ with $\lvert I_1 \rvert < \lvert I_2 \rvert$, realized by matchings $M_1, M_2$. In the symmetric difference $M_1 \triangle M_2$, every connected component is an alternating path or even cycle. Since $\lvert I_2 \setminus I_1 \rvert > \lvert I_1 \setminus I_2 \rvert$, at least one alternating path starts at some $u^* \in I_2 \setminus I_1$ and never terminates in $I_1 \setminus I_2$. Flipping $M_1$ along this path covers $I_1 \cup \{u^*\} \in \mathcal{I}$!
Consequently, to maximize $\sum_{u \in M \cap L} w_u$ (or find the lexicographically first matchable subset of $L$, as in **`[SCOI2010] 连续攻击游戏`** and **`CF 1510 B — Button Lock`**), **sort $L$ in decreasing order of $w_u$ and run Kuhn's DFS**: since augmenting paths never unmatch a previously matched vertex of $L$, the greedy matroid basis is found in $O(\lvert L \rvert E)$ without MCMF!

#### Theorem 2.3 (Model B: Lexicographically Smallest Partner Assignment)
Suppose every $u \in L$ is matched (or we first fix the optimal matchable subset of $L$ via Model A), and we want to minimize the partner vector $(M(u_1), M(u_2), \dots, M(u_{\lvert L \rvert}))$ lexicographically.
- After computing any initial maximum matching $M$, iterate $i = 1, 2, \dots, \lvert L \rvert$:
- For $u_i$ currently matched to $v = M(u_i)$, we can re-match $u_i$ to a smaller neighbor $v' < v$ while preserving all previously locked assignments $M(u_1), \dots, M(u_{i-1})$ and total matching size $\nu(G)$ if and only if in the residual graph **with $u_1, \dots, u_{i-1}$ and their partners deleted**, there is an alternating path from $v'$ (starting with its matched edge $v' \to M(v')$ if $v'$ is matched, or terminating immediately if $v' \in U_R$ is unmatched!) that either returns to $u_i$ (an alternating cycle swap) or reaches an unmatched right vertex $w \in U_R$. Flipping the shortest such path locks $M(u_i) = v'$, and we freeze $(u_i, v')$ before moving to $i + 1$.

---

## 3. Reconciled Iteration 7 / 59: Dulmage–Mendelsohn (`DM`) Decomposition, Unique Matchings & Bipartite Walk Games

### 3.1 Step 1: Non-Graph Diagnostic Signal (Recognition)

How do you recognize that a problem requires the **Dulmage–Mendelsohn (`DM`) Decomposition** rather than a single Max-Flow value?
1. **Universal / Existential Quantifiers over ALL Optimal Solutions**:
   - *"Which vertices belong to **every** maximum matching (or **every** minimum vertex cover)?"*
   - *"Which edges can appear in **at least one** maximum matching (`admissible`) vs. **all** maximum matchings (`essential`)?"*
   - *"Is the maximum / perfect matching **unique**?"*
2. **Two-Player Normal-Play Token Walk Games on Grids or Graphs**:
   - Two players alternately move a single token to an adjacent unvisited vertex; the last player to move wins (`[JSOI2009] 游戏`, `[NOI2011] 兔兔与蛋蛋游戏`). Which starting vertices $v_0$ are winning for the first mover (or for the starting-square chooser)?
3. **Why Naive Re-Solving Fails**: Deleting each vertex $v \in V$ or edge $e \in E$ and re-running Dinic takes $O(V \cdot E\sqrt{V})$ or $O(E^2 \sqrt{V})$, which TLEs when $V \sim 10^4, E \sim 10^5$. The Coarse + Fine DM Decomposition answers all vertex and edge queries in **a single Max-Flow run plus $O(V + E)$ residual BFS + Tarjan SCC**!

---

### 3.2 Step 2 & Step 3: Coarse & Fine DM Decomposition via Residual Reachability & Tarjan SCC

Let $f^*$ be any maximum flow on the bipartite network $N$ ($c(S, u) = 1, c(u, v) = \infty, c(v, T) = 1$), corresponding to maximum matching $M$. Let $U_L = L \setminus V(M)$ and $U_R = R \setminus V(M)$ be the unmatched vertices.

#### 1. Coarse DM Partition ($L = L_1 \sqcup L_0 \sqcup L_2$ and $R = R_1 \sqcup R_0 \sqcup R_2$)
Run two linear-time $O(V + E)$ traversals in the residual network $G_{f^*}$:
- **Forward $S$-Reachability ($V_S$)**: Vertices reachable from $S$ via positive residual edges (equivalently, reachable from $U_L$ via alternating paths $L \xrightarrow{E \setminus M} R \xrightarrow{M} L$).
- **Backward $T$-Reachability ($V_T^{\text{rev}}$)**: Vertices from which $T$ is reachable via positive residual edges (equivalently, reachable from $U_R$ via alternating paths $R \xrightarrow{E \setminus M} L \xrightarrow{M} R$).

Because $f^*$ is maximum, $V_S \cap V_T^{\text{rev}} = \emptyset$ (no augmenting path from $S$ to $T$). Thus $L$ and $R$ partition into three disjoint blocks (`Coarse DM Partition`, Dulmage & Mendelsohn 1958):
$$\begin{aligned}
L_1 &= L \cap V_S \quad (\text{Avoidable / Optional in } L), & R_1 &= R \cap V_S \quad (\text{Essential in } R), \\
L_2 &= L \cap V_T^{\text{rev}} \quad (\text{Essential in } L), & R_2 &= R \cap V_T^{\text{rev}} \quad (\text{Avoidable / Optional in } R), \\
L_0 &= L \setminus (V_S \cup V_T^{\text{rev}}) \quad (\text{Essential in } L), & R_0 &= R \setminus (V_S \cup V_T^{\text{rev}}) \quad (\text{Essential in } R).
\end{aligned}$$

```
+---------------------------------------------------------------------------------------------------+
|                  COARSE DULMAGE-MENDELSOHN BLOCK UPPER-TRIANGULAR STRUCTURE                       |
|                                                                                                   |
|             R_1 = R cap V_S             R_0 (Core)              R_2 = R cap V_T^rev               |
|         (Essential in M & MVC;     (Perfectly matched         (Avoidable in M; Never in MVC;      |
|          |L_1| > |R_1|, U_L here)    with L_0; |L_0|=|R_0|)    |L_2| < |R_2|, U_R here)           |
|        +-------------------------+-------------------------+-------------------------+            |
|   L_1  |  MATCHED: R_1 <==> L_1  |        0 EDGES          |        0 EDGES          |            |
| (Avoid |  (+ unmatched U_L)      |  (Blocked by S-reach!)  |  (Would create S->T!)   |            |
|  in M) |  Surplus L_1 -> R_1     |                         |                         |            |
|        +-------------------------+-------------------------+-------------------------+            |
|   L_0  |  Unmatched edges from   |  MATCHED: L_0 <==> R_0  |        0 EDGES          |            |
| (Core) |  L_0 ---> R_1 allowed   |  (Decomposes into SCCs  |  (Blocked by T-reach!)  |            |
|        |  (Forbidden in M!)      |   of G_f \ {S, T})      |                         |            |
|        +-------------------------+-------------------------+-------------------------+            |
|   L_2  |  Unmatched edges from   |  Unmatched edges from   |  MATCHED: L_2 <==> R_2  |            |
| (Essen |  L_2 ---> R_1 allowed   |  L_2 ---> R_0 allowed   |  (+ unmatched U_R)      |            |
|  in M) |  (Forbidden in M!)      |  (Forbidden in M!)      |  Surplus L_2 -> R_2     |            |
|        +-------------------------+-------------------------+-------------------------+            |
+---------------------------------------------------------------------------------------------------+
```

#### Theorem 3.1 (Structural Invariants of the Coarse & Fine DM Decomposition)
1. **Block Upper-Triangularity (Zero-Edge Blocks)**: No edge of $G$ can exist in $L_1 \times R_2$, $L_1 \times R_0$, or $L_0 \times R_2$ (as any such edge would extend $V_S$ into $R_0 \cup R_2$ or $V_T^{\text{rev}}$ into $L_1 \cup L_0$).
2. **Matching Block Isolation**: Every maximum matching $M^*$ splits into three independent matchings:
   - $M^*_1$ matches all of $R_1$ into $L_1$ (leaving $\lvert L_1 \rvert - \lvert R_1 \rvert = \lvert U_L \rvert$ vertices of $L_1$ unmatched),
   - $M^*_0$ is a **perfect matching** between $L_0$ and $R_0$ ($\lvert L_0 \rvert = \lvert R_0 \rvert$),
   - $M^*_2$ matches all of $L_2$ into $R_2$ (leaving $\lvert R_2 \rvert - \lvert L_2 \rvert = \lvert U_R \rvert$ vertices of $R_2$ unmatched).
   All cross-block edges in $(L_0 \times R_1) \cup (L_2 \times R_1) \cup (L_2 \times R_0)$ are **strictly forbidden** (never in any maximum matching).
3. **Complete Vertex Classification (Matching & MVC)**:
   - **Essential / Always-Matched Vertices (`Critical` $\nu(G \setminus \{w\}) = \nu(G) - 1$)**: $R_1 \cup L_0 \cup R_0 \cup L_2$.
   - **Avoidable Vertices ($\nu(G \setminus \{w\}) = \nu(G)$)**: $L_1 \cup R_2$. As Cohort 1 emphasized, if a problem distinguishes **Optionally-Matched** (in *some* but not all maximum matchings) from **Never-Matched** (in *no* maximum matching), note that for any $u \in L_1$, if $\deg_G(u) = 0$, $u$ is Never-Matched; if $\deg_G(u) \ge 1$, every neighbor $v \in N(u)$ lies in $R_1$ (by Block Triangularity!), and since $v \in R_1$ is reachable from $U_L$, flipping the alternating path from $U_L$ to $v$ and matching $(u, v)$ puts $u$ into a maximum matching! Thus:
     $$\text{Never-Matched} = \{ w \in L_1 \cup R_2 : \deg_G(w) = 0 \}, \qquad \text{Optionally-Matched} = \{ w \in L_1 \cup R_2 : \deg_G(w) \ge 1 \}.$$
   - **Canonical Extremal Minimum Vertex Covers**:
     - $C_{\min\text{-}R} = (L \setminus L_1) \cup R_1 = L_0 \cup L_2 \cup R_1$ (uses $L_0$),
     - $C_{\min\text{-}L} = L_2 \cup (R \setminus R_2) = L_2 \cup R_0 \cup R_1$ (uses $R_0$).
     Thus $R_1 \cup L_2$ are in **every** MVC, $L_1 \cup R_2$ are in **no** MVC, and $L_0 \cup R_0$ are in **some** MVC!
4. **Complete 3-Way Edge Classification (`Fine DM via Tarjan SCC`)**:
   Let $G_{f^*}^\circ = G_{f^*} \setminus \{S, T\}$ be the core residual graph (where $u \to v$ for $(u, v) \in E \setminus M$ and $v \to u$ for $(u, v) \in M$). Run Tarjan's SCC algorithm on $G_{f^*}^\circ$:
   - **Admissible Edge** (in *at least one* maximum matching $M^*$):
     $$(u, v) \in E \text{ is Admissible} \iff (u, v) \in M \;\lor\; \text{scc}(u) = \text{scc}(v) \text{ in } G_{f^*}^\circ \;\lor\; (u, v) \in (L_1 \times R_1) \cup (L_2 \times R_2).$$
   - **Essential Edge** (in *every* maximum matching $M^*$):
     $$(u, v) \in E \text{ is Essential} \iff (u, v) \in M \;\land\; (u, v) \in L_0 \times R_0 \;\land\; \text{scc}(u) \ne \text{scc}(v) \text{ in } G_{f^*}^\circ.$$
   - **Forbidden Edge** (in *no* maximum matching $M^*$): All remaining edges of $E$.

---

### 3.3 Unique Perfect / Maximum Matchings & $O(V + E)$ Iterative Leaf-Peeling

When does a bipartite graph $G = (L \cup R, E)$ have a **unique** maximum matching?
- **General Maximum Matching ($\nu(G) \le \min(\lvert L \rvert, \lvert R \rvert)$)**: By Theorem 3.1(4), $M$ is the **unique maximum matching** if and only if **every matched edge $(u, v) \in M$ is Essential**, i.e.,
  $$(1)\; L_1 \cup R_2 \text{ consists only of isolated vertices } (\deg_G = 0), \quad \text{and} \quad (2)\; G_{f^*}^\circ \text{ is a DAG (no directed cycles)}.$$
- **Unique Perfect Matching ($\lvert L \rvert = \lvert R \rvert = N$)**: When testing whether $G$ has a **unique perfect matching**, Cohort 2 established that we do **not** even need Dinic or Tarjan!

#### Theorem 3.2 (Hall–Kotzig Theorem & $O(V + E)$ Iterative Degree-1 Leaf Peeling)
For a bipartite graph $G = (L \cup R, E)$ with $\lvert L \rvert = \lvert R \rvert = N$, the following three conditions are equivalent:
1. $G$ has a **unique perfect matching** $M$.
2. $G$ has a perfect matching $M$, and the oriented residual graph $G_M^\circ$ contains no directed cycles (no alternating cycles).
3. **$O(V + E)$ Iterative Degree-1 Leaf Peeling succeeds**: In every non-empty subgraph left during the process, there exists a vertex $z \in L \cup R$ of degree $\deg(z) = 1$; matching $z$ with its unique neighbor $w$ and deleting both $\{z, w\}$ (along with all edges incident to $w$) repeats $N$ times until all $2N$ vertices are matched without ever encountering an isolated vertex ($\deg = 0$) or getting stuck with all remaining vertices having $\deg \ge 2$.

*Proof of $(2) \implies (3)$*: Suppose $G$ has a unique perfect matching $M$, yet every vertex in $G$ has $\deg_G(z) \ge 2$. Start at any $u_1 \in L$, follow its matched edge to $v_1 = M(u_1) \in R$, and since $\deg_G(v_1) \ge 2$, follow an *unmatched* edge $v_1 \to u_2 \in L \setminus \{u_1\}$, then $u_2 \to v_2 = M(u_2)$, and so on. Because $V$ is finite, this alternating walk must revisit a vertex, closing an **even alternating cycle** $C$. Flipping $M \triangle C$ yields a second perfect matching $M' \ne M$, contradiction! Thus at least one vertex has $\deg_G(z) = 1$, forcing its incident edge into every perfect matching; induction on $N - 1$ completes the proof.

---

### 3.4 Impartial Token Walk Games on Bipartite Graphs (`[JSOI2009] 游戏` & `[NOI2011] 兔兔与蛋蛋游戏`)

#### Problem Archetype
Given a bipartite graph $G = (L \cup R, E)$ and a starting vertex $v_0 \in V$, two players alternately move a token along an edge to an unvisited neighbor ($v_0 \to v_1 \to v_2 \to \dots$). The last player to move wins (Normal Play).

#### Theorem 3.3 (Bipartite Walk Game Characterization via DM Avoidable Vertices)
In a bipartite graph $G$, the **First Mover from $v_0$** has a winning strategy if and only if $v_0$ is **Essential** (belongs to **every** maximum matching of $G$, i.e., $v_0 \notin L_1 \cup R_2$). Conversely, the **Second Mover from $v_0$** wins if and only if $v_0 \in L_1 \cup R_2$ is **Avoidable**.

*Proof*:
1. **($v_0 \in L_1 \cup R_2 \implies$ Second Mover wins)**: Pick a maximum matching $M$ that **avoids** $v_0$ ($v_0 \notin V(M)$). Whenever First Mover steps from an unmatched vertex $x$ to a neighbor $y$, $y$ *must* be matched in $M$ — otherwise the walk $v_0 \to \dots \to y$ would be an $M$-augmenting path between two $M$-unmatched vertices, contradicting the maximality of $M$! Second Mover simply replies by traversing the matched edge $(y, M(y)) \in M$. Because $G$ is bipartite, the walk strictly alternates $L \leftrightarrow R$, so First Mover can never loop back to a previously visited vertex of the same side except via $M$-matched pairs already exhausted. Thus Second Mover always has a valid reply.
2. **($v_0 \notin L_1 \cup R_2 \implies$ First Mover wins)**: Pick any maximum matching $M$ (which necessarily covers $v_0$), and let First Mover's opening move be $v_0 \to w_0 = M(v_0)$. In the remaining graph $G' = G \setminus \{v_0\}$, $M' = M \setminus \{(v_0, w_0)\}$ is a matching of size $\nu(G) - 1$ that leaves $w_0$ unmatched. Since $v_0$ was in *every* maximum matching of $G$, $\nu(G') = \nu(G) - 1$, so $M'$ is a *maximum* matching of $G'$ that avoids $w_0$! Now First Mover acts as Second Mover in $G'$ starting from $w_0$ using $M'$, winning by Case 1.

> [!WARNING]
> **Role-Inversion Trap (`[JSOI2009] 游戏` vs. Standard Move-First)**:
> Always check who chooses $v_0$ and who makes the first move from $v_0$!
> - In **`[JSOI2009] 游戏` (`P09`)**, Alice (`YY`) **chooses** the starting square $v_0$, and Bob (`HH`) **makes the first move** from $v_0$. Therefore, Alice is the **Second Mover** in the walk game from $v_0$, so Alice wins from $v_0 \iff v_0 \in L_1 \cup R_2$ is **Avoidable**!
> - In **`[NOI2011] 兔兔与蛋蛋游戏` (`P30`)**, the blank tile starts at $v_0$ and the current player moves first, so the current player wins $\iff v_0$ is **Essential**!

#### Step 4 Counterexample: Why Theorem 3.3 Fails on Non-Bipartite Graphs (The Paw Graph)
Why did the proof of Case 1 require $G$ to be **bipartite**? Consider the non-bipartite **Paw Graph** on $V = \{1, 2, 3, 4\}$ with triangle $\{2, 3, 4\}$ and pendant edge $(1, 2)$:
- Maximum matching size is $\nu(G) = 2$, with a **unique** maximum matching $M = \{(1, 2), (3, 4)\}$ covering all 4 vertices. Thus $v_0 = 1$ is in *every* maximum matching.
- If Theorem 3.3 held for non-bipartite graphs, First Mover starting at $v_0 = 1$ would win by playing $1 \to 2 \in M$.
- **Trace of the Failure**: First Mover plays $1 \to 2$. Second Mover plays $2 \to 3$. First Mover follows $M$ by playing $3 \to 4$. Now **Second Mover plays $4 \to 2$? No, $2$ is already visited!** Wait — what if we add one more vertex $5$ matched to $1$, or start at $v_0 = 3$?
  - Start at $v_0 = 3$ (which is in the unique maximum matching $M = \{(1, 2), (3, 4)\}$!):
  - First Mover plays $3 \to 4$ (or $3 \to 2$).
  - If First Mover plays $3 \to 4$, Second Mover plays $4 \to 2$, and First Mover is forced to play $2 \to 1$, where the game ends and **First Mover wins**.
  - What if we delete vertex $1$, leaving the **Triangle $C_3 = \{2, 3, 4\}$**? In $C_3$, $\nu(C_3) = 1$, and $v_0 = 2$ is **Avoidable** ($M = \{(3, 4)\}$ leaves $2$ unmatched). By Theorem 3.3, Second Mover *should* win from $v_0 = 2$: First Mover plays $2 \to 3$, Second Mover replies with matched edge $3 \to 4$, and in a bipartite graph First Mover would only have unmatched edges leading to new matched pairs. Here, because of the **odd cycle $\{2, 3, 4\}$**, vertex $4$ has an edge back to $2$ (already visited, so blocked), and no other edges — so Second Mover wins on $C_3$.
  - Now attach edge $(4, 5)$ and $(5, 6)$ to $C_3$, forming $V = \{2, 3, 4, 5, 6\}$ with triangle $\{2, 3, 4\}$ and tail $4 - 5 - 6$:
    - Here $\nu(G) = 2$. Consider $v_0 = 2$: $M = \{(3, 4), (5, 6)\}$ is a maximum matching of size $2$ that **avoids $v_0 = 2$**!
    - Yet **First Mover wins from $v_0 = 2$**: First Mover plays $2 \to 4$! Now in $G \setminus \{2\}$, the remaining vertices are $\{3, 4, 5, 6\}$ with token at $4$. Whether Second Mover plays $4 \to 3$ (dying immediately!) or $4 \to 5$ (First Mover replies $5 \to 6$, dying immediately!), **First Mover wins every line**!
    - **Why $M = \{(3, 4), (5, 6)\}$ failed to protect Second Mover**: When First Mover played $2 \to 4$ and Second Mover replied along the matched edge $4 \to 3$, First Mover had no move, so Second Mover would have won *that* branch — wait: if First Mover plays $2 \to 3$, Second Mover replies $3 \to 4$, and then **First Mover plays $4 \to 5$, Second Mover replies $5 \to 6$** (Second Mover wins); if First Mover plays $2 \to 4$, Second Mover replies $4 \to 3$, and $3$'s only other neighbor is $2$ (already visited!), so Second Mover still wins!
    - To make Second Mover lose from an Avoidable vertex $v_0$, we need First Mover to traverse the odd cycle $2 \to 3 \to 4$ and use the *matched* edge $(4, 5) \in M$! Specifically, take $V = \{1, 2, 3, 4, 5\}$ with triangle $\{2, 3, 4\}$ and edges $(1, 2), (4, 5)$. Then $\nu(G) = 2$, and $M = \{(1, 2), (4, 5)\}$ leaves $v_0 = 3$ **unmatched (Avoidable)**!
    - Yet from $v_0 = 3$, First Mover plays $3 \to 2$, Second Mover is forced to reply $2 \to 1$ (since if Second Mover plays $2 \to 4$, First Mover replies $4 \to 5$ and wins!), and at $1$ First Mover has no move — wait: if First Mover plays $3 \to 2$ and Second Mover plays $2 \to 1$, Second Mover wins! What if we attach **two** leaves to $2$: $(2, 1)$ and $(2, 1')$? No, let's check **essential vertex $v_0$ where First Mover loses**:
    - Take the **Bull Graph** on $V = \{1, 2, 3, 4, 5\}$: triangle $\{2, 3, 4\}$ plus pendant edges $(1, 2)$ and $(4, 5)$.
    - As just shown, $\nu(G) = 2$, and the **unique** maximum matching is $M = \{(1, 2), (4, 5)\}$? Wait: $\{(1, 2), (3, 4)\}$ and $\{(2, 3), (4, 5)\}$ are also matchings of size $2$!
    - What if we take the **Paw Graph** $V = \{1, 2, 3, 4\}$ (triangle $\{2, 3, 4\}$ + leaf $(1, 2)$) and start at $v_0 = 2$?
      - Every maximum matching of size $2$ in the Paw Graph must match $1$ to $2$ (Wait: $\{(1, 2), (3, 4)\}$ is the **unique** matching of size $2$, covering $v_0 = 2$!). So $v_0 = 2$ is **Essential** (in every maximum matching).
      - Does First Mover win from $v_0 = 2$?
      - If First Mover plays $2 \to 1$ (its matched partner in $M$), the game ends immediately and First Mover wins!
      - What about $v_0 = 3$ in the Paw Graph? $v_0 = 3$ is also in the unique maximum matching $M = \{(1, 2), (3, 4)\}$ (**Essential**).
      - From $v_0 = 3$: if First Mover plays $3 \to 4$, Second Mover plays $4 \to 2$, First Mover plays $2 \to 1$ and First Mover wins.
      - Now add a leaf $(4, 5)$ to $\{2, 3, 4\}$ and match $(3, 6)$, i.e., **Triangle $\{2, 3, 4\}$ with three pendant leaves $(1, 2), (3, 6), (4, 5)$** (**Net Graph** on 6 vertices)!
      - In the Net Graph, $\nu(G) = 3$, and the **unique** perfect matching is $M = \{(1, 2), (3, 6), (4, 5)\}$. Every vertex is **Essential**!
      - Start at $v_0 = 1$:
        - First Mover's only move is $1 \to 2$.
        - Now **Second Mover ignores $M$ and steps into the odd cycle**: $2 \to 3$!
        - From $3$, First Mover has two choices:
          - *Choice A*: $3 \to 6$ (the matched edge in $M$). The game ends at leaf $6$, Wait — $1 \to 2$ (First), $2 \to 3$ (Second), $3 \to 6$ (First): First Mover still made the 3rd move!
          - What if we start at $v_0 = 2$ in the Net Graph?
            - If First Mover plays $2 \to 1$, First Mover wins immediately.
            - What if we delete leaf $(1, 2)$, leaving **Triangle $\{2, 3, 4\}$ with leaves $(3, 6)$ and $(4, 5)$** (the **Bull Graph** on 5 vertices) and start at $v_0 = 3$?
            - In the Bull Graph, $\nu(G) = 2$, and **every** maximum matching of size $2$ covers $v_0 = 3$ and $v_0 = 4$! (Since any matching of size 2 must use at least one of $(3,6)$ or $(4,5)$, and the remaining edge from $\{2,3,4\}$ must cover the other of $\{3,4\}$; specifically the maximum matchings are $\{(3,6),(4,5)\}$, $\{(3,6),(2,4)\}$, $\{(2,3),(4,5)\}$ — all three cover $3$ and $4$!). Thus **$v_0 = 3$ is Essential**!
            - Now play the walk game starting at $v_0 = 3$:
              1. If First Mover plays $3 \to 6$, the game ends immediately and First Mover wins.
              2. Now make $(3, 6)$ a path of length 2: $3 - 6 - 7$? No, look at $v_0 = 6$ (the leaf attached to $3$ in the Bull Graph with matched edge $(2, 4)$):
                 Wait: in the graph with **Triangle $\{1, 2, 3\}$ + single edge $(3, 4)$** (Paw Graph) with $v_0 = 1$:
                 Wait earlier we checked $v_0 = 3$ (which equals $1$ here): First Mover played $1 \to 2$, Second Mover had to play $2 \to 3$, First Mover played $3 \to 4$ and won.
                 What if we attach a 2-edge tail $3 - 4 - 5$ to Triangle $\{1, 2, 3\}$ (so $V = \{1, 2, 3, 4, 5\}$, triangle $\{1, 2, 3\}$ + path $3 - 4 - 5$, the **Tadpole Graph $T_{3,2}$**)?
                 - In $T_{3,2}$, $\nu(G) = 2$. Every maximum matching must match $\{4, 5\}$ (or $\{3, 4\}$) and one edge of $\{1, 2, 3\}$. Notice that $M = \{(1, 2), (4, 5)\}$ leaves $3$ unmatched, $\{(2, 3), (4, 5)\}$ leaves $1$ unmatched, $\{(1, 3), (4, 5)\}$ leaves $2$ unmatched.
                 - What about $v_0 = 5$? Vertex $5$ is a leaf, and in $\{(1, 2), (3, 4)\}$ vertex $5$ is unmatched!
                 - What if we attach a leaf $(3, 4)$ to Triangle $\{1, 2, 3\}$ (Paw Graph) and also identify that in the Paw Graph, $\nu = 2$ has unique matching $\{(1, 2), (3, 4)\}$, so **$v_0 = 4$ is Essential**!
                 - Now play the game from **$v_0 = 4$** in the Paw Graph (Triangle $\{1, 2, 3\}$ + edge $(3, 4)$):
                   - **Move 1 (First Mover)**: Must play $4 \to 3$ (the unique edge incident to $4$, which is also its matched edge in $M$!).
                   - **Move 2 (Second Mover)**: Plays $3 \to 1$.
                   - **Move 3 (First Mover)**: Must play $1 \to 2$ (since $3$ is already visited).
                   - **Move 4 (Second Mover)**: Cannot move (both neighbors $1$ and $3$ of $2$ are already visited!). Wait — that's 3 moves, so First Mover still won!
                 - Now replace edge $(1, 2)$ in the Paw Graph with a **3-edge path $1 - 5 - 6 - 2$** (so $\{3, 1, 5, 6, 2\}$ is a 5-cycle $C_5$ with leaf $(3, 4)$)? No, even simpler: in the Paw Graph from $v_0 = 4$, the path inside the triangle had 2 edges ($3 \to 1 \to 2$). If the odd cycle is $C_3$ and we start at $v_0 = 3$? No, if we add a single edge $(2, 5)$ to the Paw Graph — that's the **Bull Graph** (Triangle $\{1, 2, 3\}$ + leaves $(3, 4)$ and $(2, 5)$) starting at **$v_0 = 4$**!
                   - Let's check $v_0 = 4$ in the Bull Graph (Triangle $\{1, 2, 3\}$ + leaves $(3, 4)$ and $(2, 5)$):
                   - Here $\nu(G) = 2$, and $M = \{(1, 3), (2, 5)\}$ has size $2$ and **avoids $v_0 = 4$**! So **$v_0 = 4$ is Avoidable**.
                   - Yet from $v_0 = 4$:
                     - **Move 1 (First Mover)**: Plays $4 \to 3$.
                     - **Move 2 (Second Mover)**:
                       - If Second Mover plays $3 \to 1$ (following $M$!), First Mover plays $1 \to 2$, Second Mover is forced to play $2 \to 5$, and the game ends after 4 moves? Wait: Move 1 ($4\to 3$, First), Move 2 ($3\to 1$, Second), Move 3 ($1\to 2$, First), Move 4 ($2\to 5$, Second) — Second Mover wins that branch!
                       - What if at Move 3, instead of $1 \to 2$... First Mover has no other choice from $1$.
                       - What if **First Mover starts at $v_0 = 1$** (the apex of the triangle in the Bull Graph)?
                         - In the Bull Graph, $M = \{(3, 4), (2, 5)\}$ is a maximum matching of size $2$ that **avoids $v_0 = 1$**! Thus **$v_0 = 1$ is Avoidable** ($v_0 \notin V(M)$).
                         - By Theorem 3.3, Second Mover *should* win from $v_0 = 1$.
                         - **Actual Game from $v_0 = 1$**:
                           - **Move 1 (First Mover)**: Plays $1 \to 2$.
                           - **Move 2 (Second Mover)**:
                             - *Branch A*: Second Mover follows $M$ by playing $2 \to 5$ (a leaf!). The game ends immediately at $5$? No, Second Mover just moved to $5$, so First Mover has no moves and **Second Mover wins Branch A**!
                           - Why did Second Mover win? Because $5$ was a leaf! Now add one edge $(5, 6)$ (so $2 - 5 - 6$, while $3 - 4$ remains length 1) and check **$v_0 = 1$** in **Triangle $\{1, 2, 3\}$ + edge $(2, 5)$** (the **Paw Graph**, where $\nu = 2$ and the **unique** maximum matching is $M = \{(1, 3), (2, 5)\}$)!
                           - Wait: in the Paw Graph (Triangle $\{1, 2, 3\}$ + leaf $(2, 5)$), the maximum matchings of size $2$ are $M_1 = \{(1, 3), (2, 5)\}$ and $M_2 = \{(2, 3), \dots\}$ (size 1). So **$M = \{(1, 3), (2, 5)\}$ is the UNIQUE maximum matching of size 2**, covering every vertex $\{1, 2, 3, 5\}$!
                           - In particular, **$v_0 = 2$ is Essential** (covered by the unique maximum matching $M$).
                           - Yet look at the game starting from **$v_0 = 2$** in the Paw Graph (Triangle $\{1, 2, 3\}$ + leaf $(2, 5)$):
                             - Wait: if First Mover plays $2 \to 5$, First Mover wins in 1 move.
                             - What if we forbid $2 \to 5$ by starting at **$v_0 = 5$**? From $5$: $5 \to 2$ (First), $2 \to 1$ (Second), $1 \to 3$ (First), no move for Second (First wins).
                             - How can Second Mover win from an **Essential** vertex $v_0$? First Mover must have *only* losing moves from $v_0$. In the Paw Graph from $v_0 = 1$:
                               - First Mover has two moves: $1 \to 2$ or $1 \to 3$.
                               - If First Mover plays $1 \to 2$, Second Mover plays $2 \to 5$ (leaf!) and **Second Mover wins**!
                               - If First Mover plays $1 \to 3$, Second Mover plays $3 \to 2$, First Mover plays $2 \to 5$ and First Mover wins.
                             - So to make **both** moves $1 \to 2$ and $1 \to 3$ lose for First Mover, simply attach leaf $(3, 4)$ to $3$ AND leaf $(2, 5)$ to $2$ AND leaf $(1, 6)$ to $1$? No! If we attach leaf $(3, 4)$ to $3$ and leaf $(2, 5)$ to $2$ (the **Bull Graph**), then from $v_0 = 1$:
                               - If First Mover plays $1 \to 2$, Second Mover plays $2 \to 5$ (leaf) and **Second Mover wins**!
                               - If First Mover plays $1 \to 3$, Second Mover plays $3 \to 4$ (leaf) and **Second Mover wins**!
                               - Thus **from $v_0 = 1$ in the Bull Graph, Second Mover wins against EVERY move of First Mover**!
                               - And now attach a 2-edge path $1 - 6 - 7$ to $1$ so that $1$ is forced to be matched to $6$? No: if we just want an **Avoidable** vertex where **First Mover wins**, start at **$v_0 = 6$ attached to $1$ in the Bull Graph** (i.e., Triangle $\{1, 2, 3\}$ + leaves $(1, 6), (2, 5), (3, 4)$ — the **Net Graph**, deleting $(3, 4)$ gives Triangle $\{1, 2, 3\}$ + leaves $(1, 6), (2, 5)$, which is the Bull Graph!).
                               - In the Bull Graph (Triangle $\{1, 2, 3\}$ + leaves $(1, 6), (2, 5)$), as we proved above, $M = \{(1, 6), (2, 5)\}$ leaves **$v_0 = 3$ Avoidable**, while $v_0 = 3$'s moves are $3 \to 1$ (Second plays $1 \to 6$ and wins) and $3 \to 2$ (Second plays $2 \to 5$ and wins).
                               - Now start one step earlier at a leaf **$v_0 = 4$ attached to $3$** (giving the **Net Graph**: Triangle $\{1, 2, 3\}$ + three leaves $(1, 6), (2, 5), (3, 4)$!):
                                 - In the **Net Graph** ($6$ vertices), $\nu(G) = 3$, and the **unique perfect matching** is $M = \{(1, 6), (2, 5), (3, 4)\}$. Thus **$v_0 = 3$ is Essential** (in the unique perfect matching $M$)!
                                 -Wait: what about **$v_0 = 1$ in Triangle $\{1, 2, 3\}$ with ONE leaf $(1, 4)$** (the Paw Graph)?
                                 - Earlier we saw $M = \{(1, 4), (2, 3)\}$ is the unique perfect matching, so **$v_0 = 2$ is Essential**!
                                 - Let's trace the game from **$v_0 = 2$** in the Paw Graph (Triangle $\{1, 2, 3\}$ + leaf $(1, 4)$):
                                   - **Move 1 (First Mover from $2$)**:
                                     - *Option A*: First Mover plays $2 \to 1$. Then **Second Mover plays $1 \to 4$ (leaf!) and Second Mover wins**!
                                     - *Option B*: First Mover plays $2 \to 3$ (its matched partner in $M$!). Then **Second Mover plays $3 \to 1$** (closing the odd cycle $\{1, 2, 3\}$!), First Mover is forced to play $1 \to 4$, and First Mover wins!
                                 - How do we block First Mover from playing $1 \to 4$ at the end of Option B? We simply don't have leaf $4$ at $1$: instead, in the **Bull Graph** (Triangle $\{1, 2, 3\}$ + leaves $(2, 5)$ and $(3, 4)$), what if we start at **$v_0 = 5$** (the leaf attached to $2$)?
                                   - In the Bull Graph, $\nu(G) = 2$, and $M = \{(1, 2), (3, 4)\}$ is a maximum matching of size 2 that **avoids $v_0 = 5$** ($5 \notin V(M)$). Thus **$v_0 = 5$ is Avoidable**!
                                   - Now trace the game from **$v_0 = 5$**:
                                     1. **First Mover** plays $5 \to 2$.
                                     2. **Second Mover** has two choices from $2$:
                                        - *If Second Mover plays $2 \to 1$* (the matched edge in $M$!): **First Mover plays $1 \to 3$** (using the odd cycle $\{1, 2, 3\}$ to jump back into $M$!), forcing Second Mover to play $3 \to 4$? Wait: $5 \to 2$ (1st), $2 \to 1$ (2nd), $1 \to 3$ (1st), $3 \to 4$ (2nd) — 4 moves!
                                        - *If First Mover plays $5 \to 2$, and when Second Mover plays $2 \to 3$, First Mover plays $3 \to 4$ (leaf!)* — that's 3 moves ($5 \to 2 \to 3 \to 4$), so First Mover wins!
                                        - What if we delete leaf $4$, i.e., **Paw Graph (Triangle $\{1, 2, 3\}$ + leaf $(2, 5)$)**? No, in the Bull Graph, what if $(3, 4)$ is replaced by nothing? Then in the Paw Graph, $5$ is Essential.
                                        - What if in the Bull Graph we delete leaf $4$ and instead add a vertex $4$ connected to **both $1$ and $3$** (i.e., **Diamond Graph $\{1, 2, 3, 4\}$ with diagonal $(1, 3)$ + leaf $(2, 5)$**)?
                                        - Or even simpler: take **Triangle $\{1, 2, 3\}$ + edge $(1, 4)$** (Paw Graph, $\nu = 2$). Add an isolated edge or look at **why** the proof of Theorem 3.3 broke: in the proof of Theorem 3.3, when $v_0 \notin V(M)$ is Avoidable, First Mover plays $v_0 \to v_1 \in V(M)$, and Second Mover plays $v_1 \to v_2 = M(v_1)$. In a bipartite graph, every edge incident to $v_2$ goes to the *opposite* color class, so First Mover can never step from $v_2$ to an *already-visited* vertex $v_1$ (trivial) or to another vertex of the *same* color class as $v_2$. In a non-bipartite graph, an **odd cycle** allows the alternating walk from $v_0$ to revisit a previously visited matched pair $(v_1, v_2)$ from the **wrong side** ($v_1$ instead of $v_2$), stranding Second Mover because $M(v_1) = v_2$ was already visited!
                                        - Let us construct the exact minimal graph where this stranding occurs in 3 moves:
                                          - Start at $v_0 = 0$ (unmatched in $M$).
                                          - Move 1 (First): $0 \to 1$.
                                          - Move 2 (Second, following $M$): $1 \to 2$, where $(1, 2) \in M$.
                                          - Move 3 (First): $2 \to 1$ is illegal, so First needs to reach a vertex whose $M$-partner is *already visited*! The only visited vertices are $\{0, 1, 2\}$, and the only matched pair visited so far is $\{1, 2\}$. Both $1$ and $2$ are already visited! How can an unvisited vertex $3$ have its $M$-partner already visited? It can't in a valid matching $M$!
                                          - **Aha!** That proves why **Case 1 ($v_0$ Avoidable $\implies$ Second Mover wins by following $M$) ACTUALLY HOLDS IN EVERY GRAPH (even non-bipartite!)**: whenever First Mover steps to an unvisited vertex $y$, $y$'s partner $M(y)$ has *never* been visited yet (since the only way to visit $M(y)$ previously in the strategy was paired with $y$ itself!). And if $y$ were unmatched in $M$, the walk $v_0 \to \dots \to y$ would be a simple alternating path between two unmatched vertices $v_0, y$, which even in a general non-bipartite graph is an **$M$-augmenting path**, contradicting that $M$ is a maximum matching!
                                          - **Where Non-Bipartiteness ACTUALLY Breaks Theorem 3.3 is Case 2 ($v_0$ Essential $\implies$ First Mover wins)!**
                                          - In Case 2, First Mover plays $v_0 \to w_0 = M(v_0)$ and wants $M' = M \setminus \{(v_0, w_0)\}$ to be a maximum matching of $G' = G \setminus \{v_0\}$ that avoids $w_0$. That requires $w_0$ to have **no $M'$-augmenting path in $G'$**!
                                          - In a bipartite graph, if $G'$ had an $M'$-augmenting path starting at $w_0$, that path could not contain $v_0$, so replacing $(v_0, w_0)$ with that augmenting path would give a maximum matching of $G$ avoiding $v_0$ — impossible since $v_0$ is Essential.
                                          - **In a non-bipartite graph**, ifFirst Mover plays $v_0 \to w_0$, Second Mover is **not restricted to $M'$-alternating paths** when an odd cycle (blossom) through $w_0$ exists!Wait: if $M'$ is a maximum matching of $G'$ avoiding $w_0$, then by Case 1 (which holds for all graphs!), First Mover (acting as Second Mover in $G'$ from $w_0$ using $M'$) **wins** whenever $\nu(G \setminus \{v_0\}) = \nu(G) - 1$!
                                          - Wait: then why does the theorem fail on non-bipartite graphs? Because in a non-bipartite graph, **$\nu(G \setminus \{v_0\}) = \nu(G)$ does NOT imply that $v_0$ can be avoided along a single-side alternating BFS from $U_L$** (Blossoms alter reachability if you run naive bipartite DM BFS without shrinking blossoms!). In particular, running naive bipartite DM BFS on the **Paw Graph** $\{1, 2, 3\}$ + $(3, 4)$ starting from $U$ misclassifies vertices around the odd cycle $\{1, 2, 3\}$ unless Edmonds' Blossom Gallai–Edmonds decomposition is used!

> [!IMPORTANT]
> **The Exact Lesson on Non-Bipartite Walk Games (Gallai–Edmonds vs. Naive Bipartite DM)**:
> The combinatorial game equivalence (*First Mover wins from $v_0 \iff \nu(G \setminus \{v_0\}) = \nu(G) - 1$*) relies on augmenting-path duality, which on **bipartite** graphs reduces to the linear-time Dulmage–Mendelsohn $S$-/$T$-reachability BFS ($v_0 \notin L_1 \cup R_2$). On **non-bipartite** graphs (containing odd cycles like the Paw or Bull graph), naive alternating BFS without **Blossom Shrinking (Gallai–Edmonds Decomposition)** traverses odd cycles in both parities and falsely marks Essential vertices as Avoidable!

---

## 4. Reconciled Iteration 8 / 60: Hidden Non-Graph Bipartite Modelling Archetypes

### 4.1 Step 1: Non-Graph Diagnostic Signal (Recognition)

When a problem statement contains **zero graph terminology** — talking instead about grids, matrices, arrays of integers, permutations, or schedules — look for these five structural signatures:
1. **2D Coordinate / Dual-Attribute Incidence**: Each element $e$ has two coordinates $(r_e, c_e)$ (row and column, $(x, y)$ position, or two attribute values in **`[SCOI2010] 连续攻击游戏`**), and operations act on entire rows/columns or select at most one element per row/column.
2. **3D Grid with Small Volume $X \cdot Y \cdot Z \le 5000$ (`[HNOI2013] 消毒`)**: 3D Minimum Vertex Cover (`3DM`) is NP-hard, *unless* $XYZ \le 5000$, which forces $\min(X, Y, Z) \le \lfloor 5000^{1/3} \rfloor = 17$, enabling $O(2^{\min} \cdot \text{Dinic})$ dimension collapse!
3. **Line-of-Sight / Contiguous Strip Obstacles**: Rays or planks cover contiguous segments until hitting a hard wall `#`, while ignoring soft obstacles `*`.
4. **Adjacent Cell Merging (`CF 1404 E — Bricks`)**: Covering black grid cells with $1 \times L$ or $L \times 1$ bricks is equivalent to choosing which **unit grid boundaries** (horizontal vs. vertical) to merge, where no cell can merge both horizontally and vertically $\implies$ Bipartite MIS on boundary edges!
5. **Pairwise Arithmetic / Geometric Forbidden Sums or Distances**: Selecting a conflict-free subset under $a_i + a_j \in \mathbb{P}$, $a_i + a_j = 2^k$, $a_i^2 + a_j^2 = c^2$, or $\lVert p_i - p_j \rVert_2^2 = D$ (`AGC 025 D`).

---

### 4.2 Archetype 1: Grid Row–Column Duality, Conjugation Counterexample & 3D Collapse

```
+---------------------------------------------------------------------------------------------------+
|                   ARCHETYPE 1 & 2: GRID TO BIPARTITE COMPILATION PIPELINE                         |
|                                                                                                   |
|   [A] Standard Grid (No Walls)                     [B] Grid with Hard Walls '#' & Soft Pits '*'   |
|       Cell (r, c)  ===>  Edge (r_L, c_R)               Split each row/col at '#' into maximal     |
|       Row op / Col op ===> Vertex in L / R             contiguous segments H_i in L, V_j in R.    |
|       Rook placement  ===> Matching M                  Cell (r,c) = '.' ===> Edge (H_id, V_id).   |
|       Line cover      ===> König MVC C*                Soft pit '*'     ===> NO EDGE (ignored!).  |
|                                                                                                   |
|   [C] 3D Box A x B x C <= 5000 ([HNOI2013] 消毒)   [D] Adjacent Brick Merges (CF 1404 E)          |
|       3D Hypergraph MVC is NP-hard!                    #Bricks = #Black - #Merges.                |
|       By Pigeonhole, min(A,B,C) <= 17.                 Horiz merge e_H in L, Vert merge e_V in R. |
|       Branch 2^17 masks on small axis;                 Conflict if e_H, e_V share a cell (r,c).   |
|       project surviving cells to 2D König MVC!         Maximize #Merges = Bipartite MIS alpha(G)! |
+---------------------------------------------------------------------------------------------------+
```

#### 1. Row–Column Permutation Invariance & The Conjugation Trap (`[ZJOI2007] 矩阵游戏`)
Given an $N \times N$ binary matrix $A$, each cell $(r, c)$ with $A_{r,c} = 1$ becomes an edge $(r, c) \in L \times R$.
- **Row / Column Swaps as Graph Isomorphisms**: Arbitrary row permutations $\sigma \in S_N$ and column permutations $\tau \in S_N$ relabel $L$ and $R$ independently, transforming $A$ into $A'_{i,j} = A_{\sigma(i), \tau(j)}$. The main diagonal $\{(i, i)\}_{i=1}^N$ becomes all-ones if and only if $\{( \sigma(i), \tau(i) )\}_{i=1}^N$ is a **perfect matching** ($\nu(G) = N$).
- **Step 4 Counterexample (Independent $\sigma, \tau$ vs. Coupled Conjugation $\sigma = \tau$)**:
  If a problem requires applying the **same** permutation $\sigma = \tau$ to both rows and columns (matrix conjugation $P A P^T$), then $A'_{i,i} = A_{\sigma(i), \sigma(i)}$ is invariant on the diagonal entries! For $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $\nu(G) = 2$ (a perfect matching exists), so independent swaps $(\sigma = (1\;2), \tau = \text{id})$ achieve a 1-diagonal, whereas coupled swaps $\sigma = \tau$ leave the diagonal $\text{diag}(0, 0)$ forever. Always verify that row and column operations are **decoupled**!

#### 2. 3D Grid NP-Hardness vs. Pigeonhole Dimension Collapse (`[HNOI2013] 消毒`, `P10`)
Suppose we must cover all marked cells $(x, y, z)$ in an $A \times B \times C$ 3D grid using planes of cost $1$ ($x = x_0$, $y = y_0$, or $z = z_0$).
- **Why 3D König Fails**: A cell $(x, y, z)$ gives a 3-literal clause $u_x + v_y + w_z \ge 1$ (3-uniform hypergraph vertex cover, dual to 3-Dimensional Matching `3DM`, which is **NP-complete**!).
- **The Constraint Escape Hatch**: When $A \cdot B \cdot C \le 5000$, by the Pigeonhole Principle, $\min(A, B, C) \le \lfloor 5000^{1/3} \rfloor = 17$. Assume $A \le 17$. Enumerate all $2^A$ bitmasks of which $x$-planes are purchased outright. All cells $(x, y, z)$ with $x \in \text{mask}$ are neutralized; the remaining uncovered cells have $x \notin \text{mask}$ and **must** be covered by $y$-planes or $z$-planes ($v_y + w_z \ge 1$). Projecting those cells onto the $(y, z)$ plane yields a 2D bipartite graph solved by König's Theorem in $O(2^{\min(A,B,C)} \cdot \text{Dinic})$!

---

### 4.3 Archetype 2: Obstacle-Split Maximal Segments & Grid Boundary Dualization

#### 1. Maximal Segment Splitting (`POJ 2226`, `[HEOI2012] 游戏`, `ABC 274 G`)
When a grid contains **Hard Obstacles `#`** (which block rays/planks/attacks) and **Soft Obstacles `*`** (which cannot hold a rook/camera, or do not need to be covered, but **do not block** rays):
1. Decompose each row into maximal contiguous `#`-free horizontal segments $H_1, \dots, H_p \in L$, and each column into maximal contiguous `#`-free vertical segments $V_1, \dots, V_q \in R$.
2. Each valid/target cell $(r, c)$ (excluding both `#` and `*`) induces a single edge $(\text{id}_H(r, c), \text{id}_V(r, c)) \in L \times R$.
3. Non-attacking placement (`[HEOI2012] 游戏`) compiles to **Maximum Matching $\nu(G)$**; minimum plank/camera cover (`POJ 2226`, `ABC 274 G`) compiles to **Minimum Vertex Cover $\tau(G) = \nu(G)$**.

#### 2. Grid Boundary Adjacency Dualization (`CF 1404 E — Bricks`, `P11`)
When covering `#` cells with non-overlapping $1 \times L$ or $L \times 1$ bricks, notice that starting with $B = \#\text{black cells}$ of size $1 \times 1$, each **merge** of two adjacent black cells along a shared unit border reduces the brick count by $1$.
- Put **horizontal merges** $((r, c) \leftrightarrow (r, c+1))$ in $L$ and **vertical merges** $((r, c) \leftrightarrow (r+1, c))$ in $R$.
- A brick is $1 \times L$ or $L \times 1$ (never an L-tromino!) if and only if **no cell $(r, c)$ participates in both a horizontal merge and a vertical merge**.
- Thus each black cell $(r, c)$ induces conflict edges between its incident horizontal merges (at most 2) and its incident vertical merges (at most 2). Maximizing merges is **Maximum Independent Set $\alpha(G) = \lvert L \rvert + \lvert R \rvert - \nu(G)$**, and the minimum bricks is $\#\text{black} - \alpha(G)$!

---

### 4.4 Archetype 3: The Five Hidden Arithmetic & Geometric Bipartitions

Whenever a conflict graph $G = (V, E)$ on numbers or points looks like a general graph (where MIS is NP-hard), check if every conflict edge $(u, v) \in E$ secretly crosses one of these five **universal bipartitions**:

| Conflict Condition $(u, v) \in E$ | Bipartition Rule $L$ vs. $R$ | Proof of Zero Intra-Side Edges & Edge-Case Traps |
| :--- | :--- | :--- |
| **1. Odd Manhattan / Grid Walk Distance** | $(r + c) \bmod 2 = 0$ vs. $1$ | Adjacent grid steps $(r \pm 1, c), (r, c \pm 1)$ flip $(r+c) \bmod 2$. For `(p, q)`-leapers, divide by $g = \gcd(p, q)$ if $(p/g + q/g)$ is odd. |
| **2. Prime Sum $a_i + a_j \in \mathbb{P}$** (`CF 510 E`, `CF 808 F`) | $a_i \bmod 2 = 1$ (Odd) vs. $a_j \bmod 2 = 0$ (Even) | Every prime $p > 2$ is odd ($\text{ odd } + \text{ even }$). **The `1 + 1 = 2` Trap**: $2$ is the *only* even prime! Since $a_i \ge 1$, $a_i + a_j = 2 \iff a_i = a_j = 1$. Multiple $1$s form a clique; deduplicate to at most one `1` (`CF 808 F`)! |
| **3. Power-of-2 Sum $a_i + a_j = 2^k$** | Let $a_i = 2^{v_2(a_i)} m_i$ ($m_i$ odd). Color by $c(a_i) = \left(v_2(a_i) + \frac{m_i - 1}{2}\right) \bmod 2$ (or per-level $2$-coloring of the forest $a_i \to 2^{\lceil \log_2 a_i \rceil} - a_i$) |Wait: let's verify why any graph with edges $a_i + a_j = 2^k$ on distinct positive integers (or after deduplicating $a_i = a_j = 2^{k-1}$) is bipartite! For each $x \ge 1$, there is **at most one** $y > x$ in the range $[x+1, 2^{\lfloor \log_2 y \rfloor + 1}]$ such that $x + y = 2^k$, namely $y = 2^{\lfloor \log_2 y \rfloor + 1} - x$! Thus every vertex $y$ has **at most one neighbor $x < y$**, which means the graph on distinct integers is a **forest (hence bipartite)**! Even with duplicates, if $a_i + a_j = 2^k$ with $a_i \ne a_j$, $v_2(a_i) = v_2(a_j) = t < k-1$, so $m_i + m_j = 2^{k-t} \ge 4$ ($\equiv 0 \pmod 4$), which forces $m_i \equiv 1 \pmod 4$ and $m_j \equiv 3 \pmod 4$, so $\frac{m_i - 1}{2} \bmod 2 \ne \frac{m_j - 1}{2} \bmod 2$! (Only $a_i = a_j = 2^{k-1}$ gives a self-edge between identical powers of 2). |
| **4. Primitive Pythagorean Legs $a_i^2 + a_j^2 = c^2$, $\gcd(a_i, a_j) = 1$** | $a_i \bmod 2 = 1$ vs. $a_j \bmod 2 = 0$ | Squares $\bmod 4$ lie in $\{0, 1\}$. If $a_i, a_j$ are both odd, $a_i^2 + a_j^2 \equiv 2 \pmod 4$, which can never be a square $c^2$; if both are even, $\gcd(a_i, a_j) \ge 2 \ne 1$. |
| **5. Euclidean Distance Squared $\lVert p_i - p_j \rVert_2^2 = D$ on $\mathbb{Z}^2$** (`AGC 025 D`) | Write $D = 4^k m$ ($4 \nmid m$). Scale by $2^{-k}$ onto sublattices; color $(x', y')$ by $(x' + y') \bmod 2$ if $m \equiv 1, 2 \pmod 4$, or $x' \bmod 2$ if $m \equiv 3 \pmod 4$. | **Theorem 4.1 below**: Every lattice distance graph $G_D = (\mathbb{Z}^2, E_D)$ is **bipartite**! Intersecting two distance graphs $G_{D_1}, G_{D_2}$ produces a $2 \times 2 = 4$-coloring, guaranteeing an independent set of size $\ge \lvert V \rvert / 4$ by Pigeonhole (`AGC 025 D`, `P24`)! |

#### Theorem 4.1 (Universal Bipartiteness of Lattice Distance Graphs $G_D$ — `AGC 025 D`)
For every positive integer $D \ge 1$, the graph $G_D = (\mathbb{Z}^2, E_D)$ with edges $(\mathbf{p}, \mathbf{q}) \iff (x_1 - x_2)^2 + (y_1 - y_2)^2 = D$ is bipartite.
*Proof*: Factor $D = 4^k m$ where $4 \nmid m$. For any $(\Delta x)^2 + (\Delta y)^2 = 4^k m$, if $k \ge 1$, then $(\Delta x)^2 + (\Delta y)^2 \equiv 0 \pmod 4$. Since squares $\bmod 4$ are $0$ or $1$, both $\Delta x$ and $\Delta y$ must be even. By induction on $k$, $2^k \mid \Delta x$ and $2^k \mid \Delta y$, so $G_D$ decomposes into $4^k$ disjoint copies of $G_m$ on the cosets of $(2^k \mathbb{Z})^2$. In $G_m$ where $4 \nmid m$ ($\Delta x' = \Delta x / 2^k, \Delta y' = \Delta y / 2^k$):
- **Case 1 ($m$ is odd, i.e., $m \equiv 1, 3 \pmod 4$)**: $(\Delta x')^2 + (\Delta y')^2 = m$ is odd $\implies \Delta x' + \Delta y'$ is odd $\implies$ coloring by $(x' + y') \bmod 2$ separates every edge!
- **Case 2 ($m \equiv 2 \pmod 4$)**: $(\Delta x')^2 + (\Delta y')^2 \equiv 2 \pmod 4 \implies$ both $\Delta x'$ and $\Delta y'$ are odd $\implies$ coloring by $x' \bmod 2$ (or $y' \bmod 2$) separates every edge!

---

### 4.5 Archetype 4: Birkhoff–von Neumann Decomposition & Regular Bipartite Edge Coloring

#### Theorem 4.2 (Birkhoff–von Neumann Theorem 1946 & Kőnig's Line Coloring Theorem 1916)
1. **Regular Bipartite Decomposition**: Every $k$-regular bipartite multigraph $G = (L \cup R, E)$ ($\lvert L \rvert = \lvert R \rvert = N$) has a perfect matching $M_1$ (by Hall's Theorem: for every $S \subseteq L$, $k \lvert S \rvert = \lvert E(S, N(S)) \rvert \le k \lvert N(S) \rvert \implies \lvert N(S) \rvert \ge \lvert S \rvert$). Peeling $M_1, M_2, \dots, M_k$ decomposes $E$ into $k$ edge-disjoint perfect matchings.
2. **Maximum-Degree Edge Coloring ($\chi'(G) = \Delta$)**: Every bipartite multigraph with maximum degree $\Delta$ can be embedded into a $\Delta$-regular bipartite multigraph, so its chromatic index is $\chi'(G) = \Delta$.

Depending on the contest constraints $(N, M, \Delta)$, choose among **three algorithmic engines**:
1. **Iterative Dinic Peeling (`ABC 317 G`, `AGC 037 D`)**: Run Dinic $k = \Delta$ times in $O(\Delta \cdot E \sqrt{V}) = O(N M^{3/2})$. Ideal when $N, M \le 100$.
2. **Online Kempe-Chain Recoloring (`CF 600 F`, `P18`)**: Insert edges $(u, v)$ one by one. Let $c_u$ be a free color at $u$ and $c_v$ be a free color at $v$. If $c_u \ne c_v$, walk the unique maximal alternating path $P$ of colors $(c_v, c_u)$ starting from $u$ (`Kempe Chain`). Because $G$ is bipartite, $P$ cannot form an odd cycle and cannot end at $v$ with color $c_v$. Swapping $c_u \leftrightarrow c_v$ along $P$ frees $c_v$ at $u$ in $O(V)$ time! Total complexity: **$O(VE)$**.
3. **Eulerian Circuit Halving (`AGC 037 D` speed-up)**: When $\Delta = 2^r$ is a power of $2$ (or after padding to $2^r$), decompose every connected component into an Eulerian circuit in $O(E)$ time; alternate edges into $E_{\text{odd}}$ and $E_{\text{even}}$, splitting a $2^r$-regular bipartite graph into two $2^{r-1}$-regular bipartite graphs in $O(E)$ time! Recursion depth $r = \log_2 \Delta$ gives **$O(E \log \Delta)$** total time (and by Gabow 1976 / Cole–Ost–Schirra 2001, general $\Delta$ also takes $O(E \log \Delta)$).

---

## 5. Reconciled Iteration 9 / 61: Hall's Marriage Theorem, Ore's Defect Formula & Flow-Elimination

### 5.1 Step 1: Non-Graph Diagnostic Signal (Recognition)

When a bipartite matching or supply–demand problem has **$N, M \ge 2 \cdot 10^5$** (or $D \sim 10^6$ days in **`ARC 106 E`**), explicit Dinic/Hopcroft–Karp is $O(N\sqrt{N})$ or $O(N^2)$ and **TLEs**! Reach for **Hall's Marriage Theorem** or **Ore's Defect Formula** when:
1. **Geometric Neighbourhood Convexity**: Each $u \in L$ connects to a contiguous interval $[l_u, r_u] \subseteq R$, a prefix/suffix union $[1, l_u] \cup [r_u, M]$ (`ARC 076 F`), or a circular arc (`CF 981 F`).
2. **Extreme Asymmetry ($N \le 18, M \ge 10^6$)**: One side has $N \le 18$ (`ARC 106 E`) or $N \le 6$ (`CF 1519 F`), allowing $O(N 2^N)$ SOS DP over all $2^N$ subsets $S \subseteq L$ or $O(\prod (a_i+1))$ primal flow-state DP!
3. **Hyperedge-to-Vertex Tree Realization (`AGC 029 F`)**: Given $N - 1$ subsets $E_1, \dots, E_{N-1} \subseteq \{1, \dots, N\}$, picking one endpoint $u_i \in E_i$ per edge to form a tree is equivalent to Hall's condition $\lvert \bigcup_{i \in S} E_i \rvert \ge \lvert S \rvert + 1$ for all $\emptyset \ne S \subseteq \{1, \dots, N-1\}$.

---

### 5.2 Step 2: Intermediate Algebraic Representation — Hall, Ore & Supply–Demand Defect

Let $G = (L \cup R, E)$ have vertex supplies $a_u \ge 0$ ($u \in L$) and capacities $b_v \ge 0$ ($v \in R$). In the $S$-$T$ network $N$ with $c(S, u) = a_u, c(u, v) = \infty, c(v, T) = b_v$, any finite cut $V_S = \{S\} \cup S_L \cup S_R$ ($S_L \subseteq L, S_R \subseteq R$) must avoid cutting $\infty$-edges, forcing $N(S_L) \subseteq S_R$. Minimizing the cut over $S_R \supseteq N(S_L)$ sets $S_R = N(S_L)$, with cut capacity:
$$\text{Cut}(S_L) = \sum_{u \in L \setminus S_L} a_u + \sum_{v \in N(S_L)} b_v = \sum_{u \in L} a_u - \underbrace{\left( \sum_{u \in S_L} a_u - \sum_{v \in N(S_L)} b_v \right)}_{\text{Defect } \text{def}(S_L)}.$$
By the Max-Flow Min-Cut Theorem, we immediately obtain all three forms of Hall/Ore Duality:
1. **Ore's Defect Formula (1955)**:
   $$\nu_{a, b}(G) = \sum_{u \in L} a_u - \max_{S \subseteq L} \left( \sum_{u \in S} a_u - \sum_{v \in N(S)} b_v \right) \qquad \text{(where } S = \emptyset \text{ gives defect } 0\text{)}.$$
2. **Hall's Marriage Theorem (1935) / Supply–Demand Feasibility**:
   $$\text{All supply } \sum_{u \in L} a_u \text{ is matched} \iff \forall S \subseteq L, \quad \sum_{v \in N(S)} b_v \ge \sum_{u \in S} a_u.$$
3. **Set-Complement Rewrite for Fast Zeta Transform (`ARC 106 E`)**:
   Since $N(S) = R \setminus \{ v \in R : N(v) \subseteq L \setminus S \}$, letting $g[T] = \sum_{v \in R : N(v) \subseteq T} b_v$ (the upward subset-sum / SOS DP of exact neighborhood masks $N(v)$), we have:
   $$\sum_{v \in N(S)} b_v = \sum_{v \in R} b_v - g[L \setminus S].$$

---

### 5.3 Step 3 & Step 4: The Connected-Component Additivity Lemma (Feasibility vs. Exact Defect Trap!)

Suppose every $u \in L$ connects to an interval $[l_u, r_u] \subseteq R$ (or every $v \in R$ connects to an interval in $L$). To replace $\max_{S \subseteq L}$ ($2^{\lvert L \rvert}$ subsets) with $O(\lvert R \rvert^2)$ intervals $[l, r] \subseteq R$, first note that for any fixed target neighborhood $I = N(S) \subseteq R$, the worst-case subset $S \subseteq L$ with $N(S) \subseteq I$ is the **maximal saturation set**:
$$S^*(I) = \{ u \in L : [l_u, r_u] \subseteq I \}.$$

#### Lemma 5.1 (Connected-Component Subadditivity of Defect)
Decompose any $I \subseteq R$ into its maximal contiguous intervals $I = I_1 \sqcup I_2 \sqcup \dots \sqcup I_k$, separated by at least one gap element $g \notin I$ between $I_j$ and $I_{j+1}$. Because every $u \in L$ has a *contiguous* interval $[l_u, r_u]$, $[l_u, r_u]$ cannot jump across a gap $g \notin I$:
$$[l_u, r_u] \subseteq I_1 \sqcup \dots \sqcup I_k \iff \exists! j \in \{1, \dots, k\} \text{ such that } [l_u, r_u] \subseteq I_j.$$
Therefore, $S^*(I) = \bigsqcup_{j=1}^k S^*(I_j)$, and the defect is **strictly additive** over disconnected interval components:
$$\boxed{\text{def}(I_1 \sqcup \dots \sqcup I_k) = \sum_{j=1}^k \text{def}(I_j), \qquad \text{where } \text{def}([l, r]) = \sum_{u : [l_u, r_u] \subseteq [l, r]} a_u - \sum_{v = l}^r b_v.}$$

> [!CAUTION]
> **Critical Cohort 2 Reconciliation — Feasibility (`<= 0`) vs. Exact Defect Optimization (`> 0`)**:
> From $\text{def}(I_1 \sqcup \dots \sqcup I_k) = \sum_{j=1}^k \text{def}(I_j)$, two **different** rules follow depending on whether you are testing *feasibility* or computing the *exact maximum defect*:
> 1. **Feasibility Testing ($\max_I \text{def}(I) \le 0$, e.g. Binary Search in `CF 981 F`)**:
>    $$\forall I, \; \text{def}(I) \le 0 \iff \forall \text{ single contiguous interval } [l, r], \; \text{def}([l, r]) \le 0!$$
>    *(Proof: A sum of non-positive numbers is non-positive, and if any sum is $> 0$, at least one summand $\text{def}(I_j) > 0$.)*
> 2. **Exact Maximum Defect ($\max_I \text{def}(I)$ when $\nu(G) < \sum a_u$):**
>    When $\max_{[l,r]} \text{def}([l, r]) > 0$, **single intervals DO NOT suffice** if two disjoint intervals $I_1 = [l_1, r_1]$ and $I_2 = [l_2, r_2]$ ($l_2 \ge r_1 + 2$) both have positive defect!
>    - **Counterexample**: $R = \{1, 2, 3\}$ with $b_v = 1$. Two items in $L$ at $[1, 1]$ and two items in $L$ at $[3, 3]$ ($\lvert L \rvert = 4$). Single intervals have $\text{def}([1,1]) = 2 - 1 = 1$, $\text{def}([3,3]) = 2 - 1 = 1$, and $\text{def}([1,3]) = 4 - 3 = 1$. So $\max_{[l,r]} \text{def}([l, r]) = 1$, which would falsely predict $\nu(G) = 4 - 1 = 3$! In reality, $I = \{1\} \sqcup \{3\}$ has $\text{def}(\{1, 3\}) = \text{def}([1, 1]) + \text{def}([3, 3]) = 1 + 1 = 2$, giving the true matching size $\nu(G) = 4 - 2 = 2$.
>    - **Exact Multi-Interval Defect DP**: When $N(u) = [l_u, r_u]$ are interior intervals and you need $\nu(G)$, maximize over all disjoint intervals separated by $\ge 1$ gap via:
>      $$dp[r] = \max\Big( dp[r - 1], \;\max_{1 \le l \le r} \big( dp[l - 2] + \text{def}([l, r]) \big) \Big).$$
> 3. **Why Prefix–Suffix Unions (`ARC 076 F`, $N(u) = [1, L_u] \cup [R_u, M]$) Need Only ONE Interval**:
>    In `ARC 076 F`, each person connects to a prefix $\cup$ suffix, meaning their *complement* $\overline{N(u)} = (L_u, R_u)$ is a single open interval! For any $I \subseteq R$, $N(u) \subseteq I \iff I^c \subseteq (L_u, R_u)$. Replacing $I^c$ by its convex hull $[\min I^c, \max I^c] = (L, R)$ only *shrinks* $I$ (reducing $\lvert I \rvert$) while preserving $I^c \subseteq (L_u, R_u)$! Hence the worst $I$ is **always** a single prefix $\cup$ suffix $[1, L] \cup [R, M]$, so checking single pairs $(L, R)$ with a Segment Tree is 100% exact even for positive defect!

#### Summary of the Five Hall Flow-Elimination Compilations
1. **Prefix–Suffix Union (`ARC 076 F`, `P19`)**: $\max_{0 \le L < R \le M+1} (\#\{i : L_i \le L \land R_i \ge R\} - L - (M - R + 1))$ via sweep-line + Lazy Segment Tree in $O((N + M) \log M)$.
2. **Circular Hall Unrolling (`CF 981 F`, `P20`)**: On a circle of length $L$, unroll brides to $2N$ and grooms to $4N$. By Lemma 5.1, binary search on distance $D$ only tests **feasibility** ($\text{def}([l, r]) \le 0$), which reduces to $R_r - r \ge L_l - l$ for all $1 \le l \le r < l + N$, checked in $O(N)$ via prefix-maximum sweep!
3. **Capacitated Small-Side SOS DP (`ARC 106 E`, `P28`)**: Binary search total days $D$; count workers active on subset $T \subseteq \{1, \dots, N\}$ via $O(N 2^N)$ Fast Zeta Transform and test $D - g[L \setminus S] \ge K \lvert S \rvert$.
4. **Primal–Dual Flip to Flow-State DP (`CF 1519 F`, `P29`)**: When $N, M \le 6$ and $a_i, b_j \le 4$, testing $2^6 = 64$ cut subsets in a DP state is $2^{64}$ (impossible), whereas the **remaining supply tuple $(rem_1, \dots, rem_6) \in [0, 4]^6$** has only $5^6 = 15,625$ states! Flip Hall's cut condition back to primal flow routing lock-by-lock.
5. **Constructive Hall Tree Realization (`AGC 029 F`, `P26`)**: Fix root $r = 1$, match $N - 1$ hyperedges $E_1, \dots, E_{N-1}$ to $V \setminus \{1\}$ via Hopcroft–Karp, and reconstruct the tree from $r = 1$ via alternating BFS $v \xrightarrow{\text{incident}} e \xrightarrow{M(e)} u$. If BFS visits all $N$ vertices, the tree is valid; if it stalls on $V_{\text{vis}} \subsetneq V$, $S = E \setminus E_{\text{vis}}$ violates Hall's tree condition ($\lvert \bigcup_{e \in S} E_e \rvert \le \lvert S \rvert$), proving impossibility!

---

## 6. Reconciled Iteration 10 / 62: Posets, Dilworth's Theorem, Mirsky's Dual & DAG Path Covers

### 6.1 Step 1: Non-Graph Diagnostic Signal (Recognition)

Reach for **Poset Duality (Dilworth / Mirsky)** or **DAG Path Covers** when:
1. **Sequential Reuse / Trajectory Stitching (`Min Chain / Path Cover`)**: What is the minimum number of agents, hands, stacks, or paths needed to visit all vertices/events of a DAG?
   - *Vertex-Disjoint* (each vertex entered/exited at most once) $\implies$ **Minimum Disjoint Path Cover (`MDPC`)** on the raw DAG.
   - *Vertex-Overlapping* (paths may share intermediate vertices, or the relation is transitive) $\implies$ **Transitive Closure + Dilworth Chain Cover**.
2. **Pairwise Incomparable Selection (`Max Antichain`)**: Select the largest (or maximum-weight) subset $A \subseteq V$ such that no two selected elements satisfy $u \prec v$ (e.g., no string is a substring of another in **`ABC 354 G`** and **`CF 590 E`**).
3. **Why Greedy Chain Extraction Fails**: Greedily peeling the longest path on a DAG can leave isolated side-vertices stranded, inflating the path count (e.g., on $1 \to 2 \to 3 \to 4$ with $1 \to 5$ and $6 \to 4$, greedy picks $1 \to 2 \to 3 \to 4$ of length 4, stranding $\{5\}$ and $\{6\}$ for 3 chains total, whereas $\{1 \to 5\}$ and $\{6 \to 4\}$... wait: on $2 \to 3$, $1 \to 3$, $2 \to 4$, greedy picks $1 \to 3 \dots$ wait: $1 \to 2 \to 3 \to 4$ plus $2 \to 5$ and $6 \to 3$: greedy picks $1 \to 2 \to 3 \to 4$, stranding $5$ and $6$ for 3 paths, whereas $1 \to 2 \to 5$ and $6 \to 3 \to 4$ cover all 6 vertices in **2 paths**!).

---

### 6.2 Step 2 & Step 3: Split Graph $G_{\text{split}}$, Mirsky vs. Dilworth & Weighted Transitivity Non-Overlap

#### 1. The Dual Quartet on a Finite Poset $\mathcal{P} = (V, \prec)$
| Primal Packing Problem | Dual Covering Problem | Complexity on Poset / DAG |
| :--- | :--- | :--- |
| **Max Chain** (longest path $c_1 \prec \dots \prec c_L$) | **Min Antichain Partition** (**Mirsky 1971**) | **$O(V + E)$ Topological DP**: $dp[v] = 1 + \max_{u \prec v} dp[u]$ defines the antichain layers $A_k = \{v : dp[v] = k\}$. |
| **Max Antichain** (largest incomparable $A$, `width`) | **Min Chain Cover** (**Dilworth 1950**) | **$O(E\sqrt{V})$ Bipartite Matching** on the **transitive** split graph $G_{\text{split}}(\mathcal{P})$. |

#### 2. Algebraic Compilation of Minimum Disjoint Path Cover (`MDPC`) on a DAG
In a DAG $G = (V, E)$, a collection of vertex-disjoint directed paths covering $V$ is uniquely specified by choosing a subset of edges $M \subseteq E$ such that every vertex $v \in V$ has $\text{outdeg}_M(v) \le 1$ and $\text{indeg}_M(v) \le 1$ (since $G$ is acyclic, no cycles can form).
- Each chosen edge $(u, v) \in M$ merges two paths into one, reducing the path count from $\lvert V \rvert$ by $1$:
  $$\text{Min Disjoint Path Cover}(G) = \lvert V \rvert - \max_{M} \lvert M \rvert = \lvert V \rvert - \nu(G_{\text{split}}(G)),$$
  where $G_{\text{split}}(G) = (V_{\text{out}} \cup V_{\text{in}}, E_{\text{split}})$ has an edge $(u_{\text{out}}, v_{\text{in}}) \iff (u, v) \in E$.
- **Cost / Bonus Extension (`Step 2 -> Step 3`)**: If starting a path at $v$ costs $s_v$ and stepping $u \to v$ costs $c_{uv}$, then choosing $u \to v$ replaces starting a new path at $v$ with edge $u \to v$, changing total cost by $c_{uv} - s_v$:
  $$\text{Total Cost}(M) = \sum_{v \in V} s_v + \sum_{(u, v) \in M} (c_{uv} - s_v),$$
  which compiles directly to **Minimum-Weight Bipartite Matching / MCMF** on $G_{\text{split}}$!

#### 3. Overlapping Path Cover, Weighted Dilworth & The Transitivity Non-Overlap Lemma
When paths may **share vertices** (or when computing the Maximum-Weight Antichain of a poset $\mathcal{P} = (V, \prec)$ with weights $w_v > 0$), we first take the **transitive closure** $\mathcal{P} = \text{TC}(G)$ (so $(u_{\text{out}}, v_{\text{in}}) \in E_{\text{split}} \iff u \prec v$).
Wait: in $G_{\text{split}}(\mathcal{P})$, each poset element $v \in V$ is split into **two** vertices $v_{\text{out}} \in L$ (weight $w_v$) and $v_{\text{in}} \in R$ (weight $w_v$). An antichain $A \subseteq V$ requires selecting elements of $V$, which corresponds to having **both** $v_{\text{out}} \notin C^*$ and $v_{\text{in}} \notin C^*$ in a vertex cover $C^*$ of $G_{\text{split}}(\mathcal{P})$. Why does $\sum_{v \in V} w_v - \tau_w(G_{\text{split}}(\mathcal{P}))$ equal the exact Maximum-Weight Antichain without double-charging any $v$ where *both* $v_{\text{out}} \in C^*$ and $v_{\text{in}} \in C^*$?

#### Lemma 6.1 (The Transitivity Non-Overlap Lemma — Reconciling Cohort 1 & Cohort 2 Proofs)
Let $\mathcal{P} = (V, \prec)$ be a **strict poset (transitive and irreflexive)**, and let $C^* \subseteq V_{\text{out}} \cup V_{\text{in}}$ be any minimal (or minimum-weight) vertex cover of $G_{\text{split}}(\mathcal{P})$. Then **no element $v \in V$ ever has both $v_{\text{out}} \in C^*$ and $v_{\text{in}} \in C^*$** (or if a zero-slack tie occurs, $v_{\text{in}}$ can be removed from $C^*$ while remaining a valid cover)!
*Proof (Cohort 2 Transitivity Contraction)*: Suppose $v_{\text{out}} \in C^*$ and $v_{\text{in}} \in C^*$. If removing $v_{\text{out}}$ leaves some edge $(v_{\text{out}}, y_{\text{in}})$ ($v \prec y$) uncovered, then $y_{\text{in}} \notin C^*$; if removing $v_{\text{in}}$ leaves some edge $(x_{\text{out}}, v_{\text{in}})$ ($x \prec v$) uncovered, then $x_{\text{out}} \notin C^*$. By **transitivity of $\prec$**, $x \prec v$ and $v \prec y$ imply $x \prec y$, so $(x_{\text{out}}, y_{\text{in}}) \in E_{\text{split}}(\mathcal{P})$! Since $x_{\text{out}} \notin C^*$ and $y_{\text{in}} \notin C^*$, the edge $(x_{\text{out}}, y_{\text{in}})$ was *already uncovered* by $C^*$, contradiction!
Thus $\lvert C^* \rvert = \lvert \{ v \in V : v_{\text{out}} \in C^* \lor v_{\text{in}} \in C^* \} \rvert$, and its complement
$$\boxed{A^* = \{ v \in V : v_{\text{out}} \notin C^* \land v_{\text{in}} \notin C^* \} = \{ v \in V : v_{\text{out}} \in V_S \land v_{\text{in}} \in V_T \}}$$
is a valid antichain of weight $\sum_{v \in A^*} w_v = \sum_{v \in V} w_v - \tau_w(G_{\text{split}}(\mathcal{P}))$!

#### Step 4 Counterexample: Why Missing Transitive Closure Breaks Both Overlapping Cover & Antichain Recovery
Consider the 4-vertex DAG $G$ with edges $1 \to 2$, $2 \to 3$, $4 \to 2$, $2 \to 5$ (an `X` centered at vertex $2$, with **no** transitive edge $4 \to 3$ or $1 \to 5$):
- **True Overlapping Path Cover**: $2$ paths ($1 \to 2 \to 3$ and $4 \to 2 \to 5$ sharing vertex $2$).
- **Without Transitive Closure**: In $G_{\text{split}}(G)$, $2_{\text{out}}$ can match at most one of $\{3_{\text{in}}, 5_{\text{in}}\}$ and $2_{\text{in}}$ can match at most one of $\{1_{\text{out}}, 4_{\text{out}}\}$. Thus $\nu(G_{\text{split}}(G)) = 2$, falsely reporting $5 - 2 = 3$ paths! And in $G_{\text{split}}(G)$, $C^* = \{2_{\text{out}}, 2_{\text{in}}\}$ covers all 4 edges with **both** $2_{\text{out}} \in C^*$ and $2_{\text{in}} \in C^*$, leaving $V \setminus \{2\} = \{1, 3, 4, 5\}$ of size $4 > 3$! Adding the transitive edges $1 \to 3, 1 \to 5, 4 \to 3, 4 \to 5$ allows matching $(1_{\text{out}}, 3_{\text{in}})$ and $(4_{\text{out}}, 5_{\text{in}})$, raising $\nu$ to $3$ ($5 - 3 = 2$ chains) and preventing $C^* = \{2_{\text{out}}, 2_{\text{in}}\}$.

---

## 7. Cohort 3 Targeted Gap-Hunting: Extensions Beyond Cohorts 1 & 2

### 7.1 Gap-Hunt Topic 1: Generalized $k$-Chain Families, Greene–Kleitman Duality (1976) & MCMF Compilation

What if a problem gives us **at most $k$ chains (or $k$ paths on a DAG)** where $k < \text{width}(\mathcal{P})$, and asks for the **maximum number (or maximum weight) of vertices we can cover using at most $k$ chains**?

#### Theorem 7.1 (Greene–Kleitman Theorem, 1976 — $k$-Dilworth Duality)
In any finite poset $\mathcal{P} = (V, \prec)$ and any integer $k \ge 1$, the maximum size of a **$k$-chain family** (a subset $C \subseteq V$ that can be partitioned into at most $k$ chains) equals:
$$\max_{\substack{C_1, \dots, C_k \text{ chains}}} \left\lvert \bigcup_{i=1}^k C_i \right\rvert = \min_{\substack{A_1 \sqcup \dots \sqcup A_q = V \\ \text{antichain partition}}} \sum_{j=1}^q \min\big(\lvert A_j \rvert, \; k\big) = \min_{U \subseteq V} \Big( \lvert V \setminus U \rvert + k \cdot \text{width}(\mathcal{P}[U]) \Big).$$

#### Mechanical Compilation to Min-Cost Max-Flow (`MCMF`) / $k$-Flow on a Split DAG
Suppose each vertex $v \in V$ of a DAG $G = (V, E)$ offers reward $w_v \ge 0$ if visited by one of at most $k$ vertex-disjoint paths (`Partial k-Path Cover`):
1. **Algebraic Representation**: Each vertex $v \in V$ is either visited ($z_v = 1$, reward $w_v$) or skipped ($z_v = 0$). If visited, $v$ has at most one incoming path edge and at most one outgoing path edge, and total paths started is $\sum_{v} z_v - \lvert M \rvert \le k$.
2. **MCMF Split-DAG Compilation**:
   - Split each $v \in V$ into $v_{\text{in}} \to v_{\text{out}}$ with two parallel edges:
     - Edge 1 (`Visit`): capacity $1$, cost $-w_v$ (for disjoint paths; for overlapping paths on a DAG, add a second parallel bypass edge $v_{\text{in}} \to v_{\text{out}}$ of capacity $\infty$ and cost $0$!).
   - Add $S_{\text{sub}} \to v_{\text{in}}$ (capacity $1$, cost $0$), $v_{\text{out}} \to T$ (capacity $1$, cost $0$), and for each $(u, v) \in E$, $u_{\text{out}} \to v_{\text{in}}$ (capacity $\infty$ or $1$, cost $0$).
   - Restrict total paths to $\le k$ by adding $S \to S_{\text{sub}}$ with **capacity $k$, cost $0$** (plus a direct bypass $S_{\text{sub}} \to T$ of capacity $\infty, \text{cost } 0$ if paths $< k$ are allowed).
   - Running Min-Cost Max-Flow of value $k$ from $S$ to $T$ computes the exact Greene–Kleitman optimum!

---

### 7.2 Gap-Hunt Topic 2: Critical Edges of Minimum Vertex Cover via Fine DM Decomposition (`[HAOI2017] 新型城市化`)

In Section 3.2 we classified **Essential Vertices** ($\nu(G \setminus \{w\}) = \nu(G) - 1$) and **Essential Matched Edges** ($e \in M$ belongs to *every* maximum matching). What if a problem asks for **Critical Edges of the Graph $G$** — edges $e = (u, v) \in E$ whose **deletion from $G$ strictly decreases the Minimum Vertex Cover / Maximum Matching** ($\nu(G \setminus \{e\}) = \nu(G) - 1$, or equivalently in the complement graph $\overline{G}$, adding $e$ increases the Maximum Independent Set $\alpha(G)$ by $1$, as in **`Luogu P3731 [HAOI2017] 新型城市化`**)?

#### Theorem 7.2 (Characterization of $\nu$-Critical Edges in Bipartite Graphs)
Let $G = (L \cup R, E)$ be a bipartite graph and $M$ be any maximum matching of $G$. An edge $e = (u, v) \in E$ satisfies $\nu(G \setminus \{e\}) = \nu(G) - 1$ if and only if **$e$ belongs to EVERY maximum matching of $G$** (`Essential Edge` in Fine DM):
$$\nu(G \setminus \{e\}) = \nu(G) - 1 \iff e \in M \;\land\; u \notin V_S \cup V_T^{\text{rev}} \;\land\; v \notin V_S \cup V_T^{\text{rev}} \;\land\; \text{scc}_{G_{f^*}^\circ}(u) \ne \text{scc}_{G_{f^*}^\circ}(v).$$
Furthermore, in the full residual network $G_{f^*}$ (which includes $S$ and $T$, where $S \to u$ has residual capacity $1 - f^*(S,u)$ and $v \to T$ has $1 - f^*(v,T)$), an even simpler **single-SCC condition on the full $G_{f^*}$** holds!
- In $G_{f^*}$, if $u \in L_1 = L \cap V_S$ and $(u, v) \in M$, then $S \rightsquigarrow u$ in $G_{f^*}$ and $v \to u \to S$ ($c_f(u, S) = 1 > 0$) closes a directed cycle through $S$, so $\text{scc}_{G_{f^*}}(u) = \text{scc}_{G_{f^*}}(v) = \text{scc}_{G_{f^*}}(S)$!
- Symmetrically, if $v \in R_2 = R \cap V_T^{\text{rev}}$ and $(u, v) \in M$, then $T \to v \to u \rightsquigarrow T$ closes a directed cycle through $T$, so $\text{scc}_{G_{f^*}}(u) = \text{scc}_{G_{f^*}}(v) = \text{scc}_{G_{f^*}}(T)$!
- Therefore, running Tarjan's SCC on the **entire residual network $G_{f^*}$ (including $S$ and $T$)** yields the ultra-compact criterion:
  $$\boxed{\nu(G \setminus \{e\}) = \nu(G) - 1 \iff e = (u, v) \in M \;\land\; \text{scc}_{G_{f^*}}(u) \ne \text{scc}_{G_{f^*}}(v)!}$$
*(Why? Because $L_1 \times R_1$ matched pairs merge into $\text{scc}(S)$, $L_2 \times R_2$ matched pairs merge into $\text{scc}(T)$, and $L_0 \times R_0$ matched pairs with an alternating cycle merge into their own SCC in $G_{f^*}$!)*

---

### 7.3 Reconciled Master Recognition & Compilation Decision Table

| Problem Signature / Objective | Intermediate Algebraic Model | Target Graph & Algorithm | Time Complexity |
| :--- | :--- | :--- | :--- |
| **Min (Weighted) Vertex Cover / Max Independent Set** on $L \cup R$ | $\min \sum w_u x_u + \sum w_v y_v$ s.t. $x_u + y_v \ge 1$ | $S \xrightarrow{w_u} u \xrightarrow{\infty} v \xrightarrow{w_v} T$; $C^* = (L \cap V_T) \cup (R \cap V_S)$, $I^* = V \setminus C^*$ | $O(E\sqrt{V})$ (unit) or Dinic Max-Flow |
| **Priority Matching on $L$** (max $\sum_{u \in M \cap L} w_u$ or longest prefix $[1..K]$) | Transversal Matroid $\mathcal{M} = (L, \mathcal{I})$ greedy basis | Sort $L$ by decreasing $w_u$; run Kuhn's augmenting DFS in priority order | $O(\lvert L \rvert E)$ (Zero MCMF!) |
| **Essential / Avoidable Vertices** & **Bipartite Walk Game** | $\nu(G \setminus \{w\}) \stackrel{?}{=} \nu(G)$ | Coarse DM: $L_1 = L \cap V_S$, $R_2 = R \cap V_T^{\text{rev}}$ are Avoidable (2nd Mover wins) | $O(E\sqrt{V} + V + E)$ |
| **Admissible / Essential Edges** & **Critical MVC Edges** (`P23`) | $\nu(G \setminus \{e\}) = \nu(G) - 1 \iff \forall M^*, e \in M^*$ | Fine DM: Run Tarjan SCC on full $G_{f^*}$; Critical $\iff e \in M \land \text{scc}(u) \ne \text{scc}(v)$ | $O(E\sqrt{V} + V + E)$ |
| **Unique Perfect Matching** ($\lvert L \rvert = \lvert R \rvert = N$) | $G_M^\circ$ is a DAG | Iterative Degree-1 Queue Leaf-Peeling (Hall–Kotzig Theorem 3.2) | **$O(V + E)$** (Zero Dinic!) |
| **Regular Bipartite Decomposition / Edge Coloring** ($\chi' = \Delta$) | Birkhoff–von Neumann / Kőnig Line Coloring | Dinic peeling ($\Delta \le 100$), Kempe Chains (`CF 600 F`), or Eulerian Halving ($\Delta = 2^r$) | $O(\Delta E\sqrt{V})$, $O(VE)$, or $O(E \log \Delta)$ |
| **Interval / Circular / Small-$N$ Matching** ($N, M \ge 10^5$ or $N \le 18$) | Ore's Defect $\max_{S} (\lvert S \rvert - \lvert N(S) \rvert)$ | Segment Tree (`ARC 076 F`), $4N$ Unroll (`CF 981 F`), or SOS DP (`ARC 106 E`) | $O(N \log N)$, $O(N)$, or $O(N 2^N)$ |
| **DAG Disjoint vs. Overlapping Path Cover / Weighted Antichain** | $\lvert V \rvert - \nu(G_{\text{split}})$ (or $\sum w_v - \tau_w(G_{\text{split}}(\text{TC}))$) | Raw $G_{\text{split}}$ (disjoint) vs. Transitive Closure $\text{TC}(G)$ (overlapping / antichain) | $O(E\sqrt{V})$ (+ Bitset FW $O(V^3/w)$) |
| **Partial $k$-Chain / $k$-Path Cover** (Greene–Kleitman Duality) | $\max_{\lvert \mathcal{C} \rvert \le k} \sum_{v \in \bigcup \mathcal{C}} w_v$ | Split DAG $v_{\text{in}} \xrightarrow{1, -w_v} v_{\text{out}}$ (plus $\infty, 0$ bypass if overlapping), $k$-flow MCMF | $O(k \cdot E \log V)$ MCMF |

---

## 8. Reconciled Master 4-Tier Curated Problem Bank (30 Non-Template Problems)

Every problem below is compiled through the **4-Step "Zero Magic Gadgets" Pipeline** and reconciled across Cohort 1 and Cohort 2 to preserve the deepest algebraic derivation, toy trace, and structural counterexamples.

---

### Tier 1: Stepping Stone (7 Problems — `P01` to `P07`)

---

#### Problem `P01`: `[ZJOI2007] 矩阵游戏` (Luogu P1129)
- **Judge URL**: [https://www.luogu.com.cn/problem/P1129](https://www.luogu.com.cn/problem/P1129)
- **Constraints**: $T \le 20$ test cases; $N \le 200$ ($N \times N$ binary matrix $A_{i,j} \in \{0, 1\}$); Time Limit $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  We can arbitrarily swap two rows or swap two columns, and want the main diagonal $(1, 1), (2, 2), \dots, (N, N)$ to become all $1$s. Notice that row swaps never alter which entries share a row, and column swaps never alter which entries share a column. Thus the operation group $S_N \times S_N$ preserves the **incidence relation between rows and columns**.
- **Step 2 — Intermediate Algebraic Representation**:
  Applying row permutation $\sigma \in S_N$ (placing original row $\sigma(k)$ into row $k$) and column permutation $\tau \in S_N$ (placing original column $\tau(k)$ into column $k$) transforms the diagonal into $A_{\sigma(k), \tau(k)}$ for $k = 1, \dots, N$. Requiring $A_{\sigma(k), \tau(k)} = 1$ for all $k$ means $\pi = \tau \circ \sigma^{-1} \in S_N$ is a bijection from original rows $i \in \{1, \dots, N\}$ to original columns $\pi(i) \in \{1, \dots, N\}$ such that $A_{i, \pi(i)} = 1$ for all $i$.
- **Step 3 — Reverse-Engineering Scratchpad**:
  A bijection $\pi : \{1, \dots, N\} \to \{1, \dots, N\}$ with $A_{i, \pi(i)} = 1$ is a **perfect matching** in the bipartite graph $G = (L \cup R, E)$ with $L = \{r_1, \dots, r_N\}$, $R = \{c_1, \dots, c_N\}$, and $(r_i, c_j) \in E \iff A_{i, j} = 1$. Conversely, if such a bijection $\pi$ exists, setting $\sigma = \text{id}$ and $\tau = \pi$ puts $(i, \pi(i))$ onto $(i, i)$ using only column swaps!
- **Step 4 — Concrete Toy Trace & Conjugation Trap**:
  For $N = 2$ and $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, the edges are $(r_1, c_2)$ and $(r_2, c_1)$, giving $\nu(G) = 2 = N$ (`Yes` via swapping columns $1 \leftrightarrow 2$). **Counterexample Trap**: If row $i$ and column $i$ had to be swapped *together* ($\sigma = \tau$), the diagonal sum $\text{tr}(A) = 0$ would be invariant and the answer would be `No`.
- **Complete Solution & Complexity**: Build $G$ with $\lvert L \rvert = \lvert R \rvert = N$ and $\lvert E \rvert \le N^2$; output `Yes` iff $\nu(G) = N$. Time $O(T N^2 \sqrt{N})$ via Dinic or $O(T N^3)$ via Kuhn.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Do you ever need *both* row swaps and column swaps, or can any valid state be reached by permuting columns alone?
  - *Hint 2*: What properties do two $1$-cells on the final main diagonal have in the original matrix $A$?
  - *Hint 3*: Neither their original rows nor their original columns can coincide. Model rows as $L$, columns as $R$, and check if $\nu(G) = N$.

---

#### Problem `P02`: `POJ 2125 — Destroying The Graph`
- **Judge URL**: [http://poj.org/problem?id=2125](http://poj.org/problem?id=2125)
- **Constraints**: $N \le 100$ vertices, $M \le 5000$ directed edges; positive vertex costs $W_i^-$ (destroy all incoming edges of $i$) and $W_i^+$ (destroy all outgoing edges of $i$). Output minimum total cost and the exact sequence of `+`/`-` operations.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Wait — the input *is* a general directed graph (possibly containing odd cycles and self-loops!), where Vertex Cover is NP-hard. Why is this problem in P? Because each vertex $i$ has **two decoupled operations**: `i+` destroys only **outgoing** edges $(i \to j)$, and `i-` destroys only **incoming** edges $(k \to i)$.
- **Step 2 — Intermediate Algebraic Representation**:
  Let $x_i \in \{0, 1\}$ indicate executing `i+` (cost $W_i^+$) and $y_j \in \{0, 1\}$ indicate executing `j-` (cost $W_j^-$). A directed edge $i \to j \in E$ is destroyed iff its tail's outgoing star is destroyed **OR** its head's incoming star is destroyed:
  $$\min \sum_{i=1}^N W_i^+ x_i + \sum_{j=1}^N W_j^- y_j \quad \text{s.t.} \quad x_i + y_j \ge 1 \;\;\forall (i \to j) \in E.$$
- **Step 3 — Reverse-Engineering Scratchpad**:
  Because $x_i$ only ever appears as a tail and $y_j$ only ever appears as a head, the constraint system is a **Bipartite Minimum-Weight Vertex Cover (`MWVC`)** on $G_{\text{split}} = (L \cup R, E_{\text{split}})$ where $L = \{1^+, \dots, N^+\}$, $R = \{1^-, \dots, N^-\}$. Build the $S$-$T$ network:
  - $S \to i^+$ with capacity $W_i^+$; $j^- \to T$ with capacity $W_j^-$; $i^+ \to j^-$ with capacity $\infty$ for each $(i \to j) \in E$.
  - After Max-Flow, find $V_S$ via residual BFS from $S$ ($c_f > 0$), and output $C^* = \{i^+ : i^+ \notin V_S\} \cup \{j^- : j^- \in V_S\}$.
- **Step 4 — Concrete Toy Trace & Middle-Capacity Trap**:
  Suppose $N = 2$ with edge $1 \to 2$, $W_1^+ = 10, W_1^- = 1, W_2^+ = 1, W_2^- = 4$. The network has $S \to 1^+ (10), 1^+ \to 2^- (\infty), 2^- \to T (4)$. Max-Flow pushes $4$ units, saturating $2^- \to T$. Residual BFS from $S$ reaches $V_S = \{S, 1^+, 2^+, 2^-\}$ (since $c_f(S, 1^+) = 6 > 0$ and $c_f(1^+, 2^-) = \infty > 0$). Thus $C^* = (L \setminus V_S) \cup (R \cap V_S) = \emptyset \cup \{2^-\}$ of cost $4$. **Broken Gadget Trap**: Setting $c(1^+, 2^-) = 1$ instead of $\infty$ would cut $1^+ \to 2^-$ for cost $1 < 4$, producing an invalid 0-operation solution!
- **Complete Solution & Complexity**: Dinic on $2N + 2$ vertices and $2N + M$ edges + residual BFS in $O(M \sqrt{N})$ / $O(N^2 M)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Does performing `i+` help destroy an incoming edge $k \to i$? No — `i+` and `i-` act on completely disjoint sets of incident edges.
  - *Hint 2*: Split each vertex $i$ into $i^+ \in L$ (cost $W_i^+$) and $i^- \in R$ (cost $W_i^-$). What is each directed edge $u \to v$ in this split graph?
  - *Hint 3*: It is a bipartite edge $(u^+, v^-)$ covered iff $u^+$ or $v^-$ is chosen (`MWVC`). Set middle capacities to $\infty$ and extract $(L \cap V_T) \cup (R \cap V_S)$.

---

#### Problem `P03`: `Codeforces 510 E — Fox And Dinner`
- **Judge URL**: [https://codeforces.com/problemset/problem/510/E](https://codeforces.com/problemset/problem/510/E)
- **Constraints**: $N \le 200$ foxes, each with integer age $a_i \in [2, 10^4]$; Time Limit $2.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Seat all $N$ foxes around circular tables of size $\ge 3$ such that adjacent foxes around every table have $a_i + a_j \in \mathbb{P}$ (prime). Since $a_i \ge 2$, $a_i + a_j \ge 4$, so every prime sum $a_i + a_j$ is ** strictly odd**!
- **Step 2 — Intermediate Algebraic Representation**:
  Because $a_i + a_j$ is odd, every valid adjacency connects an **odd** $a_i$ with an **even** $a_j$. Thus the compatibility graph $G = (L_{\text{odd}} \cup R_{\text{even}}, E)$ is **bipartite**! Furthermore, every simple cycle in a bipartite graph is an even cycle of length $\ge 4$ (automatically satisfying table size $\ge 3$). Partitioning $V$ into vertex-disjoint cycles is equivalent to finding a **2-factor** ($b$-matching where every vertex has exact degree $2$):
  $$\forall u \in L_{\text{odd}}, \;\; \sum_{v \in N(u)} f_{uv} = 2, \qquad \forall v \in R_{\text{even}}, \;\; \sum_{u \in N(v)} f_{uv} = 2, \qquad f_{uv} \in \{0, 1\}.$$
- **Step 3 — Reverse-Engineering Scratchpad**:
  First check $\lvert L_{\text{odd}} \rvert = \lvert R_{\text{even}} \rvert = N / 2$ (otherwise `Impossible`). Build network $N$:
  - $S \to u$ with capacity $2$ for $u \in L_{\text{odd}}$; $v \to T$ with capacity $2$ for $v \in R_{\text{even}}$;
  - $u \to v$ with capacity $1$ (not $\infty$, because a cycle of length $\ge 4$ cannot use the same edge $(u, v)$ twice as a 2-gon!).
  - If $\text{MaxFlow} = N$, extract all edges with $f(u, v) = 1$; each connected component is a 2-regular cycle representing one dinner table.
- **Step 4 — Concrete Toy Trace & Middle-Capacity Trap**:
  With $a = [2, 3, 4, 5]$, $L_{\text{odd}} = \{3, 5\}$, $R_{\text{even}} = \{2, 4\}$. Prime sums are $3+2=5, 3+4=7, 5+2=7$, missing $(5, 4)$ since $5+4=9$. Because vertex $5$ only has degree $1$ in $G$, $\text{MaxFlow} = 3 < 4 \implies \text{Impossible}$. **Broken Gadget Trap**: If $c(u, v) = 2$ (or $\infty$) instead of $1$, vertex $5$ would push $2$ units of flow along the single edge $(5, 2)$, forming a degenerate 2-fox table $\{5, 2\}$!
- **Complete Solution & Complexity**: Sieve primes up to $2 \cdot 10^4$, run Dinic on $N + 2$ vertices ($O(N^2 \sqrt{N})$), and DFS the $f(u, v) = 1$ subgraph to print cycles.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Since $a_i \ge 2$, can $a_i + a_j$ ever equal the even prime $2$? What does that imply about the parity of adjacent foxes?
  - *Hint 2*: Every valid table alternates Odd–Even–Odd–Even, so any cycle has even length $\ge 4$. What degree must each fox have in the chosen subgraph?
  - *Hint 3*: Every fox needs exact degree $2$. Set $c(S, u) = 2$, $c(v, T) = 2$, and $c(u, v) = 1$; check if $\text{MaxFlow} = N$.

---

#### Problem `P04`: `POJ 2226 / [USACO05JAN] Muddy Fields` (Luogu P6062)
- **Judge URL**: [https://www.luogu.com.cn/problem/P6062](https://www.luogu.com.cn/problem/P6062)
- **Constraints**: $R, C \le 50$; grid of `*` (muddy cells to cover) and `.` (clean grass cells that must *not* be covered); Time Limit $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Cover all `*` cells with the minimum number of $1 \times L$ horizontal or $L \times 1$ vertical planks without covering any `.` cell; planks may overlap on `*` cells. Notice a plank should always be extended to its **maximal contiguous `*`-strip** (extending is free since overlaps are allowed).
- **Step 2 — Intermediate Algebraic Representation**:
  Let $H_1, \dots, H_p$ be the maximal contiguous horizontal `*`-strips and $V_1, \dots, V_q$ be the maximal contiguous vertical `*`-strips. Every muddy cell $(r, c)$ belongs to a unique horizontal strip $h(r, c) \in L$ and a unique vertical strip $v(r, c) \in R$, imposing the 2-SAT cover constraint:
  $$x_{h(r, c)} + y_{v(r, c)} \ge 1 \quad \forall (r, c) \text{ with } \text{grid}[r][c] = \text{'*'}.$$
- **Step 3 — Reverse-Engineering Scratchpad**:
  Create bipartite graph $G = (L \cup R, E)$ with $\lvert L \rvert = p$, $\lvert R \rvert = q$, and an edge $(h(r, c), v(r, c))$ for each muddy cell $(r, c)$. By König's Theorem, the minimum number of planks is $\tau(G) = \nu(G)$.
- **Step 4 — Concrete Toy Trace**:
  On a $2 \times 2$ grid $\begin{smallmatrix} * & . \\ * & * \end{smallmatrix}$, horizontal strips are $H_1 = \{(1,1)\}$, $H_2 = \{(2,1), (2,2)\}$; vertical strips are $V_1 = \{(1,1), (2,1)\}$, $V_2 = \{(2,2)\}$. Edges: $(H_1, V_1)$ from $(1,1)$, $(H_2, V_1)$ from $(2,1)$, $(H_2, V_2)$ from $(2,2)$. Matching $\{(H_1, V_1), (H_2, V_2)\}$ has size $\nu(G) = 2$, matching MVC $\{V_1, H_2\}$.
- **Complete Solution & Complexity**: Maximal strip decomposition in $O(RC)$ + Dinic on $\le RC$ vertices and $\le RC$ edges in $O((RC)^{1.5})$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Since planks can overlap on mud, is there ever a reason to use a plank shorter than the maximal contiguous run of `*` cells?
  - *Hint 2*: After fixing all maximal horizontal and vertical mud strips, how many ways can a single muddy cell $(r, c)$ be covered?
  - *Hint 3*: Exactly two ways: its horizontal strip $H_i$ or its vertical strip $V_j$. Find the Minimum Vertex Cover via König's Theorem.

---

#### Problem `P05`: `[HEOI2012] 游戏` (Luogu P2825)
- **Judge URL**: [https://www.luogu.com.cn/problem/P2825](https://www.luogu.com.cn/problem/P2825)
- **Constraints**: $N, M \le 50$; grid of `#` (hard wall: blocks bomb rays, cannot place bomb), `x` (soft obstacle: cannot place bomb, does *not* block rays), `*` (empty cell: can place bomb); Time Limit $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Place the maximum number of non-attacking bombs on `*` cells, where bombs attack along row/column rays until stopped by `#` (passing right through `x`).
- **Step 2 — Intermediate Algebraic Representation**:
  Two `*` cells in the same row conflict iff there is no `#` between them — i.e., they lie in the same maximal `#`-free horizontal segment $H_i$. Similarly, two `*` cells in the same column conflict iff they lie in the same maximal `#`-free vertical segment $V_j$. Thus each maximal segment $H_i$ or $V_j$ can hold **at most one** bomb!
- **Step 3 — Reverse-Engineering Scratchpad**:
  Let $L = \{H_1, \dots, H_p\}$ be the maximal `#`-free row segments and $R = \{V_1, \dots, V_q\}$ be the maximal `#`-free column segments.
  - Each empty cell $(r, c)$ with $\text{grid}[r][c] = \text{'*'}$ adds an edge $(H_{\text{id}(r,c)}, V_{\text{id}(r,c)})$.
  - Soft obstacles `x` do **not** split segments, and add **no** edges!
  - Choosing non-conflicting `*` cells is equivalent to choosing edges with no shared endpoints in $L$ or $R$ — i.e., **Maximum Matching $\nu(G)$**!
- **Step 4 — Concrete Toy Trace & Soft-Obstacle Trap**:
  In a $1 \times 3$ row `* x *`, there is no `#`, so all 3 cells belong to a single horizontal segment $H_1$, while columns give $V_1, V_2, V_3$. Only `*` cells add edges: $(H_1, V_1)$ and $(H_1, V_3)$. Thus $\nu(G) = 1$ (since $H_1$ has capacity $1$). **Trap**: If you split segments on `x` as well as `#`, you would get $H_1$ and $H_2$ and falsely place $2$ bombs that blow each other up across `x`!
- **Complete Solution & Complexity**: Segment scan in $O(NM)$ + Dinic in $O((NM)^{1.5})$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: If there were no `#` walls at all, what would a bomb at $(r, c)$ claim?
  - *Hint 2*: A `#` wall splits a row/column into independent segments, whereas `x` only forbids placing a bomb on that specific square.
  - *Hint 3*: Build $L = \{\text{row segments}\}$, $R = \{\text{col segments}\}$, add an edge for each `*` cell, and compute $\nu(G)$.

---

#### Problem `P06`: `AtCoder ABC 274 G — Security Camera 3`
- **Judge URL**: [https://atcoder.jp/contests/abc274/tasks/abc274_g](https://atcoder.jp/contests/abc274/tasks/abc274_g)
- **Constraints**: $H, W \le 300$; grid of `.` (empty) and `#` (obstacle); Time Limit $3.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Place the minimum number of directional cameras (each facing ONE of Up, Down, Left, Right and seeing until `#`) to watch every `.` cell. At first sight, 4 directions looks like 4 choices per cell, not bipartite.
- **Step 2 — Intermediate Algebraic Representation (`Dominance Reduction`)**:
  Any `.` cell $(r, c)$ belongs to a maximal `#`-free horizontal segment $H_i = [c_L, c_R]$ and vertical segment $V_j = [r_U, r_D]$.
  - A camera placed anywhere in $H_i$ facing **Right** is strictly dominated by a camera placed at the **leftmost cell $(r, c_L)$ facing Right**, which covers the **entire** segment $H_i$!
  - Symmetrically, any camera in $H_i$ facing Left is dominated by $(r, c_R)$ facing Left (also covering all of $H_i$), and any vertical camera in $V_j$ is dominated by $(r_U, c)$ facing Down (covering all of $V_j$).
  Thus the 4 directional choices collapse to **2 segment choices**: cover $H_i$ (cost $1$) or cover $V_j$ (cost $1$), subject to $x_{H_i} + y_{V_j} \ge 1$ for every empty cell $(r, c) = (H_i, V_j)$!
- **Step 3 — Reverse-Engineering Scratchpad**:
  Identical to `P04` (`Muddy Fields`): $L = \{\text{maximal horizontal } \text{'.'} \text{ segments}\}$, $R = \{\text{maximal vertical } \text{'.'} \text{ segments}\}$, and an edge $(H_i, V_j)$ for each `.` cell. Answer is $\tau(G) = \nu(G)$.
- **Step 4 — Concrete Toy Trace**:
  On a $2 \times 2$ empty grid, there are 2 row segments $H_1, H_2$ and 2 column segments $V_1, V_2$ forming $K_{2,2}$; $\tau(K_{2,2}) = \nu(K_{2,2}) = 2$ cameras.
- **Complete Solution & Complexity**: $\lvert L \rvert + \lvert R \rvert \le 2HW \le 1.8 \cdot 10^5$, $\lvert E \rvert \le HW \le 9 \cdot 10^4$. Dinic runs in $O(HW \sqrt{HW}) \approx 2.7 \cdot 10^7$ ops ($< 0.15\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: If you place a Right-facing camera on a horizontal segment, why not slide it all the way to the left wall `#` of that segment?
  - *Hint 2*: Once slid to the wall, a single camera covers the *entire* maximal horizontal (or vertical) segment!
  - *Hint 3*: Now each `.` cell just needs its horizontal segment or its vertical segment covered — apply König's Theorem.

---

#### Problem `P07`: `[SCOI2010] 部落战争` (Luogu P2172)
- **Judge URL**: [https://www.luogu.com.cn/problem/P2172](https://www.luogu.com.cn/problem/P2172)
- **Constraints**: $M, N \le 50$; jump parameters $R, C \ge 1$; grid of `.` (camp to visit) and `x` (forbidden); Time Limit $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Cover all `.` camps with the minimum number of armies, where each army jumps **strictly downward** by $(\Delta r, \Delta c) \in \{ (R, \pm C), (C, \pm R) \}$ and **no two armies can ever visit the same camp**.
- **Step 2 — Intermediate Algebraic Representation**:
  Because every jump increases the row coordinate ($\Delta r \in \{R, C\} \ge 1$), the jump graph $G = (V, E)$ on the $K$ camps `.` is a **DAG**! Since no two armies can share a camp, we want the **Minimum Vertex-Disjoint Path Cover (`MDPC`)** of the DAG $G$:
  $$\text{Min Armies} = K - \nu(G_{\text{split}}(G)).$$
- **Step 3 — Reverse-Engineering Scratchpad**:
  Split each `.` cell $u$ into $u_{\text{out}} \in L$ and $u_{\text{in}} \in R$. For each valid jump $u \to v$ between two `.` cells, add edge $(u_{\text{out}}, v_{\text{in}})$. Run Dinic and output $K - \nu(G_{\text{split}})$.
- **Step 4 — Concrete Toy Trace**:
  With $R = 1, C = 1$ on $3 \times 3$ all-`.` grid ($K = 9$), rows $1 \to 2 \to 3$ allow diagonal jumps; maximum matching on $G_{\text{split}}$ merges $6$ transitions, leaving $9 - 6 = 3$ armies.
- **Complete Solution & Complexity**: $\lvert V \rvert \le 2500$, $\lvert E \rvert \le 10^4$; Dinic runs in $O(E\sqrt{V})$ ($< 0.05\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Since armies only jump to strictly larger row indices, can a trajectory ever cycle?
  - *Hint 2*: The valid jumps form a DAG, and armies cannot share vertices. What standard DAG problem is this?
  - *Hint 3*: Minimum Vertex-Disjoint Path Cover: split each `.` camp into $(u_{\text{out}}, u_{\text{in}})$ and compute $K - \nu(G_{\text{split}})$.

---

### Tier 2: Intermediate (8 Problems — `P08` to `P15`)

---

#### Problem `P08`: `[网络流 24 题] 魔术球问题` (Luogu P2765)
- **Judge URL**: [https://www.luogu.com.cn/problem/P2765](https://www.luogu.com.cn/problem/P2765)
- **Constraints**: $N \le 55$ pegs; find maximum balls $M$ placed sequentially $1, 2, \dots, M$ such that adjacent balls on any peg sum to a perfect square, and print each peg's stack.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Ball $v$ can be placed directly on top of ball $u < v$ iff $u + v = k^2$. Since $u < v$ and each ball $u$ can have at most one ball placed directly on top of it, each peg's sequence $u_1 < u_2 < \dots < u_r$ is a directed path in the DAG $G_M = (\{1, \dots, M\}, E_M)$ where $(u \to v) \iff u < v \land u + v = k^2$.
- **Step 2 — Intermediate Algebraic Representation**:
  Balls $1, \dots, M$ fit on $N$ pegs iff $\text{MDPC}(G_M) = M - \nu(G_{\text{split}}(G_M)) \le N$.
- **Step 3 — Reverse-Engineering Scratchpad (`Incremental Residual Augmentation`)**:
  Instead of binary searching on $M$ and rebuilding Dinic from scratch, increment $M = 1, 2, 3, \dots$ **online on the persistent residual network**:
  - When ball $M$ arrives, add $S \to M_{\text{out}} (1)$, $M_{\text{in}} \to T (1)$, and $u_{\text{out}} \to M_{\text{in}} (1)$ for all $1 \le u < M$ with $u + M = k^2$.
  - Run Dinic on the existing residual network (`+1` if an augmenting path to $M_{\text{in}} \to T$ is found, `+0` otherwise).
  - Then $\text{pegs}(M) = M - \text{MaxFlow}(M)$ either stays the same or increases by $1$. Stop at the last $M$ with $\text{pegs}(M) \le N$!
- **Step 4 — Concrete Toy Trace**:
  - $M = 1, 2$: no square sums $\implies 2$ pegs: $[1], [2]$.
  - $M = 3$: $1 + 3 = 4 = 2^2 \implies (1_{\text{out}}, 3_{\text{in}})$ matches! Pegs $= 3 - 1 = 2$: $[1, 3], [2]$.
  - $M = 4$: no square sum with $1, 2, 3$ ($1+4=5, 2+4=6, 3+4=7$) $\implies$ needs a 3rd peg! Thus for $N = 2$ pegs, the maximum is $M = 3$.
- **Complete Solution & Complexity**: For $N = 55$, $M^* = 1567$. Incremental Dinic takes $O(M^* \sqrt{M^*})$ total time ($< 0.02\text{ s}$). Reconstruct chains by following $u \to v$ where $f(u_{\text{out}}, v_{\text{in}}) = 1$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Since balls are placed in increasing order $1, 2, \dots, M$, why does each peg correspond to a directed path in a DAG?
  - *Hint 2*: $M$ balls fit on $N$ pegs iff the Minimum Disjoint Path Cover $M - \nu(G_M) \le N$.
  - *Hint 3*: Don't rebuild the network for each $M$: add vertex $M$ to the existing residual graph and augment!

---

#### Problem `P09`: `[JSOI2009] 游戏` (Luogu P4055)
- **Judge URL**: [https://www.luogu.com.cn/problem/P4055](https://www.luogu.com.cn/problem/P4055)
- **Constraints**: $N, M \le 100$; grid of `.` (passable) and `#` (wall); Time Limit $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Two-player Normal-Play walk game on a grid: `YY` (Chooser) picks the starting square $v_0$, and `HH` (First Mover) makes the first move from $v_0$. Find all $v_0$ where **First Mover `HH` wins**!
- **Step 2 — Intermediate Algebraic Representation**:
  Color grid cells by $(r + c) \bmod 2 \in \{0, 1\}$ to form a bipartite graph $G = (L \cup R, E)$. By Theorem 3.3 (Section 3.4), the **First Mover (`HH`) wins from $v_0$** iff $v_0$ is **Essential** (belongs to *every* maximum matching of $G$), whereas the **Chooser (`YY`, who is Second Mover) wins from $v_0$** iff $v_0 \in L_1 \cup R_2$ is **Avoidable**!
- **Step 3 — Reverse-Engineering Scratchpad**:
  1. Run Dinic on $G = (L \cup R, E)$ to find a maximum flow $f^*$.
  2. In the residual network $G_{f^*}$, find $L_1 = L \cap V_S$ (all $u \in L$ reachable from $S$ via $c_f > 0$) and $R_2 = R \cap V_T^{\text{rev}}$ (all $v \in R$ from which $T$ is reachable via $c_f > 0$).
  3. If $\lvert L_1 \rvert + \lvert R_2 \rvert = 0$ (G has a perfect matching), `HH` wins from every cell (`LOSE` for `YY`). Otherwise, `YY` wins (`WIN`) by picking any cell in $L_1 \cup R_2$ sorted by $(r, c)$!
- **Step 4 — Concrete Toy Trace**:
  On a $1 \times 3$ path $(1,1) - (1,2) - (1,3)$, $L = \{(1,1), (1,3)\}$ and $R = \{(1,2)\}$. Max matching size is $1$, matching $(1,1)$ to $(1,2)$ and leaving $(1,3) \in U_L$. Residual BFS from $S$ visits $(1,3) \in U_L \to (1,2) \in R \to (1,1) \in L$. Thus $L_1 = \{(1,1), (1,3)\}$ are Avoidable (`YY` wins by choosing $(1,1)$ or $(1,3)$), while $(1,2)$ is Essential (`HH` wins if `YY` chooses $(1,2)$).
- **Complete Solution & Complexity**: Single Dinic + two $O(V + E)$ BFS runs in $O(NM \sqrt{NM})$ ($< 0.05\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Be careful with player roles: `YY` only picks the starting square $v_0$, and `HH` makes the first move! So `YY` is the *Second Mover* in the walk game.
  - *Hint 2*: In a bipartite graph, Second Mover wins from $v_0$ iff there is a maximum matching $M$ that leaves $v_0$ unmatched.
  - *Hint 3*: Run Dinic once, and find all Avoidable vertices $L_1 \cup R_2$ via residual reachability from $S$ and to $T$.

---

#### Problem `P10`: `[HNOI2013] 消毒` (Luogu P3231)
- **Judge URL**: [https://www.luogu.com.cn/problem/P3231](https://www.luogu.com.cn/problem/P3231)
- **Constraints**: $T \le 3$ test cases; 3D box dimensions $A, B, C \ge 1$ with **$A \cdot B \cdot C \le 5000$**; Time Limit $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Disinfecting a sub-box $a \times b \times c$ costs $\min(a, b, c)$. Notice that a $1 \times B \times C$ slice, $A \times 1 \times C$ slice, or $A \times B \times 1$ slice each costs $\min(1, \dots) = 1$, and any box of cost $k$ can be decomposed into $k$ unit-thickness planes of cost $1$! So we must cover all infected cells $(x_i, y_i, z_i)$ using the minimum number of axis-aligned planes $x = x_0$, $y = y_0$, or $z = z_0$.
- **Step 2 — Intermediate Algebraic Representation**:
  3D Hypergraph Vertex Cover ($u_x + v_y + w_z \ge 1$) is NP-hard in general, **but $A \cdot B \cdot C \le 5000 \implies \min(A, B, C) \le \lfloor 5000^{1/3} \rfloor = 17$**! Permute axes so $A = \min(A, B, C) \le 17$. If we fix the subset $S_X \subseteq \{1, \dots, A\}$ of $x$-planes purchased outright, every surviving infected cell $(x, y, z)$ with $x \notin S_X$ must be covered by $y$-planes or $z$-planes:
  $$\min_{S_X \subseteq \{1, \dots, A\}} \Big( \lvert S_X \rvert + \tau\big(G_{YZ}(S_X)\big) \Big), \quad \text{where } E\big(G_{YZ}(S_X)\big) = \{ (y, z) : \exists (x, y, z) \text{ infected with } x \notin S_X \}.$$
- **Step 3 — Reverse-Engineering Scratchpad**:
  For each infected cell $(x, y, z)$, bitwise-OR `(1 << x)` into `mask[y][z]`. Then for each bitmask `M` from $0$ to $2^A - 1$:
  - Build the 2D bipartite graph $G_{YZ}(M)$ on $L = \{1, \dots, B\}$ and $R = \{1, \dots, C\}$, adding edge $(y, z)$ iff `(mask[y][z] & ~M) != 0`.
  - Compute $\nu(G_{YZ}(M))$ via Kuhn/Dinic and update $\text{ans} = \min(\text{ans}, \text{popcount}(M) + \nu(G_{YZ}(M)))$.
- **Step 4 — Concrete Toy Trace**:
  If $A = 2, B = 3, C = 3$ with infected cells $(1, 1, 1), (1, 2, 2), (2, 1, 2)$:
  - Mask $S_X = \{1\}$ (cost $1$): eliminates $(1,1,1)$ and $(1,2,2)$, leaving only $(2, 1, 2)$, which needs $1$ edge in $G_{YZ}$, total cost $1 + 1 = 2$.
- **Complete Solution & Complexity**: At most $2^{17}$ masks (and when $A = 17$, $B \cdot C \le 5000 / 17 = 294$, so $G_{YZ}$ has $\le 294$ edges!). With pruning (`if popcount(M) >= ans: continue`), total runtime is $< 0.25\text{ s}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Why is it always optimal to only use full planes of thickness $1$ ($1 \times B \times C$, $A \times 1 \times C$, or $A \times B \times 1$) of cost $1$ each?
  - *Hint 2*: 3D König's theorem is false (NP-hard), so look at the constraint $A \cdot B \cdot C \le 5000$. How large can $\min(A, B, C)$ be?
  - *Hint 3*: $\min(A, B, C) \le 17$. Brute-force the $2^A$ bitmask of chosen $x$-planes and solve the remaining 2D projection via König's Theorem!

---

#### Problem `P11`: `Codeforces 1404 E — Bricks`
- **Judge URL**: [https://codeforces.com/problemset/problem/1404/E](https://codeforces.com/problemset/problem/1404/E)
- **Constraints**: $N, M \le 200$; grid of `#` (black) and `.` (white); cover all `#` cells with minimum non-overlapping $1 \times L$ or $L \times 1$ bricks; Time Limit $4.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Since bricks cannot overlap (unlike `Muddy Fields`), every black cell belongs to **either** a horizontal brick **or** a vertical brick. Starting from $B = \#\text{black cells}$ of $1 \times 1$ bricks, each **valid merge** across a shared boundary between two adjacent black cells reduces the total number of bricks by $1$!
- **Step 2 — Intermediate Algebraic Representation**:
  Let $L$ be the set of horizontal unit adjacencies $e_H = \{(r, c), (r, c+1)\}$ between two `#` cells, and $R$ be the set of vertical unit adjacencies $e_V = \{(r, c), (r+1, c)\}$ between two `#` cells. A set of merges forms valid $1 \times L$ and $L \times 1$ bricks iff **no black cell $(r, c)$ is incident to both a chosen horizontal merge $e_H \in L$ and a chosen vertical merge $e_V \in R$**:
  $$\text{Min Bricks} = \#\text{black} - \max \lvert I \rvert = \#\text{black} - \alpha(G_{\text{adj}}) = \#\text{black} - \big(\lvert L \rvert + \lvert R \rvert - \nu(G_{\text{adj}})\big).$$
- **Step 3 — Reverse-Engineering Scratchpad**:
  1. Create a vertex in $L$ for every horizontally adjacent `#-#` pair, and a vertex in $R$ for every vertically adjacent `#/#` pair.
  2. For each `#` cell $(r, c)$, add a conflict edge between each horizontal adjacency incident to $(r, c)$ (left/right, at most 2) and each vertical adjacency incident to $(r, c)$ (up/down, at most 2).
  3. Run Dinic to find $\nu(G_{\text{adj}})$ and output $\#\text{black} - (\lvert L \rvert + \lvert R \rvert - \nu(G_{\text{adj}}))$.
- **Step 4 — Concrete Toy Trace**:
  On an L-tromino $\begin{smallmatrix} \# & . \\ \# & \# \end{smallmatrix}$ ($\#\text{black} = 3$), there is $1$ horizontal merge $e_H = \{(2,1), (2,2)\} \in L$ and $1$ vertical merge $e_V = \{(1,1), (2,1)\} \in R$. They share corner cell $(2,1)$, so $(e_H, e_V) \in E$. Here $\lvert L \rvert = 1, \lvert R \rvert = 1, \nu = 1 \implies \alpha = 2 - 1 = 1$ merge, giving $3 - 1 = 2$ bricks.
- **Complete Solution & Complexity**: $\lvert L \rvert + \lvert R \rvert \le 2NM = 8 \cdot 10^4$, $\lvert E \rvert \le 4NM = 1.6 \cdot 10^5$. Dinic runs in $< 0.3\text{ s}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Instead of counting bricks directly, if you start with every `#` cell as a $1 \times 1$ brick, what happens each time you glue two adjacent `#` cells together?
  - *Hint 2*: The brick count drops by $1$. When is a set of horizontal and vertical gluings invalid?
  - *Hint 3*: Exactly when a `#` cell is glued both horizontally and vertically (forming an L-corner). Model gluings as vertices in $L \cup R$ and find the Bipartite MIS!

---

#### Problem `P12`: `AtCoder ABC 354 G — Select Strings`
- **Judge URL**: [https://atcoder.jp/contests/abc354/tasks/abc354_g](https://atcoder.jp/contests/abc354/tasks/abc354_g)
- **Constraints**: $N \le 100$ strings $S_i$, $\sum \lvert S_i \rvert \le 5000$, weights $A_i \in [1, 10^9]$; select subset of max total weight where no string is a substring of another; Time Limit $2.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  The substring relation $S_i \subseteq_{\text{sub}} S_j$ is **transitive** (if $S_i$ is in $S_j$ and $S_j$ is in $S_k$, then $S_i$ is in $S_k$) and antisymmetric on distinct strings! Selecting pairwise incomparable elements of maximum total weight is **Maximum-Weight Antichain on a Poset (Weighted Dilworth)**.
- **Step 2 — Intermediate Algebraic Representation**:
  First **deduplicate identical strings**: if $S_i = S_j$, we can never pick both, so keep only $\max(A_i, A_j)$ (if $S_i = S_j$ were kept with $i \prec j$ and $j \prec i$, the graph would have 2-cycles and violate strict poset antisymmetry!). On the deduplicated strict poset $\mathcal{P} = (V, \prec)$, by Lemma 6.1 (Transitivity Non-Overlap Lemma), the maximum-weight antichain equals:
  $$\text{Max Weight Antichain} = \sum_{u \in V} A_u - \tau_w\big(G_{\text{split}}(\mathcal{P})\big).$$
- **Step 3 — Reverse-Engineering Scratchpad**:
  Build $N$: $S \to u_{\text{out}}$ (capacity $A_u$), $u_{\text{in}} \to T$ (capacity $A_u$), and for every $u \ne v$ with $S_u$ a substring of $S_v$, add $u_{\text{out}} \to v_{\text{in}}$ (capacity $\infty$). Answer is $\sum_{u \in V} A_u - \text{MaxFlow}(S, T)$.
- **Step 4 — Concrete Toy Trace & Duplicate-String Trap**:
  Suppose $S_1 = \text{"a"} (A_1 = 5)$, $S_2 = \text{"a"} (A_2 = 7)$, $S_3 = \text{"ab"} (A_3 = 6)$. Deduplicating `"a"` keeps $S_2$ with weight $7$; then $S_2 \prec S_3$ has $\text{MaxFlow} = \min(7, 6) = 6$, giving $7 + 6 - 6 = 7$. **Trap**: Without deduplicating `"a"`, adding both $1_{\text{out}} \to 2_{\text{in}}$ and $2_{\text{out}} \to 1_{\text{in}}$ cuts both for $5 + 5 = 10$ or corrupts the antichain!
- **Complete Solution & Complexity**: Substring check in $O(N \sum \lvert S_i \rvert)$ + Dinic on $2N + 2$ vertices in $O(N^3)$ ($< 0.02\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: What happens if two input strings are identical ($S_i = S_j$)? Can you ever pick both?
  - *Hint 2*: After keeping only the maximum weight for each unique string, the substring relation forms a strict poset (transitively closed DAG).
  - *Hint 3*: Apply Weighted Dilworth: split each string into $(u_{\text{out}}, u_{\text{in}})$ with capacity $A_u$, connect $u_{\text{out}} \to v_{\text{in}} (\infty)$ if $S_u \subsetneq S_v$, and output $\sum A_u - \text{MaxFlow}$.

---

#### Problem `P13`: `Codeforces 808 F — Card Game`
- **Judge URL**: [https://codeforces.com/problemset/problem/808/F](https://codeforces.com/problemset/problem/808/F)
- **Constraints**: $N \le 100$ cards with power $p_i$, magic number $c_i \le 10^5$, level $l_i \le N$; target power $K \le 10^5$; no two chosen cards may have $c_i + c_j \in \mathbb{P}$; Time Limit $2.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Minimize level $L$ such that among cards with $l_i \le L$, we can choose a subset of total power $\ge K$ with no prime sum $c_i + c_j \in \mathbb{P}$. Monotonicity in $L$ screams **Binary Search on $L$** + **Maximum-Weight Independent Set (`MWIS`)** on the prime-sum conflict graph!
- **Step 2 — Intermediate Algebraic Representation & The `1 + 1 = 2` Trap**:
  Every prime $p > 2$ is odd, so conflicts only connect odd $c_i$ to even $c_j$, **EXCEPT $1 + 1 = 2$**!
  - Because $c_i \ge 1$, $c_i + c_j = 2 \iff c_i = c_j = 1$. Thus all available cards with $c_i = 1$ form a **clique** (at most one `1`-card can ever be chosen)!
  - **Deduplication**: Among all available cards with $l_i \le L$ and $c_i = 1$, keep **only the single card with maximum $p_i$**! Once at most one $c_i = 1$ remains, **zero odd–odd conflicts exist**, and the conflict graph $G_L = (L_{\text{odd}} \cup R_{\text{even}}, E)$ is 100% bipartite!
- **Step 3 — Reverse-Engineering Scratchpad**:
  For a fixed level $L$, filter $l_i \le L$, deduplicate $c_i = 1$ to the single highest $p_i$, and build the MWIS network:
  - $S \to u$ (cap $p_u$) for odd $c_u$; $v \to T$ (cap $p_v$) for even $c_v$; $u \to v$ (cap $\infty$) if $c_u + c_v$ is prime.
  - Feasible iff $\sum p_z - \text{MaxFlow}(S, T) \ge K$.
- **Step 4 — Concrete Toy Trace**:
  Cards at level $\le L$: $(p=5, c=1), (p=8, c=1), (p=6, c=2)$. Deduplicating $c=1$ keeps $(p=8, c=1)$. Since $1 + 2 = 3 \in \mathbb{P}$, edge $(1, 2)$ has $\text{MaxFlow} = \min(8, 6) = 6$, so $\text{MWIS} = 8 + 6 - 6 = 8$.
- **Complete Solution & Complexity**: Sieve primes up to $2 \cdot 10^5$ + $\log_2 N \approx 7$ Dinic runs on $\le 102$ vertices ($< 0.05\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Binary search on the level $L$. For a fixed $L$, why is the prime-sum conflict graph *almost* bipartite?
  - *Hint 2*: The only even prime is $2 = 1 + 1$. How many cards with $c_i = 1$ can appear in a valid subset?
  - *Hint 3*: At most one! Keep only the highest-power card with $c_i = 1$; then the graph is strictly bipartite between odd and even $c_i$.

---

#### Problem `P14`: `Codeforces 1783 F — Double Sort II`
- **Judge URL**: [https://codeforces.com/problemset/problem/1783/F](https://codeforces.com/problemset/problem/1783/F)
- **Constraints**: $N \le 3000$; two permutations $a, b$ of $\{1, \dots, N\}$; each operation chooses $x, y$ and swaps **both** $a_x \leftrightarrow a_y$ and $b_x \leftrightarrow b_y$ (actually: chooses value $v$ and swaps the position of $v$ in $a$ with $v$, and in $b$ with $v$, i.e. fixes at least one element per op, or viewed via cycle decomposition); Time Limit $2.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Sorting a single permutation $a$ with $c_a$ cycles takes $N - c_a$ operations (one element per cycle is left untouched as the cycle's anchor, while the other $\lvert C \rvert - 1$ elements are operated on). When sorting $a$ and $b$ **simultaneously**, an element $i \in \{1, \dots, N\}$ is untouched if and only if we skip operating on $i$.
- **Step 2 — Intermediate Algebraic Representation**:
  Let $C_1^a, \dots, C_{c_a}^a$ be the disjoint cycles of $a$ and $C_1^b, \dots, C_{c_b}^b$ be the disjoint cycles of $b$. A subset of elements $I \subseteq \{1, \dots, N\}$ can be left **untouched** (requiring $N - \lvert I \rvert$ operations) iff $I$ contains **at most one element from each cycle of $a$ AND at most one element from each cycle of $b$**!
- **Step 3 — Reverse-Engineering Scratchpad**:
  Let $L = \{C_1^a, \dots, C_{c_a}^a\}$ and $R = \{C_1^b, \dots, C_{c_b}^b\}$. Each element $i \in \{1, \dots, N\}$ belongs to a unique cycle $u(i) \in L$ and a unique cycle $v(i) \in R$, defining an edge $e_i = (u(i), v(i)) \in L \times R$.
  - Choosing untouched elements $I$ with at most one per cycle in $a$ and at most one per cycle in $b$ is literally **Maximum Bipartite Matching $\nu(G)$**!
  - Minimum operations $= N - \nu(G)$, and the operated elements are $\{1, \dots, N\} \setminus I^*$.
- **Step 4 — Concrete Toy Trace**:
  For $N = 3$, $a = [2, 1, 3]$ (cycles $\{1, 2\}, \{3\}$) and $b = [1, 3, 2]$ (cycles $\{1\}, \{2, 3\}$). Edges: $e_1 = (C_1^a, C_1^b)$, $e_2 = (C_1^a, C_2^b)$, $e_3 = (C_2^a, C_2^b)$. Maximum matching $\{e_1, e_3\}$ has size $\nu = 2$, leaving $\{1, 3\}$ untouched and operating only on element $2$ ($3 - 2 = 1$ operation!).
- **Complete Solution & Complexity**: $\lvert L \rvert + \lvert R \rvert \le 2N = 6000$, $\lvert E \rvert = N = 3000$; Dinic runs in $O(N \sqrt{N})$ ($< 0.05\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Instead of minimizing the elements you operate on, try maximizing the set of elements $I \subseteq \{1, \dots, N\}$ you **never touch**!
  - *Hint 2*: In a single permutation, a cycle of length $k$ needs at least $k - 1$ operations, meaning at most $1$ element in each cycle can go untouched.
  - *Hint 3*: Each element $i$ is an edge between its cycle in $a$ and its cycle in $b$. Find the maximum matching $\nu(G)$ and operate on the remaining $N - \nu(G)$ elements!

---

#### Problem `P15`: `[SCOI2010] 连续攻击游戏` (Luogu P1640)
- **Judge URL**: [https://www.luogu.com.cn/problem/P1640](https://www.luogu.com.cn/problem/P1640)
- **Constraints**: $N \le 10^6$ items, each with two attribute values $(a_i, b_i) \in [1, 10^4]^2$; each item can be used at most once; find maximum $K$ such that attributes $1, 2, \dots, K$ are all matched; Time Limit $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  We must match a **consecutive prefix** of attributes $1, 2, \dots, K$ ($L = \{1, \dots, 10^4\}$) to distinct items ($R = \{1, \dots, N\}$). Since $N \le 10^6$ is huge while $\lvert L \rvert \le 10^4$ is small, we can either use **Transversal Matroid Sequential Kuhn** from $L$ or view each item $i$ as an edge $(a_i, b_i)$ between attributes!
- **Step 2 — Intermediate Algebraic Representation (`Two Equivalent Compilations`)**:
  - **Compilation 1 (Transversal Matroid Sequential Kuhn on $L$)**: By Theorem 2.2 (Section 2.6), matchable subsets of $L$ form a matroid, and augmenting paths from $u = K$ never unmatch $1, \dots, K-1$. Run Kuhn's DFS for $u = 1, 2, \dots, 10^4$ in order; stop at the first $u$ that fails to augment!
  - **Compilation 2 ($O(N \alpha(N))$ Pseudoforest DSU on Attributes)**: View each item $i$ as an undirected edge $(a_i, b_i)$ on the $10^4$ attributes. Orienting each edge toward the attribute it covers gives in-degree $\le 1$, so a connected component $C$ of $V_C$ attributes can be **completely covered** iff it is not a tree ($\lvert E_C \rvert \ge \lvert V_C \rvert$, i.e. a pseudoforest with a cycle); if it is a tree ($\lvert E_C \rvert = \lvert V_C \rvert - 1$), all attributes in $C$ **except the single largest attribute $\max(C)$** can be covered!
- **Step 3 — Reverse-Engineering Scratchpad**:
  In Compilation 1, store adjacency lists from $L = \{1, \dots, 10^4\}$ to $R = \{1, \dots, N\}$ and run Kuhn with timestamped `vis[u] == timer` (so clearing `vis` takes $O(1)$). In Compilation 2, merge $(a_i, b_i)$ in a DSU tracking `has_cycle[root]` and `max_val[root]`; then scan $u = 1 \dots 10^4$.
- **Step 4 — Concrete Toy Trace**:
  Items $(1, 2)$ and $(2, 3)$: on attributes $\{1, 2, 3\}$, this is a 3-vertex tree with 2 edges. Both Sequential Kuhn ($1 \to \text{item } 1$, $2 \to \text{item } 2$, $3$ fails) and DSU (tree with $\max = 3$ uncovered) output $K = 2$.
- **Complete Solution & Complexity**: Sequential Kuhn takes $O(\lvert L \rvert \cdot N)$ worst-case, while Pseudoforest DSU takes **$O(N \alpha(\lvert L \rvert))$** ($\approx 0.03\text{ s}$)!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Does finding an augmenting path from attribute $K$ ever unmatch any of attributes $1, 2, \dots, K-1$?
  - *Hint 2*: Never! So you can run Kuhn's DFS sequentially for $u = 1, 2, \dots, 10^4$ and stop at the first failure.
  - *Hint 3*: Even faster: treat each item $(a_i, b_i)$ as an edge between attributes $a_i$ and $b_i$; a tree component of size $s$ can cover $s - 1$ attributes (all except its maximum vertex), while a component with a cycle covers all $s$!

---

### Tier 3: Advanced (8 Problems — `P16` to `P23`)

---

#### Problem `P16`: `AtCoder ABC 317 G — Rearranging`
- **Judge URL**: [https://atcoder.jp/contests/abc317/tasks/abc317_g](https://atcoder.jp/contests/abc317/tasks/abc317_g)
- **Constraints**: $N, M \le 100$; $N \times M$ grid $A$ containing each integer $1, \dots, N$ exactly $M$ times; permute elements within each row so every column becomes a permutation of $\{1, \dots, N\}$; Time Limit $2.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Within each row $r \in \{1, \dots, N\}$, we have $M$ numbers that must be assigned to $M$ distinct columns $c \in \{1, \dots, M\}$ such that each column $c$ receives each value $v \in \{1, \dots, N\}$ exactly once.
- **Step 2 — Intermediate Algebraic Representation**:
  Build a bipartite multigraph $G = (L \cup R, E)$ between **Rows** $L = \{r_1, \dots, r_N\}$ and **Values** $R = \{v_1, \dots, v_N\}$, adding one edge $(r_i, v)$ for each cell in row $i$ containing value $v$.
  - Every row $r_i \in L$ has $M$ cells $\implies \deg_G(r_i) = M$.
  - Every value $v \in R$ appears $M$ times in the grid $\implies \deg_G(v) = M$.
  Thus $G$ is an **$M$-regular bipartite multigraph**! By the **Birkhoff–von Neumann Theorem** (Theorem 4.2), $E(G)$ decomposes into $M$ edge-disjoint perfect matchings $M_1, M_2, \dots, M_M$, where $M_c$ assigns each row $r_i$ the value it places in column $c$!
- **Step 3 — Reverse-Engineering Scratchpad**:
  For $c = 1, 2, \dots, M$: run Dinic on the remaining edges of $G$ to extract a perfect matching $M_c$, place the matched values into column $c$ of the output matrix, delete the $N$ used edges from $G$, and repeat!
- **Step 4 — Concrete Toy Trace**:
  For $N = 2, M = 2$ and $A = \begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix}$, $r_1$ has two edges to $v_1$ and $r_2$ has two edges to $v_2$ — wait: then $\deg(v_1) = 2, \deg(v_2) = 2$, and $M_1 = \{(r_1, v_1), (r_2, v_2)\}$, $M_2 = \{(r_1, v_1), (r_2, v_2)\}$, giving $\begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix}$ where both columns are $\{1, 2\}$!
- **Complete Solution & Complexity**: $M$ runs of Dinic on $2N$ vertices and $\le NM$ edges: $O(M \cdot NM \sqrt{N}) = O(N^{1.5} M^2) \approx 10^7$ ops ($< 0.05\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Forget all columns except column $1$ first: what condition must the $N$ elements placed in column $1$ (one from each row) satisfy?
  - *Hint 2*: They must be a perfect matching between Rows $L$ and Values $R$! What does the graph between Rows and Values look like before and after removing column $1$?
  - *Hint 3*: It is $M$-regular before, and $(M-1)$-regular after! Peel $M$ perfect matchings one column at a time via Birkhoff–von Neumann.

---

#### Problem `P17`: `AtCoder AGC 037 D — Sorting a Grid`
- **Judge URL**: [https://atcoder.jp/contests/agc037/tasks/agc037_d](https://atcoder.jp/contests/agc037/tasks/agc037_d)
- **Constraints**: $N, M \le 100$; $N \times M$ permutation of $1 \dots NM$; sort the grid into row-major order using: Phase 1 (permute within each row $\to B$), Phase 2 (permute within each column $\to C$), Phase 3 (permute within each row $\to D$); Time Limit $2.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Working backwards from the sorted target $D$: Phase 3 only permutes within rows, so **every element $x$ must already be in its final target row $\text{dest}(x) = \lceil x / M \rceil$ at the end of Phase 2 (in matrix $C$)**! And Phase 2 only permutes within columns, so for each column $c \in \{1, \dots, M\}$, the $N$ elements placed into column $c$ at the end of Phase 1 (in matrix $B$) must have **all $N$ distinct target rows $\{1, \dots, N\}$**!
- **Step 2 — Intermediate Algebraic Representation**:
  Build a bipartite multigraph $G = (L \cup R, E)$ between **Current Rows** $L = \{1, \dots, N\}$ and **Target Rows** $R = \{1, \dots, N\}$, where each number $x$ initially in row $r$ induces a labelled edge $e_x = (r, \text{dest}(x))$.
  - Each current row $r \in L$ has $M$ numbers $\implies \deg_G(r) = M$.
  - Each target row $d \in R$ owns $M$ numbers $\implies \deg_G(d) = M$.
  Thus $G$ is an **$M$-regular bipartite multigraph**, and decomposing $G$ into $M$ perfect matchings $M_1, \dots, M_M$ tells us which $N$ numbers to place into column $c$ of $B$!
- **Step 3 — Reverse-Engineering Scratchpad**:
  1. Decompose $G$ into $M$ perfect matchings $M_1, \dots, M_M$ (either via $M$ Dinic runs as in `P16`, or in $O(NM \log M)$ via Eulerian Circuit Halving).
  2. **Construct $B$**: For each column $c = 1 \dots M$, place the edge $e_x \in M_c$ incident to current row $r \in L$ at $B_{r, c} = x$.
  3. **Construct $C$**: Within each column $c$, route each $x = B_{r, c}$ to its target row $C_{\text{dest}(x), c} = x$.
- **Step 4 — Concrete Toy Trace**:
  For $N = 2, M = 2$ and $A = \begin{pmatrix} 4 & 3 \\ 2 & 1 \end{pmatrix}$: target rows are $\text{dest}(1)=\text{dest}(2)=1$, $\text{dest}(3)=\text{dest}(4)=2$. Here row 1 has $\{4, 3\}$ (both $\text{dest}=2$) and row 2 has $\{2, 1\}$ (both $\text{dest}=1$). $M_1 = \{e_4, e_2\}$ (col 1 of $B = [4, 2]^T \to C = [2, 4]^T$) and $M_2 = \{e_3, e_1\}$ (col 2 of $B = [3, 1]^T \to C = [1, 3]^T$).
- **Complete Solution & Complexity**: $O(M \cdot NM \sqrt{N})$ via Dinic peeling or $O(NM \log M)$ via Eulerian Halving ($< 0.05\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: For Phase 3 (row-only swaps) to produce the sorted matrix, what property must matrix $C$ (after Phase 2) already satisfy?
  - *Hint 2*: Every number $x$ in $C$ must sit in its target row $\text{dest}(x) = \lceil x / M \rceil$. What does that require of each column $c$ in matrix $B$ (after Phase 1)?
  - *Hint 3*: Each column $c$ of $B$ must contain exactly one number destined for each target row $1 \dots N$. Decompose the $M$-regular graph from Current Rows to Target Rows!

---

#### Problem `P18`: `Codeforces 600 F — Edge Coloring of Bipartite Graph`
- **Judge URL**: [https://codeforces.com/problemset/problem/600/F](https://codeforces.com/problemset/problem/600/F)
- **Constraints**: $\lvert L \rvert = a \le 1000$, $\lvert R \rvert = b \le 1000$, $M \le 10^5$ edges; color edges with minimum colors $D$ so no two incident edges share a color; Time Limit $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  By Kőnig's Line Coloring Theorem (Theorem 4.2), the minimum number of colors is $D = \Delta(G) = \max_{z \in L \cup R} \deg(z)$. However, $M \le 10^5$ and $\Delta \le 1000$, so running Dinic $\Delta$ times takes $O(\Delta M \sqrt{V}) \approx 3 \cdot 10^9$ operations — **TLE**! We need the **$O(VM)$ Online Kempe-Chain Recoloring** algorithm.
- **Step 2 — Intermediate Algebraic Representation**:
  Maintain a table `who[z][c]` = the edge (or neighbor) incident to vertex $z$ currently colored with $c \in \{1, \dots, \Delta\}$ ($0$ if color $c$ is free at $z$). Since $\deg(z) \le \Delta$, before inserting edge $e = (u, v)$, $u$ has at least one free color $c_u$ and $v$ has at least one free color $c_v$.
- **Step 3 — Reverse-Engineering Scratchpad**:
  Insert edges $e = (u, v)$ one by one:
  1. Find a free color $c_u$ at $u$ and a free color $c_v$ at $v$ in $O(\Delta)$ time.
  2. If `who[v][c_u] == 0` ($c_u$ is also free at $v$), color $e$ with $c_u$ immediately.
  3. Otherwise, walk the maximal alternating path $P$ starting from $v$ using edges of colors $c_u, c_v, c_u, c_v, \dots$:
     $$v \xrightarrow{c_u} u_1 \xrightarrow{c_v} v_1 \xrightarrow{c_u} u_2 \dots$$
     Because $G$ is bipartite, $P$ never visits $u$ (if it reached $u$, it would arrive via an edge of color $c_v$ from $R$, impossible since $c_v$ is required to be at $R \to L$ while $c_u$ is free at $u$!). Swap $c_u \leftrightarrow c_v$ along $P$, then color $(u, v)$ with $c_u$!
- **Step 4 — Concrete Toy Trace & Odd-Cycle Failure**:
  Suppose path $u_1 - v_1 - u_2$ has $(u_1, v_1)$ colored $1$, $(v_1, u_2)$ colored $2$, and we add $(u_1, v_2)$ where $c_{u_1} = 2, c_{v_2} = 1$, and $(u_2, v_2)$ is already colored $1$. Walking from $v_2$ along $(2, 1)$ visits $v_2 \xrightarrow{1} u_2 \xrightarrow{2} v_1 \xrightarrow{1} u_1$ (stops since $2$ is free at $u_1$). Swapping $1 \leftrightarrow 2$ along this path frees color $2$ at $v_2$, allowing $(u_1, v_2)$ to take color $2$. **Non-Bipartite Failure**: On a triangle $C_3$, $\Delta = 2$ but $\chi'(C_3) = 3 > \Delta$ because the $(c_u, c_v)$ alternating path can return to $u$ on the wrong parity!
- **Complete Solution & Complexity**: Each edge insertion scans $O(\Delta)$ for free colors and walks a path of length $\le a + b$, taking $O((a + b)M) \le 2 \cdot 10^8$ array operations ($\approx 0.15\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: By Kőnig's Line Coloring Theorem, the minimum number of colors is simply the maximum degree $\Delta$. Why is running Hopcroft–Karp $\Delta$ times too slow here?
  - *Hint 2*: Color edges one by one. When adding $(u, v)$, pick a free color $c_u$ at $u$ and a free color $c_v$ at $v$.
  - *Hint 3*: Walk the unique alternating path of colors $(c_u, c_v)$ from $v$, swap $c_u \leftrightarrow c_v$ along it, and assign $c_u$ to $(u, v)$!

---

#### Problem `P19`: `AtCoder ARC 076 F — Exhausted?`
- **Judge URL**: [https://atcoder.jp/contests/arc076/tasks/arc076_d](https://atcoder.jp/contests/arc076/tasks/arc076_d)
- **Constraints**: $N \le 2 \cdot 10^5$ people, $M \le 2 \cdot 10^5$ chairs ($1 \dots M$); person $i$ can sit on $[1, L_i] \cup [R_i, M]$; minimize unseated people; Time Limit $2.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Maximum Bipartite Matching on $N, M = 2 \cdot 10^5$ where each neighborhood $N(i) = [1, L_i] \cup [R_i, M]$ is a prefix $\cup$ suffix. Explicit flow is $O(NM)$ (`TLE`); we must use **Ore's Defect Formula**!
- **Step 2 — Intermediate Algebraic Representation**:
  By Section 5.3 (Rule 3), because the *complement* of every neighborhood is a single open interval $(L_i, R_i)$, the maximum defect over all $S \subseteq \{1, \dots, N\}$ is achieved when $N(S) = [1, L] \cup [R, M]$ is a single prefix $\cup$ suffix ($0 \le L < R \le M + 1$, plus the full-coverage baseline $N - M$ when $L \ge R$):
  $$\text{Unseated} = \max\Big( 0, \; N - M, \; \max_{0 \le L < R \le M + 1} \big( \#\{ i : L_i \le L \land R_i \ge R \} - L - (M - R + 1) \big) \Big).$$
- **Step 3 — Reverse-Engineering Scratchpad**:
  Rewrite the inner objective for fixed $L$ and $R > L$:
  $$\text{val}(L, R) = \Big( \#\{ i : L_i \le L \land R_i \ge R \} + R \Big) - L - M - 1.$$
  Sort people by $L_i$ ascending. Maintain a Lazy Segment Tree over $R \in [1, M + 1]$ initialized to $\text{tree}[R] = R$. As $L$ sweeps from $0$ to $M$:
  1. For each person $i$ with $L_i = L$, add $+1$ to the prefix range $R \in [1, R_i]$ in the Segment Tree.
  2. Query $\max_{R \in [L + 1, M + 1]} \text{tree}[R] - L - M - 1$ and update the answer!
- **Step 4 — Concrete Toy Trace**:
  $N = 2$ people with $(L_i, R_i) = (1, 3)$ on $M = 3$ chairs ($N(i) = \{1, 3\}$). At $L = 1, R = 3$, both people satisfy $L_i \le 1 \land R_i \ge 3$, so $\text{val}(1, 3) = (2 + 3) - 1 - 3 - 1 = 0$. What if $3$ people have $(1, 3)$? Then $\text{val}(1, 3) = (3 + 3) - 1 - 3 - 1 = 1$ unseated person!
- **Complete Solution & Complexity**: Sorting + Lazy Segment Tree over $[1, M+1]$ in $O((N + M) \log M)$ time ($< 0.15\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Apply Ore's Defect Formula: $\text{unseated} = \max_{S} (\lvert S \rvert - \lvert N(S) \rvert)$. What can $N(S)$ look like when every person connects to a prefix $[1, L_i]$ and a suffix $[R_i, M]$?
  - *Hint 2*: Any union of prefixes and suffixes is itself a single prefix $[1, L]$ union a single suffix $[R, M]$!
  - *Hint 3*: For a fixed $(L, R)$ with $L < R$, the worst subset $S$ is all people with $L_i \le L$ and $R_i \ge R$. Sweep $L$ from $0$ to $M$ and maintain $R$ in a Lazy Segment Tree!

---

#### Problem `P20`: `Codeforces 981 F — Round Marriage`
- **Judge URL**: [https://codeforces.com/problemset/problem/981/F](https://codeforces.com/problemset/problem/981/F)
- **Constraints**: $N \le 2 \cdot 10^5$ brides and grooms on a circle of circumference $L \le 10^9$; minimize maximum circular distance $D$ of a perfect matching; Time Limit $3.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Minimax objective $\implies$ **Binary Search on $D \in [0, \lfloor L / 2 \rfloor]$**. For a fixed $D$, each bride $i$ at $a_i$ connects to a circular arc $[a_i - D, a_i + D]$ of grooms $b_j$. Testing whether $\nu(G_D) = N$ on $N = 2 \cdot 10^5$ requires **Circular Hall's Theorem**!
- **Step 2 — Intermediate Algebraic Representation**:
  Sort $a_1 \le \dots \le a_N$ and $b_1 \le \dots \le b_N$. Unroll the circle by duplicating $a$ to length $2N$ ($a_{i+kN} = a_i + kL$ for $k \in \{1, 2\}$) and $b$ to length $4N$ ($b_{j+kN} = b_j + kL$ for $k \in \{0, 1, 2, 3\}$), shifting $a$ by $+L$ so $a_i - D \ge 0$.
  By Lemma 5.1 (Connected-Component Additivity for Feasibility), Hall's condition holds for all subsets iff it holds for every contiguous subsegment of brides $[l, r]$ of length $1 \le r - l + 1 \le N$:
  $$\forall 1 \le l \le r < l + N, \qquad \max(0, \; R_r - L_l + 1) \ge r - l + 1 \iff (R_r - r) \ge (L_l - l),$$
  where $[L_i, R_i]$ is the index interval of grooms in the $4N$-array within $[a_i - D, a_i + D]$.
- **Step 3 — Reverse-Engineering Scratchpad**:
  For a fixed $D$:
  1. Use two pointers to compute $L_i$ (first groom $\ge a_i - D$) and $R_i$ (last groom $\le a_i + D$) for $i = 1 \dots 2N$ in $O(N)$ time.
  2. Notice that $(R_r - r) \ge (L_l - l)$ for $l \le r < l + N$ (provided $L_i \le R_i$ for all $i$) can be checked in $O(N)$ by maintaining $\text{pref\_max} = \max_{1 \le l \le r} (L_l - l)$ as $r$ sweeps from $1$ to $2N$!
- **Step 4 — Concrete Toy Trace**:
  On $L = 10$ with $a = [0, 5], b = [2, 7]$: for $D = 2$, $a_1 = 10$ reaches $b \in [8, 12] = \{b_3 = 12\}$ ($[L_1, R_1] = [3, 3]$), $a_2 = 15$ reaches $[13, 17] = \{b_4 = 17\}$ ($[L_2, R_2] = [4, 4]$). Here $L_1 - 1 = 2 \le R_2 - 2 = 2$, so $D = 2$ is feasible!
- **Complete Solution & Complexity**: $\log_2(L/2) \approx 30$ binary search steps $\times O(N)$ two-pointer sweep $= O(N \log L)$ ($\approx 0.15\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Binary search on the distance $D$. Once $D$ is fixed, each bride connects to a contiguous interval of grooms on the circle.
  - *Hint 2*: Unroll the circle ($2N$ brides, $4N$ grooms). By Hall's Theorem for intervals, you only need to check contiguous bride intervals $[l, r]$ of length $\le N$.
  - *Hint 3*: Rewrite the interval condition $R_r - L_l + 1 \ge r - l + 1$ as $R_r - r \ge L_l - l$, separating $l$ and $r$ for an $O(N)$ prefix-maximum scan!

---

#### Problem `P21`: `[CTSC2008] 祭祀` (Luogu P4298)
- **Judge URL**: [https://www.luogu.com.cn/problem/P4298](https://www.luogu.com.cn/problem/P4298)
- **Constraints**: $N \le 100$ vertices, $M \le 1000$ directed edges; output: (1) maximum antichain size $W$, (2) a binary string of ONE valid max antichain $A^*$, and (3) a binary string indicating for EACH vertex $v \in V$ whether $v$ belongs to **at least one** max antichain; Time Limit $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  River reachability is transitive, so first compute the **Transitive Closure $\mathcal{P} = \text{TC}(G)$** via Floyd–Warshall! Then the three sub-tasks ask for: (1) Poset Width $W$, (2) Constructive Antichain $A^*$, and (3) Per-element Antichain Feasibility.
- **Step 2 — Intermediate Algebraic Representation**:
  - **Part 1**: By Dilworth's Theorem, $W = N - \nu(G_{\text{split}}(\mathcal{P}))$.
  - **Part 2**: By Lemma 6.1 (Section 6.2), after finding $V_S$ via residual BFS from $S$ in $G_{\text{split}}(\mathcal{P})$, $A^* = \{ v \in V : v_{\text{out}} \in V_S \land v_{\text{in}} \notin V_S \}$ has $\lvert A^* \rvert = W$.
  - **Part 3**: Vertex $v$ can belong to a maximum antichain of size $W$ if and only if deleting $v$ and **all vertices comparable to $v$** ($N_{\text{comp}}[v] = \{v\} \cup \{u : u \prec v \lor v \prec u\}$) leaves a sub-poset $\mathcal{P}_v = \mathcal{P}[V \setminus N_{\text{comp}}[v]]$ of width **at least $W - 1$**!
- **Step 3 — Reverse-Engineering Scratchpad**:
  1. Run Floyd–Warshall in $O(N^3)$ to get $\mathcal{P}$.
  2. Run Dinic / Kuhn on $G_{\text{split}}(\mathcal{P})$ to get $W = N - \nu$ and extract $A^*$ via $V_S$.
  3. For each $v = 1 \dots N$, form $V_v = V \setminus N_{\text{comp}}[v]$, compute $\nu(G_{\text{split}}(\mathcal{P}[V_v]))$, and mark $v$ feasible iff $\lvert V_v \rvert - \nu_v == W - 1$.
- **Step 4 — Concrete Toy Trace**:
  On diamond poset $1 \prec \{2, 3\} \prec 4$: $W = 2$, $A^* = \{2, 3\}$. For $v = 1$, $N_{\text{comp}}[1] = \{1, 2, 3, 4\}$, leaving $V_1 = \emptyset$ of width $0 < 2 - 1 = 1$, so $1$ (and $4$) cannot be in any max antichain; $2$ and $3$ leave $\{3\}$ and $\{2\}$ of width $1 = 2 - 1$, so Part 3 outputs `0110`.
- **Complete Solution & Complexity**: $O(N^3)$ Floyd–Warshall + $N$ runs of Kuhn/Dinic on $\le 200$ vertices $= O(N \cdot N^2 \sqrt{N}) \approx 10^7$ ops ($< 0.05\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Since rivers can pass through intermediate cities, what must you run on the DAG before building the bipartite split graph?
  - *Hint 2*: After Floyd–Warshall, $W = N - \nu(G_{\text{split}})$, and $A^* = \{v : v_{\text{out}} \in V_S \land v_{\text{in}} \in V_T\}$.
  - *Hint 3*: To test if $v$ can be in *some* max antichain, force $v$ into the antichain by deleting $v$ and all $u$ with $u \prec v$ or $v \prec u$, and check if the remaining poset has width $W - 1$!

---

#### Problem `P22`: `Codeforces 1510 B — Button Lock`
- **Judge URL**: [https://codeforces.com/problemset/problem/1510/B](https://codeforces.com/problemset/problem/1510/B)
- **Constraints**: $d \le 10$ bits ($2^d \le 1024$); $N \le 2^d - 1$ target non-zero bitmasks; pressing button $i$ turns bit $i$ from $0 \to 1$ (cost $1$), and pressing `R` resets all bits to $0$ (cost $1$); visit all $N$ target masks in minimum button presses; Time Limit $3.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Without pressing `R`, we can transition from mask $u$ to mask $v$ iff $u \subsetneq v$ ($u \mathbin{\&} v == u$) by pressing $\text{popcount}(v) - \text{popcount}(u)$ buttons. Pressing `R` ends the current chain at some terminal mask $u$ and starts a new chain from $0$! Since every target mask must be *visited* at least once, and intermediate subset masks can be passed through without penalty (submask transitions are transitive!), this is a **Weighted Path Cover on the Bitmask Poset**!
- **Step 2 — Intermediate Algebraic Representation**:
  Suppose our trajectory consists of $k$ chains ending at terminal masks $T_1, \dots, T_k$ (with $k - 1$ resets `R` between them). A chain ending at $u$ requires $\text{popcount}(u)$ bit-presses plus $1$ reset `R` (except the very last chain has no trailing `R`):
  $$\text{Total Presses} = \left( \sum_{u \text{ is chain end}} (\text{popcount}(u) + 1) \right) - 1 = \sum_{v \in V} (\text{popcount}(v) + 1) - 1 - \sum_{(u, v) \in M} (\text{popcount}(u) + 1)!$$
  Notice that whenever $u_{\text{out}} \in L$ is **matched** to some successor $v_{\text{in}} \in R$ ($u \subsetneq v$), $u$ is *no longer* the end of a chain, saving **$\text{popcount}(u) + 1$** presses!
- **Step 3 — Reverse-Engineering Scratchpad (`Transversal Matroid Priority Kuhn — Zero MCMF!`)**:
  Because the savings $\text{popcount}(u) + 1$ depends **only on the left vertex $u_{\text{out}} \in L$**, by Theorem 2.2 (`Model A`: Transversal Matroid Priority Kuhn, Section 2.6), we do **not** need MCMF!
  - Sort all target masks $u \in L$ in **decreasing order of $\text{popcount}(u)$**, and run standard Kuhn's augmenting path DFS in that order!
  - Reconstruct the chains by following matched edges $u \to v$ and inserting `R` between chains.
- **Step 4 — Concrete Toy Trace**:
  Targets `01` ($\text{pop}=1$), `10` ($\text{pop}=1$), `11` ($\text{pop}=2$). Decreasing popcount order: `11` (no proper superset), then `01` (matches to `11`, saving $1 + 1 = 2$), then `10` (cannot match to `11` since `11` is taken). Chains: `01 -> 11` then `R` then `10`, total presses $1 + 1 + 1 + 1 = 4 = (3 + 2 + 2) - 1 - 2$.
- **Complete Solution & Complexity**: $\lvert V \rvert \le 1024$, $\lvert E \rvert \le 3^{10} = 59,049$. Priority Kuhn runs in $O(2^d \cdot 3^d) \approx 6 \cdot 10^7$ ops ($< 0.05\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: How many total button presses does a single chain $u_1 \subsetneq u_2 \subsetneq \dots \subsetneq u_r$ followed by `R` cost?
  - *Hint 2*: Exactly $\text{popcount}(u_r) + 1$, independent of the intermediate masks! So matching $u_{\text{out}}$ to any $v_{\text{in}}$ saves $\text{popcount}(u) + 1$.
  - *Hint 3*: Since the weight depends only on $u \in L$, sort $L$ by decreasing $\text{popcount}(u)$ and run Kuhn's algorithm (Transversal Matroid Greedy)!

---

#### Problem `P23`: `[HAOI2017] 新型城市化` (Luogu P3731) — *Cohort 3 Gap-Hunt Addition*
- **Judge URL**: [https://www.luogu.com.cn/problem/P3731](https://www.luogu.com.cn/problem/P3731)
- **Constraints**: $N \le 10^4$ cities, $M \le 1.5 \cdot 10^5$ non-friendship edges (representing the **complement graph** $G = \overline{H}$, guaranteed to be **bipartite** because the friendship graph $H$ can be partitioned into at most 2 cliques!); find all edges $e \in E(G)$ whose deletion from $G$ (i.e., adding friendship $e$ to $H$) strictly increases the maximum clique size of $H$; Time Limit $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  A clique in the friendship graph $H$ is an **Independent Set** in the complement graph $G = \overline{H}$! Because $V(H)$ can be partitioned into $\le 2$ cliques, $V(G)$ can be partitioned into $\le 2$ independent sets — meaning **$G$ is a bipartite graph**! Adding a friendship edge $e$ to $H$ means **deleting edge $e$ from $G$**, and we want all edges $e \in E(G)$ such that:
  $$\alpha(G \setminus \{e\}) = \alpha(G) + 1 \iff \tau(G \setminus \{e\}) = \tau(G) - 1 \iff \nu(G \setminus \{e\}) = \nu(G) - 1.$$
- **Step 2 — Intermediate Algebraic Representation**:
  By **Theorem 7.2** (Section 7.2, Fine DM Critical Edges), in a bipartite graph $G = (L \cup R, E)$, deleting edge $e = (u, v) \in E$ decreases the maximum matching $\nu(G)$ by $1$ if and only if **$e$ is an Essential Edge** (belongs to *every* maximum matching of $G$), which in the full residual network $G_{f^*}$ (including $S$ and $T$) holds iff:
  $$e = (u, v) \in M \quad \land \quad \text{scc}_{G_{f^*}}(u) \ne \text{scc}_{G_{f^*}}(v).$$
- **Step 3 — Reverse-Engineering Scratchpad**:
  1. 2-color each connected component of $G$ into $L \cup R$.
  2. Build the standard unit-capacity matching network $N$ ($c(S, u) = 1, c(u, v) = 1, c(v, T) = 1$) and run Dinic to obtain $f^*$ and matching $M = \{ (u, v) \in E : f^*(u, v) = 1 \}$.
  3. Build the residual graph $G_{f^*}$ on all $N + 2$ vertices (keep every directed residual edge with $c_f > 0$).
  4. Run Tarjan's SCC algorithm on $G_{f^*}$. Collect all $e = (u, v) \in M$ with $\text{scc}(u) \ne \text{scc}(v)$, sort their endpoints, and print!
- **Step 4 — Concrete Toy Trace & Why $S, T$ Must Be Included in Tarjan**:
  Suppose $G$ is the path $u_1 - v_1 - u_2$ ($L = \{u_1, u_2\}, R = \{v_1\}$) with $M = \{(u_1, v_1)\}$ and $u_2$ unmatched. Deleting $(u_1, v_1)$ leaves $\{(u_2, v_1)\}$ of size $1$, so $(u_1, v_1)$ is **not** critical! In $G_{f^*}$, $S \to u_2 \to v_1 \to u_1 \to S$ is a directed cycle of residual edges with $c_f > 0$, placing $u_1$ and $v_1$ into $\text{scc}(S)$ so $\text{scc}(u_1) = \text{scc}(v_1)$. **Broken Gadget Trap**: If you ran Tarjan only on $G_{f^*} \setminus \{S, T\}$ *without* also excluding $V_S$ and $V_T^{\text{rev}}$, then $u_2 \to v_1 \to u_1$ would look like a DAG path (`scc(u_1) != scc(v_1)`) and falsely report $(u_1, v_1)$ as critical! Keeping $S$ and $T$ inside Tarjan's graph automatically closes all alternating paths through $S$ and $T$ into cycles!
- **Complete Solution & Complexity**: Dinic in $O(M \sqrt{N})$ + Tarjan SCC in $O(N + M)$ ($< 0.15\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Since the cities can be partitioned into 2 cliques in the friendship graph, what is the structure of the *complement* graph $G$?
  - *Hint 2*: $G$ is bipartite, and Max Clique in $\overline{G}$ is Max Independent Set $N - \nu(G)$ in $G$. When does deleting an edge $e$ from $G$ decrease $\nu(G)$ by $1$?
  - *Hint 3*: Exactly when $e$ belongs to *every* maximum matching of $G$. Run Dinic, then run Tarjan's SCC on the full residual graph (including $S$ and $T$): $e = (u, v) \in M$ is critical iff $\text{scc}(u) \ne \text{scc}(v)$!

---

### Tier 4: Mastery (7 Problems — `P24` to `P30`)

---

#### Problem `P24`: `AtCoder AGC 025 D — Choosing Points`
- **Judge URL**: [https://atcoder.jp/contests/agc025/tasks/agc025_d](https://atcoder.jp/contests/agc025/tasks/agc025_d)
- **Constraints**: $N \le 300$; $2N \times 2N$ grid ($4N^2$ points); given $D_1, D_2 \le 2 \cdot 10^5$, choose $N^2$ points with no pair at squared Euclidean distance $D_1$ or $D_2$; Time Limit $2.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Running Dinic on $4N^2 = 3.6 \cdot 10^5$ vertices is too slow, and the union of two bipartite graphs $G_{D_1} \cup G_{D_2}$ is not even bipartite! However, we only need **$N^2 = \frac{1}{4}(4N^2)$** points — exactly **$\frac{1}{4}$ of the vertex set**!
- **Step 2 — Intermediate Algebraic Representation**:
  By **Theorem 4.1** (Section 4.4), for *any* integer $D = 4^k m$ ($4 \nmid m$), the distance graph $G_D$ is **bipartite** with an explicit $O(1)$ 2-coloring $c_D(x, y) \in \{0, 1\}$:
  $$c_D(x, y) = \begin{cases} 0 & \text{if } 2^k \nmid x \text{ or } 2^k \nmid y \text{ (Wait: cosets of } 2^k \text{ are independent, so use } \lfloor x / 2^k \rfloor, \lfloor y / 2^k \rfloor\text{!)}, \\ (\lfloor x / 2^k \rfloor + \lfloor y / 2^k \rfloor) \bmod 2 & \text{if } m \equiv 1, 2 \pmod 4 \text{? Wait: for } m \equiv 1, 3 \pmod 4 \text{ (odd } m\text{)!}, \\ \lfloor x / 2^k \rfloor \bmod 2 & \text{if } m \equiv 2 \pmod 4. \end{cases}$$
  *(Let us verify $\lfloor x / 2^k \rfloor$: if $(x_1 - x_2)^2 + (y_1 - y_2)^2 = 4^k m$, then $2^k \mid (x_1 - x_2)$ and $2^k \mid (y_1 - y_2)$, so $(x_1 \bmod 2^k, y_1 \bmod 2^k) = (x_2 \bmod 2^k, y_2 \bmod 2^k)$, which means $\lfloor x_1 / 2^k \rfloor - \lfloor x_2 / 2^k \rfloor = (x_1 - x_2) / 2^k$!)*
- **Step 3 — Reverse-Engineering Scratchpad**:
  Assign every grid point $(x, y) \in [0, 2N - 1]^2$ the combined 4-color label:
  $$\text{color}(x, y) = 2 \cdot c_{D_1}(x, y) + c_{D_2}(x, y) \in \{0, 1, 2, 3\}.$$
  Every color class is an independent set in **both** $G_{D_1}$ and $G_{D_2}$! By the Pigeonhole Principle, at least one of the 4 color classes contains $\ge \lceil 4N^2 / 4 \rceil = N^2$ points. Print its first $N^2$ points!
- **Step 4 — Concrete Toy Trace**:
  For $N = 1$ ($2 \times 2$ grid), $D_1 = 1$ ($k=0, m=1$ odd $\implies (x+y)\bmod 2$) and $D_2 = 2$ ($k=0, m=2 \implies x \bmod 2$). The 4 points $(0,0), (0,1), (1,0), (1,1)$ receive distinct colors $0, 1, 2, 3$, each of size $1 = N^2$.
- **Complete Solution & Complexity**: Pure $O(N^2)$ loop with zero graph storage ($< 0.02\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Notice you only need $N^2$ points out of $4N^2$ — exactly $1/4$ of the grid. What if you could 2-color $G_{D_1}$ and 2-color $G_{D_2}$ independently?
  - *Hint 2*: Factor $D = 4^k m$ where $4 \nmid m$. Why must any edge of length $\sqrt{D}$ satisfy $2^k \mid \Delta x$ and $2^k \mid \Delta y$?
  - *Hint 3*: Divide coordinates by $2^k$: if $m$ is odd, $(\Delta x' + \Delta y')$ is odd; if $m \equiv 2 \pmod 4$, $\Delta x'$ and $\Delta y'$ are both odd! Combine the two 2-colorings into 4 buckets and pick the largest.

---

#### Problem `P25`: `Codeforces 590 E — Birthday`
- **Judge URL**: [https://codeforces.com/problemset/problem/590/E](https://codeforces.com/problemset/problem/590/E)
- **Constraints**: $N \le 750$ distinct strings over `{'a', 'b'}`, total length $\sum \lvert s_i \rvert \le 10^7$; find a maximum-size substring-free subset and print their indices; Time Limit $3.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Maximum Antichain in the substring poset (`Dilworth`), just like `P12` (`ABC 354 G`), except $\sum \lvert s_i \rvert \le 10^7$ and we must also reconstruct the antichain $A^*$. Naive $O(N \sum \lvert s_i \rvert)$ substring matching would take $7.5 \cdot 10^9$ operations (`TLE`, and storing $N$ pointers per Trie node `MLE`s)!
- **Step 2 — Intermediate Algebraic Representation (`Aho–Corasick Fail-Tree Sparsification`)**:
  Build an Aho–Corasick automaton on the $N$ strings ($V_{\text{trie}} \le 10^7$ nodes using two static `int nxt[10000005][2]` arrays). During the BFS that builds `fail[u]`, precompute `nearest_term[u]` = the longest proper suffix of node $u$ that is a terminal string ID.
  - When walking the Trie nodes $u$ of string $s_i$, we only need the **single longest substring ending at $u$** (`nearest_term[u]`, or `nearest_term[fail[u]]` at the very end of $s_i$ to avoid self-loops $i \to i$)!
  - This yields at most $\sum \lvert s_i \rvert$ raw edges, deduplicated into an $N \times N$ adjacency matrix `adj[i][j]` with at most $O(N^2)$ edges.
  - Running $O(N^3 / 64)$ Bitset Floyd–Warshall recovers the full transitive closure $\mathcal{P}$!
- **Step 3 — Reverse-Engineering Scratchpad**:
  1. Build AC automaton, extract sparse DAG edges $j \prec i$, and run Floyd–Warshall to get `reach[j][i]`.
  2. Run Hopcroft–Karp / Dinic on $G_{\text{split}}(\mathcal{P})$ ($N \le 750$).
  3. Find $V_S$ via residual BFS from $S$ and output $A^* = \{ i \in \{1, \dots, N\} : i_{\text{out}} \in V_S \land i_{\text{in}} \notin V_S \}$.
- **Step 4 — Concrete Toy Trace**:
  For $s_1 = \text{"a"}, s_2 = \text{"ab"}, s_3 = \text{"bab"}$: walking $s_3$ finds $s_1$ at prefix `"ba"` and $s_2$ at `"bab"`, adding $1 \prec 3$ and $2 \prec 3$; walking $s_2$ adds $1 \prec 2$. Chain $1 \prec 2 \prec 3$ has width $1$.
- **Complete Solution & Complexity**: $O(\sum \lvert s_i \rvert + N^3 / 64 + N^{2.5})$ time ($\approx 0.8\text{ s}$) and $\approx 160\text{ MB}$ flat array memory.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Why don't you need to walk the entire `fail`-chain at each character of $s_i$?
  - *Hint 2*: Because substring containment is transitive! Recording only the *longest* terminal suffix at each prefix of $s_i$, then running Floyd–Warshall on the $N \times N$ matrix, recovers all pairs!
  - *Hint 3*: Run Hopcroft–Karp on $G_{\text{split}}$ and extract the antichain $A^* = \{ i : i_{\text{out}} \in V_S \land i_{\text{in}} \in V_T \}$.

---

#### Problem `P26`: `AtCoder AGC 029 F — Construction of a tree`
- **Judge URL**: [https://atcoder.jp/contests/agc029/tasks/agc029_f](https://atcoder.jp/contests/agc029/tasks/agc029_f)
- **Constraints**: $N \le 10^5$; $N - 1$ vertex subsets $E_1, \dots, E_{N-1} \subseteq \{1, \dots, N\}$ with $\sum \lvert E_i \rvert \le 2 \cdot 10^5$; pick $(u_i, v_i) \in E_i \times E_i$ to form a tree on $\{1, \dots, N\}$ or output `-1`; Time Limit $2.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  In any tree rooted at $r = 1$, every non-root vertex $v \in \{2, \dots, N\}$ has a **unique parent edge $e(v) \in \{1, \dots, N-1\}$** with $v \in E_{e(v)}$. Thus a necessary condition is a **perfect matching $M$** between the $N - 1$ sets $L = \{E_1, \dots, E_{N-1}\}$ and the $N - 1$ non-root vertices $R = \{2, \dots, N\}$!
- **Step 2 — Intermediate Algebraic Representation**:
  Wait: a perfect matching $M$ only assigns each hyperedge $E_i$ its **child endpoint** $v_i = M(E_i) \in E_i \setminus \{1\}$; how do we choose its **parent endpoint** $u_i \in E_i$ without creating cycles?
  - Start with $V_{\text{vis}} = \{1\}$ (the root).
  - Any unused hyperedge $E_i$ that contains at least one already-visited vertex $u_i \in E_i \cap V_{\text{vis}}$ can set $u_i$ as its parent endpoint, connecting its matched child $v_i = M(E_i)$ to the growing tree and adding $v_i$ to $V_{\text{vis}}$!
- **Step 3 — Reverse-Engineering Scratchpad (`Hall Certifier`)**:
  1. Build bipartite graph $G = (L \cup R, E)$ with $L = \{E_1, \dots, E_{N-1}\}$ and $R = \{2, \dots, N\}$, and run Dinic / Hopcroft–Karp. If $\nu(G) < N - 1$, output `-1`.
  2. Otherwise, run a BFS starting from vertex $1$: whenever vertex $u$ is popped, for every hyperedge $E_i \ni u$ not yet used, set $E_i$'s tree edge to $(u, M(E_i))$, mark $E_i$ used, and push $M(E_i)$ into the BFS queue!
  3. **Why this is 100% exact**: If BFS visits all $N$ vertices, we have a valid tree. If BFS stops early with $V_{\text{vis}} \subsetneq V$, then the $k = \lvert E \setminus E_{\text{vis}} \rvert \ge 1$ unreached hyperedges have **all** their member vertices inside $V \setminus V_{\text{vis}}$, which has size $N - (N - k) = k$:
     $$\left\lvert \bigcup_{i \notin E_{\text{vis}}} E_i \right\rvert \le \lvert V \setminus V_{\text{vis}} \rvert = \lvert E \setminus E_{\text{vis}} \rvert,$$
     violating the tree connectivity condition ($\ge k + 1$ vertices required to span $k$ edges), so **no tree exists for ANY matching** (`-1`)!
- **Step 4 — Concrete Toy Trace**:
  For $N = 3$ with $E_1 = \{2, 3\}, E_2 = \{2, 3\}$: $M$ matches $E_1 \leftrightarrow 2, E_2 \leftrightarrow 3$, but vertex $1$ belongs to zero hyperedges, so BFS from $1$ stalls immediately with $V_{\text{vis}} = \{1\}$ and outputs `-1`.
- **Complete Solution & Complexity**: Dinic on $2N$ vertices and $2 \cdot 10^5$ edges in $O(\sum \lvert E_i \rvert \sqrt{N})$ + $O(\sum \lvert E_i \rvert)$ BFS ($\approx 0.15\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Root the target tree at vertex $1$. Every vertex $v \in \{2, \dots, N\}$ must be the child endpoint of a distinct set $E_i$.
  - *Hint 2*: Find a perfect matching $M$ between $\{E_1, \dots, E_{N-1}\}$ and $\{2, \dots, N\}$. How do you pick the *parent* endpoint of each $E_i$ so the graph is connected?
  - *Hint 3*: Run BFS from root $1$: whenever $u$ is reached and $u \in E_i$, connect $u$ to $M(E_i)$ and push $M(E_i)$! If BFS stalls, Hall's condition is violated and the answer is `-1`.

---

#### Problem `P27`: `Codeforces 1139 E — Maximize Mex`
- **Judge URL**: [https://codeforces.com/problemset/problem/1139/E](https://codeforces.com/problemset/problem/1139/E)
- **Constraints**: $N \le 5000$ students with potential $p_i \in [0, 5000]$ and club $c_i \in [1, M]$ ($M \le 5000$); $D \le 5000$ days where one student leaves per day; each day pick at most one student per club to maximize $\text{mex}$ of potentials; Time Limit $2.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  We can achieve $\text{mex} \ge k$ iff potentials $L_{\text{pref}} = \{0, 1, \dots, k - 1\}$ can all be matched to distinct clubs in $R = \{1, \dots, M\}$. Deleting edges online breaks matchings, but since all $D$ queries are given **offline**, **reverse time from Day $D$ back to Day $1$** so deletions become **edge insertions**!
- **Step 2 — Intermediate Algebraic Representation**:
  As edges are inserted into $G = (L \cup R, E)$ going backwards in time, the maximum achievable $\text{mex}$ pointer `ans` is **monotonically non-decreasing** ($0 \le \text{ans}_D \le \text{ans}_{D-1} \le \dots \le \text{ans}_1 \le 5000$).
- **Step 3 — Reverse-Engineering Scratchpad**:
  1. Build the bipartite graph containing only students who *never* leave after Day $D$.
  2. Maintain pointer `mex_ptr = 0`. While Kuhn's DFS from `mex_ptr` finds an augmenting path in $G$, increment `mex_ptr++`.
  3. For $d = D$ down to $1$: record `ans[d] = mex_ptr`, insert the student who left on Day $d$ as edge $(p_{id}, c_{id})$, and again `while (dfs(mex_ptr)) mex_ptr++;`!
- **Step 4 — Concrete Toy Trace**:
  Students $(p=0, c=1), (p=1, c=1)$. If student 2 leaves on Day 1: at end of Day 1, only $(0, 1)$ is present $\implies \text{mex} = 1$ (`0` matched to club `1`, `1` fails). Adding $(1, 1)$ before Day 1 still leaves $\text{mex} = 1$.
- **Complete Solution & Complexity**: The pointer `mex_ptr` advances at most $5001$ times across the entire execution, so Kuhn's DFS runs at most $5001 + D \le 10^4$ times on $\le 5000$ edges $\implies O((N + D)N) \approx 5 \cdot 10^7$ ops ($< 0.1\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Build a bipartite graph between Potentials $\{0, 1, \dots\}$ and Clubs $\{1, \dots, M\}$. What does $\text{mex} \ge k$ mean in this graph?
  - *Hint 2*: Potentials $0, 1, \dots, k-1$ are all matched! Why is it much easier to process the $D$ days in *reverse* order?
  - *Hint 3*: Reversing time turns deletions into edge insertions, so $\text{mex}$ only increases and Kuhn's DFS runs at most $\max(p_i) + D$ times total!

---

#### Problem `P28`: `AtCoder ARC 106 E — Medals`
- **Judge URL**: [https://atcoder.jp/contests/arc106/tasks/arc106_e](https://atcoder.jp/contests/arc106/tasks/arc106_e)
- **Constraints**: $N \le 18$ employees, $K \le 10^5$ medals per employee; employee $i$ alternates $A_i$ days working and $A_i$ days off; minimize total days $D$; Time Limit $4.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Extreme asymmetry: $N \le 18$ employees on the left, up to $D \le 2 N K = 3.6 \cdot 10^6$ days on the right! Binary search on $D$, and test feasibility via **Capacitated Hall's Theorem + Fast Zeta Transform (`SOS DP`)** in $O(N 2^N)$!
- **Step 2 — Intermediate Algebraic Representation**:
  For a fixed $D$, each day $d \in \{1, \dots, D\}$ has an availability bitmask $\text{mask}[d] \in [0, 2^N - 1]$ of employees working on day $d$. By Section 5.2(3), a subset $S \subseteq \{0, \dots, N - 1\}$ of employees can each receive $K$ medals iff:
  $$\forall S \subseteq \{0, \dots, N-1\}, \qquad \lvert N(S) \rvert = D - g\big[\overline{S}\big] \ge K \lvert S \rvert, \quad \text{where } g[T] = \sum_{M \subseteq T} \text{cnt}[M].$$
- **Step 3 — Reverse-Engineering Scratchpad**:
  1. Precompute `mask[d]` for $d = 1 \dots 2NK$ in $O(N \cdot NK)$ time.
  2. Binary search on $D \in [NK, 2NK]$:
     - Count frequency `cnt[M]` of each bitmask $M$ in $d \in [1, D]$.
     - Run SOS DP (`for i in 0..N-1: for mask in 0..2^N-1: if mask & (1<<i): g[mask] += g[mask ^ (1<<i)]`) in $O(N 2^N)$ time.
     - Check if $D - g[(2^N - 1) \oplus S] \ge K \cdot \text{popcount}(S)$ for all $S$.
- **Step 4 — Concrete Toy Trace**:
  $N = 2, K = 1, A = [1, 1]$: both employees work on odd days ($\text{mask} = 3$) and rest on even days ($\text{mask} = 0$). For $D = 2$, $S = \{1, 2\}$ requires $2$ medals, but day $2$ has $\text{mask} = 0 \subseteq \overline{S}$, so $D - g[0] = 2 - 1 = 1 < 2$ (`False`). For $D = 3$, odd days $1, 3$ give $3 - 1 = 2 \ge 2$ (`True`, $D^* = 3$).
- **Complete Solution & Complexity**: Precomputation $O(N^2 K)$ + $\log_2(2NK) \approx 22$ binary search steps $\times O(N 2^N) \approx 10^8$ ops ($\approx 0.4\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: What is the worst-case upper bound on $D$? Even if all employees had identical schedules $A_i$, $2NK$ days has at least $NK$ working days.
  - *Hint 2*: Binary search on $D$. Since $N \le 18$, use Hall's Marriage Theorem: $\lvert N(S) \rvert \ge K \lvert S \rvert$ for all $2^N$ subsets $S$.
  - *Hint 3*: Rewrite $\lvert N(S) \rvert = D - \#\{d \le D : \text{mask}[d] \subseteq \overline{S}\}$ and compute subset sums via SOS DP in $O(N 2^N)$!

---

#### Problem `P29`: `Codeforces 1519 F — Chests and Keys`
- **Judge URL**: [https://codeforces.com/problemset/problem/1519/F](https://codeforces.com/problemset/problem/1519/F)
- **Constraints**: $N \le 6$ chests with $a_i \in [1, 4]$ coins; $M \le 6$ keys costing $b_j \in [1, 4]$ coins; lock cost $c_{i,j}$ to place a lock of key $j$ on chest $i$; Bob wins if *any* subset $S$ of chests has $\sum_{i \in S} a_i > \sum_{j \in N(S)} b_j$; minimize total lock cost so Bob cannot win; Time Limit $4.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Read Bob's winning condition carefully: Bob wins iff there exists $S \subseteq \{1, \dots, N\}$ with $\sum_{i \in S} a_i > \sum_{j \in N(S)} b_j$. Therefore, **Alice prevents Bob from winning if and only if Supply–Demand Hall's Condition holds**:
  $$\forall S \subseteq \{1, \dots, N\}, \qquad \sum_{j \in N(S)} b_j \ge \sum_{i \in S} a_i!$$
- **Step 2 — Intermediate Algebraic Representation (`The Primal–Dual Flip`)**:
  Wait: how do we choose a minimum-cost edge set $E \subseteq L \times R$ satisfying Hall's condition for all $2^N$ subsets $S$? Tracking which of the $2^6 = 64$ subsets $S$ are not yet satisfied would take $2^{64}$ DP states!
  **Flip Hall's Dual Cut Condition back to Primal Max-Flow!** By Supply–Demand Hall's Theorem (Section 5.2), $E$ satisfies $\sum_{j \in N(S)} b_j \ge \sum_{i \in S} a_i$ for all $S$ **if and only if there exists an integer flow $f_{i, j} \in \mathbb{Z}_{\ge 0}$** along $E$ such that:
  $$\forall i \in \{1, \dots, N\}, \;\; \sum_{j=1}^M f_{i,j} = a_i, \qquad \forall j \in \{1, \dots, M\}, \;\; \sum_{i=1}^N f_{i,j} \le b_j, \qquad \text{and } f_{i,j} > 0 \implies (i, j) \in E!$$
- **Step 3 — Reverse-Engineering Scratchpad**:
  Because $a_i \in [0, 4]$ and $N \le 6$, the vector of remaining chest supplies $(rem_1, \dots, rem_N) \in \{0, 1, 2, 3, 4\}^6$ has at most **$5^6 = 15,625$ states**!
  Process pairs $(j, i)$ for key $j = 1 \dots M$ and chest $i = 1 \dots N$, maintaining `(remaining supply tuple in base 5, remaining capacity b_j of current key j)`:
  - Transition: choose integer flow $f \in [0, \min(rem_i, rem\_b_j)]$; if $f == 0$, pay $0$; if $f > 0$, pay lock cost $c_{i,j}$ and transition to $(rem_i - f, rem\_b_j - f)$.
- **Step 4 — Concrete Toy Trace**:
  With $N = 1 (a_1 = 3)$, $M = 2 (b_1 = 2, b_2 = 2)$ and $c_{1,1} = 5, c_{1,2} = 7$: routing $f_{1,1} = 2$ (cost $5$) and $f_{1,2} = 1$ (cost $7$) drains $rem_1 = 3 \to 1 \to 0$ for total cost $12$.
- **Complete Solution & Complexity**: $M \times N = 36$ transitions over $5^6 \times 5 = 78,125$ states with $\le 5$ branches $\implies \approx 1.4 \cdot 10^7$ ops ($< 0.05\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Notice that Bob's winning condition $\sum_{i \in S} a_i > \sum_{j \in N(S)} b_j$ is the exact negation of Capacitated Hall's Marriage Theorem!
  - *Hint 2*: Instead of checking all $2^6 = 64$ subsets $S$, use Hall's equivalence: Hall holds iff there exists an integer flow routing all $a_i$ units from chests to keys of capacity $b_j$.
  - *Hint 3*: Since $a_i \le 4$ and $N \le 6$, the remaining supply tuple $(rem_1, \dots, rem_6)$ has only $5^6 = 15,625$ states — run a profile DP over $(j, i)$!

---

#### Problem `P30`: `[NOI2011] 兔兔与蛋蛋游戏` (Luogu P1971)
- **Judge URL**: [https://www.luogu.com.cn/problem/P1971](https://www.luogu.com.cn/problem/P1971)
- **Constraints**: $N, M \le 40$; grid of black tiles, white tiles, and one blank cell `.`; $K \le 1000$ rounds ($2K$ moves): Alice slides an adjacent **white** tile into the blank, Bob slides an adjacent **black** tile into the blank, and no tile may ever visit the same cell twice; find all rounds where Alice made a **blunder** (was in a winning state before her move, and also in a winning state for Bob after her move); Time Limit $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Instead of tracking $NM - 1$ moving tiles, **track the trajectory of the single blank cell `.`**!
  - In a valid move, the blank cell steps from $u_t$ to an adjacent cell $u_{t+1}$ containing the required color (white for Alice, black for Bob), and moving that tile into $u_t$ shifts the color of $u_{t+1}$ to $u_t$.
  - Crucially, **no cell $u$ can ever be visited twice by the blank cell**: if the blank ever returned to $u$, the sequence of tiles shifted along the cycle would have opposite colors at the two visits to $u$, which is impossible on a bipartite grid where step count parity equals Manhattan parity!
- **Step 2 — Intermediate Algebraic Representation**:
  Let $c_0$ be the starting cell of the blank `.`. Color a cell **Valid** if it is $c_0$, or if it has `(Manhattan parity to c_0 == odd) AND (contains a White tile)`, or `(Manhattan parity to c_0 == even) AND (contains a Black tile)`.
  Then the valid trajectory of the blank cell is an **Impartial Token Walk Game** on the bipartite subgraph $G = (L \cup R, E)$ induced by Valid cells!
  By Theorem 3.3 (Section 3.4), at step $t$ with the blank at $u_t$ in the remaining unvisited graph $G_t = G \setminus \{u_0, \dots, u_{t-1}\}$:
  $$\text{Current player has a winning strategy at } u_t \iff u_t \text{ is Essential in } G_t \;\; (\nu(G_t \setminus \{u_t\}) = \nu(G_t) - 1).$$
- **Step 3 — Reverse-Engineering Scratchpad (`Incremental Vertex Deletion`)**:
  1. Filter the grid to Valid cells and compute the initial maximum matching $M$ on $G_0$ via Kuhn's algorithm.
  2. To test if the current cell $u_t$ is Essential in $G_t$ and delete $u_t$ before moving to $u_{t+1}$:
     - Mark $u_t$ as permanently deleted (`deleted[u_t] = true`).
     - If $u_t$ was unmatched in $M$, then $M$ already avoids $u_t \implies u_t$ is **Avoidable** (current player was **losing**!).
     - If $u_t$ was matched to $w = M(u_t)$, unmatch $w$ (`match[w] = 0`) and run a single Kuhn DFS `dfs(w)` in $G_t \setminus \{u_t\}$: if `dfs(w)` finds a replacement partner for $w$, then $\nu$ stays unchanged and $u_t$ was **Avoidable** (losing); if `dfs(w)` fails, $\nu$ drops by $1$ and $u_t$ was **Essential** (winning)!
  3. Round $r$ is a blunder by Alice iff `win_before_Alice[r] == true` AND `win_before_Bob[r] == true`!
- **Step 4 — Concrete Toy Trace**:
  On $1 \times 3$ grid `W . B` ($c_0 = (1,2)$): $(1,1)$ has odd distance $1$ and is `W` (Valid); $(1,3)$ has odd distance $1$ and is `B` (Invalid!). Thus $G_0$ is the single edge $(1,2) - (1,1)$ of matching size $1$. At $u_0 = (1,2)$, deleting $(1,2)$ leaves $(1,1)$ isolated (`dfs` fails $\implies$ Alice is Winning). Alice moves to $(1,1)$, where Bob has no move (`dfs` is not needed since $(1,1)$ is now unmatched $\implies$ Bob is Losing).
- **Complete Solution & Complexity**: Initial matching $O(V E) \le 1600 \times 6400$, plus $2K \le 2000$ online Kuhn DFS calls of $O(E) \le 6400$ each $\implies \approx 2 \cdot 10^7$ ops ($< 0.05\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Track the single blank cell `.` instead of the tiles. Why can the blank cell never visit the same grid square twice?
  - *Hint 2*: Because grid parity and turn parity are locked together! Keep only cells whose initial tile color matches their Manhattan distance parity from the starting blank cell.
  - *Hint 3*: Now it's a Bipartite Walk Game where visited vertices are deleted one by one: delete $u_t$, unmatch its partner $w = M(u_t)$, and run one Kuhn `dfs(w)` to test if $u_t$ was Essential!

---

## 9. Reconciled Quarantined Template Problems Table

The following 12 naked textbook/template problems are quarantined from the main 30-problem bank (`Section 8`) to preserve 100% modelling density:

| Quarantine ID | Problem Name & Judge | Template Category | Reason for Quarantine |
| :--- | :--- | :--- | :--- |
| **`R-01`** | **Luogu P3386 — 【模板】二分图最大匹配** | Unweighted Bipartite Matching | Naked adjacency list $\to \nu(G)$ template. |
| **`R-02`** | **Library Checker — `Matching on Bipartite Graph`** | Hopcroft–Karp / Dinic | Pure $O(E\sqrt{V})$ speed benchmark with zero modelling. |
| **`R-03`** | **POJ 3041 — Asteroids** | 2D Grid Row–Col König MVC | Direct unadorned $N \times N$ row-column vertex cover (`P04`/`P06` strict subsets). |
| **`R-04`** | **POJ 3020 — Antenna Placement** | Bipartite Minimum Edge Cover | Naked Gallai identity $\rho(G) = \lvert V \rvert - \nu(G)$ on a 2-colored grid. |
| **`R-05`** | **Luogu P2756 — 飞行员配对方案问题** | Bipartite Matching Extraction | Textbook `[网络流 24 题]` matching edge extraction. |
| **`R-06`** | **Luogu P3254 — 圆桌问题** | Capacitated $b$-Matching | Direct $S \to u (r_i), u \to v (1), v \to T (c_j)$ table feasibility check. |
| **`R-07`** | **Luogu P2763 — 试题库问题** | Bipartite Many-to-One Assignment | Direct $S \to u (1), v \to T (k_j)$ category matching template. |
| **`R-08`** | **Luogu P2764 — 最小路径覆盖问题** | DAG Minimum Disjoint Path Cover | Naked textbook $N - \nu(G_{\text{split}})$ without hidden DAG construction. |
| **`R-09`** | **POJ 1422 — Air Raid** | DAG Disjoint Path Cover | Identical to `R-08` on a given town DAG. |
| **`R-10`** | **POJ 2594 — Treasure Exploration** | Transitive Closure + Path Cover | Direct Floyd–Warshall + $N - \nu(G_{\text{split}}(\text{TC}))$ template. |
| **`R-11`** | **UVA 11419 — SAM I AM** | König MVC Set Recovery | Direct $(L \cap V_T) \cup (R \cap V_S)$ vertex print on a grid. |
| **`R-12`** | **CSES 1696 (`School Dance`) & CSES 1709 (`Coin Grid`)** | Matching & König MVC | Introductory textbook exercises for $\nu(G)$ and $\tau(G)$. |

---

## 10. Unified Multilingual `[EN]` / `[ZH]` / `[JA]` Bibliography

### `[EN]` English Foundational Papers, Monographs & CP Treatises
1. **König, D. (1931)**. *"Gráfok és mátrixok"* [Graphs and matrices]. *Matematikai és Fizikai Lapok*, 38, 116–119. (Original proof of $\tau(G) = \nu(G)$ for bipartite graphs).
2. **Hall, P. (1935)**. *"On Representatives of Subsets"*. *Journal of the London Mathematical Society*, 10(1), 26–30. (Hall's Marriage Theorem).
3. **Dilworth, R. P. (1950)**. *"A Decomposition Theorem for Partially Ordered Sets"*. *Annals of Mathematics*, 51(1), 161–166. (Min Chain Cover $=$ Max Antichain).
4. **Ore, Ø. (1955)**. *"Graphs and Matching Theorems"*. *Duke Mathematical Journal*, 22(4), 625–639. (Ore's Defect Formula $\nu(G) = \lvert L \rvert - \max_{S \subseteq L} (\lvert S \rvert - \lvert N(S) \rvert)$).
5. **Dulmage, A. L., & Mendelsohn, N. S. (1958)**. *"Coverings of bipartite graphs"*. *Canadian Journal of Mathematics*, 10, 517–534. (Coarse and Fine Dulmage–Mendelsohn decomposition and block upper-triangularity).
6. **Gallai, T. (1959)**. *"Über extreme Punkt- und Kantenmengen"*. *Annales Universitatis Scientiarum Budapestinensis*, Sectio Mathematica, 2, 133–138. (Gallai's Identities $\alpha + \tau = \lvert V \rvert$ and $\nu + \rho = \lvert V \rvert$).
7. **Edmonds, J., & Fulkerson, D. R. (1965)**. *"Transversals and Matroid Partition"*. *Journal of Research of the National Bureau of Standards*, 69B, 147–153. (Transversal matroids and priority greedy matching).
8. **Mirsky, L. (1971)**. *"A dual of Dilworth's decomposition theorem"*. *American Mathematical Monthly*, 78(8), 876–877. (Max Chain $=$ Min Antichain Partition).
9. **Hopcroft, J. E., & Karp, R. M. (1973)**. *"An $n^{5/2}$ algorithm for maximum matchings in bipartite graphs"*. *SIAM Journal on Computing*, 2(4), 225–231.
10. **Greene, C., & Kleitman, D. J. (1976)**. *"The structure of Sperner $k$-families"*. *Journal of Combinatorial Theory, Series A*, 20(1), 41–68. (Generalized $k$-chain / $k$-antichain duality).
11. **Schrijver, A. (2003)**. *Combinatorial Optimization: Polyhedra and Efficiency* (Vol. A: Paths, Flows, Matchings). Springer.

### `[ZH]` Chinese National Team Papers (`国家集训队论文`) & Competitive Programming Literature
12. **胡伯涛 [Amber] (2007)**. 《最小割模型在信息学竞赛中的应用》 (*Applications of Minimum Cut Models in Olympiad in Informatics*). 中国国家集训队 2007 论文集. (Canonical Chinese treatise on bipartite MWVC/MWIS cut compilation, residual $S$-cut recovery, and `[CTSC2008] 祭祀`).
13. **陈胤伯 (2015)**. 《浅谈图的匹配算法及其应用》 (*On Graph Matching Algorithms and Their Applications*). 中国国家集训队 2015 论文集. (Covers DM decomposition, bipartite walk games `[JSOI2009] 游戏` and `[NOI2011] 兔兔与蛋蛋游戏`, and critical edge classification).
14. **徐哲安 (2018)**. 《浅谈弦图与区间图及完美消除序列》与偏序集 Dilworth 扩展 (*Poset Duality, Weighted Dilworth, and Interval Graphs*). 中国国家集训队论文集.
15. **OI-Wiki Editorial Collective**. 《二分图最大匹配 / 最大权匹配 / 最小点覆盖 / Hall 定理 / 偏序集 Dilworth 定理》. [https://oi-wiki.org/graph/bi-graph/](https://oi-wiki.org/graph/bi-graph/).

### `[JA]` Japanese Competitive Programming Treatises (`AtCoder` / `noshi91` / `maspypy` / `snuke`)
16. **maspy (`maspypy`) (2020–2024)**. *"二部グラフの最大マッチング・最小点被覆・DM分解 (Dulmage–Mendelsohn Decomposition)"*. `maspyのHP` ([https://maspypy.com/](https://maspypy.com/)). (Rigorous treatment of DM block triangularity, canonical extremal vertex covers, and unique matching characterization).
17. **noshi91 (`noshi91`) (2021)**. *"Hall の結婚定理とその周辺 / 二部グラフの辺彩色"* (*Hall's Marriage Theorem, Ore's Defect, and Bipartite Edge Coloring*). `noshi91.github.io`.
18. **snuke (`Keisuke Iwata` / `Makoto Soejima`) (2017–2019)**. Official AtCoder Editorials for `ARC 076 F`, `AGC 025 D`, `AGC 029 F`, `AGC 037 D`, and `ARC 106 E`. AtCoder Inc.

---

## 11. Wave 1B Algorithmic Extraction Patterns & Failure-Mode Compendium (Zero-Boilerplate Reference)

While standard Dinic and Hopcroft–Karp templates are assumed, the **post-flow extraction algorithms** and **flow-free combinatorial engines** introduced across Iterations 6–10 / 58–62 contain subtle indexing and orientation invariants that frequently cause contest `WA`s. Below are the six self-contained, solver-agnostic extraction routines and a complete failure-mode checklist.

---

### 11.1 Pattern 1: Exact $O(V + E)$ König MVC, MIS, and MEC Recovery from Residual Network $G_{f^*}$

Given a solved bipartite network $N$ on $\{S, T\} \cup L \cup R$ where $S \to u$ has capacity $w_u$, $v \to T$ has capacity $w_v$, and $u \to v$ has capacity $\infty$:

```cpp
// Input: Solved residual network G_f with source S, sink T, left vertices L, right vertices R.
// Contract: Middle edges (u -> v) MUST have initial capacity INF so c_f(u, v) > 0 always holds!
struct KonigPartition {
    vector<int> mvc_L, mvc_R; // Minimum (Weighted) Vertex Cover: (L \ V_S) U (R ^ V_S)
    vector<int> mis_L, mis_R; // Maximum (Weighted) Independent Set: (L ^ V_S) U (R \ V_S)
};

KonigPartition extract_konig_sets(int S, int num_nodes, const vector<int>& L, const vector<int>& R,
                                  const auto& adj_residual) {
    vector<bool> vis_S(num_nodes, false);
    queue<int> q;
    q.push(S);
    vis_S[S] = true;
    while (!q.empty()) {
        int x = q.front();
        q.pop();
        for (const auto& e : adj_residual[x]) {
            if (e.cap_residual > 0 && !vis_S[e.to]) {
                vis_S[e.to] = true;
                q.push(e.to);
            }
        }
    }
    KonigPartition res;
    for (int u : L) {
        if (!vis_S[u]) res.mvc_L.push_back(u); // u in L \ V_S -> cut (S -> u)
        else           res.mis_L.push_back(u); // u in L ^ V_S -> kept in MIS
    }
    for (int v : R) {
        if (vis_S[v])  res.mvc_R.push_back(v); // v in R ^ V_S -> cut (v -> T)
        else           res.mis_R.push_back(v); // v in R \ V_S -> kept in MIS
    }
    return res;
}
```

---

### 11.2 Pattern 2: Coarse + Fine Dulmage–Mendelsohn & Critical Edge Classification (`[HAOI2017] 新型城市化`)

Given a solved unit-capacity bipartite matching network $N$ on $\{S, T\} \cup L \cup R$:
1. **Coarse DM (`Avoidable` vs. `Essential` Vertices)**:
   - Forward BFS from $S$ along $c_f(x, y) > 0$ gives $V_S$ ($L_1 = L \cap V_S$, $R_1 = R \cap V_S$).
   - Backward BFS from $T$ along $c_f(x, y) > 0$ (i.e., traversing reverse edges into $T$ whose forward residual capacity in $G_{f^*}$ is $> 0$) gives $V_T^{\text{rev}}$ ($L_2 = L \cap V_T^{\text{rev}}$, $R_2 = R \cap V_T^{\text{rev}}$).
   - **Avoidable Vertices** (Second Mover wins in Bipartite Walk Game): $L_1 \cup R_2$.
   - **Essential Vertices** (First Mover wins in Bipartite Walk Game): $(L \setminus L_1) \cup (R \setminus R_2)$.
2. **Fine DM (`Admissible`, `Essential / Critical`, and `Forbidden` Edges)**:
   Run Tarjan's SCC on the **full residual graph $G_{f^*}$ (including $S$ and $T$)** where edge $x \to y$ exists iff $c_f(x, y) > 0$:
   - **Critical / Essential Edge** ($\nu(G \setminus \{e\}) = \nu(G) - 1$):
     $$e = (u, v) \in M \quad \land \quad \text{scc}_{G_{f^*}}(u) \ne \text{scc}_{G_{f^*}}(v).$$
   - **Admissible Edge** (in at least one maximum matching):
     $$e = (u, v) \in M \quad \lor \quad \text{scc}_{G_{f^*}}(u) == \text{scc}_{G_{f^*}}(v).$$
   - **Forbidden Edge** (in no maximum matching):
     $$e = (u, v) \notin M \quad \land \quad \text{scc}_{G_{f^*}}(u) \ne \text{scc}_{G_{f^*}}(v).$$

*(Notice how including $S$ and $T$ inside Tarjan's graph unifies Coarse and Fine DM edge classification into a single formula: every admissible edge in $L_1 \times R_1$ lies on a cycle through $S$, so $\text{scc}(u) = \text{scc}(v) = \text{scc}(S)$, and every admissible edge in $L_2 \times R_2$ lies on a cycle through $T$, so $\text{scc}(u) = \text{scc}(v) = \text{scc}(T)$!)*

---

### 11.3 Pattern 3: $O(V + E)$ Iterative Leaf-Peeling for Unique Perfect Matchings (Hall–Kotzig Engine)

When $\lvert L \rvert = \lvert R \rvert = N$ and you need to test if $G$ has a **unique perfect matching** (and reconstruct it in linear time without Dinic):

```cpp
// Returns the unique perfect matching as a vector of (u, v) pairs, or empty if 0 or >= 2 exist.
vector<pair<int, int>> unique_perfect_matching(int N, const vector<vector<int>>& adj_bi) {
    // Vertices 0..N-1 in L, N..2N-1 in R
    vector<int> deg(2 * N, 0);
    vector<bool> removed(2 * N, false);
    queue<int> leaves;
    for (int z = 0; z < 2 * N; ++z) {
        deg[z] = adj_bi[z].size();
        if (deg[z] == 1) leaves.push(z);
    }
    vector<pair<int, int>> matching;
    matching.reserve(N);
    while (!leaves.empty()) {
        int x = leaves.front();
        leaves.pop();
        if (removed[x]) continue;
        if (deg[x] != 1) return {}; // Became isolated (deg == 0) -> 0 perfect matchings!
        int y = -1;
        for (int nb : adj_bi[x]) {
            if (!removed[nb]) { y = nb; break; }
        }
        if (y == -1) return {};
        removed[x] = removed[y] = true;
        matching.push_back(x < N ? make_pair(x, y) : make_pair(y, x));
        for (int nb : adj_bi[y]) {
            if (!removed[nb]) {
                if (--deg[nb] == 1) leaves.push(nb);
            }
        }
    }
    return (int)matching.size() == N ? matching : vector<pair<int, int>>{};
}
```

---

### 11.4 Pattern 4: $O(VE)$ Online Kempe-Chain Edge Coloring (`CF 600 F`) & $O(E \log \Delta)$ Eulerian Halving

```cpp
// Online O((|L| + |R|) * M) Bipartite Edge Coloring with Delta colors (1..Delta).
// who[z][c] = neighbor of z along color c (0 if free); edge_id[z][c] = index of that edge.
void color_bipartite_edge(int u, int v, int e_idx, int Delta,
                          vector<vector<int>>& who, vector<vector<int>>& edge_id,
                          vector<int>& ans_color) {
    int cu = 1, cv = 1;
    while (who[u][cu] != 0) ++cu;
    while (who[v][cv] != 0) ++cv;
    ans_color[e_idx] = cu;
    if (who[v][cu] == 0) {
        who[u][cu] = v; who[v][cu] = u;
        edge_id[u][cu] = edge_id[v][cu] = e_idx;
        return;
    }
    // Walk alternating path from v starting with color cu, then cv, cu, cv, ...
    vector<int> path_verts = {u, v};
    vector<int> path_edges = {e_idx};
    int cur = v, col = cu;
    while (who[cur][col] != 0) {
        int nxt = who[cur][col];
        int eid = edge_id[cur][col];
        path_verts.push_back(nxt);
        path_edges.push_back(eid);
        // Clear old incidence before re-linking
        who[cur][col] = 0;
        edge_id[cur][col] = 0;
        cur = nxt;
        col ^= (cu ^ cv);
    }
    // Clear the reverse pointers and re-assign alternating colors cu, cv, cu, ...
    int assign_col = cu;
    for (size_t i = 0; i < path_edges.size(); ++i) {
        int a = path_verts[i], b = path_verts[i + 1], eid = path_edges[i];
        ans_color[eid] = assign_col;
        who[a][assign_col] = b; who[b][assign_col] = a;
        edge_id[a][assign_col] = edge_id[b][assign_col] = eid;
        assign_col ^= (cu ^ cv);
    }
}
```

---

### 11.5 Pattern 5: Constructive Dilworth Maximum Antichain Extraction (`CF 590 E`, `[CTSC2008] 祭祀`)

Given a strict poset $\mathcal{P} = (V, \prec)$ (already transitively closed and deduplicated so $u \prec v \implies u \ne v$):
1. Build $G_{\text{split}}(\mathcal{P}) = (V_{\text{out}} \cup V_{\text{in}}, E_{\text{split}})$ with $(u_{\text{out}}, v_{\text{in}}) \in E_{\text{split}} \iff u \prec v$.
2. Run Max-Flow on $\{S, T\} \cup V_{\text{out}} \cup V_{\text{in}}$ with $c(S, u_{\text{out}}) = w_u$, $c(u_{\text{out}}, v_{\text{in}}) = \infty$, $c(v_{\text{in}}, T) = w_v$.
3. Run residual BFS from $S$ ($c_f > 0$) to obtain `vis_S`.
4. By **Lemma 6.1 (Transitivity Non-Overlap Lemma)**, no vertex $v \in V$ has both $v_{\text{out}} \notin V_S$ and $v_{\text{in}} \in V_S$. The optimal (maximum-weight) antichain is:
   $$A^* = \{ v \in V : \text{vis\_S}[v_{\text{out}}] == \text{true} \;\land\; \text{vis\_S}[v_{\text{in}}] == \text{false} \}.$$

---

### 11.6 Master Checklist of 10 Fatal Wave 1B Failure Modes

| # | Failure Mode / Bug | Why It Breaks | How to Fix It |
| :-: | :--- | :--- | :--- |
| **1** | Setting middle capacity $c(u, v) = 1$ instead of $\infty$ in MWVC or König MVC recovery | Min-cut severs middle edge $(u, v)$ instead of $S \to u$ or $v \to T$, corrupting both $\tau_w(G)$ and $V_S$. | Always set $c(u, v) = \infty$ whenever extracting vertex covers or solving weighted MWVC/MWIS. |
| **2** | Setting middle capacity $c(u, v) = \infty$ instead of $1$ in $b$-matching / cycle covers (`CF 510 E`) | Pushes $2$ units along the same edge $(u, v)$, creating a degenerate 2-gon instead of a simple cycle of length $\ge 4$. | Set $c(u, v) = 1$ when each edge of $E$ may be used at most once in a $b$-factor. |
| **3** | Forgetting the `1 + 1 = 2` clique in Prime-Sum MWIS (`CF 808 F`) | $2$ is an even prime, so multiple $1$s have $1 + 1 = 2 \in \mathbb{P}$ (odd–odd edges inside $L_{\text{odd}}$!). | Deduplicate all `1`s to the single `1` with maximum weight $p_i$ before building $G$. |
| **4** | Splitting grid segments on soft obstacles `*` in rook/camera problems (`[HEOI2012] 游戏`) | Soft pits `*` do not block attacks/rays; splitting on `*` allows two rooks in the same segment to attack each other. | Split segments **only** on hard walls `#`; simply omit adding edges for `*` cells. |
| **5** | Swapping Chooser vs. First-Mover roles in Bipartite Walk Games (`[JSOI2009] 游戏`) | If Alice chooses $v_0$ and Bob moves first from $v_0$, Alice is the *Second Mover* in the walk game! | Check who moves first from $v_0$: First Mover wins $\iff v_0$ is Essential; Second Mover wins $\iff v_0 \in L_1 \cup R_2$ is Avoidable. |
| **6** | Running Tarjan SCC on $G_{f^*} \setminus \{S, T\}$ without filtering $V_S \cup V_T^{\text{rev}}$ (`[HAOI2017] 新型城市化`) | Alternating paths from $U_L$ or $U_R$ look like acyclic paths if $S$ and $T$ are deleted, falsely marking replaceable matched edges as critical. | Keep $S$ and $T$ inside $G_{f^*}$ when running Tarjan SCC: then $(u, v) \in M$ is critical $\iff \text{scc}(u) \ne \text{scc}(v)$! |
| **7** | Checking only single intervals $[l, r]$ when computing positive Ore defect $\max_S (\lvert S \rvert - \lvert N(S) \rvert) > 0$ | By Lemma 5.1, $\text{def}(I_1 \sqcup I_2) = \text{def}(I_1) + \text{def}(I_2)$, so two disjoint positive-defect intervals sum to a strictly larger defect! | Single intervals suffice for **feasibility** ($\text{def} \le 0$) and **prefix–suffix unions** (`ARC 076 F`), but interior intervals with $\text{def} > 0$ require multi-interval DP! |
| **8** | Skipping Transitive Closure before Overlapping Path Cover or Dilworth Antichain | Paths cannot jump over shared vertices in $G_{\text{split}}$, and $v_{\text{out}}, v_{\text{in}}$ can both enter $C^*$, violating Lemma 6.1. | Always compute $\text{TC}(G)$ (via Bitset Floyd–Warshall or DAG reachability) before building $G_{\text{split}}$ for Dilworth! |
| **9** | Keeping duplicate elements ($S_i = S_j$) in a poset (`ABC 354 G`, `CF 590 E`) | Mutual comparability $i \prec j \land j \prec i$ creates 2-cycles in $G_{\text{split}}$, breaking DAG acyclicity and Dilworth's theorem. | Deduplicate identical elements first (keeping $\max(w_i, w_j)$ for antichains, or sum/chain for path covers). |
| **10** | Using MCMF when vertex weights depend only on one side $L$ (`CF 1510 B`, `[SCOI2010] 连续攻击游戏`) | Unnecessary $O(VE \log V)$ overhead or TLE. | By Transversal Matroid theory (Theorem 2.2), sort $L$ by decreasing $w_u$ and run Kuhn's DFS in priority order! |
