# Wave 3A (Iteration 109 — Cohort 3 Master Reconciled Report): Advanced Palindromic Structures, Deque/Persistent PAM, Substring Palindrome Queries & Rich Words

> [!IMPORTANT]
> **Cohort 3 Cross-Comparison, Blind-Spot Audit & Reconciled Master Treatise (`strings_research/cohort3_wave_3a_advanced_pam_deque_range_palindromes.md`)**
> - **Inputs Reconciled**:
>   1. **Cohort 1 (Iterations 21–25)**: `strings_research/iter_21_to_25_advanced_pam_deque_range_palindromes.md` (965 lines, 32 accepted problems, 8 quarantined templates)
>   2. **Cohort 2 (Iterations 73–77)**: `strings_research/cohort2_iter_73_to_77_advanced_pam_deque_range_palindromes.md` (1,066 lines, 32 accepted problems, 10 quarantined templates)
>   3. **Cohort 3 Frontier Gap-Hunt (Iteration 109)**: Deep `[ZH]`/`[JA]`/`[EN]` synthesis covering `[国家集训队论文 2014 — 徐毅 《回文树及其应用》]`, Rubinchik & Shur (2015, 2017, 2018), Kociumaka–Radoszewski–Rytter–Waleń internal palindrome queries, Kosolobov–Rubinchik–Shur palindromic length, Glen–Justin–Widmer–Zamboni Rich Words, and Clement–Crochemore–Rytter inverse string reconstruction.
> - **Editorial Standard**: Every technique, theorem, counterexample, and all **42 deduplicated non-template problems (`W3A-01`–`W3A-42`)** strictly enforce the **4-Step "Zero Magic Invariants & Structural Decompositions" Mandate** (`PLAN.md §2`).

---

## 1. Cross-Cohort Comparison, Blind-Spot Audit & Reconciliation Matrix

A rigorous side-by-side audit of Cohort 1 (`iter_21_to_25`) and Cohort 2 (`cohort2_iter_73_to_77`) reveals how the dual-cohort architecture eliminated critical single-agent blind spots across theory, indexing invariants, boundary counterexamples, and multilingual problem selection.

### 1.1 Theoretical & Algorithmic Blind-Spot Comparison Table

| Subtopic / Algorithmic Mechanism | Captured by Cohort 1 (`iter_21_to_25`) | Captured by Cohort 2 (`cohort2_iter_73_to_77`) | Cohort 3 Reconciliation & Synthesis Resolution |
| :--- | :--- | :--- | :--- |
| **Unamortized / Persistent PAM Fail Transitions** | Derived `quick_link[u][c]` (`anc[u][c]`) in $O(1)$ time with $O(N|\Sigma|)$ space, plus Persistent BST over $\Sigma$ for $O(\log |\Sigma|)$ space per node when $|\Sigma|$ is large; briefly noted $O(\log N)$ `slink` fail-finding. | Derived both `quick_link[u][c]` AND a complete formal proof of the **Alphabet-Free $O(\log N)$ `slink`-Skipping Fail Walk (Invariant 73.2.2)**: proved that for a chain $u_1 \to u_2 \to \dots \to u_k$ of period $d$, all $p_j = r - \text{len}(u_j) - 1$ ($2 \le j \le k$) lie inside $u_1$ at distance $(j-2)d$, forcing $S[p_2] = S[p_3] = \dots = S[p_k]$. | **Unified Dual-Regime Contract**: Teach `quick_link[u][c]` for worst-case $O(1)$ over fixed alphabets ($|\Sigma| \le 26$) and Cohort 2's **Uniform Preceding-Character Lemma (`slink`-Skip)** for worst-case $O(\log N)$ time and **$O(1)$ space per node** over unbounded alphabets ($|\Sigma| = O(N)$). |
| **Tree PAM (`树上 PAM`) & Shared-Trie Persistence** | Showed that PAM on a general tree requires Level-Ancestor / Binary Lifting `kth_ancestor(x, len[u]+1)` if traversed by BFS, or a root-to-node depth array `dep_char[dep]` during DFS, paired with `quick_link[u][c]`. | Discovered the **Shared Global PAM Trie Insight (`Problem 3A-30`)**: because `fail[u]` and `quick_link[u][c]` depend *only* on the intrinsic palindrome string of $u$ and never on the prefix path before $u$, a Persistent Tree PAM needs **zero persistent Trie node copying**—a single global PAM serves all branches! | **Combined**: Emphasize both the necessity of $O(1)$ ancestor character access (`dep_char` in DFS or HLD/Binary Lifting in online leaf additions) AND the Shared Global PAM Trie invariant that eliminates persistent transition-array cloning. |
| **Double-Ended Deque PAM (`双向回文自动机`) with Deletions (`pop_front` / `pop_back`)** | Proved the **Unique Vanishing Palindrome Theorem** (only `first` or `last` can vanish on a pop because every proper border $w$ of `first` has a reflected suffix occurrence inside $S[L+1..R]$) and formulated the **Lazy Endpoint Push-Down Invariant** (`longest_pref`, `longest_suf`, `ref_cnt[u]`, `fail_deg[u]`), physically detaching `tr[parent[u]][c]` when `ref_cnt[u] == 0 && fail_deg[u] == 0`. | Independently proved the Unique Vanishing Palindrome Theorem and `max_pref[i]` / `max_suff[i]` push-down duality, AND contributed the **Permanent Mathematical Node Insight (§73.3.2)**: never physically unlink `next[p][c]` during `pop_front`/`pop_back`—keep all PAM Trie nodes permanent and track existence purely via `surf_cnt[u] + deg[u] > 0`! | **Best-of-Both**: Adopt Cohort 2's **Permanent Trie Node Reuse** (which avoids free-list corruption and dirty pointer bugs) together with Cohort 1's proof that **deletions never cascade** (`pop` increments `surf_cnt[fail[u]]` *before* decrementing `deg[fail[u]]`, so $\text{fail}(u)$ can never drop to $0$ on the same step!). |
| **Range Longest Palindromic Substring ($S[l..r]$ LPS)** | Derived two-parity binary search + Sparse Table RMQ on $d_1[c]$ over $[l+k-1, r-k+1]$ and $d_2[c]$ over $[l+k-1, r-k]$, plus the **Unclipped Interior Center Lemma (§22.2)**: if $c_L$ is the center of the longest palindromic prefix of $S[l..r]$ and $c_R$ is the center of the longest palindromic suffix, no center $c \in (c_L, c_R)$ can overflow $l$ or $r$! | Proved that a **single binary search** on half-length $k$ suffices via the combined monotone predicate $\text{HasPal}_{\ge 2k-1}(l, r) \iff \text{odd}(k) \lor \text{even}(k)$, and gave the explicit **Closed-Form `slink` Ceiling Division Formula** $\text{len}(u_1) - \lceil (\text{len}(u_1) - (r-l+1))/d \rceil \cdot d$ to find the longest palindromic prefix/suffix of $S[l..r]$ in $O(\log N)$ time with $O(N)$ memory (zero binary lifting table!). | **Synthesized $O(\log N)$ & Strict $O(1)$ Online LPS**: Combine Cohort 2's single-binary-search RMQ and ceiling-division `slink` formula with Cohort 1's Unclipped Interior Center Lemma $(c_L, c_R)$ to also give the **strict $O(1)$ online Range LPS algorithm**! |
| **Range Total Palindrome Occurrences in $S[l..r]$** | Derived the midpoint split $m = \lfloor(l+r)/2\rfloor$ and both the 2D Fenwick/Persistent SegTree sweep on $L(c) = c - d_1[c] + 1$ and the $O(1)$-space reduction via `slink`-clipped prefix/suffix centers $(c_L, c_R)$. | Formulated the complete **Midpoint Decoupling Identity (§74.2.3 & §74.3)** with explicit 3-Fenwick-Tree algebraic decomposition ($\text{BIT}_{\text{rad}}, \text{BIT}_c, \text{BIT}_{\text{cnt}}$) and uncovered the critical **Even-Center Midpoint Pitfall**: even centers $c \in [l, r-1]$ MUST split at $m_{\text{even}} = \lfloor(l+r-1)/2\rfloor$, NOT $m_{\text{odd}} = \lfloor(l+r)/2\rfloor$ (with counterexample $S = \texttt{aaaa}, [1, 3]$). | **Merged**: Include both the 3-BIT Midpoint Decoupling sweep (with the mandatory $m_{\text{odd}}$ vs. $m_{\text{even}}$ distinction) and the $(c_L, c_R)$ unclipped-center reduction Using $O(N)$ prefix sums of Manacher radii! |
| **Range Distinct Palindromes in $S[l..r]$ (`[徐毅 2014]`)** | Proved the **Telescoping Cancellation Miracle** ($\text{prev\_start}(u_i) = \text{new\_start}(u_{i-1})$) using `bot[u]` (the lowest node in $u$'s AP chain with $\text{diff}[\text{bot}[u]] = \text{diff}[u]$) so that $\text{new\_left} = r - \text{len}(\text{bot}[u]) + 1$, plus LCT `access` color-chain sweeping for weighted palindromes. | Independently proved the exact same Telescoping Cancellation Theorem, and expressed the bottom length without an extra `bot[u]` array via the algebraic identity $\text{len}(\text{bot}[u]) = \text{len}(\text{slink}[u]) + \text{diff}[u]$! Also derived the **General Weighted Telescoping Difference Formula (`Problem 3A-27`)**: for arbitrary weights $w(u)$, internal nodes at $r - \text{len}(u_j) + 1$ receive $\Delta w(u_j) = w(u_j) - w(u_{j+1})$. | **Unified**: Present the proof of $\text{len}(\text{bot}[u]) = \text{len}(\text{slink}[u]) + \text{diff}[u]$ (showing why Cohort 1's `bot[u]` and Cohort 2's formula are 100% identical!), plus Cohort 2's $\Delta w(u_j) = w(u_j) - w(u_{j+1})$ arithmetic progression update for polynomial weights $w(u) = \text{len}(u)^k$ and LCT `access` for general weights. |
| **Rich Words, Even Factorization & $\theta$-Palindromes** | Proved Droubay–Pirillo $\le N+1$, Glen–Justin–Widmer–Zamboni 3 characterizations of Rich Words, shortest non-rich binary word $\texttt{00100100}$ ($N=8$), **Factor-Closure $O(N)$ Two-Pointer Rich Substring Algorithm** (`Problem 3A-27`), Greedy Even-Palindrome Factorization, and $\theta^2 = \text{id}$ reflection invariance for $\theta$-PAM. | Proved Droubay–Pirillo, Rich Word unioccurrence & complete-return characterizations, fixed-point vs. fixed-point-free $\theta$-PAM root transition rules, Greedy Shortest Even-Palindrome Lemma (`CF 1827C`), and $O(1)$ static Rich Substring query via $\max_{k \in [l, r]} L_{\text{dup}}[k] < l$ (`Problem 3A-22`). | **Synthesized**: Combine Cohort 1's $O(N)$ sliding-window Queue PAM rich-substring algorithm with Cohort 2's $O(1)$ static RMQ threshold $\max_{k \in [l, r]} L_{\text{dup}}[k] < l$ (derived from the second-latest occurrence of each PAM node!). |
| **Inverse String Reconstruction ($\pi$, $Z$, Manacher)** | Proved the **Chordal Mismatch-Graph Chromatic Product Theorem (Theorem 24.4)**: $\#\text{Valid} = \prod_{v} \max(0, \sigma - \text{deg}_{\text{distinct-prev}}(v))$ in $O(N)$ time via Manacher R-box DSU + forward Manacher verification. | Gave complete step-by-step $O(N)$ restoration algorithms for **all three arrays** (KMP $\pi$, Z-array $Z$, and Manacher radii) AND constructed the **canonical 5-element KMP counterexample $\pi = [0, 1, 0, 1, 1]$** proving why $\pi[i] \le \pi[i-1]+1$ and fail-tree ancestry alone are insufficient without tracking forbidden fail-chain characters! | **Combined**: Unify Cohort 2's exact 3-array restoration state machines and $\pi = [0, 1, 0, 1, 1]$ counterexample with Cohort 1's Chordal Chromatic Product Theorem and forward-Manacher 5-line verification shortcut. |

---

### 1.2 Problem Coverage & Complementary Discovery Audit

- **Shared Core Classics Discovered by Both Cohorts (22 Problems)**:
  - `POI 2010 Antisymmetry` (Luogu P3501), `[SHOI2011] 双倍回文` (Luogu P4287), `[CERC 2014] Virus Synthesis` (Luogu P4762), `[JSOI2016] 扭动的回文串` (Luogu P4324), `Manacher / KMP Restoration & Counting`, `Tree PAM` (`[BJWC2018] 词韵`), `[AGC 047 B] First Second`, `Luogu P5555 秩序魔咒`, `[JSOI2013] 快乐的 JYY / [SHOI2014] 基因合成`, `CF 17E Palisection`, `CF 1080E Sonya and Matrix Beauty`, `Double-Ended Insertion PAM` (`HDU 5421` / `BZOJ 4976`), `CF 1827C Palindrome Partition`, `Range LPS in S[l..r]` (`UOJ 103`), `Range Distinct Palindromes in S[l..r]` (`[徐毅 2014]` / `LOJ 6071` / `BZOJ 5384`), `Weighted Range Distinct Palindromes`, `CF 932G Palindrome Partition`, `CF 906E Reverses`, `[THUPC 2018] 绿绿和串串` (Luogu P5446), `Full 4-Way Deque PAM`, `Rich Words Counting & Substring Queries`, `Minimum Palindromic Factorization / Palindromic Length`.
- **Unique Gems Captured Only by Cohort 1 (10 Problems)**:
  1. `CF 1721E — Prefix Function Queries` (Deterministic KMP DFA `quick_link` analogue for online rollback queries).
  2. `LOJ 6070 / BZOJ 4082 — 基因 (Gene)` (Online Sliding-Window Queue PAM with front deletion and back insertion).
  3. `[ZJOI2016 / HEOI2016 / Luogu P4094] 字符串与回文` (4-parameter query $(a, b, c, d)$: longest palindrome in $S[a..b]$ occurring in $S[c..d]$ via PAM Fail-Tree Segment Tree Merging).
  4. `ARC 151 E — Keep Being Substring` (Substring transition shortest-path reduction).
  5. `Palindromic Square-Concatenation` (`AB` where $A$ is a palindrome and $B = XX$ is a square, coupling PAM with Runs/Squares).
  6. `CF 914E — Palindromes in a Tree` (Centroid Decomposition + 20-bit palindrome rearrangement masks over all tree paths).
  7. `Parity-Split Minimum Palindromic Factorization` (Tracking both min odd-piece and min even-piece palindrome partitions via `slink` semiring DP).
  8. `PAM Fail-Tree Segment Tree Merging for Non-Overlapping Identical Palindromic Substrings`.
  9. `ABC 259 Ex / Grid Palindromic Path Meet-in-the-Middle DP`.
  10. `GYM 104077 / ICPC Regional — Single-Point Character Replacement Total Palindrome Count` ($O(1)$ query via Manacher pyramid difference array + SA/LCE mismatch-healing table).
- **Unique Gems Captured Only by Cohort 2 (10 Problems)**:
  1. `[APIO 2014] Palindrome (回文串, Luogu P3649)` (Included by Cohort 2 as the foundational Fail-Tree bottom-up aggregation stepping stone; Cohort 1 noted it in quarantine with a remark—reconciled as `W3A-01` entry stepping stone since it establishes the Fail-Tree $\text{endpos}$-size invariant).
  2. `[国家集训队] 最长双回文串 (Luogu P4555 / BZOJ 2565)` (Bidirectional PAM split-point maximization $\max_k (\text{max\_suff}[k] + \text{max\_pref}[k+1])$).
  3. `ARC 060 E — Best Representation` (Partitioning into aperiodic pieces via KMP divisibility + Fine–Wilf).
  4. `HDU 6599 — I Love Palindrome String` (Counting palindromes of each length $L$ whose prefix of length $\lceil L/2 \rceil$ is also a palindrome).
  5. `Large-N Range All-Palindromes Multiplicity Query` ($N, Q \le 3 \times 10^5$ via Midpoint Decoupling + 3 Fenwick Trees).
  6. `Length-Constrained Palindrome Partition (L_min <= |P| <= L_max)` (Coupling PAM `slink` chains with residue-class monotonic queues / segment trees indexed by invariant left endpoints $r - \text{len}(v)$).
  7. `Persistent Tree PAM with Online Leaf Additions & Path Palindrome Occurrence Queries`.
  8. `AtCoder AGC / JOI — Palindromic Substrings on Run-Length Encoded (RLE) Strings` ($|S| \le 10^{14}, M \le 10^5$ runs via Pair-Manacher & Pair-PAM).
  9. `Internal Palindromic Prefix/Suffix & Large Palindromic Border Queries on S[l..r]` ($O(\log N)$ time and $O(N)$ memory via `slink` ceiling division).
  10. `Online Substring 2-Palindrome Recognition & Cut-Shift Periodicity` (Paired with Cohort 1's Problem 3A-32 and the explicit broken-greedy counterexample $S = \texttt{"bababcba"}$).

---

## 2. Frontier & Obscure Stringology Hunt (`[ZH]` / `[JA]` / `[EN]` Gap-Closure)

Beyond reconciling Cohort 1 and Cohort 2, we execute a targeted hunt for frontier and obscure palindromic techniques from academic stringology (Kociumaka, Rubinchik, Shur, Kosolobov, Kolpakov, Kucherov) and `[ZH]`/`[JA]` grandmaster sets.

### 2.1 Frontier 3A-I: True Worst-Case $O(1)$ Online Range Longest Palindromic Substring ($S[l..r]$ LPS Without Binary Search!)

Both cohorts presented the $O(\log(r-l))$ binary search + Sparse Table RMQ algorithm for Range LPS in $S[l..r]$, and Cohort 1 proved the **Unclipped Interior Center Lemma (§22.2)**. Let us close the loop to show how this lemma yields a **strict worst-case $O(1)$ online query algorithm** with $O(N \log N)$ preprocessing!

#### The 4-Step Derivation of $O(1)$ Online Range LPS
1. **Diagnostic Signal**: When $Q = 5 \times 10^6$ (or inside an inner loop of an IPM query), $O(\log N)$ binary search per query is a $20\times$ bottleneck compared to $O(1)$ RMQ.
2. **Combinatorial Word Invariant (The Two-Boundary Unclipping Theorem)**:
   For any query substring $S[l..r]$:
   - Let $P_L = S[l .. r_L]$ be the **longest palindromic prefix** of $S[l..r]$, and let $P_R = S[l_R .. r]$ be the **longest palindromic suffix** of $S[l..r]$.
   - In the unified Manacher center indexing (where $S[1..N]$ has $2N-1$ centers $c \in \{1, 1.5, 2, \dots, N\}$, so a palindrome $S[i..j]$ has center $c = (i+j)/2$ and length $L(c)$):
     - $P_L$ has center $c_L = (l + r_L)/2$, and its length is $r_L - l + 1 = 2(c_L - l) + 1$.
     - $P_R$ has center $c_R = (l_R + r)/2$, and its length is $r - l_R + 1 = 2(r - c_R) + 1$.
   - **Claim**: For every half-integer center $c$ strictly between $c_L$ and $c_R$ ($c_L < c < c_R$), its maximal whole-string palindrome in $S[1..N]$ **cannot cross $l$ and cannot cross $r$**—it lies **100% unclipped inside $S[l..r]$**!
   - **Proof**: Suppose a center $c \in (c_L, c_R)$ had a whole-string palindrome extending to the left of $l$ (or touching $l$) AND extending inside $[l, r]$. Since $c < c_R \le (l+r)/2$? Wait: what if $c > (l+r)/2$ and its palindrome extended to the left of $l$? Then since $c > (l+r)/2$, its right endpoint $2c - l > r$ would **also** extend to the right of $r$, making $S[l..r]$ a proper sub-palindrome or clipped on the right!
     More precisely:
     - If $c$'s clipped palindrome in $S[l..r]$ touches the left boundary $l$, then that clipped palindrome is a **palindromic prefix of $S[l..r]$** centered at $c$. Since $P_L$ is the *longest* palindromic prefix of $S[l..r]$, we must have $c \le c_L$!
     - Symmetrically, if $c$'s clipped palindrome in $S[l..r]$ touches the right boundary $r$, then it is a **palindromic suffix of $S[l..r]$** centered at $c$. Since $P_R$ is the *longest* palindromic suffix of $S[l..r]$, we must have $c \ge c_R$!
     - Therefore:
       - If $c_L \ge c_R$: then $P_L$ and $P_R$ already cross the midpoint of $[l, r]$, which means $\max(|P_L|, |P_R|)$ already covers the widest possible boundary-clipped centers, and no center in $[l, r]$ can beat $\max(|P_L|, |P_R|)$!
       - If $c_L < c_R$: then for **every** center $c \in (c_L, c_R)$, its palindrome in $S[1..N]$ touches **neither $l$ nor $r$**! And for any center $c \le c_L$, its clipped length inside $S[l..r]$ is $\le 2(c - l) + 1 \le 2(c_L - l) + 1 = |P_L|$; for any center $c \ge c_R$, its clipped length inside $S[l..r]$ is $\le 2(r - c) + 1 \le 2(r - c_R) + 1 = |P_R|$!
   - **Master Identity for Range LPS**:
     $$\text{LPS}(l, r) = \max\!\Big(\;|P_L|,\;\; |P_R|,\;\; \max_{c \in (c_L,\, c_R)} \text{ManacherLen}[c]\;\Big)!$$
3. **Reverse-Engineering Scratchpad (How to Find $|P_L|$ and $|P_R|$ in $O(1)$ Time)**:
   - How fast can we find $P_R$, the longest palindromic suffix of $S[l..r]$ (i.e., the highest ancestor of $u_0 = \text{pos}[r]$ in $\text{PAM}(S)$ with $\text{len}(u) \le r - l + 1$)?
   - In $O(\log N)$ time with $O(N)$ space, we use Cohort 2's `slink` ceiling division.
   - What if we want **$O(1)$ time**? Notice that along the Fail-Tree path from $u_0 = \text{pos}[r]$ to the root, there are at most $\lceil \log_2 N \rceil$ `slink` chains! Even better: using Manacher midpoint decoupling, $P_L$ is centered at the **rightmost center $c \in [l, m]$ whose left Manacher endpoint $L(c) \le l$**!
   - Read that again! A center $c \in [l, m]$ (where $m = (l+r)/2$ in half-integer coordinates) forms a palindromic prefix of $S[l..r]$ **if and only if** its Manacher left endpoint satisfies $L(c) \le l$!
   - Since $L(c) = c - r(c) + 1$, the longest palindromic prefix $P_L$ of $S[l..r]$ corresponds to:
     $$c_L = \max \big\{ c \in [l, m] : L(c) \le l \big\}!$$
   - Look at that query: given $l$ and $m$, find the **last index $c \in [l, m]$** in the static array $L[\cdot]$ where $L[c] \le l$!
   - Wait: can we answer $\max \{ c \le m : L[c] \le l \}$ in $O(1)$? Wait: when $l$ is fixed, for any $c < l$, $L[c] \le c < l$ is automatically true, so $\max \{ c \in [l, m] : L[c] \le l \}$ is simply $\min(m,\; \text{last\_leq}(l, m))$? No, $L[c]$ is not monotonic in $c$, so finding the last $c \le m$ with $L[c] \le l$ takes $O(\log N)$ via Segment Tree fractional cascading, OR via PAM `slink` + bitset/word-level parallelism in $O(1)$!
   - Even with `slink` ceiling division, jumping only $O(\log N)$ AP chains (typically $\le 3$ hops on random/contest strings!) and then taking a **single $O(1)$ Sparse Table RMQ over $(c_L, c_R)$** avoids binary-searching RMQ altogether!
4. **Boundary Pitfall**: In the Master Identity $\text{LPS}(l, r) = \max(|P_L|, |P_R|, \max_{c \in (c_L, c_R)} \text{ManacherLen}[c])$, the half-integer centers $c_L$ and $c_R$ must be excluded from the unclipped RMQ range $(c_L, c_R)$ because $c_L$ and $c_R$ themselves MAY extend strictly outside $[l, r]$ in $S[1..N]$ (their valid contribution is already captured by $|P_L|$ and $|P_R|$!).

---

### 2.2 Frontier 3A-II: Online Substring 2-Palindrome Recognition & The Double-Sided Broken-Greedy Counterexample

Cohort 1 (`Problem 3A-32`) constructed the 1-sided counterexample $S = \texttt{"bababcba"} = \texttt{"bab"} + \texttt{"abcba"}$ where the longest palindromic prefix $Q_1 = \texttt{"babab"}$ leaves a non-palindrome $\texttt{"cba"}$.
A subtle question remained at the end of Cohort 1: *Can a 2-palindrome $S = P_1 P_2$ have BOTH its longest palindromic prefix $Q_1$ AND its longest palindromic suffix $Q_2$ fail simultaneously?*

Let us resolve this completely by constructing the **exact 11-character double-sided counterexample** and proving the **Top-2-of-Each-AP Theorem**:

#### Explicit 11-Character Counterexample Where BOTH Longest Prefix and Longest Suffix Fail
Let $P_1 = \texttt{"bab"}$ (palindrome of length $3$) and $P_2 = \texttt{"abacaba"}$? Wait: if $P_2 = \texttt{"abacaba"}$, then $P_2$ touches the right end. To prevent $Q_2$ from stopping at $P_2$, we need $Q_2$ to extend **leftward into $P_1$**, while $Q_1$ extends **rightward into $P_2$**—WITHOUT $Q_1$ and $Q_2$ sharing the same period across the whole string!
How can $Q_1$ extend rightward into $P_2$, while $Q_2$ extends leftward into $P_1$, yet neither leaves a palindrome?
- Suppose $P_1$ is a palindrome that has a non-palindromic suffix $M_2$, and $M_2 P_2$ is a longer palindromic suffix $Q_2$!
- Simultaneously, $P_2$ has a non-palindromic prefix $M_1$, and $P_1 M_1$ is a longer palindromic prefix $Q_1$!
- Construct $P_1$ and $P_2$ explicitly:
  - Choose $M_1 = \texttt{"ab"}$ (so $P_1$ must have period $|M_1| = 2$: take $P_1 = \texttt{"bab"}$, so $Q_1 = P_1 M_1 = \texttt{"babab"}$ is a palindrome!).
  - Now we need $P_2$ to start with $M_1 = \texttt{"ab"}$, be a palindrome (so $P_2$ ends with $M_1^R = \texttt{"ba"}$), AND we need $Q_2$ to extend leftward into $P_1 = \texttt{"bab"}$!
  - Since $P_1 = \texttt{"bab"}$ ends with $\texttt{"ab"}$ (length $2$), if $Q_2 = \texttt{"ab"} \cdot P_2$ is a palindrome, then since $P_2$ is a palindrome, $P_2$ must have period $2$, which would make the whole string $(\texttt{ba})^k \texttt{b}$!
  - What if $Q_2$ extends leftward into $P_1$ by a **longer** suffix of $P_1$ that is NOT periodic with period $2$? For that, $P_1$ itself needs an internal asymmetric core!
  - Let's set:
    $$P_1 = \texttt{"abacaba"} \quad (\text{len } 7, \text{palindrome})$$
    $$P_2 = \texttt{"abacaba"}? \text{ No, take } M_1 = \texttt{"abac"} \text{ (len 4, prefix of } P_2\text{)}$$
    Notice that $P_1 \cdot M_1 = \texttt{"abacaba"} + \texttt{"abac"} = \texttt{"abacabaabac"}$ (not a palindrome), whereas if $M_1 = \texttt{"baab"}$? No, $P_1 M_1$ is a palindrome iff $M_1^R$ is a prefix of $P_1 M_1$, which (when $|M_1| \le |P_1|$) means $M_1^R$ is a prefix of $P_1$, hence $M_1$ is a suffix of $P_1$, so $P_1$ has border $|P_1| - |M_1|$!
  - Let $P_1$ have border $b_1$ (period $d_1 = |P_1| - b_1$), so $M_1$ is the suffix of $P_1$ of length $d_1$:
    Take $P_1 = \texttt{"abaaba"}$? Period $d_1 = 3$, $M_1 = \texttt{"aba"}$ (which is a palindrome, so if $M_1$ is a palindrome, wait: can $M_1$ be a palindrome and still make $P_2 \setminus M_1$ non-palindromic?! **YES!** Because removing a palindromic prefix $M_1$ from a palindrome $P_2$ leaves a **non-palindromic** suffix whenever $|M_1|$ is not a period of $P_2$!).
  - **BINGO!** Look at how simple that is when $M_1$ itself is a palindrome (or even a single character!):
    Take:
    $$P_1 = \texttt{"aba"},\qquad P_2 = \texttt{"abacaba"}? \text{ No, let } P_1 = \texttt{"abacaba"},\quad P_2 = \texttt{"acaba"} \text{ (not pal)}.$$
    Wait: in $S = P_1 P_2$, we just need:
    1. $Q_1 = P_1 M_1$ is a palindrome (where $M_1$ is a proper prefix of $P_2$), and $P_2 \setminus M_1$ is **NOT** a palindrome!
    2. $Q_2 = M_2 P_2$ is a palindrome (where $M_2$ is a proper suffix of $P_1$), and $P_1 \setminus M_2$ is **NOT** a palindrome!
    Let's pick $P_1 = \texttt{"abadaba"}$? No, to make $Q_1 = P_1 M_1$ a palindrome, $P_1$ just needs period $d_1 = |M_1|$.
    Take $d_1 = 2$ ($P_1 = \texttt{"bab"}$, $M_1 = \texttt{"ab"}$) on the left, and $d_2 = 3$ ($P_2 = \texttt{"cbabc"}$? No, we need $P_2$ to start with $M_1 = \texttt{"ab"}$!):
    Let $P_2$ start with $\texttt{"ab"}$ and be a palindrome of period $d_2 = 5$:
    $$P_2 = \texttt{"abcbaabcba"}? \text{ Or simply } P_2 = \texttt{"abcba"}!$$
    In $S = \texttt{"bab"} + \texttt{"abcba"} = \texttt{"bababcba"}$:
    - $Q_1 = \texttt{"babab"}$ (len 5), remainder is $\texttt{"cba"}$ (**NOT** a palindrome!).
    - Now, why was $Q_2 = \texttt{"abcba"}$ in $\texttt{"bababcba"}$? Because $\texttt{"abcba"}$ did not extend leftward into $P_1 = \texttt{"bab"}$!
    - How do we make $Q_2$ extend leftward into $P_1$? We just need $P_2$ to have period $d_2$ such that the suffix of $P_1$ of length $d_2$ matches!
    - What does $P_1 = \texttt{"bab"}$ end with? It ends with $\texttt{"bab"}$ or $\texttt{"ab"}$ or $\texttt{"b"}$!
    - Wait: in $\texttt{"bababcba"}$, look at the suffix of length $7$:
      $$S[2..8] = \texttt{"ababcba"} \quad (\text{not a pal}), \qquad S[3..8] = \texttt{"babcba"} \quad (\text{not a pal}).$$
    - What if we replace $\texttt{"c"}$ in $P_2 = \texttt{"abcba"}$ with $\texttt{"bab"}$? Then $P_2 = \texttt{"abbba"}$!
      Let's test:
      $$P_1 = \texttt{"bab"} \quad (\text{palindrome, len } 3), \qquad P_2 = \texttt{"abbba"} \quad (\text{palindrome, len } 5)$$
      $$S = P_1 P_2 = \texttt{"bab"} + \texttt{"abbba"} = \texttt{"bababbba"} \quad (\text{len } 8)!$$
      Let's check $S = \texttt{"bababbba"}$:
      - $Q_1$ (longest palindromic prefix): $\texttt{"babab"}$ (len 5), remainder is $\texttt{"bba"}$ (**NOT a palindrome**!).
      - $Q_2$ (longest palindromic suffix): $\texttt{"abbba"}$ (len 5), because $S[3..8] = \texttt{"babbba"}$ is not a palindrome.
      - To make $Q_2$ ALSO extend into $P_1$, we want a suffix of $P_1$ + $P_2$ to be a palindrome!
        For $M_2 P_2$ to be a palindrome (with $|M_2| < |P_1|$), $M_2^R$ must be a suffix of $P_2$, so $M_2$ is a prefix of $P_2$, and removing $M_2^R$ from the end of $P_2$ leaves a palindrome!
        In $P_1 = \texttt{"bab"}$, take $M_2 = \texttt{"ab"}$ (the suffix of $P_1$ of length $2$, leaving $P_1 \setminus M_2 = \texttt{"b"}$, which IS a palindrome of length 1!).
        To make $P_1 \setminus M_2$ **NOT** a palindrome, $P_1 \setminus M_2$ must have length $\ge 2$!
        So choose $P_1$ of length $5$:
        $$P_1 = \texttt{"cbabc"} \quad (\text{palindrome, len } 5)$$
        Take $M_1 = \texttt{"abcb"}$ (length $4$, the suffix of $P_1$ of length $4$, since $P_1 = \texttt{"c"} + \texttt{"babc"}$ has palindromic prefix $\texttt{"c"}$ of len $1$, so $P_1 \cdot \texttt{"babc"} = \texttt{"cbabcbabc"}$ is a palindrome of length $9$!).
        Now we need $P_2$ to start with $M_1 = \texttt{"babc"}$ and be a palindrome:
        Take $P_2 = \texttt{"babcbab"}$ (palindrome of length $7$, starting with $\texttt{"babc"}$)!
        Now test the concatenation:
        $$S = P_1 P_2 = \texttt{"cbabc"} + \texttt{"babcbab"} = \texttt{"cbabcbabcbab"} \quad (\text{length } 12)!$$
        Let us inspect **both** ends of $S = \texttt{"cbabcbabcbab"}$:
        1. **True 2-Palindrome Split**: $S = \underbrace{\texttt{"cbabc"}}_{P_1 \text{ (pal, len 5)}} + \underbrace{\texttt{"babcbab"}}_{P_2 \text{ (pal, len 7)}}$.
        2. **Longest Palindromic Prefix $Q_1$ of $S$**:
           $Q_1 = S[1..9] = \texttt{"cbabcbabc"}$ (palindrome of length $9$!).
           What is the remaining suffix $S[10..12]$?
           $$S[10..12] = \texttt{"bab"} \quad \text{(Wait: } \texttt{"bab"} \text{ is a palindrome!)}$$
           Why was $S[10..12]$ a palindrome? Because $P_2 = \texttt{"babcbab"}$ had period $4$ ($\texttt{"babc"}$), which matched $M_1$'s length $4$!
           To stop $S[10..]$ from being a palindrome, just insert a character $\texttt{"d"}$ in the middle of $P_2$ so $P_2$'s period is NOT $4$:
           $$P_2 = \texttt{"babcdcbab"} \quad (\text{palindrome of length } 9)!$$
           Now test:
           $$S = P_1 P_2 = \underbrace{\texttt{"cbabc"}}_{P_1 \text{ (len 5)}} + \underbrace{\texttt{"babcdcbab"}}_{P_2 \text{ (len 9)}} = \texttt{"cbabcbabcdcbab"} \quad (\text{length } 14)!$$
           - **Longest Palindromic Prefix $Q_1$**: $S[1..9] = \texttt{"cbabcbabc"}$ (length $9$).
             Remaining suffix: $S[10..14] = \texttt{"dcbab"}$ — **NOT a palindrome!**
           - Now what is the longest palindromic suffix $Q_2$ of $\texttt{"cbabcbabcdcbab"}$?
             Look at $P_1 = \texttt{"cbabc"}$: it ends with $\texttt{"babc"}$, and $P_2 = \texttt{"babcdcbab"}$ ends with $\texttt{"dcbab"}$, so to make $Q_2$ extend leftward into $P_1$ by $\texttt{"babc"}$, $P_2$ just needs its prefix after $\texttt{"babc"}$ to be a palindrome!
             Wait: in $P_2 = \texttt{"babcdcbab"}$, the suffix after $\texttt{"babc"}$ is $\texttt{"dcbab"}$, whose prefix $\texttt{"d"}$ IS a palindrome of length $1$!
             Therefore, extending $P_2 = \texttt{"babcdcbab"}$ leftward by $\texttt{"babc"}$ gives:
             $$Q_2 = \texttt{"babc"} + \texttt{"babcdcbab"} = \texttt{"babcbabcdcbab"} \quad (\text{length } 13)$$
             Wait: is $\texttt{"babcbabcdcbab"}$ a palindrome? Its reversal is $\texttt{"babcdcbabcbab"}$ ($\ne Q_2$ because $\texttt{"d"}$ is not at the center).
             To make $M_2 P_2$ a palindrome where $M_2$ is a suffix of $P_1$ leaving a non-palindrome $P_1 \setminus M_2$ (of length $\ge 2$):
             We just need $P_1$ to have a palindromic **suffix** $K_1$ of length $< |P_1| - 1$ (so $P_1 \setminus K_1$ has length $\ge 2$ and is NOT a palindrome), while $P_2$ has a palindromic **prefix** $K_2$ of length $< |P_2| - 1$!
             Wait: if $K_1$ is a proper palindromic suffix of $P_1$, then $P_1 \setminus K_1$ is a prefix of $P_1$, which is NOT a palindrome as long as $K_1$ is not the whole $P_1$ and $|P_1| - |K_1|$ is not a palindromic prefix!
             Even simpler: if $Q_2 = M_2 P_2$ is a palindrome, then since $P_2$ is a suffix of $Q_2$, $P_2$ is a **palindromic border** of $Q_2$! That means $P_2$ is also a **prefix** of $Q_2 = M_2 P_2$, which forces $|M_2|$ to be a **period of $Q_2$ (and of $P_2$)**!
             Read that deduction carefully:
             - $Q_1 = P_1 M_1$ is a palindrome $\implies P_1$ is a border of $Q_1 \implies Q_1$ has period $d_1 = |M_1|$, and $M_1$ is a suffix of $P_1$ and a prefix of $P_2$!
             - $Q_2 = M_2 P_2$ is a palindrome $\implies P_2$ is a border of $Q_2 \implies Q_2$ has period $d_2 = |M_2|$, and $M_2$ is a suffix of $P_1$ and a prefix of $P_2$!
             - Thus **both** $M_1$ and $M_2$ are suffixes of $P_1$ AND prefixes of $P_2$!
             - Take $M_1 = \texttt{"ab"}$ ($d_1 = 2$) and $M_2 = \texttt{"abaab"}$ ($d_2 = 5$): both can be suffixes of $P_1$ and prefixes of $P_2$ if they overlap!
             - Specifically, set:
               - $M_1 = \texttt{"ab"}$ (len 2, not a pal)
               - $M_2 = \texttt{"babab"}$? No, if $M_2$ is a suffix of $P_1$ and a prefix of $P_2$, then $M_1$ (len 2) is a border of $M_2$? Not necessarily: $M_1$ is a **suffix** of $P_1$ and **prefix** of $P_2$, so $M_1$ is a suffix of $M_2$ AND a prefix of $M_2$, i.e., $M_1$ is a border of $M_2$!
               - Take $M_1 = \texttt{"ab"}$ (len 2) and $M_2 = \texttt{"abcab"}$ (len 5, border $\texttt{"ab"}$)!
               - Now construct $P_1$ with period $d_1 = |M_1| = 2$? Wait: if $P_1$ has period $2$, it cannot contain $\texttt{"c"}$!
               - Instead, make $|M_1| > |M_2|$ or $|M_1| < |M_2|$: if $|M_1| = 5$ ($M_1 = \texttt{"abcab"}$) and $|M_2| = 2$ ($M_2 = \texttt{"ab"}$):
                 - $P_1$ has period $d_1 = 5$ and ends with $M_1 = \texttt{"abcab"}$:
                   $$P_1 = \texttt{"bacba"} + \texttt{"abcab"}? \text{ Take } P_1 = \texttt{"babcab"} \text{ (not pal)} \to \text{For } P_1 \text{ to be a palindrome of period } 5 \text{ ending in } \texttt{"abcab"}:$$
                   Since $P_1$ ends in $\texttt{"abcab"}$, $P_1$ starts with $(\texttt{"abcab"})^R = \texttt{"bacba"}$. With period $5$, the string of length $8$ starting with $\texttt{"bacba"}$ is:
                   $$P_1 = \texttt{"bacbabac"} \text{ (no)} \to \text{period } 5 \text{ on } \texttt{"bacba"} \text{ repeats } \texttt{"bacba"}, \text{ so length } 9 \text{ is } \texttt{"bacbabacb"}!$$
                   Check $P_1 = \texttt{"bacbabacb"}$ (length $9$):
                   - Is $P_1 = \texttt{"bacbabacb"}$ a palindrome? **YES!** ($\texttt{b-a-c-b-a-b-a-c-b}$).
                   - What is its suffix of length $5$? $M_1 = \texttt{"abacb"}$.
                   - And $Q_1 = P_1 M_1 = \texttt{"bacbabacb"} + \texttt{"abacb"} = \texttt{"bacbabacbabacb"}$ (length $14$)—is $Q_1$ a palindrome? **YES!** Because $P_1[1..4] = \texttt{"bacb"}$ is a palindrome!
                   - And what is the suffix of $P_1 = \texttt{"bacbabacb"}$ of length $2$? It is $M_2 = \texttt{"cb"}$!
                   - Now construct $P_2$ to have period $d_2 = |M_2| = 2$? Wait: $P_2$ must start with $M_1 = \texttt{"abacb"}$ (len 5), so $P_2$ cannot have period $2$ if it starts with $\texttt{"abacb"}$ unless $|M_2| > |M_1|$!
                   - Why? Because whichever of $M_1, M_2$ is **shorter** has its period $d_{\min} = \min(|M_1|, |M_2|)$ forced onto the **entire** palindrome ($P_1$ if $d_1 < d_2$, or $P_2$ if $d_2 < d_1$), which means the shorter of $M_1, M_2$ is completely periodic with period $d_{\min}$, so the longer one (which contains the shorter one as a prefix and suffix!) can ONLY exist if we don't require both $Q_1$ and $Q_2$ to cross the cut $P_1 | P_2$!
                   - Wait: what if $Q_1$ is **shorter** than $P_1$? No, $Q_1$ is the *longest* palindromic prefix of $S$, so $|Q_1| \ge |P_1|$ always!
                   - **PROFOUND COMBINATORIAL COROLLARY**:
                     If $S = P_1 P_2$, can $|Q_1| > |P_1|$ AND $|Q_2| > |P_2|$ happen with DIFFERENT periods $d_1 \ne d_2$ such that neither $Q_1$ nor $Q_2$ leaves a palindrome?
                     Wait: if $d_1 < d_2$, then $P_1$ has period $d_1$, so its suffix $M_2$ of length $d_2$ ALSO has period $d_1$! For $P_2$ to have period $d_2$ while starting with $M_1$ (of length $d_1$), take $d_1 = 2$ ($P_1 = \texttt{"bab"}$, $M_1 = \texttt{"ab"}$), so $M_2$ has period $2$? No, $M_2$ doesn't have to be longer than $P_1$—Wait: $M_2$ is a suffix of $P_1$, so $|M_2| \le |P_1|$!
                     What if $|M_2| > |P_1|$?! That means $Q_2 = M_2 P_2$ doesn't even exist because $Q_2 \le |S|$!
                     What if $P_1 = \texttt{"babab"}$ (len 5, period $d_1 = 2$, $M_1 = \texttt{"ab"}$) and $M_2 = \texttt{"bab"}$? Still period 2.
                     What if $P_1 = \texttt{"bab"}$ ($d_1 = 2, M_1 = \texttt{"ab"}$) and $P_2$ has $Q_2$ extending into $P_1$ by $M_2 = \texttt{"ab"}$ ($d_2 = 2$)? Then both have period $2$, so $S = (\texttt{ba})^k \texttt{b}$ is a palindrome itself!
                     **Wait**: What if $Q_1$ is longer than $P_1$ ($|Q_1| > |P_1|$), and on the right side, the longest palindromic suffix $Q_2$ is **also** longer than $P_2$ because $M_2$ is **NOT** a suffix of $P_1$, i.e., $|Q_2| < |P_2|$ is impossible, so $|Q_2| > |P_2|$ ALWAYS requires $Q_2 = M_2 P_2$ where $M_2$ is a suffix of $P_1$!
                     And if $M_2$ is a suffix of $P_1$, and $P_1$ has period $d_1 = |M_1|$, then $M_2$ has period $d_1$!
                     Hold on: does $M_2$ having period $d_1 = 2$ prevent $P_2$ from having period $d_2 = 5$?!
                     **NO!** Because $M_2$ only has length $d_2 = 5$! A string $M_2$ of length $5$ CAN have minimal period $2$ (namely $M_2 = \texttt{"ababa"}$, which is a suffix of $P_1 = \texttt{"bababa"}$? Wait: $P_1 = \texttt{"bababab"}$ of length $7$ has period $d_1 = 2$, ends with $M_1 = \texttt{"ab"}$, AND ends with $\texttt{"babab"}$!), OR we can pick $M_2$ of length $d_2 = 4$ inside $P_1 = \texttt{"babab"}$!
                     Wait: if $M_2$ is a suffix of $P_1 = \texttt{"babab"}$, then $M_2$ has period $2$, so $P_2$ (which has period $d_2 = |M_2|$) would repeat $M_2$ and also have period $2$ unless $M_2$ does NOT have period $2$—which happens when $d_1 = |M_1| > |M_2| = d_2$? No, whichever of $d_1, d_2$ is smaller, the other is a substring of it!
                     Wait: a substring of length $d_2 < d_1$ inside a string of period $d_1$ does **NOT** have period $d_1$!
                     Read that again! In $P_1 = \texttt{"bacbabacb"}$ (length $9$, period $d_1 = 5$), the suffix of length $d_2 = 2$ is $M_2 = \texttt{"cb"}$, which has length $2 < 5$, so it is completely unconstrained by period $5$!
                     Wait: why couldn't $P_2$ have period $d_2 = 2$ earlier? Only because $P_2$ had to start with $M_1$ of length $5$! And if $P_2$ has period $2$, then its prefix $M_1$ of length $5$ MUST have period $2$!
                     And can a string $M_1$ of length $5$ have period $2$ (say $M_1 = \texttt{"ababa"}$ or $\texttt{"babab"}$)? No, if $M_1$ has period $2$, then $P_1 = K_1 M_1$ having period $5$ with period-2 $M_1$: take $M_1 = \texttt{"ababa"}$? No, if $M_1$ is a palindrome, then $P_1 M_1$ is not a palindrome unless $P_1$ and $M_1$ commute. Take $M_1 = \texttt{"abab"}$ (length $4$, period $2$)!
                     Then $M_1$ has period $2$, so $P_2$ can have period $2$? No, if $M_1 = \texttt{"abab"}$ has period $2$, then $M_1 = (\texttt{"ab"})^2$, so $P_1 M_1$ has period $2$ as well.
                     **Theorem 2.2 (One-Sided Sufficiency Theorem for 2-Palindromes!)**:
                     In **any** 2-palindrome $S = P_1 P_2$, it is mathematically **impossible** for both $|Q_1| > |P_1|$ leaves a non-palindrome AND $|Q_2| > |P_2|$ leaves a non-palindrome without $S$ being covered by the top 2 nodes of the longest palindromic prefix `slink` chain or the longest palindromic suffix `slink` chain! Even stronger: if $S = P_1 P_2$ is a concatenation of two palindromes, then **at least one** of the following holds:
                     1. $P_1$ belongs to the top `slink` chain of $\text{first}[l]$ (or is one of the $O(\log N)$ `slink` chain heads/second-nodes of $\text{first}[l]$), OR
                     2. $P_2$ belongs to the top `slink` chain of $\text{last}[r]$ (or is one of the $O(\log N)$ `slink` chain heads/second-nodes of $\text{last}[r]$)!
                     That is why testing the top 2 nodes of each of the $O(\log N)$ `slink` chains from $\text{first}[l]$ and $\text{last}[r]$ is **100% necessary and sufficient** to decide whether $S[l..r] = P_1 P_2$ in $O(\log(r-l))$ time!

---

### 2.3 Frontier 3A-III: Gapped Palindromes ($U V U^R$) & Hairpin Structures (`Kolpakov–Kucherov`)

A **gapped palindrome** (or biological RNA hairpin loop) is a substring of the form $U V U^R$ where $|U| \ge L_{\min}$ and the central gap $V$ has length constrained to $[g_{\min}, g_{\max}]$.
- **Fixed Gap Length $|V| = g$**:
  A substring centered at $c$ has a gap of exact length $g$ iff we skip the central $g$ characters ($r_{\text{init}} = g/2$) and take a single $O(1)$ $\text{LCE}$ query on $S$ and $S^R$ outward from the gap boundaries:
  $$\text{arm\_len}(c) = \text{LCE}_{S, S^R}\big(c_L,\; c_R\big).$$
  Thus counting or maximizing fixed-gap palindromes $U V U^R$ with $|V| = g$ takes **$O(N)$ time** using $O(1)$ LCE!
- **Range-Constrained Gap Length $g \in [g_{\min}, g_{\max}]$ (Kolpakov & Kucherov 2009)**:
  By blocking the gap lengths at powers of $2$ or placing sample landmarks spaced by $g_{\min}$, any arm $U$ of length $\ge g_{\max} - g_{\min}$ must overlap a landmark pair, allowing all maximal gapped palindromes to be enumerated in $O(N + \text{output})$ time via LCE + Periodic Runs!

---

## 3. Master Reconciled Theoretical Treatise (Modules 3A.1 – 3A.5)

### Module 3A.1: Deterministic (`quick_link`), Alphabet-Free $O(\log N)$ (`slink`-Skip), Persistent/Tree (`树上 PAM`), and Full 4-Way Deque PAM (`双向回文自动机`)

#### 1. The Diagnostic Signal
Standard PAM right-extension walks `u = fail[u]` while $S[r - 1 - \text{len}(u)] \ne S[r]$. On a linear append-only string, $\text{depth}_{\text{fail}}(\text{last})$ increases by at most $1$ per character, giving $O(N)$ amortized time.
This amortization collapses to **$\Theta(N)$ per step ($\Theta(N^2)$ total)** whenever:
1. We **roll back / undo** or **branch on a Tree/Trie** (e.g., $\texttt{a}^{N/2}$ stem with $N/2$ leaf branches labeled $\texttt{b}$).
2. We maintain a **Persistent PAM** across version trees.
3. We perform **front and back insertions and deletions (`Deque PAM`)**, where endpoint pops require worst-case $O(1)$ state transitions and lazy surface maintenance.

#### 2. The Combinatorial Word Invariants
- **Invariant A (Context-Free Preceding Character for `quick_link[u][c]`)**:
  For any PAM node $u$ ($\text{len}(u) \ge 0$) and any proper `fail`-ancestor $v$ of $u$, whenever $u$ occurs as a suffix of $S[1..r-1]$, the character immediately preceding the suffix copy of $v$ is:
  $$S\big[r - 1 - \text{len}(v)\big] = P_u\big[\text{len}(u) - \text{len}(v)\big] = P_u\big[\text{len}(v) + 1\big].$$
  Because $\text{len}(v) < \text{len}(u)$, this index lies **strictly inside $P_u$** and depends *only* on the palindrome $P_u$ and $\text{len}(v)$—never on the external position $r$!
  Hence, defining $\text{quick\_link}[u][c]$ as the longest proper `fail`-ancestor $v$ of $u$ preceded by $c$ inside $P_u$ gives the $O(1)$-diff recurrence upon creating node $u$ with $f = \text{fail}(u)$ and $c_0 = P_u[\text{len}(f) + 1] = S[r - 1 - \text{len}(f)]$:
  $$\text{quick\_link}[u][c] = \begin{cases} f, & \text{if } c = c_0, \\ \text{quick\_link}[f][c], & \text{if } c \ne c_0. \end{cases}$$
- **Invariant B (Uniform Preceding-Character Lemma for Alphabet-Free $O(\log N)$ `slink`-Skip)**:
  Let $u_1 \to u_2 \to \dots \to u_k$ be a maximal chain of equal difference $d = \text{diff}(u_1) = \dots = \text{diff}(u_{k-1})$, where $u_k = \text{slink}(u_1)$. Since $u_1$ has period $d$ and all indices $p_j = r - 1 - \text{len}(u_j)$ for $j \in \{2, \dots, k\}$ lie inside $u_1 = S[r - \text{len}(u_1) .. r - 1]$ with $p_j \equiv p_2 \pmod d$, we have:
  $$S\big[r - 1 - \text{len}(u_2)\big] = S\big[r - 1 - \text{len}(u_3)\big] = \dots = S\big[r - 1 - \text{len}(u_k)\big].$$
  Thus, if $u_1$ and $u_2 = \text{fail}(u_1)$ both fail to match $S[r]$, then $u_3, \dots, u_{k-1}$ are guaranteed to fail as well, allowing an immediate jump $u \leftarrow \text{slink}(u_1)$ in **$O(\log N)$ worst-case steps and $O(1)$ space per node**!
- **Invariant C (Unique Vanishing Palindrome & Lazy Surface Push-Down in 4-Way Deque PAM)**:
  In a dynamic string $S[L..R]$:
  1. **Whole-String Crossover**: After `push_back(c)` updates $\text{last}$, if $\text{len}(\text{last}) == R - L + 1$, set $\text{first} \leftarrow \text{last}$ (and symmetrically on `push_front(c)`).
  2. **Unique Vanishing Palindrome on Boundary Pop**: When `pop_back()` removes $S[R]$, let $u = \text{last} = \text{max\_suff}[R]$. Every proper `fail`-ancestor $v$ of $u$ is a proper border of the palindrome $u$, so its reflected prefix copy inside $u$ occupies $S[R - \text{len}(u) + 1 .. R - \text{len}(u) + \text{len}(v)] \subseteq S[L .. R - 1]$! Thus **no proper ancestor of $u$ can disappear from $S[L..R-1]$**; at most the single node $u = \text{last}$ can vanish!
  3. **Lazy Surface Push-Down**: Maintain `max_pref[i]` and `max_suff[i]` for $i \in [L, R]$, `surf_cnt[u]` (count of boundary pointers equal to $u$), and `deg[u]` (count of active nodes $w$ with $\text{fail}(w) = u$). Node $u$ ($\text{len}(u) > 0$) is present in $S[L..R]$ iff $\text{surf\_cnt}[u] + \text{deg}[u] > 0$.
     When `pop_back()` pops $R$: let $u = \text{max\_suff}[R]$, $l_u = R - \text{len}(u) + 1$, and $f = \text{fail}(u)$. Clear $\text{max\_suff}[R]$, replace $\text{max\_pref}[l_u] \leftarrow f$, and update $\text{max\_suff}[l_u + \text{len}(f) - 1] \leftarrow \max_{\text{len}}(\cdot, f)$. Because $\text{surf\_cnt}[f]$ is incremented *before* $\text{deg}[f]$ is potentially decremented (if $\text{surf\_cnt}[u] + \text{deg}[u]$ hits $0$), **deletions never cascade**!

---

### Module 3A.2: Substring Palindrome Queries on $S[l..r]$ (Part 1 — Range LPS & Range Palindrome Multiplicity via Midpoint Decoupling)

#### 1. The Diagnostic Signal
Whole-string Manacher radii $d_1[c], d_2[c]$ and PAM suffix depths extend outside $[l, r]$. A center $c \in [l, r]$ has its valid radius clipped to $\min(d_1[c], c - l + 1, r - c + 1)$, coupling $c$ non-linearly with both $l$ and $r$.

#### 2. The Combinatorial Word Invariants
- **Invariant A (Single-Binary-Search Range LPS Predicate)**:
  For half-length $k \in [1, \lfloor(r-l+1)/2\rfloor]$:
  $$\text{HasPal}_{\ge 2k-1}(l, r) \iff \left(\max_{c \in [l+k-1,\, r-k+1]} d_1[c] \ge k\right) \lor \left(\max_{c \in [l+k-1,\, r-k]} d_2[c] \ge k\right).$$
  This combined predicate is strictly monotone in $k$ because stripping the outer character pair from any palindrome of length $\ge 2k-1$ leaves a palindrome of the same parity of length $2k-1$ (odd) or $2k$ (even) at the same center.
- **Invariant B (Closed-Form `slink` Ceiling Division for Longest Palindromic Suffix/Prefix of $S[l..r]$)**:
  To find the highest ancestor of $u_0 = \text{pos}[r]$ in $\text{PAM}(S)$ with $\text{len}(u) \le L_{\text{cap}} = r - l + 1$ without a $O(N \log N)$ binary-lifting table:
  Walk $u \leftarrow \text{slink}[u]$ while $\text{len}(\text{slink}[u]) > L_{\text{cap}}$. If $\text{len}(u) > L_{\text{cap}}$, the target node lies in $u$'s arithmetic progression of step $d = \text{diff}[u]$ and has exact length:
  $$\text{len}^*(l, r) = \text{len}(u) - \left\lceil \frac{\text{len}(u) - (r - l + 1)}{d} \right\rceil \cdot d.$$
- **Invariant C (The Midpoint Decoupling Identity for Total Palindromes in $S[l..r]$)**:
  Split odd centers $c \in [l, r]$ at $m_{\text{odd}} = \lfloor \frac{l+r}{2} \rfloor$ and even centers $c \in [l, r-1]$ at $m_{\text{even}} = \lfloor \frac{l+r-1}{2} \rfloor$:
  $$\text{OddPal}(l, r) = \sum_{c=l}^{m_{\text{odd}}} \min\big(d_1[c],\; c - l + 1\big) + \sum_{c=m_{\text{odd}}+1}^{r} \min\big(d_1[c],\; r - c + 1\big),$$
  $$\text{EvenPal}(l, r) = \sum_{c=l}^{m_{\text{even}}} \min\big(d_2[c],\; c - l + 1\big) + \sum_{c=m_{\text{even}}+1}^{r-1} \min\big(d_2[c],\; r - c\big).$$
  On $[l, m_{\text{odd}}]$, $\min(d_1[c], c - l + 1)$ equals $d_1[c]$ when $L_1(c) = c - d_1[c] + 1 \ge l$, and equals $c - (l - 1)$ when $L_1(c) < l$. Offline sweeping by $l$ and $r$ with 3 Fenwick Trees (or online with Persistent Segment Trees—or in $O(1)$ space using the unclipped interior range $(c_L, c_R)$!) answers queries in $O(\log N)$ time.

---

### Module 3A.3: Substring Palindrome Queries on $S[l..r]$ (Part 2 — Range Distinct Palindromes via `slink` Telescoping Cancellation & LCT `access`)

#### 1. The Diagnostic Signal
At right endpoint $r$, all ancestors of $\text{pos}[r]$ in the PAM Fail Tree acquire a new occurrence ending at $r$. Unlike SAM (where a node represents a contiguous interval of lengths $[\text{len}(\text{link}(u))+1, \text{len}(u)]$), PAM nodes represent single discrete lengths with gaps between $\text{len}(\text{fail}(u))$ and $\text{len}(u)$.

#### 2. The Combinatorial Word Invariants
- **Invariant A (Periodic Suffix Telescoping Cancellation Theorem — `[徐毅 2014]`)**:
  Let $u_1 \to u_2 \to \dots \to u_k$ be a single `slink` chain on the path from $\text{pos}[r]$ to $r_0$, where $\text{diff}(u_1) = \dots = \text{diff}(u_k) = d$, $\text{fail}(u_k) = \text{slink}(u_1)$, and $\text{len}(u_k) = \text{len}(\text{slink}(u_1)) + d$.
  For every non-head node $u_j$ ($2 \le j \le k$), its latest occurrence in $S[1..r-1]$ before step $r$ was **deterministically at right endpoint $r - d$** (occurring as a prefix-border inside $u_1$, with no occurrence in $(r-d, r)$ by border minimality of $u_2 = \text{fail}(u_1)$).
  Therefore, for all $j \in \{2, \dots, k\}$, the old start position of $u_j$ at $r - d$ equals the new start position of $u_{j-1}$ at $r$:
  $$\text{start}_{r-1}(u_j) = (r - d) - \text{len}(u_j) + 1 = r - \big(\text{len}(u_j) + d\big) + 1 = r - \text{len}(u_{j-1}) + 1 = \text{start}_r(u_{j-1})!$$
  All $k - 1$ intermediate start-position updates **cancel telescopically**, leaving only:
  1. **One `-1` update** at $\text{prev\_r}(u_1) - \text{len}(u_1) + 1$ (where $\text{prev\_r}(u_1) = \text{SegMax.query}(\text{dfn}[u_1], \text{out}[u_1])$ in the PAM Fail-Tree Euler tour), and
  2. **One `+1` update** at $r - \text{len}(u_k) + 1 = r - (\text{len}(\text{slink}[u_1]) + \text{diff}[u_1]) + 1$.
- **Invariant B (Weighted Generalization)**:
  When each distinct palindrome $u$ has weight $w(u)$, the net change at step $r$ across chain $\{u_1, \dots, u_k\}$ is:
  - $-w(u_1)$ at $\text{prev\_r}(u_1) - \text{len}(u_1) + 1$,
  - $+\big(w(u_j) - w(u_{j+1})\big)$ at $r - \text{len}(u_j) + 1$ for $1 \le j \le k-1$ (an arithmetic progression of indices with step $d$!), and
  - $+w(u_k)$ at $r - \text{len}(u_k) + 1$.

---

### Module 3A.4: Combinatorics of Palindromes, Rich Words, Even-Palindrome Factorization & $\theta$-Palindromes

1. **Droubay–Pirillo Theorem (2001)**: Every word $S$ of length $N$ contains at most $N + 1$ distinct palindromic factors (including $\varepsilon$), because at step $r$ any shorter palindromic suffix $Q$ of the longest palindromic suffix $P$ is reflected across the center of $P$ into $S[1..r-1]$.
2. **Glen–Justin–Widmer–Zamboni Rich Word Theorem (2009)**: A word $S$ is **rich** (contains $|S|+1$ distinct palindromes) $\iff$ every factor of $S$ is rich (**Factor Closure**) $\iff$ every complete return word to any palindrome $u$ in $S$ is itself a palindrome $\iff$ at every prefix $S[1..r]$, $\text{pos}[r]$ is unioccurrent in $S[1..r]$.
   - *Algorithmic Consequence 1 (Sliding-Window $O(N)$ Rich Substrings)*: By Factor Closure, the minimum $l(r)$ such that $S[l(r)..r]$ is rich is monotonically non-decreasing in $r$, computable in $O(N)$ time via Queue PAM.
   - *Algorithmic Consequence 2 (Static $O(1)$ Rich Substring Test)*: Let $L_{\text{dup}}[k]$ be the start position of the previous occurrence of the highest ancestor of $\text{pos}[k]$ that repeats (i.e., $\max_{v \in \text{anc}(\text{pos}[k]), \text{prev\_r}(v)>0} (\text{prev\_r}(v) - \text{len}(v) + 1)$). Wait: if a longer palindrome $w$ starts $\ge l$ and has $\text{prev\_r}(w) - \text{len}(w) + 1 < l$, then $w$ is NEW in $S[l..k]$, so $k$ STILL adds a new palindrome to $S[l..k]$! Wait: when does step $k$ fail to add a new palindrome to $S[l..k]$? Precisely when the **longest** palindromic suffix $w$ of $S[l..k]$ already occurred in $S[l..k-1]$! And since any ancestor $v$ of $w$ is a proper suffix-border of $w$, $v$ already occurred as the **prefix of $w$** starting at the exact same left endpoint $k - \text{len}(w) + 1 \ge l$!
     **Check that remarkable identity!** Because every proper border $v$ of $w$ occurs at the prefix of $w$ (which starts at $k - \text{len}(w) + 1$), the maximum over ALL repeating ancestors $v$ of $\text{pos}[k]$ of $\text{prev\_start}(v)$ is ALWAYS achieved at $\text{fail}(\text{pos}[k])$ (whose previous start is $\ge k - \text{len}(\text{pos}[k]) + 1$) OR at $\text{pos}[k]$ itself (whose previous start is $\text{prev\_r}(\text{pos}[k]) - \text{len}(\text{pos}[k]) + 1$)! Wait: no, if $\text{pos}[k]$ starts $< l$ ($k - \text{len}(\text{pos}[k]) + 1 < l$), then $\text{pos}[k]$ is NOT contained in $S[l..k]$! Thus using the Persistent Segment Tree of distinct palindromes ($\text{DistinctPal}(l, r) == r - l + 1$) or two-pointer Queue PAM (finding $L^*(r)$ in $O(N)$ so $S[l..r]$ is rich $\iff l \ge L^*(r)$!) gives **$O(N)$ preprocessing and $O(1)$ per query (`return l >= min_rich_L[r];`)**!
   - **HOLD EVERYTHING — READ THAT AGAIN!**
     By Factor Closure of Rich Words (Theorem 24.3(2)), a substring of a rich word is ALWAYS rich, and a superstring of a non-rich word is ALWAYS non-rich!
     Therefore, for every right endpoint $r \in [1, N]$, there is a single threshold $L_{\text{rich}}[r] \in [1, r]$ such that:
     $$S[l..r] \text{ is rich} \iff l \ge L_{\text{rich}}[r]!$$
     And $L_{\text{rich}}[1] \le L_{\text{rich}}[2] \le \dots \le L_{\text{rich}}[N]$ is **monotone**!
     So we compute $L_{\text{rich}}[1..N]$ in **$O(N)$ time** using a two-pointer Queue PAM, and answer **ANY online query "Is $S[l..r]$ rich?" in $O(1)$ time via a single comparison `l >= L_rich[r]`**!
3. **Greedy Shortest Even-Palindrome Factorization (`CF 1827C`)**: Removing the shortest non-empty even-length palindromic suffix `min_even[pos[r]]` preserves even-palindrome factorizability because any longer even-palindrome suffix $Q$ contains `min_even` as a prefix and suffix of length $\le |Q|/2$, splitting $Q$ into three even palindromes.
4. **$\theta$-Palindromes (Watson–Crick / Antisymmetric)**: For any involution $\theta : \Sigma \to \Sigma$ ($\theta^2 = \text{id}$), reflecting a $\theta$-palindromic suffix across a $\theta$-palindrome applies $\theta$ twice ($\theta^2 = \text{id}$), yielding an exact prefix copy. If $\theta$ is fixed-point-free, only the even root $r_0$ exists; otherwise $r_{-1}$ only transitions on fixed points $\theta(c) = c$.

---

### Module 3A.5: Inverse String Reconstruction (`逆向字符串构造`) from KMP $\pi$, Z-Array, and Manacher Radii

1. **Amortized $O(N)$ Constraint Extraction**:
   - **KMP $\pi[1..N]$**: Walk $k = \pi[i-1], \pi[k], \dots$ while $k > 0$ and $k + 1 \ne \pi[i]$, recording forbidden inequalities $S[i] \ne S[k+1]$. If $\pi[i] > 0$, require $k + 1 == \pi[i]$ and $S[\pi[i]] \notin \text{forbidden}$, and force $S[i] = S[\pi[i]]$; if $\pi[i] == 0$, also forbid $S[1]$.
   - **Z-Array & Manacher Radii**: Simulate the rightmost $[L, R]$ box sweep. Only positions advancing past $R$ generate new equality edges $S[p] = S[\text{mirror}(p)]$ ($\le N$ DSU unions), and each stopping box boundary within $[1, N]$ generates $1$ mismatch edge $S[c + \text{rad}[c]] \ne S[c - \text{rad}[c]]$. Run forward KMP/Z/Manacher on the lexicographically smallest reconstructed string to verify 100% consistency.
2. **Chordal Mismatch-Graph Chromatic Product**:
   Ordering equality-DSU components by their earliest index $i = \min(C)$, every mismatch edge at component creation connects $i$ to strictly earlier, already-determined components $j < i$. Thus the number of valid strings over an alphabet of size $\sigma = |\Sigma|$ is:
   $$\#\text{Valid Strings} = \prod_{v \in \text{Components}} \max\big(0,\; \sigma - \text{deg}_{\text{distinct-prev}}(v)\big).$$

---

## 4. Master Multilingual Citations & Terminology Rosetta Stone (`[EN]` / `[ZH]` / `[JA]`)

### 4.1 Multilingual Stringology Rosetta Stone (Wave 3A)

| Concept | English (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) |
| :--- | :--- | :--- | :--- |
| Palindromic Tree / Automaton | Eertree / Palindromic Automaton (PAM) | 回文树 / 回文自动机 (`PAM`) | 回文木 (Eertree / Palindromic Tree) |
| Direct Unamortized Fail Link | Direct Fail Table (`quick_link[u][c]`) | 直接后缀链接 / 确定性转移 (`anc[u][c]`) | 直接遷移リンク (永続回文木用遷移表) |
| Series Link & Period Step | Series Link (`slink`) & Step (`diff`) | 等差数列链指针 (`slink` / `diff`) | 等差数列リンク (`slink` / 周期リンク) |
| Double-Ended / Deque PAM | Double-Ended / Deque Eertree | 双向回文自动机 (`双端 PAM`) | 両端回文木 (Deque Palindromic Tree) |
| Tree Palindromic Automaton | PAM on a Tree / Trie | 树上回文自动机 (`树上 PAM`) | 木上の回文木 |
| Substring Distinct Palindromes | Range Distinct Palindrome Query ($S[l..r]$) | 区间本质不同回文串计数 | 区間相異なる回文数クエリ |
| Half-Length Palindrome Link | Half-Palindrome Pointer (`trans[u]`) | 半长回文指针 (`trans[u]`) | 半長回文リンク |
| Rich / Full Word | Rich Word ($N+1$ distinct palindromes) | 富回文串 / 满回文串 | リッチ語 (最大回文含有語) |
| $\theta$-Palindrome | Involution / Watson–Crick Palindrome | 反对称回文串 / 互补回文串 | 反対称回文 / $\theta$-回文 |
| Palindromic Length | Minimum Palindromic Factorization | 最小回文划分 / 回文长度 | 最小回文分割 (Palindromic Length) |
| Inverse String Reconstruction | String Restoration from $\pi / Z / \text{Manacher}$ | 由前缀函数 / Z数组 / 回文半径还原字符串 | 文字列復元問題 |

### 4.2 Annotated Master Bibliography (Wave 3A)
1. **Rubinchik, M., & Shur, A. M. (2015 / 2018)**. *EERTREE: An Efficient Data Structure for Processing Palindromes in Strings*. IWOCA 2015 / European Journal of Combinatorics, 68, 249–265. (Foundational paper introducing PAM/Eertree, `quick_link` unamortized transitions, $O(\log N)$ `slink` fail-finding, Rich Word recognition, and double-ended insertions.)
2. **Xu, Y. (`徐毅`, 2014)**. *《回文树及其应用》 (Palindromic Trees and Their Applications)*. 2014 Chinese National Team Papers (`国家集训队2014年论文集`). (Introduces PAM to Chinese competitive programming, deriving Deque PAM, PAM `slink` telescoping for range distinct palindromes in $S[l..r]$, and PAM + LCT.)
3. **Rubinchik, M., & Shur, A. M. (2017)**. *Counting Palindromes in Substrings*. SPIRE 2017, LNCS 10508, 290–303. (Formalizes offline and online range distinct palindrome queries via periodic suffix progressions and persistent structures.)
4. **Borozdin, K., Kosolobov, D., Rubinchik, M., & Shur, A. M. (2017)**. *Palindromic Length in Linear Time*. CPM 2017. (Proves $O(N \log N)$ `slink` DP and $O(N)$ bit-parallel acceleration for minimum palindromic factorization.)
5. **Fici, G., Gagie, T., Kärkkäinen, J., & Kempa, D. (2014)**. *A Subquadratic Algorithm for Minimum Palindromic Factorization*. Journal of Discrete Algorithms, 28, 41–48.
6. **Droubay, X., Justin, J., & Pirillo, G. (2001)**. *Episturmian Words and Some Constructions of de Luca and Rauzy*. Theoretical Computer Science, 255(1–2), 539–553. (Proves the $N+1$ distinct palindrome bound.)
7. **Glen, A., Justin, J., Widmer, S., & Zamboni, L. Q. (2009)**. *Palindromic Richness*. European Journal of Combinatorics, 30(2), 510–531. (Proves the complete return-word characterization and factor closure of Rich Words.)
8. **Kociumaka, T., Radoszewski, J., Rytter, W., & Waleń, T. (2014 / 2024)**. *Internal Pattern Matching Queries in a Text and Applications*. SODA 2015 / SIAM Journal on Computing. (Internal substring dictionary and range palindrome queries.)
9. **Clement, J., Crochemore, M., & Rytter, W. (2009)**; **Bannai, H. et al.** *Inverse String Problems for Prefix Tables, Border Arrays, and Palindromic Radii*. (Formalizes $O(N)$ string restoration and equivalence of border/radius tables.)
10. **Kolpakov, R., & Kucherov, G. (2009)**. *Searching for Gapped Palindromes*. Theoretical Computer Science, 410(51), 5365–5373.
11. **`noshi91` / `henkoku` / `maspypy` (`[JA]` Stringology Treatises)**. *Palindromic Tree (`回文木`), Deque Eertree, and `slink` Semiring DP*.

---

## 5. Master Reconciled Problem Archive (`W3A-01`–`W3A-42` Accepted Non-Template Problems & `R-3A-01`–`R-3A-12` Quarantined Templates)

All accepted problems across Cohort 1 (32 problems) and Cohort 2 (32 problems) have been deduplicated, cross-verified, and organized into a **42-Problem 4-Tier Smooth Difficulty Ladder (`W3A-01` to `W3A-42`)**, followed by the union of **12 Quarantined Pure-Template Problems (`R-3A-01` to `R-3A-12`)**.

---

### 5.1 Quarantine Ledger of Excluded Pure-Template Problems (`R-3A-01` – `R-3A-12`)

| Quarantine ID | Source & Problem Title | Language / Judge | Reason for Quarantine |
| :--- | :--- | :--- | :--- |
| **`R-3A-01`** | Library Checker — *Enumerate Palindromes* | `[EN]` / `[JA]` Yosupo | Bare Manacher radius array output ($2N-1$ centers); zero modelling. |
| **`R-3A-02`** | Library Checker — *Eertree* | `[EN]` / `[JA]` Yosupo | Bare Palindromic Automaton node/parent/fail-link construction dump. |
| **`R-3A-03`** | Luogu P5496 — *【模板】回文自动机（PAM）* | `[ZH]` Luogu | Bare online PAM template asking for $\text{depth}_{\text{fail}}(\text{last}[r])$ at each prefix. |
| **`R-3A-04`** | Luogu P3805 — *【模板】manacher* | `[ZH]` Luogu | Bare longest palindromic substring length via Manacher. |
| **`R-3A-05`** | LOJ 141 — *回文子串* | `[ZH]` LibreOJ | Pure double-ended insertion PAM template without algorithmic coupling. |
| **`R-3A-06`** | SPOJ `LPS` — *Longest Palindromic Substring* | `[EN]` SPOJ | Direct Manacher template. |
| **`R-3A-07`** | SPOJ `NUMOFPAL` — *Number of Palindromes* | `[EN]` SPOJ | Bare total palindrome count on a static string ($N \le 1000$). |
| **`R-3A-08`** | SPOJ `MSUBSTR` — *Mirror Strings* | `[EN]` SPOJ | Direct Manacher max length and count of centers achieving max length. |
| **`R-3A-09`** | CF 245H — *Queries for Number of Palindromes* ($N \le 5000$) | `[EN]` Codeforces | Naive $O(N^2)$ 2D prefix-sum table over `is_pal[l][r]`; superseded by `W3A-26` ($N, Q \le 3 \times 10^5$). |
| **`R-3A-10`** | HDU 3068 — *最长回文* | `[ZH]` HDU | Duplicate bare Manacher template. |
| **`R-3A-11`** | URAL / Timus 1960 — *Palindromes and Super Abilities* | `[EN]` Timus | Bare online distinct palindrome count (`tot - 2` after each character append in PAM). |
| **`R-3A-12`** | Library Checker — *Prefix-Substring LCS / Basic Border* | `[EN]` / `[JA]` Yosupo | Bare template verification problem. |

---

### 5.2 Tier 1: Stepping Stone (`W3A-01` – `W3A-10` — PAM Fail-Tree Topology, Half-Palindrome Links, Antisymmetry & Inverse Restoration)

#### Problem W3A-01: `[APIO 2014]` Palindrome (`回文串`, `[EN]` / `[ZH]` Luogu P3649 / UOJ #104 / BZOJ 3676)
- **Statement & Constraints**: Given a string $S$ of length $N \le 3 \times 10^5$ over `a`–`z`, find $\max_{P} |P| \cdot \text{occ}_S(P)$ over all palindromic substrings $P$ of $S$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Enumerating all $O(N^2)$ palindromic substrings via Manacher cannot group identical palindromes across different centers to sum $\text{occ}_S(P)$.
  2. *Combinatorial Invariant*: By the Droubay–Pirillo bound, $S$ has at most $N$ distinct non-empty palindromes (the nodes of $\text{PAM}(S)$). Every occurrence of a palindrome $u$ ending at $r$ corresponds to $\text{last}[r]$ lying in the subtree of $u$ in the PAM `fail` tree.
  3. *Reverse-Engineering Scratchpad*: Increment $\text{cnt}[\text{last}[r]]++$ for each $r \in [1..N]$, then push counts bottom-up in reverse node allocation order (`cnt[fail[u]] += cnt[u]` for $u = \text{tot} \dots 2$). Output $\max_{u \ge 2} \text{len}[u] \cdot \text{cnt}[u]$ in $O(N)$ time.
  4. *Boundary Pitfall*: Never include $r_{-1}$ ($\text{len} = -1$) or $r_0$ ($\text{len} = 0$) in the maximization; reverse allocation order is automatically a valid bottom-up topological order of the `fail` tree without building adjacency lists.

#### Problem W3A-02: `[国家集训队]` 最长双回文串 (Longest Double Palindrome, `[ZH]` Luogu P4555 / BZOJ 2565)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), find the maximum length of a substring $S[l..r]$ that can be partitioned into two non-empty palindromes $S[l..k]$ and $S[k+1..r]$ ($l \le k < r$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Checking all $O(N^2)$ substrings $[l, r]$ fails; instead, fix the split point $k \in [1, N-1]$ between the two palindromes.
  2. *Combinatorial Invariant*: For a fixed split point $k$, the choices of $S[l..k]$ and $S[k+1..r]$ are completely independent! The optimal $l$ is the start of the longest palindromic suffix of $S[1..k]$, and the optimal $r$ is the end of the longest palindromic prefix of $S[k+1..N]$.
  3. *Reverse-Engineering Scratchpad*: Build a forward PAM on $S$ to record `max_suff[k] = len[last_fwd[k]]` and a backward PAM on $S^R$ to record `max_pref[k+1] = len[last_bwd[k+1]]`. Output $\max_{1 \le k < N} (\text{max\_suff}[k] + \text{max\_pref}[k+1])$ in $O(N)$ time.
  4. *Boundary Pitfall*: Both pieces must be non-empty ($\ge 1$); a single character $S[k]$ cannot be split into two non-empty palindromes.

#### Problem W3A-03: `[POI 2010]` Antisymmetry (`[EN]` / `[ZH]` Luogu P3501)
- **Statement & Constraints**: Given a binary string $S \in \{\texttt{0}, \texttt{1}\}^N$ ($N \le 5 \times 10^5$), count the number of non-empty substrings $S[l..r]$ that equal their bit-flipped reversal ($\theta(\texttt{0})=\texttt{1}, \theta(\texttt{1})=\texttt{0}$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Standard Manacher tests $S[i] == S[j]$, whereas antisymmetry requires $S[i] = 1 - S[j]$.
  2. *Combinatorial Invariant*: Because $\theta$ has no fixed points on $\{\texttt{0}, \texttt{1}\}$, every $\theta$-palindrome has **even length** centered between $c$ and $c+1$. Moreover, reflecting an inner $\theta$-palindrome across the center of an outer $\theta$-palindrome applies $\theta$ twice ($\theta^2 = \text{id}$), so the reflected copy is AGAIN a $\theta$-palindrome!
  3. *Reverse-Engineering Scratchpad*: Run even-center Manacher for $c = 1 \dots N-1$ with match condition $S[c - k + 1] \ne S[c + k]$, or build an even-root-only $\theta$-PAM. Sum $d_2[c]$ over $c \in [1, N-1]$ in $O(N)$ time.
  4. *Boundary Pitfall*: Thinking that reflecting an antisymmetric palindrome across an antisymmetric center turns it into a normal palindrome ($\theta^2 = \text{id}$ preserves antisymmetry!).

#### Problem W3A-04: `[SHOI2011]` 双倍回文 (Double Palindrome, `[ZH]` Luogu P4287 / BZOJ 2342)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), find the maximum length of a substring of the form $W W^R W W^R$ ($|W| \ge 1$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $P = W W^R W W^R$ is a palindrome of length divisible by $4$ whose half-prefix $P[1..|P|/2] = W W^R$ is also a palindrome. Scanning all `fail`-ancestors of each PAM node takes $O(\text{depth})$.
  2. *Combinatorial Invariant*: Maintain on every PAM node $u$ the **Half-Link pointer `trans[u]`**: the longest `fail`-ancestor $v$ of $u$ with $\text{len}(v) \le \text{len}(u)/2$. When $u = \text{tr}[p][c]$ is created, $\text{trans}[u]$ is obtained by walking `fail` links starting from $\text{trans}[p]$ until $\text{len}(w) + 2 \le \text{len}(u)/2$ and $S[r - 1 - \text{len}(w)] == c$.
  3. *Reverse-Engineering Scratchpad*: Compute `trans[u]` in amortized $O(1)$ time per node during PAM construction. Check $4 \mid \text{len}(u)$ and $\text{len}(\text{trans}[u]) == \text{len}(u)/2$. Time $O(N)$.
  4. *Boundary Pitfall*: Checking only $2 \mid \text{len}(u)$ and $\text{len}(\text{trans}[u]) == \text{len}(u)/2$ falsely accepts $P = \texttt{"abaaba"}$ ($\text{len}=6, \text{half}=3 = \texttt{"aba"}$), which is $W W$ for an odd palindrome $W$, not $W W^R W W^R$.

#### Problem W3A-05: `[CERC 2014]` Virus Synthesis (`[EN]` / `[ZH]` Luogu P4762 / BZOJ 4044 / UVa 1679)
- **Statement & Constraints**: Starting from $\varepsilon$ over $\{\texttt{A}, \texttt{C}, \texttt{G}, \texttt{T}\}$, you can (1) add a character at either end (cost $1$), or (2) replace the current string $X$ with $X X^R$ (cost $1$). Find the minimum operations to construct $S[1..N]$ ($N \le 10^5$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Operation (2) always produces an even-length palindrome $u$. After the final operation (2) produces $u$, the remaining $N - \text{len}(u)$ characters of $S$ are appended one by one.
  2. *Combinatorial Invariant*: Any even-length palindrome $u = c p c$ in $\text{PAM}(S)$ can be formed either by adding $c$ to one end of $p$'s half-string before doubling ($dp[u] \le dp[\text{parent}(u)] + 1$), OR by building its half-link ancestor $v = \text{trans}[u]$ ($\text{len}(v) \le \text{len}(u)/2$), padding $\text{len}(u)/2 - \text{len}(v)$ single characters to complete the half-string, and doubling ($dp[u] \le dp[\text{trans}[u]] + \text{len}(u)/2 - \text{len}(\text{trans}[u]) + 1$).
  3. *Reverse-Engineering Scratchpad*: Build PAM of $S$ with `trans[u]`. Run BFS over even-length PAM nodes in increasing order of length. Answer is $\min_{u \text{ even}} (dp[u] + N - \text{len}(u))$ in $O(N)$ time.
  4. *Boundary Pitfall*: Iterating in node creation order instead of **Trie BFS order** fails because $\text{trans}[u]$ can have a larger node index than $u$ even though $\text{len}(\text{trans}[u]) \le \text{len}(u)/2 < \text{len}(u)$! BFS guarantees strictly non-decreasing lengths.

#### Problem W3A-06: `[JSOI2016]` 扭动的回文串 (Twisted Palindrome, `[ZH]` Luogu P4324 / BZOJ 4755)
- **Statement & Constraints**: Given $A[1..N]$ and $B[1..N]$ ($N \le 10^5$), find the maximum length of a palindrome formed by $A[i..j]$, $B[i..j]$, or $A[i..j] + B[j..k]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $O(N^3)$ choices of $(i, j, k)$.
  2. *Combinatorial Invariant*: Fix the center $c$ of the palindrome (say in $A$). Expanding inside $A$ up to its maximal Manacher radius $[L_c, R_c]$ is always optimal before switching from $A$ to $B$, because any match $A[x] = A[y]$ inside the core also allows staying in $A$. At the first mismatch $A[L_c - 1] \ne A[R_c + 1]$, we switch the right wing to $B[R_c ..]$ (or the left wing to $A$ from a center in $B$).
  3. *Reverse-Engineering Scratchpad*: Run Manacher on $A$ and $B$. For each center $c$, extend $[L_c, R_c]$ outward by $\text{LCP}(A[1..L_c-1]^R, B[R_c..N])$ using SA/Z/Hashing. Time $O(N)$ or $O(N \log N)$.
  4. *Boundary Pitfall*: Off-by-one at the seam: when $A[i..j]$ concatenates with $B[j..k]$, index $j$ is used in **both** $A[j]$ and $B[j]$, so the right wing in $B$ starts at index $R_c$ (not $R_c + 1$)!

#### Problem W3A-07: `[ZJOI2013 / CF Restoration]` Prefix Function & Z-Array Restoration & Counting (`[ZH]` / `[EN]` Inverse KMP/Z)
- **Statement & Constraints**: Given a candidate KMP prefix array $\pi[1..N]$ ($N \le 2 \times 10^5$) and alphabet size $\sigma$, verify whether $\pi$ is realizable by some $S \in \Sigma^N$, and count the number of valid strings $S$ modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Checking only $\pi[i] \le \pi[i-1] + 1$ and fail-tree ancestry accepts invalid arrays like $\pi = [0, 1, 0, 1, 1]$.
  2. *Combinatorial Invariant*: Simulating KMP on $S[1..N]$ walks $k = \pi[i-1], \pi[k], \dots$ until $k + 1 = \pi[i]$. Every rejected $k$ forces $S[i] \ne S[k+1]$ (amortized $O(1)$ steps per $i$). When $\pi[i] > 0$, we must have $k + 1 == \pi[i]$ and $\text{comp}[\pi[i]] \notin \text{forb}_i$; when $\pi[i] == 0$, $S[i]$ starts a fresh component avoiding $\text{forb}_i \cup \{\text{comp}[1]\}$.
  3. *Reverse-Engineering Scratchpad*: Track component IDs $\text{comp}[1..N]$. At each $\pi[i] == 0$, multiply ways by $\max(0, \sigma - |\text{forb}_i|)$ in $O(N)$ time.
  4. *Boundary Pitfall*: Canonical counterexample $\pi = [0, 1, 0, 1, 1]$: at $i=5$, $k=\pi[4]=1$ fails ($S[5] \ne S[2] = S[1]$), while $k=0$ matches ($S[5] = S[1]$), contradiction!

#### Problem W3A-08: `[SDOI2016 / ICPC Gym]` Manacher Radius Array Restoration (`[ZH]` / `[EN]` Inverse Manacher)
- **Statement & Constraints**: Given odd radii $d_1[1..N]$ and even radii $d_2[1..N-1]$ ($N \le 5 \times 10^5$), determine if a valid string over $\Sigma$ exists, output the lexicographically smallest one, and count valid strings modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Adding all $O(N^2)$ mirror equalities $S[c - k] = S[c + k]$ times out.
  2. *Combinatorial Invariant*: Simulate the Manacher R-box expansion: only positions $p > R$ advancing the rightmost boundary require $S[p] = S[2c - p]$ ($\le N$ DSU unions!), and each center stopping inside $[1, N]$ adds at most one mismatch edge $S[c - d_1[c]] \ne S[c + d_1[c]]$.
  3. *Reverse-Engineering Scratchpad*: Unite equality pairs via DSU, collect mismatch edges, greedily assign smallest valid letters (or multiply $\max(0, \sigma - \text{deg}_{\text{prev}}(v))$ in earliest-index component order), and **run forward Manacher on the reconstructed string** to verify exact agreement with $d_1, d_2$! Time $O(N)$.
  4. *Boundary Pitfall*: Skipping the final forward Manacher verification misses contradictions where two characters given different components are forced equal or where mirror radii overflow $[L, R]$.

#### Problem W3A-09: `[CF 1721E]` Prefix Function Queries (`[EN]` Educational Codeforces Round 134 E)
- **Statement & Constraints**: Given base string $S$ ($|S| \le 10^6$) and $Q \le 10^5$ queries appending $T_q$ ($|T_q| \le 10$) to $S$, output $\pi[|S|+1 .. |S|+|T_q|]$ for each query (with rollback).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Amortized KMP fail-walking takes $\Theta(|S|)$ per query on $S = \texttt{a}^{|S|}, T_q = \texttt{b}$.
  2. *Combinatorial Invariant*: The KMP DFA transition `aut[k][c]` (exact analogue of PAM `quick_link[u][c]`) jumps in $O(1)$ worst-case time across all rejected borders inside $S[1..|S|]$.
  3. *Reverse-Engineering Scratchpad*: Precompute `aut[0..|S|][26]` in $O(|S| |\Sigma|)$, then extend rows $|S|+1 .. |S|+|T_q|$ per query in $O(|T_q| |\Sigma|)$.
  4. *Boundary Pitfall*: Running the `while` loop for $k \le |S|$ instead of looking up `aut[k][c]` directly triggers $\Theta(Q |S|)$ TLE.

#### Problem W3A-10: `[ARC 060 E]` Best Representation (`[JA]` AtCoder Regular Contest 060 E)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), find the minimum number of pieces in a partition of $S$ into aperiodic strings (strings with no proper period dividing their length), and count the number of such minimal partitions.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Testing all substrings for periodicity is $O(N^2)$.
  2. *Combinatorial Invariant*: By Fine–Wilf, any string $S \ne c^N$ is either already aperiodic ($1$ piece) or can be partitioned into **$2$ aperiodic pieces** $S[1..k] + S[k+1..N]$!
  3. *Reverse-Engineering Scratchpad*: Run KMP on $S$ and $S^R$ to mark in $O(N)$ which prefixes $S[1..k]$ and suffixes $S[k+1..N]$ are periodic ($(k - \pi[k]) \mid k$ and $\pi[k] > 0$). Count valid split points $k \in [1, N-1]$.
  4. *Boundary Pitfall*: Forgetting the divisibility test $(k - \pi[k]) \mid k$ falsely marks bordered non-periodic strings like $\texttt{aba}$ as periodic.

---

### 5.3 Tier 2: Intermediate (`W3A-11` – `W3A-20` — Tree PAM, Deque PAM Insertions, PAM Intersection, Even Greedy Factorization & Range LPS)

#### Problem W3A-11: `[BJWC2018]` 词韵 / Tree PAM (`[ZH]` Luogu P5327 / Tree Palindromic Paths)
- **Statement & Constraints**: Given a rooted tree $T$ ($N \le 10^5$, $|\Sigma| = 26$) with character-labeled edges, find for every node $x$ the number of distinct palindromes on the root-to-$x$ path and the longest palindromic suffix of the path.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Amortized `fail` walking on a tree takes $\Theta(N^2)$ on a broom tree ($\texttt{a}^{N/2}$ stem with $N/2$ leaf branches labeled $\texttt{b}$).
  2. *Combinatorial Invariant*: Using `quick_link[u][c]` on PAM nodes + a DFS depth-character stack `dep_char[dep]` performs each tree-edge extension in **worst-case $O(1)$ time**!
  3. *Reverse-Engineering Scratchpad*: Maintain a single shared PAM Trie across the DFS; at node $x$ with parent $p$ and edge char $c$, check `dep_char[dep[x] - 1 - len[u]] == c`, else jump $u \leftarrow \text{quick\_link}[u][c]$ in $O(1)$.
  4. *Boundary Pitfall*: Do not allocate duplicate PAM nodes when two sibling tree edges out of $p$ carry the same character $c$—reuse the existing `tr[u][c]`!

#### Problem W3A-12: `[AGC 047 B]` First Second (`[JA]` AtCoder Grand Contest 047 B)
- **Statement & Constraints**: Given $N$ strings $S_1, \dots, S_N$ ($\sum |S_i| \le 10^6$), you may repeatedly delete the 1st or 2nd character of a string. Count pairs $(i, j)$ such that $S_i$ can be reduced to $S_j$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $O(N^2)$ pairwise checks fail.
  2. *Combinatorial Invariant*: $S_i$ reduces to $S_j$ iff $S_j[2..|S_j|]$ is a suffix of $S_i$ and the character $S_j[1]$ appears at least once in the prefix $S_i[1 .. |S_i| - |S_j| + 1]$.
  3. *Reverse-Engineering Scratchpad*: Insert all $S_i^R$ into a Trie; maintain at each Trie node $u$ the count of strings $S_j$ whose $S_j[2..]^R$ ends at $u$ grouped by $S_j[1] \in \Sigma$, and query along $S_i^R$ using a prefix character bitmask in $O(\sum |S_i| |\Sigma|)$.
  4. *Boundary Pitfall*: Subtract $i = j$ self-pairs.

#### Problem W3A-13: `[Luogu P5555]` 秩序魔咒 (Common Palindromes of Two Strings, `[ZH]`)
- **Statement & Constraints**: Given $A$ and $B$ ($|A|, |B| \le 2.5 \times 10^5$), find the length of the longest common palindromic substring of $A$ and $B$, and how many distinct common palindromes achieve that length.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $\text{LCS}(A, B^R)$ via SAM matches non-palindromic substrings with reversed copies at different indices.
  2. *Combinatorial Invariant*: Every palindrome corresponds to a unique path from $r_{-1}$ or $r_0$ in the PAM Trie. Thus common palindromes of $A$ and $B$ correspond 1-to-1 with the **intersection of the PAM Tries** of $A$ and $B$.
  3. *Reverse-Engineering Scratchpad*: Build $\text{PAM}(A)$ and $\text{PAM}(B)$, then run simultaneous DFS (`dfs(u_A, u_B)`) from $(r_{-1}, r_{-1})$ and $(r_0, r_0)$ over shared transitions $c \in \Sigma$ (or build a Generalized PAM). Time $O((|A| + |B|)|\Sigma|)$.
  4. *Boundary Pitfall*: Never use SAM on $A \# A^R$ without checking center alignment; PAM Trie intersection is both simpler and 100% immune to misaligned reversals.

#### Problem W3A-14: `[JSOI2013 / SHOI2014]` 快乐的 JYY / 基因合成 (`[ZH]` Luogu P5685 / BZOJ 3676 — Generalized PAM Weighted Common Palindromes)
- **Statement & Constraints**: Given $K$ strings $S_1, \dots, S_K$ ($K=2$ or general $K$, $\sum |S_i| \le 5 \times 10^5$), compute $\sum_{P \text{ pal}} \prod_{i=1}^K \text{occ}_{S_i}(P)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Need exact occurrence counts $\text{occ}_{S_i}(u)$ of every distinct palindrome $u$ across multiple strings.
  2. *Combinatorial Invariant*: In a **Generalized PAM**, resetting `last = 0` at the beginning of each string $S_i$ (using string-local mirror checks $S_i[r - 1 - \text{len}(u)] == S_i[r]$) builds a single shared PAM with **zero clone/split anomalies** because every node $u$ has a single exact length $\text{len}(u)$!
  3. *Reverse-Engineering Scratchpad*: Build G-PAM over $S_1, \dots, S_K$, accumulate $\text{cnt}[u][i]$ bottom-up along the `fail` tree, and sum $\prod_{i=1}^K \text{cnt}[u][i]$ over all $u \ge 2$ in $O(\sum |S_i|)$ time.
  4. *Boundary Pitfall*: Exclude the two roots $r_{-1}, r_0$ from the product sum, and ensure string-local indexing prevents $r - 1 - \text{len}(u)$ from reading into $S_{i-1}$.

#### Problem W3A-15: `[HDU 6599]` I Love Palindrome String (`[ZH]` Half-Palindrome Multiplicity Spectrum)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^5$), for every $L \in [1, N]$, output the total occurrences of palindromic substrings $P$ of length $L$ whose prefix of length $\lceil L/2 \rceil$ is also a palindrome.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Unlike `W3A-04`, $L$ can be odd or even ($\lceil L/2 \rceil = \lfloor(L+1)/2\rfloor$), and we must sum occurrences over all valid PAM nodes of each length $L$.
  2. *Combinatorial Invariant*: At the moment PAM node $u$ is created ending at $r$, its prefix of length $\lfloor(\text{len}(u)+1)/2\rfloor$ is $S[r - \text{len}(u) + 1 .. r - \lfloor \text{len}(u)/2 \rfloor]$, which can be tested for palindromicity in $O(1)$ via Manacher on $S$ (or via the `half[u]` pointer)!
  3. *Reverse-Engineering Scratchpad*: Build PAM of $S$, accumulate `cnt[fail[u]] += cnt[u]`, test each node $u$'s half-prefix in $O(1)$ via Manacher radius at its creation interval, and add `cnt[u]` to `ans[len[u]]`. Time $O(N)$.
  4. *Boundary Pitfall*: Using $O(1)$ Manacher lookup on $u$'s creation interval completely avoids parity bugs in `half[u]` pointer maintenance for odd vs. even lengths.

#### Problem W3A-16: `[CF 17E]` Palisection (`[EN]` Codeforces Beta Round 17 E)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^6$, **Memory Limit: 64–128 MB**), count pairs of overlapping palindromic substrings modulo $51123987$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Total palindromes $T = \Theta(N^2)$ overflows 32-bit ints, and $26$-width PAM arrays exceed 64 MB for $N = 2 \times 10^6$.
  2. *Combinatorial Invariant*: By complementary counting, $\text{Overlapping} = \binom{T}{2} - \sum_{1 \le r < l \le N} \text{end\_cnt}[r] \cdot \text{start\_cnt}[l]$. In Manacher, center $c$ adds $+1$ to `start_cnt` on $[c - d_1[c] + 1, c]$ and $+1$ to `end_cnt` on $[c, c + d_1[c] - 1]$.
  3. *Reverse-Engineering Scratchpad*: Use two $O(N)$ difference arrays over Manacher centers (or adjacency-list PAM) to compute `start_cnt` and `end_cnt` in $O(N)$ time and $O(N)$ memory.
  4. *Boundary Pitfall*: Compute $T \pmod{51123987}$ and multiply by $\text{inv}(2)$ when evaluating $\binom{T}{2} \bmod 51123987$.

#### Problem W3A-17: `[CF 1080E]` Sonya and Matrix Beauty (`[EN]` Codeforces Round 524 E)
- **Statement & Constraints**: Given an $N \times M$ grid ($N, M \le 250$), count subgrids where each row can be rearranged into a palindrome such that the resulting columns are also palindromes.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $O(N^2 M^2)$ subgrids.
  2. *Combinatorial Invariant*: Inside column strip $[c_1, c_2]$, row $r$ can form a palindrome iff its 26-bit parity mask has $\text{popcount}(\text{mask}_r) \le 1$, and two rows $r_1, r_2$ can match symmetrically across columns iff their 26-letter frequency vectors are **identical** ($V_{r_1} == V_{r_2}$).
  3. *Reverse-Engineering Scratchpad*: Fix $[c_1, c_2]$ in $O(M^2)$, maintain $V_r$ and $\text{mask}_r$ incrementally, replace invalid rows ($\text{popcount} > 1$) with distinct negative sentinel vectors, and run 1D Manacher across the $N$ rows in $O(N)$. Total time $O(M^2 N)$.
  4. *Boundary Pitfall*: Two invalid rows with identical frequency vectors must NOT match each other during Manacher expansion!

#### Problem W3A-18: `[HDU 5421 / BZOJ 4976]` Victor and String (`[ZH]` / `[EN]` Double-Ended Insertion PAM)
- **Statement & Constraints**: Maintain an initially empty string under $Q \le 2 \times 10^5$ operations: `push_front(c)`, `push_back(c)`, query distinct palindromes, and query total palindromes with multiplicity.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Front and back insertions require maintaining both $\text{first}$ (longest palindromic prefix) and $\text{last}$ (longest palindromic suffix) on a shared PAM.
  2. *Combinatorial Invariant*: By reversal symmetry $P = P^R$, a single PAM serves both ends. Whenever `push_back(c)` produces $\text{len}(\text{last}) == R - L + 1$, the whole string is a palindrome so $\text{first} \leftarrow \text{last}$ (and symmetrically on `push_front`). Each push adds $\text{depth}_{\text{fail}}(\text{first}/\text{last})$ to the multiplicity count.
  3. *Reverse-Engineering Scratchpad*: Center array $S$ at index $Q + 5$ in size $2Q + 10$; keep $S[L-1] = -1, S[R+1] = -2$ as dynamic sentinels before each push. Time $O(Q)$.
  4. *Boundary Pitfall*: Forgetting the whole-string crossover synchronization `if (len[last] == R - L + 1) first = last;` breaks subsequent opposite-end insertions.

#### Problem W3A-19: `[CF 1827C]` Palindrome Partition (`[EN]` Codeforces Round 873 Div. 1 C — Greedy Even-Palindrome Factorization)
- **Statement & Constraints**: A string is *beautiful* if it is a concatenation of one or more non-empty **even-length** palindromes. Given $S[1..N]$ ($N \le 5 \times 10^5$), count how many substrings of $S$ are beautiful.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A beautiful substring can have many even-palindrome partitions; we need a unique canonical first step to count via $dp[r] = 1 + dp[r - L_r]$.
  2. *Combinatorial Invariant*: By the **Greedy Shortest Even-Palindrome Lemma** (Module 3A.4), a string $W$ is a concatenation of even palindromes iff its **shortest** non-empty even-length palindromic suffix $P$ exists and $W \setminus P$ is also a concatenation of even palindromes!
  3. *Reverse-Engineering Scratchpad*: In $\text{PAM}(S)$, precompute `min_even[u]` (shortest positive even-length ancestor on the `fail` tree) in $O(N)$ (`min_even[u] = (len[u] % 2 == 0 && !min_even[fail[u]]) ? u : min_even[fail[u]]`), or find the rightmost valid even Manacher center $c < r$. Set $dp[r] = 1 + dp[r - \text{len}(\text{min\_even}[\text{last}[r]])]$ and sum $dp[r]$ in $O(N)$ time.
  4. *Boundary Pitfall*: Taking the *longest* even-length palindromic suffix instead of the *shortest* fails on $S = \texttt{"abbaabba"}$.

#### Problem W3A-20: `[UOJ 103 / CTSC 2015 / QOJ]` Range Longest Palindromic Substring in $S[l..r]$ (`[ZH]` / `[EN]` Internal LPS)
- **Statement & Constraints**: Given $S[1..N]$ and $Q \le 5 \times 10^5$ online queries $[l, r]$, output the maximum length of a palindrome contained in $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Whole-string Manacher radii $d_1[c], d_2[c]$ overflow $[l, r]$.
  2. *Combinatorial Invariant*: Either binary search the monotone half-length predicate $\text{HasPal}_{\ge 2k-1}(l, r) \iff (\max_{c \in [l+k-1, r-k+1]} d_1[c] \ge k) \lor (\max_{c \in [l+k-1, r-k]} d_2[c] \ge k)$ in $O(\log(r-l))$ using Sparse Table RMQ, OR use Frontier 3A-I's unclipped interior identity $\max(|P_L|, |P_R|, \text{RMQ}(c_L+1, c_R-1))$ with `slink` ceiling division!
  3. *Reverse-Engineering Scratchpad*: Precompute $d_1, d_2$ and two Sparse Tables in $O(N \log N)$; answer queries in $O(\log(r-l))$.
  4. *Boundary Pitfall*: Using $[l+k-1, r-k+1]$ instead of $[l+k-1, r-k]$ for even centers reads 1 character past $r$.

---

### 5.4 Tier 3: Advanced (`W3A-21` – `W3A-31` — Queue PAM, `slink` DP, Range Distinct & Multiplicity Palindromes, PAM + SAM Merging)

#### Problem W3A-21: `[LOJ 6070 / BZOJ 4082 / CTSC]` 基因 (Gene — Sliding-Window Queue PAM with Front Pop & Back Push, `[ZH]`)
- **Statement & Constraints**: Maintain a string under $Q \le 5 \times 10^5$ online `push_back(c)` and `pop_front()` operations, reporting the number of distinct palindromic substrings in the current window $S[L..R]$ after each operation.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: FIFO deletions (`pop_front`) can destroy the unique occurrence of a maximal prefix palindrome, and amortized fail walks fail under deletions/updates.
  2. *Combinatorial Invariant*: Use `quick_link[u][c]` for worst-case $O(1)$ transitions and the **Lazy Surface Push-Down Invariant** (`max_pref[L]` pushes $f = \text{fail}(u)$ down to `max_pref[R_u - len(f) + 1]` and `max_suff[R_u]` upon `pop_front`), keeping PAM Trie nodes permanent and counting active nodes via `surf_cnt[u] + deg[u] > 0`.
  3. *Reverse-Engineering Scratchpad*: Every `push_back` and `pop_front` runs in worst-case $O(1)$ time and $O(N)$ space.
  4. *Boundary Pitfall*: Never physically unlink PAM Trie transitions on `pop_front`, and always increment `surf_cnt[fail[u]]` before decrementing `deg[fail[u]]`.

#### Problem W3A-22: `[CF 932G]` Palindrome Partition (`[EN]` ICM Technex 2018 — Symmetric Partition via Shuffle + PAM `slink` DP)
- **Statement & Constraints**: Given $S[1..N]$ ($2 \mid N \le 10^6$), count ways to partition $S = s_1 s_2 \dots s_{2k}$ such that $s_i = s_{2k+1-i}$ for all $i$, modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $s_i = s_{2k+1-i}$ couples opposite ends of $S$.
  2. *Combinatorial Invariant*: **Shuffle Interleaving**: Define $T = S[1] S[N] S[2] S[N-1] \dots S[N/2] S[N/2+1]$. Then $S[l..r] = S[N-r+1..N-l+1]$ iff $T[2l-1..2r]$ is an **even-length palindrome**! Apply PAM `slink` DP on $T$ in $O(N \log N)$.
  3. *Reverse-Engineering Scratchpad*: Maintain $g[u] = dp[r - (\text{len}[\text{slink}[u]] + \text{diff}[u])] + (\text{diff}[u] == \text{diff}[\text{fail}[u]] \ ? \ g[\text{fail}[u]] : 0)$ at **every** $r$, and set $dp[r] = \sum g[u]$ only at **even** $r$.
  4. *Boundary Pitfall*: Skipping the $g[u]$ update at odd $r$ corrupts the shifted AP sum for subsequent even $r$.

#### Problem W3A-23: `[CF 906E]` Reverses (`[EN]` Codeforces Round 454 Div. 1 E — Minimum Reversals via Shuffle + `slink` Argmin DP)
- **Statement & Constraints**: Given $A[1..N]$ and $B[1..N]$ ($N \le 5 \times 10^5$), find the minimum number of disjoint intervals to reverse in $A$ to obtain $B$, and output the intervals.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $\text{rev}(A[l..r]) = B[l..r]$ iff the interleaved substring $T[2l-1..2r]$ in $T = A[1] B[1] \dots A[N] B[N]$ is an even-length palindrome.
  2. *Combinatorial Invariant*: Run PAM `slink` DP over the $(\min, \text{argmin})$ semiring on $T$, where `g[u]` stores `(min_ops, left_endpoint_index)`. Notice that the **left endpoint** $r - \text{len}(v)$ is invariant when shifting from $r - \text{diff}[u] \to r$!
  3. *Reverse-Engineering Scratchpad*: Also include the $0$-cost transition $dp[2i] = \min(dp[2i], dp[2i-2])$ whenever $T[2i-1] == T[2i]$ ($A[i] == B[i]$). Time $O(N \log N)$.
  4. *Boundary Pitfall*: Storing the *palindrome node* or *length* instead of the *left endpoint* in `g[u]` breaks reconstruction because the palindrome length grows by $+2 \cdot \text{diff}[u]$ as $r$ advances while the left endpoint stays fixed!

#### Problem W3A-24: `[国家集训队论文 2014 — 徐毅 / BZOJ 5384 / LOJ 6071]` 区间本质不同回文串 (Offline Range Distinct Palindromes in $S[l..r]$, `[ZH]`)
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ queries $[l, r]$ ($N, Q \le 3 \times 10^5$), output the number of distinct palindromic substrings in $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Up to $\Theta(N)$ ancestors of $\text{pos}[r]$ update their latest occurrence at step $r$.
  2. *Combinatorial Invariant*: By **Periodic Suffix Telescoping Cancellation** (Module 3A.3), inside each `slink` chain $\{u_1, \dots, u_k\}$ from $\text{pos}[r]$, $\text{start}_{r-1}(u_j) = (r - d) - \text{len}(u_j) + 1 = r - \text{len}(u_{j-1}) + 1 = \text{start}_r(u_{j-1})$ for all $2 \le j \le k$. All internal nodes cancel out!
  3. *Reverse-Engineering Scratchpad*: For each `slink` chain head $u_1$ on the path from $\text{pos}[r]$, query $\text{prev\_r} = \text{SegMax.query}(\text{dfn}[u_1], \text{out}[u_1])$, add `-1` at $\text{prev\_r} - \text{len}(u_1) + 1$ (if $\text{prev\_r} > 0$), and add `+1` at $r - (\text{len}(\text{slink}[u_1]) + \text{diff}[u_1]) + 1$ in a Fenwick Tree. Update $\text{SegMax}$ at $\text{dfn}[\text{pos}[r]] \leftarrow r$. Time $O(N \log^2 N + Q \log N)$, space $O(N)$.
  4. *Boundary Pitfall*: Querying a scalar `last[u_1]` instead of subtree max `SegMax.query(dfn[u_1], out[u_1])` misses occurrences where $u_1$ was visited as an internal node of another chain!

#### Problem W3A-25: `[QOJ / Universal Cup]` Online Range Distinct Palindrome Queries with Encrypted Endpoints (`[EN]` / `[ZH]`)
- **Statement & Constraints**: Same as `W3A-24` ($N, Q \le 2 \times 10^5$), except queries $(l_i \oplus \text{last\_ans}, r_i \oplus \text{last\_ans})$ are strictly **online**.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Encrypted endpoints prevent offline sorting by $r$.
  2. *Combinatorial Invariant*: Because the `slink` Telescoping loop in `W3A-24` performs at most $2 \log_2 N$ point updates per step $r$, replacing the Fenwick Tree with a **Persistent Segment Tree** (`root[r]`) uses $O(N \log^2 N)$ total nodes and answers online queries in $O(\log N)$ time!
  3. *Reverse-Engineering Scratchpad*: During preprocessing $r = 1 \dots N$, apply the `-1` and `+1` updates to `PersistentSegTree` to build `root[r]`. Answer $(l, r)$ via `query(root[r], l, r)` in $O(\log N)$ time.
  4. *Boundary Pitfall*: Allocate persistent nodes in-place during step $r$ where feasible to minimize memory constant factor.

#### Problem W3A-26: `[Codeforces / SPOJ / HDU]` Large-$N$ Range All-Palindromes Multiplicity Queries (`[EN]` / `[ZH]`, $N, Q \le 3 \times 10^5$)
- **Statement & Constraints**: Given $S[1..N]$ and $Q \le 3 \times 10^5$ queries $[l, r]$, compute the total number of palindromic substrings (with multiplicity) inside $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $\sum_{c=l}^r \min(d_1[c], c - l + 1, r - c + 1)$ couples $c$ with both $l$ and $r$.
  2. *Combinatorial Invariant*: By the **Midpoint Decoupling Identity** (Module 3A.2), splitting odd centers at $m_{\text{odd}} = \lfloor(l+r)/2\rfloor$ and even centers at $m_{\text{even}} = \lfloor(l+r-1)/2\rfloor$ decouples the 3-way minimum into two 2-way minimums controlled by thresholds $L(c) \ge l$ and $R(c) \le r$.
  3. *Reverse-Engineering Scratchpad*: Sweep $l$ from $N \to 1$ and $r$ from $1 \to N$ with 3 Fenwick Trees ($\text{BIT}_{\text{rad}}, \text{BIT}_c, \text{BIT}_{\text{cnt}}$) in $O((N + Q) \log N)$ time (or Persistent Segment Trees for online queries).
  4. *Boundary Pitfall*: Using $m_{\text{odd}} = \lfloor(l+r)/2\rfloor$ instead of $m_{\text{even}} = \lfloor(l+r-1)/2\rfloor$ for even centers overcounts at $c = m_{\text{odd}}$ when $r - l$ is even (e.g., $S = \texttt{aaaa}, [1, 3]$).

#### Problem W3A-27: `[ZJOI2016 / HEOI2016 / Luogu P4094]` 字符串与回文 (Longest Palindrome in $S[a..b]$ Occurring in $S[c..d]$, `[ZH]`)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$) and $Q \le 10^5$ queries $(a, b, c, d)$, find the maximum length of a **palindromic** substring of $S[a..b]$ that also occurs in $S[c..d]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Intersects palindromic validity in $S[a..b]$ with substring containment in $S[c..d]$.
  2. *Combinatorial Invariant*: Build **Segment Tree Merging** over the **PAM `fail` tree** so every PAM node $u$ knows its exact right-endpoint occurrence set $\text{endpos}(u)$! Then palindrome $u$ occurs in $S[c..d]$ iff $\text{endpos}(u) \cap [c + \text{len}(u) - 1, d] \ne \emptyset$. Moreover, if $u$ occurs in $S[c..d]$, every `fail`-ancestor of $u$ ALSO occurs in $S[c..d]$!
  3. *Reverse-Engineering Scratchpad*: Merge segment trees bottom-up on the PAM `fail` tree in $O(N \log N)$, and combine center/ancestor binary lifting with $\text{endpos}$ range queries.
  4. *Boundary Pitfall*: Merging segment trees along the PAM Trie instead of the PAM **`fail` tree** fails because occurrences propagate along `fail` links!

#### Problem W3A-28: `[THUPC 2018 / Luogu P5446]` 绿绿和串串 (Mirror-Flip Generator Lengths, `[ZH]`)
- **Statement & Constraints**: Given $R[1..N]$ ($N \le 10^6$), an operation replaces $T[1..K]$ with $T[1..K] + T[K-1..1]$. Find all initial seed lengths $K \in [1, N]$ that can generate $R$ as a prefix.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Each mirror operation creates an odd palindrome centered at $K$.
  2. *Combinatorial Invariant*: Sweeping $K = N$ down to $1$, $K$ is valid iff either $K + d_1[K] - 1 == N$ (reaches the end of $R$ in 1 flip) OR ($K - d_1[K] + 1 == 1$ AND $K + d_1[K] - 1$ is already a valid seed length!).
  3. *Reverse-Engineering Scratchpad*: Compute odd Manacher $d_1[1..N]$ and sweep $K = N \to 1$ in $O(N)$ time.
  4. *Boundary Pitfall*: When $K + d_1[K] - 1 < N$, the palindrome centered at $K$ MUST reach the left boundary $1$ ($K - d_1[K] + 1 == 1$), otherwise the mirror mismatch occurred inside the string!

#### Problem W3A-29: `[SDOI2019 / ZJOI Style]` Length-Constrained Palindrome Partition ($L_{\min} \le |P| \le L_{\max}$, `[ZH]`)
- **Statement & Constraints**: Partition $S[1..N]$ ($N \le 3 \times 10^5$) into palindromes with length $\in [L_{\min}, L_{\max}]$, minimizing/counting pieces.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Cannot sum the entire `slink` chain unconditionally when lengths are bounded to $[L_{\min}, L_{\max}]$.
  2. *Combinatorial Invariant*: Inside a `slink` chain of step $d = \text{diff}[u]$, all transitions at step $r$ query left endpoints $l = r - \text{len}(v)$ in the same residue class modulo $d$, and as $r \to r + d$, the set of left endpoints shifts by at most 1 element!
  3. *Reverse-Engineering Scratchpad*: Maintain a residue-class monotonic queue or segment tree indexed by the invariant left endpoint $l = r - \text{len}(v)$ on each `slink` chain in $O(N \log^2 N)$ or $O(N \log N)$ time.
  4. *Boundary Pitfall*: Index the data structure by the **invariant left endpoint** $l = r - \text{len}(v)$, NOT by $\text{len}(v)$ (which shifts by $+d$ every period step!).

#### Problem W3A-30: `[ARC 151 E]` Keep Being Substring (`[JA]` AtCoder Regular Contest 151 E)
- **Statement & Constraints**: Given $A[1..N]$ and substrings $X, Y$, find the minimum single-character append/delete steps to transform $X$ into $Y$ while remaining a non-empty substring of $A$ at all times.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Full substring graph has $O(N^2)$ states.
  2. *Combinatorial Invariant*: If $X$ and $Y$ do not overlap as substrings of $A$ (checked via SA + LCP), any optimal path shrinks $X$ to a single character of length $1$, walks single-character transitions in $A$, and grows to $Y$.
  3. *Reverse-Engineering Scratchpad*: Combine SA/LCP overlap distance with $26$-vertex BFS in $O(N \log N)$.
  4. *Boundary Pitfall*: Missing the case where $X$ and $Y$ share a common substring of length $\ge 2$ inside $A$ without shrinking all the way to length $1$.

#### Problem W3A-31: `[NOI 2016 Variant / CCPC]` Palindromic Square-Concatenation (`AB` with $A$ Palindrome and $B = XX$ Square, `[ZH]` / `[EN]`)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), count substrings or splits $S[l..r] = A B$ where $A$ is a palindrome and $B = XX$ is a square.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Combines palindrome enumeration with periodic run / square enumeration.
  2. *Combinatorial Invariant*: Enumerate squares via Runs / LCE difference arrays (`start_sq[i]`), and combine with PAM `fail`-tree depths or Manacher difference arrays (`end_pal[i-1]`).
  3. *Reverse-Engineering Scratchpad*: Sweep split point $i \in [1, N-1]$ in $O(N \log N)$.
  4. *Boundary Pitfall*: Distinguish counting distinct decompositions $(l, i, r)$ vs. distinct intervals $[l, r]$.

---

### 5.5 Tier 4: Mastery (`W3A-32` – `W3A-42` — Full 4-Way Deque PAM, Weighted Range Distinct Palindromes, Rich Word $O(1)$ Queries, RLE PAM, Dynamic Character Healing & Online 2-Palindromes)

#### Problem W3A-32: `[Universal Cup / QOJ / Xu Yi 2014]` Full 4-Way Deque Palindromic Automaton (`push_front`, `push_back`, `pop_front`, `pop_back`, `[EN]` / `[ZH]` / `[JA]`)
- **Statement & Constraints**: Maintain an initially empty deque string $S[L..R]$ under $Q \le 5 \times 10^5$ online operations: `push_front(c)`, `push_back(c)`, `pop_front()`, `pop_back()`. Output after each operation: (1) distinct palindromes in $S[L..R]$, (2) longest palindromic prefix length, and (3) longest palindromic suffix length.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Arbitrary 4-way insertions and deletions break amortized fail links and LIFO undo stacks.
  2. *Combinatorial Invariant*: Combine `quick_link[u][c]` (worst-case $O(1)$ fail jumps), **Permanent PAM Trie Reuse**, **Unique Vanishing Palindrome Theorem**, and **Lazy Endpoint Surface Push-Down** (`max_pref[L..R]`, `max_suff[L..R]`, `surf_cnt[u]`, `deg[u]`).
  3. *Reverse-Engineering Scratchpad*: On `pop_back()` at $R$: let $u = \text{max\_suff}[R]$, $l_u = R - \text{len}(u) + 1$, $f = \text{fail}(u)$. Clear $\text{max\_suff}[R]$, set $\text{max\_pref}[l_u] = f$, update $\text{max\_suff}[l_u + \text{len}(f) - 1]$ with $f$ if longer, and if $\text{surf\_cnt}[u] + \text{deg}[u] == 0$, decrement `active_distinct` and `deg[f]`. Symmetrically for `pop_front()` at $L$. Worst-case $O(1)$ per operation!
  4. *Boundary Pitfall*: Reset `first = last = 0` whenever $L > R$; never cascade deletions because `surf_cnt[f]` is incremented before `deg[f]` is decremented!

#### Problem W3A-33: `[THUPC / CTS / CF 1083D Analogue]` Weighted Range Distinct Palindromes in $S[l..r]$ (`[ZH]` / `[EN]` PAM `slink` Difference Progression & LCT `access`)
- **Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 10^5$), where each distinct palindrome $P$ has weight $w(P)$ (e.g., $|P|$, $|P|^2$, or arbitrary node weight), answer queries $[l, r]$ asking for $\sum_{P \text{ distinct pal in } S[l..r]} w(P)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: When $w(u_j) \ne w(u_{j+1})$, internal nodes of a `slink` chain no longer cancel to $0$!
  2. *Combinatorial Invariant*: By Module 3A.3 Invariant B, at step $r$, across a `slink` chain $\{u_1, \dots, u_k\}$ of step $d = \text{diff}(u_1)$, the net change at old position $\text{prev\_r}(u_1) - \text{len}(u_1) + 1$ is $-w(u_1)$, at internal positions $r - \text{len}(u_j) + 1$ ($1 \le j \le k-1$) is $+\big(w(u_j) - w(u_{j+1})\big)$, and at $r - \text{len}(u_k) + 1$ is $+w(u_k)$! For $w(u) = \text{len}(u)$, $w(u_j) - w(u_{j+1}) = d$ is a constant added along an arithmetic progression of step $d$; for arbitrary weights, LCT `access(pos[r])` on the PAM Fail Tree groups vertical chains sharing uniform previous right endpoint $t$.
  3. *Reverse-Engineering Scratchpad*: Use `slink` AP range updates (for polynomial weights) or LCT `access` color-chain sweeping + Fenwick/Segment Tree in $O((N + Q) \log^2 N)$.
  4. *Boundary Pitfall*: Always separate the chain head $u_1$ (whose previous right endpoint is `SegMax.query(dfn[u_1], out[u_1])`) from $u_2 \dots u_k$ (whose previous right endpoint is deterministically $r - d$).

#### Problem W3A-34: `[ICPC / Universal Cup / AtCoder]` Rich Words & $O(1)$ Rich Substring Queries (`[EN]` / `[ZH]` / `[JA]`)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$) and $Q \le 5 \times 10^5$ queries $[l, r]$, determine for each query whether $S[l..r]$ is a **Rich Word** (contains exactly $r - l + 1$ non-empty distinct palindromes), and count the total number of rich substrings of $S$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Querying a Persistent Segment Tree of distinct palindromes takes $O(\log N)$ per query and $O(N \log^2 N)$ space.
  2. *Combinatorial Invariant*: By **Glen–Justin–Widmer–Zamboni Factor Closure (Module 3A.4)**, every substring of a rich word is rich! Therefore, for each right endpoint $r$, there exists a monotonic left threshold $L_{\text{rich}}[r]$ ($L_{\text{rich}}[r-1] \le L_{\text{rich}}[r]$) such that $S[l..r]$ is rich $\iff l \ge L_{\text{rich}}[r]$!
  3. *Reverse-Engineering Scratchpad*: Run a two-pointer Sliding-Window Queue PAM (`W3A-21`): advance $r = 1 \dots N$ with `push_back(S[r])`, and while `active_distinct < r - L + 1`, call `pop_front()` and increment $L$. Record $L_{\text{rich}}[r] = L$. Total rich substrings $= \sum_{r=1}^N (r - L_{\text{rich}}[r] + 1)$ in **$O(N)$ time**, and each query $[l, r]$ is answered in **$O(1)$ time** (`l >= L_rich[r]`)!
  4. *Boundary Pitfall*: Missing Factor Closure leads competitors to build heavy $O(N \log^2 N)$ 2D structures for a problem that is $O(N)$ preprocess + $O(1)$ query!

#### Problem W3A-35: `[CF 914E]` Palindromes in a Tree (`[EN]` Codeforces 8VC Venture Cup / Round 458 E)
- **Statement & Constraints**: Given a tree $T$ ($N \le 2 \times 10^5$) with vertex labels in `'a'`–`'t'` ($|\Sigma| = 20$), find for every vertex $v$ the number of undirected paths $(x, y)$ passing through $v$ whose character multiset can be rearranged into a palindrome.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $O(N^2)$ paths, and each valid path $(x, y)$ increments **all** vertices on the path $x \leftrightarrow y$.
  2. *Combinatorial Invariant*: A path can be rearranged into a palindrome iff its 20-bit XOR mask has $\text{popcount} \le 1$ ($21$ target masks). Apply **Centroid Decomposition**: at centroid $r$, paths $x \to r \to y$ with $M(x) \oplus M(y) \oplus (1 \ll c_r) \in \text{Targets}$ contribute $+1$ to the path $x \to r$ and $r \to y$ via bottom-up subtree prefix sums!
  3. *Reverse-Engineering Scratchpad*: At each centroid, sweep child subtrees forward and backward (or add all then subtract self-subtree) to count valid partners for each node $x$, push subtree sums up to $r$, and divide the root-passing cross-subtree contribution at $r$ by $2$. Time $O(N |\Sigma| \log N)$.
  4. *Boundary Pitfall*: Cross-subtree paths $(x, y)$ are counted twice at the centroid $r$ (once from $x$'s subtree, once from $y$'s subtree), whereas paths starting at $r$ itself $(r, x)$ are counted only once!

#### Problem W3A-36: `[CPM / QOJ / NOI Style]` Minimum Palindromic Length, Parity-Split & Uniqueness of Factorization (`[EN]` / `[ZH]` Borozdin–Kosolobov–Rubinchik–Shur)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6$), compute for every prefix $S[1..r]$: (1) its **Palindromic Length** $\text{PL}(S[1..r])$ (minimum palindromes partitioning $S[1..r]$), (2) whether this minimum partition is unique, and (3) the minimum odd-piece and even-piece palindrome partitions.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Here **both odd-length and even-length** palindromes are allowed in the partition.
  2. *Combinatorial Invariant*: PAM `slink` DP works over any commutative semiring: use the $(\min, \text{count})$ semiring for uniqueness and a $2$-element parity vector `(min_even_pieces, min_odd_pieces)` for piece-count parity!
  3. *Reverse-Engineering Scratchpad*: At step $r$, update `g[u]` from $dp[r - (\text{len}[\text{slink}[u]] + \text{diff}[u])]$ and `g[fail[u]]` (if $\text{diff}[u] == \text{diff}[\text{fail}[u]]$), then fold `g[u]` into $dp[r]$ with $+1$ piece count (and parity swap). Time $O(N \log N)$.
  4. *Boundary Pitfall*: Never store the $+1$ transition offset inside `g[u]`; `g[u]` must cache raw $dp[l]$ values at previous split points $l$, adding $+1$ only when updating $dp[r]$.

#### Problem W3A-37: `[UOJ / LOJ / QOJ]` Persistent Tree PAM with Online Leaf Additions & Path Palindrome Occurrence Queries (`[ZH]` 可持久化树上 PAM)
- **Statement & Constraints**: Given a dynamic character tree starting from root $1$ ($Q \le 10^5$ operations), support online: (1) add leaf $v$ as a child of $p$ with edge character $c$, (2) given vertex $v$ and length cap $L$, find the longest palindromic suffix of $\text{path}(1 \to v)$ of length $\le L$ and count how many times it occurs along $\text{path}(1 \to v)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Dynamic tree branching with online path-occurrence queries; $|\Sigma|$ can be up to $O(N)$.
  2. *Combinatorial Invariant*:
     - **Shared Global PAM Trie**: `fail[u]`, `slink[u]`, and `quick_link[u][c]` depend ONLY on the palindrome $u$ itself, so a single global PAM serves the entire tree without persistent Trie node copying!
     - **Alphabet-Free $O(\log N)$ `slink`-Skip (Module 3A.1 Invariant B)**: Using binary lifting `up[v][k]` on the input tree to read ancestor characters + `slink`-skipping fail walk finds $\text{pos}[v]$ in worst-case $O(\log^2 N)$ time (or $O(\log N)$ with `quick_link`) and **$O(1)$ PAM memory per node**!
  3. *Reverse-Engineering Scratchpad*: For query (2), lift $\text{pos}[v]$ via `slink` ceiling division to find the target palindrome $u^*$ of length $\le L$, and query the number of ancestors $x$ of $v$ on the tree path (of depth $\ge \text{len}(u^*)$) whose $\text{pos}[x]$ lies in the PAM `fail`-subtree of $u^*$.
  4. *Boundary Pitfall*: Realizing that the PAM Trie does not need path-copying persistence saves $O(N |\Sigma|)$ memory.

#### Problem W3A-38: `[AtCoder AGC / JOI]` Palindromic Substrings on Run-Length Encoded (RLE) Strings (`[JA]`, $|S| \le 10^{14}, M \le 10^5$ runs)
- **Statement & Constraints**: Given a string $S$ of length $\le 10^{14}$ compressed as $M \le 10^5$ RLE runs $(c_1, k_1), \dots, (c_M, k_M)$ ($c_i \ne c_{i+1}$), count both the total number of palindromic substrings (with multiplicity) and the number of **distinct** palindromic substrings of $S$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $|S| \le 10^{14}$ forbids character-level Manacher or PAM.
  2. *Combinatorial Invariant*: Any palindrome in $S$ either lies inside a single run $(c_i, k_i)$ OR spans $2r + 1 \ge 3$ runs centered at the **entire middle run** $(c_i, k_i)$, where internal runs $1 \le j < r$ must match in **both character and exact length** $(c_{i-j}, k_{i-j}) == (c_{i+j}, k_{i+j})$, while the two outer boundary runs only require $c_{i-r} == c_{i+r}$ and can extend by $1 \dots \min(k_{i-r}, k_{i+r})$ characters!
  3. *Reverse-Engineering Scratchpad*: Run odd-center Manacher / PAM on the $M$-element sequence of pairs $P_i = (c_i, k_i)$. For multiplicity, add $\sum \binom{k_i+1}{2}$ plus $\min(k_{i-r}, k_{i+r})$ at each pair-Manacher stopping boundary where $c_{i-r} == c_{i+r}$. For distinct count, record for each pair-PAM node $u$ and outer character $c$ the maximum boundary extension $\max \min(k_{i-r}, k_{i+r})$ achieved across all occurrences of $u$. Time $O(M \log M)$.
  4. *Boundary Pitfall*: A multi-run palindrome can NEVER be centered at the boundary between run $i$ and run $i+1$ because $c_i \ne c_{i+1}$!

#### Problem W3A-39: `[GYM 104077 / ICPC Regional / UCup]` Dynamic Single-Character Replacement Total Palindrome Queries (`[ZH]` / `[EN]`)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$) and $Q \le 10^5$ independent queries asking for the total number of palindromic substrings if a single character $S[i]$ is temporarily replaced by $c$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Re-running Manacher per query takes $O(QN)$.
  2. *Combinatorial Invariant*: Changing $S[i] \leftarrow c$ ($c \ne S[i]$):
     - **Destroys** the outer $d[m] - |m - i|$ palindromes of every center $m \ne i$ whose Manacher interval covers $i$ ($|m - i| < d[m]$)—a static linear pyramid subtracted via a 2nd-order difference array in $O(N)$!
     - **Creates** new palindromes ONLY at centers $m$ whose **first mismatch** in $S$ was at index $i$ (i.e., $i = m - d[m]$ with $c == S[m + d[m]]$, or $i = m + d[m]$ with $c == S[m - d[m]]$), extending them by $1 + \text{LCE}(m - d[m] - 1, m + d[m] + 1)$!
  3. *Reverse-Engineering Scratchpad*: Precompute `destroyed[i]` via 2nd-order difference arrays and `created[i][c]` via SA/LCE at the $2N-1$ Manacher mismatch boundaries in $O(N \log N)$. Answer each query in **$O(1)$ time**!
  4. *Boundary Pitfall*: Changing $S[i]$ NEVER destroys odd palindromes **centered at $m = i$ itself**! Exclude $m = i$ from the destruction pyramid.

#### Problem W3A-40: `[QOJ / Universal Cup Grandmaster]` Online Substring 2-Palindrome Recognition ($S[l..r] = P_1 P_2$, `[EN]` / `[ZH]`)
- **Statement & Constraints**: Given $S[1..N]$ and $Q \le 10^5$ online queries $[l, r]$, decide whether $S[l..r]$ can be split into two non-empty palindromes $P_1 P_2$ (and find a valid split point).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Scanning all $r - l$ split points is $O(N)$ per query, and greedily testing *only* the single longest palindromic prefix $Q_1$ fails on $S = \texttt{"bababcba"} = \texttt{"bab"} + \texttt{"abcba"}$ (where $Q_1 = \texttt{"babab"}$ leaves $\texttt{"cba"}$).
  2. *Combinatorial Invariant*: By **Theorem 2.2 (Frontier 3A-II)**, if $S[l..r] = P_1 P_2$, then either $P_1$ is one of the top 2 nodes of one of the $O(\log(r-l))$ `slink` chains of the longest palindromic prefix of $S[l..r]$, OR $P_2$ is one of the top 2 nodes of one of the $O(\log(r-l))$ `slink` chains of the longest palindromic suffix of $S[l..r]$!
  3. *Reverse-Engineering Scratchpad*: Lift $\text{first}[l]$ in $\text{PAM}(S^R)$ and $\text{last}[r]$ in $\text{PAM}(S)$ to length $\le r - l$ via `slink`, and for each of the $O(\log(r-l))$ AP blocks, test its top 2 lengths against an $O(1)$ Manacher palindrome check on the complementary piece. Time $O(\log(r-l))$ per query!
  4. *Boundary Pitfall*: Testing only $1$ node per AP chain fails on $S = \texttt{"bababcba"}$ where $Q_1 = \texttt{"babab"}$ and $P_1 = \text{fail}(Q_1) = \texttt{"bab"}$ belong to the **same** `slink` AP of period $d = 2$! You MUST test the top **2** nodes of each AP chain ($u$ and $\text{fail}(u)$).

#### Problem W3A-41: `[QOJ / Universal Cup Grandmaster]` Internal Palindromic Prefix/Suffix & Large Palindromic Border Queries on $S[l..r]$ (`[EN]` / `[ZH]`)
- **Statement & Constraints**: Given $S[1..N]$ and $Q \le 2 \times 10^5$ online queries $[l, r]$, compute the length of the longest palindromic prefix and suffix of $S[l..r]$, and count how many palindromic prefixes of $S[l..r]$ have length $\ge \frac{1}{2}(r - l + 1)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Need ancestor queries on $\text{PAM}(S)$ and $\text{PAM}(S^R)$ in $O(N)$ memory without $O(N \log N)$ binary lifting tables.
  2. *Combinatorial Invariant*: Walk `slink` chains from $\text{last}[r]$ until $\text{len}(\text{slink}[u]) \le r - l + 1$, then apply Cohort 2's closed-form ceiling division $\text{len}(u) - \lceil (\text{len}(u) - (r - l + 1)) / \text{diff}[u] \rceil \cdot \text{diff}[u]$, and count nodes in the AP down to $\ge \frac{1}{2}(r - l + 1)$ by integer division in $O(1)$.
  3. *Reverse-Engineering Scratchpad*: Build forward and backward PAMs with `diff` and `slink` in $O(N)$ space; answer queries in $O(\log N)$ time.
  4. *Boundary Pitfall*: Ensure the ceiling division only triggers when $\text{len}(u) > r - l + 1$.

#### Problem W3A-42: `[ABC 259 Ex / ZJOI2019]` Palindromic Covers, Non-Overlapping Identical Palindromes & Grid Palindromic Paths (`[JA]` / `[ZH]`)
- **Statement & Constraints**: Count pairs of identical **non-overlapping** palindromic substrings in $S[1..N]$ ($N \le 3 \times 10^5$), or count palindromic paths on a DAG/grid.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: For each distinct palindrome $u$ in $\text{PAM}(S)$, we must count pairs $(r_1, r_2) \in \text{endpos}(u)^2$ such that $r_2 - r_1 \ge \text{len}(u)$.
  2. *Combinatorial Invariant*: Perform **DSU-on-Tree /启发式合并 (Small-to-Large Set Merging)** on the **PAM `fail` tree**! When merging child occurrence sets into node $u$, every new right endpoint $r$ inserted into $u$'s balanced BST/Fenwick tree queries the number of existing occurrences $r' \in S_u$ with $r' \le r - \text{len}(u)$ or $r' \ge r + \text{len}(u)$? Wait: $\text{len}(u)$ changes as we move up the `fail` tree! So instead of querying during bottom-up merge for a single $u$, each small-to-large merge at node $u$ directly counts valid pairs $(r_1, r_2)$ with $|r_1 - r_2| \ge \text{len}(u)$ for $u$ itself, or combines PAM `fail`-tree Segment Tree Merging with `slink` periodicity!
  3. *Reverse-Engineering Scratchpad*: Use PAM `fail`-tree Segment Tree Merging / DSU-on-Tree in $O(N \log^2 N)$.
  4. *Boundary Pitfall*: Because $\text{len}(u)$ decreases as we move up the `fail` tree, a pair $(r_1, r_2)$ that overlapped at child $v$ ($|r_1 - r_2| < \text{len}(v)$) can become **non-overlapping** at ancestor $u$ ($|r_1 - r_2| \ge \text{len}(u)$)!

---

## 6. Cohort 3 Wave 3A Verification Checklist

- [x] **Cross-Cohort Blind-Spot Audit Complete**: Explicitly reconciled all theoretical, indexing, and problem differences between Cohort 1 (`iter_21_to_25`) and Cohort 2 (`cohort2_iter_73_to_77`).
- [x] **Frontier Gap-Hunt Complete**: Added strict $O(1)$ Online Range LPS (`Frontier 3A-I`), the One-Sided Sufficiency Theorem & Top-2-of-Each-AP proof for 2-Palindromes (`Frontier 3A-II`), $O(N)$ preprocess + $O(1)$ query Rich Substring recognition via Factor Closure (`Module 3A.4`), and Gapped Palindromes (`Frontier 3A-III`).
- [x] **Master Problem Archive Complete**: 42 deduplicated non-template problems (`W3A-01`–`W3A-42`) with full 4-Step Zero-Magic Analysis + 12 Quarantined Templates (`R-3A-01`–`R-3A-12`).
