# Part III Critic C Audit Report: Algorithm Contracts, Failure Modes, Editorial Policy & Quarto Syntax

- **Auditor**: Part III Critic C (`AGENTS.md` Editorial Policy, Algorithm Contracts, Canonical Failure Modes & Quarto Syntax Auditor)
- **Target Scope**:
  1. [`chapters/ch09-cdq-fft-online-relaxed-convolution.qmd`](../../chapters/ch09-cdq-fft-online-relaxed-convolution.qmd) (1,350 lines)
  2. [`chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd`](../../chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd) (1,351 lines)
  3. [`chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd`](../../chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd) (1,654 lines)
  4. [`chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`](../../chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd) (1,116 lines)
  5. [`chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd`](../../chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd) (1,532 lines)
  6. [`checkpoints/cp03-part3-online-implicit-lif-graphs.qmd`](../../checkpoints/cp03-part3-online-implicit-lif-graphs.qmd) (1,296 lines)
- **Total Lines Audited**: 8,299 lines across 6 `.qmd` files.

---

## Executive Summary & Scorecard

| Audit Dimension | Status | Summary of Findings |
| :--- | :--- | :--- |
| **1. `AGENTS.md` Code Policy ($\le 15$ Lines, Zero Boilerplate, Language Tags)** | **NEEDS FIXES (8 blocks)** | Zero `modint`/NTT/sieve library dumps exist anywhere in Part III. However, **5 code/ASCII blocks exceed 15 lines** (`ch09` L220–237 [16 lines], L321–340 [18 lines], L381–401 [19 lines], L449–472 [22 lines]; `cp03` L665–683 [17 lines]), **3 fenced blocks lack a language tag** (`ch09` L321, L381; `cp03` L126), and **2 Mermaid blocks in `ch12`** (L286, L402) use ```` ```mermaid ```` instead of Quarto's ```` ```{mermaid} ````. Also, **15 stream-of-consciousness `"Wait—"` / `"Wait:"` self-correction artifacts** remain in derivations (`ch09` L349, L1266; `ch10` L987, L1068; `ch11` L169, L939, L1048–1056, L1162, L1304, L1417, L1479, L1496, L1514; `cp03` L1161). |
| **2. Algorithm Contracts & Exact Index Boundaries** | **NEEDS FIXES (52 contracts)** | **Main Sections**: Missing or incomplete `Algorithm Contract` boxes in `ch09` (§9.2 missing loop invariant, §9.3 missing preconditions/postconditions/invariant, §9.4 missing contract box), `ch10` (§10.2 Coupled $2\times 2$ Jacobian Newton, §10.3 Higher-Power Pólya–Euler Newton, and §10.4 Otter's Dissimilarity Engine lack contract boxes), `ch11` (§11.1–§11.3 lack contract boxes), `ch12` (§12.1, §12.2, §12.4 lack contract boxes), and `ch13` (§13.1, §13.2, §13.3 lack contract boxes).<br>**Practice Ladders (40 Chapter Problems + 8 Checkpoint Problems)**: All 8 problems in `ch09`, `ch11`, and `ch12` lack formal `Algorithm Contract` callout boxes; all 8 problems in `ch10` and `ch13` have `Algorithm Contract` blocks but omit the mandatory **1-sentence Loop Invariant** and **Exact Index Boundaries**. |
| **3. Canonical Failure Modes (`CURRICULUM_ARCHITECTURE.md` Part III)** | **NEEDS FIXES (3 boxes)** | Almost all Part III failure modes are thoroughly explained, with three gaps requiring dedicated `.callout-warning` boxes:<br>1. **`ch13` §13.3**: Missing a dedicated `.callout-warning` box for **Canonical Failure Mode #15** (*Robinson's DAG Inclusion–Exclusion Sign Error $(-1)^{k-1}$ vs. $(-1)^{|V|-|S|}$*, currently only mentioned in prose at L333–337).<br>2. **`ch10` §10.1**: Missing a dedicated `.callout-warning` box for the **Implicit Newton Singular Derivative Trap $P_y(0, y_0) = 0$** (explained in prose at L101–125 and L1334, but needs a formal `.callout-warning` box alongside #8 and #9).<br>3. **`ch12` §12.1**: Pointed vs. Unpointed symmetry contrast is in a `.callout-note` at L43–59; needs an explicit `.callout-warning` for the **Pointed vs. Unpointed $1/n$ Division & Symmetry Factor Trap**. |
| **4. Quarto & Pandoc Markdown Syntax Safety** | **NEEDS FIXES (36 issues)** | Zero `\(` or `\[` delimiters, zero unclosed `:::` or `<details>` blocks, zero missing blank lines around `<summary>`/`</details>`, and zero unescaped `|` in tables. **However**:<br>1. **31 display math blocks (`$$...$$`) end with an unescaped emphatic `!`** (`!$$` or `!\n$$` in `ch09` [8], `ch10` [7], `ch11` [16]), which LaTeX/MathJax renders as a **factorial symbol** at the end of the equation!<br>2. **5 broken internal `.qmd` links** exist (`ch12` L358; `ch13` L5, L27, L685, L1525), including broken links to `ch12` and `ch14` using outdated file slugs. |

---

## Check 1: `AGENTS.md` Code Policy (`<= 15` Lines, Zero Boilerplate, Fenced Language Tags & Editorial Cleanliness)

### 1.1 Code & ASCII Blocks Exceeding 15 Lines or Missing Language Tags

#### Finding 1.1.1 — `ch09` L220–237 (`cpp`, 16 lines): Semi-Online CDQ Kernel Exceeds 15-Line Limit
- **Location**: `chapters/ch09-cdq-fft-online-relaxed-convolution.qmd`, lines 220–237 (16 lines).
- **Drop-in Replacement (12 lines)**:
```cpp
auto solve = [&](auto& self, int l, int r) -> void {
    if (r - l == 1) {
        f[l] = (l == 0) ? f0 : f[l] * inv_c(l) % MOD; // base case or finalize f[l]
        return;
    }
    int mid = (l + r) >> 1;
    self(self, l, mid);
    Poly prod = conv(Poly(f.begin() + l, f.begin() + mid),
                     Poly(g.begin(), g.begin() + (r - l)));
    for (int i = mid; i < r; ++i)
        f[i] = (f[i] + prod[i - l]) % MOD; // accumulate [l, mid) -> [mid, r)
    self(self, mid, r);
};
```

#### Finding 1.1.2 — `ch09` L321–340 (No language tag, 18 lines) & L349–375: Unlabeled Buggy 0-Indexed Grid & Stream-of-Consciousness Self-Correction
- **Location**: `chapters/ch09-cdq-fft-online-relaxed-convolution.qmd`, lines 321–375.
- **Issue**:
  1. Fenced block at L321–340 has **no language tag** (` ``` ` instead of ` ```text `) and is **18 lines** long.
  2. More importantly, L321–340 displays a **broken** 0-indexed table where $(0,5)$ and $(5,0)$ are labeled `q=5`, and then L349 says: *"Wait! Look closely at $q = 5$ ($i + j = 6$) in the 0-indexed table above: why did the table above show `q=5` at $(0, 5)$ and $(5, 0)$? Let us check this trap carefully!"* Per `AGENTS.md`, stream-of-consciousness `"Wait!"` self-corrections are forbidden; the text should state the 0-indexed boundary special-casing directly and present only the clean 1-indexed interior schedule (or a compact $\le 12$-line comparison).
- **Drop-in Replacement for `ch09` L315–401 (replaces both oversized untagged grids L321–340 and L381–401 and removes the `"Wait!"` self-correction)**:
````markdown
Why does a naive 0-indexed schedule $\ell = \operatorname{lowbit}(q)$ fail on the boundary axes $i = 0$ and $j = 0$? Because at step $q$, the boundary terms $f_0 g_q$ and $f_q g_0$ require $g_q$ and $f_q$ **immediately** at step $q$, whereas the interior pairs $(i, j)$ with $i, j \ge 1$ and $i + j = q + 1$ can wait until step $q$ (when $f_1 \dots f_q$ and $g_1 \dots g_q$ are all known) and be grouped by $\ell = \operatorname{lowbit}(q + 1)$:

1. **Boundary Axes ($i = 0$ or $j = 0$)**: Processed in $O(1)$ time immediately at step $q$:
   - At $q = 0$: add $f_0 g_0$ to $h_0$.
   - At $q \ge 1$: add $f_0 g_q + f_q g_0$ to $h_q$.
2. **Interior Quadrant ($i \ge 1, j \ge 1$)**: At step $q \ge 1$, let $\ell = \operatorname{lowbit}(q + 1) = (q + 1) \mathbin{\&} -(q + 1)$. We convolve the interior block $f[\ell \dots 2\ell - 1] \times g[q + 1 - 2\ell \dots q - \ell]$ (and its symmetric counterpart when the two ranges differ), which partitions all interior pairs $(i, j) \in \mathbb{Z}_{\ge 1}^2$ into disjoint $\ell \times \ell$ squares:

```text
  i \ j |   1     2     3     4     5     6     7
--------+------------------------------------------
    1   |  q=1   q=2   q=3   q=4   q=5   q=6   q=7
    2   |  q=2  [q=3   q=3]  q=5  [q=7   q=7]  ...
    3   |  q=3  [q=3   q=3]  q=5  [q=7   q=7]  ...
    4   |  q=4   q=5   q=5  {q=7   q=7   q=7   q=7}
    5   |  q=5  [q=7   q=7] {q=7   q=7   q=7   q=7}
```
````

#### Finding 1.1.3 — `ch09` L449–472 (`cpp`, 22 lines): `struct RelaxedConvolution` Exceeds 15-Line Limit
- **Location**: `chapters/ch09-cdq-fft-online-relaxed-convolution.qmd`, lines 449–472 (22 lines).
- **Drop-in Replacement (15 lines)**:
```cpp
long long next_step(int q, long long fq, long long gq) {
    f[q] = fq; g[q] = gq;
    if (q == 0) return h[0] = (h[0] + f[0] * g[0]) % MOD;
    h[q] = (h[q] + f[0] * g[q] + f[q] * g[0]) % MOD;
    int len = (q + 1) & -(q + 1); // lowbit(q + 1)
    auto add_box = [&](int l1, int l2) {
        Poly p = conv(Poly(f.begin() + l1, f.begin() + l1 + len),
                      Poly(g.begin() + l2, g.begin() + l2 + len));
        for (int k = 0; k < (int)p.size() && l1 + l2 + k <= N; ++k)
            h[l1 + l2 + k] = (h[l1 + l2 + k] + p[k]) % MOD;
    };
    add_box(len, q + 1 - 2 * len);
    if (q + 1 != 3 * len) add_box(q + 1 - 2 * len, len);
    return h[q];
}
```

#### Finding 1.1.4 — `ch12` L286–293 & L402–413: Use ```` ```{mermaid} ```` Instead of ```` ```mermaid ````
- **Location**: `chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`, lines 286–293 and 402–413.
- **Issue**: Both Mermaid diagrams use ```` ```mermaid ```` instead of Quarto's native ```` ```{mermaid} ```` chunk syntax (which is used consistently in `ch09`, `ch10`, `ch11`, `ch13`, and `cp03`).
- **Drop-in Fix**:
  - At `ch12` L286: change ```` ```mermaid ```` to ```` ```{mermaid} ````.
  - At `ch12` L402: change ```` ```{mermaid} ```` (from ```` ```mermaid ````) and simplify the edge labels on L409–412 to avoid parentheses inside edge labels:
````markdown
```{mermaid}
flowchart TD
    r["Root Vertex r — Factor: x"]
    B1["2-Vertex-Connected Block B_1 — E'(R(x))"]
    B2["2-Vertex-Connected Block B_2 — E'(R(x))"]
    e1["Bridge Child Tree T_1 — R(x)"]
    e2["Bridge Child Tree T_2 — R(x)"]
    r -->|"SET of non-bridge blocks"| B1
    r -->|"SET of non-bridge blocks"| B2
    r ==>|"Bridge edge"| e1
    r ==>|"Bridge edge"| e2
```
````

#### Finding 1.1.5 — `cp03` L126–135 (No language tag, 8 lines) & L665–683 (`cpp`, 17 lines)
- **Location**: `checkpoints/cp03-part3-online-implicit-lif-graphs.qmd`, lines 126–135 and 665–683.
- **Issues & Drop-in Replacements**:
  1. At `cp03` L126: change ```` ``` ```` to ```` ```text ```` (or ```` ```python ````).
  2. At `cp03` L665–683 (`cpp`, 17 lines): condense to 13 lines:
```cpp
void cdq(int l, int r) {
    if (r - l == 1) return;
    int mid = (l + r) >> 1;
    cdq(l, mid);
    // 3 forward NTTs on D0..D2[l..mid), 3 on P0..P2[0..r-l),
    // 3 pointwise linear combinations, and 3 inverse NTTs into D0..D2[mid..r):
    apply_coupled_transition(l, mid, r);
    cdq(mid, r);
}
```

---

### 1.2 Stream-of-Consciousness `"Wait—"` / `"Wait:"` Self-Corrections to Clean Up

Per `AGENTS.md`, derivations must be deliberate and clean rather than leaving raw stream-of-consciousness `"Wait—"` / `"Wait:"` mid-derivation self-corrections. Below are all **15 occurrences** across Part III and their clean replacements:

| File & Line | Current Stream-of-Consciousness Text | Clean Pedagogical Replacement |
| :--- | :--- | :--- |
| `ch09` L349 | `Wait! Look closely at $q = 5$ ($i + j = 6$) in the 0-indexed table above: why did the table above show q=5...` | Replace L315–401 using the clean derivation in **Finding 1.1.2** above. |
| `ch09` L1256 & L1266–1296 (`Mas-2` `AGC 060 D`) | Hint 3 (L1256) has an un-updated formula $\left(\frac{2(e^x-1)}{e^x+1}\right)^{m+1}$ that contradicts Step 2 (L1266–1296), where L1266 says: `Wait: let us check $N = 2$: for $N = 2$, $2! [x^2] ... = 2$, whereas the total number of pairs for $N = 2$ is 3!` | Update Hint 3 (L1256) to state $A(x) = \sum_{n \ge 0} \frac{a_n}{n!} x^n = \frac{1}{2 - e^x}$ and $R_1(x) = \frac{e^x - 1}{2 - e^x}$, and rewrite Step 2 (L1262–1296) to define $R_1(x) = A(x) - 1 = \frac{e^x - 1}{2 - e^x}$ directly from the alternating-run inclusion–exclusion without the false start. |
| `ch10` L987 (`Adv-1` `ABC 261 Ex`) | `Wait: in step 1 we cleared $(1 - y^{d_2})$ BEFORE taking $\partial_y$...` | Replace with: `**Why Clearing $(1 - y^{d_2})$ Before Differentiating Simplifies the Algebra**: Because $(1 - y^{d_2})$ vanishes at every root $y_j$ ($j \ge 1$), multiplying by $(1 - y^{d_2})$ first eliminates all quotient-rule denominators before applying $\partial_y$.` |
| `ch10` L1068 (`Adv-2` `AGC 058 D`) | `\frac{(1 - x_1 - x_2 - x_3 + \dots) \text{ Wait: standard Carlitz factor}}{...}` | Replace with the exact Carlitz exclusion factor: `$$\sum_{a, b, c \ge 0} \text{dp}(a, b, c) x_1^a x_2^b x_3^c = \frac{1}{1 - (x_1 + x_2 + x_3) + 2 x_1 x_2 x_3}.$$` |
| `ch11` L169 | `Wait — is $c_{-1}$ guaranteed to be $0$ after a change of variables $x = g(u)$?` | Replace with: `**Key Question**: Does the residue $c_{-1} = [x^{-1}] f(x)$ remain $0$ for derivative terms after a change of variables $x = g(u)$?` |
| `ch11` L939 (`Int-1` `CF 1930I`) | `Wait — let us check our small trace for $n = 1$!` | Replace with: `**Boundary Refinement at $h \ge 1$ ($n = 1, 2, 3$ Verification)**:` |
| `ch11` L1048–1056 (`Int-2` `ABC 345 G`) | `Wait — in Step 2, did we include $c_0 = [z^0](1 - P(z))^{-1} = 1$? Let us check $N = 2, K = 1$: ...` | State from Step 1 that when $s_r = N$ ($j = N$), the final transition from $s_{r-1}$ to $N$ is an **overshoot** step of size $\ge N - s_{r-1}$ (factor $\frac{z}{1 - z}$), so $F_N(z) = \frac{z}{1-z}\big((1 - P(z))^{-1} - 1\big) + [r=1 \text{ overshoot } \ge N]$. |
| `ch11` L1162 (`Adv-1` `CF 1528F`) | `(Wait: for $m = 0$, $0^k = 0$ since $k \ge 1$; for $j = 0$, $\left\{\begin{smallmatrix} k \\ 0 \end{smallmatrix}\right\} = 0$ since $k \ge 1$.)` | Replace with: `(Since $k \ge 1$, both the $m = 0$ term $0^k = 0$ and the $j = 0$ Stirling number $\left\{\begin{smallmatrix} k \\ 0 \end{smallmatrix}\right\} = 0$ vanish.)` |
| `ch11` L1304 (`Adv-2` `Luogu P8555`) | `Wait: what if $k \equiv 0 \pmod p$? If $p \mid k$ and $p \mid n$, Form 1 gives $\frac{k}{n}$ where BOTH numerator and denominator are $0 \pmod p$! That is why Form 1 is completely unusable when $p \mid n$, whereas Form 3 (`Variant B`) ... has NO $k$ in the prefactor and NO $1/n$ division!` | Replace with: `**Crucial Trap When Both $p \mid k$ and $p \mid n$**: Even if $p \mid k$, Form 1 produces the indeterminate form $0 / 0 \pmod p$ whenever $p \mid n$. Instead, we must use **Canonical Form 2 (Derivative-Free LIF)**: $$[x^n] F(x)^k = [u^{n-k}] \Big( u^{-k+1} (F^k)'(u) \big(\Phi(u) - u\Phi'(u)\big) \Phi(u)^{n-1} \Big)?$$ No — wait: let us check the exact identity for $[x^n] F(x)^k$!` (See **Important Mathematical Note on `ch11` L1305 & `cp03` L485/L1126** in Check 3 below!) |
| `ch11` L1417 (`Mas-1` `Luogu P5853`) | `Wait: we need a tree edge $(x, y)$ to be an ascent (`x < y`) if $y$ is the parent of $x$ or $x$ is the parent of $y$?` | Replace with: `**Convention**: Direct each tree edge away from the root $1$; an edge $u \to v$ is an ascent if $u < v$ and a descent if $u > v$.` |
| `ch11` L1479, L1496, L1514 (`Mas-1` `Luogu P5853`) | Three consecutive `"Wait —"` self-corrections while deriving the bivariate LIF for $T(x, y) = z \exp(\dots)$ in `P5853`. | Replace L1463–1545 with a single clean derivation of the symmetric Eulerian tree equation $U(x) = z \frac{y - x}{y e^{-U(x)} - x e^{-y U(x)/x}}$ and its Lagrange inversion extraction. |
| `cp03` L1161 (`CP-III.7`) | `Wait — in $\mathbb{F}_p[u]$, binary exponentiation of $\Phi(u)$ using polynomial multiplication uses **zero divisions**...` | Replace with: `Specifically, in $\mathbb{F}_p[u]$, binary exponentiation of $\Phi(u)$ using direct polynomial multiplication uses **zero divisions** and runs in $O(d p \log(dp))$ time per digit.` |

---

## Check 2: Algorithm Contracts & Index Boundaries Audit

Per `AGENTS.md` and `CURRICULUM_ARCHITECTURE.md`, every core algorithm in the main text AND every problem solution in the 8-problem ladder must specify:
1. **Input & Exact Index Boundaries**
2. **Preconditions** (local algebraic hypotheses: $\operatorname{val}(F)$, unit $[x^0]F \in R^\times$, prime characteristic $p > N$)
3. **Postconditions / Output**
4. **Time & Space Complexity**
5. **1-Sentence Loop/Recursion Invariant**

### 2.1 Main Section Algorithm Contracts Audit (`Ch 09`–`Ch 13`)

#### Chapter 9 (`ch09-cdq-fft-online-relaxed-convolution.qmd`)
1. **§9.2 Contract (L209–238)**: Has Precondition, Complexity, and Pitfall, but is **missing the 1-sentence Recursion Invariant and Postcondition**.
   - **Drop-in Addition (insert at `ch09` L218)**:
   ```markdown
   - **Postcondition**: Upon returning from `solve(solve, 0, 1 << ceil(log2(N + 1)))`, `f[0..N]` holds the exact coefficients $[x^n] F(x) \bmod 998244353$.
   - **Recursion Invariant**: Immediately before calling `solve(solve, mid, r)`, `f[0..mid-1]` holds the finalized coefficients $[x^i]F(x)$, and every index $n \in [mid, r)$ has accumulated $\sum_{i=0}^{mid-1} f_i g_{n-i} \bmod p$.
   ```
2. **§9.3 Contract (L438–473)**: Currently has only `State Space`, `Query Step`, and `Total Complexity`. Missing **Preconditions**, **Postconditions**, **Exact Index Boundaries**, and **1-Sentence Loop Invariant**.
   - **Drop-in Addition (insert at `ch09` L440)**:
   ```markdown
   - **Input / Index Boundaries**: Sequential queries $q = 0, 1, \dots, N$ arriving one by one with $f_q, g_q \in \mathbb{F}_p$.
   - **Preconditions**: Prime modulus $p = 998244353$ with $2^{\lceil \log_2(N+1) \rceil} \mid (p - 1)$.
   - **Postconditions**: At the end of step $q$, `h[q]` equals $\sum_{i=0}^{q} f_i g_{q-i} \bmod p$.
   - **Loop Invariant**: After step $q \ge 1$ completes, `h[m]` ($m > q$) holds the partial sum of $f_i g_j$ over all pairs $(i, j) \in [1, q]^2$ belonging to completed dyadic boxes of side $\ell = \operatorname{lowbit}(r + 1)$ for all $1 \le r \le q$, while `h[0..q]` are 100% finalized.
   ```
3. **§9.4 (`10-Line Online Replacements for inv, ln, exp, and Pólya Euler Transforms`, L477–560)**: **Missing an `Algorithm Contract` box altogether!**
   - **Drop-in `Algorithm Contract` Box (insert at `ch09` L560)**:
   ```markdown
   ::: {.callout-note}
   ## Algorithm Contract: Online `inv`, `ln`, `exp`, and Pólya `Euler` via CDQ / Relaxed Convolution
   - **Input & Index Boundaries**: Degree bound $N \ge 1$ and coefficient stream $g_0, g_1, \dots, g_N \in \mathbb{F}_p$.
   - **Preconditions**:
     - For `inv`: $g_0 \in \mathbb{F}_p^\times$ is invertible.
     - For `ln`: $g_0 = 1$ and $p > N$.
     - For `exp` and Pólya `Euler`: $g_0 = 0$ and $p > N$.
   - **Postconditions**: Computes $f_0, f_1, \dots, f_N \bmod p$ where $F(x) = G(x)^{-1}$, $\ln G(x)$, $\exp G(x)$, or $\prod_{k \ge 1}(1 - x^k)^{-g_k} \bmod x^{N+1}$.
   - **Time & Space Complexity**: $O(N \log^2 N)$ time and $O(N)$ space.
   - **1-Sentence Invariant**: At index $n \ge 1$, the online accumulator contains $\sum_{i=0}^{n-1} f_i \tilde{g}_{n-i}$ (where $\tilde{g}_k = k g_k$ for `ln`/`exp`), and dividing by $n$ (or $-g_0$) finalizes $f_n$ before any transition out of $n$ is scheduled.
   :::
   ```

#### Chapter 10 (`ch10-implicit-equations-newton-unlabeled-trees-otter.qmd`)
- §10.1 (L175–183) and §10.2 Differential Newton (L313–321) have complete `Algorithm Contract` boxes.
- **Missing Main-Section Contracts in `ch10`**:
  1. **§10.2 Coupled $2 \times 2$ Jacobian Newton (`L226`)**
  2. **§10.3 Higher-Power Pólya–Euler Newton (`L414`)**
  3. **§10.4 Otter's Dissimilarity Engine for Unrooted Unlabeled Trees (`L545`)**
- **Drop-in `Algorithm Contract` Boxes for `ch10` §10.2, §10.3, and §10.4**:
```markdown
::: {.callout-note}
## Algorithm Contract: Coupled $2 \times 2$ Jacobian Newton Iteration (Insert at `ch10` L226)
- **Input & Index Boundaries**: Target precision $N \ge 1$, coupled system $P(x, A, B) = 0, Q(x, A, B) = 0$, and base constants $(a_0, b_0)$ at $x = 0$.
- **Preconditions**: The $2 \times 2$ Jacobian determinant $\Delta_0 = (\partial_A P \cdot \partial_B Q - \partial_B P \cdot \partial_A Q)\big|_{x=0} \in \mathbb{F}_p^\times$ is invertible.
- **Postconditions**: Returns $(A(x) \bmod x^N, B(x) \bmod x^N)$ satisfying $P(x, A, B) \equiv Q(x, A, B) \equiv 0 \pmod{x^N}$.
- **Time & Space Complexity**: $O(N \log N)$ time and $O(N)$ space.
- **1-Sentence Loop Invariant**: At doubling step $m \to 2m$, $(A_m, B_m) \equiv (A, B) \pmod{x^m}$ implies that solving $J(A_m, B_m) [\Delta A, \Delta B]^T \equiv -[P(A_m, B_m), Q(A_m, B_m)]^T \pmod{x^{2m}}$ via Cramer's rule yields $(A_{2m}, B_{2m}) \equiv (A, B) \pmod{x^{2m}}$.
:::

::: {.callout-note}
## Algorithm Contract: Pólya–Euler Rooted Tree Newton Solver (Insert at `ch10` L414)
- **Input & Index Boundaries**: Target degree $N \ge 1$, prime modulus $p > N$.
- **Preconditions**: Base case $T_1(x) = 0 \bmod x$ and $p > N$ so $1/k \bmod p$ exists for all $1 \le k \le N$.
- **Postconditions**: Returns $T(x) = \sum_{n=1}^{N-1} t_n x^n \bmod x^N$ where $t_n$ is the number of unlabeled rooted trees on $n$ vertices modulo $p$.
- **Time & Space Complexity**: $O(N \log N)$ time and $O(N)$ space.
- **1-Sentence Loop Invariant**: At the start of precision step $m \to 2m$, $T_m(x) \equiv T(x) \pmod{x^m}$, the higher-power sum $S_{\ge 2}(x) = \sum_{k=2}^{2m-1} \frac{T_m(x^k)}{k} \bmod x^{2m}$ is exact to $O(x^{2m})$ because $2m \le 2(2m-1)$ for $m \ge 1$, and one Newton step produces $T_{2m}(x) \equiv T(x) \pmod{x^{2m}}$.
:::

::: {.callout-note}
## Algorithm Contract: Otter's Dissimilarity Engine for Unrooted Unlabeled Trees (Insert at `ch10` L545)
- **Input & Index Boundaries**: Rooted tree OGF $T(x) \bmod x^{N+1}$ with $[x^0]T(x) = 0$.
- **Preconditions**: Prime modulus $p > N$ (specifically $2 \in \mathbb{F}_p^\times$).
- **Postconditions**: Returns $U(x) = \sum_{n=1}^{N} u_n x^n \bmod x^{N+1}$ counting unrooted unlabeled trees on $n$ vertices.
- **Time & Space Complexity**: $O(N \log N)$ time and $O(N)$ space ($1$ squaring of $T(x)$ after computing $T(x)$).
- **1-Sentence Loop Invariant**: For each degree $n \in [1, N]$, $[x^n]\big(T(x) - \frac{1}{2}T(x)^2 + \frac{1}{2}T(x^2)\big)$ evaluates $|V(\tau)| - |E(\tau)| + |E_{\text{sym}}(\tau)| = 1$ on every unrooted tree isomorphism class $\tau$ of size $n$.
:::
```

#### Chapter 11 (`ch11-laurent-residues-raney-lagrange-inversion.qmd`)
- §11.4 (`L752–780`) has a complete `Algorithm Contract` box.
- **Missing Main-Section Contracts in `ch11`**:
  1. **§11.2 The 6 Canonical Forms of Lagrange Inversion (`L408`)**
  2. **§11.2 Elegia's Coupled Binomial Sum Linearization (`L526`)**
  3. **§11.3 Formal Laurent Series Negative-Valuation Shift (`L610`)**
  4. **§11.3 Raney's Cycle Lemma Extraction (`L654`)**
- **Drop-in `Algorithm Contract` Boxes for `ch11` §11.2 and §11.3**:
```markdown
::: {.callout-note}
## Algorithm Contract: Single-Target Lagrange Inversion Extraction (Insert at `ch11` L408)
- **Input & Index Boundaries**: Target index $n \ge 1$, series $\Phi(u) \bmod u^{n+1}$ and $H(u) \bmod u^{n+1}$.
- **Preconditions**: $[u^0]\Phi(u) \in R^\times$ is a unit; for Forms 1 and 5, $n \in R^\times$ ($p \nmid n$); for Forms 2, 3, and 4, valid over **any** commutative ring $R$ without dividing by $n$.
- **Postconditions**: Returns $[x^n] H(F(x))$ where $F(x) = x \Phi(F(x))$ (or $[z^n] H(u(z))$ where $z = u / \Phi(u)$).
- **Time & Space Complexity**: $O(n \log n)$ time via polynomial $\ln/\exp$ (when $p > n$), or $O(n)$ time when $\Phi(u) = (1+u)^t$ or $(1-u)^{-t}$.
- **1-Sentence Invariant**: Changing variables $x = u / \Phi(u)$ inside the formal residue $\operatorname{res}_x(H(F(x)) x^{-n-1} dx)$ preserves the residue identically across all $n \ge 1$.
:::

::: {.callout-note}
## Algorithm Contract: Elegia's Coupled Binomial-Power Linearization (Insert at `ch11` L526)
- **Input & Index Boundaries**: Parameters $n, t, r$, polynomial/rational series $A(u) \bmod u^{n+1}$, prime modulus $p > n$.
- **Preconditions**: $u = z(1+u)^t$ has $\Phi(u) = (1+u)^t$ with $\Phi(0) = 1$.
- **Postconditions**: Evaluates $\sum_{k=0}^{n} a_k \binom{r + tk}{n - k} \bmod p$ as $[u^n]\big(A(u)(1+u)^{r + tn}\big)$.
- **Time & Space Complexity**: $O(n)$ time and $O(n)$ space when $A(u)$ is rational of degree $O(1)$; $O(n \log n)$ time for general $A(u)$.
- **1-Sentence Invariant**: At index $k \in [0, n]$, the term $a_k [u^{n-k}](1+u)^{r + tn}$ equals $a_k [u^n]\big((u(1+u)^{-t})^k (1+u)^{r+tn}\big) = a_k \binom{r + tn - tk}{n - k}$.
:::

::: {.callout-note}
## Algorithm Contract: Negative-Valuation Laurent Inversion (`ABC 345 G` Trick, Insert at `ch11` L610)
- **Input & Index Boundaries**: Series $D(z) \in K[[z]]$ with $\operatorname{val}(D) = v \ge 1$ and $[z^v]D(z) \in K^\times$, target degree $N \ge 0$.
- **Preconditions**: Prime modulus $p$ such that $d_v = [z^v]D(z) \not\equiv 0 \pmod p$.
- **Postconditions**: Returns the Laurent series $D(z)^{-1} = z^{-v} \tilde{D}(z)^{-1}$ up to $z^N$ (requiring $\tilde{D}(z)^{-1} \bmod z^{N + v + 1}$).
- **Time & Space Complexity**: $O((N + v) \log(N + v))$ time and $O(N + v)$ space.
- **1-Sentence Invariant**: Factoring $D(z) = z^v \tilde{D}(z)$ shifts the leading non-zero coefficient $d_v$ to index $0$, making $\tilde{D}(z)$ a unit in $K[[z]]$ whose inverse truncated to $z^{N+v+1}$ determines all Laurent coefficients from $z^{-v}$ to $z^N$.
:::
```

#### Chapter 12 (`ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`)
- §12.3 (`L315–328`) has a complete `Algorithm Contract` box.
- **Missing Main-Section Contracts in `ch12`**:
  1. **§12.1 Pointing $\Theta$ & Labeled Functional Digraphs (`L165`)**
  2. **§12.2 Husimi Cactus & Labeled Desert Enumeration (`L255`)**
  3. **§12.4 Bridge-Block Trees & 2-Edge-Connected Graphs (`L492`)**
- **Drop-in `Algorithm Contract` Boxes for `ch12` §12.1, §12.2, and §12.4**:
```markdown
::: {.callout-note}
## Algorithm Contract: Labeled Functional Digraphs & Rooted Trees via Pointing (Insert at `ch12` L165)
- **Input & Index Boundaries**: Degree bound $N \ge 1$, prime modulus $p > N$.
- **Preconditions**: $T(x) = x \exp(T(x))$ has $\operatorname{val}(T) = 1$ and $[x^1]T(x) = 1$.
- **Postconditions**: Computes $T(x) \bmod x^{N+1}$, $C_{\text{func}}(x) = \ln\frac{1}{1 - T(x)} \bmod x^{N+1}$, and $F_{\text{func}}(x) = \frac{1}{1 - T(x)} \bmod x^{N+1}$.
- **Time & Space Complexity**: $O(N \log N)$ time and $O(N)$ space (or $O(N)$ closed-form via LIF).
- **1-Sentence Invariant**: At each precision doubling step $m \to 2m$, $T_{2m}(x) = T_m(x) - \frac{T_m(x) - x \exp(T_m(x))}{1 - T_m(x)} \bmod x^{2m}$ satisfies $T_{2m}(x) \equiv x \exp(T_{2m}(x)) \pmod{x^{2m}}$.
:::

::: {.callout-note}
## Algorithm Contract: Labeled Husimi Cactus & Desert EGF Solver (Insert at `ch12` L255)
- **Input & Index Boundaries**: Maximum vertex count $N \ge 1$, prime modulus $p > N$.
- **Preconditions**: $2 \in \mathbb{F}_p^\times$ and $p > N$ so $\exp$ and $\ln$ are valid up to $x^N$.
- **Postconditions**: Computes rooted cactus EGF $C^{\bullet}(x) \bmod x^{N+1}$, unrooted cactus EGF $C(x) = \int \frac{C^{\bullet}(x)}{x}\,dx \bmod x^{N+1}$, and desert EGF $D(x) = \exp(C(x)) \bmod x^{N+1}$.
- **Time & Space Complexity**: $O(N \log N)$ time and $O(N)$ space.
- **1-Sentence Invariant**: At Newton step $m \to 2m$ on $P(C^{\bullet}) = C^{\bullet} - x \exp\!\big(\frac{2C^{\bullet} - (C^{\bullet})^2}{2(1 - C^{\bullet})}\big)$, $\partial_{C^{\bullet}} P(0) = 1 \in \mathbb{F}_p^\times$ guarantees quadratic convergence to $C^{\bullet}(x) \bmod x^{2m}$.
:::

::: {.callout-note}
## Algorithm Contract: 2-Edge-Connected Graphs via Bridge-Block Inversion (Insert at `ch12` L492)
- **Input & Index Boundaries**: Rooted connected graph EGF $R(x) = x C'(x) \bmod x^{N+1}$ for $1 \le n \le N$.
- **Preconditions**: Prime modulus $p > N$; $\operatorname{val}(R) = 1$ and $[x^1]R(x) = 1 \in \mathbb{F}_p^\times$.
- **Postconditions**: Computes $E_{\text{2ec}}(x) \bmod x^{N+1}$ where $n! [x^n] E_{\text{2ec}}(x)$ is the number of labeled 2-edge-connected graphs on $n$ vertices.
- **Time & Space Complexity**: $O(N \log N)$ time for all $n \le N$ via Newton compositional inversion of $W(x) = R(x)\exp(-R(x))$, or $O(N \log N)$ for a single $n$ via LIF.
- **1-Sentence Invariant**: Substituting $y = R(x)$ into $R(x) = y \exp(R(x) - y \partial_y E_{\text{2ec}}(y))$ transforms the bridge-block grammar into the compositional inverse relation $y = R(y \exp(-y)) \iff y \exp(-y) = R^{\langle -1 \rangle}(y)$.
:::
```

#### Chapter 13 (`ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd`)
- §13.4 (`L688–712`) has a complete `Algorithm Contract` block.
- **Missing Main-Section Contracts in `ch13`**:
  1. **§13.1 Connected Simple & Eulerian Graphs + Chirp-$z$ Edge Convolution (`L213`)**
  2. **§13.2 Connected & Total Bipartite Graphs via 2-Colored Bridge (`L290`)**
  3. **§13.3 Labeled DAGs & Strongly Connected Digraphs (`L463`)**
- **Drop-in `Algorithm Contract` Boxes for `ch13` §13.1, §13.2, and §13.3**:
```markdown
::: {.callout-note}
## Algorithm Contract: Connected Simple & Eulerian Graphs and Chirp-$z$ Twist (Insert at `ch13` L213)
- **Input & Index Boundaries**: Maximum vertex count $N \ge 1$, prime modulus $p > N$.
- **Preconditions**: $[x^0]G(x) = 1$, $p > N$, and quadratic exponents $\binom{n}{2}$ are reduced modulo $p - 1$ (by Fermat's Little Theorem) before evaluating $2^{\pm \binom{n}{2}} \bmod p$.
- **Postconditions**: Returns $C(x) = \ln G(x) \bmod x^{N+1}$ (connected graphs), $C_{\text{even}}(x) = \ln G_{\text{even}}(x) \bmod x^{N+1}$ (connected Eulerian graphs), or Chirp-$z$ twisted products $\hat{H}(x) = \hat{A}(x)\hat{B}(x) \bmod x^{N+1}$.
- **Time & Space Complexity**: $O(N \log N)$ time and $O(N)$ space.
- **1-Sentence Invariant**: Dividing the $n$-th EGF coefficient by $2^{\binom{n}{2}}$ before multiplication and multiplying the $n$-th output coefficient by $2^{\binom{n}{2}}$ afterward converts the cross-bipartition edge factor $2^{k(n-k)}$ into a standard Cauchy product.
:::

::: {.callout-note}
## Algorithm Contract: Labeled Bipartite Graphs via 2-Colored EGF Bridge (Insert at `ch13` L290)
- **Input & Index Boundaries**: Maximum vertex count $N \ge 1$, prime modulus $p > N$.
- **Preconditions**: $2 \in \mathbb{F}_p^\times$ and $p > N$.
- **Postconditions**: Returns $C_{\text{bip}}(x) = \frac{1}{2}\ln B_2(x) \bmod x^{N+1}$ (connected bipartite graphs) and $B(x) = \exp(C_{\text{bip}}(x)) \bmod x^{N+1}$ (all bipartite graphs).
- **Time & Space Complexity**: $O(N \log N)$ time and $O(N)$ space ($1$ squaring of $\hat{I}(x)$, $1$ polynomial $\ln$, and $1$ polynomial $\exp$).
- **1-Sentence Invariant**: For every $n \in [0, N]$, untwisting $[x^n]\hat{I}(x)^2$ by $2^{\binom{n}{2}}$ produces $[x^n]B_2(x) = \frac{b_{2,n}}{n!}$, where each connected bipartite component contributes a factor of $2$ to $B_2(x)$ that is halved in $\frac{1}{2}\ln B_2(x)$ before re-exponentiating.
:::

::: {.callout-note}
## Algorithm Contract: Labeled DAGs & Strongly Connected Digraphs via Robinson–Stanley Inversion (Insert at `ch13` L463)
- **Input & Index Boundaries**: Maximum vertex count $N \ge 1$, prime modulus $p > N$.
- **Preconditions**: $[x^0]\hat{\Phi}(x) = 1$ and $[x^0]\hat{G}(x) = 1$; exponents $\binom{n}{2}$ reduced modulo $p - 1$.
- **Postconditions**: Returns $d_n = n! 2^{\binom{n}{2}} [x^n]\hat{\Phi}(x)^{-1} \bmod p$ (DAGs on $n$ vertices) and $s_n = n! [x^n](-\ln(1 - F(x))) \bmod p$ (strongly connected digraphs on $n$ vertices).
- **Time & Space Complexity**: $O(N \log N)$ time and $O(N)$ space.
- **1-Sentence Invariant**: Inverting $\hat{G}(x) = \sum_{n \ge 0} 2^{\binom{n}{2}} \frac{x^n}{n!}$ produces $1 - \hat{F}(x)$, which MUST be untwisted termwise by $2^{\binom{n}{2}}$ to obtain the ordinary EGF $F(x)$ before applying $-\ln(1 - F(x))$ to extract strongly connected digraphs.
:::
```

---

### 2.2 Practice Ladder Algorithm Contracts Audit (40 Chapter Problems + 8 Checkpoint Problems)

Below is the audit status and drop-in contract specification for all 48 problems across `Ch 09`–`Ch 13` and `CP-III`:

#### A. Chapter 9 Practice Ladder (`ch09` L568–1331)
Currently, **none of the 8 problems in `ch09`** have an `::: {.callout-note} ## Algorithm Contract:` box (they end with prose paragraphs or bulleted complexity lines). Also note: in **`SS-1` (`ARC 138 E`, L612–631)**, the derivation writes $f_n = \sum_{k=1}^{n-1} f_k \binom{n-k-1}{k-1} \psi_{n,k}$ without specifying the closed form of the outside completion factor $\psi_{n,k}$; make sure $\psi_{n,k}$ is explicitly defined in Step 2 of `SS-1`.
- **Drop-in `Algorithm Contract` Summary Table for `ch09` (`SS-1` through `Mas-2`)** (insert as `::: {.callout-note} ## Algorithm Contract` at the end of each problem's `<details>` solution block):

| Problem & Insert Line | Input & Index Boundaries | Preconditions | Postconditions | Complexity | 1-Sentence Loop/Recursion Invariant |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`SS-1` (`ARC 138 E`)** (`L653`) | $N, K \in [1, 5000]$ (or $10^5$), indices $0 \le k \le N$. | $p = 998244353 > N$. | Outputs valid sequence count modulo $p$. | $O(N^2)$ DP or $O(N \log^2 N)$ CDQ, $O(N)$ space. | Before recursing on $[mid, r)$, `dp[0..mid-1]` are finalized and their binomial transitions to $[mid, r)$ have been added. |
| **`SS-2` (`CF 553E`)** (`L761`) | $n \le 50, m \le 100, T \le 2\times 10^4$, time indices $t \in [0, T]$. | $p_{e, k} \ge 0, \sum_{k=1}^T p_{e, k} = 1$. | Outputs minimum expected cost $D_{1, 0}$ at $t = 0$. | $O(m T \log^2 T + n T)$ time, $O((n+m)T)$ space. | Because transitions advance $t \to t + k$ ($k \ge 1$), anti-causal CDQ processes $[mid, r)$ **before** $[l, mid)$ so `D[v][mid..r)` is finalized before convolving backward into `E[e][l..mid)`. |
| **`Int-1` (`ABC 230 Ex`)** (`L891`) | Target weight $W \le 10^5$, item indicator $c_w \in \{0, 1\}$ for $w \in [1, W]$. | $t_0 = 0$, $p = 998244353 > W$. | Outputs $t_2, \dots, t_W \bmod p$ where $T(x) = x\exp(\sum_{k\ge 1}\frac{T(x^k)-C(x^k)}{k})$. | $O(W \log^2 W)$ time, $O(W)$ space. | Immediately after `t[n]` is finalized at leaf $n$, `t[n]` is propagated to all harmonic multiples $m = k n \le W$ (`g[m] += n * t[n]`) before step $n + 1$ begins. |
| **`Int-2` (`ABC 315 Ex`)** (`L974`) | $N \le 2\times 10^5$, array $A_1 \dots A_N$, indices $n \in [0, N]$. | $f_0 = 1$, $p = 998244353$. | Outputs $f_1, \dots, f_N \bmod p$ where $f_n = A_n [x^{n-1}] F(x)^2$. | $O(N \log N)$ via Relaxed Convolution (or $O(N \log^2 N)$ self-CDQ), $O(N)$ space. | After step $q = n - 1$ of `RelaxedConvolution`, `h[n-1]` equals $\sum_{i=0}^{n-1} f_i f_{n-1-i} \bmod p$, which determines $f_n = A_n h_{n-1} \bmod p$ in time to feed $(f_n, f_n)$ into step $q = n$. |
| **`Adv-1` (`ABC 384 G` / Online `inv`/`exp`)** (`L1065`) | $N \le 10^5$, streaming coefficients $a_0 \dots a_N$, queries $q \in [0, N]$. | $a_0 = 1$ (for `inv`/`ln`) or $a_0 = 0$ (for `exp`), $p = 998244353 > N$. | Outputs $b_q \bmod p$ online after each query $q$. | $O(N \log^2 N)$ total time, $O(N)$ space. | At step $q \ge 1$, the relaxed convolution engine has accumulated $\sum_{i=1}^{q-1} i a_i b_{q-i}$ into `h[q]`, so adding $q a_q b_0$ and dividing by $q$ finalizes $b_q$ before advancing to $q + 1$. |
| **`Adv-2` (`CF 848E`)** (`L1149`) | Circle semi-length $n \le 5\times 10^4$, states $c \in \{0, 1, 2\}$, indices $k \in [0, n]$. | $\operatorname{val}(P_c) \ge 2$, $p = 998244353$. | Outputs total circular matching beauty modulo $p$. | $O(n \log^2 n)$ time ($9$ NTTs per CDQ node), $O(n)$ space. | At each CDQ node $[l, r)$, transforming `D0..D2[l..mid)` and `P0..P2[0..r-l)` once into point-value form updates all three right-half slices `D0..D2[mid..r)` in $9$ NTTs instead of $18$. |
| **`Mas-1` (`Luogu P4705` / Coupled CDQ)** (`L1231`) | $N \le 10^5$, coupled system dimension $d$, indices $n \in [0, N]$. | Transition matrix $M(x)$ has $M(0) = 0$, $p = 998244353 > N$. | Outputs coupled state vectors $F_0 \dots F_N \bmod p$. | $O(d^2 N \log N + d N \log^2 N)$ time, $O(d N)$ space. | Pre-transforming $M(x)$ slices or reusing forward NTTs of $F[l \dots mid)$ across all $d$ rows preserves exact semi-online causality while reducing NTT calls from $O(d^2)$ to $O(d)$ per CDQ node. |
| **`Mas-2` (`AGC 060 D`)** (`L1330`) | $N \le 2\times 10^5$, indices $n \in [0, N]$. | $p = 998244353 > N$, $[x^0](2 - e^x) = 1 \in \mathbb{F}_p^\times$. | Outputs $[x^N/N!] A(x) \sum_{m \ge 0} R_1(x)^{2m}$ via EGF inversion/CDQ. | $O(N \log N)$ (via `inv`) or $O(N \log^2 N)$ (via CDQ), $O(N)$ space. | At each degree $n \in [0, N]$, the alternating-run EGF coefficients $[x^n]A(x)$ and $[x^n]R_1(x)$ satisfy $(2 - e^x)A(x) \equiv 1 \pmod{x^{N+1}}$. |

#### B. Chapter 10 Practice Ladder (`ch10` L649–1325)
All 8 problems in `ch10` already have `::: {.callout-note} ## Algorithm Contract` callout boxes (`SS-1` L649, `SS-2` L744, `Int-1` L830, `Int-2` L925, `Adv-1` L1012, `Adv-2` L1096, `Mas-1` L1220, `Mas-2` L1315), **but all 8 omit the mandatory `- **Loop Invariant**:` and `- **Exact Index Boundaries**:` bullets** (and `Adv-1` L1012 also omits `- **Preconditions**:`).
- **Drop-in Additions for `ch10` Practice Ladder Contracts**:
  1. **`SS-1` (`Luogu P4389` / Implicit Newton Warmup, `L655`)**:
     - `- **Index Boundaries**: Precision doubles $m = 1, 2, 4, \dots, 2^{\lceil \log_2(N+1) \rceil}$, truncating all series to $[0, 2m)$.`
     - `- **Loop Invariant**: At the start of step $m \to 2m$, $A_m(x) \equiv A(x) \pmod{x^m}$, and one Newton update zeroes the residual $P(x, A_{2m}(x)) \pmod{x^{2m}}$.`
  2. **`SS-2` (`SPOJ TRP` / Unlabeled Trees, `L750`)**:
     - `- **Index Boundaries**: $1 \le n \le N$; $T(x)$ computed on $[0, N]$, then Otter correction applied on $[1, N]$.`
     - `- **Loop Invariant**: At Newton step $m \to 2m$, $T_m(x) \equiv T(x) \pmod{x^m}$ determines $\sum_{k=2}^{2m-1} \frac{T_m(x^k)}{k} \bmod x^{2m}$ exactly without needing $T_{2m}$.`
  3. **`Int-1` (`CodeChef TREDEG` / Tree Degree Powers, `L837`)**:
     - `- **Index Boundaries**: $0 \le j \le N - 2$ for EGF coefficients; $1 \le n \le N$ for tree sizes.`
     - `- **Loop Invariant**: After convolving $A(x)$ and $B(x)$ up to degree $N - 2$, $[x^{n-2}](A(x)B(x))$ equals the exact Prüfer sum over all degree sequences on $n$ vertices.`
  4. **`Int-2` (`CF 438E` — The Child and Binary Tree, `L932`)**:
     - `- **Index Boundaries**: $0 \le n \le m \le 10^5$, Newton precision $d = 1, 2, 4, \dots$ up to $m + 1$.`
     - `- **Loop Invariant**: After each doubling step $d \to 2d$, $F_{2d}(x)$ satisfies $C(x) F_{2d}(x)^2 - F_{2d}(x) + 1 \equiv 0 \pmod{x^{2d}}$ with $[x^0]F_{2d}(x) = 1$.`
  5. **`Adv-1` (`ABC 261 Ex` — Game on Graph / Kernel Method, `L1012`)**:
     - `- **Preconditions**: $d_1 + d_2 \le N$, prime modulus $p = 998244353$, distinct nonzero roots $y_1, \dots, y_{d_2}(x)$ of the kernel.`
     - `- **Index Boundaries**: Bivariate boundary indices $0 \le r < d_2$, series truncated to $x^N$.`
     - `- **Loop Invariant**: Substituting each root branch $y = y_j(x)$ into the kernel identity annihilates the unknown interior function $F(x, y_j(x))$, yielding $d_2$ independent linear equations for the $d_2$ boundary series.`
  6. **`Adv-2` (`AGC 058 D` — Yet Another ABC String, `L1103`)**:
     - `- **Index Boundaries**: $0 \le k \le \min(A, B, C)$ for the Carlitz inclusion–exclusion index $k$, with $N = A + B + C$.`
     - `- **Loop Invariant**: At index $k \in [0, \min(A, B, C)]$, the $k$-th summand counts arrangements in which at least $k$ forbidden cyclic triples $(\mathtt{ABC}, \mathtt{BCA}, \mathtt{CAB})$ are collapsed into super-blocks.`
  7. **`Mas-1` (`Luogu P4747` — Simple Permutations, `L1227`)**:
     - `- **Index Boundaries**: $1 \le k \le n \le 10^5$, Newton compositional inverse precision $m = 2, 4, 8, \dots$ up to $n + 1$.`
     - `- **Loop Invariant**: At step $m \to 2m$, $G_m(y) \equiv F^{\langle -1 \rangle}(y) \pmod{y^m}$, and $G_{2m}(y) = G_m(y) - \frac{F(G_m(y)) - y}{F'(G_m(y))} \bmod y^{2m}$ satisfies $F(G_{2m}(y)) \equiv y \pmod{y^{2m}}$.`
  8. **`Mas-2` (`Luogu P5900` — Unlabeled Trees Without Centroid Ties, `L1322`)**:
     - `- **Index Boundaries**: Rooted tree sizes $1 \le s \le \lfloor(n-1)/2\rfloor$, total degree $1 \le n \le N$.`
     - `- **Loop Invariant**: Processing maximum subtree size cap $M = \lfloor(n-1)/2\rfloor$ via Pólya $\exp\big(\sum_{k \ge 1}\frac{1}{k}\sum_{s=1}^{M} r_s x^{ks}\big)$ counts exactly those rooted trees whose children all have size $\le \lfloor(n-1)/2\rfloor$ (the unique centroid).`

#### C. Chapter 11 Practice Ladder (`ch11` L790–1635)
Currently, **none of the 8 problems in `ch11`** have an `::: {.callout-note} ## Algorithm Contract:` callout box.
- **Drop-in `Algorithm Contract` Summary Table for `ch11` (`SS-1` through `Mas-2`)** (insert as `::: {.callout-note} ## Algorithm Contract` at the end of each problem's `<details>` block):

| Problem & Insert Line | Input & Index Boundaries | Preconditions | Postconditions | Complexity | 1-Sentence Loop/Recursion Invariant |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`SS-1` (`Luogu P7439` / $k$-ary Trees)** (`L862`) | $n, k \ge 1$, index $0 \le j \le n$. | $\Phi(u) = (1+u)^k$ has $\Phi(0) = 1$, $p = 998244353$. | Outputs $\frac{1}{(k-1)n+1}\binom{kn}{n} \bmod p = \binom{kn}{n} - (k-1)\binom{kn}{n-1} \bmod p$. | $O(1)$ per query after $O(kn)$ factorial precomputation (or $O(\log_p(kn))$ via Lucas). | The derivative-free identity $[u^{n-1}](1 - (k-1)u)(1+u)^{kn-1} = \binom{kn-1}{n-1} - (k-1)\binom{kn-1}{n-2}$ holds over $\mathbb{Z}$ without dividing by $n$. |
| **`SS-2` (`CF 1264D2` / Bracket Depth or Raney Dyck)** (`L950`) | $1 \le n \le 10^6$, summation index $0 \le k \le n$. | Prime modulus $p = 998244353 > 2n$. | Outputs exact excursion/Dyck count modulo $p$. | $O(n)$ time and $O(n)$ space. | At step $k \in [0, n]$, the prefix factorial tables provide $\binom{2n}{n-k} \bmod p$ in $O(1)$ time with zero NTT calls. |
| **`Int-1` (`CF 1930I` — Counting Is Fun)** (`L1071`) | $1 \le n \le 5\times 10^5$, arbitrary prime $p \in (10^8, 10^9+9)$, $0 \le k \le n$. | $z = u/(1+u)^2$ has $[u^1]z = 1$, $p > 2n$. | Outputs $[z^n]F(z) = \sum_{k=0}^n q_k \binom{2n}{n-k} \bmod p$. | $O(n)$ time, $O(n)$ space (zero NTTs, zero divisions by $n$). | At each $k \in [0, n]$, $q_k = [u^k]\frac{1+2u+u^2+u^3}{1+2u+u^2-u^3} \bmod p$ is updated by the 3-term integer recurrence $q_k = -2q_{k-1} - q_{k-2} + q_{k-3}$. |
| **`Int-2` (`ABC 345 G` — Sugoroku 5)** (`L1165`) | $1 \le N \le 2\times 10^5$, $1 \le K \le 10^5$, degrees $0 \le j \le N + 1$. | $\operatorname{val}(1 - P(z)) = 1$ and $[z^1](1 - P(z)) = -1/K \in \mathbb{F}_p^\times$. | Outputs hitting probabilities for steps $r = 1 \dots N \bmod 998244353$. | $O(N \log N)$ time, $O(N)$ space. | Factoring $1 - P(z) = -z Q(z)$ shifts the leading coefficient to $[z^0]Q(z) = 1/K \neq 0$, so $Q(z)^{-1} \bmod z^{N+1}$ gives all coefficients of $(1 - P(z))^{-1}$ up to $z^{N-1}$. |
| **`Adv-1` (`CF 1528F` — AmShZ Farm)** (`L1272`) | $1 \le n \le 10^9$, $1 \le k \le 10^5$, index $1 \le j \le \min(n, k)$. | Prime $p = 998244353 > k$, $\gcd(n, n+1) = 1$. | Outputs $\sum_{j=1}^{\min(n,k)} \left\{\begin{smallmatrix} k \\ j \end{smallmatrix}\right\} n^{\underline{j}} (n+1)^{n-j} \bmod p$. | $O(k \log k)$ time, $O(k)$ space. | At iteration $j \in [1, \min(n, k)]$, `fall_n` equals $n^{\underline{j}} \bmod p$ and `pw` equals $(n+1)^{n-j} \bmod p$. |
| **`Adv-2` (`Luogu P8555` — Crypto HW 3)** (`L1376`) | $1 \le k \le n \le 10^{18}$, $d \le 5$, prime $p \le 10^5$. | $\Phi(0) \not\equiv 0 \pmod p$ ($p \mid n$ allowed). | Outputs $[x^n]F(x)^k \bmod p$. | $O(d p \log(dp) \log_p n)$ time, $O(d p)$ space. | At each base-$p$ digit step $(K, M) \to (\lfloor K/p \rfloor, \lfloor M/p \rfloor)$, $\deg A \le d$ and $[u^K](A(u)\Phi(u)^M) \equiv [x^n]F(x)^k \pmod p$ are preserved. |
| **`Mas-1` (`Luogu P5853` — Eulerian Labeled Trees)** (`L1540`) | $1 \le n \le 10^5$ (or $5000$), ascent count $0 \le k < n$. | Prime $p = 998244353 > n$. | Outputs Eulerian tree counts $T_{n, k} \bmod p$ for $0 \le k < n$. | $O(n^2)$ or $O(n \log^2 n)$ time, $O(n)$ space. | Applying LIF in $z$ to $U(x, y, z) = z \Phi(U)$ extracts $[z^n]U = \frac{1}{n}[u^{n-1}]\Phi(u)^n$ as a bivariate polynomial in $(x, y)$ of homogeneous degree $n$. |
| **`Mas-2` (`UOJ #424` — Bracket Excursion Rank Bounded Cartesian Trees)** (`L1634`) | $1 \le n \le 10^5$, height cap $1 \le m \le n$, indices $j \in \mathbb{Z}$. | Prime $p = 998244353 > 2n$; $z = u/(1+u)^2$. | Outputs bounded-left-depth Cartesian tree count $[z^n]C_m(z) \bmod p$. | $O(n)$ time, $O(1)$ auxiliary space. | Under $z = u/(1+u)^2$, the bounded-depth Chebyshev quotient $C_m(z) = \frac{1 - u^{m+1}}{1 - u^{m+2}}(1+u)$ pulls back to $\sum_{j \in \mathbb{Z}} \big([u^{n - j(m+2)}](1 - u) - [u^{n - (m+1) - j(m+2)}](1 - u)\big)(1+u)^{2n-1}$. |

#### D. Chapter 12 Practice Ladder (`ch12` L514–1112)
Currently, all 8 problems in `ch12` end with `- **Time Complexity**:` and `- **Space Complexity**:` bullets (`SS-1` L578, `SS-2` L655, `Int-1` L729, `Int-2` L813, `Adv-1` L883, `Adv-2` L956, `Mas-1` L1035, `Mas-2` L1112), **without a formal `Algorithm Contract` callout box, Preconditions, Postconditions, Index Boundaries, or 1-Sentence Loop Invariant**.
- **Drop-in `Algorithm Contract` Summary Table for `ch12` (`SS-1` through `Mas-2`)** (replace the 2-bullet complexity lines at the end of each problem with a full `::: {.callout-note} ## Algorithm Contract` box):

| Problem & Line | Input & Index Boundaries | Preconditions | Postconditions | Complexity | 1-Sentence Loop/Recursion Invariant |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`SS-1` (`ABC 387 F` — Count Arrays)** (`L578–580`) | $1 \le N, M \le 2025$, $f_i \in [1, N]$, colors $c \in [1, M]$. | Functional digraph partitioned into weak components with unique directed cycles. | Outputs $\prod_{\text{comp}} \sum_{c=1}^M \prod_{r \in \text{cycle}} \text{dp}[r][c] \bmod 998244353$. | $O(N M)$ time, $O(N M)$ space. | After processing subtree $u$ in reverse topological order, `pref[u][c]` equals $\sum_{x=1}^c \text{dp}[u][x] \bmod p$ for the rooted tree hanging off $u$. |
| **`SS-2` (`CF 1229E2` / Unicyclic EGF)** (`L655–657`) | $1 \le N \le 10^5$, tree sizes $1 \le k \le N$. | Prime $p = 998244353 > N$, $2 \in \mathbb{F}_p^\times$. | Outputs connected unicyclic simple graph counts $[x^n/n!] U(x) \bmod p$. | $O(N \log N)$ (or $O(N)$ closed-form sum), $O(N)$ space. | Subtracting the $k = 1$ self-loop term $T(x)$ and $k = 2$ multi-edge term $\frac{1}{2}T(x)^2$ from $\frac{1}{2}\ln\frac{1}{1 - T(x)}$ isolates simple undirected cycles of length $k \ge 3$. |
| **`Int-1` (`Luogu P5219` / Prufer Bounded Degree)** (`L729–731`) | $2 \le M < N \le 10^5$, degree $0 \le c < K \le M$. | $[x^0]E_{K-1}(x) = 1$, $p = 998244353 > N$. | Outputs $(f(M) - f(M-1)) \bmod p$ where $f(K) = (N-2)![x^{N-2}]E_{K-1}(x)^N$. | $O(N \log N)$ time, $O(N)$ space. | Truncating $E_{K-1}(x) = \sum_{c=0}^{K-1} \frac{x^c}{c!}$ restricts each vertex's Prüfer multiplicity $c_i = d_i - 1$ to $[0, K-1]$ inside the $N$-fold EGF product. |
| **`Int-2` (`CF 888G` / Labeled Cactus EGF)** (`L813–815`) | $1 \le N \le 10^5$, Newton precision $m = 1, 2, 4, \dots \le 2N$. | Prime $p = 998244353 > N$, $2 \in \mathbb{F}_p^\times$. | Outputs $n! [x^n] C(x) \bmod p$ for $1 \le n \le N$. | $O(N \log N)$ time, $O(N)$ space. | At Newton step $m \to 2m$, $C^{\bullet}_{2m}(x)$ satisfies $C^{\bullet} \equiv x \exp\!\big(\frac{2C^{\bullet} - (C^{\bullet})^2}{2(1 - C^{\bullet})}\big) \pmod{x^{2m}}$, and dividing $[x^n]C^{\bullet}(x)$ by $n$ unpoints the root vertex. |
| **`Adv-1` (`Luogu P5434` — Labeled Deserts)** (`L883–885`) | $1 \le N \le 10^5$, indices $0 \le n \le N$. | $[x^0]C(x) = 0$, prime $p = 998244353 > N$. | Outputs $n! [x^n] \exp(C(x)) \bmod p$ for $1 \le n \le N$. | $O(N \log N)$ time, $O(N)$ space. | Applying $\exp$ to the unrooted cactus EGF $C(x) = \sum_{n \ge 1} [x^n]C^{\bullet}(x) \frac{x^n}{n}$ assembles unordered sets of connected cactus components into labeled deserts. |
| **`Adv-2` (`CF 1707E` / Block-Cut Degree Constraint)** (`L956–958`) | $1 \le N \le 10^5$, allowed block sizes $S \subseteq [2, N]$. | Prime $p = 998244353 > N$. | Outputs $n! [x^n] C(x) = \frac{1}{n} n! [x^{n-1}] \exp(n E'(x)) \bmod p$. | $O(N \log N)$ time, $O(N)$ space. | By LIF on $R(x) = x \exp(E'(R(x)))$, the single-$n$ extraction $\frac{1}{n}[u^{n-1}]\exp(n E'(u))$ computes $r_n = c_n$ in a single polynomial $\exp$ of degree $n - 1$. |
| **`Mas-1` (`LOJ #6512` / Biconnected Graphs)** (`L1035–1037`) | Single integer $n \le 10^5$ (or all $k \le n$), indices $0 \le j < n$. | Prime $p = 998244353 > n$, $[x^1]R(x) = 1$. | Outputs $b_n = (n-1)! [u^{n-1}] \ln\frac{R(u)}{u} \cdot \left(\frac{u}{R'(u)}\right)^n \bmod p$. | $O(n \log n)$ time, $O(n)$ space. | Applying Form 2 / Variant A of LIF to $R(x) = x \exp(B'(R(x)))$ inverts $u \mapsto R(u)$ at the single degree $n - 1$ using only $\ln$ and $\exp$ without $O(n^2)$ multi-degree composition. |
| **`Mas-2` (`Luogu P5827` — Pointed Tree / 2-Edge-Connected)** (`L1112–1115`) | Single integer $n \le 10^5$, indices $0 \le j < n$. | Prime $p = 998244353 > n$, $[x^1]W(x) = 1$ where $W(x) = R(x)e^{-R(x)}$. | Outputs $e_n = n! [x^n] E_{\text{2ec}}(x) \bmod p$. | $O(n \log n)$ time, $O(n)$ space. | Extracting $[y^{n-1}]\big(R'(y)(1 - R(y))\big) \left(\frac{y}{R(y)e^{-R(y)}}\right)^n$ via a single $\ln/\exp$ yields $n [y^n] R^{\langle -1 \rangle}(y e^{-y})$ in $O(n \log n)$ time. |

#### E. Chapter 13 Practice Ladder (`ch13` L807–1518)
All 8 problems in `ch13` have a `#### Algorithm Contract` subheading (`SS-1` L807, `SS-2` L902, `Int-1` L1000, `Int-2` L1091, `Adv-1` L1176, `Adv-2` L1270, `Mas-1` L1385, `Mas-2` L1510), **but all 8 omit `Preconditions`, `Postconditions`, `Exact Index Boundaries`, and a `1-Sentence Loop Invariant`**.
- **Drop-in Additions for `ch13` Practice Ladder Contracts**:
  1. **`SS-1` (`Luogu P5219` — Bounded-Degree Labeled Trees, `L807`)**:
     - `- **Preconditions**: $2 \le M < N \le 10^5$, prime $p = 998244353 > N$, $[x^0]E_{K-1}(x) = 1$.`
     - `- **Exact Index Boundaries**: $E_{K-1}(x)$ populated for $0 \le c \le K - 1$ and exponentiated modulo $x^{N-1}$ to extract $[x^{N-2}]$.`
     - `- **Loop Invariant**: For each $K \in \{M-1, M\}$, $(N-2)![x^{N-2}]\exp(N \ln E_{K-1}(x))$ counts all Prüfer sequences of length $N - 2$ with symbol frequencies $< K$.`
  2. **`SS-2` (`CF 1109D` — Sasha and Interesting Fact from Graph Theory, `L902`)**:
     - `- **Preconditions**: $1 \le n, m \le 10^6$, prime $p = 10^9 + 7 > \max(n, m)$.`
     - `- **Exact Index Boundaries**: Path edge count $1 \le k \le \min(n - 1, m)$.`
     - `- **Loop Invariant**: At iteration $k \in [1, \min(n-1, m)]$, the $k$-th summand counts all weighted trees in which the unique path between vertices $a$ and $b$ has exactly $k$ edges (forming a super-component of $k + 1$ vertices completed by Generalized Cayley's formula).`
  3. **`Int-1` (`CF 917D` — Stranger Trees, `L1000`)**:
     - `- **Preconditions**: $1 \le n \le 100$, prime $p = 10^9 + 7 > n$.`
     - `- **Exact Index Boundaries**: Interpolation points $x_i = i \in \{1, 2, \dots, n\}$, Laplacian minor size $(n-1) \times (n-1)$, output degrees $0 \le k \le n - 1$.`
     - `- **Loop Invariant**: For each evaluation point $x_i \in \{1, \dots, n\}$, Gaussian elimination computes $y_i = \det L^{(n, n)}(x_i) = \sum_{k=0}^{n-1} c_k x_i^k \bmod p$ in $O(n^3)$ scalar operations.`
  4. **`Int-2` (`Luogu P6624` — `[省选联考 2020 A 卷] 作业题`, `L1091`)**:
     - `- **Preconditions**: $1 \le n \le 30$, $w_i \le 152501$, prime $p = 998244353$.`
     - `- **Exact Index Boundaries**: Divisor $d \in [1, \max w_i]$ with $\ge n - 1$ multiples in $E$; Gaussian elimination over $\mathbb{F}_p[x]/(x^2)$.`
     - `- **Loop Invariant**: For each divisor $d$ with $\ge n - 1$ multiples, pivoting by minimum valuation in $\mathbb{F}_p[x]/(x^2)$ extracts $[x^1]\det L_d^{(n, n)}(x) = \sum_{T \subseteq E_d} \sum_{e \in T} w_e \bmod p$.`
  5. **`Adv-1` (`POJ 1737` / Connected Bipartite & Eulerian EGFs, `L1176`)**:
     - `- **Preconditions**: $1 \le N \le 10^5$, prime $p = 998244353 > N$, exponents $\binom{n}{2}$ reduced modulo $p - 1$.`
     - `- **Exact Index Boundaries**: EGF arrays indexed $0 \le n \le N$; $[x^0]\hat{I}(x) = 1$, $[x^0]B_2(x) = 1$.`
     - `- **Loop Invariant**: Untwisting $\hat{I}(x)^2$ by $2^{\binom{n}{2}}$ at every index $0 \le n \le N$ converts the Chirp-$z$ Cauchy product back into the standard EGF $B_2(x)$ before $\frac{1}{2}\ln B_2(x)$ is called.`
  6. **`Adv-2` (`SPOJ DAGCNT2` / Labeled Connected DAGs & SCCs, `L1270`)**:
     - `- **Preconditions**: $1 \le N \le 10^5$, prime $p = 998244353 > N$, $[x^0]\hat{\Phi}(x) = 1$.`
     - `- **Exact Index Boundaries**: $0 \le n \le N$, with $\binom{n}{2} \bmod (p - 1)$ used for all $2^{\pm\binom{n}{2}}$ twists.`
     - `- **Loop Invariant**: After inverting $\hat{\Phi}(x) = \sum_{k=0}^N (-1)^k 2^{-\binom{k}{2}} \frac{x^k}{k!}$ modulo $x^{N+1}$, multiplying the $n$-th coefficient by $2^{\binom{n}{2}}$ yields the exact DAG EGF coefficient $d_n / n! \bmod p$ before $\ln D(x)$ extracts connected DAGs.`
  7. **`Mas-1` (`Luogu P5206` — `[WC2019] 数树`, `L1385`)**:
     - `- **Preconditions**: $1 \le n \le 10^5$, $y \in [0, 998244353)$, separate guard for $y = 1$ before dividing by $1 - y$.`
     - `- **Exact Index Boundaries**: Component sizes $1 \le s \le n$, EGF truncated to $x^{n+1}$.`
     - `- **Loop Invariant**: In Mode 1, `dp[u][0/1]` tracks the sum of $\prod (w \cdot s_i)$ over all closed components inside $u$'s subtree with $0$ or $1$ marked vertex in $u$'s open component; in Mode 2, $[x^n]\exp\big(\sum_{s=1}^n \frac{n^2 y}{1-y}\frac{s^s}{s!}x^s\big)$ sums over all spanning forests $S$.`
  8. **`Mas-2` (`ABC 287 Ex` / Tensor Product Connected Components, `L1510`)**:
     - `- **Preconditions**: $1 \le K \le 10^5$, $N = \max_i n_i \le 10^5$, prime $p = 998244353 > N$.`
     - `- **Exact Index Boundaries**: Component size $2 \le s \le N$, graph sizes $1 \le n \le N$, coordinate product $1 \le i \le K$.`
     - `- **Loop Invariant**: Convolving $(c_s \pm c_{\text{bip}, s})_{s=2}^N$ with $G(x)$ up to degree $N$ precomputes the single-coordinate component sums $P(n)$ and $Q(n)$ for all $n \in [1, N]$, allowing the $K$-fold tensor sum to factor into $O(K)$ scalar multiplications.`

#### F. Checkpoint III (`cp03-part3-online-implicit-lif-graphs.qmd`)
All 8 problems in `CP-III` (`CP-III.1` L655, `CP-III.2` L742, `CP-III.3` L841, `CP-III.4` L928, `CP-III.5` L996, `CP-III.6` L1078, `CP-III.7` L1164, `CP-III.8` L1266) already have dedicated `::: {.callout-note} ## Algorithm Contract:` boxes with `Input`, `Output`, `Complexity`, and `Core Invariant`! Only minor additions are needed on 4 of the 8 boxes to include an explicit `- **Preconditions**:` bullet:
- `CP-III.2` (`L745`): Add `- **Preconditions**: $a_1 = 1$, prime modulus $p = 998244353$, $2 \in \mathbb{F}_p^\times$.`
- `CP-III.3` (`L844`): Add `- **Preconditions**: Arbitrary prime $p > 2n$; $z = u/(1+u)^2$ has $[u^1]z = 1$.`
- `CP-III.7` (`L1167`): Add `- **Preconditions**: Prime $2 \le p \le 10^5$, $\Phi(0) \not\equiv 0 \pmod p$ ($p \mid n$ allowed).`
- `CP-III.8` (`L1269`): Add `- **Preconditions**: Prime $p = 998244353 > n$; guard $y = 1$ separately before computing $(1 - y)^{-1} \bmod p$.`

---

## Check 3: Canonical Failure Modes Verification (`CURRICULUM_ARCHITECTURE.md` Part III)

### 3.1 Summary Matrix of Part III Canonical Failure Modes

| Chapter | Assigned Failure Modes | Current Coverage in `.qmd` | Action Required |
| :--- | :--- | :--- | :--- |
| **`Ch 09`** | **#13**: Self-Referential CDQ $l = 0$ vs. $l > 0$ missing $2\times$ symmetry factor;<br>Online Relaxed Convolution base-case / `lowbit(q+1)` vs. `lowbit(q)` offset trap | **Covered** (`L240–292` has a dedicated `.callout-warning` box for #13 with numerical trace & code; `L349–436` covers the `lowbit(q+1)` vs `lowbit(q)` offset trap). | Clean up the untagged 0-indexed table at `L321–340` & `"Wait!"` at `L349` (see **Finding 1.1.2**). |
| **`Ch 10`** | Implicit Newton $P_y(0, y_0) = 0$ singularity trap (valuation shift / differentiation first);<br>**#9**: Higher-power $T(x^k)$ ($k \ge 2$) zero-derivative trap;<br>**#8**: Otter's Dissimilarity $T(x^2)$ parity & $A(x)-1$ edge-branch trap | **#9 Covered** (`L365–394` `.callout-warning`);<br>**#8 Covered** (`L546–576` `.callout-warning`);<br>**$P_y(0, y_0) = 0$ Trap**: Explained in prose (`L101–125`, `L178`, `L1334`), **but missing a dedicated `.callout-warning` box in §10.1**! | **Add Drop-in `.callout-warning` Box 3.2.1** at `ch10` L174. |
| **`Ch 11`** | **#5**: Lagrange Inversion Division-by-$n$ Crash when $p \mid n$ (requiring Derivative-Free LIF & Base-$p$ Frobenius LIF);<br>**#16**: Catalan negative upper-index trap at $k = 0$ | **#5 Covered** (`L379–394` `.callout-warning` + full §11.4 `L656–780`);<br>**#16 Covered** (`L535–558` `.callout-warning`).<br>*(Note: Check $k > 1$ coefficient in `ch11` L1305 & `cp03` L485/L1126 — see **Finding 3.2.4** below!)* | **Apply Fix 3.2.4** in `ch11` L1305 and `cp03` L485/L1126 for general $k \ge 1$ when $p \mid n$. |
| **`Ch 12`** | Pointed vs. Unpointed symmetry factor trap;<br>Cactus cycle orientation $\frac{1}{2}$ factor for length $\ge 3$ vs. length $2$ bridges | **Cactus $\frac{1}{2}$ Cycle Trap Covered** (`L225–236` `.callout-warning`);<br>**2-EC vs. 2-VC Trap Covered** (`L481–491` `.callout-warning`);<br>**Pointed vs. Unpointed Trap**: In a `.callout-note` (`L43–59`), needs a `.callout-warning` for the missing $1/n$ unpointing / $\Theta$ trap. | **Add Drop-in `.callout-warning` Box 3.2.2** at `ch12` L59. |
| **`Ch 13`** | **#15**: Robinson's DAG Inclusion–Exclusion Sign Error $(-1)^{k-1}$ vs. $(-1)^{|V|-|S|}$;<br>Chirp-$z$ $2^{-\binom{n}{2}}$ exponent reduction $\bmod (p-1)$ vs. $\bmod p$ | **Chirp-$z$ $\bmod (p-1)$ Trap Covered** (`L197–212` `.callout-warning`);<br>**#15 Robinson DAG Sign Error**: Mentioned briefly in prose (`L333–337`), **missing a dedicated `.callout-warning` box in §13.3**! | **Add Drop-in `.callout-warning` Box 3.2.3** at `ch13` L368. |

---

### 3.2 Drop-In Failure Mode Boxes & Mathematical Precision Fixes

#### Drop-In Box 3.2.1 — `ch10` L174: Implicit Newton Singular Derivative Trap $P_y(0, y_0) = 0$
Insert at `chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd`, line 174:
```markdown
::: {.callout-warning}
## Failure Mode & Remedy: Singular Partial Derivative $\partial_y P(0, y_0) = 0$ in Implicit Newton Iteration

- **The Bug**: Applying the Newton iteration step $A_{2m} = A_m - \frac{P(x, A_m)}{\partial_y P(x, A_m)} \bmod x^{2m}$ directly to an equation where $\partial_y P(0, a_0) = 0$ (for example, writing the Catalan equation as $P(x, C) = x C^2 - C + 1 = 0$ multiplied by $x$, or $P(x, F) = F^2 - x^2(1 + F)^3 = 0$ where $[x^0]\partial_y P = 0$). Because $[x^0]\partial_y P(x, A_m) = 0$, the denominator $\partial_y P(x, A_m)$ is **not a unit** in $K[[x]]$, and `inv(dP_dy)` crashes immediately with a division-by-zero error at $[x^0]$!
- **Why It Happens**: Newton's quadratic convergence $P(x, A_m + \Delta) \equiv P(x, A_m) + \partial_y P(x, A_m)\Delta \pmod{x^{2m}}$ requires dividing by $\partial_y P(x, A_m)$ in $K[[x]] / (x^{2m})$. If $\operatorname{val}(\partial_y P(x, A_m)) = v \ge 1$, every division loses $v$ degrees of precision and cannot invert $[x^0]$.
- **The Remedy**:
  1. **Valuation Shift First ($A(x) = x^v \tilde{A}(x)$)**: Before writing down Newton's step, factor out the exact $x$-valuation $v = \operatorname{val}(A - a_0)$ so that the shifted unknown $\tilde{A}(x)$ satisfies a deflated equation $\tilde{P}(x, \tilde{A}) = 0$ with $\partial_{\tilde{A}} \tilde{P}(0, \tilde{a}_0) \in K^\times$.
  2. **Differentiate with Respect to $x$ First**: If $P_y(0, y_0) = 0$ arises from a higher-multiplicity root or transcendental composition, differentiate $P(x, A(x)) = 0$ with respect to $x$ to obtain a first-order ODE $P_x(x, A) + P_y(x, A) A'(x) = 0$ and clear common powers of $x$ before running Differential Newton Iteration (§10.2).
:::
```

#### Drop-In Box 3.2.2 — `ch12` L59: Pointed vs. Unpointed $1/n$ Symmetry & Unpointing Trap
Insert at `chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`, line 59:
```markdown
::: {.callout-warning}
## Failure Mode & Remedy: The Pointed vs. Unpointed Symmetry & Unpointing Trap

- **The Bug**:
  1. **Unlabeled Trap**: Trying to convert an unlabeled rooted tree OGF $T(x)$ into the unrooted tree OGF $U(x)$ by dividing $[x^n]T(x)$ by $n$ (as if all $n$ vertices had distinct orbits). Because an unlabeled tree $\tau$ can have non-trivial automorphisms ($\lvert \operatorname{Aut}(\tau) \rvert > 1$), a single unrooted unlabeled tree of size $n$ does **not** correspond to $n$ rooted unlabeled trees—it requires **Otter's Dissimilarity Theorem** $U(x) = T(x) - \frac{1}{2}T(x)^2 + \frac{1}{2}T(x^2)$ ([Chapter 10.4](ch10-implicit-equations-newton-unlabeled-trees-otter.qmd))!
  2. **Labeled Trap**: Solving a rooted block-cut or cactus grammar for the **pointed** EGF $C^{\bullet}(x) = x C'(x)$ and then passing $C^{\bullet}(x)$ directly into $\exp\big(C^{\bullet}(x)\big)$ to count forests or deserts (instead of first integrating $C(x) = \int \frac{C^{\bullet}(x)}{x}\,dx$, i.e., dividing $[x^n]C^{\bullet}(x)$ by $n$ to unpoint each connected component before applying `SET` = $\exp$!).
- **The Remedy**: Always track whether your EGF is **pointed** ($A^{\bullet}(x) = \Theta A(x) = x A'(x)$, where each component carries $n$ choices of a distinguished root vertex) or **unpointed** ($A(x) = \int \frac{A^{\bullet}(x)}{x}\,dx$). You must **unpoint** ($[x^n]A(x) = \frac{1}{n}[x^n]A^{\bullet}(x)$) *before* applying $\exp(A(x))$ to form multi-component graphs!
:::
```

#### Drop-In Box 3.2.3 — `ch13` L368: Canonical Failure Mode #15 (Robinson's DAG Inclusion–Exclusion Sign Error)
Insert at `chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd`, line 368:
```markdown
::: {.callout-warning}
## Failure Mode #15: Robinson's DAG Inclusion–Exclusion Sign Error $(-1)^{k-1}$ vs. $(-1)^{\lvert V \rvert - \lvert S \rvert}$

- **The Bug**:
  1. **Sign Confusion in the Recurrence vs. the EGF Denominator**: In Robinson's recurrence for $n \ge 1$, the inclusion–exclusion weight for choosing $k \ge 1$ sources has sign $(-1)^{k-1}$:
     $$d_n = \sum_{k=1}^{n} (-1)^{k-1} \binom{n}{k} 2^{k(n-k)} d_{n-k}.$$
     When moving all terms to the left-hand side to form the twisted convolution $\hat{D}(x) \hat{\Phi}(x) = 1$, the signs for $k \ge 1$ **flip** from $(-1)^{k-1}$ to $-(-1)^{k-1} = (-1)^k$! A frequent contest bug is to define $\hat{\Phi}(x) = 1 + \sum_{k \ge 1} (-1)^{k-1} 2^{-\binom{k}{2}} \frac{x^k}{k!}$ (which has $+x$ instead of $-x$) and call `inv`, producing garbage from $n = 1$ onward!
  2. **Subset-Complement Sign Error $(-1)^{n - k}$**: Writing the sign as $(-1)^{n - k}$ (the parity of the non-source complement $V \setminus S$) instead of $(-1)^{k - 1}$ (the parity of the chosen source subset $S$). Because inclusion–exclusion is performed over the non-empty subsets $S \subseteq \operatorname{Sources}(G)$, the weight depends **only on $k = \lvert S \rvert$**, never on $n - k$.
- **The Remedy**: Memorize the exact sign test at $k = 0$ and $k = 1$: in $\hat{\Phi}(x) = \sum_{k=0}^{N} (-1)^k 2^{-\binom{k}{2}} \frac{x^k}{k!}$, we have $[x^0]\hat{\Phi}(x) = +1$ and $[x^1]\hat{\Phi}(x) = -1$, so that $\hat{\Phi}(x)^{-1} = 1 + x + \dots$ has $+1$ at $[x^1]$ ($d_1 = 1$ DAG on $1$ vertex). Always verify $d_1 = 1, d_2 = 3, d_3 = 25$ before submitting!
:::
```

#### Important Mathematical Note 3.2.4 — `ch11` L1305 & `cp03` L485 / L1124: Derivative-Free LIF Formula for $[x^n] F(x)^k$ When $k > 1$ and $p \mid n$
- **Location**:
  - `chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd`, lines 707–711 and 1300–1318 (`Adv-2`: `Luogu P8555`)
  - `checkpoints/cp03-part3-online-implicit-lif-graphs.qmd`, lines 485 and 1122–1127 (`CP-III.7`: `Luogu P8555`)
- **Mathematical Audit**:
  Look closely at the change of variables $u = F(x) \iff x = \frac{u}{\Phi(u)}$ with $dx = \frac{\Phi(u) - u\Phi'(u)}{\Phi(u)^2}\,du$ applied to $[x^n] H(F(x))$ when $H(u) = u^k$:
  $$\begin{aligned}
  [x^n] F(x)^k &= \operatorname{res}_x \Big( F(x)^k x^{-n-1} \, dx \Big) \\
  &= \operatorname{res}_u \left( u^k \left(\frac{\Phi(u)}{u}\right)^{n+1} \frac{\Phi(u) - u\Phi'(u)}{\Phi(u)^2} \, du \right) \\
  &= \operatorname{res}_u \Big( u^{-(n - k) - 2} \big(\Phi(u) - u\Phi'(u)\big) \Phi(u)^{n - 1} \, du \Big) \\
  &= [u^{n - k + 1}] \Big( \big(\Phi(u) - u\Phi'(u)\big) \Phi(u)^{n - 1} \Big) \quad (\text{Wait: check the exponent of } u\text{!})
  \end{aligned}$$
  Let's check the exponent of $u$ carefully!
  In $u^k \cdot u^{-n-1} = u^{k - n - 1} = u^{-(n - k) - 1}$, the exponent of $u$ is indeed $-(n - k) - 1$, whose residue $\operatorname{res}_u(u^{-(n-k)-1} \dots du)$ is $[u^{n-k}]\big((\Phi(u) - u\Phi'(u))\Phi(u)^{n-1}\big)$!
  Now let us test if $[x^n] F(x)^k = [u^{n-k}]\big((\Phi(u) - u\Phi'(u))\Phi(u)^{n-1}\big)$ is true for $k = 2, n = 3$, and $\Phi(u) = 1 + u$ (where $F(x) = \frac{x}{1-x}$, so $F(x)^2 = \frac{x^2}{(1-x)^2} = x^2 + 2x^3 + 3x^4 + \dots$, meaning $[x^3] F(x)^2 = \mathbf{2}$):
  - What does $[u^{n-k}]\big((\Phi(u) - u\Phi'(u))\Phi(u)^{n-1}\big)$ give for $n = 3, k = 2, \Phi(u) = 1 + u$?
    Here $\Phi(u) - u\Phi'(u) = (1 + u) - u(1) = 1$, and $\Phi(u)^{n-1} = (1 + u)^2 = 1 + 2u + u^2$.
    Extracting $[u^{3-2}] = [u^1]$ gives $[u^1](1 \cdot (1 + 2u + u^2)) = \mathbf{2}$!
  - What about $n = 4, k = 2, \Phi(u) = 1 + u$?
    $[x^4] F(x)^2 = 3$. And $[u^{4-2}](1 \cdot (1+u)^3) = [u^2](1 + 3u + 3u^2 + u^3) = \mathbf{3}$!
  - Why did that work without any $k$ factor?! Because $\operatorname{res}_x(H(F(x)) x^{-n-1} dx) = [u^n]\big(H(u)(1 - u\Phi'(u)/\Phi(u))\Phi(u)^n\big)$ is **Canonical Form 4** (`ch11` L241: $[x^n]H(F(x)) = [u^n]\big(H(u)\frac{\Phi(u) - u\Phi'(u)}{\Phi(u)}\Phi(u)^n\big)$), and when $H(u) = u^k$, $[u^n]\big(u^k (\Phi(u) - u\Phi'(u))\Phi(u)^{n-1}\big) = [u^{n-k}]\big((\Phi(u) - u\Phi'(u))\Phi(u)^{n-1}\big)$!
  - **HOWEVER**, look at `ch11` L709 (in §11.4):
    In `ch11` L709, the author wrote:
    $$[x^n] F(x)^k = [u^{n-k}] \Big( k \big(\Phi(u) - u \Phi'(u)\big) \Phi(u)^{n-1} \Big) \quad \text{(for } k = 1\text{, simply } [u^{n-1}]\big((\Phi(u) - u\Phi'(u))\Phi(u)^{n-1}\big)\text{!)}$$
    Notice the extra factor of $k$ in `ch11` L709! For $k > 1$, multiplying by $k$ in `ch11` L709 is **WRONG** by a factor of $k$ (as our test $n = 3, k = 2, \Phi(u) = 1+u$ just proved: without $k$ it gives the true answer $2$, whereas with $k$ it would give $2 \times 2 = 4$)!
    Meanwhile, in `ch11` L1305 (`Adv-2`) and `cp03` L485 / L1126 (`CP-III.7`), the author wrote $[u^{n-k}]\big((\Phi(u) - u\Phi'(u))\Phi(u)^{n-1}\big)$ **without** $k$, which is **100% mathematically TRUE** for all $k \ge 1$!
  - **Drop-in Fix for `ch11` L705–712**: Remove the erroneous factor of $k$ in `ch11` L709 and cite Canonical Form 4 ($H(u) = u^k$):
  ```markdown
  Instead of Form 1 (which divides by $n$), we use **Canonical Form 4 (Derivative-Free Residue Form)** with $H(u) = u^k$:

  $$
  [x^n] F(x)^k = [u^n] \Big( u^k \big(\Phi(u) - u \Phi'(u)\big) \Phi(u)^{n-1} \Big) = [u^{n-k}] \Big( \big(\Phi(u) - u \Phi'(u)\big) \Phi(u)^{n-1} \Big).
  $$
  ```
  And in `ch11` L1304 (`Adv-2`), remove the `"Wait:"` self-correction and refer directly to Canonical Form 4 with $H(u) = u^k$.

---

## Check 4: Quarto & Pandoc Markdown Syntax Verification

### 4.1 Display Math Blocks Ending with Emphatic `!` (`!$$` or `!\n$$`) — 31 Instances

In LaTeX/MathJax, placing an exclamation mark `!` immediately before the closing `$$` of a display equation renders a **factorial symbol** (`!`) inside the math equation! All **31 instances** below must have the trailing `!` changed to `.` (or moved outside the `$$` block):

#### 1. `chapters/ch09-cdq-fft-online-relaxed-convolution.qmd` (8 instances)
- **L375**: `q + 1 - 2\ell = \ell \cdot (2k) \ge 0\text{!}` $\to$ `q + 1 - 2\ell = \ell \cdot (2k) \ge 0.`
- **L550**: `g_n = \sum_{d \mid n} d \, a_d \quad (n \ge 1)!` $\to$ `g_n = \sum_{d \mid n} d \, a_d \quad (n \ge 1).`
- **L721**: `E_{e, t} = \sum_{k=1}^{T - t} p_{e, k} \, D_{v, t + k} + \text{rem}_{e, t} \, D_{v, T + 1}!` $\to$ `E_{e, t} = \sum_{k=1}^{T - t} p_{e, k} \, D_{v, t + k} + \text{rem}_{e, t} \, D_{v, T + 1}.`
- **L882**: `t_n = \frac{1}{n - 1} \sum_{i=1}^{n-1} t_i \, g_{n - i} \quad (n \ge 2)!` $\to$ `t_n = \frac{1}{n - 1} \sum_{i=1}^{n-1} t_i \, g_{n - i} \quad (n \ge 2).`
- **L1261**: `[x^N] \sum_{m=0}^{N} \left(R_1(x)\right)^{2m} = [x^N] \frac{1}{1 - R_1(x)^2}!` $\to$ `[x^N] \sum_{m=0}^{N} \left(R_1(x)\right)^{2m} = [x^N] \frac{1}{1 - R_1(x)^2}.`
- **L1277**: `A(x) = \sum_{n=0}^{\infty} a_n \frac{x^n}{n!} = \frac{1}{1 - \sum_{k \ge 1} (-1)^{k-1} \frac{x^k}{k!}} = \frac{1}{1 - (1 - e^{-x})} = e^x? \text{ No: } (-1)^{k-1} \text{ gives } 1 - (1 - e^{-x}) = e^{-x}? \text{ Let's check signs!}` $\to$ Replace L1266–1296 per **Finding 1.2**.
- **L1286**: `A(x) = \frac{1}{1 - (e^x - 1)} = \frac{1}{2 - e^x}!` $\to$ `A(x) = \frac{1}{1 - (e^x - 1)} = \frac{1}{2 - e^x}.`
- **L1296**: `N! [x^N] \frac{A(x)^2}{1 - (A(x) - 1)^2} = N! [x^N] \frac{A(x)^2}{2 A(x) - A(x)^2} = N! [x^N] \frac{A(x)}{2 - A(x)}!` $\to$ `N! [x^N] \frac{A(x)^2}{1 - (A(x) - 1)^2} = N! [x^N] \frac{A(x)^2}{2 A(x) - A(x)^2} = N! [x^N] \frac{A(x)}{2 - A(x)}.`

#### 2. `chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd` (7 instances)
- **L166**: `= \left(1 + x + 2x^2 + 5x^3\right) + \left(14x^4 + 42x^5 + 132x^6 + 429x^7\right) \pmod{x^8}!` $\to$ remove `!`
- **L351**: `\ln \frac{T(x)}{x} = \sum_{k=1}^{\infty} \frac{T(x^k)}{k} \iff T(x) = x \exp\!\left(\sum_{k=1}^{\infty} \frac{T(x^k)}{k}\right)!` $\to$ remove `!`
- **L393**: `\partial_y P(x, T_m) = 1 - T_m(x) \pmod{x^{2m}}!` $\to$ remove `!`
- **L429**: `= x + x^2 + 2x^3 + 4x^4 + 9x^5 + 20x^6 + 48x^7 + O(x^8)!` $\to$ remove `!`
- **L966**: `P(x, y) \cdot F(x, y) = y^{d_2} - x \sum_{r=0}^{d_2 - 1} F_r(x) \left(y^{d_2} - y^r\right)!` $\to$ remove `!`
- **L1150**: `\sum_{m=2}^{\infty} \left(F(x) - F_{\text{inc}}(x)\right)^m = \frac{(F - F_{\text{inc}})^2}{1 - (F - F_{\text{inc}})}!` $\to$ remove `!`
- **L1268**: `[x^k] B(x) = [x^k] T(x) \quad \text{for all } 1 \le k \le M!` $\to$ remove `!`

#### 3. `chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd` (16 instances)
- **L487**: `u = z (1 + u)^t \iff z = u (1 + u)^{-t}!` $\to$ remove `!`
- **L524**: `= [u^n] \left( A(u) \, (1 + u)^{r + t n} \right)!` $\to$ remove `!`
- **L689**: `[u^2] (1 + u)^3 = \binom{3}{2} = 3 \equiv 0 \pmod 3!` $\to$ remove `!`
- **L711**: `(for $k = 1$, simply $[u^{n-1}]\big((\Phi(u) - u\Phi'(u))\Phi(u)^{n-1}\big)$!)` $\to$ see **Fix 3.2.4**.
- **L728**: `\Phi(u)^p \equiv \sum_{i=0}^{d} c_i^p u^{p i} \equiv \sum_{i=0}^{d} c_i u^{p i} = \Phi(u^p) \pmod p!` $\to$ remove `!`
- **L931**: `[u^n] \left( R(u) \frac{1 - u}{1 + u} (1 + u)^{2n} \right)!` $\to$ remove `!`
- **L1069**: `-\frac{1}{z} Q(z)^{-1} = -\frac{1}{z} \sum_{m=0}^{\infty} q_m z^m \implies [z^j] \big(1 - P(z)\big)^{-1} = -q_{j+1}!` $\to$ remove `!`
- **L1262**: `\text{Ans} = \sum_{j=1}^{\min(n, k)} \left\{\begin{matrix} k \\ j \end{matrix}\right\} n^{\underline{j}} \, (n + 1)^{n - j} \pmod{998244353}!` $\to$ remove `!`
- **L1370**: `\text{Answer} = A(0) = 1 \pmod 3!` $\to$ remove `!`
- **L1476, L1481, L1492, L1506, L1527, L1531, L1535**: 7 equations in `Mas-1` (`Luogu P5853`) ending with `!` $\to$ remove `!` from all 7 equations.

*(Note: `ch12`, `ch13`, and `cp03` have **zero** `!$$` instances!)*

---

### 4.2 Broken Internal `.qmd` Links — 5 Instances

| File & Line | Current Markdown Link | Issue | Drop-in Replacement |
| :--- | :--- | :--- | :--- |
| `ch12` L358 | `[Chapter 21](ch21-kinoshita-li-composition-power-projection-revert.qmd)` | Target file `ch21-...qmd` does not exist yet in `chapters/` (Part V is not yet rendered). | Change to bold text `**Chapter 21 (Kinoshita–Li Fast Composition & Power Projection)**` until Part V files are created, or ensure exact filename match when `ch21` is created. |
| `ch13` L5 | `[Chapter 12](ch12-pointed-trees-cacti-block-cut-tutte.qmd)` | **Broken slug!** Actual Chapter 12 filename is `ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`. | `[Chapter 12](ch12-cacti-deserts-block-cut-biconnected-graphs.qmd)` |
| `ch13` L27 | `[Chapter 12](ch12-pointed-trees-cacti-block-cut-tutte.qmd)` | **Broken slug!** Same wrong slug for Chapter 12. | `[Chapter 12](ch12-cacti-deserts-block-cut-biconnected-graphs.qmd)` |
| `ch13` L685 | `[Chapter 24](ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd)` | Target file `ch24-...qmd` does not exist yet in `chapters/`. | Change to bold text `**Chapter 24 (Bitwise FWT, Set Power Series & Dirichlet GFs)**` until Part V is created. |
| `ch13` L1525 | `[Chapter 14](ch14-stirling-eulerian-bernoulli-poly-interp.qmd)` | **Wrong Chapter 14 slug & topic!** Actual Chapter 14 file is `ch14-pgf-stopping-times-renewal-poisson-martingales.qmd`. | `[Chapter 14](ch14-pgf-stopping-times-renewal-poisson-martingales.qmd)` |

---

### 4.3 Other Quarto & Pandoc Checks (100% Clean)
- **Forbidden Math Delimiters (`\(` or `\[`)**: **0 instances** across all 6 files.
- **Unescaped `|` Inside `$...$` in Markdown Tables**: **0 instances** across all 6 files (`ch11` L161 and `cp03` L578 properly use `\lvert ... \rvert`).
- **Blank Lines After `<summary>` and Before `</details>`**: **100% compliant** across all 192 `<details>` blocks in Part III (`ch09` [32], `ch10` [32], `ch11` [32], `ch12` [32], `ch13` [32], `cp03` [33]).
- **Balanced `:::` Callout Fences and `<details>` Tags**: **100% balanced** across all 6 files.
- **Blind Checkpoint `CP-III` Stage 1 Spoiler-Free Compliance**: **100% compliant** — Stage 1 problem statements, hand-checkable traces, and `Hint 1` blocks contain zero chapter numbers and zero spoiler paradigm names.
