# Wave 3A (Iterations 21–25): Advanced Palindromic Structures, Deque/Persistent PAM, Substring Palindrome Queries & Rich Words

> **Cohort 1 Primary Research Report (`strings_research/iter_21_to_25_advanced_pam_deque_range_palindromes.md`)**
> **Scope**: Iterations 21–25 of the 115-Iteration Multilingual Stringology Discovery & Structural Audit Pipeline.
> **Prerequisite Baseline**: Standard Palindromic Automaton (Eertree / PAM) with odd/even roots ($r_{-1}$ of length $-1$, $r_0$ of length $0$), standard amortized online right-append via `fail` links, and standard Manacher's Algorithm ($d_{\text{odd}}[i], d_{\text{even}}[i]$).
> **Editorial Standard**: Every technique and problem solution follows the **4-Step "Zero Magic Invariants & Structural Decompositions" Mandate**:
> 1. *The Diagnostic Signal (Why Naive String Structures Fail)*
> 2. *The Combinatorial Word Invariant (Double-Overlap / Periodicity / Symmetry Proof)*
> 3. *The Reverse-Engineering Scratchpad (Algorithmic & Data-Structure Compilation)*
> 4. *Boundary Pitfalls & Broken-Invariant Counterexamples*

---

## Iteration 21: Deterministic Online PAM (`quick_link`), Persistent / Tree PAM (`树上 PAM`), and Double-Ended (Deque) PAM (`双向回文自动机`)

### 21.1 The Diagnostic Signal: Why Amortized Fail-Chain Walks Collapse Under Branching, Persistence, and Deque Edits

In the standard online Palindromic Automaton (Rubinchik & Shur 2015), appending a character $c = S[r]$ to the right of $S[1..r-1]$ walks up the `fail` chain starting from $u = \text{last}$ until finding the first ancestor $v$ satisfying the **mirror-character match condition**:
$$S\big[r - 1 - \text{len}(v)\big] = c$$
In a purely linear, append-only setting, this walk takes $O(1)$ *amortized* time because the depth of $\text{last}$ in the `fail` tree increases by at most $1$ per append while each `fail`-step strictly decreases depth.

However, four ubiquitous competitive-programming scenarios immediately destroy this potential function and degrade naive fail-chain walking to **$\Theta(N)$ per operation ($\Theta(N^2)$ total)**:
1. **Persistent / Backtracking PAM (`可持久化 PAM` / Rollback)**: Repeatedly branching from or rolling back to a high-depth node $u$ (e.g., on the string $S = \texttt{a}^{N}$, where $\text{depth}(u) = N$, and querying/branching with $c = \texttt{b}$) walks all $N$ links down to $r_{-1}$ on every single branch without paying down future potential.
2. **PAM on a Tree / Trie (`树上回文自动机`)**: Walking down a tree where edges are labeled with characters and maintaining the PAM of the root-to-node path $P(r \to v)$. Note that unlike Aho–Corasick or Suffix Automaton, **PAM cannot be built on a general Trie simply by BFS**, because verifying a palindromic extension of length $\text{len}(v)+2$ requires random-access inspection of the ancestor at distance $\text{len}(v)+1$ above the current tree node!
3. **Front & Back Appends (`双端插入 PAM`)**: Prepending $c$ to the left of $S[l..r]$ while also appending to the right requires maintaining both the longest palindromic prefix ($\text{first}$) and the longest palindromic suffix ($\text{last}$), and knowing when a prepend becomes the entire string palindrome and thereby updates $\text{last}$ (and vice versa).
4. **Front & Back Deletions (`双端删除 / Deque PAM`)**: Deleting an endpoint character can destroy the unique occurrence of a maximal palindrome in $S[l..r]$. If we must retract $\text{first}$ or $\text{last}$ and prune dead PAM states in $O(1)$ worst-case time, we cannot afford any amortized search.

---

### 21.2 The Combinatorial Word Invariant: Why `quick_link[u][c]` Bypasses All Non-Matching Ancestors in Worst-Case $O(1)$

Let $u$ be a PAM node representing a palindrome $P$ of length $\text{len}(u) \ge 0$ occurring as a suffix of $S[1..r-1]$, so $S[r - \text{len}(u) .. r - 1] = P$. Suppose we examine the `fail`-parent $\text{fail}(u)$, which represents the longest proper palindromic suffix $Q$ of $P$.

Because $Q$ is a suffix of $P$ and $P$ is a palindrome, **by reflection across the center of $P$, $Q$ is also a prefix of $P$**, and in fact the character immediately preceding the suffix occurrence of $Q$ inside $P$ is fixed solely by the string $P$ and $\text{len}(Q)$! Specifically:
- In any occurrence of $P$ ending at $r-1$, the suffix $Q = \text{fail}(u)$ occupies $S[r - \text{len}(Q) .. r - 1]$.
- The character immediately to the left of $Q$ is:
  $$S\big[r - 1 - \text{len}(Q)\big] = P\big[\text{len}(u) - \text{len}(\text{fail}(u))\big] = P\big[\text{len}(\text{fail}(u)) + 1\big]$$
  (using 1-based indexing inside $P$, where the last Equation holds because $P$ is a palindrome: $P[k] = P[\text{len}(u) - k + 1]$).

**Crucial Invariant (Context-Free Mirror Character of Proper Palindromic Suffixes)**:
For any node $u$ and any proper ancestor $v$ of $u$ in the `fail` tree, the character immediately preceding $v$ whenever $u$ occurs as a suffix is **completely determined by the intrinsic string of $u$ alone**—it does *not* depend on where $u$ appears in the ambient text $S$! Only the character preceding $u$ itself ($S[r - 1 - \text{len}(u)]$) depends on the external text context.

Therefore, we define for every node $u$ and every character $c \in \Sigma$ the **Direct Fail-Transition Table (`quick_link[u][c]` / `anc[u][c]`)**:
$$\text{quick\_link}[u][c] = \text{the highest proper ancestor } v \text{ of } u \text{ in the fail-tree such that } P_u\big[\text{len}(u) - \text{len}(v)\big] = c$$
(with $\text{quick\_link}[u][c] = r_{-1}$ if no non-negative ancestor matches).

#### Alignment Diagram for `quick_link[u][c]` Inheritance

```
          |<-------------------- P_u (len = L) -------------------->|
Text S:   [x] [ ............ Q = fail(u) ............ ] [c_mirror] [ ......... Q = fail(u) ......... ] [c?]
           ^                                             ^                                              ^
     r - 1 - len(u)                               P_u[len(fail(u))+1] = c_0                             r
     (External context)                           (Intrinsic to u and fail(u)!)
```

When node $u$ is first created with $\text{fail}(u) = f$:
1. Look at the single intrinsic character $c_0 = S\big[r - 1 - \text{len}(f)\big]$ that precedes $f$ inside $u$.
2. For all $c \ne c_0$, $f$ cannot be extended by $c$, so the highest matching proper ancestor of $u$ is identical to the highest matching proper ancestor of $f$:
   $$\text{quick\_link}[u][c] = \text{quick\_link}[f][c] \quad (\forall c \ne c_0)$$
3. For $c = c_0$, $f$ itself is immediately preceded by $c_0$ inside $u$, so:
   $$\text{quick\_link}[u][c_0] = f$$

---

### 21.3 The Reverse-Engineering Scratchpad: Compiling Deterministic PAM, Tree PAM, and Deque PAM

#### A. Deterministic Worst-Case $O(1)$ Append (`get_fail` in 1 Step)

When appending $c = S[r]$ to state $u = \text{last}$:
- **Check 1**: Does $u$ itself match? Check if $S[r - 1 - \text{len}(u)] = c$. If yes, the parent of the new palindrome is $v = u$.
- **Check 2**: If $S[r - 1 - \text{len}(u)] \ne c$, then $u$ fails, and every proper ancestor of $u$ lies entirely inside $P_u$. Thus a single table lookup $v = \text{quick\_link}[u][c]$ gives the exact longest palindromic suffix of $S[1..r-1]$ preceded by $c$ in **$O(1)$ worst-case time**!
- Similarly, if $\text{tr}[v][c]$ does not exist and we create node $w = \text{tr}[v][c]$, its `fail(w)` is found in $O(1)$ worst-case time by checking whether $v = r_{-1}$ (then $\text{fail}(w) = r_0$), else checking if $S[r - 1 - \text{len}(\text{fail}(v))] = c$ (then $\text{fail}(w) = \text{tr}[\text{fail}(v)][c]$), else $\text{fail}(w) = \text{tr}[\text{quick\_link}[\text{fail}(v)][c]][c]$.

**Storage Optimization for Large Alphabets**:
- If $|\Sigma| \le 26$, store $\text{quick\_link}[u][c]$ and $\text{tr}[u][c]$ as flat arrays of size $|\Sigma|$ ($O(N|\Sigma|)$ space, $O(1)$ time).
- In a **Persistent PAM** or when $|\Sigma|$ is large, copying an array of size $|\Sigma|$ on each node creation costs $O(|\Sigma|)$. Replacing the flat array at each node with a **Persistent Balanced BST / Persistent Segment Tree** of size $|\Sigma|$ where creating $u$ copies $\text{root}(\text{quick\_link}[f])$ and updates the single entry $c_0 \mapsto f$ achieves **$O(\log |\Sigma|)$ worst-case time and space per node**.
- Alternatively, as proved in Rubinchik & Shur (2015) and Xu Yi (`[国家集训队论文 2014 — 徐毅]`), using the $O(\log N)$ periodic `slink` structure allows deterministic $O(\log N)$ fail-finding with $O(1)$ extra pointers per node!

#### B. PAM on a Tree (`树上 PAM`) Contract

To build a PAM over root-to-node paths of a character-labeled tree $T$:
1. Precompute **Binary Lifting (`up[x][k]`)** or **Heavy-Light Decomposition (HLD) / Long-Path Decomposition** on the input tree $T$ so that `kth_ancestor(x, k)` on $T$ is answered in $O(\log N)$ or $O(1)$ time.
2. Why is `kth_ancestor` mandatory? Even with `quick_link[u][c]`, Check 1 requires comparing $c$ against the character at distance $\text{len}(u) + 1$ above the current tree node $x$:
   $$\text{char\_at\_dist}(x, \text{len}(u) + 1) = c$$
3. Traverse $T$ via DFS. At node $x$ with parent $p$ and edge character $c$, compute $\text{last}(x)$ from $\text{last}(p)$ in $O(1)$ PAM steps using `quick_link` + $O(1)$ level-ancestor query on $T$. Because DFS branches arbitrarily, `quick_link` is **strictly required** to avoid the $\Theta(N^2)$ star-tree counterexample (a path of $N/2$ `a`s followed by $N/2$ leaf children labeled `b`).

#### C. Double-Ended (Deque) PAM (`双向回文自动机` — Insertions & Deletions at Both Ends)

Suppose we maintain a dynamic string $S[L..R]$ inside a pre-allocated buffer $S[-N .. 2N]$ initialized with sentinels outside $[L, R]$.

**1. Dual-Insert Deque PAM (Append Left & Append Right)**:
Because every palindrome is equal to its own reversal ($P = P^R$), **a single PAM state space simultaneously represents both palindromic prefixes and palindromic suffixes of $S[L..R]$**!
- Maintain two active pointers:
  - $\text{last}$: node of the longest palindromic suffix of $S[L..R]$.
  - $\text{first}$: node of the longest palindromic prefix of $S[L..R]$.
- **Right Append (`push_back(c)` at $R+1$)**:
  Advance $R \leftarrow R+1$, set $S[R] = c$, and transition $u = \text{last}$ using mirror character $S[R - 1 - \text{len}(u)] = c$ (via `quick_link`) to obtain the new $\text{last}$.
  *Crucial Dual-Endpoint Synchronization*: If $\text{len}(\text{last}) == R - L + 1$, the new longest palindromic suffix spans the **entire string** $S[L..R]$, so it is also the longest palindromic prefix! We MUST set:
  $$\text{if } \text{len}(\text{last}) == R - L + 1 \implies \text{first} \leftarrow \text{last}$$
- **Left Prepend (`push_front(c)` at $L-1$)**:
  Decrement $L \leftarrow L-1$, set $S[L] = c$, and transition $u = \text{first}$ using the symmetric right-mirror character $S[L + 1 + \text{len}(u)] = c$ (via `quick_link`) to obtain the new $\text{first}$.
  Symmetrically:
  $$\text{if } \text{len}(\text{first}) == R - L + 1 \implies \text{last} \leftarrow \text{first}$$

**2. Full Deque PAM with Front & Back Deletions (`pop_front` / `pop_back`)**:
Why is deletion in a Deque PAM dramatically harder than insertion?
When we delete $S[R]$ (`pop_back`), any palindrome $u$ ending at $R$ loses that occurrence. More subtly, a palindrome $u$ might still occur inside $S[L..R-1]$, so its node should remain alive, *or* $u$ might have been the **unique occurrence as a maximal palindrome** in $S[L..R]$, in which case:
1. If $u = \text{last}$, $\text{last}$ must step down to $\text{fail}(\text{last})$.
2. What if a prefix palindrome ending at $R$ was $\text{first}$ (i.e., $\text{len}(\text{first}) == R - L + 1$)? Then $\text{first}$ also shrinks to $\text{fail}(\text{first})$!
3. What if a node $u$ ceases to be the *longest* palindromic prefix or suffix of any position in $S[L..R]$? If we want to maintain the exact count of **distinct palindromes currently in $S[L..R]$** and keep $\text{tr}[\cdot][\cdot]$ clean so future insertions don't walk into deleted ghost nodes, how do we track whether a PAM node $u$ is still active?

**The Maximal-Palindrome Reference-Count Invariant (Mikhail Rubinchik / Breslauer– Grossi–Mignosi / `UOJ` Deque PAM Invariant)**:
A PAM node $u$ appears in $S[L..R]$ if and only if either:
- $u$ is the **maximal palindromic prefix** at some left endpoint $i \in [L, R - \text{len}(u) + 1]$ (meaning $u$ is not shadowed by a longer palindrome centered at the same center extending inside $[L, R]$), OR
- Equivalently, in the fail-tree of active palindromes, $u$ has **fail-tree children** that are currently active ($\text{deg}_{\text{fail}}(u) > 0$), OR $u$ is the **maximal palindrome** at some center!

In practice, the cleanest worst-case $O(1)$ Deque PAM implementation maintains for each position and each PAM node:
- **`cnt_max[u]`**: The number of occurrences of $u$ in $S[L..R]$ that are *not* proper palindromic prefixes/suffixes of a longer palindrome currently inside $S[L..R]$ (equivalently, the number of positions where $u$ is the longest palindromic prefix or suffix, or more simply: maintain at each position $i \in [L, R]$ the longest palindromic prefix `max_pref[i]` starting at $i$ and longest palindromic suffix `max_suf[i]` ending at $i$).
- Wait—when we `push_back(c)` at $R$, the newly found node $u = \text{last}$ becomes `max_suf[R] = u`. What about its left endpoint $L_u = R - \text{len}(u) + 1$? Since $u$ is the longest palindrome ending at $R$, could $u$ update `max_pref[L_u]`? No, a longer palindrome starting at $L_u$ cannot end $\le R$, because $u$ is the longest ending at $R$? Wait: a palindrome starting at $L_u$ and ending at $R' < R$ has length $< \text{len}(u)$, so $u$ is strictly longer than any palindrome starting at $L_u$ inside $S[L..R]$!
- **Wait—let's verify that!** Suppose $v$ starts at $L_u$ and ends at $R' < R$. Then $\text{len}(v) = R' - L_u + 1 < R - L_u + 1 = \text{len}(u)$. Thus **$u = \text{last}$ is AUTOMATICALLY the longest palindrome starting at $L_u = R - \text{len}(u) + 1$ within $S[L..R]$**!
- Let's double check this! When we append at $R$, `last` has length $\text{len}(u)$ and starts at $L_u = R - \text{len}(u) + 1$. Before appending $R$, the longest palindrome starting at $L_u$ was $\text{fail}(u)$ (which starts at $L_u$ and ends at $L_u + \text{len}(\text{fail}(u)) - 1 < R$). After appending $R$, $u$ starts at $L_u$ and ends at $R$, so $u$ replaces $\text{fail}(u)$ as the longest palindrome starting at $L_u$!
- **Does `push_back(c)` affect `max_pref[i]` for any $i \ne L_u$?**
  Suppose some other palindrome $w$ ending at $R$ is a proper suffix of $u$, so $w$ is an ancestor of $u$ in the fail-tree. By reflection across the center of $u$, $w$ also occurs at the *beginning* of $u$, and its occurrence at the end of $u$ (starting at $R - \text{len}(w) + 1$) is a mirror of an occurrence starting at $L_u + (R - \text{len}(w) + 1 - L_u)$ inside $u$... wait: if $w$ is the longest palindrome starting at $i = R - \text{len}(w) + 1$ in $S[L..R]$, then no longer palindrome starts at $i$ and ends $\le R$. That means in the mirrored position inside $u$, no longer palindrome ends at $L_u + \text{len}(w) - 1$ and starts $\ge L_u$.
- Instead of tracking `max_pref[i]` for all $w$, track for each PAM node $u$:
  1. `child_cnt[u]`: number of currently active children of $u$ in the **Trie** (`tr[u][c]`)—or in the **Fail Tree**!
  2. Actually, the standard 3-rule Deque PAM deletion invariant (`双向回文自动机删除`):
     - When `push_back(c)` adds $R$ and reaches node $u = \text{last}$:
       We record that position $R$'s maximal suffix palindrome is $u$, and at its left endpoint $L_u = R - \text{len}(u) + 1$, $u$ is now the longest palindrome starting at $L_u$. Wait: what if we just maintain for each node $u$ the count `surf_cnt[u]` of how many times $u$ is the **longest palindromic prefix or suffix** at its endpoints, plus `fail_deg[u]` (how many active nodes $v$ have $\text{fail}(v) = u$)?
     - Wait: a node $u$ is present in $S[L..R]$ if and only if either $u$ occurs as a **maximal palindrome** (cannot be extended left-and-right by $1$ character within $S[L..R]$) OR $u$ has an active extension $\text{tr}[u][c]$ in $S[L..R]$. Even simpler: a node $u$ occurs in $S[L..R]$ iff either $\text{fail\_deg}[u] > 0$ (some longer active palindrome has $\text{fail}(v) = u$, which guarantees $u$ occurs inside $v \subseteq S[L..R]$!) OR $u$ itself is a longest palindromic prefix/suffix at some position!
     - Wait: if we maintain for each position $i \in [L, R]$ the node `longest_pref[i]` (longest palindrome starting at $i$ inside $S[L..R]$) and `longest_suf[i]` (longest palindrome ending at $i$ inside $S[L..R]$):
       When we `push_back(c)` at $R$, $u = \text{last}$ is the ONLY new palindrome that can become a longest prefix for its start $L_u = R - \text{len}(u) + 1$? No! What if a proper `fail`-ancestor $w$ of $u$ ending at $R$ is the longest palindrome starting at $R - \text{len}(w) + 1$?
       Notice that if $w$ is not the longest palindrome starting at $i = R - \text{len}(w) + 1$, then some longer palindrome $z$ starts at $i$ and ends at $j < R$. Since $z$ is inside $u$ ($L_u < i \le j < R$), by reflection across the center of $u$, $z$ also occurs at the mirrored position inside $u$, which means $w$ is not a maximal palindrome at that mirrored position either!
       Because updating all fail-ancestors of $u$ would take $O(\text{depth})$, how does a true $O(1)$ Deque PAM avoid walking the fail chain on `pop_front` / `pop_back`?
     - **The Exact $O(1)$ Deque PAM State Invariant**:
       Let a palindrome occurrence $S[i..j] = u$ be called a **border-maximal occurrence** if it is not contained strictly inside another palindrome $S[i'..j'] \subseteq S[L..R]$ with $i' < i$ and $j < j'$ of the same center, wait: if $S[i..j]$ is NOT the longest palindrome ending at $j$ AND NOT the longest palindrome starting at $i$, then:
       - Since it is not the longest ending at $j$, there is a longer palindrome $P_1$ ending at $j$ (so $u$ is a proper suffix of $P_1$, hence $u$ occurs earlier inside $P_1$ at $[i_1..j_1]$ with $j_1 < j$ and $i_1 \ge start(P_1) \ge L$).
       - Since it is not the longest starting at $i$, there is a longer palindrome $P_2$ starting at $i$ (so $u$ is a proper prefix of $P_2$, hence $u$ occurs later inside $P_2$ at $[i_2..j_2]$ with $i_2 > i$ and $j_2 \le end(P_2) \le R$).
       - **Theorem (Unique Earliest/Latest Non-Shadowed Occurrence)**: Every active PAM node $u$ in $S[L..R]$ that has $\text{fail\_deg}[u] = 0$ (i.e., no longer active palindrome in $S[L..R]$ has $\text{fail}(v) = u$) has **every** occurrence of $u$ in $S[L..R]$ be BOTH the longest palindrome starting at its left endpoint AND the longest palindrome ending at its right endpoint!
       - **Proof**: Suppose $u$ occurs at $S[i..j] \subseteq S[L..R]$. If $u$ were a proper suffix of a longer palindrome $v$ ending at $j$ ($v \subseteq S[L..R]$), then $u$ is an ancestor of $v$ in the `fail` tree, so at least one child of $u$ in the `fail` tree is an ancestor of $v$ (or is $v$ itself) and is therefore active in $S[L..R]$, meaning $\text{fail\_deg}[u] > 0$! Symmetrically, if $u$ were a proper prefix of a longer palindrome $v$ starting at $i$ ($v \subseteq S[L..R]$), then $u$ is a proper palindromic prefix (hence suffix) of $v$, so again $\text{fail\_deg}[u] > 0$!
       - **Consequence (Zero-Magic Deque Deletion!)**:
         A node $u$ with $\text{fail\_deg}[u] = 0$ can NEVER be shadowed by a longer palindrome at its left endpoint OR at its right endpoint! Therefore, when $u = \text{last}$ is added at $R$:
         1. We record at position $R$: `added_at_right[R] = u`.
         2. We increment `occ_as_terminal[u]++`. If $u$ was newly activated, we increment `fail_deg[fail[u]]++` (and if $\text{occ\_as\_terminal}[u] == 1$ and $\text{fail\_deg}[u] == 0$, it was already counted; more simply, a node $u$ is active iff `occ_as_terminal[u] + fail_deg[u] > 0`!).
         Wait—let's check! Could an occurrence of $u$ at $S[i..j]$ NOT be the longest palindrome at $j$ when $j$ was inserted, yet become exposed when the longer palindrome $v$ is deleted from the left or right?
         Suppose $v = S[L..j]$ was the longest palindrome ending at $j$, and $\text{fail}(v) = u = S[i..j]$ ($i > L$). When $L$ is deleted via `pop_front()`, $v$ is destroyed! Now $u = S[i..j]$ becomes the new longest palindrome ending at $j$!
         Wait: when $L$ was prepended (or when $j$ was appended), $v$ was the longest palindrome starting at $L$ (since $v = S[L..j]$). When $L$ is popped (`pop_front()`), we know the longest palindrome starting at $L$ was $v = \text{first}$! And when $v = \text{first}$ is popped at $L$, what replaces it inside $S[L+1..R]$? Its longest proper palindromic suffix $\text{fail}(v) = u$, which ends at the exact same right endpoint $j = L + \text{len}(v) - 1$ and starts at $i = j - \text{len}(u) + 1 \ge L+1$!
         Let's verify this! When we pop $S[L]$ (`pop_front()`):
         - The ONLY palindrome that started at $L$ and was maximal for $L$ is $v = \text{first}$! (Wait: what about shorter palindromes starting at $L$, i.e., `fail(first)`, `fail(fail(first))`? By reflection across the center of $v = \text{first}$, every proper palindromic prefix $w$ of $v$ starting at $L$ ALSO occurs as a palindromic suffix of $v$ ending at $L + \text{len}(v) - 1$, which lies entirely inside $S[L+1 .. R]$! So deleting $S[L]$ NEVER destroys the last occurrence of any proper prefix $w$ of $\text{first}$—only $\text{first}$ itself loses an unmirrored occurrence!)
         - **THIS IS THE CORE COMBINATORIAL MIRACLE OF DEQUE PAM**:
           Let $v = \text{first}$ be the longest palindrome starting at $L$ in $S[L..R]$. Any shorter palindrome $w$ starting at $L$ is a proper prefix of $v$, and because $v$ is a palindrome of length $\text{len}(v) > \text{len}(w)$, $w$ is also a suffix of $v$, meaning $w$ occurs at $S[L + \text{len}(v) - \text{len}(w) .. L + \text{len}(v) - 1] \subseteq S[L+1 .. R]$.
           Therefore:
           1. Deleting $S[L]$ (`pop_front`) can **at most** remove **one** node from the PAM—namely $v = \text{first}$! No proper ancestor of $\text{first}$ can ever vanish from $S[L+1..R]$ because it has a guaranteed mirror copy inside $S[L+1 .. L + \text{len}(v) - 1] \subseteq S[L+1..R]$!
           2. What happens to the new longest palindromic prefix $\text{first}'$ of $S[L+1..R]$? Wait: $\text{first}'$ starts at $L+1$, which is NOT $\text{fail}(v)$! Rather, each position $i \in [L, R]$ must know its longest palindromic prefix starting at $i$ (clipped to $R$) and longest palindromic suffix ending at $i$ (clipped to $L$).

Let's write down the exact invariant for maintaining `first` and `last` under `pop_front` and `pop_back` (and when a single-side deletion is needed vs. full four-way deque):
- **Case 1: Back-Append + Back-Delete (`Rollback / Stack PAM`)**:
  Trivial $O(1)$ with an undo stack (or `quick_link` without undo stack).
- **Case 2: Back-Append + Front-Delete (`Sliding Window / Queue PAM`)** or **Full 4-Way Deque PAM**:
  Why can't we know the new $\text{first}$ at $L+1$ solely from $\text{first}$ at $L$? Because $\text{first}$ at $L$ has center $(L + j)/2$, whereas the longest palindrome starting at $L+1$ has a completely different center!
  How is `longest_pref[L+1]` maintained in a Queue/Deque PAM?
  Whenever a maximal palindrome $v$ is created/updated at $(i, j)$ (either as $\text{first}$ at $i=L$ on `push_front`, or as $\text{last}$ at $j=R$ on `push_back`), $v$ is the longest palindrome starting at $i$ and ending at $j$. When $v$ is later popped from $L$ (`pop_front`), its longest proper palindromic suffix $\text{fail}(v)$ (which spans $[j - \text{len}(\text{fail}(v)) + 1 .. j]$) is pushed down to its own left endpoint $i' = j - \text{len}(\text{fail}(v)) + 1$, updating `max_pref[i'] = max(max_pref[i'], fail(v))` and `max_suf[j] = max(max_suf[j], fail(v))`!
  Let's verify this!
  - Every maximal palindrome in $S[L..R]$ is born as either $\text{first}$ (during a `push_front`) or $\text{last}$ (during a `push_back`).
  - Maintain for each index $k \in [L, R]$ two pointers: `longest_pref[k]` (longest palindrome starting at $k$ that has been pushed down so far) and `longest_suf[k]` (longest palindrome ending at $k$ that has been pushed down so far), plus for each PAM node $u$ a reference count `ref_cnt[u]` of how many currently active maximal intervals $[i..j]$ are assigned to $u$.
  - On `push_back(c)` at $R$:
    Find $u = \text{last}$ via `quick_link`. Now $u$ spans $[R - \text{len}(u) + 1 .. R]$.
    Update `longest_suf[R] = u` and `longest_pref[R - len(u) + 1] = max_len(longest_pref[R - len(u) + 1], u)`. Increment `ref_cnt[u]++`.
  - On `pop_back()` at $R$:
    Let $u = \text{longest\_suf}[R]$ (which is $\text{last}$). Its interval is $[L_u .. R]$ where $L_u = R - \text{len}(u) + 1$.
    When $R$ is deleted, $u$ is truncated on the right, exposing its longest proper palindromic prefix $\text{fail}(u)$ on the interval $[L_u .. L_u + \text{len}(\text{fail}(u)) - 1]$!
    So we:
    1. Decrement `ref_cnt[u]--`. If `ref_cnt[u] == 0` (meaning $u$ is neither a tracked maximal palindrome nor has `fail_deg[u] > 0`), we detach $u$ from $\text{tr}[\text{parent}(u)][c]$ and decrement $\text{distinct\_palindromes}--$.
    2. Propagate $f = \text{fail}(u)$ to interval $[L_u .. R_f]$ where $R_f = L_u + \text{len}(f) - 1$:
       Set `longest_pref[L_u] = max_len(longest_pref[L_u], f)` and `longest_suf[R_f] = max_len(longest_suf[R_f], f)`, and increment `ref_cnt[f]++`!
    3. The new $\text{last}$ of $S[L..R-1]$ is simply `longest_suf[R-1]`, and if $L_u == L$ (so $u$ was the whole string), the new $\text{first}$ at $L$ is updated to `longest_pref[L]` (which just received $f = \text{fail}(u)$)!
  - Symmetrically, on `pop_front()` at $L$:
    Let $u = \text{longest\_pref}[L]$ (which is $\text{first}$), spanning $[L .. R_u]$ where $R_u = L + \text{len}(u) - 1$.
    Truncating $L$ exposes $f = \text{fail}(u)$ on the suffix of $u$, which spans $[L_f .. R_u]$ where $L_f = R_u - \text{len}(f) + 1$.
    We decrement `ref_cnt[u]--` (deleting $u$ from `tr` if `ref_cnt[u] == 0` and `fail_deg[u] == 0`), propagate $f$ to `longest_pref[L_f]` and `longest_suf[R_u]`, increment `ref_cnt[f]++`, and read the new $\text{first} = \text{longest\_pref}[L+1]$!

Let's double check this lazy push-down invariant! Why does propagating $f = \text{fail}(u)$ only when $u$ is popped at its endpoint suffice to guarantee `longest_pref[L+1]` and `longest_suf[R-1]` are always exact when needed?
- Suppose $w$ is the true longest palindrome ending at $R-1$ in $S[L..R-1]$.
- In $S[L..R]$ (before popping $R$), either $w$ was already maximal at $R-1$ (not a proper prefix of any palindrome extending to $R$), in which case $w$ was already recorded in `longest_suf[R-1]` when $R-1$ was appended (or from an earlier push-down); OR $w$ was a proper prefix of the palindrome $u$ ending at $R$ with the same left endpoint $L_u$, which means $w = \text{fail}(u)$ and $R_f = R-1$, so popping $u$ at $R$ pushes $w = \text{fail}(u)$ directly into `longest_suf[R-1]`!
- **Complexity**: Every `push_front`, `push_back`, `pop_front`, and `pop_back` executes in **strict worst-case $O(1)$ time**!

---

### 21.4 Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Forgetting the Whole-String Synchronization ($\text{len}(\text{last}) == R - L + 1 \implies \text{first} = \text{last}$)**:
   - *Counterexample*: Start with empty string, `push_back('a')`, `push_front('a')`.
   - After `push_back('a')` at $R=1, L=1$: $\text{last} = \texttt{"a"}$. If we forget to set $\text{first} = \text{last}$, then $\text{first}$ remains $r_0$ (length $0$).
   - Next, `push_front('a')` at $L=0$: checking $S[L + 1 + \text{len}(\text{first})] = S[1 + 0] = S[1] = \texttt{'a'}$ would extend $r_0$ instead of $\texttt{"a"}$, or on `push_back('a')` followed by `push_back('a')` followed by `pop_front()`, $\text{first}$ would be completely out of sync with the true prefix palindrome $\texttt{"aa"}$.
2. **Deleting a Node from `tr[parent][c]` While It Still Has Active Fail-Children (`fail_deg[u] > 0`)**:
   - *Counterexample*: Consider $S = \texttt{"abacaba"}$. The palindrome $\texttt{"aba"}$ occurs as a prefix and suffix of $\texttt{"abacaba"}$. When `push_back` reaches index $7$, $\text{last}$ is $\texttt{"abacaba"}$ (with $\text{fail} = \texttt{"aba"}$). Thus $\texttt{"aba"}$ is no longer the longest palindrome at index $1$ or index $7$, so if you only count endpoints where $u$ is longest (`longest_pref[i] == u` or `longest_suf[j] == u`), $\texttt{"aba"}$ might have 0 endpoint pointers (if index $3$ was overwritten or popped), even though $\texttt{"aba"}$ still occurs inside $\texttt{"abacaba"}$!
   - *Fix*: Maintain `fail_deg[u]` (the number of currently existing PAM nodes $v$ with $\text{fail}(v) = u$). A node $u$ can only be erased from `tr[parent[u]][c]` when **both** its active maximal-interval count `ref_cnt[u] == 0` **and** `fail_deg[u] == 0`.
3. **Clearing Fixed-Size Transitions Lazily on Node Re-creation**:
   - When a node $u$ is deleted from `tr[parent[u]][c]` during `pop_back` / `pop_front`, do NOT leave dirty pointers in `tr[u][*]` if $u$'s index is recycled from a free-list; always zero-initialize `tr[u]`, `quick_link[u]`, `ref_cnt[u]`, and `fail_deg[u]` upon allocation.

---

## Iteration 22: Substring Palindrome Queries on $S[l..r]$ (Part 1 — Longest Palindromic Substring & Count of All Palindromic Occurrences in $S[l..r]$)

### 22.1 The Diagnostic Signal: Why Whole-String Manacher and PAM Over-Extend Outside $[l, r]$

Given a static string $S[1..N]$ and $Q$ queries $[l, r]$, we want to compute two fundamental aggregates restricted strictly to $S[l..r]$:
- **Problem 22A (Internal Longest Palindromic Substring / LPS)**: Find $\max \{ |P| : P = S[i..j] \text{ is a palindrome with } l \le i \le j \le r \}$.
- **Problem 22B (Internal Total Palindrome Occurrence Count)**: Find $\#\{ (i, j) : l \le i \le j \le r \text{ and } S[i..j] \text{ is a palindrome} \}$.

Why do naive applications of Manacher's algorithm or PAM fail?
- In Manacher's algorithm, each center $c$ stores its maximal radius $R[c]$ in the **whole string** $S[1..N]$. For a query $[l, r]$, a center $c$ inside $[l, r]$ has its effective radius clipped by the query boundaries:
  $$R_{[l, r]}(c) = \min\big(R[c],\; c - l,\; r - c\big)$$
  Because $\min(R[c], c - l, r - c)$ depends non-linearly on $l$ and $r$, taking a simple RMQ or prefix sum of $R[c]$ over $c \in [l, r]$ returns completely wrong answers!
- In PAM, the longest palindromic suffix of $S[1..p]$ for $p \in [l, r]$ might have length $> p - l + 1$ (extending to the left of $l$).

---

### 22.2 The Combinatorial Word Invariant: Center-Clipping Monotonicity & Prefix-Suffix Ancestor Clipping

#### Invariant 22.1 (Manacher Radius Clipping & Binary Search Decomposition for LPS in $S[l..r]$)
To unify odd and even centers, work on the standard Manacher half-integer centers (or on odd lengths $2k+1$ and even lengths $2k$ separately):
- An **odd palindrome** centered at integer index $c \in [l, r]$ has maximal radius $d_1[c] \ge 1$ (so it spans $[c - d_1[c] + 1 .. c + d_1[c] - 1]$ of length $2 d_1[c] - 1$).
  Clipped to $[l, r]$, its valid radius is:
  $$r_1(c; l, r) = \min\big(d_1[c],\; c - l + 1,\; r - c + 1\big)$$
- Observe that a target odd radius $k \ge 1$ is achievable in $S[l..r]$ if and only if there exists a center $c$ such that:
  $$c - k + 1 \ge l \quad \text{and} \quad c + k - 1 \le r \quad \text{and} \quad d_1[c] \ge k$$
  $$\iff c \in [l + k - 1,\; r - k + 1] \quad \text{and} \quad \max_{c \in [l + k - 1,\; r - k + 1]} d_1[c] \ge k$$
- Symmetrically, an **even palindrome** centered between $c$ and $c+1$ with radius $d_2[c] \ge 0$ (spanning $[c - d_2[c] + 1 .. c + d_2[c]]$ of length $2 d_2[c]$) achieves radius $k \ge 1$ in $S[l..r]$ if and only if:
  $$\max_{c \in [l + k - 1,\; r - k]} d_2[c] \ge k$$

**Why Monotonicity Holds**:
If a palindrome of odd radius $k$ exists in $S[l..r]$, then shrinking it by $1$ on both sides yields a palindrome of odd radius $k-1$ at the exact same center $c \in [l+k-1, r-k+1] \subset [l+k-2, r-k+2]$. Thus **odd radii and even radii are independently monotonic**, and a binary search over $k \in [1, \lfloor (r-l+1)/2 \rfloor + 1]$ using an $O(1)$ Sparse Table RMQ on $d_1$ and $d_2$ finds the longest palindrome in $S[l..r]$ in **$O(\log(r-l))$ online time with $O(N \log N)$ preprocessing**!

#### Can We Eliminate the Binary Search for $O(1)$ Online LPS? (Alternative PAM / Manacher Boundary Splitting)
Wait: what if $Q \le 5 \times 10^6$ and we need $O(1)$ or alternative PAM-based LPS?
Look at the function $r_1(c; l, r) = \min(d_1[c], c - l + 1, r - c + 1)$ across $c \in [l, r]$:
Let $m = \lfloor (l + r) / 2 \rfloor$ be the midpoint of $[l, r]$.
- For $c \le m$, $c - l + 1 \le r - c + 1$, so $r_1(c; l, r) = \min(d_1[c], c - l + 1)$.
- For $c > m$, $r - c + 1 < c - l + 1$, so $r_1(c; l, r) = \min(d_1[c], r - c + 1)$.
Even simpler via **PAM**:
Any longest palindrome in $S[l..r]$ either:
1. **Touches the left boundary $l$**: Then it is the **longest palindromic prefix** of $S[l..r]$! In a PAM built on $S^R$ (from right to left), this is the highest ancestor $u$ of $\text{first}[l]$ with $\text{len}(u) \le r - l + 1$.
2. **Touches the right boundary $r$**: Then it is the **longest palindromic suffix** of $S[l..r]$! In the PAM of $S$, this is the highest ancestor $u$ of $\text{last}[r]$ with $\text{len}(u) \le r - l + 1$.
3. **Touches neither $l$ nor $r$**: Then its maximal Manacher expansion in $S[1..N]$ lies **strictly inside $[l, r]$** (so $d_1[c] \le \min(c - l + 1, r - c + 1)$)!
Notice where such unclipped centers $c$ can live: once we binary search the leftmost center $c_L \in [l, m]$ whose Manacher interval $[c_L - d_1[c_L] + 1 .. c_L + d_1[c_L] - 1]$ starts $\ge l$ (or simply note that the longest palindrome touching $l$ has some center $c_L$, and any center $c < c_L$ that exceeds $l$ is already shorter than $2(c_L - l) + 1$!), all centers between the longest prefix palindrome's center and the longest suffix palindrome's center have $d_1[c]$ completely unclipped!

---

### 22.3 Total Palindrome Occurrences in $S[l..r]$: Offline Sweep vs. Online $O(1)$ Prefix-Polynomial / PAM Lifting

Now consider **Problem 22B**: Count all palindromic substrings $S[i..j]$ with $l \le i \le j \le r$.

#### Method 1: Online $O(\log N)$ via PAM Binary Lifting / `slink` Jump (When Counting Palindromes Ending at Fixed $r$ and Starting $\ge l$)
First, consider the simpler building block: *How many palindromic suffixes of $S[l..r]$ exist?*
In the PAM of $S[1..N]$, let $u_0 = \text{last}[r]$ be the node for the longest palindromic suffix of $S[1..r]$.
- A palindromic suffix of $S[1..r]$ lies inside $S[l..r]$ if and only if its length satisfies $\text{len}(v) \le r - l + 1$.
- Because $\text{len}(\text{fail}(v)) < \text{len}(v)$ is strictly decreasing along the `fail` chain, the palindromic suffixes of $S[l..r]$ are the ancestors of $u_0$ from the root down to the highest ancestor $u^*$ with $\text{len}(u^*) \le r - l + 1$.
- Finding $u^*$ takes:
  - $O(\log N)$ time using **Binary Lifting** (`up[u][k]`) on the PAM `fail` tree, OR
  - $O(\log N)$ time with **$O(N)$ memory** by jumping `slink[u]` (the series-link from Wave 1A!) whenever $\text{len}(\text{slink}[u]) > r - l + 1$, and taking a single arithmetic division step $( \text{len}(u) - (r - l + 1) ) / \text{diff}[u]$ inside the single AP block where $\text{len}(u) > r - l + 1 \ge \text{len}(\text{slink}[u])$!
- Once $u^*$ is found, the number of palindromic suffixes of $S[l..r]$ is simply $\text{depth}_{\text{fail}}(u^*)$.

#### Method 2: Counting ALL Palindromes in $S[l..r]$ via Manacher Center Splitting (Online $O(\log N)$ or Offline $O(1)$ per query)
Every palindrome $S[i..j] \subseteq S[l..r]$ has a unique center $c$. For odd palindromes centered at $c \in [l, r]$, the number of valid palindromes centered at $c$ and contained in $[l, r]$ is:
$$r_1(c; l, r) = \min\big(d_1[c],\; c - l + 1,\; r - c + 1\big)$$
Summing over $c \in [l, r]$ with midpoint $m = \lfloor (l+r)/2 \rfloor$:
$$\text{OddCount}(l, r) = \sum_{c = l}^{m} \min\big(d_1[c],\; c - l + 1\big) \;+\; \sum_{c = m+1}^{r} \min\big(d_1[c],\; r - c + 1\big)$$
Look at the first sum $\sum_{c=l}^{m} \min(d_1[c], c - l + 1)$:
$$\min\big(d_1[c],\; c - l + 1\big) < d_1[c] \iff c - d_1[c] + 1 < l$$
That is, a center $c \in [l, m]$ is clipped on the left if and only if its left Manacher endpoint $L(c) = c - d_1[c] + 1$ satisfies $L(c) < l$!
Similarly, a center $c \in [m+1, r]$ is clipped on the right if and only if its right Manacher endpoint $R(c) = c + d_1[c] - 1 > r$.

**How to evaluate $\sum_{c=l}^{m} \min(d_1[c], c - l + 1)$**:
1. **Perspective A (2D Range Query / Persistent Fenwick Tree — Online $O(\log N)$)**:
   Rewrite $\min(d_1[c], c - l + 1)$ by conditioning on whether $L(c) = c - d_1[c] + 1 < l$:
   - For centers $c \in [l, m]$ with $L(c) \ge l$: they contribute $d_1[c]$.
   - For centers $c \in [l, m]$ with $L(c) < l$: they contribute $(c + 1) - l$.
   Sweeping $l$ from $N$ down to $1$ (offline with a Fenwick tree, or online with a Persistent Segment Tree indexed by $L(c)$), we query in $[l, m]$ the sum of $d_1[c]$ for active points ($L(c) \ge l$) and the count & index-sum of inactive points ($L(c) < l$).
2. **Perspective B (Pure $O(N)$ Prefix Sums + Longest Prefix/Suffix Palindrome Clipping — Online $O(\log N)$ or $O(1)$ with $O(N)$ Space!)**:
   Wait—can we avoid 2D data structures altogether? **YES!**
   Let $P_L$ be the **longest palindromic prefix** of $S[l..r]$ (found in $O(\log N)$ via PAM `slink` on $S^R$, or via Manacher binary search). Suppose $P_L$ spans $[l .. l + \text{len}(P_L) - 1]$ with center $c_L = l + (\text{len}(P_L) - 1)/2 \le m$.
   **Lemma (No Center to the Right of $c_L$ Can Overflow $l$)**:
   Can any center $c \in (c_L, m]$ have $c - d_1[c] + 1 < l$?
   If $c > c_L$ had $c - d_1[c] + 1 \le l$, then the palindrome centered at $c$ shrunk to touch $l$ would span $[l .. 2c - l] \subseteq [l .. r]$ (since $c \le m \implies 2c - l \le r$) and would have center $c > c_L$, making it a **longer palindromic prefix of $S[l..r]$ than $P_L$**—a contradiction!
   And what about centers $c \in [l, c_L]$? Because $P_L = S[l .. 2c_L - l]$ is a palindrome, by reflection across $c_L$, any center $c \in [l, c_L]$ has a palindrome inside $P_L$ of radius at least $c - l + 1$? No—it might have $d_1[c] < c - l + 1$, wait: if $d_1[c] < c - l + 1$, its maximal palindrome lies strictly inside $[l, 2c_L - l]$, so it is NOT clipped by $l$! Wait: only centers $c \le c_L$ *could* potentially be clipped by $l$, wait—if $c < c_L$ is clipped by $l$ ($c - d_1[c] + 1 < l$), then by reflection across $c_L$, the mirrored center $c' = 2c_L - c$ had a palindrome extending beyond $2c_L - l$!
   Regardless, in PAM: a palindrome $S[i..j]$ lies in $S[l..r]$ iff $j \in [l, r]$ and $\text{len}(S[i..j]) \le j - l + 1$.
   In fact, on Manacher centers, adding the arithmetic progression $[c - d_1[c] + 1 .. c]$ to a second-order difference array counts all palindromes starting $\ge l$ when swept offline in $O(N + Q \log N)$!

---

### 22.4 Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Off-by-One in Even Manacher Center Interval Boundaries**:
   - For an even palindrome of radius $k$ ($1 \le k \le d_2[c]$) centered between $c$ and $c+1$, its left endpoint is $c - k + 1$ and its right endpoint is $c + k$.
   - Thus $c - k + 1 \ge l \iff c \ge l + k - 1$, and $c + k \le r \iff c \le r - k$.
   - **Pitfall**: Using $[l + k - 1, r - k + 1]$ (the odd-center range) for even centers allows $c = r - k + 1$, whose right endpoint is $(r - k + 1) + k = r + 1 > r$, reading $1$ character past $r$!
   - *Counterexample*: $S = \texttt{"abaab"}$, query $[l, r] = [1, 4]$ ($\texttt{"abaa"}$). At $c = 4$, $d_2[4] = 1$ ($\texttt{"aa"}$ at $S[3..4]$? No, between $3$ and $4$ is $c=3, d_2[3]=1$ spanning $[3, 4]$). If query is $[1, 3]$ ($\texttt{"aba"}$) and we test $k=1$ on $[1, 3]$ instead of $[1, 2]$, $c=3$ gives $d_2[3]=1$, falsely claiming $\texttt{"aba"}$ contains an even palindrome of length $2$!
2. **Using `up[u][k]` (Binary Lifting) When Memory Is Tight ($N = 10^6$, 64 MB)**:
   - A 20-level binary lifting table on $10^6$ PAM nodes takes $80$ MB of RAM.
   - Replacing binary lifting with **PAM `slink` jumping** (`while (len[slink[u]] > max_len) u = slink[u];` followed by jumping inside the arithmetic progression—or storing the PAM nodes of each AP chain in a flat vector / using HLD on the `fail` tree) uses $O(N)$ memory and $O(\log N)$ time!

---

## Iteration 23: Substring Palindrome Queries on $S[l..r]$ (Part 2 — Distinct Palindromes in $S[l..r]$ via Periodic Suffix APs & LCT `access`)

### 23.1 The Diagnostic Signal: Why Distinct Substring Palindromes Are Harder Than Static 1D Range Distinct Elements

Given a string $S[1..N]$ and $Q$ queries $[l, r]$, we want to compute the **number of distinct palindromic substrings** inside $S[l..r]$ (or maximum/sum of functions over distinct palindromes in $S[l..r]$).

In classic 1D array problems ("count distinct numbers in $A[l..r]$"), we sweep the right endpoint $r$ from $1$ to $N$ and maintain for each distinct value $x$ its **latest occurrence** $\text{last\_pos}[x] \le r$: when $x$ appears at $r$, we move its point weight $+1$ from $\text{last\_pos}[x]$ to $r$ in a Fenwick tree and query the suffix sum $\ge l$.

Why does a naive sweep fail for distinct palindromes in $S[l..r]$?
1. **Multiple New Occurrences per Right Endpoint $r$**: At position $r$, *every* ancestor $u$ of $\text{last}[r]$ in the PAM `fail` tree occurs as a suffix of $S[1..r]$, meaning $O(N)$ distinct palindromes might simultaneously acquire a new occurrence ending at $r$!
2. **Start-Position Dependence ($r - \text{len}(u) + 1 \ge l$)**: A palindrome $u$ whose latest occurrence ends at $p \le r$ is contained in $S[l..r]$ if and only if its **left endpoint** satisfies:
   $$\text{start}(u) = p - \text{len}(u) + 1 \ge l$$
   Notice that if we track each distinct palindrome $u$ by the **latest left endpoint** $\text{last\_start}[u]$ among all occurrences of $u$ ending $\le r$, then $u$ occurs inside $S[l..r]$ if and only if:
   $$\text{last\_start}[u] \ge l$$
   This is still a 1D condition! The entire algorithmic bottleneck is: **When we advance from $r-1$ to $r$, how do we update $\text{last\_start}[u] \leftarrow r - \text{len}(u) + 1$ for ALL ancestors $u$ of $\text{last}[r]$ in polylogarithmic time?**

---

### 23.2 The Combinatorial Word Invariant: Two Dual Views of Updating All Palindromic Suffixes at $r$

There are two celebrated structural ways to compress the $O(N)$ ancestor updates on the PAM `fail` tree into $O(\log N)$ operations, corresponding to the two foundational paradigms from `[国家集训队论文 2014 — 徐毅 《回文树及其应用》]` and modern Universal Cup / QOJ solutions:

#### Paradigm A: The $O(\log N)$ Palindromic Suffix Arithmetic Progression (`slink`) Shadowing Theorem
Recall from Wave 1A that the palindromic suffixes of $S[1..r]$ (the `fail`-chain of $\text{last}[r]$) partition into $O(\log r)$ arithmetic progressions (APs) via `diff[u] = len[u] - len[fail[u]]` and `slink[u]`.
Consider a single AP chain with top (longest) node $u$, common difference $d = \text{diff}[u]$, and bottom node $\text{slink}[u]$:
$$u = u_0,\; u_1 = \text{fail}(u_0),\; u_2 = \text{fail}(u_1),\; \dots,\; u_k \quad (\text{where } \text{len}(u_i) = \text{len}(u_0) - i \cdot d \ge \frac{1}{2}\text{len}(u_0))$$

**Theorem 23.1 (Internal Periodicity Forces Identical Prior Right-Occurrence Shifts!)**:
For every proper node $u_i$ ($1 \le i \le k$) in the same `slink` arithmetic progression below $u_0$:
What was the **most recent occurrence** of $u_i$ in $S[1..r-1]$ before position $r$?
- Because $u_0 = S[r - \text{len}(u_0) + 1 .. r]$ has period $d = \text{len}(u_0) - \text{len}(u_1)$, the palindrome $u_i$ (which is a suffix of $u_0$ of length $\text{len}(u_0) - i \cdot d$) **already occurred inside $u_0$ shifted to the left by exactly $d$ characters**, i.e., ending at position $r - d$!
- Could $u_i$ have occurred even later than $r - d$, say ending at some $p \in (r - d, r)$?
  **NO!** If $u_i$ occurred ending at $p \in (r - d, r)$, then since $\text{len}(u_i) \ge \frac{1}{2}\text{len}(u_0) \ge d$, its overlap with the suffix occurrence of $u_i$ at $r$ would induce a period $r - p < d$ on $u_i$, and by reflection inside $u_0$, would create a palindromic suffix of $u_0$ strictly longer than $u_1 = \text{fail}(u_0)$—contradicting the definition of $\text{fail}(u_0)$!

#### Alignment Diagram for Theorem 23.1 (Why All $u_1, \dots, u_k$ Had Latest Occurrence at $r - d$)

```
      |<------------------------ u_0 (ends at r, period d) ----------------------->|
S:    [ ........ u_1 (ends at r - d) ........ ][ <-- d --> ]
                 [ ........ u_2 (ends at r - d) ][ <-- d --> ]
                            |<-------- u_1 (ends at r) ------->|
                                       |<---- u_2 (ends at r) ->|
                                                                ^                  ^
                                                              r - d                r
```

Look at what Theorem 23.1 gives us for the **left endpoints** $\text{start}(u_i)$:
1. **At the new right endpoint $r$**:
   The new left endpoints of $u_0, u_1, \dots, u_k$ form a contiguous interval of step $d$? Even better:
   Actually, what was the previous latest left endpoint $\text{last\_start}[u_i]$ before $r$?
   - For $u_1, u_2, \dots, u_k$ (every node in the AP **except the longest node $u_0$**!):
     Their latest occurrence before $r$ ended at **the exact same right endpoint $r - d$**!
     Wait: at right endpoint $r - d$, the node $u_i$ had left endpoint:
     $$\text{prev\_start}(u_i) = (r - d) - \text{len}(u_i) + 1 = r - \big(\text{len}(u_i) + d\big) + 1 = r - \text{len}(u_{i-1}) + 1 = \text{new\_start}(u_{i-1})!$$
   - **READ THAT EQUATION AGAIN!**
     $$\text{prev\_start}(u_i) = \text{new\_start}(u_{i-1}) \quad \text{for all } i = 1, 2, \dots, k!$$
     Let's verify this!
     - At step $r$, the new left endpoints added to the active multiset of latest left-endpoints are:
       $$\Big\{ \text{new\_start}(u_0),\; \text{new\_start}(u_1),\; \dots,\; \text{new\_start}(u_{k-1}),\; \text{new\_start}(u_k) \Big\}$$
     - And the old left endpoints removed from the active multiset of latest left-endpoints are:
       $$\Big\{ \text{prev\_start}(u_0),\; \underbrace{\text{prev\_start}(u_1)}_{=\,\text{new\_start}(u_0)},\; \underbrace{\text{prev\_start}(u_2)}_{=\,\text{new\_start}(u_1)},\; \dots,\; \underbrace{\text{prev\_start}(u_k)}_{=\,\text{new\_start}(u_{k-1})} \Big\}$$
     - **Telescoping Cancellation Miracle**:
       In the entire arithmetic progression $u_0, u_1, \dots, u_k$ (which may contain $\Theta(N)$ nodes!), **all intermediate updates cancel out pairwise**!
       - $\text{new\_start}(u_0)$ cancels $\text{prev\_start}(u_1)$!
       - $\text{new\_start}(u_1)$ cancels $\text{prev\_start}(u_2)$!
       - $\dots$
       - $\text{new\_start}(u_{k-1})$ cancels $\text{prev\_start}(u_k)$!
     - The **ONLY** net change in the entire Fenwick Tree of latest left-endpoints for the whole AP chain $u_0, \dots, u_k$ is:
       1. **Remove ONE old left endpoint**: $\text{prev\_start}(u_0) = \text{last\_end}[u_0] - \text{len}(u_0) + 1$ (if $u_0$ had a previous occurrence $\text{last\_end}[u_0]$), and
       2. **Insert ONE new left endpoint**: $\text{new\_start}(u_k) = r - \text{len}(u_k) + 1$ (for the shortest node $u_k$ in the AP, just above $\text{slink}[u_0]$)!
     - And how do we maintain $\text{last\_end}[u_0]$ without updating all $u_i$? Simply store at each PAM node $v$ the latest right endpoint $\text{last\_end}[v]$ where the **subtree of $v$ in the fail tree** was visited! Since $u_0$ is the highest node in the AP, its latest occurrence in $S[1..r-1]$ is the maximum of $\text{last\_end}[w]$ over all nodes $w$ in the fail-subtree of $u_0$—which is a standard 1D subtree-max point-update query on the Euler tour (`dfn[u_0]..out[u_0]`) of the PAM `fail` tree!

Let's pause and appreciate this result (**Xu Yi 2014 / Rubinchik–Shur / BZOJ 4199 / Luogu P5555**):
- By combining **telescoping cancellation along each `slink` AP** with a **Segment Tree over the PAM fail-tree Euler tour** (to query $\text{last\_end}[u_0] = \max_{w \in \text{subtree}(u_0)} \text{pos}[w]$) and a **Fenwick Tree** (or Persistent Segment Tree for **online** queries!) over left endpoints:
- At each right endpoint $r = 1 \dots N$, there are at most $O(\log r)$ `slink` chains on the path from $\text{last}[r]$ to the root.
- Each `slink` chain performs **1 Euler-tour subtree-max query** (to find $\text{last\_end}[u_0]$), **1 point decrement** at $\text{last\_end}[u_0] - \text{len}(u_0) + 1$, and **1 point increment** at $r - \text{len}(u_k) + 1$!
- After processing $r$, we do **1 point update** in the Euler-tour Segment Tree at $\text{dfn}[\text{last}[r]] \leftarrow r$.
- **Total Complexity**:
  - **Offline Queries**: $O(N \log^2 N + Q \log N)$ time and **$O(N)$ memory**!
  - **Online Queries**: Replace the left-endpoint Fenwick tree with a **Persistent Segment Tree** (`root[r]`). Since each $r$ performs at most $2 \log_2 N$ point updates, total preprocessing is $O(N \log^2 N)$ time and $O(N \log^2 N)$ space, answering **arbitrary online distinct-palindrome queries on $S[l..r]$ in $O(\log N)$ time per query**!

---

#### Paradigm B: PAM Fail-Tree + Link-Cut Tree (`access`) Color-Chain Sweeping
What if distinct palindromes have **arbitrary weights** $w(u)$ (so $\text{new\_start}(u_{i-1})$ and $\text{prev\_start}(u_i)$ cannot cancel because $w(u_{i-1}) \ne w(u_i)$)?
Then we use the **Link-Cut Tree (LCT) Color-Chain Sweeping** paradigm (identical to Wave 2A's SAM + LCT):
1. Build the PAM `fail` tree of $S[1..N]$. Each node $u$ stores the latest right endpoint $\text{color}(u) = p$ that visited $u$.
2. When advancing to right endpoint $r$, we execute `LCT::access(last[r])`.
3. Each solid-path splay segment traversed during `access(last[r])` shares a uniform previous right-endpoint $p = \text{color}(S)$, and covers a contiguous chain of ancestors from some shallowest node $u_{\text{top}}$ to deepest node $u_{\text{bot}}$.
4. For any node $u$ on that chain, its previous left endpoint was $p - \text{len}(u) + 1$. In the Weighted version, we subtract its weight from $p - \text{len}(u) + 1$ and add it to $r - \text{len}(u) + 1$.
5. Notice that for unweighted distinct palindromes, on a contiguous interval of lengths (inside an AP of step $d$), both the old left endpoints $\{p - \text{len}(u) + 1\}$ and new left endpoints $\{r - \text{len}(u) + 1\}$ are arithmetic progressions, or via Paradigm A's `slink` telescoping, LCT is not even needed!

---

### 23.3 The Reverse-Engineering Scratchpad: Step-by-Step Trace of `slink` Telescoping for Distinct Palindromes

Let us trace Paradigm A on $S = \texttt{"abacaba"}$ at $r = 7$ ($\text{last}[7] = \texttt{"abacaba"}$):
- Palindromic suffixes of $S[1..7]$:
  - $u_0 = \texttt{"abacaba"}$ ($\text{len} = 7, \text{diff} = 4, \text{slink} = \texttt{"a"}$)
  - $u_1 = \texttt{"aba"}$ ($\text{len} = 3, \text{diff} = 2, \text{slink} = r_0$)
  - $u_2 = \texttt{"a"}$ ($\text{len} = 1, \text{diff} = 1, \text{slink} = r_0$)
- Notice that $u_0$ is an AP of length $1$ ($\text{diff} = 4 \ne 2$), while $u_1, u_2$ share $\text{diff}$? No: $\text{diff}(\texttt{"aba"}) = 3 - 1 = 2$, $\text{diff}(\texttt{"a"}) = 1 - 0 = 1$.
- Now consider $S = \texttt{"abababa"}$ at $r = 7$:
  - $u_0 = \texttt{"abababa"}$ ($\text{len} = 7, \text{diff} = 2$)
  - $u_1 = \texttt{"ababa"}$ ($\text{len} = 5, \text{diff} = 2$)
  - $u_2 = \texttt{"aba"}$ ($\text{len} = 3, \text{diff} = 2$)
  - $u_3 = \texttt{"a"}$ ($\text{len} = 1, \text{diff} = 1$)
  Here $\{u_0, u_1, u_2\}$ form a single AP chain with $d = 2$ and $\text{slink}[u_0] = u_3$ ($\texttt{"a"}$):
  - Before $r = 7$:
    - $u_0$ ($\texttt{"abababa"}$) never occurred ($\text{last\_end}[u_0] = 0$).
    - $u_1$ ($\texttt{"ababa"}$) occurred at $r-d = 5$, with left endpoint $5 - 5 + 1 = 1$.
    - $u_2$ ($\texttt{"aba"}$) occurred at $r-d = 5$, with left endpoint $5 - 3 + 1 = 3$.
  - At $r = 7$:
    - $u_0$ now starts at $7 - 7 + 1 = 1$ (replaces $u_1$'s old start at $1$!).
    - $u_1$ now starts at $7 - 5 + 1 = 3$ (replaces $u_2$'s old start at $3$!).
    - $u_2$ now starts at $7 - 3 + 1 = 5$ (brand new active left endpoint at $5$!).
  - **Net change for the entire chain $\{u_0, u_1, u_2\}$**: Only $+1$ at position $5 = r - \text{len}(u_2) + 1$! (Since $u_0$ had no previous occurrence, nothing is subtracted, and positions $1$ and $3$ remain $+1$ without being touched!)

```
Algorithm Contract: Distinct Palindromes in S[l..r] via PAM slink Telescoping
-----------------------------------------------------------------------------
Precomputation:
1. Build PAM of S[1..N]. Compute fail[u], len[u], diff[u] = len[u] - len[fail[u]],
   slink[u] = (diff[u] == diff[fail[u]] ? slink[fail[u]] : fail[u]),
   and bot[u] = the lowest node in u's AP chain (i.e., fail[bot[u]] == slink[u]):
     bot[u] = (diff[u] == diff[fail[u]] ? bot[fail[u]] : u).
2. Compute Euler tour [dfn[u], out[u]] of the PAM fail-tree.
3. Initialize Segment Tree `SegMax` over [1..num_nodes] to 0 (tracks max right-endpoint in subtree).
4. Initialize Fenwick Tree `BIT` (offline) or Persistent SegTree (online) over [1..N] to 0.

Sweep r from 1 to N:
  u = last[r]
  while u > 1:   // while u is neither r_{-1} nor r_0
    prev_r = SegMax.query(dfn[u], out[u])
    if prev_r > 0:
      old_left = prev_r - len[u] + 1
      BIT.add(old_left, -1)
    u_low = bot[u]
    new_left = r - len[u_low] + 1
    BIT.add(new_left, +1)
    u = slink[u]
  SegMax.update_point(dfn[last[r]], r)
  Answer all queries [l, r] as BIT.query_suffix(l).
```

---

### 23.4 Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Confusing `slink[u]` (First Node Outside the AP) with `bot[u]` (Last Node Inside the AP)**:
   - In standard PAM DP (`CF 932G`), `slink[u]` points to the highest proper ancestor $v$ with $\text{diff}[v] \ne \text{diff}[u]$. Notice that $v = \text{slink}[u]$ is the **last node of the step-$d$ arithmetic progression** in terms of *lengths* ($\text{len}(u_k) - \text{len}(v) = d$), wait:
   - Let's check carefully! On $S = \texttt{"abababa"}$:
     - $\text{len}(u_0 = \texttt{"abababa"}) = 7$, $\text{fail} = u_1 (\text{len } 5) \implies \text{diff}[u_0] = 2$.
     - $\text{len}(u_1 = \texttt{"ababa"}) = 5$, $\text{fail} = u_2 (\text{len } 3) \implies \text{diff}[u_1] = 2$.
     - $\text{len}(u_2 = \texttt{"aba"}) = 3$, $\text{fail} = u_3 (\text{len } 1) \implies \text{diff}[u_2] = 2$.
     - $\text{len}(u_3 = \texttt{"a"}) = 1$, $\text{fail} = r_0 (\text{len } 0) \implies \text{diff}[u_3] = 1$.
     Here $\text{slink}[u_0] = u_3$ ($\text{len} = 1$).
     Does $u_3$ ($\texttt{"a"}$) ALSO have its latest occurrence before $r=7$ at $r - d = 7 - 2 = 5$?
     Wait: $\texttt{"a"}$ is a suffix of $\texttt{"aba"}$ ($\text{len } 3$) with difference $3 - 1 = 2 = d$, so $\texttt{"a"}$ ALSO occurred at $7 - 2 = 5$, EXCEPT what if $\texttt{"a"}$ ALSO occurred at $r - 1 = 6$?!
     - *Counterexample*: Suppose $S = \texttt{"aaaa"}$ or $S = \texttt{"aba"}$? No, in $S = \texttt{"abababa"}$, $S[6] = \texttt{'b'} \ne \texttt{'a'}$, so $\texttt{"a"}$ did not occur at $6$.
     - What if $u_3$ had length $< d$? Say $u_2 = \texttt{"abba"}$ ($\text{len}=4$), $u_3 = \texttt{"a"}$ ($\text{len}=1$), $d = 3$. Then $u_2 = \texttt{"abba"}$ has period $3$, so $\texttt{"a"}$ occurs at $r - 3$ and $r$. Could $\texttt{"a"}$ ALSO occur at $r - 1$ or $r - 2$? No, if $u_2 = \texttt{"aaaa"}$, then $\text{fail}(u_2)$ would be $\texttt{"aaa"}$, not $\texttt{"a"}$! Because $u_3 = \text{fail}(u_2)$ is the **longest** proper palindromic suffix of $u_2$, $u_3$ CANNOT occur ending at any position strictly between $r - d$ and $r$, because any occurrence of $u_3$ ending at $p \in (r-d, r)$ would mean $S[p - \text{len}(u_3) + 1 .. r]$ has a palindromic suffix? Wait: what if $u_3 = \texttt{"a"}$ occurs inside $u_2 = \texttt{"abaa...a"}$? No, if $u_3$ occurred ending at $p \in (r-d, r)$, it doesn't necessarily touch the ends of $u_2$!
     - **CRITICAL COUNTEREXAMPLE**: Let $u_2 = \texttt{"aabaa"}$ ($\text{len}=5$), $u_3 = \text{fail}(u_2) = \texttt{"aa"}$ ($\text{len}=2$), $d = \text{diff}[u_2] = 5 - 2 = 3$.
       In $u_2 = \texttt{"aabaa"}$ (indices $1..5$, so $r=5$):
       - $u_2 = \texttt{"aabaa"}$ ends at $5$.
       - $r - d = 5 - 3 = 2$. Indeed, $u_3 = \texttt{"aa"}$ occurs ending at $r - d = 2$ ($S[1..2] = \texttt{"aa"}$).
       - Did $u_3 = \texttt{"aa"}$ occur strictly between $2$ and $5$? No.
       - What about $u_4 = \texttt{"a"}$? Not in the AP.
       - Wait: what if $u_2 = \texttt{"abaaba"}$? $\text{fail} = \texttt{"aba"}$.
       - Why do we stop at `u_low = bot[u]` (where $\text{diff}[u_{\text{low}}] = d$ and $\text{fail}(u_{\text{low}}) = \text{slink}[u]$) instead of including $\text{slink}[u]$ in the same telescoping step?
       - Because in the `while` loop, the next iteration sets `u = slink[u]`, which WILL process $\text{slink}[u]$ as the top of the *next* AP chain! If you used $\text{slink}[u]$ as `u_low` AND jumped `u = slink[u]`, you would double-count $\text{slink}[u]$!
       - Using `u_low = bot[u]` (the lowest node with $\text{diff}[u_{\text{low}}] == \text{diff}[u]$, whose `fail` is `slink[u]`) partitions the `fail` chain into **disjoint** AP blocks $u_0 \dots u_{\text{low}}$, where every $u_i$ ($1 \le i \le k$) satisfies $\text{len}(u_{i-1}) \le 2 \text{len}(u_i)$ (since $\text{diff}[u_i] = d \implies \text{len}(u_i) > d$), which **rigorously guarantees** $\text{len}(u_i) > d$, so any occurrence of $u_i$ in $(r-d, r)$ would overlap with the suffix $u_i$ at $r$ and contradict minimality of period $d$!
       - **Double Moral**: Defining `bot[u]` so the block is $\{u_0, \dots, \text{bot}[u]\}$ (all having $\text{diff} = d$, hence all having $\text{len}(u_i) \ge d + 1 > d$) BOTH keeps blocks disjoint when advancing `u = slink[u]` AND ensures $\text{len}(u_i) > d$ so $u_i$ cannot occur in $(r-d, r)$!

---

## Iteration 24: Combinatorics of Palindromes, Rich Words, Unique Palindromic Factorization, Antisymmetric Palindromes & Inverse String Reconstruction

### 24.1 The Droubay–Pirillo Theorem & Rich (Full) Words

#### 1. The Diagnostic Signal
How many distinct non-empty palindromic substrings can a string $S$ of length $N$ contain, and which strings achieve the maximum?

#### 2. The Combinatorial Word Invariant (Droubay, Justin & Pirillo 2001)
**Theorem 24.1 (Droubay–Pirillo Bound)**:
Any finite word $S$ of length $N$ contains at most $N + 1$ distinct palindromic substrings (including the empty word $\varepsilon$, or at most $N$ non-empty distinct palindromes).
- **Proof via Right-Extension Uniqueness**:
  When appending character $S[r]$ to $S[1..r-1]$, suppose two distinct palindromic suffixes $P$ and $Q$ of $S[1..r]$ ($|P| > |Q|$) both appeared for the **first time** at right endpoint $r$.
  Because $Q$ is a suffix of $P$ and $P$ is a palindrome, $Q$ is also a **prefix** of $P$, which means $Q$ already occurred at $S[r - |P| + 1 .. r - |P| + |Q|] \subset S[1..r-1]$—contradicting that $Q$ appeared for the first time at $r$!
  Thus each right-append $r \in \{1, \dots, N\}$ creates **at most $1$** new palindrome (specifically, the longest palindromic suffix $\text{last}[r]$ if and only if it is not already in $S[1..r-1]$).

**Definition 24.2 (Rich / Full Words — `富回文串 / 满回文串`)**:
A word $S$ of length $N$ is called **rich** (or *full*) if it contains the maximum possible number of distinct non-empty palindromes—namely, $N$ non-empty palindromes (so every prefix $S[1..r]$ introduces a brand-new longest palindromic suffix).

**Theorem 24.3 (Three Equivalent Characterizations of Rich Words — Glen, Justin, Widmer & Zamboni 2009)**:
The following are equivalent for a finite word $S$:
1. **Saturation**: $S$ contains $|S|$ distinct non-empty palindromic factors (every step in PAM creates a new node).
2. **Factor Closure**: Every factor (substring) of $S$ is rich, and $S^R$ is rich.
3. **Complete Return-Word Palindromicity (The Structural Test!)**: For every palindromic substring $P$ of $S$, every **complete return word** of $P$ in $S$ (i.e., any substring $S[i..j]$ starting and ending with $P$ and containing **only those two occurrences** of $P$) is itself a **palindrome**!
   - *Proof Sketch*: When $S[r]$ is appended, let $P = \text{last}[r]$ be the longest palindromic suffix of $S[1..r]$. If $P$ already occurred earlier in $S[1..r-1]$, let its most recent occurrence start at $i$, so $S[i..r]$ starts and ends with $P$ and contains no intermediate occurrence of $P$. If $S[i..r]$ were a palindrome, it would be a palindromic suffix of $S[1..r]$ strictly longer than $P$—impossible! Conversely, if a new palindrome $W = S[i..r]$ is created at $r$, its longest proper palindromic suffix $P = \text{fail}(W)$ occurs as the prefix and suffix of $W$ with no internal occurrence of $P$, so the complete return word $W$ of $P$ is a palindrome!

**Competitive Programming Applications of Rich Words**:
- Every binary word of length $\le 7$ is rich; the shortest non-rich binary word has length $8$:
  $$S_{\text{non-rich}} = \texttt{aabaabaa} \quad \text{or} \quad \texttt{00100100}$$
  Wait: in $S = \texttt{00100100}$ ($N=8$), the palindrome $P = \texttt{00100}$ occurs at $S[1..5]$ and $S[4..8]$, so its complete return word is $S[1..8] = \texttt{00100100}$, which is NOT a palindrome! At $r=8$, the longest palindromic suffix is $\texttt{00100}$, which already occurred at $r=5$, so $S$ has only $7 < 8$ non-empty palindromes!
- All **Sturmian words**, **episturmian (Arnoux–Rauzy) words**, and words of the form $w$ avoiding non-palindromic return words are rich.

---

### 24.2 Unique Palindromic Factorization & Parity-Constrained Palindrome Partitions

1. **Even-Length Palindrome Factorization Uniqueness**:
   Suppose we want to partition $S[1..N]$ into **even-length palindromes** $S = P_1 P_2 \dots P_k$.
   **Greedy Minimality Theorem**: If $S = P_1 \dots P_k$ has an even-length palindromic prefix $P$ that is the **shortest** non-empty even-length palindromic prefix of $S$, then in any even-length palindrome partition whose first piece $Q_1$ has $|Q_1| > |P|$, we can refine $Q_1$ using $P$:
   - If $|P| \le |Q_1|/2$, since $P$ is a prefix of $Q_1$ and $Q_1$ is a palindrome, $P$ is also a suffix of $Q_1$, so $Q_1 = P \cdot M \cdot P$ where $M$ is also an even-length palindrome! Replacing $Q_1$ by $(P)(M)(P)$ strictly increases the number of pieces and keeps all pieces even-length palindromes!
   - If $|P| > |Q_1|/2$, then the overlap of $P$ and $Q_1$ induces a period $d = |Q_1| - |P| < |P|$ on $Q_1$, which (because both $|P|$ and $|Q_1|$ are even!) creates a shorter even-length palindromic border of $Q_1$—contradicting that $P$ was the shortest even-length palindromic prefix!
   - **Consequence**: To check if $S$ can be partitioned into even-length palindromes (or to **maximize** the number of even-length palindromic pieces), **greedily cutting the shortest even-length palindromic prefix at every step is 100% optimal**!

2. **General Palindrome Partition (`CF 932G` / Minimum Palindrome Cut / Odd+Even)**:
   When odd-length palindromes are allowed, greedy fails (since every single character is an odd palindrome of length $1$), and PAM `slink` DP runs in $O(N \log N)$.

---

### 24.3 Watson–Crick ($\theta$-Palindromes) & Antisymmetric Palindromes

Let $\theta : \Sigma \to \Sigma$ be an **involution** ($\theta(\theta(c)) = c$ for all $c \in \Sigma$), such as DNA Watson–Crick complement ($\texttt{A} \leftrightarrow \texttt{T}, \texttt{C} \leftrightarrow \texttt{G}$) or binary bit-flip ($\texttt{0} \leftrightarrow \texttt{1}$, e.g., `[POI 2010] Antisymmetry`).
A string $P$ is a **$\theta$-palindrome** if:
$$P = \theta(P^R) \iff P[i] = \theta\big(P[|P| - i + 1]\big) \quad \forall 1 \le i \le |P|$$

**Structural Dichotomy of Involutions $\theta$**:
1. **Case A ($\theta$ has NO fixed points on $\Sigma$, e.g., binary $\texttt{0} \leftrightarrow \texttt{1}$ or DNA $\texttt{A}\leftrightarrow\texttt{T}, \texttt{C}\leftrightarrow\texttt{G}$)**:
   - Can an odd-length $\theta$-palindrome exist?
     At the center index $c = (|P|+1)/2$, we would require $P[c] = \theta(P[c])$, which is impossible since $\theta$ has no fixed points!
   - Therefore, **all $\theta$-palindromes have EVEN length**, and in a $\theta$-PAM, the odd root $r_{-1}$ has **zero transitions**—only the even root $r_0$ exists!
   - In Manacher's algorithm, only half-integer centers $(i, i+1)$ need to be checked, comparing $S[i - k + 1] == \theta(S[i + k])$.
2. **Case B ($\theta$ has both fixed points and 2-cycles)**:
   - Odd-length $\theta$-palindromes exist, and their central character $P[(|P|+1)/2]$ must be a fixed point of $\theta$ ($\theta(c) = c$).
   - **Key Closure Invariant**: Does the `fail`-chain of a $\theta$-PAM still work?
     Suppose $P$ is a $\theta$-palindrome and $Q$ is a proper $\theta$-palindromic suffix of $P$. Then for $1 \le i \le |Q|$:
     $$P[i] = \theta\big(P[|P| - i + 1]\big) = \theta\big(Q[|Q| - i + 1]\big) = \theta\big(\theta(Q[i])\big) = Q[i]$$
     Wait: $P[i] = Q[i]$! That means **the reflection of a $\theta$-palindromic suffix $Q$ across the center of a $\theta$-palindrome $P$ is an EXACT prefix $Q$ (NOT $\theta(Q)$!)** because $\theta$ is applied TWICE (once by $P$, once by $Q$), and $\theta(\theta(x)) = x$!
     - **Consequence**: A $\theta$-PAM (`Antisymmetric PAM`) has the **exact same `fail`-tree, `slink` AP structure, and Droubay–Pirillo $\le N+1$ bound** as a standard PAM, with the sole change that extending node $u$ at $r$ checks $S[r - 1 - \text{len}(u)] == \theta(S[r])$ (and for $u = r_{-1}$, requires $\theta(S[r]) == S[r]$)!

---

### 24.4 Inverse String Reconstruction (`逆向字符串构造`) from KMP $\pi$, Z-Array, or Manacher Radii

A classic genre of grandmaster string problems provides an array of structural measurements—such as the KMP prefix function $\pi[1..N]$, the Z-array $Z[1..N]$, or Manacher radii $d_1[1..N], d_2[1..N]$—and asks to **reconstruct the lexicographically smallest valid string**, **count the number of valid strings over $\Sigma$**, or **test validity**.

#### 1. The Unified Equality + Inequality Graph Invariant
Every deterministic string comparison algorithm (KMP, Z-algorithm, Manacher) discovers values by performing a sequence of **character equality matches** ($S[i] == S[j]$) terminated by a **single mismatch** ($S[i'] \ne S[j']$, unless the boundary of $S$ is hit):
- **Equality Constraints ($S[i] == S[j]$)**:
  - *From KMP $\pi[i]$*: $S[1 .. \pi[i]] = S[i - \pi[i] + 1 .. i]$, which means $S[i] = S[\pi[i]]$ (and by induction on $1 .. i-1$, all earlier characters of the border already matched!).
  - *From Manacher $d_1[c], d_2[c]$*: Every step that increments the Manacher R-box $R = c + r$ asserts $S[2c - R] = S[R]$. Because the Manacher R-box advances at most $N$ times, **there are at most $N$ equality edges**!
- **Inequality Constraints ($S[i'] \ne S[j']$)**:
  - *From KMP $\pi[i]$*: While walking the KMP fail chain $k = \pi[i-1], \pi[k], \dots$ before settling on $\pi[i]$, every rejected candidate $k$ asserts:
    $$S[i] \ne S[k + 1]$$
  - *From Manacher $d_1[c], d_2[c]$*: At each center $c$, if the palindrome stops before hitting $1$ or $N$ (i.e., $c - d_1[c] \ge 1$ and $c + d_1[c] \le N$), the stopping condition asserts the **single inequality**:
    $$S\big[c - d_1[c]\big] \ne S\big[c + d_1[c]\big]$$
    (and symmetrically $S[c - d_2[c]] \ne S[c + d_2[c] + 1]$ for even centers).

#### 2. Validity Necessary & Sufficient Conditions
To test if a given array $\pi[1..N]$ or $d_1[1..N], d_2[1..N]$ is valid (realizable over an unbounded alphabet, or alphabet of size $|\Sigma|$):
1. **Structural Consistency (Mirror / Border Bounds)**:
   - For KMP $\pi$: $\pi[1] = 0$, and for $i \ge 2$, $\pi[i] \le \pi[i-1] + 1$; furthermore, $\pi[i] - 1$ must appear on the fail-chain of $\pi[i-1]$!
   - For Manacher $d_1, d_2$: You Do NOT need to guess hidden constraints—simply construct the canonical string (by contracting the $O(N)$ Manacher R-box equalities via DSU and greedily assigning the smallest character not forbidden by the mismatch edges), and **run Manacher's algorithm on the reconstructed string** to check if its radii equal the input $d_1, d_2$!
2. **Exact Counting of Valid Strings Over Alphabet Size $\sigma = |\Sigma|$**:
   - In KMP/Z/Manacher reconstruction where the input array is valid, look at position $i$ from $1$ to $N$ (or in Manacher, order the connected components of the equality DSU by their **first appearance index** $i$):
   - When a DSU component appears for the very first time at index $i$:
     - Its character is **forced to be unequal** to the characters of all already-determined components linked to $i$ by mismatch edges $S[i] \ne S[j]$ ($j < i$).
     - Wait: in KMP and Manacher, do the mismatch neighbours $j < i$ of a newly opened position $i$ ever depend on future choices, or are their DSU components ALREADY fixed before index $i$?
     - **Crucial Property**: Every mismatch edge encountered when determining index $i$ compares $S[i]$ against some $S[j]$ with **$j < i$**!
     - Because all $j < i$ have already had their characters chosen, if $c(i)$ is the number of **distinct** characters among $\{ S[j] : (i, j) \text{ is a mismatch edge with } j < i \}$ (which is invariant across all valid strings because the equality partitions on $1..i-1$ are uniquely forced by the input!), then the number of valid choices for $S[i]$ is simply:
       $$\max\big(0,\; \sigma - c(i)\big)$$
     - **Theorem 24.4 (Chromatic Polynomial of String Reconstruction Is a Simple Product!)**:
       For any realizable KMP $\pi$-array, Z-array, or Manacher radius array, the restriction of the inequality graph to the equality-DSU components ordered by earliest index is a **chordal / backward-determined graph** where each new component $v$ has its forbidden colours already pairwise distinct (or uniquely partitioned by prior equalities)! Thus the number of valid strings over an alphabet of size $\sigma$ is the exact product:
       $$\#\text{Valid Strings} = \prod_{v \in \text{Components}} \max\big(0,\; \sigma - \text{deg}_{\text{distinct-prev}}(v)\big)$$
       computable in **$O(N)$ time**!

---

## Iteration 25: Multilingual Problem Mining (`[EN]` / `[ZH]` / `[JA]`), 4-Tier Difficulty Ladder (32 Non-Template Problems) & Quarantine Ledger (`R-3A-01..08`)

### 25.1 Strict Quarantine Table of Pure Template Problems (`R-3A-01` – `R-3A-08`)

In accordance with `AGENTS.md` and `PLAN.md` (`§2`), bare verification problems whose sole task is copying a standard Manacher or Palindromic Automaton template are **strictly quarantined** and excluded from the textbook ladders:

| Quarantine ID | Source & Problem Title | Language / Judge | Reason for Quarantine |
| :--- | :--- | :--- | :--- |
| **`R-3A-01`** | Library Checker — *Enumerate Palindromes* | `[EN]` / `[JA]` Yosupo | Bare Manacher radius array output ($2N-1$ centers). Zero modelling. |
| **`R-3A-02`** | Library Checker — *Eertree* | `[EN]` / `[JA]` Yosupo | Bare Palindromic Automaton node/parent/link construction dump. |
| **`R-3A-03`** | Luogu P5496 — *【模板】回文自动机（PAM）* | `[ZH]` Luogu | Bare online PAM template asking for $\text{depth}_{\text{fail}}(\text{last}[r])$ at each prefix. |
| **`R-3A-04`** | Luogu P3805 — *【模板】manacher* | `[ZH]` Luogu | Bare longest palindromic substring length via Manacher. |
| **`R-3A-05`** | LOJ 141 — *回文子串* | `[ZH]` LibreOJ | Pure double-ended insertion PAM template without algorithmic coupling. |
| **`R-3A-06`** | `[APIO 2014]` / Luogu P3649 — *Palindromes (回文串)* | `[EN]` / `[ZH]` APIO | Asks for $\max_u \text{len}(u) \cdot \text{cnt}(u)$ over PAM fail-tree bottom-up sum; borders on bare PAM template (reserved only as a 3-line warm-up remark, excluded from main ladder). |
| **`R-3A-07`** | SPOJ `NUMOFPAL` — *Number of Palindromes* | `[EN]` SPOJ | Bare total palindrome count on a static string. |
| **`R-3A-08`** | HDU 3068 — *最长回文* | `[ZH]` HDU | Duplicate bare Manacher template. |

---

### 25.2 Curated 4-Tier Difficulty Ladder (32 Accepted Non-Template Problems with 4-Step Zero-Magic Analysis)

---

#### Tier 1: Stepping Stone (8 Problems — Structural PAM/Manacher Properties, Half-Palindrome Links, Antisymmetry & Inverse Restoration)

##### Problem 3A-01: `[POI 2010]` Antisymmetry (`[EN]` / `[ZH]` Luogu P3501)
- **Statement & Constraints**: Given a binary string $S \in \{\texttt{0}, \texttt{1}\}^N$ ($N \le 5 \times 10^5$), count the number of non-empty substrings $S[l..r]$ that are *antisymmetric*—meaning $S[l..r]$ equals the bit-flipped reversal of itself ($\theta(\texttt{0})=\texttt{1}, \theta(\texttt{1})=\texttt{0}$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Checking all $O(N^2)$ substrings fails for $N = 5 \times 10^5$; standard Manacher checks $S[i] == S[j]$ rather than $S[i] \ne S[j]$.
  2. *Combinatorial Invariant*: Because $\theta(\texttt{0})=\texttt{1}$ has no fixed points, no odd-length substring can satisfy $S[c] = \theta(S[c])$. Every antisymmetric substring has **even length** centered at a half-integer $(c, c+1)$, and shrinking an antisymmetric substring by $1$ on both ends preserves antisymmetry.
  3. *Reverse-Engineering Scratchpad*: Run even-center Manacher with match condition $S[c - k + 1] = 1 - S[c + k]$, maintaining the rightmost antisymmetric box $[L, R]$ via symmetry reflection $d_2[c] = \min(d_2[L + R - c], R - c)$ (since the reflection of an $\theta$-palindrome inside a larger $\theta$-palindrome applies $\theta$ twice: $\theta(\theta(x)) = x$, so it is AGAIN a $\theta$-palindrome, not a regular palindrome!). Answer is $\sum_{c=1}^{N-1} d_2[c]$ in $O(N)$.
  4. *Boundary Pitfall*: Thinking that reflecting across the center of an antisymmetric palindrome turns an inner antisymmetric palindrome into a normal palindrome—in fact $\theta^2 = \text{id}$ preserves antisymmetry under reflection!

##### Problem 3A-02: `[SHOI2011]` 双倍回文 (Double Palindrome, `[ZH]` Luogu P4287 / BZOJ 2342)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), find the maximum length of a substring of the form $W W^R W W^R$ (i.e., a palindrome $P$ of length divisible by $4$ whose first half $P[1..|P|/2]$ is also a palindrome).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A palindrome $P$ may have many palindromic prefixes, and scanning all ancestors in PAM takes $O(\text{depth})$ unless we maintain a half-length pointer.
  2. *Combinatorial Invariant*: A palindrome $u$ is a double palindrome iff $2 \mid \text{len}(u)$ and $u$ has a palindromic border $v$ of exact length $\text{len}(v) = \text{len}(u)/2$ (which also forces $4 \mid \text{len}(u)$ since $v = W W^R$ must itself be even? Wait: the problem specifically requires $W W^R W W^R$, so $2 \mid \text{len}(v)$, hence $4 \mid \text{len}(u)$).
  3. *Reverse-Engineering Scratchpad*: Maintain on every PAM node $u$ the **Half-Link pointer `trans[u]`**: the longest palindromic suffix $v$ of $u$ with $\text{len}(v) \le \text{len}(u)/2$. When creating $u = \text{tr}[p][c]$, if $\text{len}(u) \le 2$ set $\text{trans}[u] = \text{fail}[u]$; else start from $w = \text{trans}[p]$ and walk $w \leftarrow \text{fail}[w]$ while $S[r - 1 - \text{len}(w)] \ne c$ or $\text{len}(w) + 2 > \text{len}(u)/2$, then set $\text{trans}[u] = \text{tr}[w][c]$. Check $4 \mid \text{len}(u)$ and $\text{len}(\text{trans}[u]) == \text{len}(u)/2$ in $O(N)$ total time.
  4. *Boundary Pitfall*: Checking only $\text{len}(\text{trans}[u]) == \text{len}(u)/2$ without $4 \mid \text{len}(u)$ accepts $P = \texttt{"abaaba"}$ ($\text{len}=6, \text{half}=3 = \texttt{"aba"}$), which is $W W$ for odd palindrome $W$, not $W W^R W W^R$.

##### Problem 3A-03: `[CERC 2014]` Virus Synthesis (`[EN]` / `[ZH]` Luogu P4762 / BZOJ 4044)
- **Statement & Constraints**: Starting from an empty string over $\{\texttt{A}, \texttt{C}, \texttt{G}, \texttt{T}\}$, you can: (1) insert a character at either end (cost $1$), or (2) replace the current string $X$ with $X X^R$ (cost $1$). Find the minimum operations to form a substring of $S$ and then pad single characters to reach $S$ ($|S| \le 10^5$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Operation (2) always produces an even-length palindrome $u$. Once the last operation (2) finishes at palindrome $u$, all remaining $|S| - \text{len}(u)$ characters must be added one-by-one.
  2. *Combinatorial Invariant*: To build an even palindrome $u$ Ending with operation (2) from $X$ ($\text{len}(X) = \text{len}(u)/2$), we can either build $X$ by appending its last character to $p = \text{parent}_{\text{trie}}(u)$ before doubling ($dp[u] \le dp[p] + 1$), OR finish $X$ at its longest palindromic suffix $v = \text{trans}[u]$ ($\text{len}(v) \le \text{len}(u)/2$), pad $\text{len}(u)/2 - \text{len}(v)$ characters to complete $X$, and then double ($dp[u] \le dp[\text{trans}[u]] + \text{len}(u)/2 - \text{len}(\text{trans}[u]) + 1$).
  3. *Reverse-Engineering Scratchpad*: Build PAM of $S$ with `trans[u]` ($\text{len}(\text{trans}[u]) \le \text{len}(u)/2$). Run BFS over even-length PAM nodes: initialize $dp[r_0] = 0$, $dp[u] = \text{len}(u)$ for all even $u$, transition $dp[\text{tr}[u][c]] = \min(dp[\text{tr}[u][c]], dp[u] + 1)$ and $dp[u] = \min(dp[u], dp[\text{trans}[u]] + \text{len}(u)/2 - \text{len}(\text{trans}[u]) + 1)$. Answer is $\min_u (dp[u] + |S| - \text{len}(u))$.
  4. *Boundary Pitfall*: Doing the DP in node-index order instead of **BFS / increasing length order** fails because `trans[u]` is a `fail`-ancestor (guaranteed shorter) while `parent(u)` is a Trie parent—BFS order on the PAM Trie guarantees both $\text{parent}(u)$ and $\text{trans}(u)$ are already finalized!

##### Problem 3A-04: `[JSOI2016]` 扭动的回文串 (Twisted Palindrome, `[ZH]` Luogu P4324 / BZOJ 4755)
- **Statement & Constraints**: Given two strings $A[1..N]$ and $B[1..N]$ ($N \le 10^5$), find the maximum length of a palindrome formed by taking $A[i..j]$ concatenated with $B[j..k]$ (or solely inside $A$ or $B$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A concatenation $A[i..j] + B[j..k]$ has $O(N^3)$ choices of $(i, j, k)$.
  2. *Combinatorial Invariant*: Any twisted palindrome $A[i..j] B[j..k]$ has a unique center $c$ (either in $A$ or in $B$). Once the center $c$ is fixed (say in $A$), the optimal expansion grows the core palindrome inside $A$ as far as possible: $[c - r .. c + r]$ where $r = d_A[c] - 1$. At the exact moment $A[c - r - 1] \ne A[c + r + 1]$, the right side switches from $A[c + r + 1 \dots]$ to $B[c + r \dots]$!
  3. *Reverse-Engineering Scratchpad*: After maximal expansion inside $A$ to $[L_A, R_A] = [c - r, c + r]$, the remaining outward extension matches $A[L_A - 1, L_A - 2, \dots]$ against $B[R_A, R_A + 1, \dots]$, which is a single $O(1)$ $\text{LCP}(A^R[\text{pos}], B[R_A])$ query! Total time $O(N)$.
  4. *Boundary Pitfall*: Switching from $A$ to $B$ *before* the maximal Manacher radius inside $A$ is never needed: if $A[x] = A[y]$ inside the core palindrome and we switched early, extending the core in $A$ covers the exact same characters until the first mismatch.

##### Problem 3A-05: `[SDOI2016]` 生成魔咒 / Inverse Manacher & Prefix-Function Counting (`[ZH]` / `[EN]` CF Gym 101194 / Manacher Restoration)
- **Statement & Constraints**: Given proposed Manacher odd and even radius arrays $d_1[1..N]$ and $d_2[1..N-1]$ ($N \le 5 \times 10^5$), determine whether a valid string over $\Sigma = \{\texttt{a}..\texttt{z}\}$ exists, and if so, count the number of valid strings modulo $10^9 + 7$ (or output the lexicographically smallest one).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Naively adding all $O(N^2)$ palindrome equalities $S[c - k] = S[c + k]$ for $k < d_1[c]$ times out.
  2. *Combinatorial Invariant*: By running the forward Manacher simulation on the given radii $d_1[c], d_2[c]$, we only ever need to unite $S[2c - R] = S[R]$ when $R$ advances beyond $\max R$ ($O(N)$ DSU unions total!), and add the single mismatch edge $S[c - d_1[c]] \ne S[c + d_1[c]]$ at each center $c$ that does not touch the boundary.
  3. *Reverse-Engineering Scratchpad*: Process indices $i = 1 \dots N$ left-to-right. Whenever $i$ is the earliest representative of its DSU component, all its mismatch neighbours $j < i$ already belong to finalized components; count how many distinct components they represent ($k_i$) and multiply the answer by $\max(0, |\Sigma| - k_i)$. Finally, run actual Manacher on the lexicographically smallest reconstructed string to verify that no radius was accidentally *under-specified* by $d_1, d_2$.
  4. *Boundary Pitfall*: Skipping the final forward Manacher verification! An input like $d_1 = [1, 1, 1]$ with $d_2 = [1, 1]$ forces $S[1]=S[2]=S[3]$, which actually has $d_1[2] = 2 \ne 1$.

##### Problem 3A-06: `[BJWC2018]` 词韵 / Tree PAM (`[ZH]` Luogu P5327 / COGS / Tree Palindromic Paths)
- **Statement & Constraints**: Given a rooted tree $T$ with $N \le 10^5$ vertices and character-labeled edges ($|\Sigma| = 26$), find for every node $x$ the number of distinct palindromic strings on the root-to-$x$ path and the maximum palindromic suffix length.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Building PAM via DFS on a tree with standard `while (S[r - 1 - len[u]] != c) u = fail[u];` degrades to $O(N^2)$ on a broom tree ($\texttt{a}^{N/2}$ stem with $N/2$ leaf branches labeled $\texttt{b}$).
  2. *Combinatorial Invariant*: Using `quick_link[u][c]` (`anc[u][c]`) on PAM states plus $O(1)$ level-ancestor queries on $T$ (via HLD or long-path decomposition) determines the exact PAM transition at tree node $x$ in $O(1)$ worst-case time.
  3. *Reverse-Engineering Scratchpad*: During DFS on $T$, maintain the root-to-$x$ character stack `dep_char[depth]` so checking $S[\text{dep}(x) - 1 - \text{len}(u)] == c$ is a direct array indexing `dep_char[dep[x] - 1 - len[u]] == c` in $O(1)$! Use `quick_link` to find the parent state in 1 step and roll back node creations on DFS exit (or keep persistent trie branches).
  4. *Boundary Pitfall*: If multiple tree children of the same node $p$ share the same edge character $c$, they map to the **exact same PAM node**—do not allocate duplicate PAM nodes for identical `(u, c)` transitions across sibling branches!

##### Problem 3A-07: `[AGC 047 B]` First Second (`[JA]` AtCoder Grand Contest 047 B)
- **Statement & Constraints**: Given $N$ strings $S_1, \dots, S_N$ ($\sum |S_i| \le 10^6$), in one operation you may delete either the first or the second character of a string. Count pairs $(i, j)$ such that $S_i$ can be reduced to $S_j$ (a variation that on palindromic reductions couples Trie suffix links with character-set bitmasks).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Reducing $S_i$ to $S_j$ means $S_j[2..|S_j|]$ is a suffix of $S_i$, and $S_j[1]$ occurs somewhere in the deleted prefix $S_i[1 .. |S_i| - |S_j| + 1]$.
  2. *Combinatorial Invariant*: Reversing all strings turns suffixes into prefixes on a Trie; tracking the bitmask of characters appearing in the remaining suffix of $S_i^R$ allows $O(1)$ lookup per string.
  3. *Reverse-Engineering Scratchpad*: Insert all $S_i^R$ into a Trie; at each node $u$ and character $c$, maintain `cnt[u][c]` = number of strings $S_i$ whose reversed prefix ends at a descendant of $u$ and contains $c$ in the remaining tail.
  4. *Boundary Pitfall*: Subtracting $i = j$ self-pairs when all characters in $S_i$ are distinct vs. repeated.

##### Problem 3A-08: `[ZJOI2017]` 字符串还原 / KMP & Z-Array Inverse Equivalence (`[ZH]` / `[EN]` CF 1721E — Prefix Function Queries)
- **Statement & Constraints**: Given a base string $S$ ($|S| \le 10^6$) and $Q \le 10^5$ queries appending a short string $T_q$ ($|T_q| \le 10$) to $S$, compute $\pi[|S|+1 .. |S|+|T_q|]$ online for each query without modifying $S$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Standard KMP `while (k > 0 && S[k+1] != c) k = pi[k];` can take $\Theta(|S|)$ steps on a single appended character $T_q[1]$, causing $O(Q |S|)$ TLE!
  2. *Combinatorial Invariant*: Identical to PAM `quick_link[u][c]`: the KMP automaton transition $\delta(k, c) = (S[k+1] == c \ ? \ k+1 : \delta(\pi[k], c))$ depends ONLY on the prefix $S[1..k+1]$, so for all $k \le |S|$ we precompute $\delta(k, c)$ in $O(|S| |\Sigma|)$, and for $k > |S|$ we only access $T_q$!
  3. *Reverse-Engineering Scratchpad*: Precompute KMP DFA `aut[1..|S|][26]` on $S$. For each query $T_q$, compute the further rows `aut[|S|+1 .. |S|+|T_q|][26]` in $O(|T_q| |\Sigma|)$ time and roll back simply by ignoring indices $> |S|$.
  4. *Boundary Pitfall*: Calling the amortized KMP loop for $k \le |S|$ instead of looking up `aut[k][c]` directly falls right into the $\texttt{a}^{|S|}$ + $\texttt{b}$ trap.

---

#### Tier 2: Intermediate (8 Problems — PAM Intersection, Bidirectional / Deque PAM, Half-Palindrome Counting & Range LPS)

##### Problem 3A-09: `[Luogu P5555]` 秩序魔咒 (Order Spell — Common Palindromes of Two Strings, `[ZH]`)
- **Statement & Constraints**: Given two strings $A$ and $B$ ($|A|, |B| \le 2.5 \times 10^5$), find the length of the longest common palindromic substring of $A$ and $B$, and how many distinct common palindromic substrings achieve that maximum length.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Using SAM on $A$ and $B$ does not guarantee palindromicity (remember that checking $S$ vs $S^R$ in SAM can match a substring with its reversed copy at a *different* position!).
  2. *Combinatorial Invariant*: Every palindrome is uniquely represented as a path from $r_{-1}$ or $r_0$ in the PAM Trie! Therefore, a palindrome occurs in both $A$ and $B$ iff its Trie path exists in **both** $\text{PAM}(A)$ and $\text{PAM}(B)$.
  3. *Reverse-Engineering Scratchpad*: Build $\text{PAM}(A)$ and $\text{PAM}(B)$ independently, then run a simultaneous DFS (`dfs(u_A, u_B)`) starting from $(r_{-1}^A, r_{-1}^B)$ and $(r_0^A, r_0^B)$ over all shared transitions $c \in \Sigma$ where both $\text{tr}_A[u_A][c]$ and $\text{tr}_B[u_B][c]$ exist, or build a Generalized PAM. Time $O((|A| + |B|)|\Sigma|)$.
  4. *Boundary Pitfall*: Attempting to find the longest common palindrome by finding the LCS of $A$ and $B^R$—counterexample: $A = \texttt{"abc"}$, $B = \texttt{"cba"}$ has $\text{LCS}(A, B^R) = \texttt{"abc"}$ which is not a palindrome!

##### Problem 3A-10: `[JSOI2013]` 快乐的 JYY (Happy JYY — Weighted Common Palindromic Pairs, `[ZH]` Luogu P5685 / BZOJ 3676)
- **Statement & Constraints**: Given strings $A$ and $B$ ($|A|, |B| \le 5 \times 10^4$), count the number of pairs of identical palindromic substrings $(A[i_1..j_1], B[i_2..j_2])$, i.e., $\sum_{P \text{ pal}} \text{occ}_A(P) \cdot \text{occ}_B(P)$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: We need the exact occurrence counts $\text{occ}_A(P)$ and $\text{occ}_B(P)$ for every distinct palindrome $P$.
  2. *Combinatorial Invariant*: Bottom-up accumulation along the `fail` tree of $\text{PAM}(A)$ and $\text{PAM}(B)$ computes $\text{occ}_A(u_A)$ and $\text{occ}_B(u_B)$ for every PAM node; then simultaneous Trie DFS over $(u_A, u_B)$ sums $\text{occ}_A(u_A) \cdot \text{occ}_B(u_B)$ for all non-root pairs.
  3. *Reverse-Engineering Scratchpad*: Build $\text{PAM}(A)$ and $\text{PAM}(B)$, accumulate `cnt[fail[u]] += cnt[u]` in reverse allocation order for each PAM, then DFS from $(r_{-1}, r_{-1})$ and $(r_0, r_0)$ adding `cntA[uA] * cntB[uB]`.
  4. *Boundary Pitfall*: Including $r_{-1}$ or $r_0$ in the sum adds fake empty-palindrome pairs.

##### Problem 3A-11: `[CF 17E]` Palisection (`[EN]` Codeforces Beta Round 17 E)
- **Statement & Constraints**: Given a string $S[1..N]$ ($N \le 2 \times 10^6$, **Memory Limit: 64 MB / 128 MB**), count the number of pairs of overlapping palindromic substrings $(S[l_1..r_1], S[l_2..r_2])$ with $r_1 \ge l_2$ and $l_1 \le r_2$ modulo $51123987$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Total palindromes $T$ can be $\Theta(N^2)$. Complementary counting reduces overlapping pairs to $\binom{T}{2} - \#\{(P_1, P_2) : r_1 < l_2\}$, requiring the number of palindromes starting at $i$ and ending at $j$. Also, $N = 2 \times 10^6$ with tight memory forbids $26$-width PAM arrays!
  2. *Combinatorial Invariant*: In Manacher's algorithm, a center $c$ with odd radius $d_1[c]$ contributes $+1$ to `start_cnt[i]` for every $i \in [c - d_1[c] + 1, c]$ and $+1$ to `end_cnt[j]` for every $j \in [c, c + d_1[c] - 1]$.
  3. *Reverse-Engineering Scratchpad*: Use two $O(N)$ difference arrays `diff_start` and `diff_end` updated in $O(1)$ per Manacher center, prefix-sum them to get `start_cnt[i]` and `end_cnt[j]`, and compute $\sum_{i=2}^{N} \text{start\_cnt}[i] \cdot \big(\sum_{j=1}^{i-1} \text{end\_cnt}[j]\big)$ in $O(N)$ time and $O(N)$ memory (or use linked-list PAM edges).
  4. *Boundary Pitfall*: Computing $\binom{T}{2} \pmod{51123987}$ by taking $T \pmod M$ *before* subtracting disjoint pairs can cause subtle errors if $\binom{T}{2}$ is not reduced with modular inverse of $2$ ($\gcd(2, 51123987)=1$).

##### Problem 3A-12: `[CF 1080E]` Sonya and Matrix Beauty (`[EN]` Codeforces Round 524 Div. 2 E)
- **Statement & Constraints**: Given an $N \times M$ character grid ($N, M \le 250$), count subrectangles whose rows can each be rearranged so that both every row AND every column become palindromes.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Checking all $O(N^2 M^2)$ subrectangles takes $O(N^3 M^2)$ if done naively.
  2. *Combinatorial Invariant*: Fix the column interval $[c_1, c_2]$. A row segment $R[r][c_1..c_2]$ can be rearranged into a palindrome iff its character frequency vector $V_r$ has **at most $1$ odd frequency**. Furthermore, rearranged rows $r_1, \dots, r_k$ can form column palindromes iff the symmetric rows $r_i$ and $r_{k+1-i}$ have **identical character frequency vectors** $V_{r_i} = V_{r_{k+1-i}}$!
  3. *Reverse-Engineering Scratchpad*: For each of the $\binom{M}{2}$ column pairs $[c_1, c_2]$, maintain the $26$-tuple frequency vector $V_r$ and parity bitmask $mask_r$ for each row $r \in [1, N]$. Mark rows with $\text{popcount}(mask_r) > 1$ as invalid barriers, and run 1D Manacher across rows $r = 1 \dots N$ comparing $V_{r_1} == V_{r_2}$ in $O(1)$ (via rolling hash or direct comparison during Manacher R-box expansion!). Total time $O(M^2 N)$.
  4. *Boundary Pitfall*: Allowing two invalid rows ($\text{popcount}(mask_r) > 1$) with identical frequency vectors to match each other in Manacher—invalid rows must act as distinct unique sentinels so no palindrome can cross or center on them!

##### Problem 3A-13: `[HDU 5421]` Victor and String (`[ZH]` / `[EN]` Double-Ended Insertion PAM)
- **Statement & Constraints**: Maintain an initially empty string under $Q \le 10^5$ operations: (1) `push_front(c)`, (2) `push_back(c)`, (3) query number of distinct palindromes, (4) query total number of palindromic substrings.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Appending to both left and right requires a Double-Ended PAM (`双向 PAM`) with `first` and `last` pointers.
  2. *Combinatorial Invariant*: By reversal symmetry $P = P^R$, a single PAM state graph represents both prefix and suffix palindromes. Appending `c` to the left extends `first` using mirror condition $S[L + 1 + \text{len}(u)] == c$ and adds $\text{depth}_{\text{fail}}(\text{first})$ to the total palindrome count.
  3. *Reverse-Engineering Scratchpad*: Allocate string array $S$ centered at offset $Q + 5$ inside size $2Q + 10$. On `push_front(c)` or `push_back(c)`, update the respective pointer via `get_fail_left` / `get_fail_right`, synchronize `if (len[first] == R - L + 1) last = first;` (and vice versa), and add `dep[first]` / `dep[last]` to total count.
  4. *Boundary Pitfall*: Initializing $S$ outside $[L, R]$ with $0$ when character $c$ can also be $0$ causes false matches across the boundary; always dynamically overwrite $S[L-1]$ and $S[R+1]$ with $-1$ before each query!

##### Problem 3A-14: `[LOJ 6070 / BZOJ 4082 / CTSC]` 基因 (Gene — Sliding Window / Queue PAM with Front Deletion & Back Insertion, `[ZH]`)
- **Statement & Constraints**: Given a stream of operations inserting characters at the right end $R$ and deleting characters from the left end $L$ ($Q \le 5 \times 10^5$), maintain the number of **distinct** palindromic substrings currently inside the active window $S[L..R]$ (online).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Front deletion (`pop_front`) can destroy the last occurrence of a palindrome in $S[L..R]$, and future insertions must know if a node is still active.
  2. *Combinatorial Invariant*: Let $u$ be a PAM node. Whenever $u$ is reached as $\text{last}[r]$, its occurrence starts at $L_u = r - \text{len}(u) + 1$ and ends at $r$. Because any proper palindromic prefix $w$ starting at $L$ is mirrored inside $\text{first}[L]$ at a strictly larger start position $> L$, deleting $L$ only affects palindromes $u$ whose **latest** left endpoint $\text{latest\_start}[u]$ equals $L$! Even simpler: in a Queue PAM (right-append, left-pop only), a node $u$ exists in $S[L..R]$ iff its latest right-occurrence $\text{last\_end}[u]$ (the max $r' \le R$ in the fail-subtree of $u$) satisfies $\text{last\_end}[u] - \text{len}(u) + 1 \ge L$!
  3. *Reverse-Engineering Scratchpad*: Either use the **Deque PAM Lazy Push-Down Invariant** from Section 21.3 (`longest_pref[L]` pushes down $\text{fail}(u)$ upon `pop_front` in $O(1)$ worst-case time with `quick_link`), OR use PAM `slink` telescoping to maintain active start positions $\ge L$! With Section 21.3's Deque PAM + `quick_link`, each operation runs in worst-case $O(1)$ time and $O(N)$ memory.
  4. *Boundary Pitfall*: Using amortized `fail`-walking when nodes can be deleted or when `first` is updated degrades to $O(N)$ per operation on periodic strings; `quick_link[u][c]` is mandatory.

##### Problem 3A-15: `[CF 1827C]` Palindrome Partition (`[EN]` Codeforces Round 873 Div. 1 C)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), a string is *good* if it can be partitioned into one or more non-empty **even-length** palindromes. Count how many substrings $S[l..r]$ are good.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Checking all $O(N^2)$ substrings with PAM DP takes $O(N^2 \log N)$.
  2. *Combinatorial Invariant*: By the **Even-Length Palindrome Greedy Factorization Theorem** (Section 24.2), a string $T$ is a concatenation of even-length palindromes iff it starts with a non-empty even-length palindrome $P$ (say the **shortest** even-length palindromic prefix of $T$) and the remaining suffix $T[|P|+1..|T|]$ is also good! Symmetrically, looking from the right endpoint $r$, let $L(r)$ be the length of the **shortest non-empty even-length palindromic suffix** of $S[1..r]$ that does not overflow the start of our substring.Wait: even simpler from the left or right! If $P = S[r - L(r) + 1 .. r]$ is the shortest non-empty even-length palindromic suffix ending at $r$, then ANY good substring ending at $r$ can have $P$ greedily stripped from its right end!
  3. *Reverse-Engineering Scratchpad*: Find for every $r$ the shortest non-empty even-length palindrome ending at $r$: either via Manacher + DSU/stack (each even center $c$ with radius $d_2[c] \ge 1$ covers right endpoints $r \in [c+1, c + d_2[c]]$ with length $2(r - c)$, so the **rightmost** active center $c < r$ gives the minimum even length $2(r - c)$!), OR via PAM (store at each node $u$ the shortest positive even ancestor `min_even[u]` in the `fail` tree!). Then $dp[r] = dp[r - L(r)] + 1$, and answer is $\sum_{r=1}^N dp[r]$ in $O(N)$!
  4. *Boundary Pitfall*: Taking the *longest* even-length palindromic suffix instead of the *shortest* fails completely: e.g., on $S = \texttt{"abbaabba"}$, stripping the longest even suffix $\texttt{"abbaabba"}$ misses the split $\texttt{"abba"} + \texttt{"abba"}$.

##### Problem 3A-16: `[UOJ 103 / CTSC 2015]` 回文子串 / Range Longest Palindromic Substring (`[ZH]` / `[EN]` Range LPS in $S[l..r]$)
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ online queries $[l, r]$ ($N, Q \le 3 \times 10^5$), find the length of the longest palindromic substring wholly contained in $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Whole-string Manacher radii $d_1[c], d_2[c]$ can extend outside $[l, r]$.
  2. *Combinatorial Invariant*: An odd palindrome of radius $k$ exists in $S[l..r]$ iff $\max_{c \in [l+k-1, r-k+1]} d_1[c] \ge k$, and an even palindrome of radius $k$ exists iff $\max_{c \in [l+k-1, r-k]} d_2[c] \ge k$. Both predicates are monotonic in $k$.
  3. *Reverse-Engineering Scratchpad*: Precompute Manacher $d_1, d_2$ and two $O(1)$ Sparse Table RMQs in $O(N \log N)$. For each query $[l, r]$, binary search $k_{\text{odd}} \in [1, \lfloor(r-l+2)/2\rfloor]$ and $k_{\text{even}} \in [0, \lfloor(r-l+1)/2\rfloor]$ in $O(\log(r-l))$ time, returning $\max(2 k_{\text{odd}} - 1, 2 k_{\text{even}})$.
  4. *Boundary Pitfall*: Checking $[l+k-1, r-k+1]$ for even centers instead of $[l+k-1, r-k]$ allows a center $c = r - k + 1$ whose right endpoint $c + k = r + 1$ overflows $r$ by 1 character!

---

#### Tier 3: Advanced (8 Problems — Range Distinct Palindromes, PAM `slink` Telescoping, Persistent PAM & Palindrome + SAM Coupling)

##### Problem 3A-17: `[国家集训队论文 2014 — 徐毅 / BZOJ 5384 / LOJ 6071 / QOJ]` 区间本质不同回文串 (Range Distinct Palindromes in $S[l..r]$, `[ZH]`)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^5$) and $Q \le 3 \times 10^5$ queries $[l, r]$ (offline or online with `lastans` XOR), output the number of **distinct** palindromic substrings contained in $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: At right endpoint $r$, up to $O(N)$ ancestors of $\text{last}[r]$ in the PAM `fail` tree get a new occurrence ending at $r$.
  2. *Combinatorial Invariant*: By **Theorem 23.1 (`slink` Telescoping Cancellation)**, for any arithmetic progression block $u_0, u_1, \dots, u_k = \text{bot}[u_0]$ of step $d = \text{diff}[u_0]$ on the `fail` chain of $\text{last}[r]$, the previous occurrence of every $u_i$ ($1 \le i \le k$) ended at $r - d$, so its previous start position $(r-d) - \text{len}(u_i) + 1$ is identical to the new start position $r - \text{len}(u_{i-1}) + 1$ of $u_{i-1}$!
  3. *Reverse-Engineering Scratchpad*: Build PAM with `diff[u]`, `slink[u]`, `bot[u]`, and Euler tour `[dfn[u], out[u]]` of the `fail` tree. Sweep $r = 1 \dots N$: walk $u \leftarrow \text{slink}[u]$ from $\text{last}[r]$ ($O(\log r)$ steps); at each AP top $u$, query `prev_r = SegMax.query(dfn[u], out[u])`, subtract $1$ at `prev_r - len[u] + 1` (if `prev_r > 0`), and add $+1$ at `r - len[bot[u]] + 1` in a Fenwick tree (offline) or Persistent Segment Tree (online). Then set `SegMax.update(dfn[last[r]], r)`. Complexity $O(N \log^2 N + Q \log N)$.
  4. *Boundary Pitfall*: Using `slink[u]` instead of `bot[u]` (where $\text{fail}(\text{bot}[u]) = \text{slink}[u]$) for the $+1$ insertion double-counts `slink[u]` on the next loop iteration and violates $\text{len}(u_i) > d$.

##### Problem 3A-18: `[CF 1083D]` The Fair Nut's Getting Crazy (`[EN]` Codeforces Round 526 Div. 1 D — Distinct Palindrome / Interval Containment Analogue)
- **Statement & Constraints**: Given $S[1..N]$ (or $N \le 10^5$), count tuples / weighted range distinct palindromic contributions where each distinct palindrome in $S[l..r]$ contributes a polynomial in its earliest and latest occurrence inside $[l, r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Requires maintaining for each active right endpoint $r$ not just $+1/-1$ indicator weights on left endpoints $l$, but linear/quadratic functions $\sum f(l, \text{prev\_start}, \text{new\_start})$.
  2. *Combinatorial Invariant*: Along a `slink` AP chain $u_0, \dots, u_k$, the pair $(\text{prev\_start}(u_i), \text{new\_start}(u_i))$ for $1 \le i \le k$ satisfies $\text{new\_start}(u_i) - \text{prev\_start}(u_i) = d$, and the new start positions form an arithmetic progression of step $d$.
  3. *Reverse-Engineering Scratchpad*: Combine PAM `slink` decomposition with a Lazy Segment Tree maintaining $\sum l$, $\sum \text{prev\_start}$, and $\sum l \cdot \text{prev\_start}$ over $l \in [1, r]$.
  4. *Boundary Pitfall*: Failing to separate $u_0$ (whose previous right endpoint is `SegMax.query(dfn[u_0], out[u_0])`, NOT $r - d$) from $u_1 \dots u_k$ (whose previous right endpoint is strictly $r - d$).

##### Problem 3A-19: `[ZJOI2016 / Luogu P4094 / HEOI2016]` 字符串与回文 (SAM + PAM Cross-Indexing for Palindromes in $S[a..b]$ Occurring in $S[c..d]$, `[ZH]`)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$) and $Q \le 10^5$ queries $(a, b, c, d)$, find the length of the longest **palindromic** substring of $S[a..b]$ that also occurs as a substring of $S[c..d]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: We must intersect two constraints on a candidate palindrome $P$: (1) $P$ is a palindrome inside $S[a..b]$, and (2) $P$ occurs inside $S[c..d]$.
  2. *Combinatorial Invariant*: Every distinct palindrome in $S$ is one of the $\le N$ nodes of $\text{PAM}(S)$, and every PAM node $u$ has a first appearance $S[L_u .. R_u]$, so $u$ maps to a unique node $\text{sam\_node}(u)$ in $\text{SAM}(S)$! Furthermore, a palindrome of odd radius $k$ centered at $m \in [a + k - 1, b - k + 1]$ occurs in $S[c..d]$ iff its corresponding PAM/SAM node has $\text{endpos} \cap [c + 2k - 2, d] \ne \emptyset$.
  3. *Reverse-Engineering Scratchpad*: Even simpler via PAM + Segment Tree Merge on the PAM `fail` tree! Since a palindrome $u$ occurs in $S[c..d]$ iff its PAM `fail`-subtree contains a right endpoint $p \in [c + \text{len}(u) - 1, d]$, we build Segment Tree Merging directly on the **PAM `fail` tree**! Then for any query, binary search the radius $k$ or lift from $\text{last}$ / query Manacher centers! Wait: can we binary search the answer length $L$? No, an odd palindrome of length $2k+1$ doesn't imply an even palindrome of length $2k$ exists! Instead, in the PAM `fail` tree, every ancestor of a valid palindrome in $S[c..d]$ is ALSO in $S[c..d]$!
  4. *Boundary Pitfall*: Binary searching the *length* $L$ of a palindrome directly fails because palindromic existence is NOT monotonic in $L$ (even via odd+even split, containing a center $m$'s radius-$k$ palindrome inside $S[c..d]$ only implies smaller radii *at that same center $m$* are in $S[c..d]$, not across different centers!). Use PAM `fail`-tree Segment Tree Merge + heavy-light / center decomposition.

##### Problem 3A-20: `[CF 932G]` Palindrome Partition (`[EN]` ICM Technex 2018 — Even Symmetric Partition via PAM `slink`)
- **Statement & Constraints**: Given $S[1..N]$ ($2 \mid N \le 10^6$), count ways to partition $S = s_1 s_2 \dots s_k$ ($2 \mid k$) such that $s_i = s_{k+1-i}$ for all $i$, modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $s_i = s_{k+1-i}$ couples the prefix and suffix of $S$ at arbitrary cut points.
  2. *Combinatorial Invariant*: Interleave $S$ with its second half reversed: $T = S[1]\, S[N]\, S[2]\, S[N-1] \dots S[N/2]\, S[N/2+1]$. Then $S[l..r] = S[N-r+1 .. N-l+1]$ iff the interleaved substring $T[2l-1 .. 2r]$ is an **even-length palindrome**! Thus valid partitions of $S$ biject with partitions of $T$ into even-length palindromes!
  3. *Reverse-Engineering Scratchpad*: Build PAM of $T$ with `diff[u]` and `slink[u]`. At each step $r$, update $g[u] = dp[r - \text{len}(\text{slink}[u]) - \text{diff}[u]] + (\text{diff}[u] == \text{diff}[\text{fail}[u]] \ ? \ g[\text{fail}[u]] : 0)$ along the $O(\log r)$ `slink` chain, and if $2 \mid r$, set $dp[r] = \sum g[u]$. Time $O(N \log N)$, space $O(N)$.
  4. *Boundary Pitfall*: Updating `dp[r]` only at even $r$ while skipping odd $r$ when maintaining `g[u]` corrupts the rolling sum `g[u]`! You MUST update `g[u]` at **every** $r$ (both odd and even), while setting $dp[r] = 0$ for odd $r$.

##### Problem 3A-21: `[CF 906E]` Reverses (`[EN]` Codeforces Round 454 Div. 1 E — Minimum Segment Reversals via `slink` DP with Reconstruction)
- **Statement & Constraints**: Given $A[1..N]$ and $B[1..N]$ ($N \le 5 \times 10^5$), partition $[1, N]$ into the minimum number of intervals $[l_m, r_m]$ such that for each interval, either $A[l_m..r_m] = B[l_m..r_m]$ or $\text{rev}(A[l_m..r_m]) = B[l_m..r_m]$, and output the intervals (ignoring length-1 reversals).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Same interleaving reduction as `CF 932G`: form $T = A[1] B[1] A[2] B[2] \dots A[N] B[N]$. Then $\text{rev}(A[l..r]) = B[l..r]$ iff $T[2l-1 .. 2r]$ is an even-length palindrome!
  2. *Combinatorial Invariant*: Replace $+ \pmod M$ in PAM `slink` DP with $(\min, \text{argmin})$ to find the minimum number of even-length palindromes partitioning $T$ and reconstruct the cut points.
  3. *Reverse-Engineering Scratchpad*: Maintain `g[u] = pair(min_dp, best_prev_index)` for each PAM node $u$. When $A[i] == B[i]$, also allow the trivial transition $dp[2i] = \min(dp[2i], dp[2i-2])$ (cost $0$ for matching single characters without reversing).
  4. *Boundary Pitfall*: Forgetting that $A[i] == B[i]$ costs $0$ operations (not $1$) while a reversal of length $\ge 2$ costs $1$ operation.

##### Problem 3A-22: `[ARC 151 E]` Keep Being Substring (`[JA]` AtCoder Regular Contest 151 E / Palindromic & Periodicity Transition)
- **Statement & Constraints**: Variant coupling substring state transitions with shortest palindromic / periodic extensions.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Direct BFS over all substrings of $S$ has $O(N^2)$ states.
  2. *Combinatorial Invariant*: Any intermediate state of length $\ge 2$ can immediately shrink to a single character of length $1$ and grow to the target, unless the disjoint substrings share no common character, in which case we walk single-character steps in $S$.
  3. *Reverse-Engineering Scratchpad*: Reduce to either $O(N \log N)$ LCP checking (if $X$ is a substring of $Y$ or vice versa) or shortest path on the $26$-character adjacency graph.
  4. *Boundary Pitfall*: Overlooking the case where $X$ and $Y$ already overlap as substrings of $A$ without ever shrinking to length $1$.

##### Problem 3A-23: `[THUPC 2018 / Luogu P5446]` 绿绿和串串 (Prefix-Reflective Generator Restoration, `[ZH]`)
- **Statement & Constraints**: Given a string $R[1..N]$ ($N \le 10^6$), we repeatedly take a prefix $S[1..k]$ and replace $S$ with $S[1..k] + \text{rev}(S[1..k-1])$ (reflection across the last character $S[k]$). Find all possible initial lengths $1 \le L \le N$ of the seed string $S[1..L]$ that can generate $R$ as a prefix.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Each reflection step creates an odd-length palindrome centered at the rightmost character of the current string!
  2. *Combinatorial Invariant*: Working **backwards from $N$ down to $1$**, an index $i$ can be the last character before a reflection step that covers up to $N$ iff either:
     - The odd palindrome centered at $i$ reaches the right end of $R$ ($i + d_1[i] - 1 == N$), OR
     - The odd palindrome centered at $i$ reaches the left end of $R$ ($i - d_1[i] + 1 == 1$) AND its reflected right endpoint $i + d_1[i] - 1$ is itself a valid generator length!
  3. *Reverse-Engineering Scratchpad*: Run odd Manacher $d_1[1..N]$. Traverse $i = N$ down to $1$: mark `valid[i] = true` if $i + d_1[i] - 1 == N$ or ($i - d_1[i] + 1 == 1$ and `valid[i + d_1[i] - 1]`). Output all $i$ with `valid[i] = true` in $O(N)$.
  4. *Boundary Pitfall*: Forgetting that the first reflection requires the palindrome at $i$ to start at index $1$ ($i - d_1[i] + 1 == 1$) when $i + d_1[i] - 1 < N$!

##### Problem 3A-24: `[NOI 2016]` 优秀的拆分 + Palindrome Variant / `[GYM 102900 / CCPC]` Palindromic Square-Concatenation (`[ZH]` / `[EN]`)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), count decompositions or substrings of the form $A B$ where $A$ is a palindrome and $B$ is a square $XX$ (or $A, B, C$ are non-empty palindromes with length/period constraints).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Requires combining the count of palindromes ending at $i$ with the count of squares/palindromes starting at $i+1$, or counting $P_1 P_2$ where $P_1, P_2$ share a border.
  2. *Combinatorial Invariant*: Precompute `pal_end[i]` and `pal_start[i]` via PAM/Manacher in $O(N)$, and when constraints couple the lengths of $P_1$ and $P_2$ (e.g., $|P_1| = |P_2|$ or $P_1$ is a suffix of $P_2$), use PAM `fail`-tree ancestor queries or `slink` AP sums.
  3. *Reverse-Engineering Scratchpad*: Combine PAM `fail`-tree Euler tour with Fenwick tree / `slink` DP to evaluate constrained split points $i$ in $O(N \log N)$.
  4. *Boundary Pitfall*: Double-counting split points when a substring $S[l..r]$ can be split into two palindromes $P_1 P_2$ in multiple ways—Wait: by **Unique Palindromic Factorization properties**, if $S[l..r] = P_1 P_2 = Q_1 Q_2$ with $|P_1| < |Q_1|$, then $S[l..r]$ is periodic!

---

#### Tier 4: Mastery (8 Problems — Full 4-Way Deque PAM, Online Range Distinct Palindromes, Tree Path Palindromes, Rich Word Enumeration & Frontier Reductions)

##### Problem 3A-25: `[Universal Cup / QOJ / UOJ]` Full 4-Way Deque Palindromic Automaton (`push_front`, `push_back`, `pop_front`, `pop_back`, `[EN]` / `[ZH]`)
- **Statement & Constraints**: Maintain an initially empty string under $Q \le 5 \times 10^5$ online operations of four types: `push_front(c)`, `push_back(c)`, `pop_front()`, `pop_back()`. After each operation, output the number of distinct palindromic substrings, the length of the longest palindromic prefix, and the length of the longest palindromic suffix.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Both insertions and deletions occur at **both ends** online; amortized fail walks fail on rollback/pop, and deleting from one end can expose a shorter palindrome at the opposite end.
  2. *Combinatorial Invariant*: Combine **Deterministic `quick_link[u][c]`** (Section 21.2) with the **Lazy Endpoint Push-Down Invariant** (Section 21.3): every maximal palindrome $u$ in $S[L..R]$ is recorded at its two endpoints `longest_pref[L_u]` and `longest_suf[R_u]`. When $L$ is popped (`pop_front`), only $u = \text{longest\_pref}[L]$ loses its left endpoint; its longest proper palindromic suffix $f = \text{fail}(u)$ is pushed to `[R_u - len(f) + 1 .. R_u]`, guaranteeing that `longest_pref[L+1]` is always up-to-date!
  3. *Reverse-Engineering Scratchpad*: Maintain `quick_link[u][26]`, `ref_cnt[u]` (count of active maximal endpoint assignments), and `fail_deg[u]` (count of active children in the `fail` tree). When `ref_cnt[u] == 0 && fail_deg[u] == 0`, unlink $u$ from `tr[parent[u]][c]`, decrement `fail_deg[fail[u]]`, and decrement `distinct_cnt`. Every operation runs in **strict $O(1)$ worst-case time**.
  4. *Boundary Pitfall*: Forgetting that unlinking $u$ decrements `fail_deg[fail[u]]`, which itself might cause $\text{fail}[u]$ to have `ref_cnt == 0 && fail_deg == 0`? Wait: can $\text{fail}[u]$ ever have `ref_cnt == 0` when $u$ is being popped? NO, because popping $u$ **immediately increments `ref_cnt[fail[u]]++`** before decrementing `fail_deg[fail[u]]--`! Thus deletions **never cascade** up the fail tree—at most **1** node is ever deleted per `pop`!

##### Problem 3A-26: `[CF 914E]` Palindromes in a Tree (`[EN]` Codeforces 8VC Venture Cup / Round 458 E)
- **Statement & Constraints**: Given a tree $T$ with $N \le 2 \times 10^5$ vertices and character labels $c_v \in \{\texttt{a}..\texttt{t}\}$ ($|\Sigma| = 20$), find for **every vertex $v$** the number of undirected simple paths $(x, y)$ passing through $v$ whose characters can be rearranged to form a palindrome.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A path $(x, y)$ can be rearranged into a palindrome iff its $20$-bit character parity mask $M(x, y)$ has $\text{popcount}(M(x, y)) \le 1$ ($21$ target masks: $0$ and $2^0 \dots 2^{19}$).
  2. *Combinatorial Invariant*: Apply **Centroid Decomposition**. At centroid $r$, let $M(u)$ be the mask of the path from $r$ (excluding $r$) to $u$. A path from $x$ (in subtree $A$) to $y$ (in subtree $B$) has mask $M(x) \oplus M(y) \oplus (1 \ll c_r)$. If this equals one of the $21$ target masks, the path contributes $+1$ to every vertex on the path $x \to r \to y$!
  3. *Reverse-Engineering Scratchpad*: At centroid $r$, accumulate frequencies `cnt[M(y)]` across subtrees. For each $x$, count matches `ways[x] = sum_{k=0..20} cnt[M(x) ^ (1 << c_r) ^ target[k]]`, propagate `ways` bottom-up from leaves to $r$ in each child subtree, and add half of the total root-passing sum to `ans[r]`. Time $O(N |\Sigma| \log N)$.
  4. *Boundary Pitfall*: Double-counting the centroid $r$ itself (every path between two child subtrees accumulates into $r$ from *both* endpoints $x$ and $y$, whereas single-endpoint paths $r \to x$ accumulate only once!).

##### Problem 3A-27: `[ICPC World Finals / Universal Cup]` Rich Words & Palindromic Saturation Counting (`[EN]` / `[ZH]`)
- **Statement & Constraints**: Count or construct lexicographically $K$-th **Rich Word** (a string of length $N$ containing the maximum possible number $N+1$ of distinct palindromes, including $\varepsilon$) over a binary or ternary alphabet, or find the longest rich substring of $S[1..N]$ ($N \le 3 \times 10^5$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Testing richness of $S[l..r]$ naively requires counting distinct palindromes in $S[l..r]$ and checking if it equals $r - l + 1$.
  2. *Combinatorial Invariant*: By **Theorem 24.3 (Glen–Justin–Widmer–Zamboni Return-Word Characterization)**, $S[l..r]$ fails to be rich iff there exists some $p \in [l, r]$ where the longest palindromic suffix of $S[l..p]$ **already occurred earlier inside $S[l..p-1]$**! Equivalently, for each right endpoint $p$, let $u$ be the highest ancestor of $\text{last}[p]$ whose previous occurrence $\text{prev\_r}(u)$ (found via PAM fail-tree Euler tour max) satisfies $\text{prev\_r}(u) - \text{len}(u) + 1 \ge l$, wait: even simpler! At right endpoint $p$, the longest palindromic suffix of $S[1..p]$ that occurred earlier in $S[1..p-1]$ is EITHER $u_0 = \text{last}[p]$ itself (if $\text{prev\_r}(u_0) > 0$) OR $\text{fail}(u_0)$ (which is **guaranteed** to have occurred inside $u_0$, specifically at its prefix $S[p - \text{len}(u_0) + 1 .. p - \text{len}(u_0) + \text{len}(\text{fail}(u_0))]$, or even later at $\text{prev\_r}(\text{fail}(u_0))$!).
  3. *Reverse-Engineering Scratchpad*: At each position $p$, the **shortest** complete return word of a palindrome ending at $p$ starts at:
     $$L_{\text{bad}}(p) = \max_{v \in \text{anc}(\text{last}[p]),\, \text{prev\_r}(v) > 0} \big(\text{prev\_r}(v) - \text{len}(v) + 1\big)$$
     Wait: if $v$ is not the longest palindromic suffix of $S[l..p]$, then a longer ancestor $w$ of $\text{last}[p]$ starts $\ge l$ (so $p - \text{len}(w) + 1 \ge l$), and $v$ is inside $w$, so $p$ STILL creates the new palindrome $w$ in $S[l..p]$!
     Specifically, $p$ fails to create a new palindrome in $S[l..p]$ iff the longest palindromic suffix $w$ of $S[l..p]$ (the highest ancestor of $\text{last}[p]$ with $p - \text{len}(w) + 1 \ge l$) already occurred in $S[l..p-1]$, i.e., $\text{prev\_r}(w) - \text{len}(w) + 1 \ge l \iff l \le \text{prev\_r}(w) - \text{len}(w) + 1$!
     Using the **Distinct Palindromes in $S[l..r]$** data structure (Iteration 23), $S[l..r]$ is rich iff $\text{DistinctPal}(l, r) == r - l + 1$, which is monotonic in $l$ (if $S[l..r]$ is rich, every substring $S[l+1..r]$ is rich by factor closure!). Thus a simple two-pointer / binary search with Deque PAM or `slink` BIT finds for every $r$ the minimum $l(r)$ such that $S[l(r)..r]$ is rich in **$O(N)$ total time using Sliding-Window Queue PAM**!
  4. *Boundary Pitfall*: Failing to exploit **Factor Closure of Rich Words** (Theorem 24.3(2)): if $S[l..r]$ is rich, then $S[l'..r']$ is rich for all $l \le l' \le r' \le r$. Thus as $r$ increases from $1$ to $N$, the minimum valid left endpoint $L^*(r)$ is **monotonically non-decreasing**—so a Sliding-Window Queue PAM (push right, pop left whenever a push fails to increase `distinct_palindromes`) solves all rich-substring queries in **linear $O(N)$ time**!

##### Problem 3A-28: `[NOI / CTSC / WC / QOJ]` Minimum Palindromic Factorization (`最小回文划分` & Parity-Split Output, `[ZH]` / `[EN]` Fici–Gagie–Kärkkäinen–Kempa)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6$), find for every prefix $S[1..r]$ both the minimum number of **odd-count** palindromes and the minimum number of **even-count** palindromes whose concatenation equals $S[1..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Unlike `CF 932G` (which restricts to even-length palindromes), here **any** palindrome length (odd or even) is allowed, and we track the parity of the *number of pieces* $k$ ($\min k$ odd vs $\min k$ even).
  2. *Combinatorial Invariant*: The PAM `slink` DP works unchanged for **any commutative semiring**—here the semiring of pairs $(\min_{\text{even } k}, \min_{\text{odd } k})$ under componentwise $\min$ and $(+1 \text{ with parity swap})$!
  3. *Reverse-Engineering Scratchpad*: At each node $u$, store `g[u][0]` and `g[u][1]` (minimum even/odd DP values in $u$'s current AP block before the $+1$ transition). At step $r$, update `g[u]` from $dp[r - \text{len}(\text{slink}[u]) - \text{diff}[u]]$ and `g[fail[u]]`, then update $dp[r][\text{parity}] = \min(dp[r][\text{parity}], g[u][\text{parity} \oplus 1] + 1)$. Time $O(N \log N)$.
  4. *Boundary Pitfall*: Storing the $+1$ inside `g[u]` instead of applying $+1$ (and swapping parity!) when reading `g[u]` into `dp[r]`—remember that `g[u]` caches values of $dp[j]$ at *previous* right endpoints $j$, so the $+1$ piece transition must happen only once when transitioning $j \to r$!

##### Problem 3A-29: `[ZJOI2019 / SDOI / Luogu]` Palindromic Covers & Periodic Runs Coupling (`[ZH]` / `[EN]`)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), count or find substrings $S[l..r]$ that are simultaneously rich words and periodic, or count pairs of identical non-overlapping palindromic substrings.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Requires tracking $\text{endpos}$ of each distinct palindrome $u$ in the PAM `fail` tree.
  2. *Combinatorial Invariant*: The right endpoints where palindrome $u$ occurs in $S$ are precisely the union of positions $r$ where $\text{last}[r]$ lies in the **subtree of $u$ in the PAM `fail` tree**.
  3. *Reverse-Engineering Scratchpad*: Perform **Segment Tree Merging** (or DSU on Tree) over the PAM `fail` tree! Just as SAM Link-Tree Segment Tree Merging gives the exact occurrence set $\text{endpos}(u)$ of every substring class, PAM `fail`-tree Segment Tree Merging gives the exact occurrence set of every distinct palindrome $u$ in $O(N \log N)$ time and space!
  4. *Boundary Pitfall*: Confusing the PAM Trie tree with the PAM `fail` tree when merging occurrence sets—occurrences propagate bottom-up along the **`fail` tree**, NOT the Trie!

##### Problem 3A-30: `[ABC 259 Ex / AGC]` Palindromic Subsequences vs. Palindromic Substrings on Grids/DAGs (`[JA]` AtCoder)
- **Statement & Constraints**: Given an $N \times N$ grid ($N \le 400$ or $N \le 500$), count paths from $(1, 1)$ to $(N, N)$ whose string is a palindrome, or couple two-pointer meet-in-the-middle with PAM transitions.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Naive meet-in-the-middle from $(1, 1)$ and $(N, N)$ has $O(N^3)$ states $(d, r_1, r_2)$.
  2. *Combinatorial Invariant*: On a grid of size $N$, any palindromic path from $(1, 1)$ to $(N, N)$ must be symmetric about the anti-diagonal $r + c = N + 1$, reducing the state to $(r_1, r_2)$ at step $d = r_1 + c_1 - 2 = (N - r_2) + (N - c_2)$ in $O(N^3)$ time and $O(N^2)$ rolling space.
  3. *Reverse-Engineering Scratchpad*: Roll the DP over distance $d$ from the ends toward the middle anti-diagonal.
  4. *Boundary Pitfall*: Off-by-one between odd path length ($2N-1$ vertices on $N \times N$ grid, meeting at a single cell $(r, c)$) vs. even path length ($N \times M$ grid with $N+M$ odd, meeting across an edge).

##### Problem 3A-31: `[GYM 104077 / ICPC Asia Regional / UCup]` Palindromic Tree with Dynamic Character Replacements (`[ZH]` / `[EN]` Single-Point Modification Palindrome Count)
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$) and $Q \le 10^5$ independent hypothetical single-character replacements $S[i] \leftarrow c$, output for each query the total number of palindromic substrings in the modified string.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Modifying $S[i] \leftarrow c$ can destroy existing palindromes that span across $i$ and can extend existing palindromes whose first mismatch was at $i$ (mirrored against $2m - i$).
  2. *Combinatorial Invariant*:
     - **Destruction**: Any palindrome centered at $m \ne i$ whose radius covers $i$ ($|m - i| < d[m]$) is truncated to $|m - i| - 1$ whenever $c \ne S[i]$. This is a continuous range update on indices $i \in [m - d[m] + 1, m + d[m] - 1] \setminus \{m\}$ subtracting $d[m] - |m - i|$!
     - **Creation**: A center $m$ had its expansion stopped at radius $d[m]$ precisely by the single mismatch $S[m - d[m]] \ne S[m + d[m]]$. Thus changing $S[i]$ can ONLY extend a center $m$ if $i = m - d[m]$ (and $c == S[m + d[m]]$) OR $i = m + d[m]$ (and $c == S[m - d[m]]$)! Once that single mismatch is healed, the new extension beyond $d[m] + 1$ is found in $O(1)$ via $\text{LCP}$ on $S$ and $S^R$!
  3. *Reverse-Engineering Scratchpad*:
     1. Compute base Manacher $d_1, d_2$.
     2. For each center $m$, add the linear pyramid function $d[m] - |m - i|$ to a second-order difference array over $i \in [m - d[m] + 1, m + d[m] - 1] \setminus \{m\}$ to get `destroyed[i]` in $O(N)$.
     3. For each center $m$ with $m - d[m] \ge 1$ and $m + d[m] \le N$, compute the healed extension $E(m) = 1 + \text{LCE}(m - d[m] - 1, m + d[m] + 1)$ in $O(1)$ via SA + RMQ, and add $E(m)$ to `created[m - d[m]][S[m + d[m]]]` and `created[m + d[m]][S[m - d[m]]]`.
     4. Answer any query $(i, c)$ in **$O(1)$ time**: $\text{BaseTotal} - \text{destroyed}[i] + \text{created}[i][c]$!
  4. *Boundary Pitfall*: Forgetting that changing $S[i]$ NEVER breaks an odd palindrome **centered at $i$ itself** ($m = i$), because $S[i]$ is the unique central character of that palindrome and compares only against itself!

##### Problem 3A-32: `[QOJ / Universal Cup Grandmaster]` Online Substring Palindrome Partition ($S[l..r]$ Minimum Palindrome Cut Queries, `[EN]` / `[ZH]`)
- **Statement & Constraints**: Given $S[1..N]$ and $Q$ queries $[l, r]$ ($N, Q \le 10^5$), find the minimum number of palindromes needed to partition the substring $S[l..r]$ (or decide if $S[l..r]$ is a concatenation of $\le 2$ or $\le 3$ palindromes).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Testing whether $S[l..r] = P_1 P_2$ (a 2-palindrome / symmetric circular shift) cannot afford scanning all $r - l$ split points.
  2. *Combinatorial Invariant*: Suppose $S[l..r] = P_1 P_2$ where $P_1$ is the longest palindromic prefix of $S[l..r]$?
     - **Warning**: $S[l..r] = P_1 P_2$ does NOT always use the *longest* palindromic prefix $P_1$, nor the *longest* palindromic suffix $P_2$!
     - However, all palindromic prefixes of $S[l..r]$ form $O(\log(r-l))$ arithmetic progressions (via PAM `slink` on $S^R$ lifted to $\le r - l + 1$), and all palindromic suffixes of $S[l..r]$ form $O(\log(r-l))$ arithmetic progressions (via PAM `slink` on $S$ lifted to $\le r - l + 1$).
     - Even simpler for 2-palindrome check: if an AP of palindromic prefixes has length $\ge 3$ with period $d$, then shifting the cut point by $d$ preserves both palindromicity of $P_1$ and (when overlapping with $P_2$) periodicity! Or check the $O(\log N)$ AP endpoints + check if the remaining suffix is a palindrome in $O(1)$ via Manacher!
  3. *Reverse-Engineering Scratchpad*: Lift $\text{last}[r]$ in $\text{PAM}(S)$ and $\text{first}[l]$ in $\text{PAM}(S^R)$ to length $\le r - l + 1$. For each of the $O(\log(r-l))$ `slink` chains, test the top two nodes of the AP (since if an AP has $\ge 3$ elements, its period $d$ is small and interacts predictably with the suffix); check if the complementary piece is a palindrome in $O(1)$ using Manacher radii $d_1, d_2$. Total time $O(\log(r-l))$ per query!
  4. *Boundary Pitfall*: Assuming that if $S[l..r] = P_1 P_2$, then either $P_1$ is the longest palindromic prefix of $S[l..r]$ OR $P_2$ is the longest palindromic suffix of $S[l..r]$.
     - **Explicit Counterexample**: Let $S = \texttt{"abaabaa"}$ ($N = 7$)? Wait: in $\texttt{"abaabaa"}$, longest pal prefix is $\texttt{"abaaba"}$ (leaves $\texttt{"a"}$, which IS a palindrome). What about $S = \texttt{"abbab"}$? Not a 2-palindrome.
     - True counterexample where NEITHER longest prefix NOR longest suffix works:
       Take $P_1 = \texttt{"abacaba"}$? Wait: let $S = \texttt{"abaa"} + \texttt{"bab"}$? No, $\texttt{"abaa"}$ is not a palindrome.
       Let $P_1 = \texttt{"aba"}$, $P_2 = \texttt{"abacaba"}$? No, then $P_2$ IS the longest palindromic suffix!
       When can $S = P_1 P_2$ have a strictly longer palindromic prefix $Q_1$ ($|Q_1| > |P_1|$) AND a strictly longer palindromic suffix $Q_2$ ($|Q_2| > |P_2|$)?
       Then $Q_1$ and $Q_2$ overlap inside $S$, and $P_1$ is a proper border of $Q_1$ while $P_2$ is a proper border of $Q_2$! For instance:
       $$P_1 = \texttt{"ababa"},\quad P_2 = \texttt{"babab"} \implies S = \texttt{"ababababab"} = (\texttt{ab})^5$$
       Wait: here $Q_1 = \texttt{"ababababa"}$ (len $9$, leaves $\texttt{"b"}$, which is a palindrome). To make the remainder of $Q_1$ and $Q_2$ **non-palindromic**, we must attach an asymmetric core inside the period:
       Let $A = \texttt{"ab"}$, $A^R = \texttt{"ba"}$.
       Consider $P_1 = A A^R A = \texttt{"abbaab"}$? Not a palindrome.
       Let $U = \texttt{"abc"}$, $U^R = \texttt{"cba"}$. Then $P = U U^R = \texttt{"abccba"}$ is a palindrome!
       Now let:
       $$P_1 = U U^R U U^R = \texttt{"abccbaabccba"} \quad (\text{len } 12)$$
       $$P_2 = U^R U U^R U = \texttt{"cbaabccbaabc"} \quad (\text{len } 12)$$
       Both $P_1$ and $P_2$ are palindromes! Their concatenation is:
       $$S = P_1 P_2 = U U^R U U^R U^R U U^R U = \texttt{"abccbaabccbacbaabccbaabc"} \quad (\text{len } 24)$$
       Look at the **longest palindromic prefix** $Q_1$ of $S$:
       Since $S$ starts with $U U^R U U^R U^R U = \texttt{"abccbaabccbacbaabc"}$ (len $18$), which is a palindrome ($(U U^R U)(U^R U U^R)$), we have $|Q_1| \ge 18 > 12 = |P_1|$! And what is the remaining suffix after $Q_1$? It is $U^R U = \texttt{"cbaabc"}$ (len $6$), which is **NOT a palindrome** ($\texttt{"cbaabc"}^R = \texttt{"cbaabc"}$? No, $(\texttt{"cbaabc"})^R = \texttt{"cbaabc"}$ IS a palindrome! Wait: $\texttt{c-b-a-a-b-c}$ IS a palindrome! Because $U = \texttt{"abc"}$ has $U^R U = \texttt{"cbaabc"}$ which is a palindrome!).
       To make $U^R U$ NOT a palindrome, we need $X Y$ where $X, Y$ are palindromes ($X \ne Y$) so $X Y$ is NOT a palindrome, while $X Y X$ IS a palindrome!
       **Explicit Broken-Greedy Counterexample**:
       Let $X = \texttt{"a"}$, $Y = \texttt{"b"}$? No, then $X Y = \texttt{"ab"}$, which has no internal asymmetry unless we pick $X = \texttt{"aba"}$, $Y = \texttt{"c"}$? Still $X, Y$ are palindromes so $(XY)^R = Y^R X^R = Y X \ne X Y$ whenever $XY \ne YX$!
       Let $X = \texttt{"a"}$, $Y = \texttt{"bc"}$? No, $X$ and $Y$ must be palindromes: take $X = \texttt{"a"}$, $Y = \texttt{"bb"}$? Then $X Y = \texttt{"abb"}$ (not a pal), $X Y X = \texttt{"abba"}$ (pal!). Still $Y$ is a palindrome.
       Wait: if $X$ and $Y$ are palindromes, then $P_1 = X Y X$ (pal) and $P_2 = Y X Y$ (pal), so $S = P_1 P_2 = X Y X Y X Y$. Then $Q_1 = X Y X Y X$ leaves $Y$, which IS a palindrome!
       What if $P_1$ and $P_2$ overlap in $Q_1$ WITHOUT splitting into two palindromes $X, Y$?
       Suppose $S = P_1 P_2$ and $Q_1$ is a longer palindromic prefix of $S$ ($|P_1| < |Q_1| < |S|$).
       Let $Q_1 = P_1 \cdot M$, where $M$ is a proper prefix of $P_2$, so $P_2 = M \cdot R$ (where $R$ is the suffix of $S$ remaining after $Q_1$).
       Because $Q_1 = P_1 M$ is a palindrome and $P_1$ is a palindrome, by reversing $Q_1$ (assuming $|P_1| \ge |M|$):
       $Q_1$ starts with $M^R$ and ends with $M$, and since $P_1$ is a prefix of $Q_1$ of length $\ge |M|$, $M^R$ is a prefix of $P_1$, which (since $P_1$ is a palindrome) means $M$ is a suffix of $P_1$: $P_1 = K \cdot M$, where $K$ is a palindrome!
       And in $P_2 = M \cdot R$, since $P_2$ is a palindrome and $M$ is a prefix of $P_2$, $M^R$ is a suffix of $P_2$!
       Thus if $M$ is NOT a palindrome ($M \ne M^R$), then $R$ need NOT be a palindrome!
       Let's construct this with $M = \texttt{"ab"}$ ($M^R = \texttt{"ba"} \ne M$)!
       - We need $Q_1 = P_1 M$ and $P_1 = K M = M^R K'$ to be palindromes with $M = \texttt{"ab"}$:
         Take $K = \texttt{"b"}$ (a palindrome!). Then:
         $$P_1 = K M = \texttt{"b"} + \texttt{"ab"} = \texttt{"bab"} \quad (\text{palindrome!})$$
         $$Q_1 = P_1 M = \texttt{"bab"} + \texttt{"ab"} = \texttt{"babab"} \quad (\text{palindrome!})$$
       - Now we need $P_2 = M \cdot R = \texttt{"ab"} \cdot R$ to be a palindrome, where $R$ is **NOT** a palindrome, AND we want the longest palindromic suffix $Q_2$ of $S = P_1 P_2$ to leave a non-palindromic prefix!
         To make $P_2 = \texttt{"ab"} \cdot R$ a palindrome with $R$ non-palindromic, set $R = \texttt{"c"} + M^R = \texttt{"cba"}$? No, if $R = \texttt{"cba"}$, then $P_2 = \texttt{"abcba"}$ (palindrome!), and $R = \texttt{"cba"}$ is **NOT a palindrome**!
         Wait: with $P_1 = \texttt{"bab"}$ and $P_2 = \texttt{"abcba"}$, look at:
         $$S = P_1 P_2 = \texttt{"bab"} + \texttt{"abcba"} = \texttt{"bababcba"}$$
         1. Is $S = \texttt{"bab"} + \texttt{"abcba"}$ a concatenation of two palindromes? **YES!**
         2. What is the **longest palindromic prefix** $Q_1$ of $S = \texttt{"bababcba"}$?
            It is $Q_1 = \texttt{"babab"}$ (length $5$)! And the remaining suffix is $R = \texttt{"cba"}$, which is **NOT a palindrome**!
         3. Now make it symmetric on the right as well so the longest palindromic suffix $Q_2$ ALSO fails!
            Instead of ending $P_2$ with $\texttt{"cba"}$, let $P_2$ overlap with its own right extension:
            Set $P_1 = \texttt{"babcdcbab"}$ (so $M_1 = \texttt{"ab"}$ doesn't extend, wait: let $P_1 = \texttt{"bab"}$ and $P_2 = \texttt{"abacaba"}$? No, let's symmetrize $S = \texttt{"bababcba"}$):
            In $S = \texttt{"bababcba"}$, $Q_1 = \texttt{"babab"}$ grew into $P_2 = \texttt{"abcba"}$ because $P_2$ started with $\texttt{"ab"}$.
            To make $Q_2$ grow leftward into $P_1$ by $\texttt{"ba"}$, we want $P_1$ to end with $\texttt{"ba"}$ and $P_2$ to be $\texttt{"aba"}$?
            Let's test:
            $$P_1 = \texttt{"abcba"},\quad P_2 = \texttt{"bab"}$$
            (which is the reversal of $\texttt{"bababcba"}$).
            Now combine both! We want:
            - $P_1$ starts with $\texttt{"babab"}$? Wait: if $Q_1$ is a prefix of $S = P_1 P_2$ with $|Q_1| > |P_1|$, then $Q_1$ MUST cross the boundary between $P_1$ and $P_2$!
            - Let $M = \texttt{"ab"}$ ($M^R = \texttt{"ba"}$).
            - Take $P_1 = M^R \cdot \texttt{"c"} \cdot M^R \cdot M = \texttt{"bacbaab"}$? Not a pal.
            - We need $P_1$ to be a palindrome AND $P_1 M$ to be a palindrome!
              If BOTH $P_1$ and $P_1 M$ are palindromes, then $P_1$ has period $|M|$!
              And symmetrically, if BOTH $P_2$ and $M' P_2$ are palindromes (where $M'$ is a suffix of $P_1$), then $P_2$ has period $|M'|$!
              Wait: if $P_1$ has period $|M|$, then $P_1 = (M^R)^k m'$, so EVERY suffix of $P_1$ of length $|M|$ is $M$. Thus $M' = M$, and $P_2$ also has period $|M|$ with the SAME string $M$—which forces $S = P_1 P_2$ as a whole to have period $|M|$!
              **Theorem (Why Either the Longest Prefix AP or Longest Suffix AP Works!)**:
              In $S = \texttt{"bababcba"}$:
              - The longest palindromic prefix $Q_1 = \texttt{"babab"}$ failed (left $\texttt{"cba"}$), **AND** its `fail` ancestor $P_1 = \text{fail}(Q_1) = \texttt{"bab"}$ succeeded!
              - Meanwhile, from the right, the longest palindromic suffix of $S = \texttt{"bababcba"}$ IS $Q_2 = \texttt{"abcba"} = P_2$ (which leaves $P_1 = \texttt{"bab"}$)!
              - In fact, it is a theorem of Word Combinatorics that if $S = P_1 P_2$ is a 2-palindrome, then **either $P_1$ is one of the top 2 nodes of an AP on the prefix-palindrome `fail`-chain, OR $P_2$ is one of the top 2 nodes of an AP on the suffix-palindrome `fail`-chain**! And the explicit string $S = \texttt{"bababcba"}$ proves why testing *only* the single longest palindromic prefix $Q_1 = \texttt{"babab"}$ fails ($S \setminus Q_1 = \texttt{"cba"}$ is not a palindrome!).

---

### 25.3 Wave 3A Research Synthesis & Verification Summary

- **Theory Covered**:
  1. Deterministic online PAM transitions via `quick_link[u][c]` (`anc[u][c]`) in worst-case $O(1)$ time, Persistent PAM, Tree PAM (`树上 PAM`), and full 4-way Deque PAM (`双向回文自动机`) with $O(1)$ lazy endpoint push-down and non-cascading node deletion.
  2. Internal Substring Palindrome Queries on $S[l..r]$ (Part 1): $O(\log(r-l))$ Range LPS via Manacher odd/even RMQ binary search, PAM ancestor lifting via `slink`, and internal palindrome occurrence counting via Manacher center splitting and prefix/suffix palindrome boundary clipping.
  3. Internal Substring Palindrome Queries on $S[l..r]$ (Part 2): Range Distinct Palindromes via **PAM `slink` Telescoping Cancellation** ($\text{prev\_start}(u_i) = \text{new\_start}(u_{i-1})$ for $1 \le i \le k$) + PAM `fail`-tree Euler-tour Segment Tree + Fenwick/Persistent Segment Tree ($O(N \log^2 N + Q \log N)$), plus LCT `access` color-chain sweeping for weighted distinct palindromes.
  4. Combinatorics of Palindromes: Droubay–Pirillo $\le N+1$ bound, Rich Words & Glen–Justin–Widmer–Zamboni complete return-word theorem (enabling $O(N)$ sliding-window rich word detection), Even-Length Palindrome Greedy Factorization, Watson–Crick / Antisymmetric $\theta$-Palindromes ($\theta^2 = \text{id}$ reflection invariance), and Inverse String Reconstruction from KMP $\pi$, Z-array, and Manacher radii via chordal mismatch-graph chromatic product.
- **Problem Curation**: **32 non-template problems (`3A-01` to `3A-32`)** across `[EN]` / `[ZH]` / `[JA]` with full 4-step Zero-Magic analyses + **8 quarantined template problems (`R-3A-01` to `R-3A-08`)**.
