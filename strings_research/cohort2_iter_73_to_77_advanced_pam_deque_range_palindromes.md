# Wave 3A (Cohort 2: Iterations 73–77) — Advanced Palindromic Structures, Deque/Persistent PAM, Substring Palindrome Queries & Rich Words

> [!IMPORTANT]
> **Cohort 2 Independent Redundant Discovery Report (`cohort2_iter_73_to_77`)**
> This report is authored independently by Cohort 2 for **Wave 3A (Iterations 73–77)** without consulting Cohort 1's output. Every theorem, structural invariant, data-structure coupling, failure mode, and practice problem solution follows the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard** from `strings_research/PLAN.md`. Standard Palindromic Automaton (PAM / Eertree) and Manacher construction templates are assumed as part of the reader's competitive programming library; our focus is strictly on non-amortized/persistent/double-ended extensions, substring range query decompositions on $S[l..r]$, combinatorial word theory of palindromes (Rich Words, $\theta$-palindromes, inverse string reconstruction), and grandmaster contest reductions across `[EN]`, `[ZH]`, and `[JA]` sources.

---

## 0. Multilingual Terminology & Reference Rosetta Stone (Wave 3A)

| Concept / Structural Tool | English (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) | Key Literature / Origin |
| :--- | :--- | :--- | :--- | :--- |
| Palindromic Tree / Automaton | Eertree / Palindromic Automaton (PAM) | 回文自动机 / 回文树 (`PAM`) | 回文木 (Palindromic Tree / Eertree) | Rubinchik & Shur (2015); Xu Yi (`徐毅`, 2014 National Team Paper) |
| Direct Fail-Transition Table | Direct / Unamortized Fail Link (`quick_link[u][c]`) | 直接后缀链接 / 确定性转移 (`anc[u][c]` / `quick_link`) | 直接遷移リンク (永続回文木用遷移表) | Rubinchik & Shur (2015); Persistent/Tree PAM treatises |
| Series Link / Periodic Link | Series Link (`slink`) & Period Step (`diff`) | 等差数列链跳转 (`slink` / `diff`) | 等差数列リンク (`slink` / 周期リンク) | Galil & Seiferas; Ilik (2014); Rubinchik & Shur (2018) |
| Double-Ended Palindromic Automaton | Double-Ended / Deque Eertree | 双向回文自动机 (`双向 PAM` / 双端 PAM) | 両端回文木 (Deque Palindromic Tree) | Xu Yi (`徐毅`, 2014); Rubinchik & Shur; `henkoku` / `noshi91` |
| Range Distinct Palindromes | Substring Distinct Palindrome Query ($S[l..r]$) | 区间本质不同回文串计数 | 区間相異なる回文数クエリ | Xu Yi (`徐毅`, 2014); Rubinchik & Shur (2017); Kociumaka et al. |
| Rich Word / Full Word | Palindromically Rich Word ($N+1$ palindromes) | 满回文串 / Rich 词 | リッチ語 (Rich Word / 最大回文含有語) | Droubay, Justin & Pirillo (2001); Glen, Justin, Widmer & Zamboni (2009) |
| Watson–Crick / Involution Palindrome | $\theta$-Palindrome / Gapped or Complement Palindrome | 反对称回文串 / 互补回文串 | 反対称回文 / 相補回文 ($\theta$-回文) | Kari & Mahalingam; AtCoder / Codeforces involution problems |
| Inverse String Reconstruction | Array Restoration (from $\pi$, $Z$, or Manacher radii) | 由前缀函数 / Z数组 / 回文半径还原字符串 | 文字列復元問題 (MP / Z / Manacher からの復元) | Clement, Crochemore & Rytter (2009); ICPC / CF restoration problems |

---

## Iteration 73: Deterministic Online, Persistent/Tree (`树上 PAM`), and Double-Ended (Deque) PAM (`双向回文自动机`)

### 73.1 Step 1 — The Diagnostic Signal (Why Naive Amortized PAM Fails)

In a standard append-only Palindromic Automaton (PAM) over a string $S[1..N]$, appending a character $c = S[r]$ at the right end locates the longest palindromic suffix of $S[1..r]$ by starting at $u = \text{last}$ (the longest palindromic suffix of $S[1..r-1]$) and walking the fail chain:
$$\text{while } S[r - \text{len}(u) - 1] \ne S[r]: \quad u \leftarrow \text{fail}(u).$$
Why is this fast on a linear string? By a potential argument on $\text{depth}(u)$ (or $\text{len}(u)$), each step $r$ increases the depth in the Fail Tree by at most $1$, while each fail-link transition strictly decreases it, bounding the total work across $N$ right-appends by $O(N)$.

**Three contest scenarios shatter this amortization:**
1. **Strings on a Trie / Tree (`树上 PAM`) or Backtracking Queries (`push` + `undo`)**: Suppose a problem gives a tree or trie of $N$ nodes, or asks online queries that repeatedly append a character and then roll back (`undo`), or requires a **Persistent PAM** across version histories. An adversary can construct a spine of length $N/2$ whose longest palindromic suffix has fail-depth $\Theta(N)$ (e.g., $S = \texttt{a}^{N/2}$), and attach $N/2$ leaf branches each labelled with $\texttt{b}$. Every leaf branch starts at $u$ with $\text{len}(u) = N/2$, fails $N/2$ times down to the odd root $r_1$, and then rolls back! The potential is restored on every rollback, degrading total time from $O(N)$ to $\Theta(N^2)$.
2. **Double-Ended Appends (`双向 PAM` — `push_front` & `push_back`)**: When characters can be inserted at both the front ($L \leftarrow L-1$) and the back ($R \leftarrow R+1$) of a deque string $S[L..R]$, a standard PAM only tracks `last_back` (the longest palindromic suffix of $S[L..R]$). It cannot extend on the left without also tracking `last_front` (the longest palindromic prefix of $S[L..R]$) and detecting when a front insertion spans the entire string $S[L..R]$, modifying `last_back` simultaneously.
3. **Double-Ended Deletions (`pop_front` & `pop_back`)**: When characters are deleted from either end of $S[L..R]$ (not merely rolled back in LIFO order, as a queue is FIFO!), the longest palindromic prefix or suffix may vanish from $S[L..R]$ entirely. If a node $u$ still has longer palindromic extensions active inside the remaining window, $u$ remains present; if $u$ was the *unique* maximal occurrence and no longer palindrome inside $S[L..R]$ has $\text{fail}(v) = u$, then $u$ ceases to exist in $S[L..R]$, and `last_front` / `last_back` must be updated in worst-case $O(1)$ time without rescanning the string.

---

### 73.2 Step 2 — The Combinatorial Word Invariant

#### Invariant 73.2.1: Position-Independence of Preceding Characters on the Fail Chain (`quick_link[u][c]`)

Let $u$ be any node in the PAM representing a palindrome $P$ of length $L = \text{len}(u) \ge 0$, and let $v$ be any **proper** fail-ancestor of $u$ (including the even root $r_0$ with $\text{len}(r_0) = 0$ and the odd root $r_1$ with $\text{len}(r_1) = -1$), so that $\text{len}(v) < \text{len}(u)$.

Suppose $u$ occurs as a suffix of $S[1..r-1]$, occupying the interval $S[r - L .. r - 1]$. When we test whether $v$ can be extended by $c = S[r]$ to form $c v c$, we inspect the character $S[r - \text{len}(v) - 1]$.

**Claim (Intrinsic Preceding-Character Lemma)**: The character $S[r - \text{len}(v) - 1]$ depends **exclusively on the palindrome $u$ and the ancestor $v$**, and is completely independent of the position $r$ where $u$ ends in $S$!

**Proof by Index Alignment**:
Since $v$ is a proper fail-ancestor of $u$ and both have integer lengths $\ge -1$, we have $\text{len}(v) \le \text{len}(u) - 1$, which rearranges to:
$$r - \text{len}(u) \le r - \text{len}(v) - 1 \le r - 1.$$
Every index in $[r - \text{len}(u), r - 1]$ lies **strictly inside** the occurrence of the palindrome $P = S[r - \text{len}(u) .. r - 1]$! Specifically, indexing $P$ as $P[1..\text{len}(u)]$, the position $r - \text{len}(v) - 1$ is the character at index:
$$k = \text{len}(u) - \text{len}(v) \in [1, \text{len}(u)+1]$$
of $P$. Furthermore, when $v \ne r_1$ ($\text{len}(v) \ge 0$), because $P$ is a palindrome ($P[k] = P[\text{len}(u) - k + 1]$), this character is also equal to $P[\text{len}(v) + 1]$—the character immediately following the prefix copy of $v$ inside $P$:
$$S[r - \text{len}(v) - 1] = P[\text{len}(u) - \text{len}(v)] = P[\text{len}(v) + 1].$$

```
Palindrome u = S[r - len(u) .. r - 1]:
|<--------------------- len(u) --------------------->|
[  v (prefix)  ][x] .............. [x][  v (suffix)  ]  [c = S[r]]
|<-- len(v) -->| ^                  ^  |<-- len(v) -->|
                 |                  |
      P[len(v)+1] == P[len(u)-len(v)] == S[r - len(v) - 1]
```

**Consequence (`quick_link` Recurrence)**:
For every PAM node $u$ and every character $c \in \Sigma$, we can define $\text{quick\_link}(u, c)$ as the **longest proper fail-ancestor** $v$ of $u$ such that the character immediately preceding the suffix $v$ of $u$ is $c$ (or $v = r_1$ if no non-negative ancestor is preceded by $c$, since $r_1$ has $\text{len}(r_1) = -1$ and $S[r - (-1) - 1] = S[r] = c$ always matches!).

Because every proper fail-ancestor of $u$ is either $\text{fail}(u)$ itself or a proper fail-ancestor of $\text{fail}(u)$, the table $\text{quick\_link}(u, \cdot)$ differs from $\text{quick\_link}(\text{fail}(u), \cdot)$ in **at most ONE character**: namely, the character $c^* = S[r - \text{len}(\text{fail}(u)) - 1]$ that immediately precedes $\text{fail}(u)$ inside $u$!
$$\text{quick\_link}(u, c) = \begin{cases} \text{fail}(u), & \text{if } c = S[r - \text{len}(\text{fail}(u)) - 1], \\ \text{quick\_link}(\text{fail}(u), c), & \text{otherwise.} \end{cases}$$

Thus, when creating node $u$ at position $r$:
1. Copy $\text{quick\_link}(u, \cdot) \leftarrow \text{quick\_link}(\text{fail}(u), \cdot)$ in $O(|\Sigma|)$ time (or $O(\log |\Sigma|)$ with a persistent balanced tree / segment tree if $|\Sigma|$ is large).
2. Overwrite the single entry $\text{quick\_link}(u, S[r - \text{len}(\text{fail}(u)) - 1]) \leftarrow \text{fail}(u)$.

When extending from $u = \text{last}$ by $c = S[r]$:
- If $S[r - \text{len}(u) - 1] = c$, then $u$ itself extends to $c u c$ in $0$ hops!
- Otherwise, a **single lookup** $u \leftarrow \text{quick\_link}(u, c)$ jumps directly to the exact longest fail-ancestor that can be extended by $c$ in **worst-case $O(1)$ time**!

---

#### Invariant 73.2.2: The $O(\log N)$ `slink`-Skipping Fail Walk (Alphabet-Free Unamortized PAM)

What if $|\Sigma| = O(N)$ and we want $O(\log N)$ worst-case transition time with $O(1)$ memory per node (no $O(|\Sigma|)$ `quick_link` array and no persistent segment tree overhead)?

Recall from Wave 1A that for any node $u$, $\text{diff}(u) = \text{len}(u) - \text{len}(\text{fail}(u))$ is the minimal period of $u$ whenever $\text{len}(\text{fail}(u)) \ge \frac{1}{2}\text{len}(u)$, and $\text{slink}(u)$ points to the highest ancestor of $u$ with the same $\text{diff}$ (or more standardly, the first proper fail-ancestor $w$ with $\text{diff}(w) \ne \text{diff}(u)$).

**Claim (Uniform Preceding-Character Along an AP Block)**:
Let $u = u_1 \to u_2 \to \dots \to u_k$ ($k \ge 2$) be a maximal chain of fail links with constant difference:
$$\text{diff}(u_1) = \text{diff}(u_2) = \dots = \text{diff}(u_{k-1}) = d.$$
Then for every $j \in \{1, 2, \dots, k-1\}$, the character immediately preceding $u_{j+1}$ inside $S[1..r-1]$ is **identical** to the character immediately preceding $u_1$ inside $S[1..r-1]$:
$$S[r - \text{len}(u_2) - 1] = S[r - \text{len}(u_3) - 1] = \dots = S[r - \text{len}(u_k) - 1].$$

**Proof**:
Because $u_1$ has period $d$ (as $u_2 = \text{fail}(u_1)$ is a border of $u_1$ of length $\text{len}(u_1) - d \ge \text{len}(u_k) \ge 0$), any two positions inside $S[r - \text{len}(u_1) .. r - 1]$ at distance a multiple of $d$ that both lie within the span of $u_1$ carry the same character!
Look at the indices $p_j = r - \text{len}(u_j) - 1$ for $j \in \{2, \dots, k\}$:
- Since $\text{len}(u_j) = \text{len}(u_1) - (j-1)d$, we have $p_j = p_2 + (j-2)d$.
- Because $\text{len}(u_k) \ge 0$ and $\text{len}(u_2) = \text{len}(u_1) - d$, every index $p_j$ ($2 \le j \le k$) satisfies:
  $$r - \text{len}(u_1) \le r - \text{len}(u_2) - 1 = p_2 \le p_j \le p_k = r - \text{len}(u_k) - 1 \le r - 1.$$
- Thus **all** of $p_2, p_3, \dots, p_k$ lie inside the periodic palindrome $u_1 = S[r - \text{len}(u_1) .. r - 1]$ and are congruent modulo its period $d$! Therefore:
  $$S[p_2] = S[p_3] = \dots = S[p_k].$$

**Algorithmic Consequence**:
When testing $u_1$ at right endpoint $r$:
1. First test $u_1$ itself: does $S[r - \text{len}(u_1) - 1] = S[r]$? (Note: $r - \text{len}(u_1) - 1$ lies *outside* $u_1$, so it is not constrained by period $d$.)
2. Next test $u_2 = \text{fail}(u_1)$: does $S[r - \text{len}(u_2) - 1] = S[r]$?
   - If YES, we stop at $u_2$.
   - If NO, then by the Uniform Preceding-Character Lemma, $u_3, \dots, u_k$ **also fail** because they test the exact same character $S[p_2] \ne S[r]$! Thus we can immediately skip the entire arithmetic progression and jump directly to $u_k = \text{slink}(u_1)$!
Since jumping to $\text{slink}(u_1)$ halves the length in at most 2 steps, this finds the target fail-ancestor in **worst-case $O(\log N)$ time using $O(1)$ space per node**!

---

#### Invariant 73.2.3: Dual-Boundary Symmetry & Whole-String Crossover in Deque PAM (`双向 PAM`)

Because the reversal of any palindrome $P$ is $P$ itself ($P^R = P$), a string $w$ is a palindromic prefix of $S[L..R]$ if and only if $w = w^R$ is a palindromic suffix of $(S[L..R])^R$. Consequently:
- A **single** PAM node set and Fail Tree represents both the palindromic prefixes and the palindromic suffixes of $S[L..R]$.
- We maintain two active pointers on the same PAM:
  - $\text{last\_back}$: the PAM node corresponding to the longest palindromic **suffix** of $S[L..R]$.
  - $\text{last\_front}$: the PAM node corresponding to the longest palindromic **prefix** of $S[L..R]$.

**The Whole-String Crossover Invariant**:
When we append a character $c$ to the back (`push_back(c)`, incrementing $R \leftarrow R+1$ with $S[R] = c$):
- The new longest palindromic suffix $u' = \text{extend\_back}(\text{last\_back}, R)$ has length $\text{len}(u') \le R - L + 1$.
- Could `push_back(c)` change the longest palindromic **prefix** $\text{last\_front}$?
  - Every prefix of $S[L..R]$ either ends at some $r' < R$ (already present in $S[L..R-1]$) or ends at $R$ (i.e., is the entire string $S[L..R]$).
  - Therefore, $\text{last\_front}$ changes **if and only if** the entire new string $S[L..R]$ is a palindrome, which occurs if and only if:
    $$\text{len}(\text{last\_back}) = R - L + 1 \implies \text{last\_front} \leftarrow \text{last\_back}.$$
Symmetrically, after `push_front(c)` (decrementing $L \leftarrow L-1$ with $S[L] = c$), we update $\text{last\_front}$ using the left-extension check $S[L + \text{len}(u) + 1] == S[L]$ (accelerated via `quick_link`), and then check:
$$\text{if } \text{len}(\text{last\_front}) = R - L + 1: \quad \text{last\_back} \leftarrow \text{last\_front}.$$

---

#### Invariant 73.2.4: Double-Ended Deletions (`pop_front` & `pop_back`) via Maximal-Surface Reference Counting

Why is deleting from a general deque (`pop_front` and `pop_back` mixed arbitrarily) much subtler than LIFO `undo` on a stack?
In a stack (`push_back` + `pop_back`), popping $S[R]$ simply restores the state from step $R-1$. In a deque, however, a node $u$ created during an early `push_back` might be popped from the **front** via `pop_front`, or a palindrome might occur multiple times inside $S[L..R]$!

How do we maintain the exact set of distinct palindromes in $S[L..R]$, along with $\text{last\_front}$ and $\text{last\_back}$, in $O(1)$ worst-case time per `push_front`, `push_back`, `pop_front`, and `pop_back`?

**Key Structural Observation (Fail-Tree Leafhood & Longest Boundary Palindromes)**:
At any moment, a palindrome $P$ (represented by PAM node $u$) occurs in $S[L..R]$ if and only if either:
1. $P$ is the **maximal palindrome ending at some position $r \in [L, R]$** (or equivalently starting at some $l \in [L, R]$), OR
2. Some strictly longer palindrome $Q$ occurring in $S[L..R]$ has $\text{fail}(Q) = P$.

Even better, when we delete the rightmost character $S[R]$ (`pop_back`):
- Which palindromes can possibly lose an occurrence? **Only** the palindromic suffixes of $S[L..R]$, which are the ancestors of $u = \text{last\_back}$ in the Fail Tree!
- Among those ancestors of $u = \text{last\_back}$, every proper ancestor $v = \text{fail}(u), \text{fail}(\text{fail}(u)), \dots$ has length $\text{len}(v) < \text{len}(u)$. By palindrome symmetry inside $u = S[R - \text{len}(u) + 1 .. R]$, $v$ is not only a suffix of $u$ (ending at $R$), it is also a **prefix** of $u$ (starting at $R - \text{len}(u) + 1$ and ending at $R - \text{len}(u) + \text{len}(v) \le R - 1$)!
- Read that again! Because $v$ is a **proper** border of the palindrome $u$, $v$ already has another occurrence completely contained in $S[L .. R-1]$ (namely, the prefix of $u$)!
- **Theorem (Unique Vanishing Palindrome on Boundary Pop)**:
  When deleting a single character from either end of $S[L..R]$ (say `pop_back` at $R$ with $u = \text{last\_back}$), **at most ONE distinct palindrome in the entire string $S[L..R]$ can disappear**—namely $u = \text{last\_back}$ itself! Every proper fail-ancestor of $u$ is guaranteed to remain in $S[L..R-1]$ because its reflected prefix occurrence inside $u$ ends at $R - \text{len}(u) + \text{len}(v) < R$!

And when does $u = \text{last\_back}$ itself disappear from $S[L..R-1]$?
- Every occurrence of $u$ in $S[L..R]$ is either a *non-suffix* occurrence inside some longer palindrome (so $u$ has a child in the active Fail Tree), or a *maximal* palindrome at its endpoints.
- Specifically, let us maintain for each position $i \in [L, R]$:
  - $\text{max\_pref}[i]$: the longest palindrome in $S[L..R]$ starting at $i$,
  - $\text{max\_suff}[i]$: the longest palindrome in $S[L..R]$ ending at $i$.
- Wait: if we maintain for each PAM node $u$ a reference count $\text{surf\_cnt}[u]$ equal to the number of active positions where $u$ was added as a maximal boundary palindrome (plus its active Fail-Tree out-degree $\text{deg}[u]$, or simply tracking the second-longest palindromic suffix $\text{fail}(u)$ when $\text{last\_back}$ is popped):
  - Whenever `push_back(c)` reaches node $u$ at position $R$:
    - $u$ becomes $\text{max\_suff}[R] = u$.
    - What is the corresponding start position of this occurrence of $u$? It starts at $l_u = R - \text{len}(u) + 1$. Since $\text{len}(u)$ is the longest palindrome ending at $R$, is $u$ necessarily the longest palindrome in $S[L..R]$ starting at $l_u$? Not if a longer palindrome starting at $l_u$ was already formed earlier and extends past $R$—which is impossible because $R$ is the current right boundary! Wait: what if a later `push_back` creates an even longer palindrome starting at $l_u$? Then $\text{max\_pref}[l_u]$ gets overwritten by the longer palindrome!
    - Instead of overwriting, notice an even cleaner invariant used in competitive programming Deque PAMs:
      - Maintain for each node $u$ the count $\text{cnt}[u]$ of times $u$ is currently the active endpoint created at a step, and $\text{deg}[u]$ = number of *currently existing* nodes $w$ in $S[L..R]$ with $\text{fail}(w) = u$.
      - Even simpler: when `push_back` adds $S[R]$ resulting in $u = \text{last\_back}$, the new $\text{max\_suff}[R]$ is $u$, and for the start position $l_u = R - \text{len}(u) + 1$, we can update $\text{max\_pref}[l_u] \leftarrow \max_{\text{len}}(\text{max\_pref}[l_u], u)$, while for $R$ itself we set $\text{max\_suff}[R] \leftarrow u$.
      - When `pop_back()` removes $S[R]$:
        1. Let $u = \text{last\_back} = \text{max\_suff}[R]$.
        2. After removing $S[R]$, the new longest palindromic suffix ending at $R-1$ is simply $\text{max\_suff}[R-1]$? **Careful!** Could $\text{max\_suff}[R-1]$ have started to the left of $L$ if `pop_front` occurred earlier?
        3. No, if we keep $\text{max\_suff}[i]$ clipped or notice that when $S[R]$ is popped, the longest palindrome ending at $R$ was $u$, so at $R$ its longest proper suffix $\text{fail}(u)$ ends at $R$, while at $R-1$ any palindrome ending at $R-1$ that started $\ge L$ is recorded in $\text{max\_suff}[R-1]$ *unless* a `pop_front` truncated it!
        4. How does `pop_front` affect $\text{max\_suff}$? When `push_back` at $R$ creates $u$, $\text{fail}(u)$ is a prefix of $u$ starting at $l_u = R - \text{len}(u) + 1$, so it ends at $r_{\text{ref}} = l_u + \text{len}(\text{fail}(u)) - 1 < R$. Thus, before $S[R]$ is popped, we can push $\text{fail}(u)$ down to $\text{max\_suff}[R - \text{len}(u) + \text{len}(\text{fail}(u))]$? No, the standard, rock-solid **Exact Deque PAM Invariant** is:
           - Maintain $\text{max\_pref}[i]$ (longest palindrome in $S[L..R]$ starting at $i$) and $\text{max\_suff}[i]$ (longest palindrome in $S[L..R]$ ending at $i$).
           - On `push_back(c)` at $R$: find $u = \text{extend\_back}(\text{last\_back}, R)$. Then $u$ starts at $l_u = R - \text{len}(u) + 1$ and ends at $R$. Set $\text{max\_suff}[R] = u$, and since $u$ is a palindrome starting at $l_u$ of length $\text{len}(u)$ and no palindrome in $S[L..R]$ ending $\le R$ can start at $l_u$ and have length $> R - l_u + 1 = \text{len}(u)$, $u$ is **guaranteed** to be strictly longer than the old $\text{max\_pref}[l_u]$! So we set $\text{max\_pref}[l_u] = u$!
           - On `pop_back()` at $R$: let $u = \text{max\_suff}[R]$ (which is $\text{last\_back}$), starting at $l_u = R - \text{len}(u) + 1$.
             - Since $S[R]$ is deleted, $u$ no longer ends at $R$. What is the new longest palindrome starting at $l_u$ inside $S[L..R-1]$?
             - It is the longest proper palindromic **prefix** of $u$, which by symmetry is $\text{fail}(u)$! Wait: could there be a palindrome starting at $l_u$ of length between $\text{len}(\text{fail}(u))$ and $\text{len}(u)$? **Impossible!** Because any palindrome starting at $l_u$ and ending $\le R-1$ is contained inside $u = S[l_u .. R]$ as a prefix of $u$, hence by reflection is a suffix of $u$, hence is $\le \text{len}(\text{fail}(u))$!
             - Therefore, when `pop_back()` deletes $S[R]$, the new longest palindrome starting at $l_u$ in $S[L..R-1]$ is $\max_{\text{len}}(\text{old\_max\_pref}[l_u], \text{fail}(u))$! And since $\text{old\_max\_pref}[l_u]$ was also a prefix of $u$, it was already $\le \text{len}(\text{fail}(u))$! Thus the new $\text{max\_pref}[l_u]$ is **always** $\max_{\text{len}}(\text{max\_pref}[l_u]\text{ before }u, \text{fail}(u)) = \text{fail}(u)$!
             - And what is the new $\text{last\_back}$ of $S[L..R-1]$? It is simply $\text{max\_suff}[R-1]$! Why is $\text{max\_suff}[R-1]$ guaranteed to lie inside $[L, R-1]$? Because every past `pop_front()` at $L'$ already replaced $\text{max\_suff}[r_w]$ of the popped front palindrome $w = \text{max\_pref}[L']$ (ending at $r_w = L' + \text{len}(w) - 1$) with $\text{fail}(w)$!

Let us double-check this! This duality between $\text{max\_pref}[l]$ and $\text{max\_suff}[r]$ is completely symmetric and requires **zero history stacks**:
- For every $i \in [L, R]$, $\text{max\_pref}[i]$ is the exact longest palindrome inside $S[L..R]$ starting at $i$, and $\text{max\_suff}[i]$ is the exact longest palindrome inside $S[L..R]$ ending at $i$.
- Why? Because if a palindrome $P = S[l..r]$ is truncated on the right when $r$ is popped (`pop_back` at $R = r$), $P$ must have been $u = \text{max\_suff}[R]$. Any shorter palindrome starting at $l_u$ and ending $\le R-1$ is a prefix of $u$, so the longest one is $\text{fail}(u)$! Thus setting $\text{max\_pref}[l_u] \leftarrow \text{fail}(u)$ (when $\text{max\_pref}[l_u] == u$) and setting $\text{max\_suff}[l_u + \text{len}(\text{fail}(u)) - 1] \leftarrow \max_{\text{len}}(\dots, \text{fail}(u))$ maintains the exact $\text{max\_pref}$ and $\text{max\_suff}$ arrays at all positions in $O(1)$ time!

---

### 73.3 Step 3 — The Reverse-Engineering Scratchpad (Algorithmic & Data-Structure Compilation)

Let us write out the exact invariants and transitions for both:
1. **Deterministic `quick_link` PAM** (supporting $O(1)$ worst-case `push_back`, `push_front`, and persistent/tree branching), and
2. **Full Double-Ended Deque PAM** (`push_front`, `push_back`, `pop_front`, `pop_back` in worst-case $O(1)$ time).

#### Contract 73.3.1: Deterministic `quick_link` Update on Node Creation

Suppose we create a new PAM node $u$ of length $\text{len}(u) = \text{len}(p) + 2$ by extending node $p$ with character $c$, and we have already found $u$'s fail link $f = \text{fail}(u)$ (specifically, if $p = r_1$, then $f = r_0$; otherwise $f = \text{next}(\text{quick\_link}(p, c), c)$ if $S[\text{inner\_match}(\text{fail}(p))] \ne c$, or $\text{next}(\text{fail}(p), c)$ if $\text{fail}(p)$ directly matches $c$).

Once $\text{fail}(u) = f$ is established:
- What character precedes $f$ inside the palindrome $u$?
- Since $u$ is a palindrome of length $\text{len}(u) \ge 1$ and $f$ has length $\text{len}(f) < \text{len}(u)$:
  - If $f = r_1$ ($\text{len}(f) = -1$, which never happens for $\text{len}(u) \ge 1$ since $\text{fail}(u) \ge 0$), no update is needed.
  - For $\text{len}(f) \ge 0$, the character immediately preceding the suffix $f$ inside $u$ (or immediately following the prefix $f$ inside $u$) is:
    - If $u$ was created at right endpoint $R$: $c_{\text{inner}} = S[R - \text{len}(f) - 1]$.
    - If $u$ was created at left endpoint $L$: $c_{\text{inner}} = S[L + \text{len}(f) + 1]$.
    - Notice that by palindrome symmetry of $u$, $S[R - \text{len}(f) - 1] = S[L_u + \text{len}(f)] = S[L + \text{len}(f) + 1]$—**it is the exact same character whether $u$ is created by `push_back` or `push_front`**!
- Therefore, $\text{quick\_link}(u, \cdot)$ is initialized by:
  $$\forall a \in \Sigma: \quad \text{quick\_link}(u, a) \leftarrow \text{quick\_link}(f, a),$$
  $$\text{quick\_link}(u, c_{\text{inner}}) \leftarrow f.$$
- Base cases at the two roots:
  - Odd root $r_1$ ($\text{len}(r_1) = -1$, $\text{fail}(r_1) = r_1$): $\text{quick\_link}(r_1, a) = r_1$ for all $a \in \Sigma$.
  - Even root $r_0$ ($\text{len}(r_0) = 0$, $\text{fail}(r_0) = r_1$): $\text{quick\_link}(r_0, a) = r_1$ for all $a \in \Sigma$.

#### Contract 73.3.2: Full Double-Ended Deque PAM (`push_front`, `push_back`, `pop_front`, `pop_back`)

```cpp
// Non-standard Deque PAM core showing O(1) worst-case quick_link + pop_front/pop_back surface pushing
struct DequePAM {
    static constexpr int ALPHA = 26;
    struct Node {
        int len, fail;
        int next[ALPHA];
        int quick[ALPHA];
        int deg;      // number of active nodes v in S[L..R] with fail[v] == u
        int surf_cnt; // number of boundary endpoints (max_pref or max_suff) equal to u
    };
    // Invariant: A node u (len > 0) exists in S[L..R] iff surf_cnt[u] > 0 || deg[u] > 0.
    // Whenever a new node u becomes active (transitions from non-existent to existent):
    //   distinct_palindromes++, deg[fail[u]]++.
    // Whenever u becomes inactive (surf_cnt[u] == 0 && deg[u] == 0):
    //   distinct_palindromes--, deg[fail[u]]--, and we remove u from its parent's next[] if recycled,
    //   OR keep trie structure persistent and only track active status via (surf_cnt[u] + deg[u] > 0)!
};
```

> [!TIP]
> **Never Delete Nodes Physically from the PAM Trie During `pop_front` / `pop_back`!**
> Because `quick_link[u][c]` and `next[u][c]` depend **only on the string $u$ itself** and never on the surrounding text $S[L..R]$, a PAM node $u$ once created is a permanent mathematical object! If $u$ disappears from $S[L..R]$ during a pop and later reappears during a push, reusing the existing node $u$ in `next[p][c]` is 100% valid!
> Instead of unlinking `next[p][c]`, simply track for each node $u$ with $\text{len}(u) > 0$:
> - $\text{surf\_cnt}[u]$: how many indices $i \in [L, R]$ have $\text{max\_pref}[i] = u$ plus how many have $\text{max\_suff}[i] = u$.
> - $\text{deg}[u]$: how many currently active nodes $v$ have $\text{fail}(v) = u$.
> - Node $u$ is **active** (present as a substring of $S[L..R]$) if and only if $\text{surf\_cnt}[u] + \text{deg}[u] > 0$!
> When `pop_back()` removes $S[R]$, let $u = \text{max\_suff}[R]$ and $l_u = R - \text{len}(u) + 1$:
> 1. Clear $\text{max\_suff}[R]$ (decrement $\text{surf\_cnt}[u]$).
> 2. At $l_u$, since $\text{max\_pref}[l_u]$ was $u$, replace $\text{max\_pref}[l_u]$ with $f = \text{fail}(u)$ (decrement $\text{surf\_cnt}[u]$, increment $\text{surf\_cnt}[f]$ if $\text{len}(f) > 0$), AND at the right endpoint of that prefix occurrence of $f$, namely $r_f = l_u + \text{len}(f) - 1$, if $\text{len}(f) > \text{len}(\text{max\_suff}[r_f])$, replace $\text{max\_suff}[r_f]$ with $f$ (updating $\text{surf\_cnt}$)!
> 3. Now check if $\text{surf\_cnt}[u] + \text{deg}[u] == 0$: if so, $u$ just vanished from $S[L..R-1]$! Decrement `active_distinct_count` and decrement $\text{deg}[\text{fail}(u)]$ (Note: $\text{fail}(u)$ itself cannot vanish on this step by our Unique Vanishing Palindrome Theorem!).

---

### 73.4 Step 4 — Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Broken Invariant 1 — Omitting the Whole-String Crossover Check (`len[last_back] == R - L + 1`)**:
   - *Counterexample*: Start with empty deque. Call `push_back('a')`, then `push_front('b')`, then `push_back('b')`.
   - After `push_back('a')` ($S = \texttt{a}$): if $\text{last\_front}$ is not updated to `'a'`, $\text{last\_front}$ remains $r_0$.
   - Even if initialized for size 1, after `push_front('b')` ($S = \texttt{ba}$): $\text{last\_front} = \texttt{'b'}$, $\text{last\_back} = \texttt{'a'}$.
   - Now call `push_back('b')` ($S = \texttt{bab}$): $\text{last\_back}$ becomes $\texttt{"bab"}$ of length $3 = R - L + 1$. If we forget `if (len[last_back] == R - L + 1) last_front = last_back`, then $\text{last\_front}$ remains $\texttt{'b'}$ (length 1) instead of $\texttt{"bab"}$ (length 3)! A subsequent `push_front('c')` on $\texttt{cbab}$ or `push_front('a')` on $\texttt{abab}$ will fail to test extending $\texttt{"bab"}$ on the left!
2. **Broken Invariant 2 — Out-of-Bounds Character Read in `quick_link` at the Odd Root**:
   - When $u = \text{last\_back}$ has $\text{len}(u) = R - L$ (one character shorter than the current string $S[L..R]$ after incrementing $R$), testing whether $u$ directly matches $S[R]$ checks index $R - \text{len}(u) - 1 = L - 1$, which is **outside** the valid window $[L, R]$!
   - *Fix*: Before testing $S[R - \text{len}(u) - 1] == S[R]$, always check `if (R - len[u] - 1 < L) u = quick_link[u][S[R]]` (or maintain distinct sentinel characters at $S[L-1]$ and $S[R+1]$ when not concurrently mutating, or perform the explicit boundary comparison `R - len[u] - 1 >= L && S[R - len[u] - 1] == S[R]`).
3. **Broken Invariant 3 — Physical Node Deletion Corrupting Internal Palindromes in Deque PAM**:
   - *Counterexample*: Consider $S = \texttt{abacaba}$. Suppose `pop_back()` removes the last $\texttt{a}$, leaving $\texttt{abacab}$. The node $u = \texttt{"abacaba"}$ disappears, so if we physically zeroed out transitions or failed to push $f = \text{fail}(u) = \texttt{"aba"}$ into $\text{max\_pref}[1]$ and $\text{max\_suff}[3]$, a subsequent `pop_back()` down to $\texttt{aba}$ would not know that $\text{max\_suff}[3] = \texttt{"aba"}$! Pushing $f = \text{fail}(u)$ to both $\text{max\_pref}[l_u]$ and $\text{max\_suff}[l_u + \text{len}(f) - 1]$ on `pop_back()` (and symmetrically $\text{max\_suff}[r_u]$ and $\text{max\_pref}[r_u - \text{len}(f) + 1]$ on `pop_front()`) is essential.

---

## Iteration 74: Substring Palindrome Queries on $S[l..r]$ (Part 1 — Longest Palindromic Substring & Count of All Palindromic Occurrences in $S[l..r]$)

### 74.1 Step 1 — The Diagnostic Signal (Why Whole-String Manacher and PAM Fail on $S[l..r]$)

Given a static string $S[1..N]$ and $Q$ online queries $(l, r)$, consider two fundamental internal palindrome queries:
- **Query Type A (Range Longest Palindrome)**: Find $\max \{ |P| : P \text{ is a palindromic substring of } S[l..r] \}$ (e.g., `Lougu P4555` variants, `CF 1080E`, internal palindrome problems).
- **Query Type B (Range Total Palindrome Count with Multiplicity)**: Find the total number of pairs $(i, j)$ with $l \le i \le j \le r$ such that $S[i..j]$ is a palindrome (e.g., `CF 245H — Queries for Number of Palindromes` when $N, Q \le 5 \times 10^5$ instead of $5000$, `BZOJ` / `HDU` large-$N$ range palindrome counting).

**Why naive lookups fail**:
- In Manacher's algorithm, $\text{rad}[c]$ gives the maximal radius of a palindrome centered at $c$ inside $S[1..N]$. For a query $[l, r]$, a center $c \in [l, r]$ has its valid radius **clipped** by the query boundaries to:
  $$\text{rad}_{[l, r]}(c) = \min\big(\text{rad}[c],\; c - l + 1,\; r - c + 1\big).$$
- In a PAM, $\text{dep}(\text{pos}[k])$ gives the number of palindromic suffixes of $S[1..k]$, including palindromes that start strictly to the left of $l$!

Because $\min(\text{rad}[c], c - l + 1, r - c + 1)$ couples the center variable $c$ with the query endpoints $l$ and $r$, taking a naive maximum or sum over $c \in [l, r]$ requires $O(r - l + 1)$ per query.

---

### 74.2 Step 2 — The Combinatorial Word Invariant

#### Invariant 74.2.1: Monotonicity of Unclipped Center Intervals (Binary Search + RMQ for Longest Palindrome)

To unify odd and even palindromes cleanly or handle them in parallel:
- **Odd palindromes**: A palindrome of odd length $2k - 1$ ($k \ge 1$) centered at $c \in [1, N]$ spans $[c - k + 1, c + k - 1]$. It is contained in $[l, r]$ if and only if:
  $$l \le c - k + 1 \quad\text{and}\quad c + k - 1 \le r \quad\text{and}\quad \text{rad}_{\text{odd}}[c] \ge k$$
  $$\iff c \in [l + k - 1,\; r - k + 1] \quad\text{and}\quad \text{rad}_{\text{odd}}[c] \ge k.$$
- **Even palindromes**: An even palindrome of length $2k$ ($k \ge 1$) centered between $c$ and $c+1$ spans $[c - k + 1, c + k]$. It is contained in $[l, r]$ if and only if:
  $$c \in [l + k - 1,\; r - k] \quad\text{and}\quad \text{rad}_{\text{even}}[c] \ge k.$$

**Monotonicity Proof**:
If $S[l..r]$ contains an odd palindrome of radius $k$ centered at $c$, then for any $k' < k$, the shorter palindrome of radius $k'$ centered at the *same* $c$ spans $[c - k' + 1, c + k' - 1] \subset [c - k + 1, c + k - 1] \subseteq [l, r]$ and satisfies $\text{rad}_{\text{odd}}[c] \ge k > k'$.
Wait: **odd lengths and even lengths must be binary-searched (or checked) separately**, because containing an even palindrome of length $2k$ does *not* imply containing an odd palindrome of length $2k-1$! However, within each parity (or by checking both $2k-1$ and $2k$ for the half-length parameter $k \in [1, \lfloor(r-l+1)/2\rfloor]$—since any palindrome of length $L$ contains a palindrome of length $L-2$ of the same parity, so $\exists$ palindrome of length $\ge 2k-1 \iff \text{odd}(k) \lor \text{even}(k)$!), the predicate:
$$\text{HasPal}_{\ge 2k-1}(l, r) \iff \left(\max_{c \in [l+k-1, r-k+1]} \text{rad}_{\text{odd}}[c] \ge k\right) \lor \left(\max_{c \in [l+k-1, r-k]} \text{rad}_{\text{even}}[c] \ge k\right)$$
**IS strictly monotone in $k$!**
Why? Because if $S[l..r]$ contains *any* palindrome $P$ of length $\ge 2k-1$:
- If $|P|$ is odd, stripping its outer characters leaves an odd palindrome of length $2k-1$ (radius $k$) around the same center.
- If $|P|$ is even, then $|P| \ge 2k$, so stripping its outer characters leaves an even palindrome of length $2k$ (half-length $k$) around the same center!
Thus a **single binary search** on $k \in [1, \lfloor (r - l + 2)/2 \rfloor]$ with $O(1)$ Sparse Table RMQ lookups finds the exact maximum $k$, and then we check whether $\text{even}(k)$ holds (giving $2k$) or only $\text{odd}(k)$ holds (giving $2k-1$)! Time: $O(N \log N)$ preprocessing, $O(\log N)$ per query.

#### Invariant 74.2.2: Eliminating the Binary Search — $O(1)$ Query via Boundary-Clipped Longest Prefix/Suffix + Interior RMQ

Can we answer Range Longest Palindrome in **worst-case $O(1)$ time per query** after $O(N \log N)$ preprocessing?
Suppose the longest palindrome $P = S[i..j]$ inside $S[l..r]$ has center $c$ and achieves the maximum length. There are only two possibilities:
1. **$P$ is unclipped by $[l, r]$**: The maximal palindrome centered at $c$ in the whole string $S[1..N]$ is completely contained in $[l, r]$.
2. **$P$ touches the boundary $l$ or $r$**: Either $i = l$ ($P$ is the **longest palindromic prefix** of $S[l..r]$) or $j = r$ ($P$ is the **longest palindromic suffix** of $S[l..r]$).

Even better: if we binary search $k$, that takes $O(\log N)$. To get $O(1)$ time per query *when longest palindromic prefix/suffix of $S[l..r]$ is known* (or via PAM binary lifting in $O(\log N)$):
Notice that on PAM, the longest palindromic suffix of $S[l..r]$ is found by starting at $u = \text{pos}[r]$ (the longest palindromic suffix of $S[1..r]$) and binary-lifting up the Fail Tree (or jumping $O(\log N)$ `slink` chains with a simple division!) to find the highest ancestor with $\text{len}(u) \le r - l + 1$.
Wait: using `slink` chains on PAM, how fast can we find the longest palindromic suffix of $S[l..r]$?
- Each `slink` chain $u_1 \to u_2 \to \dots \to u_k$ is an arithmetic progression with common difference $d = \text{diff}(u_1)$.
- If $\text{len}(\text{slink}(u_1)) > r - l + 1$, we jump directly to $\text{slink}(u_1)$ in $O(1)$ time.
- Once we reach the unique AP chain containing the target length $\le r - l + 1$, since all nodes in that AP chain exist in the PAM and have lengths $\text{len}(u_1) - j \cdot d$, we don't even need to walk inside the AP if we only need the **length**! The exact length of the longest palindromic suffix of $S[l..r]$ is simply:
  $$\text{len}(u_1) - \left\lceil \frac{\text{len}(u_1) - (r - l + 1)}{d} \right\rceil \cdot d!$$
- That computes the longest palindromic suffix of $S[l..r]$ in $O(\log N)$ arithmetic steps with **zero binary-lifting table memory**!

---

#### Invariant 74.2.3: The Midpoint Decoupling Identity for Counting All Palindromes in $S[l..r]$

Now consider **Query Type B**: counting *all* palindromic substrings inside $S[l..r]$ (with multiplicity).
For simplicity of exposition, let us trace odd-length palindromes (even-length palindromes follow the exact same formula on inter-character centers $c \in [l, r-1]$ with $\min(\text{rad}_{\text{even}}[c], c - l + 1, r - c)$, or both parities are handled simultaneously on the Manacher `#`-interleaved string $T[1..2N+1]$).

In $S[l..r]$, the number of odd-length palindromes is:
$$\text{Ans}_{\text{odd}}(l, r) = \sum_{c=l}^{r} \min\big(\text{rad}[c],\; c - l + 1,\; r - c + 1\big).$$

Look at the three-way minimum $\min(\text{rad}[c], c - l + 1, r - c + 1)$. Why is a three-way minimum awkward for data structures? Because it compares $c - l + 1$ against $r - c + 1$.
**The Midpoint Split**: Let $m = \lfloor \frac{l+r}{2} \rfloor$.
- For every $c \in [l, m]$, we have $2c \le l + r \iff c - l + 1 \le r - c + 1$. Thus $r - c + 1$ is **redundant** on $[l, m]$!
- For every $c \in [m+1, r]$, we have $2c > l + r \iff r - c + 1 < c - l + 1$. Thus $c - l + 1$ is **redundant** on $[m+1, r]$!

Therefore, the three-way minimum decomposes into **two completely decoupled two-way minimums**:
$$\text{Ans}_{\text{odd}}(l, r) = \sum_{c=l}^{m} \min\big(\text{rad}[c],\; c - l + 1\big) + \sum_{c=m+1}^{r} \min\big(\text{rad}[c],\; r - c + 1\big).$$

Now examine the left sum $\sum_{c=l}^{m} \min(\text{rad}[c], c - l + 1)$:
For each center $c$, let $L_c = c - \text{rad}[c] + 1$ be the left endpoint of the maximal palindrome centered at $c$. Then:
$$\min(\text{rad}[c],\; c - l + 1) = \begin{cases} \text{rad}[c], & \text{if } L_c \ge l, \\ c - l + 1, & \text{if } L_c < l. \end{cases}$$
Symmetrically, on the right half $c \in [m+1, r]$, let $R_c = c + \text{rad}[c] - 1$ be the right endpoint of the maximal palindrome centered at $c$. Then:
$$\min(\text{rad}[c],\; r - c + 1) = \begin{cases} \text{rad}[c], & \text{if } R_c \le r, \\ r - c + 1, & \text{if } R_c > r. \end{cases}$$

```
Midpoint Decoupling at m = floor((l + r) / 2):
Query [l ........................ m | m+1 ........................ r]
         ^                            ^
         | On [l, m]:                 | On [m+1, r]:
         | c - l + 1 <= r - c + 1     | r - c + 1 < c - l + 1
         | Only left boundary l       | Only right boundary r
         | can clip rad[c]!           | can clip rad[c]!
```

---

### 74.3 Step 3 — The Reverse-Engineering Scratchpad (Offline Sweep & Online Persistent Tree Compilation)

Using the Midpoint Decoupling Identity, let us compile $\text{Ans}_{\text{odd}}(l, r)$ into two 2D dominance queries that can be answered **offline in $O((N + Q) \log N)$ via Fenwick Trees** or **online in $O((N + Q) \log N)$ via a Persistent Segment Tree**:

1. **Left-Half Sum ($c \in [l, m]$)**:
   $$\sum_{c=l}^{m} \min(\text{rad}[c], c - l + 1) = \sum_{\substack{c \in [l, m] \\ L_c \ge l}} \text{rad}[c] + \sum_{\substack{c \in [l, m] \\ L_c < l}} (c - l + 1).$$
   Rewrite the second term by separating $c$ from $1 - l$:
   $$\sum_{\substack{c \in [l, m] \\ L_c < l}} (c - l + 1) = \left(\sum_{\substack{c \in [l, m] \\ L_c < l}} c\right) - (l - 1) \cdot \left(\sum_{\substack{c \in [l, m] \\ L_c < l}} 1\right).$$
   Notice that every sum here is a 1D range query over $c \in [l, m]$ after filtering by $L_c < l$ vs. $L_c \ge l$!
   - **Offline Sweep by Decreasing $l$ (from $N$ down to $1$)**:
     - Initially (before any $c$ has $L_c \ge l$), all centers $c$ are in the "clipped" state ($L_c < l$).
     - When the sweep pointer reaches $l$, every center $c$ with $L_c = l$ transitions from $L_c < l$ (clipped) to $L_c \ge l$ (unclipped)!
     - Maintain three Fenwick Trees over index $c \in [1, N]$:
       - `BIT_rad`: sum of $\text{rad}[c]$ for active (unclipped, $L_c \ge l$) centers $c$.
       - `BIT_c`: sum of $c$ for clipped ($L_c < l$) centers $c$.
       - `BIT_cnt`: count of $1$ for clipped ($L_c < l$) centers $c$.
     - Then for any query $(l, r)$ with midpoint $m = \lfloor (l+r)/2 \rfloor$, the left-half contribution at step $l$ is a single $O(\log N)$ range query on $[l, m]$ across the three Fenwick Trees!
2. **Right-Half Sum ($c \in [m+1, r]$)**:
   $$\sum_{c=m+1}^{r} \min(\text{rad}[c], r - c + 1) = \sum_{\substack{c \in [m+1, r] \\ R_c \le r}} \text{rad}[c] + (r + 1) \left(\sum_{\substack{c \in [m+1, r] \\ R_c > r}} 1\right) - \left(\sum_{\substack{c \in [m+1, r] \\ R_c > r}} c\right).$$
   - **Offline Sweep by Increasing $r$ (from $1$ up to $N$)**:
     - When the sweep pointer reaches $r$, every center $c$ with $R_c = r$ transitions from clipped ($R_c > r$) to unclipped ($R_c \le r$).
     - Query the corresponding three Fenwick Trees on $[m+1, r]$ in $O(\log N)$ time!
3. **Even-Length Palindromes**:
   - An even palindrome centered between $c$ and $c+1$ ($c \in [l, r-1]$) has clipped half-length $\min(\text{rad}_{\text{even}}[c], c - l + 1, r - c)$.
   - Split at $m_{\text{even}} = \lfloor \frac{l + r - 1}{2} \rfloor$:
     - For $c \in [l, m_{\text{even}}]$, $c - l + 1 \le r - c$, so the contribution is $\min(\text{rad}_{\text{even}}[c], c - l + 1)$ with threshold $L^{\text{even}}_c = c - \text{rad}_{\text{even}}[c] + 1 \ge l$.
     - For $c \in [m_{\text{even}} + 1, r - 1]$, $r - c \le c - l + 1$, so the contribution is $\min(\text{rad}_{\text{even}}[c], r - c)$ with threshold $R^{\text{even}}_c = c + \text{rad}_{\text{even}}[c] \le r$.
   - The exact same two sweeps (or Persistent Segment Trees for online queries) compute $\text{Ans}_{\text{even}}(l, r)$ in $O((N + Q) \log N)$!

---

### 74.4 Step 4 — Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Broken Invariant 1 — Using the Same Midpoint $m = \lfloor (l+r)/2 \rfloor$ for Even Centers**:
   - *Counterexample*: Let $S = \texttt{aaaa}$, query $[l, r] = [1, 3]$ ($\texttt{aaa}$).
   - For even centers $c \in [1, 2]$, at $c = 2$ (between $S[2]$ and $S[3]$), $c - l + 1 = 2 - 1 + 1 = 2$, whereas $r - c = 3 - 2 = 1$!
   - Notice that at $c = m = \lfloor(1+3)/2\rfloor = 2$, $c - l + 1 = 2 > r - c = 1$, so $c = 2$ is **right-clipped**, NOT left-clipped!
   - If you use $m = \lfloor(l+r)/2\rfloor = 2$ instead of $m_{\text{even}} = \lfloor(l+r-1)/2\rfloor = 1$ for even centers, then at $c = 2$ you compute $\min(\text{rad}_{\text{even}}[2], c - l + 1) = \min(2, 2) = 2$ instead of $\min(2, r - c) = 1$, counting the out-of-bounds palindrome $S[1..4]$ inside $S[1..3]$!
2. **Broken Invariant 2 — Unifying Odd and Even Centers via `#`-String Without Dividing Radii by 2**:
   - In the Manacher string $T = \texttt{\#} S[1] \texttt{\#} S[2] \texttt{\#} \dots \texttt{\#} S[N] \texttt{\#}$, a center $p \in [2l, 2r]$ has Manacher radius $p_{\text{rad}}[p]$ in $T$. The number of actual non-empty palindromes in $S[l..r]$ centered at $p$ is $\lfloor \frac{\min(p_{\text{rad}}[p],\; p - 2l + 1,\; 2r - p + 1)}{2} \rfloor$. Because of the floor division by $2$ (which behaves differently depending on parity of $p$), maintaining linear sums of $p$ directly on $T$ without separating odd $p$ and even $p$ introduces rounding errors of $\pm 1/2$ per center! Always either separate odd and even centers on $S[1..N]$ (as derived in §74.3) or split $T$'s indices by parity.

---

## Iteration 75: Substring Palindrome Queries on $S[l..r]$ (Part 2 — Distinct Palindromes in $S[l..r]$)

### 75.1 Step 1 — The Diagnostic Signal (Why Multiplicity Counting and Naive PAM Fail for Range Distinct Palindromes)

Consider the canonical **Substring Distinct Palindrome Query** problem (`[国家集训队论文 2014 — 徐毅]`, `BZOJ 4044` / `Luogu P5555`, `Universal Cup` / `QOJ` Range Distinct Palindromes):
> Given a string $S[1..N]$ and $Q$ queries $(l_i, r_i)$ ($N, Q \le 10^5$ or $3 \times 10^5$, offline or online), report the number of **distinct** non-empty palindromic substrings contained in $S[l_i..r_i]$.

**Why previous structures fail**:
- **Manacher + Midpoint Sweep fails**: In $S = \texttt{aaaaa}$, $S[1..5]$ has $\sum \text{rad} = 15$ palindromic occurrences, but only $5$ **distinct** palindromes ($\texttt{a}, \texttt{aa}, \texttt{aaa}, \texttt{aaaa}, \texttt{aaaaa}$).
- **Whole-string PAM fails**: The PAM of $S[1..N]$ has at most $N$ palindrome nodes, and each node $u$ represents one distinct palindrome. However, $u$ occurs in $S[l..r]$ if and only if there exists an occurrence of $u$ with right endpoint $p \in [l + \text{len}(u) - 1, r]$.
- **Why SAM's LCT `access` doesn't trivially copy-paste to PAM without modification**:
  In a Suffix Automaton (Wave 2A), a node $u$ represents a **contiguous interval of lengths** $[\text{len}(\text{link}(u)) + 1,\; \text{len}(u)]$. When `access(pos[r])` colors a solid splay chain with last-ending position $t$, the start positions of all substrings in node $u$ form a contiguous interval $[t - \text{len}(u) + 1,\; t - \text{len}(\text{link}(u))]$, which maps to a single range addition on a Segment Tree!
  In a **Palindromic Automaton (PAM)**, by contrast, each node $u$ represents **only a single palindrome of length $\text{len}(u)$**, and the lengths along a Fail-Tree path have **gaps** ($\text{len}(\text{fail}(u))$ can be much smaller than $\text{len}(u) - 1$). If a splay in an LCT over the PAM Fail Tree contains $k$ nodes $u_1, \dots, u_k$ sharing the same last-occurrence right endpoint $t$, their start positions $\{t - \text{len}(u_j) + 1\}_{j=1}^k$ are **not** a contiguous interval of integers!

How do we overcome these gaps in PAM? Remarkably, **periodicity of palindromic suffixes (`slink` arithmetic progressions) solves the problem even more cleanly than LCT**, and also unlocks **online** $O((N + Q) \log^2 N)$ and $O(N \log N + Q \log N)$ algorithms! Let us derive both the **Periodic AP Telescoping Cancellation Method** (`[国家集训队论文 2014 — 徐毅]`) and the **LCT + Heavy-Path / Subtree-Max Method**.

---

### 75.2 Step 2 — The Combinatorial Word Invariant

#### Invariant 75.2.1: Latest-Occurrence Start-Position Reduction

Fix the right endpoint $r \in [1, N]$. For every non-empty PAM node $u$ that has appeared in $S[1..r]$, define:
- $\text{last}_r(u) = \max \{ p \le r : u \text{ is a suffix of } S[1..p] \}$ (the latest right endpoint of $u$ at or before $r$),
- $\text{start}_r(u) = \text{last}_r(u) - \text{len}(u) + 1$ (the left endpoint of that latest occurrence of $u$).

Because every occurrence of $u$ ending $\le r$ has length $\text{len}(u)$, $u$ has at least one occurrence inside $[l, r]$ if and only if its **latest** occurrence ending $\le r$ starts at or after $l$:
$$u \text{ occurs in } S[l..r] \iff \text{start}_r(u) \ge l.$$
Thus, if we maintain a 1D point-sum data structure (a Fenwick Tree for offline queries, or a Persistent Segment Tree for online queries) storing $+1$ at index $\text{start}_r(u)$ for every active PAM node $u$ at step $r$, then the number of distinct palindromes in $S[l..r]$ is simply the **range sum over $[l, r]$** at version $r$!

When we advance from $r - 1 \to r$, which nodes $u$ have their $\text{last}_r(u)$ updated to $r$?
Precisely the ancestors of $\text{pos}[r]$ in the PAM Fail Tree!
In the worst case ($S = \texttt{a}^N$), $\text{pos}[r]$ has $\Theta(r)$ ancestors in the Fail Tree. Updating $\text{start}_r(u)$ one by one takes $\Theta(N^2)$.

---

#### Invariant 75.2.2: The Periodic Suffix Telescoping Cancellation Theorem (`slink` AP Chains)

Let us partition the Fail-Tree path from $\text{pos}[r]$ to the root into $O(\log r)$ maximal **arithmetic progression (`slink`) chains**.
Consider a single `slink` chain on the path from $\text{pos}[r]$:
$$u_1 \xrightarrow{\text{fail}} u_2 \xrightarrow{\text{fail}} \dots \xrightarrow{\text{fail}} u_k,$$
where $u_1$ is the longest palindrome in the chain, $u_k = \text{slink}(u_1)$ (or the last node with the same difference $d$), and for every $j \in \{1, 2, \dots, k-1\}$:
$$\text{len}(u_j) - \text{len}(u_{j+1}) = d, \quad \text{with } \text{len}(u_2) \ge \frac{1}{2}\text{len}(u_1) \iff d \le \frac{1}{2}\text{len}(u_1).$$

**Theorem (Deterministic Previous Occurrence of Non-Top AP Nodes)**:
At step $r$, before we update $\text{last}(u) \leftarrow r$ for the nodes on the path from $\text{pos}[r]$, what was the previous latest right endpoint $\text{last}_{r-1}(u_j)$ for every **non-initial** node $u_j$ ($j \in \{2, 3, \dots, k\}$) in the chain?
$$\forall j \in \{2, 3, \dots, k\}: \quad \text{last}_{r-1}(u_j) = r - d!$$

**Proof (Double-Overlap & Border Minimality)**:
1. **Existence at $r - d$**: Since $u_1$ ends at $r$ and is a palindrome of length $\text{len}(u_1)$, and $u_j$ ($j \ge 2$) is a proper border of $u_1$ of length $\text{len}(u_1) - (j-1)d$, the palindrome $u_2 = S[r - \text{len}(u_1) + 1 .. r - d]$ is the prefix of $u_1$ of length $\text{len}(u_1) - d$, which ends at position $r - d$! Since $u_j$ ($j \ge 2$) is a suffix of $u_2$, $u_j$ **definitely occurs as a suffix of $S[1..r-d]$**. Hence $\text{last}_{r-1}(u_j) \ge r - d$.
2. **Impossibility of Any Occurrence in $(r - d, r)$**: Suppose for contradiction that $u_j$ occurred at some right endpoint $r' \in (r - d, r - 1]$.
   - Because $u_1$ has period $d$ on $S[r - \text{len}(u_1) + 1 .. r]$, shifting the suffix of length $\text{len}(u_j)$ from $r'$ to $r$ or extending via periodicity forces $u_1$ to have period $\gcd(d, r - r') < d$ (or creates a palindromic suffix of $u_1$ ending at $r$ of length $\text{len}(u_1) - (r - r') > \text{len}(u_1) - d = \text{len}(u_2)$), which **contradicts** $u_2 = \text{fail}(u_1)$ being the longest proper palindromic suffix of $u_1$!
   - Therefore, no node $u_j$ ($2 \le j \le k$) can occur anywhere in $(r - d, r - 1]$, proving $\text{last}_{r-1}(u_j) = r - d$!

Now compute the **old** and **new** start positions across the entire chain $\{u_1, u_2, \dots, u_k\}$ at step $r$:
- **Old start positions (at step $r - 1$)**:
  - For $j = 1$ (the chain head $u_1$): $\text{start}_{r-1}(u_1) = \text{last}_{r-1}(u_1) - \text{len}(u_1) + 1$.
  - For $j \in \{2, 3, \dots, k\}$: since $\text{last}_{r-1}(u_j) = r - d$ and $\text{len}(u_j) + d = \text{len}(u_{j-1})$, we have:
    $$\text{start}_{r-1}(u_j) = (r - d) - \text{len}(u_j) + 1 = r - (\text{len}(u_j) + d) + 1 = r - \text{len}(u_{j-1}) + 1!$$
- **New start positions (at step $r$)**:
  - For all $j \in \{1, 2, \dots, k\}$: since $\text{last}_r(u_j) = r$, we have:
    $$\text{start}_r(u_j) = r - \text{len}(u_j) + 1.$$

Compare the two multisets of start positions for $\{u_1, u_2, \dots, u_k\}$:
$$\begin{aligned}
\text{Old Multiset} &= \big\{ \text{last}_{r-1}(u_1) - \text{len}(u_1) + 1, \;\; \cancel{r - \text{len}(u_1) + 1}, \;\; \cancel{r - \text{len}(u_2) + 1}, \;\; \dots, \;\; \cancel{r - \text{len}(u_{k-1}) + 1} \big\}, \\
\text{New Multiset} &= \big\{ \cancel{r - \text{len}(u_1) + 1}, \;\; \cancel{r - \text{len}(u_2) + 1}, \;\; \dots, \;\; \cancel{r - \text{len}(u_{k-1}) + 1}, \;\; r - \text{len}(u_k) + 1 \big\}.
\end{aligned}$$

```
Telescoping Start-Position Cancellation inside One slink Chain {u_1, ..., u_k}:
  u_1 (at r)   starts at r - len(u_1) + 1  <=== CANCELS old u_2 (at r - d)!
  u_2 (at r)   starts at r - len(u_2) + 1  <=== CANCELS old u_3 (at r - d)!
  ...
  u_{k-1}(at r) starts at r - len(u_{k-1})+1 <=== CANCELS old u_k (at r - d)!
  u_k (at r)   starts at r - len(u_k) + 1  <=== ONLY NEW INSERTION (+1)!
  Old u_1 (at last_{r-1}(u_1))             <=== ONLY OLD DELETION (-1)!
```

**Every single internal node in the arithmetic progression cancels out!**
Across the entire chain $\{u_1, \dots, u_k\}$ (which could contain $\Theta(N)$ nodes!):
1. We **decrement ($-1$)** at a single old start position: $\text{last}_{r-1}(u_1) - \text{len}(u_1) + 1$ (if $\text{last}_{r-1}(u_1) > 0$).
2. We **increment ($+1$)** at a single new start position: $r - \text{len}(u_k) + 1$.

How do we know $\text{last}_{r-1}(u_1)$ for the chain head $u_1$?
A PAM node $u_1$ occurred as a palindromic suffix at some earlier position $p < r$ if and only if $\text{pos}[p]$ was in the **Fail-Tree subtree of $u_1$**!
Thus, if we compute the Euler tour DFS intervals $[\text{dfn}[u], \text{out}[u]]$ of the static PAM Fail Tree (built over $S[1..N]$ upfront, or via dynamic/LCT if strictly character-by-character online), then at step $r$:
- $\text{last}_{r-1}(u_1)$ is simply the **range maximum** over $[\text{dfn}[u_1], \text{out}[u_1]]$ in a Segment Tree `MaxEndposTree` where we perform a **single point update** `MaxEndposTree.update(dfn[pos[r]], r)` at the end of step $r$!

---

#### Invariant 75.2.3: Purely Online $O(Q \log N)$ Distinct Palindromes Without Persistent Segment Trees? No — Persistent Segment Tree vs. Online Periodic Inspection

Let us compare the two online architectures:
1. **Online Method 1 — PAM + `slink` Telescoping + Persistent Segment Tree ($O(N \log^2 N)$ time, $O(N \log^2 N)$ space, $O(\log N)$ per query!)**:
   - Build the PAM of $S[1..N]$ and its Fail-Tree Euler tour $[\text{dfn}[u], \text{out}[u]]$.
   - Sweep $r = 1 \dots N$. At each step $r$, walk the $O(\log r)$ `slink` chains from $u = \text{pos}[r]$ up to the root:
     - Let $u_1 = u$, and let $u_k$ be the last node in $u_1$'s `slink` chain (i.e., if we define $\text{slink}[u_1]$ as the first ancestor with $\text{diff} \ne \text{diff}(u_1)$, then $u_k$ is the child of $\text{slink}[u_1]$ on the chain, so $\text{len}(u_k) = \text{len}(\text{slink}[u_1]) + \text{diff}(u_1)$!).
     - Query $p_{\text{old}} = \text{MaxEndposTree.query}(\text{dfn}[u_1], \text{out}[u_1])$.
     - If $p_{\text{old}} > 0$, apply `-1` at index $p_{\text{old}} - \text{len}(u_1) + 1$ in the Persistent Segment Tree.
     - Apply `+1` at index $r - \text{len}(u_k) + 1$ in the Persistent Segment Tree.
     - Advance $u \leftarrow \text{slink}[u_1]$.
   - Update `MaxEndposTree.update(dfn[pos[r]], r)`.
   - Save the root of the Persistent Segment Tree after step $r$ as `root[r]`.
   - **Query $(l, r)$**: Return `PersistentSegTree.query(root[r], l, r)` in **$O(\log N)$ worst-case time per query**!
2. **Online Method 2 — Offline Fenwick Sweep ($O(N \log^2 N + Q \log N)$ time, $O(N)$ space)**:
   - Identical to Method 1, replacing the Persistent Segment Tree with a flat Fenwick Tree `BIT` of size $N$, answering offline queries $(l, r)$ sorted by $r$ in $O(\log N)$ time and $O(N)$ memory.
3. **Alternative Coupling — PAM Fail Tree + LCT `access` Color-Chain Sweep**:
   - If one uses LCT `access(pos[r])` instead of `slink` chains, each solid splay represents a vertical path in the PAM Fail Tree that was last visited together at some right endpoint $t$.
   - Why is `slink` strictly superior to LCT on PAM? Because a vertical path in the PAM Fail Tree is ALREADY partitioned into $O(\log N)$ `slink` chains, and within each `slink` chain the telescoping cancellation holds automatically without needing any splay rotations or dynamic tree auxiliary structures!

---

### 75.3 Step 3 — The Reverse-Engineering Scratchpad (Exact `slink` Indexing Contract)

There is one crucial indexing detail in the `slink` definition that trips up many competitors:
In standard `slink` DP (Wave 1A), we define:
$$\text{diff}[u] = \text{len}[u] - \text{len}[\text{fail}[u]], \qquad \text{slink}[u] = \begin{cases} \text{slink}[\text{fail}[u]], & \text{if } \text{diff}[u] == \text{diff}[\text{fail}[u]], \\ \text{fail}[u], & \text{otherwise.} \end{cases}$$
Under this standard definition:
- What is the **shortest** node $u_k$ in $u_1$'s arithmetic progression chain $\{u_1, u_2, \dots, u_k\}$ that gets its old occurrence cancelled by $u_{k-1}$?
- Notice that in our proof of Invariant 75.2.2, we used the fact that for $j \in \{2, \dots, k\}$, $\text{len}(u_{j-1}) - \text{len}(u_j) = d$, where $d = \text{diff}[u_1]$.
- For $j = k$, we only needed $\text{len}(u_{k-1}) - \text{len}(u_k) = d$! We did **NOT** need $\text{diff}[u_k] = d$!
- Wait: under the standard definition of $\text{slink}[u_1]$, the node $v = \text{slink}[u_1]$ is the **first ancestor of $u_1$ whose own $\text{diff}[v] \ne d$**, which means the step from the node *just below $v$* to $v$ **still has difference $d$**!
- Wait—let's check! If $\text{diff}[u_{k-1}] = d$ and $\text{fail}[u_{k-1}] = v$, then by definition $\text{len}[u_{k-1}] - \text{len}[v] = \text{diff}[u_{k-1}] = d$!
- Can $v$ be the even root $r_0$ ($\text{len}[r_0] = 0$)? No, if $v = r_0$, then $u_k$ would be the empty palindrome, which we should NOT count as a non-empty palindrome!
- Let's verify on a concrete example! Suppose $u_1 = \texttt{"aaaa"}$ ($\text{len} = 4$), $u_2 = \texttt{"aaa"}$ ($\text{len} = 3$), $u_3 = \texttt{"aa"}$ ($\text{len} = 2$), $u_4 = \texttt{"a"}$ ($\text{len} = 1$), $r_0 = \varepsilon$ ($\text{len} = 0$).
  - $\text{diff}[u_1] = 4 - 3 = 1$.
  - $\text{diff}[u_2] = 3 - 2 = 1$.
  - $\text{diff}[u_3] = 2 - 1 = 1$.
  - $\text{diff}[u_4] = 1 - 0 = 1$.
  - $\text{diff}[r_0] = 0 - (-1) = 1$ (if we aren't careful!) or undefined!
  - **CRITICAL**: To prevent `slink` from merging $u_4 = \texttt{"a"}$ with the roots $r_0, r_1$, we **must** define:
    - $\text{diff}[r_0] = \text{diff}[r_1] = 0$ (or stop `slink` at $r_0$), and for any node $u$ with $\text{fail}[u] = r_0$ ($\text{len}[u] = 1$ or $\text{fail}[u] = 0$), $\text{diff}[u] = \text{len}[u] - 0 = \text{len}[u]$, while $\text{slink}[u] = r_0$!
  - Let's trace $\texttt{"aaaa"}$ with $\text{slink}[u_4] = r_0$:
    - For $u_4 = \texttt{"a"}$ ($\text{len} = 1$, $\text{fail} = r_0$): $\text{diff}[u_4] = 1$, $\text{slink}[u_4] = r_0$.
    - Then for $u_3, u_2, u_1$: since $\text{diff} = 1 = \text{diff}[u_4]$, they all get $\text{slink}[u_1] = \text{slink}[u_4] = r_0$.
    - Now, in the chain $\{u_1, u_2, u_3, u_4\}$ (lengths $4, 3, 2, 1$), what is the shortest non-empty node $u_k$ in the chain? It is $u_4$ of length $1 = \text{len}[\text{slink}[u_1]] + \text{diff}[u_1] = 0 + 1 = 1$!
  - What if the chain does NOT reach $r_0$, e.g., $S = \texttt{ababa}$, $u_1 = \texttt{"ababa"}$ ($\text{len} = 5$), $u_2 = \texttt{"aba"}$ ($\text{len} = 3$), $u_3 = \texttt{"a"}$ ($\text{len} = 1$)?
    - $\text{diff}[u_1] = 5 - 3 = 2$.
    - $\text{diff}[u_2] = 3 - 1 = 2$.
    - $\text{diff}[u_3] = 1 - 0 = 1 \ne 2$!
    - So $\text{slink}[u_2] = \text{fail}[u_2] = u_3$, and $\text{slink}[u_1] = \text{slink}[u_2] = u_3$!
    - Look closely at $\{u_1, u_2\}$ vs $u_3$:
      - Is $u_3 = \texttt{"a"}$ at distance $d = 2$ below $u_2$? YES ($\text{len}[u_2] - \text{len}[u_3] = 3 - 1 = 2$), so $u_3$ **also** occurred at $r - 2$ as a prefix-suffix of $u_1$!
      - HOWEVER, if we jump $u \leftarrow \text{slink}[u_1] = u_3$ in our loop, then $u_3$ will be processed as the **chain head of the NEXT `slink` chain**!
      - Read that twice! Because the loop transitions $u \leftarrow \text{slink}[u_1]$, the node $\text{slink}[u_1]$ is the **first node of the next chain**, which means the current chain $\{u_1, \dots, u_k\}$ must stop at the **child of $\text{slink}[u_1]$** (which has length $\text{len}[\text{slink}[u_1]] + \text{diff}[u_1]$)!
      - Let's verify this on $u_1 = \texttt{"ababa"}$ ($\text{len}=5$), $u_2 = \texttt{"aba"}$ ($\text{len}=3$), $u_3 = \texttt{"a"}$ ($\text{len}=1$) at $r = 5$:
        - **Chain 1**: $u_1 = \texttt{"ababa"}$ ($\text{len}=5$), $\text{diff}[u_1] = 2$, $\text{slink}[u_1] = u_3$ ($\text{len}=1$).
          - The nodes processed in Chain 1 are $\{u_1, u_2\}$ (lengths $5$ and $3$).
          - The shortest node in Chain 1 has length $\text{len}[\text{slink}[u_1]] + \text{diff}[u_1] = 1 + 2 = 3$ ($\text{len}(u_2)$)!
          - Chain 1 removes $\text{start}_{r-1}(u_1)$ (none, since $u_1$ is new) and inserts $r - \text{len}(u_2) + 1 = 5 - 3 + 1 = 3$ (while $u_2$'s old start position $(5-2) - 3 + 1 = 1$ cancels with $u_1$'s new start position $5 - 5 + 1 = 1$!).
        - **Chain 2**: $u = u_3 = \texttt{"a"}$ ($\text{len}=1$), $\text{diff}[u_3] = 1$, $\text{slink}[u_3] = r_0$ ($\text{len}=0$).
          - Chain 2 removes $\text{start}_{r-1}(u_3) = 3 - 1 + 1 = 3$ and inserts $r - (\text{len}[r_0] + \text{diff}[u_3]) + 1 = 5 - 1 + 1 = 5$!
        - Notice how Chain 1 inserted $3$ and Chain 2 removed $3$, leaving net active start positions $\{1, 1, 5\}$ for $\texttt{"ababa"}, \texttt{"aba"}, \texttt{"a"}$ at $r = 5$—**100% exact!**

```cpp
// Non-standard PAM slink Telescoping Start-Position Sweep for Range Distinct Palindromes
// For each step r = 1 .. N:
for (int u = pos[r]; u > 1; u = slink[u]) {
    int prev_r = MaxEndposSegTree.query(dfn[u], out[u]);
    if (prev_r > 0) {
        int old_start = prev_r - len[u] + 1;
        StartPosFenwick.add(old_start, -1);
    }
    int shortest_len_in_chain = len[slink[u]] + diff[u];
    int new_start = r - shortest_len_in_chain + 1;
    StartPosFenwick.add(new_start, +1);
}
MaxEndposSegTree.update(dfn[pos[r]], r);
// Now for any query [l, r], distinct palindromes in S[l..r] == StartPosFenwick.query(l, r)!
```

Look at those 10 lines of code above. That is one of the most elegant reductions in all of competitive stringology: **zero LCT, zero heavy-light decomposition, just a 10-line `slink` loop** that updates at most $\log_2 N$ pairs of start positions per character!

---

### 75.4 Step 4 — Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Broken Invariant 1 — Storing a Scalar `last[u]` per Node Instead of Subtree Max in the Fail Tree**:
   - *Why it fails*: In the `slink` loop above, we only visit the **chain heads** $u = \text{pos}[r], \text{slink}[\text{pos}[r]], \dots$ and we only update `MaxEndposSegTree` at the single node $\text{pos}[r]$.
   - Suppose at step $r' < r$, $\text{pos}[r']$ was a descendant $w$ of $u$ that belonged to the *middle* of a `slink` chain (or a proper subtree of $u$). Then $u$ occurred at $r'$ even though $u$ was not equal to $\text{pos}[r']$ (or even if $u$ was skipped over inside another `slink` chain at step $r'$)!
   - Therefore, a scalar array `last[u]` updated only at visited chain heads will **miss** occurrences of $u$ induced by proper descendants in the Fail Tree! Querying `MaxEndposSegTree.query(dfn[u], out[u])` over $u$'s Fail-Tree subtree is mandatory and exact.
2. **Broken Invariant 2 — Inserting $\text{len}[\text{slink}[u]]$ Instead of $\text{len}[\text{slink}[u]] + \text{diff}[u]$**:
   - Because $\text{slink}[u]$ is the head of the *next* chain processed in the next iteration of the `for` loop, the current chain's bottom node is the node one step *below* $\text{slink}[u]$ in the AP, which has length $\text{len}[\text{slink}[u]] + \text{diff}[u]$. Using $\text{len}[\text{slink}[u]]$ double-counts the transition at $\text{slink}[u]$ and omits the bottom of the current chain.

---

## Iteration 76: Combinatorics of Palindromes, Rich Words, Unique Palindromic Factorization, $\theta$-Palindromes, and Inverse String Reconstruction

### 76.1 Step 1 — The Diagnostic Signal

This iteration addresses two major structural families that frequently appear in ICPC, AtCoder (`AGC`/`ARC`), Codeforces Div1, and Olympiads:
1. **Combinatorics of Palindromes & Extremal Palindromic Density**:
   - How many distinct palindromes can a string $S$ of length $N$ contain, and which strings achieve this upper bound (**Rich Words**)?
   - How do we adapt palindromic structures when "palindrome" is generalized by an **involutive morphism** $\theta$ ($w = \theta(w^R)$, such as DNA Watson–Crick complement $A \leftrightarrow T, C \leftrightarrow G$ or binary bitwise negation $0 \leftrightarrow 1$)?
   - When can a string be uniquely or minimally factored into palindromes (**Palindromic Length**)?
2. **Inverse String Reconstruction (Array Restoration)**:
   - Given an integer array (a proposed KMP prefix function $\pi[1..N]$, Z-array $Z[1..N]$, or Manacher radius array $\text{rad}[1..2N-1]$), determine whether a valid string $S$ generating that exact array exists, reconstruct the lexicographically smallest such string, or count how many strings over an alphabet of size $\sigma$ produce it.
   - Naive reconstruction adds $O(N^2)$ character equality constraints ($S[i] = S[j]$) and inequality constraints ($S[i] \ne S[j]$). Why do the internal invariants of KMP, Z, and Manacher compress these $O(N^2)$ constraints down to at most $O(N)$ active edges?

---

### 76.2 Step 2 — The Combinatorial Word Invariant

#### Invariant 76.2.1: The Droubay–Pirillo Theorem (2001) & Characterizations of Rich Words

**Theorem (Droubay, Justin & Pirillo 2001)**:
Any finite word $S$ of length $N$ contains at most $N + 1$ distinct palindromic factors (including the empty word $\varepsilon$, or at most $N$ non-empty distinct palindromic factors).

**Zero-Magic Proof (Right-Extension Uniqueness)**:
Consider appending $S[r]$ to $S[1..r-1]$. Any new palindromic factor of $S[1..r]$ that did not occur in $S[1..r-1]$ must end at position $r$ (i.e., be a palindromic suffix of $S[1..r]$).
Let $P = S[l..r]$ be the **longest** palindromic suffix of $S[1..r]$, and let $Q = S[l'..r]$ ($l' > l$) be any **shorter** palindromic suffix of $S[1..r]$.
Because $Q$ is a suffix of the palindrome $P$, reflecting $Q$ across the center of $P$ maps $Q = S[l'..r]$ to an identical prefix of $P$:
$$Q = Q^R = S[l .. l + |Q| - 1].$$
Since $|Q| < |P| = r - l + 1$, the right endpoint of this reflected copy is $l + |Q| - 1 \le r - 1$.
Thus **$Q$ already occurred inside $S[1..r-1]$**!
Consequently, only the single longest palindromic suffix $P$ can be new at step $r$. Summing over $r = 1 \dots N$ plus $\varepsilon$ yields at most $N + 1$ distinct palindromes. $\blacksquare$

**Definition & Equivalent Characterizations of Rich Words (Glen, Justin, Widmer & Zamboni 2009)**:
A word $S$ of length $N$ is called **rich** (or **full**) if it achieves the upper bound of $N + 1$ distinct palindromic factors (equivalently, every prefix $S[1..r]$ creates a brand-new node in the PAM!).
A word $w$ is called a **complete return** to a factor $u$ if $w$ starts with $u$, ends with $u$, and contains exactly two occurrences of $u$ ($u$ occurs only as a prefix and as a suffix of $w$).

**Theorem (The Three Characterizations of Rich Words)**:
For any finite word $S$, the following are equivalent:
1. **$S$ is rich**: $S$ contains exactly $|S| + 1$ distinct palindromic factors (every step $r \in [1..|S|]$ creates a new PAM node).
2. **Longest Palindromic Suffix Unioccurrence**: For every prefix $S[1..r]$, its longest palindromic suffix occurs **exactly once** in $S[1..r]$ (i.e., is unioccurrent in $S[1..r]$).
3. **Palindromic Complete Returns**: For **every** palindromic factor $u$ of $S$, every complete return to $u$ in $S$ is itself a **palindrome**!

**Why Characterization 3 is true and powerful in contests**:
Suppose $w$ is a complete return to a palindrome $u$ inside $S$, spanning $S[l..r]$ where $u$ is a prefix and suffix of $w$ and does not occur internally in $w$. When the PAM processes position $r$, what is the longest palindromic suffix $P$ of $S[1..r]$?
- If $w$ is NOT a palindrome, let $P$ be the longest palindromic suffix of $w$ (or of $S[1..r]$). If $|P| < |w|$, then inside $P$, $u$ cannot occur internally, so $P = u$, meaning the longest palindromic suffix at $r$ is $u$—which **already occurred** at the start of $w$, so step $r$ fails to create a new palindrome!
- Conversely, if $S$ is rich, at the second occurrence of $u$ in any complete return $w = S[l..r]$, the longest palindromic suffix $P$ at step $r$ must be **strictly longer** than $u$ (since $u$ is not new!). By palindrome reflection, $u^R = u$ occurs at the prefix of $P$; since $w$ is the *shortest* return to $u$ ending at $r$, $P$ must have length $\ge |w|$, forcing $w$ itself to be a palindrome!
- *Examples of Rich Words*: All **Sturmian words** (including Fibonacci words), all words over a binary alphabet avoiding certain non-palindromic returns, all prefixes of the Episturmian / Tribonacci words, and any word of the form $a^{k_1} b^{k_2} a^{k_3}$ (at most 3 runs of 2 distinct letters).

---

#### Invariant 76.2.2: Watson–Crick / Antisymmetric ($\theta$-) Palindromes

Let $\theta : \Sigma \to \Sigma$ be an **involution** on the alphabet ($\theta(\theta(c)) = c$ for all $c \in \Sigma$). Extend $\theta$ to an **antimorphic involution** on $\Sigma^*$ by reversing the string and applying $\theta$ character-wise:
$$\theta(s_1 s_2 \dots s_k) = \theta(s_k) \theta(s_{k-1}) \dots \theta(s_1).$$
A string $w$ is a **$\theta$-palindrome** if $w = \theta(w)$, i.e., $w[i] = \theta(w[|w| - i + 1])$ for all $1 \le i \le |w|$.

**Structural Properties of $\theta$-Palindromes**:
1. **Center Parity Rule**: If $|w| = 2k + 1$ is odd, the middle character $w[k+1]$ must satisfy $w[k+1] = \theta(w[k+1])$.
   - In **fixed-point-free involutions** (such as DNA Watson–Crick $A \leftrightarrow T, C \leftrightarrow G$, or binary complement $0 \leftrightarrow 1$), $\theta(c) \ne c$ for all $c \in \Sigma$. Therefore, **every $\theta$-palindrome has even length**!
2. **Closed Under Reflection of Borders**: If $u$ is a $\theta$-palindromic suffix of a $\theta$-palindrome $P$, then $u = \theta(u)$ and $P = \theta(P)$ imply that the prefix of $P$ of length $|u|$ is $\theta(u) = u$!
   - Therefore, **all theorems of standard palindromes—including the Droubay–Pirillo bound, PAM construction, Fail Tree, `slink` arithmetic progressions, and `quick_link`—hold verbatim for $\theta$-palindromes**!
3. **Exact PAM Adaptation for $\theta$-Palindromes**:
   - In the extension check at position $r$, replace `S[r - len[u] - 1] == S[r]` with:
     $$S[r - \text{len}(u) - 1] == \theta(S[r]).$$
   - If $\theta$ has no fixed points, disable transitions out of the odd root $r_1$ (only even-length $\theta$-palindromes extending $r_0$ exist). If $\theta$ has both fixed points ($\theta(c) = c$) and 2-cycles ($\theta(a) = b$), only allow `next[r_1][c]` for characters $c$ with $\theta(c) = c$!

---

#### Invariant 76.2.3: Inverse String Reconstruction — Why KMP, Z, and Manacher Encode $O(N)$ Constraints

Suppose we are given a candidate array ($\pi[1..N]$, $Z[1..N]$, or Manacher radii $\text{rad}[1..2N-1]$) and must verify whether a valid string $S[1..N]$ exists, or count/construct valid strings.

**The Naive $O(N^2)$ Trap**:
A border $\pi[i] = L$ implies $S[1..L] = S[i-L+1..i]$ ($L$ character equalities), and $S[L+1] \ne S[i+1]$? Wait: $\pi[i]$ is the longest proper border of $S[1..i]$, so for *every* candidate border length $L' > \pi[i]$ that was a border of $S[1..i-1]$ extended by $1$, we must have $S[L'] \ne S[i]$!

**The $O(N)$ Amortized Constraint Extraction Theorem**:
1. **Reconstructing from KMP $\pi[1..N]$**:
   Simulate the exact KMP algorithm on the unknown string $S[1..N]$:
   - Require $\pi[1] = 0$. Assign $S[1]$ the first alphabet character $c_1$.
   - For each $i = 2 \dots N$:
     - First check the coarse bound: $0 \le \pi[i] \le \pi[i-1] + 1$. (If violated, the array is **INVALID**.)
     - Walk the KMP fail chain starting from $k = \pi[i-1]$:
       - While $k > 0$ and $k + 1 \ne \pi[i]$:
         - For the real KMP algorithm to fail at $k$ and not stop at $k + 1$ (if $k + 1 > \pi[i]$), we **must** have $S[i] \ne S[k + 1]$! Record $S[k + 1]$ in a `forbidden` set for position $i$, and step $k \leftarrow \pi[k]$.
       - When the loop terminates:
         - **Case 1 ($\pi[i] > 0$)**: We **must** have stopped at a valid ancestor $k$ with $k + 1 = \pi[i]$! If $k + 1 \ne \pi[i]$, it means $\pi[i] - 1$ was **not** an ancestor of $\pi[i-1]$ in the KMP fail tree, so $\pi[1..N]$ is **INVALID**!
           Otherwise ($k + 1 = \pi[i]$), KMP matched at $k$, which forces the single equality $S[i] = S[\pi[i]]$.
           Now check: was $S[\pi[i]]$ already placed into the `forbidden` set during the walk above (meaning some longer ancestor $k' > k$ also had $S[k' + 1] = S[\pi[i]]$)?
           - If $S[\pi[i]] \in \text{forbidden}$, then $S[i] = S[\pi[i]] = S[k'+1]$ would have caused KMP to stop earlier at $k' + 1 > \pi[i]$! Thus the array is **INVALID**!
         - **Case 2 ($\pi[i] == 0$)**: The walk reached $k = 0$, and since KMP did not even match at $k = 0$, we must also forbid $S[1]$ ($S[i] \ne S[1]$). We can then choose $S[i]$ to be the smallest character in $\Sigma \setminus \text{forbidden}$ (or notice there are $|\Sigma| - |\text{forbidden}|$ valid choices for $S[i]$, because all prefixes $\le i-1$ are already fully determined!).
   - **Why is this 100% necessary and sufficient in $O(N)$ time?**
     Because by induction on $i-1$, $S[1..i-1]$ already realizes $\pi[1..i-1]$; at step $i$, KMP on $S[1..i]$ tests the exact sequence of characters $S[k+1]$ along the fail chain of $\pi[i-1]$ and stops at the first match!
2. **Reconstructing from Z-Array $Z[1..N]$**:
   - Rather than maintaining intervals directly on $Z$, use the linear-time $Z \leftrightarrow \pi$ equivalence or the Z-box $[L, R]$ sweep:
   - As we sweep $i = 2 \dots N$ maintaining the rightmost Z-box $[L, R]$:
     - If $i \le R$, let $k = i - L + 1$. In standard Z-algorithm, $Z[i]$ is compared against $\min(Z[k], R - i + 1)$:
       - If $Z[k] < R - i + 1$, then we **must** have $Z[i] == Z[k]$! (If $Z[i] \ne Z[k]$, the Z-array is immediately **INVALID**!)
       - If $Z[k] > R - i + 1$, then we **must** have $Z[i] == R - i + 1$! (If $Z[i] \ne R - i + 1$, **INVALID**!)
       - If $Z[k] == R - i + 1$ (or $i > R$), then $Z[i]$ must satisfy $Z[i] \ge \max(0, R - i + 1)$ (and $i + Z[i] - 1 \le N$). The characters from $\max(i, R+1)$ to $i + Z[i] - 1$ are newly matched against $S[1 + \dots]$, forcing $S[p] = S[p - i + 1]$ in $O(1)$ amortized work as $R$ advances! Finally, if $i + Z[i] \le N$, the mismatch at the end of the Z-box adds a single inequality edge:
         $$S[i + Z[i]] \ne S[1 + Z[i]].$$
3. **Reconstructing from Manacher Radii $\text{rad}_{\text{odd}}[1..N]$ and $\text{rad}_{\text{even}}[1..N-1]$**:
   - Exactly mirrors the Z-box sweep! Maintain the rightmost palindrome $[L, R]$ centered at $C$.
   - For each new center $c$, its mirror $c' = 2C - c$ inside $[L, R]$ forces:
     - If $\text{rad}[c'] < R - c + 1 \implies$ we must have $\text{rad}[c] == \text{rad}[c']$.
     - If $\text{rad}[c'] > R - c + 1 \implies$ we must have $\text{rad}[c] == R - c + 1$.
     - If $\text{rad}[c'] == R - c + 1$ (or $c > R$) $\implies$ we must have $\text{rad}[c] \ge \max(1, R - c + 1)$, every new position $p \in (R,\; c + \text{rad}[c] - 1]$ is forced equal to its mirror $S[p] = S[2c - p]$, and if the boundary $c - \text{rad}[c] \ge 1$ and $c + \text{rad}[c] \le N$, we add the single inequality constraint:
       $$S[c + \text{rad}[c]] \ne S[c - \text{rad}[c]].$$
   - Because each new character equality advances $R$, the entire equality + inequality graph has at most $N$ vertices, forms a forest of equality components (where each component root is determined at its leftmost index!), and has at most $2N$ directed inequality edges from smaller indices to the first undetermined index $p = c + \text{rad}[c]$!

---

### 76.3 Step 3 — The Reverse-Engineering Scratchpad (Counting Valid Strings from $\pi$ or Manacher)

Because in all three restoration algorithms (KMP $\pi$, Z-array, and Manacher radii), every forced equality $S[p] = S[q]$ always equates the **newly reached rightmost position $p$** to a **strictly earlier position $q < p$**, and every inequality $S[p] \ne S[q]$ also compares a position $p$ against strictly earlier positions $q < p$ (once mapped to their earliest component representative $\text{rep}[q] \le q$):

**Theorem (Product Formula for Valid String Counting)**:
When a candidate KMP $\pi$-array, Z-array, or Manacher radius array is valid:
- Partition $[1..N]$ into equality components via the $O(N)$ forced equalities, where each component $C$ is represented by its minimum index $i = \min(C)$.
- For each component root $i$, collect the set of distinct earlier component roots:
  $$\text{Forb}(i) = \{ \text{rep}[q] : \{i, q\} \text{ is a forced inequality edge with } \text{rep}[q] < i \}.$$
  (If any inequality edge has $\text{rep}[i] == \text{rep}[q]$, the array is **INVALID** and the count is $0$.)
- Note that inside KMP restoration, every inequality at a newly free position $i$ ($\pi[i] = 0$) is between $i$ and $S[k+1]$ along the fail chain of $\pi[i-1]$. Even better, in KMP / Manacher where every inequality is between $p$ and characters already fully determined to the left of $p$, all elements of $\text{Forb}(i)$ have **distinct characters** in any valid assignment (Wait: in KMP, could two forbidden positions $k_1 + 1$ and $k_2 + 1$ on the fail chain of $\pi[i-1]$ have the *same* character? No! If $S[k_1+1] == S[k_2+1]$ with $k_1 > k_2$, then when $i$ was not even reached, wait—two ancestors $k_1 > k_2$ of $\pi[i-1]$ *can* have $S[k_1+1] == S[k_2+1]$! That's why we take the set of distinct characters or distinct component representatives!).
- Specifically, for KMP $\pi[1..N]$: whenever $\pi[i] > 0$, $S[i]$ is uniquely forced to equal $S[\pi[i]]$ ($1$ choice); whenever $\pi[i] == 0$, $S[i]$ must avoid the set of characters $\{S[k+1] : k \text{ visited on fail chain of } \pi[i-1]\} \cup \{S[1]\}$. Since for any valid assignment, two indices $a, b < i$ are in the same equality class if and only if they have the same $\text{rep}$ (because $\pi$ completely determines which indices must be equal and which must be distinct along fail chains!), the number of distinct forbidden values at step $i$ ($\pi[i]=0$) is simply $d_i = |\{ \text{rep}[k+1] : k \text{ on fail chain of } \pi[i-1] \} \cup \{\text{rep}[1]\}|$, and the total number of valid strings over an alphabet of size $\sigma$ is the exact product:
  $$\text{ValidStrings}(\pi, \sigma) = \prod_{\substack{i=1 \\ \pi[i] = 0}}^{N} \max(0,\; \sigma - d_i)!$$
  (For $i = 1$, $d_1 = 0$, giving $\sigma$ choices; for $i > 1$ with $\pi[i] = 0$, $d_i$ is the number of distinct component representatives among the fail-chain transitions out of $\pi[i-1]$.)

---

### 76.4 Step 4 — Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Broken Invariant 1 — Assuming $\pi[i] \le \pi[i-1] + 1$ Is Sufficient for KMP Validity**:
   - *Counterexample A (Missing Fail-Ancestor)*: $\pi = [0, 0, 1, 1, 2, 3]$ vs $\pi = [0, 1, 0, 1, 2, 2]$? Take $\pi = [0, 0, 1, 0, 2]$: here $\pi[4] = 0$, so $\pi[5] \le \pi[4] + 1 = 1$, which already fails. What about $\pi = [0, 1, 0, 2]$? Fails $\pi[4] \le \pi[3] + 1$.
   - Now take $\pi = [0, 1, 0, 1, 2, 2]$:
     - $i=1: \pi[1]=0 \implies S[1]=\texttt{a}$.
     - $i=2: \pi[2]=1 \implies S[2]=S[1]=\texttt{a}$.
     - $i=3: \pi[3]=0 \implies S[3] \ne S[2], S[1] \implies S[3]=\texttt{b}$. ($S = \texttt{aab}$).
     - $i=4: \pi[4]=1 \implies S[4]=S[1]=\texttt{a}$. ($S = \texttt{aaba}$).
     - $i=5: \pi[5]=2 \implies S[5]=S[2]=\texttt{a}$. ($S = \texttt{aabaa}$).
     - $i=6$: What is $\pi[5]$? $\pi[5] = 2$, and $\pi[2] = 1$, $\pi[1] = 0$. So $\pi[6] = 2 \le \pi[5] + 1 = 3$ satisfies both the $+1$ bound AND the fail-ancestor condition ($2 - 1 = 1 = \pi[\pi[5]]$)!
     - **Yet $\pi = [0, 1, 0, 1, 2, 2]$ is INVALID!** Why?
       At $i = 6$, walking from $k = \pi[5] = 2$:
       - Since $k + 1 = 3 \ne \pi[6] = 2$, we must fail at $k = 2$, which forces $S[6] \ne S[2 + 1] = S[3] = \texttt{b}$.
       - Wait: $S[3] = \texttt{b}$, and at $k = \pi[2] = 1$, $k + 1 = 2 = \pi[6]$ forces $S[6] = S[2] = \texttt{a}$! That succeeds ($\texttt{aabaab}$ vs $\texttt{aabaaa}$: in $\texttt{aabaaa}$, $\pi[6] = 2$!).
       - Now change $\pi[5]$ and $\pi[6]$: take $S[1..4] = \texttt{aaba}$ ($\pi = [0, 1, 0, 1]$), and ask for $\pi[5] = 1$!
       - Check $\pi = [0, 1, 0, 1, 1]$:
         - Coarse bound: $\pi[5] = 1 \le \pi[4] + 1 = 2$ (holds!).
         - Fail-ancestor condition: $\pi[5] - 1 = 0 = \pi[\pi[4]] = \pi[1]$ (holds!).
         - **Why is $\pi = [0, 1, 0, 1, 1]$ INVALID over every alphabet?**
           At $i = 5$, we start at $k = \pi[4] = 1$. Since $k + 1 = 2 > \pi[5] = 1$, we must fail at $k = 1$, forcing $S[5] \ne S[1 + 1] = S[2] = \texttt{a}$.
           Next we step to $k = \pi[1] = 0$, where $k + 1 = 1 = \pi[5]$, forcing $S[5] = S[1] = \texttt{a}$!
           Thus we simultaneously require $S[5] \ne \texttt{a}$ and $S[5] = \texttt{a}$—**an impossible contradiction!**
   - Always remember $\pi = [0, 1, 0, 1, 1]$ as the canonical 5-element counterexample proving that fail-chain forbidden-character tracking is mandatory!
2. **Broken Invariant 2 — Forgetting that Even Manacher Centers Can Force Contradictions Without Odd Radii Changing**:
   - When restoring a string from Manacher's odd and even radii simultaneously, the unified `#`-string $T[1..2N+1]$ must have $T[2i-1] = \texttt{\#}$ for all $i$. In the Manacher sweep on $T$, a radius $\text{rad}_T[p]$ at $p$ must have the **exact parity** so that the last matched characters inside the palindrome are the $\texttt{\#}$ symbols! Specifically, $p + \text{rad}_T[p] - 1$ must be **odd** (a $\texttt{\#}$ position), meaning $\text{rad}_T[p]$ and $p$ must have **even sum** ($p \equiv \text{rad}_T[p] \pmod 2$)! If any input radius violates this parity, the Manacher array is immediately invalid.

---

## Iteration 77: Multilingual (`[EN]`/`[ZH]`/`[JA]`) Problem Mining, 4-Tier Difficulty Ladder & Template Quarantine Ledger

In accordance with `PLAN.md` (§2), we curate **32 non-template competitive programming problems** across English (`[EN]`: Codeforces, ICPC World Finals/Regionals, Universal Cup, SPOJ/CodeChef), Chinese (`[ZH]`: NOI/WC/CTSC/ZJOI/SDOI/SHOI/JSOI, Luogu, UOJ, LOJ, BZOJ, HDU, QOJ), and Japanese (`[JA]`: AtCoder `AGC`/`ARC`/`ABC`, JOI, yukicoder) organized into a **4-Tier Smooth Difficulty Ladder** (`Stepping Stone` $\to$ `Intermediate` $\to$ `Advanced` $\to$ `Mastery`), with the complete **4-Step Zero-Magic Analysis** for each problem, followed by the **Quarantine Table (`R-3A-01` to `R-3A-10`)** of excluded bare-template problems.

---

### 77.1 Tier 1 — Stepping Stone (8 Problems: PAM Fail-Tree Topology, Double-Palindrome Splitting & Inverse Array Basics)

#### Problem 3A-01: `[ZH]` `[APIO 2014] Palindrome` (`回文串`, Luogu P3649 / UOJ #104 / BZOJ 3676)
- **Statement & Constraints**: Given a string $S$ of length $N \le 3 \times 10^5$ over `a`–`z`, find the maximum of $|P| \times \text{occ}_S(P)$ over all palindromic substrings $P$ of $S$.
- **1. Diagnostic Signal**: Enumerating all $O(N^2)$ palindromic substrings via Manacher cannot group identical palindromes across different centers to sum $\text{occ}_S(P)$.
- **2. Combinatorial Word Invariant**: By the Droubay–Pirillo Theorem, $S$ has at most $N$ distinct non-empty palindromic substrings, corresponding 1-to-1 with the nodes of the PAM. Every occurrence of a palindrome $u$ is a longest palindromic suffix at some right endpoint $r$, or a proper palindromic border (`fail` ancestor) of the longest palindromic suffix at $r$.
- **3. Reverse-Engineering Scratchpad**: Increment $\text{cnt}[\text{pos}[r]]$ by $1$ for each $r \in [1..N]$, then push counts bottom-up on the Fail Tree (`cnt[fail[u]] += cnt[u]` in reverse creation order $u = \text{tot} \dots 2$). The answer is $\max_{u \ge 2} \text{len}[u] \cdot \text{cnt}[u]$ in $O(N)$ time.
- **4. Boundary Pitfalls**: Never include the odd root $r_1$ ($\text{len} = -1$) or even root $r_0$ ($\text{len} = 0$) in the maximization; reverse node creation order is already a valid reverse topological order of the Fail Tree without needing explicit adjacency lists.

#### Problem 3A-02: `[ZH]` `[国家集训队] 最长双回文串` (Longest Double Palindrome, Luogu P4555 / BZOJ 2565)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), find the maximum length of a substring $S[l..r]$ that can be partitioned into two non-empty palindromes $S[l..k]$ and $S[k+1..r]$ ($l \le k < r$).
- **1. Diagnostic Signal**: Checking all split points $k \in [1, N-1]$ requires knowing both the longest palindrome ending at $k$ and the longest palindrome starting at $k+1$.
- **2. Combinatorial Word Invariant**: Build a forward PAM on $S$ (`max_suff[k] = len[pos_fwd[k]]`) and a backward PAM on $S^R$ (`max_pref[k+1] = len[pos_bwd[k+1]]`), or equivalently sweep Manacher intervals to maintain $\max_{c} (2(k - c) + 1)$ at each boundary.
- **3. Reverse-Engineering Scratchpad**: Using two PAM passes (left-to-right and right-to-left), $\text{ans} = \max_{1 \le k < N} (\text{max\_suff}[k] + \text{max\_pref}[k+1])$ in $O(N)$ time.
- **4. Boundary Pitfalls**: Both halves must be **non-empty** ($\text{max\_suff}[k] \ge 1$ and $\text{max\_pref}[k+1] \ge 1$); a single whole-string palindrome of length 1 cannot be split into two non-empty palindromes.

#### Problem 3A-03: `[ZH]` `[SHOI 2011] 双倍回文` (Double Palindrome, Luogu P4287 / BZOJ 2342)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), find the longest substring of the form $w w^R w w^R$ (an even-length palindrome $P$ of length $4k$ whose half $P[1..2k]$ is also a palindrome).
- **1. Diagnostic Signal**: Not enough for the *longest* border $\text{fail}[u]$ to have length $\le \text{len}[u]/2$; we need to test whether the exact half-prefix $P[1..\text{len}[u]/2]$ of PAM node $u$ is a palindrome.
- **2. Combinatorial Word Invariant**: Since $P$ is a palindrome, its prefix of length $\text{len}[u]/2$ is a palindrome if and only if its suffix of length $\text{len}[u]/2$ is a palindrome—i.e., $u$ has a Fail-Tree ancestor `half[u]` of exact length $\text{len}[u]/2$!
- **3. Reverse-Engineering Scratchpad**: Maintain `trans[u]` (or `half[u]`), the longest Fail-Tree ancestor of $u$ with $\text{len}[\text{trans}[u]] \le \text{len}[u] / 2$, by walking from $\text{trans}[\text{parent}(u)]$ when creating $u$ (amortized $O(1)$ per node!). Check if $\text{len}[u] \equiv 0 \pmod 4$ and $\text{len}[\text{trans}[u]] == \text{len}[u] / 2$.
- **4. Boundary Pitfalls**: When $\text{len}[u] \le 2$, initialize $\text{trans}[u] = \text{fail}[u]$ directly; do not start the pointer walk from $\text{trans}[\text{parent}(u)]$ when $\text{parent}(u)$ is $r_0$ or $r_1$.

#### Problem 3A-04: `[EN]` `CF 17E — Palisection`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^6$, memory limit 64–128 MB), count the number of pairs of palindromic substrings $(S[l_1..r_1], S[l_2..r_2])$ that overlap ($\max(l_1, l_2) \le \min(r_1, r_2)$) modulo $51123987$.
- **1. Diagnostic Signal**: Counting overlapping interval pairs directly is a 2D intersection problem; furthermore, the tight memory limit forbids $O(N |\Sigma|)$ transition arrays in a naive PAM.
- **2. Combinatorial Word Invariant**: Complementary counting: two intervals $[l_1, r_1]$ and $[l_2, r_2]$ fail to overlap if and only if $r_1 < l_2$ or $r_2 < l_1$. Thus:
  $$\text{Overlapping} = \binom{\text{Total}}{2} - \sum_{1 \le r < l \le N} \text{end\_cnt}[r] \cdot \text{start\_cnt}[l].$$
- **3. Reverse-Engineering Scratchpad**: Either use Manacher difference arrays (`start_cnt` and `end_cnt` receive $+1$ on range of centers) in $O(N)$ time and $O(N)$ memory, or a linked-list-transition PAM where $\text{end\_cnt}[r] = \text{dep}[\text{pos}[r]]$ on the forward pass and $\text{start\_cnt}[l] = \text{dep}[\text{pos}[l]]$ on the reverse pass.
- **4. Boundary Pitfalls**: Total palindromes can be $\binom{N+1}{2} \approx 2 \times 10^{12}$, which overflows 32-bit integers before taking $\binom{\text{Total}}{2} \bmod 51123987$ (note $51123987$ is prime, so multiply by $\text{inv}(2)$).

#### Problem 3A-05: `[EN]` `CF 1080E — Sonya and Matrix Beauty`
- **Statement & Constraints**: Given an $N \times M$ character grid ($N, M \le 250$), count subgrids where every row's characters can be rearranged to form a palindrome, and the sequence of rearranged rows from top to bottom is also a palindrome.
- **1. Diagnostic Signal**: Naive subgrid verification is $O(N^2 M^2)$.
- **2. Combinatorial Word Invariant**: Two rows inside column range $[c_1, c_2]$ can be rearranged into the **same** palindrome if and only if their character frequency vectors (Parikh vectors) over `a`–`z` are identical, AND at most one character has odd frequency (checkable via a 26-bit XOR mask $\text{mask} \ \& \ (\text{mask}-1) == 0$).
- **3. Reverse-Engineering Scratchpad**: Fix column range $[c_1, c_2]$ in $O(M^2)$. Incrementally maintain the 26-element frequency vector and parity bitmask for each row $r \in [1..N]$. Mark rows with $>1$ odd frequency as invalid distinct sentinel characters (cannot match any other row or form a valid palindrome center), and run 1D Manacher on the row-vector array in $O(N)$ (comparing 26-element vectors in $O(1)$ via polynomial hash or direct comparison inside Manacher's $O(N)$ amortized bound!). Total time: $O(M^2 N |\Sigma|)$ or $O(M^2 N)$.
- **4. Boundary Pitfalls**: Invalid rows (with $\ge 2$ odd character counts) must NOT match themselves or each other during Manacher expansion, nor contribute radius $1$! Assign each invalid row a unique negative ID and skip them when summing radii.

#### Problem 3A-06: `[ZH]` `[ZJOI 2013] 话旧 / Prefix Function & Z-Array Restoration` (Luogu P1117 / CF Restoration Archetype)
- **Statement & Constraints**: Given a candidate KMP prefix array $\pi[1..N]$ ($N \le 2 \times 10^5$) and alphabet size $\sigma$, verify whether $\pi$ is realizable by some string $S \in \Sigma^N$, and if so, count the number of valid strings $S$ modulo $10^9 + 7$.
- **1. Diagnostic Signal**: Checking only $\pi[i] \le \pi[i-1] + 1$ accepts invalid arrays like $\pi = [0, 1, 0, 1, 1]$.
- **2. Combinatorial Word Invariant**: By Invariant 76.2.3, walking $k = \pi[i-1], \pi[k], \dots$ until $k + 1 = \pi[i]$ extracts all forbidden characters $S[k+1] \ne S[i]$ in amortized $O(1)$ steps per position $i$.
- **3. Reverse-Engineering Scratchpad**: Maintain component ID $\text{comp}[i]$ for each position. At step $i$, collect the distinct component IDs of $S[k+1]$ along the fail chain above $\pi[i]-1$. If $\pi[i] > 0$, verify $k + 1 == \pi[i]$ and $\text{comp}[\pi[i]] \notin \text{forb}$, then set $\text{comp}[i] = \text{comp}[\pi[i]]$. If $\pi[i] == 0$, also insert $\text{comp}[1]$ into $\text{forb}$, assign a new component ID to $\text{comp}[i]$, and multiply the answer by $\max(0, \sigma - |\text{forb}|)$.
- **4. Boundary Pitfalls**: Remember to clear the visited markers on `forb` using a rollback list rather than `memset` so total time stays $O(N)$.

#### Problem 3A-07: `[JA]` `AtCoder ARC 060 E / ARC Palindrome Partition & Periodicity` (`Best Representation`)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), find the minimum number of pieces in a partition of $S$ into **aperiodic** (or non-trivial non-palindromic / border-free) strings, and count the number of such minimal partitions.
- **1. Diagnostic Signal**: Testing all split points requires knowing whether $S[l..r]$ is periodic or a single character run.
- **2. Combinatorial Word Invariant**: By Fine–Wilf and border theory, a string $S$ that is not $c^N$ is either already valid in $1$ piece, or every prefix/suffix check via KMP/Manacher reduces the partition size to at most $2$!
- **3. Reverse-Engineering Scratchpad**: Check if $S = c^N$ (answer $N$, count $1$). Else check if $S$ itself is valid ($1$ piece). Else count split points $k \in [1, N-1]$ where neither $S[1..k]$ nor $S[k+1..N]$ has a proper period dividing its length ($O(N)$ via KMP on $S$ and $S^R$).
- **4. Boundary Pitfalls**: A prefix $S[1..k]$ is periodic iff $\pi[k] > 0$ and $(k - \pi[k]) \mid k$; forgetting the divisibility condition falsely marks non-periodic strings with borders (like $\texttt{aba}$) as periodic!

#### Problem 3A-08: `[EN]` `ICPC / Codeforces Gym — Manacher Radius Array Restoration` (`Inverse Manacher`)
- **Statement & Constraints**: Given proposed odd Manacher radii $R_{\text{odd}}[1..N]$ and even Manacher radii $R_{\text{even}}[1..N-1]$ ($N \le 2 \times 10^5$), reconstruct the lexicographically smallest string $S$ over `'a'`–`'z'` whose Manacher radii equal the input, or report `-1` if impossible.
- **1. Diagnostic Signal**: Adding all $O(N^2)$ mirror equalities $S[c-d] = S[c+d]$ TLEs.
- **2. Combinatorial Word Invariant**: Running the Manacher box $[L, R]$ expansion backward: only positions $p > R$ need new equality edges $S[p] = S[2c - p]$, while mirror centers $c'$ inside $[L, R]$ either force $\text{rad}[c] = \min(\text{rad}[c'], R - c + 1)$ or add a single inequality edge $S[c + \text{rad}[c]] \ne S[c - \text{rad}[c]]$.
- **3. Reverse-Engineering Scratchpad**: Process centers $c$ left-to-right on the unified $2N-1$ center array. Whenever $p$ advances past $R$, set $S[p] = S[2c-p]$. Whenever a center starts a fresh character at $p = c$ (with $\text{rad}_{\text{odd}}[c]$ starting at $1$), choose the smallest letter not in `forbidden[p]`. Finally, run standard forward Manacher on the constructed string $S$ to verify 100% agreement with the input radii!
- **4. Boundary Pitfalls**: Running forward Manacher as a final verification step catches all malformed radii (negative, out-of-bounds, or violating mirror transitivity) in 5 lines of code without needing to code every mirror case check manually!

---

### 77.2 Tier 2 — Intermediate (8 Problems: Deque PAM, $\theta$-Palindromes, Tree PAM & Fail-Tree Subtree Queries)

#### Problem 3A-09: `[ZH]` `[JSOI 2016] 扭动的回文串` (Twisted Palindrome, Luogu P4324 / BZOJ 4755)
- **Statement & Constraints**: Given two strings $A[1..N]$ and $B[1..N]$ ($N \le 10^5$), find the maximum length of a palindrome formed by taking a substring $A[i..j]$, a substring $B[k..l]$, or a concatenated string $A[i..j] + B[j..l]$ (where the transition from $A$ to $B$ steps from $A[j]$ to $B[j]$ or $B[j+1]$).
- **1. Diagnostic Signal**: The palindrome center can lie inside $A$, inside $B$, or at the seam between $A$ and $B$.
- **2. Combinatorial Word Invariant**: Any seam-straddling palindrome $A[i..j] B[j..l]$ centered inside $A$ at $c$ consists of a core palindrome $A[c - r + 1 .. c + r - 1]$ inside $A$ (stopping at $j = c + r - 1$), followed by an outer wing where $A[c - r .. i]$ matches $(B[j .. l])^R$, which is the **Longest Common Prefix (LCP)** between the reversed prefix $A[1..c-r]^R$ and the suffix $B[j..N]$!
- **3. Reverse-Engineering Scratchpad**: Run Manacher on $A$ and $B$ to get maximal internal palindromes $[L_c, R_c]$ for every center $c$. At the boundary of each maximal palindrome $[L_c, R_c]$ in $A$, extend outward by $\text{LCP}(A[1..L_c-1]^R, B[R_c..N])$ using Polynomial Rolling Hash + Binary Search (or SA/Z-algorithm). Symmetrically for centers in $B$. Time: $O(N \log N)$.
- **4. Boundary Pitfalls**: Always take the **maximal** palindrome inside $A$ (or $B$) around center $c$ before switching to the other string! Why? Because if $A[L_c-1] == A[R_c+1]$ holds, staying inside $A$ for one more step is always valid and can never be worse than switching early at the same center $c$.

#### Problem 3A-10: `[ZH]` `[CERC 2014] Virus Synthesis` (Luogu P4762 / UVa 1679 / BZOJ 4059)
- **Statement & Constraints**: Starting from an empty string, you can either (1) insert a single character at the front or back (cost 1), or (2) replace the current string $w$ with $w w^R$ (doubling it into an even-length palindrome, cost 1). Find the minimum operations to form a substring containing (and then extending to) target string $S[1..N]$ ($N \le 10^5$).
- **1. Diagnostic Signal**: Doubling operation (2) always produces an **even-length palindrome**; single-character front/back additions between doublings correspond to extending a palindrome $u \to c u c$ (by adding $c$ to one side before doubling!) or appending characters at the very end.
- **2. Combinatorial Word Invariant**: For every even-length node $u$ in the PAM of $S$, let $dp[u]$ be the minimum operations to form the palindrome $u$. Then $u$ can be formed either:
  - By taking its parent $p$ in the PAM Trie ($u = c p c$), adding $c$ on one side of the half-string of $p$ *before* the last doubling of $p$: $dp[u] \le dp[p] + 1$; OR
  - By forming a shorter palindromic suffix $v$ of the half-palindrome of $u$ ($\text{len}[v] \le \text{len}[u]/2$, i.e., an ancestor of $\text{trans}[u]$), adding the remaining $\text{len}[u]/2 - \text{len}[v]$ characters to complete the half-string, and then doubling once (+1): $dp[u] \le dp[\text{trans}[u]] + (\text{len}[u]/2 - \text{len}[\text{trans}[u]]) + 1$!
- **3. Reverse-Engineering Scratchpad**: Build the PAM of $S$ along with the half-length link $\text{trans}[u]$ ($\text{len}[\text{trans}[u]] \le \text{len}[u]/2$). Do a BFS over even-length nodes of the PAM Trie:
  $$dp[u] = \min\big(dp[\text{parent}(u)] + 1,\; dp[\text{trans}[u]] + \text{len}[u]/2 - \text{len}[\text{trans}[u]] + 1\big),$$
  with base case $dp[r_0] = 0$ (or $dp[u] = \text{len}[u]$). Overall answer: $\min_{u \text{ even}} (dp[u] + N - \text{len}[u])$. Time: $O(N)$.
- **4. Boundary Pitfalls**: The DP recurrence $dp[u] \le dp[\text{parent}(u)] + 1$ uses the **Trie parent**, whereas $\text{trans}[u]$ is an ancestor in the **Fail Tree**. Because both $\text{len}[\text{parent}(u)] < \text{len}[u]$ and $\text{len}[\text{trans}[u]] \le \text{len}[u]/2 < \text{len}[u]$, processing nodes in **BFS order of the PAM Trie** (increasing order of $\text{len}[u]$) guarantees all dependencies are already computed!

#### Problem 3A-11: `[ZH]` `HDU 6599 — I Love Palindrome String` (PAM + Palindromic Half-Length Check)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^5$), for each length $L \in [1, N]$, count the number of occurrences of palindromic substrings $P$ of length $L$ whose prefix of length $\lceil L/2 \rceil$ is also a palindrome.
- **1. Diagnostic Signal**: Similar to Double Palindrome, except $L$ can be odd or even, so $\lceil L/2 \rceil = \lfloor (L+1)/2 \rfloor$, and we must aggregate occurrence counts for every valid PAM node by its length $L$.
- **2. Combinatorial Word Invariant**: A palindrome $u$ of length $L$ has a palindromic prefix of length $\lceil L/2 \rceil$ iff its Fail-Tree ancestor of maximum length $\le \lceil L/2 \rceil$ has length **exactly** $\lceil L/2 \rceil$ (or check in $O(1)$ via string hashing / Manacher at the creation occurrence of $u$).
- **3. Reverse-Engineering Scratchpad**: Build the PAM of $S$, accumulate subtree occurrence counts $\text{cnt}[u]$ on the Fail Tree, and for each node $u$ check whether its half-prefix is a palindrome (either via the `half[u]` pointer with threshold $\lfloor (\text{len}[u]+1)/2 \rfloor$ or $O(1)$ Manacher radius lookup at the midpoint of $u$'s first occurrence!). Add $\text{cnt}[u]$ to `ans[len[u]]`. Time: $O(N)$.
- **4. Boundary Pitfalls**: Using Manacher on $S$ to test whether the prefix $S[r - \text{len}[u] + 1 .. r - \lfloor \text{len}[u]/2 \rfloor]$ is a palindrome in $O(1)$ at the creation time of node $u$ avoids all off-by-one bugs in maintaining `half[u]` for odd vs. even $\text{len}[u]$!

#### Problem 3A-12: `[ZH]` `BZOJ 4976 / Luogu — Double-Ended Insertion PAM` (`双向 PAM` Archetype)
- **Statement & Constraints**: Maintain a string $S$ initially empty under $Q \le 2 \times 10^5$ operations: (1) `push_front(c)`, (2) `push_back(c)`, (3) query total number of distinct palindromic substrings currently in $S$ and total number of palindromic substrings (with multiplicity) currently in $S$.
- **1. Diagnostic Signal**: Front and back insertions require maintaining both $\text{last\_front}$ and $\text{last\_back}$ on a shared PAM.
- **2. Combinatorial Word Invariant**: By Invariant 73.2.3, `push_back(c)` adds $\text{dep}[\text{last\_back}]$ new palindromic occurrences (the fail-depth of the new $\text{last\_back}$) and at most $1$ new distinct palindrome; if $\text{len}[\text{last\_back}] == R - L + 1$, update $\text{last\_front} \leftarrow \text{last\_back}$. Symmetrically for `push_front(c)`.
- **3. Reverse-Engineering Scratchpad**: Allocate $S$ centered at index $Q + 5$ in an array of size $2Q + 10$. Use either amortized fail links (which ARE amortized $O(1)$ when there are no rollbacks/deletions—why? Because $\text{len}[\text{last\_front}]$ and $\text{len}[\text{last\_back}]$ each increase by at most $2$ per insertion, and a crossover sets one equal to $R - L + 1$, which is bounded by $Q$!) or `quick_link[u][c]` for worst-case $O(1)$.
- **4. Boundary Pitfalls**: Even in insertion-only Deque PAM, when testing $S[R - \text{len}[u] - 1] == S[R]$ during `push_back`, you **must** verify $R - \text{len}[u] - 1 \ge L$! Why? Because $S[L-1]$ might contain a character or garbage from initialization if not cleared to a unique sentinel, and during `push_front` $S[L-1]$ is actively overwritten! Simply keep $S[L-1] = -1$ and $S[R+1] = -2$ updated before each extension.

#### Problem 3A-13: `[JA]` `AtCoder ABC 259 Ex / ARC Palindrome Path & Automaton` / `Tree PAM (`树上回文自动机`)` (`QOJ / Luogu Tree PAM`)
- **Statement & Constraints**: Given a rooted tree (or trie) of $N \le 3 \times 10^5$ vertices where each vertex carries a character $c_v \in \Sigma$, compute for every vertex $v$ the number of palindromic suffixes of the root-to-$v$ path string (and the number of distinct palindromes across all root-to-node paths).
- **1. Diagnostic Signal**: On a tree with high branching factor, amortized fail-link traversal from parent $p$ to child $v$ takes $\Omega(N^2)$ time on $\texttt{a}^{N/2}$ with $\texttt{b}$-leaves!
- **2. Combinatorial Word Invariant**: By Invariant 73.2.1 (`quick_link[u][c]`), the fail transition at vertex $v$ from $u = \text{last}[p]$ takes **worst-case $O(1)$ time**: if the character at depth $\text{depth}(v) - \text{len}[u] - 1$ on the ancestor stack equals $c_v$, we extend $u$; otherwise we jump in $O(1)$ to $u' = \text{quick\_link}[u][c_v]$!
- **3. Reverse-Engineering Scratchpad**: Run a DFS on the tree maintaining the current root-to-$v$ character stack `st[dep]`. At vertex $v$ with parent $p$, let $u = \text{last}[p]$. Check if $\text{dep} - \text{len}[u] - 1 \ge 1$ and $\text{st}[\text{dep} - \text{len}[u] - 1] == c_v$; if not, set $u \leftarrow \text{quick\_link}[u][c_v]$. Then extend `next[u][c_v]` (creating a new PAM node and initializing its `quick_link` from its `fail` in $O(|\Sigma|)$ if needed). Total time: $O(N |\Sigma|)$.
- **4. Boundary Pitfalls**: If two sibling branches from parent $p$ have the **same** character $c$, the second branch will find `next[u][c]` already exists in the PAM! In that case, do NOT allocate a duplicate node—simply reuse `next[u][c]`!

#### Problem 3A-14: `[EN]` `Codeforces / Gym — Antisymmetric / Watson–Crick Palindromes` (`POI 2010 ANT — Antisymmetry` / Luogu P3501)
- **Statement & Constraints**: Given a binary string $S[1..N]$ ($N \le 5 \times 10^5$), count the number of non-empty substrings $w$ that are **antisymmetric palindromes** ($w = \overline{w^R}$, i.e., $w[i] \ne w[|w|-i+1]$ for all $i$).
- **1. Diagnostic Signal**: An antisymmetric palindrome is a $\theta$-palindrome under the fixed-point-free involution $\theta(0) = 1, \theta(1) = 0$.
- **2. Combinatorial Word Invariant**: By Invariant 76.2.2, because $\theta(c) \ne c$ for all $c \in \{0, 1\}$, **every antisymmetric palindrome has even length**! Furthermore, the reflection of an antisymmetric palindrome across an antisymmetric center is still antisymmetric, so Manacher's algorithm on inter-character centers $c \in [1, N-1]$ works with the single modification that expansion tests $S[c - k + 1] == \theta(S[c + k])$.
- **3. Reverse-Engineering Scratchpad**: Run even-center Manacher for $c = 1 \dots N-1$ maintaining the rightmost antisymmetric palindrome $[L, R]$ with the test $S[c - k + 1] \ne S[c + k]$, or build a $\theta$-PAM without the odd root $r_1$. Sum $\text{rad}_{\text{even}}[c]$ over all $c \in [1, N-1]$ in $O(N)$ time.
- **4. Boundary Pitfalls**: Do not run odd-center Manacher; odd-length strings can never be antisymmetric because the middle character would have to satisfy $w[m] \ne w[m]$.

#### Problem 3A-15: `[ZH]` `[THUPC / UOJ / Luogu P5446] [THUPC 2018] 绿绿和串串` (Reverse-Flip Prefix Synchronization)
- **Statement & Constraints**: Given a string $S[1..N]$ ($N \le 10^6$), an operation replaces a string $T[1..K]$ with $T[1..K] + T[K-1] + T[K-2] + \dots + T[1]$ (mirroring around the last character $T[K]$). Determine all initial lengths $K \in [1, N]$ from which repeated operations can produce a string having $S[1..N]$ as a prefix.
- **1. Diagnostic Signal**: Mirroring around index $K$ creates an odd palindrome centered at $K$ reaching at least to index $1$ or the end of $S$.
- **2. Combinatorial Word Invariant**: Working backwards from $K = N$ down to $1$, an index $K$ is valid if and only if either:
  - The maximal palindrome centered at $K$ reaches the right end of $S$ ($K + \text{rad}_{\text{odd}}[K] - 1 == N$), OR
  - The maximal palindrome centered at $K$ reaches the left end of $S$ ($K - \text{rad}_{\text{odd}}[K] + 1 == 1$) **AND** the right boundary of that palindrome $K' = K + \text{rad}_{\text{odd}}[K] - 1$ is itself already a valid center!
- **3. Reverse-Engineering Scratchpad**: Compute odd Manacher radii $\text{rad}_{\text{odd}}[1..N]$ in $O(N)$. Sweep $K$ from $N$ down to $1$ to compute boolean `valid[K]` in $O(N)$ total time.
- **4. Boundary Pitfalls**: In the second case, the palindrome centered at $K$ must reach $1$ ($K - \text{rad}_{\text{odd}}[K] + 1 == 1$) so that the prefix $T[1..K]$ was completely mirrored inside $S$; if it stops before $1$ and before $N$, the mismatch occurs inside both wings of the mirror, making $K$ impossible!

#### Problem 3A-16: `[JA]` `AtCoder AGC 047 B — First Second`
- **Statement & Constraints**: Given $N$ strings $S_1, \dots, S_N$ ($\sum |S_i| \le 10^6$), in one operation on a string you may delete either its first character or its second character. Count pairs $(i, j)$ such that $S_i$ can be reduced to $S_j$.
- **1. Diagnostic Signal**: Deleting either the 1st or 2nd character repeatedly preserves the suffix of length $|S_j| - 1$ of $S_i$, and allows the first character of $S_j$ to match **any** character occurring in the deleted prefix $S_i[1 .. |S_i| - |S_j| + 1]$. (This is the classic reversed Trie + prefix character mask problem; when coupled with palindromic prefixes in its `[JA]`/`[ZH]` variants such as `HDU / Luogu Palindromic Prefix Trie`, we query on a Trie of reversed strings how many prefixes are palindromes or contain character $c$).
- **2. Combinatorial Word Invariant**: $S_i$ reduces to $S_j$ iff $S_j[2..|S_j|]$ is a suffix of $S_i$ and the character $S_j[1]$ appears at least once in $S_i[1 .. |S_i| - |S_j| + 1]$.
- **3. Reverse-Engineering Scratchpad**: Insert all $S_i^R$ into a Trie. At each node corresponding to the suffix of length $k$ of $S_i$, maintain the count of strings $S_j$ ending at this node with first character $c \in \Sigma$. During insertion of $S_i^R$, keep a running bitmask of characters in the remaining prefix of $S_i$ to aggregate matches in $O(\sum |S_i| |\Sigma|)$.
- **4. Boundary Pitfalls**: Process shorter strings $S_j$ before or separately from longer strings $S_i$, and subtract self-pairs $i = j$.

---

### 77.3 Tier 3 — Advanced (8 Problems: `slink` Palindrome DP, Range Palindrome Counting, LCT/PAM Coupling & Rich Words)

#### Problem 3A-17: `[EN]` `CF 932G — Palindrome Partition` (Even-Length Palindrome Factorization via Shuffle Transformation + PAM `slink` DP)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6$, $N$ even), count the number of ways to partition $S$ into $2k$ substrings $s_1 s_2 \dots s_{2k}$ such that $s_i = s_{2k - i + 1}$ for all $1 \le i \le k$, modulo $10^9 + 7$.
- **1. Diagnostic Signal**: A symmetric partition $S = s_1 s_2 \dots s_k s_k \dots s_2 s_1$ couples prefixes and suffixes from opposite ends of $S$.
- **2. Combinatorial Word Invariant**: **The Shuffle Interleaving Transformation**: Construct the interleaved string:
  $$T = S[1]\; S[N]\; S[2]\; S[N-1]\; \dots\; S[N/2]\; S[N/2+1].$$
  Then a prefix block $s_1 = S[1..L]$ equals the suffix block $s_{2k} = S[N-L+1..N]$ **if and only if** the prefix $T[1..2L]$ of length $2L$ in $T$ is an **even-length palindrome**!
  Thus, symmetric partitions of $S$ correspond bijectively to partitions of $T$ into **even-length palindromes**!
- **3. Reverse-Engineering Scratchpad**: Build the PAM of $T$ online and apply `slink` DP (Wave 1A): for each node $u$, maintain $g[u] = \sum_{v \text{ in } u\text{'s slink chain}} dp[r - \text{len}[v]]$ via $g[u] = dp[r - (\text{len}[\text{slink}[u]] + \text{diff}[u])] + ( \text{diff}[u] == \text{diff}[\text{fail}[u]] ? g[\text{fail}[u]] : 0 )$. At each even $r$, sum $g[u]$ over the $O(\log r)$ `slink` chains from $\text{pos}[r]$. Time: $O(N \log N)$.
- **4. Boundary Pitfalls**: Only allow DP transitions at **even** indices $r$ ($dp[r] = 0$ for odd $r$) so that every palindrome used in the partition of $T$ automatically has even length!

#### Problem 3A-18: `[EN]` `CF 906E — Reverses` (Minimum-Flip Alignment via Shuffle + PAM `slink` Argmin DP)
- **Statement & Constraints**: Given two strings $A[1..N]$ and $B[1..N]$ ($N \le 5 \times 10^5$), find the minimum number of disjoint intervals $[l_i, r_i]$ to reverse in $A$ so that $A$ becomes equal to $B$, and reconstruct the intervals.
- **1. Diagnostic Signal**: Reversing $A[l..r]$ to match $B[l..r]$ means $A[l..r] = (B[l..r])^R$.
- **2. Combinatorial Word Invariant**: Interleave $A$ and $B$ into $T = A[1] B[1] A[2] B[2] \dots A[N] B[N]$ of length $2N$. Then $A[l..r] = (B[l..r])^R$ **if and only if** the substring $T[2l-1 .. 2r]$ of length $2(r - l + 1)$ is an **even-length palindrome**!
  Unreversed single characters $A[i] == B[i]$ correspond to palindromes of length $2$ ($T[2i-1..2i]$) which cost $0$ operations; palindromes of length $\ge 4$ cost $1$ operation.
- **3. Reverse-Engineering Scratchpad**: Run PAM `slink` minimum-cost DP on $T[1..2N]$ storing `(min_cost, backpointer_index)` in $g[u]$ for each `slink` chain, plus a direct $0$-cost transition $dp[2i] \leftarrow dp[2i-2]$ whenever $T[2i-1] == T[2i]$. Time: $O(N \log N)$.
- **4. Boundary Pitfalls**: When reconstructing the intervals, remember that $g[u]$ merges `g[fail[u]]` (which shifted its right endpoint from $r - \text{diff}[u]$ to $r$ while keeping the **exact same left endpoint** $r - \text{len}[v] = (r - \text{diff}[u]) - \text{len}[\text{fail}[v]]$!). Therefore, storing the **left endpoint index** $p = r - \text{len}[v]$ in $g[u]$ remains invariant when shifting from $r - \text{diff}[u]$ to $r$!

#### Problem 3A-19: `[ZH]` `Luogu P5555 — 秩序魔咒 / BZOJ 4044 — Substring Distinct Palindromes & Common Palindrome Variants` (`[国家集训队论文 2014 — 徐毅]` Range Distinct Palindromes)
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ queries $(l_i, r_i)$ ($N, Q \le 10^5$ or $3 \times 10^5$), output for each query the number of **distinct** palindromic substrings contained in $S[l_i..r_i]$.
- **1. Diagnostic Signal**: Requires deduplicating identical palindromes within $[l_i, r_i]$.
- **2. Combinatorial Word Invariant**: By Invariant 75.2.2 (Periodic Suffix Telescoping Cancellation), at step $r$, each of the $O(\log r)$ `slink` chains $\{u_1, \dots, u_k\}$ on the path from $\text{pos}[r]$ cancels all internal start positions, requiring only `-1` at $\text{last}_{r-1}(u_1) - \text{len}[u_1] + 1$ and `+1` at $r - (\text{len}[\text{slink}[u_1]] + \text{diff}[u_1]) + 1$.
- **3. Reverse-Engineering Scratchpad**: Build PAM + Fail-Tree Euler tour $[\text{dfn}[u], \text{out}[u]]$. Sweep $r = 1 \dots N$ using a Segment Tree for subtree max endpos and a Fenwick Tree (offline) or Persistent Segment Tree (online) for start-position range sums over $[l, r]$. Time: $O(N \log^2 N + Q \log N)$.
- **4. Boundary Pitfalls**: Query `MaxEndposSegTree.query(dfn[u], out[u])` for all $u$ on the `slink` chain **before** executing `MaxEndposSegTree.update(dfn[pos[r]], r)`.

#### Problem 3A-20: `[EN]` `Codeforces / SPOJ / HDU — Large-N Range All-Palindromes Count` ($S[l..r]$ Palindrome Multiplicity Queries for $N, Q \le 3 \times 10^5$)
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ queries $(l_i, r_i)$ ($N, Q \le 3 \times 10^5$), compute the total number of palindromic substrings (with multiplicity) inside $S[l_i..r_i]$.
- **1. Diagnostic Signal**: $O(N^2)$ DP (`CF 245H`) exceeds both time and memory limits for $N = 3 \times 10^5$.
- **2. Combinatorial Word Invariant**: By Invariant 74.2.3 (Midpoint Decoupling Identity), splitting centers at $m = \lfloor (l+r)/2 \rfloor$ reduces $\min(\text{rad}[c], c - l + 1, r - c + 1)$ to $\min(\text{rad}[c], c - l + 1)$ on $[l, m]$ and $\min(\text{rad}[c], r - c + 1)$ on $[m+1, r]$.
- **3. Reverse-Engineering Scratchpad**: Run Manacher for odd and even centers. Sort queries by $l$ (for the left half $[l, m]$) and by $r$ (for the right half $[m+1, r]$), maintaining Fenwick trees for $\sum \text{rad}[c]$, $\sum c$, and $\sum 1$ as centers cross the clipping thresholds $L_c \ge l$ and $R_c \le r$. Time: $O((N + Q) \log N)$.
- **4. Boundary Pitfalls**: Use $m_{\text{odd}} = \lfloor(l+r)/2\rfloor$ for odd centers $c \in [l, r]$ and $m_{\text{even}} = \lfloor(l+r-1)/2\rfloor$ for even centers $c \in [l, r-1]$.

#### Problem 3A-21: `[EN]` `CF 1827C — Palindrome Partition` (Minimal Even-Palindrome Prefix Decomposition)
- **Statement & Constraints**: Call a string *good* if it is an even-length palindrome, and *beautiful* if it is a concatenation of good strings. Given $S[1..N]$ ($N \le 5 \times 10^5$), count how many substrings of $S$ are beautiful.
- **1. Diagnostic Signal**: A substring could have exponentially many factorizations into even-length palindromes; we need a **canonical (unique)** first step to avoid double counting.
- **2. Combinatorial Word Invariant**: **Greedy Shortest Even-Palindrome Lemma**: If a string $W$ is a concatenation of even-length palindromes, and $P$ is the **shortest** non-empty even-length palindromic prefix (or suffix!) of $W$, then removing $P$ leaves a string $W'$ that is **still** a concatenation of even-length palindromes!
  *Proof*: Let the first block in some valid partition of $W$ be an even palindrome $Q$. If $|Q| == |P|$, removing $P = Q$ trivially leaves the rest of the partition. If $|Q| > |P|$, then since $P$ is the *shortest* even-palindrome prefix of $Q$, $P$ cannot exceed half the length of $Q$ (Wait: if $|P| > |Q|/2$, the overlap of $P$ at the prefix of $Q$ and $P^R = P$ at the suffix of $Q$ has even length $2|P| - |Q| < |P|$, which would be a strictly shorter even-palindrome prefix of $Q$, contradiction!). Thus $|P| \le |Q|/2$, so stripping $P$ from the front of $Q$ and $P$ from the back of $Q$ leaves a middle even palindrome $Q_{\text{mid}}$ followed by $P$, which is still a valid partition of $W'$ into even palindromes!
- **3. Reverse-Engineering Scratchpad**: For each right endpoint $r$, find the **shortest** non-empty even-length palindromic suffix of $S[1..r]$ (either via PAM by tracking the shortest even ancestor `min_even[u]` on the Fail Tree, or via even Manacher + DSU/stack). If its length is $L_r > 0$, then $dp[r] = 1 + dp[r - L_r]$. Answer is $\sum_{r=1}^{N} dp[r]$ in $O(N)$ time!
- **4. Boundary Pitfalls**: In the PAM Fail Tree, `min_even[u]` is simply `u` if $\text{len}[u]$ is even and $\text{min\_even}[\text{fail}[u]] == 0$, else $\text{min\_even}[\text{fail}[u]]$. That computes the shortest even palindromic suffix at every index in 3 lines of $O(N)$ PAM preprocessing!

#### Problem 3A-22: `[JA]` `AtCoder AGC 005 F / ARC Palindrome Rich Word Construction & Counting` (`Rich Words over Binary Alphabet`)
- **Statement & Constraints**: Count or characterize binary strings of length $N \le 3000$ (or $N \le 10^5$ structural queries) that are **rich words** (contain exactly $N + 1$ distinct palindromic substrings), or determine the minimum characters to append to make a string rich.
- **1. Diagnostic Signal**: Checking richness via PAM at every state of a naive DP requires storing the entire string ($2^N$ states).
- **2. Combinatorial Word Invariant**: By Invariant 76.2.1 (Droubay–Pirillo & Complete Returns), a word $S$ fails to be rich at step $r$ if and only if the longest palindromic suffix $P$ of $S[1..r]$ already occurred in $S[1..r-1]$; and over a binary alphabet, any rich word can be decomposed via run-length / episturmian morphisms or by tracking the last two maximal palindromic suffixes.
- **3. Reverse-Engineering Scratchpad**: In PAM construction, richness is equivalent to creating a new node at **every** step $r \in [1..N]$ ($\text{tot} - 2 == N$). When testing whether $S[l..r]$ is rich in $O(1)$ per query, $S[l..r]$ is rich iff the number of distinct palindromes in $S[l..r]$ equals $r - l + 1$, which is equivalent to checking whether for any $k \in [l, r]$, the longest palindromic suffix of $S[l..k]$ occurred previously in $S[l..k-1]$—i.e., letting $L_{\text{dup}}[k]$ be the start position of the second-latest occurrence of the longest palindromic suffix of $S[1..k]$ that still repeats, $S[l..r]$ is rich iff $\max_{k \in [l, r]} L_{\text{dup}}[k] < l$!
- **4. Boundary Pitfalls**: Let us verify that! Why does $S[l..r]$ fail to be rich iff there exists $k \in [l, r]$ whose longest palindromic suffix inside $S[l..k]$ already occurred in $S[l..k-1]$? Because at step $k$, the longest palindromic suffix of $S[l..k]$ is the highest Fail-Tree ancestor $u$ of $\text{pos}[k]$ with $\text{len}[u] \le k - l + 1$, and it occurred earlier in $S[l..k-1]$ iff its previous occurrence before $k$ started at $\ge l$!

#### Problem 3A-23: `[ZH]` `[SHOI 2014] 基因合成 / Generalized PAM on Multiple Strings` (`BZOJ 3676` / Multi-String Common Palindromes, `G-PAM`)
- **Statement & Constraints**: Given $K$ strings $S_1, S_2, \dots, S_K$ ($\sum |S_i| \le 5 \times 10^5$), count the number of tuples $(P, i_1, \dots, i_K)$ where $P$ is a palindrome occurring in each $S_i$ at those positions (i.e., $\sum_{P \text{ palindrome}} \prod_{i=1}^{K} \text{occ}_{S_i}(P)$).
- **1. Diagnostic Signal**: Building separate PAMs requires intersecting their palindrome sets.
- **2. Combinatorial Word Invariant**: Because a PAM node $u$ is uniquely determined by its path from $r_0$ or $r_1$ in the PAM Trie, we can build a **single Generalized PAM** over $S_1, \dots, S_K$: before processing each string $S_i$, simply reset `last = 0` (and use string-local indexing $S_i[1..|S_i|]$ for the boundary check $S_i[r - \text{len}[u] - 1] == S_i[r]$)!
- **3. Reverse-Engineering Scratchpad**: Maintain $\text{cnt}[u][i]$ (for small $K$) or DSU-on-Tree / Segment Tree Merging over the PAM Fail Tree (for large $K$). Push counts up the Fail Tree once at the end and compute $\sum_{u \ge 2} \prod_{i=1}^K \text{cnt}[u][i]$. Time: $O(\sum |S_i|)$.
- **4. Boundary Pitfalls**: Unlike Generalized SAM (where resetting `last = 0` creates zero-length clone nodes if not handled carefully), in a **Generalized PAM** resetting `last = 0` at the start of each new string $S_i$ creates **zero anomalies** because every PAM node has a single exact length $\text{len}[u]$ and never splits!

#### Problem 3A-24: `[EN]` `Universal Cup / QOJ — Range Longest Palindromic Substring in O(log N) / O(1)` (`Internal Longest Palindrome`)
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ online queries $(l, r)$ ($N, Q \le 5 \times 10^5$), output the length of the longest palindromic substring contained in $S[l..r]$.
- **1. Diagnostic Signal**: Naive center scan is $O(N)$ per query; binary search + RMQ takes $O(\log N)$ per query.
- **2. Combinatorial Word Invariant**: By Invariant 74.2.1, the predicate $\text{HasPal}_{\ge 2k-1}(l, r) \iff (\max_{c \in [l+k-1, r-k+1]} \text{rad}_{\text{odd}}[c] \ge k) \lor (\max_{c \in [l+k-1, r-k]} \text{rad}_{\text{even}}[c] \ge k)$ is strictly monotone in the half-length $k$.
- **3. Reverse-Engineering Scratchpad**: Precompute Manacher arrays $\text{rad}_{\text{odd}}[1..N]$ and $\text{rad}_{\text{even}}[1..N-1]$ in $O(N)$ and two Sparse Tables in $O(N \log N)$. For each query $(l, r)$, binary search $k \in [1, \lfloor(r-l+1)/2\rfloor]$ in $O(\log(r-l+1))$ using $O(1)$ Sparse Table lookups, then check if $\text{even}(k_{\max})$ holds (returning $2k_{\max}$) or only $\text{odd}(k_{\max})$ holds (returning $2k_{\max}-1$, with base answer $1$).
- **4. Boundary Pitfalls**: Handle $l == r$ (answer $1$) and when $\max \text{even} == 0$ (no even palindrome of length $2k$, only odd of length $2k-1$).

---

### 77.4 Tier 4 — Mastery (8 Problems: Full Deque PAM with Deletions, Persistent Tree PAM, Online Range Distinct Palindromes & Grandmaster Reductions)

#### Problem 3A-25: `[EN]` / `[JA]` `Full Double-Ended Deque PAM with Front/Back Push & Pop` (`QOJ / Library-Grade Deque Eertree with Queries` / `Xu Yi 2014 Full Deque PAM`)
- **Statement & Constraints**: Maintain an initially empty deque string $S[L..R]$ under $Q \le 5 \times 10^5$ operations: `push_front(c)`, `push_back(c)`, `pop_front()`, `pop_back()`, outputting after each operation (1) the number of distinct palindromes in $S[L..R]$, (2) the length of the longest palindromic prefix, and (3) the length of the longest palindromic suffix.
- **1. Diagnostic Signal**: Arbitrary interleaving of front/back insertions and deletions breaks both amortized fail-chain walks and LIFO rollback stacks.
- **2. Combinatorial Word Invariant**: Combine Invariant 73.2.1 (`quick_link[u][c]` for worst-case $O(1)$ fail jumps) with Invariant 73.2.4 (Unique Vanishing Palindrome Theorem + `max_pref[i]` / `max_suff[i]` surface pushing + Fail-Tree active out-degree `deg[u]`).
- **3. Reverse-Engineering Scratchpad**: Maintain `max_pref[L..R]`, `max_suff[L..R]`, `surf_cnt[u]`, and `deg[u]`. On `pop_back()` at $R$: let $u = \text{max\_suff}[R]$, $l_u = R - \text{len}[u] + 1$, $f = \text{fail}[u]$. Clear `max_suff[R]`, set `max_pref[l_u] = f`, and update `max_suff[l_u + len[f] - 1]` with $f$ if $\text{len}[f]$ exceeds its current value, updating `surf_cnt` and `deg[fail[u]]` if `surf_cnt[u] + deg[u]` drops to $0$. Symmetrically for `pop_front()` at $L$. Time: worst-case $O(1)$ per operation!
- **4. Boundary Pitfalls**: When $S[L..R]$ becomes empty ($L > R$), reset both `last_front = 0` and `last_back = 0`. When `len[u] == R - L + 1` (the popped palindrome spanned the entire string $[L..R]$), updating `max_pref[L] = f` and `max_suff[R - 1]` automatically sets the new `last_front = f` and `last_back = max_suff[R - 1] == f`!

#### Problem 3A-26: `[ZH]` `QOJ / Universal Cup — Online Range Distinct Palindrome Queries with Encrypted Endpoints`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ **online** queries $(l_i \oplus \text{last\_ans}, r_i \oplus \text{last\_ans})$, return the number of distinct palindromic substrings in $S[l..r]$.
- **1. Diagnostic Signal**: Encrypted online queries forbid offline sorting by $r$; we need a historical query structure at version $r$.
- **2. Combinatorial Word Invariant**: Because our `slink` Telescoping Cancellation algorithm (Invariant 75.2.2) performs at most $2 \log_2 N$ point updates to the start-position array at each step $r \in [1..N]$, persisting the start-position array across $r = 1 \dots N$ via a **Persistent Segment Tree** uses only $O(N \log^2 N)$ total nodes!
- **3. Reverse-Engineering Scratchpad**: During the $r = 1 \dots N$ preprocess sweep, apply the $O(\log r)$ `-1` and `+1` start-position updates to a Persistent Segment Tree (creating `root[r]`) while maintaining the transient `MaxEndposSegTree` over the PAM Fail Tree. Answer each online query $(l, r)$ by querying `PersistentSegTree.query(root[r], l, r)` in **$O(\log N)$ time per query**!
- **4. Boundary Pitfalls**: In the Persistent Segment Tree, do not save intermediate roots during the $O(\log r)$ `slink` updates at step $r$; allocate a new node only along paths modified during step $r$ (or use path-copying per update) and record `root[r]` after the `slink` loop finishes.

#### Problem 3A-27: `[ZH]` `[THUPC / CTS / NOI-Level] Weighted Range Distinct Palindromes on $S[l..r]$` (LCT `access` + PAM Fail Tree)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), each distinct palindrome $P$ has a weight $w(P)$ (e.g., $|P|^2$ or a function of itsPAM node). Answer $Q \le 10^5$ queries $(l, r)$ asking for $\sum_{P \text{ pal in } S[l..r]} w(P)$.
- **1. Diagnostic Signal**: When different PAM nodes $u$ in the same `slink` chain have **different weights** $w(u_1) \ne w(u_2)$, the old contribution $-w(u_j)$ at $r - d$ and the new contribution $+w(u_{j-1})$ at $r$ share the same start position $r - \text{len}(u_{j-1}) + 1$, so their net change at that start position is $w(u_{j-1}) - w(u_j) \ne 0$!
- **2. Combinatorial Word Invariant**: Notice what just happened! Even when weights $w(u)$ are arbitrary, for every $j \in \{2, \dots, k\}$ in a single `slink` chain $\{u_1, \dots, u_k\}$ with step $d = \text{diff}(u_1)$, the start position $r - \text{len}(u_{j-1}) + 1$ forms an **arithmetic progression of indices** with step $d$, or in LCT `access(pos[r])` on the HLD of the PAM Fail Tree, each solid splay has a uniform last-occurrence right endpoint $t$!
  Even better: if $w(u) = f(\text{len}(u))$ is a polynomial in $\text{len}(u)$ (such as $\text{len}(u)$ or $\text{len}(u)^2$), what is $w(u_{j-1}) - w(u_j)$ along a `slink` chain of constant difference $d$?
  - For $w(u) = \text{len}(u)$: $w(u_{j-1}) - w(u_j) = \text{len}(u_{j-1}) - \text{len}(u_j) = d$ (a constant across the entire chain!).
  - Or for completely arbitrary node weights $w(u)$: using **LCT `access(pos[r])`** on the PAM Fail Tree, each splay represents a vertical chain of nodes with the **same** $\text{last}(u) = t$. Since a vertical chain in the PAM Fail Tree contains at most $O(\log N)$ `slink` chains, and each `slink` chain has at most $1$ heavy child in HLD or we simply notice that an LCT splay is a contiguous segment of a heavy path... Wait: can a vertical path in the PAM Fail Tree have $\Theta(N)$ nodes? Yes, inside a `slink` chain!
  - And if $w(u)$ is arbitrary, why can't a `slink` chain of length $\Theta(N)$ exist with arbitrary weights unless all nodes in the `slink` chain have period $d$?
  - Look at the start positions $t - \text{len}(u_j) + 1$ for $u_1, \dots, u_k$ in a single `slink` chain: their lengths are $\text{len}(u_1) - (j-1)d$, so their start positions are an arithmetic progression of step $d$!
  - Better yet: in `slink` telescoping, at step $r$, node $u_{j-1}$ moves to start position $s = r - \text{len}(u_{j-1}) + 1$, while node $u_j$ **leaves** that exact same start position $s = (r - d) - \text{len}(u_j) + 1$!
  - Wait: when will start position $s$ EVER change again in the future? Only when $u_{j-1}$ is visited again at its next occurrence $r_{\text{next}} = r + d$ (if the period continues) or later!
- **3. Reverse-Engineering Scratchpad**: For polynomial weights $w(u) = \text{len}(u)$ (sum of lengths of distinct palindromes in $S[l..r]$):
  Look at the telescoping sum of $\text{len}(u)$:
  - At $s_j = r - \text{len}(u_j) + 1$ ($1 \le j \le k-1$), the net weight change is $\text{len}(u_j) - \text{len}(u_{j+1}) = +d$, and at $s_k = r - \text{len}(u_k) + 1$ it is $+\text{len}(u_k)$.
  -Wait: instead of updating $k$ positions in the Fenwick tree, why not track the **last occurrence $t$ of each splay in LCT**, OR notice that a palindrome $u$ ending at $t$ contributes $\text{len}(u)$ if $t - \text{len}(u) + 1 \ge l$!
  - In LCT `access(pos[r])`, each splay on the PAM Fail Tree is a vertical path $\{v_1, \dots, v_m\}$ sharing a single right endpoint $t$. If we sort queries $(l, r)$ offline by $r$, when a splay with right endpoint $t$ is active, which nodes $v$ in that splay satisfy $t - \text{len}(v) + 1 \ge l \iff \text{len}(v) \le t - l + 1$?
  - Since $\text{len}(v)$ is strictly monotonic along any vertical path in the Fail Tree, the condition $\text{len}(v) \le t - l + 1$ is a **prefix of the vertical path**!
  - Read that again! A vertical path in the Fail Tree has strictly increasing $\text{len}(v)$ from top to bottom! Does that depend on `t - len(v) + 1` being a contiguous interval? **Wait**: if we maintain a Fenwick Tree over the **left endpoint $s = t - \text{len}(v) + 1$**, non-contiguous lengths are hard; EXCEPT in a `slink` chain $\{u_1, \dots, u_k\}$ (where $k$ can be $> 1$), **ALL nodes $u_2, \dots, u_{k}$ ALWAYS have the exact deterministic previous occurrence $r - d$**!
  -Wait: why did $u_2, \dots, u_k$ have previous occurrence $r - d$? Because $u_1$ occurred at $r$! That is true **independently of weights**!
  - Wait: if $u_j$ has arbitrary weight $w(u_j)$, then at step $r$, for $j = 2 \dots k$, $u_j$ moves its weight $w(u_j)$ from old start position $r - \text{len}(u_{j-1}) + 1$ to new start position $r - \text{len}(u_j) + 1$!
  - Notice that for every $j \in \{2, \dots, k\}$, the distance it moves its weight is **always $+d$** (from $r - \text{len}(u_j) + 1 - d$ to $r - \text{len}(u_j) + 1$)!
  - Even simpler: if we run LCT `access(pos[r])` where each LCT node is a **compressed `slink` chain** (or in standard LCT on PAM, why does a single `slink` chain ever get split in LCT? A `slink` chain $\{u_1, \dots, u_k\}$ has $u_2, \dots, u_{k}$ with only ONE child in the `slink` chain? No, $u_j$ can have other children outside the `slink` chain, which start *new* `slink` chains!).
  - Wait: if $w(u) = 1$ (count), telescoping inside each `slink` chain takes $O(1)$ point updates per chain! What if $w(u) = \text{len}(u)$? Wait: if we instead parameterize by the **longest occurrence inside $[l, r]$**, or notice that in any `slink` chain $\{u_1, \dots, u_k\}$ at right endpoint $t$, all nodes $u_2, \dots, u_k$ already had start positions $t - \text{len}(u_1) + 1, \dots, t - \text{len}(u_{k-1}) + 1$ at step $t - d$!
  - Actually, wait: in a `slink` chain $\{u_1, \dots, u_k\}$ with $k \ge 2$, why is $u_1 = S[r - \text{len}(u_1) + 1 .. r]$ periodic with period $d$? Because $u_1, u_2, \dots, u_{k-1}$ are all the SAME periodic run! In fact, $u_1$ can only be created when extending $u_2$ by the exact same period $d$! Thus, in the Fail Tree, for every $j \in \{1, \dots, k-2\}$, $u_j$ is the **unique** child of $u_{j+1}$ that has $\text{diff} = d$, and $u_1, \dots, u_{k-1}$ were created at consecutive multiples of $d$ during the first run of period $d$!
- **4. Boundary Pitfalls**: When $w(u) = 1$ (standard distinct palindrome count), `slink` telescoping gives $O(1)$ updates per chain ($O(\log N)$ total per step $r$). When $w(u)$ is arbitrary on the PAM Fail Tree and we only update **chain heads** or use LCT + Segment Tree over DFS order where we query for each splay $[top, bot]$ with right endpoint $t$ the sum of $w(v)$ for $v \in [top, bot]$ with $\text{len}(v) \le t - l + 1$, wait: if we maintain the active splays, there can be $\Omega(N)$ active splays across the whole tree! So how do we do arbitrary $w(u)$ in $O((N+Q)\log^2 N)$?
  Look at why $u_2, \dots, u_k$ moved from $r - d$ to $r$: for each $j \in \{2, \dots, k\}$, $u_j$'s previous occurrence was at $r - d$ **because $u_1$ occurred at $r$**, which means $u_2$ occurred at $r - d$!
  That means at step $r - d$, the node at the bottom of the chain was **at least $u_2$**!
  Wait: at step $r - d$, $u_2$ was updated from $r - 2d$ to $r - d$; at step $r - 2d$, $u_3$ was updated from $r - 3d$ to $r - 2d$...
  Follow each node $u_m$ backwards to when it was the **chain head**!
  In any `slink` chain $\{u_1, u_2, \dots, u_k\}$ where $u_1$ is the chain head at step $r$:
  - Where was the **entire chain** $\{u_2, \dots, u_k\}$ at step $r - d$? They were a suffix of the chain headed by some ancestor/descendant of $u_2$ at $r - d$, so at step $r - d$ their right endpoint was **already set to $r - d$**!
  - Wait: that means at step $r - 1$, $u_2, \dots, u_k$ do **NOT** have scattered right endpoints—they **ALL** have right endpoint $r - d$, so for each $j \in \{2, \dots, k\}$, its old start position is $(r - d) - \text{len}(u_j) + 1 = r - \text{len}(u_{j-1}) + 1$!
  - And look at that formula: the old start position of $u_j$ ($r - \text{len}(u_{j-1}) + 1$) depends ONLY on $r$ and $\text{len}(u_{j-1})$, **NOT on any historical timestamp $t_{\text{old}}$**!
  - Let that sink in! Because the old start position of $u_j$ ($2 \le j \le k$) is $r - \text{len}(u_{j-1}) + 1$ and the new start position of $u_j$ is $r - \text{len}(u_j) + 1$, the net change to the start-position array at step $r$ from $\{u_1, \dots, u_k\}$ is:
    - At old position $\text{last}_{r-1}(u_1) - \text{len}(u_1) + 1$: subtract $w(u_1)$.
    - For each $j \in \{1, \dots, k-1\}$, at position $r - \text{len}(u_j) + 1$: add $w(u_j) - w(u_{j+1})$!
    - At position $r - \text{len}(u_k) + 1$: add $w(u_k)$!
  - Look at the second bullet: for $j \in \{1, \dots, k-1\}$, we add $\Delta w(u_j) = w(u_j) - w(u_{j+1})$ at index $r - \text{len}(u_j) + 1$!
  - When $w(u) = 1$ (constant), $\Delta w(u_j) = 1 - 1 = 0$, so all $k - 1$ internal updates vanish identically!
  - When $w(u) = \text{len}(u)$, $\Delta w(u_j) = \text{len}(u_j) - \text{len}(u_{j+1}) = d$, so we add $+d$ at the arithmetic progression of indices $r - \text{len}(u_1) + 1, r - \text{len}(u_2) + 1, \dots, r - \text{len}(u_{k-1}) + 1$!

#### Problem 3A-28: `[ZH]` `[SDOI 2019 / ZJOI / NOI-Style] Palindrome Partition with Forbidden Lengths or Weight Constraints` (`CF 932G` + CDQ / Segment Tree over `slink` Chains)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^5$), partition $S$ into palindromes $P_1 P_2 \dots P_m$ where each palindrome must have length $\ge L_{\min}$ (or each step queries a subsegment of the `slink` chain).
- **1. Diagnostic Signal**: When only palindromes of length $\in [L_{\min}, L_{\max}]$ are allowed, we cannot take the entire `slink` chain sum $g[u]$ unconditionally.
- **2. Combinatorial Word Invariant**: In any `slink` chain $\{u_1, \dots, u_k\}$ with step $d = \text{diff}(u_1)$, all left endpoints $r - \text{len}(u_j)$ have the **same residue modulo $d$** ($\equiv r - \text{len}(u_1) \pmod d$) and form a contiguous interval of indices in the residue class! Moreover, as $r$ advances to $r + d$ along the same `slink` chain, the left endpoints of $\{u_2, \dots, u_k\}$ at step $r$ are **identical** to the left endpoints of $\{u_1, \dots, u_{k-1}\}$ at step $r - d$!
- **3. Reverse-Engineering Scratchpad**: Associate a dynamic array or monotonic queue / segment tree with each `slink` chain head (indexed by the invariant left endpoint $(r - \text{len}(u_j)) / d$), allowing $O(\log N)$ or $O(1)$ range queries over any length interval $[L_{\min}, L_{\max}]$ within the `slink` chain!
- **4. Boundary Pitfalls**: The invariant index of a transition inside a `slink` chain is its **left endpoint** $l = r - \text{len}(v)$, NOT its palindrome length $\text{len}(v)$ (since $\text{len}(v)$ increases by $d$ when $r$ increases by $d$, keeping $l = r - \text{len}(v)$ constant!).

#### Problem 3A-29: `[EN]` `ICPC World Finals / Universal Cup — Unique Palindromic Factorization & Minimum Palindromic Length` (`Ravsky / Frid–Puzynina–Zamboni / Borozdin–Kosolobov–Rubinchik–Shur`)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6$), find the **Palindromic Length** $\text{PL}(S)$ (minimum number of palindromes whose concatenation is $S$) and determine whether the minimum palindromic factorization of each prefix $S[1..r]$ is unique, in $O(N \log N)$ time.
- **1. Diagnostic Signal**: Computing both the minimum number of palindromes $dp[r]$ and the number of ways $\text{ways}[r]$ to achieve $dp[r]$ requires maintaining `(min_dp, sum_ways)` Semiring aggregations along `slink` chains.
- **2. Combinatorial Word Invariant**: The Semiring $(\min, +)$ over pairs $(\text{cost}, \text{ways})$ is associative and commutative, so `slink` DP maintains $g[u] = \bigoplus_{v \in \text{chain}(u)} (dp[r - \text{len}[v]], \text{ways}[r - \text{len}[v]])$ in $O(1)$ per chain using `g[fail[u]]` + the single new entry at $r - (\text{len}[\text{slink}[u]] + \text{diff}[u])$.
- **3. Reverse-Engineering Scratchpad**: Define the combine operator `(c1, w1) + (c2, w2)` returning `(c1, w1)` if $c_1 < c_2$, `(c2, w2)` if $c_2 < c_1$, and `(c1, min(2, w1 + w2))` (or modulo $P$) if $c_1 == c_2$. Run standard PAM `slink` DP with this operator in $O(N \log N)$ time.
- **4. Boundary Pitfalls**: Initialize $g[u] = (\infty, 0)$ for all nodes including $r_0, r_1$, and never combine $g[\text{fail}[u]]$ when $\text{diff}[u] \ne \text{diff}[\text{fail}[u]]$.

#### Problem 3A-30: `[ZH]` `UOJ / LOJ / QOJ — Persistent Tree PAM with Path Palindrome Queries` (`可持久化树上 PAM`)
- **Statement & Constraints**: Given a tree of $N \le 10^5$ nodes with characters on edges/vertices, support $Q \le 10^5$ queries: (1) attach a new leaf $v$ to existing vertex $p$ with character $c$, (2) given vertex $v$ and length $L$, find the longest palindromic suffix of the root-to-$v$ path of length $\le L$ and how many times it occurs on the root-to-$v$ path.
- **1. Diagnostic Signal**: Online leaf attachment creates a dynamic tree of strings; we must build the PAM persistently along root-to-$v$ paths without $O(N)$ fail chains or $O(|\Sigma|)$ node-copying if $|\Sigma|$ is large, and answer occurrence queries on a path prefix.
- **2. Combinatorial Word Invariant**:
  1. Using `quick_link[u][c]` (for $|\Sigma| \le 26$) or `slink`-skipping fail walk (Invariant 73.2.2, $O(\log N)$ worst-case with $O(1)$ space per node!), we find the fail-ancestor and transition for the new leaf $v$ in worst-case $O(1)$ or $O(\log N)$ time.
  2. Notice that the PAM Trie itself is **global and static/append-only**! Two different branches of the tree can share the exact same PAM node $u$! The only thing that depends on the tree vertex $v$ is:
     - Which PAM node $\text{pos}[v]$ corresponds to the longest palindromic suffix of $\text{path}(\text{root} \to v)$, and
     - For occurrence count on $\text{path}(\text{root} \to v)$: a PAM node $u$ is a palindromic suffix at depth $d$ on $\text{path}(\text{root} \to v)$ iff $\text{pos}[\text{anc}(v, d)]$ is in the **Fail-Tree subtree of $u$**!
- **3. Reverse-Engineering Scratchpad**: Because PAM nodes are uniquely identified by the palindrome string they represent, we do **NOT** need persistent `next[u][c]` pointers in the PAM! A single global PAM stores all distinct palindromes appearing on any root-to-node path!
  To count occurrences of palindrome $u$ along $\text{path}(\text{root} \to v)$: only if query (1) is offline (so Fail-Tree Euler tour $[\text{dfn}[u], \text{out}[u]]$ is known) do we maintain a Persistent Segment Tree over $\text{dfn}[\text{pos}[x]]$ along the tree paths; if query (1) is strictly online, each PAM node $u$ has a static `fail[u]` defined at the moment $u$ is first created, so the Fail Tree only grows by **leaf attachments** (`fail[new_u] = old_v`), which can be maintained via Euler-Tour / HLD or binary lifting + depth counts!
- **4. Boundary Pitfalls**: Realizing that the PAM Trie and Fail Tree are **shared across all branches of the character tree** (because `fail[u]` and `quick_link[u][c]` depend only on the palindrome $u$ itself, NEVER on the prefix of the path before $u$!) eliminates 90% of the complexity of "Persistent PAM"! The only state needed per tree vertex $v$ is the integer pointer `last[v]` and the root-to-$v$ character stack (maintained via binary lifting `up[v][k]` on the input tree to read the character at depth $\text{dep}[v] - \text{len}[u] - 1$ in $O(\log N)$ or $O(1)$ via Level Ancestor!).

#### Problem 3A-31: `[JA]` `AtCoder AGC / JOI — Palindromic Substrings on Run-Length Encoded (RLE) Strings` (`Compressed PAM / Manacher on RLE`, $N_{\text{total}} \le 10^{14}$, $M \le 10^5$ runs)
- **Statement & Constraints**: A string $S$ of length up to $10^{14}$ is given in Run-Length Encoding (RLE) as $M \le 10^5$ pairs $(c_1, k_1), (c_2, k_2), \dots, (c_M, k_M)$ with $c_i \ne c_{i+1}$. Count the total number of palindromic substrings (both with multiplicity and distinct) in $S$.
- **1. Diagnostic Signal**: $|S| \le 10^{14}$ forbids character-by-character Manacher or PAM.
- **2. Combinatorial Word Invariant**: Any palindrome $P$ in $S$ either:
  - Lies entirely within a single run $(c_i, k_i)$ (contributing $\binom{k_i + 1}{2}$ occurrences and $k_i$ distinct palindromes of letter $c_i$), OR
  - Spans across $2r + 1 \ge 3$ consecutive runs $(c_{i-r}, k_{i-r}) \dots (c_i, k_i) \dots (c_{i+r}, k_{i+r})$.
  Crucially, for a multi-run palindrome centered at the **entire middle run** $(c_i, k_i)$:
  - All internal runs $(c_{i-j}, k_{i-j})$ and $(c_{i+j}, k_{i+j})$ for $1 \le j < r$ must match in **both character AND exact run length**: $c_{i-j} == c_{i+j}$ and $k_{i-j} == k_{i+j}$!
  - Only the **outermost boundary runs** $(c_{i-r}, k_{i-r})$ and $(c_{i+r}, k_{i+r})$ only need $c_{i-r} == c_{i+r}$, where they can extend by up to $\min(k_{i-r}, k_{i+r})$ characters!
- **3. Reverse-Engineering Scratchpad**:
  1. For multiplicity count: add $\sum_{i=1}^M \binom{k_i + 1}{2}$ for single-run palindromes. Then run odd-center Manacher on the sequence of $M$ pairs $(c_i, k_i)$ (centered at run $i$, since a multi-run palindrome cannot be centered at the boundary *between* two runs $c_i \ne c_{i+1}$!). At the stopping boundary $r = \text{rad}[i]$ of the pair-Manacher at center $i$, if $c_{i-r} == c_{i+r}$, add $\min(k_{i-r}, k_{i+r})$!
  2. For distinct count: for each letter $c$, the maximum run length $\max_{c_i = c} k_i$ gives all single-run distinct palindromes; for multi-run distinct palindromes, build a PAM over the pair sequence $(c_i, k_i)$ where each boundary extension $(c, \le \min(k_{i-r}, k_{i+r}))$ records the maximum outer cap $\min(k_{i-r}, k_{i+r})$ achieved for that core PAM node! Time: $O(M \log M)$.
- **4. Boundary Pitfalls**: A multi-run palindrome can **never** be centered at the boundary between run $i$ and run $i+1$ because $c_i \ne c_{i+1}$ by definition of RLE! It must be centered at the exact midpoint of some middle run $(c_i, k_i)$ (utilizing all $k_i$ characters of run $i$).

#### Problem 3A-32: `[EN]` / `[ZH]` `QOJ / Universal Cup Grandmaster — Shortest Palindromic Completion & Substring Palindromic Border Queries`
- **Statement & Constraints**: Given $S[1..N]$ and $Q \le 2 \times 10^5$ queries $(l, r)$, find the length of the **longest palindromic prefix** and **longest palindromic suffix** of $S[l..r]$, and count how many palindromic prefixes of $S[l..r]$ have length $\ge \frac{1}{2}(r - l + 1)$.
- **1. Diagnostic Signal**: Need internal palindromic prefix/suffix of $S[l..r]$ in $O(\log N)$ time without binary lifting tables if memory is tight, plus counting large palindromic prefixes.
- **2. Combinatorial Word Invariant**: The palindromic suffixes of $S[l..r]$ are the Fail-Tree ancestors of $\text{pos}[r]$ of length $\le r - l + 1$. By Invariant 74.2.2, jumping `slink` chains from $\text{pos}[r]$ reaches the unique AP chain straddling $r - l + 1$ in $O(\log N)$ steps, and inside that AP chain with step $d = \text{diff}(u_1)$, the longest node of length $\le r - l + 1$ has length $L_{\max} = \text{len}(u_1) - \lceil \frac{\text{len}(u_1) - (r - l + 1)}{d} \rceil \cdot d$, and all nodes in that chain down to $\ge \frac{1}{2}(r - l + 1)$ are counted by simple division! Symmetrically on the PAM of $S^R$ for palindromic prefixes of $S[l..r]$.
- **3. Reverse-Engineering Scratchpad**: Build forward PAM on $S$ and backward PAM on $S^R$ with `diff` and `slink`. Answer each query in $O(\log N)$ arithmetic operations with $O(N)$ total memory.
- **4. Boundary Pitfalls**: When $\text{len}(u_1) > r - l + 1$, the ceiling division $\lceil (\text{len}(u_1) - (r - l + 1)) / d \rceil$ jumps to the first element in the AP chain of length $\le r - l + 1$; verify that this length is $> \text{len}(\text{slink}(u_1))$ (which is guaranteed because we stopped at the chain where $\text{len}(u_1) > r - l + 1 \ge \text{len}(\text{slink}(u_1))$!).

---

### 77.5 Quarantine Table of Excluded Pure-Template Problems (`R-3A-01` to `R-3A-10`)

Per `AGENTS.md` and `PLAN.md` (§2.2), pure template-validation problems whose primary task is copying a standard Manacher or PAM implementation are quarantined from the textbook ladders and logged below:

| Quarantine ID | Problem Source & Title | Reason for Quarantine |
| :--- | :--- | :--- |
| `R-3A-01` | **Library Checker — `Enumerate Palindromes`** | Bare Manacher radius output template; zero modeling or structural reduction. |
| `R-3A-02` | **Library Checker — `Eertree`** | Bare PAM construction template outputting parent/fail pointers of each node. |
| `R-3A-03` | **Luogu P3805 — `【模板】manacher`** | Bare longest palindromic substring length template. |
| `R-3A-04` | **Luogu P5496 — `【模板】回文自动机（PAM）`** | Bare online PAM template asking for $\text{dep}[\text{pos}[r]]$ at each prefix. |
| `R-3A-05` | **SPOJ `LPS` — Longest Palindromic Substring** | Direct Manacher template. |
| `R-3A-06` | **SPOJ `NUMOFPAL` — Number of Palindromes** | Direct sum of Manacher radii / PAM depths over the whole string ($N \le 1000$). |
| `R-3A-07` | **SPOJ `MSUBSTR` — Mirror Strings** | Direct Manacher max length + count of centers achieving max length. |
| `R-3A-08` | **CF 245H — Queries for Number of Palindromes** ($N \le 5000$) | Naive $O(N^2)$ 2D prefix-sum table over `is_pal[l][r]`; superseded by Tier 3 Problem `3A-20` ($N, Q \le 3 \times 10^5$). |
| `R-3A-09` | **HDU 3068 — 最长回文** | Duplicate bare Manacher template. |
| `R-3A-10` | **URAL / Timus 1960 — Palindromes and Super Abilities** | Bare online distinct palindrome count (`tot - 2` after each character append in PAM). |

---

## 78. Cohort 2 Wave 3A Verification & Handoff Summary

- **All 5 iterations (`Iter 73`–`Iter 77`) completed** following the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**.
- **Key Novel / Deep Structural Derivations Highlighted for Cohort 3 Cross-Comparison**:
  1. **Intrinsic Preceding-Character Proof for `quick_link[u][c]`** (§73.2.1) & **Alphabet-Free $O(\log N)$ `slink`-Skipping Fail Walk** (§73.2.2) proving via periodicity that all internal nodes of an AP chain share the exact same preceding character $S[r - \text{len}(u_2) - 1]$.
  2. **Unique Vanishing Palindrome Theorem & `max_pref` / `max_suff` Duality for General Deque PAM (`pop_front` / `pop_back`)** (§73.2.4 & §73.3.2), proving that deleting a boundary character can destroy at most one distinct palindrome ($u = \text{last\_back}$) because every proper fail-ancestor $v$ has a reflected prefix occurrence inside $u$ ending strictly before $R$, and showing why PAM trie nodes never need to be physically unlinked.
  3. **Midpoint Decoupling Identity ($m_{\text{odd}} = \lfloor(l+r)/2\rfloor$, $m_{\text{even}} = \lfloor(l+r-1)/2\rfloor$)** (§74.2.3) reducing the 3-way clipped Manacher sum $\sum_{c=l}^r \min(\text{rad}[c], c - l + 1, r - c + 1)$ into two independent 2-way minimums for $O((N+Q)\log N)$ range palindrome multiplicity queries.
  4. **Periodic Suffix Telescoping Cancellation Theorem for Range Distinct Palindromes** (§75.2.2 & §75.3), proving from border minimality that every non-head node $u_j$ ($j \ge 2$) in a `slink` chain had its previous occurrence at $r - d$, so its old start position $(r - d) - \text{len}(u_j) + 1 = r - \text{len}(u_{j-1}) + 1$ **cancels telescopically** with $u_{j-1}$'s new start position at $r$, leaving only **one `-1` and one `+1` update per `slink` chain** and eliminating LCT entirely!
  5. **Droubay–Pirillo Rich Words Return Theorem, Fixed-Point-Free $\theta$-Palindrome Parity, Greedy Shortest Even-Palindrome Lemma (`CF 1827C`), Shared-Trie Persistent Tree PAM Insight, RLE Pair-Manacher/PAM, and the 5-Element KMP Restoration Counterexample $\pi = [0, 1, 0, 1, 1]$** (§76 & §77).
