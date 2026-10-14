# Phase 3 Iteration 4 Audit Report: Single-Step Algebraic Derivations, Verbal Annotations & Loop Invariant Precision (`Ch 01`–`Ch 24`)

- **Auditor**: `fps-textbook-critic` (Phase 3 Iteration 4 Specialist — Single-Step Algebraic Derivations & Verbal Annotations)
- **Date**: 2026-10-15
- **Scope**: All 24 core textbook chapters (`chapters/ch01-*.qmd` through `chapters/ch24-*.qmd`) and their 192 Practice Ladder solutions.
- **Reference Standards**: `AGENTS.md` (Zero Multi-Step Leaps, Verbalized Summands, Zero Unexplained Shorthands, Index Boundary & Loop Invariant Precision), `fps_research/PLAN.md` (Phase 3 Iteration 4).

---

## Executive Summary

Across the 24 chapters (`Ch 01`–`Ch 24`), the textbook demonstrates high overall rigor: every major theorem and Practice Ladder solution includes a `Diagnostic Signal & Reverse-Engineering Scratchpad` callout and an `Algorithm Contract` block. However, a ruthless line-by-line audit against the four Iteration 4 criteria uncovered **37 specific, actionable defects** across the 24 chapters:

1. **Multi-Step Algebraic Leaps (`26 instances`)**: Equations where 2–4 non-trivial algebraic steps (e.g., index substitution + binomial simplification, isolating boundary terms $d=0, n$ + dividing by $n$, extracting $[x^m]$ from an ODE + rearranging into a recurrence, or applying kernel identities + reversal symmetries) are compressed into a single `=` or `\implies` sign without showing intermediate equalities.
2. **Mathematical / Sign / Exponent Inaccuracies Caught via Single-Step Expansion (`2 critical instances`)**:
   - **`Ch 06` Line `1122` (`#094` CF 923E — Perpetual Subtraction)**: The parenthetical verification of the eigenbasis diagonalization writes $\sum_{j=i}^k \frac{1}{j + 1} (-1)^{j - i} \binom{j}{i} \binom{k}{j} = \dots = \frac{1}{k + 1} \delta_{i, k}$, which is mathematically false (that sum evaluates to $\frac{(-1)^{k-i}}{k+1}$, not $\frac{1}{k+1}\delta_{i,k}$). The actual matrix entry check is $(P \Lambda P^{-1})_{i,k} = \sum_{j=i}^k \binom{j}{i} \frac{1}{j+1} (-1)^{k-j} \binom{k}{j} = \frac{1}{k+1} = M_{i,k}$.
   - **`Ch 21` Line `316` (Theorem 21.1(2) — Kinoshita-Li Single-$n$ $w$-Plane Form)**: The first expression on the right-hand side writes $\left(\frac{w}{g(w)}\right)^{n+1} \frac{(1 + g(w))^{\alpha n + \gamma + 1}}{1 + (\beta + 1)g(w)}$, which double-counts a factor of $(1 + g(w))^\beta$ because $(1 + g(w))^{-(\beta - 1)}$ from $g'(w)$ was already absorbed into $(1 + g(w))^{\alpha n + \gamma + 1}$; the true intermediate factor before substituting $\frac{w}{g(w)} = (1 + g(w))^\beta$ is $\left(\frac{w}{g(w)}\right)^n \frac{(1 + g(w))^{\alpha n + \gamma + 1}}{1 + (\beta + 1)g(w)}$, which then equals the second expression $\frac{(1 + g(w))^{(\alpha + \beta)n + \gamma + 1}}{1 + (\beta + 1)g(w)}$.
3. **Unexplained Shorthands & Raw Draft Self-Corrections (`7 instances`)**: Unexpanded `"By LIF"` shorthands (`Ch 12` L239, `Ch 15` L449), `"Obviously"` (`Ch 15` L695), `"trivially"` (`Ch 11` L506, `Ch 16` L642), a malformed draft equation with `...` (`Ch 17` L474), and raw `"Wait:"` / live scratch-note self-talk (`Ch 02` L1206, `Ch 03` L1277, `Ch 07` L328, `Ch 20` L359–360).
4. **Index Boundary & Loop Invariant Precision (`2 instances`)**: Missing explicit subsegment index boundaries $[L, M] \sqcup [M+1, R]$ in `prod_tree` (`Ch 01` L484–490) and missing in-place descending loop bounds in `#091` CF 891E (`Ch 02` L1309–1318).

### Summary Table by Chapter

| Chapter | Multi-Step Leaps | Shorthands / Raw Draft Talk | Boundary / Invariant Gaps | Math / Sign Fixes | Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Ch 01** (`ch01-ring-convolutions-newton-inv.qmd`) | 1 (L594) | 0 | 1 (L484–490) | 0 | Needs 2 edits |
| **Ch 02** (`ch02-calculus-frobenius-sparse-ode-newton.qmd`) | 1 (L506–510) | 1 (L1206) | 1 (L1309–1318) | 0 | Needs 3 edits |
| **Ch 03** (`ch03-mset-partitions-euler-polya.qmd`) | 1 (L971–978) | 1 (L1277) | 0 | 0 | Needs 2 edits |
| **Ch 04** (`ch04-egf-set-cyc-boxed-prufer.qmd`) | 2 (L379, L1068) | 0 | 0 | 0 | Needs 2 edits |
| **Ch 05** (`ch05-rational-bostan-mori-berlekamp-massey.qmd`) | 3 (L1357, L1794, L1803) | 0 | 0 | 0 | Needs 3 edits |
| **Ch 06** (`ch06-binomial-snake-oil-taylor-shift-stirling.qmd`) | 1 (L708–709) | 0 | 0 | 1 (L1122) | Needs 2 edits |
| **Ch 07** (`ch07-roots-of-unity-cyclotomic-czt.qmd`) | 1 (L1457) | 1 (L328) | 0 | 0 | Needs 2 edits |
| **Ch 08** (`ch08-connected-component-ie-rook-goulden-jackson.qmd`) | 2 (L75, L1073) | 0 | 0 | 0 | Needs 2 edits |
| **Ch 09** (`ch09-cdq-fft-online-relaxed-convolution.qmd`) | 1 (L1284) | 0 | 0 | 0 | Needs 1 edit |
| **Ch 10** (`ch10-implicit-equations-newton-unlabeled-trees-otter.qmd`) | 2 (L408, L1147–1149) | 0 | 0 | 0 | Needs 2 edits |
| **Ch 11** (`ch11-laurent-residues-raney-lagrange-inversion.qmd`) | 2 (L326, L1583) | 1 (L506) | 0 | 0 | Needs 3 edits |
| **Ch 12** (`ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`) | 3 (L213, L228–230, L509) | 1 (L239) | 0 | 0 | Needs 4 edits |
| **Ch 13** (`ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd`) | 1 (L663) | 0 | 0 | 0 | Needs 1 edit |
| **Ch 14** (`ch14-pgf-stopping-times-renewal-poisson-martingales.qmd`) | 2 (L296, L676) | 0 | 0 | 0 | Needs 2 edits |
| **Ch 15** (`ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`) | 1 (L341) | 2 (L449, L695) | 0 | 0 | Needs 3 edits |
| **Ch 16** (`ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`) | 2 (L633, L1192) | 1 (L642) | 0 | 0 | Needs 3 edits |
| **Ch 17** (`ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`) | 1 (L474) | 0 | 0 | 0 | Needs 1 edit |
| **Ch 18** (`ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd`) | 2 (L269–273, L1341) | 0 | 0 | 0 | Needs 2 edits |
| **Ch 19** (`ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd`) | 1 (L169) | 0 | 0 | 0 | Needs 1 edit |
| **Ch 20** (`ch20-tellegen-transposition-multipoint-sampling-shift.qmd`) | 0 | 1 (L359–360) | 0 | 0 | Needs 1 edit |
| **Ch 21** (`ch21-kinoshita-li-composition-power-projection-revert.qmd`) | 0 | 0 | 0 | 1 (L316) | Needs 1 edit |
| **Ch 22** (`ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd`) | 1 (L527) | 0 | 0 | 0 | Needs 1 edit |
| **Ch 23** (`ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd`) | 3 (L629, L925, L1109) | 0 | 0 | 0 | Needs 3 edits |
| **Ch 24** (`ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd`) | 2 (L484–495, L1365) | 0 | 0 | 0 | Needs 2 edits |

---

## Detailed Chapter-by-Chapter Findings & Drop-In Replacements

---

### Chapter 01 (`chapters/ch01-ring-convolutions-newton-inv.qmd`)

#### 1.1 `[Boundary / Invariant Precision]` Lines `484–490` — `prod_tree(P, N)` Algorithm Contract
- **File**: [ch01-ring-convolutions-newton-inv.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L484-L490)
- **Issue**: The Algorithm Contract for `prod_tree(P, N)` states the heap invariant but omits the explicit recursive segment index boundaries $1 \le L \le R \le k$, midpoint split $M = \lfloor(L + R)/2\rfloor$, and disjoint interval partition $[L, R] = [L, M] \sqcup [M + 1, R]$ for the divide-and-conquer variant.
- **Drop-In Replacement (Line `488`)**:
  ```markdown
  - **Loop / Algebraic Invariant**: In the recursive segment tree over indices $1 \le L \le R \le k$ with midpoint $M = \lfloor (L + R)/2 \rfloor$, each call on $[L, R]$ partitions the index interval into disjoint halves $[L, M] \sqcup [M + 1, R]$ so every factor $P_i(x)$ ($1 \le i \le k$) is multiplied into the product exactly once; in the min-heap formulation, after $t$ merges ($0 \le t < k-1$), the priority queue contains $k - t$ polynomials whose product equals $\prod_{i=1}^k P_i(x)$, and each merge pops the two smallest-degree polynomials $A, B$ and pushes $(A \cdot B) \bmod x^{N+1}$.
  ```

#### 1.2 `[Multi-Step Leap & Verbalized Summand]` Line `594` — `#019` AtCoder ABC 178 D (Redistribution), Method B
- **File**: [ch01-ring-convolutions-newton-inv.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L591-L597)
- **Issue**: Line 594 writes $[x^S] x^{3k}(1-x)^{-k} = [x^{S-3k}](1-x)^{-k} = \binom{S-2k-1}{k-1}$, compressing the substitution $m = S - 3k$ into $\binom{m + k - 1}{k - 1}$ and the arithmetic simplification $(S - 3k) + k - 1 = S - 2k - 1$ into a single `=` sign.
- **Drop-In Replacement (Lines `591–597`)**:
  ```markdown
  2. **Method B (Direct Binomial Extraction in $O(S)$ Time)**:
     Alternatively, break the sum over the number of parts $k \in \{1, 2, \dots, \lfloor S/3 \rfloor\}$, where the $k$-th summand counts ordered $k$-tuples of integers $\ge 3$ summing to $S$. By the valuation-shift rule $[x^S] \bigl(x^{3k} H(x)\bigr) = [x^{S-3k}] H(x)$ and the negative binomial series $[x^m](1 - x)^{-k} = \binom{m + k - 1}{k - 1}$ applied at $m = S - 3k$:
     $$
     \begin{aligned}
     [x^S] \bigl(x^3(1 - x)^{-1}\bigr)^k
     &= [x^S] x^{3k}(1 - x)^{-k}
     && \text{(factor out the minimum weight } 3k \text{ of } k \text{ parts)} \\[4pt]
     &= [x^{S-3k}](1 - x)^{-k}
     && \text{(shift index by } 3k \text{ remaining distributes across } k \text{ bins)} \\[4pt]
     &= \binom{(S - 3k) + k - 1}{k - 1}
     && \text{(apply } [x^m](1 - x)^{-k} = \binom{m + k - 1}{k - 1} \text{ at } m = S - 3k\text{)} \\[4pt]
     &= \binom{S - 2k - 1}{k - 1}.
     && \text{(simplify } S - 3k + k - 1 = S - 2k - 1\text{)}
     \end{aligned}
     $$
     Summing over all valid part counts $1 \le k \le \lfloor S/3 \rfloor$:
     $$a_S = \sum_{k=1}^{\lfloor S/3 \rfloor} \binom{S - 2k - 1}{k - 1} \pmod{10^9 + 7}.$$
  ```

---

### Chapter 02 (`chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd`)

#### 2.1 `[Multi-Step Leap]` Lines `506–510` — `sparse_ln` Coefficient Extraction
- **File**: [ch02-calculus-frobenius-sparse-ode-newton.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L502-L512)
- **Issue**: Jumps from $\sum_{0 \le d \le n} p_d (n - d) f_{n-d} = n p_n$ directly to $f_n = p_n - \frac{1}{n} \sum_{1 \le d \le n-1} (n - d) p_d f_{n-d}$ in one step, simultaneously isolating $d = 0$ (using $p_0 = 1$), dropping $d = n$ (using $n - d = 0$), moving the remaining sum to the RHS, and dividing by $n$.
- **Drop-In Replacement (Lines `504–511`)**:
  ```markdown
  2. **Sparse Logarithm $F(x) = \ln P(x)$ (given $p_0 = 1$, so $f_0 = 0$)**:
     Differentiating gives $F'(x) = \frac{P'(x)}{P(x)}$, so $P(x) F'(x) = P'(x)$. Extracting $[x^{n-1}]$ for $n \ge 1$ where $[x^{n-d-1}]F'(x) = (n - d)f_{n-d}$ and $[x^{n-1}]P'(x) = n p_n$:
     $$
     \begin{aligned}
     \sum_{d=0}^{n} p_d (n - d) f_{n-d} &= n p_n
     && \text{(extract } [x^{n-1}] \text{ of the Cauchy product } P(x)F'(x) = P'(x)\text{)} \\[4pt]
     p_0 n f_n + \sum_{d=1}^{n-1} (n - d) p_d f_{n-d} + 0 &= n p_n
     && \text{(isolate } d = 0 \text{ and drop } d = n \text{ since } n - n = 0\text{)} \\[4pt]
     f_n &= p_n - \frac{1}{n} \sum_{\substack{1 \le d \le n-1 \\ p_d \ne 0}} (n - d) p_d f_{n-d}.
     && \text{(use } p_0 = 1 \text{ and divide by } n \in \mathbb{F}_p^\times\text{)}
     \end{aligned}
     $$
  ```

#### 2.2 `[Raw Draft Self-Correction]` Line `1206` — `#030` AtCoder ABC 267 Ex (Odd Sum)
- **File**: [ch02-calculus-frobenius-sparse-ode-newton.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L1204-L1210)
- **Issue**: Contains raw draft self-questioning `"Wait: can we simplify even further and call exp only if needed, or exploit $A_i \le 10$?"`.
- **Drop-In Replacement (Line `1206`)**:
  ```markdown
  3. **Exploiting Small Weights $A_i \le 10$ to Avoid General `exp`**:
     Can we bypass general polynomial `exp` entirely by exploiting the constraint $A_i \le 10$?
  ```

#### 2.3 `[Boundary / Invariant Precision]` Lines `1309–1318` — `#091` Codeforces 891E (Lust)
- **File**: [ch02-calculus-frobenius-sparse-ode-newton.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L1309-L1318)
- **Issue**: States that $P(x) = \prod_{i=1}^n (a_i - x)$ is computed in $O(n^2)$ time by a simple DP, without stating the exact outer/inner loop index boundaries (`i = 1..n`, `j = i` down to `0`) and the in-place loop invariant that prevents overwriting $c_{j-1}$ before it is read.
- **Drop-In Replacement (Lines `1311–1315`)**:
  ```markdown
  4. **Final $O(n^2)$ Algorithm**:
     - Initialize $P^{(0)}(x) = c_0 = 1$ and $c_1 = \dots = c_n = 0$. For $i = 1, 2, \dots, n$, update the coefficients in-place in **descending** degree order $j = i, i - 1, \dots, 0$ via $c_j \gets a_i c_j - c_{j-1}$ (with $c_{-1} = 0$). **Loop Invariant**: After outer step $i$, $\sum_{j=0}^i c_j x^j = \prod_{r=1}^i (a_r - x)$, and iterating $j$ from $i$ down to $0$ guarantees $c_{j-1}$ still holds its step-$(i-1)$ value when computing the new $c_j$.
  ```

---

### Chapter 03 (`chapters/ch03-mset-partitions-euler-polya.qmd`)

#### 3.1 `[Multi-Step Leap]` Lines `971–978` — `#001` AtCoder `fps-24` A (Snack), Variant B
- **File**: [ch03-mset-partitions-euler-polya.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L970-L979)
- **Issue**: Compresses isolating $i = 0$ ($q_0 = 1$), shifting the $i \ge 1$ terms to the RHS, and combining $D i q_i y_{n-i} - (n - i) q_i y_{n-i} = q_i (i(D + 1) - n) y_{n-i}$ into a single `\implies` step.
- **Drop-In Replacement (Lines `973–978`)**:
  ```markdown
  $$
  \begin{aligned}
  \sum_{i=0}^{\min(5, n)} q_i (n - i) y_{n-i} &= D \sum_{i=1}^{\min(5, n)} i q_i y_{n-i}
  && \text{(extract } [x^{n-1}] \text{ from } Q(x) Y'(x) = D Q'(x) Y(x)\text{)} \\[4pt]
  q_0 n y_n + \sum_{i=1}^{\min(5, n)} q_i (n - i) y_{n-i} &= \sum_{i=1}^{\min(5, n)} D i q_i y_{n-i}
  && \text{(isolate the } i = 0 \text{ term on the LHS)} \\[4pt]
  n y_n &= \sum_{i=1}^{\min(5, n)} q_i \bigl(i(D + 1) - n\bigr) y_{n-i}.
  && \text{(use } q_0 = 1 \text{ and collect } D i - (n - i) = i(D + 1) - n\text{)}
  \end{aligned}
  $$
  ```

#### 3.2 `[Raw Draft Self-Correction]` Line `1277` — `#221` LibreOJ 6089 (小 Y 的背包计数问题), Hint 1
- **File**: [ch03-mset-partitions-euler-polya.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L1275-L1281)
- **Issue**: Hint 1 contains `"Wait: the modulus is $23333333$ (which is prime, not NTT-friendly), and $\ln / \exp$ takes $O(N \log N)$ with MTT or $O(N \sqrt{N})$ without FFT!"`.
- **Drop-In Replacement (Line `1277`)**:
  ```markdown
  Notice the modulus Obstacle: $p = 23333333$ is prime ($23333333 > N$, so $1, \dots, N$ are invertible), but $p - 1 = 2^2 \times 5833333$ is not NTT-friendly! Can we avoid FFT/MTT altogether and achieve $O(N\sqrt{N})$ time using only simple $O(N)$ array passes?
  ```

---

### Chapter 04 (`chapters/ch04-egf-set-cyc-boxed-prufer.qmd`)

#### 4.1 `[Multi-Step Leap]` Line `379` — §4.4 Generalized Cayley Forest Formula
- **File**: [ch04-egf-set-cyc-boxed-prufer.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L377-L382)
- **Issue**: Compresses factoring $\prod_{i=1}^k s_i$ out of the coefficient extractor, summing the exponents $\sum_{i=1}^k s_i x = n x$, and extracting $(k - 2)![x^{k-2}]e^{nx} = n^{k-2}$ into one `=` sign.
- **Drop-In Replacement (Lines `378–381`)**:
  ```markdown
  $$
  \begin{aligned}
  \text{Forests}(s_1, \dots, s_k)
  &= (k - 2)! [x^{k-2}] \prod_{i=1}^{k} \bigl(s_i e^{s_i x}\bigr)
  && \text{(Prüfer EGF over } k \text{ super-nodes of weights } s_i\text{)} \\[4pt]
  &= \left(\prod_{i=1}^{k} s_i\right) (k - 2)! [x^{k-2}] \exp\!\left(\sum_{i=1}^{k} s_i x\right)
  && \text{(factor constants } s_i \text{ and combine exponentials)} \\[4pt]
  &= \left(\prod_{i=1}^{k} s_i\right) (k - 2)! [x^{k-2}] e^{n x}
  && \text{(substitute total vertex count } \sum_{i=1}^{k} s_i = n\text{)} \\[4pt]
  &= \left(\prod_{i=1}^{k} s_i\right) n^{k-2}.
  && \text{(extract } (k - 2)! [x^{k-2}] e^{n x} = n^{k-2}\text{)}
  \end{aligned}
  $$
  ```

#### 4.2 `[Multi-Step Leap]` Line `1068` — `#174` Luogu P5401 (珍珠 / Pearls)
- **File**: [ch04-egf-set-cyc-boxed-prufer.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L1065-L1072)
- **Issue**: Line 1068 writes $g_k = \frac{\binom{D}{k} k!}{2^k} n! [x^n] \dots$, whereas Hint 3 (line 1032) and the code use $\frac{D!}{(D - k)! 2^k}$; show the intermediate factorial cancellation explicitly.
- **Drop-In Replacement (Lines `1067–1070`)**:
  ```markdown
  $$
  g_k = \binom{D}{k} n! [x^n] \left(\frac{e^x - e^{-x}}{2}\right)^k e^{(D - k)x}
  = \frac{D!}{k!(D - k)!} \cdot \frac{k!}{2^k} \, n! [x^n] \frac{(e^x - e^{-x})^k}{k!} e^{(D - k)x}
  = \frac{D!}{(D - k)! \, 2^k} \sum_{j=0}^{k} (-1)^{k - j} \binom{k}{j} (D - 2k + 2j)^n.
  $$
  ```

---

### Chapter 05 (`chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd`)

#### 5.1 `[Multi-Step Leap]` Line `1357` — `#040` AtCoder ABC 300 Ex (Fibonacci: Revisited)
- **File**: [ch05-rational-bostan-mori-berlekamp-massey.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1354-L1361)
- **Issue**: Compresses $(1 - x)\sum_{n=0}^{K-1}(1 - n)x^n = 1 - x - x^2 - \cdots - x^{K-1} + (K - 2)x^K$ into one `=` sign without showing the index-shifted subtraction.
- **Drop-In Replacement (Lines `1356–1360`)**:
  ```markdown
  $$
  \begin{aligned}
  (1 - x)P_0(x)
  &= \sum_{n=0}^{K-1} (1 - n) x^n - \sum_{n=0}^{K-1} (1 - n) x^{n+1}
  && \text{(distribute } 1 - x \text{ across } P_0(x)\text{)} \\[4pt]
  &= 1 + \sum_{n=1}^{K-1} \bigl((1 - n) - (2 - n)\bigr) x^n - (2 - K) x^K
  && \text{(reindex second sum via } n \gets n - 1 \text{ and combine } x^n\text{)} \\[4pt]
  &= 1 - x - x^2 - \cdots - x^{K-1} + (K - 2)x^K.
  && \text{(simplify } (1 - n) - (2 - n) = -1\text{)}
  \end{aligned}
  $$
  ```

#### 5.2 `[Multi-Step Leaps]` Lines `1794–1803` — `#073` AtCoder AGC 054 E (ZigZag Break)
- **File**: [ch05-rational-bostan-mori-berlekamp-massey.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1791-L1805)
- **Issue**:
  1. Line `1794` substitutes $B = k + A + 2$ into $(B - A - 1)(B - 3)!$ and converts $\frac{(k + A - 1)!}{(A - 1)! k!} = \binom{k + A - 1}{A - 1}$ in a single `=` sign.
  2. Line `1803` jumps from $\sum_{k=0}^\infty (k + 1)\binom{k + A - 1}{A - 1}x^k$ directly to $\frac{1 + (A - 1)x}{(1 - x)^{A+1}}$ without displaying the intermediate split $k + 1 = (k + A) - (A - 1)$ and the negative binomial sums.
- **Drop-In Replacement (Lines `1792–1805`)**:
  ```markdown
  Let $k = B - A - 2 \ge 0$, so $B = k + A + 2$, $B - A - 1 = k + 1$, and $B - 3 = k + A - 1$. Multiplying and dividing by $(A - 1)!$ to form a binomial coefficient in $k$:
  $$
  (B - A - 1)(B - 3)!
  = (k + 1)(k + A - 1)!
  = (A - 1)! \, k! \, (k + 1) \frac{(k + A - 1)!}{(A - 1)! \, k!}
  = (A - 1)! \, k! \, (k + 1) \binom{k + A - 1}{A - 1}.
  $$
  Look at the factor $(k + 1) \binom{k + A - 1}{A - 1}$. Using $k + 1 = (k + A) - (A - 1)$ and $\frac{k + A}{A}\binom{k + A - 1}{A - 1} = \binom{k + A}{A}$, its ordinary generating function is:
  $$
  \begin{aligned}
  G_A(x)
  &= \sum_{k=0}^{\infty} (k + 1) \binom{k + A - 1}{A - 1} x^k \\[4pt]
  &= A \sum_{k=0}^{\infty} \binom{k + A}{A} x^k - (A - 1) \sum_{k=0}^{\infty} \binom{k + A - 1}{A - 1} x^k
  && \text{(split } (k + 1)\binom{k+A-1}{A-1} = A\binom{k+A}{A} - (A-1)\binom{k+A-1}{A-1}\text{)} \\[4pt]
  &= \frac{A}{(1 - x)^{A+1}} - \frac{A - 1}{(1 - x)^A}
  && \text{(apply } \sum_{k \ge 0} \binom{k+r}{r} x^k = (1 - x)^{-(r+1)}\text{)} \\[4pt]
  &= \frac{A - (A - 1)(1 - x)}{(1 - x)^{A+1}} = \frac{1 + (A - 1)x}{(1 - x)^{A+1}}.
  && \text{(combine over common denominator } (1 - x)^{A+1}\text{)}
  \end{aligned}
  $$
  ```

---

### Chapter 06 (`chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd`)

#### 6.1 `[Multi-Step Leap]` Lines `708–709` — §6.4 Eulerian Row Extraction from Worpitzky's Identity
- **File**: [ch06-binomial-snake-oil-taylor-shift-stirling.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L704-L716)
- **Issue**: Compresses four distinct operations (summing Worpitzky's identity over $m \ge 0$, applying Kernel `K1` $\sum_{m \ge 0} \binom{m + n - k}{n} x^m = \frac{x^{k-n}}{(1 - x)^{n+1}}$, applying the reversal symmetry $\left\langle \begin{matrix} n \\ n - 1 - j \end{matrix} \right\rangle = \left\langle \begin{matrix} n \\ j \end{matrix} \right\rangle$, and shifting $m \gets m + 1$) into a single line.
- **Drop-In Replacement (Lines `706–712`)**:
  ```markdown
  3. **Apply Snake Oil (`K1`) & Eulerian Reversal Symmetry**:
     Using the reversal symmetry $\left\langle \begin{matrix} n \\ k \end{matrix} \right\rangle = \left\langle \begin{matrix} n \\ n - 1 - k \end{matrix} \right\rangle$ (reversing a permutation swaps ascents and descents), set $j = n - 1 - k$ in Worpitzky's identity so $\binom{m + k}{n} = \binom{m + n - 1 - j}{n}$. Now multiply by $x^m$ and sum over $m \ge 1$ (setting $r = m - 1 \ge 0$):
     $$
     \begin{aligned}
     \sum_{r=0}^{\infty} (r + 1)^n x^r
     &= \sum_{r=0}^{\infty} \sum_{j=0}^{n-1} \left\langle \begin{matrix} n \\ j \end{matrix} \right\rangle \binom{r + n - j}{n} x^r
     && \text{(substitute Worpitzky at } m = r + 1 \text{ with } j = n - 1 - k\text{)} \\[4pt]
     &= \sum_{j=0}^{n-1} \left\langle \begin{matrix} n \\ j \end{matrix} \right\rangle x^j \sum_{r=j}^{\infty} \binom{(r - j) + n}{n} x^{r-j}
     && \text{(swap sums and factor } x^j \text{ so inner index is } s = r - j \ge 0\text{)} \\[4pt]
     &= \frac{1}{(1 - x)^{n+1}} \sum_{j=0}^{n-1} \left\langle \begin{matrix} n \\ j \end{matrix} \right\rangle x^j.
     && \text{(apply Kernel K1: } \sum_{s \ge 0} \binom{s + n}{n} x^s = (1 - x)^{-(n+1)}\text{)}
     \end{aligned}
     $$
     Multiplying both sides by $(1 - x)^{n+1}$ isolates the Eulerian row polynomial $A_n(x)$ as a single truncated polynomial product:
     $$A_n(x) = \sum_{j=0}^{n-1} \left\langle \begin{matrix} n \\ j \end{matrix} \right\rangle x^j = (1 - x)^{n+1} \sum_{r=0}^{\infty} (r + 1)^n x^r \pmod{x^n}.$$
  ```

#### 6.2 `[Mathematical / Sign Fix & Multi-Step Leap]` Line `1122` — `#094` Codeforces 923E (Perpetual Subtraction)
- **File**: [ch06-binomial-snake-oil-taylor-shift-stirling.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L1120-L1125)
- **Issue**: Line 1122 writes:
  > `(Indeed, $\sum_{j=i}^k \frac{1}{j + 1} (-1)^{j - i} \binom{j}{i} \binom{k}{j} = \binom{k}{i} \sum_{j=i}^k (-1)^{j-i} \binom{k-i}{j-i} \frac{1}{j+1} = \frac{1}{k + 1} \delta_{i, k}$ on the eigenbasis, confirming $M = P \Lambda P^{-1}$.)`
  This is both a multi-step leap and mathematically incorrect as written:
  1. For $(P \Lambda P^{-1})_{i,k}$, since $P_{i,j} = \binom{j}{i}$, $\Lambda_{j,j} = \frac{1}{j+1}$, and $(P^{-1})_{j,k} = (-1)^{k-j}\binom{k}{j}$, the sign is $(-1)^{k-j}$, **not** $(-1)^{j-i}$.
  2. Furthermore, the $(i, k)$ entry of $M = P \Lambda P^{-1}$ is $M_{i,k} = \frac{1}{k+1}$ for **all** $0 \le i \le k$, **not** $\frac{1}{k+1}\delta_{i,k}$! (Indeed, $\binom{k}{i} \sum_{r=0}^{k-i} (-1)^{k-i-r} \binom{k-i}{r} \frac{1}{i+1+r} = \binom{k}{i} (-1)^{k-i} \frac{(k-i)! i!}{(k+1)!} (-1)^{k-i} = \frac{1}{k+1} = M_{i,k}$.)
- **Drop-In Replacement (Line `1122`)**:
  ```markdown
     (Indeed, for every $0 \le i \le k$, $(P \Lambda P^{-1})_{i,k} = \sum_{j=i}^k \binom{j}{i} \frac{1}{j+1} (-1)^{k-j} \binom{k}{j} = \binom{k}{i} \int_0^1 x^i (x - 1)^{k-i}\,dx$ at $i = 0$ — or algebraically via $\binom{j}{i}\frac{1}{j+1} = \frac{1}{i+1}\binom{j+1}{i+1}$ and Pascal's identity, every column $j$ of $P$ satisfies $(M P)_{i,j} = \frac{1}{j+1}\sum_{r=i}^j \binom{r}{i} = \frac{1}{j+1}\binom{j+1}{i+1} = \binom{j}{i}\frac{1}{j+1} = (P \Lambda)_{i,j}$, immediately confirming $M P = P \Lambda \iff M = P \Lambda P^{-1}$!)
  ```

---

### Chapter 07 (`chapters/ch07-roots-of-unity-cyclotomic-czt.qmd`)

#### 7.1 `[Raw Draft Self-Correction]` Line `328` — §7.3.1 Scratchpad Step 4
- **File**: [ch07-roots-of-unity-cyclotomic-czt.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd#L326-L331)
- **Issue**: Contains conversational `"Wait—test this over a finite field $\mathbb{F}_p$!"`.
- **Drop-In Replacement (Line `328`)**:
  ```markdown
    4. **Crucial Finite-Field Pitfall (`Failure Mode #6`)**: Does $c^{j k} = \bigl(c^{1/2}\bigr)^{(j+k)^2 - j^2 - k^2}$ always work over $\mathbb{F}_p$? What if $c$ is a **quadratic non-residue** modulo $p$, so $c^{1/2} = \sqrt{c} \notin \mathbb{F}_p$ does not exist?
  ```

#### 7.2 `[Multi-Step Leap]` Line `1457` — `#092` Codeforces 958F3 / Mastery 1
- **File**: [ch07-roots-of-unity-cyclotomic-czt.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd#L1454-L1461)
- **Issue**: Compresses substituting $a_i - b_i = a_0 + (\delta_i - b_i)$, expanding the square $(a_0 + (\delta_i - b_i))^2$, and distributing $\sum_{i=0}^{n-1}$ across the three terms into a single `=` sign.
- **Drop-In Replacement (Lines `1456–1460`)**:
  ```markdown
  $$
  \begin{aligned}
  \sum_{i=0}^{n-1} (a_i - b_i)^2
  &= \sum_{i=0}^{n-1} \bigl(a_0 + (\delta_i - b_i)\bigr)^2
  && \text{(substitute } a_i = a_0 + \delta_i\text{)} \\[4pt]
  &= \sum_{i=0}^{n-1} \Bigl(a_0^2 + 2(\delta_i - b_i)a_0 + (\delta_i - b_i)^2\Bigr)
  && \text{(expand the quadratic in } a_0\text{)} \\[4pt]
  &= n a_0^2 + 2\left(\sum_{i=0}^{n-1} (\delta_i - b_i)\right) a_0 + \sum_{i=0}^{n-1} (\delta_i - b_i)^2.
  && \text{(distribute } \sum_{i=0}^{n-1} \text{ and factor out } a_0\text{)}
  \end{aligned}
  $$
  ```

---

### Chapter 08 (`chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd`)

#### 8.1 `[Multi-Step Leap]` Line `75` — §8.1 Cumulative At-Least-$k$ Extraction
- **File**: [ch08-connected-component-ie-rook-goulden-jackson.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd#L71-L78)
- **Issue**: States $\sum_{r=k}^j (-1)^{j-r}\binom{j}{r} = (-1)^{j-k}\binom{j-1}{k-1}$ in one `=` sign without showing the Pascal telescoping step $\binom{j}{r} = \binom{j-1}{r} + \binom{j-1}{r-1}$.
- **Drop-In Replacement (Lines `73–77`)**:
  ```markdown
  $$
  \begin{aligned}
  E_{\ge k}
  &= \sum_{j=k}^{m} G_j \sum_{r=k}^{j} (-1)^{j-r} \binom{j}{r}
  && \text{(swap the sums over } r \text{ and } j\text{)} \\[4pt]
  &= \sum_{j=k}^{m} G_j \sum_{r=k}^{j} \left[(-1)^{j-r}\binom{j-1}{r} - (-1)^{j-(r-1)}\binom{j-1}{r-1}\right]
  && \text{(expand } \binom{j}{r} = \binom{j-1}{r} + \binom{j-1}{r-1} \text{ to telescope)} \\[4pt]
  &= \sum_{j=k}^{m} (-1)^{j-k} \binom{j - 1}{k - 1} G_j.
  && \text{(telescope from } r = k \text{ to } r = j\text{, since } \binom{j-1}{j} = 0\text{)}
  \end{aligned}
  $$
  ```

#### 8.2 `[Multi-Step Leap]` Line `1073` — `#139` Codeforces Gym 102978H (Harsh Comments)
- **File**: [ch08-connected-component-ie-rook-goulden-jackson.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd#L1070-L1077)
- **Issue**: Compresses $\frac{1}{1 - 2x + \frac{2x^2}{1+x}} = \frac{1+x}{1-x}$ into a single `=` sign without showing the clearing of $(1 + x)$ and cancellation of $-2x^2 + 2x^2$.
- **Drop-In Replacement (Lines `1072–1075`)**:
  ```markdown
  $$
  F(x) = \frac{1}{1 - 2x + \frac{2x^2}{1 + x}}
  = \frac{1 + x}{(1 - 2x)(1 + x) + 2x^2}
  = \frac{1 + x}{(1 - x - 2x^2) + 2x^2}
  = \frac{1 + x}{1 - x}
  = 1 + 2x + 2x^2 + 2x^3 + \cdots
  $$
  ```

---

### Chapter 09 (`chapters/ch09-cdq-fft-online-relaxed-convolution.qmd`)

#### 9.1 `[Multi-Step Leap]` Line `1284` — `#075` AtCoder AGC 060 D (Same Generating Function)
- **File**: [ch09-cdq-fft-online-relaxed-convolution.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch09-cdq-fft-online-relaxed-convolution.qmd#L1281-L1288)
- **Issue**: Compresses expanding the product $\prod_{i=1}^{N-1}(1 + \sigma_i(P)\sigma_i(Q))$ over subsets $T \subseteq [1, N-1]$, swapping the sum over $T$ with the double sum over $(P, Q) \in S_N^2$, and factoring the decoupled double sum into a square into a single `=` sign.
- **Drop-In Replacement (Lines `1282–1287`)**:
  ```markdown
  $$
  \begin{aligned}
  \text{Ans}
  &= \sum_{P, Q \in S_N} \prod_{i=1}^{N-1} \frac{1 + \sigma_i(P)\sigma_i(Q)}{2}
  && \text{(indicator that } \sigma_i(P) = \sigma_i(Q) \text{ for all } 1 \le i \le N-1\text{)} \\[4pt]
  &= \frac{1}{2^{N-1}} \sum_{P, Q \in S_N} \sum_{T \subseteq \{1, \dots, N-1\}} \left(\prod_{i \in T} \sigma_i(P)\right) \left(\prod_{i \in T} \sigma_i(Q)\right)
  && \text{(expand the product of } N - 1 \text{ binomials over subsets } T\text{)} \\[4pt]
  &= \frac{1}{2^{N-1}} \sum_{T \subseteq \{1, \dots, N-1\}} \left( \sum_{P \in S_N} \prod_{i \in T} \sigma_i(P) \right)^2.
  && \text{(swap sums and factor the independent sums over } P, Q \in S_N\text{)}
  \end{aligned}
  $$
  ```

---

### Chapter 10 (`chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd`)

#### 10.1 `[Multi-Step Leap]` Line `408` — §10.3 Case 2: Pólya $S_3$ Ternary Trees Newton Step
- **File**: [ch10-implicit-equations-newton-unlabeled-trees-otter.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd#L405-L412)
- **Issue**: Compresses placing $A_d(x)$ over the common denominator $1 - \frac{x}{2}(A_d(x)^2 + P_2(x))$ and canceling $A_d(x) - \frac{x}{2}A_d(x)P_2(x)$ into a single `\equiv` sign.
- **Drop-In Replacement (Lines `406–411`)**:
  ```markdown
  $$
  \begin{aligned}
  A_{2d}(x)
  &\equiv A_d(x) - \frac{A_d(x) - 1 - \frac{x}{6}\bigl(A_d(x)^3 + 3 A_d(x) P_2(x) + 2 P_3(x)\bigr)}{1 - \frac{x}{2}\bigl(A_d(x)^2 + P_2(x)\bigr)} \\[4pt]
  &\equiv \frac{A_d(x)\bigl(1 - \frac{x}{2}A_d(x)^2 - \frac{x}{2}P_2(x)\bigr) - A_d(x) + 1 + \frac{x}{6}A_d(x)^3 + \frac{x}{2}A_d(x)P_2(x) + \frac{x}{3}P_3(x)}{1 - \frac{x}{2}\bigl(A_d(x)^2 + P_2(x)\bigr)} \\[4pt]
  &\equiv \frac{1 - \frac{x}{3}\bigl(A_d(x)^3 - P_3(x)\bigr)}{1 - \frac{x}{2}\bigl(A_d(x)^2 + P_2(x)\bigr)} \pmod{x^{2d}}.
  \end{aligned}
  $$
  ```

#### 10.2 `[Multi-Step Leap]` Lines `1147–1149` — `#126` Codeforces 1687F (Koishi's Unconscious Permutation)
- **File**: [ch10-implicit-equations-newton-unlabeled-trees-otter.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd#L1143-L1153)
- **Issue**: Invokes the change-of-variables identity $[u^k]\psi(u)^j = [w^{k-j}]\left(\frac{g(w)}{w}\right)^{-k-1} g'(w)$ and states in prose that summing over $j$ reduces to a 1D shift without writing out the intermediate single-step equation.
- **Drop-In Replacement (Lines `1146–1151`)**:
  ```markdown
     By the Cauchy Residue Change of Variables $u = g(w)$ (which we formalize systematically in Chapter 11; equivalently via the bivariate compositional inverse of $u = w(1 + G(w))$):
     $$
     \begin{aligned}
     \sum_{j=0}^{k} c_j [u^k] \psi(u)^j
     &= \sum_{j=0}^{k} c_j [w^{k-j}] \left(\frac{g(w)}{w}\right)^{-k-1} g'(w)
     && \text{(change variables } u = g(w) \iff w = \psi(u)\text{)} \\[4pt]
     &= [w^k] \left( \left(\sum_{j=0}^{k} c_j w^j\right) \left(\frac{g(w)}{w}\right)^{-k-1} g'(w) \right).
     && \text{(absorb } [w^{k-j}] = [w^k] w^j \text{ into a polynomial product)}
     \end{aligned}
     $$
  ```

---

### Chapter 11 (`chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd`)

#### 11.1 `[Multi-Step Leap]` Line `326` — §11.2.2 Form 4a ($r$-Forests of $k$-ary Trees)
- **File**: [ch11-laurent-residues-raney-lagrange-inversion.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd#L323-L330)
- **Issue**: Compresses combining $r G(w)^{r-1} G'(w) G(w)^{kn} = \frac{r}{kn + r} \frac{d}{dw}\bigl(G(w)^{kn+r}\bigr)$ and applying $[w^{n-1}] H'(w) = n [w^n] H(w)$ to cancel $n$ into a single `=` sign.
- **Drop-In Replacement (Lines `325–329`)**:
  ```markdown
  $$
  \begin{aligned}
  [x^n] F(x)^r
  &= \frac{1}{n} [w^{n-1}] \bigl( r G(w)^{r-1} G'(w) G(w)^{kn} \bigr)
  && \text{(apply LIF Form 2 with } H(w) = w^r \circ G(w)\text{)} \\[4pt]
  &= \frac{r}{n(kn + r)} [w^{n-1}] \frac{d}{dw} \Bigl( G(w)^{kn + r} \Bigr)
  && \text{(chain rule: } (G^{kn+r})' = (kn + r) G^{kn + r - 1} G'\text{)} \\[4pt]
  &= \frac{r}{kn + r} [w^n] G(w)^{kn + r}
  && \text{(apply } [w^{n-1}] A'(w) = n [w^n] A(w) \text{ to cancel } n\text{)} \\[4pt]
  &= \frac{r}{kn + r} \binom{kn + r}{n}.
  && \text{(substitute } G(w) = 1 + w\text{)}
  \end{aligned}
  $$
  ```

#### 11.2 `[Unexplained Shorthand]` Line `506` — §11.3.1 Bruns's Lemma Proof
- **File**: [ch11-laurent-residues-raney-lagrange-inversion.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd#L504-L509)
- **Issue**: Uses `"trivially $S_n = 0$ for $n \ge M$"` instead of stating why the degree bound implies $[t^n](1 + t)^m = 0$.
- **Drop-In Replacement (Line `506`)**:
  ```markdown
  *Proof.* Since $P(t)$ has degree $< M$, it is a linear combination of the binomial basis polynomials $(1 + t)^m$ for $0 \le m < M$. For each basis element $(1 + t)^m$ with $0 \le m < M$, the polynomial $(1 + t)^m$ has degree $m < M \le n$, so its coefficient of $t^n$ is zero for every $n \ge M$.
  ```

#### 11.3 `[Multi-Step Leap]` Line `1583` — `#114` Codeforces 1349F2 (Slime and Sequences)
- **File**: [ch11-laurent-residues-raney-lagrange-inversion.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd#L1580-L1587)
- **Issue**: Jumps from $\operatorname{Res}_{w=0} \frac{\frac{e^w - 1}{w}}{\frac{e^w - 1}{w} - 1} \cdot \frac{dw}{w^{j+1}}$ directly to $[w^j] \left(\frac{e^w - 1}{e^w - 1 - w}\right)$ in one `=` sign without showing multiplication of numerator and denominator by $w$.
- **Drop-In Replacement (Lines `1582–1585`)**:
  ```markdown
  $$
  \sum_{m=1}^{n+1} C_{m, j} x^m
  = \operatorname{Res}_{w=0} \frac{\frac{e^w - 1}{w}}{\frac{e^w - 1}{w} - 1} \cdot \frac{dw}{w^{j+1}}
  = \operatorname{Res}_{w=0} \frac{e^w - 1}{e^w - 1 - w} \cdot \frac{dw}{w^{j+1}}
  = [w^j] \left( \frac{e^w - 1}{e^w - 1 - w} \right).
  $$
  ```

---

### Chapter 12 (`chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`)

#### 12.1 `[Multi-Step Leap]` Line `213` — §12.1.4 Unrooted Labeled Cacti Dissymmetry Simplification
- **File**: [ch12-cacti-deserts-block-cut-biconnected-graphs.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd#L210-L216)
- **Issue**: Jumps from $C(x) = T(x) + B_{\text{cactus}}(T(x)) - T(x) B'_{\text{cactus}}(T(x))$ directly to $\frac{1}{2}\ln\frac{1}{1 - T(x)} + \frac{2T(x) - 5T(x)^2 + T(x)^3}{4(1 - T(x))}$ without showing the intermediate substitution of $B_{\text{cactus}}(y) = \frac{2y - y^2}{4} + \frac{1}{2}\ln\frac{1}{1 - y}$ and $B'_{\text{cactus}}(y) = \frac{1}{2} - \frac{y}{2} + \frac{1}{2(1 - y)}$.
- **Drop-In Replacement (Lines `211–215`)**:
  ```markdown
  Substituting $T = T(x)$, $B_{\text{cactus}}(T) = \frac{2T - T^2}{4} + \frac{1}{2}\ln\frac{1}{1 - T}$, and $T \cdot B'_{\text{cactus}}(T) = \frac{2T - T^2}{2(1 - T)}$ into Theorem 12.1 gives the **Unrooted Connected Cactus EGF** $C(x)$:
  $$
  \begin{aligned}
  C(x)
  &= T + B_{\text{cactus}}(T) - T \cdot B'_{\text{cactus}}(T) \\[4pt]
  &= \frac{1}{2}\ln\frac{1}{1 - T} + T + \frac{2T - T^2}{4} - \frac{2T - T^2}{2(1 - T)}
  && \text{(substitute } B_{\text{cactus}}(T) \text{ and } T B'_{\text{cactus}}(T)\text{)} \\[4pt]
  &= \frac{1}{2}\ln\frac{1}{1 - T(x)} + \frac{2T(x) - 5T(x)^2 + T(x)^3}{4\big(1 - T(x)\big)},
  && \text{(combine rational terms over } 4(1 - T)\text{)}
  \end{aligned}
  $$
  ```

#### 12.2 `[Multi-Step Leap]` Lines `228–230` — §12.1.5 $O(N)$ Recurrence for $H(u) = \exp\bigl(n B'_{\text{cactus}}(u)\bigr)$
- **File**: [ch12-cacti-deserts-block-cut-biconnected-graphs.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd#L225-L234)
- **Issue**: Jumps from $2(1 - 2u + u^2) H'(u) = n(2 - 2u + u^2) H(u)$ directly to the final recurrence for $a_m$ without writing out the intermediate $[u^{m-1}]$ extraction.
- **Drop-In Replacement (Lines `227–232`)**:
  ```markdown
  Clearing the denominator gives $2(1 - 2u + u^2) H'(u) = n(2 - 2u + u^2) H(u)$. Extracting $[u^{m-1}]$ on both sides (where $[u^{m-1}]H'(u) = m a_m$, $[u^{m-1}]u H'(u) = (m-1)a_{m-1}$, and $[u^{m-1}]u^2 H'(u) = (m-2)a_{m-2}$):
  $$
  \begin{aligned}
  2m a_m - 4(m - 1)a_{m-1} + 2(m - 2)a_{m-2} &= 2n a_{m-1} - 2n a_{m-2} + n a_{m-3}
  && \text{(extract } [u^{m-1}] \text{ on both sides)} \\[4pt]
  a_m &= \frac{1}{m}\left((2m - 2 + n) a_{m-1} - (m - 2 + n) a_{m-2} + \frac{n}{2} a_{m-3}\right)
  && \text{(solve for } a_m\text{)}
  \end{aligned}
  $$
  ```

#### 12.3 `[Unexplained Shorthand & Multi-Step Leap]` Line `239` — §12.1.6 Concrete Trace ($N = 4$)
- **File**: [ch12-cacti-deserts-block-cut-biconnected-graphs.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd#L237-L243)
- **Issue**: Uses the unexplained shorthand `"By LIF, $c_4 = \frac{4!}{4}[u^3]\exp(4 B'_{\text{cactus}}(u))"` and jumps straight to the numerical convolution without citing Theorem 11.2 (Lagrange Inversion Form 1).
- **Drop-In Replacement (Line `239`)**:
  ```markdown
  1. **Rooted Cacti $T_4 = 4! [x^4] T(x)$**: Applying Lagrange Inversion Form 1 (Theorem 11.2, $[x^n]T(x) = \frac{1}{n}[u^{n-1}]\phi(u)^n$) to $T = x \exp\bigl(B'_{\text{cactus}}(T)\bigr)$ at $n = 4$ gives $T_4 = \frac{4!}{4} [u^3] \exp\big(4 B'_{\text{cactus}}(u)\big) = 6 [u^3] \exp\big(4u + 2u^3 + \dots\big) = 6 [u^3] \left(\Big(1 + 4u + 8u^2 + \frac{32}{3}u^3\Big)\Big(1 + 2u^3\Big)\right) = 6 \left(\frac{32}{3} + 2\right) = 64 + 12 = 76$.
  ```

#### 12.4 `[Multi-Step Leap]` Line `509` — §12.3.4 $N = 4$ Biconnected Trace
- **File**: [ch12-cacti-deserts-block-cut-biconnected-graphs.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd#L507-L512)
- **Issue**: Jumps from $\exp\bigl(-4x - 4x^2 - 8x^3 - \frac{76}{3}x^4 + O(x^5)\bigr)$ to $[x^4]\exp(-4R(x)) = -\frac{20}{3}$ in a single `\implies` without showing the $[x^4]$ expansion of $\sum_{k=1}^4 \frac{(-4R(x))^k}{k!}$.
- **Drop-In Replacement (Line `509`)**:
  ```markdown
     - For $n = 4$: Let $A(x) = -4R(x) = -4x - 4x^2 - 8x^3 - \frac{76}{3}x^4 + O(x^5)$. Expanding $[x^4]\exp(A(x)) = [x^4]\left(A + \frac{A^2}{2!} + \frac{A^3}{3!} + \frac{A^4}{4!}\right)$ gives
       $$[x^4]\exp\big(-4R(x)\big) = -\frac{76}{3} + \frac{2(-4)(-8) + (-4)^2}{2} + \frac{3(-4)^2(-4)}{6} + \frac{(-4)^4}{24} = -\frac{76}{3} + 40 - 32 + \frac{32}{3} = -\frac{20}{3}.$$
  ```

---

### Chapter 13 (`chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd`)

#### 13.1 `[Multi-Step Leap]` Line `663` — §13.4.3 Generalized Cayley Forest Determinant Evaluation
- **File**: [ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd#L660-L667)
- **Issue**: Compresses factoring $n$ out of $\prod_{i=1}^{k-1}(n s_i)$, substituting $\sum_{i=1}^{k-1} s_i = n - s_k$, and simplifying $n^{k-1}(1 - \frac{n - s_k}{n}) = n^{k-2} s_k$ on a single line.
- **Drop-In Replacement (Lines `662–666`)**:
  ```markdown
  $$
  \begin{aligned}
  \det(\widetilde{L}_{k,k})
  &= \left(\prod_{i=1}^{k-1} n s_i\right) \left(1 - \sum_{i=1}^{k-1} \frac{s_i^2}{n s_i}\right)
  && \text{(apply the rank-1 matrix determinant lemma)} \\[4pt]
  &= n^{k-1} \left(\prod_{i=1}^{k-1} s_i\right) \left(1 - \frac{\sum_{i=1}^{k-1} s_i}{n}\right)
  && \text{(factor } n^{k-1} \text{ and cancel } s_i \text{ in each fraction)} \\[4pt]
  &= n^{k-1} \left(\prod_{i=1}^{k-1} s_i\right) \left(\frac{s_k}{n}\right) = n^{k-2} \prod_{i=1}^{k} s_i.
  && \text{(use } \sum_{i=1}^{k} s_i = n \implies n - \sum_{i=1}^{k-1} s_i = s_k\text{)}
  \end{aligned}
  $$
  ```

---

### Chapter 14 (`chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd`)

#### 14.1 `[Multi-Step Leap]` Line `296` — §14.2.3 First-Order Taylor Expansion of $(1 - \lambda(1 + t))^{-1}$
- **File**: [ch14-pgf-stopping-times-renewal-poisson-martingales.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd#L294-L300)
- **Issue**: Jumps from $\frac{1}{(1 - \lambda) - \lambda t}$ to $\frac{1}{1 - \lambda} + \frac{\lambda}{(1 - \lambda)^2} t \pmod{t^2}$ in one `\equiv` step without factoring out $\frac{1}{1 - \lambda}$.
- **Drop-In Replacement (Lines `295–298`)**:
  ```markdown
  $$
  \frac{1}{1 - \lambda(1 + t)}
  = \frac{1}{(1 - \lambda) - \lambda t}
  = \frac{1}{1 - \lambda} \cdot \frac{1}{1 - \frac{\lambda}{1 - \lambda} t}
  \equiv \frac{1}{1 - \lambda} + \frac{\lambda}{(1 - \lambda)^2} t \pmod{t^2},
  $$
  ```

#### 14.2 `[Multi-Step Leap]` Line `676` — `#115` Codeforces 1392H (ZS Shuffles Cards)
- **File**: [ch14-pgf-stopping-times-renewal-poisson-martingales.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd#L673-L680)
- **Issue**: Compresses splitting $\sum_{k=1}^n (-1)^{k-1}\binom{n}{k}\bigl(1 + \frac{m}{k}\bigr)$ into two sums and evaluating $\sum_{k=1}^n (-1)^{k-1}\binom{n}{k} = 1 - (1 - 1)^n = 1$ in a single `=` sign.
- **Drop-In Replacement (Lines `675–679`)**:
  ```markdown
  $$
  \begin{aligned}
  \mathbb{E}[I]
  &= \sum_{k=1}^{n} (-1)^{k-1} \binom{n}{k} \frac{k + m}{k}
  && \text{(Min-Max inversion over subset size } k = |S|\text{)} \\[4pt]
  &= \sum_{k=1}^{n} (-1)^{k-1} \binom{n}{k} + m \sum_{k=1}^{n} \frac{(-1)^{k-1}}{k} \binom{n}{k}
  && \text{(split } \frac{k + m}{k} = 1 + \frac{m}{k}\text{)} \\[4pt]
  &= 1 + m \sum_{k=1}^{n} \frac{(-1)^{k-1}}{k} \binom{n}{k}.
  && \text{(evaluate } \sum_{k=1}^n (-1)^{k-1}\binom{n}{k} = 1 - (1 - 1)^n = 1\text{)}
  \end{aligned}
  $$
  ```

---

### Chapter 15 (`chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`)

#### 15.1 `[Multi-Step Leap]` Line `341` — §15.2.3 Two-Root Kernel Elimination on Bounded Strip $[0, H]$
- **File**: [ch15-1d-lattice-walks-chebyshev-kernel-method.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L337-L345)
- **Issue**: Jumps from multiplying the $y_0$ equation by $y_1^{H+2}$ and subtracting the $y_1$ equation multiplied by $y_0^{H+2}$ directly to the final ratio $F_0(x)$ without displaying the intermediate linear equation for $F_0(x)$.
- **Drop-In Replacement (Lines `339–344`)**:
  ```markdown
  To eliminate $F_H(x)$, multiply the first equation by $y_1^{H+2}$ and subtract the second equation multiplied by $y_0^{H+2}$. Since the $F_H(x)$ terms cancel identically:
  $$
  w_{-1} x \bigl(y_1^{H+2} - y_0^{H+2}\bigr) F_0(x)
  = y_0^{s+1} y_1^{H+2} - y_1^{s+1} y_0^{H+2}
  = (y_0 y_1)^{s+1} \bigl(y_1^{H+1-s} - y_0^{H+1-s}\bigr).
  $$
  Using Vieta's relation $y_0 y_1 = \frac{w_{-1}}{w_1}$ and dividing by $w_{-1} x \bigl(y_1^{H+2} - y_0^{H+2}\bigr)$ yields:
  $$
  F_0(x) = \frac{1}{w_{-1} x} \left(\frac{w_{-1}}{w_1}\right)^{s+1} \frac{y_1^{H+1-s} - y_0^{H+1-s}}{y_1^{H+2} - y_0^{H+2}}.
  $$
  ```

#### 15.2 `[Unexplained Shorthand & Multi-Step Leap]` Line `449` — §15.3.3 Duchon's Club Verification
- **File**: [ch15-1d-lattice-walks-chebyshev-kernel-method.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L447-L452)
- **Issue**: Writes `"By LIF, $[x^{3m}] F_0(x) = [x^{3m+1}] u(x) = \frac{1}{3m+1} \binom{3m+1}{m}$"` without citing Theorem 11.2 or showing $[u^{3m}](1 + u^3)^{3m+1} = [u^{3m}]\sum_k \binom{3m+1}{k} u^{3k} = \binom{3m+1}{m}$.
- **Drop-In Replacement (Line `449`)**:
  ```markdown
     - **Verification**: Applying Lagrange Inversion Form 1 (Theorem 11.2) to $u = x(1 + u^3)$ at $n = 3m + 1$ gives
       $$[x^{3m}] F_0(x) = [x^{3m+1}] u(x) = \frac{1}{3m + 1} [u^{3m}] (1 + u^3)^{3m+1} = \frac{1}{3m + 1} \binom{3m + 1}{m}.$$
       For $m = 1$ ($n = 3$ steps): $\frac{1}{4}\binom{4}{1} = 1$.
  ```

#### 15.3 `[Unexplained Shorthand]` Line `695` — `#067` AtCoder AGC 021 E (Ball Eat Chameleons), Hint 1
- **File**: [ch15-1d-lattice-walks-chebyshev-kernel-method.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd#L693-L698)
- **Issue**: Writes `"Obviously we need $R \ge N$ and $R \ge B$."` without stating why $R < B$ or $R < N$ makes it impossible for all $N$ chameleons to turn red.
- **Drop-In Replacement (Line `695`)**:
  ```markdown
  Fix the total number of Red balls $R$ and Blue balls $B = K - R$. Since every chameleon must end up Red, each of the $N$ chameleons must eat at least one Red ball ($R \ge N$), and the total number of Red balls must be at least the total number of Blue balls ($R \ge B$, with $R > B$ strictly required when $R = B$ would leave the very last ball of the sequence unable to provide a strict Red majority).
  ```

---

### Chapter 16 (`chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`)

#### 16.1 `[Multi-Step Leap]` Line `633` — §16.4 Failure Mode #15 (Delannoy / Catalan Residue Check)
- **File**: [ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L630-L637)
- **Issue**: Jumps from $\frac{z_1(t) + t}{z_1(t)\sqrt{1 - 4t}}$ to $\frac{1 + \frac{1 + \sqrt{1 - 4t}}{2}}{\sqrt{1 - 4t}}$ without stating that $z_1(t)$ is a root of $-z^2 + z - t = 0$, which gives $\frac{t}{z_1(t)} = 1 - z_1(t) = \frac{1 + \sqrt{1 - 4t}}{2}$.
- **Drop-In Replacement (Lines `631–636`)**:
  ```markdown
  $$
  \begin{aligned}
  \operatorname{Res}_{z = z_1(t)} \frac{z + t}{z(-z^2 + z - t)}
  &= \frac{z_1(t) + t}{z_1(t)\bigl(1 - 2z_1(t)\bigr)}
  && \text{(apply simple-pole residue formula } \frac{A(z_1)}{B'(z_1)}\text{)} \\[4pt]
  &= \frac{1 + \frac{t}{z_1(t)}}{\sqrt{1 - 4t}}
  && \text{(divide numerator by } z_1(t) \text{ and use } 1 - 2z_1(t) = \sqrt{1 - 4t}\text{)} \\[4pt]
  &= \frac{1 + \bigl(1 - z_1(t)\bigr)}{\sqrt{1 - 4t}} = \frac{3 + \sqrt{1 - 4t}}{2\sqrt{1 - 4t}},
  && \text{(since } z_1^2 - z_1 + t = 0 \implies \frac{t}{z_1} = 1 - z_1 = \frac{1 + \sqrt{1-4t}}{2}\text{)}
  \end{aligned}
  $$
  ```

#### 16.2 `[Unexplained Shorthand]` Line `642` — §16.4 Failure Mode #15
- **File**: [ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L640-L645)
- **Issue**: Uses `"trivially term-by-term"` when describing the residue extraction.
- **Drop-In Replacement (Line `642`)**:
  ```markdown
  2. **Keep the Original Variable $x$ When Extracting $\operatorname{Res}_{x=0}$**: Notice that in the original variable $x$, $\operatorname{Res}_{x=0} x^{-1} F(x, t/x)$ extracts the coefficient $[x^0] F(x, t/x)$ directly term-by-term without any rational root substitution!
  ```

#### 16.3 `[Multi-Step Leap]` Line `1192` — `#053` AtCoder ARC 118 E (Avoid Permutations)
- **File**: [ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd#L1189-L1196)
- **Issue**: Compresses substituting $r = k + 1$ and $r = k$ into $\binom{(N - 3k) + r - 1}{r - 1}$ and factoring out $(-2)^{k-1}$ into a single sentence.
- **Drop-In Replacement (Lines `1191–1195`)**:
  ```markdown
     Extracting $[t^{N-3k}]$ via $[t^m](1 - t)^{-r} = \binom{m + r - 1}{r - 1}$ at $m = N - 3k$ for $r = k + 1$ and $r = k$, and factoring out $(-2)^{k-1}$:
     $$
     \begin{aligned}
     [x^N y^k] P(x, y)
     &= (-2)^k \binom{(N - 3k) + (k + 1) - 1}{(k + 1) - 1} + (-2)^{k-1} \binom{(N - 3k) + k - 1}{k - 1} \\[4pt]
     &= (-2)^{k-1} \left( \binom{N - 2k - 1}{k - 1} - 2 \binom{N - 2k}{k} \right).
     \end{aligned}
     $$
  ```

---

### Chapter 17 (`chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`)

#### 17.1 `[Malformed Draft Equation]` Line `474` — §17.2.4 Theorem 17.4 Proof
- **File**: [ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd#L471-L478)
- **Issue**: Line 474 contains an unfinished draft equation with `...`:
  `$$\frac{x y Q(x, y; t) + F(x; t) + G(y; t)}{1 - t S(x, y)} = \frac{x y}{1 - t S(x, y)} + x y Q(x, y; t) - \dots \implies \big(1 - t S(x, y)\big) x y Q(x, y; t) = x y - F(x; t) - G(y; t).$$`
- **Drop-In Replacement (Lines `473–476`)**:
  ```markdown
  *Proof.* Start from the Fundamental Quarter-Plane Kernel Equation (Theorem 17.1):
  $$
  \big(1 - t S(x, y)\big) x y Q(x, y; t) = x y - F(x; t) - G(y; t).
  $$
  Moving $F(x; t) + G(y; t)$ to the left-hand side and dividing by $1 - t S(x, y)$ (which is a unit in $\mathbb{Q}[x, \bar{x}, y, \bar{y}][[t]]$) yields the exact algebraic decomposition:
  $$
  x y Q(x, y; t) + \frac{F(x; t) + G(y; t)}{1 - t S(x, y)} = \frac{x y}{1 - t S(x, y)}.
  $$
  ```

---

### Chapter 18 (`chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd`)

#### 18.1 `[Multi-Step Leap]` Lines `269–273` — §18.1.3 Krawtchouk Three-Term Recurrence (`#058` ARC 136 F)
- **File**: [ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L267-L275)
- **Issue**: Jumps from $(1 - z^2) F_m'(z) = \big((N - 2m) - N z\big) F_m(z)$ directly to $(r + 1) K_{r+1}(m) = (N - 2m) K_r(m) + (N - r + 1) K_{r-1}(m)$ without displaying the intermediate $[z^r]$ coefficient extraction.
- **Drop-In Replacement (Lines `268–274`)**:
  ```markdown
  3. **Extract $[z^r]$ to Obtain the 3-Term Recurrence**:
     Since $[z^r] F_m'(z) = (r + 1) K_{r+1}(m)$ and $[z^r] z^2 F_m'(z) = (r - 1) K_{r-1}(m)$, extracting $[z^r]$ on both sides of $(1 - z^2) F_m'(z) = \big((N - 2m) - N z\big) F_m(z)$ gives:
     $$
     \begin{aligned}
     (r + 1) K_{r+1}(m) - (r - 1) K_{r-1}(m) &= (N - 2m) K_r(m) - N K_{r-1}(m)
     && \text{(extract } [z^r] \text{ on both sides)} \\[4pt]
     (r + 1) K_{r+1}(m) &= (N - 2m) K_r(m) + (N - r + 1) K_{r-1}(m).
     && \text{(collect } K_{r-1}(m) \text{ on the RHS)}
     \end{aligned}
     $$
  ```

#### 18.2 `[Multi-Step Leap]` Line `1341` — `#202` Luogu P7440 (Mastery 2), Hint 2
- **File**: [ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd#L1339-L1344)
- **Issue**: Jumps from $\widetilde{A}(x) P'(x) = n \widetilde{A}'(x) P(x)$ directly to $m \tilde{a}_0 p_m = \sum_{j \in S \setminus \{0\},\, j \le m} \big(j(n + 1) - m\big) \tilde{a}_j p_{m-j}$ in one `\implies` step without showing the intermediate $[x^{m-1}]$ extraction.
- **Drop-In Replacement (Line `1341`)**:
  ```markdown
  - By Miller's $O(N |S|)$ power recurrence (log-derivative of $P = \widetilde{A}^n$), $\widetilde{A}(x) P'(x) = n \widetilde{A}'(x) P(x)$: extracting $[x^{m-1}]$ gives $\sum_{j \in S} (m - j) \tilde{a}_j p_{m-j} = \sum_{j \in S} n j \tilde{a}_j p_{m-j}$, and isolating $j = 0$ yields $m \tilde{a}_0 p_m = \sum_{j \in S \setminus \{0\},\, j \le m} \big(j(n + 1) - m\big) \tilde{a}_j p_{m-j}$!
  ```

---

### Chapter 19 (`chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd`)

#### 19.1 `[Multi-Step Leap]` Line `169` — §19.1.4 `EI`'s Differential-Residue Engine
- **File**: [ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd#L166-L173)
- **Issue**: Compresses $[x^n] (1 + x)^n (1 + c(1 + x))^n = \operatorname{Res}_{x=0} \left[ x^{-1} \left( \frac{(1 + x)(1 + c + cx)}{x} \right)^n \right]$ into a single `=` sign without showing the intermediate residue definition $[x^n] G(x) = \operatorname{Res}_{x=0}\bigl(x^{-n-1} G(x)\bigr)$ and factoring $x^{-n-1} = x^{-1} \cdot x^{-n}$.
- **Drop-In Replacement (Lines `168–172`)**:
  ```markdown
  $$
  \begin{aligned}
  S(c)
  &= [x^n] (1 + x)^n \bigl(1 + c(1 + x)\bigr)^n \\[4pt]
  &= \operatorname{Res}_{x=0} \Bigl[ x^{-n-1} (1 + x)^n (1 + c + cx)^n \Bigr]
  && \text{(write } [x^n] G(x) = \operatorname{Res}_{x=0} x^{-n-1} G(x)\text{)} \\[4pt]
  &= \operatorname{Res}_{x=0} \left[ x^{-1} \left( \frac{(1 + x)(1 + c + cx)}{x} \right)^n \right].
  && \text{(absorb } x^{-n} \text{ into the } n\text{-th power)}
  \end{aligned}
  $$
  ```

---

### Chapter 20 (`chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd`)

#### 20.1 `[Raw Draft Self-Correction]` Lines `359–360` — §20.3.2 Transposed Multipoint Evaluation Derivation
- **File**: [ch20-tellegen-transposition-multipoint-sampling-shift.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd#L355-L370)
- **Issue**: Lines 359–360 contain conversational live scratch-notes (`"To transpose this gate clearly in terms of mulT, pad F(x) to length n, reverse or align indices... Let us check the exact index algebra with Q_u(x): in the primal circuit, if we instead define the root extraction... how do we write the root initialization cleanly?"`) before presenting the clean derivation on lines 361–371.
- **Drop-In Replacement (Lines `359–362`)**:
  ```markdown
  To express the transposed root initialization cleanly in terms of $\operatorname{mul}_T$, let us align the primal root reduction with the reversed divisor $Q_{\text{root}}^{\text{rev}}(x) = x^m Q_{\text{root}}(x^{-1}) = \prod_{i=0}^{m-1} (1 - c_i x)$:
  ```

---

### Chapter 21 (`chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd`)

#### 21.1 `[Mathematical / Exponent Fix & Single-Step Expansion]` Line `316` — §21.2.1 Theorem 21.1(2) ($w$-Plane Single-$n$ Form)
- **File**: [ch21-kinoshita-li-composition-power-projection-revert.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd#L312-L320)
- **Issue**: Line 316 writes:
  `$$[u^n] F(u) = [w^n] \left[ H(g(w)) \left(\frac{w}{g(w)}\right)^{n+1} \frac{(1 + g(w))^{\alpha n + \gamma + 1}}{1 + (\beta + 1)g(w)} \right] = [w^n] \left[ H(g(w)) \frac{(1 + g(w))^{(\alpha + \beta)n + \gamma + 1}}{1 + (\beta + 1)g(w)} \right].$$`
  Because $\frac{w}{g(w)} = (1 + g(w))^\beta$, the middle expression $\left(\frac{w}{g(w)}\right)^{n+1} (1 + g(w))^{\alpha n + \gamma + 1}$ actually equals $(1 + g(w))^{(\alpha + \beta)n + \beta + \gamma + 1}$, **not** $(1 + g(w))^{(\alpha + \beta)n + \gamma + 1}$! Why? Because in the residue change of variables:
  $$\frac{du}{u^{n+1}} = \frac{g'(w)\,dw}{g(w)^{n+1}} = \frac{dw}{w^{n+1}} \left(\frac{w}{g(w)}\right)^{n+1} g'(w) = \frac{dw}{w^{n+1}} (1 + g(w))^{\beta(n+1)} \frac{(1 + g(w))^{-(\beta - 1)}}{1 + (\beta + 1)g(w)} = \frac{dw}{w^{n+1}} \frac{(1 + g(w))^{\beta n + 2}}{1 + (\beta + 1)g(w)}.$$
  Multiplying this by $(1 + g(w))^{\alpha n + \gamma - 1}$ (the exponent from line 311) gives the final exponent $(\alpha + \beta)n + \gamma + 1$! Writing both $\left(\frac{w}{g(w)}\right)^{n+1}$ and $(1 + g(w))^{\alpha n + \gamma + 1}$ together double-counted $(1 + g(w))^\beta$.
- **Drop-In Replacement (Lines `314–318`)**:
  ```markdown
  2. **(Single-$n$ $w$-Plane Form)**: Substituting $u = g(w) = w(1 + g(w))^{-\beta}$ and $du = \frac{(1 + g(w))^{1 - \beta}}{1 + (\beta + 1)g(w)}\,dw$ into $[u^n]F(u) = \operatorname{Res}_{u=0} F(u) u^{-n-1}\,du$:
     $$
     \begin{aligned}
     [u^n] F(u)
     &= [w^n] \left[ H(g(w)) (1 + g(w))^{\alpha n + \gamma - 1} \left(\frac{w}{g(w)}\right)^{n+1} g'(w) \right] \\[4pt]
     &= [w^n] \left[ H(g(w)) (1 + g(w))^{\alpha n + \gamma - 1} (1 + g(w))^{\beta(n+1)} \frac{(1 + g(w))^{1 - \beta}}{1 + (\beta + 1)g(w)} \right] \\[4pt]
     &= [w^n] \left[ H(g(w)) \frac{(1 + g(w))^{(\alpha + \beta)n + \gamma + 1}}{1 + (\beta + 1)g(w)} \right].
     \end{aligned}
     $$
  ```

---

### Chapter 22 (`chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd`)

#### 22.1 `[Multi-Step Leap]` Line `527` — §22.4 Alternative Edge-Count Derivation
- **File**: [ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd#L523-L529)
- **Issue**: Compresses $\binom{N}{k} + \sum_{e=(u,v) \in E} \left[\binom{N}{k} - \binom{\text{sz}[v]}{k} - \binom{N - \text{sz}[v]}{k}\right] = N \binom{N}{k} - \sum_{s=1}^{N-1} \text{cnt}[s] \binom{s}{k}$ into a single `=` sign without showing the intermediate sum over $|E| = N - 1$ edges.
- **Drop-In Replacement (Line `527`)**:
  ```markdown
  $$
  \begin{aligned}
  \text{ans}_k
  &= \binom{N}{k} + \sum_{e=(u,v) \in E} \left[\binom{N}{k} - \binom{\text{sz}[v]}{k} - \binom{N - \text{sz}[v]}{k}\right] \\[4pt]
  &= \bigl(1 + (N - 1)\bigr)\binom{N}{k} - \sum_{e=(u,v) \in E} \left[\binom{\text{sz}[v]}{k} + \binom{N - \text{sz}[v]}{k}\right]
  && \text{(since } |E| = N - 1\text{)} \\[4pt]
  &= N \binom{N}{k} - \sum_{s=1}^{N-1} \text{cnt}[s] \binom{s}{k}.
  && \text{(group the } 2(N-1) \text{ component sizes into } \text{cnt}[s]\text{)}
  \end{aligned}
  $$
  ```

---

### Chapter 23 (`chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd`)

#### 23.1 `[Multi-Step Leap]` Line `629` — `#012` AtCoder AGC 054 D / Stepping Stone 2
- **File**: [ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L627-L631)
- **Issue**: Compresses expanding $\begin{bmatrix} r \\ j \end{bmatrix}_2 = \frac{(2; 2)_r}{(2; 2)_j (2; 2)_{r-j}}$ and factoring out $(2; 2)_r$ into a single `=` sign.
- **Drop-In Replacement (Line `629`)**:
  ```markdown
  $$
  f_{m, r}
  = \sum_{j=0}^r (-1)^{r-j} 2^{\binom{r-j}{2}} \begin{bmatrix} r \\ j \end{bmatrix}_2 (2^j)^{\underline{m}}
  = \sum_{j=0}^r (-1)^{r-j} 2^{\binom{r-j}{2}} \frac{(2; 2)_r}{(2; 2)_{r-j} (2; 2)_j} (2^j)^{\underline{m}}
  = (2; 2)_r \sum_{j=0}^r \frac{(-1)^{r-j} 2^{\binom{r-j}{2}}}{(2; 2)_{r-j}} \cdot \frac{(2^j)^{\underline{m}}}{(2; 2)_j}.
  $$
  ```

#### 23.2 `[Multi-Step Leap]` Line `925` — `#062` AtCoder ARC 139 F (Many Xor Optimization Problems)
- **File**: [ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L923-L927)
- **Issue**: Jumps from multiplying $\begin{bmatrix} m + 1 \\ j + 1 \end{bmatrix}_2 = \begin{bmatrix} m \\ j \end{bmatrix}_2 + 2^{j+1} \begin{bmatrix} m \\ j + 1 \end{bmatrix}_2$ by $x^m$ and summing over $m = j, \dots, M - 1$ directly to $\frac{1}{x}\bigl(T_{j+1} - \begin{bmatrix} M \\ j + 1 \end{bmatrix}_2 x^M\bigr) = T_j + 2^{j+1} T_{j+1}$ without showing the index shift $m' = m + 1$ on the LHS.
- **Drop-In Replacement (Lines `924–926`)**:
  ```markdown
     To compute $T_0, T_1, \dots, T_{\min(N, M-1)}$ in $O(M)$ total time, multiply the $q$-Pascal identity $\begin{bmatrix} m + 1 \\ j + 1 \end{bmatrix}_2 = \begin{bmatrix} m \\ j \end{bmatrix}_2 + 2^{j+1} \begin{bmatrix} m \\ j + 1 \end{bmatrix}_2$ by $x^m$ and sum over $m = j, \dots, M - 1$ (reindexing the LHS via $m' = m + 1 \in \{j + 1, \dots, M\}$):
     $$
     \begin{aligned}
     \frac{1}{x} \sum_{m'=j+1}^{M} \begin{bmatrix} m' \\ j + 1 \end{bmatrix}_2 x^{m'}
     &= \sum_{m=j}^{M-1} \begin{bmatrix} m \\ j \end{bmatrix}_2 x^m + 2^{j+1} \sum_{m=j+1}^{M-1} \begin{bmatrix} m \\ j + 1 \end{bmatrix}_2 x^m \\[4pt]
     \frac{1}{x}\left(T_{j+1} - \begin{bmatrix} M \\ j + 1 \end{bmatrix}_2 x^M\right) &= T_j + 2^{j+1} T_{j+1}
     \implies (1 - 2^{j+1} x) T_{j+1} = x T_j + \begin{bmatrix} M \\ j + 1 \end{bmatrix}_2 x^M.
     \end{aligned}
     $$
  ```

#### 23.3 `[Multi-Step Leap]` Line `1109` — `#063` AtCoder ARC 145 F (Modulo Sum of Increasing Sequences)
- **File**: [ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd#L1106-L1112)
- **Issue**: Compresses the derivation of $\beta_t - \beta_{t-1} = -(\alpha_t - \overline{\alpha})$ modulo $1 + x + \dots + x^{m-1}$ into a single prose sentence without displaying the $[x^t]$ extraction modulo $1 - x^m$.
- **Drop-In Replacement (Line `1109`)**:
  ```markdown
     - Equivalently, lifting $(1 - x) \sum_{t=0}^{m-1} \beta_t x^t \equiv \sum_{t=0}^{m-1} (\alpha_t - \overline{\alpha}) x^t \pmod{1 + x + \dots + x^{m-1}}$ to $\mathbb{F}_p[x]/(1 - x^m)$ (where $\overline{\alpha} = \frac{1}{m}\sum_{t=0}^{m-1} \alpha_t$ ensures the RHS vanishes at $x = 1$) and extracting $[x^t]$ gives
       $$[x^t]\left((1 - x)\sum_{u=0}^{m-1} \beta_u x^u \bmod (1 - x^m)\right) = \beta_t - \beta_{(t-1)\bmod m} = \alpha_t - \overline{\alpha} \implies \beta_t = \beta_{t-1} - (\alpha_t - \overline{\alpha}) \quad (1 \le t < m),$$
       which determines $(\beta_0, \dots, \beta_{m-1})$ up to an additive constant in a single $O(m)$ linear scan. Across all $g$ cosets, each division by $(1 - q^i)$ takes $O(d)$ time, so computing
  ```

---

### Chapter 24 (`chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd`)

#### 24.1 `[Multi-Step Leap]` Lines `484–495` — §24.4 Dirichlet $\ln_D, \exp_D, f^\alpha$ Divisor Recurrences
- **File**: [ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd#L482-L496)
- **Issue**: Jumps directly from the operator equations $\vartheta g *_D f = \vartheta f$, $\vartheta g = \vartheta f *_D g$, and $f *_D \vartheta g = \alpha \, \vartheta f *_D g$ to the final isolated recurrences for $g(n)$ without showing the intermediate divisor sum extraction at $n \ge 2$ and isolation of $d = n$ or $d = 1$.
- **Drop-In Replacement (Lines `484–495`)**:
  ```markdown
  1. **Dirichlet Logarithm** ($g = \ln_D f$, $f(1) = 1 \implies \vartheta g *_D f = \vartheta f$):
     Evaluating $(\vartheta g *_D f)(n) = (\vartheta f)(n)$ at $n \ge 2$ and isolating $d = n$ (since $\Omega(1) = 0$ kills $d = 1$):
     $$
     \sum_{d \mid n} \Omega(d) g(d) f\!\left(\frac{n}{d}\right) = \Omega(n) f(n)
     \implies \Omega(n) g(n) f(1) + \sum_{\substack{d \mid n \\ 1 < d < n}} \Omega(d) g(d) f\!\left(\frac{n}{d}\right) = \Omega(n) f(n)
     \implies g(n) = f(n) - \frac{1}{\Omega(n)} \sum_{\substack{d \mid n \\ 1 < d < n}} \Omega(d) \, g(d) \, f\!\left(\frac{n}{d}\right).
     $$
  2. **Dirichlet Exponential** ($g = \exp_D f$, $f(1) = 0 \implies \vartheta g = \vartheta f *_D g$):
     Evaluating $(\vartheta g)(n) = (\vartheta f *_D g)(n)$ at $n \ge 2$ (where $d = n$ vanishes because $\Omega(1) = 0$):
     $$
     \Omega(n) g(n) = \sum_{d \mid n} \Omega\!\left(\frac{n}{d}\right) f\!\left(\frac{n}{d}\right) g(d)
     \implies g(n) = \frac{1}{\Omega(n)} \sum_{\substack{d \mid n \\ d < n}} \Omega\!\left(\frac{n}{d}\right) f\!\left(\frac{n}{d}\right) g(d) \qquad (n \ge 2, \ g(1) = 1).
     $$
  3. **Dirichlet Power** ($g = f^\alpha$, $f(1) = 1 \implies f *_D \vartheta g = \alpha \, \vartheta f *_D g$):
     Evaluating $\sum_{d \mid n} f(n/d) \Omega(d) g(d) = \alpha \sum_{d \mid n} \Omega(n/d) f(n/d) g(d)$ at $n \ge 2$ and isolating $d = n$ on the LHS (where $f(1) = 1$ and $\Omega(1) = 0$):
     $$
     \Omega(n) g(n) + \sum_{\substack{d \mid n \\ d < n}} \Omega(d) f\!\left(\frac{n}{d}\right) g(d) = \alpha \sum_{\substack{d \mid n \\ d < n}} \Omega\!\left(\frac{n}{d}\right) f\!\left(\frac{n}{d}\right) g(d)
     \implies g(n) = \frac{1}{\Omega(n)} \sum_{\substack{d \mid n \\ d < n}} \left(\alpha \, \Omega\!\left(\frac{n}{d}\right) - \Omega(d)\right) f\!\left(\frac{n}{d}\right) g(d).
     $$
  ```

#### 24.2 `[Multi-Step Leap]` Line `1365` — `#038` AtCoder ABC 288 Ex (A Nameless Counting Problem)
- **File**: [ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd#L1362-L1370)
- **Issue**: Compresses $\prod_{v=0}^M \exp(x^v z) = \prod_{v=0}^M \big(\cosh(z) + x^v \sinh(z)\big)$ into a single `=` sign without showing the parity split of $\exp(x^v z)$ into even and odd powers of $z$.
- **Drop-In Replacement (Lines `1364–1369`)**:
  ```markdown
  $$
  \begin{aligned}
  \Psi(x, z)
  &= \sum_{j=0}^{\infty} \left(\sum_{v=0}^M x^v\right)^j \frac{z^j}{j!}
  = \prod_{v=0}^M \exp(x^v z) \\[4pt]
  &= \prod_{v=0}^M \left( \sum_{m=0}^{\infty} (x^v)^{2m} \frac{z^{2m}}{(2m)!} + \sum_{m=0}^{\infty} (x^v)^{2m+1} \frac{z^{2m+1}}{(2m+1)!} \right)
  && \text{(split } \exp(x^v z) \text{ into even and odd powers of } z\text{)} \\[4pt]
  &= \prod_{v=0}^M \big(\cosh(z) + x^v \sinh(z)\big),
  && \text{(use } (x^v)^{2m} = 1 \text{ and } (x^v)^{2m+1} = x^v \text{ in } \mathbb{F}_p[\mathbb{Z}_2^{30}]\text{)}
  \end{aligned}
  $$
  ```
