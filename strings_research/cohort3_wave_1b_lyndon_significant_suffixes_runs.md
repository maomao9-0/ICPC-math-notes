# Wave 1B Reconciled Master Treatise & Problem Archive (Cohort 3, Iteration 106)
## Lyndon Words, Duval's Algorithm, Significant Suffixes (`显著后缀`), Lyndon Trees & The Runs Theorem (`极长周期子串`)

> [!IMPORTANT]
> **Cohort 3 Cross-Comparison, Blind-Spot Audit & Reconciled Wave 1B Master Document (`cohort3_wave_1b_lyndon_significant_suffixes_runs.md`)**
> This document is the **Cohort 3 (Iteration 106)** reconciled master synthesis of:
> - **Cohort 1 (Iterations 06–10)**: `strings_research/iter_06_to_10_lyndon_significant_suffixes_runs.md` (991 lines, 32 accepted problems, 8 quarantined templates)
> - **Cohort 2 (Iterations 58–62)**: `strings_research/cohort2_iter_58_to_62_lyndon_significant_suffixes_runs.md` (1100 lines, 32 accepted problems, 9 quarantined templates)
>
> All proofs, counterexamples, algorithmic kernels, frontier extensions, and the deduplicated union of **42 accepted non-template problems (`W1B-01`–`W1B-42`)** and **10 quarantined template problems (`R-1B-01`–`R-1B-10`)** strictly enforce the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard** defined in `strings_research/PLAN.md`.

---

## Section 1. Cross-Cohort Comparison & Blind-Spot Audit (Cohort 1 vs. Cohort 2)

### 1.1 High-Level Quantitative & Structural Comparison

| Audit Dimension | Cohort 1 (`iter_06_to_10`) | Cohort 2 (`cohort2_iter_58_to_62`) | Cohort 3 Reconciled Master (`cohort3_wave_1b`) |
| :--- | :--- | :--- | :--- |
| **Lyndon Equivalence & CFL Theory** | 4-way equivalence ($1 \iff 2 \iff 3 \iff 4$); Duval potential $\Phi = 2i + k$; all-prefix CFL recurrence via $r \to r - d\cdot p$ | 3-way equivalence + Witt's Necklace/Lyndon formula + FKM $O(1)$ amortized generation; phase-bound $< 2N$ comparisons | **Unified 4-Way Proof + Witt/FKM + All-Prefix State Sharing + RLE & Bijective BWT** |
| **Significant Suffixes (`显著后缀`)** | Tandem decomposition $v = w^2 u', u = wu'$; counterexample $S = \texttt{aaba}$ for $\text{Cand}_{\min}(S[l..r]) \not\subseteq \text{Cand}_{\min}(S[1..r])$; block-hash $O(1)$ LCE | Two-way strict monotonicity $\min(u'T, vT) < uT < \max(u'T, vT)$; **Segment Tree `pushup` 1-Survivor Theorem** ($O(N)$ build); static shortest-border reduction | **Unified Doubling + 1-Survivor Proof + $O(\log N)$ Dyadic Band RMQ without Segment Trees** |
| **Lyndon Array & Lyndon Tree** | Monotonic stack on $\text{rk}$; right-child right-maximality proof | Explicit Min-Cartesian Tree isomorphism on $\text{rk}[2..n+1]$ with $-1$ left shift; counterexample $S = \texttt{bab}$ for negating $\text{rk}_<$ | **Complete Cartesian Isomorphism + Exact $(>, -\infty)$ Comparator + Persistent Binary-Lifting Spine** |
| **Runs Theorem & Squares** | Interior $L$-root window $[l+1, l+p]$ mutual exclusion $S[i] <_R S[i-1]$; Fine–Wilf substring run-clipping non-collision; palindromic run $w = P_1 P_2$ | Same $[l+1, l+p]$ trick + **The $< 2N$ Representative Squares Lemma** ($\sum (r-l+1-2p+1) \le N-1$) + explicit C++ enumeration kernel | **Complete Bannai et al. Proof + $< 2N$ Representative Squares + Fraenkel–Simpson / Brlek–Li Hierarchy** |
| **Accepted Non-Template Problems** | 32 (`P-1B-01`–`P-1B-32`) | 32 (`Problem 1`–`32`) | **42 Unique Deduplicated Problems (`W1B-01`–`W1B-42`)** |
| **Quarantined Template Problems** | 8 (`R-1B-01`–`R-1B-08`) | 9 (`R-1B-01`–`R-1B-09`) | **10 Unique Quarantined Templates (`R-1B-01`–`R-1B-10`)** |
| **Multilingual Citations** | 9 (inc. Franek 2016, Bille 2020, Barcelo 1990, `henkoku` 2020) | 8 (inc. Lothaire, Kociumaka 2014/2016, Jin Ce 2019) | **15 Consolidated `[EN]`/`[ZH]`/`[JA]` Primary Citations** |

---

### 1.2 What Cohort 1 Captured That Cohort 2 Missed (Cohort 2 Blind Spots)

1. **All-Prefix CFL Factorization via Duval Inner-Loop State Sharing (`r -> r - d*p`, `P-1B-20`)**:
   - When Duval's algorithm is at inner-loop state $(i, j, k = r + 1)$ with period $p = k - j$ and pre-Lyndon remainder $S[i..r] = w^d w'$ ($d = \lfloor (r - i + 1)/p \rfloor \ge 1, |w'| < p$), Cohort 1 proved that if the string terminated at $r$, Duval would emit $d$ copies of $w = S[i..i+p-1]$ followed by the CFL factorization of $w' = S[i + dp .. r]$. Because $w'$ is an exact copy of the prefix $S[i .. r - dp]$ (which was visited during the **exact same outer iteration** starting at $i$ at step $r' = r - dp$!), the CFL factor count, last factor, and XOR/sum of factor right-endpoints for **all $N$ prefixes $S[1..r]$** can be computed in $O(N)$ total time via a 3-line recurrence reading from $r - dp$. Cohort 2 only derived the `min_suf[j]` shift for the last factor in Problem 11, missing the general all-prefix CFL factorization recurrence (`Luogu P6127`).
2. **Explicit 4-Character Counterexample $S = \texttt{aaba}$ for Left-Truncation Non-Inclusion (`P-1B-12`)**:
   - Cohort 1 exhibited $S = \texttt{aaba}$ with query $[l, r] = [2, 4]$ ($S[2..4] = \texttt{aba}$): in the full prefix $S[1..4] = \texttt{aaba}$, the suffix $\texttt{aba}$ ($i=2$) is killed by the longer suffix $\texttt{aaba}$ ($i=1$) because $\texttt{aaba} \prec \texttt{aba}$, leaving $\text{Cand}_{\min}(\texttt{aaba}) = \{\texttt{a}, \texttt{aaba}\}$. When $l = 2$ cuts off $i = 1$, $\texttt{aba}$ revives in $\text{Cand}_{\min}(\texttt{aba}) = \{\texttt{a}, \texttt{aba}\}$ (needed when right-extending by $T = \texttt{c}$, since $\texttt{abac} < \texttt{ac}$). Cohort 2 gave $S = \texttt{abbb}$ (where $\text{Cand}(\texttt{abbb}) = \{1\}$ has empty intersection with $[2, 4]$), and Cohort 3 unifies both counterexamples to distinguish $T = \varepsilon$ from general $T \in \Sigma^*$.
3. **Substring Run Counting $|\mathcal{R}(S[L_q..R_q])|$ via Fine–Wilf Clipping Non-Collision (`P-1B-26`)**:
   - Cohort 1 proved that when global runs $R = [l_R, r_R, p] \in \mathcal{R}(S)$ are clipped to a query substring $[L_q, R_q]$, **no two distinct global runs $R_1, R_2$ ($p_1 < p_2$) can ever clip to the same sub-interval of length $\ge 2p_2$**. Why? Because their overlap would have length $\ge 2p_2 > p_1 + p_2 - \gcd(p_1, p_2)$, which by Fine–Wilf forces period $\gcd(p_1, p_2) \le p_1 < p_2$ throughout $R_2$'s clipped interval, contradicting that $p_2$ is the *primitive* period of $R_2$! This reduces $|\mathcal{R}(S[L_q..R_q])|$ to counting global runs with $\min(R_q, r_R) - \max(L_q, l_R) + 1 \ge 2p$ via 2D/3D orthogonal dominance.
4. **Symmetric Period Decomposition Theorem for Palindromic Runs (`P-1B-23`)**:
   - Cohort 1 proved that a run $R = [l, r, p]$ contains a palindrome of length $\ge p + 1$ if and only if its period block $w$ ($|w| = p$) factors into **two palindromes** $w = P_1 P_2$, which causes palindromic centers inside $R$ to repeat with half-period $p/2$ across two congruence classes modulo $p$.
5. **$O(\sqrt{N})$-Update, $O(1)$-Query Block Rolling Hash for `[ZJOI2017] 字符串` (`P-1B-09`)**:
   - Cohort 1 pointed out that replacing a Fenwick/Segment Tree rolling hash ($O(\log N)$ per hash query $\implies O(\log^2 N)$ per binary-search LCE) with a $\sqrt{N}$-block decomposition ($O(\sqrt{N})$ per range add, $O(1)$ per hash query $\implies O(\log N)$ per LCE) shaves a full $\log N$ factor off the query complexity of `[ZJOI2017] 字符串`.
6. **10 Accepted Problems Exclusive to Cohort 1**:
   - `CF 1051E — Vasya and Big Integers`, `Lyndon Array / CFL Reconstruction`, `CF 1043G — Speckled Band`, `Square-Free Substring Range Queries`, `Longest Lyndon Substring in S[l..r]`, `CF 1098F — Ж-function`, `Substring Minimum Cyclic Shift Queries`, `Substring Run Counting |\mathcal{R}(S[L_q..R_q])|`, `Longest Square / k-th Power in S[L_q..R_q]`, `Tree Path Significant Suffixes via HLD`, and `2D Range Queries over Interior L-Roots`.

---

### 1.3 What Cohort 2 Captured That Cohort 1 Missed (Cohort 1 Blind Spots)

1. **Witt's Necklace & Lyndon Formula + The FKM $O(1)$-Amortized Generation Algorithm (`Iter 58.2`)**:
   - Cohort 2 derived Witt's identity $\sigma^n = \sum_{d \mid n} d \cdot L_\sigma(d) \iff L_\sigma(n) = \frac{1}{n} \sum_{d \mid n} \mu(n/d) \sigma^d$ by grouping $\Sigma^n$ by primitive root length $d \mid n$ and taking the unique Lyndon rotation in each primitive orbit, alongside Burnside's necklace formula $N_\sigma(n) = \frac{1}{n} \sum_{d \mid n} \varphi(n/d) \sigma^d = \sum_{d \mid n} L_\sigma(d)$ and the Fredricksen–Kessler–Maiorana (FKM) algorithm.
2. **Two-Way Strict Monotonicity $\min(u'T, vT) < uT < \max(u'T, vT)$ & The Segment Tree `pushup` 1-Survivor Theorem (`Iter 59.2–59.3`)**:
   - Cohort 2 proved that for $u' \in \text{Suf}(U), u = wu', v = w^2 u'$ ($|u| < |v| < 2|u|$), left-cancellation invariance forces either $u'T < uT < vT$ or $u'T > uT > vT$ for **every** finite $T \in \Sigma^*$. Thus $uT$ is strictly sandwiched between $u'T$ and $vT$ and can **neither minimize nor maximize** $xT$!
   - Crucially, Cohort 2 proved the **Segment Tree `pushup` 1-Survivor Theorem**: when merging `left_child` $[L, M]$ and `right_child` $[M+1, R]$, every candidate suffix starting in $[L, M]$ has length in $[R-M+1, R-L+1]$. Since $R-L+1 \le 2(R-M+1)$, **all candidates from `left_child` lie within a factor of $2$ of one another**! Therefore, **at most ONE candidate from `left_child` can survive in $\text{Cand}([L, R])$**, which immediately proves both $|\text{Cand}([L, R])| \le |\text{Cand}(\text{right\_child})| + 1 \le \lfloor \log_2(R-L+1) \rfloor + 1$ and that building the entire Segment Tree of Significant Suffixes for a static string takes $\sum_{h=1}^{\log N} \frac{N}{2^h} O(h) = O(N)$ time!
3. **Static Substring Minimum Suffix via Shortest Border of $\arg\min_{i \in [l, r]} \text{rk}[i]$ (`Iter 62, Problem 20`)**:
   - Cohort 2 proved that when $S$ is static and $T = \varepsilon$, if $i_0 = \arg\min_{i \in [l, r]} \text{rk}[i]$, then $W = S[i_0..r]$ beats every suffix $S[j..r]$ ($j \in [l, r]$) that mismatches $W$ before $r$; any suffix $S[j..r]$ that does *not* mismatch $W$ before $r$ is a proper prefix and suffix of $W$—i.e., a **border** of $W$ with $j > i_0 \ge l$ (automatically inside $[l, r]$!). Since all borders of $W$ are prefixes of one another, the lexicographically smallest suffix of $S[l..r]$ is **literally the shortest non-empty border of $W = S[i_0..r]$** (or $W$ itself if $W$ is unbordered)!
4. **Min-Cartesian Tree Isomorphism of the Lyndon Tree & The $S = \texttt{bab}$ Counterexample for $\lambda_>$ (`Iter 60.3–60.4`)**:
   - Cohort 2 proved that the Right-Standard Lyndon Tree of $\$S[1..n]$ is isomorphic to the **Min-Cartesian Tree of $\text{rk}[2..n+1]$**, where each node $m = \arg\min_{j \in [l+1, r]} \text{rk}[j]$ with Cartesian range $[L_m, R_m]$ represents the Lyndon word $S[L_m - 1 .. R_m]$ (exposing the $-1$ left-endpoint shift bug).
   - Cohort 2 also constructed the minimal 3-character counterexample $S = \texttt{bab}$ ($\text{rk}_< = [3, 1, 2]$) showing why negating $\text{rk}_<$ to compute $\lambda_>$ fails: $-\text{rk}_<$ claims $\texttt{b} >_R \texttt{bab}$ and falsely labels the bordered word $\texttt{bab}$ as a $>-$Lyndon word!
5. **The $< 2N$ Representative Squares Lemma (`Iter 61.2 & Problem 26`)**:
   - Cohort 2 proved that across all runs $R = (l, r, p) \in \mathcal{R}(S)$ and all integer multiples $k \ge 1$, the total number of canonical square starting positions $a \in [l, \min(l + p - 1, r - 2kp + 1)]$ is **strictly less than $2N$** (and the number of primitively rooted square starting positions $\sum_{R \in \mathcal{R}(S)} (r - l + 1 - 2p + 1) \le N - 1$), allowing explicit enumeration of all distinct square candidates in $O(N)$ time!
6. **10 Accepted Problems Exclusive to Cohort 2**:
   - `CF 1537E2 — Erase and Extend`, `ARC 050 D — Suffix Concat`, `POJ 3693 — Maximum Repetition Substring`, `ABC 272 F — Two Strings`, `CF 825F — String Compression`, `AGC 023 F — 01 on Tree (Lyndon Tree Merge)`, `ARC 113 E — Rvom and Rsrev`, `Square-Free String Partitioning DP in O(N)`, `Longest Unbordered Substring (Ehrenfeucht–Silberger)`, `Sum over Distinct Squares f(endpos(w^2), |w|)`, and `CFL Shuffle / Interleaving of Two Strings`.

---

### 1.4 Obscure & Frontier Stringology Techniques Hunted in Cohort 3 (Gap-Hunting Pass)

To guarantee zero blind spots across `[EN]`, `[ZH]` (`国家集训队论文`), and `[JA]` (`henkoku`, `noshi91`, `maspypy`) grandmaster literature for Wave 1B, Cohort 3 hunts down and integrates **five frontier extensions** in detail:

1. **Segment-Tree-Free $O(\log N)$ Computation of $\text{Cand}_{\min}(S[l..r])$ via Dyadic SA-Rank RMQ Bands (Kociumaka et al. 2014 / Babenko et al.)**:
   - Can we extract the entire Significant Suffix set $\text{Cand}_{\min}(S[l..r])$ for any substring $S[l..r]$ in $O(\log(r - l + 1))$ time using **only $O(N)$ space** (just the Suffix Array RMQ table, with no Segment Tree of vectors)? In **Section 3.5**, we prove how partitioning $[1, r - l + 1]$ into $\le \lfloor \log_2(r-l+1) \rfloor + 1$ dyadic length bands $[2^k, 2^{k+1})$ and querying $i_k = \arg\min_{x \in I_k} \text{rk}[x]$ in each band recovers a superset of $\text{Cand}_{\min}(S[l..r])$ (after left-shifting $i_k$ to the earliest copy of its period inside $I_k$ when $S[i_k..r]$ is periodic!).
2. **Run-Length Encoded (RLE) Duval Algorithm in $O(M)$ Time (`RLE Lyndon Factorization`)**:
   - When $S = c_1^{a_1} c_2^{a_2} \cdots c_M^{a_M}$ has $M \le 10^5$ blocks but total length $\sum a_t \le 10^{18}$, how do we factor $S$ into Lyndon words in $O(M)$ time? In **Section 2.6**, we prove the **RLE-Lyndon Block Split Invariant**: a Lyndon word of length $> 1$ never starts in the interior of a unary block $c_t^{a_t}$, and an RLE block $c_k^{a_k}$ only splits when $c_k = c_j$ and $a_k < a_j$ at the very start of a period ($j = i$, triggering Case 2 after consuming $a_k$ copies of $c_i$) or $a_k > a_j$ when $c_k$ is the minimum character!
3. **Bijective Burrows–Wheeler Transform (BWTS — Gil & Scott 2012; Kufleitner 2009)**:
   - Standard BWT appends a sentinel $\$$ to force primitivity. In **Section 2.7**, we show how the Chen–Fox–Lyndon factorization $S = w_1 w_2 \cdots w_k$ defines a **sentinel-free bijection $\Sigma^N \leftrightarrow \Sigma^N$** by sorting all cyclic shifts of all $w_i$ under the infinite periodic order $X^\omega \le Y^\omega$, and why decomposing the LF-mapping into disjoint cycles recovers the CFL factors in $O(N)$ time.
4. **Worst-Case $O(\log N)$ Online & Persistent Lyndon Factorization via Binary-Lifting on the Lyndon Tree Right Spine**:
   - In **Section 4.4**, we show how to upgrade Duval's amortized $O(1)$ right-append to **worst-case $O(\log N)$ per append** (supporting persistent tree branching) by maintaining the CFL stack $w_1^{d_1} > \cdots > w_m^{d_m}$ with binary lifting and $O(1)$ LCE.
5. **The Complete Hierarchy of Square & Run Density Bounds (Fraenkel–Simpson $\le 2N$, Brlek–Li $\le N - \Theta(\log N)$, and Binary Runs $\le \frac{22}{23}N$)**:
   - In **Section 5.4**, we give the self-contained Three-Squares proof of the Fraenkel–Simpson theorem (at most $2$ distinct squares can have their *last* occurrence starting at any index $i$) alongside the modern tightening to $\le N - \Theta(\log N)$ (Brlek–Li 2022).

---

## Section 2. Reconciled Master Treatise Part I: Lyndon Words, the Chen–Fox–Lyndon Theorem, Witt's Formula & Duval's Algorithm

### 2.1 Prerequisite Boundary & Multilingual Rosetta Stone

Per `AGENTS.md` and `strings_research/PLAN.md`, the reader is assumed to hold tested $O(N)$ library implementations of **KMP (`pi`)**, **Z-Algorithm (`z`)**, **Suffix Array (`SA`, `rk`, `height` + $O(1)$ RMQ LCE)**, and **Suffix Automaton (SAM)**.

| Concept (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) | Key Invariant / Bound |
| :--- | :--- | :--- | :--- |
| **Lyndon word** ($w \in \mathcal{L}$) | Lyndon 串 / 林登词 | Lyndon 語 (リンドン語) | Strictly smaller than all proper suffixes ($w \prec v$) |
| **Strong lexicographical order** ($u \prec v$) | 强字典序小于 (非前缀小于) | 強い辞書順順序 | $u < v$ and $u \not\sqsubset v$; stable under right-extensions |
| **Chen–Fox–Lyndon (CFL) factorization** | Lyndon 分解 (CFL 分解) | Lyndon 分解 | Unique $S = w_1 w_2 \cdots w_k$ with $w_i \in \mathcal{L}, w_1 \ge \cdots \ge w_k$ |
| **Pre-Lyndon / Duval word** | 近似 Lyndon 串 / 前缀周期串 | 準 Lyndon 語 / プレネックレス | Prefix of a Lyndon word: $P = w^d w'$ ($w \in \mathcal{L}, w' \sqsubset w$) |
| **Smallest cyclic shift** | 最小表示法 | 辞書順最小の巡回シフト | First copy of the CFL factor of $S+S$ whose block crosses $N$ |
| **Significant Suffixes** ($\text{Cand}(P)$) | 显著后缀 (`Cand(r)`) | 有意接尾辞 / 最小接尾辞候補 | $|u| < |v| < 2|u| \implies \min(u'T, vT) < uT < \max(u'T, vT)$; size $\le \lfloor\log_2 |P|\rfloor + 1$ |
| **Standard factorization** ($w = uv$) | 标准分解 ($v$ 为最长真 Lyndon 后缀) | 標準分解 | $v$ is longest proper Lyndon suffix = smallest proper suffix |
| **Lyndon Array** ($\lambda[i], R_{\mathcal{L}}[i]$) | 最长 Lyndon 前缀数组 | Lyndon 配列 | $i + \lambda[i] = \min\{j > i \mid S[j..N] < S[i..N]\}$ |
| **Lyndon Tree** | Lyndon 树 | Lyndon 木 | Recursive standard factorization; isomorphic to Min-Cartesian Tree of $\text{rk}[2..N+1]$ |
| **Run (Maximal repetition)** | 极长周期子串 (Runs) | 極大周期部分文字列 (Run) | $R = [l, r, p]$ with $r - l + 1 \ge 2p$; $|\mathcal{R}(S)| < N, \sum \text{exp}(R) < 3N$ |
| **Lyndon root of a run** ($L$-root) | Run 的 Lyndon 根 | Run の Lyndon 根 | Unique $<_R$-Lyndon shift in $[l+1, l+p]$ where $S[r+1] <_R S[r+1-p]$ |
| **Three-Squares Lemma** | 三平方引理 | 三平方補題 | Primitive $u^2 \sqsubset v^2 \sqsubset w^2 \implies |w| \ge |u| + |v|$ |

---

### 2.2 Equivalent Characterizations of Lyndon Words & Strong Lexicographical Algebra

Let $(\Sigma, <)$ be a totally ordered alphabet. For $A, B \in \Sigma^*$, write $A \sqsubset B$ if $A$ is a proper prefix of $B$, and write $A \prec B$ (**strong lexicographical inequality**) if $A < B$ and $A \not\sqsubset B$ (meaning $A$ and $B$ differ at some character position $t \le \min(|A|, |B|)$ with $A[t] < B[t]$).

**Two Fundamental Laws of Lexicographical Order**:
1. **Left-Cancellation Invariance**: For any $W, X, Y \in \Sigma^*$, $X < Y \iff WX < WY$, and $X \prec Y \iff WX \prec WY$.
2. **Right-Extension Stability of $\prec$**: If $X \prec Y$, then for **all** right-extensions $Z_1, Z_2 \in \Sigma^*$, $X Z_1 \prec Y Z_2$. By contrast, if $X \sqsubset Y$, appending $Z_1, Z_2$ can flip the inequality!

#### Theorem 2.1 (Four Equivalent Characterizations of a Lyndon Word)
For a nonempty word $w \in \Sigma^+$, the following four conditions are equivalent (and define a **Lyndon word**, written $w \in \mathcal{L}$):
1. **(Strict Minimal Cyclic Shift)**: $w$ is strictly smaller than all of its nontrivial cyclic rotations: for every split $w = uv$ with $u, v \in \Sigma^+$, $uv < vu$.
2. **(Strict Minimal Proper Suffix)**: $w$ is strictly smaller than every nonempty proper suffix of $w$: for every split $w = uv$ with $u, v \in \Sigma^+$, $w < v$.
3. **(Strong Inequality Against Proper Suffixes & Border-Freeness)**: Every nonempty proper suffix $v$ of $w$ satisfies $w \prec v$; in particular, $w$ is **border-free** (unbordered, $\pi(|w|) = 0$) and **primitive**.
4. **(Recursive / Standard Factorization Characterization)**: Either $|w| = 1$, or $|w| \ge 2$ and there exist Lyndon words $u, v \in \mathcal{L}$ with $u < v$ such that $w = uv$ (and furthermore $u < uv < v$).

**Complete Proof ($1 \iff 2 \iff 3 \iff 4$)**:
- **($2 \implies 3$)**: Since $|w| > |v|$ for any proper suffix $v$, $w$ cannot be a prefix of $v$. Thus $w < v$ immediately forces a character mismatch within $|v|$, so $w \prec v$. If $b$ were a nonempty proper border of $w$, then $b \sqsubset w \implies b < w$, contradicting $w < b$ applied to the proper suffix $b$.
- **($3 \implies 1$)**: For any split $w = uv$ ($u, v \in \Sigma^+$), (3) gives $uv = w \prec v$. By right-extension stability of $\prec$, $uv \prec vu \implies uv < vu$.
- **($1 \implies 2$)**: Suppose $uv < vu$ for all $u, v \in \Sigma^+$, and suppose for contradiction that $v \le w$ for some nonempty proper suffix $v$. Choose the **longest** nonempty proper suffix $v$ such that $v \le w = uv$. Clearly $v \ne w$. If $v \prec uv$, right-extending $v$ to $vu$ gives $vu \prec uv$, contradicting (1). Thus $v$ must be a proper prefix of $w$: $v \sqsubset uv$. Since $v$ is both a prefix and suffix of $w$ and $|v| < |w|$, if $|v| \ge |u|$ then $v$ overlaps $u$, or writing $u = v u'$ (when $|v| < |u|$) or $w = v z$: apply (1) to the rotation starting at the suffix of length $|w| - |v|$ or note that if $w = u v$ has prefix $v$, then $w = v y$ with $|y| = |u|$. By (1), $w = u v < v u$. Substituting $w = v y$ gives $v y < v u$, and left-cancelling $v$ yields $y < u \sqsubset w$. Thus $y$ is a nonempty proper suffix of $w$ with $y < w$; if we instead chose the **shortest** counterexample suffix $v$, then $|y| = |w| - |v| < |v|$ (if $|v| > |w|/2$) or $v \sqsubset u \implies u = v u'$ where $(v u') v < v (v u') \implies u' v < v u' = u < w$ gives a strictly **longer** counterexample suffix $u'v$ ($|u'v| > |v|$), contradicting the maximality of $|v|$!
- **($4 \implies 2$)**: Let $u, v \in \mathcal{L}$ with $u < v$ and $w = uv$. First we show $uv < v$: if $u \prec v$, then $uv \prec v$; if $u \sqsubset v$, write $v = u v'$. Since $v \in \mathcal{L}$, its proper suffix $v'$ satisfies $v < v'$; prepending $u$ gives $uv = u u v' < u v' = v$. Now take any nonempty proper suffix $s$ of $uv$:
  - If $s = v$: $uv < v = s$.
  - If $s$ is a proper suffix of $v$: since $v \in \mathcal{L}$, $uv < v < s$.
  - If $s = u'v$ for a nonempty proper suffix $u'$ of $u$: since $u \in \mathcal{L}$, $u \prec u'$, so right-extending by $v$ gives $uv \prec u'v = s$.
- **($2 \implies 4$)**: For $|w| \ge 2$, let $v$ be the **longest** nonempty proper suffix of $w$ that belongs to $\mathcal{L}$ (well-defined since $w[|w|] \in \mathcal{L}$), and write $w = uv$. Since $w \in \mathcal{L}$, $uv = w < v \implies u < uv < v$. Suppose for contradiction $u \notin \mathcal{L}$; let $s$ be the lexicographically smallest nonempty proper suffix of $u$ (which is necessarily Lyndon and satisfies $s \le u < v$). By ($4 \implies 2$), $sv \in \mathcal{L}$, and $sv$ is a proper suffix of $w = uv$ strictly longer than $v$, contradicting the maximality of $|v|$! $\blacksquare$

---

### 2.3 The Chen–Fox–Lyndon (CFL) Uniqueness Theorem & Canonical Corollaries

#### Theorem 2.2 (Chen–Fox–Lyndon Theorem, 1958)
Every nonempty string $S \in \Sigma^+$ admits a **unique** factorization into Lyndon words
$$S = w_1 w_2 \cdots w_k \qquad \text{such that } w_i \in \mathcal{L} \text{ and } w_1 \ge w_2 \ge \cdots \ge w_k.$$

**Proof**:
- *Existence*: Start from the $N$ single-character Lyndon words $S[1], \dots, S[N]$. Repeatedly merge any adjacent pair satisfying $w_i < w_{i+1}$ into $w_i w_{i+1} \in \mathcal{L}$ (Theorem 2.1(4)). This terminates in $\le N-1$ steps with $w_1 \ge \cdots \ge w_k$.
- *Uniqueness*: Suppose $S = w_1 \cdots w_k = w'_1 \cdots w'_{k'}$ are two valid CFL factorizations with $|w_1| > |w'_1|$ at the first differing factor. Then $w_1 = w'_1 \cdots w'_{r-1} p$ where $r \ge 2$ and $p$ is a nonempty prefix of $w'_r$. Since $p$ is a nonempty proper suffix of the Lyndon word $w_1$, Theorem 2.1(2) gives $w_1 < p$. Chaining with $p \sqsubseteq w'_r \le \cdots \le w'_1 \sqsubset w_1$ yields the contradiction $w_1 < p \le w'_r \le w'_1 < w_1$. Thus $w_1 = w'_1$, and induction completes the proof. $\blacksquare$

> [!TIP]
> **Two Structural Pillars of the CFL Factorization $S = w_1 w_2 \cdots w_k$**
> 1. **First Factor ($w_1$)**: $w_1$ is the **longest prefix** of $S$ that is a Lyndon word.
> 2. **Last Factor ($w_k$)**: $w_k$ is both the **longest Lyndon suffix** of $S$ and the **lexicographically smallest nonempty suffix** of $S$!

---

### 2.4 Witt's Necklace & Lyndon Formula and the FKM Generation Algorithm

Let $\sigma = |\Sigma|$. Every word $S \in \Sigma^N$ has a unique primitive root of length $d \mid N$ ($S = u^{N/d}$). Each primitive word of length $d$ belongs to an equivalence class of $d$ distinct cyclic rotations, **exactly one** of which is a Lyndon word of length $d$. Denoting by $L_\sigma(d)$ the number of Lyndon words of length $d$ and $N_\sigma(N)$ the number of necklaces (cyclic equivalence classes) of length $N$:
$$\sigma^N = \sum_{d \mid N} d \cdot L_\sigma(d) \implies L_\sigma(N) = \frac{1}{N} \sum_{d \mid N} \mu\!\left(\frac{N}{d}\right) \sigma^d, \qquad N_\sigma(N) = \sum_{d \mid N} L_\sigma(d) = \frac{1}{N} \sum_{d \mid N} \varphi\!\left(\frac{N}{d}\right) \sigma^d.$$

**Duval's Next-Lyndon / FKM Theorem (1988)**: Given any Lyndon word $w \in \mathcal{L}$ of length $\le N$, form the length-$N$ periodic truncation $P = (w^\omega)[1..N]$, strip all trailing occurrences of the maximum alphabet character $z = \max \Sigma$, and increment the last remaining character by $+1$. The resulting string is the **exact lexicographically next Lyndon word** of length $\le N$ (and concatenating all Lyndon words of lengths $d \mid N$ in lexicographical order produces the **lexicographically smallest De Bruijn cycle** of order $N$ in $O(1)$ amortized time per bit/character!).

---

### 2.5 Duval's $O(N)$ Three-Pointer Algorithm & All-Prefix CFL State Sharing

**Definition 2.3 (Pre-Lyndon Word)**. A nonempty prefix of a Lyndon word is called a **pre-Lyndon word**; every pre-Lyndon word has the unique representation $P = w^d w'$, where $w \in \mathcal{L}$ is its fundamental Lyndon period ($p = |w|$), $d \ge 1$, and $w'$ is a proper prefix of $w$ ($0 \le |w'| < p$).

#### The Three-Pointer Automaton $(i, j, k)$
While factoring $S[i..N]$, Duval's inner loop maintains the pre-Lyndon prefix $S[i..k-1] = w^d w'$ of period $p = k - j$:
- **Case 1 ($S[k] == S[j]$ — Periodic Continuation)**: Extends $w'$ by one character (`j++, k++`; period $p = k - j$ is unchanged).
- **Case 2 ($S[k] > S[j]$ — Collapse into a Single Lyndon Word)**: Because $w' S[k] \succ w$, repeated application of Theorem 2.1(4) collapses the entire prefix $S[i..k] = w^d w' S[k]$ into a single Lyndon word of period $p_{\text{new}} = k - i + 1$ (`j = i, k++`).
- **Case 3 ($S[k] < S[j]$ — Periodic Rupture & CFL Emission)**: Now $w' S[k] \prec w$, so any prefix $S[i..m]$ ($m \ge k$) has a proper suffix starting with $w' S[k] \prec w$ and can **never** be Lyndon. Emit the $d = \lfloor (k - i)/p \rfloor$ frozen copies of $w$ (`while (i <= j) emit(i, p), i += p`) and restart the outer loop from the new $i = i_{\text{old}} + d \cdot p$ (the start of the incomplete remainder $w'$).

**Dual Complexity Proofs ($< 2N$ Comparisons)**:
1. *Phase-Rewind Bound (Cohort 2)*: In each outer phase advancing $i$ by $\Delta i = d \cdot p$, the incomplete remainder $w'$ has length $r = |w'| < p \le d \cdot p = \Delta i$. Thus the inner loop runs $m = \Delta i + r < 2\Delta i$ comparisons per phase, summing to $\sum m < 2 \sum \Delta i = 2N$.
2. *Strict Potential Function (Cohort 1)*: $\Phi(i, k) = 2i + k$ increases by $+1$ in Cases 1–2 and by $2\Delta i + (1 - |w'|) > \Delta i \ge 1$ in Case 3.

#### Theorem 2.4 (All-Prefix CFL Factorization via Duval State Sharing — `r -> r - d*p`)
At the moment the inner pointer inspects $S[r]$ (so $S[i..r] = w^d w'$ is pre-Lyndon after updating $j$ for $S[r]$, with current period $p = r + 1 - j$ and $d = \lfloor (r - i + 1)/p \rfloor \ge 1$), what is the complete CFL factorization of the prefix $S[1..r]$?
- It consists of:
  1. The already-emitted CFL factors of $S[1..i-1]$,
  2. Followed by $d$ copies of the Lyndon word $w = S[i..i+p-1]$,
  3. Followed by the CFL factorization of the remainder $w' = S[i + dp .. r]$, which (when $|w'| > 0$) is **identical up to index shift $+dp$** to the CFL factorization of $S[i .. r - dp]$ computed at step $r' = r - dp$ during the **exact same outer phase** starting at $i$!
- Consequently, the CFL factor count `cnt[r]`, the starting index of the last CFL factor (= minimum suffix) `min_suf[r]`, and the sum of factor right-endpoints `sum_end[r]` of **every prefix $S[1..r]$** are computed in $O(1)$ per step inside Duval's loop:
  - If $|w'| = (r - i + 1) \bmod p == 0$:
    $$\text{cnt}[r] = \text{cnt}[i-1] + d, \qquad \text{min\_suf}[r] = r - p + 1.$$
  - If $|w'| > 0$, let $r' = r - d \cdot p \in [i, i + p - 2]$:
    $$\text{cnt}[r] = \text{cnt}[r'] + d, \qquad \text{min\_suf}[r] = \text{min\_suf}[r'] + d \cdot p.$$
- **Asymmetric Duality for Prefix Maximum Suffix**: If we run Duval's algorithm under the **reversed alphabet order $>$,** the starting position of the **lexicographically largest suffix** of $S[1..r]$ is simply the active outer pointer $i$ (the start of the longest active pre-$>-$Lyndon suffix $w^d w'$ ending at $r$)!

---

### 2.6 Frontier Extension I: $O(M)$ Duval Factorization on Run-Length Encoded (RLE) Strings

Suppose $S = c_1^{a_1} c_2^{a_2} \cdots c_M^{a_M}$ ($c_t \ne c_{t+1}$, $M \le 10^5$, $\sum a_t \le 10^{18}$). Can a Lyndon factor $w$ of length $|w| > 1$ ever start or end strictly in the middle of a run $c_t^{a_t}$?
- **Lemma 2.5 (RLE-Lyndon Boundary Invariant)**:
  1. No Lyndon word $w$ of length $|w| > 1$ can **start** in the interior of a unary block $c_t^{a_t}$ (at the 2nd or later copy of $c_t$) inside a CFL factorization, because if $w$ starts with $c_t$, then $c_t = \min(w)$; any preceding copy of $c_t$ would concatenate with $w$ via $c_t < w \implies c_t w \in \mathcal{L}$!
  2. When running Duval on the $M$ pairs $(c_t, a_t)$:
     - If $j = i$ (comparing a block $c_k^{a_k}$ against the very first block $c_i^{a_i}$ of the current Lyndon factor, so $c_i$ is the minimum character of $w$):
       - If $c_k == c_i$ and $a_k > a_i$: then $c_i^{a_k} = c_i^{a_i} c_i^{a_k - a_i}$ contains a suffix starting with $c_i^{a_i + 1} \prec c_i^{a_i} c_{i+1}\dots$, triggering **Case 3** after matching $a_i$ characters!
       - If $c_k == c_i$ and $a_k < a_i$: after matching $a_k$ copies of $c_i$, the next block $c_{k+1} > c_i$ triggers **Case 2** against the $(a_k+1)$-st copy of $c_i$ in $c_i^{a_i}$, collapsing $S[i..k]$ into a single Lyndon word without splitting any block!
     - Thus **every non-unary Lyndon factor starts and ends on exact RLE block boundaries**, and only unary factors $c_t^{a_t}$ emit $a_t$ copies of the single character $c_t$! Running Duval directly on the $M$ blocks with the tuple comparison `(c_k, -a_k)` at the start of the period solves RLE CFL factorization in $O(M)$ time!

---

### 2.7 Frontier Extension II: The Bijective Burrows–Wheeler Transform (BWTS)

In the CFL factorization $S = w_1 w_2 \cdots w_k$ ($w_1 \ge w_2 \ge \cdots \ge w_k$), each factor $w_i$ has $\lvert w_i \rvert$ distinct cyclic shifts. If we collect all $N = \sum_{i=1}^k |w_i|$ cyclic shifts of all factors $w_1, \dots, w_k$ and sort them under the **infinite periodic order** $X^\omega \le Y^\omega$ (breaking ties between identical factors $w_i = w_j$ by index $i < j$), the sequence of last characters of the sorted shifts forms the **Bijective BWT ($\text{BWTS}(S)$)** (Scott 2007; Gil & Scott 2012; Kufleitner 2009).
- **Why It Is a Sentinel-Free Bijection $\Sigma^N \leftrightarrow \Sigma^N$**: Every string $T \in \Sigma^N$ defines a standard LF-permutation $\pi_{LF}$ mapping the $r$-th occurrence of character $c$ in $T$ to the $r$-th occurrence of $c$ in $\text{sort}(T)$. Decomposing $\pi_{LF}$ into its **disjoint cycles** reconstructs one primitive necklace per cycle; rotating each cycle to its unique Lyndon representative and sorting the resulting Lyndon words in non-increasing order $w_1 \ge w_2 \ge \cdots \ge w_k$ recovers $S = w_1 w_2 \cdots w_k$ uniquely in $O(N)$ time!

---

## Section 3. Reconciled Master Treatise Part II: The Significant Suffixes (`显著后缀`) Theorem & Substring Lexicographical Queries

### 3.1 Step 1 — The Diagnostic Signal: Why Global Suffix Ranks Fail Under Right-Extensions

When a problem queries the **lexicographically smallest (or largest) suffix of a substring $S[l..r]$**, or asks for $i \in [l, r]$ minimizing $S[i..r] + T$ under an unknown future right-extension $T$ (as in Segment Tree range decomposition `[ZJOI2017] 字符串` or substring cyclic shifts), the global Suffix Array rank $\text{rk}[i]$ compares $S[i..r] + S[r+1..N]$ rather than $S[i..r] + T$.
Crucially, for two suffixes $u, v$ of $P = S[L..R]$ with $|u| < |v|$:
- If $u \not\sqsubset v$, then $u$ and $v$ have a character mismatch at some position $\le |u|$, so either $u \prec v$ or $v \prec u$. By right-extension stability of $\prec$, **their relative order $uT \prec vT$ or $vT \prec uT$ is 100% invariant across ALL $T \in \Sigma^*$**!
- Only when **$u$ is a proper prefix (and hence a border) of $v$ ($u \sqsubset v$)** can the choice of right-extension $T$ flip the winner between $uT$ and $vT$!

---

### 3.2 Step 2 — The Combinatorial Word Invariant: Two-Way Tandem Annihilation & Doubling

For any string $U$, define the **Minimal Significant Suffix Set** $\text{Cand}_{\min}(U)$ (resp. **Maximal Significant Suffix Set** $\text{Cand}_{\max}(U)$) to be the set of suffixes $u \in \text{Suf}(U)$ for which there exists at least one finite string $T \in \Sigma^*$ such that $uT$ is the **strictly shortest** among all suffixes $x \in \text{Suf}(U)$ minimizing (resp. maximizing, tie-breaking by longest or shortest) $xT$.

#### Theorem 3.1 (The Significant Suffixes Tandem-Annihilation & Doubling Theorem — Jin Ce 2019; Kociumaka et al.)
Let $u, v \in \text{Suf}(U)$ satisfy $|u| < |v| < 2|u|$ and $u \sqsubset v$ (so $u$ is a border of $v$ of length $> |v|/2$). Then there exists a nonempty proper suffix $u' \in \text{Suf}(U)$ of length $|u'| = 2|u| - |v| < |u|$ and a period block $w$ of length $p = |v| - |u| < |u|$ such that
$$u' \in \text{Suf}(U), \qquad u = w u', \qquad v = w^2 u',$$
and for **every** finite right-extension $T \in \Sigma^*$:
$$\min(u'T,\; vT) < uT < \max(u'T,\; vT).$$
Consequently:
1. The middle suffix **$u$ can NEVER belong to $\text{Cand}_{\min}(U)$ and can NEVER belong to $\text{Cand}_{\max}(U)$**!
2. In both $\text{Cand}_{\min}(U)$ and $\text{Cand}_{\max}(U)$, ordering the surviving suffixes by increasing length $|u_1| < |u_2| < \cdots < |u_k|$ yields
   $$u_1 \sqsubset u_2 \sqsubset \cdots \sqsubset u_k, \qquad |u_{i+1}| \ge 2|u_i| \quad (1 \le i < k), \qquad k \le \lfloor \log_2 |U| \rfloor + 1.$$

**Complete Zero-Magic Proof**:
Since $u$ is both a prefix and a suffix of $v$ with $p = |v| - |u| < |u|$, let $w = v[1..p]$. Shifting $v$ by $p$ gives $v = w u$. Because $|u| > p = |w|$ and $u \sqsubset v = wu$, $w$ is also a proper prefix of $u$; write $u = w u'$ with $|u'| = |u| - p = 2|u| - |v| > 0$. Since $u'$ is a suffix of $u \in \text{Suf}(U)$, we have $u' \in \text{Suf}(U)$, $u = wu'$, and $v = w^2 u'$:

```
v = [---- w ----][---- w ----][-- u' --]
u =              [---- w ----][-- u' --]
u'=                           [-- u' --]
```

Now fix any $T \in \Sigma^*$. Since $|u'T| < |uT|$, we have $u'T \ne uT$. Compare $u'T$ and $uT = w u' T$:
- **Case A ($u'T < uT$)**: Applying left-cancellation invariance by prepending $w$ to both sides of $u'T < w u' T$ gives:
  $$w(u'T) < w(w u' T) \iff uT < vT.$$
  Thus $u'T < uT < vT$.
- **Case B ($u'T > uT$)**: Prepending $w$ to both sides of $u'T > w u' T$ gives:
  $$w(u'T) > w(w u' T) \iff uT > vT.$$
  Thus $vT < uT < u'T$.

In both cases, $uT$ lies **strictly between** $u'T$ and $vT$, so $u$ is strictly beaten by $\min(u'T, vT)$ for minimization and strictly beaten by $\max(u'T, vT)$ for maximization! $\blacksquare$

---

### 3.3 Step 3 — Reverse-Engineering the Three Algorithmic Compilations

#### Compilation A: Online Prefix Maintenance of $\text{Cand}_{\min}(S[1..r])$ in $O(\log r)$ per Step (`[JSOI2019] 节日庆典`)
When appending $c = S[r]$ to $\text{Cand}_{\min}(S[1..r-1])$:
1. Form the raw candidate list by taking $\{u \cdot c \mid u \in \text{Cand}_{\min}(S[1..r-1])\} \cup \{c\}$.
2. Scan candidates in increasing order of length. When comparing the current survivor $u$ on top of the stack against the next longer candidate $v$ ($|u| < |v|$, where $u[1..|u|-1] \sqsubset v$), compare their newly appended character $c = S[r]$ at position $|u|$ of $u$ against $d = v[|u|] = S[r - |v| + |u|]$:
   - If $c < d$: $u \prec v$ at position $|u|$, so $v$ is permanently eliminated; skip $v$.
   - If $c > d$: $v \prec u$ at position $|u|$, so $u$ is permanently eliminated; pop $u$ and re-compare $v$ against the new top of stack.
   - If $c == d$: $u \sqsubset v$ still holds! If $|v| < 2|u|$, then by Theorem 3.1 the **middle** suffix $u$ is dominated between the candidate below $u$ on the stack and $v$, so **pop $u$ and push $v$**; otherwise ($|v| \ge 2|u|$), keep $u$ and push $v$!

#### Compilation B: Segment Tree of Significant Suffixes & The 1-Survivor `pushup` Theorem (`[ZJOI2017] 字符串`)
Suppose a Segment Tree node $[L, R]$ merges `left_child` $[L, M]$ and `right_child` $[M+1, R]$ ($R - M \le M - L + 1 \le R - M + 1$).
- **Theorem 3.2 (The `pushup` 1-Survivor Theorem — Cohort 2)**: Every suffix of $S[L..R]$ starting in `left_child` $[L, M]$ has length in $[R - M + 1,\; R - L + 1]$. Because $R - L + 1 \le 2(R - M + 1)$, **every pair of candidates $x, y$ coming from `left_child` (extended by $S[M+1..R]$) satisfies $|x| < |y| < 2|x|$**!
- By Theorem 3.1, **at most ONE candidate from `left_child` can survive in $\text{Cand}([L, R])$**!
- **Algorithmic Payoff**:
  1. In `pushup([L, R])`, copy $\text{Cand}([M+1, R])$ from `right_child`. Scan $x \in \text{Cand}([L, M])$ maintaining a single tournament winner $x^*$ on $[L, R]$ via LCE comparisons (if $x \sqsubset x^*$ up to $R$, keep the longer one $x^*$ because the shorter one $x$ is sandwiched between $x^*$ and $u' \in [M+1, R]$!). Finally, append the single winner $x^*$ to $\text{Cand}([M+1, R])$ ( popping the longest candidate of $\text{right\_child}$ if $x^*$ dominates it or if $|x^*| < 2|\text{longest}_{\text{right}}|$).
  2. For a static string with $O(1)$ SA-LCE, `pushup` takes $O(\log(R - L))$ time, so **building the entire Segment Tree takes $\sum_{h=1}^{\log N} \frac{N}{2^h} O(h) = O(N)$ total time and $O(N)$ space**!
  3. For dynamic range addition `S[l..r] += d` (`[ZJOI2017] 字符串`), adding $+d$ to all characters in $[L, R]$ leaves $\text{Cand}([L, R])$ **100% invariant** on fully covered nodes, and maintaining a $\sqrt{N}$-block rolling hash ($O(\sqrt{N})$ update, $O(1)$ query) supports binary-search LCE in $O(\log N)$ time!

#### Compilation C: Static Substring Minimum Suffix ($T = \varepsilon$) via Shortest Border of $\arg\min_{i \in [l, r]} \text{rk}[i]$
For a static string $S$ and query $(l, r)$ asking for the minimum suffix of $S[l..r]$ ($T = \varepsilon$):
- Let $i_0 = \arg\min_{i \in [l, r]} \text{rk}[i]$ (found in $O(1)$ via RMQ on $\text{rk}$), and set $W = S[i_0..r]$.
- Every $j \in [l, r]$ that does not match a prefix of $W$ up to $r$ loses to $W$ at their first mismatch before $r$ because $\text{rk}[i_0] < \text{rk}[j]$.
- Every $j \in [l, r]$ ($j > i_0$) that *does* match a prefix of $W$ up to $r$ is a **proper border** of $W = S[i_0..r]$ (and automatically satisfies $j > i_0 \ge l$, so $j \in [l, r]$!).
- Because all borders of $W$ are prefixes of one another and shorter prefixes win at $T = \varepsilon$, the **lexicographically smallest suffix of $S[l..r]$ is literally the shortest nonempty border of $W = S[i_0..r]$** (or $W$ itself if $W$ is border-free)!

---

### 3.4 Step 4 — Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Counterexample 1 ($S = \texttt{aaba}, [l, r] = [2, 4]$ — Why $\text{Cand}_{\min}(S[l..r]) \not\subseteq \text{Cand}_{\min}(S[1..r])$)**:
   - In $S[1..4] = \texttt{aaba}$, $\texttt{aaba}$ ($i=1$) beats $\texttt{aba}$ ($i=2$) via $\texttt{aaba} \prec \texttt{aba}$, so $\text{Cand}_{\min}(S[1..4]) = \{\texttt{a} (4), \texttt{aaba} (1)\}$.
   - When querying $[l, r] = [2, 4]$ ($S[2..4] = \texttt{aba}$), $i=1$ is out of bounds ($1 < l = 2$), so $\texttt{aba}$ ($i=2$) revives: $\text{Cand}_{\min}(S[2..4]) = \{\texttt{a} (4), \texttt{aba} (2)\} \not\subseteq \text{Cand}_{\min}(S[1..4])$.
   - Even worse, on $S = \texttt{abbb}, [l, r] = [2, 4]$, $\text{Cand}_{\min}(S[1..4]) = \{1\}$, so $\text{Cand}_{\min}(S[1..4]) \cap [2, 4] = \emptyset$!
2. **Counterexample 2 (Appending $+\infty$ vs. $-\infty$ for Maximum Suffix)**:
   - At $T = \varepsilon$, if $u \sqsubset v$, then $u < v$ ALWAYS holds: for **Minimum Suffix**, the shorter suffix $u$ wins; for **Maximum Suffix**, the **longer** suffix $v$ wins! If you naively append $+\infty$ to $S[l..r]$ to find the maximum suffix, then $u + (+\infty) > v + (+\infty)$ falsely makes the shorter prefix $u$ win!

---

### 3.5 Frontier Extension III: Segment-Tree-Free $O(\log N)$ Extraction of $\text{Cand}_{\min}(S[l..r])$ via Dyadic SA-Rank RMQ Bands

How can we compute $\text{Cand}_{\min}(S[l..r])$ in $O(\log(r - l + 1))$ time using **only $O(N)$ space** (no Segment Tree)?
Partition the suffix lengths $[1, r - l + 1]$ into $\le \lfloor \log_2(r-l+1) \rfloor + 1$ dyadic bands $B_k = [2^k, \min(r-l+1, 2^{k+1}-1)]$, corresponding to starting-index intervals $I_k = [\max(l, r - 2^{k+1} + 2),\; r - 2^k + 1]$.
- By Theorem 3.1, $\text{Cand}_{\min}(S[l..r])$ contains **at most one** suffix in each band $I_k$.
- In band $I_k$, query $i_k = \arg\min_{x \in I_k} \text{rk}[x]$ in $O(1)$ time via RMQ on $\text{rk}$.
- Could the true member $x^* \in \text{Cand}_{\min}(S[l..r]) \cap I_k$ have $\text{rk}[x^*] > \text{rk}[i_k]$?
  Only if no mismatch occurs between $S[i_k..r]$ and $S[x^*..r]$ before $r$—meaning $x^* < i_k$ in $I_k$ and $S[i_k..r] \sqsubset S[x^*..r]$!
  In that case, both $u = S[i_k..r]$ and $v = S[x^*..r]$ lie in $B_k = [2^k, 2^{k+1})$, so $|u| < |v| < 2|u|$ and $v$ has period $p = i_k - x^* < |u|$. By Theorem 3.1, only the **longest** periodic extension of $S[i_k..r]$ inside $I_k$ can survive! And what is the period $p$? Since $v = w^2 u'$ contains at least two copies of $w$ ($|v| \ge 2p$), $S[i_k..r]$ itself has shortest period $p = |S[i_k..r]| - |\text{longest\_border}(S[i_k..r])|$ (or is covered by the unique run of period $p \le |S[i_k..r]|$), so shifting $i_k$ left by multiples of $p$ up to the left boundary of $I_k$ (checked by a single $O(1)$ $\text{LCS}(i_k - 1, i_k + p - 1)$ query!) recovers $x^*$ in $O(1)$ time!
- Filtering the $\le \lfloor \log_2(r-l+1) \rfloor + 1$ band representatives from shortest to longest using $O(1)$ LCE constructs the exact set $\text{Cand}_{\min}(S[l..r])$ in **$O(\log(r - l + 1))$ time and $O(N)$ global space**!

---

## Section 4. Reconciled Master Treatise Part III: Lyndon Arrays, Double-Order Monotonic Stacks & The Lyndon Tree

### 4.1 The Next-Smaller-Suffix Characterization of the Lyndon Array $\lambda[1..N]$

For each $i \in [1, N]$, let $\lambda[i]$ be the length of the longest Lyndon prefix of $S[i..N]$, and let $R_{\mathcal{L}}[i] = i + \lambda[i] - 1$ be its right endpoint.

#### Theorem 4.1 (ISA Next-Smaller-Suffix Characterization — Hohlweg & Reutenauer 2003; Franek et al. 2016)
Viewing $S[N+1..N] = \varepsilon$ as strictly smaller than all nonempty suffixes, for every $i \in [1, N]$:
$$\text{nsv}[i] = \min \bigl\{ j \in [i+1, N+1] \;\big|\; S[j..N] < S[i..N] \bigr\}, \qquad R_{\mathcal{L}}[i] = \text{nsv}[i] - 1, \qquad \lambda[i] = \text{nsv}[i] - i.$$

**Two-Way Proof**:
Let $S[i..N] = w_1 w_2 \cdots w_k$ ($w_1 \ge \cdots \ge w_k$) be the CFL factorization of $S[i..N]$; by Corollary 2.2, $w_1 = S[i..r_1]$ ($r_1 = i + \lambda[i] - 1$) is the longest Lyndon prefix of $S[i..N]$.
1. For any $j \in [i+1, r_1]$, $v = S[j..r_1]$ is a nonempty proper suffix of the Lyndon word $w_1$, so Theorem 2.1(3) gives $w_1 \prec v$. By right-extension stability of $\prec$, $S[i..N] = w_1 S[r_1+1..N] \prec v S[r_1+1..N] = S[j..N]$, so $\text{nsv}[i] \ge r_1 + 1$.
2. At $j = r_1 + 1$: if $k = 1$, $S[r_1+1..N] = \varepsilon < S[i..N]$. If $k \ge 2$, suppose $w_1 = \cdots = w_q > w_{q+1}$. Cancelling the common prefix $w_1^{q-1}$ from $S[i..N] = w_1^q w_{q+1}\cdots w_k$ and $S[r_1+1..N] = w_1^{q-1} w_{q+1}\cdots w_k$ compares $w_1 w_{q+1}\cdots w_k$ against $w_{q+1}\cdots w_k$; since $w_{q+1}$ is the longest Lyndon prefix of $w_{q+1}\cdots w_k$ while $w_1 > w_{q+1}$, we have $S[r_1+1..N] < S[i..N]$, so $\text{nsv}[i] = r_1 + 1$. $\blacksquare$

---

### 4.2 Double-Order ($<$ and $>$) Monotonic Stack & The $S = \texttt{bab}$ Negation Trap

To compute $R_{\mathcal{L}, <}[1..N]$ and $R_{\mathcal{L}, >}[1..N]$ in $O(N)$ time, scan $i = N$ down to $1$ maintaining a monotonic stack of indices $i < j_1 < j_2 < \cdots < N+1$ with strictly decreasing suffixes $S[i..N] > S[j_1..N] > \cdots > \varepsilon$.

> [!CAUTION]
> **Critical Bug: Why Negating `rk[i]` (`-rk_<[i]`) Fails for Reversed Order $>$ ($S = \texttt{bab}$ Counterexample)**
> On $S = \texttt{bab}$ ($N = 3$), the suffixes under $<$ are $\texttt{ab} (2) < \texttt{b} (3) < \texttt{bab} (1)$, so $\text{rk}_< = [3, 1, 2]$.
> - If you blindly negate $\text{rk}_<$ to $[-3, -1, -2]$, you claim $S[1..3] = \texttt{bab} <_> S[3..3] = \texttt{b}$, giving $\text{nsv}_>[1] = 4$ and claiming $S[1..3] = \texttt{bab}$ is a $>-$Lyndon word!
> - **FALSE!** $\texttt{bab}$ has border $\texttt{b}$, so it is not Lyndon under *any* order! Because $S[3..3] = \texttt{b}$ is a **proper prefix** of $S[1..3] = \texttt{bab}$, we still have $S[3..3] <_> S[1..3]$ under $(>, -\infty)$, so $\text{nsv}_>[1] = 3$ and $R_{\mathcal{L}, >}[1] = 2$ ($\texttt{ba}$)!
> - **Two Exact $O(N)$ Fixes**:
>   1. Build the second Suffix Array $\text{rk}_>$ on the character-inverted string $\overline{S}[t] = |\Sigma| + 1 - S[t]$ (keeping the end-of-string sentinel $0 = -\infty$), OR
>   2. Use $O(1)$ LCE in the stack comparator: for $\ell = \text{LCP}(i, j)$, if $j + \ell > N$ (since $i < j$), $S[j..N] \sqsubset S[i..N]$ so $S[j..N] <_> S[i..N]$; otherwise compare $S[j+\ell] > S[i+\ell]$.

---

### 4.3 The Lyndon Tree & Min-Cartesian Tree Isomorphism

Let $w = \$S[1..N]$ (where $\$ = -\infty$, making $w$ a Lyndon word of length $N+1$). Recursively applying the **Right-Standard Factorization** $u v$ (where $v$ is the longest proper Lyndon suffix = lexicographically smallest proper suffix of $uv$) builds a full binary tree of $2N + 1$ nodes called the **Lyndon Tree**.

#### Theorem 4.2 (Min-Cartesian Tree Isomorphism — Barcelo 1990; Bannai et al. 2017)
1. For any Lyndon node $S[l..r]$ ($l < r$) in the Lyndon Tree, all proper suffixes $S[j..r]$ ($l < j \le r$) satisfy $S[l..r] \prec S[j..r]$, so their relative order truncated at $r$ is identical to their global Suffix Array order $\text{rk}[j]$. Thus the standard-factorization split point $m$ is:
   $$m = \arg\min_{j \in [l+1, r]} \text{rk}[j].$$
2. Consequently, the internal nodes of the Lyndon Tree of $\$S[1..N]$ are **isomorphic to the Min-Cartesian Tree of $\text{rk}[2..N+1]$**: an internal Cartesian node $m$ with Cartesian subtree range $[L_m, R_m]$ represents the Lyndon word **$S[L_m - 1 .. R_m]$** (with left child $S[L_m - 1 .. m - 1]$ and right child $S[m .. R_m]$), and every right child $S[m..R_m]$ is a right-maximal Lyndon word ($R_m = R_{\mathcal{L}}[m]$)!

---

### 4.4 Frontier Extension IV: Worst-Case $O(\log N)$ Online & Persistent Lyndon Factorization

When characters are appended on a persistent version tree (`append(v, c)`), Duval's three-pointer state cannot afford an $O(N)$ Case-2 collapse on branches like $\texttt{a}^N \texttt{b}$ vs $\texttt{a}^N \texttt{a}$.
- **Right-Spine Binary-Lifting Invariant**: View the CFL factorization of the current prefix as a strictly decreasing stack of blocks $(w_1, d_1) > (w_2, d_2) > \cdots > (w_m, d_m)$ ($w_t \in \mathcal{L}$).
- When appending a single character $c$: push $(c, 1)$ onto the stack. While the top two blocks $(u, d)$ and $v$ satisfy $u < v$ (tested in $O(1)$ via LCE on the persistent tree using SAM or binary-lifting rolling hashes + character lookup), replace them by the single Lyndon word $u^d v$!
- To achieve **worst-case $O(\log N)$ time per append**, note that whenever $u^d v$ is formed:
  - If $d|u| \le |v|$, $|u^d v| \ge 2 d|u|$ doubles the length of the merged suffix.
  - If $d|u| > |v|$, instead of popping one block at a time when a sequence of short blocks merges, store binary-lifting pointers on the CFL stack storing the minimum factor length and lexicographical threshold, jumping directly to the first block on the stack with $w_t \ge$ the merged suffix!

---

## Section 5. Reconciled Master Treatise Part IV: The Runs (`极长周期子串`) Theorem, Three-Squares Lemma & 2D Sweep-Line

### 5.1 Concrete Definition of a Run (`极长周期子串`)

**Definition 5.1 (Run / Maximal Periodic Substring)**. A **run** in $S[1..N]$ is a triple $R = [l, r, p]$ ($1 \le l < r \le N, 1 \le p \le \lfloor (r-l+1)/2 \rfloor$) such that:
1. **(Primitive Period & Exponent $\ge 2$)**: $p$ is the **shortest (primitive) period** of $S[l..r]$, and $\text{exp}(R) = \frac{r - l + 1}{p} \ge 2$.
2. **(Left-Maximality)**: Either $l = 1$, or $S[l-1] \ne S[l-1+p]$.
3. **(Right-Maximality)**: Either $r = N$, or $S[r+1] \ne S[r+1-p]$.

Let $\mathcal{R}(S)$ denote the set of all runs of $S$.

---

### 5.2 Complete Lyndon-Root Proof of $|\mathcal{R}(S)| < N$, $\sum \text{exp}(R) < 3N$ & The $< 2N$ Representative Squares Lemma

#### Step 1: Canonical Order Assignment $<_R \in \{<_0, <_1\}$ via Right-Maximality
Append $S[N+1] = -\infty$ (smaller than all characters in $\Sigma$ under **both** $<_0 = (<)$ and $<_1 = (>)$). For each run $R = [l, r, p] \in \mathcal{R}(S)$:
- If $r = N$, $S[N+1] = -\infty <_0 S[N+1-p]$ (and $<_1$); assign $<_R = <_0$.
- If $r < N$, right-maximality guarantees $S[r+1] \ne S[r+1-p]$; assign $<_R \in \{<_0, <_1\}$ to be the **unique order** under which
  $$S[r+1] <_R S[r+1-p].$$

#### Step 2: Interior $L$-Roots in $[l+1, l+p]$ & Exact Right-Maximality $\lambda_{<_R}[i] = p$
An **$L$-root** of $R = [l, r, p]$ is any length-$p$ substring $S[i..i+p-1]$ ($l \le i \le r - p + 1$) that is a Lyndon word under $<_R$.
- **Why every run has an interior $L$-root starting in $[l+1, l+p]$**: Because $p$ is primitive and $r - l + 1 \ge 2p$, the window $[l+1, l+p]$ of size $p$ lies entirely inside $[l, r - p + 1]$ and contains all $p$ distinct cyclic shifts of the period block; the unique $<_R$-smallest among them is an $L$-root $S[i..i+p-1]$ with **$i \in [l+1, l+p] \subseteq [2, N]$**!
- **Why $\lambda_{<_R}[i] = p$ for every $L$-root of $R$**: Inside $S[i..r]$, the Lyndon word $w = S[i..i+p-1]$ repeats as a pre-Lyndon word $S[i..r] = w^d w'$. At index $r + 1$, the periodic continuation predicts $S[r+1-p]$, whereas the actual character is $S[r+1] <_R S[r+1-p]$. This triggers **Duval's Case 3** at $r + 1$, freezing the longest $<_R$-Lyndon prefix starting at $i$ to be a single period $w = S[i..i+p-1]$:
  $$R_{\mathcal{L}, <_R}[i] = i + p - 1, \qquad \lambda_{<_R}[i] = p!$$

```
Run R = [l, r, p] with right-mismatch S[r+1] <_R S[r+1-p]:
l     i         i+p       i+2p           r   r+1
|-----|----w----|----w----|----...-------|---|
      [    w    ][   w    ][  w'  ]       S[r+1] <_R S[r+1-p]
      |<-- p -->|                         ^
      Lyndon under <_R (i >= l+1)         Triggers Duval Case 3!
      Last char w[p] = S[i+p-1] = S[i-1]  ===> \lambda_{<_R}[i] = p!
```

#### Step 3: Mutual Exclusion $S[i] <_R S[i-1]$ at Every $i \in [2, N]$
Let $B(R) = \{ i \in [l+1, r - p + 1] \mid S[i..i+p-1] \text{ is an } L\text{-root of } R \text{ under } <_R \}$. We just showed $|B(R)| \ge 1$ and $B(R) \subseteq \{2, \dots, N\}$.
Can two distinct runs $R_1, R_2$ share an index $i \in B(R_1) \cap B(R_2)$?
1. **Same Order ($<_{R_1} = <_{R_2} = <_\ell$)**: Then $p_1 = \lambda_{<_\ell}[i] = p_2 = p$, and since $i \ge l_1 + 1, l_2 + 1$, both runs contain $S[i-1..i+p-1]$ of length $p + 1 > p$ with period $p$, forcing $R_1 = R_2$.
2. **Opposite Orders ($<_0$ vs. $<_1$) at the Same $i \in \{2, \dots, N\}$**: Because $i \ge l + 1$, the index $i - 1 \ge l$ lies **inside the run $R$**, so by periodicity $S[i - 1] = S[i + p - 1]$ is the **last character** of the Lyndon word $w = S[i..i+p-1]$!
   - If $p \ge 2$: by Theorem 2.1(2), the first character $w[1] = S[i]$ of a Lyndon word of length $\ge 2$ is strictly smaller than its last character $w[p] = S[i+p-1] = S[i-1]$:
     $$S[i] <_R S[i-1]!$$
     Since $S[i] < S[i-1]$ and $S[i] > S[i-1]$ are mutually exclusive, at most **one** of $<_0, <_1$ can have an $L$-root of length $\ge 2$ at $i$!
   - If $p = 1$: then $S[i] = S[i-1]$, so no $p \ge 2$ Lyndon word can start at $i$, and a unary run $[l, r, 1]$ is only assigned to one order $<_R$.
Therefore, the sets $\{B(R)\}_{R \in \mathcal{R}(S)}$ are **pairwise disjoint subsets of $\{2, 3, \dots, N\}$**!

#### Theorem 5.2 (The Runs Theorem & Representative Squares Bounds — Bannai et al. 2017)
For every string $S[1..N]$ of length $N \ge 1$:
1. **Total Number of Runs**:
   $$|\mathcal{R}(S)| \le \sum_{R \in \mathcal{R}(S)} |B(R)| \le N - 1 < N.$$
2. **Sum of Exponents**: Since $|B(R)| = \lfloor \text{exp}(R) - 1 \rfloor > \text{exp}(R) - 2$ and $|B(R)| \ge 1 \implies \text{exp}(R) < 3|B(R)|$,
   $$\sum_{R \in \mathcal{R}(S)} \text{exp}(R) < 3N, \qquad \text{and} \qquad \sum_{R \in \mathcal{R}(S)} \left\lfloor \frac{\text{exp}(R)}{2} \right\rfloor < 1.5N.$$
3. **Primitively Rooted Square Starting Positions & The $< 2N$ Representative Squares Lemma**:
   - In each run $R = [l, r, p]$, every full period window $[a, a+p-1]$ inside $[l+1, r-p+1]$ contains an interior $L$-root under **both** $<_0$ and $<_1$ (except when $p = 1$). Summing interior $L$-roots across both orders proves that the total number of starting positions of primitively rooted squares $S[a..a+2p-1]$ ($l \le a \le r - 2p + 1$) satisfies:
     $$\sum_{R = [l, r, p] \in \mathcal{R}(S)} (r - l + 1 - 2p + 1) \le 2(N - 1) < 2N \quad (\text{and } \le N - 1 \text{ for } p \ge 2).$$
   - **Corollary (The $< 2N$ Representative Squares Lemma)**: For each run $R = [l, r, p]$ and each harmonic $k \ge 1$ ($2kp \le r - l + 1$), two squares of length $2kp$ inside $R$ starting at $a_1, a_2$ are identical strings iff $a_1 \equiv a_2 \pmod p$. Thus the canonical representatives of distinct squares generated by $(R, k)$ are the first $\min(p, r - l + 1 - 2kp + 1)$ starting positions $a \in [l, \min(l + p - 1, r - 2kp + 1)]$. Since each such $(R, k, a)$ injects into the distinct primitive-square start position $a_k = a + 2(k-1)p \in [l, r - 2p + 1]$, **the total number of canonical square representatives $(R, k, a)$ across ALL runs and ALL harmonics $k \ge 1$ is strictly less than $2N$**!

---

### 5.3 The Three-Squares Lemma & Exact Enumeration Algorithms

#### Theorem 5.3 (Crochemore–Rytter Three-Squares Lemma, 1995)
If $u^2, v^2, w^2$ are three prefixes of a string $S$ with $0 < |u| < |v| < |w|$ and **$u$ is primitive**, then
$$|w| \ge |u| + |v|.$$
*Proof*: If $|w| < |u| + |v|$, the second copy of $v$ in $v^2$ and the second copy of $w$ in $w^2$ force $u^2$ (of length $2|u|$) to have period $d = |w| - |v| < |u|$. By the Weak Periodicity Lemma on $u^2$ ($2|u| \ge |u| + d$), $u$ has period $\gcd(|u|, d) < |u|$, contradicting that $u$ is primitive! $\blacksquare$

#### Two Canonical Runs Enumeration Kernels
1. **Method A: $O(N \log N)$ Harmonic LCE-Gluing (`[NOI2016] 优秀的拆分`)**:
   - For each $p = 1 \dots \lfloor N/2 \rfloor$ and checkpoint pair $(kp, (k+1)p)$, compute $L_1 = \text{LCS}(kp, (k+1)p)$ and $L_2 = \text{LCP}(kp, (k+1)p)$. If $L_1 + L_2 - 1 \ge p$, record $[kp - L_1 + 1, (k+1)p + L_2 - 1, p]$. Sort by $(l, r, p)$ and keep only the **smallest** $p$ for each $(l, r)$ (since non-primitive multiples $kp$ also trigger checkpoint matches!).
2. **Method B: $O(N)$ Lyndon-Array Enumeration (Bannai et al. 2017 / Jin Ce 2019)**:
   - Compute $R_{\mathcal{L}, <}[1..N]$ and $R_{\mathcal{L}, >}[1..N]$ in $O(N)$ via the Double-Order Monotonic Stack (Section 4.2).
   - For each order $\prec \in \{<, >\}$ and $i \in [1, N]$: let $j = R_{\mathcal{L}, \prec}[i], p = j - i + 1$, $l = i - \text{LCS}(i - 1, j)$, $r = j + \text{LCP}(i, j + 1)$. If $r - l + 1 \ge 2p$, record $[l, r, p]$ (note $p = |w|$ is automatically primitive because Lyndon words are border-free!). Radix-sort and deduplicate identical triples $[l, r, p]$ in $O(N)$ time.

---

### 5.4 Frontier Extension V: The Fraenkel–Simpson $\le 2N$ and Brlek–Li $\le N - \Theta(\log N)$ Distinct Squares Hierarchy

Why can a string $S[1..N]$ contain **at most $2N$ distinct square substrings** $w^2$ (including non-primitive squares)?
- **Direct Proof from the Three-Squares Lemma (Fraenkel & Simpson 1998; Ilie 2005)**:
  For each distinct square substring $X = w^2$ occurring in $S$, look at its **rightmost (last) starting position** $i_{\text{last}}(X) \in [1, N]$. Suppose three distinct squares $u^2, v^2, w^2$ with $|u| < |v| < |w|$ all had their **last** occurrence starting at the exact same index $i$!
  - Since $u^2$ and $w^2$ are both prefixes of $S[i..N]$ with $|u| < |w|$, if $|w| < 2|u|$ (or even if $|w| \ge |u| + |v|$: look at the second copy of $w$ starting at $i + |w|$!), the prefix of $w$ of length $2|u|$ (if $2|u| \le |w|$) equals $u^2$, which means $u^2$ **also occurs at $i + |w| > i$**, contradicting that $i$ was the *last* occurrence of $u^2$!
  - And if $|w| < 2|u|$, then $|u| < |v| < |w| < 2|u|$ forces $u$ to be non-primitive ($u = z^k$) by the Three-Squares Lemma, in which case $u^2 = z^{2k}$ shifts by $|z| \le |w| - |u|$ inside $w^2$ to occur again at $i + |z| > i$, again contradicting that $i$ is the last occurrence of $u^2$!
  - Therefore, **at most 2 distinct squares can have their last occurrence starting at any index $i \in [1, N]$**, immediately proving $\#\{\text{distinct squares in } S\} \le 2N - 2$! (Subsequently tightened to $\le \frac{11}{6}N$ by Deza–Franek–Thierry 2015 and $\le N - \Theta(\log N)$ by Brlek–Li 2022).

---

## Section 6. Master Reconciled Problem Archive: 42 Accepted Non-Template Problems (`W1B-01`–`W1B-42`) & 10 Quarantined Templates (`R-1B-01`–`R-1B-10`)

Every accepted problem below is deduplicated across Cohort 1 (`P-1B-01..32`) and Cohort 2 (`Problem 1..32`), assigned a canonical Wave 1B ID (`W1B-01`–`W1B-42`), and equipped with the complete **4-Step Zero-Magic Analysis**.

---

### Tier 1: Stepping Stone (10 Problems — `W1B-01` to `W1B-10`)

#### **`W1B-01`. `[NOI2016] 优秀的拆分 (Excellent Split)` (Luogu P1117 / UOJ 219 / LOJ 2083)** — `[ZH]` *(Cohort 1 `P-1B-02` + Cohort 2 `#1`)*
- **Inline Mathematical Statement & Constraints**: Given $T \le 10$ testcases of strings $S[1..N]$ ($\sum N \le 3 \times 10^4$), count the number of ways to split a substring of $S$ into $AABB$ ($A, B \in \Sigma^+$), i.e., compute $\sum_{i=1}^{N-1} f[i] \cdot g[i+1]$ where $f[i]$ is the number of squares $AA$ ending at $i$ and $g[j]$ is the number of squares $BB$ starting at $j$. Time limit $1.5\text{ s}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Testing all $O(N^2)$ substrings for $AA$ takes $O(N^2)$ time; we need an $O(N \log N)$ (or $O(N)$) batch mark of all square start/end intervals.
  2. *Combinatorial Word Invariant*: Every square $AA$ of length $2p$ covers **at least one** adjacent pair of multiples $(kp, (k+1)p)$ of $p$, and if we clamp the left/right extensions from $(kp, (k+1)p)$ to at most $p$, each square of length $2p$ covers **exclusively one** pair $(kp, (k+1)p)$.
  3. *Reverse-Engineering Scratchpad*: For each $p = 1 \dots \lfloor N/2 \rfloor$ and $k = 1 \dots \lfloor N/p \rfloor - 1$, query $L_1 = \min(p, \text{LCS}(kp, (k+1)p))$ and $L_2 = \min(p, \text{LCP}(kp, (k+1)p))$ in $O(1)$ via SA + RMQ on $S$ and $S^R$. Whenever $L_1 + L_2 - 1 \ge p$, increment $g[\cdot]$ on $[kp - L_1 + 1,\; kp + L_2 - p]$ and $f[\cdot]$ on $[(k+1)p - L_1 + p,\; (k+1)p + L_2 - 1]$ via difference arrays in $O(1)$. Total time: $O(N \log N)$.
  4. *Boundary Pitfalls*: Forgetting to clamp $L_1 \gets \min(L_1, p)$ and $L_2 \gets \min(L_2, p)$ causes a run of length $\ge 3p$ to count the same square of length $2p$ across multiple checkpoint pairs.

---

#### **`W1B-02`. Codeforces 1537E2 — `Erase and Extend (Hard Version)`** — `[EN]` *(Cohort 2 `#4`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$) and target length $K \le 5 \times 10^5$, you may repeatedly delete the last character of $S$ or duplicate $S \gets S + S$. Find the lexicographically smallest string of length $K$ obtainable. Time limit $2.0\text{ s}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Duplicating a prefix $S[1..p]$ yields the infinite periodic word $(S[1..p])^\omega$ truncated to length $K$. Comparing all $N$ prefixes naively takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: Run Duval's first-phase pointer loop from $i = 1$ (under reversed alphabet $>$ since we want $(S[1..p])^\omega$ to be minimal, i.e., any drop $S[k] < S[j]$ improves the period to $p = k$, while any rise $S[k] > S[j]$ means $(S[1..p])^d w' S[k] \succ (S[1..p])^\omega$, permanently ruling out all prefixes of length $\ge k$!).
  3. *Reverse-Engineering Scratchpad*: Initialize best period $p = 1$. For $k = 2 \dots N$, compare $S[k]$ against $S[j]$ where $j = ((k - 1) \bmod p) + 1$: if $S[k] < S[j]$, update $p \gets k$; if $S[k] > S[j]$, `break` immediately! Output $(S[1..p])^\omega[1..K]$ in $O(N + K)$ time and $O(1)$ space.
  4. *Boundary Pitfalls*: When $S[k] == S[j]$, do **not** update $p \gets k$; keeping the shorter period $p$ prevents an incomplete tail $w'$ from wrapping around to $S[1]$ prematurely at index $k + 1$.

---

#### **`W1B-03`. `[JSOI2019] 节日庆典 (Festival Celebration)` (Luogu P5287 / LOJ 3051)** — `[ZH]` *(Cohort 1 `P-1B-01` + Cohort 2 `#14`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^6$), for every prefix $S[1..r]$ ($1 \le r \le N$), find the starting index $i \in [1, r]$ of the lexicographically smallest cyclic shift $S[i..r] + S[1..i-1]$ (tie-breaking by smallest index $i$). Time limit $1.0\text{ s}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Running Duval on $S[1..r] + S[1..r]$ for each $r$ takes $O(N^2)$ time; $N = 3 \times 10^6$ also forbids Suffix Arrays.
  2. *Combinatorial Word Invariant*: Minimizing the cyclic shift $S[i..r] + S[1..i-1]$ of length $r$ is order-equivalent to minimizing $S[i..r] + T$ where the right-extension is $T = S[1..r]$ (independent of $i$!). By **Theorem 3.1 (Significant Suffixes)**, the optimal suffix $S[i..r]$ must belong to $\text{Cand}_{\min}(S[1..r])$, which has size $\le \lfloor \log_2 r \rfloor + 1 \le 22$.
  3. *Reverse-Engineering Scratchpad*: Precompute the Z-array $Z[1..N]$ of $S$ in $O(N)$ time. Maintain $\text{Cand}_{\min}(S[1..r])$ online via Compilation A (Section 3.3). At step $r$, compare the $\le 22$ candidates in $\text{Cand}_{\min}(S[1..r])$ pairwise: for $u \sqsubset v$ ($i_v < i_u$), their first $|u|$ characters match, so comparing $u S[1..i_u-1]$ vs $v S[1..i_v-1]$ reduces to **at most two $O(1)$ Z-array lookups** ($Z[r - |v| + |u| + 1]$ and $Z[|v| - |u| + 1]$)!
  4. *Boundary Pitfalls*: On a tie ($u S[1..i_u-1] = v S[1..i_v-1]$), the problem asks for the **smallest starting index $i$** (the longer suffix $v$). Because Theorem 3.1 only eliminates the *middle* element $u = wu'$ while keeping the longest element $v = w^2 u'$ on the stack, the smallest index $i$ is never lost!

---

#### **`W1B-04`. AtCoder ARC 060 F (ABC 044 D) — `Best Representation`** — `[JA]` *(Cohort 1 `P-1B-04` + Cohort 2 `#5`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), call a string "good" if it is primitive (not of the form $u^k$ for $k \ge 2$). Find the minimum number of good substrings into which $S$ can be partitioned, and the number of such minimal partitions modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A substring $W$ is non-primitive iff its shortest period $p = |W| - \pi(|W|)$ satisfies $p < |W|$ and $p \mid |W|$.
  2. *Combinatorial Word Invariant*: By Fine–Wilf, if $S$ itself is primitive, the answer is $(1, 1)$; if $S = c^N$, the answer is $(N, 1)$; otherwise $S = u^k$ ($k \ge 2, |u| \ge 2$), and cutting off a single character $S[1..1] + S[2..N]$ already yields two primitive parts, so the minimum number of parts is **always $2$**!
  3. *Reverse-Engineering Scratchpad*: Run KMP on $S$ and $S^R$ in $O(N)$ to mark all non-primitive prefixes $S[1..i]$ and non-primitive suffixes $S[i+1..N]$, then count $i \in [1, N-1]$ where both pieces are primitive.
  4. *Boundary Pitfalls*: Checking $\pi(i) \ge i/2$ without checking $(i - \pi(i)) \mid i$ falsely flags bordered primitive strings (like $\texttt{aba}$) as periodic.

---

#### **`W1B-05`. AtCoder ARC 050 D — `Suffix Concat`** — `[JA]` *(Cohort 2 `#2`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), find a permutation $\pi$ of $\{1, \dots, N\}$ that minimizes the concatenation $S[\pi(1)..N] + S[\pi(2)..N] + \cdots + S[\pi(N)..N]$ lexicographically.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Sorting suffixes by standard SA rank $\text{rk}[i]$ fails when one suffix is a proper prefix of another (e.g., $A = \texttt{ba}, B = \texttt{baa}$ has $A < B$ but $BA = \texttt{baaba} < AB = \texttt{baba}$).
  2. *Combinatorial Word Invariant*: By CFL concatenation ordering, $A + B < B + A \iff A^\omega < B^\omega$. For two suffixes $A = S[i..N]$ and $B = S[j..N]$ ($|A| > |B|$), comparing $AB$ vs $BA$ splits into comparing three substring pairs of $S$ of total length $|A| + |B|$.
  3. *Reverse-Engineering Scratchpad*: Precompute SA + LCP RMQ in $O(N)$, and sort $\{1, \dots, N\}$ using the 3-step $O(1)$ LCE comparator (1: $S[i..]$ vs $S[j..]$ up to $|B|$; 2: $S[i+|B|..]$ vs $S[i..]$ up to $|A|-|B|$; 3: $S[j..]$ vs $S[i+|A|-|B|..]$ up to $|B|$) in $O(N \log N)$ time.
  4. *Boundary Pitfalls*: Forgetting step 3 when $|A| - |B| < |B|$ stops the comparison before reaching the end of $AB$ vs $BA$.

---

#### **`W1B-06`. POJ 3693 — `Maximum Repetition Substring`** — `[EN]` *(Cohort 2 `#6`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), find a substring $S[l..r]$ maximizing the integer repetition exponent $k = \lfloor (r - l + 1)/p \rfloor$, breaking ties by lexicographically smallest substring $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Every $k$-power $u^k$ is contained in a run $R = [L, R, p]$ of exponent $\ge k$.
  2. *Combinatorial Word Invariant*: Inside a run $R = [L, R, p]$ achieving $k_{\max} = \lfloor (R - L + 1)/p \rfloor$, valid starting positions of $u^{k_{\max}}$ form the contiguous window $a \in [L,\; R - k_{\max} p + 1]$, and among them the lexicographically smallest string $S[a..a+k_{\max}p-1]$ is the one minimizing $\text{rk}[a]$.
  3. *Reverse-Engineering Scratchpad*: Find all runs (or harmonic LCE checkpoints), compute $k_{\max}$, and for each run achieving $k_{\max}$, query $\arg\min_{a \in [L, R - k_{\max}p + 1]} \text{rk}[a]$ in $O(1)$ via RMQ on $\text{rk}$.
  4. *Boundary Pitfalls*: Because the window $[L,\; R - k_{\max}p + 1]$ has length $(R - L + 1) \bmod p + 1 \le p$, it may not contain all $p$ cyclic shifts of the period, so the global $<$-Lyndon root of $R$ can fall outside $[L, R - k_{\max}p + 1]$; querying RMQ on $\text{rk}[L..R-k_{\max}p+1]$ avoids out-of-window roots.

---

#### **`W1B-07`. AtCoder ABC 272 F — `Two Strings`** — `[JA]` *(Cohort 2 `#8`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ and $T[1..N]$ ($N \le 2 \times 10^5$), count pairs $(i, j) \in [1, N]^2$ such that the $i$-th cyclic shift of $S$ is lexicographically $\le$ the $j$-th cyclic shift of $T$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Comparing suffixes in $S + S + \# + T + T + \$$ breaks ties using characters past offset $N$ when two cyclic shifts are equal.
  2. *Combinatorial Word Invariant*: Appending $\texttt{a}^N$ after $S+S$ and $\texttt{z}^N$ after $T+T$ (or clamping LCP at $N$) guarantees that whenever a cyclic shift of $S$ and a cyclic shift of $T$ agree on all $N$ characters ($\text{LCP} \ge N$), the $S$-shift always precedes the $T$-shift in the Suffix Array!
  3. *Reverse-Engineering Scratchpad*: Build SA on $S + S + \texttt{a}^N + T + T + \texttt{z}^N$ in $O(N)$ and sweep SA counting how many valid $S$-starts $i \in [1, N]$ precede each $T$-start $j \in [1, N]$.
  4. *Boundary Pitfalls*: Using a single character $\texttt{a}$ and $\texttt{z}$ instead of $\texttt{a}^N$ (or clamping LCP at $N$) fails when $S[i..i+N-1] = T[j..j+N-1]$ but $S[(i \bmod N)+1] > T[(j \bmod N)+1]$ at the $(N+1)$-st character inside $S+S$ vs $T+T$!

---

#### **`W1B-08`. Luogu P4916 / Universal Cup — `Duval Next-Lyndon & Lexicographically Smallest De Bruijn Sequence`** — `[ZH]`/`[EN]` *(Cohort 1 `P-1B-06`)*
- **Inline Mathematical Statement & Constraints**: Construct the lexicographically smallest De Bruijn sequence of order $N$ over alphabet $\Sigma$ (or answer $K$-th character / necklace Burnside queries).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: An explicit De Bruijn graph has $\sigma^N$ vertices, which cannot be stored in memory when $\sigma^N \sim 10^7$ and $O(1)$ space is required.
  2. *Combinatorial Word Invariant*: By the **Fredricksen–Maiorana Theorem (1978)**, concatenating all Lyndon words whose length divides $N$ in lexicographical order produces the **exact lexicographically smallest De Bruijn cycle** of length $\sigma^N$!
  3. *Reverse-Engineering Scratchpad*: Iterate through all Lyndon words of length $\le N$ in $O(1)$ amortized time per word using **Duval's Next-Lyndon algorithm** (Section 2.4): repeat $w$ to length $N$, strip trailing $\max \Sigma$, increment the last character, and emit $w$ whenever $|w| \mid N$.
  4. *Boundary Pitfalls*: Emitting Lyndon words of lengths $d \nmid N$ destroys the $N$-mer window bijectivity.

---

#### **`W1B-09`. Codeforces 1051E — `Vasya and Big Integers`** — `[EN]` *(Cohort 1 `P-1B-07`)*
- **Inline Mathematical Statement & Constraints**: Given digit strings $A, L, R$ ($|A| \le 10^6$), count valid partitions of $A$ into decimal integers (no leading zeros except `"0"`) each lying numerically in $[L, R]$ modulo $998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Numerical comparison of equal-length digit strings is pure lexicographical comparison.
  2. *Combinatorial Word Invariant*: $A[i..i+|L|-1] \ge L$ is decided in $O(1)$ by the single mismatch character at offset $\ell = \text{LCP}(A[i..], L)$.
  3. *Reverse-Engineering Scratchpad*: Compute Z-arrays on $L + \# + A$ and $R + \# + A$ in $O(|A| + |L| + |R|)$ to determine the exact valid transition length window $[|L| + \delta_L,\; |R| - \delta_R]$ at each index $i$, and maintain prefix sums of DP.
  4. *Boundary Pitfalls*: When $A[i] = \texttt{'0'}$, the only valid piece starting at $i$ is the single digit `"0"` (length $1$, valid iff $L = \texttt{"0"}$).

---

#### **`W1B-10`. Universal Cup / QOJ — `Lyndon Array & CFL Factorization Reconstruction`** — `[EN]`/`[ZH]` *(Cohort 1 `P-1B-08`)*
- **Inline Mathematical Statement & Constraints**: Given the Lyndon array $\lambda[1..N]$ (or the Lyndon Tree structure) of an unknown string $S[1..N]$, determine the minimum alphabet size $\sigma$ required to realize $\lambda[1..N]$ and construct the lexicographically smallest valid string $S$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: By Theorem 4.1, $\lambda[i] = \text{nsv}[i] - i$ encodes the exact Next-Smaller-Element forest of the inverse suffix array $\text{rk}[1..N]$.
  2. *Combinatorial Word Invariant*: First verify that the intervals $[i, i + \lambda[i] - 1]$ are laminar (never cross properly). Then the Next-Smaller-Element tree / Min-Cartesian Tree uniquely determines a canonical suffix rank permutation $\text{rk}[1..N]$ (breaking ties among siblings from left to right so $S[j..N] < S[i..N]$ for $j = i + \lambda[i]$).
  3. *Reverse-Engineering Scratchpad*: Reconstruct $\text{SA}[1..N]$ and $\text{rk}[1..N]$ from the Cartesian tree in $O(N)$ time, then greedily assign characters along $\text{SA}[1..N]$: $S[\text{SA}[t]]$ must strictly exceed $S[\text{SA}[t-1]]$ iff $\text{rk}[\text{SA}[t-1]+1] > \text{rk}[\text{SA}[t]+1]$. Finally, verify that the reconstructed $S$ reproduces $\lambda[1..N]$.
  4. *Boundary Pitfalls*: Non-laminar intervals ($i < j \le i + \lambda[i] - 1 < j + \lambda[j] - 1$) are immediately impossible because a right-maximal Lyndon word cannot cross a boundary where $S[i + \lambda[i]..N] < S[i..N] < S[j..N]$.

---

### Tier 2: Intermediate (11 Problems — `W1B-11` to `W1B-21`)

#### **`W1B-11`. Codeforces 594E — `Cutting the Line`** — `[EN]` *(Cohort 1 `P-1B-03` + Cohort 2 `#12`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^6$) and $k \le N$, partition $S$ into at most $k$ nonempty contiguous substrings and optionally reverse each piece independently to minimize the resulting concatenated string lexicographically. Time limit $2.0\text{ s}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $N = 5 \times 10^6$ requires strictly $O(N)$ algorithms (Duval + Z-algorithm). Reversing a prefix of $S$ is equivalent to detaching a suffix of $T = S^R$ and placing it at the front.
  2. *Combinatorial Word Invariant*: In the CFL factorization $T = S^R = w_1^{d_1} w_2^{d_2} \cdots w_r^{d_r}$ ($w_1 > w_2 > \cdots > w_r$), Corollary 2.2 guarantees that the lexicographically smallest suffix of $T$ is $w_r$, and detaching the entire equal-factor block $B_r = w_r^{d_r}$ at once uses only **one** reversal cut in $S$! Furthermore, if $|w_r| = |w_{r-1}| = 1$, consecutive single-character Lyndon blocks correspond to an **unreversed** prefix of $S$ and merge into a single cut!
  3. *Reverse-Engineering Scratchpad*:
     1. Factor $T = S^R$ via Duval in $O(N)$ and coalesce equal adjacent factors into blocks $B_1, \dots, B_r$.
     2. Greedily peel $B_r$ from the end of $T$ while $k \ge 3$ (decrementing $k$ unless merging adjacent length-$1$ blocks).
     3. When $k = 2$ remains on a prefix $S'[1..m]$, take the lexicographical minimum of four $O(m)$ candidates: (A) $S'$ unreversed; (B) $T' = (S')^R$ fully reversed; (C) Reverse prefix + Unreversed suffix: minimize $(S'[1..i])^R + S'[i+1..m]$ via Z-array on $T' + S'$ (or Duval first-phase); (D) Unreversed prefix + Reversed suffix: test cutting after the last CFL block $B_r$ and (if $B_r \sqsubset B_{r-1}$) after $B_{r-1} B_r$.
  4. *Boundary Pitfalls*: Failing to merge consecutive $|w_t| = 1$ blocks wastes cuts on 1-character reversals; in Case (D) with $k=2$, failing to test both $B_r$ and $B_{r-1} B_r$ when $B_r \sqsubset B_{r-1}$ misses the case where the unreversed tail breaks the tie in favor of $B_{r-1} B_r$.

---

#### **`W1B-12`. Luogu P6127 / `[国家集训队论文 2019 — 金策]` — `All-Prefix CFL Factorization, Minimum Suffix & Maximum Suffix in O(N)`** — `[ZH]` *(Cohort 1 `P-1B-20` + Cohort 2 `#11`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6$ or $5 \times 10^6$), compute in $O(N)$ time for every prefix $S[1..r]$ ($1 \le r \le N$): (a) the number of CFL factors and sum of right endpoints of $S[1..r]$, (b) the starting position of the lexicographically smallest suffix of $S[1..r]$, and (c) the starting position of the lexicographically largest suffix of $S[1..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Running Duval from scratch on each prefix $S[1..r]$ takes $O(N^2)$ time.
  2. *Combinatorial Word Invariant*: By **Theorem 2.4 (All-Prefix CFL State Sharing)**, when Duval's inner scan is at $r$ with active pre-Lyndon block $S[i..r] = w^d w'$ ($p = |w|, d = \lfloor (r-i+1)/p \rfloor$), the incomplete remainder $w' = S[i+dp..r]$ is identical to $S[i..r-dp]$ (visited at step $r' = r - dp$ in the same outer phase!). Meanwhile, under reversed alphabet $>$, the longest pre-$>-$Lyndon suffix starting at the outer pointer $i$ is the **lexicographically largest suffix** of $S[1..r]$!
  3. *Reverse-Engineering Scratchpad*:
     - Run Duval under $<$ to maintain `cnt[r] = (|w'| == 0 ? cnt[i-1] + d : cnt[r - d*p] + d)` and `min_suf[r] = (|w'| == 0 ? r - p + 1 : min_suf[r - d*p] + d*p)`.
     - Run Duval under $>$ and record `max_suf[r] = i` (the active outer pointer at the moment index $r$ is matched/extended).
  4. *Boundary Pitfalls*: When $(r - i + 1) \bmod p == 0$ ($|w'| = 0$), reading from $r - d \cdot p = i - 1$ would shift an old factor from *before* $i$; handle $|w'| = 0$ explicitly as $d$ copies of $w$.

---

#### **`W1B-13`. `[ZJOI2017] 字符串 (Strings)` (LOJ 2257 / UOJ 296 / Luogu P4323)** — `[ZH]` *(Cohort 1 `P-1B-09` + Cohort 2 `#17`)*
- **Inline Mathematical Statement & Constraints**: Given an integer string $S[1..N]$ ($N, Q \le 2 \times 10^5$), support:
  1. `1 l r d`: Add $d$ to $S[k]$ for all $k \in [l, r]$.
  2. `2 l r`: Find the starting position $i \in [l, r]$ of the **lexicographically largest suffix** of $S[l..r]$. Time limit $4.0\text{ s}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Dynamic range additions shift relative character values across segment boundaries, invalidating any static SA or SAM.
  2. *Combinatorial Word Invariant*: By **Theorem 3.1 (Significant Suffixes)** and **Theorem 3.2 (The `pushup` 1-Survivor Theorem)**, each Segment Tree node $[L, R]$ only needs to store $\text{Cand}_{\max}([L, R])$ of size $\le \lfloor \log_2(R - L + 1) \rfloor + 1$, where `pushup` retains all candidates from `right_child` and at most **one** tournament winner $x^*$ from `left_child`! Better still, adding $+d$ to every character inside $[L, R]$ preserves all internal comparisons and leaves $\text{Cand}_{\max}([L, R])$ **100% unchanged** on fully covered nodes!
  3. *Reverse-Engineering Scratchpad*:
     - Maintain a $\sqrt{N}$-block decomposition with polynomial rolling hashes ($O(\sqrt{N})$ per range addition update, $O(1)$ per substring hash query) so binary-search LCE between any two substrings takes $O(\log N)$ time.
     - Maintain the Segment Tree of $\text{Cand}_{\max}([L, R])$. Each update recomputes `pushup` on $O(\log N)$ ancestors ($O(\log^3 N)$ total per update); each query $(l, r)$ gathers the $O(\log^2 N)$ candidates from the $O(\log N)$ canonical nodes and finds the winner at right boundary $r$ ($T = \varepsilon$) in $O(\log^3 N)$ time.
  4. *Boundary Pitfalls*: At the query right boundary $r$ ($T = \varepsilon$), if $\text{LCP}(i, j) \ge r - j + 1$ ($i < j \le r$), then $S[j..r] \sqsubset S[i..r]$, so for **Maximum Suffix**, the **longer** suffix $i$ beats the shorter suffix $j$ ($S[i..r] > S[j..r]$).

---

#### **`W1B-14`. Codeforces 1043G — `Speckled Band`** — `[EN]` *(Cohort 1 `P-1B-10`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$, $|\Sigma| \le 26$) and $Q \le 2 \times 10^5$ queries $[l, r]$, find the minimum number of distinct strings in a partition of $S[l..r]$ into $k \ge 2$ contiguous pieces such that at least two pieces are equal (or $-1$ if no such partition exists).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Whenever two identical characters exist in $S[l..r]$ at $x < y$, the 4-piece partition $S[l..x-1] \mid S[x] \mid S[x+1..y-1] \mid S[y] \mid S[y+1..r]$ (merging $S[y..r]$ if needed, or splitting around $x, y$) uses at most **4** distinct pieces!
  2. *Combinatorial Word Invariant*: Exact classification into $\{-1, 1, 2, 3, 4\}$:
     - **$-1$**: All characters in $S[l..r]$ are distinct (only possible if $r - l + 1 \le 26$).
     - **$1$**: $S[l..r] = A^k$ ($k \ge 2$), checked by testing prime divisors $p \mid (r - l + 1)$ via $O(1)$ LCE.
     - **$2$**: $S[l..r] = AAB$ (starts with a square), $BAA$ (ends with a square), or $ABA$ (has a nonempty proper border).
     - **$3$**: $S[l]$ appears again in $S[l+1..r]$, $S[r]$ appears in $S[l..r-1]$, or $S[l..r] = BAAC$ (**contains a square $AA$ strictly inside $[l, r]$**).
     - **$4$**: Otherwise.
  3. *Reverse-Engineering Scratchpad*: Enumerate all runs $R = [l_R, r_R, p]$ in $O(N)$ time. Sort runs by increasing $2p$ and use a DSU skip-list to assign `min_sq_start[x] = 2p` for $x \in [l_R, r_R - 2p + 1]$ and `min_sq_end[y] = 2p` for $y \in [l_R + 2p - 1, r_R]$ in $O(N \alpha(N))$ time. Then $S[l..r]$ contains a square iff $\min_{x \in [l, r]} (x + \text{min\_sq\_start}[x] - 1) \le r$ (a single RMQ query!). Check borders via IPM or BSGS.
  4. *Boundary Pitfalls*: Assigning `min_sq_start[x]` naively across $[l_R, r_R - 2p + 1]$ without a DSU skip-list degrades to $O(N^2)$ when many runs of different periods overlap.

---

#### **`W1B-15`. Codeforces 825F — `String Compression` & Runs-Accelerated Period DP** — `[EN]` *(Cohort 2 `#9`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$, compress $S$ into a concatenation of periodic blocks $k_1(u_1) k_2(u_2) \cdots$ minimizing the total length of the compressed encoding $\sum (\text{digits}(k_i) + |u_i|)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Any repetition $u^k$ ($k \ge 2$) of primitive root $u$ ($|u| = p$) is a sub-interval of a unique run $R = [l_R, r_R, p]$.
  2. *Combinatorial Word Invariant*: Instead of testing all $O(N^2)$ substrings for periodicity, transitions with $k \ge 2$ only occur along multiples of $p$ inside the $< N$ runs (or via KMP $\pi$-tables in $O(N^2)$ for $N = 8000$).
  3. *Reverse-Engineering Scratchpad*: Use Runs (or KMP period checks $p = \text{len} - \pi(\text{len})$) to drive DP transitions $dp[i] \to dp[i + k p] + \text{digits}(k) + p$.
  4. *Boundary Pitfalls*: Writing a non-primitive repetition $(v^2)^3$ as `3(vv)` uses $1 + 2|v|$ characters whereas `6(v)` uses $1 + |v|$ characters; only primitive periods $p$ ever need to be considered for $k \ge 2$.

---

#### **`W1B-16`. AtCoder AGC 023 F — `01 on Tree` & Tree Topological Lyndon Merging** — `[JA]`/`[EN]` *(Cohort 2 `#13`)*
- **Inline Mathematical Statement & Constraints**: Given a rooted tree of $N \le 2 \times 10^5$ vertices where each vertex $u$ holds a character/word $w_u$, find a valid topological ordering of the tree (every parent before its children) minimizing the lexicographical rank (or inversion count) of the concatenated string.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Local greedy from the root fails because a large parent vertex can hide a tiny child vertex directly beneath it.
  2. *Combinatorial Word Invariant*: Equip words with the transitive **infinite-periodic Lyndon order** $X \prec_\omega Y \iff X^\omega < Y^\omega$ (or $XY < YX$ for Lyndon words / $01$-ratio for inversions). If $v$ is the global minimum non-root vertex under $\prec_\omega$, then in **every** optimal topological ordering, $v$ must be visited **immediately** after its parent $p = \text{parent}(v)$!
  3. *Reverse-Engineering Scratchpad*: Maintain all non-root components in a priority queue ordered by $\prec_\omega$. Repeatedly pop the minimum component $v$, DSU-merge $v$ into its parent $p$ by concatenating $w_p \gets w_p w_v$, and push the updated $p$ back into the priority queue in $O(N \log N)$ time.
  4. *Boundary Pitfalls*: For general strings, comparing $X + Y < Y + X$ is transitive on equivalence classes of primitive roots ($X^\omega = Y^\omega \iff \text{root}(X) = \text{root}(Y)$), whereas comparing finite prefixes without periodic wrap-around violates transitivity.

---

#### **`W1B-17`. Codeforces 1286E — `Fedya the Potter Strikes Back`** — `[EN]` *(Cohort 1 `P-1B-05`/`P-1B-19` + Cohort 2 `#15`)*
- **Inline Mathematical Statement & Constraints**: Maintain $S[1..r]$ and weights $W[1..r]$ online ($N \le 6 \times 10^5$, forced online via decryption mask), outputting after each step $r$ the sum of $\min_{k \in [l, r]} W[k]$ over all $l \in [1, r]$ such that $S[l..r]$ is a border of $S[1..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Forced online queries forbid offline Suffix Arrays; at step $r$, borders of $S[1..r-1]$ that fail $S[\text{len}+1] == S[r]$ must be deleted, while all surviving borders have their weights clamped to $\min(\cdot, W[r])$.
  2. *Combinatorial Word Invariant*: Define `next_diff[u]` on the KMP fail chain to be the highest ancestor $v = \pi[u]$ with $S[v+1] \ne S[u+1]$. Walking $\pi[r-1]$ and skipping matching blocks via `next_diff` visits **only** borders that fail $S[\text{len}+1] == S[r]$ and are permanently deleted! Since each border starts at some $l \in [1, N]$ and is deleted at most once, total deletions are $O(N)$ amortized!
  3. *Reverse-Engineering Scratchpad*: Maintain active border start indices in a `std::map<int, int>` (weight $\to$ count of active borders) plus a monotonic stack of $W$ for range-minimum clamping, updating the running `__int128` sum in $O(N \log N)$ total time.
  4. *Boundary Pitfalls*: Walking single KMP links $\pi[u]$ instead of jumping via `next_diff[u]` visits surviving borders repeatedly and TLEs in $O(N^2)$ on $S = \texttt{a}^{N/2}\texttt{b}\dots$; also the answer reaches $\approx 1.8 \times 10^{20} > 2^{64}$, requiring `__int128` or twin-modulus arithmetic.

---

#### **`W1B-18`. Universal Cup / QOJ — `Square-Free Substring Range Queries`** — `[EN]`/`[ZH]` *(Cohort 1 `P-1B-15`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$) and $Q \le 5 \times 10^5$ queries $[L_q, R_q]$, count how many substrings $S[a..b] \subseteq S[L_q..R_q]$ are **square-free** (contain no tandem repeat $ww$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A substring $S[a..b]$ is square-free iff it contains no **primitively rooted** square $S[x..x+2p-1]$.
  2. *Combinatorial Word Invariant*: Every primitive square $S[x..x+2p-1]$ comes from a run $R = [l_R, r_R, p]$ with $x \in [l_R, r_R - 2p + 1]$. For each $x$, let $M[x]$ be the minimum right endpoint $x + 2p - 1$ of a square starting at $x$, and let $F[a] = \min_{x \ge a} M[x]$. Then $S[a..b]$ is square-free $\iff b < F[a]$, and $F[1] \le F[2] \le \cdots \le F[N]$ is monotonically non-decreasing!
  3. *Reverse-Engineering Scratchpad*: Rewrite $M[x] \gets \min(M[x], x + 2p - 1)$ as $D[x] = M[x] - x \gets \min(D[x], 2p - 1)$ on $x \in [l_R, r_R - 2p + 1]$—a **constant range-chmin** over the $< N$ runs, solvable in $O(N \alpha(N))$ via DSU skip-list after sorting runs by $2p$! Compute $F[a] = \min_{x \ge a} (x + D[x])$ from right to left, and answer each query $[L_q, R_q]$ in $O(\log N)$ via binary search + prefix sums on $F$.
  4. *Boundary Pitfalls*: Applying range-chmin to $M[x]$ directly (with slope-1 value $x + 2p - 1$) instead of subtracting $x$ first ($D[x] = M[x] - x \gets 2p - 1$) misses the constant range assignment reduction.

---

#### **`W1B-19`. Universal Cup / QOJ — `Square-Free String Partitioning DP in O(N)`** — `[EN]` *(Cohort 2 `#22`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), count the number of ways to partition $S$ into contiguous square-free substrings modulo $998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Using the same $L_{\max}[r] = \max \{ x \mid \exists \text{ square } S[x..y] \text{ with } y \le r \}$, $dp[r] = \sum_{t = L_{\max}[r]}^{r-1} dp[t]$.
  2. *Combinatorial Word Invariant*: By **Theorem 5.2(3)**, the total number of primitively rooted square occurrences $\sum_{R = [l, r, p] \in \mathcal{R}(S)} (r - l + 1 - 2p + 1)$ across the entire string is $< 2N$!
  3. *Reverse-Engineering Scratchpad*: Enumerate all runs $R = [l_R, r_R, p]$ in $O(N)$ time, directly loop over all $b \in [l_R + 2p - 1, r_R]$ setting $L_{\max}[b] = \max(L_{\max}[b], b - 2p + 1)$ in $O(N)$ total steps (or set $L_{\max}[r_R] \gets r_R - 2p + 1$ and propagate $L_{\max}[b] \gets \max(L_{\max}[b], L_{\max}[b+1]-1)$ across each run!), take prefix maxes $L_{\max}[r] = \max(L_{\max}[r], L_{\max}[r-1])$, and maintain prefix sums of $dp$ in $O(N)$ time.
  4. *Boundary Pitfalls*: Only checking squares that *end* exactly at $r$ forgets that $S[l..r]$ is also invalid if it contains a square ending at some $y < r$ with start $x \ge l$ (handled by the prefix max $L_{\max}[r] = \max(L_{\max}[r], L_{\max}[r-1])$).

---

#### **`W1B-20`. AtCoder ARC 113 E — `Rvom and Rsrev`** — `[JA]` *(Cohort 2 `#16`)*
- **Inline Mathematical Statement & Constraints**: Given a binary string $S \in \{\texttt{a}, \texttt{b}\}^N$ ($N \le 2 \times 10^5$), you may repeatedly choose two occurrences of the same character $S[l] = S[r]$, delete both $S[l]$ and $S[r]$, and reverse the substring $S[l+1..r-1]$ between them. Find the lexicographically largest string obtainable.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Reversing and deleting creates exponentially many reachable strings unless we characterize the canonical maximum suffix/prefix structure.
  2. *Combinatorial Word Invariant*: Every operation preserves the parity of $\#\texttt{a}$ and $\#\texttt{b}$, can never increase their counts, and can consolidate all $\texttt{b}$'s to the front so the optimal result has the form $\texttt{b}^x \texttt{a}^y$ (or $\texttt{b}^x \texttt{a}^y \texttt{b}^z$ when $S$ ends in $\texttt{b}$).
  3. *Reverse-Engineering Scratchpad*: Decompose $S$ into run-length blocks of $\texttt{a}$'s separated by $\texttt{b}$'s; each internal block of $\texttt{a}$'s of size $L_t$ can contribute $L_t - 2$ (or $L_t$ for the last two blocks) to the final trailing $\texttt{a}$-run without sacrificing any $\texttt{b}$'s.
  4. *Boundary Pitfalls*: When $S$ ends with $\texttt{b}$ and $\#\texttt{a}$ is odd, one $\texttt{b}$ is sacrificed to move the odd $\texttt{a}$ to the very end versus sacrificing $\texttt{a}$'s to keep all $\texttt{b}$'s at the front.

---

#### **`W1B-21`. `[SCOI / HNOI / UCup]` — `Run-Length Encoded (RLE) Lyndon Factorization & Minimal Cyclic Shift`** — `[ZH]`/`[EN]` *(Cohort 1 `P-1B-14`)*
- **Inline Mathematical Statement & Constraints**: Given an RLE string $S = c_1^{a_1} c_2^{a_2} \cdots c_M^{a_M}$ ($M \le 2 \times 10^5, c_t \ne c_{t+1}, a_t \le 10^9$), compute its CFL factorization and lexicographically smallest cyclic shift in $O(M)$ time.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Total uncompressed length $\sum a_t \le 2 \times 10^{14}$ forbids character-by-character Duval.
  2. *Combinatorial Word Invariant*: By **Lemma 2.5 (RLE-Lyndon Boundary Invariant)**, every non-unary Lyndon factor starts and ends on exact RLE block boundaries! Only when comparing the first block $c_i^{a_i}$ of the current Lyndon factor against a later block $c_k^{a_k}$ with $c_k = c_i$ does $a_k > a_i$ trigger Case 3 (more copies of the minimal character $c_i$ is lexicographically smaller!) and $a_k < a_i$ trigger Case 2 (fewer copies followed by $c_{k+1} > c_i$ is lexicographically larger!).
  3. *Reverse-Engineering Scratchpad*: Run Duval directly on the array of pairs $(c_t, a_t)$: at $j = i$ with $c_k = c_i$, treat $a_k > a_i$ as Case 3 and $a_k < a_i$ as Case 2 (advancing to $k+1$ if $c_{k+1} > c_i$); at $j > i$ with $c_k = c_j$ and $a_k \ne a_j$, the mismatch occurs at the character $c_{k+1}$ vs $c_j$ (if $a_k < a_j$) or $c_k$ vs $c_{j+1}$ (if $a_k > a_j$) immediately after $\min(a_k, a_j)$ characters!
  4. *Boundary Pitfalls*: If a cyclic shift wraps around $S_M$ and $S_1$ with $c_M = c_1$, coalesce the boundary blocks into $c_1^{a_1 + a_M}$ before running RLE-Duval.

---

### Tier 3: Advanced (11 Problems — `W1B-22` to `W1B-32`)

#### **`W1B-22`. `[BJWC2018] Border 的四种求法 (Four Methods of Finding Substring Borders)` (Luogu P4482 / LOJ 2541)** — `[ZH]` *(Cohort 1 `P-1B-17` + Cohort 2 `#18`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[l, r]$, find the length of the longest proper border of the substring $S[l..r]$ (or $0$ if unbordered). Time limit $2.0\text{ s}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A border of $S[l..r]$ of length $b \in [1, r - l]$ satisfies $\text{LCS}(l + b - 1, r) \ge b \iff (l + b - 1) - \text{LCS}(l + b - 1, r) \le l - 1$.
  2. *Combinatorial Word Invariant*: Four structural paradigms solve this problem:
     - **Method 1 (SAM Link-Tree HLD + $\text{endpos}$ Segment Tree Merge — $O(N \log^2 N)$)**: Decompose the root-to-$u_r$ path in the SAM Link Tree into $O(\log N)$ heavy chains and query $i \in [l, r-1]$ with $i - \text{len}(\text{LCA}(u_i, u_r)) \le l - 1$.
     - **Method 2 (BSGS $\sqrt{N}$ Split)**: Check border lengths $b \le \sqrt{N}$ directly via $O(1)$ LCE, and check SA ranks within $\pm \sqrt{N}$ of $\text{rk}[l]$.
     - **Method 3 (IPM Basic Substring Dictionary — $O(\log N)$ Dyadic AP Bands)**: In each dyadic band $b \in [2^k, 2^{k+1})$, occurrences of $S[l..l+2^k-1]$ inside $S[r-2^{k+1}+1..r]$ form a single arithmetic progression by the Weak Periodicity Lemma.
     - **Method 4 (2D Sweep-Line over Runs for Long Borders $\ge |S[l..r]|/2$)**: Any border of length $b \ge (r - l + 1)/2$ implies period $p = (r - l + 1) - b \le (r - l + 1)/2$, which holds iff **$S[l..r]$ is contained inside a run $R = [l_R, r_R, p] \in \mathcal{R}(S)$** ($l_R \le l$ and $r \le r_R$)! Thus the longest border $\ge |S[l..r]|/2$ is $(r - l + 1) - p_{\min}$, where $p_{\min}$ is the minimum period of a global run covering $[l, r]$!
  3. *Reverse-Engineering Scratchpad*: Combine Method 4 (2D dominance query $l_R \le l, r_R \ge r$ over $< N$ runs) or Method 1/3 for $O((N + Q) \log N)$ or $O((N + Q) \log^2 N)$ query time.
  4. *Boundary Pitfalls*: Exclude $i = r$ (the improper border of length $r - l + 1$); in Method 4, only runs with $2p \le r - l + 1$ induce a border of length $\ge (r - l + 1)/2$.

---

#### **`W1B-23`. `[国家集训队论文 2019 — 金策]` / LOJ 6681 / UOJ — `Range Distinct Squares in S[L_q..R_q]`** — `[ZH]`/`[EN]` *(Cohort 1 `P-1B-11` + Cohort 2 `#19a`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[L_q, R_q]$, count the number of **distinct square substrings** $w^2$ contained inside $S[L_q..R_q]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A square $w^2$ can occur multiple times inside the same run $R = [l_R, r_R, p]$ (at indices $x \equiv x' \pmod p$) and also across different runs $R_1, R_2$.
  2. *Combinatorial Word Invariant*: By the **$< 2N$ Representative Squares Lemma (Theorem 5.2(3))**, across all runs $R = [l_R, r_R, p]$ and all harmonics $d = kp \le (r_R - l_R + 1)/2$, there are strictly fewer than $2N$ canonical representatives $x \in [l_R, \min(l_R + p - 1, r_R - 2d + 1)]$. Inside a single run $R$, every subsequent shift $y \in [l_R + p, r_R - 2d + 1]$ has its previous occurrence of the exact same square at $y - p$ inside $R$!
  3. *Reverse-Engineering Scratchpad*: Sweep query right endpoint $r = 1 \to N$ maintaining $+1$ in a Fenwick tree at the latest starting position of each distinct square ending $\le r$:
     - For the $< 2N$ canonical representatives $x \in [l_R, \min(l_R + p - 1, r_R - 2d + 1)]$, look up the previous run occurrence via SAM node / Hash table and move its $+1$ marker from `last_pos` to $x$ when $r$ reaches $x + 2d - 1$.
     - For $y \in [l_R + p, r_R - 2d + 1]$, as $r$ sweeps across $[l_R + 2d - 1 + p, r_R]$, the active start position shifts uniformly from $r - 2d + 1 - p$ to $r - 2d + 1$ (a batch range progression update on the Fenwick tree!). Total time: $O((N + Q) \log N)$.
  4. *Boundary Pitfalls*: Omitting harmonics $k \ge 2$ ($d = kp$) misses non-primitive squares like $\texttt{aaaa}$ inside a run of period $p = 1$.

---

#### **`W1B-24`. `[国家集训队论文 2019 — 金策]` / Universal Cup — `Range Square Occurrences in S[L_q..R_q]`** — `[ZH]`/`[EN]` *(Cohort 1 `P-1B-18` + Cohort 2 `#19b`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 2 \times 10^5$), for each query $[L_q, R_q]$, count all pairs $(a, b)$ with $L_q \le a < b \le R_q$ such that $S[a..b]$ is a square $u^2$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Every square occurrence $S[a..b] = u^2$ has a unique primitive root $w$ ($u = w^k, |w| = p$) by Fine–Wilf, and thus belongs to a **unique run** $R = [l_R, r_R, p] \in \mathcal{R}(S)$!
  2. *Combinatorial Word Invariant*: The total number of square occurrences in $S[L_q..R_q]$ is the **exact disjoint sum** over all runs $R = [l_R, r_R, p] \in \mathcal{R}(S)$ and all harmonics $k = 1 \dots \lfloor \text{exp}(R)/2 \rfloor$ of:
     $$\max\!\left(0,\; \min(R_q, r_R) - \max(L_q, l_R) + 2 - 2kp\right).$$
  3. *Reverse-Engineering Scratchpad*: Because $\sum_{R \in \mathcal{R}(S)} \lfloor \text{exp}(R)/2 \rfloor < 1.5N$, there are $< 1.5N$ slope-$1$ diagonal segments $\{(x, x + 2kp - 1) \mid x \in [l_R, r_R - 2kp + 1]\}$. Sweep $R_q = 1 \to N$ with a linear-function Fenwick tree over $L_q$ to answer all $Q$ queries in $O((N + Q) \log N)$ time.
  4. *Boundary Pitfalls*: Counting only $k = 1$ counts *primitively rooted* squares; summing over all $1 \le k \le \lfloor \text{exp}(R)/2 \rfloor$ counts *all* squares while still keeping total segments $< 1.5N$.

---

#### **`W1B-25`. QOJ / Universal Cup — `Static Substring Minimum & Maximum Suffix Queries in O(N + Q log N)`** — `[EN]`/`[ZH]` *(Cohort 2 `#20` + `#25`)*
- **Inline Mathematical Statement & Constraints**: Given a static string $S[1..N]$ ($N, Q \le 5 \times 10^5$), answer $Q$ online queries $(l, r)$ asking for the starting position of (a) the lexicographically smallest suffix of $S[l..r]$, and (b) the lexicographically largest suffix of $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: With static $S$, $O(1)$ SA-LCE is available, allowing much faster preprocessing and queries than `[ZJOI2017] 字符串`.
  2. *Combinatorial Word Invariant*:
     - **For Minimum Suffix ($T = \varepsilon$, Compilation C)**: Let $i_0 = \arg\min_{i \in [l, r]} \text{rk}[i]$; the minimum suffix of $S[l..r]$ is the **shortest nonempty border of $S[i_0..r]$** (or $S[i_0..r]$ if unbordered). Alternatively, use the Segment-Tree-Free Dyadic Band RMQ (Section 3.5) in $O(\log(r - l + 1))$ time!
     - **For Maximum Suffix ($T = \varepsilon$, Compilation B)**: By Theorem 3.2 (`pushup` 1-Survivor Theorem), building the Segment Tree of $\text{Cand}_{\max}([L, R])$ using $O(1)$ SA-LCE takes $\sum_{h=1}^{\log N} \frac{N}{2^h} O(h) = O(N)$ total time! Moreover, for adjacent candidates $u_a \sqsubset u_{a+1}$ in $\text{Cand}_{\max}([L_t, R_t])$, their period $p_a = |u_{a+1}| - |u_a|$ extends right up to the end $R_a$ of its run: if $r \le R_a$, $u_{a+1}$ beats $u_a$; if $r > R_a$, the mismatch at $R_a + 1$ permanently decides $u_a$ vs $u_{a+1}$.
  3. *Reverse-Engineering Scratchpad*: Build SA + LCP RMQ and the Significant Suffix Segment Tree in $O(N)$ time; answer queries in $O(\log N)$ (via run-threshold precomputation on $\text{Cand}$) or $O(\log^2 N)$ via direct $O(1)$ LCE tournament across the $O(\log N)$ canonical nodes.
  4. *Boundary Pitfalls*: Assuming $\text{Cand}_{\min}(S[1..r]) \cap [l, r]$ is non-empty fails on $S = \texttt{abbb}, [l, r] = [2, 4]$; always use either $i_0 = \arg\min_{i \in [l, r]} \text{rk}[i]$ + shortest border, Dyadic Band RMQ, or the $O(N)$-built Segment Tree.

---

#### **`W1B-26`. Codeforces Gym 102012D / THUPC — `Substring Suffix + Arbitrary Pattern Extension Minimization`** — `[EN]`/`[ZH]` *(Cohort 1 `P-1B-12`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ and $Q$ queries $(l, r, a, b)$, find $i \in [l, r]$ minimizing the concatenation $S[i..r] + S[a..b]$ lexicographically.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Here the right-extension $T = S[a..b]$ is non-empty and varies per query!
  2. *Combinatorial Word Invariant*: By **Theorem 3.1 (Significant Suffixes)**, the winning suffix $S[i..r]$ of $S[l..r]$ under $T = S[a..b]$ must belong to $\text{Cand}_{\min}(S[l..r])$, which has size $\le \lfloor \log_2(r - l + 1) \rfloor + 1$.
  3. *Reverse-Engineering Scratchpad*: Extract $\text{Cand}_{\min}(S[l..r])$ in $O(\log(r - l + 1))$ time using either the $O(N)$-built Significant Suffix Segment Tree or Dyadic SA-Rank RMQ Bands (Section 3.5), then compare the $\le \log_2(r-l+1)+1$ candidates under $S[i..r] + S[a..b]$ using at most two $O(1)$ LCE queries per comparison!
  4. *Boundary Pitfalls*: Here $T = S[a..b] \ne \varepsilon$, so Cohort 1's counterexample $S = \texttt{aaba}, [l, r] = [2, 4], T = \texttt{c}$ is active: $\texttt{aba}$ ($i=2$) wins because $\texttt{abac} < \texttt{ac}$, proving why you must extract $\text{Cand}_{\min}(S[l..r])$ rather than using $T = \varepsilon$ shortcuts!

---

#### **`W1B-27`. Luogu P5353 / JOI / QOJ — `Lyndon Tree Construction & Substring Longest Lyndon Word Queries`** — `[ZH]`/`[JA]` *(Cohort 1 `P-1B-16` + Cohort 2 `#21`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 2 \times 10^5$), build the Lyndon Tree of $S$ in $O(N)$ time and answer queries $(l, r)$ asking for the length of the **longest Lyndon substring** contained inside $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: In the CFL factorization of $S[l..r] = w_1 w_2 \cdots w_k$ ($w_1 \ge \cdots \ge w_k$), no Lyndon word can cross a boundary between $w_m$ and $w_{m+1}$!
  2. *Combinatorial Word Invariant*: Every Lyndon substring of $S[l..r]$ is contained inside a **single** CFL factor $w_m$ of $S[l..r]$, and since each $w_m$ is itself a Lyndon word, the longest Lyndon substring of $S[l..r]$ is $\max_{1 \le m \le k} |w_m|$!
  3. *Reverse-Engineering Scratchpad*: In the Next-Smaller-Element tree (`nsv[i] = R_{\mathcal{L}}[i] + 1`), the CFL factors of $S[l..N]$ follow the parent path $l \to \text{nsv}[l] \to \text{nsv}[\text{nsv}[l]] \to \dots$. Binary-lift from $l$ to the last ancestor $i_k \le r$ with $\text{nsv}[i_k] > r+1$ (finding the max factor length along the tree path in $O(\log N)$), and for the final truncated factor $S[i_k..r]$, walk down the Lyndon Tree (Min-Cartesian Tree of $\text{rk}[i_k+1..r]$) or query RMQ of $\text{rk}$ to decompose $S[i_k..r]$ in $O(\log N)$ steps!
  4. *Boundary Pitfalls*: Truncating a right-maximal Lyndon word $S[i_k..R_{\mathcal{L}}[i_k]]$ at $r < R_{\mathcal{L}}[i_k]$ does **not** leave $S[i_k..r]$ as a single Lyndon word (e.g., truncating the Lyndon word $\texttt{abababb}$ at $r=6$ leaves $\texttt{ababab} = (\texttt{ab})(\texttt{ab})(\texttt{ab})$ of max Lyndon length $2$, not $6$!).

---

#### **`W1B-28`. Codeforces 1098F — `Ж-function`** — `[EN]` *(Cohort 1 `P-1B-21`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 2 \times 10^5$), for each query $[l, r]$, compute $\sum_{i=l}^r \min(r - i + 1, \text{LCP}(S[l..N], S[i..N]))$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: The clamp $\min(r - i + 1, \text{LCP}(l, i))$ splits indices $i \in [l, r]$ into those where $S[i..r]$ mismatches $S[l..]$ before $r$ vs. those where $S[i..r]$ is a border of $S[l..r]$.
  2. *Combinatorial Word Invariant*: In the Suffix Tree (or SAM Link Tree of $S^R$), $\text{LCP}(l, i) = \text{len}(\text{LCA}(u_l, u_i))$. Decomposing the root-to-$u_l$ path via Heavy-Light Decomposition reduces the query to $O(\log N)$ heavy-chain updates/queries.
  3. *Reverse-Engineering Scratchpad*: Offline 2D sweep-line over the HLD chains using Fenwick trees to separate $\text{len}(v) \le r - i + 1 \iff i + \text{len}(v) \le r + 1$ from $i + \text{len}(v) > r + 1$ in $O((N + Q) \log^2 N)$ time.
  4. *Boundary Pitfalls*: Off-by-one between $\text{LCP}$ on $S$ (which requires the SAM of $S^R$) and $\text{LCS}$ on $S$.

---

#### **`W1B-29`. AtCoder ARC 165 D — `Substring Comparison` & Periodic Collapse** — `[JA]` *(Cohort 1 `P-1B-22` + Cohort 2 `#30`)*
- **Inline Mathematical Statement & Constraints**: Given $N \le 2000$ and $M \le 2000$ constraints $S[A_i..B_i] < S[C_i..D_i]$, determine whether there exists a string $S[1..N]$ satisfying all $M$ strict lexicographical inequalities.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $S[A_i..B_i] < S[C_i..D_i]$ holds iff at the first mismatch offset $k \ge 0$, $S[A_i + k] < S[C_i + k]$ (or $S[A_i..B_i] \sqsubset S[C_i..D_i]$).
  2. *Combinatorial Word Invariant*: Maintain a DSU of forced character equalities $S[x] = S[y]$. Whenever the current head positions $A_i$ and $C_i$ of constraint $i$ lie in the same DSU component, $S[A_i] = S[C_i]$ is forced, so we advance $(A_i, C_i) \gets (A_i + 1, C_i + 1)$! Furthermore, in the directed graph of candidate strict inequalities $\text{find}(A_i) \to \text{find}(C_i)$, **any Strongly Connected Component (SCC) of size $\ge 2$ forces $S[x_1] \le S[x_2] \le \cdots \le S[x_1]$, which forces all characters in the SCC to be equal**!
  3. *Reverse-Engineering Scratchpad*: Repeatedly build the directed graph of active heads $\text{find}(A_i) \to \text{find}(C_i)$; if it is a DAG, return `Yes`. Otherwise, DSU-merge all vertices inside each nontrivial SCC, advance all constraints whose heads now share a DSU component (returning `No` if any $C_i$ exhausts $D_i$ before $A_i$ exhausts $B_i$), and repeat. Since there are at most $N - 1$ DSU merges in total, the algorithm runs in $O(N(N + M))$ time!
  4. *Boundary Pitfalls*: Treating a directed cycle in the $<$-graph as an immediate `No` is **wrong**—a cycle on the current candidate mismatch characters simply proves those characters must be **equal**, pushing the mismatch to the next position!

---

#### **`W1B-30`. AtCoder AGC 050 E / ARC 135 E — `K-th Lexicographically Smallest Lyndon Word & Necklace with Prefix Constraints`** — `[JA]`/`[ZH]` *(Cohort 1 `P-1B-31` + Cohort 2 `#23`)*
- **Inline Mathematical Statement & Constraints**: Given length $N \le 60$, alphabet size $\sigma$, and $K \le 10^{18}$ (or a fixed prefix $P[1..m]$), count how many Lyndon words (and necklaces) of length $N$ start with $P[1..m]$, and reconstruct the $K$-th Lyndon word of length $N$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Witt's formula counts unconstrained Lyndon words, but once a prefix $P[1..m]$ is fixed, Burnside's lemma does not directly count valid completions.
  2. *Combinatorial Word Invariant*: A completion $S[1..N]$ of $P[1..m]$ is a pre-Lyndon word iff Duval's pointer comparison $S[t]$ vs $S[j]$ never hits Case 3 ($S[t] < S[j]$) for any $t \le N$. Moreover:
     - $S[1..N]$ is a **necklaces representative (pre-Lyndon with period dividing $N$)** iff its final Duval period $p$ at $t = N$ satisfies $p \mid N$.
     - $S[1..N]$ is a **Lyndon word** iff its final Duval period at $t = N$ is $p = N$!
  3. *Reverse-Engineering Scratchpad*: Whenever $S[t] > S[j]$ (Case 2) at step $t > m$, the period jumps to $p = t > m$ and $j$ resets to $1$ (the very start of the fixed prefix $P$!). Thus a simple DP `dp[t][j]` ($t \in [m, N], j \in [1, t]$) simulating Duval's comparison pointer $j$ counts exact pre-Lyndon completions in $O(N^2)$ time per prefix check!
  4. *Boundary Pitfalls*: A power of a shorter Lyndon word $w^{N/p}$ ($p \mid N, p < N$) never triggers Case 3 up to $N$, so you must either require final period $p = N$ or apply Möbius inversion over divisor periods $p \mid N$ to isolate primitive Lyndon words from necklaces.

---

#### **`W1B-31`. ICPC / Petrozavodsk — `Longest Unbordered Substring (Ehrenfeucht–Silberger / Duval Lemma)`** — `[EN]` *(Cohort 2 `#24`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$), find the maximum length of an unbordered (border-free) substring of $S$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: By Theorem 2.1(3), every Lyndon word is unbordered.
  2. *Combinatorial Word Invariant*: Let $p$ be the minimum period of $S[1..N]$. Any substring of length $p$ equal to the $<$-Lyndon (or $>$-Lyndon) shift of the period block is unbordered, so the answer is **at least $p$** (unless $S$ is shorter than a full period rotation, in which case we check suffixes/prefixes). Furthermore, by Duval's Theorem on unbordered factors (1982), if the longest unbordered factor has length $L$, then $N - L = O(p)$, so we only need to test candidate lengths descending from $N$ down to $p$!
  3. *Reverse-Engineering Scratchpad*: Compute the minimum period $p = N - \pi(N)$ and work downwards from length $L = N$, or use the Lyndon Array $\max_i \max(\lambda_<[i], \lambda_>[i])$ alongside border checks near the ends of $S$.
  4. *Boundary Pitfalls*: The longest unbordered substring of $S$ can be **strictly longer** than the minimum period $p$ of $S$! Counterexample: $S = \texttt{aabaabaa}$ has period $p = 3$ ($\texttt{aab}$), yet $S[2..6] = \texttt{abaab}$ is a Lyndon (and hence unbordered) substring of length $5 > p = 3$!

---

#### **`W1B-32`. Codeforces 1906I / ICPC WF — `Lexicographically Optimal Interleaving (Shuffle) of Two Strings via CFL`** — `[EN]` *(Cohort 2 `#28`)*
- **Inline Mathematical Statement & Constraints**: Given two strings $A[1..N]$ and $B[1..M]$ ($N, M \le 2 \times 10^5$), interleave $A$ and $B$ into $C[1..N+M]$ to minimize (or maximize) $C$ lexicographically.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: When $A[i] == B[j]$, a greedy local comparison cannot decide whether to advance $i$ or $j$ without inspecting the suffixes.
  2. *Combinatorial Word Invariant*: By **Lothaire's CFL Shuffle Theorem**, if we factor $A = u_1 \cdots u_p$ and $B = v_1 \cdots v_q$ into Lyndon words under the **reversed order $>$** (so $u_1 \le_< u_2 \le_< \cdots \le_< u_p$ in standard order $<$ and each $u_t$ is $>-$Lyndon), the lexicographically smallest interleaving of $A$ and $B$ **never splits any factor $u_t$ or $v_s$**, and is obtained simply by merging the two sorted factor lists $(u_1, \dots, u_p)$ and $(v_1, \dots, v_q)$! Equivalently, at the character level, append $+\infty$ to both $A$ and $B$ and greedily advance whichever suffix $A[i..N]\infty$ or $B[j..M]\infty$ is smaller!
  3. *Reverse-Engineering Scratchpad*: Build SA on $A + (+\infty) + B + (+\infty)$ in $O(N + M)$ time (or run Duval under $>$ when pieces must be merged as blocks) and merge in $O(N + M)$ time.
  4. *Boundary Pitfalls*: Using $-\infty$ instead of $+\infty$ at the ends of $A$ and $B$ when minimizing $C$ makes an exhausted prefix $A[i..N] \sqsubset B[j..M]$ falsely win even when the next character of $B$ after the prefix is tiny!

---

### Tier 4: Mastery (10 Problems — `W1B-33` to `W1B-42`)

#### **`W1B-33`. `[国家集训队论文 2019 — 金策]` / UOJ 429 / QOJ — `Substring Minimum Cyclic Shift Queries`** — `[ZH]` *(Cohort 1 `P-1B-25`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 2 \times 10^5$), for each query $[l, r]$, find the starting position $i \in [l, r]$ that minimizes the cyclic shift $S[i..r] + S[l..i-1]$ of the substring $S[l..r]$ (tie-breaking by smallest $i$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Generalizes `[JSOI2019] 节日庆典` (`W1B-03`, where $l = 1$ was fixed) to arbitrary substrings $S[l..r]$.
  2. *Combinatorial Word Invariant*: Minimizing $S[i..r] + S[l..i-1]$ of length $r - l + 1$ is equivalent to minimizing $S[i..r] + T$ for the fixed right-extension $T = S[l..r]$! By **Theorem 3.1**, the winning suffix $S[i..r]$ must belong to $\text{Cand}_{\min}(S[l..r])$.
  3. *Reverse-Engineering Scratchpad*: Extract the $\le \lfloor \log_2(r-l+1) \rfloor + 1$ candidates of $\text{Cand}_{\min}(S[l..r])$ in $O(\log(r - l + 1))$ time using either the $O(N)$-built Significant Suffix Segment Tree (Section 3.3B) or Dyadic SA-Rank RMQ Bands (Section 3.5). Then compare consecutive candidates $u \sqsubset v$ under $u + S[l..i_u-1]$ vs $v + S[l..i_v-1]$ using at most **two $O(1)$ LCE queries**! Total time: $O(N + Q \log N)$!
  4. *Boundary Pitfalls*: Remember Cohort 1's counterexample $S = \texttt{aaba}, [l, r] = [2, 4]$: here $T = S[2..4] = \texttt{aba} \ne \varepsilon$, so $\text{Cand}_{\min}(S[l..r])$ **must** be extracted for $[l, r]$ rather than filtered from $\text{Cand}_{\min}(S[1..r])$.

---

#### **`W1B-34`. Universal Cup / QOJ — `Substring Run Counting Queries` ($|\mathcal{R}(S[L_q..R_q])|$)** — `[ZH]`/`[EN]` *(Cohort 1 `P-1B-26`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 2 \times 10^5$), for each query $[L_q, R_q]$, compute the exact number of runs in the substring $S[L_q..R_q]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Clipping $S$ to $S[L_q..R_q]$ truncates each global run $R = [l_R, r_R, p] \in \mathcal{R}(S)$ to $[\max(L_q, l_R),\; \min(R_q, r_R)]$.
  2. *Combinatorial Word Invariant*: **Fine–Wilf Clipping Non-Collision Lemma**: Could two distinct global runs $R_1 = [l_1, r_1, p_1]$ and $R_2 = [l_2, r_2, p_2]$ ($p_1 < p_2$) clip to the **exact same interval** inside $[L_q, R_q]$ with clipped length $\ge 2p_2$? **NO!** Their overlap would have length $\ge 2p_2 > p_1 + p_2 - \gcd(p_1, p_2)$, which by Fine–Wilf forces period $\gcd(p_1, p_2) \le p_1 < p_2$ across $R_2$'s clipped interval, contradicting that $p_2$ is the *primitive* period of $R_2$! Therefore, $|\mathcal{R}(S[L_q..R_q])|$ equals the exact number of global runs $R = [l_R, r_R, p] \in \mathcal{R}(S)$ satisfying
     $$\min(R_q, r_R) - \max(L_q, l_R) + 1 \ge 2p!$$
  3. *Reverse-Engineering Scratchpad*: Rewrite $\min(R_q, r_R) - \max(L_q, l_R) + 1 \ge 2p$ as: (1) $L_q \le r_R - 2p + 1$, (2) $R_q \ge l_R + 2p - 1$, and (3) $R_q - L_q + 1 \ge 2p$. Notice that (1) and (2) already imply (3) *except* when $[L_q, R_q] \subsetneq [l_R, r_R]$ with $R_q - L_q + 1 < 2p$. Separate that strict-containment correction by sorting runs and queries by length $2p$ vs $R_q - L_q + 1$ and using a 2D Fenwick sweep in $O((N + Q) \log N)$ time!
  4. *Boundary Pitfalls*: Omitting condition (3) ($R_q - L_q + 1 \ge 2p$) overcounts global runs of length $\ge 4p$ when $[L_q, R_q]$ is a tiny window strictly inside $[l_R + 2p - 1, r_R - 2p + 1]$.

---

#### **`W1B-35`. Universal Cup / QOJ — `Longest Square & k-th Power Substring in S[L_q..R_q]`** — `[EN]` *(Cohort 1 `P-1B-27`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 2 \times 10^5$) and $k \ge 2$, find for each query $[L_q, R_q]$ the maximum length of a $k$-th power substring $u^k$ contained in $S[L_q..R_q]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: In a global run $R = [l_R, r_R, p]$ clipped to $M = \min(R_q, r_R) - \max(L_q, l_R) + 1 \ge kp$, the longest $k$-th power has length $\lfloor M / (kp) \rfloor \cdot kp$.
  2. *Combinatorial Word Invariant*: Partition runs intersecting $[L_q, R_q]$ into four geometric classes: (1) $[l_R, r_R] \subseteq [L_q, R_q]$ (2D range max of $\lfloor (r_R - l_R + 1)/(kp) \rfloor kp$); (2) runs containing $[L_q, R_q]$ ($l_R < L_q \le R_q < r_R$, where we only need minimum $p \le (R_q - L_q + 1)/k$); (3) runs crossing $L_q$ ($l_R < L_q \le r_R \le R_q$); and (4) runs crossing $R_q$ ($L_q \le l_R \le R_q < r_R$). By the **Three-Squares Lemma (Theorem 5.3)**, at most $O(\log N)$ runs of distinct primitive periods can cover $L_q$ and extend to $\ge L_q + 2p - 1$ (and symmetrically for $R_q$)!
  3. *Reverse-Engineering Scratchpad*: Handle Class (1) and (2) via offline 2D sweep-line + Segment Tree in $O((N + Q) \log N)$, and handle the $O(\log N)$ boundary-straddling runs at $L_q$ and $R_q$ directly in $O(Q \log N)$!
  4. *Boundary Pitfalls*: Using $M$ instead of $\lfloor M / (kp) \rfloor \cdot kp$ fails because a clipped run is generally a fractional power $u^{k + \delta}$, whereas the problem requires an exact integer power $u^{m k}$ (or $w^k$).

---

#### **`W1B-36`. Universal Cup / QOJ — `Sum of Functions over Distinct Squares` ($\sum_{w^2} f(|\text{endpos}(w^2)|, |w|)$)** — `[EN]` *(Cohort 2 `#26`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$), compute $\sum_{w^2 \text{ distinct square in } S} f(\text{occ}(w^2), |w|)$, where $\text{occ}(w^2)$ is the total number of occurrences of $w^2$ in $S$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Requires coupling **Runs Enumeration** with **SAM $\text{endpos}$ sizes**.
  2. *Combinatorial Word Invariant*: By the **$< 2N$ Representative Squares Lemma (Theorem 5.2(3))**, iterating over all runs $R = [l_R, r_R, p]$, all $k = 1 \dots \lfloor (r_R - l_R + 1)/(2p) \rfloor$, and all canonical phase shifts $a \in [l_R, \min(l_R + p - 1, r_R - 2kp + 1)]$ visits **fewer than $2N$ candidate substrings $S[a..a+2kp-1]$ in total**, and covers 100% of all distinct squares in $S$!
  3. *Reverse-Engineering Scratchpad*: Build the SAM of $S$ (computing $|\text{endpos}(u)|$ by Link-Tree bottom-up sum) and enumerate all runs in $O(N)$. For each of the $< 2N$ representative squares $(a, 2kp)$, locate its SAM node $u$ via Link-Tree binary lifting (or offline tarjan/weighted ancestor in $O(1)$), deduplicate pairs `(u, 2kp)` so squares appearing in multiple disjoint runs are counted once, and accumulate $f(|\text{endpos}(u)|, kp)$.
  4. *Boundary Pitfalls*: Assuming $\text{occ}(w^2)$ equals the number of occurrences inside a *single* run $R$ is false—the exact same square $w^2$ can occur in several disjoint runs across $S$ (e.g., $\texttt{ababxabab}$), which is why $|\text{endpos}(u)|$ on the SAM (or summing multiplicities across deduplicated runs) is required.

---

#### **`W1B-37`. Universal Cup Grandmaster / QOJ — `K-th Lexicographically Smallest Square Substring (Distinct & With Multiplicity)`** — `[EN]` *(Cohort 1 `P-1B-24` + Cohort 2 `#31`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q$ queries $K \le 10^{12}$, find the $K$-th lexicographically smallest square substring of $S$ (both for distinct squares and counted with occurrence multiplicity).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: There are up to $\Theta(N^2)$ square occurrences, but $< 2N$ distinct squares.
  2. *Combinatorial Word Invariant*: In run $R = [l_R, r_R, p]$, the canonical square $S[l_R + \delta .. l_R + \delta + 2kp - 1]$ ($0 \le \delta < p$) occurs exactly $\lfloor \frac{(r_R - l_R + 1) - \delta - 2kp}{p} \rfloor + 1$ times inside $R$. Since no two distinct runs of the same period can overlap by $\ge 2p$, the total multiplicity of a distinct square $w^2$ in $S$ is the exact sum of its occurrences across all runs generating it (or $|\text{endpos}(u)|$ in SAM)!
  3. *Reverse-Engineering Scratchpad*: Extract the $< 2N$ representative squares $(a, 2kp)$, sort them lexicographically in $O(N \log N)$ time using $O(1)$ SA-LCE (`rk` + `height` RMQ), merge identical squares (checking $\text{LCP}(a_1, a_2) \ge 2kp$) while summing their run multiplicities, and answer $K$-th queries via binary search on prefix sums in $O(\log N)$ time.
  4. *Boundary Pitfalls*: Two squares of different lengths $2k_1 p_1 < 2k_2 p_2$ with $\text{LCP}(a_1, a_2) \ge 2k_1 p_1$ have the **shorter** square $2k_1 p_1$ strictly smaller lexicographically than the longer square.

---

#### **`W1B-38`. `[THUPC / QOJ]` — `Palindromic Runs & Rich Palindromic Squares Synthesis`** — `[ZH]` *(Cohort 1 `P-1B-23` + Cohort 2 `#32`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^5$), count (both distinct and total occurrences of) substrings that are **simultaneously a square $w^2$ and a palindrome**, and characterize all palindromic centers inside runs.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Bridges **Wave 1B (Runs Theorem)** with **Wave 3A (Manacher / PAM)**.
  2. *Combinatorial Word Invariant*:
     - **Palindromic Square Identity**: A square $w^2$ is a palindrome $\iff w^2 = (w^2)^R = (w^R)^2 \iff w = w^R$ (**the half-string $w$ is itself a palindrome**!).
     - **Symmetric Period Decomposition Theorem**: Inside a run $R = [l_R, r_R, p]$, a cyclic shift $w = S[a..a+p-1]$ is a palindrome iff the base period block factors into **two palindromes** $u v$, and within such a run, palindromic centers of length $\ge 2p$ occur at half-period spacing $p/2$!
  3. *Reverse-Engineering Scratchpad*: Enumerate the $< 2N$ representative squares $(a, 2kp)$ across all runs; for each representative, test in $O(1)$ via Manacher's array whether its half-string $S[a..a+kp-1]$ is a palindrome! Deduplicate valid palindromic squares via SAM/SA to get distinct and total counts in $O(N \log N)$ or $O(N)$ time.
  4. *Boundary Pitfalls*: Checking whether $w^2 = S[a..a+2kp-1]$ is a palindrome directly via Manacher at center $a + kp - 0.5$ is equivalent to $w = w^R$, and remember that inside a single run of period $p$, **at most two** shifts $\delta \in [0, p-1]$ can make $S[l_R+\delta .. l_R+\delta+kp-1]$ a palindrome!

---

#### **`W1B-39`. UOJ / QOJ / `[JA]` Treatise — `Online & Persistent Lyndon Factorization / Lyndon Tree Maintenance under Right-Appends`** — `[ZH]`/`[JA]` *(Cohort 1 `P-1B-28` + Cohort 2 `#29`)*
- **Inline Mathematical Statement & Constraints**: Given an initially empty string (or a persistent version tree of $Q \le 2 \times 10^5$ character appends `append(v, c)`), output after each append the CFL factor count, last Lyndon factor, or Lyndon Tree right-spine hash in **worst-case $O(\log^2 N)$ or $O(\log N)$ time per operation**.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: On a persistent version tree, adversary branching on $\texttt{a}^N \texttt{b}$ breaks Duval's amortized $O(1)$ analysis.
  2. *Combinatorial Word Invariant*: Appending $c$ to the CFL factorization $w_1^{d_1} > w_2^{d_2} > \cdots > w_m^{d_m}$ pushes $(c, 1)$ onto the right spine of the Lyndon Tree and repeatedly merges the top two blocks $(u, d)$ and $v$ into the single Lyndon word $u^d v$ whenever $u < v$.
  3. *Reverse-Engineering Scratchpad*: Maintain the CFL block stack persistently using binary-lifting parent pointers + tree-depth rolling hashes for $O(\log N)$ LCE comparisons. Whenever $d|u| \le |v|$, merging $(u, d)$ and $v$ doubles the length of the top factor $|u^d v| \ge 2|v|$ or $\ge 2d|u|$; when $d|u| > |v|$, use binary-lifting on the stack to jump past contiguous blocks that collapse together in $O(\log N)$ merges!
  4. *Boundary Pitfalls*: Merging one copy of $u$ at a time instead of collapsing the entire power block $(u, d)$ with $v$ into $(u^d v, 1)$ in a single step degrades to $O(N)$ on $\texttt{a}^N \texttt{b}$.

---

#### **`W1B-40`. ZJOI / THUPC / QOJ — `Lexicographically Monotone String Partition DP` ($s_1 < s_2 < \cdots < s_k$)** — `[ZH]` *(Cohort 1 `P-1B-29`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$ or $5000$), find the maximum number of pieces (or count partitions) $S = s_1 s_2 \cdots s_k$ such that $s_1 < s_2 < \cdots < s_k$, or find a partition into $k$ pieces minimizing the lexicographically largest piece.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Contrasts directly with CFL factorization ($w_1 \ge \cdots \ge w_k$): here we want strictly increasing pieces $s_1 < s_2 < \cdots < s_k$.
  2. *Combinatorial Word Invariant*: For a split point $i$, a previous piece $s_{m-1} = S[j..i-1]$ is smaller than $s_m = S[i..r]$ iff either (a) $\text{LCP}(j, i) < i - j$ and $\text{rk}[j] < \text{rk}[i]$ (which holds for **all** $r \ge i + \text{LCP}(j, i)$), or (b) $\text{LCP}(j, i) \ge i - j$ and $r - i + 1 > i - j$ ($S[j..i-1] \sqsubset S[i..r]$).
  3. *Reverse-Engineering Scratchpad*: For minimizing the maximum piece in $k$ cuts, binary search on the rank among all $O(N^2)$ distinct substrings (using SA + LCP array to pick the midpoint substring $P$ in $O(N)$ time), and greedily cut from right to left whenever the current suffix exceeds $P$ (checking $S[i..r] \le P$ in $O(1)$ via LCE)!
  4. *Boundary Pitfalls*: If $P$ has length $|P|$ and $S[i] > P[1]$, no substring starting at $i$ can be $\le P$, making $P$ immediately infeasible.

---

#### **`W1B-41`. Codeforces 1608G / Universal Cup — `Tree Path Significant Suffixes & Lexicographical Path Queries`** — `[EN]`/`[ZH]` *(Cohort 1 `P-1B-30`)*
- **Inline Mathematical Statement & Constraints**: Given a tree of $N \le 10^5$ vertices with characters on edges and $Q \le 10^5$ queries $(u, v)$, find the lexicographically smallest suffix (or cyclic shift) of the string formed by the simple path from $u$ to $v$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Heavy-Light Decomposition (HLD) splits the directed path $u \to v$ into $O(\log N)$ contiguous intervals on the heavy-chain string $H$ and its reversal $H^R$.
  2. *Combinatorial Word Invariant*: By **Theorem 3.1 (Significant Suffixes)** and **Theorem 3.2 (The `pushup` 1-Survivor Theorem)**, we can prebuild the $O(N)$-time Significant Suffix Segment Tree over $H + H^R$, decomposing $u \to v$ into $k = O(\log^2 N)$ canonical Segment Tree nodes $I_1, I_2, \dots, I_k$.
  3. *Reverse-Engineering Scratchpad*: Merge the candidate sets $\text{Cand}_{\min}(I_t)$ along the path $I_1, \dots, I_k$ using $O(1)$ SA-LCE on $H + H^R$ (since at any point along the path, any suffix starting in $I_t$ is followed by the remaining path suffix $I_{t+1} \cdots I_k$, which we compare across the $\le \log_2 N$ path segments in $O(\log N)$ LCE steps!).
  4. *Boundary Pitfalls*: Upward segments from $u$ to $\text{LCA}(u, v)$ must be mapped to the reversed heavy-chain string $H^R$, while downward segments from $\text{LCA}(u, v)$ to $v$ map to $H$.

---

#### **`W1B-42`. Universal Cup Grandmaster / QOJ — `2D Orthogonal Range Queries over Interior Lyndon Roots & Run Exponents` (`Syn-1B Reserve`)** — `[EN]`/`[ZH]` *(Cohort 1 `P-1B-32`)*
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 2 \times 10^5$), for each query $[L_q, R_q]$, compute $\sum_{R \in \mathcal{R}(S[L_q..R_q])} \lfloor \text{exp}(R) \rfloor$ (or weighted sum of interior Lyndon roots of all runs inside $S[L_q..R_q]$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Synthesizes the **Interior $L$-Root Proof of the Runs Theorem (Section 5.2)** with **Substring Run Clipping (`W1B-34`)**.
  2. *Combinatorial Word Invariant*: By Section 5.2 Step 3, each index $i \in [2, N]$ is an interior $L$-root ($l_R + 1 \le i \le r_R - p + 1$) for **at most one global run** $R_i = [l_R, r_R, p] \in \mathcal{R}(S)$! When $S$ is clipped to $[L_q, R_q]$, $i$ remains an interior $L$-root of the clipped run iff $L_q \le i - 1$, $R_q \ge i + p - 1$, and the clipped run has length $\min(R_q, r_R) - \max(L_q, l_R) + 1 \ge 2p$.
  3. *Reverse-Engineering Scratchpad*: Associate each of the $\le N - 1$ interior $L$-roots $i \in [2, N]$ with its activation constraints on $(L_q, R_q)$ and answer all $Q$ queries via 2D/3D orthogonal range sum in $O((N + Q) \log N)$ time!
  4. *Boundary Pitfalls*: Remember that the number of interior $L$-roots of a clipped run $[l', r', p]$ in $[l'+1, r'-p+1]$ equals $\lfloor (r' - l') / p \rfloor$, which differs from $\lfloor (r' - l' + 1) / p \rfloor$ by $+1$ precisely when $p \mid (r' - l' + 1)$ (handled by testing whether the $L$-root at $l'$ is also included).

---

### Section 6.5 Quarantine Ledger: 10 Excluded Pure-Template Problems (`R-1B-01`–`R-1B-10`)

Per `AGENTS.md` and `strings_research/PLAN.md §2.2`, the union of pure template verification problems across Cohort 1 and Cohort 2 is strictly quarantined from textbook chapters:

| Quarantine ID | Judge & Problem Name | Language | Reason for Quarantine |
| :--- | :--- | :--- | :--- |
| **`R-1B-01`** | **Library Checker — `Lyndon Factorization`** | `[EN]`/`[JA]` | Bare verification of Duval's $O(N)$ CFL factorization algorithm with zero modelling. |
| **`R-1B-02`** | **Library Checker — `Run Enumerate`** | `[EN]`/`[JA]` | Bare verification of outputting all runs $(p, l, r)$ of $S[1..N]$. |
| **`R-1B-03`** | **Luogu P6114 — `【模板】Lyndon 分解`** | `[ZH]` | Bare Chinese template asking for the XOR sum of right endpoints of Duval's CFL factors. |
| **`R-1B-04`** | **Luogu P6656 — `【模板】Runs`** | `[ZH]` | Bare Chinese template asking to print all runs $(l, r, p)$ in lexicographical order. |
| **`R-1B-05`** | **LOJ 172 — `Runs`** | `[ZH]` | Identical bare template verification of Runs enumeration. |
| **`R-1B-06`** | **Luogu P1368 — `【模板】最小表示法 (工艺)`** | `[ZH]` | Bare template verification of lexicographically smallest cyclic shift via Duval on $S+S$. |
| **`R-1B-07`** | **UVA 719 / SPOJ `BEADS` / POJ 1509 — `Glass Beads`** | `[EN]` | Bare single-string minimal cyclic rotation template without structural coupling. |
| **`R-1B-08`** | **CSES 1110 — `Minimal Rotation`** | `[EN]` | Bare minimal cyclic rotation template on a single string of length $10^6$. |
| **`R-1B-09`** | **Codeforces Gym 103102I (Educational) — `Lyndon Array`** | `[EN]` | Direct verification of longest Lyndon prefix array $\lambda[1..N]$ without coupling. |
| **`R-1B-10`** | **Library Checker — `Z Algorithm` / `Suffix Array`** | `[EN]`/`[JA]` | Assumed baseline prerequisite library primitives per `PLAN.md §1`. |

---

## Section 7. Master Summary of Diagnostic Signals, Invariants & Counterexamples (Wave 1B)

| Technique / Structural Theorem | Diagnostic Signal in Problem Statement | Core Combinatorial Word Invariant | Canonical Broken-Invariant Counterexample |
| :--- | :--- | :--- | :--- |
| **Duval's $O(N)$ CFL Automaton & All-Prefix State Sharing** | Smallest cyclic shift, $k$-cut reversal greedy (`CF 594E`), all-prefix CFL/min-suffix/max-suffix in $O(N)$ time and $O(1)$ space. | Pre-Lyndon invariant $S[i..k-1] = w^d w'$; Case 2 ($S[k] > S[j]$) collapses $w^d w' S[k] \in \mathcal{L}$; Case 3 ($S[k] < S[j]$) freezes $w^d$; remainder $w'$ shares CFL state with $r' = r - d \cdot p$. | Rewinding $k \gets i+1$ without advancing $i$ by $d \cdot p$ causes $O(N^2)$ TLE on $(\texttt{ab})^{N/2}\texttt{a}$; forgetting to merge adjacent $|w_t| = 1$ blocks in `CF 594E` wastes cuts on $S = \texttt{cba}\dots$. |
| **Significant Suffixes (`显著后缀`, $\text{Cand}_{\min/\max}$)** | Substring minimum/maximum suffix or cyclic shift under right-extensions $T$ (`[ZJOI2017] 字符串`, `[JSOI2019] 节日庆典`). | For $|u| < |v| < 2|u|$ with $u \sqsubset v$, writing $v = w^2 u', u = wu'$ forces $\min(u'T, vT) < uT < \max(u'T, vT)$ for **all** $T \in \Sigma^*$, eliminating the middle suffix $u$ and leaving $\le \lfloor\log_2 |U|\rfloor + 1$ candidates (and $\le 1$ survivor from `left_child` in `pushup`!). | Assuming $\text{Cand}_{\min}(S[l..r]) \subseteq \text{Cand}_{\min}(S[1..r])$ fails on $S = \texttt{aaba}, [l, r] = [2, 4]$ (where $\texttt{aaba}$ kills $\texttt{aba}$ at $l=1$) and on $S = \texttt{abbb}, [l, r] = [2, 4]$ ($\text{Cand}(\texttt{abbb}) \cap [2, 4] = \emptyset$). |
| **Lyndon Array ($\lambda_<, \lambda_>$) & Lyndon Tree** | All-start longest Lyndon prefixes, Lyndon Tree subtree queries, $O(N)$ Runs enumeration. | $R_{\mathcal{L}}[i] = \text{nsv}[i] - 1 = \min\{j > i \mid S[j..N] < S[i..N]\} - 1$; Lyndon Tree of $\$S$ is isomorphic to the Min-Cartesian Tree of $\text{rk}[2..N+1]$ with left endpoint $L_m - 1$. | Negating $\text{rk}_<$ (`-rk_<[i]`) to build $\lambda_>$ fails on $S = \texttt{bab}$ ($\text{rk}_< = [3, 1, 2]$), falsely claiming $S[3..3] = \texttt{b} >_R \texttt{bab}$ and marking the bordered word $\texttt{bab}$ as Lyndon! |
| **The Runs Theorem (`极长周期子串`, Bannai et al. 2017)** | Counting squares (`AABB`), range distinct/total squares, longest border $\ge |S[l..r]|/2$, square-free DP. | Assigning $<_R \in \{<, >\}$ via $S[r+1] <_R S[r+1-p]$ guarantees every interior $L$-root $i \in [l+1, l+p]$ has $\lambda_{<_R}[i] = p$ and $S[i] <_R S[i-1]$, proving $|\mathcal{R}(S)| < N$, $\sum \text{exp}(R) < 3N$, and $< 2N$ canonical square representatives. | Forgetting non-primitive harmonics $d = kp$ ($k \ge 2$) when counting squares inside a run, or failing to deduplicate identical squares occurring in two disjoint runs (e.g., $\texttt{ababxabab}$). |

---

## Section 8. Consolidated Multilingual Bibliography (Cohort 1 + Cohort 2 + Cohort 3)

1. **Lyndon, R. C. (1954)**. *On Burnside's problem*. Transactions of the American Mathematical Society, 77(2), 202–215. (Introduces standard lexicographical words, later named Lyndon words).
2. **Chen, K.-T., Fox, R. H., & Lyndon, R. C. (1958)**. *Free differential calculus, IV. The quotient groups of the lower central series*. Annals of Mathematics, 68(1), 81–95. (Proves the Chen–Fox–Lyndon uniqueness theorem $S = w_1 w_2 \cdots w_k$ with $w_1 \ge \cdots \ge w_k$).
3. **Fredricksen, H., & Maiorana, J. (1978)**; **Fredricksen, H., & Kessler, I. (1986)**. *Necklaces of beads in $k$ colors and $k$-ary de Bruijn sequences*. Discrete Mathematics, 23(3), 207–210. (The FKM $O(1)$-amortized Lyndon/necklace generation and lexicographically smallest De Bruijn cycle).
4. **Duval, J.-P. (1983)**. *Factorizing words over an ordered alphabet*. Journal of Algorithms, 4(4), 363–381. (Duval's $O(N)$-time, $O(1)$-space three-pointer CFL factorization and minimal cyclic shift algorithm).
5. **Duval, J.-P. (1988)**. *Génération d'une section des classes de conjugaison et arbre des mots de Lyndon de longueur bornée*. Theoretical Computer Science, 60(3), 255–283. (Duval's Next-Lyndon word generation theorem).
6. **Barcelo, H. (1990)**; **Hohlweg, C., & Reutenauer, C. (2003)**. *Lyndon words, permutations and trees*. Discrete Mathematics, 260, 153–158. (Introduces the Lyndon Tree and its Cartesian-Tree / permutation-descent isomorphism).
7. **Crochemore, M., & Rytter, W. (1995)**. *Squares, cubes, and time-space efficient string searching*. Algorithmica, 13(5), 405–425. (Proves the Three-Squares Lemma $|w| \ge |u| + |v|$ for primitive $u$).
8. **Fraenkel, A. S., & Simpson, J. (1998)**; **Brlek, S., & Li, S. (2022)**. *How many squares can a string contain?* Journal of Combinatorial Theory, Series A, 82(1), 112–120 (and Brlek–Li $\le N - \Theta(\log N)$ resolution).
9. **Kolpakov, R., & Kucherov, G. (1999)**. *Finding maximal repetitions in a word in linear time*. FOCS 1999, 596–604. (Proves $|\mathcal{R}(S)| = O(N)$ and $\sum \text{exp}(R) = O(N)$, formulating the Runs Conjecture $|\mathcal{R}(S)| < N$).
10. **Gil, J. Y., & Scott, D. A. (2012)**; **Kufleitner, M. (2009)**. *A Bijective String Sorting Transform (BWTS)*. arXiv:1201.3077. (Sentinel-free Bijective Burrows–Wheeler Transform via CFL factorization).
11. **Kociumaka, T., Radoszewski, J., Rytter, W., & Waleń, T. (2014 / 2016)**. *Minimal Suffixes, Significant Suffixes & Internal Pattern Matching Queries in a Text*. CPM 2014 / SODA 2015 / SICOMP. (Establishes the $O(\log N)$ Significant Suffixes candidate set under right-extensions and dyadic band reductions).
12. **Franek, F., Islam, A. S. M. S., Rahman, M. S., & Smyth, W. F. (2016)**; **Bille, P., et al. (2020)**. *Algorithms to compute the Lyndon Array*. Stringology 2016 / CPM 2020. ($O(N)$ ISA monotonic stack and Suffix-Tree constructions of the Lyndon Array).
13. **Bannai, H., I, T., Inenaga, S., Nakashima, Y., Takeda, M., & Tsuruta, K. (2015 / 2017)**. *The "Runs" Theorem*. SODA 2015 / SIAM Journal on Computing (SICOMP), 46(5), 1501–1514. (Landmark Lyndon-root proof that $|\mathcal{R}(S)| < N$ and $\sum \text{exp}(R) < 3N$, and $O(N)$ Lyndon-array runs enumeration).
14. **金策 (Jin Ce, Tsinghua University) (2019)**. *《字符串算法选讲》 (Selected Topics in String Algorithms — Runs, Lyndon Words & Significant Suffixes `显著后缀`)*. 2019 国家集训队论文 (Chinese IOI National Training Team Papers, 2019, pp. 1–31). (Canonical Chinese treatise unifying Duval's algorithm, the Significant Suffixes Theorem for `[ZJOI2017] 字符串`, Lyndon Arrays/Trees, and 2D sweep-line algorithms over Runs).
15. **Japanese Competitive Stringology Treatises (`[JA]`)**:
    - **`henkoku` (2020)**: *Runs (極大周期部分文字列) の理論と実装* (Complete derivation of Bannai et al.'s Runs theorem, double-order ISA monotonic stack, and Library Checker `Run Enumerate` reference implementation).
    - **`noshi91` & `maspypy`**: *Lyndon Factorization, Significant Suffixes, and De Bruijn Sequences in Competitive Programming*.
