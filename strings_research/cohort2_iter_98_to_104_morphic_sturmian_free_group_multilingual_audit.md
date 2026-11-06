# Cohort 2 Independent Research & Structural Audit Report — Wave 5B (Iterations 98–104): Combinatorics on Words (Sturmian, Morphic, Thue–Morse), Free Group / $SL_2(\mathbb{F}_p)$ Stack Hashing & Master Multilingual Audit

> [!IMPORTANT]
> **Cohort 2 Redundancy & Independence Certification**
> This report (`strings_research/cohort2_iter_98_to_104_morphic_sturmian_free_group_multilingual_audit.md`) was authored independently by Cohort 2 without reading Cohort 1's `iter_46_to_52_morphic_sturmian_free_group_multilingual_audit.md`. Every structural derivation, algebraic invariant, obscure-topic survey, multilingual `[ZH]`/`[JA]`/`[EN]` source audit, and 4-Tier problem ladder entry adheres strictly to the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard** defined in `strings_research/PLAN.md`.

---

## Iteration 98: Sturmian Words, Fibonacci Strings, Thue–Morse & Substitutive Morphisms ($\varphi : \Sigma^* \to \Sigma^*$)

### 98.1 The Diagnostic Signal: Why Naive Simulation of Morphic & Recursive Strings Fails

In competitive programming, recursive strings are generated either by iterating a **substitutive morphism** $\varphi : \Sigma^* \to \Sigma^*$ (where $\varphi(u v) = \varphi(u)\varphi(v)$ for all $u, v \in \Sigma^*$), by concatenation recurrences such as the **Fibonacci strings** $F_0 = \text{b}, F_1 = \text{a}, F_k = F_{k-1} F_{k-2}$ ($k \ge 2$), or by level-indexed insertion rules such as the **Sirens song recurrence** $s_{k} = s_{k-1} + t_k + s_{k-1}$ (`CF 1466G — Song of the Sirens`).

- **What breaks naive structures**: After $k$ steps ($k \le 10^5$ or $k \le 10^{18}$), the expanded string $W_k = \varphi^k(S)$ has length $|\varphi^k(S)| = \Theta(\lambda^k |S|)$ where $\lambda > 1$ is the Perron–Frobenius eigenvalue of the incidence matrix $M_\varphi$ (for Fibonacci strings, $\lambda = \frac{1+\sqrt{5}}{2}$; for Thue–Morse or `CF 1466G`, $\lambda = 2$). Building SAM, Suffix Array, or KMP over $W_k$ explicitly requires $\Omega(\lambda^k)$ time and memory, failing immediately for $k \ge 30$.
- **Diagnostic Triggers in Problem Statements**:
  1. Count occurrences of a query pattern $P$ ($|P| \le 10^5$ or $|P| \le 2000$) inside $\varphi^k(S)$ or $F_k$ for $k \le 10^{18}$.
  2. Compute the number of distinct substrings, Runs, borders, or palindromes in prefix $F_k[1..n]$ ($n \le 10^{18}$) or in the $k$-th Fibonacci/Sturmian word (`[国家集训队论文 2017 — 周任飞] Fibonacci 串性质的研究`).
  3. Determine whether a word avoids fractional powers $w^\alpha$ ($\alpha \ge 2$ or $\alpha > 2$), or construct extremal counterexamples that maximize the number of runs, distinct squares, or KMP/Euclid steps.

---

### 98.2 Combinatorial Word Invariants: Equivalent Characterizations of Sturmian Words

Let $w = w_0 w_1 w_2 \dots \in \{0, 1\}^\omega$ be an infinite binary word, and let $\mathcal{L}_n(w)$ denote the set of distinct contiguous substrings (factors) of length $n$ occurring in $w$. Define the **factor complexity function** $p_w(n) = |\mathcal{L}_n(w)|$.

#### Theorem 98.1 (Morse–Hedlund Theorem, 1940)
For any infinite word $w$, either $p_w(n)$ is strictly increasing with $p_w(n) \ge n + 1$ for all $n \ge 0$, or there exists $n_0$ such that $p_w(n_0) \le n_0$, in which case $p_w(n)$ is bounded and $w$ is **ultimately periodic** ($w = u v^\omega$).

*4-Step Zero-Magic Proof (Right-Special Factors)*:
1. **Concrete Objects**: For $u \in \mathcal{L}_n(w)$, define its right-degree $d^+(u) = |\{c \in \Sigma : u c \in \mathcal{L}_{n+1}(w)\}|$. Every factor of length $n$ has $d^+(u) \ge 1$ because $w$ is infinite. A factor $u \in \mathcal{L}_n(w)$ is **right-special** if $d^+(u) \ge 2$.
2. **Double-Counting Identity**: Each factor of length $n+1$ is obtained by appending one character to its length-$n$ prefix, so:
   $$p_w(n+1) - p_w(n) = \sum_{u \in \mathcal{L}_n(w)} (d^+(u) - 1)$$
3. **Propagation of Special Factors**: If $p_w(n+1) = p_w(n)$ for some $n$, then $d^+(u) = 1$ for *every* $u \in \mathcal{L}_n(w)$. That means every length-$n$ factor in $w$ uniquely determines the next character! In the De Bruijn graph of order $n$ restricted to $\mathcal{L}_n(w)$, every vertex has out-degree $1$. Since $|\mathcal{L}_n(w)|$ is finite, the infinite walk traced by $w$ must eventually enter a simple cycle, making $w$ ultimately periodic.
4. **Minimality**: Since $p_w(0) = 1$ (the empty word $\epsilon$), if $w$ is aperiodic then $p_w(n+1) - p_w(n) \ge 1$ for all $n \ge 0$, yielding $p_w(n) \ge n + 1$. $\blacksquare$

#### Theorem 98.2 (Six Equivalent Characterizations of Sturmian Words)
An infinite binary word $w \in \{0, 1\}^\omega$ is **Sturmian** if it satisfies any (and hence all) of the following equivalent properties:

1. **Minimal Aperiodic Complexity**: $p_w(n) = n + 1$ for every $n \ge 0$. Equivalently, for every length $n \ge 0$, $w$ contains **exactly one right-special factor** $R_n$ (so $R_n 0, R_n 1 \in \mathcal{L}_{n+1}(w)$) and **exactly one left-special factor** $L_n$ (so $0 L_n, 1 L_n \in \mathcal{L}_{n+1}(w)$).
2. **Balance Property**: $w$ is aperiodic and **1-balanced**: for any two factors $u, v \in \mathcal{L}_n(w)$ of the same length $n$, their Hamming weights ($|u|_1$ and $|v|_1$) differ by at most $1$:
   $$\big| |u|_1 - |v|_1 \big| \le 1$$
3. **Mechanical / Irrational Circle Rotation Words**: There exist an irrational slope $\alpha \in (0, 1) \setminus \mathbb{Q}$ and an intercept $\rho \in [0, 1)$ such that $w$ is either the lower mechanical word $s_{\alpha, \rho}$ or upper mechanical word $s'_{\alpha, \rho}$:
   $$s_{\alpha, \rho}(n) = \lfloor (n+1)\alpha + \rho \rfloor - \lfloor n\alpha + \rho \rfloor, \qquad s'_{\alpha, \rho}(n) = \lceil (n+1)\alpha + \rho \rceil - \lceil n\alpha + \rho \rceil$$
   When $\rho = 0$, the suffix starting at $n=1$ is the **characteristic Sturmian word** $c_\alpha$ of slope $\alpha$.
4. **Cutting Sequences on the Square Grid**: $w$ encodes the sequence of horizontal ($0$) and vertical ($1$) grid lines crossed by a ray $y = \frac{\alpha}{1-\alpha} x + \rho'$ of irrational slope in $\mathbb{R}_{\ge 0}^2$.
5. **Standard Sturmian Words & Continued Fractions**: If $\alpha = [0; d_1 + 1, d_2, d_3, \dots]$ is the simple continued fraction of $\alpha \in (0, 1) \setminus \mathbb{Q}$, define the **directive sequence** $(s_k)_{k \ge -1}$ by:
   $$s_{-1} = 1, \quad s_0 = 0, \quad s_1 = s_0^{d_1} s_{-1}, \quad s_k = s_{k-1}^{d_k} s_{k-2} \quad (k \ge 2)$$
   Then $c_\alpha = \lim_{k \to \infty} s_k$. The finite words $s_k$ are called **standard words**.
6. **Palindromic Central Words (de Luca's Characterization)**: Every standard word $s_k$ ($k \ge 1$) has the form $s_k = \pi_k a b$ where $\{a, b\} = \{0, 1\}$ and $\pi_k$ is a **central word**—a palindrome of length $|s_k| - 2$ that has two coprime periods $p = |s_{k-1}|$ and $q = |s_{k-2}|$ satisfying $|\pi_k| = p + q - 2 = p + q - \gcd(p, q) - 1$.

*Why Characterization 3 $\implies$ Characterization 1 & 6 (Concrete Alignment Proof)*:
- In the circle $\mathbb{R}/\mathbb{Z}$, a factor $u = u_0 u_1 \dots u_{n-1}$ of length $n$ occurs at position $i$ iff $\{i\alpha + \rho\}$ falls into the half-open interval $I(u) = \bigcap_{j=0}^{n-1} T^{-j}(I_{u_j})$, where $T(x) = \{x + \alpha\}$, $I_0 = [0, 1-\alpha)$, and $I_1 = [1-\alpha, 1)$.
- The $n+1$ endpoints of these intervals are the fractional parts $\{-j\alpha\} \pmod 1$ for $j = 0, 1, \dots, n$. Because $\alpha$ is irrational, these $n+1$ points on the unit circle are **pairwise distinct**!
- $n+1$ distinct points partition the unit circle $\mathbb{R}/\mathbb{Z}$ into **exact $n+1$ elementary intervals**. By Kronecker's density theorem, the orbit $\{i\alpha + \rho\}_{i \ge 0}$ is dense in $\mathbb{R}/\mathbb{Z}$, so it visits every one of the $n+1$ intervals. Thus $|\mathcal{L}_n(w)| = n + 1$.
- Furthermore, when moving from length $n$ to $n+1$, the single new point $\{-(n+1)\alpha\}$ splits **exactly one** existing interval into two—which corresponds to the unique right-special factor $R_n$ splitting into $R_n 0$ and $R_n 1$!
- By symmetry of the rotation $T$ and $T^{-1}$, $L_n = R_n^R$. Since $c_\alpha$ starts with every left-special factor $L_n$, a factor $u$ is a prefix of $c_\alpha$ iff $u^R$ is right-special. When $u = \pi_k$ is both left-special and right-special (a **bispecial factor**), $\pi_k = \pi_k^R$ is a palindrome of length $|s_{k-1}| + |s_{k-2}| - 2$, achieving the exact **Fine–Wilf extremal bound**!

---

### 98.3 Deep Anatomy of the Fibonacci Word & Zeckendorf Numeration (`[国家集训队论文] Fibonacci 串`)

When $\alpha = \frac{3 - \sqrt{5}}{2} = 2 - \phi = [0; 2, 1, 1, 1, \dots]$ (or its complement $\frac{1}{\phi} = \frac{\sqrt{5}-1}{2} = [0; 1, 1, 1, \dots]$), all partial quotients are $d_k = 1$. This generates the **Fibonacci words**:
$$F_1 = \text{b}, \quad F_2 = \text{a}, \quad F_3 = \text{ab}, \quad F_4 = \text{aba}, \quad F_5 = \text{abaab}, \quad F_6 = \text{abaababa}, \quad F_k = F_{k-1} F_{k-2}$$
where $|F_k| = f_k$ ($f_1 = 1, f_2 = 1, f_3 = 2, f_4 = 3, f_5 = 5, f_6 = 8, \dots$). They are fixed points of the **Fibonacci morphism** $\varphi(\text{a}) = \text{ab}$, $\varphi(\text{b}) = \text{a}$.

#### Five Fundamental Structural Properties of $F_k$ (Zhou Renfei, IOI 2017 China National Team Paper)

1. **Near-Commutativity Law (Swap of Last Two Characters)**:
   For every $k \ge 3$, define $\pi_k$ by removing the last two characters of $F_k$. Then:
   $$F_k = \begin{cases} \pi_k \text{ab} & \text{if } k \text{ is odd} \\ \pi_k \text{ba} & \text{if } k \text{ is even} \end{cases}$$
   and the reversed concatenation $F_{k-2} F_{k-1}$ differs from $F_k = F_{k-1} F_{k-2}$ **only in the last two characters**:
   $$F_{k-1} F_{k-2} = \pi_k x y \iff F_{k-2} F_{k-1} = \pi_k y x$$
   Moreover, $\pi_k$ is a palindrome ($\pi_k = \pi_k^R$) of length $f_k - 2 = f_{k-1} + f_{k-2} - 2$.
   *Hand-checkable example ($k=6$)*: $F_5 F_4 = \text{abaab} + \text{aba} = \text{abaababa} = \underline{\text{abaaba}}\text{ba}$, while $F_4 F_5 = \text{aba} + \text{abaab} = \underline{\text{abaaba}}\text{ab}$. Here $\pi_6 = \text{abaaba}$ is a palindrome of length $6 = 5 + 3 - 2$ with periods $5$ and $3$, but period $\gcd(5, 3) = 1$ fails!

2. **Zeckendorf / Ostrowski Numeration Characterization**:
   Every non-negative integer $n \ge 0$ has a unique **Zeckendorf representation** $n = \sum_{i \ge 2} \epsilon_i f_i$ with $\epsilon_i \in \{0, 1\}$ and no two adjacent $1$s ($\epsilon_i \epsilon_{i+1} = 0$). Then the $0$-indexed $n$-th character of $F_\infty = \text{abaababaabaab}\dots$ is determined solely by the least significant digit $\epsilon_2$:
   $$F_\infty[n] = \begin{cases} \text{a} & \text{if } \epsilon_2(n) = 0 \\ \text{b} & \text{if } \epsilon_2(n) = 1 \end{cases}$$
   Equivalently, using $1$-based indexing $n \ge 1$, $F_\infty[n] = \text{a}$ iff $\lfloor (n+1)/\phi \rfloor - \lfloor n/\phi \rfloor = 1$.

3. **Singular Words ($\text{Sing}_k$) & Rytter's Compact Suffix / DAWG Structure**:
   Define the $k$-th **singular word** $w_k$ by inverting the last character of $\pi_{k+2}$ (equivalently, $w_1 = \text{a}, w_2 = \text{b}, w_3 = \text{aa}, w_4 = \text{bab}, w_5 = \text{aabaa}, \dots$, where $|w_k| = f_k$ and $w_k$ is a palindrome).
   - Every factor of $F_\infty$ of length $f_k$ is a cyclic shift of $F_k$, except for $w_k$ which occurs without wrap-around.
   - All factors of $F_\infty$ are partitioned into disjoint **singular blocks**; the Suffix Automaton (SAM) and Palindromic Tree (PAM) of $F_k$ have a chain-with-shortcuts topology of size $O(k)$ after compressing degree-1 paths (Compact DAWG / Rytter 2006), allowing substring / palindrome / run queries on prefixes $F_k[1..n]$ ($n \le 10^{18}$) in $O(k) = O(\log n)$ time!

4. **Fourth-Power Freeness & Exact Fractional Exponent Spectrum**:
   $F_\infty$ contains **no fourth powers** ($u^4$). Its maximal critical exponent is $2 + \phi = \frac{5+\sqrt{5}}{2} \approx 3.618$, achieved by prefixes of the form $F_k^2 \pi_k = F_k F_k F_{k-1}\dots$ where $|F_k^2 \pi_k| / |F_k| = 2 + \frac{f_k - 2}{f_k} \to 2 + \frac{1}{\phi} + 1 = 2 + \phi$.
   - The squares in $F_\infty$ are **exclusively** cyclic shifts of $F_k^2$ for $k \ge 2$!
   - In particular, $F_k$ has exactly $f_{k-2}$ distinct square factors, and the Runs of $F_k$ are in 1-to-1 correspondence with sub-occurrences of singular words $w_j$.

5. **Extremal Run & Border Complexity**:
   Because every bispecial factor $\pi_j$ spawns a periodic run of period $f_{j-1}$, Fibonacci and Sturmian words are the **unique extremal worst-case inputs** for:
   - KMP failure-link hops ($\Theta(\log |S|)$ hops at index $f_k - 1$),
   - Number of Border AP blocks in $S[1..r]$,
   - Ratio of Runs $\rho(n)/n \to \approx 0.944575$ (and sum of exponents $\sum \text{exp}(R)/n$),
   - Distinct palindromes (achieving the Droubay–Pirillo upper bound $N + 1$ for every prefix!).

---

### 98.4 The Thue–Morse Word ($\mu$: $0 \mapsto 01, 1 \mapsto 10$) and Overlap-Freeness

Define the **Thue–Morse morphism** $\mu : \{0, 1\}^* \to \{0, 1\}^*$ by $\mu(0) = 01$ and $\mu(1) = 10$. Iterating from $0$ yields:
$$T_0 = 0, \quad T_1 = 01, \quad T_2 = 0110, \quad T_3 = 01101001, \quad T_4 = 0110100110010110, \dots$$
where $T_\infty = \lim_{k \to \infty} \mu^k(0)$.

#### Key Combinatorial Invariants of $T_\infty$
1. **Popcount Parity Formula ($O(1)$ Character Lookup)**:
   For any $n \ge 0$ (0-indexed), $T_\infty[n] = \text{popcount}(n) \bmod 2$.
   *Proof*: $\mu$ replaces each bit at index $m$ with two bits at $2m$ and $2m+1$: $T_\infty[2m] = T_\infty[m]$ and $T_\infty[2m+1] = 1 - T_\infty[m]$, matching the recurrence of $\text{popcount}(n) \bmod 2$.
2. **Overlap-Freeness (Thue, 1906)**:
   $T_\infty$ is **overlap-free**—it contains no factor of the form $c u c u c$ where $c \in \{0, 1\}$ and $u \in \{0, 1\}^*$ (i.e., no fractional power of exponent $> 2$, and no cube $w^3$).
   *Zero-Magic Parity Alignment Proof*:
   - Suppose for contradiction $w = c u c u c$ is a shortest overlap in $T_\infty$, occurring at index $i$ with period $p = |cu| \ge 1$.
   - **Case 1 ($p = 2q$ is even)**: Regardless of whether $i$ is even or odd, grouping adjacent aligned pairs $(2m, 2m+1)$ inside $T_\infty$ shows that every aligned block of length $2$ is in $\{01, 10\}$. If $i$ is even, $w$ is the image under $\mu$ of a factor $w'$ of length $2q + 1$ starting with the same character at $0, q, 2q$— wait: the character at $i + 2q$ is determined by $T_\infty[i + 2q] = c$, so the pre-image $\mu^{-1}$ has length $q + 1$ repeated twice plus one character, forming a shorter overlap $c' u' c' u' c'$ of period $q = p/2 < p$, contradicting minimality! If $i$ is odd, prepending $T_\infty[i-1] = 1-c$ (which must equal $T_\infty[i+2q-1]$ because $T_\infty[i-1]T_\infty[i], T_\infty[i+2q-1]T_\infty[i+2q] \in \{01, 10\}$ share their second character $c$) shifts the overlap to even index $i-1$, reducing to the even case.
   - **Case 2 ($p$ is odd)**: If $p = 1$, $c u c u c = c c c$, which is impossible since any 3 consecutive characters span a block $01$ or $10$ and its neighbor, never $000$ or $111$. If $p \ge 3$ is odd, the factor $c u c u c$ has length $2p + 1 \ge 7$. In $T_\infty$, $00$ and $11$ can only occur starting at **odd** indices (crossing the boundary between $\mu(x)$ and $\mu(y)$). Yet in $c u c u c$, any occurrence of $00$ or $11$ in $c u$ at position $j$ repeats at $j + p$; since $p$ is odd, $j$ and $j+p$ have *opposite* parities! Thus $c u$ cannot contain $00$ or $11$ at all, forcing $c u c u c$ to be alternating $01010\dots$, which fails in $T_\infty$ for length $\ge 5$ (since $01010$ contains $0101$ starting at an even or odd index, forcing pre-image $00$ or $11$ and next bit flip). $\blacksquare$
3. **Tarry–Escott Equal-Power-Sum Identity**:
   Partition $[0, 2^k - 1]$ into $A_k = \{n : T_\infty[n] = 0\}$ and $B_k = \{n : T_\infty[n] = 1\}$. Then for every polynomial $P(x)$ of degree $\le k - 1$:
   $$\sum_{n \in A_k} P(n) = \sum_{n \in B_k} P(n)$$
   *Proof*: Let $\Delta(x) = \sum_{n=0}^{2^k-1} (-1)^{T_\infty[n]} z^n = \prod_{j=0}^{k-1} (1 - z^{2^j})$. Since $(1-z)^k \mid \Delta(z)$, the first $k-1$ derivatives of $\Delta(z)$ vanish at $z = 1$.

---

### 98.5 Algorithmic Compilation: Counting Pattern Occurrences in Morphic & Recursive Strings

#### Paradigm A: Matrix Exponentiation over Boundary-Straddling Windows ($\varphi^k(S)$ for $k \le 10^{18}$)

Suppose we want to count occurrences of a pattern $P$ ($|P| = m$) in $\varphi^k(S)$ where $k \le 10^{18}$.

1. **The Reverse-Engineering Scratchpad**:
   When a string $W$ is decomposed into blocks $W = B_1 B_2 \dots B_r$, every occurrence of $P$ in $W$ is either:
   - Strictly inside some block $B_i$, OR
   - Straddling a boundary between $B_i$ and $B_{i+1}$ (assuming $|B_i| \ge m - 1$; if blocks can be shorter, we first replace $\varphi$ by $\varphi^{k_0}$ where $k_0 = O(\log m)$ so that $|\varphi^{k_0}(c)| \ge m - 1$ for every non-erasing growing letter $c$).
2. **Boundary Window Compression**:
   Any occurrence of $P$ straddling the junction $B_i B_{i+1}$ must start within the last $m - 1$ characters of $B_i$ and end within the first $m - 1$ characters of $B_{i+1}$. Thus it is completely determined by:
   $$\text{suff}_{m-1}(B_i) + \text{pref}_{m-1}(B_{i+1})$$
   which is a string of length at most $2m - 2$!
3. **Two Dual State-Space Compilations**:
   - **Method 1 (2-Letter / Junction Incidence Matrix — Best when $|\Sigma|$ is small and $m \le 10^5$)**:
     For each letter $c \in \Sigma$, once $k \ge k_0$ (so $|\varphi^{k_0}(c)| \ge m - 1$), the length-$(m-1)$ prefix $L(c, k) = \text{pref}_{m-1}(\varphi^k(c))$ and length-$(m-1)$ suffix $R(c, k) = \text{suff}_{m-1}(\varphi^k(c))$ become **periodic** (typically period $1$ or $2$ in $k$).
     Even simpler: every junction in $\varphi^k(S)$ between two level-$k_0$ blocks $\varphi^{k_0}(a)$ and $\varphi^{k_0}(b)$ comes from an adjacent pair of characters $a b$ occurring in $\varphi^{k - k_0}(S)$!
     Therefore, we only need to count how many times each length-1 letter $a \in \Sigma$ and each length-2 factor $ab \in \Sigma^2$ occurs in $\varphi^{k - k_0}(S)$!
     - Each letter $a$ maps to $\varphi(a)$, creating internal pairs $(x_i, x_{i+1})$ inside $\varphi(a)$.
     - Each adjacent pair $ab$ creates the single cross-boundary pair $(\text{last}(\varphi(a)), \text{first}(\varphi(b)))$.
     This is a linear recurrence of dimension $|\Sigma| + |\Sigma|^2$, solved in $O((|\Sigma|^2)^3 \log k + |\Sigma|^2 m)$ time!
   - **Method 2 (KMP Automaton Homomorphic Matrix — General Non-Uniform Recurrences)**:
     Each string $W$ defines a transition map $f_W : \{0, 1, \dots, m-1\} \to \{0, 1, \dots, m-1\} \times \mathbb{Z}_{\ge 0}$ on the KMP automaton of $P$, mapping starting state $q$ to $(\delta^*(q, W), \text{matches}(q, W))$. In tropical or linear algebra, $f_W$ is represented by an $(m+1) \times (m+1)$ matrix $M(W)$ where:
     $$M(W)_{q, q'} = [q' = \delta^*(q, W)], \qquad M(W)_{q, m} = \text{matches}(q, W), \qquad M(W)_{m, m} = 1$$
     Since $M(U V) = M(U) M(V)$, for any morphism or recurrence $W_k = W_{k-1} W_{k-2}$, we simply compute $M(W_k) = M(W_{k-1}) M(W_{k-2})$ in $O(m^2)$ or $O(m)$ time (exploiting that lines $0 \dots m-1$ of $M(W)$ each have a single $1$!).

#### Paradigm B: Recursive Halving & KMP Border Filtration (`CF 1466G — Song of the Sirens`)

In `CF 1466G`, $s_0$ is given ($|s_0| \le 100$) and $s_{i} = s_{i-1} + t_i + s_{i-1}$ for $1 \le i \le n$ ($n \le 10^5$), and we are given queries $(k, w)$ asking for the number of occurrences of $w$ ($|w| \le 10^6$) in $s_k$ modulo $10^9 + 7$.

*Step-by-Step Reverse-Engineering*:
1. **Phase 1 (Base Expansion up to $|s_{k_0}| \ge |w|$)**:
   While $k_0 < k$ and $|s_{k_0}| < |w|$, explicitly construct $s_{k_0 + 1} = s_{k_0} + t_{k_0 + 1} + s_{k_0}$. Since $|s_{k_0}|$ doubles each step, this takes at most $\lceil \log_2(|w|/|s_0|) \rceil$ steps and builds a string $s_{k_0}$ of length $< 2|w| + 1$.
2. **Phase 2 (Single-Pivot Straddling Decomposition for $i > k_0$)**:
   Once $|s_{k_0}| \ge |w|$, in every higher level $s_i = s_{i-1} + t_i + s_{i-1}$ ($k_0 < i \le k$), the two copies of $s_{i-1}$ have length $\ge |w|$. Therefore, no occurrence of $w$ can span *both* the left $s_{i-1}$ and the right $s_{i-1}$ across $t_i$ and another $t_j$!
   Every occurrence of $w$ in $s_k$ is either:
   - Completely inside one of the $2^{k - k_0}$ copies of $s_{k_0}$ (contributing $2^{k - k_0} \cdot \text{occ}(w, s_{k_0})$), OR
   - Centered across the single character $t_i$ at some level $i \in [k_0 + 1, k]$, flanked immediately by $\text{suff}_{|w|-1}(s_{i-1})$ on the left and $\text{pref}_{|w|-1}(s_{i-1})$ on the right.
3. **Invariant of the Flanking Windows**:
   Because $|s_{k_0}| \ge |w| - 1$ and $s_{i-1}$ both starts and ends with $s_{k_0}$, for **every** $i > k_0$:
   $$\text{suff}_{|w|-1}(s_{i-1}) = \text{suff}_{|w|-1}(s_{k_0}) =: L, \qquad \text{pref}_{|w|-1}(s_{i-1}) = \text{pref}_{|w|-1}(s_{k_0}) =: R$$
   Notice that $L$ and $R$ **do not depend on $i$**!
4. **Reduction to Weighted Character Sums**:
   For each character $c \in \{\text{'a'}, \dots, \text{'z'}\}$, any level $i \in [k_0 + 1, k]$ with $t_i = c$ spawns $2^{k - i}$ copies of the straddling window $L + c + R$, contributing $2^{k - i} \cdot \text{occ}(w, L + c + R)$.
   Using KMP / Z-algorithm on $w$ against $s_{k_0}$, we can find in $O(|w|)$ time which alignment splits $w = u + c + v$ satisfy $u$ is a suffix of $s_{k_0}$ (via KMP on $w$ and $s_{k_0}$) and $v$ is a prefix of $s_{k_0}$ (via KMP on $w^R$ and $s_{k_0}^R$). Then we sum $\sum_{i = k_0 + 1}^k [t_i = c] 2^{k - i}$ in $O(1)$ per character $c$ using precomputed prefix sums $\text{pref\_cnt}[i][c] = \sum_{j=1}^i [t_j = c] 2^{-j} \pmod{10^9 + 7}$!
   Total time per query: $O(|s_0| + |w| + |\Sigma|)$, independent of $k$!

---

### 98.6 Boundary Pitfalls & Broken-Invariant Counterexamples (Iter 98)

1. **Pitfall 1: Assuming $|\varphi^{k_0}(c)| \ge |P| - 1$ holds after $O(\log |P|)$ steps for mortal or unit-growth characters**.
   - *Counterexample*: Consider $\varphi(\text{a}) = \text{ab}$, $\varphi(\text{b}) = \text{b}$. Here $|\varphi^k(\text{b})| = 1$ for all $k$, so $\varphi^{k_0}(\text{b})$ never reaches length $|P| - 1$. A pattern $P$ can span across arbitrarily many consecutive $\text{b}$'s!
   - *Fix*: Use the KMP Automaton Matrix $M(\varphi^k(c)) \in \mathbb{Z}^{(m+1) \times (m+1)}$ (or its functional representation $\delta^*(q, \varphi^k(c))$) rather than fixed-window boundary slicing whenever $\varphi$ is not strictly expanding on all characters.
2. **Pitfall 2: Off-by-one in Zeckendorf vs. Golden Ratio floor for Fibonacci Strings**.
   - *Counterexample*: For $\alpha = \frac{\sqrt{5}-1}{2}$, the mechanical sequence $\lfloor (n+1)\alpha \rfloor - \lfloor n\alpha \rfloor$ at $n = 0$ gives $0$ ($\text{b}$), whereas the standard Fibonacci word $F_\infty = \text{abaababa}\dots$ starts at $n = 1$! Confusing $0$-based $s_{\alpha, 0}(0)$ with $1$-based $c_\alpha(1)$ shifts every query range $[l, r]$ by $1$ and corrupts palindrome centers.

---

## Iteration 99: Free Group Word Reduction & Non-Abelian Matrix Hashing ($SL_2(\mathbb{F}_p)$) for Stack/Bracket Cancellation

### 99.1 The Diagnostic Signal: Why Polynomial Rolling Hash Fails on Stack-Cancellation Languages

Consider problems where adjacent identical characters annihilate (`AA` $\to \epsilon$, as in `CF 1223F — Stack Exterminable Arrays`, `AGC 050 C — Block Game`, `ABC 250 G` / bracket elimination variants) or where inverse pairs annihilate (`aA` $\to \epsilon, \text{Aa} \to \epsilon$, free group reduction).

- **What breaks Polynomial Rolling Hash**:
  Standard polynomial rolling hash represents a string $S = s_1 s_2 \dots s_n$ via the affine map $h_c(x) = B x + v_c \pmod P$, which embeds $\Sigma^*$ into the triangular matrix monoid $\begin{pmatrix} B & v_c \\ 0 & 1 \end{pmatrix}$. In this monoid:
  $$h_c(h_c(x)) = B^2 x + (B + 1) v_c \not\equiv x \pmod P$$
  unless $B \equiv -1 \pmod P$. However, if $B \equiv -1 \pmod P$, then the hash reduces to an **alternating sum** $\sum_{i=1}^n (-1)^{i} v_{s_i}$, which is **abelian on even-spaced positions**:
  $$\text{Hash}(\text{ABAB}) = v_A - v_B + v_A - v_B = 2(v_A - v_B) \neq \text{Hash}(\epsilon) = 0$$
  Wait—even worse: for $B = -1$, $\text{Hash}(\text{ABBA}) = v_A - v_B + v_B - v_A = 0$ (correct), AND $\text{Hash}(\text{ABAB})$ is non-zero, **WAIT**: what about $\text{Hash}(\text{AB C BA})$ vs $\text{Hash}(\text{C})$? With $B = -1$, $\text{Hash}(\text{ABCBA}) = v_A - v_B + v_C - v_B + v_A = 2v_A - 2v_B + v_C \neq v_C$!
  And what about $\text{Hash}(\text{ABC A B C})$? In alternating sum:
  $$\text{Hash}(\text{ABCABC}) = (v_A - v_B + v_C) - (v_A - v_B + v_C) = 0 = \text{Hash}(\epsilon)$$
  even though $\text{ABCABC}$ has **zero** adjacent equal characters and is completely irreducible!
- **Why**: Any commutative (abelian) group or 1D alternating group has relations $xyzxyz = 1$ or $xy = yx$, creating catastrophic structural collisions on strings like `ABCABC` or `ABACABA`.

---

### 99.2 The Combinatorial & Algebraic Invariant: The Coxeter Group $(\mathbb{Z}_2)^{*|\Sigma|}$, the Free Group $F_{|\Sigma|}$, and $SL_2(\mathbb{F}_p)$

#### 1. Exact Algebraic Models of Stack Cancellation
- **Adjacent Equal-Character Cancellation (`AA` $\to \epsilon$)**:
  The equivalence classes of words over $\Sigma$ under $c c \leftrightarrow \epsilon$ form the **universal Coxeter group** (free product of $|\Sigma|$ copies of $\mathbb{Z}_2$):
  $$G_{\text{stack}} = \langle \Sigma \mid c^2 = 1 \text{ for all } c \in \Sigma \rangle \cong \underbrace{\mathbb{Z}_2 * \mathbb{Z}_2 * \dots * \mathbb{Z}_2}_{|\Sigma| \text{ times}}$$
  By **Normal Form for Free Products**, every element $g \in G_{\text{stack}}$ has a **unique reduced word** (containing no adjacent equal letters $cc$), and a substring $S[l..r]$ is **stack-exterminable** (reduces to $\epsilon$ via a stack) if and only if its image in $G_{\text{stack}}$ equals the identity $1_G$!
  Since every generator satisfies $c^{-1} = c$, for prefix products $P_r = s_1 s_2 \dots s_r \in G_{\text{stack}}$:
  $$S[l..r] =_G 1_G \iff P_{l-1}^{-1} P_r = 1_G \iff P_{l-1} = P_r$$
- **Symmetric Bracket / Free Group Cancellation (`aA` $\to \epsilon, \text{Aa} \to \epsilon$)**:
  The equivalence classes under $c \bar{c} = \bar{c} c = \epsilon$ form the **Free Group** $F_{|\Sigma|}$. Again, by Schreier/Nielsen-reduced word uniqueness, $S[l..r] =_{F_{|\Sigma|}} 1 \iff P_{l-1} = P_r$.

#### 2. Non-Abelian Matrix Hashing in $SL_2(\mathbb{F}_p)$ (or $PGL_2(\mathbb{F}_p)$)
Why does $SL_2(\mathbb{F}_p)$ avoid the `ABCABC` collision of abelian/alternating hashes?
- **Sanov's Theorem & Free Subgroups of $SL_2(\mathbb{Z})$**: The matrices $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}$ generate a **free group** of rank $2$ inside $SL_2(\mathbb{Z})$. By taking random matrices in $SL_2(\mathbb{F}_p)$ for a large prime $p \approx 10^9 + 7$, there are **no low-degree polynomial identities** satisfied by generic matrices of $SL_2(\mathbb{F}_p)$ (unlike $1 \times 1$ matrices which satisfy $AB - BA = 0$).
- **Constructing Involutions ($M_c^2 = I$) for `AA` $\to \epsilon$**:
  By the **Cayley–Hamilton Theorem**, any $2 \times 2$ matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ satisfies:
  $$M^2 - \text{tr}(M) M + \det(M) I = 0$$
  Therefore, if we choose:
  $$\text{tr}(M_c) = a + d \equiv 0 \pmod p \quad \text{and} \quad \det(M_c) = a d - b c \equiv -1 \pmod p$$
  then $M_c^2 = 0 \cdot M_c - (-1) I = I \pmod p$ for **every** choice of $a, b, c$!
  Explicitly, to generate a random involution $M_c \in GL_2(\mathbb{F}_p)$ with $M_c^2 = I$:
  1. Pick $a \in \mathbb{F}_p$ and $b \in \mathbb{F}_p^\times$ uniformly at random.
  2. Set $d = -a \pmod p$ and $c = (1 - a^2) b^{-1} \pmod p$.
  3. Then:
     $$M_c = \begin{pmatrix} a & b \\ (1 - a^2)b^{-1} & -a \end{pmatrix} \implies M_c^2 = \begin{pmatrix} a^2 + 1 - a^2 & ab - ab \\ \dots & 1 - a^2 + a^2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$
  *(Or in projective form $M_c^2 = \lambda_c I$, pick $\text{tr}(M_c) = 0$ and normalize prefix matrices, or simply use $\det(M_c) = -1$ as above so $M_c^2 = I$ holds strictly with zero scalar normalization!)*
- **Error Probability (Schwartz–Zippel on Non-Commutative Word Equations)**:
  If $W = s_l \dots s_r$ has a non-empty reduced word $w_1 w_2 \dots w_k$ ($w_i \neq w_{i+1}$, $k \ge 1$), then the entries of $\prod_{i=1}^k M_{w_i} - I$ are non-zero rational functions (after clearing $b_c^{-1}$, polynomials of degree $\le 2k$) in the independent random variables $(a_c, b_c)_{c \in \Sigma}$. By the **Schwartz–Zippel Lemma**, the probability that a non-trivial reduced word of length $k \le N$ evaluates to $I \pmod p$ is at most $\frac{2N}{p}$. Using a single prime $p \approx 10^9 + 7$ (or a pair of primes / $3 \times 3$ involuntary matrices) makes the collision probability $\le (2N/p)^2 \approx 4 \cdot 10^{-8}$.

---

### 99.3 Deterministic Counterpart: Dynamic Stack-Tree (Trie Walk) & Transition Table (`CF 1223F`)

While $SL_2(\mathbb{F}_p)$ matrix hashing is indispensable when substrings are **concatenated across segments, reversed, or modified in a segment tree** (where each segment node stores the $2 \times 2$ matrix product $M_{l..r}$ in $O(1)$ space), for static or offline prefix-reduction queries we also have a **100% deterministic $O(N \log N)$ or $O(N)$ Trie Walk**:

1. **The Stack-State Trie Invariant**:
   Imagine feeding $s_1, s_2, \dots, s_n$ into a stack one by one. Let $\text{red}(S[1..i])$ be the reduced string remaining on the stack after step $i$.
   - Every reduced string $\text{red}(S[1..i])$ is a node $u_i$ in a rooted Trie $\mathcal{T}$ (initially at root $u_0 = \text{root}$).
   - When processing $s_i = c$ at node $u_{i-1}$:
     - If $u_{i-1} \neq \text{root}$ and the edge from $\text{parent}(u_{i-1})$ to $u_{i-1}$ has label $c$, the character $c$ **pops** the top of the stack: $u_i = \text{parent}(u_{i-1})$!
     - Otherwise, $c$ **pushes** onto the stack: $u_i = \text{child}(u_{i-1}, c)$ (creating the child node if it does not exist).
2. **Exact Equivalence**:
   $$S[l..r] \text{ is stack-exterminable} \iff \text{red}(S[1..l-1]) = \text{red}(S[1..r]) \iff u_{l-1} = u_r$$
   Counting stack-exterminable substrings is simply counting pairs $0 \le l-1 < r \le n$ with $u_{l-1} = u_r$:
   $$\text{Ans} = \sum_{u \in \mathcal{T}} \binom{\text{cnt}(u)}{2}$$
   where $\text{child}(u, c)$ is stored in a hash map or balanced BST (`std::map<int, int>`), taking $O(N \log |\Sigma|)$ deterministic time and $O(N)$ memory!
3. **Alternate Deterministic View (`next_match[i]` DP in `CF 1223F`)**:
   Define $\text{nxt}[i]$ as the smallest $j > i$ such that $S[i..j]$ is stack-exterminable. If we maintain at each $i$ a pointer-swapped map $M_i[c]$ storing the earliest index $j \ge i$ such that $S[i..j-1]$ reduces to $\epsilon$ and $S[j] = c$:
   - Let $p = M_{i+1}[S[i]]$. If $p$ exists, then $\text{nxt}[i] = p$, and for $i$'s map we inherit $M_i \leftarrow M_{p+1}$ (via O(1) pointer swap!) and set $M_i[S[i]] = i$.
   - Then $\text{dp}[i] = 1 + \text{dp}[\text{nxt}[i] + 1]$.

#### When You MUST Use $SL_2(\mathbb{F}_p)$ Instead of the Trie Walk
- **Point Updates / Segment Reversals / Range Swaps**: In a Segment Tree where $S[i] \leftarrow c$, a single update changes $O(N)$ Trie positions $u_i \dots u_n$, breaking the Trie walk. In contrast, a Segment Tree over $SL_2(\mathbb{F}_p)$ matrices updates in $O(\log N)$ time!
- **Checking if $S[l_1..r_1] + S[l_2..r_2]$ is Stack-Exterminable**: With prefix products $P_i = M_{s_1} \dots M_{s_i}$, the reduced matrix of $S[l..r]$ is $M(l, r) = P_{l-1}^{-1} P_r$. Then $S[l_1..r_1] + S[l_2..r_2] =_G \epsilon$ iff $M(l_1, r_1) M(l_2, r_2) = I$, answered in $O(1)$ time!

---

### 99.4 Boundary Pitfalls & Broken-Invariant Counterexamples (Iter 99)

1. **Pitfall 1: Choosing singular matrices ($\det M_c = 0$) or scalar matrices ($M_c = -I$)**.
   - *Counterexample*: If $M_c^2 = I$ has $\text{tr}(M_c) \neq 0$, then by Cayley–Hamilton $M_c$ is a scalar matrix $\pm I$, which commutes with everything (`ABAB` $\to I$). You *must* enforce $\text{tr}(M_c) = 0$ and $\det(M_c) = -1$.
2. **Pitfall 2: Using $SL_2(\mathbb{F}_p)$ for Directed Dyck Words (`(` $\neq$ `)`)**.
   - *Counterexample*: In a standard Dyck language, `()` $\to \epsilon$, so $M_{\text{`)'}} = M_{\text{`('}}^{-1}$. However, in a group, $M_{\text{`)'}} M_{\text{`('}} = I$ ALSO holds, which means `)(` also evaluates to $I$!
   - *Fix*: To forbid `)(` $\to \epsilon$, either pair $SL_2(\mathbb{F}_p)$ hashing with a standard 1D bracket balance RMQ check ($\min_{k=l}^r \text{bal}[k] \ge \text{bal}[l-1]$), OR note that if no prefix has negative balance, then in the free group $F_{|\Sigma|}$ any word with only positive generators pushed and matching inverses popped cannot reduce `)(` unless a mismatch already occurred! Wait: in `([)]`, balance never drops below $0$, and `([)]` $\neq 1$ in $F_2$, whereas in `)(`, balance drops to $-1 < 0$. Wait: what about `() )(`? There balance drops to $-1$. What about `(( )( ))`? In `(( )( ))`, the inner `)(` cancels in $F_1$! So for *multi-type* Dyck words, `(( )( ))` has valid 1D balance AND reduces to $1$ in $F_k$ if `(` and `)` are inverses!
   - *Exact Resolution for Multi-Type Dyck Words*: Assign each opening bracket $c_i$ at **depth $d$** or use the stack explicitly; if you must do range queries with updates on multi-type Dyck words, note that `)(` of the *same* type cancels in $F_k$, so to distinguish `(` from `)` of the same type, assign at position $i$ the generator $g_{(S[i], \text{bal}[i])}$ indexed by both bracket type and current 1D balance height $\text{bal}[i]$ (since a matched pair `(` at $l$ and `)` at $r$ always has $\text{bal}[l] = \text{bal}[r-1] + 1$ and $\min_{k=l}^{r-1} \text{bal}[k] \ge \text{bal}[l-1]$)!

---

## Iteration 100: Obscure & Frontier Stringology Hunt

To ensure Phase 1.5 (`CURRICULUM_ARCHITECTURE.md`) does not miss newly emerging paradigms from theoretical stringology (STOC/FOCS/SODA/CPM) that have migrated into QOJ, Universal Cup, and Chinese National Team papers, we catalog six frontier string domains and their exact competitive programming reductions.

---

### 100.1 String Attractors ($\gamma(S)$ — Kempa & Prezza, STOC 2018)

- **Concrete Object & Question**: A **string attractor** of $S[1..n]$ is a subset of positions $\Gamma \subseteq \{1, \dots, n\}$ such that **every distinct contiguous substring** $S[l..r]$ has at least one occurrence $S[l'..r'] = S[l..r]$ that crosses a position in $\Gamma$ (i.e., $[l', r'] \cap \Gamma \neq \emptyset$). The minimum size of a string attractor is denoted $\gamma(S)$.
- **Combinatorial Invariants**:
  1. **Universal Lower Bound for Repetitive Measures**: Every standard dictionary compression induces an attractor:
     - Lempel–Ziv (LZ77) parse of $z$ phrases: the right endpoints of the $z$ phrases form an attractor ($\gamma(S) \le z$).
     - Straight-Line Program (SLP) of $g$ rules: the split boundary of each production's first occurrence forms an attractor ($\gamma(S) \le g$).
     - Run-Length BWT ($r$ equal-letter runs): $\gamma(S) \le r$.
  2. **Sturmian & Fibonacci Extremality**: For any standard Sturmian or Fibonacci prefix of length $n \ge 2$, $\gamma(S) = 2$! Specifically, $\Gamma = \{f_{k-1}, f_{k-1} + 1\}$ (or the two positions straddling the main concatenation boundary $F_{k-1} | F_{k-2}$) is a size-2 attractor for $F_k$, because every factor of $F_k$ either occurs across the boundary between $F_{k-1}$ and $F_{k-2}$ or occurs inside $F_{k-1} = F_{k-2} F_{k-3}$ where its image in the other copy crosses that same boundary!
  3. **Hardness vs. Contest Reductions**: Computing $\gamma(S)$ for an arbitrary string over alphabet $|\Sigma| \ge 3$ is NP-complete (via reduction from Set Cover on the minimal unique substrings / `endpos` equivalence classes of SAM). In contest problems:
     - Notice that a substring $u$ needs to be covered iff it is **minimal unique** in the sense of interval inclusion: if $u$ is a substring of $v$, covering an occurrence of $u$ automatically covers a shorter substring, WAIT—it is the **reverse**: if $u$ is a substring of $v$, covering an occurrence of $v$ does NOT necessarily cover $u$ (the attractor position in $v$ might fall outside $u$!), whereas if every occurrence of $u$ contains some $i \in \Gamma$, then any superstring $v$ containing $u$ automatically contains $i \in \Gamma$!
     - **Crucial Duality Invariant**: $\Gamma$ is a string attractor of $S$ if and only if $\Gamma$ hits at least one occurrence of every **minimal-length representative** (length $\text{minlen}(q)$) of every SAM node $q$ (or even narrower: only SAM nodes whose occurrence interval family has no strict subset dominance)!

---

### 100.2 $\tau$-Synchronizing Sets & Locally Consistent Sampling (Kempa & Kociumaka, STOC 2019)

- **The Diagnostic Signal**: Classic suffix structures (SA, SAM, Suffix Tree) use $\Theta(n)$ words of memory. If we try to sample every $\tau$-th suffix ($i \equiv 0 \pmod \tau$), two equal substrings $S[i..i+\ell-1] = S[j..j+\ell-1]$ can have $i \not\equiv j \pmod \tau$, so their sampled suffixes are misaligned! On the other hand, simple local minima (minimizers) fail inside periodic regions (`aaaa...a`), either sampling everything or sampling nothing for $\Omega(n)$ steps.
- **Definition of a $\tau$-Synchronizing Set**: Given a parameter $\tau \ge 1$, a subset $\mathsf{S} \subseteq [1, n - 2\tau + 1]$ is a **$\tau$-synchronizing set** if it satisfies three simultaneous invariants:
  1. **Local Consistency**: Whether $i \in \mathsf{S}$ depends **only** on the length-$2\tau$ substring $S[i..i+2\tau-1]$ ($S[i..i+2\tau-1] = S[j..j+2\tau-1] \implies (i \in \mathsf{S} \iff j \in \mathsf{S})$).
  2. **Sparsity**: $|\mathsf{S}| = O(n / \tau)$ in the worst case.
  3. **Density (Non-Periodic Guarantee)**: For every window $[i, i + \tau - 1]$, if the length-$(3\tau - 1)$ substring $S[i..i+3\tau-2]$ does **not** have minimal period $\le \tau / 3$, then $[i, i + \tau - 1] \cap \mathsf{S} \neq \emptyset$.
- **Explicit Construction (Why It Works)**:
  Fix a random or Karp–Rabin injective naming of length-$\tau$ substrings, and define $i \in \mathsf{S}$ iff $\min_{k \in [i, i+\tau]} \text{id}(S[k..k+\tau-1])$ is achieved at $k = i$ OR $k = i + \tau$ (and exclude $i$ if $S[i..i+2\tau-1]$ has period $\le \tau/3$).
  - Whenever a substring of length $3\tau - 1$ is aperiodic, the minimum over $[i, i+2\tau-1]$ of length-$\tau$ identifiers is unique, so as the sliding window $[j, j+\tau]$ moves across that minimum, it hits the boundary at least once in $[i, i+\tau-1]$!
  - And if $S[i..i+3\tau-2]$ IS periodic with period $p \le \tau / 3$, it lies inside a maximal **Run** of period $p \le \tau / 3$, which we handle analytically by jumping to the end of the run!
- **Competitive Programming Applications**:
  - $O(n / \log_\Sigma n)$ word-packed LCE and Suffix Array construction,
  - Sublinear-space / block-compressed pattern matching,
  - Deterministic locally consistent parsing without randomized coin tossing.

---

### 100.3 Cartesian-Tree Pattern Matching (Park, Amir, Landau, Kunsoo Park 2019–2021)

- **Concrete Objects & Question**: Given a numeric text $T[1..n]$ and a pattern $P[1..m]$, we say $T[i..i+m-1]$ **Cartesian-tree matches** $P[1..m]$ if they have the exact same **Cartesian Tree** shape (with min-heap property and left-to-right tie-breaking).
- **The Parent-Distance Encoding (`PD` representation)**:
  Two arrays have the same min-Cartesian tree if and only if for every $j \in [1, m]$, the **nearest strictly smaller (or $\le$) element to the left** has the same relative distance!
  Wait—is left-nearest smaller alone sufficient?
  *4-Step Verification*:
  In the standard incremental construction of a Cartesian Tree scanning $j = 1 \dots m$ and maintaining the **right spine** (a monotonic stack of elements), when inserting $P[j]$, we pop all elements on the right spine that are $> P[j]$. The last popped element becomes the left child of $j$, and the new top of the stack (the nearest index $L(j) < j$ with $P[L(j)] \le P[j]$) becomes the parent of $j$!
  Since the right-spine pop sequence at every step $j$ is uniquely determined by how far back $L(j)$ lies, defining the **Parent-Distance encoding**:
  $$\text{PD}_P[j] = \begin{cases} j - \max\{k < j : P[k] \le P[j]\} & \text{if such } k \text{ exists} \\ 0 & \text{otherwise} \end{cases}$$
  uniquely determines the entire Cartesian tree!
- **Modified KMP Automaton**:
  Just like parameterized KMP (`prev[j]`), for a window starting at $s$, an index $j$ has effective parent-distance $\text{val}(s, j) = \text{PD}[j]$ if $j - \text{PD}[j] \ge s$, and $0$ otherwise. Thus we run standard KMP where equality of characters at prefix length $q$ and position $j$ tests:
  $$\min(\text{PD}[j], q) = \text{PD}_P[q+1]$$
  Wait: $\text{PD}_T[j] \ge q + 1 \iff \text{PD}_P[q+1] = 0$, and if $\text{PD}_P[q+1] > 0$, we require $\text{PD}_T[j] = \text{PD}_P[q+1]$. This runs in **strict $O(n + m)$ time** with zero balanced trees (unlike order-isomorphic matching which requires $O(n \log m)$)!

---

### 100.4 Weighted / Position-Weight Strings (Stochastic Strings — Barton, Kociumaka, Pissis, Radoszewski 2016–2020)

- **Concrete Objects**: A **weighted string** (or position weight matrix / PWM) of length $n$ specifies at each position $i \in [1, n]$ a probability distribution $\pi_i : \Sigma \to [0, 1]$ with $\sum_{c \in \Sigma} \pi_i(c) = 1$. A deterministic string $P[1..m]$ occurs at position $i$ with **probability threshold $1/z$** if $\prod_{j=1}^m \pi_{i+j-1}(P[j]) \ge \frac{1}{z}$.
- **Structural Sparsity Theorem (The Heavy-String Decomposition)**:
  Naively, a weighted string of length $n$ can generate $|\Sigma|^n$ valid strings. However, Barton et al. proved a remarkable structural theorem:
  > For any weighted string $W$ of length $n$ and threshold $1/z$, there exists a **Weighted Suffix Tree** of size $O(n z)$ constructed in $O(n z)$ time, or even stronger: $W$ can be decomposed into $\lfloor z \rfloor$ deterministic strings of total length $O(n z)$ that preserve all $1/z$-solid factors!
- **Why**: At each node of the suffix trie, the sum of branch probabilities across disjoint suffixes starting at the same position $i$ is $\le 1$, so at most $\lfloor z \rfloor$ branches starting at $i$ can have probability $\ge 1/z$! Furthermore, positions where $\max_c \pi_i(c) \ge 1 - \frac{1}{2z}$ have a unique "heavy" character, and positions where the second-largest probability is $\ge \frac{1}{2z}$ can occur at most $O(\log z)$ times before any non-heavy branch's cumulative probability drops below $1/z$!

---

### 100.5 Two-Dimensional Periodicity & Amir–Benson Lattice Classification (Amir & Benson 1992–1998)

- **Concrete Object**: Given a 2D pattern $P[1..R][1..C]$, a **period vector** is an offset $\vec{v} = (\Delta r, \Delta c) \in \mathbb{Z}^2$ such that $P[r + \Delta r][c + \Delta c] = P[r][c]$ wherever both coordinates lie inside $[1..R] \times [1..C]$.
- **Amir–Benson 4-Class Periodicity Taxonomy**:
  Consider the set of period vectors $\vec{v}$ in the central quadrant $|\Delta r| < R/2, |\Delta c| < C/2$. Unlike 1D strings (where all small periods are multiples of a single shortest period $p_0$), in 2D there are **four structural classes**:
  1. **Non-Periodic**: Only $\vec{0} = (0, 0)$ is a period vector.
  2. **1D Line-Periodic**: All period vectors in the quadrant are collinear multiples $k \vec{v}_1$ of a single primitive vector $\vec{v}_1$.
  3. **1D Radiant-Periodic**: Period vectors exist in multiple directions along a monotonic staircase curve, because the overlapping corners near the boundary do not share a common central intersection.
  4. **2D Lattice-Periodic**: There exist two linearly independent period vectors $\vec{v}_1, \vec{v}_2$ generating a 2D lattice $\Lambda = \mathbb{Z}\vec{v}_1 \oplus \mathbb{Z}\vec{v}_2$!
- **2D KMP / Duel / Baker–Bird**:
  - **Baker–Bird Algorithm ($O(N^2 + M^2)$)**: Run Aho–Corasick on the distinct rows of $P$ to turn each row of $T$ into a sequence of row-IDs, then run 1D KMP vertically along each column of row-IDs!
  - **2D Duel Paradigm (Vishkin)**: For any two candidate positions, precompute a **witness table** $\text{Wit}[\Delta r][\Delta c] = (r^*, c^*)$ storing a coordinate where $P$ disagrees with $P$ shifted by $(\Delta r, \Delta c)$. In $O(1)$ time, inspecting $T[i + r^*][j + c^*]$ eliminates at least one of the two overlapping candidates!

---

### 100.6 Lempel–Ziv (LZ77) & Grammar-Compressed Indexing (Claude–Navarro / Christiansen–Ettienne–Kociumaka)

- **The Core Invariant (Primary vs. Secondary Occurrences, Kärkkäinen–Ukkonen)**:
  Suppose a text $T[1..n]$ is represented by its LZ77 parse $T = Z_1 Z_2 \dots Z_z$ ($z$ phrases) or an SLP of $g$ rules.
  - Every occurrence of a pattern $P[1..m]$ in $T$ is either:
    1. **Primary occurrence**: Crosses at least one phrase boundary between $Z_k$ and $Z_{k+1}$ (or is the canonical split point of a lowest SLP non-terminal $X \to A B$).
    2. **Secondary occurrence**: Contained completely inside a single phrase $Z_k$ (or inside $A$ or $B$).
  - By definition of LZ77, every phrase $Z_k = T[i_k..j_k]$ is a copy of an earlier substring $T[i'_k..j'_k]$ ($i'_k < i_k$). Thus every secondary occurrence inside $Z_k$ is an exact shifted copy of an earlier occurrence in $T[i'_k..j'_k]$; tracing these copy pointers backward must terminate at a **primary occurrence**!
- **Algorithmic Compilation (2D Orthogonal Range Reporting)**:
  1. For each phrase boundary $k \in [1, z-1]$, extract the reversed left context $\overleftarrow{Z_1 \dots Z_k}$ and the right context $Z_{k+1} \dots Z_z$.
  2. Sort all $z-1$ reversed left contexts lexicographically ($X$-coordinate) and all $z-1$ right contexts lexicographically ($Y$-coordinate), placing $z-1$ points on a $(z-1) \times (z-1)$ grid.
  3. For a query pattern $P[1..m]$, there are $m-1$ ways to split $P = P[1..j] + P[j+1..m]$ at the first phrase boundary it crosses. Each split $(P[1..j]^R, P[j+1..m])$ defines a 1D lexicographical interval $[x_1, x_2]$ on the reversed left contexts and $[y_1, y_2]$ on the right contexts—reducing primary occurrence counting/reporting across $z$ phrases to **$m-1$ 2D Orthogonal Range Queries** on $z-1$ points via a Wavelet Tree or Persistent Segment Tree!

---

## Iteration 101: `[ZH]` Master Audit (Chinese National Team Papers `国家集训队论文`, NOI/WC/CTSC/CTS/ZJOI/SDOI/HEOI/BJWC/THUPC, UOJ, LOJ, QOJ)

### 101.1 Comprehensive Audit of Chinese IOI National Team Papers (`国家集训队论文`, 2004–2024)

We audit the canonical Chinese National Team treatises on string algorithms, mapping each paper's core theorem and structural techniques to our textbook waves:

| Year | Author | Chinese Title & English Translation | Core Structural Invariants & Algorithms Introduced | Target Wave / Chapter |
| :--- | :--- | :--- | :--- | :--- |
| **2004** | **许智磊** (Xu Zhilei) | 《后缀数组》 (*Suffix Arrays*) | Doubling SA, `height` array LCP theorem ($h[i] \ge h[i-1] - 1$), RMQ-LCP, monotonic stack over `height`. | Prerequisite Baseline |
| **2009** | **罗穗骞** (Luo Suiqian) | 《后缀数组——处理字符串的有力工具》 (*Suffix Array: A Powerful Tool for String Processing*) | 12 canonical SA reductions: binary search on `height` blocks, harmonic-series periodic substring enumeration ($O(N \log N)$ LCE + LCE^R), monotonic stack LCP aggregations. | Wave 1B / Wave 2B |
| **2012** | **陈立杰** (Chen Lijie / WJMZBMR) | 《后缀自动机》 (*Suffix Automaton — SAM Lecture & Treatise*) | Endpos equivalence classes, Link Tree (`parent` tree), why $|V| \le 2n-1$ and $|E| \le 3n-4$, right-extension transition invariant, LCS on SAM, $k$-th substring on SAM DAG. | Wave 2A |
| **2014** | **徐毅** (Xu Yi) | 《回文树及其应用》 (*Palindromic Tree [PAM] and Its Applications*) | Proof of $\le n+2$ states in PAM, online fail-chain amortisation, **Series-Link (`slink` / `diff`) $O(\log n)$ AP decomposition of palindromic suffixes**, $O(n \log n)$ palindrome partition DP, Double-Ended (Deque) PAM (`双向回文自动机`) via `quick_link`, Persistent PAM on trees, and offline $[l, r]$ distinct palindromes via PAM + LCT / Fenwick! | Wave 1A / Wave 3A |
| **2015** | **刘研绎** (Liu Yanyi) | 《后缀自动机在字典树上的拓展》 (*Extension of Suffix Automaton to Tries — Generalized SAM*) | Why naive online insertion into SAM with `last` reset creates dead/disconnected zero-length clones when a prefix already exists; BFS on Trie vs. correct online split-transition GSAM; Tree GSAM (`[ZJOI2015] 诸神眷顾的幻想乡`). | Wave 2A / Wave 5A |
| **2016** | **张天扬** (Zhang Tianyang) | 《后缀树结点数目的性质及应用》 (*Properties and Applications of Suffix Tree Node Counts*) | Compact Suffix Tree construction from SAM of $S^R$, Virtual Suffix Trees (`后缀树虚树`), DSU-on-Tree over Suffix Tree. | Wave 2B |
| **2017** | **周任飞** (Zhou Renfei) | 《Fibonacci 串性质的研究》 (*Research on the Properties of Fibonacci Strings*) | Near-commutativity $F_{k-1}F_{k-2}$ vs $F_{k-2}F_{k-1}$, singular words $w_k$, Compact DAWG / PAM of $F_k$ in $O(k)$ states, counting distinct substrings / palindromes / runs in $F_k[1..n]$ ($n \le 10^{18}$) via Zeckendorf decomposition. | Wave 5B (Iter 98) |
| **2018** | **洪华敦** (Hong Huadun) | 《浅谈保序回归与字符串问题》 / String Periodicity Notes | Periodicity lemmas, internal substring queries (`[BJWC2018] Border 的四种求法`). | Wave 1A / Wave 2B |
| **2019** | **金策** (Jin Ce) | 《字符串算法选讲》 (*Selected Lectures on String Algorithms: Border Theory, Lyndon Words, Significant Suffixes & The Runs Theorem*) | The definitive `[ZH]` treatise unifying: (1) Weak Periodicity Lemma & $O(\log n)$ Border APs, (2) **Significant Suffixes (`显著后缀`) Theorem** ($\le \log_2 n$ candidate suffixes under right extension, solving `[ZJOI2017] 字符串`), (3) Duval's algorithm & Lyndon Tree via double-order ($<$ / $>$) monotonic stack, (4) **Bannai et al. (2017) Runs Theorem** ($\text{Runs}(S) < n$, $\sum \text{exp}(R) < 3n$) and 2D sweep-line for substring square/run queries! | Wave 1A / Wave 1B / Wave 2B |
| **2020** | **王修涵** (Wang Xiuhan) | 《浅谈字符串周期与基本子串字典》 (*String Periodicity and the Basic Substring Dictionary / IPM*) | Kociumaka et al.'s Internal Pattern Matching (IPM) framework in $O(1)$ query time: internal occurrences of $U$ in $V$ when $|V| < 2|U|$ return an arithmetic progression; substring border/period queries in $O(\log n)$. | Wave 2B |
| **2021** | **潘佳奇 / 戴江齐** (Pan Jiaqi / Dai Jiangqi) | 《浅谈单位蒙日矩阵乘法及其在字符串问题中的应用》 (*Unit-Monge Matrix Multiplication and Its Applications to String Problems — Seaweed Matrices*) | Tiskin's **Seaweed Matrices (`海草矩阵`)**, why the cross-difference $\Delta^2 \text{LCS}$ is a permutation matrix, $O(n^2)$ incremental wiring swaps for all-pairs interval LCS, and $O(n \log^2 n)$ divide-and-conquer Unit-Monge distance multiplication $\boxdot$ (`[THUPC 2021] 区间 LCS`). | Wave 4B |
| **2022–2024** | **各类集训队论文** (Recent IOI Papers) | Locally Consistent Parsing (`局部一致性剖析`), Dynamic Strings, Lyndon + SAM couplings, Weighted/Approximate Matching | Grammar compression (SLP) with $O(\log n)$ LCE under split/concat/reverse, $k$-mismatch Kangaroo + FFT, and 2D orthogonal range queries over Lyndon/Runs structures. | Wave 3B / Wave 5B |

---

### 101.2 Audit of Major Chinese Contests (`NOI`, `WC`, `CTSC/CTS`, `ZJOI`, `SDOI`, `HEOI`, `BJWC`, `THUPC`) & Judges (`UOJ`, `LOJ`, `QOJ`)

- **NOI / WC / CTSC / CTS Canonical Landmarks**:
  - `[NOI2014] 动物园` (KMP tree binary lifting / pointer sweep for non-overlapping borders $\le i/2$).
  - `[NOI2015] 品酒大会` (SA `height` sorting / Cartesian tree DSU for pairwise LCP $\ge r$ max product & count).
  - `[WC2016] 论战捆竹竿` (Border $O(\log n)$ AP decomposition + Modulo Shortest Path with residue-class monotonic queue transitions).
  - `[NOI2016] 优秀的拆分` (Harmonic-series LCE + $\text{LCE}^R$ gluing for $\text{AA}\text{BB}$ split counting; precursor to Runs).
  - `[NOI2017] 蚯蚓排队` (Hash table / Trie sliding window over short $k \le 50$ strings under split/merge).
  - `[NOI2018] 你的名字` (The ultimate SAM + Segment Tree Merging on $\text{endpos}$ + Link-Tree binary lifting benchmark: counting substrings of $T$ not occurring in $S[l..r]$).
  - `[CTSC2006] 歌唱王国` & `[SDOI2017] 硬币游戏` (Martingale Optional Stopping / PGF Overlap Border Polynomials $C_{A,B}(x)$).
  - `[CTS2019] 重复` (Counting infinite periodic words whose $m$-prefix is $\ge$ some substring of $S$, via KMP Automaton minimal-shift DP).
- **Provincial Selection (`省选`: `ZJOI`, `SDOI`, `HEOI`, `BJWC`, `十二省联考`, `SCOI`, `AHOI`, `JSOI`) Landmarks**:
  - `[ZJOI2015] 诸神眷顾的幻想乡` (Tree having $\le 20$ leaves $\implies$ rooting at each leaf covers all tree paths in a Generalized Trie + GSAM!).
  - `[ZJOI2017] 字符串` (Significant Suffixes Theorem + Segment Tree + $O(1)$ LCE for dynamic alphabet / range minimum suffix under right-extension).
  - `[BJWC2018] Border 的四种求法` (Internal Pattern Matching / 2D orthogonal range / SAM Link-Tree HLD + VIP prefix-period buckets for substring border queries).
  - `[SDOI2017] 序列计数` / SAM + LCT `access` offline range distinct substring problems.
  - `[SDOI2019] 连续子序列` (Thue–Morse recursive halving DP / morphism decompression).
  - `[十二省联考 2019] 字符串问题` (SAM Link-Tree node splitting + Segment-Tree/Prefix-optimised DAG longest path).
  - `[SCOI2016] 萌萌哒` (Word equations / Binary-lifting DSU `倍增并查集`).
  - `[HEOI2015] 最短不公共子串` (4-way DP/BFS product of SAM and Subsequence Automaton DASG).
  - `[HEOI2016/TJOI2016] 字符串` (Binary search + SAM Link-Tree binary lifting + $\text{endpos}$ Segment Tree Merge).
- **UOJ / LOJ / QOJ / THUPC Frontier Gems**:
  - `UOJ #52 / #77 / #131 / #219 / #429 / #553 / #607` (SAM + LCT, Runs 2D sweep-line, Lyndon suffix maintenance).
  - `THUPC 2021 — 区间 LCS` / `LOJ #6564` (Tiskin's Seaweed Matrices / Unit-Monge multiplication).
  - `QOJ` & `Universal Cup` (Seasons 1–3): Substring distinct palindromes via PAM + `slink` + Fenwick (`LOJ #6071` / `QOJ` variants), Runs + Segment Tree, Subsequence Matrix inversion with updates, and $SL_2(\mathbb{F}_p)$ stack-cancellation tree/range problems.

---

## Iteration 102: `[JA]` Master Audit (AtCoder `AGC`/`ARC`/`ABC`, JOI, yukicoder & Japanese Stringology Treatises)

### 102.1 Audit of Canonical Japanese Competitive Programming String Treatises

| Author / Handle | Key Treatises & Blog Series (`[JA]`) | Core Mathematical & Algorithmic Contributions | Target Wave / Chapter |
| :--- | :--- | :--- | :--- |
| **`noshi91`** | • *Run の列挙 (Bannai et al. 2017) の解説*<br>• *Rolling Hash の衝突と安全性の数理*<br>• *Subsequence Automaton と行列積*<br>• *Locally Consistent Parsing / Block Compression* | First accessible Japanese exposition of $O(N)$ Lyndon-Tree Runs enumeration via double-order ($<$ / $>$) LCE monotonic stack; $2^{61}-1$ Mersenne prime multiplication-free modular arithmetic; deterministic block parsing for dynamic strings. | Wave 1B, Wave 3B, Wave 4B |
| **`maspypy`** | • *AtCoder String / Automaton / Generating Function Editorials*<br>• *Goulden–Jackson Cluster Method & Autocorrelation Polynomials*<br>• *Lyndon Word & Duval Algorithm Notes* | Systematic Formal Power Series (FPS) formulation of string avoidance, overlap polynomials, DFA minimization for `DP套DP`, and lexicographical concatenation orders. | Wave 1B, Wave 4A |
| **`tatyam`** | • *Palindromic Tree (Eertree) の $O(\log N)$ DP 遷移*<br>• *Seaweed Matrix (Unit-Monge) の直感的理解*<br>• *Dynamic String / Deque PAM Implementation Notes* | Clear diagrammatic derivation of why shifting a palindrome suffix AP covers all but one transition; braid-wiring interpretation of Seaweed matrices. | Wave 1A, Wave 3A, Wave 4B |
| **`snuke`** | • *AtCoder Grand Contest (AGC) String Invariant Editorial Canon* (`AGC 004 F`, `AGC 019 F`, `AGC 022 E`, `AGC 044 E`, `AGC 050 C`) | Pioneered **Monoid / Group Reductions (`AGC`/`ARC` String Rewrite Games)**: turning local string rewrite rules (`AB` $\to$ `BA`, `00` $\to$ `1`, `AA` $\to \epsilon$) into invariant homomorphisms into finite automata, Coxeter groups, or $\mathbb{Z}_3$. | Wave 4A, Wave 5B (Iter 99) |
| **`henkoku`** | • *Suffix Automaton + LCT / Segment Tree Merge 総整理*<br>• *Z-Algorithm / KMP / Manacher 逆問題 (Inverse String Reconstruction)*<br>• *Significant Suffixes と区間辞書順最小接尾辞* | Deep comparative taxonomy of offline vs. online substring queries on SAM and PAM, plus exact equivalence-class graphs for reconstructing strings from prefix/border arrays. | Wave 1B, Wave 2A, Wave 3A, Wave 5A |
| **`Nyaan`** | • *競技プログラミングのための文字列アルゴリズムライブラリ* (`Nyaan's Library`: SA-IS, Runs, Lyndon, Z, PAM, Wildcard FFT) | Production-grade benchmarks and corner-case analyses of SA-IS LMS-substring traps, 1-FFT complex wildcard matching, and PAM `slink` DP. | Wave 1B, Wave 2B, Wave 3A, Wave 3B |

---

### 102.2 Audit of AtCoder (`AGC` / `ARC` / `ABC`), JOI & yukicoder String Archetypes

Japanese contests (especially `AGC` and `ARC`) emphasize **combinatorial word invariants, string rewrite monoids, lexicographical greedy games, and palindromic/periodic symmetries** over heavy data-structure boilerplate:

1. **String Rewrite Monoids, Free Group Reductions & Automaton Compressions**:
   - `AGC 022 E — Median Replace` (Compressing $3$-to-$1$ majority reductions on binary strings into a 4-state stack automaton).
   - `AGC 050 C — Block Game` / `ARC 119 E` / `ABC 250 G` variants (Stack-cancellation and reverse-difference reductions).
   - `AGC 027 E — ABBreviate` ($\mathbb{Z}_3$ invariant: mapping $\text{a} \mapsto 1, \text{b} \mapsto 2 \pmod 3$, replacing $\text{aa} \to \text{b}$ and $\text{bb} \to \text{a}$ preserves the total sum $\pmod 3$ AND can reach any target subsequence of matching sum as long as the string is not strictly alternating `ababab...`!).
   - `ARC 135 D` / `AGC 004 F` (Bipartite sign-flip trick: flipping every odd position turns identical-neighbor annihilation `00` $\to \epsilon, 11 \to \epsilon$ into standard swap/permutation invariants `01` $\leftrightarrow$ `10`!).
2. **Lexicographical Extremal Greedies, Lyndon Words & Border Games**:
   - `AGC 007 C` / `AGC 047 B — First Second` (Reversed Trie + Palindrome/Character presence mask for prefix-deletion matching).
   - `ARC 050 D — Suffix Concatenation` (Comparing $S[i..n] + S[1..i-1]$ or arbitrary suffix pairs via SA + LCP in $O(1)$ per comparison).
   - `ABC 272 Ex` / `ABC 214 F` / `ABC 141 E` / `ABC 284 F` / `ABC 257 G` (Subsequence Automaton DP, KMP + DP over prefix jumps, and polynomial/FFT substring matching).
   - `AGC 055 D — ABC Ultimatum` / `AGC 046 D — Secret Passage` (Canonical substring/subsequence generation via Automaton DP to avoid overcounting multiple deletion paths).
3. **JOI (Japanese Olympiad in Informatics) & yukicoder Gems**:
   - `JOI Spring Camp 2018 — Bitaro's Party` / `JOI SC 2019 — Naan` / `JOI SC 2021 — Ancient Machine` / `JOI Open` string compression and automaton tasks.
   - `yukicoder` (`No. 430`, `No. 590`, `No. 866`, `No. 1038`, `No. 1549`): Palindromic tree `slink` DP, SAM $\text{endpos}$ queries, Runs enumeration applications, and $SL_2(\mathbb{F}_p)$ stack hashing problems.

---

## Iteration 103: `[EN]` Master Audit (Codeforces Div1 D–F, ICPC WF/Regionals, Universal Cup, POI & Academic Stringology Canon)

### 103.1 The Academic Competitive-Stringology Canon

Every major breakthrough in 2015–2026 competitive stringology traces directly to five foundational academic groups:

1. **Crochemore & Rytter (*Jewels of Stringology*, 2002; *Text Algorithms*, 1994; Rytter 2006)**:
   - Fine–Wilf Theorem, Duval's Lyndon Factorization, Compact DAWG / SAM anatomy, 2D Baker–Bird / Vishkin Duel, and the structure of Fibonacci/Sturmian words.
2. **The Warsaw School (Kociumaka, Radoszewski, Rytter, Waleń, Charalampopoulos, Straszyński — 2014–2024)**:
   - **Internal Pattern Matching (IPM, SODA 2015 / SICOMP)**: Showing that occurrences of $U$ in $V$ ($|V| < 2|U|$) form a single arithmetic progression of period $\text{per}(U)$, enabling $O(1)$ internal substring occurrences, $O(\log N)$ internal borders, and $O(1)$ periodic extension queries.
   - **Dynamic Strings & Locally Consistent Parsing (FOCS / SODA)**: Maintaining a dynamic collection of strings under split, concatenate, and reverse with $O(\log N)$ deterministic LCE.
3. **Bannai, I, Inenaga, Nakashima, Takeda, Tsuruta (*The "Runs" Theorem*, SICOMP 2017)**:
   - Replaced 15 years of intricate geometric proofs of Kolpakov–Kucherov's $\rho(n) = O(n)$ theorem with a 3-page proof via **Lyndon Roots**: assigning each run $R = [l, r, p]$ its lexicographically minimal period rotation under either $<$ or $>$ order (chosen so the character after the run disagrees in the direction making the root a Lyndon word), proving $\text{Runs}(S) < n$ and $\sum \text{exp}(R) < 3n$, and giving an $O(n)$ algorithm via the Lyndon Tree.
4. **Tiskin (*Semi-Local String Comparison and the Algebra of Seaweeds*, 2008–2015)**:
   - Proved that the matrix of all prefix-suffix and substring-whole LCS scores between $A$ and $B$ has a **Unit-Monge** density matrix (a permutation matrix of size $(|A|+|B|) \times (|A|+|B|)$ called the **Seaweed Matrix**), composable in $O(L \log L)$ via the **0-Hecke / Braid Monoid product** $\boxdot$.
5. **Rubinchik & Shur (*EERTREE: An Efficient Data Structure for Processing Palindromes in Strings*, 2015–2018)** & **Fici, Gagie, Manea, Kempa, Prezza (2018–2022)**:
   - Formalized the Palindromic Tree (PAM), series-links (`slink`), Rich Words, Deque Eertree, and String Attractors ($\gamma$).

---

### 103.2 Audit of Codeforces Div1 D–F, ICPC World Finals, Universal Cup & POI

- **Codeforces Div1 D–F Canonical Benchmarks**:
  - *Periodicity & PAM `slink` DP*: `CF 932G — Palindrome Partition`, `CF 906E — Reverses`, `CF 1827C — Palindrome Partition`.
  - *SAM + Endpos Segment Tree Merging + Binary Lifting*: `CF 666E — Forensic Examination`, `CF 700E — Cool Slogans`, `CF 1037H — Security`, `CF 1063F — String Journey`, `CF 1098F — Ж-function` (SAM Link-Tree HLD + Fenwick range weighting), `CF 1437G`, `CF 235C`.
  - *Algebraic / FFT Matching*: `CF 528D — Fuzzy Search`, `CF 827E — Rusty String`, `CF 1334G — Substring Search`, `CF 954I — Yet Another String Matching Problem`.
  - *Subsequence Automaton Matrices & Monoids*: `CF 750E — New Year and Old Subsequence`, `CF 1609E`, `CF 1223F — Stack Exterminable Arrays` ($SL_2(\mathbb{F}_p)$ / Trie Walk).
  - *Morphic & Recursive Strings*: `CF 1466G — Song of the Sirens`, `CF 1770F` / `CF 1718D` / `CF 633H`.
- **POI (Polish Olympiad in Informatics) — The Birthplace of Combinatorial String Problems**:
  - `POI XII — Template (Szablon)` (KMP border tree + greedy coverage validation in $O(N)$).
  - `POI XIII — Periods of Words (Okresy słów)` (Shortest border $\implies$ longest period).
  - `POI XV — Boys (Chłopaki) / Palindromes (Palindromy)` (Early palindrome periodicity & Trie reductions).
  - `POI XVII — Antisymmetry (Antysymetria)` & `POI XIX — Prefixuffix (Prefiksufiks)` (Decreasing boundary expansion $L(i) \le L(i+1) + 2$ for longest secondary border).
  - `POI XXI — Couriers / String Cycles` & `POI XXV — Poetry`.
- **ICPC World Finals & Universal Cup (`UCup`)**:
  - `ICPC WF 2012 — Fibonacci Words` (Classic 2-state boundary-straddling matrix DP over $F_k$).
  - `ICPC WF 2015 — Evolution in Parallel` / `ICPC WF 2019 — First of Her Name` (Reversed Trie KMP/AC link tree query).
  - `Universal Cup` (2023–2026): Runs 2D rectangle queries, Seaweed Interval LCS (`UCup` Stage problems), Deque PAM with `quick_link`, and $SL_2(\mathbb{F}_p)$ dynamic bracket/stack queries.

---

## Iteration 104: Wave 5B Problem Mining (36 Non-Template Problems in a 4-Tier Difficulty Ladder + 4-Step Zero-Magic Analysis & Quarantine Ledger)

### 104.1 Quarantine Table of Excluded Template Problems (`R-5B-01` to `R-5B-08`)

Per `AGENTS.md` and `strings_research/PLAN.md`, pure algorithm-verification or library-copying problems are quarantined from the main textbook ladders:

| Quarantine ID | Source & Problem Name | Reason for Quarantine |
| :--- | :--- | :--- |
| **`R-5B-01`** | **Library Checker** — `Z Algorithm` / `Suffix Array` / `Number of Substrings` | Pure template verification of baseline string structures with zero modelling. |
| **`R-5B-02`** | **Library Checker** — `Enumerate Palindromes` / `Lyndon Factorization` / `Run Enumerate` | Direct output of standard algorithm tables without a structural reduction or query coupling. |
| **`R-5B-03`** | **Library Checker** — `Wildcard Pattern Matching` | Bare 3-FFT $\sum P_j T_{i+j}(P_j - T_{i+j})^2$ verification. |
| **`R-5B-04`** | **Luogu P3805 / P3808 / P5357 / P3809 / P3804 / P5496 / P6139** (`【模板】Manacher / AC自动机 / SA / SAM / PAM / 广义SAM`) | Explicit Chinese `【模板】` verification problems. |
| **`R-5B-05`** | **SPOJ — `FIBWORD`** (Bare small-$N$ version without large-pattern or modulo constraints) | Superseded by `ICPC WF 2012 — Fibonacci Words` and `CF 1466G — Song of the Sirens`. |
| **`R-5B-06`** | **Codeforces 26B / LeetCode 20 — `Valid Parentheses`** | Trivial single-pass stack verification without substring range queries, updates, or group hashing. |
| **`R-5B-07`** | **UVa 10298 — `Power Strings`** | Bare $N / (N - \pi[N])$ divisibility check covered as a 2-line Warmup Lemma in Chapter 1. |
| **`R-5B-08`** | **BZOJ 3676 — `[APIO2014] 回文串`** | Bare $\max_u (\text{len}(u) \cdot \text{cnt}(u))$ on PAM link tree with zero additional combinatorial structure. |

---

### 104.2 Accepted Non-Template Problem Archive for Wave 5B (36 Problems Across 4 Tiers)

All 36 problems below are curated for **Combinatorics on Words (Sturmian, Fibonacci, Thue–Morse, Substitutive Morphisms), Free Group / $SL_2(\mathbb{F}_p)$ Stack Hashing, String Rewrite Monoids, and Frontier Cross-Wave Synthesis**, ordered along a 4-Tier Difficulty Ladder (`Stepping Stone` $\to$ `Intermediate` $\to$ `Advanced` $\to$ `Mastery`).

---

#### Tier 1: Stepping Stone (9 Problems — Discovering Word Invariants, Stack Equivalence & Morphic Boundaries)

##### Problem 5B-01: `CF 1223F` — Stack Exterminable Arrays (`[EN]` Codeforces Round 588 Div. 1 C)
- **Inline Statement & Constraints**: Given an array $a[1..n]$ of integers ($1 \le a_i \le n$, $\sum n \le 3 \cdot 10^5$), a subarray $a[l..r]$ is **stack-exterminable** if feeding $a_l, \dots, a_r$ into a stack (where pushing $x$ on top of an equal element $x$ pops both) leaves the stack empty. Count the number of stack-exterminable subarrays $1 \le l \le r \le n$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Naive stack simulation from each left endpoint $l$ takes $O(n^2)$ time. Standard polynomial rolling hash cannot model $x x \to \epsilon$.
  2. *Combinatorial Word Invariant*: In the universal Coxeter group $G = \langle \Sigma \mid c^2 = 1 \rangle$, the stack reduction of $a[1..i]$ is its unique reduced word $\text{red}(a[1..i])$. Because every generator is its own inverse ($c^{-1} = c$), $a[l..r] =_G 1 \iff \text{red}(a[1..l-1]) = \text{red}(a[1..r])$.
  3. *Reverse-Engineering Compilation*:
     - **Deterministic Trie Walk**: Maintain the current reduced prefix as a node $u_i$ in a Trie. If the edge from $\text{parent}(u_{i-1})$ to $u_{i-1}$ has label $a_i$, step up to $u_i = \text{parent}(u_{i-1})$; otherwise step down to $\text{child}(u_{i-1}, a_i)$. Answer is $\sum_u \binom{\text{cnt}(u)}{2}$ in $O(n \log n)$ time.
     - **Non-Abelian $SL_2(\mathbb{F}_p)$ Matrix Hash**: Assign each value $c$ a random trace-zero determinant-$(-1)$ matrix $M_c \in GL_2(\mathbb{F}_p)$ so $M_c^2 = I$. Compute prefix products $P_i = P_{i-1} M_{a_i}$ and count equal prefix matrices via a hash table in $O(n)$ time!
  4. *Boundary Pitfall*: Never use alternating scalar hashes $\sum (-1)^i h(a_i)$, which falsely equate `1 2 3 1 2 3` with $\epsilon$.

##### Problem 5B-02: `AGC 027 E` — ABBreviate (`[JA]` AtCoder Grand Contest 027 E)
- **Inline Statement & Constraints**: Given a string $S \in \{\text{'a'}, \text{'b'}\}^n$ ($n \le 10^5$), you may repeatedly replace `'aa'` with `'b'` or `'bb'` with `'a'`. Count the number of distinct strings obtainable from $S$ modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Transitions shrink the string and branch non-uniquely (`aaa` $\to$ `ab` or `ba`), making direct DAG exploration exponential.
  2. *Combinatorial Word Invariant ($\mathbb{Z}_3$ Homomorphism)*: Assign weight $w(\text{'a'}) = 1, w(\text{'b'}) = 2 \pmod 3$. Since $1 + 1 \equiv 2 \pmod 3$ and $2 + 2 \equiv 1 \pmod 3$, **every legal operation preserves the total weight $W(S) \pmod 3$**! Conversely, as long as $S$ contains at least one adjacent equal pair ($S$ is not strictly alternating `abab...`), a contiguous substring $S[l..r]$ can be reduced to a **single character** $c \in \{\text{'a'}, \text{'b'}\}$ if and only if $W(S[l..r]) \equiv w(c) \pmod 3$!
  3. *Reverse-Engineering Compilation*: To avoid overcounting target strings $T = t_1 \dots t_k$, match each character $t_j$ greedily to the **shortest valid prefix** of the remaining suffix of $S$, leaving a final suffix whose weight is $\equiv 0 \pmod 3$. Let $\text{nxt}[i][c]$ be the smallest $j \ge i$ with $W(S[i..j]) \equiv w(c) \pmod 3$. Run a standard subsequence-automaton style DP over $\text{nxt}[i][\text{'a'}]$ and $\text{nxt}[i][\text{'b'}]$ in $O(n)$ time.
  4. *Boundary Pitfall*: If $S$ has **no** adjacent equal characters (`ababab`), zero operations can be performed and the answer is $1$, even though substrings have weights $\equiv 1, 2 \pmod 3$!

##### Problem 5B-03: `ARC 135 D` / `AGC 004 F` Archetype — Alternating Parity Flip on Neighbor Cancellation (`[JA]` AtCoder)
- **Inline Statement & Constraints**: Given a string $S \in \{\text{'A'}, \text{'B'}, \text{'C'}\}^n$ ($n \le 2 \cdot 10^5$) where you can insert/delete `'AA'`, `'BB'`, `'CC'`, or in binary strings where you can swap `'00'` $\leftrightarrow$ `'11'`, determine reachability or count valid target configurations.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Operations on *identical* adjacent characters (`00` $\leftrightarrow$ `11` or `00` $\to \epsilon$) do not preserve character counts.
  2. *Combinatorial Word Invariant (Bipartite Odd-Index Flip)*: In a binary string where `00` $\leftrightarrow$ `11` is allowed, **flip every character at an odd index** ($s'_i = s_i \oplus (i \bmod 2)$). Under this involution, an identical pair `00` or `11` at $(i, i+1)$ becomes an alternating pair `01` or `10`, and changing `00` $\leftrightarrow$ `11` becomes **swapping adjacent distinct characters `01` $\leftrightarrow$ `10`**!
  3. *Reverse-Engineering Compilation*: After flipping odd positions, any two strings are equivalent under `00` $\leftrightarrow$ `11` if and only if their odd-flipped images have the **exact same number of `1`s** (or reduce to the same relative order of non-swappable barriers)!
  4. *Boundary Pitfall*: When string length changes (deletion of `00`), parity of indices after the deletion shifts by $2$ (preserving odd/even index parity!), so the odd-index flip still turns `00` deletion into `01`/`10` deletion (standard 1D balance $\sum (-1)^i s_i$!).

##### Problem 5B-04: `ICPC WF 2012 D` — Fibonacci Words (`[EN]` ICPC World Finals 2012)
- **Inline Statement & Constraints**: Define $F_0 = \text{"0"}, F_1 = \text{"1"}, F_n = F_{n-1} + F_{n-2}$ ($n \le 100$). Given a binary pattern $P$ ($1 \le |P| \le 10^5$), compute the exact number of occurrences of $P$ in $F_n$ (using 64-bit integers).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $|F_{100}| = f_{101} > 10^{20}$, while $|P| \le 10^5$.
  2. *Combinatorial Word Invariant*: Once $|F_{k}| \ge |P| - 1$, every occurrence of $P$ in $F_m = F_{m-1} F_{m-2}$ is either strictly inside $F_{m-1}$, strictly inside $F_{m-2}$, or straddles the concatenation boundary inside $\text{suff}_{|P|-1}(F_{m-1}) + \text{pref}_{|P|-1}(F_{m-2})$.
  3. *Reverse-Engineering Compilation*: Because $F_{m-2}$ is a prefix of $F_{m-1}$ for all $m \ge 3$, $\text{pref}_{|P|-1}(F_m)$ is **constant** for all $m \ge k_0$, while $\text{suff}_{|P|-1}(F_m)$ alternates with **period 2** (by the near-commutativity law $F_m = \pi_m \text{01}$ vs $\pi_m \text{10}$)! Compute $\text{occ}(P, F_m)$ for small $m$ until $|F_{m-2}| \ge |P|-1$, run KMP once on the two boundary windows of length $2|P|-2$, and propagate $\text{dp}[m] = \text{dp}[m-1] + \text{dp}[m-2] + \text{cross}[m \bmod 2]$ in $O(|P| + n)$ time.
  4. *Boundary Pitfall*: When $|P| = 1$, $2|P| - 2 = 0$, so there are **zero** boundary-straddling occurrences ($\text{cross} = 0$).

##### Problem 5B-05: `[SDOI2019] 连续子序列` (`[ZH]` Luogu P5344 / LOJ #3111)
- **Inline Statement & Constraints**: Let $T_\infty = 0110100110010110\dots$ be the infinite Thue–Morse word ($\mu(0)=01, \mu(1)=10$). Given a binary string $S$ ($|S| \le 100$) and an integer $k \le 10^{18}$, count how many strings of length $k$ can be appended to $S$ such that the resulting string $S + W$ occurs as a contiguous factor of $T_\infty$, modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $k \le 10^{18}$ precludes building any automaton of size $k$.
  2. *Combinatorial Word Invariant (Thue–Morse Decimation / Inverse Morphism)*: Every factor $U$ of $T_\infty$ aligns with the 2-block partition $\mu(0) = 01, \mu(1) = 10$ in at most two ways: either starting at an **even** index ($U = \mu(U')$ or $U = \mu(U') c$) or starting at an **odd** index ($U = \bar{c} \mu(U')$ or $U = \bar{c} \mu(U') d$). By Thue's overlap-freeness and four-block uniqueness, for $|U| \ge 4$ the parity of starting positions of $U$ in $T_\infty$ is **uniquely forced** whenever $U$ contains $00$ or $11$!
  3. *Reverse-Engineering Compilation*: Define $f(S, k)$ as the number of valid right-extensions $W$ of length $k$ such that $S + W$ is a factor of $T_\infty$. Split into two alignments of $S$ (even start vs. odd start):
     - If $S$ starts at an even index, pair adjacent characters of $S$ into $01 \mapsto 0, 10 \mapsto 1$. If any pair is $00$ or $11$, this parity is invalid. Otherwise $S$ contracts to $S'$ of length $\lceil |S|/2 \rceil$, and $k$ reduces to $\lfloor k/2 \rfloor$ or $\lceil k/2 \rceil$ depending on $|S| \bmod 2$!
     - Memoize over the small reachable set of $(S, k)$ pairs in $O(|S| \log k)$ time.
  4. *Boundary Pitfall*: For $|S| \le 3$ and $k \le 3$, both even and odd alignments can produce the **exact same** extension $W$ (e.g., $S = \text{"0"}, W = \text{"1"}$ gives $S+W = \text{"01"}$, which occurs at both even index $0$ and odd index $3$ in $01101$!). You must brute-force base cases when $|S| + k \le 3$ to avoid double-counting identical strings $W$ across both parities!

##### Problem 5B-06: `CF 1466G` — Song of the Sirens (`[EN]` Good Bye 2020 G)
- **Inline Statement & Constraints**: Given $s_0$ ($|s_0| \le 100$) and $t[1..n]$ ($n \le 10^5$), where $s_i = s_{i-1} + t_i + s_{i-1}$, answer $q \le 10^5$ queries $(k, w)$ ($\sum |w| \le 10^6$): find the number of occurrences of $w$ in $s_k$ modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $|s_k| = \Theta(2^k |s_0|)$ while $\sum |w| \le 10^6$.
  2. *Combinatorial Word Invariant*: Expand $s_0 \to s_{k_0}$ until $|s_{k_0}| \ge |w|$ (or $k_0 = k$). Then $|s_{k_0}| < 2|w| + |s_0|$. For every higher level $i \in [k_0 + 1, k]$, any occurrence of $w$ crossing the central pivot $t_i$ is contained strictly inside $\text{suff}_{|w|-1}(s_{i-1}) + t_i + \text{pref}_{|w|-1}(s_{i-1}) = \text{suff}_{|w|-1}(s_{k_0}) + t_i + \text{pref}_{|w|-1}(s_{k_0})$.
  3. *Reverse-Engineering Compilation*: Using Z-algorithm / KMP on $w + \# + s_{k_0}$ and $w^R + \# + s_{k_0}^R$, find in $O(|w| + |s_{k_0}|)$ time all split positions $j \in [1, |w|]$ where $w[1..j-1]$ is a suffix of $s_{k_0}$ and $w[j+1..|w|]$ is a prefix of $s_{k_0}$. Each such $j$ requires $t_i = w[j]$ and contributes $2^{k - i}$ to the answer, queried in $O(1)$ via precomputed prefix sums $\sum_{i=1}^k [t_i = c] 2^{-i} \pmod{10^9 + 7}$.
  4. *Boundary Pitfall*: Remember to scale the prefix sum $\sum_{i = k_0 + 1}^k [t_i = c] 2^{-i}$ by $2^k \pmod{10^9 + 7}$, and handle $k_0 = k$ early when $|s_k| < |w|$.

##### Problem 5B-07: `ABC 284 F` — ABCBAC (`[JA]` AtCoder Beginner Contest 284 F)
- **Inline Statement & Constraints**: Given a string $T$ of length $2N$ ($N \le 10^6$), determine if there exist a string $S$ of length $N$ and an index $i \in [0, N]$ such that $T = S[1..i] + S^R + S[i+1..N]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Checking all $N+1$ split positions $i$ naively takes $O(N^2)$ time.
  2. *Combinatorial Word Invariant*: $T[1..2N] = S[1..i] + S[1..N]^R + S[i+1..N]$ holds if and only if:
     - $T[1..i]$ equals the reverse of $T[i+N-i+1..i+N] = T[N+1..N+i]$ (wait: $S^R = S[i+1..N]^R + S[1..i]^R$, so the **last $i$ characters** of $T[i+1..i+N]$ must equal $T[1..i]^R$, and the **first $N-i$ characters** of $T[i+1..i+N]$ must equal $T[i+N+1..2N]^R$!).
  3. *Reverse-Engineering Compilation*: Construct $A = T[1..N] + T[N+1..2N]^R$ and $B = T[1..N]^R + T[N+1..2N]$. Compute their Z-arrays in $O(N)$ time (or compare $S[1..i] + S[i+1..N]$ against $T[i+1..i+N]^R$ via $SL_2(\mathbb{F}_p)$ / Rolling Hash) to test each $i \in [0, N]$ in $O(1)$ time.
  4. *Boundary Pitfall*: Indexing of $S^R$: reversing $S = U V$ gives $S^R = V^R U^R$ (order of blocks reverses!), not $U^R V^R$.

##### Problem 5B-08: `POI XII` — Template / Szablon (`[EN]` Polish Olympiad in Informatics 2005)
- **Inline Statement & Constraints**: Given a string $S[1..n]$ ($n \le 5 \cdot 10^5$), find the length of the shortest substring $P$ that can stamp/cover $S$ by placing overlapping copies of $P$ (each position of $S$ must be covered by at least one occurrence of $P$, and characters at overlapping positions must agree).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Any valid stamp $P$ must cover position $1$ (so $P$ is a prefix of $S$) and position $n$ (so $P$ is a suffix of $S$), meaning $P$ is a **border** of $S$. Testing all $O(n)$ borders naively by scanning $S$ takes $O(n^2)$ time.
  2. *Combinatorial Word Invariant (KMP Fail-Tree Gap Maintenance & $\times 2$ Pruning)*:
     - A border $P = S[1..b]$ covers $S$ iff the maximum gap between consecutive occurrences of $P$ in $S$ (which are the nodes in the subtree of $b$ in the KMP fail tree!) is at most $b$.
     - Moreover, if $b_1 < b_2 < 2 b_1$ are both borders on the KMP fail chain of $n$ and $b_1$ is a valid template for $S[1..b_2]$, then any occurrence of $b_2$ is already covered by copies of $b_1$, so we only need to test candidate borders where each tested candidate is at least **twice as long** as the previous failed/tested candidate (or maintain max gap via bottom-up DSU/linked-list deletion on the KMP tree)!
  3. *Reverse-Engineering Compilation*: Either walk the fail chain of $n$ with the $2\times$ skip rule (testing at most $O(\log n)$ borders via KMP in $O(n)$ total time!) or merge endpos sets on the KMP tree while maintaining maximum adjacent distance in a doubly linked list in $O(n)$ time.
  4. *Boundary Pitfall*: In the $2\times$ skip rule on the fail chain of $n$, you discard $b'$ if $b' < 2 b_{\text{prev}}$ ONLY when $b_{\text{prev}}$ has already been verified to cover $S$ (wait: if $b_{\text{prev}}$ *succeeded*, we are already done since we want the *shortest* template! Instead, if we scan increasing border lengths $b$, we only test $b$ if $b$ can cover the prefix $S[1..\text{last\_cov}[b]]$—giving a simple DP on the KMP chain in $O(n)$!).

##### Problem 5B-09: `CF 1827C` — Palindrome Partition (`[EN]` Codeforces Round 873 Div. 1 C)
- **Inline Statement & Constraints**: Call a string **good** if it is an even-length palindrome or a concatenation of even-length palindromes. Given $S[1..n]$ ($n \le 5 \cdot 10^5$), count the number of good substrings $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A substring can have multiple decompositions into even palindromes (`aaaa` $= \text{aa}+\text{aa} = \text{aaaa}$).
  2. *Combinatorial Word Invariant (Shortest Even Palindromic Prefix / Suffix Uniqueness)*:
     Suppose a string $W$ starts with two even-length palindromes $P_1$ and $P_2$ with $|P_1| < |P_2|$. If $|P_2| \le 2|P_1|$ (or in general, reflecting the prefix $P_1$ across the center of $P_2$), the suffix of $P_2$ of length $|P_1|$ equals $P_1^R = P_1$. Repeating this reflection shows that $P_2 = P_1 U P_1$ where $U$ is ALSO an even-length palindrome!
     Therefore, $W$ is a concatenation of even-length palindromes if and only if removing its **shortest non-empty even-length palindromic suffix** (or prefix) leaves a good string!
  3. *Reverse-Engineering Compilation*: Using Manacher's algorithm + monotonic stack / DSU (or PAM with `slink` / even-length ancestor tracking), find for each right endpoint $r$ the shortest non-empty even-length palindrome ending at $r$, say of length $2 d_r$. If it exists, $\text{dp}[r] = 1 + \text{dp}[r - 2 d_r]$; otherwise $\text{dp}[r] = 0$. Sum $\sum_{r=1}^n \text{dp}[r]$ in $O(n)$ time!
  4. *Boundary Pitfall*: This greedy shortest-palindrome reduction ONLY works for **even-length** palindromes! For odd+even palindromes (`aba` vs `abacaba`), greedy shortest removal fails (`CF 932G` requires full PAM `slink` DP).

---

#### Tier 2: Intermediate (9 Problems — Matrix Homomorphisms, Free Group Reductions, Thue–Morse & Automaton DP)

##### Problem 5B-10: `AGC 050 C` — Block Game (`[JA]` AtCoder Grand Contest 050 C)
- **Inline Statement & Constraints**: Given a string $S \in \{\text{'B'}, \text{'S'}, \text{'?'}\}^n$ ($n \le 10^6$), replace `'?'` in $2^{\#?}$ ways and count how many resulting strings allow Snuke (`S`) to win a 1D block-pushing/jumping game against Takahashi (`B`).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Game states depend on distances between consecutive `'S'` characters, which can be up to $n$.
  2. *Combinatorial Word Invariant (Exponential Threshold Compression)*: Reading the string from right to left after the last `'S'`, each `'S'` halves the maximum gap of `'B'`s that can be survived to its left: before the last `'S'` any number works; moving left across the $k$-th `'S'` from the end, the gap of consecutive `'B'`s immediately before it cannot exceed $2^{k-1}$!
  3. *Reverse-Engineering Compilation*: Since $2^{21} > 10^6$, only the last $\le 21$ occurrences of `'S'` matter! Running DP from right to left tracking $k \in [0, 21]$ (how many `'S'`s have been placed so far) and using prefix sums to enforce that the gap of `'B'`s before the $k$-th `'S'` is $\le 2^{k-1}$ solves the problem in $O(n \log n)$ time.
  4. *Boundary Pitfall*: A string with **zero** `'S'` characters is always a win for `'B'`, and characters *after* the last `'S'` have no restriction on `'B'` count.

##### Problem 5B-11: `AGC 022 E` — Median Replace (`[JA]` AtCoder Grand Contest 022 E)
- **Inline Statement & Constraints**: Given an odd-length string $S \in \{\text{'0'}, \text{'1'}, \text{'?'}\}^n$ ($n \le 3 \cdot 10^5$), you repeatedly replace any $3$ consecutive characters with their median until a single character remains. Count how many replacements of `'?'` can produce `'1'` modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: There are $\Omega(n!)$ reduction orders for $3$-to-$1$ median operations.
  2. *Combinatorial Word Invariant (Canonical Stack-Monoid Automaton)*: Maintain a greedy left-to-right stack invariant:
     - Whenever `'0'` and `'1'` are adjacent at the top of the stack (and the stack does not start with `'11'`), a `'01'` pair together with any neighbor reduces to that neighbor (`01x` $\to x$), so **`'01'` and `'10'` annihilate on the stack** just like a free group!
     - Whenever `'000'` appears on the stack, reduce `'000'` $\to$ `'0'` immediately (never hurting `'1'`).
     - Whenever `'11'` reaches the bottom of the stack, `'11'` + anything = `'1'`, so the string is **permanently locked into winning (`'1'`)**!
  3. *Reverse-Engineering Compilation*: Under these four local reduction rules, the reduced stack can only ever be in one of **7 states**: $\epsilon, \text{`0'}, \text{`00'}, \text{`1'}, \text{`10'}, \text{`100'}, \text{`11' (win)}$. Run a 7-state DFA DP over $S$ in $O(n)$ time!
  4. *Boundary Pitfall*: Do **not** reduce `'101'` $\to$ `'1'` if the first `'1'` could instead pair with a future `'1'` to form the absorbing state `'11'`; the canonical stack rule (reducing `'000'` $\to$ `'0'` and cancelling `'0'` against a preceding `'1'` when `'0'` arrives) is provably optimal.

##### Problem 5B-12: `CF 750E` — New Year and Old Subsequence (`[EN]` Good Bye 2016 E)
- **Inline Statement & Constraints**: Given a digit string $S[1..n]$ ($n \le 2 \cdot 10^5$) and $q \le 2 \cdot 10^5$ queries $[l, r]$, find the minimum number of characters to delete from $S[l..r]$ so that it contains subsequence `"2016"` but **not** subsequence `"2017"`.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Range queries $[l, r]$ over subsequence avoidance cannot be answered by greedy matching because `"2016"` and `"2017"` share the prefix `"201"`.
  2. *Combinatorial Word Invariant (Tropical DFA Homomorphism)*: Build the 5-state DFA tracking the longest prefix of `"2016"` matched so far: states $0 (\epsilon), 1 (\text{"2"}), 2 (\text{"20"}), 3 (\text{"201"}), 4 (\text{"2016"})$. At character $c = S[i]$, either we delete $c$ (cost $+1$, state unchanged) or keep $c$ (cost $0$, state advances if $c$ matches the next needed digit, and is forbidden from state $3, 4$ if $c = \text{'7'}$).
  3. *Reverse-Engineering Compilation*: Each character $S[i]$ maps to a $5 \times 5$ $(\min, +)$ tropical matrix $M_{S[i]}$. Store $M_{S[i]}$ in a Segment Tree; each query $[l, r]$ multiplies a $1 \times 5$ vector through $O(\log n)$ segment tree nodes in $O(5^2 \log n)$ time per query.
  4. *Boundary Pitfall*: Once in state $4$ (`"2016"` completed), any `'6'` has cost $0$ to stay in state $4$, whereas any `'7'` MUST be deleted (cost $+1$) so that `"2017"` is still avoided!

##### Problem 5B-13: `ABC 214 F` + Range Extension — Subsequence Automaton Invertible Matrix (`[JA]` AtCoder / QOJ Archetype)
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 2 \cdot 10^5, |\Sigma| \le 26$) and $q \le 2 \cdot 10^5$ range queries $[l, r]$, count the number of distinct non-empty subsequences of $S[l..r]$ (or subsequences with no two adjacent in $S$) modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A Segment Tree of $(|\Sigma|+1) \times (|\Sigma|+1)$ matrices takes $O(|\Sigma|^3 \log n)$ or $O(|\Sigma|^2 \log n)$ per query, which TLEs for $|\Sigma| = 26, q = 2 \cdot 10^5$.
  2. *Combinatorial Word Invariant (Elementary Rank-1 Update & $O(1)$-Sparse Matrix Inverse)*:
     In the distinct-subsequence DP tracking the vector $v = (\text{dp}_{c_1}, \dots, \text{dp}_{c_{|\Sigma|}}, 1)^T$ where $\text{dp}_c$ is the number of distinct subsequences ending with character $c$, appending character $x$ replaces row $x$ by the sum of all entries:
     $$M_x = I + e_x (\mathbf{1}^T - e_x^T)$$
     Notice that $\det(M_x) = 1$, and its **exact inverse** in $GL_{|\Sigma|+1}(\mathbb{F}_p)$ simply subtracts the other rows from row $x$ and divides by $1$ (or for the total-sum representation $M'_x$, has $O(1)$ non-zero off-diagonal entries)!
  3. *Reverse-Engineering Compilation*: Because $M_x$ and $M_x^{-1}$ both act on any vector in **$O(1)$ operations**, we precompute prefix matrices $P_i = M_{s_i} P_{i-1}$ and suffix inverse matrices $P_i^{-1} = P_{i-1}^{-1} M_{s_i}^{-1}$ in $O(n |\Sigma|)$ total time, and answer each range query $[l, r]$ via $P_r P_{l-1}^{-1} v_0$ in $O(|\Sigma|)$ time per query—**zero segment trees**!
  4. *Boundary Pitfall*: In the formulation where state $0$ stores the *total* sum $\sum \text{dp}_c + 1$ and state $x$ stores $\text{prev\_total}$, the transition matrix has determinant $-1$ (invertible!), whereas if a transition zeros out a row without preserving the old value in another register, $\det = 0$ and the matrix is not invertible!

##### Problem 5B-14: `[HEOI2015] 最短不公共子串` (`[ZH]` Luogu P4112 / BZOJ 4032)
- **Inline Statement & Constraints**: Given two lowercase strings $A$ and $B$ ($|A|, |B| \le 2000$), find the minimum length of a string $W$ that is: (1) a substring of $A$ not a substring of $B$, (2) a substring of $A$ not a subsequence of $B$, (3) a subsequence of $A$ not a substring of $B$, and (4) a subsequence of $A$ not a subsequence of $B$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: "Substring" vs. "Subsequence" requires two different automata on the same strings.
  2. *Combinatorial Word Invariant (Automaton Product Shortest Path)*:
     - All **substrings** of a string $X$ are accepted by the **Suffix Automaton** $\text{SAM}(X)$.
     - All **subsequences** of a string $X$ are accepted by the **Subsequence Automaton** $\text{DASG}(X)$ (where $\delta_{\text{DASG}}(i, c) = \min\{j > i : X[j] = c\}$).
     - Therefore, a shortest string accepted by Automaton $\mathcal{A}_1(A)$ and **rejected** by Automaton $\mathcal{A}_2(B)$ is simply a shortest path in the product graph $V(\mathcal{A}_1(A)) \times (V(\mathcal{A}_2(B)) \cup \{\bot\})$ from $(\text{root}_A, \text{root}_B)$ to any state $(u, \bot)$!
  3. *Reverse-Engineering Compilation*: Build $\text{SAM}(A)$, $\text{SAM}(B)$, $\text{DASG}(A)$, and $\text{DASG}(B)$ in $O((|A| + |B|)|\Sigma|)$ time. For Subtasks (1) and (2), each state $u \in \text{SAM}(A)$ already knows its shortest length $\text{minlen}(u)$, or we simply run BFS/DP on the product graph of size $|A| \times |B| \le 4 \cdot 10^6$ in $O(|A| |B|)$ time!
  4. *Boundary Pitfall*: In Subtask (3) ($\text{DASG}(A) \times \text{SAM}(B)$), not every state $(i, u)$ is needed: since we want the **shortest** string, in $\text{DASG}(A)$ at index $i$, for each state $u \in \text{SAM}(B)$ we only need the minimum length to reach $(i, u)$, which is a DAG DP over $i = |A| \dots 0$ and $u \in \text{SAM}(B)$.

##### Problem 5B-15: `POI XVII` — Antisymmetry (`[EN]` Polish Olympiad in Informatics 2010)
- **Inline Statement & Constraints**: Given a binary string $S[1..n]$ ($n \le 5 \cdot 10^5$), count the number of contiguous substrings of even length that are **antisymmetric** (reversing the substring and bitwise-negating every character yields the original substring).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Standard Manacher tests $S[i - k] = S[i + k - 1]$, whereas antisymmetry requires $S[i - k] = 1 - S[i + k - 1]$.
  2. *Combinatorial Word Invariant (Involution-Palindrome Symmetry)*: Let $\theta : \Sigma \to \Sigma$ be any involution ($\theta(\theta(c)) = c$, here $\theta(0) = 1, \theta(1) = 0$) and extend $\theta(w_1 \dots w_m) = \theta(w_m) \dots \theta(w_1)$. Because $\theta(U V) = \theta(V) \theta(U)$, the reflection of an antisymmetric substring inside a larger antisymmetric substring centered at $c$ is **also** antisymmetric!
  3. *Reverse-Engineering Compilation*: Run even-center Manacher's algorithm verbatim, replacing only the character comparison `S[i - k] == S[i + k - 1]` with `S[i - k] != S[i + k - 1]`. The radius $R[i]$ at each boundary $i$ equals the number of antisymmetric substrings centered at $i$; sum $\sum_{i=1}^{n-1} R[i]$ in $O(n)$ time.
  4. *Boundary Pitfall*: Odd-length strings can **never** be antisymmetric over $\{0, 1\}$ because the middle character would have to satisfy $c = 1 - c$.

##### Problem 5B-16: `POI XIX` — Prefixuffix / Prefiksufiks (`[EN]` Polish Olympiad in Informatics 2012)
- **Inline Statement & Constraints**: Two strings $A, B$ are **cyclically equivalent** if $A = U V$ and $B = V U$ for some strings $U, V$. Given $S[1..n]$ ($n \le 10^6$), find the longest proper prefix $S[1..k]$ ($k \le n/2$) that is cyclically equivalent to the suffix $S[n-k+1..n]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Testing cyclic equivalence of $S[1..k]$ and $S[n-k+1..n]$ for each $k$ takes $O(n^2)$ if done via Booth/Duval per $k$.
  2. *Combinatorial Word Invariant ($\le +2$ Contraction of Inner Borders)*:
     $S[1..k]$ and $S[n-k+1..n]$ are cyclically equivalent if and only if $S[1..k] = U V$ and $S[n-k+1..n] = V U$, where $U$ is a **border** of the whole string $S[1..n]$ (of length $i = |U| \le k$) and $V$ is a **border** of the stripped middle substring $S[i+1..n-i]$ (of length $f(i) = |V| \le n/2 - i$)!
     How do we compute the longest non-overlapping border $f(i)$ of $S[i+1..n-i]$ for ALL $i$ in $O(n)$ total time?
     **Key Lemma**: If $S[i+1..n-i]$ has a border of length $\ell$, then stripping one character from both ends of that border yields a border of $S[i+2..n-i-1]$ of length $\ell - 2$! Therefore:
     $$f(i) \le f(i+1) + 2$$
  3. *Reverse-Engineering Compilation*: Compute $f(\lfloor n/2 \rfloor) = 0$, and loop $i$ downward from $\lfloor n/2 \rfloor - 1$ to $0$: start candidate length at $\min(\lfloor n/2 \rfloor - i, f(i+1) + 2)$ and decrement until $S[i+1..i+\ell] = S[n-i-\ell+1..n-i]$ (checked in $O(1)$ via LCE / double hash). Total decrements $\le 2n$, running in $O(n)$ time! Then take $\max_{i \in \text{Borders}(S)} (i + f(i))$.
  4. *Boundary Pitfall*: Remember to enforce $i + f(i) \le \lfloor n/2 \rfloor$ so the prefix and suffix (or the inner border $V$) do not overlap the center.

##### Problem 5B-17: `[CTSC2006] 歌唱王国` & `[SDOI2017] 硬币游戏` (`[ZH]` Luogu P4548 / P3706)
- **Inline Statement & Constraints**: In P4548, a random string over $\{1, \dots, m\}$ is generated one character at a time until pattern $S$ ($|S| \le 10^5$) appears; find the expected stopping time $\pmod{10^4}$. In P3706, $n \le 300$ binary patterns $P_1, \dots, P_n$ each of length $m \le 300$ race against each other on a fair coin stream; find the winning probability of each $P_i$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Building the Aho–Corasick automaton on $n$ patterns of length $m$ has $n m = 9 \cdot 10^4$ states, making Gaussian elimination $O((nm)^3)$ impossible.
  2. *Combinatorial Word Invariant (Martingale Optional Stopping / Goulden–Jackson Overlap Polynomial)*:
     Imagine a casino where before each step $t$, a new gambler arrives with $\$1$ and bets comprehensively on $P_i$: if the character matches the $k$-th character of $P_i$, their stake multiplies by $|\Sigma|$; otherwise they go broke.
     When $P_j$ wins at stopping time $T$, the total payout to gamblers betting on $P_i$ is **exact**: a gambler who started at $T - k + 1$ survives iff the length-$k$ prefix of $P_i$ equals the length-$k$ suffix of $P_j$!
     Thus the overlap correlation value is:
     $$C(P_j, P_i) = \sum_{k=1}^m [P_j[m-k+1..m] = P_i[1..k]] |\Sigma|^k$$
  3. *Reverse-Engineering Compilation*:
     - For a single pattern $S$ (`[CTSC2006]`), $E[T_S] = \sum_{k \in \text{Borders}(S)} m^k$ in $O(|S|)$ time via KMP!
     - For $n$ racing patterns (`[SDOI2017]`), let $p_i$ be the winning probability of $P_i$ and $p_0$ be the PGF coefficient of non-terminating strings ($G_N(1)$). By Optional Stopping (or PGF equations), $\sum_{j=1}^n C(P_j, P_i) p_j - p_0 = 0$ for each $i = 1 \dots n$, plus $\sum_{j=1}^n p_j = 1$. Solve this $(n+1) \times (n+1)$ system via Gaussian elimination in $O(n^3 + n^2 m)$ time!
  4. *Boundary Pitfall*: $C(P_j, P_i)$ is **not symmetric**: it checks whether a **suffix of $P_j$** (the pattern that just finished!) equals a **prefix of $P_i$** (the gambler still in progress). Swapping $i$ and $j$ transposes the matrix and gives completely wrong probabilities!

##### Problem 5B-18: `ARC 119 E` — Pancakes / Reverse Subarray Difference (`[JA]` AtCoder Regular Contest 119 E)
- **Inline Statement & Constraints**: Given an array $A[1..N]$ ($N \le 3 \cdot 10^5$), you may reverse at most one contiguous subarray $A[l..r]$ ($1 \le l \le r \le N$). Minimize $\sum_{i=1}^{N-1} |A[i] - A[i+1]|$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Reversing $A[l..r]$ changes the internal order of $r - l + 1$ elements, seemingly requiring $O(N^2)$ checks.
  2. *Combinatorial Word Invariant (Boundary-Only Involution of Internal Adjacencies)*:
     Reversing a contiguous substring $A[l..r]$ preserves **every single internal adjacency** $\{A[i], A[i+1]\}$ for $l \le i < r$! Only the two boundary cuts $(A[l-1], A[l])$ and $(A[r], A[r+1])$ are replaced by $(A[l-1], A[r])$ and $(A[l], A[r+1])$.
  3. *Reverse-Engineering Compilation*: For two segments $[A_{l-1}, A_l]$ and $[A_r, A_{r+1}]$ ordered in the same direction (both $A_{l-1} \le A_l$ and $A_r \le A_{r+1}$, or both $\ge$), reversing $A[l..r]$ saves exactly $2 \times \text{overlap}([A_{l-1}, A_l], [A_r, A_{r+1}])$. Sort interval pairs by left endpoint and maintain maximum right endpoint in $O(N \log N)$ time.
  4. *Boundary Pitfall*: Do not forget the boundary cases $l = 1$ (only right cut $(A_r, A_{r+1})$ changes to $(A_1, A_{r+1})$) and $r = N$ (only left cut changes).

---

#### Tier 3: Advanced (9 Problems — Sturmian/Fibonacci Compressions, Dynamic $SL_2(\mathbb{F}_p)$ Trees, WC/NOI Classics)

##### Problem 5B-19: `[国家集训队论文 2017] Fibonacci 串 / BZOJ 4567 / Fibonacci Substring & Palindrome Queries` (`[ZH]` National Team Paper Archetype)
- **Inline Statement & Constraints**: Let $F_k$ be the $k$-th Fibonacci string ($F_1 = \text{b}, F_2 = \text{a}, F_k = F_{k-1} F_{k-2}$). Given $q \le 10^5$ queries of an index $n \le 10^{18}$, compute for the prefix $F_\infty[1..n]$: (a) the number of distinct substrings, (b) the number of distinct palindromes, and (c) the sum of lengths of all distinct substrings modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $n \le 10^{18}$ makes $O(n)$ SAM/PAM construction impossible.
  2. *Combinatorial Word Invariant (Sturmian Complexity $p(m) = m+1$ & Singular Word Thresholds)*:
     - In the infinite Fibonacci word $F_\infty$, there are at most $m+1$ distinct factors of length $m$. How soon do all $m+1$ factors of length $m$ appear in a prefix $F_\infty[1..n]$?
     - By Rytter's Singular Word decomposition, every new factor introduced at position $i$ of $F_\infty$ belongs to a predictable arithmetic/Fibonacci progression: specifically, for each $k \ge 3$, in the interval $n \in [f_k, f_{k+1} - 1]$, each step $i \to i+1$ introduces **exact $1$ new distinct substring of each length $\ell \in [i - f_{k-1} + 1, i - f_{k-2}]$** (which is a constant count $f_{k-1} - f_{k-2} = f_{k-3}$ per position up to the overlap point $f_k + f_{k-2} - 1$)!
     - For palindromes, $F_\infty$ is a **Rich Word** (every prefix of length $n$ contains the maximum possible number of distinct non-empty palindromes: **exact $n$ distinct non-empty palindromes** for every $n \ge 1$ by Droubay–Pirillo!).
  3. *Reverse-Engineering Compilation*:
     - Part (b) is $n$ immediately by richness of Sturmian words!
     - For Parts (a) and (c), locating $k$ such that $f_k \le n < f_{k+1}$, the SAM of $F_\infty[1..n]$ decomposes into complete singular layers $1 \dots k-2$ plus a linear ramp on $[f_k, \min(n, f_k + f_{k-2} - 1)]$ and a second ramp on $[f_k + f_{k-2}, n]$, answered in $O(\log n)$ time per query!
  4. *Boundary Pitfall*: Be careful with $n = 1, 2, 3$: the general formula $f_k + f_{k-2} - 1$ requires $k \ge 4$.

##### Problem 5B-20: `[WC2016] 论战捆竹竿` (`[ZH]` Luogu P4156 / UOJ #179)
- **Inline Statement & Constraints**: Given a string $S[1..n]$ ($n \le 5 \cdot 10^5$) and a target bound $W \le 10^{18}$, you start with one copy of $S$ (length $n$) and can repeatedly append $S$ overlapping along any proper border of $S$ (adding $n - b$ to the current length for any border $b \in \text{Borders}(S)$). Count how many total lengths $\ell \in [n, W]$ can be formed across $T \le 5$ testcases.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: The set of step sizes $\{n - b : b \in \text{Borders}(S)\}$ has up to $n-1$ elements, so naive Modulo Shortest Path (`同余最短路`) on modulo $n - b_{\max}$ takes $O(n^2)$ edges, TLEing for $n = 5 \cdot 10^5$.
  2. *Combinatorial Word Invariant ($O(\log n)$ Border AP Decomposition)*:
     By the Weak Periodicity Lemma, the set of period steps $\{n - b : b \in \text{Borders}(S)\}$ partitions into **$O(\log n)$ arithmetic progressions** $A_k = \{x_k + j \cdot d_k : 0 \le j < c_k\}$ where $x_k$ is the smallest period in the block and $d_k$ is the step size!
  3. *Reverse-Engineering Compilation*:
     - Process the $O(\log n)$ arithmetic progressions one by one.
     - When transitioning from old modulus $m_{\text{old}}$ to the new base modulus $x_k$: change the modulo shortest path array $\text{dist}[0..m_{\text{old}}-1] \to \text{dist}'[0..x_k-1]$ by setting $\text{dist}'[v \bmod x_k] = \min \text{dist}[v]$ and running a single cycle scan of step $m_{\text{old}} \pmod{x_k}$ on the $\gcd(m_{\text{old}}, x_k)$ cycles.
     - Then, within modulus $x_k$, any transition in $A_k$ adds $x_k + j \cdot d_k \equiv j \cdot d_k \pmod{x_k}$ for $0 \le j < c_k$. On each of the $\gcd(x_k, d_k)$ residue cycles of step $d_k$, this is a **sliding window minimum of width $c_k$**, solved in $O(x_k)$ time via a **Monotonic Queue**!
     - Total time: $O(n \log n)$!
  4. *Boundary Pitfall*: When unrolling a cycle of length $L = x_k / \gcd(x_k, d_k)$ for the monotonic queue, you must **start the unrolled cycle at the index achieving the global minimum `dist`** on that cycle so that no relaxation wraps around the start twice.

##### Problem 5B-21: `CF 932G` — Palindrome Partition (`[EN]` ICM Technex 2018 G)
- **Inline Statement & Constraints**: Given an even-length string $S[1..n]$ ($n \le 10^6$), count the number of ways to partition $S = s_1 s_2 \dots s_k$ ($k$ even) such that $s_i = s_{k - i + 1}$ for all $1 \le i \le k$, modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Matching outer blocks $s_1 = s_k, s_2 = s_{k-1}$ couples prefixes and suffixes across the whole string.
  2. *Combinatorial Word Invariant (Interleaving Shuffle Bijection + PAM `slink` AP Invariant)*:
     - **Step A (Shuffle Reduction)**: Construct the interleaved string:
       $$T = S[1] S[n] S[2] S[n-1] \dots S[n/2] S[n/2 + 1]$$
       Under this bijection, a symmetric block pair $s_i = s_{k-i+1}$ of length $\ell$ in $S$ becomes an **even-length palindrome** of length $2\ell$ in $T$! Thus the problem reduces to counting partitions of $T[1..n]$ into even-length palindromes!
     - **Step B (PAM `slink` Invariant)**: For a node $u$ in the Palindromic Tree of $T$ with $\text{diff}(u) = \text{len}(u) - \text{len}(\text{fail}(u)) = \text{diff}(\text{fail}(u))$, the palindromic suffixes in $u$'s arithmetic progression ending at $r$ are at lengths $\ell, \ell - d, \ell - 2d, \dots$. Crucially, the suffixes of lengths $\ell - d, \ell - 2d, \dots$ ending at $r$ are **identical to the AP of $\text{fail}(u)$ ending at $r - d$**!
  3. *Reverse-Engineering Compilation*: Maintain at each PAM node $u$ the sum $g[u]$ of $\text{dp}[r - \text{len}(v)]$ over the AP chain of $u$. When $u$ is visited at index $r$, update:
     $$g[u] = \text{dp}[r - \text{len}(\text{slink}(u)) - \text{diff}(u)] + [\text{diff}(u) = \text{diff}(\text{fail}(u))] \cdot g[\text{fail}(u)]$$
     and add $g[u]$ to $\text{dp}[r]$ (if $r$ is even). Time & space: $O(n \log n)$ time, $O(n)$ memory.
  4. *Boundary Pitfall*: Only update $\text{dp}[r]$ when $r$ is **even** (since every block in $T$ must correspond to an aligned pair of characters from $S$, meaning only even-length palindromes at even prefixes of $T$ are valid!).

##### Problem 5B-22: `CF 906E` — Reverses (`[EN]` Codeforces Round 454 Div. 1 E)
- **Inline Statement & Constraints**: Given two strings $A[1..n]$ and $B[1..n]$ ($n \le 5 \cdot 10^5$), find the minimum number of non-overlapping substrings of $A$ you need to reverse so that $A$ becomes equal to $B$, and output the reversed intervals.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Reversing $A[l..r]$ to match $B[l..r]$ means $A[l..r] = B[l..r]^R$.
  2. *Combinatorial Word Invariant*: Interleave $A$ and $B$ into $T = A[1] B[1] A[2] B[2] \dots A[n] B[n]$ of length $2n$. Then $A[l..r] = B[l..r]^R$ if and only if $T[2l-1..2r]$ is an **even-length palindrome** in $T$!
     - Reversing a block of length $1$ ($A[i] = B[i]$) costs $0$ reversals, while reversing a block of length $\ge 2$ costs $1$ reversal.
  3. *Reverse-Engineering Compilation*: Run PAM `slink` DP on $T[1..2n]$ where $g[u]$ stores the **minimum** $(\text{dp}[j], j)$ over $u$'s AP chain instead of the sum, and if $T[2i-1] = T[2i]$ also allow the cost-0 transition $\text{dp}[2i] \leftarrow \text{dp}[2i-2]$. Time: $O(n \log n)$.
  4. *Boundary Pitfall*: To reconstruct the intervals, `g[u]` must store the argmin index $j$ alongside the minimum value $\text{dp}[j]$, not just `u` itself, because `g[u]` is overwritten as $r$ advances!

##### Problem 5B-23: `Dynamic Stack-Exterminable Range Queries with Updates` (`[JA]` / `[EN]` yukicoder / QOJ $SL_2(\mathbb{F}_p)$ Benchmark)
- **Inline Statement & Constraints**: Given a string $S[1..n]$ ($n \le 2 \cdot 10^5, |\Sigma| \le 10^5$) where adjacent identical characters cancel (`cc` $\to \epsilon$), support $q \le 2 \cdot 10^5$ operations:
  1. `1 i c`: Change $S[i] \leftarrow c$.
  2. `2 l r`: Determine if $S[l..r]$ is stack-exterminable.
  3. `3 l1 r1 l2 r2`: Determine if $\text{red}(S[l_1..r_1]) = \text{red}(S[l_2..r_2])$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Point updates invalidate $O(n)$ states of any deterministic Trie walk.
  2. *Combinatorial Word Invariant*: Map each character $c \in \Sigma$ to an independent random involution $M_c = \begin{pmatrix} a_c & b_c \\ (1 - a_c^2)b_c^{-1} & -a_c \end{pmatrix} \in GL_2(\mathbb{F}_p)$ with $\text{tr}(M_c) = 0, \det(M_c) = -1$, so $M_c^2 = I$. Since matrix multiplication is associative, a Segment Tree over $S[1..n]$ stores at each node the product $M_{l..r} = M_{S[l]} \dots M_{S[r]}$.
  3. *Reverse-Engineering Compilation*:
     - Operation 1 updates a leaf matrix in $O(\log n)$ time.
     - Operation 2 tests whether $\text{query}(1, 1, n, l, r) = I$ in $O(\log n)$ time.
     - Operation 3 tests whether $\text{query}(l_1, r_1) = \text{query}(l_2, r_2)$ in $O(\log n)$ time.
  4. *Boundary Pitfall*: What if we also need to verify that the reduced string has **exact length $k$** or find the **first differing character** of two reduced strings? Augment each Segment Tree node with only the $SL_2(\mathbb{F}_p)$ hash if we just need equality, OR if we need the $k$-th character of the reduced string, see Problem 5B-31 (Segment Tree Recursive Cancellation)!

##### Problem 5B-24: `[NOI2016] 优秀的拆分` (`[ZH]` Luogu P1117 / UOJ #219)
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 3 \cdot 10^4$, $T \le 10$ testcases), count the number of quadruples $(i, j, k)$ such that $S[i..j]$ is of the form `AA` and $S[j+1..k]$ is of the form `BB`.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Counting squares ending at $j$ (`f[j]`) and starting at $j+1$ (`g[j+1]`) naively takes $O(n^2)$ per testcase.
  2. *Combinatorial Word Invariant (Harmonic Keypoint Sampling / Runs Gluing)*:
     Place keypoints at $p, 2p, 3p, \dots, \lfloor n/p \rfloor p$ for every half-length $p \in [1, n/2]$. Any square $AA$ of length $2p$ must cover **exact two consecutive keypoints** $kp$ and $(k+1)p$!
     Given $u = kp$ and $v = (k+1)p$, let $l_1 = \min(p, \text{LCS}(u, v))$ (longest common suffix) and $l_2 = \min(p - 1, \text{LCP}(u+1, v+1))$ (longest common prefix). If $l_1 + l_2 \ge p$, then every starting position in $[u - l_1 + 1, u + l_2 - p + 1]$ begins a square of length $2p$!
  3. *Reverse-Engineering Compilation*: Using Suffix Array + $O(1)$ RMQ on $S$ and $S^R$, each of the $\sum_{p=1}^{n/2} \frac{n}{p} = O(n \log n)$ adjacent keypoint pairs performs two $O(1)$ LCE queries and two range-add difference-array updates on `f[]` and `g[]`. Total time: $O(n \log n)$.
  4. *Boundary Pitfall*: Cap $l_1 \le p$ and $l_2 \le p - 1$ (strictly $< p$ on one side!) so that a long periodic run is not double-counted by adjacent keypoint pairs $(kp, (k+1)p)$ and $((k+1)p, (k+2)p)$!

##### Problem 5B-25: `CF 1037H` — Security (`[EN]` Manthan, Codefest 18 H)
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 10^5$) and $q \le 2 \cdot 10^5$ queries $(l, r, T)$ ($\sum |T| \le 2 \cdot 10^5$), find the lexicographically smallest substring of $S[l..r]$ that is **strictly greater** than $T$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: We must match the longest possible prefix $T[1..i]$ inside $S[l..r]$ that can be followed by a character $c > T[i+1]$ while keeping the entire substring $T[1..i] + c$ inside $S[l..r]$.
  2. *Combinatorial Word Invariant ($\text{endpos}$ Clipping on SAM)*:
     A string $W$ of length $m = i + 1$ sitting at SAM state $u$ occurs completely inside $S[l..r]$ if and only if $u$'s $\text{endpos}$ set contains at least one position $p \in [l + m - 1, r]$!
  3. *Reverse-Engineering Compilation*: Build the SAM of $S$ and merge persistent Segment Trees of $\text{endpos}$ bottom-up along the Link Tree in $O(n \log n)$ time. For each query $(l, r, T)$, walk $T[1..|T|]$ in the SAM as far as possible, and at each depth $i$ check transitions $c > T[i+1]$ via a Segment Tree range query on $[l + i, r]$. Backtrack from largest $i$ down to $0$ until a valid $(i, c)$ is found. Time: $O((n + \sum |T| |\Sigma|) \log n)$.
  4. *Boundary Pitfall*: Querying $[l, r]$ instead of $[l + i, r]$ in the $\text{endpos}$ segment tree counts occurrences of $T[1..i] + c$ whose right endpoint is in $[l, l+i-1]$, meaning their left endpoint starts **strictly before $l$**!

##### Problem 5B-26: `[SCOI2016] 萌萌哒` (`[ZH]` Luogu P3295 / BZOJ 4569)
- **Inline Statement & Constraints**: A decimal number of length $n \le 10^5$ (no leading zero) satisfies $m \le 10^5$ constraints $S[l_1..r_1] = S[l_2..r_2]$. Count how many valid numbers exist modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Naively merging $r_1 - l_1 + 1$ point pairs in a DSU for each of $m$ constraints takes $O(n m)$ time.
  2. *Combinatorial Word Invariant (Binary-Lifting Parallel DSU `倍增并查集`)*:
     Create $\lfloor \log_2 n \rfloor + 1$ DSU layers $k = 0 \dots 16$, where node $(k, i)$ represents the substring $S[i..i + 2^k - 1]$.
     Each constraint $S[l_1..r_1] = S[l_2..r_2]$ of length $L$ splits into **two** overlapping intervals of length $2^k$ ($2^k \le L < 2^{k+1}$), performing two `union` calls at layer $k$.
  3. *Reverse-Engineering Compilation*: After processing all $m$ queries into their top layers, push equivalences **top-down** from layer $k$ to layer $k-1$: if $\text{find}(k, i) = r$, then `union(k-1, i, r)` and `union(k-1, i + 2^{k-1}, r + 2^{k-1})`. If layer $0$ ultimately has $C$ connected components, the answer is $9 \cdot 10^{C-1} \pmod{10^9 + 7}$. Time: $O(n \log n \cdot \alpha(n))$.
  4. *Boundary Pitfall*: Do **not** push down during each query! Push down only **once** from $k = 16$ down to $1$ after all queries are inserted (or skip already-merged pairs at layer $k$).

##### Problem 5B-27: `CF 528D` + `CF 827E` + `CF 1334G` — Algebraic / FFT String Matching Triad (`[EN]` Codeforces)
- **Inline Statement & Constraints**:
  - `CF 827E` ($n \le 5 \cdot 10^5$): Given $S \in \{\text{'V'}, \text{'K'}, \text{'?'}\}^n$, find all periods $d \in [1, n]$ completable by filling `'?'`.
  - `CF 1334G` ($|P|, |T| \le 2 \cdot 10^5$): Given a permutation $\pi$ on `'a'`–`'z'`, find all positions where $T[i+j] \in \{P[j], \pi(P[j])\}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Wildcards (`?`) and 2-choice matches ($T \in \{P, \pi(P)\}$) violate transitivity of equality, breaking KMP/Z.
  2. *Combinatorial Word Invariant (Sum-of-Squares Non-Negativity)*:
     - For wildcards (`CF 827E`): `V` and `K` conflict at distance $d$ iff there exist $i, j$ with $j - i = d$, $S[i] = \text{'V'}$, $S[j] = \text{'K'}$ (or vice versa). One FFT between $1_{S=\text{'V'}}$ and reversed $1_{S=\text{'K'}}$ finds all forbidden differences $k = j - i$, and a period $d$ is valid iff no multiple $m d$ is forbidden!
     - For 2-choice matching (`CF 1334G`): assign random values $v_c \in \mathbb{F}_p$ and evaluate $\sum_{j=0}^{m-1} (T_{i+j} - P_j)^2 (T_{i+j} - \pi(P_j))^2 \equiv 0 \pmod p$ (or over $\mathbb{R}$), expanding the degree-4 polynomial into a sum of products $T_{i+j}^a \cdot Q_{j, a}$ computable in 2–3 FFTs!
  3. *Reverse-Engineering Compilation*: In `CF 827E`, run 1 FFT of size $2^{\lceil \log_2(2n) \rceil}$ and sieve multiples $m d$ in $O(n \log n)$ time.
  4. *Boundary Pitfall*: In `CF 827E`, `'?'` allows different choices if a chain doesn't connect, wait: since $d$ is a **period** of the entire string, every residue class $\bmod d$ must be monochromatic (`V` or `K`), which happens iff no two positions in the same residue class $\bmod d$ have one `'V'` and one `'K'`—i.e., no multiple $m d$ is a `V`–`K` distance!

---

#### Tier 4: Mastery (9 Problems — NOI/ZJOI/BJWC/THUPC Grandmaster Landmarks & Multi-Paradigm Synthesis)

##### Problem 5B-28: `[NOI2018] 你的名字` (`[ZH]` Luogu P4770 / UOJ #395 / LOJ #2720)
- **Inline Statement & Constraints**: Given a reference string $S[1..|S|]$ ($|S| \le 5 \cdot 10^5$) and $q \le 10^5$ queries $(T, l, r)$ ($\sum |T| \le 10^6$), count how many **distinct substrings** of $T$ do **not** occur as a substring of $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: We must intersect two distinct-substring spaces: $T$ (arbitrary query string) and $S[l..r]$ (a dynamically clipped substring of $S$).
  2. *Combinatorial Word Invariant (Dual SAM + Clipped $\text{endpos}$ Match Lengths)*:
     For each prefix $T[1..i]$ ($1 \le i \le |T|$), let $\text{lim}[i]$ be the maximum length $\ell$ such that $T[i - \ell + 1..i]$ occurs inside $S[l..r]$.
     Then in the SAM of $T$ itself, a state $u \in \text{SAM}(T)$ (with representative right endpoint $\text{pos}(u) \in [1, |T|]$) contributes all its lengths in $[\text{minlen}(u), \text{len}(u)]$ that are **strictly greater than $\text{lim}[\text{pos}(u)]$**:
     $$\text{Ans} = \sum_{u \in \text{SAM}(T)} \max\Big(0, \text{len}(u) - \max(\text{minlen}(u) - 1, \text{lim}[\text{pos}(u)])\Big)$$
  3. *Reverse-Engineering Compilation*:
     - Prebuild $\text{SAM}(S)$ with persistent Segment Tree Merge of $\text{endpos}$ in $O(|S| \log |S|)$.
     - For each query $(T, l, r)$, build $\text{SAM}(T)$ in $O(|T|)$, and maintain the current state $v \in \text{SAM}(S)$ and match length $\ell$ as $i$ scans $1 \dots |T|$: if transition $T[i]$ from $v$ has an occurrence in $[l + \ell, r]$ (checked via $\text{endpos}$ Segment Tree query), advance $v \leftarrow \delta(v, T[i])$ and $\ell \leftarrow \ell + 1$; otherwise decrement $\ell$ (stepping $v \leftarrow \text{link}(v)$ when $\ell = \text{minlen}(v) - 1$) until $[l + \ell, r]$ is non-empty!
     - Since $\ell$ increases at most $|T|$ times and decreases at most $|T|$ times, total Segment Tree queries per $(T, l, r)$ is $O(|T|)$, running in $O((|S| + \sum |T|) \log |S|)$!
  4. *Boundary Pitfall*: When $v$ cannot extend in $S[l..r]$, you MUST decrement $\ell \leftarrow \ell - 1$ one by one (only jumping $v \leftarrow \text{link}(v)$ when $\ell < \text{minlen}(v)$), NOT jump $\ell \leftarrow \text{len}(\text{link}(v))$ directly—because a longer prefix of state $v$ might fail the $[l + \ell, r]$ boundary while a shorter length **still inside the same SAM state $v$** satisfies $p - \ell' + 1 \ge l$!

##### Problem 5B-29: `[ZJOI2017] 字符串` (`[ZH]` Luogu P3763 / LOJ #2270 — Significant Suffixes Benchmark)
- **Inline Statement & Constraints**: Given a string $S[1..n]$ ($n \le 2 \cdot 10^5$) over an integer alphabet with range-add updates (adding $d$ to $S[l..r]$), and queries $(l, r)$: find the starting position $i \in [l, r]$ of the **lexicographically smallest suffix** of the substring $S[l..r]$ (throwing ties to smaller or larger $i$ as specified).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A suffix of $S[l..r]$ is a truncated suffix of $S$ clipped at $r$. Comparing two suffixes of $S[l..r]$ of lengths $|u| < |v|$ when $u$ is a prefix of $v$ ends in a tie or makes $u$ smaller, AND when we merge two segment tree nodes $[l, m]$ and $[m+1, r]$, appending $S[m+1..r]$ to the right of candidates in $[l, m]$ can change which suffix in $[l, m]$ wins!
  2. *Combinatorial Word Invariant (The Significant Suffixes Theorem)*:
     Fix any interval $[l, m]$. How many starting positions $i \in [l, m]$ can *possibly* become the lexicographically minimal suffix of $S[l..r]$ for *some* right extension $T = S[m+1..r]$?
     Suppose $u = S[i..m]$ and $v = S[j..m]$ ($|u| < |v| < 2|u|$) are both candidates.
     - If $u$ is NOT a prefix of $v$, their relative order is decided inside $[l, m]$ before reaching $m+1$, so the larger one is permanently dead!
     - If $u$ IS a prefix of $v$, since $u$ is also a suffix of $v$, $u$ is a **border** of $v$ of length $> |v|/2$, so $v = w u$ where $|w| = |v| - |u| < |u|$. For any right extension $T$, comparing $v T = w u T$ against $u T$ is equivalent to comparing $w w T'$ against $w T'$: if $u T < v T$, then $w u T > u T$ (and by transitivity $w^2 u T > w u T > u T$), so **$v$ can never strictly beat $u$** (and in case of ties, the tie-breaking rule eliminates one of them)!
     Therefore, adjacent candidate lengths satisfy $|v| \ge 2|u|$, meaning any Segment Tree node $[l, m]$ has **at most $\lceil \log_2(m - l + 1) \rceil \le 18$ Significant Suffixes**!
  3. *Reverse-Engineering Compilation*: Each Segment Tree node stores its $\le 18$ candidate suffix indices. Merging two nodes filters the $\le 36$ candidates down to $\le 18$ using $O(1)$ LCE (via block-hash + Fenwick for range-add updates).
  4. *Boundary Pitfall*: Range-add updates $S[i] \leftarrow S[i] + d$ shift all polynomial hashes in $[l, r]$ by $d \cdot \sum_{k=l}^r B^k$, which is maintained in a Fenwick tree / Segment Tree to keep $O(1)$ LCE!

##### Problem 5B-30: `[BJWC2018] Border 的四种求法` (`[ZH]` Luogu P4482)
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 2 \cdot 10^5$) and $q \le 2 \cdot 10^5$ queries $(l, r)$, find the length of the longest proper border of the substring $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: KMP cannot be run per query $[l, r]$, and borders of $S[l..r]$ are not borders of $S[1..r]$.
  2. *Combinatorial Word Invariant (SAM Link-Tree HLD + 2D Range Minimum)*:
     $S[l..p]$ ($l \le p < r$) is a border of $S[l..r]$ iff $S[l..p]$ is a suffix of $S[1..r]$, which means in the SAM of $S$, the state $u = \text{LCA}_{\text{LinkTree}}(\text{pref}(p), \text{pref}(r))$ has $\text{len}(u) \ge p - l + 1$, i.e.:
     $$p - \text{len}(\text{LCA}(\text{pref}(p), \text{pref}(r))) \le l - 1$$
  3. *Reverse-Engineering Compilation*:
     Decompose the SAM Link Tree via Heavy-Light Decomposition (HLD). The path from $\text{pref}(r)$ to the root visits $O(\log n)$ heavy chains. At each light-edge jump at ancestor $w$, any $p$ in the off-chain subtree of $w$ has $\text{LCA}(\text{pref}(p), \text{pref}(r)) = w$, requiring $p \in [l, \min(r - 1, l - 1 + \text{len}(w))]$ (a 1D predecessor query in $\text{endpos}(w)$!). Along each heavy chain, $\text{LCA}$ is the shallower of the two chain-heads, reducing to an offline 2D Segment Tree query $p - \text{len}(\text{head}(p)) \le l - 1$ for $p < r$. Total time: $O((n + q) \log^2 n)$.
  4. *Boundary Pitfall*: Also قابل to be solved via **Internal Pattern Matching ($O(\log n)$ border buckets)**: split candidate border lengths into power-of-2 intervals $[2^k, 2^{k+1})$; in each interval, occurrences of $S[l..l+2^k-1]$ in $S[r-2^{k+1}+1..r]$ form a single arithmetic progression!

##### Problem 5B-31: `[THUPC 2021] 区间 LCS` / `LOJ #6564` (`[ZH]` Seaweed Matrix Benchmark)
- **Inline Statement & Constraints**: Given strings $A[1..n]$ and $B[1..m]$ ($n, m \le 2000$ or $n, m \le 5 \cdot 10^4$) and $q \le 2 \cdot 10^5$ queries $(l, r)$, compute $\text{LCS}(A[1..n], B[l..r])$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Computing LCS from scratch per query $[l, r]$ takes $O(q n m)$ time.
  2. *Combinatorial Word Invariant (Tiskin's Seaweed Wiring & Unit-Monge Dominance)*:
     Place $n$ wires entering on the left wall at rows $-n + 0.5, \dots, -0.5$ and $m$ wires entering on the top wall at columns $0.5, \dots, m - 0.5$. At each cell $(i, j)$:
     - If $A[i] \neq B[j]$ OR the two entering wires have already crossed earlier, the two wires **cross** (swap).
     - If $A[i] = B[j]$ and the two entering wires have **never** crossed yet, they **bounce** (do not cross).
     Then $\text{LCS}(A[1..n], B[l..r])$ equals $(r - l + 1)$ minus the number of wires entering on the top in $[l - 0.5, r - 0.5]$ that exit on the bottom in $[l - 0.5, r - 0.5]$!
  3. *Reverse-Engineering Compilation*:
     - For $n, m \le 2000$: simulate the $n \times m$ grid wire swaps in $O(nm)$ time, then answer all $q$ queries via a 2D dominance / Fenwick tree count of `(entry_col >= l)` and `(exit_col <= r)` in $O(q \log m)$ time!
     - For $n, m \le 5 \cdot 10^4$: run Tiskin's $O((n+m)\log^2(n+m))$ divide-and-conquer Unit-Monge Seaweed multiplication $\boxdot$.
  4. *Boundary Pitfall*: Wires start ordered by their initial coordinate ($-n \dots m$), so "have already crossed" is equivalent to checking whether the left-entering wire's origin index is **strictly greater** than the top-entering wire's origin index!

##### Problem 5B-32: `LOJ #6071` / `[国家集训队论文 — 徐毅]` — Substring Distinct Palindromes (`[ZH]` Offline PAM + LCT / `slink` + Fenwick)
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 10^5$ or $3 \cdot 10^5$) and $q \le 2 \cdot 10^5$ queries $(l, r)$, output the number of **distinct palindromic substrings** inside $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A palindrome $P$ ending at $i \in [l, r]$ is inside $S[l..r]$ iff $i - |P| + 1 \ge l$. We must count each distinct palindrome occurring in $S[l..r]$ **exact once** (at its last occurrence $\le r$).
  2. *Combinatorial Word Invariant ($O(\log n)$ `slink` Last-Occurrence Jumps)*:
     Sweep right endpoint $r$ from $1$ to $n$, maintaining in a Fenwick tree at each left endpoint $L$ how many distinct palindromes have their **latest occurrence $\le r$ starting at $L$**.
     When $r$ advances, all palindromic suffixes of $S[1..r]$ get a new occurrence ending at $r$. Partition these suffixes into $O(\log r)$ arithmetic progressions via `slink`.
     For an AP $u \to \dots \to \text{slink}(u)$ of step $d$: every palindrome $v \neq \text{top}(u)$ in the AP occurred just $d$ positions ago at $r - d$ (since $u$ has period $d$)! Thus for all $v$ in the AP except the longest one $u$, their previous last-occurrence endpos was **exact $r - d$**, meaning their previous starting positions formed a contiguous interval $[L_1, L_2]$ shifted by $d$—Wait: they ALL had different lengths $\ell, \ell-d, \dots$, so their starting positions at their previous occurrences ($r - d - (\ell - kd) + 1$) and new occurrences ($r - \ell + 1$) cancel in telescopes except for **one removed start position** $\text{last\_end}(u) - \text{len}(u) + 1$ and **one added start position** $r - \text{len}(\text{slink}(u)) - d + 1$!
  3. *Reverse-Engineering Compilation*: For each of the $O(\log r)$ `slink` jumps $u$ from the longest palindrome suffix at $r$:
     - Subtract $1$ at $\text{last\_pos}[u] - \text{len}(u) + 1$ in the Fenwick tree,
     - Add $1$ at $r - \text{len}(\text{slink}(u)) - \text{diff}(u) + 1$ (wait: actually at $\text{last\_pos}[u] - \text{len}(\text{slink}(u)) - \text{diff}(u) + 1$? Let's be exact: every palindrome $v$ of length $\ell_v$ in the chain has previous occurrence ending at $\text{last\_pos}[u]$ because $u$ covers them all at $\text{last\_pos}[u]$! No: a shorter palindrome $v$ in the chain also occurred at $r$ itself via $u$, AND its previous occurrence was at $\max(\text{last\_pos}[u], r - d)$!).
     Wait—let's state the **exact telescopy invariant**:
     At step $r$, because $u$ is a palindrome of period $d$, every proper member $v$ of $u$'s AP chain already occurred at $r - d$! Therefore, for every $v \neq u$ in the chain, its previous last-occurrence right endpoint was $r - d$, so its previous starting position was:
     $$(r - d) - \text{len}(v) + 1 = r - (\text{len}(v) + d) + 1 = r - \text{len}(\text{prev\_in\_chain}(v)) + 1$$
     which is **identical to the NEW starting position of its predecessor in the chain at step $r$**!
     Thus, across the entire AP chain of $u$, the new starting positions at $r$ and the old starting positions at $r - d$ **telescope completely**, leaving only:
     - **$-1$** at the old starting position of $u$ itself: $\text{last\_pos}[u] - \text{len}(u) + 1$, and
     - **$+1$** at the new starting position of the shortest member of $u$'s chain: $r - (\text{len}(\text{slink}(u)) + \text{diff}(u)) + 1$!
     And we update $\text{last\_pos}[u] \leftarrow r$ on the Segment Tree over the PAM fail-tree (via subtree max).
     Total time: $O(n \log^2 n + q \log n)$!
  4. *Boundary Pitfall*: This telescoping identity ($(r - d) - \text{len}(v) + 1 = r - (\text{len}(v) + d) + 1$) is one of the deepest miracles in competitive stringology—if you try to update all members of the AP instead of using this $+1 / -1$ telescopy, it degrades to $O(n^2)$!

##### Problem 5B-33: `[国家集训队论文 2019 — 金策]` / `LOJ #171` / `UOJ` — Substring Distinct Squares via Runs + 2D Sweep-Line (`[ZH]` Runs Benchmark)
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 10^5$ or $2 \cdot 10^5$) and $q \le 2 \cdot 10^5$ queries $(l, r)$, count the number of **distinct square substrings** (or all square occurrences) inside $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A string can have $\Theta(n^2)$ square occurrences, but at most $< 2n$ **distinct** squares (Fraenkel–Simpson / Deza–Franek–Thierry bound $\le n - \Theta(\log n)$)!
  2. *Combinatorial Word Invariant (Runs Generation of All Squares)*:
     Every square substring $S[i..i+2p-1]$ of primitive root period $p$ is contained inside a **unique maximal Run** $R = [l_R, r_R, p]$ of period $p$!
     Moreover, two squares of the same primitive period $p$ inside the same run $R$ are equal as strings if and only if their starting positions satisfy $i_1 \equiv i_2 \pmod p$!
  3. *Reverse-Engineering Compilation*:
     - Enumerate all maximal Runs $R = [l_R, r_R, p]$ in $O(n \log n)$ (or $O(n)$ via Lyndon Tree).
     - By the Runs Theorem, $\sum (r_R - l_R + 1 - 2p + 1) / p = \sum (\text{exp}(R) - 1) < 2n$, meaning there are only **$O(n)$ primitive square equivalence classes across all runs** (or if counting all $k p$ multiples, $\sum \lfloor \text{len}(R)/2p \rfloor < n$)!
     - Sweep right endpoint $r = 1 \dots n$ just like Problem 5B-32: each square occurrence ending at $r$ updates the last-occurrence starting position of its string equivalence class (identified via SAM/SA or run ID) in a Fenwick tree in $O((n \log n + q) \log n)$ time!
  4. *Boundary Pitfall*: The same square string $W^2$ can appear in **two different runs** at earlier and later positions of $S$; you must deduplicate identical squares across different runs using SA/SAM substring IDs (`endpos` equivalence node + length) when tracking `last_occurrence`!

##### Problem 5B-34: `[ZJOI2015] 诸神眷顾的幻想乡` (`[ZH]` Luogu P3346 / BZOJ 3926 — Tree Generalized SAM)
- **Inline Statement & Constraints**: Given an unrooted tree $T$ with $n \le 10^5$ vertices, each labeled with a character in $\{0, \dots, c-1\}$ ($c \le 10$), and **at most $20$ leaves** ($\deg(v) = 1$), count the number of distinct strings formed by simple paths in $T$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: There are $\binom{n}{2}$ directed simple paths in a tree, and building a Generalized SAM on all $n$ rootings takes $O(n^2)$ states.
  2. *Combinatorial Word Invariant (Leaf-Rooting Path Coverage)*:
     Every simple path $u \leadsto v$ in a tree can be extended to a path starting at some **leaf** $L$ and moving monotonically away from $L$! Therefore, every simple-path string in $T$ is a **substring of a root-to-node path when $T$ is rooted at one of the $\le 20$ leaves**!
  3. *Reverse-Engineering Compilation*: Root the tree at each of the $\le 20$ leaves in turn. Insert all 20 rooted trees into a single Generalized SAM (using parent pointers `sam_pos[parent]` during BFS/DFS from each leaf root!). Total states in the GSAM is at most $2 \times (20 n) = 4 \cdot 10^6$. Sum $\sum_{u} (\text{len}(u) - \text{len}(\text{link}(u)))$ in $O(20 n c)$ time!
  4. *Boundary Pitfall*: You MUST use true Generalized SAM insertion (checking if `ch[p][c]` already exists when branching from `sam_pos[tree_parent]`, or BFS order) so zero-length clone states are never created!

##### Problem 5B-35: `[十二省联考 2019] 字符串问题` (`[ZH]` Luogu P5284 / LOJ #3049)
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 2 \cdot 10^5$), $n_a$ substrings $A_i = S[l_{a,i}..r_{a,i}]$, $n_b$ substrings $B_j = S[l_{b,j}..r_{b,j}]$, and $m$ directed edges $A_i \to B_j$. Additionally, there is a directed edge from every $B_j$ to every $A_i$ of whom $B_j$ is a **prefix**. Each $A_i$ has weight $|A_i|$. Find the maximum total weight of a walk in this graph (or $-1$ if a cycle exists).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: "Is a prefix of" is a suffix link condition on the **reversed string** $S^R$ (or Suffix Tree of $S$). Explicitly adding edges from $B_j$ to all $A_i$ in its subtree creates $O(n_a n_b)$ edges.
  2. *Combinatorial Word Invariant (SAM of $S^R$ + Intra-Node Length Sorting)*:
     In the SAM of $S^R$, $B_j$ is a prefix of $A_i$ iff $B_j$'s node $u_B$ is an ancestor of $A_i$'s node $u_A$ in the Link Tree (or $u_B = u_A$ AND $|B_j| \le |A_i|$)!
  3. *Reverse-Engineering Compilation*:
     - Locate each $A_i$ and $B_j$ in $\text{SAM}(S^R)$ via Link-Tree binary lifting in $O(\log n)$.
     - Within each SAM node $u$, sort all $A_i$ and $B_j$ attached to $u$ by length (placing $B_j$ before $A_i$ on ties), and link them in a **prefix-optimised chain** inside $u$ so that $B_j$ only points to longer $A_i$ in $u$ and to all children of $u$ in the Link Tree!
     - Run topological sort + DAG longest path in $O((n + n_a + n_b) \log n + m)$ time.
  4. *Boundary Pitfall*: If $B_j$ and $A_i$ map to the **exact same SAM node $u$** with $|B_j| > |A_i|$, $B_j$ is NOT a prefix of $A_i$! Failure to sort items inside each SAM node by length creates false cycles and WA.

##### Problem 5B-36: `Universal Cup / QOJ Synthesis` — Dynamic Morphic & Free-Group Substring LCE (`[EN]` / `[ZH]` Frontier Synthesis)
- **Inline Statement & Constraints**: Maintain a sequence of strings where operations concatenate strings, apply involution/stack cancellation (`AA` $\to \epsilon$), or query the Longest Common Prefix (LCE) of the **stack-reduced forms** of two substrings $S[l_1..r_1]$ and $S[l_2..r_2]$ ($n, q \le 10^5$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: In $S[l..r]$, characters inside $[l, r]$ can cancel with characters far to the right, so the $k$-th character of $\text{red}(S[l..r])$ is not at $l + k - 1$!
  2. *Combinatorial Word Invariant (Segment Tree Binary-Search Cancellation + $SL_2(\mathbb{F}_p)$ Prefix Hash)*:
      Wait: while $SL_2(\mathbb{F}_p)$ tests whether $\text{red}(S[l..m]) = \text{red}(S[l'..m'])$ in $O(1)$, two different prefixes $S[l..m_1]$ and $S[l'..m_2]$ can reduce to the **same** prefix of length $k$ of the full reduced strings $\text{red}(S[l..r])$ and $\text{red}(S[l'..r'])$ ONLY if the suffix after $m_1$ does not pop into $\text{red}(S[l..m_1])$!
     To handle pops across segment tree nodes deterministically (like bracket-tree / `Segment Tree Beats` for stack reduction, orTrie-ancestry binary lifting):
     - In the static / append-only case, $\text{red}(S[l..r])$ in the Stack Trie is the **simple tree path** between $u_{l-1}$ and $u_r$ in the Stack Trie!
     - **Crucial Tree-Path Discovery**: Because $u_{l-1}$ and $u_r$ are nodes in the deterministic Stack Trie $\mathcal{T}$ (from Iteration 99.3), pushing/popping along $S[l..r]$ simply walks from $u_{l-1}$ down to $w = \text{LCA}_{\mathcal{T}}(u_{l-1}, u_r)$ (popping the suffix of $\text{red}(S[1..l-1])$ below $w$) and then down to $u_r$!
     - Therefore, the reduced string $\text{red}(S[l..r])$ is **literally the label of the unique tree path from $u_{l-1}$ to $u_r$ in the Stack Trie $\mathcal{T}$**!
  3. *Reverse-Engineering Compilation*:
     - Build the Stack Trie $\mathcal{T}$ of size $\le n + 1$ in $O(n \log |\Sigma|)$ time.
     - Store standard polynomial rolling hashes (moving up and down via HLD / binary lifting) on the tree $\mathcal{T}$!
     - Then for any two substrings $S[l_1..r_1]$ and $S[l_2..r_2]$, their reduced forms $\text{red}(S[l_1..r_1])$ and $\text{red}(S[l_2..r_2])$ are simply the tree paths $u_{l_1 - 1} \leadsto u_{r_1}$ and $u_{l_2 - 1} \leadsto u_{r_2}$ in $\mathcal{T}$!
     - We find the LCE of two tree paths in $\mathcal{T}$ via binary lifting + hash comparison (or HLD + Suffix Array on the Euler/HLD tour of $\mathcal{T}$) in $O(\log n)$ time per query!
  4. *Boundary Pitfall*: Notice how combining the **Stack Trie path invariant** ($\text{red}(S[l..r]) = \text{path}_{\mathcal{T}}(u_{l-1}, u_r)$) with **Tree Path LCE** completely eliminates internal stack-popping ambiguity: any character on the path $u_{l-1} \leadsto \text{LCA}(u_{l-1}, u_r) \leadsto u_r$ is guaranteed never to be popped by anything inside $[l, r]$ because $\mathcal{T}$ is a tree and the shortest path between $u_{l-1}$ and $u_r$ never backtracks!

---

## Summary of Cohort 2 Wave 5B Discoveries & Post-Research Curriculum Recommendations for Phase 1.5

1. **Dedicated Chapter on Combinatorics on Words & Morphic / Recursive Strings**:
   - The 6 equivalent characterizations of Sturmian words, Fibonacci near-commutativity $F_{k-1}F_{k-2} = \pi_k xy$, Zeckendorf / Ostrowski numeration, Rytter's Singular Words, Thue–Morse overlap-freeness, and the `CF 1466G` / KMP-matrix morphism compilation must form a full standalone chapter.
2. **Dedicated Coverage of Non-Abelian Group Hashing ($SL_2(\mathbb{F}_p)$) + Stack Trie Path Reduction**:
   - Pair the randomized trace-zero determinant-$(-1)$ involution matrices $M_c \in GL_2(\mathbb{F}_p)$ (for dynamic segment-tree updates) with the deterministic **Stack Trie path isomorphism** $\text{red}(S[l..r]) = \text{path}_{\mathcal{T}}(u_{l-1}, u_r)$ (which reduces static stack-reduced substring LCE and lexicographical comparison to tree-path LCE!).
3. **Frontier Section / Appendix on String Attractors ($\gamma$), $\tau$-Synchronizing Sets, and Cartesian-Tree KMP**:
   - Include the Parent-Distance (`PD`) $O(n+m)$ Cartesian-Tree KMP reduction, Kempa–Prezza string attractor duality with minimal SAM representatives, and Kempa–Kociumaka $\tau$-synchronizing sets in the textbook's advanced frontier module.
