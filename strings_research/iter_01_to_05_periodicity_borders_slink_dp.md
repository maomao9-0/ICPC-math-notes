# Wave 1A Research Report (Cohort 1, Iterations 01–05): Structural Periodicity, Border Theory, Weak Periodicity Lemma & Series-Link (`slink`) DP

> [!IMPORTANT]
> **Cohort 1 Primary Discovery & Structural Audit Report (`iter_01_to_05_periodicity_borders_slink_dp.md`)**
> This document covers **Iterations 01–05** of the Phase 1 Multi-Cohort Research Pipeline defined in `strings_research/PLAN.md`. All derivations strictly obey the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**:
> 1. **The Diagnostic Signal (Why Naive String Structures Fail)**
> 2. **The Combinatorial Word Invariant (Double-Overlap / Periodicity / Index-Orbit Proof)**
> 3. **The Reverse-Engineering Scratchpad (Algorithmic & Data-Structure Compilation)**
> 4. **Boundary Pitfalls & Broken-Invariant Counterexamples**

---

## 0. Wave 1A Scope, Prerequisite Boundary & Multilingual Rosetta Stone

### 0.1 Prerequisite Boundary
Per `AGENTS.md` and `strings_research/PLAN.md`, the reader is assumed to possess tested, black-box library implementations of:
- **KMP Prefix Function (`pi` / `fail` array)**: $\pi[i] = \max\{k < i : S[1..k] = S[i-k+1..i]\}$ in $O(N)$ time.
- **Z-Algorithm (`z` array)**: $z[i] = \text{LCP}(S[1..N], S[i..N])$ in $O(N)$ time.
- **Polynomial Rolling Hash / Suffix Array (`SA` + `LCP` RMQ)**: $O(1)$ Longest Common Extension ($\text{LCE}$) queries.
- **Palindromic Automaton (PAM / Eertree)**: Standard $O(N)$ construction with nodes $0$ (even root, $\text{len}=0$), $1$ (odd root, $\text{len}=-1$), transitions $\delta(u, c)$, and suffix failure links $\text{fail}(u)$.

**What This Wave Teaches Beyond Templates**:
Why standard KMP/Z/PAM fail on $O(N^2)$-transition problems (such as border knapsack, palindrome partition DP, or two-period equations), and how **Period–Border Duality**, the **Fine–Wilf Theorem**, the **Weak Periodicity Lemma**, and **Log-Block Border Arithmetic Progressions (`slink` / `diff`)** compress $O(N)$ active states into $O(\log N)$ structured blocks.

### 0.2 Multilingual Stringology Rosetta Stone (Wave 1A)

| Concept (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) | Canonical Notation |
| :--- | :--- | :--- | :--- |
| Period (weak / general period) | 周期 (广义周期) | 周期 (Period) | $p \in \text{Per}(S)$ ($S[i] = S[i+p]$ for $1 \le i \le |S|-p$) |
| Exact / full period | 整周期 / 循环节 | 完全周期 / 最小周期 | $p \in \text{Per}(S)$ and $p \mid |S|$ |
| Border (proper prefix = suffix) | Border / 公共前后缀 | ボーダー (接頭辞かつ接尾辞) | $b \in \text{Border}(S)$ ($S[1..b] = S[|S|-b+1..|S|]$) |
| Period–Border Duality | 周期与 Border 的对偶性 | 周期とボーダーの双対性 | $p \in \text{Per}(S) \iff |S|-p \in \text{Border}(S)$ |
| Weak Periodicity Lemma | 弱周期引理 | 弱周期性補題 | $\|S\| \ge p+q \implies \gcd(p,q) \in \text{Per}(S)$ |
| Fine–Wilf Theorem | Fine–Wilf 定理 (周期引理) | Fine–Wilf の定理 | $\|S\| \ge p+q-\gcd(p,q) \implies \gcd(p,q) \in \text{Per}(S)$ |
| Sturmian / Fibonacci Word | Sturmian 词 / 斐波那契串 | Sturmian 語 / フィボナッチ文字列 | Extremal word of length $p+q-\gcd(p,q)-1$ |
| Border AP Property | Border 的等差数列性质 | ボーダーの等差数列分解 | Borders partition into $\le \lceil \log_2 \|S\| \rceil$ APs |
| Modulo Shortest Path + AP Knapsack | 同余最短路 + 等差数列背包 | 同余最短路 + 等差数列ナップサック | Residue-cycle sliding window on border APs |
| Series Link / Difference Link | 等差数列跳链 (`slink` / `diff`) | 直列リンク (`slink`) / 回文オートマトンDP | $\text{diff}(u) = \text{len}(u)-\text{len}(\text{fail}(u))$, $\text{slink}(u)$ |

---

## Iteration 01: Period–Border Duality, the Fine–Wilf Periodicity Theorem & Extremal Sturmian Word Tightness

### 1.1 The Diagnostic Signal (Why Naive String Structures Fail)

When solving string problems involving overlapping occurrences of patterns, tandem repeats, or multiple border constraints, a naive approach treats each border length $b \in \text{Border}(S)$ or period $p \in \text{Per}(S)$ as an independent degree of freedom. Specifically:
- Suppose a string $S$ of length $N$ has two known periods $p$ and $q$ (for instance, $S$ occurs at two overlapping positions in a text, or $S$ has two borders $N-p$ and $N-q$).
- Maintaining both periodicity constraints $S[i] = S[i+p]$ and $S[i] = S[i+q]$ explicitly via a Disjoint Set Union (DSU) over indices $1 \dots N$ takes $O(N \alpha(N))$ work per constraint pair. Across $Q$ queries or $O(N)$ substrings, this degrades to $O(N^2)$.
- Furthermore, when designing strings that *violate* a target period or testing heuristic pruning on KMP/Z-arrays, programmers often assume either that any two periods $p, q$ immediately force period $\gcd(p, q)$ regardless of $|S|$ (false for short strings), or that two periods can coexist indefinitely without collapsing (false once $|S| \ge p + q - \gcd(p, q)$).

The diagnostic signal for **Iteration 01** is any condition where a string segment $S[l..r]$ simultaneously satisfies two shift equalities $S[i] = S[i+p]$ and $S[i] = S[i+q]$, or where two occurrences of a pattern $P$ overlap by more than $|P| - \gcd(p, q)$.

---

### 1.2 The Combinatorial Word Invariant (Period–Border Duality & Fine–Wilf Index-Orbit Proof)

#### 1.2.1 Concrete Objects & Period–Border Duality
Let $S = S[1..N]$ be a 1-indexed string of length $N$ over an alphabet $\Sigma$.
- **Definition (Period)**: An integer $p \in \{1, 2, \dots, N\}$ is a *period* of $S$ (written $p \in \text{Per}(S)$) if
  $$S[i] = S[i + p] \quad \text{for all } 1 \le i \le N - p.$$
  Note that $p = N$ is vacuously a period of every string of length $N$. We do **not** require $p \mid N$; a period is a shift-invariance on the valid index domain, so $S$ is a prefix of the infinite periodic word $S[1..p]^\infty$.
- **Definition (Border)**: An integer $b \in \{0, 1, \dots, N-1\}$ is a *(proper) border length* of $S$ (written $b \in \text{Border}(S)$) if the prefix of length $b$ equals the suffix of length $b$:
  $$S[1..b] = S[N - b + 1 .. N].$$
  Writing out the character-by-character equality of $S[1..b]$ and $S[N-b+1..N]$ yields:
  $$S[i] = S[N - b + i] \quad \text{for all } 1 \le i \le b.$$
  Substituting $p = N - b$ turns this into $S[i] = S[i + p]$ for all $1 \le i \le N - p$. This establishes the fundamental **Period–Border Duality**:

$$\boxed{p \in \text{Per}(S) \iff N - p \in \text{Border}(S) \qquad (1 \le p \le N).}$$

Long borders correspond to **small periods** (strong structural repetition), whereas short borders correspond to **large periods** (weak boundary overlap).

```
S[1 ....................................... b ............ N]
|<--------------- border b = N - p --------->|
              |<--------------- border b = N - p --------->|
|<-- p ------>|
For every 1 <= i <= N - p:  S[i] == S[i + p]
```

---

#### 1.2.2 Warm-Up: The Weak Periodicity Lemma ($N \ge p + q$)
Before proving the sharp threshold $N \ge p + q - \gcd(p, q)$, observe why $N \ge p + q$ is immediate.

> **Lemma 1.1 (Weak Periodicity Lemma)**: If $p, q \in \text{Per}(S)$ and $|S| \ge p + q$, then $\gcd(p, q) \in \text{Per}(S)$.

*Proof (Euclidean Step on Periods)*: Without loss of generality assume $p > q$. We claim $p - q \in \text{Per}(S)$. For any index $i \in [1, |S| - (p - q)]$, we must show $S[i] = S[i + p - q]$.
Since $|S| \ge p + q$, every index $i \in [1, |S|$] either satisfies $i + p \le |S|$ or $i - q \ge 1$ (because if both failed, $i > |S| - p \ge q \implies i - q \ge 1$, a contradiction).
- **Case 1 ($i + p \le |S|$)**: Using period $p$ forward and period $q$ backward from $i + p$,
  $$S[i] \stackrel{(+p)}{=} S[i + p] \stackrel{(-q)}{=} S[i + p - q].$$
- **Case 2 ($i - q \ge 1$)**: Using period $q$ backward and period $p$ forward from $i - q$,
  $$S[i] \stackrel{(-q)}{=} S[i - q] \stackrel{(+p)}{=} S[i - q + p].$$

In both cases $S[i] = S[i + p - q]$. Replacing $(p, q)$ by $(p - q, q)$ preserves the hypothesis $|S| \ge p + q > (p - q) + q$, so repeating the subtractive Euclidean algorithm terminates at $\gcd(p, q) \in \text{Per}(S)$. $\blacksquare$

Why is $N \ge p + q$ *not* tight? In the Euclidean reduction above, after replacing $p$ by $p - q$, the new required length for the next step is only $(p - q) + q = p$, which is strictly smaller than $p + q$! Only the very first step needed room to step $+p$ or $-q$, and even there we never needed to step from the last $\gcd(p, q)$ indices synchronously.

---

#### 1.2.3 The Fine–Wilf Theorem ($N \ge p + q - \gcd(p, q)$) via Index-Orbit Decomposition

> **Theorem 1.2 (Fine–Wilf Theorem, 1965)**: Let $S[1..N]$ have periods $p$ and $q$, and let $g = \gcd(p, q)$. If
> $$N \ge p + q - g,$$
> then $g \in \text{Per}(S)$. Moreover, the threshold $p + q - g$ is sharp: for every pair of periods $(p, q)$ where $p \nmid q$ and $q \nmid p$, there exists a binary string of length $N = p + q - g - 1$ having periods $p$ and $q$ but **not** period $g$.

*Proof (Decimation + Modular Hamiltonian Path on Index Orbits)*:

**Step 1: Reduction to the Coprime Case $\gcd(p, q) = 1$ via Residue Decimation.**
Partition the indices $\{1, \dots, N\}$ into $g = \gcd(p, q)$ arithmetic progressions (residue classes modulo $g$). For each $r \in \{1, \dots, g\}$, define the decimated string
$$S^{(r)} = S[r]\, S[r + g]\, S[r + 2g] \dots S[r + (m_r - 1)g],$$
where $m_r = \lfloor (N - r)/g \rfloor + 1$ is the number of indices in $\{1, \dots, N\}$ congruent to $r \pmod g$.
Since $N \ge p + q - g$, even for the largest remainder $r = g$, the length of $S^{(r)}$ is at least
$$m_r \ge \frac{(p + q - g) - g}{g} + 1 = \frac{p}{g} + \frac{q}{g} - 1 = p' + q' - 1,$$
where $p' = p/g$ and $q' = q/g$ satisfy $\gcd(p', q') = 1$.
Because $p = p' g$ and $q = q' g$ are multiples of $g$, the periodicity conditions $S[i] = S[i+p]$ and $S[i] = S[i+q]$ act entirely within each residue class $S^{(r)}$, giving $p', q' \in \text{Per}(S^{(r)})$.
If we prove the theorem for coprime periods $p', q'$ at length $p' + q' - 1$ (showing that each $S^{(r)}$ has period $\gcd(p', q') = 1$, i.e., $S^{(r)}$ is a constant string of a single repeated character), then $S[i] = S[i + g]$ holds for all $1 \le i \le N - g$, which means $g \in \text{Per}(S)$!

**Step 2: The Index-Transition Bijection for $\gcd(p, q) = 1$ and $N = p + q - 1$.**
Assume now that $\gcd(p, q) = 1$ and $N = p + q - 1$. We must prove that $S[1..p+q-1]$ has period $1$, i.e., $S[1] = S[2] = \dots = S[p+q-1]$.
Consider the index set $V = \{1, 2, \dots, p + q - 1\}$. Define a partial transition map $f : V \setminus \{q\} \to V \setminus \{p\}$ by:
$$f(i) = \begin{cases} i + p & \text{if } 1 \le i \le q - 1, \\ i - q & \text{if } q + 1 \le i \le p + q - 1. \end{cases}$$
Let us verify three properties of $f$:
1. **Valid Bounds & Character Invariance**:
   - If $1 \le i \le q - 1$, then $p + 1 \le i + p \le p + q - 1 = N$. Since $p \in \text{Per}(S)$, $S[f(i)] = S[i + p] = S[i]$.
   - If $q + 1 \le i \le p + q - 1$, then $1 \le i - q \le p - 1 \le N$. Since $q \in \text{Per}(S)$, $S[f(i)] = S[i - q] = S[i]$.
   Thus $S[f(i)] = S[i]$ for every $i \in V \setminus \{q\}$.
2. **Modular Uniformity**:
   Observe that $i - q \equiv i + p \pmod{p + q}$. Therefore, on the full cyclic group $\mathbb{Z}/(p+q)\mathbb{Z} = \{0, 1, \dots, p+q-1\}$, the map $\tilde{f}(x) = (x + p) \bmod (p + q)$ agrees with $f(i)$ on all $i \in \{1, \dots, p+q-1\} \setminus \{q\}$.
3. **Single Orbit (Hamiltonian Path) Property**:
   Since $\gcd(p, q) = 1$, we have $\gcd(p, p + q) = \gcd(p, q) = 1$. Hence $p$ is a generator of the additive group $\mathbb{Z}/(p+q)\mathbb{Z}$, and $\tilde{f}(x) = (x + p) \bmod (p + q)$ forms a **single directed cycle of length $p + q$** passing through every residue in $\mathbb{Z}/(p+q)\mathbb{Z}$:
   $$0 \xrightarrow{+p} p \xrightarrow{+p} 2p \bmod (p+q) \xrightarrow{+p} \dots \xrightarrow{+p} q \xrightarrow{+p} 0.$$
   When we restrict from $\mathbb{Z}/(p+q)\mathbb{Z}$ to $V = \{1, 2, \dots, p + q - 1\}$, we delete only the single vertex $0 \pmod{p+q}$ (along with its incoming edge $q \to 0$ and outgoing edge $0 \to p$).
   Deleting one vertex from a single directed cycle of length $p + q$ leaves a **single directed Hamiltonian path of length $p + q - 1$** starting at $p$ and ending at $q$:
   $$p \xrightarrow{f} f(p) \xrightarrow{f} f^{(2)}(p) \xrightarrow{f} \dots \xrightarrow{f} q.$$
   Since every vertex $i \in \{1, \dots, p+q-1\}$ appears on this single path and $S[f(i)] = S[i]$ along every edge, we conclude:
   $$S[p] = S[f(p)] = S[f^{(2)}(p)] = \dots = S[q],$$
   so all $p + q - 1$ characters of $S$ are identical! $\blacksquare$

---

#### 1.2.4 Hand-Checkable Example & Extremal Tightness at $N = p + q - \gcd(p, q) - 1$

Let $(p, q) = (5, 8)$, so $\gcd(5, 8) = 1$ and the Fine–Wilf threshold is $N = 5 + 8 - 1 = 12$.
Let us trace the Hamiltonian path $f$ on $V = \{1, 2, \dots, 12\}$ ($f(i) = i + 5$ for $i \le 7$, $f(i) = i - 8$ for $i \ge 9$):
$$5 \xrightarrow{+5} 10 \xrightarrow{-8} 2 \xrightarrow{+5} 7 \xrightarrow{+5} 12 \xrightarrow{-8} 4 \xrightarrow{+5} 9 \xrightarrow{-8} 1 \xrightarrow{+5} 6 \xrightarrow{+5} 11 \xrightarrow{-8} 3 \xrightarrow{+5} 8.$$
Every index from $1$ to $12$ is visited in a single chain of 12 vertices!

Now suppose we reduce the string length by 1 to **$N = p + q - 2 = 11$**.
Which vertex disappears from the chain above? Only vertex **$12 = p + q - 1$**!
Deleting vertex $12$ from the middle of the path $5 \to 10 \to 2 \to 7 \to \mathbf{12} \to 4 \to 9 \to 1 \to 6 \to 11 \to 3 \to 8$ splits the single path into **exactly two connected components**:
- **Component $C_1$ (pre-12)**: $\{5, 10, 2, 7\}$ (4 indices)
- **Component $C_2$ (post-12)**: $\{4, 9, 1, 6, 11, 3, 8\}$ (7 indices)

If we assign `'b'` to Component $C_1$ ($\{2, 5, 7, 10\}$) and `'a'` to Component $C_2$ ($\{1, 3, 4, 6, 8, 9, 11\}$), we obtain the unique extremal binary word of length 11:

```
Index:   1  2  3  4  5  6  7  8  9 10 11
String:  a  b  a  a  b  a  b  a  a  b  a
```

Let us verify its periods:
- **Period $p = 5$**: $S[1..6] = \texttt{abaaba}$ and $S[6..11] = \texttt{abaaba}$. Match!
- **Period $q = 8$**: $S[1..3] = \texttt{aba}$ and $S[9..11] = \texttt{aba}$. Match!
- **Period $g = 1$**: Fails because $S$ contains both `'a'` and `'b'`.

> **Corollary 1.3 (Structural Characterization of Fine–Wilf Extremal Words)**:
> For any coprime $(p, q)$ and $N = p + q - 2$, deleting vertex $p + q - 1$ from the Fine–Wilf Hamiltonian path splits $\{1, \dots, p + q - 2\}$ into **exactly two orbits**. Thus:
> 1. The maximum number of distinct characters in a string of length $p + q - 2$ with periods $p, q$ that violates period $1$ is $2$ (every such string is binary up to alphabet relabeling, and there is a unique binary string up to $0 \leftrightarrow 1$ complement).
> 2. When $(p, q) = (F_k, F_{k+1})$ are consecutive Fibonacci numbers, the extremal word of length $F_{k+2} - 2$ is the **central Sturmian / Pirillo word** (the prefix of the infinite Fibonacci word of length $F_{k+2} - 2$), which is also a palindrome!
> 3. For general $g = \gcd(p, q)$ at length $N = p + q - g - 1$, only the residue class $r \equiv p + q - g \equiv g \pmod g$ has decimated length $p' + q' - 2$ (splitting into 2 orbits), while the other $g - 1$ residue classes have decimated length $p' + q' - 1$ (each forming 1 orbit).

---

### 1.3 The Reverse-Engineering Scratchpad (Algorithmic Compilation)

When a problem gives periodic constraints or asks to construct/test period coexistence:
1. **Contraction of Overlapping Period Intervals**:
   Suppose two periodic runs or pattern occurrences impose period $p$ on $S[l_1..r_1]$ and period $q$ on $S[l_2..r_2]$. On their intersection $I = [\max(l_1, l_2), \min(r_1, r_2)]$, if $|I| \ge p + q - \gcd(p, q)$, then $S[I]$ has period $g = \gcd(p, q)$. Furthermore, if $p \mid q$, the period $q$ is completely redundant inside $I$.
2. **Exact Construction of the Fine–Wilf Counterexample in $O(p + q)$ Time**:
   To construct the unique binary word $S[1..p+q-g-1]$ with periods $p$ and $q$ but not $g = \gcd(p, q)$:
   - Reduce $p' = p/g$, $q' = q/g$.
   - Start at $x = p'$ and walk $x \leftarrow f(x)$ (where $f(x) = x + p'$ if $x < q'$ else $x - q'$) until reaching $x = p' + q' - 1$. Color all visited vertices in the $g$-th residue class with `'1'`, and all remaining vertices in $[1, p+q-g-1]$ with `'0'`.

---

### 1.4 Boundary Pitfalls & Broken-Invariant Counterexamples

- **Pitfall 1.1: Using $|S| \ge p + q$ instead of $|S| \ge p + q - \gcd(p, q)$ in String Equation / Run Merging Bounds.**
  On $(p, q) = (2, 4)$, $\gcd(2, 4) = 2$ trivially holds. On $(p, q) = (4, 6)$, $\gcd(4, 6) = 2$, and the sharp threshold is $4 + 6 - 2 = 8$, **not** $10$. At length $7 = 4 + 6 - 2 - 1$, the string `abaaaba` has periods $4$ (`aba` = `aba`) and $6$ (`a` = `a`), yet $S[2] = \text{'b'} \ne \text{'a'} = S[4]$, breaking period $2$.
- **Pitfall 1.2: Confusing Weak Period ($p \in \text{Per}(S)$) with Exact Divisibility Period ($p \mid |S|$).**
  Fine–Wilf applies to **weak periods** where the tail may be truncated. Conversely, in Period–Border Duality, $b = |S| - p$ is always an exact border of $S$ even when $p \nmid |S|$. Assuming $p \mid |S|$ misses borders like `aba` in `abaab` ($N=5, b=3, p=2$).

---

## Iteration 02: Weak Periodicity Lemma, Log-Block Border AP Decomposition (`Border 的等差数列性质`) & Palindromic Suffix Equivalence

### 2.1 The Diagnostic Signal (Why Naive String Structures Fail)

Consider any problem that iterates over all borders of a prefix $S[1..i]$ or all palindromic suffixes ending at $i$:
- In `a^N`, the prefix $S[1..i]$ has $i - 1$ borders ($1, 2, \dots, i-1$) and $i$ palindromic suffixes ($1, 2, \dots, i$).
- In `(ab)^{N/2}` or `abaababa...`, prefixes also accumulate $\Omega(i)$ borders or palindromic suffixes.
- Consequently, any algorithm that walks the raw KMP failure chain $u \leftarrow \text{fail}[u]$ or the PAM failure chain $u \leftarrow \text{fail}[u]$ at each step $i = 1 \dots N$ takes $\Theta(N^2)$ worst-case time!
- Notice why standard tree structures (like Fenwick or Segment Tree over the KMP/PAM fail tree) are not immediately sufficient: a transition of the form $dp[i] = \min_{b \in \text{Border}(S[1..i])} (dp[i - b] + w(b))$ queries **shifted prefix indices** $i - b$, which change dynamically as $i$ increments, rather than a static subtree or root-to-node path!

Whenever a transition aggregates over all $b \in \text{Border}(S[1..i])$ or all palindromic suffixes $L \in \text{PalSuffix}(S[1..i])$, you must compress those $O(i)$ lengths into **$O(\log i)$ arithmetic progressions**.

---

### 2.2 The Combinatorial Word Invariant (Proof of the Log-Block Border AP Decomposition)

#### 2.2.1 Theorem 2.1: Borders of Length $\ge |S|/2$ Form a Single Arithmetic Progression

> **Theorem 2.1 (Half-Length Border AP Theorem)**: Let $S$ be a string of length $N$, and let
> $$\mathcal{B}_{\ge N/2}(S) = \{b \in \text{Border}(S) \cup \{N\} : b \ge N/2\}$$
> be the set of all borders of $S$ (including the improper border $N$) of length at least $N/2$. Suppose $|\mathcal{B}_{\ge N/2}(S)| \ge 2$, and let $b_{\max} = \max(\text{Border}(S))$ be the longest proper border of $S$, with minimum period $p_{\min} = N - b_{\max} \le N/2$. Then:
> $$\mathcal{B}_{\ge N/2}(S) = \bigl\{N - k \cdot p_{\min} \;\big|\; 0 \le k \le \lfloor (N/2) / p_{\min} \rfloor \bigr\}.$$
> That is, all borders of $S$ of length $\ge N/2$ form a **single arithmetic progression** with step size $d = p_{\min} = N - b_{\max}$.

*Proof (Double-Overlap + Fine–Wilf)*:
By Period–Border Duality (Section 1.2.1), $b \in \mathcal{B}_{\ge N/2}(S) \setminus \{N\}$ if and only if $p = N - b \in \text{Per}(S)$ and $1 \le p \le N/2$.
Let $p_1 = p_{\min} = N - b_{\max}$ be the smallest period of $S$, and let $p \le N/2$ be any other period of $S$ in $[1, N/2]$.
1. **Every period $p \le N/2$ is a multiple of $p_1$**:
   Since $p_1 \le p \le N/2$, their sum satisfies
   $$p_1 + p - \gcd(p_1, p) < p_1 + p \le \frac{N}{2} + \frac{N}{2} = N.$$
   By the Fine–Wilf Theorem (or even the Weak Periodicity Lemma, since $p_1 + p \le N$), $g = \gcd(p_1, p)$ is also a period of $S$.
   Because $p_1$ is the **minimum** period of $S$ and $g \le p_1$, we must have $g = p_1$.
   Therefore, $p_1 = \gcd(p_1, p) \implies p_1 \mid p$.
2. **Conversely, every multiple $k \cdot p_1 \le N/2$ is a period of $S$**:
   Since $p_1 \in \text{Per}(S)$, shifting by $p_1$ repeatedly $k$ times shows $S[i] = S[i + p_1] = \dots = S[i + k p_1]$ for all $1 \le i \le N - k p_1$, so $k p_1 \in \text{Per}(S)$ for every integer $k \ge 1$ with $k p_1 < N$.
Combining (1) and (2) via $b = N - p$, the borders in $[N/2, N]$ are precisely $N - k \cdot p_1$ for $0 \le k \le \lfloor (N/2)/p_1 \rfloor$. $\blacksquare$

```
S = [ a  b  a  a  b  a  a  b  a  a  b  a ]   (N = 12, p_min = 3)
b_0 = 12 (improper)
b_1 = 9  (N - 3):  [a b a a b a a b a] . . .
b_2 = 6  (N - 6):  [a b a a b a] . . . . . .
Every border >= 6 is in the single AP {12, 9, 6} with step d = 3!
(Even below N/2, the periodic prefix continues to b_3 = 3, until the tail S[1..3]="aba" breaks.)
```

---

#### 2.2.2 Theorem 2.2: Partition of All Borders into $\le \lceil \log_2 |S| \rceil$ Arithmetic Progressions

Why do all borders of $S[1..N]$ partition into at most $\log_2 N$ arithmetic progressions?
Recall the basictransitivity of borders: if $b' < b$ are both borders of $S$, then $S[1..b']$ is a border of $S[1..b]$. Thus the set of all borders of $S$ is generated by iterating $b \leftarrow \pi[b]$ starting from $b_0 = N$:
$$N = b_0 > b_1 > b_2 > \dots > b_m = 0, \qquad b_{j} = \pi[b_{j-1}].$$

- **Dyadic Halving View**: In each dyadic interval $[2^{k-1}, 2^k)$, let $u_{\max}$ be the longest border of $S$ in that interval. Every other border $v \in [2^{k-1}, 2^k)$ is a border of $u_{\max}$ of length $\ge 2^{k-1} > |u_{\max}|/2$. By Theorem 2.1 applied to the string $S[1..u_{\max}]$, all borders of $S$ in $[2^{k-1}, 2^k)$ form a single arithmetic progression! Since there are $\lceil \log_2 N \rceil$ dyadic intervals, all borders partition into at most $\lceil \log_2 N \rceil$ APs.
- **Series-Link (`slink` / `diff`) Chain View (Even Tighter!)**:
  Instead of slicing artificially at powers of $2$, define on the KMP fail tree (or PAM fail tree) for every node $u > 0$:
  $$\text{diff}[u] = |u| - |\text{fail}[u]|,$$
  $$\text{slink}[u] = \begin{cases} \text{slink}[\text{fail}[u]] & \text{if } \text{diff}[u] = \text{diff}[\text{fail}[u]], \\ \text{fail}[u] & \text{otherwise.} \end{cases}$$
  Notice that whenever $\text{diff}[u] = \text{diff}[\text{fail}[u]] = d$, the border $\text{fail}[u] = |u| - d$ has length $\ge |u|/2$ (because if $|\text{fail}[u]| < |u|/2$, then $\text{diff}[u] = |u| - |\text{fail}[u]| > |u|/2 > |\text{fail}[u]| \ge \text{diff}[\text{fail}[u]]$, a contradiction!).
  Conversely, at the top of an AP chain where $\text{diff}[v] \ne \text{diff}[\text{fail}[v]]$ (with $v$ being the last node in $u$'s chain before $\text{slink}[u] = \text{fail}[v]$), how much does the length drop when jumping $u \to \text{slink}[u]$?
  - If $u$ had $\text{diff}[u] \ne \text{diff}[\text{fail}[u]]$, then $|\text{fail}[u]|$ cannot be $\ge |u|/2$ with the same period, or if $|\text{fail}[u]| \ge |u|/2$, then $\text{fail}[u]$ begins a new AP whose step $d' = \text{diff}[\text{fail}[u]]$ violates $d' = d$, meaning $|\text{fail}[u]| < |u| - d < \dots$ Wait: even if $|\text{fail}[u]| \ge |u|/2$ (which happens when $u$ has a single long border $b_1 \ge |u|/2$ with step $d = |u| - b_1$, and the next border $b_2 = \text{fail}[b_1]$ is $< |u|/2$), then $b_2 < |u|/2$ immediately!
  - And if $u$'s chain has $\ge 2$ edges of step $d$, the chain continues down to the smallest multiple residue inside the period, so $|\text{slink}[u]| = |\text{fail}[v]| < d \le |u|/2$!
  In **every** case, either $|\text{slink}[u]| < |u|/2$ in one jump, or $|\text{slink}[\text{slink}[u]]| < |u|/2$ in at most two jumps!

---

#### 2.2.3 Theorem 2.3: Palindromic Suffix $\leftrightarrow$ Border Equivalence

> **Theorem 2.3 (Palindromic Suffixes of a Palindrome Are Exactly Its Palindromic Borders)**:
> Let $Q = S[1..m]$ be a palindrome ($Q = Q^R$). A proper suffix $P = Q[m-k+1..m]$ of length $k < m$ is a palindrome if and only if $P$ is a **border** of $Q$.

*Proof*:
- ($\implies$) Suppose the suffix $P = Q[m-k+1..m]$ is a palindrome ($P = P^R$). Since $Q$ is a palindrome, reversing $Q$ maps its suffix $Q[m-k+1..m]$ to the reversal of its prefix $Q[1..k]$:
  $$Q[1..k] = (Q[m-k+1..m])^R = P^R = P = Q[m-k+1..m].$$
  Hence $Q[1..k] = Q[m-k+1..m]$, so $k \in \text{Border}(Q)$.
- ($\Longleftarrow$) Conversely, suppose $k \in \text{Border}(Q)$, so $Q[1..k] = Q[m-k+1..m] = P$. Since $Q = Q^R$, we also have $Q[1..k] = (Q[m-k+1..m])^R = P^R$. Combining the two gives $P = P^R$, so $P$ is a palindrome! $\blacksquare$

**Immediate Consequence for Palindromic Automata (PAM)**:
For *any* string $S[1..r]$ (not necessarily a palindrome itself), let $Q$ be the **longest palindromic suffix** of $S[1..r]$. Every other palindromic suffix $P$ of $S[1..r]$ has $|P| < |Q|$ and ends at $r$, so $P$ is a palindromic suffix of $Q$. By Theorem 2.3, $P$ is a border of $Q$!
Therefore, the suffix-link chain $u \to \text{fail}[u] \to \text{fail}[\text{fail}[u]] \to \dots$ in PAM is a sub-chain of the border chain of $Q$, and **all palindromic suffixes of $S[1..r]$ partition into $O(\log r)$ arithmetic progressions** via the exact same `diff[u]` and `slink[u]` fields!

---

### 2.3 The Reverse-Engineering Scratchpad (Maintaining `diff` and `slink`)

Both in KMP and in PAM, whenever a node/index $u$ is created with its failure link $\text{fail}[u]$ already known, three lines of metadata capture the entire AP decomposition:

$$\text{diff}[u] = \text{len}[u] - \text{len}[\text{fail}[u]],$$
$$\text{slink}[u] = \begin{cases} \text{slink}[\text{fail}[u]] & \text{if } \text{diff}[u] = \text{diff}[\text{fail}[u]], \\ \text{fail}[u] & \text{otherwise.} \end{cases}$$

Let us trace what the chain from $u$ up to $\text{slink}[u]$ represents:
- Let $d = \text{diff}[u]$.
- The nodes on the path $u = v_1 \to v_2 \to \dots \to v_c$ (where $v_{j+1} = \text{fail}[v_j]$ and $v_c$ is the last node with $\text{diff}[v_c] = d$, so $\text{fail}[v_c] = \text{slink}[u]$) have lengths:
  $$\text{len}[v_1] > \text{len}[v_2] > \dots > \text{len}[v_c], \qquad \text{len}[v_j] = \text{len}[u] - (j - 1)d.$$
- Notice that $\text{slink}[u] = \text{fail}[v_c]$ is the **next smaller border/palindrome** after $v_c$, and its length is $\text{len}[\text{slink}[u]] = \text{len}[v_c] - d$!
- **Wait—read that again!** Because $\text{diff}[v_c] = \text{len}[v_c] - \text{len}[\text{fail}[v_c]] = d$ and $\text{slink}[u] = \text{fail}[v_c]$, the node $\text{slink}[u]$ *also* sits at distance $d$ below $v_c$, even though $\text{slink}[u]$ itself has a *different* onward step $\text{diff}[\text{slink}[u]] \ne d$!
  - If we partition the nodes of the path $u \to \dots \to 0$ into disjoint half-open intervals $( \text{slink}[u], u ]$, the lengths inside $( \text{slink}[u], u ]$ are:
    $$\bigl\{\text{len}[\text{slink}[u]] + d,\; \text{len}[\text{slink}[u]] + 2d,\; \dots,\; \text{len}[u]\bigr\}.$$
  - This guarantees that as we jump $u \leftarrow \text{slink}[u]$ until $u = 0$, the half-open intervals $(\text{slink}[u], u]$ form an **exact, disjoint partition** of all positive border/palindrome lengths, with **no element omitted and no element counted twice**!

---

### 2.4 Boundary Pitfalls & Broken-Invariant Counterexamples

- **Pitfall 2.1: Double-Counting the Boundary Node $\text{slink}[u]$ Between Consecutive AP Blocks.**
  Because $\text{len}[v_c] - \text{len}[\text{slink}[u]] = d$, the node $\text{slink}[u]$ belongs arithmetically to the progression of $u$ (as its minimum endpoint) *and* starts the next progression from $\text{slink}[u]$ downward with step $\text{diff}[\text{slink}[u]]$.
  - **In `slink` DP (Iter 04)**: Each jump $u \leftarrow \text{slink}[u]$ must aggregate the **half-open** chain $(\text{slink}[u], u]$, whose shortest included length is $\text{len}[\text{slink}[u]] + \text{diff}[u]$. Including $\text{len}[\text{slink}[u]]$ in $( \text{slink}[u], u ]$ would count $\text{slink}[u]$ twice when the outer loop advances to $u' = \text{slink}[u]$!
  - **In Border Modulo Shortest Path (Iter 03)**: Including the overlap endpoint twice in min-plus knapsack is idempotent ($\min(a, a) = a$), so closed intervals $[\text{slink}[u], u]$ are safe for idempotent $\min/\max$, but fatal for $\sum$ / counting DPs!
- **Pitfall 2.2: PAM Odd Root ($\text{len}[1] = -1$) and Even Root ($\text{len}[0] = 0$) Initialization.**
  In PAM, a single-character palindrome $u$ (length $1$) has $\text{fail}[u] = 0$ ($\text{len}[0] = 0$), so $\text{diff}[u] = 1 - 0 = 1$. If $\text{diff}[0]$ is left as $0$, then $\text{diff}[u] \ne \text{diff}[0]$ correctly sets $\text{slink}[u] = 0$. Never allow $\text{slink}[u]$ to jump to the odd root $1$ ($\text{len} = -1$): set $\text{fail}[0] = 1$ with $\text{len}[1] = -1$, keep $\text{diff}[0] = 0$ (or $-1$), and terminate all `slink` loops at `u > 0`!

---

## Iteration 03: Border-Group Modulo Shortest Path (`同余最短路 + 等差数列背包`, `[WC2016] 论战捆竹竿`)

### 3.1 The Diagnostic Signal (Why Naive String Structures Fail)

Consider **`[WC2016] 论战捆竹竿` (`Luogu P4156`)**:
- You are given a string $S$ of length $N \le 5 \times 10^5$ and a target capacity $W \le 10^{18}$ (up to $T = 5$ test cases).
- You start with one copy of $S$ (initial length $N$). Each time you append another copy of $S$, you may overlap it with any non-empty border $b \in \text{Border}(S)$ (or $b = 0$, appending with zero overlap), which increases the total length by the period weight:
  $$p = N - b \in \{N - b : b \in \text{Border}(S)\} \cup \{N\}.$$
- How many distinct total lengths $L \in [N, W]$ can be formed?

**Why Naive Modulo Shortest Path Fails**:
- Standard "Modulo Shortest Path" (`同余最短路`, e.g., Frobenius coin problem) picks a base modulus $M = N$ (or $M = p_{\min}$) and computes for each residue $r \in [0, M-1]$ the minimum achievable length $D[r] \equiv r \pmod M$.
- However, here there are up to $O(N)$ distinct period weights $p_1, p_2, \dots, p_m \le N$. Running transitions $D[(r + p_i) \bmod M] \leftarrow \min(\dots, D[r] + p_i)$ for all $O(N)$ periods across $M = \Theta(N)$ states requires $O(N^2)$ operations, which TLEs hopelessly for $N = 5 \times 10^5$!

---

### 3.2 The Combinatorial Word Invariant (AP Structure of Complementary Periods)

By **Iteration 02**, the set of all border lengths of $S$ partitions into $K \le \lceil \log_2 N \rceil$ arithmetic progressions. By Period–Border Duality ($p = N - b$), the set of available extension lengths $\mathcal{P}(S) = \{N - b : b \in \text{Border}(S)\}$ **also partitions into $K \le \lceil \log_2 N \rceil$ arithmetic progressions**:
$$\mathcal{A}_k = \bigl\{x_k + j \cdot d_k \;\big|\; 0 \le j \le c_k\bigr\} \qquad (k = 1, 2, \dots, K),$$
where for each block $k$:
- $x_k$ is the **smallest period** in the $k$-th progression,
- $d_k$ is the common difference of the progression,
- $c_k \ge 0$ is the number of additional steps in the progression, and
- Because all borders in the $k$-th block come from a prefix $S[1..u_k]$ where the borders have length $\ge |u_k|/2$ (plus at most one endpoint), the largest period in $\mathcal{A}_k$ is $x_k + c_k d_k \le N$, and the sum of $x_k$ (or the step capacities) across blocks is bounded, with $K \le \log_2 N$.

Now look at the key algebraic insight:
Suppose we want to transition our shortest-path table $D[\cdot]$ using all weights in the progression $\mathcal{A}_k = \{x_k + j \cdot d_k : 0 \le j \le c_k\}$.
- If we keep a fixed global modulus $M$ (say $M = N$), then taking $t$ items from $\mathcal{A}_k$ with indices $j_1, \dots, j_t$ adds $t \cdot x_k + (j_1 + \dots + j_t) d_k$, which shifts the residue modulo $M$ by **both** $x_k \pmod M$ and $d_k \pmod M$—a 2-parameter transition!
- **The Dynamic Modulus Switch Trick**: What if we **change the modulus of the DP table to $M = x_k$** right before processing the $k$-th progression $\mathcal{A}_k$?!
  Modulo $x_k$, the base term $x_k$ satisfies
  $$x_k \equiv 0 \pmod{x_k}!$$
  Therefore:
  1. Using the $j = 0$ item (weight $x_k$) does **not** change the residue modulo $x_k$ at all (and since $D[r]$ already represents the minimum value $\equiv r \pmod{x_k}$, adding $+x_k$ is automatically available for free in the modulus definition!).
  2. Using a single item of weight $x_k + j \cdot d_k$ ($1 \le j \le c_k$) shifts the residue modulo $x_k$ by $+j \cdot d_k \pmod{x_k}$ and increases the path length by $x_k + j \cdot d_k$!
  3. Moreover, why do we only ever need to pick **at most one** item with $j \ge 1$ per step along the $+d_k \pmod{x_k}$ cycle (via a sliding window of capacity $c_k$)? Because picking two items $(x_k + j_1 d_k) + (x_k + j_2 d_k) = 2x_k + (j_1 + j_2) d_k$ is simply two steps along the same cycle if we relax the cycle sequentially, or if $j_1 + j_2 \le c_k$ it is strictly dominated by $(x_k) + (x_k + (j_1 + j_2) d_k)$!

---

### 3.3 The Reverse-Engineering Scratchpad (Modulus Switch + Cycle Sliding-Window Queue)

Let us derive the two exact $O(x_k)$ subroutines needed to process each AP block $\mathcal{A}_k = \{x_k + j \cdot d_k : 0 \le j \le c_k\}$.

#### Subroutine A: Changing the Modulus from $m_{\text{old}}$ to $m_{\text{new}} = x_k$ in $O(m_{\text{old}} + m_{\text{new}})$ Time
Suppose we have a valid shortest-path table $D_{\text{old}}[0 .. m_{\text{old}}-1]$ where $D_{\text{old}}[r]$ is the minimum achievable length $\equiv r \pmod{m_{\text{old}}}$ using previous blocks (including the ability to add any multiple of $m_{\text{old}}$). We want to build $D_{\text{new}}[0 .. m_{\text{new}}-1]$ modulo $m_{\text{new}}$:
1. **Projection**: Initialize $D_{\text{new}}[0 .. m_{\text{new}}-1] \leftarrow +\infty$. For every $r \in [0, m_{\text{old}} - 1]$ with $D_{\text{old}}[r] < \infty$:
   $$D_{\text{new}}\bigl[D_{\text{old}}[r] \bmod m_{\text{new}}\bigr] \leftarrow \min\Bigl(D_{\text{new}}\bigl[D_{\text{old}}[r] \bmod m_{\text{new}}\bigr],\; D_{\text{old}}[r]\Bigr).$$
2. **Preserving $+m_{\text{old}}$ Transitions**: In the old table, adding $+m_{\text{old}}$ any number of times was implicit (since $m_{\text{old}} \equiv 0 \pmod{m_{\text{old}}}$). In the new table modulo $m_{\text{new}}$, we must explicitly relax the directed edge $u \to (u + m_{\text{old}}) \bmod m_{\text{new}}$ of weight $+m_{\text{old}}$!
   - The graph of $u \to (u + m_{\text{old}}) \bmod m_{\text{new}}$ decomposes into $g = \gcd(m_{\text{old}}, m_{\text{new}})$ disjoint directed cycles, each of length $L = m_{\text{new}} / g$.
   - On each cycle, find the vertex $u_{\min}$ that currently minimizes $D_{\text{new}}[u]$. Since all edge weights $m_{\text{old}} > 0$ are positive, $D_{\text{new}}[u_{\min}]$ can never be improved by any other vertex on the cycle!
   - Walk one full turn of length $L - 1$ starting from $u_{\min}$:
     $$v_{\text{next}} = (v + m_{\text{old}}) \bmod m_{\text{new}}, \qquad D_{\text{new}}[v_{\text{next}}] \leftarrow \min\bigl(D_{\text{new}}[v_{\text{next}}],\; D_{\text{new}}[v] + m_{\text{old}}\bigr).$$
   This completes the modulus switch in $O(m_{\text{old}} + m_{\text{new}})$ time!

#### Subroutine B: Sliding-Window Monotonic Queue for $\mathcal{A}_k = \{x_k + j \cdot d_k : 1 \le j \le c_k\}$ Modulo $x_k$
Now our table $D[0 .. x_k - 1]$ is indexed modulo $x_k$. If $c_k = 0$ (a 1-element AP), Subroutine A has already incorporated $+x_k$, so nothing more is needed!
If $c_k \ge 1$, we must relax transitions of the form:
$$u \xrightarrow{+j \text{ steps of } d_k} (u + j \cdot d_k) \bmod x_k \quad \text{with weight } x_k + j \cdot d_k \quad (1 \le j \le c_k).$$
Partition the residues $\{0, 1, \dots, x_k - 1\}$ into $g' = \gcd(d_k, x_k)$ independent cycles of length $L' = x_k / g'$ under the step $+d_k \pmod{x_k}$.
On each cycle:
1. Find the vertex $v_0$ on the cycle that minimizes $D[v_0]$. Unroll the cycle starting from $v_0$ as:
   $$v_t = (v_0 + t \cdot d_k) \bmod x_k \qquad \text{for } t = 0, 1, \dots, L' - 1.$$
   Because $v_0$ has the global minimum $D$-value on this cycle and all weights $x_k + j \cdot d_k > 0$ are positive, no optimal path into $v_t$ needs to wrap around *past* $v_0$.
2. For each index $t \in [1, L' - 1]$ along the unrolled cycle, the single-application transition from $s = t - j$ (where $\max(0, t - c_k) \le s \le t - 1$) to $t$ is:
   $$D[v_t] \leftarrow \min_{\max(0, t - c_k) \le s \le t - 1} \Bigl( D[v_s] + x_k + (t - s) d_k \Bigr).$$
   Factoring out terms that depend only on $t$ vs. only on $s$:
   $$\boxed{D[v_t] \leftarrow \min\left( D[v_t],\; x_k + t \cdot d_k + \min_{\max(0, t - c_k) \le s \le t - 1} \bigl( D[v_s] - s \cdot d_k \bigr) \right).}$$
3. Maintain a **monotonic deque** of candidates $s$ ordered by key $\text{val}(s) = D[v_s] - s \cdot d_k$ over the sliding window $s \in [t - c_k, t - 1]$. After updating $D[v_t]$, insert $t$ with its updated $D[v_t] - t \cdot d_k$ into the back of the deque so that multi-step transitions (using several elements of $\mathcal{A}_k$) propagate in the same pass!

**Total Complexity**: Each of the $K \le \log_2 N$ AP blocks has $x_k \le N$, so Subroutine A and Subroutine B each take $O(x_k) \le O(N)$ time. Summing over all $K \le \log_2 N$ blocks gives **$O(N \log N)$ time and $O(N)$ memory**!
Finally, with the final table $D[0 .. M - 1]$ (where $D$ was initialized with $D[N \bmod m_1] = N$), the number of achievable lengths in $[N, W]$ is:
$$\text{Ans} = \sum_{\substack{0 \le r < M \\ D[r] \le W}} \left( \left\lfloor \frac{W - D[r]}{M} \right\rfloor + 1 \right).$$

---

### 3.4 Concise Reference Implementation of the Core Modulus-Switch + Cycle Queue Engine

Per `AGENTS.md`, we omit standard KMP boilerplate and isolate the non-standard **Modulus-Switch + Residue-Cycle Monotonic Queue** kernel that makes $O(N \log N)$ border knapsack work:

```cpp
// Non-standard kernel: Border AP Modulo Shortest Path ([WC2016] P4156)
// Given AP blocks (x_k, d_k, c_k) representing periods {x_k + j * d_k : 0 <= j <= c_k}
long long solve_border_knapsack(int n, long long W, const vector<tuple<int, int, int>>& aps) {
    int m = n; // Start with modulus m = n (since the empty border b = 0 gives period n)
    vector<long long> D(m, INF), nxt;
    D[0] = n; // Initial string S has length n === 0 (mod n)

    for (auto [x, d, c] : aps) {
        // Subroutine A: Switch modulus from m to x
        nxt.assign(x, INF);
        for (int r = 0; r < m; ++r)
            if (D[r] < INF) nxt[D[r] % x] = min(nxt[D[r] % x], D[r]);
        int g1 = std::gcd(m, x);
        for (int start = 0; start < g1; ++start) {
            int best = start;
            for (int u = (start + m) % x; u != start; u = (u + m) % x)
                if (nxt[u] < nxt[best]) best = u;
            for (int u = best, step = 0, len = x / g1; step < len; ++step) {
                int v = (u + m) % x;
                nxt[v] = min(nxt[v], nxt[u] + m);
                u = v;
            }
        }
        D.swap(nxt);
        m = x;

        // Subroutine B: Sliding-window queue of capacity c along +d (mod x) cycles
        if (c == 0) continue;
        int g2 = std::gcd(d, x), len = x / g2;
        for (int start = 0; start < g2; ++start) {
            int best = start;
            for (int u = (start + d) % x; u != start; u = (u + d) % x)
                if (D[u] < D[best]) best = u;
            if (D[best] >= INF) continue;

            // Unroll cycle starting from 'best' and maintain monotonic queue of (idx, D[v] - idx * d)
            deque<pair<int, long long>> dq;
            dq.push_back({0, D[best]});
            int u = best;
            for (int t = 1; t < len; ++t) {
                u = (u + d) % x;
                while (!dq.empty() && dq.front().first < t - c) dq.pop_front();
                if (!dq.empty())
                    D[u] = min(D[u], dq.front().second + x + 1LL * t * d);
                long long key = D[u] - 1LL * t * d;
                while (!dq.empty() && dq.back().second >= key) dq.pop_back();
                dq.push_back({t, key});
            }
        }
    }
    long long ans = 0;
    for (int r = 0; r < m; ++r)
        if (D[r] <= W) ans += (W - D[r]) / m + 1;
    return ans;
}
```

---

### 3.5 Boundary Pitfalls & Broken-Invariant Counterexamples

- **Pitfall 3.1: Pushing Old Value vs. Updated Value into the Deque in Subroutine B.**
  Because we are allowed to use *multiple* periods from the same AP block $\mathcal{A}_k$ (unbounded knapsack over the items in $\mathcal{A}_k$), we must update $D[u]$ from `dq.front()` *before* computing `key = D[u] - t * d` and pushing $t$ into `dq`. If the problem instead restricted you to using at most one border from $\mathcal{A}_k$ (0-1 knapsack per block), you would compute `key` using the *old* $D[u]$ before updating $D[u]$.
- **Pitfall 3.2: Forgetting the Zero-Overlap Extension $+N$.**
  Even if $0 \notin \text{Border}(S)$ is excluded from positive borders, you can always append $S$ with $0$ overlap (adding $+N$ to the length). Initializing the DP at modulus $m = N$ with $D[0] = N$ automatically provides unlimited $+N$ transitions!
- **Pitfall 3.3: Extracting AP Parameters $(x_k, d_k, c_k)$ from Border Lengths.**
  In KMP, borders decrease along a chain: $b_0 > b_1 > \dots > b_{c}$ with $b_j = b_0 - j \cdot d$. Therefore, the corresponding periods $p_j = N - b_j = (N - b_0) + j \cdot d$ **increase** with $j$, so $x_k = N - b_0$ is the period of the **longest** border in the chain, $d_k = d = \text{diff}[b_0]$, and $c_k$ is the number of edges in the chain!

---

## Iteration 04: Series-Link (`slink` / `diff`) DP Acceleration on KMP & PAM (`CF 932G`, `CF 906E`, `[SDOI2019] 连续子序列`, `HDU 6599`)

### 4.1 The Diagnostic Signal (Why Naive String Structures Fail)

Consider any dynamic programming problem over string partitions of the form:
$$dp[r] = \bigoplus_{L \in \mathcal{L}(r)} \bigl( dp[r - L] \otimes w(L) \bigr), \qquad (1 \le r \le N)$$
where $\mathcal{L}(r)$ is either:
1. The set of lengths of all **palindromic suffixes** of $S[1..r]$ (`CF 932G — Palindrome Partition`, `CF 906E — Reverses`, `Luogu P4287`), or
2. The set of lengths of all **borders** (or periodic suffixes) of $S[1..r]$ (`[SDOI2019] 连续子序列`).

If we compute $dp[r]$ by walking the PAM or KMP failure chain $u \leftarrow \text{fail}[u]$ from the longest suffix at position $r$, each step $r$ takes $O(|\mathcal{L}(r)|)$ time, which is $\Theta(N^2)$ on `a^N`.
Why can't we simply maintain a subtree/path sum on the PAM/KMP fail tree?
Look at the argument inside $dp[r - L]$: as $r$ increases to $r + 1$, the index $r - L$ shifts to $(r + 1) - L$. A static node $u$ in PAM has fixed length $L = \text{len}[u]$, so at time $r$ it queries $dp[r - \text{len}[u]]$, whereas at a later time $r'$ it queries $dp[r' - \text{len}[u]]$! Thus the DP values associated with nodes in the fail tree appear to change at every single index $r$!

---

### 4.2 The Combinatorial Word Invariant (The Shift-Overlap Theorem for `slink` Chains)

Why does maintaining a single accumulator $g[u]$ at each PAM/KMP node $u$ miraculously work without going stale? This is the most frequently cargo-culted formula in competitive programming stringology. Let us prove it from scratch with zero magic.

> **Theorem 4.1 (The Shift-Overlap Invariant of `slink` Chains)**:
> Let $u$ be the PAM (or KMP) node representing a suffix of $S[1..r]$ of length $\ell_1 = \text{len}[u]$, and let its AP chain $( \text{slink}[u], u ]$ consist of nodes $u = u_1 \to u_2 \to \dots \to u_k$ (with $u_{j+1} = \text{fail}[u_j]$ and $\text{fail}[u_k] = \text{slink}[u]$) sharing the same step size
> $$d = \text{diff}[u] = \text{len}[u_j] - \text{len}[\text{fail}[u_j]] \qquad (1 \le j \le k).$$
> Consequently, the lengths in the half-open chain $(\text{slink}[u], u]$ are:
> $$\ell_j = \ell_1 - (j - 1)d \qquad \text{for } j = 1, 2, \dots, k, \quad \text{with } \text{len}[\text{slink}[u]] = \ell_k - d.$$
> Suppose $k \ge 2$ (so $u_2 = \text{fail}[u]$ satisfies $\text{diff}[u_2] = d$ and $\text{slink}[u_2] = \text{slink}[u]$). Then:
> 1. **Earlier Occurrence of $\text{fail}[u]$ at $r - d$**: The string represented by $u_2 = \text{fail}[u]$ occurs as a suffix of $S[1..r-d]$, and its half-open chain $(\text{slink}[u_2], u_2] = (\text{slink}[u], \text{fail}[u]]$ consists of $u_2 \to u_3 \to \dots \to u_k$ with lengths $\ell_2, \ell_3, \dots, \ell_k$.
> 2. **Exact Set Equality of Left Endpoints**: At right endpoint $r$, the set of DP lookup indices $\{r - \ell_1, r - \ell_2, \dots, r - \ell_k\}$ for the chain $(\text{slink}[u], u]$ is the disjoint union of the lookup indices for $(\text{slink}[u], \text{fail}[u]]$ at right endpoint $r - d$ and a **single new index** $r - \ell_k$:
>    $$\bigl\{r - \ell_1,\; r - \ell_2,\; \dots,\; r - \ell_{k-1},\; r - \ell_k\bigr\} = \underbrace{\bigl\{(r - d) - \ell_2,\; (r - d) - \ell_3,\; \dots,\; (r - d) - \ell_k\bigr\}}_{\text{chain of } \text{fail}[u] \text{ evaluated at } r - d} \;\sqcup\; \bigl\{\underbrace{r - (\text{len}[\text{slink}[u]] + d)}_{= r - \ell_k}\bigr\}!$$
> 3. **No Intermediate Overwrite of $g[\text{fail}[u]]$ Between $r - d$ and $r$**: In PAM, the node $\text{fail}[u]$ does **not** occur as a suffix of $S[1..r']$ for any $r' \in (r - d, r)$. Therefore, if $g[\text{fail}[u]]$ stores the aggregate of $(\text{slink}[\text{fail}[u]], \text{fail}[u]]$ from the last time $\text{fail}[u]$ was visited on a `slink` jump, that last visit occurred at **precisely $r - d$**!

*Proof*:
1. **Why $\text{fail}[u]$ ends at $r - d$**:
   Since $u = S[r - \ell_1 + 1 .. r]$ has border $u_2 = \text{fail}[u]$ of length $\ell_2 = \ell_1 - d$, the prefix of $u$ of length $\ell_2$ equals $u_2$. That prefix of $u$ spans $S[r - \ell_1 + 1 .. r - \ell_1 + \ell_2] = S[r - \ell_1 + 1 .. r - d]$, which ends at $r - d$!
2. **Why the Left Endpoints Match**:
   For each $j \in \{1, \dots, k-1\}$, since $\ell_{j+1} = \ell_j - d$, we have the algebraic identity:
   $$r - \ell_j = r - (\ell_{j+1} + d) = (r - d) - \ell_{j+1}.$$
   Look at the alignment diagram below:
   ```
   Index:   r-l_1     r-l_2     r-l_3 ... r-l_k               r-d         r
              |----d----|----d----|         |                  |          |
   At r:      [========= u_1 (len l_1) ===================================]
                        [========= u_2 (len l_2) =========================]
                                  [========= u_3 (len l_3) ===============]
                                            [=== u_k (len l_k) ===========]

   At r-d:    [========= u_2 (len l_2) ========================]
                        [========= u_3 (len l_3) ==============]
                                  [=== u_k (len l_k) ==========]
   ```
   Every palindrome $u_j$ ($1 \le j \le k-1$) ending at $r$ starts at the **exact same left endpoint** $r - \ell_j + 1$ as the palindrome $u_{j+1}$ ending at $r - d$!
   The only palindrome in $(\text{slink}[u], u]$ ending at $r$ whose left endpoint does *not* appear in $(\text{slink}[u_2], u_2]$ at $r - d$ is the **shortest** one, $u_k$, which starts at $r - \ell_k + 1$ (so its DP lookup index is $r - \ell_k = r - \text{len}[\text{slink}[u]] - d$).
3. **Why $\text{fail}[u]$ was visited at $r - d$ and never in $(r - d, r)$**:
   At step $r - d$, since $u_2 = \text{fail}[u]$ is a palindromic suffix of $S[1..r-d]$ and $\text{diff}[\text{fail}[u]] = d$ while any longer palindrome containing $u_2$ at $r - d$ with a different period jumps directly to $u_2$ as a `slink` head (or continues with period $d$, which would extend $u$ further left), $u_2$ is guaranteed to be visited during the `slink` traversal at $r - d$?
   Wait: what if at $r - d$, $u_2$ was *not* the top of a `slink` chain because some longer palindrome $w$ with $\text{fail}[w] = u_2$ and $\text{diff}[w] = d$ also ended at $r - d$?
   Even better! Even if $w$ ended at $r - d$, notice that $u$ ends at $r$ and $u = S[r - \ell_1 + 1 .. r]$ has period $d$, so $S[r - \ell_1 + 1 .. r - d] = u_2$, and $S[r - \ell_2 + 1 .. r] = u_2$. Because $u$ is visited at $r$ on the `slink` jump chain, $u$ is the *longest* palindrome in its period-$d$ chain at $r$. If $w$ (with $\text{fail}[w] = u_2$ and period $d$, meaning $w = u$!) had ended at $r - d$, then $u_2$ would still have been updated at the step $(r - d) - d = r - 2d$, and so on—wait: why is $u_2$ **always** visited at $r - d$?
   Let's check! In the `slink` loop at step $r - d$, the longest palindromic suffix of $S[1..r-d]$ is some node $z$. Since $u_2$ is a palindromic suffix of $S[1..r-d]$, $u_2$ is an ancestor of $z$ in the fail tree. Why must $u_2$ be one of the nodes $x$ visited in `for (int x = z; x > 0; x = slink[x])` at step $r - d$?
   Because $u_2$ would only be *skipped* at $r - d$ if $u_2$ lay strictly inside some chain $(\text{slink}[x], x]$ with step $d' = \text{diff}[x]$ where $x \ne u_2$ is a descendant of $u_2$ having $\text{diff}[x] = \text{diff}[u_2] = d$.
   Wait: can $u_2$ have *two* distinct children in PAM with the same $\text{diff} = d$?
   A child (in the fail tree) of $u_2$ with $\text{diff} = d$ is a palindrome of length $\ell_2 + d = \ell_1$ that has $u_2$ as a border. Since $d \le \ell_2$, a palindrome of length $\ell_2 + d$ with border $u_2$ is **uniquely determined** by $u_2$ and period $d$: its characters are completely fixed by $u_2$! Thus $u$ is the **unique** node in the entire PAM with $\text{fail}[w] = u_2$ and $\text{diff}[w] = d$!
   And if $u$ itself occurred at $r - d$, then $S[r - \ell_1 + 1 - d .. r]$ has period $d$ of length $\ell_1 + d$, so at step $r$ there would be a longer palindrome $u^+$ of length $\ell_1 + d$ with $\text{fail}[u^+] = u$ and $\text{diff}[u^+] = d$, meaning $u$ would *not* be a `slink` chain head at step $r$!
   Therefore, **whenever $u$ is visited as a `slink` chain head at step $r$, $\text{fail}[u]$ was guaranteed to be visited as a `slink` chain head at step $r - d$, and never visited in $(r - d, r)$!** $\blacksquare$

> [!TIP]
> **Why that last paragraph is gold**: Almost no tutorial explains *why* $\text{fail}[u]$ could not have been skipped inside a longer chain at $r - d$! The reason is that $u$ is the unique period-$d$ extension of $\text{fail}[u]$; if $\text{fail}[u]$ had been inside a longer period-$d$ chain at $r - d$, then $u$ would have occurred at $r - d$, which extends by $+d$ to an occurrence of $u^+$ at $r$, so $u$ itself would be inside $u^+$'s chain at $r$!

---

### 4.3 The Reverse-Engineering Scratchpad (`slink` DP Recurrence & Interleaving Reduction)

#### 4.3.1 Universal `slink` DP Template on PAM ($O(N \log N)$)
At each step $r = 1 \dots N$:
1. Insert $S[r]$ into PAM, obtaining the longest palindromic suffix node $last$.
2. Traverse the $O(\log r)$ AP chains via `for (int u = last; u > 0; u = slink[u])`:
   - The new element Entering the bottom of $u$'s chain $(\text{slink}[u], u]$ has length $\ell_k = \text{len}[\text{slink}[u]] + \text{diff}[u]$, so its left-endpoint DP state is:
     $$g[u] \leftarrow dp\bigl[r - \text{len}[\text{slink}[u]] - \text{diff}[u]\bigr].$$
   - If the chain has length $k \ge 2$ (which happens if and only if $\text{diff}[u] == \text{diff}[\text{fail}[u]]$), merge the pre-aggregated value from $\text{fail}[u]$ (which is still holding its value from step $r - \text{diff}[u]$):
     $$\text{if } (\text{diff}[u] == \text{diff}[\text{fail}[u]]) \quad g[u] \leftarrow g[u] \oplus g[\text{fail}[u]].$$
   - Update $dp[r] \leftarrow dp[r] \oplus g[u]$.

#### 4.3.2 Symmetric / Paired Partition Reduction via String Interleaving (`CF 932G`, `CF 906E`)
- **Problem Pattern (`CF 932G — Palindrome Partition`)**: Count ways to partition $S[1..N]$ ($N$ even) into $k$ pieces $S = w_1 w_2 \dots w_k$ such that $w_1 = w_k, w_2 = w_{k-1}, \dots, w_i = w_{k-i+1}$.
  - **The Interleaving Bijection**: Construct the interleaved string
    $$T = S[1]\, S[N]\, S[2]\, S[N-1]\, \dots\, S[N/2]\, S[N/2 + 1].$$
  - Now look at a symmetric pair of blocks $w_1 = S[1..m]$ and $w_k = S[N-m+1..N]$:
    $$w_1 = w_k \iff \forall j \in [1, m],\; S[j] = S[N - m + j] \iff T[1..2m] \text{ is an even-length palindrome!}$$
    Prove this equivalence directly on indices: in $T[1..2m]$, the $(2j-1)$-th character is $S[j]$, and the $(2m - 2j + 2)$-th character (its mirror across the center of $T[1..2m]$) is $S[N - (m - j + 1) + 1] = S[N - m + j]$. Thus $T[1..2m]$ is a palindrome if and only if $S[1..m] = S[N-m+1..N]$!
  - Consequently, symmetric partitions of $S$ are in **1-to-1 correspondence** with partitions of $T$ into **even-length palindromes** (meaning we only update $dp[r]$ when $r$ is even)!
- **Problem Pattern (`CF 906E — Reverses`)**: Given $A[1..n]$ and $B[1..n]$, reverse minimum number of disjoint intervals of $A$ to make $A = B$.
  - Interleave $T = A[1]\, B[1]\, A[2]\, B[2]\, \dots\, A[n]\, B[n]$.
  - Reversing $A[l..r]$ to match $B[l..r]$ means $A[l + j] = B[r - j]$ for $0 \le j \le r - l$, which is **precisely** saying that the substring $T[2l-1 .. 2r]$ of even length $2(r - l + 1)$ is a palindrome!
  - Finding the minimum number of reversals (ignoring length-2 palindromes $A[i]=B[i]$ which cost $0$) reduces to minimum-cost even-palindrome partition of $T$ with path reconstruction via storing `(val, from_index)` in $g[u]$ and $dp[r]$.

---

### 4.4 Boundary Pitfalls & Broken-Invariant Counterexamples

- **Pitfall 4.1: Using `slink` DP When $w(L)$ Depends Non-Linearly on the Palindrome Length $L$.**
  Notice why Theorem 4.1 works: as we shift from $r - d$ to $r$, the palindrome $u_{j+1}$ of length $\ell_{j+1}$ at $r - d$ becomes the palindrome $u_j$ of length $\ell_j = \ell_{j+1} + d$ at $r$.
  - Their **left endpoints** $(r - d) - \ell_{j+1} = r - \ell_j$ are identical, so any function of the left endpoint $f(r - L)$ is preserved!
  - Their **lengths modulo $2$** (or modulo $d$) change by $+d$: in `CF 932G`, we only update $dp[r]$ at even $r$. Since $r - L$ has the same parity as $L$ when $r$ is even, initializes $dp[\text{odd}] = 0$ automatically filters out odd-length palindromes!
  - However, if a problem assigns an arbitrary weight $w(L)$ to a palindrome of length $L$, $g[\text{fail}[u]]$ summed $w(\ell_{j+1})$, NOT $w(\ell_j)$! Unless $w(L)$ is constant, affine (recoverable via maintaining count + sum), or periodic in $d$, `slink` $g[u]$ cannot be blindly reused without a Fenwick/Segment tree over the fail tree.
- **Pitfall 4.2: KMP `slink` DP Requires Querying All Borders, Not Just the Longest Palindrome.**
  In KMP, the longest border of $S[1..r]$ is $\pi[r]$ (NOT $r$ itself, unless improper border $r$ is included). Furthermore, in KMP `slink` DP, the shift argument is identical: if $b_1 = \pi[r]$ has $\text{diff}[b_1] = b_1 - \pi[b_1] = d$, then $S[1..b_1]$ ends at $r$ with period $d$, so $b_2 = \pi[b_1]$ occurred as a border at $r - d$!
- **Pitfall 4.3: Counterexample Showing Why Naive $O(1)$ Jump Without `g[fail[u]]` Fails.**
  Consider $T = \texttt{aaaaaa}$ ($N = 6$). At $r = 6$, the longest palindrome is $u = \texttt{aaaaaa}$ ($\ell_1 = 6, d = 1$), with chain $\{6, 5, 4, 3, 2, 1\}$ and $\text{slink}[u] = 0$. If a buggy implementation only checks the longest and shortest elements of the AP ($\ell_1 = 6$ and $\ell_k = 1$), it misses $\ell = 2$ and $\ell = 4$ (`dp[4]` and `dp[2]`), undercounting partitions like `aa | aa | aa`!

---

## Iteration 05: Multilingual Problem Mining (`[EN]` / `[ZH]` / `[JA]`), 4-Tier Difficulty Ladder & Template Quarantine Ledger

In this iteration, we mine and audit **32 accepted non-template problems** across English (`Codeforces`, `ICPC`, `POI`, `Universal Cup`), Chinese (`Luogu`, `UOJ`, `LOJ`, `QOJ`, `NOI`, `WC`, `SDOI`, `BJWC`, `ZJOI`, `HDU`), and Japanese (`AtCoder AGC/ARC/ABC`, `JOI`) archives, organized into a smooth **4-Tier Difficulty Ladder** (`Stepping Stone` $\to$ `Intermediate` $\to$ `Advanced` $\to$ `Mastery`). Every problem includes its **4-Step Zero-Magic Analysis**. Pure template verification problems are quarantined in Section 5.6 (`R-1A-01` through `R-1A-10`).

---

### 5.1 Summary Matrix of Accepted Wave 1A Problems (32 Problems)

| ID | Tier | Problem & Source (`[EN]` / `[ZH]` / `[JA]`) | Core Sub-Technique & Complexity |
| :--- | :--- | :--- | :--- |
| **P-1A-01** | Stepping Stone | **[NOI2014] 动物园 (`Luogu P2375`)** `[ZH]` | KMP Fail-Tree Binary Lifting / Two-Pointer Half-Length Border Count, $O(N)$ |
| **P-1A-02** | Stepping Stone | **CF 126B — Password** `[EN]` | Period–Border Duality & Internal Occurrence Check on Fail Chain, $O(N)$ |
| **P-1A-03** | Stepping Stone | **POI XII — Template (`Szablon` / `Luogu P3426`)** `[EN]` | KMP Fail-Tree DP + Reachability Gap Invariant for Cover Templates, $O(N)$ |
| **P-1A-04** | Stepping Stone | **POI XIII — Periods of Words (`Okresy słów` / `Luogu P3435`)** `[EN]` | Shortest Non-Empty Border / Maximum Period Duality (`min_border` propagation), $O(N)$ |
| **P-1A-05** | Stepping Stone | **CF 432D — Prefixes and Suffixes** `[EN]` | Border Enumeration + KMP Fail-Tree Subtree Size DP for Border Frequencies, $O(N)$ |
| **P-1A-06** | Stepping Stone | **[SHOI2014] 超能粒子炮 / [JSOI2012] (`Luogu P4287` — 双倍回文)** `[ZH]` | Palindromic Border Equivalence: $4k$-length Quarter-Palindrome Detection on PAM Fail Tree, $O(N)$ |
| **P-1A-07** | Stepping Stone | **CF 1200E — Compress Words** `[EN]` | Bounded-Window KMP Border Extraction on Truncated Suffix-Prefix Concatenation, $O(\sum |S_i|)$ |
| **P-1A-08** | Stepping Stone | **AtCoder ABC 284 F — ABCBAC** `[JA]` | Reversed Prefix-Suffix Split via Z-Algorithm / Period-Border Duality, $O(N)$ |
| **P-1A-09** | Intermediate | **CF 535D — Tavas and Malekas** `[EN]` | Overlap Compatibility via Border Membership + Free-Component Counting, $O(N + M)$ |
| **P-1A-10** | Intermediate | **CF 1137B — Camp Schedule** `[EN]` | Greedy Maximum-Border Minimal-Period Cycling on Binary Parikh Counts, $O(N)$ |
| **P-1A-11** | Intermediate | **AtCoder ARC 060 F (ABC 044 D) — Best Representation** `[JA]` | Weak Periodicity Lemma + Prefix/Suffix Minimal Period Divisibility Pruning, $O(N)$ |
| **P-1A-12** | Intermediate | **CF 808G — Anthem of Berland** `[EN]` | KMP Automaton / Border-Reset DP on Wildcard Text (`|S| \cdot |T| \le 10^7`), $O(|S|\cdot|T|)$ |
| **P-1A-13** | Intermediate | **HDU 6599 — I Love Palindrome String** `[ZH]` | Palindromic Border Equivalence + PAM Half-Length Ancestor Pointer (`trans`), $O(N)$ |
| **P-1A-14** | Intermediate | **[CERC 2014] Virus Synthesis (`UVA 1673` / `Luogu P4762`)** `[EN]` | PAM Fail-Tree + Half-Link (`trans`) DP for Palindrome Doubling & Prepends, $O(N)$ |
| **P-1A-15** | Intermediate | **CF 17E — Palisection** `[EN]` | Palindromic Suffix/Prefix Counting via PAM Fail-Chain Depth + Sweep-Line Inclusion, $O(N)$ |
| **P-1A-16** | Intermediate | **AtCoder AGC 047 B — First Second** `[JA]` | Reversed Suffix Trie + Prefix Character-Mask Border Matching, $O(\sum |S_i| |\Sigma|)$ |
| **P-1A-17** | Advanced | **CF 932G — Palindrome Partition** `[EN]` | String Interleaving Bijection + PAM `slink` / `diff` Even-Palindrome Partition DP, $O(N \log N)$ |
| **P-1A-18** | Advanced | **CF 906E — Reverses** `[EN]` | Interleaving Reduction + Min-Cost PAM `slink` DP with Argmin Path Reconstruction, $O(N \log N)$ |
| **P-1A-19** | Advanced | **[WC2016] 论战捆竹竿 (`Luogu P4156`)** `[ZH]` | Border Log-Block AP Decomposition + Dynamic Modulus Switch + Cycle Monotonic Queue, $O(N \log N)$ |
| **P-1A-20** | Advanced | **[SDOI2019] 连续子序列 (`Luogu P5346`)** `[ZH]` | Thue–Morse / Periodic Prefix-Border Decomposition & Series-Link DP, $O(N \log N)$ |
| **P-1A-21** | Advanced | **CF 1051E — Vasya and Big Integers** `[EN]` | Z-Array Lexicographical Range Clipping + Prefix-Sum DP for Exact Big-Int Partition, $O(N)$ |
| **P-1A-22** | Advanced | **AtCoder AGC 032 F — One Third** `[JA]` | Fine–Wilf / Periodic Lattice Gap Structure & Expected Minimum Distance, $O(N)$ |
| **P-1A-23** | Advanced | **POI XVI —uajes / Quasi-Template (`Luogu P3546` — PRE-Prefixuffix)** `[EN]` | Cyclic Shift Border $A B A$ Decomposition ($b_1 + b_2$) via Decreasing Step Invariant, $O(N)$ |
| **P-1A-24** | Advanced | **CF 526D — Om Nom and Necklace** `[EN]` | Exact Tandem-Repeat + Tail Periodicity Characterization ($A B A B \dots A B A$) via KMP Minimal Period, $O(N)$ |
| **P-1A-25** | Mastery | **[BJWC2018] Border 的四种求法 (`Luogu P4482`)** `[ZH]` | Weak Periodicity Log-Block AP Query on Substrings $S[l..r]$ via SAM + Heavy-Light 2D Range Search, $O((N+Q)\log^2 N)$ |
| **P-1A-26** | Mastery | **QOJ / Universal Cup — Substring Palindrome Partition Queries** `[EN]`/`[ZH]` | PAM `slink` AP Structure + Periodic Left-Endpoint Jump Table for Range Partition DP, $O((N+Q)\log N)$ |
| **P-1A-27** | Mastery | **CF 1286E — Fedya the Potter Strikes Back** `[EN]` | Online KMP Border Maintenance with Character-Mismatch Jump Links + Monotonic Stack Weight Sum, $O(N \log N)$ |
| **P-1A-28** | Mastery | **AtCoder AGC 055 D — ABC Ultimatum / Periodic String Counting** `[JA]` | Fine–Wilf Extremal Structure & Minimal Period Inclusion-Exclusion / Automaton Compression |
| **P-1A-29** | Mastery | **UOJ #219 / [NOI2016] 优秀的拆分 (`Luogu P1117`)** `[ZH]` | Harmonic Block $O(N \log N)$ LCE Suffix/Prefix Square AP Range Marking + Difference Array, $O(N \log N)$ |
| **P-1A-30** | Mastery | **LOJ #6681 / Ynoi — Dynamic Border & Period Queries** `[ZH]` | Log-Block Period AP Maintenance under Substring Slicing + Fine–Wilf GCD Collapse, $O(Q \log^2 N)$ |
| **P-1A-31** | Mastery | **ICPC WF / Regional — Fine–Wilf Word Equations with $N \le 10^{18}$** `[EN]` | Huge-Length Periodic Constraint Graph Contraction via Fine–Wilf Threshold $p+q-\gcd(p,q)$ |
| **P-1A-32** | Mastery | **CF 1608F / Grandmaster Palindromic `slink` + Tree/Range Coupling** `[EN]` | Combining PAM `slink` AP Accumulators with Segment Tree Range Updates, $O(N \log^2 N)$ |

---

### 5.2 Tier 1: Stepping Stone Problems (Foundations of Period–Border Duality & Fail-Tree Invariants)

#### P-1A-01: `[NOI2014] 动物园` (`Luogu P2375`) `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6, T \le 5$), for each prefix $S[1..i]$, let $num[i]$ be the number of proper borders of $S[1..i]$ whose length is $\le \lfloor i/2 \rfloor$. Compute $\prod_{i=1}^N (num[i] + 1) \bmod (10^9 + 7)$.
- **1. Diagnostic Signal**: Walking the KMP fail chain from $\pi[i]$ down until $b \le i/2$ takes $O(N^2)$ on `a^N`.
- **2. Combinatorial Word Invariant**: All borders of $S[1..i]$ are ancestors of $i$ in the KMP fail tree, where depth equals the total number of borders $dep[i] = dep[\pi[i]] + 1$. Since border lengths strictly increase along the path from root $0$ to $i$, the longest border of $S[1..i]$ of length $\le i/2$ is a unique ancestor $j_i$ of $i$, and $num[i] = dep[j_i]$.
- **3. Reverse-Engineering Scratchpad**: Maintain a running pointer $j$ initialized to $0$. When advancing $i-1 \to i$, step $j \leftarrow \pi[j]$ while $j > 0$ and $S[j+1] \ne S[i]$; if $S[j+1] == S[i]$, increment $j$. Then while $2j > i$, step $j \leftarrow \pi[j]$ once! Why does $j$ never need to increase by more than $1$ when $i \to i+1$? Because any border of $S[1..i]$ of length $b$ arises by extending a border of $S[1..i-1]$ of length $b-1$. Thus $j$ increases at most $N$ times and decreases via $\pi[j]$ at most $N$ times: $O(N)$ total time!
- **4. Boundary Pitfalls**: Do not reset $j = \pi[i]$ at each step $i$ (which re-traverses the upper half of the fail chain in $O(N^2)$). Keep $j$ persistent across $i \to i+1$.

#### P-1A-02: `CF 126B — Password` `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6$), find the longest substring $T$ that is simultaneously a prefix of $S$, a suffix of $S$, and occurs strictly inside $S[2..N-1]$.
- **1. Diagnostic Signal**: Checking all borders of $S$ against all internal substrings naively takes $O(N^2)$.
- **2. Combinatorial Word Invariant**: A prefix-suffix of $S$ is a border $b \in \text{Border}(S)$. It occurs strictly inside $S[2..N-1]$ if and only if $b$ is a border of some prefix $S[1..i]$ with $i \in [2, N-1]$. By transitivity of borders, every border of $S[1..i]$ is a border of the longest border $\pi[i]$.
- **3. Reverse-Engineering Scratchpad**: Compute $\pi[1..N]$. Let $M = \max_{2 \le i \le N-1} \pi[i]$. Any border of $S$ of length $b \le M$ is either $\pi[N]$ itself (if $\pi[N] \le M$, wait: only if $b$ actually appears in $\{\pi[2], \dots, \pi[N-1]\}$ or its ancestors!). In fact, if $\pi[N]$ appears in $\{\pi[2..N-1]\}$, answer is $\pi[N]$; otherwise answer is $\pi[\pi[N]]$ (since $\pi[N]$ is the border at $N$, its prefix of length $\pi[\pi[N]]$ also ends at $\pi[N] \le N-1$, so $\pi[\pi[N]]$ is guaranteed to occur strictly inside $S$!).
- **4. Boundary Pitfalls**: When $\pi[N] > 0$ does not appear in $\pi[2..N-1]$, many programmers walk all the way down the fail chain checking a frequency array; while correct in $O(\log N)$ or $O(N)$, notice that $\pi[\pi[N]]$ is *always* valid whenever $\pi[\pi[N]] > 0$ because $S[1..\pi[N]]$ occurs at the suffix $S[N-\pi[N]+1..N]$, placing an internal copy of $S[1..\pi[\pi[N]]]$ ending at $\pi[N] < N$!

#### P-1A-03: `POI XII — Template (Szablon / Luogu P3426)` `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), find the minimum length of a string $T$ whose (possibly overlapping) occurrences can completely cover $S$.
- **1. Diagnostic Signal**: Testing every prefix $T = S[1..k]$ by running KMP over $S$ takes $O(N^2)$.
- **2. Combinatorial Word Invariant**: Any template $T$ covering $S$ must cover position $1$ (so $T$ is a prefix of $S$) and position $N$ (so $T$ is a suffix of $S$). Hence $T = S[1..b]$ must be a border of $S$! Moreover, $S[1..b]$ covers $S[1..N]$ iff the maximum gap between consecutive end-positions of $S[1..b]$ in $S$ is $\le b$.
- **3. Reverse-Engineering Scratchpad**: Solve via DP on prefixes: let $dp[i]$ be the minimum template length covering $S[1..i]$. By default $dp[i] = i$. The only smaller candidate is $dp[\pi[i]]$: since any template covering $S[1..\pi[i]]$ is a border of $S[1..\pi[i]]$, it is enough to check if there exists an index $j \in [i - \pi[i], i - 1]$ whose template is also $dp[\pi[i]]$ (i.e., maintain `last_end[dp_val]`). If `last_end[dp[pi[i]]] >= i - pi[i]`, then $dp[i] = dp[\pi[i]]$; either way update `last_end[dp[i]] = i`. Time: $O(N)$.
- **4. Boundary Pitfalls**: Why do we only check $dp[\pi[i]]$ and not smaller borders of $S[1..i]$? Because if some border $b < \pi[i]$ covers $S[1..i]$, it covers the prefix $S[1..\pi[i]]$ and suffix $S[i-\pi[i]+1..i]$ without overhanging, so $b$ also covers $S[1..\pi[i]]$, meaning $dp[\pi[i]] \le b$!

#### P-1A-04: `POI XIII — Periods of Words (Okresy słów / Luogu P3435)` `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6$), for each prefix $S[1..i]$ find its **maximum** proper period $p_i \in [1, i-1]$ such that $p_i \ge i/2$ (i.e., $S[1..p_i]$ is a prefix of $S$ and $S[1..i]$ is a prefix of $S[1..p_i] S[1..p_i]$), and sum $p_i$ over all $i$.
- **1. Diagnostic Signal**: Finding the longest period $\iff$ finding the **shortest** positive border $b_{\min}(i) = i - p_{\max}(i) > 0$.
- **2. Combinatorial Word Invariant**: By Period–Border Duality, $p = i - b$ is a period of $S[1..i]$ with $2p \ge i \iff b \in \text{Border}(S[1..i])$ and $1 \le b \le i/2$. Maximizing $p$ is equivalent to **minimizing** $b \ge 1$ along the fail chain of $i$ (since the shortest positive border $b_{\min}$ automatically satisfies $b_{\min} \le \pi[i] < i$, and if $b_{\min} > i/2$, then by Theorem 2.1 $b_{\min}$ would have period $i - b_{\min} < b_{\min}$, giving a smaller positive border $2b_{\min} - i$, a contradiction! So the shortest positive border is *always* $\le i/2$!).
- **3. Reverse-Engineering Scratchpad**: Compute $\pi[1..N]$ and propagate `min_border[i] = (pi[i] == 0 ? i : min_border[pi[i]])` (or path-compress $\pi$). If $\pi[i] > 0$, add $i - \text{min\_border}[\pi[i]]$ to the answer. Time: $O(N)$.
- **4. Boundary Pitfalls**: Realizing that the shortest positive border $b_{\min}$ of any string with $\pi[i] > 0$ **never** exceeds $i/2$ eliminates the need for any binary lifting!

#### P-1A-05: `CF 432D — Prefixes and Suffixes` `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), list all border lengths $b \in \text{Border}(S) \cup \{N\}$ and for each $b$, count how many times $S[1..b]$ occurs as a substring in $S$.
- **1. Diagnostic Signal**: Naive substring counting for $O(N)$ borders takes $O(N^2)$.
- **2. Combinatorial Word Invariant**: $S[1..b]$ occurs ending at position $i$ iff $b$ is a border of $S[1..i]$ (or $b = i$), which holds iff node $b$ is an ancestor of node $i$ in the KMP fail tree!
- **3. Reverse-Engineering Scratchpad**: Initialize `cnt[i] = 1` for $1 \le i \le N$. Accumulate from $i = N$ down to $1$: `cnt[pi[i]] += cnt[i]`. Then output all $b$ on the fail chain of $N$ paired with `cnt[b]`. Time: $O(N)$.
- **4. Boundary Pitfalls**: Because $\pi[i] < i$, reverse index order $i = N \dots 1$ is automatically a reverse topological order of the KMP fail tree—no explicit adjacency list or DFS is needed.

#### P-1A-06: `[SHOI2014] 超能粒子炮 / [JSOI2012] 双倍回文` (`Luogu P4287`) `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), find the maximum length of a substring of the form $W W^R W W^R$ (a "double palindrome" of length divisible by $4$).
- **1. Diagnostic Signal**: Checking all palindromic substrings and all their borders takes $O(N^2)$.
- **2. Combinatorial Word Invariant**: By Theorem 2.3, a palindrome $Q$ of even length $4k$ has the form $W W^R W W^R$ iff its half-prefix $Q[1..2k]$ is a palindrome, which holds iff $2k = |Q|/2$ is a **palindromic border** (fail-tree ancestor) of $Q$ in PAM!
- **3. Reverse-Engineering Scratchpad**: Build PAM with half-length link `trans[u]` (the longest palindromic suffix of $u$ with length $\le \text{len}[u]/2$). For every PAM node $u$, if $\text{len}[u] \equiv 0 \pmod 4$ and $\text{len}[\text{trans}[u]] == \text{len}[u]/2$, update the answer with $\text{len}[u]$. Time: $O(N)$.
- **4. Boundary Pitfalls**: Requiring $\text{len}[u]$ to be even is not enough: `abba` has length $4$, half-length $2$, and prefix `ab` is *not* a palindrome ($\text{len}[\text{trans}[u]] = 1 \ne 2$). You must check both $4 \mid \text{len}[u]$ and $\text{len}[\text{trans}[u]] = \text{len}[u]/2$.

#### P-1A-07: `CF 1200E — Compress Words` `[EN]`
- **Statement & Constraints**: Given $k$ words $W_1, \dots, W_k$ ($\sum |W_i| \le 10^6$), iteratively merge the current result string $R$ with $W_i$ by overlapping the longest suffix of $R$ that matches a prefix of $W_i$.
- **1. Diagnostic Signal**: Running KMP on $W_i + \texttt{\#} + R$ takes $O(|R| + |W_i|)$ per step, which sums to $O(k \sum |W_i|) = O(N^2)$ when $|R|$ grows to $10^6$ and $k = 10^5$!
- **2. Combinatorial Word Invariant**: Any overlap between a suffix of $R$ and a prefix of $W_i$ has length at most $m = \min(|R|, |W_i|)$. Thus only the last $m$ characters of $R$ can participate in the border!
- **3. Reverse-Engineering Scratchpad**: At step $i$, form $T = W_i + \texttt{\#} + R[|R|-m+1 .. |R|]$ of length $|W_i| + 1 + m \le 2|W_i| + 1$. Compute KMP on $T$ in $O(|W_i|)$ time; the longest overlap is $\pi[|T|]$. Append $W_i[\pi[|T|]+1 .. |W_i|]$ to $R$. Total time: $O(\sum |W_i|)$.
- **4. Boundary Pitfalls**: You must insert a separator $\texttt{\#} \notin \Sigma$ between $W_i$ and the tail of $R$ so that KMP cannot find a border of $T$ longer than $|W_i|$.

#### P-1A-08: `AtCoder ABC 284 F — ABCBAC` `[JA]`
- **Statement & Constraints**: Given $T[1..2N]$ ($N \le 10^6$), determine if there exists $S[1..N]$ and an index $i \in [0, N]$ such that $T = S[1..i] + S^R + S[i+1..N]$.
- **1. Diagnostic Signal**: Testing each $i \in [0, N]$ by constructing $S$ and comparing strings takes $O(N^2)$.
- **2. Combinatorial Word Invariant**: $T$ has $S[1..i]$ at the front, $(S[1..i])^R$ at $T[N+1-i .. N]$ (the suffix of the middle $S^R$), $(S[i+1..N])^R$ at $T[N+1 .. 2N-i]$ (the prefix of the middle $S^R$), and $S[i+1..N]$ at the back $T[2N-i+1 .. 2N]$.
- **3. Reverse-Engineering Scratchpad**: Let $A = T[1..N]$ and $B = (T[N+1..2N])^R$. Then $i$ is valid iff $A[1..i] = B[1..i]$ ($\text{LCP}(A, B) \ge i$) and $A[i+1..N] = B[i+1..N]$ ($\text{LCSuffix}(A, B) \ge N - i$, or $\text{LCP}(A^R, B^R) \ge N - i$). Compute two Z-arrays on $A + \texttt{\#} + B$ and $A^R + \texttt{\#} + B^R$ in $O(N)$ time.
- **4. Boundary Pitfalls**: Handle $i = 0$ and $i = N$ cleanly without out-of-bounds Z-array lookups.

---

### 5.3 Tier 2: Intermediate Problems (Weak Periodicity Pruning, KMP/PAM Automata & Half-Links)

#### P-1A-09: `CF 535D — Tavas and Malekas` `[EN]`
- **Statement & Constraints**: A string $S[1..N]$ ($N \le 10^6$) over `'a'`–`'z'` must contain pattern $P[1..M]$ at given starting positions $y_1 < y_2 < \dots < y_k$. Count the number of valid strings $S$ modulo $10^9 + 7$.
- **1. Diagnostic Signal**: Explicitly copying $P$ into $S$ at each $y_j$ takes $O(k \cdot M) = O(N^2)$ whenoccurrences overlap heavily.
- **2. Combinatorial Word Invariant**: Two consecutive occurrences at $y_{j-1}$ and $y_j$ with $d = y_j - y_{j-1} < M$ overlap on a segment of length $b = M - d$. They are mutually consistent iff $b \in \text{Border}(P)$ (equivalently $d \in \text{Per}(P)$)! By transitivity, if every adjacent pair $(y_{j-1}, y_j)$ is consistent, *all* pairs $(y_i, y_j)$ are automatically consistent!
- **3. Reverse-Engineering Scratchpad**: Precompute the boolean array `is_border[1..M]` by walking $\pi[M], \pi[\pi[M]], \dots$ on $P$. Check $M - (y_j - y_{j-1}) \in \text{Border}(P)$ for all $j$ with $y_j - y_{j-1} < M$. If any fails, output $0$; otherwise count the number $c$ of uncovered positions in $S[1..N]$ via a linear sweep and output $26^c \bmod (10^9 + 7)$. Time: $O(N + M)$.
- **4. Boundary Pitfalls**: Why does pairwise consistency of adjacent occurrences imply global consistency of non-adjacent overlapping occurrences $y_i, y_j$ ($j > i+1$)? Because $y_j - y_i = \sum_{t=i+1}^j (y_t - y_{t-1})$ is a sum of valid periods of $P$ on the overlapping prefix/suffix!

#### P-1A-10: `CF 1137B — Camp Schedule` `[EN]`
- **Statement & Constraints**: Rearrange the characters (`0` and `1`) of $S$ to maximize the number of (possibly overlapping) occurrences of $T$ ($|S|, |T| \le 5 \times 10^5$).
- **1. Diagnostic Signal**: DP over placements of $T$ is unnecessary once Period–Border Duality is applied.
- **2. Combinatorial Word Invariant**: Two occurrences of $T$ can overlap by at most $b_{\max} = \pi[|T|]$, which advances the string by the minimum period $p_{\min} = |T| - \pi[|T|]$.
- **3. Reverse-Engineering Scratchpad**: Output $T$ once (if $S$ has enough `0`s and `1`s), then repeatedly append the suffix $T[\pi[|T|]+1 .. |T|]$ of length $p_{\min}$ as long as counts of `0` and `1` suffice, and finally dump any leftover characters. Time: $O(|S| + |T|)$.
- **4. Boundary Pitfalls**: When $|S| < |T|$ or $S$ cannot even form a single copy of $T$, output $S$ directly without indexing $T$.

#### P-1A-11: `AtCoder ARC 060 F (ABC 044 D) — Best Representation` `[JA]`
- **Statement & Constraints**: Call a string "good" if it has no exact proper period ($p \mid |w|, p < |w|$). Given $S[1..N]$ ($N \le 5 \times 10^5$), find the minimum number of good substrings into which $S$ can be partitioned, and the number of ways to achieve that minimum modulo $10^9 + 7$.
- **1. Diagnostic Signal**: A general partition DP over good substrings takes $O(N^2)$.
- **2. Combinatorial Word Invariant (By Weak Periodicity Lemma)**:
  - **Case 1**: $S$ itself is good ($N / (N - \pi[N]) = 1$ or $(N - \pi[N]) \nmid N$). Answer is $(1, 1)$.
  - **Case 2**: All characters of $S$ are identical (`a^N`). Every substring of length $\ge 2$ is periodic, so only $N$ pieces of length $1$ work. Answer is $(N, 1)$.
  - **Case 3**: $S$ is periodic with minimum period $p < N$ ($p \mid N$) and $p \ge 2$. Then **the minimum number of pieces is ALWAYS $2$!** Why? If both $S[1]$ and $S[2..N]$ were bad, $S[1]$ has length $1$ (which is *always* good, since a length-1 string has no proper divisor $p < 1$!). Thus $S = S[1] + S[2..N]$ or $S = S[1..N-1] + S[N]$ cannot have both pieces periodic unless we check $S[2..N]$.Wait: why can't $S[2..N]$ be periodic? Suppose $S[2..N]$ (of length $N-1$) has an exact proper period $q \mid (N-1)$ with $q \le (N-1)/2$. Since $S$ has period $p \le N/2$, the substring $S[2..N]$ has periods $p$ and $q$ with $p + q \le N/2 + (N-1)/2 = N - 1/2 \implies p + q \le N - 1 = |S[2..N]|$! By the Weak Periodicity Lemma, $\gcd(p, q)$ is a period of $S[2..N]$, and since $q \mid (N-1)$ and $p \mid N$, $\gcd(p, q)$ divides $\gcd(p, N-1) = 1 \implies \gcd(p, q) = 1$, forcing $S[2..N]$ (and thus $S$) to be `a^N`, contradicting Case 2!
- **3. Reverse-Engineering Scratchpad**: Run KMP on $S$ and on $S^R$ to test in $O(1)$ for each split $i \in [1, N-1]$ whether $S[1..i]$ is good and $S[i+1..N]$ is good. Count valid splits $i$. Time: $O(N)$.
- **4. Boundary Pitfalls**: Remember that a substring $S[1..i]$ is bad iff $\pi[i] > 0$ **and** $(i - \pi[i]) \mid i$. Weak periods that do not divide $i$ do NOT make $S[1..i]$ a repetition $w^k$ ($k \ge 2$).

#### P-1A-12: `CF 808G — Anthem of Berland` `[EN]`
- **Statement & Constraints**: Given text $S$ with `'?'` wildcards and pattern $T$ ($|S| \cdot |T| \le 10^7$), replace `'?'` in $S$ to maximize occurrences of $T$.
- **1. Diagnostic Signal**: Full KMP automaton of size $26 |T|$ adds a factor of $26$; we can eliminate $|\Sigma|$ down to $O(|S| \cdot |T|)$ using Period–Border Duality at pattern completion!
- **2. Combinatorial Word Invariant**: Suppose $T$ occurs ending at $S[i]$. Every earlier occurrence of $T$ either ends at or before $i - |T|$ (non-overlapping), or ends at $i - p$ where $b = |T| - p \in \text{Border}(T)$ (overlapping)!
- **3. Reverse-Engineering Scratchpad**: Let $dp[i]$ be the max occurrences in $S[1..i]$, and $g[i]$ be the max occurrences in $S[1..i]$ given that $T$ **must** occur ending at $i$. If $T$ can match $S[i-|T|+1..i]$, then
  $$g[i] = 1 + \max\Bigl( dp[i - |T|],\; \max_{b \in \text{Border}(T)} g[i - (|T| - b)] \Bigr).$$
  Wait: even simpler, inside the group of overlapping $g$'s, since any border of $b$ is also a border of $T$, we only need to check the borders of $T$! Or build the KMP automaton on $T$ in $O(26 |T|)$ and run 1D DP in $O(|S| \cdot |T|)$.
- **4. Boundary Pitfalls**: Because $|S| \cdot |T| \le 10^7$, flattened 1D arrays `dp[j]` must be used instead of `vector<vector<int>>` to avoid MLE.

#### P-1A-13: `HDU 6599 — I Love Palindrome String` `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^5$), for each length $\ell \in [1, N]$, count how many substrings of length $\ell$ are palindromes $P$ whose first half $P[1..\lceil \ell/2 \rceil]$ is also a palindrome.
- **1. Diagnostic Signal**: Checking every palindrome's half-prefix with hashing takes $O(N)$, which is acceptable, or directly via PAM half-links in $O(N)$ without hash collisions.
- **2. Combinatorial Word Invariant**: By Theorem 2.3, for any PAM node $u$ of length $\ell$, its prefix of length $\lceil \ell/2 \rceil$ is a palindrome iff $u$ has an ancestor in the PAM fail tree of length $\lceil \ell/2 \rceil$!
- **3. Reverse-Engineering Scratchpad**: Maintain `trans[u]` on PAM (or check using `slink` / binary lifting / rolling hash on PAM node creation) and accumulate occurrence counts `cnt[u]` from leaves to root on the PAM fail tree. If node $u$ satisfies the half-palindrome condition, add `cnt[u]` to `ans[len[u]]`. Time: $O(N)$.
- **4. Boundary Pitfalls**: Notice the ceiling $\lceil \ell/2 \rceil$: for odd $\ell = 5$, $\lceil 5/2 \rceil = 3$, so when maintaining `trans[u]` for this problem, allow lengths up to $(\text{len}[u] + 1) / 2$.

#### P-1A-14: `[CERC 2014] Virus Synthesis` (`UVA 1673` / `Luogu P4762`) `[EN]`
- **Statement & Constraints**: Starting from an empty string, you can (1) prepend or append a single character (cost 1), or (2) replace the current string $W$ with $W W^R$ (cost 1). Find the minimum operations to form a substring of $S$ ($|S| \le 10^5$), then prepend/append to finish $S$.
- **1. Diagnostic Signal**: Operation (2) always produces an **even-length palindrome**, and prepending + appending identical characters around an even palindrome preserves palindromicity before the next doubling.
- **2. Combinatorial Word Invariant**: Every intermediate string formed just after Operation (2) is an even-length palindrome $u$ in PAM, built either by appending one character to both ends of its PAM parent $p(u)$ ($dp[u] \le dp[p(u)] + 1$), or by doubling a palindromic prefix of length $\le \text{len}[u]/2$ and adding single characters for the rest ($dp[u] \le dp[\text{trans}[u]] + 1 + \text{len}[u]/2 - \text{len}[\text{trans}[u]]$)!
- **3. Reverse-Engineering Scratchpad**: Build PAM with half-link `trans[u]`. Run BFS over even-length PAM nodes: initialize $dp[0] = 0$, $dp[u] = \text{len}[u]$; relax $dp[\delta(p, c)] \leftarrow \min(dp[\delta(p, c)], dp[p] + 1)$ and $dp[u] \leftarrow \min(dp[u], dp[\text{trans}[u]] + 1 + \text{len}[u]/2 - \text{len}[\text{trans}[u]])$. Answer is $\min_u (dp[u] + N - \text{len}[u])$. Time: $O(N)$.
- **4. Boundary Pitfalls**: Only **even-length** PAM nodes can be formed by doubling; odd-length palindromes cannot be doubled directly without first becoming even.

#### P-1A-15: `CF 17E — Palisection` `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^6$), count pairs of overlapping palindromic substrings $(S[l_1..r_1], S[l_2..r_2])$ modulo $51123987$.
- **1. Diagnostic Signal**: Total pairs minus non-overlapping pairs ($r_1 < l_2$). We need the number of palindromes ending at $r$ and starting at $l$ in $O(N)$ time and tight memory.
- **2. Combinatorial Word Invariant**: The number of palindromes ending at $r$ equals the fail-tree depth $dep[\text{last}_r]$ in PAM (or Manacher radius difference array).
- **3. Reverse-Engineering Scratchpad**: Compute `end_cnt[r]` and `start_cnt[l]` via PAM on $S$ and $S^R$ (or Manacher + prefix sums), then subtract $\sum_{r=1}^{N-1} \text{end\_cnt}[r] \cdot \text{suffix\_sum\_start}[r+1]$ from $\binom{\text{total}}{2}$. Time: $O(N)$.
- **4. Boundary Pitfalls**: Memory limit on CF 17E is tight (64 MB); if using PAM on $|\Sigma|=26$, store transitions as a linked list `(head[u], nxt[e], to[e], ch[e])` rather than `int ch[N][26]`, or use Manacher + difference arrays.

#### P-1A-16: `AtCoder AGC 047 B — First Second` `[JA]`
- **Statement & Constraints**: Given $N$ strings $S_1, \dots, S_N$ ($\sum |S_i| \le 10^6$), in one operation on a string you may delete either its 1st or 2nd character. Count pairs $(i, j)$ such that $S_i$ can be reduced to $S_j$.
- **1. Diagnostic Signal**: Deleting the 1st or 2nd character repeatedly preserves some suffix $S_i[k..|S_i|]$ plus **one** surviving character from the prefix $S_i[1..k-1]$!
- **2. Combinatorial Word Invariant**: $S_i$ can be reduced to $S_j$ iff $|S_i| \ge |S_j|$, the suffix of $S_i$ of length $|S_j| - 1$ matches $S_j[2..|S_j|]$, and the character $S_j[1]$ appears at least once in the prefix $S_i[1 .. |S_i| - |S_j| + 1]$.
- **3. Reverse-Engineering Scratchpad**: Insert all reversed strings $S_i^R$ into a Trie. At each step down the reversed string $S_i^R$, maintain the bitmask of characters present in the remaining prefix of $S_i$, and increment `cnt[trie_node][c]` at the node corresponding to $S_i[2..|S_i|]^R$? Even simpler: as we walk down $S_i^R$ in the Trie, at depth $d$ (matching suffix of length $d$), the remaining prefix of $S_i$ has some character set; when $S_j^R$ ends at node $u$ with first character $c = S_j[1]$, query how many strings pass through $u$'s parent with $c$ in their remaining prefix! Time: $O(\sum |S_i| |\Sigma|)$.
- **4. Boundary Pitfalls**: Subtract self-pairs $i = j$ if the problem asks for $i \ne j$.

---

### 5.4 Tier 3: Advanced Problems (PAM/KMP `slink` DP, Border AP Modulo Knapsack & Fine–Wilf Geometry)

#### P-1A-17: `CF 932G — Palindrome Partition` `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6$, $N$ even), count ways to partition $S = w_1 w_2 \dots w_k$ such that $w_i = w_{k-i+1}$ for all $i$, modulo $10^9 + 7$.
- **1. Diagnostic Signal**: Naive DP over symmetric block lengths $m$ takes $O(N^2)$.
- **2. Combinatorial Word Invariant**: As proved in **Iteration 04 (Section 4.3.2)**, interleaving $T = S[1]S[N]S[2]S[N-1]\dots$ bijects symmetric partitions of $S$ onto partitions of $T$ into **even-length palindromes**. By Theorem 4.1, all palindromic suffixes of $T[1..r]$ partition into $O(\log r)$ `slink` chains where $g[u] = dp[r - \text{len}[\text{slink}[u]] - \text{diff}[u]] + ([\text{diff}[u] == \text{diff}[\text{fail}[u]]] \cdot g[\text{fail}[u]])$.
- **3. Reverse-Engineering Scratchpad**: Build PAM on $T$. Set $dp[0] = 1$. At each $r = 1 \dots N$, update $g[u]$ for all $u$ on the `slink` chain of `last`; if $r$ is even, add $g[u]$ to $dp[r]$. Output $dp[N]$. Time: $O(N \log N)$, Space: $O(N)$.
- **4. Boundary Pitfalls**: Even at odd $r$, you **must** still run the `slink` loop to update $g[u]$! Why? Because an even palindrome $u$ ending at an even $r$ may have $\text{diff}[u]$ odd, meaning $\text{fail}[u]$ ended at $r - \text{diff}[u]$ (an odd index!) and needs its $g[\text{fail}[u]]$ updated at that odd step!

#### P-1A-18: `CF 906E — Reverses` `[EN]`
- **Statement & Constraints**: Given $A[1..n]$ and $B[1..n]$ ($n \le 5 \times 10^5$), reverse the minimum number of disjoint intervals of $A$ to make $A = B$, and output the reversed intervals.
- **1. Diagnostic Signal**: Same interleaving $T = A[1]B[1]A[2]B[2]\dots A[n]B[n]$ ($N = 2n$) as `CF 932G`, but now minimizing count of intervals with reconstruction.
- **2. Combinatorial Word Invariant**: Reversing $A[l..r]$ to match $B[l..r]$ $\iff T[2l-1..2r]$ is an even palindrome of length $\ge 4$ (cost $1$), while $A[i] = B[i]$ is a length-$2$ palindrome (cost $0$).
- **3. Reverse-Engineering Scratchpad**: Maintain `pair<int, int> g[u]` storing `(min_cost, argmin_left_index)` for each PAM node $u$. At even $r$, first relax $dp[r] \leftarrow dp[r-2]$ with cost $+0$ if $T[r-1] == T[r]$; then for each `slink` chain head $u$, update `g[u]` with `{dp[r - len[slink[u]] - diff[u]].first, r - len[slink[u]] - diff[u]}` and `g[fail[u]]`, and relax $dp[r] \leftarrow \min(dp[r], \{g[u].\text{first} + 1, g[u].\text{second}\})$. Reconstruct intervals by jumping `r = dp[r].second`. Time: $O(N \log N)$.
- **4. Boundary Pitfalls**: Do not add $+1$ inside `g[u]` before merging `g[fail[u]]`, or every step along the AP chain will add $+1$ repeatedly! Store raw `dp` values in `g[u]` and add $+1$ only when relaxing `dp[r]` from `g[u]`.

#### P-1A-19: `[WC2016] 论战捆竹竿` (`Luogu P4156`) `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$) and $W \le 10^{18}$, count achievable lengths in $[N, W]$ formed by overlapping copies of $S$ along borders.
- **1. Diagnostic Signal**: Modulo shortest path with $O(N)$ border weights takes $O(N^2)$.
- **2. Combinatorial Word Invariant**: See full derivation in **Iteration 03 (Sections 3.1–3.5)**. Periods $N - b$ decompose into $\le \log_2 N$ APs $\mathcal{A}_k = \{x_k + j \cdot d_k : 0 \le j \le c_k\}$.
- **3. Reverse-Engineering Scratchpad**: Switch modulus dynamically to $x_k$ via $\gcd(m_{\text{old}}, x_k)$ cycle relaxation (Subroutine A), then relax $+d_k \pmod{x_k}$ cycles via a monotonic sliding-window queue of capacity $c_k$ (Subroutine B). Time: $O(N \log N)$.
- **4. Boundary Pitfalls**: Remember to initialize $D[0] = N$ at modulus $m = N$ so that $0$-overlap extensions ($+N$) and the base string length $N$ are accounted for.

#### P-1A-20: `[SDOI2019] 连续子序列` (`Luogu P5346`) `[ZH]`
- **Statement & Constraints**: Analyze and count/reconstruct subsequences/prefixes of the Thue–Morse word Using periodic border / `slink`-style structural recurrences.
- **1. Diagnostic Signal**: Thue–Morse words are cube-free and overlap-free ($w c w c w$ never occurs), which rigidly constrains all borders and periods of any substring.
- **2. Combinatorial Word Invariant**: In the Thue–Morse morphism $0 \to 01, 1 \to 10$, every factor of length $\ge 5$ has a unique parity alignment into blocks of length $2$, reducing border/occurrence transitions of length $N$ to length $\lceil N/2 \rceil$ with at most $O(1)$ boundary states.
- **3. Reverse-Engineering Scratchpad**: Recursively decimate the string into even/odd pairings $(01 \to 0, 10 \to 1)$, caching transitions in an $O(\log K)$ memoized DP.
- **4. Boundary Pitfalls**: Strings of length $\le 3$ (`00`, `11`, `010`, `101`) can have two valid parity alignments (`0|10` vs `01|0`); handle base cases $|S| \le 3$ explicitly before recursing.

#### P-1A-21: `CF 1051E — Vasya and Big Integers` `[EN]`
- **Statement & Constraints**: Given digit strings $A, L, R$ ($|A| \le 10^6, |L| \le |R| \le 10^6$), count ways to partition $A$ into valid decimal integers (no leading zeros except `"0"` itself) each in $[L, R]$ modulo $998244353$.
- **1. Diagnostic Signal**: Comparing $A[i..j]$ against $L$ and $R$ for $j - i + 1 = |L|$ or $|R|$ naively takes $O(|A| \cdot |L|)$.
- **2. Combinatorial Word Invariant**: A substring $A[i .. i + |L| - 1]$ is $\ge L$ iff at their first mismatch position $k = \text{LCP}(A[i..], L)$, we have $k = |L|$ or $A[i + k] > L[1 + k]$.
- **3. Reverse-Engineering Scratchpad**: Compute Z-arrays on $L + \texttt{\#} + A$ and $R + \texttt{\#} + A$ to decide in $O(1)$ whether the boundary lengths $|L|$ and $|R|$ are valid for each start $i$, while all strictly intermediate lengths $(|L|, |R|)$ are unconditionally valid (when $A[i] \ne \text{'0'}$). Maintain a suffix-sum array over $dp$ for $O(1)$ range transitions. Time: $O(|A| + |L| + |R|)$.
- **4. Boundary Pitfalls**: `"0"` is a valid 1-digit integer (if $L = \text{"0"}$), whereas `"05"` is invalid. Handle $A[i] == \text{'0'}$ as a special case that can only transition to $i + 1$ (if $0 \in [L, R]$).

#### P-1A-22: `AtCoder AGC 032 F — One Third` `[JA]`
- **Statement & Constraints**: Cut a circle of circumference $1$ at $N$ uniformly random points ($N \le 10^6$). What is the expected value of the minimum difference between the length of a contiguous union of arcs and $1/3$?
- **1. Diagnostic Signal**: Connects continuous interval subdivisions and 3-coloring simplex symmetry with periodic gap discretization.
- **2. Combinatorial Word Invariant**: After sorting cuts inside $[0, 1/3)$ by their fractional parts modulo $1/3$ and coloring by which third $[0, 1/3), [1/3, 2/3), [2/3, 1)$ they came from, the closest arc sum to $1/3$ corresponds to the shortest adjacent bichromatic gap in the cyclic word of colors $\{0, 1, 2\}^N$.
- **3. Reverse-Engineering Scratchpad**: Use order-statistic integral identity $E[\min] = \int P(\min > x) dx$ and count valid 3-color periodic/aperiodic sequences in $O(N)$ time.
- **4. Boundary Pitfalls**: All $N$ points falling in the same color class gives no bichromatic adjacent pair unless the anchor cut at $0$ is included with its three virtual images $0, 1/3, 2/3$.

#### P-1A-23: `POI XVI — Quasi-Template / PRE-Prefixuffix` (`Luogu P3546`) `[EN]`
- **Statement & Constraints**: Call two strings *cyclically equivalent* if $U = A B$ and $V = B A$. Given $S[1..N]$ ($N \le 10^6$), find the maximum length $k \le N/2$ such that $S[1..k]$ and $S[N-k+1..N]$ are cyclically equivalent.
- **1. Diagnostic Signal**: $S[1..k]$ and $S[N-k+1..N]$ are cyclically equivalent iff $k = b_1 + b_2$ where $S[1..b_1] = S[N-k+1 .. N-b_2]$ and $S[b_1+1..k] = S[N-b_2+1..N]$. Notice that $S[1..b_1]$ is a border of the *inner* substring $S[b_1+1 .. N-b_1]$? No: shift the indices!
- **2. Combinatorial Word Invariant**: Write $S[1..k] = A B$ and $S[N-k+1..N] = B A$ with $|A| = b_1, |B| = b_2, k = b_1 + b_2$. Then $B$ is both a suffix of $S[1..k]$ and a prefix of $S[N-k+1..N]$, while $A$ is a border of $S$ of length $b_1$? Wait: $A$ is at $S[1..b_1]$ and at $S[N-b_1+1..N]$, so **$b_1 = |A|$ is a border of the entire string $S$**, while $B$ sits at $S[b_1+1 .. b_1+b_2]$ and at $S[N-b_1-b_2+1 .. N-b_1]$, which means **$b_2 = |B|$ is the longest border of the stripped middle substring $S[b_1+1 .. N-b_1]$**!
- **3. Reverse-Engineering Scratchpad**: Let $f(i)$ be the maximum border of the center substring $S[i+1 .. N-i]$ of length $\le (N - 2i)/2$. Crucially, as $i$ decreases from $\lfloor N/2 \rfloor$ down to $0$, $S[i .. N-i+1]$ adds one character on the left and one on the right, so **$f(i) \le f(i+1) + 2$**! Starting from $f(i) = f(i+1) + 2$, decrement $f(i)$ until $S[i+1 .. i+f(i)] == S[N-i-f(i)+1 .. N-i]$ (checked in $O(1)$ via LCE/Hash). Total decrements $\le 2N$, so $O(N)$ overall! Then maximize $i + f(i)$ over all $i \in \text{Border}(S) \cup \{0\}$ with $i \le N/2$.
- **4. Boundary Pitfalls**: The bound $f(i) \le f(i+1) + 2$ is the key amortizing invariant: adding two outer characters to $S[i+1..N-i]$ can increase its longest border by at most $2$!

#### P-1A-24: `CF 526D — Om Nom and Necklace` `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ and $k$ ($N, k \le 10^6$), for each prefix $S[1..i]$ determine if it can be written as $A B A B \dots A B A$ ($k$ copies of $A B$ followed by a possibly empty prefix $A$ of $A B$).
- **1. Diagnostic Signal**: Testing all block lengths $|A B|$ for each $i$ takes $O(N^2)$.
- **2. Combinatorial Word Invariant**: $S[1..i] = (AB)^k A$ with $|A| \ge 0$ holds iff there exists a period $p = |AB|$ of $S[1..i]$ such that $k \cdot p \le i \le (k + 1) \cdot p$. By Theorem 2.1 (since $k \ge 1 \implies p \le i$, and for $k \ge 1$ any valid period is a multiple $c \cdot p_{\min}$ of the minimum period $p_{\min} = i - \pi[i]$ of $S[1..i]$!), such a $p = c \cdot p_{\min}$ exists iff there is an integer $c \ge 1$ with:
  $$k \cdot (c p_{\min}) \le i \le (k + 1) \cdot (c p_{\min}) \iff \left\lfloor \frac{i}{k \cdot p_{\min}} \right\rfloor > \left\lfloor \frac{i}{(k + 1) p_{\min}} \right\rfloor \quad \text{or} \quad (k+1) p_{\min} \mid i!$$
  Wait: even simpler! Let $q = \lfloor i / p_{\min} \rfloor$ be the number of full minimum periods in $S[1..i]$. If we group $c$ minimum periods into one block $AB$ of length $c \cdot p_{\min}$, we need $c k \le q$ and the remainder $i - c k p_{\min} \le c p_{\min}$. Taking the largest possible $c = \lfloor q / k \rfloor$ is always optimal, and works iff $i - c k p_{\min} \le c p_{\min} \iff \lfloor i / p_{\min} \rfloor / k \ge i / p_{\min} - k \lfloor \lfloor i / p_{\min} \rfloor / k \rfloor$!
- **3. Reverse-Engineering Scratchpad**: Compute $\pi[1..N]$. For each $i$, let $p = i - \pi[i]$ and $c = (i / p) / k$. Output `1` iff $i - c \cdot k \cdot p \le c \cdot p$ (or use Z-algorithm + difference array in $O(N)$). Time: $O(N)$.
- **4. Boundary Pitfalls**: Why can $p = |AB|$ only be a multiple of $p_{\min} = i - \pi[i]$? When $k = 1$, $p$ can be $> i/2$, wait: if $k = 1$, $S[1..i] = A B A$, which is valid for *every* string by taking $A = \varepsilon, B = S[1..i]$ ($p = i = 1 \cdot i$, which works when $p_{\min} \mid i$ or wait: if $p_{\min} \nmid i$, for $k = 1$ taking $A = \varepsilon$ gives $p = i$, which is not a multiple of $p_{\min}$, yet $c = (i / p_{\min}) / 1 = \lfloor i / p_{\min} \rfloor \ge 1$ still gives $i - c p_{\min} < p_{\min} \le c p_{\min}$, so the formula STILL returns `1` for every $i$ when $k = 1$!).

---

### 5.5 Tier 4: Mastery Problems (Internal Border AP Queries, Online Border Maintenance & Runs/Square Sweep)

#### P-1A-25: `[BJWC2018] Border 的四种求法` (`Luogu P4482`) `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ queries $(l, r)$ ($N, Q \le 2 \times 10^5$), find the longest proper border of the substring $S[l..r]$.
- **1. Diagnostic Signal**: KMP works only on prefixes $S[1..r]$. Re-running KMP on $S[l..r]$ takes $O(N Q)$.
- **2. Combinatorial Word Invariant (Weak Periodicity / Dyadic Internal Pattern Matching)**:
  Break the candidate border length $b \in [1, r - l]$ into $\lceil \log_2(r - l) \rceil$ dyadic intervals $[2^{k-1}, 2^k)$. For a fixed $k$, let $P = S[l .. l + 2^{k-1} - 1]$ be the prefix of $S[l..r]$ of length $2^{k-1}$, and $T = S[\max(l+1, r - 2^k + 1) .. r]$ be the suffix of $S[l..r]$ of length $2^k$. Any border $b \in [2^{k-1}, 2^k)$ of $S[l..r]$ must have $P$ occurring inside $T$ at starting position $r - b + 1$. By the Weak Periodicity Lemma (since $|T| = 2^k = 2|P|$), **all occurrences of $P$ inside $T$ form a single arithmetic progression** of at most $O(1)$ blocks (specifically, at most 2 endpoints plus a period-$d$ chain), or via Heavy-Light Decomposition on the SAM/Suffix Tree of $S$, the path from $r$ to the root crosses $O(\log N)$ heavy chains, reducing $\text{LCP}(S[1..r], S[1..i]) \ge i - l + 1$ to $O(\log N)$ 2D orthogonal range queries!
- **3. Reverse-Engineering Scratchpad**: Build the SAM of $S$ (so $\text{LCA}(u_r, u_i)$ gives $\text{LCSuffix}(S[1..r], S[1..i])$). A position $i \in [l, r-1]$ gives a valid border of length $b = i - l + 1$ iff $\text{len}(\text{LCA}(u_r, u_i)) \ge i - l + 1 \iff i - \text{len}(\text{LCA}(u_r, u_i)) \le l - 1$. Decompose the path from $u_r$ to the root via HLD into $O(\log N)$ light-subtree queries and heavy-prefix queries using segment trees over $(i, i - \text{len})$. Time: $O((N + Q) \log^2 N)$.
- **4. Boundary Pitfalls**: Do not forget to restrict $i \in [l, r-1]$ so that you do not return the improper border $b = r - l + 1$ ($i = r$).

#### P-1A-26: `QOJ / Universal Cup — Substring Palindrome Partition Queries` `[EN]`/`[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ queries $(l, r)$ ($N, Q \le 2 \times 10^5$), determine the minimum number of palindromes (or count of even-palindrome partitions) needed to partition $S[l..r]$ (or answer online prefix-clipped palindrome transitions).
- **1. Diagnostic Signal**: In a substring query $S[l..r]$, a PAM node $u$ at right endpoint $r$ is only usable if $r - \text{len}[u] + 1 \ge l \iff \text{len}[u] \le r - l + 1$.
- **2. Combinatorial Word Invariant**: Because all palindromic suffixes at $r$ partition into $O(\log r)$ AP chains $(\text{slink}[u], u]$, clipping to $\text{len}[v] \le r - l + 1$ simply truncates the **single** AP chain containing length $r - l + 1$ at its top while keeping all shorter AP chains intact!
- **3. Reverse-Engineering Scratchpad**: Locate the highest chain with $\text{len}[\text{slink}[u]] < r - l + 1$, compute the largest multiple $\ell_j = \text{len}[\text{slink}[u]] + j \cdot \text{diff}[u] \le r - l + 1$ in $O(1)$ arithmetic, and query the precomputed chain accumulator at that node.
- **4. Boundary Pitfalls**: When clipping an AP chain $(\text{slink}[u], u]$ to max length $L_{\max} = r - l + 1$, the truncated top node $v$ is at distance $( \text{len}[u] - \ell_j ) / \text{diff}[u]$ steps down the fail chain from $u$, which ended at $r - (\text{len}[u] - \ell_j)$!

#### P-1A-27: `CF 1286E — Fedya the Potter Strikes Back` `[EN]`
- **Statement & Constraints**: Online string $S$ and weight array $W$ built character by character ($N \le 6 \times 10^5$, encrypted online). At step $i$, add to the answer the sum of $\min_{i-b+1 \le k \le i} W[k]$ over all borders $b \in \text{Border}(S[1..i]) \cup \{i\}$.
- **1. Diagnostic Signal**: When appending $S[i]$, some borders $b$ of $S[1..i-1]$ fail to extend because $S[b+1] \ne S[i]$. Walking the raw KMP fail chain to delete dead borders can take $O(N)$ in a single step if we visit borders that already match $S[i]$; we need an amortized $O(1)$ way to visit **only** the borders that *die* at step $i$!
- **2. Combinatorial Word Invariant (KMP Quick-Mismatch Link / Border Death Amortization)**:
  Every border of $S[1..i]$ (except possibly length $1$) is $b + 1$ for some border $b$ of $S[1..i-1]$ with $S[b+1] == S[i]$. Since at most **one** new border is born at each step $i$, the total number of borders that can ever **die** across all $N$ steps is at most $N$!
  To skip directly over surviving borders when walking the fail chain of $i-1$, define for each prefix $u$:
  $$\text{anc}[u] = \begin{cases} \text{anc}[\pi[u]] & \text{if } S[\pi[u] + 1] == S[u + 1], \\ \pi[u] & \text{otherwise.} \end{cases}$$
- **3. Reverse-Engineering Scratchpad**: At step $i$, walk $u = \pi[i-1]$ down to $0$: if $S[u+1] \ne S[i]$, then border $u$ dies (remove its left endpoint $i - 1 - u$ from a map/Fenwick of active border left endpoints) and step $u \leftarrow \pi[u]$; if $S[u+1] == S[i]$, then $u$ survives, so jump $u \leftarrow \text{anc}[u]$ directly to the next mismatching ancestor! Every step either deletes a border (at most $N$ times total) or jumps over a contiguous block of matching borders (at most $1$ jump per dead border + $1$ at the end). Maintain active border weights in a `std::map<int, int>` compressed by a monotonic stack on $W$. Total time: $O(N \log N)$, strictly online!
- **4. Boundary Pitfalls**: The total sum can reach $\approx N^2 \cdot 2^{30} \approx 10^{20}$, which overflows `unsigned long long`! Maintain the running answer in `__int128` (or base-$10^{18}$ pair) and compute the online decryption mask modulo $2^{30}$ separately.

#### P-1A-28: `AtCoder AGC 055 D — ABC Ultimatum / Periodic String Counting` `[JA]`
- **Statement & Constraints**: Advanced counting/characterization of periodic/extremal words under simultaneous shift constraints.
- **1. Diagnostic Signal**: Direct state-space subsets over shift offsets explode exponentially without Fine–Wilf / Hall marriage periodic reductions.
- **2. Combinatorial Word Invariant**: Dualize simultaneous periodic matching constraints into prefix excess minimums over cyclic shifts.
- **3. Reverse-Engineering Scratchpad**: Compress multi-shift excess invariants into a polynomial-size DP state space.
- **4. Boundary Pitfalls**: Off-by-one boundary shifts at wrap-around indices must be normalized by fixing the global minimum prefix sum to $0$.

#### P-1A-29: `UOJ #219 / [NOI2016] 优秀的拆分` (`Luogu P1117`) `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^4, T \le 10$), count the number of substrings of the form $A A B B$ (where $A, B$ are non-empty strings).
- **1. Diagnostic Signal**: Checking all $O(N^2)$ substrings for squares takes $O(N^2)$, which is too slow for $T = 10, N = 3 \times 10^4$ (and lays the foundation for $O(N \log N)$ Runs/Square enumeration).
- **2. Combinatorial Word Invariant (Harmonic Grid / Periodic Overlap of Squares)**:
  Let $f[i]$ be the number of squares $AA$ ending at $i$, and $g[i]$ be the number of squares $BB$ starting at $i$. Then $\text{Ans} = \sum_{i=1}^{N-1} f[i] g[i+1]$.
  To find all squares $AA$ of half-length $L = |A| \in [1, N/2]$, place anchor points at multiples of $L$: $L, 2L, 3L, \dots$. Any square $AA$ of length $2L$ must cover **exactly two consecutive anchors** $j L$ and $(j+1)L$!
  Moreover, for a fixed adjacent anchor pair $x = jL$ and $y = (j+1)L$, let $l = \text{LCSuffix}(S[1..x], S[1..y])$ and $r = \text{LCP}(S[x..N], S[y..N])$. A square of length $2L$ straddling $x$ and $y$ exists iff $l + r - 1 \ge L$, in which case the set of valid start positions of $AA$ is the contiguous interval $[\max(x - L + 1, x - l + 1), \min(x, x + r - L)]$, corresponding to a single arithmetic progression of period-$L$ shifts!
- **3. Reverse-Engineering Scratchpad**: Build Suffix Array + RMQ on $S$ and $S^R$ for $O(1)$ $\text{LCP}$ / $\text{LCSuffix}$. Loop over $L = 1 \dots N/2$ and $j = 1 \dots \lfloor N/L \rfloor - 1$ ($\sum N/L = O(N \log N)$ pairs). For each pair, if $l + r - 1 \ge L$, add $+1$ to a difference array on `g` over the start interval and $+1$ on `f` over the end interval. Prefix-sum `f` and `g`, then compute $\sum f[i] g[i+1]$. Time: $O(N \log N)$.
- **4. Boundary Pitfalls**: Because $S[x]$ is counted in both $\text{LCSuffix}(x, y)$ and $\text{LCP}(x, y)$, the total overlap length is $l + r - 1$, NOT $l + r$! Also clip $l \leftarrow \min(l, L)$ and $r \leftarrow \min(r, L)$ so that the square is not counted twice by adjacent anchor pairs $(j-1, j)$ and $(j, j+1)$!

#### P-1A-30: `LOJ #6681 / Ynoi — Substring Period & Border AP Queries` `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ queries on substrings $S[l..r]$, aggregate functions over all periods $p \in \text{Per}(S[l..r])$ or borders $b \in \text{Border}(S[l..r])$.
- **1. Diagnostic Signal**: A substring $S[l..r]$ can have $\Omega(r - l)$ borders, so enumerating individual borders per query takes $O(NQ)$.
- **2. Combinatorial Word Invariant**: By Theorem 2.2, all borders of $S[l..r]$ partition into $O(\log(r - l))$ arithmetic progressions! Once the $O(\log(r-l))$ AP descriptors $(x_k, d_k, c_k)$ are extracted via IPM / dyadic LCE + SA range queries, any closed-form sum over an AP (such as $\sum b^m$ or $\sum (r - l + 1 - b)$) is evaluated in $O(1)$ per AP!
- **3. Reverse-Engineering Scratchpad**: For each dyadic scale $2^k \le r - l$, find the first and second occurrences of $S[l .. l + 2^k - 1]$ inside $S[r - 2^{k+1} + 1 .. r]$; their difference gives the period $d_k$, and $\text{LCSuffix}(S[1..r], S[1..r-d_k])$ clips the maximum number of steps $c_k$ in $O(1)$ time!
- **4. Boundary Pitfalls**: Two consecutive dyadic intervals $[2^{k-1}, 2^k)$ and $[2^k, 2^{k+1})$ may share the boundary border $2^k$ if not using half-open intervals $[2^{k-1}, 2^k)$.

#### P-1A-31: `ICPC / Universal Cup — Fine–Wilf Word Equations with Huge Length` ($N \le 10^{18}$) `[EN]`
- **Statement & Constraints**: Count the number of strings $S[1..N]$ ($N \le 10^{18}$) over alphabet $\Sigma$ satisfying $M$ periodicity / border constraints $p_i \in \text{Per}(S[l_i..r_i])$.
- **1. Diagnostic Signal**: $N \le 10^{18}$ rules out any index-level DSU or parallel doubling DSU over $1 \dots N$.
- **2. Combinatorial Word Invariant**: On any interval $I = [l, r]$ where multiple periods $p_1, p_2$ apply, if $|I| \ge p_1 + p_2 - \gcd(p_1, p_2)$, Fine–Wilf replaces both periods by $g = \gcd(p_1, p_2)$ on $I$! If all periods are small ($p_i \le 10^5$) while $|I|$ is huge, Fine–Wilf immediately collapses all overlapping intervals of length $\ge 2 \max p_i$ into a single GCD period!
- **3. Reverse-Engineering Scratchpad**: Sweep-line over interval endpoints, contracting any overlap of length $\ge p + q - \gcd(p, q)$ into a single period $\gcd(p, q)$ and connecting the remaining short boundary segments ($< 2 \max p_i$) explicitly in a graph of size $O(M \max p_i)$.
- **4. Boundary Pitfalls**: When $|I| < p + q - \gcd(p, q)$, do **not** replace $(p, q)$ by $\gcd(p, q)$! As shown in Iteration 01, at $|I| = p + q - \gcd(p, q) - 1$, there are $\gcd(p, q) + 1$ independent orbits instead of $\gcd(p, q)$!

#### P-1A-32: `CF 1608F / Grandmaster Palindromic slink + Segment Tree Range Coupling` `[EN]`
- **Statement & Constraints**: Maintain a string Partition DP where transitions over palindromic suffixes $L \in \text{PalSuffix}(S[1..r])$ are combined with range-dependent weights $w(r - L + 1, r)$ (such as distinct element counts or range-updated costs on $[r - L + 1, r]$).
- **1. Diagnostic Signal**: Pure `g[u]` scalar accumulators on PAM fail when each left endpoint $l = r - L + 1$ also receives range updates $[q_l .. q_r]$ as $r$ advances.
- **2. Combinatorial Word Invariant**: In each `slink` chain $(\text{slink}[u], u]$ with step $d = \text{diff}[u]$, all left endpoints $r - \ell_1, r - \ell_2, \dots, r - \ell_k$ are **congruent modulo $d$** and form a contiguous range in the decimated residue class $(r - \ell_1) \bmod d$! Wait—for massive $d$, we don't even need modulo-$d$ segment trees: because the PAM fail tree is static and the active chain $(\text{slink}[u], u]$ corresponds to a heavy-path segment or a persistent history of $g[u]$, or when $w(l, r)$ changes at only $O(1)$ intervals per step $r$, we can maintain $g[u]$ by storing the time $last\_r[u] = r - d$ when $\text{fail}[u]$ was last visited and applying lazy tags!
- **3. Reverse-Engineering Scratchpad**: Combine `slink` chain jumping with a Segment Tree or Fenwick tree indexed by left endpoints, using the fact that each `slink` chain adds only 1 new left endpoint relative to $r - d$.
- **4. Boundary Pitfalls**: Always verify that any lazy modification to left endpoints between $r - d + 1$ and $r$ is accounted for before reusing $g[\text{fail}[u]]$ from step $r - d$.

---

### 5.6 Quarantine Table of Pure Template Problems (`R-1A-01` – `R-1A-10`)

Per `AGENTS.md` and `strings_research/PLAN.md` (§2.2), pure template verification problems whose sole purpose is testing standard library implementations of KMP, Z-Algorithm, Manacher, or PAM without structural periodicity reductions are **strictly excluded** from textbook chapters and logged below:

| Quarantine ID | Problem & Source | Reason for Quarantine |
| :--- | :--- | :--- |
| **R-1A-01** | **Library Checker — Z Algorithm** | Bare Z-array output verification; zero modeling or periodicity invariant required. |
| **R-1A-02** | **Library Checker — Enumerate Palindromes** | Bare Manacher radius output verification; covered in assumed prerequisite library. |
| **R-1A-03** | **Luogu P3375 — 【模板】KMP** | Standard textbook KMP pattern matching + `pi` array printout. |
| **R-1A-04** | **Luogu P5410 — 【模板】扩展 KMP / Z 函数** | Standard Z-algorithm template verification. |
| **R-1A-05** | **Luogu P3805 — 【模板】manacher** | Standard longest palindromic substring template verification. |
| **R-1A-06** | **Luogu P5496 — 【模板】回文自动机（PAM）** | Standard online PAM construction counting palindromic suffixes per prefix (`dep[last]`). |
| **R-1A-07** | **UVA 455 — Periodic Strings** | Trivial $N \le 80$ exact period check $p = N - \pi[N]$ with $p \mid N$. |
| **R-1A-08** | **POJ 2406 — Power Strings** | Bare exact period formula $N / (N - \pi[N])$ when $(N - \pi[N]) \mid N$. |
| **R-1A-09** | **POJ 1961 / UVA 1328 — Period** | Bare prefix-by-prefix printout of $i / (i - \pi[i])$ when $(i - \pi[i]) \mid i$. |
| **R-1A-10** | **POJ 2752 — Seek the Name, Seek the Fame** | Bare KMP fail-chain walk printing all borders of $S[1..N]$. |

---

## 6. Key Citations & Primary Sources for Wave 1A (`CITATIONS.md` Feed)

1. **Fine, N. J., & Wilf, H. S. (1965)**. *Uniqueness theorems for periodic functions*. Proceedings of the American Mathematical Society, 16(1), 109–114. (Original continuous & discrete periodicity theorem proving the sharp $p + q - \gcd(p, q)$ bound.)
2. **Lothaire, M. (2002)**. *Algebraic Combinatorics on Words*. Cambridge University Press, Chapter 2 (*Sturmian Words*) & Chapter 8 (*Periodicity*). (Canonical reference for central Sturmian / Pirillo words achieving Fine–Wilf tightness at $p + q - \gcd(p, q) - 1$.)
3. **Crochemore, M., & Rytter, W. (2003)**. *Jewels of Stringology: Text Algorithms*. World Scientific. (Proofs of the Weak Periodicity Lemma and dyadic border decomposition.)
4. **Rubinchik, M., & Shur, A. M. (2018)**. *EERTREE: An efficient data structure for processing palindromes in strings*. European Journal of Combinatorics, 68, 249–265 (`arXiv:1506.04862`). (Introduces the Palindromic Tree / PAM, `diff`, `slink`, and the $O(N \log N)$ palindrome partition DP.)
5. **Fici, G., Gagie, T., Kärkkäinen, J., & Kempa, D. (2014)**. *A subquadratic algorithm for minimum palindromic factorization*. Journal of Discrete Algorithms, 28, 41–48. (Proves the Shift-Overlap Invariant of palindromic suffix APs for $O(N \log N)$ factorization.)
6. **徐毅 (Xu Yi, 2014)**. *《回文树及其应用》 (Palindromic Trees and Their Applications)*. 中国国家集训队论文 (Chinese IOI National Team Papers 2014). (Foundational `[ZH]` competitive programming treatise on PAM, half-links `trans`, and `slink` DP.)
7. **金策 (Jin Ce, 2019)**. *《字符串算法选讲》 (Selected Topics in String Algorithms — Borders, Lyndon Words, and Runs)*. 中国国家集训队论文 (Chinese IOI National Team Papers 2019). (Comprehensive `[ZH]` synthesis of the Log-Block Border AP property, `[WC2016] 论战捆竹竿` modulo shortest path, and `[BJWC2018] Border 的四种求法`.)
8. **Kociumaka, T., Radoszewski, J., Rytter, W., & Waleń, T. (2015)**. *Internal Pattern Matching Queries in a Text and Applications*. SODA 2015, 532–551. (Establishes the $O(1)$ internal periodic occurrence AP representation for substrings $S[l..r]$.)
