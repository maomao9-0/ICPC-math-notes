# Wave 1A Reconciled Master Treatise & Problem Archive (Cohort 3, Iteration 105)
## Structural Periodicity, Border Theory, Weak Periodicity Lemma, Border-Group Modulo Shortest Path & Series-Link (`slink`) DP

> [!IMPORTANT]
> **Cohort 3 Cross-Comparison, Blind-Spot Audit & Reconciled Wave 1A Master Document (`cohort3_wave_1a_periodicity_borders_slink_dp.md`)**
> This document is the **Cohort 3 (Iteration 105)** reconciled master synthesis of:
> - **Cohort 1 (Iterations 01–05)**: `strings_research/iter_01_to_05_periodicity_borders_slink_dp.md` (895 lines, 32 accepted problems, 10 quarantined templates)
> - **Cohort 2 (Iterations 53–57)**: `strings_research/cohort2_iter_53_to_57_periodicity_borders_slink_dp.md` (777 lines, 32 accepted problems, 8 quarantined templates)
>
> All proofs, counterexamples, algorithmic kernels, frontier extensions, and the deduplicated union of **42 accepted non-template problems (`W1A-01`–`W1A-42`)** and **13 quarantined template problems (`R-1A-01`–`R-1A-13`)** strictly enforce the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard** defined in `strings_research/PLAN.md`.

---

## Section 1. Cross-Cohort Comparison & Blind-Spot Audit (Cohort 1 vs. Cohort 2)

### 1.1 High-Level Quantitative & Structural Comparison

| Audit Dimension | Cohort 1 (`iter_01_to_05`) | Cohort 2 (`cohort2_iter_53_to_57`) | Cohort 3 Reconciled Master (`cohort3_wave_1a`) |
| :--- | :--- | :--- | :--- |
| **Fine–Wilf Proof Architecture** | Single-orbit Hamiltonian path on $\mathbb{Z}/(p+q)\mathbb{Z}$ with $0$ deleted | First-return cycle map on $\mathbb{Z}/q\mathbb{Z}$ + Euclidean suffix induction | **Unified 3-Proof Synthesis** + exact component formula $p + q - n$ below threshold |
| **Border AP Halving Proof** | Dyadic interval $[2^{k-1}, 2^k)$ + `slink` 2-jump halving | Exact overlap inequality $\pi[u] < d_1 + d_2 \implies \pi[u] < \frac{2}{3}u$, $\pi[\pi[u]] < \frac{1}{2}u$ | **Both proofs unified** + explicit half-open $(\text{slink}[u], u]$ partition invariant |
| **`[WC2016]` Modulo Knapsack** | Full C++ kernel + unbounded vs. 0-1 deque push invariant | Argmin cycle-unrolling DAG proof + separated key derivation | **Full DAG proof + C++ reference kernel + boundary audit** |
| **PAM/KMP `slink` DP Proof** | Uniqueness of period-$d$ child in PAM fail tree + left-endpoint diagram | Explicit Lemma 56.2 (non-extendability of period $d$) + Pitfall 2 ($r-\text{len}[u]$ trap) | **Complete Zero-Magic Proof** + Polynomial/Affine & Length-Bounded `slink` extensions |
| **Accepted Non-Template Problems** | 32 (`P-1A-01`–`P-1A-32`) | 32 (`Problem 1A-01`–`1A-32`) | **42 Unique Deduplicated Problems (`W1A-01`–`W1A-42`)** |
| **Quarantined Template Problems** | 10 (`R-1A-01`–`R-1A-10`) | 8 (`R-1A-01`–`R-1A-08`) | **13 Unique Quarantined Templates (`R-1A-01`–`R-1A-13`)** |
| **Multilingual Citations** | 8 (inc. Crochemore–Rytter, Xu Yi 2014, Kociumaka SODA 2015) | 7 (inc. Weng Wentao 2017, `snuke`/`maspypy`/`noshi91`) | **12 Consolidated `[EN]`/`[ZH]`/`[JA]` Primary Citations** |

---

### 1.2 What Cohort 1 Captured That Cohort 2 Missed (Cohort 2 Blind Spots)

1. **Full-Domain Hamiltonian Path Proof of Fine–Wilf on $V = \{1, \dots, p + q - 1\}$**:
   - Cohort 1 observed that on $V = \{1, \dots, p+q-1\}$ (for $\gcd(p, q) = 1$), the partial transition map $f(i) = i + p$ (if $i < q$) and $f(i) = i - q$ (if $i > q$) satisfies $f(i) \equiv i + p \pmod{p + q}$. Since $\gcd(p, p + q) = \gcd(p, q) = 1$, $+p$ generates a single directed cycle of length $p + q$ on $\mathbb{Z}/(p+q)\mathbb{Z}$, and deleting the single out-of-bounds residue $0 \pmod{p+q}$ leaves a **single directed Hamiltonian path visiting all $p + q - 1$ indices**. Furthermore, at $N = p + q - 2$, the *only* deleted vertex is $p + q - 1$, which sits strictly inside the path $p \to \dots \to p+q-1 \to \dots \to q$ and splits $V \setminus \{p+q-1\}$ into **two explicit orbits**. Cohort 2 initially stumbled when trying to define $T$ on $\{1, \dots, p+q-1\}$ and retreated to the induced return map on $\{1, \dots, q\}$.
2. **Half-Open Interval Partition Invariant $(\text{slink}[u], u]$ vs. Closed Interval Double-Counting**:
   - Cohort 1 proved why $\text{slink}[u] = \text{fail}[v_c]$ (where $v_c$ is the bottom node of $u$'s constant-`diff` chain) sits at distance $d = \text{diff}[u]$ below $v_c$ even though $\text{diff}[\text{slink}[u]] \ne d$. Cohort 1 explicitly distinguished **counting/sum DPs** (which *must* use the half-open interval $(\text{slink}[u], u]$ with shortest length $\text{len}[\text{slink}[u]] + \text{diff}[u]$ to avoid double-counting $\text{slink}[u]$) from **idempotent $\min/\max$ knapsack transitions** (where closed intervals $[\text{slink}[u], u]$ are harmless because $\min(a, a) = a$).
3. **Production-Grade C++ Kernel & Unbounded vs. 0-1 Deque Push Invariant for `[WC2016] 论战捆竹竿`**:
   - Cohort 1 provided the complete, bug-free C++ implementation of dynamic modulus switching + monotonic queue relaxation, and explicitly pinpointed **Pitfall 3.1**: why `D[u]` must be updated from `dq.front()` *before* computing `key = D[u] - t * d` and pushing into `dq` (because multiple borders from the same AP block $\mathcal{A}_k$ can be used in sequence, corresponding to unbounded knapsack within the AP block).
4. **Uniqueness of Period-$d$ Child in PAM Fail Tree**:
   - When proving that $\text{fail}[u]$ is never skipped inside a longer AP chain at $r - \text{diff}[u]$, Cohort 1 proved a key structural lemma: a node $u_2$ in PAM can have **at most one child $u$ in the fail tree with $\text{diff}[u] = d \le \text{len}[u_2]$**, because a palindrome of length $\text{len}[u_2] + d$ with border $u_2$ has all of its characters uniquely determined by $u_2$ and period $d$.
5. **10 Problems & 5 Quarantine Entries Exclusive to Cohort 1**:
   - *Cohort 1 Exclusive Accepted Problems*: `CF 535D — Tavas and Malekas` (adjacent border compatibility + transitivity), `CF 17E — Palisection` (64MB PAM linked-list / Manacher sweep), `CF 1051E — Vasya and Big Integers` (Z-array lexicographical range clipping), `AtCoder AGC 032 F — One Third` (periodic lattice gap discretization), `UOJ #219 / [NOI2016] 优秀的拆分` (harmonic $O(N \log N)$ LCE square AP marking), `LOJ #6681 / Ynoi Substring Border AP Sums`, `QOJ Substring Palindrome Partition Queries`, `ICPC/UCup Huge-Length Fine–Wilf Word Equations (N <= 10^18)`, and `CF 1608F / PAM slink + Segment Tree Range Coupling`.
   - *Cohort 1 Exclusive Quarantined Templates*: `Luogu P3805 (Manacher)`, `UVA 455`, `POJ 2406`, `POJ 1961 / UVA 1328`, `POJ 2752`.
6. **Citations Exclusive to Cohort 1**:
   - **徐毅 (Xu Yi, 2014)** 《回文树及其应用》 (`国家集训队论文 2014`, foundational Chinese PAM treatise), **Crochemore & Rytter (2003)** *Jewels of Stringology*, and **Kociumaka et al. (SODA 2015)** *Internal Pattern Matching Queries in a Text*.

---

### 1.3 What Cohort 2 Captured That Cohort 1 Missed (Cohort 1 Blind Spots)

1. **Two Additional Proofs of Fine–Wilf & Exact Component Formula Below the Threshold**:
   - Cohort 2 provided (a) the **Induced First-Return Map** $\psi(x) = ((x + p - 1) \bmod q) + 1$ on $\{1, \dots, q\}$ (showing why $N = p + q - 2$ breaks *two* edges $x = q$ and $x = q - 1$ on the $q$-cycle), and (b) the **Euclidean Suffix Induction** on $(p, q) \to (p, q - p)$ over $S[p+1..n]$.
   - More importantly, Cohort 2 discovered the **exact connected component count below the Fine–Wilf threshold**: for $\max(p, q) \le n < p + q - \gcd(p, q)$, a string of length $n$ with periods $p$ and $q$ has **exactly $p + q - n$ independent character orbits (connected components)**! (Each unit reduction of $n$ below $p + q - \gcd(p, q)$ removes one edge from the cycle forest without creating cycles, increasing the component count by $+1$ from $\gcd(p, q)$ up to $p + q - n$.)
2. **Exact $\frac{2}{3}$ and $\frac{1}{2}$ Length-Drop Proof at `diff` Transitions**:
   - Whereas Cohort 1 used dyadic intervals $[2^{k-1}, 2^k)$ to bound the number of AP blocks by $\lceil \log_2 N \rceil$, Cohort 2 proved directly from periodicity overlap that whenever $d_2 = \text{diff}(\pi[u]) < \text{diff}(u) = d_1$, the overlap $2\pi[u] - u = \pi[u] - d_1$ must be strictly less than $d_2$ (otherwise $d_2 \mid d_1$ propagates across the overlap to give $S[1..u]$ period $d_2 < d_1$, a contradiction!). This yields the sharp inequalities:
     $$\pi[u] < d_1 + d_2 < 2 d_1 \implies \pi[u] < \frac{2}{3} u \quad \text{and} \quad \pi[\pi[u]] = \pi[u] - d_2 < d_1 = u - \pi[u] \implies \pi[\pi[u]] < \frac{1}{2} u.$$
3. **Explicit Diagnosis of the "$r - \text{len}[u]$ vs. $r - \text{len}[\text{slink}[u]] - \text{diff}[u]$" Trap in `slink` DP**:
   - Cohort 2 caught and dissected the #1 implementation bug when writing `slink` DP from memory: thinking that the longest palindrome $u$ at position $r$ contributes the *new* left endpoint $r - \text{len}[u]$. In fact, $r - \text{len}[u] = (r - d) - (\text{len}[u] - d) = (r - d) - \text{len}[\text{fail}[u]]$ is the **oldest (leftmost)** left endpoint and was **already included in $g[\text{fail}[u]]$ at step $r - d$**! The single *new* left endpoint entering $g[u]$ at step $r$ is the **shortest (rightmost)** member of the half-open chain $(\text{slink}[u], u]$, namely $r - \text{len}[\text{slink}[u]] - \text{diff}[u]$.
4. **10 Problems & 3 Quarantine Entries Exclusive to Cohort 2**:
   - *Cohort 2 Exclusive Accepted Problems*: `[BOI 2009] Radio Transmission (Luogu P4391)`, `UCup / QOJ Fine–Wilf Sub-Threshold Component Count (p + q - n)`, `CF 1721E — Prefix Function Queries` (KMP `slink` jump acceleration without $|\Sigma|$ table), `CF 149E — Martian Strings`, `CF 615C — Running Track`, `[POI 2012] OKR-A Horrible Poem (Luogu P3538)` ($O(\log L)$ exact period queries via SPF prime division + Weak Periodicity GCD closure), `CF 1043G — Speckled Band` ($\le 4$ block-type classification via periods/borders/squares), `Luogu P5555 — Common Palindromes on Dual PAMs`, `[THUPC 2018] 绿绿和串串 (Luogu P5446)` (mirror-flipping Manacher reachability), and `CF 1764G / Inverse KMP & Border-Set Realizability via slink`.
   - *Cohort 2 Exclusive Quarantined Templates*: `Luogu P5829 (KMP Fail Tree LCA)`, `CSES 1753`, `CSES 1732`.
5. **Citations Exclusive to Cohort 2**:
   - **翁文涛 (Weng Wentao, 2017)** 《回文自动机及其应用》 & WC2016《论战捆竹竿》命题报告 (`国家集训队论文 2017`), and Japanese competitive stringology treatises by **`snuke`**, **`maspypy`**, and **`noshi91`**.

---

### 1.4 Obscure & Frontier Stringology Techniques Hunted in Cohort 3 (Gap-Hunting Pass)

To ensure zero blind spots across `[EN]`, `[ZH]`, and `[JA]` grandmaster literature for Wave 1A, Cohort 3 hunts down and integrates **five frontier extensions** that neither Cohort 1 nor Cohort 2 developed in full:

1. **Unification of KMP Shortcut Links: `slink[u]` (Constant-Period Link) vs. `anc[u]` (Next-Character-Mismatch Link)**:
   - Both `CF 1721E` and `CF 1286E` use $O(\log N)$ or $O(1)$-amortized jumps on the KMP fail chain, but competitive programmers frequently confuse `slink[u]` (which groups borders by $\text{diff}[u] = u - \pi[u]$) with `anc[u]` (which skips ancestors $v = \pi[u]$ having $S[v+1] = S[u+1]$). In **Section 2.4**, we prove the exact structural inclusion: **every internal step inside a `slink` AP chain automatically has $S[\pi[u]+1] = S[\pi[\pi[u]]+1]$**, meaning `anc[u]` is an exact coarsening of `slink[u]`!
2. **Polynomial-Weight & Affine-Weight `slink` DP (`w(L) = P(L)`) without Segment Trees**:
   - Cohort 1 noted in Pitfall 4.1 that `slink` DP fails if $w(L)$ depends non-trivially on the palindrome/border length $L$. In **Section 4.4**, we show how **binomial index splitting** $L^m = (r - i)^m = \sum_{t=0}^m \binom{m}{t} (-1)^t r^{m-t} i^t$ allows maintaining $m+1$ scalar accumulators $g_t[u] = \sum_{i \in \mathcal{I}(u, r)} i^t dp[i]$ per PAM/KMP node, solving degree-$m$ polynomial-weighted palindrome/border partition DPs in $O(m \cdot N \log N)$ time!
3. **Length-Bounded (`L >= L_min` or `L_min <= L <= L_max`) & Windowed `slink` DP**:
   - When a problem restricts palindromic/border transitions to lengths $L \in [L_{\min}, L_{\max}]$, an AP chain $(\text{slink}[u], u]$ is clipped at both ends. In **Section 4.5**, we prove that because indices enter $g[u]$ in **strictly increasing order of left endpoint $i = r - \ell_k$**, maintaining a deque or delayed pointer on each residue class / `slink` chain handles arbitrary length windows in $O(N \log N)$.
4. **Multi-Period Fine–Wilf Theorem (Castelli–Mignosi–Restivo Theorem, 1999)**:
   - What if a string $S[1..N]$ has *three* periods $p_1 < p_2 < p_3$? In **Section 2.2.5**, we state the exact 3-period Fine–Wilf threshold and show how multi-period word equations contract in practice.
5. **The Critical Factorization Theorem (CFT — Cesari, Vincent, Duval)**:
   - Connecting local period $\text{lp}(i)$ (the shortest non-empty square/overlap centered at $i$) to global period $p_{\min}(S)$: in every string $S$, there exists at least one factorization $S = u v$ where the local period equals the global period $\text{lp}(|u|) = p_{\min}(S)$, and $\text{lp}(i) \le p_{\min}(S)$ everywhere.

---

## Section 2. Reconciled Master Treatise: Period–Border Duality, Fine–Wilf & Log-Block Border APs

### 2.1 Prerequisite Boundary & Multilingual Rosetta Stone

Per `AGENTS.md` and `strings_research/PLAN.md`, the reader is assumed to hold tested $O(N)$ library implementations of **KMP (`pi` array)**, **Z-Algorithm (`z` array)**, **Rolling Hash / Suffix Array (`SA` + `LCP` RMQ)**, and **Palindromic Automaton (PAM / Eertree)**. Standard construction code is omitted; we focus strictly on structural invariants, complexity collapses, and non-standard algorithmic kernels.

| Concept (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) | Canonical Notation |
| :--- | :--- | :--- | :--- |
| Period (weak / general period) | 周期 (广义周期) | 周期 (Period) | $p \in \text{Per}(S)$ ($S[i] = S[i+p],\; 1 \le i \le |S|-p$) |
| Exact / full period | 整周期 / 循环节 | 完全周期 / 最小周期 | $p \in \text{Per}(S)$ and $p \mid |S|$ |
| Proper Border | Border / 真公共前后缀 | ボーダー (接頭辞かつ接尾辞) | $b \in \text{Border}(S)$ ($S[1..b] = S[|S|-b+1..|S|]$) |
| Period–Border Duality | 周期与 Border 的对偶性 | 周期とボーダーの双対性 | $p \in \text{Per}(S) \iff |S|-p \in \text{Border}(S)$ |
| Weak Periodicity Lemma | 弱周期引理 | 弱周期性補題 | $|S| \ge p+q \implies \gcd(p,q) \in \text{Per}(S)$ |
| Fine–Wilf Theorem | Fine–Wilf 定理 (周期引理) | Fine–Wilf の定理 | $|S| \ge p+q-\gcd(p,q) \implies \gcd(p,q) \in \text{Per}(S)$ |
| Central Sturmian Word | 中心 Sturmian 词 / 斐波那契前缀 | 中心 Sturmian 語 / 極値反例 | Unique binary word of length $p+q-\gcd(p,q)-1$ |
| Border AP Property | Border 的等差数列性质 | ボーダーの等差数列分解 | All borders partition into $\le \lceil \log_2 |S| \rceil$ APs |
| Modulo Shortest Path + AP Knapsack | 同余最短路 + 等差数列背包 | 同余最短路 + 等差数列DP | Dynamic modulus switch + residue-cycle deque |
| Series Link / Difference Link | 等差数列跳链 (`slink` / `diff`) | 直列リンク (`slink`) / 回文木DP | $\text{diff}[u] = \text{len}[u]-\text{len}[\text{fail}[u]]$, $\text{slink}[u]$ |
| Next-Character Mismatch Link | 失配加速跳链 (`anc[u]`) | KMP 短絡リンク (`anc`) | $\text{anc}[u] = \pi[u]$ if $S[\pi[u]+1] \ne S[u+1]$ else $\text{anc}[\pi[u]]$ |

---

### 2.2 Period–Border Duality & The Fine–Wilf Periodicity Theorem

#### 2.2.1 Period–Border Duality Bijection
Let $S = S[1..N]$ be a 1-indexed string of length $N$.
- **Period**: $p \in \{1, 2, \dots, N\}$ belongs to $\text{Per}(S)$ iff $S[i] = S[i+p]$ for all $1 \le i \le N - p$.
- **Proper Border**: $b \in \{0, 1, \dots, N-1\}$ belongs to $\text{Border}(S)$ iff $S[1..b] = S[N-b+1..N]$, i.e., $S[i] = S[i + (N - b)]$ for all $1 \le i \le b$.

> **Theorem 2.1 (Period–Border Duality Bijection)**:
> The map $\Phi(b) = N - b$ is an order-reversing bijection between $\text{Border}(S) \subseteq \{0, \dots, N-1\}$ and $\text{Per}(S) \subseteq \{1, \dots, N\}$:
> $$\boxed{b \in \text{Border}(S) \iff p = N - b \in \text{Per}(S), \qquad p_{\min}(S) = N - \pi[N].}$$

```
Index:    1   2   3   ...   N-p  ...   p   p+1  ...   N
S:      [ a   b   a   ...    c   ... ]
                  || (shifted by period p = N - b)
S:                      [    a    b    a   ...   c  ]
        |<------ p ------>|<--------- b = N-p --------->|
```

- **Prefix-Truncation Persistence vs. Right-Extension Fragility**: If $p \in \text{Per}(S[1..N])$, then $p$ is a valid period of every substring $S[l..r]$. However, appending $S[N+1]$ preserves period $p$ *if and only if* the single character equality $S[N+1] = S[N+1-p]$ holds.

---

#### 2.2.2 Three Unified Proofs of the Fine–Wilf Theorem ($N \ge p + q - \gcd(p, q)$)

> **Theorem 2.2 (Fine–Wilf Theorem, 1965)**:
> Let $S[1..N]$ admit periods $p$ and $q$, and let $g = \gcd(p, q)$.
> 1. **Above Threshold ($N \ge p + q - g$)**: $g = \gcd(p, q)$ is also a period of $S[1..N]$.
> 2. **Below Threshold ($\max(p, q) \le N < p + q - g$)**: The index graph of $S[1..N]$ under edges $\{i \leftrightarrow i+p\}$ and $\{i \leftrightarrow i+q\}$ decomposes into **exactly $p + q - N$ connected components** (independent character orbits). In particular, at $N = p + q - g - 1$, there are $g + 1$ components (one residue class modulo $g$ splits into $2$ components while the other $g - 1$ residue classes remain single components), yielding a binary counterexample of length $p + q - g - 1$ whenever $p \nmid q$ and $q \nmid p$.

*Reduction to the Coprime Case $\gcd(p, q) = 1$ via Residue Decimation*:
Partition $\{1, \dots, N\}$ into $g = \gcd(p, q)$ residue classes modulo $g$: for each $r \in \{1, \dots, g\}$, form the decimated string $S^{(r)}$ of length $m_r = \lfloor (N - r)/g \rfloor + 1$ at indices $r, r+g, \dots, r+(m_r-1)g$. Since $p = p' g$ and $q = q' g$ are multiples of $g$, each $S^{(r)}$ has coprime periods $p' = p/g$ and $q' = q/g$. When $N \ge p + q - g$, every $r \in \{1, \dots, g\}$ satisfies $m_r \ge \lfloor (p + q - 2g)/g \rfloor + 1 = p' + q' - 1$. If the coprime case holds at length $p' + q' - 1$ (making each $S^{(r)}$ constant), then $S[i] = S[i+g]$ holds for all $1 \le i \le N - g$, so $g \in \text{Per}(S)$.

Assume now $\gcd(p, q) = 1$ and $N = p + q - 1$. We give three complementary proofs that $S[1..p+q-1]$ is constant:

- **Proof I (Full-Domain Hamiltonian Path on $V = \{1, \dots, p + q - 1\}$ — Cohort 1)**:
  Define $f : V \setminus \{q\} \to V \setminus \{p\}$ by
  $$f(i) = \begin{cases} i + p & \text{if } 1 \le i \le q - 1, \\ i - q & \text{if } q + 1 \le i \le p + q - 1. \end{cases}$$
  Every $i \in V \setminus \{q\}$ stays in bounds ($p+1 \le i+p \le p+q-1$ for $i < q$, and $1 \le i-q \le p-1$ for $i > q$) and satisfies $S[f(i)] = S[i]$. Modulo $p + q$, both branches satisfy $f(i) \equiv i + p \pmod{p + q}$. Since $\gcd(p, p + q) = \gcd(p, q) = 1$, $+p$ generates a single directed cycle of length $p + q$ on $\mathbb{Z}/(p+q)\mathbb{Z}$. Restricting to $V = \{1, \dots, p+q-1\}$ deletes only vertex $0 \pmod{p+q}$, leaving a **single directed Hamiltonian path of length $p + q - 1$** from $p$ to $q$:
  $$p \xrightarrow{f} f(p) \xrightarrow{f} f^{(2)}(p) \xrightarrow{f} \dots \xrightarrow{f} q.$$
  Thus all $p + q - 1$ characters of $S$ are equal! $\blacksquare$

- **Proof II (Induced First-Return Cycle on $U = \{1, \dots, q\}$ & Exact Component Count — Cohort 2)**:
  For any $x \in \{1, \dots, q - 1\}$, $x + p \le p + q - 1 = N$, so $S[x] = S[x + p]$. If $x + p > q$, then $1 \le x + p - q \le p - 1 \le q$ and $S[x + p] = S[x + p - q]$. Hence the map $\psi(x) = ((x + p - 1) \bmod q) + 1$ preserves characters ($S[x] = S[\psi(x)]$) for every $x \in \{1, \dots, q\}$ **such that $x + p \le N$**.
  Since $\gcd(p, q) = 1$, $\psi$ forms a single directed cycle of length $q$ on $\{1, \dots, q\}$.
  - When $N = p + q - 1$, only $x = q$ fails $x + p \le N$ (since $q + p = N + 1$). Deleting $1$ edge from a $q$-cycle leaves a single path of $q$ vertices, so $S[1..q]$ (and hence $S[1..N]$) is constant.
  - More generally, when $q \le N \le p + q - 1$, how many vertices $x \in \{1, \dots, q\}$ fail $x + p \le N$? Those with $N - p + 1 \le x \le q$, which is **exactly $k = q - (N - p) = p + q - N$ vertices**! Deleting $k$ edges from a single cycle of length $q$ splits $\{1, \dots, q\}$ (and hence $S[1..N]$) into **exactly $p + q - N$ connected components**! $\blacksquare$

- **Proof III (Subtractive Euclidean Induction — Cohort 1 & 2)**:
  Assume $1 \le p < q$ and $N \ge p + q - \gcd(p, q)$. For every index $j \in \{p + 1, \dots, N - (q - p)\}$ in the suffix $S[p+1..N]$, we have $j - p \ge 1$ and $j + (q - p) \le N$, so $S[j] \stackrel{(-p)}{=} S[j - p] \stackrel{(+q)}{=} S[j - p + q]$. Thus $S[p+1..N]$ (of length $N - p \ge p + (q - p) - \gcd(p, q - p)$) has periods $p$ and $q - p$. By induction on $p + q$, $S[p+1..N]$ has period $g = \gcd(p, q)$, and since $p$ is a multiple of $g$, period $g$ extends across the prefix $S[1..p]$ as well. $\blacksquare$

---

#### 2.2.3 Hand-Checkable Extremal Counterexample at $N = p + q - \gcd(p, q) - 1$
Take $(p, q) = (5, 8)$ ($\gcd(5, 8) = 1$). The Fine–Wilf threshold is $5 + 8 - 1 = 12$.
At length $N = 12$, the Hamiltonian path $f$ on $\{1, \dots, 12\}$ is:
$$5 \xrightarrow{+5} 10 \xrightarrow{-8} 2 \xrightarrow{+5} 7 \xrightarrow{+5} \mathbf{12} \xrightarrow{-8} 4 \xrightarrow{+5} 9 \xrightarrow{-8} 1 \xrightarrow{+5} 6 \xrightarrow{+5} 11 \xrightarrow{-8} 3 \xrightarrow{+5} 8.$$
At length $N = 11 = p + q - 2$, vertex $\mathbf{12}$ disappears, cutting the path into $p + q - N = 5 + 8 - 11 = 2$ orbits:
- $C_1 = \{2, 5, 7, 10\} \gets \texttt{'b'}$
- $C_2 = \{1, 3, 4, 6, 8, 9, 11\} \gets \texttt{'a'}$

```
Index:   1  2  3  4  5  6  7  8  9 10 11
String:  a  b  a  a  b  a  b  a  a  b  a   (Central Sturmian / Fibonacci word of length 11)
```
Here $S[1..6] = \texttt{abaaba} = S[6..11]$ (period $5$) and $S[1..3] = \texttt{aba} = S[9..11]$ (period $8$), yet $S$ is not constant!

---

#### 2.2.4 Frontier Extension: Three-Period Fine–Wilf Theorem (Castelli–Mignosi–Restivo, 1999)
What if a string $S[1..N]$ has **three** periods $p_1 < p_2 < p_3$?
Let $g = \gcd(p_1, p_2, p_3)$. Define the three-variable Euclidean step $h(x, y, z)$ ($x \le y \le z$) recursively by:
$$h(x, y, z) = \begin{cases} y + z - \gcd(y, z) & \text{if } x = 0, \\ x + h\bigl(y \bmod x,\; \min(x, z - x \lfloor y/x \rfloor),\; \max(x, z - x \lfloor y/x \rfloor)\bigr) & \text{if } x > 0 \text{ (via } (x, y-x, z-x)\text{)}. \end{cases}$$
More concretely, **Castelli, Mignosi, and Restivo (1999)** proved that if $S$ has periods $p_1, p_2, p_3$, then $\gcd(p_1, p_2, p_3) \in \text{Per}(S)$ whenever
$$N \ge \frac{1}{2}\bigl(p_1 + p_2 + p_3 - 2\gcd(p_1, p_2, p_3) + h(p_1, p_2, p_3)\bigr),$$
which is strictly smaller than the pairwise bound $\min_{i \ne j}(p_i + p_j - \gcd(p_i, p_j))$, and extremal counterexamples are three-letter **episturmian (Arnoux–Rauzy) words**.

---

### 2.3 The Weak Periodicity Lemma & Log-Block Border AP Decomposition (`Border 的等差数列性质`)

#### 2.3.1 Single-AP Structure of Borders in $[N/2, N]$
> **Theorem 2.3 (Half-Length Border AP Theorem)**:
> For any string $S[1..N]$, let $p_{\min} = N - \pi[N]$ be its shortest period. If $p_{\min} \le N/2$, then every period $p \in \text{Per}(S)$ with $p \le N/2$ is an **exact multiple** of $p_{\min}$. Equivalently, all borders of $S$ of length $\ge \lceil N/2 \rceil$ form a **single arithmetic progression** with step $p_{\min}$:
> $$\mathcal{B}_{\ge N/2}(S) = \bigl\{N - k \cdot p_{\min} \;\big|\; 1 \le k \le \lfloor N / (2 p_{\min}) \rfloor \bigr\}.$$

*Proof*: For any period $p \le N/2$, we have $p_{\min} + p \le N/2 + N/2 = N$. By the Weak Periodicity Lemma (Theorem 2.2), $g = \gcd(p_{\min}, p) \in \text{Per}(S)$. Since $p_{\min}$ is the minimum positive period of $S$ and $g \le p_{\min}$, we must have $g = p_{\min}$, so $p_{\min} \mid p$. Conversely, every multiple $k \cdot p_{\min} < N$ is trivially a period of $S$. $\blacksquare$

---

#### 2.3.2 Reconciled Proof of the $O(\log N)$ Border AP Partition (Dyadic + Exact $\frac{2}{3} / \frac{1}{2}$ Drop)
For every node $u \ge 1$ in the KMP fail tree (or PAM fail tree), define:
$$\text{diff}[u] = \text{len}[u] - \text{len}[\text{fail}[u]], \qquad \text{slink}[u] = \begin{cases} \text{slink}[\text{fail}[u]] & \text{if } \text{diff}[u] = \text{diff}[\text{fail}[u]], \\ \text{fail}[u] & \text{otherwise.} \end{cases}$$

> **Theorem 2.4 (Exact Length-Drop & Disjoint Half-Open Partition via `slink`)**:
> 1. **Exact Length-Drop Inequality (Cohort 2)**: Let $u$ be a border/palindrome, $v = \text{fail}[u]$, and $w = \text{fail}[v]$, with $d_1 = \text{diff}[u] = |u| - |v|$ and $d_2 = \text{diff}[v] = |v| - |w|$. Since $S[1..v]$ is a prefix of $S[1..u]$, $d_1 \in \text{Per}(S[1..v])$, so $d_2 \le d_1$. Whenever a series-link boundary occurs ($d_2 < d_1$):
>    - In $S[1..u]$, the prefix $S[1..v]$ and suffix $S[u-v+1..u]$ both have period $d_2$, and overlap on a middle segment of length $2|v| - |u| = |v| - d_1$. If $|v| - d_1 \ge d_2$, the two period-$d_2$ copies overlap by at least $d_2$ (and since $d_1 + d_2 \le |v|$, $d_2 \mid d_1$), forcing all of $S[1..u]$ to have period $d_2 < d_1$, a contradiction!
>    - Therefore $|v| - d_1 < d_2$, which implies:
>      $$\boxed{|v| < d_1 + d_2 < 2d_1 \implies |\text{fail}[u]| < \frac{2}{3}|u|, \qquad |\text{fail}[\text{fail}[u]]| = |v| - d_2 < d_1 = |u| - |v| < \frac{1}{2}|u|!}$$
>    Thus every jump $u \leftarrow \text{slink}[u]$ shrinks $|u|$ by a factor $< 1/2$ in at most $2$ steps (and partitioning borders into dyadic intervals $[2^{k-1}, 2^k)$ gives at most $\lceil \log_2 N \rceil$ APs).
> 2. **Half-Open Partition Invariant (Cohort 1)**: Let $v_c$ be the lowest ancestor of $u$ with $\text{diff}[v_c] = \text{diff}[u] = d$, so $\text{slink}[u] = \text{fail}[v_c]$. Because $\text{len}[v_c] - \text{len}[\text{slink}[u]] = \text{diff}[v_c] = d$, the half-open chain $(\text{slink}[u], u]$ consists of the exact arithmetic progression:
>    $$\mathcal{L}(u) = \bigl\{\text{len}[\text{slink}[u]] + d,\; \text{len}[\text{slink}[u]] + 2d,\; \dots,\; \text{len}[u]\bigr\}.$$
>    Iterating $u \leftarrow \text{slink}[u]$ while $u > 0$ partitions all positive borders/palindromic suffixes into **disjoint** half-open progressions $(\text{slink}[u], u]$, omitting no element and counting no element twice.

---

#### 2.3.3 Palindromic Suffix $\leftrightarrow$ Border Equivalence
> **Theorem 2.5 (Palindromic Suffixes Are Palindromic Borders)**:
> For any palindrome $Q = Q[1..m]$, a proper suffix $Q[m-k+1..m]$ of length $k < m$ is a palindrome if and only if $k \in \text{Border}(Q)$. Consequently, for any string $S[1..r]$ with longest palindromic suffix $Q$, all palindromic suffixes of $S[1..r]$ are borders of $Q$ and partition into $\le \lceil \log_2 r \rceil$ arithmetic progressions via `diff[u]` and `slink[u]` on the PAM fail tree.

---

### 2.4 Unifying KMP Shortcut Links: `slink[u]` vs. `anc[u]` (Frontier Synthesis)

In competitive programming, two seemingly different KMP fail-tree shortcut pointers appear across problems like `CF 1721E` and `CF 1286E`:
1. **The Period-Difference Link (`slink[u]`)**: Skips ancestors with the same period step $\text{diff}[u] = \text{diff}[\pi[u]]$:
   $$\text{slink}[u] = \bigl(\text{diff}[u] == \text{diff}[\pi[u]] \;\text{?}\; \text{slink}[\pi[u]] : \pi[u]\bigr).$$
2. **The Next-Character Mismatch Link (`anc[u]`)**: Skips ancestors whose next character matches $S[u+1]$:
   $$\text{anc}[u] = \bigl(S[\pi[u]+1] == S[u+1] \;\text{?}\; \text{anc}[\pi[u]] : \pi[u]\bigr).$$

How are `slink[u]` and `anc[u]` related?

> **Theorem 2.6 (`slink` Implies Next-Character Equality Inside the Chain)**:
> Suppose $u \ge 1$ satisfies $\text{diff}[u] = \text{diff}[\pi[u]] = d$. Let $v = \pi[u] = u - d$ and $w = \pi[v] = u - 2d$. Then the characters immediately following $v$ and $w$ in $S$ are **guaranteed to be identical**:
> $$\boxed{\text{diff}[u] = \text{diff}[\pi[u]] = d \implies S[\pi[u] + 1] = S[\pi[\pi[u]] + 1]!}$$

*Proof*: Since $d = u - \pi[u]$ is a period of $S[1..u]$, for every index $i \in [1, u - d]$ we have $S[i] = S[i + d]$.
Now evaluate this equality at $i = w + 1 = \pi[\pi[u]] + 1 = u - 2d + 1$:
- Since $w = \pi[v] \ge 0$, we have $i = w + 1 \ge 1$.
- Furthermore, $i + d = (u - 2d + 1) + d = u - d + 1 = \pi[u] + 1 = v + 1 \le u$ (because $d = \text{diff}[v] = v - w \ge 1 \implies v + 1 \le v + d = u$)!
- Because **both** $w + 1$ and $v + 1$ lie strictly inside $[1, u]$, the period $d$ of $S[1..u]$ forces:
  $$S[\pi[\pi[u]] + 1] = S[w + 1] = S[w + 1 + d] = S[v + 1] = S[\pi[u] + 1]! \quad \blacksquare$$

> [!TIP]
> **Why Theorem 2.6 Matters (`slink[u]` vs. `anc[u]`)**:
> Notice that $u + 1$ lies *outside* $S[1..u]$, so $S[u+1]$ may or may not equal $S[\pi[u]+1]$. However, for **every strict ancestor inside $u$'s AP chain** ($v = \pi[u], \pi[\pi[u]], \dots, v_c$), the index $v + 1 \le u$ lies *inside* $S[1..u]$, so **all of them share the exact same next character $S[\pi[u]+1]$**!
> - Therefore, in KMP transition queries (`CF 1721E`) or Inverse KMP (`CF 1764G`), testing $S[\pi[u]+1]$ once and jumping to $\text{slink}[u]$ tests the entire AP chain in $O(1)$ time!
> - And in online border deletion (`CF 1286E`), `anc[u]` is even coarser than `slink[u]`: it skips not only the constant-period chain where $S[v+1]$ is forced equal by periodicity, but also any accidental character matches $S[v+1] == S[u+1]$ across different AP blocks!

---

## Section 3. Reconciled Master Treatise: Border-Group Modulo Shortest Path (`同余最短路 + 等差数列背包`)

### 3.1 Problem Archetype & The $O(N^2)$ Bottleneck (`[WC2016] 论战捆竹竿`)
Given $S[1..N]$ ($N \le 5 \times 10^5$) and $W \le 10^{18}$, we start with $S$ (length $N$) and repeatedly append $S$ overlapping by any border $b \in \text{Border}(S)$ (adding period weight $p = N - b \in \text{Per}(S)$). Count how many total lengths $L \in [N, W]$ are achievable.
- **Why Standard Modulo Shortest Path Fails**: $|\text{Per}(S)|$ can be $\Theta(N)$, so relaxing $\Theta(N)$ periods across $\Theta(N)$ residues takes $\Theta(N^2)$ time.

### 3.2 Dynamic Modulus Switching + Residue-Cycle Monotonic Queue ($O(N \log N)$)
By Theorem 2.4, $\text{Per}(S) = \{N - b : b \in \text{Border}(S)\}$ partitions into $K \le \lceil \log_2 N \rceil$ arithmetic progressions:
$$\mathcal{A}_k = \bigl\{x_k + j \cdot d_k \;\big|\; 0 \le j \le c_k\bigr\}, \qquad x_k = N - b_{\max, k},\; d_k = \text{diff}[b_{\max, k}].$$

Initialize the shortest-path array modulo $m = N$ with $D[0] = N$ and $D[1..N-1] = +\infty$ (which automatically provides unlimited zero-overlap $+N$ extensions). For each AP block $(x_k, d_k, c_k)$:

1. **Subroutine A — Dynamic Modulus Switch ($m_{\text{old}} \to x_k$) in $O(m_{\text{old}} + x_k)$ Time**:
   - Why switch the DP modulus to $x_k$? Because modulo $x_k$, the base weight $x_k$ satisfies $x_k \equiv 0 \pmod{x_k}$ (zero residue shift, unlimited copies implicitly available!), and any $x_k + j \cdot d_k \in \mathcal{A}_k$ shifts the residue by $+j \cdot d_k \pmod{x_k}$ with weight $x_k + j \cdot d_k$.
   - Project $D_{\text{old}}[0..m_{\text{old}}-1]$ into $D_{\text{new}}[0..x_k-1]$ via $D_{\text{new}}[D_{\text{old}}[r] \bmod x_k] \leftarrow \min(\dots, D_{\text{old}}[r])$.
   - To preserve unlimited $+m_{\text{old}}$ transitions from earlier stages, partition $\{0, \dots, x_k - 1\}$ into $g_1 = \gcd(m_{\text{old}}, x_k)$ independent directed cycles of step $+m_{\text{old}} \pmod{x_k}$. On each cycle of length $L_1 = x_k / g_1$, locate the global minimum vertex $u_{\min} = \arg\min D_{\text{new}}[u]$ (which can never be improved since $m_{\text{old}} > 0$) and relax $L_1 - 1$ steps forward around the cycle:
     $$D_{\text{new}}\bigl[(u + m_{\text{old}}) \bmod x_k\bigr] \leftarrow \min\Bigl(D_{\text{new}}\bigl[(u + m_{\text{old}}) \bmod x_k\bigr],\; D_{\text{new}}[u] + m_{\text{old}}\Bigr).$$

2. **Subroutine B — Bounded-Window Monotonic Queue on $+d_k \pmod{x_k}$ Cycles in $O(x_k)$ Time**:
   - If $c_k = 0$, Subroutine A already handled $+x_k$. If $c_k \ge 1$, partition $\{0, \dots, x_k - 1\}$ into $g_2 = \gcd(d_k, x_k)$ independent cycles of length $L_2 = x_k / g_2$.
   - On each cycle, rotate the cycle to start at its minimum-distance vertex $v_0 = \arg\min D[v]$ (unrolling the cycle into a DAG $v_t = (v_0 + t \cdot d_k) \bmod x_k$ for $t = 0, 1, \dots, L_2 - 1$ with zero wrap-around needed!).
   - For $t = 1 \dots L_2 - 1$, transitioning from $s = t - j$ ($1 \le j \le c_k$) adds weight $x_k + (t - s)d_k$:
     $$\boxed{D[v_t] \leftarrow \min\left(D[v_t],\; x_k + t \cdot d_k + \min_{\max(0, t - c_k) \le s \le t - 1} \bigl(D[v_s] - s \cdot d_k\bigr)\right).}$$
   - Maintain a monotonic deque of pairs `(s, D[v_s] - s * d_k)` over window $[t - c_k, t - 1]$. Crucially, update $D[v_t]$ from `dq.front()` **before** pushing `(t, D[v_t] - t * d_k)` into `dq` so that multi-item combinations from $\mathcal{A}_k$ propagate within the same pass!

```cpp
// Reconciled Reference Kernel: Border-Group Modulo Shortest Path ([WC2016] Luogu P4156)
// Input: string length n, max length W, and O(log n) border-period APs (x_k, d_k, c_k)
long long solve_border_knapsack(int n, long long W, const vector<tuple<int, int, int>>& aps) {
    int m = n;
    vector<long long> D(m, INF), nxt;
    D[0] = n; // Base copy of S has length n === 0 (mod n); +n is free

    for (auto [x, d, c] : aps) {
        // Subroutine A: Switch modulus m -> x via gcd(m, x) cycle unrolling
        nxt.assign(x, INF);
        for (int r = 0; r < m; ++r)
            if (D[r] < INF) nxt[D[r] % x] = min(nxt[D[r] % x], D[r]);
        int g1 = std::gcd(m, x), len1 = x / g1;
        for (int start = 0; start < g1; ++start) {
            int best = start;
            for (int u = (start + m) % x; u != start; u = (u + m) % x)
                if (nxt[u] < nxt[best]) best = u;
            for (int u = best, step = 1; step < len1; ++step) {
                int v = (u + m) % x;
                nxt[v] = min(nxt[v], nxt[u] + m);
                u = v;
            }
        }
        D.swap(nxt);
        m = x;

        // Subroutine B: Sliding-window monotonic queue of width c on +d (mod x) cycles
        if (c == 0) continue;
        int g2 = std::gcd(d, x), len2 = x / g2;
        for (int start = 0; start < g2; ++start) {
            int best = start;
            for (int u = (start + d) % x; u != start; u = (u + d) % x)
                if (D[u] < D[best]) best = u;
            if (D[best] >= INF) continue;

            deque<pair<int, long long>> dq;
            dq.push_back({0, D[best]});
            int u = best;
            for (int t = 1; t < len2; ++t) {
                u = (u + d) % x;
                while (!dq.empty() && dq.front().first < t - c) dq.pop_front();
                if (!dq.empty())
                    D[u] = min(D[u], dq.front().second + x + 1LL * t * d);
                long long key = D[u] - 1LL * t * d; // Push UPDATED D[u] for unbounded knapsack
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

## Section 4. Reconciled Master Treatise: Series-Link (`slink` / `diff`) DP on PAM & KMP

### 4.1 The Complete Zero-Magic Proof of the `slink` Shift-Overlap Invariant

Consider a 1D string partition DP over palindromic suffixes or borders $\mathcal{A}(r)$ at right endpoint $r$:
$$dp[r] = \bigoplus_{L \in \mathcal{A}(r)} dp[r - L].$$
Let $u$ be a chain-top node visited during the `slink` loop at position $r$, with step $d = \text{diff}[u]$ and half-open AP chain $(\text{slink}[u], u]$ consisting of lengths:
$$\mathcal{L}(u) = \bigl\{\ell_1, \ell_2, \dots, \ell_k\bigr\}, \qquad \ell_j = \text{len}[u] - (j - 1)d, \qquad \ell_k = \text{len}[\text{slink}[u]] + d.$$

> **Theorem 4.1 (Complete Reconciled Shift-Overlap Theorem — Cohorts 1 & 2)**:
> Suppose $k \ge 2$, so $v = \text{fail}[u]$ has $\text{diff}[v] = \text{diff}[u] = d$ and $\text{slink}[v] = \text{slink}[u]$. Then:
> 1. **Exact Left-Endpoint Set Alignment**:
>    At position $r$, the set of left-endpoint DP indices queried by $u$'s half-open chain $(\text{slink}[u], u]$ is:
>    $$\mathcal{I}(u, r) = \bigl\{r - \ell_1,\; r - \ell_2,\; \dots,\; r - \ell_{k-1},\; r - \ell_k\bigr\}.$$
>    At the earlier position $r' = r - d$, node $v = \text{fail}[u]$ has half-open chain $(\text{slink}[v], v]$ of lengths $\{\ell_2, \ell_3, \dots, \ell_k\}$. Since $(r - d) - \ell_{j+1} = (r - d) - (\ell_j - d) = r - \ell_j$, the left endpoints queried by $v$ at $r - d$ are:
>    $$\mathcal{I}(v, r - d) = \bigl\{r - \ell_1,\; r - \ell_2,\; \dots,\; r - \ell_{k-1}\bigr\}.$$
>    Therefore:
>    $$\boxed{\mathcal{I}(u, r) = \mathcal{I}(\text{fail}[u],\, r - \text{diff}[u]) \;\sqcup\; \bigl\{\,r - \text{len}[\text{slink}[u]] - \text{diff}[u]\,\bigr\}!}$$
> 2. **Guaranteed Chain-Top Visit at $r - d$ & Non-Overwrite in $(r - d, r)$**:
>    - *Why $v = \text{fail}[u]$ occurred at $r - d$*: $v$ is a prefix of $u = S[r-\ell_1+1..r]$ of length $\ell_1 - d$, so $v = S[r-\ell_1+1 .. r-d]$ ends at $r - d$.
>    - *Why $v$ was NOT skipped inside a longer period-$d$ chain at $r - d$*: In PAM, $u$ is the **unique** node in the fail tree with $\text{fail}[w] = v$ and $\text{diff}[w] = d$ (because $d \le \text{len}[v]$ fixes all characters of $w$ to match $u$). If $u$ itself had occurred ending at $r - d$, then gluing $u$ at $r - d$ and $u$ at $r$ along their overlap $v$ of length $\ell_1 - d \ge d$ would form a palindrome $u^+$ of length $\ell_1 + d$ ending at $r$ with $\text{fail}[u^+] = u$ and $\text{diff}[u^+] = d$, contradicting that $u$ is a `slink` chain head at step $r$!
>    - *Why $v$ was never overwritten in $(r - d, r)$*: If $v$ occurred as a suffix at some $r'' \in (r - d, r)$, then inside $u = S[r-\ell_1+1..r]$ (which has minimum period $d$), $v$ would occur at shift $r - r'' \in (0, d)$, forcing a period $< d$ by the Weak Periodicity Lemma, a contradiction!

```
Index:   r-l_1     r-l_2     r-l_3 ... r-l_k               r-d         r
           |----d----|----d----|         |                  |          |
At r:      [========= u_1 (len l_1) ===================================]
                     [========= u_2 (len l_2) =========================]
                               [========= u_3 (len l_3) ===============]
                                         [=== u_k (len l_k) ===========]  <-- NEW index: r - l_k = r - len[slink[u]] - d

At r-d:    [========= u_2 (len l_2) ========================]
                     [========= u_3 (len l_3) ==============]
                               [=== u_k (len l_k) ==========]
           \_______________________ ________________________/
                                   v
                      Exact match = g[fail[u]]!
```

### 4.2 Universal `slink` DP Recurrence & Double-End Interleaving Bijection (`CF 932G`, `CF 906E`)
For every $r = 1 \dots N$, after advancing PAM (or KMP) to `last`:
```cpp
for (int u = last; u > 0; u = slink[u]) { // Note: even root is 0, odd root is 1 (len = -1)
    g[u] = dp[r - len[slink[u]] - diff[u]];
    if (diff[u] == diff[fail[u]])
        g[u] = combine(g[u], g[fail[u]]);
    dp[r] = combine(dp[r], g[u]); // In CF 932G / CF 906E, gate this line on (r % 2 == 0)
}
```
- **Symmetric Partition Interleaving (`CF 932G`)**: Interleaving $T = S[1]\,S[N]\,S[2]\,S[N-1]\dots$ turns $S[1..m] = S[N-m+1..N]$ into the condition that $T[1..2m]$ is an even-length palindrome.
- **Interval Reversal Interleaving (`CF 906E`)**: Interleaving $T = A[1]\,B[1]\,A[2]\,B[2]\dots$ turns $A[l..r]^R = B[l..r]$ into the condition that $T[2l-1..2r]$ is an even-length palindrome.

---

### 4.3 Frontier Extension 1: Polynomial-Weighted `slink` DP (`w(L) = P(L)`) via Binomial Splitting
Suppose the transition weight depends polynomially on the palindrome/border length $L$:
$$dp[r] = \sum_{L \in \mathcal{A}(r)} dp[r - L] \cdot P(L), \qquad P(L) = \sum_{m=0}^D c_m L^m.$$
Because each length $L = \ell_j$ in $g[\text{fail}[u]]$ grows by $+d$ when advancing from $r - d \to r$, a naive scalar $g[u]$ cannot maintain $\sum L^m dp[r - L]$ directly. However, substitute $L = r - i$ where $i = r - L \in \mathcal{I}(u, r)$ is the **invariant left endpoint**:
$$L^m = (r - i)^m = \sum_{t=0}^m \binom{m}{t} (-1)^t r^{m-t} \cdot i^t.$$
Now the factor $i^t$ depends **only on the left endpoint $i$**, which is 100% invariant under the shift $r - d \to r$!
Therefore, maintaining $D + 1$ scalar accumulators at each node $u$:
$$g_t[u] = \bigl(r_{\text{new}}\bigr)^t dp[r_{\text{new}}] + [\text{diff}[u] == \text{diff}[\text{fail}[u]]] \cdot g_t[\text{fail}[u]] \qquad (0 \le t \le D,\; r_{\text{new}} = r - \text{len}[\text{slink}[u]] - \text{diff}[u])$$
evaluates $\sum_{i \in \mathcal{I}(u, r)} (r - i)^m dp[i] = \sum_{t=0}^m \binom{m}{t} (-1)^t r^{m-t} g_t[u]$ in $O(D)$ time per `slink` jump, solving the entire DP in **$O(D \cdot N \log N)$ time** without any segment tree!

---

### 4.4 Frontier Extension 2: Length-Bounded (`L_min <= L <= L_max`) & Parity-Filtered `slink` DP
1. **Parity Filtering on Length $L$**:
   - In `CF 932G`, only even $r$ have $dp[r] \ne 0$, which automatically restricts $L = r - i$ to be even at even $r$.
   - What if both odd and even $r$ are active, and we only want **even-length** (or only **odd-length**) palindromes $L$?
   - If $\text{diff}[u]$ is **even**, all lengths in $(\text{slink}[u], u]$ have the same parity as $\text{len}[u]$. If $\text{diff}[u]$ is **odd**, lengths in $(\text{slink}[u], u]$ alternate parity, and correspondingly their left endpoints $i = r - L$ alternate parity! Thus maintaining two accumulators $g_{\text{even\_i}}[u]$ and $g_{\text{odd\_i}}[u]$ partitioned by the parity of the left endpoint $i$ handles arbitrary length-parity constraints in $O(1)$ per `slink` jump!
2. **Minimum/Maximum Length Window $L \in [L_{\min}, L_{\max}]$**:
   - Because $L = r - i$, the constraint $L_{\min} \le L \le L_{\max}$ is equivalent to $r - L_{\max} \le i \le r - L_{\min}$ on left endpoints $i \in \mathcal{I}(u, r)$.
   - Since each `slink` chain $(\text{slink}[u], u]$ inserts one new left endpoint $i_{\text{new}} = r - \text{len}[\text{slink}[u]] - \text{diff}[u]$ at the **right end** of $\mathcal{I}(u, r)$ while the **leftmost** endpoint in $\mathcal{I}(u, r)$ is $i_{\text{old}} = r - \text{len}[u]$, the elements of $\mathcal{I}(u, r)$ form a sliding window in strictly increasing order of $i$, which can be maintained via a persistent/deque structure or queried on the PAM fail tree.

---

## Section 5. Master Atlas of Boundary Pitfalls & Broken-Invariant Counterexamples

| Pitfall ID | Category | The Broken Shortcut / Bug | Exact Counterexample & Structural Fix |
| :--- | :--- | :--- | :--- |
| **BP-1A-01** | Fine–Wilf | Using $N \ge p + q$ instead of $N \ge p + q - \gcd(p, q)$, or replacing $(p, q)$ by $\gcd(p, q)$ when $N < p + q - \gcd(p, q)$. | For $(p, q) = (4, 6)$, $g = 2$ and threshold is $4 + 6 - 2 = 8$. At $N = 7$, `abaaaba` has periods $4$ and $6$ but not $2$ ($S[2]=\texttt{b} \ne \texttt{a}=S[4]$), with $p + q - N = 3$ components instead of $2$. |
| **BP-1A-02** | Period–Border | Assuming a period $p \in \text{Per}(S)$ must divide $|S|$ ($p \mid |S|$). | In `abaab` ($N=5$), $b=3$ (`aba`) is a valid border and $p = 5 - 3 = 2$ is a valid weak period even though $2 \nmid 5$. Check $(N - \pi[N]) \mid N$ **only** when testing exact repetitions $w^k$. |
| **BP-1A-03** | Border APs | Including $\text{slink}[u]$ as a closed interval $[\text{slink}[u], u]$ in counting/sum DPs. | Since $\text{len}[v_c] - \text{len}[\text{slink}[u]] = \text{diff}[u]$, node $\text{slink}[u]$ sits at distance $d$ below $v_c$ AND starts the next AP chain. Always use the **half-open** interval $(\text{slink}[u], u]$ with shortest length $\text{len}[\text{slink}[u]] + \text{diff}[u]$. |
| **BP-1A-04** | `[WC2016]` Knapsack | Unrolling a $+d \pmod x$ cycle from an arbitrary residue instead of $v_0 = \arg\min D[v]$. | Starting at a non-minimum vertex misses shortest paths that wrap past index $0$. Rotating to $v_0 = \arg\min D[v]$ turns the cycle into a DAG because all weights $x + j d > 0$ are strictly positive. |
| **BP-1A-05** | `[WC2016]` Knapsack | Pushing the *old* $D[v_t] - t \cdot d$ into the monotonic queue before updating $D[v_t]$ from `dq.front()`. | Multiple borders from the same AP block $\mathcal{A}_k$ can be used together (complete/unbounded knapsack). You must update $D[v_t]$ from `dq.front()` *first*, then push the updated $D[v_t] - t \cdot d$ into `dq`. |
| **BP-1A-06** | `slink` DP | Writing `dp[r - len[u]]` instead of `dp[r - len[slink[u]] - diff[u]]` for the new element entering $g[u]$. | On `T = aaaa` ($r=4, \text{len}[u]=4, d=1, \text{slink}[u]=0$), $\mathcal{I}(u, 4) = \{0, 1, 2, 3\}$ and $\mathcal{I}(\text{fail}[u], 3) = \{0, 1, 2\}$. The index $r - \text{len}[u] = 0$ is the **oldest** index (already in $g[\text{fail}[u]]$); the **newest** index is $4 - 0 - 1 = 3$! |
| **BP-1A-07** | `slink` DP | Skipping `slink` updates of $g[u]$ at odd indices $r$ in `CF 932G` / `CF 906E`. | On `T = aaaaaa` ($r=4$), $u = \texttt{aaaa}$ ($\text{len}=4$, even) has $\text{fail}[u] = \texttt{aaa}$ ($\text{len}=3$, odd) and $\text{diff}[u] = 1$ (odd), so $g[u]$ at $r = 4$ reads $g[\text{fail}[u]]$ from $r - 1 = 3$ (odd)! Always update $g[u]$ at **every** $r$; only gate `dp[r]` on $2 \mid r$. |
| **BP-1A-08** | Online Borders | Walking raw $\pi[u]$ to delete mismatched borders in `CF 1286E` without `anc[u]`. | On $S = \texttt{a}^N$, walking $\pi[u]$ visits $O(N)$ surviving borders at every step ($\Theta(N^2)$). Jumping via $\text{anc}[u]$ skips all borders with $S[v+1] == S[i]$ in $O(1)$, amortizing deletions to $O(N)$ total. |

---

## Section 6. Master Reconciled Wave 1A Problem Archive (42 Accepted Problems + 13 Quarantined Templates)

### 6.1 Complete Deduplicated Master Matrix (`W1A-01` – `W1A-42`)

All problems from Cohort 1 (`P-1A-01..32`) and Cohort 2 (`1A-01..32`) have been reconciled, deduplicated, and organized into a smooth 4-tier difficulty ladder:
- **Tier 1 — Stepping Stone (`W1A-01` – `W1A-10`, 10 problems)**: Period–Border Duality, fail-tree geometry, and basic palindromic borders.
- **Tier 2 — Intermediate (`W1A-11` – `W1A-21`, 11 problems)**: Weak Periodicity pruning, Fine–Wilf sub-threshold orbits, PAM half-links (`trans`/`half`), and KMP `slink` transition jumps.
- **Tier 3 — Advanced (`W1A-22` – `W1A-32`, 11 problems)**: PAM/KMP `slink` DP, `[WC2016]` Border-Group Modulo Shortest Path, SPF exact-period queries, and cyclic borders.
- **Tier 4 — Mastery (`W1A-33` – `W1A-42`, 10 problems)**: Internal Border AP queries (`[BJWC2018]`), online border death amortization (`CF 1286E`), harmonic square AP sweeps (`[NOI2016]`), inverse KMP via `slink`, and huge-length Fine–Wilf word equations.

| Master ID | Tier | Problem Name & Judge IDs | Lang | Cohort Origin | Core Structural Invariant & Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **W1A-01** | Stepping Stone | **[BOI 2009] Radio Transmission (`Luogu P4391` / `BZOJ 1355`)** | `[EN]`/`[ZH]` | Cohort 2 (`1A-01`) | Minimum weak period $p_{\min} = N - \pi[N]$ via Period–Border Duality, $O(N)$ |
| **W1A-02** | Stepping Stone | **[NOI 2014] 动物园 (`Luogu P2375`)** | `[ZH]` | Both (`P-1A-01` / `1A-03`) | Persistent half-length KMP pointer $2j \le i$ + fail-tree depth, $O(N)$ |
| **W1A-03** | Stepping Stone | **CF 126B — Password** | `[EN]` | Both (`P-1A-02` / `1A-04`) | Internal border occurrence check ($\pi[N] \le \max_{2..N-1}\pi[i]$ else $\pi[\pi[N]]$), $O(N)$ |
| **W1A-04** | Stepping Stone | **[POI XII / 2005] Template (`Szablon` / `Luogu P3426`)** | `[EN]`/`[ZH]` | Both (`P-1A-03` / `1A-07`) | KMP fail-tree cover DP ($dp[i] \in \{i, dp[\pi[i]]\}$) via gap invariant, $O(N)$ |
| **W1A-05** | Stepping Stone | **[POI XIII / 2006] Periods of Words (`Okresy słów` / `Luogu P3435`)** | `[EN]`/`[ZH]` | Both (`P-1A-04` / `1A-02`) | Maximum period $\leftrightarrow$ minimum positive border $b_{\min} \le i/2$ path compression, $O(N)$ |
| **W1A-06** | Stepping Stone | **CF 432D — Prefixes and Suffixes** | `[EN]` | Both (`P-1A-05` / `1A-05`) | Reverse-index bottom-up subtree sum on KMP fail tree for border counts, $O(N)$ |
| **W1A-07** | Stepping Stone | **[SHOI 2011 / JSOI 2012] 双倍回文 (`Luogu P4287`)** | `[ZH]` | Both (`P-1A-06` / `1A-30`) | Palindromic border equivalence: $4 \mid \text{len}[u]$ and $\text{len}[\text{trans}[u]] = \text{len}[u]/2$, $O(N)$ |
| **W1A-08** | Stepping Stone | **CF 1200E — Compress Words** | `[EN]` | Both (`P-1A-07` / `1A-13`) | Bounded-window suffix-prefix KMP on $W_i + \texttt{\#} + R[\text{tail}]$, $O(\sum |W_i|)$ |
| **W1A-09** | Stepping Stone | **AtCoder ABC 284 F — ABCBAC** | `[JA]` | Both (`P-1A-08` / `1A-23`) | Bidirectional Z-array prefix/suffix split alignment with $S^R$, $O(N)$ |
| **W1A-10** | Stepping Stone | **CF 1137B — Camp Schedule** | `[EN]` | Both (`P-1A-10` / `1A-14`) | Maximum packing density via minimum-period suffix cycling $T[\pi[|T|]+1..|T|]$, $O(N)$ |
| **W1A-11** | Intermediate | **CF 535D — Tavas and Malekas** | `[EN]` | Cohort 1 (`P-1A-09`) | Adjacent overlap compatibility via border membership + transitive closure, $O(N+M)$ |
| **W1A-12** | Intermediate | **AtCoder ARC 060 F (ABC 044 D) — Best Representation** | `[JA]` | Both (`P-1A-11` / `1A-08`) | Weak Periodicity Lemma proof that $\le 2$ aperiodic parts always suffice unless $S=\texttt{a}^N$, $O(N)$ |
| **W1A-13** | Intermediate | **Universal Cup / QOJ — Fine–Wilf Sub-Threshold Component Count** | `[EN]`/`[ZH]` | Cohort 2 (`1A-09`) | Closed-form orbit count $\gcd(p, q)$ vs. $p + q - N$ below Fine–Wilf threshold, $O(\log(\min(p,q)))$ |
| **W1A-14** | Intermediate | **CF 808G — Anthem of Berland** | `[EN]` | Both (`P-1A-12` / `1A-10`) | Wildcard pattern matching DP compressed via border-reset transitions, $O(|S|\cdot|T|)$ |
| **W1A-15** | Intermediate | **HDU 6599 — I Love Palindrome String** | `[ZH]` | Both (`P-1A-13` / `1A-12`) | PAM fail-tree occurrence sum + half-border check $\text{len}[\text{trans}[u]] = \lceil \ell/2 \rceil$, $O(N)$ |
| **W1A-16** | Intermediate | **[CERC 2014] Virus Synthesis (`Luogu P4762` / `UVA 1673`)** | `[EN]`/`[ZH]` | Both (`P-1A-14` / `1A-11`) | Even-node PAM BFS DP over Trie parent + half-link `trans[u]` doubling, $O(N)$ |
| **W1A-17** | Intermediate | **CF 17E — Palisection** | `[EN]` | Cohort 1 (`P-1A-15`) | Overlapping palindrome pairs via PAM fail-depth / Manacher + complement sweep, $O(N)$ |
| **W1A-18** | Intermediate | **AtCoder AGC 047 B — First Second** | `[JA]` | Both (`P-1A-16` / `1A-15`) | Reversed Suffix Trie + prefix character-bitmask border matching, $O(\sum |S_i| |\Sigma|)$ |
| **W1A-19** | Intermediate | **CF 1721E — Prefix Function Queries** | `[EN]` | Cohort 2 (`1A-16`) | Appended KMP queries via `slink[u]` constant-period next-character skip, $O(N + Q m \log N)$ |
| **W1A-20** | Intermediate | **CF 149E — Martian Strings** | `[EN]` | Cohort 2 (`1A-21`) | Disjoint split matching via forward/reverse KMP earliest-end $L[k]$ and latest-start $R[k+1]$, $O(M(N+|P|))$ |
| **W1A-21** | Intermediate | **CF 615C — Running Track** | `[EN]` | Cohort 2 (`1A-22`) | Hereditary greedy right-extension interval cover via Z/KMP on $S$ and $S^R$, $O(NM)$ / $O(N+M)$ |
| **W1A-22** | Advanced | **CF 932G — Palindrome Partition** | `[EN]` | Both (`P-1A-17` / `1A-17`) | Double-end interleaving $T$ + PAM `slink` even-palindrome partition DP, $O(N \log N)$ |
| **W1A-23** | Advanced | **CF 906E — Reverses** | `[EN]` | Both (`P-1A-18` / `1A-18`) | Interleaving $A, B$ + min-cost PAM `slink` DP with argmin path reconstruction, $O(N \log N)$ |
| **W1A-24** | Advanced | **[WC 2016] 论战捆竹竿 (`Luogu P4156` / `UOJ 179` / `LOJ 2085`)** | `[ZH]` | Both (`P-1A-19` / `1A-19`) | Border AP decomposition + dynamic modulus switch + residue-cycle monotonic queue, $O(N \log N)$ |
| **W1A-25** | Advanced | **[SDOI 2019] 连续子序列 (`Luogu P5328` / `P5346` / `LOJ 3113`)** | `[ZH]` | Both (`P-1A-20` / `1A-20`) | Periodic border AP / Thue–Morse parity decimation & `slink` recurrence, $O(N \log N)$ |
| **W1A-26** | Advanced | **CF 1051E — Vasya and Big Integers** | `[EN]` | Cohort 1 (`P-1A-21`) | Z-array first-mismatch lexicographical clipping + range-sum partition DP, $O(N)$ |
| **W1A-27** | Advanced | **AtCoder AGC 032 F — One Third** | `[JA]` | Cohort 1 (`P-1A-22`) | Mod-$1/3$ periodic folding + 3-color bichromatic gap order-statistic integral, $O(N)$ |
| **W1A-28** | Advanced | **[POI XVI / 2009] Quasi-Template / PRE-Prefixuffix (`Luogu P3546`)** | `[EN]`/`[ZH]` | Both (`P-1A-23` / `1A-24a`) | Cyclic border $A B \sim B A$ decomposition + amortized inner border $f(i) \le f(i+1)+2$, $O(N)$ |
| **W1A-29** | Advanced | **[POI XIX / 2012] OKR-A Horrible Poem (`Luogu P3538`)** | `[EN]`/`[ZH]` | Cohort 2 (`1A-24b`) | Substring minimum exact period via SPF prime-factor trial + Weak Periodicity GCD closure, $O(Q \log N)$ |
| **W1A-30** | Advanced | **CF 526D — Om Nom and Necklace** | `[EN]` | Both (`P-1A-24` / `1A-06`) | Tandem-repeat + tail $(AB)^k A$ characterization via $p_{\min} = i - \pi[i]$ quotient arithmetic, $O(N)$ |
| **W1A-31** | Advanced | **[THUPC 2018] 绿绿和串串 (`Luogu P5446`)** | `[ZH]` | Cohort 2 (`1A-29`) | Prefix mirror-flipping restoration via backwards Manacher boundary-reachability DP, $O(N)$ |
| **W1A-32** | Advanced | **Luogu P5555 — 秩序魔咒 (Common Palindromes on Dual PAMs)** | `[ZH]` | Cohort 2 (`1A-27`) | Simultaneous Trie DFS over even/odd roots of $\text{PAM}(S) \times \text{PAM}(T)$ + fail-subtree sums, $O(|S|+|T|)$ |
| **W1A-33** | Mastery | **[BJWC 2018] Border 的四种求法 (`Luogu P4482` / `LOJ 2541`)** | `[ZH]` | Both (`P-1A-25` / `1A-25`) | Substring $S[l..r]$ longest border via dyadic Weak Periodicity APs / SAM Link-Tree HLD + 2D range query, $O((N+Q)\log^2 N)$ |
| **W1A-34** | Mastery | **CF 1286E — Fedya the Potter Strikes Back** | `[EN]` | Both (`P-1A-27` / `1A-32`) | Online encrypted border min-weight sum via `anc[u]` mismatch link + monotonic stack map + `__int128`, $O(N \log N)$ |
| **W1A-35** | Mastery | **[NOI 2016] 优秀的拆分 (`UOJ #219` / `Luogu P1117`)** | `[ZH]` | Cohort 1 (`P-1A-29`) | $A A B B$ counting via harmonic $O(N \log N)$ LCE anchor grid + square AP difference arrays, $O(N \log N)$ |
| **W1A-36** | Mastery | **CF 1043G — Speckled Band** | `[EN]` | Cohort 2 (`1A-26`) | Substring partition block-frequency minimization ($\le 4$ bound) via exact periods, borders & squares, $O((N+Q)\log N)$ |
| **W1A-37** | Mastery | **QOJ / UCup — Substring & Length-Bounded Palindrome Partition (`slink`)** | `[EN]`/`[ZH]` | Both (`P-1A-26` / `1A-28`) | Clipping PAM `slink` AP chains to $L \in [L_{\min}, r-l+1]$ via left-endpoint monotonicity, $O((N+Q)\log N)$ |
| **W1A-38** | Mastery | **LOJ #6681 / Ynoi — Substring Period & Border AP Polynomial Sums** | `[ZH]` | Cohort 1 (`P-1A-30`) | Extracting $O(\log(r-l))$ border AP descriptors $(x_k, d_k, c_k)$ on $S[l..r]$ via dyadic IPM, $O(Q \log N)$ |
| **W1A-39** | Mastery | **CF 1764G / UCup — Inverse KMP & Border-Set Realizability via `slink`** | `[EN]`/`[JA]` | Cohort 2 (`1A-31`) | Collecting the $\le \log_2 i$ forbidden next characters along KMP fail chain via Theorem 2.6 (`slink`), $O(N \log N)$ |
| **W1A-40** | Mastery | **AtCoder AGC 055 D — ABC Ultimatum / Periodic Shift Counting** | `[JA]` | Cohort 1 (`P-1A-28`) | Multi-shift periodic constraint dualization into prefix-excess minimums, $O(N^4)$ / polynomial DP |
| **W1A-41** | Mastery | **ICPC WF / UCup — Huge-Length Fine–Wilf Word Equations ($N \le 10^{18}$)** | `[EN]` | Cohort 1 (`P-1A-31`) | Interval sweep-line + Fine–Wilf threshold $p+q-\gcd(p,q)$ period contraction on $N \le 10^{18}$ |
| **W1A-42** | Mastery | **CF 1608F / Grandmaster Palindromic `slink` + Segment Tree Range Coupling** | `[EN]` | Cohort 1 (`P-1A-32`) | Coupling PAM `slink` AP left-endpoint accumulators with lazy segment tree range updates, $O(N \log^2 N)$ |

---

### 6.2 Reconciled 4-Step Zero-Magic Analyses Across All Four Tiers

#### Tier 1: Stepping Stone (`W1A-01` – `W1A-10`)

- **`W1A-01`: `[BOI 2009] Radio Transmission` (`Luogu P4391`)** `[EN]`/`[ZH]`
  1. *Diagnostic Signal*: Testing candidate period lengths $p \in [1, N]$ by character comparison takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: $S[1..N]$ is a prefix of $T^\infty$ with $|T| = p \iff p \in \text{Per}(S) \iff b = N - p \in \text{Border}(S)$.
  3. *Reverse-Engineering Scratchpad*: Minimize $p = N - b$ by maximizing $b \in \text{Border}(S)$: output $N - \pi[N]$ in $O(N)$ time.
  4. *Boundary Pitfall*: Do not require $(N - \pi[N]) \mid N$; $S$ is a truncated prefix of $T^\infty$.

- **`W1A-02`: `[NOI 2014] 动物园` (`Luogu P2375`)** `[ZH]`
  1. *Diagnostic Signal*: Walking $\pi[i]$ down until $b \le i/2$ at each step $i$ takes $\Theta(N^2)$ on `a^N`.
  2. *Combinatorial Word Invariant*: In the KMP fail tree, node depth $dep[u] = dep[\pi[u]] + 1$ counts positive borders of $S[1..u]$. The longest border $j_i \le i/2$ of $S[1..i]$ satisfies $j_{i} \le j_{i-1} + 1$.
  3. *Reverse-Engineering Scratchpad*: Maintain a persistent KMP pointer $j$ across $i = 1 \dots N$; after advancing $j$ with $S[i]$, step $j \leftarrow \pi[j]$ while $2j > i$, and multiply answer by $(dep[j] + 1)$ in $O(N)$ time.
  4. *Boundary Pitfall*: Never reset $j = \pi[i]$ at step $i$, and enforce $2j \le i$ *after* matching $S[j+1] == S[i]$.

- **`W1A-03`: `CF 126B — Password`** `[EN]`
  1. *Diagnostic Signal*: Searching for each border of $S[1..N]$ inside $S[2..N-1]$ naively takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: Border $b$ of $S[1..N]$ occurs ending at some $i \in [2, N-1] \iff b \le \max_{2 \le i \le N-1} \pi[i]$. Moreover, $\pi[\pi[N]]$ always occurs ending at $\pi[N] \le N-1$.
  3. *Reverse-Engineering Scratchpad*: Let $M = \max_{2 \le i \le N-1} \pi[i]$. Output $\pi[N]$ if $\pi[N] \le M$, else $\pi[\pi[N]]$ (or `"Just a legend"` if $0$). Time: $O(N)$.
  4. *Boundary Pitfall*: Thinking one needs to check $\pi^{(3)}[N]$ when $\pi[N] > M$; $\pi[\pi[N]]$ is guaranteed $\le \pi[N]-1$ and occurs at index $i = \pi[N] \in [1, N-1]$.

- **`W1A-04`: `[POI XII] Template (`Szablon` / `Luogu P3426`)`** `[EN]`/`[ZH]`
  1. *Diagnostic Signal*: Testing every border of $S$ as a cover template takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: Any template covering $S[1..i]$ must be a border of $S[1..i]$, so $dp[i] \in \{i, dp[\pi[i]]\}$. Specifically, $dp[i] = dp[\pi[i]]$ iff $S[1..dp[\pi[i]]]$ covers $S[1..i]$, which holds iff there is a previous prefix $j \ge i - \pi[i]$ with $dp[j] = dp[\pi[i]]$.
  3. *Reverse-Engineering Scratchpad*: Track `last_end[x]` = largest $j < i$ with $dp[j] = x$. Set $dp[i] = dp[\pi[i]]$ if `last_end[dp[pi[i]]] >= i - pi[i]`, else $dp[i] = i$. Time: $O(N)$.
  4. *Boundary Pitfall*: Checking `last_end >= i - dp[pi[i]]` instead of `i - pi[i]` (since $S[i-\pi[i]+1..i] = S[1..\pi[i]]$ is already covered by $dp[\pi[i]]$!).

- **`W1A-05`: `[POI XIII] Periods of Words (`Okresy słów` / `Luogu P3435`)`** `[EN]`/`[ZH]`
  1. *Diagnostic Signal*: Walking down to the shortest positive border of $S[1..i]$ for every $i$ takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: By Period–Border Duality, the maximum period $p_i = i - b_i$ corresponds to the **minimum positive border** $b_{\min}(i)$ in the KMP fail tree, which automatically satisfies $b_{\min}(i) \le i/2$ (by Theorem 2.3).
  3. *Reverse-Engineering Scratchpad*: Path-compress `min_b[i] = (pi[i] == 0 ? i : min_b[pi[i]])` and sum $i - \text{min\_b}[\pi[i]]$ over all $i$ with $\pi[i] > 0$. Time: $O(N)$.
  4. *Boundary Pitfall*: Adding binary lifting to enforce $b \le i/2$; the shortest positive border of any prefix with $\pi[i] > 0$ is *always* $\le i/2$.

- **`W1A-06`: `CF 432D — Prefixes and Suffixes`** `[EN]`
  1. *Diagnostic Signal*: Counting occurrences of each border independently takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: $S[1..b]$ occurs ending at $i \iff b$ is an ancestor of $i$ in the KMP fail tree.
  3. *Reverse-Engineering Scratchpad*: Initialize `cnt[1..N] = 1`, loop $i = N \dots 1$ setting `cnt[pi[i]] += cnt[i]`, and output $(b, \text{cnt}[b])$ along the fail chain of $N$. Time: $O(N)$.
  4. *Boundary Pitfall*: Iterating $1 \to N$ instead of reverse topological order $N \to 1$.

- **`W1A-07`: `[SHOI 2011 / JSOI 2012] 双倍回文` (`Luogu P4287`)** `[ZH]`
  1. *Diagnostic Signal*: Checking all palindromic substrings for $W W^R W W^R$ structure takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: By Theorem 2.5, a palindrome $Q$ of length $4k$ equals $W W^R W W^R \iff Q$ has a palindromic border of length $2k = |Q|/2$.
  3. *Reverse-Engineering Scratchpad*: Maintain the PAM half-link `trans[u]` ($\text{len}[\text{trans}[u]] \le \text{len}[u]/2$) during PAM construction; maximize $\text{len}[u]$ over nodes with $4 \mid \text{len}[u]$ and $\text{len}[\text{trans}[u]] == \text{len}[u]/2$. Time: $O(N)$.
  4. *Boundary Pitfall*: Checking $2 \mid \text{len}[u]$ instead of $4 \mid \text{len}[u]$ (`abaaba` has length $6$ and palindromic half `aba`, which is $W W$ with $W = W^R$, not $X X^R X X^R$).

- **`W1A-08`: `CF 1200E — Compress Words`** `[EN]`
  1. *Diagnostic Signal*: Running KMP on the full accumulated string $R$ at step $i$ takes $O(|R|) = O(\sum_{j \le i} |W_j|)$, giving $O(N^2)$ total time.
  2. *Combinatorial Word Invariant*: Any border overlap between $R$ and $W_i$ has length $\le m = \min(|R|, |W_i|)$.
  3. *Reverse-Engineering Scratchpad*: Run KMP on $W_i + \texttt{\#} + R[|R|-m+1..|R|]$ of length $\le 2|W_i| + 1$ in $O(|W_i|)$ time. Total time: $O(\sum |W_i|)$.
  4. *Boundary Pitfall*: Omitting the delimiter `\texttt{#}`, which allows overlaps $> |W_i|$.

- **`W1A-09`: `AtCoder ABC 284 F — ABCBAC`** `[JA]`
  1. *Diagnostic Signal*: Testing each split $i \in [0, N]$ by string slicing takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: $T = S[1..i] + S^R + S[i+1..N] \iff$ the prefix of $T[1..N]$ of length $i$ matches the reversed suffix of $T[N+1..2N]$, and the suffix of $T[1..N]$ of length $N-i$ matches the reversed prefix of $T[N+1..2N]$.
  3. *Reverse-Engineering Scratchpad*: Compute two Z-arrays on $A + \texttt{\#} + B$ and $A^R + \texttt{\#} + B^R$ (where $A = T[1..N], B = (T[N+1..2N])^R$) in $O(N)$ time.
  4. *Boundary Pitfall*: Guard $i = 0$ and $i = N$ against out-of-bounds Z-array lookups.

- **`W1A-10`: `CF 1137B — Camp Schedule`** `[EN]`
  1. *Diagnostic Signal*: Non-overlapping placement of $T$ misses self-overlaps.
  2. *Combinatorial Word Invariant*: Maximum overlap between consecutive copies of $T$ is $\pi[|T|]$, advancing by minimum period $p_{\min} = |T| - \pi[|T|]$.
  3. *Reverse-Engineering Scratchpad*: Emit $T$ once, then greedily emit $T[\pi[|T|]+1..|T|]$ while `0`/`1` counts allow. Time: $O(|S| + |T|)$.
  4. *Boundary Pitfall*: Handle the case where $S$ cannot form even one copy of $T$.

---

#### Tier 2: Intermediate (`W1A-11` – `W1A-21`)

- **`W1A-11`: `CF 535D — Tavas and Malekas`** `[EN]`
  1. *Diagnostic Signal*: Copying $P[1..M]$ into $S[1..N]$ at each $y_j$ takes $O(k M) = O(N^2)$.
  2. *Combinatorial Word Invariant*: Adjacent overlapping placements $y_{j-1}, y_j$ ($d = y_j - y_{j-1} < M$) are compatible $\iff M - d \in \text{Border}(P)$ ($d \in \text{Per}(P)$). By additive closure of periods on the overlap, adjacent compatibility implies global compatibility!
  3. *Reverse-Engineering Scratchpad*: Mark `is_border[b]` along the fail chain of $M$ on $P$, verify $M - (y_j - y_{j-1})$ for all adjacent overlaps, and output $26^{\text{free\_cells}} \bmod (10^9+7)$. Time: $O(N + M)$.
  4. *Boundary Pitfall*: Checking non-adjacent overlaps is redundant once adjacent overlaps pass.

- **`W1A-12`: `AtCoder ARC 060 F (ABC 044 D) — Best Representation`** `[JA]`
  1. *Diagnostic Signal*: Full partition DP over aperiodic substrings takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: By the Weak Periodicity Lemma, if $S$ is periodic with minimum period $p \ge 2$ ($p \mid N$), then $S[2..N]$ of length $N-1$ **cannot** have any proper exact period $q \mid (N-1)$ (otherwise $p + q \le N/2 + (N-1)/2 \le N - 1 \implies \gcd(p, q) = 1 \in \text{Per}(S[2..N]) \implies S = \texttt{a}^N$, contradiction!). Thus the minimum number of pieces is **at most $2$** (unless $S = \texttt{a}^N$, where it is $N$).
  3. *Reverse-Engineering Scratchpad*: Run KMP on $S$ and $S^R$ to mark periodic prefixes and suffixes ($d = L - \pi[L] < L$ and $d \mid L$), then count valid 2-piece splits $k \in [1, N-1]$ in $O(N)$.
  4. *Boundary Pitfall*: A string is periodic ("bad") iff $(L - \pi[L]) \mid L$ and $\pi[L] > 0$; fractional periods do not make a string bad.

- **`W1A-13`: `Universal Cup / QOJ — Fine–Wilf Sub-Threshold Component Count`** `[EN]`/`[ZH]`
  1. *Diagnostic Signal*: Explicit DSU on $N \le 10^{12}$ with periods $p, q$ TLEs/MLEs.
  2. *Combinatorial Word Invariant*: By Theorem 2.2 (Proof II), for $\max(p, q) \le N < p + q - \gcd(p, q)$, each missing index in $[N+1, p+q-\gcd(p,q)]$ cuts exactly one non-bridge cycle edge in the residue graph, yielding **exactly $p + q - N$ connected components**.
  3. *Reverse-Engineering Scratchpad*: Output $\gcd(p, q)$ if $N \ge p + q - \gcd(p, q)$, and $p + q - N$ if $\max(p, q) \le N < p + q - \gcd(p, q)$. Time: $O(\log \min(p, q))$.
  4. *Boundary Pitfall*: When $N < \max(p, q)$ (say $p \le N < q$), period $q$ imposes zero edges, so the number of components is simply $p$.

- **`W1A-14`: `CF 808G — Anthem of Berland`** `[EN]`
  1. *Diagnostic Signal*: $O(|S| \cdot |T| \cdot |\Sigma|)$ KMP-automaton DP TLEs when $|S| \cdot |T| = 10^7$ and $|\Sigma| = 26$.
  2. *Combinatorial Word Invariant*: Two DP arrays $f[i]$ (best in $S[1..i]$) and $g[i]$ (best in $S[1..i]$ ending with a match of $T$ at $i$) transition via $g[i] = 1 + \max(f[i-|T|], \max_{b \in \text{Border}(T)} g[i - |T| + b])$ whenever $T$ matches $S[i-|T|+1..i]$.
  3. *Reverse-Engineering Scratchpad*: Either use the border-transition DP in $O(|S| \cdot |\text{Border}(T)|)$ / `slink` $O(|S| \log |T|)$ or flattened 1D KMP automaton.
  4. *Boundary Pitfall*: Gate $g[i]$ transitions on $S[i-|T|+1..i]$ actually matching $T$ under `?` wildcards.

- **`W1A-15`: `HDU 6599 — I Love Palindrome String`** `[ZH]`
  1. *Diagnostic Signal*: Checking each palindrome's half-prefix via naive scanning takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: By Theorem 2.5, for any PAM node $u$ of length $\ell$, its prefix of length $\lceil \ell/2 \rceil$ is a palindrome iff $u$ has a fail-tree ancestor of length $\lceil \ell/2 \rceil$.
  3. *Reverse-Engineering Scratchpad*: Maintain PAM half-link `trans[u]` for $\le \lceil \text{len}[u]/2 \rceil$, accumulate `cnt[fail[u]] += cnt[u]` bottom-up, and add `cnt[u]` to `ans[len[u]]` when $\text{len}[\text{trans}[u]] == \lceil \text{len}[u]/2 \rceil$. Time: $O(N)$.
  4. *Boundary Pitfall*: Use $\lceil \ell/2 \rceil = (\ell + 1)/2$, not $\lfloor \ell/2 \rfloor$, for odd-length palindromes.

- **`W1A-16`: `[CERC 2014] Virus Synthesis` (`Luogu P4762`)** `[EN]`/`[ZH]`
  1. *Diagnostic Signal*: Doubling $W \to W W^R$ produces only even-length palindromes in PAM.
  2. *Combinatorial Word Invariant*: An even palindrome $u$ in PAM is formed either by flanking its PAM Trie parent $p(u)$ and doubling ($dp[p(u)] + 1$), or by extending its longest palindromic border $\text{trans}[u]$ of length $\le \text{len}[u]/2$ via single-character appends and doubling ($dp[\text{trans}[u]] + \text{len}[u]/2 - \text{len}[\text{trans}[u]] + 1$).
  3. *Reverse-Engineering Scratchpad*: Build PAM with `trans[u]`, run BFS over even PAM nodes, and take $\min_u (dp[u] + N - \text{len}[u])$. Time: $O(N)$.
  4. *Boundary Pitfall*: Never apply the doubling recurrence to odd-length PAM nodes.

- **`W1A-17`: `CF 17E — Palisection`** `[EN]`
  1. *Diagnostic Signal*: Counting overlapping palindrome pairs directly takes $O(N^2)$; 64MB memory forbids `ch[N][26]` PAM tables.
  2. *Combinatorial Word Invariant*: Total pairs $\binom{\text{tot}}{2}$ minus non-overlapping pairs $\sum_{r < l} \text{end}[r] \cdot \text{start}[l]$.
  3. *Reverse-Engineering Scratchpad*: Use Manacher + difference arrays (or linked-list PAM) to compute `end[r]` and `start[l]` in $O(N)$ time and $O(N)$ memory.
  4. *Boundary Pitfall*: Standard `int ch[2000005][26]` uses 208 MB and MLEs the 64 MB limit.

- **`W1A-18`: `AtCoder AGC 047 B — First Second`** `[JA]`
  1. *Diagnostic Signal*: Pairwise reduction checks take $O(N^2)$.
  2. *Combinatorial Word Invariant*: Deleting the 1st or 2nd character reduces $S_i$ to $S_j$ iff $S_j[2..|S_j|]$ is a suffix of $S_i$ and $S_j[1]$ occurs in $S_i[1..|S_i|-|S_j|+1]$.
  3. *Reverse-Engineering Scratchpad*: Insert $S_i^R$ into a Trie, accumulating `cnt[u][c]` for each character $c$ present in the remaining prefix of $S_i$; query $S_j[2..|S_j|]^R$ with $c = S_j[1]$. Time: $O(\sum |S_i| |\Sigma|)$.
  4. *Boundary Pitfall*: Subtract self-pairs $i = j$.

- **`W1A-19`: `CF 1721E — Prefix Function Queries`** `[EN]`
  1. *Diagnostic Signal*: Naive KMP on $S + T$ can walk $O(N)$ fail links per query on $S = \texttt{a}^N, T = \texttt{b}$, taking $O(Q N)$ time.
  2. *Combinatorial Word Invariant*: By Theorem 2.6, inside any constant-period `slink` chain ($\text{diff}[u] = \text{diff}[\pi[u]]$), all strict ancestors share the exact same next character $S[\pi[u]+1] = S[\pi[\pi[u]]+1]$.
  3. *Reverse-Engineering Scratchpad*: Precompute `slink[u]` on $S[1..N]$ (or KMP automaton); during query KMP jumps for $i \in [N+1, N+m]$, if $S[\pi[u]+1] \ne S[i]$ and $\text{diff}[u] == \text{diff}[\pi[u]]$, jump directly to `slink[u]` in $O(\log N)$ steps!
  4. *Boundary Pitfall*: Do not use stale automaton transitions for $u \ge N$ without updating them for $S[N+1..N+m]$.

- **`W1A-20`: `CF 149E — Martian Strings`** `[EN]`
  1. *Diagnostic Signal*: Testing each split $P = A + B$ independently takes $O(|P| \cdot N)$.
  2. *Combinatorial Word Invariant*: $P[1..k]$ and $P[k+1..|P|]$ occur disjointly in $S \iff$ earliest end $L[k]$ of $P[1..k]$ satisfies $L[k] < R[k+1]$ (latest start of $P[k+1..|P|]$).
  3. *Reverse-Engineering Scratchpad*: Compute $L[1..|P|]$ via KMP of $P$ on $S$, and $R[1..|P|]$ via KMP of $P^R$ on $S^R$ in $O(N + |P|)$ per pattern.
  4. *Boundary Pitfall*: Enforce $1 \le k \le |P|-1$ (both pieces non-empty).

- **`W1A-21`: `CF 615C — Running Track`** `[EN]`
  1. *Diagnostic Signal*: $O(M^2)$ DP is unnecessary because substring containment in $S$ or $S^R$ is hereditary.
  2. *Combinatorial Word Invariant*: Greedily choosing the longest prefix of $T[i..M]$ occurring in $S$ or $S^R$ dominates all shorter choices.
  3. *Reverse-Engineering Scratchpad*: At each step, run KMP/Z on $T[i..M] + \texttt{\#} + S + \texttt{\$} + S^R$ (or query SAM of $S$ and $S^R$) to jump to $i + L_{\max}$.
  4. *Boundary Pitfall*: Output reversed 1-based indices $(n - l + 1, n - r + 1)$ when the match comes from $S^R$.

---

#### Tier 3: Advanced (`W1A-22` – `W1A-32`)

- **`W1A-22`: `CF 932G — Palindrome Partition`** `[EN]`
  1. *Diagnostic Signal*: Symmetric partition $w_i = w_{k+1-i}$ couples both ends of $S$, and $O(N^2)$ DP TLEs at $N = 10^6$.
  2. *Combinatorial Word Invariant*: Interleaving $T = S[1]S[N]S[2]S[N-1]\dots$ bijects symmetric partitions of $S$ onto partitions of $T$ into even-length palindromes. By Theorem 4.1, `slink` chains maintain $g[u]$ in $O(1)$ per chain.
  3. *Reverse-Engineering Scratchpad*: Run PAM + `slink` DP on $T[1..N]$ (Section 4.2), updating $g[u]$ at all $r$ and adding $g[u]$ to $dp[r]$ at even $r$. Time: $O(N \log N)$.
  4. *Boundary Pitfall*: Never skip updating $g[u]$ at odd $r$ (Pitfall `BP-1A-07`).

- **`W1A-23`: `CF 906E — Reverses`** `[EN]`
  1. *Diagnostic Signal*: Minimum disjoint interval reversals on $A, B$ ($n \le 5 \times 10^5$) with interval reconstruction.
  2. *Combinatorial Word Invariant*: Interleave $T = A[1]B[1]A[2]B[2]\dots A[n]B[n]$; $A[l..r]^R = B[l..r] \iff T[2l-1..2r]$ is an even palindrome.
  3. *Reverse-Engineering Scratchpad*: Maintain `pair<int,int> g[u]` = `(min_cost, argmin_index)` along PAM `slink` chains; allow 0-cost step-2 transitions when $T[2i-1] == T[2i]$. Time: $O(N \log N)$.
  4. *Boundary Pitfall*: Store raw `dp` costs inside `g[u]` and add $+1$ only when relaxing `dp[r]` from `g[u]`.

- **`W1A-24`: `[WC 2016] 论战捆竹竿` (`Luogu P4156` / `UOJ 179`)** `[ZH]`
  1. *Diagnostic Signal*: Frobenius modulo shortest path with $\Theta(N)$ border weights takes $\Theta(N^2)$.
  2. *Combinatorial Word Invariant*: Extension periods $N - b$ partition into $\le \lceil \log_2 N \rceil$ APs $\mathcal{A}_k = \{x_k + j d_k : 0 \le j \le c_k\}$.
  3. *Reverse-Engineering Scratchpad*: For each AP, switch modulus $m_{\text{old}} \to x_k$ via $\gcd(m_{\text{old}}, x_k)$ cycles (Subroutine A) and relax $+d_k \pmod{x_k}$ cycles from $\arg\min D[v]$ using a sliding-window monotonic deque of width $c_k$ (Subroutine B, Section 3.2). Time: $O(N \log N)$.
  4. *Boundary Pitfall*: Unroll each cycle from $\arg\min D[v]$ (`BP-1A-04`) and push updated $D[v_t]$ into the deque (`BP-1A-05`).

- **`W1A-25`: `[SDOI 2019] 连续子序列` (`Luogu P5328` / `P5346` / `LOJ 3113`)** `[ZH]`
  1. *Diagnostic Signal*: Counting/optimizing over periodic border chains or Thue–Morse extensions takes $O(N^2)$ naively.
  2. *Combinatorial Word Invariant*: Combine KMP `slink` AP aggregation ($\mathcal{I}(u, r) = \mathcal{I}(\pi[u], r - d) \sqcup \{r - \text{len}[\text{slink}[u]] - d\}$) and parity-pair decimation ($01 \to 0, 10 \to 1$).
  3. *Reverse-Engineering Scratchpad*: Maintain affine/weighted `slink` accumulators (or memoized recursive decimation for huge lengths) in $O(N \log N)$.
  4. *Boundary Pitfall*: Handle short base strings ($|S| \le 3$) where two parity alignments coexist.

- **`W1A-26`: `CF 1051E — Vasya and Big Integers`** `[EN]`
  1. *Diagnostic Signal*: Comparing substring $A[i..j]$ against $L$ and $R$ at boundary lengths $|L|, |R|$ takes $O(|A| \cdot |L|)$ naively.
  2. *Combinatorial Word Invariant*: $A[i..i+|L|-1] \ge L \iff$ at $k = \text{LCP}(A[i..], L)$, either $k = |L|$ or $A[i+k] > L[1+k]$.
  3. *Reverse-Engineering Scratchpad*: Precompute Z-arrays on $L + \texttt{\#} + A$ and $R + \texttt{\#} + A$ for $O(1)$ boundary checks; accumulate $dp$ via suffix sums in $O(|A| + |L| + |R|)$.
  4. *Boundary Pitfall*: `"0"` is a valid 1-digit number if $L = \text{"0"}$, but `"0..."` of length $\ge 2$ is forbidden.

- **`W1A-27`: `AtCoder AGC 032 F — One Third`** `[JA]`
  1. *Diagnostic Signal*: Continuous circle cuts require periodic folding modulo $1/3$.
  2. *Combinatorial Word Invariant*: Folding $[0, 1)$ modulo $1/3$ into $[0, 1/3)$ with 3 colors $\{0, 1, 2\}$ reduces the closest arc sum to $1/3$ to the minimum bichromatic gap among $N+1$ 3-colored points in $[0, 1/3)$.
  3. *Reverse-Engineering Scratchpad*: Integrate $P(\text{min bichromatic gap} > x)$ via $O(N)$ combinatorics on periodic/aperiodic color blocks.
  4. *Boundary Pitfall*: Include the anchor cut at $0$ so all 3 colors are represented at the boundary.

- **`W1A-28`: `[POI XVI] Quasi-Template / PRE-Prefixuffix` (`Luogu P3546`)** `[EN]`/`[ZH]`
  1. *Diagnostic Signal*: Testing all $k \le N/2$ for cyclic equivalence $S[1..k] = A B$ and $S[N-k+1..N] = B A$ takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: $S[1..k] = A B$ and $S[N-k+1..N] = B A \iff b_1 = |A| \in \text{Border}(S)$ and $b_2 = |B|$ is a border of the inner substring $S[b_1+1 .. N-b_1]$. Crucially, letting $f(i)$ be the longest border of $S[i+1..N-i]$ ($\le (N-2i)/2$), shrinking $i \to i-1$ adds 2 outer characters, so **$f(i-1) \le f(i) + 2$**!
  3. *Reverse-Engineering Scratchpad*: Sweep $i = \lfloor N/2 \rfloor \to 0$, starting $f(i)$ from $f(i+1) + 2$ and decrementing until $\text{LCE}$/hash matches in amortized $O(N)$ time; maximize $i + f(i)$ over $i \in \text{Border}(S) \cup \{0\}$.
  4. *Boundary Pitfall*: Clip $f(i) \le \lfloor N/2 \rfloor - i$.

- **`W1A-29`: `[POI XIX] OKR-A Horrible Poem` (`Luogu P3538`)** `[EN]`/`[ZH]`
  1. *Diagnostic Signal*: Testing all divisors of $L = r - l + 1$ for $Q$ substring queries takes $O(Q \sqrt{N})$.
  2. *Combinatorial Word Invariant*: By Period–Border Duality, $d \mid L$ is an exact period of $S[l..r] \iff S[l..r-d] = S[l+d..r]$. By the Weak Periodicity Lemma ($\gcd$ closure of exact periods), the minimum exact period $d_{\min}$ divides $L / p$ if and only if $L / p$ is itself an exact period of $S[l..r]$!
  3. *Reverse-Engineering Scratchpad*: Precompute smallest prime factors $\text{spf}[1..N]$ and rolling hash / LCE; for each query $[l, r]$, factorize $L = r - l + 1$ in $O(\log L)$ steps and greedily replace $ans \leftarrow ans / p$ whenever $S[l..r - ans/p] == S[l + ans/p .. r]$. Time: $O(N + Q \log N)$.
  4. *Boundary Pitfall*: Test $S[l .. r - ans/p] == S[l + ans/p .. r]$ using the *current* reduced $ans$, not the original $L$, so prime powers $p^e$ are stripped completely.

- **`W1A-30`: `CF 526D — Om Nom and Necklace`** `[EN]`
  1. *Diagnostic Signal*: Checking all candidate block lengths $|AB|$ for each prefix $S[1..i]$ takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: $S[1..i] = (AB)^k A \iff$ there is a multiple $p = c \cdot p_{\min}$ of $p_{\min} = i - \pi[i]$ such that $k p \le i \le (k+1)p$. The optimal choice is $c = \lfloor (i / p_{\min}) / k \rfloor$.
  3. *Reverse-Engineering Scratchpad*: Compute $\pi[1..N]$; for each $i$, let $p_{\min} = i - \pi[i]$ and $c = (i / p_{\min}) / k$; output `1` iff $i - c k p_{\min} \le c p_{\min}$. Time: $O(N)$.
  4. *Boundary Pitfall*: Handle $p_{\min} \mid i$ vs. $p_{\min} \nmid i$ cleanly via $i - c k p_{\min} \le c p_{\min}$.

- **`W1A-31`: `[THUPC 2018] 绿绿和串串` (`Luogu P5446`)** `[ZH]`
  1. *Diagnostic Signal*: Simulating prefix mirror reflections takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: Prefix $S[1..k]$ can generate $S[1..N]$ by mirror flips iff the odd palindrome centered at $k$ reaches $N$ ($k + R[k] - 1 = N$), OR reaches $1$ ($k - R[k] + 1 = 1$) and its right endpoint $k + R[k] - 1$ is itself valid!
  3. *Reverse-Engineering Scratchpad*: Compute Manacher odd radii $R[1..N]$ and scan $k = N \to 1$ in $O(N)$ time.
  4. *Boundary Pitfall*: At $k = 1$, $k - R[k] + 1 = 1$ is trivially true with $R[1] = 1$, which does not advance to a larger index.

- **`W1A-32`: `Luogu P5555 — 秩序魔咒 (Common Palindromes on Dual PAMs)`** `[ZH]`
  1. *Diagnostic Signal*: Intersecting all palindromic substrings of $S$ and $T$ naively takes $O(|S| \cdot |T|)$.
  2. *Combinatorial Word Invariant*: Every common palindrome of $S$ and $T$ corresponds to a shared Trie path from the even root ($0$) or odd root ($1$) in $\text{PAM}(S)$ and $\text{PAM}(T)$.
  3. *Reverse-Engineering Scratchpad*: Build $\text{PAM}(S)$ and $\text{PAM}(T)$, push occurrence counts bottom-up on both fail trees, and run a synchronized DFS from $(0, 0)$ and $(1, 1)$ over shared transitions $\delta_S(u, c)$ and $\delta_T(v, c)$ in $O(|S| + |T|)$ time.
  4. *Boundary Pitfall*: Traverse *both* roots $(0, 0)$ and $(1, 1)$.

---

#### Tier 4: Mastery (`W1A-33` – `W1A-42`)

- **`W1A-33`: `[BJWC 2018] Border 的四种求法` (`Luogu P4482` / `LOJ 2541`)** `[ZH]`
  1. *Diagnostic Signal*: KMP only gives borders of prefixes $S[1..r]$; computing the longest border of an arbitrary substring $S[l..r]$ naively takes $O(N Q)$.
  2. *Combinatorial Word Invariant*:
     - **Method 1 (SAM Link-Tree HLD + 2D Range Search)**: $i \in [l, r-1]$ is a border of $S[l..r]$ (of length $i - l + 1$) $\iff \text{LCSuffix}(S[1..r], S[1..i]) \ge i - l + 1 \iff i - \text{len}(\text{LCA}(u_r, u_i)) \le l - 1$. Decomposing the path from $u_r$ to the SAM root into $O(\log N)$ heavy chains reduces this to $O(\log N)$ 1D/2D segment tree queries in $O((N+Q)\log^2 N)$.
     - **Method 2 (Dyadic Weak Periodicity / IPM)**: In each dyadic scale $[2^{k-1}, 2^k)$, any border $b \in [2^{k-1}, 2^k)$ of $S[l..r]$ corresponds to an occurrence of the prefix $P_k = S[l..l+2^{k-1}-1]$ inside the suffix $T_k = S[r-2^k+1..r]$. Since $|T_k| = 2|P_k|$, by the Weak Periodicity Lemma all occurrences of $P_k$ in $T_k$ form a **single arithmetic progression**!
  3. *Reverse-Engineering Scratchpad*: Either implement SAM Link-Tree HLD with segment trees keyed by $i - \text{len}(\text{LCA})$ or dyadic IPM occurrence AP extraction in $O((N+Q)\log^2 N)$ / $O(N \log N + Q \log N)$.
  4. *Boundary Pitfall*: Strictly restrict $i \in [l, r-1]$ so $i = r$ (the improper border $r - l + 1$) is excluded.

- **`W1A-34`: `CF 1286E — Fedya the Potter Strikes Back`** `[EN]`
  1. *Diagnostic Signal*: Online encrypted queries require maintaining $\sum_{b \in \text{Border}(S[1..i]) \cup \{i\}} \min_{i-b+1 \le k \le i} W[k]$ in $O(N \log N)$ without ever revisiting surviving borders during KMP fail-chain deletions.
  2. *Combinatorial Word Invariant*: Define $\text{anc}[u] = (\text{if } S[\pi[u]+1] == S[u+1] \text{ then } \text{anc}[\pi[u]] \text{ else } \pi[u])$. At step $i$, walking $u = \pi[i-1] \to 0$ and jumping $u \leftarrow \text{anc}[u]$ whenever $S[u+1] == S[i]$ visits **only** borders that permanently die at step $i$. Since at most $1$ border is born per step, at most $N$ borders ever die across the entire run!
  3. *Reverse-Engineering Scratchpad*: Maintain active border left-endpoint minimums in a `std::map<int, int>` compressed by a monotonic stack on $W[1..i]$; erase dead borders via $\text{anc}[u]$ jumps and accumulate the running sum in `__int128`. Time: $O(N \log N)$.
  4. *Boundary Pitfall*: The sum reaches $\approx 10^{20} > 2^{64}$, so `__int128` (or high/low 64-bit limbs) is mandatory (`BP-1A-08`).

- **`W1A-35`: `[NOI 2016] 优秀的拆分` (`UOJ #219` / `Luogu P1117`)** `[ZH]`
  1. *Diagnostic Signal*: Counting $A A B B$ substrings naively takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: Every square $AA$ of half-length $L = |A|$ covers two consecutive grid anchors $x = j L$ and $y = (j+1)L$. Letting $l = \min(L, \text{LCSuffix}(x, y))$ and $r = \min(L, \text{LCP}(x, y))$, valid squares of period $L$ straddling $(x, y)$ exist iff $l + r - 1 \ge L$ and form a contiguous interval of start/end positions (a single AP of period-$L$ shifts!).
  3. *Reverse-Engineering Scratchpad*: Build SA + RMQ on $S$ and $S^R$; iterate over all $\sum_{L=1}^{N/2} (N/L) = O(N \log N)$ anchor pairs, range-add $+1$ to difference arrays `start_sq` and `end_sq`, and sum `end_sq[i] * start_sq[i+1]`. Time: $O(N \log N)$.
  4. *Boundary Pitfall*: Subtract $1$ in $l + r - 1 \ge L$ (since $S[x]$ is counted in both $l$ and $r$) and clip $l, r \le L$ to avoid double-counting across adjacent anchor pairs.

- **`W1A-36`: `CF 1043G — Speckled Band`** `[EN]`
  1. *Diagnostic Signal*: For any substring $S[l..r]$ over $|\Sigma| = 26$, the answer is $-1$ if all characters are distinct ($r - l + 1 \le 26$), and **always $\in \{1, 2, 3, 4\}$** otherwise!
  2. *Combinatorial Word Invariant*:
     - Ans $= 1 \iff S[l..r]$ has an exact proper period $d \mid (r-l+1)$ (`W1A-29`).
     - Ans $= 2 \iff S[l..r]$ has a proper border ($A B A$), OR starts with a square $AA$, OR ends with a square $AA$.
     - Ans $= 3 \iff S[l] = S[r]$ ($c B c$), OR $S[l]$ / $S[r]$ repeats inside $S[l+1..r-1]$, OR $S[l..r]$ contains any internal square $AA$.
     - Else Ans $= 4$.
  3. *Reverse-Engineering Scratchpad*: Precompute shortest start/end squares via harmonic LCE grid (`W1A-35`), exact periods via SPF (`W1A-29`), and substring borders (`W1A-33`) in $O((N+Q)\log N)$.
  4. *Boundary Pitfall*: Do not forget that a non-empty border $S[l..r] = A B A$ gives Answer $= 2$ via $(AB)(A)$ even when no square touches $l$ or $r$.

- **`W1A-37`: `QOJ / UCup — Substring & Length-Bounded Palindrome Partition (`slink`)`** `[EN]`/`[ZH]`
  1. *Diagnostic Signal*: Restricting palindrome transitions at $r$ to lengths $L \in [L_{\min}, r - l + 1]$ truncates `slink` AP chains at both ends.
  2. *Combinatorial Word Invariant*: In $\mathcal{I}(u, r)$, the constraint $L_{\min} \le L \le L_{\max}$ translates to $r - L_{\max} \le i \le r - L_{\min}$, which is a contiguous slice of the AP chain because elements enter $g[u]$ in strictly increasing order of left endpoint $i = r - \ell_k$!
  3. *Reverse-Engineering Scratchpad*: Clip the top of the chain by binary-jumping / modular division to the largest $\ell_j \le r - l + 1$, and clip the bottom via a delayed pointer / monotonic queue per chain in $O((N+Q)\log N)$.
  4. *Boundary Pitfall*: A node $v$ that is $t$ steps below $u$ in the same period-$d$ chain had its $g[v]$ last updated at step $r - t \cdot d$.

- **`W1A-38`: `LOJ #6681 / Ynoi — Substring Period & Border AP Polynomial Sums`** `[ZH]`
  1. *Diagnostic Signal*: Summing $f(b)$ over all borders $b \in \text{Border}(S[l..r])$ takes $O(N Q)$ if enumerated element-by-element.
  2. *Combinatorial Word Invariant*: By Theorem 2.4, $\text{Border}(S[l..r])$ partitions into $\le \lceil \log_2(r-l) \rceil$ arithmetic progressions $(x_k, d_k, c_k)$.
  3. *Reverse-Engineering Scratchpad*: Extract the $O(\log(r-l))$ APs via dyadic IPM (`W1A-33` Method 2) and evaluate closed-form power sums $\sum_{j=0}^{c_k} (x_k + j d_k)^m$ in $O(1)$ per AP!
  4. *Boundary Pitfall*: Use half-open dyadic ranges $[2^{k-1}, 2^k)$ so borders equal to $2^k$ are not summed twice.

- **`W1A-39`: `CF 1764G / UCup — Inverse KMP & Border-Set Realizability via slink`** `[EN]`/`[JA]`
  1. *Diagnostic Signal*: Validating or counting strings matching a given $\pi[1..N]$ requires collecting all forbidden characters $S[u+1]$ along the fail chain from $\pi[i-1]$ down to $\pi[i]$, which has length $O(N)$ on adversarial arrays.
  2. *Combinatorial Word Invariant*: By Theorem 2.6, whenever $\text{diff}[u] = \text{diff}[\pi[u]]$, we have $S[\pi[u]+1] = S[\pi[\pi[u]]+1]$. Thus the entire fail chain of $i-1$ contains **at most $O(\log i)$ distinct characters $S[v+1]$**, reachable by jumping `slink`!
  3. *Reverse-Engineering Scratchpad*: Jump `slink` from $\pi[i-1]$ to collect the $O(\log i)$ forbidden characters in $O(\log i)$ time per index; total time $O(N \log N)$.
  4. *Boundary Pitfall*: Inside an AP chain of $u$, $S[\pi[u]+1] = S[\pi[\pi[u]]+1]$, whereas $S[u+1]$ (at the chain top) can differ because $u+1$ is outside $S[1..u]$.

- **`W1A-40`: `AtCoder AGC 055 D — ABC Ultimatum / Periodic Shift Counting`** `[JA]`
  1. *Diagnostic Signal*: Counting periodic strings under simultaneous cyclic shift matching constraints.
  2. *Combinatorial Word Invariant*: Dualize simultaneous shift matchings via Hall's Marriage Theorem / prefix-excess minimums over the period lattice.
  3. *Reverse-Engineering Scratchpad*: Track the 3 prefix-excess minimums in a polynomial-time DP over the period length.
  4. *Boundary Pitfall*: Normalize the global minimum prefix excess to $0$ to avoid double-counting states.

- **`W1A-41`: `ICPC WF / UCup — Huge-Length Fine–Wilf Word Equations ($N \le 10^{18}$)`** `[EN]`
  1. *Diagnostic Signal*: $N \le 10^{18}$ makes index-level DSU or $O(N \log N)$ parallel DSU impossible.
  2. *Combinatorial Word Invariant*: Whenever two period intervals $[l_1, r_1]$ (period $p$) and $[l_2, r_2]$ (period $q$) overlap on an interval $I$ of length $|I| \ge p + q - \gcd(p, q)$, Theorem 2.2 collapses both periods on $I$ to $g = \gcd(p, q)$!
  3. *Reverse-Engineering Scratchpad*: Sweep interval endpoints, contracting overlaps of length $\ge p + q - \gcd(p, q)$ into a single $\gcd$ period and keeping explicit graph nodes only for short boundary overlaps ($< 2 \max p_i$).
  4. *Boundary Pitfall*: Never contract to $\gcd(p, q)$ when $|I| < p + q - \gcd(p, q)$ (`BP-1A-01`).

- **`W1A-42`: `CF 1608F / Grandmaster Palindromic slink + Segment Tree Range Coupling`** `[EN]`
  1. *Diagnostic Signal*: Partition DP over palindromic suffixes $L \in \text{PalSuffix}(S[1..r])$ where each left endpoint $l = r - L + 1$ also receives dynamic range updates $[q_l, q_r]$ as $r$ advances.
  2. *Combinatorial Word Invariant*: By Theorem 4.1, each `slink` chain $(\text{slink}[u], u]$ adds only **one** new left endpoint $r - \text{len}[\text{slink}[u]] - \text{diff}[u]$ relative to step $r - \text{diff}[u]$, and all left endpoints in the chain form a contiguous segment in the residue class modulo $\text{diff}[u]$ (or can be maintained by recording the timestamp $r - \text{diff}[u]$ and applying lazy range deltas).
  3. *Reverse-Engineering Scratchpad*: Couple PAM `slink` chain heads with a lazy segment tree / Fenwick tree over left endpoints in $O(N \log^2 N)$.
  4. *Boundary Pitfall*: Account for range updates occurring during $(r - \text{diff}[u], r]$ before merging $g[\text{fail}[u]]$.

---

### 6.3 Reconciled Quarantine Ledger of Pure Template Problems (`R-1A-01` – `R-1A-13`)

Per `AGENTS.md` and `strings_research/PLAN.md` (§2.2), the union of all 13 bare template verification problems identified by Cohort 1 and Cohort 2 is strictly quarantined from textbook chapters:

| Quarantine ID | Problem & Source | Lang | Cohort Origin | Reason for Quarantine |
| :--- | :--- | :--- | :--- | :--- |
| **R-1A-01** | **Library Checker — Z Algorithm** | `[EN]`/`[JA]` | Both | Bare $Z[0..N-1]$ array output with zero period/border modeling. |
| **R-1A-02** | **Library Checker — Enumerate Palindromes** | `[EN]`/`[JA]` | Both | Bare Manacher radius array verification. |
| **R-1A-03** | **Luogu P3375 — 【模板】KMP** | `[ZH]` | Both | Direct verification of pattern occurrences and $\pi[1..M]$. |
| **R-1A-04** | **Luogu P5410 — 【模板】扩展 KMP / exKMP (Z 函数)** | `[ZH]` | Both | Direct XOR-sum verification of the $Z$-array. |
| **R-1A-05** | **Luogu P3805 — 【模板】manacher** | `[ZH]` | Cohort 1 | Standard longest palindromic substring template verification. |
| **R-1A-06** | **Luogu P5496 — 【模板】回文自动机（PAM）** | `[ZH]` | Both | Standard online PAM construction outputting `dep[last]` per step. |
| **R-1A-07** | **Luogu P5829 — 【模板】失配树 (KMP Fail Tree LCA)** | `[ZH]` | Cohort 2 | Bare LCA query on the KMP fail tree $u \to \pi[u]$ without combinatorics. |
| **R-1A-08** | **CSES 1753 — String Matching** | `[EN]` | Cohort 2 | Standard single-pattern matching template. |
| **R-1A-09** | **CSES 1732 — Finding Borders** | `[EN]` | Cohort 2 | Direct printout of $\pi[N], \pi[\pi[N]], \dots$ without structural constraints. |
| **R-1A-10** | **UVA 455 — Periodic Strings** | `[EN]` | Cohort 1 | Trivial $N \le 80$ exact period check $p = N - \pi[N]$ with $p \mid N$. |
| **R-1A-11** | **POJ 2406 — Power Strings** | `[EN]` | Cohort 1 | Bare exact period formula $N / (N - \pi[N])$ when $(N - \pi[N]) \mid N$. |
| **R-1A-12** | **POJ 1961 / UVA 1328 — Period** | `[EN]` | Cohort 1 | Bare prefix-by-prefix printout of $i / (i - \pi[i])$ when $(i - \pi[i]) \mid i$. |
| **R-1A-13** | **POJ 2752 — Seek the Name, Seek the Fame** | `[EN]` | Cohort 1 | Bare KMP fail-chain walk printing all border lengths of $S[1..N]$. |

---

## Section 7. Consolidated Multilingual Bibliography & Curriculum Integration Notes

### 7.1 Master Wave 1A Bibliography (`[EN]` / `[ZH]` / `[JA]`)

1. **[EN] Fine, N. J., & Wilf, H. S. (1965)**. *"Uniqueness theorems for periodic functions"*, Proceedings of the American Mathematical Society, 16(1), 109–114. (Proves the sharp $p + q - \gcd(p, q)$ periodicity threshold.)
2. **[EN] Castelli, M. G., Mignosi, F., & Restivo, A. (1999)**. *"Fine and Wilf's theorem for three periods and a generalization of Sturmian words"*, Theoretical Computer Science, 218(1), 83–94. (Three-period Fine–Wilf extension and episturmian extremal words.)
3. **[EN] Lothaire, M. (1997 / 2002)**. *Combinatorics on Words* & *Algebraic Combinatorics on Words*, Cambridge University Press. (Chapters on Periodicity, Critical Factorization Theorem, and Central Sturmian / Pirillo words.)
4. **[EN] Crochemore, M., & Rytter, W. (2003)**. *Jewels of Stringology: Text Algorithms*, World Scientific. (Weak Periodicity Lemma and dyadic border decomposition.)
5. **[EN] Fici, G., Gagie, T., Kärkkäinen, J., & Kempa, D. (2014)**. *"A subquadratic algorithm for minimum palindromic factorization"*, Journal of Discrete Algorithms, 28, 41–48. (Proves the Shift-Overlap Invariant of palindromic suffix APs for $O(N \log N)$ factorization.)
6. **[EN] Rubinchik, M., & Shur, A. M. (2018)**. *"EERTREE: An efficient data structure for processing palindromes in strings"*, European Journal of Combinatorics, 68, 249–265 (`arXiv:1506.04862`). (Introduces PAM, `diff[u]`, `slink[u]`, and $O(N \log N)$ palindrome partition DP.)
7. **[EN] Kociumaka, T., Radoszewski, J., Rytter, W., & Waleń, T. (2015)**. *"Internal Pattern Matching Queries in a Text and Applications"*, SODA 2015, 532–551. (Proves that internal occurrences of $P$ in $T$ with $|T| < 2|P|$ form a single arithmetic progression.)
8. **[ZH] 徐毅 (Xu Yi, 2014)**. 《回文树及其应用》 (*Palindromic Trees and Their Applications*), 中国国家集训队论文 (Chinese IOI National Team Papers 2014). (Foundational `[ZH]` treatise on PAM, half-links `trans[u]`, and `slink` DP.)
9. **[ZH] 翁文涛 (Weng Wentao, 2017)**. 《回文自动机及其应用》 & WC2016《论战捆竹竿》命题报告, 中国国家集训队论文 (Chinese IOI National Team Papers 2017). (Establishes `Border 的等差数列性质`, dynamic modulus switching, and residue-cycle monotonic queue in $O(N \log N)$.)
10. **[ZH] 金策 (Jin Ce, 2019)**. 《字符串算法选讲》 (*Selected Topics in String Algorithms — Borders, Lyndon Words, and Runs*), 中国国家集训队论文 (Chinese IOI National Team Papers 2019). (Definitive `[ZH]` synthesis of Weak Periodicity, `[BJWC2018] Border 的四种求法`, and Runs.)
11. **[JA] `snuke` / `maspypy` / `noshi91` (2018–2024)**. Japanese competitive stringology treatises on Palindromic Tree `slink` DP (`回文木の等差数列分解とDP高速化`) and KMP shortcut mismatch links (`CF 1286E`).
12. **[EN] Iium / Gawrychowski et al.** Substring period & border AP query reductions (`CF 1043G`, `Universal Cup` stringology sets).

### 7.2 Handoff Recommendations for Phase 1.5 Curriculum Architecture (`Part I`)
- **Chapter 01 (`Period–Border Duality, the Fine–Wilf Theorem & Extremal Sturmian Words`)**: Anchor on the 3 unified proofs of Fine–Wilf, the exact sub-threshold component formula $p + q - N$, the $(5, 8) \to \text{length } 11$ central Sturmian counterexample, and the 3-period Castelli–Mignosi–Restivo frontier note. Ladder: `W1A-01`, `W1A-03`, `W1A-04`, `W1A-05`, `W1A-10`, `W1A-11`, `W1A-13`, `W1A-30`, `W1A-41`.
- **Chapter 02 (`The Weak Periodicity Lemma, Log-Block Border APs & KMP Shortcut Links`)**: Prove Both the dyadic halving bound and the exact $|\text{fail}[u]| < \frac{2}{3}|u|$, $|\text{fail}[\text{fail}[u]]| < \frac{1}{2}|u|$ drop at `diff` boundaries, plus the unification of `slink[u]` and `anc[u]` (Theorem 2.6). Ladder: `W1A-02`, `W1A-06`, `W1A-08`, `W1A-12`, `W1A-19`, `W1A-29`, `W1A-34`, `W1A-39`.
- **Chapter 03 (`Border-Group Modulo Shortest Path & Residue-Cycle Monotonic Queues`)**: Develop Subroutine A (dynamic modulus switch on $\gcd(m_{\text{old}}, x_k)$ cycles) and Subroutine B (argmin-unrolled DAG monotonic deque on $\gcd(d_k, x_k)$ cycles) for `[WC2016] 论战捆竹竿`. Ladder: `W1A-24`, `W1A-26`, `W1A-27`, `W1A-28`, `W1A-40`.
- **Chapter 04 (`Series-Link (slink / diff) DP Acceleration on PAM & KMP`)**: Present the complete zero-magic proof of Theorem 4.1 (including uniqueness of period-$d$ PAM child and non-skipping at $r - d$), double-end interleaving (`CF 932G`, `CF 906E`), polynomial-weighted binomial splitting (§4.3), and length-bounded `slink` DP (§4.4). Ladder: `W1A-07`, `W1A-15`, `W1A-16`, `W1A-17`, `W1A-22`, `W1A-23`, `W1A-25`, `W1A-32`, `W1A-37`, `W1A-42`.
- **Cross-Link to Part IV (`Internal Pattern Matching`)**: Reserve `W1A-33` (`[BJWC2018] Border 的四种求法`), `W1A-35` (`[NOI2016] 优秀的拆分`), `W1A-36` (`CF 1043G`), and `W1A-38` (`LOJ #6681`) as the bridge connecting Part I's border AP theory to Part II (Runs) and Part IV (Internal Pattern Matching).

---

## Section 8. Hand-Checkable Worked Traces for Phase 2 Chapter Authoring

### 8.1 Worked Trace 1: `slink` DP Step-by-Step Evolution on $T = \texttt{aaaaaa}$ ($N = 6$)
To eliminate any ambiguity around Pitfalls `BP-1A-06` and `BP-1A-07`, here is the complete step-by-step state table of the PAM `slink` DP counting even-palindrome partitions of $T = \texttt{aaaaaa}$ (`CF 932G` kernel, $dp[0] = 1$, $dp[\text{odd}] = 0$):

- **PAM Nodes Created on $T = \texttt{a}^6$**:
  - Even root $0$: $\text{len}[0] = 0, \text{fail}[0] = 1$.
  - Odd root $1$: $\text{len}[1] = -1, \text{fail}[1] = 1$.
  - For each $k \in \{1, 2, 3, 4, 5, 6\}$, node $u_k$ represents $\texttt{a}^k$ with $\text{len}[u_k] = k$:
    - $u_1$ ($\texttt{a}$): $\text{len} = 1, \text{fail} = 0, \text{diff} = 1 - 0 = 1, \text{slink} = 0$.
    - $u_k$ ($\texttt{a}^k, k \ge 2$): $\text{len} = k, \text{fail} = u_{k-1}, \text{diff} = 1 == \text{diff}[u_{k-1}] \implies \text{slink}[u_k] = \text{slink}[u_{k-1}] = 0$.

- **Step-by-Step Execution ($r = 1 \dots 6$)**:
  - **$r = 1$** (`last` $= u_1$, odd $r$):
    - New index $r_{\text{new}} = 1 - \text{len}[0] - 1 = 0$.
    - $\text{diff}[u_1] \ne \text{diff}[0] \implies g[u_1] = dp[0] = 1$.
    - Since $r = 1$ is odd, $dp[1] = 0$. (Notice $g[u_1] = 1$ is saved for $r = 2$!)
  - **$r = 2$** (`last` $= u_2$, even $r$):
    - $r_{\text{new}} = 2 - 0 - 1 = 1$.
    - $\text{diff}[u_2] == \text{diff}[u_1] = 1 \implies g[u_2] = dp[1] + g[u_1] = 0 + 1 = 1$ (covering left endpoints $\{0, 1\}$).
    - Since $r = 2$ is even, $dp[2] = g[u_2] = 1$ (`aa`).
  - **$r = 3$** (`last` $= u_3$, odd $r$):
    - $r_{\text{new}} = 3 - 0 - 1 = 2$.
    - $g[u_3] = dp[2] + g[u_2] = 1 + 1 = 2$ (covering left endpoints $\{0, 1, 2\}$).
    - Since $r = 3$ is odd, $dp[3] = 0$. (**Crucial**: if we had skipped $r = 3$, $g[u_3]$ would not have incorporated $dp[2] = 1$!)
  - **$r = 4$** (`last` $= u_4$, even $r$):
    - $r_{\text{new}} = 4 - 0 - 1 = 3$.
    - $g[u_4] = dp[3] + g[u_3] = 0 + 2 = 2$ (covering left endpoints $\{0, 1, 2, 3\}$).
    - Since $r = 4$ is even, $dp[4] = g[u_4] = 2$ (`aaaa`, `aa|aa`).
  - **$r = 5$** (`last` $= u_5$, odd $r$):
    - $r_{\text{new}} = 5 - 0 - 1 = 4$.
    - $g[u_5] = dp[4] + g[u_4] = 2 + 2 = 4$; $dp[5] = 0$.
  - **$r = 6$** (`last` $= u_6$, even $r$):
    - $r_{\text{new}} = 6 - 0 - 1 = 5$.
    - $g[u_6] = dp[5] + g[u_5] = 0 + 4 = 4$; $dp[6] = g[u_6] = 4$ (`aaaaaa`, `aaaa|aa`, `aa|aaaa`, `aa|aa|aa`).

---

### 8.2 Worked Trace 2: Dynamic Modulus Switching on `[WC2016] 论战捆竹竿`
Suppose $S = \texttt{ababaababa}$ ($N = 10$).
1. **Borders of $S$**:
   - $b_1 = \pi[10] = 5$ ($\texttt{ababa}$), $\text{diff}[5] = 5 - \pi[5] = 5 - 3 = 2$.
   - $b_2 = \pi[5] = 3$ ($\texttt{aba}$), $\text{diff}[3] = 3 - \pi[3] = 3 - 1 = 2 \implies \text{slink}[5] = \text{slink}[3] = 1$.
   - $b_3 = \pi[3] = 1$ ($\texttt{a}$), $\text{diff}[1] = 1 - 0 = 1 \implies \text{slink}[1] = 0$.
2. **Complementary Period APs ($\mathcal{P}(S) = \{10 - b : b \in \{5, 3, 1\}\} = \{5, 7, 9\}$)**:
   - Half-open chain $(1, 5]$ (or closed chain $[1, 5]$ since $\min$ is idempotent!): borders $\{5, 3, 1\}$ have constant step $d_1 = 2$, giving periods:
     $$\mathcal{A}_1 = \{10 - 5,\; 10 - 3,\; 10 - 1\} = \{5, 7, 9\} = \{x_1 + j \cdot d_1 : 0 \le j \le 2\} \quad (x_1 = 5, d_1 = 2, c_1 = 2).$$
3. **Execution of Subroutine A & B**:
   - Start at $m_0 = 10$ with $D[0] = 10, D[1..9] = \infty$.
   - **Subroutine A ($m_0 = 10 \to x_1 = 5$)**: Project $D[0] = 10$ into $D_{\text{new}}[10 \bmod 5] = D_{\text{new}}[0] = 10$. Since $\gcd(10, 5) = 5$, each cycle of $+10 \pmod 5$ has length $1$; $D_{\text{new}} = [10, \infty, \infty, \infty, \infty]$.
   - **Subroutine B ($+2 \pmod 5$ with window $c_1 = 2$, weights $5 + 2j \in \{7, 9\}$)**:
     - $\gcd(2, 5) = 1$, so there is a single cycle of length $5$ starting at $\arg\min D = 0$:
       $$(v_0, v_1, v_2, v_3, v_4) = (0, 2, 4, 1, 3).$$
     - $t = 0$ ($v_0 = 0$): $D[0] = 10$, push `(0, 10 - 0*2) = (0, 10)`.
     - $t = 1$ ($v_1 = 2$): window $[0, 0] \implies D[2] = 10 + 5 + 1 \cdot 2 = 17$ (using period $7$), push `(1, 17 - 2) = (1, 15)`.
     - $t = 2$ ($v_2 = 4$): window $[0, 1]$, min key is $(0, 10) \implies D[4] = 10 + 5 + 2 \cdot 2 = 19$ (using period $9$), push `(2, 19 - 4) = (2, 15)`.
     - $t = 3$ ($v_3 = 1$): $t - c_1 = 1$ pops $0$; window $[1, 2]$, min key is $15 \implies D[1] = 15 + 5 + 3 \cdot 2 = 26$ (using $7 + 9 = 16$ or $9 + 7 = 16$), push `(3, 26 - 6) = (3, 20)`.
     - $t = 4$ ($v_4 = 3$): $t - c_1 = 2$ pops $1$; window $[2, 3]$, min key is $(2, 15) \implies D[3] = 15 + 5 + 4 \cdot 2 = 28$ (using $9 + 9 = 18$).
   - Final shortest lengths modulo $5$: $D = [10, 26, 17, 28, 19]$, computed in a single 5-step pass!

---

### 8.3 Worked Trace 3: The Critical Factorization Theorem (CFT) Local vs. Global Period
Consider the Fine–Wilf extremal Sturmian word $S = \texttt{abaababaaba}$ of length $N = 11$, whose global minimum period is $p_{\min}(S) = 5$ (since $\pi[11] = 6$, $11 - 6 = 5$).
- At any split point $i \in [1, N-1]$ factoring $S = u v$ ($u = S[1..i], v = S[i+1..N]$), a *local repetition* at $i$ is a shortest non-empty word $w$ such that $w$ is a suffix of $u$ (or $u$ is a suffix of $w$) AND $w$ is a prefix of $v$ (or $v$ is a prefix of $w$). Its length $|w|$ is the **local period** $\text{lp}(i)$.
- Let us compute $\text{lp}(i)$ across $S = \texttt{abaababaaba}$:
  - $i = 1$ (`a | baababaaba`): $w = \texttt{ab}$ ($\text{lp}(1) = 2$)
  - $i = 2$ (`ab | aababaaba`): $w = \texttt{aba}$ ($\text{lp}(2) = 3$)
  - $i = 3$ (`aba | ababaaba`): $w = \texttt{aba}$ ($\text{lp}(3) = 3$)
  - $i = 4$ (`abaa | babaaba`): $w = \texttt{abaab}$ ($\text{lp}(4) = \mathbf{5} = p_{\min}(S)$, **Critical Point!**)
  - $i = 5$ (`abaab | abaaba`): $w = \texttt{abaab}$ ($\text{lp}(5) = \mathbf{5} = p_{\min}(S)$, **Critical Point!**)
  - $i = 6$ (`abaaba | baaba`): $w = \texttt{baaba}$ ($\text{lp}(6) = \mathbf{5} = p_{\min}(S)$, **Critical Point!**)
  - $i = 7$ (`abaabab | aaba`): $w = \texttt{abaab}$ ($\text{lp}(7) = \mathbf{5} = p_{\min}(S)$, **Critical Point!**)
- Notice that $\text{lp}(i) \le p_{\min}(S) = 5$ everywhere, and at the critical factorizations $i \in \{4, 5, 6, 7\}$, the local period attains the exact global period $5$! Furthermore, per the **Critical Factorization Theorem (Cesari–Vincent–Duval)**, the critical point $i = 4$ (`abaa | babaaba`) is obtained Directly by taking the maximum between the lexicographically maximal suffix under $<$ (`babaaba`, starting at $5 \implies i = 4$) and under $>$ (`abaababaaba` / `aababaaba`). This forms the direct theoretical bridge from **Wave 1A (Periodicity & Borders)** to **Wave 1B (Lyndon Words, Duval's Algorithm & Significant Suffixes)**.
