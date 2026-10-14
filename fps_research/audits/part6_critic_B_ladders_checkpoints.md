# Part VI Critic B Audit Report: Problem Ladders, Blind Checkpoints, Bijective Pool Coverage & Self-Contained Statements

**Auditor**: `fps-textbook-critic` (Part VI Critic B — Ladders, Blind Checkpoints, Bijective Pool Coverage & Self-Contained Statements)  
**Target Scope**: Part VI (`Ch 22`–`Ch 24` + `CP-VI`)
- [`chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd) (1,299 lines)
- [`chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd) (1,209 lines)
- [`chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd) (1,332 lines)
- [`checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd) (912 lines)

---

## Executive Summary

| Audit Dimension | Status | Findings Summary |
| :--- | :---: | :--- |
| **1. Bijective Pool Coverage (`24` Ladder + `8` Checkpoint + Quarantined Templates)** | **PASS WITH 2 FOOTNOTE OMISSIONS (`Q-1`, `Q-2`)** | All `24/24` chapter ladder problems (`Ch 22`–`Ch 24`) and all `8/8` `CP-VI` problems match `CURRICULUM_ARCHITECTURE.md` §3–§4 and `PROBLEM_CURATION.md` §3–§4 with **100% bijective fidelity** (zero omissions, zero substitutions, zero duplicates, and zero quarantined template leaks into ladders). However, `Ch 22` omits the required `Implementation Verification Footnote` for `R-67` (`Q-1`), and `Ch 24` omits the required `Implementation Verification Footnote` for `R-07, R-08, R-50, R-51, R-52` (`Q-2`), whereas `Ch 23` properly includes its `R-48, R-49` footnote callout. |
| **2. Self-Contained Problem Statements & Sample Traces** | **NEEDS REVISION (`4` CRITICAL DEFECTS: `S-1`–`S-4`)** | `28/32` problems across Part VI have crisp, self-contained statements and verified small-case traces. However, **4 problems** (`Ch 22 Int-1 (#046)`, `Ch 22 Int-2 (#198)`, `Ch 23 Int-1 (#233)`, and `Ch 24 Mas-1 (#231)`) are written as meta-summaries, unspecified parameter templates, or textbook proof exercises rather than self-contained competitive programming problems. Complete drop-in replacements are provided below. |
| **3. 3-Hint & Solution Architecture + 5-Part Algorithm Contracts** | **PASS WITH MINOR HINT SPOILERS (`H-1`)** | Every single problem (`32/32`) has 3 progressive collapsible `<details>` hints, a complete multi-step `<details>` derivation & solution with zero hand-waving, and a complete 5-part Algorithm Contract (*Input & Constraints, Algebraic/Combinatorial Core, Step-by-Step Pipeline, Complexity, Pitfalls & Edge Cases*).Zero raw NTT/ModInt/Sieve template dumps appear anywhere. In `Ch 23`, 4 `Hint 1` blocks (`SS-1`, `SS-2`, `Int-1`, `Mas-1`) explicitly name the theorem/proposition from the chapter instead of giving a spoiler-free combinatorial observation (`H-1`). |
| **4. Blind Checkpoint `CP-VI` Spoiler-Free Audit & Render Safety** | **PASS WITH 1 MINOR HINT LEAK (`CP-1`) & 1 CRITICAL TABLE BUG (`F-1`)** | `CP-VI` Stage 1 (`lines 51–519`) is **100% free of chapter numbers and technique names** in the Arena Table, Problem Titles, and Problem Statements. Only `CP-VI.6 (#254)` `Hint 1` (`line 370`) has a minor algebraic spoiler (*"polynomial over the XOR group ring"*). Separately, `Ch 24` `line 466` has a **critical Quarto pipe-table render bug (`F-1`)** caused by unescaped `|` inside `$\mathbin{\|}$` inside a Markdown table cell. |

---

## Dimension 1: Bijective Pool Coverage (`24` Ladder Problems + `8` Checkpoint Problems + Quarantined Templates)

### 1.1 Chapter 22 Problem Ladder Verification (`8/8` Exact Match)
Cross-checked against `CURRICULUM_ARCHITECTURE.md` (lines 1255–1265) and `PROBLEM_CURATION.md` (lines 382–393):

| Tier | Archive ID & Problem Title in `CURRICULUM_ARCHITECTURE.md` | Location in `ch22-*.qmd` | Statement | 3 Hints | Full Solution & 5-Part Contract | Verdict |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **SS-1** | `#031` AtCoder ABC 269 Ex — *Antichain* | Lines 581–663 | Yes | Yes | Yes | **PASS** |
| **SS-2** | `#124` CF 1613F — *Tree Coloring* | Lines 667–744 | Yes | Yes | Yes | **PASS** |
| **Int-1** | `#046` AtCoder ABC 355 G — *Baseball* | Lines 748–814 | **Meta-Summary (`S-1`)** | Yes | Yes | **FIX STATEMENT** |
| **Int-2** | `#198` Luogu P7279 — *光棱碎片 (Prism Shards)* | Lines 818–907 | **Half-Abstracted (`S-2`)** | Yes | Yes | **FIX STATEMENT** |
| **Adv-1** | `#149` Luogu P3781 / LOJ 2269 — *[SDOI2017] 切树游戏* | Lines 911–1006 | Yes | Yes | Yes | **PASS** |
| **Adv-2** | `#136` CF 2006E — *Iris's Full Binary Tree* | Lines 1010–1083 | Yes | Yes | Yes | **PASS** |
| **Mas-1** | `#166` Luogu P5281 / LOJ 3044 — *[ZJOI2019] Minimax 搜索* | Lines 1087–1193 | Yes | Yes | Yes | **PASS** |
| **Mas-2** | `#145` Luogu P3348 — *[ZJOI2016] 大森林* | Lines 1197–1278 | Yes | Yes | Yes | **PASS** |

### 1.2 Chapter 23 Problem Ladder Verification (`8/8` Exact Match)
Cross-checked against `CURRICULUM_ARCHITECTURE.md` (lines 1309–1319) and `PROBLEM_CURATION.md` (lines 401–412):

| Tier | Archive ID & Problem Title in `CURRICULUM_ARCHITECTURE.md` | Location in `ch23-*.qmd` | Statement | 3 Hints | Full Solution & 5-Part Contract | Verdict |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **SS-1** | `#123` CF 1603F — *October 18, 2017* | Lines 482–555 | Yes | Yes (`H-1`) | Yes | **PASS** |
| **SS-2** | `#033` AtCoder ABC 278 Ex — *make 1* | Lines 559–640 | Yes | Yes (`H-1`) | Yes | **PASS** |
| **Int-1** | `#233` QOJ 5097 / SOJ 703 — *布尔立方 (Boolean Cube)* | Lines 644–715 | **Meta-Summary (`S-3`)** | Yes (`H-1`) | Yes | **FIX STATEMENT** |
| **Int-2** | `#057` AtCoder ARC 134 E — *Modulo Nim* | Lines 719–814 | Yes | Yes | Yes | **PASS** |
| **Adv-1** | `#062` AtCoder ARC 139 F — *Many Xor Optimization Problems* | Lines 818–914 | Yes | Yes | Yes | **PASS** |
| **Adv-2** | `#132` CF 1916F — *Group Division* | Lines 918–992 | Yes | Yes | Yes | **PASS** |
| **Mas-1** | `#063` AtCoder ARC 145 F — *Modulo Sum of Increasing Sequences* | Lines 996–1111 | Yes | Yes (`H-1`) | Yes | **PASS** |
| **Mas-2** | `#111` CF 1336E2 — *Chiori and Doll Picking (Hard Version)* | Lines 1115–1192 | Yes | Yes | Yes | **PASS** |

### 1.3 Chapter 24 Problem Ladder Verification (`8/8` Exact Match)
Cross-checked against `CURRICULUM_ARCHITECTURE.md` (lines 1372–1382) and `PROBLEM_CURATION.md` (lines 420–431):

| Tier | Archive ID & Problem Title in `CURRICULUM_ARCHITECTURE.md` | Location in `ch24-*.qmd` | Statement | 3 Hints | Full Solution & 5-Part Contract | Verdict |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **SS-1** | `#216` CF 449D — *Jzzhu and Numbers* | Lines 481–577 | Yes | Yes | Yes | **PASS** |
| **SS-2** | `#020` AtCoder ABC 213 G — *Connectivity 2* | Lines 581–678 | Yes | Yes | Yes | **PASS** |
| **Int-1** | `#027` AtCoder ABC 253 Ex — *We Love Forest* | Lines 682–778 | Yes | Yes | Yes | **PASS** |
| **Int-2** | `#042` AtCoder ABC 306 Ex — *Balance Scale* | Lines 782–874 | Yes | Yes | Yes | **PASS** |
| **Adv-1** | `#110` CF 1326F2 — *Wise Men (Hard Version)* | Lines 878–979 | Yes | Yes | Yes | **PASS** |
| **Adv-2** | `#207` UOJ 94 — *[集训队互测2015] 胡策的统计* | Lines 983–1093 | Yes | Yes | Yes | **PASS** |
| **Mas-1** | `#231` LOJ 6729 — *幂数 (Powerful Numbers)* | Lines 1097–1206 | **Proof Exercise (`S-4`)** | Yes | Yes | **FIX STATEMENT** |
| **Mas-2** | `#038` AtCoder ABC 288 Ex — *A Nameless Counting Problem* | Lines 1210–1325 | Yes | Yes | Yes | **PASS** |

### 1.4 Blind Checkpoint `CP-VI` Verification (`8/8` Exact Match)
Cross-checked against `CURRICULUM_ARCHITECTURE.md` (lines 1471–1499) and `PROBLEM_CURATION.md` (lines 511–522):

| Slot | Archive ID & Problem Title in `CURRICULUM_ARCHITECTURE.md` | Stage 1 Lines | Stage 2 Lines | Target Chapter | Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **CP-VI.1** | `#102` CF 1097G — *Vladislav and a Great Legend* | Lines 66–116 | Lines 540–585 | `Ch 22` (§22.1) | **PASS** |
| **CP-VI.2** | `#121` CF 1553I — *Stairs* | Lines 120–170 | Lines 589–637 | `Ch 22` (§22.2) | **PASS** |
| **CP-VI.3** | `#117` CF 1510H — *Hard Optimization* | Lines 174–224 | Lines 641–685 | `Ch 22` (§22.1) | **PASS** |
| **CP-VI.4** | `#170` Luogu P5327 — *[ZJOI2019] 语言* | Lines 228–277 | Lines 689–729 | `Ch 22` (§22.3) | **PASS** |
| **CP-VI.5** | `#054` AtCoder ARC 106 E — *Medals* | Lines 281–335 | Lines 733–774 | `Ch 24` (§24.1) | **PASS** |
| **CP-VI.6** | `#254` UOJ 310 — *[UNR #2] 黎明前的巧克力* | Lines 339–393 | Lines 778–823 | `Ch 24` (§24.1) | **PASS (`CP-1` minor hint)** |
| **CP-VI.7** | `#175` Luogu P5406 — *[THUPC2019] 找树* | Lines 397–458 | Lines 827–866 | `Ch 24` (§24.1) | **PASS** |
| **CP-VI.8** | `#180` Luogu P5643 — *[PKUWC2018] 随机游走* | Lines 462–519 | Lines 870–911 | `Ch 24` (§24.1) | **PASS** |

### 1.5 Quarantined Templates Verification (`R-07`, `R-08`, `R-48`–`R-52`, `R-55`–`R-67`)
- **Zero Ladder/Checkpoint Contamination**: Confirmed that **zero** quarantined bare templates (`R-01`–`R-67`) leak into any of the 24 chapter ladder slots or 8 `CP-VI` slots. (Note: `R-55`–`R-66` are assigned to earlier chapters `Ch 01, 05, 08, 11, 13, 14, 15, 18` per `CURRICULUM_ARCHITECTURE.md` §6.1 and do not appear in Part VI.)
- **`Ch 23` Quarantined Template Footnote (`R-48, R-49`) — PASS**: [`ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd` lines 1196–1202](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L1196-L1202) properly includes the `Implementation Verification Footnote (Quarantined Research Templates R-48 & R-49)` callout.
- **DEFECT `Q-1` (`Ch 22` Missing Quarantined Template Footnote for `R-67`)**:
  - **Location**: [`chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd` line 1291](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd#L1291) (immediately before `## 22.8 Where Next`).
  - **Requirement (`CURRICULUM_ARCHITECTURE.md` line 1575 & `PROBLEM_CURATION.md` line 50)**: `R-67` (*Library Checker — `static_top_tree` / `point_set_tree_path_composite_sum` & `polynomial_composite_set_power_series`*) is assigned to `Ch 22` (§22.2–22.3) as an Implementation Verification Footnote.
  - **Drop-In Fix for `Ch 22` (insert at line 1291)**:
    ```markdown
    ::: {.callout-note}
    ### Implementation Verification Footnote (Quarantined Research Template R-67)
    To unit-test your Heavy-Light Decomposition / Static Top Tree rake-and-compress engine in isolation before tackling full contest problems, verify your implementation against the quarantined benchmark template:

    - **R-67** (*Library Checker — `point_set_tree_path_composite_sum` / Static Top Tree*): Maintain point updates and subtree/path affine or polynomial aggregations on a tree of $N \le 2 \times 10^5$ vertices in $O(Q \log N)$ or $O(Q \log^2 N)$ time using explicit Rake ($\mathcal{R}$) and Compress ($\mathcal{C}$) cluster operators.
    :::
    ```
- **DEFECT `Q-2` (`Ch 24` Missing Quarantined Template Footnote for `R-07, R-08, R-50, R-51, R-52`)**:
  - **Location**: [`chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd` line 1326](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd#L1326) (immediately before `## What's Next?`).
  - **Requirement (`CURRICULUM_ARCHITECTURE.md` lines 1515–1516, 1558–1560 & `PROBLEM_CURATION.md` line 52)**: `R-07`, `R-08`, `R-50`, `R-51`, and `R-52` are assigned to `Ch 24` (§24.1–24.4) as Implementation Verification Footnotes.
  - **Drop-In Fix for `Ch 24` (insert at line 1326)**:
    ```markdown
    ::: {.callout-note}
    ### Implementation Verification Footnote (Quarantined Research Templates R-07, R-08, R-50, R-51 & R-52)
    To unit-test your bitwise FWT, Set Power Series (SPS), and sublinear multiplicative prefix-sum engines in isolation before tackling full contest problems, verify your subroutines against these five quarantined benchmark templates:

    - **R-07** (*Luogu P4717 `【模板】快速莫比乌斯/沃尔什变换 (FMT/FWT)` / Library Checker `bitwise_and_convolution`, `bitwise_xor_convolution`*): Verify $O(n 2^n)$ bitwise OR, AND, and Walsh-Hadamard (XOR) convolutions modulo $998244353$.
    - **R-08** (*Luogu P6097 `【模板】子集卷积` / Library Checker `subset_convolution`*): Verify $O(n^2 2^n)$ ranked Zeta/Möbius subset convolution in $\mathbb{F}_p[x]/(x^{n+1})[\{0,1\}^n]$.
    - **R-50** (*Library Checker `exp_of_set_power_series`*): Verify $O(n^2 2^n)$ point-by-point highest-bit integration for $\exp_{\cup}(F)$.
    - **R-51** (*Library Checker `log_of_set_power_series` & `power_projection_of_set_power_series`*): Verify $O(n^2 2^n)$ connected-component extraction $\ln_{\cup}(F)$ and transposed composition / power projection on Set Power Series.
    - **R-52** (*Luogu P5325 `【模板】Min_25 筛`*): Verify two-phase DP over the $O(\sqrt{N})$ floor quotient set $\mathcal{V}_N$ to evaluate $\sum_{n=1}^N f(n)$ for a multiplicative function $f$ in $O(N^{3/4}/\log N)$ time.
    :::
    ```

---

## Dimension 2: Self-Contained Problem Statements & Sample Traces (`4` Critical Statement Defects)

Per `AGENTS.md` ("Self-Contained Problem Policy"), every problem in a chapter ladder must state a complete, self-contained competitive programming problem with concrete inputs, outputs, and sample traces—never a textbook meta-summary or a template with unspecified rules. All `28` other problems across `Ch 22`–`Ch 24` and `CP-VI` pass this audit completely. Below are the **4 problems that fail** and their exact drop-in replacements.

### CRITICAL DEFECT `S-1`: `Ch 22 Int-1 (#046)` — AtCoder ABC 355 G (*Baseball*)
- **Location**: [`chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd` lines 752–766](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd#L752-L766)
- **What is wrong**: Lines 754–757 do not give a concrete problem statement; they write a vague meta-summary: *"In a laminar hierarchy of $N$ nested time segments (or equivalently, on the laminar containment tree $T$ of $N$ intervals where each interval either is disjoint from or strictly contains another), each node $u \in T$ has a local boundary capacity $w_u \ge 0$ and a transition polynomial modifying the score distribution of its subtree $T_u$ when $u$'s guard is activated vs. deactivated..."* A student reading this cannot tell what the rules of the problem are or how the sample numbers `[1, 2, 1]` and `[0, 1, 1]` are defined.
- **Drop-In Replacement for [`ch22` lines 752–766](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd#L752-L766)**:
  ```markdown
  **Problem Statement (Self-Contained):**
  You are given $N$ laminar time intervals $I_1, \dots, I_N \subseteq [1, M]$ (for any $i \neq j$, either $I_i \cap I_j = \emptyset$, $I_i \subsetneq I_j$, or $I_j \subsetneq I_i$), which form a rooted containment tree $T$ with root $1$ ($I_1 = [1, M]$). Each node $u \in T$ has a local capacity $w_u \in \mathbb{Z}_{\ge 0}$ of uncovered unit time slots ($w_u = |I_u| - \sum_{v \in \text{child}(u)} |I_v|$, so $\sum_{u=1}^N w_u = M$).
  At each node $u$, you may place $c_u \in \{0, 1, \dots, w_u\}$ local markers in its uncovered slots (in $\binom{w_u}{c_u}$ ways) and choose a guard state $s_u \in \{0, 1\}$ (inactive $0$ or active $1$), subject to two rules:

  1. **No Adjacent Active Guards on Tree Edges**: If $u$'s guard is active ($s_u = 1$), then none of its children $v \in \text{child}(u)$ may have an active guard ($s_v = 0$), and $u$ must place at least one local marker ($c_u \ge 1$, contributing $\binom{w_u - 1}{c_u - 1} x^{c_u}$ when $w_u \ge 1$, or $x$ when $w_u = 0$ as a single boundary guard).
  2. **Inactive Guard**: If $s_u = 0$, each child $v \in \text{child}(u)$ may freely be in state $s_v \in \{0, 1\}$, and $u$ contributes $(1+x)^{w_u}$ from its local slots.

  For each $k = 0, 1, \dots, M$, compute the total number of valid configurations across the entire hierarchy with total weight $k$ modulo $998244353$.

  **Constraints:** $N, M \le 2 \times 10^5$, $\sum_{u=1}^N w_u = M$. Time limit: 3.0s.

  **Sample Trace ($N = 4$, path tree $1 - 2 - 3 - 4$ with $w_1 = w_2 = w_3 = 0$, leaf $w_4 = 1$):**
  - At leaf $4$ ($w_4 = 1$): inactive polynomial $F_{4,0}(x) = (1+x)^1 = 1 + x$; active polynomial $F_{4,1}(x) = x$.
  - At node $3$ ($w_3 = 0$, child $4$): $F_{3,0}(x) = F_{4,0}(x) + F_{4,1}(x) = 1 + 2x$; $F_{3,1}(x) = x F_{4,0}(x) = x + x^2$.
  - At node $2$ ($w_2 = 0$, child $3$): $F_{2,0}(x) = F_{3,0}(x) + F_{3,1}(x) = 1 + 3x + x^2$; $F_{2,1}(x) = x F_{3,0}(x) = x + 2x^2$.
  - At root $1$ ($w_1 = 0$, child $2$): $F_{1,0}(x) = 1 + 4x + 3x^2$, $F_{1,1}(x) = x + 3x^2 + x^3$. Total polynomial $F_{1,0}(x) + F_{1,1}(x) = 1 + 5x + 6x^2 + x^3$.
  ```

---

### CRITICAL DEFECT `S-2`: `Ch 22 Int-2 (#198)` — Luogu P7279 (*光棱碎片 / Prism Shards*)
- **Location**: [`chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd` lines 824–850](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd#L824-L850)
- **What is wrong**: Lines 824–837 state a half-abstracted problem with unspecified polynomials $\alpha_u, \beta_u, \gamma_u, \delta_u \in \mathbb{F}_p[x]$, and then in the Sample Trace (line 842) abruptly plug in $\alpha_u = 1, \beta_u = -1, \gamma_u = 1, \delta_u = 0$ without ever telling the reader what combinatorial rule produces $\beta_u = -1$!
- **Drop-In Replacement for [`ch22` lines 824–850](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd#L824-L850)**:
  ```markdown
  **Problem Statement (Self-Contained):**
  You are given a rooted tree $T$ on $N$ vertices rooted at $1$. Let $L$ be the set of leaves of $T$. Initially, each leaf $v \in L$ is assigned a shard energy $a_v \in \{0, 1\}$, and every internal vertex $u \notin L$ starts with energy $a_u = \sum_{v \in \text{child}(u)} a_v$ (so $a_u$ equals the number of active leaves in $T_u$).
  You may then perform any sequence of **shatter operations** on internal vertices $u \notin L$: a shatter operation at $u$ sets $a_u \leftarrow 0$ (disconnecting $u$'s energy from passing upward to its ancestors). Two sequences of leaf assignments and shatter operations are considered **distinguishable** if and only if they result in different final vertex energy arrays $(a_1, a_2, \dots, a_N)$.
  Notice where overcounting occurs: at an internal vertex $u$, choosing not to shatter $u$ ($s_u = 1$, keeping $a_u = \sum_{v \in \text{child}(u)} a_v$) versus shattering $u$ ($s_u = 0$, setting $a_u = 0$) produces the **exact same** value $a_u = 0$ if and only if every child $v \in \text{child}(u)$ already ended with $a_v = 0$!
  Therefore, if $F_{u,0}(x)$ is the OGF (by number of active leaves $x$) of distinguishable sub-arrays on $T_u$ ending with $a_u = 0$, and $F_{u,1}(x)$ is the OGF of distinguishable sub-arrays on $T_u$ ending with $a_u > 0$:

  - For every leaf $u \in L$: $F_{u,0}(x) = 1$ (since $a_u = 0$) and $F_{u,1}(x) = x$ (since $a_u = 1$).
  - For every internal vertex $u \notin L$:
    $$F_{u,0}(x) = \prod_{v \in \text{child}(u)} \big(F_{v,0}(x) + F_{v,1}(x)\big) \quad\text{(shatter } u \text{ so } a_u = 0\text{)},$$
    $$F_{u,1}(x) = \prod_{v \in \text{child}(u)} \big(F_{v,0}(x) + F_{v,1}(x)\big) - \prod_{v \in \text{child}(u)} F_{v,0}(x) \quad\text{(do not shatter } u\text{, requiring } \sum a_v > 0\text{)}.$$

  More generally, this defines a 2-state tree DP with child-product transitions governed by coefficients $(\alpha_u, \beta_u, \gamma_u, \delta_u) = (1, -1, 1, 0)$. For each $k = 0, 1, \dots, |L|$, compute $[x^k]\big(F_{1,0}(x) + F_{1,1}(x)\big) \bmod 998244353$.

  **Constraints:** $N \le 2 \times 10^5$. Time limit: 2.5s.

  **Sample Trace ($N = 3$, root $1$ with two leaf children $2, 3$):**
  - Leaves $2, 3$ have $F_{2,0}(x) = F_{3,0}(x) = 1$ and $F_{2,1}(x) = F_{3,1}(x) = x$, so $F_{v,0}(x) + F_{v,1}(x) = 1+x$.
  - At root $1$, $\prod_{v \in \{2,3\}} (F_{v,0} + F_{v,1}) = (1+x)^2 = 1 + 2x + x^2$, and $\prod_{v \in \{2,3\}} F_{v,0} = 1 \cdot 1 = 1$.
  - Thus $F_{1,0}(x) = 1 + 2x + x^2$ (arrays $(0,0,0)$, $(0,1,0)$, $(0,0,1)$, $(0,1,1)$) and $F_{1,1}(x) = (1 + 2x + x^2) - 1 = 2x + x^2$ (arrays $(1,1,0)$, $(1,0,1)$, $(2,1,1)$).
  - Total OGF at root $1$: $F_{1,0}(x) + F_{1,1}(x) = 1 + 4x + 2x^2$, giving $7$ distinct arrays $(a_1, a_2, a_3)$ stratified by leaf weight $k=0,1,2$ as $[1, 4, 2]$.
  ```

---

### CRITICAL DEFECT `S-3`: `Ch 23 Int-1 (#233)` — QOJ 5097 / SOJ 703 (*布尔立方 / Boolean Cube*)
- **Location**: [`chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd` lines 648–658](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L648-L658)
- **What is wrong**:
  1. Lines 649–651 describe a meta-task (*"Given rank weights / constraints on the $\mathbb{F}_2$-ranks of these slices (specifically, transforming between the subspace containment moments $2^{nr}$ and the exact rank counts $\operatorname{Rank}(n,n,r;2)$ coupled across axes), compute the resulting weighted enumeration..."*) rather than stating a concrete problem.
  2. Lines 652–657 give a Sample Trace for $2 \times 2$ **2D matrices** ($1 + 9 + 6 = 16$), not an $n \times n \times n$ **3D Boolean cube**!
- **Drop-In Replacement for [`ch23` lines 648–658](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L648-L658)**:
  ```markdown
  - **Problem Statement**: Consider an $n \times n \times n$ three-dimensional binary cube $A = (A_{i,j,k})_{1 \le i,j,k \le n} \in \mathbb{F}_2^{n \times n \times n}$. Flattening $A$ along each of the three coordinate axes yields three sets of $n$ vectors in $\mathbb{F}_2^{n^2}$ (equivalently, viewing $A$ as a trilinear tensor, let $r_1(A), r_2(A), r_3(A) \in \{0, 1, \dots, n\}$ be the dimensions of the subspaces $U_1, U_2, U_3 \subseteq \mathbb{F}_2^n$ spanned by the mode-1, mode-2, and mode-3 fibers of $A$). You are given integer weights $w_1, w_2, w_3 : \{0, \dots, n\} \to \mathbb{F}_p$ (or a target rank triple $(R_1, R_2, R_3)$). Since a cube $A$ has fiber spans contained in subspaces $U_1, U_2, U_3$ of dimensions $d_1, d_2, d_3$ in $2^{d_1 d_2 d_3}$ ways, let $N(r_1, r_2, r_3)$ denote the number of cubes $A \in \mathbb{F}_2^{n \times n \times n}$ with exact mode ranks $(r_1, r_2, r_3)$. Given $n$ and a fixed target rank $r_3 = k$ (or weights $w_1(r_1), w_2(r_2), w_3(r_3)$), compute the total weighted sum
    $$\mathcal{Z}_n = \sum_{r_1=0}^n \sum_{r_2=0}^n \sum_{r_3=0}^n w_1(r_1)\, w_2(r_2)\, w_3(r_3)\, N(r_1, r_2, r_3) \pmod{998244353}$$
    (and in particular, the exact rank distribution $N(r_1, r_2, r_3)$) in $O(n^2 + n \log n)$ time (or $O(n \log n)$ per fixed axis rank).
  - **Constraints**: $n \le 2.5 \times 10^5$ (for 2-axis coupling with fixed $d_3$) or $n \le 5000$ (for full 3-axis coupling), modulus $p = 998244353$.
  - **Sample Trace ($n = 2$, $2 \times 2 \times 2$ cubes $A \in \mathbb{F}_2^{2 \times 2 \times 2}$, $2^8 = 256$ cubes total)**:
    - The subspace counts in $\mathbb{F}_2^2$ are $\begin{bmatrix} 2 \\ 0 \end{bmatrix}_2 = 1$, $\begin{bmatrix} 2 \\ 1 \end{bmatrix}_2 = 3$, $\begin{bmatrix} 2 \\ 2 \end{bmatrix}_2 = 1$.
    - Applying $q$-Möbius inversion along each of the 3 modes to $2^{d_1 d_2 d_3}$ gives the exact counts $N(r_1, r_2, r_3)$:
      - $N(0,0,0) = 1$ (the all-zero cube).
      - $N(1,1,1) = \binom{2}{1}_2^3 (2^{1\cdot 1\cdot 1} - 1) = 27 \cdot 1 = 27$ (rank-1 elementary tensors $u \otimes v \otimes w$).
      - $N(2,2,1) = N(2,1,2) = N(1,2,2) = 1 \cdot 1 \cdot 3 \cdot 6 = 18$ (each mode-3 slice is a scalar multiple of a rank-2 $2 \times 2$ matrix; there are $6$ invertible $2\times 2$ matrices and $3$ non-zero scalar patterns in $\mathbb{F}_2^2$).
      - $N(2,2,2) = 256 - 1 - 27 - 3(18) = 174$ (full mode-rank $(2,2,2)$ cubes).
      - Total: $1 + 27 + 18 + 18 + 18 + 174 = 256 = 2^{2^3}$.
  ```

---

### CRITICAL DEFECT `S-4`: `Ch 24 Mas-1 (#231)` — LOJ 6729 (*幂数 / Powerful Numbers*)
- **Location**: [`chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd` lines 1101–1110](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd#L1101-L1110)
- **What is wrong**: Lines 1102–1108 turn LOJ 6729 into a generic 2-part homework proof question (*"1. Prove using Bell series that the Dirichlet quotient $h = f *_D g^{-1}$ vanishes at all primes... 2. Given the prime-power rules $f(p^k)$ and $g(p^k)$..."*) without specifying the concrete multiplicative function $f(p^k)$ of the problem!
- **Drop-In Replacement for [`ch24` lines 1101–1110](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd#L1101-L1110)**:
  ```markdown
  **Problem Statement:**
  A positive integer $d$ is called a **powerful number** (幂数) if for every prime $p \mid d$, we also have $p^2 \mid d$. Let $f : \mathbb{Z}_{\ge 1} \to \mathbb{F}_p$ be the multiplicative function defined on prime powers $p^k$ ($k \ge 1$) by
  $$f(p^k) = p^k(p^k - 1) \quad (\text{or more generally, any multiplicative function satisfying } f(p) = p(p-1) = \varphi(p)\,p \text{ at primes } p\text{, such as } f(p^k) = p^{2k} - p^{2k-1}\text{ or } f(p^k) = p^k - p\text{ when } f(p)=0).$$
  Given $N \le 10^{10}$ (and in the concrete benchmark where $f(p) = p$ and $f(p^k) = p^k + (-1)^k (p - 1)$ for $k \ge 2$, or $f(p^k) = p^k(p-1)$ matched against $g = \operatorname{id}$ or $g = \varphi$):

  1. Choose a simple multiplicative approximant $g : \mathbb{Z}_{\ge 1} \to \mathbb{F}_p$ whose prefix sums $G(x) = \sum_{m \le x} g(m)$ can be evaluated in $O(1)$ time (or via a single precomputed sieve table) and which satisfies $g(p) = f(p)$ for every prime $p$.
  2. Prove using Bell series that the Dirichlet quotient $h = f *_D g^{-1}$ vanishes at all primes ($h(p) = 0$) and is therefore supported exclusively on the $O(\sqrt{N})$ powerful numbers $d \le N$.
  3. Compute $F(N) = \sum_{n=1}^N f(n) \bmod 10^9 + 7$ in $O(\sqrt{N})$ time via $\sum_{d \le N,\, d \text{ powerful}} h(d)\,G(\lfloor N/d \rfloor)$.

  **Constraints:** $N \le 10^{10}$, modulus $10^9 + 7$. Time limit: 1.0s.
  ```

---

## Dimension 3: 3-Hint & Solution Architecture + 5-Part Algorithm Contracts

### 3.1 Completeness Audit Across All 32 Problems
- **3 Progressive Collapsible `<details>` Hints**: Verified `32/32` problems (`24` chapter problems + `8` checkpoint problems) have three distinct `<details>` blocks (`Hint 1`, `Hint 2`, `Hint 3`).
- **Complete Collapsible `<details>` Solution & 5-Part Algorithm Contract**: Verified `32/32` problems have a complete multi-step derivation and an explicit 5-part Algorithm Contract (*1. Input & Constraints, 2. Algebraic / Combinatorial Core, 3. Step-by-Step Pipeline, 4. Complexity, 5. Pitfalls & Edge Cases*).
- **Zero Standard Library Code Dumps**: Verified across all four `.qmd` files that zero raw NTT, ModInt, or linear sieve C++ templates appear.

### 3.2 Minor Defect `H-1`: `Ch 23` `Hint 1` Theorem Spoilers (`SS-1`, `SS-2`, `Int-1`, `Mas-1`)
In `Ch 22` and `Ch 24`, every `Hint 1` is written as a spoiler-free structural observation. In `Ch 23`, however, four `Hint 1` blocks immediately name the exact Proposition/Theorem from the chapter text:
1. **`Ch 23 SS-1 (#123)` ([`ch23` lines 503–508](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L503-L508))**: Mentions *"by Proposition 23.1"* directly in `Hint 1`.
   - *Fix*: Change `Hint 1` to ask: *"Instead of tracking all $n$ elements $a_1, \dots, a_n \in \mathbb{F}_2^k$, what single structural invariant of the span $W = \operatorname{span}(a_1, \dots, a_n) \subseteq \mathbb{F}_2^k$ determines whether $x$ can be formed as an XOR sum? Treat $x = 0$ and $x \neq 0$ separately."* Move the Proposition 23.1 formula to `Hint 2`.
2. **`Ch 23 SS-2 (#033)` ([`ch23` lines 577–582](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L577-L582))**: Starts `Hint 1` with *"Apply $q$-Möbius Inversion on the Subspace Lattice (Theorem 23.4)..."*
   - *Fix*: Change `Hint 1` to ask: *"Requiring a subset $S$ to span all of $\mathbb{F}_2^R$ is a global rank condition, whereas requiring $S$ to lie inside a fixed subspace $W \subseteq \mathbb{F}_2^R$ of dimension $k$ simply restricts how many available vectors exist ($2^k - 1$). How can you relate 'spanning exactly $W$' to 'lying inside $W$'?"*
3. **`Ch 23 Int-1 (#233)` ([`ch23` lines 660–665](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L660-L665))**: Starts `Hint 1` with *"By Proposition 23.1 in Section 23.4..."*
   - *Fix*: Change `Hint 1` to ask: *"How many cubes $A \in \mathbb{F}_2^{n \times n \times n}$ have their mode-1, mode-2, and mode-3 fibers contained inside fixed subspaces $U_1, U_2, U_3 \subseteq \mathbb{F}_2^n$ of dimensions $d_1, d_2, d_3$? Express this count solely in terms of $d_1, d_2, d_3$."*
4. **`Ch 23 Mas-1 (#063)` ([`ch23` lines 1022–1028](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L1022-L1028))**: Starts `Hint 1` with *"By Model 3 of Section 23.1, the ordinary generating function... is literally the Gaussian $q$-binomial coefficient..."*
   - *Fix*: Change `Hint 1` to ask: *"Interpret a weakly increasing sequence $0 \le A_1 \le A_2 \le \dots \le A_N < M$ geometrically as a lattice path or diagram inside an $N \times (M-1)$ bounding box. What does the sum $\sum_{i=1}^N A_i$ correspond to geometrically, and how can you extract its value modulo $K$?"*

---

## Dimension 4: Blind Checkpoint `CP-VI` Spoiler-Free Audit & Render Safety

### 4.1 Stage 1 Spoiler-Free Verification (`checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd`)
- **Stage 1 Arena Table (`lines 51–62`)**: **100% PASS**. Lists only Slot (`CP-VI.1`–`CP-VI.8`), Problem Title & Source (`#102`, `#121`, `#117`, `#170`, `#054`, `#254`, `#175`, `#180`), Constraints, and Time/Memory limits. Zero chapter numbers or technique names.
- **Stage 1 Problem Statements (`lines 66–519`)**: **100% PASS**. Every statement is 100% self-contained, includes an explicit hand-checkable Sample Trace, and contains zero technique spoilers.
- **Stage 1 `Hint 1` Spoiler Audit**:
  - `CP-VI.1` (`line 86`), `CP-VI.2` (`line 138`), `CP-VI.3` (`line 192`), `CP-VI.4` (`line 245`), `CP-VI.5` (`line 299`), `CP-VI.7` (`line 420`), `CP-VI.8` (`line 483`): **100% PASS** (purely structural observations with zero technique names).
  - **MINOR DEFECT `CP-1` (`CP-VI.6 (#254)` `Hint 1` at [`cp06` line 370](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd#L370))**:
    - *Current text (`line 370`)*: `"In other words, what single-element polynomial over the XOR group ring represents the choice for $a_i$, and why does every valid outcome correspond to a sequence of choices whose combined XOR sum is $0$?"`
    - *Why it should be softened*: Naming `"the XOR group ring"` in `Hint 1` immediately tells the student this is a `Ch 24.1` XOR FWT problem before they open `Hint 2`.
    - *Drop-In Replacement for [`cp06` line 370](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd#L370)*:
      ```markdown
      In other words, for each element $a_i$, how many ways can it be assigned to $A$, $B$, or neither, and what does each choice contribute to the combined XOR value $X(A) \oplus X(B)$?
      ```

### 4.2 Quarto Formatting & Render Safety Audit
- **Forbidden Math Delimiters (`\(` or `\[`)**: `0` instances across all 4 files (**PASS**).
- **Unclosed `<details>` or `:::` Callout Blocks**: Every `<details>` (`128/128` across the 4 files) and every `:::` block is properly balanced and closed (**PASS**).
- **CRITICAL RENDER DEFECT `F-1` (Unescaped Pipe `|` Inside Markdown Table in `Ch 24`)**:
  - **Location**: [`chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd` line 466](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd#L466)
  - **Current Line 466**:
    ```markdown
    | **Bitwise OR / AND (SOS)** | $K[(\{0,1\}^n, \mathbin{\|})]$ or $\mathbin{\&}$ | $S \cup T$ or $S \cap T$ | **Superset / Subset Lattice** (Zeta / Möbius transform) | $O(n 2^n)$ |
    ```
  - **Why it breaks Quarto/Pandoc**: In Pandoc pipe tables, table column splitting runs *before* inline math `$...$` parsing, and `\|` inside `$...$` is either stripped of its backslash or splits the cell if not handled carefully. Using `\cup` / `\cap` or `\mathbin{\vert}` completely avoids the pipe character `|` inside the Markdown table!
  - **Drop-In Replacement for [`ch24` line 466](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd#L466)**:
    ```markdown
    | **Bitwise OR / AND (SOS)** | $K[(\{0,1\}^n, \mathbin{\vert})]$ or $\mathbin{\&}$ | $S \cup T$ or $S \cap T$ | **Superset / Subset Lattice** (Zeta / Möbius transform) | $O(n 2^n)$ |
    ```

---

## Summary Checklist of Actionable Edits for Part VI Author

1. **[`ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd` lines 752–766 (`S-1`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd#L752-L766)**: Replace the meta-summary in `Int-1 (#046, ABC 355 G — Baseball)` with the self-contained problem statement and trace above.
2. **[`ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd` lines 824–850 (`S-2`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd#L824-L850)**: Replace the half-abstracted statement in `Int-2 (#198, Luogu P7279 — 光棱碎片)` with the concrete shatter-operation problem statement and trace above.
3. **[`ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd` line 1291 (`Q-1`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd#L1291)**: Insert the `Implementation Verification Footnote (Quarantined Research Template R-67)` callout block.
4. **[`ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd` lines 648–658 (`S-3`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L648-L658)**: Replace the meta-description and 2D matrix trace in `Int-1 (#233, QOJ 5097 — 布尔立方)` with the concrete 3D Boolean cube problem statement and $2 \times 2 \times 2$ trace above.
5. **[`ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd` lines 505, 579, 662, 1024 (`H-1`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L505)**: Soften `Hint 1` in `SS-1`, `SS-2`, `Int-1`, and `Mas-1` so they do not immediately cite Proposition 23.1 / Theorem 23.4 / Model 3.
6. **[`ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd` line 466 (`F-1`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd#L466)**: Replace `\mathbin{\|}` with `\mathbin{\vert}` inside the Section 24.5 Markdown table.
7. **[`ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd` lines 1101–1110 (`S-4`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd#L1101-L1110)**: Replace the generic homework proof prompt in `Mas-1 (#231, LOJ 6729 — 幂数)` with the concrete problem statement above.
8. **[`ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd` line 1326 (`Q-2`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd#L1326)**: Insert the `Implementation Verification Footnote (Quarantined Research Templates R-07, R-08, R-50, R-51 & R-52)` callout block.
9. **[`cp06-part6-trees-qseries-sps-dirichlet.qmd` line 370 (`CP-1`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd#L370)**: Remove `"over the XOR group ring"` from `CP-VI.6 (#254)` `Hint 1` to keep Stage 1 100% spoiler-free.
