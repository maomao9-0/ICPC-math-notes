# Wave 4A (Cohort 3 Master Reconciliation — Iteration 111): Goulden–Jackson Cluster Method, String PGFs / Martingales, Automaton DP & DFA Minimization (`DP套DP`)

> [!IMPORTANT]
> **Cohort 3 Cross-Comparison, Blind-Spot Audit & Reconciled Master Treatise**
> - **Iteration & Wave**: Iteration 111 (Cohort 3 Reconciliation for **Wave 4A**)
> - **Source Files Reconciled**:
>   - **Cohort 1 (Iterations 31–35)**: `strings_research/iter_31_to_35_goulden_jackson_pgf_automaton_dp.md`
>   - **Cohort 2 (Iterations 83–87)**: `strings_research/cohort2_iter_83_to_87_goulden_jackson_pgf_automaton_dp.md`
> - **Editorial & Pedagogical Standard**: Every theorem, algebraic system, probabilistic stopping argument, and practice problem in this reconciled master document strictly enforces the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**:
>   1. *The Diagnostic Signal (Why Naive String / Automaton Structures Fail)*
>   2. *The Combinatorial Word Invariant (Double-Overlap / Cluster / Martingale / Nerode Proof)*
>   3. *The Reverse-Engineering Scratchpad (Algorithmic & Algebraic Compilation)*
>   4. *Boundary Pitfalls & Broken-Invariant Counterexamples*

---

## 1. Cross-Cohort Comparison, Blind-Spot Audit & Reconciliation Matrix

A line-by-line audit of Cohort 1 (`iter_31_to_35_goulden_jackson_pgf_automaton_dp.md`, 794 lines) and Cohort 2 (`cohort2_iter_83_to_87_goulden_jackson_pgf_automaton_dp.md`, 762 lines) revealed substantial complementary discoveries. Below is the complete cross-cohort blind-spot ledger detailing what each cohort uniquely captured and how both are unified in this Cohort 3 synthesis.

### 1.1 What Cohort 1 Captured That Cohort 2 Missed

1. **Explicit Guibas–Odlyzko End-Tagged Word Formulation & Cluster Ratio Identity**:
   - Cohort 1 derived the unsigned **Guibas–Odlyzko $(m+1) \times (m+1)$ OGF System** alongside the signed Goulden–Jackson cluster system: by appending $P_j$ to a $\mathcal{P}$-avoiding word $W$ (counted by $F(x)x^{|P_j|}$) and decomposing at the *first* occurrence $P_i \in \mathcal{P}$ (counted by $F_i(x)$), Cohort 1 proved
     $$F(x) x^{|P_j|} = \sum_{i=1}^m F_i(x) C_{i,j}(x), \qquad (1 - \sigma x) F(x) + \sum_{i=1}^m F_i(x) = 1,$$
     and established the exact duality identity $\dfrac{F_i(x)}{F(x)} = -C_i(x)$ (the signed cluster GF $C_i(x)$ is literally the negative ratio of the first-hit end-tagged GF $F_i(x)$ to the avoidance GF $F(x)$!).
2. **Combinatorial 3-Factor Proof of $F_k(x) = \frac{x^L D_1(x)^{k-1}}{D_0(x)^{k+1}}$ & FPS $\ln/\exp$ Valuation Pitfall**:
   - While both cohorts derived the rational form of $[t^k] F(x, t)$ algebraically, Cohort 1 additionally gave the **direct bijective 3-piece decomposition** of a word with *exactly* $k$ occurrences of $P$: (1) prefix up to first occurrence $\frac{x^L}{D_0(x)}$, (2) $k-1$ inter-occurrence transitions $\left(\frac{D_1(x)}{D_0(x)}\right)^{k-1}$ (either overlapping along a proper border or restarting after an avoiding bridge), and (3) avoiding suffix $\frac{1}{D_0(x)}$.
   - Cohort 1 also caught a critical implementation bug when computing $D_1(x)^{k-1}$ via FPS $\ln/\exp$: while $D_0(0) = 1$, **$D_1(0) = 0$**! Specifically, the lowest nonzero term of $D_1(x) = (1 - \sigma x)(C_P(x) - 1) + x^L$ has degree $d = \min\text{Period}(P) = L - \max\text{ProperBorder}(P) \ge 1$, which must be factored out before calling `poly_ln`.
3. **Unique Structural Paradigms & Contest Problems in Cohort 1**:
   - **Dynamic Online AC Automaton via Binary Grouping (`二进制分组`, `CF 710F`)**: Maintaining $O(\log M)$ immutable AC automata of sizes $2^k$ to support online insertions, deletions, and occurrence queries in $O((\sum |P| + \sum |T|) \log M)$.
   - **Offline Trie DFS $\times$ AC `fail`-Tree Euler Tour + Fenwick Tree (`CF 1207G — Indie Album`)**: Answering $(s_i, P_j)$ occurrence queries where texts $s_i$ form a Trie.
   - **SAM DAG Path-Counting vs. Link-Tree Subtree Multiplicity (`[TJOI2015] 弦论`)**: Distinguishing $w(u) = 1$ (distinct substrings) from $w(u) = |\text{endpos}(u)|$ (total occurrences) in SAM DAG DP.
   - **Greedy Root-Reset AC Partition Matrix (`[BJWC2011] 禁忌`)**: Redirecting `bad[v]` transitions immediately back to the root $q_0$ with $+1$ score reward.
   - **Bitwise `fail`-Mask DP (`[HNOI2004] L语言`)**: Compressing dictionary word lengths on AC `fail` chains into a 20-bit machine word `len_mask[u]`.
   - **Digit LIS Patience-Sorting `DP套DP` (`HDU 4352 — XHXJ's List`)**: Encoding the $O(N \log N)$ LIS patience-sorting array as a 10-bit subset mask $\in [0, 2^{10})$.
   - **Two-Sided Overhang Palindromic Concatenation DFA (`AtCoder ABC 249 G / ARC 141 D`)** and **Palindromic Goulden–Jackson** (center-straddling symmetric clusters).
   - **Multilingual Rosetta Stone Table (`[EN]` $\leftrightarrow$ `[ZH]` $\leftrightarrow$ `[JA]`)** and formal academic citations (Goulden–Jackson 1979, Guibas–Odlyzko 1981, Noonan–Zeilberger 1999, Li 1980, Liu Jiahua 2018).

### 1.2 What Cohort 2 Captured That Cohort 1 Missed

1. **Formal Commutative Ring Invertibility Theorem & Gaussian Elimination Pivot Invariant**:
   - Cohort 2 explicitly proved why the Goulden–Jackson matrix $\mathbf{C}(x) = [C_{i,j}(x)]$ is invertible over $R[[x]]$ for *any* commutative ring $R$ (regardless of characteristic): under the Antichain Invariant, $C_{j,j}(0) = 1$ and $C_{i,j}(0) = 0$ ($i \ne j$), so $\mathbf{C}(0) = I_m$ and $\det \mathbf{C}(x) \in 1 + x R[x]$ is always a unit in $R[[x]]$.
   - Cohort 2 also identified the **Gaussian Elimination Off-Diagonal Pivot Trap** over $\mathbb{F}_p[[x]]$: one must pivot strictly on the diagonal entry $C_{j,j}(x)$ (whose constant term is $1$), because off-diagonal entries $C_{i,j}(x)$ ($i \ne j$) have constant term $0$ and are non-invertible in $\mathbb{F}_p[[x]]$.
2. **The $t = 1 + u$ Binomial Moment Shift Trick (`Universal Cup / QOJ` $\mathbb{E}[\text{occ}_P(W)^K]$)**:
   - Cohort 2 discovered a major algebraic shortcut for computing $K$-th moments $\sum_{W \in \Sigma^n} \text{occ}_P(W)^K$ when $n \le 10^{18}, |P| \le 10^5, K \le 20$: instead of expanding $F(x, t)$ in powers of $t$ around $t = 0$ (where $[t^k] F(x, t)$ has denominator $D_0(x)^{k+1}$ of degree $(k+1)L$), substitute **$t = 1 + u$** (expanding around $t = 1$)!
   - In $u = t - 1$, the denominator collapses from $D_0(x)^{j+1}$ to the trivial monomial power **$(1 - \sigma x)^{j+1}$**:
     $$[u^j] F(x, 1 + u) = \sum_{W \in \Sigma^*} \binom{\text{occ}_P(W)}{j} x^{|W|} = \frac{x^L \Bigl((1 - \sigma x)\bigl(C_P(x) - 1\bigr) + x^L\Bigr)^{j-1}}{(1 - \sigma x)^{j+1}},$$
     turning $[x^n][u^j]F(x, 1+u)$ into a direct binomial-coefficient convolution computable in $O(K L \log(KL))$ without Bostan–Mori!
3. **Explicit Non-Antichain Embedded Substring Weight-Absorption Formula**:
   - While Cohort 1 noted qualitatively that nested patterns in weighted problems ($t_i \ne 0$) can be absorbed into super-patterns, Cohort 2 derived the **exact multiplicative adjustment**: when $P_i \subsetneq P_j$, marking $P_j$ absorbs all internal occurrences of $P_i$ via $\widetilde{W}_j = (w_j - 1) \prod_{P_i \subsetneq P_j} w_i^{\text{occ}(P_i, P_j)}$, while overlap transitions $C_{a,b}$ divide by $\prod_{P_i \subseteq P_b[1..k]} w_i$ (to cancel double-counted occurrences inside the overlap) and multiply by $\prod_{P_i \text{ straddling}} w_i$.
4. **Multivariate Cyclic Cluster Cancellation (`AtCoder AGC 058 D — Yet Another ABC String`)**:
   - Cohort 2 showed how applying the Goulden–Jackson cluster GF to $\mathcal{P} = \{\texttt{ABC}, \texttt{BCA}, \texttt{CAB}\}$ yields $\sum_{L \ge 3} w_L x^L = \frac{-3x^3}{1 + x + x^2}$, which **cancels all clusters of length $L \equiv 2 \pmod 3$ to zero** and reduces 3-variable exact letter counting ($x^A y^B z^C$) to a 1D multinomial sum in $O(\min(A, B, C))$.
5. **Explicit Hopcroft Partition-Refinement Trace & Additional Problems in Cohort 2**:
   - Worked 6-state-to-2-state trace of Hopcroft's algorithm on an inner DP DFA, plus `POJ 2778`, `CSES 1112`, `ARC 058 E` (Unary Prefix-Sum Bitmask DFA), `BZOJ 3864` (`Hero meet devil`), `UVa 11468`, `CF 1349D` (Initial-Seed Martingale Potential Subtraction), Palindrome-Avoiding Restricted-Growth String DFA, and Random Walk with Reset/Backspace on KMP (`dp[u] = E[u] - E[u+1]`).

---

## 2. Frontier & Obscure `[ZH]` / `[JA]` / `[EN]` Technique Hunt (Closing Remaining Wave 4A Blind Spots)

To ensure zero gaps before Phase 1.5 curriculum design, we conducted a targeted hunt for frontier and niche results across Chinese National Team papers (`国家集训队论文`), Japanese grandmaster blogs (`maspypy`, `noshi91`), and analytic combinatorics literature (Flajolet–Sedgewick, Bassino–Nicaud). Five frontier extensions are integrated below:

### 2.1 Frontier Extension 1: Rank-1 Sherman–Morrison Reduction of Multi-Pattern Goulden–Jackson Systems
In both Cohort 1 and Cohort 2, solving for the avoidance OGF $F(x)$ with $m$ patterns was written as solving for $C_1(x), \dots, C_m(x)$ from $\sum_{i=1}^m C_i(x) C_{i,j}(x) = -x^{|P_j|}$ and plugging into $F(x) = \bigl(1 - \sigma x - \sum_{i=1}^m C_i(x)\bigr)^{-1}$.
What if we also want the first-hit generating functions $F_1(x), \dots, F_m(x)$ (or stopping-time PGFs $F_i(z)$ at arbitrary $z$, not just $z = 1$)?
- By Guibas–Odlyzko duality ($F_i(x) = -F(x) C_i(x)$), let $u_i(x) = -C_i(x)$ be the solution to the $m \times m$ system:
  $$\sum_{i=1}^m u_i(x) C_{i,j}(x) = x^{|P_j|} \quad (1 \le j \le m).$$
- Then the avoidance GF and every first-hit GF are given simultaneously by:
  $$F(x) = \frac{1}{1 - \sigma x + \sum_{i=1}^m u_i(x)}, \qquad F_i(x) = \frac{u_i(x)}{1 - \sigma x + \sum_{r=1}^m u_r(x)}.$$
- **Determinantal Rational Form (Bassino–Nicaud / Cramer's Rule)**: Let $\mathbf{C}(x) = [C_{i,j}(x)]_{m \times m}$ and $\mathbf{x} = (x^{|P_1|}, \dots, x^{|P_m|})^T$. By the Matrix Determinant Lemma (rank-1 update),
  $$F(x) = \frac{\det \mathbf{C}(x)}{(1 - \sigma x) \det \mathbf{C}(x) + \mathbf{1}^T \text{adj}(\mathbf{C}(x)) \mathbf{x}} = \frac{\det \mathbf{C}(x)}{\det\bigl((1 - \sigma x) \mathbf{C}(x) + \mathbf{x} \mathbf{1}^T \mathbf{C}(x)\bigr) / (1 - \sigma x)^{m-1}}.$$
  This bounds the numerator and denominator degrees of $F(x)$ tightly by $\sum_{i=1}^m |P_i|$, proving that the minimal linear recurrence for $a_n = [x^n]F(x)$ has order **at most $\sum_{i=1}^m |P_i|$** (and often much smaller when overlaps share common borders!).

### 2.2 Frontier Extension 2: Conditional Pattern Racing from a Non-Empty Initial Seed Prefix $S_0$ (`已知初始前缀的康威赌博`)
What if the random string stream does **not** start empty, but begins with a given prefix $S_0 \in \Sigma^*$ that has not yet triggered any pattern in $\mathcal{P} = \{P_1, \dots, P_m\}$?
- **The Diagnostic Trap**: In standard Conway's Casino Martingale (`Iteration 32 / 84`), the initial wealth of all gamblers at $t = 0$ is $M_0 = 0$. When $S_0 \ne \epsilon$ is already written on the tape at $t = 0$, gamblers who started betting inside $S_0$ and matched a suffix of $S_0$ against a prefix of $P_j$ are **already alive at $t = 0$**!
- **The Combinatorial Word Invariant**:
  At $t = 0$ (after $S_0$ is on the tape), the initial fortune already held by gamblers targeting $P_j$ is deterministically:
  $$\Omega_{S_0, P_j} = \sum_{\substack{1 \le k \le \min(|S_0|, |P_j|) \\ S_0[|S_0|-k+1..|S_0|] = P_j[1..k]}} \frac{1}{\mathbb{P}(P_j[1..k])}.$$
  Since $M_t = (\text{wealth at step } t) - t$ is a martingale starting at $M_0 = \Omega_{S_0, P_j}$, Doob's Optional Stopping Theorem at $T = \min_i T_{P_i}$ gives $\mathbb{E}[M_T] = M_0$, which modifies the $(m+1) \times (m+1)$ linear system to:
  $$\boxed{\sum_{i=1}^m \pi_i \, \Omega_{P_i, P_j} - \mathbb{E}[T \mid S_0] = \Omega_{S_0, P_j} \quad \forall j \in \{1, \dots, m\}, \qquad \sum_{i=1}^m \pi_i = 1.}$$
  In particular, for a single pattern $S$ ($m = 1$, $\pi_1 = 1$) starting from seed prefix $S_0$:
  $$\mathbb{E}[T_S \mid S_0] = \Omega_{S, S} - \Omega_{S_0, S} = \sum_{k \in \text{Borders}(S)} \frac{1}{\mathbb{P}(S[1..k])} - \sum_{k \in \text{Overlap}(S_0, S)} \frac{1}{\mathbb{P}(S[1..k])}.$$

### 2.3 Frontier Extension 3: Renewal Theory & Expected Waiting Time for the $k$-th Overlapping vs. Non-Overlapping Occurrence
Suppose we generate random characters until a single pattern $S$ ($|S| = L$) has appeared **$k$ times** at stopping time $T_{S, k}$.
1. **Case A (Overlapping Occurrences Counted)**:
   Once the 1st occurrence of $S$ finishes at time $T_{S, 1}$, the string on the tape ends with $S$ itself!
   To reach the 2nd occurrence of $S$, we are starting from the initial seed prefix $S_0 = S$, EXCEPT we require at least $1$ new character to be drawn (so the existing full match $r = L$ does not immediately count as the 2nd occurrence, while all **proper borders** $r \in \text{ProperBorders}(S)$ DO remain alive as active gamblers!).
   Therefore, at time $T_{S, 1}$, the surviving gamblers targeting the next occurrence of $S$ hold initial fortune:
   $$W_{\text{proper}} = \sum_{\substack{r \in \text{Borders}(S) \\ 1 \le r < L}} \frac{1}{\mathbb{P}(S[1..r])} = \mathbb{E}[T_{S, 1}] - \frac{1}{\mathbb{P}(S)}.$$
   By the Seed-Prefix Martingale Formula (Section 2.2), the expected additional waiting time $\Delta T = T_{S, r+1} - T_{S, r}$ between any two consecutive overlapping occurrences of $S$ is:
   $$\mathbb{E}[T_{S, r+1} - T_{S, r}] = \mathbb{E}[T_{S, 1}] - W_{\text{proper}} = \frac{1}{\mathbb{P}(S)} \quad \left(= \sigma^L \text{ in the uniform case}\right)!$$
   Thus, for every $k \ge 1$, the expected time to the $k$-th overlapping occurrence of $S$ is simply:
   $$\boxed{\mathbb{E}[T_{S, k}^{\text{overlap}}] = \mathbb{E}[T_{S, 1}] + (k - 1) \frac{1}{\mathbb{P}(S)} = \sum_{\substack{r \in \text{Borders}(S) \\ 1 \le r < L}} \frac{1}{\mathbb{P}(S[1..r])} + \frac{k}{\mathbb{P}(S)}.}$$
2. **Case B (Non-Overlapping / Buffer-Reset Occurrences Counted)**:
   If the buffer resets to $\epsilon$ after each occurrence of $S$, the renewals are i.i.d. copies of $T_{S, 1}$, giving $\mathbb{E}[T_{S, k}^{\text{disjoint}}] = k \, \mathbb{E}[T_{S, 1}]$.

### 2.4 Frontier Extension 4: Cyclic Goulden–Jackson Cluster Method (Avoiding Forbidden Substrings on a Circle / Necklace)
How many circular strings (or length-$n$ words where boundary wrap-around occurrences of $\mathcal{P}$ are also forbidden) avoid $\mathcal{P} = \{P_1, \dots, P_m\}$ when $L = \sum |P_i|$ is too large for $\text{Tr}(M^n)$ on the AC transition matrix?
- **The Combinatorial Word Invariant (Rooted Circular Marked Words)**:
  On a circle of $n$ positions $1, 2, \dots, n \pmod n$, a marked circular word $(W, M)$ has a collection of marked occurrences $M$. Assuming $n \ge \max |P_i|$ so no single occurrence wraps all the way around itself:
  - Case 1 (**All-Covering Circular Cluster**): The union of marked intervals in $M$ covers all $n$ positions of the circle, or wraps across the boundary $n \to 1$.
  - Case 2 (**Rooted Linear Decomposition via Logarithmic Derivative**): If every cluster has length $< n$, a circular marked word that is *not* completely covered by a single wrap-around cluster consists of a cyclic sequence of $r \ge 1$ items (free letters $\sigma x$ and linear clusters $C(x)$).
  In generating function terms, a rooted cycle of linear items where position $1$ is marked by $x \frac{d}{dx}$ gives:
  $$\sum_{n \ge 1} a_n^{\text{cyc}} x^n = x \frac{d}{dx} \ln \frac{1}{1 - \sigma x - C(x)} + R_{\text{wrap}}(x) = \frac{\sigma x + x C'(x)}{1 - \sigma x - C(x)} + R_{\text{wrap}}(x),$$
  where $R_{\text{wrap}}(x)$ corrects for circular clusters that wrap around the entire circle of length $n$ (overlapping the tail of the last pattern in the cluster with the head of the first pattern in the cluster!). Specifically, the non-wrapping rooted cluster term $\frac{\sigma x + x C'(x)}{1 - \sigma x - C(x)}$ already weights a linear cluster of length $L$ by $L$ (its $L$ possible cyclic rotations on a circle of length $n \ge L$), while clusters that wrap completely around the circle of length $n$ correspond to $\text{Tr}\bigl((-\widetilde{\mathbf{C}}(x))^k\bigr)$ where the last pattern overlaps the first pattern across the seam!

### 2.5 Frontier Extension 5: Brzozowski's Double-Reversal Minimization vs. Hopcroft's Partition Refinement in `DP套DP`
In `DP套DP` automaton synthesis (`Iteration 33 / 85`), we often start from a Nondeterministic Finite Automaton (NFA) $\mathcal{A}$ (or an over-specified inner DP). Two canonical minimization pipelines exist:
1. **Reachable Subset Construction + Hopcroft's Algorithm**: Run BFS from $\{q_0\}$ to build only the reachable DFA states $Q_{\text{reach}}$, then refine partitions $\Pi_0 = \{F, Q_{\text{reach}} \setminus F\}$ in $O(|\Sigma| |Q_{\text{reach}}| \log |Q_{\text{reach}}|)$ time.
2. **Brzozowski's Algebraic Minimization Theorem (1962)**:
   For any NFA/DFA $\mathcal{A}$, let $\text{rev}(\mathcal{A})$ be the NFA obtained by reversing all transition arrows and swapping initial and accepting states, and let $\text{det}(\mathcal{B})$ be the reachable subset construction from the initial state set of $\mathcal{B}$. Then:
   $$\mathcal{M}_{\min} \cong \text{det}\Bigl(\text{rev}\bigl(\text{det}(\text{rev}(\mathcal{A}))\bigr)\Bigr)!$$
   *Why it matters in competitive programming*: If you already wrote the 20-line BFS subset construction function `det(NFA)` for `DP套DP`, you do not even need to code Hopcroft's partition refinement! Calling `det(rev(det(rev(A))))` twice automatically outputs the **exact Myhill–Nerode minimal DFA**!

---

## 3. Master Reconciled Treatise — Module A: The Goulden–Jackson Cluster Method & Autocorrelation Linear Systems

### 3.1 The Diagnostic Signal: Why Naive Aho–Corasick Matrix Power & Naive PIE Fail
Given an alphabet $\Sigma$ of size $\sigma = |\Sigma|$ and a set of forbidden patterns $\mathcal{P} = \{P_1, \dots, P_m\} \subset \Sigma^+$, we want to count the number $a_n$ of strings $W \in \Sigma^n$ containing **no** $P_i \in \mathcal{P}$ as a contiguous substring, or compute the ordinary generating function (OGF)
$$F(x) = \sum_{n \ge 0} a_n x^n \in R[[x]].$$
- **When AC Automaton DP / Matrix Power Fails**: The Aho–Corasick automaton on $\mathcal{P}$ has $V = O(\sum_{i=1}^m |P_i|)$ states. When $|P_i| \le 10^5$ (or $\sum |P_i| \approx 10^5$) and $n \le 10^5$ or $10^{18}$, $O(V^3 \log n)$ matrix exponentiation and $O(n V)$ DP both TLE.
- **When Naive Inclusion–Exclusion Fails**: Choosing $k$ occurrences of patterns from $\mathcal{P}$ in $W$ leaves $n - |\bigcup_{r=1}^k I_r|$ free characters, which depends on the **exact overlap lengths** of adjacent intervals $I_r$.
- **The Goulden–Jackson Breakthrough**: Group overlapping marked occurrences into maximal connected chains (**clusters**). Because two patterns in a reduced pattern set can overlap *only* when a suffix of $P_i$ matches a prefix of $P_j$, all $O(\sum |P_i|)$ internal prefix states vanish, collapsing the problem to an **$m \times m$ polynomial linear system**!

### 3.2 The Combinatorial Word Invariant: Antichain Precondition, Marked Words & Clusters

#### Step 1: The Antichain Precondition
Reduce $\mathcal{P} = \{P_1, \dots, P_m\}$ so that no pattern is a contiguous substring of another ($i \ne j \implies P_i \not\subseteq P_j$). For pure avoidance, if $P_i \subseteq P_j$, any word avoiding $P_i$ automatically avoids $P_j$, so $P_j$ is deleted before building the system.

#### Step 2: Marked-Word Double Counting
For $W \in \Sigma^*$, let $\text{Occ}(W)$ be the set of all occurrences of patterns from $\mathcal{P}$ in $W$. A **marked word** is a pair $(W, M)$ with $M \subseteq \text{Occ}(W)$ and weight $(-1)^{|M|} x^{|W|}$. Summing over all $W \in \Sigma^*$ and $M \subseteq \text{Occ}(W)$:
$$\sum_{W \in \Sigma^*} \sum_{M \subseteq \text{Occ}(W)} (-1)^{|M|} x^{|W|} = \sum_{W \in \Sigma^*} x^{|W|} (1 - 1)^{|\text{Occ}(W)|} = \sum_{\substack{W \in \Sigma^* \\ \text{Occ}(W) = \emptyset}} x^{|W|} = F(x).$$

#### Step 3: Unique Factorization into Free Letters and Clusters
Under the Antichain Precondition, ordering the intervals in $M$ by left endpoints $l_1 < l_2 < \dots < l_s$ is equivalent to ordering by right endpoints $r_1 < r_2 < \dots < r_s$. Two consecutive marked occurrences $e_q = [l_q, r_q]$ and $e_{q+1} = [l_{q+1}, r_{q+1}]$ **overlap** if and only if $l_{q+1} \le r_q$ (sharing $k = r_q - l_{q+1} + 1 \ge 1$ characters).
Taking connected components of $M$ decomposes every marked word $(W, M)$ uniquely as a sequence (`SEQ`) of:
1. **Free single characters** $c \in \Sigma$, with generating function $\sigma x$, and
2. **Clusters** (`簇`): maximal chains of overlapping marked occurrences $P_{i_1}, P_{i_2}, \dots, P_{i_s}$ ($s \ge 1$), with total generating function $C(x) = \sum_{j=1}^m C_j(x)$, where $C_j(x)$ sums over clusters whose **rightmost** marked pattern is $P_j$.

By the geometric series (`SEQ`) construction:
$$F(x) = \frac{1}{1 - \sigma x - \sum_{j=1}^m C_j(x)}. \tag{3.1}$$

### 3.3 The Reverse-Engineering Scratchpad: Two Dual Derivations of the $m \times m$ System

Define the **proper overlap set** and **full overlap set** between $P_i$ (on the left) and $P_j$ (on the right):
$$\text{Overlap}(P_i, P_j) = \Bigl\{ k \in \{1, \dots, \min(|P_i|, |P_j|)\} \setminus \{|P_i| \text{ if } i = j\} \;\Big|\; P_i\bigl[|P_i|-k+1 .. |P_i|\bigr] = P_j[1..k] \Bigr\},$$
$$\text{Overlap}^+(P_i, P_j) = \Bigl\{ k \in \{1, \dots, \min(|P_i|, |P_j|)\} \;\Big|\; P_i\bigl[|P_i|-k+1 .. |P_i|\bigr] = P_j[1..k] \Bigr\},$$
and the corresponding **Overlap (Cross-Correlation) Polynomials**:
$$\widetilde{C}_{i,j}(x) = \sum_{k \in \text{Overlap}(P_i, P_j)} x^{|P_j| - k}, \qquad C_{i,j}(x) = \delta_{i,j} + \widetilde{C}_{i,j}(x) = \sum_{k \in \text{Overlap}^+(P_i, P_j)} x^{|P_j| - k}. \tag{3.2}$$

#### View 1: Signed Cluster Extension (Goulden–Jackson, 1979)
A cluster ending with $P_j$ is either the single marked pattern $P_j$ alone (weight $-x^{|P_j|}$) or a cluster ending with some $P_i$ extended by $P_j$ at a proper overlap $k \in \text{Overlap}(P_i, P_j)$ (adding $|P_j| - k$ new characters and flipping sign by $-1$):
$$C_j(x) = -x^{|P_j|} - \sum_{i=1}^m C_i(x) \widetilde{C}_{i,j}(x) \iff \boxed{\sum_{i=1}^m C_i(x) C_{i,j}(x) = -x^{|P_j|} \quad \forall j \in \{1, \dots, m\}.} \tag{3.3}$$

#### View 2: Unsigned First-Hit End-Tagging (Guibas–Odlyzko, 1981)
Let $F_i(x)$ be the OGF of strings that avoid $\mathcal{P}$ until the very end, where they terminate with their **first** occurrence of a pattern from $\mathcal{P}$, namely $P_i$.
1. Extending any $\mathcal{P}$-avoiding word by $1$ character gives either a non-empty $\mathcal{P}$-avoiding word or a first hit $F_i(x)$:
   $$(1 - \sigma x) F(x) + \sum_{i=1}^m F_i(x) = 1. \tag{3.4}$$
2. Appending the full pattern $P_j$ to a $\mathcal{P}$-avoiding word $W$ (GF $F(x) x^{|P_j|}$) must trigger the **first** occurrence of some $P_i \in \mathcal{P}$ at some prefix $P_j[1..k]$ ($k \in \text{Overlap}^+(P_i, P_j)$), followed by the remaining $|P_j| - k$ characters of $P_j$:
   $$\boxed{\sum_{i=1}^m F_i(x) C_{i,j}(x) = F(x) x^{|P_j|} \quad \forall j \in \{1, \dots, m\}.} \tag{3.5}$$
   Dividing (3.5) by $F(x)$ proves $\dfrac{F_i(x)}{F(x)} = -C_i(x)$, showing that (3.3) and (3.5) are the exact same linear system!

#### Single-Pattern Closed Form ($m = 1$)
For a single pattern $P$ of length $L = |P|$ with autocorrelation polynomial $C_P(x) = \sum_{k \in \text{Borders}(P)} x^{L - k}$ (where $L \in \text{Borders}(P)$ contributes $x^0 = 1$):
$$\boxed{F(x) = \frac{C_P(x)}{(1 - \sigma x) C_P(x) + x^L}, \qquad F_1(x) = \frac{x^L}{(1 - \sigma x) C_P(x) + x^L}.} \tag{3.6}$$

> [!IMPORTANT]
> **Commutative Ring Invertibility & Gaussian Elimination Pivot Invariant**
> - Under the Antichain Precondition, for $i \ne j$, every $k \in \text{Overlap}^+(P_i, P_j)$ satisfies $k < |P_j|$, so $|P_j| - k \ge 1$ and $C_{i,j}(0) = 0$. Meanwhile, $C_{j,j}(0) = 1$ (from $k = |P_j|$).
> - Thus $\mathbf{C}(0) = I_m$, so $\det \mathbf{C}(x) \in 1 + x R[x]$ is **always a unit in $R[[x]]$** over any commutative ring $R$.
> - **Crucial Implementation Rule**: When solving $\sum_{i=1}^m C_i(x) C_{i,j}(x) = -x^{|P_j|}$ via Gaussian elimination over $\mathbb{F}_p[[x]] \bmod x^{N+1}$, **always pivot on the diagonal entry $C_{j,j}(x)$**, because off-diagonal entries have zero constant term and are not invertible in $\mathbb{F}_p[[x]]$.

---

## 4. Master Reconciled Treatise — Module B: Bivariate $(t-1)$ Weighted Cluster GFs, Exact $k$-Occurrence Formula & The $t = 1 + u$ Moment Shift

### 4.1 The Combinatorial Word Invariant: The $t_i = 1 + (t_i - 1)$ Sieve
Suppose we want the multivariate generating function weighting each occurrence of $P_i$ by a formal variable $t_i$:
$$F(x; t_1, \dots, t_m) = \sum_{W \in \Sigma^*} x^{|W|} \prod_{i=1}^m t_i^{\text{occ}_i(W)}.$$
Writing $\prod_{e \in \text{Occ}(W)} t_{\text{pat}(e)} = \prod_{e \in \text{Occ}(W)} \bigl(1 + (t_{\text{pat}(e)} - 1)\bigr) = \sum_{M \subseteq \text{Occ}(W)} \prod_{e \in M} (t_{\text{pat}(e)} - 1)$, we sum over the exact same marked words $(W, M)$ as in Module A, except each marked pattern $P_j \in M$ carries weight **$(t_j - 1)$** instead of $-1$!

When $\mathcal{P}$ is an antichain, replacing $-1$ by $(t_j - 1)$ in (3.3) yields the **Weighted Goulden–Jackson Linear System**:
$$\boxed{\sum_{i=1}^m C_i(x; \mathbf{t}) \Bigl(\delta_{i,j} - (t_j - 1) \widetilde{C}_{i,j}(x)\Bigr) = (t_j - 1) x^{|P_j|} \quad \forall j \in \{1, \dots, m\},} \tag{4.1}$$
with $F(x; \mathbf{t}) = \Bigl(1 - \sigma x - \sum_{i=1}^m C_i(x; \mathbf{t})\Bigr)^{-1}$.

### 4.2 Single-Pattern Bivariate GF, Exact $k$-Occurrence OGF & The $t = 1 + u$ Binomial Shift

For a single pattern $P$ ($L = |P|$) with autocorrelation polynomial $C_P(x) = 1 + \widetilde{C}_P(x)$, solving (4.1) gives $C_1(x, t) = \frac{(t - 1) x^L}{1 - (t - 1)(C_P(x) - 1)}$, and hence:
$$\boxed{F(x, t) = \frac{1 - (t - 1)\bigl(C_P(x) - 1\bigr)}{(1 - \sigma x)\Bigl(1 - (t - 1)\bigl(C_P(x) - 1\bigr)\Bigr) - (t - 1) x^L} = \frac{C_P(x) - t\bigl(C_P(x) - 1\bigr)}{D_0(x) - t D_1(x)},} \tag{4.2}$$
where $D_0(x) = (1 - \sigma x) C_P(x) + x^L$ and $D_1(x) = (1 - \sigma x)\bigl(C_P(x) - 1\bigr) + x^L$.

1. **Expansion Around $t = 0$ (Strings with *Exactly* $k$ Occurrences of $P$)**:
   Using the identity $C_P(x) D_1(x) - (C_P(x) - 1) D_0(x) = x^L$, for every $k \ge 1$:
   $$\boxed{F_k(x) = [t^k] F(x, t) = \frac{x^L \, D_1(x)^{k-1}}{D_0(x)^{k+1}} = \frac{x^L \Bigl((1 - \sigma x)\bigl(C_P(x) - 1\bigr) + x^L\Bigr)^{k-1}}{\Bigl((1 - \sigma x) C_P(x) + x^L\Bigr)^{k+1}}.} \tag{4.3}$$
   *Combinatorial meaning*: $\frac{x^L}{D_0(x)}$ is the first occurrence of $P$; each of the $k-1$ factors $\frac{D_1(x)}{D_0(x)} = 1 - \frac{1 - \sigma x}{D_0(x)}$ advances from the $r$-th occurrence of $P$ to the $(r+1)$-th occurrence; and $\frac{1}{D_0(x)}$ is the $P$-avoiding suffix after the $k$-th occurrence.
2. **Expansion Around $t = 1$ via $u = t - 1$ (The Binomial Moment Shift for Huge $n \le 10^{18}$)**:
   Substituting $t = 1 + u$ directly into the first form of (4.2) gives:
   $$\boxed{F(x, 1 + u) = \frac{1}{1 - \sigma x} + \sum_{j \ge 1} u^j \, \frac{x^L \, D_1(x)^{j-1}}{(1 - \sigma x)^{j+1}}, \quad \text{so} \quad \sum_{W \in \Sigma^n} \binom{\text{occ}_P(W)}{j} = [x^n] \frac{x^L \, D_1(x)^{j-1}}{(1 - \sigma x)^{j+1}}!} \tag{4.4}$$
   Because the denominator is simply $(1 - \sigma x)^{j+1}$ instead of $D_0(x)^{j+1}$, the $K$-th moment $\sum_{W \in \Sigma^n} \text{occ}_P(W)^K = \sum_{j=0}^K \left\{\begin{matrix} K \\ j \end{matrix}\right\} j! \sum_{W \in \Sigma^n} \binom{\text{occ}_P(W)}{j}$ can be computed for $n \le 10^{18}, L \le 10^5, K \le 20$ in **$O(K L \log(KL))$** time!

### 4.3 Non-Antichain Embedded Substring Adjustment (When $P_i \subsetneq P_j$ and $t_i \ne 0$)
If $P_i$ is a contiguous substring of $P_j$ and $t_i \ne 0$, we cannot delete $P_j$. Instead, we restrict cluster chains to patterns that are not proper substrings of another marked pattern in the chain, and **absorb** all occurrences of shorter patterns $P_i$ that lie strictly inside a marked $P_j$ into the effective weight of $P_j$:
- Replace the single-pattern weight $(t_j - 1)$ of $P_j$ by:
  $$\widetilde{W}_j = (t_j - 1) \prod_{P_i \subsetneq P_j} t_i^{\text{occ}(P_i, P_j)}.$$
- When $P_a$ and $P_b$ overlap by $k$ characters ($P_a[|P_a|-k+1..|P_a|] = P_b[1..k]$), any pattern $P_i$ completely contained inside the overlap $P_b[1..k]$ was counted in both $\widetilde{W}_a$ and $\widetilde{W}_b$, while any new pattern $P_i$ straddling the junction inside $P_a P_b[k+1..|P_b|]$ must be multiplied in. Thus the overlap transition multiplies $x^{|P_b|-k}$ by $\dfrac{\prod_{P_i \text{ straddling}} t_i}{\prod_{P_i \subseteq P_b[1..k]} t_i}$.

---

## 5. Master Reconciled Treatise — Module C: String PGFs, Conway's Casino Martingale (`康威赌博`) & Multi-Player Pattern Races

### 5.1 Unified Duality: PGFs vs. Conway's Casino Martingale
Let character $c \in \Sigma$ be drawn independently at each step with probability $p_c > 0$ ($\sum_{c \in \Sigma} p_c = 1$), and write $\mathbb{P}(u) = \prod_{r=1}^{|u|} p_{u_r}$ ($\mathbb{P}(u) = \sigma^{-|u|}$ in the uniform case).
Given an antichain of competing patterns $\mathcal{P} = \{P_1, \dots, P_m\}$, let $T = \min_i T_{P_i}$ be the first step when any $P_i \in \mathcal{P}$ appears, $F_i(z) = \sum_{n \ge 0} \mathbb{P}(T = n \text{ on } P_i) z^n$, and $G(z) = \sum_{n \ge 0} \mathbb{P}(T > n) z^n$.

#### The Fundamental PGF System
Replacing $x^L$ by $\mathbb{P}(P_j) z^{|P_j|}$ in the Guibas–Odlyzko system (3.4)–(3.5) and dividing the $j$-th overlap equation by $\mathbb{P}(P_j)$ yields:
$$(1 - z) G(z) + \sum_{i=1}^m F_i(z) = 1, \qquad G(z) z^{|P_j|} = \sum_{i=1}^m F_i(z) \sum_{k \in \text{Overlap}^+(P_i, P_j)} \frac{z^{|P_j| - k}}{\mathbb{P}(P_j[1..k])} \quad (1 \le j \le m). \tag{5.1}$$

#### 1. Single-Pattern Expected Stopping Time $\mathbb{E}[T_S]$ & Variance $\text{Var}(T_S)$
Setting $m = 1$ ($P_1 = S$, $L = |S|$) and differentiating (5.1) once and twice at $z = 1$ (where $F_1(1) = 1$, $F_1'(1) = G(1) = \mathbb{E}[T_S]$, and $F_1''(1) = 2 G'(1)$):
$$\boxed{\mathbb{E}[T_S] = \sum_{k \in \text{Borders}(S)} \frac{1}{\mathbb{P}(S[1..k])} \quad \left(= \sum_{k \in \text{Borders}(S)} \sigma^k \text{ for uniform } \Sigma\right),} \tag{5.2}$$
$$\boxed{\text{Var}(T_S) = \bigl(\mathbb{E}[T_S]\bigr)^2 + \mathbb{E}[T_S] - 2 \sum_{k \in \text{Borders}(S)} \frac{k}{\mathbb{P}(S[1..k])}.} \tag{5.3}$$

#### 2. Multi-Player Pattern Race Linear System (`[SDOI2017] 硬币游戏`, `[JSOI2009] 有趣的游戏`)
Evaluating (5.1) at $z = 1$ (or applying Doob's Optional Stopping Theorem to Conway's $P_j$-betting casino syndicate where a gambler entering at step $t$ stakes $\$1$ and multiplies their wealth by $p_{P_j[r]}^{-1}$ on each matched character $P_j[r]$) gives an **$(m+1) \times (m+1)$ linear system** for the winning probabilities $\pi_i = F_i(1)$ and expected game length $\mathbb{E}[T] = G(1)$:
$$\boxed{\sum_{i=1}^m \pi_i \, \Omega_{i,j} - \mathbb{E}[T] = 0 \quad (1 \le j \le m), \qquad \sum_{i=1}^m \pi_i = 1, \qquad \Omega_{i,j} = \sum_{k \in \text{Overlap}^+(P_i, P_j)} \frac{1}{\mathbb{P}(P_j[1..k])}.} \tag{5.4}$$
- **Un-Divided Form for Zero-Probability Letters ($p_c = 0$) & Floating-Point Stability**:
  Multiplying the $j$-th equation of (5.4) by $\mathbb{P}(P_j)$ gives the **division-free system**:
  $$\sum_{i=1}^m \pi_i \left(\sum_{k \in \text{Overlap}^+(P_i, P_j)} \mathbb{P}\bigl(P_j[k+1..|P_j|]\bigr)\right) - \mathbb{P}(P_j) \mathbb{E}[T] = 0, \tag{5.5}$$
  which never divides by zero when $p_c = 0$ and keeps all matrix entries bounded in $[0, 2]$ even when $|P_j| = 10^5$!

---

## 6. Master Reconciled Treatise — Module D: Automaton DP (`自動機上のDP`), `DP套DP` & DFA Minimization

### 6.1 The 4-Stage `DP套DP` Compiler Pipeline
Whenever an outer problem asks to **count** strings $T \in \Sigma^N$ for which an **inner dynamic programming algorithm** $\mathcal{A}(T)$ outputs a target value $c$:
1. **Stage 1 — Inner State Relative/Capped Compression**:
   Eliminate unbounded prefix coordinates from the inner DP state tuple by encoding **monotonic differences** (e.g., $\Delta f[j] = f[j] - f[j-1] \in \{0, 1\}$ for LCS, compressing $(K+1)^K$ tuples to $2^K$ bitmasks; or patience-sorting subset masks $\in [0, 2^{|\Sigma|})$ for LIS) or **clamping** values at the acceptance cap ($\min(\text{melds}, 4)$ in `[ZJOI2019] 麻将`).
2. **Stage 2 — Automated BFS Reachability Discovery**:
   Starting from the initial inner state $q_0$, run a BFS over transitions $c \in \Sigma$ using a hash/tree map `id[State]` to discover only the **reachable** inner states $Q_{\text{reach}}$ and build the transition table `trans[u][c]`.
3. **Stage 3 — Myhill–Nerode / Hopcroft Partition Refinement (or Brzozowski Double Reversal)**:
   Quotient $Q_{\text{reach}}$ by suffix indistinguishability: initialize $\Pi_0$ by grouping states with identical final output $\text{out}(u)$, and repeatedly split any block $B \in \Pi_t$ whenever two states $u, v \in B$ have $\bigl(\text{block}(\text{trans}[u][c])\bigr)_{c \in \Sigma}$ distinct.
4. **Stage 4 — Outer DP / Matrix Exponentiation**:
   Run the outer counting DP $dp[i][q]$ (or product-automaton DP $dp[i][q_{\text{inner}}][q_{\text{KMP/AC}}]$, or matrix power $M^N$) over the minimized DFA $\mathcal{M}_{\min}$!

---

## 7. Deduplicated Master Problem Archive (`W4A-01` to `W4A-42`) & Quarantine Ledger (`R-4A-01` to `R-4A-12`)

### 7.1 Master Index of Reconciled Wave 4A Non-Template Problems (42 Problems)

Combining and deduplicating Cohort 1 (`P-4A-01..P-4A-32`) and Cohort 2 (`#1..#32`) yields **42 unique accepted non-template problems** ordered across our 4-Tier Difficulty Ladder:

| ID | Problem Title & Judge / Source | Lang | Tier | Cohort Origin | Core Technique & Structural Invariant |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`W4A-01`** | `[JSOI2007] 文本生成器` (Luogu P4052) | `[ZH]` | Stepping Stone | C1 (`P-4A-01`) + C2 (`#2`) | Complement counting $\sigma^N - (\text{avoiding all } P_i)$ via `fail`-propagated `bad[u]` |
| **`W4A-02`** | `[POI 2000] 病毒 Viruses` (Luogu P2444) | `[EN]`/`[ZH]` | Stepping Stone | C1 (`P-4A-03`) + C2 (`#6`) | Infinite avoiding binary string $\iff$ directed cycle in safe AC DFA subgraph |
| **`W4A-03`** | `POJ 2778 — DNA Sequence` | `[EN]` | Stepping Stone | C2 (`#3`) | Safe AC transition matrix power $M^n$ ($n \le 2 \times 10^9, V \le 101$) |
| **`W4A-04`** | `CSES 1112 — Required Substring` | `[EN]` | Stepping Stone | C2 (`#5`) | Equivalence of absorbing KMP DP and single-pattern Guibas–Odlyzko OGF |
| **`W4A-05`** | `[HNOI2004] L语言` (Luogu P2292) | `[ZH]` | Stepping Stone | C1 (`P-4A-02`) + C2 (`#6`) | 20-bit machine word `reach_mask` $\times$ AC `fail`-chain dictionary length mask |
| **`W4A-06`** | `[TJOI2015] 弦论` (Luogu P3975) | `[ZH]` | Stepping Stone | C1 (`P-4A-07`) | $k$-th substring on SAM DAG with $w(u) = 1$ (distinct) vs. $w(u) = |\text{endpos}(u)|$ |
| **`W4A-07`** | `CF 494B — Obsessive String` | `[EN]` | Stepping Stone | C1 (`P-4A-12`) + C2 (`#7`) | Disjoint substring picks containing $T$ via KMP `last_start[r]` + double prefix sum |
| **`W4A-08`** | `[AHOI2005] 病毒检测` (Luogu P2536) | `[ZH]` | Stepping Stone | C1 (`P-4A-06`) | Wildcard `?`/`*` NFA-over-Trie bitset reachability |
| **`W4A-09`** | `AtCoder ARC 081 E (081 C) — Don't Be a Subsequence` | `[JA]` | Stepping Stone | C1 (`P-4A-16`) + C2 (`#15`) | Shortest absent string via DAG shortest path to dead sink $\perp$ on DASG |
| **`W4A-10`** | `AtCoder ARC 058 E — Iroha and Haiku` | `[JA]` | Stepping Stone | C2 (`#8`) | Unary-encoded suffix-sum bitmask DFA ($2^{X+Y+Z}$ states) for subsegment sum avoidance |
| **`W4A-11`** | `[CTSC2006] 歌唱王国` (Luogu P4548) | `[ZH]` | Intermediate | C1 (`P-4A-09`) + C2 (`#1`) | $\mathbb{E}[T_S] = \sum_{k \in \text{Borders}(S)} \sigma^k$ via PGF $F'(1) = G(1)$ and Conway Martingale |
| **`W4A-12`** | `[SDOI2017] 硬币游戏` (Luogu P3706) | `[ZH]` | Intermediate | C1 (`P-4A-10`) + C2 (`#9`) | Multi-player coin race $(m+1) \times (m+1)$ Conway / Guibas–Odlyzko overlap system |
| **`W4A-13`** | `[JSOI2009] 有趣的游戏` (Luogu P2467 / BZOJ 1444) | `[ZH]` | Intermediate | C1 (`P-4A-11`) + C2 (`#10`) | Biased letter probabilities $p_c \ge 0$ and division-free overlap linear system |
| **`W4A-14`** | `CF 86C — Genetic Engineering` | `[EN]` | Intermediate | C1 (`P-4A-04`) + C2 (`#14`) | Full tile coverage by $\mathcal{P}$ via AC state + uncovered tail depth $d \le \max |P_i|$ |
| **`W4A-15`** | `[SDOI2014] 数数` (Luogu P3311) | `[ZH]` | Intermediate | C1 (`P-4A-05`) + C2 (`#11`) | Digit DP $\times$ AC Automaton with leading-zero root-stay invariant |
| **`W4A-16`** | `[HNOI2008] GT考试` (Luogu P3193) | `[ZH]` | Intermediate | C1 (`P-4A-14`) | Single-pattern avoidance for huge $N$ via KMP matrix or Goulden–Jackson + Bostan–Mori |
| **`W4A-17`** | `[BJWC2011] 禁忌` (Luogu P3735) | `[ZH]` | Intermediate | C1 (`P-4A-13`) | Greedy non-overlapping AC partition with root-reset transition matrix |
| **`W4A-18`** | `AtCoder ABC 305 G — Banned Substrings` | `[JA]` | Intermediate | C1 (`P-4A-15`) + C2 (`#4`) | Length-5 De Bruijn suffix mask DFA + matrix exponentiation for $N \le 10^{18}$ |
| **`W4A-19`** | `[BZOJ 3864] Hero meet devil` | `[ZH]` | Intermediate | C2 (`#12`) | Canonical LCS `DP套DP` via monotonic row-difference bitmask $\Delta f \in \{0,1\}^K$ |
| **`W4A-20`** | `UVa 11468 — Substring` | `[EN]` | Intermediate | C2 (`#16`) | Biased survival probability $[z^n]G(z)$ on AC automaton |
| **`W4A-21`** | `[TJOI2018] 游园会` (Luogu P4590) | `[ZH]` | Advanced | C1 (`P-4A-17`) + C2 (`#13`) | Product automaton `DP套DP`: $2^K$ LCS difference mask $\times$ 3-state $\texttt{NOI}$ KMP |
| **`W4A-22`** | `HDU 4352 — XHXJ's List` | `[ZH]`/`[EN]` | Advanced | C1 (`P-4A-18`) | Digit DP $\times$ 10-bit patience-sorting LIS tail-subset DFA |
| **`W4A-23`** | `AtCoder AGC 022 E — Median Replace` | `[JA]` | Advanced | C1 (`P-4A-19`) + C2 (`#21`) | Greedy ternary median-reduction stack compressed to 7-state / 5-class minimal DFA |
| **`W4A-24`** | `[ZJOI2019] 麻将` (Luogu P5279) | `[ZH]` | Advanced | C1 (`P-4A-23`) + C2 (`#19`) | Capped Mahjong Hu-checker inner DP $\to$ 2092-state DFA via BFS + EGF stopping time |
| **`W4A-25`** | `CF 1207G — Indie Album` | `[EN]` | Advanced | C1 (`P-4A-20`) | Offline Trie DFS $\times$ AC `fail`-tree Euler tour Fenwick subtree queries |
| **`W4A-26`** | `[SDOI2017] 天才黑客` (Luogu P3703) | `[ZH]` | Advanced | C1 (`P-4A-21`) | Trie Virtual Tree + DFS-order prefix/suffix range optimization for LCP edge costs |
| **`W4A-27`** | `AtCoder ABC 249 G / ARC 141 D — Palindromic Concatenation` | `[JA]` | Advanced | C1 (`P-4A-22`) | Two-sided outside-in palindrome construction tracking overhang suffix/prefix states |
| **`W4A-28`** | `QOJ / UCup — Long Pattern Avoidance ($|P_i|, N \le 10^5$)` | `[EN]`/`[ZH]` | Advanced | C1 (`P-4A-24`) + C2 (`#17`) | Goulden–Jackson $m \times m$ polynomial system + NTT inversion / Bostan–Mori |
| **`W4A-29`** | `CF Gym 102538 / Extended [CTSC2006] — Stopping Variance` | `[EN]`/`[ZH]` | Advanced | C1 (`P-4A-27`) + C2 (`#18`) | Single-pattern hitting variance $\text{Var}(T_S)$ via PGF second derivative $F''(1) = 2G'(1)$ |
| **`W4A-30`** | `AtCoder AGC 020 E — Encoding Subsets` | `[JA]` | Advanced | C1 (`P-4A-26`) + C2 (`#22`) | Recursive interval/automaton DP over bitwise-AND slices of repeating blocks |
| **`W4A-31`** | `CF 1349D / Seed-Prefix Conditional Pattern Race` | `[EN]` | Advanced | C2 (`#24`) | Non-empty initial seed prefix $S_0$ subtracting initial martingale potential $\Omega_{S_0, P_j}$ |
| **`W4A-32`** | `CF 710F — String Set Queries` | `[EN]` | Mastery | C1 (`P-4A-25`) | Online dynamic AC dictionary via Binary Grouping (`二进制分组`) of $O(\log M)$ automata |
| **`W4A-33`** | `UOJ / QOJ — Exact $k$ Occurrences of Long Pattern` | `[ZH]`/`[EN]` | Mastery | C1 (`P-4A-29`) + C2 (`#20`) | Bivariate Guibas–Odlyzko $[t^k]F(x, t) = \frac{x^L D_1(x)^{k-1}}{D_0(x)^{k+1}}$ via FPS $\ln/\exp$ with shift $d = \min\text{Per}(P)$ |
| **`W4A-34`** | `UCup / QOJ — Expected $K$-th Power $\mathbb{E}[\text{occ}_P(W)^K]$ ($n \le 10^{18}$)` | `[EN]`/`[ZH]` | Mastery | C2 (`#27`) | The $t = 1 + u$ binomial moment shift collapsing denominator to $(1 - \sigma x)^{j+1}$ + Stirling numbers |
| **`W4A-35`** | `AtCoder AGC 058 D — Yet Another ABC String` | `[JA]` | Mastery | C2 (`#31`) | 3-variable Goulden–Jackson cluster GF $\frac{-3x^3}{1+x+x^2}$ canceling $3k+2$ clusters to zero |
| **`W4A-36`** | `THUPC / QOJ — Non-Antichain Weighted Pattern Product` | `[ZH]` | Mastery | C2 (`#28`) | Embedded substring weight absorption $\widetilde{W}_j$ and overlap double-count correction |
| **`W4A-37`** | `CF 1608F / AGC 039 F / Duval Lyndon Automaton Counting` | `[EN]`/`[JA]` | Mastery | C1 (`P-4A-28`) + C2 (`#23`, `#29`) | Duval pre-Lyndon pointer state $(L, p)$ & deferred open-class alphabet DP |
| **`W4A-38`** | `AtCoder AGC 064 C / Palindrome-Avoiding Restricted-Growth DFA` | `[JA]` | Mastery | C2 (`#25`) | Avoiding palindromes of length $\ge K$ via length $K, K+1$ restricted-growth partition DFA + Hopcroft |
| **`W4A-39`** | `Project Euler 597 / Penney's Game Optimal Counter-Pattern` | `[EN]` | Mastery | C1 (`P-4A-30`) | Maximizing $\pi_2$ against $P_1$ via prepended bit $b \cdot P_1[1..L-1]$ on the border payoff matrix |
| **`W4A-40`** | `[国家集训队论文] Regex & Game Counting via Hopcroft / Brzozowski Minimization` | `[ZH]` | Mastery | C1 (`P-4A-31`) + C2 (`#26`, `#32`) | Thompson $\epsilon$-NFA / Sprague–Grundy inner DP $\to$ Subset DFA $\to$ Hopcroft / Brzozowski minimal DFA |
| **`W4A-41`** | `LOJ 3042 / Random Walk to String Target with Backspace/Reset` | `[ZH]` | Mastery | C2 (`#30`) | KMP fail-tree tridiagonal potential elimination $dp[u] = E[u] - E[u+1]$ under non-uniform resets |
| **`W4A-42`** | `UCup / QOJ — Palindromic & Cyclic Goulden–Jackson` | `[EN]`/`[ZH]` | Mastery | C1 (`P-4A-32`) + C3 Frontier | Counting palindromes (center-straddling symmetric clusters) and circular words avoiding $\mathcal{P}$ |

---

### 7.2 Tier 1 (`Stepping Stone`): Foundational Automaton DP & Complement Invariants (`W4A-01` to `W4A-10`)

#### **`W4A-01` — `[JSOI2007] 文本生成器` (Luogu P4052 — Text Generator)**
- **Statement & Constraints**: Given $m \le 60$ uppercase words of length $\le 100$, count strings $W \in \{\texttt{A}..\texttt{Z}\}^N$ ($N \le 100$) containing **at least one** of the $m$ words as a contiguous substring, modulo $10^4 + 7$.
- **1. The Diagnostic Signal**: Tracking *which* non-empty subset of the $60$ patterns has appeared would require $2^{60}$ states. However, "at least one $P_i$ appears" is the complement of "zero $P_i$ appear".
- **2. The Combinatorial Word Invariant**: By complementation, $\#\{\text{valid}\} = 26^N - \#\{\mathcal{P}\text{-avoiding}\}$. A prefix avoids $\mathcal{P}$ iff at every step the reached AC node $u$ has no pattern ending on its `fail`-tree path to the root (`bad[u] = own_bad[u] | bad[fail[u]] == false`).
- **3. The Reverse-Engineering Scratchpad**: Build AC automaton ($\le 6001$ states), propagate `bad[u] |= bad[fail[u]]` in BFS order, run $O(N \cdot |Q| \cdot 26)$ DP over non-`bad` nodes, and return $(26^N - \sum_u dp[N][u]) \bmod 10007$.
- **4. Boundary Pitfalls**: Failing to propagate `bad[u] |= bad[fail[u]]` during BFS allows a longer pattern prefix `u` to hide a shorter forbidden pattern `P_i` that is a suffix of `u`.

#### **`W4A-02` — `[POI 2000] 病毒 Viruses` (Luogu P2444)**
- **Statement & Constraints**: Given binary virus patterns $\mathcal{P}$ of total length $\sum |P_i| \le 3 \times 10^4$, decide whether an **infinite** binary string avoiding $\mathcal{P}$ exists.
- **1. The Diagnostic Signal**: Instead of finite length $N$, we must decide if $a_N > 0$ for all $N \to \infty$.
- **2. The Combinatorial Word Invariant (König's Lemma on Finite DFAs)**: On the finite deterministic AC automaton, an infinite safe path from the root $q_0$ exists **if and only if** the subgraph of reachable non-`bad` states contains a **directed cycle**.
- **3. The Reverse-Engineering Scratchpad**: Build AC automaton over $\{\texttt{0}, \texttt{1}\}$ with explicit trie-graph transitions `tr[u][c] = tr[fail[u]][c]`, propagate `bad[u] |= bad[fail[u]]`, and run 3-color DFS (`vis[u]` $\in \{0, \text{in\_stack}, \text{done}\}$) from $q_0$ avoiding `bad` states.
- **4. Boundary Pitfalls**: Treating `vis[v] == done` (cross-edge in a DAG) as a cycle, or forgetting to wire `tr[u][c] = tr[fail[u]][c]` before cycle detection.

#### **`W4A-03` — `POJ 2778 — DNA Sequence`**
- **Statement & Constraints**: Given $m \le 10$ forbidden DNA strings of length $\le 10$ over $\{\texttt{A}, \texttt{C}, \texttt{G}, \texttt{T}\}$ and $N \le 2 \times 10^9$, count avoiding strings of length $N$ modulo $10^5$.
- **1. The Diagnostic Signal**: $N \le 2 \times 10^9$ rules out $O(N V)$ DP, while total AC states $V \le 101$ is small.
- **2. The Combinatorial Word Invariant**: Safe transitions between non-`bad` AC states form a directed graph whose adjacency matrix $M$ satisfies $\sum_u (M^N)_{0, u} = a_N$.
- **3. The Reverse-Engineering Scratchpad**: Build AC automaton, propagate `bad[u]`, delete `bad` rows/columns to form $M$ of size $V_{\text{safe}} \le 101$, and compute $M^N$ in $O(V_{\text{safe}}^3 \log N)$.
- **4. Boundary Pitfalls**: Multiple transitions between the same pair of states $(u, v)$ via different characters $c \in \{\texttt{A}, \texttt{C}, \texttt{G}, \texttt{T}\}$ must be **incremented** (`M[u][v] += 1`), not overwritten (`M[u][v] = 1`)!

#### **`W4A-04` — `CSES 1112 — Required Substring`**
- **Statement & Constraints**: Given $N \le 1000$ and a pattern $P$ of length $M \le 100$ over $\{\texttt{A}..\texttt{Z}\}$, count strings of length $N$ containing $P$ at least once modulo $10^9 + 7$.
- **1. The Diagnostic Signal**: Single-pattern avoidance complement bridging KMP automaton DP and the Guibas–Odlyzko autocorrelation rational GF.
- **2. The Combinatorial Word Invariant**: Answer is $26^N - [x^N] \frac{C_P(x)}{(1 - 26x)C_P(x) + x^M}$.
- **3. The Reverse-Engineering Scratchpad**: Run KMP DP in $O(N M \sigma)$ (making state $M$ an absorbing sink) or extract $[x^N] \frac{C_P(x)}{(1 - 26x)C_P(x) + x^M}$ in $O(N M)$ time.
- **4. Boundary Pitfalls**: In KMP DP without complementation, once state $M$ is reached, `tr[M][c]` must stay at $M$ rather than falling back to `pi[M]`.

#### **`W4A-05` — `[HNOI2004] L语言` (Luogu P2292)**
- **Statement & Constraints**: Given a dictionary $D$ of $|D| \le 20$ words with $|w_i| \le 20$ and query strings $T$ with $|T| \le 2 \times 10^6$, find the longest prefix of $T$ that is a concatenation of words from $D$.
- **1. The Diagnostic Signal**: Checking all dictionary suffixes at each index $i \le 2 \times 10^6$ naively takes $O(|T| \cdot \max |w_i|)$, which TLEs.
- **2. The Combinatorial Word Invariant**: Since $\max |w_i| \le 20$, at index $i$ we only need a 20-bit machine word `reach_mask` where bit $d-1$ is $1$ iff $T[1..i-d]$ is a valid concatenation. Precomputing `len_mask[u]` (the bitmask of lengths of all dictionary words on AC node $u$'s `fail` chain) lets us test $T[1..i]$ in $O(1)$ bitwise AND: `(reach_mask & len_mask[u]) != 0`!
- **3. The Reverse-Engineering Scratchpad**: Precompute `len_mask[u] |= len_mask[fail[u]]` on AC automaton; scan $T$ updating `reach_mask = (reach_mask << 1) | valid[i-1]` in $O(|T|)$ time.
- **4. Boundary Pitfalls**: Forgetting to initialize bit $0$ of `reach_mask` for the empty prefix $T[1..0]$.

#### **`W4A-06` — `[TJOI2015] 弦论` (Luogu P3975)**
- **Statement & Constraints**: Given string $S$ ($|S| \le 5 \times 10^5$) and $k \le 10^9$, output the $k$-th lexicographically smallest substring of $S$, either counting distinct substrings ($T=0$) or counting multiplicity ($T=1$).
- **1. The Diagnostic Signal**: Enumerating substrings is $O(|S|^2)$; we need a DAG where paths from the root biject with distinct substrings in lexicographical order.
- **2. The Combinatorial Word Invariant**: Every directed path from the root $t_0$ in the DAWG of $\text{SAM}(S)$ spells a unique distinct substring of $S$! Stopping at node $u$ contributes weight $w(u) = 1$ (if $T = 0$) or $w(u) = |\text{endpos}(u)|$ (if $T = 1$, accumulated bottom-up on the Link Tree).
- **3. The Reverse-Engineering Scratchpad**: Build $\text{SAM}(S)$, compute $w(u)$ via Link-Tree sum, compute $dp[u] = w(u) + \sum_{c} dp[\text{tr}[u][c]]$ in reverse topological (`len`) order, and walk greedily from $t_0$.
- **4. Boundary Pitfalls**: Multiplying $w(u)$ by $\text{len}(u) - \text{len}(\text{link}(u))$ in the DAG DP—that conflates Link-Tree equivalence classes with DAWG paths (where each path length already isolates a single substring!).

#### **`W4A-07` — `CF 494B — Obsessive String`**
- **Statement & Constraints**: Given $S, T$ ($|S|, |T| \le 10^5$), count ways to choose $k \ge 1$ disjoint substrings $S[l_1..r_1], \dots, S[l_k..r_k]$ such that every chosen substring contains $T$ at least once, modulo $10^9 + 7$.
- **1. The Diagnostic Signal**: A chosen segment $S[l..r]$ can contain multiple overlapping copies of $T$, so we must characterize valid $(l, r)$ pairs without double counting.
- **2. The Combinatorial Word Invariant**: $S[l..r]$ contains $T$ iff $l \le \text{last\_start}(r)$, where $\text{last\_start}(r)$ is the maximum starting position of an occurrence of $T$ ending at or before $r$.
- **3. The Reverse-Engineering Scratchpad**: Find all occurrences of $T$ in $S$ via KMP to populate $\text{last\_start}(r)$, and maintain $dp[r] = dp[r-1] + \sum_{l=1}^{\text{last\_start}(r)} (dp[l-1] + 1)$ via double prefix sums in $O(|S|)$.
- **4. Boundary Pitfalls**: Off-by-one between the 1-based end index $r$ of a match and its start index $r - |T| + 1$.

#### **`W4A-08` — `[AHOI2005] 病毒检测` (Luogu P2536)**
- **Statement & Constraints**: Given a wildcard pattern $P$ ($|P| \le 1000$ with `?` and `*`) and $n \le 500$ DNA strings of length $\le 500$, count how many strings do *not* match $P$.
- **1. The Diagnostic Signal**: Running $O(|P| \cdot |S_i|)$ wildcard DP independently on $500$ strings with shared prefixes wastes work.
- **2. The Combinatorial Word Invariant**: Insert all $n$ strings into a Trie; each Trie node $u$ maintains a `std::bitset<1005>` of reachable pattern prefix lengths in $P$.
- **3. The Reverse-Engineering Scratchpad**: DFS the Trie; at node $u$, propagate `*` transitions (`b |= b << 1` closure) and step to child `v` on character `c` via `(b & match_mask[c]) << 1`.
- **4. Boundary Pitfalls**: Failing to close `*` epsilon-transitions both before and after reading a character.

#### **`W4A-09` — `AtCoder ARC 081 E (081 C) — Don't Be a Subsequence`**
- **Statement & Constraints**: Given $S$ ($|S| \le 2 \times 10^5$), find the shortest (and lexicographically smallest) string over `'a'..'z'` that is **not** a subsequence of $S$.
- **1. The Diagnostic Signal**: Connects substring avoidance with subsequence automaton (DASG) shortest paths.
- **2. The Combinatorial Word Invariant**: In the DASG where $\delta(i, c)$ is the first occurrence of $c$ at or after $i+1$ (or $\perp = |S|+1$ if none), absent subsequences are paths from $0$ to $\perp$.
- **3. The Reverse-Engineering Scratchpad**: Compute $dp[i] = 1 + \min_{c} dp[\delta(i, c)]$ backward from $i = |S|$ to $0$ in $O(26 |S|)$ and reconstruct the lexicographically smallest optimal character at each step.
- **4. Boundary Pitfalls**: Starting at index $1$ instead of a virtual root $0$ before $S[1]$, which misses the first character $S[1]$.

#### **`W4A-10` — `AtCoder ARC 058 E — Iroha and Haiku`**
- **Statement & Constraints**: Given $N \le 40$ and $X \le 5, Y \le 7, Z \le 5$, count sequences $A \in \{1..10\}^N$ containing a contiguous subsegment whose prefix sums hit $X, X+Y, X+Y+Z$ modulo $10^9 + 7$.
- **1. The Diagnostic Signal**: A haiku $(X, Y, Z)$ is not a single string, but any sequence of digits summing to $X$, then $Y$, then $Z$.
- **2. The Combinatorial Word Invariant (Unary Prefix-Sum Bitmask DFA)**: Since $S = X + Y + Z \le 17$, encode each integer $a \in \{1..10\}$ in unary as $10^{a-1}$. Maintaining the last $S$ bits of this unary stream as a bitmask $M \in [0, 2^S)$ tracks all suffix sums $\le S$ simultaneously! A haiku ends at the current step iff bits $Z-1$, $Y+Z-1$, and $X+Y+Z-1$ are all $1$ in $M$.
- **3. The Reverse-Engineering Scratchpad**: Run complement DP over $N$ steps and $2^{17}$ safe masks in $O(N \cdot 10 \cdot 2^{X+Y+Z})$.
- **4. Boundary Pitfalls**: Shifting by $a$ without setting bit $a-1$ (`(M << a) | (1 << (a - 1))`) loses the suffix consisting of the single element $a$ itself!

---

### 7.3 Tier 2 (`Intermediate`): Single & Multi-Pattern PGFs, Martingales & Basic `DP套DP` (`W4A-11` to `W4A-20`)

#### **`W4A-11` — `[CTSC2006] 歌唱王国` (Luogu P4548 — Singing Kingdom)**
- **Statement & Constraints**: Alphabet size $\sigma \le 10^5$, $T \le 50$ queries, each giving a pattern $S$ of length $L \le 10^5$. Characters in $\{1..\sigma\}$ are generated uniformly until $S$ appears. Output $\mathbb{E}[T_S] \bmod 10^4$.
- **1. The Diagnostic Signal**: $L \le 10^5$ per query makes $O(L^3)$ Markov Gaussian elimination impossible.
- **2. The Combinatorial Word Invariant**: By Equation (5.2) (proved via PGF $F'(1) = G(1)$ and Conway's Casino Martingale), surviving gamblers at stopping time $T_S$ correspond bijectively to $k \in \text{Borders}(S)$, each holding fortune $\sigma^k$:
  $$\mathbb{E}[T_S] = \sum_{k \in \text{Borders}(S)} \sigma^k \pmod{10^4}.$$
- **3. The Reverse-Engineering Scratchpad**: Build KMP `pi` array of $S$ in $O(L)$; traverse $k = L, \text{pi}[L], \text{pi}[\text{pi}[L]], \dots > 0$ summing $\sigma^k \bmod 10^4$.
- **4. Boundary Pitfalls**: Forgetting to include the improper border $k = L$ itself.

#### **`W4A-12` — `[SDOI2017] 硬币游戏` (Luogu P3706 — Coin Game)**
- **Statement & Constraints**: $m \le 300$ players each pick a distinct binary string $P_i \in \{\texttt{H}, \texttt{T}\}^L$ of length $L \le 300$. Fair coin flips continue until some $P_i$ appears. Find each player's winning probability $\pi_i$ to $10^{-6}$ precision.
- **1. The Diagnostic Signal**: Total AC states $m L = 9 \times 10^4$ is too large for $O((mL)^3)$ Gaussian elimination, whereas $m = 300$ is small.
- **2. The Combinatorial Word Invariant**: Since all $P_i$ have equal length $L$ and are distinct, $\mathcal{P}$ is an antichain. Using the normalized $(m+1) \times (m+1)$ system (5.5):
  $$\sum_{i=1}^m \pi_i \left(\sum_{k \in \text{Overlap}^+(P_i, P_j)} 2^{k - L}\right) - 2^{-L} \mathbb{E}[T] = 0 \quad (1 \le j \le m), \qquad \sum_{i=1}^m \pi_i = 1.$$
- **3. The Reverse-Engineering Scratchpad**: Compute all suffix-prefix overlaps via rolling hash or KMP in $O(m^2 L)$ and solve the $(m+1) \times (m+1)$ linear system in $O(m^3)$.
- **4. Boundary Pitfalls**: Using unscaled $2^k$ instead of $2^{k-L}$ risks floating-point overflow when $L > 1023$; also remember $\text{Overlap}^+(P_i, P_j)$ matches suffixes of $P_i$ against prefixes of $P_j$ (do not transpose $i$ and $j$!).

#### **`W4A-13` — `[JSOI2009] 有趣的游戏` (Luogu P2467 / BZOJ 1444)**
- **Statement & Constraints**: $m \le 10$ players, $|P_i| = L \le 10$, alphabet $\sigma \le 10$ with rational letter probabilities $p_c = a_c / b_c \ge 0$. Find each player's winning probability.
- **1. The Diagnostic Signal**: Letter probabilities are non-uniform and can be zero ($p_c = 0$).
- **2. The Combinatorial Word Invariant**: Use the division-free Guibas–Odlyzko system (5.5) where overlap term $k$ contributes $\mathbb{P}(P_j[k+1..L])$, and first discard any pattern containing a character with $p_c = 0$ ($\pi_j = 0$).
- **3. The Reverse-Engineering Scratchpad**: Filter zero-probability patterns, form the $(m'+1) \times (m'+1)$ matrix (or $V \le 100$ AC Markov matrix), and solve via Gaussian elimination.
- **4. Boundary Pitfalls**: Dividing by $\mathbb{P}(P_j[1..k])$ when $p_c = 0$ causes `NaN` / division by zero.

#### **`W4A-14` — `CF 86C — Genetic Engineering`**
- **Statement & Constraints**: Given $N \le 1000$ and $m \le 10$ DNA patterns of length $\le 10$, count strings $W \in \{\texttt{A}, \texttt{C}, \texttt{G}, \texttt{T}\}^N$ where **every** character of $W$ is covered by at least one occurrence of some $P_i \in \mathcal{P}$, modulo $10^9 + 9$.
- **1. The Diagnostic Signal**: Requires 100% tile coverage by overlapping patterns of length $\le 10$.
- **2. The Combinatorial Word Invariant**: Track `(ac_node u, uncovered_tail_len d)` where $0 \le d \le \max |P_i|$. Upon stepping $u \xrightarrow{c} v$, the uncovered tail becomes $d+1$, unless the longest pattern ending at $v$ (`max_len[v]` propagated down the `fail` tree) satisfies $\text{max\_len}[v] \ge d + 1$, which covers the entire uncovered tail and resets $d' \gets 0$!
- **3. The Reverse-Engineering Scratchpad**: Precompute $\text{max\_len}[u] = \max(\text{own\_len}[u], \text{max\_len}[\text{fail}[u]])$, run DP over `dp[r][u][d]`, and sum `dp[N][u][0]`.
- **4. Boundary Pitfalls**: Thinking a pattern of length $L < d+1$ reduces $d+1$ to $d+1-L$—it does NOT, because a gap remains at $r - d$!

#### **`W4A-15` — `[SDOI2014] 数数` (Luogu P3311)**
- **Statement & Constraints**: Count integers in $[1, N]$ ($N \le 10^{1200}$) whose decimal string avoids $\mathcal{P}$ ($\sum |P_i| \le 1500$) modulo $10^9 + 7$.
- **1. The Diagnostic Signal**: Product of Digit DP and AC Automaton DP.
- **2. The Combinatorial Word Invariant**: Leading zeros before the most significant nonzero digit do **not** exist in the decimal string of an integer, so while `leading_zero == true` and digit `0` is placed, the AC state must stay at $q_0$.
- **3. The Reverse-Engineering Scratchpad**: Memoized Digit DP over `(pos, ac_node, tight, leading_zero)` in $O(\log_{10} N \cdot 10 \cdot \sum |P_i|)$.
- **4. Boundary Pitfalls**: Stepping from $q_0$ on `'0'` during leading zeros falsely triggers forbidden patterns starting with `'0'`.

#### **`W4A-16` — `[HNOI2008] GT考试` (Luogu P3193)**
- **Statement & Constraints**: Count digit strings of length $N \le 10^9$ avoiding a single pattern $P$ of length $M \le 20$ modulo $K \le 1000$.
- **1. The Diagnostic Signal**: Large $N \le 10^9$, single pattern $M \le 20$, general modulus $K$.
- **2. The Combinatorial Word Invariant**: KMP transition matrix $T$ of size $M \times M$ (excluding state $M$), or linear recurrence of order $M$ from the Goulden–Jackson denominator $(1 - 10x)C_P(x) + x^M$.
- **3. The Reverse-Engineering Scratchpad**: Build $M \times M$ KMP matrix $T$ and compute $\sum_{j=0}^{M-1} (T^N)_{0, j} \bmod K$ in $O(M^3 \log N)$.
- **4. Boundary Pitfalls**: Modulus $K$ is not prime (so avoid division in Gaussian elimination).

#### **`W4A-17` — `[BJWC2011] 禁忌` (Luogu P3735)**
- **Statement & Constraints**: Given $\mathcal{P}$ ($\sum |P_i| \le 75$), alphabet $\sigma$, and $N \le 10^9$, a random string of length $N$ is scanned left-to-right: whenever any $P_i \in \mathcal{P}$ completes, score increments by $+1$ and the buffer is **cleared** (reset to root $q_0$). Find expected score.
- **1. The Diagnostic Signal**: Greedy non-overlapping matches reset the AC state to $q_0$.
- **2. The Combinatorial Word Invariant**: Redirect every transition $u \xrightarrow{c} v$ with `bad[v] == true` directly to $q_0$ with reward $+1$.
- **3. The Reverse-Engineering Scratchpad**: Maintain a block matrix (or pair of matrices $(P, E)$ for transition probability and expected score) of size $|Q| \times |Q|$ and exponentiate to power $N$ in $O(|Q|^3 \log N)$.
- **4. Boundary Pitfalls**: Leaving `bad[v]` states in the graph instead of immediately redirecting incoming edges to $q_0$.

#### **`W4A-18` — `AtCoder ABC 305 G — Banned Substrings`**
- **Statement & Constraints**: Given $N \le 10^{18}$ and $m \le 126$ banned binary strings of length $\le 6$, count avoiding binary strings of length $N$ modulo $998244353$.
- **1. The Diagnostic Signal**: $N \le 10^{18}$ and tiny pattern length $\le 6$.
- **2. The Combinatorial Word Invariant**: For $N \ge 5$, any banned substring of length $\le 6$ ending at step $t$ is determined by the last $5$ characters ($2^5 = 32$ De Bruijn states) plus the new character.
- **3. The Reverse-Engineering Scratchpad**: Brute-force $N < 5$; for $N \ge 5$, initialize valid length-$5$ masks avoiding $\mathcal{P}$ and multiply by $M^{N-5}$ in $O(32^3 \log N)$.
- **4. Boundary Pitfalls**: Forgetting to check if a banned string of length $\le 5$ already appears inside the initial 5-bit seed mask!

#### **`W4A-19` — `[BZOJ 3864] Hero meet devil`**
- **Statement & Constraints**: Given DNA string $S$ ($K = |S| \le 15$) and $N \le 1000$, count strings $T \in \{\texttt{A}, \texttt{C}, \texttt{G}, \texttt{T}\}^N$ with $\text{LCS}(S, T) = c$ for each $0 \le c \le K$ modulo $10^9 + 7$.
- **1. The Diagnostic Signal**: Canonical LCS `DP套DP` archetype.
- **2. The Combinatorial Word Invariant**: Inner LCS DP row $f[0..K]$ satisfies $\Delta f[j] = f[j] - f[j-1] \in \{0, 1\}$, bijecting with a $K$-bit mask $M \in [0, 2^K)$ with $\text{LCS}(S, T) = \text{popcount}(M)$.
- **3. The Reverse-Engineering Scratchpad**: Precompute `trans[M][ch]` in $O(K \cdot 4 \cdot 2^K)$, then run outer DP in $O(N \cdot 4 \cdot 2^K)$.
- **4. Boundary Pitfalls**: Recomputing inner LCS transitions inside the $N$-loop without precomputing `trans[M][ch]`.

#### **`W4A-20` — `UVa 11468 — Substring`**
- **Statement & Constraints**: Given $m \le 20$ patterns of length $\le 20$, character probabilities $p_c$, and length $N \le 100$, compute the probability that a random string of length $N$ avoids all patterns.
- **1. The Diagnostic Signal**: Evaluates survival probability $g_N = [z^N]G(z)$ on a biased alphabet.
- **2. The Combinatorial Word Invariant**: Biased AC automaton DP where safe transition $(u, c)$ multiplies by $p_c$.
- **3. The Reverse-Engineering Scratchpad**: Build AC automaton, propagate `bad[u]`, run $O(N V \sigma)$ DP.
- **4. Boundary Pitfalls**: Forgetting `bad[u] |= bad[fail[u]]`.

---

### 7.4 Tier 3 (`Advanced`): Product `DP套DP`, Minimal DFAs, Variance PGFs & Long-Pattern Clusters (`W4A-21` to `W4A-31`)

#### **`W4A-21` — `[TJOI2018] 游园会` (Luogu P4590)**
- **Statement & Constraints**: Given $S \in \{\texttt{N}, \texttt{O}, \texttt{I}\}^K$ ($K \le 15$) and $N \le 1000$, count strings $T \in \{\texttt{N}, \texttt{O}, \texttt{I}\}^N$ avoiding substring $\texttt{NOI}$ with $\text{LCS}(S, T) = c$ for each $0 \le c \le K$ modulo $10^9 + 7$.
- **1. The Diagnostic Signal**: Couples subsequence LCS `DP套DP` with substring KMP avoidance.
- **2. The Combinatorial Word Invariant**: Product DFA of the $2^K$-state LCS difference-mask automaton and the $3$-state KMP automaton for $\texttt{NOI}$ ($q \in \{0, 1, 2\}$).
- **3. The Reverse-Engineering Scratchpad**: Precompute `trans_mask[M][ch]` and `trans_kmp[q][ch]`; run rolling-array outer DP `dp[2][1 << K][3]` in $O(N \cdot 9 \cdot 2^K)$.
- **4. Boundary Pitfalls**: Transitioning $(q = 1 \text{ or } 2, \texttt{N}) \to 0$ instead of $q' = 1$, or exceeding the $128$ MB limit by not rolling the outer dimension $i$.

#### **`W4A-22` — `HDU 4352 — XHXJ's List`**
- **Statement & Constraints**: Given $L \le R \le 2^{63}-1$ and $1 \le K \le 10$, count integers in $[L, R]$ whose decimal digits have Longest Increasing Subsequence $\text{LIS} = K$.
- **1. The Diagnostic Signal**: Digit DP coupled with inner LIS DP across $10^4$ queries.
- **2. The Combinatorial Word Invariant**: The $O(N \log N)$ patience-sorting LIS array is strictly increasing over $\{0..9\}$, so it is encoded by a 10-bit subset mask $M \in [0, 2^{10})$ with $\text{LIS} = \text{popcount}(M)$! Appending digit $d$ replaces the smallest element $\ge d$ in $M$ with $d$ (or inserts $d$ if none exists).
- **3. The Reverse-Engineering Scratchpad**: Precompute `dp[pos][mask][K]` independent of $R$ (when `tight == false` and `started == true`) once outside the query loop; answer each query in $O(\log_{10} R)$ time.
- **4. Boundary Pitfalls**: Advancing `mask` on leading zeros before the first nonzero digit.

#### **`W4A-23` — `AtCoder AGC 022 E — Median Replace`**
- **Statement & Constraints**: Given $S \in \{\texttt{0}, \texttt{1}, \texttt{?}\}^N$ ($N \le 3 \times 10^5$ odd), repeatedly replace any 3 adjacent bits with their median until 1 bit remains. Count completions reducing to $\texttt{1}$ modulo $10^9 + 7$.
- **1. The Diagnostic Signal**: Interval reduction is $O(N^3)$; we need an $O(1)$-state left-to-right greedy stack DFA.
- **2. The Combinatorial Word Invariant**: Maintain a canonical stack where `11` at the bottom is capped (already an irreversible win), `000` reduces to `0`, and `1` on top of `0` cancels both (`01x -> x`). The stack only ever holds $a \in \{0, 1, 2\}$ ones followed by $b \in \{0, 1, 2\}$ zeros ($7$ reachable states, $5$ minimal Nerode classes), accepting iff $a \ge b$ at the end!
- **3. The Reverse-Engineering Scratchpad**: Run $O(N)$ outer DP over the $7$-state stack DFA.
- **4. Boundary Pitfalls**: Failing to cap $a$ at $2$ causes the stack to grow to $O(N)$.

#### **`W4A-24` — `[ZJOI2019] 麻将` (Luogu P5279 — Mahjong)**
- **Statement & Constraints**: $n \le 100$ tile types ($4$ copies each), $13$ initial tiles given. Draw remaining tiles uniformly at random until a winning hand ($4$ melds + $1$ pair, or $7$ distinct pairs) is formed. Output expected draws $\mathbb{E}[T] \bmod 998244353$.
- **1. The Diagnostic Signal**: $\mathbb{E}[T] = \sum_{k \ge 0} \mathbb{P}(T > k)$ requires counting tile multisets of size $k$ that do **not** contain a winning hand—an outer knapsack DP over an inner tile-scanning Hu-checker DP!
- **2. The Combinatorial Word Invariant**: The inner DP tracks two $3 \times 3$ matrices $f_0[j][k], f_1[j][k] \in \{-1, 0, \dots, 4\}$ (max melds with $0$ or $1$ pair given $j, k \in \{0, 1, 2\}$ open sequences) plus pair count $p \in [0, 7]$. Capping melds at $4$ and pairs at $7$, BFS reachability from the initial state discovers **only $2092$ non-winning states**!
- **3. The Reverse-Engineering Scratchpad**: Build the $2092$-state Mahjong DFA via BFS; run outer DP over $i = 1..n$, total drawn tiles $k \le 4n-13$, and DFA state $u \in [1, 2092]$ in $O(n^2 \cdot 2092)$.
- **4. Boundary Pitfalls**: Not clamping meld counts at $4$ or not merging all winning states into a single sink explodes the BFS state space.

#### **`W4A-25` — `CF 1207G — Indie Album`**
- **Statement & Constraints**: $n \le 4 \times 10^5$ strings defined on a Trie ($s_i$ appends a char to $s_{p_i}$), $q \le 4 \times 10^5$ queries asking for occurrences of pattern $P_j$ in $s_i$ ($\sum |P_j| \le 4 \times 10^5$).
- **1. The Diagnostic Signal**: Each $s_i$ can have length $O(n)$, so scanning $s_i$ per query is $O(n q)$.
- **2. The Combinatorial Word Invariant**: $P_j$ occurs ending at prefix $s_i[1..r]$ iff the AC node of $s_i[1..r]$ lies in the **subtree of $\text{end}(P_j)$ in the AC `fail` tree**!
- **3. The Reverse-Engineering Scratchpad**: Build the AC automaton of all $\{P_j\}$ and compute the Euler tour `[tin[u], tout[u]]` of its `fail` tree. DFS the input Trie of $s_i$ while walking the AC automaton: add $+1$ at `tin[u]` in a Fenwick tree on entry, answer all queries at $s_i$ by Fenwick range sum `[tin[end(P_j)], tout[end(P_j)]]`, and add $-1$ on exit!
- **4. Boundary Pitfalls**: Confusing the input Trie (which we DFS) with the query-pattern AC Trie/Automaton (whose `fail` tree supports the Fenwick tree).

#### **`W4A-26` — `[SDOI2017] 天才黑客` (Luogu P3703)**
- **Statement & Constraints**: Directed graph ($N, M \le 5 \times 10^4$) where each edge $e$ has a string label given as a node on a Trie ($|T| \le 2 \times 10^4$). Switching from incoming edge $e_1$ to outgoing edge $e_2$ at vertex $v$ costs $\text{LCP}(s(e_1), s(e_2))$. Find shortest paths from vertex $1$.
- **1. The Diagnostic Signal**: At a high-degree vertex $v$, adding $O(\text{deg}(v)^2)$ transition edges with LCA depths on the Trie TLEs.
- **2. The Combinatorial Word Invariant**: Build the **Virtual Tree** of the Trie nodes of all edges incident to $v$; for each Virtual Tree node $w$ with depth $d$, any incoming edge in one child subtree of $w$ and outgoing edge in a *different* child subtree of $w$ has $\text{LCA} = w$ (cost $d$), handled by prefix/suffix auxiliary nodes over the DFS order of $v$'s incident edges!
- **3. The Reverse-Engineering Scratchpad**: Construct prefix/suffix range edges on each vertex's Virtual Tree and run Dijkstra in $O(M \log M)$.
- **4. Boundary Pitfalls**: Off-by-one when excluding the same child subtree of $w$ in prefix/suffix range wiring.

#### **`W4A-27` — `AtCoder ABC 249 G / ARC 141 D — Two-Sided Palindromic Concatenation DFA`**
- **Statement & Constraints**: Given dictionary $D$ of words $w_i$ ($|D| \le 50, |w_i| \le 20$) with costs $c_i$, find the minimum cost (or count ways) to concatenate words from $D$ to form a palindrome.
- **1. The Diagnostic Signal**: A palindrome matches characters from both ends simultaneously, whereas words in $D$ have varying lengths.
- **2. The Combinatorial Word Invariant**: Grow the palindrome from both ends toward the center; at any moment, the unmatched **overhang** on either the left or right is a suffix or prefix of a single dictionary word $w_i$ ($O(\sum |w_i|)$ states)!
- **3. The Reverse-Engineering Scratchpad**: Run Dijkstra / DAG DP over overhang states `(side, word_id, rem_len)` transitioning by appending a new word to the shorter side.
- **4. Boundary Pitfalls**: Accepting an overhang state `(side, word_id, rem_len)` at termination without checking that the remaining overhang substring $w_i[\dots]$ is itself a **palindrome**!

#### **`W4A-28` — `QOJ / UCup — Multi-Pattern & Long-Pattern Avoidance ($|P_i|, N \le 10^5$)`**
- **Statement & Constraints**: Given $m \le 15$ patterns of length $L \le 5000$ (or $m=1, L \le 10^5$) and $N \le 10^5$ (or $N \le 10^{18}$), compute $a_N \bmod 998244353$.
- **1. The Diagnostic Signal**: Total AC states $\sum |P_i|$ is too large for $O(V^3)$ or $O(N V)$ DP.
- **2. The Combinatorial Word Invariant**: Reduce $\mathcal{P}$ to an antichain, build the $m \times m$ Goulden–Jackson overlap matrix $C_{i,j}(x) = \sum_{k \in \text{Overlap}^+(P_i, P_j)} x^{|P_j|-k}$, solve $\sum_{i=1}^m C_i(x) C_{i,j}(x) = -x^{|P_j|}$, and evaluate $F(x) = (1 - \sigma x - \sum C_i(x))^{-1}$.
- **3. The Reverse-Engineering Scratchpad**: Use KMP/Z-algorithm to build $C_{i,j}(x)$ in $O(m^2 L)$, solve the $m \times m$ system over $\mathbb{F}_p[[x]] \bmod x^{N+1}$ pivoting strictly on the diagonal $C_{j,j}(x)$ via NTT polynomial inversion in $O(m^3 N \log N)$ (or rational Cramer/Gauss + Bostan–Mori for $N \le 10^{18}$).
- **4. Boundary Pitfalls**: Failing to remove patterns containing shorter patterns before building $\mathbf{C}(x)$, or pivoting on off-diagonal $C_{i,j}(x)$ ($C_{i,j}(0) = 0$).

#### **`W4A-29` — `CF Gym 102538 / Extended [CTSC2006] — Stopping Time Variance $\text{Var}(T_S)$`**
- **Statement & Constraints**: Given $S$ ($|S| = L \le 10^6$) and biased letter probabilities $p_c > 0$, compute $\mathbb{E}[T_S]$ and $\text{Var}(T_S) \bmod 998244353$.
- **1. The Diagnostic Signal**: Requires second moment $\mathbb{E}[T_S^2]$ in $O(L)$ time.
- **2. The Combinatorial Word Invariant**: By Equation (5.3), $\text{Var}(T_S) = (\mathbb{E}[T_S])^2 + \mathbb{E}[T_S] - 2 \sum_{k \in \text{Borders}(S)} \frac{k}{\mathbb{P}(S[1..k])}$.
- **3. The Reverse-Engineering Scratchpad**: Walk KMP border chain $k = L, \text{pi}[L], \dots > 0$ accumulating $S_0 = \sum \mathbb{P}(S[1..k])^{-1}$ and $S_1 = \sum k \, \mathbb{P}(S[1..k])^{-1}$ in $O(L)$ time.
- **4. Boundary Pitfalls**: Dropping the $+\mathbb{E}[T_S]$ term when converting factorial moment $F''(1) = \mathbb{E}[T_S(T_S - 1)]$ to variance.

#### **`W4A-30` — `AtCoder AGC 020 E — Encoding Subsets`**
- **Statement & Constraints**: Given binary string $S$ ($|S| \le 100$), count valid run-length encodings $(P \times k)$ of all submasks $T \le S$ modulo $998244353$.
- **1. The Diagnostic Signal**: A repeated block $(P \times k)$ in $T \le S$ is valid iff $P$ is a submask of the **bitwise AND** of the $k$ contiguous blocks of $S$.
- **2. The Combinatorial Word Invariant**: Closure of $S$ under taking substrings and bitwise-AND of periodic slices produces $< 2000$ distinct strings across all lengths!
- **3. The Reverse-Engineering Scratchpad**: Memoize `solve(U)` using an `std::map<string, mint>`, splitting $U$ into its first atomic token ($1$ char or $(V \times k)$ for $k \ge 2$) plus the remaining suffix.
- **4. Boundary Pitfalls**: Allowing the first token to be an unparenthesized multi-character string double-counts concatenations.

#### **`W4A-31` — `CF 1349D / Seed-Prefix Conditional Pattern Race`**
- **Statement & Constraints**: Given an initial string prefix $S_0$ already on the tape and competing patterns $P_1, \dots, P_m$, find each pattern's winning probability and expected remaining steps $\mathbb{E}[T \mid S_0]$.
- **1. The Diagnostic Signal**: Non-empty initial condition $S_0 \ne \epsilon$ breaks the homogeneous $0$ right-hand side of standard Conway equations.
- **2. The Combinatorial Word Invariant**: By Section 2.2, gamblers who entered during $S_0$ and survived to the end of $S_0$ hold initial fortune $\Omega_{S_0, P_j} = \sum_{k \in \text{Overlap}(S_0, P_j)} \mathbb{P}(P_j[1..k])^{-1}$, shifting the $j$-th equation to $\sum_i \pi_i \Omega_{P_i, P_j} - \mathbb{E}[T \mid S_0] = \Omega_{S_0, P_j}$.
- **3. The Reverse-Engineering Scratchpad**: Check if $S_0$ already contains some $P_i$; otherwise compute $\Omega_{S_0, P_j}$ and solve the $(m+1) \times (m+1)$ system.
- **4. Boundary Pitfalls**: Forgetting to check whether a pattern $P_i$ has *already* occurred inside $S_0$ before $t = 0$.

---

### 7.5 Tier 4 (`Mastery`): Dynamic AC Grouping, Bivariate Moment Shifts, Non-Antichain Clusters & Minimal DFA Synthesis (`W4A-32` to `W4A-42`)

#### **`W4A-32` — `CF 710F — String Set Queries`**
- **Statement & Constraints**: $m \le 3 \times 10^5$ online operations (insert pattern $P$, delete pattern $P$, query total occurrences of active patterns in text $T$), $\sum |P| + \sum |T| \le 3 \times 10^5$, forced online.
- **1. The Diagnostic Signal**: AC `fail` links cannot be maintained dynamically in $O(1)$ per character insertion.
- **2. The Combinatorial Word Invariant (Binary Grouping / `二进制分组`)**: Occurrence counts are linear over disjoint pattern sets. Maintain an insertion collection and a deletion collection, each partitioned into $O(\log m)$ immutable AC automata of sizes $2^{k_1} > 2^{k_2} > \dots$; merge equal-sized blocks by rebuilding AC from scratch in $O((\sum |P|) \log m)$ total time.
- **3. The Reverse-Engineering Scratchpad**: Query $T$ across the $\le \log_2 m$ insertion automata minus the $\le \log_2 m$ deletion automata in $O(|T| \log m)$.
- **4. Boundary Pitfalls**: Re-allocating 26-width transition tables without recycling deleted block nodes can exceed memory limits if not pooled.

#### **`W4A-33` — `UOJ / QOJ — Exact $k$ Occurrences of a Long Pattern`**
- **Statement & Constraints**: Given pattern $P$ ($L \le 5 \times 10^4$), $N \le 10^5$, $0 \le k \le N$, alphabet $\sigma$, compute the number of strings of length $N$ with **exactly $k$** occurrences of $P$ modulo $998244353$.
- **1. The Diagnostic Signal**: $O(N L k)$ DP is infeasible; requires bivariate cluster extraction $[x^N t^k] F(x, t)$.
- **2. The Combinatorial Word Invariant**: By Equation (4.3), for $k \ge 1$, $F_k(x) = \frac{x^L D_1(x)^{k-1}}{D_0(x)^{k+1}}$.
- **3. The Reverse-Engineering Scratchpad**: Compute $C_P(x)$ via KMP in $O(L)$, factor out the lowest nonzero term $c x^d$ of $D_1(x)$ ($d = \min\text{Period}(P) \ge 1$), and compute $D_1(x)^{k-1} D_0(x)^{-(k+1)} \bmod x^{N-L+1}$ via FPS $\ln/\exp$ in $O(N \log N)$.
- **4. Boundary Pitfalls**: Calling `poly_ln` directly on $D_1(x)$ without shifting by $x^d$ fails because $D_1(0) = 0$! Also handle $k = 0$ separately via $\frac{C_P(x)}{D_0(x)}$.

#### **`W4A-34` — `UCup / QOJ — Expected $K$-th Power $\mathbb{E}[\text{occ}_P(W)^K]$ in Huge Strings ($n \le 10^{18}$)`**
- **Statement & Constraints**: Given $P$ ($L \le 10^5$), $n \le 10^{18}$ (or $10^9$), $K \le 20$, compute $\sum_{W \in \Sigma^n} \text{occ}_P(W)^K \bmod 998244353$.
- **1. The Diagnostic Signal**: Expanding around $t = 0$ gives denominator $D_0(x)^{k+1}$ of degree $\approx K L \approx 2 \times 10^6$, which is expensive for Bostan–Mori.
- **2. The Combinatorial Word Invariant (The $t = 1 + u$ Binomial Moment Shift)**: By Equation (4.4), expanding $F(x, 1 + u)$ around $t = 1$ gives $[u^j] F(x, 1+u) = \frac{x^L D_1(x)^{j-1}}{(1 - \sigma x)^{j+1}}$, whose denominator is simply $(1 - \sigma x)^{j+1}$!
- **3. The Reverse-Engineering Scratchpad**: Compute $x^L D_1(x)^{j-1}$ of degree $\le j L$ via NTT for $1 \le j \le K$, read off $[x^n] \frac{x^L D_1(x)^{j-1}}{(1 - \sigma x)^{j+1}} = \sum_d c_d \binom{n - d + j}{j} \sigma^{n - d}$, and combine with Stirling numbers $\left\{\begin{matrix} K \\ j \end{matrix}\right\} j!$ in $O(K L \log(KL))$ time!
- **4. Boundary Pitfalls**: Expanding around $t = 0$ instead of $t = 1$ ($u = t - 1$).

#### **`W4A-35` — `AtCoder AGC 058 D — Yet Another ABC String`**
- **Statement & Constraints**: Given $A, B, C \le 10^6$, count strings with $A$ `'A'`s, $B$ `'B'`s, $C$ `'C'`s avoiding `"ABC"`, `"BCA"`, `"CAB"` modulo $998244353$.
- **1. The Diagnostic Signal**: 3-variable exact character count ($x^A y^B z^C$) with cyclic forbidden patterns.
- **2. The Combinatorial Word Invariant**: Any cluster of $\{\texttt{ABC}, \texttt{BCA}, \texttt{CAB}\}$ is a cyclic run `"ABCABC..."` of length $L \ge 3$, with univariate cluster GF $\frac{-3x^3}{1 + x + x^2} = \sum_{k \ge 1} \bigl(3(-1)^k x^{3k} - 3(-1)^k x^{3k+1}\bigr)$. Every cluster of length $3k + 2$ has weight **$0$**, and clusters of length $3k$ or $3k+1$ use equal numbers $k$ of `'A'`, `'B'`, `'C'` (plus at most $1$ extra letter for $3k+1$)!
- **3. The Reverse-Engineering Scratchpad**: Sum over the number $k \le \min(A, B, C)$ of $(xyz)$ triples consumed by clusters using a single $O(\min(A, B, C))$ binomial-coefficient loop!
- **4. Boundary Pitfalls**: Missing the $1 + x + x^2$ cancellation that zeroes out all $3k+2$ clusters.

#### **`W4A-36` — `THUPC / QOJ — Non-Antichain Weighted Pattern Product`**
- **Statement & Constraints**: Given $m \le 8$ patterns $P_1, \dots, P_m$ ($L \le 2000$, where $P_i$ may be substrings of $P_j$) with occurrence weights $w_i \in \mathbb{F}_p$, compute $\sum_{W \in \Sigma^n} \prod_{i=1}^m w_i^{\text{occ}_i(W)} \bmod 998244353$ for $n \le 10^5$.
- **1. The Diagnostic Signal**: Non-antichain pattern set where $w_i \ne 0$ forbids deleting super-patterns $P_j$.
- **2. The Combinatorial Word Invariant**: Apply the Non-Antichain Embedded Substring Absorption formula (Section 4.3), replacing $(w_j - 1)$ with $\widetilde{W}_j = (w_j - 1)\prod_{P_i \subsetneq P_j} w_i^{\text{occ}(P_i, P_j)}$ and adjusting overlap weights for internal/straddling occurrences.
- **3. The Reverse-Engineering Scratchpad**: Precompute internal and straddling occurrences via AC automaton, solve the $m \times m$ polynomial system mod $x^{n+1}$.
- **4. Boundary Pitfalls**: Double-counting a short pattern $P_i$ contained inside the overlap $P_b[1..k]$ of $P_a$ and $P_b$.

#### **`W4A-37` — `CF 1608F / AGC 039 F / Duval Lyndon Automaton Counting`**
- **Statement & Constraints**: Count strings $W \in \{1..\sigma\}^n$ ($n \le 100$) that are Lyndon words (or have $k$ Lyndon factors) while satisfying an auxiliary automaton constraint.
- **1. The Diagnostic Signal**: Coupling Lyndon factorization with left-to-right DP.
- **2. The Combinatorial Word Invariant**: Duval's algorithm tracks the current pre-Lyndon length $L$ and period $p$: appending $c = W[L - p + 1]$ preserves period $p$, appending $c > W[L - p + 1]$ resets $p' \gets L+1$ (making the prefix a simple Lyndon word), and $c < W[L - p + 1]$ is forbidden for a single Lyndon word.
- **3. The Reverse-Engineering Scratchpad**: Combine Duval pointer state with deferred alphabet assignment.
- **4. Boundary Pitfalls**: Accepting a proper periodic repetition ($p \mid L, p < L$) as a Lyndon word at the end ($p$ must equal $L$).

#### **`W4A-38` — `AtCoder AGC 064 C / Palindrome-Avoiding Restricted-Growth DFA`**
- **Statement & Constraints**: Count strings of length $n \le 10^{18}$ over alphabet $\sigma$ avoiding all palindromes of length $\ge K$ ($K \le 10$).
- **1. The Diagnostic Signal**: Every palindrome of length $\ge K$ contains a palindrome of length $K$ or $K+1$.
- **2. The Combinatorial Word Invariant**: Encode the last $K$ characters up to alphabet isomorphism as a Restricted Growth String (at most Bell number $B_{10}$ states), prune states containing a length-$K$ or $(K+1)$ palindrome, and run Hopcroft DFA minimization to get $< 100$ Nerode states!
- **3. The Reverse-Engineering Scratchpad**: Offline BFS + Hopcroft minimization + matrix exponentiation in $O(V_{\min}^3 \log n)$.
- **4. Boundary Pitfalls**: Forbidding only length $K$ and forgetting length $K+1$ (which misses even/odd parity palindromes).

#### **`W4A-39` — `Project Euler 597 / Penney's Game Optimal Counter-Pattern`**
- **Statement & Constraints**: Given Player 1's binary pattern $P_1 \in \{0, 1\}^L$, find Player 2's pattern $P_2 \in \{0, 1\}^L$ maximizing $\pi_2$.
- **1. The Diagnostic Signal**: Optimizing over $2^L$ candidate patterns using the $2 \times 2$ Conway payoff matrix $\Omega$.
- **2. The Combinatorial Word Invariant**: From $\pi_2 = \frac{\Omega_{1,1} - \Omega_{1,2}}{(\Omega_{1,1} - \Omega_{1,2}) + (\Omega_{2,2} - \Omega_{2,1})}$, choosing $P_2 = b \cdot P_1[1..L-1]$ for $b \in \{0, 1\}$ guarantees $\Omega_{2,1} \ge 2^{L-1}$, intercepting $P_1$ one step before completion!
- **3. The Reverse-Engineering Scratchpad**: Evaluate the two candidates $b \in \{0, 1\}$ via their border sets in $O(L)$ time.
- **4. Boundary Pitfalls**: Choosing $P_2 = P_1$, which violates the distinct-pattern race precondition.

#### **`W4A-40` — `[国家集训队论文] Regex & Game Counting via Hopcroft / Brzozowski Minimization`**
- **Statement & Constraints**: Given a regular expression (or custom string reduction game) and $N \le 10^{18}$, count matching strings of length $N$ modulo $998244353$.
- **1. The Diagnostic Signal**: An $\epsilon$-NFA cannot be used directly for counting because a single string can have multiple accepting paths.
- **2. The Combinatorial Word Invariant**: Convert $\epsilon$-NFA to deterministic DFA via reachable subset construction, then minimize via Hopcroft partition refinement (or Brzozowski's double-reversal $\text{det}(\text{rev}(\text{det}(\text{rev}(\mathcal{A}))))$, Section 2.5).
- **3. The Reverse-Engineering Scratchpad**: Subset construction $\to$ Hopcroft minimization $\to$ Berlekamp–Massey + Bostan–Mori in $O(V_{\min}^2 + V_{\min} \log V_{\min} \log N)$.
- **4. Boundary Pitfalls**: Counting paths in an unambiguous-looking NFA that actually has subtle multi-path ambiguity.

#### **`W4A-41` — `LOJ 3042 / Random Walk to String Target with Backspace/Reset`**
- **Statement & Constraints**: Characters are appended randomly, or with probability $p_0$ the last character is deleted (or reset), until $S$ ($|S| \le 10^5$) is formed. Compute $\mathbb{E}[T_S]$.
- **1. The Diagnostic Signal**: Backspaces break the standard $\sigma^k$ martingale multiplier.
- **2. The Combinatorial Word Invariant**: On the KMP DAG + back-edges of $S$, only one forward edge advances $u \to u+1$, so $dp[u] = E[u] - E[u+1]$ satisfies a linear recurrence in $dp[v]$ for $v \le u$, solvable in $O(|S| |\Sigma|)$ from $u = 0$ to $|S|-1$.
- **3. The Reverse-Engineering Scratchpad**: Solve for $dp[u] = E[u] - E[u+1]$ sequentially and output $\sum_{u=0}^{|S|-1} dp[u]$.
- **4. Boundary Pitfalls**: Applying $\sum_{k \in \text{Borders}(S)} \sigma^k$ when backspaces are present.

#### **`W4A-42` — `UCup / QOJ — Palindromic & Cyclic Goulden–Jackson`**
- **Statement & Constraints**: Count palindromes (or circular strings) of length $N \le 10^5$ avoiding $\mathcal{P}$ ($\sum |P_i| \le 10^5$).
- **1. The Diagnostic Signal**: Palindromic symmetry $W[i] = W[N-i+1]$ couples the left and right halves of the string, while circular strings forbid wrap-around occurrences across $N \to 1$.
- **2. The Combinatorial Word Invariant**: For palindromes (assuming $\mathcal{P} = \mathcal{P}^R$), marked words decompose from the outside in into symmetric pairs of free letters ($\sigma x^2$), symmetric pairs of clusters ($C(x^2)$), and a single central palindrome-symmetric cluster (or central free letter) straddling the midpoint $N/2$. For circular words, apply the logarithmic derivative + wrap-around trace correction (Section 2.4).
- **3. The Reverse-Engineering Scratchpad**: Solve the linear cluster system for $C_i(x)$, compute the central symmetric cluster polynomial $C_{\text{mid}}(x)$, and evaluate $(1 + \sigma x + C_{\text{mid}}(x)) / (1 - \sigma x^2 - C(x^2))$ via FPS inversion in $O(N \log N)$.
- **4. Boundary Pitfalls**: Forgetting clusters that straddle the exact center of the palindrome (which appear only once, with $x^L$, rather than paired with $x^{2L}$).

---

### 7.6 Reconciled Quarantine Ledger (`R-4A-01` to `R-4A-12` — Excluded Pure Template Problems)

The union of all pure template verification problems flagged by Cohort 1 and Cohort 2 is strictly quarantined from textbook chapters:

| Quarantine ID | Problem Source & Title | Cohort Flag | Reason for Quarantine |
| :--- | :--- | :--- | :--- |
| **`R-4A-01`** | Luogu P3808 — `【模板】AC 自动机（简单版）` | C1 + C2 | Bare Aho–Corasick construction & single-pass matching template. |
| **`R-4A-02`** | Luogu P3796 — `【模板】AC 自动机（加强版）` | C1 + C2 | Standard AC occurrence counting template without DP or GF reduction. |
| **`R-4A-03`** | Luogu P5357 — `【模板】AC 自动机（二次加强版）` | C1 + C2 | Bare AC `fail`-tree topological subtree sum template. |
| **`R-4A-04`** | Luogu P3804 — `【模板】后缀自动机（SAM）` | C1 | Bare SAM construction and `len[u] * cnt[u]` Link-Tree sum template. |
| **`R-4A-05`** | Library Checker — `Number of Substrings` | C1 | Pure template verification of $\sum (\text{len}(u) - \text{len}(\text{link}(u)))$. |
| **`R-4A-06`** | Luogu P3375 — `【模板】KMP` | C1 + C2 | Baseline KMP border array verification assumed in reader's library. |
| **`R-4A-07`** | Library Checker — `Z Algorithm` | C2 | Pure prefix-match array verification with zero combinatorial modeling. |
| **`R-4A-08`** | Luogu P3389 — `【模板】高斯消元法` | C1 | Routine linear algebra library routine without string-overlap structure. |
| **`R-4A-09`** | Luogu P4723 — `【模板】常系数齐次线性递推` | C1 | Pure Bostan–Mori / Kitamasa library template (covered in FPS textbook). |
| **`R-4A-10`** | Library Checker — `Find Linear Recurrence / Kth Term` | C2 | Pure Berlekamp–Massey / Bostan–Mori algebra template. |
| **`R-4A-11`** | HDU 2222 — `Keywords Search` | C2 | Bare Aho–Corasick textbook template problem. |
| **`R-4A-12`** | POJ 1204 — `Word Puzzles` | C2 | 2D grid Aho–Corasick search implementation exercise with no theoretical reduction. |

---

## 8. Consolidated Multilingual Bibliography, Rosetta Stone & Diagnostic Routing Matrix

### 8.1 Master Bibliography for Wave 4A

1. **Goulden, I. P., & Jackson, D. M. (1979)**. *An inversion theorem for cluster decompositions of sequences with distinguished subsequences*. Journal of the London Mathematical Society, s2-20(3), 567–576.
2. **Guibas, L. J., & Odlyzko, A. M. (1981)**. *String overlaps, pattern matching, and nontransitive games*. Journal of Combinatorial Theory, Series A, 30(2), 183–208.
3. **Li, S.-Y. R. (1980)**. *A martingale approach to the study of occurrence of sequence patterns in repeated experiments*. The Annals of Probability, 8(6), 1171–1176.
4. **Noonan, J., & Zeilberger, D. (1999)**. *The Goulden–Jackson cluster method: extensions, applications, and implementations*. Journal of Difference Equations and Applications, 5(4-5), 355–377.
5. **Graham, R. L., Knuth, D. E., & Patashnik, O. (1994)**. *Concrete Mathematics* (2nd ed., Chapter 8.4: Flipping Coins). Addison-Wesley.
6. **Flajolet, P., & Sedgewick, R. (2009)**. *Analytic Combinatorics* (Chapter I.4 & III.7: Autocorrelation and Pattern Avoidance). Cambridge University Press.
7. **Brzozowski, J. A. (1962)**. *Canonical regular expressions and minimal state graphs for definite events*. Mathematical Theory of Automata, 529–561.
8. **Hopcroft, J. (1971)**. *An $n \log n$ algorithm for minimizing states in a finite automaton*. Theory of Machines and Computations, 189–196.
9. **中国国家集训队论文 (Chinese National Team Papers)**:
   - 刘家骅 (Liu Jiahua, 2018), *《浅谈“DP套DP”问题》* (`DP套DP`, inner-DP DFA construction, difference state compression, and Myhill–Nerode minimization).
   - 钟知闲 (Zhong Zhixian) / 杜瑜皓 (Du Yuhao), *《概率生成函数在字符串匹配问题中的应用》* (PGFs, Conway's Martingale, `[CTSC2006] 歌唱王国`, `[SDOI2017] 硬币游戏`).
10. **Japanese Competitive Stringology Treatises (`[JA]`)**:
    - `maspypy` — *文字列の周期とオートマトン・母関数 (String Periodicity, Automata, and Generating Functions / Goulden–Jackson Cluster Method)*.
    - `noshi91` / `tatyam` — *DFA Minimization & Automaton DP (`自動機上のDP` / `DP of DP`) in AtCoder Grand Contests*.

### 8.2 Wave 4A Multilingual Stringology Rosetta Stone (`[EN]` $\leftrightarrow$ `[ZH]` $\leftrightarrow$ `[JA]`)

| English (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) | Core Mathematical Object |
| :--- | :--- | :--- | :--- |
| **Goulden–Jackson Cluster Method** | **Goulden–Jackson 簇方法 / 标记串容斥** | **Goulden–Jackson 法 (クラスター法)** | PIE over overlapping marked pattern chains (`clusters`) |
| **Autocorrelation / Overlap Polynomial** | **自相关多项式 / 互相关多项式 $C_{i,j}(x)$** | **自己相関多項式 / オーバーラップ多項式** | $C_{i,j}(x) = \sum_{k \in \text{Overlap}^+(P_i, P_j)} x^{|P_j|-k}$ |
| **Probability Generating Function (PGF)** | **概率生成函数** | **確率母関数** | $F(z) = \sum_{n \ge 0} \mathbb{P}(T = n) z^n$, $\mathbb{E}[T] = F'(1)$ |
| **Conway's Casino Martingale** | **康威赌博 (鞅与可选停时定理)** | **コンウェイのギャンブル (マルチンゲール)** | Fair sequential betting where surviving bettors match $\text{Borders}(S)$ |
| **DP of DP / Automaton DP** | **DP套DP / 自动机上的动态规划** | **自動機上のDP / DP of DP** | Outer counting DP over reachable states of an inner decision/value DP |
| **Myhill–Nerode Equivalence & Hopcroft Minimization** | **Myhill–Nerode 等价类与最小化 DFA** | **DFA 最小化 (Nerode 同値関係)** | Quotienting inner DP states by suffix indistinguishability |
| **Binary Grouping of AC Automata** | **AC自动机二进制分组** | **Aho–Corasick 法のバイナリグルーピング** | Dynamizing static AC structures into $O(\log M)$ powers-of-two blocks |

### 8.3 Master Wave 4A Diagnostic Routing Matrix

| Problem Signature & Constraints | Why Competing Approaches Fail | Reconciled Wave 4A Engine | Optimal Complexity |
| :--- | :--- | :--- | :--- |
| $\sum |P_i| \le 200$, $N \le 10^{18}$, arbitrary pattern containment | GJ requires antichain reduction or non-antichain weights | **AC Safe Transfer Matrix + Matrix Exponentiation** | $O(V^3 \log N)$ ($V \le \sum |P_i|$) |
| Avoid single pattern $P$ ($L \le 10^5$), all $n \le N \le 10^5$ | KMP DP takes $O(N L) = 10^{10}$ | **Single-Pattern Guibas–Odlyzko + FPS Inversion**: $\frac{C_P(x)}{(1-\sigma x)C_P(x) + x^L}$ | $O(L + N \log N)$ |
| Avoid $m \le 15$ long patterns ($L \le 10^5$), huge $N \le 10^{18}$ | AC automaton has $V = O(m L)$ states; $O(V^3)$ impossible | **Goulden–Jackson $m \times m$ System + Bostan–Mori** | $O(m^2 L + m^3 D \log D + D \log D \log N)$ |
| Exactly $k$ occurrences of $P$ ($L, N \le 10^5$) | 2D KMP DP takes $O(N L k)$ | **Bivariate $(t-1)$ Cluster GF $[t^k]F(x,t) = \frac{x^L D_1(x)^{k-1}}{D_0(x)^{k+1}}$** | $O(L + N \log N)$ |
| Moment $\mathbb{E}[\text{occ}_P(W)^K]$ ($K \le 20, L \le 10^5, N \le 10^{18}$) | Expanding around $t=0$ has degree-$KL$ denominator $D_0(x)^{K+1}$ | **$t = 1 + u$ Binomial Moment Shift around $t = 1$** (Eq. 4.4) | $O(K L \log(KL))$ |
| Single pattern $S$ ($L \le 10^6$), $\mathbb{E}[T_S]$ and $\text{Var}(T_S)$ | State elimination on $10^6$ states is error-prone for variance | **Conway Martingale & PGF Derivatives $F'(1), F''(1)$** (Eqs. 5.2–5.3) | $O(L)$ |
| $m \le 300$ patterns ($L \le 10^5$), pattern race probabilities $\pi_i$ | AC Markov Gaussian elimination is $O((mL)^3)$ | **Conway / Guibas–Odlyzko $(m+1) \times (m+1)$ Overlap System** (Eqs. 5.4–5.5) | $O(m^2 L + m^3)$ |
| Count strings $T \in \Sigma^N$ by output of inner DP $f(S, T)$ ($|S| \le 15$) | Naive inner state has $(K+1)^K$ tuples | **4-Stage `DP套DP` Pipeline (Difference/Capped BFS + Hopcroft Minimization)** | $O(|\Sigma| V \log V + N |\Sigma| V_{\min})$ |
| Online pattern insert/delete + occurrence queries ($\sum |P|, \sum |T| \le 3 \times 10^5$) | AC `fail` pointers cannot be updated online in $O(1)$ | **Binary Grouping (`二进制分组`) of $O(\log M)$ Immutable AC Automata** | $O((\sum |P| + \sum |T|) \log M)$ |

---

## 9. Reconciled Hand-Checkable Numerical Traces & Verification Scratchpads

To preserve every pedagogical trace from Cohort 1 and Cohort 2 in one canonical reference for Phase 2 textbook authoring, we include the four foundational hand-checked traces below.

### 9.1 Trace 1: Border Clustering Density ($P = \texttt{ABA}$ vs. $P = \texttt{AAA}$, $\sigma = 2$) & Exact $k = 1$ Occurrence of $\texttt{AA}$

1. **Why Stronger Borders Produce *More* Avoiding Strings (`ABA` vs. `AAA`, $L = 3, \sigma = 2$)**:
   - **Case $P = \texttt{ABA}$**: Borders are $k \in \{3, 1\}$, so $C_{\texttt{ABA}}(x) = x^{3-3} + x^{3-1} = 1 + x^2$.
     $$F_{\texttt{ABA}}(x) = \frac{1 + x^2}{(1 - 2x)(1 + x^2) + x^3} = \frac{1 + x^2}{1 - 2x + x^2 - x^3} = 1 + 2x + 4x^2 + 7x^3 + 12x^4 + 21x^5 + \cdots$$
     At $n = 4$: $4$ strings contain $\texttt{ABA}$ ($\texttt{ABAA}, \texttt{ABAB}, \texttt{AABA}, \texttt{BABA}$), leaving $16 - 4 = 12$.
     At $n = 5$: $\texttt{ABABA}$ contains two overlapping copies of $\texttt{ABA}$ (`[1..3]` and `[3..5]`), which is corrected by the 2-pattern cluster weight $(-1)^2 x^5 = +x^5$, giving $32 - 12 + 1 = 21$.
   - **Case $P = \texttt{AAA}$**: Borders are $k \in \{3, 2, 1\}$, so $C_{\texttt{AAA}}(x) = 1 + x + x^2$.
     $$F_{\texttt{AAA}}(x) = \frac{1 + x + x^2}{(1 - 2x)(1 + x + x^2) + x^3} = \frac{1 + x + x^2}{1 - x - x^2 - x^3} = 1 + 2x + 4x^2 + 7x^3 + 13x^4 + 24x^5 + \cdots$$
     At $n = 4$: Because $\texttt{AAA}$ has a length-$2$ border ($x^1$ term in $C_{\texttt{AAA}}(x)$), $\texttt{AAAA}$ packs two occurrences of $\texttt{AAA}$ inside length $4$! Thus only $3$ strings contain $\texttt{AAA}$ ($\texttt{AAAA}, \texttt{AAAB}, \texttt{BAAA}$), leaving $16 - 3 = 13 > 12$ avoiding strings!
2. **Exact $k = 1$ Occurrence of $P = \texttt{AA}$ ($L = 2, \sigma = 2$) via Equation (4.3)**:
   - Here $C_{\texttt{AA}}(x) = 1 + x$, $D_0(x) = (1 - 2x)(1 + x) + x^2 = 1 - x - x^2$, and $D_1(x) = (1 - 2x)x + x^2 = x - x^2$.
   - For $k = 1$, Formula (4.3) gives:
     $$F_1(x) = \frac{x^2 D_1(x)^0}{D_0(x)^2} = \frac{x^2}{(1 - x - x^2)^2} = x^2 + 2x^3 + 5x^4 + 10x^5 + \cdots$$
   - Hand-check $n = 3$: Strings with *exactly* $1$ copy of $\texttt{AA}$ are $\texttt{AAB}, \texttt{BAA}$ ($\texttt{AAA}$ has $2$ overlapping copies of $\texttt{AA}$!), so $[x^3] F_1(x) = 2$.
   - Hand-check $n = 4$: Strings with *exactly* $1$ copy of $\texttt{AA}$ are $\texttt{AABA}, \texttt{AABB}, \texttt{BAAB}, \texttt{ABAA}, \texttt{BBAA}$ ($5$ strings; $\texttt{AAAA}$ has $3$ copies, $\texttt{AAAB}$ and $\texttt{BAAA}$ have $2$ copies), matching $[x^4] F_1(x) = 5$.

---

### 9.2 Trace 2: Two Penney's Game Paradoxes (`HHT` vs. `THH` Non-Transitivity & `HTH` vs. `HTT` Tie Paradox)

1. **Equal Solo Expectations ($8$ vs. $8$), $3:1$ Head-to-Head Asymmetry ($P_1 = \texttt{HHT}$ vs. $P_2 = \texttt{THH}$, $\sigma = 2$)**:
   - Solo waiting times: neither $\texttt{HHT}$ nor $\texttt{THH}$ has a proper border, so $\mathbb{E}[T_{\texttt{HHT}}] = \mathbb{E}[T_{\texttt{THH}}] = 2^3 = 8$.
   - Payoff matrix $\Omega_{i,j} = \sum_{k \in \text{Overlap}^+(P_i, P_j)} 2^k$:
     - $\Omega_{1,1} = 2^3 = 8$, $\Omega_{1,2} = 2^1 = 2$ (suffix `T` of `HHT` matches prefix `T` of `THH`).
     - $\Omega_{2,1} = 2^1 + 2^2 = 6$ (suffixes `H` and `HH` of `THH` match prefixes of `HHT`), $\Omega_{2,2} = 2^3 = 8$.
   - Linear system (5.4):
     $$\begin{cases} 8 \pi_1 + 6 \pi_2 = \mathbb{E}[T] \\ 2 \pi_1 + 8 \pi_2 = \mathbb{E}[T] \\ \pi_1 + \pi_2 = 1 \end{cases} \implies 6 \pi_1 = 2 \pi_2 \implies \pi_1 = \frac{1}{4}, \;\; \pi_2 = \frac{3}{4}, \;\; \mathbb{E}[T] = \frac{13}{2}.$$
2. **Unequal Solo Expectations ($10$ vs. $8$), $1:1$ Head-to-Head Tie ($P_1 = \texttt{HTH}$ vs. $P_2 = \texttt{HTT}$, $\sigma = 2$)**:
   - Solo waiting times: $\mathbb{E}[T_{\texttt{HTH}}] = 2^3 + 2^1 = 10 > 8 = 2^3 = \mathbb{E}[T_{\texttt{HTT}}]$.
   - Payoff matrix: $\Omega_{1,1} = 10$, $\Omega_{1,2} = 2^1 = 2$, $\Omega_{2,1} = 0$, $\Omega_{2,2} = 8$.
   - Linear system (5.4):
     $$\begin{cases} 10 \pi_1 + 0 \pi_2 = \mathbb{E}[T] \\ 2 \pi_1 + 8 \pi_2 = \mathbb{E}[T] \\ \pi_1 + \pi_2 = 1 \end{cases} \implies 8 \pi_1 = 8 \pi_2 \implies \pi_1 = \pi_2 = \frac{1}{2}, \;\; \mathbb{E}[T] = 5.$$
     Even though $\texttt{HTH}$ takes $25\%$ longer on average to appear alone, it ties $\texttt{HTT}$ $50\%$–$50\%$ in a race because whenever $\texttt{HTH}$ wins, the $\texttt{HTT}$-syndicate holds a live $\$2$ bet ($\Omega_{1,2} = 2$), whereas when $\texttt{HTT}$ wins, the $\texttt{HTH}$-syndicate holds $\$0$ ($\Omega_{2,1} = 0$)!

---

### 9.3 Trace 3: Hopcroft Partition Refinement on a 6-State Inner DP Automaton (`DP套DP` Minimization)

Suppose Stage 2 (BFS reachability) of a `DP套DP` problem produces $6$ reachable inner DP states $Q_{\text{reach}} = \{q_0, q_1, q_2, q_3, q_4, q_5\}$ over $\Sigma = \{\texttt{0}, \texttt{1}\}$ with accepting set $F = \{q_3, q_4, q_5\}$:

| State $u$ | $\delta(u, \texttt{0})$ | $\delta(u, \texttt{1})$ | Accepting? | Initial Block $\Pi_0(u)$ | Destination Classes $\bigl(\Pi_0(\delta(u,\texttt{0})), \Pi_0(\delta(u,\texttt{1}))\bigr)$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $q_0$ | $q_1$ | $q_3$ | No | $B_0$ | $(B_0, B_1)$ |
| $q_1$ | $q_2$ | $q_4$ | No | $B_0$ | $(B_0, B_1)$ |
| $q_2$ | $q_2$ | $q_5$ | No | $B_0$ | $(B_0, B_1)$ |
| $q_3$ | $q_1$ | $q_3$ | **Yes** | $B_1$ | $(B_0, B_1)$ |
| $q_4$ | $q_2$ | $q_4$ | **Yes** | $B_1$ | $(B_0, B_1)$ |
| $q_5$ | $q_2$ | $q_5$ | **Yes** | $B_1$ | $(B_0, B_1)$ |

- **Partition Refinement**:
  - In $\Pi_0 = \{B_0, B_1\}$ with $B_0 = \{q_0, q_1, q_2\}$ and $B_1 = \{q_3, q_4, q_5\}$, every state $u \in B_0$ has signature $(B_0, B_1)$, and every state $u \in B_1$ also has signature $(B_0, B_1)$.
  - Thus $\Pi_1 = \Pi_0$ stabilizes immediately in $1$ pass, collapsing the $6$-state inner DP down to a **2-state minimal DFA** $\{B_0, B_1\}$!

---

## 10. Phase 1.5 Curriculum Handoff Notes for Wave 4A

1. **Chapter Architecture Recommendation (`Ch 18` & `Ch 19`)**:
   - **Chapter 18 (Goulden–Jackson Cluster Method, Bivariate Occurrence GFs & Martingale PGFs on Strings)**:
     - Unify the **Goulden–Jackson Signed Cluster System** (Eq. 3.3), the **Guibas–Odlyzko Unsigned End-Tagged System** (Eq. 3.5), and **Conway's Casino Martingale / PGF System** (Eq. 5.4) via the identity $G(z) = F(z/\sigma)$ and $\Omega_{i,j} = \sigma^{|P_j|} C_{i,j}(\sigma^{-1})$.
     - Feature the **Bivariate $(t-1)$ Cluster Sieve** (Eq. 4.2), the **Exact $k$-Occurrence Rational Formula** (Eq. 4.3), the **$t = 1 + u$ Binomial Moment Shift** (Eq. 4.4), and **Non-Antichain Embedded Substring Weight Absorption** (Section 4.3).
   - **Chapter 19 (Automaton DP, `DP套DP` & Myhill–Nerode DFA Minimization)**:
     - Present the **4-Stage `DP套DP` Compiler Pipeline** (Difference/Capped State Compression $\to$ BFS Reachability $\to$ Hopcroft / Brzozowski Minimization $\to$ Outer DP / Matrix Power) alongside **Dynamic AC Binary Grouping (`二进制分组`)** and **Offline Trie $\times$ AC `fail`-Tree Euler Tour**.
2. **Verification Suite Targets (`tests/audit_strings_math.py`)**:
   - Exact rational comparison of brute-force string avoidance vs. $m \times m$ Goulden–Jackson cluster inversion,
   - Exact bivariate coefficient check of $[x^n t^k] F(x, t)$ and $[x^n u^j] F(x, 1+u)$,
   - Exact rational verification of $\mathbb{E}[T_S]$, $\text{Var}(T_S)$, and multi-player race probabilities $\pi_i$ (including seed-prefix conditioning $S_0$),
   - Automated Hopcroft vs. Brzozowski minimal DFA equivalence check on LCS and Median-Replace (`AGC 022 E`) inner automata.
