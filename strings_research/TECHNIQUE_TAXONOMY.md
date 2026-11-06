# Master Advanced Stringology Technique Taxonomy & Diagnostic Atlas (`strings_research/TECHNIQUE_TAXONOMY.md`)

> [!IMPORTANT]
> **Canonical Phase 1.5 Master Synthesis Across All 115 Research Iterations (Cohorts 1, 2 & 3)**
> This document (`strings_research/TECHNIQUE_TAXONOMY.md`) is the definitive master technique taxonomy synthesized from the 10 Cohort 3 Reconciled Master Wave Treatises (`cohort3_wave_1a_*.md` through `cohort3_wave_5b_*.md`, spanning Iterations 01–115) across English (`[EN]`), Chinese (`[ZH]`: `国家集训队论文`, NOI/WC/CTSC/CTS/ZJOI/SDOI/BJWC/THUPC, UOJ/LOJ/QOJ), and Japanese (`[JA]`: AtCoder `AGC`/`ARC`/`ABC`, JOI, `noshi91`/`maspypy`/`henkoku`/`tatyam`/`snuke` treatises) sources.
>
> Every technique family strictly follows the **6-Point Structural-Invariant Schema**:
> 1. **Technique ID & Multilingual Name (`[EN]` / `[ZH]` / `[JA]`)**
> 2. **Diagnostic Signal (Constraints & Query Shape that Trigger This Tool)**
> 3. **Core Combinatorial Word Invariant (Exact Mathematical Statement & Why It Holds)**
> 4. **Algorithmic / Data-Structure Compilation & Complexity**
> 5. **Canonical Failure Modes & Counterexamples**
> 6. **Canonical Representative Problems**

---

## Executive Overview of the 10-Wave & Frontier Stringology Ecosystem

| Wave | Domain Focus | Core Technique Families (`ID`) | Primary Structural Collapse |
| :--- | :--- | :--- | :--- |
| **Wave 1A** | Structural Periodicity, Border Algebra & `slink` DP | `T-1A-01` – `T-1A-05` | $\Theta(N)$ borders/palindromic suffixes $\to \le \lceil \log_2 N \rceil$ arithmetic progressions |
| **Wave 1B** | Lyndon Theory, Significant Suffixes & The Runs Theorem | `T-1B-01` – `T-1B-06` | $\Theta(N^2)$ periodic squares $\to < N$ Lyndon-rooted runs; $\Theta(N)$ suffixes $\to O(\log N)$ significant suffixes |
| **Wave 2A** | Advanced SAM, GSAM, Endpos Merging & LCT/HLD | `T-2A-01` – `T-2A-05` | Substring containment $\to$ 1D clipped $\text{endpos}$ range; distinct substrings $\to$ LCT solid color chains |
| **Wave 2B** | SA-IS, Virtual Suffix Trees, Dominant Pairs, IPM & Bi-Directional Suffixes | `T-2B-01` – `T-2B-06` | $\Theta(N^2)$ suffix pairs $\to 2N \log_2 N$ dominant pairs; substring occurrences in $|T|<2|P| \to 1$ AP |
| **Wave 3A** | Deque/Persistent PAM, Range Palindromes, Rich Words & Inverse Construction | `T-3A-01` – `T-3A-06` | Amortized fail hops $\to O(1)$ `quick_link`; Deque PAM $\to$ surface push; Range LPS $\to O(1)$ unclipping |
| **Wave 3B** | FFT/NTT Matching, $k$-Mismatch, Isomorphism & Locally Consistent Parsing (SLP) | `T-3B-01` – `T-3B-05` | Non-transitive relations $\to$ polynomial convolution; $10^{18}$ strings $\to O(\log N)$-depth SLPs |
| **Wave 4A** | Goulden–Jackson Cluster Method, Martingale PGFs & `DP套DP` | `T-4A-01` – `T-4A-05` | $O(\sum |P_i|)$ AC states $\to m \times m$ border system; $k$-occurrences $\to t = 1 + u$ binomial moment shift |
| **Wave 4B** | Subsequence Automata (DASG), Invertible Matrices & Tiskin's Seaweed Matrices | `T-4B-01` – `T-4B-05` | Range subsequence DP $\to O(1)$-sparse inverse matrix; all $O(N^2)$ interval LCS $\to N \times N$ Seaweed permutation |
| **Wave 5A** | Word Equations, Signed Binary-Lifting DSU, Inequalities, Wheeler/BWT & Tree Strings | `T-5A-01` – `T-5A-05` | $M$ substring/palindrome equations $\to O(N \log N)$ dyadic DSU levels; RLBWT $\to O(1)$ Move Structure |
| **Wave 5B & Frontier** | Sturmian/Fibonacci Singular Words, $SL_2(\mathbb{F}_p)$ Stack Hashing & 6 Frontier Paradigms | `T-5B-01` – `T-5B-08` | Stack cancellation $\to$ non-abelian $SL_2(\mathbb{F}_p)$ prefix product / Stack-Trie; dictionary compression $\to$ Attractors $\gamma(S)$ & $\tau$-Synchronizing Sets |

---

## Wave 1A: Structural Periodicity, Border Theory, Weak Periodicity Lemma & Series-Link (`slink`) DP

### `T-1A-01`. Period–Border Duality, Fine–Wilf Theorem & Sub-Threshold Orbit Counting
1. **Multilingual Name**:
   - `[EN]`: Period–Border Duality & The Fine–Wilf Periodicity Theorem (with Sub-Threshold Orbit Formula & Three-Period Castelli–Mignosi–Restivo Extension)
   - `[ZH]`: 周期与 Border 的对偶性、Fine–Wilf 周期定理及阈值下连通块计数
   - `[JA]`: 周期とボーダーの双対性・Fine–Wilf の定理と閾値未満の連結成分数
2. **Diagnostic Signal**:
   - A string $S[1..N]$ is constrained simultaneously by two periods $p$ and $q$ (or two borders $N-p$ and $N-q$), or a counting problem asks for the number of strings of length $N$ admitting periods $p, q$ ($N$ above or below $p+q-\gcd(p,q)$), or word equations impose overlapping periodicities.
3. **Core Combinatorial Word Invariant**:
   - **Period–Border Bijection**: $b \in \text{Border}(S) \iff p = |S| - b \in \text{Per}(S)$, with shortest period $p_{\min}(S) = |S| - \pi[|S|]$.
   - **Fine–Wilf Threshold**: If $p, q \in \text{Per}(S[1..N])$ and $N \ge p + q - \gcd(p, q)$, then $g = \gcd(p, q) \in \text{Per}(S[1..N])$.
   - **Why It Holds (Hamiltonian Path & First-Return Cycle Proofs)**: For $\gcd(p, q) = 1$ and $N = p + q - 1$, the index map $f(i) = i + p$ ($i < q$) and $f(i) = i - q$ ($i > q$) satisfies $f(i) \equiv i + p \pmod{p+q}$. Since $\gcd(p, p+q) = 1$, $+p$ generates a single cycle on $\mathbb{Z}/(p+q)\mathbb{Z}$; deleting residue $0$ leaves a **single directed Hamiltonian path** $p \to \dots \to q$ across all $p + q - 1$ indices.
   - **Sub-Threshold Exact Component Count**: When $\max(p, q) \le N < p + q - \gcd(p, q)$, the induced return map $\psi(x) = ((x + p - 1) \bmod q) + 1$ on $\{1, \dots, q\}$ loses $q - (N - p) = p + q - N$ edges, splitting the index graph into **exactly $p + q - N$ independent character orbits (connected components)**.
   - **Three-Period Extension (Castelli–Mignosi–Restivo 1999)**: Three periods $p_1 < p_2 < p_3$ force period $\gcd(p_1, p_2, p_3)$ at threshold $\frac{1}{2}(p_1 + p_2 + p_3 - 2\gcd(p_1, p_2, p_3) + h(p_1, p_2, p_3))$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Contract any pair of overlapping periodic constraints of overlap $\ge p + q - \gcd(p, q)$ to a single period $\gcd(p, q)$ in $O(\log(\min(p, q)))$ time. Below threshold, count free alphabet choices as $|\Sigma|^{p + q - N}$ in $O(1)$ time.
5. **Canonical Failure Modes & Counterexamples**:
   - **Threshold Off-by-One (`BP-1A-01`)**: Using $N \ge p + q$ (the Weak Periodicity Lemma) instead of $N \ge p + q - \gcd(p, q)$, or assuming $\gcd(p, q)$ holds at $N = p + q - \gcd(p, q) - 1$. At $(p, q) = (5, 8)$, the length-11 Central Sturmian (Fibonacci) word `abaababaaba` has periods $5$ and $8$ (borders `abaaba` of length $6$ and `aba` of length $3$) but $p + q - N = 2$ orbits, so period $1$ fails.
   - **Full vs. Weak Period Confusion (`BP-1A-02`)**: Assuming $p \in \text{Per}(S)$ requires $p \mid |S|$. In `abaab` ($N=5$), $p=2$ is a valid period even though $2 \nmid 5$.
6. **Canonical Representative Problems**:
   - `W1A-01` (`[BOI 2009] Radio Transmission` / Luogu P4391), `W1A-02` (`CF 535D — Tavas and Malekas`), `W1A-11` (`[POI 2012] OKR-A Horrible Poem` / Luogu P3538), `W1A-15` (UCup / QOJ Sub-Threshold Period Orbit Counting $|\Sigma|^{p+q-N}$), `W1A-24` (`AtCoder AGC 032 F — One Third`).

---

### `T-1A-02`. Weak Periodicity Lemma, Log-Block Border AP Decomposition & `slink[u]` vs. `anc[u]` Duality
1. **Multilingual Name**:
   - `[EN]`: Weak Periodicity Lemma, $O(\log N)$ Arithmetic Progression Structure of Borders & KMP Shortcut Link Duality (`slink` vs. `anc`)
   - `[ZH]`: 弱周期引理、Border 的 $O(\log N)$ 等差数列分解与 KMP 加速跳链对偶 (`slink` 与 `anc`)
   - `[JA]`: 弱周期性補題・ボーダーの $O(\log N)$ 等差数列分解と KMP 短絡リンク (`slink` / `anc`)
2. **Diagnostic Signal**:
   - An algorithm must iterate over all borders of $S[1..u]$ (or all palindromic suffixes of $S[1..r]$), or maintain KMP transitions under online character appends/queries (`CF 1721E`) or monotone border deletions (`CF 1286E`) where naive $\pi$-chain traversal takes $\Theta(N)$ per step.
3. **Core Combinatorial Word Invariant**:
   - **Half-Length Single-AP Theorem**: All borders of $S[1..u]$ of length $\ge \lceil u/2 \rceil$ have periods $p \le \lfloor u/2 \rfloor$ that are exact multiples of $p_{\min}(S[1..u]) = u - \pi[u]$ (since $p + p_{\min} \le u \implies \gcd(p, p_{\min}) = p_{\min}$), forming a single AP with step $d = \text{diff}[u] = u - \pi[u]$.
   - **Exact $\frac{2}{3}$ and $\frac{1}{2}$ Length-Drop Inequality**: Let $v = \pi[u], w = \pi[v], d_1 = u - v, d_2 = v - w$. Whenever $d_2 < d_1$, the overlap $2v - u = v - d_1$ between prefix $S[1..v]$ and suffix $S[u-v+1..u]$ must satisfy $v - d_1 < d_2$ (otherwise period $d_2$ propagates across $S[1..u]$). Thus $v < d_1 + d_2 < 2d_1 \implies \pi[u] < \frac{2}{3}u$ and $\pi[\pi[u]] = v - d_2 < d_1 = u - v \implies \pi[\pi[u]] < \frac{1}{2}u$.
   - **`slink[u]` Implies Next-Character Equality (`anc[u]` Coarsening Theorem)**: Whenever $\text{diff}[u] = \text{diff}[\pi[u]] = d$, both $\pi[\pi[u]] + 1 = u - 2d + 1$ and $\pi[u] + 1 = u - d + 1$ lie inside $[1, u]$, so period $d$ of $S[1..u]$ forces $S[\pi[\pi[u]] + 1] = S[\pi[u] + 1]$. Thus every internal step of a `slink` AP chain has identical next character in $S$, and `anc[u]` (which skips ancestors with $S[\pi[u]+1] = S[u+1]$) is an exact coarsening of `slink[u]`.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Precompute $\text{diff}[u] = \text{len}[u] - \text{len}[\text{fail}[u]]$ and $\text{slink}[u] = (\text{diff}[u] == \text{diff}[\text{fail}[u]] \text{ ? } \text{slink}[\text{fail}[u]] : \text{fail}[u])$ in $O(N)$ time.
   - Iterating $u \leftarrow \text{slink}[u]$ visits $\le \lceil \log_2 N \rceil$ disjoint half-open progressions $(\text{slink}[u], u]$ of lengths $\{\text{len}[\text{slink}[u]] + d, \dots, \text{len}[u]\}$ in $O(\log N)$ time per prefix.
5. **Canonical Failure Modes & Counterexamples**:
   - **Closed-Interval Double Counting (`BP-1A-03`)**: Treating $[\text{slink}[u], u]$ as a closed interval in sum/counting DPs counts $\text{slink}[u]$ twice (once as the bottom of $u$'s chain and once as the top of the next chain). Always use the half-open interval $(\text{slink}[u], u]$ with shortest length $\text{len}[\text{slink}[u]] + \text{diff}[u]$.
   - **Using `anc[u]` Beyond Current End of String**: In `CF 1721E` (appending $T[1..10]$ to $S[1..N]$), `anc[u]` cannot be precomputed at $u = N$ before $S[N+1]$ is known, whereas `slink[u]` depends only on $S[1..u]$ and skips each constant-period chain in $O(1)$ after testing $S[\pi[u]+1]$ once.
6. **Canonical Representative Problems**:
   - `W1A-06` (`CF 1721E — Prefix Function Queries`), `W1A-18` (`CF 1286E — Fedya the Potter Strikes Back`), `W1A-22` (`CF 1764G / Inverse Border Realizability`), `W1A-28` (`[SDOI2019] 连续子序列`).

---

### `T-1A-03`. Border-Group Modulo Shortest Path (`同余最短路 + 等差数列背包`)
1. **Multilingual Name**:
   - `[EN]`: Border-Group Modulo Shortest Path via Dynamic Modulus Switching & Residue-Cycle Monotonic Queues
   - `[ZH]`: 同余最短路 + Border 等差数列分组背包（动态模数切换与环上单调队列）
   - `[JA]`: ボーダー等差数列分解による同余最短路・剰余環上のスライド最小値DP
2. **Diagnostic Signal**:
   - Given a string $S[1..N]$ ($N \le 5 \times 10^5$) and huge target length $W \le 10^{18}$, we repeatedly append $S$ overlapping by any border $b \in \text{Border}(S)$ (adding period weight $p = N - b \in \text{Per}(S)$) and must count achievable lengths $\le W$ or find minimum-weight combinations.
3. **Core Combinatorial Word Invariant**:
   - By Period–Border Duality and `T-1A-02`, the $\Theta(N)$ period weights $\text{Per}(S) = \{N - b : b \in \text{Border}(S)\}$ partition into $K \le \lceil \log_2 N \rceil$ arithmetic progressions $\mathcal{A}_k = \{x_k + j \cdot d_k \mid 0 \le j \le c_k\}$ where $x_k = N - b_{\max, k}$ and $d_k = \text{diff}[b_{\max, k}]$.
   - Switching the shortest-path modulus dynamically to $m = x_k$ makes the base item $x_k \equiv 0 \pmod{x_k}$ free (0 residue shift) and turns the remaining items $x_k + j \cdot d_k$ ($1 \le j \le c_k$) into a bounded-width sliding window of width $c_k$ along each of the $\gcd(d_k, x_k)$ directed cycles of step $+d_k \pmod{x_k}$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Initialize $m = N, D[0] = N, D[1..N-1] = +\infty$. For each AP block $(x_k, d_k, c_k)$:
     1. **Modulus Switch ($m_{\text{old}} \to x_k$)**: Project $D_{\text{old}}[r]$ to $D_{\text{new}}[D_{\text{old}}[r] \bmod x_k]$. On each of the $\gcd(m_{\text{old}}, x_k)$ cycles of step $+m_{\text{old}} \pmod{x_k}$, start at the cycle argmin $u_{\min}$ and relax $x_k / \gcd(m_{\text{old}}, x_k) - 1$ steps forward by $+m_{\text{old}}$.
     2. **Residue-Cycle Monotonic Queue**: On each of the $\gcd(d_k, x_k)$ cycles of step $+d_k \pmod{x_k}$, unroll the cycle into a linear DAG starting at its argmin $v_0$, and relax $D[v_t] \leftarrow \min(D[v_t], x_k + t \cdot d_k + \min_{t - c_k \le s \le t - 1} (D[v_s] - s \cdot d_k))$ using a monotonic deque.
   - **Complexity**: $O(N \log N)$ time and $O(N)$ space.
5. **Canonical Failure Modes & Counterexamples**:
   - **0-1 vs. Unbounded Deque Push Order (`BP-1A-04`)**: Pushing the old value $D_{\text{old}}[v_t] - t \cdot d_k$ into the monotonic deque *before* updating $D[v_t]$ from `dq.front()` restricts each pass to using at most one period from $\mathcal{A}_k$. Because periods in $\mathcal{A}_k$ can be used repeatedly (unbounded knapsack), you **must** update $D[v_t]$ from `dq.front()` *first* and then push the updated $D[v_t] - t \cdot d_k$ into `dq`.
   - **Starting Cycle Relaxation at Vertex $0$ Instead of Argmin**: Starting the DAG unrolling at an arbitrary vertex $r$ instead of $v_0 = \arg\min D[v]$ fails to propagate across the wrap-around boundary of the cycle.
6. **Canonical Representative Problems**:
   - `W1A-33` (`[WC2016] 论战捆竹竿` / Luogu P4156 / UOJ #179), `W1A-38` (Weighted / Bounded-Copy Border Modulo Shortest Path variants).

---

### `T-1A-04`. Series-Link (`slink` / `diff`) DP Acceleration on PAM & KMP (with Double-End Interleaving)
1. **Multilingual Name**:
   - `[EN]`: Series-Link (`slink` / `diff`) DP Acceleration on Palindromic & KMP Automata (with Double-End Interleaving Bijection)
   - `[ZH]`: 回文自动机与 KMP 上的等差数列跳链 (`slink` / `diff`) DP 优化（含首尾穿插构造）
   - `[JA]`: 回文木 (PAM)・KMP 上の直列リンク (`slink`) DP 高速化と交互配置帰着
2. **Diagnostic Signal**:
   - A 1D string partition DP $dp[r] = \bigoplus_{L \in \mathcal{A}(r)} dp[r - L]$ transitions over all palindromic suffixes (or all borders) of $S[1..r]$ at $N \le 10^6$, or partitions $S[1..N]$ into symmetric pairs $s_1 s_2 \dots s_k$ ($s_i = s_{k+1-i}$) or interval reversals $A[l..r]^R = B[l..r]$.
3. **Core Combinatorial Word Invariant**:
   - **Shift-Overlap Invariant (`Theorem 4.1`)**: Let $u$ be a `slink` chain head at right endpoint $r$, with step $d = \text{diff}[u]$ and half-open chain $(\text{slink}[u], u]$ of lengths $\ell_1 > \ell_2 > \dots > \ell_k = \text{len}[\text{slink}[u]] + d$. When $\text{diff}[u] = \text{diff}[\text{fail}[u]] = d$, the left endpoints $\mathcal{I}(u, r) = \{r - \ell_1, \dots, r - \ell_k\}$ decompose as:
     $$\mathcal{I}(u, r) = \mathcal{I}(\text{fail}[u],\, r - d) \;\sqcup\; \bigl\{\,r - \text{len}[\text{slink}[u]] - d\,\bigr\}.$$
   - **Why $g[\text{fail}[u]]$ Is Up-to-Date at $r - d$**: Node $v = \text{fail}[u]$ occurred as a suffix at $r - d$ (since $v$ is a prefix of $u$), was a `slink` chain head at $r - d$ (since $u$ is the unique fail-tree child of $v$ with period $d \le \text{len}[v]$, and if $u$ had occurred at $r - d$, gluing $u$ at $r-d$ and $u$ at $r$ would extend $u$ by $+d$ at $r$, contradicting that $u$ is a chain head at $r$), and was never visited in $(r - d, r)$ (by minimum period $d$ of $u$).
   - **Double-End & Reversal Interleaving Bijections**:
     - Symmetric blocks $S[1..m] = S[N-m+1..N] \iff$ prefix $T[1..2m]$ of $T = S[1]S[N]S[2]S[N-1]\dots$ is an even-length palindrome (`CF 932G`).
     - Reversed blocks $A[l..r]^R = B[l..r] \iff T[2l-1..2r]$ of $T = A[1]B[1]A[2]B[2]\dots$ is an even-length palindrome (`CF 906E`).
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - At each $r = 1 \dots N$, advance PAM to `last` and loop `for (int u = last; u > 0; u = slink[u])`:
     1. Initialize `g[u] = dp[r - len[slink[u]] - diff[u]]`.
     2. If `diff[u] == diff[fail[u]]`, combine `g[u] = op(g[u], g[fail[u]])`.
     3. Combine `dp[r] = op(dp[r], g[u])` (gated on `r % 2 == 0` for interleaved strings).
   - **Complexity**: $O(N \log N)$ time and $O(N)$ space.
5. **Canonical Failure Modes & Counterexamples**:
   - **The "$r - \text{len}[u]$ vs. $r - \text{len}[\text{slink}[u]] - \text{diff}[u]$" Trap (`BP-1A-05`)**: Initializing `g[u] = dp[r - len[u]]` instead of `dp[r - len[slink[u]] - diff[u]]`. Because $r - \text{len}[u] = (r - d) - \text{len}[\text{fail}[u]]$, the longest palindrome's left endpoint $r - \text{len}[u]$ is the **oldest** element and is **already stored inside $g[\text{fail}[u]]$**! The single new element entering at step $r$ is the **shortest** member of $(\text{slink}[u], u]$, at $r - \text{len}[\text{slink}[u]] - \text{diff}[u]$.
   - **Skipping Odd Positions in `g[u]` Maintenance (`BP-1A-06`)**: In `CF 932G` / `CF 906E`, only even $r$ update `dp[r]`, but `g[u]` **must** still be updated at odd $r$ because an even position $r$ with odd $\text{diff}[u] = d$ reads `g[fail[u]]` from the odd position $r - d$!
6. **Canonical Representative Problems**:
   - `W1A-25` (`CF 932G — Palindrome Partition`), `W1A-26` (`CF 906E — Reverses`), `W1A-27` (`[CERC 2014] Virus Synthesis`), `W1A-34` (Minimum/Odd-Even Palindrome Factorizations).

---

### `T-1A-05`. Polynomial-Weighted (`w(L) = P(L)`), Parity-Filtered & Length-Windowed `slink` DP
1. **Multilingual Name**:
   - `[EN]`: Binomial-Split Polynomial-Weighted `slink` DP & Windowed/Parity-Filtered Series-Link Accumulation
   - `[ZH]`: 多项式带权 `slink` DP（二项式左端点拆分）、奇偶过滤与长度受限 `slink` DP
   - `[JA]`: 多項式重み付き `slink` DP（二項展開分離）と長さ制約付き回文木DP
2. **Diagnostic Signal**:
   - A palindrome/border partition DP has transition weight $w(L) = P(L) = \sum_{m=0}^D c_m L^m$ depending polynomially on the palindrome/border length $L$, or restricts transitions to even-length / odd-length palindromes or length windows $L \in [L_{\min}, L_{\max}]$.
3. **Core Combinatorial Word Invariant**:
   - **Binomial Left-Endpoint Invariance**: While the length $L = r - i$ increases by $+d$ when shifting from $r - d \to r$, the **left endpoint $i = r - L \in \mathcal{I}(u, r)$ is 100% invariant**! Expanding $(r - i)^m = \sum_{t=0}^m \binom{m}{t} (-1)^t r^{m-t} i^t$ separates the changing right endpoint $r^{m-t}$ from the shift-invariant left-endpoint moments $i^t \cdot dp[i]$.
   - **Monotonic Left-Endpoint Arrival Order**: In any `slink` chain $(\text{slink}[u], u]$, the new left endpoint $i_{\text{new}} = r - \text{len}[\text{slink}[u]] - d$ is strictly larger than all existing left endpoints in $\mathcal{I}(\text{fail}[u], r - d)$, so $\mathcal{I}(u, r)$ is a sliding window with newest element $r - \text{len}[\text{slink}[u]] - d$ and oldest element $r - \text{len}[u]$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - For degree-$D$ polynomial weights, maintain $D+1$ accumulators $g_t[u] = \sum_{i \in \mathcal{I}(u, r)} i^t dp[i]$ ($0 \le t \le D$) per node in $O(D \cdot N \log N)$ time.
   - For length-parity constraints when both odd and even $r$ are active, maintain $g_{\text{even\_i}}[u]$ and $g_{\text{odd\_i}}[u]$ partitioned by $i \bmod 2$ in $O(N \log N)$ time.
5. **Canonical Failure Modes & Counterexamples**:
   - Attempting to maintain $\sum L^m dp[r-L]$ directly via $g[u] = g[\text{fail}[u]] + \dots$ without binomial expansion fails because every term in $g[\text{fail}[u]]$ had length $L - d$ instead of $L$.
6. **Canonical Representative Problems**:
   - `W1A-39` (Polynomial-Weighted Palindrome Partition DP), `W1A-40` (Length-Bounded & Parity-Restricted Palindrome Partitioning).

---

## Wave 1B: Lyndon Words, Duval's Algorithm, Significant Suffixes, Lyndon Trees & The Runs Theorem

### `T-1B-01`. Chen–Fox–Lyndon (CFL) Factorization, Duval's Algorithm, All-Prefix State Sharing & RLE Duval
1. **Multilingual Name**:
   - `[EN]`: Chen–Fox–Lyndon (CFL) Factorization, Duval's $O(N)$ Three-Pointer Automaton, All-Prefix State Sharing & $O(M)$ RLE Duval
   - `[ZH]`: Chen–Fox–Lyndon (CFL) 分解、Duval 三指针算法、全前缀状态共享与 RLE 游程编码 Lyndon 分解
   - `[JA]`: Chen–Fox–Lyndon 分解・Duval のアルゴリズム・全接頭辞状態共有と RLE Lyndon 分解
2. **Diagnostic Signal**:
   - Problems requiring lexicographically extremal cyclic shifts, greedy concatenation ordering ($A^\omega < B^\omega$), longest Lyndon prefixes, smallest suffixes of all prefixes $S[1..r]$ in $O(N)$ time, or Lyndon factorization of a Run-Length Encoded string $S = c_1^{a_1} \dots c_M^{a_M}$ ($\sum a_t \le 10^{18}, M \le 10^5$).
3. **Core Combinatorial Word Invariant**:
   - **Four-Way Lyndon Equivalence (`Theorem 2.1`)**: $w \in \mathcal{L} \iff \forall w=uv, uv < vu \iff \forall w=uv, w < v \iff \forall w=uv, w \prec v \iff w = uv$ with $u, v \in \mathcal{L}, u < v$.
   - **CFL Uniqueness (`Theorem 2.2`)**: Every $S \in \Sigma^+$ factors uniquely as $S = w_1 w_2 \dots w_k$ with $w_i \in \mathcal{L}$ and $w_1 \ge w_2 \ge \dots \ge w_k$. Here $w_1$ is the longest Lyndon prefix of $S$, and $w_k$ is the lexicographically smallest nonempty suffix of $S$.
   - **All-Prefix Duval State-Sharing Invariant (`Theorem 2.4`)**: When Duval's inner loop at outer anchor $i$ inspects $S[r]$ with current period $p = r + 1 - j$ and $S[i..r] = w^d w'$ ($d = \lfloor (r - i + 1)/p \rfloor \ge 1, |w'| < p$), the CFL factorization of $S[1..r]$ equals the frozen factors of $S[1..i-1]$, plus $d$ copies of $w = S[i..i+p-1]$, plus the CFL factorization of $w' = S[i+dp..r]$—which is **identical up to shift $+dp$** to the CFL state at $r' = r - dp$ visited in the exact same outer phase!
   - **RLE Block Boundary Invariant (`Lemma 2.5`)**: No Lyndon factor of length $> 1$ ever starts or ends strictly inside a unary block $c_t^{a_t}$; every non-unary Lyndon factor aligns with exact RLE block boundaries.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Standard Duval runs in $< 2N$ character comparisons ($O(N)$ time, $O(1)$ auxiliary space) via potential $\Phi = 2i + k$.
   - All-prefix CFL factor count `cnt[r]` and minimum suffix `min_suf[r]` update in $O(1)$ per step from $r' = r - dp$.
   - RLE Duval runs on $M$ blocks $(c_t, a_t)$ in $O(M)$ time.
5. **Canonical Failure Modes & Counterexamples**:
   - **Prefix Maximum Suffix Asymmetry**: Taking the last CFL factor under reversed alphabet $>$ does **not** give the longest prefix when ties occur; instead, under reversed alphabet $>$, the starting index of the lexicographically largest suffix of $S[1..r]$ is simply the active outer pointer $i$ of Duval's loop!
6. **Canonical Representative Problems**:
   - `W1B-02` (`CF 1537E2 — Erase and Extend`), `W1B-05` (`ARC 050 D — Suffix Concat`), `W1B-15` (`Luogu P6127` / All-Prefix CFL Factorization via $r \to r - dp$), `W1B-35` ($O(M)$ RLE Lyndon Factorization).

---

### `T-1B-02`. The Bijective Burrows–Wheeler Transform (`BWTS` / `BBWT`) & Witt's Necklace Formula
1. **Multilingual Name**:
   - `[EN]`: Bijective Burrows–Wheeler Transform (`BWTS` / `BBWT`), Witt's Lyndon Formula & FKM De Bruijn Generation
   - `[ZH]`: 双射 Burrows–Wheeler 变换 (`BBWT`)、Witt 项链公式与 FKM 字典序最小 De Bruijn 序列
   - `[JA]`: 全単射 Burrows–Wheeler 変換 (`BBWT`)・Witt の公式と FKM アルゴリズム
2. **Diagnostic Signal**:
   - Transforming a string $S \in \Sigma^N$ into $T \in \Sigma^N$ bijectively **without** appending an end-of-string sentinel $\$$, inverting multi-component BWTs (disjoint cycles of LF-mapping), or generating lexicographically smallest Eulerian / De Bruijn cycles in $O(1)$ amortized time per character.
3. **Core Combinatorial Word Invariant**:
   - **Witt's Identity**: Grouping $\Sigma^N$ by primitive root length $d \mid N$ yields $\sigma^N = \sum_{d \mid N} d \cdot L_\sigma(d) \iff L_\sigma(N) = \frac{1}{N}\sum_{d \mid N} \mu(N/d)\sigma^d$.
   - **Bijective BWT Cycle-Lyndon Bijection (Gil–Scott 2012; Kufleitner 2009)**: Factoring $S = w_1 w_2 \dots w_k$ ($w_1 \ge \dots \ge w_k, w_i \in \mathcal{L}$) and sorting all $N = \sum |w_i|$ cyclic rotations of all factors $w_i$ under the infinite periodic order $X^\omega \le Y^\omega$ defines a bijection $\text{BWTS} : \Sigma^N \leftrightarrow \Sigma^N$. Conversely, decomposing the LF-mapping $\pi_{LF}$ of any $T \in \Sigma^N$ into disjoint cycles yields one primitive necklace per cycle, whose unique Lyndon rotations sorted in non-increasing order $w_1 \ge \dots \ge w_k$ uniquely reconstruct $S$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Forward $\text{BWTS}$: CFL factorize $S$ in $O(N)$ via Duval, then sort rotations of $w_i$ via Cyclic SA-IS in $O(N)$.
   - Inverse $\text{BWTS}$: Build $\pi_{LF}$ in $O(N)$, extract disjoint cycles, rotate each cycle to its minimum Lyndon shift via Duval in $O(|\text{cycle}|)$, and sort factors in $O(N)$.
5. **Canonical Failure Modes & Counterexamples**:
   - Sorting cyclic shifts of $w_i$ by finite string comparison $X < Y$ instead of infinite periodic order $X^\omega < Y^\omega$ breaks the LF-mapping bijection when one factor is a prefix of another (e.g., $\texttt{ab}$ vs. $\texttt{aba}$).
6. **Canonical Representative Problems**:
   - `W1B-18` (FKM $k$-ary De Bruijn Lexicographical Generation), `W1B-36` (Bijective BWT Forward & Inverse Reconstruction), `W5A-31` (Multi-Cycle BWT Necklace Counting).

---

### `T-1B-03`. Significant Suffixes (`显著后缀`) Theorem, Segment Tree 1-Survivor `pushup` & Dyadic SA-Rank RMQ Bands
1. **Multilingual Name**:
   - `[EN]`: The Significant Suffixes Theorem, Segment Tree 1-Survivor `pushup` & Segment-Tree-Free Dyadic SA-Rank RMQ Extraction
   - `[ZH]`: 显著后缀 (`Cand`) 定理、线段树 `pushup` 单存留者定理与无线段树倍增 SA-RMQ 提取
   - `[JA]`: 有意接尾辞 (`Significant Suffixes`) 定理・セグメント木単一生存補題と二進帯域 SA-RMQ
2. **Diagnostic Signal**:
   - Querying the lexicographically minimal (or maximal) suffix or cyclic shift of a substring $S[l..r]$, or maintaining suffix optima under right-extensions $S[i..r] + T$ (such as merging Segment Tree intervals $[L, M]$ and $[M+1, R]$ in `[ZJOI2017] 字符串`, or online prefix cyclic shifts in `[JSOI2019] 节日庆典`).
3. **Core Combinatorial Word Invariant**:
   - **Tandem-Annihilation & Doubling Theorem (`Theorem 3.1` — Jin Ce 2019; Kociumaka et al.)**: If two suffixes $u, v \in \text{Suf}(U)$ satisfy $|u| < |v| < 2|u|$ and $u \sqsubset v$, then $u$ is a border of $v$ of length $> |v|/2$, forcing $u = w u'$ and $v = w^2 u'$ for some nonempty $u' \in \text{Suf}(U)$ and period block $w$ ($|w| = |v| - |u|$). By left-cancellation invariance of lexicographical order, for **every** right-extension $T \in \Sigma^*$:
     $$\min(u'T,\; vT) < uT < \max(u'T,\; vT).$$
     Thus the middle suffix $u$ can **never** minimize or maximize $xT$, and surviving candidates $u_1 \sqsubset u_2 \sqsubset \dots \sqsubset u_k$ satisfy $|u_{i+1}| \ge 2|u_i|$, bounding $|\text{Cand}(U)| \le \lfloor \log_2 |U| \rfloor + 1$.
   - **The Segment Tree `pushup` 1-Survivor Theorem (`Theorem 3.2`)**: When merging `left_child` $[L, M]$ and `right_child` $[M+1, R]$, all suffixes starting in $[L, M]$ have lengths in $[R-M+1, R-L+1]$ inside $[L, R]$. Since $R-L+1 \le 2(R-M+1)$, **at most ONE candidate from `left_child` can survive in $\text{Cand}([L, R])$**!
   - **Static $T = \varepsilon$ Shortest-Border Reduction**: For static $S[l..r]$ and $T = \varepsilon$, let $i_0 = \arg\min_{i \in [l, r]} \text{rk}[i]$; the minimum suffix of $S[l..r]$ is the **shortest nonempty border** of $W = S[i_0..r]$ (or $W$ itself if unbordered).
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - **Online Prefix (`[JSOI2019]`)**: Maintain $\text{Cand}_{\min}(S[1..r])$ in $O(\log r)$ per step; compare candidates via $O(1)$ Z-array lookups in $O(N \log N)$ total time.
   - **Segment Tree (`[ZJOI2017]`)**: Build in $\sum \frac{N}{2^h} O(h) = O(N)$ time; answer $[l, r]$ by testing $\le 1$ survivor from each of the $O(\log N)$ canonical Segment Tree nodes, using a $\sqrt{N}$-block rolling hash ($O(\sqrt{N})$ range-add, $O(1)$ hash $\implies O(\log N)$ LCE) in $O(Q \log^2 N + N\sqrt{N})$ time.
   - **Segment-Tree-Free Dyadic SA-RMQ (`Section 3.5`)**: Partition $[1, r-l+1]$ into $\le \lfloor \log_2(r-l+1) \rfloor + 1$ dyadic bands $B_k = [2^k, 2^{k+1})$, query $i_k = \arg\min_{x \in I_k} \text{rk}[x]$ in $O(1)$, shift $i_k$ to the leftmost period copy in $I_k$ via one $O(1)$ LCE query, and filter in **$O(\log(r-l+1))$ time and $O(N)$ global space**.
5. **Canonical Failure Modes & Counterexamples**:
   - **Left-Truncation Non-Inclusion ($\text{Cand}_{\min}(S[l..r]) \not\subseteq \text{Cand}_{\min}(S[1..r])$)**: On $S = \texttt{aaba}$, $\text{Cand}_{\min}(S[1..4]) = \{\texttt{a}(4), \texttt{aaba}(1)\}$ kills $\texttt{aba}(2)$ because $\texttt{aaba} \prec \texttt{aba}$. On $[l, r] = [2, 4]$ ($S[2..4] = \texttt{aba}$), index $1$ is cut off and $\texttt{aba}(2)$ revives! On $S = \texttt{abbb}, [2, 4]$, $\text{Cand}_{\min}(S[1..4]) \cap [2, 4] = \{1\} \cap [2, 4] = \emptyset$.
   - **Appending $+\infty$ for Maximum Suffix**: At $T = \varepsilon$, $u \sqsubset v \implies u < v$, so the **longer** suffix $v$ wins for Maximum Suffix. Appending $+\infty$ falsely makes the shorter prefix $u$ win.
6. **Canonical Representative Problems**:
   - `W1B-03` (`[JSOI2019] 节日庆典` / Luogu P5287), `W1B-22` (`[ZJOI2017] 字符串` / Luogu P3642), `W1B-25` (Substring Minimum Cyclic Shift Queries), `W1B-37` (Tree Path Significant Suffixes via HLD).

---

### `T-1B-04`. Lyndon Arrays, Double-Order ($<$ / $>$) Monotonic Stacks & Min-Cartesian Lyndon Tree Isomorphism
1. **Multilingual Name**:
   - `[EN]`: Lyndon Arrays ($\lambda_<, \lambda_>$), Double-Order Monotonic Stacks & Min-Cartesian Lyndon Tree Isomorphism
   - `[ZH]`: Lyndon 数组、正反双序单调栈与 Lyndon 树的笛卡尔树同构
   - `[JA]`: Lyndon 配列・双順序単調スタックと Lyndon 木の Cartesian Tree 同型
2. **Diagnostic Signal**:
   - Computing the longest Lyndon prefix $\lambda[i]$ starting at every index $i \in [1..N]$ in $O(N)$ time (as required for $O(N)$ Runs enumeration), building the Lyndon Tree of $S$, or maintaining online/persistent Lyndon factorizations in worst-case $O(\log N)$ time per step.
3. **Core Combinatorial Word Invariant**:
   - **Next-Smaller-Suffix Identity (`Theorem 4.1`)**: Viewing $S[N+1..N] = \varepsilon$ as $-\infty$, the right endpoint $R_{\mathcal{L}}[i] = i + \lambda[i] - 1$ of the longest Lyndon prefix starting at $i$ satisfies $R_{\mathcal{L}}[i] + 1 = \text{nsv}[i] = \min\{j \in [i+1, N+1] \mid S[j..N] < S[i..N]\}$.
   - **Min-Cartesian Tree Isomorphism (`Theorem 4.2`)**: In $\$S[1..N]$, the standard factorization $w = uv$ of any Lyndon node $S[l..r]$ splits at $m = \arg\min_{j \in [l+1, r]} \text{rk}[j]$. Thus the internal nodes of the Lyndon Tree of $\$S[1..N]$ are **canonically isomorphic to the Min-Cartesian Tree of $\text{rk}[2..N+1]$**, where Cartesian node $m$ with range $[L_m, R_m]$ represents the Lyndon word $S[L_m - 1 .. R_m]$ (notice the $-1$ left shift!).
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Scan $i = N$ down to $1$ with a monotonic stack over $\text{rk}_<[i]$ and $\text{rk}_>[i]$ to compute $R_{\mathcal{L}, <}[1..N]$ and $R_{\mathcal{L}, >}[1..N]$ in $O(N)$ time.
   - For persistent/online worst-case $O(\log N)$ Lyndon factorization (`Section 4.4`), maintain the decreasing CFL stack with binary-lifting pointers on the right spine of the Lyndon Tree.
5. **Canonical Failure Modes & Counterexamples**:
   - **The $S = \texttt{bab}$ Negated-Rank Trap**: Negating $\text{rk}_<$ to $-\text{rk}_<$ to simulate reversed alphabet order $>$ is **wrong** whenever one suffix is a proper prefix of another! On $S = \texttt{bab}$, $\text{rk}_< = [3, 1, 2]$ ($\texttt{ab} < \texttt{b} < \texttt{bab}$). Negating gives $[ -3, -1, -2 ]$, claiming $\texttt{bab} <_> \texttt{b}$ and falsely labeling the bordered string $\texttt{bab}$ as a $>-$Lyndon word! You **must** either build a second SA on the character-inverted string $\overline{S}[t] = |\Sigma| + 1 - S[t]$ (keeping sentinel $0 = -\infty$) or compare via $O(1)$ LCE where shorter prefixes always remain smaller ($S[j..N] \sqsubset S[i..N] \implies S[j..N] <_> S[i..N]$).
6. **Canonical Representative Problems**:
   - `W1B-12` (`Luogu P6127` / Lyndon Array Construction), `W1B-19` (`AGC 023 F — 01 on Tree` / Lyndon Tree Greedy Merge), `W1B-28` (Longest Lyndon Substring in $S[l..r]$), `W1B-39` (Persistent Online Lyndon Factorization).

---

### `T-1B-05`. The Runs (`极长周期子串`) Theorem (Bannai et al.), $< 2N$ Representative Squares & 2D Run Sweeps
1. **Multilingual Name**:
   - `[EN]`: The Runs Theorem (Bannai–I Tomohiro–Inenaga–Nakashima–Takeda–Tsuruta 2017), $< 2N$ Representative Squares Lemma & 2D Sweep-Line over Runs
   - `[ZH]`: Runs 定理（极长周期子串定理）、$< 2N$ 本质不同平方串代表元引理与二维扫描线
   - `[JA]`: Runs 定理（極大周期部分文字列の線形性）・代表平方数補題と 2 次元平面走査
2. **Diagnostic Signal**:
   - Counting, summing, or querying periodic substrings, squares $w^2$, $k$-th powers $w^k$, or $AABB$ decompositions across $S$ or inside substring queries $S[L_q..R_q]$ (`[NOI2016] 优秀的拆分`, `[BJWC2018]`, Universal Cup Runs problems).
3. **Core Combinatorial Word Invariant**:
   - **Lyndon-Root Disjointness Proof of $|\mathcal{R}(S)| < N$ & $\sum \text{exp}(R) < 3N$ (`Theorem 5.2`)**: For each run $R = [l, r, p]$, choose the unique order $<_R \in \{<_0, <_1\}$ under which $S[r+1] <_R S[r+1-p]$ (with $S[N+1] = -\infty$). Every full period window inside $[l+1, r-p+1]$ contains a $<_R$-Lyndon root $S[i..i+p-1]$ with $i \ge l+1 \ge 2$ and $\lambda_{<_R}[i] = p$ (frozen by Duval Case 3 at $r+1$). Because $i - 1 \ge l$ lies inside $R$, $S[i-1] = S[i+p-1]$ is the last character of the Lyndon word $S[i..i+p-1]$, forcing $S[i] <_R S[i-1]$. Since $S[i] < S[i-1]$ and $S[i] > S[i-1]$ are mutually exclusive, the interior Lyndon-root sets $B(R) \subseteq \{2, \dots, N\}$ are **pairwise disjoint** across all runs $R \in \mathcal{R}(S)$, proving $|\mathcal{R}(S)| \le N - 1$ and $\sum \text{exp}(R) < 3N$.
   - **The $< 2N$ Representative Squares Lemma**: Across all runs $R = [l, r, p]$ and all harmonics $k \ge 1$ ($2kp \le r - l + 1$), the canonical square representatives starting at $a \in [l, \min(l + p - 1, r - 2kp + 1)]$ inject into primitive-square start positions $a + 2(k-1)p \in [l, r - 2p + 1]$, so their total count is **strictly less than $2N$**!
   - **Fine–Wilf Substring Run-Clipping Non-Collision**: No two distinct global runs $R_1, R_2$ ($p_1 < p_2$) can clip to the same sub-interval of length $\ge 2p_2$ inside $S[L_q..R_q]$, because overlap $\ge 2p_2 > p_1 + p_2 - \gcd(p_1, p_2)$ would force period $\gcd(p_1, p_2) < p_2$ on $R_2$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - **Enumeration**: Either (a) $O(N \log N)$ harmonic LCE checkpoint gluing at $(kp, (k+1)p)$, or (b) $O(N)$ Lyndon-array seeding $j = R_{\mathcal{L}, \prec}[i], p = j - i + 1, l = i - \text{LCS}(i-1, j), r = j + \text{LCP}(i, j+1)$, filtering $r - l + 1 \ge 2p$ and deduplicating $(l, r)$ keeping minimum $p$.
   - **2D Range Queries**: Each run $R = [l, r, p]$ induces structured 2D lines/rectangles in $(L, R)$-space swept via Fenwick/Segment Trees in $O((N + Q)\log N)$ time.
5. **Canonical Failure Modes & Counterexamples**:
   - **Non-Primitive Harmonic Duplicates in Method A**: Checkpoints $(kp, (k+1)p)$ also detect non-primitive periods $2p, 3p, \dots$ on the same interval $[l, r]$. Always deduplicate by $(l, r)$ keeping only the **minimum** $p$.
6. **Canonical Representative Problems**:
   - `W1B-01` (`[NOI2016] 优秀的拆分` / Luogu P1117), `W1B-26` (Substring Run Counting $|\mathcal{R}(S[L_q..R_q])|$), `W1B-33` (Sum over Distinct Squares $f(\text{endpos}(w^2), |w|)$), `W1B-40` (Palindromic Runs $w = P_1 P_2$).

---

### `T-1B-06`. The Three-Squares Lemma & Distinct Squares Density Hierarchy (Fraenkel–Simpson / Brlek–Li)
1. **Multilingual Name**:
   - `[EN]`: Crochemore–Rytter Three-Squares Lemma & The Fraenkel–Simpson ($\le 2N$) / Brlek–Li ($\le N - \Theta(\log N)$) Distinct Squares Hierarchy
   - `[ZH]`: 三平方引理与本质不同平方串上界定理（Fraenkel–Simpson $\le 2N$ 与 Brlek–Li $< N$）
   - `[JA]`: 三平方補題と相異なる平方部分文字列の個数評価
2. **Diagnostic Signal**:
   - Bounding or indexing all distinct square substrings $w^2$ occurring in $S$, or proving $O(\log N)$ local square stack depth at a single starting index $i$.
3. **Core Combinatorial Word Invariant**:
   - **Three-Squares Lemma (Crochemore–Rytter 1995)**: If $u^2, v^2, w^2$ are prefixes of $S$ with $0 < |u| < |v| < |w|$ and **$u$ is primitive**, then $|w| \ge |u| + |v|$ (Fibonacci growth).
   - **Last-Occurrence Proof of $\le 2N - 2$ Distinct Squares**: At any index $i \in [1..N]$, at most **two** distinct squares $u^2, v^2$ can have their **last (rightmost)** occurrence in $S$ starting at $i$. If three squares $u^2, v^2, w^2$ ($|u| < |v| < |w|$) had their last occurrence at $i$, then either $2|u| \le |w|$ (so $u^2$ occurs again inside the second half of $w^2$ at $i + |w| > i$) or $|w| < 2|u|$ (forcing $u$ to be non-primitive by the Three-Squares Lemma and shifting $u^2$ by its primitive root $< |w| - |u|$ to occur after $i$).
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Extract the $< 2N$ representative squares from $\mathcal{R}(S)$ (`T-1B-05`) and group identical squares via SAM / Suffix Tree locus lookup in $O(N)$ or $O(N \log N)$ time.
5. **Canonical Failure Modes & Counterexamples**:
   - Assuming at most $2$ squares can **start** at index $i$ (false: $\Theta(\log N)$ primitive squares can start at $i$ along a Fibonacci prefix, and $\Theta(N)$ non-primitive squares start at $i=1$ in $\texttt{a}^N$). The bound $\le 2$ holds only for **last occurrences** starting at $i$!
6. **Canonical Representative Problems**:
   - `W1B-31` (Square-Free String Partitioning DP in $O(N)$), `W1B-34` (Distinct Square Counting & SAM Locus Marking).

---

## Wave 2A: Advanced Suffix Automaton (SAM), Generalized SAM (`广义 SAM`), Endpos Merging & LCT/HLD

### `T-2A-01`. Blumer–Crochemore SAM $\leftrightarrow \text{ST}(S^R)$ Duality & 3-Case Generalized SAM (`广义 SAM`)
1. **Multilingual Name**:
   - `[EN]`: SAM Link-Tree $\leftrightarrow$ Reversed Suffix Tree Duality & 3-Case Generalized SAM (`GSAM`) Construction
   - `[ZH]`: 后缀自动机 Link 树与反串后缀树对偶性、三分支广义后缀自动机 (`广义 SAM`) 与 Trie-BFS 复杂度定理
   - `[JA]`: 接尾辞オートマトン (SAM) と反転接尾辞木の双対性・一般化 SAM (`GSAM`) の Trie-BFS 構築
2. **Diagnostic Signal**:
   - Multi-string substring statistics over $\mathcal{S} = \{S_1, \dots, S_k\}$ ($\sum |S_i| = L$) or a compressed Trie $\mathcal{T}$ of $V$ vertices without sentinel bloat, or converting prefix `LCP` queries on $S$ into Link-Tree LCA queries on $\text{SAM}(S^R)$.
3. **Core Combinatorial Word Invariant**:
   - **Blumer–Crochemore Reversal Duality (`Theorem 3.2`)**: $\mathcal{T}_{\text{link}}(\text{SAM}(S)) \cong \text{ST}(S^R)$ and $\mathcal{T}_{\text{link}}(\text{SAM}(S^R)) \cong \text{ST}(S)$. State $u \in \text{SAM}(S)$ represents the contiguous suffix-length interval $[\text{len}(\text{link}(u)) + 1, \text{len}(u)]$ sharing $\text{endpos}_S(u)$.
   - **3-Case GSAM Invariant & Binary-Alphabet $\Theta(V^2)$ Trie-DFS Theorem (`Theorem 3.3`)**:
     - When extending state $p$ by $c$ in a GSAM: if $\delta(p, c) = q \ne 0$ and $\text{len}(q) = \text{len}(p)+1$ (**Case 2**), return $q$; if $\delta(p, c) = q \ne 0$ and $\text{len}(q) > \text{len}(p)+1$ (**Case 3**), allocate **only one state `clone`** (do not allocate `cur`!) and return `clone`.
     - On a compressed Trie $\mathcal{T}$ of $V$ vertices, **DFS takes $\Theta(V^2)$ worst-case time even on a binary alphabet**: on $\{\texttt{a}^k \texttt{b} \mid 1 \le k \le m\}$ ($V = 2m+1$), visiting $\texttt{a}^m\texttt{b}$ first and backtracking $k = m-1 \dots 1$ triggers Case 3 at every $k$, walking $k+1$ links to redirect $\delta(\texttt{a}^j, \texttt{b}) \leftarrow \text{clone}_k$ for $\sum (k+1) = \Theta(V^2)$ steps! **BFS processes vertices in non-decreasing depth $d = \text{len}(p)$ and runs in strict $O(V|\Sigma|)$ time.**
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - String list $\sum |S_i| = L$: online `extend_gsam` with `last = 1` reset runs in $O(L|\Sigma|)$ time.
   - Compressed Trie of $V$ vertices: BFS over $\mathcal{T}$ calling `extend_gsam(sam[parent], c)` runs in $O(V|\Sigma|)$ time and $\le 2V$ states.
5. **Canonical Failure Modes & Counterexamples**:
   - **Zero-Length Clone Bug (`Counterexample 3.4`)**: Calling single-string `extend(c)` on $\{\texttt{ab}, \texttt{b}\}$ after resetting `last = 1` allocates both `cur = 4` ($\text{len}=1$) and `clone = 5` ($\text{len}=1, \text{link}(4)=5$), creating an unreachable ghost state $4$ with empty length interval $\text{len}(4) - \text{len}(\text{link}(4)) = 0$ that steals $S_2$'s $\text{endpos}$ weight!
6. **Canonical Representative Problems**:
   - `W2A-02` (`[ZJOI2015] 诸神眷顾的幻想乡` / Luogu P3346), `W2A-05` (`CF 204E — Little Elephant and Strings`), `W2A-08` (`[USACO 2017 Dec Plat] Standing Out from the Herd`), `W2A-14` (`CF 452E — Three Strings`).

---

### `T-2A-02`. Compact Directed Acyclic Word Graph (`CDAWG`) & Unamortized Tree/Persistent SAM
1. **Multilingual Name**:
   - `[EN]`: Compact Directed Acyclic Word Graph (`CDAWG` / Maximal Repeats) & Unamortized Deterministic / Persistent SAM
   - `[ZH]`: 紧凑有向无环词图 (`CDAWG` / 极长重复子串) 与可持久化 / 树上不可均摊 SAM
   - `[JA]`: コンパクト有向非巡回単語グラフ (`CDAWG`) と永続・非償却接尾辞オートマトン
2. **Diagnostic Signal**:
   - Compressing unary right-extension chains in $\text{SAM}(S)$ so vertices correspond bijectively to **maximal repeats** ($\overleftarrow{w} = w = \overrightarrow{w}$), or supporting **online tree-branching / persistent version queries** (`append(version_v, c)`) where an adversary repeatedly branches from a state with a long suffix-link chain.
3. **Core Combinatorial Word Invariant**:
   - **Symmetric Maximal-Repeat Vertex Bijection (`Theorem 2.1`)**: Compacting every non-terminal state $u \in \text{SAM}(S)$ of DAG out-degree $1$ yields $\text{CDAWG}(S)$, whose internal vertices correspond bijectively to the maximal repeats of $S$ (substrings that cannot be extended left or right without losing occurrences). Thus $V_{\text{CDAWG}}(S) = V_{\text{CDAWG}}(S^R)$ ($= O(\log N)$ on Fibonacci words).
   - **Persistent Ancestor-Transition Inheritance**: In a persistent single-path SAM on a version tree, each state $u$ maintains $\text{anc\_trans}[u][c] =$ deepest ancestor $p$ on $\mathcal{T}_{\text{link}}$ with $\delta(p, c) \ne 0$, and stores $\delta(u, \cdot)$ as a persistent balanced BST / bitwise trie of depth $\lceil \log_2 |\Sigma| \rceil$. When `clone` splits $q$, it inherits $\text{anc\_trans}[\text{link}(q)]$ with a single point update at $c$, eliminating the amortized link-walk loop!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Persistent SAM extension runs in **worst-case $O(\log |\Sigma|)$ time and space per version step**.
5. **Canonical Failure Modes & Counterexamples**:
   - Running standard amortized `while (p && !ch[p][c]) p = link[p];` across $K$ online 1-character branches from the same state $u$ takes $\Theta(KN) = \Theta(N^2)$ time and overwrites `ch[p][c]` across sibling versions.
6. **Canonical Representative Problems**:
   - `W2A-41` (Online Persistent Version-Tree SAM Queries), `W2B-41` (CDAWG / SCDAWG Maximal Repeat Counting).

---

### `T-2A-03`. SAM + Persistent Segment Tree Merging on $\text{endpos}$ & Substring Containment Clipping
1. **Multilingual Name**:
   - `[EN]`: SAM + Persistent Segment Tree Merging on $\text{endpos}$ & Substring Containment Clipping
   - `[ZH]`: 后缀自动机 + 线段树合并维护 $\text{endpos}$ 集合与子串区间裁剪 (`[l + L - 1, r]`)
   - `[JA]`: SAM 上の永続セグメント木マージ ($\text{endpos}$ 集合管理) と部分文字列区間クリッピング
2. **Diagnostic Signal**:
   - Pattern matching, interval LCS, or lexicographically next substring queries restricted to an arbitrary substring $S[l..r]$ (`[NOI2018] 你的名字`, `CF 1037H`, `CF 666E`, `CF 700E`).
3. **Core Combinatorial Word Invariant**:
   - **Substring Containment Clipping Identity (`Theorem 4.1`)**: A substring $P \in E(u)$ of exact length $L = |P| \in [\text{len}(\text{link}(u)) + 1, \text{len}(u)]$ occurs inside $S[l..r]$ **if and only if**:
     $$L \le r - l + 1 \quad \text{and} \quad \text{endpos}_S(u) \cap [l + L - 1, \, r] \ne \emptyset.$$
   - **Predecessor Maximum-Length Jump (`Corollary 4.2`)**: For state $u \in \text{SAM}(S)$, let $e_{\max} = \max(\text{endpos}_S(u) \cap [1, r])$. Then the longest suffix in $E(u)$ of length $\le L_{\text{raw}}$ occurring in $S[l..r]$ has length $L_{\text{valid}}(u) = \min(L_{\text{raw}}, e_{\max} - l + 1)$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Insert $r$ into $\text{rt}[\text{pos}_S[r]]$ and merge bottom-up along $\mathcal{T}_{\text{link}}$ in decreasing order of $\text{len}(u)$: $\text{rt}[\text{link}(u)] \leftarrow \text{merge}(\text{rt}[\text{link}(u)], \text{rt}[u], 1, N)$, always allocating a **new node `z = ++seg_sz`** when both children are non-zero so historical state roots remain persistent.
   - Locate $S[l..r]$ via binary lifting on $\mathcal{T}_{\text{link}}$ in $O(\log N)$ time, or walk $\text{SAM}(S)$ two-pointer style (`Contract B`).
   - **Complexity**: $O(N \log N)$ preprocessing time and space; $O(\log N)$ per containment/predecessor query.
5. **Canonical Failure Modes & Counterexamples**:
   - **Unclipped $[l, r]$ Overflow (`Counterexample 4.3`)**: On $S = \texttt{"ababa"}, [l, r] = [3, 5]$ ($\texttt{"aba"}$), $P = \texttt{"baba"}$ ($L=4$) has $\text{endpos}_S(P) = \{4\} \subseteq [3, 5]$, so querying $[l, r]$ instead of $[l + L - 1, r] = [6, 5] = \emptyset$ falsely claims a length-4 pattern occurs inside a length-3 substring!
   - **Skipping Intra-State Lengths (`Counterexample 4.4`)**: In `[NOI2018] 你的名字`, jumping $u \leftarrow \text{link}_S(u)$ immediately when $L+1$ fails skips valid shorter lengths inside $[\text{len}(\text{link}_S(u)) + 1, L - 1]$. Always decrement $L \leftarrow L - 1$ (or jump via $e_{\max} - l + 1$) and only follow $\text{link}_S(u)$ when $L == \text{len}(\text{link}_S(u))$.
6. **Canonical Representative Problems**:
   - `W2A-23` (`CF 666E — Forensic Examination`), `W2A-24` (`CF 700E — Cool Slogans`), `W2A-25` (`CF 1037H — Security`), `W2A-34` (`[NOI2018] 你的名字` / Luogu P4770).

---

### `T-2A-04`. Dynamic SAM + Link-Cut Tree (`access` Color-Chain Sweeping / `树点涂色`) & Second-Occurrence Sweeps
1. **Multilingual Name**:
   - `[EN]`: Dynamic SAM + Link-Cut Tree (`access` Color-Chain Sweeping) & LCT Second-Largest $\text{endpos}$ Sweeping
   - `[ZH]`: 动态 SAM + LCT `access` 树点涂色（区间本质不同子串）与次大 $\text{endpos}$ 扫描
   - `[JA]`: 動的 SAM + Link-Cut Tree (`access` 色塗り走査) による区間相異なる部分文字列クエリ
2. **Diagnostic Signal**:
   - **Regime A**: Online character appends to $S$ interleaved with pattern occurrence queries (`[BZOJ 2555]`).
   - **Regime B**: $Q$ range queries $(l, r)$ asking for the number (or polynomial length-weighted sum) of **distinct substrings** (or longest repeated substring) inside $S[l..r]$ (`Luogu P6292`, `[SDOI2017]`).
3. **Core Combinatorial Word Invariant**:
   - **Solid-Chain Last-Occurrence Telescoping (`Section 5.1`)**: When sweeping right endpoint $r = 1 \dots N$, every $w \in E(u)$ of length $\ell \in [\text{len}(\text{link}(u))+1, \text{len}(u)]$ has rightmost occurrence $\text{last}_r(u) = p_{\text{old}}$, starting at $s = p_{\text{old}} - \ell + 1 \in [p_{\text{old}} - \text{len}(u) + 1, p_{\text{old}} - \text{len}(\text{link}(u))]$. Along any vertical solid LCT chain $C = (u_1, \dots, u_k)$ sharing color $p_{\text{old}}$, these intervals tile without gaps into a **single contiguous interval** $[p_{\text{old}} - \text{len}(u_k) + 1, \, p_{\text{old}} - \text{len}(\text{link}(u_1))]$.
   - **Second-Largest Occurrence Invariant (`Corollary 2.3`)**: A substring $w \in E(u)$ occurs **$\ge 2$ times** in $S[l..r]$ iff the second-largest ending position $e_2(u, r)$ of $u$ in $[1, r]$ satisfies $l \le e_2(u, r) - |w| + 1$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - At step $r$, call `access(pos[r])` on $\mathcal{T}_{\text{link}}$. Each detached splay chain $C$ with old color $p_{\text{old}} > 0$ triggers a range $-1$ update on $[p_{\text{old}} - \text{sub\_max}[C] + 1, \, p_{\text{old}} - \text{sub\_min}[C] + 1]$ in a Fenwick/Segment Tree; then color the root-to-`pos[r]` chain with $r$ and add $+1$ on $[1, r]$.
   - **Complexity**: $O(N \log^2 N + Q \log N)$ time and $O(N)$ space.
5. **Canonical Failure Modes & Counterexamples**:
   - **Unpushed Lazy Tag on `clone` Split (`[BZOJ 2555]`)**: When splitting $q \to \text{clone}$ in online LCT-SAM, failing to call `access(q); splay(q);` before copying `val[clone] = val[q]` leaves pending $+1$ lazy tags on ancestors of $q$ unpushed, corrupting `clone`'s subtree size!
   - **Including Root $1$ in `[sub_min, sub_max]`**: Root $1$ represents $\epsilon$ ($\text{len} = 0$) and must have $\text{self\_min}[1] = +\infty, \text{self\_max}[1] = -\infty$.
6. **Canonical Representative Problems**:
   - `W2A-26` (`[BZOJ 2555] SubString`), `W2A-35` (`Luogu P6292 — 区间本质不同子串个数`), `W2A-36` (Shifted-Weight Range Distinct Substrings).

---

### `T-2A-05`. Intra-State Length Stratification & Link-Tree HLD (`[十二省联考 2019] 字符串问题`)
1. **Multilingual Name**:
   - `[EN]`: Intra-State Length Stratification on the SAM Link Tree & HLD Prefix-Suffix Graph Compilation
   - `[ZH]`: SAM 状态内按长度拆点建图 (`[十二省联考 2019] 字符串问题`) 与 Link 树树链剖分优化建图
   - `[JA]`: SAM 状態内長さ順頂点分割と Link 木 HLD によるグラフ構築最適化
2. **Diagnostic Signal**:
   - Building a directed graph or 2-SAT implication system over substrings $A_i, B_j$ where edges depend on whether $B_j$ is a prefix (or suffix) of $A_i$.
3. **Core Combinatorial Word Invariant**:
   - On $\mathcal{T}_{\text{link}}(\text{SAM}(S^R)) \cong \text{ST}(S)$, $B_j$ is a prefix of $A_i$ iff either $u(B_j)$ is a strict ancestor of $u(A_i)$, OR **$u(B_j) = u(A_i)$ and $|B_j| \le |A_i|$**.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Locate each substring $A_i, B_j$ on $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$ via binary lifting. Inside each state $u$, sort all landed substrings by **non-decreasing length**, breaking ties $|B_j| = |A_i|$ by placing **$B_j$ strictly before $A_i$**, and wire them along a linear prefix chain $\text{out}(\text{link}(u)) \to \text{in}(u) \to v_1 \to \dots \to v_k = \text{out}(u)$.
   - **Complexity**: $O((N + n_a + n_b)\log N + m)$ time and space.
5. **Canonical Failure Modes & Counterexamples**:
   - Connecting $B_j$ to the entire state $u(B_j)$ without intra-state sorting adds false edges from longer $B_j$ to shorter $A_i$ landing in the same SAM equivalence class (creating bogus cycles and false `-1` outputs!).
6. **Canonical Representative Problems**:
   - `W2A-37` (`[十二省联考 2019] 字符串问题` / Luogu P5284), `W2A-39` (`[Code+#3] 白金元首与莫斯科` / 2-SAT on Link Tree HLD), `W2A-40` (`CF 1098F — Ж-function`).

---

## Wave 2B: SA-IS, Virtual Suffix Trees, Dominant Pairs, IPM & Bi-Directional Suffix Structures

### `T-2B-01`. Linear-Time Induced Sorting (`SA-IS`), Fischer's Induced LCP & `rk`-Descent Duality
1. **Multilingual Name**:
   - `[EN]`: Linear-Time Induced Sorting (`SA-IS`, Nong–Zhang–Chan 2009), Fischer's Induced LCP & $\text{rk}$-Descent Duality
   - `[ZH]`: 线性时间诱导排序 (`SA-IS`)、Fischer 诱导 `height` 算法与逆后缀数组下降集对偶
   - `[JA]`: 線形時間誘導ソート (`SA-IS`)・誘導 LCP 配列と逆接尾辞配列の降下集合双対性
2. **Diagnostic Signal**:
   - Suffix sorting at scale $N \in [10^6, 10^7]$ or over recursive integer alphabets, upward tree suffix sorting (`ICPC WF 2019 D`), or counting strings with a prescribed Suffix Array / descent set (`AGC 060 D`).
3. **Core Combinatorial Word Invariant**:
   - **$\text{rk}$-Descent Duality**: $\text{type}(i) = L \iff \text{suf}(i) > \text{suf}(i+1) \iff \text{rk}[i] > \text{rk}[i+1]$ (a descent in $\text{rk}$), and LMS positions ($\text{type}(i)=S, \text{type}(i-1)=L$) are the local valleys of $\text{rk}$ ($m \le \lfloor N/2 \rfloor$).
   - **Intra-Bucket $L < S$ Partition (`Lemma 2.2`)**: In every character bucket $\mathcal{B}(c)$, all $L$-type suffixes precede all $S$-type suffixes ($\text{suf}(i) < c^\infty < \text{suf}(j)$).
   - **LMS-Substring Prefix-Free Order Homomorphism (`Theorem 2.4`)**: Under character-and-type comparison $(S[\cdot], \text{type}(\cdot))$ with $L < S$, no LMS-substring is a proper prefix of another (since an $L \to S$ transition occurs only at the right endpoint $p_{a+1}$), and consecutive LMS intervals overlap only at endpoints ($\sum |U_k| < 2N$). Thus naming LMS-substrings preserves global suffix order and halves the problem size.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Two-pass `InduceSort` (Pass 0: seed LMS at bucket tails from $k=m$ down to $1$; Pass 1: left-to-right induce $L$ at bucket heads; Pass 2: right-to-left induce $S$ at bucket tails) runs in $T(N) = T(N/2) + O(N) = O(N)$ time.
   - Fischer (2011) induces $\text{height}[2..N]$ simultaneously via bucket RMQ in $O(N)$ time.
5. **Canonical Failure Modes & Counterexamples**:
   - **Comparing LMS-Substrings Without $L/S$ Types**: Equates `"ab"` where `'b'` is $S^*$ with prefix `"ab"` of `"aba"` where `'b'` is $L$.
   - **Reversed Pass-0 Seed Order / Stale LMS Seeds**: Pushing sorted LMS positions $q_1 \dots q_m$ in increasing order into decrementing bucket tails reverses the LMS order; failing to clear preliminary seeds before Pass 2 corrupts $S$-buckets.
6. **Canonical Representative Problems**:
   - `W2B-07` (`[JSOI2007] 字符加密`), `W2B-08` (`ABC 213 F`), `W2B-31` (`ICPC WF 2019 D — First of Her Name`), `W2B-42` (`AtCoder AGC 060 D — Same Descent Set`).

---

### `T-2B-02`. Three-Way Suffix Tree Isomorphism, `height` Cartesian Trees & Zero-Tree Virtual Suffix Trees (`后缀树虚树`)
1. **Multilingual Name**:
   - `[EN]`: Three-Way Suffix Tree Isomorphism, `height` Min-Cartesian Trees & Zero-Tree Virtual Suffix Trees
   - `[ZH]`: 后缀树三元同构、`height` 笛卡尔树与零显式建树子串虚后缀树 (`后缀树虚树`)
   - `[JA]`: 接尾辞木の三者同型・LCP 配列の Cartesian Tree と圧縮接尾辞木 (Auxiliary Tree)
2. **Diagnostic Signal**:
   - Aggregating $\sum_{u \in A_q} \sum_{v \in B_q} f(\text{LCP}(u, v))$ over query subsets of substrings with $\sum (|A_q| + |B_q|) \le 5 \times 10^5$, or computing global sums/products over all suffix pairs grouped by $\text{LCP} = r$.
3. **Core Combinatorial Word Invariant**:
   - **Three-Way Isomorphism (`Section 3.1`)**: $\mathcal{T}_{\text{ST}}(S) \cong \mathcal{T}_{\text{link}}(\text{SAM}(S^R)) \cong \text{Min-Cartesian Tree}(\text{height}[2..N])$. Internal Cartesian node $u$ with SA span $[L_u, R_u]$ and parent height $h_{p(u)}$ represents $h_u - h_{p(u)}$ distinct substrings each occurring $R_u - L_u + 1 \ge 2$ times.
   - **Zero-Tree Substring Virtual Suffix Tree (`Theorem 3.1`)**: Sorting $k$ arbitrary query substrings $U_t = S[l_t..r_t]$ lexicographically via $O(1)$ LCE comparisons and setting $h_t = \min(\text{LCE}(l_{t-1}, l_t), |U_{t-1}|, |U_t|)$ satisfies $\text{LCP}(U_a, U_b) = \min_{a < t \le b} h_t$; the Min-Cartesian tree of $h_2, \dots, h_k$ is the exact Virtual Suffix Tree of $\{U_1, \dots, U_k\}$ without building an explicit Suffix Tree!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Monotonic stack / Kruskal DSU on $H[2..N]$ in $O(N)$ / $O(N \log N)$ time; Virtual Suffix Tree over $k$ substrings in $O(k \log k)$ time.
5. **Canonical Failure Modes & Counterexamples**:
   - **Omitting $\text{occ} = 1$ Leaf Edges**: Internal nodes of the Cartesian tree of $H[2..N]$ only represent substrings with $\text{occ} \ge 2$; unique substrings ($\text{occ} = 1$) lie on leaf edges of length $(N - \text{SA}[x] + 1) - \max(H[x], H[x+1])$.
   - **Evaluating Uncontracted Equal-Height Nodes with Negative Weights (`CF 616F`)**: Inspects a partial subset of occurrences and produces wrong maxima when weights $c_i < 0$.
6. **Canonical Representative Problems**:
   - `W2B-01` (`[AHOI2013] 差异`), `W2B-03` (`CF 802I`), `W2B-04` (`[NOI2015] 品酒大会`), `W2B-11` (`CF 1073G — Yet Another LCP Problem`), `W2B-15` (`CF 616F — Expensive Strings`).

---

### `T-2B-03`. Suffix Tree Dominant Pairs (`启发式合并支配对`)
1. **Multilingual Name**:
   - `[EN]`: DSU-on-Tree Dominant Pairs on Suffix Trees / `height` Cartesian Trees
   - `[ZH]`: 后缀树 / `height` 笛卡尔树上的启发式合并支配对 (`支配对理论`)
   - `[JA]`: 接尾辞木上のマージテクによる支配ペア列挙 (`Dominant Pairs`)
2. **Diagnostic Signal**:
   - Range queries $[l, r]$ on original string indices optimizing or summing a function of $\text{LCP}(\text{suf}(a), \text{suf}(b))$ (or $\text{LCSuf}(S[1..a], S[1..b])$) over $l \le a < b \le r$ (e.g., longest repeated substring in $S[l..r]$, or $\max_{l \le a < b \le r} (\text{LCP}(a, b) + f(|a-b|))$).
3. **Core Combinatorial Word Invariant**:
   - **Dominant Pair Sparsity & Predecessor/Successor Dominance (`Theorem 3.2`)**: When merging light-subtree original string indices $i$ into the heavy child's `std::set<int>` at Suffix Tree node $u$ (string depth $\ell_u$), let $i^-$ and $i^+$ be the immediate predecessor and successor of $i$ in the heavy set. Any further element $z < i^-$ has $[z, i] \supset [i^-, i]$ and the exact same LCA depth $\ell_u$, so $(i^-, i, \ell_u)$ strictly dominates $(z, i, \ell_u)$ for every query $[l, r]$ (and $(i, i^+, \ell_u)$ strictly dominates any $w > i^+$ in both containment $[l, r]$ and right-clipped length $\min(r - b + 1, \ell_u)$).
   - Across the entire tree, DSU-on-Tree generates **at most $2N \log_2 N$ dominant triples $(a, b, \ell_u)$** capturing all $\binom{N}{2}$ pairwise interactions!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Extract $\le 2N \log_2 N$ triples $(a, b, \ell)$ via DSU-on-Tree in $O(N \log^2 N)$ time.
   - Split clipped contribution $\min(r - b + 1, \ell)$ at threshold $b + \ell - 1 \le r$ into two 2D offline Fenwick / Segment Tree sweeps in $O(N \log^2 N + Q \log N)$ time.
5. **Canonical Failure Modes & Counterexamples**:
   - Forgetting to clip $\ell$ by the right boundary $r - b + 1$ ($b > a$) when querying substrings inside $S[l..r]$ allows matches that extend past $r$.
6. **Canonical Representative Problems**:
   - `W2B-35` (`[UOJ/LOJ/QOJ] 区间最长重复子串` via Dominant Pairs), `W2B-36` (`CF 1043G — Speckled Band`), `W2A-40` (`CF 1098F — Ж-function`).

---

### `T-2B-04`. Kociumaka's Basic Substring Dictionary, Bounded-Ratio IPM & The 6 Methods of Substring Borders (`[BJWC2018]`)
1. **Multilingual Name**:
   - `[EN]`: Basic Substring Dictionary, Bounded-Ratio Internal Pattern Matching (IPM) & The 6 Canonical Methods for Substring Border Queries
   - `[ZH]`: 基本子串字典、有界比例内部模式匹配 (IPM) 与区间 Border 的六种求法 (`[BJWC2018] Border 的四种求法`)
   - `[JA]`: 基本部分文字列辞書・内部パターンマッチング (`IPM`) と部分文字列 Border クエリの 6 手法
2. **Diagnostic Signal**:
   - Answering internal queries on substrings of a static text $S[1..N]$: occurrences of $P = S[l_1..r_1]$ inside $T = S[l_2..r_2]$, longest proper border (or shortest period) of $S[l..r]$ (`[BJWC2018]`), or global lexicographical rank `Rank(S[l..r])` / `Select(K)`.
3. **Core Combinatorial Word Invariant**:
   - **Bounded-Ratio IPM Arithmetic Progression Theorem (`Theorem 4.1` — Kociumaka et al. SODA 2015)**: Whenever $|P| \le |T| < 2|P|$, all occurrences of $P$ in $T$ overlap on a nonempty common core of length $> 0$, forcing $\text{Occ}(P, T)$ to have either $\le 2$ elements or form a **single arithmetic progression** with step $d = \text{per}(P)$.
   - **Dyadic Scale Coverage for Substring Borders**: Any border of $S[l..r]$ of length $b \in [2^m, 2^{m+1}-1]$ is uniquely covered by the prefix $P_m = S[l..l+2^m-1]$ occurring in the tail window $S[r-2^{m+1}+2..r]$ AND the suffix $Q_m = S[r-2^m+1..r]$ occurring in the head window $S[l..l+2^{m+1}-2]$ (since $2^m + 2^m \ge b + 1$ leaves zero unverified gap!).
   - **The 6 Canonical Methods for `[BJWC2018]`**:
     1. *Method 1 (Dyadic $2^m$ IPM + AP Intersection)*: Intersect the AP of $P_m$ in the tail window with the AP of $Q_m$ in the head window across $\le \log_2 N$ scales.
     2. *Method 2 (SAM Link-Tree HLD + SegTree Merge)*: Decompose $\text{LCA}(u_r, u_i) = w$ into $O(\log N)$ light-subtree $\text{endpos}$ queries and heavy-chain $i - \text{len}(w) \le l - 1$ queries.
     3. *Method 3 (Link-Tree Centroid Decomposition `点分治`)*: Split bottleneck $L(u) = \text{len}(\text{LCA}(u, c))$ into two 2D orthogonal range queries $L(u_r) \le L(u_i)$ vs. $L(u_i) < L(u_r)$.
     4. *Method 4 (Link-Tree DSU-on-Tree)*: Offline small-to-large $\text{endpos}$ merge with heavy-path ascents.
     5. *Method 5 ($\sqrt{N}$ SA-Neighborhood Split)*: Test short borders $b \le \sqrt{N}$ via LCE and long borders via $\pm \sqrt{N}$ SA-rank neighbors + periodic buckets.
     6. *Method 6 (Runs Sweep-Line + Short Fallback)*: Long borders $b \ge (r-l+1)/2$ correspond to the unique run $R = [l_R, r_R, p]$ covering $S[l..r]$ with period $p = (r-l+1)-b$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Methods 1–4 run in $O(N \log^2 N)$ time and $O(N \log N)$ space (Method 1 achieves $O(Q \log N)$ with $2^m$-buckets, and $O(1)$ for shortest period $\text{per}(S[l..r])$ via `Corollary 4.2`).
5. **Canonical Failure Modes & Counterexamples**:
   - **One-Sided $P_m$ Check Without $Q_m$ (`Pitfall 2`)**: On $S = \texttt{"ababacababab"}, [1, 12], m = 1$, checking only $P_1 = \texttt{"ab"}$ in the tail misses the mismatch `'c'` at index $6$. Both $P_m$ and $Q_m$ APs must be intersected!
   - **Improper Border $i = r$**: Failing to clip $i \in [l, r - 1]$ returns the full substring $b = r - l + 1$.
6. **Canonical Representative Problems**:
   - `W2B-33` (`[BJWC2018] Border 的四种求法` / Luogu P4482), `W2B-13` (`CF 504E`), `W2B-25` (Substring Global Rank & Select Queries), `W2B-34` ($O(1)$ Internal Period Queries).

---

### `T-2B-05`. Bi-Directional Suffix Structures: SCDAWG & Affix Automata
1. **Multilingual Name**:
   - `[EN]`: Symmetric Compact DAWG (`SCDAWG` — Inenaga et al. 2005) & Affix Automata (Stoye / Maaß 2000)
   - `[ZH]`: 对称压缩有向无环词图 (`SCDAWG`)、词缀自动机与双端在线后缀结构
   - `[JA]`: 対称圧縮 DAWG (`SCDAWG`)・Affix Automaton と双方向オンライン接尾辞構造
2. **Diagnostic Signal**:
   - Online character insertions at **both** front (`push_front(c)`) and back (`push_back(c)`) while maintaining exact substring occurrences, distinct substring counts, or bi-maximal repeats.
3. **Core Combinatorial Word Invariant**:
   - **Two-Sided Closure Commutativity (`Theorem 5.1`)**: Extending $u \in \text{Sub}(S)$ maximally left inside $[u]_R$ and maximally right inside $[u]_L$ commutes: $\text{rep}_L([\text{rep}_R([u]_R)]_L) = \text{rep}_R([\text{rep}_L([u]_L)]_R) = \overleftrightarrow{u}$, yielding $\le N - 1$ internal bi-maximal vertices in $\text{SCDAWG}(S)$.
   - **Ukkonen–Weiner Active-Frontier Duality (`Theorem 5.2`)**: Under `push_back(c)`, Ukkonen's active suffix point advances on $\mathcal{T}_{\text{ST}}(S)$ while Weiner's algorithm inserts a single leaf at $R_{\max}^R$ on $\mathcal{T}_{\text{ST}}(S^R)$, adding $|Sc| - |R_{\max}(Sc)|$ distinct substrings; `push_front(c)` swaps their roles ($+\Delta = |cS| - |L_{\max}(cS)|$).
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Online bi-directional SCDAWG / coupled suffix-prefix maintenance runs in $O(N \log |\Sigma|)$ time and $O(N)$ space.
5. **Canonical Failure Modes & Counterexamples**:
   - Updating only $R_{\max}$ without notifying $L_{\max}$ when an extension causes the entire string $S$ to become a repeated substring ($L_{\max}$ and $R_{\max}$ cross).
6. **Canonical Representative Problems**:
   - `W2B-40` (Online Bi-Directional Distinct Substring Maintenance), `W2B-41` (SCDAWG Prime Factor / Maximal Repeat Queries).

---

### `T-2B-06`. Hash-Free Suffix Balanced Tree (`后缀平衡树`)
1. **Multilingual Name**:
   - `[EN]`: Hash-Free Suffix Balanced Tree via Dietz–Sleator 64-Bit Scapegoat Tags & BST LCP Bootstrapping
   - `[ZH]`: 无哈希后缀平衡树（替罪羊树 64 位整数顺序标签 + BST 区间 RMQ 递推 LCP）
   - `[JA]`: 接尾辞平衡二分探索木 (`Suffix Balanced Tree` / Order-Maintenance Scapegoat Tree)
2. **Diagnostic Signal**:
   - **Online encrypted** `push_front(c)` / `pop_front()` (or `push_back(c)` when querying reversed prefixes) requiring $O(1)$ suffix order comparisons, $O(|P| + \log N)$ pattern counting, or online distinct substring maintenance (`[BZOJ 3682] Phorni`, `[BZOJ 4768]`).
3. **Core Combinatorial Word Invariant**:
   - **Dietz–Sleator 64-Bit Dyadic Tag Invariant (`Theorem 5.3`)**: Maintaining suffixes $\text{suf}(1), \dots, \text{suf}(n)$ in an $\alpha = 0.75$ Scapegoat Tree with 64-bit integer midpoint tags $\text{tag}[x] = (L_x + R_x)/2 \in [0, 2^{62}]$ allows comparing any two existing suffixes in $O(1)$ via $\text{tag}[i] < \text{tag}[j]$, and comparing the newly prepended suffix $\text{suf}(n) = c \cdot \text{suf}(n-1)$ against any BST node $u$ in $O(1)$ via $(c, \text{tag}[n-1]) \lessgtr (S[u], \text{tag}[u-1])$.
   - **Hash-Free Combinatorial LCP Recurrence**: Once $\text{suf}(n)$ is inserted between BST predecessor $u^-$ and successor $u^+$, its adjacent LCP satisfies:
     $$\text{LCP}(\text{suf}(n), u^-) = \bigl(S[n] \ne S[u^-] \;\text{?}\; 0 : 1 + \text{LCP}(\text{suf}(n-1), u^- - 1)\bigr),$$
     where $\text{LCP}(\text{suf}(n-1), u^- - 1)$ is a deterministic **$O(\log n)$ BST range-minimum query** over the adjacent `height` values stored in the Suffix Balanced Tree itself—requiring **zero hashing**!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - $O(\log n)$ amortized insertion/deletion per `push_front`/`pop_front`, $O(1)$ suffix comparison, $O(\log n)$ deterministic LCP, $O(n)$ space.
5. **Canonical Failure Modes & Counterexamples**:
   - **Why `push_back(c)` Cannot Use a Suffix Balanced Tree Directly**: On $S = \texttt{"aa"}$, $\text{suf}(1) = \texttt{"aa"} > \text{suf}(2) = \texttt{"a"}$; after `push_back('b')`, $\text{suf}(1) = \texttt{"aab"} < \text{suf}(2) = \texttt{"ab"}$—their relative order **flips**! A Suffix Balanced Tree must always insert at the **front** (`push_front`) of the strings it sorts.
   - **53-Bit `double` Tag Precision Collapse in Treaps**: Using `double` tags in a randomized Treap overflows the 53-bit IEEE-754 mantissa whenever tree depth $\ge 53$; use an $\alpha = 0.75$ Scapegoat Tree with `uint64_t` tags in $[0, 2^{62}]$ (depth $\le 49$).
6. **Canonical Representative Problems**:
   - `W2B-37` (`[BZOJ 3682] Phorni`), `W2B-38` (`[BZOJ 4768] wxh loves substring`), `W2B-39` (Encrypted Online Tree-Branched Suffix Ranking).


---

## Wave 3A: Advanced Palindromic Trees (PAM), Deque PAM, Range Palindromes & Rich Words

### `T-3A-01`. Unamortized Deterministic PAM (`quick_link` vs. Alphabet-Free `slink`-Skip) & Shared-Trie Tree PAM
1. **Multilingual Name**:
   - `[EN]`: Unamortized Deterministic PAM (`quick_link[u][c]` vs. Alphabet-Free `slink`-Skip) & Shared-Trie Persistent/Tree PAM
   - `[ZH]`: 非均摊确定性回文自动机（`quick_link` 与大字符集 `slink` 跳链）及共用节点树上/可持久化 PAM (`[钟知闲 2017]`)
   - `[JA]`: 非償却決定的回文木 (`quick_link` / `slink` ジャンプ) と木上の永続回文木
2. **Diagnostic Signal**:
   - Extending a PAM along branched version trees (`push`/`pop` with rollbacks), persistent substring snapshots, or tree-path palindrome queries where amortized $O(1)$ `fail` walking degrades to $O(N)$ per step.
3. **Core Combinatorial Word Invariant**:
   - **Uniform Preceding-Character Lemma (`Lemma 1.1`)**: Let $u$ be a PAM state with $\text{diff}(u) = \text{len}(u) - \text{len}(\text{fail}(u)) = d$, and let $v$ be any ancestor on the same arithmetic progression (`diff(v) == d`, `v != slink[u]`). Because $\text{fail}(v)$ is a prefix of $u$ of length $\text{len}(v) - d$ and $u$ has period $d$, the character immediately preceding $\text{fail}(v)$ inside $S[1..i-1]$ equals $S[i - \text{len}(\text{fail}(v)) - 1] = S[i - \text{len}(v) - 1 + d] = S[i - \text{len}(v) - 1]$—identical to the character immediately preceding $v$!
   - Therefore, if $v$ fails the extension test $S[i - \text{len}(v) - 1] = c$, then $\text{fail}(v)$ (and every intermediate node above $\text{slink}(u)$ in the AP) **automatically fails** the test too, allowing a deterministic jump directly to $\text{slink}(u)$ in $O(\log N)$ worst-case time **with zero $|\Sigma|$ memory overhead**!
   - When $|\Sigma| \le 26$, precomputing `quick_link[u][c] = (S[i - len(fail(u)) - 1] == c ? fail(u) : quick_link[fail(u)][c])` finds the extensible ancestor in **$O(1)$ worst-case time**.
   - **Tree / Persistent Shared-Trie Invariant**: Since a PAM node $u$ is uniquely determined by the palindrome string it represents, two tree branches creating the same palindrome share the **exact same PAM node ID $u$**; only the active frontier state `last_u` depends on the branch.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Small $|\Sigma|$: `quick_link[u][c]` gives $O(1)$ worst-case step and $O(N|\Sigma|)$ space.
   - Large $|\Sigma|$: `slink`-skip + persistent functional Trie `ch[u][c]` gives $O(\log^2 N)$ step and $O(N \log N)$ space.
5. **Canonical Failure Modes & Counterexamples**:
   - Using raw `while (S[i - len[u] - 1] != S[i]) u = fail[u]` on a version tree with star branching at $S = \texttt{"a"}^N$ takes $\Omega(N)$ steps per leaf branch ($O(N^2)$ TLE).
6. **Canonical Representative Problems**:
   - `W3A-07` (`Luogu P4555` / Rollback PAM), `W3A-15` (Persistent PAM on Version Trees), `W3A-29` (`[钟知闲 2017]` Tree-Path Palindrome Queries).

---

### `T-3A-02`. Four-Way Double-Ended Deque PAM (`双向回文自动机`)
1. **Multilingual Name**:
   - `[EN]`: Four-Way Double-Ended Palindromic Automaton (`push_front`, `push_back`, `pop_front`, `pop_back`)
   - `[ZH]`: 四向双端回文自动机 (`双向 PAM`, `push/pop_front/back` 惰性表面回文下推)
   - `[JA]`: 両端キュー回文木 (`Deque PAM` — 4 操作対応)
2. **Diagnostic Signal**:
   - Sliding-window palindrome queries or online 4-way deque edits (`push_front`, `push_back`, `pop_front`, `pop_back`) maintaining distinct palindromes, total palindromic occurrences, and longest prefix/suffix palindromes.
3. **Core Combinatorial Word Invariant**:
   - **Palindrome Reversal Self-Duality (`Theorem 2.1`)**: Because every palindrome satisfies $P = P^R$, a single PAM node set $V$ simultaneously indexes both forward and backward extensions!
   - **Unique Vanishing Palindrome Theorem (`Theorem 2.2`)**: Deleting $S[R]$ (`pop_back`) can reduce the occurrence count of **at most one** distinct palindrome to $0$—specifically $u = \text{max\_suff}[R]$, and only when $\text{surf\_cnt}[u] + \text{deg}[u] = 0$.
   - **Non-Cascading Lazy Surface Push-Down (`Theorem 2.3`)**: Maintain for each index $i \in [L, R]$ the longest palindrome starting at $i$ (`max_pref[i]`) and ending at $i$ (`max_suff[i]`). When $u = \text{max\_suff}[R]$ is popped at $R$, its longest proper palindromic suffix $v = \text{fail}(u)$ becomes the new `max_suff[R]` AND (by palindromic symmetry across $[R - \text{len}(u) + 1 .. R]$) is also a prefix of $u$ starting at $l_u = R - \text{len}(u) + 1$, updating `max_pref[l_u] = max_len(max_pref[l_u], v)`! Since $v$ is only promoted to surface status and not deleted, **push-down never cascades**.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Keep allocated PAM nodes permanent (`active` iff `surf_cnt[u] + deg[u] > 0`) with `quick_link[u][c]` on $S[-Q..2Q]$.
   - **Complexity**: Strictly **$O(1)$ worst-case time per operation** (`push_front`, `push_back`, `pop_front`, `pop_back`) and $O(Q|\Sigma|)$ space.
5. **Canonical Failure Modes & Counterexamples**:
   - **Full-Window Palindrome Crossover (`len(u) == R - L + 1`)**: When adding/removing $u$ with $\text{len}(u) = R - L + 1$, both `last_pref` and `last_suff` must be updated simultaneously.
   - **Physically Freeing Node `u` on Pop**: Another index $j \in [L, R]$ may still store `max_pref[j] == u` or `max_suff[j] == u`; physically unlinking `u` from `ch[p][c]` creates dangling pointers.
6. **Canonical Representative Problems**:
   - `W3A-18` (2-Way Push-Only Deque PAM), `W3A-35` (Full 4-Way Deque PAM with Pop & Distinct/Total Counts), `W3A-36` (Sliding-Window Palindrome Queries).

---

### `T-3A-03`. Online Range Longest Palindromic Substring ($S[l..r]$ LPS) & Midpoint-Decoupled Multiplicity
1. **Multilingual Name**:
   - `[EN]`: Online Range Longest Palindromic Substring (`Range LPS` in $O(\log N)$ or $O(1)$) & Midpoint-Decoupled Range Palindrome Counting
   - `[ZH]`: 在线区间最长回文子串（单二分 RMQ、`slink` 整除截断与 $O(1)$ 双边界去截断）及奇偶中心解耦计数
   - `[JA]`: オンライン区間最長回文部分文字列 (`Range LPS`) と中心分離区間回文数え上げ
2. **Diagnostic Signal**:
   - $Q$ online queries $(l, r)$ asking for the maximum length of a palindrome inside $S[l..r]$ (`Range LPS`) or the total number of palindromic occurrences inside $S[l..r]$.
3. **Core Combinatorial Word Invariant**:
   - **Regime A (Single Binary Search + RMQ)**: A length $\ge k$ palindrome fits in $S[l..r]$ iff $\max_{c \in [2(l+\lceil k/2\rceil-1), \, 2(r-\lceil k/2\rceil+1)]} \text{rad}[c] \ge k$. Since `F(k) = max(...) - k` decreases by at most $3$ when $k \to k+1$ (`-1` from $-k$ and at most `-2` from boundary shrinking), a single binary search on $k$ works without splitting odd/even parities!
   - **Regime B (`slink` Ceiling Division)**: Walking `slink` from `pos_suff[r]`, the longest palindrome in chain $u$ with period $d = \text{diff}(u)$ fitting inside $L = r - l + 1$ has length $\text{len}(u) - \left\lceil \frac{\text{len}(u) - L}{d} \right\rceil \cdot d$.
   - **Regime C (True $O(1)$ Online Range LPS via Two-Boundary Unclipping — `Theorem 3.2`)**: Let $c_L \ge 2l-1$ be the leftmost Manacher center whose palindrome touches $l$ ($c_L - \text{rad}[c_L] + 1 \le 2l-1$, found in $O(1)$ via precomputed `rightmost_reach[2l-1]`), and let $c_R \le 2r-1$ be the rightmost center whose palindrome touches $r$ ($c_R + \text{rad}[c_R] - 1 \ge 2r-1$). For **every** center $c \in (c_L, c_R)$, its maximal palindrome in $S$ touches **neither $l$ nor $r$**, so its clipped radius inside $S[l..r]$ is **unclipped** ($\text{rad}[c]$)! Thus:
     $$\text{LPS}(l, r) = \max\Bigl( \min\bigl(\text{rad}[c_L], \text{dist}(c_L, r)\bigr), \; \min\bigl(\text{rad}[c_R], \text{dist}(l, c_R)\bigr), \; \max_{c \in (c_L, c_R)} \text{rad}[c] \Bigr),$$
     which reduces to **one $O(1)$ Sparse-Table RMQ**!
   - **Midpoint Decoupling for Range Palindrome Multiplicity (`Section 3.3`)**: Split centers at $m_{\text{odd}} = \lfloor (l+r)/2 \rfloor$ and $m_{\text{even}} = \lfloor (l+r-1)/2 \rfloor$ so left halves only clip against $l$ ($\min(R[i], i - l + 1)$) and right halves only clip against $r$ ($\min(R[i], r - i + 1)$), answered in $O(\log N)$ via Chairman Tree.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Regime C (`Two-Boundary Unclipping` + `<O(N), O(1)>` RMQ): **$O(N)$ preprocessing and $O(1)$ worst-case time per query**!
5. **Canonical Failure Modes & Counterexamples**:
   - Using a single midpoint $m = \lfloor (l+r)/2 \rfloor$ for both odd and even palindromes misclassifies even center $m$ when $r - l + 1$ is odd ($m - l + 1 > r - m$, so $m$ is right-constrained, not left-constrained!).
6. **Canonical Representative Problems**:
   - `W3A-11` (Online Range Palindrome Multiplicity), `W3A-21` ($O(\log N)$ / $O(1)$ Online Range LPS), `W3A-38` (`[BZOJ/LOJ]` Range Palindrome Sum Queries).

---

### `T-3A-04`. Range Distinct Palindromes via `slink` Periodic Telescoping (`[徐毅 2014]` / `LOJ 6071`)
1. **Multilingual Name**:
   - `[EN]`: Range Distinct Palindromes in $S[l..r]$ via `slink` Periodic Suffix Telescoping & LCT `access`
   - `[ZH]`: 区间本质不同回文子串（`[徐毅 2014]` PAM `slink` 等差数列错位相消 + 树状数组 / LCT）
   - `[JA]`: 区間相異なる回文部分文字列クエリ (`slink` 周期相殺 + Fenwick Tree)
2. **Diagnostic Signal**:
   - $Q$ queries $(l, r)$ asking for the number of **distinct** palindromic substrings (or weighted sum of distinct palindromes) inside $S[l..r]$ ($N, Q \le 3 \cdot 10^5$).
3. **Core Combinatorial Word Invariant**:
   - **Periodic Suffix Telescoping Cancellation (`Theorem 3.3`)**: When sweeping right endpoint $r$ and walking a `slink` chain $C = \{u_1, u_2, \dots, u_k\}$ ($\text{diff} = d$) on the PAM fail tree, every node $u_j$ ($j \ge 2$) is a proper suffix AND prefix of $u_1$ of length $\text{len}(u_1) - (j-1)d$, so $u_j$ occurred at $r - (j-1)d$ with rightmost end-position $\text{last}_{r-1}(u_j) = r - (j-1)d$. Thus its old start position $\text{start}_{r-1}(u_j) = (r - (j-1)d) - (\text{len}(u_1) - (j-1)d) + 1 = r - \text{len}(u_1) + 1$ **equals the new start position $\text{start}_r(u_{j-1})$ of $u_{j-1}$**!
   - All $k - 1$ intermediate start positions telescope and cancel identically, leaving **only two point updates per `slink` chain**:
     1. `-1` at $\text{prev\_r}(u_1) - \text{len}(u_1) + 1$ (if $\text{prev\_r}(u_1) > 0$), and
     2. `+1` at $\text{start}_r(u_k) = r - \text{len}(\text{slink}[u_1]) - \text{diff}[u_1] + 1$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Maintain $\text{prev\_r}(u) = \max_{\text{sub}(u)} \text{last\_end}$ via a segment tree over the Euler tour of the PAM fail tree; perform $\le 2 \log_2 r$ point updates in a Fenwick tree at step $r$ (or use persistent Segment Tree for online queries).
   - **Complexity**: $O(N \log^2 N + Q \log N)$ time and $O(N)$ space (offline) or $O(N \log^2 N)$ space (online persistent).
5. **Canonical Failure Modes & Counterexamples**:
   - Storing `last_end[u]` only on the node $u$ reached at step $r$ instead of querying the **fail-subtree maximum** misses longer palindromes in $\text{sub}(u)$ that updated $u$'s rightmost occurrence without visiting $u$ directly.
6. **Canonical Representative Problems**:
   - `W3A-31` (`LOJ #6071` / `[徐毅 2014]` Range Distinct Palindromes), `W3A-32` (Weighted Range Distinct Palindromes via LCT `access`).

---

### `T-3A-05`. Rich Words, Greedy Even-Palindrome Factorization, Online 2-Palindromes & $\theta$-Palindromes
1. **Multilingual Name**:
   - `[EN]`: Droubay–Pirillo Rich Words, Greedy Even-Palindrome Factorization, Online 2-Palindromes & $\theta$-Palindromes
   - `[ZH]`: 富回文串 (`Rich Words`)、最短偶回文贪心分解 (`CF 1827C`)、在线双回文串判定与反对称 $\theta$-回文串
   - `[JA]`: Rich Words (充満回文語)・最短偶回文貪欲分解・二連回文判定と $\theta$-回文 (`Antisymmetry`)
2. **Diagnostic Signal**:
   - Testing if every substring in $S[l..r]$ is rich ($|\text{Pal}(W)| = |W|+1$), counting/factoring strings into even-length palindromes (`CF 1827C`), recognizing concatenations of 2 palindromes $P_1 P_2$ (`UVa 11888`), or matching Watson–Crick / bitwise-complement palindromes (`POI XVII Antisymmetry`).
3. **Core Combinatorial Word Invariant**:
   - **Droubay–Pirillo Bound & Glen–Justin–Widmer–Zamboni Rich Characterization (`Theorem 4.1–4.2`)**: Every word $S$ has $|\text{Pal}(S)| \le |S|+1$. $S$ is **rich** ($|\text{Pal}(S)| = |S|+1$) iff every factor of $S$ is rich, iff every longest palindromic suffix at $i = 1..N$ is unioccurrent in $S[1..i]$, yielding a monotonic two-pointer boundary $L_{\text{rich}}[r]$ so $S[l..r]$ is rich iff $l \ge L_{\text{rich}}[r]$ ($O(1)$ per query!).
   - **Shortest Even-Palindrome Overlap Lemma (`Theorem 4.3` — `CF 1827C`)**: Any even-length palindrome $P$ has a shortest even-length palindromic suffix $E$; stripping $E$ from both ends of any longer even palindrome $P'$ starting at the same index leaves an even palindrome, so partitioning into **minimal** even palindromes is canonical ($dp[i] = 1 + dp[i - \text{min\_even}[i]]$).
   - **Online 2-Palindrome Top-2 `slink` Sufficiency (`Theorem 4.4`)**: When $u = \text{last}[i]$ has period $d = \text{diff}(u)$ and $\text{len}(u) \ge 2d$, stripping $u$ (`len(u)`) or $u' = \text{fail}(u)$ (`len(u)-d`) removes a palindrome while preserving prefix periodicity $d$ on $S[1..i]$, so checking **only the top 2 nodes** $u$ and $\text{fail}(u)$ per `slink` chain suffices!
   - **$\theta$-Palindrome Parity Dichotomy**: For an antimorphic involution $\theta(a) \ne a$ (e.g., $\theta(0)=1, \theta(1)=0$), every non-empty $\theta$-palindrome ($w = \theta(w)^R$) has **strictly even length** (since a midpoint character $c$ would require $c = \theta(c)$, impossible!).
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Rich range queries: $O(N)$ two-pointer Queue-PAM preprocessing + $O(1)$ per query.
   - `CF 1827C` shortest even palindrome: $O(N)$ Manacher + monotonic stack/DSU next-uncovered jump.
   - Online 2-Palindrome: $O(\log N)$ per prefix via PAM `slink`.
5. **Canonical Failure Modes & Counterexamples**:
   - **Broken Longest-Palindrome Greedy for 2-Palindromes**: On $S = \texttt{"bababcba"}$ ($N=8$), the longest palindromic prefix is `"babab"` (leaving non-palindrome `"cba"`) and the longest palindromic suffix is `"abcba"` (leaving non-palindrome `"bab"`), yet $S = \texttt{"bab"} + \texttt{"abcba"}$ is a valid 2-palindrome!
6. **Canonical Representative Problems**:
   - `W3A-03` (`CF 1827C — Palindrome Partition`), `W3A-05` (`POI XVII — Antisymmetry`), `W3A-19` (Online 2-Palindrome Prefix Recognition), `W3A-26` ($O(1)$ Range Rich Substring Queries).

---

### `T-3A-06`. Inverse String Reconstruction from KMP, Z-Array & Manacher Radii
1. **Multilingual Name**:
   - `[EN]`: Inverse String Reconstruction & Validity Verification from KMP $\pi$, Z-Array, and Manacher Radii
   - `[ZH]`: 逆向字符串构造（由 KMP $\pi$、Z 数组、Manacher 半径还原原串与弦图色多项式计数）
   - `[JA]`: KMP・Z配列・Manacher 半径からの文字列逆構築と正当性検証
2. **Diagnostic Signal**:
   - Given an integer array claiming to be $\pi[1..N]$, $Z[1..N]$, or Manacher radii $R[1..2N-1]$, construct the lexicographically smallest valid string $S$, check realizability over $|\Sigma| = \sigma$, or count all valid strings $S \in \Sigma^N$.
3. **Core Combinatorial Word Invariant**:
   - **Equality + Forbidden-Character Dual Decomposition**:
     - *KMP $\pi[i]$*: If $\pi[i] > 0$, then $S[i] = S[\pi[i]]$; and for every ancestor $q$ on the failure chain of $\pi[i-1]$ that was rejected ($q + 1 > \pi[i]$), $S[i] \ne S[q + 1]$ (plus $S[i] \ne S[1]$ if $\pi[i] = 0$). By KMP potential amortization, at most $2N$ total mismatch edges are generated across $i = 1..N$!
     - *Chordal Chromatic Product*: For a valid KMP/Z/Manacher array, every index $i$ with $\pi[i] = 0$ (or first appearance of its DSU component) only has mismatch edges to strictly earlier components $j < i$. Since the distinct forbidden characters at $i$ already exist in $S[1..i-1]$, the number of valid strings over $|\Sigma| = \sigma$ is the exact chromatic polynomial product $\prod_{v} \max\bigl(0, \sigma - \text{deg}_{\text{distinct-prev}}(v)\bigr)$!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Construct $S$ left-to-right in $O(N)$ time, then **run the forward KMP / Z / Manacher algorithm on $S$ in $O(N)$ time** to verify exact entry-by-entry equality.
5. **Canonical Failure Modes & Counterexamples**:
   - **Why Local Conditions Are Insufficient Without Forward Verification**: Consider $\pi = [0, 1, 0, 1, 1]$ ($N = 5$). It satisfies $\pi[1]=0$ and $\pi[i] \le \pi[i-1]+1$ everywhere. However, $\pi[2]=1 \implies S[2]=S[1]=\texttt{'a'}$; $\pi[3]=0 \implies S[3]=\texttt{'b'}$ ($S[1..3]=\texttt{"aab"}$); $\pi[4]=1 \implies S[4]=S[1]=\texttt{'a'}$; and $\pi[5]=1 \implies S[5]=S[1]=\texttt{'a'}$, forcing $S = \texttt{"aabaa"}$ whose actual $\pi[5] = 2 \ne 1$! Forward verification catches this in $O(N)$ time.
6. **Canonical Representative Problems**:
   - `W3A-08` (Inverse KMP String Reconstruction & Counting), `W3A-14` (Inverse Z-Array & Manacher Radius Verification), `W5A-08` (`[SDOI2017]` / `BZOJ 4974` Period Array Reconstruction).

---

## Wave 3B: FFT/NTT String Matching, $k$-Mismatch, Isomorphism Matching & Locally Consistent Parsing (SLPs)

### `T-3B-01`. Polynomial & Wildcard String Matching (1-NTT Indicator, Kalai's Randomized NTT & 3-in-2 FFT)
1. **Multilingual Name**:
   - `[EN]`: Wildcard String Matching via Degree-Reduced Indicator Polynomials, Kalai's Randomized $\mathbb{F}_p$ Projection & 3-in-2 Complex FFT
   - `[ZH]`: 通配符卷积匹配（降次指示多项式单模 NTT、Kalai 随机投影与复数 FFT 三次变两次优化）
   - `[JA]`: ワイルドカード文字列検索（多項式畳み込み・Kalai の乱択 NTT・複素 FFT 回数削減）
2. **Diagnostic Signal**:
   - Pattern matching with wildcards `'?'` ($N, M \le 5 \cdot 10^5$), cyclic shifts with mismatches, or bitset/convolution-based string alignment.
3. **Core Combinatorial Word Invariant**:
   - **Index-Reflection Duality (`Theorem 1.1`)**: Reversing the pattern $P^R[k] = P[M-1-k]$ turns alignment offset $T[i+j]$ vs. $P[j]$ into a Cauchy convolution sum $k + t = i + M - 1$ at index $i + M - 1$.
   - **Clifford–Clifford Cubic Penalty (`Theorem 1.2`)**: $D(i) = \sum_{j=0}^{M-1} p_j t_{i+j} (p_j - t_{i+j})^2 = \sum p_j^3 t_{i+j} - 2 \sum p_j^2 t_{i+j}^2 + \sum p_j t_{i+j}^3 = 0 \iff P \text{ matches } T[i..i+M-1]$ (3 convolutions).
   - **Degree-Reduced Indicator Penalty (`Equation 1.5`)**: Encode Wildcard as `(u=0, v=0)` and character $c \in \{1..|\Sigma|-1\}$ as `(u=1, v=c)`. Then $D_{\text{ind}}(i) = \sum_{j=0}^{M-1} u_{P[j]} u_{T[i+j]} (v_{P[j]} - v_{T[i+j]})^2$ has maximum value $M(|\Sigma|-1)^2 \le 5\cdot 10^5 \times 25^2 = 3.125 \times 10^8 < 998244353$, so **zero false positives occur in a single NTT prime**!
   - **Kalai's Randomized Projection (2002)**: Draw $r_j \in \mathbb{F}_p$ uniformly at random; if only $T$ has wildcards, $\sum_{j=0}^{M-1} [T_{i+j} \ne \texttt{'?'}] r_j (T_{i+j} - P_j) = \sum (r_j P_j)[T_{i+j}\ne\texttt{'?'}] - \sum r_j (T_{i+j}[T_{i+j}\ne\texttt{'?'}])$ requires **only 1 NTT** (and 2 NTTs for two-sided wildcards) with collision probability $\le 1/p$.
   - **3-in-2 Complex FFT Packing (`三次变两次`)**: Pack real arrays $(A_1, A_2)$ into $Z_A = A_1 + i A_2$ and $(B_1, B_2)$ into $Z_B = B_1 + i B_2$ to extract $\widehat{A_k}[u]$ from $\frac{1}{2}(\widehat{Z_A}[u] + \overline{\widehat{Z_A}[L-u]})$ and accumulate all 3 products in frequency space before a **single IFFT** (5 real FFT passes total instead of 9!).
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - $O(N \log N)$ time and $O(N)$ space.
5. **Canonical Failure Modes & Counterexamples**:
   - **Cubic Overflow Modulo $998244353$**: Using raw ASCII values $c \in [97, 122]$ in $p_j t_{i+j} (p_j - t_{i+j})^2$ reaches $5 \cdot 10^5 \times 26^4 \approx 2.28 \times 10^{11} > 998244353$, permitting modular wrap-around false positives! Always use the degree-reduced indicator encoding `(u=1, v=c)` (`<= 3.125e8 < 998244353`).
6. **Canonical Representative Problems**:
   - `W3B-01` (`CF 528D — Fuzzy Search`), `W3B-03` (`[BZOJ 4503] 两个串`), `W3B-12` (`[ZJOI2013] 力` / Wildcard Distances).

---

### `T-3B-02`. Permutation/Involution Matching (`CF 1334G`), Affine Matching & $\sqrt{M \log M}$ Bucket Splitting
1. **Multilingual Name**:
   - `[EN]`: Permutation/Involution Quartic Matching (`CF 1334G`), Cauchy–Schwarz Affine Matching & $\sqrt{M\log M}$ Bucket Splitting
   - `[ZH]`: 置换/对合四次多项式匹配 (`CF 1334G`)、柯西不等式仿射匹配与值域分块 $\sqrt{M\log M}$ 卷积
   - `[JA]`: 置換・対合マッチング (`CF 1334G`)、アフィン変換一致判定と平方分割 FFT
2. **Diagnostic Signal**:
   - Matching when each position $j$ allows 2 valid characters $\{P_j, \pi(P_j)\}$ (`CF 1334G`), testing affine equality $T_{i+j} = \alpha P_j + \beta$ ($\alpha > 0$), or dominance/distance matching ($\forall j, P_j \le T_{i+j}$ or $\sum |P_j - T_{i+j}|$).
3. **Core Combinatorial Word Invariant**:
   - **`CF 1334G` 4-Method Hierarchy**:
     1. *When $\pi^2 = \text{id}$ (Involution)*: Each cycle $\{a, \pi(a)\}$ is an unordered pair, so replacing every letter $c$ by $\min(c, \pi(c))$ reduces the problem to **$O(N + M)$ deterministic KMP**!
     2. *General $\pi$ via Quartic Penalty (3 NTTs)*: $\sum_{j=0}^{M-1} (T_{i+j} - P_j)^2 (T_{i+j} - \pi(P_j))^2$ expands into degree-$k$ powers of $T$ ($k \in \{0..4\}$), requiring only 3 NTTs for $k = 1, 2, 3$.
     3. *General $\pi$ via 1 Complex FFT*: Place letters on $e^{i\theta_c}$; then $\text{Re}\bigl(e^{i(\theta_{T_{i+j}} - \frac{\theta_{P_j}+\theta_{\pi(P_j)}}{2})}\bigr) \le \cos\bigl(\frac{\theta_{P_j}-\theta_{\pi(P_j)}}{2}\bigr)$ with equality iff $T_{i+j} \in \{P_j, \pi(P_j)\}$!
     4. *General $\pi$ via 2-NTT Kalai*: $\sum r_j (T_{i+j}-P_j)(T_{i+j}-\pi(P_j)) = \sum r_j T_{i+j}^2 - \sum r_j(P_j+\pi(P_j))T_{i+j} + \sum r_j P_j \pi(P_j)$.
   - **Affine Scale-and-Shift Matching**: Take first differences $\Delta P_j = P_{j+1}-P_j$ to eliminate $\beta$, then apply Cauchy–Schwarz $\bigl(\sum \Delta P_j \Delta T_{i+j}\bigr)^2 = \bigl(\sum \Delta P_j^2\bigr)\bigl(\sum \Delta T_{i+j}^2\bigr)$ (1 FFT!).
   - **$\sqrt{M \log M}$ Value-Bucket Splitting**: Partition sorted values into $B$ buckets; inter-bucket pairs have known order/sign (counted via 1 FFT per bucket), while intra-bucket pairs are brute-forced in $O((N+M)^2/B)$, balanced at $B = \sqrt{M / \log M}$ for $O(N\sqrt{M \log M})$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Involution $\pi^2 = \text{id}$: $O(N+M)$; General $\pi$ or Affine: $O(N \log N)$; Less-Than / $L_1$ Distance: $O(N\sqrt{M \log M})$.
5. **Canonical Failure Modes & Counterexamples**:
   - In Affine Matching, Cauchy–Schwarz holds for **both** $\alpha > 0$ and $\alpha < 0$; when $\alpha > 0$ is required, verify $\sum \Delta P_j \Delta T_{i+j} > 0$.
6. **Canonical Representative Problems**:
   - `W3B-04` (`CF 1334G — Substring Search`), `W3B-18` (Affine Scale-and-Shift Pattern Matching), `W3B-24` (Dominance & $L_1$ Distance String Matching).

---

### `T-3B-03`. $k$-Mismatch & $k$-Edit String Matching (Kangaroo Jumps, Diagonal Wavefronts & $2k$-Period Dichotomy)
1. **Multilingual Name**:
   - `[EN]`: $k$-Mismatch & $k$-Edit String Matching (Landau–Vishkin Kangaroo Jumps, Abrahamson $\sqrt{M\log M}$, and Clifford et al. $O(N\sqrt{k\log k})$ $2k$-Period Dichotomy)
   - `[ZH]`: $k$-失配与 $k$-编辑距离匹配（袋鼠跳 LCE、对角线波前 DP、高频字符分治与 $2k$-周期二分法）
   - `[JA]`: $k$-ミスマッチ・$k$-編集距離文字列検索（Kangaroo Jump LCE・対角波面 DP・周期性二分法）
2. **Diagnostic Signal**:
   - Finding all occurrences of $P[0..M-1]$ in $T[0..N-1]$ with $\le k$ Hamming mismatches or $\le k$ Levenshtein edits.
3. **Core Combinatorial Word Invariant**:
   - **Landau–Vishkin Kangaroo Jumps (`Theorem 2.1`)**: $k$ mismatches partition $P$ into $\le k+1$ exact-match runs, each skipped in $O(1)$ via $\text{LCE}_{P\#T}(j, M + 1 + i + j)$, giving $O(Nk)$ for $k$-mismatch and $O(N + k^2)$ via diagonal wavefront $d = x - y \in [-k, k]$ for $k$-edit distance.
   - **Abrahamson's Heavy–Light Alphabet Split (`Theorem 2.2`)**: Characters occurring $\ge B$ times in $P$ number $\le M/B$ (each handled by 1 FFT); light characters have $\le MB$ total $(j, t)$ pairs, giving $O(N\sqrt{M\log M})$ at $B = \sqrt{M \log M}$.
   - **Clifford–Gawrychowski–Uznański $2k$-Period Dichotomy (`Theorem 2.3`, SODA 2016)**:
     - *Case A ($\text{per}(P) > 2k$, Aperiodic)*: There exists a set of $\le 2k$ **mismatching witness pairs** in $P$. Only $O(N/k)$ candidate alignments $i$ survive a filter, each verified in $O(k)$ LCE jumps $\implies O(N)$ total time!
     - *Case B ($\text{per}(P) = p \le 2k$, Near-Periodic)*: Both $P$ and any relevant window of $T$ break into $O(k)$ periodic RLE runs modulo $p$. Taking the **second-order periodic difference** $\text{diff}_p(S)[x] := \mathbf{1}[S[x] \ne S[x-p]]$ reduces the convolution support to $O(k)$ nonzero transitions, solved in $O(N\sqrt{k\log k})$!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - $O(Nk)$ ($k$ tiny), $O(N\sqrt{M\log M})$ (Abrahamson), $O(N\sqrt{k\log k})$ (Clifford et al.), $O(N + k^2)$ ($k$-edit wavefront).
5. **Canonical Failure Modes & Counterexamples**:
   - Allowing the kangaroo cursor $j$ to jump past $M$ when $P$ shares a prefix with $T[i+M..]$: always clamp $j \leftarrow j + \min(\text{LCE}, M - j)$.
6. **Canonical Representative Problems**:
   - `W3B-08` (`[BZOJ 4259] 残缺的字符串`), `W3B-15` ($k$-Mismatch Pattern Matching), `W3B-27` (Landau–Vishkin $k$-Edit Wavefront Alignment).

---

### `T-3B-04`. Structural Isomorphism Matching (`p-KMP`, `Order-KMP`, `Cartesian-KMP`, `p-SA` & Abelian Parikh Envelopes)
1. **Multilingual Name**:
   - `[EN]`: Window-Clipped Structural KMP (`p-KMP`, `Order-KMP`, `Cartesian-KMP`), Parameterized SA (`p-SA`) & Abelian Parikh Envelopes
   - `[ZH]`: 结构同构匹配（窗口截断参数化 KMP、保序 KMP、笛卡尔树 KMP、参数化后缀数组 `p-SA` 与阿贝尔 Parikh 包络）
   - `[JA]`: 構造同型文字列検索（パラメータ化 KMP・順序同型 KMP・Cartesian-Tree KMP・Abelian マッチング）
2. **Diagnostic Signal**:
   - Matching $T[i..i+M-1] \cong P[0..M-1]$ under bijective character renaming (Parameterized), relative order (Order-Preserving), min-heap Cartesian tree shape, or multiset permutation (Abelian/Jumbled).
3. **Core Combinatorial Word Invariant**:
   - **Unified Window-Clipped Canonical Encoding (`Theorem 3.1`)**: Because shifting a window $[i, i+q]$ deletes links pointing left of $i$, a relative offset $\text{prev}(x) = x - \text{last}[S[x]]$ must be **window-clipped** against the current matched prefix length $q$:
     $$\text{clip}(\text{prev}_S[x], q) := \bigl(\text{prev}_S[x] \le q \;\text{?}\; \text{prev}_S[x] : 0\bigr).$$
     This single clipped equality $\text{clip}(\text{prev}_T[i], q) = \text{prev}_P[q]$ powers $O(N+M)$ Parameterized KMP (`p-KMP`) and $O(N+M)$ Cartesian-Tree KMP (`PD_S[x] = x - max{k < x : S[k] <= S[x]}`)!
   - **Order-Preserving `LMax`/`LMin` Sufficiency**: In a window $W[0..q-1]$ whose first $q$ elements match the relative order of $P[0..q-1]$, $W[q]$ fits the relative order of $P[q]$ **iff** $W[q - \text{LMax}_P[q]] \le W[q] \le W[q - \text{LMin}_P[q]]$ (with strictness matching equality in $P$), reducing an $O(q)$-element order check to **$O(1)$ comparisons**!
   - **Baker's Single-Position Mutation Invariant for `p-SA` (`Theorem 3.2`)**: Passing from $\text{prev}(S[i..N])$ to $\text{prev}(S[i+1..N])$ shifts all offsets by $1$ and resets **at most one entry** (at $\text{next}_S[i] - i$) to $0$, enabling $O(1)$ dynamic LCE and $O(N \log N)$ Parameterized Suffix Sorting!
   - **Binary Abelian Parikh Continuity (`Christou et al. 2013`)**: For binary $S \in \{0, 1\}^N$, let $m_\ell = \min_i |S[i..i+\ell-1]|_1$ and $M_\ell = \max_i |S[i..i+\ell-1]|_1$. Because sliding a window by $1$ changes $|W|_1$ by $\in \{-1, 0, +1\}$, by discrete intermediate value theorem **every integer $c \in [m_\ell, M_\ell]$ is realized** by some length-$\ell$ substring!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - `p-KMP` & `Cartesian-KMP`: $O(N+M)$ time; `Order-KMP`: $O(N \log M + M)$ time; `p-SA`: $O(N \log N)$ time; Binary Abelian queries: $O(1)$ after $O(N^2/\text{RLE})$ or $O(N)$ envelope precomputation.
5. **Canonical Failure Modes & Counterexamples**:
   - Comparing unclipped `prev_T[i]` against `prev_P[q]` fails whenever $T[i]$ appeared earlier inside $T[0..i-q-1]$ outside the active pattern window!
6. **Canonical Representative Problems**:
   - `W3B-06` (Parameterized KMP & `p-SA`), `W3B-09` (Order-Preserving KMP via `LMax`/`LMin`), `W3B-31` (Cartesian-Tree Matching), `W3B-34` (Binary Abelian Parikh Envelope Queries).

---

### `T-3B-05`. Locally Consistent Parsing (`局部一致性剖析`), Cole–Vishkin / Jeż Recompression & Grammar-Compressed Strings (SLPs)
1. **Multilingual Name**:
   - `[EN]`: Locally Consistent Parsing (`LCParsing`), Cole–Vishkin Deterministic $6$-Coloring, Jeż's Recompression & Dynamic Straight-Line Programs (`SLPs`)
   - `[ZH]`: 局部一致性剖析、Cole–Vishkin 确定性 6 染色、Jeż 重压缩文法 (`Recompression`) 与动态块压缩文法树 (`SLP`)
   - `[JA]`: 局所一意分割 (`Locally Consistent Parsing` / Block Compression)・Jeż の Recompression と動的文法圧縮 (`SLP`)
2. **Diagnostic Signal**:
   - Dynamic string cut/paste/reverse/duplicate operations generating exponentially long strings ($|S| \le 10^{18}$) while answering LCE queries, lexicographical comparisons, pattern matching $P$ in $\mathcal{G}$, or counting palindromes/runs/Lyndon roots on an SLP of $g \le 10^5$ rules.
3. **Core Combinatorial Word Invariant**:
   - **Three-Engine Alternating Contraction (`Section 4.1`)**:
     - *Phase A (RLE Block Compression `RComp`)*: Compress maximal runs $c^\ell \to (c, \ell)$, leaving a run-reduced string $S'$ where $S'[i] \ne S'[i+1]$ everywhere.
     - *Phase B (Aperiodic Local Cut Selection)*: Because $S'[i] \ne S'[i+1]$, either (1) **Cole–Vishkin 1-Round Bit-Diff Coloring** $\text{col}(c) = 2p + \text{bit}_p(c)$ ($p = \text{ctz}(x \oplus y)$) reduces $|\Sigma| \to 6$ in 3 rounds so local maxima cut every $3$ positions, or (2) **Randomized 64-Bit Hash Local Extrema** cuts with probability $1/3$, or (3) **Jeż's Recompression** partitions $\Sigma = \Sigma_L \sqcup \Sigma_R$ capturing $\ge 1/2$ of transitions in $\Sigma_L \times \Sigma_R$, shrinking length by $\le 5/6$ per level $\implies O(\log N)$ height!
   - **Bounded Destroyed Context under Dynamic Split/Concat**: Changing $O(1)$ characters at a cut/join boundary invalidates local parsing decisions in a radius of **$O(1)$ blocks per level** ($\le 4$ symbols), so rebuilding $O(\log N)$ levels allocates only $O(\log N)$ new grammar nodes!
   - **Boundary-Seam Non-Proliferation on SLPs (`Theorem 4.2`)**: Every occurrence of pattern $P$ (or maximal palindrome center, or run $R = [l, r, p]$) in $X = L \cdot R$ has a unique **primary grammar node** $X$ where it first straddles the seam $|L|$. By the Weak Periodicity Lemma, occurrences of $P$ straddling $|L|$ inside $\text{suff}_{|P|-1}(L) \cdot \text{pref}_{|P|-1}(R)$ form $O(\log |P|)$ arithmetic progressions!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Dynamic Split/Concat/Reverse + LCE: $O(\log N)$ per operation (with RLE Early-Termination when $(c, \ell_1)$ and $(c, \ell_2)$ have $\ell_1 \ne \ell_2$: add $\min(\ell_1, \ell_2)$ and stop!).
   - Pattern matching $P$ in SLP of $g$ rules: $O(g |P| + |P|)$ (naive seam KMP), $O(g \log |P| + |P|)$ (Border-AP seam matching), or $O((g + |P|) \log |P|)$ (Jeż's synchronized recompression).
   - Rytter's LZ77-to-SLP conversion: $O(z \log(N/z))$ rules via AVL-balanced grammar concatenation.
5. **Canonical Failure Modes & Counterexamples**:
   - **Continuing Tree Traversal Past Partial RLE Match**: If $(c, \ell_1)$ meets $(c, \ell_2)$ with $\ell_1 < \ell_2$, the next character after the shorter run is guaranteed $\ne c$ (by maximal RLE invariance), while the longer run continues with $c$, so a mismatch occurs immediately at offset $\min(\ell_1, \ell_2)$—never recurse further!
6. **Canonical Representative Problems**:
   - `W3B-29` (Dynamic String Split/Concat/Reverse + LCE via Locally Consistent Parsing), `W3B-35` (Pattern Matching & Palindrome Counting on Huge SLPs), `W3B-40` (Significant Suffixes & Runs on SLPs).

---

## Wave 4A: Goulden–Jackson Cluster Method, String PGFs, Conway's Casino & Automaton DP (`DP套DP`)

### `T-4A-01`. Goulden–Jackson Cluster Method & Guibas–Odlyzko End-Tagged Autocorrelation System
1. **Multilingual Name**:
   - `[EN]`: Goulden–Jackson Cluster Method & Guibas–Odlyzko End-Tagged Autocorrelation Linear System
   - `[ZH]`: Goulden–Jackson 簇方法与 Guibas–Odlyzko 尾标记自相关方程组 (`[CTSC2006] 歌唱王国`)
   - `[JA]`: Goulden–Jackson クラスター法と Guibas–Odlyzko 自己相関多項式連立方程式
2. **Diagnostic Signal**:
   - Counting words of length $n$ ($n \le 10^{18}$ or $n \le 10^5$) over $\Sigma$ avoiding a dictionary $\mathcal{P} = \{P_1, \dots, P_m\}$ where individual pattern lengths $|P_i|$ may be large ($|P_i| \le 10^5$) while $m$ is small ($m \le 300$), so the Aho–Corasick automaton has too many states for matrix exponentiation.
3. **Core Combinatorial Word Invariant**:
   - **Guibas–Odlyzko Autocorrelation Polynomial**: For $P_i, P_j$ in a reduced antichain $\mathcal{P}$, define
     $$C_{i, j}(x) := \sum_{k \in \text{Overlap}(P_i, P_j)} x^{|P_j| - k}, \quad \text{where } \text{Overlap}(P_i, P_j) = \bigl\{\, k \in [1, \min(|P_i|, |P_j|)] \;\big|\; \text{suff}_k(P_i) = \text{pref}_k(P_j) \,\bigr\}.$$
   - **End-Tagged Cluster & Avoidance System (`Theorem 1.1–1.2`)**: Let $F(x)$ be the OGF of $\mathcal{P}$-avoiding words and $F_i(x)$ be the OGF of words ending with a **first** occurrence of $P_i$. Double-counting unrestricted extensions $w \cdot P_j$ ($w \in \mathcal{A}(\mathcal{P})$) by the first pattern $P_i$ that completes inside $w P_j$ yields:
     $$(1 - \sigma x) F(x) + \sum_{i=1}^m F_i(x) = 1 \quad \text{and} \quad F(x) x^{|P_j|} = \sum_{i=1}^m F_i(x) C_{i, j}(x) \quad (1 \le j \le m).$$
     Dividing by $F(x)$ sets $C_i(x) = -F_i(x)/F(x)$, which solves $\sum_{i=1}^m C_i(x) C_{i, j}(x) = -x^{|P_j|}$ and gives $F(x) = \frac{1}{1 - \sigma x - \sum_{i=1}^m C_i(x)}$.
   - **Commutative Ring Invertibility & Rank-1 Sherman–Morrison Form**: In $\mathcal{R}[[x]]$, since $\mathcal{P}$ is an antichain, $C_{i,i}(0) = 1$ and $C_{i,j}(0) = 0$ ($i \ne j$), so $\mathbf{C}(0) = I_m$ and $\det \mathbf{C}(x) \in 1 + x\mathcal{R}[[x]] \subseteq \mathcal{R}[[x]]^\times$ is **always invertible over any commutative ring $\mathcal{R}$ without field division**! By Sherman–Morrison, $F(x) = \frac{\det \mathbf{C}(x)}{\det\bigl((1-\sigma x)\mathbf{C}(x) + \mathbf{u}(x)\mathbf{1}^T\bigr)}$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Single pattern $P$: $F(x) = \frac{C_{P,P}(x)}{(1-\sigma x)C_{P,P}(x) + x^{|P|}}$, solved in $O(|P| + \text{len}\log\text{len})$ via polynomial inversion or $O(|P|\log |P| \log n)$ via Bostan–Mori.
   - $m$ patterns: $O(m^2 \sum |P_i| + m^3 d)$ via Gaussian elimination at evaluation points.
5. **Canonical Failure Modes & Counterexamples**:
   - **Failure to Reduce $\mathcal{P}$ to an Antichain**: If $P_1 = \texttt{"ab"}$ is a substring of $P_2 = \texttt{"cabd"}$, then $w \cdot P_2$ can trigger $P_1$ strictly before the overlap with $P_2$ even starts! Always discard superstrings before building $C_{i, j}(x)$ for avoidance.
6. **Canonical Representative Problems**:
   - `W4A-01` (Single-Pattern Avoidance OGF), `W4A-12` (Multi-Pattern Goulden–Jackson Cluster Avoidance), `W4A-25` (Bostan–Mori $n \le 10^{18}$ Pattern Avoidance).

---

### `T-4A-02`. Bivariate $(t-1)$ Weighted Goulden–Jackson, Exact $k$-Occurrence FPS & Embedded Substring Weight Absorption
1. **Multilingual Name**:
   - `[EN]`: Bivariate $(t-1)$ Weighted Cluster GFs, Exact $k$-Occurrence FPS (`ln`/`exp`) & Non-Antichain Weight Absorption
   - `[ZH]`: 二元 $(t-1)$ 加权 Goulden–Jackson、恰好出现 $k$ 次生成函数与内嵌子串权重吸收定理
   - `[JA]`: 二変数重み付き Goulden–Jackson 法・ちょうど $k$ 回出現する文字列の数え上げと部分文字列重み吸収
2. **Diagnostic Signal**:
   - Counting strings of length $n$ containing a pattern $P$ **at least $k$ times** or **exactly $k$ times** ($n, k \le 10^5$), or evaluating $\sum_{W \in \Sigma^n} \prod_{j=1}^m t_j^{\text{occ}_{P_j}(W)}$ when patterns $P_i \subset P_j$ are **not** an antichain.
3. **Core Combinatorial Word Invariant**:
   - **Exact $k$-Occurrence OGF (`Corollary 1.3`)**: Substituting $w = t - 1$ into the bivariate cluster OGF $F(x, t) = \frac{(1-t)C(x) + t}{(1-\sigma x)\bigl((1-t)C(x) + t\bigr) + (1-t)x^L}$ and extracting $[t^k]$ via $D_0(x) = (1-\sigma x)C(x) + x^L$ and $D_1(x) = (1-\sigma x)(C(x)-1) + x^L$ yields for all $k \ge 1$:
     $$[t^k]F(x, t) = \frac{x^L \, D_1(x)^{k-1}}{D_0(x)^{k+1}} \qquad \text{and} \qquad [t^0]F(x, t) = \frac{C(x)}{D_0(x)}.$$
   - **Non-Antichain Embedded Substring Weight Absorption (`Section 1.2.4`)**: When $P_a$ occurs $\text{emb}(P_a, P_j)$ times strictly inside $P_j$ (not as a suffix of $P_j$), we cannot discard $P_j$ in weighted counting ($t_j \ne 0$). Instead, keep only **suffix-reduced** patterns and absorb internal occurrences into modified cluster entry weights $\widetilde{W}_j = \bigl(\prod_{a : P_a \text{ suffix of } P_j} (t_a - 1)\bigr) \cdot \prod_{b} t_b^{\text{emb}(P_b, P_j)}$ and modified overlap transitions $\widetilde{C}_{i, j}(x, \mathbf{t})$!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Exact $k$ occurrences for $n \le 2 \cdot 10^5$: Compute $D_1(x)^{k-1} D_0(x)^{-(k+1)} \bmod x^{n-L+1}$ in $O(n \log n)$ time via FPS $\ln / \exp$.
5. **Canonical Failure Modes & Counterexamples**:
   - **Zero Constant Term in $D_1(x)$ Before FPS `ln`/`exp`**: Because $C(0) = 1$, we have $D_1(0) = (1-0)(1-1) + 0 = 0$! Calling FPS $\ln(D_1(x))$ directly divides by $0$. Always factor out the lowest nonzero degree $d = \min\text{Per}(P)$ ($D_1(x) = x^d c_d \widetilde{D}_1(x)$ with $\widetilde{D}_1(0) = 1$) before taking $\ln$ and $\exp$!
6. **Canonical Representative Problems**:
   - `W4A-08` (Strings with $\ge k$ or Exactly $k$ Pattern Occurrences via FPS), `W4A-28` (Non-Antichain Weighted Multi-Pattern Cluster Counting), `W4A-35` (Cyclic & Palindromic Goulden–Jackson).

---

### `T-4A-03`. The $t = 1 + u$ Binomial Moment Shift Trick (`Universal Cup / QOJ`)
1. **Multilingual Name**:
   - `[EN]`: The $t = 1 + u$ Binomial Moment Shift in Bivariate Goulden–Jackson Cluster GFs
   - `[ZH]`: 二元 Goulden–Jackson 的 $t = 1 + u$ 二项式矩换元法（将分母降维为 $(1-\sigma x)^{j+1}$）
   - `[JA]`: Goulden–Jackson 母関数における $t = 1 + u$ 二項モーメント変換
2. **Diagnostic Signal**:
   - Computing the $K$-th power moment $\sum_{W \in \Sigma^n} \text{occ}_P(W)^K$ (or $\mathbb{E}[\text{occ}_P(W)^K]$) for **huge $n \le 10^{18}$**, large pattern length $|P| \le 10^5$, and small $K \le 20$.
3. **Core Combinatorial Word Invariant**:
   - **Denominator Collapse under $t = 1 + u$ (`Section 1.2.5`)**: Extracting $[t^k]F(x, t)$ gives a denominator $D_0(x)^{k+1}$ of degree $(k+1)|P|$, which is impossible for Bostan–Mori when $|P| = 10^5$. Instead, substitute $t = 1 + u$ so $[u^j]F(x, 1+u) = \sum_{W \in \Sigma^*} \binom{\text{occ}_P(W)}{j} x^{|W|}$:
     $$F(x, 1+u) = \frac{1 + u(1 - C(x))}{(1 - \sigma x) + u\bigl((1-\sigma x)(1 - C(x)) - x^L\bigr)} = \sum_{j=0}^K u^j \frac{x^L \bigl(x^L - (1-\sigma x)(1 - C(x))\bigr)^{j-1}}{(1 - \sigma x)^{j+1}}!$$
   - Because the denominator is now purely $(1 - \sigma x)^{j+1}$, $[x^n][u^j]F(x, 1+u)$ is a simple convolution of $\binom{n - m + j}{j} \sigma^{n-m}$ against the polynomial numerator of degree $\le jL \le KL$, converting binomial moments to power moments via Stirling numbers of the second kind $\text{occ}^K = \sum_{j=0}^K \left\{ \begin{matrix} K \\ j \end{matrix} \right\} j! \binom{\text{occ}}{j}$!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Compute $\bigl(x^L - (1-\sigma x)(1-C(x))\bigr)^{j-1}$ for $j = 1..K$ in $O(KL \log(KL))$ time and extract $[x^n]$ in $O(KL)$ time — **completely independent of $n \le 10^{18}$**!
5. **Canonical Failure Modes & Counterexamples**:
   - Attempting to extract $[t^k]F(x, t)$ first and run Bostan–Mori on $D_0(x)^{k+1}$ when $L = 10^5$ and $n = 10^{18}$ TLEs ($O(KL \log(KL) \log n)$ vs. $O(KL \log(KL))$).
6. **Canonical Representative Problems**:
   - `W4A-39` (`Universal Cup / QOJ` — Expected $K$-th Power of Pattern Occurrences for $n \le 10^{18}$).

---

### `T-4A-04`. String PGFs, Conway's Casino Martingale & Pattern Races (`[SDOI2017] 硬币游戏`)
1. **Multilingual Name**:
   - `[EN]`: String Probability Generating Functions, Conway's Casino Martingale, Pattern Races & Renewal Waiting Times
   - `[ZH]`: 字符串概率生成函数 (PGF)、康威赌博鞅定理 (`[CTSC2006] 歌唱王国`) 与多模式串赛跑 (`[SDOI2017] 硬币游戏`)
   - `[JA]`: 文字列確率母関数 (`PGF`)・コンウェイのギャンブルマルチンゲールと文字列オッズ法 (`[SDOI2017]`)
2. **Diagnostic Signal**:
   - Expected waiting time $\mathbb{E}[T_S]$, variance $\text{Var}(T_S)$, $k$-th occurrence waiting time $\mathbb{E}[T_{S, k}]$, or winning probabilities $p_1, \dots, p_m$ in a random character stream until the first pattern in $\{P_1, \dots, P_m\}$ appears.
3. **Core Combinatorial Word Invariant**:
   - **Conway's Casino Fair-Betting Martingale & Odds Polynomial**: For pattern $P$ under i.i.d. letter probabilities $p_c > 0$ ($\mathbb{P}(w) = \prod_{r=1}^{|w|} p_{w[r]}$), a casino stream of $1$-dollar gamblers betting at reciprocal odds $1/p_c$ along $P$ has net terminal payoff at stopping time $T$:
     $$\Omega_{P_i, P_j} := \sum_{k \in \text{Overlap}(P_i, P_j)} \frac{1}{\mathbb{P}\bigl(P_j[1..k]\bigr)}.$$
   - **Optional Stopping Theorem Identities (`Theorem 2.1–2.2`)**:
     1. *Single-Pattern Mean & Variance*: $\mathbb{E}[T_S] = \Omega_{S, S} = \sum_{k \in \text{Border}(S)} \mathbb{P}(S[1..k])^{-1}$, and $\text{Var}(T_S) = \mathbb{E}[T_S]^2 - \sum_{k \in \text{Border}(S)} (2k - 1)\mathbb{P}(S[1..k])^{-1}$.
     2. *$k$-th Occurrence Renewal Waiting Time (`Corollary 2.3`)*: Moving from the $(r-1)$-th occurrence to the $r$-th starts from border state $\pi(|S|)$ rather than $0$, giving increment $\Omega_{S, S} - \sum_{b \in \text{Border}(S), b < |S|} \mathbb{P}(S[1..b])^{-1} = \mathbb{P}(S)^{-1}$, so $\mathbb{E}[T_{S, k}] = \mathbb{E}[T_{S, 1}] + \frac{k - 1}{\mathbb{P}(S)}$!
     3. *Division-Free Multi-Player Pattern Race System (`[SDOI2017]`) & Seed Prefix $S_0$*: To avoid division by $0$ when some $p_c = 0$, define $\Phi_{i, j} = \mathbb{P}(P_j)\Omega_{P_i, P_j} = \sum_{k \in \text{Overlap}(P_i, P_j)} \mathbb{P}(P_j[k+1..|P_j|])$. Then $(p_1, \dots, p_m, E)$ solves:
        $$\sum_{i=1}^m p_i \Phi_{i, j} = \mathbb{P}(P_j) \quad (1 \le j \le m) \qquad \text{and} \qquad \sum_{i=1}^m p_i = 1.$$
        If the game starts from an already-typed seed prefix $S_0$, the right-hand side shifts to $\mathbb{P}(P_j)\bigl(1 - \Omega_{S_0, P_j}\bigr)$!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Single pattern: $O(|S|)$ via KMP border walking.
   - $m$-pattern race: $O(m^2 L + m^3)$ via KMP/Z/AC overlap extraction + Gaussian elimination.
5. **Canonical Failure Modes & Counterexamples**:
   - **Wrong Order of Indices in $\Omega_{P_i, P_j}$**: $\Omega_{P_i, P_j}$ tests **suffixes of the winner $P_i$** against **prefixes of the gambler $P_j$**; transposing $\Omega_{P_i, P_j}$ and $\Omega_{P_j, P_i}$ produces wrong probabilities whenever $\text{Overlap}(P_i, P_j) \ne \text{Overlap}(P_j, P_i)$.
6. **Canonical Representative Problems**:
   - `W4A-02` (`[CTSC2006] 歌唱王国`), `W4A-09` (`[SDOI2017] 硬币游戏`), `W4A-19` (Variance of Pattern Waiting Time & $k$-th Occurrence Renewal), `W4A-27` (Pattern Race with Initial Seed Prefix $S_0$).

---

### `T-4A-05`. Automaton DP (`自動機上のDP`), `DP套DP` 4-Stage Compiler & Binary-Grouped Dynamic AC (`CF 710F`)
1. **Multilingual Name**:
   - `[EN]`: Automaton DP, `DP-of-DP` (`DP套DP`) 4-Stage State-Compression Compiler & Binary-Grouped Dynamic Aho–Corasick
   - `[ZH]`: 自动机 DP、`DP套DP` 四阶段状态压缩编译器（差分编码 + BFS + Hopcroft/Brzozowski 最小化）与二进制分组动态 AC 自动机 (`CF 710F`)
   - `[JA]`: オートマトン DP・`DP of DP` (内側 DP の DFA 化 + Hopcroft/Brzozowski 最小化) とバイナリグルーピング動的 AC
2. **Diagnostic Signal**:
   - Counting outer strings $T \in \Sigma^n$ classified by the output of an inner string DP $f(S, T)$ (e.g., $\text{LCS}(S, T) = k$ for $|S| \le 20$, edit distance $\le 2$, or game-theoretic regex evaluation), or online pattern insertions/deletions with substring occurrence queries (`CF 710F`).
3. **Core Combinatorial Word Invariant**:
   - **4-Stage `DP套DP` Compiler Pipeline (`Section 3.3`)**:
     1. *Stage 1 (Relative/Capped Inner State Encoding)*: Encode the inner DP array $v$ so values stay bounded (e.g., for LCS, horizontal adjacent differences $\Delta_i = dp[i] - dp[i-1] \in \{0, 1\}$ reduce $(n+1)^m$ states to $2^m$ bitmasks; for Edit Distance $\le K$, track offset strip $dp[i] - i \in [-K, K+1]$ of size $\le 3^{2K+1}$).
     2. *Stage 2 (Reachable DFA Discovery via BFS)*: Explore only states reachable from $v_{\text{init}}$ on input $S$, shrinking the state space by $10\times$–$100\times$ before outer DP.
     3. *Stage 3 (Offline Hopcroft Partition Refinement / Brzozowski Double Reversal)*: Minimize the discovered DFA $\mathcal{A}$ via Hopcroft's $O(|\Sigma||Q|\log |Q|)$ refinement or Brzozowski's Theorem $\mathcal{A}_{\min} = \text{det}(\text{rev}(\text{det}(\text{rev}(\mathcal{A}))))$.
     4. *Stage 4 (Outer DP / Matrix Exponentiation)*: Run the $O(n \cdot |Q_{\min}| \cdot |\Sigma|)$ outer DP on the minimized transition table.
   - **Binary-Grouped Dynamic AC (`二进制分组` — Bentley–Saxe)**: Decompose active patterns into $O(\log M)$ static AC automata of power-of-two sizes; rebuild only the carries on insert, and maintain parallel add-groups and delete-groups for deletions.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - LCS `DP套DP` ($|S| = m \le 15$): $O(2^m m |\Sigma| + n 2^m |\Sigma|)$ using the 4-instruction Allison–Dix transition (`T-4B-05`).
   - Binary-Grouped AC (`CF 710F`): $O(\sum |P| |\Sigma| \log M)$ total build work and $O(|T| \log M)$ total query work.
5. **Canonical Failure Modes & Counterexamples**:
   - **Calling `build_AC()` After Every Insertion**: Rebuilds the entire Trie of size $O(\sum |P|)$ on each of $Q$ insertions $\implies O((\sum |P|)^2)$ TLE!
   - **Failing to Propagate `bad[u] |= bad[fail[u]]` in BFS Order**: Misses forbidden patterns that are proper suffixes of longer Trie prefixes.
6. **Canonical Representative Problems**:
   - `W4A-05` (`[JSOI2007] 文本生成器`), `W4A-14` (`CF 710F — String Set Queries`), `W4A-30` (`[TJOI2018] 游园会` / LCS `DP套DP`), `W4A-37` (Edit-Distance Strip `DP套DP` + Hopcroft Minimization).

---

## Wave 4B: Subsequence Automata (DASG), Arch Factorization, Invertible Matrices, Seaweed & Bit-Parallel LCS

### `T-4B-01`. Directed Acyclic Subsequence Graph (`序列自动机` / DASG), Four-Comb Product Automata & 2D Predecessor Rectangles
1. **Multilingual Name**:
   - `[EN]`: Directed Acyclic Subsequence Graph (`DASG`), Leftmost-Prefix Dominance, Four-Comb Product Automata & 2D Predecessor-Rectangle Path Counting
   - `[ZH]`: 序列自动机 (`DASG`)、最左前缀贪心优势定理、四合一乘积自动机 (`[HEOI2015] 最短不公共子串`) 与二维前驱矩形去重计数
   - `[JA]`: 部分列オートマトン (`Subsequence Automaton` / `DASG`)・直積オートマトン BFS と二次元累積和による共通部分列数え上げ
2. **Diagnostic Signal**:
   - Distinct subsequence counting, shortest/lexicographically extremal subsequence synthesis, interleaved disjoint subsequence packing (`CF 1149B`), or joint Substring-vs.-Subsequence language difference queries (`[HEOI2015]`).
3. **Core Combinatorial Word Invariant**:
   - **Leftmost-Prefix Dominance (`Theorem 1.1`)**: Because occurrence sets nest monotonically ($j_1 \le j_2 \implies \{k > j_1\} \supseteq \{k > j_2\}$), the greedy leftmost embedding $\text{pos}_S(P)$ strictly maximizes the available suffix $S[j+1..N]$ for all future extensions, establishing a **1-to-1 bijection** between distinct subsequences $P \preceq S$ and directed paths from $0$ in $\text{DASG}(S)$ ($\delta(i, c) = \text{nxt}_S[i][c]$).
   - **Four-Comb Product Automaton (`Theorem 1.2` — `[HEOI2015]`)**: Pairing $\mathcal{A}^+(A) \in \{\text{SAM}(A), \text{DASG}(A)\}$ with $\mathcal{A}^-(B) \in \{\text{SAM}(B), \text{DASG}(B)\}$ turns all four combinations of *"shortest string that is a (Substring / Subsequence) of $A$ and NOT a (Substring / Subsequence) of $B$"* into a uniform 0-1 BFS on $\mathcal{A}^+(A) \times \mathcal{A}^-(B)$ finding the shortest path to $(\delta^+(u, c) \ne \bot, \delta^-(v, c) = \bot)$!
   - **Alphabet-Independent $O(|A||B|)$ Distinct Common Subsequence Counting (`Section 1.3.4`)**: A matching pair $(i', j')$ with $A[i'] = B[j'] = c$ is the leftmost jump from $(i, j)$ on character $c$ **iff** $\text{prev}_A[i'] \le i < i'$ and $\text{prev}_B[j'] \le j < j'$. Thus $(i', j')$ adds $dp[i'][j']$ to the 2D rectangle $[\text{prev}_A[i'], i'-1] \times [\text{prev}_B[j'], j'-1]$, removing the $|\Sigma|$ factor via 2D difference arrays!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - $\text{DASG}(S)$ construction: $O(N|\Sigma|)$ (or $O(N)$ persistent segmented arrays for large $|\Sigma|$).
   - Four-Comb Product Automaton: $O(|A||B||\Sigma|)$; Distinct Common Subsequences of $A, B$: $O(|A||B|)$ (alphabet-independent!).
5. **Canonical Failure Modes & Counterexamples**:
   - **Following `link[v]` in $\text{SAM}(B)$ During Product BFS**: In $\text{SAM}(A) \times \text{SAM}(B)$, taking a suffix link in $\text{SAM}(B)$ on a missing transition drops a prefix of the current word and tests a different string! If $\delta_B(v, c) = \bot$, transition directly to $\bot$.
   - **Using Subtractive $2dp[i-1] - dp[\text{prev}[i]-1]$ Under $\min(K, \cdot)$ Clamping (`CF 1183H`)**: Subtracting a clamped value corrupts counts; always sum out-edges additively on $\text{DASG}(S)$.
6. **Canonical Representative Problems**:
   - `W4B-05` (`CF 1303E`), `W4B-07` (Distinct Common Subsequences via 2D Predecessor Rectangles), `W4B-11` (`[HEOI2015] 最短不公共子串`), `W4B-12` (`CF 1149B — Three Religions`).

---

### `T-4B-02`. Hébrard's Arch Factorization, Universality Index $\iota(S)$, Range SAS & Simon's Congruence ($\sim_k$)
1. **Multilingual Name**:
   - `[EN]`: Hébrard's Arch Factorization, Universality Index $\iota(S)$, $O(\log N)$ Range Shortest Absent Subsequence (`Range SAS`) & Simon's Congruence ($\sim_k$)
   - `[ZH]`: Hébrard 拱分解 (`Arch Factorization`)、全子序列阶 $\iota(S)$、倍增区间最短缺失子序列与 Simon 同余 ($\sim_k$)
   - `[JA]`: アーチ分解 (`Arch Factorization`)・普遍性指数 $\iota(S)$・区間最短非部分列クエリと Simon 合同 ($\sim_k$)
2. **Diagnostic Signal**:
   - Testing whether $S$ (or $S[l..r]$) contains all $\sigma^k$ strings of length $k$ as subsequences, reconstructing a shortest absent subsequence (`SAS`) on ranges $[l, r]$, or finding a shortest subsequence distinguishing two strings $U \ne V$.
3. **Core Combinatorial Word Invariant**:
   - **Hébrard's Arch Factorization (`Theorem 1.3`, 1991)**: Greedily factoring $S = A_1 A_2 \dots A_k R$ where each arch $A_r = S[l_r..r_r]$ is the shortest prefix of the remaining string containing all $\sigma$ letters of $\Sigma$ (and $\text{alph}(R) \subsetneq \Sigma$) yields the exact **universality index** $\iota(S) = k$ and shortest absent subsequence length $\text{sas}(S) = k + 1$.
   - **Canonical Absent Witness**: Choosing the **last character** $m_r = S[r_r]$ of each arch (which appears **only once** in $A_r$, at its very end!) plus any $m_{k+1} \in \Sigma \setminus \text{alph}(R)$ produces $M = m_1 m_2 \dots m_k m_{k+1} \not\preceq S$, because matching $m_1$ consumes all of $A_1$, matching $m_2$ consumes all of $A_2$, ..., and $m_{k+1} \notin R$.
   - **Simon's Congruence ($\sim_k$ — Simon 1975)**: $U \sim_k V$ iff $U$ and $V$ have the exact same set of subsequences of length $\le k$, iff $\iota(U, V) \ge k$. Barker et al. (2020) build the **Simon-Tree** partitioning $[0..|U|] \times [0..|V|]$ by $\sim_k$-classes in **$O(|U| + |V|)$ time** (independent of $|\Sigma|$) to output a minimal distinguishing subsequence!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Whole string: $O(N)$ greedy arch sweep.
   - Range $[l, r]$ SAS (`Range SAS`): Precompute $\text{arch\_end}[l] = \max_{c \in \Sigma} \text{nxt}_S[l-1][c]$ via a sliding window and binary lift $\text{jump}[k][l] = \text{jump}[k-1][\text{jump}[k-1][l] + 1]$ to count arches inside $[l, r]$ in **$O(\log N)$ time per query**!
5. **Canonical Failure Modes & Counterexamples**:
   - **Forward Greedy $\arg\max_c \text{nxt}[u][c]$ Fails Lexicographical Tie-Breaking (`ARC 081 E`)**: To find the *lexicographically smallest* shortest absent subsequence, you must compute shortest-path distances $d[u] = 1 + \min_c d[\text{nxt}[u][c]]$ backward from $N \downarrow 0$ and step to the **smallest letter $c$** achieving $d[\text{nxt}[u][c]] = d[u] - 1$, not the farthest index $\arg\max_c \text{nxt}[u][c]$!
6. **Canonical Representative Problems**:
   - `W4B-02` (`AtCoder ARC 081 E — Don't Be a Subsequence`), `W4B-03` (`CF 1924A`), `W4B-24` ($O(\log N)$ Range Shortest Absent Subsequence via Arch Binary Lifting), `W4B-41` (Shortest Distinguishing Subsequence via Simon's Congruence).

---

### `T-4B-03`. Invertible Subsequence Automaton Matrices (`子序列 DP 矩阵可逆性`) & $O(|\Sigma|)$ Matrix-Free Range Queries
1. **Multilingual Name**:
   - `[EN]`: Invertible Subsequence Automaton Matrices ($\det M_c = 1$) & Matrix-Free $O((N+Q)|\Sigma|)$ Range Distinct Subsequence Queries
   - `[ZH]`: 子序列自动机可逆转移矩阵（行列式为 $1$ 的初等矩阵逆）与无矩阵 $O((N+Q)|\Sigma|)$ 区间本质不同子序列查询
   - `[JA]`: 部分列 DP 遷移行列の可逆性 (`maspy` 法) と $O((N+Q)|\Sigma|)$ 区間相異なる部分列数え上げ
2. **Diagnostic Signal**:
   - $Q$ range queries $(l, r)$ (or two-ended deque updates) asking for the number of **distinct subsequences** (or weighted subsequences, or fixed-pattern wildcard subsequence counts) of $S[l..r]$ modulo $M$, where Segment Tree matrix multiplication $O((N + Q \log N)|\Sigma|^3)$ is $27\times$–$600\times$ too slow.
3. **Core Combinatorial Word Invariant**:
   - **Rank-1 Elementary Matrix & Exact Inverse (`Theorem 2.1`)**: Over **any commutative ring $\mathcal{R}$**, the $(|\Sigma|+1) \times (|\Sigma|+1)$ distinct-subsequence transition matrix $M_c = I_{\sigma+1} + \mathbf{e}_c \mathbf{1}^T$ sets row $c$ to the sum of all rows and has $\det(M_c) = 1$, with exact $O(1)$-sparse inverse:
     $$M_c^{-1} = I_{\sigma+1} - \mathbf{e}_c (\mathbf{1} - 2\mathbf{e}_c)^T \quad \text{(subtract all other rows } a \ne c \text{ from row } c\text{)}.$$
     *(For weighted subsequences where picking $c$ multiplies weight by $\alpha_c$, $\det(M_{c,\alpha_c}) = \alpha_c$, which is invertible iff $\alpha_c \in \mathcal{R}^\times$!)*
   - **Matrix-Free Bilinear Dot Product (`Theorem 2.2`)**: Instead of storing $(|\Sigma|+1) \times (|\Sigma|+1)$ prefix matrices, maintain only the **1D row vectors** $\mathbf{u}_i^T = \mathbf{e}_0^T P_i$ and **1D column vectors** $\mathbf{v}_i = Q_i (\mathbf{1} - \mathbf{e}_0)$. Then $\mathbf{u}_i^T$ obeys the $O(1)$ scalar recurrence
     $$\mathbf{u}_i^T = 2\mathbf{u}_{i-1}^T - \mathbf{u}_{\text{last}[S[i]] - 1}^T,$$
     and $\mathbf{v}_i = M_{S[i]}^{-1} \mathbf{v}_{i-1}$ adds $-v_{i-1}[c]$ to all entries $a \ne c$ via a single global lazy offset $g_i = g_{i-1} - v_{i-1}[c]$ in $O(1)$ time! Answering $[l, r]$ reduces to a single length-$(|\Sigma|+1)$ dot product $\mathbf{u}_r^T \cdot \mathbf{v}_{l-1}$ in **$O(|\Sigma|)$ time**!
   - **Fixed-Pattern Upper-Unitriangular Inverse (`CF 1426F`)**: Counting occurrences of fixed pattern $P[1..K]$ uses $(K+1) \times (K+1)$ upper-unitriangular matrices $A_c = I_{K+1} + \sum_{r : P[r]=c} E_{r-1, r}$ with $A_c^{-1} = I_{K+1} - \sum_{r : P[r]=c} E_{r-1, r}$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Precomputation: $O(N)$ time (or $O(N|\Sigma|)$ to materialize $\mathbf{u}_i, \mathbf{v}_i$).
   - Query $[l, r]$: **$O(|\Sigma|)$ time and $O(1)$ auxiliary space** (zero segment trees!).
   - Deque `push/pop_front/back`: Two-stack queue maintaining $Q_{\text{front}}^{-1}$ and $P_{\text{back}}$ in $O(|\Sigma|)$ amortized time per op.
5. **Canonical Failure Modes & Counterexamples**:
   - **Non-Invertibility under Gap $\ge 2$ (`ABC 214 F`) or Tropical $(\min, +)$ (`CF 750E`)**: Gap $\ge 2$ transitions overwrite old states ($\det = 0$), and the tropical semiring $(\mathbb{Z}\cup\{\infty\}, \min, +)$ has no additive inverse—both **must** use a Segment Tree.
6. **Canonical Representative Problems**:
   - `W4B-15` (`CF 1426F` / Range Fixed-Pattern Subsequence Multiplicity in $O(1)$), `W4B-27` (Matrix-Free $O((N+Q)|\Sigma|)$ Range Distinct Subsequences), `W4B-33` (Deque Distinct Subsequence Maintenance).

---

### `T-4B-04`. Tiskin's Seaweed Matrices (`海草矩阵`), Unit-Monge $\boxdot$ Multiplication & $O(N \log^2 N)$ Range LIS
1. **Multilingual Name**:
   - `[EN]`: Tiskin's Seaweed Matrices (Braid Monoid), $O(K \log K)$ Unit-Monge Permutation Multiplication ($\boxdot$) & $O(N \log^2 N)$ Sparse Range LIS
   - `[ZH]`: 海草矩阵 (`Seaweed Matrix`)、$O(K \log K)$ 单位蒙日矩阵乘法 ($\boxdot$) 与 $O(N \log^2 N)$ 稀疏区间最长上升子序列 (`[国家集训队论文 2021]`)
   - `[JA]`: Seaweed 行列 (`Tiskin`)・Unit-Monge 行列積 ($\boxdot$) による全区間 LCS クエリと区間 LIS
2. **Diagnostic Signal**:
   - Answering $Q$ **semi-local LCS queries**:Substring-vs.-Full $\text{LCS}(A, B[l..r])$ (`[THUPC 2021]`), Prefix-Substring $\text{LCS}(A[1..i], B[l..r])$, or **Range LIS** $\text{LIS}(B[l..r])$ on a permutation $B[1..N]$ ($N, Q \le 10^5$).
3. **Core Combinatorial Word Invariant**:
   - **Planar Uncrossing & Cross-Difference Permutation (`Theorem 3.1`)**: Route $M + N$ wires entering at left rowports $-(1..M)$ and top columnports $1..N$. At cell $(i, j)$, two wires cross if $A[i] \ne B[j]$ and ** already-crossed wires OR matching cells ($A[i] = B[j]$) uncross (bounce)** (`if (A[i] == B[j] || u > W[j]) swap(u, W[j])`).
   - **Unified Three-Family Semi-Local LCS Dominance (`Theorem 3.2`)**: Let $W[k]$ be the entry port of the wire exiting bottom column $k \in [1, N]$, and $R[i]$ be the entry port exiting right row $i \in [1, M]$:
     1. *Substring $B[l..r]$ vs. All of $A$*: $\text{LCS}(A, B[l..r]) = (r - l + 1) - \#\{k \in [l, r] \mid W[k] \ge l\} = \#\{k \in [l, r] \mid W[k] < l\}$.
     2. *Prefix $A[1..i]$ vs. Substring $B[l..r]$*: $\text{LCS}(A[1..i], B[l..r]) = \#\{k \in [l, r] \mid -i \le W[k] < l\}$.
     3. *Suffix $A[i..M]$ vs. Prefix $B[1..r]$*: $\text{LCS}(A[i..M], B[1..r]) = r - \#\{k \in [1, r] \mid W[k] > -i\} - \#\{x \in [i, M] \mid 1 \le R[x] \le r\}$.
   - **$O(K \log K)$ Unit-Monge $\boxdot$ Staircase Merge**: Splitting a $K \times K$ Unit-Monge product $D_{P_1} \boxdot D_{P_2}$ at $M = \lfloor K/2 \rfloor$ defines an advantage function $\delta(i, k) = F_R(i, k) - F_L(i, k)$ that is monotone in both $i$ and $k$; walking its separator staircase from $(0, K) \to (K, 0)$ takes $\le 2K$ $O(1)$-steps!
   - **Range LIS Reduction (`Section 3.3.4`)**: $\text{LIS}(B[l..r]) = \text{LCS}((1, 2, \dots, N), B[l..r])$, where the $N \times N$ grid has **only $N$ total match cells** (one per row)! Divide-and-conquer over rows $x \in [1, N]$ compresses active columns to size $K$ and multiplies via $\boxdot$ in $T(K) = 2T(K/2) + O(K \log K) = O(N \log^2 N)$!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Comb construction: $O(MN)$ time (8 lines of code!) + $O(\log N)$ Wavelet/Chairman Tree per query.
   - Dynamic `append_A(c)` / `append_B(c)`: $O(N)$ / $O(M)$ per character.
   - Range LIS: $O(N \log^2 N)$ build + $O(\log N)$ per query $[l, r]$.
5. **Canonical Failure Modes & Counterexamples**:
   - **Confusing Entry-to-Exit $p[l]$ with Exit-to-Entry $W[k]$**: In Tiskin's convention, $p[i] = k \iff W[k] = i$. Using `# { i in [l, r] : p[i] <= r }` counts top-entering wires instead of bottom-exiting wires, which fails for Prefix-Substring queries $\text{LCS}(A[1..i], B[l..r])$ because negative rowports $-i$ are entry values stored in $W[k]$, not indices of $p$!
6. **Canonical Representative Problems**:
   - `W4B-28` (`[THUPC 2021] 区间 LCS`), `W4B-35` (Prefix-Substring LCS via Signed Seaweed), `W4B-39` (Dynamic Character Appends + Semi-Local LCS), `W4B-42` ($O(N \log^2 N)$ Range LIS via Sparse Seaweed $\boxdot$).

---

### `T-4B-05`. Bit-Parallel LCS & Edit Distance (Allison–Dix Borrow Identity, Myers' Levenshtein & Hirschberg Bitset Reconstruction)
1. **Multilingual Name**:
   - `[EN]`: Bit-Parallel LCS & Edit Distance (Allison–Dix 4-Instruction Hardware Borrow Identity, Myers' Levenshtein & Hirschberg Space-Optimal Bitset Alignment)
   - `[ZH]`: 位并行 LCS 与编辑距离（Allison–Dix 硬件借位传播公式、Myers 编辑距离与 Hirschberg 线性空间回溯）
   - `[JA]`: ビット並列 LCS・編集距離（Allison–Dix の引き算ボロー伝播・Myers 法・Hirschberg 線形空間復元）
2. **Diagnostic Signal**:
   - Computing $\text{LCS}(A, B)$ or $\text{EditDistance}(A, B)$ for $M, N \in [3 \cdot 10^4, 10^5]$, reconstructing the actual LCS alignment string in $O(M+N)$ memory, or building LCS `DP套DP` transition tables `trans[D][c]` in $O(1)$ bitwise ops.
3. **Core Combinatorial Word Invariant**:
   - **Allison–Dix / Hyyrö Interval-Local Borrow Absorption (`Theorem 4.1`)**: Pack row differences $D_{i-1}[j] = dp[i-1][j] - dp[i-1][j-1] \in \{0, 1\}$ into bitmask $V$ (whose $1$-bits at $j_1 < \dots < j_k$ partition $[1, N]$ into intervals $I_r = [j_{r-1}+1, j_r]$), and let $M[c]$ be the match mask of character $c$ in $B$. Setting
     $$X = V \mathbin{|} M\bigl[A[i]\bigr], \qquad Y = (V \ll 1) \mathbin{|} 1 \quad \implies \quad V' = X \mathbin{\&} \sim(X - Y)$$
     updates **all $k+1$ intervals in parallel**: inside each $I_r$, $Y$ has a single $1$-bit at the bottom $j_{r-1}+1$ and $X$ has a guaranteed $1$-bit at the top $j_r$, so the subtraction borrow in $X - Y$ propagates from $j_{r-1}+1$ up to the **earliest match $j'_r \in I_r$ of $X$**, flips bit $j'_r$ from $1 \to 0$, and **never crosses $j_r$ into $I_{r+1}$**!
   - **Myers' Bit-Parallel Levenshtein Difference Vectors (1999)**: Encodes $\Delta V, \Delta H \in \{-1, 0, +1\}$ via bitvector pairs $(VP, VN)$ and $(HP, HN)$, switching between **global edit distance** ($X' = (HP \ll 1) \mathbin{|} 1$) and **semi-local substring edit distance** ($X' = HP \ll 1$) via a single bit $b_0 \in \{0, 1\}$.
   - **Hirschberg + Bit-Parallel LCS (`Section 4.2.2`)**: Running Allison–Dix forward on $A[1..M/2]$ and backward on $A[M/2+1..M]^R$ to split at $j^* = \arg\max_j (\text{fwd}[j] + \text{bwd}[N-j])$ reconstructs the actual LCS string in $\sum_{d \ge 0} O(MN / (2^d w)) = O(MN/w)$ time and **$O(M + N)$ memory**!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - $O(MN / w)$ time ($w = 64$, $\approx 3.9 \times 10^7$ word ops at $N = 50{,}000$) and $O((M + |\Sigma|) N / w)$ space (or $O(M+N)$ space with Hirschberg).
5. **Canonical Failure Modes & Counterexamples**:
   - **Unsliced Pattern Masks Inside Hirschberg Recursion**: Rebuilding or scanning $M[c]$ over the full length $N$ instead of the active slice width $r_B - l_B + 1$ and active characters of $A[l_A..r_A]$ degrades $O(MN/w)$ to $O(MN \log M / w)$ or $O(M N)$.
6. **Canonical Representative Problems**:
   - `W4B-19` (Bit-Parallel LCS + Hirschberg Linear-Space Alignment Reconstruction), `W4B-26` (Myers' Bit-Parallel Semi-Local Substring Edit Distance), `W4B-36` (Bit-Parallel Circular LCS & Constrained Alignment).


---

## Wave 5A: Word Equations, Parallel DSU (`倍增并查集`), String Inequalities, Wheeler/De Bruijn Graphs & Strings on Trees

### `T-5A-01`. Signed Binary-Lifting DSU (`倍增并查集`), Root Self-Palindrome Bit `is_pal[k][r]` & Online Conflict Rollback
1. **Multilingual Name**:
   - `[EN]`: Signed Binary-Lifting DSU (`Parallel DSU`), Root Self-Palindrome Invariant (`is_pal[k][r]`) & Online Potential Amortization
   - `[ZH]`: 带权倍增并查集 (`[SCOI2016] 萌萌哒`)、根节点自回文标记 `is_pal[k][r]` 与在线势能均摊/冲突回滚
   - `[JA]`: ダブリング Union-Find (`倍増 DSU` / 区間等価クエリ)・符号付き反転伝播と自己回文ビット
2. **Diagnostic Signal**:
   - $M$ bulk substring equality constraints $S[l_1..l_1+L-1] = S[l_2..l_2+L-1]$ ($t=0$) or reversed/palindrome constraints $S[l_1..l_1+L-1] = S[l_2..l_2+L-1]^R$ ($t=1$) over $S[1..N]$ ($N, M \le 5 \cdot 10^5$), counting connected components $C$ ($|\Sigma|^C$) or checking online consistency against point inequalities $S[u] \ne S[v]$.
3. **Core Combinatorial Word Invariant**:
   - **Lossless Dyadic Block Covering (`Theorem 1.1`)**: Let $k = \lfloor \log_2 L \rfloor$. Because $[0, 2^k-1] \cup [L-2^k, L-1] = [0, L-1]$, each length-$L$ equation is 100% equivalent to **two** level-$k$ block equations (with cross-swapped offsets $B_k(l_1) = B_k(l_2+L-2^k)^R$ and $B_k(l_1+L-2^k) = B_k(l_2)^R$ when $t=1$).
   - **Signed Half-Block Pushdown & Root Self-Palindrome Invariant (`Contract 4.1`)**: Pushing $B_k(i) = B_k(r)^R$ ($d=1$) from level $k$ to $k-1$ with $h = 2^{k-1}$ cross-swaps half-blocks: $B_{k-1}(i) = B_{k-1}(r+h)^R$ and $B_{k-1}(i+h) = B_{k-1}(r)^R$. Crucially, if a merge at level $k$ connects two nodes in the **same** component with net reversal parity $1$, it induces a **self-reversal $B_k(r) = B_k(r)^R$ on the component root $r$**, recorded in `is_pal[k][r] = 1` and pushed down via `UNITE(k-1, r, r + h, 1)`!
   - *(Alternative $S' = S \cdot S^R$ Concatenation Trick)*: Pre-uniting $i \sim 2N+1-i$ at level $0$ on a length-$2N$ string turns every reversed equation into a pure $t=0$ forward equation.
   - **Online Potential Bound (`Theorem 1.2`)**: $\Phi = \sum_{k=0}^K (c_k + p_k) \le 2N(K+1)$ drops by $\ge 1$ on every productive recursive call, bounding online `merge_block` calls by $2M + 6N(\lfloor \log_2 N \rfloor + 1)$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Offline top-down sweep or online recursive `merge_block`: $O((M + N \log N)\alpha(N))$ time and $O(N \log N)$ space.
5. **Canonical Failure Modes & Counterexamples**:
   - **The Self-Reversal Root Loop Bug (`Pitfall 1`)**: On $N = 4$ with a single palindrome query $S[1..4] = S[1..4]^R$ ($k=2$), calling `UNITE(2, 1, 1, rev=1)` sees `find(2, 1) == find(2, 1)`; returning early without setting `is_pal[2][1] = 1` drops the constraint completely and outputs $C = 4$ instead of $C = 2$!
6. **Canonical Representative Problems**:
   - `W5A-01` (`[SCOI2016] 萌萌哒` / Luogu P3295), `W5A-14` (Signed Palindrome & Substring Equations), `W5A-29` (Online Word Equations with Inequality Conflict Rollback).

---

### `T-5A-02`. Tree Binary-Lifting DSU (`树上倍增并查集`) & Huge-Length ($N \le 10^{18}$) Word Equations
1. **Multilingual Name**:
   - `[EN]`: Signed Tree Binary-Lifting DSU for Path Equations & Huge-Length ($N \le 10^{18}$) Word Equations (Fine–Wilf Folding, Dihedral Reflections & Jeż's Recompression)
   - `[ZH]`: 树上带权倍增并查集与超大长度 ($N \le 10^{18}$) 词方程（Fine–Wilf 周期折叠、二面体反射平移群与 Jeż 重压缩）
   - `[JA]`: 木上のダブリング Union-Find と巨大長 ($N \le 10^{18}$) 語方程式（周期折りたたみ・Recompression）
2. **Diagnostic Signal**:
   - **Regime A**: Path-equality constraints $\text{str}(u_1 \rightsquigarrow v_1) = \text{str}(u_2 \rightsquigarrow v_2)$ on a tree $T$ ($N, M \le 2 \cdot 10^5$).
   - **Regime B**: Word equations / palindrome constraints on a string of huge length $N \le 10^{18}$ with $M \le 10^5$ equations.
3. **Core Combinatorial Word Invariant**:
   - **LCA Path Splitting + Signed Tree DSU (`Section 1.5`)**: Every simple tree path $u \rightsquigarrow v$ splits at $w = \text{lca}(u, v)$ into an upward prefix $u \uparrow w$ and a downward suffix $\text{child}(w, v) \downarrow v$ which is the **exact reversal** of the upward path $v \uparrow \text{child}(w, v)$! Thus equating $\text{str}(u_1 \rightsquigarrow v_1) = \text{str}(u_2 \rightsquigarrow v_2)$ splits into $\le 3$ pairs of upward ancestor equations (with $t \in \{0, 1\}$) on tree blocks $B_k(u) = (u \uparrow 2^k)$, pushed down via $\text{anc}(u, 2^{k-1})$!
   - **Three Contraction Engines for $N \le 10^{18}$ (`Section 1.4`)**:
     1. *Plandowski / Fine–Wilf Euclidean Period Folding*: An overlapping shift $S[l_1..r_1] = S[l_2..r_2]$ ($p = l_2 - l_1$) folds $[l_2, r_2]$ into $[l_1, l_1+p-1]$ via $x \mapsto l_1 + ((x-l_1)\bmod p)$; overlapping periods $p, q$ contract via $\gcd(p, q)$ or $(p, q \bmod p)$ in $O(\log N)$ Euclidean steps.
     2. *Dihedral Reflection-to-Translation Reduction*: Two overlapping palindrome involutions $\sigma_1(x) = l_1+r_1-x$ and $\sigma_2(x) = l_2+r_2-x$ compose to a pure translation $\sigma_2(\sigma_1(x)) = x + (l_2+r_2-l_1-r_1)$.
     3. *Jeż's Recompression (JACM 2016)*: Alternating $c^k \to c_k$ and $\Sigma_L \times \Sigma_R$ pair compression solves general word equations in $O(M \log N)$ phases.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Tree Binary-Lifting DSU: $O((M + N \log N)\alpha(N))$ time; Huge-$N$ Word Equations: $O(M \log^2 N)$ time.
5. **Canonical Failure Modes & Counterexamples**:
   - Naively coordinate-compressing endpoint intervals on $N = 10^{18}$ without period modulo folding: a single equation $S[1..10^{18}-1] = S[2..10^{18}]$ has $p = 1$ and $O(N)$ fragments unless folded modulo $p$.
6. **Canonical Representative Problems**:
   - `W5A-36` (Huge-Length $N \le 10^{18}$ Palindrome & Translation Equations), `W5A-48` (Tree Binary-Lifting DSU + Path Inequality Graph).

---

### `T-5A-03`. String Inequality Graphs, SA Adjacency Theorem (`CF 1526E`), 2-SAT & SCC Longest Path
1. **Multilingual Name**:
   - `[EN]`: String Inequality Digraphs, Suffix Array Adjacency Theorem (`CF 1526E`), 2-SAT Prefix Branching & Tarjan SCC Condensation
   - `[ZH]`: 字符串不等式差分约束图、后缀数组相邻判定定理 (`CF 1526E`)、2-SAT 字典序分支与 SCC 缩点最长路
   - `[JA]`: 文字列不等式グラフ・接尾辞配列隣接条件 (`CF 1526E`)・2-SAT 辞書順制約と強連結成分分解
2. **Diagnostic Signal**:
   - Reconstructing or counting strings satisfying substring inequalities $S[l_1..r_1] \le S[l_2..r_2]$ (given LCP witnesses), a target Suffix Array $\text{SA}[1..N]$ (`ARC 044 D`, `CF 1526E`), or 2-SAT vowel/consonant rules with $S \ge S_0$ (`CF 568C`).
3. **Core Combinatorial Word Invariant**:
   - **Suffix Array Adjacency Theorem (`Theorem 2.1`)**: With empty-suffix rank sentinel $\text{rk}[N+1] = 0$, $S$ has suffix array $\text{SA}[1..N]$ **iff** for every $i \in [1, N-1]$ with $u = \text{SA}[i], v = \text{SA}[i+1]$:
     1. $\text{rk}[u+1] < \text{rk}[v+1] \implies S[u] \le S[v]$ (permissive step), and
     2. $\text{rk}[u+1] > \text{rk}[v+1] \implies S[u] < S[v]$ (forced strict step).
     If $D = \sum_{i=1}^{N-1} [\text{rk}[\text{SA}[i]+1] > \text{rk}[\text{SA}[i+1]+1]]$, then $|\Sigma|_{\min} = D + 1$ and the number of valid strings over $|\Sigma| = K$ is $\binom{N + K - 1 - D}{N}$!
   - **Zero-One Weighted Inequality Digraph & SCC Feasibility (`Section 2.2.3`)**: After contracting equalities via Binary-Lifting DSU, add weight-$0$ edges for $\le$ and weight-$1$ edges for $<$. The system is feasible iff **no weight-$1$ edge has both endpoints inside the same SCC**; longest paths on the condensation DAG give $K_{\min} = 1 + \max_X \text{dist}[X]$ and the lexicographically smallest valid string.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Inverse SA: $O(N)$ time; General LCP-witnessed inequality system: $O((M + N \log N)\alpha(N))$ time.
5. **Canonical Failure Modes & Counterexamples**:
   - **Omitting Sentinel $\text{rk}[N+1] = 0$**: At $u = N$, $u+1 = N+1$ must have rank $0 < \text{rk}[v+1]$ so $S[N] = S[v]$ is permitted (`"banana"`, $u=6, v=4$).
   - **SA + `height` Boundary Trap**: For $u = \text{SA}[i-1], v = \text{SA}[i]$ with $\text{LCP} = h_i$, if $v + h_i > N$, the specification is **impossible** (since the larger suffix $S[v..N]$ cannot be a proper prefix of the smaller suffix $S[u..N]$!).
6. **Canonical Representative Problems**:
   - `W5A-03` (`AtCoder ARC 044 D`), `W5A-04` (`CF 1526E — Oolimry and Suffix Array`), `W5A-19` (`CF 568C — New Language`), `W5A-33` (Combined Substring Equations + LCP Inequalities).

---

### `T-5A-04`. De Bruijn Graphs, the BEST Theorem & Aho–Corasick DFA Eulerian String Counting
1. **Multilingual Name**:
   - `[EN]`: De Bruijn Graphs, the BEST Theorem, Aho–Corasick DFA Eulerian String Counting & Lex-Smallest Hierholzer
   - `[ZH]`: De Bruijn 图、BEST 定理（欧拉回路与内向生成树计数）、AC 自动机欧拉串计数与字典序最小 Hierholzer 算法
   - `[JA]`: De Bruijn グラフ・BEST 定理（オイラー閉路の数え上げ）・AC オートマトン上のオイラー路と辞書順最小構築
2. **Diagnostic Signal**:
   - Reconstructing or counting strings of huge length $N \le 10^{18}$ with prescribed $k$-mer multiplicities $c(w)$ (`AtCoder ABC 336 G`) or prescribed transition multiplicities on an Aho–Corasick DFA avoiding forbidden substrings.
3. **Core Combinatorial Word Invariant**:
   - **De Bruijn Subword-to-Edge Bijection & The BEST Theorem (`Theorem 3.1`)**: Strings with $k$-mer counts $c(w)$ correspond to Eulerian trails in $\mathcal{B}(\Sigma, k)$ (closed into circuits by a virtual edge $e_{\text{virt}} : u_{\text{end}} \to u_{\text{start}}$ rooted at $r = u_{\text{end}}$). Dividing out indistinguishable parallel copies of each $k$-mer $w$ (or each character transition $(u, c)$ in an AC DFA) gives the exact string count:
     $$\mathcal{E}_{\text{string}}(G) = \frac{t_{\text{in}}(G, r) \cdot \prod_{v \in V_{\text{act}}} \bigl(d(v) - 1\bigr)!}{\prod_{u \in V_{\text{act}}, c \in \Sigma} \text{count}(u, c)!},$$
     where $t_{\text{in}}(G, r) = \det L_{\text{out}}^{(r)}$ is the $(r, r)$-cofactor of the out-degree Laplacian restricted to active vertices $V_{\text{act}} = \{v : d(v) > 0\}$.
   - **Lex-Smallest Hierholzer Post-Order Invariant**: Consuming outgoing edges from each vertex in strictly increasing character order and reversing the post-order vertex list produces the **lexicographically smallest** Eulerian string in $O(|E|)$ time, because the first branch ever splices in at the earliest possible dead-end while committed prefix edges take minimum available characters.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - BEST Counting: $O(|V_{\text{act}}|^3 + \sum \log \text{count}(u, c))$ time (independent of $N \le 10^{18}$ if factorials are precomputed or mod is small/structured).
5. **Canonical Failure Modes & Counterexamples**:
   - **The AC-DFA vs. De Bruijn Parallel-Edge Trap (`Section 3.3`)**: In an Aho–Corasick DFA, two transitions $u \xrightarrow{c_1} v$ and $u \xrightarrow{c_2} v$ with **different characters $c_1 \ne c_2$** can land in the same state $v$ (e.g., root $0$). Dividing by $\prod_{u, v} A(u, v)!$ instead of $\prod_{u, c} \text{count}(u, c)!$ falsely treats distinct letters $c_1 \ne c_2$ as indistinguishable!
   - **Including Isolated Vertices ($d(v) = 0$) in $L_{\text{out}}$**: Forces $\det L_{\text{out}}^{(r)} = 0$ identically; always filter to $V_{\text{act}} = \{v : d(v) > 0\}$ and verify weak connectivity.
6. **Canonical Representative Problems**:
   - `W5A-11` (`CF 508D`), `W5A-24` (`AtCoder ABC 336 G — 16 Integers`), `W5A-41` (`UOJ 607` / AC-DFA BEST Theorem String Counting).

---

### `T-5A-05`. Burrows–Wheeler Transform (`BWT`), Bijective BWT (`BBWT`), Wheeler Graphs & $O(1)$ RLBWT Move Structures
1. **Multilingual Name**:
   - `[EN]`: Burrows–Wheeler Transform (`BWT`), Bijective BWT (`BBWT`), Wheeler Graphs & Nishimoto–Tabei $O(1)$ RLBWT Move Structures
   - `[ZH]`: BWT 变换、双射 BWT (`BBWT` Lyndon 分解)、Wheeler 图区间自动机与 RLBWT $O(1)$ Move Structure 跳转
   - `[JA]`: Burrows–Wheeler 変換 (`BWT`)・全単射 BWT (`BBWT`)・Wheeler Graph と RLBWT Move Structure ($O(1)$ LF 遷移)
2. **Diagnostic Signal**:
   - Inverting BWT or counting pattern occurrences in $O(|P|)$ steps on compressed text of length $N \le 10^{18}$ with $R \le 10^5$ BWT runs (`RLBWT`), sentinel-free bijective BWT on $\Sigma^N$, or indexing edge-labeled DFAs/graphs in $O(1)$ per character (`Wheeler Graphs`).
3. **Core Combinatorial Word Invariant**:
   - **LF-Mapping Rank Preservation (`Theorem 3.2`)**: Prepending the same character $c$ preserves relative order of cyclic shifts ($u_i c < u_j c \iff u_i < u_j \iff c u_i < c u_j$), so the $k$-th $c$ in $L$ is the $k$-th $c$ in $F$: $\text{LF}(i) = C[L[i]] + \text{Occ}(L[i], i)$.
   - **Bijective BWT (`BBWT` — Mantaci–Restivo–Rosone 2007)**: Factor $S = w_1 w_2 \dots w_m$ into non-increasing Lyndon words and sort all cyclic shifts of all $w_r$ under **$\omega$-order** ($u \prec_\omega v \iff u^\infty < v^\infty$); then $\text{LF}$ decomposes into $m$ disjoint cycles reconstructing $w_1, \dots, w_m$ with **no sentinel `$`**!
   - **Wheeler Graph Axioms & Two-Step Edge-Rank Transition (`Section 3.3`)**: Under vertex order $\prec$, incoming labels are homogeneous and monotone ($a_1 < a_2 \implies v_1 \prec v_2$) and same-label edges are order-preserving ($a_1 = a_2 \wedge u_1 \prec u_2 \implies v_1 \preceq v_2$). Unlike linear BWT, general Wheeler graphs have multi-degree vertices, so updating vertex interval $[l_V, r_V]$ on character $c$ is a **two-step lookup**:
     $$[l_E, r_E] = \bigl[\text{rank}_{\text{out}, c}(l_V - 1) + 1, \, \text{rank}_{\text{out}, c}(r_V)\bigr] \implies [l'_V, r'_V] = \bigl[\text{target}(c, l_E), \, \text{target}(c, r_E)\bigr].$$
   - **Nishimoto–Tabei (2021) Move Structure for RLBWT**: Each BWT run $L[l..r] = c^k$ maps by piecewise translation to a single interval in $F$. Splitting runs so no mapped interval spans more than $2$ output runs turns $\text{LF}(idx, \text{offset})$ into a **strictly $O(1)$-time pointer jump** in $O(R)$ space!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - FM-Index / Wheeler DFA backward search: $O(|P|)$ time; RLBWT Move Structure: $O(R \log R)$ build, $O(1)$ per LF-step (independent of $N \le 10^{18}$!).
5. **Canonical Failure Modes & Counterexamples**:
   - **Wheeler Forbidden Interval-Interleaving Obstruction**: If $u_1 \prec u_2 \prec u_3$ have $c$-edges to $v_1 = v_3 \ne v_2$, then $v_1 \preceq v_2 \preceq v_1 \implies v_1 = v_2$, a contradiction; no Wheeler ordering exists.
6. **Canonical Representative Problems**:
   - `W5A-15` (Cyclic BWT Inversion & Pattern Counting), `W5A-38` (Wheeler Graph Recognition & Interval DFA Matching), `W5A-43` (RLBWT Pattern Matching for $N \le 10^{18}$ via Piecewise-Translation / Move Structure).

---

### `T-5A-06`. Strings on Trees — Dual-Rank Tree SA (`Luogu P5353`), Leaf-Rooted Tree GSAM (`[ZJOI2015]`) & Centroid + Dual-SAM Split (`[CTSC2010] 珠宝商`)
1. **Multilingual Name**:
   - `[EN]`: Strings on Trees — Dual-Rank Tree Suffix Array, Leaf-Rooted Tree GSAM & Centroid Decomposition with Dual-SAM Split
   - `[ZH]`: 树上字符串三大引擎：双秩树上后缀数组 (`Luogu P5353`)、叶根广义 SAM (`[ZJOI2015] 诸神眷顾的幻想乡`) 与点分治双 SAM 根号分治 (`[CTSC2010] 珠宝商`)
   - `[JA]`: 木上の文字列アルゴリズム（木上の接尾辞配列・葉根一般化 SAM・重心分解 + 双方向 SAM）
2. **Diagnostic Signal**:
   - Sorting upward ancestor strings $S(u)$ and answering Tree LCP queries (`Luogu P5353`), counting distinct undirected path strings when leaves $|\mathcal{L}| \le 20$ (`[ZJOI2015]`), or counting occurrences of all $N^2$ tree paths inside a text $S[1..M]$ (`[CTSC2010] 珠宝商`, `CF 914E`).
3. **Core Combinatorial Word Invariant**:
   - **Dual-Rank Tree SA (`Invariant 4A`)**: Because distinct tree nodes $u \ne v$ can have identical upward strings $S(u) = S(v)$, maintain **two arrays** at step $k$: true string equivalence $\text{rk}_k[u]$ (used to test equality of $2^k$-halves) and tie-broken permutation rank $\text{id}_k[u] \in \{1..N\}$ (used for $O(N)$ bucket radix sorting). Sort by the 4-tuple $(\text{rk}_k[u], \text{rk}_k[\text{anc}(u, 2^k)], \text{id}_k[u], \text{id}_k[\text{anc}(u, 2^k)])$ and answer $\text{LCP}(S(u), S(v))$ in $O(\log N)$ by binary lifting on saved $\text{rk}_k$ layers!
   - **Leaf-Rooted Substring Cover (`Theorem 4.1` — `[ZJOI2015]`)**: Every simple path $u \rightsquigarrow v$ in an unrooted tree $T$ can be extended backward from $u$ away from $v$ until hitting a leaf $\ell \in \mathcal{L}$, making $\text{str}(u \rightsquigarrow v)$ a suffix of the root-to-node path $\ell \rightsquigarrow v$ in $T_\ell$ ($\le 2|\mathcal{L}|N$ GSAM states).
   - **Centroid + $\sqrt{M}$ Dual-SAM Split (`Invariant 4C` — `[CTSC2010] 珠宝商`)**: At centroid $c$ of size $S_c$, if $S_c \le \sqrt{M}$, brute-force all $O(S_c^2)$ pairs on $\text{SAM}_S$; if $S_c > \sqrt{M}$, walk from $c$ into $\text{SAM}_{S^R}$ and $\text{SAM}_S$, push path counts down both Link Trees to indices $1..M$ of $S$, and convolve $\sum_{i=1}^M \text{up}[i]\text{down}[i+1]$ in $O(S_c + M)$ time!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Dual-Rank Tree SA + LCP: $O(N \log N)$ build, $O(\log N)$ LCP; `[ZJOI2015]`: $O(|\mathcal{L}| N |\Sigma|)$; `[CTSC2010] 珠宝商`: $O((N\sqrt{M} + M\sqrt{N})\log N)$.
5. **Canonical Failure Modes & Counterexamples**:
   - **Why Kasai's $O(N)$ LCP Algorithm Fails on Branched Trees (`Step 1.2`)**: Multiple nodes $u, w$ can share parent $\text{fa}(u) = \text{fa}(w)$ and character $c(u) = c(w)$, so the SA-predecessor of $u$ may be $w$ (whose parent is $\text{fa}(u)$), completely disconnecting $\text{height}[\text{id}[u]]$ from $\text{height}[\text{id}[\text{fa}(u)]]$!
   - **The Child-Subtree Subtraction Threshold Bug in `[CTSC2010] 珠宝商` (`Step 4.2`)**: When $S_c > \sqrt{M}$ has $O(S_c)$ tiny leaf children of size $1$, running $O(|T_{\text{sub}}| + M)$ Link-Tree sweeps on every child subtree to subtract same-subtree pairs takes $O(S_c M) = O(NM)$ TLE! Always threshold each child subtree $|T_{\text{sub}}|$ against $\sqrt{M}$ as well.
   - **Amortized KMP Failure-Link Hazard on Branched Trees (`CF 291E`)**: Star-branching from a deep KMP state $q = |P|-1$ breaks amortization ($O(N|P|)$); always use the deterministic KMP DFA $\delta(q, c)$ or `slink` jumping ($O(\log |P|)$).
6. **Canonical Representative Problems**:
   - `W5A-18` (Dual-Rank Tree SA + Tree LCP Queries), `W5A-21` (`[ZJOI2015] 诸神眷顾的幻想乡`), `W5A-35` (`CF 914E — Palindromes in a Tree`), `W5A-46` (`[CTSC2010] 珠宝商`).

---

## Wave 5B & Frontier Stringology: Sturmian/Morphic Words, $SL_2(\mathbb{F}_p)$ Stack Hashing & Modern String Theory

### `T-5B-01`. Sturmian Words (6-Way Equivalence), Fibonacci Words & Rytter's Singular Words (`[周任飞 2017]`)
1. **Multilingual Name**:
   - `[EN]`: Sturmian Words (6-Way Equivalence), Fibonacci Words, Zeckendorf Addressing & Rytter's Singular Words ($w_k$)
   - `[ZH]`: Sturmian 串六重等价定理、Fibonacci 串近交换律、Zeckendorf 寻址与 Rytter 奇异串分解 (`[周任飞 2017]`)
   - `[JA]`: Sturmian 語の 6 同値特徴付け・フィボナッチ文字列・Zeckendorf 表現と特異語 (`Singular Words`)
2. **Diagnostic Signal**:
   - Problems on mechanical floor-sum strings $s_{\alpha, \rho}(n) = \lfloor(n+1)\alpha+\rho\rfloor - \lfloor n\alpha+\rho\rfloor$ (`ABC 313 G`), Fibonacci string prefixes $F_\infty[1..n]$ ($n \le 10^{18}$), or constructing worst-case inputs for KMP / PAM / Runs / Fine–Wilf.
3. **Core Combinatorial Word Invariant**:
   - **Morse–Hedlund & 6-Way Sturmian Equivalence (`Theorem 2.1–2.2`)**: For $\mathbf{w} \in \{0, 1\}^\omega$, $p_{\mathbf{w}}(n) = n + 1 \iff$ unique right/left-special factors $L_n = R_n^R \iff$ aperiodic 1-balanced ($||u|_1 - |v|_1| \le 1$) $\iff$ irrational mechanical rotation word $s_{\alpha, \rho} \iff$ grid cutting sequence with directive standard words $s_k = s_{k-1}^{d_k} s_{k-2} \iff$ central bispecial palindromes $\pi_k$ ($s_k = \pi_k ab$) hitting the Fine–Wilf threshold $|s_{k-1}| + |s_{k-2}| - 2$.
   - **5-Part Fibonacci & Singular Word Anatomy (`[周任飞 2017]`, `Section 2.3`)**:
     1. *Near-Commutativity*: $F_{k-1} F_{k-2} = \pi_k xy \iff F_{k-2} F_{k-1} = \pi_k yx$ ($xy \in \{\texttt{ab}, \texttt{ba}\}$).
     2. *Zeckendorf $O(\log n)$ Character Lookup*: $F_\infty[n]$ depends only on the lowest Zeckendorf digit $\epsilon_2(n)$.
     3. *Rytter's Singular Words $w_k$*: Complementing the boundary letter of $\pi_{k+2}$ gives palindrome $w_k$ ($|w_k| = f_k$); the $f_k + 1$ factors of $F_\infty$ of length $f_k$ are the $f_k$ cyclic shifts of $F_k$ plus $w_k$, partitioning all factors into disjoint singular layers and compressing the CDAWG/PAM of $F_k$ into $O(k)$ states!
     4. *Critical Exponent*: $F_\infty$ is 4th-power free with critical exponent $2 + \phi = \frac{5+\sqrt{5}}{2} \approx 3.618$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Substring, palindrome, and run counting on $F_\infty[1..n]$ ($n \le 10^{18}$): $O(\log n)$ time via Zeckendorf decomposition over singular word layers.
5. **Canonical Failure Modes & Counterexamples**:
   - Assuming $F_k = F_{k-1} F_{k-2}$ is a palindrome: $F_k$ is **never** a palindrome for $k \ge 3$; only its prefix $\pi_k$ of length $f_k - 2$ is a palindrome!
6. **Canonical Representative Problems**:
   - `W5B-04` (`AtCoder ABC 313 G`), `W5B-18` (`ICPC WF 2012 D — Fibonacci Words`), `W5B-31` (`[周任飞 2017]` Distinct Substrings, Palindromes & Runs in $F_\infty[1..n]$ for $n \le 10^{18}$).

---

### `T-5B-02`. Prouhet–Thue–Morse Word: Overlap-Freeness, Tarry–Escott & $\bmod 2^{64}$ Rolling-Hash Annihilation
1. **Multilingual Name**:
   - `[EN]`: Prouhet–Thue–Morse Word ($\mu(0)=01, \mu(1)=10$), Overlap-Freeness, Tarry–Escott Equal-Power-Sum Identity & $\bmod 2^{64}$ Rolling-Hash Annihilation
   - `[ZH]`: Thue–Morse 串（无重叠子串定理、Prouhet–Tarry–Escott 等幂和恒等式与 $\bmod 2^{64}$ 自然溢出哈希构造）
   - `[JA]`: Thue–Morse 語（Overlap-Free 定理・Prouhet–Tarry–Escott 等べき和・$\bmod 2^{64}$ ローリングハッシュ衝突構築）
2. **Diagnostic Signal**:
   - Constructing overlap-free / cube-free binary words, partitioning $[0, 2^k-1]$ into two sets with equal power sums $\sum_{n \in A_k} n^d = \sum_{n \in B_k} n^d$ for $0 \le d < k$, or hacking `uint64_t` polynomial rolling hashes.
3. **Core Combinatorial Word Invariant**:
   - **Thue's Overlap-Freeness (`Section 2.4.1`)**: $\mathbf{t}[n] = \text{popcount}(n) \bmod 2$ contains no overlap $c u c u c$ (even periods $p = 2q$ pull back via $\mu^{-1}$ to period $q$; odd periods force equal pairs `00`/`11` at both parities, whereas `00`/`11` only occur at odd indices in $\mathbf{t}$).
   - **Prouhet–Tarry–Escott Identity (`Section 2.4.2`)**: $\sum_{n=0}^{2^k-1} (-1)^{\mathbf{t}[n]} z^n = \prod_{j=0}^{k-1} (1 - z^{2^j})$ is divisible by $(1-z)^k$, so its first $k-1$ derivatives vanish at $z = 1$, forcing $\sum_{n \in A_k} P(n) = \sum_{n \in B_k} P(n)$ for every polynomial $\deg P \le k-1$.
   - **2-Adic Valuation of Rolling Hashes (`Section 2.4.3`)**: For any odd base $B$, $H(T_k) - H(\overline{T_k}) = (c_0 - c_1) \prod_{j=0}^{k-1} (B^{2^j} - 1)$ has 2-adic valuation $v_2 \ge 1 + \sum_{j=1}^{k-1} (j+1) = \frac{k(k+1)}{2}$. At $k = 11$ ($|T_{11}| = 2048$), $v_2 \ge 66 > 64$, annihilating $\bmod 2^{64}$ hashes for **every** odd base $B$!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - $O(2^k)$ generation ($k = 11 \implies 2048$ chars); $O(\log n)$ point lookup via `__builtin_parityll(n)`.
5. **Canonical Failure Modes & Counterexamples**:
   - Using `uint64_t` natural overflow rolling hashes in competitive programming without a prime modulus is deterministically defeated by $(T_{11}, \overline{T_{11}})$ of length $2048$.
6. **Canonical Representative Problems**:
   - `W5B-02` (Universal Anti-`uint64_t` Hash Construction), `W5B-11` (Tarry–Escott Equal-Power-Sum Partitioning via Thue–Morse), `W5B-22` (Overlap-Free & Cube-Free Morphic Constructions).

---

### `T-5B-03`. Pattern Counting in Iterated Morphisms $\varphi^k(S_0)$ & Recursive Strings (`CF 1466G`)
1. **Multilingual Name**:
   - `[EN]`: Pattern Counting in Iterated Morphisms $\varphi^k(S_0)$ ($k \le 10^{18}$) & Level-Promoted Recursive Strings (`CF 1466G`)
   - `[ZH]`: 迭代态射 $\varphi^k(S_0)$ 模式串计数（二元交界矩阵、KMP 同态矩阵与 `CF 1466G` 层级提升前缀和）
   - `[JA]`: 反復準同型写像 $\varphi^k(S_0)$ におけるパターン出現数え上げ（境界 2 文字遷移行列・KMP 準同型行列・`CF 1466G`）
2. **Diagnostic Signal**:
   - Counting occurrences of pattern $P[1..m]$ inside $W_k = \varphi^k(S_0)$ ($k \le 10^{18}$) or $s_k = s_{k-1} + t_k + s_{k-1}$ (`CF 1466G`, $\sum |P| \le 10^6$).
3. **Core Combinatorial Word Invariant**:
   - **Internal + Boundary-Window Decomposition (`Theorem 2.3`)**: Whenever $|A|, |B| \ge m - 1$, $\text{occ}(P, AB) = \text{occ}(P, A) + \text{occ}(P, B) + \text{occ}(P, \text{suff}_{m-1}(A) + \text{pref}_{m-1}(B))$.
   - **Three-Regime Compilation (`Section 2.5`)**:
     1. *Regime 1 (Expanding $\varphi$, $k \le 10^{18}$, $|P| \le 10^5$)*: Expand $k_0 = O(\log |P|)$ steps until $|\varphi^{k_0}(c)| \ge m - 1$ for all $c$; then occurrences in $\varphi^k(S_0)$ depend only on 1-letter factors $a$ and 2-letter factors $ab$ in $\varphi^{k-k_0}(S_0)$, counted via $(|\Sigma| + |\Sigma|^2)^3 \log k$ matrix exponentiation!
     2. *Regime 2 (Mortal/Unit-Growth Characters $|\varphi^k(b)| = 1$, $k \le 10^{18}$, $m \le 100$)*: Map each string $W$ to its $(m+1) \times (m+1)$ KMP transition-and-match matrix $M(W)$ and compute $M(\varphi^r(c)) = \prod_{x \in \varphi(c)} M(\varphi^{r-1}(x))$ in $O(|\Sigma| m \log k)$ via functional composition.
     3. *Regime 3 (`CF 1466G` Level Promotion $r_0$)*: Promote $s_0 \to s_{r_0}$ until $|s_{r_0}| \ge |P|$; for all $r > r_0$, $\text{suff}_{m-1}(s_{r-1}) = U$ and $\text{pref}_{m-1}(s_{r-1}) = V$ freeze, reducing $\sum_{r=r_0+1}^k 2^{k-r} \text{occ}(P, U + t_r + V)$ to $O(|P| + |\Sigma|)$ via precomputed $2^{-r}$ prefix sums!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Regime 1: $O(|\Sigma|^6 \log k + |\Sigma|^2 |P|)$; Regime 2: $O(|\Sigma| |P| \log k)$; Regime 3: $O(|P| + |\Sigma|)$ per query.
5. **Canonical Failure Modes & Counterexamples**:
   - **Unit-Growth Character Trap in Regime 1**: If $\varphi(a) = ab, \varphi(b) = b$, then $|\varphi^k(b)| = 1$ forever, so $P$ can span arbitrarily many `'b'` blocks; Regime 1 fails and Regime 2 (KMP functional composition) is mandatory.
   - **$|P| = 1$ Empty-Junction Window**: When $m = 1$, $\text{suff}_0(A) + c + \text{pref}_0(B) = c$ has length $1$, not $0$.
6. **Canonical Representative Problems**:
   - `W5B-06` (`CF 1466G — Song of the Sirens`), `W5B-18` (`ICPC WF 2012 D`), `W5B-27` (Pattern Counting in Iterated Morphisms for $k \le 10^{18}$).

---

### `T-5B-04`. Free Group / Coxeter Stack Reduction, Non-Abelian $GL_2(\mathbb{F}_p) / SL_2(\mathbb{F}_p)$ Matrix Hashing & Stack-Trie Path Isomorphism
1. **Multilingual Name**:
   - `[EN]`: Free Group / Universal Coxeter Stack Reduction, Non-Abelian $GL_2(\mathbb{F}_p) / SL_2(\mathbb{F}_p)$ Matrix Hashing, Height-Indexed Dyck Hashing & Stack-Trie Path Isomorphism
   - `[ZH]`: 自由群/Coxeter 栈消除、非交换 $GL_2(\mathbb{F}_p)/SL_2(\mathbb{F}_p)$ 矩阵哈希、带高度索引的 Dyck 括号哈希与栈字典树 (`Stack-Trie`) 路径同构定理
   - `[JA]`: 自由群・スタック簡約・非可換行列ハッシュ ($GL_2(\mathbb{F}_p)/SL_2(\mathbb{F}_p)$) とスタック木 (`Stack-Trie`) パス同型定理
2. **Diagnostic Signal**:
   - Testing whether $S[l..r]$ reduces to $\varepsilon$ under `cc` $\to \varepsilon$ (`CF 1223F`) or directed brackets `()` $\to \varepsilon$, maintaining stack-reduced strings under dynamic point updates / range swaps on a Segment Tree, or computing $\text{LCE}$ / lexicographical order of stack-reduced substrings $\text{red}(S[l_1..r_1])$ vs. $\text{red}(S[l_2..r_2])$.
3. **Core Combinatorial Word Invariant**:
   - **Stack-Trie Path Isomorphism Theorem (`Theorem 3.1.2`)**: Walking prefixes $i = 1..n$ on a rooted **Stack Trie** $\mathcal{T}$ (stepping to `parent(u)` if the top edge cancels $S[i]$, else descending to child `ch[u][S[i]]`), the reduced form $\text{red}(S[l..r]) = P_{l-1}^{-1} P_r$ is **literally the sequence of edge labels along the unique simple tree path $u_{l-1} \leadsto \text{LCA}_{\mathcal{T}}(u_{l-1}, u_r) \leadsto u_r$ in $\mathcal{T}$**!
     - Because a simple path in a tree never backtracks, no further cancellations can occur across $\text{LCA}_{\mathcal{T}}(u_{l-1}, u_r)$, reducing $|\text{red}(S[l..r])|$ to $\text{dist}_{\mathcal{T}}(u_{l-1}, u_r)$ and reducing lexicographical comparison of $\text{red}(S[l_1..r_1])$ vs. $\text{red}(S[l_2..r_2])$ to **$O(\log N)$ Tree-Path LCE** — **100% deterministically with zero matrices**!
   - **Non-Abelian $GL_2(\mathbb{F}_p) / SL_2(\mathbb{F}_p)$ Matrix Embeddings (`Section 3.2`)**:
     - *Symmetric `cc` $\to \varepsilon$*: By Cayley–Hamilton ($M^2 - \text{tr}(M)M + \det(M)I_2 = 0$), any $M_c \in GL_2(\mathbb{F}_p)$ with $\text{tr}(M_c) = 0$ and $\det(M_c) = -1$ ($M_c = \begin{pmatrix} a_c & b_c \\ (1-a_c^2)b_c^{-1} & -a_c \end{pmatrix}$) satisfies **$M_c^2 = I_2$ identically** while remaining non-abelian!
     - *Directed Dyck Words*: Index random $SL_2(\mathbb{F}_p)$ generators by **both character type $c$ and 1D balance height $d = \text{bal}[i]$** ($M_{(c, d)}$ for open, $M_{(c, d)}^{-1}$ for close) alongside $\min_{k=l}^r \text{bal}[k] \ge \text{bal}[l-1]$ and $\text{bal}[r] = \text{bal}[l-1]$.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Static queries (`CF 1223F`, Stack-Trie LCE): $O(N \log |\Sigma|)$ or $O(N)$ pointer-swapped `next_match[i]` DP; Dynamic updates: $O(\log N)$ Segment Tree of $2 \times 2$ matrices ($8$ multiplications per merge).
5. **Canonical Failure Modes & Counterexamples**:
   - **Why Un-Indexed $SL_2(\mathbb{F}_p)$ + 1D Balance Fails on `(( )( ))` (`Pitfall 1`)**: On `(( )( ))`, the 1D balance is $[1, 2, 1, 2, 1, 0] \ge 0$ everywhere, yet if only one bracket type exists (or outer brackets are `(` and inner are `) (`), un-indexed group multiplication cancels the inner `) (`! Indexing generators by $(c, \text{bal}[i])$ prevents a closing bracket at depth $d$ from cancelling an opening bracket at depth $d+1$.
6. **Canonical Representative Problems**:
   - `W5B-01` (`CF 1223F — Stack Exterminable Arrays`), `W5B-15` (Dynamic Point-Update Range Dyck / Stack Reduction via $SL_2(\mathbb{F}_p)$ Segment Tree), `W5B-42` (Lexicographical Comparison of Stack-Reduced Substrings via Stack-Trie Path LCE).

---

### `T-5B-05`. Kempa–Prezza String Attractors $\gamma(S)$ & Kempa–Kociumaka $\tau$-Synchronizing Sets
1. **Multilingual Name**:
   - `[EN]`: String Attractors ($\gamma(S)$ — Kempa & Prezza, STOC 2018) & $\tau$-Synchronizing Sets (Kempa & Kociumaka, STOC 2019)
   - `[ZH]`: 字符串吸引子 ($\gamma(S)$ 最小唯一代表元对偶) 与 $\tau$-同步集 (`$\tau$-Synchronizing Sets`)
   - `[JA]`: 文字列アトラクター (`String Attractor` $\gamma(S)$) と $\tau$-同期集合 (`$\tau$-Synchronizing Set`)
2. **Diagnostic Signal**:
   - Finding a minimum-size index subset $\Gamma \subseteq [1, n]$ intersecting at least one occurrence of every distinct substring of $S$, bounding dictionary compression measures ($\gamma \le \min(z_{\text{LZ77}}, r_{\text{BWT}}, g_{\text{SLP}})$), or building flat $O(n/\tau)$-anchor LCE structures.
3. **Core Combinatorial Word Invariant**:
   - **SAM Minimal-Unique Representative Hitting-Set Duality (`Section 4.1`)**: Because any occurrence interval covering a shorter factor $u$ automatically covers every superstring $v$ containing that occurrence, $\Gamma \subseteq [1, n]$ is a string attractor of $S$ **iff** $\Gamma$ intersects at least one occurrence interval of length $\text{minlen}(q) = \text{len}(\text{link}(q)) + 1$ for every SAM state $q$!
   - **$\tau$-Synchronizing Set Minimizer Rule (`Section 4.2`)**: Excluding regions of local period $\le \tau/3$ and selecting $i \in \mathsf{S}$ iff $\arg\min_{k \in [i, i+\tau]} \text{id}(S[k..k+\tau-1]) \in \{i, i+\tau\}$ produces a locally consistent set of size $O(n/\tau)$ hitting every aperiodic length-$\tau$ window.
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Exact minimum attractor on trees/small alphabets or interval-hitting reductions via SAM $\text{minlen}(q)$ intervals; $\tau$-synchronizing set construction in $O(n)$ time.
5. **Canonical Failure Modes & Counterexamples**:
   - Enforcing coverage on $\text{maxlen}(q) = \text{len}(q)$ instead of $\text{minlen}(q)$ in SAM: covering $\text{len}(q)$ does **not** guarantee covering the shorter substrings in $q$'s equivalence class!
6. **Canonical Representative Problems**:
   - `W5B-45` (Minimum String Attractor Verification & SAM `minlen` Hitting Set), `W5B-46` ($\tau$-Synchronizing Set Anchor LCE).

---

### `T-5B-06`. Parent-Distance Cartesian-Tree Matching & $1/z$ Weighted Suffix Trees (PWM)
1. **Multilingual Name**:
   - `[EN]`: Parent-Distance Cartesian-Tree Pattern Matching & $1/z$ Heavy-String Decomposition for Weighted Strings (PWM)
   - `[ZH]`: 父距离编码笛卡尔树模式匹配 (`Cartesian-Tree KMP`) 与 $1/z$ 加权后缀树重路径分解
   - `[JA]`: 親距離符号化による Cartesian Tree マッチングと重み付き文字列の $1/z$ 接尾辞木分解
2. **Diagnostic Signal**:
   - Finding substrings $T[i..i+m-1]$ sharing the same min-heap Cartesian tree shape as $P[1..m]$ in $O(n+m)$ time, or indexing a position-weight matrix $\pi_i(c)$ for solid patterns with probability $\prod \pi_{i+j-1}(P[j]) \ge 1/z$.
3. **Core Combinatorial Word Invariant**:
   - **Parent-Distance Bijection (`Section 4.3`)**: Two arrays have identical Cartesian trees iff their left-parent distances $\text{PD}_S[j] = j - \max\{k < j : S[k] \le S[j]\}$ ($0$ if none) are identical at every index $j \in [1, m]$, tested in $O(1)$ per KMP transition via window clipping $\text{PD}_T[j] \cdot [\text{PD}_T[j] \le q] = \text{PD}_P[q+1]$.
   - **Disjoint-Event Probability Sum Bound (`Section 4.4` — Barton et al. STOC 2016)**: Divergent solid continuations from any prefix are disjoint events in $\Sigma^n$, so their probabilities sum to $\le 1$; hence **at most $\lfloor z \rfloor$ branches** can have probability $\ge 1/z$, decomposing the weighted string into $\lfloor z \rfloor$ deterministic heavy strings of total length $O(nz)$!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - Cartesian-Tree KMP: $O(n + m)$ time via monotonic deque + KMP; Weighted Suffix Tree: $O(nz)$ time and space.
5. **Canonical Failure Modes & Counterexamples**:
   - Using strict inequality $S[k] < S[j]$ on both sides when duplicate values occur: tie-breaking must be consistent (`<=` on left, `<` on right).
6. **Canonical Representative Problems**:
   - `W5B-47` ($1/z$ Weighted String Indexing & Pattern Matching), `W5B-48` ($O(n+m)$ Cartesian-Tree Pattern Matching).

---

### `T-5B-07`. Two-Dimensional Periodicity Lattices, Baker–Bird & Vishkin's 2D Witness Duel
1. **Multilingual Name**:
   - `[EN]`: Two-Dimensional Periodicity Lattices, Baker–Bird 2D Automaton Matching & Vishkin's 2D Witness Duel
   - `[ZH]`: 二维周期格分类、Baker–Bird 二维 AC+KMP 匹配与 Vishkin 二维证人决斗算法 (`2D Duel`)
   - `[JA]`: 二次元周期格子・Baker–Bird 法と Vishkin の二次元 Witness Duel
2. **Diagnostic Signal**:
   - 2D pattern matching of an $r \times c$ matrix $P$ inside an $R \times C$ matrix $T$, or classifying 2D periodic symmetries of a grid.
3. **Core Combinatorial Word Invariant**:
   - **Baker–Bird Row-ID Factoring**: Replace each row of $P$ with its unique Aho–Corasick terminal state ID $id_1 \dots id_r$, run the AC automaton horizontally across every row of $T$, and run 1D KMP on $id_1 \dots id_r$ down each column of $T$ in $O(RC)$ time!
   - **Vishkin's 2D Duel (`Section 4.5`)**: For any displacement $(\Delta r, \Delta c)$ that is not a 2D period of $P$, precompute a **witness cell** $\text{Wit}[\Delta r][\Delta c] = (r^*, c^*)$ where $P[r^*][c^*] \ne P[r^* - \Delta r][c^* - \Delta c]$. Inspecting $T[i + r^*][j + c^*]$ kills at least one of the two overlapping candidates $(i, j)$ and $(i - \Delta r, j - \Delta c)$ in **$O(1)$ time**!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - $O(RC + rc)$ time and $O(RC)$ space.
5. **Canonical Failure Modes & Counterexamples**:
   - Treating duplicate rows of $P$ as distinct IDs in vertical KMP fails; identical rows of $P$ must share the **exact same AC terminal ID**.
6. **Canonical Representative Problems**:
   - `W5B-49` (Baker–Bird 2D Pattern Matching & Vishkin 2D Periodicity Duel).

---

### `T-5B-08`. LZ77 / SLP Primary–Secondary Occurrence Split & 2D Orthogonal Range Indexing
1. **Multilingual Name**:
   - `[EN]`: LZ77 / SLP Compressed Indexing via Kärkkäinen–Ukkonen Primary–Secondary Split & Wavelet-Tree 2D Range Queries
   - `[ZH]`: LZ77 / 文法压缩索引（主次出现分解 `Primary/Secondary Split` 与二维正交矩形小波树查询）
   - `[JA]`: LZ77 / SLP 圧縮全文索引（一次・二次出現分解と Wavelet Tree 二次元直交領域探索）
2. **Diagnostic Signal**:
   - Counting or locating occurrences of a pattern $P[1..m]$ inside an LZ77-parsed text $T = Z_1 Z_2 \dots Z_z$ ($z \le 10^5, |T| \le 10^{18}$) in $O(m \log z + \text{occ})$ time.
3. **Core Combinatorial Word Invariant**:
   - **Primary vs. Secondary Occurrence Dichotomy (`Section 4.6`)**: Every occurrence of $P$ is either **primary** (straddling at least one phrase boundary $Z_k \mid Z_{k+1}$) or **secondary** (strictly inside a phrase $Z_k$, copied from an earlier source interval).
   - **2D Grid Bijection**: Sort the $z-1$ reversed left prefixes $\overleftarrow{Z_1 \dots Z_k}$ ($X$-rank) and $z-1$ right suffixes $Z_{k+1} \dots Z_z$ ($Y$-rank). Each of the $m-1$ split points $P = P[1..j] \cdot P[j+1..m]$ defines a 1D prefix range $[x_1, x_2]$ and 1D suffix range $[y_1, y_2]$, so primary occurrences of $P$ with leftmost phrase split at $j$ correspond bijectively to points in $[x_1, x_2] \times [y_1, y_2]$!
4. **Algorithmic / Data-Structure Compilation & Complexity**:
   - $O(z \log z)$ Wavelet Tree build; $O(m \log z + \text{occ})$ query time.
5. **Canonical Failure Modes & Counterexamples**:
   - Double-counting a primary occurrence that crosses **multiple** phrase boundaries $Z_k \mid Z_{k+1} \mid Z_{k+2}$: restrict the left piece $P[1..j]$ to fit **strictly inside the single phrase $Z_k$** ($j \le |Z_k|$) so each primary occurrence is counted at its **first** crossed boundary!
6. **Canonical Representative Problems**:
   - `W5B-50` (LZ77 / SLP Primary–Secondary 2D Range Pattern Indexing).

---

## 11. Global Diagnostic Decision Matrix ("Contest Symptom $\to$ Word Invariant $\to$ Engine")

Use this lookup matrix during a contest or research audit to route any string problem statement directly to its exact structural invariant and technique ID:

| # | Contest Symptom / Query & Constraint Profile | Underlying Combinatorial Word Invariant | Primary Engine & Technique ID |
| :--- | :--- | :--- | :--- |
| **1** | Count/optimize partitions of $S$ where transition lengths are **all borders** of $S[1..i]$ ($N \le 5 \cdot 10^5$) | Borders of $S[1..i]$ partition into $\le \log_2 i$ arithmetic progressions; shifting $i-1 \to i$ reuses $\text{anc}(u)$ | Border AP + `slink` DP (`T-1A-02`, `T-1A-03`) |
| **2** | Test if $L \le 10^{18}$ is realizable by concatenating periods of $S$ (`[WC2016] 论战捆竹竿`) | Period transitions per border AP $(a, d, k)$ form bounded knapsack items modulo $a_1$ | Residue-Class Monotonic Queue (`T-1A-02`) |
| **3** | Maintain KMP border weights while characters $S[i]$ and upper bounds $W[i]$ arrive online (`CF 1286E`) | Surviving borders only shrink; each deleted border adds $O(1)$ amortized work; `slink` skips equal chars | KMP `slink` Active-Set Deletion (`T-1A-04`) |
| **4** | Compare $S[1..i] + T$ vs. $S[1..j] + T$ for arbitrary right-extensions $T$ (`[ZJOI2017] 字符串`) | Candidate minimal suffixes double in length; if $\|u\| < \|v\| < 2\|u\|$, $u$ is a border of $v$ and one dominates | Significant Suffixes ($\le \log_2 N$) (`T-1B-04`) |
| **5** | Find lexicographically smallest/largest suffix of $S[l..r]$ in $O(\log N)$ or $O(1)$ | Max suffix is the first complete Lyndon factor inside $[l, r]$; min suffix lies in $\Lambda(S[1..r])$ of size $\le \log_2 r$ | Duval / Lyndon Tree / Significant Suffixes (`T-1B-01..05`) |
| **6** | Enumerate all squares, $k$-powers, or periodic substrings in $S[l..r]$ ($N \le 5 \cdot 10^5$) | Every maximal run $R = [l, r, p]$ has a unique Lyndon root under $<$ or $>$ ($\#\text{Runs} < N, \sum e < 3N$) | Lyndon-Root Runs + 2D Sweep (`T-1B-06`) |
| **7** | Count distinct substrings or multi-string occurrences on a Trie (`[ZJOI2015]`, `CF 616F`) | $\text{endpos}$ equivalence classes nest into a tree of $\le 2N-1$ states; BFS avoids zero-length clones | SAM / Safe Trie GSAM (`T-2A-01`) |
| **8** | Query occurrences of $S[p_l..p_r]$ inside $S[a..b]$ or optimal repeat in $S[a..b]$ (`CF 666E`, `CF 700E`) | $w$ occurs in $S[a..b] \iff \text{endpos}(u) \cap [a+\|w\|-1, b] \ne \emptyset$; optimal chain needs only 1 witness `pos[u]` | SAM + Persistent SegTree Merge (`T-2A-02`, `T-2A-03`) |
| **9** | Online range $[l, r]$ distinct substrings (or polynomial length sums) (`Luogu P6292`) | Solid LCT chains sharing last-endpos color $p_{\text{old}}$ have gapless start-position intervals | SAM + LCT `access` Color Sweep (`T-2A-04`) |
| **10** | Build a graph / 2-SAT over substrings $A_i, B_j$ with prefix/suffix edges (`[十二省联考 2019]`) | On $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$, $B_j$ is a prefix of $A_i$ iff ancestor OR same node with $\|B_j\| \le \|A_i\|$ | Intra-State Length Stratification (`T-2A-05`) |
| **11** | Linear-time suffix sorting ($N \le 10^7$) or counting strings with a given SA descent set (`AGC 060 D`) | $\text{type}(i) = L \iff \text{rk}[i] > \text{rk}[i+1]$; LMS-substrings are prefix-free under $(S[\cdot], \text{type})$ | Induced Sorting (`SA-IS`) (`T-2B-01`) |
| **12** | Sum $f(\text{LCP}(u, v))$ over query subsets of substrings $U_1 \dots U_k$ (`CF 1073G`, `[AHOI2013]`) | Min-Cartesian tree of adjacent LCEs $h_2 \dots h_k$ is isomorphic to the Virtual Suffix Tree | Zero-Tree Virtual Suffix Tree (`T-2B-02`) |
| **13** | Range $[l, r]$ optimal pair $a, b \in [l, r]$ maximizing $g(\text{LCP}(a, b), a, b)$ | Predecessor/successor pairs $(i^-, i), (i, i^+)$ in DSU-on-Tree dominate all $\binom{N}{2}$ pairs ($\le 2N\log_2 N$) | Suffix Tree Dominant Pairs (`T-2B-03`) |
| **14** | Longest border or shortest period of $S[l..r]$, or internal occurrences of $P$ in $T$ (`[BJWC2018]`) | Occurrences of $P$ in $T$ ($\|T\| < 2\|P\|$) form a single AP; dyadic $2^m$ prefix+suffix APs cover all borders | Bounded-Ratio IPM / 6-Method Borders (`T-2B-04`) |
| **15** | Online encrypted `push_front(c)` / `pop_front()` with suffix rank & LCP queries (`[BZOJ 3682]`) | 64-bit Scapegoat midpoint tags give $O(1)$ order; BST adjacent `height` RMQ gives $O(\log N)$ hash-free LCP | Suffix Balanced Tree (`后缀平衡树`) (`T-2B-06`) |
| **16** | Persistent / Tree-branched palindrome extension or 4-way deque `push/pop_front/back` | All nodes in a `slink` AP share the same preceding char; popping at $R$ promotes `fail(u)` to `max_pref[l_u]` | Deterministic / 4-Way Deque PAM (`T-3A-01`, `T-3A-02`) |
| **17** | Online $O(1)$ Range Longest Palindromic Substring (`Range LPS`) in $S[l..r]$ | Every Manacher center $c \in (c_L, c_R)$ strictly between the boundary-touching centers is unclipped! | Two-Boundary Unclipping + $O(1)$ RMQ (`T-3A-03`) |
| **18** | Range $[l, r]$ distinct palindromes (`LOJ 6071`) | Along a `slink` chain, $\text{start}_{r-1}(u_j) = \text{start}_r(u_{j-1})$ telescopes to 2 Fenwick updates | PAM `slink` Telescoping + Fenwick (`T-3A-04`) |
| **19** | Wildcard matching ($N \le 5 \cdot 10^5$) or involution/permutation matching (`CF 528D`, `CF 1334G`) | Indicator penalty $\le M(\|\Sigma\|-1)^2 < 998244353$ fits in 1 NTT; $\pi^2=\text{id}$ collapses to $O(N)$ KMP | 1-NTT Indicator / Kalai / 3-in-2 FFT (`T-3B-01`, `T-3B-02`) |
| **20** | $k$-mismatch or $k$-edit matching ($k$ small vs. $k$ moderate) | $k$ mismatches = $k+1$ LCE kangaroo hops; $\text{per}(P) \le 2k$ compresses via 2nd-order difference `diff_p` | Kangaroo LCE / $2k$-Period Dichotomy (`T-3B-03`) |
| **21** | Parameterized, Order-Preserving, or Cartesian-Tree pattern matching | Clipping relative backward offsets $\text{prev}_T[i] \cdot [\text{prev}_T[i] \le q]$ restores prefix monotonicity | Window-Clipped Structural KMP (`T-3B-04`, `T-5B-06`) |
| **22** | Dynamic string cut/paste/reverse on $\|S\| \le 10^{18}$ with $O(\log N)$ LCE or SLP pattern matching | Alternating RLE + Cole–Vishkin 6-coloring / Jeż recompression modifies $O(1)$ blocks per level | Locally Consistent Parsing (`SLP`) (`T-3B-05`) |
| **23** | Count strings avoiding $m$ long patterns $P_1 \dots P_m$, or exact $k$ occurrences, or $\mathbb{E}[\text{occ}^K]$ for $n \le 10^{18}$ | Overlap polynomial $C_{i,j}(x)$ compresses AC states to $m \times m$; $t = 1 + u$ collapses denominator to $(1-\sigma x)^{j+1}$ | Goulden–Jackson + $t=1+u$ Shift (`T-4A-01..03`) |
| **24** | Expected waiting time $\mathbb{E}[T_S]$, variance, or winning probabilities in a pattern race (`[SDOI2017]`) | Fair-betting casino gamblers along borders accumulate terminal payoff $\Omega_{P_i, P_j}$ | Conway's Casino Martingale PGF (`T-4A-04`) |
| **25** | Count outer strings $T \in \Sigma^n$ with $\text{LCS}(S, T) = k$ ($\|S\| \le 20$) or online AC inserts/deletes (`CF 710F`) | Horizontal LCS differences $\Delta_i \in \{0, 1\}$ form a $2^{\|S\|}$-state DFA updated in 4 bitwise ops | `DP套DP` Compiler / Binary-Grouped AC (`T-4A-05`, `T-4B-05`) |
| **26** | Shortest (un)common substring/subsequence (`[HEOI2015]`) or range $[l, r]$ shortest absent subsequence | Leftmost-greedy $\text{DASG}(S)$; Hébrard arch factorization $\iota(S)$ lifted via `jump[k][l]` | Four-Comb Product / Arch Factorization (`T-4B-01`, `T-4B-02`) |
| **27** | Range $[l, r]$ distinct subsequences in $O(\|\Sigma\|)$ time without segment trees | Rank-1 transition $M_c = I + \mathbf{e}_c \mathbf{1}^T$ has $\det = 1$ and $O(1)$-sparse inverse $\mathbf{u}_r^T \cdot \mathbf{v}_{l-1}$ | Invertible Subsequence Matrices (`T-4B-03`) |
| **28** | All-substring LCS $\text{LCS}(A, B[l..r])$ or Range LIS $\text{LIS}(B[l..r])$ ($N, Q \le 10^5$) | Planar uncrossing permutation $W[k]$ encodes all semi-local LCS via 2D dominance; Unit-Monge $\boxdot$ in $O(K\log K)$ | Tiskin's Seaweed Matrices (`海草矩阵`) (`T-4B-04`) |
| **29** | Bulk substring/palindrome equations on $S[1..N]$ (`[SCOI2016]`) or on tree paths $u \rightsquigarrow v$ | Overlapping $2^k$ blocks cover $[l, r]$ losslessly; root self-palindrome bit `is_pal[k][r]` preserves $B_k(r)=B_k(r)^R$ | Signed / Tree Binary-Lifting DSU (`T-5A-01`, `T-5A-02`) |
| **30** | Reconstruct/count strings from SA (`CF 1526E`), $k$-mer spectrum (`ABC 336 G`), or RLBWT ($N \le 10^{18}$) | SA adjacency $\text{rk}[u+1] > \text{rk}[v+1] \implies S[u] < S[v]$; BEST theorem $\det L_{\text{out}}^{(r)}$; $O(1)$ Move Structure | SA Adjacency / BEST / RLBWT (`T-5A-03..05`) |
| **31** | Sort upward tree paths (`Luogu P5353`), count path strings with $\le 20$ leaves (`[ZJOI2015]`), or all-pairs tree path occurrences (`[CTSC2010]`) | Dual-rank $(\text{rk}_k, \text{id}_k)$ prevents false tie-splitting; leaf-rooted cover; centroid $\sqrt{M}$ dual-SAM split | Dual-Rank Tree SA / Tree GSAM / Centroid SAM (`T-5A-06`) |
| **32** | Queries on Fibonacci / mechanical words ($n \le 10^{18}$), $\varphi^k(S_0)$, or range stack/Dyck reduction (`CF 1223F`) | Rytter's singular words $w_k$; 2-letter junction matrix; trace-zero $\det=-1$ $GL_2(\mathbb{F}_p)$ & Stack-Trie path $\text{LCA}$ | Singular Words / Morphic Matrix / $SL_2(\mathbb{F}_p)$ (`T-5B-01..04`) |

---

## 12. Post-Research Curriculum Restructuring Recommendation for Phase 1.5 (`CURRICULUM_ARCHITECTURE.md`)

Based on the depth, problem density (430+ unique accepted non-template problems), and new frontier paradigms uncovered across the 115-iteration discovery corpus, the initial 24-chapter outline in `PLAN.md` §3 should be restructured in `strings_research/CURRICULUM_ARCHITECTURE.md` via **five high-impact architectural splits and upgrades**:

1. **Upgrade Part II (`Ch 08`: Runs) with Lyndon-Tree Dominance & 6-Method Internal Borders**:
   - Pair Bannai et al.'s Runs Theorem (`T-1B-06`) directly with Kociumaka's Bounded-Ratio IPM and the **6 Canonical Methods for `[BJWC2018] Border 的四种求法`** (`T-2B-04`) across Part II (`Ch 08`) and Part IV (`Ch 14`), explicitly contrasting Runs-based long border lookup ($b \ge |W|/2$) against dyadic IPM and SAM Link-Tree HLD/Centroid decompositions.
2. **Split & Expand Part III (`Ch 10`–`Ch 12`) to Give Dominant Pairs, Virtual Suffix Trees, SCDAWG & Suffix Balanced Trees Dedicated Sections**:
   - **Chapter 11** (`SAM + LCT & Substring Graph Constructions`) should house both LCT `access` color-chain sweeping (`T-2A-04`) and Intra-State Length Stratification (`[十二省联考 2019]`, `T-2A-05`).
   - **Chapter 12** (`SA-IS, Virtual Suffix Trees, Dominant Pairs & Bi-Directional Suffix Structures`) must explicitly separate: (a) Induced Sorting (`SA-IS`) + Fischer's Induced LCP + `rk`-Descent Duality (`AGC 060 D`), (b) Zero-Tree Virtual Suffix Trees + **Suffix Tree Dominant Pairs (`启发式合并支配对`, `T-2B-03`)**, and (c) Bi-directional **SCDAWG** + **Hash-Free Suffix Balanced Trees (`后缀平衡树`, `T-2B-06`)**.
3. **Elevate Locally Consistent Parsing (`SLP` / Jeż Recompression) & $O(1)$ Range Palindromes in Part IV (`Ch 13`–`Ch 16`)**:
   - **Chapter 13** (`Dynamic Strings, Locally Consistent Parsing & Compressed Indexing`) should unify Cole–Vishkin 6-coloring, randomized local extrema, and **Jeż's Recompression (`T-3B-05`)** with **Kempa–Prezza String Attractors $\gamma(S)$, $\tau$-Synchronizing Sets (`T-5B-05`)**, and **LZ77/SLP 2D Orthogonal Range Indexing (`T-5B-08`)**.
   - **Chapter 15** (`Deque PAM, Persistent Tree PAM & Online Range Palindromes`) must feature the **True $O(1)$ Online Range LPS via Two-Boundary Unclipping (`T-3A-03`)**, the 4-way Deque PAM lazy surface push-down (`T-3A-02`), and `[徐毅 2014]` `slink` periodic telescoping (`T-3A-04`).
   - **Chapter 16** (`FFT/NTT Wildcards, $k$-Mismatch & Structural Isomorphism Matching`) must integrate **1-NTT Degree-Reduced Indicator matching, Kalai's Randomized Projection, 3-in-2 Complex FFT (`T-3B-01`)**, the `CF 1334G` 4-method hierarchy (`T-3B-02`), Clifford–Gawrychowski–Uznański $O(N\sqrt{k\log k})$ $2k$-period dichotomy (`T-3B-03`), and **Window-Clipped Structural KMP (`p-KMP`, `Order-KMP`, `Cartesian-KMP`, `p-SA`, `T-3B-04`, `T-5B-06`)**.
4. **Refocus Part V (`Ch 17`–`Ch 20`) on Algebraic & Semigroup String Engines**:
   - **Chapter 17** (`Goulden–Jackson, Bivariate $(t-1)$ Cluster GFs, the $t=1+u$ Moment Shift & Conway's Casino PGFs`) must showcase the **`Universal Cup / QOJ` $t = 1 + u$ Binomial Moment Shift (`T-4A-03`)**, Embedded Substring Weight Absorption (`T-4A-02`), and Division-Free Pattern Races with Seed Prefixes (`T-4A-04`).
   - **Chapter 19** (`Subsequence Automata, Arch Factorization, Simon's Congruence & Matrix-Free Invertible Transitions`) and **Chapter 20** (`Tiskin's Seaweed Matrices, $O(K\log K)$ Unit-Monge $\boxdot$, $O(N\log^2 N)$ Range LIS & Bit-Parallel Alignment`) form a cohesive two-chapter subsequence suite.
5. **Expand Part VI (`Ch 21`–`Ch 24`) to Cover Tree Binary-Lifting DSU, Wheeler/RLBWT Move Structures, Singular Words & Stack-Trie Path Isomorphism**:
   - **Chapter 21**: Word Equations, Signed & **Tree Binary-Lifting DSU (`T-5A-01`, `T-5A-02`)**, String Inequality Digraphs, SA Adjacency (`T-5A-03`), and Inverse Reconstruction (`T-3A-06`).
   - **Chapter 22**: De Bruijn Graphs, AC-DFA BEST Theorem (`T-5A-04`), BWT / Bijective BWT, **Wheeler Graphs & $O(1)$ RLBWT Move Structures (`T-5A-05`)**, and Strings on Trees (`Dual-Rank Tree SA`, `Leaf-Rooted Tree GSAM`, `[CTSC2010] 珠宝商` with child-subtree thresholding, `T-5A-06`).
   - **Chapter 23**: Free Group / Coxeter Word Reduction, Non-Abelian **$GL_2(\mathbb{F}_p) / SL_2(\mathbb{F}_p)$ Matrix Hashing**, Height-Indexed Dyck Hashing, and **Deterministic Stack-Trie Path Isomorphism (`T-5B-04`)**.
   - **Chapter 24**: Combinatorics on Words — **Sturmian 6-Way Equivalence, Fibonacci & Rytter's Singular Words (`[周任飞 2017]`, `T-5B-01`)**, Thue–Morse Overlap-Freeness / Tarry–Escott / Anti-Hash (`T-5B-02`), Iterated Morphisms $\varphi^k(S_0)$ (`T-5B-03`), $1/z$ Weighted Suffix Trees (`T-5B-06`), and 2D Periodicity Lattices (`T-5B-07`).
