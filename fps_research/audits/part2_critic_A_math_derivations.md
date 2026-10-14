# Part II Audit Report — Critic A: Mathematical Rigor, Single-Step Derivations & Zero-Magic-Steps

- **Auditor**: FPS Textbook Critic & Mathematical Auditor (Part II Critic A)
- **Date**: 2026-10-14
- **Scope**:
  1. [`chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd) (1,759 lines)
  2. [`chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd) (1,302 lines)
  3. [`chapters/ch07-roots-of-unity-cyclotomic-czt.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd) (1,437 lines)
  4. [`chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd) (1,241 lines)
  5. [`checkpoints/cp02-part2-rational-transforms-ie.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd) (1,270 lines)
- **Reference Standards**: [`AGENTS.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/AGENTS.md), [`fps_research/CURRICULUM_ARCHITECTURE.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md)

---

## Executive Summary & Verdict Matrix

Across all 7,009 lines of Part II (`Ch 05`–`Ch 08` + `CP-II`), the mathematical exposition, reverse-engineering scratchpads, characteristic-$p$ boundary treatments, and 40 problem derivations are remarkably thorough and pedagogically clear. Every subsection (`5.1`–`5.5`, `6.1`–`6.4`, `7.1`–`7.4`, `8.1`–`8.4`), every Canonical Failure Mode assigned to Part II (`#1`, `#2`, `#4`, `#5`, `#6`, `#11`, `#12`, `#14`), and all 40 curated problems (`8` per chapter + `8` in `CP-II`) are present and accompanied by step-by-step derivations and hand-checkable numerical traces.

However, a line-by-line mathematical audit uncovered **2 Critical Mathematical/Notation Errors**, **6 Major Issues**, and **9 Minor Polish Items** that must be fixed to reach 100% publication-grade perfection:

| File | Total Lines | Critical Issues | Major Issues | Minor Issues | Overall Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| [`ch05-rational-bostan-mori-berlekamp-massey.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd) | 1,759 | **1** (`Mas-2` Hint 3 wrong formula + draft artifact) | **1** (6 instances of emphatic `!` inside `$$...$$` rendering as factorials) | **3** (Prereq box $K((x))$, Stirling forward-ref, Quarantine IDs) | Needs Targeted Fixes |
| [`ch06-binomial-snake-oil-taylor-shift-stirling.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd) | 1,302 | **1** (`§6.2` line 361 `= 0!` inside display math $= 0! = 1$, plus 8 other display-math `!`s) | **1** (`§6.2` line 344 wrong upper limit $\lfloor n/2 \rfloor$ + line 352 inequality typo) | **1** (`Int-2` `#080` KUPC 2019 K $B_j$ statement alignment) | Needs Targeted Fixes |
| [`ch07-roots-of-unity-cyclotomic-czt.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd) | 1,437 | **0** | **2** (Missing Revisited Cross-Ref `#6` `Luogu P4705` in `§7.3`; 1 display-math `!` on line 1272) | **3** (`Mas-1` prime search complexity $O(n\sqrt{P}) \to O(\sqrt{P}\log P)$, typo on line 522, Quarantine titles) | Needs Targeted Fixes |
| [`ch08-connected-component-ie-rook-goulden-jackson.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd) | 1,241 | **0** | **1** (`Mas-1` `#052` line 1107 off-by-one coefficient $(K-j) \to (K-j+1)$ in forward/backward DP) | **2** (`Adv-2` line 973 missing minus sign on $\mathbf{1}^\top$; spacing typo on line 254) | Needs Targeted Fixes |
| [`cp02-part2-rational-transforms-ie.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd) | 1,270 | **0** | **1** (Pre-Stage-1 Diagnostic Rubric & Mermaid diagram spoil all 8 problems + `CP-II.8` Hint 1 leaks `Ch 04`) | **2** (3 draft "wait" self-correction artifacts; section-number citation mismatches) | Needs Targeted Fixes |

---

## File 1: Chapter 05 — Rational Generating Functions, Bostan–Mori & Berlekamp–Massey
**File**: [`chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd)

### 1.1 Mathematical Accuracy & Index Boundary Verification

#### [CRITICAL-05-1] `Mas-2` (`#073` AtCoder AGC 054 E — ZigZag Break): Contradictory/Wrong Formula in Hint 3 vs. Complete Derivation, plus Unedited Draft Self-Correction Artifact
- **Location**: [Lines 1621–1623](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1621-L1623) (Hint 3) vs. [Lines 1655–1669](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1655-L1669) (Complete Derivation).
- **What is wrong**:
  1. In **Hint 3** ([lines 1621–1623](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1621-L1623)), the text claims:
     > "Every $S$ must be placed immediately before an $M$, so out of the $m + s$ elements of $S \cup M$, the $m$ elements of $M$ act as dividers and no $S$ can follow $L$. Wait—actually, in a sequence with no `SL` and no `MS`, all $S$'s must appear in a single block, or rather: in the relative order of $S, M, L$, no $S$ can be followed by $L$ and no $M$ can be followed by $S$! This collapses the count of valid $(S, M, L)$ arrangements to a single binomial coefficient:
     > $$\text{Bad}(A, B) = (A - 1)! (N - B)! (B - A - 1) \binom{N - 2 - (B - A)}{A - 1}$$"
  2. Then, in the **Complete Derivation** ([lines 1655–1656](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1655-L1656)), the author realized mid-draft that an $S$ *can* follow an $L$ (`LSM` has no `SL` and no `MS`!), leaving the raw self-correction note in the text:
     > `3. **Wait—let us check the product**:`
     > `Wait: in the skeleton of $m$ copies of $M$ and $l$ copies of $L$, can an $S$ be placed after an $L$ and before an $M$? Yes, LSM has no SL!`
     And on [lines 1667–1669](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1667-L1669), the Complete Derivation derives the **correct** formula:
     $$\text{Bad}(A, B) = (B - A - 1)(N - A - 2)!(B - 3)! = (A - 1)!(N - A - 2)!(B - A - 1)\binom{B - 3}{A - 1}.$$
  3. **Concrete Counterexample**: Take $N = 6, A = 2, B = 5$, so $s = A - 1 = 1$, $l = N - B = 1$, $m = B - A - 1 = 2$.
     - The true formula on line 1668 gives $(5 - 2 - 1)(6 - 2 - 2)!(5 - 3)! = 2 \cdot 2! \cdot 2! = 8$.
     - The wrong formula in Hint 3 (line 1622) gives $1! \cdot 1! \cdot 2 \cdot \binom{6 - 2 - 3}{1} = 2 \cdot \binom{1}{1} = 2 \neq 8$.
- **Exact Fix**:
  1. In **Hint 3** ([lines 1621–1623](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1621-L1623)), replace the erroneous explanation and formula with:
     ```markdown
     Every $S$ must be followed by an $S$ or an $M$ (since $S$ cannot be at the end and `SL` is forbidden), and no $M$ can be followed by an $S$ (`MS` is forbidden). Thus each maximal contiguous block of $S$'s is immediately preceded by `A` or an `L` (and never by an `M`) and immediately followed by an `M`, which means every $S$ must occur strictly before the last $M$. By stars-and-bars + Vandermonde convolution, this collapses the count of valid $(S, M, L)$ arrangements to a single factorial product:
     $$\text{Bad}(A, B) = (B - A - 1)(N - A - 2)!(B - 3)! = (A - 1)!(N - A - 2)!(B - A - 1)\binom{B - 3}{A - 1}$$
     ```
  2. In the **Complete Derivation** ([lines 1647–1661](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1647-L1661)), remove the false start in step 2 (lines 1650–1654) and the conversational `"Wait—let us check the product: Wait:"` header on lines 1655–1656, presenting the stars-and-bars + Vandermonde derivation on lines 1657–1669 directly as Step 2.

---

#### [MAJOR-05-1] 6 Instances of Emphatic Exclamation Marks (`!`) Inside `$$...$$` Display Math Blocks Rendering as Factorials
In LaTeX/MathJax, placing an exclamation mark `!` at the end of a `$$...$$` display math block typesets a **factorial operator** on the final mathematical symbol:
1. **[Line 260 (`§5.2`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L260)**:
   - Current: `[x^0] Q^{\text{rev}}(x) = [x^m] Q(x) = b_m \in K^\times!` (renders as $b_m \in K^\times!$, factorial of the unit group $K^\times$).
   - Fix: Replace `!` with `.`.
2. **[Line 500 (`§5.4`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L500)**:
   - Current: `Q(x) Q(-x) = Q(x)^2 = \left(\sum_{j=0}^d q_j x^j\right)^p = \sum_{j=0}^d q_j^p x^{pj} = Q(x^p) \pmod p!` (renders as $\pmod{p!}$, modulo $p$ factorial!).
   - Fix: Replace `\pmod p!` with `\pmod p.`.
3. **[Line 665 (`§5.5`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L665)**:
   - Current: `\det(I - xA) = \exp\Big(\operatorname{tr} \ln(I - xA)\Big) = \exp\!\left(-\sum_{k=1}^\infty \frac{\operatorname{tr}(A^k)}{k} x^k\right) \quad \text{in } K[[x]]!` (renders as $K[[x]]!$).
   - Fix: Replace `!` with `.`.
4. **[Line 1169 (`Int-2` `#069`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1169)**:
   - Current: `Q_2(x) = (1 - x)^3 - x(1 + x) = 1 - 4x + 2x^2 - x^3!` (renders as $- x^3!$, reading as $-(x^3)!$).
   - Fix: Replace `!` with `.`.
5. **[Line 1308 (`Adv-1` `#036`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1308)**:
   - Current: `S(P, Q, N) = [x^0] P(x) + S\big(U_0(y) + U_1(y), V(y), (N - 1) / 2\big)!` (renders as factorial of the recursive call $S(\dots)!$).
   - Fix: Replace `!` with `.`.
6. **[Line 1484 (`Mas-1` `#177`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1484)**:
   - Current: `\binom{\ell}{j} = \frac{1}{j!} \sum_{i=0}^j (-1)^{j-i} \left[\begin{matrix} j \\ i \end{matrix}\right] \binom{j}{i} A^i B^{j-i} \sum_{n=L}^R \big(\alpha^i \beta^{j-i}\big)^n!` (renders as $(\alpha^i \beta^{j-i})^{n!}$, i.e., $n$-factorial in the exponent!).
   - Fix: Replace `!` with `.`.

---

### 1.2 Prerequisite Closure & Zero Forward-Reference Audit

#### [MINOR-05-1] Prerequisite Callout Box Lists $K((x))$ (`Ch 11`) Instead of $K[x, x^{-1}]$ and Omits `Ch 02`
- **Location**: [Lines 8–12](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L8-L12).
- **Issue**: Line 10 lists `formal Laurent series $K((x))$` under **Chapter 01**, whereas the field of formal Laurent series $K((x))$ is formally introduced in **Chapter 11** (`§5.2` on line 233 only uses Laurent polynomials $K[x, x^{-1}]$). Meanwhile, `§5.3` (Repeated Root Theorem 5.2) and `§5.4` (Odd-Characteristic Bostan–Mori) use the formal derivative $D_x$ and Frobenius endomorphism from **Chapter 02**, which is omitted from the Prerequisites list.
- **Exact Fix**: Change `formal Laurent series $K((x))$` on line 10 to `Laurent polynomials $K[x, x^{-1}]$`, and add a bullet for **Chapter 02**: `Formal differentiation $D_x$, logarithmic derivative $Q'/Q$, and the Frobenius endomorphism $(A+B)^p \equiv A^p + B^p \pmod p$.`

#### [MINOR-05-2] Unflagged Forward Reference to Stirling Numbers of the First Kind (`Ch 06, §6.4`) in `Mas-1` (`#177` BJOI 2019 勘破神机) and Eulerian Polynomials in `Int-2` (`#069`) / MTT in `SS-1` (`#104`)
- **Location**: [Lines 820](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L820), [1174](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1174), and [1469, 1510–1518](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1510-L1518).
- **Issue**:
  - `Mas-1` (`#177`, lines 1469 & 1510–1518) expands $x^{\underline{k}} = \sum_{i=0}^k (-1)^{k-i} \left[\begin{smallmatrix} k \\ i \end{smallmatrix}\right] x^i$ using unsigned Stirling numbers of the first kind one chapter before `Ch 06 (§6.4)` defines them. (Since $k \le 501$, defining the coefficients inductively via $x^{\underline{j}} = x^{\underline{j-1}}(x - (j - 1)) \implies s(j, i) = s(j-1, i-1) + (j-1)s(j-1, i)$ makes the solution 100% self-contained within `Ch 05`!)
  - Line 820 mentions 3-prime NTT / MTT without a forward pointer to `Chapter 07, §7.2`, and line 1174 mentions Eulerian polynomials $A_K(x)$ without a forward pointer to `Chapter 06, §6.4`.
- **Exact Fix**: Add a 1-sentence inductive definition of the falling-factorial expansion coefficients $\left[\begin{smallmatrix} j \\ i \end{smallmatrix}\right]$ on line 1511 along with `(studied systematically in Chapter 06, §6.4)`, and add explicit forward pointers on lines 820 and 1174.

#### [MINOR-05-3] Quarantined Library Verification Footnotes (`§5.6`) Missing Explicit Quarantine IDs (`R-05`, `R-39`, `R-40`, `R-41`)
- **Location**: [Lines 1749–1758](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd#L1749-L1758).
- **Issue**: `CURRICULUM_ARCHITECTURE.md` §6.1 assigns four quarantined template IDs to Chapter 05: `R-05` (Luogu P4512 — Polynomial Division), `R-39` (Luogu P4723 — Linear Recurrence), `R-40` (Luogu P5487 — Berlekamp–Massey), and `R-41` (Luogu P7439 — Bostan–Mori). Currently lines 1749–1758 list Library Checker links and Luogu P4723/P5487 without tagging `R-05`, `R-39`, `R-40`, `R-41` or mentioning Luogu P4512 and Luogu P7439.
- **Exact Fix**: Add the explicit tags `R-05` (`Luogu P4512`), `R-39` (`Luogu P4723`), `R-40` (`Luogu P5487`), and `R-41` (`Luogu P7439`) to the bullet list in `§5.6`.

---

## File 2: Chapter 06 — Binomial Sums, Snake Oil, Taylor Shift & Stirling Numbers
**File**: [`chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd)

### 2.1 Mathematical Accuracy & Index Boundary Verification

#### [CRITICAL-06-1] `= 0!` Inside Display Math Rendering as Zero Factorial ($0! = 1$) in `§6.2` Worked Derivation 4, Plus 8 Additional Display-Math `!` Punctuation Bugs
- **Location**: [Line 361 (`§6.2`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L361), plus lines [328](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L328), [494](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L494), [623](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L623), [678](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L678), [940](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L940), [942](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L942), [1013](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L1013), [1218](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L1218).
- **What is wrong**:
  1. On **[line 361](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L361)**, Worked Derivation 4 concludes its proof that the alternating binomial sum vanishes for all $n \ge 1$ by writing:
     ```latex
     &= [u^{n-1}] \big(u^2 + 2u\big)^n = [u^{n-1}] u^n (2 + u)^n = 0! && \text{(since }\operatorname{val}(u^n(2+u)^n) = n > n - 1\text{)}
     ```
     In math mode, `= 0!` is the notation for **zero factorial** ($0! = 1$), directly contradicting the theorem result ($= 0$)!
  2. Similarly, on **[line 494](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L494)**, `= \frac{\alpha^{\overline{n}}}{\alpha^{\overline{k}} \cdot (n - k)!}!` places a second `!` right after the fraction containing $(n-k)!$.
  3. The other 7 instances of emphatic `!` inside `$$...$$` display math in Chapter 06 also render as unintended factorials:
     - **[Line 328](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L328)**: `... = [u^n] \Big((1 + u)^n \cdot (1 + u)^k\Big)!`
     - **[Line 623](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L623)**: `... = \sum_{j=0}^{\min(n, m)} c_j n^{\underline{j}} a^j (a + b)^{n - j}!` (renders as $(a+b)^{(n-j)!}$)
     - **[Line 678](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L678)**: `... = (1 - x)^{n+1} \sum_{m=0}^{n-1} (m + 1)^n x^m \pmod{x^n}!`
     - **[Line 940](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L940)**: `... = \binom{d}{i} (1 + y)^{d - i} (1 - y)^i!` (renders as $(1-y)^{i!}$)
     - **[Line 942](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L942)**: `... = \binom{d}{i} [y^k] \big((1 + y)^{d - i} (1 - y)^i\big)!`
     - **[Line 1013](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L1013)**: `... = \frac{1}{k + 1} (x - 1)^k!` (renders as $(x-1)^{k!}$)
     - **[Line 1218](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L1218)**: `... = n^{\underline{j}} p^j!` (renders as $p^{j!}$)
- **Exact Fix**: Remove the trailing `!` (or replace with `.`) in all 9 display math blocks on lines 328, 361, 494, 623, 678, 940, 942, 1013, and 1218.

---

#### [MAJOR-06-1] Wrong Upper Summation Index $\lfloor n/2 \rfloor$ in Heading of Worked Derivation 4 (`§6.2`) and Index Inequality Typo in Scratchpad
- **Location**: [Lines 344 and 352 (`§6.2`)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L344-L352).
- **What is wrong**:
  1. On **[line 344](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L344)**, the heading states:
     `#### Worked Derivation 4 (Scaled-Variable Egorychev Extraction): $\sum_{k=0}^{\lfloor n/2 \rfloor} (-1)^k \binom{n}{k} \binom{2n - 2k}{n - 1}$`
     whereas line 346 states the sum up to $n$: $\sum_{k=0}^n (-1)^k \binom{n}{k} \binom{2n - 2k}{n - 1} = 0$.
     Notice that $\binom{2n - 2k}{n - 1} \neq 0$ whenever $2n - 2k \ge n - 1 \iff 2k \le n + 1 \iff k \le \lfloor \frac{n + 1}{2} \rfloor$.
     For **odd $n$** (for example $n = 3$), $\lfloor n/2 \rfloor = 1$ omits the $k = \frac{n+1}{2} = 2$ term $(-1)^2 \binom{3}{2}\binom{2}{2} = +3$, so $\sum_{k=0}^{\lfloor 3/2 \rfloor} (-1)^k \binom{3}{k}\binom{6-2k}{2} = \binom{6}{2} - 3\binom{4}{2} = 15 - 18 = -3 \neq 0$!
  2. On **[line 352](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L352)**, the scratchpad asks:
     `Wait: what if $k > \lfloor \frac{n+1}{2} \rfloor$ so that $2n - 2k < 0$?`
     For $0 \le k \le n$, $2n - 2k = 2(n - k) \ge 0$ is **never** negative! Rather, when $k > \lfloor \frac{n+1}{2} \rfloor$, we have $0 \le 2n - 2k < n - 1$, which is why $\binom{2n - 2k}{n - 1} = 0$ and $[u^{n-1}](1 + u)^{2n - 2k} = 0$ (since $\deg (1+u)^{2n-2k} = 2n - 2k < n - 1$).
- **Exact Fix**:
  1. On line 344, change `\sum_{k=0}^{\lfloor n/2 \rfloor}` to `\sum_{k=0}^{n}` (or `\sum_{k=0}^{\lfloor (n+1)/2 \rfloor}`).
  2. On line 352, replace `so that $2n - 2k < 0$? Note that for $0 \le k \le n$, $2n - 2k \ge 0$ always holds! Even if the upper index were $2n - 2k < n - 1$, the polynomial $(1 + u)^{2n - 2k}$ has degree $2n - 2k < n - 1$, so $[u^{n-1}](1 + u)^{2n - 2k} = 0 = \binom{2n - 2k}{n - 1}$ automatically!` with: `so that $0 \le 2n - 2k < n - 1$? Then the polynomial $(1 + u)^{2n - 2k}$ has degree $2n - 2k < n - 1$, so $[u^{n-1}](1 + u)^{2n - 2k} = 0 = \binom{2n - 2k}{n - 1}$ holds automatically for all $0 \le k \le n$!`

---

### 2.2 8-Problem Ladder Completeness Audit

#### [MINOR-06-1] `Int-2` (`#080` KUPC 2019 K — One-Dimensional cellular automaton): Unused $B_j$ Array in Problem Statement
- **Location**: [Lines 917–920 and 980](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L917-L920).
- **Issue**: Line 917 introduces two sequences $A_1, \dots, A_N$ and $B_1, \dots, B_N$ in the problem statement, but lines 918–979 only define and compute $S_j = \sum_{i=1}^N A_i (X_i + Y_i)^j$ for $1 \le j \le N$, mentioning $B_j$ only in a parenthetical note at the very end of the derivation (line 980).
- **Exact Fix**: In the problem statement ([lines 917–920](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd#L917-L920)), state clearly that the core algebraic task of KUPC 2019 K is to evaluate the sequence of weighted signed binomial sums $S_k$ for all $0 \le k \le d$ (and once all $S_k$ are computed in $O(d \log d)$ time via the Bruhat Taylor-shift pipeline, they can be combined with $B_k$ in $O(d)$ time).

---

## File 3: Chapter 07 — Roots of Unity, Multiplicative Indexing & Chirp-$Z$ Transform
**File**: [`chapters/ch07-roots-of-unity-cyclotomic-czt.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd)

### 3.1 Sub-Section, Failure Mode & Revisited Dual-Perspective Completeness

#### [MAJOR-07-1] Missing Mandatory Revisited Dual-Perspective Cross-Reference `#6` (`#154` Luogu P4705 — 玩游戏) in `§7.3`
- **Location**: [`§7.3` (Lines 252–406)](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd#L252-L406).
- **Requirement in `CURRICULUM_ARCHITECTURE.md` §5.2 (Entry `#6`)**:
  - **Problem**: `#154` Luogu P4705 — 玩游戏
  - **Primary Home**: `Ch 04 Mas-2` (EGF Power Sums & Log-Derivative $\sum a_i^k$)
  - **Revisited Cross-Reference**: `Ch 07 (§7.3)` — *"When power sums meet geometric evaluation points $c^{ij}$, connects Newton's power sums to Bluestein's CZT."*
- **Issue**: Currently `§7.3` does not mention `#154` (`Luogu P4705 — 玩游戏`) or contrast `Ch 04 Mas-2`'s additive power-sum decoupling with `§7.3`'s multiplicative geometric evaluation decoupling.
- **Exact Fix**: Insert a `.callout-note` box at the end of `§7.3` (right after line 405, before `## 7.4`):
  ```markdown
  ::: {.callout-note}
  ### Revisited Dual-Perspective Cross-Reference: Additive Power Sums (`Ch 04 Mas-2`, `#154` Luogu P4705) vs. Multiplicative Geometric Evaluations (`§7.3` Bluestein CZT)
  Compare the bilinear sum in **Chapter 04 (`Mas-2`, `#154` Luogu P4705 — 玩游戏)** with Bluestein's Chirp-$Z$ Transform in this section:
  - **Additive Base + Fixed Exponent (`Ch 04 Mas-2`, Luogu P4705)**: To evaluate $\sum_{i=1}^n \sum_{j=1}^m (a_i + b_j)^k$ for $1 \le k \le t$, the coupling is **additive inside the base**. Expanding $(a_i + b_j)^k = k! \sum_{r=0}^k \frac{a_i^r}{r!} \frac{b_j^{k-r}}{(k-r)!}$ in the EGF ring reduces the problem to computing power sums $P_r(A) = \sum_{i=1}^n a_i^r = [x^r]\Big(n - x \frac{d}{dx}\ln \prod_{i=1}^n (1 - a_i x)\Big)$ via Newton's logarithmic derivative (`Ch 04`), followed by a single 1D EGF convolution.
  - **Multiplicative Exponent + Geometric Base (`Ch 07 §7.3`, Bluestein CZT)**: When the coupling moves into the **exponent** as $\sum_{j=0}^{n-1} f_j a^j c^{ij}$ (or $\sum_{i, j} a_i b_j c^{i^2 j^3}$ in `Int-2 #100`), the binomial theorem on the base no longer applies. Instead, Bluestein's identity $ij = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$ acts as the **exponent-space analogue of EGF binomial decoupling**, factoring the coupled weight $c^{ij}$ into $c^{\binom{i+j}{2}} \cdot c^{-\binom{i}{2}} \cdot c^{-\binom{j}{2}}$ and reducing multipoint geometric evaluation to a single 1D Cauchy convolution!
  :::
  ```

---

#### [MAJOR-07-2] Emphatic `!` Inside `$$...$$` Display Math on Line 1272 (`Mas-1` `#092` CF 901E)
- **Location**: [Line 1272](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd#L1272).
- **What is wrong**:
  - Current: `\delta_i := a_i - a_0 \in \mathbb{Z} \qquad (0 \le i < n)!` (renders as $(0 \le i < n)!$, a factorial sign after the parenthetical range).
- **Exact Fix**: Replace `!` with `.` on line 1272.

---

### 3.2 Complexity & Editorial Polish in Chapter 07

#### [MINOR-07-1] Inaccurate Complexity Bound $O(n \sqrt{P})$ for Finding a Prime $P \equiv 1 \pmod n$ in `Mas-1` (`#092` CF 901E)
- **Location**: [Line 1289](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd#L1289).
- **Issue**: Line 1289 states: `Finding $P \equiv 1 \pmod n$ takes $O(n \sqrt{P})$ or $O(\text{polylog } P)$ time`. Because we step through candidates $P = m \cdot n + 1$ for $m = \lceil 2 \times 10^9 / n \rceil, \dots$ in arithmetic progression of step $n$, by the Prime Number Theorem in arithmetic progressions (Linnik/Dirichlet) we test only $O(\log P)$ candidates $m$, each in $O(\sqrt{P})$ trial-division time, for a total of **$O(\sqrt{P} \log P)$** time (not $O(n \sqrt{P})$, which for $n = 10^5, P = 2 \times 10^9$ would be $4.5 \times 10^9$ operations!).
- **Exact Fix**: Change `$O(n \sqrt{P})$` on line 1289 to `$O(\sqrt{P} \log P)$`.

#### [MINOR-07-2] Double-Verb Typo on Line 522
- **Location**: [Line 522](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd#L522).
- **Issue**: `or the modulus $M$ is isn't even prime` has a duplicated verb (`is isn't`).
- **Exact Fix**: Change `is isn't` to `isn't`.

#### [MINOR-07-3] Include Explicit Luogu Problem IDs Alongside Quarantine Tags in `§7.6`
- **Location**: [Lines 1434–1435](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch07-roots-of-unity-cyclotomic-czt.qmd#L1434-L1435).
- **Issue**: Lines 1434–1435 list `R-02, R-19, R-27, R-31, R-45, R-64` by code only, without naming the corresponding Luogu verification problems from `CURRICULUM_ARCHITECTURE.md` §6.1.
- **Exact Fix**: Expand the references on lines 1434–1435 to name `R-02` (`Luogu P4245` Arbitrary-Mod NTT), `R-19` (`Luogu P5282` Fast Factorial), `R-27` (`Luogu P6800` Chirp-$Z$ Transform), `R-31` (`Luogu P5050` Multipoint Evaluation), `R-45` (`Luogu P5273` Arbitrary-Mod Polynomial Power), and `R-64` (`Luogu P4191` Primitive Root / Bluestein DFT).

---

## File 4: Chapter 08 — Sieve Methods, Connected-Component IE, Rook Polynomials & Goulden–Jackson
**File**: [`chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd)

### 4.1 Mathematical Accuracy & Index Boundary Verification

#### [MAJOR-08-1] `Mas-1` (`#052` AtCoder ARC 100 F — Colorful Sequences): Off-by-One Coefficient $(K - j)$ Instead of $(K - j + 1)$ in Case 2 Forward/Backward Automaton Transition
- **Location**: [Lines 1107–1108](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd#L1107-L1108) (compare with the correct transition on [Line 1092](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd#L1092)).
- **What is wrong**:
  - On **[line 1092](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd#L1092)**, the Rainbow-Avoidance Automaton transition into state $j \in \{1, \dots, K-1\}$ is correctly derived as:
    $$dp_{\text{next}}[j] = (K - j + 1) \cdot dp[j - 1] + \sum_{t=j}^{K-1} dp[t] \qquad (1 \le j \le K - 1),$$
    because from state $j - 1$ (a suffix of $j - 1$ distinct elements), there are $K - (j - 1) = K - j + 1$ characters in $\{1, \dots, K\}$ that are distinct from all $j - 1$ elements in the suffix and therefore advance the state from $j - 1$ to $j$.
  - However, on **[line 1107](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd#L1107)** (inside Case 2 of the Complete Derivation), the transition is written with $(K - j)$ instead of $(K - j + 1)$:
    > `set $dp_{\text{right}}[0][q] = 1$ (and $0$ for $j \neq q$), and run the exact automaton transition $dp_{\text{next}}[j] = (K - j) dp[j - 1] + \sum_{t=j}^{K-1} dp[t]$ for $r = 0, \dots, N - M$.`
  - **Concrete Verification ($K = 3, A = (1, 1), q = 1, r = 1$)**:
    Appending $1$ character $c \in \{1, 2, 3\}$ after $A = (1, 1)$ gives $(1, 1, 1)$ (state $j = 1$, $1$ way) and $(1, 1, 2), (1, 1, 3)$ (state $j = 2$, $2$ ways), totaling $3$ non-colorful extensions.
    - Using $(K - j + 1) dp[j - 1] + \sum_{t=j}^{K-1} dp[t]$ gives $dp_{\text{right}}[1][1] = 1$ and $dp_{\text{right}}[1][2] = (3 - 2 + 1) \cdot 1 = 2$, sum $1 + 2 = 3$ (Correct).
    - Using $(K - j) dp[j - 1] + \sum_{t=j}^{K-1} dp[t]$ gives $dp_{\text{right}}[1][2] = (3 - 2) \cdot 1 = 1$, sum $1 + 1 = 2 \neq 3$ (Wrong).
- **Exact Fix**:
  1. On **[line 1107](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd#L1107)**, change `dp_{\text{next}}[j] = (K - j) dp[j - 1] + \sum_{t=j}^{K-1} dp[t]` to `dp_{\text{next}}[j] = (K - j + 1) dp[j - 1] + \sum_{t=j}^{K-1} dp[t]`.
  2. On **[line 1108](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd#L1108)**, add a 1-sentence justification for why the prefix DP `dp_left` uses the exact same transition: *because reversing the string $S^{\text{rev}}$ preserves rainbow windows of length $K$, prepending characters to the left of $A$ is isomorphic to appending characters to the right of $A^{\text{rev}}$ starting from its longest distinct suffix of length $p$.*

---

### 4.2 Minor Notation & Editorial Fixes in Chapter 08

#### [MINOR-08-1] Missing Minus Sign on $\mathbf{1}^\top$ in Inline Bordered Matrix on Line 973 (`Adv-2` `#139`)
- **Location**: [Line 973 vs. Line 974](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd#L973-L974).
- **Issue**: Line 974 (and line 1185 in `Mas-2`) correctly writes the $(m+1)\times(m+1)$ bordered matrix as $\begin{pmatrix} C(x)^\top & \mathbf{w}(x) \\ -\mathbf{1}^\top & 1 - \alpha x \end{pmatrix}$ so that its Schur complement is $(1 - \alpha x) - (-\mathbf{1}^\top)(C(x)^\top)^{-1}\mathbf{w}(x) = 1 - \alpha x + \mathbf{1}^\top (C(x)^\top)^{-1}\mathbf{w}(x)$. However, the inline matrix on line 973 omits the minus sign (`\begin{pmatrix} C(x)^\top & \mathbf{w}(x) \\ \mathbf{1}^\top & 1 - \alpha x \end{pmatrix}`).
- **Exact Fix**: Change `\mathbf{1}^\top` to `-\mathbf{1}^\top` in the inline matrix on line 973.

#### [MINOR-08-2] Missing Space in `**ProblemInt-2 (`#089` CF 840C)**` on Line 254
- **Location**: [Line 254](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd#L254).
- **Exact Fix**: Change `**ProblemInt-2 (`#089` CF 840C)**` to `**Problem Int-2 (`#089` CF 840C)**`.

---

## File 5: Blind Checkpoint II — Part II Diagnostic Arena (`CP-II`)
**File**: [`checkpoints/cp02-part2-rational-transforms-ie.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd)

### 5.1 100% Spoiler-Free Stage 1 Audit (`CURRICULUM_ARCHITECTURE.md` §3.1)

#### [MAJOR-09-1] Visible Pre-Stage-1 "3-Axis Part II Diagnostic Rubric" & Mermaid Flowchart Spoil All 8 Problems and Target Chapters Before Stage 1, and `CP-II.8` Hint 1 Leaks `Chapter 04`
- **Location**: [Lines 7, 29–90](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L29-L90), and [Line 1147 (`CP-II.8` Hint 1)](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L1147).
- **Requirement**: Audit Dimension 5 & `CURRICULUM_ARCHITECTURE.md` §3.1 mandate **100% Spoiler-Free Stage 1**: the visible problem arena and `Hint 1` must NOT reveal the target chapter number or specific technique name before the student attempts cold diagnostic routing.
- **What is wrong**:
  1. Right *above* `## Stage 1: Spoiler-Free Blind Problem Set (CP-II.1 to CP-II.8)`, lines 29–90 display a completely uncollapsed section (`## The 3-Axis Part II Diagnostic Rubric (No Spoilers)`) whose table (lines 54–60), bullet points (lines 37–49, 66–69), and Mermaid flowchart (lines 71–89) explicitly list the **exact input constraints, exact summands/strings (`\binom{j}{k}(-1)^{j-k}k^i`, `\sum_k \binom{x}{k-L}\binom{y}{k-R}`, `c^{f(i)g(j)} \pmod P`, `0 \le x_i \le f_i`, `'RG'`, `A_i > B_{\pi(i)}`, `d_1 \dots d_n`), exact reductions (`Vandermonde Convolution`, `Bluestein CZT`, `Prüfer Bijection`, `Ferrers Board Rook DP`, `O(K) Lagrange Interpolation`), and target chapters (`(Ch 04 / Ch 06)`, `(Ch 06)`, `(Ch 07)`, `(Ch 08)`)** for all 8 problems in `CP-II`!
  2. In `CP-II.8` (`#141` Luogu P2290), **Hint 1** ([line 1147](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L1147)) explicitly says:
     > `there is one canonical bijection from **Part I (Chapter 04)** that turns the graph-theoretic tree structure into a flat sequence of length $n - 2$.`
     Revealing `Part I (Chapter 04)` belongs in `Hint 2` (where it is already stated on line 1154), not `Hint 1`.
- **Exact Fix**:
  1. Wrap the specific technique/chapter-routing table and Mermaid flowchart in `## The 3-Axis Part II Diagnostic Rubric` inside a collapsible `<details><summary>Open the 3-Axis Part II Diagnostic Decision Tree (Consult After Cold Read or in Stage 2)</summary>...</details>` block (or move them into `## Stage 2` at the bottom of the file), keeping only general non-spoiler questions visible above Stage 1.
  2. On **[line 1147 (`CP-II.8` Hint 1)](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L1147)**, change `there is one canonical bijection from **Part I (Chapter 04)** that turns` to `there is one canonical bijection from Part I that turns`.

---

### 5.2 Editorial Polish & Section-Number Alignment in `CP-II`

#### [MINOR-09-1] 3 Conversational Draft Self-Correction Artifacts (`"wait..."`) in `CP-II.1`, `CP-II.3`, and `CP-II.6`
1. **[Line 152 (`CP-II.1`, Hint 3)](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L152)**:
   - Current: `*(Note: Because $n - 1 < P$, this direct falling-factorial formula is valid modulo $P$ even when $m + n - 1$ crosses multiples of $P$, wait—is that always true, or should you check Lucas's Theorem? Be careful! Actually, over $\mathbb{Z}$, $\binom{M}{k} = \frac{M(M-1)\cdots(M-k+1)}{k!}$ is an exact integer equality, and since $\gcd(k!, P) = 1$ for $k = n - 1 < P$, reducing the numerator and denominator modulo $P$ in the ring $\mathbb{Z}_{(P)}$ of rationals with denominator coprime to $P$ is 100% exact for all $M \ge 0$!)*`
   - Fix: Remove `wait—is that always true, or should you check Lucas's Theorem? Be careful! Actually, ` so the note reads cleanly as an authoritative mathematical remark.
2. **[Lines 516–517 (`CP-II.3`, Concrete Trace)](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L516-L517)**:
   - Current:
     ```markdown
     1. `((()` $\to$ beauty $1$ (`()`)
     2. `((()` wait: positions $1$ and $3$ are `?`, position $2$ is `(`, position $4$ is `)`.
     ```
     followed by the clean 4-bullet list on lines 518–521.
   - Fix: Delete lines 516–517 so the 4 completions are listed cleanly once on lines 518–521.
3. **[Lines 949–950 (`CP-II.6`, Concrete Trace)](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L949-L950)**:
   - Current: `- Valid strings (7 total): RGBR, RGRB, RRGB, BRGR, RBRG, BRRG... wait let's list all 7: Contract RG -> X, leaving tokens {X, R, B} (3! = 6 ways: XRB, XBR, RXB, BX R, RBX, BRX). Wait: does RXB (RRGB) have 1 RG? Yes! ... So there are **6** valid strings (RGBR, RGRB, RRGB, BRGR, RBRG, BRRG).`
   - Fix: Replace lines 949–950 with the clean statement: `- Valid strings (6 total): Contracting the single G and its preceding R into X leaves the 3 distinct tokens {X, R, B}, giving 3! = 6 valid strings: RGBR (XRB), RBRG (XBR), RRGB (RXB), BRGR (BXR), RGRB (RBX), and BRRG (BRX).`

#### [MINOR-09-2] Section-Number Citation Mismatches Between `CP-II` and Chapters 06–08
- **Locations**: [Lines 7, 14](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L7-L14), [Line 580](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L580), [Line 1011](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L1011), [Lines 1263 & 1266](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp02-part2-rational-transforms-ie.qmd#L1263-L1266).
- **Issues & Exact Fixes**:
  1. **Lines 7 & 14**: Update the summary of Chapter 06 and Chapter 07 so that **Taylor Shift** is listed under **Chapter 06 (`§6.3`)** and **Chapter 07** is titled *Roots of Unity, Multiplicative Indexing, 3-Prime NTT & Bluestein's Chirp-$Z$ Transform (CZT)* (matching `ch07-roots-of-unity-cyclotomic-czt.qmd`).
  2. **Lines 580 & 1263 (`CP-II.4` CF 622F)**: Change `Chapter 07 (§7.4 Multiplicative Linear Sieve for i^k)` to `Chapter 06 (§6.4 Faulhaber's Power Sums, Multiplicative Euler Sieve for i^k & O(k) Consecutive Lagrange Interpolation)`, since `§7.4` of Chapter 07 is *Root-of-Unity Filter & Cyclotomic Polynomial Reduction* and the $O(d)$ Euler sieve for $i^k$ is taught directly in `Chapter 06, §6.4`.
  3. **Lines 1011 & 1266 (`CP-II.7` Luogu P4859)**: Change `Chapter 08 (§8.1 Binomial Inversion & §8.2 Rook Polynomials on Ferrers Boards)` to `Chapter 08 (§8.1 Binomial Inversion & Rook Polynomials on Ferrers Boards)`, since Rook Polynomials are in `§8.1` (`§8.2` is Connected-Component IE & Universal Run-Length Transfer).
