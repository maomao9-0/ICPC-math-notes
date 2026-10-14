# Phase 3 Iteration 8 Global Specialist Audit: Blind Checkpoint Spoiler-Free Design & Progressive Hints Quality (`CP-I`–`CP-VI` & `capstones/synthesis-reserve.qmd`)

**Auditor**: `fps-textbook-critic` (Phase 3 Iteration 8 Global Specialist Critic)  
**Target Files Audited (100% Line-by-Line Read — 8,359 Total Lines)**:
1. [`checkpoints/cp01-part1-foundations.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd) (`1,033` lines)
2. [`checkpoints/cp02-part2-rational-transforms-ie.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd) (`1,288` lines)
3. [`checkpoints/cp03-part3-online-implicit-lif-graphs.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp03-part3-online-implicit-lif-graphs.qmd) (`1,290` lines)
4. [`checkpoints/cp04-part4-pgf-walks-multivariate.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd) (`992` lines)
5. [`checkpoints/cp05-part5-dfinite-transposition-composition.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp05-part5-dfinite-transposition-composition.qmd) (`837` lines)
6. [`checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd) (`914` lines)
7. [`capstones/synthesis-reserve.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/synthesis-reserve.qmd) (`2,005` lines)

---

## Executive Summary & Verdict Matrix

| Audit Dimension | Status | Summary of Findings |
| :--- | :-: | :--- |
| **1. Zero Topic Spoilers in Stage 1 & `Hint 1` (`CP-I`–`CP-VI`)** | **ACTION REQUIRED (`8` Spoilers Found)** | Out of 48 Blind Checkpoint problems, 42 are completely spoiler-free in Stage 1 and `Hint 1`. However, **8 concrete Stage 1 / `Hint 1` spoilers** remain across `cp01`, `cp03`, `cp04`, and `cp05` (detailed in §1 below with drop-in replacements). In addition, `Hint 2` naming is inconsistent between `CP-I..IV` (which reveal home chapters in `Hint 2`) and `CP-V..VI` (which defer chapter numbers to `Stage 2`). |
| **2. Self-Contained Inline Statements, Constraints & Sample Traces (`CP-I`–`CP-VI` + `Syn-01`–`Syn-14`)** | **PASS WITH `2` FIXES** | All 48 Blind Checkpoint problems and all 14 Synthesis Reserve problems (`Syn-01`–`Syn-14`) match `CURRICULUM_ARCHITECTURE.md` 100% by ID and slot, and all 62 problems feature inline statements, explicit constraints/moduli, and visible $N \le 4$ sample traces before `<details>`. Two problems (`CP-I.3` and `CP-V.7`) bake algebraic reductions into their Stage 1 problem statements and require clean combinatorial rewrites (§2). |
| **3. 3-Stage Progressive Hints & Complete Solutions with 5-Part Algorithm Contracts** | **ACTION REQUIRED (`3` Structural Issues)** | (a) In `cp04-part4-pgf-walks-multivariate.qmd` (`Lines 518–976`), all 8 Stage 2 solutions (`CP-IV.1`–`CP-IV.8`) are trapped inside a **single monolithic `<details>` block** instead of 8 individual per-problem `<details>` blocks. (b) Layout split: `cp01`/`cp02` place the 4th `<details>` solution block inline under `Hint 3` of each problem, whereas `cp03`–`cp06` place solutions in a separate Stage 2 section at the bottom of the file. (c) In `cp01`, `cp02`, `cp03`, `cp05`, and `capstones/synthesis-reserve.qmd`, the `Algorithm Contract` bullet list omits the 5th mandatory bullet (`Failure Modes & Edge Cases`), either placing it in an external callout box (`cp01`–`cp03`, `synthesis-reserve.qmd`) or omitting it from the solution block entirely (`cp05`). |
| **4. 12 Revisited Dual-Perspective Cross-Studies in `capstones/synthesis-reserve.qmd`** | **ACTION REQUIRED (`2` Gaps Found)** | `capstones/synthesis-reserve.qmd` §3 (`Lines 1954–2004`) includes Table 3.1 covering the 12 Revisited problems from `CURRICULUM_ARCHITECTURE.md` §5.2 (`#101, #084, #040, #094, #089, #023, #244, #200, #183, #156, #220, #058`), but only provides prose callout walk-throughs for **5 of the 12** (`#101, #023, #244, #200, #058`), leaving 7 problems as 1-line table entries. Furthermore, we audit and provide drop-in Dual-Perspective Cross-Study blocks for the 10 additional cross-chapter Revisited threads from the Iteration 8 specification (`#011, #037, #074, #076, #107, #110, #169, #185, #226, #237`). |
| **5. Quarto Formatting & Hygiene Sweep** | **100% PASS (`0` Violations)** | Zero forbidden `\(` or `\[` math delimiters, zero `!$$` or `![x^` strings, zero unescaped `|` inside `$...$` in Markdown tables, zero raw `"Wait"` strings, zero C++/Python code blocks $> 15$ inner lines, and 100% balanced `<details>` and `:::` blocks with blank lines after every `</summary>` and before every `</details>`. |

---

## 1. Checklist 1: Zero Topic Spoilers in Stage 1 & `Hint 1` Across All 48 Blind Checkpoint Problems (`CP-I`–`CP-VI`)

### 1.1 Detailed List of Stage 1 & `Hint 1` Spoilers (`8` Findings)

#### Finding 1.1 (`HIGH` — Pre-Stage-1 Chapter & Formula Spoilers in `cp01-part1-foundations.qmd`, Lines 22–90)
- **Location**: [`checkpoints/cp01-part1-foundations.qmd:22-90`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L22-L90)
- **What Is Wrong**: Section 1 (`## 1. The Part I 3-Axis Diagnostic Rubric`) appears **visibly above Stage 1** (`Lines 22–90`) and explicitly names target chapters and exact problem-specific generating function formulas before the student even reads the blind problem statements:
  - `Lines 32–46` (Mermaid chart) and `Lines 57, 67, 73, 76, 88–89` explicitly cite `Chapters 01 & 03`, `Chapter 01`, `Chapter 04 §4.3`, `Chapter 03`, `Pólya cycle index over \lambda \vdash N`, `\ln(1+x) connected-component sieve`, `(1+x)^A(1-x)^{-B}(1-x^d)^{-C}`, and `\prod(1+x^{w_k})`.
  - Compare with `cp02` (`Lines 57–111`), which properly wraps its Diagnostic Decision Tree inside a collapsible `<details>` block (`Click to Reveal Part II Diagnostic Decision Tree (Read AFTER Attempting Stage 1)`).
- **Drop-In Fix**: Wrap `Lines 24–90` of `checkpoints/cp01-part1-foundations.qmd` inside a collapsible `<details>` block (or remove explicit chapter numbers and problem-specific formulas from the visible rubric):

```markdown
<details>
<summary><strong>Click to Reveal Part I 3-Axis Diagnostic Rubric (Read AFTER Attempting Stage 1 Blind Diagnosis)</strong></summary>

*(keep existing lines 24–90 here)*

</details>
```

---

#### Finding 1.2 (`CRITICAL` — Stage 1 Problem Statement Spoils the Decomposition & Formula in `CP-I.3`, Lines 314–327)
- **Location**: [`checkpoints/cp01-part1-foundations.qmd:314-327`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L314-L327)
- **What Is Wrong**: In `CP-I.3` (`#246`, `HDU 5279 — YJC plays minecraft`), the visible **Problem Statement** (`Lines 318–327`) does not state the raw graph problem; instead, it decomposes the problem into two solved sub-steps (`1. Part A (Connected Labeled Subgraphs of Each Clique)` and `2. Part B (Weighted Circular Arc Partitions)`) and **hands the reader the exact intermediate formula** $(N+1)\prod_{i=1}^m c_{a_i}$ right inside the problem statement!
- **Drop-In Fix** (Replace `Lines 314–327` of `checkpoints/cp01-part1-foundations.qmd`):

```markdown
**Problem Statement**:  
In a blocky world, $N$ islands are arranged in a circle in clockwise order $1, 2, \dots, N$ (with island $N$ adjacent to island $1$). The $i$-th island contains $a_i$ labeled vertices ($1 \le a_i \le N$) with all $\binom{a_i}{2}$ internal edges initially present (forming a complete graph $K_{a_i}$). Additionally, between each pair of adjacent islands $i$ and $(i \bmod N) + 1$, there is a single bridge edge connecting a designated port vertex of island $i$ to a designated port vertex of island $(i \bmod N) + 1$.

You may delete any subset of internal island edges and any subset of the $N$ circular bridge edges, subject to two rules:
1. For each island $i \in \{1, \dots, N\}$, the remaining internal edges on island $i$ must keep all $a_i$ vertices of island $i$ **connected**;
2. You must delete **at least one** of the $N$ circular bridge edges, throwing the circle into $m \ge 1$ contiguous circular arcs of sizes $s_1, s_2, \dots, s_m \ge 1$ ($\sum_{r=1}^m s_r = N$), and the weight of a configuration with arc sizes $s_1, \dots, s_m$ is multiplied by $(N+1) \prod_{r=1}^m c_{s_r}$, where $c_k$ is the number of connected labeled graphs on $k$ vertices.

Wait—equivalently, in the canonical two-phase formulation of **HDU 5279**: first determine $c_k$ (the number of connected labeled graphs on $k$ vertices) for all $1 \le k \le N$, and then compute the total weight of all ways to cut the $N$-island cycle into $m \ge 1$ contiguous circular arcs of lengths $s_1, \dots, s_m \ge 1$ where an arc of length $s$ carries weight $c_s$, all modulo $998244353$.
```
*(Better yet, avoid any `"Wait"` string: state the exact two-rule HDU 5279 circular block-splitting problem cleanly without naming `Part A`/`Part B`.)* Here is the exact zero-`"Wait"` drop-in replacement for `Lines 314–327`:

```markdown
**Problem Statement**:  
A circular ring consists of $N$ unit slots numbered $0, 1, \dots, N-1$ around a circle, with $N$ unit boundary edges separating adjacent slots. A valid configuration consists of choosing a non-empty subset of boundary edges to cut, partitioning the circle into $m \ge 1$ contiguous circular arcs of integer lengths $a_1, a_2, \dots, a_m \ge 1$ ($\sum_{i=1}^m a_i = N$), and building an independent **connected simple graph** on $a_i$ labeled vertices inside the $i$-th arc for each $i = 1, \dots, m$ (with an overall circular multiplier of $N+1$ given by the problem's block rules).

Two configurations are distinct if they cut a different non-empty subset of the $N$ circular boundary edges or choose a different connected simple graph on the labeled vertices of any resulting arc. Compute the total weighted count of valid configurations modulo $998244353$.
```

---

#### Finding 1.3 (`HIGH` — Stage 1 Title, Statement & `Hint 1` Spoil Modular Decomposition / 析合树 in `CP-III.4`, Lines 253, 259, 281–284)
- **Location**: [`checkpoints/cp03-part3-online-implicit-lif-graphs.qmd:253-286`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp03-part3-online-implicit-lif-graphs.qmd#L253-L286)
- **What Is Wrong**:
  1. `Line 253` (Stage 1 Title): `### Problem CP-III.4: Simple Permutations (`#160` — Luogu P4747 / CERC 2017 Intrinsic Interval — Classic Modular Decomposition / 析合树 Enumeration Benchmark)` explicitly names `Modular Decomposition / 析合树` in the title!
  2. `Line 259` (Stage 1 Statement): `A permutation $\pi \in S_n$ is called **simple** (or **interval-indecomposable**, corresponding to a prime node / 析点 in the permutation modular decomposition tree) if...` explicitly names `prime node / 析点 in the permutation modular decomposition tree`.
  3. `Lines 281–284` (`Hint 1`): Explicitly names the three modular decomposition node types `1. Ascending Join (升序合点)`, `2. Descending Join (降序合点)`, and `3. Simple Quotient (析点)` inside `Hint 1`!
- **Drop-In Fix** (Replace `Lines 253–262` and `Lines 276–287` of `checkpoints/cp03-part3-online-implicit-lif-graphs.qmd`):

```markdown
### Problem CP-III.4: Simple Permutations (`#160` — Luogu P4747 / CERC 2017 Intrinsic Interval Enumeration)

**Problem Statement**:  
A permutation $\pi = (\pi_1, \pi_2, \dots, \pi_n)$ of $\{1, 2, \dots, n\}$ is called a **framed interval** (or **block**) if every contiguous subarray $\pi[l..r]$ takes a contiguous set of values $\{\min \pi[l..r], \dots, \max \pi[l..r]\}$ if and only if $\max \pi[l..r] - \min \pi[l..r] = r - l$. Every permutation trivially has blocks of length $1$ (singletons) and length $n$ (the whole permutation).

A permutation $\pi \in S_n$ is called **simple** (or **interval-indecomposable**) if it has **no** block of length $k$ with $2 \le k \le n-1$. Given $N$, compute the number of simple permutations $s_n$ for **all** $1 \le n \le N$ modulo $998244353$.
```

And for `Hint 1` (`Lines 276–287`):

```markdown
<details>
<summary><strong>Hint 1 — Combinatorial Decomposition (Zero Spoilers)</strong></summary>

Instead of directly counting permutations that *avoid* all non-trivial contiguous value blocks, consider how an arbitrary permutation $\pi \in S_n$ ($n \ge 2$) is built by inflating a smaller base permutation $\sigma \in S_m$ ($m \ge 2$) with $m$ contiguous value blocks $B_1, B_2, \dots, B_m$. When is this inflation decomposition unique, and what special case arises when $\sigma$ itself can be split into two monotone pieces?

</details>
```

---

#### Finding 1.4 (`MEDIUM` — Stage 1 Constraints Spoil the FPS Framing in `CP-III.6`, Line 384)
- **Location**: [`checkpoints/cp03-part3-online-implicit-lif-graphs.qmd:382-385`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp03-part3-online-implicit-lif-graphs.qmd#L382-L385)
- **What Is Wrong**: Under **Constraints** in Stage 1 (`Line 384`), the bullet reads:
  `- *General Upper-Bound FPS Variant*: Also analyze how to solve the generalized version where the upper cap on $A_i$ is an arbitrary given sequence $B_i$ with $\sum_{i=1}^N B_i \le 2 \times 10^5$!`
  Calling it `General Upper-Bound FPS Variant` in Stage 1 gives away the FPS product modeling.
- **Drop-In Fix** (Replace `Line 384` of `checkpoints/cp03-part3-online-implicit-lif-graphs.qmd`):

```markdown
- *Generalized Cap Subtask*: Also analyze how to solve the version where the upper cap $\min(i, A_i)$ is replaced by $\min(B_i, A_i)$ for an arbitrary given positive integer array $B_1, \dots, B_N$ with $\sum_{i=1}^N B_i \le 2 \times 10^5$.
```

---

#### Finding 1.5 (`CRITICAL` — Stage 1 Overview Table, Title & Statement Spoil the Fuss–Catalan Functional Equation in `CP-IV.7`, Lines 37, 368–390)
- **Location**: [`checkpoints/cp04-part4-pgf-walks-multivariate.qmd:37`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L37) and [`checkpoints/cp04-part4-pgf-walks-multivariate.qmd:368-390`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L368-L390)
- **What Is Wrong**:
  1. In the Stage 1 Overview Table (`Line 37`), `CP-IV.7` is described as: `Given p, q, n, a \le 2 \times 10^5, extract [x^{pn+a} y^n] (1 - x - y)^{-1} and Fuss–Catalan series.`
  2. In the Stage 1 Problem Title (`Line 368`) and Problem Statement (`Lines 370–389`), Part (b) explicitly gives the reader the Fuss–Catalan implicit equation $w(t) = \frac{t}{(1 - w(t))^p}$ and the exact Jacobian denominator $[t^n] \frac{A(w(t))}{1 - (p+1)w(t)}$ in Stage 1! That completely gives away the Furstenberg residue / Fuss–Catalan substitution before `Hint 1`.
- **Drop-In Fix** (Replace `Line 37` and `Lines 368–390` of `checkpoints/cp04-part4-pgf-walks-multivariate.qmd`):
  - For `Line 37`:
    `| **CP-IV.7** | `#243` | **yukicoder 2104 — Asymmetric Lattice Paths** | Given $p, n, a \le 2 \times 10^5$, count $2\text{D}$ lattice paths from $(0,0)$ to $(pn+a, n)$ avoiding or touching the line $x = py + a$, and evaluate the weighted path sum for general step weights. |`
  - For `Lines 368–390`:

```markdown
### Problem CP-IV.7: Asymmetric Lattice Path & $(p+1)$-ary Tree Enumeration (`#243` — yukicoder 2104)

**Statement.** Fix an integer slope parameter $p \ge 1$ and an offset $a \ge 0$. Consider lattice paths in $\mathbb{Z}_{\ge 0}^2$ starting at $(0, 0)$ and taking unit steps $(1, 0)$ (East) and $(0, 1)$ (North) to $(pn + a, n)$:

1. **(a) Unconstrained & Boundary-Constrained Slope-$p$ Paths**: Every path to $(pn+a, n)$ corresponds to picking the $n$ vertical step positions among $(p+1)n + a$ total steps. How many such paths never cross above the line $x - py = a$, and how does the sum over all $n \ge 0$ of the unconstrained path counts $\binom{(p+1)n + a}{n} t^n$ relate to the constrained path counts?
2. **(b) Weighted Return Series**: Given a polynomial $A(z) = \sum_{k=0}^d a_k z^k$ encoding the weight $a_k$ of decomposing a path into $k$ primitive boundary-returning excursions, compute the weighted total over all unconstrained slope-$p$ paths of vertical height $n$ modulo $998244353$.
```

---

#### Finding 1.6 (`MEDIUM` — Stage 1 Problem Statement Spoils the Degree-$k$ Transition Polynomial Complexity in `CP-V.6`, Line 327)
- **Location**: [`checkpoints/cp05-part5-dfinite-transposition-composition.qmd:325-328`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp05-part5-dfinite-transposition-composition.qmd#L325-L328)
- **What Is Wrong**: In `CP-V.6` (`#215`, `UOJ 604 — [UR #20] 跳蚤电话`), `Line 327` inside the visible Stage 1 Problem Statement states:
  `2. **Part 2 (Refined Subdivision Generating Polynomial)**: When an operation is chosen uniformly at random (or when tracking the exact order in which the $k$ child subtrees of a vertex $u$ are attached vs. subdivided), show how to merge the multi-child transition polynomials across a vertex $u$ of degree $k$ in $O(k \log^2 k)$ time.`
  This directly tells the student to merge multi-child transition polynomials in $O(k \log^2 k)$ time before `Hint 1`.
- **Drop-In Fix** (Replace `Lines 325–328` of `checkpoints/cp05-part5-dfinite-transposition-composition.qmd`):

```markdown
Two construction histories are distinct if at any step $i \in \{1, \dots, n-1\}$, either the chosen operation type or the chosen ordered pair of vertices differs. Compute the number of valid construction histories modulo $998244353$, and analyze how the transition changes when operation 2 can split an edge between $u$ and any of its $k$ children in arbitrary interleaved order.
```

---

#### Finding 1.7 (`CRITICAL` — Stage 1 Overview Table & Statement Replace `ARC 138 F — KD-Tree` with an Abstract Composition/Inversion Template in `CP-V.7`, Lines 39, 374–399)
- **Location**: [`checkpoints/cp05-part5-dfinite-transposition-composition.qmd:39`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp05-part5-dfinite-transposition-composition.qmd#L39) and [`checkpoints/cp05-part5-dfinite-transposition-composition.qmd:374-399`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp05-part5-dfinite-transposition-composition.qmd#L374-L399)
- **What Is Wrong**:
  1. In `Line 39` (Overview Table), `CP-V.7` (`#061`, `ARC 138 F — KD-Tree`) is described as: `Solve F(x) = x G(F(x)) \bmod x^{N+1} and W(x) = H(F(x)) \bmod x^{N+1} for all n \le N \le 2 \times 10^5.`
  2. In `Lines 376–386` (Stage 1 Problem Statement), instead of stating a combinatorial KD-tree / recursive interval-splitting problem and letting the student discover the composition/inversion reduction, the text states:
     `In combinatorial tree/graph enumeration problems where a family of structures $\mathcal{A}$ decomposes into sub-components via a known generating series $G(y)$...` and writes out `1. Task A: Solve the implicit functional equation F(x) = x G(F(x)) \bmod x^{N+1}` and `2. Task B: Given another series H(y), evaluate the composite series W(x) = H(F(x)) \bmod x^{N+1}`!
  This violates both **Checklist 1** (spoiling the exact FPS composition/reversion equations in Stage 1) and **Checklist 2** (replacing a contest problem with a bare polynomial template in Stage 1).
- **Drop-In Fix** (Replace `Line 39` and `Lines 374–399` of `checkpoints/cp05-part5-dfinite-transposition-composition.qmd`):
  - For `Line 39`:
    `| **CP-V.7** | `#061` | **ARC 138 F — KD-Tree** | Given a recursive tree-splitting rule with branching weights $g_c$ and root aggregation weights $h_c$, compute the total weight of all valid $n$-leaf decomposition trees for every $1 \le n \le N \le 2 \times 10^5$. |`
  - For `Lines 374–399`:

```markdown
### Problem CP-V.7: Recursive Partition Trees & Multi-Size Aggregation (`#061` — AtCoder ARC 138 F — KD-Tree / QOJ 8528)

##### Self-Contained Mathematical Statement & Constraints
Consider recursively partitioning $n$ ordered points into a rooted decomposition tree:
1. A single leaf has size $1$. An internal node splits its point set into $c \ge 0$ ordered child subtrees with branching weight $g_c \in \mathbb{F}_p$ (with $g_0 \neq 0$), so a rooted decomposition tree on $n$ nodes carries weight equal to the product of $g_{\text{deg}(v)}$ over all nodes $v$. Let $f_n$ be the total weight of all rooted decomposition trees of size $n$.
2. At the top level, a global partition connects $k \ge 0$ rooted decomposition trees of sizes $s_1 + s_2 + \dots + s_k = n$ with a root aggregation weight $h_k \in \mathbb{F}_p$. Let $w_n$ be the total weight of all global partitions of total size $n$.

Given the arrays $g_0, g_1, \dots, g_N$ (with $g_0 \neq 0$) and $h_0, h_1, \dots, h_N$, compute **both** sequences $f_1, \dots, f_N$ and $w_0, w_1, \dots, w_N$ simultaneously for **all** $n \le N$ modulo $998244353$.

- **Constraints**: $1 \le N \le 2 \times 10^5$, $g_0 \not\equiv 0 \pmod{998244353}$, modulus $P = 998244353$.

##### Visible Small-Case Sample Trace ($N = 3$)
Take $g_0 = 1, g_1 = 1, g_2 = 1, g_3 = 0$ (each node has $0, 1,$ or $2$ ordered children with weight $1$, i.e., Motzkin trees) and $h_0 = 0, h_1 = 1, h_2 = 1, h_3 = 0$ (the global partition combines $1$ or $2$ Motzkin trees):
- **Rooted decomposition counts ($f_n$)**:
  - $n = 1$: a single leaf ($c = 0$, weight $g_0 = 1$) $\implies f_1 = 1$.
  - $n = 2$: root with $1$ child of size $1$ ($c = 1$, weight $g_1 f_1 = 1$) $\implies f_2 = 1$.
  - $n = 3$: root with $1$ child of size $2$ ($g_1 f_2 = 1$) or $2$ children of size $1$ ($g_2 f_1^2 = 1$) $\implies f_3 = 2$.
- **Global partition counts ($w_n$)**:
  - $w_0 = h_0 = 0$; $w_1 = h_1 f_1 = 1$; $w_2 = h_1 f_2 + h_2 f_1^2 = 1 + 1 = 2$; $w_3 = h_1 f_3 + 2 h_2 f_1 f_2 = 2 + 2 = 4$.
```

---

#### Finding 1.8 (`MEDIUM` — Cross-Checkpoint Inconsistency in `Hint 2` Spoiler Policy Across `CP-I..IV` vs. `CP-V..VI`)
- **Locations**:
  - `cp01`, `cp02`, `cp03`, `cp04`: `Hint 2` is titled `Hint 2 — Chapter Routing & Technique Identification` and explicitly reveals the Home Chapter and Section (e.g., `Target Home: Chapter 01, Section 1.3`).
  - `cp05` and `cp06`: `Hint 2` is titled `Hint 2 — Algebraic Setup & Scratchpad` and keeps the Home Chapter hidden until `Stage 2`!
- **Recommendation**: Standardize `Hint 2` across all 6 checkpoints so that `Hint 2` gives the **Algebraic Setup & Generating Function Formulation without naming the Chapter/Section number**, reserving the explicit `Target Home: Chapter XX, Section XX.Y` routing label for `Stage 2` (or `Hint 3`).

---

## 2. Checklist 2: Self-Contained Inline Statements, Constraints & Sample Traces (`CP-I`–`CP-VI` + `Syn-01`–`Syn-14`)

### 2.1 Complete 62-Problem Verification Table (`48` Blind Checkpoints + `14` Synthesis Reserve)

Every single problem slot across `cp01`–`cp06` and `capstones/synthesis-reserve.qmd` was cross-checked against `fps_research/CURRICULUM_ARCHITECTURE.md` (§4 and §5.1):

| File & Part | Slots Verified | Match with `CURRICULUM_ARCHITECTURE.md` | Self-Contained Statement | Exact Constraints & Modulus | Visible $N \le 4$ Sample Trace Before `<details>` | Audit Notes |
| :--- | :-: | :-: | :-: | :-: | :-: | :--- |
| [`cp01-part1-foundations.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd) | `CP-I.1`–`CP-I.8` (`#078, #144, #246, #032, #079, #250, #037, #024`) | **8 / 8 (100%)** | Yes (`CP-I.3` needs de-spoiling per Finding 1.2) | Yes (`8 / 8`) | Yes (`8 / 8`) | Sample traces verified mathematically for all 8 problems. |
| [`cp02-part2-rational-transforms-ie.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd) | `CP-II.1`–`CP-II.8` (`#085, #152, #251, #252, #100, #029, #162, #141`) | **8 / 8 (100%)** | Yes (`8 / 8`) | Yes (`8 / 8`) | Yes (`8 / 8`) | Sample traces verified mathematically for all 8 problems. |
| [`cp03-part3-online-implicit-lif-graphs.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp03-part3-online-implicit-lif-graphs.qmd) | `CP-III.1`–`CP-III.8` (`#090, #131, #133, #160, #119, #035, #205, #163`) | **8 / 8 (100%)** | Yes (`8 / 8`) | Yes (`8 / 8`) | Yes (`8 / 8`) | Remove modular decomposition / FPS spoilers in `CP-III.4` & `CP-III.6` (§1.3–1.4). |
| [`cp04-part4-pgf-walks-multivariate.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd) | `CP-IV.1`–`CP-IV.8` (`#158, #169, #099, #116, #194, #058, #243, #082`) | **8 / 8 (100%)** | Yes (`CP-IV.7` needs de-spoiling per Finding 1.5) | Yes (`8 / 8`) | Yes (`8 / 8`) | Sample traces verified mathematically for all 8 problems. |
| [`cp05-part5-dfinite-transposition-composition.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp05-part5-dfinite-transposition-composition.qmd) | `CP-V.1`–`CP-V.8` (`#236, #108, #130, #135, #185, #215, #061, #068`) | **8 / 8 (100%)** | `7 / 8` (`CP-V.7` needs combinatorial statement per Finding 1.7) | Yes (`8 / 8`) | Yes (`8 / 8`) | Rewrite `CP-V.7` statement so Stage 1 states the combinatorial tree-splitting problem. |
| [`cp06-part6-trees-qseries-sps-dirichlet.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd) | `CP-VI.1`–`CP-VI.8` (`#102, #121, #117, #170, #054, #254, #175, #180`) | **8 / 8 (100%)** | Yes (`8 / 8`) | Yes (`8 / 8`) | Yes (`8 / 8`) | Zero Stage 1 spoilers; all 8 sample traces verified. |
| [`capstones/synthesis-reserve.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/synthesis-reserve.qmd) | `Syn-01`–`Syn-14` (`#006, #014, #051, #087, #106, #112, #142, #171, #173, #182, #172, #247, #249, #253`) | **14 / 14 (100%)** | Yes (`14 / 14`) | Yes (`14 / 14`) | Yes (`14 / 14`) | All 14 capstone problems have full dual-perspective derivations and sample traces. |

---

## 3. Checklist 3: 3-Stage Progressive Hints & Complete Step-by-Step Solutions with 5-Part Algorithm Contracts

### 3.1 Structural & Contract Audit Summary Across All 7 Files

| File | `Hint 1`–`Hint 3` `<details>` Blocks | 4th `<details>` Solution Block Placement | 5-Part `Algorithm Contract` Completeness |
| :--- | :-: | :--- | :--- |
| [`cp01-part1-foundations.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd) | `24 / 24` (`3` per problem) | `8` individual `<details>` blocks inline right below `Hint 3` (`Lines 199, 286, 377, 476, 594, 710, 845, 968`) | **Missing 5th bullet (`Failure Modes & Edge Cases`) inside the `Algorithm Contract` list** (it is placed in a separate `callout-warning` box above the contract). |
| [`cp02-part2-rational-transforms-ie.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd) | `24 / 24` (`3` per problem) | `8` individual `<details>` blocks inline right below `Hint 3` (`Lines 226, 360, 491, 616, 756, 899, 1043, 1185`) | **Missing 5th bullet (`Failure Modes & Edge Cases`) inside the `Algorithm Contract` list** (placed in a separate `callout-warning` box above the contract). |
| [`cp03-part3-online-implicit-lif-graphs.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp03-part3-online-implicit-lif-graphs.qmd) | `24 / 24` (`3` per problem) | `8` individual `<details>` blocks placed in **Stage 2** (`Lines 603, 687, 759, 839, 922, 1005, 1091, 1179`) | **Missing 5th bullet (`Failure Modes & Edge Cases`) inside the `Algorithm Contract` list** (placed in a separate `callout-warning` box above the contract). |
| [`cp04-part4-pgf-walks-multivariate.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd) | `24 / 24` (`3` per problem) | **DEFECT (`Lines 518–976`)**: All 8 solutions are trapped inside **ONE single `<details>` block** in Stage 2! | Has `Input`, `Output`, `Time & Space Complexity`, `Failure Modes & Edge Cases`, and `Step 1..k`, but **omits the explicit `Loop / Algebraic Invariant` label** on all 8 contracts (`Lines 556, 613, 660, 712, 767, 829, 892, 954`). |
| [`cp05-part5-dfinite-transposition-composition.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp05-part5-dfinite-transposition-composition.qmd) | `24 / 24` (`3` per problem) | `8` individual `<details>` blocks placed in **Stage 2** (`Lines 513, 553, 591, 631, 670, 709, 750, 790`) | **Missing 5th bullet (`Failure Modes & Edge Cases`)** in all 8 Stage 2 `Algorithm Contract` blocks (`Lines 539, 578, 618, 657, 696, 737, 777, 816`)—boundary hazards are only mentioned in `Hint 3`! |
| [`cp06-part6-trees-qseries-sps-dirichlet.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd) | `24 / 24` (`3` per problem) | `8` individual `<details>` blocks placed in **Stage 2** (`Lines 513, 560, 608, 657, 706, 752, 799, 853`) | **100% PASS**: Every single one of the 8 `Algorithm Contract` blocks in `cp06` has all 5 canonical bullets (`Input & Preconditions`, `Postconditions (Output)`, `Time & Space Complexity`, `Loop / Algebraic Invariant`, `Failure Modes & Edge Cases`)! |
| [`capstones/synthesis-reserve.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/synthesis-reserve.qmd) | `42 / 42` (`3` per problem) | `14` individual `<details>` blocks inline right below `Hint 3` (`Lines 122, 249, 381, 513, 650, 779, 914, 1054, 1192, 1327, 1489, 1618, 1749, 1879`) | **Missing 5th bullet (`Failure Modes & Edge Cases`) inside the `Algorithm Contract` list** (placed in a separate `callout-warning` box above the contract). |

---

### 3.2 Concrete Findings & Drop-In Fixes for Checklist 3

#### Finding 3.1 (`HIGH` — Monolithic Single `<details>` Block Wrapping All 8 Solutions + Missing `Loop / Algebraic Invariant` Bullet in `cp04-part4-pgf-walks-multivariate.qmd`, Lines 518–976)
- **Location**: [`checkpoints/cp04-part4-pgf-walks-multivariate.qmd:518-976`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp04-part4-pgf-walks-multivariate.qmd#L518-L976)
- **What Is Wrong**:
  1. At `Line 518`, a single `<details>` tag (`<summary><strong>Click to Reveal Stage 2: Diagnostic Routing Table & Complete Step-by-Step Solutions</strong></summary>`) opens and is not closed until `Line 976`! As a result, a student who wants to check the solution to `CP-IV.1` is forced to expand all 8 solutions (`CP-IV.1` through `CP-IV.8`) simultaneously.
  2. Each of the 8 `Algorithm Contract` blocks in `cp04` (`Lines 556, 613, 660, 712, 767, 829, 892, 954`) lists `- **Input**:`, `- **Output**:`, `- **Step 1..k**:`, `- **Time & Space Complexity**:`, and `- **Failure Modes & Edge Cases**:`, omitting `- **Loop / Algebraic Invariant**:`.
- **Drop-In Fix**:
  1. Close the Stage 2 Routing Table `<details>` block right after the routing table at `Line 534` (`</details>`), and wrap each of the 8 problem solutions (`### Solution CP-IV.1` through `### Solution CP-IV.8` at `Lines 536, 581, 639, 684, 738, 792, 855, 917`) in its own individual `<details><summary><strong>Click to Reveal Complete Solution for CP-IV.k</strong></summary> ... </details>` block (matching `cp03`, `cp05`, and `cp06`).
  2. Add the missing `- **Loop / Algebraic Invariant**:` bullet to each of the 8 `Algorithm Contract` blocks in `cp04`:
     - **`CP-IV.1` (`Line 565`)**: `- **Loop / Algebraic Invariant**: After processing item $i$, $dp[w][c]$ equals the exact sum of $(-1)^{|T|-k}\binom{|T|-1}{k-1}$ over all non-empty subsets $T \subseteq \{1, \dots, i\}$ with $\sum_{j \in T} a_j = w$ and $\binom{|T|-1}{k-1}$ offset state $c$.`
     - **`CP-IV.2` (`Line 622`)**: `- **Loop / Algebraic Invariant**: $A(x)$ and $B(x)$ maintain $\sum_{j=-S}^S a_j x^{j+S}$ and $\sum_{j=-S}^S b_j x^{j+S}$ where $a_j, b_j$ are the exact signed subset sums over switches processed so far.`
     - **`CP-IV.3` (`Line 667`)**: `- **Loop / Algebraic Invariant**: At every random merger step, $\Phi(S_{t+1}) - \Phi(S_t)$ has conditional expectation $-1$, so $\Phi(S_t) + t$ is a true martingale.`
     - **`CP-IV.4` (`Line 721`)**: `- **Loop / Algebraic Invariant**: The homogeneous difference $d_s = f(s+1) - f(s)$ satisfies the exact two-term ratio recurrence lifted from the 3-term single-pile drift equation.`
     - **`CP-IV.5` (`Line 776`)**: `- **Loop / Algebraic Invariant**: $[x^s] P(x)$ equals the number of valid card subsets of size $s$ containing zero contiguous runs of length $\ge k$.`
     - **`CP-IV.6` (`Line 838`)**: `- **Loop / Algebraic Invariant**: For each $(r, c)$ parity split, the EGF product $\sinh^r(x/N)\cosh^{N-r}(x/N)$ tracks the exact per-cell flip parities before reading off $(e^{\lambda x}) \mapsto \lambda^T$.`
     - **`CP-IV.7` (`Line 901`)**: `- **Loop / Algebraic Invariant**: Under $x = t/y^p$, the unique small root $w(t) \in tK[[t]]$ satisfies $w(t) = t(1-w(t))^{-p}$ and converts the 2D diagonal into a 1D residue at $y = w(t)$.`
     - **`CP-IV.8` (`Line 963`)**: `- **Loop / Algebraic Invariant**: For every subtree $u$, the polynomial $P_u(z)$ maintains the exact probability distribution of the truncated cap state passed from $u$ to its parent.`

---

#### Finding 3.2 (`MEDIUM` — Missing `Failure Modes & Edge Cases` Bullet Inside the 8 Stage 2 `Algorithm Contract` Blocks of `cp05-part5-dfinite-transposition-composition.qmd`)
- **Location**: [`checkpoints/cp05-part5-dfinite-transposition-composition.qmd:539-830`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp05-part5-dfinite-transposition-composition.qmd#L539-L830)
- **What Is Wrong**: Unlike `cp06-part6-trees-qseries-sps-dirichlet.qmd` (which sets the gold standard by including all 5 required contract bullets inside every Stage 2 `Algorithm Contract`), all 8 Stage 2 `Algorithm Contract` blocks in `cp05` (`Lines 539–545, 578–584, 618–624, 657–663, 696–702, 737–743, 777–783, 816–822`) have only 4 bullets (`Input`, `Output`, `Complexity`, `Core Invariant`), omitting `Failure Modes & Edge Cases`.
- **Drop-In Fix**: Append the 5th bullet `- **Failure Modes & Edge Cases**:` to each of the 8 `Algorithm Contract` blocks in `cp05`:
  - **`CP-V.1` (` after Line 544`)**: `- **Failure Modes & Edge Cases**: In `cdq(l, r)`, when $l = 0$ both factors depend on $[0..m]$, whereas when $l > 0$ symmetric pairs $(i, n-1-i)$ must be multiplied by $2$ (**Failure Mode #13**); also handle $N = 1$ separately since up-down and down-up coincide at length $1$.`
  - **`CP-V.2` (`after Line 583`)**: `- **Failure Modes & Edge Cases**: Guard against $Q - 1 < 0$ when $Q = 0$ (no `'?'` characters in $s$): evaluate the second prefix sum $P_{Q-1}$ only when $Q \ge 1$.`
  - **`CP-V.3` (`after Line 623`)**: `- **Failure Modes & Edge Cases**: In transposed convolution $\operatorname{mulT}(A, B)_k = \sum_i a_i b_{i+k}$, pad the FFT length to $2^{\lceil \log_2(\deg B + 1) \rceil}$ (not $\deg A + \deg B$) and slice $[0..\deg B - \deg A]$ without off-by-one shift.`
  - **`CP-V.4` (`after Line 662`)**: `- **Failure Modes & Edge Cases**: Because $N \le 700$ and the bivariate polynomial has total degree $O(N^2)$, only re-convolve on indices where the probability/weight parameter actually changes, or flatten via Kronecker substitution with base $B = N + 1$.`
  - **`CP-V.5` (`after Line 701`)**: `- **Failure Modes & Edge Cases**: When building the subproduct tree for $M_{0, n}(x) = \prod_{j=0}^{n-1}(x - j)$, ensure the root middle product initializes $R_{0, n} = \operatorname{mulT}(M_{0, n}^{\text{rev}}, F) \bmod x^n$ to degree $< n$ before descending.`
  - **`CP-V.6` (`after Line 742`)**: `- **Failure Modes & Edge Cases**: Leaves have subtree size $s_u = 1$ ($s_u - 1 = 0$); guard $(s_u - 1)!$ and inverse factorials at $0! = 1$, and push child polynomials into a min-heap by degree (`Failure Mode #1`).`
  - **`CP-V.7` (`after Line 782`)**: `- **Failure Modes & Edge Cases**: Route A (`Power Projection` + `pow(-1/n)`) divides by $1, \dots, N$ and fails when $p \le N$ (**Failure Mode #6**); if $g_0 = 0$, $F(x) = x G(F(x))$ has no unit inverse—verify $g_0 \neq 0$ first.`
  - **`CP-V.8` (`after Line 821`)**: `- **Failure Modes & Edge Cases**: Each undirected edge $e$ contributes both $s_e$ and $N - s_e$ to the frequency array $c_s$; only accumulate $c_s \binom{s}{K}$ for $s \ge K$, and verify $K = 1 \implies N \binom{N}{1} = N^2$.`

---

#### Finding 3.3 (`LOW/EDITORIAL` — Standardizing the 5-Bullet `Algorithm Contract` Format in `cp01`, `cp02`, `cp03`, and `capstones/synthesis-reserve.qmd`)
- **Locations**: `cp01`, `cp02`, `cp03` (8 problems each), and `capstones/synthesis-reserve.qmd` (`Syn-01`–`Syn-14`).
- **Observation**: In these 4 files, every solution block contains both a `::: {.callout-warning}` box (titled `Boundary, Valuation & Characteristic-$p$ Audit`) **and** a `::: {.callout-note}` box (titled `Algorithm Contract`) with 5 bullets (`Input`, `Output`, `Preconditions`, `Complexity`, `Core Invariant`). Thus all 5 required pieces of information are 100% present inside every solution `<details>` block, though `Failure Modes & Edge Cases` is in the adjacent warning callout rather than inside the `Algorithm Contract` bullet list (unlike `cp06`, which puts all 5 bullets inside `Algorithm Contract`). If strict 1-box uniformity with `cp06` is desired, merge `Input` + `Preconditions` into `- **Input & Preconditions**:` and add `- **Failure Modes & Edge Cases**:` as the 5th bullet of `Algorithm Contract`.

---

## 4. Checklist 4: 12 Revisited Dual-Perspective Cross-Studies in `capstones/synthesis-reserve.qmd`

### 4.1 Audit of What Currently Exists in `capstones/synthesis-reserve.qmd` (§3, Lines 1954–2004)

In [`capstones/synthesis-reserve.qmd:1954-2004`](file:///home/maomao90/Documents/IO/ICPC-math-notes/capstones/synthesis-reserve.qmd#L1954-L2004), Section 3 (`## 3. The 12 Revisited Dual-Perspective Cross-Reference Index`) currently contains:
1. **Table 3.1 (`Lines 1960–1973`)**: Lists the 12 Revisited problems from `CURRICULUM_ARCHITECTURE.md` §5.2 (`#101, #084, #040, #094, #089, #023, #244, #200, #183, #156, #220, #058`), with exact home slots, first perspective, second perspective, and pedagogical takeaway.
2. **Three Prose Callout Notes (`Lines 1975–2004`)**:
   - Callout 1 (`Lines 1975–1983`): Covers `#101` (`CF 1096G — Lucky Tickets`).
   - Callout 2 (`Lines 1985–1994`): Covers `#023` (`ABC 230 Ex`), `#244` (`yukicoder 3029`), and `#200` (`Luogu P7438`).
   - Callout 3 (`Lines 1996–2004`): Covers `#058` (`ARC 136 F — Flip Cells`).

### 4.2 Two Specific Gaps Identified in Section 3

1. **Gap 4.1 (`7` of the 12 problems in Table 3.1 have no worked Dual-Perspective Cross-Study callout in §3)**:
   Specifically, `#084` (`CF 438E`), `#040` (`ABC 300 Ex`), `#094` (`CF 923E`), `#089` (`CF 840C`), `#183` (`Luogu P5827`), `#156` (`Luogu P4548`), and `#220` (`Luogu P3266`) appear only as 1-line rows in Table 3.1 without worked comparative equations in §3.
2. **Gap 4.2 (Reconciling the Iteration 8 Specification's 12 Revisited IDs `#011, #037, #040, #058, #074, #076, #107, #110, #169, #185, #226, #237`)**:
   Comparing the Iteration 8 checklist (`#011, #037, #040, #058, #074, #076, #107, #110, #169, #185, #226, #237`) with `CURRICULUM_ARCHITECTURE.md` §5.2 (`#101, #084, #040, #094, #089, #023, #244, #200, #183, #156, #220, #058`), `#040` and `#058` are in both lists, while the other 10 problems (`#011, #037, #074, #076, #107, #110, #169, #185, #226, #237`) are additional dual-perspective problems across the 254-problem pool.

### 4.3 Drop-In Replacement for `capstones/synthesis-reserve.qmd` Lines 1975–2004 (Complete Worked Cross-Studies for Both Sets of Revisited Problems)

Replacing `Lines 1975–2004` of `capstones/synthesis-reserve.qmd` with the following block makes §3 100% complete for **all 12 problems in `CURRICULUM_ARCHITECTURE.md` §5.2** *and* **all 12 problems in the Iteration 8 Revisited specification**:

```markdown
### 3.1 Worked Dual-Perspective Cross-Studies (Core 12 Architectural Threads)

::: {.callout-note}
#### Cross-Study A — Sparse ODEs vs. Dense NTT & Bostan–Mori (`#101` CF 1096G, `#040` ABC 300 Ex, `#084` CF 438E)
- **`#101` (CF 1096G — Lucky Tickets, `Ch 02 [Int-1]`)**:
  - *Perspective 1 (`Ch 02.4` $O(NK)$ Sparse Power ODE)*: Because $P(x) = \sum_{d=0}^9 x^d = \frac{1-x^{10}}{1-x}$, differentiating $G(x) = P(x)^k$ yields $(1-x)(1-x^{10})G'(x) = k(1 - 10x^9 + 9x^{10})G(x)$, extracting all coefficients up to $9k$ in $O(k)$ scalar operations with **zero NTTs**.
  - *Perspective 2 (`Ch 01` / `Ch 07` Cyclic NTT Power)*: Evaluate $P(\omega_L^r)^k$ on a power-of-two NTT grid of length $L > 9k$ and interpolate in $O(N \log N)$ time.
- **`#040` (ABC 300 Ex — Fibonacci: Revisited, `Ch 05 [Adv-1]`)**:
  - *Perspective 1 (`Ch 05.3` General Bostan–Mori)*: Extract $[x^{N-K}](1 - x - x^2 - \dots - x^K)^{-1}$ via parity splitting $Q(x)Q(-x)$ in $O(K \log K \log N)$ time.
  - *Perspective 2 (`Ch 02.4` $(1-x)$ Sparse Multiplier + Frobenius/Doubling)*: Multiply numerator and denominator by $(1-x)$ so $(1-x)Q(x) = 1 - 2x + x^{K+1}$ collapses to a **3-sparse trinomial**, reducing each parity-halving or modular doubling step from $O(K \log K)$ to $O(K)$ when $K$ is small or $N$ is moderate!
- **`#084` (CF 438E — The Child and Binary Tree, `Ch 02 [Adv-2]`)**:
  - *Perspective 1 (`Ch 02.3` Explicit Radical)*: Solve $C(x)F(x)^2 - F(x) + 1 = 0$ via the rationalized quadratic formula $F(x) = \frac{2}{1 + \sqrt{1 - 4C(x)}} \bmod x^{M+1}$ using 1D `sqrt` and `inv`.
  - *Perspective 2 (`Ch 10.2` Direct Implicit Fréchet Newton Iteration)*: Apply $F_{k+1} = F_k - \frac{C F_k^2 - F_k + 1}{2 C F_k - 1} \bmod x^{2^{k+1}}$ directly without square roots, which generalizes immediately to degree-$d \ge 5$ tree equations where no radical formula exists.
:::

::: {.callout-note}
#### Cross-Study B — Taylor Shift, Spectral Diagonalization & Laguerre IE (`#094` CF 923E, `#089` CF 840C)
- **`#094` (CF 923E — Perpetual Subtraction, `Ch 06 [Adv-1]`)**:
  - *Perspective 1 (`Ch 06.3` Algebraic Taylor Shift)*: The transition $[x^j] P_{\text{next}}(x) = \sum_{i=j}^N \frac{[x^i]P(x)}{i+1}$ becomes diagonal after shifting $G(y) = P(y+1)$: each coefficient $[y^k]G(y)$ simply multiplies by $(k+1)^{-1}$ per step, so $M$ steps take two Taylor shifts $P(x) \xrightarrow{x \mapsto y+1} G(y) \xrightarrow{\times (k+1)^{-M}} \widetilde{G}(y) \xrightarrow{y \mapsto x-1} P_M(x)$ in $O(N \log N)$ time.
  - *Perspective 2 (`Ch 13.3` Eigenbasis Factorization)*: The upper-triangular matrix $T_{j,i} = \frac{1}{i+1}[j \le i]$ is diagonalized by the Pascal matrix $V_{i,j} = \binom{i}{j}$ ($T = V \operatorname{diag}(1, \frac{1}{2}, \dots, \frac{1}{N+1}) V^{-1}$), because $V$ is the matrix representation of the formal shift operator $\exp(D_x) : x^i \mapsto (x+1)^i$.
- **`#089` (CF 840C — On the Bench, `Ch 08 [Int-2]`)**:
  - *Perspective 1 (`Ch 08.3` Connected-Component IE)*: Split $c_i$ identical-class balls into $b \in [1, c_i]$ blocks with signed EGF $P_{c_i}(x) = \sum_{b=1}^{c_i} (-1)^{c_i-b} \binom{c_i}{b}\binom{c_i-1}{b-1} \frac{x^b}{b!}$ and multiply in $O(N^2)$ DP.
  - *Perspective 2 (`Ch 19.3` Laguerre Polynomials & D&C NTT)*: Recognize $P_{c}(x)$ as a shifted Laguerre polynomial and multiply $\prod_{i=1}^m P_{c_i}(x)$ via a min-heap divide-and-conquer NTT tree in $O(N \log^2 N)$ time (scaling to $N \le 2.5 \times 10^5$ in `#028` ABC 260 Ex).
:::

::: {.callout-note}
#### Cross-Study C — Online Convolutions, Coupled Newton, LIF & Fast Reversion (`#023` ABC 230 Ex, `#244` yukicoder 3029, `#200` Luogu P7438, `#183` Luogu P5827)
- **`#023` (ABC 230 Ex — Bullion, `Ch 09 [Int-2]`) & `#244` (yukicoder 3029 — Cactus Weight, `Ch 10 [Int-1]`)**:
  - *Perspective 1 (`Ch 09.3–9.4` Online Relaxed Convolution)*: Solve $F(x) = x \exp\!\left(\sum_{k \ge 1} \frac{F(x^k)}{k}\right)$ or $2 \times 2$ coupled functional systems coefficient-by-coefficient in $O(N \log^2 N)$ time using a 15-line `RelaxedConvolution` maintainer without computing Fréchet Jacobians.
  - *Perspective 2 (`Ch 10.2–10.3` Pólya & Coupled Jacobian Newton)*: Linearize with respect to the top-precision term $F(x)$ (treating $F(x^2), F(x^3), \dots$ as known constants at step $2^k \to 2^{k+1}$) or invert the $2 \times 2$ Jacobian matrix $(I - J_G(F_k))^{-1}$ in $O(N \log N)$ time.
- **`#200` (Luogu P7438 — 恐龙, `Ch 11 [SS-2]`) & `#183` (Luogu P5827 — 点双连通图计数, `Ch 12 [Mas-1]`)**:
  - *Perspective 1 (`Ch 11.2` & `Ch 12.3` Single-$N$ Lagrange Inversion)*: For a single target $N$, invert $R(x) = x \exp(B'(R(x)))$ at degree $N$ via $\frac{1}{N}[u^{N-1}] H'(u) \exp(N B'(u))$ in $O(N \log N)$ time.
  - *Perspective 2 (`Ch 21.3` All-$n$ Kinoshita–Li `revert` & `Ch 24.3` Pointed SPS $\ln$)*: When answers are required for **all** $1 \le n \le N$ simultaneously (`#016 fps_24_w`), apply $O(N \log^2 N)$ fast compositional inversion; when counting biconnected subgraphs of a **fixed** input graph $G = (V, E)$ with $|V| \le 20$ (`#207 UOJ 94`), lift Tutte's pointed block-cut $\ln$ into the Set Power Series ring $\mathcal{R}_V$ in $O(n^2 2^n)$ time!
:::

::: {.callout-note}
#### Cross-Study D — PGFs, Lattice Reflections, Furstenberg Diagonals & D-Finite ODEs (`#156` Luogu P4548, `#220` Luogu P3266, `#058` ARC 136 F)
- **`#156` (Luogu P4548 — 歌唱王国, `Ch 14 [Int-1]`)**:
  - *Perspective 1 (`Ch 14.2` Stopping-Time PGF & L'Hôpital Shift)*: Set up $(1-z)G(z) + F(z) = 1$ and $G(z) + \sum_{b \in \text{Borders}(P)} m^{|b|-L} z^{L-|b|} F(z) = m^{-L} z^L G(z)$, then differentiate at $z = 1$ to obtain $F'(1) = \sum_{b \in \text{Borders}(P)} m^{|b|}$.
  - *Perspective 2 (`Ch 08.4` Goulden–Jackson Cluster Matrix & `Ch 14.5` Optional Stopping Martingale)*: Evaluate the deterministic Goulden–Jackson avoidance OGF at $x = z/m$, or run Li's fair-casino betting martingale in $O(L)$ KMP time.
- **`#220` (Luogu P3266 — 骗我呢, `Ch 15 [Int-1]`)**:
  - *Perspective 1 (`Ch 15.1` Kelvin Alternating Reflection across Two Parallel Walls)*: Unfold the strip $0 \le x - y \le M+1$ via alternating reflections across $L_1: x - y = -1$ and $L_2: x - y = M+2$, summing $\binom{2N+M+1}{N - k(M+3)}$ in $O(N/M)$ time.
  - *Perspective 2 (`Ch 15.3` Bivariate Kernel Method & `Ch 05` Rational Transfer)*: Write the bounded step equation in $(K[y, y^{-1}])[[t]]$ and eliminate the two boundary series via the conjugate kernel roots $y_1(t), y_2(t)$ (Chebyshev quotient $U_{M+1} / U_{M+2}$).
- **`#058` (ARC 136 F — Flip Cells, `CP-IV.6`)**:
  - *Perspective 1 (`Ch 16.3–16.4` Bivariate Rational/Exponential Parity Walk)*: Formulate the $(r, c)$ parity-flip walk as a bivariate generating function and extract the target coefficient via formal residues.
  - *Perspective 2 (`Ch 18.2` Algebraic-to-D-Finite ODE Compilation)*: Differentiate the bivariate kernel/diagonal to compile a linear differential equation with polynomial coefficients, then unroll the resulting P-recursive sequence recurrence in **$O(N)$ linear time**!
:::

### 3.2 Extended Multi-Resolution Revisited Threads (10 Additional Cross-Part Bridges)

| # | Primary Slot | Problem ID & Title | First Perspective (Home Chapter) | Second Perspective (Revisited Chapter) | Comparative Payoff |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 13 | `Ch 01 [Mas-2]` (`#107`) | **CF 1251F — Red-White Fence** | **Ch 01 (1.3)**: Group planks into $(1+2x)^{c_1}(1+x)^{2c_2}$ via explicit binomial coefficients and 1D NTT per red board. | **Ch 02 (2.5)**: Logarithmic derivative $\ln/\exp$ compression when plank multiplicities are arbitrary. | Shows when explicit binomial factoring $(1+2x)^a(1+x)^b$ beats general $\ln/\exp$. |
| 14 | `Ch 04 [Adv-2]` (`#011`) | **`fps_24_q` — Dice** | **Ch 04 (4.2)**: Labeled EGF moment expansion $\sum_{k=1}^M [x^k/k!] A(x)^N$ via EGF powers. | **Ch 02 (2.5) & Ch 17 (17.3)**: Newton–Girard power-sum duality $P(t) = -t \frac{d}{dt}\ln\prod(1 - a_i t)$ in $O(N \log^2 N + M \log M)$. | Connects EGF tuple moments (`Ch 04`) to symmetric function Newton–Girard identities (`Ch 02, 17`). |
| 15 | `CP-I.7` (`#037`) | **ABC 284 Ex — Count Unlabeled Graphs** | **Ch 03 (3.5)**: Burnside's Lemma over integer partitions $\lambda \vdash N$ with edge-orbit power $2^{\sum \gcd(l_i, l_j) + \sum \lfloor l_i/2 \rfloor}$. | **Ch 10 (10.3) & Ch 23**: Pólya cycle index OGF product over part multiplicities $c_k$. | Demonstrates how grouping cycle lengths by multiplicity collapses pair-gcd sums to $O(p(N) \cdot d^2)$. |
| 16 | `CP-IV.2` (`#169`) | **Luogu P5326 — [ZJOI2019] 开关** | **Ch 14 (14.2)**: Switching-walk EGF renewal quotient $F(x) = G(x)/H(x)$ differentiated after clearing $(1 - e^x)$ pole. | **Ch 24 (24.1)**: Walsh–Hadamard (XOR FWT) spectral diagonalization of hypercube random walks. | Reveals why $\sinh/\cosh$ EGF factors (`Ch 14`) are the 1D projection of the $\mathbb{Z}_2^n$ Walsh transform (`Ch 24`). |
| 17 | `Ch 15 [Mas-1]` (`#076`) | **AGC 061 E — Increment or XOR** | **Ch 15 (15.3)**: Bit-by-bit carry propagation via kernel / state reduction across binary blocks. | **Ch 24 (24.1)**: Bitwise XOR FWT combined with carry state transitions. | Bridges 1D carry-state transfer (`Ch 15`) with bitwise Walsh–Hadamard algebra (`Ch 24`). |
| 18 | `Ch 16 [Adv-1]` (`#237`) | **yukicoder 1080 — Coupled Series** | **Ch 16 (16.1)**: Complexification $(A(x) \pm i B(x))$ over $\mathbb{F}_p[i]$ ($i^2 \equiv -1$) decoupling $2 \times 2$ rotation systems into two 1D $\exp/\ln$ calls. | **Ch 10 (10.2) & Ch 18 (18.2)**: Coupled $2 \times 2$ Jacobian Newton iteration (`Ch 10`) or 2nd-order D-finite harmonic ODE (`Ch 18`). | Contrasts diagonalization via field extension $\mathbb{F}_p[i]$ (`Ch 16`) against coupled matrix Newton (`Ch 10`). |
| 19 | `Ch 16 [Adv-2]` (`#074`) | **AGC 058 D — Yet Another ABC String** | **Ch 08 (8.4)**: Goulden–Jackson cluster inclusion–exclusion contracting forbidden `ABC`/`BCA`/`CAB` overlaps into $-xyz/(1-xyz)$. | **Ch 16 (16.4) & Ch 18 (18.2)**: Trivariate rational diagonal $[x^A y^B z^C] \frac{1-xyz}{1-(x+y+z)+2xyz}$ extracted in $O(A+B+C)$ via binomial expansion or Lipshitz D-finite recurrence. | Unites string cluster sieves (`Ch 08`) with multivariate rational diagonals (`Ch 16`). |
| 20 | `Ch 10 [SS-2]` (`#226`) | **LOJ 6538 — 烷基计数 加强版 加强版** | **Ch 10 (10.3)**: $S_3$ Burnside cycle index $A(x) = 1 + \frac{x}{6}(A(x)^3 + 3A(x)A(x^2) + 2A(x^3))$ solved in $O(N \log N)$ via 1D Pólya Newton iteration. | **Ch 09 (9.4)**: Solved online in $O(N \log^2 N)$ via `RelaxedConvolution` without Newton derivatives. | Canonical benchmark comparing `Ch 09` relaxed convolution against `Ch 10` Pólya Newton. |
| 21 | `CP-V.5` (`#185`) | **Luogu P5853 — Stirling & Falling Factorial Transpose** | **Ch 20 (20.2)**: Tellegen transposed subproduct tree (`mulT` down-tree) converting between power and falling-factorial bases in $O(N \log^2 N)$. | **Ch 06 (6.3)**: Direct EGF multiplication by $e^{\pm x}$ when sample points are consecutive integers $0, 1, \dots, N$. | Clarifies when $O(N \log N)$ EGF convolution (`Ch 06`) suffices vs. when arbitrary tree/node shifts require $O(N \log^2 N)$ transposed multipoint evaluation (`Ch 20`). |
| 22 | `Ch 24 [Adv-1]` (`#110`) | **CF 1326F2 — Wise Men (Hard Version)** | **Ch 24 (24.1–24.2)**: Or-FWT product of path-mask arrays evaluated over all integer partitions $\lambda \vdash N$, followed by AND-Möbius inversion in $O(p(N) n + n 2^n)$. | **Ch 03 (3.3) & Ch 08 (8.1)**: Partition compression of symmetric subset convolutions + poset inclusion–exclusion over adjacency runs. | Shows how collapsing permutation symmetry into integer partitions (`Ch 03`) reduces $2^{n-1}$ FWT products to $p(n) = 385$ partition evaluations (`Ch 24`). |
```

---

## 5. Checklist 5: Quarto Formatting & Hygiene Sweep

An automated Python audit was executed across all 8,359 lines of the 7 target `.qmd` files (`cp01`–`cp06` and `capstones/synthesis-reserve.qmd`). Every single formatting rule passed with **zero violations**:

| Formatting & Hygiene Rule | Audit Result | Verification Details |
| :--- | :-: | :--- |
| **1. No `\(` or `\[` math delimiters** | **0 Violations (PASS)** | The only 5 regex hits for `\[` across all 8,359 lines (`cp06` lines 623, 836, 837, 842, 843) are valid LaTeX line-break spacing commands `\\[10pt]` inside `\begin{cases} ... \end{cases}`. Zero `\(` or `\[` math delimiters exist. |
| **2. No `!$$` or `![x^` strings** | **0 Violations (PASS)** | Verified across all 7 files. |
| **3. No unescaped `\|` inside `$...$` in Markdown tables** | **0 Violations (PASS)** | All absolute-value and divisibility bars inside Markdown table cells properly use `\lvert`, `\rvert`, or `\mid`. |
| **4. No raw `"Wait"` strings** | **0 Violations (PASS)** | Zero occurrences of `"Wait"` or conversational filler in any of the 7 files. |
| **5. No C++/Python code blocks $> 15$ inner lines** | **0 Violations (PASS)** | All C++/Python snippets are $\le 15$ inner lines (the only fenced blocks $> 15$ lines are two `mermaid` diagrams: `cp01` lines 26–48 and `cp02` lines 70–88). |
| **6. Blank lines after `</summary>` and before `</details>`** | **0 Violations (PASS)** | Every `<details>` block across all 7 files has a blank line immediately after `</summary>` and immediately before `</details>`, and all `<details>` and `:::` blocks are properly balanced and closed. |
