# Phase 3 Global Audit — Iteration 02: Deep-Dive Verification of the Four User-Highlighted Flagship Problems

## 1. Executive Summary & Audit Scope

- **Audit Pass**: Phase 3, Iteration 02 (`phase3_iter02_four_user_flagships_deep_audit.md`)
- **Target Flagships**: The four non-graph-to-flow benchmark problems explicitly highlighted in the user prompt:
  1. **[AtCoder AGC 038 F — Two Permutations](https://atcoder.jp/contests/agc038/tasks/agc038_f)** (**Problem `#087`**, authored in `flows/chapters/ch11-bipartite-variable-inversion-supermodular-rescue.qmd` §4 & §6.7)
  2. **[AtCoder ARC 107 F — Sum of Abs](https://atcoder.jp/contests/arc107/tasks/arc107_f?lang=en)** (**Problem `#095`**, authored in `flows/chapters/ch12-multi-state-unary-chains-threshold-cuts.qmd` §2 & §6.7)
  3. **[AtCoder ARC 142 E — Pairing Wizards](https://atcoder.jp/contests/arc142/tasks/arc142_e?lang=en)** (**Problem `#096`**, authored in `flows/chapters/ch12-multi-state-unary-chains-threshold-cuts.qmd` §4 & §6.8)
  4. **[Codeforces 1427 G — One Billion Shades of Grey](https://codeforces.com/problemset/problem/1427/G)** (**Problem `#103`**, authored in `flows/chapters/ch13-ishikawa-convex-penalties-coarea-parametric-cuts.qmd` §4 & §6.7)
- **Automated Verification Status**: All 4 flagships have exact reference flow/cut compilations verified against exhaustive combinatorial brute-force enumeration in `tests/audit_flows_models.py` (`oracle_ch11_bipartite_inversion_and_agc038f`, `oracle_ch12_arc107f_and_arc142e`, `oracle_ch13_cf1427g_coarea_and_ishikawa` — **100% PASS**).

---

## 2. Flagship 1: AtCoder AGC 038 F — Two Permutations (`#087`, `Ch 11 §4`)

### 2.1 Non-Graph English Statement $\to$ Hidden Bipartite Cut Structure
- **Why No Graph Seems Present**: The statement gives two permutations $P, Q$ of $\{0, \dots, N-1\}$ ($N \le 10^5$) and asks us to construct two new permutations $A, B$ maximizing $|\{i : A_i \neq B_i\}|$ subject to $A_i \in \{i, P_i\}$ and $B_i \in \{i, Q_i\}$.
- **Step 1 (Cycle Rigidity Reduction)**: Because $A$ must be a bijection and $A_i \in \{i, P_i\}$, on each directed cycle $C \in \mathcal{C}_P$ of $P$, either $A_i = i$ for all $i \in C$ ($x_C = 0$) or $A_i = P_i$ for all $i \in C$ ($x_C = 1$). Similarly, each cycle $D \in \mathcal{C}_Q$ of $Q$ has a single binary choice $y_D \in \{0, 1\}$.
- **Step 2 (The 5 Index Cases & The Supermodular Obstacle)**: Minimizing agreements $\sum_{i=0}^{N-1} [A_i = B_i]$ over $x_C \in \{0,1\}$ and $y_D \in \{0,1\}$ breaks into 5 cases per index $i$:
  1. $P_i = i \land Q_i = i$: always $A_i = B_i = i$ (constant $+1$).
  2. $P_i = i \land Q_i \neq i$: $A_i = B_i \iff y_D = 0$ (unary penalty $1 - y_D$).
  3. $P_i \neq i \land Q_i = i$: $A_i = B_i \iff x_C = 0$ (unary penalty $1 - x_C$).
  4. $P_i \neq i \land Q_i \neq i \land P_i \neq Q_i$: $A_i = B_i \iff x_C = 0 \land y_D = 0$ (same-state penalty $(1-x_C)(1-y_D)$).
  5. $P_i = Q_i \neq i$: $A_i = B_i \iff x_C = y_D$ (both $(1-x_C)(1-y_D) + x_C y_D$).
  In Cases 4 and 5, penalizing $x_C = y_D$ has $2 \times 2$ diagonal sum $A + D > B + C$ (**supermodular**, negative cut capacity!).
- **Step 3 (Bipartite Variable Inversion Rescue `二部グラフの片側反転`)**: Every interaction is strictly between a $P$-cycle $C$ and a $Q$-cycle $D$—a **bipartite graph** $\mathcal{C}_P \sqcup \mathcal{C}_Q$! Substituting $z_D = 1 - y_D \in \{0, 1\}$ for all $Q$-cycles $D$ transforms $(1 - x_C)(1 - y_D) = z_D(1 - x_C)$ (a single directed edge $D \xrightarrow{1} C$) and $x_C y_D = x_C (1 - z_D)$ (a single directed edge $C \xrightarrow{1} D$).
- **Step 4 (Complexity & Oracle Check)**: Every cycle vertex has at least one unit-capacity incident edge per index $i$, yielding a unit network solved by Dinic in $O(N\sqrt{N})$ time for $N = 10^5$. Verified against $2^{|\mathcal{C}_P| + |\mathcal{C}_Q|}$ brute force in `oracle_ch11_bipartite_inversion_and_agc038f`.

---

## 3. Flagship 2: AtCoder ARC 107 F — Sum of Abs (`#095`, `Ch 12 §2`)

### 3.1 Non-Linear Component Sum $\to$ 3-State Ordered Chain Cut
- **Why Flow Is Surprising**: Deleting vertex $v$ costs $A_v$, and each surviving connected component $C$ contributes $\left|\sum_{v \in C} B_v\right|$ ($N, M \le 300$). Component-level absolute values appear non-local and non-linear.
- **Step 1 (Sign Decoupling Identity $|X| = \max(+X, -X)$)**: Instead of computing connected components after deletion, assign each surviving vertex $v$ a sign $\sigma_v \in \{-1, +1\}$ and each deleted vertex $\sigma_v = 0$. Any valid assignment where **no surviving edge $(u, v) \in E$ connects $\sigma_u = -1$ and $\sigma_v = +1$** guarantees that every surviving connected component is monochromatic in sign, and optimizing over $\sigma \in \{-1, 0, +1\}^V$ automatically selects the true component signs!
- **Step 2 (3-State Unary Chain Ordering $-1 \prec 0 \prec +1$)**: Order the three states as $\{-1, 0, +1\}$. The only forbidden pairwise configuration across an edge $\{u, v\} \in E$ is $\{\sigma_u, \sigma_v\} = \{-1, +1\}$—a **2-step jump** across the middle deleted state $0$!
- **Step 3 (Chain Compilation)**: Subtracting losses from the ideal upper bound $M_0 = \sum_{v \in V} |B_v|$, each vertex $v$ becomes a 2-node, 3-edge chain:
  $$S \xrightarrow{|B_v| + B_v} v_{\text{in}} \xrightarrow{|B_v| + A_v} v_{\text{out}} \xrightarrow{|B_v| - B_v} T, \qquad v_{\text{out}} \xrightarrow{\infty} v_{\text{in}},$$
  where cutting $S \to v_{\text{in}}$ sets $\sigma_v = -1$, cutting $v_{\text{in}} \to v_{\text{out}}$ sets $\sigma_v = 0$ (net profit $-A_v$), cutting $v_{\text{out}} \to T$ sets $\sigma_v = +1$, the reverse $\infty$-edge $v_{\text{out}} \to v_{\text{in}}$ prevents cutting both $S \to v_{\text{in}}$ and $v_{\text{out}} \to T$ (`FM-12`), and each undirected edge $\{u, v\} \in E$ adds cross-chain $\infty$-edges $u_{\text{out}} \xrightarrow{\infty} v_{\text{in}}$ and $v_{\text{out}} \xrightarrow{\infty} u_{\text{in}}$.
- **Step 4 (Oracle Check)**: Verified across all $3^N$ state assignments in `oracle_ch12_arc107f_and_arc142e`.

---

## 4. Flagship 3: AtCoder ARC 142 E — Pairing Wizards (`#096`, `Ch 12 §4`)

### 4.1 Non-Graph Pairwise $\min/\max$ Thresholds $\to$ Bipartite Unary OR Cut
- **Why Flow Is Surprising**: We can increment $a_i \gets a_i + 1$ at cost $1$ ($N \le 100, a_i, b_i \le 100$) so every pair $(u, v) \in E$ satisfies $\min(x_u, x_v) \ge \min(b_u, b_v)$ and $\max(x_u, x_v) \ge \max(b_u, b_v)$. Disjunctive $\max(x_u, x_v) \ge M$ constraints ("either $x_u \ge M$ OR $x_v \ge M$") normally look like NP-hard Vertex Cover / non-submodular OR clauses.
- **Step 1 (Mandatory Pre-Promotion Lemma)**: The conjunctive constraint $\min(x_u, x_v) \ge \min(b_u, b_v)$ unconditionally forces $x_u \ge \min(b_u, b_v)$ and $x_v \ge \min(b_u, b_v)$. Pre-promoting $a_u \gets \max(a_u, \min(b_u, b_v))$ across all pairs is 100% mandatory.
- **Step 2 (The Low-Role vs. High-Role Bipartite Dichotomy Theorem)**: After pre-promotion, consider any remaining unsatisfied pair $(u, v)$ where $b_u > b_v$ (so $\max(b_u, b_v) = b_u$). Because $a_u, a_v \ge \min(b_u, b_v) = b_v$ and $\max(a_u, a_v) < b_u$, we **must** have:
  $$a_u < b_u \quad (\text{Low-Role } u \in V_{\text{low}}) \qquad \text{and} \qquad a_v \ge b_v \quad (\text{High-Role } v \in V_{\text{high}}) !$$
  Crucially, $V_{\text{low}} = \{w : a_w < b_w\}$ and $V_{\text{high}} = \{w : a_w \ge b_w\}$ are **disjoint**! Furthermore, a Low-Role wizard $u \in V_{\\text{low}}$ only ever needs to jump all the way to $b_u$ (a single binary decision $y_u \in \{0, 1\}$ of cost $b_u - a_u$), whereas a High-Role wizard $v \in V_{\text{high}}$ is promoted along a unary chain $z_{v,k} = [x_v \ge k]$ for $k \in (a_v, 100]$.
- **Step 3 (Bipartite Disjunctive OR Cut Compilation)**: For each unsatisfied pair $(u, v)$ with $u \in V_{\text{low}}, v \in V_{\text{high}}$, we need $y_u = 1 \lor z_{v, b_u} = 1$. Placing $y_u = 0$ on the $S$-side ($S \xrightarrow{b_u - a_u} u_{\text{low}}$) and $z_{v, k} = 0$ on the $T$-side ($v_{k} \xrightarrow{1} T$ with chain $v_{k-1} \xrightarrow{\infty} v_k$), the single arc $u_{\text{low}} \xrightarrow{\infty} v_{b_u}$ forbids $y_u = 0 \land z_{v, b_u} = 0$!
- **Step 4 (Oracle Check)**: Verified against exhaustive integer brute force $x \in \{1..B_{\max}\}^N$ in `oracle_ch12_arc107f_and_arc142e`.

---

## 5. Flagship 4: Codeforces 1427 G — One Billion Shades of Grey (`#103`, `Ch 13 §4`)

### 5.1 $10^9$-State Grid Smoothing $\to$ Discrete Coarea Formula + Parametric Residual Rollback
- **Why Flow Is Surprising**: On an $N \times N$ grid ($N \le 200$) with fixed boundary shades $b_{r,c} \in [1, 10^9]$ and free interior tiles, we want to minimize $\sum_{\text{adj}} |h_u - h_v|$. With $K = 10^9$ states, Ishikawa's multi-state chain (`Ch 12`–`13`) would require $4 \times 10^{13}$ vertices!
- **Step 1 (Discrete Coarea / Layer-Cake Decomposition)**: Let $v_1 < v_2 < \dots < v_m$ ($m \le 4N \le 800$) be the sorted distinct boundary shades. By the discrete Coarea identity:
  $$\sum_{(u,v) \in E} |h_u - h_v| = \sum_{k=1}^{m-1} (v_{k+1} - v_k) \sum_{(u,v) \in E} \big|[h_u > v_k] - [h_v > v_k]\big|.$$
- **Step 2 (Submodular Cut Nesting $S_1 \supseteq S_2 \supseteq \dots \supseteq S_{m-1}$)**: Because the boundary conditions $[b_u > v_k]$ are monotone decreasing in $k$, the minimal $s$-$t$ cuts $S_k$ for the $m - 1$ independent binary threshold problems automatically nest ($S_1 \supseteq S_2 \supseteq \dots \supseteq S_{m-1}$), defining a valid integer height function $h_u \in \{v_1, \dots, v_m\}$ without any cross-layer $\infty$-edges!
- **Step 3 (Parametric Residual Rollback `退流` in $O(N^3)$ Total Time)**: When sweeping from threshold $v_{k-1}$ to $v_k$, only the boundary tiles $b$ with shade $v_k$ switch from $S \to b$ (capacity $\infty$) to $b \to T$ (capacity $\infty$). Since each boundary tile has degree $\le 4$ inside the unit-capacity grid, it carries at most $4$ units of flow! Draining those $\le 4$ units of flow along $b \rightsquigarrow S$ in $G_f$, zeroing $S \to b$, attaching $b \xrightarrow{\infty} T$, and re-augmenting $S \rightsquigarrow T$ performs at most $O(N)$ total augmentations across all $4N$ phases ($O(N^3)$ total time!).
- **Step 4 (Oracle Check)**: Verified against exhaustive continuous/integer height minimization in `oracle_ch13_cf1427g_coarea_and_ishikawa`.
