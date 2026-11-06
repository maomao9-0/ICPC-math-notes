# Wave 5B (Cohort 1 — Iterations 46–52): Combinatorics on Words (Sturmian, Morphic, Thue–Morse), Free Group / $SL_2(\mathbb{F}_p)$ Stack Hashing & Master Multilingual Audit

> [!IMPORTANT]
> **Cohort 1 Primary Discovery Report (`iter_46_to_52`)**
> This document executes **Iterations 46 through 52** of the Phase 1 Multi-Cohort Research Loop defined in [`strings_research/PLAN.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/strings_research/PLAN.md). Every structural theorem, matrix reduction, and cataloged problem enforces the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**:
> 1. **Diagnostic Signal**: Why standard whole-string structures (SAM, SA, KMP, PAM, abelian polynomial hashing) fail in time or memory.
> 2. **Combinatorial Word Invariant**: Rigorous proof of the underlying word-combinatorial property, algebraic homomorphism, or structural sparsity.
> 3. **Reverse-Engineering Scratchpad**: Step-by-step compilation into recurrences, matrix transitions, or data-structure operations with exact index boundaries.
> 4. **Boundary Pitfalls & Broken-Invariant Counterexamples**: Concrete edge cases and failure modes that break naive implementations.

---

## Iteration 46: Sturmian Words, Fibonacci Strings, Thue–Morse & Substitutive Morphisms ($\varphi : \Sigma^* \to \Sigma^*$)

### 46.1 Concrete Objects & Central Questions

Let $\Sigma$ be a finite alphabet. A **morphism** (or substitution) is a map $\varphi : \Sigma^* \to \Sigma^*$ satisfying the homomorphism law $\varphi(uv) = \varphi(u)\varphi(v)$ for all words $u, v \in \Sigma^*$, uniquely determined by the images $\varphi(c)$ of each letter $c \in \Sigma$. Iterating $\varphi$ on a seed string $S_0$ produces an exponentially growing family of strings $S_k = \varphi^k(S_0)$ (or a generalised recurrent sequence such as $S_k = S_{k-1} + t_k + S_{k-1}$ or $F_k = F_{k-1} F_{k-2}$).

Two canonical questions dominate competitive stringology on morphic and Sturmian words:
1. **Extremal Structure & Worst-Case Counterexamples**: Which infinite binary words maximize the number of runs, borders, palindromic prefixes, or Fine–Wilf periods while minimizing subword complexity?
2. **Pattern Counting & Indexing in Exponentially Long Morphic Words**: Given a seed $S_0$, a morphism $\varphi$ (or recurrence rule), an iteration depth $k \le 10^{18}$, and query patterns $P$ with $|P| \le 10^6$, how do we count occurrences of $P$ in $S_k$ (or extract $S_k[l..r]$) without materializing a string of length $|\varphi^k(S_0)| \approx \lambda^k$?

---

### 46.2 Equivalent Characterizations of Sturmian Words

For an infinite word $\mathbf{w} = w_0 w_1 w_2 \dots \in \{0, 1\}^\mathbb{N}$, define its **subword complexity function** $p_{\mathbf{w}}(n)$ as the number of distinct contiguous substrings (factors) of length $n$ occurring in $\mathbf{w}$.

#### 1. Diagnostic Signal (Why Naive Complexity Intuition Fails)
By the Morse–Hedlund Theorem (1938), if there exists any $n \ge 1$ such that $p_{\mathbf{w}}(n) \le n$, then $p_{\mathbf{w}}(m)$ cannot strictly increase for all $m \le n$, forcing $p_{\mathbf{w}}(m) = p_{\mathbf{w}}(m+1)$ for some $m \le n$. In a right-infinite word, $p_{\mathbf{w}}(m) = p_{\mathbf{w}}(m+1)$ implies that every factor of length $m$ has a unique right-extension, which forces $\mathbf{w}$ to be **ultimately periodic**. Therefore, the minimum possible subword complexity of an **aperiodic** infinite word is $p_{\mathbf{w}}(n) = n + 1$ for every $n \ge 0$. Words achieving this lower bound are called **Sturmian words**.

#### 2. Combinatorial Word Invariant (Four Equivalent Characterizations)

> **Theorem 46.1 (Coven–Hedlund / Lothaire Equivalence of Sturmian Words).**
> For a right-infinite binary word $\mathbf{w} \in \{0, 1\}^\mathbb{N}$, the following four properties are equivalent:
> 1. **Minimal Aperiodic Complexity**: $p_{\mathbf{w}}(n) = n + 1$ for all integers $n \ge 0$.
> 2. **Balancedness + Aperiodicity**: $\mathbf{w}$ is aperiodic and **1-balanced**: for every $n \ge 1$ and every pair of factors $u, v$ of $\mathbf{w}$ with $|u| = |v| = n$, their Hamming weights (counts of `1`s) differ by at most $1$:
>    $$\bigl| |u|_1 - |v|_1 \bigr| \le 1.$$
> 3. **Mechanical Irrational Rotation Words**: There exist an irrational slope $\alpha \in (0, 1) \setminus \mathbb{Q}$ and an intercept $\rho \in [0, 1)$ such that $\mathbf{w}$ is either the lower mechanical word $s_{\alpha, \rho}$ or upper mechanical word $s'_{\alpha, \rho}$:
>    $$s_{\alpha, \rho}(n) = \lfloor \alpha(n+1) + \rho \rfloor - \lfloor \alpha n + \rho \rfloor, \qquad s'_{\alpha, \rho}(n) = \lceil \alpha(n+1) + \rho \rceil - \lceil \alpha n + \rho \rceil.$$
> 4. **Unique Right-Special Factor + Palindromic Closure**: For every $n \ge 0$, $\mathbf{w}$ has **exactly one** right-special factor $u_n$ of length $n$ (a factor such that both $u_n 0$ and $u_n 1$ occur in $\mathbf{w}$). Moreover, when $\rho = 0$ (a **characteristic Sturmian word**), the reversal $u_n^R$ is the prefix of $\mathbf{w}$ of length $n$, and every central word is a palindrome.

**Proof of Core Equivalences (Double-Count & Ostrowski Geometry):**
- *$(1) \iff (4)$*: Each factor $u$ of length $n$ extends to at least one factor $u c$ of length $n+1$ ($c \in \{0,1\}$). Let $r(n)$ be the number of right-special factors of length $n$ (those extending to both $u0$ and $u1$). Counting factors of length $n+1$ by their length-$n$ prefix gives the exact identity
  $$p_{\mathbf{w}}(n+1) - p_{\mathbf{w}}(n) = r(n).$$
  Thus $p_{\mathbf{w}}(n) = n+1$ for all $n \ge 0$ if and only if $p_{\mathbf{w}}(0)=1$ and $r(n) = 1$ for every $n \ge 0$.
- *$(3) \implies (1)$ (Circle Rotation Partition)*: Under $s_{\alpha, \rho}$, a factor $u = c_0 c_1 \dots c_{n-1}$ occurs at index $i$ iff the fractional part $\{i\alpha + \rho\} \in [0, 1)$ falls in the intersection of $n$ half-open intervals determined by whether $\{ (i+j)\alpha + \rho \} \in [1-\alpha, 1)$ ($c_j = 1$) or $[0, 1-\alpha)$ ($c_j = 0$). The $n$ threshold points $\{-j\alpha \bmod 1\}_{j=1}^n$ are pairwise distinct because $\alpha \notin \mathbb{Q}$, and $n$ distinct points on the unit circle $[0, 1)$ partition it into **exactly $n+1$ half-open intervals**. By Kronecker's density theorem, the orbit $\{i\alpha + \rho \bmod 1\}_{i \ge 0}$ is dense in $[0, 1)$, so every one of the $n+1$ intervals is visited infinitely often, yielding $p_{\mathbf{w}}(n) = n+1$.
- *$(2) \iff (1)$*: If $\mathbf{w}$ were unbalanced, there would exist a minimal length $n$ with factors $0 v 0$ and $1 v 1$ for the same core $v$ of length $n-2$ (otherwise the first mismatch after a common prefix would already differ by $2$). Then $v$ is both left-special and right-special, and tracking extensions along $\mathbf{w}$ forces $p_{\mathbf{w}}(m) \ge m+2$ once both branches diverge.

---

### 46.3 Fibonacci Words, Zeckendorf Numeration & Extremal Stringology Bounds

The **Fibonacci morphism** $\varphi_F : \{a, b\}^* \to \{a, b\}^*$ is defined by
$$\varphi_F(a) = ab, \qquad \varphi_F(b) = a.$$
Setting $F_0 = b$, $F_1 = a$, and $F_k = \varphi_F^k(b) = F_{k-1} F_{k-2}$ for $k \ge 2$:

| $k$ | $|F_k| = f_k$ | $F_k$ | Factorization $F_{k-2} F_{k-3} \dots$ |
| :--- | :--- | :--- | :--- |
| $0$ | $1$ | `b` | — |
| $1$ | $1$ | `a` | — |
| $2$ | $2$ | `ab` | `a` + `b` |
| $3$ | $3$ | `aba` | `ab` + `a` |
| $4$ | $5$ | `abaab` | `aba` + `ab` |
| $5$ | $8$ | `abaababa` | `abaab` + `aba` |
| $6$ | $13$ | `abaababaabaab` | `abaababa` + `abaab` |

#### Near-Commutativity & Central Palindrome Theorem

> **Lemma 46.2 (Near-Commutativity & Central Palindrome $P_k$).**
> For every $k \ge 2$, write $F_k = P_k c_k d_k$, where $P_k$ has length $f_k - 2$ and $c_k d_k = ab$ if $k$ is even, or $ba$ if $k$ is odd. Then:
> 1. **Near-Commutativity**: $F_{k-1} F_{k-2}$ and $F_{k-2} F_{k-1}$ agree on their prefix $P_k$ of length $f_k - 2$ and differ only by swapping their last two letters ($ab \leftrightarrow ba$).
> 2. **Central Palindrome**: $P_k$ is a palindrome, and $P_k = P_{k-1} c_{k-2} d_{k-2} P_{k-2} = F_{k-2} P_{k-1}$.
> 3. **Fine–Wilf Extremality**: $P_k$ has length $f_k - 2 = f_{k-1} + f_{k-2} - \gcd(f_{k-1}, f_{k-2}) - 1$, possesses both periods $p = f_{k-1}$ and $q = f_{k-2}$ (since $P_k$ is a prefix of both $F_{k-1}F_{k-2}$ of period $f_{k-1}$ and $F_{k-2}F_{k-1}$ of period $f_{k-2}$), yet is not periodic with period $\gcd(f_{k-1}, f_{k-2}) = 1$.

**Proof by Induction on $k$:**
For $k=2$, $F_1 F_0 = ab = P_2 ab$ and $F_0 F_1 = ba = P_2 ba$ with $P_2 = \varepsilon$. For $k=3$, $F_2 F_1 = aba = P_3 ba$ and $F_1 F_2 = aab = P_3 ab$ with $P_3 = a$. Assume the claim holds up to $k$. Then for $k+1$:
$$F_k F_{k-1} = F_{k-1} F_{k-2} F_{k-1} = F_{k-1} (P_k d_k c_k),$$
whereas by inductive swap on the prefix $F_{k-1} F_{k-2}$:
$$F_{k-1} F_k = (F_{k-2} F_{k-1} \text{ with last two swapped}) \dots \implies F_k F_{k-1} = P_{k+1} c_{k+1} d_{k+1} \text{ and } F_{k-1} F_k = P_{k+1} d_{k+1} c_{k+1}.$$
Because $P_k$ is a palindrome and $F_{k-1} = P_{k-1} c_{k-1} d_{k-1} = P_{k-1} d_k c_k$, substituting gives $P_{k+1} = P_{k-1} d_k c_k P_k = P_{k-2} c_{k-2} d_{k-2} P_{k-3} d_k c_k P_k$, which reverses to itself! $\blacksquare$

#### Zeckendorf / Ostrowski Numeration Address of $\mathbf{F}[n]$
In the infinite Fibonacci word $\mathbf{F} = \lim_{k\to\infty} F_k = \text{abaababaabaab}\dots$ (0-indexed), every non-negative integer $n$ has a unique **Zeckendorf representation** $n = \sum_{i \ge 2} \epsilon_i f_i$ with $\epsilon_i \in \{0, 1\}$ and no two adjacent ones ($\epsilon_i \epsilon_{i+1} = 0$). Since $|F_k| = f_k$ and $F_k = F_{k-1} F_{k-2}$, stripping the largest Fibonacci prefix $F_k$ with $f_k \le n$ maps index $n$ to $n - f_k < f_{k-1}$ inside $F_{k-2}$. Consequently:
$$\mathbf{F}[n] = \begin{cases} a & \text{if } \epsilon_2(n) = 0, \\ b & \text{if } \epsilon_2(n) = 1. \end{cases}$$
Equivalently, $\mathbf{F}$ is the lower mechanical Sturmian word with slope $\alpha = \frac{1}{\phi^2} = \frac{3 - \sqrt{5}}{2}$ and $\rho = 0$.

#### Thue–Morse Word ($\mu(0) = 01, \mu(1) = 10$)
The **Prouhet–Thue–Morse word** $\mathbf{t} = \lim_{k\to\infty} \mu^k(0) = \text{0110100110010110}\dots$ satisfies $\mathbf{t}[n] = \text{popcount}(n) \bmod 2$.
- **Overlap-Freeness (Thue 1912)**: $\mathbf{t}$ contains **no overlap** $c u c u c$ ($c \in \{0,1\}, u \in \{0,1\}^*$) and hence no cube $w^3$ ($w \ne \varepsilon$).
- **Polynomial Hash Annihilation across $\mathbb{F}_2^k$ / $\bmod 2^{64}$**: Let $T_k = \mu^k(0)$ and $\overline{T_k} = \mu^k(1)$ of length $2^k$. For any base $B$ with $B \equiv 1 \pmod 2$, the polynomial rolling hash difference is
  $$H(T_k) - H(\overline{T_k}) = (c_0 - c_1) \prod_{j=0}^{k-1} \bigl(B^{2^j} - 1\bigr).$$
  Since $B^{2^j} - 1$ is divisible by $2^{j+2}$ for odd $B$ and $j \ge 1$, the 2-adic valuation satisfies
  $$v_2\bigl(H(T_k) - H(\overline{T_k})\bigr) \ge 1 + \sum_{j=1}^{k-1} (j+1) = \frac{k(k+1)}{2}.$$
  For $k = 11$ ($|T_{11}| = 2048$), $\frac{11 \times 12}{2} = 66 > 64$, so $H(T_{11}) \equiv H(\overline{T_{11}}) \pmod{2^{64}}$ for **every** odd base $B$!

---

### 46.4 Pattern Counting in Iterated Morphisms $\varphi^k(S_0)$ & Generalized Recurrences

#### 1. Diagnostic Signal (Why Naive String Matching Fails)
When $S_k = \varphi^k(S_0)$ or $S_k = S_{k-1} + t_k + S_{k-1}$ (`CF 1466G — Song of the Sirens`) or $F_k = F_{k-1} F_{k-2}$ (`[国家集训队论文] Fibonacci 串`), the string length grows exponentially ($|S_k| \ge 2^k$), while $|P|$ can be either small ($|P| \le 100, k \le 10^{18}$) or large ($|P| \le 10^6, k \le 10^5$). Building an automaton over $S_k$ is impossible.

#### 2. Combinatorial Word Invariant (Internal vs. Boundary-Straddling Split)

> **Theorem 46.3 (Boundary-Window Decomposition for Concatenated/Morphic Words).**
> Suppose a word $W$ is formed by concatenating two non-empty words $A$ and $B$: $W = AB$. Any occurrence of a pattern $P$ of length $m = |P| \ge 1$ in $W = A[1..|A|]B[1..|B|]$ belongs to **exactly one** of three disjoint sets by its starting position $i \in [1, |A|+|B|-m+1]$:
> 1. **Left-Internal**: $1 \le i \le |A| - m + 1$ (occurs entirely inside $A$).
> 2. **Right-Internal**: $|A| + 1 \le i \le |A| + |B| - m + 1$ (occurs entirely inside $B$).
> 3. **Boundary-Straddling**: $\max(1, |A| - m + 2) \le i \le \min(|A|, |A| + |B| - m + 1)$ (starts in $A$ and ends in $B$).
>
> Moreover, every boundary-straddling occurrence lies entirely inside the **junction window**
> $$J_{m-1}(A, B) = \text{suff}_{m-1}(A) + \text{pref}_{m-1}(B),$$
> a string of length at most $2m - 2 = 2|P| - 2$ (provided $|A|, |B| \ge m-1$). Thus:
> $$\text{occ}(P, AB) = \text{occ}(P, A) + \text{occ}(P, B) + \text{occ}\bigl(P, \text{suff}_{m-1}(A) + \text{pref}_{m-1}(B)\bigr).$$

#### 3. Reverse-Engineering Scratchpad (Two Algorithmic Regimes)

##### Regime A: Large $k \le 10^{18}$, Small $|P| = m \le 100$ (KMP Automaton Matrix Exponentiation or stabilized Junctions)
- **Method 1 (Stabilized Prefix/Suffix Junctions on $F_k = F_{k-1} F_{k-2}$)**:
  Once $f_{k-2} \ge m - 1$, $\text{pref}_{m-1}(F_k)$ is constant for all $k \ge k_0$, and $\text{suff}_{m-1}(F_k)$ is **2-periodic** in $k$ (alternating between $k$ even and $k$ odd because $F_k = F_{k-1} F_{k-2}$ ends with $F_{k-2}$). Therefore, for all $k \ge k_0 + 2$, the junction count $C_{k \bmod 2} = \text{occ}(P, \text{suff}_{m-1}(F_{k-1}) + \text{pref}_{m-1}(F_{k-2}))$ depends only on $k \bmod 2$, yielding a $4 \times 4$ linear recurrence over $2$-step blocks solvable in $O(m + \log k)$ time!
- **Method 2 (KMP Automaton Pullback $\mathcal{M}_c$ for General Morphisms $\varphi$)**:
  Build the deterministic KMP automaton for $P$ with states $0, 1, \dots, m$, where state $m$ records a match and immediately transitions as $\pi(m)$ on the next character, accumulating $+1$ to a match counter. For each character $c \in \Sigma$, represent its action as an $(m+1) \times (m+1)$ matrix $M_c$ where row $q$ has a $1$ at column $\delta(q, c)$ and a $1$ at the accumulator column $m$ if $\delta(q, c) = m$. For a morphism $\varphi$, define $M^{(r)}_c = \prod_{x \in \varphi(c)} M^{(r-1)}_x$, computable in $O(|\Sigma| m^3 \log k)$ (when $\varphi$ is uniform/matrix-exponentiable) or $O(\sum |\varphi(c)| m^3)$ per level.

##### Regime B: Large Queries $\sum |P| \le 10^6$, Moderate $k \le 10^5$ (`CF 1466G — Song of the Sirens`)
In `CF 1466G`, $s_0$ is given ($|s_0| \le 100$) and $s_{i} = s_{i-1} + t_i + s_{i-1}$ for $1 \le i \le n \le 10^5$. Given $(k, P)$ with $|P| \le 10^6$:
1. **Promote to First Sufficient Level $r_0$**: Advance $r = 0, 1, \dots$ until $|s_{r_0}| \ge |P|$ or $r_0 = k$. Since $|s_r| = 2|s_{r-1}| + 1$, it takes at most $\lceil \log_2(|P|) \rceil$ steps to reach $|s_{r_0}| \ge |P|$, and the total length satisfies $|s_{r_0}| \le 2|P| + |s_0| = O(|P| + |s_0|)$.
2. **Count at Level $r_0$**: Run KMP to find $\text{occ}(P, s_{r_0})$ in $O(|s_{r_0}| + |P|) = O(|P| + |s_0|)$ time.
3. **Invariant Stabilization for $r > r_0$**: For every $r > r_0$, $s_r = s_{r-1} + t_r + s_{r-1}$. Because $|s_{r-1}| \ge |s_{r_0}| \ge |P| > |P|-1$, the suffix $\text{suff}_{|P|-1}(s_{r-1})$ is **identical** to $U = \text{suff}_{|P|-1}(s_{r_0})$, and the prefix $\text{pref}_{|P|-1}(s_{r-1})$ is **identical** to $V = \text{pref}_{|P|-1}(s_{r_0})$ for all $r > r_0$!
4. **Closed-Form Weighted Alphabet Sum**: Each transition $s_{r-1} \to s_r$ doubles the existing internal occurrences and adds $\text{occ}(P, U + t_r + V)$. Multiplying by $2^{k-r}$ for the remaining $k-r$ doublings yields the exact formula:
   $$\text{occ}(P, s_k) = 2^{k - r_0} \text{occ}(P, s_{r_0}) + \sum_{c \in \Sigma} \text{occ}(P, U + c + V) \sum_{\substack{r = r_0 + 1 \\ t_r = c}}^{k} 2^{k - r}.$$
   By precomputing prefix sums $W[c][i] = \sum_{j=1, t_j = c}^i 2^{-j} \pmod{10^9+7}$ and computing which central positions of $U + c + V$ match $P$ via KMP/Z-algorithm on $P$ and $s_{r_0}$ in $O(|P|)$ time, each query runs in $O(|P| + |\Sigma|)$!

#### 4. Boundary Pitfalls & Broken-Invariant Counterexamples
- **Pitfall 1 (Premature Stabilization when $|A| < |P| - 1$)**: If you apply $\text{occ}(P, A c A) = 2\text{occ}(P, A) + \text{occ}(P, \text{suff}_{m-1}(A) + c + \text{pref}_{m-1}(A))$ while $|A| < m - 1$, then in $s_{r+1} = A c A c' A c A$, a single occurrence of $P$ can span **three or more** copies of $A$ and **two** pivot characters $c, c'$ simultaneously! You *must* explicitly simulate the recurrence until $|s_{r_0}| \ge |P|$.
- **Pitfall 2 ($|P| = 1$ Empty Junction Window)**: When $|P| = 1$, $m - 1 = 0$, so $U = V = \varepsilon$. In $S_k = AB$, the boundary-straddling window $J_0(A, B) = \varepsilon$ contains $0$ occurrences; in $s_r = s_{r-1} + t_r + s_{r-1}$, the window $U + t_r + V = t_r$ has length $1$ and contributes $1$ iff $P = t_r$. Failing to special-case $m - 1 = 0$ causes out-of-bounds slicing.

---

## Iteration 47: Free Group Word Reduction & Non-Abelian Matrix Hashing ($SL_2(\mathbb{F}_p)$) for Stack/Bracket Cancellation

### 47.1 Concrete Objects & Central Questions

Given an alphabet $\Sigma$, consider two fundamental stack-cancellation languages:
1. **Involutive Adjacent Cancellation (Symmetric Stack Extermination)**: Every letter $c \in \Sigma$ is its own inverse ($c^2 = \varepsilon$). Repeatedly deleting adjacent identical pairs $cc \to \varepsilon$ reduces any string $S$ to a unique reduced word $\text{red}(S)$. A substring $S[l..r]$ is **stack-exterminable** (`CF 1223F`, `ABC 295D` non-commutative variant, `AGC 050 C`) iff $\text{red}(S[l..r]) = \varepsilon$.
2. **Directed Free Group Reduction (Dyck / Bracket Cancellation)**: The alphabet is $\Sigma \sqcup \Sigma^{-1}$ where $c c^{-1} = c^{-1} c = \varepsilon$, but $c c \ne \varepsilon$.

**Central Question**: How do we test whether $\text{red}(S[l..r]) = \text{red}(T[l'..r'])$ in $O(1)$ time, count exterminable substrings in $O(N)$ or $O(N \log N)$ time, or support point updates and range cancellation queries on a Segment Tree?

---

### 47.2 The 4-Step Zero-Magic Analysis of Stack Reduction & $SL_2(\mathbb{F}_p)$ Hashing

#### 1. Diagnostic Signal (Why Abelian Polynomial / XOR Hashes Fail)
- **Why XOR / Parity Hashing Fails**: Mapping each character $c$ to a random 64-bit integer $v_c$ and computing prefix XORs satisfies $v_c \oplus v_c = 0$, so exterminable substrings have XOR $0$. However, XOR is **abelian** ($v_a \oplus v_b = v_b \oplus v_a$): the non-exterminable crossing string `abab` has prefix XOR $v_a \oplus v_b \oplus v_a \oplus v_b = 0$, producing a 100% deterministic false positive on `abab`!
- **Why Alternating-Sign Polynomial Hash $\sum (-1)^i v_{S[i]}$ Fails on `abcba`**: Alternating signs cancel adjacent pairs `(i, i+1)` and fail on `abab` (giving $2(v_a - v_b) \ne 0$), **but** any odd-length palindrome such as `aba` gives $+v_a - v_b + v_a$, and `abacaba` or `aabba` vs `abbaa` creates linear dependencies where two non-cancelling characters at the same parity offset cancel!

#### 2. Combinatorial Word Invariant (Universal Property of Free Products $\Asterisk_{c \in \Sigma} (\mathbb{Z}/2\mathbb{Z})$ and Free Groups $F_\Sigma$)

> **Theorem 47.1 (Confluent Rewriting & Prefix State Equivalence in $G = \Asterisk_{c \in \Sigma} (\mathbb{Z}/2\mathbb{Z})$).**
> The rewriting system $\mathcal{R} = \{cc \to \varepsilon : c \in \Sigma\}$ is terminating and locally confluent (by Newman's Diamond Lemma: the only critical overlap $ccc$ reduces via $(cc)c \to c$ and $c(cc) \to c$). Hence every word $w \in \Sigma^*$ has a **unique irreducible normal form** $\text{red}(w)$, which is the canonical representative of $w$ in the Coxeter group $G = \langle c \in \Sigma \mid c^2 = 1 \rangle \cong \Asterisk_{c \in \Sigma} (\mathbb{Z}/2\mathbb{Z})$.
>
> Let $P_i = \text{red}(S[1..i])$ be the reduced prefix stack after processing $S[1..i]$. Because every generator in $G$ satisfies $g^{-1} = g^R$:
> $$\text{red}(S[l..r]) = \varepsilon \iff P_{l-1}^{-1} P_r = 1_G \iff P_{l-1} = P_r.$$

Thus, counting stack-exterminable substrings $S[l..r]$ is **identical** to counting pairs $0 \le l-1 < r \le N$ that visit the **exact same vertex** in the Cayley tree of $G$!

#### 3. Reverse-Engineering Scratchpad (Two Exact / Probabilistic Compilations)

##### Compilation A: Deterministic Stack-Trie Walk (`CF 1223F — Stack Exterminable Arrays`)
When we process $S[1..N]$ sequentially from left to right:
1. Maintain the explicit Cayley tree (a Trie of irreducible words) rooted at $u_0 = \text{root}$ (representing $\varepsilon$).
2. Suppose after $S[1..i-1]$ we are at Trie node $u_{i-1}$, which was reached from its parent $\text{par}(u_{i-1})$ via edge character $\text{in\_char}(u_{i-1})$.
3. On reading $c = S[i]$:
   - **Cancellation Step**: If $u_{i-1} \ne \text{root}$ and $\text{in\_char}(u_{i-1}) = c$, the top of the stack cancels! We set $u_i = \text{par}(u_{i-1})$ in $O(1)$ time without allocating any node.
   - **Push Step**: Otherwise, we transition $u_i = \text{next}(u_{i-1}, c)$, creating a child node if absent (using a hash map or sorted map at each node when $|\Sigma| = N$).
4. Every visit to node $u_i$ increments $\text{cnt}[u_i]$ and adds the previous $\text{cnt}[u_i]$ to the answer. Total states created $\le N + 1$, running in $O(N \log |\Sigma|)$ deterministic or $O(N)$ expected time!

##### Compilation B: Non-Abelian Matrix Hashing in $GL_2(\mathbb{F}_p)$ / $SL_2(\mathbb{F}_p)$ for Range Queries & Segment Trees
When queries ask whether $\text{red}(S[l..r]) = \text{red}(T[l'..r'])$ in $O(1)$ time or under point updates in $O(\log N)$ time, we embed $G$ into $2 \times 2$ matrices over $\mathbb{F}_p$ ($p \approx 10^9+7$).
- **For Involutive Cancellation ($c^2 = \varepsilon$)**:
  Choose for each letter $c \in \Sigma$ a uniform random trace-zero matrix of determinant $-1$ in $GL_2(\mathbb{F}_p)$:
  $$M_c = \begin{pmatrix} a_c & b_c \\ d_c & -a_c \end{pmatrix} \quad \text{with} \quad a_c^2 + b_c d_c \equiv 1 \pmod p.$$
  By the Cayley–Hamilton Theorem, every $2 \times 2$ matrix satisfies $M^2 - \text{tr}(M) M + \det(M) I = 0$. Since $\text{tr}(M_c) = 0$ and $\det(M_c) = -(a_c^2 + b_c d_c) = -1$:
  $$M_c^2 = -(-1)I = I \pmod p!$$
  Moreover, to obtain determinant $+1$ in $SL_2(\mathbb{F}_{p^2})$ or $GL_2(\mathbb{F}_p)$, one only needs to select random $a_c, b_c \in \mathbb{F}_p$ with $b_c \not\equiv 0 \pmod p$ and set $d_c = (1 - a_c^2) b_c^{-1} \bmod p$. Then $M_c^{-1} = M_c$, so the prefix product $H_i = M_{S[1]} M_{S[2]} \cdots M_{S[i]}$ satisfies:
  $$H(S[l..r]) = H_{l-1}^{-1} H_r = \bigl(\underbrace{M_{S[l-1]} \cdots M_{S[1]}}_{\text{reverse prefix}}\bigr) (M_{S[1]} \cdots M_{S[r]}).$$
- **For Directed Free Group / Bracket Cancellation ($c c^{-1} = \varepsilon$, $c^2 \ne \varepsilon$)**:
  Map opening character $c$ to a random matrix $M_c \in SL_2(\mathbb{F}_p)$ ($\det(M_c) = 1$) and its closing counterpart $\bar{c}$ to the exact matrix inverse:
  $$M_{\bar{c}} = M_c^{-1} = \begin{pmatrix} d_c & -b_c \\ -c_c & a_c \end{pmatrix} \pmod p.$$
  By Sanov's Theorem and the Schwartz–Zippel lemma on generic matrix rings, any non-empty reduced word $w \in F_\Sigma \setminus \{\varepsilon\}$ of length $L \le N$ evaluates to $I_2$ with probability at most $\frac{L}{p}$!

#### Hand-Checkable Example (`abab` vs `abba` over $\mathbb{F}_7$)
Let $p = 7$. Pick two involutory matrices ($\text{tr} = 0, \det = -1 \equiv 6 \pmod 7$):
$$M_a = \begin{pmatrix} 1 & 2 \\ 0 & 6 \end{pmatrix} \implies M_a^2 = \begin{pmatrix} 1 & 14 \\ 0 & 36 \end{pmatrix} \equiv \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \pmod 7,$$
$$M_b = \begin{pmatrix} 2 & 1 \\ 4 & 5 \end{pmatrix} \implies M_b^2 = \begin{pmatrix} 8 & 7 \\ 28 & 29 \end{pmatrix} \equiv \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \pmod 7.$$
- On the exterminable string `abba`:
  $$M_a M_b M_b M_a = M_a (M_b^2) M_a = M_a I M_a = M_a^2 = I.$$
- On the non-exterminable string `abab`:
  $$M_a M_b = \begin{pmatrix} 1 & 2 \\ 0 & 6 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 4 & 5 \end{pmatrix} = \begin{pmatrix} 10 & 11 \\ 24 & 30 \end{pmatrix} \equiv \begin{pmatrix} 3 & 4 \\ 3 & 2 \end{pmatrix} \pmod 7,$$
  $$(M_a M_b)^2 = \begin{pmatrix} 3 & 4 \\ 3 & 2 \end{pmatrix}^2 = \begin{pmatrix} 21 & 20 \\ 15 & 16 \end{pmatrix} \equiv \begin{pmatrix} 0 & 6 \\ 1 & 2 \end{pmatrix} \ne I \pmod 7!$$
Unlike XOR, non-commutativity $M_a M_b \ne M_b M_a$ immediately separates `abab` from `abba`!

#### 4. Boundary Pitfalls & Broken-Invariant Counterexamples
- **Pitfall 1 (Unidirectional Bracket Matching vs. Free Group Cancellation)**: In standard valid parentheses (`()`), `) (` does **not** reduce to $\varepsilon$, whereas in $SL_2(\mathbb{F}_p)$ free-group hashing, $M_{c}^{-1} M_c = I$ *does* cancel `) (`! To test *valid bracket strings* (Dyck language, where prefix depth never drops below $0$ and types match), you must either:
  1. Combine $SL_2(\mathbb{F}_p)$ hash equality $H_{l-1} = H_r$ (which verifies that every matched pair has the right bracket type) with a 1D range-minimum query $\min_{l \le i \le r} \text{depth}[i] \ge \text{depth}[l-1]$ (which forbids `) (` cancellation), OR
  2. Use Segment Tree Monoid Reduction storing `(unmatched_close_hash, unmatched_open_hash)` per node (`O(log^2 N)` per query).
- **Pitfall 2 (Dihedral Group $D_n$ Trap when Choosing Special Matrices)**: If you pick $M_c$ from a commutative or small finite subgroup (e.g., permutation matrices or diagonal/anti-diagonal matrices where $(M_a M_b)^2 = I$), then `abab` still collides with $\varepsilon$! Always choose $a_c, b_c$ uniformly at random from $\mathbb{F}_p$ with $b_c \ne 0$.

---

## Iteration 48: Obscure & Frontier Stringology Hunt

Per Section 4 of [`PLAN.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/strings_research/PLAN.md), this iteration hunts down **six frontier stringology paradigms** from theoretical computer science and modern grandmaster contests (Universal Cup, QOJ, POI, ICALP/SODA/STOC papers by Kempa, Kociumaka, Park, Amir, and Gawrychowski) that lie outside Waves 1A–5A.

### 48.1 String Attractors ($\gamma(S)$ — Kempa & Prezza, STOC 2018)
- **Concrete Object**: A set of positions $\Gamma \subseteq \{1, \dots, |S|\}$ is a **string attractor** of $S$ if every distinct contiguous substring $S[l..r]$ has at least one occurrence $S[l'..r'] = S[l..r]$ that crosses a position in $\Gamma$ (i.e., $\Gamma \cap [l', r'] \ne \emptyset$). The minimum size of a string attractor is denoted $\gamma(S)$.
- **Combinatorial Invariant**:
  1. Every dictionary compressor (LZ77 phrases $z$, BWT runs $r$, Straight-Line Program size $g$, CDAWG size $e$) induces a string attractor of size $O(\text{compressed size})$, so $\gamma(S) \le \min(z, r, g, e)$.
  2. For **Sturmian words**, $\gamma(S) = 2$: the last two positions of the prefix of length $f_k$ (or the positions straddling the unique right-special factor boundary) suffice to capture every factor!
  3. For **Thue–Morse words** $T_k$, $\gamma(T_k) = 4$ (Kutsukake et al. 2020).
- **Competitive Programming Relevance**: Whenever a problem asks for the minimum number of "checkpoint indices" such that every distinct substring of $S$ covers at least one checkpoint, or asks to index all distinct substrings around $O(z)$ LZ77 phrase boundaries, it is querying a string attractor.

### 48.2 $\tau$-Synchronizing Sets & Locally Consistent Anchors (Kempa & Kociumaka, STOC 2019)
- **Concrete Object**: Given a parameter $\tau \ge 1$, a subset of positions $\mathsf{S} \subseteq [1, n - 2\tau + 1]$ is a **$\tau$-synchronizing set** of $S$ if:
  1. **Local Consistency**: Whether $i \in \mathsf{S}$ depends *only* on the length-$2\tau$ substring $S[i .. i + 2\tau - 1]$ (i.e., $S[i..i+2\tau-1] = S[j..j+2\tau-1] \implies (i \in \mathsf{S} \iff j \in \mathsf{S})$).
  2. **Density / Coverage**: For every $i \in [1, n - 3\tau + 2]$, if the window $S[i .. i + 3\tau - 2]$ is **not** periodic with minimal period $\le \tau/3$, then $\mathsf{S} \cap [i, i + \tau] \ne \emptyset$.
  3. **Sparsity**: $|\mathsf{S}| = O(n / \tau)$.
- **Reverse-Engineering Construction (Smallest-Minimizer Rule)**:
  Assign each length-$\tau$ factor $S[k .. k+\tau-1]$ a deterministic identifier (its lexicographical rank or collision-free Karp–Rabin hash). Put $i \in \mathsf{S}$ iff $\min_{k \in [i, i+\tau]} \text{id}(S[k..k+\tau-1])$ is achieved at $k = i$ or $k = i + \tau$. In the non-periodic regime, sliding a window of width $\tau+1$ over $\text{id}$ values forces a local minimum at least once every $\tau$ steps; in the periodic regime (runs of period $p \le \tau/3$), one handles the run boundary explicitly!
- **Why It Matters**: Replaces $O(\log N)$-level randomized/deterministic Locally Consistent Parsing (SLP) with a **single-level $O(N/\tau)$ anchor set**, enabling $O(1)$ LCE in $O(N / \log_\Sigma N)$ space and optimal substring hashing.

### 48.3 Cartesian-Tree Pattern Matching (Park, Amir, Landau, Kunisada, SPIRE 2019 / `QOJ` / `POI`)
- **Concrete Object**: Two numeric arrays $A[1..m]$ and $B[1..m]$ are **Cartesian-tree isomorphic** ($A \approx_{\text{CT}} B$) iff they have the exact same Cartesian tree shape (assuming min-heap with leftmost-minimum tie-breaking).
- **Diagnostic Signal**: Unlike order-isomorphic matching (which requires all $m$ relative ranks to match and uses Fenwick KMP in $O(N \log m)$), Cartesian-tree isomorphism only requires every index $i$ to have the **same parent in the Cartesian tree**!
- **Combinatorial Invariant (Parent-Distance Encoding $\text{PD}_S$)**:
  For an array $S[1..m]$, build its Cartesian tree incrementally from left to right using a monotonic stack. When inserting $S[i]$, let $L(i) < i$ be the nearest index to the left with $S[L(i)] \le S[i]$, and let $C(i) < i$ be the last element popped from the monotonic stack (which becomes the left child of $i$ in the Cartesian tree). Define the **Parent-Distance encoding** $\text{PD}_S[1..m]$ by:
  $$\text{PD}_S[i] = \bigl(i - L(i),\; i - C(i)\bigr) \quad (\text{recording } 0 \text{ if } L(i) \text{ or } C(i) \text{ does not exist}).$$
  Because adding $S[i]$ at the right end of $S[1..i-1]$ only inspects elements on the rightmost spine of the Cartesian tree of $S[1..i-1]$, $A[1..m] \approx_{\text{CT}} B[1..m] \iff \text{PD}_A[1..m] = \text{PD}_B[1..m]$!
- **KMP Automaton in $O(N)$ Time**: Unlike order-preserving matching (which requires a Fenwick tree to test rank equality), advancing the monotonic stack by one element $T[r]$ and checking whether $(r - L_{\ge l}(r), r - C_{\ge l}(r)) = \text{PD}_P[q+1]$ (clipping indices $< l$ to $0$) runs in **amortized $O(1)$ time per step** using a deque-monotonic stack!

### 48.4 Weighted / Position-Weight Strings (PWM) & $1/z$-Threshold Suffix Trees
- **Concrete Object**: A **Weighted String** (or Position Weight Matrix, PWM) of length $n$ specifies at each index $i$ a probability distribution $\pi_i : \Sigma \to [0, 1]$ with $\sum_{c \in \Sigma} \pi_i(c) = 1$. Given a threshold $1/z \in (0, 1]$, a solid string $P[1..m]$ occurs at position $i$ with probability $\prod_{j=1}^m \pi_{i+j-1}(P[j]) \ge 1/z$.
- **Combinatorial Sparsity Theorem (Barton, Kociumaka, Pissis, Radoszewski, STOC 2016)**:
  Although a weighted string of length $n$ generates $|\Sigma|^n$ possible solid strings, at most $\lfloor z \rfloor$ maximal solid factors starting at any given position can have probability $\ge 1/z$ (because the probabilities of pairwise diverging solid continuations from any prefix are disjoint events in the product space $\Sigma^n$, so their sum is $\le 1$!).
- **Algorithmic Compilation**: Every weighted string of length $n$ with threshold $1/z$ can be covered by a family of $\lfloor z \rfloor$ solid strings of total length $O(nz)$ (the **Weighted Suffix Tree**), built in $O(nz)$ time via Heavy-Light probability branching, answering pattern matching in $O(|P| + \text{occ})$ time!

### 48.5 2D Periodicity & Lattice Classification (Amir & Benson, SICOMP 1998)
- **Concrete Object**: For a 2D array $M[1..R][1..C]$, a vector $\mathbf{v} = (dr, dc) \in \mathbb{Z}^2$ is a **2D period vector** if $M[r][c] = M[r+dr][c+dc]$ whenever both cells lie inside $[1..R] \times [1..C]$.
- **Four-Class Taxonomy of 2D Periodicity**:
  Looking at period vectors inside the central quarter $[0, R/2] \times [-C/2, C/2]$, the set of valid period vectors falls into **4 structural classes**:
  1. **Non-Periodic**: Only $(0, 0)$ is a period vector.
  2. **1D Line-Periodic**: All period vectors lie on a single ray (rational slope $dr/dc$), generated by one primitive vector $\mathbf{v}_1$ plus possibly non-lattice edge-hugging vectors near the corners.
  3. **2D Radiant-Periodic**: Period vectors lie on multiple rays because small corner overlaps do not interact.
  4. **2D Lattice-Periodic**: Period vectors form a 2D Euclidean lattice $\mathbb{Z}\mathbf{v}_1 \oplus \mathbb{Z}\mathbf{v}_2$ generated by two linearly independent vectors $\mathbf{v}_1, \mathbf{v}_2$.
- **Competitive Reduction**: 2D pattern matching reduces to 1D AC Automaton (selecting distinct rows of $P$ as patterns and running KMP on the sequence of row IDs) in $O(RC)$ time (Baker–Bird algorithm).

### 48.6 LZ77 / Grammar-Compressed Indexing (Claude & Navarro / Christiansen et al.)
- **Concrete Object**: Given an LZ77 factorization $S = F_1 F_2 \dots F_z$ into $z$ phrases (or an SLP of $g$ rules), count/locate all occurrences of $P$ in $S$ in $O(|P|^2 + \text{occ})$ or $O(|P| \log N + \text{occ})$ time without decompressing $S$.
- **Combinatorial Invariant (Primary vs. Secondary Occurrences)**:
  1. **Primary Occurrences**: Occurrences of $P$ that **cross at least one LZ77 phrase boundary** (or touch the explicit split point of the lowest SLP non-terminal $X \to AB$ containing $P$). Because each phrase boundary can be straddled by at most $|P|-1$ alignments, there are at most $z(|P|-1)$ (or $g(|P|-1)$) primary anchor pairs!
  2. **Secondary Occurrences**: Occurrences contained strictly inside a single phrase $F_k = S[\text{src}_k .. \text{src}_k + \ell_k - 1]$ (or copied non-terminal). Every secondary occurrence is a **copied image** of a primary occurrence from its source interval $[\text{src}_k, \text{src}_k + \ell_k - 1]$, enumerable via 2D orthogonal range reporting on phrase source intervals!

---

## Iteration 49: `[ZH]` Master Audit (Chinese National Team Papers `国家集训队论文`, NOI/WC/CTSC/ZJOI/SDOI/BJWC/THUPC, UOJ/LOJ/QOJ)

This iteration conducts an exhaustive audit of the Chinese competitive-programming stringology corpus to verify that no advanced theorem, data-structure coupling, or National Team treatise is missed across Waves 1A–5B.

### 49.1 Master Inventory of Chinese National Team Papers (`IOI 中国国家候选队论文集`)

| Year & Author | Chinese Title & English Translation | Core Structural Invariants & Algorithms Introduced | Target Textbook Coverage |
| :--- | :--- | :--- | :--- |
| **2004 — 许智磊 (Xu Zhilei)** | 《后缀数组》 (*Suffix Arrays*) | Doubling $O(N \log N)$ SA, Kasai's $O(N)$ `height` array via $h[i] \ge h[i-1]-1$, monotonic stack / binary search over LCP intervals. | Assumed Prerequisite / Part III (`Ch 12`) |
| **2009 — 罗穗骞 (Luo Suiqian)** | 《后缀数组——处理字符串的有力工具》 (*Suffix Array: A Powerful Tool for String Processing*) | Taxonomizes 12 SA paradigms: non-overlapping repeats, lexicographical $k$-th substring, $O(1)$ LCE + harmonic series enumeration of periodic runs ($O(N \log N)$ block placement at multiples of $L$). | Part II (`Ch 08`) & Part IV (`Ch 13`) |
| **2012 — 陈立杰 (Chen Lijie / WJMZBMR)** | 《后缀自动机》(Noi/WC Lecture Notes & Treatise) | Formalizes $\text{endpos}$ equivalence classes, Link Tree (`parent` tree), why $|V| \le 2N-1$ and $|E| \le 3N-4$, and right-extension state splitting. | Part III (`Ch 09`) |
| **2014 — 徐毅 (Xu Yi)** | 《浅谈回文子串问题》 (*On Palindromic Substring Problems*) | Introduces Palindromic Tree (PAM / Eertree) to China; proves the $O(\log N)$ arithmetic progression structure of palindromic suffixes (`slink` / `diff`); offline & online range distinct palindrome queries on $S[l..r]$ via periodic occurrence jumps; double-ended PAM. | Part I (`Ch 04`) & Part IV (`Ch 15`–`Ch 16`) |
| **2015 — 张天扬 (Zhang Tianyang)** | 《后缀自动机及其应用》 (*Suffix Automaton and Its Applications*) | Generalized SAM (`广义 SAM`) on Tries vs. multiple strings; SAM + LCT `access` for online $\text{endpos}$ size maintenance; SAM + Segment Tree Merge (`线段树合并维护 Endpos`). | Part III (`Ch 09`–`Ch 11`) |
| **2017 — 钟知闲 (Zhong Zhixian)** | 《回文树及其应用》 (*Palindromic Tree and Its Applications*) | Rigorous proof of PAM `slink` DP (`CF 932G` / `CF 906E`), Persistent PAM on trees (`quick_link` elimination of amortized fail walks), and minimum palindrome partition with parity constraints. | Part I (`Ch 04`) & Part IV (`Ch 15`) |
| **2018 — 洪华敦 (Hong Huadun)** | 《浅谈字符串周期与 Border 理论》 / WC Lectures | Weak Periodicity Lemma, $O(\log N)$ border AP blocks, `[WC2016] 论战捆竹竿` residue-class knapsack with monotonic queues, and `[BJWC2018] Border 的四种求法` internal border queries via 2D IPM + AP blocks. | Part I (`Ch 01`–`Ch 03`) & Part IV (`Ch 14`) |
| **2019 — 金策 (Jin Ce)** | 《字符串算法选讲》 (*Selected Topics in String Algorithms*) | **Landmark Treatise**: Complete elementary proofs of Chen–Fox–Lyndon, **Significant Suffixes (`显著后缀`) Theorem** ($O(\log N)$ candidate suffixes for `[ZJOI2017] 字符串`), Lyndon Tree construction from ISA + Cartesian Tree, and **Bannai et al.'s Runs Theorem** ($< N$ runs, $\sum \text{exp} < 3N$). | Part II (`Ch 05`–`Ch 08`) |
| **2020 — 国家集训队论文 (Fibonacci & Sturmian Words)** | 《Fibonacci 串与 Sturmian 串的性质及应用》 | Zeckendorf representation of Fibonacci strings, near-commutativity $F_{k-1}F_{k-2}$ vs $F_{k-2}F_{k-1}$, why Fibonacci strings maximize Runs and PAM `fail` chain depth, and subword complexity $p(n) = n+1$. | Part I (`Ch 01`) & Part VI (`Ch 24`) |
| **2021 — 刘雨辰 / 集训队论文 (Unit-Monge & Seaweed Matrices)** | 《浅谈单位蒙日矩阵乘法及其在字符串问题中的应用》 (*Unit-Monge Matrix Multiplication and Applications to Strings*) | **Tiskin's Seaweed Matrices (`海草矩阵`)**: Proves the Monge property of the alignment grid DAG, cross-difference permutation matrix representation, $O(N \log^2 N)$ Unit-Monge distance product via divide-and-conquer, and all-pairs interval LCS (`[THUPC 2021] 区间 LCS`). | Part V (`Ch 20`) |
| **2022–2024 — 集训队论文 (IPM, GSAM Pitfalls & Lyndon/Runs Extensions)** | 《广义后缀自动机与基本子串字典》 (*Generalized SAM and Basic Substring Dictionary*) | Exposes the online Generalized SAM zero-length clone bug; unifies Kociumaka's Basic Substring Dictionary (IPM) with Wavelet Trees / Persistent Segment Trees and Tree Suffix Structures. | Part III (`Ch 09`) & Part IV (`Ch 13`–`Ch 14`) |

### 49.2 Complete `[ZH]` Contest & Judge Audit Matrix (`NOI` / `WC` / `CTSC` / `ZJOI` / `SDOI` / `BJWC` / `THUPC` / `UOJ` / `LOJ` / `QOJ`)

1. **Periodicity, Border APs & `slink` DP**:
   - `[WC2016] 论战捆竹竿` (Luogu P4156 / LOJ 2087): Border APs + modulo shortest path with monotonic queue in $O(N \log N)$.
   - `[SDOI2019] 连续子序列` (Luogu P5362): Thue–Morse / morphic string reconstruction + `slink`/automaton DP.
   - `[BJWC2018] Border 的四种求法` (Luogu P4482 / LOJ 2542): Internal border queries on $S[l..r]$ via $\log N$ length-doubling buckets + IPM + AP intersection.
2. **Lyndon, Significant Suffixes & Runs**:
   - `[ZJOI2017] 字符串` (Luogu P3763 / LOJ 2249): Dynamic block additions + Significant Suffixes ($O(\log N)$ candidates per block) for range minimum suffix.
   - `[NOI2016] 优秀的拆分` (Luogu P1117 / UOJ 219): LCE harmonic-series block placement / Runs difference array for counting $AABB$.
   - `[THUPC 2019 / LOJ / QOJ] Runs`: Enumerating runs + 2D orthogonal sweep-line over run intervals for distinct square substring range queries.
3. **SAM, GSAM, Endpos Merge & LCT**:
   - `[NOI2018] 你的名字` (Luogu P4770 / LOJ 2720): SAM of $S$ + Segment Tree Merge on $\text{endpos}$ + SAM of query $T$ with $[l + \text{len} - 1, r]$ clipping.
   - `[HEOI2016 / TJOI2016] 字符串` (Luogu P4094): Binary search + Link-Tree binary lifting + Segment Tree Merge on $\text{endpos}$.
   - `[十二省联考 2019] 字符串问题` (Luogu P5284 / LOJ 3052): SAM Link Tree prefix-optimised DAG + longest path.
   - `[SDOI2017] 相关分析 / 树点涂色` & `[BZOJ 2555] SubString`: Dynamic SAM + LCT `access` color-chain sweeping for online occurrences / offline range distinct substrings.
   - `[ZJOI2015] 诸神眷顾的幻想乡` (Luogu P3346): Leaf-rooted Trie ($\le 20$ leaves) + Generalized SAM for distinct path substrings on a tree.
4. **Virtual Suffix Trees, Goulden–Jackson, DASG & Seaweed Matrices**:
   - `[NOI2015] 品酒大会` (Luogu P2178 / UOJ 131) & `[AHOI2013] 差异` (Luogu P4248): Suffix Tree / Cartesian Tree on `height` + DSU aggregation.
   - `[CTSC2006] 歌唱王国` (Luogu P4548), `[SDOI2017] 硬币游戏` (Luogu P3706), `[JSOI2009] 有趣的游戏` (Luogu P3193): Goulden–Jackson cluster / Conway's martingale PGFs.
   - `[HEOI2015] 最短不公共子串` (Luogu P4112): Product automata coupling SAM and Subsequence Automaton (DASG) across 4 combinations.
   - `[THUPC 2021] 区间 LCS` (LOJ 3516 / QOJ): Tiskin's Seaweed Matrix + 2D Dominance Queries for all-pairs interval $\text{LCS}(A, B[l..r])$.
   - `[SCOI2016] 萌萌哒` (Luogu P3295): Binary-Lifting DSU (`倍增并查集`) for $M$ interval equality constraints.

---

## Iteration 50: `[JA]` Master Audit (AtCoder `AGC`/`ARC`/`ABC`, JOI, yukicoder & Japanese Stringology Treatises)

This iteration audits the Japanese competitive-programming stringology ecosystem—spanning AtCoder Grand/Regular/Beginner Contests (`AGC`/`ARC`/`ABC`), the Japanese Olympiad in Informatics (`JOI` Spring Camp / Open), `yukicoder`, and technical treatises by `noshi91`, `maspypy`, `tatyam`, `snuke`, `Nyaan`, and `henkoku`.

### 50.1 Master Inventory of Japanese Technical Treatises & Blogs

| Author / Handle | Key Treatises & Algorithmic Contributions | Core Structural Invariants Explained | Target Textbook Coverage |
| :--- | :--- | :--- | :--- |
| **`noshi91`** | 1. *Palindromic Tree の DP 高速化 (`slink` DP)*<br>2. *非可換ハッシュと自由群・括弧列判定 ($SL_2(\mathbb{F}_p)$ Matrix Hash)*<br>3. *Lempel-Ziv / 文法圧縮と局所一意分割 (Block Compression / Synchronizing Sets)* | 1. Proves why PAM `slink` shifts cover all but one palindromic transition at $r - \text{len}(\text{slink}(u))$.<br>2. Constructs explicit involutory and free-group $2 \times 2$ matrices over $\mathbb{F}_p$ for stack-exterminable and Dyck queries.<br>3. Deterministic $O(\log N)$ coin-tossing / 3-coloring block compression for dynamic string LCE. | Part I (`Ch 04`), Part VI (`Ch 23`) |
| **`maspypy`** | 1. *Subsequence DP と逆行列による区間部分列数え上げ (`序列自动机 + 矩阵求逆`)*<br>2. *Lyndon 分解・Runs 列挙の実装と数理*<br>3. *DP on Automaton (DFA 最小化と DP套DP)* | 1. Shows that the $(|\Sigma|+1)\times(|\Sigma|+1)$ transition matrix for distinct subsequences is an elementary matrix whose inverse costs $O(1)$ per step (`ABC 214F` range extension).<br>2. Connects Duval's algorithm, Lyndon trees, and Runs enumeration.<br>3. Systematic Nerode state minimization for counting strings with complex subsequence/substring properties. | Part II (`Ch 05`–`Ch 08`), Part V (`Ch 19`) |
| **`henkoku`** | 1. *Tiskin's Seaweed Matrix (Unit-Monge 行列積と全区間 LCS)*<br>2. *Weighted / Cartesian String Matching & Internal Queries* | 1. Visualizes Tiskin's seaweed combing rule: two crossing seaweeds swap only if they have not previously crossed and meet at a mismatch cell ($A[i] \ne B[j]$).<br>2. Recursive Russo–Tiskin $O(N \log^2 N)$ Unit-Monge distance multiplication. | Part V (`Ch 20`) |
| **`tatyam` & `Nyaan`** | 1. *SA-IS (Induced Sorting) の完全理解と実装*<br>2. *Wildcard Pattern Matching & Bit-Parallel Myers LCS*<br>3. *Double-Ended Palindromic Tree (`双向 PAM`)* | 1. Step-by-step invariant of L-type/S-type/LMS classification and why two induced-sort passes sort all suffixes.<br>2. $64$-bit word-parallel LCS (`Delta DP` subtraction carry) and 3-FFT Clifford–Clifford wildcard matching.<br>3. Deque PAM using `quick_link` + surface palindrome counts. | Part III (`Ch 12`), Part IV (`Ch 15`), Part V (`Ch 17`, `Ch 20`) |
| **`snuke`** | *AtCoder Grand Contest (`AGC`) Editorial Canon on String Rewriting, Invariants & Free-Group Games* | Classification of string rewriting games and reachability (`AGC 050 C`, `AGC 027 F`, `AGC 047 B`, `AGC 048 D`, `AGC 060 C/D`) via homomorphic group invariants, run-length compressions, and backwards Trie suffixes. | Part VI (`Ch 21`, `Ch 23`, `Ch 24`) |

### 50.2 Complete `[JA]` Contest Audit (`AGC` / `ARC` / `ABC` / `JOI` / `yukicoder`)

1. **Free-Group / Stack Cancellation, Rewriting Systems & Homomorphic Invariants**:
   - `AGC 050 C — Block Game`: Rewriting / block-merging game on strings reduced to a logarithmic horizon of active boundaries (at most $\lceil \log_2 N \rceil \le 21$ moves before survival is guaranteed).
   - `ARC 119 E — Pancakes` / `ABC 295 D` / `yukicoder` Stack-Cancellation variants: Contrasting abelian parity masks ($2^{|\Sigma|}$ states when permutation is allowed) against non-abelian $SL_2(\mathbb{F}_p)$ / Stack-Trie walks when adjacent order matters.
   - `AGC 013 E — Placing Squares` & `AGC 004 D` / `ARC 150 D`: Matrix monoid compositions over combinatorially interpreted string/segment states.
   - `ARC 140 D` / `AGC 031 D — A Sequence of Permutations`: Commutator word exponentiation $f_n = f_{n-1} f_{n-2}^{-1} = p^q G p^{-q}$ in non-abelian symmetric groups ($S_N$ word equations).
2. **Lexicographical Greedies, Lyndon Words & Palindrome Structures**:
   - `AGC 047 B — First Second`: Backwards Trie + character presence bitmask for counting pairs where $S_i$ matches $S_j$ after deleting one of the first two characters.
   - `AGC 022 E — Median Replace`: 3-state minimal DFA (`DP套DP`) for ternary majority reduction `000 -> 0`, `111 -> 1`, `010 -> 0`.
   - `ABC 214 F — Substrings` & Range Extensions: Subsequence Automaton (DASG) DP and its $(|\Sigma|+1)\times(|\Sigma|+1)$ invertible matrix generalization.
   - `ABC 272 G` / `ABC 284 F` / `ABC 313 G` / `ARC 151 D`: Floor-sum / Ostrowski mechanical words (`ABC 313 G` connects directly to Sturmian mechanical sum counts!) and Z/KMP/Hash structural inversions.
   - `JOI Spring Camp (JOISC)` String Classics: `JOISC 2017 — Long Mansion`, `JOISC 2019 — Naan / Bitaro`, `JOISC 2022 — Copy and Paste 3` (Interval DP on string repeats via harmonic/LCE transitions).

---

## Iteration 51: `[EN]` Master Audit (Codeforces Div1 D–F, ICPC WF/Regionals, Universal Cup, POI & Academic Canon)

This iteration audits the English-language competitive and academic stringology corpus to verify complete coverage of Western/Eastern European Olympiads (`POI`, `CEOI`, `BOI`, `IOI`), `Codeforces` Div1 D–F, `ICPC World Finals` / Regionals, `Universal Cup`, and foundational theoretical stringology papers.

### 51.1 Academic Competitive-Stringology Canon

| Authors & Venue | Seminal Work | Core Structural Theorems & Algorithmic Compilations |
| :--- | :--- | :--- |
| **Lothaire (1983, 2002, 2005)** | *Combinatorics on Words* / *Algebraic Combinatorics on Words* / *Applied Combinatorics on Words* | Fine–Wilf Theorem, Chen–Fox–Lyndon Theorem, Sturmian Words (Coven–Hedlund theorem, mechanical words, Ostrowski numeration), Thue–Morse overlap-freeness. |
| **Crochemore & Rytter (1994, 2002)** | *Text Algorithms* / *Jewels of Stringology* | Weak Periodicity Lemma, Three-Squares Lemma, DAWG / Suffix Automaton duality, Two-Way string matching (Constant-Space Critical Factorization Theorem). |
| **Goulden & Jackson (1979)** | *An Inversion Theorem for Cluster Decompositions of Sequences with Distinguished Subsequences* | Inclusion–exclusion over overlapping forbidden pattern clusters; reduces $O(\sum |P_i|)$ Aho–Corasick states to an $m \times m$ correlation polynomial linear system. |
| **Mehlhorn, Sundar, Uhrig (1997) & Gawrychowski (2011–2019)** | *Maintaining Dynamic Sequences under Equality Tests* / *Pattern Matching in Lempel–Ziv & SLP Compressed Strings* | Locally Consistent Parsing ($O(\log N)$ balanced SLP hierarchy supporting split/concat/LCE) and $O(|P| + \log N)$ pattern matching in compressed strings. |
| **Tiskin (2008, 2013, 2015)** | *Semi-Local String Comparison: Algorithmic Techniques and Applications* | **Seaweed Matrices**: Proves that the boundary distances of the alignment grid DAG form a Unit-Monge matrix whose cross-difference is a permutation matrix composable in $O(N \log N)$. |
| **Rubinchik & Shur (2015, 2018)** | *EERTREE: An Efficient Data Structure for Processing Palindromes in Strings* | Formalizes Palindromic Tree (PAM), `slink` / `diff` series links for $O(N \log N)$ palindrome partition DP, rich words, and joint/persistent eertrees. |
| **Bannai, I, Inenaga, Nakashima, Takeda, Tsuruta (2017)** | *The "Runs" Theorem* (*SIAM J. Comput.*) | Assigns every run $R = [l, r, p]$ a unique Lyndon root under either $<$ or $>$ alphabet order, proving $\text{runs}(N) < N$ and $\sum \text{exp}(R) < 3N$ in 5 pages. |
| **Kociumaka, Radoszewski, Rytter, Waleń (2014–2024)** | *Internal Pattern Matching (IPM) in Text & The Basic Substring Dictionary* (*SODA / SICOMP*) | Answers internal pattern matching ($|v| \le 2|u|$ yields $\le 2$ arithmetic progressions of occurrences), internal borders, substring rank, and minimal cyclic shift of $S[l..r]$ in $O(1)$ or $O(\log N)$ time. |
| **Kempa & Prezza (2018); Kempa & Kociumaka (2019)** | *At the Roots of Dictionary Compression: String Attractors* (*STOC 2018*); *String Synchronizing Sets* (*STOC 2019*) | Unifies dictionary compressors under string attractors $\gamma(S)$ and replaces multi-level SLP parsing with single-level $O(N/\tau)$ locally consistent $\tau$-synchronizing sets. |

### 51.2 Complete `[EN]` Contest Audit (`Codeforces` Div1, `ICPC WF`, `Universal Cup`, `POI`)

1. **Wave 1A–1B (Periodicity, `slink` DP, Lyndon & Runs)**:
   - `CF 932G — Palindrome Partition` & `CF 906E — Reverses`: Interleaving $S_1 S_n S_2 S_{n-1}\dots$ to reduce symmetric even block partitions to even-length palindrome partition via PAM `slink` DP.
   - `CF 1286E — Fedya the Potter Strikes Back`: Online KMP border maintenance + `slink` skipping + monotonic stack minimum query with $128$-bit rolling answer.
   - `POI XII — Template (Szablon)` & `POI XIII — Periods (Okresy)`: KMP Link-Tree DP and shortest-border propagation.
2. **Wave 2A–2B (SAM, Endpos Merge, Virtual Suffix Tree & IPM)**:
   - `CF 666E — Forensic Examination`, `CF 700E — Cool Slogans`, `CF 1037H — Security`, `CF 1063F — String Journey`: Canonical SAM + Segment Tree Merge on $\text{endpos}$ + Link-Tree binary lifting suite.
   - `CF 873F — Forbidden Indices`, `CF 802I — Fake News (hard)`, `CF 235C — Cyclical Quest`: Virtual Suffix Tree / SAM Link-Tree aggregation and cyclic shift walks on SAM.
3. **Wave 3B–4B (FFT Matching, Goulden–Jackson, Subsequence Matrices & Seaweed)**:
   - `CF 528D — Fuzzy Search`, `CF 827E — Rusty String`, `CF 1334G — Substring Search`: FFT threshold expansion, wildcard difference convolution ($a-b$ index differences), and involution-constrained polynomial matching.
   - `CF 1017G / CF 750E — New Year and Old Subsequence` & `Universal Cup` Range Subsequence sets: $(|\Sigma|+1)\times(|\Sigma|+1)$ tropical/linear subsequence matrices.
   - `Universal Cup` / `ICPC WF` Seaweed & Goulden–Jackson problems: `ICPC WF 2017 — Son of Pipe Stream / Tarot Sham Bo` (overlap autocorrelation polynomials).
4. **Wave 5A–5B (Morphic Words, Free-Group Hashing, Word Equations & Tree Strings)**:
   - `CF 1466G — Song of the Sirens`: Iterated recurrence $s_i = s_{i-1} + t_i + s_{i-1}$ pattern counting via level promotion $r_0$ + boundary window $U + c + V$ weighted prefix sums.
   - `CF 1223F — Stack Exterminable Arrays`: Adjacent pair cancellation (`cc -> \varepsilon`) via Stack-Trie walk / $SL_2(\mathbb{F}_p)$ hashing in $O(N \log N)$.
   - `CF 914E — Palindromes in a Tree`: Centroid decomposition + XOR bitmask frequency array for path reorderable-palindrome counting.

---

## Iteration 52: Multilingual Problem Mining (`[EN]` / `[ZH]` / `[JA]`) — 36 Curated Non-Template Problems (4-Tier Difficulty Ladder) & Quarantine Ledger (`R-5B-01..R-5B-10`)

Every accepted problem below is **strictly non-template**, requires a genuine structural reduction or invariant discovery, and is analyzed under the **4-Step Zero-Magic Standard**.

---

### Tier 1: Stepping Stone (Core Invariant Recognition & Single-Mechanism Reductions — 9 Problems)

#### Problem 5B-01: `CF 1223F — Stack Exterminable Arrays` (`[EN]` Codeforces Round 588 Div. 1 C)
- **Inline Mathematical Statement & Constraints**: Given an array $a[1..n]$ of integers ($1 \le a_i \le n$, $\sum n \le 3 \cdot 10^5$), a contiguous subarray $a[l..r]$ is *stack-exterminable* if pushing $a_l, a_{l+1}, \dots, a_r$ onto an initially empty stack (popping whenever the new element equals the current stack top) leaves the stack empty at the end. Count the number of stack-exterminable subarrays $1 \le l \le r \le n$. Time limit: $2.0\text{s}$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Naive simulation from every left endpoint $l$ takes $O(n^2)$. Replacing stack reduction by prefix XOR ($v_{a_i} \oplus v_{a_i} = 0$) fails because XOR is commutative and falsely accepts `1 2 1 2`.
  2. **Combinatorial Word Invariant**: In the free product $G = \Asterisk_{x=1}^n (\mathbb{Z}/2\mathbb{Z})$ where each generator satisfies $x^2 = 1_G$, every prefix $a[1..i]$ reduces to a unique irreducible word $P_i = \text{red}(a[1..i])$. Since $x^{-1} = x$, $\text{red}(a[l..r]) = \varepsilon \iff P_{l-1}^{-1} P_r = 1_G \iff P_{l-1} = P_r$.
  3. **Reverse-Engineering Scratchpad**: Maintain the Cayley tree (a Trie of irreducible stacks) rooted at $u_0 = \text{root}$. At step $i$, if $u_{i-1} \ne \text{root}$ and the incoming edge label of $u_{i-1}$ equals $a_i$, step up to $u_i = \text{par}(u_{i-1})$; otherwise step down to child $\text{next}[u_{i-1}][a_i]$ (allocating a new node if needed). Add $\text{cnt}[u_i]$ to the answer and increment $\text{cnt}[u_i]$. Alternatively, multiply prefix $2 \times 2$ trace-zero determinant-$-1$ matrices in $GL_2(\mathbb{F}_p)$.
  4. **Boundary Pitfalls**: Clearing a global Trie of size $n$ with `memset` across test cases takes $O(n^2)$ if $|\Sigma| = n$; use `std::map<int, int>` per node and only clear nodes `0..nodes_used` to guarantee $O(n \log n)$ total time.

#### Problem 5B-02: `AGC 031 D — A Sequence of Permutations` (`[JA]` AtCoder Grand Contest 031 D)
- **Inline Mathematical Statement & Constraints**: For permutations $p, q \in S_N$, define $f(p, q)$ as the permutation $r$ where $r_{p_i} = q_i$, i.e., $f(p, q) = q p^{-1}$. Given $a_1 = p$, $a_2 = q$, and $a_n = f(a_{n-2}, a_{n-1})$ for $n \ge 3$, compute $a_K$ for $N \le 10^5$ and $K \le 10^9$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: $S_N$ is non-abelian! Treating $a_n = a_{n-1} a_{n-2}^{-1}$ like a scalar linear recurrence ($a_n = a_{n-1} - a_{n-2}$, which is strictly 6-periodic) fails for $n \ge 7$ because $p$ and $q$ do not commute.
  2. **Combinatorial Word Invariant**: Expand the first 8 terms in the free group generated by $p, q$:
     - $a_1 = p$, $a_2 = q$, $a_3 = q p^{-1}$, $a_4 = q p^{-1} q^{-1}$, $a_5 = q p^{-1} q^{-1} p q^{-1}$, $a_6 = q p^{-1} q^{-1} p q p^{-1} q^{-1}$,
     - $a_7 = (q p^{-1} q^{-1} p) p (q p^{-1} q^{-1} p)^{-1} = G p G^{-1}$,
     - $a_8 = (q p^{-1} q^{-1} p) q (q p^{-1} q^{-1} p)^{-1} = G q G^{-1}$, where $G = q p^{-1} q^{-1} p$ is the group commutator!
     Because conjugation $\Phi_G(x) = G x G^{-1}$ is a **group homomorphism** ($\Phi_G(xy^{-1}) = \Phi_G(x)\Phi_G(y)^{-1}$) and $\Phi_G(G) = G$, shifting $n \mapsto n + 6$ simply conjugates every term by $G$:
     $$a_{6m + r} = G^m a_r G^{-m} \quad (r \in \{1, \dots, 6\}).$$
  3. **Reverse-Engineering Scratchpad**: Compute $G = q p^{-1} q^{-1} p$ in $O(N)$, exponentiate $G^m$ in $O(N)$ via cycle decomposition of $G$ (where $m = \lfloor (K-1)/6 \rfloor$), and evaluate $G^m a_r G^{-m}$ in $O(N)$ time.
  4. **Boundary Pitfalls**: Confusing left vs. right permutation composition ($r_{p_i} = q_i \iff r = q \circ p^{-1}$ where $(A \circ B)_i = A_{B_i}$) inverts the commutator $G$ to $G^{-1}$; always test $a_3 = q p^{-1}$ on a 3-element non-commuting example before exponentiating.

#### Problem 5B-03: `CF 1466G — Song of the Sirens` (`[EN]` Good Bye 2020 G)
- **Inline Mathematical Statement & Constraints**: Given a seed string $s_0$ ($|s_0| \le 100$) and a pivot string $t[1..n]$ ($n \le 10^5$), define $s_i = s_{i-1} + t_i + s_{i-1}$ for $1 \le i \le n$. Answer $q \le 10^5$ queries $(k, w)$ ($\sum |w| \le 10^6$): count occurrences of pattern $w$ in $s_k \bmod (10^9+7)$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: $|s_k| = (|s_0|+1)2^k - 1$ reaches $2^{10^5}$, while $\sum |w| \le 10^6$ forbids $O(|w|^3 \log k)$ matrix exponentiation.
  2. **Combinatorial Word Invariant**: Let $r_0 \le k$ be the smallest index with $|s_{r_0}| \ge |w|$. Since $|s_r| = 2|s_{r-1}|+1$, $|s_{r_0}| \le 2|w| + |s_0|$. For every $r > r_0$, $s_r = s_{r-1} + t_r + s_{r-1}$ has the **exact same** length-$(|w|-1)$ suffix $U = \text{suff}_{|w|-1}(s_{r_0})$ and prefix $V = \text{pref}_{|w|-1}(s_{r_0})$. Thus every boundary-straddling match at level $r > r_0$ occurs inside the fixed string $U + t_r + V$ of length $2|w|-1$ and doubles $k - r$ times afterward.
  3. **Reverse-Engineering Scratchpad**: Explicitly build $s_{r_0}$ in $O(|w| + |s_0|)$ time and count $\text{occ}(w, s_{r_0})$ via KMP. Extract $U = \text{suff}_{|w|-1}(s_{r_0})$ and $V = \text{pref}_{|w|-1}(s_{r_0})$. Use KMP/Z-algorithm on $w \# U$ and $V \# w$ to determine in $O(|w|)$ time which center positions $j \in [1, |w|]$ of $w$ can align with the pivot $t_r$ (requiring $w[1..j-1]$ to be a suffix of $U$ and $w[j+1..|w|]$ to be a prefix of $V$). Sum the precomputed geometric weights $\sum_{r=r_0+1, t_r = w[j]}^k 2^{k-r}$ over all valid pivot positions $j$.
  4. **Boundary Pitfalls**: If $|s_k| < |w|$ even at $r = k$, return $0$ immediately; do not advance $r_0$ past $k$.

#### Problem 5B-04: `ABC 313 G — Redistribution of Piles` / Mechanical Sturmian Word Sums (`[JA]` AtCoder Beginner Contest 313 G)
- **Inline Mathematical Statement & Constraints**: Count distinct configurations or prefix sums generated by floor-linear operations $\lfloor (ai + b)/c \rfloor$, which correspond directly to the 1-weight prefix sums of lower mechanical Sturmian words $s_{\alpha, \rho}$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Iterating over $i = 0, \dots, N$ when $N \le 10^{18}$ or $a_i \le 10^9$ takes linear time.
  2. **Combinatorial Word Invariant**: The lower mechanical word $s_{a/c, b/c}(i) = \lfloor \frac{a(i+1)+b}{c} \rfloor - \lfloor \frac{ai+b}{c} \rfloor$ is balanced, and its prefix sum $\sum_{i=0}^{n-1} s(i) = \lfloor \frac{an+b}{c} \rfloor$ satisfies the Euclidean lattice reflection symmetry (`floor_sum` / Ostrowski continued-fraction reduction).
  3. **Reverse-Engineering Scratchpad**: Apply the Euclidean continued-fraction step $(a, c) \mapsto (c \bmod a, a)$—which in Sturmian word theory corresponds to the Ostrowski directive sequence of morphisms $\varphi_{q_k}$—reducing the sum in $O(\log(\min(a, c)))$ steps.
  4. **Boundary Pitfalls**: Off-by-one errors when $an + b < 0$ or at exact lattice hits $(ai+b) \equiv 0 \pmod c$ (distinguishing lower mechanical $s_{\alpha,\rho}$ from upper mechanical $s'_{\alpha,\rho}$).

#### Problem 5B-05: `AGC 022 E — Median Replace` (`[JA]` AtCoder Grand Contest 022 E)
- **Inline Mathematical Statement & Constraints**: Given a string $S \in \{\text{`0'}, \text{`1'}, \text{`?'}\}^N$ ($N \le 3 \cdot 10^5$, $N$ odd), count how many ways to replace `?` with `0`/`1` produce a string that can be reduced to `'1'` by repeatedly replacing any contiguous length-3 substring with its median.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Since any length-3 substring can be reduced in any order, the set of valid strings appears non-local ($O(N^3)$ interval DP).
  2. **Combinatorial Word Invariant**: Maintain a stack holding a reduced prefix matching the regular expression `1* 0*` with at most two `1`s and at most two `0`s:
     - Whenever `000` appears at the stack top, replace `000 -> 0` (losing nothing, since three `0`s can never help form `1`).
     - Whenever `01` appears on the stack (`...0` followed by incoming `1`), **immediately cancel `01 -> \varepsilon`** (because in median replacement, an adjacent `0` and `1` act as an identity element: $\text{med}(0, 1, x) = x$!).
     - Once the stack reaches `11` (two unmatched `1`s), any further `1` is capped at `11` because `11` already guarantees the entire string can be reduced to `1` regardless of future characters!
  3. **Reverse-Engineering Scratchpad**: The minimal deterministic stack automaton has only **6 reachable states** $(c_1, c_0) \in \{0, 1, 2\} \times \{0, 1, 2\}$ (representing $c_1$ ones followed by $c_0$ zeros). Run a $6$-state Automaton DP over $S[1..N]$ in $O(N)$ time; accept states with $c_1 \ge c_0$ at the end.
  4. **Boundary Pitfalls**: Failing to cap $c_1$ at $2$ or reducing `10` instead of `01` on the stack allows `00` at the end to annihilate `11` in the wrong order; the invariant requires maintaining `1`s at the bottom (`c_1`) and `0`s at the top (`c_0`).

#### Problem 5B-06: `CF 808G — Anthem of Berland` (`[EN]` Codeforces Educational Round 21 G)
- **Inline Mathematical Statement & Constraints**: Given $S \in (\Sigma \cup \{\text{`?'}\})^n$ and $T \in \Sigma^m$ with $n \cdot m \le 10^7$, replace each `?` in $S$ to maximize the number of occurrences of $T$ in $S$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Naive KMP Automaton DP has $n \times m$ states and $26$ transitions per `?`, costing $26 nm \approx 2.6 \cdot 10^8$ operations.
  2. **Combinatorial Word Invariant**: Any placement of $T$ ending at position $i$ forces $S[i-m+1..i] = T$. Two occurrences of $T$ ending at $j < i$ with $i - j < m$ are compatible **if and only if** their overlap length $k = m - (i - j)$ belongs to $\text{Borders}(T)$!
  3. **Reverse-Engineering Scratchpad**: Let $dp[i]$ be the maximum occurrences in $S[1..i]$ given an occurrence of $T$ ends at $i$, and $ans[i] = \max_{j \le i} dp[j]$. Then $dp[i] = 1 + \max\bigl(ans[i-m],\; \max_{k \in \text{Borders}(T)} dp[i - m + k]\bigr)$. Because $\text{Borders}(T) = \{ \pi(m), \pi(\pi(m)), \dots \}$, setting $g[i] = \max_{k \in \text{Borders}(T)} dp[i - m + k]$ satisfies the $O(1)$ KMP-tree recurrence when $T$ matches at $i$, reducing total time to $O(nm)$ with constant factor $1$!
  4. **Boundary Pitfalls**: Only update $dp[i]$ at indices $i$ where $S[i-m+1..i]$ is compatible with $T[1..m]$.

#### Problem 5B-07: `AGC 047 B — First Second` (`[JA]` AtCoder Grand Contest 047 B)
- **Inline Mathematical Statement & Constraints**: Given $N$ strings $S_1, \dots, S_N$ ($\sum |S_i| \le 10^6$), in one operation on string $X$ ($|X| \ge 2$) you may delete either $X[1]$ or $X[2]$. Count pairs $(i, j)$ such that $S_i$ can be reduced to $S_j$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Checking all pairs $(i, j)$ takes $O(N^2)$.
  2. **Combinatorial Word Invariant**: Repeatedly deleting $X[1]$ or $X[2]$ from $S_i$ keeps the suffix $S_i[k..|S_i|]$ ($k \ge 2$) intact and allows the first character to be **any character that appeared in the prefix $S_i[1..k-1]$**! Thus $S_i \to S_j$ iff $|S_i| \ge |S_j|$, the suffix of $S_i$ of length $|S_j|-1$ equals $S_j[2..|S_j|]$, and $S_j[1] \in \{ S_i[1], \dots, S_i[|S_i|-|S_j|+1] \}$.
  3. **Reverse-Engineering Scratchpad**: Insert all reversed strings $S_i^R$ into a Trie. For each $S_i$, walk down $S_i^R$ while maintaining the bitmask of characters present in the remaining prefix of $S_i$; at each step, increment `cnt[node][c]` for every character $c$ in the prefix bitmask. Then query `cnt[end_node(S_j^R[1..|S_j|-1])][S_j[1]]`.
  4. **Boundary Pitfalls**: Subtract $N$ self-pairs $(i, i)$ if $i \ne j$ is required.

#### Problem 5B-08: `POI XII — Template (Szablon)` (`[EN]` Polish Olympiad in Informatics XII / Luogu P3426)
- **Inline Mathematical Statement & Constraints**: Given a string $S$ ($|S| \le 5 \cdot 10^5$), find the length of the shortest prefix $P = S[1..k]$ that can stamp the entire string $S$ by overlapping copies of $P$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Testing every prefix $S[1..k]$ independently takes $O(N^2)$.
  2. **Combinatorial Word Invariant**: A substring $P$ can stamp $S$ iff $P$ is a **border** of $S$ (so it covers $S[1..|P|]$ and $S[N-|P|+1..N]$) and the maximum gap between consecutive end-positions of $P$ in $S$ is at most $|P|$.
  3. **Reverse-Engineering Scratchpad**: Build the KMP failure tree (`pi` tree). Any candidate $P$ must lie on the ancestor spine from $N$ to $0$. Perform a bottom-up DP on the KMP tree: for node $u$ on the spine of $N$, $dp[u] = u$ unless $u$ has a child $v$ with $\max\_gap(v) \le v$ (or in the spine formulation, $dp[i] = dp[\pi(i)]$ if there exists $j \ge i - dp[\pi(i)]$ with $dp[j] = dp[\pi(i)]$, else $i$). Runs in $O(N)$ time!
  4. **Boundary Pitfalls**: Checking only $\text{last\_occurrence} \ge i - \pi(i)$ is wrong; you must check against $i - dp[\pi(i)]$ because $\pi(i)$ itself might not be a valid stamp while its shortest valid stamp $dp[\pi(i)]$ is!

#### Problem 5B-09: `[SCOI2016] 萌萌哒` (`[ZH]` Luogu P3295)
- **Inline Mathematical Statement & Constraints**: Given $N \le 10^5$ digits (first digit $\ne 0$) and $M \le 10^5$ substring equality constraints $S[l_1..r_1] = S[l_2..r_2]$, count the number of valid $N$-digit numbers modulo $10^9+7$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Merging $r_1 - l_1 + 1$ character pairs per constraint in a flat DSU takes $O(NM)$ time.
  2. **Combinatorial Word Invariant**: Decompose each interval length $L = r_1 - l_1 + 1$ into two overlapping power-of-two blocks of length $2^k$ ($k = \lfloor \log_2 L \rfloor$). Maintain $O(\log N)$ DSU layers where layer $k$ tracks equality of length-$2^k$ substrings.
  3. **Reverse-Engineering Scratchpad**: Insert each constraint into layer $k = \lfloor \log_2 L \rfloor$ via two `unite` calls. Then push down from $k = \log_2 N$ down to $1$: if `find(k, i) == r`, execute `unite(k-1, i, r)` and `unite(k-1, i + 2^{k-1}, r + 2^{k-1})`. If layer $0$ has $C$ connected components, the answer is $9 \cdot 10^{C-1} \bmod (10^9+7)$.
  4. **Boundary Pitfalls**: When $N = 1$ and $M = 0$, all $10$ digits `0..9` may be valid if single-digit `0` is allowed, or $9$ if strictly positive—check the problem's $N=1$ convention.

---

### Tier 2: Intermediate (Multi-Step Coupling, Automaton/Matrix Algebra & Periodicity — 9 Problems)

#### Problem 5B-10: `[SDOI2019] 连续子序列` (`[ZH]` Luogu P5362)
- **Inline Mathematical Statement & Constraints**: Let $\mathbf{t}$ be the infinite Thue–Morse word (`01101001...`, generated by $\mu(0)=01, \mu(1)=10$). Given a binary string $S$ ($|S| \le 100$) and an integer $k \le 10^{18}$, count the number of strings of length $|S| + k$ of the form $S + W$ ($|W| = k$) that occur as a contiguous substring of $\mathbf{t}$, modulo $10^9+9$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: $k \le 10^{18}$ forbids building the string $S+W$. Moreover, $\mathbf{t}$ is aperiodic, so its factors do not repeat periodically.
  2. **Combinatorial Word Invariant (Inverse Morphism Decimation / Odd-Even Pairing)**: Every occurrence of a factor $X$ in $\mathbf{t} = \mu(\mathbf{t})$ either aligns with block boundaries at even indices ($X = c_{\text{left}} \mu(Y) c_{\text{right}}$ starting at odd index) or even index ($X = \mu(Y) c_{\text{right}}$). Crucially, for any $|X| \ge 4$, the parity of the starting index of $X$ in $\mathbf{t}$ is **uniquely forced** because `00` and `11` can only occur straddling a block boundary (starting at an odd index)!
  3. **Reverse-Engineering Scratchpad**: Because $W$ is arbitrary of length $k$, define a memoized recursion `solve(S, k)`:
     - Base cases: When $|S| + k \le 3$, explicitly check all $2^k$ extensions $W$ against the known length-$\le 3$ factors of $\mathbf{t}$ (`0, 1, 00, 01, 10, 11, 001, 010, 011, 100, 101, 110`).
     - Recursive step: Consider the two possible starting parities $p \in \{0, 1\}$ of $S$ in $\mathbf{t}$. If $S$ is consistent with parity $p$ (every internal pair at even offset is `01` or `10`), compress $S$ via $\mu^{-1}$ into a shorter prefix $S'$ of length $\lceil |S|/2 \rceil$ and recurse on $(S', \lfloor k/2 \rfloor)$ and $(S', \lceil k/2 \rceil)$ depending on whether the last character of $S+W$ straddles a pair!
     Memoize on the tuple $(S, k)$: since $|S|$ halves at each step and reaches $|S| \le 2$ within $\lceil \log_2 |S| \rceil$ steps, only $O(|S| + \log k)$ states are ever visited!
  4. **Boundary Pitfalls**: For $|S| \le 3$, **both** parities $p = 0$ and $p = 1$ can simultaneously be valid for the same $S+W$ (e.g., `010` occurs at both odd and even positions in $\mathbf{t}$!). If you sum $p=0$ and $p=1$ branches while $|S| + k \le 3$, you double-count extensions $W$ that appear at both parities! Always cut off the recursion and brute-force against the exact factor set whenever $|S| + k \le 3$.

#### Problem 5B-11: `AGC 050 C — Block Game` (`[JA]` AtCoder Grand Contest 050 C)
- **Inline Mathematical Statement & Constraints**: Given a string $S \in \{\text{`B'}, \text{`S'}, \text{`?'}\}^N$ ($N \le 10^6$), count ways to replace `?` so Snuke wins the block-eliminating game.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Game state depends on lengths of runs of `'S'` between `'B'`s, seemingly requiring $O(N^2)$ DP.
  2. **Combinatorial Word Invariant**: Working backwards from the last `'B'` to the first `'B'`, at the $k$-th `'B'` from the right, Snuke loses **if and only if** every run of `'S'` between consecutive `'B'`s has length $< 2^{k-1}$! Since $2^{20} > 10^6$, at most $21$ `'B'`s from the right can ever constrain a losing configuration!
  3. **Reverse-Engineering Scratchpad**: Count losing configurations via a 2D DP `dp[i][k]` ($1 \le i \le N$, $0 \le k \le 21$) tracking the position $i$ of the $k$-th `'B'` from the right, accelerated with prefix sums in $O(N \log N)$ time.
  4. **Boundary Pitfalls**: The rightmost segment (after the last `'B'`) requires length $0$ (i.e., the string must end with `'B'` or have $< 2^0 = 1$ trailing `'S'` to lose at step $0$).

#### Problem 5B-12: `[WC2016] 论战捆竹竿` (`[ZH]` Luogu P4156 / LOJ 2087)
- **Inline Mathematical Statement & Constraints**: Given a string $S$ of length $n \le 5 \cdot 10^5$ and target limit $W \le 10^{18}$ ($\sum n \le 5 \cdot 10^5$), each overlapping concatenation of $S$ with border $b$ adds $n - |b|$ to the total length. Count how many total lengths $\in [n, W]$ are achievable.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Each border $b$ gives a knapsack item weight $p = n - |b|$ (a period of $S$). Since there can be $O(n)$ periods, standard modulo shortest path (Dijktra on $\mathbb{Z}/p_0\mathbb{Z}$) takes $O(n^2)$.
  2. **Combinatorial Word Invariant (Weak Periodicity Lemma)**: The periods $p = n - |b|$ of $S$ partition into $O(\log n)$ arithmetic progressions $p_i = x + k d$ ($0 \le k \le c$).
  3. **Reverse-Engineering Scratchpad**: Process the $O(\log n)$ AP blocks one by one. When transitioning from previous modulus $m_{\text{old}}$ to new modulus $x$ (the base of the current AP), remap shortest paths $D_{\text{old}}[r] \to D_{\text{new}}[D_{\text{old}}[r] \bmod x]$ and relax the edge $+m_{\text{old}}$ on cycles of $\gcd(m_{\text{old}}, x)$. Then relax the bounded AP items $x + kd$ ($1 \le k \le c$) on each residue class modulo $d$ using a **sliding-window monotonic queue** of width $c$ in $O(x)$ time! Total time: $O(n \log n)$.
  4. **Boundary Pitfalls**: When transitioning from modulus $m_{\text{old}}$ to $x$, you **must** relax the single item of weight $m_{\text{old}}$ around each cycle of $\gcd(m_{\text{old}}, x)$ (taking two passes around the cycle starting from its minimum element) before applying the new AP!

#### Problem 5B-13: `CF 932G — Palindrome Partition` (`[EN]` ICM Technex 2018 G)
- **Inline Mathematical Statement & Constraints**: Given $S[1..n]$ ($n \le 10^6$, $n$ even), count symmetric partitions $S = s_1 s_2 \dots s_k$ with $s_i = s_{k-i+1}$ for all $i$, modulo $10^9+7$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Symmetric matching connects prefix $s_1$ with suffix $s_k$ simultaneously, which looks 2-sided.
  2. **Combinatorial Word Invariant**: Interleave $S$ with its reversal into $T = S_1 S_n S_2 S_{n-1} \dots S_{n/2} S_{n/2+1}$. Then $s_i = s_{k-i+1}$ in $S$ holds **if and only if** the corresponding interleaved block in $T$ is an **even-length palindrome**! By the Weak Periodicity Lemma on PAM, all palindromic suffixes of $T[1..r]$ partition into $O(\log r)$ `slink` chains.
  3. **Reverse-Engineering Scratchpad**: Maintain `g[u]` on each PAM node $u$: the sum of $dp[r - \text{len}(v)]$ for all $v$ in the arithmetic progression above $u$ down to $\text{slink}(u)$. At index $r$, update `g[u] = dp[r - len(slink(u)) - diff(u)] + g[fail(u)]` in $O(1)$ per chain, and sum `g[u]` into $dp[r]$ when $r$ is even.
  4. **Boundary Pitfalls**: Never clear or zero out `g[u]` when $r$ is odd! Although $dp[r] = 0$ at odd $r$, `g[u]` must still be updated at odd $r$ so that future even positions $r' > r$ that inherit `g[fail(u)]` read the properly shifted AP sum.

#### Problem 5B-14: `CF 666E — Forensic Examination` (`[EN]` Codeforces Round 349 Div. 1 E)
- **Inline Mathematical Statement & Constraints**: Given a string $S$ ($|S| \le 5 \cdot 10^5$) and dictionary $T_1, \dots, T_m$ ($\sum |T_i| \le 5 \cdot 10^4$), answer $Q \le 5 \cdot 10^5$ queries $(l, r, p_l, p_r)$: which $T_i$ ($l \le i \le r$) maximizes $\text{occ}(S[p_l..p_r], T_i)$?
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Querying an arbitrary substring $S[p_l..p_r]$ across a range of dictionary strings $[l, r]$ cannot be done on a static AC automaton.
  2. **Combinatorial Word Invariant**: Build a Generalized SAM over $T_1, \dots, T_m$ (plus walk $S$ over the GSAM to record the deepest matched state $u_r$ and match length $\ell_r$ for each prefix $S[1..r]$). If $\ell_{p_r} < p_r - p_l + 1$, $S[p_l..p_r]$ has $0$ occurrences everywhere; otherwise binary-lift from $u_{p_r}$ up the Link Tree to the shallowest ancestor $v$ with $\text{len}(v) \ge p_r - p_l + 1$.
  3. **Reverse-Engineering Scratchpad**: Merge persistent segment trees over dictionary index $i \in [1, m]$ bottom-up along the GSAM Link Tree, storing `(max_count, -min_index)`. Query $[l, r]$ at node $v$ in $O(\log m)$ time.
  4. **Boundary Pitfalls**: When $\max_{i \in [l, r]} \text{cnt}_v(i) = 0$, the tie-breaking rule requires returning the smallest index $l$ with count $0$ (not index $0$ from an empty segment tree node!).

#### Problem 5B-15: `[ZJOI2015] 诸神眷顾的幻想乡` (`[ZH]` Luogu P3346)
- **Inline Mathematical Statement & Constraints**: Given an unrooted tree with $N \le 10^5$ vertices, vertex colors in $\{0, \dots, c-1\}$ ($c \le 10$), and **at most $20$ leaves**, count the number of distinct strings formed by simple paths on the tree.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: A tree has $O(N^2)$ simple paths; inserting all paths into a SAM takes $O(N^2)$.
  2. **Combinatorial Word Invariant**: Every directed simple path $u \to v$ on a tree is a contiguous sub-path of some root-to-leaf path when the tree is rooted at the leaf of the component in the direction of $u$! Therefore, the union of the **20 rooted Tries** (one rooted at each leaf of the tree) contains every directed simple path as a root-to-node prefix!
  3. **Reverse-Engineering Scratchpad**: For each of the $\le 20$ degree-1 vertices $r$, run a DFS from $r$ to insert all paths into a single shared Trie (size $\le 20 N$), then build a BFS-based Generalized SAM on the Trie and return $\sum_u (\text{len}(u) - \text{len}(\text{link}(u)))$.
  4. **Boundary Pitfalls**: Build the GSAM via **BFS on the Trie** (passing `gsam_pos[trie_parent]` to `extend`), never by resetting `last = 1` along DFS branches without checking existing transitions (which creates zero-length clone nodes!).

#### Problem 5B-16: `CF 528D — Fuzzy Search` (`[EN]` Codeforces Round 296 Div. 1 D)
- **Inline Mathematical Statement & Constraints**: Given $S, T \in \{\text{`A', `C', `G', `T'}\}^*$ ($|T| \le |S| \le 2 \cdot 10^5$) and threshold $k \ge 0$, character $T[j]$ matches at $S[i+j]$ if some $S[p] = T[j]$ exists with $|p - (i+j)| \le k$. Count valid shifts $i$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Naive $O(|S||T|)$ fails; standard KMP fails because matching is non-transitive under threshold radius $k$.
  2. **Combinatorial Word Invariant**: Since $|\Sigma| = 4$ is tiny, expand each character $c \in \{\text{A,C,G,T}\}$ separately: dilate $S$'s indicator array for $c$ by window $[-k, +k]$ via difference arrays, then compute the cross-correlation with $T$'s indicator array for $c$ via FFT.
  3. **Reverse-Engineering Scratchpad**: For each $c \in \Sigma$, compute $C_c[i] = \sum_{j=0}^{|T|-1} I_{S, c}^{\text{dilated}}[i+j] \cdot I_{T, c}[j]$ by reversing $I_{T, c}$ and running 1 NTT/FFT. Shift $i$ is valid iff $\sum_{c \in \Sigma} C_c[i] = |T|$.
  4. **Boundary Pitfalls**: Clamp the dilated indicator $I_{S, c}^{\text{dilated}}[p]$ to $\min(1, \text{prefix\_sum}[p])$ before running FFT; otherwise a position $p$ near multiple copies of $c$ contributes $> 1$ and masks a mismatch elsewhere!

#### Problem 5B-17: `[CTSC2006] 歌唱王国` (`[ZH]` Luogu P4548)
- **Inline Mathematical Statement & Constraints**: An $m$-sided fair die generates characters one by one until pattern $S[1..n]$ ($n \le 10^5$) appears. Compute the expected stopping time $\mathbb{E}[T_S] \bmod 10^4$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Building the $n \times n$ KMP transition matrix and inverting $(I - P)$ takes $O(n^3)$.
  2. **Combinatorial Word Invariant (Conway's Casino Martingale / PGF Cluster System)**: Let $F(z)$ be the PGF of $T_S$ and $G(z)$ be the GF of non-terminated prefixes. Decomposing $G(z) \cdot (\frac{z}{m})^n$ by the first index where $S$ finishes inside the appended tail $S$ yields:
     $$1 + \frac{z-1}{m^n} G(z) = F(z), \qquad G(z) \cdot \left(\frac{z}{m}\right)^n = \sum_{k \in \text{Borders}(S)} F(z) \left(\frac{z}{m}\right)^{n-k}.$$
     Evaluating at $z = 1$ ($F(1) = 1, F'(1) = \mathbb{E}[T_S] = G(1)$) gives $\mathbb{E}[T_S] = \sum_{k \in \text{Borders}(S)} m^k$ (including $k = n$).
  3. **Reverse-Engineering Scratchpad**: Compute the KMP `pi` array of $S$ in $O(n)$ time and sum $m^k \bmod 10^4$ along the border chain $k = n, \pi(n), \pi(\pi(n)), \dots > 0$.
  4. **Boundary Pitfalls**: Output must be zero-padded to 4 digits (`%04d`) as required by the problem statement.

#### Problem 5B-18: `ABC 214 F — Substrings` & Range Invertible Matrix Extension (`[JA]` AtCoder Beginner Contest 214 F / Range Variant)
- **Inline Mathematical Statement & Constraints**: Count distinct non-empty subsequences of $S[1..N]$ (or query $S[l..r]$ for $Q$ range queries) such that no two chosen indices are adjacent in $S$ (or in the standard range subsequence variant, any subsequence of $S[l..r]$).
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Standard distinct-subsequence DP $dp[i] = 2 dp[i-1] - dp[\text{last}[S[i]] - 1]$ depends on `last[c]`, which changes with the left endpoint $l$ in range queries $S[l..r]$.
  2. **Combinatorial Word Invariant**: Reformulate the state at step $i$ as the vector $\mathbf{v}_i = (w_a, w_b, \dots, w_z, 1)^T$, where $w_c$ is the number of distinct subsequences ending with character $c$. Appending $c = S[i]$ replaces row $c$ by $\sum_{x \in \Sigma} w_x + 1$, which is multiplication by a rank-1 perturbation of the identity matrix $M_c = I + \mathbf{e}_c \mathbf{1}^T$. Its exact inverse is $M_c^{-1} = I - \frac{1}{2} \mathbf{e}_c (\mathbf{1} - \mathbf{e}_c)^T$ (subtracting all other rows from row $c$), which also takes $O(|\Sigma|)$ to multiply!
  3. **Reverse-Engineering Scratchpad**: Maintain prefix products $P_r = M_{S[r]} \cdots M_{S[1]} \mathbf{v}_0$ and inverse prefix matrices $P_{l-1}^{-1}$ in $O(N |\Sigma|^2)$ preprocessing, answering each range query $[l, r]$ in $O(|\Sigma|)$ time! (For the non-adjacent step in `ABC 214F`, jump from $\text{prev}(i)$ to $j \le i - 2$.)
  4. **Boundary Pitfalls**: In the non-adjacent variant (`ABC 214F`), to avoid double-counting a subsequence of length $k$, require that if $S[i]$ is chosen as the $k$-th character after $S[j]$ ($j \le i-2$), $i$ must be the **first** occurrence of character $S[i]$ at index $\ge j + 2$!

---

### Tier 3: Advanced (Deep Structural Synthesis, Significant Suffixes, Runs & Substring Clipping — 9 Problems)

#### Problem 5B-19: `[NOI2018] 你的名字` (`[ZH]` Luogu P4770 / LOJ 2720 / UOJ 395)
- **Inline Mathematical Statement & Constraints**: Given a base string $S$ ($|S| \le 5 \cdot 10^5$) and $Q \le 10^5$ queries $(T, l, r)$ ($\sum |T| \le 10^6$), count how many **distinct** substrings of $T$ do **not** occur as a contiguous substring of $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Both deduplicating substrings of $T$ and checking containment inside a restricted window $S[l..r]$ must run in $O(|T| \log |S|)$ time per query.
  2. **Combinatorial Word Invariant ($\text{endpos}$ Clipping + Dual SAM)**:
     - Build the SAM of $S$ and merge persistent segment trees over $\text{endpos}_S(u)$ bottom-up on its Link Tree.
     - A candidate prefix $T[1..i]$ of length $\ell$ occurs in $S[l..r]$ iff the corresponding SAM state $u$ of $S$ contains an end-position $p \in \text{endpos}_S(u)$ such that the substring $T[i-\ell+1..i]$ both ends at $\le r$ and **starts at $\ge l$**, i.e., $p \in [l + \ell - 1, r]$!
  3. **Reverse-Engineering Scratchpad**: For each query $T$:
     1. Build a standalone SAM for $T$.
     2. Compute for each prefix $T[1..i]$ the maximum suffix length $\text{lim}[i]$ that occurs in $S[l..r]$ by walking on the SAM of $S$: attempt to advance $(u, \ell)$ on $T[i]$ while $\text{query\_endpos}(u, l + \ell, r)$ is true; if false, decrement $\ell$ (stepping $u \leftarrow \text{link}_S(u)$ whenever $\ell = \text{len}_S(\text{link}_S(u))$) until valid.
     3. Each state $v$ in the SAM of $T$ (with representative end-position $\text{pos}(v)$) contributes $\max\bigl(0,\; \text{len}_T(v) - \max(\text{len}_T(\text{link}_T(v)),\; \text{lim}[\text{pos}(v)])\bigr)$ to the answer!
  4. **Boundary Pitfalls**: Dropping $\ell$ directly to $\text{len}_S(\text{link}_S(u))$ when $\text{query\_endpos}(u, l + \ell - 1, r)$ fails is **wrong**! Because the interval $[l + \ell - 1, r]$ widens as $\ell$ decreases, a shorter length $\ell' \in (\text{len}_S(\text{link}_S(u)), \ell)$ inside the **same** state $u$ might already satisfy $\text{max\_endpos}_u(\le r) - \ell' + 1 \ge l$! Either set $\ell \leftarrow \min(\ell - 1, \text{max\_endpos}_u(\le r) - l + 1)$ or decrement $\ell$ by $1$ per step.

#### Problem 5B-20: `CF 1037H — Security` (`[EN]` Manthan, Codefest 18 H)
- **Inline Mathematical Statement & Constraints**: Given $S$ ($|S| \le 10^5$) and $Q \le 2 \cdot 10^5$ queries $(l, r, T)$ ($\sum |T| \le 2 \cdot 10^5$), find the lexicographically smallest substring of $S[l..r]$ strictly greater than $T$ (or `-1` if none exists).
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Searching over all substrings of $S[l..r]$ takes $O((r-l)^2)$.
  2. **Combinatorial Word Invariant**: Any substring of $S[l..r]$ strictly greater than $T$ shares a longest common prefix $T[1..i]$ ($0 \le i \le |T|$) followed by the smallest character $c > T[i+1]$ such that $T[1..i] + c$ occurs in $S[l..r]$, i.e., $\text{endpos}_S(\delta(u_i, c)) \cap [l + i, r] \ne \emptyset$.
  3. **Reverse-Engineering Scratchpad**: Walk $T$ along the SAM of $S$ as far as possible, recording the state $u_i$ for each prefix $T[1..i]$. Backtrack $i$ from $\min(|T|, r-l)$ down to $0$, testing $c \in (T[i+1], \text{`z'}]$ via Segment Tree Merge query on $[l + i, r]$ in $O(|\Sigma| \log |S|)$ time.
  4. **Boundary Pitfalls**: Don't forget $i = |T|$ (appending `'a'..'z'` to the entire string $T$ when $|T| < r - l + 1$).

#### Problem 5B-21: `[ZJOI2017] 字符串` (`[ZH]` Luogu P3763 / LOJ 2249)
- **Inline Mathematical Statement & Constraints**: Maintain a dynamic string $S[1..n]$ ($n \le 2 \cdot 10^5$, $q \le 2 \cdot 10^5$) under two operations: (1) add $d$ to all characters in $S[l..r]$; (2) find the starting index $p \in [l, r]$ of the lexicographically smallest suffix of $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: A suffix of $S[l..r]$ is a truncated suffix of $S$: comparing $S[i..r]$ and $S[j..r]$ depends on the right boundary $r$, so the globally smallest suffix of $S$ in $[l, r]$ need not be the smallest suffix of $S[l..r]$!
  2. **Combinatorial Word Invariant (Significant Suffixes Theorem — Jin Ce 2019)**:
     When building a Segment Tree over $S$, each node covering $[L, R]$ only needs to maintain a set $\mathcal{C}(L, R)$ of **Significant Suffixes**—indices $i \in [L, R]$ that can achieve the minimal suffix of $S[L..R] + T$ for *some* right extension $T$. For any two candidates $u, v \in \mathcal{C}(L, R)$ with $|u| < |v| < 2|u|$:
     - $u$ must be a border of $v$ (otherwise the smaller one dominates for all $T$).
     - Thus $v = w^k u'$ is periodic with period $d = |v| - |u|$, and comparing $u T$ vs $v T$ reduces to comparing $v$ against $u$, which eliminates one of $u$ or $v$ independent of $T$!
     Hence $|\mathcal{C}(L, R)| \le \lceil \log_2(R - L + 1) \rceil$!
  3. **Reverse-Engineering Scratchpad**: Maintain $\mathcal{C}(u)$ ($|\mathcal{C}(u)| \le \log_2(\text{len})$) at each Segment Tree node by merging $\mathcal{C}(\text{right})$ with the surviving winner from $\mathcal{C}(\text{left})$ using $O(1)$ LCE (via Fenwick-tree polynomial hash + difference array for range $+d$ updates).
  4. **Boundary Pitfalls**: When merging $\mathcal{C}(\text{left})$ into $\mathcal{C}(\text{right})$, at most **one** candidate from $\mathcal{C}(\text{left})$ can survive (the one that beats all others on $S[\dots R]$), and you must then prune candidates with $< 2\times$ length ratio.

#### Problem 5B-22: `[NOI2016] 优秀的拆分` (`[ZH]` Luogu P1117 / UOJ 219)
- **Inline Mathematical Statement & Constraints**: Given $S[1..n]$ ($n \le 3 \cdot 10^4$), count the number of quadruples $(i, j, k, l)$ forming an $AABB$ substring ($S[i..j] = AA$, $S[j+1..l] = BB$).
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: $O(n^2)$ checks TLE across 10 test cases.
  2. **Combinatorial Word Invariant**: Let $f[i]$ be the number of squares $AA$ ending at $i$, and $g[i]$ be the number of squares $BB$ starting at $i$. Then the answer is $\sum_{i=1}^{n-1} f[i] g[i+1]$. For each half-length $L \in [1, n/2]$, place checkpoints at $L, 2L, 3L, \dots$; any square of length $2L$ must cover **exactly two** adjacent checkpoints $kL$ and $(k+1)L$!
  3. **Reverse-Engineering Scratchpad**: For each $L$ and $k$, compute $l_1 = \text{LCS}(kL, (k+1)L)$ and $l_2 = \text{LCP}(kL, (k+1)L)$ in $O(1)$ via RMQ on SA and reversed SA. If $l_1 + l_2 - 1 \ge L$, the valid starting positions of $AA$ form a contiguous interval of length $l_1 + l_2 - L$, so range-add $+1$ to $f$ and $g$ via difference arrays in $O(n \log n)$ total time!
  4. **Boundary Pitfalls**: Clamp $l_1 \le L$ and $l_2 \le L$ so a long run of period $L$ does not double-count the same square across adjacent checkpoint pairs $(k-1, k)$ and $(k, k+1)$!

#### Problem 5B-23: `CF 700E — Cool Slogans` (`[EN]` Codeforces Round 364 Div. 1 E)
- **Inline Mathematical Statement & Constraints**: Given $S[1..n]$ ($n \le 2 \cdot 10^5$), find the maximum $k$ such that there exist strings $s_1, s_2, \dots, s_k$ where $s_1$ is a substring of $S$ and each $s_{i-1}$ occurs at least twice inside $s_i$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Within a SAM node $u$, which length in $[\text{len}(\text{link}(u))+1, \text{len}(u)]$ should represent $s_i$?
  2. **Combinatorial Word Invariant**: Every string in the $\text{endpos}$ equivalence class of $u$ appears at the **exact same set of end-positions**. Therefore, we can always greedily pick the **longest** string in $u$'s class! Furthermore, an ancestor $v$ of $u$ on the Link Tree occurs at least twice inside $u$'s longest representative $S[\text{pos}(u) - \text{len}(u) + 1 .. \text{pos}(u)]$ iff $v$ has another occurrence in $\text{endpos}(v)$ inside $[\text{pos}(u) - \text{len}(u) + \text{len}(v), \text{pos}(u) - 1]$.
  3. **Reverse-Engineering Scratchpad**: Merge $\text{endpos}$ segment trees bottom-up on the SAM Link Tree, then run a top-down DP tracking the lowest ancestor $v$ with the current maximum $dp[v]$, testing $\text{query\_endpos}(v, \text{pos}(u) - \text{len}(u) + \text{len}(v), \text{pos}(u) - 1)$ in $O(\log n)$ time.
  4. **Boundary Pitfalls**: Always store an arbitrary representative $\text{pos}(u) \in \text{endpos}(u)$ at every SAM node (propagated from children during the bottom-up pass).

#### Problem 5B-24: `[SDOI2017] 硬币游戏` (`[ZH]` Luogu P3706)
- **Inline Mathematical Statement & Constraints**: $N \le 300$ players each choose a binary string $P_i \in \{H, T\}^M$ ($M \le 300$). A fair coin is tossed repeatedly until one of $P_1, \dots, P_N$ appears first. Compute the winning probability $p_i$ of each player.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: AC Automaton has $NM = 9 \cdot 10^4$ states; Gaussian elimination on $9 \cdot 10^4$ states takes $O((NM)^3)$, which is impossible.
  2. **Combinatorial Word Invariant (Goulden–Jackson Overlap System)**: Let $G(z)$ be the PGF of sequences containing none of $P_1, \dots, P_N$, and $F_i(z)$ be the PGF of sequences terminating with player $i$'s win. Appending $P_j$ to a non-terminated sequence decomposes by the first index where some $P_i$ completes, which must be an overlap suffix-prefix of length $k \in \text{Overlap}(P_i, P_j)$:
     $$\sum_{i=1}^N p_i \sum_{k \in \text{Overlap}(P_i, P_j)} 2^k = G(1) \quad (\forall j = 1, \dots, N), \qquad \sum_{i=1}^N p_i = 1.$$
  3. **Reverse-Engineering Scratchpad**: Compute $\text{Overlap}(P_i, P_j)$ for all $N^2$ pairs via KMP or hashing in $O(N^2 M)$ time, then solve the $(N+1) \times (N+1)$ linear system via Gaussian elimination in $O(N^3)$ time!
  4. **Boundary Pitfalls**: Evaluate $\sum_{k \in \text{Overlap}(P_i, P_j)} 2^{k-M}$ in `long double` (dividing by $2^M$) so $2^{300}$ does not overflow!

#### Problem 5B-25: `[HEOI2015] 最短不公共子串` (`[ZH]` Luogu P4112)
- **Inline Mathematical Statement & Constraints**: Given two strings $A, B \in \{\text{`a'..\text{`z'}}\}^*$ ($|A|, |B| \le 2000$), find the minimum length of a string $C$ for all 4 combinations of: ($C$ is a contiguous substring vs. subsequence of $A$) and ($C$ is NOT a contiguous substring vs. subsequence of $B$).
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Unifies the exact structural difference between **Suffix Automaton (SAM)** (accepting all contiguous substrings) and **Direct Acyclic Subsequence Graph (DASG / `序列自动机`)** (accepting all subsequences).
  2. **Combinatorial Word Invariant**: Build $\text{SAM}(A), \text{SAM}(B), \text{DASG}(A), \text{DASG}(B)$. For each of the 4 pairs $(\mathcal{A}_1(A), \mathcal{A}_2(B))$, the shortest string accepted by $\mathcal{A}_1(A)$ and rejected by $\mathcal{A}_2(B)$ corresponds to the shortest path in the **product automaton** $\mathcal{A}_1(A) \times \mathcal{A}_2(B)$ from $(\text{root}_A, \text{root}_B)$ to any state $(u, \emptyset)$ where $u \ne \emptyset$ and $\mathcal{A}_2(B)$ falls off a missing transition!
  3. **Reverse-Engineering Scratchpad**: Run a 0-1 BFS on the $O(|A| \cdot |B|)$ product state space for each of the 4 cases in $O(|\Sigma| |A| |B|)$ time (or $O(|A||B|)$ DP).
  4. **Boundary Pitfalls**: Ensure $\text{SAM}(A)$ does not transition from root on a character absent from $A$.

#### Problem 5B-26: `CF 827E — Rusty String` (`[EN]` Codeforces Round 423 Div. 1 E)
- **Inline Mathematical Statement & Constraints**: Given $S \in \{\text{`V', `K', `?'}\}^n$ ($\sum n \le 5 \cdot 10^5$), find all periods $d \in [1, n]$ that can be achieved by replacing each `?` with `'V'` or `'K'`.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Testing all $d$ via DSU or harmonic jumps fails when `?` allows multiple incompatible transitive chains, or wait: in a string with wildcards, a period $d$ is invalid **if and only if** there exists a multiple $k d$ ($k \ge 1$) such that some `'V'` at index $i$ and `'K'` at index $j$ satisfy $|i - j| = kd$!
  2. **Combinatorial Word Invariant**: Why must we check all multiples $kd$? Because `?` is not transitive: `'V'` at $1$, `'?'` at $1+d$, `'K'` at $1+2d$ has no direct mismatch at distance $d$, yet forces $S[1] = S[1+d] = S[1+2d]$, a contradiction at distance $2d$! Conversely, if no `'V'` and `'K'` lie in the same residue class modulo $d$ (i.e., no distance $|i - j|$ is a multiple of $d$), we can color each residue class modulo $d$ uniformly!
  3. **Reverse-Engineering Scratchpad**: Compute the difference polynomial $\bigl(\sum_{S[i]=\text{V}} x^i\bigr)\bigl(\sum_{S[j]=\text{K}} x^{n-j}\bigr)$ in 1 FFT to find all forbidden differences $\Delta = |i - j|$, then sieve multiples $d, 2d, 3d, \dots$ in $O(n \log n)$ time!
  4. **Boundary Pitfalls**: Forgetting to check multiples $2d, 3d, \dots$ fails immediately on `V ? K` for $d = 1$.

#### Problem 5B-27: `CF 914E — Palindromes in a Tree` (`[EN]` Codeforces Divide by Zero 2018 E)
- **Inline Mathematical Statement & Constraints**: Given a tree of $N \le 2 \cdot 10^5$ vertices with letters `'a'..'t'` ($|\Sigma| = 20$), for every vertex $v$, count simple paths passing through $v$ whose characters can be rearranged to form a palindrome.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Checking all $O(N^2)$ paths is too slow.
  2. **Combinatorial Word Invariant**: A multiset of characters can be rearranged into a palindrome iff at most one character has odd frequency, i.e., its 20-bit parity mask $M(u, v) = \bigoplus_{w \in \text{path}(u, v)} 2^{c(w)}$ satisfies $\text{popcount}(M(u,v)) \le 1$ ($21$ target masks: $0$ and $2^0, \dots, 2^{19}$).
  3. **Reverse-Engineering Scratchpad**: Run Centroid Decomposition. For centroid $r$, compute root-to-node parity masks, aggregate path counts across subtrees using a frequency array `cnt[1 << 20]`, and propagate path contributions via tree prefix sums (difference array on tree paths to $r$) in $O(N |\Sigma| \log N)$ time.
  4. **Boundary Pitfalls**: Remember to divide paths counted from both endpoints by $2$ at the centroid $r$, while keeping paths starting at $r$ with weight $1$.

---

### Tier 4: Mastery (Grandmaster Synthesis, Internal Periodicity, Deque/Range PAM, Seaweed Matrices & Frontier Reductions — 9 Problems)

#### Problem 5B-28: `[BJWC2018] Border 的四种求法` (`[ZH]` Luogu P4482 / LOJ 2542)
- **Inline Mathematical Statement & Constraints**: Given $S[1..n]$ ($n \le 2 \cdot 10^5$) and $Q \le 2 \cdot 10^5$ queries $(l, r)$, find the longest proper border of the substring $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: KMP is not hereditary on substrings; building KMP for $S[l..r]$ takes $O(r-l)$.
  2. **Combinatorial Word Invariant (Basic Substring Dictionary + Periodic AP Intersection)**:
     Partition candidate border lengths $b \in [1, r-l]$ into $\lceil \log_2(r-l) \rceil$ dyadic intervals $[2^k, 2^{k+1}-1]$. For a fixed $k$, $S[l..l+b-1] = S[r-b+1..r]$ means the prefix of length $2^k$ at $l$ occurs ending at $r - b + 2^k$, and the suffix of length $2^k$ ending at $r$ occurs starting at $l + b - 2^k$. By the Weak Periodicity Lemma, all occurrences of $S[l..l+2^k-1]$ inside a window of length $2^{k+1}$ form **at most ONE arithmetic progression**!
  3. **Reverse-Engineering Scratchpad**: Alternatively (or via Heavy-Light Decomposition on the SAM Link Tree), decompose the ancestor path of $u_r$ into $O(\log n)$ heavy chains; on each heavy chain, valid borders satisfy $\text{endpos}(v) \ge l \text{ and } v - \text{len}(\text{lca}(v, u_r)) + 1 \le l$, answered via 2D Segment Tree / Persistent Segment Tree in $O(n \log^2 n)$.
  4. **Boundary Pitfalls**: Ensure $b < r - l + 1$ (strictly proper border!).

#### Problem 5B-29: `[THUPC 2021] 区间 LCS` (`[ZH]` LOJ 3516 / QOJ / Universal Cup Seaweed Canon)
- **Inline Mathematical Statement & Constraints**: Given two strings $A[1..m]$ and $B[1..n]$ ($m, n \le 10^5$ or $m \le 5000, Q \le 2 \cdot 10^5$), answer $Q$ queries $(l, r)$: compute $\text{LCS}(A, B[l..r])$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Standard LCS takes $O(m(r-l))$ per query.
  2. **Combinatorial Word Invariant (Tiskin's Seaweed Matrix / Unit-Monge Permutation)**:
     In the $(m+1) \times (n+1)$ alignment grid DAG of $A$ and $B$, the highest-scoring paths satisfy the **Monge property** (never cross twice). Represent the cross-differences of $\text{LCS}(A, B[l..r])$ by tracing $m + n$ "seaweeds" entering from the left boundary (indices $-m, \dots, -1$) and top boundary ($0, \dots, n-1$). At cell $(i, j)$:
     - If $A[i] = B[j]$ OR the two entering seaweeds have already crossed earlier, they **do not cross** (pass straight through / bounce).
     - If $A[i] \ne B[j]$ AND the two entering seaweeds have not crossed yet, they **cross**!
     Then $\text{LCS}(A, B[l..r])$ equals $(r - l + 1)$ minus the number of seaweeds that enter at the top in $[l, r]$ and exit at the bottom in $[l, r]$!
  3. **Reverse-Engineering Scratchpad**: Compute the seaweed permutation $P$ in $O(mn)$ (via bit-parallel / naive combing) or $O((m+n)\log^2(m+n))$ (via recursive Russo–Tiskin Unit-Monge multiplication), then answer each query $(l, r)$ as a **2D orthogonal range counting query** (counting $c \in [l, r]$ with $P(c) > r$) using a Persistent Segment Tree / Wavelet Tree in $O(\log n)$ time!
  4. **Boundary Pitfalls**: Seaweeds entering from the left boundary ($-m \dots -1$) start in reverse order of row index so that initially every pair of seaweeds is uncrossed.

#### Problem 5B-30: `Substrings Distinct Palindromes Range Query` (`[ZH]` `[国家集训队论文 2014 — 徐毅]` / `BZOJ 4044` / `QOJ` Range Palindromes)
- **Inline Mathematical Statement & Constraints**: Given $S[1..n]$ ($n \le 10^5$) and $Q \le 10^5$ queries $(l, r)$, count the number of **distinct palindromic substrings** inside $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: A palindrome ending at $i \in [l, r]$ only counts if its length is $\le i - l + 1$, and each distinct palindrome in $S[l..r]$ must be counted **only at its last occurrence** in $[l, r]$.
  2. **Combinatorial Word Invariant (PAM `slink` Periodic Last-Occurrence Compression)**:
     For Offline queries sweeping $r = 1 \dots n$: when advancing to $r$, all palindromic suffixes of $S[1..r]$ have their last occurrence updated to $r$. By the Weak Periodicity Lemma, the palindromic suffixes of $S[1..r]$ form $O(\log r)$ arithmetic progressions (`slink` chains). Within a single `slink` chain $u \to \dots \to \text{slink}(u)$, every palindrome $v$ except the longest one $u$ occurred inside $u$ just $\text{diff}(u)$ positions ago (at $r - \text{diff}(u)$)!
  3. **Reverse-Engineering Scratchpad**: Therefore, updating the last-occurrence starting positions for the entire `slink` chain of $u$ removes a single previous start position $\text{last}(u) - \text{len}(u) + 1$ and adds a single new start position $r - \text{len}(\text{top}(u)) + 1$ in a Fenwick Tree! Store `last[u]` via a Segment Tree over the PAM fail tree, achieving $O((n + Q) \log^2 n)$ time!
  4. **Boundary Pitfalls**: Only the longest palindrome $u$ in the chain uses `last[u]` from the PAM subtree maximum; all shorter members in the same AP had their previous occurrence at exactly $r - \text{diff}(u)$, causing telescopic cancellation inside the chain!

#### Problem 5B-31: `CF 1286E — Fedya the Potter Strikes Back` (`[EN]` Codeforces Round 609 Div. 1 E)
- **Inline Mathematical Statement & Constraints**: Online string $S$ and weight array $W$ built character by character ($n \le 6 \cdot 10^5$, decoded via $\text{ans} \bmod 2^{30}$ and $\text{ans} \bmod 26$). At step $i$, add the sum of $\min_{k \in [i-L+1, i]} W[k]$ over all border lengths $L$ of $S[1..i]$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Must run **strictly online** and maintain the sum of range minimums over all active borders of $S[1..i]$.
  2. **Combinatorial Word Invariant**: As $i-1 \to i$, every border of $S[1..i]$ (except length $1$) is a border of $S[1..i-1]$ of length $L-1$ whose next character $S[L] = S[i]$. On the KMP `pi` chain of $i-1$, skip directly over ancestors $u$ with $S[u+1] = S[i]$ using a precomputed shortcut pointer `anc[u][c]` in $O(\log i)$ amortized deletions!
  3. **Reverse-Engineering Scratchpad**: Maintain a multiset (`std::map<int, int>`) of active border starting positions weighted by their current suffix-minimum $W$ (updated via a monotonic stack on $W$). Each inserted border at $i$ is deleted at most once across the entire algorithm!
  4. **Boundary Pitfalls**: Because the total sum can reach $\approx \frac{n^2}{2} \cdot 2^{30} \approx 2 \cdot 10^{20} > 2^{64}$, accumulate the answer in `__int128`!

#### Problem 5B-32: `CF 1063F — String Journey` (`[EN]` Codeforces Round 516 Div. 1 F)
- **Inline Mathematical Statement & Constraints**: Given $S[1..n]$ ($n \le 5 \cdot 10^5$), find the maximum $k$ such that there exist non-overlapping substrings $t_1, \dots, t_k$ (ordered left-to-right in $S$) with $|t_i| = k - i + 1$ and $t_{i+1}$ a substring of $t_i$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: $t_i$ need not shrink by 1 character from $t_{i-1}$ at the start, only have length $|t_i| = k - i + 1$.
  2. **Combinatorial Word Invariant**: There is always an optimal sequence where $|t_i| = |t_{i+1}| + 1$, meaning $t_{i+1}$ is either the **prefix** $t_i[1..L-1]$ or the **suffix** $t_i[2..L]$ of $t_i$! Moreover, $dp[i]$ (the max $L$ starting at $i$) satisfies $dp[i] \le dp[i+1] + 1$!
  3. **Reverse-Engineering Scratchpad**: Decrease $L$ at most $O(n)$ times overall across $i = n \dots 1$. Before testing whether $L$ is valid at $i$, insert $i + L$ into a Segment Tree over the SAM Link Tree DFS order, and test if the subtree of the SAM node of $S[i..i+L-2]$ or $S[i+1..i+L-1]$ has $\max dp \ge L - 1$.
  4. **Boundary Pitfalls**: Only insert $j = i + L$ into the segment tree as $L$ decreases so that non-overlapping $j \ge i + L$ is strictly enforced!

#### Problem 5B-33: `[十二省联考 2019] 字符串问题` (`[ZH]` Luogu P5284 / LOJ 3052)
- **Inline Mathematical Statement & Constraints**: Given $S$ ($|S| \le 2 \cdot 10^5$), $n_a$ A-substrings $A_i = S[l_{a,i}..r_{a,i}]$, $n_b$ B-substrings $B_j = S[l_{b,j}..r_{b,j}]$, and $m$ directed edges $A_i \to B_j$, plus implicit edges $B_j \to A_i$ whenever $B_j$ is a **prefix** of $A_i$. Find the maximum total length of A-strings on a path (or `-1` if infinite).
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Explicitly adding edges from every $B_j$ to all $A_i$ having $B_j$ as a prefix creates $O(n_a n_b)$ edges.
  2. **Combinatorial Word Invariant**: Build the SAM of $S^R$ (so the Link Tree is the Suffix Tree of $S$, where $u$ is an ancestor of $v$ iff $u$ is a **prefix** of $v$!).
  3. **Reverse-Engineering Scratchpad**: Locate each $A_i$ and $B_j$ on the Link Tree via binary lifting. Sort strings sharing the same SAM node by length (splitting the node into a chain so shorter $B_j$ precedes longer $A_i$ at the same node), then compute longest path on the resulting $O(N + n_a + n_b)$-node DAG via topological sort!
  4. **Boundary Pitfalls**: At a single SAM node containing both $A_i$ and $B_j$ of the **exact same length**, $B_j$ IS a prefix of $A_i$, so when sorting within the node by length, ties must put $B_j$ **before** $A_i$!

#### Problem 5B-34: `Double-Ended Palindromic Tree (Deque PAM)` (`[JA]` / `[ZH]` `QOJ` / `UCup` Deque Palindromes)
- **Inline Mathematical Statement & Constraints**: Maintain a string $D$ under $Q \le 5 \cdot 10^5$ operations: `push_front(c)`, `push_back(c)`, `pop_front()`, `pop_back()`, reporting after each step the number of distinct palindromes and longest palindrome in $D$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Standard PAM relies on amortized fail-chain walks (which break under `pop` or two-sided insertions) and only tracks palindromic suffixes.
  2. **Combinatorial Word Invariant**:
     - By symmetry, adding `c` at the front extends the longest **palindromic prefix**, which equals the longest palindromic suffix when the whole string is a palindrome!
     - Precomputing direct transition links `quick_link[u][c]` (the longest proper palindromic suffix $v$ of $u$ preceded by $c$, i.e., `S[pos - len(v) - 1] == c`) makes finding the fail parent worst-case $O(1)$!
  3. **Reverse-Engineering Scratchpad**: Maintain for each PAM node $u$ a reference counter `cnt[u]` of how many times $u$ is a **surface palindrome** (longest palindromic prefix or suffix of some active position, so `cnt[u] > 0` and has no active fail-child), plus a doubly-ended array of active prefix/suffix longest palindrome pointers.
  4. **Boundary Pitfalls**: When a push creates a palindrome of length $|D|$ (covering the entire deque), **both** `max_pref` and `max_suff` must be updated to point to this new node!

#### Problem 5B-35: `Cartesian-Tree Pattern Matching` (`[EN]` / `[JA]` Park et al. 2019 / `QOJ` / `POI` Cartesian Matching)
- **Inline Mathematical Statement & Constraints**: Given an integer text $T[1..n]$ and pattern $P[1..m]$ ($m \le n \le 5 \cdot 10^5$), find all shifts $i$ such that $T[i..i+m-1]$ has the exact same Cartesian tree shape as $P[1..m]$.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Rebuilding the Cartesian tree for each window takes $O(nm)$; order-isomorphism KMP with a Fenwick tree is both slower ($O(n \log m)$) and solves a stricter relation ($[2, 1, 3]$ and $[3, 1, 2]$ have different relative orders of $2, 3$ but the **exact same** Cartesian tree shape!).
  2. **Combinatorial Word Invariant**: Two arrays $A[1..m]$ and $B[1..m]$ have the same Cartesian tree iff their **Parent-Distance encodings** $\text{PD}[j] = j - \text{left\_parent}(j)$ (or $(j - L(j), j - C(j))$) are identical at every $j \in [1..m]$.
  3. **Reverse-Engineering Scratchpad**: Compute $\text{PD}_P[1..m]$ via a monotonic stack in $O(m)$ time, then run KMP where the equality test at state $q$ maintains a monotonic deque over the active window $[r - q .. r]$, testing whether the clipped parent distance matches $\text{PD}_P[q+1]$ in amortized $O(1)$ time!
  4. **Boundary Pitfalls**: When sliding the left boundary $l = r - q$ rightward during a KMP fallback $q \leftarrow \pi(q)$, any parent index $L(r) < r - q$ becomes out-of-window and must be treated as $0$ (root of the left spine).

#### Problem 5B-36: `Dynamic String LCE & Equality under Split/Concat/Reverse via Locally Consistent Parsing` (`[EN]` / `[JA]` Gawrychowski / `noshi91` / `QOJ` Dynamic Strings)
- **Inline Mathematical Statement & Constraints**: Maintain a string $S$ ($|S| \le 2 \cdot 10^5$) under $Q \le 2 \cdot 10^5$ operations: cut/paste/reverse any substring $S[l..r]$, and query $\text{LCE}(i, j)$ between any two suffixes.
- **4-Step Zero-Magic Analysis**:
  1. **Diagnostic Signal**: Splay / Treap with polynomial rolling hash suffers birthday-paradox collisions when $Q$ LCE binary searches perform $Q \log N$ hash comparisons, or fails when deterministic guarantees are required.
  2. **Combinatorial Word Invariant (Locally Consistent Parsing / Deterministic Coin Tossing)**:
     At each level $h = 0, 1, \dots, O(\log N)$, compress maximal runs $c^k$ into a single RLE symbol $(c, k)$, then color the remaining non-repetitive sequence into blocks of length $2$ or $3$ using the deterministic local minimum/3-coloring of adjacent character IDs (Cole–Vishkin). Because the block boundaries at position $i$ depend only on a radius-$O(\log^* |\Sigma|)$ local neighborhood of $S$, two identical substrings $S[l_1..r_1] = S[l_2..r_2]$ agree on **all internal block boundaries** except $O(1)$ blocks near their endpoints!
  3. **Reverse-Engineering Scratchpad**: Updating a cut/paste operation only recomputes $O(1)$ blocks around the cut point at each of the $O(\log N)$ levels, taking $O(\log^2 N)$ deterministic time per update and $O(\log N)$ for exact LCE!
  4. **Boundary Pitfalls**: Always alternate **RLE compression** (collapsing $c^k$) and **2-3 Block Compression** (collapsing non-repetitive pairs/triples); skipping RLE causes unary strings `aaaaaa...` to have no local minima!

---

### 52.5 Quarantine Table of Excluded Template Problems (`R-5B-01..R-5B-10`)

Per [`AGENTS.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/AGENTS.md) and [`PLAN.md`](file:///home/maomao90/Documents/IO/ICPC-math-notes/strings_research/PLAN.md), the following pure implementation/verification template problems are **strictly excluded** from the textbook difficulty ladders and logged here for quarantine tracking:

| Quarantine ID | Source & Problem Title | Reason for Exclusion |
| :--- | :--- | :--- |
| **`R-5B-01`** | Library Checker — `Suffix Array` | Pure $O(N)$ / $O(N \log N)$ SA construction verification template. |
| **`R-5B-02`** | Library Checker — `Number of Substrings` | Direct formula $\sum (n - SA[i] - LCP[i])$ or $\sum (\text{len}(u) - \text{len}(\text{link}(u)))$ with zero modeling. |
| **`R-5B-03`** | Library Checker — `Z Algorithm` | Bare Z-array output template. |
| **`R-5B-04`** | Library Checker — `Enumerate Palindromes` | Bare Manacher radii array output template. |
| **`R-5B-05`** | Library Checker — `Run Enumerate` | Pure implementation check of Lyndon + LCE Runs enumeration with no downstream problem reduction. |
| **`R-5B-06`** | Library Checker — `Lyndon Factorization` | Direct Duval's algorithm output template. |
| **`R-5B-07`** | Library Checker — `Wildcard Pattern Matching` | Direct 3-FFT Clifford–Clifford formula verification. |
| **`R-5B-08`** | Luogu P3804 — `【模板】后缀自动机 (SAM)` | Standard SAM subtree $\text{endpos}$ size $\times \text{len}(u)$ template. |
| **`R-5B-09`** | Luogu P5496 — `【模板】回文自动机 (PAM)` | Bare online PAM fail-tree depth template. |
| **`R-5B-10`** | Luogu P6139 — `【模板】广义后缀自动机 (广义 SAM)` | Bare Trie-GSAM distinct substring count template. |

---

## Summary of Wave 5B Structural Discoveries & Post-Research Curriculum Impact

1. **Sturmian & Morphic Word Engine (Iter 46)**: Proved the 4-way equivalence of Sturmian words ($p(n)=n+1$, 1-balanced aperiodic, mechanical rotation $s_{\alpha,\rho}$, unique right-special factor), the near-commutativity and central palindrome structure of Fibonacci words $F_k = P_k c_k d_k$, Thue–Morse overlap-freeness and $\bmod 2^{64}$ hash annihilation, and the internal + $(2|P|-2)$ boundary-window decomposition for counting patterns in $\varphi^k(S)$ (`CF 1466G`, `[SDOI2019] 连续子序列`).
2. **Non-Abelian Free-Group & $SL_2(\mathbb{F}_p)$ Stack Hashing (Iter 47)**: Proved why abelian XOR and alternating polynomial hashes fail on crossing/palindrome patterns, and derived both the deterministic Stack-Trie walk ($G = \Asterisk_{c \in \Sigma} (\mathbb{Z}/2\mathbb{Z})$) and trace-zero involutory / $SL_2(\mathbb{F}_p)$ matrix hashes (`CF 1223F`, `AGC 031D`).
3. **Frontier Stringology Additions for Phase 1.5 Restructuring (Iter 48)**: Cataloged **String Attractors $\gamma(S)$**, **$\tau$-Synchronizing Sets**, **Cartesian-Tree Pattern Matching ($\text{PD}_S$ parent-distance KMP)**, **Weighted Strings ($1/z$ Heavy-Light Suffix Tree)**, **2D Periodicity Lattices**, and **LZ77 Primary/Secondary Occurrence Indexing**—all ready for dedicated coverage in `TECHNIQUE_TAXONOMY.md` and `CURRICULUM_ARCHITECTURE.md`.
4. **Master Multilingual Audit & 36-Problem Ladder (Iter 49–52)**: Completed full cross-audits of `[ZH]` `国家集训队论文` (2004–2024), `[JA]` treatises (`noshi91`, `maspypy`, `henkoku`, `tatyam`, `snuke`), and `[EN]` academic/contest canons, alongside 36 fully analyzed non-template problems and 10 quarantined templates (`R-5B-01..R-5B-10`).
