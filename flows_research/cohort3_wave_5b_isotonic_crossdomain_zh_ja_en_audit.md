# Cohort 3 Wave 5B Master Reconciliation Monograph (Iterations 46–52 & 98–104 / Iteration 114): $L_p$ Isotonic Regression (`保序回归`), Cross-Domain Reductions, Continuous-Discrete Total Variation Duality, and Exhaustive Tri-Lingual (`[ZH]` / `[JA]` / `[EN]`) Literature & Problem Archive Audit

**Document Role**: Definitive Cohort 3 Master Reconciliation Monograph for Wave 5B (synthesizing and auditing Cohort 1 `flows_research/iter_46_to_52_isotonic_crossdomain_zh_ja_en_audit.md` and Cohort 2 `flows_research/cohort2_iter_98_to_104_isotonic_crossdomain_zh_ja_en_audit.md`).
**Pedagogical Contract**: Strict enforcement of the **4-Step "Zero Magic Gadgets" Compilation Mandate** (Step 1: Non-Graph Diagnostic Signal $\to$ Step 2: Intermediate Algebraic/Logical Representation $\to$ Step 3: Mechanical Graph Compilation Scratchpad $\to$ Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexamples) and the **No Boilerplate Library Code Mandate**.

---

## 1. Cross-Cohort Blind-Spot Audit & Reconciliation Matrix

A rigorous side-by-side audit of Cohort 1 (`iter_46_to_52`, 1,400 lines / 178 KB) and Cohort 2 (`cohort2_iter_98_to_104`, 1,411 lines / 183 KB) revealed that each cohort captured crucial structural theorems, subtle edge-case traps, and contest problems that the other omitted or glossed over. This section catalogs every theoretical blind-spot, notation discrepancy, and problem-bank divergence resolved in this unified Cohort 3 monograph.

### 1.1 Theoretical & Modelling Blind-Spot Matrix

| Iteration / Topic | Cohort 1 (`iter_46_to_52`) Strengths & Exclusive Contributions | Cohort 2 (`cohort2_iter_98_to_104`) Strengths & Exclusive Contributions | Cohort 3 Reconciliation & Gap-Hunting Resolution |
| :--- | :--- | :--- | :--- |
| **Iter 46 vs. 98: $L_p$ Isotonic Regression (`保序回归`)** | 1. Derived the **$L_\infty$ Difference-Constraint Specialization** ($O((N+M)\log U)$ via binary search + longest path on DAG without Max-Flow).<br>2. Formulated exact rational block averaging $f^*_C = \frac{\sum_{v \in C} w_v y_v}{\sum_{v \in C} w_v}$ for continuous $L_2$ before rounding.<br>3. Contrasted 1D Chain $L_1$ Isotonic Regression via Leftist Heap / Slope Trick (`[BOI2004] Sequence`, $O(N \log N)$) against general DAG `整体二分`.<br>*Blind-spot*: Mislabelled Luogu ID of `[省选联考 2020 A 卷] 魔法商店` (`P6621` / `LOJ 3303`) as `P6624` (`作业题`), and omitted Preorder SCC contraction. | 1. Proved **Preorder SCC Contraction Lemma**: cycles $v_1 \preceq \dots \preceq v_k \preceq v_1$ force $f(v_1)=\dots=f(v_k)$ and contract to a single super-vertex with convex cost $\Phi_C(x) = \sum_{v \in C} w_v \phi_v(x)$.<br>2. Proved the **Two-Point Threshold Contraction Theorem** via the clean unit-step potential $\Psi(f^*)$ minimality argument.<br>3. Highlighted the **$O(N^2)$ Dinic `head[]` Clearing Trap** when failing to re-index $V_{\text{sub}}$ locally.<br>*Blind-spot*: Omitted $L_\infty$ difference-constraint bypass and 1D PAVA / Slope Trick contrast. | **Synthesized in §2**: Unifies Preorder SCC Contraction, both complementary proofs of the Two-Point Threshold Contraction Theorem (Strict Convexity Midpoint Shift + Unit-Step Potential $\Psi(f^*)$), exact $L_1 / L_2 / L_\infty$ specializations, 1D Slope Trick vs. DAG `整体二分` boundary, local re-indexing invariant, and corrects Judge IDs (`Luogu P6621 / LOJ 3303` for `魔法商店` vs. Gao Ruiquan's 2018 general $L_p$ Isotonic Regression framework). |
| **Iter 47 vs. 99: Combinatorial Games & DM Decomposition** | 1. Clean 2-player strategy-stealing proof for fixed-start alternating walk games.<br>2. Full compilation of `ARC 074 F (Lotus Leaves)` Row/Column Hub virtualization.<br>3. Explicit constructive vertex-cut recovery trap in `ABC 239 G` ($v_{\text{in}} \in R_S \land v_{\text{out}} \notin R_S$ vs. saturated edge fallacy).<br>*Blind-spot*: Missed `[SCOI2012] 奇怪的游戏` chessboard parity invariant and conflated the two turn-order variants of `[JSOI2009] 游戏`. | 1. Explicit **Turn-Order Polarity Table** distinguishing **Variant A** (Player 1 places token at $v_0$, Player 2 moves first $\implies$ P1 wins iff $v_0$ is **NOT** in every max matching, i.e., $v_0 \in \mathcal{E}$) vs. **Variant B** (token starts at $v_0$, Player 1 moves first $\implies$ P1 wins iff $v_0$ **IS** in every max matching, i.e., $v_0 \notin \mathcal{E}$).<br>2. Full derivation of `[SCOI2012] 奇怪的游戏` (`Luogu P5038`) parity invariant ($N \cdot M$ odd fixes unique $X$; $N \cdot M$ even uses domino-tiling monotonicity).<br>3. Variable-payoff Hide-and-Seek capacity scaling $1/c_{r,c}$. | **Synthesized in §3**: Integrates the Turn-Order Polarity Theorem and Dulmage–Mendelsohn $(\mathcal{E}, \mathcal{O}, \mathcal{U})$ reachability certificate, `[SCOI2012] 奇怪的游戏` parity split, variable-payoff Von Neumann Minimax LP duality, and `ARC 074 F` / `ABC 239 G` barrier cuts with constructive residual reachability recovery. |
| **Iter 48 vs. 100: Computational Geometry** | 1. Planar Euler characteristic derivation ($F - C$ invariant) of Imai–Asano rectilinear polygon partitioning.<br>2. **Minkowski Sum Inflation** ($R'_i = R_i \oplus B_r$) for finite-radius moving objects in `[BOI 2002] Escape`.<br>3. `CF 1404 E (Bricks)` shared-border dual bipartite MIS.<br>*Blind-spot*: Used $+h$ without reconciling why standard papers write $1 - h + c_{\text{conc}} - |I^*|$ vs. $\frac{N}{2} - 1 + h - |I^*|$. | 1. Proved the **Topological Reflex–Convex Identity** $c_{\text{conv}} - c_{\text{conc}} = 4 - 4h \iff c_{\text{conc}} = \frac{N}{2} - 2 + 2h$ and the **$90^\circ$ Corner Double-Counting Proof** ($4R = c_{\text{conv}} + c_{\text{conc}} + 2k$).<br>2. Explicitly resolved the famous $\pm h$ sign discrepancy in literature.<br>*Blind-spot*: Omitted Minkowski Sum inflation for finite-radius objects in barrier cuts. | **Synthesized in §4**: Provides both the Euler Characteristic ($F-C$) proof and the $90^\circ$ Corner Double-Counting proof side-by-side, proving $R_{\min} = 1 - h + c_{\text{conc}} - |I^*| = \frac{N}{2} - 1 + h - |I^*|$, plus the Endpoint-Sharing Non-Disjointness Trap, `CF 1404 E` Dual Border MIS, and Minkowski-inflated continuous-to-discrete barrier cuts. |
| **Iter 49 vs. 101: Strings, Matroids & Number Theory** | 1. Stated and proved the **Bruhat–Hall Strong Basis Bijection Theorem** ($G_{\text{ex}}(B_1, B_2)$ always admits a perfect matching via matroid rank submodularity).<br>2. Proved why minimal vertex covers on transitively closed DAGs never select both $u_L$ and $u_R$ in `ABC 354 G`.<br>3. Included `CF 498 C (Array and Operations)` prime-wise decoupling.<br>*Blind-spot*: Omitted the sparse-DAG $u_R \xrightarrow{\infty} u_L$ bypass gadget and `AGC 025 D` Gaussian Integer 2-adic bipartition. | 1. Derived the **Sparse-DAG Bypass Gadget $u_R \xrightarrow{\infty} u_L$** for Weighted Dilworth Antichain (`ABC 354 G`), which enforces transitivity and prevents double-cutting $u_L, u_R$ without full $O(N^2)$ edge materialization.<br>2. Contrasted `[SHOI2004] 最小生成树` ($L_1$ LP Dual $\to$ Bipartite MCMF) against `[BJWC2018] 最小生成树` ($L_2$ $\to$ Isotonic Regression).<br>3. Full 2-adic Gaussian Integer factorization proof for `AGC 025 D (Choosing Points)`. | **Synthesized in §5**: Unifies the Aho–Corasick Compressed-Link Jump Table (`CF 590 E`), both `ABC 354 G` formulations (Transitive Closure vs. $u_R \xrightarrow{\infty} u_L$ Bypass Gadget), Bruhat–Hall Strong Basis Bijection, $L_1$ vs. $L_2$ Inverse MST, and the 4-way Number-Theoretic Graph taxonomy (`ARC 085 E`, `[SDOI2016] 数字配对`, `AGC 025 D`, `CF 498 C`). |
| **Iter 50–52 vs. 102–104: Tri-Lingual Archive Audit** | 1. Cataloged `网络流 24 题`, Chinese National Team papers, Japanese `燃やす埋める` ecosystem (`noshi91`, `maspypy`, `tatyam`), and English archives.<br>*Blind-spot*: Slight LOJ ID numbering shift on `#17/#21/#22/#23/#24`; missed that `#24 猴子上树 (Luogu P2769)` is a 4th non-flow DP problem in the 24-problem suite. | 1. Exact `LOJ 6000–6023` canonical indexing, flagging **all 4 non-flow traps** (`#10 软件补丁`, `#17 孤岛营救`, `#22 汽车加油行驶`, and `#24 猴子上树` $O(NM)$ DP) plus the $L=1$ infinite-flow trap in `#06 最长不下降子序列`.<br>2. Included `CF 1517 G`, `CF 1783 F`, `AGC 029 F`, `ARC 107 F`, `ARC 142 E`. | **Synthesized in §6**: Complete reconciled `LOJ 6000–6023` master table with all 4 non-flow anomalies and degenerate traps documented, plus expanded `[ZH]`, `[JA]`, and `[EN]` archive tables. |
| **Cohort 3 Targeted Gap-Hunting (§7)** | Mentioned discrete Coarea formula (`CF 1427 G`) and planar duals (`[NOI2010] 海拔`) separately. | Mentioned discrete Coarea formula (`CF 1427 G`, `ABC 347 G`) separately. | **New in §7**: Establishes the unified **Continuous Max-Flow / Min-Cut on Euclidean Domains & Total Variation (`Rudin–Osher–Fatemi TV Denoising` & Strang's Continuous Max-Flow $\leftrightarrow$ Discrete Grid Cuts + Coarea Formula + $L_p$ Isotonic Regression)** bridge. |

---

### 1.2 Practice Problem Cross-Cohort Deduplication & Tier Audit (32 Unified Problems)

Combining Cohort 1's 22 problems (`P01–P22`) and Cohort 2's 22 problems (`P01–P22`) yields 12 shared core problems and 20 cohort-exclusive problems, totaling **32 unique, non-template problems** organized across 4 pedagogical tiers in **Section 8**:

| Unified ID | Problem Name & Judge Coordinates | Cohort 1 ID | Cohort 2 ID | Assigned Tier & Core Structural Mechanism |
| :--- | :--- | :---: | :---: | :--- |
| **P01** | `CF 498 C (Array and Operations)` | `P01` | — | **Stepping Stone**: Prime-Wise Independent Bipartite Max-Flow |
| **P02** | `ARC 074 F (Lotus Leaves)` | `P02` | `P01` | **Stepping Stone**: Row/Column Hub Virtualization & Bipartite Vertex Min-Cut |
| **P03** | `ARC 085 E (MUL)` | `P03` | `P02` | **Stepping Stone**: Complimentary Gain Transformation & Divisor Closure (`燃やす埋める`) |
| **P04** | `ABC 239 G (Builder Takahashi)` | `P04` | `P03` | **Stepping Stone**: Vertex-Split Min-Cut & Residual Reachability Recovery |
| **P05** | `ICPC WF 2017 C (Mission Improbable)` | `P05` | `P04` | **Stepping Stone**: 3D Grid Cross-Intersection Bipartite Matching |
| **P06** | `CF 1783 F (Double Sort II)` | — | `P05` | **Stepping Stone**: Permutation Cycle Cover Intersection via Bipartite Matching |
| **P07** | `LOJ 6007 / Luogu P2774 (方格取数问题)` | `P06` | — | **Stepping Stone**: Grid Parity Bipartition & Complement Minimum Vertex Cover |
| **P08** | `LOJ 6019 / Luogu P3355 (骑士共存问题)` | — | `P06` | **Stepping Stone**: Knight-Graph Color-Parity Bipartition & MWIS |
| **P09** | `[JSOI2009] 游戏 (Luogu P4055)` | `P07` | `P07` | **Intermediate**: Bipartite Walk Game & Dulmage–Mendelsohn $\mathcal{E}$-Set Polarity |
| **P10** | `[SCOI2012] 奇怪的游戏 (Luogu P5038)` | — | `P08` | **Intermediate**: Chessboard Parity Invariant + Binary Search & Domino Feasibility |
| **P11** | `CF 1404 E (Bricks)` | `P08` | `P09` | **Intermediate**: Dual Shared-Border Unit-Segment Cover & Corner Conflict MIS |
| **P12** | `[BOI 2002] Escape (Luogu P1345 / P5039)` | `P09` | — | **Intermediate**: Minkowski-Inflated Obstacle Intersection Graph & Vertex-Split Cut |
| **P13** | `ABC 354 G (Select Strings)` | `P10` | `P10` | **Intermediate**: Substring Poset Weighted Dilworth Antichain & $u_R \to u_L$ Bypass |
| **P14** | `[SDOI2016] 数字配对 (Luogu P4068)` | `P11` | `P11` | **Intermediate**: Prime-Omega $\Omega(a_i) \bmod 2$ Bipartition & Positive-Cost Stopping MCMF |
| **P15** | `AGC 025 D (Choosing Points)` | — | `P12` | **Intermediate**: Gaussian Integer 2-Adic Valuation Bipartition & Product 4-Coloring |
| **P16** | `[BJOI2018] 智力竞赛 (Luogu P4589)` | `P12` | — | **Intermediate**: Binary Search on Min Excluded Value + Weighted/Bounded Dilworth Chain Cover |
| **P17** | `CF 590 E (Birthday)` | `P13` | `P13` | **Advanced**: Aho–Corasick Compressed-Link Jump Table + Dilworth Kőnig Recovery |
| **P18** | `[SHOI2004] 最小生成树 (Luogu P2538)` | `P14` | `P14` | **Advanced**: Inverse MST in $L_1$ Norm via LP Duality to Bipartite Assignment MCMF |
| **P19** | `[BJWC2018] 最小生成树 (Inverse MST L2)` | — | `P19` | **Advanced**: Inverse MST in $L_2$ Norm via Fundamental Cycle DAG & Isotonic Regression |
| **P20** | `[CQOI2014] 危桥 (Luogu P3163)` | `P15` | — | **Advanced**: Okamura–Seymour Two-Commodity Undirected Flow Decomposition |
| **P21** | `AGC 029 F (Construction of a Tree)` | — | `P16` | **Advanced**: Hall's Marriage Theorem + Constructive BFS Tree Orientation |
| **P22** | `ABC 347 G (Grid Coloring 2)` | `P16` | `P21` | **Advanced**: 5-State Unary Threshold Chain (`燃やす埋める`) & Discrete Coarea Cut |
| **P23** | `CF 1517 G (Starry Night Camping)` | — | `P15` | **Advanced**: 4-Phase Modulo Parity Path (`(x%2, y%2)`) Minimum Vertex-Split Cut |
| **P24** | `Rectilinear Polygon Partition (UVa 1711)` | `P17` | `P17` | **Mastery**: Imai–Asano Axis-Parallel Chord Bipartite MIS & Euler–Reflex Duality |
| **P25** | `[省选联考 2020 A 卷] 魔法商店 (Luogu P6621 / LOJ 3303)` | `P18` | `P18` | **Mastery**: Linear Basis Exchange DAG + $L_p$ Isotonic Regression via `整体二分` |
| **P26** | `[BOI2004] Sequence (Luogu P4331)` & DAG $L_1$ | `P19` | — | **Mastery**: Strict Monotonic Shift $b_i = a_i - i$, 1D Slope Trick vs. DAG `整体二分` |
| **P27** | `AGC 038 F (Two Permutations)` | `P20` | — | **Mastery**: Cycle Decomposition + Bipartite Flip Rescue of Supermodular Agreement |
| **P28** | `ARC 107 F (Sum of Abs)` | — | `P20` | **Mastery**: 3-State Sign/Deletion Selection $\{-1, \text{del}, +1\}$ & Bipartite Parity Cut |
| **P29** | `ARC 142 E (Pairing Wizards)` | — | `P22` | **Mastery**: Dominance Split + Unary Threshold Chains for Pairwise Max-Min Constraints |
| **P30** | `CF 1427 G (One Billion Shades of Grey)` | `P21` | — | **Mastery**: Coarea Level-Set Decomposition + Incremental Re-Optimization (`退流`) |
| **P31** | `[NOI2009] 植物大战僵尸 (Luogu P2805)` | `P22` | — | **Mastery**: Topological Cycle-Pruning + Maximum Weight Closure |
| **P32** | `[NOI2010] 海拔 (Luogu P2046)` | `P22b` | — | **Mastery**: Continuous Threshold Rounding $\{0,1\}$ + Planar Dual $s$-$t$ Dijkstra |

---

## 2. Iteration 46 & 98 Reconciled: $L_p$ Isotonic Regression (`保序回归`), Preorder SCC Contraction, Parallel Binary Search (`整体二分`), and Matroid Basis Exchange Reductions

### 2.1 Non-Graph Diagnostic Signal & Problem Formulation

#### Step 1: Non-Graph Diagnostic Signal (Recognition)
When a problem provides $N$ variables $f_1, f_2, \dots, f_N$ (typically $N \le 10^3$, or $N \le 500, M \le 10^4$) with target values $y_i$, weights $w_i > 0$, and asks to minimize a separable convex deviation objective
$$\min_{f \in D^N} \sum_{i=1}^N w_i |f_i - y_i|^p \quad (p \ge 1)$$
subject to **pairwise order constraints** $f_u \le f_v$ for all $(u, v) \in E$ (where $G = (V, E)$ is a directed graph representing a preorder or partial order), examine the **topology of $G$** and the **value domain $D$**:
1. **Why Naive Greedy / Local Averaging Fails**: On a 1D chain ($1 \prec 2 \prec \dots \prec N$), adjacent violations $y_i > y_{i+1}$ can be merged greedily via the **Pool Adjacent Violators Algorithm (PAVA)** or **Slope Trick / Leftist Heaps** (`Luogu P4331`) in $O(N \log N)$ time because each element has at most one predecessor and one successor. On a general DAG or tree with both upward and downward branching, merging a violating pair $(u, v)$ alters $f_u = f_v$, which can simultaneously violate order constraints along multiple incomparable branches.
2. **Why Direct Unary Encoding (`燃やす埋める`) Blows Up**: If the coordinate range is $U = \max y_i - \min y_i \approx 10^9$, building a static threshold chain of length $U$ per vertex requires $O(N U)$ vertices, which is hopelessly exponential in $\log U$.
3. **The Isotonic Regression Signature**: Arbitrary DAG order constraints $f_u \le f_v$ + Separable convex loss $\sum_{v \in V} \phi_v(f_v)$ + Huge coordinate range $U \le 10^9$ $\implies$ **Parallel Binary Search (`整体二分`) over Two-Point Threshold Minimum Cuts**.

---

### 2.2 Step 2: Intermediate Algebraic Representation & Preorder SCC Contraction

Before running any threshold cut, we must reduce an arbitrary directed constraint graph $G = (V, E)$ to a Directed Acyclic Graph (DAG).

> [!IMPORTANT]
> **Lemma 2.1 (Preorder Strongly Connected Component Contraction — Cohort 2 Insight)**:
> If the order constraint graph $G = (V, E)$ contains a directed cycle $v_1 \to v_2 \to \dots \to v_k \to v_1$, the chain of inequalities $f_{v_1} \le f_{v_2} \le \dots \le f_{v_k} \le f_{v_1}$ forces all variables in the cycle to be identical:
> $$f_{v_1} = f_{v_2} = \dots = f_{v_k}.$$
> Consequently, we first compute the Strongly Connected Components (SCCs) of $G$ via Tarjan's algorithm in $O(N + M)$ time. Each SCC $C \subseteq V$ is contracted into a single super-vertex with the aggregated convex cost function
> $$\Phi_C(x) = \sum_{v \in C} w_v \phi_v(x) = \sum_{v \in C} w_v |x - y_v|^p.$$
> Because a non-negative linear combination of convex (resp. strictly convex) functions is convex (resp. strictly convex), the contracted problem on the condensation DAG $G_{\text{SCC}}$ preserves all structural hypotheses of Isotonic Regression.

Assume henceforth that $G = (V, E)$ is a DAG. Beyond standard $L_p$ norms, we formulate the **General Convex Isotonic Problem** $P(V, E, \Phi, D)$:
$$\min_{f : V \to D} \sum_{v \in V} \Phi_v(f_v) \quad \text{s.t.} \quad f_u \le f_v \;\;\forall (u, v) \in E$$
where $\Phi_v : \mathbb{R} \to \mathbb{R}$ is continuous and convex, and $D$ is either $\mathbb{R}$ (continuous) or $\mathbb{Z}$ (discrete integer). To test how the optimal solution $f^*$ behaves relative to a single scalar threshold $m$, consider the **Two-Point Restricted Subproblem** $P(V, E, \Phi, \{a, b\})$ where every variable is restricted to only two adjacent values $f_v \in \{a, b\}$ with $a < b$.

Assigning a binary indicator variable $x_v \in \{0, 1\}$ to each vertex $v \in V$:
$$x_v = \begin{cases} 0 & \text{if } f_v = a \text{ (low state)}, \\ 1 & \text{if } f_v = b \text{ (high state)}. \end{cases}$$
Then $f_v = a + (b - a) x_v$, and the two-point restricted problem becomes:
$$\min_{x \in \{0, 1\}^V} \sum_{v \in V} \Big( \Phi_v(a)(1 - x_v) + \Phi_v(b) x_v \Big) \quad \text{s.t.} \quad x_u \le x_v \;\;\forall (u, v) \in E.$$
Define the **marginal discrete derivative** (the cost change of promoting $v$ from $a$ to $b$):
$$\Delta_v(a, b) := \Phi_v(b) - \Phi_v(a).$$
Then the objective simplifies to a pure **Minimum-Weight Closure / Project Selection** polynomial:
$$\sum_{v \in V} \Phi_v(a) + \min_{x \in \{0, 1\}^V} \left\{ \sum_{v \in V} \Delta_v(a, b) \, x_v + \sum_{(u, v) \in E} \infty \cdot x_u (1 - x_v) \right\}.$$

---

### 2.3 The Two-Point Threshold Contraction Theorem (Dual-Proof Synthesis)

Why does solving the binary $\{a, b\}$ problem tell us anything about the unconstrained multi-valued optimum $f^* : V \to \mathbb{R}$? Cohort 1 and Cohort 2 provided two complementary proofs of this cornerstone result (originally proven by **Chakravarti 1989** and popularized in competitive programming by **Gao Ruiquan / 高睿泉, 2018 Chinese National Team Paper**). Presenting both gives complete geometric and variational intuition.

> [!IMPORTANT]
> **Theorem 2.2 (Two-Point Threshold Contraction / Threshold Monotonicity Theorem)**:
> Let $\Phi_v : \mathbb{R} \to \mathbb{R}$ be strictly convex for each $v \in V$ (or convex when selecting a lexicographically extremal optimizer). Fix any two probe values $a < b$, and let $x^* \in \{0, 1\}^V$ be an optimal binary indicator for the two-point problem $P(V, E, \Phi, \{a, b\})$, partitioning $V$ into
> $$V_{\le} = \{v \in V : x^*_v = 0\} \quad \text{and} \quad V_{>} = \{v \in V : x^*_v = 1\}.$$
> 1. **Continuous Threshold Split ($a \to m^-, b \to m^+$)**: Taking the directional derivative limit as $a = m, b = m + \epsilon$ ($\epsilon \to 0^+$), where $\Delta_v(m, m+\epsilon)/\epsilon \to \Phi'_{v,+}(m)$, there exists a global continuous optimum $f^* : V \to \mathbb{R}$ such that
>    $$f^*_v \le m \;\;\forall v \in V_{\le}, \qquad f^*_v \ge m \;\;\forall v \in V_{>}.$$
> 2. **Discrete Integer Split ($a = m, b = m+1$)**: For $D = \mathbb{Z}$ and $m \in \mathbb{Z}$, solving $P(V, E, \Phi, \{m, m+1\})$ with marginal costs $\Delta_v(m, m+1) = \Phi_v(m+1) - \Phi_v(m)$ guarantees that there exists an optimal integer assignment $f^* : V \to \mathbb{Z}$ satisfying
>    $$f^*_v \le m \;\;\forall v \in V_{\le}, \qquad f^*_v \ge m + 1 \;\;\forall v \in V_{>}.$$
> 3. **Edge Decoupling across the Cut**: Any order constraint $(u, v) \in E$ with $u \in V_{\le}$ and $v \in V_{>}$ is **automatically satisfied** for all future recursive refinements because $f^*_u \le m < m+1 \le f^*_v$ (or $f^*_u \le m \le f^*_v$). Thus $V_{\le}$ and $V_{>}$ decouple into two completely independent subproblems!

#### Proof Method A: Unit-Step Variational Perturbation (Cohort 2 Formulation)
Let $f^*$ be an optimal integer solution to $P(V, E, \Phi, \mathbb{Z})$ that minimizes the tie-breaking potential $\Psi(f^*) = \sum_{v \in V} |f^*_v - m|$, and let $g_v = m + x^*_v \in \{m, m+1\}$ be the two-point optimum that minimizes $\sum_{v \in V} x^*_v$. Suppose for contradiction that the bad set
$$U = \{v \in V : f^*_v > m \text{ and } g_v = m\} = \{v \in V_{\le} : f^*_v \ge m + 1\}$$
is non-empty. Choose the minimal level among elements of $U$ (or consider a maximal upper-ideal inside a level component of $U$) and define two perturbed assignments:
- $f'_v = f^*_v - [v \in U_0]$ (shifting a valid lower-interface subset $U_0 \subseteq U$ down by $1$ toward $m$),
- $g'_v = g_v + [v \in U_0]$ (lifting $U_0$ from $m$ to $m+1$).

Because $g_v = m$ on $U_0$ and $f^*_v \ge m + 1$ on $U_0$, $U_0$ can be chosen closed under order constraints so that both $f'$ and $g'$ remain feasible for $E$. By optimality of $g$ for the $\{m, m+1\}$ problem:
$$\sum_{v \in U_0} \big(\Phi_v(m+1) - \Phi_v(m)\big) \ge 0.$$
By convexity of $\Phi_v$ (non-decreasing discrete slopes $\Phi_v(k) - \Phi_v(k-1) \ge \Phi_v(m+1) - \Phi_v(m)$ for all $k \ge m+1$):
$$\Phi(f^*) - \Phi(f') = \sum_{v \in U_0} \big(\Phi_v(f^*_v) - \Phi_v(f^*_v - 1)\big) \ge \sum_{v \in U_0} \big(\Phi_v(m+1) - \Phi_v(m)\big) \ge 0.$$
Thus $\Phi(f') \le \Phi(f^*)$, so $f'$ is also globally optimal, yet $\Psi(f') < \Psi(f^*)$, contradicting the minimality of $\Psi(f^*)$. By a symmetric argument on $W = \{v \in V_{>} : f^*_v \le m\}$, we conclude $f^*_v \le m$ on $V_{\le}$ and $f^*_v \ge m+1$ on $V_{>}$. $\blacksquare$

#### Proof Method B: Continuous Strict Convexity Midpoint Shift (Cohort 1 Formulation)
For continuous $L_p$ ($p > 1$) and any $a < b$ with midpoint $m = \frac{a+b}{2}$, suppose $U = \{v \in V_{\le} : f^*_v > m\} \neq \emptyset$. Let $\delta = \min_{v \in U} (f^*_v - m) > 0$. For $0 < \epsilon < \min(\delta, b-a)$, shifting $U$ down by $\epsilon$ in $f^*$ and shifting $U$ up from $a$ to $b$ in the relaxed $\{a,b\}$ indicator problem yields, by strict convexity of $|x - y_v|^p$:
$$\frac{|f^*_v - y_v|^p - |f^*_v - \epsilon - y_v|^p}{\epsilon} > \frac{|b - y_v|^p - |a - y_v|^p}{b - a} \quad \forall v \in U,$$
because the secant slope on $[f^*_v - \epsilon, f^*_v] \subset (m, \infty)$ strictly exceeds the symmetric secant slope on $[a, b]$ centered at $m$. Summing over $v \in U$ shows that decreasing $f^*$ by $\epsilon$ on $U$ strictly reduces the global objective, a contradiction. $\blacksquare$

---

### 2.4 Step 3: Mechanical Graph Compilation of the Threshold Cut `solve(V_sub, L, R)`

Given a recursive subproblem with vertex subset $V_{\text{sub}} \subseteq V$, induced edge set $E_{\text{sub}} = E \cap (V_{\text{sub}} \times V_{\text{sub}})$, and active integer coordinate interval $[L, R]$:
1. **Base Case**: If $L == R$, every $v \in V_{\text{sub}}$ is locked to $f^*_v = L$; return.
2. **Midpoint Probe**: Set $m = \lfloor (L + R) / 2 \rfloor$. We compile the two-point problem on $\{m, m+1\}$ with marginal cost $\Delta_v = \Phi_v(m+1) - \Phi_v(m)$ into an $S$-$T$ minimum cut where **Source $S$ corresponds to $x_v = 1$ ($f_v = m+1$)** and **Sink $T$ corresponds to $x_v = 0$ ($f_v = m$)**.

Let us compile each algebraic term mechanically:
- **Order Constraints $x_u \le x_v$ for $(u, v) \in E_{\text{sub}}$**:
  The forbidden state is $x_u = 1 \land x_v = 0$ ($u \in S$-side, $v \in T$-side), which incurs penalty $\infty \cdot x_u(1 - x_v)$.
  $\implies$ Add a directed edge $u \to v$ with capacity $\infty$.
- **Unary Marginal Terms $\Delta_v x_v$ for $v \in V_{\text{sub}}$**:
  - **Case 1 ($\Delta_v < 0$, i.e., promoting $v$ from $m$ to $m+1$ *decreases* cost)**:
    Write $\Delta_v x_v = \Delta_v + |\Delta_v|(1 - x_v)$. Putting $v$ on the $T$-side ($x_v = 0$) forfeits the cost reduction and pays penalty $|\Delta_v| = -\Delta_v$.
    $\implies$ Add directed edge $S \to v$ with capacity $-\Delta_v$.
  - **Case 2 ($\Delta_v > 0$, i.e., promoting $v$ from $m$ to $m+1$ *increases* cost)**:
    Putting $v$ on the $S$-side ($x_v = 1$) pays penalty $\Delta_v$.
    $\implies$ Add directed edge $v \to T$ with capacity $\Delta_v$.
  - **Case 3 ($\Delta_v = 0$)**: No terminal edge needed (or zero-capacity edge).

```
  [Source S (x_v = 1: f_v >= m+1)]
         |
         | cap = -Delta_u  (if Delta_u < 0, i.e., y_u >= m+1 for L1)
         v
      (  u  ) ------------ cap = inf ------------> (  v  )
         |     [enforces f_u <= f_v: x_u <= x_v]      |
         |                                            | cap = +Delta_v (if Delta_v > 0)
         v                                            v
  [                        Sink T (x_v = 0: f_v <= m)                        ]
```

3. **Partition & Recurse**:
   Run Dinic's algorithm on $(V_{\text{sub}} \cup \{S, T\}, E_{\text{sub}} \cup E_{\text{term}})$. Let $R_S \subseteq V_{\text{sub}}$ be the set of vertices reachable from $S$ in the final residual graph ($x_v = 1$).
   - $V_{>} = R_S$ recurses on $[m + 1, R]$ with induced edges $E \cap (V_{>} \times V_{>})$.
   - $V_{\le} = V_{\text{sub}} \setminus R_S$ recurses on $[L, m]$ with induced edges $E \cap (V_{\le} \times V_{\le})$.

> [!CAUTION]
> **Implementation Invariant (The $O(N^2)$ Array-Clearing Trap — Cohort 2 Audit)**:
> Across all $O(\log U)$ recursion levels, the sum of $|V_{\text{sub}}|$ at any single depth is $\sum |V_{\text{sub}}| = N$, and $\sum |E_{\text{sub}}| \le M$. Thus the total Max-Flow work across the entire recursion tree is:
> $$T_{\text{total}} = \sum_{\text{depth}=1}^{\lceil \log_2 U \rceil} \sum_{V_{\text{sub}}} T_{\text{Dinic}}(|V_{\text{sub}}|, |E_{\text{sub}}|) = O\big(\text{MaxFlow}(N, M) \log U\big).$$
> **HOWEVER**, if your Dinic implementation clears `head[1..N]` or `level[1..N]` using global vertex IDs inside `solve(V_sub, L, R)`, then a skewed recursion tree of $O(N)$ leaves at each depth will pay $O(N)$ per call, degrading the time complexity to $O(N^2 \log U)$!
> **Mandatory Rule**: Always re-index the vertices of $V_{\text{sub}}$ locally to $0, 1, \dots, |V_{\text{sub}}|-1$ (with $S = |V_{\text{sub}}|, T = |V_{\text{sub}}|+1$) so that graph initialization, BFS, and DFS touch strictly $O(|V_{\text{sub}}| + |E_{\text{sub}}|)$ memory!

---

### 2.5 Norm Specializations: $L_1$, $L_2$, and $L_\infty$

#### 1. $L_1$ Norm ($p = 1$, $\Phi_v(x) = w_v |x - y_v|$)
For integer $y_v \in \mathbb{Z}$ and $m \in \mathbb{Z}$, the marginal cost on $[m, m+1]$ is a pure step function:
$$\Delta_v(m, m+1) = w_v |m + 1 - y_v| - w_v |m - y_v| = \begin{cases} -w_v & \text{if } m + 1 \le y_v \iff y_v \ge m + 1, \\ +w_v & \text{if } m \ge y_v \iff y_v \le m. \end{cases}$$
- **Terminal Compilation**: If $y_v > m$, add $S \to v$ with capacity $w_v$; if $y_v \le m$, add $v \to T$ with capacity $w_v$.
- **Discrete Coordinate Compression (Vertex-Value Closure Theorem)**: Since $\Delta_v(m, m+1)$ only changes sign when $m$ crosses $y_v$, the cut capacities are completely identical for all $m \in [y_{(k)}, y_{(k+1)} - 1]$ where $y_{(1)} < y_{(2)} < \dots < y_{(K)}$ ($K \le N$) are the sorted unique target values! Therefore, there always exists an optimal $L_1$ solution with $f^*_v \in \{y_1, \dots, y_N\}$, and **Parallel Binary Search only needs to recurse over the array indices $[1, K]$ in $O(\log N)$ levels** instead of $O(\log U)$!

#### 2. $L_2$ Norm ($p = 2$, $\Phi_v(x) = w_v (x - y_v)^2$)
- **Integer $L_2$ ($D = \mathbb{Z}$)**:
  $$\Delta_v(m, m+1) = w_v \big((m + 1 - y_v)^2 - (m - y_v)^2\big) = w_v (2m + 1 - 2y_v).$$
  Unlike $L_1$, this marginal cost depends linearly on $m$, so optimal integer values $f^*_v$ can lie strictly between target values $y_i$ (as weighted averages). Recursion must run over the full integer range $[\min y_i, \max y_i]$ in $O(\log U)$ levels.
- **Continuous $L_2$ ($D = \mathbb{R}$, Exact Rational Block Averaging — Cohort 1 Insight)**:
  Using directional derivatives $\Phi'_v(m) = 2w_v(m - y_v)$ (scaled by $1/2$: capacity $w_v(y_v - m)$ from $S \to v$ if $y_v > m$, and $w_v(m - y_v)$ from $v \to T$ if $y_v < m$), binary search over $\mathbb{R}$ (or rational intervals) clusters vertices that remain inseparable into level blocks $C$. Once a block $C$ is isolated with $f^*_v = c$ for all $v \in C$, the exact continuous optimum on $C$ is its weighted mean:
  $$f^*_C = \arg\min_{x \in \mathbb{R}} \sum_{v \in C} w_v (x - y_v)^2 = \frac{\sum_{v \in C} w_v y_v}{\sum_{v \in C} w_v} \in \mathbb{Q}.$$
  Furthermore, if an integer solution is required after continuous $L_2$ block identification, the quadratic $\sum_{v \in C} w_v(x - y_v)^2 = (\sum_{v \in C} w_v)(x - f^*_C)^2 + \text{const}$ is minimized over $\mathbb{Z}$ by rounding $f^*_C$ to the nearest integer (requiring just one final `{floor, ceil}` cut per block if $f^*_C = k + 0.5$).

#### 3. $L_\infty$ Norm ($p = \infty$, $\min_f \max_{v \in V} w_v |f_v - y_v|$ — Cohort 1 Insight)
Do **not** use Max-Flow for $L_\infty$ Isotonic Regression! Testing whether $\max_v w_v |f_v - y_v| \le \lambda$ is equivalent to checking whether there exists $f : V \to \mathbb{R}$ satisfying:
$$\forall v \in V : \quad L_v(\lambda) := y_v - \frac{\lambda}{w_v} \le f_v \le y_v + \frac{\lambda}{w_v} =: R_v(\lambda), \qquad \forall (u, v) \in E : \quad f_u \le f_v.$$
By transitivity, a valid $f$ exists if and only if for every directed path $u \leadsto v$ in the DAG $G$, $L_u(\lambda) \le R_v(\lambda)$, which we check in **$O(N + M)$ time via topological DP**:
$$dp[v] = \max\Big( L_v(\lambda), \max_{(u, v) \in E} dp[u] \Big), \qquad \text{feasible iff } \forall v \in V, \; dp[v] \le R_v(\lambda).$$
Binary searching $\lambda$ solves $L_\infty$ Isotonic Regression in **$O((N + M) \log(U/\epsilon))$** time without a single flow call!

#### Summary Comparison of $L_p$ Isotonic Regression Regimes

| Regime / Graph Topology | Norm $p$ | Domain $D$ | Optimal Algorithm & Complexity | Key Structural Property |
| :--- | :---: | :---: | :--- | :--- |
| **1D Chain** ($1 \prec 2 \prec \dots \prec N$) | $L_1$ | $\mathbb{Z}$ or $\mathbb{R}$ | **Slope Trick / Leftist Heap Median Maintenance** (`Luogu P4331`): $O(N \log N)$ | Strictly monotonic $a_i < a_{i+1}$ reduces via $b_i = a_i - i$ to $b_i \le b_{i+1}$. |
| **1D Chain** ($1 \prec 2 \prec \dots \prec N$) | $L_2$ | $\mathbb{R}$ | **PAVA (Pool Adjacent Violators)** on convex hull / monotone stack: $O(N)$ | Adjacent violating blocks merge to their weighted mean. |
| **General Preorder / DAG** | $L_1$ | $\mathbb{Z}$ or $\mathbb{R}$ | SCC Contraction + **Coordinate-Compressed `整体二分` + Dinic**: $O(\text{MaxFlow}(N,M)\log N)$ | Optimal values satisfy $f^*_v \in \{y_1, \dots, y_N\}$ (Vertex-Value Closure). |
| **General Preorder / DAG** | $L_p$ ($p > 1$) | $\mathbb{Z}$ | SCC Contraction + **Range `整体二分` on $[\min y, \max y]$ + Dinic**: $O(\text{MaxFlow}(N,M)\log U)$ | Marginal cost $\Delta_v(m, m+1) = \Phi_v(m+1)-\Phi_v(m)$ varies with $m$. |
| **General Preorder / DAG** | $L_\infty$ | $\mathbb{Z}$ or $\mathbb{R}$ | **Binary Search on $\lambda$ + DAG Topological DP**: $O((N+M)\log U)$ | Reduces to interval feasibility $\max_{u \leadsto v} L_u(\lambda) \le R_v(\lambda)$; **no Max-Flow needed**. |

---

### 2.6 Step 4: Hand-Checkable Toy Trace & Broken Gadget Counterexample

#### Concrete Numerical Trace ($N = 4$ Diamond DAG, $L_1$ Norm)
Consider a 4-vertex DAG with vertices $\{1, 2, 3, 4\}$, unit weights $w_i = 1$, target values $y = [10, 4, 8, 2]$, and order edges:
$$E = \{(1, 2), (1, 3), (2, 4), (3, 4)\} \implies f_1 \le f_2 \le f_4 \text{ and } f_1 \le f_3 \le f_4.$$
Notice that $y_1 = 10$ is at the bottom of the poset while $y_4 = 2$ is at the top—every constraint is violated by $y$!
- **Sorted Unique Coordinates**: $Y = [2, 4, 8, 10]$ (indices $1..4$).
- **Level 1 Call**: `solve({1, 2, 3, 4}, idx_L = 1, idx_R = 4)`:
  - Midpoint index $mid = 2 \implies$ threshold value $m = Y[2] = 4$, testing $\{4, 8\}$ (or $\{4, 5\}$).
  - Check $y_v > 4$:
    - $y_1 = 10 > 4 \implies$ Edge $S \to 1$ with capacity $1$.
    - $y_2 = 4 \le 4 \implies$ Edge $2 \to T$ with capacity $1$.
    - $y_3 = 8 > 4 \implies$ Edge $S \to 3$ with capacity $1$.
    - $y_4 = 2 \le 4 \implies$ Edge $4 \to T$ with capacity $1$.
  - Order edges with capacity $\infty$: $1 \to 2, 1 \to 3, 2 \to 4, 3 \to 4$.
  - **Max-Flow / Min-Cut Trace**:
    - Path 1: $S \to 1 \to 2 \to T$ (flow $1$, saturates $S \to 1$ and $2 \to T$).
    - Path 2: $S \to 3 \to 4 \to T$ (flow $1$, saturates $S \to 3$ and $4 \to T$).
    - Total Max-Flow $= 2$. In the residual graph:
      - Can $S$ reach $1$? $S \to 1$ is saturated, and although $S \to 3$ is saturated too, check residual edges: from $1$, we used $1 \to 2$, so residual edge $2 \to 1$ has cap $1$; from $3$, we used $3 \to 4$, so residual edge $4 \to 3$ has cap $1$. Neither $S \to 1$ nor $S \to 3$ has residual capacity!
      - Thus $R_S = \{S\}$, meaning $V_{>} = \emptyset$ and $V_{\le} = \{1, 2, 3, 4\}$!
    - Wait: is there another min-cut? Yes! Cutting $(2 \to T)$ and $(4 \to T)$ also has cost $2$, which would put $\{1, 2, 3, 4\} \in V_{>}$. Under standard Dinic reachability from $S$, $R_S = \emptyset$, so all 4 vertices recurse left to `solve({1, 2, 3, 4}, idx_L = 1, idx_R = 2)` ($Y = [2, 4]$).
- **Level 2 Call**: `solve({1, 2, 3, 4}, idx_L = 1, idx_R = 2)` ($Y = [2, 4]$, $m = Y[1] = 2$):
  - $y_1 = 10 > 2, y_2 = 4 > 2, y_3 = 8 > 2 \implies$ Edges $S \to 1, S \to 2, S \to 3$ each with cap $1$ (total supply $3$).
  - $y_4 = 2 \le 2 \implies$ Edge $4 \to T$ with cap $1$ (total sink demand $1$).
  - Max-Flow $= 1$ (saturating $4 \to T$). Residual graph from $S$ reaches $\{1, 2, 3, 4\} = V_{>}$!
  - All 4 vertices recurse right to `idx_L = 2, idx_R = 2` ($Y[2] = 4$), locking in:
    $$f^* = [4, 4, 4, 4], \quad \text{Cost} = |4-10| + |4-4| + |4-8| + |4-2| = 6 + 0 + 4 + 2 = 12.$$
  - (Note: Any constant $f^* = [c, c, c, c]$ with $c \in [4, 8]$ achieves the exact same minimum $L_1$ cost of $12$ because two targets $\{2, 4\}$ lie $\le 4$ and two targets $\{8, 10\}$ lie $\ge 8$!)

#### Broken Gadget Counterexample (Reversing the Order Edge $u \to v$)
Suppose a solver mistakenly directs the order edge $f_u \le f_v$ from $v \to u$ with capacity $\infty$. Then $x_v = 1 \implies x_u = 1$, which enforces $f_v \le f_u$ (the exact opposite partial order!). On our toy DAG, $4 \to 2 \to 1$ and $4 \to 3 \to 1$ would allow $f_1 = 10, f_2 = 4, f_3 = 8, f_4 = 2$ to have zero cut cost, returning the completely invalid assignment $f = [10, 4, 8, 2]$!

---

### 2.7 Matroid & Linear Basis Exchange Reductions to Isotonic Regression (`[省选联考 2020 A 卷] 魔法商店`, `Luogu P6621 / LOJ 3303`)

How do problems that do not mention partial orders reduce to Isotonic Regression? The flagship archetype is **Inverse Matroid / Linear Basis Optimization** (`[省选联考 2020 A 卷] 魔法商店`, `Luogu P6621` / `LOJ 3303`, and **Gao Ruiquan's 2018 National Team Paper**).

Suppose we are given a universe $U$ of $N$ items with initial costs $y_i$, and two bases (or a single target minimum-weight basis and maximum-weight basis) $B_{\min}, B_{\max}$ of a matroid $\mathcal{M} = (U, \mathcal{I})$ (in `魔法商店`, $\mathcal{M}$ is the linear matroid over $\mathbb{F}_2^{64}$ under XOR, with $|B| = m \le 64, N \le 1000$). We want to modify item costs to $f_i$ to minimize $\sum_{i=1}^N |f_i - y_i|^p$ such that:
1. $B_{\min}$ is a **minimum-weight basis** under $f$, and
2. $B_{\max}$ is a **maximum-weight basis** under $f$.

By the **Matroid Single-Element Exchange Optimality Theorem**:
- $B_{\min}$ is a minimum-weight basis under $f$ if and only if for every non-basis element $e \notin B_{\min}$ and every basis element $b \in C(B_{\min}, e)$ in the fundamental circuit of $e$ with respect to $B_{\min}$ (i.e., $B_{\min} \setminus \{b\} \cup \{e\} \in \mathcal{I}$):
  $$f_b \le f_e \quad \text{(Order edge } b \to e\text{)}.$$
- Symmetrically, $B_{\max}$ is a maximum-weight basis under $f$ if and only if for every $e \notin B_{\max}$ and every $b \in C(B_{\max}, e)$:
  $$f_e \le f_b \quad \text{(Order edge } e \to b\text{)}.$$

> [!TIP]
> **Diagnostic Comparison: Inverse MST / Matroid Basis in $L_1$ vs. $L_2 / L_p$**:
> - **Single Basis $B_{\min}$ under $L_1$ Norm (`[SHOI2004] 最小生成树`, `Luogu P2538`)**: Every constraint $f_b \le f_e$ always pairs a tree edge $b \in T$ with a non-tree edge $e \notin T$. Thus the constraint graph is **bipartite**! Furthermore, tree edges only ever need to decrease ($f_b = y_b - d_b$) and non-tree edges only ever need to increase ($f_e = y_e + d_e$), so $L_1$ Inverse MST dualizes directly to **Maximum-Weight Bipartite Matching / MCMF** (see §5.2).
> - **Two Simultaneous Bases ($B_{\min}$ and $B_{\max}$ in `魔法商店`) or $L_2$ Norm (`[BJWC2018] 最小生成树`)**: When both $B_{\min}$ and $B_{\max}$ are constrained simultaneously, an element $x \in B_{\max} \setminus B_{\min}$ acts as a non-tree element for $B_{\min}$ and a tree element for $B_{\max}$, creating **multi-hop directed chains and cycles** $b_1 \to x \to b_2$ (non-bipartite!). Or when the norm is $L_2$ ($p = 2$), the LP dual is no longer linear assignment. In both cases, we compile the $O(N \cdot \text{rank}(\mathcal{M}))$ exchange inequalities into a directed graph, contract SCCs, and run **`整体二分` Isotonic Regression**!


---

## 3. Iteration 47 & 99 Reconciled: Cross-Domain Bridge I — Combinatorial Games, Von Neumann Minimax LP Duality, Dulmage–Mendelsohn Walk Polarity, and Chessboard Parity

Combinatorial game theory intersects flow and matching theory along four distinct mechanisms:
1. **Zero-Sum Simultaneous Matrix Games $\leftrightarrow$ LP Duality / Max-Flow** (Von Neumann's Minimax Theorem on Bipartite Graphs).
2. **Impartial Normal-Play Walk Games $\leftrightarrow$ Dulmage–Mendelsohn / Gallai–Edmonds Matching Decomposition** (`[JSOI2009] 游戏`).
3. **Adversarial Reachability & Blocker Games $\leftrightarrow$ Vertex/Row-Column Minimum Cut** (`ARC 074 F`, `ABC 239 G`).
4. **Grid Increment/Parity Games $\leftrightarrow$ Bipartite Domino Tiling + Binary Search** (`[SCOI2012] 奇怪的游戏`).

---

### 3.1 Zero-Sum Matrix Games & Von Neumann's Minimax Theorem on Bipartite Graphs

#### Step 1: Non-Graph Diagnostic Signal
A problem describes a **simultaneous-move two-player zero-sum game** on a grid or bipartite relation $E \subseteq R \times C$:
- **Player 1 (Hider / Row Player)** chooses a distribution $p \in \Delta(R)$ over rows (or places $K$ tokens on distinct rows/cells).
- **Player 2 (Seeker / Column Player)** simultaneously chooses a distribution $q \in \Delta(C)$ over columns (or inspects a valid matching/cover).
- If the Seeker hits the Hider's chosen cell $(r, c) \in E$, the Seeker wins payoff $c_{r,c} > 0$; otherwise payoff is $0$.
When the problem asks for the **Nash Equilibrium value** (the minimax expected payoff), recognize that by **Von Neumann's Minimax Theorem**, a zero-sum bilinear game $\max_{p \in \Delta(R)} \min_{q \in \Delta(C)} p^T A q$ is a Primal-Dual Linear Program pair!

#### Step 2: Intermediate Algebraic / LP Representation
In the generalized **Weighted Hide-and-Seek Game** (extending von Neumann 1953 to variable payoffs $c_{r,c} > 0$ on allowed cells $(r, c) \in E$, and returning $0$ on forbidden cells $(r, c) \notin E$):
- The Hider chooses probabilities $p_{r,c} \ge 0$ for $(r, c) \in E$ with $\sum_{(r,c) \in E} p_{r,c} = 1$ to **minimize** the maximum expected return any single row $r$ or column $c$ yields to the Seeker:
  $$\min_{p, v} \; v \quad \text{s.t.} \quad \sum_{c : (r,c) \in E} c_{r,c} p_{r,c} \le v \;\;(\forall r \in R), \quad \sum_{r : (r,c) \in E} c_{r,c} p_{r,c} \le v \;\;(\forall c \in C), \quad \sum_{(r,c) \in E} p_{r,c} = 1.$$
- Normalizing variables via $x_{r,c} = \frac{p_{r,c}}{v} \ge 0$, the constraint $\sum p_{r,c} = 1$ becomes $\sum x_{r,c} = \frac{1}{v}$. Thus minimizing $v$ is equivalent to **maximizing $\frac{1}{v} = \sum_{(r,c) \in E} x_{r,c}$** subject to:
  $$\forall r \in R: \sum_{c} c_{r,c} x_{r,c} \le 1 \iff x_{r,c} \le \frac{1}{c_{r,c}} \text{ (if } R, C \text{ are vertex-capacitated)}.$$
   specifically, in the classic **Unit-Payoff Hide-and-Seek ($c_{r,c} = 1$)** where the Seeker picks a single row $r$ OR column $c$ (or where Hider hides in one cell $(r,c) \in E$ and Seeker picks a row or column), if Hider places mass $x_{r,c}$ on edges $(r,c) \in E$ such that each row $r$ has $\sum_c x_{r,c} \le 1$ and each column $c$ has $\sum_r x_{r,c} \le 1$, then $\max \sum_{(r,c) \in E} x_{r,c}$ is the **Maximum Bipartite Matching** size $\nu(G)$!
- By **Kőnig's Theorem** (Primal-Dual LP Duality on totally unimodular bipartite incidence matrices):
  $$\max_{\text{Matching } M} |M| = \min_{\text{Vertex Cover } C} |C| = \nu(G), \quad \text{and equilibrium game value } v^* = \frac{1}{\nu(G)}.$$
- **Optimal Mixed Strategies**:
  - **Hider's Optimal Strategy**: Pick one of the $\nu(G)$ edges of a maximum matching $M^*$ uniformly at random with probability $\frac{1}{\nu(G)}$. Since no two edges in $M^*$ share a row or column, any row or column chosen by the Seeker catches the Hider with probability at most $\frac{1}{\nu(G)}$.
  - **Seeker's Optimal Strategy**: Pick one of the $\nu(G)$ lines (rows/columns) of a minimum vertex cover $C^*$ uniformly at random with probability $\frac{1}{\nu(G)}$. Since every valid hiding cell $(r, c) \in E$ is covered by at least one line in $C^*$, the Seeker catches the Hider with probability at least $\frac{1}{\nu(G)}$.

---

### 3.2 Impartial Walk Games & The Dulmage–Mendelsohn Turn-Order Polarity Theorem (`[JSOI2009] 游戏`, `Luogu P4055`)

#### Step 1: Non-Graph Diagnostic Signal
Two players play an impartial normal-play game on an undirected graph $G = (V, E)$ (often a grid with obstacles): a single token moves along edges to **previously unvisited vertices** (forming a simple path), and the last player able to move wins.
- **Why Tree/DAG Sprague–Grundy DP Fails**: General undirected graphs contain cycles, and tracking the subset of visited vertices in bitmask DP costs $O(2^N \cdot N)$, which fails for $N \le 10^4$.
- **Flow/Matching Trigger**: Alternating-turn simple paths on a graph where no vertex may be visited twice are governed by **Maximum Matching Augmenting/Alternating Path Theory**!

#### Step 2 & 3: Reconciling the Turn-Order Polarity Trap (Cohort 1 vs. Cohort 2 Audit)
A major source of bugs in competitive programming is confusing the **two standard turn-order formulations** of the Graph Walk Game. Cohort 2 identified this exact polarity reversal; here we state the unified theorem covering both variants.

> [!IMPORTANT]
> **Theorem 3.1 (Walk Game Matching Polarity & Dulmage–Mendelsohn Certificate)**:
> Let $G = (V, E)$ be an undirected graph (bipartite in `[JSOI2009] 游戏`, or general graph via Tutte–Berge / Gallai–Edmonds decomposition). Call a vertex $v_0 \in V$ **essential** (or **critical**) if $v_0$ is saturated in **every** maximum matching of $G$ (i.e., $\nu(G \setminus \{v_0\}) = \nu(G) - 1$), and **inessential** (or **avoidable**, $v_0 \in \mathcal{E}$) if there exists at least one maximum matching $M$ that leaves $v_0$ exposed ($\nu(G \setminus \{v_0\}) = \nu(G)$).
>
> | Game Variant | Rule for Starting Vertex $v_0$ | Who Moves the Token First from $v_0$? | Winning Condition for **First Mover from $v_0$** | Winning Condition for **Player 1 (`JYY` in `[JSOI2009] 游戏`)** |
> | :--- | :--- | :--- | :--- | :--- |
> | **Variant A (`[JSOI2009] 游戏`, `Luogu P4055`)** | **Player 1 (`JYY`)** chooses initial vertex $v_0$ and places the token there. | **Player 2 (`YYJ`)** makes the first move $v_0 \to v_1$. | Player 2 wins from $v_0$ iff $v_0$ is **essential** ($v_0 \notin \mathcal{E}$). | Player 1 (`JYY`) wins by placing at $v_0$ iff $v_0$ is **inessential** ($v_0 \in \mathcal{E}$, NOT in every max matching)! |
> | **Variant B (Fixed-Start Walk Game)** | The token already starts at a given vertex $v_0$. | **Player 1** makes the first move $v_0 \to v_1$. | Player 1 wins from $v_0$ iff $v_0$ is **essential** ($v_0 \notin \mathcal{E}$). | Player 1 wins from $v_0$ iff $v_0$ is **essential** ($v_0 \notin \mathcal{E}$, IN every max matching)! |

#### Proof of Theorem 3.1 (Strategy-Stealing via Alternating Paths)
Fix the initial vertex $v_0$, and call the player who must move the token out of $v_0$ the **Mover** ($M_{\text{first}}$) and the player who just placed the token at $v_0$ the **Placer** ($M_{\text{second}}$).
1. **Case 1: $v_0$ is Essential (Saturated in Every Maximum Matching $\implies$ Mover Wins)**:
   Fix any maximum matching $M^*$. Since $v_0$ is essential, $v_0$ is matched in $M^*$ to some partner $v_1 = M^*(v_0)$. The Mover moves the token along the matching edge $v_0 \to v_1$. Now the Placer must move from $v_1$ to some unvisited neighbor $v_2$.
   - Could $v_2$ be exposed (unmatched) in $M^*$? **No!** If $v_2$ were exposed, then $(v_0, v_1, v_2)$ would be an even-length $M^*$-alternating path starting at $v_0$ and ending at an exposed vertex $v_2$. Flipping the matching along this path—replacing $(v_0, v_1) \in M^*$ with $(v_1, v_2)$—produces a new maximum matching $M' = M^* \oplus \{(v_0, v_1), (v_1, v_2)\}$ of the exact same size $|M'| = |M^*|$ in which **$v_0$ is exposed**, contradicting that $v_0$ is essential!
   - By induction, after any sequence of moves $(v_0, v_1, v_2, \dots, v_{2k})$, the Placer's move $v_{2k-1} \to v_{2k}$ can never land on an $M^*$-exposed vertex (otherwise flipping $M^*$ along the even alternating path $v_0 \leadsto v_{2k}$ would expose $v_0$ in a maximum matching). Therefore, $v_{2k}$ is always matched in $M^*$ to an unvisited partner $v_{2k+1} = M^*(v_{2k})$, giving the Mover a guaranteed legal reply!
2. **Case 2: $v_0$ is Inessential (Exposed in Some Maximum Matching $M^* \implies$ Placer Wins)**:
   Choose a maximum matching $M^*$ in which $v_0$ is exposed. Whenever the Mover steps from $v_{2k}$ to an unvisited neighbor $v_{2k+1}$, the vertex $v_{2k+1}$ **must** be matched in $M^*$—for if $v_{2k+1}$ were exposed in $M^*$, the odd-length alternating path $(v_0, v_1, \dots, v_{2k+1})$ connecting two $M^*$-exposed vertices $v_0$ and $v_{2k+1}$ would be an **$M^*$-augmenting path**, contradicting that $M^*$ has maximum size! Thus the Placer always replies with $v_{2k+1} \to v_{2k+2} = M^*(v_{2k+1})$ until the Mover runs out of moves. $\blacksquare$

#### Step 3: Mechanical Graph Compilation of the Dulmage–Mendelsohn Certificate $\mathcal{E}$ in $O(M\sqrt{N})$
Do **not** re-run Maximum Matching $N$ times by deleting each vertex $v_0$ one by one! In a bipartite graph $G = (L \cup R, E)$ with a single computed maximum matching $M^*$ (via Hopcroft–Karp / Dinic from $S \to L \to R \to T$):
- An vertex $v_0 \in L$ is inessential ($v_0 \in \mathcal{E}_L$, exposed in some maximum matching) $\iff$ starting from the residual network of $M^*$, there is an even alternating path from an $M^*$-exposed vertex $u \in L$ to $v_0$.
- In terms of the **Dinic Residual Graph** $G_f$:
  1. **Left Inessential Set $\mathcal{E}_L$**: All vertices $u \in L$ reachable from Source $S$ in the residual graph $G_f$ using directed residual arcs (since $S \to u$ has residual capacity $1$ iff $u \in L$ is exposed in $M^*$, and $u \xrightarrow{\text{unmatched}} w \xrightarrow{\text{matched}} u'$ traverses alternating paths in $L$).
  2. **Right Inessential Set $\mathcal{E}_R$**: All vertices $w \in R$ that can reach Sink $T$ in the residual graph $G_f$ (i.e., reachable from $T$ in the **reversed** residual graph $G_f^{\text{rev}}$, since $w \to T$ has residual capacity $1$ iff $w \in R$ is exposed in $M^*$).
- **Total Complexity**: One Dinic run + two linear BFS traversals (from $S$ on $G_f$ and from $T$ on $G_f^{\text{rev}}$) in **$O(M\sqrt{N})$** time!

#### Step 4: Toy Trace & Broken Gadget Counterexample
Consider a path of 3 vertices $1 - 2 - 3$ ($L = \{1, 3\}, R = \{2\}$).
- Maximum matching size is $1$: either $M_1 = \{(1, 2)\}$ (exposing $3$) or $M_2 = \{(3, 2)\}$ (exposing $1$).
- Vertex $2$ is matched in **every** maximum matching ($2 \notin \mathcal{E}$), while vertices $1$ and $3$ are exposed in $M_2$ and $M_1$ respectively ($\mathcal{E} = \{1, 3\}$).
- In `[JSOI2009] 游戏` (Variant A, P1 places token, P2 moves first):
  - If P1 places at $1$, P2 must move $1 \to 2$, then P1 moves $2 \to 3$, and P2 is trapped! So P1 wins by placing at $1$ or $3$ ($\mathcal{E} = \{1, 3\}$).
  - If P1 places at $2$, P2 moves $2 \to 1$, and P1 has no moves!
- **Broken Certificate Counterexample**: A common bug is claiming "a vertex $v$ is in every maximum matching iff $v$ is matched in the *single* matching $M^*$ returned by Dinic." In our $1 - 2 - 3$ example, Dinic returns $M_1 = \{(1, 2)\}$, where vertex $1$ is matched—yet vertex $1$ is **not** in every maximum matching because $M_2 = \{(3, 2)\}$ leaves $1$ exposed! You **must** run the residual BFS from $S$ and $T$ to find all vertices reachable via even alternating paths.

---

### 3.3 Grid Increment Games & The Chessboard Parity Invariant (`[SCOI2012] 奇怪的游戏`, `Luogu P5038`)

#### Step 1: Non-Graph Diagnostic Signal
Given an $N \times M$ grid ($N, M \le 40$) with initial non-negative integers $a_{i,j}$, each operation increments **two adjacent cells** by $+1$. Find the minimum number of operations to make all cells equal to some final value $X$ (or report `-1`).
- **Diagnostic Signal**: Each operation acts on a **domino** (one black cell and one white cell in the 2-coloring of the grid). Thus every operation increments both the Black sum and the White sum by exactly $+1$!

#### Step 2: Intermediate Algebraic Representation (Odd vs. Even Grid Dichotomy)
2-color the grid by $(i + j) \bmod 2$: let $B$ be the set of Black cells (size $n_B$, initial sum $S_B$) and $W$ be the set of White cells (size $n_W$, initial sum $S_W$). Suppose all cells reach final height $X \ge \max_{i,j} a_{i,j}$. Then cell $(i, j)$ must receive $d_{i,j}(X) = X - a_{i,j} \ge 0$ increments, and the total increments on Black must equal the total increments on White:
$$\sum_{(i,j) \in B} (X - a_{i,j}) = \sum_{(i,j) \in W} (X - a_{i,j}) \iff n_B X - S_B = n_W X - S_W \iff (n_B - n_W) X = S_B - S_W.$$

> [!IMPORTANT]
> **Theorem 3.2 (The Chessboard Parity Dichotomy — Cohort 2 Insight)**:
> 1. **Case 1: $N \cdot M$ is Odd ($n_B - n_W = 1$)**:
>    The equation $(n_B - n_W) X = S_B - S_W$ uniquely locks the **only possible target height**:
>    $$X = S_B - S_W.$$
>    If $X < \max_{i,j} a_{i,j}$ or `check(X)` fails, the answer is immediately `-1`; no binary search is possible or needed!
> 2. **Case 2: $N \cdot M$ is Even ($n_B = n_W$)**:
>    A solution can exist **only if** $S_B = S_W$ initially (otherwise output `-1`). When $S_B = S_W$, **Monotonicity** holds: if target height $X$ is feasible, then $X + 1$ is also feasible!
>    *Proof of Monotonicity*: Any even $N \times M$ grid admits a **perfect domino tiling** (since at least one of $N, M$ is even, partition each even-length row or column into $1 \times 2$ dominoes). Adding $+1$ to every domino in the perfect tiling increments every cell in the grid by $+1$, lifting a valid solution for $X$ to a valid solution for $X + 1$! Thus we binary search $X \in [\max a_{i,j}, \infty)$.

#### Step 3: Mechanical Graph Compilation of `check(X)`
For a fixed $X \ge \max a_{i,j}$ satisfying $n_B X - S_B = n_W X - S_W =: K$:
- Build a bipartite flow network with Source $S$, Sink $T$:
  - For each Black cell $u \in B$: add edge $S \to u$ with capacity $X - a_u$.
  - For each White cell $v \in W$: add edge $v \to T$ with capacity $X - a_v$.
  - For each adjacent pair $(u, v)$ with $u \in B, v \in W$: add directed edge $u \to v$ with capacity $\infty$.
- `check(X)` returns `true` iff $\text{MaxFlow}(S, T) == K$, in which case the number of operations is $K$.

---

### 3.4 Adversarial Reachability & Barrier Cuts (`ARC 074 F`, `ABC 239 G`)

When an adversary blocks cells or vertices to prevent an agent from reaching $T$ from $S$:
1. **Row/Column Teleportation (`ARC 074 F - Lotus Leaves`, $H, W \le 100$)**:
   Jumping between any two leaves in the same row $r$ or column $c$ would naively create $O(HW(H+W))$ edges. Instead, introduce **Row Hubs** $R_1, \dots, R_H$ and **Column Hubs** $C_1, \dots, C_W$ (indestructible $\implies$ unsplit). Each destructible leaf at $(r, c)$ becomes a single undirected edge (or two directed edges of capacity $1$) between $R_r$ and $C_c$! Thus cutting a leaf is **an edge cut on the bipartite Row-Column incidence graph** of size $H + W \le 200$ vertices!
2. **Vertex-Split Constructive Recovery Trap (`ABC 239 G - Builder Takahashi`)**:
   Each vertex $v \in \{2, \dots, N-1\}$ with wall-building cost $c_v$ is split into $v_{\text{in}} \xrightarrow{c_v} v_{\text{out}}$, while each graph edge $(u, v)$ becomes $u_{\text{out}} \xrightarrow{\infty} v_{\text{in}}$ and $v_{\text{out}} \xrightarrow{\infty} u_{\text{in}}$.
   - **Broken Recovery Fallacy (Cohort 1 & 2 Shared Warning)**: Never output all vertices $v$ whose internal edge $v_{\text{in}} \to v_{\text{out}}$ is saturated ($f(v_{\text{in}}, v_{\text{out}}) = c_v$)! A saturated edge can lie completely inside the $S$-component or $T$-component if a bottleneck downstream blocks the path.
   - **Correct Recovery Rule**: Let $R_S$ be the set of vertices reachable from $S_{\text{out}}$ in the final residual graph. Output $v$ if and only if
     $$v_{\text{in}} \in R_S \quad \text{and} \quad v_{\text{out}} \notin R_S.$$

---

## 4. Iteration 48 & 100 Reconciled: Cross-Domain Bridge II — Computational Geometry (Rectilinear Polygon Partitioning, Dual Border MIS, and Minkowski Barrier Cuts)

### 4.1 Minimum Rectangle Partition of a Rectilinear Polygon (`Imai–Asano 1986`, `Lipski et al. 1979`, `UVa 1711`)

#### Step 1: Non-Graph Diagnostic Signal
Given an orthogonal (rectilinear) polygon $P$ with $N$ axis-aligned edges and $h$ rectilinear interior holes, partition the interior of $P$ into the **minimum number $R_{\min}$ of interior-disjoint rectangles** using axis-aligned cuts.
- **Why Geometric Sweep-Line Greedy Fails**: Every reflex ($270^\circ$ interior angle) vertex must have at least one axis-aligned cut segment emanating from it to resolve its non-convexity. Whenever a single cut segment connects **two** reflex vertices (an **effective chord**), it resolves **both** reflex angles simultaneously and reduces the total rectangle count by $1$! Choosing a horizontal chord between two reflex vertices blocks vertical chords that cross it, turning optimal chord selection into a **Maximum Independent Set on a Bipartite Intersection Graph**.

---

### 4.2 Step 2: Reconciling the Euler–Reflex Formula & the Famous $\pm h$ Literature Discrepancy

In competitive programming blogs and computational geometry papers, two seemingly contradictory formulas appear for the minimum number of rectangles $R_{\min}$:
- **Formula A (Reflex-Count Form)**: $R_{\min} = 1 - h + c_{\text{conc}} - |I^*|$, where $c_{\text{conc}}$ is the number of reflex ($270^\circ$) vertices.
- **Formula B (Total-Vertex Form)**: $R_{\min} = \frac{N}{2} - 1 + h - |I^*|$, where $N = c_{\text{conv}} + c_{\text{conc}}$ is the total number of vertices.

Why does Formula A have $-h$ while Formula B has $+h$? Cohort 1 proved Formula A via Euler's Planar Characteristic, while Cohort 2 proved their equivalence via the $90^\circ$ Corner Double-Counting Identity. We present the complete synthesis below.

> [!IMPORTANT]
> **Theorem 4.1 (Unified Rectilinear Polygon Partition Theorem — Euler & Corner Double-Counting Synthesis)**:
> Let $P$ be a rectilinear polygon with $h$ rectilinear holes, $c_{\text{conv}}$ convex ($90^\circ$ interior) vertices, $c_{\text{conc}}$ reflex/concave ($270^\circ$ interior) vertices, and $N = c_{\text{conv}} + c_{\text{conc}}$ total vertices. Let $G_{\text{chord}} = (V_H \cup V_V, E_{\text{cross}})$ be the intersection graph of all horizontal ($V_H$) and vertical ($V_V$) internal chords connecting pairs of reflex vertices, and let $I^*$ be a maximum subset of mutually **non-intersecting** (and endpoint-disjoint) chords. Then the minimum number of rectangles in any partition of $P$ is:
> $$R_{\min} = 1 - h + c_{\text{conc}} - |I^*| = \frac{N}{2} - 1 + h - |I^*|.$$

#### Proof 1: The $90^\circ$ Interior Corner Double-Counting Proof (Cohort 2 Formulation)
Suppose $P$ is partitioned into $R$ rectangles using $k = |I|$ mutually disjoint reflex-to-reflex chords and $c_{\text{conc}} - 2k$ single-reflex rays (each starting at one of the remaining $c_{\text{conc}} - 2k$ reflex vertices and terminating T-junction style on a boundary or chord segment). Notice that no cut segments are allows to cross (any crossing can be eliminated by stopping one segment at the other as a T-junction). Let us count the total number of **$90^\circ$ interior corners** across all $R$ rectangles in two ways:
1. **By Rectangles**: Each of the $R$ rectangles has $4$ corners of $90^\circ$, so the total number of $90^\circ$ corners is **$4R$**.
2. **By Vertices & Cut Endpoints**:
   - Every convex polygon vertex ($90^\circ$) contributes **$1$** corner: total $c_{\text{conv}}$.
   - Every reflex polygon vertex ($270^\circ$) has at least one cut segment incident to it, splitting the $270^\circ$ angle into $90^\circ + 180^\circ$. What happens to that $180^\circ$ side, and what happens at the other end of each cut segment?
     - Each of the $k$ **reflex-to-reflex chords** splits **two** reflex $270^\circ$ angles into $90^\circ + 180^\circ$ (if a single chord hits a reflex vertex, its $180^\circ$ side is flat unless split by a perpendicular chord, which is accounted for below), creating **$2$** new $90^\circ$ corners at its two reflex endpoints (total $2 \times 2k = 4k$ corners at the $2k$ reflex vertices incident to chords).
     - Each of the $c_{\text{conc}} - 2k$ **single-reflex rays** creates **$2$** corners of $90^\circ$ at its reflex origin (Wait: at its reflex origin it splits $270^\circ \to 90^\circ + 180^\circ$, giving $1$ corner at the origin, PLUS at its T-junction landing point on a flat $180^\circ$ edge/chord it splits $180^\circ \to 90^\circ + 90^\circ$, giving **$2$** new $90^\circ$ corners! And if a second perpendicular ray starts at the same reflex origin to split the remaining $180^\circ \to 90^\circ + 90^\circ$, that is equivalent in corner count!). Specifically, every cut segment (chord or ray) splits angles at its two endpoints:
       - At a reflex endpoint: increases the count of $90^\circ$ corners from $0$ to $1$ (first segment) or from $1$ to $3$ (second perpendicular segment, $+2$).
       - At a T-junction interior endpoint: splits a $180^\circ$ flat boundary into two $90^\circ$ corners ($+2$).
     - Summing over all $c_{\text{conc}}$ reflex vertices resolved by $k$ reflex-to-reflex chords and $c_{\text{conc}} - 2k$ T-junction rays:
       - Each of the $2k$ chord-resolved reflex vertices contributes $1$ corner (if $1$ chord) $\implies 2k$ corners? Wait—at a reflex vertex of $270^\circ$, **one** chord leaves a $90^\circ$ angle and a $180^\circ$ flat wall! A $180^\circ$ flat wall is just the side of a rectangle, NOT a corner! So resolving a $270^\circ$ reflex vertex with **one** chord turns it into **one** $90^\circ$ corner and one $180^\circ$ flat side!
       - Therefore:
         - The $c_{\text{conv}}$ convex vertices contribute $1$ corner each: $+c_{\text{conv}}$.
         - The $c_{\text{conc}}$ reflex vertices, once each has at least one incident cut segment, contribute $1$ corner each: $+c_{\text{conc}}$ (if a reflex vertex has *two* perpendicular segments, the second segment acts like a T-junction splitting its $180^\circ$ side into two $90^\circ$ corners, $+2$).
         - Every T-junction endpoint (there are $c_{\text{conc}} - 2k$ of them) splits a $180^\circ$ flat wall into two $90^\circ$ corners: $+2(c_{\text{conc}} - 2k)$.
       - Total $90^\circ$ corners:
         $$4R = c_{\text{conv}} + c_{\text{conc}} + 2(c_{\text{conc}} - 2k) = c_{\text{conv}} + 3c_{\text{conc}} - 4k.$$
3. **Applying the Polygon Exterior Angle Sum Identity**:
   - The outer boundary of $P$ turns by $+90^\circ$ at convex vertices and $-90^\circ$ at reflex vertices, summing to $+360^\circ = 4 \times 90^\circ$.
   - Each of the $h$ interior holes (oriented clockwise around the interior of $P$) turns by $-360^\circ = -4 \times 90^\circ$.
   - Therefore:
     $$c_{\text{conv}} - c_{\text{conc}} = 4 - 4h \iff c_{\text{conv}} = c_{\text{conc}} + 4 - 4h.$$
   - Substituting $c_{\text{conv}} = c_{\text{conc}} + 4 - 4h$ into $4R = c_{\text{conv}} + 3c_{\text{conc}} - 4k$:
     $$4R = (c_{\text{conc}} + 4 - 4h) + 3c_{\text{conc}} - 4k = 4 - 4h + 4c_{\text{conc}} - 4k \implies R = 1 - h + c_{\text{conc}} - k.$$
   - Or, since $N = c_{\text{conv}} + c_{\text{conc}} = 2c_{\text{conc}} + 4 - 4h \implies c_{\text{conc}} = \frac{N}{2} - 2 + 2h$:
     $$R = 1 - h + \left(\frac{N}{2} - 2 + 2h\right) - k = \frac{N}{2} - 1 + h - k.$$
   Maximizing $k = |I|$ over independent chord sets $I$ minimizes $R$. $\blacksquare$

#### Proof 2: Planar Graph Euler Characteristic Invariant $F - C$ (Cohort 1 Formulation)
View the boundary of $P$ as $1 + h$ disjoint cycles ($C_0 = 1 + h$ connected components, $F_0 = 1$ interior face, so $F_0 - C_0 = -h$). Each time we add a non-crossing segment connecting two points on the current boundary/cut network:
- Let $\Delta V_{\text{new}} \in \{0, 1, 2\}$ be the number of endpoints of the segment that land in the interior of existing edges (T-junctions) rather than at existing vertices; the segment splits $\Delta V_{\text{new}}$ existing edges, so $\Delta E - \Delta V = 1$ always!
- By Euler's Planar Formula $V - E + F_{\text{int}} - C = 0 \implies \Delta(F_{\text{int}} - C) = \Delta E - \Delta V = +1$ for **every** added cut segment!
- At the end of the partition, the boundary + cut network is a single connected planar graph ($C_{\text{final}} = 1$, assuming each hole is touched by at least one cut from its own reflex vertices) with $F_{\text{int}} = R$ rectangles, so $F_{\text{final}} - C_{\text{final}} = R - 1$.
- Since we started at $F_0 - C_0 = -h$ and added $S = k + (c_{\text{conc}} - 2k) = c_{\text{conc}} - k$ total cut segments (each increasing $F - C$ by $+1$):
  $$R - 1 = -h + (c_{\text{conc}} - k) \implies R = 1 - h + c_{\text{conc}} - k. \quad \blacksquare$$

---

### 4.3 Step 3 & 4: Mechanical Graph Compilation & The Endpoint-Sharing Non-Disjointness Trap

1. **Chord Extraction**:
   - Group reflex vertices by $y$-coordinate to find all horizontal internal chords $V_H$ (segments $[x_1, x_2] \times \{y\}$ between two reflex vertices facing each other across the interior of $P$, with no boundary obstacle strictly between them).
   - Group reflex vertices by $x$-coordinate to find all vertical internal chords $V_V$ (segments $\{x\} \times [y_1, y_2]$).
2. **Intersection Bipartite Graph $G_{\text{chord}} = (V_H \cup V_V, E_{\text{cross}})$**:
   - No two horizontal chords can intersect, and no two vertical chords can intersect (assuming general position where no three reflex vertices are collinear along the same open chord).
   - Add an undirected conflict edge $(h, v) \in V_H \times V_V$ if and only if horizontal chord $h = [x_1, x_2] \times \{y_h\}$ and vertical chord $v = \{x_v\} \times [y_1, y_2]$ **intersect Either in their interiors OR at a shared reflex endpoint**:
     $$x_1 \le x_v \le x_2 \quad \text{and} \quad y_1 \le y_h \le y_2.$$

> [!CAUTION]
> **Broken Gadget Counterexample (The Collinear / Endpoint-Sharing Trap — Cohort 2 Audit)**:
> Can we select **both** a horizontal chord $h$ and a vertical chord $v$ that share a common reflex vertex $u$?
> **NO!** Recall from Proof 1 & Proof 2 that each reflex vertex $u$ has only **one** $270^\circ$ reflex angle to resolve:
> - The first chord incident to $u$ resolves $u$'s reflexity ($270^\circ \to 90^\circ + 180^\circ$) and saves $1$ T-junction ray.
> - Once $u$ has that first chord, the remaining angle at $u$ is $180^\circ$ (convex/flat!). A second perpendicular chord starting at $u$ acts just like a T-junction ray splitting $180^\circ \to 90^\circ + 90^\circ$—it does **not** save an additional rectangle!
> Therefore, in $G_{\text{chord}}$, the intersection condition **must use non-strict inequalities** ($x_1 \le x_v \le x_2$ and $y_1 \le y_h \le y_2$) so that a horizontal chord and a vertical chord sharing a reflex endpoint $u$ are connected by a conflict edge and cannot both be chosen in $I^*$!

3. **Compile to Hopcroft–Karp / Dinic**:
   By Kőnig's Theorem on $G_{\text{chord}}$:
   $$|I^*| = |V_H| + |V_V| - \nu(G_{\text{chord}}), \qquad R_{\min} = 1 - h + c_{\text{conc}} - \big(|V_H| + |V_V| - \nu(G_{\text{chord}})\big).$$

---

### 4.4 Dual Shared-Border Unit-Segment Cover (`CF 1404 E - Bricks`) & Minkowski Barrier Cuts (`[BOI 2002] Escape`)

1. **Grid Brick Partition via Dual Shared-Border MIS (`CF 1404 E - Bricks`, $N, M \le 200$)**:
   Instead of partitioning a continuous polygon with chords of arbitrary length, suppose we are given an $N \times M$ binary grid of `#` cells ($K$ cells total) and want to partition the `#` cells into the minimum number of $1 \times L$ or $L \times 1$ bricks.
   - **Step 1 & 2 (Dual Transformation)**: Merging two horizontally adjacent `#` cells across their shared vertical unit border $v$ reduces the brick count by $1$; merging two vertically adjacent `#` cells across their shared horizontal unit border $h$ also reduces the brick count by $1$. Starting from $K$ isolated $1 \times 1$ bricks, selecting $k$ valid shared unit borders leaves **$R = K - k$** bricks!
   - **Step 3 (Corner Conflict Condition)**: No cell can be simultaneously part of a horizontal brick ($1 \times L$) and a vertical brick ($L \times 1$). Therefore, a horizontal unit border $h$ and a vertical unit border $v$ conflict if and only if they are **both incident to the same `#` cell** (i.e., they meet at one of the $4$ corners of that `#` cell). Since $V_H$ (horizontal merges) and $V_V$ (vertical merges) only conflict with each other, the conflict graph is **bipartite**, and $R_{\min} = K - \big(|V_H| + |V_V| - \nu(G_{\text{border}})\big)$.
2. **Continuous-to-Discrete Barrier Cuts & Minkowski Sum Inflation (`[BOI 2002] Escape`)**:
   By **Planar Topological Duality**, an agent of radius $r \ge 0$ can navigate from $y = 0$ (Bottom) to $y = W$ (Top) through a field of obstacles $O_1, \dots, O_N$ if and only if there is no continuous barrier chain of obstacles connecting the Left boundary ($x = 0$) to the Right boundary ($x = L$).
   - **Minkowski Sum Inflation**: A circular agent of radius $r$ avoids colliding with obstacle $O_i$ iff the center of the agent stays outside the inflated obstacle $O'_i = O_i \oplus B_r$. Two obstacles $O_i, O_j$ block the agent from passing between them iff $\text{dist}(O_i, O_j) < 2r$ (or $\le 2r$).
   - If the problem asks for the **minimum number of guards/sensors to destroy** (where each guard $i$ has detection radius $R$ and destruction cost $c_i$, as in `[BOI 2002] Escape`), build the **Obstacle Overlap Graph**:
     - Split each guard $i$ into $i_{\text{in}} \xrightarrow{c_i} i_{\text{out}}$.
     - Connect $S$ (Top wall $y = W$) to $i_{\text{in}}$ with capacity $\infty$ if $W - y_i \le R$.
     - Connect $i_{\text{out}}$ to $T$ (Bottom wall $y = 0$) with capacity $\infty$ if $y_i \le R$.
     - Connect $i_{\text{out}} \xrightarrow{\infty} j_{\text{in}}$ and $j_{\text{out}} \xrightarrow{\infty} i_{\text{in}}$ if $(x_i - x_j)^2 + (y_i - y_j)^2 \le (2R)^2$.
     The $S$-$T$ Minimum Cut equals the minimum cost to breach every Top-to-Bottom sensor barrier!


---

## 5. Iteration 49 & 101 Reconciled: Cross-Domain Bridge III — String Automata, Matroid Basis Exchange, and Number-Theoretic Graphs

### 5.1 String Substring Posets, Aho–Corasick Jump Tables, and Weighted Dilworth Antichains (`CF 590 E`, `ABC 354 G`)

#### Step 1: Non-Graph Diagnostic Signal
Given $N$ strings $s_1, \dots, s_N$ (with weights $w_i > 0$, or $w_i = 1$), select a maximum-weight (or maximum-cardinality) subset of strings such that **no selected string is a substring of another selected string**.
- **Step 2 (Poset & Dilworth Formulation)**: Deduplicate identical strings first (keeping the maximum weight $w_i$ if duplicates cannot both be chosen). Then the substring relation $s_i \sqsubseteq s_j$ (meaning $s_i$ occurs as a contiguous substring of $s_j$) forms a strict Partial Order (DAG) $(P, \prec)$. A subset of pairwise non-substring strings is an **Antichain** of $(P, \prec)$!

#### Step 3: Reconciling Unweighted Large-Length (`CF 590 E`) vs. Weighted Poset (`ABC 354 G`)
Cohort 1 and Cohort 2 analyzed two complementary regimes of Substring Antichains:

1. **Unweighted Substring Poset with Huge Total Length (`CF 590 E - Birthday`, $N \le 750, \sum |s_i| \le 10^7$)**:
   - **The $O(N \sum |s_i|)$ Bottleneck**: If we walk the Aho–Corasick fail tree upward from every prefix node of $s_j$ to find all $s_i \sqsubset s_j$, a deep fail tree of height $10^7$ takes $O(\sum |s_i|)$ per step, TLEing!
   - **Compressed-Link Jump Table**: During BFS construction of the Aho–Corasick automaton, maintain for each trie state $u$ the pointer `nearest_word[u]` to the longest dictionary string ending at $u$ or an ancestor of $u$ in the fail tree:
     $$\text{nearest\_word}[u] = \begin{cases} \text{id}(u) & \text{if } u \text{ is the terminal node of some } s_k, \\ \text{nearest\_word}[\text{fail}[u]] & \text{otherwise}. \end{cases}$$
   - When scanning the prefixes $v$ of $s_j$, we only add one directed edge per prefix: from $j$ to $\text{nearest\_word}[v]$ (or $\text{nearest\_word}[\text{fail}[v]]$ at the terminal node of $s_j$ itself, to avoid self-loops!). This collects all **immediate** substring predecessors of $s_j$ in $O(\sum |s_i|)$ total time!
   - Next, compute the full transitive closure of this $N$-vertex DAG in $O(N^3 / 64)$ time using `std::bitset<750>`, and run Hopcroft–Karp + Kőnig Minimum Vertex Cover recovery ($I^* = \{i : i_L \in R_S \land i_R \notin R_S\}$).

2. **Weighted Substring Poset (`ABC 354 G - Select Strings`, $N \le 100, w_i \ge 1$) — Transitive Closure vs. The $u_R \xrightarrow{\infty} u_L$ Bypass Gadget**:
   How do we compute a **Maximum-Weight Antichain** on a poset $(V, \prec)$? We want to maximize $\sum_{u \in V} w_u (1 - z_u)$, or equivalently minimize the **Minimum-Weight Vertex Cover** $\sum_{u \in V} w_u (x_{u,L} + y_{u,R})$ on the split bipartite graph where each comparability $u \prec v$ requires $x_{u,L} + y_{v,R} \ge 1$.
   - **What if both $x_{u,L} = 1$ and $y_{u,R} = 1$ are cut for the same vertex $u$?** That would charge $2w_u$ instead of $w_u$ for deleting $u$! Cohort 1 and Cohort 2 resolved this via two distinct, both valid mechanisms:

> [!IMPORTANT]
> **Theorem 5.1 (Equivalence of Transitive Closure and the $u_R \xrightarrow{\infty} u_L$ Bypass Gadget for Weighted Dilworth Antichains)**:
> Build the split network where each $u \in V$ has two nodes $u_L, u_R$ with terminal edges $S \xrightarrow{w_u} u_L$ and $u_R \xrightarrow{w_u} T$, and each comparability edge $(u, v)$ has an infinite-capacity edge $u_L \xrightarrow{\infty} v_R$.
> 1. **Method A (Full Transitive Closure — Cohort 1 Proof)**: If we materialize **all** transitive edges $u_L \xrightarrow{\infty} v_R$ for $u \prec v$, then in any minimal $S$-$T$ cut, $S \to u_L$ and $u_R \to T$ are **never both cut**.
>    *Proof*: Suppose both $S \to u_L$ and $u_R \to T$ are cut. For $S \to u_L$ to be essential to the cut, there must exist some $v \succ u$ such that $v_R \to T$ is **not** cut ($v_R$ can reach $T$). For $u_R \to T$ to be essential, there must exist some $a \prec u$ such that $S \to a_L$ is **not** cut ($S$ can reach $a_L$). By transitivity, $a \prec u \prec v \implies a \prec v$, so the transitive edge $a_L \xrightarrow{\infty} v_R$ is present, creating an uncut path $S \to a_L \xrightarrow{\infty} v_R \to T$! Contradiction!
> 2. **Method B (Sparse-DAG $u_R \xrightarrow{\infty} u_L$ Bypass Gadget — Cohort 2 Proof)**: What if we only add Hasse/sparse DAG edges $u_L \xrightarrow{\infty} v_R$ for $(u, v) \in E$ AND add a **reverse internal bypass edge $u_R \xrightarrow{\infty} u_L$** for every $u \in V$?
>    *Proof*: With $u_R \xrightarrow{\infty} u_L$ present, any path $a_L \xrightarrow{\infty} u_R \xrightarrow{\infty} u_L \xrightarrow{\infty} v_R$ automatically propagates reachability through $u$ whenever neither $S \to a_L$ nor $v_R \to T$ is cut! Thus the bypass edges $u_R \xrightarrow{\infty} u_L$ simulate the entire transitive closure in $O(|V| + |E_{\text{sparse}}|)$ edges without needing $O(|V|^2)$ transitive edges, and cutting either $S \to u_L$ or $u_R \to T$ (or putting $u_L, u_R$ together on the $S$-side or $T$-side) is impossible to double-count!

```
   Method B (Sparse-DAG Bypass Gadget for Weighted Dilworth):
   S ---(w_a)---> [a_L] ===(inf)===> [u_R] ---(w_u)---> T
                                       ||
                                     (inf)  <-- Reverse Bypass u_R -> u_L!
                                       vv
   S ---(w_u)---> [u_L] ===(inf)===> [v_R] ---(w_v)---> T
```

---

### 5.2 Matroid Basis Exchange & Inverse Minimum Spanning Tree (`Bruhat–Hall` Bijection, `[SHOI2004]` vs. `[BJWC2018]`)

#### 1. The Bruhat–Hall Strong Basis Bijection Theorem (Cohort 1 Insight)
Given two bases $B_1, B_2$ of any matroid $\mathcal{M} = (U, \mathcal{I})$ of rank $r$, define the **Bipartite Basis Exchange Graph** $G_{\text{ex}}(B_1, B_2) = (B_1, B_2, E_{\text{ex}})$, where $(x, y) \in B_1 \times B_2$ is an edge iff $(B_1 \setminus \{x\}) \cup \{y\} \in \mathcal{I}$ (equivalently, $x$ lies in the fundamental circuit $C(B_1, y)$).

> [!IMPORTANT]
> **Theorem 5.2 (Bruhat 1969 — Perfect Matching in Matroid Basis Exchange Graphs)**:
> For any two bases $B_1, B_2$ of a matroid $\mathcal{M}$, the bipartite exchange graph $G_{\text{ex}}(B_1, B_2)$ has a **perfect matching**.
> *Proof via Hall's Marriage Theorem & Submodularity of Rank*: Take any subset $Y \subseteq B_2$, and let $N(Y) \subseteq B_1$ be the set of neighbors of $Y$ in $G_{\text{ex}}(B_1, B_2)$. For every $x \in B_1 \setminus N(Y)$ and every $y \in Y$, $x \notin C(B_1, y)$, which means $B_1 \setminus N(Y)$ is independent of $Y$ in the sense that every $y \in Y$ is spanned by $N(Y)$: $Y \subseteq \text{span}(N(Y))$. Since $Y \subseteq B_2$ is an independent set contained in $\text{span}(N(Y))$, matroid rank monotonicity gives:
> $$|Y| = \text{rank}(Y) \le \text{rank}(\text{span}(N(Y))) = \text{rank}(N(Y)) = |N(Y)|.$$
> By Hall's Marriage Theorem, $G_{\text{ex}}(B_1, B_2)$ admits a perfect matching! $\blacksquare$

#### 2. Inverse MST Dichotomy: $L_1$ LP Dual (`[SHOI2004]`) vs. $L_2$ Isotonic Regression (`[BJWC2018]`)
Given an undirected graph $G = (V, E)$ with initial edge weights $w_e$ and cost multipliers $c_e$ (cost $c_e |w'_e - w_e|^p$ to change weight $w_e \to w'_e$), modify the weights so that a target spanning tree $T \subseteq E$ becomes a Minimum Spanning Tree (MST).
- **Step 2 (Fundamental Cycle Optimality Condition)**: $T$ is an MST under $w'$ iff for every non-tree edge $f = (u, v) \notin T$ and every tree edge $e \in P_T(u, v)$ on the unique tree path between $u$ and $v$:
  $$w'_e \le w'_f.$$
- **Regime A: $L_1$ Norm ($p = 1$, `[SHOI2004] 最小生成树`, `Luogu P2538`)**:
  Tree edges $e \in T$ only ever decrease ($w'_e = w_e - x_e, x_e \ge 0$) and non-tree edges $f \notin T$ only ever increase ($w'_f = w_f + y_f, y_f \ge 0$). For every pair $(e, f)$ with $e \in P_T(f)$ and $w_e > w_f$, define the violation gap $\Delta_{e,f} = w_e - w_f > 0$. Then:
  $$\min_{x, y \ge 0} \sum_{e \in T} c_e x_e + \sum_{f \notin T} c_f y_f \quad \text{s.t.} \quad x_e + y_f \ge \Delta_{e,f} \;\;\forall e \in P_T(f).$$
  Taking the **LP Dual** with dual flow variable $z_{e,f} \ge 0$ for each pair $(e, f)$ with $e \in P_T(f)$:
  $$\max_{z \ge 0} \sum_{e \in T, f \notin T} \Delta_{e,f} z_{e,f} \quad \text{s.t.} \quad \sum_{f : e \in P_T(f)} z_{e,f} \le c_e \;\;(\forall e \in T), \quad \sum_{e \in P_T(f)} z_{e,f} \le c_f \;\;(\forall f \notin T).$$
  This is a **Maximum-Weight Bipartite Matching / Min-Cost Flow** problem on the bipartite graph $(T, E \setminus T)$! (When $c_e = c_f = 1$, it is standard Kuhn–Munkres / Hungarian Assignment!)
- **Regime B: $L_2$ Norm ($p = 2$, `[BJWC2018] 最小生成树`)**:
  Quadratic costs $(w'_e - w_e)^2$ cannot be dualized to linear assignment; instead, build the bipartite DAG of order constraints $w'_e \le w'_f$ ($e \to f$ for $e \in P_T(f)$) and run **$L_2$ Isotonic Regression via `整体二分`** (§2)!

---

### 5.3 Number-Theoretic Graphs: Divisibility Posets, Prime-Omega Parity, and Gaussian Integer Valuations

Number-theoretic constraints disguise clean bipartite graphs and DAG closures behind arithmetic predicates. The table below synthesizes all four canonical Number-Theoretic Flow archetypes audited across Cohort 1 and Cohort 2:

| Archetype & Representative Problem | Arithmetic Predicate between $i, j$ | Structural Graph Property | Mechanical Flow / Matching Compilation |
| :--- | :--- | :--- | :--- |
| **1. Divisibility Closure (`ARC 085 E - MUL`)** | Choosing index $i$ requires choosing all multiples $k \cdot i$ (or destroying $i$ destroys $k \cdot i$). | Directed Acyclic Poset $(i \mid j)$ on $\{1, \dots, N\}$ with $O(N \log N)$ edges. | **Max-Weight Closure (`燃やす埋める`)**: Keep $i$ ($x_i=1$) forces keep $k i$ ($x_{ki}=1$) via $i \xrightarrow{\infty} ki$. |
| **2. Prime-Factor Quotient Pairing (`[SDOI2016] 数字配对`, `Luogu P4068`)** | Pair $a_i, a_j$ if $a_j / a_i = p$ is prime, earning value $c_i c_j$. | Let $\Omega(n) = \sum_{p^k \parallel n} k$ be total prime factors with multiplicity. Any valid edge changes $\Omega$ by $\pm 1 \implies$ **Bipartite by $\Omega(a_i) \bmod 2$**! | **Positive-Cost Stopping MCMF**: Split by $\Omega(a_i) \bmod 2$; augment shortest paths in decreasing order of gain until path gain $< 0$, then fractionally truncate the last augmentation. |
| **3. Prime-Wise GCD Operations (`CF 498 C - Array and Operations`)** | Given good pairs $(i, j)$ with $i + j$ odd, divide $a_i, a_j$ by common prime $p \mid \gcd(a_i, a_j)$. | Exponents of distinct primes $p_1 \neq p_2$ never interact! Graph is already **bipartite by index parity $i \bmod 2$**. | **Prime-Wise Independent Max-Flow**: For each distinct prime $p \mid \prod a_i$ ($\le 900$ primes), run Dinic with vertex capacities $v_p(a_i)$. |
| **4. Forbidden Euclidean Distance $\sqrt{D}$ (`AGC 025 D - Choosing Points`)** | Select $N^2$ points in $2N \times 2N$ grid with no pair at squared distance $D_1$ or $D_2$. | Factor $D = 2^k m$ ($m$ odd). In $\mathbb{Z}[i]$, $2 = -i(1+i)^2$. Rotating/scaling by $(1+i)^{-k}$ reduces to $m$ odd, where $\Delta x^2 + \Delta y^2 = m \implies \Delta x + \Delta y$ is odd $\implies$ **Bipartite**! | **Product Bipartite 4-Coloring**: Every distance graph $G(D)$ is bipartite (2-colorable in $O(N^2)$). Overlay the two 2-colorings $(c_1(p), c_2(p)) \in \{0,1\}^2$; by Pigeonhole, one of the $4$ color classes has size $\ge \frac{4N^2}{4} = N^2$! (No Dinic needed!) |

---

## 6. Iteration 50–52 & 102–104 Reconciled: Exhaustive Tri-Lingual (`[ZH]` / `[JA]` / `[EN]`) Literature & Problem Archive Audit

### 6.1 Complete Reconciled Master Table of the Chinese "24 Network Flow Problems" (`网络流 24 题`, `LOJ 6000–6023`)

Cohort 1 and Cohort 2 both audited `网络流 24 题`, and Cohort 2 caught a critical historical fact: **4 of the 24 problems (`#10`, `#17`, `#22`, and `#24`) are NOT network flow problems at all** (they were bundled into the early 2000s training suite as graph/search/DP companions)! The table below provides the definitive, reconciled `LOJ 6000–6023` / `Luogu` reference, modern classification, and edge-case traps.

| # | LOJ ID | Luogu ID | Chinese Title & English Translation | Canonical Modern Classification | Key Structural Gadget & Degenerate Traps |
| :-: | :---: | :---: | :--- | :--- | :--- |
| **01** | `6000` | `P2756` | `飞行员配对方案问题` (Pilot Pairing) | **Quarantined Template (`R-01`)**: Unweighted Bipartite Matching | Standard $S \to L \to R \to T$ unit network. |
| **02** | `6001` | `P2762` | `太空飞行计划问题` (Space Flight Plan) | **Max-Weight Closure (`燃やす埋める` / Project Selection)** | Experiment $i \in S$ forces equipment $j \in S$ ($i \xrightarrow{\infty} j$). **Trap**: Read line-terminated input carefully; recover via residual BFS $R_S$, NOT saturated edges! |
| **03** | `6002` | `P2764` | `最小路径覆盖问题` (Minimum Path Cover) | **DAG Minimum Disjoint Path Cover** | $N - \nu(G_{\text{split}})$ where each merge $u_L \to v_R$ decreases path count by $1$. |
| **04** | `6003` | `P2765` | `魔术球问题` (Magic Ball Problem) | **Incremental DAG Path Cover (`u < v, u+v = k^2`)** | Add $n = 1, 2, \dots$ incrementally and augment existing residual network until $n - \text{flow} > K$. |
| **05** | `6004` | `P3254` | `圆桌问题` (Round Table Problem) | **Quarantined Template (`R-02`)**: Bipartite Multi-Matching | Delegation $i$ ($S \xrightarrow{r_i} i$) to table $j$ ($j \xrightarrow{c_j} T$) via cap-$1$ edge. |
| **06** | `6005` | `P2766` | `最长不下降子序列问题` (LIS Disjoint Paths) | **Layered DP DAG + Vertex-Split Max-Flow** | Precompute $dp[i]$; keep edges with $i < j, a_i \le a_j, dp[j]=dp[i]+1$. **Critical Trap**: When max LIS length $L = 1$, freeing endpoints $1$ and $N$ to capacity $\infty$ creates a direct $S \to 1_{\text{in}} \to 1_{\text{out}} \to T$ path of capacity $\infty$! Handle $L = 1 \implies \text{ans} = N$ separately! |
| **07** | `6006` | `P2763` | `试题库问题` (Test Question Bank) | **Quarantined Template (`R-03`)**: Bipartite Multi-Assignment | Category quotas on sink edges; question capacities $= 1$. |
| **08** | `6007` | `P2774` | `方格取数问题` (Grid Number Selection) | **Grid Parity Bipartite MWIS** (`P07`) | 2-color by $(r+c)\bmod 2$; $\sum w - \text{MinCut}$. |
| **09** | `6008` | `P1251` | `餐巾计划问题` (Napkin Planning) | **Daily Split-Node Supply/Demand MCMF** | Split day $i$ into dirty supply $i_{\text{dirty}}$ ($S \to i_{\text{dirty}}$) and clean demand $i_{\text{clean}}$ ($i_{\text{clean}} \to T$); fast/slow laundry transitions $i_{\text{dirty}} \to (i+d)_{\text{clean}}$. |
| **10** | `6009` | `P2761` | `软件补丁问题` (Software Patches) | **NON-FLOW TRAP #1**: Bitmask Dijkstra ($2^{20}$ states) | State is 20-bit bug mask; no flow involved! |
| **11** | `6010` | `P4016` | `负载平衡问题` (Load Balancing) | **Quarantined Template (`R-04`)**: Circular Transshipment / Median | Solved in $O(N \log N)$ via prefix-sum median $\sum |S_i - \text{med}|$ (or MCMF). |
| **12** | `6011` | `P4015` | `运输问题` (Transportation Problem) | **Quarantined Template (`R-05`)**: Bipartite Hitchcok MCMF | Run once with $+c_{ij}$ and once with $-c_{ij}$ (restore capacities between runs!). |
| **13** | `6012` | `P4014` | `分配问题` (Assignment Problem) | **Quarantined Template (`R-06`)**: Bipartite Min/Max Assignment | Unit-capacity version of `#12`. |
| **14** | `6013` | `P4013` | `数字梯形问题` (Number Trapezoid) | **3-Rule Vertex/Edge Disjoint Path MCMF** | Rule 1: vertex+edge disjoint ($v_{\text{in}} \xrightarrow{1} v_{\text{out}}$, edges cap $1$). Rule 2: vertex overlap allowed ($v_{\text{in}} \xrightarrow{\infty} v_{\text{out}}$, edges cap $1$). Rule 3: both overlap allowed (both cap $\infty$). |
| **15** | `6014` | `P3358` | `最长k可重区间集问题` (Max $k$-Interval Set) | **Coordinate-Compressed Interval Line MCMF** | Discretize endpoints $1..M$; backbone $x \xrightarrow{k, 0} x+1$; interval $[l_i, r_i]$ adds $l_i \xrightarrow{1, -w_i} r_i$. |
| **16** | `6015` | `P2754` | `家园 / 星际转移问题` (Home / Interstellar Transfer) | **Time-Expanded Layered Network (`时间分层图`)** | Increment $T = 1, 2, \dots$; add layer $V_T$, shuttle movement edges $(u, T-1) \to (v, T)$, and wait edges $(u, T-1) \to (u, T)$; check connectivity via DSU first! |
| **17** | `6016` | `P4011` | `孤岛营救问题` (Island Rescue) | **NON-FLOW TRAP #2**: Key-Bitmask 0-1 BFS / Dijkstra | Grid position $(r, c)$ + key bitmask $\in [0, 2^P)$. |
| **18** | `6017` | `P2770` | `航空路线问题` (Airline Routes) | **Bitonic Tour / 2 Vertex-Disjoint $1 \to N$ Paths MCMF** | Split $1_{\text{out}}$ (cap $2$), $N_{\text{in}}$ (cap $2$), internal $v_{\text{in}} \xrightarrow{1, -1} v_{\text{out}}$. **Trap**: Direct edge $(1, N)$ allows degenerate $1 \to N \to 1$ tour of size $2$ if no intermediate path exists. |
| **19** | `6018` | `P4012` | `深海机器人问题` (Deep Sea Robot) | **Grid Multi-Robot Specimen Collection MCMF** | Each grid edge has two parallel arcs: $(1, -w_e)$ (first traversal collects reward) and $(\infty, 0)$ (subsequent traversals free). |
| **20** | `6019` | `P3355` | `骑士共存问题` (Knight Coexistence) | **Knight-Move Parity Bipartite MIS** (`P08`) | Knight jump $(\pm 1, \pm 2)$ flips $(r+c)\bmod 2 \implies$ bipartite! |
| **21** | `6020` | `P3356` | `火星探险问题` (Mars Exploration) | **Rock-Collecting Grid MCMF + Path Reconstruction** | Same dual-arc gadget as `#19` on split vertices + DFS flow decomposition to trace rover moves. |
| **22** | `6021` | `P4009` | `汽车加油行驶问题` (Car Refueling) | **NON-FLOW TRAP #3**: Layered Fuel-State Dijkstra | State $(r, c, \text{fuel} \in [0, K])$; shortest path on $O(N^2 K)$ states. |
| **23** | `6022` | `P3357` | `最长k可重线段集问题` (Max $k$-Segment Set) | **2D Segment Projection MCMF (Double-Coordinate Trick)** | Vertical segments $x_1 = x_2$ collapse to self-loops if projected naively! **Fix**: Scale all $x \gets 2x$; map vertical segment at $x$ to $[2x, 2x+1]$ and non-vertical $[x_1, x_2]$ to $[2x_1+1, 2x_2]$! |
| **24** | `6023` | `P2769` | `猴子上树` (Monkeys Climbing Trees) | **NON-FLOW TRAP #4**: Sort + $O(NM)$ Interval/Prefix DP | Despite appearing in LOJ's 24-problem list, $N, M \le 5000$ TLEs with MCMF; sorting monkeys and trees reduces to standard $O(NM)$ DP! |

---

### 6.2 Chinese (`[ZH]`) National Team Papers (`国家集训队论文`) & Elite Archive Map

| Year & Author | Title & Core Theoretical Contribution | Flagship Problems (`Luogu` / `UOJ` / `LOJ`) |
| :--- | :--- | :--- |
| **2006 — Wangul / 王文涛 (`Wang Wentao`)** | *《网络流在信息学竞赛中的应用》*: Early systematization of vertex splitting, time-expanded layered networks, and bipartite matching reductions. | `[NOI2006] 最大获利 (P4174)` |
| **2007 — Amber / 胡伯涛 (`Hu Botao`)** | *《最小割模型在信息学竞赛中的应用》*: Seminal Chinese treatise introducing **Maximum-Weight Closure (Picard 1976)**, **Maximum Density Subgraph (Goldberg 1984)**, **0-1 Fractional Programming**, and **Pseudo-Boolean Posiform Minimization** to OI. | `[NOI2006] 最大获利 (P4174)`, `[NOI2009] 植物大战僵尸 (P2805)`, `UVA 1389 (Hard Life)`, `[文理分科]` |
| **2009 — 周冬 (`Zhou Dong`)** | *《浅谈平面图最小割》*: Formalized the **Bipartite / Planar $s$-$t$ Min-Cut $\leftrightarrow$ Dual $s^*$-$t^*$ Shortest Path Theorem** ($O(N \log N)$ Dijkstra bypass of Dinic). | `[ICPC Beijing 2006 / BJOI2006] 狼抓兔子 (P4001)`, `[NOI2010] 海拔 (P2046)` |
| **2016 — 姜志豪 (`Jiang Zhihao`)** | *《网络流的一些建模方法》*: Formalized consecutive equation differencing ($E_t - E_{t-1}$), circulation with demands (`上下界网络流`), and project selection extensions. | `[NOI2008] 志愿者招募 (P3980)`, `[AHOI2014] 支线剧情 (P4043)` |
| **2018 — 高睿泉 (`Gao Ruiquan`)** | *《浅谈保序回归问题》*: Introduced **Chakravarti's $L_p$ Isotonic Regression** and the **Two-Point Threshold Contraction + `整体二分` Dinic** algorithm to competitive programming. | `[省选联考 2020 A 卷] 魔法商店 (P6621 / LOJ 3303)`, `[BJWC2018] 最小生成树` |
| **2018–2019 — 模拟费用流 (`Simulated MCMF`)** | *《浅谈模拟费用流》*: Replaced explicit residual graphs on trees, 1D lines, and convex functions with priority queues, slope trick, and segment tree lazy propagation. | `[NOI2019] 序列 (P5470)`, `[NOI2017] 蔬菜 (P3826)`, `UOJ 455 (雪灾与外卖)` |

---

### 6.3 Japanese (`[JA]`) `燃やす埋める` (`Moyasu-Umeru`) Ecosystem & AtCoder (`AGC` / `ARC` / `ABC`) Master Archive

In the Japanese competitive programming community, Minimum-Cut Pseudo-Boolean Optimization is universally known as **`燃やす埋める` ("Burn or Bury")**, coined around 2013–2015 (`TopCoder SRM` / early AtCoder blogs) and formalized into an algebraic discipline by **`noshi91`**, **`maspypy`**, and **`tatyam`**:
1. **Binary Submodular Foundation**: A binary penalty function $\phi : \{0, 1\}^N \to \mathbb{R} \cup \{+\infty\}$ is cut-representable (without auxiliary nodes) iff every pairwise interaction $\phi_{ij}(x_i, x_j)$ satisfies the **Submodularity Inequality**:
   $$\phi_{ij}(0, 0) + \phi_{ij}(1, 1) \le \phi_{ij}(0, 1) + \phi_{ij}(1, 0) \iff B + C - A - D \ge 0.$$
2. **Bipartite Variable Inversion ("Sign Flipping" / `二部グラフの反転`)**: When a pairwise reward isgiven for **equal states** ($\phi_{ij}(0,0) + \phi_{ij}(1,1) > \phi_{ij}(0,1) + \phi_{ij}(1,0)$, which is supermodular!), check whether the interaction graph is **bipartite** ($V = L \cup R$). If so, invert the variables on $R$ by defining $y_j = 1 - x_j$ for $j \in R$. Then "same state $x_i = x_j$" becomes "different state $x_i \neq y_j$", flipping the sign of $A + D - B - C$ and restoring submodularity!
3. **$K$-Valued Monge / Submodular Functions (`noshi91` & `tatyam` Unary Threshold Chains)**: For $a_i \in \{1, \dots, K\}$, encode $K-1$ binary threshold variables $z_{i,t} = [a_i \ge t] \in \{0, 1\}$ ($t = 2, \dots, K$) linked by the **Monotonicity Chain** $z_{i,t+1} \le z_{i,t}$ (compiled as $z_{i,t+1} \xrightarrow{\infty} z_{i,t}$). Any pairwise cost $f_{ij}(a_i, a_j)$ satisfying the **Discrete Monge Condition** ($f_{ij}(s+1, t) + f_{ij}(s, t+1) - f_{ij}(s, t) - f_{ij}(s+1, t+1) \ge 0$) decomposes exactly into non-negative cut edges $z_{i,s+1} \to z_{j,t+1}$!

| AtCoder Problem | Core `燃やす埋める` / Matching / Flow Mechanism | Key Structural Twist |
| :--- | :--- | :--- |
| **`ARC 074 F - Lotus Leaves`** | Row/Column Hub Bipartite Vertex Min-Cut (`P02`) | $H + W$ hubs eliminate $O(H^2 W^2)$ clique edges. |
| **`ARC 085 E - MUL`** | Divisor Closure `燃やす埋める` (`P03`) | Multiples $i \xrightarrow{\infty} ki$. |
| **`AGC 025 D - Choosing Points`** | Gaussian Integer 2-Adic Bipartition (`P15`) | Product of two bipartite 2-colorings $\implies$ 4-coloring without Dinic! |
| **`AGC 029 F - Construction of a Tree`** | Hall's Marriage + BFS Constructive Orientation (`P21`) | Match $E_i$ to $V \setminus \{1\}$, then propagate reachability from root $1$ along matched pairs. |
| **`AGC 038 F - Two Permutations`** | Cycle-Variable Bipartite Flip `燃やす埋める` (`P27`) | Each permutation cycle is a single binary decision; invert $Q$-cycle variables ($y_C = 1 - x_C$) to rescue supermodular $P_i = Q_i$ agreement! |
| **`ABC 239 G - Builder Takahashi`** | Vertex-Split Min-Cut & Reachability Recovery (`P04`) | Recover cut via $v_{\text{in}} \in R_S \land v_{\text{out}} \notin R_S$. |
| **`ARC 107 F - Sum of Abs`** | 3-State Sign/Deletion `{-1, del, +1}` Cut (`P28`) | Split vertex into $v_{\text{in}} \xrightarrow{|A_v| + B_v} v_{\text{out}}$ to model 3 states with 2 cuts. |
| **`ARC 142 E - Pairing Wizards`** | Max-Min Dominance Split + Threshold Chain (`P29`) | $\max(x_u, x_v) \ge \max(b_u, b_v)$ forces the smaller target to be dominated; compile via unary chain. |
| **`ABC 347 G - Grid Coloring 2`** | 5-State Unary Chain + Coarea Squared Difference (`P22`) | $(a_u - a_v)^2 = \sum_{s,t} (2[s=t] - 1) [z_{u,s} \neq z_{v,t}]$? No: $(a_u - a_v)^2$ uses Monge cross-threshold edges! |
| **`ABC 354 G - Select Strings`** | Weighted Dilworth Substring Antichain (`P13`) | $u_R \xrightarrow{\infty} u_L$ bypass gadget or full transitive closure. |

---

### 6.4 English (`[EN]`) Codeforces, ICPC World Finals, and TopCoder Master Archive

| Problem & Source | Core Theoretical Mechanism | Diagnostic Signature |
| :--- | :--- | :--- |
| **`CF 498 C - Array and Operations`** | Prime-Wise Independent Bipartite Max-Flow (`P01`) | Odd+Even index sum $\implies$ bipartite; distinct primes decouple. |
| **`CF 590 E - Birthday`** | AC Compressed-Link Jump Table + Dilworth Antichain (`P17`) | $\sum |s_i| \le 10^7$ requires skipping non-terminal fail states. |
| **`CF 1404 E - Bricks`** | Dual Shared-Border Unit-Segment Bipartite MIS (`P11`) | $R_{\min} = \#(\text{cells}) - \text{MIS}(G_{\text{border}})$. |
| **`CF 1427 G - One Billion Shades of Grey`** | Coarea Level-Set Cut + Incremental Re-Optimization (`P30`) | $\sum |a_u - a_v| = \sum_k (\text{cut}_{k+1} - \text{cut}_k)$; undo flow (`退流`) between thresholds! |
| **`CF 1517 G - Starry Night Camping`** | 4-Phase Modulo Parity Path `(x%2, y%2)` Min-Cut (`P23`) | Forbidden L-trominoes mapped to 4-layer DAG $0 \to 1 \to 2 \to 3$. |
| **`CF 1783 F - Double Sort II`** | Two-Permutation Cycle Cover Intersection Matching (`P06`) | Match cycles of $P$ and $Q$ sharing element $i$ to save $1$ operation per match. |
| **`ICPC WF 2017 C - Mission Improbable`** | 3D Grid Cross-Intersection Bipartite Matching (`P05`) | Match row $r$ and column $c$ iff $\max_c H_{r,c} == \max_r H_{r,c}$ and cell $(r,c)$ is non-empty. |

---

## 7. Cohort 3 Targeted Gap-Hunting: Continuous Max-Flow / Min-Cut on Euclidean Domains & Total Variation (`Rudin–Osher–Fatemi TV Denoising`) $\leftrightarrow$ Discrete Grid Cuts & Isotonic Regression

Neither Cohort 1 nor Cohort 2 explicitly connected the discrete Coarea level-set cuts (`CF 1427 G`, `[NOI2010] 海拔`, `ABC 347 G`) and $L_p$ Isotonic Regression to their continuous partial differential equation (PDE) and variational origin: **Strang's Continuous Max-Flow / Min-Cut Duality (1983)** and the **Rudin–Osher–Fatemi (ROF) Total Variation Denoising Model (1992)**. Understanding this bridge gives a unified continuous-to-discrete lens over Wave 5B.

### 7.1 Strang's Continuous Max-Flow / Min-Cut Theorem & The Coarea Formula

On a bounded Euclidean domain $\Omega \subset \mathbb{R}^d$ with capacity density $c(x) > 0$, a **continuous flow** is a vector field $\vec{\phi} : \Omega \to \mathbb{R}^d$ satisfying the point-wise capacity bound $|\vec{\phi}(x)|_2 \le c(x)$ (or $|\vec{\phi}(x)|_\infty \le c(x)$ on an axis-aligned grid) and conservation laws $\operatorname{div} \vec{\phi} = 0$ inside $\Omega$.
By the **Gauss–Green Divergence Theorem** and **Federer's Coarea Formula**:
$$\int_\Omega u(x) \, (-\operatorname{div} \vec{\phi}(x)) \, dx = \int_\Omega \nabla u(x) \cdot \vec{\phi}(x) \, dx \le \int_\Omega c(x) |\nabla u(x)| \, dx = \int_{-\infty}^{+\infty} \left( \int_{\partial \{x \in \Omega : u(x) > \lambda\}} c(x) \, d\mathcal{H}^{d-1}(x) \right) d\lambda.$$
Here:
- The left-hand side maximizes the **continuous flow divergence** against the scalar potential $u : \Omega \to [0, 1]$ (where $u|_S = 1$ on the source boundary and $u|_T = 0$ on the sink boundary).
- The middle term $\text{TV}_c(u) := \int_\Omega c(x) |\nabla u(x)| \, dx$ is the **Weighted Total Variation** of $u$.
- The right-hand side is the **Coarea Integral** over all level-set perimeters (cuts!) $E_\lambda = \{x \in \Omega : u(x) > \lambda\}$.

> [!IMPORTANT]
> **Theorem 7.1 (The Four-Way Equivalence: Continuous ROF Total Variation $\leftrightarrow$ Discrete Coarea Cut $\leftrightarrow$ Threshold Rounding $\leftrightarrow$ Isotonic Regression)**:
> Consider the discrete counterpart on a graph $G = (V, E)$ with edge weights $c_{uv} \ge 0$ and vertex data fidelity $\sum_{v \in V} \Phi_v(u_v)$:
> $$\min_{u : V \to \mathbb{R}} \left\{ \underbrace{\sum_{v \in V} \Phi_v(u_v)}_{\text{Data Fidelity (ROF / Isotonic)}} + \underbrace{\sum_{(u, v) \in E} c_{uv} |u_u - u_v|}_{\text{Discrete Total Variation } \text{TV}_c(u)} \right\}.$$
> 1. **Limit $c_{uv} \to \infty$ on Directed Arcs (`保序回归` / Isotonic Regression, §2)**:
>    Replacing the symmetric $|u_u - u_v|$ by the asymmetric infinite barrier $\infty \cdot \max(0, u_u - u_v)$ yields exact **$L_p$ Isotonic Regression** $\min \sum \Phi_v(u_v)$ s.t. $u_u \le u_v$.
> 2. **Pure Total Variation with Boundary Pinning (`CF 1427 G` & `[NOI2010] 海拔`, $\Phi_v = 0$ on interior)**:
>    By the **Discrete Coarea Identity** $|u_u - u_v| = \int_{-\infty}^{+\infty} \big|[u_u > \lambda] - [u_v > \lambda]\big| \, d\lambda$:
>    $$\sum_{(u, v) \in E} c_{uv} |u_u - u_v| = \int_{-\infty}^{+\infty} \text{Cut}_c\big(\{w \in V : u_w > \lambda\}\big) \, d\lambda.$$
>    Since each level-set indicator $x_w(\lambda) = [u_w > \lambda] \in \{0, 1\}$ is minimized independently at every threshold $\lambda$ (and nestedness $E_{\lambda_2} \subseteq E_{\lambda_1}$ for $\lambda_1 < \lambda_2$ holds automatically by submodularity of cuts, **Chambolle 2004 / Darbon–Sigelle 2006**!):
>    - If boundary values are in $\{0, 1\}$ (`[NOI2010] 海拔`), all optimal interior values satisfy $u^*_v \in \{0, 1\}$ (one single $s$-$t$ min-cut / planar dual Dijkstra!).
>    - If boundary values are $b_1 < b_2 < \dots < b_K$ (`CF 1427 G`), $u^*_v$ is compiled by summing $(b_{k+1} - b_k) \cdot \text{MinCut}(\lambda \in (b_k, b_{k+1}))$ across the $K-1$ intervals via incremental residual re-optimization (`退流`)!
> 3. **Rudin–Osher–Fatemi ($L_2$-TV) Image Denoising ($\Phi_v(u_v) = w_v (u_v - y_v)^2 + \text{TV}_c(u)$)**:
>    For any convex $\Phi_v$ PLUS finite Total Variation $\sum c_{uv} |u_u - u_v|$, the **Two-Point Threshold Contraction Theorem (§2.3)** still holds verbatim because $|u_u - u_v|$ is submodular! Thus `整体二分` (Parallel Binary Search with Dinic) solves the exact discrete Rudin–Osher–Fatemi $L_p$-TV problem in $O(\text{MaxFlow}(N, M) \log U)$ time!

---

### 7.2 Reconciled Master Recognition & Compilation Decision Table

| Problem Surface Signature | Underlying Mathematical Structure | Optimal Compilation & Complexity | Reference Section & Flagship Problems |
| :--- | :--- | :--- | :--- |
| Minimize $\sum w_v |f_v - y_v|^p$ ($p \in [1, \infty)$) s.t. $f_u \le f_v$ on arbitrary Preorder/DAG | **Convex Isotonic Regression (`保序回归`)** | Contract SCCs $\to$ `整体二分` on Two-Point Cuts ($O(\log N)$ levels for $L_1$; $O(\log U)$ for $L_p, p>1$) | **§2**: `P25 (Luogu P6621 / LOJ 3303)`, `P19 ([BJWC2018] MST)`, `P26 (Luogu P4331)` |
| Minimize $\max_v w_v |f_v - y_v|$ s.t. $f_u \le f_v$ on DAG | **$L_\infty$ Isotonic / Difference Constraints** | Binary search $\lambda$ + Topological Longest-Path DP in $O((N+M)\log U)$ (**No Flow!**) | **§2.5**: $L_\infty$ specialization |
| 2-Player Impartial Alternating Walk on Undirected Graph | **Dulmage–Mendelsohn Matching Polarity** | Check Variant A (P1 places $\implies v_0 \in \mathcal{E}$) vs. Variant B (P1 moves $\implies v_0 \notin \mathcal{E}$) via 1 Dinic + Residual BFS | **§3.2**: `P09 ([JSOI2009] 游戏)` |
| Increment adjacent grid pairs by $+1$ to equalize all cells to $X$ | **Chessboard Parity + Domino Feasibility** | If $NM$ odd: $X = S_B - S_W$ fixed; if $NM$ even: $S_B = S_W$ + Binary Search $X$ with Bipartite Max-Flow | **§3.3**: `P10 ([SCOI2012] 奇怪的游戏)` |
| Minimum Rectangle Partition of Rectilinear Polygon (with $h$ holes) | **Imai–Asano Chord Intersection Bipartite MIS** | $R_{\min} = 1 - h + c_{\text{conc}} - |I^*| = \frac{N}{2} - 1 + h - |I^*|$; conflict uses non-strict $\le$ at shared endpoints! | **§4.1–4.3**: `P24 (UVa 1711)`, `P11 (CF 1404 E)` |
| Maximum-Weight Substring / Poset Antichain | **Weighted Dilworth Theorem + Kőnig Cut** | Split $S \xrightarrow{w_u} u_L, u_R \xrightarrow{w_u} T$; either full transitive closure OR sparse DAG + $u_R \xrightarrow{\infty} u_L$ bypass! | **§5.1**: `P13 (ABC 354 G)`, `P17 (CF 590 E)` |
| Modify edge weights to make $T$ an MST under $L_1$ vs. $L_2$ norm | **Fundamental Cycle Inequality $w'_e \le w'_f$** | $L_1$: LP Dual $\to$ Bipartite Assignment MCMF; $L_2$: `整体二分` Isotonic Regression | **§5.2**: `P18 ([SHOI2004] MST)`, `P19 ([BJWC2018] MST)` |
| Minimize $\sum_{(u,v) \in E} c_{uv} |a_u - a_v|$ with pinned boundary values | **Coarea Level-Set Cut Decomposition** | $\sum_k (b_{k+1} - b_k) \text{MinCut}(\lambda_k)$ via incremental flow rollback (`退流`) or Planar Dual Dijkstra | **§7.1**: `P30 (CF 1427 G)`, `P32 ([NOI2010] 海拔)`, `P22 (ABC 347 G)` |


---

## 8. Reconciled Master 4-Tier Curated Problem Bank (32 Non-Template Problems)

Every problem below combines the strongest insights of Cohort 1 and Cohort 2 and adheres strictly to the **4-Step "Zero Magic Gadgets" Compilation Mandate**.

---

### Tier 1: Stepping Stone (`P01–P08`)

---

#### P01 — CF 498 C: Array and Operations
- **URL**: `https://codeforces.com/problemset/problem/498/C`
- **Constraints**: $N, M \le 100$, $1 \le a_i \le 10^9$, $M$ good pairs $(i_k, j_k)$ where $i_k + j_k$ is always odd. Time Limit: 1.0s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  In one operation, you choose a good pair $(i, j)$ and a common divisor $d > 1$ of $\gcd(a_i, a_j)$, and divide both $a_i$ and $a_j$ by $d$. To maximize total operations, you should always pick a **prime** $d = p$. Crucially, dividing by prime $p$ never affects the exponent of any other prime $q \neq p$, and the condition "$i_k + j_k$ is odd" means every good pair connects an **odd index** to an **even index** (a bipartite graph!).
- **Step 2 — Intermediate Algebraic Representation**:
  Let $v_p(a_i)$ be the exponent of prime $p$ in the prime factorization of $a_i$. For each prime $p$, let $x_{e}^{(p)} \in \mathbb{Z}_{\ge 0}$ be the number of times pair $e = (i, j) \in E$ is divided by $p$. Then we maximize $\sum_{p} \sum_{e \in E} x_e^{(p)}$ subject to:
  $$\forall i \in \{1, \dots, N\}: \quad \sum_{e \ni i} x_e^{(p)} \le v_p(a_i).$$
- **Step 3 — Mechanical Graph Compilation**:
  Since $\sum_{i=1}^N \omega(a_i) \le 100 \times 9 = 900$, there are at most $900$ distinct primes dividing $\prod_{i=1}^N a_i$. For each such prime $p$ independently:
  - Source $S \to i$ (for odd $i$) with capacity $v_p(a_i)$.
  - $j \to \text{Sink } T$ (for even $j$) with capacity $v_p(a_j)$.
  - For each good pair $(i, j)$ with $i$ odd and $j$ even: directed edge $i \to j$ with capacity $\infty$.
  Sum $\text{MaxFlow}_p(S, T)$ over all distinct primes $p$.
- **Step 4 — Toy Trace, Traps & Complexity**:
  - *Toy Trace*: $a = [6, 12, 4]$, pairs $(1, 2)$ and $(2, 3)$. For $p = 2$: $v_2 = [1, 2, 2]$. Odd side $\{1, 3\}$ supplies $1 + 2 = 3$ to even node $\{2\}$ which has sink capacity $2 \implies$ flow $2$. For $p = 3$: $v_3 = [1, 1, 0] \implies$ flow $1$ on $(1, 2)$. Total $= 2 + 1 = 3$.
  - *Complexity*: Trial division up to $\sqrt{10^9} \le 31622$ per $a_i$, followed by $\le 900$ tiny Dinic runs on $\le 102$ vertices: $< 5$ ms.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Should you ever divide by a composite number $d$, or always by a prime $p$? Do operations for different primes $p_1 \neq p_2$ interfere with each other?
  2. *Hint 2*: Notice the constraint that $i_k + j_k$ is always odd. What does this tell you about the structure of the graph of good pairs?
  3. *Hint 3*: Factor all $a_i$ into primes. For each unique prime $p$, build a bipartite network between odd indices ($S \to i$ with cap $v_p(a_i)$) and even indices ($j \to T$ with cap $v_p(a_j)$) and sum the maximum flows.

---

#### P02 — AtCoder ARC 074 F: Lotus Leaves
- **URL**: `https://atcoder.jp/contests/arc074/tasks/arc074_d`
- **Constraints**: Grid $H \times W$ ($2 \le H, W \le 100$) with characters `S`, `T`, `o` (leaf), `.` (water). Time Limit: 2.0s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  A frog jumps between leaves in the **same row or same column**. We want to remove the minimum number of `o` leaves so `S` cannot reach `T`. Naive pairwise edges between leaves in the same row/column create $O(HW(H+W))$ edges and require splitting every cell into $v_{\text{in}} \to v_{\text{out}}$. Instead, jumping along a row or column means **rows and columns are the hubs, and each leaf `(r, c)` is an incidence link between Row `r` and Column `c`**!
- **Step 2 — Intermediate Algebraic Representation**:
  Let $u_r \in \{0, 1\}$ ($r = 1..H$) and $v_c \in \{0, 1\}$ ($c = 1..W$) be binary reachability indicators from `S` ($u_{r_S} = v_{c_S} = 1$) to `T` ($u_{r_T} = v_{c_T} = 0$). A leaf at $(r, c)$ allows transitioning $u_r \leftrightarrow v_c$ unless cut at cost $1$:
  $$\min_{u, v \in \{0, 1\}} \sum_{(r, c) \in \text{Leaves}} |u_r - v_c| \quad \text{s.t.} \quad u_{r_S} = v_{c_S} = 1, \;\; u_{r_T} = v_{c_T} = 0.$$
- **Step 3 — Mechanical Graph Compilation**:
  - If $r_S == r_T$ or $c_S == c_T$, output `-1` immediately (indestructible direct jump).
  - Create $H$ row vertices $R_1, \dots, R_H$ and $W$ column vertices $C_1, \dots, C_W$.
  - Connect $S \xrightarrow{\infty} R_{r_S}$, $S \xrightarrow{\infty} C_{c_S}$, and $R_{r_T} \xrightarrow{\infty} T$, $C_{c_T} \xrightarrow{\infty} T$.
  - For every leaf `o` at $(r, c)$: add undirected edge $R_r \leftrightarrow C_c$ of capacity $1$ (i.e., $R_r \xrightarrow{1} C_c$ and $C_c \xrightarrow{1} R_r$).
- **Step 4 — Toy Trace, Traps & Complexity**:
  - *Trap*: Do not add capacity-$1$ edges for `S` and `T` themselves (or give them capacity $\infty$, which is already handled by $S \to R_{r_S}, C_{c_S}$ and $R_{r_T}, C_{c_T} \to T$).
  - *Complexity*: Unit network on $H + W + 2 \le 202$ vertices and $\le 2HW \le 2 \times 10^4$ edges; Dinic runs in $O(HW \sqrt{H+W}) \approx 3 \times 10^5$ ops.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: When IS the answer `-1`? Check when `S` and `T` share a row or column.
  2. *Hint 2*: Instead of making leaves the vertices and jumps the edges, what if the $H$ rows and $W$ columns are the vertices?
  3. *Hint 3*: Each leaf at $(r, c)$ enables jumping between Row $r$ and Column $c$, so it is simply a capacity-$1$ undirected edge between vertex $R_r$ and vertex $C_c$!

---

#### P03 — AtCoder ARC 085 E: MUL
- **URL**: `https://atcoder.jp/contests/arc085/tasks/arc085_c`
- **Constraints**: $N \le 100$, $|a_i| \le 10^9$. Smashing gem $i$ smashes all gems $k \cdot i$ ($k \ge 1$). Maximize remaining sum. Time Limit: 2.0s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  "Smashing $i$ forces smashing all multiples $k \cdot i$" is the contrapositive of "Keeping $j$ forces keeping all divisors $i \mid j$". Since $a_i$ has arbitrary signs and $N \le 100$, this is a textbook **Maximum-Weight Closure (`燃やす埋める`)** problem on the divisibility poset $(1..N, \mid)$.
- **Step 2 — Intermediate Algebraic Representation**:
  Let $x_i \in \{0, 1\}$ be $1$ if gem $i$ is **kept** and $0$ if **smashed**. Start from the ideal baseline where we keep all positive gems $P = \sum_{a_i > 0} a_i$:
  - If $a_i > 0$ and we smash $i$ ($x_i = 0$), we lose $a_i$: penalty $a_i(1 - x_i)$.
  - If $a_i < 0$ and we keep $i$ ($x_i = 1$), we lose $|a_i| = -a_i$: penalty $(-a_i) x_i$.
  - Closure constraint: smashing $i$ ($x_i = 0$) forces smashing $k i$ ($x_{ki} = 0$), i.e., $x_{ki} \le x_i \iff$ forbidden state $x_{ki} = 1 \land x_i = 0$: penalty $\infty \cdot x_{ki}(1 - x_i)$ (or if $S$ = smashed ($y_i=1$) and $T$ = kept ($y_i=0$), $y_i = 1 \implies y_{ki} = 1$, penalty $\infty \cdot y_i(1 - y_{ki})$).
- **Step 3 — Mechanical Graph Compilation**:
  Let $S$ represent **Smashed** ($y_i = 1$) and $T$ represent **Kept** ($y_i = 0$):
  - For each $i$ with $a_i > 0$: keeping $i$ is ideal; smashing $i$ ($y_i = 1 \implies i \in S$) costs $a_i \implies$ add edge $i \xrightarrow{a_i} T$.
  - For each $i$ with $a_i < 0$: smashing $i$ is free; keeping $i$ ($y_i = 0 \implies i \in T$) costs $-a_i \implies$ add edge $S \xrightarrow{-a_i} i$.
  - For each $i \in \{1, \dots, N\}$ and multiple $j = k \cdot i$ ($k \ge 2$): smashing $i$ ($i \in S$) forces smashing $j$ ($j \in S$) $\implies$ add directed edge $i \xrightarrow{\infty} j$.
  - Output $\sum_{a_i > 0} a_i - \text{MinCut}(S, T)$ in `long long`.
- **Step 4 — Toy Trace, Traps & Complexity**:
  - *Trap*: Total flow can reach $100 \times 10^9 = 10^{11}$, so Dinic capacities and flow accumulator MUST be `long long` (`INF = 1e18`).
  - *Complexity*: $N \le 100$, $\sum_{i=1}^N \lfloor N/i \rfloor = N H_N \approx 518$ closure edges; Dinic takes $< 1$ ms.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Assume you initially collect every positive gem $a_i > 0$ and smash every negative gem $a_i \le 0$. What penalties do you pay if you deviate from this ideal choice?
  2. *Hint 2*: Notice that smashing $i$ forces smashing $2i, 3i, \dots$. Express this as an implication $y_i = 1 \implies y_{ki} = 1$.
  3. *Hint 3*: Build an $S$-$T$ cut where $i \in S$ means "smashed" and $i \in T$ means "kept", with $i \xrightarrow{\infty} ki$, $S \xrightarrow{-a_i} i$ ($a_i < 0$), and $i \xrightarrow{a_i} T$ ($a_i > 0$).

---

#### P04 — AtCoder ABC 239 G: Builder Takahashi
- **URL**: `https://atcoder.jp/contests/abc239/tasks/abc239_g`
- **Constraints**: $N \le 100, M \le \binom{N}{2}$, $1 \le c_i \le 10^9$ ($i = 2..N-1$). Output minimum cost AND exact vertex list. Time Limit: 2.0s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Standard minimum-weight vertex cut between $1$ and $N$, paired with **explicit reconstruction of the cut vertices**.
- **Step 2 & 3 — Algebraic & Mechanical Graph Compilation**:
  Split each vertex $v \in \{1, \dots, N\}$ into $v_{\text{in}}$ and $v_{\text{out}}$:
  - Internal edges: $v_{\text{in}} \xrightarrow{c_v} v_{\text{out}}$ for $v \in \{2, \dots, N-1\}$, and $\infty$ for $v \in \{1, N\}$.
  - Graph edges $(u, v) \in E$: $u_{\text{out}} \xrightarrow{\infty} v_{\text{in}}$ and $v_{\text{out}} \xrightarrow{\infty} u_{\text{in}}$.
  - Source $= 1_{\text{out}}$, Sink $= N_{\text{in}}$.
- **Step 4 — Constructive Recovery Trap**:
  After Dinic terminates, run a single BFS from $1_{\text{out}}$ using only residual edges with positive remaining capacity (`e.cap - e.flow > 0`) to mark the reachable set $R_S$. Vertex $v \in \{2, \dots, N-1\}$ belongs to the minimum vertex cut **if and only if** $v_{\text{in}} \in R_S$ and $v_{\text{out}} \notin R_S$. (Do NOT check `e.flow == e.cap` alone!)
- **3-Tier Progressive Hints**:
  1. *Hint 1*: How do you convert vertex destruction costs $c_v$ into edge capacities?
  2. *Hint 2*: Split each vertex $v$ into $v_{\text{in}} \xrightarrow{c_v} v_{\text{out}}$ and route undirected edges $(u, v)$ as $u_{\text{out}} \xrightarrow{\infty} v_{\text{in}}$ and $v_{\text{out}} \xrightarrow{\infty} u_{\text{in}}$.
  3. *Hint 3*: To reconstruct the exact set of cut vertices, find all nodes reachable from $1_{\text{out}}$ in the residual graph ($R_S$), and output $v$ iff $v_{\text{in}} \in R_S$ and $v_{\text{out}} \notin R_S$.

---

#### P05 — ICPC World Finals 2017 Problem C: Mission Improbable
- **URL**: `https://icpc.global/worldfinals/problems/2017-ICPC-World-Finals/icpc2017.pdf` (also `Luogu P6919` / `Codeforces Gym`)
- **Constraints**: Grid $R \times C$ ($1 \le R, C \le 100$), heights $0 \le H_{r,c} \le 10^9$. Time Limit: 1.0s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  We want to leave the minimum possible number of crates (maximizing stolen crates) while preserving:
  1. Top-down camera view: $(r, c)$ remains non-empty ($\ge 1$ crate) iff $H_{r,c} > 0$.
  2. Front & Side silhouettes: each row $r$ keeps at least one stack of height $M_r = \max_c H_{r,c}$, and each column $c$ keeps at least one stack of height $N_c = \max_r H_{r,c}$.
  Whenever $M_r == N_c > 0$ and cell $(r, c)$ is non-empty ($H_{r,c} > 0$), placing a single stack of height $M_r$ at $(r, c)$ satisfies **both** Row $r$ and Column $c$ simultaneously, saving $M_r - 1$ crates!
- **Step 2 & 3 — Algebraic & Mechanical Graph Compilation**:
  - Group rows and columns by their target maximum height $h = M_r = N_c > 0$. Different heights $h_1 \neq h_2$ can never share a sentinel stack!
  - Even simpler: build a single bipartite graph between Rows $1..R$ and Columns $1..C$ where an edge $(r, c)$ exists iff:
    $$H_{r,c} > 0 \quad \text{and} \quad M_r == N_c.$$
  - Since every row $r$ has only one height $M_r$ and every column $c$ has only one height $N_c$, the graph naturally decomposes into connected components of equal height $h = M_r = N_c$! Every matched edge $(r, c)$ in this bipartite graph saves exactly $M_r - 1$ crates!
  - Total crates we must leave behind (above the base layer of $1$ crate per non-empty cell):
    $$\text{MinKept} = \#\{(r, c) : H_{r,c} > 0\} + \sum_{r : M_r > 0} (M_r - 1) + \sum_{c : N_c > 0} (N_c - 1) - \sum_{(r, c) \in M^*} (M_r - 1),$$
    where $M^*$ is any **Maximum Cardinality Bipartite Matching** (because inside each height component $h$, every edge has identical weight $h - 1$!).
- **Step 4 — Toy Trace, Traps & Complexity**:
  - *Critical Trap*: Never add an edge $(r, c)$ if $H_{r,c} == 0$, even if $M_r == N_c$! Placing a stack of height $M_r > 0$ on an initially empty cell $(r, c)$ violates the top-down camera view!
  - *Complexity*: Hopcroft–Karp / Dinic on $R + C \le 200$ vertices takes $< 1$ ms.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Every initially non-empty cell $(r, c)$ ($H_{r,c} > 0$) must keep at least $1$ crate. After placing $1$ crate on every non-empty cell, how many *extra* crates does Row $r$ or Column $c$ need?
  2. *Hint 2*: Row $r$ needs one cell boosted by $M_r - 1$, and Column $c$ needs one cell boosted by $N_c - 1$. When can a single cell $(r, c)$ satisfy both Row $r$ and Column $c$ at the same time?
  3. *Hint 3*: Only when $H_{r,c} > 0$ and $M_r == N_c$! Since the weight $M_r - 1$ is constant within each equal-height component, standard unweighted Maximum Bipartite Matching maximizes the saved crates!

---

#### P06 — Codeforces 1783 F: Double Sort II
- **URL**: `https://codeforces.com/problemset/problem/1783/F`
- **Constraints**: $N \le 3000$, two permutations $a, b$ of $1..N$. In one operation, choose $x$ and swap $x$ to its correct position in $a$ (if needed) and in $b$ (if needed). Minimize operations. Time Limit: 2.0s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Sorting a permutation $a$ with $c_A$ disjoint cycles requires at least $N - c_A$ swaps; equivalently, in each cycle $C \in \mathcal{C}_A$, we can leave **at most one element $x \in C$ untouched** (as the pivot/last element of the cycle) while operating on the other $|C| - 1$ elements. If we choose the **same element $x$** to be the untouched pivot in its $a$-cycle $C_A(x)$ AND its $b$-cycle $C_B(x)$, then $x$ never needs to be chosen at all, saving $1$ operation out of $N$!
- **Step 2 & 3 — Algebraic & Mechanical Graph Compilation**:
  - Decompose $a$ into cycles $\mathcal{C}_A = \{A_1, \dots, A_p\}$ and $b$ into cycles $\mathcal{C}_B = \{B_1, \dots, B_q\}$.
  - Each element $x \in \{1, \dots, N\}$ belongs to a unique cycle $A_{u(x)} \in \mathcal{C}_A$ and a unique cycle $B_{v(x)} \in \mathcal{C}_B$, forming a bipartite edge $e_x = (A_{u(x)}, B_{v(x)})$ labeled by $x$.
  - A matching $M^*$ of size $k$ in this bipartite graph $(\mathcal{C}_A, \mathcal{C}_B)$ selects $k$ elements $x$ that serve as simultaneous untouched pivots for both their $a$-cycle and their $b$-cycle!
  - The minimum number of operations is $N - |M^*|$, and the elements operated on are $\{1, \dots, N\} \setminus \{x : e_x \in M^*\}$.
- **Step 4 — Toy Trace & Complexity**:
  - $|\mathcal{C}_A|, |\mathcal{C}_B| \le N \le 3000$ and $|E| = N \le 3000$; Dinic / Hopcroft–Karp runs in $O(N\sqrt{N}) \approx 1.6 \times 10^5$ ops.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Instead of minimizing the number of elements you operate on, maximize the number of elements $x \in \{1, \dots, N\}$ that you **never** operate on!
  2. *Hint 2*: In any cycle $C$ of permutation $a$, how many elements of $C$ can remain completely untouched while still sorting $C$? At most $1$!
  3. *Hint 3*: An untouched element $x$ uses up the "1 untouched element" quota of its cycle in $a$ AND its cycle in $b$. Model cycles of $a$ on the left, cycles of $b$ on the right, and each element $x \in \{1, \dots, N\}$ as an edge between its two cycles!

---

#### P07 — LOJ 6007 / Luogu P2774: 方格取数问题 (Grid Number Selection)
- **URL**: `https://loj.ac/p/6007` / `https://www.luogu.com.cn/problem/P2774`
- **Constraints**: $M, N \le 100$ (or $\le 30$), $w_{r,c} \ge 0$. Select non-adjacent grid cells to maximize total weight. Time Limit: 1.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 (Signal)**: Maximum Weight Independent Set (MWIS) on a grid graph. Since grid adjacency only links cells of opposite $(r+c) \bmod 2$ parity, the conflict graph is **bipartite**!
  - **Step 2 (Algebraic)**: $\max \sum w_u (1 - x_u) = \sum w_u - \min \sum w_u x_u$ subject to $x_u + x_v \ge 1$ for adjacent $(u, v) \in B \times W$.
  - **Step 3 (Graph)**: $S \xrightarrow{w_u} u$ for Black cells $u \in B$; $v \xrightarrow{w_v} T$ for White cells $v \in W$; $u \xrightarrow{\infty} v$ for adjacent $u \in B, v \in W$. Answer $= \sum w - \text{MinCut}(S, T)$.
  - **Step 4 (Complexity)**: $V \le 10^4, E \le 3 \times 10^4$, Dinic runs in $< 15$ ms.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Can an odd cycle exist in a 4-connected grid graph?
  2. *Hint 2*: In any graph, $\text{MWIS} = \text{Total Weight} - \text{Minimum Weight Vertex Cover}$.
  3. *Hint 3*: 2-color the grid by $(r+c) \bmod 2$ and find the Minimum Weight Vertex Cover via an $S$-$T$ minimum cut.

---

#### P08 — LOJ 6019 / Luogu P3355: 骑士共存问题 (Knight Coexistence)
- **URL**: `https://loj.ac/p/6019` / `https://www.luogu.com.cn/problem/P3355`
- **Constraints**: $N \le 200$ chessboard with $M$ forbidden cells. Maximize mutually non-attacking knights. Time Limit: 1.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 (Signal)**: Every knight jump $(\pm 1, \pm 2)$ or $(\pm 2, \pm 1)$ changes $r + c$ by $\pm 1$ or $\pm 3$ (always **odd**!). Thus every knight move flips $(r + c) \bmod 2$, making the Knight Attack Graph **bipartite**!
  - **Step 2 & 3 (Graph)**: Delete the $M$ forbidden cells. Partition remaining $N^2 - M$ cells into $B$ ($(r+c)$ even) and $W$ ($(r+c)$ odd). Connect $S \xrightarrow{1} u \xrightarrow{\infty} v \xrightarrow{1} T$ for attacking pairs $(u, v) \in B \times W$. Output $(N^2 - M) - \text{MaxFlow}(S, T)$.
  - **Step 4 (Complexity)**: Unit network on $V \le 4 \times 10^4$ vertices, $E \le 2 \times 10^5$ edges; Dinic takes $O(E\sqrt{V}) \approx 4 \times 10^7$ ops ($\approx 80$ ms).
- **3-Tier Progressive Hints**:
  1. *Hint 1*: How does $(r + c) \bmod 2$ change when a knight makes a valid move?
  2. *Hint 2*: Since every knight move connects a Black cell to a White cell, the knight conflict graph is bipartite!
  3. *Hint 3*: By Kőnig's Theorem, Maximum Independent Set $= (N^2 - M) - \text{Maximum Matching}$.

---

### Tier 2: Intermediate (`P09–P16`)

---

#### P09 — [JSOI2009] 游戏 (`Luogu P4055`)
- **URL**: `https://www.luogu.com.cn/problem/P4055`
- **Constraints**: Grid $N \times M$ ($N, M \le 100$) with `#` obstacles and `.` open cells. `JYY` (Player 1) chooses starting cell $v_0$; `YYJ` (Player 2) moves first along 4-adjacent unvisited `.` cells. Find all winning starting cells $v_0$ for `JYY`. Time Limit: 1.0s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  Impartial walk game on a bipartite grid graph where Player 1 **places** the token and Player 2 **moves first** (Variant A of Theorem 3.1!).
- **Step 2 — Intermediate Algebraic / Matching Polarity Representation**:
  By Theorem 3.1 (§3.2), `JYY` (the Placer) has a winning strategy at $v_0$ if and only if `YYJ` (the First Mover from $v_0$) loses from $v_0$, which happens **if and only if $v_0$ is inessential ($v_0 \in \mathcal{E}$, NOT saturated in every maximum matching)**!
- **Step 3 — Mechanical Graph Compilation**:
  1. 2-color the open `.` cells into $L$ ($(r+c)\bmod 2 = 0$) and $R$ ($(r+c)\bmod 2 = 1$).
  2. Build unit matching network $S \xrightarrow{1} u \xrightarrow{1} v \xrightarrow{1} T$ ($u \in L, v \in R$) and run Dinic once.
  3. In the final residual network $G_f$:
     - Run BFS from $S$ along edges with positive residual capacity: every reached $u \in L$ is in $\mathcal{E}_L$ (winning for `JYY`).
     - Run BFS from $T$ along **reversed** edges whose forward arc $(x \to y)$ has positive residual capacity: every reached $v \in R$ is in $\mathcal{E}_R$ (winning for `JYY`).
  4. If $\mathcal{E}_L \cup \mathcal{E}_R$ is non-empty, output `WIN` and list all cells in $\mathcal{E}_L \cup \mathcal{E}_R$ in lexicographical order; else output `LOSE`.
- **Step 4 — Toy Trace & Traps**:
  - *Trap*: Re-read who moves first! In `P4055`, `JYY` places the token and `YYJ` moves first, so `JYY` wins iff $v_0 \in \mathcal{E}$. In fixed-start variants where the first mover from $v_0$ is queried, the condition is inverted ($v_0 \notin \mathcal{E}$).
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Suppose the grid has a perfect matching. Can `YYJ` (who moves first after `JYY` places the token) always win by moving along matching edges?
  2. *Hint 2*: Show that `JYY` wins by placing at $v_0$ if and only if there exists at least one maximum matching that leaves $v_0$ unmatched.
  3. *Hint 3*: Instead of running Dinic $NM$ times, run Dinic once and use residual BFS from $S$ (for $L$) and reverse residual BFS from $T$ (for $R$) to find all avoidable vertices in $O(NM)$ time!

---

#### P10 — [SCOI2012] 奇怪的游戏 (`Luogu P5038`)
- **URL**: `https://www.luogu.com.cn/problem/P5038`
- **Constraints**: $T \le 10$ testcases, $N, M \le 40$, $a_{i,j} \le 10^9$. Increment adjacent pairs by $+1$ to make all cells equal. Time Limit: 1.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 & 2 (Parity Invariant, Theorem 3.2)**: 2-color the grid into $B$ ($n_B$ cells, sum $S_B$) and $W$ ($n_W$ cells, sum $S_W$). Let $M_{\max} = \max_{i,j} a_{i,j}$.
    - **If $N \cdot M$ is odd ($n_B = n_W + 1$)**: Final target height is uniquely locked to $X = S_B - S_W$. Test if $X \ge M_{\max}$ and `check(X)` holds; if so, output $n_B X - S_B$, else `-1`.
    - **If $N \cdot M$ is even ($n_B = n_W$)**: If $S_B \neq S_W$, output `-1`. Otherwise, by the Domino Tiling Monotonicity Lemma (§3.3), `check(X)` is monotone in $X$! Binary search $X \in [M_{\max}, 2 \times 10^{11}]$ and output $n_B X^* - S_B$.
  - **Step 3 (`check(X)` Network)**: $S \xrightarrow{X - a_u} u$ ($u \in B$), $v \xrightarrow{X - a_v} T$ ($v \in W$), $u \xrightarrow{\infty} v$ for adjacent $u \in B, v \in W$. Return `MaxFlow == n_B * X - S_B`.
  - **Step 4 (Traps)**: The upper bound of binary search when $N \cdot M$ is even must be at least $\max a_{i,j} + 10^{11}$ (e.g., `2e11` or `1e12`), and all capacities must use `long long`.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Color the grid like a chessboard. How does one operation change the sum of Black cells vs. the sum of White cells?
  2. *Hint 2*: Write the equation $n_B X - S_B = n_W X - S_W$. Notice that when $N \cdot M$ is odd, $n_B - n_W = 1$, which uniquely determines $X$!
  3. *Hint 3*: When $N \cdot M$ is even, $n_B = n_W$, and any even grid has a perfect domino tiling—so if $X$ is feasible, $X+1$ is also feasible! Binary search $X$ and check feasibility via Bipartite Max-Flow.

---

#### P11 — Codeforces 1404 E: Bricks
- **URL**: `https://codeforces.com/problemset/problem/1404/E`
- **Constraints**: $N, M \le 200$ grid of `#` and `.`. Partition `#` cells into minimum $1 \times k$ or $k \times 1$ bricks. Time Limit: 4.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 (Signal)**: Start with $K = \#(\text{`\#` cells})$ isolated $1 \times 1$ bricks. Every valid horizontal merge across a shared vertical border $v \in V_H$ or vertical merge across a shared horizontal border $h \in V_V$ reduces the brick count by $1$.
  - **Step 2 (Algebraic)**: $R_{\min} = K - \max |I|$, where $I \subseteq V_H \cup V_V$ is an independent set of borders. Two borders $u \in V_H$ and $v \in V_V$ conflict iff they touch the **same `#` cell** (meeting at one of its 4 corners).
  - **Step 3 (Graph)**: Build the bipartite conflict graph $(V_H, V_V, E_{\text{corner}})$ where $|V_H|, |V_V| \le NM \le 4 \times 10^4$ and each vertex has degree $\le 4$. By Kőnig's Theorem, $\max |I| = |V_H| + |V_V| - \nu(G_{\text{corner}})$.
  - **Step 4 (Complexity)**: Unit bipartite network with $\le 8 \times 10^4$ vertices and $\le 1.6 \times 10^5$ edges; Dinic finishes in $\approx 60$ ms.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: If you start with every `#` cell as a $1 \times 1$ brick, what happens to the number of bricks each time you glue two adjacent `#` cells together?
  2. *Hint 2*: You can glue horizontally adjacent cells or vertically adjacent cells, as long as no `#` cell is glued both horizontally AND vertically.
  3. *Hint 3*: Create a vertex for each valid horizontal glue and each valid vertical glue, add a conflict edge whenever they share a `#` cell, and compute the Maximum Independent Set of this bipartite graph!

---

#### P12 — [BOI 2002] Escape (`Luogu P1345 / P5039` Archetype)
- **URL**: `https://www.luogu.com.cn/problem/P5039` (and `BOI 2002 Escape`)
- **Constraints**: Canyon of length $L$, width $W$, $N \le 250$ circular sensors of radius $R = 100$ at $(x_i, y_i)$. Eliminate minimum sensors to open a path from $x = 0$ to $x = L$. Time Limit: 1.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 & 2 (Continuous-to-Discrete Barrier Duality, §4.4)**: A path from Left ($x=0$) to Right ($x=L$) exists iff no chain of overlapping sensor disks connects the Top wall ($y=W$) to the Bottom wall ($y=0$).
  - **Step 3 (Graph)**: Split each sensor $i$ into $i_{\text{in}} \xrightarrow{1} i_{\text{out}}$ (or capacity $c_i$). Add $S \xrightarrow{\infty} i_{\text{in}}$ if $W - y_i \le R$; add $i_{\text{out}} \xrightarrow{\infty} T$ if $y_i \le R$; add $i_{\text{out}} \xrightarrow{\infty} j_{\text{in}}$ and $j_{\text{out}} \xrightarrow{\infty} i_{\text{in}}$ if $(x_i - x_j)^2 + (y_i - y_j)^2 \le (2R)^2$. Output $\text{MinCut}(S, T)$.
  - **Step 4 (Complexity)**: $2N + 2 \le 502$ vertices; Dinic takes $< 2$ ms.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: By topological duality, what blocks a prisoner from walking from Left ($x=0$) to Right ($x=L$)?
  2. *Hint 2*: A continuous barrier of overlapping sensor disks stretching from the Top wall ($y=W$) to the Bottom wall ($y=0$)!
  3. *Hint 3*: Split each sensor $i$ into $i_{\text{in}} \xrightarrow{1} i_{\text{out}}$, connect overlapping sensors with $\infty$ edges, and compute the Top-to-Bottom $S$-$T$ minimum cut.

---

#### P13 — AtCoder ABC 354 G: Select Strings
- **URL**: `https://atcoder.jp/contests/abc354/tasks/abc354_g`
- **Constraints**: $N \le 100$, $|s_i| \le 100$, $1 \le A_i \le 10^9$. Maximize weight of mutually non-substring strings. Time Limit: 2.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 (Signal)**: Maximum-Weight Antichain on the substring poset $(s_i \sqsubseteq s_j)$.
  - **Step 2 (Deduplication)**: First, if $s_i == s_j$, we can never pick both! Merge identical strings by keeping only the copy with the **maximum** weight $A_i$ and discarding the rest.
  - **Step 3 (Graph — Theorem 5.1)**: Build the split network on the remaining unique strings:
    - $S \xrightarrow{A_i} i_L$ and $i_R \xrightarrow{A_i} T$.
    - For every $i \neq j$ such that $s_i$ is a substring of $s_j$: add $i_L \xrightarrow{\infty} j_R$.
    - (Optionally add the bypass edge $i_R \xrightarrow{\infty} i_L$ for every $i$, or rely on the fact that the substring relation is already transitively closed!).
    - Output $\sum_{\text{unique } i} A_i - \text{MinCut}(S, T)$.
  - **Step 4 (Trap)**: Failing to deduplicate identical strings $s_i == s_j$ before building the poset will create a 2-cycle $i \prec j \prec i$, allowing you to keep neither or double-counting!
- **3-Tier Progressive Hints**:
  1. *Hint 1*: First, what if two strings in the input are identical ($s_i = s_j$)? Can you ever select both? Keep only the one with larger $A_i$!
  2. *Hint 2*: After deduplicating, the "is a substring of" relation is a strict partial order (DAG), and you want a Maximum-Weight Antichain.
  3. *Hint 3*: By Weighted Dilworth / Kőnig duality, split each string $i$ into $S \xrightarrow{A_i} i_L$ and $i_R \xrightarrow{A_i} T$, add $i_L \xrightarrow{\infty} j_R$ whenever $s_i$ is a substring of $s_j$, and subtract the Min-Cut from $\sum A_i$.

---

#### P14 — [SDOI2016] 数字配对 (`Luogu P4068`)
- **URL**: `https://www.luogu.com.cn/problem/P4068`
- **Constraints**: $N \le 200$, $a_i \le 10^9, b_i \le 10^5, |c_i| \le 10^5$. Pair $i, j$ if $a_j / a_i$ is prime, earning $c_i c_j$. Maximize pairs subject to total value $\ge 0$. Time Limit: 1.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 (Signal)**: $a_j / a_i = p$ (prime) means $\Omega(a_j) = \Omega(a_i) + 1$, where $\Omega(x)$ is the total number of prime factors of $x$ with multiplicity. Thus the pairing graph is **bipartite by $\Omega(a_i) \bmod 2$**!
  - **Step 2 & 3 (Graph & Greedy MCMF Stopping)**:
    - Partition $i \in \{1, \dots, N\}$ into $L$ ($\Omega(a_i)$ even, $S \xrightarrow{b_i, 0} i$) and $R$ ($\Omega(a_j)$ odd, $j \xrightarrow{b_j, 0} T$).
    - Whenever $a_i \mid a_j$ and $a_j / a_i$ is prime (or vice versa), connect the $L$-endpoint to the $R$-endpoint with capacity $\infty$ and cost $-c_i c_j$ (to maximize gain via shortest paths).
    - Run successive shortest-path MCMF (SPFA along min-cost / max-gain paths). Let $G_{\text{total}}$ be the accumulated gain. As long as the current augmenting path has gain $g \ge 0$ (cost $\le 0$), push full flow $f$ and add $f \cdot g$ to $G_{\text{total}}$.
    - When $g < 0$, we can push at most $\lfloor G_{\text{total}} / (-g) \rfloor$ additional units of flow before $G_{\text{total}}$ would drop below $0$; push $\min(f, \lfloor G_{\text{total}} / (-g) \rfloor)$ and **terminate if $G_{\text{total}} < -g$**!
  - **Step 4 (Trap)**: Use `__int128` or `long long` carefully for $G_{\text{total}} + f \cdot g$ since $b_i \le 10^5$ and $c_i c_j \le 10^{10}$ can reach $10^{15}$.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Count the total number of prime factors $\Omega(a_i)$ (with multiplicity) of each number. How does $\Omega(a_i)$ relate to $\Omega(a_j)$ when $a_j / a_i$ is prime?
  2. *Hint 2*: Their $\Omega$ values differ by $1$, so the graph is bipartite by $\Omega(a_i) \bmod 2$!
  3. *Hint 3*: Run Max-Gain Flow (MCMF with negated costs) greedily from highest gain per unit flow to lowest, and stop (truncating the final path's flow) the moment total accumulated gain would become negative.

---

#### P15 — AtCoder AGC 025 D: Choosing Points
- **URL**: `https://atcoder.jp/contests/agc025/tasks/agc025_d`
- **Constraints**: Grid $2N \times 2N$ ($N \le 300$), $1 \le D_1, D_2 \le 2 \times 10^5$. Select $N^2$ points with no pair at distance $\sqrt{D_1}$ or $\sqrt{D_2}$. Time Limit: 2.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 (Signal)**: $(2N)^2 = 4N^2 \le 3.6 \times 10^5$ vertices is too large for general Dinic, and we have **two** forbidden distances $D_1, D_2$ simultaneously! However, choosing $N^2 = \frac{1}{4}(4N^2)$ points out of $4N^2$ suggests a **4-Coloring** where each single distance graph $G(D)$ is **bipartite (2-colorable)**!
  - **Step 2 (Algebraic Proof via 2-Adic Valuation in $\mathbb{Z}[i]$)**:
    Write $D = 4^k d$ (or $2^k m$). Why is $G(D)$ on $\mathbb{Z}^2$ always bipartite?
    - **Base Case ($D \equiv 1, 2 \pmod 4$, or $D$ odd)**:
      - If $D$ is odd: $\Delta x^2 + \Delta y^2 = D \equiv 1 \pmod 2 \implies \Delta x + \Delta y$ is odd! Coloring $(x, y)$ by $(x + y) \bmod 2$ properly 2-colors $G(D)$!
      - If $D \equiv 2 \pmod 4$: $\Delta x^2 + \Delta y^2 \equiv 2 \pmod 4 \implies \Delta x$ and $\Delta y$ are **both odd**! Coloring $(x, y)$ by $x \bmod 2$ properly 2-colors $G(D)$!
    - **Inductive Case ($D = 4 D'$, i.e., $D \equiv 0 \pmod 4$)**:
      $\Delta x^2 + \Delta y^2 \equiv 0 \pmod 4 \implies \Delta x$ and $\Delta y$ are **both even**! Thus points only connect within the same parity class of $(x \bmod 2, y \bmod 2)$, and dividing coordinates by $2$ ($x' = \lfloor x/2 \rfloor, y' = \lfloor y/2 \rfloor$) reduces $D \gets D/4$ until $D \not\equiv 0 \pmod 4$!
  - **Step 3 (Compilation without Flow!)**:
    For $D \in \{D_1, D_2\}$, let $2^t \parallel D$ be the highest power of $2$ dividing $D$:
    - If $t = 2k$ is even ($D / 4^k$ is odd): color $c_D(x, y) = \big(\lfloor x / 2^k \rfloor + \lfloor y / 2^k \rfloor\big) \bmod 2$.
    - If $t = 2k + 1$ is odd ($D / 4^k \equiv 2 \pmod 4$): color $c_D(x, y) = \lfloor x / 2^k \rfloor \bmod 2$.
    Combine the two binary colors into a 4-color label $C(x, y) = 2 c_{D_1}(x, y) + c_{D_2}(x, y) \in \{0, 1, 2, 3\}$. By the Pigeonhole Principle, at least one of the 4 color classes contains $\ge \frac{4N^2}{4} = N^2$ points! Output the first $N^2$ points of that color class in $O(N^2)$ time!
- **3-Tier Progressive Hints**:
  1. *Hint 1*: You need to pick $\frac{1}{4}$ of the $4N^2$ grid points. What if the graph for $D_1$ is bipartite (2-colorable) and the graph for $D_2$ is ALSO bipartite (2-colorable)?
  2. *Hint 2*: Prove that for ANY integer $D \ge 1$, the graph on $\mathbb{Z}^2$ connecting pairs with $\Delta x^2 + \Delta y^2 = D$ is bipartite! Check the cases $D$ odd, $D \equiv 2 \pmod 4$, and $D \equiv 0 \pmod 4$.
  3. *Hint 3*: Factor out powers of $4$ from $D_1$ and $D_2$ to get explicit $O(1)$ 2-coloring formulas $c_1(x, y)$ and $c_2(x, y)$, and pick the largest of the 4 combined color classes `(c_1, c_2)`.

---

#### P16 — [BJOI2018] 智力竞赛 (`Luogu P4589`)
- **URL**: `https://www.luogu.com.cn/problem/P4589`
- **Constraints**: $N+1$ rounds ($N \le 50$), $M \le 500$ vertices in a DAG, each vertex $u$ has question value $a_u$ ($a_u \le 10^9$). Choose $N+1$ paths to maximize the minimum unvisited value ($\text{mex}$-style threshold). Time Limit: 1.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 & 2 (Binary Search + Dilworth Chain Cover)**: Binary search the score threshold $K$ (meaning we must visit **every** vertex $u$ that has $a_u < K$). Since paths can step through vertices with $a_v \ge K$ on the way between required vertices $u$ with $a_u < K$, first compute the **transitive closure** of the full $M$-vertex DAG using Floyd–Warshall in $O(M^3)$.
  - **Step 3 (Induced Poset Minimum Path Cover)**: For a fixed $K$, restrict to the subset of required vertices $V_K = \{u \in V : a_u < K\}$. Since the transitive closure is already computed, $(V_K, \prec)$ is a transitively closed DAG! By Dilworth's Theorem, the minimum number of paths needed to cover all vertices in $V_K$ is:
    $$\text{MinChains}(V_K) = |V_K| - \nu(G_{\text{split}}(V_K)).$$
    Thus score $K$ is achievable iff $|V_K| - \nu(G_{\text{split}}(V_K)) \le N + 1$. If even $K = \max a_u + 1$ is achievable, output `AK`!
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Binary search the answer $K$. Which vertices in the DAG are you *forced* to visit to achieve a score $\ge K$?
  2. *Hint 2*: You must cover the subset of vertices $V_K = \{u : a_u < K\}$ using at most $N+1$ directed walks in the original DAG (which may pass through vertices outside $V_K$ or revisit vertices).
  3. *Hint 3*: Run Floyd–Warshall once on the whole DAG, then for each binary search probe $K$, find the minimum chain cover of the induced sub-poset $V_K$ via Bipartite Matching!


---

### Tier 3: Advanced (`P17–P23`)

---

#### P17 — Codeforces 590 E: Birthday
- **URL**: `https://codeforces.com/problemset/problem/590/E`
- **Constraints**: $N \le 750$ distinct strings over `{a, b}`, $\sum_{i=1}^N |s_i| \le 10^7$. Output maximum size AND indices of pairwise non-substring strings. Time Limit: 3.0s.
- **Step 1–4 — 4-Step Compilation (§5.1)**:
  - **Step 1 (Signal)**: Maximum Antichain on substring poset $(s_i \sqsubset s_j)$, with massive total length $\sum |s_i| \le 10^7$.
  - **Step 2 & 3 (AC Compressed-Link Jump Table + Bitset Transitive Closure)**:
    1. Build Aho–Corasick trie over $s_1, \dots, s_N$ (using a flat `int tr[10000005][2]` array to respect memory limits!).
    2. During BFS fail-link construction, propagate `nearest_word[u] = word_id[u] ? word_id[u] : nearest_word[fail[u]]`.
    3. For each string $j$ and each prefix node $u$ of $s_j$:
       - If $u$ is not the terminal node of $s_j$ and `nearest_word[u] != 0`, add edge `nearest_word[u] -> j`.
       - Also check `nearest_word[fail[u]]` (which is strictly shorter than $u$, so safe even at the terminal node of $s_j$) and add edge `nearest_word[fail[u]] -> j`.
    4. Run $O(N^3 / 64)$ `std::bitset<750>` Floyd–Warshall to obtain the full strict transitive closure $G_{\text{TC}}$.
    5. Run Hopcroft–Karp on $(L, R, G_{\text{TC}})$. Recover Minimum Vertex Cover $C^* = (L \setminus R_S) \cup (R \cap R_S)$ via residual BFS from $S$, and output the Maximum Antichain $I^* = \{i \in \{1..N\} : i_L \in R_S \text{ and } i_R \notin R_S\}$.
  - **Step 4 (Memory Trap)**: With $10^7$ trie nodes, do NOT store `std::vector` per node! Store only `tr[V][2]`, `fail[V]`, and `nearest_word[V]` (`4 * 40 MB = 160 MB`).
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Why does walking `fail[u]` all the way to the root for every prefix of every string TLE when $\sum |s_i| = 10^7$?
  2. *Hint 2*: You only need the **longest** dictionary string that is a suffix of each prefix $u$! Maintain `nearest_word[u]` during BFS and take transitive closure on the $750 \times 750$ graph afterwards.
  3. *Hint 3*: After Hopcroft–Karp on the transitively closed DAG, run residual BFS from $S$ and output all $i$ where $i_L$ IS reachable from $S$ and $i_R$ is NOT reachable from $S$.

---

#### P18 — [SHOI2004] 最小生成树 (`Luogu P2538`)
- **URL**: `https://www.luogu.com.cn/problem/P2538`
- **Constraints**: $N \le 50, M \le 1000$, target spanning tree $T$, unit modification cost $|w'_e - w_e|$ ($L_1$ norm). Time Limit: 1.0s.
- **Step 1–4 — 4-Step Compilation (§5.2)**:
  - **Step 1 & 2 (Fundamental Cycle Inequality + LP Dual)**:
    Tree $T$ is an MST under $w'$ iff $w'_e \le w'_f$ for every non-tree edge $f \notin T$ and every tree edge $e \in P_T(f)$. Setting $w'_e = w_e - x_e$ ($x_e \ge 0, e \in T$) and $w'_f = w_f + y_f$ ($y_f \ge 0, f \notin T$) gives the primal LP:
    $$\min_{x, y \ge 0} \sum_{e \in T} c_e x_e + \sum_{f \notin T} c_f y_f \quad \text{s.t.} \quad x_e + y_f \ge \max(0, w_e - w_f) \;\;\forall e \in P_T(f).$$
  - **Step 3 (Dual Compilation to Bipartite Assignment / MCMF)**:
    By LP Duality, the minimum $L_1$ modification cost equals the **Maximum-Weight Bipartite Matching / Flow** on the bipartite graph $(T, E \setminus T)$ where edge $(e, f)$ ($e \in P_T(f), w_e > w_f$) has weight $\Delta_{e,f} = w_e - w_f$, vertex $e \in T$ has capacity $c_e$, and vertex $f \notin T$ has capacity $c_f$!
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Under what exact condition on fundamental cycles is a spanning tree $T$ a Minimum Spanning Tree?
  2. *Hint 2*: Notice that tree edges only ever need to decrease ($w_e - x_e$) and non-tree edges only ever need to increase ($w_f + y_f$), giving $x_e + y_f \ge w_e - w_f$.
  3. *Hint 3*: Look at the dual of $\min \sum x_e + \sum y_f$ s.t. $x_e + y_f \ge \Delta_{e,f}$: it is the classic Maximum-Weight Bipartite Matching problem between $T$ and $E \setminus T$!

---

#### P19 — [BJWC2018] 最小生成树 (`Inverse MST in L2 Norm`)
- **URL**: `https://loj.ac/p/6392` / `BJWC 2018`
- **Constraints**: $N \le 300, M \le 1000$, target MST $T$, minimize $\sum_{e \in E} (w'_e - w_e)^2$ ($L_2$ norm). Time Limit: 2.0s.
- **Step 1–4 — 4-Step Compilation (§2 & §5.2)**:
  - **Step 1 & 2 (Signal)**: Same fundamental cycle inequalities $w'_e \le w'_f$ ($e \in P_T(f)$) as `P18`, except the objective is the **quadratic $L_2$ norm** $\sum (w'_e - w_e)^2$!
  - **Step 3 (Graph)**: Create a bipartite 2-layer DAG with vertices $V_{\text{DAG}} = T \cup (E \setminus T)$ and directed order edges $e \to f$ for all $e \in P_T(f)$. Run **$L_2$ Isotonic Regression via `整体二分`** (§2.4–2.5) with marginal cost $\Delta_e(m) = (m + 1 - w_e)^2 - (m - w_e)^2 = 2m + 1 - 2w_e$ (for integer $w'_e$) or directional derivative $2(m - w_e)$ (for continuous $w'_e$).
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Write the MST optimality constraints $w'_e \le w'_f$ for every $f \notin T$ and $e \in P_T(f)$.
  2. *Hint 2*: Why does the Kuhn–Munkres LP dual from `[SHOI2004]` no longer apply when the cost function is $(w'_e - w_e)^2$?
  3. *Hint 3*: Because $(w'_e - w_e)^2$ is strictly convex and $w'_e \le w'_f$ are partial order constraints, this is an exact instance of $L_2$ Isotonic Regression (`保序回归`)!

---

#### P20 — [CQOI2014] 危桥 (`Luogu P3163`)
- **URL**: `https://www.luogu.com.cn/problem/P3163`
- **Constraints**: $N \le 50$ vertices, undirected bridges with capacity $2$ (`N`, normal) or $1$ (`O`, fragile). Alice wants $a_n$ round trips between $a_1, a_2$ ($2a_n$ one-way trips); Bob wants $b_n$ round trips between $b_1, b_2$ ($2b_n$ one-way trips). Time Limit: 1.0s.
- **Step 1 — Non-Graph Diagnostic Signal**:
  **Two-Commodity Undirected Flow Feasibility**! A single Max-Flow test from $\{a_1, b_1\} \to \{a_2, b_2\}$ is **insufficient** because flow from $a_1$ might exit at $b_2$ while flow from $b_1$ exits at $a_2$ (cross-routing fallacy!).
- **Step 2 — Intermediate Algebraic Representation (Okamura–Seymour / Two-Commodity Decomposition)**:
  Suppose Run 1 ($S \to a_1$ cap $2a_n$, $S \to b_1$ cap $2b_n$, $a_2 \to T$ cap $2a_n$, $b_2 \to T$ cap $2b_n$) has max flow $2a_n + 2b_n$, realizing net edge flows $\vec{f}_1$ that route $2a_n - \delta$ from $a_1 \to a_2$, $\delta$ from $a_1 \to b_2$, $\delta$ from $b_1 \to a_2$, and $2b_n - \delta$ from $b_1 \to b_2$.
  Now suppose **Run 2** (where we **swap Bob's terminals** $b_1 \leftrightarrow b_2$: $S \to a_1$ cap $2a_n$, $S \to b_2$ cap $2b_n$, $a_2 \to T$ cap $2a_n$, $b_1 \to T$ cap $2b_n$) ALSO has max flow $2a_n + 2b_n$, realizing net edge flows $\vec{f}_2$!
  Because the graph is **undirected** (symmetric capacities on $(u, v)$ and $(v, u)$):
  - Taking the half-sum $\vec{f}_A = \frac{\vec{f}_1 + \vec{f}_2}{2}$ cancels Bob's reversed terminal demands $(+2b_n - 2b_n)/2 = 0$ and routes pure Alice flow $2a_n$ from $a_1 \to a_2$!
  - Taking the half-difference $\vec{f}_B = \frac{\vec{f}_1 - \vec{f}_2}{2}$ cancels Alice's identical terminal demands $(+2a_n - 2a_n)/2 = 0$ and routes pure Bob flow $2b_n$ from $b_1 \to b_2$!
  - Furthermore, on every undirected edge $e$, $|\vec{f}_A(e)| + |\vec{f}_B(e)| = \frac{|\vec{f}_1(e) + \vec{f}_2(e)| + |\vec{f}_1(e) - \vec{f}_2(e)|}{2} = \max(|\vec{f}_1(e)|, |\vec{f}_2(e)|) \le \text{cap}(e)$!
  And because all capacities (`2` for fragile, `INF` for normal) and demands ($2a_n, 2b_n$) are **even**, dividing by $2$ preserves integrality!
- **Step 3 & 4 — Compilation**:
  Give fragile bridges undirected capacity $2$ and normal bridges $\infty$. Run Dinic twice:
  - Run 1: $S \to a_1 (2a_n), S \to b_1 (2b_n), a_2 \to T (2a_n), b_2 \to T (2b_n)$.
  - Run 2: $S \to a_1 (2a_n), S \to b_2 (2b_n), a_2 \to T (2a_n), b_1 \to T (2b_n)$.
  Output `Yes` iff **both** runs achieve flow $2a_n + 2b_n$!
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Why does a single Max-Flow from $\{a_1, b_1\}$ to $\{a_2, b_2\}$ fail? Flow from $a_1$ could illegally go to $b_2$!
  2. *Hint 2*: What happens if you ALSO test the network with $b_1$ and $b_2$ swapped ($S \to b_2$ and $b_1 \to T$)?
  3. *Hint 3*: Add and subtract the two flow vectors $\frac{f_1 + f_2}{2}$ and $\frac{f_1 - f_2}{2}$ to prove that both runs succeeding is both necessary and sufficient!

---

#### P21 — AtCoder AGC 029 F: Construction of a Tree
- **URL**: `https://atcoder.jp/contests/agc029/tasks/agc029_f`
- **Constraints**: $N \le 10^5$, $N-1$ vertex subsets $E_1, \dots, E_{N-1} \subseteq \{1, \dots, N\}$ with $\sum |E_i| \le 2 \times 10^5$. Pick $u_i, v_i \in E_i$ for each $i$ to form a spanning tree. Time Limit: 2.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 & 2 (Rooted Tree Orientation + Hall's Marriage Condition)**:
    Root the target spanning tree at vertex $1$. Every edge $e_i = (u_i, v_i)$ has a unique child endpoint $c_i \in V \setminus \{1\}$ (the endpoint further from root $1$), establishing a **bijection (perfect matching)** between the $N-1$ sets $\{E_1, \dots, E_{N-1}\}$ and the $N-1$ non-root vertices $V \setminus \{1\}$ such that $c_i \in E_i$!
  - **Step 3 (Two-Phase Constructive Algorithm)**:
    1. **Phase 1 (Bipartite Matching)**: Build the bipartite graph between $L = \{E_1, \dots, E_{N-1}\}$ and $R = \{2, 3, \dots, N\}$ (omitting vertex $1$!) where $E_i \to v$ iff $v \in E_i$. Run Dinic ($O(\sum |E_i| \sqrt{N})$). If Max-Flow $< N - 1$, output `-1`!
    2. **Phase 2 (BFS Connectivity Propagation from Root $1$)**:
       Wait—a perfect matching $c_i \in E_i$ is necessary, but could it form disconnected cycles away from $1$? To construct a connected tree rooted at $1$:
       Start a BFS queue with visited vertex $u = 1$. Whenever a vertex $u$ is popped from the queue, iterate over all sets $E_i$ that contain $u$ and have not yet been oriented: set $u$ as the **parent** endpoint of $E_i$ and its matched partner $c_i = M^*(E_i) \in E_i$ as the **child** endpoint of $E_i$ (orienting edge $i$ as $(u, c_i)$), and push $c_i$ into the BFS queue!
       - **Why does this work?** If the BFS terminates before reaching all $N$ vertices, the unvisited vertices $U \subseteq V \setminus \{1\}$ and their matched sets $M^{-1}(U)$ contain **zero** vertices outside $U$—meaning $|M^{-1}(U)| = |U|$ sets are completely trapped inside $U$ vertices, which can never form a tree! Thus the BFS reaches all $N$ vertices iff a valid tree exists!
- **3-Tier Progressive Hints**:
  1. *Hint 1*: If the $N-1$ edges form a tree rooted at vertex $1$, map each edge $i$ to its child endpoint $c_i \in \{2, \dots, N\}$. What graph structure is this?
  2. *Hint 2*: It is a perfect matching between the $N-1$ sets $E_1, \dots, E_{N-1}$ and the $N-1$ vertices $\{2, \dots, N\}$!
  3. *Hint 3*: After finding a perfect matching $c_i = M^*(E_i)$ with Dinic, run a BFS starting from root $1$: whenever visited vertex $u \in E_i$, pair $u$ with $c_i$ as edge $(u, c_i)$ and mark $c_i$ visited!

---

#### P22 — AtCoder ABC 347 G: Grid Coloring 2
- **URL**: `https://atcoder.jp/contests/abc347/tasks/abc347_g`
- **Constraints**: Grid $N \times N$ ($N \le 20$), cells have $A_{r,c} \in \{0, 1, 2, 3, 4, 5\}$ ($0$ means uncolored). Fill $0$s with $\{1..5\}$ to minimize $\sum_{\text{adj } (u,v)} (a_u - a_v)^2$. Time Limit: 2.0s.
- **Step 1–4 — 4-Step Compilation (`noshi91` 5-State Unary Threshold Chain)**:
  - **Step 1 (Signal)**: Multi-state assignment $a_u \in \{1, 2, 3, 4, 5\}$ minimizing a convex pairwise difference $\sum (a_u - a_v)^2$ (`燃やす埋める` with $K = 5$ states).
  - **Step 2 (Intermediate Algebraic Representation — Coarea for Squared Difference)**:
    For each cell $u$, define **$4$ binary threshold indicators** $z_{u,1}, z_{u,2}, z_{u,3}, z_{u,4} \in \{0, 1\}$ where $z_{u,t} = [a_u > t]$ ($t = 1, 2, 3, 4$), subject to the monotonicity chain:
    $$z_{u,1} \ge z_{u,2} \ge z_{u,3} \ge z_{u,4} \quad \text{and} \quad a_u = 1 + \sum_{t=1}^4 z_{u,t}.$$
    How does $(a_u - a_v)^2$ expand in terms of $z_{u,s}$ and $z_{v,t}$? Notice that for any $a_u, a_v \in \{1..5\}$:
    $$(a_u - a_v)^2 = \sum_{s=1}^4 |z_{u,s} - z_{v,s}| + 2 \sum_{1 \le s < t \le 4} \Big( z_{u,t}(1 - z_{v,s}) + z_{v,t}(1 - z_{u,s}) \Big)!$$
    *Verification*: Suppose $a_u = 4$ ($z_u = [1, 1, 1, 0]$) and $a_v = 1$ ($z_v = [0, 0, 0, 0]$).
    - Diagonal terms ($s = t$): $|1 - 0| \times 3 = 3$.
    - Off-diagonal terms ($1 \le s < t \le 3$): there are $\binom{3}{2} = 3$ pairs $(s, t)$ where $z_{u,t} = 1$ and $z_{v,s} = 0$, contributing $2 \times 3 = 6$.
    - Total $= 3 + 6 = 9 = (4 - 1)^2$! Every single term is a pure **non-negative $s$-$t$ cut penalty**!
  - **Step 3 (Mechanical Graph Compilation)**:
    - Create 4 nodes $(u, 1), (u, 2), (u, 3), (u, 4)$ per cell $u$.
    - **Monotonicity Chain ($z_{u,t} = 1 \implies z_{u,t-1} = 1$)**: Add directed edge $(u, t) \xrightarrow{\infty} (u, t-1)$ for $t = 2, 3, 4$.
    - **Pre-colored Cells ($A_u \in \{1..5\}$)**: Lock $z_{u,t} = 1$ ($S \xrightarrow{\infty} (u, t)$) for $t < A_u$, and lock $z_{u,t} = 0$ ($(u, t) \xrightarrow{\infty} T$) for $t \ge A_u$.
    - **Adjacent Cell Penalties $(u, v) \in E$**:
      - For $s \in \{1..4\}$: undirected edge $(u, s) \leftrightarrow (v, s)$ of capacity $1$.
      - For $1 \le s < t \le 4$: directed edge $(u, t) \xrightarrow{2} (v, s)$ and directed edge $(v, t) \xrightarrow{2} (u, s)$ of capacity $2$.
    - Output $\text{MinCut}(S, T)$.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Represent each cell's value $a_u \in \{1..5\}$ using 4 binary threshold variables $z_{u,t} = [a_u > t]$ ($t = 1..4$) with $z_{u,1} \ge z_{u,2} \ge z_{u,3} \ge z_{u,4}$.
  2. *Hint 2*: Expand $(a_u - a_v)^2 = \big(\sum_{t=1}^4 (z_{u,t} - z_{v,t})\big)^2$ using $z^2 = z$ and the monotonicity chain $z_{u,s} z_{u,t} = z_{u,\max(s,t)}$.
  3. *Hint 3*: Verify the exact identity $(a_u - a_v)^2 = \sum_{s=1}^4 |z_{u,s} - z_{v,s}| + 2 \sum_{1 \le s < t \le 4} (z_{u,t}(1 - z_{v,s}) + z_{v,t}(1 - z_{u,s}))$, and compile each term directly into an edge!

---

#### P23 — Codeforces 1517 G: Starry Night Camping
- **URL**: `https://codeforces.com/problemset/problem/1517/G`
- **Constraints**: $N \le 1000$ tents at integer coordinates $(x_i, y_i)$ with weights $w_i \ge 1$. No 4 kept tents may form an axis-aligned L-tromino (3 mutually adjacent corners of a $1 \times 1$ square + a 4th tent adjacent to one of the two end-corners). Maximize kept weight. Time Limit: 2.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 & 2 (4-Phase Parity Signature `(x mod 2, y mod 2)`)**:
    Inspect the coordinate parities $(x \bmod 2, y \bmod 2)$ of any forbidden 4-tent configuration! Because the two central tents of the 4-tent path must share an $x$ or $y$ edge at a specific parity boundary, every forbidden 4-tent path passes through the **exact 4 parity classes in a fixed linear order**:
    $$\text{Type } 0: (\text{odd}, \text{even}) \to \text{Type } 1: (\text{even}, \text{even}) \to \text{Type } 2: (\text{even}, \text{odd}) \to \text{Type } 3: (\text{odd}, \text{odd})!$$
  - **Step 3 (4-Layer Vertex-Split Minimum Cut)**:
    - Split each tent $i$ into $i_{\text{in}} \xrightarrow{w_i} i_{\text{out}}$.
    - Connect $S \xrightarrow{\infty} i_{\text{in}}$ for all Type 0 tents; connect $i_{\text{out}} \xrightarrow{\infty} T$ for all Type 3 tents.
    - For any two tents $i, j$ at Euclidean distance $1$ ($|x_i - x_j| + |y_i - y_j| = 1$) with $\text{Type}(j) = \text{Type}(i) + 1$: add directed edge $i_{\text{out}} \xrightarrow{\infty} j_{\text{in}}$.
    - Output $\sum_{i=1}^N w_i - \text{MinCut}(S, T)$.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Classify every grid point $(x, y)$ into one of 4 types based on $(x \bmod 2, y \bmod 2)$.
  2. *Hint 2*: Check the sequence of types along any forbidden 4-tent path specified in the problem statement!
  3. *Hint 3*: Every forbidden 4-tent path visits Type $0 \to 1 \to 2 \to 3$ in order! Build a 4-layer vertex-split DAG and subtract the $S$-$T$ minimum cut from $\sum w_i$.

---

### Tier 4: Mastery (`P24–P32`)

---

#### P24 — Minimum Rectangle Partition of a Rectilinear Polygon (`Imai–Asano 1986` / `UVa 1711`)
- **URL**: `https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4656`
- **Constraints**: Rectilinear polygon with $N \le 2000$ vertices and $h$ rectilinear holes. Minimize rectangle partition count $R_{\min}$. Time Limit: 2.0s.
- **Step 1–4 — 4-Step Compilation (Full Theory in §4.1–4.3)**:
  - **Step 1 & 2 (Euler–Reflex & Corner Identity, Theorem 4.1)**:
    $$R_{\min} = 1 - h + c_{\text{conc}} - |I^*| = \frac{N}{2} - 1 + h - |I^*|,$$
    where $I^*$ is a Maximum Independent Set in the bipartite intersection graph $G_{\text{chord}} = (V_H \cup V_V, E_{\text{cross}})$ of axis-aligned internal chords connecting pairs of reflex ($270^\circ$) vertices.
  - **Step 3 & 4 (Compilation & Endpoint-Sharing Trap)**:
    - Sweep horizontally and vertically to extract all unobstructed internal reflex-to-reflex chords $V_H$ and $V_V$.
    - Add a conflict edge $(u, v) \in V_H \times V_V$ whenever $u = [x_1, x_2] \times \{y_u\}$ and $v = \{x_v\} \times [y_1, y_2]$ satisfy **$x_1 \le x_v \le x_2$ and $y_1 \le y_u \le y_2$** (using non-strict $\le$ so chords sharing a reflex endpoint conflict!).
    - Compute $|I^*| = |V_H| + |V_V| - \nu(G_{\text{chord}})$ via Hopcroft–Karp.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Every $270^\circ$ reflex vertex needs at least one cut segment starting at it. When does a single cut segment resolve TWO reflex vertices at once?
  2. *Hint 2*: When two reflex vertices are collinear horizontally or vertically and can see each other inside $P$ (an effective chord)!
  3. *Hint 3*: Build the bipartite intersection graph of horizontal and vertical effective chords (including shared reflex endpoints as conflicts) and apply $R_{\min} = 1 - h + c_{\text{conc}} - \text{MIS}(G_{\text{chord}})$.

---

#### P25 — [省选联考 2020 A 卷] 魔法商店 (`Luogu P6621` / `LOJ 3303`) & General $L_p$ Isotonic Regression
- **URL**: `https://www.luogu.com.cn/problem/P6621` / `https://loj.ac/p/3303`
- **Constraints**: $N \le 1000$ items, 64-bit XOR attributes $c_i < 2^{64}$, initial prices $v_i \le 10^6$, basis size $M \le 64$. Given $A$ (min-cost linear basis) and $B$ (max-cost linear basis), modify prices to $f_i \in \mathbb{Z}$ to minimize $\sum_{i=1}^N (f_i - v_i)^2$. Time Limit: 3.0s.
- **Step 1–4 — 4-Step Compilation (Full Theory in §2.1–2.7)**:
  - **Step 1 (Signal)**: Quadratic $L_2$ price modification $\sum (f_i - v_i)^2$ subject to $A$ being a minimum-weight XOR basis and $B$ being a maximum-weight XOR basis.
  - **Step 2 (Linear Basis Fundamental Circuit Inequalities)**:
    - Insert the $M$ vectors of $A$ into a 64-bit XOR Gaussian elimination basis tracking linear combinations. For each $x \notin A$, decompose $c_x = \bigoplus_{a \in C(A, x)} c_a$; for every $a \in C(A, x)$, $A \setminus \{a\} \cup \{x\}$ is a valid basis, which forces:
      $$f_a \le f_x \quad (\text{add directed edge } a \to x).$$
    - Insert the $M$ vectors of $B$ into a second XOR basis. For each $y \notin B$ and each $b \in C(B, y)$, $B \setminus \{b\} \cup \{y\}$ is a valid basis, which forces:
      $$f_y \le f_b \quad (\text{add directed edge } y \to b).$$
  - **Step 3 (`整体二分` + Dinic Compilation)**:
    Run `solve(V_sub, L, R)` over $[0, 10^6]$ with midpoint $m = \lfloor (L + R)/2 \rfloor$:
    - Marginal cost of moving $i$ from $m$ to $m+1$ is $\Delta_i = (m + 1 - v_i)^2 - (m - v_i)^2 = 2m + 1 - 2v_i$.
    - If $\Delta_i < 0$ ($v_i > m$): add $S \xrightarrow{2v_i - 2m - 1} i$.
    - If $\Delta_i > 0$ ($v_i \le m$): add $i \xrightarrow{2m + 1 - 2v_i} T$.
    - Order edges $u \to w$ within $V_{\text{sub}}$: add $u \xrightarrow{\infty} w$.
    - Partition into $V_{>} = R_S$ on $[m+1, R]$ and $V_{\le} = V_{\text{sub}} \setminus R_S$ on $[L, m]$.
  - **Step 4 (Complexity)**: $N \le 1000$, $M_{\text{edges}} \le 2 N M \le 1.28 \times 10^5$, $\log_2(10^6) = 20$ levels; total time $\approx 150$ ms when locally re-indexing $V_{\text{sub}}$!
- **3-Tier Progressive Hints**:
  1. *Hint 1*: By the Matroid Exchange Property, when is $A$ guaranteed to be a minimum-weight XOR basis and $B$ a maximum-weight XOR basis?
  2. *Hint 2*: Express each $x \notin A$ as an XOR sum of elements in $A$ ($c_x = \bigoplus_{a \in C(A, x)} c_a$); then $f_a \le f_x$ for all $a \in C(A, x)$, and symmetrically $f_y \le f_b$ for $B$.
  3. *Hint 3*: You now have $O(NM)$ inequalities $f_u \le f_w$ and want to minimize $\sum (f_i - v_i)^2$—solve via `整体二分` ($L_2$ Isotonic Regression)!

---

#### P26 — [BOI 2004] Sequence (`Luogu P4331`) & DAG $L_1$ Isotonic Regression
- **URL**: `https://www.luogu.com.cn/problem/P4331`
- **Constraints**: $N \le 10^6$, integers $t_1, \dots, t_N$. Construct strictly increasing $z_1 < z_2 < \dots < z_N$ minimizing $\sum_{i=1}^N |z_i - t_i|$. Time Limit: 1.0s.
- **Step 1–4 — 4-Step Compilation (§2.5)**:
  - **Step 1 & 2 (Strict-to-Weak Monotonic Shift)**:
    For integers, $z_1 < z_2 < \dots < z_N \iff z_1 - 1 \le z_2 - 2 \le \dots \le z_N - N$! Set $b_i = z_i - i$ and $y_i = t_i - i$; the problem reduces to standard $L_1$ Isotonic Regression on a 1D chain:
    $$\min_{b_1 \le b_2 \le \dots \le b_N} \sum_{i=1}^N |b_i - y_i|.$$
  - **Step 3 (1D Chain Slope Trick / Leftist Heap vs. General DAG `整体二分`)**:
    - On a **1D chain** ($N \le 10^6$): Maintain a monotone stack of segments $[l_k, r_k]$, each with a max-heap (or Leftist Heap) storing the median of $\{y_i : i \in [l_k, r_k]\}$. Whenever the median of block $k-1$ exceeds the median of block $k$, merge the two heaps and prune to size $\lceil \text{len}/2 \rceil$ in $O(N \log N)$ time!
    - On a **general DAG** ($N \le 1000$): Coordinate-compress $Y = \text{sort\_unique}(y_1, \dots, y_N)$ and run `整体二分` over $[1, |Y|]$ in $O(\text{MaxFlow}(N, M) \log N)$ time!
- **3-Tier Progressive Hints**:
  1. *Hint 1*: How do you transform the strict inequality $z_i < z_{i+1}$ on integers into a non-strict inequality $b_i \le b_{i+1}$?
  2. *Hint 2*: Substitute $b_i = z_i - i$ and $y_i = t_i - i$. For any contiguous block where $b_l = b_{l+1} = \dots = b_r = c$, what value of $c$ minimizes $\sum_{i=l}^r |c - y_i|$?
  3. *Hint 3*: The median of $\{y_l, \dots, y_r\}$! Maintain a monotone stack of block medians using mergeable Leftist Heaps (or Slope Trick priority queue).

---

#### P27 — AtCoder AGC 038 F: Two Permutations
- **URL**: `https://atcoder.jp/contests/agc038/tasks/agc038_f`
- **Constraints**: $N \le 10^5$, two permutations $P, Q$ of $0..N-1$. Construct $A, B$ where $A_i \in \{i, P_i\}$ and $B_i \in \{i, Q_i\}$ are valid permutations to maximize $\#\{i : A_i \neq B_i\}$. Time Limit: 2.0s.
- **Step 1–4 — 4-Step Compilation (§6.3)**:
  - **Step 1 (Cycle Binary Locking)**: For $A_i \in \{i, P_i\}$ to remain a permutation (bijection), every cycle $C$ of $P$ must either **stay completely fixed** ($A_i = i \; \forall i \in C$, state $x_C = 0$) or **shift completely along $P$** ($A_i = P_i \; \forall i \in C$, state $x_C = 1$)! Similarly, each cycle $D$ of $Q$ has a single binary state $y_D \in \{0, 1\}$.
  - **Step 2 (Bipartite Flip Rescue of Supermodularity)**:
    Maximizing $\#\{i : A_i \neq B_i\}$ is equivalent to **$N - \min \#\{i : A_i == B_i\}$**. For each position $i \in \{0..N-1\}$ belonging to $P$-cycle $C$ and $Q$-cycle $D$, when does $A_i == B_i$ (paying penalty $1$)?
    - Notice that $x_C = 0 \land y_D = 0 \implies A_i = i = B_i$! In original variables $(x_C, y_D)$, this penalizes $x_C = y_D = 0$, which is **supermodular**!
    - **Bipartite Variable Inversion**: Since every position $i$ only ever connects a $P$-cycle $C$ to a $Q$-cycle $D$, the interaction graph is **bipartite**! Invert all $Q$-cycle variables by setting $z_D = 1 - y_D$ ($z_D = 1 \iff B_i = i$, $z_D = 0 \iff B_i = Q_i$)!
  - **Step 3 (Case-by-Case Mechanical Compilation for Position $i$)**:
    With $x_C = [A_i = P_i]$ ($x_C = 1$ means $C \in S$) and $z_D = [B_i = i]$ ($z_D = 1$ means $D \in S$), check the 5 cases of $(P_i, Q_i)$:
    1. $P_i == i$ and $Q_i == i$: Always $A_i = B_i = i$; constant penalty $+1$.
    2. $P_i == i$ and $Q_i \neq i$: $A_i = B_i \iff B_i = i \iff z_D = 1 \implies$ edge $D \xrightarrow{1} T$.
    3. $P_i \neq i$ and $Q_i == i$: $A_i = B_i \iff A_i = i \iff x_C = 0 \implies$ edge $S \xrightarrow{1} C$.
    4. $P_i \neq i, Q_i \neq i$, and $P_i \neq Q_i$: $A_i = B_i \iff (A_i = i \land B_i = i) \iff (x_C = 0 \land z_D = 1) \implies$ directed edge $D \xrightarrow{1} C$.
    5. $P_i \neq i, Q_i \neq i$, and $P_i == Q_i$: $A_i = B_i \iff (x_C = 0 \land z_D = 1) \lor (x_C = 1 \land z_D = 0) \iff x_C \neq z_D \implies$ undirected edge $C \leftrightarrow D$ of capacity $1$!
    Output $N - \text{const} - \text{MinCut}(S, T)$ in $O(N\sqrt{N})$ time!
- **3-Tier Progressive Hints**:
  1. *Hint 1*: For $A_i \in \{i, P_i\}$ to form a valid permutation, can you choose $A_i = P_i$ for only *part* of a cycle of $P$?
  2. *Hint 2*: Each cycle $C$ of $P$ is a single binary variable $x_C \in \{0, 1\}$, and each cycle $D$ of $Q$ is a single binary variable $y_D \in \{0, 1\}$.
  3. *Hint 3*: Flip the $Q$-cycle variables via $z_D = 1 - y_D$ so that $A_i = B_i = i$ becomes the cut condition $(z_D = 1 \land x_C = 0)$, and run Dinic!

---

#### P28 — AtCoder ARC 107 F: Sum of Abs
- **URL**: `https://atcoder.jp/contests/arc107/tasks/arc107_f`
- **Constraints**: $N, M \le 300$, deletion cost $A_i \ge 0$, signed value $|B_i| \le 10^6$. Delete a subset of vertices; for each remaining connected component $C$, earn $|\sum_{v \in C} B_v|$. Maximize net score. Time Limit: 2.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 & 2 (Linearizing $|\sum_{v \in C} B_v|$ into 3 States $\{-1, \text{del}, +1\}$)**:
    Notice that $|X| = \max_{s \in \{-1, +1\}} s \cdot X$! Thus choosing a sign $s_C \in \{-1, +1\}$ for each remaining connected component $C$ is equivalent to assigning every vertex $v \in V$ one of **3 states**:
    - **State $+$ ($v$ kept with $+1$ multiplier)**: earns $+B_v$.
    - **State $-$ ($v$ kept with $-1$ multiplier)**: earns $-B_v$.
    - **State $0$ ($v$ deleted)**: pays $-A_v$ (so net gain relative to $|B_v|$ is $-(A_v + |B_v|)$).
    Constraint: No kept vertex in State $+$ can be adjacent to a kept vertex in State $-$!
  - **Step 3 (Vertex-Split 3-State Cut Gadget)**:
    Start from the optimistic baseline $\text{Base} = \sum_{v=1}^N |B_v|$ (assuming every vertex gets its preferred sign!). Split each vertex $v$ into $v_{\text{in}}$ and $v_{\text{out}}$:
    - **State $+$**: $v_{\text{in}} \in S, v_{\text{out}} \in S$ (cuts $v_{\text{out}} \to T$).
    - **State $-$**: $v_{\text{in}} \in T, v_{\text{out}} \in T$ (cuts $S \to v_{\text{in}}$).
    - **State $0$ (Deleted)**: $v_{\text{in}} \in S, v_{\text{out}} \in T$ (cuts internal edge $v_{\text{in}} \to v_{\text{out}}$).
    Set capacities to match the exact penalties from $\text{Base} = \sum |B_v|$:
    - Internal edge $v_{\text{in}} \xrightarrow{A_v + |B_v|} v_{\text{out}}$ (deleting $v$ loses $|B_v|$ and pays $A_v$).
    - If $B_v > 0$: choosing State $-$ loses $2B_v \implies S \xrightarrow{2B_v} v_{\text{in}}$; choosing State $+$ loses $0$.
    - If $B_v < 0$: choosing State $+$ loses $2|B_v| \implies v_{\text{out}} \xrightarrow{2|B_v|} T$; choosing State $-$ loses $0$.
    - For each undirected edge $(u, v) \in E$: forbid $(u \text{ in } +) \land (v \text{ in } -)$ via $u_{\text{out}} \xrightarrow{\infty} v_{\text{in}}$ and $v_{\text{out}} \xrightarrow{\infty} u_{\text{in}}$!
    Output $\sum_{v=1}^N |B_v| - \text{MinCut}(S, T)$.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Rewrite $|\sum_{v \in C} B_v|$ as $\max_{s \in \{-1, +1\}} \sum_{v \in C} s \cdot B_v$. What does this imply for adjacent kept vertices $u$ and $v$?
  2. *Hint 2*: Every vertex $v$ is assigned to $\{+, 0 (\text{deleted}), -\}$, and an edge $(u, v)$ forbids one endpoint being $+$ while the other is $-$.
  3. *Hint 3*: Split each vertex into $v_{\text{in}} \xrightarrow{A_v + |B_v|} v_{\text{out}}$, where $(S, S)$ is $+$, $(S, T)$ is deleted, and $(T, T)$ is $-$, with $u_{\text{out}} \xrightarrow{\infty} v_{\text{in}}$ forbidding $+\to-$ adjacency!

---

#### P29 — AtCoder ARC 142 E: Pairing Wizards
- **URL**: `https://atcoder.jp/contests/arc142/tasks/arc142_e`
- **Constraints**: $N \le 100$ wizards, initial strengths $a_i \le 100$, target $b_i \le 100$. For each pair $(u, v) \in E$: $\min(x_u, x_v) \ge \min(b_u, b_v)$ and $\max(x_u, x_v) \ge \max(b_u, b_v)$. Minimize $\sum (x_i - a_i)$. Time Limit: 2.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 & 2 (Hard Lower Bounds + Bipartite Dominance Split)**:
    First, $\min(x_u, x_v) \ge \min(b_u, b_v)$ means **both** $x_u \ge \min(b_u, b_v)$ and $x_v \ge \min(b_u, b_v)$ unconditionally! Update every wizard's mandatory base strength:
    $$L_u = \max\Big(a_u, \max_{(u, v) \in E} \min(b_u, b_v)\Big).$$
    Now consider any pair $(u, v) \in E$ where $\max(b_u, b_v) > \min(b_u, b_v)$, say $b_u < b_v$. If $L_u \ge b_v$ or $L_v \ge b_v$, the constraint $\max(x_u, x_v) \ge b_v$ is already satisfied! Otherwise, we have $L_v < b_v$, which implies that **no neighbor of $v$ has $\min(b_v, b_w) \ge b_v$**—so for every edge incident to $v$, $b_v$ is the strict maximum!
    Consequently, vertices split into two disjoint sets: **High-Demand Wizards** $H = \{v : L_v < b_v\}$ and **Helper Wizards** $W = \{u : L_u \ge b_u\}$! Every remaining constraint $(u, v)$ has $u \in W, v \in H$ and requires:
    $$x_v \ge b_v \quad \text{OR} \quad x_u \ge b_v \iff \text{if } x_v < b_v, \text{ then } x_u \ge b_v!$$
  - **Step 3 (Compilation to Unary Threshold Cut)**:
    - Each $v \in H$ only ever takes one of two values: $x_v = L_v$ (stays at base, $v \in S$) or $x_v = b_v$ (upgraded to $b_v$ at cost $b_v - L_v$, $v \in T$). Add edge $S \xrightarrow{b_v - L_v} v$.
    - Each $u \in W$ has a unary threshold chain $(u, t)$ for $t = L_u + 1, \dots, 100$ where $(u, t) \in S$ means $x_u \ge t$: add $(u, t) \xrightarrow{1} T$ and $(u, t) \xrightarrow{\infty} (u, t-1)$.
    - For each edge $(u, v)$ with $v \in H, u \in W$: if $v \in S$ ($x_v = L_v < b_v$), then we must have $x_u \ge b_v$ ($(u, b_v) \in S$) $\implies$ add $v \xrightarrow{\infty} (u, b_v)$!
    - Output $\sum_{i=1}^N (L_i - a_i) + \text{MinCut}(S, T)$.
- **3-Tier Progressive Hints**:
  1. *Hint 1*: First, $\min(x_u, x_v) \ge \min(b_u, b_v)$ forces both $x_u$ and $x_v$ to be at least $\min(b_u, b_v)$. Raise every $a_i$ to this mandatory lower bound $L_i$ first!
  2. *Hint 2*: Prove that if a wizard $v$ still has $L_v < b_v$, then for EVERY edge $(u, v)$ incident to $v$, we must have $b_u \le L_v < b_v$, so $u$ already satisfies $L_u \ge b_u$!
  3. *Hint 3*: Thus wizards with $L_v < b_v$ only make a binary decision $x_v \in \{L_v, b_v\}$, while wizards with $L_u \ge b_u$ use a unary chain of length $\le 100$!

---

#### P30 — Codeforces 1427 G: One Billion Shades of Grey
- **URL**: `https://codeforces.com/problemset/problem/1427/G`
- **Constraints**: Grid $N \times N$ ($N \le 200$), border cells pinned to $b_{r,c} \in [1, 10^9]$, obstacles `-1`, interior `0`. Minimize $\sum_{\text{adj}} |a_u - a_v|$. Time Limit: 2.0s.
- **Step 1–4 — 4-Step Compilation (§7.1)**:
  - **Step 1 & 2 (Discrete Coarea Formula)**:
    Let $v_1 < v_2 < \dots < v_K$ ($K \le 4N \le 800$) be the sorted unique values of the pinned border cells. By Theorem 7.1 (Discrete Coarea Identity):
    $$\min_{a} \sum_{(u,w) \in E} |a_u - a_w| = \sum_{k=1}^{K-1} (v_{k+1} - v_k) \cdot \text{MinCut}_k,$$
    where $\text{MinCut}_k$ is the minimum cut on the grid when border cells with $b_u > v_k$ are connected to $S$ ($x_u = 1$) and border cells with $b_u \le v_k$ are connected to $T$ ($x_u = 0$).
  - **Step 3 & 4 (Incremental Residual Re-Optimization / Flow Rollback `退流`)**:
    Running Dinic from scratch $K \le 800$ times on $N^2 = 4 \times 10^4$ vertices would TLE! Instead, as $k$ advances from $1$ to $K-1$, only the border cells with $b_u == v_k$ switch from $S$ ($S \xrightarrow{\infty} u$) to $T$ ($u \xrightarrow{\infty} T$)!
    To switch a border cell $u$ from $S$ to $T$ in the **existing residual graph**:
    1. If $S \to u$ currently carries flow $f \le 4$ (at most $4$ because $u$ has $\le 4$ grid neighbors of capacity $1$!), push up to $f$ units of flow backward from $u$ to $S$ (or from $T$ to $u$) along residual paths of length $\le N^2$ using simple DFS/BFS!
    2. Zero out the edge $S \to u$, add edge $u \xrightarrow{\infty} T$, and run Dinic on the updated residual network to find any newly created $S \to T$ augmenting paths!
    Since each grid edge has capacity $1$ and at most $4N$ border cells ever switch, total flow pushed and rolled back across all $K$ steps is $O(N^2)$, running in $\approx 150$ ms!
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Apply the Coarea Identity $|a_u - a_w| = \sum_{k=1}^{K-1} (v_{k+1} - v_k) |[a_u > v_k] - [a_w > v_k]|$.
  2. *Hint 2*: Notice that for each interval $(v_k, v_{k+1})$, minimizing $\sum |[a_u > v_k] - [a_w > v_k]|$ is a unit-capacity $S$-$T$ minimum cut on the grid!
  3. *Hint 3*: Instead of rebuilding the graph $4N$ times, incrementally move border vertices with $b_u = v_k$ from $S$ to $T$ by rolling back their $\le 4$ units of flow in the residual graph!

---

#### P31 — [NOI2009] 植物大战僵尸 (`Luogu P2805`)
- **URL**: `https://www.luogu.com.cn/problem/P2805`
- **Constraints**: Grid $N \times M$ ($N \le 20, M \le 30$), scores $s_{r,c} \in [-10^4, 10^4]$, protection links $u \to v$ plus right-to-left row protection $(r, c) \to (r, c-1)$. Maximize score. Time Limit: 1.0s.
- **Step 1–4 — 4-Step Compilation**:
  - **Step 1 (Signal)**: Maximum-Weight Closure with **Directed Cycles of Mutual Protection**!
  - **Step 2 & 3 (Topological Kahn Pruning + Closure Cut)**:
    - If plant $u$ protects plant $v$, then eating $v$ **requires** eating $u$ first ($v \implies u$).
    - **The Cycle Trap**: If $u_1, \dots, u_k$ form a cycle of protection (or are protected by a cycle), **none of them can ever be eaten**, even if their scores are $+10^4$! A raw Max-Weight Closure cut would happily include a positive-sum cycle in the $S$-set (`x = 1`), producing an illegal answer!
    - **Mandatory Preprocessing**: Build the protection graph where edges go from `protector -> protected` ($u \to v$), and run **Kahn's Topological Sort (in-degree $0$ queue)**! Only vertices visited by Kahn's algorithm are valid; delete all unvisited vertices before running Max-Weight Closure (`燃やす埋める`)!
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Remember that zombies enter from the right, so $(r, c)$ automatically protects $(r, c-1)$!
  2. *Hint 2*: What happens if two plants protect each other in a cycle, and both have positive scores? Would a standard Project Selection Min-Cut pick them?
  3. *Hint 3*: Yes, which is illegal! First run Kahn's algorithm (topological sort from in-degree $0$ protectors) to discard all plants trapped in or behind cycles, then run Max-Weight Closure on the surviving DAG!

---

#### P32 — [NOI2010] 海拔 (`Luogu P2046`)
- **URL**: `https://www.luogu.com.cn/problem/P2046`
- **Constraints**: Grid $(N+1) \times (N+1)$ ($N \le 500$), North/West border altitude $0$, South/East border altitude $1$, directed traffic weights $w_{u \to v}$. Minimize $\sum w_{u \to v} \max(0, h_v - h_u)$. Time Limit: 2.0s.
- **Step 1–4 — 4-Step Compilation (§7.1)**:
  - **Step 1 & 2 (Coarea Threshold Rounding to $\{0, 1\}$)**:
    By Theorem 7.1, for any assignment $h : V \to [0, 1]$ with boundary values in $\{0, 1\}$:
    $$\sum_{(u,v) \in E} w_{u \to v} \max(0, h_v - h_u) = \int_0^1 \text{Cut}_w\big(\{x : h_x > \lambda\}\big) \, d\lambda \ge \min_{\lambda \in (0, 1)} \text{Cut}_w(E_\lambda).$$
    Thus there always exists an optimal altitude map where **every vertex has $h_v \in \{0, 1\}$**, reducing the problem to a single directed $s$-$t$ Minimum Cut on a $(N+1) \times (N+1)$ planar grid!
  - **Step 3 & 4 (Planar Dual $s^*$-$t^*$ Dijkstra)**:
    Because $V = 2.5 \times 10^5$ is large for general Dinic, construct the **Planar Dual Graph** (`Zhou Dong 2009`):
    - Dual source $S^*$ corresponds to the outer face along the South/West boundary; dual sink $T^*$ corresponds to the outer face along the North/East boundary.
    - Each interior $1 \times 1$ grid square is a dual vertex.
    - Each primal directed edge $u \to v$ ( separating altitude $0$ on one side from altitude $1$ on the other) becomes a **directed dual edge** rotated $90^\circ$ with weight $w_{u \to v}$.
    Run **Dijkstra's Algorithm** from $S^*$ to $T^*$ in $O(N^2 \log N)$ time ($\approx 80$ ms)!
- **3-Tier Progressive Hints**:
  1. *Hint 1*: Do you ever need fractional altitudes $0 < h_v < 1$, or can every vertex optimally take $h_v \in \{0, 1\}$?
  2. *Hint 2*: Use the Coarea integral $\int_0^1 \text{Cut}(h > \lambda) d\lambda$ to prove that an optimal $\{0, 1\}$ solution always exists, reducing the problem to a directed $s$-$t$ Minimum Cut!
  3. *Hint 3*: Since $(N+1)^2 \approx 2.5 \times 10^5$ is a planar $s$-$t$ network, convert the directed $s$-$t$ Min-Cut into a directed shortest path in the Planar Dual Graph and run Dijkstra in $O(N^2 \log N)$!

---

## 9. Reconciled Quarantined Template Problems Table (`R-01` to `R-15`)

In accordance with `PLAN.md`, the following 15 pure-template or non-flow problems are quarantined from the curated problem bank so they do not dilute pedagogical space:

| Quarantine ID | Problem Name & Judge ID | Reason for Quarantine |
| :--- | :--- | :--- |
| **R-01** | `LOJ 6000 / Luogu P2756 (飞行员配对方案问题)` | Pure textbook unweighted Bipartite Matching template. |
| **R-02** | `LOJ 6004 / Luogu P3254 (圆桌问题)` | Pure textbook Bipartite Multi-Matching template. |
| **R-03** | `LOJ 6006 / Luogu P2763 (试题库问题)` | Pure textbook Bipartite Multi-Assignment template (`#05` duplicate). |
| **R-04** | `LOJ 6010 / Luogu P4016 (负载平衡问题)` | Trivial circular transshipment MCMF (or $O(N \log N)$ prefix-sum median). |
| **R-05** | `LOJ 6011 / Luogu P4015 (运输问题)` | Pure textbook Hitchcock Bipartite Transportation MCMF template. |
| **R-06** | `LOJ 6012 / Luogu P4014 (分配问题)` | Pure textbook Bipartite Assignment MCMF template. |
| **R-07** | `LOJ 6009 / Luogu P2761 (软件补丁问题)` | **Non-Flow Trap #1**: $2^{20}$ Bitmask Dijkstra. |
| **R-08** | `LOJ 6016 / Luogu P4011 (孤岛营救问题)` | **Non-Flow Trap #2**: Grid + Key-Bitmask BFS. |
| **R-09** | `LOJ 6021 / Luogu P4009 (汽车加油行驶问题)` | **Non-Flow Trap #3**: Layered Fuel-State Dijkstra. |
| **R-10** | `LOJ 6023 / Luogu P2769 (猴子上树)` | **Non-Flow Trap #4**: Sort + $O(NM)$ DP. |
| **R-11** | `Luogu P3376 (【模板】网络最大流)` | Pure Dinic / ISAP library verification problem. |
| **R-12** | `Luogu P3381 (【模板】最小费用最大流)` | Pure SSP / Primal-Dual MCMF library verification problem. |
| **R-13** | `Luogu P3386 (【模板】二分图最大匹配)` | Pure Hopcroft–Karp library verification problem. |
| **R-14** | `AtCoder Practice2 D (Maxflow)` | Pure ACL `mf_graph` chessboard domino template. |
| **R-15** | `AtCoder Practice2 E (MinCostFlow)` | Pure ACL `mcf_graph` grid selection template. |

---

## 10. Unified Multilingual (`[EN]` / `[ZH]` / `[JA]`) Bibliography

### 10.1 English (`[EN]`) Foundational Papers & Textbooks
1. **[EN] Chakravarti, N. (1989)**. *"Isotonic median regression: a linear programming approach."* Mathematics of Operations Research, 14(2), 303–308. *(Foundational LP duality & threshold cut formulation for $L_1$ isotonic regression).*
2. **[EN] Hochbaum, D. S., & Queyranne, M. (2003)**. *"Minimizing a convex cost closure set."* SIAM Journal on Discrete Mathematics, 16(2), 192–207. *(Parametric minimum cut & threshold binary search for convex closures and $L_p$ isotonic regression).*
3. **[EN] Picard, J. C. (1976)**. *"Maximal closure of a graph and applications to combinatorial problems."* Management Science, 22(11), 1268–1272. *(Original Maximum-Weight Closure theorem).*
4. **[EN] Kolmogorov, V., & Zabih, R. (2004)**. *"What energy functions can be minimized via graph cuts?"* IEEE TPAMI, 26(2), 147–159. *(Submodularity characterization $B + C \ge A + D$ for binary pseudo-Boolean cut representability).*
5. **[EN] Ishikawa, H. (2003)**. *"Exact optimization for Markov random fields with convex priors."* IEEE TPAMI, 25(10), 1333–1336. *(Unary threshold chains & Monge convex interaction edges).*
6. **[EN] Strang, G. (1983)**. *"Maximal flow through a domain."* Mathematical Programming, 26(2), 123–143. *(Continuous Max-Flow / Min-Cut duality and Total Variation Coarea integral).*
7. **[EN] Rudin, L. I., Osher, S., & Fatemi, E. (1992)**. *"Nonlinear total variation based noise removal algorithms."* Physica D, 60(1–4), 259–268. *(ROF Total Variation denoising model).*
8. **[EN] Chambolle, A. (2004) & Darbon, J., & Sigelle, M. (2006)**. *"Image restoration with discrete constrained Total Variation."* JMIV, 26(3), 261–276. *(Exact level-set Coarea decomposition of discrete Total Variation via parametric minimum cuts).*
9. **[EN] Von Neumann, J. (1953)**. *"A certain zero-sum two-person game equivalent to the optimal assignment problem."* Contributions to the Theory of Games, Vol. II, 5–12. *(Hide-and-Seek matrix game equivalence to Bipartite Matching / Kőnig duality).*
10. **[EN] Dulmage, A. L., & Mendelsohn, N. S. (1958)**. *"Coverings of bipartite graphs."* Canadian Journal of Mathematics, 10, 517–534. *(Canonical $(\mathcal{E}, \mathcal{O}, \mathcal{U})$ bipartite decomposition for alternating walk games).*
11. **[EN] Lipski, W., Lodi, E., Luccio, F., Mugnai, C., & Pagli, L. (1979) & Imai, H., & Asano, T. (1986)**. *"Efficient algorithms for geometric graph search problems."* SIAM Journal on Computing, 15(2), 478–494. *(Minimum rectangle partition of rectilinear polygons via chord intersection bipartite MIS).*
12. **[EN] Bruhat, R. A. (1969)**. *"Comments on bases in dependence structures."* Bulletin of the Australian Mathematical Society, 1(2), 161–167. *(Strong symmetric basis bijection theorem for matroid exchange graphs).*
13. **[EN] Okamura, H., & Seymour, P. D. (1981)**. *"Multicommodity flows in planar graphs."* Journal of Combinatorial Theory, Series B, 31(1), 75–81. *(Two-commodity flow sum/difference decomposition in undirected networks).*

### 10.2 Chinese (`[ZH]`) National Team Papers & Monographs
14. **[ZH] 胡伯涛 (Hu Botao / Amber, 2007)**. *《最小割模型在信息学竞赛中的应用》 (Applications of Minimum Cut Models in Olympiad in Informatics)*. 2007 国家集训队论文. *(Seminal Chinese reference on Max-Weight Closure, Maximum Density Subgraph, and pseudo-Boolean posiform cuts).*
15. **[ZH] 高睿泉 (Gao Ruiquan, 2018)**. *《浅谈保序回归问题》 (On the Isotonic Regression Problem)*. 2018 国家集训队论文. *(Definitive competitive programming reference on $L_p$ Isotonic Regression via `整体二分` + Dinic and matroid basis exchange reductions).*
16. **[ZH] 周冬 (Zhou Dong, 2009)**. *《浅谈平面图最小割》 (On Minimum Cuts in Planar Graphs)*. 2009 国家集训队论文. *(Planar $s$-$t$ Min-Cut $\leftrightarrow$ Dual Shortest Path theorem).*
17. **[ZH] 姜志豪 (Jiang Zhihao, 2016)**. *《网络流的一些建模方法》 (Some Modelling Methods in Network Flows)*. 2016 国家集训队论文. *(Algebraic equation differencing and bounded circulations).*
18. **[ZH] LibreOJ (`LOJ 6000–6023`) & OI-Wiki**. *《线性规划与网络流 24 题》 (24 Problems in Linear Programming and Network Flows)*. `https://loj.ac/p?keyword=网络流24题` & `https://oi-wiki.org/graph/flow/`.

### 10.3 Japanese (`[JA]`) `燃やす埋める` Treatises & Algorithm Blogs
19. **[JA] `noshi91` (2019)**. *「燃やす埋める問題と劣モジュラ関数のグラフ表現可能性」 (Project Selection Problem and Graph Representability of Submodular Functions)*. `https://noshi91.hatenablog.com/entry/2021/06/29/044225`. *(Canonical derivation of $K$-state unary threshold chains and Monge edge capacities).*
20. **[JA] `maspypy` (2020)**. *「燃やす埋める」と二部グラフの反転 (Burn-or-Bury and Bipartite Variable Inversion)*. `https://maspypy.com/atcoder-燃やす埋める`. *(Systematic treatment of bipartite variable inversion $y_j = 1 - x_j$ to rescue supermodular rewards).*
21. **[JA] `tatyam` (2022)**. *「k 値の燃やす埋める」 (K-Valued Burn-or-Bury Optimization)*. AtCoder Editorial & Competitive Programming Notes (`ABC 347 G`, `ARC 142 E`).
