# Part VI Audit Report — Critic C: Algorithm Contracts, Failure Modes, Code Limits & Quarto Syntax

- **Auditor**: Part VI Critic C (`fps-textbook-critic` — Algorithm Contracts, Failure Modes, Code Limits & Quarto Syntax)
- **Target Files Audited**:
  1. [`chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd) (1,298 lines)
  2. [`chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd) (1,208 lines)
  3. [`chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd) (1,332 lines)
  4. [`checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd) (912 lines)
- **Reference Standards**: `AGENTS.md` (§Code Policy, §Algorithm Contracts, §Mandatory Failure Modes, §Quarto Syntax Hygiene) & `fps_research/CURRICULUM_ARCHITECTURE.md` (§2.3, §2.4).

---

## Executive Summary & Audit Scorecard

| Audit Dimension | Ch 22 | Ch 23 | Ch 24 | CP-VI | Overall Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1. 5-Part Algorithm Contracts (`AGENTS.md` L11–16)** | ❌ Missing §22.1 contract; 11/11 existing contracts omit Part 5 (`Failure Modes & Edge Cases`) | ❌ 12/12 existing contracts omit Part 5 (`Failure Modes & Edge Cases`) | ❌ Missing all 4 core engine contracts (§24.1–§24.4); 8/8 ladder contracts omit Part 5 | ❌ 8/8 checkpoint solution contracts omit Part 5 (`Failure Modes & Edge Cases`) | **Action Required (44 contracts)** |
| **2. Mandatory Failure Mode Callouts (`#9`, `#10`, `IFWT-XOR` $p \neq 2$)** | ✅ FM #10 callout at L376–385 + midpoint warning at L219–229 | ✅ FM #9 callout at L227–232 | ✅ `IFWT-XOR` $p \neq 2$ & zero-factor callout at L132–137 | ✅ Covered in solution contracts | **Pass** |
| **3. Code Block Length ($\le 15$ lines) & Standard Library Ban (`AGENTS.md` L9–10)** | ✅ 4/4 `cpp` blocks $\le 13$ lines, all non-standard kernels | ✅ 2/2 `cpp` blocks $\le 14$ lines, all non-standard kernels | ⚠️ 13/13 `cpp` blocks $\le 15$ lines, but L68–78 (`fwt`) & L558–567 (SOS loop) are standard templates | ❌ L758–763 has an **untagged** code block (`lang=''`) containing a 4-line standard SOS loop | **Action Required (3 blocks)** |
| **4. Quarto Math & Display Hygiene (`!$$` Factorial Collisions, `\(` / `\[`, `\|` in Tables)** | ❌ Unescaped `\|S\|` inside `$...$` in Markdown table at L571; truncated words at L90, L213 | ❌ **4 critical `!$$` spurious factorial collisions** inside display math (L438, L1025, L1037, L1144); broken Theorem refs | ❌ **`!\n\n$$` collision** at L161–163; unescaped `\|` inside `\mathbin{\|}` in table at L466; raw `>` quote at L5 | ✅ 0 math/table collisions; Stage 1 is 100% spoiler-free | **Action Required (8 critical fixes)** |
| **5. Collapsible `<details>` & `:::` Callout Hygiene** | ✅ 32/32 `<details>` & 11/11 `:::` valid with blank lines | ❌ **32/32 `<details>` blocks lack mandatory blank line before `</details>`**; meta-footnote at L1196–1202 | ✅ 32/32 `<details>` & 15/15 `:::` valid with blank lines | ✅ 32/32 `<details>` & 1/1 `:::` valid with blank lines | **Action Required (Ch 23 `<details>` & checklist)** |

---

## Audit Dimension 1: 5-Part Algorithm Contracts (`AGENTS.md` L11–16)

Per `AGENTS.md` L11–16:
> *"Every core engine and worked problem must present an explicit **Algorithm Contract** box covering 5 mandatory parts: (1) **Input & Exact Index Boundaries**, (2) **Postconditions (Output)**, (3) **Time & Space Complexity**, (4) **Loop / Algebraic Invariant**, and (5) **Failure Modes & Edge Cases** (e.g., modulus constraints $p > N$, valuation conditions $[x^0]F = 1$ or $\neq 0$, zero-divisor tracking, or degree overflow)."*

### 1.1 Systemic Omission Across All 4 Files
Across all 39 existing `Algorithm Contract` blocks in `Ch 22` (11 blocks), `Ch 23` (12 blocks), `Ch 24` (8 blocks), and `CP-VI` (8 blocks), **100% of them split `Input` and `Preconditions` into two separate bullets to reach 5 bullets and completely omit the 5th mandatory part: `Failure Modes & Edge Cases`**.

Furthermore:
- **Chapter 22 (§22.1)** is missing its core engine `Algorithm Contract` box after **Theorem 22.1 (The $O(NK)$ Tree Knapsack Complexity Bound)** (around L81).
- **Chapter 24 (§24.1, §24.2, §24.3, §24.4)** is missing **all four** core engine `Algorithm Contract` callout boxes in the main text (relying only on a summary table in §24.5 at L464–471).

---

### 1.2 Chapter 22 Contract Fixes (`ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd`)

#### Fix 22-C1: Add Missing Core Engine Algorithm Contract in §22.1 (after L81)
Insert immediately after L81 (`Summing over all $\binom{N}{2}$ unordered pairs of vertices yields at most $\binom{N}{2}$ scalar multiplications in total. $\blacksquare$`):

```markdown
::: {.callout-note}
## Algorithm Contract: Truncated Subtree Knapsack Convolution ($O(NK)$ / $O(N^2)$)

- **Input & Exact Index Boundaries**: Rooted tree $T = (V, E)$ with $N = |V| \ge 1$ vertices; truncation bound $K \in [1, N]$; initial degree-$\le 1$ polynomial $f_u(x)$ at each vertex $u \in V$.
- **Preconditions**: Commutative coefficient ring $R$ (or tropical semiring $(\mathbb{Z} \cup \{\pm\infty\}, \min/\max, +)$); child loop at $u$ must bound loop upper limits by `min(sz[u], K)` and `min(sz[v], K)` **before** incrementing `sz[u] += sz[v]`.
- **Postconditions (Output)**: At every vertex $u \in V$, $f_u(x) \bmod x^{K+1}$ equals the exact subtree convolution over $T_u$ up to degree $\min(\text{sz}[u], K)$.
- **Time & Space Complexity**: $O(N \min(N, K)) = O(NK)$ arithmetic operations (and $O(N^2)$ when $K = N$) with $O(N \min(N, K))$ space.
- **Loop / Algebraic Invariant**: After merging the first $r$ children $v_1, \dots, v_r$ of $u$, $\text{sz}[u] = 1 + \sum_{j=1}^r \text{sz}[v_j]$ and $\deg f_u \le \min(\text{sz}[u], K)$, so each elementary multiplication corresponds to a unique pair $(a, b) \in V(T_u^{\text{cur}}) \times V(T_{v_{r+1}})$ with $\operatorname{LCA}(a, b) = u$.
- **Failure Modes & Edge Cases**:
  1. **Premature Size Update (`sz[u] += sz[v]` before the inner loop)** or looping up to $K$ without clipping to `sz[u]` and `sz[v]` destroys the LCA pair-counting bijection and degrades complexity from $O(NK)$ to $O(N K^2)$.
  2. **In-Place Overwrite**: Updating `f_u[i + j]` in place without either a temporary buffer `nxt` or descending index order corrupts higher coefficients within the same child merge.
:::
```

#### Fix 22-C2: Add `Failure Modes & Edge Cases` to All 11 Existing Contracts in Ch 22
Append the following `- **Failure Modes & Edge Cases**:` bullet to each existing contract in `ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd`:

1. **§22.2 HLD Chain D&C Contract (L336–344, after L343)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Using index midpoint $\lfloor(l+r)/2\rfloor$ instead of prefix degree-weight midpoint $\ge W/2$ degrades skewed heavy chains to $O(N^2)$ (Failure Mode: Unbalanced `Compress`); prime modulus $p$ must satisfy $p \equiv 1 \pmod{2^{\lceil\log_2(2N)\rceil}}$ for NTT.
   ```
2. **§22.3 Zero-Divisor Pair $(a, c)$ Contract (L447–455, after L454)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Calling raw `inv(val)` when $x \equiv 0 \pmod p$ causes division-by-zero or corrupts $0 \mapsto 0$ into a silent bug (Failure Mode #10); during addition $(a_1, c_1) + (a_2, c_2)$ with $c_1 = c_2$, if $a_1 + a_2 \equiv 0 \pmod p$, the result drops out of the unit group and is only valid when additions occur after all tree-DP divisions.
   ```
3. **§22.4 Static Top Tree (`Rake` / `Compress`) Contract (L549–557, after L556)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Mixing up endpoint ordering $(t, b)$ during non-commutative `Compress(L, R)` corrupts boundary state transitions; for $d \times d$ matrix states, performing $d^3$ inverse NTTs instead of point-value accumulation adds a $d\times$ overhead.
   ```
4. **Practice Ladder `SS-1` (`#012` AtCoder ABC 267 Ex, L655–662, after L661)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Evaluating $[x^M]$ when $M > \sum_{i=1}^N A_i$ must return $0$ before out-of-bounds array indexing; multiplying in linear left-to-right order instead of a priority-queue / D&C tree degrades to $O(N \cdot (\sum A_i))$.
   ```
5. **Practice Ladder `SS-2` (`#106` CF 1251F, L736–743, after L742)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Only white stones with $c_i < r_j$ are valid for red stone $r_j$; querying perimeter $Q_q$ that is odd or satisfies $k = Q_q/2 - r_j - 1 < 0$ or $k > c_1 + 2c_2$ must immediately output $0$.
   ```
6. **Practice Ladder `Int-1` (`#025` AtCoder ABC 247 Ex, L806–813, after L812)**:
   ```markdown
   - **Failure Modes & Edge Cases**: By parity of cycle decomposition ($N - c \equiv K \pmod 2$), only indices $c \in [1, N]$ with $N - c \le K$ and $(N - c) \equiv K \pmod 2$ contribute to the sum; when $c_v = 1$, $\prod_{j=0}^{c_v-1}(x+j) = x$ has degree $1$.
   ```
7. **Practice Ladder `Int-2` (`#246` Library Checker Tree Path Composite Sum, L899–906, after L905)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Because affine composition $f_e(x) = b_e x + c_e$ is non-commutative, `Compress(L, R)` must carefully distinguish upward paths ($L \circ R$) from downward paths ($R \circ L$); single-vertex paths $(u, u)$ contribute $a_u$ once at the base step.
   ```
8. **Practice Ladder `Adv-1` (`#067` AtCoder ARC 145 E, L998–1005, after L1004)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Wait-free backward basis alignment must process indices $i = N$ down to $1$; if at step $i$ the discrepancy $A_i \oplus B_i$ lies outside the span of the prefix linear basis of $A_1, \dots, A_i$, immediately output `No`.
   ```
9. **Practice Ladder `Adv-2` (`#255` UOJ 347, L1075–1082, after L1081)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Because each independent-set parity state is a $2 \times 2$ matrix of polynomials over $(x, y)$, `Compress` must respect top-down order $(t, b)$ along the heavy chain while `Rake` is commutative across light subtrees.
   ```
10. **Practice Ladder `Mas-1` (`#163` Luogu P4719 Dynamic DP, L1185–1192, after L1191)**:
    ```markdown
    - **Failure Modes & Edge Cases**: In tropical $(\max, +)$ algebra there is no additive inverse, so light-child updates at `top[u]` must modify the concrete scalar `g[p][0]` and `g[p][1]` by subtracting the old chain root value and adding the new one; in $M_u \otimes M_v$, the parent $u$ must be on the left and child $v$ on the right.
    ```
11. **Practice Ladder `Mas-2` (`#171` Luogu P5331 SNOI2019, L1270–1277, after L1276)**:
    ```markdown
    - **Failure Modes & Edge Cases**: Deduping sorted $a_k$ coordinates in $[L, M]$ is essential so the auxiliary network per D&C node has $\le r - l + 1$ vertices; directed edge order must strictly enforce $j < i$ by only linking left-half stations $j \in [L, M]$ to right-half stations $i \in [M+1, R]$.
    ```

---

### 1.3 Chapter 23 Contract Fixes (`ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd`)

Append the following `- **Failure Modes & Edge Cases**:` bullet to all 12 Algorithm Contracts in `ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd`:

1. **§23.1 Gaussian Binomials & Grassmannian Inversion (L174–181, after L180)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Out-of-range queries ($k < 0$ or $k > n$) must return $0$; when $q = 1 \pmod P$, the formula $(1 - q^m)/(1 - q)$ divides by zero (`0/0`) and must fall back to classical $\binom{n}{k} \bmod P$ (Failure Mode #9).
   ```
2. **§23.2 $q$-Lucas & Root-of-Unity Evaluation (L249–256, after L255)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Applying standard multiplicative inverse to $1 - q^i$ when $d = \operatorname{ord}_P(q) \mid i$ causes fatal division by zero (Failure Mode #9); if $r_0 > m_0$ in the $q$-Lucas remainder step, $\begin{bmatrix} m_0 \\ r_0 \end{bmatrix}_q = 0$ immediately zeroes the entire product.
   ```
3. **§23.3 Pentagonal & Durfee Square Partition Engine (L369–376, after L375)**:
   ```markdown
   - **Failure Modes & Edge Cases**: In place-value loops, generalized pentagonal exponents $g_k = k(3k-1)/2$ and $g_{-k} = k(3k+1)/2$ must both be checked against $\le N$ separately (since $g_k \le N$ can hold while $g_{-k} > N$); signs follow $(-1)^k$, repeating in pairs $+, +, -, -, +, +$.
   ```
4. **§23.4 MacWilliams Duality Engine (L451–458, after L457)**:
   ```markdown
   - **Failure Modes & Edge Cases**: When row-reducing $G$ over $\mathbb{F}_q$ to systematic form $[I_r \mid P]$, column permutations must be tracked if exact coordinate weights matter (for total Hamming weight enumerators $W_{\mathcal{C}}(x, y)$, column permutations preserve weight); requires $\gcd(q, P) = 1$ so $|\mathcal{C}|^{-1} = q^{-r} \bmod P$ exists.
   ```
5. **Practice Ladder `SS-1` (`#107` CF 1278F, L549–555, after L554)**:
   ```markdown
   - **Failure Modes & Edge Cases**: When $m = 1$, $p = 1/1 \equiv 1 \pmod P$ is valid and needs no special branch, whereas $m \equiv 0 \pmod{998244353}$ has no modular inverse; when $j > n$, the falling factorial $n^{\underline{j}} = 0$ automatically truncates the sum at $\min(n, k)$.
   ```
6. **Practice Ladder `SS-2` (`#132` CF 1916F, L634–640, after L639)**:
   ```markdown
   - **Failure Modes & Edge Cases**: During the $O(n_1^3)$ inner DP or Grassmannian subspace enumeration, disconnected components or zero-divisors when $2^k \equiv 1 \pmod P$ must be guarded; ensure $[x^0]$ base cases initialize the single-root seed before expanding cuts.
   ```
7. **Practice Ladder `Int-1` (`#113` CF 1423G, L709–715, after L714)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Splitting active runs in the `std::set` must update both the value-specific `std::set` and the two global Fenwick trees for $(r - l + 1)$ and $\binom{r - l + 1}{2}$ before inserting the new interval; window size $k = 1$ or $k = N$ must not underflow $L - k + 1$.
   ```
8. **Practice Ladder `Int-2` (`#124` CF 1603F, L808–814, after L813)**:
   ```markdown
   - **Failure Modes & Edge Cases**: When $x = 0$, the subset size condition is trivially violated for $n \ge 1$ (since $0$ lies in the empty span), so output $2^{nk}$ if $n = 0$ and wait: for $x = 0$, no sequence can avoid having a non-empty subset XOR to $0$ when $n > k$, and for $n \le k$ the answer is $\prod_{i=0}^{n-1}(2^k - 2^i)$; when $2^m \equiv 1 \pmod{998244353}$, $m < 998244352$ holds since $\operatorname{ord}_P(2) = 998244352 > 10^7$.
   ```
9. **Practice Ladder `Adv-1` (`#016` AtCoder ABC 235 Ex, L908–914, after L913)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Multiple edges with the same weight $w_i$ must be grouped into a single Kruskal batch so all components merging at threshold $w_i$ transition simultaneously; truncate each tree knapsack convolution to $\min(\text{sz}[u], K)$ to maintain $O(NK)$ total work.
   ```
10. **Practice Ladder `Adv-2` (`#046` AtCoder AGC 054 E, L986–992, after L991)**:
    ```markdown
    - **Failure Modes & Edge Cases**: Small $N \le 3$ boundary cases ($N = 1, 2, 3$) and $A = 1$ or $A = N$ where binomial upper indices become negative must return $0$ cleanly via a guarded `C(n, k)` helper (`if (k < 0 || k > n) return 0`).
    ```
11. **Practice Ladder `Mas-1` (`#034` AtCoder ABC 278 Ex, L1105–1111, after L1110)**:
    ```markdown
    - **Failure Modes & Edge Cases**: Directly evaluating $\begin{bmatrix} n \\ k \end{bmatrix}_{\zeta_d}$ via factorial tables fails with $0/0$ whenever $d \mid (N + M)$ (Failure Mode #9); the $q$-Lucas split $\binom{\lfloor n/d \rfloor}{\lfloor k/d \rfloor} \begin{bmatrix} n \bmod d \\ k \bmod d \end{bmatrix}_{\zeta_d}$ is mandatory.
    ```
12. **Practice Ladder `Mas-2` (`#109` CF 1336E2, L1186–1192, after L1191)**:
    ```markdown
    - **Failure Modes & Edge Cases**: If $\dim \mathcal{C} = r$ satisfies $m - r < r$ ($r \ge 27$), running DFS on $\mathcal{C}$ instead of the orthogonal code $\mathcal{C}^\perp = \ker G$ TLEs ($2^{53}$ vs $2^{26}$); the $n - r$ free redundant elements contribute an overall multiplier of $2^{n - r} \bmod 998244353$.
    ```

---

### 1.4 Chapter 24 Contract Fixes (`ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd`)

#### Fix 24-C1: Add 4 Missing Core Engine Algorithm Contracts in §24.1, §24.2, §24.3, and §24.4

1. **Insert at the end of §24.1 (after L137)**:
   ```markdown
   ::: {.callout-note}
   ## Algorithm Contract: Bitwise FWT / FZT & Small-Support XOR Eigenvalue Trick

   - **Input & Exact Index Boundaries**: Bit-width $n \ge 0$ ($N = 2^n$ masks indexed $0 \dots 2^n - 1$); arrays $A, B$ of length $2^n$ over commutative ring $R$ (or $M$ sparse tuples for the eigenvalue trick).
   - **Preconditions**: For OR/AND FZT and IFMT, any commutative ring $R$ suffices; for `IFWT-XOR`, $2 \in R^\times$ must be invertible ($\operatorname{char}(R) \neq 2$). For the small-support XOR eigenvalue trick, the forward frequency FWT must be computed over exact 64-bit integers (`int64_t`), not modulo $p$.
   - **Postconditions (Output)**: Exact bitwise OR, AND, or XOR convolution $C_k = \sum_{i \diamond j = k} A_i B_j$ for all $k \in [0, 2^n - 1]$.
   - **Time & Space Complexity**: $O(n 2^n)$ time and $O(2^n)$ in-place space (or $O(M + k 2^k + n 2^n)$ for $k$-sparse factors).
   - **Loop / Algebraic Invariant**: After processing bit stages $0, 1, \dots, b - 1$, each block of size $2^b$ holds the $b$-dimensional character evaluation along the lowest $b$ bits while higher bits $b \dots n - 1$ remain in the time domain.
   - **Failure Modes & Edge Cases**:
     1. **Characteristic-2 Collapse**: Dividing by $2^n$ in `IFWT-XOR` fails when $2$ is not a unit in $R$ (e.g., $\mathbb{F}_2$ or $\mathbb{Z}/2^64\mathbb{Z}$ without extra precision bits).
     2. **Modular Reduction of Frequency Counts**: Reducing $\widehat{C}_S$ modulo $p$ before solving the linear system for multiplicity counts $c_r(S)$ corrupts the integer exponents used in $\prod_r \lambda_r^{c_r(S)} \bmod p$.
     3. **Zero Point-Value Factors**: When evaluating ratios or dynamic updates in the FWT domain, frequencies with $\widehat{A}_S \equiv 0 \pmod p$ cannot be divided out naively and require $(a, c)$ zero-divisor tracking (Ch 22 §22.3).
   :::
   ```

2. **Insert at the end of §24.2 (after L192)**:
   ```markdown
   ::: {.callout-note}
   ## Algorithm Contract: Ranked Fast Zeta Transform (Disjoint Subset Convolution)

   - **Input & Exact Index Boundaries**: Bit-width $n \le 20$; Set Power Series $F(\mathbf{x}), G(\mathbf{x}) \in \mathcal{R}_n = R[x_1, \dots, x_n]/(x_1^2, \dots, x_n^2)$ represented as arrays of length $2^n$.
   - **Preconditions**: Any commutative ring $R$ (no division required).
   - **Postconditions (Output)**: Disjoint subset convolution $H_S = \sum_{T \subseteq S} F_T G_{S \setminus T}$ for all $S \in [0, 2^n - 1]$.
   - **Time & Space Complexity**: $O(n^2 2^n)$ time and $O(n 2^n)$ space.
   - **Loop / Algebraic Invariant**: At each mask $S$ and rank $r \in [0, n]$, after forward FZT $\widehat{H}^{(r)}_S = \sum_{i=0}^r \widehat{F}^{(i)}_S \widehat{G}^{(r-i)}_S$ aggregates all pairs $(A, B)$ with $A \cup B \subseteq S$ and $|A| + |B| = r$; applying IFMT and extracting $r = |S|$ isolates $A \cap B = \varnothing$ and $A \cup B = S$.
   - **Failure Modes & Edge Cases**: Forgetting to filter the output by the diagonal rank $r = \operatorname{popcount}(S)$ includes overlapping subsets where $A \cap B \neq \varnothing$; for $n \ge 21$, storing $(n+1) 2^n$ words side-by-side may exceed memory limits unless evaluated blockwise or in-place.
   :::
   ```

3. **Insert at the end of §24.3 (after L379)**:
   ```markdown
   ::: {.callout-note}
   ## Algorithm Contract: Set Power Series Transcendental Engine ($\ln, \exp, \Phi(F)$ & Pointed Biconnected $\ln$)

   - **Input & Exact Index Boundaries**: Bit-width $n \le 21$; Set Power Series $F(\mathbf{x}) \in \mathcal{R}_n$ of length $2^n$, and truncated scalar power series $\Phi(t) = \sum_{j=0}^n \phi_j t^j / j!$ for general composition.
   - **Preconditions**: Commutative ring $R$ where $1, 2, \dots, n \in R^\times$ are invertible ($\operatorname{char}(R) = 0$ or $p > n$). For $\ln F$: $[x^\varnothing] F = 1$; for $\exp F$: $[x^\varnothing] F = 0$.
   - **Postconditions (Output)**: Exact Set Power Series $\ln F(\mathbf{x})$, $\exp F(\mathbf{x})$, $\Phi(F(\mathbf{x}))$, or biconnected graph enumerator $B(\mathbf{x}) \in \mathcal{R}_n$.
   - **Time & Space Complexity**: $O(n^2 2^n)$ time and $O(n 2^n)$ space ($O(n^3 2^n)$ time for the $n$-round pointed vertex-deletion biconnected engine).
   - **Loop / Algebraic Invariant**: Under the MSB split $F = F^{[0]} + x_k F^{[1]}$ at stage $k \in [0, n-1]$, nilpotency $x_k^2 = 0$ linearizes every smooth functional equation into $\Phi(F^{[0]} + x_k F^{[1]}) = \Phi(F^{[0]}) + x_k \Phi'(F^{[0]}) *_{\text{sub}} F^{[1]}$.
   - **Failure Modes & Edge Cases**:
     1. **Non-Zero Constant Term in $\exp$ / Non-Unit in $\ln$**: Calling $\exp F$ when $F_\varnothing \neq 0$ or $\ln F$ when $F_\varnothing \neq 1$ violates nilpotency of the positive-degree ideal $\mathfrak{m} = (x_1, \dots, x_n)$.
     2. **Double-Counting in Naive Ranked ODE**: Performing separate FZT/IFMT transforms inside each rank step of the ODE loop degrades $O(n^2 2^n)$ to $O(n^3 2^n)$; the pointwise rank-series ODE must stay inside the transformed FZT domain across all ranks $r = 1 \dots n$.
   :::
   ```

4. **Insert at the end of §24.4 (after L460)**:
   ```markdown
   ::: {.callout-note}
   ## Algorithm Contract: Dirichlet Generating Function Engine ($*_{\text{Dir}}, A^{-1}, \ln_D, \exp_D$)

   - **Input & Exact Index Boundaries**: Upper index bound $N \ge 1$; arithmetic sequence $a_1, a_2, \dots, a_N \in R$ representing $A(s) = \sum_{n=1}^N a_n n^{-s}$.
   - **Preconditions**:
     - For $*_{\text{Dir}}$ and $A^{-1}$: $a_1 \in R^\times$ must be invertible (no characteristic bound on $R$).
     - For $\ln_D A$ and $\exp_D A$: $1, 2, \dots, \lfloor\log_2 N\rfloor \in R^\times$ must be invertible ($p > \lfloor\log_2 N\rfloor$); $\ln_D A$ requires $a_1 = 1$, and $\exp_D A$ requires $a_1 = 0$.
   - **Postconditions (Output)**: Exact Dirichlet coefficients $c_1, \dots, c_N$ of $A *_{\text{Dir}} B$, $A^{-1}$, $\ln_D A$, or $\exp_D A$.
   - **Time & Space Complexity**: $O(N \log N)$ time via harmonic divisor loops (or $O(N \log \log N)$ when factoring along primes $p$) and $O(N)$ space.
   - **Loop / Algebraic Invariant**: The totally additive prime-omega derivation $\partial_\Omega(n^{-s}) = \Omega(n) n^{-s}$ satisfies $\Omega(d \cdot m) = \Omega(d) + \Omega(m)$, reducing $B = \exp_D A$ to $\Omega(n) b_n = \sum_{d \mid n, d > 1} \Omega(d) a_d b_{n/d}$ for all $n \ge 2$.
   - **Failure Modes & Edge Cases**:
     1. **Using $\ln n$ Instead of $\Omega(n)$**: The real derivative $-a_n \ln n$ does not exist in $\mathbb{F}_p$; replacing it with $\Omega(n)$ (or $\operatorname{spf}(n)$ variations) is mandatory over finite fields.
     2. **Small Characteristic $p \le \lfloor\log_2 N\rfloor$**: When $p \mid \Omega(n)$ for some $n \le N$ (e.g., $n = 2^p \le N$), dividing by $\Omega(n) \bmod p$ fails with division by zero.
   :::
   ```

#### Fix 24-C2: Add `Failure Modes & Edge Cases` to All 8 Practice Ladder Contracts in Ch 24
Append the following `- **Failure Modes & Edge Cases**:` bullet to each Practice Ladder contract in `ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd`:

1. **`SS-1` (`#104` CF 1208F, L570–577, after L576)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Merging identical array indices when lifting $m \oplus 2^b$ into $m$ corrupts the second-largest index $s_m$ ($a_j \text{ and } a_k$ must be strictly distinct indices $i < j < k$); only update the answer once $s_0 \ge 2$ (at least two elements exist to the right of $i$).
   ```
2. **`SS-2` (`#020` AtCoder ABC 213 G, L670–677, after L676)**:
   ```markdown
   - **Failure Modes & Edge Cases**: In the pointed submask recurrence $C_S = F_S - \sum_{1 \in T \subsetneq S} C_T F_{S \setminus T}$, iterating over all submasks $T \subsetneq S$ without pinning the anchor vertex $1 \in T$ overcounts by $|T|$ and fails in characteristic $p \mid |T|$.
   ```
3. **`Int-1` (`#027` AtCoder ABC 253 Ex, L785–792, after L791)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Parallel edges between the same pair $(u, v)$ are distinct labeled edges and must be summed in the adjacency/Laplacian count $c_{u,v}$; when $m = 0$, $m^{-k} \bmod p$ is undefined (prevented here by $m \ge 1$).
   ```
4. **`Int-2` (`#173` Luogu P5363 SDOI2019, L874–881, after L880)**:
   ```markdown
   - **Failure Modes & Edge Cases**: When $n < m$, no valid board configuration exists and the answer is $0$; bit-DP transitions must ensure the total subtracted coins never exceed $n - m$.
   ```
5. **`Adv-1` (`#100` CF 1034E, L978–985, after L984)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Because the target modulus is $4 = 2^2$ (non-prime, characteristic $2$), standard modular arithmetic fails; the $4^{|S|}$ rank shift requires a full 64-bit `uint64_t` integer (`2 * popcount(S)` bits up to $2 \times 21 = 42 < 64$) so intermediate products do not overflow before shifting right by `2 * popcount(S)`.
   ```
6. **`Adv-2` (`#101` CF 1119H, L1095–1102, after L1101)**:
   ```markdown
   - **Failure Modes & Edge Cases**: The 3 frequency arrays $\widehat{C}^{(1)}, \widehat{C}^{(2)}, \widehat{C}^{(3)}$ must be transformed over `int64_t` **without** modulo $998244353$ so that $c_r(S) \in [0, n]$ are exact integer exponents; remember to XOR all $c_i$ into a baseline shift $X_{\text{base}} = \bigoplus c_i$ or keep the 4-eigenvalue system symmetric.
   ```
7. **`Mas-1` (`#245` Library Checker Exp of Set Power Series, L1200–1207, after L1206)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Requires $B_\varnothing = 0$; at MSB stage $k$, the slice $B^{[1]}$ has size $2^k$ (not $2^n$), and each recursive call must reuse a pre-allocated $(k+1) \times 2^k$ rank buffer to fit comfortably within memory and cache limits for $n = 20$.
   ```
8. **`Mas-2` (`#274` QOJ 5089 Biconnected Graph Counting, L1304–1311, after L1310)**:
   ```markdown
   - **Failure Modes & Edge Cases**: At round $v$, masks $S \subseteq V \setminus \{v\}$ must be re-indexed into a contiguous $2^{n-1}$-element SPS before calling $\ln$; after round $v$ completes, only coefficients $H_S$ with $v \in S$ and $|S \setminus \{v\}| \ge 2$ receive the $+1$ vertex-block adjustment (single edges $|S| = 2$ are already biconnected and need no cut-vertex subtraction).
   ```

---

### 1.5 Blind Checkpoint VI Contract Fixes (`checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd`)

Append the following `- **Failure Modes & Edge Cases**:` bullet to all 8 solution contracts in `checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd`:

1. **`CP-VI.1` (`#102` CF 1097G, L576–583, after L582)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Updating `sz[u] += sz[v]` before the inner knapsack loop degrades $O(nk)$ to $O(nk^2)$; forgetting to subtract the upward overcount $x P_v(x) = Q_v(x) - P_v(x)$ at every non-root vertex $v \ne 1$ includes invalid edges lying above $\operatorname{LCA}(X)$.
   ```
2. **`CP-VI.2` (`#121` CF 1553I, L630–637, after L636)**:
   ```markdown
   - **Failure Modes & Edge Cases**: If any base block of target length $s$ is truncated by the end of the array ($i + s - 1 > n$) or contains an element $a_r \ne s$, immediately output $0$; base blocks of length $s_j = 1$ have only $1$ internal orientation, whereas merging $\ge 2$ blocks of length $1$ upgrades the macro-block orientation weight from $1$ to $2$.
   ```
3. **`CP-VI.3` (`#117` CF 1510H, L681–688, after L687)**:
   ```markdown
   - **Failure Modes & Edge Cases**: When interval $u$ claims one of the $j \ge 1$ segments inside $[L_u, R_u]$, if it claims a segment touching $L_u$ ($b_L = 1$) or $R_u$ ($b_R = 1$), that boundary flag must reset to $0$ so no ancestor of $u$ can fuse with $u$'s already-claimed interval across $L_u$ or $R_u$.
   ```
4. **`CP-VI.4` (`#170` Luogu P5327, L728–735, after L734)**:
   ```markdown
   - **Failure Modes & Edge Cases**: At $w_i = \operatorname{LCA}(s_i, t_i)$, endpoints $\{s_i, t_i\}$ are inserted twice (once at $s_i$ and once at $t_i$), so they must be decremented **twice** at $\operatorname{parent}(w_i)$ (not once at $w_i$ and once at $\operatorname{parent}(w_i)$, since path $P_i$ still covers $w_i$ itself!); when a leaf's multiplicity `cnt` drops to $0$, `L_v`, `R_v`, and `val` must reset to $0$.
   ```
   *(Note also the mathematical detail in `CP-VI.4` L262 and L716–717: since path $P_i = (s_i, t_i)$ **does** cover $w_i = \operatorname{LCA}(s_i, t_i)$, both $+1$ insertions at $s_i$ and $t_i$ must remain active at $w_i$ and both $-1$ removals must occur at $\operatorname{parent}(w_i)$! If one removal is placed at $w_i$, the multiplicity at $w_i$ is still $2 - 1 = 1 > 0$, which happens to work for a single path, so that's why $-1$ at $w_i$ and $-1$ at $\operatorname{parent}(w_i)$ also works! Mentioning `cnt == 0` leaf reset in `Failure Modes & Edge Cases` is key.)*
5. **`CP-VI.5` (`#054` AtCoder ARC 106 E, L766–773, after L772)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Recomputing the daily working masks $M_1, \dots, M_D$ from scratch inside every binary search step adds an $O(N)$ factor and TLEs; precompute $M_1, \dots, M_{2NK}$ once before the binary search.
   ```
6. **`CP-VI.6` (`#254` UOJ 310, L807–814, after L813)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Computing $\widehat{C} = \operatorname{FWT}_\oplus(C)$ modulo $998244353$ destroys the integer identity $k_S = (n + \widehat{C}_S)/2$ needed for the exponent in $3^{k_S}$; the empty pair $A = B = \emptyset$ contributes $+1$ to $[x^0]P(x)$ and must be subtracted before dividing by $2$.
   ```
7. **`CP-VI.7` (`#175` Luogu P5406, L856–863, after L862)**:
   ```markdown
   - **Failure Modes & Edge Cases**: Self-loops must be ignored and parallel edges accumulated into $L(z)$; if $\det \widehat{L^{(n)}}(\omega) \equiv 0 \pmod P$ for all $\omega$ (or all $c_v = 0$ after $\operatorname{IFWT}_{\text{op}}$), the graph is disconnected and the algorithm must output $-1$.
   ```
8. **`CP-VI.8` (`#180` Luogu P5643, L903–910, after L909)**:
   ```markdown
   - **Failure Modes & Edge Cases**: When the starting vertex $x$ lies in the target set $T$ ($x \in T$), $E_x = 0$ immediately ($A_x = B_x = 0$); for the empty set $T = \emptyset$, set $g(\emptyset) = 0$ before running the SOS transform.
   ```

---

## Audit Dimension 2: Mandatory Failure Mode Callouts (`CURRICULUM_ARCHITECTURE.md` §2.3–§2.4)

We verified all three Part VI mandatory failure modes required by the specification:

1. **Chapter 22 — Failure Mode #10 (Zero-Divisor Persistence $(a, c) \equiv a \cdot 0^c$)**:
   - **Verified Present & Prominent**: Highlighted in `::: {.callout-warning}` at [`ch22` L376–385](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd#L376-L385) (`## Failure Mode #10: Naive Modular Inverse Corrupts Zero Point-Values`), plus a second `::: {.callout-warning}` at L219–229 for unbalanced HLD `Compress` midpoint splits.
2. **Chapter 23 — Failure Mode #9 ($\begin{bmatrix}n\\k\end{bmatrix}_q$ when $q^d \equiv 1 \pmod p$ & $q$-Lucas)**:
   - **Verified Present & Prominent**: Highlighted in `::: {.callout-warning}` at [`ch23` L227–232](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L227-L232) (`## Failure Mode #9 & Remedy: $0/0$ Cancellation in \begin{bmatrix} n \\ k \end{bmatrix}_q \bmod p`), accompanied by Theorem 23.2 ($q$-Lucas Theorem) and a 12-line C++ implementation at L234–247.
3. **Chapter 24 — `IFWT-XOR` Division-by-2 ($p \neq 2$) & Characteristic-$p$ Limits**:
   - **Verified Present & Prominent**: Highlighted in `::: {.callout-warning}` at [`ch24` L132–137](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd#L132-L137) (`### Failure Mode & Remedy: Characteristic-2 Collapse & Zero Factors in Pointwise FWT Products`), plus explicit $p > n$ / $p > \lfloor\log_2 N\rfloor$ preconditions in §24.3 and §24.4.

---

## Audit Dimension 3: Code Block Length ($\le 15$ Lines) & Standard Library Ban (`AGENTS.md` L9–10)

### 3.1 Inventory of All Code Blocks Across Part VI

| File | Line Range | Language Tag | Inner Lines | Limit ($\le 15$) | Content & `AGENTS.md` L9–10 Compliance |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `ch22` | L45–57 | `cpp` | 11 | ✅ Pass | $O(NK)$ truncated subtree knapsack kernel (`merge_child`) |
| `ch22` | L167–181 | `{mermaid}` | 13 | ✅ Pass | Mermaid diagram for HLD `Rake` + `Compress` |
| `ch22` | L276–288 | `cpp` | 11 | ✅ Pass | Weighted prefix-sum midpoint `compress` kernel |
| `ch22` | L410–424 | `cpp` | 13 | ✅ Pass | `ZeroFreeVal` $(a, c)$ zero-divisor struct |
| `ch22` | L537–547 | `cpp` | 9 | ✅ Pass | Static Top Tree node builder (`make_node`) |
| `ch23` | L234–247 | `cpp` | 12 | ✅ Pass | $q$-Lucas root-of-unity evaluator (`q_binom_root`) |
| `ch23` | L328–338 | `{mermaid}` | 9 | ✅ Pass | Mermaid diagram for Durfee square decomposition |
| `ch23` | L352–367 | `cpp` | 14 | ✅ Pass | $O(N\sqrt{N})$ Euler pentagonal partition solver |
| `ch24` | L68–78 | `cpp` | 9 | ⚠️ Review | Standard 3-loop FWT butterfly template (`fwt`) |
| `ch24` | L181–192 | `cpp` | 10 | ✅ Pass | Ranked FZT subset convolution kernel (`subset_conv`) |
| `ch24` | L285–298 | `cpp` | 12 | ✅ Pass | MSB-split recursive SPS $\exp$ (`sps_exp`) |
| `ch24` | L366–379 | `cpp` | 12 | ✅ Pass | Pointed vertex-deletion biconnected graph counter |
| `ch24` | L447–460 | `cpp` | 12 | ✅ Pass | Dirichlet $\Omega(n)$-derivation $\exp_D$ (`dirichlet_exp`) |
| `ch24` | L558–567 | `cpp` | 8 | ⚠️ Review | `SS-1`: Superset FZT pair-merging loop (`merge_pair`) |
| `ch24` | L659–668 | `cpp` | 8 | ✅ Pass | `SS-2`: Pointed connected component query loop |
| `ch24` | L771–783 | `cpp` | 11 | ✅ Pass | `Int-1`: Ranked FZT divided power $T(\mathbf{x})^c / c!$ |
| `ch24` | L857–872 | `cpp` | 14 | ✅ Pass | `Int-2`: Bitwise XOR-zero Nim DP |
| `ch24` | L963–976 | `cpp` | 12 | ✅ Pass | `Adv-1`: Base-4 bit-packed `uint64_t` subset convolution |
| `ch24` | L1078–1093 | `cpp` | 14 | ✅ Pass | `Adv-2`: Triple-XOR Walsh–Hadamard eigenvalue solver |
| `ch24` | L1186–1198 | `cpp` | 11 | ✅ Pass | `Mas-1`: Pointwise rank-series ODE for SPS $\exp$ |
| `ch24` | L1287–1302 | `cpp` | 14 | ✅ Pass | `Mas-2`: $n$-round pointed $\ln$ biconnected solver |
| `cp06` | L758–763 | ❌ **None (`''`)** | 4 | ❌ **Fail** | **Untagged code block** + standard SOS loop in `CP-VI.5` |

### 3.2 Actionable Code Block Fixes

#### Fix CP06-CB1: Replace Untagged SOS Code Block in `cp06-part6-trees-qseries-sps-dirichlet.qmd` (L757–764)
In [`cp06-part6-trees-qseries-sps-dirichlet.qmd` L757–764](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd#L757-L764), the 4-line code block has **no language tag** (` ``` `) and prints a raw SOS loop. Replace L757–764 with a single clean mathematical invocation:

- **Target (L757–764)**:
  ```markdown
  Computing $F(X) = \sum_{T \subseteq X} c(T)$ for all $X \subseteq U$ is a single $N$-bit **Fast Zeta / SOS Transform**:
  ```
  for i = 0 to N - 1:
      for mask = 0 to 2^N - 1:
          if (mask & (1 << i)):
              F[mask] += F[mask ^ (1 << i)]
  ```
  We then check $D - F[(2^N - 1) \oplus S] \ge \operatorname{popcount}(S) \cdot K$ for all $S \in [1, 2^N - 1]$. Binary searching $D \in [N K, 2 N K]$ takes $\lceil \log_2(N K) \rceil \le 22$ iterations.
  ```
- **Replacement**:
  ```markdown
  Computing $F(X) = \sum_{T \subseteq X} c(T)$ for all $X \subseteq U$ is a single $N$-bit **Fast Zeta / SOS Transform** $F = \operatorname{FZT}_{\text{OR}}(c)$ (iterating $b = 0, \dots, N - 1$ and accumulating $F[\text{mask}] \mathrel{+}= F[\text{mask} \oplus 2^b]$ whenever bit $b$ of $\text{mask}$ is $1$).
  We then check $D - F[(2^N - 1) \oplus S] \ge \operatorname{popcount}(S) \cdot K$ for all $S \in [1, 2^N - 1]$. Binary searching $D \in [N K, 2 N K]$ takes $\lceil \log_2(N K) \rceil \le 22$ iterations.
  ```

---

## Audit Dimension 4: Quarto Syntax, Math Delimiters, Table Pipes & Collapsible Hygiene

### 4.1 Critical `!$$` Spurious Factorial Collisions in Display Math (5 Instances)

Per `AGENTS.md`:
> *"Never end a sentence immediately before a display math block with an exclamation mark (`!$$`) or place an exclamation mark before closing display math (`... !$$`), as LaTeX/Pandoc parses `!` inside `$...$` as a factorial operator."*

#### 1. `ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd` L438 (`0!$$` renders as $0! = 1$)
- **Target (L438)**:
  ```markdown
  $$G H^T = I_r P + P I_{m-r} = P \oplus P = 0!$$
  ```
- **Replacement**:
  ```markdown
  $$G H^T = I_r P + P I_{m-r} = P \oplus P = 0.$$
  ```

#### 2. `ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd` L1025 (`\begin{bmatrix} N + M \\ N \end{bmatrix}_q!$$`)
- **Target (L1025)**:
  ```markdown
  $$F(q) = \sum_{0 \le A_1 \le \dots \le A_N \le M} q^{\sum_{i=1}^N A_i} = \begin{bmatrix} N + M \\ N \end{bmatrix}_q!$$
  ```
- **Replacement**:
  ```markdown
  $$F(q) = \sum_{0 \le A_1 \le \dots \le A_N \le M} q^{\sum_{i=1}^N A_i} = \begin{bmatrix} N + M \\ N \end{bmatrix}_q.$$
  ```

#### 3. `ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd` L1037 (`\begin{bmatrix} a_0 \\ b_0 \end{bmatrix}_{\zeta_d}!$$`)
- **Target (L1037)**:
  ```markdown
  $$\begin{bmatrix} N + M \\ N \end{bmatrix}_{\zeta_d} = \binom{a_1}{b_1} \begin{bmatrix} a_0 \\ b_0 \end{bmatrix}_{\zeta_d}!$$
  ```
- **Replacement**:
  ```markdown
  $$\begin{bmatrix} N + M \\ N \end{bmatrix}_{\zeta_d} = \binom{a_1}{b_1} \begin{bmatrix} a_0 \\ b_0 \end{bmatrix}_{\zeta_d}.$$
  ```

#### 4. `ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd` L1144 (`26!$$` renders as $26!$)
- **Target (L1144)**:
  ```markdown
  $$\dim \mathcal{C}^\perp = m - r \le 53 - 27 = 26!$$
  ```
- **Replacement**:
  ```markdown
  $$\dim \mathcal{C}^\perp = m - r \le 53 - 27 = 26.$$
  ```

#### 5. `ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd` L161–163 (`!\n\n$$` pattern)
- **Target (L161–163)**:
  ```markdown
  Notice what happens when we multiply two monomials $\mathbf{x}^A$ and $\mathbf{x}^B$ in the quotient ring!

  $$
  ```
- **Replacement**:
  ```markdown
  Notice what happens when we multiply two monomials $\mathbf{x}^A$ and $\mathbf{x}^B$ in the quotient ring:

  $$
  ```

---

### 4.2 Unescaped `|` Inside `$...$` in Markdown Tables (2 Instances)

In Pandoc/Quarto pipe tables, any raw `|` character on a table row (even inside `$...$` or `\|`) splits the table cell before MathJax runs.

#### 1. `ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd` L571 (`|S|=k` splits the table row into 6 columns instead of 4!)
- **Target (L571)**:
  ```markdown
  | Global sum $\sum_{|S|=k} \text{cost}(S)$ for all $k = 1 \dots N$ | Full $O(N^2)$ subtree polynomial | **§22.2** HLD Chain D&C / **§22.4** Static Top Tree | $O(N \log^2 N)$ |
  ```
- **Replacement**:
  ```markdown
  | Global sum $\sum_{\lvert S \rvert = k} \text{cost}(S)$ for all $k = 1 \dots N$ | Full $O(N^2)$ subtree polynomial | **§22.2** HLD Chain D&C / **§22.4** Static Top Tree | $O(N \log^2 N)$ |
  ```

#### 2. `ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd` L466 (`\mathbin{\|}` inside `$...$` in Markdown table)
- **Target (L466)**:
  ```markdown
  | **Bitwise OR / AND FZT & IFMT** | $K[(\{0,1\}^n, \mathbin{\|})]$ or $\mathbin{\&}$ | $O(n 2^n)$ | $O(2^n)$ | None (arbitrary ring $R$) | Bitwise OR / AND convolution, SOS DP |
  ```
- **Replacement**:
  ```markdown
  | **Bitwise OR / AND FZT & IFMT** | $K[(\{0,1\}^n, \mathbin{\vert})]$ or $\mathbin{\&}$ | $O(n 2^n)$ | $O(2^n)$ | None (arbitrary ring $R$) | Bitwise OR / AND convolution, SOS DP |
  ```

---

### 4.3 Missing Blank Lines Before `</details>` in Chapter 23 (32 Instances)

In [`ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd), **all 32 `</details>` closing tags lack a preceding blank line**, which can cause Pandoc/Quarto to treat the preceding line (especially bullet lists in the Algorithm Contracts at L555, L640, L715, L814, L914, L992, L1111, L1192) as raw HTML rather than closing the Markdown block cleanly:
- **Affected lines in `ch23`**:
  `L505, L515, L523, L555, L586, L595, L606, L640, L665, L674, L682, L715, L745, L753, L776, L814, L844, L853, L863, L914, L939, L950, L961, L992, L1027, L1039, L1050, L1111, L1138, L1149, L1158, L1192`.
- **Fix**: Insert a blank line immediately before every `</details>` in `ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd` (`replace("</details>", "\n</details>")`).

---

### 4.4 Truncated Words, Mismatched Internal Theorem References & Editorial Polish

#### 1. `ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd` L90 & L213 (Truncated Leading Words)
- **L90**:
  - **Target**: ` encounter two distinct geometric bottlenecks on trees:`
  - **Replacement**: `We encounter two distinct geometric bottlenecks on trees:`
- **L213**:
  - **Target**: ` moreover, because the heavy chains partition all vertices of $T$`
  - **Replacement**: `Moreover, because the heavy chains partition all vertices of $T$`

#### 2. `ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd` Mismatched Internal Theorem References & Meta-Footnote
- **L593 & L621 (`SS-2` CF 1916F)**: Cites `Theorem 23.4` for Grassmannian Subspace Möbius Inversion, but `Theorem 23.4` (L389) is Jacobi's Triple Product Identity! Replace `Theorem 23.4` at L593 and L621 with `§23.1 (Grassmannian Subspace Möbius Inversion)`.
- **L860 & L896 (`Adv-1` ABC 235 Ex)**: Cites `Proposition 23.1` (non-existent). Replace `Proposition 23.1` at L860 and L896 with `§23.1 (Theorem 22.1 / §23.4 Method Comparison)`.
- **L1036, L1069, L1200 (`Mas-1` ABC 278 Ex)**: Cites `Theorem 23.3` for the $q$-Lucas Theorem, but the $q$-Lucas Theorem is **`Theorem 23.2`** (L205), whereas `Theorem 23.3` (L286) is Euler's Pentagonal Number Theorem! Replace `Theorem 23.3` at L1036, L1069, and L1200 with `Theorem 23.2`.
- **L803 & L806 (`Int-2` CF 1603F)**: Fix minor typos `which Gives` $\to$ `which gives` (L803) and `elementsall` $\to$ `elements all` (L806).
- **L1196–1202 (Quarantined Research Templates Meta-Footnote)**: Replace the internal editorial meta-note (`Implementation Verification Footnote (Quarantined Research Templates R-48 & R-49)`) with a student-facing **Self-Assessment Checklist** callout matching Chapter 22 (L1281–1298) and Chapter 24 (L1315–1331).

#### 3. `ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd` L5 (Prerequisites Callout Consistency)
- **Target (L5)**:
  ```markdown
  > **Prerequisites**: Chapters 1–4 (Formal Power Series ring operations, Newton's method for $\ln$ and $\exp$, formal derivative ODEs), Chapter 13 (Matrix-Tree Theorem).
  ```
- **Replacement**:
  ```markdown
  ::: {.callout-note}
  ## Prerequisites
  - **Chapters 1–4**: Formal Power Series ring operations, Newton's method for $\ln$ and $\exp$, and formal derivative ODEs ($F' = G' F$).
  - **Chapter 13**: Kirchhoff's Matrix-Tree Theorem.
  :::
  ```
