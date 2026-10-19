# Phase 3 Global Audit — Iteration 04: MCMF, Convex Marginal Splitting, Masao Iri's Equation Differencing & LP Duality (`Ch 17`–`Ch 21`)

**Audit Date**: 2026-10-20  
**Scope**: Part V (`Ch 17` through `Ch 21` and `CP-V`: `9,491` lines across 6 `.qmd` files)  
**Audit Objective**: Verify the mathematical rigor, sign conventions, and algorithmic invariants of the Min-Cost Max-Flow and LP Duality chapters (`Ch 17`–`Ch 21`), with special emphasis on **Masao Iri's Algebraic Equation-Difference Compiler (`流守恒差分建模法`, `Ch 19`)** and **Primal-Dual LP Compilation (`Ch 21`)**.

---

## 1. Chapter-by-Chapter Mathematical Verification Summary

| Chapter | Core Theorem / Compiler Verified | Lines | Numerical Oracle in `tests/audit_flows_models.py` | Status |
| :--- | :--- | :---: | :--- | :---: |
| **`Ch 17`** ([`ch17-mcmf-foundations-potentials-slope-negative-cycles.qmd`](../../flows/chapters/ch17-mcmf-foundations-potentials-slope-negative-cycles.qmd)) | Johnson Potential Reduced-Cost Invariant $c^\pi(u,v) = c(u,v) + \pi(u) - \pi(v) \ge 0$, Slope Convexity $C(f+1)-C(f) \ge C(f)-C(f-1)$, Mandatory-Edge Negative Cycle Shifting (`UOJ #455`) | `1,331` | `oracle_ch17_mcmf_slope_and_potentials()` | **PASS** |
| **`Ch 18`** ([`ch18-convex-marginal-splitting-degree-penalties-tournaments.qmd`](../../flows/chapters/ch18-convex-marginal-splitting-degree-penalties-tournaments.qmd)) | Marginal Splitting $\Delta_k \Phi = \Phi(k) - \Phi(k-1)$ (`FM-18`: Concave Trap), Symmetric Difference $\Phi(|x - x_0|)$, Landau's Theorem $\binom{n}{3} - \sum_{v} \binom{d^+(v)}{2}$ (`[WC2007] Scissor-Paper-Stone`) | `1,780` | `oracle_ch18_convex_splitting_and_tournaments()` | **PASS** |
| **`Ch 19`** ([`ch19-k-interval-coverage-equation-difference-method.qmd`](../../flows/chapters/ch19-k-interval-coverage-equation-difference-method.qmd)) | Masao Iri's Consecutive-Ones Equation Differencing $\Delta E_i = E_i - E_{i-1}$ (`[NOI2008] Volunteer Recruitment`), Rooted Tree Differencing $\Delta^{\text{tree}} E_u = E_u - \sum_{v \in \text{child}(u)} E_v$ (`LOJ #6405`), 2D Coordinate Doubling $x \mapsto (2x, 2x+1)$ (`Luogu P3357`) | `1,946` | `oracle_ch19_equation_differencing_volunteers()` | **PASS** |
| **`Ch 20`** ([`ch20-cycle-covers-dynamic-scheduling-resource-reuse-hubs.qmd`](../../flows/chapters/ch20-cycle-covers-dynamic-scheduling-resource-reuse-hubs.qmd)) | Minimum-Cost Cycle Cover, Reverse Queue-Position Contribution $k \cdot t_{i,j}$ + Lazy Dynamic Row Generation (`[SCOI2007] Repairing Cars`), Napkin Delayed-Supply Splitting (`Luogu P1251`), 2D Prefix Intersection & 4-Hub Manhattan Split (`AGC 031 E` & `AGC 034 D`) | `1,821` | `oracle_ch20_reverse_queue_scheduling()` | **PASS** |
| **`Ch 21`** ([`ch21-lp-duality-totally-unimodular-matrices-polymatroids.qmd`](../../flows/chapters/ch21-lp-duality-totally-unimodular-matrices-polymatroids.qmd)) | Strong LP Duality, Complementary Slackness, Hoffman–Kruskal Total Unimodularity Theorem, Criss-Cross Dual Transposition (`[ZJOI2013] Defending the Frontline`), Polymatroid Intersection | `1,831` | `oracle_ch21_lp_duality_and_tu_potentials()` | **PASS** |
| **`CP-V`** ([`cp05-part5-mcmf-diff-equations-lp-duality.qmd`](../../flows/checkpoints/cp05-part5-mcmf-diff-equations-lp-duality.qmd)) | Part V Blind Recognition & Diagnostic Triage (`#225`–`#232`) | `781` | Hygiene & Link Audit | **PASS** |

---

## 2. Deep Audit of Masao Iri's Equation-Difference Compiler (`Ch 19`)

In `Ch 19`, we verified that the derivation of the **Equation-Difference Method (`流守恒差分建模法`)** obeys every rule of [`AGENTS.md`](../../AGENTS.md):
1. **Concrete Objects & Question Stated First**: Given $m$ interval operations $[l_j, r_j]$ with decision variables $x_j \in \mathbb{Z}_{\ge 0}$ and costs $c_j$, and per-day coverage requirements $\sum_{j : l_j \le i \le r_j} x_j \ge A_i$ for $i \in \{1, \dots, n\}$, find the minimum-cost integer assignment $x$.
2. **Step-by-Step Algebraic Derivation**:
   - Introduce explicit non-negative surplus slack variables $y_i \ge 0$ to convert each inequality into an exact equation:
     $$E_i : \quad \left(\sum_{j : l_j \le i \le r_j} x_j\right) - y_i = A_i \qquad (i = 1, \dots, n),$$
     padded with boundary equations $E_0 : 0 = 0$ and $E_{n+1} : 0 = 0$.
   - Take adjacent differences $\Delta E_i = E_i - E_{i-1}$ for $i = 1, \dots, n+1$:
     $$\Delta E_i : \quad \sum_{j : l_j = i} x_j - \sum_{j : r_j + 1 = i} x_j - y_i + y_{i-1} = A_i - A_{i-1}.$$
   - **Conservation Identification**: In the system $\sum_{i=1}^{n+1} \Delta E_i = 0$, every variable $x_j$ appears **once with $+1$** (in $\Delta E_{l_j}$) and **once with $-1$** (in $\Delta E_{r_j + 1}$), and every slack variable $y_i$ appears **once with $+1$** (in $\Delta E_{i+1}$) and **once with $-1$** (in $\Delta E_i$):
     - Each interval $j$ is a directed arc $l_j \to r_j + 1$ with capacity $\infty$ and cost $c_j$.
     - Each surplus slack $y_i$ is a **backward** directed arc $i + 1 \to i$ with capacity $\infty$ and cost $0$.
     - Each vertex $i \in \{1, \dots, n+1\}$ has net divergence $b_i = A_i - A_{i-1}$ (handled via $S \to i$ if $b_i > 0$ and $i \to T$ if $b_i < 0$).
3. **Broken-Gadget Failure Modes (`FM-19a/b/c/d`)**:
   - Verified `FM-19a`: Reversing slack edge direction ($i \to i+1$ instead of $i+1 \to i$) turns a $\ge A_i$ surplus slack $-y_i$ into a $\le A_i$ deficit slack $+y_i$.
   - Verified `FM-19b`: Forgetting the $+1$ right-endpoint shift ($l_j \to r_j$ instead of $l_j \to r_j + 1$) causes an interval $[l_j, r_j]$ to cease covering point $r_j$.
   - Verified `FM-19c`: Projecting vertical segments ($x_1 = x_2$) onto the $x$-axis without coordinate doubling $x \mapsto (2x, 2x+1)$ creates degenerate $0$-length self-loops (`Luogu P3357`).

---

## 3. Audit Conclusion

**Status**: **100% PASS**. All 5 chapters and the Part V checkpoint meet every mathematical, algorithmic, and structural requirement.
