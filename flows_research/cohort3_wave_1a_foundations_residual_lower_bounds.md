# Cohort 3 — Wave 1A Master Reconciliation Monograph: Foundations of Max-Flow, Residual Geometry, Cut Lattices, Structural Gadgets, and Flows with Demands

**Iteration 105 Synthesis** — Reconciling Cohort 1 (`iter_01_to_05_foundations_residual_lower_bounds.md`, Iterations 01–05) and Cohort 2 (`cohort2_iter_53_to_57_foundations_residual_lower_bounds.md`, Iterations 53–57) into the unified Phase 1 Wave 1A master reference.

> **Pedagogical Mandate (Zero Magic Gadgets & No Boilerplate Code)**:
> Throughout this monograph, no flow network, vertex-splitting gadget, residual reachability test, or lower-bound auxiliary graph is ever presented as a black-box trick. Every modelling archetype and every problem in the 30-problem master bank strictly enforces the **4-Step English-to-Graph Compilation Pipeline**:
> 1. **Non-Graph Diagnostic Signal (Recognition)**: What surface clue in the English problem statement and constraint bounds ($N, M, V_{\max}$) tells a solver to reach for Max-Flow / Min-Cut / Circulation — and why greedy or DP fails.
> 2. **Intermediate Algebraic / Logical Representation**: Formulate the exact conservation equations, indicator cuts, or affine slack shifts $f(e) = l(e) + \tilde{f}(e)$ *before* introducing vertices or directed arcs.
> 3. **Reverse-Engineering Scratchpad (Mechanical Graph Compilation)**: Show term-by-term how each equation or inequality forces the vertices, directed capacities, reverse residual arcs, or super-source/sink supplies.
> 4. **Hand-Checkable Toy Trace & Broken-Gadget Counterexamples**: Verify on a concrete $N \le 4$ instance and prove what fails when subtle invariants (such as `edge_idx ^ 1` pairing, $\text{out} \to \text{in}$ port wiring, or feedback arc residual neutralization) are violated.

---

## 1. Cross-Cohort Comparative Audit & Blind-Spot Synthesis Matrix

Before synthesizing the unified theory, we audit the two independent Phase 1 cohorts across all five foundational sub-topics to expose mutually complementary blind spots, proof variations, and problem selections.

### 1.1 Theoretical & Modelling Blind-Spot Matrix

| Wave 1A Sub-Topic | Cohort 1 (`iter_01_to_05`) Unique Strengths | Cohort 2 (`cohort2_iter_53_to_57`) Unique Strengths | Cohort 3 Reconciled Synthesis & Gap-Hunting Additions |
| :--- | :--- | :--- | :--- |
| **Iter 01 / 53: Flow-Cut Algebra, Residual Space & Path Decomposition** | Explicit `edge_idx ^ 1` memory-layout contract proving why merging anti-parallel edges $(u,v)$ and $(v,u)$ corrupts individual edge recovery in lower-bound and MCMF graphs; amortized $O(E + \sum |P_i|)$ pointer-advancing DAG path extraction. | Incidence-matrix inner-product proof $\mathbf{1}_S^T (Bf) = (\mathbf{1}_S^T B)f$ of the Flow Value Lemma; interpretation of $G_f$ as the feasible linear tangent cone $\Delta = \Delta^+ - \Delta^-$ of the flow polytope; complete 4-Step compilation of **Horn's Preemptive Parallel-Machine Scheduling Theorem ($P \mid r_j, \text{pmtn}, d_j \mid -$)** and **McNaughton's Wrap-Around Rule**. | Unifies incidence-matrix algebra with the `edge_idx ^ 1` adjacency contract; integrates Zwick's 6-vertex $\phi$-irrational network, $O(E)$ pointer-advancing path decomposition, and Horn–McNaughton scheduling under a single flow-polytope framework. |
| **Iter 02 / 54: Blocking Flows, Dinic Tight Regimes, Scaling & HLPP** | Explicit 4-layer dead-end hub counterexample proving why omitting `cur[u]` degrades a single Dinic phase from $O(VE)$ to $\Theta(VE^2)$ (and $\Omega(2^{V/6})$ across phases); Zadeh/Karzanov ladder-and-funnel adversarial graph anatomy. | **Asymmetric Bipartite Capacity Generalization** ($O(E\sqrt{|R|})$ when right-hand nodes have unit degree/capacity even if left-hand capacities are arbitrary); **Capacity Scaling** ($O(E^2 \log U)$ / $O(VE \log U)$) with residual cut bound $|f^*| - |f| < |E|\Delta$; **HLPP Phase-1 vs. Phase-2 Pitfall** (why stopping at height $\ge |V|$ gives the exact value $\text{ex}(t) = |f^*|$ but leaves unreturned internal excess that invalidates edge-level flow queries). | Synthesizes all four polynomial Dinic regimes ($O(V^2 E)$, $O(E^{3/2})$, $O(V^{2/3}E)$, $O(E\sqrt{V})$ + asymmetric $O(E\sqrt{|R|})$), the `cur[u]` $\Theta(VE^2)$ counterexample, **Zhong's (2025) Adversarial Graph & Goldberg–Rao (1998) Binary Blocking Flow**, Capacity Scaling, and HLPP Phase-1/Phase-2 execution discipline. |
| **Iter 03 / 55: Cut Lattice, Picard–Queyranne DAG & Dynamic Rollback** | Flow-conservation proof on $R(u) = \{w : u \to^* w \text{ in } G_{f^*}\}$ showing why any saturated edge $(u,v)$ with $u \not\to^* v$ automatically satisfies $u \to^* s$ and $t \to^* v$; single-edge parametric capacity sensitivity ($\pm \epsilon$). | Complete 16-region partition double-counting table proving the Cut Submodularity Identity $\kappa(A) + \kappa(B) = \kappa(A \cup B) + \kappa(A \cap B) + c(A \setminus B, B \setminus A) + c(B \setminus A, A \setminus B)$; **Lemma 55.3** (Flow-Decomposition proof of SCC reachability); **Dynamic Single-Edge Flow Rollback (`退流` — `[SDOI2014] LIS`)** via bounded Dinic on $(t \to v)$ and $(u \to s)$. | Merges the 16-region submodularity table, Both proofs (flow-conservation and path-decomposition) of `[AHOI2009]` Feasible vs. Essential edge classification, minimum-cardinality cut perturbation $\tilde{c}(e) = c(e)(|E|+1)+1$, and dynamic flow rollback `退流`, plus **Gap 2: Directed Cut Submodularity vs. Undirected Cut Posimodularity (Uncrossing)**. |
| **Iter 04 / 56: Structural Gadgets, Vertex Splitting, Menger & Layered DAGs** | Explicit 6-vertex Diamond-Bridge counterexample against greedy shortest-path removal; crucial **MCMF Caveat** proving why the 2-half-edge undirected shortcut (`cap[e] = cap[e^1] = C`) fails when edges have costs $+w$ vs. $-w$. | Complete 4-variant Menger duality table with exact Dinic complexities; physical flow recovery formula $f_{\text{phys}}(u \to v) = \max(0, C - \text{cap}[e]) = \max(0, \text{cap}[e \oplus 1] - C)$; **Incremental Dynamic Layer Addition (`动态加层`)** vs. binary search on $T$. | Consolidates vertex splitting, undirected compact pairs (with both physical flow recovery and the MCMF $+w/-w$ failure mode), Menger's 4 variants, dynamic time-expanded DAGs, and **Row/Column Hub Sparsification (`[ARC 074 D]`)**. |
| **Iter 05 / 57: Flows with Demands (`上下界`), Hoffman's Theorem & Compilations** | Explicit analysis of Phase-2 traps in `LOJ #116/#117` (Trap 1: forgetting `cap[e_fb ^ 1] = 0` double-counts $f_0$; Trap 2: why $S^*, T^*$ are automatically inert dead ends once $\Sigma^+$ is saturated); proof in `P30` (`[NOI2008] 志愿者招募`) that Lower-Bound Circulation on a line spine $[A_t, \infty)$ is algebraically identical to Consecutive Equation Differencing ($E_t - E_{t-1}$). | **Baranyai's Rounding Lemma** guarantee for Contingency-Table / Matrix Rounding; warning against reading $|f_0|$ from $\text{MaxFlow}(S^*, T^*) = \Sigma^+$ instead of $\tilde{f}(t,s)$; full non-graph compilation of Mixed-Graph Eulerian Orientation and Minimum-Fleet DAG Coverage. | Unifies all 4 Lower-Bound variants, the Deletion vs. Non-Deletion equivalence proof, Hoffman's Theorem, Baranyai's Matrix Rounding, Eulerian Orientation, Minimum-Fleet DAG Cover, the `[NOI2008]` spine isomorphism, and **Gap 3: Extracting Hoffman Violation Certificates & Minimum Demand Relaxations from $S_{\min}^*$**. |

---

### 1.2 Practice Problem Cross-Cohort Deduplication & Tier Audit (30 Unique Problems)

Across Cohort 1 (22 problems) and Cohort 2 (21 problems), 14 problems overlapped (often with complementary algebraic derivations or implementation insights) and 15 were unique to one cohort. Adding 1 targeted gap-hunting problem on Minimum Cut Uniqueness yields **30 unique non-template problems** organized across four progressive tiers in Section 8:

| Master ID | Problem & Judge URL | Lang | Source Audit | Primary Structural Archetype |
| :--- | :--- | :---: | :--- | :--- |
| **Tier 1** | **Stepping Stone (7 Problems)** | | | |
| **P01** | `[CF 546E]` Soldier and Traveling | `[EN]` | Cohort 1 (`P01`) + Cohort 2 (`P01`) | 2-layer departure/arrival time-split graph preventing multi-hop cascades |
| **P02** | `[CSES 1711]` Distinct Routes | `[EN]` | Cohort 1 (`P02`) | Edge-disjoint $s$-$t$ paths + $O(E)$ pointer-advancing DAG path extraction |
| **P03** | `[USACO 5.4 / Luogu P1345]` Telecowmunication | `[EN]`/`[ZH]` | Cohort 1 (`P03`) | Undirected vertex cut $v_{\text{in}} \xrightarrow{1} v_{\text{out}}$ + lexicographical cut enumeration |
| **P04** | `[ZOJ 2314 / ASC 1]` Reactor Cooling | `[EN]`/`[ZH]` | Cohort 1 (`P04`) + Cohort 2 (`R-03`) | Canonical Variant 1 (`无源汇上下界可行流`) pipe circulation & excess balance |
| **P05** | `[Luogu P2763]` 试题库问题 | `[ZH]` | Cohort 2 (`P02`) | Asymmetric one-to-many bipartite quota matching ($O(E\sqrt{N})$) & recovery |
| **P06** | `[Luogu P2766]` 最长不下降子序列问题 | `[ZH]` | Cohort 2 (`P03`) | LNDS layered DAG transition filtering, vertex splitting & $K=1$ trap |
| **P07** | `[AtCoder ABC 239 G]` Builder Takahashi | `[JA]` | Cohort 1 (`P05`) | Minimum-weight vertex cut + $S_{\min}$ cut set extraction ($v_{\text{in}} \in S_{\min} \land v_{\text{out}} \notin S_{\min}$) |
| **Tier 2** | **Intermediate (8 Problems)** | | | |
| **P08** | `[POJ 1637 / UVa 10735]` Sightseeing Tour | `[EN]`/`[ZH]` | Cohort 1 (`P06`) + Cohort 2 (`P07`) | Mixed-graph Eulerian circuit via parity check & $\frac{\text{out}_0 - \text{in}_0}{2}$ flow + Hierholzer |
| **P09** | `[AHOI2009 / Luogu P4126]` 最小割 | `[ZH]` | Cohort 1 (`P07`) + Cohort 2 (`P08`) | Picard–Queyranne DAG & Tarjan SCC classification of Feasible/Essential cuts |
| **P10** | `[CTSC1999 / Luogu P2754]` 家园 / 星际转移问题 | `[ZH]` | Cohort 1 (`P08`) + Cohort 2 (`P06`) | DSU pre-check + Time-Expanded Layered DAG with incremental dynamic layers |
| **P11** | `[SCOI2007 / Luogu P2472]` 蜥蜴 | `[ZH]` | Cohort 1 (`P09`) + Cohort 2 (`P04`) | 2D Euclidean jump graph with pillar durability vertex splitting |
| **P12** | `[CF 653D]` Delivery Bears | `[EN]` | Cohort 1 (`P10`) + Cohort 2 (`P05`) | Binary search on per-bear weight $w$ + floor capacity $\min(X, \lfloor c_e / w \rfloor)$ |
| **P13** | `[CF 498C]` Array and Operations | `[EN]` | Cohort 2 (`P09`) | Prime factorization independence + parity bipartite $b$-matching |
| **P14** | `[AtCoder ARC 074 D (F)]` Lotus Leaves | `[JA]` | Cohort 1 (`P11`) | Row/Column Hub Sparsification reducing $O(HW(H+W))$ to $O(HW)$ |
| **P15** | `[AtCoder ABC 285 G]` Tatami | `[JA]` | Cohort 1 (`P12`) + Cohort 2 (`P10`) | Bipartite domino/monomino tiling via Variant 2 lower-bound flow ($[1,1]$ vs. $[0,1]$) |
| **Tier 3** | **Advanced (8 Problems)** | | | |
| **P16** | `[ZJOI2010 / Luogu P5192]` Shoot the Bullet (东方文花帖) | `[ZH]` | Cohort 1 (`P13`) + Cohort 2 (`P11`) | 3-layer interval bounds compiled to Variant 3 (`有源汇上下界最大流`) |
| **P17** | `[POJ 2396]` Budget | `[EN]`/`[ZH]` | Cohort 1 (`P14`) + Cohort 2 (`P12`) | Submatrix inequality interval intersection + Variant 2 matrix reconstruction |
| **P18** | `[Luogu P4843 / LOJ #2042]` 清理雪道 | `[ZH]` | Cohort 1 (`P15`) + Cohort 2 (`P13`) | Minimum-fleet DAG edge cover via Variant 4 (`有源汇上下界最小流`) |
| **P19** | `[CF 704D]` Captain America | `[EN]` | Cohort 1 (`P16`) + Cohort 2 (`P14`) | 2D line discrepancy $|R_L - B_L| \le d_L$ + $O(N\sqrt{N})$ Variant 3 optimization |
| **P20** | `[CQOI2014 / Luogu P3163]` 危桥 | `[ZH]` | Cohort 1 (`P17`) + Cohort 2 (`P15`) | Two-Commodity Undirected Flow via Okamura–Seymour $(b_1 \leftrightarrow b_2)$ Swap & $\frac{f_1 \pm f_2}{2}$ |
| **P21** | `[Luogu P3254 / POJ 3498 / Horn]` Preemptive Scheduling | `[EN]`/`[ZH]` | Cohort 2 (`P16`) | Coordinate-compressed elementary intervals $I_k = [t_{k-1}, t_k]$ + McNaughton wrap-around |
| **P22** | `[BZOJ 3698]` XWW 的难题 | `[ZH]` | Cohort 1 (`P18`) | Matrix rounding with row/column/grand-total accumulators via Variant 3 |
| **P23** | `[ZOJ 2587 / UVa 10480]` Unique Attack (Min-Cut Uniqueness) | `[EN]`/`[ZH]` | Cohort 3 Gap-Hunt | Testing uniqueness of the minimum $s$-$t$ cut via $S_{\min} \cup T_{\min} = V$ in $G_{f^*}$ |
| **Tier 4** | **Mastery (7 Problems)** | | | |
| **P24** | `[SDOI2014 / Luogu P3308]` LIS | `[ZH]` | Cohort 1 (`P19`) + Cohort 2 (`P17`) | Lexicographically smallest min vertex cut via `!bfs(u_in, u_out)` + Dynamic Rollback (`退流`) |
| **P25** | `[CF 1383F]` Special Edges | `[EN]` | Cohort 1 (`P20`) + Cohort 2 (`P18`) | $K \le 10$ parametric edges solved for $Q = 2 \times 10^5$ queries via $2^K$ Cut-Mask Duality |
| **P26** | `[ICPC WF 2007 / UVa 1106]` Chips Challenge | `[EN]` | Cohort 1 (`P21`) | $\text{row}_i = \text{col}_i \le K$ circulation with slack bypass $y_i = K - \text{row}_i$ & $K$-sweep |
| **P27** | `[CF 611H]` New Year and Forgotten Tree | `[EN]` | Cohort 2 (`P19`) | Prüfer $D^{D-2} \le 1296$ hub tree enumeration + edge-orientation bipartite flow |
| **P28** | `[AtCoder ABC 263 G]` Erasing Prime Sums | `[JA]` | Cohort 2 (`P20`) | Even–Odd prime bipartite graph + $1+1=2$ self-loop sensitivity $u_{\min} = F_{\text{with-1}} - F_{\text{no-1}}$ |
| **P29** | `[CF 903G]` Yet Another MaxFlow Problem | `[EN]` | Cohort 2 (`P21`) | Direction B (Flow $\to$ Non-Flow): Prefix-cut dominance + Lazy Segment Tree sweep |
| **P30** | `[NOI2008 / Luogu P3980]` 志愿者招募 (Lower-Bound Spine View) | `[ZH]` | Cohort 1 (`P22`) | Algebraic isomorphism between Lower-Bound Circulation $[A_t, \infty)$ and Equation Differencing |

---

## 2. Iteration 01 / 53 Reconciled: The Flow-Cut Algebra, Residual Tangent Space, and Path–Cycle Decomposition

### 2.1 Incidence Matrix Algebra and Nonnegative vs. Skew-Symmetric Flow Representations

Let $G = (V, E)$ be a directed multigraph with source $s \in V$, sink $t \in V$ ($s \neq t$), and nonnegative capacity function $c: E \to \mathbb{R}_{\ge 0}$. Every edge $e \in E$ has a well-defined tail $\text{tail}(e) \in V$ and head $\text{head}(e) \in V$. For any vertex $v \in V$, denote the outgoing and incoming incidence stars by:
$$\delta^+(v) = \{e \in E : \text{tail}(e) = v\}, \qquad \delta^-(v) = \{e \in E : \text{head}(e) = v\}$$

#### Definition 2.1 (Feasible Nonnegative $s$-$t$ Flow and the Flow Polytope)
A function $f: E \to \mathbb{R}$ is a feasible $s$-$t$ flow if it satisfies:
1. **Capacity Constraints (Box Bounds)**:
   $$0 \le f(e) \le c(e) \qquad \forall e \in E$$
2. **Kirchhoff's Flow Conservation (Divergence-Free Interior)**: Define the net outflow (divergence) at vertex $v$ as $\text{div}_f(v) = \sum_{e \in \delta^+(v)} f(e) - \sum_{e \in \delta^-(v)} f(e)$. Then:
   $$\text{div}_f(v) = 0 \qquad \forall v \in V \setminus \{s, t\}$$

The **value** of the flow $f$, denoted $|f|$, is the net flow leaving the source $s$:
$$|f| = \text{div}_f(s) = \sum_{e \in \delta^+(s)} f(e) - \sum_{e \in \delta^-(s)} f(e)$$

In matrix notation, let $B \in \{-1, 0, +1\}^{|V| \times |E|}$ be the directed **vertex-edge incidence matrix** of $G$, where:
$$B_{v, e} = \begin{cases} +1 & \text{if } v = \text{tail}(e) \\ -1 & \text{if } v = \text{head}(e) \\ 0 & \text{otherwise} \end{cases}$$
Then the feasible flow polytope is the bounded convex polyhedron:
$$\mathcal{P}(G, c) = \left\{ (f, v_0) \in \mathbb{R}^{|E|} \times \mathbb{R} \;\middle|\; B f = v_0 (\mathbf{e}_s - \mathbf{e}_t), \;\; \mathbf{0} \le f \le c \right\}$$
where $\mathbf{e}_s, \mathbf{e}_t \in \mathbb{R}^{|V|}$ are the standard basis vectors at $s$ and $t$, and $v_0 = |f|$. Because every column $B_{\cdot, e}$ has exactly one $+1$ and one $-1$, the sum of all rows of $B$ is zero ($\mathbf{1}_V^T B = \mathbf{0}^T$), which immediately implies $\text{div}_f(t) = -\text{div}_f(s) = -|f|$.

#### The Skew-Symmetric Formulation vs. The `edge_idx ^ 1` Adjacency Contract
Classical textbooks (such as CLRS 2nd Edition and Sleator–Tarjan) often define flow over $V \times V$ via skew-symmetry $f_{\text{skew}}(u, v) = -f_{\text{skew}}(v, u)$ with upper bound $f_{\text{skew}}(u, v) \le c(u, v)$. While algebraically compact, **the $V \times V$ skew-symmetric formulation is a severe anti-pattern in competitive programming** whenever the input graph contains **anti-parallel directed edges** $e_1 = (u \to v)$ with capacity $c_1$ and $e_2 = (v \to u)$ with capacity $c_2$, or parallel multi-edges:
- If $e_1$ and $e_2$ are merged into a single pair of $V \times V$ matrix entries, it is impossible to recover the individual physical flows $f(e_1) \in [0, c_1]$ and $f(e_2) \in [0, c_2]$ uniquely (only their difference $f(e_1) - f(e_2)$ is preserved).
- Worse, if $e_1$ and $e_2$ have **lower bounds** $[l_1, u_1]$ and $[l_2, u_2]$ (Section 6) or **distinct costs** $w_1$ and $w_2$ (Wave 2A MCMF), merging them destroys the feasible polytope outright: the reverse residual arc of $e_1$ must carry cost $-w_1$, whereas the forward physical arc $e_2$ carries cost $+w_2$.

> [!IMPORTANT]
> **The `edge_idx ^ 1` Adjacency-List Representation Contract**:
> Every physical directed edge $e = (u \to v)$ with capacity $c(e)$ is allocated as an **independent consecutive pair of half-edges** at indices $2k$ and $2k+1$ (initialized with `tot = 0` or `tot = 2` so that `(2k) ^ 1 == 2k + 1` and `(2k + 1) ^ 1 == 2k`):
> - **Forward half-edge ($2k$, $u \to v$)**: initialized with residual capacity $\text{cap}[2k] = c(e)$.
> - **Reverse half-edge ($2k+1$, $v \to u$)**: initialized with residual capacity $\text{cap}[2k+1] = 0$.
>
> At any point during or after execution, the physical flow on edge $e_k$ is uniquely recovered in $O(1)$ time as:
> $$f(e_k) = \text{cap}[2k+1] = c(e_k) - \text{cap}[2k]$$
> Never merge two distinct input edges $(u, v)$ and $(v, u)$ into a single half-edge pair unless the problem explicitly defines an **undirected** uncosted edge (analyzed in Section 5.2).

---

### 2.2 Cut Algebra, The Residual Tangent Cone $G_f$, and Physical Path-Splicing

#### Definition 2.2 ($s$-$t$ Cut and Cut Capacity)
An **$s$-$t$ cut** is a partition of the vertex set $V = S \sqcup T$ ($T = V \setminus S$) such that $s \in S$ and $t \in T$. Define the **forward cut-set** $\delta^+(S)$ and **backward cut-set** $\delta^-(S)$ by:
$$\delta^+(S) = \{e \in E : \text{tail}(e) \in S \land \text{head}(e) \in T\}, \qquad \delta^-(S) = \{e \in E : \text{tail}(e) \in T \land \text{head}(e) \in S\}$$
The **capacity** of the cut $(S, T)$ depends **only on the forward directed arcs** from $S$ to $T$:
$$\kappa(S) = c(S, T) = \sum_{e \in \delta^+(S)} c(e)$$

#### Lemma 2.3 (The Flow Value Lemma & Weak Duality)
For **every** feasible $s$-$t$ flow $f$ and **every** $s$-$t$ cut $(S, T)$:
$$|f| = \sum_{e \in \delta^+(S)} f(e) - \sum_{e \in \delta^-(S)} f(e) \le \kappa(S)$$
with equality $|f| = \kappa(S)$ if and only if:
1. **Forward Saturation**: $f(e) = c(e)$ for all $e \in \delta^+(S)$, and
2. **Backward Emptiness (Zero Backflow)**: $f(e) = 0$ for all $e \in \delta^-(S)$.

*Proof via Incidence Matrix Inner Product*: Let $\mathbf{1}_S \in \{0, 1\}^{|V|}$ be the indicator vector of $S \subseteq V$. Since $s \in S$, $t \notin S$, and $Bf = |f|(\mathbf{e}_s - \mathbf{e}_t)$, taking the inner product of $\mathbf{1}_S$ with $Bf$ yields:
$$\mathbf{1}_S^T (Bf) = |f| \cdot \mathbf{1}_S^T (\mathbf{e}_s - \mathbf{e}_t) = |f|(1 - 0) = |f|$$
By associativity of matrix multiplication, $\mathbf{1}_S^T (Bf) = (\mathbf{1}_S^T B) f$. For each edge $e = (u \to v)$, the $e$-th coordinate of $\mathbf{1}_S^T B$ is $\mathbf{1}_S(u) - \mathbf{1}_S(v)$, which equals:
- $+1$ if $u \in S, v \in T$ ($e \in \delta^+(S)$),
- $-1$ if $u \in T, v \in S$ ($e \in \delta^-(S)$),
- $0$ if $u, v \in S$ or $u, v \in T$ (internal edges cancel cleanly).

Therefore:
$$|f| = (\mathbf{1}_S^T B) f = \sum_{e \in \delta^+(S)} f(e) - \sum_{e \in \delta^-(S)} f(e)$$
Since $f(e) \le c(e)$ on $\delta^+(S)$ and $f(e) \ge 0$ on $\delta^-(S)$, we immediately obtain $|f| \le \sum_{e \in \delta^+(S)} c(e) - \sum_{e \in \delta^-(S)} 0 = \kappa(S)$, with equality if and only if both complementarity conditions hold. $\blacksquare$

#### The Residual Network $G_f$ as the Feasible Tangent Cone
Suppose we currently hold a feasible flow $f \in \mathcal{P}(G, c)$ and wish to perturb it to $f' = f + \Delta$ so that $f'$ remains feasible and $|f'| > |f|$. What are the exact algebraic conditions on the perturbation vector $\Delta \in \mathbb{R}^{|E|}$?
1. **Linearity of Conservation**: $B(f + \Delta) = (|f| + |\Delta|)(\mathbf{e}_s - \mathbf{e}_t) \iff B\Delta = |\Delta|(\mathbf{e}_s - \mathbf{e}_t)$.
2. **Box Perturbation Bounds**: $0 \le f(e) + \Delta(e) \le c(e) \iff -f(e) \le \Delta(e) \le c(e) - f(e)$.

Split $\Delta(e) = \Delta^+(e) - \Delta^-(e)$ into nonnegative forward and backward perturbations $\Delta^+(e), \Delta^-(e) \ge 0$:
- Increasing flow on $e = (u \to v)$ by $\Delta^+(e) \in [0, c(e) - f(e)]$ transports $\Delta^+(e)$ units from $u$ to $v$.
- Decreasing flow on $e = (u \to v)$ by $\Delta^-(e) \in [0, f(e)]$ is **algebraically and physically identical** to transporting $\Delta^-(e)$ units in the opposite direction $v \to u$!

This motivates the **Residual Network** $G_f = (V, E_f)$: for each physical edge $e = (u \to v) \in E$:
- If $c_f(e) = c(e) - f(e) > 0$, include the **forward residual arc** $e = (u \to v)$ with residual capacity $c_f(e) = c(e) - f(e)$.
- If $c_f(e^{\text{rev}}) = f(e) > 0$, include the **backward residual arc** $e^{\text{rev}} = (v \to u)$ with residual capacity $c_f(e^{\text{rev}}) = f(e)$.

#### Physical Meaning of Reverse Arcs: The Path-Splicing Operator
Beginners frequently view reverse residual arcs as an abstract bookkeeping trick. Geometrically, pushing $\delta > 0$ units of flow along a backward residual arc $e^{\text{rev}} = (v \to u)$ executes a **physical path-splicing surgery**:

```
Before Augmentation (Greedy choice routed 1 unit along s -> u -> v -> t):
    s =======(1)=======> u =======(1)=======> v =======(1)=======> t
    s - - - -(0)- - - -> v                    u - - - -(0)- - - -> t

Augmenting Path P in Residual Graph G_f:
    s ------> v ===(reverse arc v->u, cancels u->v)=== u ------> t

After Augmentation (Two edge-disjoint physical paths of 1 unit each!):
    Path 1: s =======(1)=======> u =======(1)=======> t
    Path 2: s =======(1)=======> v =======(1)=======> t
    (Physical edge u -> v now carries 1 - 1 = 0 flow!)
```

When an earlier path routed flow along $P_1 = s \leadsto u \to v \leadsto t$, and a new residual path routes flow along $P_2 = s \leadsto v \xrightarrow{e^{\text{rev}}} u \leadsto t$, cancelling the shared segment $u \to v$ splices the prefix $s \leadsto u$ of $P_1$ onto the suffix $u \leadsto t$ of $P_2$, and splices the prefix $s \leadsto v$ of $P_2$ onto the suffix $v \leadsto t$ of $P_1$.

---

### 2.3 Ford–Fulkerson Max-Flow Min-Cut Theorem, Integrality, and Zwick's Irrational Pathology

#### Theorem 2.4 (Ford–Fulkerson Max-Flow Min-Cut Equivalence Theorem, 1956)
For any feasible $s$-$t$ flow $f$ in $G = (V, E, c)$, the following three statements are equivalent:
1. $f$ is a **maximum flow** in $G$ (i.e., $|f| \ge |f'|$ for all feasible flows $f'$).
2. The residual network $G_f$ contains **no augmenting path** (no directed path from $s$ to $t$ consisting of arcs with strictly positive residual capacity).
3. There exists an $s$-$t$ cut $(S, T)$ such that $|f| = \kappa(S)$ (and hence $(S, T)$ is a **minimum $s$-$t$ cut**).

*Constructive Proof ($2 \implies 3 \implies 1 \implies 2$)*:
- **($2 \implies 3$)**: Assume $G_f$ has no directed path from $s$ to $t$. Define the **residual reachable set**:
  $$S = \{v \in V : \text{there exists a directed path } s \leadsto v \text{ in } G_f\}, \qquad T = V \setminus S$$
  By definition, $s \in S$, and by hypothesis (2), $t \in T$, so $(S, T)$ is a valid $s$-$t$ cut. Now take any vertex $u \in S$ and any vertex $v \in T$. Because $u$ is reachable from $s$ in $G_f$ and $v$ is not, **no arc $(u \to v)$ can exist in $G_f$**:
  - For every forward physical edge $e = (u \to v) \in \delta^+(S)$, $e \notin E_f \implies c_f(e) = c(e) - f(e) = 0 \implies f(e) = c(e)$ (**forward saturation**).
  - For every backward physical edge $e = (v \to u) \in \delta^-(S)$, its reverse arc $e^{\text{rev}} = (u \to v) \notin E_f \implies c_f(e^{\text{rev}}) = f(e) = 0$ (**backward emptiness**).
  Substituting both into Lemma 2.3 yields $|f| = \sum_{e \in \delta^+(S)} c(e) - \sum_{e \in \delta^-(S)} 0 = \kappa(S)$.
- **($3 \implies 1$)**: By Weak Duality (Lemma 2.3), any feasible flow $f'$ satisfies $|f'| \le \kappa(S) = |f|$, so $f$ is maximum and $(S, T)$ is minimum.
- **($1 \implies 2$)**: Contrapositive: if $G_f$ contains a simple $s$-$t$ path $P$ with bottleneck capacity $\delta = \min_{e \in P} c_f(e) > 0$, augmenting $f$ by $\delta$ along $P$ produces a valid flow $f'$ with $|f'| = |f| + \delta > |f|$. $\blacksquare$

#### Corollary 2.5 (The Integrality Theorem — Dantzig & Fulkerson, 1956)
If all capacities $c: E \to \mathbb{Z}_{\ge 0}$ are integers, then:
1. There exists an **integral maximum flow** $f^*: E \to \mathbb{Z}_{\ge 0}$.
2. Every augmenting-path algorithm starting from $f \equiv 0$ augments by $\delta = \min_{e \in P} c_f(e) \in \mathbb{Z}_{\ge 1}$ at each step, terminating in at most $|f^*| \le \sum_{e \in \delta^+(s)} c(e)$ steps in $O(|E| \cdot |f^*|)$ time.
3. Geometrically, the incidence matrix $B$ is **totally unimodular (TUM)** (every square submatrix has determinant in $\{-1, 0, +1\}$), so every extreme point (vertex) of the flow polytope $\mathcal{P}(G, c)$ is integral.

#### Counterexample 2.6: Zwick's 6-Vertex Golden-Ratio Network (Irrational Non-Termination)
What if capacities are irrational real numbers and we choose augmenting paths adversarially? Uri Zwick (1995) constructed the smallest possible network ($|V| = 6, |E| = 9$) on which Ford–Fulkerson never terminates and converges to a **strictly suboptimal limit**!

Let $\phi = \frac{\sqrt{5} - 1}{2} \approx 0.618034$ be the reciprocal golden ratio, which satisfies the recurrence $\phi^k - \phi^{k+1} = \phi^{k+2}$ for all $k \ge 0$ (since $1 - \phi = \phi^2$). Construct $G = (V, E)$ with $V = \{s, t, a, b, c, d\}$:
- **3 Central Horizontal Edges**: $e_1 = (a \to b)$ with capacity $1$; $e_2 = (c \to b)$ with capacity $1$; $e_3 = (c \to d)$ with capacity $\phi$.
- **6 External Connector Edges** (each with capacity $X = 5 \ge \frac{1}{1-\phi} = \phi^{-2} \approx 2.618$): $(s \to a), (s \to c), (s \to d)$ and $(a \to t), (b \to t), (d \to t)$.

The true maximum flow is $|f^*| = 2X + 1 = 11$. Now trace the residual capacities $(r_1, r_2, r_3)$ of the three central edges $(e_1, e_2, e_3)$, initially $(1, 1, \phi)$:
1. **Initialization Step**: Augment $\Delta_0 = 1$ unit along $s \to a \xrightarrow{e_1} b \to t$. Now $(r_1, r_2, r_3) = (0, 1, \phi) = (0, \phi^0, \phi^1)$.
2. **Inductive Round $k$ ($k = 1, 3, 5, \dots$)**: Starting from central state $(0, \phi^{k-1}, \phi^k)$, execute two alternating augmenting paths using the reverse residual arcs $e_1^{\text{rev}} = (b \to a)$, $e_2^{\text{rev}} = (b \to c)$, $e_3^{\text{rev}} = (d \to c)$:
   - **Step $k$.A**: Augment $\Delta = \phi^k$ along $s \to c \xrightarrow{e_2} b \xrightarrow{e_1^{\text{rev}}} a \to t$ (or via $e_3$). This decreases $r_2$ to $\phi^{k-1} - \phi^k = \phi^{k+1}$, increases $r_1$ from $0$ to $\phi^k$, and drops $r_3$ to $0$, yielding state $(\phi^k, \phi^{k+1}, 0)$.
   - **Step $k$.B**: Augment $\Delta = \phi^k$ along $s \to a \xrightarrow{e_1} b \xrightarrow{e_2^{\text{rev}}} c \xrightarrow{e_3} d \to t$, restoring $r_2$, and then $\Delta = \phi^{k+1}$ to reach $(0, \phi^{k+1}, \phi^{k+2})$.

Because $\phi^k > 0$ for all $k \ge 0$, the algorithm runs forever! Worse, the total flow pushed converges to the geometric series:
$$\lim_{K \to \infty} |f^{(K)}| = 1 + 2 \sum_{k=1}^{\infty} \phi^k = 1 + \frac{2\phi}{1 - \phi} = 1 + \frac{2\phi}{\phi^2} = 1 + \frac{2}{\phi} = 2 + \sqrt{5} \approx 4.236068 \ll 11 = |f^*|$$

---

### 2.4 The Path–Cycle Flow Decomposition Theorem and $O(E)$ Pointer-Advancing Extraction

While a flow $f: E \to \mathbb{R}_{\ge 0}$ is defined locally on edges (Edge Space), many problems require reconstructing explicit global routes (Path Space).

#### Theorem 2.7 (Flow Decomposition Theorem — Ford & Fulkerson)
Any feasible nonnegative $s$-$t$ flow $f$ on $G = (V, E)$ can be decomposed into a collection of directed $s$-$t$ paths $\mathcal{P} = \{P_1, \dots, P_p\}$ and directed cycles $\mathcal{C} = \{C_1, \dots, C_q\}$ with strictly positive weights $w(P_i) > 0, w(C_j) > 0$ such that:
1. $f(e) = \sum_{P_i \ni e} w(P_i) + \sum_{C_j \ni e} w(C_j)$ for every $e \in E$.
2. $|f| = \sum_{i=1}^p w(P_i)$.
3. **Sparsity Bound**: The total number of paths and cycles satisfies $p + q \le |E|$. If $f$ is acyclic (no directed cycle carries positive flow), then $q = 0$ and $p \le |E|$.
4. **Integrality**: If $f$ is integral, all weights $w(P_i), w(C_j)$ can be chosen as positive integers.

*Constructive Proof*: Define the support subgraph $G_{\text{supp}}(f) = (V, \{e \in E : f(e) > 0\})$.
- **Phase 1 (Extracting $s$-$t$ Paths)**: While $|f| > 0$, start a walk at $u_0 = s$. At each vertex $u_k \neq t$, conservation $\text{div}_f(u_k) = 0$ (or $\text{div}_f(s) = |f| > 0$) guarantees at least one outgoing edge $e \in \delta^+(u_k)$ with $f(e) > 0$. Follow any such edge to $u_{k+1}$. Within at most $|V|$ steps, either:
  - A vertex repeats ($u_i = u_j$ for $i < j$), isolating a simple directed cycle $C$. Let $w(C) = \min_{e \in C} f(e) > 0$ and subtract $w(C)$ from $f(e)$ along $C$. At least one edge drops to $f(e) = 0$ and leaves $G_{\text{supp}}(f)$.
  - The walk reaches $t$, isolating a simple $s$-$t$ path $P$. Let $w(P) = \min_{e \in P} f(e) > 0$, subtract $w(P)$ from $f(e)$ along $P$, and decrease $|f|$ by $w(P)$. Again, at least one bottleneck edge drops to $f(e) = 0$.
- **Phase 2 (Extracting Remaining Circulation Cycles)**: Once $|f| = 0$, every vertex $v \in V$ has $\text{div}_f(v) = 0$. While any edge has $f(e) > 0$, start a walk from $\text{tail}(e)$; since every reached vertex has positive inflow and thus positive outflow, the walk must repeat a vertex within $|V|$ steps, yielding a cycle $C$ whose subtraction zeroes out at least one edge.

Since every extracted path or cycle zeroes out at least one distinct bottleneck edge in $G_{\text{supp}}(f)$, at most $|E|$ primitives are extracted in $O(|V| \cdot |E|)$ time. $\blacksquare$

> [!TIP]
> **Amortized $O(|E| + \sum |P_i|)$ Pointer-Advancing Extraction on Unit/DAG Flows**:
> In unit-capacity path-disjoint problems (like `CSES 1711 Distinct Routes`) or layered DAGs, every physical edge has $f(e) \in \{0, 1\}$. If you maintain a per-vertex pointer `ptr[u]` scanning the adjacency list of $u$ and **advance `ptr[u]` past any edge once $f(e)$ is decremented to $0$**, you never rescan exhausted edges. Extracting all $|f^*|$ paths then takes **strictly linear $O(|E| + \sum_{i=1}^{|f^*|} |P_i|)$ time**!

---

### 2.5 Horn's Preemptive Parallel-Machine Scheduling Theorem & McNaughton's Wrap-Around Rule

To demonstrate the **Zero Magic Gadgets** compilation pipeline on a purely non-graph scheduling problem, we derive **Horn's Theorem (1974)** for feasibility of preemptive parallel-machine scheduling $P \mid r_j, \text{pmtn}, d_j \mid -$.

#### The Non-Graph Problem Statement
We are given $N$ jobs and $M$ identical parallel machines. Job $j \in \{1, \dots, N\}$ has release time $r_j$, processing requirement $p_j$, and strict deadline $d_j$ ($r_j + p_j \le d_j$). Preemption is allowed: a job may be paused and resumed on the same or a different machine at any real time without penalty, provided that:
1. **No Parallel Self-Overlap**: At any instant $t \in \mathbb{R}$, job $j$ runs on **at most one** machine.
2. **Machine Capacity**: At any instant $t \in \mathbb{R}$, **at most $M$ jobs** run simultaneously across the $M$ machines.

Can all $N$ jobs be completed within their $[r_j, d_j]$ windows?

#### Step 1: Non-Graph Diagnostic Signal
Because preemption is continuous and migration across machines is free, individual instants inside an interval where no job arrives or expires are indistinguishable. Collect all $2N$ critical timestamps $\{r_1, \dots, r_N, d_1, \dots, d_N\}$, sort and deduplicate them into $t_0 < t_1 < \dots < t_K$ ($K \le 2N$). This partitions the timeline into $K$ **elementary intervals** $I_k = [t_{k-1}, t_k]$ of length $\Delta_k = t_k - t_{k-1} > 0$.

#### Step 2: Intermediate Algebraic Representation
Let $x_{j, k} \in \mathbb{R}_{\ge 0}$ denote the total time allocated to job $j$ during elementary interval $I_k = [t_{k-1}, t_k]$ (if $[t_{k-1}, t_k] \subseteq [r_j, d_j]$, and $x_{j,k} = 0$ otherwise). What are the necessary and sufficient conditions on $x_{j, k}$?
1. **Job Completion**: $\sum_{k : I_k \subseteq [r_j, d_j]} x_{j, k} = p_j$ for each job $j \in \{1, \dots, N\}$.
2. **No Self-Overlap in $I_k$**: $0 \le x_{j, k} \le \Delta_k$ (job $j$ cannot run for more than $\Delta_k$ seconds during an interval of duration $\Delta_k$).
3. **Total Machine Capacity in $I_k$**: $\sum_{j=1}^N x_{j, k} \le M \cdot \Delta_k$ (the $M$ machines offer at most $M \Delta_k$ total machine-seconds during $I_k$).

#### Step 3: Reverse-Engineering Scratchpad (Mechanical Graph & Wrap-Around Compilation)
1. **Why do conditions (2) and (3) guarantee a physical non-overlapping schedule on $I_k$? (McNaughton's Wrap-Around Rule, 1959)**:
   Suppose we have numbers $x_{1,k}, \dots, x_{N,k} \in [0, \Delta_k]$ summing to at most $M \Delta_k$. Imagine a single strip of length $M \Delta_k$, folded into $M$ parallel horizontal rows (machines $1, \dots, M$) each of width $\Delta_k$. Pack the intervals of lengths $x_{1,k}, x_{2,k}, \dots, x_{N,k}$ greedily left-to-right along the strip; whenever a job overflows the right boundary $t_k$ of machine $m$ by $\delta$ seconds, **wrap the overflow $[t_{k-1}, t_{k-1} + \delta]$ onto the left boundary of machine $m+1$**!
   - Why can the wrapped prefix $[t_{k-1}, t_{k-1} + \delta]$ on machine $m+1$ **never overlap** the suffix $[t_k - (x_{j,k} - \delta), t_k]$ on machine $m$? Because $x_{j,k} \le \Delta_k \implies t_{k-1} + \delta \le t_k - (x_{j,k} - \delta)$!
2. **Compiling to a Bipartite Flow Network**:
   - Create source $S$, sink $T$, job nodes $J_1, \dots, J_N$, and interval nodes $I_1, \dots, I_K$.
   - Add supply edges $S \to J_j$ with capacity $p_j$.
   - For each $(j, k)$ with $I_k \subseteq [r_j, d_j]$, add cross edge $J_j \to I_k$ with capacity $\Delta_k$ (enforcing $0 \le x_{j,k} \le \Delta_k$).
   - For each interval $I_k$, add sink edge $I_k \to T$ with capacity $M \cdot \Delta_k$ (enforcing $\sum_j x_{j,k} \le M \Delta_k$).
   - **Verdict**: A valid preemptive schedule exists $\iff \text{MaxFlow}(S, T) = \sum_{j=1}^N p_j$.

#### Step 4: Hand-Checkable Toy Trace ($N = 3$ Jobs, $M = 2$ Machines)
Suppose $M = 2$ machines, and inside a single elementary interval $I_1 = [0, 4]$ ($\Delta_1 = 4$, total machine capacity $M \Delta_1 = 8$), the max-flow assigns $x_{1,1} = 3$, $x_{2,1} = 3$, $x_{3,1} = 2$:
- **Machine 1**: Runs Job 1 on $[0, 3]$, then starts Job 2 on $[3, 4]$ ($1$ unit of Job 2).
- **Machine 2 (Wrap-Around)**: Wraps the remaining $3 - 1 = 2$ units of Job 2 onto $[0, 2]$, then runs Job 3 on $[2, 4]$.
- Notice Job 2 runs on $[3, 4]$ (Machine 1) and $[0, 2]$ (Machine 2) — disjoint time intervals $[0, 2] \cap [3, 4] = \emptyset$ because $x_{2,1} = 3 \le \Delta_1 = 4$!
- **What breaks if we omit the cross-edge capacity $\Delta_k$ (setting $c(J_j \to I_k) = \infty$)?** If Job 1 had $p_1 = 6, r_1 = 0, d_1 = 4$, an uncapacitated cross edge would route $x_{1,1} = 6 \le M\Delta_1 = 8$ through $I_1$, forcing Job 1 to run on both machines simultaneously during $[0, 2]$ (violating non-self-overlap).

---

## 3. Iteration 02 / 54 Reconciled: Blocking Flows, Dinic's Tight Sub-Quadratic Regimes, Capacity Scaling, and HLPP

### 3.1 Level Graphs, Blocking Flows, and the Strict Distance Monotonicity Theorem

Edmonds and Karp (1972) showed that augmenting along a single shortest $s$-$t$ path in $G_f$ requires $O(VE)$ phases, each taking $O(E)$ BFS time, for $O(VE^2)$ total time. E. A. Dinic (1970) observed that all shortest augmenting paths of length $L = d_f(s, t)$ live inside a single **Level Graph (Layered DAG)** and can be exhausted simultaneously in a single phase by computing a **Blocking Flow**.

#### Definition 3.1 (Level Graph $L(G_f)$ and Blocking Flow)
Let $d_f(s, u)$ be the unweighted shortest-path distance (minimum number of edges) from $s$ to $u$ in the residual network $G_f$. The **Level Graph** $L(G_f) = (V, E_L)$ is the subgraph of $G_f$ containing only **admissible (level-advancing) arcs**:
$$E_L = \left\{ e = (u \to v) \in E_f \;\middle|\; c_f(e) > 0 \;\land\; d_f(s, v) = d_f(s, u) + 1 \right\}$$
A feasible $s$-$t$ flow $\phi$ in $L(G_f)$ ($0 \le \phi(e) \le c_f(e)$) is called a **blocking flow** if **every** directed $s$-$t$ path in $L(G_f)$ contains at least one saturated edge $e$ with $\phi(e) = c_f(e)$.

> [!WARNING]
> **Blocking Flow $\neq$ Maximum Flow in $L(G_f)$**:
> Every maximum flow in $L(G_f)$ is a blocking flow, **but a blocking flow is NOT necessarily a maximum flow in $L(G_f)$**! Consider $L(G_f)$ with vertices $\{s, a_1, a_2, b_1, b_2, t\}$ ($d(s, t) = 3$) and unit-capacity edges $(s, a_1), (s, a_2), (b_1, t), (b_2, t)$, plus middle layer edges $(a_1, b_1), (a_1, b_2), (a_2, b_2)$.
> - Pushing $1$ unit along the single path $s \to a_1 \to b_2 \to t$ saturates $(s, a_1)$ and $(b_2, t)$.
> - In the remaining admissible graph $L(G_f) \setminus \{(s, a_1), (a_1, b_2), (b_2, t)\}$, no directed $s$-$t$ path survives (since $a_2$ only connects to $b_2$, whose out-edge to $t$ is saturated). Thus $|\phi| = 1$ is a valid **blocking flow**!
> - Yet the **maximum flow** in $L(G_f)$ has value $2$ (via $s \to a_1 \to b_1 \to t$ and $s \to a_2 \to b_2 \to t$), which Dinic discovers in the *next* phase when the reverse arc $(b_2 \to a_1)$ becomes admissible at distance $d_{f'}(s, t) = 5$.

#### Theorem 3.2 (Strict Monotonicity of Source-to-Sink Distance Across Blocking Phases)
Let $f$ be a feasible flow, let $\phi$ be any blocking flow in $L(G_f)$, and let $f' = f + \phi$. Then:
1. **Non-Decreasing Prefix Distance**: For every vertex $v \in V$, $d_{f'}(s, v) \ge d_f(s, v)$.
2. **Strict Sink Distance Growth**: $d_{f'}(s, t) \ge d_f(s, t) + 1$.
Consequently, Dinic's algorithm terminates in **at most $|V| - 1$ phases**.

*Proof by Induction on Path Length*:
First examine which edges can exist in the new residual graph $G_{f'}$:
- Every surviving residual edge from $G_f$ satisfies $d_f(s, v) \le d_f(s, u) + 1$ by the triangle inequality of BFS distances in $G_f$.
- Every newly created residual edge in $G_{f'} \setminus G_f$ is the **reverse arc** $e^{\text{rev}} = (v \to u)$ of an edge $e = (u \to v) \in E_L$ that carried $\phi(e) > 0$. Since $e \in E_L$, we had $d_f(s, v) = d_f(s, u) + 1$, so its reverse arc $v \to u$ satisfies $d_f(s, u) = d_f(s, v) - 1 < d_f(s, v) + 1$.

Thus **every** edge $(x \to y) \in E_{f'}$ satisfies the fundamental inequality:
$$d_f(s, y) \le d_f(s, x) + 1$$
with equality $d_f(s, y) = d_f(s, x) + 1$ holding **if and only if** $(x \to y)$ was already an admissible arc in $E_L$ that was not saturated by $\phi$.

Now let $P = (s = v_0 \to v_1 \to \dots \to v_k = t)$ be any shortest $s$-$t$ path in $G_{f'}$, so $k = d_{f'}(s, t)$. Summing $d_f(s, v_i) - d_f(s, v_{i-1}) \le 1$ telescopes to:
$$d_f(s, t) = \sum_{i=1}^k \big(d_f(s, v_i) - d_f(s, v_{i-1})\big) \le k = d_{f'}(s, t)$$
Suppose for contradiction that equality $d_{f'}(s, t) = d_f(s, t)$ holds. Then **every single step** $(v_{i-1} \to v_i)$ along $P$ must attain equality $d_f(s, v_i) = d_f(s, v_{i-1}) + 1$, which implies every edge of $P$ belongs to $E_L$ and remained unsaturated in $G_{f'}$. This directly contradicts the hypothesis that $\phi$ is a blocking flow in $L(G_f)$! Hence $d_{f'}(s, t) \ge d_f(s, t) + 1$. $\blacksquare$

---

### 3.2 Current-Arc Optimization (`cur[u]`) and the $\Theta(VE^2)$ / $\Omega(2^{V/6})$ Failure Trace

How fast does DFS find a blocking flow in $L(G_f)$? A correct Dinic DFS maintains a per-vertex pointer `cur[u]` initialized to `head[u]` at the start of each BFS phase. When `dfs(u, pushed)` scans outgoing edges $e = (u \to v)$ from `cur[u]`:
- As long as `cur[u]` is not fully saturated and $v$ is not yet exhausted, `cur[u]` stays at $e$.
- The moment `dfs(v, ...)` returns without exhausting `pushed` (either because $e$ became saturated with $\text{cap}[e] = 0$, or because all paths from $v$ to $t$ in $L(G_f)$ are blocked), **`cur[u]` advances to `nxt[e]`**; furthermore, if `tr == 0` (total flow pushed from $u$ is zero), we set `d[u] = -1` (**dead-node pruning**).

#### Theorem 3.3 ($O(VE)$ Single-Phase Blocking Flow Bound)
With `cur[u]` pointer persistence across the phase, computing a blocking flow in $L(G_f)$ takes $O(VE)$ time, yielding $O(V^2 E)$ total time for Dinic's algorithm on general networks.

*Amortized Charging Proof*: Because $L(G_f)$ is a DAG and no new edges are added to $L(G_f)$ during a single phase (reverse arcs of $E_L$ point backward from level $\ell+1$ to $\ell$ and are never admissible in the *current* phase), once an arc $e = (u \to v) \in E_L$ either becomes saturated ($\text{cap}[e] = 0$) or leads to a dead subtree ($v$ cannot reach $t$ in $L(G_f)$), $e$ can **never** carry flow again during the current phase.
- **Unsuccessful / Retreating Advances**: Whenever `dfs(v, ...)` fails to consume the remaining flow from $u$, `cur[u]` increments by 1. Across the entire phase, `cur[u]` can increment at most $\deg^+(u)$ times per vertex $u$, costing $\sum_{u \in V} \deg^+(u) = O(E)$ total time across all dead-end retreats!
- **Successful Augmentations**: Every successful augmentation to $t$ passes through at most $d_f(s, t) \le |V|$ vertices and saturates at least one bottleneck edge $e \in E_L$ (causing `cur[tail(e)]` to advance). Since at most $|E|$ edges can be saturated in a phase, there are at most $|E|$ augmentations, each taking $O(V)$ work along its stack, for $O(VE)$ total work. $\blacksquare$

#### Counterexample 3.4: What Breaks Without `cur[u]` or Dead-Node Pruning?
1. **Within a Single Phase ($\Theta(VE^2)$ Degradation)**:
   Suppose a programmer omits `cur[u]` (iterating `for (int e = head[u]; e; e = nxt[e])` from the beginning of the adjacency list on every DFS call) and omits `d[u] = -1`. Construct a 4-layer graph ($d(s, t) = 4$):
   - Layer 0: $\{s\}$.
   - Layer 1: $K = \Theta(V)$ nodes $a_1, \dots, a_K$, with edges $s \to a_i$ of capacity $K$.
   - Layer 2: A central hub $h$, plus $K$ "dead-end" nodes $z_1, \dots, z_K$ that initially reach $t$ via a single shared choke edge $z_j \to w \to t$ of capacity $1$. Every $a_i$ has edges to $z_1, \dots, z_K$ (each capacity $\infty$) **listed in its adjacency list before** its edge $a_i \to h$.
   - Layer 3: $K$ nodes $b_1, \dots, b_K$ with edges $h \to b_j$ (capacity $1$) and $b_j \to t$ (capacity $1$).
   - **Trace without `cur[u]`**: After the first unit of flow saturates $w \to t$, all $K$ nodes $z_1, \dots, z_K$ become dead ends. Yet for each of the $K^2 = \Theta(E)$ remaining unit augmentations routed through $a_i \to h \to b_j \to t$, whenever DFS visits $a_i$, it rescans all $K$ dead edges $(a_i \to z_1), \dots, (a_i \to z_K)$ from the head of $a_i$'s adjacency list! A single phase performs $\Theta(K^2 \cdot K^2) = \Theta(E^2)$ (or $\Theta(VE^2)$ with a path prefix) redundant scans.
2. **Across Phases Without `d[u] = -1` ($\Omega(2^{V/6})$ Exponential Blowup)**:
   Even if `cur[u]` is replaced by a boolean `vis` array that is not properly persisted or if dead nodes are re-entered across diamonds of length $V$, a sequence of $V/3$串联 (series-connected) diamond gadgets forces DFS to explore $2^{V/6}$ paths to discover a dead subgraph unless `cur[u]` or `d[u] = -1` permanently seals off exhausted branches.

---

### 3.3 Tight Sub-Quadratic Regimes of Dinic's Algorithm (Karzanov 1973; Even & Tarjan 1975)

On unit-capacity and bipartite networks, Dinic's algorithm runs dramatically faster than $O(V^2 E)$. Why? The universal analytical method is the **Phase Split Argument**: run Dinic for $K$ phases (where $d_f(s, t)$ grows from $1$ to $K$), then bound the **remaining residual flow** $|f^*| - |f^{(K)}|$ via a carefully chosen cut in $G_{f^{(K)}}$, which limits the number of remaining phases to at most $|f^*| - |f^{(K)}|$.

#### Theorem 3.5 (Four Tight Sub-Quadratic Regimes of Dinic's Algorithm)

| Regime | Network Structural Condition | Max-Flow Bound after Phase $K$ | Optimal Phase Split $K^*$ | Single Phase Time | Total Dinic Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Unit-Capacity Edge Network** | $c(e) = 1 \;\;\forall e \in E$ (arbitrary degrees) | $|f^*| - |f| \le \frac{|E|}{K}$ | $K^* = \lceil |E|^{1/2} \rceil$ | $O(E)$ | **$O(E^{3/2})$** |
| **2. Unit-Capacity Simple Network** | $c(e) = 1 \;\;\forall e \in E$, no parallel edges | $|f^*| - |f| \le \frac{2|V|^2}{K^2}$ | $K^* = \lceil |V|^{2/3} \rceil$ | $O(E)$ | **$O(V^{2/3} E)$** |
| **3. Unit-Vertex (Simple) Network** | $\min(\text{in-cap}(v), \text{out-cap}(v)) \le 1 \;\;\forall v \notin \{s, t\}$ | $|f^*| - |f| \le \frac{|V|}{K}$ | $K^* = \lceil |V|^{1/2} \rceil$ | $O(E)$ | **$O(E \sqrt{V})$** |
| **4. Asymmetric Bipartite Network** | $V = \{s, t\} \sqcup L \sqcup R$, unit capacity on $R$ ($c(r \to t) = 1$), **arbitrary capacities** on $s \to L$ and $L \to R$ | $|f^*| - |f| \le \frac{|R|}{K/2}$ | $K^* = \lceil \sqrt{|R|} \rceil$ | $O(E)$ | **$O(E \sqrt{|R|})$** |

*Unified Proof of the Four Regimes*:
1. **Why Each Phase Takes $O(E)$ Time on Unit-Capacity Networks**: When $c_f(e) = 1$ for all $e \in E_L$, **every** DFS visit that traverses an edge $e \in E_L$ either immediately saturates $e$ (if the walk reaches $t$) or proves the head of $e$ is a dead end. Thus `cur[u]` advances on *every* edge traversal! Both successful augmentations and dead-end retreats touch each edge of $E_L$ at most once, reducing the single-phase time from $O(VE)$ to **$O(E)$**.
2. **Regime 1 ($O(E^{3/2})$)**: After $K$ phases, $d_f(s, t) > K$. Partition the vertices by BFS distance layers $V_i = \{v : d_f(s, v) = i\}$ for $i = 0, \dots, K$. The $K$ cuts $(S_i, V \setminus S_i)$ where $S_i = \bigcup_{j=0}^{i-1} V_j$ have **pairwise disjoint** forward residual cut-sets $\delta^+_{G_f}(S_i) \subseteq E_f(V_{i-1}, V_i)$. Since $|E_f| \le 2|E|$, by the Pigeonhole Principle there exists a layer $i \in \{1, \dots, K\}$ with $|E_f(V_{i-1}, V_i)| \le \frac{|E|}{K}$. Thus $|f^*| - |f| \le \kappa_{G_f}(S_i) \le |E|/K$. Choosing $K = \sqrt{|E|}$ gives $\le 2\sqrt{|E|}$ total phases $\implies O(E^{3/2})$.
3. **Regime 2 ($O(V^{2/3} E)$)**: In a simple graph without parallel edges, $|E_f(V_{i-1}, V_i)| \le |V_{i-1}| \cdot |V_i|$. Since $\sum_{i=0}^K |V_i| \le |V|$, by Cauchy–Schwarz / AM-GM there exists an adjacent pair $(V_{i-1}, V_i)$ with $|V_{i-1}| + |V_i| \le \frac{2|V|}{K}$, so $|V_{i-1}| \cdot |V_i| \le \left(\frac{|V|}{K}\right)^2$. Thus $|f^*| - |f| \le \frac{|V|^2}{K^2}$. Setting $K = |V|^{2/3}$ leaves at most $|V|^{2/3}$ remaining phases $\implies O(V^{2/3} E)$.
4. **Regime 3 ($O(E\sqrt{V})$ — Even & Tarjan 1975)**: When every interior vertex $v \in V \setminus \{s, t\}$ has either total incoming capacity $\le 1$ or total outgoing capacity $\le 1$, any blocking flow in $L(G_f)$ decomposes into **vertex-disjoint** augmenting paths (so each phase takes $O(E)$ time), and the remaining flow in $G_f$ after $K$ phases decomposes into $|f^*| - |f|$ vertex-disjoint paths each of length $> K$. Since these paths are vertex-disjoint on $V \setminus \{s, t\}$, they consume at least $(|f^*| - |f|)(K - 1) \le |V|$ vertices, so $|f^*| - |f| \le \frac{|V|}{K - 1}$. Setting $K = \sqrt{|V|}$ yields $\le 2\sqrt{|V|}$ phases $\implies O(E\sqrt{V})$.
5. **Regime 4 ($O(E\sqrt{|R|})$ — Asymmetric Bipartite Quota Generalization)**: Suppose $V = \{s, t\} \sqcup L \sqcup R$ where left vertices $u \in L$ have arbitrary integer capacities $c(s \to u) = k_u \ge 1$, cross edges $(u \to v) \in L \times R$ have capacity $1$ (or $\infty$), and right vertices $v \in R$ have **unit capacity** $c(v \to t) = 1$ (as in `Luogu P2763 试题库问题` or `CF 704D` when one coordinate side is small). Every augmenting path in $G_f$ alternates between $L$ and $R$, and no two paths in a blocking flow or residual decomposition can share a vertex in $R$ (because every $r \in R$ has total throughput $\le 1$!). Since any path of length $d_f(s, t) > 2K + 1$ must visit at least $K$ distinct vertices of $R$, at most $|R| / K$ units of flow remain after $2K$ phases. Setting $K = \sqrt{|R|}$ gives **$O(E\sqrt{|R|})$**, completely independent of $\sum_{u \in L} k_u$ and $|L|$! $\blacksquare$

---

### 3.4 Adversarial Worst-Case Graphs (Zadeh, Karzanov, Zhong) and Goldberg–Rao Binary Blocking Flow

Can Dinic's algorithm actually require $\Theta(V^2 E)$ operations on general integer-capacity networks?
- **Zadeh (1973) & Karzanov (1974) Ladder-and-Funnel Graphs**: By constructing a sequence of $\Theta(V)$ phases where the $k$-th phase routes flow through an alternating "ladder" of length $2k+1$ Connected to dense bipartite complete "funnels" $K_{V, V}$ of exponential capacities $2^{V - k}$, each phase saturates $\Theta(E)$ funnel edges via paths of length $\Theta(V)$, forcing $\Theta(V)$ phases $\times \Theta(E)$ augmentations $\times \Theta(V)$ path length $= \Theta(V^2 E)$ operations.
- **Zhong (2025) Tight Adversarial Construction**: Recent work (Zhong, 2025) simplified and sharpened these adversarial families, showing that even with randomized adjacency orderings and standard heuristics, Dinic's $O(V^2 E)$ bound is tight up to constant factors when capacities span multiple orders of magnitude and funnel gadgets repeatedly reverse orientation across phases.
- **How Goldberg–Rao (1998) Bridges Unit and General Networks ($O(\min(V^{2/3}, E^{1/2}) E \log(V^2/E) \log U)$)**:
  Goldberg and Rao observed that the $O(V^{2/3} E)$ and $O(E^{3/2})$ unit-network bounds can be lifted to **arbitrary integer capacities** $c(e) \le U$ by assigning each residual arc $e \in E_f$ a **binary length** $\ell(e) \in \{0, 1\}$ with respect to a target capacity threshold $\Delta$:
  $$\ell(e) = \begin{cases} 0 & \text{if } c_f(e) \ge 3\Delta \text{ (or } 2\Delta \le c_f(e) < 3\Delta \text{ on a special back-arc)} \\ 1 & \text{if } 0 < c_f(e) < 2\Delta \end{cases}$$
  By contracting strongly connected components of $0$-length arcs and pushing blocking flows capped at $\Delta$, Goldberg–Rao reduces each scaling phase of $\Delta$ to a unit-network-like blocking flow problem, achieving weakly polynomial time $O(\min(V^{2/3}, E^{1/2}) E \log(V^2/E) \log U)$.

---

### 3.5 Capacity Scaling and Highest-Label Preflow-Push (HLPP)

#### Capacity Scaling ($O(E^2 \log U)$ and $O(VE \log U)$ — Edmonds & Karp 1972; Gabow 1985)
Let $U = \max_{e \in E} c(e)$, and initialize the scale parameter $\Delta = 2^{\lfloor \log_2 U \rfloor}$. In the **$\Delta$-scaling phase**, consider the **$\Delta$-residual network** $G_f(\Delta) = (V, \{e \in E_f : c_f(e) \ge \Delta\})$:
1. While an $s$-$t$ path (or blocking flow) exists in $G_f(\Delta)$, augment along it (each augmentation pushes $\ge \Delta$ flow).
2. When no $s$-$t$ path remains in $G_f(\Delta)$, let $S_\Delta$ be the set of vertices reachable from $s$ in $G_f(\Delta)$. Every residual arc crossing from $S_\Delta$ to $V \setminus S_\Delta$ in $G_f$ has capacity strictly less than $\Delta$, so:
   $$|f^*| - |f| \le \sum_{e \in \delta^+_{G_f}(S_\Delta)} c_f(e) < |E| \cdot \Delta$$
3. Halve $\Delta \gets \Delta / 2$. At the start of the new $(\Delta/2)$-phase, the remaining augmentable flow is at most $|E|\Delta$, and each augmentation pushes at least $\Delta/2$, so **at most $2|E|$ augmentations** occur per scaling phase! Across $\lfloor \log_2 U \rfloor + 1$ phases, this yields $O(E^2 \log U)$ with BFS or $O(VE \log U)$ with Dinic blocking flows.

#### Highest-Label Preflow-Push (HLPP — Goldberg & Tarjan 1988; Cheriyan & Maheshwari 1989)
Instead of maintaining global conservation $\text{div}_f(u) = 0$ and searching for $s$-$t$ paths (which fails to meet the $O(V^2\sqrt{E})$ bound), **Preflow-Push** relaxes conservation to allow nonnegative **excess** $\text{ex}(u) = \sum_{e \in \delta^-(u)} f(e) - \sum_{e \in \delta^+(u)} f(e) \ge 0$ for all $u \in V \setminus \{s, t\}$, and maintains **height (distance) labels** $h: V \to \mathbb{Z}_{\ge 0}$ satisfying:
- $h(s) = |V|$, $h(t) = 0$, and **Residual Height Validity**: $h(u) \le h(v) + 1$ for every residual arc $(u \to v) \in E_f$.
- Notice that if $h(s) = |V|$, $h(t) = 0$, and $h(u) \le h(v) + 1$ across all edges of $E_f$, **no directed $s$-$t$ path can exist in $G_f$** (since a simple path has at most $|V| - 1$ edges, across which $h$ can drop by at most $|V| - 1 < |V|$)!

An active node $u \in V \setminus \{s, t\}$ ($\text{ex}(u) > 0$) either **pushes** excess along an admissible arc $(u \to v) \in E_f$ with $h(u) = h(v) + 1$, or **relabels** $h(u) \gets 1 + \min_{(u \to v) \in E_f} h(v)$ when no admissible arc exists. By always selecting an active vertex $u$ of **maximum height $h(u)$** (HLPP), the number of non-saturating pushes drops from $O(V^2 E)$ to $O(V^2 \sqrt{E})$, giving total complexity **$O(V^2 \sqrt{E})$**.

Two essential practical optimizations make HLPP orders of magnitude faster on dense graphs:
1. **Global Relabeling**: Periodically (every $\Theta(V)$ relabels, and once at initialization) run a reverse BFS from $t$ in $G_f$ to set $h(u) = d_{G_f}(u, t)$.
2. **Gap Relabeling (`cnt[h] == 0`)**: Maintain the count `cnt[h]` of vertices at each height $h < |V|$. If relabeling $u$ causes `cnt[old_h]` to drop to $0$, then no vertex with $old\_h < h(v) < |V|$ can ever reach $t$ in $G_f$ (the gap at $old\_h$ is an impassable barrier under $h(x) \le h(y) + 1$). Immediately lift all such vertices to $h(v) = |V| + 1$ so they stop trying to reach $t$.

> [!CAUTION]
> **The HLPP Phase-1 vs. Phase-2 Pitfall (Corrupted Internal Edge Flows)**:
> Competitive programming HLPP templates universally restrict the active-vertex bucket to heights $h(u) < |V|$, terminating **Phase 1** as soon as all active nodes with $h(u) < |V|$ have $\text{ex}(u) = 0$.
> - **What is valid after Phase 1?** The sink excess $\text{ex}(t)$ equals the **exact maximum flow value** $|f^*|$, and the height gap partition $\{v : h(v) \ge |V|\}$ defines a valid **minimum $s$-$t$ cut**!
> - **What is BROKEN after Phase 1?** Vertices $u$ with $h(u) \ge |V|$ still hold strictly positive trapped excess $\text{ex}(u) > 0$ ($\text{div}_f(u) \neq 0$)! The edge values $f(e)$ form a **preflow, NOT a valid flow**!
> - If a problem requires inspecting individual edge flows $f(e)$ (e.g., matching reconstruction, path decomposition, lower-bound circulation feasibility, or `[AHOI2009]` residual SCCs), you **must run Phase 2** (running reverse BFS from $s$ to assign heights $h(u) = |V| + d_{G_f}(u, s)$ and pushing all remaining trapped excess $\text{ex}(u) > 0$ back into $s$) — or simply use Dinic!

---

## 4. Iteration 03 / 55 Reconciled: The Distributive Minimum-Cut Lattice, Picard–Queyranne DAG, and Dynamic Flow Rollback (`退流`)

### 4.1 The 16-Region Partition Proof of Cut Submodularity and the Distributive Lattice

Why do the minimum $s$-$t$ cuts of a directed network form a **distributive lattice** closed under set intersection and union?

#### Theorem 4.1 (Submodularity of Directed Cut Capacity)
Let $G = (V, E, c)$ be any directed network with nonnegative capacities $c \ge 0$. For **any** two vertex subsets $A, B \subseteq V$:
$$\kappa(A) + \kappa(B) = \kappa(A \cup B) + \kappa(A \cap B) + c(A \setminus B, B \setminus A) + c(B \setminus A, A \setminus B) \ge \kappa(A \cup B) + \kappa(A \cap B)$$

*Proof by 16-Region Partition Double-Counting*:
Every vertex $v \in V$ belongs to one of four pairwise disjoint regions:
$$R_{11} = A \cap B, \qquad R_{10} = A \setminus B, \qquad R_{01} = B \setminus A, \qquad R_{00} = V \setminus (A \cup B)$$
Every directed edge $e = (u \to v) \in E$ connects one of the $4 \times 4 = 16$ ordered pairs of regions $(R_{ij} \to R_{kl})$. Notice that:
- $A = R_{11} \sqcup R_{10}$ and $V \setminus A = R_{01} \sqcup R_{00}$.
- $B = R_{11} \sqcup R_{01}$ and $V \setminus B = R_{10} \sqcup R_{00}$.
- $A \cup B = R_{11} \sqcup R_{10} \sqcup R_{01}$ and $V \setminus (A \cup B) = R_{00}$.
- $A \cap B = R_{11}$ and $V \setminus (A \cap B) = R_{10} \sqcup R_{01} \sqcup R_{00}$.

Now compare how many times each cross-region capacity $c(R_{ij}, R_{kl})$ is counted on the Left-Hand Side $\kappa(A) + \kappa(B)$ versus the Right-Hand Side $\kappa(A \cup B) + \kappa(A \cap B)$:

| Directed Region Pair $(R_{ij} \to R_{kl})$ | In $\delta^+(A)$? | In $\delta^+(B)$? | LHS Count ($\kappa(A) + \kappa(B)$) | In $\delta^+(A \cup B)$? | In $\delta^+(A \cap B)$? | RHS Count ($\kappa(A \cup B) + \kappa(A \cap B)$) | Difference $(\text{LHS} - \text{RHS})$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $R_{11} \to R_{00}$ | $1$ | $1$ | **$2$** | $1$ | $1$ | **$2$** | $0$ |
| $R_{11} \to R_{10}$ | $0$ | $1$ | **$1$** | $0$ | $1$ | **$1$** | $0$ |
| $R_{11} \to R_{01}$ | $1$ | $0$ | **$1$** | $0$ | $1$ | **$1$** | $0$ |
| $R_{10} \to R_{00}$ | $1$ | $0$ | **$1$** | $1$ | $0$ | **$1$** | $0$ |
| $R_{01} \to R_{00}$ | $0$ | $1$ | **$1$** | $1$ | $0$ | **$1$** | $0$ |
| **$R_{10} \to R_{01}$ ($A \setminus B \to B \setminus A$)** | **$1$** | **$0$** | **$1$** | **$0$** | **$0$** | **$0$** | **$+1$** |
| **$R_{01} \to R_{10}$ ($B \setminus A \to A \setminus B$)** | **$0$** | **$1$** | **$1$** | **$0$** | **$0$** | **$0$** | **$+1$** |
| All other 9 pairs ($R_{00} \to *$, $R_{ij} \to R_{ij}$, $R_{10/01} \to R_{11}$) | $0$ | $0$ | **$0$** | $0$ | $0$ | **$0$** | $0$ |

Every single pair matches identically except $(A \setminus B \to B \setminus A)$ and $(B \setminus A \to A \setminus B)$, proving the exact identity! Since $c \ge 0$, $\kappa(A) + \kappa(B) \ge \kappa(A \cup B) + \kappa(A \cap B)$. $\blacksquare$

#### Corollary 4.2 (The Distributive Lattice of Minimum $s$-$t$ Cuts)
Let $\lambda^* = \min_{s \in S \subseteq V \setminus \{t\}} \kappa(S)$ be the minimum $s$-$t$ cut capacity, and let $\mathcal{L}_{\min} = \{S \subseteq V : s \in S, t \notin S, \kappa(S) = \lambda^*\}$ be the family of all minimum $s$-$t$ cuts. If $A, B \in \mathcal{L}_{\min}$, then both $A \cap B$ and $A \cup B$ are valid $s$-$t$ cuts ($s \in A \cap B \subseteq A \cup B \subseteq V \setminus \{t\}$), so $\kappa(A \cap B) \ge \lambda^*$ and $\kappa(A \cup B) \ge \lambda^*$. By Theorem 4.1:
$$2\lambda^* = \kappa(A) + \kappa(B) \ge \kappa(A \cup B) + \kappa(A \cap B) \ge \lambda^* + \lambda^* = 2\lambda^*$$
Hence equality holds throughout: **$\kappa(A \cap B) = \kappa(A \cup B) = \lambda^*$**, so $(\mathcal{L}_{\min}, \subseteq, \cap, \cup)$ is a finite **distributive lattice**! Furthermore, $c(A \setminus B, B \setminus A) = c(B \setminus A, A \setminus B) = 0$.

---

### 4.2 Extremal Cuts $S_{\min}, S_{\max}$, Uniqueness Criterion, and the Picard–Queyranne DAG

Fix **any** maximum flow $f^*$ in $G$, and let $G_{f^*}$ be its residual network. By Lemma 2.3 and Theorem 2.4, an $s$-$t$ cut $(S, V \setminus S)$ belongs to $\mathcal{L}_{\min}$ **if and only if** $\delta^+_{G_{f^*}}(S) = \emptyset$ (i.e., $S$ is a **reachability-closed** set in $G_{f^*}$: if $u \in S$ and $(u \to v) \in E_{f^*}$, then $v \in S$).

Because $\mathcal{L}_{\min}$ is a finite lattice closed under $\cap$ and $\cup$, it possesses a **unique minimum element** (the source-minimal cut $S_{\min} = \bigcap_{S \in \mathcal{L}_{\min}} S$) and a **unique maximum element** (the source-maximal cut $S_{\max} = \bigcup_{S \in \mathcal{L}_{\min}} S$):
1. **Source-Minimal Minimum Cut ($S_{\min}$)**:
   $$S_{\min} = \{v \in V : s \leadsto v \text{ in } G_{f^*}\}$$
   (Computed by a single forward BFS/DFS from $s$ in $G_{f^*}$.)
2. **Source-Maximal Minimum Cut ($S_{\max}$)** and **Sink-Minimal Cut ($T_{\min} = V \setminus S_{\max}$)**:
   $$T_{\min} = \{v \in V : v \leadsto t \text{ in } G_{f^*}\}, \qquad S_{\max} = V \setminus T_{\min} = \{v \in V : v \not\leadsto t \text{ in } G_{f^*}\}$$
   (Computed by a single reverse BFS/DFS from $t$ along reversed arcs of $G_{f^*}$.)

#### Corollary 4.3 (Minimum Cut Uniqueness Criterion — `[ZOJ 2587 / UVa 10480]`)
The network $G$ has a **unique** minimum $s$-$t$ cut ($|\mathcal{L}_{\min}| = 1$) if and only if $S_{\min} = S_{\max}$, which is equivalent to:
$$S_{\min} \cup T_{\min} = V \iff |S_{\min}| + |T_{\min}| = |V|$$
That is, every vertex $v \in V$ is either reachable from $s$ in $G_{f^*}$ or can reach $t$ in $G_{f^*}$.

#### Theorem 4.4 (Picard–Queyranne Characterization of All Minimum Cuts, 1980)
Contract every Strongly Connected Component (SCC) of the residual network $G_{f^*}$ into a single supernode to form the **Residual Condensation DAG** $\mathcal{D}(G_{f^*})$. Let $\text{SCC}(v)$ denote the component containing $v$. Then:
1. $\text{SCC}(s) \neq \text{SCC}(t)$ (since $s \not\leadsto t$ in $G_{f^*}$).
2. A partition $(S, V \setminus S)$ with $s \in S, t \notin S$ is a minimum $s$-$t$ cut **if and only if** $S$ is the union of a **downward-closed (out-closed) ideal** of SCCs in $\mathcal{D}(G_{f^*})$ that contains $\text{SCC}(s)$ and excludes $\text{SCC}(t)$.

---

### 4.3 Complete Classification of Feasible vs. Essential Minimum-Cut Edges (`[AHOI2009] 最小割`)

Given a directed network $G = (V, E, c)$, when can a physical directed edge $e = (u \to v) \in E$ belong to **at least one** minimum $s$-$t$ cut (**Feasible Cut Edge** / `可行边`), and when does it belong to **every** minimum $s$-$t$ cut (**Essential Cut Edge** / `必须边`)?

#### Theorem 4.5 (The `[AHOI2009]` Tarjan SCC Edge Classification Theorem)
Run Dinic's algorithm once to obtain a maximum flow $f^*$, and run Tarjan's SCC algorithm once on the residual network $G_{f^*}$ to assign each vertex $w \in V$ its component ID $\text{scc}[w]$. Then for every physical edge $e = (u \to v) \in E$:
1. **Feasible Minimum-Cut Edge (`可行边` — $\exists S \in \mathcal{L}_{\min}$ with $e \in \delta^+(S)$)**:
   $$e \text{ is feasible} \iff f^*(e) = c(e) \;\;\land\;\; \text{scc}[u] \neq \text{scc}[v]$$
2. **Essential Minimum-Cut Edge (`必须边` — $\forall S \in \mathcal{L}_{\min}, e \in \delta^+(S)$)**:
   $$e \text{ is essential} \iff f^*(e) = c(e) \;\;\land\;\; \text{scc}[u] = \text{scc}[s] \;\;\land\;\; \text{scc}[v] = \text{scc}[t]$$

Wait — condition (1) looks almost *too* simple! To place $u \in S$ and $v \notin S$ in a valid $s$-$t$ cut $S \in \mathcal{L}_{\min}$, we also need $u \not\leadsto t$ and $s \not\leadsto v$ in $G_{f^*}$ (so that putting $u \in S$ doesn't drag $t$ into $S$, and keeping $v \notin S$ doesn't exclude $s$ from $S$). **Why didn't condition (1) need to check $u \not\leadsto t$ or $s \not\leadsto v$?** We reconcile Cohort 1's Cut-Conservation Proof and Cohort 2's Flow-Decomposition Proof (`Lemma 55.3`), both of which reveal a profound structural invariant of $G_{f^*}$:

#### Lemma 4.6 (Automatic Source/Sink Separation of Saturated Cross-SCC Edges)
If $e = (u \to v) \in E$ satisfies $f^*(e) = c(e) > 0$ and $\text{scc}[u] \neq \text{scc}[v]$ in $G_{f^*}$, then in $G_{f^*}$:
1. $u \to^* s$ (hence $u \not\to^* t$, since $s \not\to^* t$), and
2. $t \to^* v$ (hence $s \not\to^* v$, since $s \not\to^* t$).

*Proof 1 (Cohort 1 — Residual Reachability Cut Conservation)*:
Because $f^*(e) = c(e) > 0$, the backward residual arc $e^{\text{rev}} = (v \to u)$ exists in $G_{f^*}$ with capacity $c_{f^*}(e^{\text{rev}}) = f^*(e) > 0$. Since $\text{scc}[u] \neq \text{scc}[v]$ and $v \to u \in E_{f^*}$, we must have $u \not\to^* v$ in $G_{f^*}$.
Define the reachability set $R(u) = \{w \in V : u \to^* w \text{ in } G_{f^*}\}$. By definition, $u \in R(u)$, $v \notin R(u)$, and **no residual arc in $G_{f^*}$ leaves $R(u)$** ($\delta^+_{G_{f^*}}(R(u)) = \emptyset$). Thus:
- Every physical edge leaving $R(u)$ is fully saturated ($f^* = c$), and every physical edge entering $R(u)$ carries zero flow ($f^* = 0$).
- In particular, $e = (u \to v) \in \delta^+(R(u))$ carries strictly positive flow $f^*(e) = c(e) > 0$.
- Therefore, the net physical outflow of $R(u)$ is strictly positive:
  $$\sum_{w \in R(u)} \text{div}_{f^*}(w) = \sum_{e' \in \delta^+(R(u))} f^*(e') - \sum_{e' \in \delta^-(R(u))} f^*(e') \ge f^*(e) > 0$$
- However, every vertex $w \in V \setminus \{s, t\}$ has $\text{div}_{f^*}(w) = 0$, while $\text{div}_{f^*}(t) = -|f^*| < 0$ and $\text{div}_{f^*}(s) = +|f^*| > 0$. The **only** way $\sum_{w \in R(u)} \text{div}_{f^*}(w) > 0$ can hold is if $s \in R(u)$ and $t \notin R(u)$! Thus $u \to^* s$ and $u \not\to^* t$. By a symmetric argument on $R^{-1}(v) = \{w : w \to^* v \text{ in } G_{f^*}\}$, we obtain $t \in R^{-1}(v)$ and $s \notin R^{-1}(v)$. $\blacksquare$

*Proof 2 (Cohort 2 — Path–Cycle Flow Decomposition)*:
Decompose $f^*$ into weighted $s$-$t$ paths $\mathcal{P}$ and cycles $\mathcal{C}$. Since $f^*(e) = c(e) > 0$, edge $e = (u \to v)$ belongs either to a cycle $C \in \mathcal{C}$ or to an $s$-$t$ path $P \in \mathcal{P}$.
- If $e \in C$, then every edge of $C$ has positive flow, so their reverse arcs in $G_{f^*}$ form a directed path $u \leadsto v$ in $G_{f^*}$, contradicting $u \not\to^* v$.
- Thus $e$ lies on a flow-carrying $s$-$t$ path $P = (s \leadsto u \xrightarrow{e} v \leadsto t)$. The reverse arcs of the prefix $s \leadsto u$ form a directed path $u \to^* s$ in $G_{f^*}$, and the reverse arcs of the suffix $v \leadsto t$ form a directed path $t \to^* v$ in $G_{f^*}$! $\blacksquare$

*Completing the Proof of Theorem 4.5*:
- **Feasible (`可行边`)**: $(\implies)$ If $e \in \delta^+(S)$ for $S \in \mathcal{L}_{\min}$, then $f^*(e) = c(e)$ by Lemma 2.3, and since $u \in S, v \notin S$ and $S$ is out-closed in $G_{f^*}$, $u \not\to^* v$, so $\text{scc}[u] \neq \text{scc}[v]$. $(\Longleftarrow)$ If $f^*(e) = c(e)$ and $\text{scc}[u] \neq \text{scc}[v]$, set $S = \{w \in V : s \to^* w \text{ or } u \to^* w \text{ in } G_{f^*}\}$. By Lemma 4.6, $v \notin S$ and $t \notin S$, while $s, u \in S$ and $S$ is out-closed in $G_{f^*}$, so $S \in \mathcal{L}_{\min}$ cuts $e$.
- **Essential (`必须边`)**: $e \in \delta^+(S)$ for **all** $S \in \mathcal{L}_{\min} \iff u \in \bigcap_{S \in \mathcal{L}_{\min}} S = S_{\min}$ and $v \in \bigcap_{S \in \mathcal{L}_{\min}} (V \setminus S) = T_{\min}$. Since $f^*(e) = c(e) > 0$, Lemma 4.6 already gives $u \to^* s$ and $t \to^* v$. Combining $s \to^* u$ ($u \in S_{\min}$) with $u \to^* s$ yields $\text{scc}[u] = \text{scc}[s]$; combining $v \to^* t$ ($v \in T_{\min}$) with $t \to^* v$ yields $\text{scc}[v] = \text{scc}[t]$. $\blacksquare$

---

### 4.4 Parametric Capacity Sensitivity and Minimum-Cardinality Perturbation

1. **Single-Edge Parametric Sensitivity ($\Delta c(e) = \pm \epsilon$ for sufficiently small $\epsilon > 0$)**:
   Let $\lambda^*(c)$ be the minimum cut value as a function of edge capacities:
   - **Increasing $c(e)$ by $+\epsilon$**: $\lambda^*(c + \epsilon \mathbf{e}_e) = \lambda^*(c) + \epsilon \iff$ **every** minimum cut contains $e$ ($e$ is an **Essential Cut Edge**, i.e., $f^*(e) = c(e) \land \text{scc}[u] = \text{scc}[s] \land \text{scc}[v] = \text{scc}[t]$) $\iff u \to^* v$ does not hold in $G_{f^*}$ even without $e$, and $s \to^* u \land v \to^* t$ in $G_{f^*}$. Otherwise $\lambda^*$ stays unchanged.
   - **Decreasing $c(e)$ by $-\epsilon$ ($c(e) > 0$)**: $\lambda^*(c - \epsilon \mathbf{e}_e) = \lambda^*(c) - \epsilon \iff$ **at least one** minimum cut contains $e$ ($e$ is a **Feasible Cut Edge**, i.e., $f^*(e) = c(e) \land \text{scc}[u] \neq \text{scc}[v]$).
2. **Minimum-Cardinality Minimum Cut via Lexicographic Capacity Perturbation**:
   When a problem asks for the minimum $s$-$t$ cut $(S, T)$ that **first minimizes total capacity $\kappa(S)$** and **second minimizes the number of cut edges $|\delta^+(S)|$**, replace every edge capacity $c(e) \in \mathbb{Z}_{\ge 0}$ with the perturbed integer capacity:
   $$\tilde{c}(e) = c(e) \cdot (|E| + 1) + 1$$
   Then for any $s$-$t$ cut $S$:
   $$\tilde{\kappa}(S) = \sum_{e \in \delta^+(S)} \tilde{c}(e) = \kappa(S) \cdot (|E| + 1) + |\delta^+(S)|$$
   Because $0 \le |\delta^+(S)| \le |E| < |E| + 1$, minimizing $\tilde{\kappa}(S)$ simultaneously recovers both the minimum cut value $\kappa(S^*) = \lfloor \tilde{\kappa}(S^*) / (|E| + 1) \rfloor$ and the minimum edge count $|\delta^+(S^*)| = \tilde{\kappa}(S^*) \bmod (|E| + 1)$ in a **single** Max-Flow execution!

---

### 4.5 Dynamic Single-Edge Flow Rollback (`退流` — `[SDOI2014] LIS`)

Suppose we have already computed a maximum flow $f^*$ on $G$, and we now need to **permanently delete** a physical edge $e = (u \to v)$ (setting $c(e) \gets 0$) and update the residual network $G_{f^*}$ to a valid maximum-flow state **without re-running Dinic from scratch** (which would cost $O(|V| \cdot \text{Dinic})$ when deleting $|V|$ edges sequentially, as in `P24 [SDOI2014] LIS`).

#### The `退流` (Flow Rollback) Algorithm
Suppose edge $e = (u \to v)$ currently carries physical flow $k = f^*(e) = c(e) - \text{cap}[e]$.
- **Case 1 ($k = 0$)**: Simply set $\text{cap}[e] = \text{cap}[e \oplus 1] = 0$. No flow conservation is violated.
- **Case 2 ($k > 0$, General Edge)**: Setting $\text{cap}[e] = \text{cap}[e \oplus 1] = 0$ destroys $k$ units of flow on $u \to v$, creating a flow excess of $+k$ at $u$ (relative to $s$) and a flow deficit of $-k$ at $v$ (relative to $t$). To restore Kirchhoff conservation:
  1. Zero out both half-edges of $e$: $\text{cap}[e] \gets 0$, $\text{cap}[e \oplus 1] \gets 0$.
  2. Push up to $k$ units of flow from $t$ to $v$ in the current residual graph $G_{f^*}$: `dinic_bounded(t, v, k)` (reeling back the suffix flow $v \leadsto t$).
  3. Push up to $k$ units of flow from $u$ to $s$ in the current residual graph $G_{f^*}$: `dinic_bounded(u, s, k)` (reeling back the prefix flow $s \leadsto u$).
  4. (If $e$ was not proven to be a feasible minimum-cut edge, run `dinic(s, t)` to re-augment any alternative $s$-$t$ paths.)
- **Case 2b ($k = c(e) > 0$ and $e$ is a Feasible Minimum-Cut Edge, i.e., $u \not\to^* v$ in $G_{f^*}$)**:
  By Lemma 4.6, $u \to^* s$ and $t \to^* v$ hold with $k$ units of capacity in $G_{f^*}$, and deleting $e$ reduces the global Max-Flow by **exactly $k$**! Thus steps 2 and 3 (`dinic_bounded(t, v, k)` and `dinic_bounded(u, s, k)`) are **guaranteed to push the full $k$ units**, and **step 4 (`dinic(s, t)`) is completely unnecessary** because $s \not\to^* t$ still holds!
- **Complexity**: Across a sequence of deletions in `[SDOI2014] LIS`, the total flow rolled back is bounded by the initial Max-Flow $|f^*| \le N$, reducing $N$ full Dinic calls to **$O(N \cdot E)$ total rollback work**!

---

## 5. Iteration 04 / 56 Reconciled: Structural Graph Gadgets, Menger's Theorems, Time-Expanded DAGs, and Hub Sparsification

### 5.1 Vertex-Capacity Splitting ($v_{\text{in}} \xrightarrow{C_v} v_{\text{out}}$) and the Strict $\text{out} \to \text{in}$ Port Invariant

#### Step 1: Non-Graph Diagnostic Signal
A problem restricts the throughput, durability, or destruction cost of **vertices** (tolls, routers, stepping pillars, grid cells) rather than transitions: *"at most $C_v$ paths/agents may pass through vertex $v$"* or *"destroying vertex $v$ costs $w_v$; find the minimum-cost set of vertices to block all $s$-$t$ paths."*

#### Step 2: Intermediate Algebraic Representation
In standard edge-capacitated flow, conservation at $v \notin \{s, t\}$ states that the total throughput $F(v)$ passing through $v$ is:
$$F(v) = \sum_{e \in \delta^-(v)} f(e) = \sum_{e \in \delta^+(v)} f(e)$$
We must enforce the vertex-throughput inequality $0 \le F(v) \le C_v$ using only edge capacities.

#### Step 3: Reverse-Engineering Scratchpad (Mechanical Graph Compilation)
To convert the vertex-sum $F(v)$ into a single edge flow $f(e_v)$, separate the **arrival event** ($\sum_{e \in \delta^-(v)} f(e)$) from the **departure event** ($\sum_{e \in \delta^+(v)} f(e)$) by splitting $v$ into two half-vertices: an **in-port** $v_{\text{in}}$ and an **out-port** $v_{\text{out}}$ connected by a single directed internal bridge:
$$e_v = (v_{\text{in}} \to v_{\text{out}}), \qquad c(v_{\text{in}} \to v_{\text{out}}) = C_v$$
- Every original incoming edge $(u \to v) \in \delta^-(v)$ now enters $v_{\text{in}}$ from $u_{\text{out}}$: **$(u_{\text{out}} \to v_{\text{in}})$**.
- Every original outgoing edge $(v \to w) \in \delta^+(v)$ now leaves $v_{\text{out}}$ to $w_{\text{in}}$: **$(v_{\text{out}} \to w_{\text{in}})$**.
- By Kirchhoff conservation at $v_{\text{in}}$, $f(v_{\text{in}} \to v_{\text{out}}) = \sum_{e \in \delta^-(v)} f(e) = F(v)$, so $0 \le f(v_{\text{in}} \to v_{\text{out}}) \le C_v$ enforces $F(v) \le C_v$!
- **Source and Sink Convention**: If $s$ and $t$ cannot be destroyed/capacitated, route the network from **$s_{\text{out}}$ to $t_{\text{in}}$** (or set $C_s = C_t = \infty$ and route from $s_{\text{in}}$ to $t_{\text{out}}$).
- **Recovering the Cut Vertices from $S_{\min}$**: After computing Max-Flow, let $S_{\min}$ be the set of vertices reachable from the source in $G_{f^*}$. A vertex $v$ belongs to the source-minimal minimum vertex cut if and only if its internal bridge is cut by $S_{\min}$:
  $$v_{\text{in}} \in S_{\min} \;\;\land\;\; v_{\text{out}} \notin S_{\min}$$

> [!CAUTION]
> **Broken Gadget Counterexample — The Port-Bypass Bug ($u_{\text{in}} \to v_{\text{in}}$ or $u_{\text{out}} \to v_{\text{out}}$)**:
> If you accidentally wire an original edge $(u, v)$ as $u_{\text{in}} \to v_{\text{in}}$, then flow arriving at $u_{\text{in}}$ can immediately exit to $v_{\text{in}}$ **without ever crossing the internal bridge $u_{\text{in}} \to u_{\text{out}}$**, giving vertex $u$ effectively infinite capacity! Every external transition MUST go strictly from an **`out`-port to an `in`-port**: $u_{\text{out}} \to v_{\text{in}}$.

---

### 5.2 Undirected-to-Directed Compact Pairs, Physical Flow Recovery, and the MCMF Trap

#### Step 1 & 2: Algebraic Equivalence of Undirected Capacity
An undirected edge $e = \{u, v\}$ of capacity $C$ permits net flow of at most $C$ in either direction: $-C \le f_{\text{net}}(u \to v) \le C$. If we represent $e$ by two opposite directed flows $f(u \to v), f(v \to u) \in [0, C]$, any simultaneous positive flow in both directions cancels out physically:
$$f_{\text{net}}(u \to v) = f(u \to v) - f(v \to u) \in [-C, +C]$$

#### Step 3 & 4: Two Valid Representations for Pure Max-Flow — and Why Compact Pairs Fail in MCMF!
1. **Standard 2-Directed-Edge Representation (4 Half-Edges)**: Insert two independent directed edges $(u \to v, C)$ and $(v \to u, C)$. Always safe in both Max-Flow and MCMF.
2. **Compact 1-Pair Shortcut (2 Half-Edges — Pure Uncosted Max-Flow Only!)**: Allocate a single pair of half-edges `(2k, 2k+1)` with **both initial residual capacities equal to $C$**:
   $$\text{cap}[2k] = C \quad (u \to v), \qquad \text{cap}[2k+1] = C \quad (v \to u)$$
   Why does this work? At any point, $\text{cap}[2k] + \text{cap}[2k+1] = 2C$. If net flow $f \in [0, C]$ moves from $u$ to $v$, then $\text{cap}[2k] = C - f \in [0, C]$ (remaining forward room) and $\text{cap}[2k+1] = C + f \in [C, 2C]$ (which equals $f$ units of flow cancellation $v \to u$ plus $C$ units of fresh flow $v \to u$!).
   - **Physical Flow Recovery Formula**: The physical flow routed from $u$ to $v$ is:
     $$f_{\text{phys}}(u \to v) = \max(0, C - \text{cap}[2k]) = \max(0, \text{cap}[2k+1] - C)$$

> [!WARNING]
> **Why the 2-Half-Edge Compact Shortcut FAILS Catastrophically in Min-Cost Max-Flow (MCMF)**:
> Suppose an undirected edge $\{u, v\}$ has capacity $C$ and traversal cost $+w > 0$ in either direction.
> - **Physical reality**: Routing 1 unit $u \to v$ costs $+w$. Cancelling that 1 unit via the reverse residual arc $v \to u$ must **refund $-w$**, whereas routing 1 unit of fresh flow $v \to u$ costs **$+w$**!
> - Because the compact 2-half-edge shortcut merges the reverse residual arc of $(u \to v)$ (cost $-w$) and the forward physical arc $(v \to u)$ (cost $+w$) into a **single half-edge `2k+1`**, no single scalar cost can represent both $-w$ and $+w$! In MCMF, you **must** use two separate directed edges (4 half-edges total): $(u \to v, \text{cap}=C, \text{cost}=+w)$ with reverse $(\text{cap}=0, \text{cost}=-w)$, and $(v \to u, \text{cap}=C, \text{cost}=+w)$ with reverse $(\text{cap}=0, \text{cost}=-w)$.

---

### 5.3 Menger's Four Connectivity Theorems and the 6-Vertex Diamond-Bridge Greedy Failure

By combining unit edge capacities, vertex splitting ($v_{\text{in}} \xrightarrow{1} v_{\text{out}}$), and the Integrality & Flow Decomposition Theorems, Ford–Fulkerson immediately yields all four variants of **Menger's Theorem (1927)**:

| Menger Variant | Max Disjoint $s$-$t$ Paths $=$ Min $s$-$t$ Cut | Graph Compilation Gadget | Dinic Complexity |
| :--- | :--- | :--- | :--- |
| **1. Directed Edge-Disjoint** | Max edge-disjoint directed paths $=$ Min directed edge cut $\lambda_{\text{dir}}(s, t)$ | Every directed edge $e = (u \to v)$ gets capacity $c(e) = 1$. | **$O(E \min(E^{1/2}, V^{2/3}))$** |
| **2. Undirected Edge-Disjoint** | Max edge-disjoint undirected paths $=$ Min undirected edge cut $\lambda_{\text{undir}}(s, t)$ | Every undirected edge $\{u, v\}$ becomes compact pair $\text{cap}[2k] = \text{cap}[2k+1] = 1$. | **$O(E \min(E^{1/2}, V^{2/3}))$** |
| **3. Directed Vertex-Disjoint** ($s \not\to t$) | Max internally vertex-disjoint directed paths $=$ Min directed vertex cut $\kappa_{\text{dir}}(s, t)$ | Split $v \notin \{s, t\}$ into $v_{\text{in}} \xrightarrow{1} v_{\text{out}}$; replace $(u \to v)$ with $u_{\text{out}} \to v_{\text{in}}$ (cap $\infty$). | **$O(E \sqrt{V})$** (Even–Tarjan) |
| **4. Undirected Vertex-Disjoint** ($\{s, t\} \notin E$) | Max internally vertex-disjoint undirected paths $=$ Min undirected vertex cut $\kappa_{\text{undir}}(s, t)$ | Split $v \notin \{s, t\}$ into $v_{\text{in}} \xrightarrow{1} v_{\text{out}}$; replace $\{u, v\}$ with $u_{\text{out}} \xrightarrow{\infty} v_{\text{in}}$ and $v_{\text{out}} \xrightarrow{\infty} u_{\text{in}}$. | **$O(E \sqrt{V})$** (Even–Tarjan) |

#### Counterexample 5.1: The 6-Vertex Diamond-Bridge Trace (Why Naive Greedy Shortest-Path Extraction Fails)
Why can't we find the maximum number of edge-disjoint $s$-$t$ paths by repeatedly running BFS to find a shortest $s$-$t$ path and deleting its edges?
Construct the **6-Vertex Diamond-Bridge Graph** $V = \{s, a, b, u, v, t\}$ with 7 unit-capacity directed edges:
- Upper bypass: $s \to u \to b \to t$ (length 3) and $s \to a \to v \to t$ (length 3).
- Central bridge: $u \to v$ (length 1).
- **Greedy BFS Step 1**: The unique shortest $s$-$t$ path is $P_{\text{greedy}} = (s \to u \to v \to t)$ of length 3. Deleting its edges $\{s \to u, u \to v, v \to t\}$ leaves **zero** paths from $s$ to $t$ (since $s$'s only remaining outgoing edge is $s \to a \to v$, and $v$'s only outgoing edge $v \to t$ was just deleted!). Greedy terminates with **1 path**.
- **Dinic / Residual Path-Splicing Step 2**: In $G_f$, the reverse residual arc $v \to u$ has capacity $1$. Dinic finds the augmenting path $s \to a \to v \xrightarrow{v \to u} u \to b \to t$ of length 5! Pushing 1 unit along $v \to u$ cancels the flow on $u \to v$ and splices the flow into **2 edge-disjoint paths**: $P_1 = (s \to u \to b \to t)$ and $P_2 = (s \to a \to v \to t)$.

---

### 5.4 Time-Expanded Layered DAGs (`分层图`) and Incremental Dynamic Layer Addition (`动态加层`)

#### Step 1: Non-Graph Diagnostic Signal
Agents move across a graph over discrete time steps $t = 0, 1, 2, \dots, T$. Edges have transit times $\Delta t \ge 1$ and per-step capacities, agents can wait at vertices across time steps, or edges move cyclically over time (as in `P10 [CTSC1999] 星际转移问题`). We want either the maximum number of agents delivered by time $T$, or the **minimum time $T^*$** required to deliver $K$ agents.

#### Step 2 & 3: Algebraic State Space and Mechanical Graph Compilation
Unroll time into the vertex state space $V_T = V \times \{0, 1, \dots, T\}$, where node $(u, t)$ represents location $u$ at time $t$:
- **Waiting / Holding Edges**: If up to $h_u$ agents can wait at vertex $u$ from time $t-1$ to $t$, add $((u, t-1) \to (u, t))$ with capacity $h_u$ (often $\infty$).
- **Transit Edges**: If an edge/shuttle moves from $u$ at time $t-1$ to $v$ at time $t$ with capacity $c_e$, add $((u, t-1) \to (v, t))$ with capacity $c_e$.
- **Sink Aggregation**: Connect $(t_{\text{dest}}, t) \to \text{Sink}$ with capacity $\infty$ for each $t \in \{0, \dots, T\}$.

> [!TIP]
> **Incremental Dynamic Layer Addition (`动态加层`) vs. Binary Search on $T$**:
> Because Dinic's algorithm operates directly on the residual graph $G_f$, to find the minimum time $T^*$ at which total flow reaches $K$, **do NOT binary search on $T$ and rebuild the graph from scratch**!
> Instead, maintain a single persistent residual network $G_f$: at step $T = 1, 2, 3, \dots$, append the new layer of vertices $V \times \{T\}$ and the transition edges from $T-1$ to $T$, and call `total_flow += dinic(S, Sink)` directly on the existing residual graph! Each new layer inherits all previous residual paths and only augments the newly unlocked flow, running $O(\log T^*)$ times faster than binary search. (Always run a DSU / BFS reachability check first so you don't loop forever when $K$ is unreachable!)

---

### 5.5 Row/Column Hub Sparsification (`[AtCoder ARC 074 D] Lotus Leaves`)

Whenever a problem allows transitions between **any two cells in the same row or the same column** of an $H \times W$ grid (with cell destruction cost $1$), naively adding pairwise edges between all cells in a row or column creates $\Theta(HW(H + W))$ edges.
- **Hub Sparsification**: Create $H$ **Row Hub vertices** $R_1, \dots, R_H$ and $W$ **Column Hub vertices** $C_1, \dots, C_W$ (each with infinite vertex capacity, since rows/columns themselves cannot be destroyed).
- Each destroyable cell $(r, c)$ is split into $(r, c)_{\text{in}} \xrightarrow{1} (r, c)_{\text{out}}$, and wired to its two hubs via $(r, c)_{\text{out}} \xrightarrow{\infty} R_r$, $R_r \xrightarrow{\infty} (r, c)_{\text{in}}$, $(r, c)_{\text{out}} \xrightarrow{\infty} C_c$, and $C_c \xrightarrow{\infty} (r, c)_{\text{in}}$.
- Furthermore, because stepping from $(r, c)$ to $R_r$ and from $R_r$ to $(r, c')$ only uses $(r, c)$ once, **we do not even need to split $(r, c)$**! Each cell $(r, c)$ is simply an **undirected edge of capacity $1$ between hub $R_r$ and hub $C_c$**! This collapses an $O(HW(H+W))$ vertex-cut graph into a tiny **$O(H + W)$-vertex, $O(HW)$-edge bipartite unit-capacity network** solved in $O(HW \sqrt{H + W})$ time!

---

## 6. Iteration 05 / 57 Reconciled: Flows with Demands and Lower Bounds (`上下界网络流`), Hoffman's Theorem, and Non-Graph Compilations

### 6.1 The Affine Slack Shift $f(e) = l(e) + \tilde{f}(e)$ and Pre-Injected Vertex Excess $M(v)$

#### Step 1: Non-Graph Diagnostic Signal
Every variable (edge flow, matrix entry, item selection count, DAG path coverage) is constrained from **both below and above**:
$$l(e) \le f(e) \le u(e) \qquad (0 \le l(e) \le u(e))$$
Standard Dinic/HLPP requires $0 \le f(e) \le c(e)$ because $f \equiv 0$ must be a valid starting point. When $l(e) > 0$, $f \equiv 0$ violates the lower bounds!

#### Step 2: Intermediate Algebraic Representation (The Affine Slack Shift)
Decompose the physical flow $f(e)$ into its mandatory **baseline flow** $l(e)$ plus a nonnegative **slack flow** $\tilde{f}(e)$:
$$f(e) = l(e) + \tilde{f}(e), \qquad 0 \le \tilde{f}(e) \le u(e) - l(e)$$
Substitute $f = l + \tilde{f}$ into Kirchhoff's conservation law $\sum_{e \in \delta^-(v)} f(e) - \sum_{e \in \delta^+(v)} f(e) = 0$:
$$\sum_{e \in \delta^-(v)} \big(l(e) + \tilde{f}(e)\big) - \sum_{e \in \delta^+(v)} \big(l(e) + \tilde{f}(e)\big) = 0$$
Move all known constant $l(e)$ terms to the right-hand side and define the **Pre-Injected Baseline Excess (Net Imbalance)** $M(v)$ at vertex $v$:
$$M(v) \triangleq \text{in}_l(v) - \text{out}_l(v) = \sum_{e \in \delta^-(v)} l(e) - \sum_{e \in \delta^+(v)} l(e)$$
Then the slack flow $\tilde{f}$ satisfies standard $[0, u(e) - l(e)]$ box bounds, **but must satisfy non-zero divergence at every vertex**:
$$\text{div}_{\tilde{f}}(v) = \sum_{e \in \delta^+(v)} \tilde{f}(e) - \sum_{e \in \delta^-(v)} \tilde{f}(e) = M(v) \qquad \forall v \in V$$
Notice that $\sum_{v \in V} M(v) = \sum_{e \in E} l(e) - \sum_{e \in E} l(e) = 0$.

#### Step 3: Reverse-Engineering Scratchpad (Compiling $M(v)$ into Super-Source $S^*$ and Super-Sink $T^*$)
What does $\text{div}_{\tilde{f}}(v) = M(v)$ mean physically?
- If **$M(v) > 0$**: The mandatory lower bounds $l(e)$ pump $M(v)$ more units of flow *into* $v$ than they drain *out* of $v$. To conserve total flow $f = l + \tilde{f}$, the slack network $\tilde{f}$ must **absorb $M(v)$ units of incoming supply at $v$ and route them out** into the rest of the network!
  $\implies$ Add a companion arc from the **Auxiliary Super-Source** $S^* \to v$ with capacity $M(v)$.
- If **$M(v) < 0$**: The mandatory lower bounds $l(e)$ drain $|M(v)| = -M(v)$ more units *out* of $v$ than they pump *in*. To replenish this deficit, the slack network $\tilde{f}$ must **deliver $|M(v)|$ units of slack flow into $v$ and drain them out**!
  $\implies$ Add a companion arc from $v \to T^*$ (the **Auxiliary Super-Sink**) with capacity $-M(v) = |M(v)|$.

Define the total positive imbalance:
$$\Sigma^+ \triangleq \sum_{v \in V : M(v) > 0} M(v) = \sum_{v \in V : M(v) < 0} (-M(v))$$
Then $\text{div}_{\tilde{f}}(v) = M(v)$ holds at every $v \in V$ **if and only if** every companion arc leaving $S^*$ (and entering $T^*$) is completely saturated by $\tilde{f}$, i.e., **$\text{MaxFlow}_{G'}(S^*, T^*) = \Sigma^+$**!

> [!CAUTION]
> **Broken Gadget Counterexample — Reversing the Sign of $M(v)$**:
> The single most common bug in `上下界网络流` is defining $M(v) = \text{out}_l(v) - \text{in}_l(v)$ and connecting $S^* \to v$ when $\text{out}_l > \text{in}_l$.
> **Mnemonic Check on a Single Edge $u \xrightarrow{[1, 1]} v$**:
> Imagine $u$ and $v$ have a mandatory pipe $u \to v$ of $[1, 1]$ ($u(e) - l(e) = 0$, so the slack pipe $\tilde{f}(u \to v)$ is closed), plus a free return pipe $v \to u$ of $[0, 1]$.
> - Because 1 mandatory unit arrives at $v$ via $u \to v$, the slack flow $\tilde{f}$ must travel from **$v$ back to $u$** along the free pipe $v \to u$!
> - For slack flow to travel from $v$ to $u$, **$S^*$ must inject flow into $v$** ($S^* \to v$, where $\text{in}_l(v) = 1 > \text{out}_l(v) = 0 \implies M(v) = +1 > 0$) and **$u$ must drain into $T^*$** ($u \to T^*$, where $\text{in}_l(u) = 0 < \text{out}_l(u) = 1 \implies M(u) = -1 < 0$)!

---

### 6.2 Complete Calculus of the Four Lower-Bound Flow Variants (`LOJ #115, #116, #117`)

| Variant | Problem Type | Phase 1: Feasibility Setup on $G'$ | Phase 2: Optimization & Exact Value Recovery |
| :--- | :--- | :--- | :--- |
| **Variant 1: Feasible Circulation** (`无源汇上下界可行流`, `LOJ #115`) | $\text{div}_f(v) = 0 \;\;\forall v \in V$, $l(e) \le f(e) \le u(e)$. | Add $e = (u \to v)$ with cap $u(e) - l(e)$; add $S^* \to v$ ($M(v) > 0$) and $v \to T^*$ ($M(v) < 0$). Run `dinic(S*, T*)`. | Feasible $\iff F_1 = \Sigma^+$. Physical flow on $e_k$ is $f(e_k) = l(e_k) + \tilde{f}(e_k) = l(e_k) + \text{cap}[2k+1]$. |
| **Variant 2: Feasible $s$-$t$ Flow** (`有源汇上下界可行流`) | $\text{div}_f(v) = 0 \;\;\forall v \notin \{s, t\}$, $l(e) \le f(e) \le u(e)$. | Add **Feedback Arc** $e_{\text{fb}} = (t \to s)$ with $[l, u] = [0, \infty)$, reducing to Variant 1! Run `dinic(S*, T*)`. | Feasible $\iff F_1 = \Sigma^+$. The feasible $s$-$t$ flow value is **$f_0 = \tilde{f}(e_{\text{fb}}) = \text{cap}[e_{\text{fb}} \oplus 1]$** (NOT $F_1 = \Sigma^+$!). |
| **Variant 3: Maximum $s$-$t$ Flow** (`有源汇上下界最大流`, `LOJ #116`) | Maximize $|f|$ subject to Variant 2 constraints. | Run Variant 2 Phase 1 (`dinic(S*, T*)` with $t \xrightarrow{[0, \infty)} s$). Check $F_1 == \Sigma^+$. | Record $f_0 = \text{cap}[e_{\text{fb}} \oplus 1]$, **zero out both half-edges of $e_{\text{fb}}$** (`cap[e_fb] = cap[e_fb ^ 1] = 0`), then run $f_{\text{add}} = \text{dinic}(s, t)$ on $G'_{f'}$. Answer: **$|f_{\max}| = f_0 + f_{\text{add}}$**. |
| **Variant 4: Minimum $s$-$t$ Flow** (`有源汇上下界最小流`, `LOJ #117`) | Minimize $|f|$ subject to Variant 2 constraints. | Run Variant 2 Phase 1 (`dinic(S*, T*)` with $t \xrightarrow{[0, \infty)} s$). Check $F_1 == \Sigma^+$. | Record $f_0 = \text{cap}[e_{\text{fb}} \oplus 1]$, **zero out both half-edges of $e_{\text{fb}}$** (`cap[e_fb] = cap[e_fb ^ 1] = 0`), then push flow **backward from $t$ to $s$**: $f_{\text{sub}} = \text{dinic}(t, s)$ on $G'_{f'}$. Answer: **$|f_{\min}| = f_0 - f_{\text{sub}}$**. |

#### Proving the Two Subtle Phase-2 Invariants (Deletion vs. Non-Deletion Equivalence)
1. **Why MUST we zero out BOTH `cap[e_fb] = 0` and `cap[e_fb ^ 1] = 0` before Phase 2?**
   The feedback arc $e_{\text{fb}} = (t \to s)$ has forward direction $t \to s$ (capacity $\infty - f_0 = \infty$) and reverse residual direction $s \to t$ (capacity $f_0$).
   - In Variant 3 (`dinic(s, t)`), if we forget to set `cap[e_fb ^ 1] = 0`, then `dinic(s, t)` will push $f_0$ units along the reverse arc $s \to t$ of $e_{\text{fb}}$, **cancelling the feedback flow and double-counting $f_0$** (unless we omit $f_0 +$ from the sum)! Zeroing both half-edges cleanly locks $f_0$ in place so $|f_{\max}| = f_0 + \text{dinic}(s, t)$ and $|f_{\min}| = f_0 - \text{dinic}(t, s)$ hold uniformly.
2. **Why do we NOT need to delete the companion arcs incident to $S^*$ and $T^*$ before Phase 2?**
   Once Phase 1 achieves $\text{MaxFlow}(S^*, T^*) = \Sigma^+$, **every** arc leaving $S^*$ has residual capacity $0$ (and no physical edge enters $S^*$, so no residual arc can ever enter $S^*$), and **every** arc entering $T^*$ has residual capacity $0$ (and no residual arc can ever leave $T^*$). Thus in $G'_{f'}$, $S^*$ has in-degree $0$ and out-degree $0$, and $T^*$ has out-degree $0$! No augmenting path between $s$ and $t$ can ever pass through $S^*$ or $T^*$, so every Phase-2 augmentation strictly preserves $\text{div}_f(v) = 0$ at all interior vertices!

---

### 6.3 Hoffman's Circulation Theorem (1960)

When does a network $G = (V, E)$ with lower bounds $l: E \to \mathbb{R}_{\ge 0}$ and upper bounds $u: E \to \mathbb{R}_{\ge 0}$ ($l \le u$) admit a feasible circulation ($\text{div}_f(v) = 0 \;\;\forall v \in V$)?

#### Theorem 6.1 (Hoffman's Circulation Theorem, 1960)
A feasible circulation $f$ satisfying $l(e) \le f(e) \le u(e)$ exists if and only if for **every** vertex subset $A \subseteq V$, the total lower-bound demand entering $A$ does not exceed the total upper-bound capacity leaving $A$:
$$\sum_{e \in \delta^-(A)} l(e) \le \sum_{e \in \delta^+(A)} u(e) \qquad \forall A \subseteq V$$

*Proof via Max-Flow Min-Cut on the Auxiliary Network $G'$*:
By Section 6.1, a feasible circulation exists if and only if the maximum $S^*$-$T^*$ flow in $G'$ equals $\Sigma^+$, which by the Max-Flow Min-Cut Theorem holds if and only if every $S^*$-$T^*$ cut $(S^* \sqcup A, T^* \sqcup B)$ in $G'$ (where $V = A \sqcup B$) has cut capacity $\kappa_{G'}(S^* \sqcup A) \ge \Sigma^+$.
Let us expand $\kappa_{G'}(S^* \sqcup A)$:
$$\kappa_{G'}(S^* \sqcup A) = \sum_{v \in B : M(v) > 0} M(v) + \sum_{v \in A : M(v) < 0} (-M(v)) + \sum_{e \in \delta^+(A)} \big(u(e) - l(e)\big)$$
Then $\kappa_{G'}(S^* \sqcup A) \ge \Sigma^+ = \sum_{v \in A : M(v) > 0} M(v) + \sum_{v \in B : M(v) > 0} M(v)$ simplifies by cancelling $\sum_{v \in B : M(v) > 0} M(v)$ from both sides to:
$$\sum_{e \in \delta^+(A)} \big(u(e) - l(e)\big) \ge \sum_{v \in A : M(v) > 0} M(v) - \sum_{v \in A : M(v) < 0} (-M(v)) = \sum_{v \in A} M(v)$$
Now expand $\sum_{v \in A} M(v) = \sum_{v \in A} \big(\text{in}_l(v) - \text{out}_l(v)\big)$. Internal edges with both endpoints in $A$ cancel out, leaving only boundary edges crossing $(A, B)$:
$$\sum_{v \in A} M(v) = \sum_{e \in \delta^-(A)} l(e) - \sum_{e \in \delta^+(A)} l(e)$$
Substituting this into the inequality above and cancelling $-\sum_{e \in \delta^+(A)} l(e)$ from both sides yields the exact Hoffman condition:
$$\sum_{e \in \delta^+(A)} u(e) \ge \sum_{e \in \delta^-(A)} l(e) \qquad \forall A \subseteq V \qquad \blacksquare$$

---

### 6.4 Three Canonical Non-Graph Compilations to Lower-Bound Flows

1. **Contingency-Table / Matrix Rounding & Baranyai's Rounding Lemma (`[POJ 2396]`, `[BZOJ 3698]`)**:
   Given a real matrix $A \in \mathbb{R}_{\ge 0}^{R \times C}$ with row sums $r_i = \sum_j A_{i,j}$ and column sums $c_j = \sum_i A_{i,j}$, can we round every entry $X_{i,j} \in \{\lfloor A_{i,j} \rfloor, \lceil A_{i,j} \rceil\}$, every row sum $R_i \in \{\lfloor r_i \rfloor, \lceil r_i \rceil\}$, and every column sum $C_j \in \{\lfloor c_j \rfloor, \lceil c_j \rceil\}$ while preserving $R_i = \sum_j X_{i,j}$ and $C_j = \sum_i X_{i,j}$?
   - **Compilation**: Create source $S$, sink $T$, row nodes $R_1, \dots, R_n$, and column nodes $C_1, \dots, C_m$. Add $S \to R_i$ with $[\lfloor r_i \rfloor, \lceil r_i \rceil]$, $R_i \to C_j$ with $[\lfloor A_{i,j} \rfloor, \lceil A_{i,j} \rceil]$, and $C_j \to T$ with $[\lfloor c_j \rfloor, \lceil c_j \rceil]$.
   - **Baranyai's Existence Guarantee**: Because the original real numbers $A_{i,j}, r_i, c_j$ already form a **valid real-valued flow** satisfying all integer box bounds $[\lfloor \cdot \rfloor, \lceil \cdot \rceil]$, the feasible polytope is non-empty; by the **Integrality Theorem**, an integral circulation (valid rounding) is **guaranteed to exist**!
2. **Mixed-Graph Eulerian Circuit (`[POJ 1637] Sightseeing Tour`)**:
   Given a connected graph with directed edges $E_D$ and undirected edges $E_U$, orient each $e \in E_U$ so that $\text{in}(v) = \text{out}(v)$ for every $v \in V$.
   - **Algebraic Compilation**: Assign each $e \in E_U$ an arbitrary initial orientation $(u \to v)$, and let $x_e \in \{0, 1\}$ indicate whether we reverse $e$ to $(v \to u)$. Reversing $e = (u \to v)$ decreases $\text{out}(u) - \text{in}(u)$ by $2$ and increases $\text{out}(v) - \text{in}(v)$ by $2$. Thus $\text{out}(v) = \text{in}(v)$ requires:
     $$\sum_{e \in \delta^+_U(v)} x_e - \sum_{e \in \delta^-_U(v)} x_e = \frac{\text{out}_0(v) - \text{in}_0(v)}{2} \triangleq D(v)$$
     If $\text{out}_0(v) \not\equiv \text{in}_0(v) \pmod 2$ for any $v$, return `impossible` immediately; otherwise compile $D(v) > 0$ to $S \to v$ (cap $D(v)$), $D(v) < 0$ to $v \to T$ (cap $-D(v)$), and each $e \in E_U$ to $u \to v$ (cap $1$).
3. **Minimum-Fleet Edge/Vertex Cover on a DAG (`[Luogu P4843] 清理雪道`)**:
   To cover every required edge $e \in E_{\text{req}}$ (or vertex $v$) of a graph at least once using the minimum number of $S$-$T$ routes:
   - Each required edge gets lower bound $l(e) = 1$ and upper bound $u(e) = \infty$ (optional edges get $[0, \infty)$).
   - Connect $S \to v$ and $v \to T$ with $[0, \infty)$ for valid start/end nodes, and solve **Variant 4 (`有源汇上下界最小流`)**.

---

## 7. Cohort 3 Targeted Gap-Hunting & Reconciled Master Decision Table

### 7.1 Symmetric Undirected Cut Posimodularity (Uncrossing) vs. Directed Residual Reachability

Why can all-pairs minimum cuts in an **undirected** network be represented by a single tree of $N - 1$ edges (the **Gomory–Hu Tree**, explored in Wave 2B), whereas **directed** minimum cuts require a full DAG of SCCs (Picard–Queyranne) and cannot be uncrossed into a cut tree?

#### Theorem 7.1 (Posimodularity of Symmetric Undirected Cuts vs. Failure on Directed Graphs)
Let $G = (V, E, c)$ be a network with cut function $\kappa(A) = c(A, V \setminus A)$.
1. **Submodularity (Holds for ALL Directed and Undirected Graphs)**:
   $$\kappa(A) + \kappa(B) = \kappa(A \cup B) + \kappa(A \cap B) + c(A \setminus B, B \setminus A) + c(B \setminus A, A \setminus B) \ge \kappa(A \cup B) + \kappa(A \cap B)$$
2. **Posimodularity / Complementary Submodularity (Holds for Undirected Graphs ONLY)**:
   In an **undirected** graph, $c(X, Y) = c(Y, X)$ for all disjoint $X, Y \subseteq V$, so $\kappa(X) = \kappa(V \setminus X)$. Applying submodularity to $A$ and $V \setminus B$ yields:
   $$\kappa(A) + \kappa(B) = \kappa(A) + \kappa(V \setminus B) \ge \kappa(A \setminus B) + \kappa(B \setminus A) + 2\,c(A \cap B, V \setminus (A \cup B)) \ge \kappa(A \setminus B) + \kappa(B \setminus A)$$
   - **Consequence for Undirected Uncrossing**: If $B$ is a minimum $s$-$t$ cut in an undirected graph and another terminal pair $(u, v)$ is split by $B$ ($u \in B, v \notin B$), and $A$ is a minimum $u$-$v$ cut that crosses $B$, then **both** $(A \cap B, A \cup B)$ **and** $(A \setminus B, B \setminus A)$ are available to uncross $A$ depending on which quadrant of $V \setminus B$ contains $t$!
   - **Why Posimodularity Fails on Directed Graphs**: Consider $V = \{a, b, c\}$ with a single directed edge $(a \to b)$ of capacity $1$, and set $A = \{a, c\}$, $B = \{b, c\}$. Then $\kappa(A) = c(\{a, c\}, \{b\}) = 1$ and $\kappa(B) = c(\{b, c\}, \{a\}) = 0$, so $\kappa(A) + \kappa(B) = 1$. Yet $A \setminus B = \{a\}$ has $\kappa(A \setminus B) = c(\{a\}, \{b, c\}) = 1$ and $B \setminus A = \{b\}$ has $\kappa(B \setminus A) = 0$ — or if we add $(c \to a)$ of capacity $1$, $\kappa(A) = 1, \kappa(B) = 1$, while $\kappa(A \setminus B) = 1$ and $\kappa(B \setminus A) = 0$, and reversing $(c \to a)$ to $(a \to c)$ gives $\kappa(A) = 1, \kappa(B) = 0$ while $\kappa(A \setminus B) = 2 > \kappa(A) + \kappa(B) = 1$! Because $\kappa(B) \neq \kappa(V \setminus B)$ in directed graphs, minimum cuts for different $(s, t)$ pairs cannot be uncrossed via $A \setminus B$.

---

### 7.2 Circulation Infeasibility Diagnostics: Extracting Hoffman Violation Certificates from $S_{\min}^*$

When a Lower-Bound Circulation problem (`Variant 1` or `Variant 2`) fails Phase 1 ($\text{MaxFlow}_{G'}(S^*, T^*) < \Sigma^+$), how do we extract a **concrete witness subset $A \subseteq V$** proving infeasibility (or compute the **minimum total lower-bound reduction** needed to make the system feasible)?

#### Theorem 7.2 (Constructive Hoffman Violation Certificate & Minimum Demand Relaxation)
Suppose $\text{MaxFlow}_{G'}(S^*, T^*) = F_1 < \Sigma^+$ in the auxiliary network $G'$, and let $S_{\min}^* = \{w \in V \cup \{S^*, T^*\} : S^* \leadsto w \text{ in } G'_{f^*}\}$ be the reachable set from $S^*$ in the final residual network $G'_{f^*}$. Define the witness vertex subset:
$$A^* \triangleq S_{\min}^* \cap V = S_{\min}^* \setminus \{S^*\}$$
Then:
1. **Exact Violation Magnitude**: The subset $A^* \subseteq V$ violates Hoffman's condition by **strictly $\Sigma^+ - F_1 > 0$**:
   $$\text{Violation}(A^*) \triangleq \sum_{e \in \delta^-(A^*)} l(e) - \sum_{e \in \delta^+(A^*)} u(e) = \Sigma^+ - F_1 > 0$$
2. **Maximum-Violation Optimality**: Among all $2^{|V|}$ subsets $A \subseteq V$, $A^*$ **maximizes** the Hoffman violation $\sum_{e \in \delta^-(A)} l(e) - \sum_{e \in \delta^+(A)} u(e)$.
3. **Minimum Total Lower-Bound Relaxation**: If we are allowed to reduce the lower bounds $l(e) \gets l(e) - \delta(e)$ ($0 \le \delta(e) \le l(e)$) at unit cost per unit reduction, the **minimum total reduction** $\sum_{e \in E} \delta(e)$ required to make the circulation feasible is obtained by adding a free bypass edge $(u \to v, \text{cap} = l(e), \text{cost} = 1)$ alongside every edge (or in unweighted form, equals $\max_{A \subseteq V} \text{Violation}(A) = \Sigma^+ - F_1$ when single-edge reductions on $\delta^-(A^*)$ suffice).

*Proof*: By the algebraic identity proven in Section 6.3, for any cut $(S^* \sqcup A, T^* \sqcup (V \setminus A))$ in $G'$:
$$\Sigma^+ - \kappa_{G'}(S^* \sqcup A) = \sum_{e \in \delta^-(A)} l(e) - \sum_{e \in \delta^+(A)} u(e)$$
Since $(S^* \sqcup A^*, T^* \sqcup (V \setminus A^*))$ is a minimum $S^*$-$T^*$ cut in $G'$ of capacity $\kappa_{G'}(S^* \sqcup A^*) = F_1$, its Hoffman violation is $\Sigma^+ - F_1 > 0$, and no subset $A \subseteq V$ can have a strictly larger violation since $\kappa_{G'}(S^* \sqcup A) \ge F_1$ for all $A \subseteq V$. $\blacksquare$

---

### 7.3 Reconciled Master Recognition & Compilation Decision Table

| Surface Problem Signal (What the English Statement Says) | Underlying Algebraic Formulation | Target Graph Gadget & Solver Variant | Time Complexity (Dinic) |
| :--- | :--- | :--- | :--- |
| **"Disjoint routes / minimum edges to block $s \leadsto t$"** | $\max |f|$ s.t. $f(e) \in \{0, 1\}$, $\text{div}_f(v) = 0$ + Path Decomposition | Unit capacities $c(e) = 1$ (or compact undirected pairs) + pointer-advancing DAG walk | $O(E \min(E^{1/2}, V^{2/3}))$ |
| **"Destroy/capacitate vertices (tolls, pillars, intersections)"** | $0 \le \sum_{e \in \delta^-(v)} f(e) \le C_v$ | **Vertex Splitting**: $v_{\text{in}} \xrightarrow{C_v} v_{\text{out}}$; wire all external edges $u_{\text{out}} \to v_{\text{in}}$ | $O(E\sqrt{V})$ (if $C_v = 1$) |
| **"Can edge $e$ belong to ANY / EVERY min-cut?"** | $\exists S \in \mathcal{L}_{\min}, e \in \delta^+(S)$ vs. $\forall S \in \mathcal{L}_{\min}, e \in \delta^+(S)$ | **Picard–Queyranne / Tarjan SCC on $G_{f^*}$**: Feasible $\iff f^*(e)=c(e) \land \text{scc}[u] \neq \text{scc}[v]$; Essential $\iff \text{scc}[u]=\text{scc}[s] \land \text{scc}[v]=\text{scc}[t]$ | $O(\text{Dinic} + V + E)$ |
| **"Is the minimum $s$-$t$ cut unique?"** | $|\mathcal{L}_{\min}| = 1 \iff S_{\min} = S_{\max}$ | Forward BFS from $s$ ($S_{\min}$) + Reverse BFS from $t$ ($T_{\min}$) in $G_{f^*}$: check $S_{\min} \cup T_{\min} = V$ | $O(\text{Dinic} + V + E)$ |
| **"Lexicographically smallest minimum cut (`[SDOI2014] LIS`)"** | Greedy inclusion test + permanent edge deletion | Test $u_{\text{in}} \not\to^* u_{\text{out}}$ in $G_{f^*}$, then **Dynamic Rollback (`退流`)**: `dinic(t, v, k)` + `dinic(u, s, k)` | $O(\text{Dinic} + |f^*| \cdot E)$ |
| **"Agents move across time steps / periodic shuttles"** | State $(u, t) \in V \times \{0, \dots, T\}$ | **Time-Expanded Layered DAG** with **Incremental Layer Addition (`动态加层`)** | $O(T^* \cdot E_{\text{layer}})$ |
| **"Jump between any two cells in same row or column"** | Clique transitions within rows/columns | **Row/Column Hub Sparsification**: $R_r \leftrightarrow C_c$ bipartite unit graph | $O(HW\sqrt{H + W})$ |
| **"Preemptive parallel-machine scheduling $[r_j, d_j]$"** | $0 \le x_{j,k} \le \Delta_k$, $\sum_j x_{j,k} \le M \Delta_k$ | **Elementary Interval Bipartite Flow** + **McNaughton's Wrap-Around Rule** | $O(N^2 \sqrt{N})$ |
| **"Every pipe / variable / cell has $[l, u]$ bounds"** | $f = l + \tilde{f}$, $M(v) = \text{in}_l(v) - \text{out}_l(v)$ | **Variants 1–4 (`上下界网络流`)**: $S^* \to v$ ($M > 0$), $v \to T^*$ ($M < 0$), $t \xrightarrow{[0, \infty)} s$ | $O(\text{Dinic}(G'))$ |
| **"Two commodities on undirected graph (`[CQOI2014] 危桥`)"** | $|f_1(e)| + |f_2(e)| \le c(e)$ | **Okamura–Seymour Swap**: test $\text{MaxFlow}(a_1+b_1 \to a_2+b_2)$ AND $\text{MaxFlow}(a_1+b_2 \to a_2+b_1)$ | $2 \times O(\text{Dinic})$ |
| **"$K \le 10$ edges change capacity across $Q = 2\cdot 10^5$ queries"** | $\min_{\text{mask} \in \{0,1\}^K} (\text{cut}[\text{mask}] + \sum_{i \in \text{mask}} w_i)$ | **$2^K$ Cut-Mask Precomputation** via persistent residual DFS tree + $O(2^K)$ DP per query | $O(\text{Dinic} + 2^K E + Q 2^K)$ |

---

## 8. Reconciled Master 4-Tier Curated Problem Bank (30 Non-Template Problems)

Every problem below reconciles the strongest insights from Cohort 1 and Cohort 2 under the strict **4-Step English-to-Graph Compilation Pipeline** and **3-Tier Progressive Hints**.

### Tier 1: Stepping Stone (`P01`–`P07`)

---

### P01 — `[Codeforces 546E]` Soldier and Traveling (`[EN]`)
- **Judge URL**: [https://codeforces.com/problemset/problem/546/E](https://codeforces.com/problemset/problem/546/E)
- **Constraints**: $N \le 100$ cities, $M \le 200$ undirected roads, initial soldiers $a_i \in [0, 100]$, target soldiers $b_i \in [0, 100]$. Time Limit: $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Each soldier can move across **at most 1 road** (or stay put) to transform initial distribution $\mathbf{a}$ into target distribution $\mathbf{b}$, and we must output the explicit $N \times N$ movement matrix $X_{i,j} \in \mathbb{Z}_{\ge 0}$. If we simply add undirected edges of capacity $\infty$ on the original $N$-vertex graph, flow will cascade across multiple hops $u \to v \to w$, violating the 1-step movement limit!
- **Step 2 — Intermediate Algebraic Representation**:
  Let $x_{i, j} \in \mathbb{Z}_{\ge 0}$ be the number of soldiers moving from city $i$ (at $t=0$) to city $j$ (at $t=1$), defined only for $j = i$ or $\{i, j\} \in E$. Then:
  $$\sum_{j : j=i \lor \{i,j\} \in E} x_{i, j} = a_i \quad \forall i \in \{1, \dots, N\}, \qquad \sum_{i : i=j \lor \{i,j\} \in E} x_{i, j} = b_j \quad \forall j \in \{1, \dots, N\}$$
  with trivial necessary invariant $\sum_{i=1}^N a_i = \sum_{j=1}^N b_j$.
- **Step 3 — Reverse-Engineering Scratchpad & Broken-Gadget Counterexample**:
  Because row sums $\sum_j x_{i,j} = a_i$ and column sums $\sum_i x_{i,j} = b_j$ live at two distinct time instants $t = 0$ and $t = 1$, split each city $i$ into a **departure node** $L_i$ ($t = 0$) and an **arrival node** $R_i$ ($t = 1$):
  - Source $S \to L_i$ with capacity $a_i$.
  - Sink $R_j \to T$ with capacity $b_j$.
  - Stay-put arc $L_i \to R_i$ with capacity $\infty$.
  - For each undirected road $\{u, v\} \in E$, add **two directed cross-arcs** $L_u \to R_v$ and $L_v \to R_u$, each with capacity $\infty$.
  - **Broken Gadget Check**: If you leave the graph unsplit ($S \to i \to T$ with undirected edges $u \leftrightarrow v$), then on $1 - 2 - 3$ with $\mathbf{a} = (1, 0, 0)$ and $\mathbf{b} = (0, 0, 1)$, flow routes $S \to 1 \to 2 \to 3 \to T$ (2 hops!), outputting `YES` on an impossible test case.
- **Step 4 — Complete Solution & Complexity**:
  First check $\sum a_i == \sum b_i$ (if not, print `NO`). Run Dinic on the $2N + 2$ vertex bipartite network. If $\text{MaxFlow}(S, T) == \sum a_i$, print `YES` and recover $X_{i, j} = f(L_i \to R_j) = \text{cap}[e_{L_i \to R_j} \oplus 1]$ for all $(i, j)$. Complexity: $O(M \sqrt{N})$ operations ($\le 10^4$ ops).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Why does routing flow directly on the $N$-vertex road network allow soldiers to travel distance $\ge 2$?
  - *Hint 2*: Separate the state "City $i$ before moving ($t=0$)" from "City $j$ after moving ($t=1$)".
  - *Hint 3*: Don't forget to check $\sum_{i=1}^N a_i == \sum_{i=1}^N b_i$ before comparing $\text{MaxFlow}(S, T)$ against $\sum a_i$, and recover $X_{i,j}$ from the reverse residual capacities of $L_i \to R_j$.

---

### P02 — `[CSES 1711]` Distinct Routes (`[EN]`)
- **Judge URL**: [https://cses.fi/problemset/task/1711](https://cses.fi/problemset/task/1711)
- **Constraints**: $N \le 500$ rooms, $M \le 1000$ directed teleporters from room $1$ to room $N$. Time Limit: $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Find the maximum number of **edge-disjoint** directed paths from $1$ to $N$ and print each path explicitly. As proven in the 6-vertex Diamond-Bridge counterexample (Section 5.3), greedy BFS path removal fails when an early path blocks two disjoint paths; residual path-splicing is mandatory.
- **Step 2 — Intermediate Algebraic Representation**:
  Assign indicator flow $f(e) \in \{0, 1\}$ to each directed edge $e \in E$ subject to $\text{div}_f(v) = 0$ for $v \notin \{1, N\}$, maximizing $|f| = \text{div}_f(1)$. By Theorem 2.7 (Flow Decomposition), any integral flow $f \in \{0, 1\}^{|E|}$ decomposes into $|f^*|$ edge-disjoint $1 \to N$ paths (plus optional cycles).
- **Step 3 — Reverse-Engineering Scratchpad & Broken-Gadget Counterexample**:
  1. Build the directed graph with $c(e) = 1$ for every input edge $e_k$ (allocated at half-edges `2k` and `2k+1`).
  2. Run Dinic from $1$ to $N$ to obtain $K = |f^*|$.
  3. **Path Extraction**: In the physical support subgraph $G_{\text{supp}}(f^*) = \{e_k \in E : f^*(e_k) = \text{cap}[2k+1] == 1\}$, extract $K$ simple paths from $1$ to $N$ by walking forward edges with $\text{cap}[2k+1] == 1$ and setting $\text{cap}[2k+1] \gets 0$ as each edge is consumed.
  - **Broken Extraction Check**: Never trace paths along *residual* arcs during reconstruction, or you will walk backward along reverse arcs $v \to u$! Only traverse **even-indexed forward edges** $2k$ whose reverse half-edge $2k+1$ has $\text{cap}[2k+1] == 1$.
- **Step 4 — Complete Solution & Complexity**:
  By Unit-Capacity Regime 1/2 (Theorem 3.5), Dinic runs in $O(M \min(M^{1/2}, N^{2/3}))$ time, and pointer-advancing extraction takes $O(M + \sum |P_i|) = O(NM)$ time.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Every teleporter can be used at most once — what capacity does that correspond to?
  - *Hint 2*: After Dinic finishes, which edges in your adjacency list actually carry $1$ unit of physical flow?
  - *Hint 3*: Run $K = |f^*|$ greedy DFS walks from node $1$ to node $N$ using only forward edges with $f^*(e) = 1$, zeroing out each edge's flow immediately so the next walk uses disjoint edges.

---

### P03 — `[USACO 5.4 / Luogu P1345]` Telecowmunication (`[EN]`/`[ZH]`)
- **Judge URL**: [https://www.luogu.com.cn/problem/P1345](https://www.luogu.com.cn/problem/P1345)
- **Constraints**: $N \le 100$ cows (routers), $M \le 600$ undirected cables, terminals $c_1, c_2$. Find the minimum number of cows to remove to disconnect $c_1$ and $c_2$, and output the **lexicographically smallest** vertex cut set.
- **Step 1 — Non-Graph Diagnostic Signal**:
  We are disconnecting an undirected graph by removing **vertices** (not edges) and must break ties in favor of the **lexicographically smallest vertex subset** $(v_{i_1}, v_{i_2}, \dots, v_{i_k})$.
- **Step 2 — Intermediate Algebraic Representation**:
  By Menger's Undirected Vertex-Cut Theorem (Section 5.3), each interior vertex $v \in V \setminus \{c_1, c_2\}$ has throughput $F(v) \in \{0, 1\}$, and each undirected cable $\{u, v\}$ has infinite capacity in both directions.
- **Step 3 — Reverse-Engineering Scratchpad & Broken-Gadget Counterexample**:
  - Split every vertex $v \in \{1, \dots, N\}$ into $v_{\text{in}} \to v_{\text{out}}$ with capacity $1$ (or $\infty$ for $c_1, c_2$).
  - For each undirected cable $\{u, v\}$, add directed arcs $u_{\text{out}} \xrightarrow{\infty} v_{\text{in}}$ and $v_{\text{out}} \xrightarrow{\infty} u_{\text{in}}$.
  - **Why does $S_{\min}$ NOT necessarily give the lexicographically smallest vertex cut?** $S_{\min}$ gives the *nearest* cut to $c_1$ in the DAG topology, NOT the smallest integer indices!
  - **Lexicographical Enumeration**: First compute $F^* = \text{MaxFlow}((c_1)_{\text{out}}, (c_2)_{\text{in}})$. Then iterate $i = 1, 2, \dots, N$ ($i \neq c_1, c_2$): temporarily set $c(i_{\text{in}} \to i_{\text{out}}) = 0$ and re-compute Max-Flow $F_{\text{new}}$. If $F_{\text{new}} == F^* - 1$, then $i$ belongs to at least one minimum vertex cut! Permanently keep $c(i_{\text{in}} \to i_{\text{out}}) = 0$, append $i$ to the answer, and decrement $F^* \gets F^* - 1$; otherwise restore $c(i_{\text{in}} \to i_{\text{out}}) = 1$.
- **Step 4 — Complete Solution & Complexity**:
  With $N \le 100$, re-running Dinic $N$ times takes $N \times O(M\sqrt{N}) \approx 100 \times 6000 = 6 \times 10^5$ operations ($\le 5\text{ ms}$). (For $N \le 700$, we upgrade this to `退流` in `P24 [SDOI2014] LIS`!)
- **3-Tier Progressive Hints**:
  - *Hint 1*: Split each cow $v$ into $v_{\text{in}} \xrightarrow{1} v_{\text{out}}$ and route cables from $\text{out}$-ports to $\text{in}$-ports.
  - *Hint 2*: How do you test whether cow $i$ can be the first element of a minimum vertex cut?
  - *Hint 3*: If deleting $i$'s internal bridge drops the Max-Flow by $1$, commit the deletion and continue scanning $i+1 \dots N$ until the remaining Max-Flow hits $0$.

---

### P04 — `[ZOJ 2314 / ASC 1]` Reactor Cooling (`[EN]`/`[ZH]`)
- **Judge URL**: [https://pintia.cn/problem-sets/91827364500/exam/problems/91827365845](https://pintia.cn/problem-sets/91827364500/exam/problems/91827365845) (also `LOJ #115`)
- **Constraints**: $N \le 200$ nodes, $M \le 19900$ directed pipes, each with lower bound $l_e$ and upper bound $u_e$ ($0 \le l_e \le u_e \le 10^5$). Time Limit: $1.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Every pipe has a mandatory minimum cooling flow $l_e$ and maximum capacity $u_e$, and every node must strictly conserve coolant ($\text{in}(v) = \text{out}(v)$ for all $v$). This is the archetype of **Variant 1 (`无源汇上下界可行流`)**.
- **Step 2 — Intermediate Algebraic Representation**:
  Substitute $f(e) = l_e + \tilde{f}(e)$ ($0 \le \tilde{f}(e) \le u_e - l_e$). Then $\text{div}_{\tilde{f}}(v) = M(v) = \sum_{e \in \delta^-(v)} l_e - \sum_{e \in \delta^+(v)} l_e$.
- **Step 3 — Reverse-Engineering Scratchpad**:
  Construct $G'$ with super-source $S^*$ and super-sink $T^*$:
  - Each pipe $e_k = (u \to v)$ gets capacity $u_k - l_k$ at half-edges `2k` and `2k+1`.
  - Accumulate $M(v) \text{ += } l_k$ and $M(u) \text{ -= } l_k$.
  - For each $v \in \{1, \dots, N\}$: if $M(v) > 0$, add $S^* \to v$ with capacity $M(v)$ and add $M(v)$ to $\Sigma^+$; if $M(v) < 0$, add $v \to T^*$ with capacity $-M(v)$.
- **Step 4 — Complete Solution & Complexity**:
  Run `dinic(S*, T*)`. If the max-flow equals $\Sigma^+$, print `YES` and for each pipe $k$ output $l_k + \text{cap}[2k+1]$; otherwise print `NO`. Complexity: $O(N^2 M)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Pre-inject $l_e$ units of flow into every pipe $e = (u \to v)$ and compute the resulting excess $M(v) = \text{in}_l(v) - \text{out}_l(v)$ at each node.
  - *Hint 2*: Which nodes need to receive extra slack flow from $S^*$, and which nodes need to drain into $T^*$?
  - *Hint 3*: A valid circulation exists iff $\text{MaxFlow}(S^*, T^*) = \sum_{M(v) > 0} M(v)$, and pipe $k$'s final flow is $l_k + \tilde{f}(e_k)$.

---

### P05 — `[Luogu P2763]` 试题库问题 (`[ZH]`, 网络流 24 题)
- **Judge URL**: [https://www.luogu.com.cn/problem/P2763](https://www.luogu.com.cn/problem/P2763)
- **Constraints**: $K \le 20$ problem categories, $N \le 1000$ candidate problems, total required problems $M = \sum_{c=1}^K q_c \le 1000$. Each problem belongs to a subset of categories, and each selected problem can fulfill **at most 1** category.
- **Step 1 — Non-Graph Diagnostic Signal**:
  One-to-many quota assignment: category $c$ requires $q_c$ problems, while problem $i$ can be used at most once across its eligible categories.
- **Step 2 — Intermediate Algebraic Representation**:
  Let $x_{c, i} \in \{0, 1\}$ indicate whether problem $i$ is assigned to category $c \in S_i$. Then $\sum_{i : c \in S_i} x_{c, i} = q_c$ for each category $c \in \{1, \dots, K\}$, and $\sum_{c \in S_i} x_{c, i} \le 1$ for each problem $i \in \{1, \dots, N\}$.
- **Step 3 — Reverse-Engineering Scratchpad**:
  - Source $S \to \text{Cat}_c$ with capacity $q_c$ ($c = 1 \dots K$).
  - Cross edge $\text{Cat}_c \to \text{Prob}_i$ with capacity $1$ if $c \in S_i$.
  - Sink edge $\text{Prob}_i \to T$ with capacity $1$ ($i = 1 \dots N$).
- **Step 4 — Complete Solution & Complexity**:
  Run Dinic from $S$ to $T$. If $\text{MaxFlow}(S, T) < \sum_{c=1}^K q_c$, output `No Solution!`; otherwise for each category $c$, scan outgoing edges $\text{Cat}_c \to \text{Prob}_i$ and output all $i$ with reverse capacity $\text{cap}[e \oplus 1] == 1$. By **Asymmetric Bipartite Regime 4** (Theorem 3.5), since all right-hand nodes $\text{Prob}_i$ have unit capacity $1$, Dinic runs in **$O(E \sqrt{N})$** time!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Model categories on the left with supply $q_c$ and problems on the right with sink capacity $1$.
  - *Hint 2*: Why does each problem node have capacity $1$ to $T$ even if it belongs to multiple categories?
  - *Hint 3*: Inspect the reverse residual edges of $\text{Cat}_c \to \text{Prob}_i$ to list the problems assigned to category $c$.

---

### P06 — `[Luogu P2766]` 最长不下降子序列问题 (`[ZH]`, 网络流 24 题)
- **Judge URL**: [https://www.luogu.com.cn/problem/P2766](https://www.luogu.com.cn/problem/P2766)
- **Constraints**: Sequence $A_1, \dots, A_N$ ($N \le 500$). (1) Find the length $K$ of the longest non-decreasing subsequence (LNDS). (2) Find the maximum number of disjoint LNDS of length $K$ (each index $i$ used at most once). (3) Find the maximum number of LNDS of length $K$ if $A_1$ and $A_N$ can be used infinitely many times.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Subproblem (1) is classic $O(N^2)$ DP: $dp[i] = 1 + \max_{j < i, A_j \le A_i} dp[j]$, with $K = \max_i dp[i]$. Subproblems (2) and (3) ask for the maximum number of **vertex-disjoint paths of length $K$** in the DP transition DAG, where vertices $1$ and $N$ have capacity $1$ in (2) and capacity $\infty$ in (3).
- **Step 2 — Intermediate Algebraic Representation**:
  An index sequence $i_1 < i_2 < \dots < i_K$ is a valid LNDS of length $K$ iff $dp[i_1] = 1$, $dp[i_K] = K$, and for every step $t \in \{1, \dots, K-1\}$, $i_t < i_{t+1}$, $A_{i_t} \le A_{i_{t+1}}$, and **$dp[i_{t+1}] = dp[i_t] + 1$**.
- **Step 3 — Reverse-Engineering Scratchpad & The $K = 1$ Edge-Case Trap**:
  - Split every index $i \in \{1, \dots, N\}$ into $i_{\text{in}} \xrightarrow{1} i_{\text{out}}$.
  - If $dp[i] == 1$, add $S \xrightarrow{1} i_{\text{in}}$.
  - If $dp[i] == K$, add $i_{\text{out}} \xrightarrow{1} T$.
  - For each pair $i < j$ with $A_i \le A_j$ and $dp[j] == dp[i] + 1$, add $i_{\text{out}} \xrightarrow{1} j_{\text{in}}$.
  - Run Dinic for Subproblem (2).
  - For Subproblem (3), increase $c(1_{\text{in}} \to 1_{\text{out}}) = \infty$, $c(S \to 1_{\text{in}}) = \infty$ (if $dp[1] = 1$), $c(N_{\text{in}} \to N_{\text{out}}) = \infty$, and $c(N_{\text{out}} \to T) = \infty$ (if $dp[N] = K$), and augment on the residual graph!
  - **Broken Gadget Trap ($K = 1$)**: What if the sequence is strictly decreasing so $K = 1$? Then in Subproblem (3), $dp[1] = 1 = K$, so setting $S \xrightarrow{\infty} 1_{\text{in}} \xrightarrow{\infty} 1_{\text{out}} \xrightarrow{\infty} T$ creates an **infinite-capacity path** from $S$ to $T$, even though a single element $A_1$ (or $A_N$) cannot be chosen multiple times as an identical 1-element set, or if $K=1$ the answer to (2) and (3) is $N$! Always handle $K == 1$ explicitly (`ans2 = ans3 = N`).
- **Step 4 — Complete Solution & Complexity**:
  Subproblem (2) is a unit-vertex network solved in $O(E\sqrt{N}) = O(N^{2.5})$ time; Subproblem (3) adds at most $O(N)$ flow in $O(N E)$ time.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Only include DAG edges $(i \to j)$ that satisfy $i < j$, $A_i \le A_j$, AND $dp[j] = dp[i] + 1$.
  - *Hint 2*: Split each index $i$ into $i_{\text{in}} \to i_{\text{out}}$ to limit how many subsequences can use $i$.
  - *Hint 3*: Watch out for $K = 1$ in Subproblem (3): if $dp[1] = K = 1$, giving node $1$ infinite capacity on both $S \to 1_{\text{in}}$ and $1_{\text{out}} \to T$ would push $\infty$ flow!

---

### P07 — `[AtCoder ABC 239 G]` Builder Takahashi (`[JA]`)
- **Judge URL**: [https://atcoder.jp/contests/abc239/tasks/abc239_g](https://atcoder.jp/contests/abc239/tasks/abc239_g)
- **Constraints**: $N \le 100$ vertices, $M$ undirected edges, vertex wall-building costs $c_2, \dots, c_{N-1} \in [1, 10^9]$ ($c_1 = c_N = \infty$). Find the minimum total cost of vertices to block all paths between $1$ and $N$, and output the explicit list of blocked vertices.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Minimum-weight **vertex cut** on an undirected graph, with explicit vertex cut-set reconstruction.
- **Step 2 & 3 — Algebraic & Graph Compilation**:
  - Split each $v \in \{2, \dots, N-1\}$ into $v_{\text{in}} \xrightarrow{c_v} v_{\text{out}}$, and set $1_{\text{in}} \xrightarrow{\infty} 1_{\text{out}}$, $N_{\text{in}} \xrightarrow{\infty} N_{\text{out}}$.
  - For each undirected edge $\{u, v\}$, add $u_{\text{out}} \xrightarrow{\infty} v_{\text{in}}$ and $v_{\text{out}} \xrightarrow{\infty} u_{\text{in}}$.
  - **Cut Set Reconstruction**: After computing Max-Flow from $1_{\text{out}}$ to $N_{\text{in}}$, run a forward BFS from $1_{\text{out}}$ in $G_{f^*}$ to mark the reachable set $S_{\min}$. Since all external edges have capacity $\infty$, no external edge $(u_{\text{out}} \to v_{\text{in}})$ can ever cross $(S_{\min}, V \setminus S_{\min})$. The cut edges of $S_{\min}$ consist **exclusively** of internal vertex bridges $v_{\text{in}} \to v_{\text{out}}$ where:
    $$v_{\text{in}} \in S_{\min} \;\;\land\;\; v_{\text{out}} \notin S_{\min}$$
- **Step 4 — Complete Solution & Complexity**:
  Use `int64_t` (`long long`) for capacities since $\sum c_v \le 10^{11}$. Dinic + BFS runs in $< 5\text{ ms}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Split each vertex $v$ into $v_{\text{in}} \xrightarrow{c_v} v_{\text{out}}$ and give all original undirected edges capacity $\infty$ from $\text{out}$-ports to $\text{in}$-ports.
  - *Hint 2*: Why can an $\infty$-capacity edge never cross a finite minimum cut?
  - *Hint 3*: Run BFS from $1_{\text{out}}$ on positive-capacity residual edges in $G_{f^*}$ and output all $v \in \{2, \dots, N-1\}$ with `vis[v_in] && !vis[v_out]`.

---

### Tier 2: Intermediate (`P08`–`P15`)

---

### P08 — `[POJ 1637 / UVa 10735]` Sightseeing Tour (`[EN]`/`[ZH]`)
- **Judge URL**: [http://poj.org/problem?id=1637](http://poj.org/problem?id=1637) (also UVa 10735, explicit walk reconstruction)
- **Constraints**: $V \le 200$ intersections, $E \le 1000$ streets (some one-way directed, some two-way undirected). Determine whether an Eulerian circuit exists (and reconstruct the tour in UVa 10735).
- **Step 1 — Non-Graph Diagnostic Signal**:
  A connected directed graph has an Eulerian circuit iff $\text{in}(v) = \text{out}(v)$ for every $v \in V$. Here, undirected edges must be oriented to balance in-degrees and out-degrees globally.
- **Step 2 — Intermediate Algebraic Representation**:
  Give each undirected edge $e \in E_U$ an arbitrary initial orientation $(u \to v)$, and compute initial degrees $\text{in}_0(v), \text{out}_0(v)$ over $E_D \cup E_U$. Let $x_e \in \{0, 1\}$ indicate whether we flip $e \in E_U$ from $(u \to v)$ to $(v \to u)$. Flipping $e$ changes $\text{out}(u) - \text{in}(u)$ by $-2$ and $\text{out}(v) - \text{in}(v)$ by $+2$. Hence $\text{out}(v) = \text{in}(v)$ holds iff:
  $$\sum_{e \in \delta^+_U(v)} x_e - \sum_{e \in \delta^-_U(v)} x_e = \frac{\text{out}_0(v) - \text{in}_0(v)}{2} \triangleq D(v) \qquad \forall v \in V$$
- **Step 3 — Reverse-Engineering Scratchpad**:
  1. **Parity Pre-Check**: If $\text{out}_0(v) - \text{in}_0(v)$ is odd for any $v \in V$, return `impossible` immediately!
  2. **Graph Compilation**:
     - For each $e = (u \to v) \in E_U$, add directed arc $u \to v$ with capacity $1$. (Directed edges $E_D$ cannot be flipped, so they are NOT added to the flow network!)
     - For each $v$ with $D(v) > 0$, add $S \to v$ with capacity $D(v)$.
     - For each $v$ with $D(v) < 0$, add $v \to T$ with capacity $-D(v)$.
- **Step 4 — Complete Solution & Complexity**:
  An Eulerian orientation exists iff $\text{MaxFlow}(S, T) == \sum_{D(v) > 0} D(v)$. To reconstruct the tour (UVa 10735), flip every $e \in E_U$ that carries flow $x_e = 1$, and run Hierholzer's $O(V + E)$ algorithm on the resulting directed graph. Total complexity: $O(E \min(E^{1/2}, V^{2/3}))$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Orient every undirected edge arbitrarily first; why does flipping one edge change $\text{out}(v) - \text{in}(v)$ by an even number ($\pm 2$)?
  - *Hint 2*: Express the number of flipped outgoing edges minus flipped incoming edges at $v$ as $D(v) = (\text{out}_0(v) - \text{in}_0(v))/2$.
  - *Hint 3*: Only undirected edges get unit-capacity arcs in the flow graph; directed edges only contribute to the initial imbalance $D(v)$.

---

### P09 — `[AHOI2009 / Luogu P4126]` 最小割 (`[ZH]`)
- **Judge URL**: [https://www.luogu.com.cn/problem/P4126](https://www.luogu.com.cn/problem/P4126)
- **Constraints**: $N \le 4000$ vertices, $M \le 60000$ directed edges. For each edge $e_i = (u_i \to v_i)$, output two booleans: (1) can $e_i$ belong to *some* minimum $s$-$t$ cut? (2) must $e_i$ belong to *every* minimum $s$-$t$ cut?
- **Step 1 — Non-Graph Diagnostic Signal**:
  Direct application of the Picard–Queyranne Residual Condensation DAG and Theorem 4.5 (Section 4.3).
- **Step 2 & 3 — Algebraic & Graph Compilation**:
  1. Run Dinic from $s$ to $t$ to compute $f^*$ and the residual network $G_{f^*}$.
  2. Run Tarjan's SCC algorithm on $G_{f^*}$ (traversing only residual half-edges `e` with `cap[e] > 0`) to compute `scc[v]` for all $v \in V$.
  3. For each original forward half-edge `2k` ($u \to v$):
     - **Feasible (`可行边`)**: `cap[2k] == 0 && scc[u] != scc[v]`.
     - **Essential (`必须边`)**: `cap[2k] == 0 && scc[u] == scc[s] && scc[v] == scc[t]`.
  - **Broken Implementation Check**: What if $c(e) == 0$ in the input, or what if parallel edges exist between $u$ and $v$? Because Tarjan runs on the **residual graph** $G_{f^*}$, if two parallel edges exist between $u$ and $v$ and only one is saturated, the unsaturated one keeps $u \to v \in E_{f^*}$ while the saturated one provides $v \to u \in E_{f^*}$, automatically merging `scc[u] == scc[v]` and correctly reporting `0 0` for both!
- **Step 4 — Complete Solution & Complexity**:
  One Dinic call + $O(N + M)$ Tarjan SCC + $O(M)$ query loop.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Can an unsaturated edge ($\text{cap}[2k] > 0$) ever belong to a minimum cut?
  - *Hint 2*: Contract strongly connected components of positive-capacity edges in $G_{f^*}$ using Tarjan's algorithm.
  - *Hint 3*: Apply Theorem 4.5: feasible iff saturated and $\text{scc}[u] \neq \text{scc}[v]$; essential iff saturated and $\text{scc}[u] = \text{scc}[s] \land \text{scc}[v] = \text{scc}[t]$.

---

### P10 — `[CTSC1999 / Luogu P2754]` 家园 / 星际转移问题 (`[ZH]`, 网络流 24 题)
- **Judge URL**: [https://www.luogu.com.cn/problem/P2754](https://www.luogu.com.cn/problem/P2754)
- **Constraints**: $N \le 13$ space stations (Earth $= 0$, Moon $= N+1$), $M \le 20$ periodic shuttles (shuttle $i$ has capacity $H_i$ and cycles through a fixed list of stations at $1$ step per day), $K \le 50$ astronauts. Find the minimum day $T^*$ when all $K$ astronauts reach the Moon, or output `0` if impossible.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Shuttles move on periodic schedules over discrete days $t = 0, 1, 2, \dots$, and astronauts can wait at any station across days. We need the minimum horizon $T^*$ to route $K$ units of flow.
- **Step 2 & 3 — Time-Expanded Layered DAG & Incremental Layer Addition (`动态加层`)**:
  1. **Impossibility Pre-Check via DSU**: Merge all stations visited by each shuttle in a Disjoint Set Union. If Earth ($0$) and Moon ($N+1$) are in different connected components, output `0` immediately!
  2. **Incremental Layered Graph**:
     - Day $0$: Create $(v, 0)$ for $v \in \{0, \dots, N+1\}$, connect $S \xrightarrow{\infty} (0, 0)$ and $(N+1, 0) \xrightarrow{\infty} \text{Sink}$.
     - Loop $t = 1, 2, 3, \dots$:
       - Create layer $t$ nodes $(v, t)$ for $v \in \{0, \dots, N+1\}$.
       - **Station Waiting**: Add $(v, t-1) \xrightarrow{\infty} (v, t)$ for $v \in \{0, \dots, N\}$.
       - **Shuttle Transit**: For each shuttle $i$ (at station $u$ on day $t-1$ and station $v$ on day $t$), add $(u, t-1) \xrightarrow{H_i} (v, t)$.
       - **Moon Arrival**: Add $(N+1, t) \xrightarrow{\infty} \text{Sink}$.
       - **Incremental Augmentation**: Call `flow += dinic(S, Sink)` on the persistent residual network! As soon as `flow >= K`, return $t$.
- **Step 4 — Complete Solution & Complexity**:
  With $N \le 13, K \le 50$, $T^* \le 600$ (usually $T^* \le 100$), and incremental Dinic runs in $< 5\text{ ms}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Use DSU first to check if the Moon is reachable from Earth at all.
  - *Hint 2*: Represent state as $(\text{station } v, \text{day } t)$: waiting is $(v, t-1) \xrightarrow{\infty} (v, t)$, and shuttle $i$ is $(u, t-1) \xrightarrow{H_i} (v, t)$.
  - *Hint 3*: Don't binary search on $T$! Add one day's layer at a time to the existing residual graph and accumulate `flow += dinic(S, Sink)`.

---

### P11 — `[SCOI2007 / Luogu P2472]` 蜥蜴 (`[ZH]`)
- **Judge URL**: [https://www.luogu.com.cn/problem/P2472](https://www.luogu.com.cn/problem/P2472)
- **Constraints**: $R \times C$ grid ($R, C \le 20$), jump distance $D \le 4$. Pillar at $(r, c)$ has height/durability $h_{r,c} \in \{0, \dots, 3\}$ (collapses after $h_{r,c}$ jumps leaving it). Find the minimum number of lizards trapped.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Each pillar $(r, c)$ can be **departed** at most $h_{r,c}$ times before collapsing — a textbook **Vertex-Durability Splitting** constraint.
- **Step 2 & 3 — Algebraic & Graph Compilation**:
  - Split each pillar $(r, c)$ with $h_{r,c} > 0$ into $(r, c)_{\text{in}} \xrightarrow{h_{r,c}} (r, c)_{\text{out}}$.
  - If $(r, c)$ initially holds a lizard, add $S \xrightarrow{1} (r, c)_{\text{in}}$.
  - If $(r, c)$ can jump outside the grid ($\min(r, R - 1 - r, c, C - 1 - c) + 1 \le D$ in $1$-indexed coordinates), add $(r, c)_{\text{out}} \xrightarrow{\infty} T$.
  - For every pair of pillars with $(r_1 - r_2)^2 + (c_1 - c_2)^2 \le D^2$, add $(r_1, c_1)_{\text{out}} \xrightarrow{\infty} (r_2, c_2)_{\text{in}}$.
- **Step 4 — Complete Solution & Complexity**:
  Answer is $L_{\text{total}} - \text{MaxFlow}(S, T)$. With $\le 800$ vertices and $C_v \le 3$, Dinic finishes in $< 3\text{ ms}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: A pillar's height $h_{r,c}$ limits how many lizards can pass through it — split $(r, c)$ into $\text{in}$ and $\text{out}$ nodes.
  - *Hint 2*: Connect $(r, c)_{\text{out}} \xrightarrow{\infty} T$ whenever $(r, c)$ is within distance $D$ of the grid boundary.
  - *Hint 3*: Connect $(r_1, c_1)_{\text{out}} \xrightarrow{\infty} (r_2, c_2)_{\text{in}}$ whenever Euclidean distance squared is $\le D^2$.

---

### P12 — `[Codeforces 653D]` Delivery Bears (`[EN]`)
- **Judge URL**: [https://codeforces.com/problemset/problem/653/D](https://codeforces.com/problemset/problem/653/D)
- **Constraints**: $N \le 50$ nodes, $M \le 500$ directed edges with weight limit $c_e \le 10^6$, $X \le 10^5$ bears. All $X$ bears must carry the **exact same weight $w \in \mathbb{R}_{\ge 0}$** along paths from $1$ to $N$, and if $k_e \in \mathbb{Z}_{\ge 0}$ bears traverse edge $e$, then $k_e \cdot w \le c_e$. Maximize total weight $X \cdot w$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  On edge $e$, the number of bears $k_e$ must be an **integer**, while $w$ is a continuous real parameter shared across all edges: $k_e \le \lfloor c_e / w \rfloor$. This couples continuous optimization ($w$) with integer max-flow ($k_e$).
- **Step 2 & 3 — Parametric Binary Search + Integer Flow Compilation**:
  For a fixed per-bear weight $w > 0$, edge $e$ can accommodate at most:
  $$\text{cap}_w(e) = \min\!\left(X, \left\lfloor \frac{c_e}{w} \right\rfloor\right) \in \mathbb{Z}_{\ge 0}$$
  integer bears. The weight $w$ is feasible iff $\text{MaxFlow}_{\text{cap}_w}(1, N) \ge X$. Since $\text{cap}_w(e)$ is monotonically non-increasing in $w$, we binary search on $w \in [0, 10^6]$ for $80$ iterations!
  - **Overflow Trap**: When $w$ is tiny ($w \approx 10^{-7}$), $\lfloor c_e / w \rfloor \approx 10^{13}$ overflows 32-bit `int`! Capping each edge capacity at $\min((long\;long)X, \lfloor c_e / w \rfloor)$ prevents overflow and bounds the max-flow by $X$.
- **Step 4 — Complete Solution & Complexity**:
  $80$ iterations of Dinic on $N \le 50, M \le 500$ takes $80 \times O(V^2 E) \approx 5 \times 10^6$ ops ($\le 30\text{ ms}$). Print $X \cdot w^*$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Fix the weight $w$ carried by a single bear. How many integer bears can traverse edge $e$ of capacity $c_e$?
  - *Hint 2*: Binary search on $w$ for $80$ iterations; for each $w$, check if $\text{MaxFlow}(1, N) \ge X$ with integer capacities $\min(X, \lfloor c_e / w \rfloor)$.
  - *Hint 3*: Always clamp $\lfloor c_e / w \rfloor$ at $X$ so tiny values of $w$ don't overflow integer types.

---

### P13 — `[Codeforces 498C]` Array and Operations (`[EN]`)
- **Judge URL**: [https://codeforces.com/problemset/problem/498/C](https://codeforces.com/problemset/problem/498/C)
- **Constraints**: Array $a_1, \dots, a_N$ ($N \le 100, a_i \le 10^9$), and $M \le 100$ "good pairs" $(i_k, j_k)$ where **$i_k + j_k$ is always odd**. In one operation, choose a good pair $(i, j)$ and a common divisor $d > 1$ of $\gcd(a_i, a_j)$, and divide both $a_i$ and $a_j$ by $d$. Maximize the total number of operations.
- **Step 1 — Non-Graph Diagnostic Signal**:
  First, dividing by a composite $d$ is always suboptimal compared to dividing by its prime factors one at a time, and by the Fundamental Theorem of Arithmetic, **different prime factors $p$ never interact**! Second, every pair $(i_k, j_k)$ has $i_k + j_k$ odd — meaning one index is **odd** and the other is **even**, so the interaction graph is **bipartite**!
- **Step 2 & 3 — Prime-Factor Decoupling & Bipartite $b$-Matching**:
  Collect all distinct prime factors $p$ across $a_1, \dots, a_N$ (at most $100 \times 10 = 1000$ distinct primes). For each prime $p$ independently:
  - Let $e_p(i) = v_p(a_i)$ be the exponent of $p$ in $a_i$.
  - Construct a bipartite network with Odd indices on the left ($S \to i_{\text{odd}}$ with capacity $e_p(i)$), Even indices on the right ($j_{\text{even}} \to T$ with capacity $e_p(j)$), and cross edges $i_{\text{odd}} \to j_{\text{even}}$ with capacity $\infty$ for each good pair.
  - Sum $\text{MaxFlow}_p(S, T)$ over all distinct primes $p$.
- **Step 4 — Complete Solution & Complexity**:
  At most $O(N \log(\max a_i))$ distinct primes, each solved by Dinic on a tiny graph of $\le 100$ nodes in $< 10\text{ ms}$ total.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Always divide by prime numbers $p$; why are different primes $p$ completely independent of each other?
  - *Hint 2*: Notice the constraint that $i_k + j_k$ is odd — what does that tell you about the graph of good pairs?
  - *Hint 3*: For each prime $p$ dividing at least one $a_i$, run Max-Flow on the Odd-index to Even-index bipartite graph with vertex capacities $v_p(a_i)$.

---

### P14 — `[AtCoder ARC 074 D (F)]` Lotus Leaves (`[JA]`)
- **Judge URL**: [https://atcoder.jp/contests/arc074/tasks/arc074_b](https://atcoder.jp/contests/arc074/tasks/arc074_b)
- **Constraints**: $H \times W$ grid ($H, W \le 100$) with start `S`, target `T`, and lotus leaves `o`. A frog can jump between any two leaves in the **same row or the same column**. Remove the minimum number of `o` leaves to block all paths from `S` to `T` (or output `-1` if `S` and `T` share a row or column).
- **Step 1 — Non-Graph Diagnostic Signal**:
  Minimum vertex cut on a grid where rows and columns form cliques. Naive vertex splitting with pairwise row/column edges creates $O(HW(H+W)) \approx 2 \times 10^6$ edges; **Row/Column Hub Sparsification** (Section 5.5) collapses this to $O(HW)$ edges!
- **Step 2 & 3 — Algebraic & Hub Sparsification Compilation**:
  - If $r_S == r_T$ or $c_S == c_T$, output `-1` immediately.
  - Create $H$ Row Hubs $R_1, \dots, R_H$ and $W$ Column Hubs $C_1, \dots, C_W$.
  - Connect $S_{\text{src}} \xrightarrow{\infty} R_{r_S}$, $S_{\text{src}} \xrightarrow{\infty} C_{c_S}$, and $R_{r_T} \xrightarrow{\infty} T_{\text{sink}}$, $C_{c_T} \xrightarrow{\infty} T_{\text{sink}}$.
  - Every lotus leaf `o` at $(r, c)$ is the **only bridge** allowing a jump from Row $r$ to Column $c$ (or vice versa) at $(r, c)$! Thus each leaf `o` at $(r, c)$ compiles to a **single undirected edge of capacity $1$ between $R_r$ and $C_c$** ($R_r \xrightarrow{1} C_c$ and $C_c \xrightarrow{1} R_r$)!
- **Step 4 — Complete Solution & Complexity**:
  Only $V = H + W + 2 \le 202$ vertices and $E \le HW \le 10^4$ unit-capacity edges! Dinic runs in $O(HW\sqrt{H+W}) \approx 1.4 \times 10^5$ ops ($< 2\text{ ms}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Instead of connecting leaves directly to each other, introduce $H$ Row Hub vertices and $W$ Column Hub vertices.
  - *Hint 2*: Jumping to leaf $(r, c)$ along row $r$ and jumping out along column $c$ corresponds to traversing an edge between $R_r$ and $C_c$.
  - *Hint 3*: Each leaf `o` at $(r, c)$ is simply an undirected edge of capacity $1$ between $R_r$ and $C_c$!

---

### P15 — `[AtCoder ABC 285 G]` Tatami (`[JA]`)
- **Judge URL**: [https://atcoder.jp/contests/abc285/tasks/abc285_g](https://atcoder.jp/contests/abc285/tasks/abc285_g)
- **Constraints**: $H \times W$ grid ($H, W \le 300$, $HW \le 9 \times 10^4$). Each cell is `'1'` (must be covered by a $1 \times 1$ monomino), `'2'` (must be covered by a $1 \times 2$ or $2 \times 1$ domino), or `'?'` (can be covered by either a $1 \times 1$ or a $1 \times 2$ tatami). Determine if a valid tiling exists.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Domino tiling on a grid is a bipartite matching between Black ($r + c$ even) and White ($r + c$ odd) cells:
  - Cells with `'1'` are forbidden (already covered by $1 \times 1$).
  - Cells with `'2'` **must** be matched with an adjacent `'2'` or `'?'` cell (degree in matching $\in [1, 1]$).
  - Cells with `'?'` **may optionally** be matched with an adjacent `'2'` or `'?'` cell (if unmatched, they simply become a $1 \times 1$ monomino! So degree in matching $\in [0, 1]$).
  This is a **Bipartite Matching with Lower and Upper Vertex Degree Bounds `[1, 1]` vs. `[0, 1]`**!
- **Step 2 & 3 — Algebraic & Variant-2 Lower-Bound Compilation**:
  - Color the grid: $L = \{(r, c) : (r+c) \text{ even}\}$, $R = \{(r, c) : (r+c) \text{ odd}\}$.
  - For each $u \in L$ with $G[u] \neq \text{'1'}$:
    - If $G[u] == \text{'2'}$, add $S \xrightarrow{[1, 1]} u$.
    - If $G[u] == \text{'?'}$, add $S \xrightarrow{[0, 1]} u$.
  - For each $v \in R$ with $G[v] \neq \text{'1'}$:
    - If $G[v] == \text{'2'}$, add $v \xrightarrow{[1, 1]} T$.
    - If $G[v] == \text{'?'}$, add $v \xrightarrow{[0, 1]} T$.
  - For each adjacent pair $(u, v) \in L \times R$ (both $\neq \text{'1'}$), add $u \xrightarrow{[0, 1]} v$.
  - Add feedback arc $T \xrightarrow{[0, \infty)} S$ and solve **Variant 2 (`有源汇上下界可行流`)** via `dinic(S*, T*)`!
- **Step 4 — Complete Solution & Complexity**:
  Because all slack capacities in $G'$ on $L \cup R$ are unit capacities, Dinic on $G'$ runs in $O(HW \sqrt{HW}) \approx 2.7 \times 10^7$ ops ($\approx 80\text{ ms}$). Print `Yes` iff $\text{MaxFlow}(S^*, T^*) == \Sigma^+$ (where $\Sigma^+$ is the total number of `'2'` cells).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Color the grid like a chessboard ($r+c$ parity). A $1 \times 2$ domino matches one Black cell with one adjacent White cell.
  - *Hint 2*: A `'2'` cell requires matching degree in $[1, 1]$, whereas a `'?'` cell allows matching degree in $[0, 1]$.
  - *Hint 3*: Compile the $[1, 1]$ and $[0, 1]$ bounds on $S \to u$ and $v \to T$ into Variant 2 (`有源汇上下界可行流`) with feedback edge $T \xrightarrow{[0, \infty)} S$.

---

### Tier 3: Advanced (`P16`–`P23`)

---

### P16 — `[ZJOI2010 / Luogu P5192]` Shoot the Bullet (东方文花帖) (`[ZH]`)
- **Judge URL**: [https://www.luogu.com.cn/problem/P5192](https://www.luogu.com.cn/problem/P5192)
- **Constraints**: $N \le 365$ days, $M \le 1000$ girls. Day $i$ allows **at most $D_i$** photos total; Girl $j$ requires **at least $G_j$** photos across all days; on Day $i$, Girl $j \in C_i$ can be photographed in $[L_{i,j}, R_{i,j}]$ times. Maximize total photos taken (or output `-1` if infeasible).
- **Step 1 — Non-Graph Diagnostic Signal**:
  Three simultaneous layers of interval bounds: per-day upper bounds $[0, D_i]$, per-(day, girl) box bounds $[L_{i,j}, R_{i,j}]$, and per-girl lower bounds $[G_j, \infty)$, with global objective $\max \sum_{i,j} x_{i,j}$. This is the canonical benchmark for **Variant 3 (`有源汇上下界最大流`)**.
- **Step 2 & 3 — Algebraic & Variant-3 Compilation**:
  Let $x_{i, j} \in [L_{i, j}, R_{i, j}]$ be photos of girl $j$ on day $i$:
  - Source $S \to \text{Day}_i$ with $[0, D_i]$ ($\sum_j x_{i,j} \le D_i$).
  - Cross arc $\text{Day}_i \to \text{Girl}_j$ with $[L_{i,j}, R_{i,j}]$.
  - Sink arc $\text{Girl}_j \to T$ with $[G_j, \infty)$ ($\sum_i x_{i,j} \ge G_j$).
  - Feedback arc $e_{\text{fb}} = (T \to S)$ with $[0, \infty)$.
  - **Phase 1**: Construct $G'$ with $S^*, T^*$ and run `F1 = dinic(S*, T*)`. If $F_1 < \Sigma^+$, output `-1`.
  - **Phase 2**: Record $f_0 = \text{cap}[e_{\text{fb}} \oplus 1]$, set `cap[e_fb] = cap[e_fb ^ 1] = 0`, and output $f_0 + \text{dinic}(S, T)$.
- **Step 4 — Complete Solution & Complexity**:
  $|V| = N + M + 4 \le 1369$, $|E| \le 3 \times 10^4$; two Dinic runs finish in $\approx 50\text{ ms}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Model Days on the left ($[0, D_i]$ from $S$), Girls on the right ($[G_j, \infty)$ to $T$), and daily girl quotas $[L_{i,j}, R_{i,j}]$ in between.
  - *Hint 2*: Add feedback edge $T \xrightarrow{[0, \infty)} S$ to test feasibility via `dinic(S*, T*)`.
  - *Hint 3*: Don't forget to zero out both half-edges of $T \to S$ before running `dinic(S, T)` in Phase 2!

---

### P17 — `[POJ 2396]` Budget (`[EN]`/`[ZH]`)
- **Judge URL**: [http://poj.org/problem?id=2396](http://poj.org/problem?id=2396)
- **Constraints**: $M \le 200$ rows, $N \le 20$ columns, given exact row sums $R_i$ and exact column sums $C_j$, plus $K$ submatrix constraints (`i j op v` where `i=0` means all rows, `j=0` means all columns, and `op` $\in \{`<`, `=`, `>`\}$). Reconstruct a valid nonnegative integer matrix $X_{i,j}$ or print `IMPOSSIBLE`.
- **Step 1 — Non-Graph Diagnostic Signal**:
  First collapse all $K$ constraints on each cell $(i, j)$ into a single intersected integer interval $[L_{i,j}, U_{i,j}]$:
  - `'<' v`: $U_{i,j} = \min(U_{i,j}, v - 1)$
  - `'>' v`: $L_{i,j} = \max(L_{i,j}, v + 1)$
  - `'=' v`: $L_{i,j} = \max(L_{i,j}, v)$ and $U_{i,j} = \min(U_{i,j}, v)$
  If $L_{i,j} > U_{i,j}$ for any cell, or $\sum R_i \neq \sum C_j$, output `IMPOSSIBLE` immediately!
- **Step 2 & 3 — Algebraic & Variant-2 Compilation**:
  - Row supply: $S \to \text{Row}_i$ with $[R_i, R_i]$ ($u - l = 0$ in $G'$!).
  - Column demand: $\text{Col}_j \to T$ with $[C_j, C_j]$ ($u - l = 0$ in $G'$!).
  - Cell entry: $\text{Row}_i \to \text{Col}_j$ with $[L_{i,j}, U_{i,j}]$.
  - Feedback arc: $T \xrightarrow{[0, \infty)} S$.
- **Step 4 — Complete Solution & Complexity**:
  Run `dinic(S*, T*)`. If $\text{MaxFlow}(S^*, T^*) == \Sigma^+$, recover $X_{i,j} = L_{i,j} + \tilde{f}(\text{Row}_i \to \text{Col}_j)$; else print `IMPOSSIBLE`. Complexity: $O((M+N)^2 MN) \le 10^6$ ops.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Intersect all `<, =, >` constraints on cell $(i, j)$ into a single tight integer box $[L_{i,j}, U_{i,j}]$ before building any graph.
  - *Hint 2*: Exact row and column sums are simply lower-and-upper-bound edges $[R_i, R_i]$ and $[C_j, C_j]$.
  - *Hint 3*: Check both $L_{i,j} \le U_{i,j}$ for all $(i,j)$ and $\sum R_i == \sum C_j$ before running `dinic(S*, T*)`.

---

### P18 — `[Luogu P4843 / LOJ #2042]` 清理雪道 (`[ZH]`)
- **Judge URL**: [https://www.luogu.com.cn/problem/P4843](https://www.luogu.com.cn/problem/P4843)
- **Constraints**: $N \le 100$ nodes forming a DAG. Every directed edge $e \in E$ is a snowy slope that must be traversed **at least once**. A snowplow can start at any vertex and end at any vertex. Find the **minimum number of snowplows** required.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Minimum-fleet edge cover on a DAG: every edge has $f(e) \in [1, \infty)$, and we want to **minimize** total snowplows $|f|$ — textbook **Variant 4 (`有源汇上下界最小流`)**.
- **Step 2 & 3 — Algebraic & Variant-4 Compilation**:
  - Create global source $S$ and sink $T$. Since snowplows can start and end at any vertex $v \in \{1, \dots, N\}$, add $S \xrightarrow{[0, \infty)} v$ and $v \xrightarrow{[0, \infty)} T$ for all $v$.
  - For each snowy slope $e = (u \to v) \in E$, add $u \xrightarrow{[1, \infty)} v$.
  - Add feedback arc $e_{\text{fb}} = (T \xrightarrow{[0, \infty)} S)$.
  - **Phase 1**: Run `dinic(S*, T*)` on $G'$ (always feasible since $S \to v \to T$ has infinite capacity) and record $f_0 = \text{cap}[e_{\text{fb}} \oplus 1]$.
  - **Phase 2**: Set `cap[e_fb] = cap[e_fb ^ 1] = 0`, and push excess flow backward from $T$ to $S$: $f_{\text{sub}} = \text{dinic}(T, S)$. Output $f_0 - f_{\text{sub}}$.
- **Step 4 — Complete Solution & Complexity**:
  Two Dinic calls on $104$ vertices finish in $< 3\text{ ms}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Every slope $e = (u \to v)$ requires flow in $[1, \infty)$, and any node $v$ can start ($S \xrightarrow{[0, \infty)} v$) or end ($v \xrightarrow{[0, \infty)} T$) a route.
  - *Hint 2*: First find any feasible flow $f_0$ via `dinic(S*, T*)` with feedback edge $T \to S$.
  - *Hint 3*: Delete $T \to S$ and run `dinic(T, S)` (from sink back to source!) to cancel as many redundant snowplow routes as possible: answer is $f_0 - \text{dinic}(T, S)$.

---

### P19 — `[Codeforces 704D]` Captain America (`[EN]`)
- **Judge URL**: [https://codeforces.com/problemset/problem/704/D](https://codeforces.com/problemset/problem/704/D)
- **Constraints**: $N \le 10^5$ shields at $(x_i, y_i)$, $M \le 10^5$ horizontal/vertical line constraints $|R_L - B_L| \le d_L$, red paint cost $r$, blue paint cost $b$. Minimize total paint cost (or output `-1`).
- **Step 1 — Non-Graph Diagnostic Signal**:
  Without Loss of Generality assume $r \le b$ (if $r > b$, swap $r \leftrightarrow b$ and swap `'r'` $\leftrightarrow$ `'b'` in the output). Then painting all $N$ shields blue costs $N \cdot b$, and each shield painted **Red** saves $b - r \ge 0$ cost! Thus we want to **maximize the number of Red shields** subject to $|R_L - B_L| \le d_L$ on each line $L$.
- **Step 2 — Intermediate Algebraic Representation**:
  Let line $L$ contain $c_L$ shields in total. Since $R_L + B_L = c_L$, the discrepancy constraint $-d_L \le R_L - (c_L - R_L) \le d_L \iff c_L - d_L \le 2 R_L \le c_L + d_L$ compiles to the tight integer interval:
  $$L_L \triangleq \max\!\left(0, \left\lceil \frac{c_L - d_L}{2} \right\rceil\right) \le R_L \le \min\!\left(c_L, \left\lfloor \frac{c_L + d_L}{2} \right\rfloor\right) \triangleq U_L$$
  If multiple constraints apply to the same line $x = X$ or $y = Y$, take the minimum $d_L$. If $L_L > U_L$ for any line, output `-1` immediately!
- **Step 3 — Reverse-Engineering Scratchpad**:
  - Coordinate-compress active $x$-lines ($X_1, \dots, X_p$) and $y$-lines ($Y_1, \dots, Y_q$).
  - Source $S \to X_a$ with $[L_{X_a}, U_{X_a}]$.
  - Sink $Y_b \to T$ with $[L_{Y_b}, U_{Y_b}]$.
  - Shield $i$ at $(x_i, y_i)$ is a unit-capacity cross edge $X_{a_i} \to Y_{b_i}$ with $[0, 1]$.
  - Solve **Variant 3 (`有源汇上下界最大流`)**!
- **Step 4 — Complete Solution & Complexity**:
  Because every shield edge $X_a \to Y_b$ has unit capacity $1$, Dinic on this bipartite-like network runs in **$O((N + M)\sqrt{N})$** time ($\approx 150\text{ ms}$)! Total cost is $|f_{\max}| \cdot r + (N - |f_{\max}|) \cdot b$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Assume $r \le b$ by symmetry; then minimizing cost is identical to maximizing the total number of Red shields.
  - *Hint 2*: Substitute $B_L = c_L - R_L$ into $|R_L - B_L| \le d_L$ to get $\lceil (c_L - d_L)/2 \rceil \le R_L \le \lfloor (c_L + d_L)/2 \rfloor$.
  - *Hint 3*: Each shield $(x_i, y_i)$ is an edge $X_i \xrightarrow{[0, 1]} Y_i$; run Variant 3 (`有源汇上下界最大流`) to maximize Red shields.

---

### P20 — `[CQOI2014 / Luogu P3163]` 危桥 (`[ZH]`)
- **Judge URL**: [https://www.luogu.com.cn/problem/P3163](https://www.luogu.com.cn/problem/P3163)
- **Constraints**: $N \le 50$ islands with undirected bridges (normal bridge capacity $\infty$, dangerous bridge capacity $2$ traversals total). Alice needs $a_n$ round trips between $a_1$ and $a_2$ (equivalent to $a_n$ one-way trips $a_1 \to a_2$, dividing bridge capacities by $2$ so dangerous bridges have capacity $1$), and Bob needs $b_n$ one-way trips between $b_1$ and $b_2$. Can both succeed simultaneously?
- **Step 1 — Non-Graph Diagnostic Signal**:
  **Two-Commodity Undirected Flow!** If we only test a single multi-source max-flow with $S \xrightarrow{a_n} a_1$, $S \xrightarrow{b_n} b_1$ and $a_2 \xrightarrow{a_n} T$, $b_2 \xrightarrow{b_n} T$, what goes wrong? **Cross-Commodity Leakage**: flow from $a_1$ might exit at $b_2$ while flow from $b_1$ exits at $a_2$!
- **Step 2 & 3 — Algebraic Superposition & The Okamura–Seymour Swap Trick**:
  Suppose we run **Run 1** ($S \to \{a_1, b_1\}$, $\{a_2, b_2\} \to T$) and obtain flow $F^{(1)}$ of value $a_n + b_n$, AND we **swap Bob's terminals $b_1 \leftrightarrow b_2$** to run **Run 2** ($S \to \{a_1, b_2\}$, $\{a_2, b_1\} \to T$) and also obtain flow $F^{(2)}$ of value $a_n + b_n$!
  In Run 1, suppose $a_n - \delta$ units go $a_1 \to a_2$, $\delta$ go $a_1 \to b_2$, $\delta$ go $b_1 \to a_2$, and $b_n - \delta$ go $b_1 \to b_2$. Since the underlying graph is **undirected**, we can reverse Bob's components in Run 2 and take the **half-sum and half-difference**:
  $$f_{\text{Alice}}(e) = \frac{F^{(1)}(e) + F^{(2)}(e)}{2}, \qquad f_{\text{Bob}}(e) = \frac{F^{(1)}(e) - F^{(2)}(e)}{2}$$
  - In $f_{\text{Alice}}$, the flows at $b_1$ and $b_2$ cancel to $0$, while net outflow at $a_1$ is $\frac{a_n + a_n}{2} = a_n$ and at $a_2$ is $-a_n$!
  - In $f_{\text{Bob}}$, the flows at $a_1$ and $a_2$ cancel to $0$, while net outflow at $b_1$ is $\frac{b_n - (-b_n)}{2} = b_n$ and at $b_2$ is $-b_n$!
  - On every undirected edge $e$, $|f_{\text{Alice}}(e)| + |f_{\text{Bob}}(e)| = \left|\frac{F^{(1)}(e) + F^{(2)}(e)}{2}\right| + \left|\frac{F^{(1)}(e) - F^{(2)}(e)}{2}\right| = \max(|F^{(1)}(e)|, |F^{(2)}(e)|) \le c(e)$!
- **Step 4 — Complete Solution & Complexity**:
  Output `Yes` iff **both** Run 1 (`a1, b1 -> a2, b2`) and Run 2 (`a1, b2 -> a2, b1`) achieve Max-Flow $= a_n + b_n$. Two Dinic calls on $52$ vertices take $< 2\text{ ms}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Why is checking $\text{MaxFlow}(\{a_1, b_1\} \to \{a_2, b_2\}) == a_n + b_n$ necessary but NOT sufficient?
  - *Hint 2*: What happens if you reverse Bob's direction ($b_2 \to b_1$) while keeping Alice's direction ($a_1 \to a_2$) on an undirected graph?
  - *Hint 3*: Run Max-Flow twice — once with $(a_1, b_1) \to (a_2, b_2)$ and once with $(a_1, b_2) \to (a_2, b_1)$. Both must equal $a_n + b_n$.

---

### P21 — `[Luogu P3254 / POJ 3498 / Horn]` Preemptive Parallel-Machine Scheduling (`[EN]`/`[ZH]`)
- **Judge URL**: [https://www.luogu.com.cn/problem/P3254](https://www.luogu.com.cn/problem/P3254) (and general Horn scheduling with release times $r_j$ and deadlines $d_j$)
- **Constraints**: $N \le 200$ jobs with $(r_j, p_j, d_j)$ and $M \le 50$ parallel machines. Determine feasibility and output the exact preemptive schedule intervals on each machine.
- **Step 1–4 — Compilation & McNaughton Wrap-Around Reconstruction**:
  Directly implements **Section 2.5 (Horn's Theorem & McNaughton's Wrap-Around Rule)**:
  1. Sort unique timestamps $\{r_j\} \cup \{d_j\}$ into $t_0 < t_1 < \dots < t_K$ ($K \le 2N$), with $\Delta_k = t_k - t_{k-1}$.
  2. Build $S \xrightarrow{p_j} J_j \xrightarrow{\Delta_k} I_k \xrightarrow{M \Delta_k} T$ for all $I_k \subseteq [r_j, d_j]$.
  3. Check $\text{MaxFlow}(S, T) == \sum_{j=1}^N p_j$.
  4. For each interval $I_k$, maintain a running cursor `(machine m = 1, offset cur = 0)` and allocate $x_{j, k} = f^*(J_j \to I_k) \le \Delta_k$ across $[t_{k-1} + \text{cur}, t_{k-1} + \text{cur} + x_{j,k}]$, wrapping around at $t_k$ onto machine $m+1$. Complexity: $O(N^2 \sqrt{N})$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Coordinate-compress all $r_j$ and $d_j$ into elementary intervals $I_k = [t_{k-1}, t_k]$ of length $\Delta_k$.
  - *Hint 2*: Why must the cross-edge $J_j \to I_k$ have capacity $\Delta_k$ while $I_k \to T$ has capacity $M \Delta_k$?
  - *Hint 3*: Reconstruct each interval $I_k$'s schedule using McNaughton's wrap-around strip packing.

---

### P22 — `[BZOJ 3698]` XWW 的难题 (`[ZH]`)
- **Judge URL**: [https://darkbzoj.cc/problem/3698](https://darkbzoj.cc/problem/3698)
- **Constraints**: $N \times N$ real matrix $A$ ($N \le 100$) where the last row $A_{N, j} = \sum_{i=1}^{N-1} A_{i, j}$, the last column $A_{i, N} = \sum_{j=1}^{N-1} A_{i, j}$, and $A_{N, N} = \sum_{i=1}^{N-1} \sum_{j=1}^{N-1} A_{i, j}$. Round every entry $A_{i, j}$ to $B_{i, j} \in \{\lfloor A_{i, j} \rfloor, \lceil A_{i, j} \rceil\}$ preserving all row/column/corner sums, and **maximize** $\sum_{i=1}^N \sum_{j=1}^N B_{i, j}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  By conservation, $\sum_{i=1}^{N-1} \sum_{j=1}^{N-1} B_{i, j} = \sum_{i=1}^{N-1} B_{i, N} = \sum_{j=1}^{N-1} B_{N, j} = B_{N, N}$. Thus the grand sum of all $N^2$ entries of $B$ is simply **$4 \times B_{N, N}$** (or $3 \times \text{flow}$ if $A_{N,N}$ is fixed)! Maximizing the sum of $B$ is identical to **maximizing total flow $|f|$ from $S$ to $T$** under Variant 3!
- **Step 2 & 3 — Algebraic & Variant-3 Compilation**:
  - For $i \in \{1, \dots, N-1\}$: add $S \to R_i$ with $[\lfloor A_{i, N} \rfloor, \lceil A_{i, N} \rceil]$.
  - For $j \in \{1, \dots, N-1\}$: add $C_j \to T$ with $[\lfloor A_{N, j} \rfloor, \lceil A_{N, j} \rceil]$.
  - For $i, j \in \{1, \dots, N-1\}$: add $R_i \to C_j$ with $[\lfloor A_{i, j} \rfloor, \lceil A_{i, j} \rceil]$.
  - Add feedback arc $T \xrightarrow{[0, \infty)} S$ and solve **Variant 3 (`有源汇上下界最大流`)**.
- **Step 4 — Complete Solution & Complexity**:
  Run `dinic(S*, T*)` then `dinic(S, T)` in $O(N^3)$ time ($\le 15\text{ ms}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Notice that the $(N-1) \times (N-1)$ interior entries determine the $N$-th row and $N$-th column sums via flow conservation.
  - *Hint 2*: Each entry $A_{i,j}$ gives a lower bound $\lfloor A_{i,j} \rfloor$ and an upper bound $\lceil A_{i,j} \rceil$.
  - *Hint 3*: Run Variant 3 (`有源汇上下界最大流`) from $S$ (row sums) to $T$ (column sums) and multiply the maximum flow by $3$.

---

### P23 — `[ZOJ 2587 / UVa 10480]` Unique Attack (Minimum-Cut Uniqueness) (`[EN]`/`[ZH]`)
- **Judge URL**: [https://pintia.cn/problem-sets/91827364500/exam/problems/91827366118](https://pintia.cn/problem-sets/91827364500/exam/problems/91827366118)
- **Constraints**: $N \le 800$ vertices, $M \le 10000$ undirected edges with capacities $c_e$, terminals $A, B$. Determine whether the minimum $A$-$B$ cut is **unique** (`UNIQUE` vs. `AMBIGUOUS`).
- **Step 1 — Non-Graph Diagnostic Signal**:
  Directly tests **Corollary 4.3 (Minimum Cut Uniqueness Criterion)** on the distributive lattice $\mathcal{L}_{\min}$!
- **Step 2 & 3 — Algebraic & Residual Reachability Compilation**:
  By Section 4.2, the minimum $A$-$B$ cut is unique ($|\mathcal{L}_{\min}| = 1$) if and only if the source-minimal cut $S_{\min}$ equals the source-maximal cut $S_{\max} = V \setminus T_{\min}$, i.e.:
  $$S_{\min} \cup T_{\min} = V \iff |S_{\min}| + |T_{\min}| = N$$
  where $S_{\min} = \{v \in V : A \leadsto v \text{ in } G_{f^*}\}$ and $T_{\min} = \{v \in V : v \leadsto B \text{ in } G_{f^*}\}$.
  - **Subtle Trap**: Why is "unique set of cut edges" equivalent to $S_{\min} \cup T_{\min} = V$ in a connected graph? Because if any vertex $w \notin S_{\min} \cup T_{\min}$ exists in a connected graph, moving $w$'s residual SCC from $T$ to $S$ changes the cut partition and swaps the cut edges incident to $w$'s SCC!
- **Step 4 — Complete Solution & Complexity**:
  1. Build the undirected network using compact pairs (`cap[2k] = cap[2k+1] = c`) and run Dinic from $A$ to $B$.
  2. Run a forward BFS from $A$ in $G_{f^*}$ (using arcs `cap[e] > 0`) to count $|S_{\min}|$.
  3. Run a backward BFS from $B$ in $G_{f^*}$ (using reverse arcs `cap[e ^ 1] > 0`) to count $|T_{\min}|$.
  4. Output `UNIQUE` iff $|S_{\min}| + |T_{\min}| == N$, else `AMBIGUOUS`. Complexity: $O(\text{Dinic} + N + M)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Recall that $S_{\min}$ is the smallest $s$-side of a minimum cut and $S_{\max} = V \setminus T_{\min}$ is the largest $s$-side.
  - *Hint 2*: How do you compute $S_{\min}$ and $T_{\min}$ from the final residual network $G_{f^*}$?
  - *Hint 3*: Run forward BFS from $A$ and reverse BFS from $B$ in $G_{f^*}$; the minimum cut is unique iff every vertex is visited by one of the two searches ($|S_{\min}| + |T_{\min}| == N$).

---

### Tier 4: Mastery (`P24`–`P30`)

---

### P24 — `[SDOI2014 / Luogu P3308]` LIS (`[ZH]`)
- **Judge URL**: [https://www.luogu.com.cn/problem/P3308](https://www.luogu.com.cn/problem/P3308)
- **Constraints**: $T \le 5$ test cases, $N \le 700$. Each item $i$ has value $A_i$, deletion cost $B_i$, and tie-breaking rank $C_i$ (a permutation of $1 \dots N$). Find a minimum-cost subset of items to delete so that the length of the LIS of the remaining sequence strictly decreases; among all minimum-cost subsets, output the one whose sorted $C_i$-rank tuple is **lexicographically smallest**.
- **Step 1 — Non-Graph Diagnostic Signal**:
  First compute $dp[i]$ (LIS ending at $i$) and $K = \max_i dp[i]$, and build the vertex-split LIS DAG ($i_{\text{in}} \xrightarrow{B_i} i_{\text{out}}$, $S \xrightarrow{\infty} i_{\text{in}}$ if $dp[i]=1$, $i_{\text{out}} \xrightarrow{\infty} T$ if $dp[i]=K$, $i_{\text{out}} \xrightarrow{\infty} j_{\text{in}}$ if $i < j, A_i < A_j, dp[j] = dp[i]+1$).
  Now we need the **lexicographically smallest minimum vertex cut** sorted by $C_i$. Unlike `P03` ($N \le 100$), here $N \le 700$ and $E = O(N^2) \le 2.5 \times 10^5$: re-running Dinic from scratch $N$ times would cost $700 \times \text{Dinic} \implies \text{TLE}$! We MUST use **Residual Reachability Testing + Dynamic Flow Rollback (`退流`, Section 4.5)**!
- **Step 2 & 3 — Algebraic Reachability Test & `退流` Rollback**:
  Sort the items in increasing order of $C_i$: $u_1, u_2, \dots, u_N$. For each $u$ in this order:
  1. **O(E) Feasibility Test**: Can $u$'s internal bridge $e_u = (u_{\text{in}} \to u_{\text{out}})$ belong to a minimum cut of the current residual network $G_{f^*}$? By Theorem 4.5, $e_u$ is a feasible minimum-cut edge **if and only if** `cap[e_u] == 0` AND **$u_{\text{in}}$ cannot reach $u_{\text{out}}$ in $G_{f^*}$** (`!bfs(u_in, u_out)` in $O(V + E)$ time)!
  2. **Dynamic Flow Rollback (`退流`)**: If `!bfs(u_in, u_out)` holds, we commit $u$ to our answer and permanently delete $e_u$ (which carried $k = B_u$ units of flow):
     - Set `cap[e_u] = cap[e_u ^ 1] = 0`.
     - Reel back suffix flow: `dinic_bounded(T, u_out, B_u)` (or unbounded `dinic(T, u_out)`).
     - Reel back prefix flow: `dinic_bounded(u_in, S, B_u)` (or unbounded `dinic(u_in, S)`).
     - Because $e_u$ was a feasible minimum-cut edge, the global Max-Flow drops by **exactly $B_u$**, and no re-augmentation `dinic(S, T)` is needed!
- **Step 4 — Complete Solution & Complexity**:
  1 initial Dinic + $N$ BFS checks + at most $K \le N$ rollbacks (since an LIS cut contains at most 1 item per $dp$-layer, or $\le N$ items total!) $\implies O(\text{Dinic} + N \cdot E)$ time ($\approx 200\text{ ms}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Build the LIS transition DAG with vertex bridges $i_{\text{in}} \xrightarrow{B_i} i_{\text{out}}$ and compute the initial Max-Flow once.
  - *Hint 2*: Process vertices $u$ in increasing order of $C_u$: $u$ can be in a minimum cut iff $u_{\text{in}} \to u_{\text{out}}$ is saturated and $u_{\text{in}} \not\to^* u_{\text{out}}$ in $G_{f^*}$.
  - *Hint 3*: To commit $u$ without rebuilding the graph, zero out $u_{\text{in}} \to u_{\text{out}}$ and run `dinic(T, u_out)` and `dinic(u_in, S)` (`退流`).

---

### P25 — `[Codeforces 1383F]` Special Edges (`[EN]`)
- **Judge URL**: [https://codeforces.com/problemset/problem/1383/F](https://codeforces.com/problemset/problem/1383/F)
- **Constraints**: $N \le 10^4$ vertices, $M \le 10^4$ directed edges with $c_e \le 25$. The first $K \le 10$ edges are "special". Answer $Q \le 2 \times 10^5$ queries; each query specifies new capacities $w_1, \dots, w_K \in [0, 25]$ for the $K$ special edges and asks for $\text{MaxFlow}(1, N)$. Time Limit: $5.0\text{ s}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Running Max-Flow $Q = 2 \times 10^5$ times is impossible, but $K \le 10 \implies 2^K = 1024$ is tiny!
- **Step 2 — Intermediate Algebraic Representation ($2^K$ Cut-Mask Duality)**:
  Any $1$-$N$ cut $(S, V \setminus S)$ cuts a subset $\text{mask} \in \{0, 1\}^K$ of the $K$ special edges, plus some non-special edges of minimum total capacity $\text{base\_cut}[\text{mask}]$. By Max-Flow Min-Cut Duality:
  $$\text{MaxFlow}(w_1, \dots, w_K) = \min_{\text{mask} \in \{0, 1\}^K} \left( \text{base\_cut}[\text{mask}] + \sum_{i \in \text{mask}} w_i \right)$$
  Look at $\text{base\_cut}[\text{mask}]$: it is the minimum cut capacity when special edges $i \in \text{mask}$ have capacity $0$ and special edges $i \notin \text{mask}$ have capacity $\infty$ ($\ge 25$), which by duality equals **$\text{MaxFlow}$ when special edges $i \notin \text{mask}$ are forced to capacity $\infty$ and $i \in \text{mask}$ have capacity $0$**!
- **Step 3 — Reverse-Engineering Scratchpad**:
  1. First set all $K$ special edges to capacity $0$ and run Dinic once to get $\text{base\_cut}[2^K - 1]$ and base residual graph $G_0$.
  2. Traverse the $2^K = 1024$ masks on a recursion tree (or Gray code): moving from a parent state to a child state only increases **one** special edge $e_i$ from $0$ to $25$! Since $c_e \le 25$, augmenting $e_i$ by at most $25$ units of flow on the parent's residual graph takes only a few micro-DFS searches (`Ford-Fulkerson` / `Dinic` capped at $25$).
  3. For each of the $Q$ queries, compute subset sums $\text{sum\_w}[\text{mask}] = \text{sum\_w}[\text{mask} \setminus \{b\}] + w_b$ in $O(2^K)$ time and take $\min_{\text{mask}} (\text{base\_cut}[\text{mask}] + \text{sum\_w}[\text{mask}])$.
- **Step 4 — Complete Solution & Complexity**:
  Precomputation: $O(\text{Dinic}(G_0) + 2^K \cdot 25 \cdot M)$. Queries: $O(Q \cdot 2^K) \approx 2 \times 10^8$ simple integer additions ($\approx 0.4\text{ s}$).
- **3-Tier Progressive Hints**:
  - *Hint 1*: Switch from Max-Flow to Min-Cut: every cut $(S, T)$ is classified by which subset $\text{mask} \subseteq \{1, \dots, K\}$ of special edges crosses $(S, T)$.
  - *Hint 2*: The minimum capacity of non-special edges in a cut with signature $\text{mask}$ equals the Max-Flow when special edges outside $\text{mask}$ have capacity $\infty$ ($25$) and inside $\text{mask}$ have capacity $0$.
  - *Hint 3*: Precompute all $2^K = 1024$ flow values by branching on a recursion tree and augmenting one special edge at a time by $\le 25$ units.

---

### P26 — `[ICPC World Finals 2007 / UVa 1106]` Chips Challenge (`[EN]`)
- **Judge URL**: [https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3547](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3547)
- **Constraints**: $N \times N$ grid ($N \le 40$) with fixed components `'C'`, empty tunable slots `'.'`, and forbidden cells `'/'`. Place as many components $T_{\text{total}}$ as possible so that: (1) for every $i \in \{1, \dots, N\}$, the number of components in Row $i$ **equals** the number of components in Column $i$ ($\text{row}_i = \text{col}_i$), and (2) for every $i$, $\text{row}_i \le \frac{A}{B} T_{\text{total}}$.
- **Step 1 — Non-Graph Diagnostic Signal**:
  The equality $\text{row}_i = \text{col}_i$ for every $i \in \{1, \dots, N\}$ is **exact flow conservation at node $i$** if we view a component at cell $(i, j)$ as $1$ unit of flow on the directed edge $(i \to j)$!
- **Step 2 & 3 — Algebraic Slack Bypass & $K$-Sweep Compilation**:
  Fix the maximum number of components allowed in any single row/column as $K \in \{0, 1, \dots, N\}$. How do we enforce $\text{row}_i = \text{col}_i \le K$ while **maximizing** total flow $\sum_{i=1}^N \text{row}_i$?
  Introduce a **slack bypass variable** $y_i = K - \text{row}_i = K - \text{col}_i \in [0, K]$! Then:
  $$\text{row}_i + y_i = K \quad \text{and} \quad \text{col}_i + y_i = K \qquad \forall i \in \{1, \dots, N\}$$
  Compile this directly into a bipartite lower-bound network:
  - Split each index $i$ into $R_i$ (row $i$) and $C_i$ (column $i$).
  - Supply $S \xrightarrow{[K, K]} R_i$ and demand $C_i \xrightarrow{[K, K]} T$.
  - **Slack Bypass Edge**: $R_i \xrightarrow{[0, K]} C_i$ (representing $y_i = K - \text{row}_i$ unused quota!).
  - **Grid Cell Edge**: For each cell $(i, j)$: if `'C'`, add $R_i \xrightarrow{[1, 1]} C_j$; if `'.'`, add $R_i \xrightarrow{[0, 1]} C_j$.
  -Wait: how do we maximize $\sum \text{row}_i = N K - \sum y_i$ without MCMF? Instead of fixing $S \to R_i$ to $[K, K]$ with a bypass, simply set $S \xrightarrow{[0, K]} R_i$, $C_i \xrightarrow{[0, K]} T$, connect $C_i \xrightarrow{[0, K]} R_i$ directly (so node $i$ has $\text{row}_i = \text{col}_i \le K$), or use MCMF with bypass cost $+1$ and cell cost $0$! Even simpler with pure Max-Flow: contract $C_i \to R_i$ via bridge $v_i^{\text{in}} \xrightarrow{[0, K]} v_i^{\text{out}}$ and maximize circulation!
- **Step 4 — Complete Solution & Complexity**:
  Enumerate $K = 0 \dots N$ (do NOT binary search on $K$, as $\text{row}_i \le \frac{A}{B} T_{\text{total}}(K)$ is non-monotone in $K$!). For each $K$, find the maximum valid $T_{\text{total}}(K)$ and check $K \cdot B \le A \cdot T_{\text{total}}(K)$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Interpret a chip at $(i, j)$ as $1$ unit of flow from node $i$ to node $j$; then $\text{row}_i = \text{col}_i$ is simply flow conservation at node $i$!
  - *Hint 2*: Split node $i$ into $i_{\text{in}} \xrightarrow{[0, K]} i_{\text{out}}$ to cap $\text{row}_i = \text{col}_i \le K$, with `'C'` cells as $[1, 1]$ edges and `'.'` cells as $[0, 1]$ edges.
  - *Hint 3*: Loop over all $K \in \{0, \dots, N\}$, compute the maximum total flow $T_{\text{total}}(K)$, and check whether $K \le \lfloor A \cdot T_{\text{total}}(K) / B \rfloor$.

---

### P27 — `[Codeforces 611H]` New Year and Forgotten Tree (`[EN]`)
- **Judge URL**: [https://codeforces.com/problemset/problem/611/H](https://codeforces.com/problemset/problem/611/H)
- **Constraints**: $N \le 2 \times 10^5$ vertices labelled $1 \dots N$. We are given the count $c_{L_1, L_2}$ of tree edges whose endpoints have $L_1$ and $L_2$ decimal digits ($L_1, L_2 \in \{1, \dots, 6\}$). Reconstruct a valid tree or print `-1`.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Nodes with the same number of decimal digits $d \in \{1, \dots, D\}$ ($D \le 6$) are completely interchangeable! Partition $1 \dots N$ into $D \le 6$ digit-length groups $V_1, \dots, V_D$, and pick one **representative hub** $r_d \in V_d$ (e.g., $1, 10, 100, \dots$) per group.
- **Step 2 & 3 — Prüfer Hub-Tree Enumeration + Edge-Orientation Flow**:
  In any valid tree $T$, contracting each group $V_d$ or rooting $T$ shows we can select a spanning tree $T_{\text{hub}}$ on the $D$ hubs $\{r_1, \dots, r_D\}$ (one edge per pair of groups along the inter-group skeleton), and every **remaining** vertex $v \in V_d \setminus \{r_d\}$ must attach as a leaf (or directed parent edge) to some node in an adjacent group!
  - By Cayley's Formula, there are only $D^{D-2} \le 6^4 = 1296$ spanning trees $T_{\text{hub}}$ on the $D \le 6$ hubs!
  - For each fixed $T_{\text{hub}}$, subtract $1$ from $c_{u, v}$ for each edge $(u, v) \in T_{\text{hub}}$. Now the remaining $N - D$ non-hub vertices across groups $V_1, \dots, V_D$ must each receive **exactly $1$ parent edge** from the remaining $N - D$ edges in $c_{L_1, L_2}$!
  - Build a tiny bipartite network: Left = $\binom{D+1}{2} \le 21$ edge-type buckets $(L_1, L_2)$ (supply $c'_{L_1, L_2}$), Right = $D \le 6$ vertex groups (demand $|V_d| - 1$), with cross edges $(L_1, L_2) \to L_1$ and $(L_1, L_2) \to L_2$ of capacity $\infty$.
- **Step 4 — Complete Solution & Complexity**:
  At most $1296$ runs of Dinic on a $29$-vertex graph! Total time $< 50\text{ ms}$. Once a valid flow is found, assign each unit of flow on $(L_1, L_2) \to L_1$ by connecting a fresh node $v \in V_{L_1} \setminus \{r_{L_1}\}$ to hub $r_{L_2}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Group vertices by digit length $1 \dots D$ ($D \le 6$) and designate one hub vertex $r_d$ in each group.
  - *Hint 2*: Enumerate all $D^{D-2} \le 1296$ spanning trees on the $D$ hubs; once the hubs are connected, every remaining vertex $v \in V_d \setminus \{r_d\}$ just needs a directed edge to some hub!
  - *Hint 3*: Use Max-Flow on the $21$ edge-type pairs $(L_1, L_2)$ and $6$ groups $d$ to orient each remaining edge toward the group of the non-hub endpoint.

---

### P28 — `[AtCoder ABC 263 G]` Erasing Prime Sums (`[JA]`)
- **Judge URL**: [https://atcoder.jp/contests/abc263/tasks/abc263_g](https://atcoder.jp/contests/abc263/tasks/abc263_g)
- **Constraints**: $N \le 100$ distinct values $A_i \le 10^7$ with multiplicities $B_i \le 10^9$. Pair up elements whose sum $A_i + A_j$ is **prime** to maximize the total number of pairs erased.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Every prime $p > 2$ is **odd**, and the sum of two integers is odd iff one is **Even** and one is **Odd**! The **only** exception is $1 + 1 = 2$ (prime), which pairs two $1$'s with each other!
- **Step 2 & 3 — Algebraic Sensitivity of the $1 + 1 = 2$ Self-Loop**:
  Without $1 + 1 = 2$, the graph is purely bipartite between Even numbers $E$ and Odd numbers $O$:
  - Even $A_i \in E$: $S \xrightarrow{B_i} A_i$.
  - Odd $A_j \in O$: $A_j \xrightarrow{B_j} T$.
  - Cross edge $A_i \xrightarrow{\infty} A_j$ if $A_i + A_j$ is prime.
  What about the $B_1$ copies of $A_1 = 1$? Every copy of $1$ that is **not** matched with an Even number can be paired with another leftover $1$ (`ans += leftover_1 / 2`). Clearly we want to **minimize** the number of $1$'s used in the Even–Odd maximum matching while keeping the Even–Odd matching size as large as possible (since breaking two Even-$1$ pairs to form one $1+1$ pair never increases the total pairs, and breaking one Even-$1$ pair loses $1$ pair and gains at most $1$ pair!).
  Wait: how many $1$'s *must* be used to achieve the maximum Even–Odd matching $F_{\text{with-1}}$?
  1. Compute $F_{\text{with-1}} = \text{MaxFlow}(S, T)$ with $1$ included ($c(1 \to T) = B_1$).
  2. Compute $F_{\text{no-1}} = \text{MaxFlow}(S, T)$ with $1$ excluded ($c(1 \to T) = 0$).
  3. The minimum number of $1$'s required to reach $F_{\text{with-1}}$ is **exactly** $u_{\min} = F_{\text{with-1}} - F_{\text{no-1}}$!
  4. The remaining $B_1 - u_{\min}$ copies of $1$ pair with each other to form $\lfloor (B_1 - u_{\min}) / 2 \rfloor$ additional pairs!
- **Step 4 — Complete Solution & Complexity**:
  Total pairs $= F_{\text{with-1}} + \lfloor (B_1 - (F_{\text{with-1}} - F_{\text{no-1}})) / 2 \rfloor$. Two Dinic calls on $102$ vertices run in $< 5\text{ ms}$.
- **3-Tier Progressive Hints**:
  - *Hint 1*: Except for $1 + 1 = 2$, every prime sum pairs one Even number with one Odd number (a bipartite graph!).
  - *Hint 2*: Is it ever strictly better to break two $(A_{\text{even}}, 1)$ pairs just to make one $(1, 1)$ pair? No ($2 \ge 1$)!
  - *Hint 3*: Run Max-Flow once without $1$ ($F_{\text{no-1}}$) and once with $1$ ($F_{\text{with-1}}$); the minimum number of $1$'s needed in the bipartite matching is $u_{\min} = F_{\text{with-1}} - F_{\text{no-1}}$, leaving $\lfloor (B_1 - u_{\min})/2 \rfloor$ self-pairs of $1$.

---

### P29 — `[Codeforces 903G]` Yet Another MaxFlow Problem (`[EN]`)
- **Judge URL**: [https://codeforces.com/problemset/problem/903/G](https://codeforces.com/problemset/problem/903/G)
- **Constraints**: Two directed chains $A_1 \to A_2 \to \dots \to A_N$ (capacities $x_1, \dots, x_{N-1}$) and $B_1 \to B_2 \to \dots \to B_N$ (capacities $y_1, \dots, y_{N-1}$), plus $M$ cross edges $A_u \to B_v$ with capacity $z_e$ ($N, M, Q \le 2 \times 10^5$). Answer $Q$ queries that update $x_i$ and ask for $\text{MaxFlow}(A_1, B_N)$.
- **Step 1 — Non-Graph Diagnostic Signal (Direction B: Flow $\to$ Data Structure)**:
  With $N, M, Q = 2 \times 10^5$, running Dinic is completely impossible! We must switch to **Min-Cut Duality** and exploit the **directed chain topology**.
- **Step 2 & 3 — Prefix-Cut Dominance & Lazy Segment Tree Sweep**:
  Consider any $A_1$-$B_N$ cut $(S, V \setminus S)$.
  - If $A_{i+1} \in S$ while $A_i \notin S$, moving $A_{i+1} \dots$ out of $S$ (so $S \cap A = \{A_1, \dots, A_i\}$ is a **prefix** of chain $A$) never increases the cut on chain $A$ (since $A$-edges only point forward $A_k \to A_{k+1}$) and only shrinks the set of cut cross-edges $A_u \to B_v$!
  - Similarly, $T \cap B = \{B_{j+1}, \dots, B_N\}$ can be assumed to be a **suffix** of chain $B$ ($S \cap B = \{B_1, \dots, B_j\}$)!
  Therefore, every minimal cut is uniquely parameterized by a pair of split indices $(i, j) \in \{1, \dots, N\} \times \{0, \dots, N-1\}$ (where $x_N = y_0 = \infty$):
  $$\text{Cut}(i, j) = x_i + y_j + \sum_{\substack{e = (A_u \to B_v) \\ u \le i \;\land\; v > j}} z_e$$
  Define $f(i) = \min_{0 \le j < N} \left( y_j + \sum_{u \le i, v > j} z_e \right)$.Notice that $f(i)$ **does not depend on $x_1, \dots, x_{N-1}$ at all**!
  - **Precomputing $f(1), \dots, f(N)$ in $O((N + M) \log N)$**: Maintain a Lazy Segment Tree over $j \in \{0, \dots, N-1\}$ initialized to $T[j] = y_j$. Sweep $i$ from $1$ to $N$: for each cross edge $(A_i \to B_v, z_e)$, add $+z_e$ to the range $j \in [0, v - 1]$, then query $f(i) = \min_{0 \le j < N} T[j]$!
  - **Answering $Q$ Updates to $x_i$**: Maintain a global multiset or segment tree over $x_i + f(i)$ ($i = 1 \dots N$); each update to $x_i$ takes $O(\log N)$ time!
- **Step 4 — Complete Solution & Complexity**:
  $O((N + M + Q) \log N)$ total time ($\approx 250\text{ ms}$), zero flow algorithms run!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Because chain $A$ only has forward edges $A_i \to A_{i+1}$ and chain $B$ only has forward edges $B_j \to B_{j+1}$, any optimal cut cuts chain $A$ after some prefix $A_1 \dots A_i$ and cuts chain $B$ after some prefix $B_1 \dots B_j$.
  - *Hint 2*: Write the cut cost for pair $(i, j)$ as $x_i + y_j + \sum_{u \le i, v > j} z_e$, and notice that $\min_j (y_j + \sum_{u \le i, v > j} z_e)$ is independent of $x$!
  - *Hint 3*: Sweep $i = 1 \dots N$ using a range-add, range-min lazy segment tree over $j \in [0, N-1]$ to precompute $f(i)$, then maintain $\min_i (x_i + f(i))$.

---

### P30 — `[NOI2008 / Luogu P3980]` 志愿者招募 (Structural Lower-Bound Spine Equivalence) (`[ZH]`)
- **Judge URL**: [https://www.luogu.com.cn/problem/P3980](https://www.luogu.com.cn/problem/P3980)
- **Constraints**: $N \le 1000$ days (day $t$ requires at least $A_t$ volunteers), $M \le 10000$ volunteer types (type $i$ works across days $[S_i, T_i]$ at cost $C_i$ per person).
- **Step 1 — Non-Graph Diagnostic Signal (Bridging Wave 1A Lower-Bound Spine to Wave 2A Equation Differencing)**:
  Why is `[NOI2008] 志愿者招募` included at the climax of Wave 1A before we study Min-Cost Max-Flow in Wave 2A? Because it proves a **fundamental structural unification**: the **Lower-Bound Circulation Method (`上下界网络流`) on a line spine** and the **Consecutive Equation-Difference Method (`差分法` $E_t - E_{t-1}$)** construct the **exact same auxiliary graph $G'$ edge-for-edge**!
- **Step 2 & 3 — Algebraic Isomorphism Proof (Lower-Bound Spine $\equiv$ Consecutive Equation Differencing)**:
  Imagine an infinite supply of workers walking along the timeline spine $1 \to 2 \to \dots \to N \to N+1$:
  - On Day $t$ (edge $e_t = (t \to t+1)$), at least $A_t$ workers must be on duty, so $e_t$ has lower bound $l(e_t) = A_t$, upper bound $u(e_t) = \infty$, and cost $0$:
    $$t \xrightarrow{[A_t, \infty), \text{ cost } 0} t+1$$
  - Hiring $x_i$ volunteers of type $i = [S_i, T_i]$ means $x_i$ workers are **off-duty (bypassing the spine)** outside $[S_i, T_i]$ — or equivalently, hiring $x_i$ workers on $[S_i, T_i]$ allows $x_i$ units of flow on the spine segment $S_i \to \dots \to T_i + 1$ to return backward via a **return arc** $(T_i + 1 \to S_i)$ of $[0, \infty)$ and cost $C_i$!
  Now apply the standard **Section 6.1 Lower-Bound Compilation** to this spine $t \xrightarrow{[A_t, \infty)} t+1$ (defining $A_0 = A_{N+1} = 0$):
  1. The slack capacity of spine edge $t \to t+1$ is $\infty - A_t = \infty$ (cost $0$).
  2. What is the pre-injected baseline excess $M(t) = \text{in}_l(t) - \text{out}_l(t)$ at vertex $t \in \{1, \dots, N+1\}$?
     - The only edge with non-zero lower bound entering $t$ is $(t-1 \to t)$ with $l = A_{t-1}$.
     - The only edge with non-zero lower bound leaving $t$ is $(t \to t+1)$ with $l = A_t$.
     - Therefore:
       $$M(t) = A_{t-1} - A_t \qquad \forall t \in \{1, \dots, N+1\}!$$
  3. Notice that $M(t) = A_{t-1} - A_t$ is **literally the right-hand side of the consecutive difference equation $E_{t-1} - E_t$**, and connecting $S^* \to t$ when $A_{t-1} - A_t > 0$ and $t \to T^*$ when $A_{t-1} - A_t < 0$ produces the **exact same network** as Wave 2A's Consecutive Equation-Difference Method!
- **Step 4 — Complete Solution & Complexity**:
  Solved via Min-Cost Feasible Circulation on $G'$ ($N+3$ vertices, $N + M$ edges), bridging Wave 1A directly into Wave 2A!
- **3-Tier Progressive Hints**:
  - *Hint 1*: Model Day $t$'s demand as a lower-bound spine edge $t \xrightarrow{[A_t, \infty), \text{cost } 0} t+1$.
  - *Hint 2*: A volunteer working $[S_i, T_i]$ provides a return circulation arc $T_i + 1 \xrightarrow{[0, \infty), \text{cost } C_i} S_i$.
  - *Hint 3*: Compute $M(t) = \text{in}_l(t) - \text{out}_l(t) = A_{t-1} - A_t$: notice how Lower-Bound Circulation automatically derives the consecutive equation difference $A_{t-1} - A_t$!

---

## 9. Reconciled Quarantined Template Problems Table

In accordance with the Zero Boilerplate Mandate, pure naked solver verification problems are quarantined here so they do not dilute the modelling problem bank:

| Quarantine ID | Problem & Judge URL | Template Archetype Tested | Why Quarantined |
| :--- | :--- | :--- | :--- |
| **R-01** | `[Luogu P3376]` 【模板】网络最大流 | Naked Dinic / HLPP ($N \le 200, M \le 5000$) | Zero modelling; raw solver syntax verification. |
| **R-02** | `[LOJ #127]` 最大流 加强版 | Naked HLPP / Scaling ($N \le 1200, M \le 1.2 \times 10^5$) | Pure $O(V^2\sqrt{E})$ constant-factor benchmark. |
| **R-03** | `[CSES 1694]` Download Speed | Naked Max-Flow ($N \le 500, M \le 1000$) | Direct translation of English "pipes" to capacity. |
| **R-04** | `[CSES 1695]` Police Chase | Naked Min-Cut Edge Extraction ($N \le 500$) | Direct $S_{\min}$ BFS cut-edge printing. |
| **R-05** | `[LOJ #115]` 无源汇有上下界可行流 | Naked Lower-Bound Variant 1 | Raw verification of $M(v)$ and `dinic(S*, T*)`. |
| **R-06** | `[LOJ #116]` 有源汇有上下界最大流 | Naked Lower-Bound Variant 3 | Raw verification of $f_0 + \text{dinic}(s, t)$. |
| **R-07** | `[LOJ #117]` 有源汇有上下界最小流 | Naked Lower-Bound Variant 4 | Raw verification of $f_0 - \text{dinic}(t, s)$. |
| **R-08** | `[AtCoder ACL Practice D]` Maxflow | Naked Unit Bipartite Grid Matching | Pure ACL `mf_graph` API test. |
| **R-09** | `[POJ 1273 / USACO 4.2]` Drainage Ditches | Naked Max-Flow with Parallel Edges | Historical introductory template. |
| **R-10** | `[Luogu P2756]` 飞行员配对方案问题 | Naked Bipartite Matching (`网络流 24 题`) | Textbook bipartite matching with edge printing. |
| **R-11** | `[Luogu P2764]` 最小路径覆盖问题 | Naked DAG Disjoint Path Cover (`网络流 24 题`) | Deferred to Wave 1B (Dilworth & Path Cover). |

---

## 10. Unified Multilingual Bibliography (`[EN]` / `[ZH]` / `[JA]`)

### `[EN]` English Foundational Papers & Textbooks
1. **Ford, L. R., & Fulkerson, D. R. (1956)**. *Maximal flow through a network*. Canadian Journal of Mathematics, 8, 399–404. (Max-Flow Min-Cut Theorem, Integrality, and Path–Cycle Decomposition.)
2. **Ford, L. R., & Fulkerson, D. R. (1962)**. *Flows in Networks*. Princeton University Press.
3. **Dinic, E. A. (1970)**. *Algorithm for solution of a problem of maximum flow in a network with power estimation*. Soviet Mathematics Doklady, 11, 1277–1280. (Level graphs, blocking flows, and $O(V^2 E)$ bound.)
4. **Edmonds, J., & Karp, R. M. (1972)**. *Theoretical improvements in algorithmic efficiency for network flow problems*. Journal of the ACM, 19(2), 248–264. (Shortest augmenting path $O(VE^2)$ and capacity scaling $O(E^2 \log U)$.)
5. **Karzanov, A. V. (1973)**. *On finding maximum flows in networks with special structure and some applications*. Matematicheskie Voprosy Upravleniya Proizvodstvom, 5, 81–94. (Unit-network $O(E^{3/2})$, $O(V^{2/3}E)$, and $O(E\sqrt{V})$ bounds.)
6. **Even, S., & Tarjan, R. E. (1975)**. *Network flow and testing graph connectivity*. SIAM Journal on Computing, 4(4), 507–518. (Popularization of unit-network bounds and Menger connectivity complexities.)
7. **Zadeh, N. (1973)**. *A bad network problem for the simplex method and other minimum cost flow algorithms*. Mathematical Programming, 5(1), 255–266. (Adversarial worst-case graphs for augmenting-path algorithms.)
8. **Zwick, U. (1995)**. *The smallest networks on which the Ford-Fulkerson maximum flow procedure may fail to terminate*. Theoretical Computer Science, 148(1), 165–170. (6-vertex golden-ratio irrational network.)
9. **Goldberg, A. V., & Tarjan, R. E. (1988)**. *A new approach to the maximum-flow problem*. Journal of the ACM, 35(4), 921–940. (Preflow-Push framework and HLPP.)
10. **Cheriyan, J., & Maheshwari, S. N. (1989)**. *Analysis of preflow push algorithms for maximum network flow*. SIAM Journal on Computing, 18(6), 1057–1086. (Tight $O(V^2\sqrt{E})$ bound for HLPP.)
11. **Goldberg, A. V., & Rao, S. (1998)**. *Beyond the flow decomposition barrier*. Journal of the ACM, 45(5), 783–797. (Binary blocking flow $O(\min(V^{2/3}, E^{1/2})E \log(V^2/E) \log U)$.)
12. **Picard, J. C., & Queyranne, M. (1980)**. *On the structure of all minimum cuts in a network and applications*. Mathematical Programming Study, 13, 8–16. (Distributive lattice $\mathcal{L}_{\min}$ and Residual Condensation DAG.)
13. **Hoffman, A. J. (1960)**. *Some recent applications of the theory of linear inequalities to extremal combinatorial analysis*. Proceedings of Symposia in Applied Mathematics, 10, 113–127. (Hoffman's Circulation Theorem.)
14. **Horn, W. A. (1974)**. *Some simple scheduling algorithms*. Naval Research Logistics Quarterly, 21(1), 177–185; **McNaughton, R. (1959)**, *Scheduling with deadlines and loss functions*, Management Science, 6(1), 1–12.
15. **Okamura, H., & Seymour, P. D. (1981)**. *Multicommodity flows in planar graphs*. Journal of Combinatorial Theory, Series B, 31(1), 75–81. (Two-commodity swap/superposition principle used in `[CQOI2014] 危桥`.)
16. **Ahuja, R. K., Magnanti, T. L., & Orlin, J. B. (1993)**. *Network Flows: Theory, Algorithms, and Applications*. Prentice Hall.

### `[ZH]` Chinese Competitive Programming Literature (`国家集训队论文` & Classic Treatises)
17. **Amber / 胡伯涛 (2007)**. 《最小割模型在信息学竞赛中的应用》 (*Applications of Minimum Cut Models in Olympiad in Informatics*). 2007 年信息学奥林匹克中国国家集训队论文. (Foundational Chinese treatise on cut algebra, submodularity, and extreme cut properties.)
18. **周冬 (Zhou Dong, 2008)**. 《浅析最大最小定理在信息学竞赛中的应用》. 2008 年中国国家集训队论文. (Flow-cut duality, Menger's theorems, and capacity sensitivity.)
19. **刘汝佳 (Liu Rujia) & 陈锋 (Chen Feng)**. 《算法竞赛入门经典：训练指南》 (*AOAPC II: Training Guide*). 清华大学出版社. (Systematic treatment of `上下界网络流` Variants 1–4, Eulerian orientations, and `[NOI2008] 志愿者招募`.)
20. **OI-Wiki Contributors**. 《网络流 / 上下界网络流 / 最小割》 ([https://oi-wiki.org/graph/flow/](https://oi-wiki.org/graph/flow/)). (Standardized terminology for `可行边/必须边`, `动态加层`, and `退流`.)

### `[JA]` Japanese Competitive Programming Treatises (`AtCoder` / `Kyopro` Ecosystem)
21. **snuke (Takanori Maehara) & Miura, T.** *Flow Algorithms and Graph Cuts in Competitive Programming* (`AtCoder Library (ACL) mf_graph` design notes).
22. **maspy (`maspypy.com`)**. *最大流・最小カットの基礎と応用 (Foundations and Applications of Max-Flow and Min-Cut)* & *最小流量制限付き最大流 (Flows with Lower Bounds / Demands)*.
23. **noshi91 (`noshi91.hatenablog.com`)**. *フロー・カット周りの双対性と格子構造 (Duality and Lattice Structure around Flows and Cuts)*.
24. **tatyam (`tatyam.github.io`)**. *Dinic 法の計算量解析 (Complexity Analysis of Dinic's Algorithm on Special Graphs)*.

---

## 11. Worked End-to-End Numerical Traces & Counterexample Atlas

To ensure every structural invariant in Sections 2–7 is concrete and hand-verifiable, we provide three complete step-by-step numerical traces.

### 11.1 Worked Trace 1: Picard–Queyranne Residual Condensation DAG & `[AHOI2009]` Edge Classification

Consider the 6-vertex directed network $G = (V, E, c)$ with $V = \{s, u_1, u_2, v_1, v_2, t\}$ and 7 physical edges:
- $e_1 = (s \to u_1, c = 3)$, $e_2 = (u_1 \to u_2, c = 3)$, $e_3 = (u_2 \to t, c = 3)$ (Upper 3-edge chain of bottleneck 3).
- $e_4 = (s \to v_1, c = 2)$, $e_5 = (v_1 \to v_2, c = 4)$, $e_6 = (v_2 \to t, c = 2)$ (Lower 3-edge chain with middle capacity 4 and endpoint capacities 2).
- $e_7 = (u_1 \to v_2, c = 1)$ (Cross-chord from upper chain to lower chain).

#### Step 1: Maximum Flow $f^*$ and Residual Network $G_{f^*}$
Push $3$ units along $s \to u_1 \to u_2 \to t$ and $2$ units along $s \to v_1 \to v_2 \to t$, for a total maximum flow of $|f^*| = 5$. Let us inspect the residual capacities $(c_{f^*}(e), c_{f^*}(e^{\text{rev}}))$ of all 7 edges in $G_{f^*}$:

| Edge $e_k = (x \to y)$ | Physical Cap $c(e_k)$ | Flow $f^*(e_k)$ | Forward Residual $c_{f^*}(x \to y)$ | Reverse Residual $c_{f^*}(y \to x)$ | Saturated ($f^* == c$)? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $e_1 = (s \to u_1)$ | $3$ | $3$ | $0$ | $3$ ($u_1 \to s$) | **Yes** |
| $e_2 = (u_1 \to u_2)$ | $3$ | $3$ | $0$ | $3$ ($u_2 \to u_1$) | **Yes** |
| $e_3 = (u_2 \to t)$ | $3$ | $3$ | $0$ | $3$ ($t \to u_2$) | **Yes** |
| $e_4 = (s \to v_1)$ | $2$ | $2$ | $0$ | $2$ ($v_1 \to s$) | **Yes** |
| $e_5 = (v_1 \to v_2)$ | $4$ | $2$ | $2$ ($v_1 \to v_2$) | $2$ ($v_2 \to v_1$) | **No** |
| $e_6 = (v_2 \to t)$ | $2$ | $2$ | $0$ | $2$ ($t \to v_2$) | **Yes** |
| $e_7 = (u_1 \to v_2)$ | $1$ | $0$ | $1$ ($u_1 \to v_2$) | $0$ | **No** |

#### Step 2: Tarjan SCCs in $G_{f^*}$ and Minimum-Cut Lattice $\mathcal{L}_{\min}$
Wait: look closely at the cycle formed in $G_{f^*}$ by the unsaturated cross-chord $e_7 = (u_1 \to v_2)$!
- In $G_{f^*}$, we have the forward residual arcs $u_1 \xrightarrow{e_7} v_2$ (cap 1) and $v_1 \xrightarrow{e_5} v_2$ (cap 2), AND the reverse residual arcs $v_2 \xrightarrow{e_5^{\text{rev}}} v_1$ (cap 2) and $v_1 \xrightarrow{e_4^{\text{rev}}} s$ (cap 2), while $u_1 \xrightarrow{e_1^{\text{rev}}} s$ (cap 3).
- Does $s$ reach $u_1$? No ($c_{f^*}(s \to u_1) = 0$ and $c_{f^*}(s \to v_1) = 0$). Thus $\text{SCC}(s) = \{s\}$, and the **source-minimal cut is $S_{\min} = \{s\}$** (cutting $e_1, e_4$ with capacity $3 + 2 = 5$).
- What about $\{v_1, v_2\}$? Since $v_1 \to v_2$ (cap 2) and $v_2 \to v_1$ (cap 2) both exist in $G_{f^*}$, $v_1$ and $v_2$ merge into a single strongly connected component $\text{SCC}(v_1) = \text{SCC}(v_2) = \{v_1, v_2\}$!
- What about $u_1$? In $G_{f^*}$, $u_1 \to v_2 \to v_1 \to s$, so any out-closed ideal $S \in \mathcal{L}_{\min}$ containing $u_1$ **must also contain $\{v_1, v_2, s\}$**!
- The complete distributive lattice $\mathcal{L}_{\min}$ consists of **4 minimum cuts** (each of capacity $5$):
  1. $S_1 = S_{\min} = \{s\}$ — cuts $\{e_1, e_4\}$ ($3 + 2 = 5$).
  2. $S_2 = \{s, v_1, v_2\}$ — cuts $\{e_1, e_6\}$ ($3 + 2 = 5$).
  3. $S_3 = \{s, u_1, v_1, v_2\}$ — cuts $\{e_2, e_6\}$ ($3 + 2 = 5$). (Notice why $u_1$ could only join $S$ *after* $v_2$ was already in $S$: if $u_1 \in S$ and $v_2 \notin S$, then $e_7 = (u_1 \to v_2)$ would also be cut, raising the cut capacity to $3 + 2 + 1 = 6 > 5$!)
  4. $S_4 = S_{\max} = \{s, u_1, u_2, v_1, v_2\}$ — cuts $\{e_3, e_6\}$ ($3 + 2 = 5$).
- **Classification Verdict (Theorem 4.5)**:
  - **Feasible Cut Edges (`可行边`)**: $e_1, e_2, e_3, e_4, e_6$ (all 5 saturated edges, since each connects distinct SCCs in $G_{f^*}$).
  - **Essential Cut Edges (`必须边`)**: **None!** Because $\text{SCC}(s) = \{s\}$ and $\text{SCC}(t) = \{t\}$, an essential edge would need to go directly from $\{s\}$ to $\{t\}$, which none of $e_1 \dots e_6$ do! Indeed, $S_1 \cap S_4$ cuts no common edges ($\{e_1, e_4\} \cap \{e_3, e_6\} = \emptyset$).

---

### 11.2 Worked Trace 2: Complete 2-Phase Execution of Variant 3 (`有源汇上下界最大流`) & Variant 4 (`最小流`)

Consider a 4-vertex network $V = \{s, a, b, t\}$ with 5 lower-and-upper-bounded directed edges:
- $e_1 = (s \to a)$ with $[l, u] = [2, 5]$
- $e_2 = (s \to b)$ with $[l, u] = [1, 4]$
- $e_3 = (a \to b)$ with $[l, u] = [1, 3]$
- $e_4 = (a \to t)$ with $[l, u] = [1, 4]$
- $e_5 = (b \to t)$ with $[l, u] = [2, 6]$

#### Step 1: Pre-Injected Excess $M(v) = \text{in}_l(v) - \text{out}_l(v)$ and Auxiliary Graph $G'$
Add feedback arc $e_{\text{fb}} = (t \to s)$ with $[0, \infty)$. Compute $M(v)$ from the lower bounds $l = (2, 1, 1, 1, 2, 0)$:
- $M(s) = \text{in}_l(s) - \text{out}_l(s) = 0 - (2 + 1) = -3 < 0 \implies$ add companion arc $s \to T^*$ with capacity $3$.
- $M(a) = \text{in}_l(a) - \text{out}_l(a) = 2 - (1 + 1) = 0 \implies$ no companion arc.
- $M(b) = \text{in}_l(b) - \text{out}_l(b) = (1 + 1) - 2 = 0 \implies$ no companion arc.
- $M(t) = \text{in}_l(t) - \text{out}_l(t) = (1 + 2) - 0 = +3 > 0 \implies$ add companion arc $S^* \to t$ with capacity $3$.
- Total positive imbalance: $\Sigma^+ = 3$.
- Slack capacities $u(e) - l(e)$: $e_1: 3, \; e_2: 3, \; e_3: 2, \; e_4: 3, \; e_5: 4, \; e_{\text{fb}}: \infty$.

#### Step 2: Phase 1 (`dinic(S*, T*)` Feasibility)
In $G'$, `dinic(S*, T*)` pushes $3$ units of flow along the 3-hop path:
$$S^* \xrightarrow{3} t \xrightarrow{e_{\text{fb}} \text{ (cap } \infty)} s \xrightarrow{3} T^*$$
Since $F_1 = 3 == \Sigma^+$, the network is **feasible**!
- The baseline feasible $s$-$t$ flow value is $f_0 = \tilde{f}(e_{\text{fb}}) = 3$, corresponding to physical edge flows $f^{(0)} = l + \tilde{f} = (2, 1, 1, 1, 2)$.
- Now **zero out both half-edges of $e_{\text{fb}}$**: `cap[e_fb] = cap[e_fb ^ 1] = 0`.

#### Step 3: Phase 2A — Maximum Flow (`dinic(s, t)`) vs. Phase 2B — Minimum Flow (`dinic(t, s)`)
- **For Variant 3 (Maximum Flow)**: Starting from $f^{(0)} = (2, 1, 1, 1, 2)$ ($f_0 = 3$), the remaining forward slack capacities are $\tilde{c}(e_1)=3, \tilde{c}(e_2)=3, \tilde{c}(e_3)=2, \tilde{c}(e_4)=3, \tilde{c}(e_5)=4$. Running `dinic(s, t)` pushes:
  - $3$ units along $s \xrightarrow{e_1} a \xrightarrow{e_4} t$, and
  - $3$ units along $s \xrightarrow{e_2} b \xrightarrow{e_5} t$,
  giving $f_{\text{add}} = 6$. Thus **$|f_{\max}| = f_0 + f_{\text{add}} = 3 + 6 = 9$**, with physical flows $f^* = (5, 4, 1, 4, 5)$.
- **For Variant 4 (Minimum Flow)**: Starting from $f^{(0)} = (2, 1, 1, 1, 2)$ ($f_0 = 3$), all reverse slack capacities $\tilde{f}(e_1) \dots \tilde{f}(e_5)$ are currently $0$, so `dinic(t, s)` pushes $f_{\text{sub}} = 0$, confirming **$|f_{\min}| = 3 - 0 = 3$**. (Had Phase 1 routed excess slack through interior edges, `dinic(t, s)` would peel that excess back to $3$.)

---

### 11.3 Worked Trace 3: Extracting a Hoffman Violation Certificate When Phase 1 Fails

Suppose in the network of Section 11.2 we tighten the upper bound of $e_4 = (a \to t)$ from $4$ down to $1$ ($[l_4, u_4] = [1, 1]$), and raise the lower bound of $e_1 = (s \to a)$ from $2$ up to $4$ ($[l_1, u_1] = [4, 5]$), while keeping $e_3 = (a \to b)$ at $[1, 2]$.
- Look at vertex $a$: incoming lower bound is $\text{in}_l(a) = l(s \to a) = 4$, while maximum possible outgoing capacity is $u(a \to b) + u(a \to t) = 2 + 1 = 3 < 4$!
- Let us see how Theorem 7.2 automatically discovers the witness subset $A^* = \{a\}$ from $G'$:
  1. In $G'$, $M(a) = \text{in}_l(a) - \text{out}_l(a) = 4 - (1 + 1) = +2 > 0$, so $S^* \to a$ gets capacity $2$; $M(t) = +3 \implies S^* \to t$ gets capacity $3$; $\Sigma^+ = 2 + 3 = 5$.
  2. The slack capacities leaving $a$ are $u(e_3) - l(e_3) = 2 - 1 = 1$ ($a \to b$) and $u(e_4) - l(e_4) = 1 - 1 = 0$ ($a \to t$).
  3. When `dinic(S*, T*)` runs on $G'$, all $3$ units from $S^* \to t$ reach $T^*$ via $t \to s \to T^*$, and $1$ unit from $S^* \to a$ reaches $T^*$ via $a \xrightarrow{e_3} b \xrightarrow{e_5} t \xrightarrow{e_{\text{fb}}} s \to T^*$. Total flow is $F_1 = 4 < \Sigma^+ = 5$!
  4. In the final residual network $G'_{f^*}$, the arc $S^* \to a$ still has $2 - 1 = 1$ unit of residual capacity, while all arcs leaving $a$ are saturated ($c_{f^*}(a \to b) = 0, c_{f^*}(a \to t) = 0$).
  5. Therefore, forward BFS from $S^*$ in $G'_{f^*}$ visits $S_{\min}^* = \{S^*, a\}$, isolating the exact **Hoffman Violation Witness**:
     $$A^* = S_{\min}^* \setminus \{S^*\} = \{a\}$$
     with Hoffman violation $\sum_{e \in \delta^-(A^*)} l(e) - \sum_{e \in \delta^+(A^*)} u(e) = l(s \to a) - \big(u(a \to b) + u(a \to t)\big) = 4 - (2 + 1) = 1 = \Sigma^+ - F_1$!
