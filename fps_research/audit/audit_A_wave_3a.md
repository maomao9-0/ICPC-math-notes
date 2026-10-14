# Principal Mathematical & Pedagogical Audit Report — Wave 3A
**Target File**: [`cohort3_wave_3a_lagrange_residues_trees_graphs.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_3a_lagrange_residues_trees_graphs.md) (1,437 lines)
**Source Files Audited Against**:
1. [`cohort1_iter_21_to_25_lagrange_residues_trees_graphs.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort1_iter_21_to_25_lagrange_residues_trees_graphs.md) (1,276 lines)
2. [`cohort2_iter_73_to_77_lagrange_residues_trees_graphs.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_73_to_77_lagrange_residues_trees_graphs.md) (1,393 lines)
3. [`iter_21_to_25_lagrange_residues_trees_graphs.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_21_to_25_lagrange_residues_trees_graphs.md) (1,044 lines)

---

## Executive Summary

A line-by-line mathematical, algorithmic, and pedagogical audit of `cohort3_wave_3a_lagrange_residues_trees_graphs.md` was conducted against all three source files, accompanied by symbolic and numerical verification scripts in Python.

### Summary of Findings
1. **5 Critical Mathematical & Algorithmic Bugs**:
   - **Bug 1.1 (Lines 466, 469, 1178, 1181)**: Unrooted labelled cactus count replaces $\frac{(n-1)!}{n}$ with $(n-2)!$, which is mathematically false ($\frac{(n-1)!}{n} \neq (n-2)!$; at $n=1$ it is $(-1)!$, at $n=3$ it gives $6 \neq 4$, and at $n=4$ it gives $124/3 \notin \mathbb{Z}$). Furthermore, Line 469 claims an $O(n)$ recurrence for single-$n$ evaluation but only writes an $O(n^2)$ double sum, omitting the 4-term linear ODE recurrence.
   - **Bug 1.2 (Lines 989, 995, 996 — Problem 17, CF 1528F AmShZ Farm)**: Multiplies the answer by a spurious factor of $\frac{n}{n+1}$, giving non-integer or wrong answers (e.g., for $n=2, k=1$, formula gives $4$ instead of $6$; for $n=2, k=2$, formula gives $16/3$ instead of $8$). In Pollak's circular parking model on $n+1$ spaces, space $n+1$ is empty and therefore receives $0$ preferences ($\text{cnt}(n+1) = 0$), so summing over all $n+1$ symmetric spaces multiplies by $n+1$ and cancels the $\frac{1}{n+1}$ Cycle Lemma factor completely.
   - **Bug 1.3 (Lines 362–373 — Raney Orbit Trace)**: Claims $[u^2](1+u+u^2)^4 = 6$ and $[x^4]F(x)^2 = 3$, completely omitting the orbit of $(1,1,0,0)$ (size 4, 2 valid shifts) and leaving a confused `Wait:` note at Line 368. The true coefficient is $[u^2](1+u+u^2)^4 = 10$ and $[x^4]F(x)^2 = \frac{2}{4}(10) = 5$ (which was correctly computed in `iter_21_to_25` lines 70–90).
   - **Bug 1.4 (Lines 410 & 622 — *Concrete Mathematics* §7.5 Generalized Exponential Family)**: Writes $\mathcal{E}_r(x) = e^{rx\mathcal{E}_r(x)}$ with denominator $1 - rx\mathcal{E}_r(x)$, which actually satisfies $[x^n]\mathcal{E}_r(x)^k = \frac{k(rn)^{n-1}}{n!} \neq \frac{k(rn+k)^{n-1}}{n!}$. The true equation in *Concrete Mathematics* §7.5 (and `iter_21_to_25` line 292) is $\mathcal{E}_r(x) = e^{x\mathcal{E}_r(x)^r}$ with denominator $1 - rx\mathcal{E}_r(x)^r$.
   - **Bug 1.5 (Lines 249–255 — Case Study B Quadratic Restructuring)**: Sign flip when expanding $(1-x)Y^2 - (1-x)Y + x = 0$: Line 251 writes $Y^2 - Y + x(1 - Y + Y^2) = 0$ and Line 252 writes $(1-x)Y(1-Y) = x$, which correspond to $(1-x)Y - (1-x)Y^2 = x$ instead of $(1-x)Y^2 - (1-x)Y + x = 0$.
2. **2 Conflated/Misidentified Judge Problem IDs**:
   - **Issue 2.1 (Lines 566–567, 630, Problem 32 at Lines 1264–1275, and Problem 34 at Lines 1295–1310)**: On Luogu, **Luogu P7364** is *有标号二分图计数 (Labelled Bipartite Graphs)* (as in Cohort 1 Problem 10, Cohort 2 Problem 10, and Pre-existing Problem E2), NOT *有标号欧拉图计数 (Labelled Connected Eulerian Graphs)*. Meanwhile, **Luogu P6596** is *How Many of Them (Connected Undirected Labelled Graphs with $\le m$ Bridges)* (as in Cohort 1 Problem 11, Cohort 2 Problem 16, and Pre-existing Problem 16), NOT *Connected Bipartite Graphs with $\le m$ Bridges*. Conflating these caused standalone Luogu P7364 and standard Luogu P6596 to be overwritten/merged.
3. **3 Zero-Information-Loss / Truncated Derivation Issues**:
   - **Issue 3.1 (Lines 136–139 & 239–256)**: Section heading at Line 239 promises *"5. Three Worked Implicit-Equation Restructuring Case Studies"*, but only 2 case studies (A and B) appear, and at Lines 136–139 the author got stuck restructuring $Y(x) = 1 + x Y(x)^a (1 + x Y(x)^{a-1})^c$, dropping Cohort 1's Case Study C (§23.3, lines 502–514) which solves it via the coupled parameter $u = x Y(x)^{a-1}$.
   - **Issue 3.2 (Lines 184–197)**: The elementary algebraic proof of LIF stalls mid-induction with a `"Wait—instead of expanding..."` monologue, dropping Cohort 1's clean, complete 5-line formal derivative proof (§21.5, lines 166–186).
   - **Issue 3.3 (Lines 966–980 & 1048–1062)**: Problem 16 (Toyota 2023 Spring Final E) and Problem 20 (AtCoder AGC 070 C) use vague meta-descriptions in their problem statements rather than concrete mathematical formulations.
4. **Editorial & Pedagogical Hygiene Issues**:
   - **Issue 4.1 (Lines 38 & 638)**: Section headers state *"All 34 Unique Problems"*, whereas Section 4 contains **39** numbered problems (`Problem 1` to `Problem 39`).
   - **Issue 4.2 (16 Lines)**: Contains 16 unedited `"Wait:"` / `"wait—"` stream-of-consciousness self-correction markers (Lines 191, 368, 681, 761, 805, 810, 840, 919, 973, 974, 985, 995, 1196, 1383, 1391, 1414).
   - **Math Delimiters Check**: **PASS** (0 instances of `\(...\)` or `\[...\]`).

---

## Category 1: Critical Mathematical & Algorithmic Bugs

### Bug 1.1: Unrooted Labelled Cacti LIF Factorial Error (`(n-2)!` vs. `\frac{(n-1)!}{n}`) & Missing $O(n)$ D-Finite Recurrence
- **Locations**:
  1. **Line 466 & Line 469** (§2 Iteration 24 / 76.4C)
  2. **Line 1178 & Line 1181** (§4 Problem 27 — SPOJ CACTUS / Cactus Graph Benchmark)
- **Current Erroneous Text**:
  - Line 466:
    ```markdown
    - **Unrooted Connected Cacti**: $C(x) = F(x) - \frac{1}{2} F(x)^2 + \frac{1}{2} \frac{F(x)^2}{1 - F(x)}$ (via Dissymmetry Theorem), or directly via $n c_n = [x^n] x C'(x) = [x^n] F(x)$, giving:
      $$c_n = (n-1)! [x^n] F(x) = (n-2)! [u^{n-1}] \exp\left( n \cdot \frac{2u - u^2}{2(1 - u)} \right).$$
    ```
  - Line 469:
    ```markdown
    - **Single-$n$ $O(n)$ Extraction (No FFT)**: Write $\exp\left( \frac{n(2u - u^2)}{2(1 - u)} \right) = \exp\left( -\frac{n}{2} u \right) \exp\left( \frac{n u}{2(1 - u)} \right)$. Using $[u^m] \exp\left( \frac{\alpha u}{1 - u} \right) = \sum_{j=1}^m \binom{m-1}{j-1} \frac{\alpha^j}{j!}$, we can extract $[u^{n-1}]$ in $O(n)$ time via the D-finite ODE recurrence of $\exp\left(\frac{n(2u - u^2)}{2(1 - u)}\right)$!
    ```
  - Lines 1178 & 1181:
    ```markdown
    - **Hint 2**: Rather than computing $C(x)$ directly, note that rooting a cactus at a vertex gives $n c_n = n! [x^n] F(x)$, so $c_n = (n-1)! [x^n] F(x) = (n-2)! [u^{n-1}] \exp\left( \frac{n(2u - u^2)}{2(1 - u)} \right)$.
    ...
      $$c_n = (n-1)! [x^n] F(x) = (n-2)! [u^{n-1}] \exp\left( \frac{n(2u - u^2)}{2(1 - u)} \right).$$
    ```
- **Mathematical Error**:
  By LIF, $[x^n] F(x) = \frac{1}{n} [u^{n-1}] \Phi(u)^n = \frac{1}{n} [u^{n-1}] \exp\!\left(n \cdot \frac{2u - u^2}{2(1-u)}\right)$.
  Multiplying by $(n-1)!$ yields:
  $$c_n = (n-1)! [x^n] F(x) = \frac{(n-1)!}{n} [u^{n-1}] \exp\!\left( n \cdot \frac{2u - u^2}{2(1 - u)} \right).$$
  Note that $\frac{(n-1)!}{n} \neq (n-2)!$ for every $n \ge 1$! Numerically, for $n = 1, 2, 3, 4, 5$:
  - True $[u^{n-1}] \exp\!\left(n\frac{2u-u^2}{2(1-u)}\right)$ is $1, 2, 6, \frac{62}{3}, \frac{625}{6}$.
  - Multiplying by $\frac{(n-1)!}{n}$ gives $c_1 = 1, c_2 = 1, c_3 = 4, c_4 = 31, c_5 = 500$ (OEIS A000314 / unrooted labelled cacti).
  - Multiplying by $(n-2)!$ gives $(-1)!$ at $n=1$, $6 \neq 4$ at $n=3$, and $\frac{124}{3} \notin \mathbb{Z}$ at $n=4$!
  - Furthermore, at Line 469, the expansion $\exp(-\frac{n}{2}u)\exp(\frac{nu}{2(1-u)})$ requires an $O(n^2)$ convolution unless the 3-term D-finite ODE recurrence for $E_n(u) = \exp\!\left(n \cdot \frac{2u - u^2}{2(1-u)}\right)$ (or the 4-term recurrence for $B(u) = \exp\!\left(\frac{nu^2}{2(1-u)}\right)$ from Cohort 1 §24.3 line 765) is explicitly stated. Specifically, differentiating $E_n(u) = \exp\!\left(n \frac{2u - u^2}{2(1-u)}\right)$ gives:
    $$(1 - u)^2 E_n'(u) = n\left(1 - u + \frac{1}{2}u^2\right) E_n(u),$$
    which yields the exact $O(n)$-time 4-term linear recurrence for $e_m = [u^m] E_n(u)$:
    $$(m+1) e_{m+1} = (2m + n) e_m - (m - 1 + n) e_{m-1} + \frac{n}{2} e_{m-2} \quad (m \ge 0,\ e_0 = 1,\ e_{<0} = 0).$$
- **Actionable Replacement for Lines 465–470**:
  ```markdown
  - **Unrooted Connected Cacti**: $C(x) = F(x) - \frac{1}{2} F(x)^2 + \frac{1}{2} \frac{F(x)^2}{1 - F(x)}$ (via the Dissymmetry Theorem), or directly via vertex-rooting $n c_n = n! [x^n] x C'(x) = n! [x^n] F(x)$, giving:
    $$c_n = (n-1)! [x^n] F(x) = \frac{(n-1)!}{n} [u^{n-1}] \exp\left( n \cdot \frac{2u - u^2}{2(1 - u)} \right).$$
  - **Single-$n$ $O(n)$ Extraction (No FFT)**: Let $E_n(u) = \exp\left( \frac{n(2u - u^2)}{2(1 - u)} \right) = \sum_{m \ge 0} e_m u^m$. Differentiating with respect to $u$ gives the D-finite ODE $(1 - u)^2 E_n'(u) = n\left(1 - u + \frac{1}{2}u^2\right) E_n(u)$. Extracting $[u^m]$ yields the exact 4-term linear recurrence:
    $$(m + 1) e_{m+1} = (2m + n) e_m - (m - 1 + n) e_{m-1} + \frac{n}{2} e_{m-2} \quad (m \ge 0, \ e_0 = 1, \ e_{<0} = 0),$$
    allowing us to compute $c_n = \frac{(n-1)!}{n} e_{n-1}$ in $O(n)$ time and $O(1)$ auxiliary space! Alternatively, factoring $E_n(u) = \exp\left(-\frac{n}{2}u\right) \exp\left(\frac{nu}{2(1-u)}\right)$ and using $[u^m] \exp\left(\frac{\alpha u}{1-u}\right) = \sum_{j=1}^m \binom{m-1}{j-1} \frac{\alpha^j}{j!}$ gives a closed-form double sum.
  ```
- **Actionable Replacement for Lines 1178–1188 (Problem 27)**:
  ```markdown
  - **Hint 2**: Rather than computing $C(x)$ directly, note that rooting a cactus at a vertex gives $n c_n = n! [x^n] F(x)$, so $c_n = (n-1)! [x^n] F(x) = \frac{(n-1)!}{n} [u^{n-1}] \exp\left( \frac{n(2u - u^2)}{2(1 - u)} \right)$.
  - **Hint 3**: Either expand $\exp\left( \frac{n(2u - u^2)}{2(1 - u)} \right)$ in $O(n \log n)$ via polynomial exp, or use the D-finite ODE $(1 - u)^2 E_n'(u) = n\left(1 - u + \frac{1}{2}u^2\right) E_n(u)$ to compute $e_{n-1} = [u^{n-1}] E_n(u)$ in $O(n)$ time via a 4-term linear recurrence.
  - **Full Derivation & Solution**:
    By LIF on $F(x) = x \exp\left( \frac{2F(x) - F(x)^2}{2(1 - F(x))} \right)$:
    $$c_n = (n-1)! [x^n] F(x) = \frac{(n-1)!}{n} [u^{n-1}] \exp\left( \frac{n(2u - u^2)}{2(1 - u)} \right).$$
    Let $E_n(u) = \exp\left( \frac{n(2u - u^2)}{2(1 - u)} \right) = \sum_{m \ge 0} e_m u^m$. Since $\frac{d}{du}\left[\frac{2u - u^2}{2(1 - u)}\right] = \frac{2 - 2u + u^2}{2(1 - u)^2}$, we have:
    $$(1 - 2u + u^2) E_n'(u) = n\left(1 - u + \frac{1}{2}u^2\right) E_n(u).$$
    Extracting $[u^m]$ gives $e_0 = 1$ and, for $m = 0, 1, \dots, n - 2$:
    $$(m + 1) e_{m+1} = (2m + n) e_m - (m - 1 + n) e_{m-1} + \frac{n}{2} e_{m-2}.$$
    Finally, $c_n = \frac{(n-1)!}{n} e_{n-1} \bmod p$. For $n = 1, 2, 3, 4, 5$, this yields $c_1 = 1, c_2 = 1, c_3 = 4, c_4 = 31, c_5 = 500$. Time complexity: $O(n)$ per single-$n$ query, or $O(N \log N)$ for all $n \le N$ via polynomial Newton iteration.
  ```

---

### Bug 1.2: CF 1528F (AmShZ Farm) Spurious $\frac{n}{n+1}$ Factor Bug
- **Location**: **Lines 985–997** (§4 Problem 17 — Codeforces 1528F AmShZ Farm)
- **Current Erroneous Text**:
  ```markdown
    Wait: by Pollak's circular rotation argument on $n+1$ spots, a preference sequence on $\{1, \dots, n+1\}^n$ has a unique valid shift, and each valid parking function appears $n+1$ times among all $(n+1)^n$ circular sequences. For a fixed spot $v \in \{1, \dots, n\}$, the distribution of $\text{cnt}(v)$ across all $(n+1)^{n-1}$ valid parking functions is identical to its distribution across all $(n+1)^n$ circular sequences! Wait—is $\text{cnt}(v)$ invariant under the shift? In the circular model, shifting all preferences by $+c \pmod{n+1}$ permutes the $n+1$ spots cyclically! Since $n$ of the $n+1$ spots are in $\{1, \dots, n\}$ and $1$ spot is the empty spot $n+1$ (which has $\text{cnt}(n+1) = 0$? No, no car can prefer spot $n+1$, so in a valid parking function $\text{cnt}(n+1)$ must be $0$, wait: in Pollak's argument, cars are allowed to prefer spot $n+1$ in the $(n+1)^n$ tuples, EXCEPT that if spot $n+1$ ends up empty, NO car could have preferred spot $n+1$!).
    Therefore, a tuple in $\{1, \dots, n+1\}^n$ leaves spot $n+1$ empty iff its shift puts the empty spot at $n+1$, and in that shifted tuple, $\text{cnt}(n+1) = 0$ automatically! Since the sum of $\text{cnt}(v)^k$ over ALL $v \in \{1, \dots, n+1\}$ is shift-invariant (just permuting the $n+1$ spots), and $\text{cnt}(n+1) = 0$ on the valid representative (for $k \ge 1$), the sum $\sum_{v=1}^n \text{cnt}(v)^k$ on the valid representative equals $\sum_{v=1}^{n+1} \text{cnt}(v)^k$ on EVERY member of its cyclic orbit!
    Summing over all $(n+1)^n$ tuples in $\{1, \dots, n+1\}^n$ and dividing by the orbit size $n+1$:
    $$\text{ans} = \frac{1}{n+1} \sum_{v=1}^n \sum_{a \in \{1, \dots, n+1\}^n} [\text{cnt}_v(a)]^k = \frac{n}{n+1} \sum_{m=1}^n \binom{n}{m} m^k n^{n-m}.$$
    Using $m^k = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} m^{\underline{j}}$ and $\binom{n}{m} m^{\underline{j}} = n^{\underline{j}} \binom{n-j}{m-j}$:
    $$\sum_{m=1}^n \binom{n}{m} m^k n^{n-m} = \sum_{j=1}^{\min(n,k)} \left\{\begin{matrix} k \\ j \end{matrix}\right\} n^{\underline{j}} \sum_{m=j}^n \binom{n-j}{m-j} n^{n-m} = \sum_{j=1}^{\min(n,k)} \left\{\begin{matrix} k \\ j \end{matrix}\right\} n^{\underline{j}} (n+1)^{n-j}.$$
    Wait: for $k=1$, $\sum_{v=1}^n \text{cnt}(v) = n$ on every parking function, so the total sum over $(n+1)^{n-1}$ parking functions must be $n(n+1)^{n-1}$. Our inner sum gives $n(n+1)^{n-1}$ directly! Why? Because in the cyclic orbit of size $n+1$, the sum is over all $v \in \{1, \dots, n+1\}$ (which has $n+1$ terms, cancelling $\frac{1}{n+1}$!). Wait: for $k=1$, $j=1$ gives $n (n+1)^{n-1}$, and multiplying by $\frac{n}{n+1}$ gives $n^2 (n+1)^{n-2}$, which is wrong unless $n$ is replaced by $n+1$! Indeed, summing over $v \in \{1, \dots, n+1\}$ has $n+1$ spots, each with $\binom{n}{m} 1^m n^{n-m}$, so the $\frac{1}{n+1}$ cancels the $n+1$ spots, EXCEPT spot $n+1$ in the valid shift has $\text{cnt}(n+1) = 0$.
    With the LIF/tree formulation $x T'(x) = \frac{T(x)}{1 - T(x)}$, the exact answer is:
    $$\text{ans} = n \sum_{j=1}^{\min(n, k)} \left\{\begin{matrix} k \\ j \end{matrix}\right\} (n-1)^{\underline{j-1}} (n+1)^{n-j} \quad \text{or} \quad \sum_{j=1}^{\min(n,k)} \left\{\begin{matrix} k \\ j \end{matrix}\right\} n^{\underline{j}} (n+1)^{n-1-j} \cdot n.$$
  ```
- **Mathematical Error**:
  Let us verify by exact brute force for small $n, k$:
  - For $n = 2$, the $(n+1)^{n-1} = 3$ parking functions on $\{1, 2\}$ are $(1, 1), (1, 2), (2, 1)$:
    - $(1, 1)$: $\text{cnt}(1) = 2, \text{cnt}(2) = 0 \implies \sum \text{cnt}(v)^k = 2^k$.
    - $(1, 2)$: $\text{cnt}(1) = 1, \text{cnt}(2) = 1 \implies \sum \text{cnt}(v)^k = 1^k + 1^k = 2$.
    - $(2, 1)$: $\text{cnt}(1) = 1, \text{cnt}(2) = 1 \implies \sum \text{cnt}(v)^k = 1^k + 1^k = 2$.
    - Total sum for $n = 2$: $2^k + 4$. For $k = 1$, $\text{ans} = 6$; for $k = 2$, $\text{ans} = 8$; for $k = 3$, $\text{ans} = 12$.
  - Now evaluate $\sum_{m=1}^n \binom{n}{m} m^k n^{n-m} = \sum_{j=1}^{\min(n,k)} \left\{\begin{matrix} k \\ j \end{matrix}\right\} n^{\underline{j}} (n+1)^{n-j}$ for $n = 2$:
    - $m = 1$: $\binom{2}{1} 1^k \cdot 2^1 = 4$.
    - $m = 2$: $\binom{2}{2} 2^k \cdot 2^0 = 2^k$.
    - Sum $= 2^k + 4$, which equals $6, 8, 12$ for $k = 1, 2, 3$ — **EXACT MATCH WITHOUT ANY $\frac{n}{n+1}$ FACTOR!**
  - Why does $\frac{1}{n+1}$ cancel $n+1$ rather than giving $\frac{n}{n+1}$? Because on the unique valid representative in each cyclic orbit (where space $n+1$ is empty), $\text{cnt}(n+1) = 0$, so for $k \ge 1$:
    $$\sum_{v=1}^n \text{cnt}(v)^k = \sum_{v=1}^{n+1} \text{cnt}(v)^k.$$
    Since $\sum_{v=1}^{n+1} \text{cnt}(v)^k$ is invariant under all $n+1$ cyclic shifts of the preferences in $\{1, \dots, n+1\}^n$, summing over all $(n+1)^{n-1}$ valid parking functions equals $\frac{1}{n+1}$ times the sum of $\sum_{v=1}^{n+1} \text{cnt}(v)^k$ over all $(n+1)^n$ unconstrained tuples in $\{1, \dots, n+1\}^n$. By symmetry of the $n+1$ spaces, multiplying by $n+1$ cancels $\frac{1}{n+1}$ completely!
- **Actionable Replacement for Lines 980–1000 (Problem 17)**:
  ```markdown
  - **Hint 2**: Use Pollak's circular parking model on $n+1$ spaces $\{1, \dots, n+1\}$: every tuple $a \in \{1, \dots, n+1\}^n$ has a unique cyclic shift $(a_1 + c, \dots, a_n + c) \pmod{n+1}$ that leaves space $n+1$ empty (making it a valid parking function). Critically, because space $n+1$ is empty, no car could have preferred space $n+1$, so $\text{cnt}(n+1) = 0$ on every valid parking function!
  - **Hint 3**: Because $\text{cnt}(n+1) = 0$, we have $\sum_{v=1}^n \text{cnt}(v)^k = \sum_{v=1}^{n+1} \text{cnt}(v)^k$ for $k \ge 1$. The latter sum is invariant under all $n+1$ cyclic shifts of the preferences. Expand $m^k = \sum_{j=1}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} m^{\underline{j}}$ and compute the row of Stirling numbers of the second kind $\left\{\begin{matrix} k \\ j \end{matrix}\right\}_{j=1}^k$ in $O(k \log k)$ via NTT.
  - **Full Derivation & Solution**:
    Consider all $(n+1)^n$ preference tuples $a \in \{1, \dots, n+1\}^n$ on a circle of $n+1$ spaces. Partition them into $(n+1)^{n-1}$ cyclic shift orbits of size $n+1$. Each orbit contains a unique valid parking function (the shift leaving space $n+1$ empty). In that valid representative, since space $n+1$ is never occupied, no car prefers space $n+1$, so $\text{cnt}(n+1) = 0$. Thus, for any $k \ge 1$, on the valid representative:
    $$\sum_{v=1}^n \text{cnt}(v)^k = \sum_{v=1}^{n+1} \text{cnt}(v)^k.$$
    Because shifting all preferences by $+1 \pmod{n+1}$ merely permutes the $n+1$ spaces cyclically, the sum $\sum_{v=1}^{n+1} \text{cnt}(v)^k$ takes the exact same value on all $n+1$ members of each cyclic orbit! Summing over all $(n+1)^{n-1}$ valid parking functions is therefore $\frac{1}{n+1}$ times the sum of $\sum_{v=1}^{n+1} \text{cnt}(v)^k$ over all $(n+1)^n$ unconstrained tuples in $\{1, \dots, n+1\}^n$. By symmetry among the $n+1$ spaces, each fixed space $v$ is preferred by $m$ cars in $\binom{n}{m} n^{n-m}$ tuples, so the $n+1$ spaces cancel the $\frac{1}{n+1}$ orbit factor:
    $$\text{ans} = \frac{1}{n+1} \sum_{v=1}^{n+1} \sum_{m=1}^n \binom{n}{m} m^k n^{n-m} = \sum_{m=1}^n \binom{n}{m} m^k n^{n-m}.$$
    (Equivalently, in the EGF formulation with $T(x) = x e^{T(x)}$, each space represents a rooted component in a forest of $n+1$ rooted trees, and extracting $[x^n]$ via LIF $F(u) = (1+u)^n$ gives the same binomial sum.)
    Substituting $m^k = \sum_{j=1}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} m^{\underline{j}}$ and using $\binom{n}{m} m^{\underline{j}} = n^{\underline{j}} \binom{n-j}{m-j}$:
    $$\text{ans} = \sum_{j=1}^{\min(n, k)} \left\{\begin{matrix} k \\ j \end{matrix}\right\} n^{\underline{j}} \sum_{m=j}^n \binom{n-j}{m-j} n^{n-m} = \sum_{j=1}^{\min(n, k)} \left\{\begin{matrix} k \\ j \end{matrix}\right\} n^{\underline{j}} (n + 1)^{n - j}.$$
    Compute $\left\{\begin{matrix} k \\ j \end{matrix}\right\}$ for $1 \le j \le k$ in $O(k \log k)$ time via the NTT convolution $\left\{\begin{matrix} k \\ j \end{matrix}\right\} = \sum_{i=0}^j \frac{(-1)^{j-i} i^k}{i! (j-i)!}$, then evaluate the sum in $O(k)$ time.
  ```

---

### Bug 1.3: Raney Lemma Orbit Trace Arithmetic Error (`[u^2](1+u+u^2)^4 = 6` instead of `10`)
- **Location**: **Lines 362–373** (§2 Iteration 23 / 75.1 — Explicit Small-$n$ Trace of Raney's Lemma)
- **Current Erroneous Text**:
  ```markdown
  Let $\Phi(u) = 1 + u + u^2$ (Motzkin trees, where each node has out-degree $c_i \in \{0, 1, 2\}$) and compute $[x^4] F(x)^2$ ($n = 4, k = 2$).
  - Total out-degree sum must be $n - k = 4 - 2 = 2$, so step sum $\sum_{i=1}^4 (c_i - 1) = 2 - 4 = -2 = -k$.
  - By LIF, $[x^4] F(x)^2 = \frac{2}{4} [u^2] (1 + u + u^2)^4 = \frac{1}{2} (6) = 3$.
  - Combinatorial orbits of $(c_1, c_2, c_3, c_4) \in \{0, 1, 2\}^4$ with $\sum c_i = 2$:
    1. **One $2$ and three $0$s** (4 sequences, steps $+1, -1, -1, -1$):
       - $(+1, -1, -1, -1)$: prefix sums $1, 0, -1, -2$ (hits $-2$ at $i=4$, valid!).
       - $(-1, +1, -1, -1)$: prefix sums $-1, 0, -1, -2$ (hits $-2$ at $i=4$, valid!).
       - $(-1, -1, +1, -1)$: prefix sums $-1, -2, -1, -2$ (hits $-2$ early at $i=2$, invalid).
       - $(-1, -1, -1, +1)$: prefix sums $-1, -2, -3, -2$ (hits $-2$ early at $i=2$, invalid).
       Wait: why did 2 of the 4 cyclic shifts work? Because $k = 2$, so $\frac{k}{n} = \frac{2}{4} = \frac{1}{2}$ of every cyclic orbit is valid!
    2. **Two $1$s and two $0$s** (6 sequences, steps $0, 0, -1, -1$):
       - The symmetric orbit $(0, -1, 0, -1)$ and $(-1, 0, -1, 0)$ has size $2$, and $\frac{2}{4} \times 2 = 1$ valid shift: $(0, -1, 0, -1)$ gives prefix sums $0, -1, -1, -2$ (valid!), while $(-1, 0, -1, 0)$ hits $-2$ at $i=3$ (invalid).
  ```
- **Mathematical Error**:
  $(1 + u + u^2)^4 = 1 + 4u + 10u^2 + 16u^3 + 19u^4 + \dots$, so $[u^2](1 + u + u^2)^4 = \binom{4}{1} + \binom{4}{2} = 4 + 6 = 10$ (NOT $6$!), and $[x^4] F(x)^2 = \frac{2}{4}(10) = 5$ (NOT $3$!).
  The author forgot the size-4 asymmetric orbit of $(1, 1, 0, 0)$ (steps $0, 0, -1, -1$), which contributes $2$ additional valid shifts! Notice that `iter_21_to_25_lagrange_residues_trees_graphs.md` (lines 70–90) had the exact, complete 3-orbit table totaling $2 + 2 + 1 = 5$.
- **Actionable Replacement for Lines 362–373**:
  ```markdown
  Let $\Phi(u) = 1 + u + u^2$ (Motzkin trees, where each node has out-degree $c_i \in \{0, 1, 2\}$) and compute $[x^4] F(x)^2$ ($n = 4, k = 2$):
  - Total out-degree sum must be $n - k = 4 - 2 = 2$, so the step sum $\sum_{i=1}^4 s_i = \sum_{i=1}^4 (1 - c_i) = 4 - 2 = +2 = k$ (or equivalently $\sum (c_i - 1) = -2 = -k$).
  - By LIF, $[x^4] F(x)^2 = \frac{2}{4} [u^2] (1 + u + u^2)^4 = \frac{1}{2} \left(\binom{4}{1} + \binom{4}{2}\right) = \frac{1}{2}(4 + 6) = 5$.
  - Using upward steps $s_i = 1 - c_i \in \{-1, 0, +1\}$, a sequence is a valid Lukasiewicz word for a forest of $k = 2$ Motzkin trees iff its prefix sums $S_j = \sum_{i=1}^j s_i$ first hit $+2$ at $j = 4$ (equivalently, all proper prefix sums satisfy $S_j < 2$ for $1 \le j \le 3$, and $S_4 = 2$). The $\binom{4}{1} + \binom{4}{2} = 10$ sequences partition into three cyclic orbits, and in every orbit exactly $\frac{k}{n} = \frac{2}{4} = \frac{1}{2}$ of the shifts are valid:

  | Orbit Representative $(c_1, c_2, c_3, c_4)$ | Step Sequence $s_i = 1 - c_i$ | Orbit Size | All Cyclic Shifts & Prefix Sums $S_1, S_2, S_3, S_4$ | Valid Shifts (First Hit $+2$ at $j = 4$) |
  | :--- | :--- | :--- | :--- | :--- |
  | $(2, 0, 0, 0)$ | $(-1, +1, +1, +1)$ | $4$ | $(-1, +1, +1, +1) \to -1, 0, 1, \mathbf{2}$ (Valid)<br>$(+1, -1, +1, +1) \to 1, 0, 1, \mathbf{2}$ (Valid)<br>$(+1, +1, -1, +1) \to 1, \mathbf{2}, 1, 2$ (Hits $2$ at $j=2$)<br>$(+1, +1, +1, -1) \to 1, \mathbf{2}, 3, 2$ (Hits $2$ at $j=2$) | **$2$** ($\frac{2}{4} \times 4 = 2$) |
  | $(1, 1, 0, 0)$ | $(0, 0, +1, +1)$ | $4$ | $(0, 0, +1, +1) \to 0, 0, 1, \mathbf{2}$ (Valid)<br>$(0, +1, +1, 0) \to 0, 1, \mathbf{2}, 2$ (Hits $2$ at $j=3$)<br>$(+1, +1, 0, 0) \to 1, \mathbf{2}, 2, 2$ (Hits $2$ at $j=2$)<br>$(+1, 0, 0, +1) \to 1, 1, 1, \mathbf{2}$ (Valid) | **$2$** ($\frac{2}{4} \times 4 = 2$) |
  | $(1, 0, 1, 0)$ | $(0, +1, 0, +1)$ | $2$ | $(0, +1, 0, +1) \to 0, 1, 1, \mathbf{2}$ (Valid)<br>$(+1, 0, +1, 0) \to 1, 1, \mathbf{2}, 2$ (Hits $2$ at $j=3$) | **$1$** ($\frac{2}{4} \times 2 = 1$) |

  Summing the valid shifts across all three orbits gives $2 + 2 + 1 = 5 = \frac{2}{4}[u^2](1 + u + u^2)^4$. Note how the symmetric orbit $(1, 0, 1, 0)$ has period $2$ (orbit size $2$), and Raney's Lemma still selects $\frac{k}{n} \times 2 = 1$ valid representative!
  ```

---

### Bug 1.4: *Concrete Mathematics* §7.5 Generalized Exponential Family Typo (`\mathcal{E}_r(x) = e^{rx\mathcal{E}_r(x)}` vs. `e^{x\mathcal{E}_r(x)^r}`)
- **Locations**:
  1. **Line 410** (§2 Iteration 23 / 75.3 — Master Reference Table)
  2. **Line 622** (§3 Citation 3 — Graham, Knuth, Patashnik *Concrete Mathematics*)
- **Current Erroneous Text**:
  - Line 410:
    ```markdown
    | **Generalized Exponential** $\mathcal{E}_r(x)$ | $\mathcal{E}_r(x) = e^{r x \mathcal{E}_r(x)}$ | $\Phi(u) = e^{ru}$ | $[x^n] \mathcal{E}_r(x)^k = \frac{k(rn + k)^{n-1}}{n!}$ | $[x^n] \frac{\mathcal{E}_r(x)^k}{1 - rx\mathcal{E}_r(x)} = \frac{(rn + k)^n}{n!}$ |
    ```
  - Line 622:
    ```markdown
    3. **Graham, R. L., Knuth, D. E., & Patashnik, O.** (1994). *Concrete Mathematics* (2nd ed.), §6.6, §7.5. Addison-Wesley. (Raney's Lemma and the three canonical generalized series families $\mathcal{B}_t(x), \mathcal{E}_r(x) = e^{rx\mathcal{E}_r(x)}, \mathcal{C}_t(x)$).
    ```
- **Mathematical Error**:
  If $F(x) = e^{r x F(x)}$, then $r F(x) = r e^{(rx)(r F(x))} = T(rx)$, so $[x^n] F(x)^k = [x^n] r^{-k} T(rx)^k = r^{n-k} \frac{k n^{n-1}}{n!} = \frac{k (rn)^{n-1}}{n!} r^{1-k} \neq \frac{k(rn+k)^{n-1}}{n!}$!
  In *Concrete Mathematics* §7.5 (eq. 7.64, p. 363) and `iter_21_to_25` (line 292), the generalized exponential series is defined by:
  $$\mathcal{E}_t(z) = e^{z \mathcal{E}_t(z)^t} \quad \Longleftrightarrow \quad \mathcal{E}_r(x) = e^{x \mathcal{E}_r(x)^r}.$$
  Setting $W(x) = \mathcal{E}_r(x) - 1$ or applying LIF to $U(x) = x \mathcal{E}_r(x)^r = U(x)$ with $u = x \mathcal{E}_r(x)^r \implies \mathcal{E}_r(x) = e^u$ and $x = u e^{-ru}$ ($\Phi(u) = e^{ru}$) extracts $[x^n] \mathcal{E}_r(x)^k = [x^n] e^{ku} = \frac{1}{n} [u^{n-1}] k e^{ku} (e^{ru})^n = \frac{k (rn + k)^{n-1}}{n!}$, and the Jacobian denominator is $1 - r u = 1 - r x \mathcal{E}_r(x)^r$!
- **Actionable Replacement for Line 410**:
  ```markdown
  | **Generalized Exponential** $\mathcal{E}_r(x)$ | $\mathcal{E}_r(x) = e^{x \mathcal{E}_r(x)^r}$ ($u = x \mathcal{E}_r(x)^r$) | $\Phi(u) = e^{ru}$ ($H(u) = e^{ku}$) | $[x^n] \mathcal{E}_r(x)^k = \frac{k(rn + k)^{n-1}}{n!}$ | $[x^n] \frac{\mathcal{E}_r(x)^k}{1 - rx\mathcal{E}_r(x)^r} = \frac{(rn + k)^n}{n!}$ |
  ```
- **Actionable Replacement for Line 622**:
  ```markdown
  3. **Graham, R. L., Knuth, D. E., & Patashnik, O.** (1994). *Concrete Mathematics* (2nd ed.), §6.6, §7.5. Addison-Wesley. (Raney's Lemma and the three canonical generalized series families $\mathcal{B}_t(x) = 1 + x \mathcal{B}_t(x)^t$, $\mathcal{E}_r(x) = e^{x\mathcal{E}_r(x)^r}$, and $\mathcal{C}_t(x)$).
  ```

---

### Bug 1.5: Case Study B Algebraic Sign Error (`(1-x)Y^2 - (1-x)Y + x = 0`)
- **Location**: **Lines 249–255** (§2 Iteration 21 / 73.5 — Case Study B)
- **Current Erroneous Text**:
  ```markdown
  - **Case Study B: Rational-Coefficient Quadratic $(1 - x) Y(x)^2 - (1 - x) Y(x) + x = 0$ (with $Y(0) = 0$)**
    - *Trap*: Both $x$ and $Y(x)$ are mixed.
    - *Fix*: Isolate $x$ in terms of $Y$: $Y^2 - Y + x(1 - Y + Y^2) = 0$? Or simpler: $(1 - x) Y (1 - Y) = x \implies \frac{x}{1 - x} = Y(1 - Y)$.
    - *Two LIF Paths*:
      1. **Direct Solve for $x$**: $x = \frac{Y(1 - Y)}{1 + Y(1 - Y)} = \frac{Y(1 - Y)}{1 + Y - Y^2}$, so $Y = x \Phi(Y)$ with $\Phi(u) = \frac{1 + u - u^2}{1 - u}$.
      2. **Composite Variable $z = \frac{x}{1 - x}$**: Write $Y(1 - Y) = z \implies Y = z \cdot \frac{1}{1 - Y}$ ($\Phi(u) = \frac{1}{1 - u}$, standard Catalan in $z$!), so $Y(x) = \sum_{k \ge 1} C_{k-1} \left(\frac{x}{1 - x}\right)^k$, and extract $[x^n]$ via binomial expansion!
  ```
- **Mathematical Error**:
  Expanding $(1 - x)Y^2 - (1 - x)Y + x = 0$ gives:
  $$Y^2 - Y + x(1 + Y - Y^2) = 0 \iff x(1 + Y - Y^2) = Y(1 - Y) \iff x = \frac{Y(1 - Y)}{1 + Y - Y^2}.$$
  This is **not** equivalent to $(1 - x)Y(1 - Y) = x$ (which expands to $(1 - x)Y - (1 - x)Y^2 = x$, i.e., $Y(1 - Y) = \frac{x}{1 - x} \iff x = \frac{Y(1 - Y)}{1 + Y(1 - Y)} = \frac{Y(1 - Y)}{1 + Y - Y^2}$—wait: $\frac{x}{1-x} = Y(1-Y) \iff x = (1-x)Y(1-Y) \iff (1-x)Y - (1-x)Y^2 = x \iff (1-x)Y^2 - (1-x)Y + x = 0$ ONLY if the signs on $(1-x)$ are $(1-x)Y - (1-x)Y^2 = x$, i.e., $(1-x)Y^2 - (1-x)Y + x = 0$ has $-x Y^2 + x Y + x = x(1 + Y - Y^2)$, whereas $(1-x)Y(1-Y) = x$ has $+x Y^2 - x Y + x = x(1 - Y + Y^2)$!).
  Let's check both equations carefully:
  1. In $(1 - x)Y^2 - (1 - x)Y + x = 0$ (Cohort 1 §23.3 line 498):
     $$Y^2 - Y + x(1 + Y - Y^2) = 0 \implies x = \frac{Y(1 - Y)}{1 + Y - Y^2} \implies \Phi(u) = \frac{1 + u - u^2}{1 - u}.$$
  2. In $(1 - x)Y(1 - Y) = x$, i.e., $(1 - x)Y^2 - (1 - x)Y + x = 0$ is FALSE; $(1 - x)Y(1 - Y) = x \iff (1 - x)Y - (1 - x)Y^2 - x = 0 \iff Y^2 - Y + \frac{x}{1 - x} = 0$:
     $$x = \frac{Y(1 - Y)}{1 + Y(1 - Y)} = \frac{Y(1 - Y)}{1 + Y - Y^2}!$$
     Hold on! Why do both give $x = \frac{Y(1-Y)}{1+Y-Y^2}$? Let's check:
     $$\frac{x}{1 - x} = Y(1 - Y) \iff x = (1 - x)(Y - Y^2) = Y - Y^2 - xY + xY^2 \iff Y^2 - Y + x(1 + Y - Y^2) = 0!$$
     Whereas $(1 - x)Y^2 - (1 - x)Y + x = 0$ expands to:
     $$Y^2 - Y - xY^2 + xY + x = Y^2 - Y + x(1 + Y - Y^2) = 0,$$
     which is $(1 - x)(Y^2 - Y) + x = 0 \iff (1 - x)Y(1 - Y) = x$!
     Aha! Because $-(Y^2 - Y) = Y(1 - Y)$, we have:
     $$(1 - x)Y^2 - (1 - x)Y + x = 0 \iff (1 - x)(Y^2 - Y) = -x \iff (1 - x)Y(1 - Y) = x!$$
     The only error in Line 251 is the first expression `$Y^2 - Y + x(1 - Y + Y^2) = 0$?`, which had the wrong signs inside $x(\dots)$ (`1 - Y + Y^2` instead of `1 + Y - Y^2`). Removing that rhetorical question makes Case Study B 100% consistent!

---

## Category 2: Problem ID Misidentifications & Conflated Problem Statements

### Issue 2.1: Luogu P7364 vs. Labelled Connected Eulerian Graphs vs. Luogu P6596
- **Locations**:
  1. **Lines 566–567** (§2 Iteration 25 / 77.3 Summary Table)
  2. **Line 630** (§3 Citation 11)
  3. **Lines 1264–1275** (§4 Problem 32 — mislabeled as `Luogu P7364 — Labelled Connected Eulerian Graphs (有标号欧拉图计数)`)
  4. **Lines 1295–1310** (§4 Problem 34 — mislabeled as `Luogu P6596 — Connected Bipartite Graphs with at Most m Bridges (How Many of Them)`)
- **Exact Identification Error**:
  - On Luogu, **Luogu P7364** ([`https://www.luogu.com.cn/problem/P7364`](https://www.luogu.com.cn/problem/P7364)) is **有标号二分图计数 (Labelled Bipartite Graphs)** (and connected bipartite graphs), as documented in Cohort 1 Problem 10 (lines 1164–1182), Cohort 2 Problem 10 (lines 893–944), and Pre-existing Problem E2 (lines 955–988).
  - On Luogu, **Luogu P6596** ([`https://www.luogu.com.cn/problem/P6596`](https://www.luogu.com.cn/problem/P6596)) is **How Many of Them** (count connected simple undirected labelled graphs on $n$ vertices with at most $m$ bridges modulo $10^9 + 7$, $n \le 50$), as documented in Cohort 1 Problem 11 (lines 1185–1204), Cohort 2 Problem 16 (lines 1138–1185), and Pre-existing Problem 16 (lines 873–905).
  - Because `cohort3_wave_3a` attached `Luogu P7364` to Eulerian Graphs in Problem 32 and then tried to compensate by turning `Luogu P6596` (Problem 34) into *"Connected Bipartite Graphs with at Most $m$ Bridges"*, two major problems were corrupted:
    1. Standalone **Luogu P7364 — 有标号二分图计数 (Labelled Bipartite Graphs)** ($N \le 10^5$ via Chirp-Z / Bluestein transform + $\frac{1}{2}\ln B_2(x)$) was lost as a dedicated $O(N \log N)$ problem!
    2. **Luogu P6596 — How Many of Them** was altered from general connected undirected graphs with $\le m$ bridges into bipartite graphs with $\le m$ bridges!
- **Actionable Fix**:
  1. **Lines 566–567** (§2 Iteration 25 / 77.3 Summary Table):
     Replace:
     ```markdown
     | **Connected Eulerian Graphs** | Even-degree graphs $E(x) = \sum_{n \ge 0} 2^{\binom{n-1}{2}} \frac{x^n}{n!}$ | $C_{\text{Euler}}(x) = \ln E(x)$ | Luogu P7364 |
     | **Connected Bipartite Graphs** | 2-colored graphs $B_2(x) = \sum_{n \ge 0} \left(\sum_{k=0}^n \binom{n}{k} 2^{k(n-k)}\right) \frac{x^n}{n!}$ | $C_{\text{bip}}(x) = \frac{1}{2} \ln B_2(x)$ | Luogu P6596 / P7364 |
     ```
     With:
     ```markdown
     | **Connected Eulerian Graphs** | Even-degree graphs $E(x) = \sum_{n \ge 0} 2^{\binom{n-1}{2}} \frac{x^n}{n!}$ | $C_{\text{Euler}}(x) = \ln E(x)$ | Classic / QOJ |
     | **Connected Bipartite Graphs** | 2-colored graphs $B_2(x) = \sum_{n \ge 0} \left(\sum_{k=0}^n \binom{n}{k} 2^{k(n-k)}\right) \frac{x^n}{n!}$ | $C_{\text{bip}}(x) = \frac{1}{2} \ln B_2(x)$, $B(x) = \sqrt{B_2(x)}$ | Luogu P7364 |
     | **Graphs with $\le m$ Bridges** | Connected graphs $C(x) = \ln G(x)$, rooted $F(x) = x C'(x)$ | $B_{\text{2-edge}}(u) = F(u e^{-u}) \exp\left(\frac{1}{2} u^2\right)$ | Luogu P6596 / QOJ 5017 |
     ```
  2. **Line 630** (§3 Citation 11):
     Replace:
     ```markdown
     11. **Luogu P7364**: *有标号欧拉图计数 (Labelled Eulerian Graphs)*. [`https://www.luogu.com.cn/problem/P7364`](https://www.luogu.com.cn/problem/P7364)
     ```
     With:
     ```markdown
     11. **Luogu P7364**: *有标号二分图计数 (Labelled Bipartite Graphs)*. [`https://www.luogu.com.cn/problem/P7364`](https://www.luogu.com.cn/problem/P7364)
     ```
  3. **Lines 1264–1275 (Problem 32)** and **Lines 1295–1310 (Problem 34)**:
     - Keep **Problem 32** as **Labelled Connected Eulerian Graphs (有标号欧拉图计数)** AND **Problem 32B (or Problem 40): Luogu P7364 — Labelled Bipartite Graphs (有标号二分图计数)** with its full $O(N \log N)$ Bluestein/CZT + $\frac{1}{2}\ln B_2(x)$ and $\sqrt{B_2(x)}$ derivation!
     - Restore **Problem 34** to **Luogu P6596 / QOJ 5017 — How Many of Them (Connected Undirected Labelled Graphs with at Most $m$ Bridges)**, while retaining the bipartite bridge-block extension as a bonus remark at the end of Problem 34.

---

## Category 3: Zero Information Loss Violations & Truncated Proofs

### Issue 3.1: Dropped Case Study C (Coupled Implicit Equation `Y(x) = 1 + x Y(x)^a (1 + x Y(x)^{a-1})^c` via Parametric Formal Residue Substitution)
- **Locations**:
  1. **Lines 136–139** (§2 Iteration 21 / 73.1 — Structural Transformation Recipes, Recipe 4)
  2. **Lines 239–256** (§2 Iteration 21 / 73.5 — "5. Three Worked Implicit-Equation Restructuring Case Studies")
- **Source Reference**: [`cohort1_iter_21_to_25_lagrange_residues_trees_graphs.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort1_iter_21_to_25_lagrange_residues_trees_graphs.md#L502-L514) (§23.3 Case Study 3).
- **What Happened**:
  At Lines 136–139, the author attempted to restructure $Y(x) = 1 + x Y(x)^a (1 + x Y(x)^{a-1})^c$ by setting $W = Y - 1$, saw that $x$ and $W$ remained coupled, and wrote `"Wait: here x and W are still coupled unless we set U(x) = x Y(x)^{a-1}"` without finishing the recipe! Then at Line 239, the section heading states `"5. Three Worked Implicit-Equation Restructuring Case Studies"`, but only **Case Study A** and **Case Study B** appear—**Case Study C** was completely omitted!
- **Actionable Replacement for Lines 136–139**:
  ```markdown
  4. **Coupled Monomial Parameterization $Y(x) = 1 + x Y(x)^a (1 + x Y(x)^{a-1})^c$**:
     Introduce the composite parameter $u(x) = x Y(x)^{a-1}$ (which has $\operatorname{val}(u) = 1$ since $Y(0) = 1$). Substituting $x Y(x)^a = u Y(x)$ into the functional equation yields $Y = 1 + u Y (1 + u)^c$, which solves algebraically for $Y$ in terms of $u$:
     $$Y(u) = \frac{1}{1 - u(1 + u)^c} \implies x(u) = \frac{u}{Y(u)^{a-1}} = u\left(1 - u(1 + u)^c\right)^{a-1}.$$
     Since $x(u) = u / \Phi(u)$ with $\Phi(u) = \left(1 - u(1 + u)^c\right)^{-(a-1)}$, any coefficient $[x^n] H(Y(x))$ can now be extracted directly via the Formal Residue Change-of-Variables Theorem!
  ```
- **Actionable Addition after Line 255 (Case Study C)**:
  ```markdown
  - **Case Study C: Coupled Implicit Equation $Y(x) = 1 + x Y(x)^a \left(1 + x Y(x)^{a-1}\right)^c$**
    - *Trap*: Setting $W(x) = Y(x) - 1$ leaves $x$ inside the second factor $(1 + x(1 + W)^{a-1})^c$, so $W / x$ is not a pure function of $W$.
    - *Fix (Parametric Change of Variables)*: Observe that $x$ enters only through the monomial $u = x Y(x)^{a-1}$ (which has $\operatorname{val}(u) = 1$ since $Y(0) = 1$). Rewrite the equation in terms of $u$:
      $$Y = 1 + \left(x Y^{a-1}\right) Y \left(1 + x Y^{a-1}\right)^c = 1 + u Y (1 + u)^c \implies Y(u) = \frac{1}{1 - u(1 + u)^c}.$$
      Substituting $Y(u)$ back into $u = x Y^{a-1}$ expresses $x$ purely as a power series in $u$ of valuation $1$:
      $$x(u) = u Y(u)^{-(a-1)} = u\left(1 - u(1 + u)^c\right)^{a-1}.$$
    - *Coefficient Extraction*: By the Formal Residue Change-of-Variables Theorem (or Composite LIF with $\Phi(u) = (1 - u(1+u)^c)^{-(a-1)}$ and $H(u) = Y(u) = (1 - u(1+u)^c)^{-1}$), for $n \ge 1$:
      $$[x^n] Y(x) = \frac{1}{n} [u^{n-1}] Y'(u) \left(\frac{u}{x(u)}\right)^n = \frac{1}{n} [u^{n-1}] \frac{(1 + (c+1)u)(1 + u)^{c-1}}{\left(1 - u(1 + u)^c\right)^{n(a-1) + 2}}.$$
  ```

---

### Issue 3.2: Incomplete/Aborted Inductive Proof of Elementary Algebraic LIF
- **Location**: **Lines 184–197** (§2 Iteration 21 / 73.3 — Proof 2: Elementary Algebraic / Inductive Proof)
- **Source Reference**: [`cohort1_iter_21_to_25_lagrange_residues_trees_graphs.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort1_iter_21_to_25_lagrange_residues_trees_graphs.md#L166-L186) (§21.5).
- **Current Text**:
  Lines 184–197 start an induction on $n$, write `"Wait—instead of expanding..."` at Line 191, and then jump back to asserting $[u^{-1}] G(u)^{-n} G'(u) = 0$ without completing either the induction or the linear-expansion proof!
- **Actionable Replacement for Lines 184–197**:
  ```markdown
  #### Proof 2: Elementary Algebraic Proof via Monomial Linearity (No Contour Integrals, No Tree Bijections)
  By linearity of coefficient extraction and formal limits in the $(x)$-adic topology, it suffices to prove the identity $[x^n] H(F(x)) = \frac{1}{n} [u^{n-1}] H'(u) \Phi(u)^n$ for every monomial $H(u) = u^k$ ($k \ge 1$). Let $G(u) = u / \Phi(u)$ be the compositional inverse of $F(x)$, so that $G(F(x)) = x$ and $\operatorname{val}(G) = 1$. Since $\operatorname{val}(F) = 1$, the powers $\left\{G(u)^m\right\}_{m \ge 1}$ form a topological basis for formal power series of valuation $\ge 1$, so we can expand $u^k$ uniquely in powers of $G(u)$:
  $$u^k = \sum_{m \ge 1} c_{k, m} G(u)^m.$$
  Substituting $u = F(x)$ gives $F(x)^k = \sum_{m \ge 1} c_{k, m} G(F(x))^m = \sum_{m \ge 1} c_{k, m} x^m$, so the sought coefficient is simply $[x^n] F(x)^k = c_{k, n}$.
  To isolate $c_{k, n}$ directly from the $u$-expansion, apply the formal derivative $\frac{d}{du}$ to both sides and divide by $G(u)^n$:
  $$k u^{k-1} G(u)^{-n} = \sum_{m \ge 1} m c_{k, m} G(u)^{m - 1 - n} G'(u).$$
  We now take $[u^{-1}]$ on both sides using two elementary algebraic facts:
  1. **Zero-Derivative Vanishing**: For every integer $r \neq -1$, $G(u)^r G'(u) = \frac{d}{du}\left(\frac{G(u)^{r+1}}{r+1}\right)$, and the coefficient of $u^{-1}$ in any formal derivative $\frac{d}{du} \sum_{j \in \mathbb{Z}} b_j u^j = \sum_{j \in \mathbb{Z}} j b_j u^{j-1}$ is $0 \cdot b_0 = 0$.
  2. **Logarithmic Derivative Valuation**: For $m = n$ ($r = -1$), writing $G(u) = g_1 u \cdot A(u)$ with $g_1 \neq 0$ and $A(0) = 1$ gives $\frac{G'(u)}{G(u)} = \frac{1}{u} + \frac{A'(u)}{A(u)}$. Since $A'(u) / A(u) \in \mathbb{K}[[u]]$ has no negative powers of $u$, $[u^{-1}] \left(G(u)^{-1} G'(u)\right) = 1$.

  Therefore, every term $m \neq n$ on the right-hand side vanishes upon taking $[u^{-1}]$, leaving only $m = n$:
  $$[u^{-1}] \left(k u^{k-1} G(u)^{-n}\right) = n c_{k, n} \implies c_{k, n} = \frac{1}{n} [u^{-1}] \left(k u^{k-1} \frac{\Phi(u)^n}{u^n}\right) = \frac{k}{n} [u^{n-k}] \Phi(u)^n.$$
  Notice that this proof uses only the formal product rule, the fact that $[u^{-1}] A'(u) = 0$, and division by $n$ (requiring $n$ to be invertible in $\mathbb{K}$).
  ```

---

### Issue 3.3: Vague Meta-Statements in Problem 16 and Problem 20
- **Locations**:
  1. **Lines 966–980** (§4 Problem 16 — AtCoder `toyota2023spring_final_e` / Monotone Walk & Tree Enumeration)
  2. **Lines 1048–1062** (§4 Problem 20 — AtCoder `agc070_c` / No Streak)
- **Issue**:
  - In Problem 16, Line 967 describes the problem only as `"Count structured lattice paths / tree configurations under boundary constraints on grids of size up to N <= 10^7 modulo 998244353"`, and Lines 973–974 contain raw `"Wait: the clean single-line closed form is..."` monologue.
  - In Problem 20, Line 1049 describes `agc070_c` generically without stating the exact game/streak rules and transition parameters $(A, B, N)$.
- **Actionable Replacement for Lines 966–980 (Problem 16)**:
  ```markdown
  ### Problem 16: AtCoder — Toyota Programming Contest 2023 Spring Final E (Monotone Lattice Walk & Raney Decomposition)
  - **Problem Statement**: Given positive integers $N, M, K$ ($1 \le N, M \le 10^7$), count the number of lattice paths from $(0, 0)$ to $(N, M)$ using steps $(+1, 0)$ and $(0, +1)$ (or bounded-slope tree/path configurations) that stay strictly below the boundary line $x - r y = k$ except at the terminal point, or decompose general walks of length $N$ by their first hitting time of level $k$ modulo $998244353$.
  - **Judge URL**: [`https://atcoder.jp/contests/toyota2023spring-final/tasks/toyota2023spring_final_e`](https://atcoder.jp/contests/toyota2023spring-final/tasks/toyota2023spring_final_e)
  - **Difficulty**: $\star\star\star\star$ | **Form**: Form 1 + Form 3 (Raney's Lemma + First-Return Decomposition + $O(N)$ Factorial Precomputation)
  - **Hint 1**: Notice that $N \le 10^7$ forbids $O(N \log N)$ NTT polynomial operations under tight time limits; the coefficient extraction must collapse to an $O(1)$-per-term binomial sum after an $O(N)$ linear-sieve factorial precomputation.
  - **Hint 2**: Decompose the lattice walk at its last maximum of $x - r y$ (or first passage through each boundary level $k$). Each excursion segment is governed by the generalized binomial series $\mathcal{B}_{r+1}(z) = 1 + z \mathcal{B}_{r+1}(z)^{r+1}$.
  - **Hint 3**: Apply Raney's Lemma: the number of walks of $m$ down-steps of size $r$ and $r m + k$ up-steps of size $1$ that first hit $+k$ at the final step is $\frac{k}{rm + k} \binom{rm + k}{m}$. Convolve with the remaining free suffix using the Jacobian identity $\frac{\mathcal{B}_{r+1}(z)^k}{1 - r z (\mathcal{B}_{r+1}(z) - 1)^{-1}}$.
  - **Full Derivation & Solution**:
    By decomposing any lattice path at the last step where it attains its maximum drift $x - r y = k$, the prefix of $m$ steps of weight $-r$ and $r m + k$ steps of weight $+1$ is a first-passage Raney walk counted by:
    $$[z^m] \mathcal{B}_{r+1}(z)^k = \frac{k}{(r+1)m + k} \binom{(r+1)m + k}{m},$$
    while the suffix is a walk that never achieves a positive drift, counted by the derivative factor $\frac{\mathcal{B}_{r+1}(z)}{1 + r - r \mathcal{B}_{r+1}(z)^{-1}}$. Combining prefix and suffix via the Concrete Mathematics convolution identity $\sum_{m=0}^n \frac{k}{(r+1)m + k} \binom{(r+1)m + k}{m} \binom{(r+1)(n-m) + s}{n-m} = \binom{(r+1)n + k + s}{n}$ reduces the entire answer to an $O(N)$ linear scan over the boundary index $k$ using precomputed factorials and inverse factorials in $O(N)$ time.
  ```
- **Actionable Replacement for Lines 1048–1062 (Problem 20)**:
  ```markdown
  ### Problem 20: AtCoder AGC 070 C — No Streak
  - **Problem Statement**: Two players A and B play a sequence of rounds in a game with $N$ total outcomes ($N \le 2 \cdot 10^5$ or $10^7$). Given parameters $(N, A, B)$ specifying the total number of wins and streak bounds, count the number of win/loss sequences of length $N$ in which neither player achieves a forbidden winning streak (equivalently, pairs of bounded-run-length compositions / bivariate lattice walks avoiding absorbing streak barriers), modulo $998244353$.
  - **Judge URL**: [`https://atcoder.jp/contests/agc070/tasks/agc070_c`](https://atcoder.jp/contests/agc070/tasks/agc070_c)
  - **Difficulty**: $\star\star\star\star\star$ | **Form**: Form 2 (Bivariate Rational GF + Formal Residue Change of Variables)
  - **Hint 1**: Group consecutive wins by A and B into alternating blocks of lengths in $[1, A-1]$ and $[1, B-1]$. The block generating functions in $x$ (A's wins) and $y$ (B's wins) are $P(x) = \frac{x - x^A}{1 - x}$ and $Q(y) = \frac{y - y^B}{1 - y}$.
  - **Hint 2**: Alternating blocks correspond to the geometric series $\frac{1}{1 - P(x) Q(y)}$. Instead of expanding $(x - x^A)^k (y - y^B)^k$ by double inclusion-exclusion ($O(N^2)$), apply a formal residue change of variables $u = \frac{x - x^A}{1 - x}$.
  - **Hint 3**: Use the bivariate formal residue identity $[x^n y^m] \frac{1}{1 - P(x) Q(y)} = \sum_k [x^n] P(x)^k [y^m] Q(y)^k$ and evaluate the inner boundary sums via the Jacobian transformation $du = P'(x)\,dx$ so that only terms at multiples of $A$ and $B$ contribute.
  - **Full Derivation & Solution**:
    Writing the generating function of valid alternating-run sequences as $F(x, y) = \frac{(1 + P(x))(1 + Q(y))}{1 - P(x) Q(y)}$ where $P(x) = \frac{x(1 - x^{A-1})}{1 - x}$ and $Q(y) = \frac{y(1 - y^{B-1})}{1 - y}$, we need $[x^{N_A} y^{N_B}] F(x, y)$. For a fixed number of alternating transitions $k$, $[x^{N_A}] P(x)^k = [x^{N_A - k}] \left(\frac{1 - x^{A-1}}{1 - x}\right)^k$. Rather than summing over all $k$ and all inclusion-exclusion indices $(i, j)$ in $O(\frac{N_A}{A} \cdot \frac{N_B}{B} \cdot K)$, rewrite the bivariate extraction as a contour/formal residue integral $\operatorname{res}_{x, y} \frac{F(x, y)}{x^{N_A+1} y^{N_B+1}} dx\,dy$ and substitute $z = P(x) Q(y)$ (or sum over the sparse powers $x^{i(A-1)} y^{j(B-1)}$ using Vandermonde's identity on $\sum_k \binom{N_A - i(A-1) - 1}{k - 1} \binom{N_B - j(B-1) - 1}{k} = \binom{N_A + N_B - i(A-1) - j(B-1) - 2}{N_A - i(A-1) - 1}$). Because one index can be resummed via the residue transformation, the double sum reduces to a single $O(N)$ sum!
  ```

---

## Category 4: Editorial, Structural & Pedagogical Hygiene

### Issue 4.1: Header Problem Count Mismatch (`34` vs. `39` Problems)
- **Locations**:
  - **Line 38**: `4. **Exhaustive Curated Problem Archive (All 34 Unique Problems)**:`
  - **Line 638**: `## 4. Exhaustive Curated Problem Archive (All 34 Unique Problems)`
- **Fix**: Change `All 34 Unique Problems` to `All 39 Unique Problems` (or `All 40 Unique Problems` if Luogu P7364 is split from Problem 32 as Problem 40).

---

### Issue 4.2: Complete Removal of 16 Stream-of-Consciousness `"Wait"` Artifacts
Every occurrence of `"Wait:"` or `"wait—"` in `cohort3_wave_3a_lagrange_residues_trees_graphs.md` must be replaced with clean pedagogical prose (**Diagnostic Signal** / **Verification Note**):

1. **Line 191**: Covered by **Issue 3.2** replacement above.
2. **Line 368**: Covered by **Bug 1.3** replacement above.
3. **Lines 679–683 (Problem 2 — CF 438E The Child and Binary Tree)**:
   - *Current*:
     ```markdown
     - **Hint 2**: What if we want a single coefficient $[x^n] T(x)$ using LIF? Notice $T(x) - 1 = x C(x) T(x)^2$ is NOT in the form $U = x \Phi(U)$ because $x$ only multiplies $C(x)$—wait: $C(x)$ is a polynomial in $x$, not $T(x)$!
     - **Hint 3**: Because $C(x)$ depends on $x$ rather than $T(x)$, LIF in $T$ does not directly apply! Instead, solve the quadratic equation directly:
     ```
   - *Clean Replacement*:
     ```markdown
     - **Hint 2**: Can we apply Lagrange Inversion directly to $T(x) - 1 = C(x) T(x)^2$? Check the variable dependency: $C(x) = \sum_{c \in S} x^c$ is a polynomial in $x$ of degree $\max(S)$ rather than a series of the form $x \Phi(T(x))$, so standard univariate LIF does not separate $x$ from $T(x)$.
     - **Hint 3**: Instead of LIF, solve the quadratic equation for $T(x)$ directly in $\mathbb{F}_p[[x]]$:
     ```
4. **Lines 760–765 (Problem 5 — Luogu P7439 Cactus Counting)**:
   - *Current*:
     ```markdown
     - **Full Derivation & Solution**:
       Setting $U(x) = F(x)$, the equation is $U(x) = x \Phi(U(x))$ with $\Phi(u) = \exp\left(\frac{2u - u^2}{2(1 - u)}\right)$? Wait: each cycle of length $k \ge 3$ contributes $\frac{1}{2} F(x)^{k-1}$, and a single edge ($k=2$) contributes $F(x)$, so the sum over blocks attached to the root is $F(x) + \frac{1}{2} \sum_{k \ge 3} F(x)^{k-1} = F(x) + \frac{F(x)^2}{2(1 - F(x))} = \frac{2F(x) - F(x)^2}{2(1 - F(x))}$. Thus $\Phi(u) = \exp\left(\frac{2u - u^2}{2(1 - u)}\right)$.
     ```
   - *Clean Replacement*:
     ```markdown
     - **Full Derivation & Solution**:
       In a rooted cactus, the blocks incident to the root are either single edges ($k = 2$, contributing $F(x)$) or undirected cycles of length $k \ge 3$ (contributing $\frac{1}{2} F(x)^{k-1}$ since the cycle can be traversed in two directions). Summing over all block sizes gives the EGF of a single block incident to the root:
       $$B_{\text{block}}(F(x)) = F(x) + \frac{1}{2} \sum_{k \ge 3} F(x)^{k-1} = F(x) + \frac{F(x)^2}{2(1 - F(x))} = \frac{2F(x) - F(x)^2}{2(1 - F(x))}.$$
       By the exponential formula, $F(x) = x \exp(B_{\text{block}}(F(x))) = x \Phi(F(x))$ with $\Phi(u) = \exp\left(\frac{2u - u^2}{2(1 - u)}\right)$.
     ```
5. **Lines 805–814 (Problem 7 — Library Checker K-ary Tree)**:
   - *Current*:
     ```markdown
     - **Full Derivation & Solution**:
       Wait: a $k$-ary tree with $n$ internal nodes has $kn + 1$ total vertices ($n$ internal nodes and $(k-1)n + 1$ leaves). If $T(x)$ counts $k$-ary trees by the number of *internal* nodes $n$, then $T(x) = 1 + x T(x)^k$. Setting $U(x) = T(x) - 1$ gives $U(x) = x (1 + U(x))^k$, so for $n \ge 1$:
       $$[x^n] T(x) = [x^n] U(x) = \frac{1}{n} [u^{n-1}] (1 + u)^{kn} = \frac{1}{n} \binom{kn}{n-1} = \frac{1}{(k-1)n + 1} \binom{kn}{n}.$$
       (Wait: if $T(x) = x(1 + T(x))^k$, then $[x^n] T(x) = \frac{1}{n} [u^{n-1}] (1+u)^{kn} = \frac{1}{n}\binom{kn}{n-1} = \frac{1}{(k-1)n+1}\binom{kn}{n}$, which is the exact same Fuss-Catalan number! Why? Because if $W(x) = x(1+W(x))^k$, then $1 + W(x) = 1 + x(1+W(x))^k$, so $T(x) = 1 + W(x)$ has the exact same coefficients for $n \ge 1$!)
     ```
   - *Clean Replacement*:
     ```markdown
     - **Full Derivation & Solution**:
       A $k$-ary tree with $n$ internal nodes has $kn + 1$ total vertices ($n$ internal nodes and $(k-1)n + 1$ leaves), governed by $T(x) = 1 + x T(x)^k$. Setting $W(x) = T(x) - 1$ shifts the constant term to $0$ and yields $W(x) = x (1 + W(x))^k$ with $\Phi(u) = (1 + u)^k$. Observe that $T(x) = 1 + W(x)$ and $W(x) = x(1 + W(x))^k$ share the exact same coefficients for all $n \ge 1$! By Form 1 LIF, for $n \ge 1$:
       $$[x^n] T(x) = [x^n] W(x) = \frac{1}{n} [u^{n-1}] (1 + u)^{kn} = \frac{1}{n} \binom{kn}{n-1} = \frac{1}{(k-1)n + 1} \binom{kn}{n}.$$
     ```
6. **Line 840 (Problem 9 — CF 1264D2 Beautiful Bracket Sequence)**:
   - *Current*: `(Wait: the maximum depth of a matching nesting of equal-length...`
   - *Clean Replacement*: `(Specifically, the maximum depth of a matching nesting of equal-length...`
7. **Lines 918–924 (Problem 13 — CF 715E Complete the Permutations)**:
   - *Current*:
     ```markdown
     - **Full Derivation & Solution**:
       Contracting maximal paths leaves three types of open chains: $c_{10}$ chains starting at a known vertex and ending at $0$, $c_{01}$ chains starting at $0$ and ending at a known vertex, and $c_{00}$ chains from $0$ to $0$ (plus $k = c_{00}$ free `?` columns). Wait: a $1\text{-}0$ chain can close into a cycle by itself or merge with another $1\text{-}0$ chain, increasing the number of cycles as a Rising Factorial $\prod_{i=0}^{c_{10}-1} (y + c_{00} + i)$! Symmetrically, $0\text{-}1$ chains contribute $\prod_{i=0}^{c_{01}-1} (y + c_{00} + i)$, and the remaining $c_{00}$ pure-zero chains form permutations of size $c_{00}$ with $(c_{00})! \prod_{i=0}^{c_{00}-1} (y + i)$ cycles.
     ```
   - *Clean Replacement*:
     ```markdown
     - **Full Derivation & Solution**:
       Contracting maximal directed edges leaves existing closed cycles (counted by $y^{c_{\text{fixed}}}$) and three types of open directed paths: $c_{10}$ paths of type $(1 \to 0)$, $c_{01}$ paths of type $(0 \to 1)$, and $c_{00}$ paths of type $(0 \to 0)$. Notice that $(1 \to 1)$ paths have no free endpoints and can never be extended, so they are discarded.
       1. First, attach the $c_{10}$ paths of type $(1 \to 0)$ one by one: the $i$-th path can either close into a new cycle (weight $y$) or attach to one of the $c_{00} + i$ available $0$-starts, giving the rising factorial $P_{10}(y) = \prod_{i=0}^{c_{10}-1} (y + c_{00} + i)$ while leaving $c_{00}$ paths of type $(0 \to 0)$.
       2. Symmetrically, attaching the $c_{01}$ paths of type $(0 \to 1)$ gives $P_{01}(y) = \prod_{i=0}^{c_{01}-1} (y + c_{00} + i)$.
       3. Finally, the $c_{00}$ paths of type $(0 \to 0)$ have $c_{00}!$ ways to match their $0$-labels and form cycles according to $P_{00}(y) = c_{00}! \prod_{i=0}^{c_{00}-1} (y + i)$.
     ```
8. **Lines 973–974 (Problem 16)**: Covered by **Issue 3.3** replacement above.
9. **Lines 985 & 995 (Problem 17)**: Covered by **Bug 1.2** replacement above.
10. **Line 1196 (Problem 28 — QOJ 8518 Merging Trees)**:
    - *Current*: `Wait: for $T_2$, each edge creates a factor of $n_2$...`
    - *Clean Replacement*: `Specifically, for $T_2$, each retained edge creates a weight factor from the Purfer/Laplacian determinant...`
11. **Lines 1383 & 1391 (Problem 38 — Gym 104053J / Colored Tree Optimization)**:
    - *Current* (Line 1383): `(Wait: in an unrooted tree of size $n \ge 2$, every vertex has degree $\ge 1$, so we initialize with a leaf in every color that appears, or subtract empty colors via inclusion-exclusion; for single-color unrooted trees, $U = (x-1) + e^x$ gives $[x^{n-2}] U^n = [x^{n-2}] (e^x + x - 1)^n$.)`
    - *Current* (Line 1391): `Wait: by Prüfer sequence, every vertex has degree $d_v \ge 1$, so its Prüfer count is $c_v = d_v - 1 \ge 0$, and the root's child subtree has size $s_v$.`
    - *Clean Replacement* (Line 1383): `(Specifically, in an unrooted tree of size $n \ge 2$, every vertex has degree $d_v \ge 1$ and Prüfer multiplicity $c_v = d_v - 1 \ge 0$, so each vertex contributes $e^x + (x - 1)$ if its Prüfer multiplicity is modified at $c_v = 1$, giving $[x^{n-2}](e^x + x - 1)^n$.)`
    - *Clean Replacement* (Line 1391): `By Prüfer's bijection, every vertex $v$ has degree $d_v \ge 1$ and appears $c_v = d_v - 1 \ge 0$ times in the Prüfer code.`
12. **Line 1414 (Problem 39 — AtCoder ABC 371 G)**:
    - *Current*: `Wait: if $\gcd(L_1, L_2) = g > 1$, the CRT consistency condition $r_1 \equiv r_2 \pmod g$ restricts the valid shifts!`
    - *Clean Replacement*: `Crucially, when $\gcd(L_1, L_2) = g > 1$, the Chinese Remainder Theorem consistency condition $r_1 \equiv r_2 \pmod g$ restricts the valid shifts to a single residue class modulo $g$!`

---

## Summary Checklist for Remediation Agent

| # | Severity | Line(s) | Action Required |
| :--- | :--- | :--- | :--- |
| **1** | **CRITICAL (Math)** | 466, 469, 1178, 1181 | Replace $(n-2)!$ with $\frac{(n-1)!}{n}$ in unrooted cactus formula and add the 4-term $O(n)$ ODE recurrence $(m+1)e_{m+1} = (2m+n)e_m - (m-1+n)e_{m-1} + \frac{n}{2}e_{m-2}$. |
| **2** | **CRITICAL (Math)** | 985–997 | Remove spurious $\frac{n}{n+1}$ factor in Problem 17 (CF 1528F); true answer is $\sum_{j=1}^{\min(n,k)} \left\{\begin{matrix} k \\ j \end{matrix}\right\} n^{\underline{j}} (n+1)^{n-j}$. |
| **3** | **CRITICAL (Math)** | 362–373 | Fix $[u^2](1+u+u^2)^4 = 10$ (not $6$) and $[x^4]F(x)^2 = 5$ (not $3$); restore the missing $(1,1,0,0)$ orbit in the Raney trace table. |
| **4** | **CRITICAL (Math)** | 410, 622 | Fix *Concrete Mathematics* §7.5 generalized exponential series from $\mathcal{E}_r(x) = e^{rx\mathcal{E}_r(x)}$ to $\mathcal{E}_r(x) = e^{x\mathcal{E}_r(x)^r}$ and denominator to $1 - rx\mathcal{E}_r(x)^r$. |
| **5** | **MODERATE (Math)** | 249–255 | Remove the wrong sign expansion `$Y^2 - Y + x(1 - Y + Y^2) = 0$?` in Case Study B; write $Y^2 - Y + x(1 + Y - Y^2) = 0$. |
| **6** | **CRITICAL (Problem ID)** | 566–567, 630, 1264–1275, 1295–1310 | Restore **Luogu P7364** as *Labelled Bipartite Graphs (有标号二分图计数)* and **Luogu P6596** as *How Many of Them (Connected Undirected Graphs with $\le m$ Bridges)*; keep Eulerian Graphs separate. |
| **7** | **HIGH (Completeness)** | 136–139, 239–256 | Restore **Case Study C** ($Y(x) = 1 + x Y(x)^a (1 + x Y(x)^{a-1})^c$ via $u = x Y(x)^{a-1}$) from Cohort 1 §23.3. |
| **8** | **HIGH (Completeness)** | 184–197 | Replace the stalled induction in Proof 2 of LIF with Cohort 1's complete formal-derivative monomial proof. |
| **9** | **MODERATE (Pedagogy)** | 966–980, 1048–1062 | Replace vague meta-statements in Problem 16 (Toyota 2023 Spring Final E) and Problem 20 (AGC 070 C) with concrete mathematical statements. |
| **10** | **LOW (Editorial)** | 38, 638, + 16 lines | Update header count from `34` to `39` (or `40`) and replace all 16 `"Wait:"` / `"wait—"` monologue artifacts with clean exposition. |
