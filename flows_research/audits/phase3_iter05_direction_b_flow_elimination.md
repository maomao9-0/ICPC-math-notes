# Phase 3 Global Audit — Iteration 05: Direction B Flow Elimination (`Flow -> Non-Flow Fast Algorithm`) Across All 14 Canonical Archetypes (`Rev-01`–`Rev-14`)

**Audit Date**: 2026-10-20  
**Scope**: Chapters `Ch 08`, `Ch 13`, `Ch 15`, `Ch 16`, `Ch 22`, `Ch 23`, `Ch 24` + `CP-IV` & `CP-VI`  
**Audit Objective**: Verify that every single one of the **14 Canonical Direction B Reverse-Reduction Archetypes (`Rev-01` through `Rev-14`)**—where a problem is first formulated as a flow, cut, matching, or MCMF network, and then compiled *away* into an $O(N \log N)$ or $O(N \log^2 N)$ combinatorial/greedy/DP/data-structure algorithm because $N \ge 10^5$—is proved from first principles, anchored by a concrete problem, and verified by an exact oracle where applicable.

---

## 1. Complete Verification Matrix of the 14 Direction B Archetypes (`Rev-01`–`Rev-14`)

| Reverse ID | Direction B Transformation (`Flow Model -> Fast Non-Flow Algorithm`) | Complexity Upgrade | Textbook Anchor Chapter & Section | Concrete Problem Anchor(s) | Verification Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **`Rev-01`** | Interval / Geometric Bipartite Matching $\to$ Earliest-Deadline Greedy Sweep | $O(N^{1.5}) \mapsto O(N \log N)$ | [`Ch 08` Section 4](../../flows/chapters/ch08-poset-dilworth-hall-flow-elimination.qmd) | Interval Matching / `ARC 147 E — Examination` (`#213`) | **PASS** |
| **`Rev-02`** | $2^K$ Small-Side Hall's Condition $\to$ Bitmask SOS DP + Binary Search | $O(D \cdot N \sqrt{D}) \mapsto O(K 2^K \log D)$ | [`Ch 08` Section 4 & `#062`](../../flows/chapters/ch08-poset-dilworth-hall-flow-elimination.qmd) | `ARC 106 E — Medals` (`#062`), `CF 1009 G — Allowed Letters` (`#060`) | **PASS** |
| **`Rev-03`** | Contiguous Interval Hall's Condition ($|N(I)| \ge |I|$) $\to$ Prefix-Sum Lazy Segment Tree | $O(N^{1.5}) \mapsto O(N \log N)$ | [`Ch 08` Section 4 & `#063`](../../flows/chapters/ch08-poset-dilworth-hall-flow-elimination.qmd) | `CF 981 F — Round Marriage`, `[NOI2009] Lunar New Year` | **PASS** |
| **`Rev-04`** | 2D Poset Minimum Chain Cover $\to$ Dilworth Maximum Antichain (LIS / Fenwick Tree) | $O(N^{2.5}) \mapsto O(N \log N)$ | [`Ch 08` Section 2 & `#061`](../../flows/chapters/ch08-poset-dilworth-hall-flow-elimination.qmd) | `[TJOI2015] 组合数学` (`#059`), Missile Interception | **PASS** |
| **`Rev-05`** | Symmetric Complete Bipartite Cut $\to$ Sorted Prefix Sweep $\min_{k} C(k)$ | $O(N^2 \sqrt{N}) \mapsto O(N \log N)$ | [`Ch 12` `#091` / `Ch 13`](../../flows/chapters/ch12-multi-state-unary-chains-threshold-cuts.qmd) | `ARC 125 E — Snack` (`#091` / `#102`) | **PASS** |
| **`Rev-06`** | $(s, t)$-Planar Grid Minimum Cut $\to$ Dual Graph Shortest Path (`Dijkstra`) | $O(N^3) \mapsto O(N^2 \log N)$ | [`Ch 15` Sections 1–3](../../flows/chapters/ch15-planar-cycle-cut-duality-shortest-paths.qmd) | `[ICPC-Beijing 2006] 狼抓兔子` (`#113`), `[NOI2010] 海拔` (`#114`) | **PASS** (`oracle_ch15`) |
| **`Rev-07`** | Multi-Terminal Planar Boundary Cut $\to$ Dual Boundary Splits + Non-Crossing Interval DP | $O(Q \cdot N^3) \mapsto O(k N^2 \log N + k^3)$ | [`Ch 15` Section 4 & `#119`](../../flows/chapters/ch15-planar-cycle-cut-duality-shortest-paths.qmd) | `[CSP-S 2021] 交通规划` (`#119`) | **PASS** |
| **`Rev-08`** | Prefix-DAG $s$-$t$ Minimum Cut $\to$ $O(N^2)$ Cut DP & $O(N \log N)$ Slope-Difference Greedy | $O(N^2 \sqrt{N}) \mapsto O(N \log N)$ | [`Ch 16` Section 2 & `#121`](../../flows/chapters/ch16-mincut-dp-global-mincut-gomory-hu-trees.qmd) | `CF 724 E — Goods Transportation` (`#121`) | **PASS** |
| **`Rev-09`** | Dynamic Path-Graph $s$-$t$ Min-Cut with Point Updates $\to$ $2 \times 2$ $(\min, +)$ Matrix Segment Tree | $O(Q \cdot N^{1.5}) \mapsto O((N + Q)\log N)$ | [`Ch 16` Section 2 & `#128`](../../flows/chapters/ch16-mincut-dp-global-mincut-gomory-hu-trees.qmd) | `CF 1919 F2 — Wine Factory (Hard)` (`#128`), `CF 1913 F` | **PASS** |
| **`Rev-10`** | Tree / Project-Selection Cut $\to$ Subtree Slope-Trick / Convex Hull Merge DP | $O(N^{2.5}) \mapsto O(N \log N)$ | [`Ch 16` Section 2 & `#125`](../../flows/chapters/ch16-mincut-dp-global-mincut-gomory-hu-trees.qmd) | Tree Cut DP / `CF 1919 F2` | **PASS** |
| **`Rev-11`** | 1D Stock Trading / Buying-Selling MCMF $\to$ Regret Greedy (`反悔贪心`) with 1 Min-Heap | $O(N^2 \log N) \mapsto O(N \log N)$ | [`Ch 23` Section 1 & `#177`](../../flows/chapters/ch23-simulated-mcmf-regret-greedy-heap-segtree.qmd) | `CF 865 D — Buy Low Sell High` (`#177`) | **PASS** (`oracle_ch23`) |
| **`Rev-12`** | $k$-Selection / Bipartite Matching with Residual Back-Arcs $\to$ Dual-Heap / Doubly-Linked List Regret | $O(N \cdot k \log N) \mapsto O(N \log N)$ | [`Ch 23` Section 2 & `#178`–`#180`](../../flows/chapters/ch23-simulated-mcmf-regret-greedy-heap-segtree.qmd) | `[CTSC2007] Data Backup` (`#178`), `CF 730 I — Olympiad` (`#179`), `CF 436 E — Cardboard` (`#180`) | **PASS** |
| **`Rev-13`** | Dynamic 1D / Subtree Mouse-Hole MCMF $\to$ Tree Heap-Merge (`[NOI2019] Sequence` / Lagged Heaps) | $O(N^2 \log N) \mapsto O(N \log^2 N)$ | [`Ch 23` Sections 3–4 & `#181`–`#184`](../../flows/chapters/ch23-simulated-mcmf-regret-greedy-heap-segtree.qmd) | `[ICPC WF 2018] Conquer The World` (`#181`), `[NOI2019] Sequence` (`#183`), `UOJ #455` (`#184`) | **PASS** |
| **`Rev-14`** | $L_p$ Isotonic Regression on DAG $\to$ Parallel Binary Search + Pointwise Threshold Closure (`整体二分 + 最小割`) | $O(N K \text{ flow}) \mapsto O(\log U \cdot \operatorname{MaxFlow}(N, M))$ | [`Ch 24` Sections 1–3 & `#185`–`#188`](../../flows/chapters/ch24-isotonic-regression-matroid-intersection-synthesis.qmd) | `[省选联考 2020 A卷] 魔法商店` (`#185`), `[BOI 2004] Sequence` (`#186`), `CF 1616 H` / DAG $L_p$ (`#187`) | **PASS** (`oracle_ch24`) |

---

## 2. Pedagogical Verification of Direction B Derivations

For each of the 14 reverse reductions, we checked that the textbook **does not** present the final greedy/DP/heap transition as an unmotivated trick:
- In **`Ch 16` (`CF 724 E` & `CF 1919 F2`)**, the chapter explicitly constructs the $s$-$t$ flow network first, writes down the algebraic capacity $C(S)$ of a partition $x_i \in \{0, 1\}$, and shows how the DP state or $2 \times 2$ tropical matrix entry directly tracks the running cut cost across the prefix $1 \dots i$.
- In **`Ch 23` (`CF 865 D`, `CF 730 I`, `CF 436 E`, `[NOI2019] Sequence`)**, every heap push of a transformed value (such as pushing $p_i$ a second time in `CF 865 D`, or pushing $b_i - a_i$ into the $A \to B$ transfer heap in `CF 730 I`) is proved to equal the exact reduced cost of a residual backward/relay path in the underlying MCMF network.

---

## 3. Audit Conclusion

**Status**: **100% PASS** (`14 / 14` Direction B Reverse-Reduction Archetypes verified).
