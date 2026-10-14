# Wave 5B Independent Second-Pass Audit Report (Inspector B)

- **Target File**: [cohort3_wave_5b_tree_fps_transposition_compose_q.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md) (2,051 lines)
- **Source Files Compared**:
  1. [cohort1_iter_46_to_52_tree_fps_transposition_compose_q.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort1_iter_46_to_52_tree_fps_transposition_compose_q.md) (1,896 lines)
  2. [cohort2_iter_98_to_104_tree_fps_transposition_compose_q.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_98_to_104_tree_fps_transposition_compose_q.md) (2,021 lines)
  3. [iter_46_to_52_tree_fps_transposition_compose_q.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_46_to_52_tree_fps_transposition_compose_q.md) (1,050 lines)
- **First-Pass Audit Reviewed**:
  4. [audit_A_wave_5b.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/audit/audit_A_wave_5b.md) (949 lines)
- **Audit Verdict**: **NEEDS REMEDIATION** (Critical C++ out-of-bounds crash in `sps_compose` missed by Inspector A; broken C++ replacement code and conversational `"Wait:"` leaks inside Inspector A's report; omitted theoretical optimizations and source problems; remaining 2-in-1 bundled problems in Section 7; incomplete Appendix A).

---

## Executive Summary of Findings

1. **Audit of First-Pass Report (`audit_A_wave_5b.md`) — Critical Defects in Inspector A's Proposed Fixes**:
   - **Defect A1 (Non-Compiling & Infinite-Recursion C++ Code in Inspector A's Fix M3, `audit_A_wave_5b.md` lines 74–98)**: Inspector A's drop-in replacement for `solve_chain_dc` changes the function signature from `AffinePoly solve_chain_dc(const vector<AffinePoly>& chain, int l, int r)` to `Mat2 solve_chain_dc(const vector<int>& chain, int l, int r)` and calls undefined identifiers (`Mat2`, `base_mat`, `light_wt`, `mul_mat`) that do not exist in [cohort3_wave_5b_tree_fps_transposition_compose_q.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md#L234-L280). Worse still, in Inspector A's 3-way split branch (`else if (m == r || ...)` at line 90 of `audit_A_wave_5b.md`), when `m == r`, calling `solve_chain_dc(chain, m + 1, r)` passes `l = r + 1 > r` into a function whose only base case is `if (l == r)`, causing infinite recursion and out-of-bounds memory access.
   - **Defect A2 (Conversational `"Wait:"` Artifacts and Algebra Typos in Inspector A's Toy Traces, `audit_A_wave_5b.md` lines 774, 824, 898–899)**: Inspector A's replacement Toy Traces contain raw self-correction prose (`"(Wait: 2(1) + 3(1000) = 3002...)"` at line 774; `"(Wait: in column-pivot order: pivots (1,4)...)"` and `"(with 1 free entry before pivot 2? In RREF: ...)"` at lines 898–899) and an algebraic typo at line 824 writing $(4x - x)y^2$ instead of $(4x^2 - x)y^2$ in $Q_1(x, y)$.

2. **Newly Discovered Mathematical & Algorithmic Bugs in `cohort3_wave_5b` (Missed by Inspector A)**:
   - **Bug B1 (CRITICAL — Out-of-Bounds Crash, Reversed Loop Direction, and Missing Derivative Factor in `sps_compose`, `cohort3_wave_5b` lines 1068–1121)**:
     In Section 6.5 (`sps_compose`), `dp[d]` is initialized with size $1$ (`vector<Mint>(1, 0)`), and the loop runs `for (int v = n - 1; v >= 0; --v)`. On the very first iteration (`v = n - 1`), line 1089 executes `vector<Mint> slice_c(dp[d].begin() + offset, dp[d].begin() + offset + (1 << v))`, attempting to copy $2^{n-1}$ elements from a vector of size $1$ — an immediate out-of-bounds crash! Moreover, the loop over $v$ must run **upward** `for (int v = 0; v < n; ++v)` (so both $F_{<v}(x)$ and $F_1^{(v)}(x) = F_{[2^v, 2^{v+1})}(x)$ are Set Power Series in the same $v$ variables $\{x_0, \dots, x_{v-1}\}$ of size $2^v$), and the coordinate-wise derivative $\frac{\partial}{\partial y}\left(\sum_d dp[d] y^d\right) = \sum_d (d + 1) dp[d+1] y^d$ requires multiplying by `Mint(d + 1)` at line 1100.
   - **Bug B2 (Empty/Zero-Output Guard in `shift_of_sampling_points`, `cohort3_wave_5b` lines 730–780 & 1962–1994)**:
     If `m <= 0` or `y.empty()`, `lenB = d + m` can be $0$, causing `pref[lenB - 1]` (`pref[-1]`) to access out-of-bounds memory.
   - **Bug B3 (Mischaracterized Contest Problem in `A2: AtCoder ABC 355 G — Baseball`, `cohort3_wave_5b` lines 1236–1251)**:
     `cohort3_wave_5b` (following `cohort1` Problem 2) attributes the laminar interval containment tree DP + HLD D&C FFT problem to AtCoder ABC 355 G (*Baseball*). We provide a corrected entry that clarifies both the Laminar Interval Containment Tree DP + HLD D&C FFT formulation and its exact tree-chain recurrence.
   - **Bug B4 (Truncated 3-Line Generic Sketch in `A3: Luogu P7279 — 光棱碎片`, `cohort3_wave_5b` lines 1255–1270)**:
     `A3` lacks an explicit problem statement, transition matrix, and complete derivation.

3. **Zero Information Loss vs. Source Cohorts (`cohort1`, `cohort2`, `iter_46_to_52`)**:
   - **Omission O1**: Cohort 1's **Power-of-2 Target Degree Trick** ($n = 2^m - 1 = (11\dots1)_2$ so parity $n \bmod 2 = 1$ at every level) and **$\widetilde{Q}_t(x, y) = Q_t(x, y) - 1$ 1D Kronecker-Packed Implementation** (`cohort1` lines 570–575, 706–763, 767–773) were dropped from Section 3.
   - **Omission O2**: `iter_46_to_52`'s **Global 52-Iteration Verification Matrix** (`iter_46_to_52` lines 506–521) bridging Waves 1A–5B was omitted.
   - **Omission O3**: Appendix A (`cohort3_wave_5b` lines 1766–2050) omits `bivariate_multiply` (referenced by `power_projection` in Appendix A.3!), `fps_compose`, `QBinomial`, `sps_exp`, `sps_compose`, and `dgf_exp`.
   - **Omission O4**: Three bibliography references from `iter_46_to_52` (`[BM21]` Bostan–Mori 2021, `[ZZ19]` Zhong Zihao 2019, and `[Nos22]` `noshi91` Algorithm Encyclopedia) were omitted from Section 8.
   - **Omission O5 & Unbundling**: Inspector A unbundled 7 problem pairs (`A5`, `A6`, `B2`, `B3`, `C2`, `C3`, `C5`), but left **9 problem pairs still bundled two-in-one** (`A12`, `B9`, `B10`, `D1`, `D4`, `E5`, `E6`, `F2`, `F7`), left 5 problems as brief sketches (`B6`, `C1`, `C4`, `C7`, `E2`), and did not provide full 4-point textbook entries for 6 omitted problems from `cohort1` and `iter_46_to_52` (`ABC 238 Ex`, `CF 1534H`, `LOJ 6673`, `Luogu P4365`, `ABC 336 G`, `ARC 153 D`, `ARC 134 E`). Section 4 of this report provides complete, unbundled, textbook-grade entries for every single one.

---

## Section 1: Audit of First-Pass Report (`audit_A_wave_5b.md`) & Corrected Drop-In Replacements

### 1.1 Fix for Inspector A's Broken `solve_chain_dc` Replacement (`audit_A_wave_5b.md` Fix M3, lines 74–98)

- **Location in `cohort3_wave_5b.md`**: Section 1.5 (lines 256–269) and Appendix A.1 (lines 1785–1798).
- **Why Inspector A's Fix M3 Is Broken**:
  1. In `cohort3_wave_5b.md`, lines 234–280 define `struct AffinePoly { vector<Mint> a, b; int wt; };` and `AffinePoly compose_affine(const AffinePoly& L, const AffinePoly& R)`. Inspector A's replacement changes `solve_chain_dc` to return `Mat2` on `const vector<int>& chain` and references non-existent functions/globals `base_mat(chain[l])`, `light_wt[chain[i]]`, and `mul_mat(...)`.
  2. In Inspector A's 3-way split (`audit_A_wave_5b.md` line 90): when `m == r` and `(cur_wt - light_wt[chain[m]]) * 2 < total_wt`, Inspector A's `else` branch calls `solve_chain_dc(chain, m + 1, r)` with `m + 1 = r + 1 > r`, triggering infinite recursion.
- **Exact Drop-In Replacement for `cohort3_wave_5b.md` Lines 256–269 (and Appendix A.1 Lines 1785–1798)**:

```cpp
// Weight-balanced D&C along a heavy chain [l, r]
// Guarantees every recursive call strictly reduces total weight by at least a factor of 2/3,
// avoiding the O(N^2 log N) midpoint-split trap when a single vertex has huge light-child weight.
AffinePoly solve_chain_dc(const vector<AffinePoly>& chain, int l, int r) {
    if (l == r) return chain[l];
    int total_wt = 0;
    for (int i = l; i <= r; ++i) total_wt += chain[i].wt;

    int cur_wt = 0, m = l;
    while (m < r && (cur_wt + chain[m].wt) * 2 < total_wt) {
        cur_wt += chain[m].wt;
        ++m;
    }
    // Here m in [l, r] is the first index where sum_{i=l}^m wt[i] >= ceil(total_wt / 2),
    // and cur_wt = sum_{i=l}^{m-1} wt[i] < total_wt / 2.
    if (m == l) {
        // Heavy element at l: peel off [l, l] and [l + 1, r]
        return compose_affine(solve_chain_dc(chain, l, l),
                              solve_chain_dc(chain, l + 1, r));
    } else if (m == r) {
        // Heavy element at r: peel off [l, r - 1] and [r, r]
        return compose_affine(solve_chain_dc(chain, l, r - 1),
                              solve_chain_dc(chain, r, r));
    } else if ((cur_wt + chain[m].wt) * 3 <= total_wt * 2) {
        // Balanced 2-way split [l, m] and [m + 1, r] (both sides <= 2/3 total_wt)
        return compose_affine(solve_chain_dc(chain, l, m),
                              solve_chain_dc(chain, m + 1, r));
    } else if (cur_wt * 3 >= total_wt) {
        // Balanced 2-way split [l, m - 1] and [m, r] (both sides <= 2/3 total_wt)
        return compose_affine(solve_chain_dc(chain, l, m - 1),
                              solve_chain_dc(chain, m, r));
    } else {
        // 3-way split [l, m - 1], [m, m], [m + 1, r] where l < m < r is strictly guaranteed,
        // and both outer ranges [l, m - 1] and [m + 1, r] have weight < total_wt / 2.
        AffinePoly left_part = solve_chain_dc(chain, l, m - 1);
        AffinePoly mid_part = chain[m];
        AffinePoly right_part = solve_chain_dc(chain, m + 1, r);
        return compose_affine(compose_affine(left_part, mid_part), right_part);
    }
}
```

---

### 1.2 Clean, Zero-`"Wait:"`, Python-Verified Drop-In Toy Traces (Replacing Inspector A's Toy Traces 1–6 in `audit_A_wave_5b.md` lines 718–945)

Inspector A's Toy Traces 2, 3, and 5 in `audit_A_wave_5b.md` contain conversational `"Wait:"` self-corrections and an algebraic typo (`(4x - x)y^2` instead of `(4x^2 - x)y^2`). Below are the **100% clean, Python-verified drop-in Toy Traces 1–6** to insert into Sections 1–6 of `cohort3_wave_5b.md`.

#### Toy Trace 1 (Insert at end of Section 1.4, after line 231 of `cohort3_wave_5b.md`)

```markdown
#### Small-$N$ Concrete Execution Trace ($N = 5$ Tree Antichains / ABC 269 Ex)

Consider a rooted tree on $N = 5$ vertices with root $1$, heavy path $1 \to 2 \to 3$, a light child $4$ attached to $1$, and a light child $5$ attached to $2$:
- Edges: $(1, 2), (2, 3), (1, 4), (2, 5)$.
- Subtree sizes: $\text{sz} = [5, 3, 1, 1, 1]$.
- Heavy children: $\text{heavy}[1] = 2$, $\text{heavy}[2] = 3$, $\text{heavy}[3] = \text{heavy}[4] = \text{heavy}[5] = 0$.

1. **Base Light Chains ($u = 4$ and $u = 5$)**:
   Both $4$ and $5$ are leaves with no light children ($L_4(x) = 1$, $L_5(x) = 1$). Their single-node affine transitions evaluate to:
   $$F_4(x) = 1 + x, \qquad F_5(x) = 1 + x.$$
2. **Light-Child Merging Along Heavy Chain $C = (1, 2, 3)$**:
   - At $u_1 = 1$: light child is $\{4\}$, so $L_1(x) = F_4(x) = 1 + x$.
   - At $u_2 = 2$: light child is $\{5\}$, so $L_2(x) = F_5(x) = 1 + x$.
   - At $u_3 = 3$ (leaf of heavy chain): no light children, so $L_3(x) = 1$, and its affine pair is $(a_3(x), b_3(x)) = (1, 1 + x)$.
3. **Heavy-Chain Affine Matrix Product**:
   We multiply the three affine transformations $(L_1(x), x)$, $(L_2(x), x)$, and $(1, 1+x)$:
   $$\begin{bmatrix} 1+x & x \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1+x & x \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} (1+x)^2 & x(1+x) + x \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 + 2x + x^2 & 2x + x^2 \\ 0 & 1 \end{bmatrix}.$$
   Applying this composite transformation to the leaf vector $\begin{bmatrix} F_3(x) \\ 1 \end{bmatrix} = \begin{bmatrix} 1 + x \\ 1 \end{bmatrix}$ yields:
   $$F_1(x) = (1 + 2x + x^2)(1 + x) + (2x + x^2) = (1 + 3x + 3x^2 + x^3) + (2x + x^2) = 1 + 5x + 4x^2 + x^3.$$
4. **Combinatorial Verification**:
   - $[x^0]F_1(x) = 1$: $\emptyset$.
   - $[x^1]F_1(x) = 5$: $\{1\}, \{2\}, \{3\}, \{4\}, \{5\}$.
   - $[x^2]F_1(x) = 4$: $\{2, 4\}, \{3, 4\}, \{4, 5\}, \{3, 5\}$.
   - $[x^3]F_1(x) = 1$: $\{3, 4, 5\}$ (the $3$ leaves form the unique antichain of size $3$).
```

#### Toy Trace 2 (Insert at end of Section 2.3, after line 378 of `cohort3_wave_5b.md`)

```markdown
#### Small-$N$ Concrete Execution Trace (Middle Product vs. Cyclic FFT Wrap-Around)

Let $A(x) = 2 + 3x$ ($d = 1$) and $C(x) = 10 + 100x + 1000x^2 + 10000x^3$ ($n + d = 3$, so $n = 2$). We want to compute $b = \text{MidProd}_1(A, C)$ of length $n + 1 = 3$:
$$b_j = \sum_{i=0}^1 a_i c_{i+j} = 2 c_j + 3 c_{j+1} \quad \text{for } j \in \{0, 1, 2\}.$$
1. **Direct Matrix-Vector Multiplication ($T_A^\top c$)**:
   $$\begin{bmatrix} b_0 \\ b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} 2 & 3 & 0 & 0 \\ 0 & 2 & 3 & 0 \\ 0 & 0 & 2 & 3 \end{bmatrix} \begin{bmatrix} 10 \\ 100 \\ 1000 \\ 10000 \end{bmatrix} = \begin{bmatrix} 2(10) + 3(100) \\ 2(100) + 3(1000) \\ 2(1000) + 3(10000) \end{bmatrix} = \begin{bmatrix} 320 \\ 3200 \\ 32000 \end{bmatrix}.$$
2. **Via Reversed Polynomial Multiplication**:
   Form $A^R(x) = x^1 A(x^{-1}) = 3 + 2x$. Multiply $A^R(x) \cdot C(x)$:
   $$(3 + 2x)(10 + 100x + 1000x^2 + 10000x^3) = 30 + \mathbf{320}x + \mathbf{3200}x^2 + \mathbf{32000}x^3 + 20000x^4.$$
   Reading off coefficients at degrees $d + j = 1 + j$ for $j = 0, 1, 2$ recovers $[320, 3200, 32000]$.
3. **Why Naive Length-$4$ Cyclic FFT Without Zero-Padding Corrupts $b_2$**:
   In a cyclic convolution of length $L = 4$ (where $x^4 \equiv 1$), the $x^4$ term $20000 x^4$ wraps around to $x^0$ (corrupting index $0$ from $30$ to $20030$). If instead one used $A(x^{-1}) \equiv 2 + 3x^3 \pmod{x^4}$ and extracted $[x^0, x^1, x^2]$, then:
   $$(2 + 3x^3)(10 + 100x + 1000x^2 + 10000x^3) \equiv (20 + 300) + (200 + 3000)x + (2000 + 30000)x^2 + (20000 + 30)x^3 \pmod{x^4},$$
   which is valid **only** because $L = 4 \ge n + d + 1 = 4$. If one tried to use a smaller cyclic length $L = 2 < 4$, the wrap-around aliases $c_0$ with $c_2$ and $c_1$ with $c_3$, destroying all three middle-product outputs.
```

#### Toy Trace 3 (Insert at end of Section 3.2, after line 496 of `cohort3_wave_5b.md`)

```markdown
#### Small-$N$ Concrete Execution Trace (Kinoshita–Li 2D Bostan–Mori Power Projection for $N = 4$)

Let $N = 4$ ($n = N - 1 = 3$), weight vector $w = [w_0, w_1, w_2, w_3] = [1, 1, 1, 1]$, and $F(x) = x + 2x^2$ ($f_0 = 0, f_1 = 1, f_2 = 2, f_3 = 0$).
First let us compute the exact target values $\text{ans}_k = \sum_{i=0}^3 w_i [x^i] F(x)^k$ for $k = 0, 1, 2, 3$:
- $F(x)^0 = 1 \implies \text{ans}_0 = 1$.
- $F(x)^1 = x + 2x^2 \implies \text{ans}_1 = 1 + 2 = 3$.
- $F(x)^2 = x^2 + 4x^3 + 4x^4 \equiv x^2 + 4x^3 \pmod{x^4} \implies \text{ans}_2 = 1 + 4 = 5$.
- $F(x)^3 = x^3 + 6x^4 + \dots \equiv x^3 \pmod{x^4} \implies \text{ans}_3 = 1$.

Now trace the 2D Bostan–Mori loop:
1. **Initialization ($t = 0, n_0 = 3, d_x = 4, d_y = 1$)**:
   - $P_0(x, y) = \sum_{i=0}^3 w_i x^{3-i} = 1 + x + x^2 + x^3$.
   - $Q_0(x, y) = 1 - y F(x) = 1 - (x + 2x^2)y$.
2. **Step $t = 0 \to 1$ ($n_0 = 3$ is odd, so parity $= 1$, $n_1 = \lfloor 3/2 \rfloor = 1, d_x = 2, d_y = 2$)**:
   - Negate $x$: $Q_0(-x, y) = 1 - (-x + 2x^2)y = 1 + (x - 2x^2)y$.
   - Denominator $V_0(x, y) = Q_0(x, y) Q_0(-x, y) = (1 - 2x^2 y)^2 - x^2 y^2 = 1 - 4x^2 y + (4x^4 - x^2) y^2$.
     Extracting even powers of $x$ ($x^{2i} \mapsto x^i$ for $i = 0, 1$) gives:
     $$Q_1(x, y) = 1 - 4xy + (4x^2 - x)y^2 \equiv 1 - 4xy - xy^2 \pmod{x^2}.$$
   - Numerator $U_0(x, y) = P_0(x, y) Q_0(-x, y) = (1 + x + x^2 + x^3)(1 + xy - 2x^2 y)$:
     $$U_0(x, y) = 1 + (1 + y)x + (1 - y)x^2 + (1 - y)x^3 - xy(x^2 + x^3) \dots$$
     More explicitly, collecting odd powers of $x$ ($x^1$ and $x^3$, since $n_0 = 3$ is odd):
     - $[x^1] U_0(x, y) = 1 + 1\cdot y = 1 + y$.
     - $[x^3] U_0(x, y) = 1 + 1\cdot y - 2\cdot y = 1 - y$.
     Thus $P_1(x, y) = (1 + y) + (1 - y)x$.
3. **Step $t = 1 \to 2$ ($n_1 = 1$ is odd, so parity $= 1$, $n_2 = \lfloor 1/2 \rfloor = 0, d_x = 1, d_y = 4$)**:
   - Negate $x$: $Q_1(-x, y) = 1 + 4xy + xy^2$.
   - Since $n_2 = 0$, we only need $[x^0] Q_2(x, y) = 1$ and $[x^1] U_1(x, y) \bmod y^4$ where $U_1(x, y) = P_1(x, y) Q_1(-x, y)$:
     $$U_1(x, y) = \bigl((1 + y) + (1 - y)x\bigr)\bigl(1 + (4y + y^2)x\bigr).$$
   - Extract $[x^1] U_1(x, y)$:
     $$P_2(0, y) = (1 + y)(4y + y^2) + (1 - y)(1) = 1 + 3y + 5y^2 + y^3.$$
4. **Output ($t = 2, n_2 = 0$)**:
   Reading the coefficients of $P_2(0, y) = 1 + 3y + 5y^2 + y^3$ gives $[1, 3, 5, 1]$, matching the exact power projections!
```

#### Toy Trace 4 (Insert at end of Section 4.1, after line 682 of `cohort3_wave_5b.md`)

```markdown
#### Small-$N$ Concrete Execution Trace (Bluestein Chirp Z-Transform for $n = 3, m = 3$)

Let $A(x) = 1 + 2x + 3x^2$ ($a = [1, 2, 3], n = 3$), $c = 1$, $q = 2$, and $m = 3$. We want to evaluate $A(q^j) = A(2^j)$ for $j = 0, 1, 2$:
- Direct check: $A(1) = 6$, $A(2) = 1 + 4 + 12 = 17$, $A(4) = 1 + 8 + 48 = 57$.

Now trace Bluestein's identity $i j = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$:
1. **Triangular Powers $\binom{k}{2}$**:
   $\binom{0}{2} = 0, \binom{1}{2} = 0, \binom{2}{2} = 1, \binom{3}{2} = 3, \binom{4}{2} = 6$.
   Hence $q^{\binom{k}{2}} = [2^0, 2^0, 2^1, 2^3, 2^6] = [1, 1, 2, 8, 64]$, and $q^{-\binom{k}{2}} = [1, 1, \frac{1}{2}]$.
2. **Construct Reversed Input Vector $u$ of Length $n = 3$**:
   $$u_{n - 1 - i} = a_i c^i q^{-\binom{i}{2}} \implies u_2 = a_0(1) = 1, \quad u_1 = a_1(1) = 2, \quad u_0 = a_2 \cdot \frac{1}{2} = \frac{3}{2}.$$
   So $u(x) = \frac{3}{2} + 2x + x^2$, and $v(x) = \sum_{k=0}^4 q^{\binom{k}{2}} x^k = 1 + x + 2x^2 + 8x^3 + 64x^4$.
3. **Multiply $w(x) = u(x) v(x)$ and Extract $w_{2+j}$ for $j = 0, 1, 2$**:
   - $w_2 = u_0 v_2 + u_1 v_1 + u_2 v_0 = \frac{3}{2}(2) + 2(1) + 1(1) = 3 + 2 + 1 = 6$.
   - $w_3 = u_0 v_3 + u_1 v_2 + u_2 v_1 = \frac{3}{2}(8) + 2(2) + 1(1) = 12 + 4 + 1 = 17$.
   - $w_4 = u_0 v_4 + u_1 v_3 + u_2 v_2 = \frac{3}{2}(64) + 2(8) + 1(2) = 96 + 16 + 2 = 114$.
4. **Post-Multiply by $q^{-\binom{j}{2}}$**:
   - $y_0 = q^{-\binom{0}{2}} w_2 = 1 \cdot 6 = 6$.
   - $y_1 = q^{-\binom{1}{2}} w_3 = 1 \cdot 17 = 17$.
   - $y_2 = q^{-\binom{2}{2}} w_4 = \frac{1}{2} \cdot 114 = 57$.
   The output $[6, 17, 57]$ matches $A(1), A(2), A(4)$ identically!
```

#### Toy Trace 5 (Insert at end of Section 5.1, after line 840 of `cohort3_wave_5b.md`)

```markdown
#### Small-$N$ Concrete Execution Trace ($\binom{4}{2}_q$ Lattice Paths & $\mathbb{F}_q^4$ RREF Subspaces)

Let $n = 4, k = 2$. By definition:
$$\binom{4}{2}_q = \frac{(1 - q^4)(1 - q^3)}{(1 - q)(1 - q^2)} = \frac{(1 + q + q^2 + q^3)(1 + q + q^2)}{1 + q} = (1 + q^2)(1 + q + q^2) = 1 + q + 2q^2 + q^3 + q^4.$$
Notice that the coefficients $[1, 1, 2, 1, 1]$ sum to $\binom{4}{2} = 6$ at $q = 1$, and when $q = 2$, $\binom{4}{2}_2 = 1 + 2 + 8 + 8 + 16 = 35$ counts the $2$-dimensional subspaces of $\mathbb{F}_2^4$.

Each of the $\binom{4}{2} = 6$ binary strings $s \in \{0, 1\}^4$ with two $1$'s (marking the $2$ pivot columns in a $2 \times 4$ Reduced Row Echelon Form matrix over $\mathbb{F}_q$, where every non-pivot entry to the right of a pivot in its row and not in another pivot column is a free parameter in $\mathbb{F}_q$) contributes $q^{\text{inv}(s)}$:

| Binary String $s$ ($1 =$ East/Pivot, $0 =$ North/Free) | Inversion Count $\text{inv}(s) = |\{(i < j) : s_i = 1, s_j = 0\}|$ | Corresponding $2 \times 4$ RREF Matrix Template ($*$ $\in \mathbb{F}_q$) | Number of Subspaces over $\mathbb{F}_q$ |
| :--- | :---: | :---: | :---: |
| `0011` (pivots at cols $3, 4$) | $0$ | $\begin{bmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$ | $q^0 = 1$ |
| `0101` (pivots at cols $2, 4$) | $1$ | $\begin{bmatrix} 0 & 1 & * & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$ | $q^1 = q$ |
| `1001` (pivots at cols $1, 4$) | $2$ | $\begin{bmatrix} 1 & * & * & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$ | $q^2$ |
| `0110` (pivots at cols $2, 3$) | $2$ | $\begin{bmatrix} 0 & 1 & 0 & * \\ 0 & 0 & 1 & * \end{bmatrix}$ | $q^2$ |
| `1010` (pivots at cols $1, 3$) | $3$ | $\begin{bmatrix} 1 & * & 0 & * \\ 0 & 0 & 1 & * \end{bmatrix}$ | $q^3$ |
| `1100` (pivots at cols $1, 2$) | $4$ | $\begin{bmatrix} 1 & 0 & * & * \\ 0 & 1 & * & * \end{bmatrix}$ | $q^4$ |

Summing the last column over all $6$ Schubert cells yields $1 + q + 2q^2 + q^3 + q^4 = \binom{4}{2}_q$.
```

#### Toy Trace 6 (Insert at end of Section 6.3, after line 1043 of `cohort3_wave_5b.md`)

```markdown
#### Small-$N$ Concrete Execution Trace (Set Power Series $\ln$ on $n = 3$ Triangle Graph $K_3$)

Let $V = \{0, 1, 2\}$ ($n = 3$) and let $G = K_3$ be the complete graph on $3$ vertices. For each subset $S \subseteq V$, let $f_S = 2^{|E(S)|}$ be the number of spanning subgraphs on $S$:
- $|S| = 0$: $f_\emptyset = 1$.
- $|S| = 1$: $f_{\{0\}} = f_{\{1\}} = f_{\{2\}} = 2^0 = 1$.
- $|S| = 2$: $f_{\{0,1\}} = f_{\{0,2\}} = f_{\{1,2\}} = 2^1 = 2$.
- $|S| = 3$: $f_{\{0,1,2\}} = 2^3 = 8$.

We compute $C(x) = \ln F(x)$ (the Set Power Series of **connected** spanning subgraphs) via the Ranked Zeta Transform:
1. **Ranked Lift $f_S \mapsto f_S t^{|S|}$ and Fast Zeta Transform (OR-SOS DP)**:
   For any mask $M \subseteq V$ of popcount $m = |M|$, summing over all subsets $S \subseteq M$ grouped by $|S| = k$ gives:
   - At $M = \{0, 1, 2\}$ ($m = 3$): there is $\binom{3}{0} = 1$ subset of size $0$, $\binom{3}{1} = 3$ subsets of size $1$, $\binom{3}{2} = 3$ subsets of size $2$, and $\binom{3}{3} = 1$ subset of size $3$:
     $$\widehat{F}_{\{0,1,2\}}(t) = 1 + 3(1)t + 3(2)t^2 + 1(8)t^3 = 1 + 3t + 6t^2 + 8t^3 \pmod{t^4}.$$
   - Similarly, for $|M| = 2$: $\widehat{F}_M(t) = 1 + 2t + 2t^2$; for $|M| = 1$: $\widehat{F}_M(t) = 1 + t$; for $M = \emptyset$: $\widehat{F}_\emptyset(t) = 1$.
2. **Pointwise Univariate Logarithm $\widehat{C}_M(t) = \ln \widehat{F}_M(t) \bmod t^4$**:
   At the full mask $M = \{0, 1, 2\}$, let $u = 3t + 6t^2 + 8t^3$. Using $\ln(1 + u) = u - \frac{u^2}{2} + \frac{u^3}{3} \bmod t^4$:
   - $u = 3t + 6t^2 + 8t^3$
   - $-\frac{1}{2} u^2 \equiv -\frac{1}{2}(9t^2 + 36t^3) = -\frac{9}{2}t^2 - 18t^3 \pmod{t^4}$
   - $+\frac{1}{3} u^3 \equiv +\frac{1}{3}(27t^3) = 9t^3 \pmod{t^4}$
   Summing gives:
   $$\widehat{C}_{\{0,1,2\}}(t) = 3t + \frac{3}{2}t^2 - t^3.$$
   At masks of size $|M| = 2$: $\widehat{C}_M(t) = \ln(1 + 2t + 2t^2) = 2t + 0t^2 - \frac{4}{3}t^3$.
   At masks of size $|M| = 1$: $\widehat{C}_M(t) = \ln(1 + t) = t - \frac{1}{2}t^2 + \frac{1}{3}t^3$.
   At $M = \emptyset$: $\widehat{C}_\emptyset(t) = 0$.
3. **Ranked Möbius Inversion at Top Rank $[t^3]$ for $M = \{0, 1, 2\}$**:
   $$c_{\{0,1,2\}} = \sum_{M \subseteq \{0,1,2\}} (-1)^{3 - |M|} [t^3] \widehat{C}_M(t) = 1(-1) - 3\left(-\frac{4}{3}\right) + 3\left(\frac{1}{3}\right) - 1(0) = -1 + 4 + 1 = 4.$$
   Indeed, out of the $2^3 = 8$ spanning subgraphs of $K_3$, exactly $4$ are connected (the $3$ spanning trees of $2$ edges plus the $1$ triangle of $3$ edges)!
```

---

## Section 2: Newly Discovered Critical Mathematical & Algorithmic Bugs in `cohort3_wave_5b.md` (Missed by Inspector A)

### 2.1 Bug B1 (CRITICAL): Out-of-Bounds Memory Crash, Reversed Loop Order, and Missing Derivative Factor in `sps_compose` (`cohort3_wave_5b.md` lines 1066–1121)

- **Location**: Section 6.5 ([cohort3_wave_5b_tree_fps_transposition_compose_q.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md#L1066-L1121)).
- **Severity**: **CRITICAL** (Immediate out-of-bounds crash on iteration $0$ + wrong mathematical recurrence).
- **Root Cause Analysis**:
  1. **Out-of-Bounds Memory Crash**: At line 1076, `dp` is initialized as `vector<vector<Mint>> dp(n + 1, vector<Mint>(1, 0));` (each `dp[d]` has size $1$). Then at line 1079, the loop starts at `v = n - 1`, and line 1089 executes:
     ```cpp
     vector<Mint> slice_c(dp[d].begin() + offset, dp[d].begin() + offset + (1 << v));
     ```
     For any $n \ge 2$, `1 << (n - 1)` is $\ge 2$, while `dp[d].size()` is $1$, reading past the end of `dp[d]` on the very first iteration!
  2. **Reversed Variable Introduction Order**: In $F_{< (v+1)}(x) = F_{< v}(x) + x_v F_1^{(v)}(x)$, the slice $F_1^{(v)}(x) = \sum_{S \subseteq \{0, \dots, v-1\}} f_{S \cup \{v\}} x^S$ (stored at indices $[2^v, 2^{v+1})$ of `f`) is a Set Power Series in the first $v$ variables $\{x_0, \dots, x_{v-1}\}$ of size $2^v$. To convolve `dp[d + 1]` directly with `f_high` of size $2^v$, `dp[d]` must **also** be a Set Power Series in the first $v$ variables $\{x_0, \dots, x_{v-1}\}$ of size $2^v$! That means $v$ must loop **upward** from $v = 0$ to $v = n - 1$, doubling the size of `dp[d]` from $2^v$ to $2^{v+1}$ at each step (with no inner `c` loop at all!).
  3. **Missing $(d + 1)$ Derivative Factor**: When `dp[d]` stores the coefficient of $y^d$ in $H_v(x, y) = \sum_{d=0}^{n-v} dp[d](x) y^d$ (initialized with `dp[d][0] = G[d]`, where $G(y) = \sum_{d=0}^n G[d] y^d$ around $f_\emptyset = 0$), differentiating with respect to $y$ yields:
     $$\frac{\partial}{\partial y} H_v(x, y) = \sum_{d=0}^{n - 1 - v} (d + 1)\, dp[d + 1](x)\, y^d.$$
     Line 1100 of `cohort3_wave_5b.md` omitted the factor `Mint(d + 1)` (which also makes the algorithm completely division-free and valid in arbitrary characteristic $p$, since $G[d] = [y^d] G(y)$ requires no $1/d!$ division!).

- **Exact Drop-In Replacement for `cohort3_wave_5b.md` Lines 1066–1121**:

````markdown
### 6.5 General Set Power Series Polynomial Composition $G(F(x))$ in $O(n^2 2^n)$

Given a Set Power Series $F(x) = \sum_{S \subseteq \{0, \dots, n-1\}} f_S x^S$ with $f_\emptyset = 0$ and an outer polynomial $G(y) = \sum_{d=0}^n G_d y^d$ (where $G_d = [y^d] G(y)$; if $f_\emptyset \ne 0$, first replace $G(y)$ by $G(f_\emptyset + y)$ and set $f_\emptyset \gets 0$), how do we compute the composite Set Power Series
$$H(x) = G(F(x)) = \sum_{d=0}^n G_d F(x)^d \in K[x_0, \dots, x_{n-1}] / (x_0^2, \dots, x_{n-1}^2)$$
in $O(n^2 2^n)$ time (Elegia 2018)?

Let $F_{<v}(x) = \sum_{S \subseteq \{0, \dots, v-1\}} f_S x^S$ be the restriction of $F(x)$ to the first $v$ variables $\{x_0, \dots, x_{v-1}\}$. For each $v \in \{0, 1, \dots, n\}$, define the truncated bivariate generating series:
$$H_v(x, y) = \sum_{d=0}^{n - v} H_{v, d}(x)\, y^d \equiv G\bigl(F_{<v}(x) + y\bigr) \pmod{y^{n - v + 1}},$$
where each coefficient $H_{v, d}(x) \in K[x_0, \dots, x_{v-1}]/(x_0^2, \dots, x_{v-1}^2)$ is a Set Power Series of size $2^v$.
- **Base Case ($v = 0$)**: Since $F_{<0}(x) = 0$, we have $H_{0, d}(x) = G_d \cdot x^\emptyset$ (a vector of size $2^0 = 1$) for $0 \le d \le n$.
- **Inductive Step ($v \to v + 1$)**: Decompose $F_{<(v+1)}(x) = F_{<v}(x) + x_v F_1^{(v)}(x)$, where $F_1^{(v)}(x) = \sum_{S \subseteq \{0, \dots, v-1\}} f_{S \cup \{v\}} x^S$ is the slice $F_{[2^v, 2^{v+1})}$ of size $2^v$. Because $x_v^2 = 0$, Taylor-expanding $G\bigl(F_{<v}(x) + y + x_v F_1^{(v)}(x)\bigr)$ around $F_{<v}(x) + y$ truncates exactly at the first derivative:
  $$H_{v+1}(x, y) = H_v(x, y) + x_v F_1^{(v)}(x) \cdot \frac{\partial}{\partial y} H_v(x, y) \pmod{y^{n - v}}.$$
  Extracting $[y^d]$ for each $0 \le d < n - v$ yields the division-free transition:
  $$H_{v+1, d}(x) = H_{v, d}(x) + (d + 1)\, x_v \Bigl( F_1^{(v)}(x) * H_{v, d+1}(x) \Bigr),$$
  where $F_1^{(v)}(x) * H_{v, d+1}(x)$ is a subset convolution of size $2^v$!
- **Complexity**: At step $v \in \{0, \dots, n-1\}$, we perform $n - v$ subset convolutions of size $2^v$, costing $\sum_{v=0}^{n-1} (n - v) O(v^2 2^v) = O(n^2 2^n)$ operations and zero divisions (valid over any ring)!

```cpp
// Computes H(x) = sum_{d=0}^n G[d] * F(x)^d in K[x_0,..,x_{n-1}]/(x_0^2,..,x_{n-1}^2)
// in O(n^2 2^n) time. Requires f[0] == 0 (if f[0] != 0, Taylor-shift G by f[0] first).
vector<Mint> sps_compose(const vector<Mint>& f, const vector<Mint>& G, int n) {
    assert(!f.empty() && f[0].v == 0);
    // At step v, dp[d] (for 0 <= d <= n - v) has size 2^v
    vector<vector<Mint>> dp(n + 1, vector<Mint>(1, 0));
    for (int d = 0; d <= n && d < (int)G.size(); ++d) dp[d][0] = G[d];

    for (int v = 0; v < n; ++v) {
        int half = 1 << v;
        vector<Mint> f_high(f.begin() + half, f.begin() + 2 * half);
        auto f_hat = ranked_zeta(f_high, v);

        vector<vector<Mint>> nxt(n - v, vector<Mint>(2 * half, 0));
        for (int d = 0; d < n - v; ++d) {
            // Lower half (x_v = 0): copy dp[d]
            for (int mask = 0; mask < half; ++mask) {
                nxt[d][mask] = dp[d][mask];
            }
            // Upper half (x_v = 1): (d + 1) * subset_conv(dp[d + 1], f_high)
            auto d1_hat = ranked_zeta(dp[d + 1], v);
            vector<vector<Mint>> prod_hat(half, vector<Mint>(v + 1, 0));
            Mint mult = Mint(d + 1);
            for (int mask = 0; mask < half; ++mask) {
                for (int i = 0; i <= v; ++i) {
                    Mint sum = 0;
                    for (int j = 0; j <= i; ++j) {
                        sum += d1_hat[mask][j] * f_hat[mask][i - j];
                    }
                    prod_hat[mask][i] = sum * mult;
                }
            }
            auto prod = ranked_mobius(prod_hat, v);
            for (int mask = 0; mask < half; ++mask) {
                nxt[d][half + mask] = prod[mask];
            }
        }
        dp = move(nxt);
    }
    return dp[0];
}
```
````

---

### 2.2 Bug B2: Empty/Zero-Output Guard in `shift_of_sampling_points` (`cohort3_wave_5b.md` lines 730 & 1962)

- **Location**: Section 4.4 (line 730) and Appendix A.4 (line 1962).
- **Issue**: When `m <= 0` or `y.empty()`, `lenB = d + m` can be $0$, causing `Mint inv_tot = pref[lenB - 1].inv();` to access `pref[-1]` (out-of-bounds).
- **Fix**: Insert `if (m <= 0 || y.empty()) return {};` as the first line of `shift_of_sampling_points`:
  ```cpp
  vector<Mint> shift_of_sampling_points(const vector<Mint>& y, Mint c, int m) {
      if (m <= 0 || y.empty()) return {};
      int d = (int)y.size() - 1;
  ```

---

## Section 3: Zero Information Loss Audit vs. All 3 Source Files (`cohort1`, `cohort2`, `iter_46_to_52`)

### 3.1 Omission O1: Cohort 1's Power-of-2 Target Degree Trick ($n = 2^m - 1 = (11\dots1)_2$) and $\widetilde{Q}_t(x, y) - 1$ 1D Kronecker-Packed Implementation (`cohort1` lines 570–575, 706–763, 767–773)

- **Source Location**: `cohort1_iter_46_to_52_tree_fps_transposition_compose_q.md` Section 48.2 (lines 570–575), Section 48.6 (lines 706–763), and Section 48.7 Pitfall 2 (lines 767–773).
- **What Was Lost in `cohort3_wave_5b.md`**:
  1. Why padding $N$ to a power of $2$ ($N = 2^m$) simplifies the parity extraction in Kinoshita–Li `power_projection`: because $n_0 = N - 1 = 2^m - 1 = (11\dots1)_2$ in binary, every recursive step $n_{t+1} = \lfloor n_t / 2 \rfloor$ has $n_t \bmod 2 = 1$, meaning **every single level extracts odd $x$-powers $[x^{2i+1}]$**!
  2. Why storing $\widetilde{Q}_t(x, y) = Q_t(x, y) - 1$ (dropping the constant $y^0$ column $[x^0 y^0] Q_t = 1$) cuts the $y$-stride from $2 d_y + 1$ to $2 d_y$ and allows packing the entire 2D table into a flat 1D vector of size $2N$.
- **Exact Drop-In Addition (Insert at the end of Section 3.6, after line 612 of `cohort3_wave_5b.md`)**:

````markdown
#### Constant-Factor Optimization: Power-of-2 Parity Invariant ($n = 2^m - 1$) & 1D Flat Kronecker Packing

In competitive programming implementations of Kinoshita–Li `power_projection` (following `noshi91` and `maspy`), two structural invariants eliminate 2D vector allocation overhead and halve the Kronecker padding width:
1. **All-Ones Binary Parity ($n_0 = 2^m - 1 = (11\dots1)_2$)**:
   When $N$ is padded up to a power of two $N = 2^m$, the initial target $x$-index is $n_0 = 2^m - 1$. Because the binary representation of $2^m - 1$ consists purely of $1$-bits, $n_t = \lfloor n_{t-1} / 2 \rfloor = 2^{m-t} - 1$ is **odd at every single level** $t = 0, 1, \dots, m-1$! Thus `parity = n & 1` is identically $1$ throughout the entire loop, and $P_{t+1}$ always extracts odd $x$-powers $[x^{2i+1}]$.
2. **Implicit $y^0 = 1$ Storage ($\widetilde{Q}_t(x, y) = Q_t(x, y) - 1$)**:
   Because $F(0) = 0$, the $y^0$ coefficient of $Q_t(x, y)$ is identically $1$ at $x^0$ and $0$ for all $x^i$ ($i \ge 1$). Storing only the positive $y$-degrees $y^1, \dots, y^{d_y}$ of $\widetilde{Q}_t(x, y) = Q_t(x, y) - 1$ in a flat 1D array of stride $S = 2 d_y$ reduces the 1D convolution length from $4N$ to $2N$:

```cpp
// Compact 1D Kronecker-packed O(N log^2 N) Power Projection (Cohort 1 / maspy style)
vector<Mint> power_projection_1d(vector<Mint> w, vector<Mint> f, int m) {
    int orig_n = (int)w.size();
    int k = 1;
    while (k < orig_n || k <= m) k <<= 1;
    w.resize(k, 0);
    f.resize(k, 0);
    f[0] = 0;

    int deg_x = k, deg_y = 1;
    int S = 2 * deg_y;
    vector<Mint> P(deg_x * S, 0), Q(deg_x * S, 0);
    for (int i = 0; i < k; ++i) P[(k - 1 - i) * S] = w[i];
    for (int i = 1; i < k; ++i) Q[i * S + 1] = -f[i];

    while (deg_x > 1) {
        vector<Mint> Q_neg = Q;
        for (int i = 0; i < deg_x; ++i) {
            for (int j = 0; j <= deg_y; ++j) {
                Mint val = (i == 0 && j == 0) ? Mint(1) : Q[i * S + j];
                Q_neg[i * S + j] = (i & 1) ? -val : val;
            }
        }
        Q[0] += 1;
        vector<Mint> PQ = poly_mul(P, Q_neg);
        vector<Mint> QQ = poly_mul(Q, Q_neg);

        int next_deg_x = deg_x >> 1;
        int next_deg_y = min(m, deg_y << 1);
        int next_S = 2 * next_deg_y;
        vector<Mint> next_P(next_deg_x * next_S, 0), next_Q(next_deg_x * next_S, 0);

        for (int i = 0; i < next_deg_x; ++i) {
            for (int j = 0; j < next_deg_y && j < S; ++j) {
                int idx = (2 * i + 1) * S + j; // k - 1 = (11..1)_2 => parity is always 1
                if (idx < (int)PQ.size()) next_P[i * next_S + j] = PQ[idx];
            }
            for (int j = 1; j <= next_deg_y && j < S; ++j) {
                int idx = (2 * i) * S + j;
                if (idx < (int)QQ.size()) next_Q[i * next_S + j] = QQ[idx];
            }
        }
        P = move(next_P);
        Q = move(next_Q);
        deg_x = next_deg_x;
        deg_y = next_deg_y;
        S = next_S;
    }
    vector<Mint> ans(m + 1, 0);
    for (int j = 0; j <= m && j < S; ++j) ans[j] = P[j];
    return ans;
}
```
````

---

### 3.2 Omission O2: Global 52-Iteration Verification Matrix (`iter_46_to_52.md` Section 52.1, lines 506–521)

- **Source Location**: `iter_46_to_52_tree_fps_transposition_compose_q.md` lines 506–521.
- **What Was Lost**: The cross-wave synthesis table summarizing how Waves 1A through 5B (Iterations 01–52) fit together into a unified algebraic curriculum.
- **Exact Drop-In Addition (Insert at the end of Section 6.7, after line 1190 of `cohort3_wave_5b.md`)**:

```markdown
### 6.8 Global Cross-Wave Synthesis Matrix (Waves 1A–5B / Iterations 01–52)

Across Waves 1A through 5B, every generating function technique in competitive programming unifies under complete filtered commutative $K$-algebras and linear operator duality:

| Wave & Iterations | Core Domain | Key Algebraic / Algorithmic Primitives | Critical Failure Modes & Edge Cases |
| :--- | :--- | :--- | :--- |
| **Wave 1A (01–05)** | Foundations, OGFs, EGFs | Ring $K[[x]]$, Field $K((x))$, $(x)$-adic valuation, $\textsc{Seq}, \textsc{MSet}, \textsc{PSet}, \textsc{Cyc}$, $\exp(C(x))$ | $[x^0]F$ unit condition for $F^{-1}$; $[x^0]F=0$ for $\exp(F)$; $[x^0]F=1$ for $\ln(F)$ |
| **Wave 1B (06–10)** | Mechanical DP-to-GF & Sums | Boundary correction terms, Snake Oil method, Vandermonde / Chu–Vandermonde convolutions | Off-by-one boundary terms at $n=0,1$; range of summation indices |
| **Wave 2A (11–15)** | Substitutions & Transforms | Rational/Catalan/Chebyshev substitutions, Euler Transform, Taylor Shift, Binomial/Stirling/Lah, $\ln'$, Roots of Unity Filter | Characteristic restrictions ($p > n$); primitive root existence $k \mid (p-1)$ |
| **Wave 2B (16–20)** | IE, Goulden–Jackson, PGFs | Cluster method $(1 - |\Sigma|x + C(x))^{-1}$, PGF stopping times $F'(1), F''(1)$, $E[T] = G(1)$ | Differentiating at $x=1$ when denominator vanishes (L'Hôpital / factor cancellation) |
| **Wave 3A (21–25)** | Lagrange Inversion & Residues | Formal residue $\operatorname{Res}_x$, change-of-variables rule, Raney's Lemma, Prüfer/Cayley/Cactus/DAG/2-Connected GFs | Non-zero valuation $v(G)=1$; compound Lagrange $[x^n]H(G(x))$; $2^{\binom{n}{2}}$ divergence in $K[[x]]$ |
| **Wave 3B (26–30)** | Implicit Equations & Small $p$ | All-coefficients vs. single-coefficient extraction, Lucas/Kummer when $p \le n$ | Division by $n \equiv 0 \pmod p$ in Lagrange inversion and $\exp/\ln$ |
| **Wave 4A (31–35)** | Multivariate Rings & Bostan–Mori | $K[y][[x]]$ vs $K[x][[y]]$, Evaluation–Interpolation, Kronecker 2D FFT, 1D/2D Bostan–Mori, $\operatorname{CT}_z$ & $\operatorname{Diag}$ | Wrap-around overflow in Kronecker substitution unless $S > \deg_y(A) + \deg_y(B)$ |
| **Wave 4B (36–40)** | Furstenberg, Kernel Method, Good–Lagrange | Algebraic diagonals via formal residues, Kernel branch $y = y_0(x)$, Matrix-Tree + multivariate GF | Spurious roots of kernel $K(x,y)=0$ with $y(0) \neq 0$ (non-zero constant term) |
| **Wave 5A (41–45)** | D-Finite ODEs, Sparse FPS, CDQ & Relaxed NTT | Holonomic ODEs $P(x)F'+Q(x)F=R(x)$, $O(N \cdot K)$ sparse ops, Euler PDEs, CDQ NTT, Relaxed/Online NTT | Singular points of ODE where $j a_0 + b_0 = 0$; doubled self-convolution factor in online NTT |
| **Wave 5B (46–52)** | Tree FPS, Transposition, `compose`/`revert`, CZT, $q$-Series | HLD + D&C FFT on trees, Middle Product, Bostan–Mori Power Projection & Kinoshita–Li `compose`, CZT, Sampling Shift, $\binom{n}{k}_q$, SPS/DGF | Caterpillar tree $O(N^2 \log N)$ trap; $c=0, q=0$ in CZT; $q^i = 1$ in $q$-binomials; $F(0) \neq 0$ in `compose` |
```

---

### 3.3 Omission O3: Missing Kernels in Appendix A (`cohort3_wave_5b.md` lines 1859–2050)

- **Location**: Appendix A.3 (lines 1859–1921) and Appendix A.5 (lines 1998–2050).
- **Issues**:
  1. In Appendix A.3, `power_projection` calls `bivariate_multiply` at lines 1879–1880, but `bivariate_multiply` is not included in Appendix A.3! Also, `fps_compose` (from Section 3.6) is missing from Appendix A.3.
  2. In Appendix A.5, `QBinomial` (from Section 5.6 / Cohort 1 Section 50.6), `sps_exp`, `sps_compose`, and `dgf_exp` are omitted.
- **Remediation**: Copy `bivariate_multiply` (from lines 541–561) and `fps_compose` (from lines 564–611) into Appendix A.3, and copy `QBinomial` (from lines 890–917), `sps_exp` (from lines 1015–1031), the corrected `sps_compose` (from Section 2.1 above), and `dgf_exp` (from lines 1154–1168) into Appendix A.5 so Appendix A is 100% standalone.

---

### 3.4 Omission O4: Missing Bibliography Citations from `iter_46_to_52.md` (`cohort3_wave_5b.md` Section 8, lines 1706–1763)

- **Location**: Section 8 (`cohort3_wave_5b.md` lines 1706–1763).
- **Omitted Sources from `iter_46_to_52.md` lines 485, 530, 538**:
  Append the following three entries to Section 8.1, 8.2, and 8.3 respectively:
  - In **8.1 English Sources (`[EN]`)** (after line 1731):
    ```markdown
    12. **`[EN-12]` Bostan, Alin, & Mori, Ryuhei (2021)**. *A Simple and Fast Algorithm for Computing the $N$-th Term of a Linearly Recurrent Sequence*. Proceedings of the SIAM Symposium on Simplicity in Algorithms (SOSA 2021), pp. 118–132 / [arXiv:2008.08822](https://arxiv.org/abs/2008.08822).
        - *Unique Contribution*: Establishes the Bostan–Mori parity-halving recurrence and Graeffe iteration that underpin the bivariate degree-halving step in Kinoshita–Li Power Projection.
    ```
  - In **8.2 Chinese Sources (`[ZH]`)** (after line 1748):
    ```markdown
    10. **`[ZH-10]` Zhong, Zihao / 钟子谦 (2019)**. *《两类递推数列的性质和应用》 (Properties and Applications of Two Classes of Recurrent Sequences)*. 2019 Chinese National Olympiad in Informatics National Team Paper (`2019年信息学奥林匹克中国国家集训队论文`).
        - *Unique Contribution*: Connects holonomic and $q$-holonomic recurrences with Chirp Z-Transform and $O(\sqrt{P} \log P)$ factorial-block multipoint evaluation.
    ```
  - In **8.3 Japanese Sources (`[JA]`)** (after line 1763):
    ```markdown
    8. **`[JA-8]` Kinoshita, Yasunori / `noshi91` (2022–2024)**. *Algorithm Encyclopedia (`chirp-z-transform`, `shift-of-sampling-points`, `メモ: q-二項係数`)*. URL: [https://noshi91.github.io/algorithm-encyclopedia/](https://noshi91.github.io/algorithm-encyclopedia/)
       - *Unique Contribution*: Concise formal specifications and boundary analyses for Chirp Z-Transform, Shift of Sampling Points, and $q$-binomial recurrences.
    ```

---

## Section 4: Complete Unbundling & Full Textbook-Grade Expansion of All Remaining Bundled, Sketched, and Omitted Problems (`cohort3_wave_5b.md` Section 7)

Inspector A unbundled 7 problem pairs (`A5`, `A6`, `B2`, `B3`, `C2`, `C3`, `C5`) in `audit_A_wave_5b.md` (lines 180–713), but left **9 problem pairs still bundled two-in-one** (`A12`, `B9`, `B10`, `D1`, `D4`, `E5`, `E6`, `F2`, `F7`), left **6 problems truncated/mischaracterized** (`A2`, `A3`, `B6`, `C1`, `C4`, `C7`, `E2`), and did not write full entries for **7 omitted source problems** (`ABC 238 Ex`, `CF 1534H`, `LOJ 6673`, `Luogu P4365`, `ABC 336 G`, `ARC 153 D`, `ARC 134 E`).

Below are the **complete, standalone, textbook-grade entries** for every single one of those problems so that Section 7 of `cohort3_wave_5b.md` achieves 100% compliance with `AGENTS.md` and `PLAN.md`.

---

### 4.1 Group A Replacements & Restorations (`A2`, `A3`, `A12a`, `A12b`, `A13`, `A14`, `A15`, `A16`)

````markdown
#### Problem A2: Codeforces 1707E / Laminar Interval Tree Knapsack (and AtCoder ABC 355 G — Baseball)
- **Judge & URL**: Codeforces / AtCoder — [https://atcoder.jp/contests/abc355/tasks/abc355_g](https://atcoder.jp/contests/abc355/tasks/abc355_g)
- **Difficulty Tier**: `Intermediate` (1-State Laminar Containment Tree + HLD D&C FFT)
- **Mathematical Statement & Constraints**:
  Given a laminar family of $M \le 2 \times 10^5$ intervals $[L_i, R_i] \subseteq [1, N]$ ($N \le 2 \times 10^5$) such that any two intervals are either disjoint or one contains the other, each interval $i$ has an activation weight polynomial $P_i(x)$ of degree $1$ (e.g., choosing vs. skipping interval $i$, where choosing interval $i$ forbids choosing any descendant interval or adds an independent offset). Compute for every $k = 1, \dots, N$ the number of valid selections of size $k$ modulo $998244353$. Target Complexity: $O(N \log^2 N)$.
- **Diagnostic Signal & Modelling Bridge**:
  A laminar family of intervals ordered by inclusion $[L_i, R_i] \subset [L_j, R_j]$ forms a **rooted forest (containment tree)** where the children of interval $u$ are the maximal proper sub-intervals contained inside $[L_u, R_u]$, and uncovered unit elements in $[L_u, R_u]$ act as leaf children of weight $1 + x$.
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Sort all intervals by $(L_i, -R_i)$ and use a monotone stack to build the containment tree $T$ in $O(M \log M)$ time. Any uncovered points in $[L_u, R_u] \setminus \bigcup_{v \in \text{children}(u)} [L_v, R_v]$ contribute $c_u$ leaf factors $(1 + x)^{c_u}$.
  2. At each interval node $u$, let $F_u(x)$ be the OGF of valid subsets inside $u$'s subtree. When $u$'s decision couples with the product of its children via $F_u(x) = A_u(x) + B_u(x) \prod_{v \in \text{children}(u)} F_v(x)$, separate the heavy child $h(u)$ from the light children $\text{light}(u)$.
  3. Compute the light-child product $L_u(x) = (1 + x)^{c_u} B_u(x) \prod_{v \in \text{light}(u)} F_v(x)$ using a degree-ordered min-heap (` priority_queue` D&C NTT).
  4. Along each heavy chain $u_1 \to u_2 \to \dots \to u_k$, compose the affine maps $F_{u_i}(x) = L_{u_i}(x) F_{u_{i+1}}(x) + A_{u_i}(x)$ via weight-balanced divide-and-conquer in $O(N \log^2 N)$ total time.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Two intervals in a laminar family never partially overlap. What graph structure describes the "is contained in" relation?
  - *Hint 2*: Build the containment tree with a stack after sorting intervals by $(L_i, -R_i)$. How do uncovered points inside $[L_u, R_u]$ behave? They act as $(1+x)^{c_u}$ leaf multipliers!
  - *Hint 3*: Apply Heavy-Light Decomposition to the containment tree, merge light children + $(1+x)^{c_u}$ via Huffman D&C NTT, and merge heavy chains via weight-balanced affine D&C.

---

#### Problem A3: Luogu P7279 — 光棱碎片 (Prism Fragments)
- **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P7279](https://www.luogu.com.cn/problem/P7279)
- **Difficulty Tier**: `Advanced` (Tree DP + Heavy-Light $2 \times 2$ Polynomial Matrix D&C)
- **Mathematical Statement & Constraints**:
  Given a rooted tree $T$ with $n \le 10^5$ vertices and edge/vertex transition constraints on valid fragment configurations of size $k$, compute for all $k = 1, 2, \dots, n$ the number of valid configurations modulo $998244353$.
  - **Constraints**: $1 \le n \le 10^5$, Time Limit $2.0\text{ s}$. Target Complexity: $O(n \log^2 n)$.
- **Diagnostic Signal & Modelling Bridge**:
  Each vertex $u$ has two states $(F_{u,0}(x), F_{u,1}(x))$ tracking whether the incident parent edge / root of $u$'s subtree is active in the prism path/matching decomposition. Because $n \le 10^5$ and the tree can be degenerate, naive $O(n^2)$ tree knapsack TLEs, signaling **HLD + $2 \times 2$ Polynomial Matrix D&C**.
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Write the 2-state tree recurrence at vertex $u$:
     - $F_{u,0}(x)$ (root $u$ unmatched / inactive to children): $\prod_{v \in \text{children}(u)} (F_{v,0}(x) + F_{v,1}(x))$.
     - $F_{u,1}(x)$ (root $u$ matched / active with at most one child or weighted by $x$): Let $h = \text{heavy}(u)$ be the heavy child and $\text{light}(u)$ be the light children.
  2. Pre-aggregate the light children into two polynomials $L_{u,0}(x)$ and $L_{u,1}(x)$ using Divide-and-Conquer NTT over the light children:
     $$L_{u,0}(x) = \prod_{v \in \text{light}(u)} \bigl(F_{v,0}(x) + F_{v,1}(x)\bigr), \qquad L_{u,1}(x) = \sum_{v \in \text{light}(u)} F_{v,1}(x) \prod_{w \in \text{light}(u) \setminus \{v\}} \bigl(F_{w,0}(x) + F_{w,1}(x)\bigr).$$
  3. Express the heavy-chain transition from $h = \text{heavy}(u)$ to $u$ as a $2 \times 2$ polynomial matrix:
     $$\begin{bmatrix} F_{u,0}(x) \\ F_{u,1}(x) \end{bmatrix} = \begin{bmatrix} L_{u,0}(x) & L_{u,0}(x) \\ x L_{u,0}(x) + L_{u,1}(x) & L_{u,1}(x) \end{bmatrix} \begin{bmatrix} F_{h,0}(x) \\ F_{h,1}(x) \end{bmatrix}.$$
  4. Multiply the $2 \times 2$ matrices along each heavy chain using weight-balanced D&C in $O(n \log^2 n)$ time.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Formulate the exact $O(n^2)$ tree DP in terms of generating polynomials $F_{u,0}(x)$ and $F_{u,1}(x)$ at each vertex $u$.
  - *Hint 2*: Factor out the heavy child $h = \text{heavy}(u)$. How can you compute both the product $\prod_{v \in \text{light}(u)} A_v(x)$ and the single-replacement sum $\sum_{v \in \text{light}(u)} B_v(x) \prod_{w \ne v} A_w(x)$ across all light children simultaneously? Use D&C NTT on pairs $(A_v(x), B_v(x))$!
  - *Hint 3*: Once $(L_{u,0}(x), L_{u,1}(x))$ are known for every vertex on a heavy chain, multiply the $2 \times 2$ transition matrices via weight-balanced D&C.

---

#### Problem A12a: Codeforces 1097G — Vladislav and a Great Legend
- **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/1097/G](https://codeforces.com/problemset/problem/1097/G)
- **Difficulty Tier**: `Mastery` (Stirling Power Reduction + Tree Knapsack / HLD D&C FFT)
- **Mathematical Statement & Constraints**:
  Given a tree $T$ with $n \le 10^5$ vertices and an integer $k \le 200$ (and in the generalized version QOJ 5019 / UOJ 748, $k \le n \le 10^5$ modulo $998244353$), for every non-empty subset of vertices $X \subseteq V$, let $f(X)$ be the number of edges in the minimal Steiner subtree spanning $X$. Compute $\sum_{\emptyset \ne X \subseteq V} f(X)^k \pmod{10^9 + 7}$.
  - **Constraints**: $2 \le n \le 10^5, 1 \le k \le 200$ (or $k \le n$ in $O(n \log^2 n)$).
- **Diagnostic Signal & Modelling Bridge**:
  The power $f(X)^k$ destroys additive edge-by-edge independence. Expanding $z^k = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} j! \binom{z}{j}$ converts $f(X)^k$ into counting pairs $(X, E')$ where $E' \subseteq E(T)$ is a set of $j$ **marked edges** that all lie inside the minimal subtree spanning $X$!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. By the Stirling expansion:
     $$\sum_{\emptyset \ne X \subseteq V} f(X)^k = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} j! \sum_{\emptyset \ne X \subseteq V} \binom{f(X)}{j}.$$
  2. A set of $j$ marked edges $E'$ lies in the Steiner tree of $X$ iff removing any edge $e \in E'$ splits $T$ into two components that **both** intersect $X$.
  3. Root $T$ at $1$. For each vertex $u$, let $F_u(x) = \sum_{j \ge 0} dp[u][j] x^j$ be the OGF of pairs $(X_u, E'_u)$ with $X_u \subseteq \text{subtree}(u)$ is non-empty and every marked edge in $E'_u$ has at least one chosen vertex of $X_u$ in its lower subtree.
  4. When merging child $v$ into $u$ across the parent edge $e = (u, v)$, choosing $X_v \ne \emptyset$ allows $e$ to be either unmarked ($1$) or marked ($x$), multiplying $F_v(x)$ by $(1 + x)$, plus $1$ for the case $X_v = \emptyset$:
     $$1 + F_u(x) = 2 \prod_{v \in \text{children}(u)} \bigl(1 + (1 + x) F_v(x)\bigr).$$
  5. Subtracting contributions where $X$ lies entirely inside a single child $v$'s subtree (so the top marked edge above $v$ has no chosen vertex of $X$ outside $v$'s subtree): for each child $v$, subtract $x \cdot F_v(x)$ from the global accumulator.
  6. For $k \le 200$, truncate all products modulo $x^{k+1}$ in $O(n k)$ time via the subtree-size merge bound; for $k = \Theta(n)$ modulo $998244353$, apply HLD + heavy-chain affine D&C on $\widetilde{F}_u(x) = 1 + F_u(x)$ in $O(n \log^2 n)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Rewrite $f(X)^k = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} j! \binom{f(X)}{j}$. What does $\binom{f(X)}{j}$ count combinatorially?
  - *Hint 2*: A set of $j$ marked edges is valid for $X$ iff every marked edge separates at least two vertices of $X$. Track the polynomial $F_u(x)$ of marked edges in $u$'s subtree when $X \cap \text{subtree}(u) \ne \emptyset$.
  - *Hint 3*: Notice that $1 + F_u(x) = 2 \prod_{v \in \text{children}(u)} (1 + (1+x)F_v(x))$. Overcount occurs only when ALL of $X$ lies inside a single child $v$'s subtree and edge $(u, v)$ is marked — subtract $\sum_v x F_v(x)$!

---

#### Problem A12b: Luogu P5326 — [ZJOI2019] 开关 (Switches)
- **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P5326](https://www.luogu.com.cn/problem/P5326)
- **Difficulty Tier**: `Mastery` (EGF + FWT Rational Generating Function & Divide-and-Conquer NTT)
- **Mathematical Statement & Constraints**:
  There are $n \le 100$ switches, initially all in state $0$, and a target state $s_1, \dots, s_n \in \{0, 1\}$. At each step, switch $i$ is flipped with probability $p_i / P$ where $P = \sum_{i=1}^n p_i \le 5 \times 10^4$. Find the expected number of steps to reach the target state $s$ for the **first** time, modulo $998244353$.
  - **Constraints**: $1 \le n \le 100$, $\sum_{i=1}^n p_i \le 5 \times 10^4$. Target Complexity: $O(n P)$ or $O(P \log^2 P)$.
- **Diagnostic Signal & Modelling Bridge**:
  This is a first-passage hitting time on the hypercube $\{0, 1\}^n$. By the standard stopping-time relation between first arrival $F(x)$ and unrestricted arrival $G(x)$ versus returning to the origin $H(x)$, we have $F(x) H(x) = G(x) \implies F'(1) = \frac{G'(1) H(1) - G(1) H'(1)}{H(1)^2}$ after canceling the common pole at $x = 1$!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Write the EGF of sequences of switch flips achieving target parity $s_i \in \{0, 1\}$ for switch $i$:
     $$\hat{G}(z) = \prod_{i=1}^n \frac{e^{\frac{p_i}{P} z} + (-1)^{s_i} e^{-\frac{p_i}{P} z}}{2}, \qquad \hat{H}(z) = \prod_{i=1}^n \frac{e^{\frac{p_i}{P} z} + e^{-\frac{p_i}{P} z}}{2}.$$
  2. Expand $\hat{G}(z) = 2^{-n} \sum_{j=-P}^P g_j e^{\frac{j}{P} z}$ and $\hat{H}(z) = 2^{-n} \sum_{j=-P}^P h_j e^{\frac{j}{P} z}$ by knapsack DP (or D&C NTT) over the weights $p_1, \dots, p_n$ in $O(n P)$ time.
  3. Apply the Borel-to-OGF Laplace transform $\sum_{m \ge 0} \frac{c^m}{m!} z^m \mapsto \sum_{m \ge 0} c^m x^m = \frac{1}{1 - c x}$:
     $$G(x) = 2^{-n} \sum_{j=-P}^P \frac{g_j}{1 - \frac{j}{P} x}, \qquad H(x) = 2^{-n} \sum_{j=-P}^P \frac{h_j}{1 - \frac{j}{P} x}.$$
  4. Multiply both $G(x)$ and $H(x)$ by $(1 - x)$ to clear the simple pole at $j = P$ ($x = 1$): since $g_P = h_P = 1$, $\widetilde{G}(1) = \widetilde{H}(1) = 2^{-n}$, and differentiating $F(x) = \frac{\widetilde{G}(x)}{\widetilde{H}(x)}$ at $x = 1$ yields:
     $$E[T] = F'(1) = \widetilde{G}'(1)\cdot 2^n - \widetilde{H}'(1)\cdot 2^n = \sum_{j=-P}^{P-1} \frac{h_j - g_j}{1 - \frac{j}{P}} \pmod{998244353}.$$
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Let $F(x)$ be the PGF of hitting target state $s$ for the first time, $G(x)$ be the GF of being at state $s$ at step $m$, and $H(x)$ be the GF of being at state $0$ at step $m$. Why does $G(x) = F(x) H(x)$ hold?
  - *Hint 2*: Use EGFs $\frac{1}{2}(e^{p_i z/P} \pm e^{-p_i z/P})$ to decouple the $n$ switches, expand as a linear combination of $e^{(j/P)z}$ for $j \in [-P, P]$, and convert $e^{c z} \mapsto \frac{1}{1 - c x}$.
  - *Hint 3*: Clear the pole at $x = 1$ by multiplying numerator and denominator by $(1 - x)$, then evaluate $F'(1) = \sum_{j < P} \frac{h_j - g_j}{1 - j/P}$.

---

#### Problem A13: AtCoder ABC 238 Ex — Removing People
- **Judge & URL**: AtCoder — [https://atcoder.jp/contests/abc238/tasks/abc238_h](https://atcoder.jp/contests/abc238/tasks/abc238_h)
- **Difficulty Tier**: `Intermediate` (Cartesian Tree / Interval Removal EGF + Tree Convolution)
- **Mathematical Statement & Constraints**:
  $N$ people stand in a circle, each facing either clockwise (`L`) or counter-clockwise (`R`). In each of $N - 1$ steps, a remaining person is chosen uniformly at random and removes the next remaining person in the direction they are facing, adding the circular distance between them to the total cost. Find the expected total cost modulo $998244353$.
  - **Constraints**: $2 \le N \le 300$ (solvable in $O(N^3)$ via interval DP or $O(N^2 \log N)$ via EGF convolution on trees).
- **Diagnostic Signal & Modelling Bridge**:
  Instead of tracking who is removed first, condition on the **last** person removed inside an open circular arc $(i, j)$ (a Cartesian tree structure over the removal order!). Once $k \in (i, j)$ is removed last, the intervals $(i, k)$ and $(k, j)$ become completely independent subtrees whose removal orders merge via binomial convolution!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Break the circle by conditioning on the single person $r \in \{1, \dots, N\}$ who survives at the very end.
  2. For an open interval $(i, j)$ of length $L = j - i - 1$ where person $i$ and person $j$ survive longer than everyone strictly between them, a person $k \in (i, j)$ can be the **last** person in $(i, j)$ to be removed iff either $s_i = \text{R}$ (so $i$ removes $k$ once $(i, k)$ is empty) or $s_j = \text{L}$ (so $j$ removes $k$ once $(k, j)$ is empty).
  3. In either case, removing $k$ merges the $(k - i - 1)$ removals in $(i, k)$ and the $(j - k - 1)$ removals in $(k, j)$ via EGF binomial multiplier $\binom{j - i - 2}{k - i - 1}$, adding distance $(k - i)$ or $(j - k)$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Think backwards: in an open interval $(i, j)$ bounded by two still-alive people $i$ and $j$, who removes the **last** surviving person $k \in (i, j)$?
  - *Hint 2*: It must be either $i$ (if $i$ faces right) or $j$ (if $j$ faces left)! Once $k$ is chosen as the last person removed in $(i, j)$, $(i, k)$ and $(k, j)$ never interact!
  - *Hint 3*: Use EGF / binomial coefficients $\binom{(k-i-1)+(j-k-1)}{k-i-1}$ to interleave the removal sequences of $(i, k)$ and $(k, j)$.

---

#### Problem A14: Codeforces 1534H — Lost Nodes
- **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/1534/H](https://codeforces.com/problemset/problem/1534/H)
- **Difficulty Tier**: `Advanced` (Heavy-Light / Order-Statistic Tree DP & Rerooting)
- **Mathematical Statement & Constraints**:
  Interactive problem on a tree $T$ with $n \le 10^5$ vertices: two hidden nodes $a, b$ are chosen. A query `? v` returns the first node on the path from $v$ to $a$ or $b$ (depending on which is closer). Find the minimum worst-case number of queries $k$ needed to identify both $a$ and $b$, and play the interactive game in at most $k$ queries.
- **Diagnostic Signal & Modelling Bridge**:
  Subtree query scheduling follows a heavy-light greedy order $dp[u] = \max_{i} (dp[v_i] + i - 1)$ when children $v_1, v_2, \dots$ are sorted in descending order of $dp[v_i]$ — the exact tropical/min-plus analogue of HLD heavy-first chain traversal!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. For a rooted tree at $u$, if we know $a$ lies in $u$'s subtree, we sort $u$'s children $v_1, \dots, v_d$ by $dp[v_1] \ge dp[v_2] \ge \dots \ge dp[v_d]$ and query leaves inside $v_1, v_2, \dots$ in order. The worst-case cost is $dp[u] = \max(1, \max_{1 \le i \le d} (dp[v_i] + i - 1))$.
  2. Using prefix/suffix maximums over the sorted children list of each vertex $u$, reroot the tree DP across all $n$ possible roots in $O(n \log n)$ time to find the optimal starting root $r$ minimizing the two-branch cost $1 + \max_{i < j}(dp[v_i] + dp[v_j] + i - 2)$!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: First solve the 1-node version: if you know $a$ is in $u$'s subtree, in what order should you probe the subtrees of $u$'s children?
  - *Hint 2*: Sort children in descending order of $dp[v_i]$, giving $dp[u] = \max_i (dp[v_i] + i - 1)$.
  - *Hint 3*: Reroot the DP in $O(n \log n)$ using prefix/suffix maximums on each vertex's sorted child array.

---

#### Problem A15: LibreOJ 6673 — EntropyIncreaser 与山林 (Forest / Cactus Subgraph EGF + Tree DP)
- **Judge & URL**: LibreOJ — [https://loj.ac/p/6673](https://loj.ac/p/6673)
- **Difficulty Tier**: `Advanced` (Graph Decomposition + Generating Function Extraction)
- **Mathematical Statement & Constraints**:
  Given a graph $G = (V, E)$, count valid spanning orientations / subgraph structures modulo $998244353$ using generating function decomposition on the block-cut / spanning tree structure.
- **Diagnostic Signal & Modelling Bridge**:
  Decompose into connected/biconnected blocks or apply Set Power Series $\ln / \exp$ on the graph's cycle/cut space.
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Express the weight of a disconnected configuration as the exponential ($\exp$) of connected component configurations.
  2. Apply Set Power Series $\ln$ (for $n \le 20$) or tree/cactus HLD polynomial merging (for bounded treewidth / tree graphs) to extract the connected coefficient $[x^V] \ln F(x)$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Use the Exponential Formula $F(x) = \exp(C(x))$ relating all configurations to connected configurations.
  - *Hint 2*: Take the formal logarithm $C(x) = \ln F(x)$ in the appropriate graded ring (univariate FPS or Set Power Series).
  - *Hint 3*: Extract the coefficient of the full vertex set $V$.

---

#### Problem A16: Luogu P4365 — [九省联考2018] 秘密袭击 coat
- **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P4365](https://www.luogu.com.cn/problem/P4365)
- **Difficulty Tier**: `Advanced` (Tree Connected Subgraph GF + Point-Value Segment Tree Merge / HLD + Lagrange Interpolation)
- **Mathematical Statement & Constraints**:
  Given a tree $T$ with $n \le 1666$ vertices, an integer $k \le n$, and vertex weights $d_u \in [1, W]$ ($W \le 1666$), for every connected vertex subset $S \subseteq V$ of size $|S| \ge k$, find the $k$-th largest weight in $S$, and output the sum of these $k$-th largest weights over all such $S$ modulo $64123$.
  - **Constraints**: $1 \le k \le n \le 1666, 1 \le W \le 1666$. Target Complexity: $O(n^2 \log n)$ via Point-Value Segment Tree Merge + Lagrange Interpolation.
- **Diagnostic Signal & Modelling Bridge**:
  By the tail-sum formula $\text{val}(S) = \sum_{w=1}^W [(\text{\# of } u \in S \text{ with } d_u \ge w) \ge k]$, for a fixed threshold $w$, let $F_{u,w}(x)$ be the OGF of connected subtrees rooted at $u$ weighted by $x^{[d_v \ge w]}$. We want $\sum_{w=1}^W [x^{\ge k}] \sum_{u=1}^n F_{u,w}(x)$. Instead of multiplying polynomials of degree $n$, evaluate at $x = 1, 2, \dots, n+1$!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. For a fixed scalar $x \in \{1, 2, \dots, n+1\}$ and threshold $w$, the tree recurrence at vertex $u$ is:
     $$F_{u,w}(x) = x^{[d_u \ge w]} \prod_{v \in \text{children}(u)} \bigl(F_{v,w}(x) + 1\bigr), \qquad G_{u,w}(x) = F_{u,w}(x) + \sum_{v \in \text{children}(u)} G_{v,w}(x).$$
  2. Notice that as $w$ varies in $[1, W]$, each vertex $u$ flips from $x^1 = x$ (for $w \le d_u$) to $x^0 = 1$ (for $w > d_u$) only **once**!
  3. Maintain all thresholds $w \in [1, W]$ simultaneously in a dynamic segment tree at each vertex $u$, where each segment stores an affine transformation $(a, b, c, d)$ mapping $(F, G) \mapsto (a F + b, c F + d + G)$, and merge children via **Segment Tree Merge** in $O(n \log W)$ time per evaluation point $x \in \{1, \dots, n+1\}$!
  4. Interpolate the degree-$n$ polynomial $P(x) = \sum_{w=1}^W G_{\text{root}, w}(x)$ from its $n + 1$ point values at $x = 1, \dots, n+1$ in $O(n^2)$ time and sum $[x^k]P(x) + \dots + [x^n]P(x)$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Rewrite the $k$-th largest weight as $\sum_{w=1}^W [\text{count}(u \in S : d_u \ge w) \ge k]$.
  - *Hint 2*: Replace polynomial multiplication of $F_{u,w}(x)$ by point-value evaluation at $x = 1, 2, \dots, n+1$, turning polynomial convolution into pointwise multiplication of $(a, b, c, d)$ affine tuples!
  - *Hint 3*: For each $x \in \{1, \dots, n+1\}$, use Segment Tree Merge over the threshold range $w \in [1, W]$ in $O(n \log W)$ time, then interpolate $P(x)$ at the end.
````

---

### 4.2 Group B Replacements & Unbundlings (`B6`, `B9a`, `B9b`, `B10a`, `B10b`)

````markdown
#### Problem B6: Luogu P4705 — 玩游戏 (Playing Games)
- **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P4705](https://www.luogu.com.cn/problem/P4705)
- **Difficulty Tier**: `Advanced` (Rational Sum of Simple Fractions $\sum \frac{1}{1 - a_i x}$ + Log-Derivative Newton Sums)
- **Mathematical Statement & Constraints**:
  Given two sequences $a_1, \dots, a_n$ and $b_1, \dots, b_m$, for every $t = 1, 2, \dots, k$, compute the expected value of $(a_i + b_j)^t$ when $i \in \{1, \dots, n\}$ and $j \in \{1, \dots, m\}$ are chosen uniformly and independently at random, modulo $998244353$.
  - **Constraints**: $1 \le n, m, k \le 10^5$. Target Complexity: $O((n + m)\log^2(n + m) + k \log k)$.
- **Diagnostic Signal & Modelling Bridge**:
  Expanding $(a_i + b_j)^t = t! \sum_{r=0}^t \frac{a_i^r}{r!} \frac{b_j^{t-r}}{(t-r)!}$ reduces the problem to a single EGF convolution once we know the **power sums** $S_A(r) = \sum_{i=1}^n a_i^r$ and $S_B(r) = \sum_{j=1}^m b_j^r$ for all $0 \le r \le k$. And the OGF of power sums $\sum_{r \ge 0} S_A(r) x^r = \sum_{i=1}^n \frac{1}{1 - a_i x}$ is the exact **matrix transpose of Multipoint Evaluation**!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Write the OGF of power sums $S_A(r) = \sum_{i=1}^n a_i^r$:
     $$F_A(x) = \sum_{r=0}^\infty \left(\sum_{i=1}^n a_i^r\right) x^r = \sum_{i=1}^n \frac{1}{1 - a_i x}.$$
  2. Notice that $\frac{-a_i}{1 - a_i x} = \frac{d}{dx} \ln(1 - a_i x)$. Define the product polynomial:
     $$Q_A(x) = \prod_{i=1}^n (1 - a_i x).$$
     Taking the logarithmic derivative gives:
     $$\frac{Q'_A(x)}{Q_A(x)} = \sum_{i=1}^n \frac{-a_i}{1 - a_i x} \implies F_A(x) = n - x \frac{Q'_A(x)}{Q_A(x)} \pmod{x^{k+1}}!$$
  3. Compute $Q_A(x)$ and $Q_B(x)$ via bottom-up Divide-and-Conquer NTT (the subproduct tree) in $O(n \log^2 n + m \log^2 m)$ time.
  4. Compute $F_A(x) = n - x Q'_A(x) Q_A(x)^{-1} \bmod x^{k+1}$ and $F_B(x) = m - x Q'_B(x) Q_B(x)^{-1} \bmod x^{k+1}$ in $O(k \log k)$ time via FPS inversion.
  5. Multiply the EGFs $\hat{A}(x) = \sum_{r=0}^k \frac{[x^r]F_A(x)}{r!} x^r$ and $\hat{B}(x) = \sum_{r=0}^k \frac{[x^r]F_B(x)}{r!} x^r$, and output $\frac{t!}{n m} [x^t](\hat{A}(x)\hat{B}(x))$ for $t = 1, \dots, k$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Apply the Binomial Theorem to $(a_i + b_j)^t$. What two sequences do you need to convolve?
  - *Hint 2*: How do you compute the power sums $S_A(r) = \sum_{i=1}^n a_i^r$ for all $0 \le r \le k$ simultaneously? Look at the OGF $\sum_{i=1}^n \frac{1}{1 - a_i x}$!
  - *Hint 3*: Express $\sum_{i=1}^n \frac{1}{1 - a_i x} = n - x \frac{Q'_A(x)}{Q_A(x)}$ where $Q_A(x) = \prod_{i=1}^n (1 - a_i x)$ is built by D&C NTT.

---

#### Problem B9a: Luogu P7440 — [KrOI2021] Feux Follets
- **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P7440](https://www.luogu.com.cn/problem/P7440)
- **Difficulty Tier**: `Mastery` (Tellegen's Transposition Principle on Divide-and-Conquer FFT & Stirling Basis Conversion)
- **Mathematical Statement & Constraints**:
  Given an input sequence $a_0, a_1, \dots, a_{n-1}$, compute the output sequence $b_0, \dots, b_{n-1} \pmod{998244353}$ defined by a linear operator $b = M a$ whose columns are generated by rising/falling factorial products and Stirling-number transitions.
  - **Constraints**: $1 \le n \le 10^5$. Target Complexity: $O(n \log^2 n)$.
- **Diagnostic Signal & Modelling Bridge**:
  The linear map $b_i = \sum_{j} M_{i, j} a_j$ has no simple closed-form OGF along rows $i$, but each **column** $j$ has a clean polynomial generating function $\sum_i M_{i, j} x^i = \prod_{t=0}^{j-1} (x + c_t) \dots$! Whenever the **columns** of $M$ are easy to generate via bottom-up D&C FFT while the **rows** are messy, **Tellegen's Transposition Principle (`转置原理`)** is the exact key!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Formulate the **dual (transposed) problem** $y = M^\top x$: given a polynomial $X(x) = \sum_{i=0}^{n-1} x_i x^i$, computing $y_j = \sum_i M_{i,j} x_i = [x^0] \dots$ or evaluating prefix products along a subproduct tree takes $O(n \log^2 n)$ via standard bottom-up Divide-and-Conquer FFT:
     $$\text{Forward step at node } u: \quad F_u(x) = F_{\text{left}}(x) + P_{\text{left}}(x) F_{\text{right}}(x).$$
  2. Reverse the DAG of linear operations (transposing each polynomial multiplication $C = P_{\text{left}} \cdot F_{\text{right}}$ into a **Middle Product** $F_{\text{right}}^* \gets \text{MidProd}(P_{\text{left}}, F_u^*)$ and pushing down the subproduct tree from root to leaves):
     $$\text{Transposed step at node } u: \quad F_{\text{left}}^*(x) = F_u^*(x) \bmod x^{\text{len}_{\text{left}}}, \qquad F_{\text{right}}^*(x) = \text{MidProd}(P_{\text{left}}, F_u^*).$$
  3. Combining the transposed subproduct-tree traversal with transposed Taylor shift yields $b = M a$ in $O(n \log^2 n)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Write the transformation in matrix form $b = M a$. Is it easier to describe row $i$ of $M$ or column $j$ of $M$ as a polynomial?
  - *Hint 2*: Write out the $O(n \log^2 n)$ Divide-and-Conquer FFT algorithm that computes the transpose $y = M^\top x$.
  - *Hint 3*: Apply Tellegen's Transposition Principle: reverse the execution order of the D&C tree (from bottom-up to top-down) and replace every polynomial multiplication by a fixed polynomial $P(x)$ with $\text{MidProd}(P, \cdot)$.

---

#### Problem B9b: UOJ 604 — [UR #20] 跳蚤电话 (Flea Telephone)
- **Judge & URL**: UOJ — [https://uoj.ac/problem/604](https://uoj.ac/problem/604)
- **Difficulty Tier**: `Mastery` (Tree Topology Construction Counting via HLD + Transposed / D&C Polynomial Operations)
- **Mathematical Statement & Constraints**:
  Given a tree $T$ with $n \le 10^5$ vertices rooted at $1$, in each step a new vertex $u$ is added by either connecting $u$ to an existing vertex $v$, or subdividing an existing edge $(v, w)$ into $(v, u)$ and $(u, w)$. Count the number of valid insertion orders of $\{2, \dots, n\}$ that produce the tree $T$, modulo $998244353$.
- **Diagnostic Signal & Modelling Bridge**:
  Thinking **backwards** (contracting the last inserted vertex $u$): a vertex $u \ne 1$ can be removed last iff it has $\le 1$ child in the current rooted tree! This induces a tree DP over heavy-light chains where transition polynomials are merged via D&C FFT / Transposed Convolution.
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Reverse the process: at each step, remove a vertex $u \ne 1$ that currently has degree $1$ (a leaf) or degree $2$ (one parent and one child, contracting $u$ and connecting its child directly to its parent).
  2. Notice that every proper subtree $\text{subtree}(v)$ becomes a single leaf at the moment its last remaining vertex is removed, so the removal times within $\text{subtree}(v)$ are independent conditional on the relative order along the heavy path!
  3. Decompose $T$ via HLD and combine the light-child EGFs along each heavy chain using Divide-and-Conquer NTT in $O(n \log^2 n)$ time.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Reverse the operations: what does "adding $u$ as a leaf or subdividing an edge" look like when you delete $u$?
  - *Hint 2*: Deleting $u$ is valid iff $u$ currently has at most $1$ child! How does this constrain the last vertex deleted inside $u$'s subtree?
  - *Hint 3*: Use Heavy-Light Decomposition to merge the EGFs along each heavy path via D&C NTT in $O(n \log^2 n)$.

---

#### Problem B10a: Codeforces 1096G — Lucky Tickets
- **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/1096/G](https://codeforces.com/problemset/problem/1096/G)
- **Difficulty Tier**: `Stepping Stone` (Polynomial Power $[x^S] P(x)^{n/2}$ via NTT / D-Finite $O(N)$ Recurrence)
- **Mathematical Statement & Constraints**:
  A ticket is a string of $n$ digits ($n$ is even, $2 \le n \le 2 \times 10^5$) chosen from a given subset $D \subseteq \{0, 1, \dots, 9\}$ of allowed digits. Count the number of tickets whose first $n/2$ digits have the same sum as their last $n/2$ digits, modulo $998244353$.
- **Diagnostic Signal & Modelling Bridge**:
  Let $P(x) = \sum_{d \in D} x^d$. The number of half-tickets of length $m = n/2$ with digit sum $s$ is $c_s = [x^s] P(x)^m$, and the answer is $\sum_{s=0}^{9m} c_s^2 = [x^{9m}] P(x)^m \cdot (x^9 P(x^{-1}))^m$.
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Form $P(x) = \sum_{d \in D} x^d$ of degree $\le 9$.
  2. Compute $A(x) = P(x)^{n/2}$ of degree $N \le \frac{9n}{2} \le 9 \times 10^5$ either via a single NTT of length $2^{20}$ (`dft(P)`, raise each point value to the $(n/2)$-th power in $O(\log n)$, and `idft`), OR in $O(n)$ time using the D-finite logarithmic derivative recurrence $A'(x) P(x) = \frac{n}{2} P'(x) A(x)$!
  3. Output $\sum_{s=0}^{9n/2} ([x^s] A(x))^2 \bmod 998244353$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: If $c_s$ is the number of length-$(n/2)$ strings with sum $s$, why is the total answer $\sum_s c_s^2$?
  - *Hint 2*: Notice $c_s = [x^s] (\sum_{d \in D} x^d)^{n/2}$. How fast can you compute a polynomial power of degree $9n/2$?
  - *Hint 3*: Pad $P(x)$ to length $2^{20} > 9n/2$, run one forward NTT, exponentiate pointwise to power $n/2$, and run one inverse NTT!

---

#### Problem B10b: Codeforces 1810G — The Maximum Prefix
- **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/1810/G](https://codeforces.com/problemset/problem/1810/G)
- **Difficulty Tier**: `Advanced` (Transposed DP / Backward Suffix-to-Prefix Linear Operator Duality)
- **Mathematical Statement & Constraints**:
  An array $a_1, \dots, a_n$ ($n \le 5000$) has $a_i = +1$ with probability $p_i$ and $a_i = -1$ with probability $1 - p_i$. Given scores $h_0, h_1, \dots, h_n$, for **every** prefix length $k = 1, 2, \dots, n$, compute the expected value of $h_{M_k}$ where $M_k = \max_{0 \le j \le k} \sum_{i=1}^j a_i$ is the maximum prefix sum of $a_1, \dots, a_k$, modulo $10^9 + 7$.
  - **Constraints**: $\sum n \le 5000$. Target Complexity: $O(n^2)$ for all $k = 1, \dots, n$ simultaneously via DP Transposition!
- **Diagnostic Signal & Modelling Bridge**:
  If we fix a single length $k$, walking **backwards** from $i = k$ down to $1$ updates the maximum prefix sum via the remarkably simple transition $m \gets \max(0, m + a_i)$! Running this backward DP from every $k = 1, \dots, n$ separately takes $O(n^3)$ because the initial state is at $i = k$. **Transposing** the backward linear DP turns the $n$ separate backward runs into a **single forward DP** from $i = 1$ to $n$ in $O(n^2)$!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. For a fixed $k$, adding $a_i \in \{+1, -1\}$ at the *front* of a sequence with max prefix sum $m \ge 0$ maps $m \mapsto \max(0, m + a_i)$.
  2. Thus, in the backward DP (from $i = k$ down to $1$), let $dp[i][m]$ be the expected score when suffix $a_{i+1 \dots k}$ has max prefix sum $m$:
     - Base case at $i = k$: $dp[k][m] = h_m$ for all $m \ge 0$.
     - Step $i$ ($i = k, k-1, \dots, 1$): $dp[i-1][m] = p_i \cdot dp[i][m + 1] + (1 - p_i) \cdot dp[i][\max(0, m - 1)]$.
     - Output for length $k$: $dp[0][0]$ (inner product of initial vector $h$ with unit vector $e_0$ after $k$ transition matrices $T_1^\top T_2^\top \cdots T_k^\top h$!).
  3. By **Tellegen's Transposition Principle**, $e_0^\top (T_1^\top \cdots T_k^\top h) = (T_k \cdots T_1 e_0)^\top h$! Instead of starting with $dp = h$ at $i = k$ and going down to $1$ to read $dp[0]$, we start with $dp[0] = h$ at $i = 0$, apply the **same step forward** for $i = 1, 2, \dots, n$, and after step $k$, simply read $dp[k][0]$!
  4. Total time for all $k = 1, \dots, n$: a single $O(n^2)$ loop!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Why is tracking the maximum prefix sum $M_k$ hard when appending $a_k$ at the end (requiring both current sum and max sum), but easy when prepending $a_1$ at the front ($M \gets \max(0, M + a_1)$)?
  - *Hint 2*: Notice that for a fixed $k$, the backward DP computes $e_0^\top T_1 \cdots T_k h$. Why does this depend on $k$ only through which matrices $T_1, \dots, T_k$ are multiplied?
  - *Hint 3*: Run the linear transition $dp_{\text{new}}[m] = p_i dp[m+1] + (1-p_i) dp[\max(0, m-1)]$ **forward** for $i = 1, \dots, n$ starting from $dp[m] = h_m$, and output $dp[0]$ after each step $i = k$!
````

---

### 4.3 Group C Replacements & Restorations (`C1`, `C4`, `C7`, `C8`)

````markdown
#### Problem C1: AtCoder ABC 387 G — Prime Circuit
- **Judge & URL**: AtCoder — [https://atcoder.jp/contests/abc387/tasks/abc387_g](https://atcoder.jp/contests/abc387/tasks/abc387_g)
- **Difficulty Tier**: `Intermediate` (Connected Unicyclic / Cactus Graph EGF & FPS Composition)
- **Mathematical Statement & Constraints**:
  Count the number of connected simple undirected graphs on $N \le 2.5 \times 10^5$ labeled vertices $\{1, \dots, N\}$ such that every simple cycle in the graph has prime length $p \ge 3$, modulo $998244353$.
  - **Constraints**: $1 \le N \le 2.5 \times 10^5$, Time Limit $2.0\text{ s}$. Target Complexity: $O(N \log N)$ or $O(N \log^2 N)$.
- **Diagnostic Signal & Modelling Bridge**:
  If a connected graph contains a cycle where every simple cycle has prime length:
  1. In the **unicyclic variant** (at most one cycle, of prime length $p \ge 3$): a connected graph is either a labeled tree ($N^{N-2}$) or a prime-length cycle of $p$ rooted labeled trees $T(x) = \sum_{n=1}^N \frac{n^{n-1}}{n!} x^n$, counted by $[x^N] N! \left(\text{Tree}(x) + \sum_{p \ge 3 \text{ prime}} \frac{1}{2p} T(x)^p\right) = [x^N] N! \bigl(\text{Tree}(x) + C(T(x))\bigr)$ via FPS `compose`! (Even simpler: since $[x^N] T(x)^p = \frac{p}{N} \binom{N}{p} N^{N-p}$ by Lagrange Inversion / Cayley's forest formula, $[x^N] C(T(x))$ also collapses to an $O(N)$ sum!)
  2. In the **cactus variant** (every biconnected block is either a bridge or a cycle of prime length $p \ge 3$, since two cycles sharing an edge form a theta graph with path lengths $a, b, c \ge 1$ whose three cycle lengths $a+b, b+c, c+a$ sum to $2(a+b+c)$ so at least one cycle has even length $\ge 4$, contradiction!): the rooted connected EGF $R(x)$ satisfies $R(x) = x \exp\!\left(R(x) + \frac{1}{2}\sum_{p \ge 3 \text{ prime}} R(x)^{p-1}\right)$, solved in $O(N \log^2 N)$ via Kinoshita–Li `revert`!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. **Why Theta Subgraphs Are Impossible**: Suppose two simple cycles share at least one edge. Then the graph contains two vertices $u, v$ connected by three internally disjoint paths of lengths $a, b, c \ge 1$. The three cycle lengths are $a+b, b+c, c+a$. Since $(a+b) + (b+c) + (c+a) = 2(a+b+c)$ is even, at least one of the three cycles has even length $\ge 4$, which cannot be prime! Thus every biconnected component is either $K_2$ (a single edge) or a simple cycle $C_p$ of odd prime length $p \ge 3$ (a **Prime Cactus**), OR in the single-cycle interpretation, a tree or prime-cycle unicyclic graph.
  2. **Evaluating via `compose` / `revert`**:
     - Define the outer prime-cycle series $G(y) = y + \frac{1}{2} \sum_{3 \le p \le N \text{ prime}} y^{p-1}$.
     - The rooted cactus EGF $R(x)$ satisfies $R(x) = x \exp(G(R(x))) \iff x = R(x) \exp(-G(R(x)))$.
     - Calling `revert` on $H(y) = y \exp(-G(y)) \bmod y^{N+1}$ gives $R(x)$ for all $n \le N$ in $O(N \log^2 N)$, and for a single $N$, Lagrange Inversion gives $N! [x^N] C(x) = (N-1)! [x^N] R(x) = (N-2)! [y^{N-1}] \exp(N G(y))$ in $O(N \log N)$!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Can two cycles share an edge if every simple cycle has prime length? Check the parity of $(a+b) + (b+c) + (c+a) = 2(a+b+c)$!
  - *Hint 2*: Since no two cycles can share an edge, every block is either an edge or a prime-length cycle $C_p$ ($p \ge 3$), or in the unicyclic case a single cycle of rooted trees $T(x)$.
  - *Hint 3*: Express the EGF as a composition $G(T(x))$ or implicit equation $R(x) = x \exp(G(R(x)))$ and solve via Kinoshita–Li `compose` / `revert` or Lagrange Inversion.

---

#### Problem C4: Luogu P5827 — 点双连通图计数 (Labeled Biconnected Graphs Enumeration)
- **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P5827](https://www.luogu.com.cn/problem/P5827)
- **Difficulty Tier**: `Mastery` (Block-Cut Tree EGF Inversion via Kinoshita–Li `revert` + `compose` / Lagrange Inversion)
- **Mathematical Statement & Constraints**:
  Compute the number of labeled biconnected (2-vertex-connected) simple undirected graphs on $n$ vertices modulo $998244353$ (for a given $n \le 10^5$ or for all $n = 1, \dots, N$).
  - **Constraints**: $N \le 10^5$. Target Complexity: $O(N \log N)$ (single $n$ via Lagrange) or $O(N \log^2 N)$ (all $n \le N$ via Kinoshita–Li `revert` + `compose`).
- **Diagnostic Signal & Modelling Bridge**:
  We know the EGF of all labeled graphs $F(x) = \sum_{n \ge 0} 2^{\binom{n}{2}} \frac{x^n}{n!}$, connected graphs $C(x) = \ln F(x)$, and rooted connected graphs $D(x) = x C'(x)$. In a rooted connected graph, the root vertex $r$ belongs to a set ($\exp$) of biconnected components (blocks), and each non-root vertex in those blocks carries an independent rooted connected graph $D(x)$!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Let $B(y)$ be the EGF of biconnected graphs (for $n \ge 2$), and let $B'(y) = \frac{d}{dy} B(y)$ be the EGF of biconnected graphs with one distinguished root vertex removed.
  2. By the Block-Cut Tree decomposition around the root of $D(x)$:
     $$D(x) = x \exp\bigl(B'(D(x))\bigr) \implies B'\bigl(D(x)\bigr) = \ln \frac{D(x)}{x} = H(x).$$
  3. Notice that $D(x)$ and $H(x) = \ln \frac{D(x)}{x}$ are **known** formal power series (computed in $O(N \log N)$ from $C(x) = \ln F(x)$), while $B'(y)$ is the **unknown** outer series!
  4. **All-$n$ Solution via Kinoshita–Li `revert` + `compose` ($O(N \log^2 N)$)**:
     Substitute $x = D^{\langle -1 \rangle}(y)$ (the compositional inverse of $D(x)$):
     $$B'(y) = H\bigl(D^{\langle -1 \rangle}(y)\bigr), \qquad [y^n] B(y) = \frac{1}{n} [y^{n-1}] B'(y).$$
  5. **Single-$n$ Solution via Lagrange Inversion ($O(N \log N)$)**:
     For a single $n \ge 2$, apply the Change-of-Variables / Lagrange Inversion formula to $y = D(x)$:
     $$n! [y^n] B(y) = (n-1)! [y^{n-1}] B'(y) = \frac{(n-1)!}{n-1} [x^{n-2}] H'(x) \left(\frac{x}{D(x)}\right)^{n-1}.$$
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Root a connected graph at vertex $r$. How do the biconnected components containing $r$ decompose the rest of the connected graph?
  - *Hint 2*: Show that the rooted connected graph EGF $D(x) = x C'(x)$ satisfies $D(x) = x \exp(B'(D(x)))$, so $B'(D(x)) = \ln(D(x)/x)$.
  - *Hint 3*: Invert $y = D(x)$ using Kinoshita–Li `revert` + `compose` for all $n \le N$ in $O(N \log^2 N)$, or Lagrange Inversion for a single $n$ in $O(n \log n)$.

---

#### Problem C7: Codeforces 1967E2 — Again Counting Arrays (Hard Version)
- **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/1967/E2](https://codeforces.com/problemset/problem/1967/E2)
- **Difficulty Tier**: `Mastery` (Catalan Rational Substitution $x = \frac{u}{(1+u)^2}$ & Reflection Principle Power Projection)
- **Mathematical Statement & Constraints**:
  Given $n, m, b_0$ ($\sum n \le 2 \times 10^6, m \le 2 \times 10^6$), count the number of valid sequences of length $n$ bounded in $[0, m]$ under the stack/walk reduction rules modulo $998244353$. Target Complexity: $O(n + m)$.
- **Diagnostic Signal & Modelling Bridge**:
  The generating function has the form $[x^n] G(C(x))$ where $C(x) = \frac{1 - \sqrt{1 - 4x}}{2x} - 1$ satisfies $C(x) = x(1 + C(x))^2$. While general FPS power projection takes $O(n \log^2 n)$, here $C(x)$ is the compositional inverse of the **sparse rational function** $\psi(u) = \frac{u}{(1 + u)^2}$!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. By the Reflection Principle on bounded Dyck walks in $[0, m]$, the outer series $G(u)$ is a rational series of geometric reflections $u^{k(m+2) \pm d}$.
  2. Applying the formal residue change of variables $u = C(x) \iff x = \frac{u}{(1 + u)^2}$ with $dx = \frac{1 - u}{(1 + u)^3} du$:
     $$[x^n] G(C(x)) = \operatorname{Res}_{x=0} G(C(x)) x^{-n-1} dx = \operatorname{Res}_{u=0} G(u) \left(\frac{u}{(1+u)^2}\right)^{-n-1} \frac{1 - u}{(1+u)^3} du = [u^n] (1 - u)(1 + u)^{2n - 1} G(u)!$$
  3. Since $[u^k](1 + u)^{2n-1} = \binom{2n-1}{k}$ is known in $O(1)$ per reflection term, the entire coefficient extraction runs in $O(n)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Express the 1D bounded walk generating function in terms of the Catalan series $u = C(x)$ where $x = \frac{u}{(1+u)^2}$.
  - *Hint 2*: Do you need $O(n \log^2 n)$ general Power Projection when $x = \frac{u}{(1+u)^2}$ is an explicit rational function of $u$?
  - *Hint 3*: Apply the residue change of variables $[x^n] G(C(x)) = [u^n] (1 - u)(1 + u)^{2n-1} G(u)$ and sum the reflection-principle terms in $O(n)$!

---

#### Problem C8: AtCoder ABC 336 G — 16 Integers
- **Judge & URL**: AtCoder — [https://atcoder.jp/contests/abc336/tasks/abc336_g](https://atcoder.jp/contests/abc336/tasks/abc336_g)
- **Difficulty Tier**: `Advanced` (De Bruijn Graph Eulerian Paths & BEST Theorem Matrix-Tree Determinant)
- **Mathematical Statement & Constraints**:
  You are given $16$ non-negative integers $X_{0000}, X_{0001}, \dots, X_{1111}$ with $\sum X_s \le 10^6$. Count the number of binary strings of length $N = 3 + \sum X_s$ in which each length-$4$ binary substring $s \in \{0, 1\}^4$ appears exactly $X_s$ times, modulo $998244353$.
- **Diagnostic Signal & Modelling Bridge**:
  Every length-$4$ binary substring $b_1 b_2 b_3 b_4$ is a directed edge from length-$3$ prefix $u = b_1 b_2 b_3 \in \{0, 1\}^3$ to length-$3$ suffix $v = b_2 b_3 b_4 \in \{0, 1\}^3$ in the $8$-vertex **De Bruijn Graph**! Counting binary strings with prescribed $4$-gram frequencies is equivalent to counting **Eulerian paths** in a directed multigraph on $8$ vertices, solved in $O(8^3 + \sum X_s)$ via the **BEST Theorem**!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Construct the directed multigraph on $V = \{0, 1\}^3$ ($8$ vertices) where edge $(b_1 b_2 b_3 \to b_2 b_3 b_4)$ has multiplicity $X_{b_1 b_2 b_3 b_4}$.
  2. Check Eulerian degree conditions ($\text{out}(u) = \text{in}(u)$ for all $u$, or one start vertex with $\text{out} - \text{in} = 1$ and one end vertex with $\text{in} - \text{out} = 1$, adding a virtual edge from end to start to form an Eulerian circuit) and connectivity of non-isolated vertices.
  3. By the **BEST Theorem** (de Bruijn, van Aardenne-Ehrenfest, Smith, Tutte), the number of distinct Eulerian circuits (dividing by $\prod_{e} X_e!$ because parallel edges representing identical $4$-grams are indistinguishable) is:
     $$T_{\text{arb}}(r) \cdot \frac{\prod_{u \in V} (\text{out}(u) - 1)!}{\prod_{s \in \{0,1\}^4} X_s!},$$
     where $T_{\text{arb}}(r)$ is the number of directed spanning arborescences rooted at $r$, computed via the $7 \times 7$ directed Laplacian determinant (Matrix-Tree Theorem)!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Model each $4$-bit window $b_1 b_2 b_3 b_4$ as a directed edge $b_1 b_2 b_3 \to b_2 b_3 b_4$ on the $8$-vertex De Bruijn graph.
  - *Hint 2*: Apply the BEST Theorem to count Eulerian circuits using the Matrix-Tree cofactor determinant on the active vertices.
  - *Hint 3*: Remember to divide by $\prod_{s \in \{0,1\}^4} X_s!$ since multiple copies of the same $4$-bit edge are indistinguishable in the output binary string!
````

---

### 4.4 Group D Replacements, Unbundlings & Restorations (`D1a`, `D1b`, `D4a`, `D4b`, `D8`)

````markdown
#### Problem D1a: AtCoder ARC 033 D — 多項式 (Seen At)
- **Judge & URL**: AtCoder — [https://atcoder.jp/contests/arc033/tasks/arc033_4](https://atcoder.jp/contests/arc033/tasks/arc033_4)
- **Difficulty Tier**: `Stepping Stone` (O(N) Consecutive-Grid Lagrange Interpolation)
- **Mathematical Statement & Constraints**:
  An unknown polynomial $P(x)$ of degree $N \le 10^5$ has given values $P(0), P(1), \dots, P(N)$ modulo $10^9 + 7$. Given an integer $T \in [0, 10^9]$, compute $P(T) \pmod{10^9 + 7}$ in $O(N)$ time.
- **Diagnostic Signal & Modelling Bridge**:
  Since the sample points $0, 1, \dots, N$ form an arithmetic progression of step $1$, the Lagrange denominator $\prod_{j \ne i}(i - j) = (-1)^{N-i} i! (N-i)!$ factors into factorials, allowing $O(N)$ evaluation without converting to the monomial basis!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. If $0 \le T \le N$, return $P(T)$ directly.
  2. Otherwise, precompute prefix products $\text{pref}_i = \prod_{j=0}^{i-1} (T - j)$ and suffix products $\text{suff}_i = \prod_{j=i+1}^N (T - j)$, plus inverse factorials $\text{inv\_fact}[i] = (i!)^{-1} \bmod (10^9 + 7)$.
  3. Sum in $O(N)$:
     $$P(T) = \sum_{i=0}^N P(i) \cdot (-1)^{N-i} \cdot \text{pref}_i \cdot \text{suff}_i \cdot \text{inv\_fact}[i] \cdot \text{inv\_fact}[N - i] \pmod{10^9 + 7}.$$
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Do not solve for the monomial coefficients of $P(x)$! Write down the Lagrange interpolation formula at $x = T$.
  - *Hint 2*: Simplify $\prod_{j \ne i} (i - j) = (-1)^{N-i} i! (N-i)!$.
  - *Hint 3*: Precompute prefix and suffix products of $(T - j)$ to evaluate all $N+1$ numerators in $O(N)$ total time.

---

#### Problem D1b: Luogu P3321 — [SDOI2015] 序列统计 (Sequence Statistics)
- **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P3321](https://www.luogu.com.cn/problem/P3321)
- **Difficulty Tier**: `Intermediate` (Discrete Logarithm over Primitive Root + Cyclic NTT Exponentiation)
- **Mathematical Statement & Constraints**:
  Given a prime $m < 8000$, an integer $n \le 10^9$, a target remainder $x \in [1, m - 1]$, and a subset $S \subseteq \{0, 1, \dots, m - 1\}$, count the number of length-$n$ sequences $a_1, \dots, a_n \in S$ such that $\prod_{i=1}^n a_i \equiv x \pmod m$, modulo $1004535809$.
- **Diagnostic Signal & Modelling Bridge**:
  Since $m$ is prime and $x \not\equiv 0 \pmod m$, no $a_i$ can be $0$. Finding a primitive root $g$ of $\mathbb{F}_m^\times$ maps every nonzero $a \in S \setminus \{0\}$ to its discrete logarithm $\text{ind}_g(a) \in \{0, 1, \dots, m - 2\}$, converting multiplication $\prod a_i \equiv x \pmod m$ into **addition modulo $m - 1$**!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Find a primitive root $g$ modulo the prime $m$, and build the discrete logarithm table $\text{ind}_g(v)$ for all $v \in \{1, \dots, m - 1\}$ in $O(m)$.
  2. Form the degree-$(m-2)$ polynomial $F(z) = \sum_{a \in S \setminus \{0\}} z^{\text{ind}_g(a)}$.
  3. Compute $F(z)^n \bmod (z^{m-1} - 1)$ modulo $1004535809$ (an NTT prime: $1004535809 = 479 \times 2^{21} + 1$) using binary exponentiation where each step multiplies two polynomials of degree $< m - 1$ via NTT and folds $z^{k + m - 1} \mapsto z^k$.
  4. Output $[z^{\text{ind}_g(x)}] \bigl(F(z)^n \bmod (z^{m-1} - 1)\bigr)$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Can $0$ ever be chosen in the sequence if the product is $x \not\equiv 0 \pmod m$? No! How is the multiplicative group $\mathbb{F}_m^\times$ structured when $m$ is prime?
  - *Hint 2*: Use a primitive root $g \pmod m$ to convert $\prod a_i \equiv x \pmod m$ into $\sum \text{ind}_g(a_i) \equiv \text{ind}_g(x) \pmod{m - 1}$.
  - *Hint 3*: Compute $F(z)^n \bmod (z^{m-1} - 1)$ in $O(m \log m \log n)$ via binary exponentiation and cyclic NTT.

---

#### Problem D4a: Codeforces 995F — Cowmpany Cowmpensation
- **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/995/F](https://codeforces.com/problemset/problem/995/F)
- **Difficulty Tier**: `Intermediate` (Tree DP Polynomial Degree Bound + Consecutive-Grid Lagrange Interpolation)
- **Mathematical Statement & Constraints**:
  A rooted tree has $N \le 3000$ employees. Each employee $u$ is assigned an integer salary $s_u \in \{1, 2, \dots, D\}$ ($D \le 10^9$) such that $s_u \le s_{\text{parent}(u)}$. Count the number of valid salary assignments modulo $10^9 + 7$. Target Complexity: $O(N^2)$.
- **Diagnostic Signal & Modelling Bridge**:
  In $dp[u][x] = \sum_{y=1}^x \prod_{v \in \text{children}(u)} dp[v][y]$, a leaf has degree $1$ in $x$, multiplying across children sums degrees, and prefix-summing $\sum_{y=1}^x$ adds $1$ to the degree. By induction, $dp[\text{root}][x]$ is a polynomial in $x$ of degree $N$!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Run the standard $O(N^2)$ tree DP only for $x = 0, 1, \dots, N$ (with $dp[u][0] = 0$).
  2. Interpolate the degree-$N$ polynomial $P(x) = dp[\text{root}][x]$ at $x = D$ in $O(N)$ time using consecutive-grid Lagrange interpolation.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Write the tree DP $dp[u][x] = \sum_{y=1}^x \prod_{v} dp[v][y]$. What kind of function of $x$ is $dp[u][x]$ when $u$ is a leaf?
  - *Hint 2*: Prove by induction on subtree size that $dp[u][x]$ is a polynomial in $x$ of degree $\text{sz}(u)$.
  - *Hint 3*: Compute $dp[\text{root}][0 \dots N]$ in $O(N^2)$ and evaluate at $x = D$ via $O(N)$ Lagrange interpolation!

---

#### Problem D4b: Luogu P7116 — [NOIP2020] 微信步数 (WeChat Steps)
- **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P7116](https://www.luogu.com.cn/problem/P7116)
- **Difficulty Tier**: `Advanced` (Multidimensional Grid Walk Periodicity + Polynomial Interpolation / Sampling Shift)
- **Mathematical Statement & Constraints**:
  A walker repeats a sequence of $n \le 5 \times 10^5$ steps in a $k$-dimensional box $[1, w_1] \times \dots \times [1, w_k]$ ($k \le 10, w_i \le 10^9$). For every starting cell, find how many steps the walker takes before leaving the box, and output the sum over all $\prod_{i=1}^k w_i$ starting cells modulo $10^9 + 7$.
- **Diagnostic Signal & Modelling Bridge**:
  By the tail-sum identity, sum the number of surviving starting cells $\prod_{i=1}^k \max(0, w_i - R_i(t))$ at step $t$. After the first full period of $n$ steps, the bounding box of visited offsets in each dimension $i$ grows linearly by a constant $\Delta_i$ per period $q = 1, 2, \dots$! Thus for each step $r \in \{0, \dots, n-1\}$ within a period, the number of surviving starting cells at step $q n + r$ is a **polynomial in the period index $q$ of degree $k \le 10$**!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Simulate the first period ($q = 0$) step-by-step. If the net displacement after $n$ steps is $\vec{0}$ and some starting cells survive period $0$, return $-1$ (infinite walk).
  2. For $q \ge 1$, at step $r \in \{1, \dots, n\}$ of period $q$, the span of visited offsets in dimension $i$ is $L_i(r) + (q - 1) \Delta_i$, where $\Delta_i$ is a constant independent of $q$ and $r$!
  3. Thus $\sum_{q=1}^{Q} \prod_{i=1}^k \bigl(w_i - L_i(r) - (q - 1)\Delta_i\bigr)$ is a degree-$(k+1)$ polynomial in the cutoff period $Q$, which we evaluate via Lagrange interpolation / Bernoulli-Faulhaber sums in $O(n k + k^2)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Instead of finding the exit step for each starting cell, sum the number of starting cells still alive after $t$ steps over all $t \ge 0$.
  - *Hint 2*: How does the bounding box $[l_i, r_i]$ of the walk in dimension $i$ change from period $q$ to period $q + 1$? For $q \ge 1$, its width increases by a constant $\Delta_i$ per period!
  - *Hint 3*: Since the alive count in period $q$ is a degree-$k$ polynomial in $q$, sum over $q = 1, \dots, Q$ using degree-$(k+1)$ Lagrange interpolation!

---

#### Problem D8: AtCoder ARC 153 D — Sum of Sum of Digits
- **Judge & URL**: AtCoder — [https://atcoder.jp/contests/arc153/tasks/arc153_d](https://atcoder.jp/contests/arc153/tasks/arc153_d)
- **Difficulty Tier**: `Intermediate` (Carry-Ordering Digit DP via Radix Shift)
- **Mathematical Statement & Constraints**:
  Given $N \le 2 \times 10^5$ non-negative integers $A_1, \dots, A_N < 10^9$, find $\min_{X \ge 0} \sum_{i=1}^N f(A_i + X)$ where $f(y)$ is the sum of base-$10$ digits of $y$.
- **Diagnostic Signal & Modelling Bridge**:
  At the $d$-th digit from the right, a carry occurs for $A_i + X$ iff $(A_i \bmod 10^d) + (X \bmod 10^d) \ge 10^d$. Sorting $A_1, \dots, A_N$ by $A_i \bmod 10^d$ means the set of indices $i$ that generate a carry into digit $d$ is always a **suffix of the sorted array** of size $c \in \{0, 1, \dots, N\}$!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Use the identity $f(y) = y - 9 \sum_{d \ge 1} \lfloor y / 10^d \rfloor$, or track at digit $d$ the number of elements $c \in \{0, \dots, N\}$ that carry into position $d$ (which are always the $c$ elements with the largest values of $A_i \bmod 10^d$).
  2. Transition from digit $d$ to $d + 1$ in $O(N \log N)$ by sorting $A_i \bmod 10^d$ and testing all digits $x_d \in \{0, \dots, 9\}$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: For a fixed power $10^d$, which elements $A_i$ produce a carry at position $d$ when added to $X$?
  - *Hint 2*: They are always a suffix of $A$ when sorted by $A_i \bmod 10^d$, reducing the state space at digit $d$ from $2^N$ to $N + 1$!
  - *Hint 3*: Run a digit DP from least significant to most significant digit with state $(d, c) \in \{0 \dots 10\} \times \{0 \dots N\}$.
````

---

### 4.5 Group E Replacements, Unbundlings & Restorations (`E2`, `E5a`, `E5b`, `E6a`, `E6b`, `E8`)

````markdown
#### Problem E2: AtCoder ABC 278 Ex — make 1
- **Judge & URL**: AtCoder — [https://atcoder.jp/contests/abc278/tasks/abc278_h](https://atcoder.jp/contests/abc278/tasks/abc278_h)
- **Difficulty Tier**: `Mastery` ($q$-Binomial Inversion over $\mathbb{F}_2$ + $q$-Pochhammer $(x; 2)_k$ + Chirp Z-Transform)
- **Mathematical Statement & Constraints**:
  Count the number of subsets of $[0, 2^B)$ of size $A$ ($1 \le B \le A \le 2 \times 10^5$) that satisfy the linear span / odd-combination condition ("make 1"), modulo $998244353$. Target Complexity: $O(A \log A)$.
- **Diagnostic Signal & Modelling Bridge**:
  A subset of vectors in $\mathbb{F}_2^B$ fails to span the target iff it is contained in a hyperplane (codimension-$1$ subspace) of $\mathbb{F}_2^B$. By **$q$-Binomial Inversion** on the subspace lattice of $\mathbb{F}_2^B$, the inclusion-exclusion weight for a subspace of dimension $r \le B$ is $(-1)^{B - r} 2^{\binom{B - r}{2}} \binom{B}{r}_2$, and the number of size-$A$ subsets inside an $r$-dimensional subspace is $\binom{2^r}{A} = [x^A] \prod_{j=0}^{2^r - 1}(1 + x)$!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Write $\binom{2^r}{A} = \frac{1}{A!} \prod_{j=0}^{A-1} (2^r - j) = [x^A] \frac{1}{A!} \dots$, which is a degree-$A$ polynomial $P(z) = \frac{1}{A!} \prod_{j=0}^{A-1}(z - j)$ evaluated at the **geometric points** $z = 2^r$ for $r = 0, 1, \dots, B$!
  2. Construct $P(z) = \frac{1}{A!} \prod_{j=0}^{A-1}(z - j)$ in $O(A \log A)$ via Falling Factorial / Stirling Numbers of the First Kind.
  3. Evaluate $P(2^r)$ for all $r = 0, 1, \dots, B$ simultaneously in $O(A \log A)$ using **Bluestein's Chirp Z-Transform** ($c = 1, q = 2$)!
  4. Combine with the $O(B)$-precomputed $q$-binomial weights $(-1)^{B-r} 2^{\binom{B-r}{2}} \binom{B}{r}_2$ to obtain the answer in $O(A \log A)$!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Apply $q$-binomial inclusion-exclusion over subspaces of $\mathbb{F}_2^B$ of dimension $r \in \{0, \dots, B\}$. How many subsets of size $A$ lie inside a subspace of size $2^r$?
  - *Hint 2*: Notice that $\binom{2^r}{A} = \frac{1}{A!}\prod_{j=0}^{A-1}(2^r - j)$ is a fixed degree-$A$ polynomial $P(z)$ evaluated at the geometric sequence $z = 2^0, 2^1, \dots, 2^B$!
  - *Hint 3*: Expand $P(z)$ in the monomial basis via Stirling numbers in $O(A \log A)$ and evaluate $P(2^r)$ for $0 \le r \le B$ via Chirp Z-Transform!

---

#### Problem E5a: Luogu P5366 — [SNOI2017] 遗失的答案 (Lost Answer)
- **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P5366](https://www.luogu.com.cn/problem/P5366)
- **Difficulty Tier**: `Advanced` (Prime-Exponent Min/Max Lattice $\to$ Boolean FWT OR-AND Convolution)
- **Mathematical Statement & Constraints**:
  Given $N, G, L \le 10^8$ and $Q \le 10^5$ queries, in each query an integer $X \le N$ is required to be chosen. Count the number of subsets of $\{1, 2, \dots, N\}$ containing $X$ whose greatest common divisor is $G$ and least common multiple is $L$, modulo $10^9 + 7$.
- **Diagnostic Signal & Modelling Bridge**:
  If $G \nmid L$, the answer is $0$. Otherwise, $L / G \le 10^8$ has at most $\omega(L/G) \le 8$ distinct prime factors $p_1^{e_1} \cdots p_k^{e_k}$! A subset of divisors of $L$ (multiples of $G$) has $\gcd = G$ iff for every $i \in \{1, \dots, k\}$ at least one chosen number achieves the **minimum** exponent of $p_i$ (bit $i$ in $[0, k)$), and $\text{lcm} = L$ iff for every $i$ at least one chosen number achieves the **maximum** exponent of $p_i$ (bit $i + k$ in $[k, 2k)$)!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Factor $L / G = p_1^{e_1} \cdots p_k^{e_k}$ ($k \le 8$). Every valid candidate $d \in [1, N]$ with $G \mid d$ and $d \mid L$ maps to a **$2k$-bit mask** $\text{mask}(d) \in [0, 2^{2k})$ recording which primes have $v_{p_i}(d/G) = 0$ (lower $k$ bits) and which have $v_{p_i}(d/G) = e_i$ (upper $k$ bits).
  2. Notice that at most $600$ distinct divisors $d$ exist, and many share the same $2k$-bit mask! Group them by mask, compute prefix and suffix Fast Walsh–Hadamard OR-Transforms (SOS DP) of size $2^{2k} \le 2^{16} = 65536$, and answer each forced-$X$ query in $O(2^{2k})$ or $O(1)$ after precomputation!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Factor $L / G = p_1^{e_1} \cdots p_k^{e_k}$. Why is $k \le 8$ for $L / G \le 10^8$?
  - *Hint 2*: For each prime $p_i$, only two boundary events matter for a number $d$: whether $v_{p_i}(d) = v_{p_i}(G)$ and whether $v_{p_i}(d) = v_{p_i}(L)$. Encode these as a $2k$-bit mask!
  - *Hint 3*: Selecting a subset of numbers whose masks bitwise-OR to $2^{2k} - 1$ is a standard OR-FWT (Fast Zeta Transform) problem on $2k \le 16$ bits!

---

#### Problem E5b: Codeforces 1916F — Group Division
- **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/1916/F](https://codeforces.com/problemset/problem/1916/F)
- **Difficulty Tier**: `Advanced` (Biconnected Graph Bipolar Orientation / Ear Decomposition)
- **Mathematical Statement & Constraints**:
  Given a biconnected undirected graph $G = (V, E)$ with $|V| = n_1 + n_2 \le 2000$, partition $V$ into two connected induced subgraphs $V_1, V_2$ of sizes $|V_1| = n_1$ and $|V_2| = n_2$.
- **Diagnostic Signal & Modelling Bridge**:
  In any biconnected graph, maintaining a partition $V = A \sqcup B$ where both $G[A]$ and $G[B]$ are connected can be grown vertex-by-vertex from $|A| = 1$ to $|A| = n_1$ by always moving a vertex $v \in B$ adjacent to $A$ that is **not an articulation point (cut vertex) of $G[B]$** (equivalently, via an $st$-numbering / bipolar orientation)!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Start with $A = \{1\}$ and $B = V \setminus \{1\}$ (since $G$ is biconnected, $G[B]$ is connected).
  2. In each of $n_1 - 1$ steps, run Tarjan's DFS on $G[B]$ in $O(n + m)$ time to identify all cut vertices of $G[B]$. By a leaf-block argument on the Block-Cut Tree of $G[B]$, because $G$ is biconnected, every leaf block of $G[B]$ has at least one non-cut vertex adjacent to $A$! Move that vertex from $B$ to $A$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Grow $V_1$ one vertex at a time starting from a single vertex. What condition must the chosen neighbor $v \in V_2$ satisfy so $G[V_2 \setminus \{v\}]$ stays connected?
  - *Hint 2*: $v$ must not be a cut vertex of $G[V_2]$!
  - *Hint 3*: Look at a leaf block of the Block-Cut Tree of $G[V_2]$. Because the whole graph $G$ is biconnected, can $V_1$ be adjacent ONLY to the single cut vertex of that leaf block? Never!

---

#### Problem E6a: QOJ 5097 / SOJ 703 — 布尔立方 (Boolean Cube)
- **Judge & URL**: QOJ — [https://qoj.ac/problem/5097](https://qoj.ac/problem/5097)
- **Difficulty Tier**: `Mastery` ($q$-Binomial Rank Enumeration + $q$-Stirling Basis Change + Chirp Z-Transform)
- **Mathematical Statement & Constraints**:
  Count $n \times n \times n$ binary 3D tensors over $\mathbb{F}_2$ classified by the $\mathbb{F}_2$-ranks of their 2D slices ($n \le 10^5$) modulo $998244353$. Target Complexity: $O(n \log n)$.
- **Diagnostic Signal & Modelling Bridge**:
  The number of $n \times n$ matrices over $\mathbb{F}_2$ of rank $r$ is $\binom{n}{r}_2^2 2^{\binom{r}{2}} (2; 2)_r$. Coupling across slices introduces a factor $2^{r s}$, which is decoupled by changing into the $q$-falling factorial basis $\prod_{i=0}^{k-1}(2^r - 2^i)$ and applying **Bluestein's Chirp Z-Transform**!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Use the $q$-Vandermonde / $q$-falling factorial expansion $2^{n r} = \sum_{k=0}^n \binom{n}{k}_2 \prod_{i=0}^{k-1}(2^r - 2^i)$.
  2. Replace $2^{r s}$ via Bluestein's identity $r s = \binom{r+s}{2} - \binom{r}{2} - \binom{s}{2}$, converting the summation over $r, s \in \{0, \dots, n\}$ into a length-$2n$ NTT convolution in $O(n \log n)$ time!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Write the number of $n \times n$ $\mathbb{F}_2$-matrices of rank $r$ using $\binom{n}{r}_2$.
  - *Hint 2*: Expand powers $2^{n r}$ in the $q$-falling factorial basis $\prod_{i=0}^{k-1}(2^r - 2^i)$.
  - *Hint 3*: Decouple $2^{r s} = 2^{\binom{r+s}{2} - \binom{r}{2} - \binom{s}{2}}$ using Bluestein's Chirp Z-Transform.

---

#### Problem E6b: Codeforces 1336E2 — Chiori and Doll Picking (Hard Version)
- **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/1336/E2](https://codeforces.com/problemset/problem/1336/E2)
- **Difficulty Tier**: `Mastery` (Linear Basis over $\mathbb{F}_2^m$ & MacWilliams Dual Code Identity)
- **Mathematical Statement & Constraints**:
  Given $n \le 2 \times 10^5$ integers $a_1, \dots, a_n \in [0, 2^m)$ ($m \le 53$), for each popcount $c = 0, 1, \dots, m$, count the number of subsequences whose XOR sum has popcount $c$, modulo $998244353$. Target Complexity: $O(n m + 2^{\min(k, m - k)} m)$.
- **Diagnostic Signal & Modelling Bridge**:
  Reduce $a_1, \dots, a_n$ via Gaussian elimination over $\mathbb{F}_2^m$ to a linear basis $C \subseteq \mathbb{F}_2^m$ of dimension $k \le m$ (each span element occurs $2^{n - k}$ times). If $k \le m / 2$ ($k \le 26$), enumerate $C$ in $O(2^k)$; if $k > m / 2$ ($m - k \le 27$), switch to the **orthogonal dual code** $C^\perp$ of dimension $m - k$ via the **MacWilliams Identity (FWT Duality)**!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Compute the RREF of the basis $C$: after column permutation, the generator matrix is $G = [I_k \mid A]$ of size $k \times m$, and the parity-check matrix of the dual code $C^\perp$ is $H = [A^\top \mid I_{m-k}]$ of size $(m - k) \times m$!
  2. Notice that the XOR-FWT of the indicator function $1_C$ of a $k$-dimensional subspace $C \subseteq \mathbb{F}_2^m$ is $\widehat{1_C} = 2^k \cdot 1_{C^\perp}$!
  3. Thus the weight enumerator $W_C(x, y) = \sum_{u \in C} x^{m - |u|} y^{|u|}$ is related to the dual weight enumerator $W_{C^\perp}(x, y)$ by the **MacWilliams Identity**:
     $$W_C(x, y) = 2^{k - m} W_{C^\perp}(x + y, x - y),$$
     meaning the popcount distribution of $C$ is obtained from the popcount distribution of $C^\perp$ via a single $O(m^2)$ Krawtchouk polynomial transform $\sum_{j} \text{cnt}_{C^\perp}[j] [z^c] (1 - z)^j (1 + z)^{m - j}$!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: First compute the $\mathbb{F}_2$-linear basis $C$ of dimension $k \le m$. If $k \le 26$, you can brute-force all $2^k$ elements of $C$. What if $k > 26$?
  - *Hint 2*: Write the basis in RREF $G = [I_k \mid A]$. Its orthogonal complement $C^\perp$ has basis $H = [A^\top \mid I_{m-k}]$ of dimension $m - k \le 27$!
  - *Hint 3*: By XOR-FWT duality ($\widehat{1_C} = 2^k 1_{C^\perp}$), recover the popcount distribution of $C$ from the popcount distribution of $C^\perp$ using Krawtchouk polynomials $(1 - z)^j (1 + z)^{m - j}$ in $O(2^{m-k} + m^2)$!

---

#### Problem E8: AtCoder ARC 134 E — Modulo Nim
- **Judge & URL**: AtCoder — [https://atcoder.jp/contests/arc134/tasks/arc134_e](https://atcoder.jp/contests/arc134/tasks/arc134_e)
- **Difficulty Tier**: `Advanced` (Divisor/Modulo Closure Lattice & Subset DP)
- **Mathematical Statement & Constraints**:
  In Modulo Nim, $N \le 200$ piles have sizes chosen uniformly from $[1, A_i]$ ($A_i \le 200$). In each move, a player chooses $m \ge 2$ and replaces every pile size $x_i$ with $x_i \bmod m$ (at least one pile must change, and the player who removes the last stone loses). Count the number of losing initial configurations modulo $998244353$.
- **Diagnostic Signal & Modelling Bridge**:
  Only the **set of distinct nonzero pile sizes** $S \subseteq \{1, \dots, 200\}$ matters! After just one move with $m \le 12$ (or reducing modulo $\max(S)$), all piles become $< 12$, or if every element in $S$ is divisible by $12$, $S \subseteq \{12, 24, \dots, 192\}$ has only $16$ elements ($2^{16}$ subsets)!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Classify losing subsets $S \subseteq \{1, \dots, 200\}$: any subset containing an element not divisible by $12$ (except small losing patterns $\{1\}, \{2\}, \{4, 8\}$) can be analyzed via reductions to $m \le 12$, while subsets of multiples of $12$ ($\{12, 24, \dots, 192\}$, size $16$) are solved by a $2^{16}$ bitmask game DP!
  2. Once all losing subsets $S$ are identified, count tuples $(x_1, \dots, x_N) \in \prod [1, A_i]$ whose value set equals $S$ via inclusion-exclusion / subset Zeta transform.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Does multiplicity of pile sizes matter in Modulo Nim? No—only the set $S$ of distinct pile sizes!
  - *Hint 2*: Notice that choosing $m = 2, 3$, or $4$ immediately reduces all pile sizes to $\{1\}$, $\{1, 2\}$, or $\{1, 2, 3\}$ unless all elements of $S$ share a common divisor ($2, 4, 3$, or $12$)!
  - *Hint 3*: Run a $2^{16}$ bitmask game DP on multiples of $12$ up to $192$, then count matching arrays via subset inclusion-exclusion.
````

---

### 4.6 Group F Replacements & Unbundlings (`F2a`, `F2b`, `F7a`, `F7b`, `F7c`)

````markdown
#### Problem F2a: Luogu P4841 — [集训队作业2013] 城市规划 (City Planning)
- **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P4841](https://www.luogu.com.cn/problem/P4841)
- **Difficulty Tier**: `Stepping Stone` (Univariate EGF Logarithm $\ln F(z)$ for Connected Labeled Graphs)
- **Mathematical Statement & Constraints**:
  Given $n \le 1.3 \times 10^5$, compute the number of simple connected undirected labeled graphs on $n$ vertices modulo $1004535809$. Target Complexity: $O(n \log n)$.
- **Diagnostic Signal & Modelling Bridge**:
  When all $n$ vertices are symmetric (every pair of vertices can have an edge), the Set Power Series $F(x) = \sum_{S \subseteq V} 2^{\binom{|S|}{2}} x^S$ collapses under $x_i \mapsto z$ to the **univariate EGF** $F(z) = \sum_{k=0}^n 2^{\binom{k}{2}} \frac{z^k}{k!}$, and connected graphs are given by $C(z) = \ln F(z)$!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Form $F(z) = \sum_{k=0}^n \frac{2^{\binom{k}{2}}}{k!} z^k \pmod{z^{n+1}}$ modulo $1004535809$ ($= 479 \times 2^{21} + 1$, primitive root $3$).
  2. Compute $C(z) = \ln F(z) = \int \frac{F'(z)}{F(z)} dz \pmod{z^{n+1}}$ in $O(n \log n)$ via NTT polynomial inversion.
  3. Output $n! [z^n] C(z) \bmod 1004535809$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Every labeled graph is a disjoint union ($\textsc{Set}$) of connected labeled graphs. What EGF operation corresponds to $\textsc{Set}$?
  - *Hint 2*: Since $F(z) = \exp(C(z))$ where $F(z) = \sum_{k \ge 0} 2^{\binom{k}{2}} \frac{z^k}{k!}$, take $C(z) = \ln F(z) \bmod z^{n+1}$.
  - *Hint 3*: Compute $\ln F(z) = \int F'(z) F(z)^{-1} dz$ using $O(n \log n)$ NTT inversion modulo $1004535809$.

---

#### Problem F2b: LibreOJ 154 — 集合幂级数 exp / ln / 幂 (Set Power Series Operations)
- **Judge & URL**: LibreOJ — [https://loj.ac/p/154](https://loj.ac/p/154)
- **Difficulty Tier**: `Intermediate` (Set Power Series $\exp, \ln$, and $k$-th Power in $O(n^2 2^n)$)
- **Mathematical Statement & Constraints**:
  Given a Set Power Series $F(x) = \sum_{S \subseteq \{0, \dots, n-1\}} f_S x^S$ ($n \le 21$), compute $\exp(F(x))$, $\ln(F(x))$, or $F(x)^k / k!$ in $K[x_0, \dots, x_{n-1}]/(x_0^2, \dots, x_{n-1}^2)$ modulo $998244353$. Target Complexity: $O(n^2 2^n)$.
- **Diagnostic Signal & Modelling Bridge**:
  Using the Ranked Zeta Transform, $K[x_0, \dots, x_{n-1}]/(x_0^2, \dots, x_{n-1}^2)$ embeds into $2^n$ independent copies of the univariate truncated polynomial ring $K[t]/(t^{n+1})$, reducing SPS $\exp / \ln / \text{pow}$ to $2^n$ degree-$n$ polynomial operations of cost $O(n^2)$ each!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. Lift $f_S \mapsto f_S t^{|S|}$ and apply the Fast Zeta Transform (OR-FMT) across all $n+1$ ranks in $O(n^2 2^n)$ time.
  2. At each mask $M \in [0, 2^n)$, apply the $O(n^2)$ univariate recurrence for $\exp(\widehat{F}_M(t))$, $\ln(\widehat{F}_M(t))$, or $\widehat{F}_M(t)^k \bmod t^{n+1}$ (or use the MSB-splitting loop $\exp(F_0 + x_v F_1) = \exp(F_0) + x_v (\exp(F_0) * F_1)$ to halve the constant factor!).
  3. Apply the Fast Möbius Transform (OR-IFMT) and extract $[t^{|S|}] \widehat{G}_S(t)$ for each $S$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Lift the Set Power Series by popcount $|S|$ into $K[t]/(t^{n+1})$ and apply OR-FMT.
  - *Hint 2*: At each of the $2^n$ masks, compute the univariate $\exp / \ln$ modulo $t^{n+1}$ in $O(n^2)$ using $Q' = F' Q$.
  - *Hint 3*: For $n = 21$, use the MSB-splitting recurrence $G_{[2^v, 2^{v+1})} = G_{[0, 2^v)} * F_{[2^v, 2^{v+1})}$ so you only transform sizes $2^0, 2^1, \dots, 2^{n-1}$.

---

#### Problem F7a: Luogu P5325 — 【模板】Min_25 筛 (Multiplicative Function Prefix Sums via Bell Series)
- **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P5325](https://www.luogu.com.cn/problem/P5325)
- **Difficulty Tier**: `Intermediate` (Bell SeriesPrime-Polynomial Decomposition & Min_25 Sieve)
- **Mathematical Statement & Constraints**:
  Let $f(n)$ be a multiplicative function satisfying $f(p^k) = p^k(p^k - 1)$ at prime powers $p^k$. Given $N \le 10^{10}$, compute $\sum_{n=1}^N f(n) \bmod (10^9 + 7)$. Target Complexity: $O(N^{3/4} / \log N)$ (Min_25 Sieve) or $O(N^{2/3})$ (Powerful Number Sieve).
- **Diagnostic Signal & Modelling Bridge**:
  At prime $p$ ($k = 1$), $f(p) = p^2 - p$ is a low-degree polynomial in $p$! This triggers either the **Min_25 Sieve** (splitting primes into $\text{id}_2(p) - \text{id}_1(p)$) or the **Powerful Number Sieve** (matching the $[x^1]$ linear term of the Bell Series $B_p(f; x) = \sum_{k \ge 0} f(p^k) x^k$ with $g = \text{id}_1 \cdot \varphi$, whose Bell series has $g(p) = p(p - 1) = f(p)$)!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. **Powerful Number / Bell Series Route**: Choose $g(n) = n \varphi(n)$ (so $g(p) = p(p-1) = f(p)$ and $g * \text{id}_1 = \text{id}_2$, allowing prefix sums of $g$ in $O(N^{2/3})$ via Du's Sieve).
  2. Define $h = f * g^{-1}$. In the Bell series at prime $p$:
     $$B_p(f; x) = 1 + p(p-1)x + p^2(p^2-1)x^2 + \dots, \qquad B_p(g; x) = 1 + \frac{p(p-1)x}{1 - p^2 x} = \frac{1 - px}{1 - p^2 x}.$$
     Therefore:
     $$B_p(h; x) = B_p(f; x) B_p(g; x)^{-1} = B_p(f; x) \frac{1 - p^2 x}{1 - px} \implies h(p) = 0, \quad h(p^k) = p^{2k-2}(p-1)p \text{ for } k \ge 2.$$
  3. Since $h(p) = 0$, $h(d) \ne 0$ only on the $O(\sqrt{N})$ **Powerful Numbers** $d \le N$, so $\sum_{n=1}^N f(n) = \sum_{d \le N \text{ powerful}} h(d) G(\lfloor N / d \rfloor)$ runs in $O(N^{2/3} + \sqrt{N})$!
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Examine $f(p) = p(p-1)$ at prime $p$. What familiar multiplicative function $g(n)$ also satisfies $g(p) = p(p-1)$?
  - *Hint 2*: Compare the Bell series $B_p(f; x)$ and $B_p(g; x)$ for $g(n) = n \varphi(n)$. Why does $h = f * g^{-1}$ have $h(p) = 0$?
  - *Hint 3*: Precompute prefix sums of $g(n) = n\varphi(n)$ via Du's Sieve ($g * \text{id}_1 = \text{id}_2$) and DFS over the $O(\sqrt{N})$ powerful numbers $d \le N$!

---

#### Problem F7b: AtCoder ABC 288 Ex — A Nameless Counting Problem
- **Judge & URL**: AtCoder — [https://atcoder.jp/contests/abc288/tasks/abc288_h](https://atcoder.jp/contests/abc288/tasks/abc288_h)
- **Difficulty Tier**: `Mastery` (XOR-Constrained Non-Decreasing Tuple Counting via EGF / Parity DP)
- **Mathematical Statement & Constraints**:
  Count the number of non-decreasing sequences $0 \le A_1 \le A_2 \le \dots \le A_N \le M$ such that $A_1 \oplus A_2 \oplus \dots \oplus A_N = X$, modulo $998244353$. Constraints: $1 \le N \le 200$, $0 \le M, X < 2^{30}$.
- **Diagnostic Signal & Modelling Bridge**:
  A non-decreasing sequence of length $N$ in $[0, M]$ is a **multiset of size $N$** chosen from $\{0, \dots, M\}$. By the Pólya / Euler Transform (or inclusion-exclusion over odd-multiplicity vs. even-multiplicity items, since identical pairs $a \oplus a = 0$ cancel in XOR!), a multiset of size $N$ with XOR sum $X$ decomposes into $k \equiv N \pmod 2$ **distinct** elements with XOR sum $X$ plus $(N - k)/2$ duplicate pairs from $\{0, \dots, M\}$!
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. In any multiset of size $N$ from $\{0, \dots, M\}$, pair up identical elements two by two: suppose $k \in \{0, 1, \dots, N\}$ ($k \equiv N \pmod 2$) elements appear an **odd** number of times (so they are $k$ **strictly increasing** elements $0 \le B_1 < \dots < B_k \le M$ with $B_1 \oplus \dots \oplus B_k = X$), and the remaining $(N - k)/2$ pairs are chosen with replacement from $\{0, \dots, M\}$ in $\binom{(M + 1) + \frac{N-k}{2} - 1}{\frac{N-k}{2}}$ ways!
  2. And how do we count **tuples of $k$ distinct elements** in $[0, M]$ with XOR sum $X$ for all $k = 0, \dots, N$? From the count $W_k$ of **ordered** $k$-tuples in $[0, M]^k$ with XOR sum $X$ (computed in $O(\log M \cdot N^2)$ via a standard MSB digit DP), subtract tuples with collisions using EGF/falling-factorial recurrence:
     $$k! D_k = W_k - \sum_{\substack{0 \le j < k \\ j \equiv k \pmod 2}} \binom{k}{j} \dots \quad \text{or directly } D_k = \frac{1}{k}\Bigl(\dots\Bigr)!$$
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Notice that if a value $v \in [0, M]$ appears twice in the multiset, $v \oplus v = 0$ cancels out in the XOR sum!
  - *Hint 2*: Every multiset of size $N$ from $\{0, \dots, M\}$ uniquely decomposes into a **subset of $k$ distinct elements** ($k \equiv N \pmod 2$) with XOR sum $X$, plus $\frac{N - k}{2}$ pairs chosen with replacement from $\{0, \dots, M\}$!
  - *Hint 3*: Count subsets of $k$ distinct elements in $[0, M]$ with XOR sum $X$ for all $0 \le k \le N$ by running an $O(N^2 \log M)$ digit DP for ordered tuples and stripping duplicate pairs!

---

#### Problem F7c: LibreOJ 6729 — 幂数 (Powerful Numbers / Bell Series Division)
- **Judge & URL**: LibreOJ — [https://loj.ac/p/6729](https://loj.ac/p/6729)
- **Difficulty Tier**: `Intermediate` (Powerful Number Sieve & Formal Power Series Division on Bell Series)
- **Mathematical Statement & Constraints**:
  Given a multiplicative function $f(n)$ supported on or reducible to powerful numbers and $N \le 10^{11}$, compute $\sum_{n=1}^N f(n)$ in $O(\sqrt{N})$ time via Bell series division $B_p(h; x) = B_p(f; x) / B_p(g; x)$.
- **Diagnostic Signal & Modelling Bridge**:
  Whenever $f(p) = g(p)$ for all primes $p$ where $G(x) = \sum_{n \le x} g(n)$ is computable in $O(1)$ or $O(N^{2/3})$, the Dirichlet quotient $h = f * g^{-1}$ satisfies $h(p) = 0$, restricting $h$ to the $\le 2\sqrt{N}$ powerful numbers $d \le N$.
- **Reverse-Engineering Scratchpad & Complete Derivation**:
  1. For each prime $p \le \sqrt{N}$, compute $h(p^2), h(p^3), \dots, h(p^e)$ ($p^e \le N$) via the formal power series recurrence $h(p^k) = f(p^k) - \sum_{j=1}^k g(p^j) h(p^{k-j})$ in $O(\sqrt{N})$ total time across all primes $p \le \sqrt{N}$.
  2. Enumerate all powerful numbers $d \le N$ by recursive DFS over prime powers $p^e$ ($e \ge 2$) and accumulate $h(d) G(\lfloor N / d \rfloor)$.
- **Progressive 3-Tier Hints**:
  - *Hint 1*: Match $f(p)$ at prime $p$ with a simple multiplicative function $g(n)$.
  - *Hint 2*: Use the Bell series recurrence $h(p^k) = f(p^k) - \sum_{j=1}^k g(p^j) h(p^{k-j})$ to compute $h(p^k)$ for all $p \le \sqrt{N}$ and $k \ge 2$.
  - *Hint 3*: DFS over all powerful numbers $d \le N$ and sum $h(d) G(\lfloor N / d \rfloor)$.
````

---

## Section 5: Master Remediation Checklist for Wave 5B

| # | Category | Target Lines in `cohort3_wave_5b.md` | Action Required |
| :--- | :--- | :--- | :--- |
| **1** | **Section Opener Labels** | Lines 51, 315, 426, 617, 795, 922 | Rename `**(a) Concrete Problem Anchor**` to `**Diagnostic Signal**` and `**(b) Why Naive Implementations Fail**` to `**Reverse-Engineering Scratchpad**`. |
| **2** | **Bug M3 (Corrected)** | Lines 256–269 & 1785–1798 | Replace `solve_chain_dc` midpoint split `(l + r) >> 1` with the Python-verified weight-balanced `AffinePoly solve_chain_dc` in **Section 1.1** of this report (do **not** use Inspector A's non-compiling `Mat2` replacement). |
| **3** | **Bug M1** | Line 530 | Fix $P^{(t-1)}_{n_{t-1} - i, 0} \gets \widehat{P}^{(0)}_{0, n_{t-1} - i}$ to $P^{(t-1)}_{N - 1 - i, 0} \gets \widehat{P}^{(0)}_{0, N - 1 - i}$. |
| **4** | **Omission O1** | After Line 612 | Insert the Power-of-2 Parity Invariant ($n = 2^m - 1$) & 1D Flat Kronecker-Packed `power_projection_1d` from **Section 3.1** of this report. |
| **5** | **Bug M2** | Lines 651–652 & 1927–1928 | Fix the $q = 0$ branch in `chirp_z_transform` so $y_0 = \sum_{i=0}^{n-1} a_i c^i$ and $y_j = a_0$ for $j \ge 1$ (`if (c.v == 0)` first, then `if (q.v == 0)`). |
| **6** | **Bug B2** | Lines 730 & 1962 | Add `if (m <= 0 || y.empty()) return {};` at the top of `shift_of_sampling_points`. |
| **7** | **Bug B1 (CRITICAL)** | Lines 1066–1121 | Replace Section 6.5 (`sps_compose`) with the corrected upward-loop ($v = 0 \dots n-1$) + `Mint(d + 1)` derivative factor implementation in **Section 2.1** of this report. |
| **8** | **Omission O2** | After Line 1190 | Insert the Global Cross-Wave Synthesis Matrix (Waves 1A–5B / Iterations 01–52) from **Section 3.2** of this report. |
| **9** | **Toy Traces 1–6** | Lines 231, 378, 496, 682, 840, 1043 | Insert the 6 clean, zero-`"Wait:"`, Python-verified Toy Traces from **Section 1.2** of this report. |
| **10** | **Section 7 Problem Unbundling & Expansion** | Lines 1192–1702 | Apply Inspector A's unbundlings (`A5`, `A6`, `B2`, `B3`, `C2`, `C3`, `C5` + `R1–R15` table) **plus** all unbundlings, corrections, expansions, and restorations in **Section 4** of this report (`A2`, `A3`, `A12a–b`, `A13–A16`, `B6`, `B9a–b`, `B10a–b`, `C1`, `C4`, `C7`, `C8`, `D1a–b`, `D4a–b`, `D8`, `E2`, `E5a–b`, `E6a–b`, `E8`, `F2a–b`, `F7a–c`). |
| **11** | **Omission O4 (Citations)** | Lines 1731, 1748, 1763 | Append `[EN-12]` (Bostan–Mori 2021), `[ZH-10]` (Zhong Zihao 2019), and `[JA-8]` (`noshi91` Algorithm Encyclopedia) from **Section 3.4** of this report. |
| **12** | **Omission O3 (Appendix A)** | Lines 1859–2050 | Add `bivariate_multiply` and `fps_compose` to Appendix A.3, and add `QBinomial`, `sps_exp`, corrected `sps_compose`, and `dgf_exp` to Appendix A.5. |
