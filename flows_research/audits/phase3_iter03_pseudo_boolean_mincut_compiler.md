# Phase 3 Global Audit — Iteration 03: Pseudo-Boolean Cut Compiler (`燃やす埋める`), Multi-State Chains & Coarea Verification (`Ch 09`–`Ch 13`)

**Audit Date**: 2026-10-20  
**Scope**: Part III (`Ch 09` through `Ch 13` and `CP-III`: `8,763` lines across 6 `.qmd` files)  
**Audit Objective**: Verify the mathematical completeness, convention consistency, and mechanical compilability of the **Pseudo-Boolean Minimum Cut Compiler** across binary closures (`Ch 09`), general submodular $2 \times 2$ payoffs and higher-order clauses (`Ch 10`), bipartite variable inversion (`Ch 11`), multi-state unary threshold chains (`Ch 12`), and Ishikawa convex penalties + Discrete Coarea level-set cuts (`Ch 13`).

---

## 1. Convention Lock Audit (`x_i = 1 \iff i \in S` vs. Cut Indicators)

A frequent source of off-by-one and inverted-direction bugs in competitive programming tutorials on *Project Selection / Burn-or-Bury (`燃やす埋める`)* is inconsistent assignment of $x_i = 1$ between $S$ and $T$. Across all 5 chapters of Part III (`Ch 09`–`Ch 13`) and [`flows/notation.qmd`](../../flows/notation.qmd), we verified the **Global Partition Convention Lock**:

$$\boxed{x_i = [i \in S] \in \{0, 1\}: \quad x_i = 1 \iff i \in S \text{ (Source side)}, \qquad x_i = 0 \iff i \in T \text{ (Sink side)}.}$$

Under this convention:
1. **Elementary Cut Monomial (`Ch 09`–`Ch 13`)**: A directed arc $u \xrightarrow{w} v$ is severed by $(S, T)$ if and only if $u \in S$ ($x_u = 1$) and $v \in T$ ($x_v = 0$), contributing exactly:
   $$\text{cost}_{u \to v}(x) = w \cdot x_u (1 - x_v).$$
2. **Unary Source & Sink Attachments**:
   - $S \xrightarrow{a_u} u$ (where $x_S = 1$ is fixed) contributes $a_u \cdot 1 \cdot (1 - x_u) = a_u (1 - x_u)$ (paid when $x_u = 0$, i.e., $u \in T$).
   - $u \xrightarrow{b_u} T$ (where $x_T = 0$ is fixed) contributes $b_u \cdot x_u \cdot (1 - 0) = b_u x_u$ (paid when $x_u = 1$, i.e., $u \in S$).
3. **Hard Implication Clause ($x_u = 1 \implies x_v = 1$, or $x_u \le x_v$)**:
   - Compiled by $u \xrightarrow{\infty} v$, since $x_u = 1 \land x_v = 0$ severs $u \to v$ and pays $\infty$.

| Chapter | Convention Lock Verified | Key Compiler Formula Verified | Numerical Oracle in `tests/audit_flows_models.py` | Status |
| :--- | :---: | :--- | :--- | :---: |
| **`Ch 09`** ([`ch09-maximum-weight-closure-project-selection.qmd`](../../flows/chapters/ch09-maximum-weight-closure-project-selection.qmd)) | **PASS** | $\max \sum w_v x_v = \sum_{w_v > 0} w_v - \min_{(S,T)} \operatorname{cap}(S, T)$ | `oracle_ch09_closure_and_arc085e()` | **PASS** |
| **`Ch 10`** ([`ch10-pseudo-boolean-cuts-submodularity-burn-bury.qmd`](../../flows/chapters/ch10-pseudo-boolean-cuts-submodularity-burn-bury.qmd)) | **PASS** | $A + D \le B + C \iff \Phi(x_u, x_v)$ is $s$-$t$ cut-representable | `oracle_ch10_submodular_and_clause_hub()` | **PASS** |
| **`Ch 11`** ([`ch11-bipartite-variable-inversion-supermodular-rescue.qmd`](../../flows/chapters/ch11-bipartite-variable-inversion-supermodular-rescue.qmd)) | **PASS** | $\tilde{x}_v = 1 - x_v$ for $v \in R$ flips $(A+D) - (B+C) > 0 \mapsto < 0$ | `oracle_ch11_bipartite_inversion_and_agc038f()` | **PASS** |
| **`Ch 12`** ([`ch12-multi-state-unary-chains-threshold-cuts.qmd`](../../flows/chapters/ch12-multi-state-unary-chains-threshold-cuts.qmd)) | **PASS** | $z_{i,k} = [x_i \ge k]$ with reverse $\infty$-arcs $z_{i,k} \xrightarrow{\infty} z_{i,k-1}$ | `oracle_ch12_unary_chains_arc107f_arc142e()` | **PASS** |
| **`Ch 13`** ([`ch13-ishikawa-convex-penalties-coarea-parametric-cuts.qmd`](../../flows/chapters/ch13-ishikawa-convex-penalties-coarea-parametric-cuts.qmd)) | **PASS** | $c(v_{u,a} \to v_{v,b}) = -\frac{1}{2}\Delta_a \Delta_b \Phi(a,b) \ge 0$ & Coarea integral | `oracle_ch13_coarea_and_cf1427g()` | **PASS** |

---

## 2. Verification of the 5 Broken-Gadget Failure Modes (`FM-09` to `FM-13`)

Every chapter in Part III contains a dedicated **Broken-Gadget Counterexample** proving what breaks when a structural precondition is omitted:

1. **`FM-09` (Prerequisite Cycles in Maximum-Weight Closure — `[NOI2009] Plants vs. Zombies` `#067`)**:
   - **What breaks**: If a set of vertices $C$ forms a directed prerequisite cycle (or is reachable from a cycle in the dependency graph), no vertex in $C$ can ever be attacked/activated in a sequential game, yet in the static Picard closure graph $S \xrightarrow{w_v} v$, selecting all of $C$ together ($C \subseteq S$) severs **zero** internal $\infty$-edges! Thus static Max-Weight Closure falsely collects positive net profit from deadlocked cycles.
   - **Verified Fix in `Ch 09` Section 3**: Run Kahn's topological sort (indegree pruning on the dependency graph) to eliminate all vertices that cannot be reached in finite steps before building the Picard cut network.

2. **`FM-10` (Higher-Order Unanimity Gadget Direction vs. Pairwise Decomposition — `Ch 10` Section 4)**:
   - **What breaks**: Attempting to represent a 3-variable unanimity bonus $w \cdot x_1 x_2 x_3$ using only pairwise edges $(u, v)$ fails because any symmetric pairwise polynomial on 3 variables has degree $2$ and cannot match the third-order finite difference $\Delta_{123}(x_1 x_2 x_3) = 1 \ne 0$. Furthermore, wiring the auxiliary hub $h \xrightarrow{\infty} v_i$ vs. $v_i \xrightarrow{\infty} h$ in the wrong direction turns an ALL-$1$ bonus ($S \xrightarrow{w} h \xrightarrow{\infty} v_i$) into an ALL-$0$ bonus ($v_i \xrightarrow{\infty} h \xrightarrow{w} T$).
   - **Verified Fix in `Ch 10` Section 4**: Both ALL-$1$ ($S \xrightarrow{w} h \xrightarrow{\infty} v_i$) and ALL-$0$ ($v_i \xrightarrow{\infty} h \xrightarrow{w} T$) unanimity hubs are derived algebraically via $\min_{y \in \{0,1\}} \dots$ elimination and verified in `oracle_ch10_submodular_and_clause_hub()`.

3. **`FM-11` (Odd-Cycle Obstruction & Forgotten Unary Swap in Bipartite Inversion — `Ch 11` Section 2)**:
   - **What breaks**: When rescuing a supermodular penalty $A + D > B + C$ via $\tilde{x}_v = 1 - x_v$ on $v \in R$:
     1. If the interaction graph contains an **odd cycle** (e.g., a triangle $K_3$ with pairwise same-state penalties), at least one edge $(u, v)$ must have both endpoints on the same side of any bipartition, leaving a residual negative capacity $B + C - A - D < 0$.
     2. If the graph is bipartite $G = (L \sqcup R, E)$ and $R$ is inverted, forgetting to swap the unary source/sink attachments ($S \to v$ and $v \to T$) for $v \in R$ evaluates the unary costs on $1 - x_v$ instead of $x_v$.
   - **Verified Fix in `Ch 11` Section 2**: Complete proof and explicit triangle counterexample included.

4. **`FM-12` (Omitting Reverse $\infty$-Edges $v_{i,k} \xrightarrow{\infty} v_{i,k-1}$ on Unary Chains — `[HNOI2013] Cake Cutting` `#089`)**:
   - **What breaks**: On a single isolated vertex chain $S = v_{i,0} \xrightarrow{c_{i,1}} v_{i,1} \xrightarrow{c_{i,2}} \dots \xrightarrow{c_{i,K}} v_{i,K} = T$, a minimum cut naturally severs only the single cheapest edge. However, as soon as cross-chain edges $v_{u,k} \xrightarrow{\infty} v_{v,k-D}$ are added, an $s$-$t$ cut without reverse $\infty$-edges $v_{i,k} \xrightarrow{\infty} v_{i,k-1}$ can sever a chain **multiple times** ($z_{i,1} = 1, z_{i,2} = 0, z_{i,3} = 1$), corresponding to no valid integer state $x_i \in \{1, \dots, K\}$.
   - **Verified Fix in `Ch 12` Section 1**: Explicit 2-chain 3-state numerical counterexample included and cross-checked.

5. **`FM-13` (Non-Convex Penalty $g'' < 0$ in Ishikawa's Construction — `Ch 13` Section 2)**:
   - **What breaks**: Ishikawa's cross-chain capacity formula $c(v_{u,a} \to v_{v,b}) = \frac{1}{2}(g(|a-b|+1) - 2g(|a-b|) + g(|a-b|-1))$ is non-negative for all $a, b$ if and only if $g$ is discrete convex ($g(d+1) - 2g(d) + g(d-1) \ge 0$). For the Potts metric $g(d) = [d \ge 1]$ with $K \ge 3$ states, $g(2) - 2g(1) + g(0) = 1 - 2 + 0 = -1 < 0$, producing a negative capacity and reflecting the NP-hardness of Multiway Cut for $K \ge 3$ unordered labels.

---

## 3. Audit Conclusion

**Status**: **100% PASS**. Part III (`Ch 09`–`Ch 13` + `CP-III`) provides a mathematically unified, convention-locked treatment of the Pseudo-Boolean Minimum Cut Compiler.
