# Part I Audit Report — Critic A: Mathematical Rigor, Single-Step Derivations & Zero-Magic-Steps Audit

- **Auditor**: FPS Textbook Critic & Mathematical Auditor (Part I Critic A)
- **Scope**:
  1. [`chapters/ch01-ring-convolutions-newton-inv.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd) (1,157 lines)
  2. [`chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd) (1,255 lines)
  3. [`chapters/ch03-mset-partitions-euler-polya.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd) (1,526 lines)
  4. [`chapters/ch04-egf-set-cyc-boxed-prufer.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd) (1,027 lines)
  5. [`checkpoints/cp01-part1-foundations.qmd`](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd) (1,037 lines)
- **Cross-Examined Reference Specifications**:
  - [`AGENTS.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/AGENTS.md)
  - [`fps_research/CURRICULUM_ARCHITECTURE.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md)
  - [`fps_research/TECHNIQUE_TAXONOMY.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md)

---

## 1. Executive Summary & Overall Verdict

Part I (*Foundations, Formal Calculus & Combinatorial Species*, Chapters 01–04 + Blind Checkpoint `CP-I`) is an exceptionally thorough, pedagogically cohesive 6,002-line manuscript. Across all 40 problems (32 chapter ladder problems + 8 blind checkpoint problems) and 22 core theoretical subsections, **every single hand-checkable numerical trace ($N \le 4$) was independently verified and found to be 100% arithmetically exact**. Local algebraic hypotheses ($f_0 \in K^\times$ vs. field elements, $\operatorname{char} K = p > N$ vs. $p \le N$, valuation shifts $\operatorname{val}(F) = v$, and the 3-way modular reduction law for $P(x)^M$) are consistently stated beside divisions and transcendental operators.

However, our line-by-line mathematical and editorial audit uncovered **5 Major Defects** and **12 Minor / Polish Defects** that must be fixed to achieve 100% mathematical accuracy, zero magic steps, strict prerequisite closure, and spoiler-free Stage 1 compliance:

| Severity | File | Line(s) | Category | Brief Description |
| :--- | :--- | :--- | :--- | :--- |
| **MAJOR-1** | `ch02-calculus-frobenius-sparse-ode-newton.qmd` | [L242](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L242) | **Mathematical Formula Error** | The Derivative-Free Formal Residue LIF formula in the §2.2 comparison table is written as $[x^n]F(x)^k = [u^n](1 - u\phi'(u))\phi(u)^n$, which has both the wrong extraction index ($u^n$ instead of $u^{n-k}$) and is missing $\phi(u)^{-1}$ on $u\phi'(u)$ (should be $[u^{n-k}](\phi(u) - u\phi'(u))\phi(u)^{n-1}$). |
| **MAJOR-2** | `cp01-part1-foundations.qmd` | [L716](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L716), [L829](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L829), [L933](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L933), [L935](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L935) | **Mathematical Notation Bug (`!` / `!!` Factorial Corruption)** | Emphatic prose exclamation marks placed *inside* `$$...$$` display math corrupt the mathematical expressions into factorials and double factorials: $2^{k-1}!$ (L716), $\gcd(l_i, l_j)!$ (L829), $\frac{x^s}{s!}!$ (L933), and $(-1)^{|S|-1}(|S|-1)!!$ (L935, which renders as a double factorial instead of $(|S|-1)!$). |
| **MAJOR-3** | `ch04-egf-set-cyc-boxed-prufer.qmd` | [L948](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L948), [L965-L986](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L965-L986) | **Prerequisite Closure & Zero-Magic-Steps** | `Mas-2 #174` (*Luogu P5401 — Pearls*) invokes **Binomial Inversion** ($g_c = \sum_{k=c}^D (-1)^{k-c}\binom{k}{c}f_k$) and **Reversed Cauchy Convolution** in Step 3 without deriving the inversion from Chapter 04's tools and without a forward pointer, even though both are formally introduced in **Chapter 05 (§5.1–§5.2)**. |
| **MAJOR-4** | `cp01-part1-foundations.qmd` | [L226](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L226), [L331-L351](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L331-L351), [L691](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L691), [L898](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L898) | **Spoiler-Free Stage 1 Violations** | `CP-I.2`, `CP-I.3`, `CP-I.6`, and `CP-I.8` leak explicit technique names (`via $\ln$`, `via inv`, `Set Power Series $\exp$`, `SET`, `SEQ`, `PSET`) and even the full generating function formula $[x^3](x\frac{d}{dx}\ln\frac{1}{1-W(x)})$ inside the visible problem statements, visible traces, and Hint 1. |
| **MAJOR-5** | `ch01-ring-convolutions-newton-inv.qmd` | [L12](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L12), [L258](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L258), [L449](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L449) | **Swapped Chapter Forward Pointers** | Chapter 01 swaps the roles of Chapter 02 and Chapter 03 in three places: L12 says $D, \ln, \exp$ are deferred to "Chapter 03" (actually **Chapter 02**); L258 says `SEQ` of the Symbolic Method is formalized in "Chapter 02" (actually **Chapter 03**); L449 points only to "Chapter 03" for $\ln/\exp$ subset-sum products (introduced in **Chapter 02 §2.5** and **Chapter 03 §3.2**). |

---

## 2. Detailed Audit by File

---

### 2.1 Audit of `chapters/ch01-ring-convolutions-newton-inv.qmd`

#### A. Mathematical Accuracy & Hand-Checkable Numerical Traces (PASS — 100% Verified)
- **§1.2 Difference Convolution Trace ([L90-L113](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L90-L113))**: Verified $N=3$, $A(x) = 1 + 2x + 3x^2$, $B(x) = 4 + 5x + 6x^2$, $A^R(x) = 3 + 2x + x^2$, and $C(x) = A^R(x)B(x) = 12 + 23x + 32x^2 + 23x^3 + 6x^4$, yielding $d_0 = 32, d_1 = 23, d_2 = 6$. Exact.
- **§1.4 Newton `inv` Trace on Fibonacci Denominator ([L298-L326](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L298-L326))**: Verified $F(x) = 1 - x - x^2$ from $m=1 \to 2 \to 4$, producing $G_1 = 1$, $G_2 = 1 + x$, and $G_4 = 1 + x + 2x^2 + 3x^3$. Exact.
- **§1.5 Canonical Failure Mode #1 Counterexample ([L396-L402](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L396-L402))**: Verified $N = 3, v = 1$ with $A(x) = x + 5x^3$ and $B(x) = x - x^2 + x^3$. True quotient modulo $x^3$:
  $$\frac{1 + 5x^2}{1 - x + x^2} = (1 + 5x^2)(1 + x - x^3 + \cdots) \equiv 1 + x + 5x^2 \pmod{x^3},$$
  whereas premature $\bmod x^3$ truncation drops $5x^3$ and produces $1 + x + x^2$. Exact.
- **8-Problem Ladder Traces (`#019`, `#043`, `#004`, `#077`, `#049`, `#097`, `#066`, `#107`)**:
  - `SS-1 #019` ([L515-L522](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L515-L522)): Verified $a_0 \dots a_6 = (1, 0, 0, 1, 1, 1, 2)$.
  - `SS-2 #043` ([L610-L619](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L610-L619)): Verified $c_2 = 12, c_3 = 19, c_4 = 6$.
  - `Int-1 #004` ([L699-L711](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L699-L711)): Verified $A = (1, 3, 2) \implies 34$.
  - `Int-2 #077` ([L785-L793](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L785-L793)): Verified $S = \texttt{1?0}, T = \texttt{0?1} \implies (2, 0, 2)$.
  - `Adv-1 #049` ([L864-L872](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L864-L872)): Verified $F(x) = 1 - x - x^2 \implies G(x) \equiv 1 + x + 2x^2 + 3x^3 + 5x^4 \pmod{x^5}$.
  - `Adv-2 #097` ([L937-L945](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L937-L945)): Verified $S = \texttt{a?b}, k=1 \implies d=1$ is fail, $d=2, 3$ are periods.
  - `Mas-1 #066` ([L1011-L1022](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L1011-L1022)): Verified $A(x) = x + 2x^2, B(x) = x + 3x^2 \implies Q(x) \equiv 1 - x + 3x^2 \pmod{x^3}$.
  - `Mas-2 #107` ([L1090-L1099](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L1090-L1099)): Verified $c_1=2, c_2=3 \implies P(x) = 1 + 2x + 3x^2 + 6x^3$.

#### B. Specific Actionable Findings in `ch01-ring-convolutions-newton-inv.qmd`

1. **[MAJOR-5] Swapped Forward-Pointer Chapter Numbers (`Ch 02` vs. `Ch 03`)**
   - **Locations**: [L12](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L12), [L258](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L258), [L449](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L449)
   - **Problem**:
     - Line 12 states: *"Formal derivatives $D$, formal logarithms $\ln$, and formal exponentials $\exp$ are deferred entirely to Chapter 03."* In the curriculum, $D_x$, $\ln$, and $\exp$ are taught in **Chapter 02**.
     - Line 258 states: *"(In Chapter 02, we will formalize this as the `SEQ` operator of the Symbolic Method)."* In the curriculum, the unlabeled Symbolic Method and `SEQ` are taught in **Chapter 03 (§3.1)**.
     - Line 449 states: *"(In Chapter 03, we will also see how $\ln / \exp$ collapses $\prod_{i=1}^m (1 + c_i x^{w_i}) \bmod x^N$ in $O(N \log N)$ when $p > N$)."* This harmonic logarithm technique is introduced in **Chapter 02 (§2.5)** and expanded in **Chapter 03 (§3.2)**.
   - **Exact Fix**:
     - On L12, replace `Chapter 03` with `Chapter 02`.
     - On L258, replace `Chapter 02` with `Chapter 03 (§3.1)`.
     - On L449, replace `Chapter 03` with `Chapter 02 (§2.5) and Chapter 03 (§3.2)`.

2. **[MINOR-1] Prerequisite Justification for Negative Binomial Series in `SS-1 #019` ([L489](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L489), [L539-L543](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L539-L543))**
   - **Problem**: While Extraction Method A ($a_n = a_{n-1} + a_{n-3}$ via coefficient comparison) uses purely Chapter 01 tools, Extraction Method B uses $[x^m](1-x)^{-k} = \binom{m+k-1}{k-1}$ before the negative binomial series is formally derived via $D_x$ in Chapter 02 (§2.1).
   - **Exact Fix**: Add a 1-sentence justification on L539 noting that $[x^m](1-x)^{-k} = \binom{m+k-1}{k-1}$ counts weak compositions of $m$ into $k$ non-negative parts (stars-and-bars) and will be derived algebraically via iterated differentiation in Chapter 02 (§2.1).

3. **[MINOR-2] Missing Closing Pre-Submission Diagnostic Checklist (`AGENTS.md` Line 33 Compliance) ([L1157](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch01-ring-convolutions-newton-inv.qmd#L1157))**
   - **Problem**: Unlike Chapters 02 (§2.7), 03 (§3.7), and 04 (§4.6), Chapter 01 ends right after the quarantined template block in §1.6 without a closing **Pre-Submission Diagnostic Checklist**.
   - **Exact Fix**: Append a concise `## 1.7 Pre-Submission Diagnostic Checklist & Chapter Summary` (covering valuation alignment before `inv`, $f_0 \in K^\times$ invertibility, zero-padding to $2^{\lceil\log_2(2m-1)\rceil}$ inside the Newton step, and reversed-index validation at $k=0$).

---

### 2.2 Audit of `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd`

#### A. Mathematical Accuracy & Hand-Checkable Numerical Traces (PASS on Traces; 1 Formula Error on L242)
- **§2.1 Generalized Binomial Trace ([L125-L145](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L125-L145))**: Verified $(1+x)^\alpha \bmod x^5$ for $\alpha = -1, -2, 1/2, -1/2$, including $[x^n](1-4x)^{-1/2} = \binom{2n}{n}$. Exact.
- **§2.2 Frobenius Characteristic-$p$ Trace ([L208-L220](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L208-L220))**: Verified $(1 + 2x + x^2)^7 \equiv 1 + 2x + 2x^3 + x^4 \pmod{(3, x^5)}$ in 4 multiplications. Exact.
- **§2.3 Newton `sqrt`, `ln`, `exp` Traces ([L298-L377](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L298-L377))**: Verified $\sqrt{1-4x} \equiv 1 - 2x - 2x^2 - 4x^3 \pmod{x^4}$, $\ln\frac{1}{1-x} \equiv x + \frac{x^2}{2} + \frac{x^3}{3} \pmod{x^4}$, and $\exp(x + x^2/2 + x^3/3) \equiv 1 + x + x^2 + x^3 \pmod{x^4}$. Exact.
- **§2.4 Sparse Differential Recurrence Trace ([L519-L528](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L519-L528))**: Verified $(1 + 2x + x^3)^\alpha \bmod x^4$ via $k g_k = \sum_{j=1}^d ((j\alpha - k + j)p_j) g_{k-j}$. Exact.
- **8-Problem Ladder Traces (`#053`, `#050`, `#051`, `#165`, `#157`, `#170`, `#052`, `#091`)**: All 8 traces and derivations verified 100%.

#### B. Specific Actionable Findings in `ch02-calculus-frobenius-sparse-ode-newton.qmd`

1. **[MAJOR-1] Mathematical Formula Error in Derivative-Free Formal Residue LIF Table ([L242](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L242))**
   - **Location**: [L242](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L242)
   - **Current Text**:
     `| **Derivative-Free Formal Residue LIF** | $[x^n] F(x)^k = [u^n](1 - u \phi'(u))\phi(u)^n$ | Uses only polynomial powers $\phi(u)^n$ ($\operatorname{char} p \le N$ safe!) | Chapter 11 (§11.2) |`
   - **Mathematical Error**: For $F(x) = x\phi(F(x))$, the formula $[u^n](1 - u\phi'(u))\phi(u)^n$ is doubly wrong:
     1. Under the formal residue change of variables $u = F(x)$ (so $x = u/\phi(u)$ and $dx = \frac{\phi(u) - u\phi'(u)}{\phi(u)^2}\,du$), we have:
        $$[x^n] F(x)^k = [x^{-1}] x^{-n-1} F(x)^k = [u^{-1}] \left(\frac{u}{\phi(u)}\right)^{-n-1} u^k \frac{\phi(u) - u\phi'(u)}{\phi(u)^2} = [u^{n-k}] \big(\phi(u) - u\phi'(u)\big)\phi(u)^{n-1}.$$
     2. Test on Catalan trees $\phi(u) = 1 + u$, $k = 1$, $n = 2$:
        - True value: $[x^2] F(x) = C_1 = 1$.
        - Correct formula: $[u^{2-1}]\big((1+u) - u(1)\big)(1+u)^{2-1} = [u^1](1+u) = 1$.
        - Current table formula on L242: $[u^2](1 - u)(1+u)^2 = [u^2](1 + u - u^2 - u^3) = -1 \neq 1$!
   - **Exact Fix**: Replace `[x^n] F(x)^k = [u^n](1 - u \phi'(u))\phi(u)^n` on [L242](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L242) with:
     `$[x^n] F(x)^k = [u^{n-k}]\big(\phi(u) - u \phi'(u)\big)\phi(u)^{n-1}$`.

2. **[MINOR-3] Wrong Forward-Pointer Chapter Number for Semi-Online CDQ Divide-and-Conquer FFT ([L384](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L384))**
   - **Location**: [L384](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L384)
   - **Current Text**: `*(Forward pointer: in Chapter 13, we will also see an alternative $O(N \log^2 N)$ Divide-and-Conquer CDQ algorithm via $F'(x) = B'(x) F(x)$ with much smaller constant factors for $N \le 10^5$.)*`
   - **Problem**: According to `CURRICULUM_ARCHITECTURE.md`, Semi-Online CDQ Divide-and-Conquer FFT for `exp` is taught in **Chapter 09 (§9.4)**, whereas Chapter 13 is *Matrix-Tree, BEST Theorem & Algebraic Graph Theory*.
   - **Exact Fix**: Change `Chapter 13` to `Chapter 09 (§9.4)`.

3. **[MINOR-4] Forward-Pointer Polish for Algebraic EGF Usage in `Adv-1 #157` ([L983-L988](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L983-L988)) and `Mas-2 #091` ([L1177-L1204](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L1177-L1204))**
   - **Problem**: Both problems use exponential generating functions ($\sum \frac{a_n}{n!} x^n$ and $e^x$) algebraically via the Binomial/Multinomial Theorem and $\exp(x)$ from §2.3 before Chapter 04 introduces combinatorial EGFs. While the algebraic derivations are 100% self-contained in Chapter 02, adding an explicit forward pointer to Chapter 04 (§4.1) strengthens prerequisite transparency.
   - **Exact Fix**: Add a parenthetical note in `Adv-1 #157` (L985) and `Mas-2 #091` (L1178) pointing forward to **Chapter 04 (§4.1)** for the general combinatorial theory of Exponential Generating Functions (EGFs) and binomial convolutions.

4. **[MINOR-5] Radical Rationalization Branch Sign Clarification & Duplicate Word Typo ([L402](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L402), [L1254](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L1254))**
   - **Locations**: [L402](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L402) and [L1254](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd#L1254)
   - **Exact Fix**:
     - On L402, fix duplicate word `different algebraic algebraic structure` $\to$ `different algebraic structure`.
     - On L1254, clarify that in $F(x) = \frac{2C(x)}{-B(x) + \sqrt{B(x)^2 - 4A(x)C(x)}}$, the branch of $\sqrt{B(x)^2 - 4A(x)C(x)}$ is chosen with constant term $-B(0)$ so the denominator has non-zero constant term $-2B(0) \in K^\times$.

---

### 2.3 Audit of `chapters/ch03-mset-partitions-euler-polya.qmd`

#### A. Mathematical Accuracy & Hand-Checkable Numerical Traces (PASS — 100% Verified)
- **§3.1 Compositions into $\{1,2\}$ and $\ge 2$ ([L126-L150](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L126-L150))**: Verified $1, 1, 2, 3, 5$ and $1, 0, 1, 1, 2$. Exact.
- **§3.2 Forward & Inverse Euler Transform Trace ([L306-L339](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L306-L339))**: Verified $(a_1, a_2, a_3, a_4) = (1, 2, 0, 1) \Longleftrightarrow (b_0, b_1, b_2, b_3, b_4) = (1, 1, 3, 3, 7)$ in both directions (via $nb_n = \sum_{k=1}^n c_k b_{n-k}$ and Möbius inversion $n a_n = \sum_{d\mid n} \mu(n/d) c_d$). Exact.
- **§3.3 Pentagonal Number Theorem & Franklin Involution Trace ([L422-L430](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L422-L430))**: Verified $p(0\dots 5) = (1, 1, 2, 3, 5, 7)$. Exact.
- **§3.5 Burnside/Pólya Unlabeled Graphs on $n=4$ Vertices ([L866-L882](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L866-L882))**: Verified all $p(4) = 5$ partitions $\lambda \vdash 4$:
  $$g_4 = \frac{1 \cdot 2^6 + 6 \cdot 2^4 + 8 \cdot 2^2 + 3 \cdot 2^4 + 6 \cdot 2^2}{24} = \frac{64 + 96 + 32 + 48 + 24}{24} = \frac{264}{24} = 11.$$
  Exact.
- **8-Problem Ladder Traces (`#001`, `#188`, `#153`, `#009`, `#223`, `#221`, `#150`, `#159`)**: All 8 traces and derivations verified 100%.

#### B. Specific Actionable Findings in `ch03-mset-partitions-euler-polya.qmd`

1. **[MINOR-6] Prerequisite Callout Filename Slugs & Chapter Pointer ([L12-L13](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L12-L13), [L658](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L658))**
   - **Locations**: [L12-L13](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L12-L13), [L658](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L658)
   - **Exact Fix**:
     - On L12–13, update `ch01-fps-ring-formal-calculus` $\to$ `ch01-ring-convolutions-newton-inv` and `ch02-newton-ln-exp-pow` $\to$ `ch02-calculus-frobenius-sparse-ode-newton` to match the repository filenames.
     - On L658, update `Newton-iteration FPS inv (Chapter 02)` $\to$ `Newton-iteration FPS inv (Chapter 01 §1.4)`.

2. **[MINOR-7] Revisited Dual-Perspective Cross-Reference (`#153` $\leftrightarrow$ `#165`) ([L1056-L1115](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L1056-L1115))**
   - **Location**: `Int-1 #153` (*Luogu P4389 — 付公主的背包*) ([L1056-L1115](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch03-mset-partitions-euler-polya.qmd#L1056-L1115))
   - **Problem**: While §3.2 (L177) cross-references Chapter 02 §2.5, `Int-1 #153` itself should explicitly reference `Int-2 #165` (*Subset Sum $\prod(1+x^{s_i})$*) from Chapter 02 per `CURRICULUM_ARCHITECTURE.md` §5.2 Revisited Index #2.
   - **Exact Fix**: Add a 1-sentence cross-reference inside `Int-1 #153` (around L1087) contrasting the all-positive Euler transform log-coefficients $+\frac{c_v}{j} x^{jv}$ of $\operatorname{MSET}$ (`#153`) with the alternating $(-1)^{j-1} \frac{c_v}{j} x^{jv}$ coefficients of $\operatorname{PSET}$ (`#165` in Chapter 02).

---

### 2.4 Audit of `chapters/ch04-egf-set-cyc-boxed-prufer.qmd`

#### A. Mathematical Accuracy & Hand-Checkable Numerical Traces (PASS — 100% Verified)
- **§4.1 Labeled Pair Trace $n=3$ ([L29-L35](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L29-L35))**: Verified $\binom{3}{2} = 3$ relabelings. Exact.
- **§4.2 Derangement Trace $d_0 \dots d_4$ ([L108-L130](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L108-L130))**: Verified $d_0 \dots d_4 = (1, 0, 1, 2, 9)$ via $\frac{e^{-x}}{1-x}$. Exact.
- **§4.3 Connected Simple Labeled Graphs $c_1 \dots c_4$ ([L180-L195](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L180-L195))**: Verified $\ln \widehat{G}(x) = x + \frac{1}{2}x^2 + \frac{4}{6}x^3 + \frac{38}{24}x^4 \implies c_1=1, c_2=1, c_3=4, c_4=38$. Exact.
- **§4.4 Boxed Product Characteristic-$p$ Bypass Trace over $\mathbb{F}_2$ ([L292-L298](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L292-L298))**: Verified $c_1 \dots c_4 \equiv (1, 1, 0, 0) \pmod 2$, matching $1, 1, 4, 38 \bmod 2$ without dividing by $2! = 0$ or $4! = 0 \pmod 2$. Exact.
- **§4.5 Prüfer Decoding Trace $n=4$ ([L333-L340](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L333-L340))**: Verified $P = (2, 3)$ on $\{1,2,3,4\}$ decodes to path $1 - 2 - 3 - 4$ with degrees $(1, 2, 2, 1)$. Exact.
- **8-Problem Ladder Traces (`#208`, `#090`, `#070`, `#008`, `#035`, `#011`, `#041`, `#174`)**: All 8 numerical traces verified 100%.

#### B. Specific Actionable Findings in `ch04-egf-set-cyc-boxed-prufer.qmd`

1. **[MAJOR-3] Prerequisite Closure & Zero-Magic-Steps Violation in `Mas-2 #174` (*Luogu P5401 — Pearls*) ([L948](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L948), [L965-L986](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L965-L986))**
   - **Locations**: [L948](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L948), [L965-L986](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L965-L986)
   - **Problem**:
     - In Hint 3 (L948) and Step 3 (L981–986), the solution writes:
       $$f_k = \sum_{c=k}^D \binom{c}{k} g_c \implies g_c = \sum_{k=c}^D (-1)^{k-c} \binom{k}{c} f_k$$
       by citing "binomial inversion" and then evaluates it via "a single reversed Cauchy convolution (middle product)".
     - However, **Binomial Inversion** and **Reversed Cauchy Convolution (Middle Product)** are core topics of **Chapter 05 (§5.1–§5.2)**, NOT Chapters 01–04! Using them in Chapter 04 without deriving the identity from scratch and without a forward pointer violates Prerequisite Closure & Zero Magic Steps.
   - **Exact Fix**:
     1. Derive the relation between $g_c$ and $f_k$ directly from Chapter 04's bivariate hyperbolic EGF in 3 self-contained lines:
        Tagging each odd-frequency color with $y$, a single color has EGF $\cosh x + y \sinh x = e^x + (y - 1)\sinh x$. Across $D$ independent colors:
        $$\sum_{c=0}^D g_c y^c = n![x^n]\big(e^x + (y - 1)\sinh x\big)^D = \sum_{k=0}^D (y - 1)^k \underbrace{\binom{D}{k} n![x^n](\sinh x)^k e^{(D-k)x}}_{f_k}.$$
        Expanding $(y - 1)^k = \sum_{c=0}^k \binom{k}{c} (-1)^{k-c} y^c$ and extracting $[y^c]$ immediately yields $g_c = \sum_{k=c}^D (-1)^{k-c} \binom{k}{c} f_k$ using purely the Binomial Theorem!
     2. For the upper-triangular sum $\sum_{k=c}^D (-1)^{k-c} \frac{1}{(k-c)!} (k! f_k)$, show explicitly how it reduces toChapter 01 §1.2's **Reversed Convolution (Difference Index Shift)** by reversing $A_k = k! f_k$, and add a forward pointer to **Chapter 05 (§5.1–§5.2)** where Binomial Inversion and Transposed/Reversed Convolutions are developed systematically.

2. **[MINOR-8] Misattributed Chapter Reference for Otter's Dissimilarity Theorem ([L235](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L235))**
   - **Location**: [L235](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L235)
   - **Current Text**: `*(Contrast this with Chapter 03's unlabeled trees, where symmetries can make different vertices indistinguishable, requiring Otter's Dissimilarity Theorem $U(x) = T(x) - \frac{1}{2}(T(x)^2 - T(x^2))$ instead of division by $n$!)*`
   - **Problem**: Chapter 03 does not cover Otter's Dissimilarity Theorem; per `CURRICULUM_ARCHITECTURE.md`, Otter's Theorem and unlabeled tree enumeration are taught in **Chapter 11 (§11.4)**.
   - **Exact Fix**: Update L235 to: `*(Contrast this with the unlabeled setting of Chapter 03, where symmetries can make different vertices indistinguishable; as we will prove in Chapter 11 (§11.4), unpointing unlabeled trees requires Otter's Dissimilarity Theorem $U(x) = T(x) - \frac{1}{2}(T(x)^2 - T(x^2))$ instead of division by $n$!)*`.

3. **[MINOR-9] Explicit 3-Way Modular Reduction Reminder in `Adv-2 #011` (*AtCoder ARC 154 E — Dice*) ([L833](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L833))**
   - **Location**: [L833](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch04-egf-set-cyc-boxed-prufer.qmd#L833)
   - **Problem**: In `Adv-2 #011`, the number of dice is $M \le 10^9$ while $p = 998244353 < 10^9$. Line 833 writes $N^M \exp(M \ln(N^{-1}\widehat{P}_A(x)))$ without reminding the reader that $M$ in $N^M$ must be reduced $\bmod (p-1)$ (Fermat) while $M$ multiplying $\ln(\dots)$ must be reduced $\bmod p$.
   - **Exact Fix**: Write $N^{M \bmod (p-1)} \exp\!\big((M \bmod p) \ln(N^{-1}\widehat{P}_A(x))\big) \pmod{x^{K+1}}$ on L833 and cite Chapter 02's 3-way modular reduction law.

---

### 2.5 Audit of `checkpoints/cp01-part1-foundations.qmd`

#### A. Mathematical Accuracy & Hand-Checkable Numerical Traces (PASS on Traces; 4 Notation Bugs with `!` inside `$$...$$`)
- **`CP-I.1 #078` Trace ([L56-L62](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L56-L62))**: Verified $R=G=B=2, K=3, X=Y=Z=2 \implies 8$. Exact.
- **`CP-I.2 #144` Trace ([L230-L237](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L230-L237))**: Verified $q=(4, 8, 12) \implies E = (-11, -8, 9)$. Exact.
- **`CP-I.3 #246` Trace ([L339-L345](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L339-L345))**: Verified $N=3 \implies 3w_3 + 3w_1w_2 + w_1^3$. Exact.
- **`CP-I.4 #032` Trace ([L458-L463](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L458-L463))**: Verified $N=3, M=4 \implies 8$. Exact.
- **`CP-I.5 #079` Trace ([L566-L573](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L566-L573))**: Verified $N=3, M=1, S=2 \implies 3$. Exact.
- **`CP-I.6 #250` Trace ([L682-L685](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L682-L685))**: Verified $N=4 \implies 6$. Exact.
- **`CP-I.7 #037` Trace ([L799-L800](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L799-L800))**: Verified $N=3 \implies 4$ unlabeled graphs. Exact.
- **`CP-I.8 #024` Trace ([L902-L907](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L902-L907))**: Verified $N=3, M=6, D=(2,3,2) \implies 8$. Exact.

#### B. Specific Actionable Findings in `cp01-part1-foundations.qmd`

1. **[MAJOR-2] Mathematical Notation Corruption: Emphatic `!` Inside `$$...$$` Display Math ([L716](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L716), [L829](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L829), [L933](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L933), [L935](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L935))**
   - **Problem**: In four display equations across `CP-I.6`, `CP-I.7`, and `CP-I.8`, an emphatic exclamation point `!` was typed inside `$$...$$` at the end of the equation, which LaTeX renders as a **factorial** (or **double factorial** when following a real factorial!):
     - **[L716](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L716)**: `$$P_k(1) = \prod_{j=2}^k (1 + 1) = 2^{k - 1}!$$` $\to$ renders as $(2^{k-1})!$ instead of $2^{k-1}$.
     - **[L829](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L829)**: `$$\frac{l_i l_j}{\operatorname{lcm}(l_i, l_j)} = \gcd(l_i, l_j)!$$` $\to$ renders as $(\gcd(l_i, l_j))!$ instead of $\gcd(l_i, l_j)$.
     - **[L933](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L933)**: `$$C(x) = \ln(1 + x) = \sum_{s = 1}^{\infty} (-1)^{s - 1} \frac{x^s}{s} = \sum_{s = 1}^{\infty} (-1)^{s - 1} (s - 1)! \frac{x^s}{s!}!$$` $\to$ has a spurious trailing `!` after `\frac{x^s}{s!}`.
     - **[L935](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L935)**: `$$\sum_{\substack{E_S \subseteq \binom{S}{2} \\ (S, E_S) \text{ connected}}} (-1)^{|E_S|} = (-1)^{|S| - 1} (|S| - 1)!!$$` $\to$ renders as the **double factorial** $(|S|-1)!!$ instead of $(|S|-1)!$.
   - **Exact Fix**: Replace the trailing `!$$` on L716, L829, L933, and L935 with `.$$`! (Also on [L738](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L738), fix the minor typo `(1 + 1^j)` $\to$ `(1 + 1^{F_j})`).

2. **[MAJOR-4] Spoiler-Free Stage 1 Violations in `CP-I.2`, `CP-I.3`, `CP-I.6`, and `CP-I.8` ([L226](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L226), [L331-L351](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L331-L351), [L691](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L691), [L898](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L898))**
   - **Problem**: Per `CURRICULUM_ARCHITECTURE.md` §5.3 and the Checkpoint's own *Rules of Engagement* (L11–17), the visible problem statement, visible trace, and Hint 1 must **NOT** leak the technique name or generating function formula (which belong in Hint 2 / Hint 3 / Stage 2). Currently:
     - **[L226](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L226) (`CP-I.2` visible Target Complexity)**: says `using complex floating-point FFT`.
     - **[L331-L332](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L331-L332) (`CP-I.3` visible Problem Statement)**: says `Part A (Connected Clique Count via $\ln$)` and `Part B (Circular Block Partition via inv)`.
     - **[L344](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L344) (`CP-I.3` visible Hand-Checkable Trace)**: says `Notice the total is $3 w_3 + 3 w_1 w_2 + w_1^3 = [x^3]\big(x \frac{d}{dx} \ln \frac{1}{1 - W(x)}\big)$ where $W(x) = \sum_{k \ge 1} w_k x^k$!` — giving away the entire closed-form generating function in the visible problem statement!
     - **[L350-L351](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L350-L351) (`CP-I.3` Hint 1)** and **[L691](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L691) (`CP-I.6` Hint 1)**: explicitly name $\operatorname{SET}$, $\operatorname{SEQ}(W) = \frac{1}{1 - W(x)}$, and $\operatorname{PSET}$ $P(x) = \prod(1 + x^{F_k})$ inside Hint 1 instead of Hint 2.
     - **[L898](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L898) (`CP-I.8` visible Target Complexity)**: says `$O(3^N)$ time (via subset-partition DP) or $O(N^2 2^N)$ time (via Set Power Series $\exp$)`.
   - **Exact Fix**:
     - On L226: change to `$O(n \log n)$ time and $O(n)$ space.`
     - On L331–332: remove `via $\ln$` and `via inv`.
     - On L344: change to `Notice the total is $3 w_3 + 3 w_1 w_2 + w_1^3$.` (move $[x^3](x \frac{d}{dx} \ln \frac{1}{1 - W(x)})$ to Hint 2/3).
     - On L350–351 and L691: keep Hint 1 focused purely on the structural combinatorial clue (unlabeled vs. labeled connected components, and anchoring vertex $1$'s block of size $k$ with $k$ rotational placements; distinct Fibonacci summands with $\sum_{j=2}^k F_j = F_{k+2}-2$), deferring the explicit $\operatorname{SET}/\operatorname{SEQ}/\operatorname{PSET}$ names and formulas to Hint 2.
     - On L898: change to `$O(3^N + 2^N \log M)$ time (or $O(N^2 2^N + 2^N \log M)$ time) and $O(2^N)$ space.`

3. **[MINOR-10] Streamlining Step 3 of `CP-I.7` (`#037` Unlabeled Graphs) ([L853-L858](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L853-L858))**
   - **Location**: [L853-L858](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp01-part1-foundations.qmd#L853-L858)
   - **Problem**: Step 3 in `CP-I.7` discusses the colored/connected extension (ABC 284 Ex) in an informal, stream-of-consciousness paragraph (`*(Wait: why can we NOT just take $\ln$...)*`) that trails off with `c(\lambda) = g(\lambda) - \sum_{\mu \subsetneq \lambda} \dots$!)*`.
   - **Exact Fix**: Replace L853–858 with a crisp, self-contained derivation for the colored extension (for each cycle of length $l_i$, monochromaticity gives $K$ color choices, or via binomial inclusion-exclusion $\sum_{j=1}^K (-1)^{K-j}\binom{K}{j} j^{m(\lambda)}$ for surjective $K$-colorings) and write out the exact sub-partition connected recurrence $c(\lambda) = g(\lambda) - \sum_{\substack{\mu \subsetneq \lambda \\ l_1 \in \mu}} \binom{\text{mult}_\lambda}{\text{mult}_\mu} c(\mu) g(\lambda \setminus \mu)$ without trailing ellipses.

---

## 3. Summary Checklist Across All 8 Mandatory Audit Dimensions

| Audit Dimension | Status | Notes |
| :--- | :--- | :--- |
| **1. Mathematical Accuracy & Index Boundaries** | **Needs 2 Fixes (`MAJOR-1`, `MAJOR-2`)** | Fix Derivative-Free LIF preview formula in `Ch 02` L242 and remove trailing `!` inside `$$...$$` in `CP-I` L716, L829, L933, L935. All 40 numerical traces ($N \le 4$) are 100% verified. |
| **2. Zero Magic Steps & Reverse-Engineering Scratchpads** | **Needs 2 Fixes (`MAJOR-3`, `MINOR-10`)** | Add self-contained 3-line derivation of Binomial Inversion in `Ch 04` `Mas-2 #174` (L965–986) and clean up trailing `\dots` in `CP-I.7` Step 3 (L853–858). |
| **3. Strict Prerequisite Closure & Zero Forward-References** | **Needs 3 Fixes (`MAJOR-3`, `MAJOR-5`, `MINOR-3/6/8`)** | Fix swapped `Ch 02`/`Ch 03` pointers in `Ch 01` (L12, L258, L449), `Ch 02` CDQ pointer (L384 $\to$ Ch 09), and `Ch 04` Otter pointer (L235 $\to$ Ch 11). |
| **4. 100% Sub-Section, Failure Mode & Char-$p$ Completeness** | **PASS (100%)** | Canonical Failure Modes `#1`, `#2`, `#3`, `#4`, `#16` and Characteristic-$p$ bypasses (`Frobenius`, `Boxed Product`, `Cycle Index`) are exemplary. |
| **5. 8-Problem Ladder & Blind Checkpoint Completeness** | **Needs 1 Fix (`MAJOR-4`)** | All 40 problems match `CURRICULUM_ARCHITECTURE.md` 100%. Remove Stage 1 spoilers in `CP-I.2`, `CP-I.3`, `CP-I.6`, and `CP-I.8`. |
| **6. `AGENTS.md` Editorial Policy Compliance** | **Needs 1 Minor Fix (`MINOR-2`)** | Add closing Pre-Submission Diagnostic Checklist to `Ch 01`. All standard templates are properly quarantined. |
| **7. Citations & Terminology Integration** | **PASS (100%)** | `[EN]`/`[ZH]`/`[JA]` terminology and classical citations (Flajolet–Sedgewick, Brent–Kung, Euler, Franklin, Pólya, Joyal, Prüfer) are thoroughly integrated. |
| **8. Quarto Formatting & Render Safety** | **PASS (100%)** | Zero forbidden `\(` or `\[` delimiters, zero unescaped `|` in tables, and all `<details>` and `:::` blocks are properly balanced. |
