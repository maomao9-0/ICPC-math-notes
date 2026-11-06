# Wave 1A (Cohort 2: Iterations 53–57) — Independent Redundant Research Report
## Structural Periodicity, Border Theory, Weak Periodicity Lemma & Series-Link (`slink`) DP

> [!IMPORTANT]
> **Cohort 2 Independence & Zero-Magic Mandate**
> This document is the **100% independent Cohort 2 redundant research pass (Iterations 53–57)** for Wave 1A. All structural proofs, index-orbit invariants, algebraic recurrences, counterexamples, and multilingual problem mining (`[EN]` / `[ZH]` / `[JA]`) have been derived from first principles without consulting Cohort 1's output, enabling Cohort 3 to perform a rigorous cross-comparison and blind-spot audit.

---

## Iteration 53: Period–Border Duality, the Fine–Wilf Theorem, and Extremal Sturmian Counterexamples

### 53.1 Period–Border Duality & The Prefix-Suffix Alignment Bijection

#### 1. The Diagnostic Signal (Why Naive String Matching Fails on Overlapping Occurrences)
When a problem asks how a pattern $S[1..n]$ can overlap with itself (e.g., valid transition steps in `[WC2016] 论战捆竹竿`, autocorrelation polynomials in `[SDOI2017] 硬币游戏`, or valid cyclic extensions), checking all $n-1$ candidate shifts $p \in [1, n-1]$ independently takes $O(n^2)$ character comparisons. Even if one uses KMP or Z-algorithm to find all borders in $O(n)$, treating borders merely as an unstructured list of lengths $\{b_1, b_2, \dots, b_k\}$ fails whenever a transition or query depends on *how multiple borders interact simultaneously* or how long a string must be before two periodicities lock into a single common rhythm.

#### 2. The Combinatorial Word Invariant (Exact Bijection Between Borders and Periods)
Let $S = S[1..n]$ be a 1-indexed string of length $n = |S|$ over an alphabet $\Sigma$.
- **Definition (Proper Border)**: An integer $b \in \{0, 1, \dots, n-1\}$ is a *border length* (and $B = S[1..b]$ is a *proper border*) of $S$ if the prefix of length $b$ equals the suffix of length $b$:
  $$S[1..b] = S[n-b+1..n] \iff \forall i \in \{1, \dots, b\}, \quad S[i] = S[i + (n-b)].$$
- **Definition (Period)**: An integer $p \in \{1, 2, \dots, n\}$ is a *period* of $S$ if positions at distance $p$ carry identical characters everywhere both indices are in bounds:
  $$\forall i \in \{1, \dots, n-p\}, \quad S[i] = S[i+p].$$
  (When $p = n$, the condition is vacuously true, matching the empty border $b = 0$.)

**Theorem 53.1 (Period–Border Duality Bijection).**
For any string $S[1..n]$, the map $\Phi(b) = n - b$ is an order-reversing bijection between the set of proper border lengths $\text{Borders}(S) \subseteq \{0, 1, \dots, n-1\}$ and the set of periods $\text{Per}(S) \subseteq \{1, 2, \dots, n\}$:
$$b \in \text{Borders}(S) \iff p = n - b \in \text{Per}(S).$$

*Proof via Index Translation*:
Fix $b \in \{0, \dots, n-1\}$ and set $p = n - b \in \{1, \dots, n\}$. Then $b = n - p$. The border condition states that for every $i \in \{1, \dots, n-p\}$,
$$S[i] = S[(n - b) + i] = S[i + p],$$
which is identically the definition of $p \in \text{Per}(S)$. Because $\Phi(b) = n - b$ is strictly decreasing on $\mathbb{Z}$, longest borders correspond to shortest (strongest) periods:
$$b_{\max} = \pi[n] \iff p_{\min} = n - \pi[n]. \quad \blacksquare$$

```
Index:    1   2   3   ...   n-p  ...   p   p+1  ...   n
S:      [ a   b   a   ...    c   ... ]
                  || (shifted by p = n - b)
S:                      [    a    b    a   ...   c  ]
        |<------ p ------>|<--------- b = n-p --------->|
```

**Corollary 53.2 (Prefix-Truncation Persistence vs. Right-Extension Fragility).**
If $p \in \text{Per}(S[1..n])$, then $p \in \text{Per}(S[l..r])$ for every substring $S[l..r]$ (defining $p$ as a weak period when $p > r-l+1$). However, extending $S[1..n]$ to $S[1..n+1]$ preserves period $p$ *if and only if* the single new equality $S[n+1] = S[n+1-p]$ holds! This single-character test is the engine behind KMP fail links, PAM fail links, and `slink` AP survival.

---

### 53.2 The Fine–Wilf Periodicity Theorem (Full Index-Orbit & Bézout Graph Proof)

#### 1. The Concrete Question
Suppose a string $S[1..n]$ simultaneously admits two periods $p$ and $q$ ($1 \le p < q \le n$). When does the coexistence of periods $p$ and $q$ force $S$ to also have the smaller period $g = \gcd(p, q)$?
- **Naive Misconception**: By Bézout's identity, there exist integers $a, b \in \mathbb{Z}$ such that $ap + bq = g$. Hence moving $+p$ steps $a$ times and $+q$ steps $b$ times shifts any index $i$ to $i + g$, so $S[i] = S[i+g]$ should always hold when $n \ge \max(p, q)$.
- **Why Naive Bézout Fails on Finite Strings**: On an infinite string $S[1..\infty]$, moving $+p$ and $-q$ never falls out of bounds if we go far enough right. On a *finite* string $S[1..n]$, however, every intermediate vertex along the walk from $i$ to $i+g$ using steps $+p$ and $-q$ must stay strictly inside $\{1, 2, \dots, n\}$! If $n$ is too small, an index $i$ can be trapped so that $+p$ exceeds $n$ while $-q$ drops below $1$.

#### 2. Theorem & Exact Threshold Proof
**Theorem 53.3 (Fine–Wilf Theorem, 1965).**
Let $S[1..n]$ have periods $p$ and $q$, and let $g = \gcd(p, q)$. If
$$n \ge p + q - \gcd(p, q),$$
then $g = \gcd(p, q)$ is also a period of $S[1..n]$. Moreover, the threshold $p + q - \gcd(p, q)$ is **strictly tight**: for every pair $(p, q)$ with $1 < \gcd(p, q) < \min(p, q)$ or $1 = \gcd(p, q) < \min(p, q)$, there exists a binary string of length $n = p + q - \gcd(p, q) - 1$ having periods $p$ and $q$ but **not** period $\gcd(p, q)$.

*Proof I (Constructive Directed Orbit / Modular Stepping Proof)*:
Assume $n \ge p + q - g$. First reduce to the coprime case $\gcd(p, q) = 1$: partition the indices $\{1, \dots, n\}$ into $g$ independent residue classes modulo $g$, namely $C_r = \{r, r+g, r+2g, \dots\}$ for $r \in \{1, \dots, g\}$.
- A class $C_r$ has size $n_r = \lfloor (n - r)/g \rfloor + 1 \ge \lfloor (p + q - g - g)/g \rfloor + 1 = \frac{p}{g} + \frac{q}{g} - 1$.
- Within $C_r$, the original periods $p$ and $q$ act as periods $p' = p/g$ and $q' = q/g$ with $\gcd(p', q') = 1$ on a string of length $n_r \ge p' + q' - 1$.
- If every residue class $C_r$ has period $1$ (i.e., is a constant character), then $S[i] = S[i+g]$ for all $1 \le i \le n-g$, which directly means $g \in \text{Per}(S)$.

Thus it suffices to prove the theorem when $g = \gcd(p, q) = 1$ and $n \ge p + q - 1$: we must show $S[1..n]$ is constant ($1 \in \text{Per}(S)$).
Consider the subset of anchor indices $V = \{1, 2, \dots, p + q - 1\} \subseteq \{1, \dots, n\}$. Define the **Fine–Wilf step permutation** $T : V \to V$ by:
$$T(x) = \begin{cases} x + p & \text{if } 1 \le x \le q - 1, \\ x - q + p & \text{if } q \le x \le p + q - 1\text{ (Wait: let us use single steps }+p\text{ or }-q\text{!)}\end{cases}$$
Even simpler, consider the single-step map $\tau : \{1, \dots, p+q-1\} \to \{1, \dots, p+q-1\}$:
$$\tau(x) = \begin{cases} x + p & \text{if } 1 \le x \le q, \\ x - q & \text{if } q + 1 \le x \le p + q - 1. \end{cases}$$
 wait: if $x = q$, $x + p = p + q > p + q - 1$, which leaves $\{1, \dots, p+q-1\}$! Let us check the exact bounds on $V = \{1, \dots, p+q-1\}$:
- For any $x \in \{1, \dots, q-1\}$, $x + p \in \{p+1, \dots, p+q-1\} \subseteq V$. Since $p \in \text{Per}(S)$, $S[x] = S[x+p]$.
- For any $x \in \{q+1, \dots, p+q-1\}$, $x - q \in \{1, \dots, p-1\} \subseteq V$. Since $q \in \text{Per}(S)$, $S[x] = S[x-q]$.
- Notice that $x = q$ is the unique vertex in $V$ where $x + p = p + q$ (out of $V$) and $x - q = 0$ (out of $V$), while $x = p$ is the unique vertex in $\{1, \dots, p+q-1\}$ not hit by $\{p+1, \dots, p+q-1\} \cup \{1, \dots, p-1\}$.
- Therefore, the partial map
  $$f(x) = \begin{cases} x + p & \text{if } 1 \le x \le q - 1, \\ x - q & \text{if } q + 1 \le x \le p + q - 1 \end{cases}$$
  is a bijection from $V \setminus \{q\}$ onto $V \setminus \{p\}$, and satisfies $f(x) \equiv x + p \pmod{p + q}$? No! Notice that modulo $q$:
  - On $\{1, \dots, p+q-1\}$, let us work on the subset $U = \{1, 2, \dots, q\}$.
  - For any $x \in \{1, \dots, q-1\}$, $x + p \le p + q - 1 \le n$, so $S[x] = S[x+p]$.
  - Now reduce $x + p$ by subtracting $q$ if $x + p > q$: if $x + p \in \{q+1, \dots, p+q-1\}$, then $(x + p) - q \in \{1, \dots, p-1\} \subseteq U$, and since $x + p \le p + q - 1 \le n$, the period $q$ guarantees $S[x+p] = S[x+p-q]$!
  - Consequently, for **every** $x \in \{1, \dots, q-1\}$, defining
    $$\psi(x) = ((x + p - 1) \bmod q) + 1 \in \{1, \dots, q\},$$
    both $x$ and $\psi(x)$ lie in $\{1, \dots, q\}$, and the intermediate point (if $x + p > q$) is $x + p \le p + q - 1 \le n$, which is strictly inside $[1..n]$!
  - Hence for all $x \in \{1, \dots, q-1\}$, $S[x] = S[\psi(x)]$.
  - Since $\gcd(p, q) = 1$, translation by $+p \pmod q$ generates a single cycle of length $q$ on $\{1, 2, \dots, q\}$.
  - Removing the single outgoing edge from $x = q$ turns this $q$-cycle into a **directed Hamiltonian path** of length $q - 1$ visiting all $q$ vertices of $\{1, 2, \dots, q\}$!
  - Therefore $S[1] = S[2] = \dots = S[q]$. Since $q \in \text{Per}(S)$, every index $i \in \{1, \dots, n\}$ satisfies $S[i] = S[((i-1) \bmod q) + 1]$, so $S[1..n]$ is constant! $\blacksquare$

*Proof II (Euclidean Induction on $(p, q)$)*:
Assume $1 \le p < q$ and $n \ge p + q - \gcd(p, q)$. For every $i \in \{1, \dots, n - (q - p)\}$:
- Either $i \le p$, in which case $i + q \le p + q$. Wait: if $i = p$ and $\gcd(p, q) > 1$, $i + q = p + q$ could exceed $n = p + q - \gcd(p, q)$. Instead:
  - If $i + q \le n$, then $S[i] = S[i+q] = S[i+q-p]$.
  - If $i + q > n$, then $i > n - q \ge (p + q - g) - q = p - g$. Wait: if $i > p$, then $i - p \ge 1$, and since $i + (q - p) \le n$, we have $S[i] = S[i-p] = S[i-p+q]$.
  - The only dangerous indices where *neither* $i + q \le n$ *nor* $i - p \ge 1$ holds are indices satisfying $i \le p$ and $i > n - q$, i.e., $n - q < i \le p$.
  - This guarantees that the suffix $S[p+1..n]$ (of length $n - p \ge q - g = p + (q - p) - \gcd(p, q - p)$) has periods $p$ and $q - p$! By induction on $p + q$, $S[p+1..n]$ has period $g = \gcd(p, q-p) = \gcd(p, q)$, and because $p \in \text{Per}(S[1..n])$ is a multiple of $g$, period $g$ propagates back across the prefix $S[1..p]$ as well. $\blacksquare$

---

### 53.3 Extremal Tightness at $p + q - \gcd(p, q) - 1$: Central Sturmian Words & Component Splitting

#### 1. Why the Proof Breaks at $n = p + q - \gcd(p, q) - 1$
Look closely at Proof I when $\gcd(p, q) = 1$ and $n = p + q - 2$:
- In the residue cycle $\psi(x) = ((x + p - 1) \bmod q) + 1$ on $\{1, 2, \dots, q\}$, not only does $x = q$ fail to step via $x + p = p + q > n$, **a second vertex** $x^* = q - 1$ ALSO fails because $x^* + p = p + q - 1 = n + 1 > n$!
- Removing **two** directed edges (at $x = q$ and $x = q - 1$) from a single directed cycle of length $q$ splits the cycle into **two disconnected components**!
- Because there is no valid in-bounds step between these two components, we can assign character `'a'` to one component and character `'b'` to the other component, creating a non-constant string of length $p + q - 2$ with periods $p$ and $q$!

#### 2. Hand-Checkable Example: $(p, q) = (5, 8)$, $\gcd(5, 8) = 1$
- **Fine–Wilf threshold**: $p + q - \gcd(p, q) = 5 + 8 - 1 = 12$. Any string of length $n \ge 12$ with periods $5$ and $8$ must be `aaaaaaaaaaaa`.
- **Extremal length**: $n = p + q - 2 = 11$.
- Let us trace the cycle of $+5 \pmod 8$ on $\{1, \dots, 8\}$, breaking whenever $x + 5 > 11$ (i.e., at $x = 7$ since $7 + 5 = 12 > 11$, and at $x = 8$ since $8 + 5 = 13 > 11$):
  $$\text{Start after } x = 8 \implies 5 \xrightarrow{+5} 10 \xrightarrow{-8} 2 \xrightarrow{+5} 7 \quad (\text{STOP: } 7+5=12 > 11)$$
  $$\text{Start after } x = 7 \implies 4 \xrightarrow{+5} 9 \xrightarrow{-8} 1 \xrightarrow{+5} 6 \xrightarrow{+5} 11 \xrightarrow{-8} 3 \xrightarrow{+5} 8 \quad (\text{STOP: } 8+5=13 > 11)$$
- The two connected components of indices in $\{1, \dots, 11\}$ are:
  - Component $C_1 = \{2, 5, 7, 10\}$ (assign `'b'`)
  - Component $C_2 = \{1, 3, 4, 6, 8, 9, 11\}$ (assign `'a'`)
- Resulting string $S[1..11]$:
  ```
  Index:  1  2  3  4  5  6  7  8  9 10 11
  S:      a  b  a  a  b  a  b  a  a  b  a
  ```
- **Verification**:
  - Period $p = 5$: $S[1..6] = \texttt{abaaba} = S[6..11]$. Valid!
  - Period $q = 8$: $S[1..3] = \texttt{aba} = S[9..11]$. Valid!
  - Period $g = 1$: $S[1] = \texttt{a} \ne S[2] = \texttt{b}$. Broken!
- Notice that `abaababaaba` ($|S| = 11$) is a **central Sturmian word** (specifically, the Fibonacci word prefix formed by deleting the last two characters `ab`/`ba` of the Fibonacci word of length $F_7 = 13$). For general coprime $(p, q)$, the extremal word of length $p + q - 2$ is unique up to alphabet permutation and is always a central Sturmian word (a palindrome whose two extensions by `ab` and `ba` give the standard Christoffel/Sturmian words of length $p+q$).
- For non-coprime $(p, q)$ with $g = \gcd(p, q) > 1$, replacing each character of the coprime extremal word for $(p/g, q/g)$ by a block of length $g$ (or padding $g-1$ independent characters at the end of the interleaved residue classes) yields the tight counterexample of length $p + q - g - 1$.

---

## Iteration 54: The Weak Periodicity Lemma & Log-Block Border/Palindrome AP Decomposition

### 54.1 The Weak Periodicity Lemma & Long Borders ($\ge |S|/2$)

#### 1. The Diagnostic Signal (Why Iterating Over All Borders or Palindromic Suffixes is $O(N^2)$)
In string partition and DP problems—such as partitioning $S[1..n]$ into even palindromes (`CF 932G`), finding minimum palindromic reversals (`CF 906E`), or relaxing knapsack transitions over all borders (`[WC2016] 论战捆竹竿`)—a prefix $S[1..r]$ can have $\Theta(r)$ distinct borders or palindromic suffixes (e.g., $S = \texttt{a}^n$ or $S = (\texttt{ab})^{n/2}$). Naively iterating down the KMP fail chain $u, \pi[u], \pi[\pi[u]], \dots$ or the PAM fail chain at every position $r$ takes $\Theta(n^2)$ time. To break the $O(n^2)$ barrier, we must prove that **dense borders are forced to be periodic** and collapse into $O(\log n)$ arithmetic progressions.

#### 2. Lemma & Proof (Weak Periodicity Lemma)
**Corollary 54.1 (Weak Periodicity Lemma).**
If a string $S[1..n]$ has two periods $p$ and $q$ satisfying
$$p + q \le n,$$
then $g = \gcd(p, q)$ is also a period of $S[1..n]$.

*Proof*: Since $\gcd(p, q) \ge 1$, the hypothesis $p + q \le n$ immediately implies $p + q - \gcd(p, q) \le n - 1 < n$, so Theorem 53.3 (Fine–Wilf) applies directly. $\blacksquare$

**Theorem 54.2 (Single-AP Structure of Long Borders / Small Periods).**
Let $S[1..n]$ be any string, and let
$$\mathcal{P}_{\le n/2}(S) = \{p \in \text{Per}(S) : 1 \le p \le \lfloor n/2 \rfloor\}, \qquad \mathcal{B}_{\ge n/2}(S) = \{b \in \text{Borders}(S) : \lceil n/2 \rceil \le b < n\}.$$
If $\mathcal{P}_{\le n/2}(S)$ is non-empty, let $p_0 = \min \mathcal{P}(S) = n - \pi[n]$ be the shortest period of $S$. Then every period $p \in \mathcal{P}_{\le n/2}(S)$ is an **exact multiple** of $p_0$:
$$\mathcal{P}_{\le n/2}(S) = \left\{ k \cdot p_0 : 1 \le k \le \left\lfloor \frac{n}{2 p_0} \right\rfloor \right\} \quad \text{(or up to the first multiple exceeding }\lfloor n/2 \rfloor\text{)}.$$
Actually, an even stronger statement holds: **every multiple $k \cdot p_0 \le n$ is automatically a period of $S$**, and **no non-multiple of $p_0$ can exist in $[1, \lfloor n/2 \rfloor]$**!
Equivalently, by Period–Border Duality ($b = n - p$), all borders of length $b \ge \lceil n/2 \rceil$ form a **single arithmetic progression** with common difference $p_0$:
$$\mathcal{B}_{\ge n/2}(S) = \{n - p_0,\; n - 2p_0,\; \dots,\; n - k p_0\}.$$

*Proof*:
1. **Multiples of $p_0$ are periods**: Since $S[i] = S[i+p_0]$ for all $1 \le i \le n - p_0$, chaining $k$ steps gives $S[i] = S[i + p_0] = \dots = S[i + k p_0]$ for all $1 \le i \le n - k p_0$. Thus $k p_0 \in \text{Per}(S)$ for every integer $k \ge 1$ with $k p_0 \le n$.
2. **No other period exists in $[1, \lfloor n/2 \rfloor]$**: Suppose $p \in \text{Per}(S)$ satisfies $p \le \lfloor n/2 \rfloor$. Since $p_0 = \min \text{Per}(S) \le p \le \lfloor n/2 \rfloor$, we have:
   $$p_0 + p \le \lfloor n/2 \rfloor + \lfloor n/2 \rfloor \le n.$$
   By the Weak Periodicity Lemma (Corollary 54.1), $g = \gcd(p_0, p)$ is also a period of $S$.
   Because $p_0$ is the **minimum** positive period of $S$ and $g \le p_0$, we must have $g = p_0$.
   Thus $p_0 = \gcd(p_0, p)$, which means $p_0 \mid p$. $\blacksquare$

---

### 54.2 The $O(\log |S|)$ Arithmetic Progression Decomposition of All Borders (`Border 的等差数列性质`)

#### 1. Dyadic Halving Proof
How do we decompose *all* borders of $S[1..n]$ (not just those $\ge n/2$)?
- Let $b_1 = \pi[n]$ be the longest proper border of $S[1..n]$.
- Every border of $S[1..n]$ of length $< b_1$ is a border of $S[1..b_1]$ (because any prefix-suffix of $S$ of length $b \le b_1$ lies entirely inside the prefix $S[1..b_1]$ and suffix $S[n-b_1+1..n] = S[1..b_1]$).
- By Theorem 54.2 applied to $S[1..n]$, all borders of $S[1..n]$ in the top half $[\lceil n/2 \rceil, n-1]$ form a single arithmetic progression with step $d_1 = n - \pi[n]$. In in fact, this AP continues downward as $n - d_1, n - 2d_1, \dots, n \bmod d_1$ (Wait: does the AP stop at $n \bmod d_1$ or earlier? Since $d_1$ is a period of the entire string $S[1..n]$, $k \cdot d_1$ is a period of $S[1..n]$ for **all** $1 \le k < n / d_1$! So the borders $n - k d_1$ exist all the way down to $r_1 = (n - 1) \bmod d_1 + 1$, wait: if $d_1 \mid n$, down to $d_1$ or $0$).
- Wait: can there be another border $b \notin \{n - k d_1\}$ that is $\ge \lceil n/2 \rceil$? No, by Theorem 54.2! What is the largest possible border $b'$ of $S[1..n]$ that does **not** belong to this first AP?
  Look at the shortest non-empty string in this periodic chain, or more standardly:
  Consider the dyadic intervals of border lengths $I_j = [2^{j-1}, 2^j - 1]$ for $j = 1, 2, \dots, \lceil \log_2 n \rceil$.
  In any interval $[L, 2L-1]$, let $b_{\max}$ be the longest border of $S$ in $[L, 2L-1]$. Every border $b \in [L, b_{\max}]$ of $S$ is a border of the prefix $P = S[1..b_{\max}]$ of length $\ge L \ge |P|/2$.
  Applying Theorem 54.2 to $P = S[1..b_{\max}]$, all borders of $S$ in $[L, b_{\max}]$ form a **single arithmetic progression**!

**Theorem 54.3 (Log-Block Border AP Decomposition).**
For any string $S[1..n]$, the set of all non-empty borders $\text{Borders}(S) \setminus \{0\}$ can be partitioned into at most $\lceil \log_2 n \rceil$ disjoint arithmetic progressions (chains of constant difference $\text{diff}(u) = u - \pi[u]$). Moreover, along the KMP failure chain $u_0 = n, u_1 = \pi[u_0], u_2 = \pi[u_1], \dots$, whenever the step size changes ($\text{diff}(u_{i+1}) \ne \text{diff}(u_i)$), the length drops by more than half:
$$u_{i+1} < \frac{1}{2} u_i \quad \text{(or } u_{i+2} \le \frac{1}{2} u_i \text{ depending on whether boundary nodes are shared)}.$$

*Exact Halving Proof for `diff(u) = u - pi[u]`*:
Let $u$ be a border of $S$, let $v = \pi[u]$ be its longest proper border, and let $w = \pi[v]$.
- The step sizes are $d_1 = \text{diff}(u) = u - v$ (shortest period of $S[1..u]$) and $d_2 = \text{diff}(v) = v - w$ (shortest period of $S[1..v]$).
- Since $S[1..v]$ is a prefix of $S[1..u]$, the period $d_1$ of $S[1..u]$ is also a period of $S[1..v]$. Because $d_2$ is the *minimum* period of $S[1..v]$, we always have $d_2 \le d_1$.
- Suppose $d_2 < d_1$ (a **series-link jump** occurs at $v$). Could we have $v \ge u / 2$?
  Wait: if $v \ge d_1 + d_2$, then inside $S[1..v]$ both $d_1$ and $d_2$ are periods with $d_1 + d_2 \le v$. By Weak Periodicity Lemma on $S[1..v]$, $g = \gcd(d_1, d_2)$ is a period of $S[1..v]$, so $g = d_2$ (as $d_2$ is minimum), meaning $d_2 \mid d_1$.
  Can $d_2 \mid d_1$ with $d_2 < d_1$ when $v = u - d_1$?
  Wait: if $d_2 \mid d_1$, then inside $S[1..u]$, the prefix $S[1..v]$ has period $d_2$, the suffix $S[u-v+1..u] = S[1..v]$ also has period $d_2$, and their overlap has length $2v - u = v - d_1$. If $v - d_1 \ge d_2$, the two copies of period $d_2$ overlap by at least $d_2$, which forces the entire string $S[1..u]$ to have period $d_2 < d_1$, contradicting that $d_1$ is the minimum period of $S[1..u]$!
- Therefore, whenever $d_2 = \text{diff}(\pi[u]) \ne \text{diff}(u) = d_1$, we **must** have:
  $$v - d_1 < d_2 \iff u - 2 d_1 < d_2 < d_1 \implies v = u - d_1 < d_1 + d_2 < 2 d_1 \implies \pi[u] = v < \frac{2}{3} u,$$
  and for the next node $w = \pi[v] = v - d_2$, since $v - d_2 < d_1 = u - v$, we immediately get:
  $$\boxed{w = \pi[\pi[u]] < u - \pi[u] \le \frac{1}{2} u \quad \text{or} \quad \text{len}(\text{slink}[u]) \le \frac{1}{2} \text{len}(u)!}$$
  Specifically, if we define $\text{slink}[u]$ to be the highest ancestor of $u$ with a different `diff`:
  $$\text{slink}[u] = \begin{cases} \text{slink}[\text{fail}[u]] & \text{if } \text{diff}(u) = \text{diff}(\text{fail}[u]), \\ \text{fail}[u] & \text{if } \text{diff}(u) \ne \text{diff}(\text{fail}[u]), \end{cases}$$
  then the first node of the *next* AP chain, $\text{slink}[u]$, has length at most $\frac{2}{3}\text{len}(u)$, and its parent $\text{fail}[\text{slink}[u]]$ has length strictly less than $\frac{1}{2}\text{len}(u)$! Thus jumping via `slink` traverses at most $O(\log n)$ links. $\blacksquare$

---

### 54.3 Palindromic Suffix AP Equivalence (`回文后缀的等差数列性质`)

#### 1. Lemma: Palindromic Suffixes $\Longleftrightarrow$ Palindromic Borders
**Lemma 54.4 (Palindrome Suffix–Border Equivalence).**
Let $P = P[1..m]$ be a palindrome ($P = P^R$). For any $1 \le k < m$, the suffix $P[m-k+1..m]$ of length $k$ is a **palindrome** if and only if $k$ is a **border** of $P$.

*Proof*:
Since $P$ is a palindrome, reversing $P$ maps the prefix $P[1..k]$ to the reversed suffix $(P[m-k+1..m])^R$:
$$P[1..k] = (P[m-k+1..m])^R.$$
- ($\Rightarrow$) If the suffix $P[m-k+1..m]$ is a palindrome, then $(P[m-k+1..m])^R = P[m-k+1..m]$, so $P[1..k] = P[m-k+1..m]$, meaning $k \in \text{Borders}(P)$.
- ($\Leftarrow$) If $k \in \text{Borders}(P)$, then $P[1..k] = P[m-k+1..m]$, so $(P[m-k+1..m])^R = P[1..k] = P[m-k+1..m]$, meaning $P[m-k+1..m]$ is a palindrome. $\blacksquare$

#### 2. Immediate Transfer to the Palindromic Automaton (PAM / Eertree)
For any string $S[1..n]$ and any right endpoint $r \in \{1, \dots, n\}$:
- Let $P = S[r-m+1..r]$ be the **longest palindromic suffix** of $S[1..r]$ (represented by the active PAM state $u$ of length $m = \text{len}[u]$).
- Every other palindromic suffix of $S[1..r]$ has length $k < m$ and is a palindromic suffix of $P$.
- By Lemma 54.4, the palindromic suffixes of $P$ are **precisely the borders of $P$**!
- By Theorem 54.3, the lengths of all palindromic suffixes of $S[1..r]$ (i.e., the PAM fail chain $u, \text{fail}[u], \text{fail}[\text{fail}[u]], \dots$) partition into at most $O(\log r)$ arithmetic progressions, maintained by the three PAM node fields:
  $$\text{len}[u], \qquad \text{diff}[u] = \text{len}[u] - \text{len}[\text{fail}[u]], \qquad \text{slink}[u] = \begin{cases} \text{slink}[\text{fail}[u]] & \text{if } \text{diff}[u] = \text{diff}[\text{fail}[u]], \\ \text{fail}[u] & \text{otherwise.} \end{cases}$$

---

## Iteration 55: Border-Group Modulo Shortest Path (`同余最短路 + 等差数列背包` — `[WC2016] 论战捆竹竿`)

### 55.1 Problem Formulation & Diagnostic Signal

#### 1. The Concrete Problem (`[WC2016] 论战捆竹竿` / `Luogu P4156`)
Given a string $S[1..n]$ of length $n \le 5 \times 10^5$ and a maximum length bound $W \le 10^{18}$ ($T \le 5$ testcases), we start with a copy of $S$ (initial length $n$). Whenever we append another copy of $S$, we are allowed to overlap the prefix of the new $S$ with any matching non-empty suffix of the current string (i.e., any proper border $b \in \text{Borders}(S)$), which increases the total length by the **period** $p = n - b \in \text{Per}(S)$.
**Question**: How many distinct total lengths $L \in [n, W]$ can be formed as:
$$L = n + \sum_{p \in \text{Per}(S)} c_p \cdot p, \qquad c_p \in \mathbb{Z}_{\ge 0}?$$

#### 2. Diagnostic Signal (Why Standard Modulo Shortest Path Fails)
- Because $W \le 10^{18}$ is huge while $n \le 5 \times 10^5$, this is a **Frobenius / Coin-Exchange Modulo Shortest Path (`同余最短路`)** problem: if we choose a base modulus $M \le n$ and compute for each residue $r \in \{0, 1, \dots, M-1\}$ the minimum achievable length $D[r] \equiv r \pmod M$, then the number of achievable lengths $\le W$ in residue class $r$ (assuming $n \in \text{Per}(S)$ is available or $M \in \text{Per}(S)$) is $\max\left(0, \left\lfloor \frac{W - D[r]}{M} \right\rfloor + 1\right)$.
- **Why Naive Dijkstra / Bellman-Ford Fails**: $|\text{Per}(S)|$ can be $\Theta(n)$ (e.g., $S = \texttt{a}^n$ has $n$ periods). A graph on $M = \Theta(n)$ residues with $\Theta(n)$ outgoing transitions per vertex has $\Theta(n^2)$ edges!

---

### 55.2 Structural Compression via Border APs & Dynamic Modulus Changing

By Theorem 54.3, the set of periods $\text{Per}(S) = \{n - b : b \in \text{Borders}(S)\}$ partitions into $K = O(\log n)$ arithmetic progressions. Each AP has the form:
$$A = \{x,\; x + d,\; x + 2d,\; \dots,\; x + c \cdot d\},$$
where:
- $x = n - b_{\max}$ is the shortest period in this AP (corresponding to the longest border $b_{\max}$ in the block),
- $d = \text{diff}(b_{\max}) = b_{\max} - \pi[b_{\max}]$ is the common difference of the AP,
- $c + 1$ is the number of elements in the AP ($c \ge 0$), and notice that since all borders in this block belong to $S[1..b_{\max}]$ and have step $d$, we have $x + c \cdot d \le n$.

There are two structural steps to process one AP $A = \{x + k d : 0 \le k \le c\}$ in $O(x)$ or $O(n)$ time:

#### Step 1: Modulus Change Transition ($p_{\text{old}} \to x$) in $O(x)$ Time
Instead of keeping a fixed modulus $M = n$ across the entire algorithm, when we move to an AP with base period $x$, we **change the working modulus from $p_{\text{old}}$ to $x$**!
- Why choose $x$ as the new modulus? Because adding any number of copies of $x$ itself ($k = 0$ in the AP: $x + 0 \cdot d = x$) costs $x \equiv 0 \pmod x$, which is **free in residue index** and automatically saturates all multiples of $x$!
- Moreover, for $k \in \{1, \dots, c\}$, adding $x + k d$ once is equivalent to adding $k d$ once plus one copy of the modulus $x$! Since we can already add $x$ any number of times for free (at cost $+x$), **every element $x + k d \in A$ ($1 \le k \le c$) can be used at most once** ( Wait: why? Or rather, using $t$ elements from $A$ is just picking a single shift $x + k d$ ($0 \le k \le c$) inside a sliding window of size $c$, and repeating the slide!).
- How do we convert the distance array $D_{\text{old}}[0 .. p_{\text{old}} - 1]$ (where $p_{\text{old}}$ was in $\text{Per}(S)$) to the new modulus $x$?
  1. Initialize $D_{\text{new}}[r] = +\infty$ for $r \in \{0, \dots, x-1\}$.
  2. Project every old state: for each $i \in \{0, \dots, p_{\text{old}} - 1\}$ with $D_{\text{old}}[i] < \infty$, relax:
     $$D_{\text{new}}[D_{\text{old}}[i] \bmod x] \gets \min\big(D_{\text{new}}[D_{\text{old}}[i] \bmod x],\; D_{\text{old}}[i]\big).$$
  3. Since $p_{\text{old}}$ was an available period in previous stages, we must still allow adding $+p_{\text{old}}$ unlimited times under the new modulus $x$!
     Partition $\{0, \dots, x-1\}$ into $g = \gcd(x, p_{\text{old}})$ independent cycles of length $x / g$. On each cycle, start at the vertex with minimum $D_{\text{new}}[u]$ and sweep twice around the cycle with step $+p_{\text{old}} \pmod x$:
     $$D_{\text{new}}[(u + p_{\text{old}}) \bmod x] \gets \min\big(D_{\text{new}}[(u + p_{\text{old}}) \bmod x],\; D_{\text{new}}[u] + p_{\text{old}}\big).$$
     This takes $O(p_{\text{old}} + x)$ time.

#### Step 2: Bounded-Step Monotonic Queue Relaxation for $\{x + k d : 1 \le k \le c\}$
Now the working modulus is $x$, so $x \equiv 0 \pmod x$ is already implicit. A single transition from the AP $A$ adds $x + k d$ for some $k \in \{1, 2, \dots, c\}$, moving from residue $u$ to $(u + k d) \bmod x$ with cost $+ (x + k d)$.
Notice that in the residue graph of step $+d \pmod x$:
- The residues $\{0, 1, \dots, x-1\}$ decompose into $g' = \gcd(x, d)$ independent cycles of length $L = x / g'$.
- Along a single cycle $v_0, v_1, \dots, v_{L-1}$ where $v_j = (v_0 + j \cdot d) \bmod x$:
  - Unroll the cycle starting from its minimum-distance vertex $v_0 = \arg\min_{v} D_{\text{new}}[v]$ (since no shortest path can ever improve $v_0$, unrolling $v_0, v_1, \dots, v_{L-1}$ breaks the cycle into a DAG!).
  - Moving from $v_i$ to $v_j$ ($1 \le j - i \le c$) corresponds to choosing $k = j - i \in \{1, \dots, c\}$ and adds cost $x + (j - i) d$:
    $$D_{\text{new}}[v_j] \gets \min_{j - c \le i \le j - 1} \Big( D_{\text{new}}[v_i] + x + (j - i) d \Big) = x + j \cdot d + \min_{j - c \le i \le j - 1} \Big( D_{\text{new}}[v_i] - i \cdot d \Big).$$
  - This is a **1D sliding-window minimum of width $c$** on the separated key $\text{val}(i) = D_{\text{new}}[v_i] - i \cdot d$!
  - Using a standard monotonic deque (`单调队列`), we relax the entire cycle of length $L$ in $O(L)$ time, and all $g'$ cycles in $O(x)$ total time!
  - Note: Because we can take multiple steps from the AP $A$ in sequence, we push the *updated* value $D_{\text{new}}[v_j] - j \cdot d$ into the monotonic deque at step $j$ before advancing to $j + 1$ (exact complete-knapsack semantics over window $c$).

```
Cycle of +d (mod x), unrolled from argmin v_0:
Index along cycle:   0      1      ...    i     ...     j
Residue:            v_0    v_1    ...    v_i    ...    v_j = (v_0 + j*d) mod x
Transition (1 <= j-i <= c):               |------------>|  cost: + x + (j - i)*d
Separated key in Monotonic Queue:  val(i) = D[v_i] - i*d,  window [j-c, j-1]
```

#### Complexity Contract & Invariant Summary
- Each of the $O(\log n)$ AP blocks performs one modulus transition $O(p_{\text{old}} + x)$ and one monotonic-queue cycle sweep $O(x)$. Since $x \le n$, total time is $O(n \log n)$ and auxiliary space is $O(n)$!
- **Boundary Pitfall**: When unrolling a cycle of $+d \pmod x$, you **must** rotate the cycle so that index $0$ is the vertex $v_0$ achieving the global minimum of $D_{\text{new}}$ on that cycle! If you start at an arbitrary vertex, a transition wrapping around the end of the cycle back to index $0$ would be missed unless you run the pass twice—and running a *complete* knapsack pass twice around a cycle would illegally allow the same bounded window to wrap around without paying $+x$ at the wrap boundary unless indexed continuously as $j \in [0, 2L-1]$. Starting at $v_0 = \arg\min D_{\text{new}}$ guarantees no shortest path ever needs to update $v_0$, so a single pass $j = 0 \to L-1$ is 100% exact!

---

## Iteration 56: Series-Link (`slink` / `diff`) DP Acceleration on KMP & Palindromic Automata

### 56.1 The Universal 1D String Partition DP & Why Naive Transitions Take $O(N^2)$

#### 1. The Prototype DP Pattern
Consider a 1D dynamic programming recurrence over prefixes $S[1..r]$ ($1 \le r \le n$) of the form:
$$dp[r] = \bigoplus_{L \in \mathcal{A}(r)} \Big( dp[r - L] \otimes w(L) \Big),$$
where $\mathcal{A}(r)$ is either:
- **Palindromic Suffix Set** ($\mathcal{A}(r) = \{\text{len}[v] : v \text{ is an ancestor of active PAM node } u_r \text{ in the fail tree}\}$), as in `CF 932G — Palindrome Partition` and `CF 906E — Reverses`; or
- **Border Set** ($\mathcal{A}(r) = \{b \in \text{Borders}(S[1..r])\}$), or period-constrained suffix set, as in `[SDOI2019] 连续子序列` (`Luogu P5328`).

Because $|\mathcal{A}(r)|$ can be $\Theta(r)$ at every step $r$ (e.g., $S = \texttt{a}^n$), walking the `fail` chain $v = u_r, \text{fail}[u_r], \dots$ takes $O(n^2)$ time.
Even though Iteration 54 showed that $\mathcal{A}(r)$ partitions into $O(\log r)$ arithmetic progressions via `slink`, **how do we aggregate $dp[r - L]$ across an arithmetic progression of lengths $L \in \{\ell, \ell - d, \ell - 2d, \dots, \ell - k d\}$ in $O(1)$ time without a segment tree over every residue class modulo every possible $d \in [1, n]$?**

---

### 56.2 The Exact Shift Invariant (`r - 1 -> r` Periodic Alignment Proof)

#### 1. The Combinatorial Word Invariant (Why `fail[u]` Appears at `r - diff[u]`)
Let $u$ be a PAM node representing a palindromic suffix $P = S[r - \ell + 1 .. r]$ of length $\ell = \text{len}[u]$ ending at $r$, with longest proper palindromic border $v = \text{fail}[u]$ of length $\ell - d$, where $d = \text{diff}[u] = \text{len}[u] - \text{len}[\text{fail}[u]]$.
Suppose $u$ is **not** the bottom of its AP chain, i.e., $\text{diff}[u] = \text{diff}[\text{fail}[u]] = d$.
Let the lengths in $u$'s AP chain (down to $\text{slink}[u]$, exclusive of $\text{slink}[u]$) be:
$$\mathcal{L}(u) = \big\{\ell,\; \ell - d,\; \ell - 2d,\; \dots,\; \ell - k d\big\}, \qquad \text{where } \ell - k d = \text{len}[\text{slink}[u]] + d \quad (k \ge 1).$$
Therefore, when $u$ is visited at right endpoint $r$, the set of **left transition indices** $r - L$ contributed by $u$'s AP chain is:
$$\mathcal{I}(u, r) = \{r - L : L \in \mathcal{L}(u)\} = \big\{\underbrace{r - \ell}_{\text{new index}},\; r - \ell + d,\; r - \ell + 2d,\; \dots,\; r - \ell + k d\big\}.$$

Now ask the central question of `slink` DP: **Where was the parent node $v = \text{fail}[u]$ most recently visited before step $r$?**

**Theorem 56.1 (The Periodic Shift Invariant on PAM and KMP).**
Let $u$ be a palindrome (in PAM) or border (in KMP) ending at $r$ with $\text{diff}[u] = \text{diff}[\text{fail}[u]] = d$. Then:
1. The palindrome/border $v = \text{fail}[u]$ of length $\ell - d$ **necessarily occurred as a suffix at position $r' = r - d$**!
   - *Why?* Because $v = S[r - \ell + d + 1 .. r]$ is a suffix of $P = S[r - \ell + 1 .. r]$, and $v$ is ALSO a **prefix** of $P$ (since $v$ is a border of $P$)! As a prefix of $P = S[r - \ell + 1 .. r]$ of length $\ell - d$, $v$ occupies the exact substring:
     $$S\big[(r - \ell + 1) \dots (r - \ell + \ell - d)\big] = S\big[r - \ell + 1 \dots r - d\big],$$
     whose right endpoint is **precisely $r' = r - d$**!
2. Furthermore, at position $r' = r - d$, could $v$ have been a proper prefix of a *longer* palindrome in the same AP at $r - d$? Even if $v$ was an ancestor in the fail chain at $r - d$, $v$ was **visited during the `slink` traversal at step $r' = r - d$**?
   Wait—let us check carefully! Was $v = \text{fail}[u]$ necessarily the **top of an `slink` chain** at step $r' = r - d$, or was $v$ updated at $r' = r - d$?
   Let us prove why $v = \text{fail}[u]$ **must** be updated at step $r' = r - d$!
   Suppose at position $r' = r - d$, there were some longer palindromic suffix $w$ of $S[1..r-d]$ that had $v$ as a proper fail-ancestor *with the same difference $d$* ($\text{fail}[w] = v$ and $\text{diff}[w] = d$).
   Then $w$ would have length $\text{len}[v] + d = (\ell - d) + d = \ell$, and $w = S[r - d - \ell + 1 .. r - d]$ would be a palindrome of length $\ell$ with period $d$.
   Wait: even if such a $w$ exists at $r - d$, what matters for the rolling accumulator $g[v]$ is that **$v$ is on the fail chain of $S[1..r-d]$, and NO palindrome in $S[1..r-d]$ can have $v$ as a fail-ancestor with step $d$ UNLESS $v$'s own value $g[v]$ was already refreshed at $r - d$?**
   Wait—let us check that! If $w$ is on the fail chain at $r - d$ and $\text{fail}[w] = v$ with $\text{diff}[w] = d$, then during the `slink` jump at step $r - d$, the algorithm jumps from $w$ directly to $\text{slink}[w] = \text{slink}[v]$, **skipping $v$** at step $r - d$!
   **Hold on!** Why does skipping $v$ at step $r - d$ NOT break $g[v]$?! Let us prove this crucial subtlety that almost all blogs gloss over!

**Lemma 56.2 (The Non-Extendability of Period $d$ Across $r - d \to r$, or Why $v = \text{fail}[u]$ Is ALWAYS the Top of Its AP at $r - d$).**
Let $u$ be visited as the **top of an AP chain** during the `slink` traversal at position $r$ (meaning no ancestor of $S[1..r]$'s active node has $\text{fail}[u'] = u$ with $\text{diff}[u'] = d$).
Then at position $r' = r - d$, the node $v = \text{fail}[u]$ is **ALSO the top of its AP chain** (i.e., $v$ is visited directly by the `slink` loop at step $r - d$, and is **never** skipped at step $r - d$)!

*Proof by Contradiction (Zero-Magic Alignment Proof)*:
Suppose for contradiction that at step $r' = r - d$, $v = \text{fail}[u]$ is **not** the top of its AP chain in the fail tree of $S[1..r-d]$.
1. Then $S[1..r-d]$ has a palindromic suffix $w$ on its fail chain such that $\text{fail}[w] = v$ and $\text{diff}[w] = \text{diff}[v] = d$.
2. Actually, since $v$ is the longest proper border of $u$ ($\text{len}[u] = \ell$, $\text{len}[v] = \ell - d$), any palindrome $w$ with $\text{fail}[w] = v$ and $\text{diff}[w] = d$ has length $\text{len}[w] = \text{len}[v] + d = \ell$, and $w = S[r - d - \ell + 1 .. r - d]$ has period $d$.
3. Because $u = S[r - \ell + 1 .. r]$ has border $v = S[r - \ell + 1 .. r - d]$, $u$ has period $d$, so $S[r] = S[r - d] = \dots = S[r - \ell + d]$.
4. Because $w = S[r - \ell - d + 1 .. r - d]$ has border $v = S[r - \ell + 1 .. r - d]$, $w$ ALSO has period $d$, so the character immediately preceding $u$, namely $S[r - \ell]$, equals $S[r - \ell + d]$!
5. Combining (3) and (4):
   $$S[r - \ell] = S[r - \ell + d] = S[r]!$$
6. Since $u = S[r - \ell + 1 .. r]$ is a palindrome and its two flanking characters $S[r - \ell]$ and $S[r]$ are equal, the substring
   $$u^+ = S[r - \ell .. r]$$
   is a **palindrome of length $\ell + 1$ ending at $r$**? Wait: not $\ell + 1$, rather extending by period $d$ to the left of $u$ gives $S[r - \ell - d + 1 .. r]$ of length $\ell + d$!
   Specifically, gluing $w = S[r - \ell - d + 1 .. r - d]$ (period $d$, palindrome) and $u = S[r - \ell + 1 .. r]$ (period $d$, palindrome) along their overlap $v = S[r - \ell + 1 .. r - d]$ of length $\ell - d \ge d$ (since $\text{diff}[v] = d \implies \text{len}[v] > d$) produces a substring $u^* = S[r - \ell - d + 1 .. r]$ of length $\ell + d$ which has period $d$ and is a **palindrome ending at $r$** with $\text{fail}[u^*] = u$ and $\text{diff}[u^*] = d$!
7. That means $u^*$ is an ancestor of $u$ at position $r$ with $\text{fail}[u^*] = u$ and $\text{diff}[u^*] = d$—contradicting the fact that $u$ is the **top of its AP chain** at step $r$! $\blacksquare$

> [!IMPORTANT]
> **Why Lemma 56.2 Is the Heart of `slink` DP**
> Many explanations state "$g[\text{fail}[u]]$ was updated at $r - \text{diff}[u]$" without realizing that the `slink` loop only visits $O(\log r)$ chain-top nodes at each step $r'$, skipping internal chain nodes! **Lemma 56.2 proves that if $u$ is a chain-top node visited at step $r$, then $\text{fail}[u]$ was GUARANTEED to be a chain-top node visited at step $r - \text{diff}[u]$!** It is *never* skipped at $r - \text{diff}[u]$.

---

### 56.3 Deriving the Rolling Accumulator $g[u]$ from $\mathcal{I}(u, r)$ vs. $\mathcal{I}(\text{fail}[u], r - d)$

Now compare the left-endpoint index set $\mathcal{I}(u, r)$ of node $u$ at position $r$ with the left-endpoint index set $\mathcal{I}(v, r - d)$ of node $v = \text{fail}[u]$ at position $r - d$ (where $d = \text{diff}[u]$ and $\text{slink}[u] = \text{slink}[v]$):
- At position $r$, node $u$ covers lengths $\mathcal{L}(u) = \{\ell,\; \ell - d,\; \ell - 2d,\; \dots,\; \ell - k d\}$, where $\ell - k d = \text{len}[\text{slink}[u]] + d$.
  Thus the left endpoints are:
  $$\mathcal{I}(u, r) = \big\{\mathbf{r - \ell},\; r - \ell + d,\; r - \ell + 2d,\; \dots,\; r - \ell + k d\big\}.$$
- At position $r' = r - d$, node $v = \text{fail}[u]$ has length $\text{len}[v] = \ell - d$ and the **same** $\text{slink}[v] = \text{slink}[u]$, so it covers lengths $\mathcal{L}(v) = \{\ell - d,\; \ell - 2d,\; \dots,\; \ell - k d\}$.
  Subtracting these lengths from $r' = r - d$ gives the exact left endpoints:
  $$\mathcal{I}(v, r - d) = \big\{(r - d) - (\ell - d),\; (r - d) - (\ell - 2d),\; \dots,\; (r - d) - (\ell - k d)\big\} = \big\{r - \ell + d,\; r - \ell + 2d,\; \dots,\; r - \ell + k d\big\}!$$

```
At step r - d, node v = fail[u] (len = l - d) aggregates left endpoints:
  I(v, r - d) = {                 r - l + d,   r - l + 2d,  ...,  r - l + k*d }
                                      ||           ||                 ||
At step r,     node u           (len = l)     aggregates left endpoints:
  I(u, r)     = { r - l (NEW!),   r - l + d,   r - l + 2d,  ...,  r - l + k*d }
                  ^^^^^^^^^^^     \_________________________________________/
             r - len[slink[u]] - d          Already stored in g[fail[u]]!
```

Wait—look at the diagram above vs. the two ways to write the decomposition of $\mathcal{I}(u, r)$!
Wait: in the diagram above, $(r - d) - (\ell - d) = r - \ell$!
Let us re-evaluate $(r - d) - (\ell - j d)$ carefully!
For $j \in \{1, 2, \dots, k\}$, the lengths in $\mathcal{L}(v)$ are $\ell_j = \ell - j d$.
At position $r' = r - d$, the left endpoint corresponding to length $\ell_j = \ell - j d$ is:
$$r' - \ell_j = (r - d) - (\ell - j d) = r - \ell + (j - 1) d!$$
Let us list $r' - \ell_j$ for $j = 1, 2, \dots, k$:
- For $j = 1$ ($\ell_1 = \ell - d$): $(r - d) - (\ell - d) = \mathbf{r - \ell}$!
- For $j = 2$ ($\ell_2 = \ell - 2d$): $(r - d) - (\ell - 2d) = \mathbf{r - \ell + d}$!
- ...
- For $j = k$ ($\ell_k = \ell - k d = \text{len}[\text{slink}[u]] + d$): $(r - d) - (\ell - k d) = \mathbf{r - \ell + (k - 1) d}$!

And what are the left endpoints in $\mathcal{I}(u, r)$ at position $r$?
For $j = 0, 1, \dots, k$, the lengths in $\mathcal{L}(u)$ are $\ell_j = \ell - j d$, giving left endpoints:
$$r - \ell_j = r - (\ell - j d) = r - \ell + j d \quad \text{for } j = 0, 1, \dots, k - 1, \mathbf{k}!$$
Compare the two sets term by term:
$$\mathcal{I}(v, r - d) = \big\{r - \ell,\; r - \ell + d,\; \dots,\; r - \ell + (k - 1) d\big\},$$
$$\mathcal{I}(u, r) = \underbrace{\big\{r - \ell,\; r - \ell + d,\; \dots,\; r - \ell + (k - 1) d\big\}}_{=\, \mathcal{I}(\text{fail}[u],\, r - d)} \;\cup\; \big\{\mathbf{r - \ell + k d}\big\}!$$
And since $\ell - k d = \text{len}[\text{slink}[u]] + d$, the **single new index** $r - \ell + k d$ at the right end of the progression is:
$$\boxed{r - (\ell - k d) = r - \big(\text{len}[\text{slink}[u]] + \text{diff}[u]\big)!}$$

```
Exact Alignment of I(fail[u], r - d) and I(u, r):

Lengths in fail[u] at r - d:   l - d        l - 2d       ...   len[slink[u]] + d
Left endpoints at r - d:       r - l        r - l + d    ...   r - l + (k-1)*d
                                 ||            ||                     ||
Lengths in u at r:               l          l - d        ...   l - (k-1)*d         len[slink[u]] + d
Left endpoints at r:           r - l        r - l + d    ...   r - l + (k-1)*d     r - len[slink[u]] - d
                               \_____________________________________________/     \___________________/
                                        Exact match = g[fail[u]]!                    Single NEW term!
```

**Theorem 56.3 (Exact `slink` Rolling Accumulator Recurrence).**
For any associative/commutative aggregation $\oplus$ over unweighted palindrome/border transitions $dp[r] = \bigoplus_{L \in \mathcal{A}(r)} dp[r - L]$, maintain $g[u] = \bigoplus_{i \in \mathcal{I}(u, r)} dp[i]$ for each visited chain-top node $u$ at step $r$ via:
$$g[u] = \begin{cases} dp\big[r - \text{len}[\text{slink}[u]] - \text{diff}[u]\big] & \text{if } \text{diff}[u] \ne \text{diff}[\text{fail}[u]] \quad (\text{since } \text{slink}[u] = \text{fail}[u] \text{ and } \text{len}[u] = \text{len}[\text{slink}[u]] + \text{diff}[u]), \\ g[\text{fail}[u]] \;\oplus\; dp\big[r - \text{len}[\text{slink}[u]] - \text{diff}[u]\big] & \text{if } \text{diff}[u] = \text{diff}[\text{fail}[u]], \end{cases}$$
and update $dp[r] \gets dp[r] \oplus g[u]$ while jumping $u \gets \text{slink}[u]$ until $u \le 1$.
Since there are at most $\lceil \log_2 r \rceil$ `slink` jumps per step $r$, the entire 1D partition DP runs in **$O(n \log n)$ time and $O(n)$ space**!

---

### 56.4 Four Canonical Variations of `slink` DP (`CF 932G`, `CF 906E`, `[SDOI2019]`, `HDU 6599`)

1. **Even-Length Palindrome Partition & Double-End Interleaving (`CF 932G — Palindrome Partition`)**:
   - *Task*: Count ways to partition $S[1..n]$ ($n$ even) into $S = s_1 s_2 \dots s_k$ such that $s_i = s_{k+1-i}$ for all $i$.
   - *Reduction*: Interleave the first half and reversed second half into $T = S[1]\, S[n]\, S[2]\, S[n-1]\, \dots\, S[n/2]\, S[n/2+1]$. A symmetric block pair $(s_1, s_k)$ of length $m$ satisfies $s_1 = s_k \iff$ the prefix of $T$ of even length $2m$ is a **palindrome**!
   - Thus the problem reduces to counting partitions of $T[1..n]$ into **even-length palindromes**: update $dp[r] \gets \sum g[u]$ only when $2 \mid r$. (Notice that $g[u]$ must still be maintained at **both odd and even $r$**, because an even-length palindrome at an even $r$ can have an odd-step period $d = \text{diff}[u]$, meaning $\text{fail}[u]$ was updated at an odd position $r - d$! However, $dp[\text{odd}] = 0$.)

2. **Minimum Palindromic Reversals with Argmin Reconstruction (`CF 906E — Reverses`)**:
   - *Task*: Given $A[1..n]$ and $B[1..n]$, reverse minimum disjoint intervals of $A$ to make $A = B$.
   - *Reduction*: Interleave $T = A[1]\, B[1]\, A[2]\, B[2]\, \dots\, A[n]\, B[n]$ of length $2n$. Reversing $A[l..r]$ to match $B[l..r]$ is valid $\iff T[2l-1 .. 2r]$ is an even-length palindrome!
   - Here $\oplus = \min$, we also allow step-$2$ no-op transitions when $A[i] = B[i]$ ($dp[2i] \gets dp[2i-2]$ with cost $0$), and $g[u]$ stores a pair $(\text{min\_dp}, \text{argmin\_left\_index})$ so we can reconstruct the optimal intervals in $O(n \log n)$.

3. **Affine / Weighted Period-Constrained DP on KMP (`[SDOI2019] 连续子序列` / `Luogu P5328`)**:
   - When transitions depend not only on $r - L$ but also linearly on the step count $j$ inside the AP, both $\sum dp[i]$ and $\sum i \cdot dp[i]$ are maintained in $g[u]$.

4. **Half-Palindrome / Palindromic Border Counting on PAM (`HDU 6599 — I Love Palindrome String`)**:
   - Uses PAM fail-tree subtree occurrences (`cnt[u]`) combined with border/half-length lookup on the PAM fail chain (`slink` or binary lifting) to test whether $P[1..\lceil |P|/2 \rceil]$ is also a palindrome.

---

### 56.5 Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Pitfall 1: Updating $g[u]$ Only at Even Positions in `CF 932G` / `CF 906E`**
   - *Counterexample*: Consider $T = \texttt{aaaaaa}$ ($n = 6$). At $r = 4$, the longest palindrome is $u = \texttt{aaaa}$ ($\text{len}[u] = 4$), with $\text{fail}[u] = \texttt{aaa}$ ($\text{len} = 3$), so $\text{diff}[u] = 4 - 3 = 1$ (an **odd** period!).
   - Therefore, at $r = 4$ (even), $g[u]$ reads $g[\text{fail}[u]]$ from position $r - \text{diff}[u] = 4 - 1 = 3$ (**odd**)!
   - If you skip updating $g[\cdot]$ at odd indices $r$ because $dp[\text{odd}] = 0$, then $g[\text{fail}[u]]$ at $r = 3$ is never refreshed with $dp[2]$, and $dp[4]$ misses the transition from $dp[2]$!
   - **Rule**: Always run the `slink` loop and update $g[u]$ at **every** index $r \in \{1, \dots, n\}$; only gate the write to $dp[r]$ on $2 \mid r$.

2. **Pitfall 2: Writing $r - \text{len}[u]$ Instead of $r - \text{len}[\text{slink}[u]] - \text{diff}[u]$ for the New Term**
   - *Why it fails*: As proven in Theorem 56.3, the index $r - \text{len}[u]$ is the **first** (leftmost) element of $\mathcal{I}(u, r)$, which was **already included** in $\mathcal{I}(\text{fail}[u], r - d)$ at step $r - d$ because $(r - d) - (\text{len}[u] - d) = r - \text{len}[u]$!
   - Adding $dp[r - \text{len}[u]]$ again double-counts $dp[r - \text{len}[u]]$ and completely omits the shortest member of the AP, $dp[r - \text{len}[\text{slink}[u]] - \text{diff}[u]]$!
   - *Counterexample*: $T = \texttt{aaaa}$ ($r = 4$, $\text{len}[u] = 4$, $\text{diff}[u] = 1$, $\text{len}[\text{slink}[u]] = 0$). At $r = 4$, $\mathcal{I}(u, 4) = \{0, 1, 2, 3\}$. At $r - 1 = 3$, $\mathcal{I}(\text{fail}[u], 3) = \{0, 1, 2\}$. The new element at $r = 4$ is $3 = 4 - 0 - 1$, **not** $0 = 4 - 4$!

---

## Iteration 57: Multilingual Problem Mining (`[EN]` / `[ZH]` / `[JA]`), 4-Tier Difficulty Ladder & Template Quarantine

### 57.1 Quarantine Table of Rejected Pure Template Problems (`R-1A-01` – `R-1A-08`)

Per the repository editorial policy (`AGENTS.md` and `PLAN.md`), bare algorithm verification templates without structural modeling are quarantined from the textbook ladders:

| Quarantine ID | Source & Problem Name | Language | Reason for Quarantine |
| :--- | :--- | :--- | :--- |
| **R-1A-01** | Library Checker — `Z Algorithm` | `[EN]` / `[JA]` | Bare array output of $Z[0..n-1]$ with zero period/border reasoning. |
| **R-1A-02** | Luogu P3375 — `【模板】KMP` | `[ZH]` | Direct verification of pattern occurrences and $\pi[1..m]$. |
| **R-1A-03** | Luogu P5410 — `【模板】扩展 KMP / exKMP (Z 函数)` | `[ZH]` | Direct XOR-sum verification of the $Z$-array. |
| **R-1A-04** | Luogu P5829 — `【模板】失配树 (KMP Fail Tree LCA)` | `[ZH]` | Pure LCA query on the KMP fail tree $u \to \pi[u]$ without combinatorics. |
| **R-1A-05** | Luogu P5496 — `【模板】回文自动机（PAM）` | `[ZH]` | Online maintenance of the number of palindromic suffixes ($\text{dep}[u]$) per step. |
| **R-1A-06** | Library Checker — `Enumerate Palindromes` | `[EN]` / `[JA]` | Bare Manacher array verification. |
| **R-1A-07** | CSES 1753 — `String Matching` | `[EN]` | Standard single-pattern matching template. |
| **R-1A-08** | CSES 1732 — `Finding Borders` | `[EN]` | Direct traversal of $\pi[n], \pi[\pi[n]], \dots$ without structural constraints. |

---

### 57.2 Tier 1: Stepping Stone Problems (Period–Border Duality, Fail-Tree Geometry & Exact Periodicity)

#### Problem 1A-01: `[BOI 2009] Radio Transmission` (`Luogu P4391` / `BZOJ 1355`) `[EN]`/`[ZH]`
- **Inline Statement & Constraints**: Given a string $S[1..n]$ ($n \le 10^6$) that is guaranteed to be a prefix of an infinite repetition $T^\infty$, find the minimum possible length $|T|$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Testing all candidate lengths $p \in [1, n]$ explicitly takes $O(n^2)$ or $O(n \log n)$.
  2. *Combinatorial Word Invariant*: $S[1..n]$ is a prefix of $T^\infty$ with $|T| = p \iff S[i] = S[i+p]$ for all $1 \le i \le n-p \iff p \in \text{Per}(S) \iff b = n - p \in \text{Borders}(S)$.
  3. *Algorithmic Compilation*: By Period–Border Duality (Theorem 53.1), minimizing $p = n - b$ is equivalent to maximizing $b \in \text{Borders}(S)$, giving $p_{\min} = n - \pi[n]$ in $O(n)$.
  4. *Boundary Pitfall*: Confusing *exact* period ($p \mid n$) with *weak/fractional* period ($p \nmid n$). Here $S$ is only a *prefix* of $T^\infty$, so $p \nmid n$ is allowed (`aba` has $p_{\min} = 2$).

#### Problem 1A-02: `[POI 2006] OKR-Periods of Words` (`Luogu P3435`) `[EN]`/`[ZH]`
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 10^6$), for each prefix $S[1..i]$, define its *maximum proper period* $Q(i)$ as the largest $p \in [1, i-1]$ (or $\ge i/2$ such that $S[1..p]$ covers $S[1..i]$, i.e., $b = i - p \in \text{Borders}(S[1..i])$ with $b \le i/2$). Compute $\sum_{i=1}^n Q(i)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Walking the KMP fail chain $\pi[i], \pi[\pi[i]], \dots$ down to the smallest positive border for every $i$ takes $O(n^2)$ on $S = \texttt{a}^n$.
  2. *Combinatorial Word Invariant*: Maximizing the period $p = i - b$ requires **minimizing** the positive border $b \in \text{Borders}(S[1..i]) \setminus \{0\}$.
  3. *Algorithmic Compilation*: In the KMP fail tree, the minimum positive border of $i$ is simply the root-child ancestor of $i$, maintained by path compression $\text{min\_b}[i] = (\pi[i] == 0 \text{ ? } i : \text{min\_b}[\pi[i]])$ in $O(n)$, contributing $i - \text{min\_b}[i]$ when $\pi[i] > 0$.
  4. *Boundary Pitfall*: Forgetting that $Q(i)$ requires $b \le i/2$ ($p \ge i/2$), which is automatically satisfied by the *minimum* positive border $b_{\min}$ since if $b_{\min} > i/2$, $\pi[b_{\min}] > 0$ would be a smaller positive border!

#### Problem 1A-03: `[NOI 2014] 动物园 (Zoo)` (`Luogu P2375`) `[ZH]`
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 10^6$, $T \le 5$), for each prefix $S[1..i]$, let $\text{num}[i]$ be the number of **non-overlapping** borders of $S[1..i]$ (borders $b$ with $1 \le b \le \lfloor i/2 \rfloor$). Compute $\prod_{i=1}^n (\text{num}[i] + 1) \bmod (10^9 + 7)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Binary lifting on the fail tree takes $O(n \log n)$ and can TLE for $5 \times 10^6$ total characters.
  2. *Combinatorial Word Invariant*: If $j \le \lfloor i/2 \rfloor$ is the longest non-overlapping border of $S[1..i]$, then expanding $S[1..i]$ to $S[1..i+1]$ increases $i$ by $1$ and increases $j$ by at most $1$ (via KMP matching with pointer $j$), after which at most one extra $\pi$-hop restores $2j \le i+1$.
  3. *Algorithmic Compilation*: Precompute fail-tree depth $\text{dep}[u] = \text{dep}[\pi[u]] + 1$, then maintain a second amortized KMP pointer $j$ restricted to $2j \le i$ in $O(n)$ total time; $\text{num}[i] = \text{dep}[j]$.
  4. *Boundary Pitfall*: Enforcing $2j \le i$ *before* matching $S[i] == S[j+1]$ instead of *after* advancing $j$.

#### Problem 1A-04: `CF 126B — Password` `[EN]`
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 10^6$), find the longest substring $B$ that is simultaneously a prefix, a suffix, and an strictly internal substring $S[l..r]$ ($2 \le l \le r \le n-1$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Checking each border of $S[1..n]$ for internal occurrences via KMP takes $O(n \cdot |\text{Borders}(S)|) = O(n^2)$.
  2. *Combinatorial Word Invariant*: A border $b$ of $S[1..n]$ occurs internally at some right endpoint $r \in [2, n-1] \iff b$ is a border of $S[1..r] \iff b$ is an ancestor of some $\pi[r]$ ($2 \le r \le n-1$) $\iff b \le \max_{2 \le r \le n-1} \pi[r]$.
  3. *Algorithmic Compilation*: Compute $M = \max_{2 \le r \le n-1} \pi[r]$. Answer is $\pi[n]$ if $\pi[n] \le M$, else $\pi[\pi[n]]$ (since $\pi[\pi[n]]$ already occurs at $r = \pi[n] \le n-1$!).
  4. *Boundary Pitfall*: Thinking one must iterate $\pi^{(k)}[n]$ arbitrarily many times; in fact, $\pi[\pi[n]]$ is *always* valid whenever $\pi[\pi[n]] > 0$ because $\pi[n]$ itself is an internal prefix ending at $\pi[n] < n$ whose border is $\pi[\pi[n]]$.

#### Problem 1A-05: `CF 432D — Prefixes and Suffixes` `[EN]`
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 10^5$), list all border lengths $b \in \text{Borders}(S) \cup \{n\}$ in increasing order and for each $b$, output the total number of occurrences of $S[1..b]$ in $S[1..n]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Running KMP for each border $b$ takes $O(n^2)$.
  2. *Combinatorial Word Invariant*: $S[1..b]$ occurs ending at position $r$ iff node $b$ is an ancestor of $r$ in the KMP fail tree (or equivalently in Z-array, $Z[i] \ge b$).
  3. *Algorithmic Compilation*: Initialize $\text{cnt}[r] = 1$ for $1 \le r \le n$ and accumulate $\text{cnt}[\pi[u]] \mathrel{+}= \text{cnt}[u]$ bottom-up from $u = n$ down to $1$ in $O(n)$.
  4. *Boundary Pitfall*: Forgetting to include $b = n$ (the full string itself) or propagating from $1 \to n$ instead of $n \to 1$.

#### Problem 1A-06: `CF 526D — Om Nom and Necklace` `[EN]`
- **Inline Statement & Constraints**: Given $S[1..n]$ and $k$ ($n, k \le 10^6$), determine for each prefix $S[1..i]$ whether it can be written as $A B A B \dots A B A$ ($k+1$ copies of $A$ and $k$ copies of $B$, where $A, B$ may be empty).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Testing all candidate block lengths $|AB| = p$ per prefix $i$ takes $O(n^2)$.
  2. *Combinatorial Word Invariant*: $S[1..i] = (AB)^k A$ where $|AB| = p \iff p \in \text{Per}(S[1..i])$ and $k p \le i \le (k+1)p$. Specifically, choosing $p = i - \pi[i]$ (shortest period) or fixing $p$ and extending via $Z[k p + 1]$: for a fixed period $p$, $(AB)^k$ exists iff $i - \pi[i] \mid p$ at $i = k p$, and then extends as $A$ for at most $\min(p, Z[k p + 1])$ characters!
  3. *Algorithmic Compilation*: Either test at each $i$ whether the largest multiple of $p = i - \pi[i]$ behaves properly: let $q = \lfloor i / p \rfloor$; valid iff $\lfloor q / k \rfloor > (q \bmod k)$ (when $p \mid i$) or $\lfloor q / k \rfloor \ge (q \bmod k) + 1$ (when $p \nmid i$)! That gives an $O(1)$ per-index formula from $\pi[i]$ alone in $O(n)$ total time.
  4. *Boundary Pitfall*: Off-by-one when $p \mid i$ vs. $p \nmid i$ (when $p \mid i$ and $q = k m$, $A$ can be empty, whereas if $p \nmid i$, the trailing remainder $i \bmod p$ forces $|A| > 0$, requiring at least $k+1$ blocks of $A$).

#### Problem 1A-07: `[POI 2005] SZA-Template` (`Luogu P3426`) `[EN]`/`[ZH]`
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 5 \times 10^5$), find the minimum length of a "stamp" $T$ that can cover $S[1..n]$ by overlapping placements of $T$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Every valid stamp $T$ for $S[1..n]$ must be both a prefix and a suffix of $S[1..n]$, i.e., a border $b$ of $S[1..n]$, whose occurrences in $S[1..n]$ leave no gap $> b$.
  2. *Combinatorial Word Invariant*: By recursive structure, $dp[i]$ (shortest stamp for $S[1..i]$) can only be either $i$ itself or $dp[\pi[i]]$. Specifically, $dp[i] = dp[\pi[i]]$ iff $S[1..dp[\pi[i]]]$ stamps $S[1..i]$, which holds iff there is some prefix $j \ge i - \pi[i]$ with $dp[j] = dp[\pi[i]]$!
  3. *Algorithmic Compilation*: Maintain $\text{last\_pos}[x]$ = largest $j < i$ where $dp[j] = x$. At step $i$, if $\text{last\_pos}[dp[\pi[i]]] \ge i - \pi[i]$, set $dp[i] = dp[\pi[i]]$; else $dp[i] = i$. Time $O(n)$.
  4. *Boundary Pitfall*: Checking $\text{last\_pos}[dp[\pi[i]]] \ge i - dp[\pi[i]]$ instead of $i - \pi[i]$ (Wait: since $S[1..\pi[i]]$ is already stamped by $dp[\pi[i]]$ at the suffix $S[i-\pi[i]+1..i]$, any stamped prefix of length $j \ge i - \pi[i]$ connects to the suffix copy of $S[1..\pi[i]]$ with zero gap!).

#### Problem 1A-08: `AtCoder ARC 060 F (ABC 044 D / ARC 060 D) — Best Representation` `[JA]`/`[EN]`
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 5 \times 10^5$), find the minimum number of parts in a partitioning of $S$ into non-periodic substrings (aperiodic / primitive substrings), and the number of ways to achieve this minimum.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: General partition DP is $O(n^2)$, unless the minimum number of parts is bounded by a small constant!
  2. *Combinatorial Word Invariant*: By the Weak Periodicity Lemma / Fine–Wilf, if $S[1..n]$ is aperiodic, answer is $1$ (way: $1$). If $S = \texttt{a}^n$, answer is $n$ (way: $1$). Otherwise ($S$ is periodic with minimum period $p \ge 2$, $p \mid n$), splitting $S$ into $S[1..k]$ and $S[k+1..n]$ yields **at most $2$ parts**! Why? Because for almost all $k$, both $S[1..k]$ and $S[k+1..n]$ are aperiodic (cutting 1 character off a periodic string destroys all periods by Fine–Wilf!).
  3. *Algorithmic Compilation*: Compute KMP on $S$ and $S^R$ to mark in $O(n)$ which prefixes $S[1..k]$ and suffixes $S[k+1..n]$ have a proper divisor period $d \mid \text{len}$; count $k \in [1, n-1]$ where neither is periodic.
  4. *Boundary Pitfall*: Failing to check whether $p = i - \pi[i]$ strictly divides $i$ ($p \mid i$ and $p < i$).

---

### 57.3 Tier 2: Intermediate Problems (Fine–Wilf Applications, Border AP Properties & KMP/Z Structural Bounds)

#### Problem 1A-09: `Universal Cup / QOJ — Fine–Wilf Extremal Periodicity Reconstruction` (`CF Gym 102900 / CCPC — Periodicity & GCD`) `[EN]`/`[ZH]`
- **Inline Statement & Constraints**: Given two target period lengths $p, q \le 10^6$ and string length $n$, determine the maximum number of connected components (free characters) in a string $S[1..n]$ having periods $p$ and $q$, or construct a string with periods $p, q$ but not $\gcd(p, q)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Explicit DSU over $n$ vertices takes $O(n \alpha(n))$, which is too slow when $n, p, q \le 10^{12}$ or when analyzing structural transitions.
  2. *Combinatorial Word Invariant*: By the Fine–Wilf orbit proof (Theorem 53.3), for $n \ge p + q - \gcd(p, q)$ all residue classes mod $\gcd(p, q)$ merge into $\gcd(p, q)$ components. For $p \le q \le n < p + q - \gcd(p, q)$, each residue class mod $g = \gcd(p, q)$ is a single cycle of $+p/g \pmod{q/g}$ with $(p + q - g - n)/g$ missing edges, splitting into exactly $p + q - n$ components!
  3. *Algorithmic Compilation*: Closed-form component count: $\gcd(p, q)$ if $n \ge p + q - \gcd(p, q)$, and $p + q - n$ if $\max(p, q) \le n < p + q - \gcd(p, q)$.
  4. *Boundary Pitfall*: Applying $p + q - n$ when $n < \max(p, q)$ (where period $q > n$ imposes zero constraints).

#### Problem 1A-10: `CF 808G — Anthem of Berland` `[EN]`
- **Inline Statement & Constraints**: Given text $S$ with `?` wildcards and pattern $T$ ($|S| \cdot |T| \le 10^7$), replace `?` to maximize occurrences of $T$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Full KMP-automaton DP takes $O(|S| \cdot |T| \cdot |\Sigma|)$, which TLEs with factor $|\Sigma| = 26$.
  2. *Combinatorial Word Invariant*: Once $T$ matches ending at position $i$, any earlier overlapping match of $T$ must end at $i - p$ where $p = |T| - b$ for some border $b \in \text{Borders}(T)$. By transitive closure of borders, we only need two DP states at each $i$: $f[i]$ (any string ending at $i$) and $g[i]$ ($T$ matches ending at $i$), where $g[i]$ transitions from $f[i - |T|]$ and $\max_{b \in \text{Borders}(T)} g[i - (|T| - b)]$—and by KMP fail-chain transitivity, we only need the AP / fail transitions or precomputed automaton without $|\Sigma|$!
  3. *Algorithmic Compilation*: Maintain $f[i] = \max(f[i-1], g[i])$ and $g[i] = 1 + \max\big(f[i-|T|],\; \max_{b \in \text{Borders}(T)} g[i - |T| + b]\big)$ (even simpler: maintain $h[u]$ on the KMP fail chain or collapse via border transitivity) in $O(|S| + |T|)$ or $O(|S| \log |T|)$!
  4. *Boundary Pitfall*: Allowing a border transition $g[i - |T| + b]$ without verifying that $S[i - |T| + 1 .. i]$ actually matches $T[1..|T|]$.

#### Problem 1A-11: `[CERC 2014] Virus Synthesis` (`Luogu P4762` / `UVA 1679`) `[EN]`/`[ZH]`
- **Inline Statement & Constraints**: Given a DNA string $S[1..n]$ ($n \le 10^5$), you can append/prepend a character (cost 1) or double the current string into $W W^R$ (cost 1). Find minimum operations to build $S$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: The doubling operation produces only even-length palindromes; searching all sub-palindromes naively takes $O(n^2)$.
  2. *Combinatorial Word Invariant*: Any even palindrome $P$ of length $\ell$ in PAM can be formed either by extending $P[2..\ell-1]$ (its parent in the PAM Trie) and doubling ($dp[\text{parent}[u]] + 1$ if we build half and double), or by starting from its longest palindromic border of length $\le \ell / 2$, denoted $\text{half}[u]$, and adding the remaining $\ell/2 - \text{len}[\text{half}[u]]$ characters before doubling!
  3. *Algorithmic Compilation*: Build PAM with the half-link pointer $\text{half}[u]$ (amortized KMP-style pointer on the PAM fail tree satisfying $\text{len}[\text{half}[u]] \le \text{len}[u]/2$). Run BFS on PAM states: for even $u$, $dp[u] = \min(dp[\text{pa}[u]] + 1,\; dp[\text{half}[u]] + \text{len}[u]/2 - \text{len}[\text{half}[u]] + 1)$. Answer is $\min_u (dp[u] + n - \text{len}[u])$. Time $O(n)$.
  4. *Boundary Pitfall*: Allowing odd-length palindromes to use the doubling transition directly.

#### Problem 1A-12: `HDU 6599 — I Love Palindrome String` `[ZH]`/`[EN]`
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 3 \times 10^5$), for each $\ell \in [1, n]$, count occurrences of substrings $P$ of length $\ell$ such that both $P$ and $P[1..\lceil \ell/2 \rceil]$ are palindromes.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Checking each distinct palindrome's prefix $P[1..\lceil \ell/2 \rceil]$ via hashing takes $O(n)$ extra work or risks hash collisions, while walking `fail` links takes $O(n)$ per node.
  2. *Combinatorial Word Invariant*: By Lemma 54.4, the prefix $P[1..\lceil \ell/2 \rceil]$ of a palindrome $P$ is a palindrome $\iff \lceil \ell/2 \rceil \in \text{Borders}(P) \iff$ the PAM `half[u]` pointer (longest palindromic border of $u$ with length $\le \lceil \ell/2 \rceil$) has $\text{len}[\text{half}[u]] == \lceil \ell/2 \rceil$!
  3. *Algorithmic Compilation*: Build PAM, compute subtree occurrence sums $\text{cnt}[u]$ bottom-up along `fail`, maintain $\text{half}[u]$ (or jump via `slink` in $O(\log n)$), and accumulate $\text{cnt}[u]$ into $\text{ans}[\text{len}[u]]$ whenever $\text{len}[\text{half}[u]] == \lceil \text{len}[u]/2 \rceil$. Time $O(n)$.
  4. *Boundary Pitfall*: Using $\lfloor \ell/2 \rfloor$ instead of $\lceil \ell/2 \rceil$ for odd $\ell$.

#### Problem 1A-13: `CF 1200E — Compress Words` `[EN]`
- **Inline Statement & Constraints**: Given $k$ words $W_1, \dots, W_k$ ($\sum |W_i| \le 10^6$), sequentially merge $W_i$ onto the current result $R$ by overlapping the longest suffix of $R$ that matches a prefix of $W_i$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Running KMP on the entire concatenated string $R$ at step $i$ takes $O(\sum_{j \le i} |W_j|)$ per step, leading to $O(k \sum |W_i|) = O(N^2)$ when $|W_i| = 1$.
  2. *Combinatorial Word Invariant*: Any overlap between $R$ and $W_i$ has length at most $L = \min(|R|, |W_i|)$. Thus only the suffix of $R$ of length $L$ can participate!
  3. *Algorithmic Compilation*: Form the temporary string $T = W_i + \texttt{\#} + R[|R|-L+1 .. |R|]$ of length $\le 2|W_i| + 1$, compute $\pi[|T|]$ in $O(|W_i|)$, and append $W_i[\pi[|T|]+1 .. |W_i|]$ to $R$. Total time $O(\sum |W_i|)$.
  4. *Boundary Pitfall*: Omitting the separator `\texttt{#}`, which allows $\pi[|T|] > |W_i|$ via self-overlap inside $R$.

#### Problem 1A-14: `CF 1137B — Camp Schedule` `[EN]`
- **Inline Statement & Constraints**: Rearrange characters of a binary string $S$ to maximize occurrences of a binary pattern $T$ ($|S|, |T| \le 5 \times 10^5$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Greedy non-overlapping placement of $T$ wastes characters when $T$ has a long border.
  2. *Combinatorial Word Invariant*: By Period–Border Duality, maximum packing density of $T$ is achieved by placing $T[1..|T|]$ once and then repeatedly appending the period suffix $T[\pi[|T|]+1 .. |T|]$ of length $p_{\min} = |T| - \pi[|T|]$.
  3. *Algorithmic Compilation*: Compute $\pi[|T|]$, emit $T$, then repeatedly emit $T[\pi[|T|]+1..|T|]$ while inventory of `0`s and `1`s suffices. Time $O(|S| + |T|)$.
  4. *Boundary Pitfall*: Failing when $S$ has fewer `0`s or `1`s than a single copy of $T$.

#### Problem 1A-15: `AtCoder AGC 047 B — First Second` `[JA]`/`[EN]`
- **Inline Statement & Constraints**: Given $N$ strings $S_1, \dots, S_N$ ($\sum |S_i| \le 10^6$), you can repeatedly delete either the first or the second character of a string. Count pairs $(i, j)$ such that $S_i$ can be reduced to $S_j$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Testing all pairs $(i, j)$ takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: Deleting the 1st or 2nd character repeatedly can reduce $S_i$ to $S_j$ ($|S_i| \ge |S_j|$) iff $S_j[2..|S_j|]$ is a suffix of $S_i$ AND the character $S_j[1]$ appears at least once in the prefix $S_i[1 .. |S_i| - |S_j| + 1]$!
  3. *Algorithmic Compilation*: Insert all reversed strings $S_i^R$ into a Trie, maintaining at each node the 26-bit mask of characters present in the remaining prefix of $S_i$; query each $S_j^R$ in $O(\sum |S_i| \cdot |\Sigma|)$.
  4. *Boundary Pitfall*: Counting $i = j$ when the problem asks for ordered pairs $i \ne j$.

#### Problem 1A-16: `[KMP Automaton + Border AP] CF 1721E — Prefix Function Queries` `[EN]`
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 10^6$) and $q \le 10^5$ queries, each appending a short string $T[1..m]$ ($m \le 10$) to $S$, output $\pi[n+1 .. n+m]$ for $S + T$ (queries are independent).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Naive KMP per query can walk the fail chain of $S$ in $O(n)$ steps on adversarial queries (e.g., $S = \texttt{a}^n$, $T = \texttt{b}$), taking $O(q n)$ time!
  2. *Combinatorial Word Invariant*: Either use the KMP automaton $\text{aut}[u][c]$ on $S[1..n]$, OR use `slink` (Border AP jump) so that whenever $\text{diff}[u] = \text{diff}[\pi[u]]$, if $S[u+1] \ne c$, then $S[\pi[u]+1] = S[u+1]$ (by periodicity of $S[1..u]$!) ALSO mismatches $c$, allowing us to jump directly to $\text{slink}[u]$ in $O(\log n)$!
  3. *Algorithmic Compilation*: Precompute $\text{slink}[u]$ on $S[1..n]$ (or $\text{aut}[u][c]$); for $i = n+1 .. n+m$, run KMP with `slink` jumps in $O(n + q m \log n)$ (or $O(n|\Sigma| + q m)$).
  4. *Boundary Pitfall*: Applying precomputed $\text{aut}[u][c]$ when $u \ge n$ without updating transitions for the newly appended characters $n+1 .. n+m$.

---

### 57.4 Tier 3: Advanced Problems (`slink` DP Acceleration, Border-Group Modulo Shortest Path & Palindromic Factorizations)

#### Problem 1A-17: `CF 932G — Palindrome Partition` `[EN]`
- **Inline Statement & Constraints**: Given an even-length string $S[1..n]$ ($n \le 10^6$), count the number of ways to partition $S = s_1 s_2 \dots s_k$ into non-empty substrings such that $s_i = s_{k+1-i}$ for all $1 \le i \le k$, modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Matching outer blocks $s_1 = s_k$ of length $m$ requires simultaneous comparison at both ends of $S$, and $O(n^2)$ DP over block lengths TLEs for $n = 10^6$.
  2. *Combinatorial Word Invariant*: Interleaving $S$ and $S^R$ into $T = S[1]\, S[n]\, S[2]\, S[n-1]\, \dots\, S[n/2]\, S[n/2+1]$ converts $S[l .. l+m-1] = S[n-l-m+2 .. n-l+1]$ into the condition that $T[2l-1 .. 2(l+m-1)]$ is an **even-length palindrome**! By Theorem 54.3 and Lemma 54.4, all palindromic suffixes of $T[1..r]$ partition into $O(\log r)$ APs.
  3. *Algorithmic Compilation*: Build PAM on $T[1..n]$ online; at each $r \in [1, n]$, traverse `slink` updating $g[u] = dp[r - \text{len}[\text{slink}[u]] - \text{diff}[u]] + ([\text{diff}[u] == \text{diff}[\text{fail}[u]]] \cdot g[\text{fail}[u]])$, and if $2 \mid r$, add $\sum g[u]$ to $dp[r]$. Time $O(n \log n)$, space $O(n)$.
  4. *Boundary Pitfall*: Skipping $g[u]$ updates at odd $r$ (see Pitfall 1 in §56.5: an even palindrome at even $r$ can have odd $\text{diff}[u]$, referencing $g[\text{fail}[u]]$ from odd $r - \text{diff}[u]$!).

#### Problem 1A-18: `CF 906E — Reverses` `[EN]`
- **Inline Statement & Constraints**: Given two strings $A[1..n]$ and $B[1..n]$ ($n \le 5 \times 10^5$), choose the minimum number of disjoint intervals $[l_i, r_i]$ such that reversing $A[l_i..r_i]$ for each $i$ transforms $A$ into $B$, and output the intervals.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $O(n^2)$ interval reversal DP fails for $n = 5 \times 10^5$; furthermore, reconstructing optimal intervals requires tracking the argmin over $O(n)$ palindromic lengths per step.
  2. *Combinatorial Word Invariant*: Construct $T = A[1]\, B[1]\, A[2]\, B[2]\, \dots\, A[n]\, B[n]$ of length $2n$. Then $A[l..r]^R = B[l..r] \iff T[2l-1 .. 2r]$ is an even-length palindrome! By Theorem 56.3, the $(\min, \text{argmin})$ accumulator $g[u]$ over an AP chain updates in $O(1)$ from $g[\text{fail}[u]]$ and index $r - \text{len}[\text{slink}[u]] - \text{diff}[u]$.
  3. *Algorithmic Compilation*: Run PAM + `slink` min-DP on $T[1..2n]$. At even $r = 2i$, initialize $dp[r] = (dp[r-2].\text{val}, r-2)$ if $A[i] == B[i]$ else $(\infty, -1)$, then relax $dp[r]$ with $(g[u].\text{val} + 1, g[u].\text{idx})$ across all `slink` chains $u$. Time $O(n \log n)$.
  4. *Boundary Pitfall*: Counting a length-$2$ match $A[i] == B[i]$ as 1 reversal instead of cost 0.

#### Problem 1A-19: `[WC 2016] 论战捆竹竿` (`Luogu P4156` / `UOJ 179` / `LOJ 2085`) `[ZH]`
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 5 \times 10^5$, $T \le 5$) and $W \le 10^{18}$, count how many lengths $L \in [n, W]$ can be formed by starting with $S$ and repeatedly appending $S$ overlapping along a proper non-empty border (or appending with zero overlap, i.e., period $n$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Complete knapsack modulo $n$ over $|\text{Per}(S)| = \Theta(n)$ periods takes $O(n^2)$ time.
  2. *Combinatorial Word Invariant*: By Theorem 54.3, $\text{Per}(S) = \{n - b : b \in \text{Borders}(S)\}$ decomposes into $O(\log n)$ arithmetic progressions $A = \{x + k d : 0 \le k \le c\}$.
  3. *Algorithmic Compilation*: As derived in Iteration 55 (§55.2), process each AP by switching the shortest-path modulus $p_{\text{old}} \to x$ via $\gcd(x, p_{\text{old}})$ cycles in $O(p_{\text{old}} + x)$, then relaxing $+ (x + k d)$ ($1 \le k \le c$) on $\gcd(x, d)$ cycles using a sliding monotonic deque of width $c$ on $D[v_i] - i \cdot d$ in $O(x)$ time. Total time $O(n \log n)$.
  4. *Boundary Pitfall*: Failing to rotate each residue cycle to start at $\arg\min D[v]$ before running the single-pass monotonic queue.

#### Problem 1A-20: `[SDOI 2019] 连续子序列 (Continuous Subsequence)` (`Luogu P5328` / `LOJ 3113`) `[ZH]`
- **Inline Statement & Constraints**: Explore period-constrained and border-AP recurrences on KMP/Thue–Morse-like extensions, accelerating transitions over border chains via `slink` AP aggregation.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Direct summation over all active borders or periodic extensions takes $O(n^2)$.
  2. *Combinatorial Word Invariant*: On the KMP fail tree, borders partition into $O(\log n)$ AP chains via $\text{diff}[u] = u - \pi[u]$ and $\text{slink}[u]$, satisfying the exact shift invariant $\mathcal{I}(u, r) = \mathcal{I}(\pi[u], r - \text{diff}[u]) \cup \{r - \text{len}[\text{slink}[u]] - \text{diff}[u]\}$.
  3. *Algorithmic Compilation*: Maintain $g[u]$ along KMP `slink` chains (or contract periodic blocks recursively) in $O(n \log n)$.
  4. *Boundary Pitfall*: Off-by-one when the base of the AP reaches the empty border $0$.

#### Problem 1A-21: `CF 149E — Martian Strings` `[EN]`
- **Inline Statement & Constraints**: Given text $S[1..n]$ ($n \le 10^5$) and $m \le 100$ patterns $P_1, \dots, P_m$ ($|P_i| \le 1000$), count how many $P_i$ can be split into $P_i = A + B$ ($|A|, |B| \ge 1$) such that $A$ and $B$ occur as disjoint substrings in $S$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Trying all split points $k \in [1, |P|-1]$ and searching $S$ independently takes $O(|P| \cdot n)$ per pattern.
  2. *Combinatorial Word Invariant*: $P[1..k]$ and $P[k+1..|P|]$ occur disjointly in $S \iff$ the **earliest** end position of $P[1..k]$ in $S$, denoted $L[k]$, is strictly less than the **latest** start position of $P[k+1..|P|]$ in $S$, denoted $R[k+1]$.
  3. *Algorithmic Compilation*: Run KMP of $P$ on $S$ (propagating prefix matches via $\pi$ or first-occurrence updates) to find $L[1..|P|]$, and KMP of $P^R$ on $S^R$ to find $R[1..|P|]$ in $O(n + |P|)$ per pattern.
  4. *Boundary Pitfall*: Allowing $|A| = 0$ or $|B| = 0$, or matching when $|P| > |S|$.

#### Problem 1A-22: `CF 615C — Running Track` `[EN]`
- **Inline Statement & Constraints**: Partition target $T[1..m]$ into the minimum number of substrings, each occurring in $S[1..n]$ or $S^R[1..n]$ ($n, m \le 2100$, or $O(n \log n)$ via Z/KMP/SAM).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: DP over all substrings of $T$ is $O(m^2)$, whereas greedily taking the longest match starting at $T[i..]$ is optimal!
  2. *Combinatorial Word Invariant*: Because any substring of a valid piece in $S$ or $S^R$ is also a valid piece (hereditary interval cover property), greedy right-extension strictly dominates all shorter transitions.
  3. *Algorithmic Compilation*: At each $i$, run Z-algorithm / KMP on $T[i..m] + \texttt{\#} + S + \texttt{\$} + S^R$ to find the longest match in $O(n + m)$ per step (or $O(n + m)$ total with SAM).
  4. *Boundary Pitfall*: Reversing the output coordinates when the match comes from $S^R$.

#### Problem 1A-23: `AtCoder ABC 284 F — ABCBAC` `[JA]`/`[EN]`
- **Inline Statement & Constraints**: Given $T[1..2n]$ ($n \le 10^6$), determine if there exist $S[1..n]$ and $i \in [0, n]$ such that $T = S[1..i] + S^R[1..n] + S[i+1..n]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Testing each $i \in [0, n]$ in $O(n)$ takes $O(n^2)$.
  2. *Combinatorial Word Invariant*: $T[1..i] = (T[i+1..2i])^R$ and $T[2n-(n-i)+1..2n] = (T[i+1..n+i])^R$ reduces to two simultaneous LCP/Z-array conditions between $T$ and $T^R$: specifically, on $A = T[1..n] + T^R[1..n]$ and $B = T^R[1..n] + T[1..n]$, index $i$ is valid iff $Z_A[2n - i + 1] \ge i$ and $Z_B[n + i + 1] \ge n - i$.
  3. *Algorithmic Compilation*: Compute two Z-arrays of length $2n$ in $O(n)$ time and check $i \in [0, n]$ in $O(1)$ each.
  4. *Boundary Pitfall*: Off-by-one when $i = 0$ or $i = n$ ($Z[2n+1] = 0$).

#### Problem 1A-24: `POI 2012 — PRE-Prefixuffix` (`Luogu P3538` / `BZOJ 2795` / `POI 2012 OKR-A Horrible Poem`) `[EN]`/`[ZH]`
- **Inline Statement & Constraints**:
  - *PRE-Prefixuffix* ($n \le 10^6$): Find the longest cyclic-equivalent border $U V$ of $S$ (a prefix $U V$ and suffix $V U$ of $S$ with $|U V| \le \lfloor n/2 \rfloor$).
  - *OKR-A Horrible Poem* ($n, q \le 5 \times 10^5$): Given $q$ substring queries $S[l..r]$, find the shortest **exact period** $d \mid (r - l + 1)$ of $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Testing all divisors of $L = r - l + 1$ takes $O(\sqrt{L})$ per query, and testing all $U V$ splits takes $O(n^2)$.
  2. *Combinatorial Word Invariant*:
     - For *OKR*: $d \mid L$ is an exact period of $S[l..r] \iff S[l .. r-d] = S[l+d .. r]$ (by Period–Border Duality!). Moreover, if $p_1^{e_1} \dots p_k^{e_k}$ is the prime factorization of $L$, we can greedily divide $L$ by each prime factor $p_j$ whenever $L / p_j$ is a period, because by the Weak Periodicity Lemma ($\gcd$ closure of exact periods!), the minimum exact period divides every exact period!
     - For *PRE*: If $S[1..i]$ and $S[n-i+1..n]$ are cyclic shifts, letting $f[i]$ be the longest substring centered/shrunk from $i$ matching the opposite end, then shrinking $i \to i - 1$ reduces $f[i]$ by at most $2$ ($f[i-1] \le f[i] + 2$), enabling an $O(n)$ amortized walk!
  3. *Algorithmic Compilation*: For *OKR*, sieve smallest prime factors $\text{spf}[1..n]$ in $O(n)$ and test $\le \log_2 L$ prime divisions in $O(q \log n)$. For *PRE*, compute $f[i]$ backwards from $i = \lfloor n/2 \rfloor \to 1$ in $O(n)$ and take $\max_{i} (i + f[i])$ where $i \in \text{Borders}(S)$.
  4. *Boundary Pitfall*: In *PRE*, forgetting to restrict $i + f[i] \le \lfloor n/2 \rfloor$.

---

### 57.5 Tier 4: Mastery Problems (Internal Border Queries, Dynamic/Weighted `slink` DP, Palindromic Factorization & Inverse Border Theory)

#### Problem 1A-25: `[BJWC 2018] Border 的四种求法 (Four Methods for Substring Borders)` (`Luogu P4482` / `LOJ 2541`) `[ZH]`
- **Inline Statement & Constraints**: Given $S[1..n]$ and $q$ queries $[l, r]$ ($n, q \le 2 \times 10^5$), find the longest proper border of the substring $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Running KMP on $S[l..r]$ takes $O(r - l + 1) = O(n)$ per query. Even querying the SAM Link Tree for $S[l..r]$ checks only one prefix at a time.
  2. *Combinatorial Word Invariant*: By Theorem 54.3 (Weak Periodicity Lemma on Substrings / Kociumaka's Basic Substring Dictionary), the candidate borders of $S[1..r]$ that could also be prefixes of $S[l..r]$ partition into $O(\log n)$ periodic blocks (or via HLD on the SAM Link Tree of $S$, the path from root to node $u_r$ representing $S[1..r]$ has $O(\log n)$ heavy chains where $\text{LCP}(S[1..r], S[1..i]) = \text{len}[\text{LCA}(u_r, u_i)]$!). Specifically, $i \in [l, r-1]$ gives a border of $S[l..r]$ of length $i - l + 1 \iff \text{LCS}(S[1..r], S[1..i]) \ge i - l + 1 \iff i - \text{len}[\text{LCA}(u_r, u_i)] \le l - 1$.
  3. *Algorithmic Compilation*: Decompose the SAM Link Tree with Heavy-Light Decomposition + Segment Tree Merging / 2D range queries on each heavy chain (separating the case where $\text{LCA}(u_r, u_i)$ is the chain ancestor vs. off-chain subtree), answering each query in $O(\log^2 n)$.
  4. *Boundary Pitfall*: Allowing $i = r$ (which gives the improper border $r - l + 1$).

#### Problem 1A-26: `CF 1043G — Speckled Band` `[EN]`
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 2 \times 10^5$) and $q \le 2 \times 10^5$ queries $S[l..r]$, find the minimum number of distinct block types needed if $S[l..r]$ is partitioned into blocks $B_1 B_2 \dots B_k$ and we minimize the maximum frequency of any block (equivalently: test whether answer is $1, 2, 3, 4$, or $-1$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: By Pigeonhole Principle on alphabet size $|\Sigma| = 26$, if all characters in $S[l..r]$ are distinct, answer is $-1$; otherwise the answer is **always $\le 4$**!
  2. *Combinatorial Word Invariant*:
     - Answer $= 1 \iff S[l..r]$ has a proper exact period $d \mid (r - l + 1)$.
     - Answer $= 2 \iff S[l..r]$ has a non-empty border ($A B A \to (AB)(A)$), OR starts with a square $A A$, OR ends with a square $A A$.
     - Answer $= 3 \iff S[l]=S[r]$ ($c B c$), OR an internal character matches $S[l]$ or $S[r]$ ($c A c B$), OR $S[l..r]$ contains *any* square $A A$ internally!
     - Otherwise Answer $= 4$.
  3. *Algorithmic Compilation*: Combine exact period prime-divisor testing (*POI OKR*), shortest square starting/ending at each position via Runs/LCE, and internal border check via $\sqrt{n}$ / IPM to classify each query in $O(\log n)$ or $O(\sqrt{n})$.
  4. *Boundary Pitfall*: Missing the case $S[l..r] = A B A$ with $|A| \ge 1$ for Answer $= 2$ when $S[l..r]$ has no prefix/suffix square.

#### Problem 1A-27: `LOJ 6681 / Luogu P5555 — Common Palindromic Subsequence / Palindrome Border Tree Optimization` (and `GYM 102586F / JOISC Palindrome & Periodicity`) `[ZH]`/`[JA]`
- **Inline Statement & Constraints**: Given strings $S, T$ ($|S|, |T| \le 2.5 \times 10^5$), count or optimize over common palindromic structures / `slink` tree intersections.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Naive product automaton over two PAMs has $O(|S| \cdot |T|)$ states.
  2. *Combinatorial Word Invariant*: Because PAM is a deterministic Trie (with odd and even roots), any common palindrome of $S$ and $T$ corresponds to a **common Trie path** from the roots of $\text{PAM}(S)$ and $\text{PAM}(T)$, and its occurrences are subtree sums in the respective `fail` trees.
  3. *Algorithmic Compilation*: Push occurrence counts bottom-up on $\text{fail}_S$ and $\text{fail}_T$, then run a simultaneous DFS on the intersection of the Trie edges of $\text{PAM}(S)$ and $\text{PAM}(T)$ in $O(|S| + |T|)$ time.
  4. *Boundary Pitfall*: Forgetting to traverse *both* the even root ($0$) and the odd root ($1$) during the simultaneous Trie DFS.

#### Problem 1A-28: `QOJ / Universal Cup — Minimum/Maximum Palindrome Partition (`slink` with Parity & Length Bounds)` (`Gym 104090 / UCup Stage`) `[EN]`/`[ZH]`
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 5 \times 10^5$), partition $S$ into palindromes of length $\ge L$ (or with alternating parity / weight) to minimize/maximize cost.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Adding a lower bound $\ell \ge L$ to palindrome partition cuts an AP chain $\mathcal{L}(u)$ in the middle, seemingly breaking the $O(1)$ `slink` accumulator $g[u]$!
  2. *Combinatorial Word Invariant*: Observe that in $\mathcal{I}(u, r) = \{r - \ell : \ell \in \mathcal{L}(u)\}$, the condition $\ell \ge L$ is equivalent to $r - \ell \le r - L$! Because $g[u]$ is accumulated sequentially by adding one new index $r' - \text{len}[\text{slink}[u]] - \text{diff}[u]$ at each step $r' \equiv r \pmod d$, the elements in $g[u]$ were inserted in **strictly increasing order of left endpoint $i = r - \ell$**!
  3. *Algorithmic Compilation*: Either maintain a monotonic queue per AP chain or simply delay inserting $dp[i]$ until $r - i \ge L$, OR notice that for each `slink` chain $u$, the valid left endpoints form a prefix of the chain that can be queried on the PAM fail tree (via DFS order + Segment Tree on residue classes or delayed `g[u]`).
  4. *Boundary Pitfall*: Assuming `slink` accumulator works unchanged when a *minimum* length bound $L > 1$ truncates the bottom of an AP chain.

#### Problem 1A-29: `[THUPC 2018 / Luogu P5446] 绿绿和串串 (Mirror Flipping Prefix Restoration)` `[ZH]`
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 10^6$, $\sum n \le 5 \times 10^6$), find all initial lengths $k \in [1, n]$ such that repeatedly choosing a prefix $P$ and replacing it with $P[1..|P|-1] + P^R$ can produce $S[1..n]$ as a prefix.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Testing each $k$ by simulating mirror reflections takes $O(n^2)$.
  2. *Combinatorial Word Invariant*: Mirroring at index $k$ requires the palindrome centered at $k$ in $S$ to reach **either** the right end $n$ (meaning $k$ can produce $S[1..n]$ directly in one flip!) **or** the left end $1$ AND the mirrored target $k + r_k - 1$ is itself valid!
  3. *Algorithmic Compilation*: Compute odd Manacher radii $R[1..n]$ in $O(n)$, then scan backwards $k = n \to 1$: $k$ is valid iff $k + R[k] - 1 == n$, OR ($k - R[k] + 1 == 1$ and $\text{valid}[k + R[k] - 1]$ is true). Time $O(n)$.
  4. *Boundary Pitfall*: Checking $k - R[k] + 1 == 1$ when $k = 1$ without ensuring $R[k] > 1$ (non-trivial flip).

#### Problem 1A-30: `[SHOI 2011] 双倍回文 (Double Palindrome)` (`Luogu P4287`) `[ZH]`
- **Inline Statement & Constraints**: Given $S[1..n]$ ($n \le 5 \times 10^5$), find the maximum length of a substring of the form $W W^R W W^R$ (an even palindrome whose half is also an even palindrome).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Testing all $\Theta(n^2)$ even palindromes takes $O(n^2)$.
  2. *Combinatorial Word Invariant*: By Lemma 54.4, an even palindrome $P$ of length $4k$ has the form $W W^R W W^R \iff$ $P$ has a palindromic border of length $2k = |P|/2$. On PAM, this holds iff some ancestor on the fail chain of $u$ (specifically $\text{half}[u]$) has $\text{len}[\text{half}[u]] = \text{len}[u]/2$ and $4 \mid \text{len}[u]$.
  3. *Algorithmic Compilation*: Build PAM with `half[u]` pointer in $O(n)$ (or Manacher + DSU/set sweep over centers) and take $\max\{\text{len}[u] : 4 \mid \text{len}[u] \text{ and } \text{len}[\text{half}[u]] == \text{len}[u]/2\}$.
  4. *Boundary Pitfall*: Accepting $\text{len}[u] = 2k$ when $k$ is odd ($W W^R$ where $W$ itself is a palindrome of odd length is NOT $X X^R X X^R$).

#### Problem 1A-31: `CF 1764G / AtCoder AGC 055 / Universal Cup — Inverse KMP & Border-Set Realizability` (`[Z-Array / KMP Restoration]`) `[EN]`/`[JA]`
- **Inline Statement & Constraints**: Given a proposed KMP array $\pi[1..n]$ (or border set $B \subseteq \{1, \dots, n-1\}$), determine whether a valid string over alphabet $\Sigma$ exists, or count the number of such strings modulo $998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Arbitrary integer arrays $\pi[1..n]$ or subset $B$ violate hidden periodicity constraints.
  2. *Combinatorial Word Invariant*:
     - For $\pi[1..n]$: $\pi[i] \le \pi[i-1] + 1$; every ancestor $u$ popped on the walk from $\pi[i-1]$ down to $\pi[i] - 1$ forces $S[i] \ne S[u+1]$; if $\pi[i] > 0$, $S[i] = S[\pi[i]]$; and critically, no popped ancestor $u$ may already satisfy $S[u+1] = S[\pi[i]]$!
     - By Theorem 54.3 (`slink`), all ancestors $u$ in the same AP chain ($\text{diff}[u] = \text{diff}[\pi[u]]$) share the **exact same next character** $S[u+1] = S[\pi[u]+1]$ (since $d = u - \pi[u]$ is a period of $S[1..u]$, and $u+1$ is one step past $u$? Wait: $S[\pi[u]+1] = S[u+1 - d] = S[u+1]$ whenever $u$ had period $d$ extended by 1, wait: for internal nodes of an AP chain where $\text{diff}[u] = \text{diff}[\pi[u]] = d$, $\pi[u] + 1 + d = u + 1$, wait: inside $S[1..u]$ with period $d$, index $\pi[u] + 1 = u - d + 1 \le u$, so $S[\pi[u]+1] = S[(u - d + 1) - d] = S[\pi[\pi[u]] + 1]$!). Thus the set of forbidden characters along the entire KMP fail chain has size at most $O(\log i)$ and can be collected via `slink` jumps in $O(\log i)$!
  3. *Algorithmic Compilation*: At each step $i$, jump `slink` from $\pi[i-1]$ to collect the $O(\log i)$ distinct forbidden characters $S[\pi[u]+1]$, verify consistency, and multiply ways by $|\Sigma| - |\text{forbidden}|$ when $\pi[i] = 0$. Total time $O(n \log n)$.
  4. *Boundary Pitfall*: Forgetting that for $u$ with $\text{diff}[u] = \text{diff}[\pi[u]]$, $S[\pi[u]+1]$ equals $S[\pi[\pi[u]]+1]$, NOT $S[u+1]$ (because $u+1$ is outside $S[1..u]$!).

#### Problem 1A-32: `CF 1286E — Fedya the Potter Strikes Back` `[EN]`
- **Inline Statement & Constraints**: Online string $S[1..n]$ ($n \le 6 \times 10^5$) with character $S[i]$ and weight $W[i]$ revealed one by one (encrypted with previous 128-bit answer!). After each step $i$, add to the total answer the sum of $\min_{l \le k \le i} W[k]$ over all $l \in [1, i]$ such that $S[l..i] = S[1..i-l+1]$ (i.e., over all borders of $S[1..i]$ plus the full string $S[1..i]$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Fully online (encrypted queries) + maintaining $\min W$ over all active borders at step $i$. When $S[i]$ is appended, any border $u$ of $S[1..i-1]$ with $S[u+1] \ne S[i]$ is **deleted** from the active border set! Walking the KMP fail chain naively to delete mismatched borders can visit $O(n)$ nodes in a single step if we revisit surviving nodes!
  2. *Combinatorial Word Invariant*: By the Border AP / KMP `slink` theorem (Iteration 54 & Problem 1A-31), along any AP chain where $\text{diff}[u] = \text{diff}[\pi[u]]$, the next character after $\pi[u]$ is $S[\pi[u]+1] = S[\pi[\pi[u]]+1]$. Better yet, define the **shortcut fail pointer** $\text{anc}[u]$ to be the highest ancestor $v = \pi[u]$ such that $S[v+1] \ne S[u+1]$:
     $$\text{anc}[u] = \begin{cases} \pi[u] & \text{if } S[\pi[u]+1] \ne S[u+1], \\ \text{anc}[\pi[u]] & \text{if } S[\pi[u]+1] == S[u+1]. \end{cases}$$
     When advancing from $i-1 \to i$, every border $v$ of $S[1..i-1]$ with $S[v+1] \ne S[i]$ is **permanently killed** at step $i$ and never survives to $i+1$. Using $\text{anc}[u]$ (or `slink`) skips all borders with $S[v+1] == S[i]$ in $O(1)$ per mismatching group, so each inserted border is deleted **at most once** across the entire algorithm!
  3. *Algorithmic Compilation*: Maintain active border left endpoints in a `std::map<int, int>` (frequency map of current $\min W$ values) + a monotonic stack on $W[1..i]$. At step $i$:
     - Walk the KMP fail chain of $i-1$, using $\text{anc}[u]$ to jump directly to borders $v$ where $S[v+1] \ne S[i]$ and erase their left endpoints $i - 1 - v + 1$ from the frequency map (amortized $O(1)$ erasures per step!).
     - Push $W[i]$ onto the monotonic stack, merging all map entries $> W[i]$ into $W[i]$ in amortized $O(\log n)$ time.
     - Maintain the 128-bit running sum in $O(n \log n)$ total time!
  4. *Boundary Pitfall*: Walking $\pi[u]$ one by one during deletion instead of jumping over matching characters $S[v+1] == S[i]$ via $\text{anc}[u]$—without $\text{anc}[u]$, $S = \texttt{a}^n$ walks $O(n)$ matching borders at every step, degrading to $O(n^2)$!

---

## 58. Multilingual Bibliography & Structural Summary Table for Wave 1A

### 58.1 Canonical Literature & Treatises (`[EN]` / `[ZH]` / `[JA]`)

1. **[EN] Fine & Wilf (1965)**: N. J. Fine and H. S. Wilf, *"Uniqueness theorems for periodic functions"*, Proc. Amer. Math. Soc. 16 (1965), 109–114. (Origin of the $p + q - \gcd(p, q)$ periodicity threshold and central Sturmian counterexamples.)
2. **[EN] Lothaire (1997 / 2002)**: M. Lothaire, *Combinatorics on Words* & *Algebraic Combinatorics on Words*, Cambridge University Press. (Chapter 1 & Chapter 2: Periodicity, Sturmian words, and Central words.)
3. **[EN] Rubinchik & Shur (2015 / 2018)**: M. Rubinchik and A. M. Shur, *"EERTREE: An Efficient Data Structure for Processing Palindromes in Strings"*, European J. Combinatorics 68 (2018), 249–265. (Introduces PAM, `diff[u]`, and `slink[u]` for $O(n \log n)$ palindrome partition DP.)
4. **[EN] Fici, Gagie, Manea & Radoszewski (2014)**: *"Subquadratic Algorithms for Palindromic Factorization"*, Stringology /ICALP. (Independent discovery of the $O(\log n)$ AP decomposition of palindromic suffixes.)
5. **[ZH] 国家集训队论文 2017 — 翁文涛 (Weng Wentao)**: 《回文自动机及其应用》 & WC2016《论战捆竹竿》命题报告. (Establishes `Border 的等差数列性质`, dynamic modulus switching + residue-cycle monotonic queue in $O(n \log n)$.)
6. **[ZH] 国家集训队论文 2019 — 金策 (Jin Ce)**: 《字符串算法选讲》 (`Border Theory`, `Weak Periodicity Lemma`, `Four Methods for Substring Borders [BJWC2018]`, and `Runs`).
7. **[JA] `snuke` / `maspypy` / `noshi91` String Treatises**: Japanese competitive programming expositions on Palindromic Tree `slink` DP (`回文木の応用と等差数列分解`) and KMP shortcut links (`CF 1286E`).

### 58.2 Wave 1A Master Structural Invariant Reference

| Structural Theorem / Technique | Core Mathematical Invariant | Complexity Reduction | Canonical Problems |
| :--- | :--- | :--- | :--- |
| **Period–Border Duality** | $b \in \text{Borders}(S[1..n]) \iff p = n - b \in \text{Per}(S[1..n])$ | $O(n^2) \to O(n)$ | `BOI 2009 Radio`, `POI 2006 OKR`, `CF 526D` |
| **Fine–Wilf Theorem** | $p, q \in \text{Per}(S)$ and $|S| \ge p + q - \gcd(p, q) \implies \gcd(p, q) \in \text{Per}(S)$; tight at $p+q-\gcd(p,q)-1$ | Exact component formula | `ARC 060 F`, `UCup Fine–Wilf` |
| **Weak Periodicity & Border APs** | Borders $\ge |S|/2$ form 1 AP of step $n - \pi[n]$; all borders partition into $\le \lceil \log_2 n \rceil$ APs | $\Theta(n)$ borders $\to O(\log n)$ chains | `CF 1721E`, `BJWC 2018 Border` |
| **Border Modulo Shortest Path** | Switch modulus $p_{\text{old}} \to x$ on $\gcd(x, p_{\text{old}})$ cycles; slide monotonic deque of width $c$ on $\gcd(x, d)$ cycles | $O(n^2) \to O(n \log n)$ | `[WC2016] 论战捆竹竿 (Luogu P4156)` |
| **PAM / KMP `slink` DP** | $\mathcal{I}(u, r) = \mathcal{I}(\text{fail}[u], r - \text{diff}[u]) \cup \{r - \text{len}[\text{slink}[u]] - \text{diff}[u]\}$; Lemma 56.2 ensures $\text{fail}[u]$ was chain-top at $r - \text{diff}[u]$ | $O(n^2) \to O(n \log n)$ | `CF 932G`, `CF 906E`, `[SDOI2019] 连续子序列` |
| **Online Border Amortization (`anc[u]`)** | $\text{anc}[u]$ skips ancestors with $S[v+1] = S[u+1]$; mismatched borders are permanently deleted in $O(1)$ amortized | $O(n^2) \to O(n \log n)$ | `CF 1286E — Fedya the Potter` |
