# Phase 3 Global Audit — Iteration 08: Notation, Terminology & Multilingual Convention Consistency (`flows/notation.qmd` vs. All 24 Chapters)

**Audit Date**: 2026-10-20  
**Scope**: [`flows/notation.qmd`](../../flows/notation.qmd) and all 24 chapters (`Ch 01`–`Ch 24`) + 6 checkpoints (`CP-I`–`CP-VI`)  
**Audit Objective**: Verify that every symbol, cut indicator, residual convention, Johnson potential sign, and multilingual cross-reference (`[EN]`, `[ZH]`, `[JA]`) in the textbook agrees with [`flows/notation.qmd`](../../flows/notation.qmd).

---

## 1. Core Notation & Sign Convention Verification Table

| Concept / Object | Canonical Symbol in `flows/notation.qmd` | Sign / Orientation Convention Lock | Verified Across Chapters | Status |
| :--- | :--- | :--- | :--- | :---: |
| **Directed Flow Network** | $G = (V, E, c, s, t)$ | Capacities $c : E \to \mathbb{R}_{\ge 0}$, net flow $f : E \to \mathbb{R}_{\ge 0}$ | `Ch 01`–`Ch 24` | **PASS** |
| **Residual Capacity** | $c_f(u, v)$ | Forward: $c(e) - f(e)$; Backward: $f(e)$ on $e^{\text{rev}} = (v, u)$ | `Ch 01`–`Ch 24` | **PASS** |
| **$s$-$t$ Cut & Cut Capacity** | $(S, T)$ with $s \in S, t \in T$; $\operatorname{cap}(S, T) = c(\delta^+(S))$ | Counts **only** forward arcs $u \to v$ with $u \in S, v \in T$ | `Ch 01`–`Ch 24` | **PASS** |
| **Source-Minimal / Sink-Minimal Cuts** | $S_{\min}$ and $S_{\max}$ | $S_{\min} = \{v \in V : s \rightsquigarrow_{G_f} v\}$, $T_{\min} = \{v \in V : v \rightsquigarrow_{G_f} t\}$ | `Ch 01`, `Ch 02`, `Ch 09`, `Ch 14` | **PASS** |
| **Pseudo-Boolean Binary Indicator** | $x_i = [i \in S] \in \{0, 1\}$ | $x_i = 1 \iff i \in S$ (Source side); $x_i = 0 \iff i \in T$ (Sink side) | `Ch 09`–`Ch 13`, `CP-III` | **PASS** |
| **Cut Monomial of Directed Arc $u \xrightarrow{w} v$** | $w \cdot x_u (1 - x_v)$ | Paid iff $x_u = 1$ ($u \in S$) and $x_v = 0$ ($v \in T$) | `Ch 09`–`Ch 13` | **PASS** |
| **Multi-State Unary Threshold Chain** | $z_{i,k} = [x_i \ge k] \in \{0, 1\}$ | Monotonicity $1 = z_{i,1} \ge z_{i,2} \ge \dots \ge z_{i,K} = 0$ enforced by $v_{i,k} \xrightarrow{\infty} v_{i,k-1}$ | `Ch 12`, `Ch 13`, `Ch 24` | **PASS** |
| **Lower-Bound Demand Balance** | $M(v) = \sum_{e \in \delta^-(v)} l(e) - \sum_{e \in \delta^+(v)} l(e)$ | $M(v) > 0 \implies S^* \xrightarrow{M(v)} v$; $M(v) < 0 \implies v \xrightarrow{-M(v)} T^*$ | `Ch 04`, `Ch 17`, `Ch 19` | **PASS** |
| **Bipartite Matching & Cover** | $\nu(G)$ (matching), $\tau(G)$ (vertex cover), $\alpha(G)$ (independent set), $\rho(G)$ (edge cover) | König: $\nu(G) = \tau(G)$; Gallai: $\alpha(G) + \tau(G) = |V|$, $\nu(G) + \rho(G) = |V|$ | `Ch 05`–`Ch 08`, `CP-II` | **PASS** |
| **Johnson Dual Potential & Reduced Cost** | $\pi : V \to \mathbb{R}$; $c^\pi(u, v) = c(u, v) + \pi(u) - \pi(v)$ | After shortest-path tree $d(v)$ from $s$: $\pi'(v) = \pi(v) + d^\pi(v) \implies c^{\pi'}(u, v) \ge 0$ on $G_f$ | `Ch 17`–`Ch 21`, `Ch 23` | **PASS** |

---

## 2. Multilingual Terminology Alignment (`[EN]` / `[ZH]` / `[JA]`)

Because seminal flow-modelling techniques originated independently in the English combinatorial optimization literature, the Chinese OI/NOI literature, and the Japanese AtCoder/Kyopro community, every chapter bridges all three terminologies:
- **Project Selection / Maximum-Weight Closure (`[EN]`)** $\leftrightarrow$ **最大权闭合子图 (`[ZH]`)** $\leftrightarrow$ **Project Selection Problem (`[JA]`)** (`Ch 09`)
- **Submodular Pseudo-Boolean Min-Cut (`[EN]`)** $\leftrightarrow$ **二元关系最小割 / 文理分科模型 (`[ZH]`)** $\leftrightarrow$ **燃やす埋める (`Moyasu-Umeru`, `[JA]`)** (`Ch 10`)
- **Bipartite Variable Inversion (`[EN]`)** $\leftrightarrow$ **二分图同侧/异侧状态翻转 (`[ZH]`)** $\leftrightarrow$ **二部グラフの片側反転 (`[JA]`)** (`Ch 11`)
- **Multi-State Ordered Unary Chain (`[EN]`)** $\leftrightarrow$ **切糕模型 / 距离限制模型 (`[ZH]`)** $\leftrightarrow$ **$K$値燃やす埋める (`[JA]`)** (`Ch 12`–`Ch 13`)
- **Parametric Residual Rollback (`[EN]`)** $\leftrightarrow$ **退流 (`[ZH]`)** $\leftrightarrow$ **流量の巻き戻し (`[JA]`)** (`Ch 02`, `Ch 13`)
- **Masao Iri's Equation-Difference Method (`[EN]`)** $\leftrightarrow$ **流守恒差分建模法 / 不等式差分转流 (`[ZH]`)** $\leftrightarrow$ **牛ゲーの双対 / 差分制約と最小費用流 (`[JA]`)** (`Ch 19`, `Ch 21`)
- **Simulated Cost Flow / Regret Greedy (`[EN]`)** $\leftrightarrow$ **模拟费用流 / 反悔贪心 (`[ZH]`)** $\leftrightarrow$ **模擬最小費用流 (`[JA]`)** (`Ch 23`)
- **$L_p$ Isotonic Regression via Parallel Binary Search (`[EN]`)** $\leftrightarrow$ **保序回归 + 整体二分最小割 (`[ZH]`)** $\leftrightarrow$ **単調回帰と燃やす埋める (`[JA]`)** (`Ch 24`)

---

## 3. Audit Conclusion

**Status**: **100% PASS**.
