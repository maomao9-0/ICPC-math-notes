# Part II Critic B Audit Report: Problem Ladders (`Ch 05`–`Ch 08`) & Blind Checkpoint II (`CP-II`)

- **Auditor**: Part II Critic B (Problem Ladders, Self-Contained Inline Statements, Progressive Hints & Blind Checkpoint Spoiler-Free Auditor)
- **Date**: 2026-10-14
- **Audited Files**:
  1. [ch05-rational-bostan-mori-berlekamp-massey.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd) (Lines 730–1718, 8 problems)
  2. [ch06-binomial-snake-oil-taylor-shift-stirling.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd) (Lines 718–1260, 8 problems)
  3. [ch07-roots-of-unity-cyclotomic-czt.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd) (Lines 572–1414, 8 problems)
  4. [ch08-connected-component-ie-rook-goulden-jackson.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd) (Lines 532–1206, 8 problems)
  5. [cp02-part2-rational-transforms-ie.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd) (Lines 1–1270, 8 checkpoint problems)
- **Reference Spec**: [CURRICULUM_ARCHITECTURE.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md) (Lines 340–505, 1210–1245) & [AGENTS.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/AGENTS.md)

---

## Executive Summary & Compliance Matrix

| File | Check 1: ID/Title Match & Zero Split/Hedged Variants | Check 2: Self-Contained Statements, Constraints & Inline Sample Traces ($N \le 4$) | Check 3: 3 Progressive Hints & Full Solution with Complexity Contract | Check 4: 100% Spoiler-Free Stage 1 (`CP-II` Only) | Overall Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ch 05** | **FAIL** (2 hedged variants: `#040`, `#177`) | **FAIL** (0/8 have visible inline sample traces; 3/8 lack traces even in solutions) | **FAIL** (Math error in `#073` Hint 3; draft `"wait..."` text in `#177`, `#073`; Ch 06 forward refs in `#069`, `#177`) | N/A | **NEEDS REVISION** |
| **Ch 06** | **FAIL** (1 hedged/incomplete statement: `#080`) | **FAIL** (0/8 have visible inline sample traces; 0/8 have traces in solutions) | **FAIL** (Draft `"WAIT: no C(d,k)! Hold on!"` text in `#080` Hint 2; Ch 13 forward ref in `#080`) | N/A | **NEEDS REVISION** |
| **Ch 07** | **PASS** (8/8 match & unhedged) | **FAIL** (0/8 have visible inline sample traces; 0/8 have traces in solutions) | **PASS** (All 8 have 3 progressive hints, full derivations, and complexity contracts) | N/A | **NEEDS SAMPLE TRACES** |
| **Ch 08** | **FAIL** (3 split `"Part I/II"` or `"Part A/B"` problems: `#241`, `#139`, `#052`) | **FAIL** (0/8 have visible inline sample traces; `#139` Part II & `#052` Part A lack concrete statements) | **PASS** (All 8 have 3 hints and full derivations, modulo the split-problem structure) | N/A | **NEEDS REVISION** |
| **CP-II** | **FAIL** (`CP-II.8` (`#141`) is split into `Part A / Part B`) | **FAIL** (0/8 have visible inline sample traces in Stage 1 statements; all traces are hidden in `<details>`) | **FAIL** (Unedited `"wait..."` stream-of-consciousness in `CP-II.1` Hint 3, `CP-II.3` trace, `CP-II.6` trace) | **CRITICAL FAIL** (Pre-Stage-1 Rubric & Mermaid chart spoil all 8 problems; `Hint 1` leaks techniques/chapters in 6/8 problems) | **CRITICAL REVISION NEEDED** |

---

## Check 1 Audit: Exact Problem ID & Title Match + Zero Split/Hedged Variants

### 1.1 Master Verification Table (40 / 40 Problems)

All 40 problem IDs (`#xxx`) and slots across `Ch 05`–`Ch 08` and `CP-II` match `CURRICULUM_ARCHITECTURE.md`:

- **Ch 05**: `SS-1 (#104)`, `SS-2 (#034)`, `Int-1 (#187)`, `Int-2 (#069)`, `Adv-1 (#040)`, `Adv-2 (#081)`, `Mas-1 (#177)`, `Mas-2 (#073)` — **8/8 IDs match**.
- **Ch 06**: `SS-1 (#005)`, `SS-2 (#055)`, `Int-1 (#193)`, `Int-2 (#080)`, `Adv-1 (#094)`, `Adv-2 (#096)`, `Mas-1 (#098)`, `Mas-2 (#109)` — **8/8 IDs match**.
- **Ch 07**: `SS-1 (#224)`, `SS-2 (#248)`, `Int-1 (#178)`, `Int-2 (#143)`, `Adv-1 (#147)`, `Adv-2 (#012)`, `Mas-1 (#092)`, `Mas-2 (#168)` — **8/8 IDs match**.
- **Ch 08**: `SS-1 (#018)`, `SS-2 (#241)`, `Int-1 (#155)`, `Int-2 (#089)`, `Adv-1 (#067)`, `Adv-2 (#139)`, `Mas-1 (#052)`, `Mas-2 (#137)` — **8/8 IDs match**.
- **CP-II**: `CP-II.1 (#085)`, `CP-II.2 (#152)`, `CP-II.3 (#251)`, `CP-II.4 (#252)`, `CP-II.5 (#100)`, `CP-II.6 (#029)`, `CP-II.7 (#162)`, `CP-II.8 (#141)` — **8/8 IDs match**.

### 1.2 Violations of the Zero Split `"Part A / Part B"` & Zero Hedged `"Variant A / Variant B"` Policy

7 problems across `Ch 05`, `Ch 06`, `Ch 08`, and `CP-II` violate the editorial policy against split `"Part A / Part B"` or hedged `"Variant A / Variant B"` problem statements:

1. **[Ch 05 `Adv-1 (#040)` — `AtCoder ABC 300 Ex: Fibonacci: Revisited`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1210-L1311)**:
   - **Defect**:
     - Line 1210 hedges between 0-indexed $a_N$, 1-indexed $A_N = a_{N-1}$, and a fabricated **"Submask-Sum Variant $\sum_{M \subseteq N} a_M$ where $(M \mathbin{\&} N) = M$ is a bitwise submask of $N$"**.
     - Lines 1230, 1236, 1251–1268, and 1293–1311 continue this split, and line 1295 falsely states: *"In the official AtCoder ABC 300 Ex variant where we sum $a_M$ over all bitwise submasks $M \subseteq N$..."* In reality, official AtCoder ABC 300 Ex asks solely for the single term $A_N \bmod 998244353$ (which matches `CURRICULUM_ARCHITECTURE.md` line 386: *"Bostan–Mori at $N \le 10^{18}$ on $Q(x) = 1 - x - \dots - x^K$, plus the $(1-x)Q(x) = 1 - 2x + x^{K+1}$ 3-sparse trick"*).
   - **Required Fix**: Remove the fabricated bitwise submask-sum variant from lines 1210, 1230, 1236, 1251–1268, and 1293–1311. State the exact official ABC 300 Ex problem ($A_1 = \dots = A_K = 1$, $A_n = A_{n-1} + \dots + A_{n-K}$ for $n > K$, compute $A_N \bmod 998244353$), and use Step 4 of the solution to detail the $(1-x)Q(x) = 1 - 2x + x^{K+1}$ 3-sparse denominator optimization from `CURRICULUM_ARCHITECTURE.md`.

2. **[Ch 05 `Mas-1 (#177)` — `Luogu P5487: [BJOI 2019] 勘破神机`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1441-L1557)**:
   - **Defect**:
     - Line 1453 hedges: `*(or in the 1 \times 3 domino variant, g_1 = 2, g_r = 4g_{r-1} - g_{r-2})*`.
     - Worse, in the $m=2$ solution (lines 1441 vs. 1553–1556), line 1441 defines $f_0 = 1, f_1 = 2, f_2 = 7$, while line 1553 writes $A = \frac{3+\sqrt{3}}{6}, B = \frac{3-\sqrt{3}}{6}$ (which corresponds to $f_1 = 3, f_2 = 11$, i.e., $n$ vs. $2n$ column scaling), followed on line 1556 by an unedited parenthetical self-argument: `*(Check: n = 0 => A + B = 1; n = 1 => A\alpha + B\beta = 3 if f_1 = 3, or for f_1 = 2, f_2 = 7, A = 1/2, B = 1/2...)*`!
   - **Required Fix**: Use the official BJOI 2019 definitions consistently throughout both the statement and solution:
     - For $m = 2$ ($2 \times 2n$ board with $1 \times 2$ dominoes, or $3 \times 2n$ board where $f_0 = 1, f_1 = 3, f_2 = 11$ and $f_n = 4f_{n-1} - f_{n-2}$): fix $f_0 = 1, f_1 = 3, f_2 = 11$ in line 1441 so that $A = \frac{3+\sqrt{3}}{6}, B = \frac{3-\sqrt{3}}{6}$ in line 1553 is 100% consistent, and delete the hedged parentheticals in lines 1453 and 1556.

3. **[Ch 06 `Int-2 (#080)` — `AtCoder KUPC 2019 K: One or All`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L911-L982)**:
   - **Defect**:
     - Line 917 introduces `"and N integers B_1, B_2, ..., B_N"`, then line 918 defines $S_j$ without ever referencing $B_j$, and line 919 hedges: `"compute the product over all 1 <= j <= N of the linear combinations S_j = ... or more generally evaluate the polynomial transforms linking P(x) to the Krawtchouk basis (1+x)^k (1-x)^{d-k}."`
     - Line 980 then hand-waves: `*(If the problem further combines S_{k+1} with a subproduct tree over B_j, that takes at most O(N \log^2 N) time.)*`
     - Line 913 also lists `Ch 01 (Subproduct Tree)` as a prerequisite, even though Subproduct Trees are taught in **Chapter 13** (Part III)!
   - **Required Fix**: State a single, self-contained, unhedged problem requiring only Part I–II tools (`Ch 01`–`Ch 06`): Given $A_0, A_1, \dots, A_d$, compute for all $0 \le k \le d$ the Krawtchouk / signed-subset sums $S_k = \sum_{i=0}^d A_i [x^i] (1 + x)^k (1 - x)^{d - k} \pmod{998244353}$ in $O(d \log d)$ time via two Taylor shifts and one convolution. Remove the unused $B_1, \dots, B_N$ and the Chapter 13 subproduct tree reference.

4. **[Ch 08 `SS-2 (#241)` — `yukicoder 1810: Substring Avoidance (and CSES 1112)`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd#L612-L686)**:
   - **Defect**:
     - Lines 612 and 620–625 split the problem into `1. (Avoidance Form — yukicoder 1810)` and `2. (Containment Complement — CSES 1112)` and split the constraints into `Polynomial Inversion Regime` vs. `Large-N Rational Regime`.
   - **Required Fix**: Make `yukicoder 1810` ($N, m \le 2 \times 10^5$, output for each length $n = 1, \dots, N$ the number of length-$n$ strings over $\Sigma$ avoiding $P$ modulo $998244353$) the single primary problem statement, and mention the complement $\sigma^N - [x^N]F(x)$ (`CSES 1112`) and Bostan–Mori large-$N$ evaluation inside a brief remark at the end of the solution.

5. **[Ch 08 `Adv-2 (#139)` — `CF Gym 102978H: Harsh Comments`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd#L906-L1004)**:
   - **Defect**:
     - Lines 906–1004 explicitly split the problem into two completely unrelated problems:
       - `1. Part I (Multi-Pattern Goulden–Jackson Cluster Matrix — 2B#D2)` (lines 914–915, 957–978)
       - `2. Part II (Motzkin Trinomial Radical Substitution — 2A#16)` (lines 916–919, 981–1001)
     - Furthermore, Part II's problem statement (lines 917–919) is not even a well-defined problem (`"Given a sequence of weights w_{i,j}, evaluate a sum of the form S = \sum_{i=0}^n \sum_{j=0}^{n-i} \binom{n}{i, j, n-i-j} w_{i,j} where the weight w_{i,j} depends only on the linear combination k = i + 2j (or where each step takes a trinomial transition (1 + x + x^2)^n)"`).
   - **Required Fix**: Present **CF Gym 102978H — Harsh Comments** (the multi-pattern Goulden–Jackson / Aho–Corasick rational generating function problem) as the single unified problem statement with exact input/output specification and constraints, and if desired, include the trinomial/Motzkin coefficient identity $[x^k](1 + ax + bx^2)^n$ as an auxiliary lemma inside the solution or in the Chapter prose rather than splitting the problem into `Part I / Part II`.

6. **[Ch 08 `Mas-1 (#052)` — `AtCoder ARC 100 F / LOJ 3395: Colorful Sequences & ez_lcw Bounded-Run Sieve`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd#L1008-L1119)**:
   - **Defect**:
     - Lines 1016–1020 split the problem into `1. Part A (LOJ 3395 — The All-k Bounded-Run Sieve)` and `2. Part B (AtCoder ARC 100 F — Colorful Sequences)`.
     - Part A's statement (lines 1016–1017) is hedged and underspecified: `"Given N and a sequence weight v_1, \dots, v_N, or m colors, compute for every 1 \le k \le N simultaneously the total weight of sequences of length N in which no contiguous monochromatic run has length > k (where a maximal run of length L \le k carries weight w_L, or w_L = 1)."`
   - **Required Fix**: Present **AtCoder ARC 100 F — Colorful Sequences** ($N \le 25000, K \le 400, M \le 26$, given $A = (A_1, \dots, A_M)$, sum over all $K^N$ sequences of the number of contiguous subsegments containing $A$, where a colorful sequence is a permutation of $1 \dots K$) as the single unified problem statement, and present the all-$k$ bounded-run sieve (`LOJ 3395`, $O(N \log^2 N)$ via harmonic block summation) as a self-contained bonus subsection inside the collapsible solution.

7. **[CP-II `Problem CP-II.8 (#141)` — `Counting Labeled Trees with Prescribed Degrees`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L1128-L1142)**:
   - **Defect**:
     - Lines 1136–1141 split `CP-II.8` into `1. Part A (Luogu P2290 — Exact Labeled Tree Count)` and `2. Part B (Luogu P4430 — Ordered Construction Variant)` with hedged parentheticals (`"or equivalently, if the n - 2 internal choices in the construction are ordered up to (n-1)!"`, `"modulus P = 9999991 (or 998244353)"`).
   - **Required Fix**: State **Luogu P2290 — [HNOI2004] 树的计数** ($1 \le n \le 150$, $0 \le d_i \le n - 1$, exact 64-bit integer count of labeled trees on $\{1, \dots, n\}$ with vertex degrees $d_1, \dots, d_n$) as the single, exact Stage 1 problem statement, and discuss the modular $n \le 10^6$ regime (`P4430`) inside the collapsible solution (`Step 2B`).

---

## Check 2 Audit: Self-Contained Inline Statements, Constraints & Sample Traces ($N \le 4$)

### 2.1 Universal Omission of Visible Inline Sample Traces ($N \le 4$) Across All 40 Problem Statements

**Critical Finding**: **0 out of 40** problem statements across `Ch 05` (8), `Ch 06` (8), `Ch 07` (8), `Ch 08` (8), and `CP-II` (8) include a visible small sample trace ($N \le 4$) inside the problem statement!
- In `Ch 05`: Only 5 of 8 problems (`#104`, `#034`, `#040`, `#081`, `#073`) include a small trace inside the hidden `<details>` solution; `#187`, `#069`, and `#177` have **no sample trace anywhere**.
- In `Ch 06`: **0 of 8** problems have a sample trace anywhere (neither in the problem statement nor in the solution).
- In `Ch 07`: **0 of 8** problems have a sample trace anywhere (neither in the problem statement nor in the solution).
- In `Ch 08`: Only 1 of 8 problems (`#018`, line 601) has a small trace inside the hidden solution; the remaining **7 of 8** problems (`#241`, `#155`, `#089`, `#067`, `#139`, `#052`, `#137`) have **no sample trace anywhere**.
- In `CP-II`: All 8 problems have a concrete trace inside the hidden `<details>` solution (`#### 3. Hand-Checkable Concrete Trace`), but **0 of 8** have a visible sample input/output trace inside the Stage 1 problem statement.

### 2.2 Required Sample Traces to Add to Problem Statements

Every problem statement in `Ch 05`–`Ch 08` and `CP-II` should include a compact `- **Sample Trace ($N \le 4$)**:` bullet immediately after `- **Input Constraints**:` showing a tiny parameter instance and its exact output (without spoiling the algebraic method!). Specifically:

- **Ch 05**:
  - `SS-1 (#104)` (Line 744): Add sample $K = 2, N = 4$ with $(c_1, c_2) = (1, 1)$ and $(a_0, a_1) = (0, 1) \implies a_2 = 1, a_3 = 2, a_4 = 3$.
  - `SS-2 (#034)` (Line 853): Add sample $S = (1, 2, 4, 8, 16) \implies L = 1, C(x) = 1 - 2x$.
  - `Int-1 (#187)` (Line 974): Add sample $N = 2, K = 2 \implies 12$ valid arrays (`[0,0],[1,1],[2,2]` have $\max < 2$ if disallowed, or trace $M(2,2) - M(2,1) = 7 - 2 = 5$ where $M(2,2) = 7$ is the number of arrays in $\{1, 2, 3\}^2$ with no adjacent pair summing to $> 4$: all $9$ except $(2,3)$ and $(3,2)$).
  - `Int-2 (#069)` (Line 1102): Add sample $N = 4, K = 2 \implies 1^2 + 2^2 + 3^2 + 4^2 = 30$.
  - `Adv-1 (#040)` (Line 1217): Add sample $K = 3, N = 5 \implies A_1 = A_2 = A_3 = 1, A_4 = 3, A_5 = 5$.
  - `Adv-2 (#081)` (Line 1326): Add sample $N = 4 \implies f(2) = 1, f(3) = 2, f(4) = 5$, sum $= 8$.
  - `Mas-1 (#177)` (Line 1451): Add sample $m = 2, l = 1, r = 2, k = 1 \implies \frac{1}{2}(f_1 + f_2) = \frac{1}{2}(3 + 11) = 7$.
  - `Mas-2 (#073)` (Line 1581): Add sample $N = 4, (A, B) = (2, 3) \implies \text{Bad}(2, 3) = 0 \implies \text{Good}(2, 3) = 2! = 2$; $(A, B) = (1, 4) \implies \text{Bad}(1, 4) = 2 \cdot 1! \cdot 1! = 2 \implies \text{Good}(1, 4) = 0$.
- **Ch 06**:
  - `SS-1 (#005)` (Line 737): Add sample $N = 2, (A_1, B_1) = (1, 1), (A_2, B_2) = (1, 2) \implies i=1, j=2$ gives $\binom{4}{2} = 6$.
  - `SS-2 (#055)` (Line 795): Add sample $p(x) = 1 + 2x + 3x^2, c = 1 \implies p(x + 1) = 6 + 8x + 3x^2$.
  - `Int-1 (#193)` (Line 853): Add sample $N = 3 \implies \left\{\begin{smallmatrix} 3 \\ 0..3 \end{smallmatrix}\right\} = (0, 1, 3, 1)$ and $\left[\begin{smallmatrix} 3 \\ 0..3 \end{smallmatrix}\right] = (0, 2, 3, 1)$.
  - `Int-2 (#080)` (Line 922): Add sample $d = 2, A = (1, 1, 1) \implies S_0 = 1 - 1 + 1 = 1, S_1 = 1 + 0 - 1 = 0, S_2 = 1 + 2 + 1 = 4$.
  - `Adv-1 (#094)` (Line 1002): Add sample $N = 3, K = 2 \implies 3 \cdot 2^{3-2}\binom{3-1}{2-1} + \dots = 6$ (pairs $(1,2),(2,3)$ each appear in $3$ connected induced subgraphs: size 2 (`{1,2}` / `{2,3}`), size 3 (`{1,2,3}`), wait—trace exact count from formula).
  - `Adv-2 (#096)` (Line 1063): Add sample $n = 3, a = 2, b = 1 \implies \left[\begin{smallmatrix} 2 \\ 2 \end{smallmatrix}\right] \binom{2}{1} = 1 \cdot 2 = 2$ (`[1, 3, 2]` and `[2, 3, 1]`).
  - `Mas-1 (#098)` (Line 1126): Add sample $N = 3, K = 1 \implies \sum_{u=1}^3 \text{deg}(u)^1 = 2(3-1) \cdot 3^{3-2} = 12$ across the $3$ labeled trees on $3$ vertices.
  - `Mas-2 (#109)` (Line 1200): Add sample $n = 2, m = 1, a = (1, 2), x = 1 \implies \sum_{k=0}^2 (1 + 2k) \binom{2}{k} 1^k = 1 \cdot 1 + 3 \cdot 2 + 5 \cdot 1 = 12$.
- **Ch 07**:
  - `SS-1 (#224)` (Line 596): Add sample $n = 3, s = 1, a = (1, 1, 1, 1) \implies \sum_{k \equiv 1 \pmod 4} \binom{3}{k} 1^k = \binom{3}{1} = 3$.
  - `SS-2 (#248)` (Line 696): Add sample $A = (1, 2, 1), c = 2, M = 3 \implies A(1) = 4, A(2) = 9, A(4) = 25$.
  - `Int-1 (#178)` (Line 795): Add sample $n = 1, k = 1, p = 998244353 \implies \binom{4}{0} + \binom{4}{4} = 2$.
  - `Int-2 (#143)` (Line 903): Add sample $n = 4, k = 1 \implies 4\left(\binom{4}{0} + \binom{4}{4}\right) + \binom{4}{1} + \binom{4}{3} = 8 + 8 = 16$.
  - `Adv-1 (#147)` (Line 1007): Add sample $n = 2, p = 3, c = (1, 1, 1), A = (1, 0, 0) \implies (1 + x + x^2)^2 \bmod (x^3 - 1) = 3 + 3x + 3x^2$.
  - `Adv-2 (#012)` (Line 1110): Add sample $n = 1 \implies \Phi_1(x) = x - 1$; $n = 6 \implies \Phi_1(x) = x-1, \Phi_2(x) = x+1, \Phi_3(x) = x^2+x+1, \Phi_6(x) = x^2-x+1$.
  - `Mas-1 (#092)` (Line 1218): Add sample $p = 3, A = (1, 2, 3) \implies B(0) = 6 \equiv 0, B(1) = 1 + 2 + 3 = 6 \equiv 0, B(2) = 1 + 4 + 3 = 8 \equiv 2 \pmod 3$.
  - `Mas-2 (#168)` (Line 1327): Add sample $m = 3, k = 1, L = 4 \implies c_1 = 2, c_2 = 3, c_3 = 1, c_4 = 0$.
- **Ch 08**:
  - `SS-1 (#018)` (Line 548): Move or summarize the $N = 3$ sample trace ($!3 = 2$: `(2,3,1)` and `(3,1,2)`) into the problem statement.
  - `SS-2 (#241)` (Line 628): Add sample $\sigma = 2, P = \texttt{00}, N = 3 \implies$ counts for $n = 1, 2, 3$ are $2, 3, 5$.
  - `Int-1 (#155)` (Line 701): Add sample $N = 2, M = 1, K = 1, S = 2 \implies 4$ grids (`[[2,0]], [[0,2]]` have row sum 2, col max 2; valid grids where row/col max is 1: `[[1,1]]` has sum 2 and max 1 $\implies 1$).
  - `Int-2 (#089)` (Line 772): Add sample $N = 3, K = 1 \implies 4$ permutations (`(1,2,3)` has 0 positions with $|P_i - i| = 1$, wait: trace exact count for $N=3, K=1$: `(1,2,3)` has $3$ with $|P_i - i| \neq 1$; `(2,3,1)` and `(3,1,2)` have $1$ position each ($|3-1|=2$ vs $|2-1|=1$)).
  - `Adv-1 (#067)` (Line 846): Add sample $N = 4, K = 1 \implies$ count of size-2 matchings with no adjacent vertices on a 4-vertex path ($1$ matching: `{(1,3), (2,4)}`).
  - `Adv-2 (#139)` (Line 923): Add sample $\sigma = 2, \mathcal{P} = \{\texttt{01}, \texttt{10}\}, N = 3 \implies 2$ valid strings (`000` and `111`).
  - `Mas-1 (#052)` (Line 1024): Add sample $N = 3, K = 2, A = (1, 1) \implies$ among $2^3 = 8$ sequences, `111` has 2 subsegments `(1,1)` andContains `(1,2)` or `(2,1)` in `112` and `211` $\implies$ total $2$ occurrences of $A$ inside sequences containing a colorful subsegment.
  - `Mas-2 (#137)` (Line 1134): Add sample $N = 2, k_1 = 2, k_2 = 1 \implies 2$ valid color-avoiding circular arrangements.
- **CP-II**:
  - Add a visible `- **Sample Trace**:` bullet to each Stage 1 problem statement (`CP-II.1` to `CP-II.8`) stating only the input parameters and the final integer answer (leaving the step-by-step trace inside the collapsible solution so Stage 1 stays 100% spoiler-free).

---

## Check 3 Audit: 3 Progressive Hints, Full Derivations, Mathematical Accuracy & Prerequisite Closure

### 3.1 Mathematical Error in `Ch 05 Mas-2 (#073)` Hint 3 (`chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd`, Line 1622)

- **Location**: [ch05-rational-bostan-mori-berlekamp-massey.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1622)
- **Defect**: Line 1622 states:
  $$
  \text{Bad}(A, B) = (A - 1)! (N - B)! (B - A - 1) \binom{N - 2 - (B - A)}{A - 1}.
  $$
  This formula is **mathematically wrong** and directly contradicts the true formula derived 46 lines later in the Solution (line 1668):
  $$
  \text{Bad}(A, B) = (B - A - 1)(N - A - 2)!(B - 3)!.
  $$
  **Verification**: Set $N = 6, A = 2, B = 4$.
  - True formula (line 1668): $(4 - 2 - 1)(6 - 2 - 2)!(4 - 3)! = 1 \cdot 2! \cdot 1! = 2$.
  - Hint 3 formula (line 1622): $1! \cdot 2! \cdot 1 \cdot \binom{6 - 2 - 2}{1} = 2 \cdot \binom{2}{1} = 4 \neq 2$!
  Why did Hint 3 get it wrong? Because $(B - 3)! = (A - 1)!(B - A - 2)!\binom{B - 3}{A - 1}$, not $(N - B)!\binom{N - 2 - (B - A)}{A - 1}$!
- **Replacement Text for Line 1622**:
  ```markdown
  \text{Bad}(A, B) = (B - A - 1)(N - A - 2)!(B - 3)! = (A - 1)!(B - A - 2)!(N - A - 2)!(B - A - 1)\binom{B - 3}{A - 1} \qquad (\text{for } B - A \ge 2, \text{ and } 0 \text{ for } B = A + 1).
  ```

### 3.2 Unedited Stream-of-Consciousness Draft Notes (`"wait..."`, `"Hold on!"`, `"WAIT: no C(d,k)!"`)

The following 6 locations contain raw, unedited author scratchpad monologues (`"wait..."`, `"Hold on!"`) that must be cleaned up into polished textbook prose:

1. **[ch05-rational-bostan-mori-berlekamp-massey.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1553-L1556) (`Mas-1 #177` Solution)**:
   - Line 1556: `*(Check: n = 0 => A + B = 1; n = 1 => A\alpha + B\beta = 3 if f_1 = 3, or for f_1 = 2, f_2 = 7, A = 1/2, B = 1/2—adjust the linear system A + B = f_0, A\alpha + B\beta = f_1 to the exact boundary convention of the statement!)*`
   - **Fix**: Standardize on $f_0 = 1, f_1 = 3, f_2 = 11$ in line 1441 and replace line 1556 with: `*(Check: at $n = 0$, $A + B = 1 = f_0$; at $n = 1$, $A\alpha + B\beta = 2 + 1 = 3 = f_1$.)*`

2. **[ch05-rational-bostan-mori-berlekamp-massey.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1606) & [Lines 1655–1656](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1655-L1656) (`Mas-2 #073` Hint 2 & Solution)**:
   - Line 1606: `(2 \le k \le N - A, since for B = A + 1 the pair (P_1, P_N) after deleting interior elements would force a jump, wait: for B = A + 1, every permutation is good because there is no value strictly between A and A + 1—check the base cases carefully!)`
   - Lines 1655–1656: `3. **Wait—let us check the product**:` / `Wait: in the skeleton of m copies of M and l copies of L, how many such skeletons exist?`
   - **Fix**: Remove `"wait:"` in line 1606 (simply state: `(for B = A + 1, every permutation is good because there is no integer strictly between A and A + 1)`), and replace lines 1655–1656 with: `3. **Counting Valid $(L, M)$ Skeletons and Labelings**: In a skeleton consisting of $m$ copies of $M$ and $l$ copies of $L$ (with $m + l = k \ge 2$):`

3. **[ch06-binomial-snake-oil-taylor-shift-stirling.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L934-L938) (`Int-2 #080` Hint 2)**:
   - Lines 935–937:
     ```markdown
     &= \sum_{i=0}^d A_i [x^i] \big((1 + x) + y(1 - x)\big)^d \quad \text{WAIT: no }\binom{d}{k}\text{!}
     $$
     Hold on! There is no $\binom{d}{k}$ in $\sum_k S_{k+1} y^k$, so we cannot just sum $(1+x)^k (1-x)^{d-k} y^k$ with $\binom{d}{k}$. Instead, look at the exponent $k$ vs $d - k$:
     ```
   - **Fix**: Delete the false equation and `"WAIT: no \binom{d}{k}! Hold on!"` and go directly to the clean factorization $(1 + x)^k (1 - x)^{d - k} = (1 - x)^d \left(\frac{1 + x}{1 - x}\right)^k$:
     ```markdown
     Because the summand $(1 + x)^k (1 - x)^{d - k}$ lacks a $\binom{d}{k}$ factor, we factor out $(1 - x)^d$ to isolate $k$ in a single ratio:
     $$
     S_k = [x^d] \sum_{i=0}^d A_i x^{d - i} (1 + x)^k (1 - x)^{d - k} = [x^d] R(x) (1 + x)^k (1 - x)^{d - k},
     $$
     where $R(x) = \sum_{i=0}^d A_{d - i} x^i$ is the reversed polynomial.
     ```

4. **[cp02-part2-rational-transforms-ie.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L152) (`CP-II.1` Hint 3)**:
   - Line 152: `*(Note: Because n - 1 < P, this direct falling-factorial formula is valid modulo P even when m + n - 1 crosses multiples of P, wait—is that always true, or should you check Lucas's Theorem? Be careful! Actually, over \mathbb{Z}, \binom{M}{k} = ...)*`
   - **Fix**: Replace with direct, authoritative prose:
     ```markdown
     *(Note: Over $\mathbb{Z}$, $\binom{M}{k} = \frac{M(M-1)\cdots(M-k+1)}{k!}$ is an exact integer identity. Because $k = n - 1 < P$, $\gcd(k!, P) = 1$, so reducing each factor $(M - j) \bmod P$ in the numerator and multiplying by $((n-1)!)^{-1} \bmod P$ in the localization $\mathbb{Z}_{(P)}$ is 100% exact for all $M \ge 0$, even when $M \ge P$.)*
     ```

5. **[cp02-part2-rational-transforms-ie.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L516-L518) (`CP-II.3` Solution Trace)**:
   - Lines 516–518: `1. ((() -> beauty 1 (())` / `2. ((() wait: positions 1 and 3 are ?, position 2 is (, position 4 is ).`
   - **Fix**: Remove the false start `1.` and `2. ((() wait:` and directly list the 4 completions of `?(?)`: `((()`, `(())`, `)(()`, `)(())`.

6. **[cp02-part2-rational-transforms-ie.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L949-L950) (`CP-II.6` Solution Trace)**:
   - Lines 949–950: `- Valid strings (7 total): RGBR, RGRB, RRGB, BRGR, RBRG, BRRG... wait let's list all 7: Contract RG -> X, leaving tokens {X, R, B} (3! = 6 ways: XRB, XBR, RXB, BX R, RBX, BRX). Wait: does RXB (RRGB) have 1 RG? Yes! ... So there are 6 valid strings`
   - **Fix**: Replace with: `- Valid strings (6 total): Contracting the unique occurrence of RG into X leaves the 3 distinct tokens {X, R, B}, yielding 3! = 6 valid strings: RGBR (XRB), RGRB (XBR), RRGB (RXB), BRGR (BXR), RBRG (RBX), and BRRG (BRX).`

### 3.3 Forward-Reference Violations (Check 3 / Dimension 3)

1. **`Ch 05 Mas-1 (#177)` ([Lines 1469, 1510–1522](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1469))**:
   - Uses signed Stirling numbers of the first kind $(-1)^{k-j}\left[\begin{smallmatrix} k \\ j \end{smallmatrix}\right]$ before Stirling numbers are introduced in **Chapter 06 (`§6.4`)**.
   - **Fix**: Define the polynomial coefficients $c_0, c_1, \dots, c_k$ of the falling factorial polynomial $x(x - 1)\cdots(x - k + 1) = \sum_{j=0}^k c_j x^j$ self-containedly by expanding the product of $k$ linear factors iteratively in $O(k^2)$ time, and add a parenthetical note `(which we will recognize in Chapter 06 as signed Stirling numbers of the first kind)`.
2. **`Ch 05 Int-2 (#069)` ([Line 1174](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1174))**:
   - References Eulerian polynomials $A_K(x)$ (`§6.4`) inside the `Ch 05` solution.
   - **Fix**: Derive the degree $\le K + 1$ of the numerator polynomial $P_K(x) = (1 - x)^{K+1} \sum_{n \ge 0} n^K x^n$ purely from the recurrence / finite-difference annihilation $(1 - x)^{K+1}$ taught in `Ch 05`, without invoking `§6.4` Eulerian numbers.
3. **`Ch 06 Int-2 (#080)` ([Lines 913, 980](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L913))**:
   - Cites `Subproduct Tree` (taught in **Chapter 13**) as a prerequisite.
   - **Fix**: Remove the Subproduct Tree reference as detailed in §1.2 Item 3 above.
4. **Broken Section References in `CP-II` ([Lines 7, 13–14, 580, 1154, 1188, 1263, 1267](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L7-L15))**:
   - Line 7 calls Chapter 07 `*Chapter 07 (Change of Variables, Substitutions & Point-Value Transforms)*` and Line 14 puts `Coordinate Shifts (Taylor Shift)` and `Number-Theoretic / Dirichlet / Multiplicative Sieves` in Chapter 07, while lines 580 and 1263 cite `Chapter 07 (§7.4 Multiplicative Linear Sieve for i^k)`. In the actual textbook, Taylor Shift is in **Chapter 06 (`§6.3`)**, and Chapter 07 is *Roots of Unity Filter, Cyclotomic Symmetry & Bluestein's Chirp-$Z$ Transform* (`§7.1`–`§7.3`, with no `§7.4`).
   - Lines 1154, 1188, and 1267 cite `Chapter 04 (§4.5 Labeled Trees, Prüfer Sequences & Degree-Distribution EGFs)`. In Chapter 04, Prüfer sequences and labeled trees are in **`§4.4`**, not `§4.5`.

---

## Check 4 Audit: 100% Spoiler-Free Stage 1 in `CP-II` (`checkpoints/cp02-part2-rational-transforms-ie.qmd`)

### 4.1 Critical Spoiler Leak #1: Visible Pre-Stage-1 Section `## The 3-Axis Part II Diagnostic Rubric (No Spoilers)` (Lines 29–89)

Despite the heading `(No Spoilers)` on line 29, lines 37–89 explicitly leak the **exact parameters, exact generating function formulas, exact algebraic identities, and exact home chapters** for all 8 problems in `CP-II` right at the top of the page before `## Stage 1: Spoiler-Free Blind Problem Set`:

| Lines | Leaked Content in Visible Pre-Stage-1 Text | Spoiled Problem |
| :--- | :--- | :--- |
| **37–39, 66, 83** | Mentions `$n \le 20$, target sum $S \le 10^{14}$`, `"At most $f_i$ items from box $i$": Bounded geometric series $\frac{1 - x^{f_i+1}}{1 - x}$`, and `[x^{S-d}](1-x)^{-n} = \binom{S-d+n-1}{n-1}` (`Ch 06 / Ch 08`). | **Spoils `CP-II.1 (#085)`** |
| **56, 79** | Mentions `\binom{j}{k}(-1)^{j-k}k^i \| Factor \binom{j}{k} = \frac{j!}{k!(j-k)!} and apply 1D NTT Cauchy Convolution (Ch 06 / Ch 07)` and `Stirling / Binomial Sum, N <= 10^5 -> Expand falling/Stirling basis, swap sums, decouple via 1D NTT (Ch 06)`. | **Spoils `CP-II.2 (#152)`** |
| **42, 57, 69, 80** | Mentions `"Maximum nested depth of a bracket subsequence": By split-point duality, equals \max_{0 \le i \le n} \min('(' in s[1..i], ')' in s[i+1..n]), occurring at the unique split point i where prefix '(' count equals suffix ')' count` and `\sum_k \binom{x}{k-L}\binom{y}{k-R} -> Absorb linear factor k = L + (k-L), collapse via Vandermonde Convolution (Ch 06)`. | **Spoils `CP-II.3 (#251)`** |
| **46–48, 78** | Mentions `Huge Evaluation Point (N <= 10^9) + Moderate Degree (K <= 10^6) ... evaluate F(N) in O(K) time via consecutive-node Lagrange interpolation (Ch 06)`. | **Spoils `CP-II.4 (#252)`** |
| **45, 58, 81** | Mentions `if the coupling is multiplicative in an exponent c^{I \cdot J} \pmod P, reduce exponents modulo P-1 via Fermat's Little Theorem and convert I \cdot J into (I+J) via Bluestein's identity IJ = \binom{I+J}{2} - \binom{I}{2} - \binom{J}{2} (Ch 07)`. | **Spoils `CP-II.5 (#100)`** |
| **59, 67, 84, 87** | Mentions `"Exactly K occurrences / wins / matches" -> Binomial Inversion (Ch 08)` and `Disjoint tokens (e.g. 'RG') -> Contract j tokens directly: Closed-form g_j + Binomial Inversion (Ch 08)`. | **Spoils `CP-II.6 (#029)`** |
| **42, 67, 84, 88** | Mentions `prefix count \times selected pairs on a sorted Ferrers board` and `Bipartite dominance A_i > B_pi(i) -> Sort A and B (Ferrers Board): O(N^2) Rook DP for r_j + Binomial Inversion (Ch 08)`. | **Spoils `CP-II.7 (#162)`** |
| **60, 68, 85** | Mentions `"Number of labeled trees with prescribed degrees d_1, ..., d_n": Biject via Prüfer sequences to words of length n-2 ... Multinomial EGF (n-2)! / prod (d_i-1)! (Ch 04 / Ch 06)`. | **Spoils `CP-II.8 (#141)`** |

- **Required Fix for Lines 29–89**:
  1. Either wrap the entire detailed `3-Axis Part II Diagnostic Rubric` and Mermaid flowchart (lines 33–89) inside a collapsible `<details><summary>Optional Pre-Flight Reference: The 3-Axis Part II Diagnostic Rubric (Open Only After Stage 1 Cold Read or Moves to Stage 2)</summary>...</details>` block (or move it into `## Stage 2` at line 1251), **AND**
  2. Strip the problem-specific literals (`'RG'`, `A_i > B_pi(i)`, `f_i <= 10^{12}, S <= 10^{14}`, `"Maximum nested depth of a bracket subsequence"`) from the general rubric so it teaches general diagnostic axes without quoting the 8 checkpoint problems verbatim.

---

### 4.2 Critical Spoiler Leak #2: Line-by-Line Spoiler Leaks Inside Stage 1 Problem Statements & `Hint 1` Blocks

Below is every spoiler leak inside `## Stage 1: Spoiler-Free Blind Problem Set` (lines 93–1248), together with the exact line numbers and drop-in spoiler-free replacement text:

1. **`CP-II.1 (#085)` — `Hint 1` Body ([Line 119](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L119))**:
   - **Leak**: `Instead, the 2^n scale tells you that the finite upper bounds x_i <= f_i must be handled by a **sparse 2^n-term expansion**, while the unbounded sum \sum x_i = s must be evaluated in O(n) closed form.` (Directly leaks the sparse polynomial expansion + closed-form unbounded series).
   - **Spoiler-Free Replacement for Line 119**:
     ```markdown
     Look at the extreme asymmetry in the constraints: the number of boxes is tiny ($n \le 20$, so $2^n \approx 10^6$), whereas the individual capacities $f_i \le 10^{12}$ and the target sum $s \le 10^{14}$ are astronomical. Because $s$ can exceed the modulus $P = 10^9 + 7$ by five orders of magnitude, any algorithm that iterates up to $s$ is impossible. Instead, ask yourself: how easy would this problem be if there were *no* upper capacity bounds $x_i \le f_i$, and how can you use the $2^n$ subsets of boxes to account for selections that violate one or more capacity bounds?
     ```

2. **`CP-II.2 (#152)` — Problem Statement Constraints ([Line 246](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L246)) & `Hint 1` Body ([Line 252](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L252))**:
   - **Leak**: Line 246 labels the modulus `(NTT-friendly prime)` in the visible problem statement, and Line 252 says `and the modulus is the canonical NTT prime 998244353`.
   - **Spoiler-Free Replacement for Line 246**:
     ```markdown
     - Modulus: $P = 998244353$ (prime)
     ```
   - **Spoiler-Free Replacement for Line 252**:
     ```markdown
     The upper limit is $n = 10^5$, so computing the full triangle of numbers $\left\{\begin{smallmatrix} i \\ j \end{smallmatrix}\right\}$ for $0 \le j \le i \le n$ via the $O(n^2)$ recurrence will TLE and MLE. Notice that the weight $2^j j!$ depends **only on the column index $j$**, not on the row index $i$. What happens if you swap the order of summation so $j$ is on the outside and $i$ is on the inside, and how can you express the number of surjections $j! \left\{\begin{smallmatrix} i \\ j \end{smallmatrix}\right\}$ as a sum of $i$-th powers?
     ```

3. **`CP-II.3 (#251)` — Visible Source Note ([Line 393](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L393)), Target Complexity ([Line 408](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L408)), and `Hint 1` Body ([Line 413](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L413))**:
   - **Leak**: Line 413 explicitly reveals the `**unique canonical split point**` and prefix `(` vs. suffix `)` comparison in `Hint 1`.
   - **Spoiler-Free Replacement for Line 413**:
     ```markdown
     At first glance, finding the maximum depth of a simple subsequence $\texttt{(}^d \texttt{)}^d$ looks like an interval dynamic programming problem, which cannot be run across $2^q$ completions simultaneously. To sum $b(T)$ over all $2^q$ completions using linearity of expectation/summation, we need a simpler characterization of $b(T)$ for a single fixed bracket string $T$. Since every simple subsequence $\texttt{(}^d \texttt{)}^d$ consists of $d$ opening brackets followed by $d$ closing brackets, how is $b(T)$ related to partitioning $T$ into a prefix $T[1..i]$ and a suffix $T[i+1..n]$?
     ```

4. **`CP-II.4 (#252)` — Visible Target Complexity ([Line 568](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L568)) & `Hint 1` Body ([Line 573](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L573))**:
   - **Leak**:
     - Line 568 (visible in Stage 1!) says: `- **Target Complexity**: $O(k)$ time (using a linear sieve for $i^k$, or $O(k \log k)$ with binary exponentiation) and $O(k)$ space.`
     - Line 573 (`Hint 1`) names `NTT prime`, `Bernoulli numbers`, `polynomial inversion \frac{x}{e^x - 1}`, `Faulhaber's formula`, and `how many sample values S_k(0), S_k(1), ..., S_k(d) uniquely determine it?`!
   - **Spoiler-Free Replacement for Line 568**:
     ```markdown
     - **Target Complexity**: $O(k)$ or $O(k \log k)$ time, $O(k)$ space.
     ```
   - **Spoiler-Free Replacement for Line 573**:
     ```markdown
     Look at the two parameters: $n$ is up to $10^9$ (ruling out direct $O(n)$ iteration), while the exponent $k$ is up to $10^6$, and the modulus is $10^9 + 7$. For small fixed values of $k$ such as $k = 1, 2, 3$, you know the closed-form formulas $S_1(n) = \frac{n(n+1)}{2}$, $S_2(n) = \frac{n(n+1)(2n+1)}{6}$, and $S_3(n) = \left(\frac{n(n+1)}{2}\right)^2$. What kind of function of $n$ is $S_k(n)$ for a general fixed integer $k \ge 0$, and what is its degree in $n$?
     ```

5. **`CP-II.6 (#029)` — `Hint 1` Body ([Line 861](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L861))**:
   - **Leak**: `What happens if we instead designate j >= K occurrences of RG and fuse each designated RG into a single atomic super-character X?` (Spoils the exact Binomial Inversion + token contraction reduction in `Hint 1`).
   - **Spoiler-Free Replacement for Line 861**:
     ```markdown
     The problem asks for strings with **exactly $K$** occurrences of the contiguous two-character substring `RG`, with $R, G, B \le 10^6$. Counting "exactly $K$" directly is awkward because once we place $K$ copies of `RG`, we must prevent the remaining $R - K$ copies of `R` and $G - K$ copies of `G` from accidentally forming additional `RG` pairs. Instead of enforcing the "no additional `RG`" constraint directly, is it easier to count arrangements where a chosen subset of $j \ge K$ occurrences of `RG` are guaranteed to appear, and what structural property of the two-letter string `RG` makes choosing $j$ simultaneous occurrences particularly simple?
     ```

6. **`CP-II.7 (#162)` — `Hint 1` Body ([Line 1004](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L1004))**:
   - **Leak**: `What happens if we **sort A and B** and only enforce the condition A_i > B_{\pi(i)} on j chosen rows, leaving the other n - j rows completely unconstrained?` (Explicitly spoils both the Ferrers-board sorting step and the Binomial Inversion relaxation in `Hint 1`).
   - **Spoiler-Free Replacement for Line 1004**:
     ```markdown
     First, simplify the win-loss margin condition: since all $2n$ numbers are pairwise distinct, every index $i$ satisfies either $A_i > B_{\pi(i)}$ or $A_i < B_{\pi(i)}$. If $m$ indices satisfy $A_i > B_{\pi(i)}$, then the remaining $n - m$ indices automatically satisfy $A_i < B_{\pi(i)}$, so $m - (n - m) = k \iff 2m = n + k$. Thus we need **exactly $m = \frac{n + k}{2}$** indices with $A_i > B_{\pi(i)}$. Why is it difficult for an $O(n^2)$ dynamic program to track both $A_i > B_{\pi(i)}$ and $A_i < B_{\pi(i)}$ simultaneously, and what happens if we reorder $A$ and $B$ so that the sets of valid partners $\{r : B_r < A_i\}$ become nested?
     ```

7. **`CP-II.8 (#141)` — `Hint 1` Body ([Line 1147](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L1147))**:
   - **Leak**: `Whenever a problem specifies **labeled trees on n vertices** together with **vertex degrees d_1, ..., d_n**, there is one canonical bijection from **Part I (Chapter 04)** that turns the graph-theoretic tree structure into a flat sequence of length n - 2 with fixed character multiplicities.` (Directly leaks `Part I (Chapter 04)` and the exact length-$n-2$ Prüfer sequence description in `Hint 1`, whereas target chapter routing belongs exclusively in `Hint 2`).
   - **Spoiler-Free Replacement for Line 1147**:
     ```markdown
     Counting trees directly by adding edges one by one while maintaining acyclicity and tracking all $n$ vertex degrees is combinatorially messy. Instead, ask yourself: is there a classical $1$-to-$1$ correspondence between labeled trees on $n$ vertices and a much simpler family of words/sequences over the alphabet $\{1, 2, \dots, n\}$, and how is the degree $d_i$ of each vertex $i$ reflected in that sequence? (Also pay close attention to the small constraints $n \le 150$ with exact 64-bit integer output and the boundary case $n = 1$!)
     ```

### 4.3 Verification of Callout Boxes Inside `CP-II`

We verified all 8 `::: {.callout-warning}` boxes (`### Failure Mode & Remedy:...` at lines 211, 369, 533, 657, 812, 961, 1103, 1228): all 8 are properly nested **inside** the collapsible `<details><summary>Complete Derivation, Algorithm Contract & Complexity Analysis</summary>...</details>` blocks (which close at lines 228, 387, 549, 676, 834, 975, 1124, 1247), so they are hidden during Stage 1.
