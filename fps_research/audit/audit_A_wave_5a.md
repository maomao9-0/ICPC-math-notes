# Principal Mathematical & Pedagogical Audit Report — Wave 5A (`cohort3_wave_5a_ode_sparse_cdq_relaxed.md`)

- **Auditor**: Inspector A (Principal Mathematical & Pedagogical Auditor)
- **Target File Audited**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md` (1,421 lines)
- **Source Files Compared**:
  1. `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort1_iter_41_to_45_ode_sparse_cdq_relaxed.md` (1,709 lines)
  2. `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_93_to_97_ode_sparse_cdq_relaxed.md` (1,896 lines)
  3. `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_41_to_45_ode_sparse_cdq_relaxed.md` (313 lines)

---

## 1. Executive Summary & Audit Scorecard

| Audit Dimension | Status | Summary of Findings |
| :--- | :---: | :--- |
| **Mathematical & Algorithmic Exactness** | **FAIL (4 Critical Bugs)** | 1. **Lines 125–127 (Sec 2.4 #5)**: Wrong chain-rule sign and wrong index shift on 2-regular graph EGF $F(x) = (1-x)^{-1/2}e^{-x/2-x^2/4}$; states $2(1-x)F' = -(x^2+x)F$ and $f_n = f_{n-1} - \frac{1}{2n}f_{n-2} - \frac{1}{2n}f_{n-3}$ (which yields negative counts $g_3=-1, g_4=-4$) instead of $2(1-x)F' = x^2 F$ and $f_n = \frac{n-1}{n}f_{n-1} + \frac{1}{2n}f_{n-3}$.<br>2. **Lines 432–438 (Sec 4.2)**: False arithmetic $-\frac{1}{2}(1) = 0$ on line 432 followed by two banned `\)` LaTeX delimiters and raw stream-of-consciousness self-correction (`wait: at $n=2$... why did $g_2=0$?`).<br>3. **Lines 360–368 (Sec 3.3 Demo 3)**: Algebraic mismatch between $F(x) = (1-x)^{-1/2}\exp(\frac{x^2}{2(1-x)})$ and $F(x) = e^{-x/(1-x)}G(x)$ where $G(x) = (1-x)^{-1/2}\exp(\frac{x}{2(1-x)})$ (off by a factor of $e^{x/2}$).<br>4. **Lines 651–665 (Sec 5.2 Engine 3) & Lines 1009–1018 (Sec 7 Prob 12)**: Truncated derivations containing `\dots`, `wait:`, and a false claim that $a_k = [y^k]F_n(y)$ in CF 755G satisfies a standalone 3-term recurrence in $k$ (the minimal standalone recurrence in $k$ has 4 terms; a 3-term relation requires the coupled pair $(F_n, F_{n-1})$). |
| **Zero Information Loss vs. Source Cohorts** | **FAIL (6 Omissions)** | 1. Omitted the standalone `solve_first_order_ode` C++ reference kernel (Newton + Integrating Factor) from Cohort 2 Sec 94.1.<br>2. Omitted 5 hand-checkable small-$n$ toy traces ($n \le 4$) present in Cohort 1 & Cohort 2 (Autonomous ODE, Change-of-Variable ODE, Riccati ODE, Sparse Exp $\exp(x+2x^3)$, and Parametric Binomial Sum $c=2$).<br>3. Omitted the Summary Table of Classic Binomial Sums & Diagonal ODEs from Cohort 2 Sec 96.5.<br>4. Omitted Derivation 1 ($[x^n](1+ax)^n(1+bx)^n$ via bivariate differential elimination) from Cohort 1 Sec 44.3.<br>5. Omitted rejected template problem `Luogu P6115 — 【模板】整式递推` from Cohort 1 Sec 8.<br>6. Omitted `Lipshitz (1988/1989)` and `peltorator (2020)` from Section 9, corrupted author names in `[EN-6]` as `L.abahn, M.abahn`, and dropped direct URLs for EI's CSDN blogs and Nyaan's Library headers. |
| **Pedagogical & Editorial Completeness** | **FAIL (7 Violations)** | - 2 banned `\)` math delimiters on lines 435 and 438.<br>- 4 raw stream-of-consciousness `Wait` / `wait:` blocks (lines 385, 435, 654/660, 1015).<br>- 3 formatting/spacing typos (lines 405, 830, 1400). |
| **Accepted Problem Coverage (25/25)** | **PASS (with 1 fix)** | All 25 unique accepted problems across Cohort 1 (24 problems) and Cohort 2 (25 problems, including ABC 222 H) are present with statements, constraints, judge URLs, 3-tier hints, and solutions; Problem 12 (`Codeforces 755G`) requires replacing the truncated `\dots` / `Wait:` paragraph on lines 1009–1018. |

---

## 2. Part I: Critical Mathematical, Algorithmic & LaTeX Bugs (With Drop-In Replacements)

### Bug 1 [CRITICAL MATH ERROR]: Wrong ODE Sign and Wrong Recurrence for 2-Regular Graphs in Section 2.4, Item 5 (Lines 125–127)

- **Location**: [cohort3_wave_5a_ode_sparse_cdq_relaxed.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L125-L127)
- **Current Erroneous Text (Lines 125–127)**:
  ```markdown
  5. **2-Regular Graphs (Disjoint Unions of Cycles of Length $\ge 3$)**:
     - $F(x) = (1-x)^{-1/2} \exp\left(-\frac{x}{2} - \frac{x^2}{4}\right) \implies \frac{F'(x)}{F(x)} = -\frac{1}{2(1-x)} - \frac{1}{2} - \frac{x}{2} = \frac{-1 - (1-x^2)}{2(1-x)} = \frac{x^2 - 2}{2(1-x)}$... Wait: $\ln F(x) = -\frac{1}{2}\ln(1-x) - \frac{x}{2} - \frac{x^2}{4}$, so $\frac{F'(x)}{F(x)} = +\frac{1}{2(1-x)} - \frac{1}{2} - \frac{x}{2}?$ Wait: in Cohort 1 & 2, $F(x) = (1-x)^{-1/2}\exp(-x/2 - x^2/4)$ (or $(1+x)$); let's check both signs carefully:
     - For **2-regular simple graphs**, $\ln F(x) = \sum_{k \ge 3} \frac{x^k}{2k} = -\frac{1}{2}\ln(1-x) - \frac{x}{2} - \frac{x^2}{4}$. Differentiating gives $\frac{F'(x)}{F(x)} = \frac{1}{2(1-x)} - \frac{1+x}{2} = \frac{1 - (1-x^2)}{2(1-x)} = \frac{x^2}{2(1-x)}$, or if $F(x) = (1+x)^{-1/2}\exp\left(-\frac{x}{2}-\frac{x^2}{4}\right)$, $2(1-x)F'(x) = -(x^2+x)F(x) \implies f_n = f_{n-1} - \frac{1}{2n}f_{n-2} - \frac{1}{2n}f_{n-3}$.
  ```
- **Mathematical Audit**:
  1. **Stream-of-Consciousness Contamination**: Line 125 contains raw self-argument (`... Wait: ... Wait: in Cohort 1 & 2 ... let's check both signs carefully`).
  2. **Chain-Rule Sign Error (Inherited from Cohort 1 Line 168 & Cohort 2 Line 113)**: For $F(x) = (1-x)^{-1/2} \exp\left(-\frac{x}{2} - \frac{x^2}{4}\right)$, we have $\ln F(x) = -\frac{1}{2}\ln(1-x) - \frac{x}{2} - \frac{x^2}{4}$. By the chain rule, $\frac{d}{dx}\left[-\frac{1}{2}\ln(1-x)\right] = +\frac{1}{2(1-x)}$, so:
     $$\frac{F'(x)}{F(x)} = \frac{1}{2(1-x)} - \frac{1}{2} - \frac{x}{2} = \frac{1 - (1 - x^2)}{2(1-x)} = \frac{x^2}{2(1-x)} \implies 2(1 - x) F'(x) = x^2 F(x)$$
  3. **Index-Shift Error**: Even when extracting $[x^{n-1}]$ from $(1-x)F'(x)$, the coefficient of $x^{n-1}$ in $x F'(x)$ is $(n-1)f_{n-1}$, NOT $n f_{n-1}$! Writing $f_n = f_{n-1} - \frac{1}{2n}f_{n-2} - \frac{1}{2n}f_{n-3}$ produces **negative numbers** for labeled 2-regular graphs ($g_3 = -1, g_4 = -4, g_5 = -18$).
  4. **Exact Recurrence**: Extracting $[x^{n-1}]$ from $2 F'(x) - 2x F'(x) = x^2 F(x)$ gives:
     $$2n f_n - 2(n - 1) f_{n-1} = f_{n-3} \implies f_n = \frac{n - 1}{n} f_{n-1} + \frac{1}{2n} f_{n-3} \quad (n \ge 1)$$
     Multiplying by $n!$ gives the labeled 2-regular graph recurrence $g_n = (n-1)g_{n-1} + \binom{n-1}{2}g_{n-3}$, yielding $g_0 = 1, g_1 = 0, g_2 = 0, g_3 = 1, g_4 = 3, g_5 = 12, g_6 = 70$ (OEIS A001205).
- **Drop-In Replacement for Lines 125–127**:
  ```markdown
  5. **2-Regular Simple Graphs (Disjoint Unions of Undirected Cycles of Length $\ge 3$)**:
     - By the Exponential Formula, a 2-regular simple graph is a set of undirected cycles of length $k \ge 3$ (each cycle on $k$ labeled vertices has $\frac{(k-1)!}{2}$ orientations), so $\ln F(x) = \sum_{k=3}^{\infty} \frac{x^k}{2k} = -\frac{1}{2}\ln(1-x) - \frac{x}{2} - \frac{x^2}{4}$, giving $F(x) = (1-x)^{-1/2} \exp\left(-\frac{x}{2} - \frac{x^2}{4}\right)$.
     - Taking the logarithmic derivative via the chain rule $\frac{d}{dx}\big[-\frac{1}{2}\ln(1-x)\big] = +\frac{1}{2(1-x)}$ yields:
       $$\frac{F'(x)}{F(x)} = \frac{1}{2(1-x)} - \frac{1}{2} - \frac{x}{2} = \frac{1 - (1 - x^2)}{2(1-x)} = \frac{x^2}{2(1-x)} \implies 2(1 - x) F'(x) = x^2 F(x)$$
     - Extracting $[x^{n-1}]$ from $2 F'(x) - 2x F'(x) = x^2 F(x)$ gives $2n f_n - 2(n-1) f_{n-1} = f_{n-3}$, i.e., $f_n = \frac{n-1}{n} f_{n-1} + \frac{1}{2n} f_{n-3}$ for $n \ge 1$ ($f_0 = 1, f_1 = 0, f_2 = 0$). Multiplying by $n!$ recovers the combinatorial recurrence $g_n = (n-1)g_{n-1} + \binom{n-1}{2}g_{n-3}$ ($g_0 = 1, g_1 = 0, g_2 = 0, g_3 = 1, g_4 = 3, g_5 = 12, g_6 = 70$).
  ```

---

### Bug 2 [CRITICAL LATEX CORRUPTION + ARITHMETIC ERROR + STREAM-OF-CONSCIOUSNESS]: Sparse Square Root Trace in Section 4.2 (Lines 430–438)

- **Location**: [cohort3_wave_5a_ode_sparse_cdq_relaxed.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L430-L438)
- **Current Erroneous Text (Lines 430–438)**:
  ```markdown
  - $n = 0$: $g_0 = f_0^{1/2} = 1$.
  - $n = 1$: $g_1 = \frac{1}{1} \left( \frac{3}{2}(1) - 1 \right) (2) g_0 = \frac{1}{2} (2)(1) = 1$.
  - $n = 2$: $g_2 = \frac{1}{2} \left[ \left(\frac{3}{2}(1) - 2\right)(2) g_1 \right] = \frac{1}{2} \left(-\frac{1}{2}\right)(2)(1) = -\frac{1}{2}(1) = 0$... wait: $\frac{1}{2}(-1)(1) = -1/2$! Let's check: $(1 + 2x + x^3)^{1/2} = 1 + \frac{1}{2}(2x + x^3) - \frac{1}{8}(2x + x^3)^2 + \frac{1}{16}(2x + x^3)^3 - \frac{5}{128}(2x + x^3)^4 \pmod{x^5} = 1 + x - \frac{1}{2}x^2 + \frac{1}{2}x^3 - \frac{1}{2}x^4 + \frac{1}{2}x^3 - \dots$
  - $n = 3$: $g_3 = \frac{1}{3} \left[ \left(\frac{3}{2}(1) - 3\right)(2) g_2 + \left(\frac{3}{2}(3) - 3\right)(1) g_0 \right] = \frac{1}{3} \left[ (-3)(0) + \frac{3}{2}(1)(1) \right] = \frac{1}{2}$ (wait: with $g_2 = -1/2$,let's trace carefully!).
  - $n = 4$: $g_4 = \frac{1}{4} \left[ \left(\frac{3}{2}(1) - 4\right)(2) g_3 + \left(\frac{3}{2}(3) - 4\right)(1) g_1 \right] = \frac{1}{4} \left[ (-5)\left(\frac{1}{2}\right) + \frac{1}{2}(1) \right] = -\frac{1}{2}$.
  *(Self-check via Binomial Expansion: $(1 + (2x + x^3))^{1/2} = 1 + \frac{1}{2}(2x + x^3) - \frac{1}{8}(4x^2 + 4x^4) + \frac{1}{16}(8x^3) - \frac{5}{128}(16x^4) + O(x^5) = 1 + x - \frac{1}{2}x^2 + x^3 - \frac{9}{8}x^4 + O(x^5)$.\) Wait: why did $g_2 = 0$ in the line above? Because $\frac{1}{2}\left(\frac{3}{2} - 2\right)(2)(1) = \frac{1}{2}\left(-\frac{1}{2}\right)(2) = -\frac{1}{2} \neq 0$! Let's re-evaluate $n=2, 3, 4$ with $g_2 = -1/2$:
  - $n = 2$: $g_2 = \frac{1}{2} \left(\frac{3}{2} - 2\right)(2)(1) = -\frac{1}{2}$.
  - $n = 3$: $g_3 = \frac{1}{3} \left[ \left(\frac{3}{2} - 3\right)(2)\left(-\frac{1}{2}\right) + \left(\frac{9}{2} - 3\right)(1)(1) \right] = \frac{1}{3}\left[ \frac{3}{2} + \frac{3}{2} \right] = 1$.
  - $n = 4$: $g_4 = \frac{1}{4} \left[ \left(\frac{3}{2} - 4\right)(2)(1) + \left(\frac{9}{2} - 4\right)(1)(1) \right] = \frac{1}{4}\left[ -5 + \frac{1}{2} \right] = -\frac{9}{8}$.
  Thus $G(x) = 1 + x - \frac{1}{2}x^2 + x^3 - \frac{9}{8}x^4 + O(x^5)$, matching the Taylor expansion term-for-term!)*\)
  ```
- **Audit Findings**:
  1. Line 432 writes $-\frac{1}{2}(1) = 0$, then argues with itself (`wait: ...`), then lines 433–434 compute wrong values $g_3 = 1/2, g_4 = -1/2$ using $g_2 = 0$, and then lines 435–438 re-compute $g_2, g_3, g_4$ while leaving two stray banned `\)` delimiters on lines 435 and 438!
  2. Notice that the pre-existing source file `iter_41_to_45_ode_sparse_cdq_relaxed.md` (lines 191–204) already had the completely clean, error-free trace.
- **Drop-In Replacement for Lines 430–438**:
  ```markdown
  - $n = 0$: $g_0 = f_0^{1/2} = 1$.
  - $n = 1$: $g_1 = \frac{1}{1} \left( \frac{3}{2}(1) - 1 \right) (2) g_0 = \frac{1}{2} (2)(1) = 1$.
  - $n = 2$: $g_2 = \frac{1}{2} \left[ \left(\frac{3}{2}(1) - 2\right)(2) g_1 \right] = \frac{1}{2} \left(-\frac{1}{2}\right)(2)(1) = -\frac{1}{2}$.
  - $n = 3$: $g_3 = \frac{1}{3} \left[ \left(\frac{3}{2}(1) - 3\right)(2) g_2 + \left(\frac{3}{2}(3) - 3\right)(1) g_0 \right] = \frac{1}{3} \left[ \left(-\frac{3}{2}\right)(2)\left(-\frac{1}{2}\right) + \frac{3}{2}(1)(1) \right] = \frac{1}{3}\left[\frac{3}{2} + \frac{3}{2}\right] = 1$.
  - $n = 4$: $g_4 = \frac{1}{4} \left[ \left(\frac{3}{2}(1) - 4\right)(2) g_3 + \left(\frac{3}{2}(3) - 4\right)(1) g_1 \right] = \frac{1}{4} \left[ \left(-\frac{5}{2}\right)(2)(1) + \frac{1}{2}(1)(1) \right] = \frac{1}{4}\left[-5 + \frac{1}{2}\right] = -\frac{9}{8}$.
  *(Self-check via Binomial Expansion: $(1 + (2x + x^3))^{1/2} = 1 + \frac{1}{2}(2x + x^3) - \frac{1}{8}(4x^2 + 4x^4) + \frac{1}{16}(8x^3) - \frac{5}{128}(16x^4) + O(x^5) = 1 + x - \frac{1}{2}x^2 + x^3 - \frac{9}{8}x^4 + O(x^5)$, matching $G(x)$ term-for-term!)*
  ```

---

### Bug 3 [MATH INCONSISTENCY + STREAM-OF-CONSCIOUSNESS]: Section 3.3 Worked Demonstrations 2 & 3 (Lines 360–388)

- **Location**: [cohort3_wave_5a_ode_sparse_cdq_relaxed.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L360-L388)
- **Audit Findings**:
  1. **Demonstration 3 (Lines 360–368, `QOJ #60 Chinese Elephant Chess`)**:
     Line 361 defines $F(x) = (1-x)^{-1/2} \exp\left(\frac{x^2}{2(1-x)}\right)$, and Line 362 claims we can factor $F(x) = e^{-x/(1-x)} G(x)$ where $G(x) = (1-x)^{-1/2} \exp\left(\frac{x}{2(1-x)}\right)$.
     **Algebraic Error**: $\frac{x}{2(1-x)} - \frac{x}{1-x} = -\frac{x}{2(1-x)} \neq \frac{x^2}{2(1-x)}$!
     Specifically:
     - Since $\frac{x^2}{2(1-x)} = -\frac{x}{2} + \frac{x}{2(1-x)}$, the function $F_1(x) = (1-x)^{-1/2}\exp\left(\frac{x^2}{2(1-x)}\right)$ factors as $F_1(x) = e^{-x/2} G(x)$.
     - On the other hand, if we already stripped $e^{x/2 + x^2/4}$ so the remaining factor is $F_2(x) = (1-x)^{-1/2}\exp\left(-\frac{x}{2(1-x)}\right)$, then since $-\frac{x}{2(1-x)} = -\frac{x}{1-x} + \frac{x}{2(1-x)}$, it factors as $F_2(x) = e^{-x/(1-x)} G(x)$.
     Both gauge transformations reduce to the exact same core D-finite series $G(x) = (1-x)^{-1/2}\exp\left(\frac{x}{2(1-x)}\right)$ satisfying $2(1-x)^2 G'(x) = (2-x) G(x) \implies 2n g_n = (4n-2) g_{n-1} - (2n-3) g_{n-2}$. We should state both identities accurately!
  2. **Demonstration 2 (Lines 380–388, Substitution of Dependent/Independent Variable)**:
     Lines 380–385 start with a non-Catalan equation $F'(x) = \frac{F(x)^2}{1 - x F(x)}$, derive $\frac{d}{dy}[y G(y)] = \frac{1}{y}$, and then on line 385 abruptly write `Wait—for the algebraic tree equation $F(x) = 1 + x F(x)^2$, differentiating gives...`. We must remove the false start and present the clean derivation for $(1 - 2x F(x)) F'(x) = F(x)^2$ directly.
- **Drop-In Replacement for Lines 360–388**:
  ```markdown
  #### Worked Demonstration 1: Gauge Transformation on D-Finite Graph EGF (`QOJ #60 — Chinese Elephant Chess`)
  Suppose we need the coefficients of the core cycle-path EGF $F(x) = (1-x)^{-1/2} \exp\left(\frac{x^2}{2(1-x)}\right)$ (or, after stripping 1-cycles and 2-cycles via $e^{-x/2 - x^2/4}$, the companion series $\widetilde{F}(x) = (1-x)^{-1/2} \exp\left(-\frac{x}{2(1-x)}\right)$) up to $N = 10^7$.
  1. **Gauge Factorization**: Define the canonical D-finite kernel
     $$G(x) = (1-x)^{-1/2} \exp\left(\frac{x}{2(1-x)}\right)$$
     Using the identities $\frac{x^2}{2(1-x)} = -\frac{x}{2} + \frac{x}{2(1-x)}$ and $-\frac{x}{2(1-x)} = -\frac{x}{1-x} + \frac{x}{2(1-x)}$, both series reduce immediately to $G(x)$ via elementary multipliers:
     $$F(x) = e^{-x/2} G(x), \qquad \widetilde{F}(x) = e^{-x/(1-x)} G(x)$$
  2. **Logarithmic Differentiation of $G(x)$**:
     $$\ln G(x) = -\frac{1}{2}\ln(1-x) + \frac{x}{2(1-x)} \implies \frac{G'(x)}{G(x)} = \frac{1}{2(1-x)} + \frac{1}{2(1-x)^2} = \frac{2-x}{2(1-x)^2}$$
  3. **Linear ODE & 3-Term Recurrence**: Clearing denominators gives:
     $$2(1 - 2x + x^2) G'(x) = (2 - x) G(x)$$
     Extracting $[x^{n-1}]$ yields the $O(1)$-per-term recurrence:
     $$2n g_n - 4(n-1) g_{n-1} + 2(n-2) g_{n-2} = 2 g_{n-1} - g_{n-2} \implies 2n g_n = (4n - 2) g_{n-1} - (2n - 3) g_{n-2}$$
     From $g_0, \dots, g_N$, a single linear scan (or single convolution with $e^{-x/2}$) recovers $[x^N]F(x)$ in $O(N)$ time, completely avoiding $O(N \log N)$ polynomial `exp` and `sqrt`.

  #### Worked Demonstration 2: Dependent Variable Substitution on a Non-Standard Riccati ODE
  Consider solving $F'(x) = 1 + 2x F(x) + F(x)^2$ with $F(0) = 0$.
  1. **Ansatz**: Apply the Riccati-to-Second-Order transformation $F(x) = -\frac{U'(x)}{U(x)}$ with $U(0) = 1, U'(0) = -F(0) = 0$.
  2. **Substitution**: Since $F'(x) = -\frac{U''}{U} + \left(\frac{U'}{U}\right)^2$, the quadratic term $\left(\frac{U'}{U}\right)^2$ cancels $F(x)^2$ identically:
     $$-\frac{U''(x)}{U(x)} = 1 - 2x \frac{U'(x)}{U(x)} \implies U''(x) - 2x U'(x) + U(x) = 0$$
  3. **Coefficient Extraction**: Extracting $[x^n]$ from $U''(x) - 2x U'(x) + U(x) = 0$ gives:
     $$(n+2)(n+1) u_{n+2} - 2n u_n + u_n = 0 \implies u_{n+2} = \frac{2n - 1}{(n+2)(n+1)} u_n$$
     Since $u_0 = 1$ and $u_1 = 0$, all odd coefficients vanish and $U(x) = 1 - \frac{1}{2}x^2 - \frac{1}{8}x^4 - \frac{7}{240}x^6 - \dots$ is computed in $O(N)$ time, after which $F(x) = -U'(x) U(x)^{-1} \pmod{x^N}$ requires only a single polynomial inversion.

  #### Worked Demonstration 3: Independent Variable Substitution via Compositional Inverse
  Consider the differential form of the binary tree equation $(1 - 2x F(x)) F'(x) = F(x)^2$ with $F(0) = 1$.
  1. **Variable Swap**: Treat $y = x F(x)$ as the new independent variable, and express $x$ as a function of $y$. Since $F(x) = \frac{y}{x}$, differentiating $y = x F(x)$ with respect to $x$ gives $\frac{dy}{dx} = F(x) + x F'(x)$.
  2. **Rewriting the ODE**: Multiplying $(1 - 2y) F'(x) = F(x)^2$ by $x$ yields $(1 - 2y)\left(\frac{dy}{dx} - F(x)\right) = y F(x)$, which simplifies to $(1 - 2y) \frac{dy}{dx} = (1 - y) F(x) = (1 - y) \frac{y}{x}$.
  3. **Separable Integration**: Separating variables $x$ and $y$ gives:
     $$\frac{dx}{x} = \frac{1 - 2y}{y(1 - y)} \, dy = \left(\frac{1}{y} - \frac{1}{1 - y}\right) dy \implies \ln x = \ln\big(y(1 - y)\big) \implies x = y(1 - y)$$
     Since $y = x F(x)$ satisfies the quadratic $y^2 - y + x = 0$ with $y(0) = 0$, we immediately recover $F(x) = \frac{1 - \sqrt{1 - 4x}}{2x} = \sum_{n=0}^{\infty} C_n x^n$.
  ```

---

### Bug 4 [TRUNCATED DERIVATION + STREAM-OF-CONSCIOUSNESS]: Section 5.2 Engine 3 (`EI's Direct Differential-Residue Method`, Lines 651–665)

- **Location**: [cohort3_wave_5a_ode_sparse_cdq_relaxed.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L651-L665)
- **Current Erroneous Text (Lines 651–665)**:
  ```markdown
  Instead of computing the 2D rational function $R(x, y)$ and its univariate diagonal, we can stay strictly inside 1D formal Laurent series and use **Creative Telescoping by Parts**:
  1. Write the target sum as a single residue in $x$:
     $$S_n = \sum_{k=0}^n \binom{n}{k} \binom{n+k}{k} c^k = [x^n] (1+x)^n (1 + cx(1+x)^{-1})^n \dots \text{ wait: } \binom{n}{k}\binom{n+k}{k} = \binom{n}{k}[x^k](1+x)^{n+k} \text{ does not have a fixed exponent } [x^n].$$
     Instead, use $\binom{n}{k} = [x^{n-k}](1+x)^n$ and $\binom{n+k}{k} = [y^k](1-y)^{-(n+1)}$, OR write $\binom{n+k}{k} = (-1)^k \binom{-n-1}{k} = [x^k](1-x)^{-(n+1)}$:
     $$S_n = \sum_{k=0}^n [x^{n-k}](1+x)^n \cdot [t^k](1-t)^{-(n+1)} c^k = [x^n] (1+x)^n (1 - cx)^{-(n+1)} = [x^{-1}] \frac{(1+x)^n}{x^{n+1} (1-cx)^{n+1}}$$
  2. Define the kernel $W_n(x) = \frac{(1+x)^n}{x^{n+1}(1-cx)^{n+1}}$, so $S_n = [x^{-1}] W_n(x)$. Notice that $W_n(x) = \frac{1}{x(1-cx)} Q(x)^n$ where $Q(x) = \frac{1+x}{x(1-cx)}$.
  3. Differentiate $Q(x)^n$ with respect to $x$:
     $$\frac{d}{dx} \big[ Q(x)^n \big] = n Q(x)^{n-1} Q'(x) = n Q(x)^{n-1} \frac{cx^2 + 2cx - 1}{x^2 (1-cx)^2}$$
     Since $[x^{-1}] \frac{d}{dx}[\dots] = 0$, any linear combination of $W_{n+1}(x), W_n(x), W_{n-1}(x)$ that equals a total derivative $\frac{d}{dx}[P(x) Q(x)^n]$ has zero residue!
     Specifically, express $\frac{cx^2 + 2cx - 1}{x(1-cx)}$ as a linear combination of $Q(x)$, $1$, and $Q(x)^{-1}$... Wait: rewriting each power of $x$ via $x(1-cx) Q(x) = 1+x$ and extracting $[x^{-1}] = 0$ immediately produces the 3-term recurrence:
     $$(n+1) S_{n+1} - (2n+1)(1+2c) S_n + n S_{n-1} = 0$$
     without ever introducing a second variable $y$ or solving a quadratic root $y_0(s)$!
  ```
- **Mathematical Audit**:
  1. On line 654, the text gets confused trying to represent $\binom{n+k}{k}$ with a fixed coefficient extraction and writes `... wait: ... does not have a fixed exponent [x^n]`. In fact, by symmetry $\binom{n+k}{k} = \binom{n+k}{n} = [x^n](1+x)^{n+k}$, which **does** have a fixed exponent $[x^n]$!
     Using $\binom{n+k}{k} = [x^n](1+x)^{n+k}$ gives the Laurent trinomial representation:
     $$S_n = \sum_{k=0}^n \binom{n}{k} c^k [x^n](1+x)^{n+k} = [x^n](1+x)^n\big(1 + c(1+x)\big)^n = [x^0] Q(x)^n = [x^{-1}] x^{-1} Q(x)^n$$
     where $Q(x) = \frac{(1+x)(1+c+cx)}{x} = (1+c)x^{-1} + (1+2c) + cx$.
  2. Furthermore, on lines 659–661, the text leaves the algebra unfinished (`... Wait: rewriting each power ...`). With $Q(x) = A x^{-1} + B + C x$ (where $A = 1+c, B = 1+2c, C = c$), the creative telescoping certificate is an **exact 3-line algebraic identity**:
     Since $x Q'(x) = Cx - Ax^{-1}$, we have $\frac{d}{dx}[x Q'(x)] = C + Ax^{-2} = x^{-1}(Q(x) - B)$ and $(x Q'(x))^2 = (Q(x) - B)^2 - 4AC = Q(x)^2 - 2B Q(x) + (B^2 - 4AC)$. Differentiating $x Q'(x) Q(x)^n$ gives:
     $$\frac{d}{dx}\Big[x Q'(x) Q(x)^n\Big] = (n+1) W_{n+1}(x) - (2n+1) B W_n(x) + n(B^2 - 4AC) W_{n-1}(x)$$
     where $W_n(x) = x^{-1} Q(x)^n$ and $B^2 - 4AC = (1+2c)^2 - 4c(1+c) = 1$!
- **Drop-In Replacement for Lines 651–665**:
  ```markdown
  Instead of computing the 2D rational function $R(x, y)$ and its univariate diagonal, we can stay strictly inside 1D formal Laurent series and use **Creative Telescoping by Parts**:
  1. **Single-Variable Laurent Trinomial Representation**: Using binomial symmetry $\binom{n+k}{k} = \binom{n+k}{n} = [x^n](1+x)^{n+k}$ (where the extracted power $[x^n]$ is independent of $k$), we fold the sum over $k$ via the Binomial Theorem:
     $$S_n = \sum_{k=0}^n \binom{n}{k} c^k [x^n](1+x)^{n+k} = [x^n] (1+x)^n \big(1 + c(1+x)\big)^n = [x^{-1}] x^{-1} Q(x)^n$$
     where $Q(x) = \frac{(1+x)(1+c+cx)}{x} = A x^{-1} + B + C x$ is a Laurent trinomial with $A = 1+c$, $B = 1+2c$, and $C = c$.
  2. **Exact Differential-Residue Certificate**: Define $W_n(x) = x^{-1} Q(x)^n$, so $S_n = [x^{-1}] W_n(x)$. Observe that $Q(x) - B = C x + A x^{-1}$ and $x Q'(x) = C x - A x^{-1}$. These two expressions satisfy two fundamental identities:
     $$\frac{d}{dx}\big[x Q'(x)\big] = C + A x^{-2} = x^{-1}\big(Q(x) - B\big)$$
     $$\big(x Q'(x)\big)^2 = (C x - A x^{-1})^2 = (C x + A x^{-1})^2 - 4AC = \big(Q(x) - B\big)^2 - 4AC = Q(x)^2 - 2B Q(x) + (B^2 - 4AC)$$
  3. **Creative Telescoping Step**: Differentiate the single product $x Q'(x) Q(x)^n$ with respect to $x$:
     $$\begin{aligned}
     \frac{d}{dx}\Big[x Q'(x) Q(x)^n\Big] &= \frac{d}{dx}\big[x Q'(x)\big] Q(x)^n + n \big(x Q'(x)\big) Q'(x) Q(x)^{n-1} \\
     &= x^{-1}\big(Q(x) - B\big) Q(x)^n + n x^{-1}\big(x Q'(x)\big)^2 Q(x)^{n-1} \\
     &= (n+1) x^{-1} Q(x)^{n+1} - (2n+1) B x^{-1} Q(x)^n + n(B^2 - 4AC) x^{-1} Q(x)^{n-1} \\
     &= (n+1) W_{n+1}(x) - (2n+1) B W_n(x) + n(B^2 - 4AC) W_{n-1}(x)
     \end{aligned}$$
     Since $[x^{-1}] \frac{d}{dx}[\dots] = 0$ and $B^2 - 4AC = (1+2c)^2 - 4(1+c)c = 1$, extracting $[x^{-1}]$ on both sides immediately yields:
     $$(n+1) S_{n+1} - (2n+1)(1+2c) S_n + n S_{n-1} = 0$$
     without ever introducing a second variable $y$ or solving a quadratic root $y_0(s)$! *(Bonus: this exact same 3-line proof establishes the 3-term P-recursive recurrence for any central trinomial power $[x^n](A + Bx + Cx^2)^n$.)*
  ```

---

### Bug 5 [TRUNCATED DERIVATION + FALSE 3-TERM CLAIM]: Section 7, Problem 12 (`Codeforces 755G — PolandBall and Many Other Balls`, Lines 1009–1018)

- **Location**: [cohort3_wave_5a_ode_sparse_cdq_relaxed.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L1009-L1018)
- **Current Erroneous Text (Lines 1009–1018)**:
  ```markdown
  3. **ODE Reduction**: Let $\Delta(y) = y^2 + 6y + 1$ and $A(y) = \frac{1 + y + \sqrt{\Delta(y)}}{2}$. Differentiating $A(y)$ gives:
     $$A'(y) = \frac{1}{2}\left(1 + \frac{y+3}{\sqrt{\Delta(y)}}\right) = \frac{\sqrt{\Delta(y)} + y + 3}{2\sqrt{\Delta(y)}}$$
     Notice that $\sqrt{\Delta(y)} + y + 3$... actually, $A(y)$ satisfies $A(y)^2 - (1+y)A(y) - y = 0$.
     Even cleaner: $P_n(y) = [x^n] \frac{1}{1 - (1+y)x - yx^2} = \sum_{j=0}^{\lfloor n/2 \rfloor} \binom{n-j}{j} y^j (1+y)^{n-2j}$.
     By the Diagonal / D-Finite theorem on $R(x, y) = \frac{1}{1 - (1+y)x - yx^2}$, or by differentiating $G_n(y) = A(y)^{n+1} \Delta(y)^{-1/2}$:
     $$(y^2 + 6y + 1) P_n'(y) = \dots$$
     Wait: even simpler, write the bivariate recurrence $F_n(y) = (1+y)F_{n-1}(y) + y F_{n-2}(y)$ and combine it with the partial derivative $\frac{\partial}{\partial y} \frac{1}{1-(1+y)x-yx^2} = \frac{x+x^2}{(1-(1+y)x-yx^2)^2}$ to obtain the exact 3-term P-recursive recurrence in $k$ for $a_k = [y^k] F_n(y)$ directly in $O(K)$ time!
     Specifically, $a_k = \sum_{j=0}^k \binom{n-j}{j} \binom{n-2j}{k-j} = \sum_{j=0}^k \binom{k}{j} \binom{n-k}{j} 2^j$ (by Vandermonde-like rearrangement, $a_k$ is a Jacobi/Delannoy polynomial evaluation), which satisfies the 4-term (or 3-term after shift) linear recurrence...
  ```
- **Mathematical Audit**:
  1. Lines 1011, 1014, 1015, and 1018 contain unfinished sentences (`\dots`, `Wait: even simpler...`, `satisfies the 4-term (or 3-term after shift) linear recurrence...`) without ever writing out the actual recurrence!
  2. **Mathematical Fact Check**:
     - Let $r_{1,2}(y) = \frac{1 + y \pm \sqrt{\Delta(y)}}{2}$ where $\Delta(y) = y^2 + 6y + 1$. Then $\sqrt{\Delta(y)} \, r_1'(y) = \frac{\sqrt{\Delta(y)} + y + 3}{2} = r_1(y) + 1$ and $\sqrt{\Delta(y)} \, r_2'(y) = -\big(r_2(y) + 1\big)$.
     - Differentiating $\sqrt{\Delta(y)} F_n(y) = r_1(y)^{n+1} - r_2(y)^{n+1}$ and using $r_1(y)^{n+1} + r_2(y)^{n+1} = (1+y)F_n(y) + 2y F_{n-1}(y)$ and $r_1(y)^n + r_2(y)^n = 2F_n(y) - (1+y)F_{n-1}(y)$ gives the **exact coupled first-order differential relation**:
       $$(y^2 + 6y + 1) F_n'(y) = n(y + 3) F_n(y) + (n + 1)(y - 1) F_{n-1}(y)$$
     - Furthermore, eliminating $F_{n-1}(y)$ (or applying Zeilberger creative telescoping to $a_k = \sum_{j=0}^k \binom{k}{j}\binom{n-k}{j} 2^j$) yields the **exact standalone 4-term P-recursive recurrence** for $a_k = [y^k] F_n(y)$ (for $m = k - 1 \ge 0$):
       $$(m + 1)(n - m) a_{m+1} = \big(5m^2 - 5(n-1)m + n(2n-1)\big) a_m - \big(5m^2 - 5(n+3)m + (n+2)(2n+5)\big) a_{m-1} + (m - 1)(n + 2 - m) a_{m-2}$$
       *(Note: no standalone 3-term recurrence in $k$ exists for $a_k$; 3 shifts only exist when tracking the coupled pair $(F_n(y), F_{n-1}(y))$ or after changing variables to $z = \frac{y}{(1+y)^2}$ in $F_n(y) = (1+y)^n \sum_{j=0}^{\lfloor n/2 \rfloor} \binom{n-j}{j} z^j$.)*
- **Drop-In Replacement for Lines 1009–1025**:
  ```markdown
  3. **ODE Reduction & Exact $O(K)$ P-Recursive Recurrences**: Let $\Delta(y) = y^2 + 6y + 1$. From $r_{1,2}(y) = \frac{1 + y \pm \sqrt{\Delta(y)}}{2}$, differentiating with respect to $y$ gives the remarkable identity:
     $$\sqrt{\Delta(y)} \, r_1'(y) = \frac{\sqrt{\Delta(y)} + y + 3}{2} = r_1(y) + 1, \qquad \sqrt{\Delta(y)} \, r_2'(y) = -\big(r_2(y) + 1\big)$$
     - **Method A ($O(K \log K)$ Radical FPS)**: Compute $\Delta(y) = 1 + 6y + y^2$, $S(y) = \sqrt{\Delta(y)} \pmod{y^{K+1}}$ via `fps_sqrt` (or $O(K)$ sparse sqrt), $r_1(y) = \frac{1 + y + S(y)}{2}$, and $F_n(y) \equiv S(y)^{-1} \exp\big((n+1) \ln r_1(y)\big) \pmod{y^{K+1}}$ in $O(K \log K)$ time.
     - **Method B ($O(K)$ Coupled First-Order ODE / Lucas-Delannoy System)**: Differentiating $\sqrt{\Delta(y)} F_n(y) = r_1(y)^{n+1} - r_2(y)^{n+1}$ and substituting the Lucas-type identities $r_1^{n+1} + r_2^{n+1} = (1+y)F_n(y) + 2y F_{n-1}(y)$ and $r_1^n + r_2^n = 2F_n(y) - (1+y)F_{n-1}(y)$ eliminates all radicals:
       $$(y^2 + 6y + 1) F_n'(y) = n(y + 3) F_n(y) + (n + 1)(y - 1) F_{n-1}(y)$$
     - **Method C ($O(K)$ Standalone 4-Term P-Recursive Recurrence for $a_k = [y^k] F_n(y)$)**: Setting $u = x$ and $v = xy$ in $F(x, y) = \frac{1}{1 - x - xy - x^2 y} = \frac{1}{1 - u - v - uv}$ identifies $a_k = [x^n y^k] F(x, y) = [u^{n-k} v^k]\frac{1}{1 - u - v - uv} = D(n-k, k) = \sum_{j=0}^k \binom{k}{j}\binom{n-k}{j} 2^j$ as the anti-diagonal Delannoy number. Eliminating $F_{n-1}(y)$ from Method B (or writing $F_n(y) = (1+y)^n G_n\big(\frac{y}{(1+y)^2}\big)$ where $G_n(z) = \sum_{j \ge 0} \binom{n-j}{j} z^j$ satisfies a hypergeometric 2nd-order ODE) yields the exact 4-term recurrence for $a_{m+1}$ ($m = k-1 \ge 0$, with $a_0 = 1$):
       $$(m + 1)(n - m) a_{m+1} = \big(5m^2 - 5(n-1)m + n(2n-1)\big) a_m - \big(5m^2 - 5(n+3)m + (n+2)(2n+5)\big) a_{m-1} + (m - 1)(n + 2 - m) a_{m-2}$$
       Using precomputed linear modular inverses $\text{inv}[1 \dots K]$, this computes all $a_0, a_1, \dots, a_K$ in $O(K)$ time and $O(K)$ space!
  ```

---

## 3. Part II: Information Loss vs. Source Cohorts (With Complete Drop-In Restorations)

### Omission 1: Missing C++ Reference Kernel `solve_first_order_ode` (Newton + Integrating Factor) in Section 3.2.3

- **Source Location**: `cohort2_iter_93_to_97_ode_sparse_cdq_relaxed.md`, Section 94.1, Lines 255–280.
- **Target Location to Insert**: [cohort3_wave_5a_ode_sparse_cdq_relaxed.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L305-L315) (at the end of Section 3.2.3).
- **Drop-In Restoration Text**:
  ````markdown
  ```cpp
  // General First-Order Non-Linear ODE Solver: F'(x) = G(x, F(x)) mod x^N, F(0) = f0
  // Uses Newton's Method + Integrating Factor in O(N log N) time (Nyaan's Library style)
  // eval_G(F, d) must return {G(x, F(x)) mod x^d, (dG/dy)(x, F(x)) mod x^d}
  template <typename EvalFunc>
  Poly solve_first_order_ode(int N, long long f0, EvalFunc eval_G) {
      Poly F = {f0 % MOD};
      for (int d = 1; d < N; d <<= 1) {
          int next_d = min(N, 2 * d);
          auto [G_val, G_y] = eval_G(F, next_d);
          // 1. Integrating factor: I(x) = exp(-integral(G_y dx)) mod x^{next_d}
          Poly minus_Gy(next_d, 0);
          for (int i = 0; i < (int)G_y.size() && i < next_d; ++i)
              minus_Gy[i] = (MOD - G_y[i]) % MOD;
          Poly int_minus_Gy = fps_integ(minus_Gy);
          int_minus_Gy.resize(next_d, 0);
          Poly I = fps_exp(int_minus_Gy, next_d);
          Poly I_inv = fps_inv(I, next_d);
          // 2. Residual: R(x) = G(x, F_k) - F_k'(x) + G_y(x, F_k) * F_k(x) mod x^{next_d}
          Poly F_der = fps_deriv(F);
          Poly Gy_F = multiply(G_y, F);
          Gy_F.resize(next_d, 0);
          Poly R(next_d, 0);
          for (int i = 0; i < next_d; ++i) {
              long long v = (i < (int)G_val.size() ? G_val[i] : 0);
              if (i < (int)F_der.size()) v = (v - F_der[i] + MOD) % MOD;
              if (i < (int)Gy_F.size()) v = (v + Gy_F[i]) % MOD;
              R[i] = v;
          }
          // 3. Linear solve: F_{k+1} = I_inv * (f0 + integral(I * R dx)) mod x^{next_d}
          Poly IR = multiply(I, R);
          IR.resize(next_d - 1, 0);
          Poly int_IR = fps_integ(IR);
          int_IR.resize(next_d, 0);
          int_IR[0] = (int_IR[0] + f0) % MOD;
          F = multiply(I_inv, int_IR);
          F.resize(next_d, 0);
      }
      return F;
  }
  ```
  ````

---

### Omission 2: Five Missing Hand-Checkable Toy Traces ($n \le 4$) Across Sections 3, 4, and 5

1. **Toy Trace A (Autonomous ODE $F'(x) = (1 + F(x))^2, F(0) = 0$)** — from `cohort1_iter_41_to_45` Lines 465–471.
   - **Insert in Section 3.3.1 (after Line 326)**:
     ```markdown
     - **Hand-Checkable Toy Trace ($n \le 4$)**: Solve $F'(x) = (1 + F(x))^2$ with $F(0) = 0$ via compositional inverse $G(y) = \int_0^y \frac{dt}{(1+t)^2}$:
       1. Expand $\frac{1}{(1+t)^2} = 1 - 2t + 3t^2 - 4t^3 + O(t^4)$.
       2. Term-by-term integration gives $G(y) = y - y^2 + y^3 - y^4 + O(y^5) = \frac{y}{1+y}$.
       3. Solving $x = \frac{y}{1+y}$ gives $F(x) = y = \frac{x}{1-x} = x + x^2 + x^3 + x^4 + O(x^5)$.
     ```
2. **Toy Trace B (Change of Independent Variable $u = \ln(1+x)$ on Euler-Cauchy ODE)** — from `cohort1_iter_41_to_45` Lines 505–521 & `cohort2_iter_93_to_97` Lines 410–425.
   - **Insert in Section 3.3.3 (after Line 356)**:
     ```markdown
     - **Hand-Checkable Toy Trace ($n \le 4$)**: Solve $(1+x)^2 F''(x) + (1+x) F'(x) - F(x) = 0$ with $F(0) = 1, F'(0) = 2$:
       1. Substitute $u = \ln(1+x)$, so $(1+x)\frac{d}{dx} = \frac{d}{du}$ and $(1+x)^2 F''(x) + (1+x) F'(x) = G''(u)$ where $G(u) = F(e^u - 1)$.
       2. The variable-coefficient ODE collapses to $G''(u) - G(u) = 0$ with $G(0) = 1, G'(0) = 2$, yielding $G(u) = \cosh(u) + 2\sinh(u) = \frac{3}{2}e^u - \frac{1}{2}e^{-u}$.
       3. Substituting back $e^u = 1+x$ gives $F(x) = \frac{3}{2}(1+x) - \frac{1}{2}(1+x)^{-1} = 1 + 2x - \frac{1}{2}x^2 + \frac{1}{2}x^3 - \frac{1}{2}x^4 + O(x^5)$.
     ```
3. **Toy Trace C (Sparse Exponential $\exp(x + 2x^3) \pmod{x^5}$)** — from `cohort1_iter_41_to_45` Lines 737–744 & `cohort2_iter_93_to_97` Lines 681–693.
   - **Insert in Section 4.2 (after Line 438)**:
     ```markdown
     #### Hand-Checkable Trace 2: Compute $\exp(x + 2x^3) \pmod{x^5}$
     Here $F(x) = x + 2x^3$ has $f_0 = 0$ and two nonzero terms: $(i_1 = 1, f_1 = 1)$ and $(i_2 = 3, f_3 = 2)$. Using $g_0 = 1$ and $g_n = \frac{1}{n} \sum_{i \in \{1, 3\}} i \, f_i \, g_{n-i}$:
     - $n = 1$: $g_1 = \frac{1}{1}\big(1 \cdot 1 \cdot g_0\big) = 1$.
     - $n = 2$: $g_2 = \frac{1}{2}\big(1 \cdot 1 \cdot g_1\big) = \frac{1}{2}$.
     - $n = 3$: $g_3 = \frac{1}{3}\big(1 \cdot 1 \cdot g_2 + 3 \cdot 2 \cdot g_0\big) = \frac{1}{3}\left(\frac{1}{2} + 6\right) = \frac{13}{6}$.
     - $n = 4$: $g_4 = \frac{1}{4}\big(1 \cdot 1 \cdot g_3 + 3 \cdot 2 \cdot g_1\big) = \frac{1}{4}\left(\frac{13}{6} + 6\right) = \frac{49}{24}$.
     *(Self-check: $\exp(x)\exp(2x^3) = \left(1 + x + \frac{1}{2}x^2 + \frac{1}{6}x^3 + \frac{1}{24}x^4\right)(1 + 2x^3) + O(x^5) = 1 + x + \frac{1}{2}x^2 + \frac{13}{6}x^3 + \frac{49}{24}x^4 + O(x^5)$.)*
     ```
4. **Toy Trace D (Parametric Binomial Sum $S_n = \sum_{k=0}^n \binom{n}{k}\binom{n+k}{k} c^k$ for $c = 2, n \le 4$)** — from `cohort2_iter_93_to_97` Lines 832–843.
   - **Insert in Section 5.2 (after Line 665)**:
     ```markdown
     #### Hand-Checkable Numerical Trace ($c = 2, n \le 4$)
     For $c = 2$, $1 + 2c = 5$, so the recurrence is $(n+1) S_{n+1} = 5(2n+1) S_n - n S_{n-1}$ with $S_0 = 1$:
     - $n = 0$: $S_0 = \binom{0}{0}\binom{0}{0} 2^0 = 1$.
     - $n = 1$: $1 \cdot S_1 = 5(1) S_0 - 0 = 5$ (Direct check: $\binom{1}{0}\binom{1}{0} + \binom{1}{1}\binom{2}{1} 2^1 = 1 + 4 = 5$).
     - $n = 2$: $2 S_2 = 5(3) S_1 - 1 \cdot S_0 = 75 - 1 = 74 \implies S_2 = 37$ (Direct check: $1 + 6(2) + 6(4) = 37$).
     - $n = 3$: $3 S_3 = 5(5) S_2 - 2 S_1 = 25(37) - 10 = 915 \implies S_3 = 305$ (Direct check: $1 + 12(2) + 30(4) + 20(8) = 305$).
     - $n = 4$: $4 S_4 = 5(7) S_3 - 3 S_2 = 35(305) - 111 = 10564 \implies S_4 = 2641$.
     ```

---

### Omission 3: Missing Summary Table of Classic Binomial Sums & Diagonal ODEs + Missing Derivation of $[x^n](1+ax)^n(1+bx)^n$ in Section 5.4

- **Source Locations**:
  - `cohort1_iter_41_to_45_ode_sparse_cdq_relaxed.md`, Section 44.3, Lines 810–834 (Derivation 1: $a_n = [x^n](1+ax)^n(1+bx)^n$).
  - `cohort2_iter_93_to_97_ode_sparse_cdq_relaxed.md`, Section 96.5, Lines 847–855 (Summary Table of Classic Binomial Sums & Their Diagonal ODEs).
- **Target Location to Insert**: [cohort3_wave_5a_ode_sparse_cdq_relaxed.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L708-L711) (at the end of Section 5.4).
- **Drop-In Restoration Text**:
  ```markdown
  #### Derivation 4: Generalized Franel / Product Powers $a_n = [x^n](1+ax)^n(1+bx)^n = \sum_{k=0}^n \binom{n}{k}^2 a^k b^{n-k}$
  1. **Diagonal Reduction**: Write $a_n = [x^n y^n] \frac{1}{1 - y(1+ax)(1+bx)}$. Substituting $s = xy$ gives $Q(y) = y^2 - (1 - (a+b)s)y + ab s^2$, with discriminant:
     $$\Delta(s) = \big(1 - (a+b)s\big)^2 - 4ab s^2 = 1 - 2(a+b)s + (a-b)^2 s^2$$
  2. **First-Order ODE & 3-Term Recurrence**: Hence $D(s) = \sum_{n=0}^{\infty} a_n s^n = \Delta(s)^{-1/2}$ satisfies $2\Delta(s) D'(s) + \Delta'(s) D(s) = 0$:
     $$\big(1 - 2(a+b)s + (a-b)^2 s^2\big) D'(s) = \big((a+b) - (a-b)^2 s\big) D(s)$$
     Extracting $[s^{n-1}]$ yields the $O(1)$-per-term recurrence:
     $$n a_n = (2n - 1)(a + b) a_{n-1} - (n - 1)(a - b)^2 a_{n-2}$$

  #### Summary Table of Classic Binomial Sums & Their Diagonal ODEs

  | Target Sequence $a_n$ | Bivariate Rational Denominator $Q(x, y)$ | Discriminant $\Delta(s)$ | Resulting $O(1)$-Per-Term P-Recursive Recurrence |
  | :--- | :--- | :--- | :--- |
  | $\sum_{k=0}^n \binom{n}{k}\binom{n+k}{k} c^k$ (Legendre / Delannoy) | $1 - x - y - (1+2c)xy$ | $1 - 2(1+2c)s + s^2$ | $(n+1)a_{n+1} = (2n+1)(1+2c)a_n - n a_{n-1}$ |
  | $\sum_{k=0}^n \binom{n}{k}^2 c^k$ (Franel / Narayana 2D) | $1 - x - cy - (1-c)xy$ | $1 - 2(1+c)s + (1-c)^2 s^2$ | $(n+1)a_{n+1} = (2n+1)(1+c)a_n - n(1-c)^2 a_{n-1}$ |
  | $[x^n](p_0 + p_1 x + p_2 x^2)^n$ (Trinomial Powers) | $1 - y(p_0 + p_1 x + p_2 x^2)$ | $1 - 2p_1 s + (p_1^2 - 4p_0 p_2)s^2$ | $(n+1)a_{n+1} = (2n+1)p_1 a_n - n(p_1^2 - 4p_0 p_2)a_{n-1}$ |
  | $\sum_{k=0}^n \binom{n+k}{2k} C_k c^k$ (Large Schröder) | $1 - x - y - (1+c)xy$ (shifted) | $1 - 2(1+2c)s + s^2$ | $(n+1)S_n = (2n-1)(1+2c)S_{n-1} - (n-2)S_{n-2}$ |
  ```

---

### Omission 4: Missing Rejected Template Problem (`Luogu P6115`) in Section 8

- **Source Location**: `cohort1_iter_41_to_45_ode_sparse_cdq_relaxed.md`, Section 8, Line 1669 (`Luogu P6115 — 【模板】整式递推`).
- **Target Location to Insert**: [cohort3_wave_5a_ode_sparse_cdq_relaxed.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L1391-L1392) (append row to Section 8 table).
- **Drop-In Row to Append**:
  ```markdown
  | **Luogu P6115 — 【模板】整式递推** | `https://www.luogu.com.cn/problem/P6115` | Pure implementation template for $\sqrt{N}$ baby-step giant-step factorial/P-recursive evaluation without a combinatorial or ODE modeling step (covered in Wave 5B). |
  ```

---

### Omission 5: Missing & Corrupted Bibliography Citations in Section 9 (Lines 1396–1421)

- **Location**: [cohort3_wave_5a_ode_sparse_cdq_relaxed.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5a_ode_sparse_cdq_relaxed.md#L1396-L1421)
- **Audit Findings**:
  1. **Corrupted Author Names on Line 1400 (`[EN-6]`)**: Writes `Bostan, A., Chyzak, F., L.abahn, G., & M.abahn (2007)` — `L.abahn, G., & M.abahn` is a garbled hallucination of two distinct foundational 2007 papers from Cohort 1 (#6) and Cohort 2 (#4):
     - `Bostan, A., Chyzak, F., Ollivier, F., Salvy, B., Schost, É., & Sedoglavic, A. (2007). "Fast computation of power series solutions of systems of differential equations." Proceedings of the 18th ACM-SIAM Symposium on Discrete Algorithms (SODA 2007), pp. 1012–1021.`
     - `Bostan, A., Gaudry, P., & Schost, É. (2007). "Linear recurrences with polynomial coefficients and application to integer factorization and Cartier-Manin operator." SIAM Journal of Computing, 36(6), 1777–1806.`
  2. **Omitted Citation from Cohort 1 (`[EN]` #2)**:
     - `Lipshitz, L. (1988). "The diagonal of a D-finite power series is D-finite." Journal of Algebra, 113(2), 373–378.` and `Lipshitz, L. (1989). "D-finite power series." Journal of Algebra, 122(2), 353–373.`
  3. **Omitted Citation from Cohort 2 (`[EN]` #5)**:
     - `peltorator (2020). "Solving Differential Equations in Formal Power Series." Codeforces Blog Entry #76447 (https://codeforces.com/blog/entry/76447).`
  4. **Omitted Direct URLs from Cohort 1 & Cohort 2**:
     - EI (`EI_Captain`) CSDN Monograph URLs: `https://blog.csdn.net/EI_Captain/article/details/119425048`, `115118001`, `119546405`, `118074883`.
     - Nyaan's Library Header URLs: `https://nyaannyaan.github.io/library/fps/online-fps.hpp`, `https://nyaannyaan.github.io/library/fps/differential-equation.hpp`, `https://nyaannyaan.github.io/library/fps/find-p-recursive.hpp`.
- **Drop-In Replacement for Section 9 (Lines 1396–1421)**:
  ```markdown
  ### English Literature (`[EN]`)
  1. **[EN-1] Stanley, R. P. (1980).** *"Differentiably finite power series."* European Journal of Combinatorics, 1(2), 175–188. (Foundational paper establishing closure properties of D-finite generating functions and P-recursive sequences.)
  2. **[EN-2] Lipshitz, L. (1988).** *"The diagonal of a D-finite power series is D-finite."* Journal of Algebra, 113(2), 373–378; and **Lipshitz, L. (1989).** *"D-finite power series."* Journal of Algebra, 122(2), 353–373. (Proves that the diagonal of any multivariate D-finite series remains D-finite.)
  3. **[EN-3] Stanley, R. P. (1999).** *Enumerative Combinatorics, Volume 2*, Chapter 6: *"Rational, Algebraic, and D-Finite Generating Functions."* Cambridge University Press.
  4. **[EN-4] Flajolet, P., & Sedgewick, R. (2009).** *Analytic Combinatorics*, Chapters VII & VIII (Singularities, ODEs, and Saddle-Point / Holonomic Transfer). Cambridge University Press.
  5. **[EN-5] Zeilberger, D. (1990).** *"A holonomic systems approach to special functions identities."* Journal of Computational and Applied Mathematics, 32(3), 321–368; and **Petkovšek, M., Wilf, H. S., & Zeilberger, D. (1996).** *A=B*. A K Peters/CRC Press. (The algorithmic bible of Creative Telescoping and hypergeometric recurrences.)
  6. **[EN-6] van der Hoeven, J. (1997).** *"Lazy multiplication of formal power series."* Proceedings of the 1997 International Symposium on Symbolic and Algebraic Computation (ISSAC '97), ACM, 17–20.
  7. **[EN-7] van der Hoeven, J. (2002).** *"Relaxed multiplication of formal power series."* Journal of Symbolic Computation, 34(6), 479–542. (Introduces the $O(N \log^2 N)$ and $O(N \frac{\log^2 N}{\log \log N})$ radix-$B$ relaxed convolution algorithms.)
  8. **[EN-8] Bostan, A., Chyzak, F., Ollivier, F., Salvy, B., Schost, É., & Sedoglavic, A. (2007).** *"Fast computation of power series solutions of systems of differential equations."* Proceedings of the 18th ACM-SIAM Symposium on Discrete Algorithms (SODA 2007), 1012–1021. (Introduces the Newton-Integrating-Factor method for nonlinear ODEs in $O(N \log N)$ time.)
  9. **[EN-9] Bostan, A., Gaudry, P., & Schost, É. (2007).** *"Linear recurrences with polynomial coefficients and application to integer factorization and Cartier-Manin operator."* SIAM Journal on Computing, 36(6), 1777–1806.
  10. **[EN-10] Bostan, A., Chyzak, F., Giusti, M., Lebreton, R., Lecerf, G., Salvy, B., & Schost, É. (2017).** *Algorithmes Efficaces en Calcul Formel*, Chapters 14–16 (Differential Equations, Holonomic Functions, and Creative Telescoping).
  11. **[EN-11] Kauers, M. (2013).** *"The Holonomic Toolkit."* Computer Algebra in Quantum Field Theory, Springer, 119–144.
  12. **[EN-12] peltorator (2020).** *"Solving Differential Equations in Formal Power Series."* Codeforces Blog Entry #76447 (`https://codeforces.com/blog/entry/76447`).

  ### Chinese Literature (`[ZH]`)
  1. **[ZH-1] 钟子谦 (Zhong Ziqian, 2019).** 《两类递推数列的性质和应用》 (*Properties and Applications of Two Classes of Recursive Sequences — Algebraic and Holonomic/D-Finite Generating Functions*). IOI 2019 Chinese National Training Team (CTT / 国家集训队论文集).
  2. **[ZH-2] 镇海中学 — EI (`Elegia` / 虞皓翔, 2020–2022).**
     - 《浅谈微分有限生成函数与整式递推》 (*A Brief Discussion on D-Finite Generating Functions and P-Recursive Sequences*): `https://blog.csdn.net/EI_Captain/article/details/119425048`
     - 《生成函数杂谈 — 微分法与留数》 (*Generating Function Miscellany — Differential Method and Residues*): `https://blog.csdn.net/EI_Captain/article/details/115118001`
     - 《QOJ #60 中国象棋 题解》 (*Editorial for QOJ #60 Chinese Elephant Chess*): `https://blog.csdn.net/EI_Captain/article/details/119546405`
     - 《Polya / D-finite / CF755G $O(k)$ 做法》 (*$O(K)$ P-Recursive Reduction for Codeforces 755G*): `https://blog.csdn.net/EI_Captain/article/details/118074883`
  3. **[ZH-3] 郇真 (Huan Zhen / command_block, 2020).** 《多项式计数杂谈》 (*Polynomial Counting Miscellany — CDQ NTT, ODE Method, and Sparse Polynomials*).
  4. **[ZH-4] OI-Wiki Contributors.** *"多项式初等函数 / 常微分方程 / 分治 FFT (半在线卷积)."* OI-Wiki (`https://oi-wiki.org/math/poly/`).

  ### Japanese Literature (`[JA]`)
  1. **[JA-1] Nyaan (2021–2023).** *"Formal Power Series & Differential Equations / Online Convolution."* Nyaan's Competitive Programming Library:
     - Online / Relaxed Convolution: `https://nyaannyaan.github.io/library/fps/online-fps.hpp`
     - Nonlinear First-Order ODE Solver: `https://nyaannyaan.github.io/library/fps/differential-equation.hpp`
     - Berlekamp-Massey for P-Recursive Sequences: `https://nyaannyaan.github.io/library/fps/find-p-recursive.hpp`
  2. **[JA-2] maspy (2020–2023).** *"形式的べき級数解説 — 疎なべき級数の inv, exp, log, pow / P-recursive 数列."* `maspypy.com` (`https://maspypy.com/category/%e5%bd%a2%e5%bc%8f%e7%9a%84%e3%81%b9%e3%81%8d%e7%b4%9a%e6%95%b0/`).
  3. **[JA-3] noshi91 (2019–2022).** *"Relaxed Convolution (オンライン畳み込み) の計算量と実装."* `noshi91.hatenablog.com`.
  ```

---

## 4. Part III: Editorial & Formatting Checklist

1. **Banned Math Delimiters (`\(...\)` and `\[...\]`)**:
   - **Line 435**: `... - \frac{9}{8}x^4 + O(x^5)$.\) Wait:` $\to$ Remove `\)` (fixed by Bug 2 replacement).
   - **Line 438**: `... matching the Taylor expansion term-for-term!)*\)` $\to$ Remove `\)` (fixed by Bug 2 replacement).
   - Zero other occurrences in the file.
2. **Stream-of-Consciousness (`Wait` / `wait:`) & Truncated Derivations (`\dots`)**:
   - **Line 125**: `... Wait: ... Wait:` $\to$ Fixed by Bug 1 replacement.
   - **Line 385**: `Wait—for the algebraic tree equation...` $\to$ Fixed by Bug 3 replacement.
   - **Lines 432, 433, 435**: `... wait: ... (wait: ...) ... Wait:` $\to$ Fixed by Bug 2 replacement.
   - **Lines 654, 660**: `\dots \text{ wait: } ... Wait:` $\to$ Fixed by Bug 4 replacement.
   - **Lines 1011, 1014, 1015, 1018**: `... actually ... \dots ... Wait: even simpler ...` $\to$ Fixed by Bug 5 replacement.
3. **Minor Spacing & Typo Fixes**:
   - **Line 405**: Change `-Instead, for **every** elementary transcendental operation, we construct a differential equation where $F(x)$ or $F'(x)$ remains uninverted, and only the output $G(x)$ remainsdense:` to `- Instead, for **every** elementary transcendental operation, we construct a differential equation where $F(x)$ or $F'(x)$ remains uninverted, and only the output $G(x)$ remains dense:`.
   - **Line 830**: Change `- *Hint 3*:Shift $P(x)$` to `- *Hint 3*: Shift $P(x)$`.
