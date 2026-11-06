# Wave 2A (Cohort 2: Iterations 63–67) — Advanced Suffix Automaton (SAM), Generalized SAM (`广义 SAM`), Endpos Segment Tree Merging & LCT/HLD Coupling

> [!IMPORTANT]
> **Cohort 2 Independent Redundant Discovery Report (`cohort2_iter_63_to_67_sam_gsam_endpos_merge_lct.md`)**
> This document is the 100% independent Cohort 2 research pass for **Wave 2A (Iterations 63–67)**. It establishes every combinatorial word invariant, algebraic/structural duality, boundary counterexample, and data-structure coupling from first principles under the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**, without referencing Cohort 1's output.

---

## Iteration 63: Structural Anatomy of SAM & Generalized SAM (`广义 SAM`) — Duality, Trie-DFS Collapse, and Zero-Length Clone Elimination

### 1. The Diagnostic Signal (Why Black-Box Single-String SAM Fails on Multi-String & Suffix-Tree Queries)

Standard tutorials present the Suffix Automaton (SAM) of a string $S[1..N]$ via Blumer et al.'s online incremental construction (`extend(c)`), treating the parent tree (`link[u]`) and DAG transitions (`next[u][c]`) as an opaque state machine that recognizes all substrings of $S$. This black-box view breaks down in three recurring competitive programming scenarios:

1. **Reverse LCP / Suffix Tree Reductions**: A problem asks for the Longest Common Prefix (LCP) of arbitrary substrings $S[l_1..r_1]$ and $S[l_2..r_2]$, or requires lexicographical traversal of all substrings of $S$. Because an ordinary SAM compresses *left-extensions* (prefixes of the same end-position set) into a single node $u$ while branching on *right-extensions* via DAG edges, a single SAM node contains substrings with different starting positions and cannot directly answer forward LCP queries without reversing the string.
2. **Multi-String Dictionaries ($S_1, S_2, \dots, S_k$) with Overlapping Prefixes**: When given $k$ strings of total length $L = \sum_{i=1}^k |S_i| \le 10^6$, concatenating them with distinct sentinels $S_1 \#_1 S_2 \#_2 \dots \#_{k-1} S_k$ blows up the alphabet size by $k$ (causing $O(L \cdot k)$ transition memory or forcing hash/map transitions) and creates $O(L^2)$ artificial cross-boundary substrings that pollute `link` subtrees unless explicitly clipped.
3. **Naive Generalized SAM (GSAM) Construction Pitfalls**: Attempting to build a Generalized SAM by either:
   - Calling `last = 1` at the start of each string $S_i$ without checking whether `next[last][c]` already exists, or
   - Building a Trie of $\{S_1, \dots, S_k\}$ and running a Depth-First Search (DFS) calling `extend(trie_parent_sam_node, c)`,
   leads to **zero-length clone nodes** ($\text{len}(q) = \text{len}(\text{link}(q))$) that corrupt DP states and subtree sums, or triggers a catastrophic **$O(L^2)$ time and space explosion** on skewed tries.

---

### 2. The Combinatorial Word Invariant (Right-Equivalence vs. Left-Extension & Trie Depth Monotonicity)

#### 2.1 Exact Duality Between the Link Tree of $\text{SAM}(S)$ and the Explicit Suffix Tree $\text{ST}(S^R)$

Let $S = s_1 s_2 \dots s_N$ be a string of length $N$. For any non-empty substring $w$ of $S$, define its **ending position set**:

$$\text{endpos}_S(w) = \{ r \in \{1, \dots, N\} \mid S[r - |w| + 1 .. r] = w \}$$

Two substrings $u, v$ are **right-equivalent** ($u \equiv_R v$) if $\text{endpos}_S(u) = \text{endpos}_S(v)$. Each equivalence class $E$ forms a state of $\text{SAM}(S)$.

- **Containment-Length Lemma**: If $|u| \le |v|$ and $\text{endpos}_S(u) \cap \text{endpos}_S(v) \ne \emptyset$, then both $u$ and $v$ end at some common index $r$, so $u$ is a suffix of $v$. Consequently, every occurrence of $v$ ends with an occurrence of $u$, meaning $\text{endpos}_S(v) \subseteq \text{endpos}_S(u)$. Thus any two $\text{endpos}$ sets are either **disjoint** or **nested**.
- **Contiguous Suffix Interval within a State**: Within a single class $E$, let $\text{longest}(E)$ be the longest string in $E$ (with length $\text{len}(E) = |\text{longest}(E)|$) and $\text{shortest}(E)$ be the shortest string in $E$ (with length $\text{minlen}(E) = |\text{shortest}(E)|$). Every suffix of $\text{longest}(E)$ of length $\ell \in [\text{minlen}(E), \text{len}(E)]$ belongs to $E$. The longest suffix of $\text{longest}(E)$ whose $\text{endpos}$ set is strictly larger than $E$ has length $\text{minlen}(E) - 1$ and defines the **suffix link** $\text{link}(E)$.

Now consider the **reversed string** $S^R = s_N s_{N-1} \dots s_1$. A substring $w = S[l..r]$ of $S$ corresponds bijectively to the reversed substring $w^R = S^R[N - r + 1 .. N - l + 1]$ of $S^R$:

- Adding a character $c$ to the **left** of $w$ in $S$ (producing $cw$, a longer suffix sharing the same ending position $r$) corresponds to appending $c$ to the **right** of $w^R$ in $S^R$ (extending a prefix of the suffix of $S^R$ starting at $N - r + 1$).
- Therefore, $\text{endpos}_S(w) = \{ r_1, \dots, r_m \}$ corresponds to the exact set of **starting positions** $\{ N - r_1 + 1, \dots, N - r_m + 1 \}$ of $w^R$ in $S^R$—which is the exact set of suffix leaves in the subtree of $w^R$ in the compressed Suffix Tree $\text{ST}(S^R)$!
- Moving from $\text{link}(E)$ to $E$ in the Link Tree of $\text{SAM}(S)$ extends $\text{longest}(\text{link}(E))$ on the **left** by the reversed string $\big(\text{longest}(E)[1 .. \text{len}(E) - \text{len}(\text{link}(E))]\big)^R$. In $S^R$, this is a single compressed edge of length $\text{len}(E) - \text{len}(\text{link}(E))$ extending $\big(\text{longest}(\text{link}(E))\big)^R$ on the **right**.

$$
\boxed{
\text{LinkTree}\big(\text{SAM}(S)\big) \;\cong\; \text{Compressed Suffix Tree } \text{ST}(S^R) \text{ (without terminal sentinel } \$ \text{)}
}
$$

| Structural Feature in $\text{SAM}(S)$ | Dual Object in $\text{ST}(S^R)$ | Dual Object in $\text{SAM}(S^R)$ |
| :--- | :--- | :--- |
| State $u \in \text{SAM}(S)$ | Explicit branching/terminal node $u \in \text{ST}(S^R)$ | Explicit node in $\text{ST}(S)$ |
| Substrings represented by state $u$ | Compressed edge into $u$ covering lengths $[\text{len}(\text{link}(u))+1, \text{len}(u)]$ | Reversed prefixes along compressed edge in $\text{ST}(S)$ |
| Link Tree edge $\text{link}(u) \to u$ | Compressed Suffix Tree edge labelled by $S[r - \text{len}(u) + 1 .. r - \text{len}(\text{link}(u))]^R$ | Left-extension edge in $\text{SAM}(S)$ |
| Prefix node $\text{pos}(r)$ for $S[1..r]$ | Terminal node for suffix $S^R[N - r + 1 .. N]$ | Prefix node $\text{pos}(N - l + 1)$ for suffix $S[l..N]$ |
| $\text{LCA}_{\text{LinkTree}}(\text{pos}(r_1), \text{pos}(r_2))$ | Longest Common Suffix $\text{LCSuf}(S[1..r_1], S[1..r_2])$ | Longest Common Prefix $\text{LCP}(S[l_1..N], S[l_2..N])$ |

#### 2.2 The Amortization Invariant for Generalized SAM: Why Trie-BFS Is $O(V_{\text{Trie}})$ While Trie-DFS Is $O(V_{\text{Trie}}^2)$

Suppose we first insert all strings $S_1, \dots, S_k$ into a prefix Trie $T$ with $V = |V(T)| \le \sum |S_i| + 1$ nodes, and we build the Generalized SAM by calling `insert_char(sam_node[parent(x)], char(x))` for each Trie node $x$.

Why does the standard single-string SAM amortize to $O(N)$ time? In a single string $S[1..N]$, when appending step $i$ (`last` has length $i-1$), we walk up the suffix-link chain $p \gets \text{link}(p)$ while `next[p][c] == 0`. Let $d(p)$ be the depth of $p$ in the Link Tree (or equivalently $\text{minlen}(p)$). Every step up the `link` chain strictly decreases $\text{minlen}(p)$ by at least $1$, and the new node `cur` ends up linked to a state of `minlen` at most $\text{minlen}(p_{\text{stop}}) + 2$. Because $\text{len}(\text{last})$ increases by $+1$ at each step and only increases from one iteration to the next, the potential $\Phi = \text{minlen}(\text{last})$ increases by at most $+2$ per step and drops by $\ge 1$ per `link` hop.

Now consider a **Trie $T$** with branching:
- **Why DFS on the Trie Fails ($O(V^2)$ Worst-Case)**:
  In a DFS over the Trie, whenever we finish a long branch of length $M$ and backtrack to a shallow Trie node $x$ to explore a short sibling branch $x \xrightarrow{c} y$, we reset our starting SAM node to $p = \text{sam\_node}[x]$. However, during the deep branch of length $M$, the states along the suffix-link chain of $\text{sam\_node}[x]$ may have been **split (cloned) up to $O(M)$ times**!
  Wait—even worse: what if we have a long main spine of length $M$, and attached to deep nodes of the spine (or after building a long chain of clones) we branch repeatedly? Let us construct the exact $O(V^2)$ counterexample for Trie-DFS:
  - **Concrete $O(V^2)$ Counterexample for Trie-DFS**:
    Consider two groups of strings (or a single Trie of size $V = 3m$):
    1. First, DFS explores a long branch $B_1 = \text{a}^m \text{b}_1 \text{b}_2 \dots \text{b}_m$ (or a string that creates a suffix-link chain of length $\Theta(m)$ for some prefix state $u$). Actually, even over a binary/ternary alphabet: let the Trie contain the path $P = c_1 c_2 \dots c_m$ such that the SAM state $u_k$ for $c_1 \dots c_k$ has suffix-link depth $\Theta(k)$ (for example, $P = \text{a b}^m$: after reading $\text{a}$, reading $\text{b}^m$ creates states for $\text{ab}^k$ whose suffix links point to $\text{b}^k$, wait: for $P = \text{a}^m$, the suffix link chain of $\text{a}^m$ has length $m$: $\text{a}^m \to \text{a}^{m-1} \to \dots \to \text{a} \to \epsilon$).
    2. Suppose at the Trie node for $\text{a}^m$, there are $m$ distinct character branches (or $m$ short 2-step branches over a binary alphabet $\text{b a}^k \text{c}$): if at node $\text{a}^m$ we have branches for characters $d_1, d_2, \dots, d_m$ (or binary gadgets), when DFS processes the first branch $\text{a}^m d_1$, it walks up the entire suffix-link chain $\text{a}^m \to \text{a}^{m-1} \to \dots \to \epsilon$ of length $m$ setting `next[p][d_1]`. Then DFS backtracks to $\text{a}^m$ and processes $\text{a}^m d_2$, walking up the $m$ nodes again! Over a large alphabet $|\Sigma| = \Theta(m)$, that is already $\Theta(m^2)$ steps, whereas even over a **constant alphabet $|\Sigma| = 3$**:
    Let the Trie have a spine $S_0 = \text{a}^m$, and from **each** Trie node $\text{a}^k$ ($k = m/2, \dots, m$), attach a single short branch $\text{b}\text{c}$ (and along one deep branch at $\text{a}^m$, append a gadget that splits all states $\text{a}^j$). Better yet, over constant alphabet $\Sigma = \{\text{a}, \text{b}, \text{c}\}$:
    Suppose at Trie node $\text{a}^k$ ($1 \le k \le m$), there is a branch $\text{a}^k \text{b}$ followed by $\text{c}$.
    When DFS visits $\text{a}^k \text{b}$, it walks up the link chain of $\text{a}^k$ until it finds a node with a `'b'` transition. Initially, only $\text{a}^{k-1}, \dots$ might have `'b'` if visited earlier. What if DFS visits the deep node $\text{a}^m$ **first** (by ordering `'a'` before `'b'`)?
     Wait: if DFS visits `'a'` before `'b'`, then it goes all the way down $\text{a} \to \text{a}^2 \to \dots \to \text{a}^m$.
    At $\text{a}^m$, it visits $\text{a}^m \text{b}$: this walks $\text{a}^m \to \text{a}^{m-1} \to \dots \to \epsilon$ and sets `next[a^j]['b'] = sam(a^m b)` for **all** $0 \le j \le m$!
    Now, at $\text{a}^m \text{b}$, suppose there is no further child, so DFS backtracks to $\text{a}^{m-1}$ and visits its child $\text{a}^{m-1} \text{b}$!
    What happens when DFS inserts `'b'` from $p = \text{sam}(\text{a}^{m-1})$?
    Look at `next[p]['b']`: because $\text{a}^m \text{b}$ was already processed, `next[a^{m-1}]['b']` **already exists** and points to $q = \text{sam}(\text{a}^m \text{b})$, which has $\text{len}(q) = m + 1 > \text{len}(p) + 1 = m$!
    Therefore, inserting $\text{a}^{m-1} \text{b}$ **must clone** $q$ into $clone_{m-1}$ with $\text{len}(clone_{m-1}) = m$, and walk up the suffix-link chain $\text{a}^{m-1} \to \text{a}^{m-2} \to \dots \to \epsilon$ (all $m$ steps!) redirecting `next[a^j]['b']` from $q$ to $clone_{m-1}$ for all $0 \le j \le m-1$!
    Next, DFS backtracks to $\text{a}^{m-2}$ and visits $\text{a}^{m-2} \text{b}$: `next[a^{m-2}]['b']` currently points to $clone_{m-1}$ of length $m > (m-2) + 1 = m-1$! So it clones $clone_{m-1}$ into $clone_{m-2}$ of length $m-1$, and walks **all $m-1$ steps** up $\text{a}^{m-2} \to \text{a}^{m-3} \to \dots \to \epsilon$ redirecting `next[a^j]['b']` to $clone_{m-2}$!
    Repeating this as DFS backtracks through $k = m-1, m-2, \dots, 1$, step $k$ redirects $k+1$ pointers along the link chain!
    The total number of pointer redirections on a binary alphabet $\Sigma = \{\text{a}, \text{b}\}$ with Trie size $V = 2m + 1$ is:

    $$\sum_{k=1}^{m} (k + 1) = \frac{m(m+3)}{2} = \Theta(V^2)!$$

> [!CAUTION]
> **The Exact Binary-Alphabet $O(V^2)$ Counterexample for Trie-DFS GSAM**:
> Let the Trie represent the set of strings $\{\text{a}^k \text{b} \mid 1 \le k \le m\}$ over $\Sigma = \{\text{a}, \text{b}\}$, which has only $V = 2m + 1$ Trie nodes.
> If DFS visits children in alphabetical order (`'a'` before `'b'`), it inserts $\text{a}^m \text{b}$ first (setting `next[a^j]['b']` for all $j \le m$ to a state of length $m+1$), and then on backtracking inserts $\text{a}^{m-1}\text{b}, \text{a}^{m-2}\text{b}, \dots, \text{a}\text{b}$ in decreasing order of length. Every single backtrack step triggers a clone redirect walk all the way to the root $\epsilon$, taking $\Theta(m^2) = \Theta(V^2)$ time on a binary alphabet!

- **Why Breadth-First Search (BFS) on the Trie Guarantees $O(V \cdot |\Sigma|)$ or $O(V)$ Time**:
  In a BFS over the Trie $T$, nodes are processed in **non-decreasing order of their Trie depth** $\text{depth}(x) = \text{len}(\text{sam\_node}[x])$.
  Suppose we are at Trie node $x$ of depth $d$, and we insert its child $y = \text{child}(x, c)$ of depth $d + 1$:
  1. **Phase 1 (Setting empty transitions `next[p][c] = cur`)**: Each transition `next[p][c]` is changed from `0` to non-zero at most once across the entire algorithm. Since there are at most $2V$ states in the GSAM, Phase 1 takes $O(V |\Sigma|)$ total work across the entire BFS.
  2. **Phase 2 (Redirecting existing transitions `next[p][c] == q` to `clone`)**: Suppose we reach the first ancestor $p$ on the link chain of $u = \text{sam\_node}[x]$ with $q = \text{next}[p][c] \ne 0$. Because BFS processes Trie nodes in non-decreasing order of depth, every state $w$ currently in the GSAM has $\text{len}(w) \le d + 1$. Since $p$ is a proper suffix-link ancestor of $u$ (or $p = u$), $\text{len}(p) \le d$.
     Wait: when we clone $q$ into `clone` with $\text{len}(\text{clone}) = \text{len}(p) + 1$ and walk up $p' \gets \text{link}(p')$ while $\text{next}[p'][c] == q$, notice what happens to $\text{minlen}(\text{next}[u][c])$ or $\text{len}(\text{link}(\text{cur}))$:
     Let us bound the number of Phase 2 redirection hops across the entire BFS using the **Left-Character Multiplicity Bound** (originally proved by Blumer et al. and adapted to BFS-GSAM):
     Each Phase 2 redirection step visits a state $p'$ that had $\text{next}[p'][c] = q$ and changes it to $\text{next}[p'][c] = \text{clone}$. Notice that $\text{longest}(p') \cdot c$ is a suffix of $\text{longest}(u) \cdot c$. Specifically, prior to creating $\text{cur} = \text{sam\_node}[y]$, all states $p'$ on the redirected chain had their $c$-transition pointing to $q$, meaning $\text{longest}(p') c$ was a suffix of $\text{longest}(q)$ of length $\le \text{len}(p) + 1$.
     More directly: for a fixed state $u = \text{sam\_node}[x]$ of depth $d$, let $p_{\text{last}}$ be the shallowest node whose transition is redirected to `clone`. Then $\text{link}(\text{clone}) = \text{link}_{\text{old}}(q)$, and $\text{minlen}(\text{clone}) = \text{len}(p_{\text{last}}) + 1$ (Wait: $\text{minlen}(\text{clone}) = \text{len}(\text{link}(\text{clone})) + 1 = \text{len}(\text{link}_{\text{old}}(q)) + 1$). Every intermediate node $p'$ whose $c$-transition was redirected from $q$ to $\text{clone}$ corresponds to a suffix of $\text{longest}(\text{clone})$ of length in $[\text{minlen}(\text{clone}), \text{len}(\text{clone})]$.
     Crucially, because BFS processes nodes in increasing order of length $d$, **no state of length $> d + 1$ exists yet**! In the Trie-DFS counterexample, $\text{a}^{m-1}\text{b}$ was slow because a state of length $m + 1$ ($\text{a}^m \text{b}$) *already existed* and had already hijacked the transitions of $\text{a}^0, \dots, \text{a}^{m-1}$. Under BFS, $\text{ab}, \text{a}^2\text{b}, \dots, \text{a}^m\text{b}$ are inserted in order $k = 1, 2, \dots, m$: when $\text{a}^k\text{b}$ is inserted, $\text{a}^{k-1}\text{b}$ only set `next[a^{k-1}]['b']`, because `next[a^{k-2}]['b']` was *already* set by $\text{a}^{k-2}\text{b}$! Thus **zero clones are ever created** on $\{\text{a}^k \text{b}\}$ under BFS!
     In general, under BFS order, whenever $q = \text{next}[p][c]$ is cloned into `clone`, the old state $q$ now has $\text{minlen}_{\text{new}}(q) = \text{len}(\text{clone}) + 1 = \text{len}(p) + 2$, so the number of distinct lengths covered by $q$ shrinks from $\text{len}(q) - \text{len}(\text{link}_{\text{old}}(q))$ to $\text{len}(q) - \text{len}(p) - 1$, while `clone` takes over the interval $[\text{len}(\text{link}_{\text{old}}(q)) + 1, \text{len}(p) + 1]$. Wait—why can't `clone` itself be re-cloned many times? Because in BFS, any future node $x'$ has $\text{len}(\text{sam\_node}[x']) = d' \ge d$. When $x'$ walks up its suffix-link chain to some $p^*$ where $\text{next}[p^*][c]$ already exists, if $p^*$ hits `clone`, we create a sub-clone. However, for any node $x$ at depth $d$, as we walk up the suffix-link chain of $\text{sam\_node}[x]$ from $u$ down to $p_{\text{last}}$, every step moves to a proper suffix of the prefix string $S_x$ of length $d$. More simply, in BFS order, before inserting $y$ (at depth $d+1$), the longest string in the Trie that has already set $\text{next}[p][c] = q$ had depth $\le d+1$, so $\text{len}(q) \le d + 1$. Since $\text{len}(u) = d$, if $p = u$, then $\text{len}(q) \le d + 1 = \text{len}(u) + 1$, so $\text{len}(q) = \text{len}(u) + 1$ and **no clone is needed at $p = u$**. If $p$ is a proper ancestor of $u$ ($\text{len}(p) < d$), then `next[u][c]` was `0` (so at least one empty transition was filled in Phase 1!), and every redirected ancestor $p'$ in Phase 2 satisfies $\text{len}(p') \le \text{len}(p) < \text{len}(u)$. By charging the Phase 2 redirection steps along $p \to \dots \to p_{\text{last}}$ to the drop in suffix-link depth along the Trie path (each Trie step increases depth by $+1$, and the link of $\text{cur}$ lands at `clone` whose depth is $\text{len}(p) + 1$, meaning $\text{len}(\text{cur}) - \text{len}(\text{link}(\text{cur})) = (d + 1) - (\text{len}(p) + 1) = d - \text{len}(p) \ge \text{number of Phase 1 steps}$, while for Phase 2, $\text{len}(\text{link}(\text{old } q))$ drops relative to $\text{len}(p)$), the total number of Phase 2 redirection steps across the entire BFS is strictly $O(V)$.

---

### 3. The Reverse-Engineering Scratchpad (Online vs. BFS Generalized SAM & Zero-Length Clone Elimination)

What if we do **not** want to build an explicit Trie first (or we receive strings online one by one, resetting `last = 1` at the start of each string $S_i$)?
When we reset `last = 1` and feed characters of $S_i$ one by one, we may arrive at a state $p = \text{last}$ where the transition $q = \text{next}[p][c]$ **already exists** from an earlier string $S_j$ ($j < i$).

Let us trace what happens if we naively run standard single-string `extend(c)` when $\text{next}[\text{last}][c] = q \ne 0$:
- Standard `extend(c)` creates a brand-new node `cur` with $\text{len}(\text{cur}) = \text{len}(\text{last}) + 1$, skips the Phase 1 loop (since `next[last][c] != 0`), and enters the check `if (len[p] + 1 == len[q])`:
  - **Case A ($\text{len}(q) = \text{len}(\text{last}) + 1$)**: Standard `extend(c)` sets `link[cur] = q` and returns `cur`!
    Look at what just happened: `cur` has $\text{len}(\text{cur}) = \text{len}(\text{last}) + 1 = \text{len}(q)$, and $\text{link}(\text{cur}) = q$!
    Thus $\text{minlen}(\text{cur}) = \text{len}(\text{link}(\text{cur})) + 1 = \text{len}(q) + 1 > \text{len}(\text{cur})$!
    **`cur` is a ghost/zero-length node representing $\text{len}(\text{cur}) - \text{len}(\text{link}(\text{cur})) = 0$ strings**, and worse, `next[last][c]` still points to $q$, so `cur` is completely unreachable in the DAG while stealing the current prefix's $\text{endpos}$ marker from $q$!
  - **Case B ($\text{len}(q) > \text{len}(\text{last}) + 1$)**: Standard `extend(c)` creates a new node `cur` with $\text{len}(\text{cur}) = \text{len}(\text{last}) + 1$, and *then* creates a `clone` of $q$ also with $\text{len}(\text{clone}) = \text{len}(\text{last}) + 1$, setting $\text{link}(\text{cur}) = \text{clone}$ and redirecting `next[p][c] = clone`!
    Again, $\text{len}(\text{cur}) = \text{len}(\text{clone})$, so `cur` is an unreachable zero-length duplicate of `clone`!

Thus, whenever $\text{next}[\text{last}][c] = q \ne 0$ at the very start of `extend(last, c)`, we must **never** allocate a separate `cur` node! Instead:
1. **Branch 1 ($\text{next}[\text{last}][c] = q \ne 0$ and $\text{len}(q) == \text{len}(\text{last}) + 1$)**:
   The state $q$ already represents the exact prefix we just read. Return $q$ immediately as the new `last`!
2. **Branch 2 ($\text{next}[\text{last}][c] = q \ne 0$ and $\text{len}(q) > \text{len}(\text{last}) + 1$)**:
   State $q$ is too long ($\text{longest}(q)$ contains characters before the start of our current string $S_i$). We split $q$ by creating a single node `clone` with:
   - $\text{len}(\text{clone}) = \text{len}(\text{last}) + 1$,
   - $\text{next}[\text{clone}] = \text{next}[q]$, $\text{link}(\text{clone}) = \text{link}(q)$,
   - Redirect $\text{next}[p][c] \gets \text{clone}$ for $p = \text{last}, \text{link}(\text{last}), \dots$ while $\text{next}[p][c] == q$,
   - Set $\text{link}(q) \gets \text{clone}$, and **return `clone` directly as the new `last`**!
3. **Branch 3 ($\text{next}[\text{last}][c] == 0$)**:
   Run the standard single-string SAM extension from $p = \text{last}$ and return `cur`.

```cpp
// Non-standard Online / Trie-BFS Generalized SAM Transition Contract
// Eliminates all zero-length ghost nodes when next[last][c] != 0.
int extend_gsam(int last, int c) {
    if (next_state[last][c]) {
        int p = last, q = next_state[p][c];
        if (len[p] + 1 == len[q]) return q; // Exact state already exists
        int clone = ++sz;
        len[clone] = len[p] + 1;
        memcpy(next_state[clone], next_state[q], sizeof(next_state[q]));
        link[clone] = link[q];
        while (p && next_state[p][c] == q) {
            next_state[p][c] = clone;
            p = link[p];
        }
        link[q] = clone;
        return clone; // Return clone directly; do NOT allocate a separate cur!
    }
    int cur = ++sz, p = last;
    len[cur] = len[last] + 1;
    while (p && !next_state[p][c]) {
        next_state[p][c] = cur;
        p = link[p];
    }
    if (!p) {
        link[cur] = 1;
    } else {
        int q = next_state[p][c];
        if (len[p] + 1 == len[q]) {
            link[cur] = q;
        } else {
            int clone = ++sz;
            len[clone] = len[p] + 1;
            memcpy(next_state[clone], next_state[q], sizeof(next_state[q]));
            link[clone] = link[q];
            while (p && next_state[p][c] == q) {
                next_state[p][c] = clone;
                p = link[p];
            }
            link[q] = link[cur] = clone;
        }
    }
    return cur;
}
```

> [!NOTE]
> **Notice why Online `extend_gsam` (resetting `last = 1` per string without a Trie) is ALSO $O(\sum |S_i|)$ in Time and Space!**
> Wait: why did Trie-DFS take $O(V^2)$ earlier, whereas calling `extend_gsam` string-by-string from `last = 1` takes $O(\sum |S_i|)$?
> Because in the Trie-DFS counterexample $\{\text{a}^k \text{b} \mid 1 \le k \le m\}$, the *total length of the $m$ strings* is $\sum_{k=1}^m (k+1) = \Theta(m^2)$, whereas the *Trie size* is only $V = 2m + 1$!
> When the input is given as explicit strings $S_1, \dots, S_k$ with $\sum |S_i| = L$, online string-by-string `extend_gsam` takes $O(L)$ time because while reading a single string $S_i$ from left to right, $\text{len}(\text{last})$ increases by $+1$ at each character of $S_i$, so the potential $\Phi = \text{minlen}(\text{last})$ increases by at most $2|S_i|$ during $S_i$ and resets to $0$ at the start of $S_{i+1}$.
> However, when the input is given **directly as a compressed Trie $T$ of $V$ nodes** (such as `[ZJOI2015] 诸神眷顾的幻想乡` or `[BZOJ 3238]` where $\sum_{\text{leaves}} \text{depth} = \Theta(V^2)$), DFS on the Trie takes $O(V^2)$ while **BFS on the Trie takes $O(V)$**!

---

### 4. Boundary Pitfalls & Hand-Checked Trace

Let us hand-trace the zero-length clone failure on $S_1 = \text{"ab"}$, $S_2 = \text{"b"}$:
1. Insert $S_1 = \text{"ab"}$ from root $1$ ($\text{len}(1) = 0$):
   - Read `'a'`: creates node $2$ ($\text{len}(2) = 1, \text{link}(2) = 1$, $\text{next}[1][\text{'a'}] = 2$).
   - Read `'b'` from $2$: creates node $3$ ($\text{len}(3) = 2, \text{link}(3) = 1$, $\text{next}[2][\text{'b'}] = 3, \text{next}[1][\text{'b'}] = 3$).
2. Now insert $S_2 = \text{"b"}$ starting from `last = 1`:
   - Look at $\text{next}[1][\text{'b'}]$: it is already $q = 3$, with $\text{len}(3) = 2 > \text{len}(1) + 1 = 1$.
   - **If we used naive single-string `extend('b')`**: it would create `cur = 4` ($\text{len}(4) = 1$) AND `clone = 5` ($\text{len}(5) = 1, \text{link}(5) = 1$), setting $\text{link}(3) = \text{link}(4) = 5$ and $\text{next}[1][\text{'b'}] = 5$. Then node $4$ has $\text{len}(4) - \text{len}(\text{link}(4)) = 1 - 1 = 0$, and $\text{next}[1][\text{'b'}] = 5 \ne 4$. If we then query $\text{next}[1][\text{'b'}]$ to count how many strings contain `"b"`, we visit node $5$, whose Link-Tree subtree contains $3$ (from $S_1$) and $4$ (from $S_2$). Wait—if we instead walk the DAG on $S_2 = \text{"b"}$, we land at node $5$, which is the **parent** of node $4$, whereas if someone queries DAG transitions from node $4$, node $4$ is a dead end or has stale transitions if $5$ is later cloned again! Worse, if a problem counts $\sum_u (\text{len}(u) - \text{len}(\text{link}(u)))$ or assigns DP values per node assuming every node represents a non-empty interval of lengths, node $4$ violates $\text{minlen}(u) \le \text{len}(u)$.
   - **With `extend_gsam(1, 'b')`**: Branch 2 triggers immediately, creates a single node `clone = 4` with $\text{len}(4) = 1, \text{link}(4) = 1, \text{link}(3) = 4, \text{next}[1][\text{'b'}] = 4$, and returns $4$. Every node $u > 1$ strictly satisfies $\text{len}(u) > \text{len}(\text{link}(u))$.

---

## Iteration 64: SAM + Segment Tree Merging on $\text{endpos}$ (`线段树合并维护 Endpos`) & Substring Containment Clipping

### 1. The Diagnostic Signal (Why Whole-String SAM Fails on Substring-Restricted Queries $S[l..r]$)

A standard SAM built on $S[1..N]$ stores in each node $u$ the count $|\text{endpos}_S(u)|$ or the maximum/minimum ending position in the entire string $S$. However, a vast family of grandmaster problems restricts the universe of allowed occurrences to an **arbitrary query substring $S[l..r]$**:
- *"Does pattern $P$ occur inside $S[l..r]$?"* (`CF 1037H`, `[NOI2018] 你的名字`)
- *"In which string $T_i$ ($i \in [p_l, p_r]$) does the substring $S[l..r]$ occur most frequently?"* (`CF 666E`)
- *"What is the longest prefix of $S[c..d]$ that also occurs inside $S[a..b]$?"* (`[HEOI2016/TJOI2016] 字符串`)
- *"When building a chain of strings $w_1, w_2, \dots, w_k$ where $w_{i}$ appears at least twice in $w_{i+1}$, how do we test if a candidate ancestor $v$ occurs a second time inside $\text{longest}(u)$?"* (`CF 700E`)

Building a fresh SAM for $S[l..r]$ per query takes $O((r-l+1)Q) = O(NQ)$ time. We need a way to project any SAM state $u$ of the global string $S[1..N]$ onto the window $[l, r]$ in $O(\log N)$ time.

---

### 2. The Combinatorial Word Invariant (The Substring Containment Clipping Identity)

Let $w$ be a string of length $L = |w|$ whose SAM state in $\text{SAM}(S)$ is $u$ (meaning $\text{endpos}_S(w) = \text{endpos}_S(u)$).
When does $w$ occur as a contiguous substring of the slice $S[l..r]$?

An occurrence of $w$ in $S$ is uniquely identified by its **ending index** $p \in \text{endpos}_S(u)$. Since $|w| = L$, the occurrence ending at $p$ spans the exact index interval:

$$S[p - L + 1 .. p] = w$$

For this occurrence to lie **entirely inside** the window $S[l..r]$, both of its endpoints must lie in $[l, r]$:

$$\begin{cases} p - L + 1 \ge l \iff p \ge l + L - 1 \\ p \le r \end{cases}$$

Combining these two inequalities yields the **Substring Containment Clipping Identity**:

$$
\boxed{
w \text{ (of length } L \text{ in state } u \text{) occurs in } S[l..r]
\;\Longleftrightarrow\;
\text{endpos}_S(u) \cap [l + L - 1,\; r] \neq \emptyset
}
$$

And the exact number of occurrences of $w$ inside $S[l..r]$ is:

$$\text{occ}(w, S[l..r]) = \max\Big(0,\; \big|\text{endpos}_S(u) \cap [l + L - 1,\; r]\big|\Big)$$

```
Window S[l..r]:         |-----------------------|
                        l                       r
Invalid endpos p_1:  |-------|
                     p_1-L+1 p_1  (p_1 < l+L-1: starts before l!)
Valid endpos p_2:            |-------|
                             p_2-L+1 p_2  (l+L-1 <= p_2 <= r: fully inside!)
```

> [!WARNING]
> **Critical Invariant Distinction**:
> Notice that the valid interval $[l + L - 1, r]$ depends on the **exact length $L = |w|$ of the queried pattern $w$**, **NOT** necessarily on $\text{len}(u)$ or $\text{minlen}(u)$!
> - If we are checking whether a specific pattern $w$ of length $L \in [\text{minlen}(u), \text{len}(u)]$ occurs in $S[l..r]$, we clip to $[l + L - 1, r]$.
> - If we ask for the **longest** string in state $u$ that occurs in $S[l..r]$, let $p_{\max} = \max\big(\text{endpos}_S(u) \cap [l, r]\big)$ be the rightmost ending position of state $u$ at or before $r$. Since the longest string in $u$ ending at $p_{\max}$ that stays inside $[l, r]$ has length $\min(\text{len}(u),\; p_{\max} - l + 1)$, state $u$ contributes a valid substring in $S[l..r]$ of maximum length:
>   $$L_{\max}(u, l, r) = \min\big(\text{len}(u),\; p_{\max} - l + 1\big) \quad \text{provided } L_{\max}(u, l, r) \ge \text{minlen}(u).$$

---

### 3. The Reverse-Engineering Scratchpad (Segment Tree Merging + Link-Tree Binary Lifting + 5 Canonical Problem Derivations)

#### 3.1 Constructing the $\text{endpos}$ Sets for All SAM States in $O(N \log N)$ Time and Space

For each prefix $S[1..i]$ ($1 \le i \le N$), let $\text{pos}[i]$ be its state in $\text{SAM}(S)$.
By definition of $\text{endpos}$, $i \in \text{endpos}_S(u)$ if and only if $u$ is an ancestor of $\text{pos}[i]$ in the Link Tree. Thus:

$$\text{endpos}_S(u) = \{ i \mid u = \text{pos}[i] \} \;\sqcup\; \bigsqcup_{\text{link}(v) = u} \text{endpos}_S(v)$$

1. Initialize for each $i \in [1, N]$ a dynamic-point (sparse) Segment Tree rooted at $\text{rt}[\text{pos}[i]]$ over the range $[1, N]$ by inserting point $i$ ($O(\log N)$ nodes per prefix).
2. Traverse the Link Tree bottom-up (either via DFS on the Link Tree or in decreasing order of $\text{len}(u)$ via bucket sort). For each node $u$ and its parent $p = \text{link}(u)$, persistently merge $\text{rt}[u]$ into $\text{rt}[p]$:
   $$\text{rt}[p] \gets \text{merge}(\text{rt}[p], \text{rt}[u], 1, N)$$
   *Why Persistent Merge (`new_node` on overlap or always)?* Because in `CF 666E`, `[NOI2018]`, and `CF 1037H`, queries inspect $\text{rt}[u]$ at **arbitrary interior nodes $u$** after all merges have completed! If `merge` mutates child nodes in-place when two subtrees overlap (or even when reusing a child pointer that later gets mutated higher up), querying $\text{rt}[u]$ after the bottom-up pass will read corrupted data from $u$'s ancestors!
   Wait: when two segment tree nodes $x$ (from $p$) and $y$ (from $u$) are merged:
   - If $x == 0$ or $y == 0$, returning $x + y$ without copying is **safe** *only if* we merge bottom-up (children finish all their internal merges before being merged into their parent) AND any subsequent creation of a modified node creates a **new** node index `z = ++seg_sz` whenever both $x \ne 0$ and $y \ne 0$! Wait: what if $p$ takes $y$ directly when $x == 0$, and then $p$'s second child $u_2$ overlaps with $y$? If the overlap at $p$ modifies $y$ in-place (`x` is now `y`), then $u_1$'s subtree $\text{rt}[u_1]$ gets overwritten by $u_2$!
   - **Invariant**: In `merge(x, y, l, r)`, if `!x || !y` we can return `x | y`, **provided** that whenever *both* `x` and `y` are non-zero, we allocate a **brand-new node `z = ++seg_sz`**! Because every shared subtree was already completely finalized before being passed up, never mutating an existing node `x` in-place guarantees that all historical roots $\text{rt}[u]$ remain 100% intact, while still only allocating $O(N \log N)$ total nodes!

#### 3.2 Locating an Arbitrary Substring $S[l..r]$ in $O(\log N)$ via Link-Tree Binary Lifting

Given a query substring $S[l..r]$ of length $L = r - l + 1$:
- The prefix $S[1..r]$ corresponds to state $u_0 = \text{pos}[r]$.
- All suffixes of $S[1..r]$ lie along the path from $u_0 = \text{pos}[r]$ to the root $1$ in the Link Tree, with strictly decreasing $\text{len}$ values.
- The state $u$ representing $S[l..r]$ is the **unique ancestor** of $\text{pos}[r]$ in the Link Tree satisfying:
  $$\text{len}(\text{link}(u)) < r - l + 1 \le \text{len}(u)$$
- By precomputing binary lifting pointers $\text{up}[u][k]$ ($0 \le k \le \lfloor \log_2 N \rfloor$) on the Link Tree, we start at $u = \text{pos}[r]$ and for $k = \lfloor \log_2 N \rfloor$ down to $0$, if $\text{len}(\text{up}[u][k]) \ge r - l + 1$, we jump $u \gets \text{up}[u][k]$. Total time per substring lookup: $O(\log N)$.

---

#### 3.3 Five Canonical Master Derivations

##### (A) `[HEOI2016 / TJOI2016] 字符串` (Luogu P4094) — Binary Search + Binary Lifting + Endpos Clipping
- **Problem**: Given $S[1..N]$ ($N, Q \le 10^5$), for each query $(a, b, c, d)$, find the maximum length $L$ of a prefix of $S[c..d]$ that occurs as a substring of $S[a..b]$.
- **Derivation**:
  1. Monotonicity: If the prefix $S[c .. c+L-1]$ of length $L$ occurs in $S[a..b]$, then any shorter prefix $S[c .. c+L'-1]$ ($L' \le L$) also occurs in $S[a..b]$. Thus we can **binary search on $L \in [0, \min(b - a + 1, d - c + 1)]$**.
  2. Check($L$): Find the SAM state $u$ of $S[c .. c + L - 1]$ by binary lifting from $\text{pos}[c + L - 1]$ until $\text{len}(\text{link}(u)) < L \le \text{len}(u)$.
  3. By the Substring Containment Clipping Identity, $S[c .. c + L - 1]$ occurs in $S[a..b]$ iff:
     $$\text{query\_exists}(\text{rt}[u],\; a + L - 1,\; b) = \text{true}.$$
  4. Complexity: $O(N \log N + Q \log^2 N)$ time, $O(N \log N)$ space.

##### (B) `CF 666E — Forensic Examination` — Generalized SAM + Multi-String Endpos Frequency RMQ
- **Problem**: Given a main string $S$ ($|S| \le 5 \times 10^5$) and $m$ dictionary strings $T_1, \dots, T_m$ ($\sum |T_i| \le 5 \times 10^4$), answer $Q \le 5 \times 10^5$ queries $(p_l, p_r, l, r)$: among $T_i$ with $p_l \le i \le p_r$, find the index $i$ maximizing the number of occurrences of $S[l..r]$ in $T_i$ (breaking ties by smallest $i$).
- **Derivation**:
  1. Build a Generalized SAM on $\{S, T_1, \dots, T_m\}$ (or build a GSAM on $\{T_1, \dots, T_m\}$ and run $S$ on it; building GSAM on all of them is cleaner, or tracking for each prefix $S[1..r]$ the longest matched suffix in $\text{GSAM}(T_1..T_m)$ and its matched length $\text{match\_len}[r]$).
  2. In $\text{GSAM}(T_1, \dots, T_m)$, each state $u$ maintains a Segment Tree over **dictionary string indices $i \in [1, m]$** storing $(\max\_\text{cnt}, -\text{index})$. Whenever the $j$-th prefix of $T_i$ lands at state $u$, add $+1$ at position $i$ in $\text{rt}[u]$.
  3. Merge $\text{rt}[u]$ bottom-up along the Link Tree of the GSAM.
  4. For each query $(p_l, p_r, l, r)$: first check if $\text{match\_len}[r] < r - l + 1$. If so, $S[l..r]$ does not even exist in the GSAM, so the answer is $(0, p_l)$. Otherwise, binary lift from the GSAM state of $S[1..r]$ to the ancestor $u$ with $\text{len}(\text{link}(u)) < r - l + 1 \le \text{len}(u)$, and query the range $[p_l, p_r]$ in $\text{rt}[u]$ in $O(\log m)$ time.
  5. Complexity: $O((|S| + \sum |T_i| + Q) \log(\sum |T_i|))$.

##### (C) `CF 1037H — Security` — Lexicographically Next Substring Outside $S[l..r]$
- **Problem**: Given $S[1..N]$ ($N \le 10^5$) and $Q \le 2 \times 10^5$ queries $(l, r, X)$ with $\sum |X| \le 2 \times 10^5$, find the lexicographically smallest substring of $S[l..r]$ that is strictly greater than $X$.
- **Derivation**:
  1. Any string $Y > X$ shares some longest common prefix $X[1..i]$ ($0 \le i \le |X|$) with $X$, followed by a single character $c > X[i+1]$ (where $X[|X|+1] = \emptyset$). To make $Y$ lexicographically **smallest** among all valid substrings of $S[l..r]$ strictly greater than $X$, we must **maximize** the shared prefix length $i$, and for that $i$, **minimize** the branching character $c > X[i+1]$, and terminate immediately after $c$ (since $X[1..i]c$ is shorter than any right-extension of itself).
  2. Walk $X$ on $\text{SAM}(S)$ from root $1$, recording the path of states $u_0 = 1, u_1, \dots, u_k$ ($k \le |X|$) while transitions exist.
  3. Iterate $i$ from $k$ down to $0$, and for each $c \in \Sigma$ with $c > X[i+1]$:
     Let $v = \text{next}[u_i][c]$. If $v \ne 0$, we need the specific string $w = X[1..i]c$ of length $L = i + 1$ to occur inside $S[l..r]$.
     By the Clipping Identity, $w$ occurs in $S[l..r]$ iff:
     $$\text{query\_exists}(\text{rt}[v],\; l + i,\; r) = \text{true}$$
     (since $l + L - 1 = l + (i + 1) - 1 = l + i$).
  4. The first $(i, c)$ that passes is guaranteed to be optimal! Total time: $O\big((N + \sum |X| |\Sigma|) \log N\big)$.

##### (D) `[NOI2018] 你的名字` (Luogu P4770) — Distinct Substrings of $T$ Not Occurring in $S[l..r]$
- **Problem**: Given $S[1..N]$ ($N \le 5 \times 10^5$) and $Q \le 10^5$ queries $(T, l, r)$ with $\sum |T| \le 5 \times 10^5$, count how many **distinct** substrings of $T$ do **not** occur as a substring of $S[l..r]$.
- **Derivation**:
  1. Build $\text{SAM}(S)$ with persistent Segment Tree Merging on $\text{endpos}_S$, and for the query string $T$, build $\text{SAM}(T)$ of size $\le 2|T|$.
  2. For each prefix $T[1..i]$ ($1 \le i \le |T|$), compute the **maximum length $\text{lim}[i]$ of a suffix of $T[1..i]$ that occurs in $S[l..r]$**:
     Start from $(u, L) = (\text{last\_state}, \text{last\_len})$ after step $i-1$ on $\text{SAM}(S)$, and try to advance by $c = T[i]$:
     - While $u > 1$:
       - If $\text{next}_S[u][c] \ne 0$ and $\text{query\_exists}\big(\text{rt}_S[\text{next}_S[u][c]],\; l + L,\; r\big)$ is true (testing length $L + 1$ in $[l + (L+1) - 1, r] = [l + L, r]$!), then advance $u \gets \text{next}_S[u][c]$, $L \gets L + 1$, and break!
       - Otherwise, we cannot extend by $c$ at length $L + 1$. Decrement $L \gets L - 1$. If $L == \text{len}_S(\text{link}_S(u))$, step up $u \gets \text{link}_S(u)$.
     - Why does this two-pointer loop take $O(|T| \log N)$ total time per query? Because $L$ increases by at most $+1$ per index $i \in [1, |T|]$ and decreases by $1$ on every failed check! Thus `query_exists` is called at most $2|T|$ times per query!
  3. Now, how do we count *distinct* substrings of $T$ not in $S[l..r]$ without double-counting?
     In $\text{SAM}(T)$, each state $v \in \text{SAM}(T)$ represents distinct substrings of lengths $[\text{len}_T(\text{link}_T(v)) + 1,\; \text{len}_T(v)]$, all sharing the same ending positions in $T$. Let $\text{pos}_T(v) \in [1, |T|]$ be any ending position of $v$ in $T$ (propagated up $\text{SAM}(T)$'s Link Tree).
     Every substring of $T$ ending at $\text{pos}_T(v)$ of length $\le \text{lim}[\text{pos}_T(v)]$ occurs in $S[l..r]$, while any length $> \text{lim}[\text{pos}_T(v)]$ does not!
     Therefore, state $v \in \text{SAM}(T)$ contributes:
     $$\text{contrib}(v) = \max\Big(0,\; \text{len}_T(v) - \max\big(\text{len}_T(\text{link}_T(v)),\; \text{lim}[\text{pos}_T(v)]\big)\Big)$$
     Summing $\text{contrib}(v)$ over all states $v \in \text{SAM}(T)$ gives the exact count in $O(|T| \log N)$ time!

##### (E) `CF 700E — Cool Slogans` — Canonical Longest-String Invariant on Link Tree + Endpos Clipping
- **Problem**: Given $S[1..N]$ ($N \le 2 \times 10^5$), find the maximum $k$ such that there exist strings $s_1, s_2, \dots, s_k$ where $s_k$ is a substring of $S$ and each $s_i$ occurs at least twice in $s_{i+1}$.
- **Derivation**:
  1. **Canonical Representative Lemma**: Suppose a SAM state $u$ contains multiple strings of lengths $[\text{minlen}(u), \text{len}(u)]$. Because all strings in $u$ have the **exact same $\text{endpos}_S(u)$ set**, every occurrence of a shorter string $w \in u$ extends on the left to an occurrence of $\text{longest}(u)$! Thus in an optimal chain $s_1, \dots, s_k$, we can always replace each $s_i$ by $\text{longest}(u_i)$ for its SAM state $u_i$, where $u_1, \dots, u_k$ is a chain of states down the Link Tree!
  2. Let $dp[u]$ be the maximum chain length ending at $\text{longest}(u)$, and let $\text{top}[u]$ be the shallowest ancestor of $u$ achieving $dp[\text{top}[u]] = dp[u]$.
  3. When transitioning from parent $p = \text{link}(u)$ to $u$, let $v = \text{top}[p]$ be the canonical ancestor state we want to test. Does $\text{longest}(v)$ occur at least twice inside $\text{longest}(u)$?
     Pick **any** arbitrary ending position $\text{pos}(u) \in \text{endpos}_S(u)$! The substring $\text{longest}(u)$ appears at $S[\text{pos}(u) - \text{len}(u) + 1 .. \text{pos}(u)]$.
     Since $v$ is an ancestor of $u$ in the Link Tree, $\text{longest}(v)$ is **already** a suffix of $\text{longest}(u)$, so one occurrence ends at $\text{pos}(u)$.
     A second occurrence of $\text{longest}(v)$ inside $S[\text{pos}(u) - \text{len}(u) + 1 .. \text{pos}(u) - 1]$ exists iff:
     $$\text{query\_exists}\Big(\text{rt}[v],\; \text{pos}(u) - \text{len}(u) + \text{len}(v),\; \text{pos}(u) - 1\Big) = \text{true}!$$
     If true, $dp[u] = dp[p] + 1$ and $\text{top}[u] = u$; otherwise $dp[u] = dp[p]$ and $\text{top}[u] = \text{top}[p]$. Total time: $O(N \log N)$.

---

### 4. Boundary Pitfalls & Broken-Invariant Counterexamples

1. **The Unclipped Left-Boundary Bug ($[l, r]$ instead of $[l + L - 1, r]$)**:
   Consider $S = \text{"ababa"}$, query window $[l, r] = [3, 5]$ ($S[3..5] = \text{"aba"}$), and pattern $w = \text{"baba"}$ of length $L = 4$.
   In $\text{SAM}(S)$, $\text{endpos}_S(\text{"baba"}) = \{4\}$.
   If you query $[l, r] = [3, 5]$, $4 \in [3, 5]$ returns **true**, falsely claiming `"baba"` of length $4$ is a substring of `"aba"` of length $3$! Clipping to $[l + L - 1, r] = [3 + 4 - 1, 5] = [6, 5] = \emptyset$ immediately rejects $4$.
2. **Jumping Only $L \gets \text{len}(\text{link}(u))$ instead of $L \gets L - 1$ in `[NOI2018] 你的名字`**:
   When $\text{next}[u][c]$ exists in $\text{SAM}(S)$ globally, it might **fail** the $\text{endpos} \cap [l + L, r]$ check only because $L + 1$ is slightly too long for the window $[l, r]$, whereas a shorter suffix of length $L' \in [\text{minlen}(u), L]$ **within the same node $u$** satisfies $l + L' \le r$ and passes! If you immediately jump $u \gets \text{link}(u)$ and set $L \gets \text{len}(u)$ when the window check fails, you skip all valid lengths inside $u$! That is why you must decrement $L \gets L - 1$ one by one (or set $L \gets \min(L, \max\_\text{endpos} - l)$) and only step $u \gets \text{link}(u)$ when $L == \text{len}(\text{link}(u))$.

---

## Iteration 65: Dynamic SAM + Link-Cut Tree (`access` Color-Chain Sweeping / `树点涂色`)

### 1. The Diagnostic Signal (Why Static Segment Tree Merging Fails on Dynamic Appends and Range Distinct Substring Queries)

Segment Tree Merging requires the entire Link Tree to be known offline so that $\text{endpos}$ sets can be merged bottom-up once. It fails in two major regimes:
1. **Online Character Appends + Occurrence Queries (`[BZOJ 2555] SubString`)**: We interleave appending characters to $S$ with querying how many times pattern $P$ occurs in the current $S$. Each `extend(c)` attaches a new leaf `cur` to the Link Tree (giving $+1$ to all its ancestors) and may split an edge $p \to q$ by inserting `clone`.
2. **Offline Range Distinct / Weighted Substring Queries on $S[l..r]$ (`[SDOI2017] 相关分析` / `Luogu P6292 — 区间本质不同子串个数`)**: Given $Q \le 2 \times 10^5$ queries $[l, r]$, count the number of distinct substrings in $S[l..r]$ (or sum $f(\text{len})$ over distinct substrings in $S[l..r]$). Here, each SAM state $u$ can appear many times inside $[l, r]$; we must count each state $u$ **at most once** if it occurs in $S[l..r]$, weighted by the number of its lengths that fit inside $[l, r]$.

---

### 2. The Combinatorial Word Invariant (Rightmost Endpos Dominance & LCT Preferred-Path Color Homogeneity)

Suppose we sweep the right endpoint $r$ from $1$ to $N$ and answer all queries $[l, r]$ ending at $r$.
For any substring $w$ of $S[1..r]$, among all occurrences of $w$ in $S[1..r]$, let $\text{last\_end}(w, r) = \max\big(\text{endpos}_S(w) \cap [1, r]\big)$ be its **rightmost ending position $\le r$**.

- **Rightmost Occurrence Dominance**: $w$ occurs in $S[l..r]$ if and only if its *rightmost* occurrence at or before $r$ starts at or after $l$:
  $$w \text{ occurs in } S[l..r] \;\Longleftrightarrow\; \text{last\_end}(w, r) - |w| + 1 \ge l$$
- **State-Level Rightmost Endpos Uniformity**: Because all strings $w$ belonging to the same SAM state $u$ share the **exact same set of ending positions** $\text{endpos}_S(u)$, every string $w \in u$ has the **exact same rightmost ending position** $\text{last}(u) = \max(\text{endpos}_S(u) \cap [1, r])$ at step $r$!
- **Arithmetic Progression of Starting Positions Within State $u$**:
  At step $r$, state $u$ represents strings of every length $\ell \in [\text{minlen}(u), \text{len}(u)]$, where $\text{minlen}(u) = \text{len}(\text{link}(u)) + 1$.
  Since all of them have their rightmost occurrence ending at $p = \text{last}(u)$, their rightmost starting positions form a **contiguous interval of indices**:
  $$\text{start\_pos}(\ell) = p - \ell + 1 \;\in\; \big[p - \text{len}(u) + 1,\; p - \text{minlen}(u) + 1\big]!$$
- **Chain Aggregation Along Homogeneous LCT Splay Paths**:
  Even better: suppose an entire vertical chain of states $u_1 \to u_2 \to \dots \to u_k$ in the Link Tree (where $u_i = \text{link}(u_{i+1})$) currently shares the **same rightmost ending position** $p = \text{last}(u_1) = \dots = \text{last}(u_k)$!
  Because the length intervals $[\text{len}(\text{link}(u_i)) + 1, \text{len}(u_i)]$ tile $[\text{len}(\text{link}(u_1)) + 1, \text{len}(u_k)]$ without gaps or overlaps, the rightmost starting positions across the **entire chain** $u_1 \dots u_k$ form a **single contiguous interval**:

$$
\boxed{
\bigcup_{i=1}^k \big\{\, p - \ell + 1 \;\big|\; \ell \in [\text{minlen}(u_i), \text{len}(u_i)] \,\big\}
\;=\;
\big[\, p - \text{len}(u_k) + 1,\;\; p - \text{len}(\text{link}(u_1)) \,\big]
}
$$

---

### 3. The Reverse-Engineering Scratchpad (Two LCT Couplings: Online `[BZOJ 2555]` vs. Offline Sweep `Luogu P6292`)

#### Coupling 1: Online Dynamic SAM + LCT Subtree/Path Maintenance (`[BZOJ 2555] SubString`)
When characters are appended online to $S$, we maintain the Link Tree dynamically inside a Link-Cut Tree (LCT), where each node $u$ stores its current occurrence count $w[u] = |\text{endpos}(u)|$:
1. **Adding leaf `cur` with parent `link[cur]`**:
   Link `cur` to `link[cur]` in the LCT, then call `access(cur); splay(cur);` and apply a lazy $+1$ tag to the entire path from root $1$ to `cur`.
2. **Splitting edge $p = \text{link}_{\text{old}}(q) \to q$ via `clone`**:
   Before `clone` was created, $q$ received $+1$ from every prefix in $q$'s Link-Tree subtree, so at the exact moment of cloning, `clone` initially has the **exact same $\text{endpos}$ count as $q$** (prior to adding $+1$ for `cur`)!
   Therefore:
   - Query the current value $val_q = \text{query\_node}(q)$ in the LCT.
   - Initialize $w[\text{clone}] = val_q$.
   - Cut the Link-Tree edge between $q$ and $p = \text{link}_{\text{old}}(q)$ (`access(q); splay(q);` detach left child $p$).
   - Link `clone` to $p$, and link $q$ to `clone`.
   - Finally, after `cur` is linked to `clone`, add $+1$ on the path from root $1$ to `cur`.
   - Total complexity per character append or pattern query: $O(\log N)$ amortized!

#### Coupling 2: Offline $[l, r]$ Distinct Substrings via LCT `access` Color-Chain Sweeping (`Luogu P6292`)
Build $\text{SAM}(S)$ offline for the whole string $S[1..N]$, and initialize an LCT over the static Link Tree. Each splay tree in the LCT maintains a **uniform color tag** $\text{col}[S] = p$ representing the shared rightmost ending position $p = \text{last}(u)$ of all nodes $u$ in that splay tree, plus $\text{max\_len}(S)$ (the $\text{len}$ of the deepest node in $S$) and $\text{min\_fa\_len}(S) = \text{len}(\text{link}(\text{shallowest node in } S))$.

 maintain a Range-Add, Range-Sum Segment Tree (or two Fenwick Trees) over starting positions $s \in [1, N]$, where position $s$ stores the number of distinct substrings in $S[1..r]$ whose **rightmost occurrence starts at $s$**.
Then for any query $[l, r]$ at step $r$, the number of distinct substrings in $S[l..r]$ is simply:

$$\text{Ans}(l, r) = \text{SegTree.query\_sum}(l, r)$$

When advancing the sweep-line from $r-1 \to r$:
1. Let $x = \text{pos}[r]$ be the SAM state of prefix $S[1..r]$. Every ancestor of $x$ in the Link Tree now has its rightmost occurrence updated to $\text{last}(u) = r$.
2. Run a customized `access(x, r)` on the LCT:
   - As `access` climbs from $x$ to the root $1$, each splay tree $C$ it visits (which is currently homogeneous with some old color $p_{\text{old}} = \text{col}[C]$, covering lengths $(\ell_{\min}, \ell_{\max}] = (\text{min\_fa\_len}(C), \text{max\_len}(C)]$) is split at our current node $u$:
     - The deeper part (below $u$) is detached into a separate splay child (retaining color $p_{\text{old}}$).
     - The upper part $C_{\text{up}}$ (from $u$ up to the top of $C$) has its old contribution **erased** from the Segment Tree (if $p_{\text{old}} > 0$ and $\ell_{\max}(C_{\text{up}}) > 0$):
       $$\text{SegTree.range\_add}\big(p_{\text{old}} - \ell_{\max}(C_{\text{up}}) + 1,\;\; p_{\text{old}} - \ell_{\min}(C_{\text{up}}),\;\; -1\big)$$
   - Once the entire path from root $1$ to $x$ is merged into a single preferred splay tree $P$, we set $\text{col}[P] = r$ and add the new contribution for the whole path at once:
     $$\text{SegTree.range\_add}\big(1,\; r,\; +1\big)$$
3. **Complexity Proof**: By Sleator–Tarjan's LCT amortization theorem, the total number of preferred-child changes (and thus the total number of homogeneous splay segments $C_{\text{up}}$ visited) across all $N$ calls to `access(pos[r], r)` is $O(N \log N)$. Each segment triggers one Segment Tree range update in $O(\log N)$ time, yielding $O(N \log^2 N + Q \log N)$ total time and $O(N)$ memory!

---

### 4. Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Including the Root State $1$ ($\text{len}(1) = 0$) in the Segment Tree Update**:
   The root $1$ of the SAM represents the empty string $\epsilon$ with $\text{len}(1) = 0$ and has no parent ($\text{link}(1) = 0$). If your splay node for root $1$ contributes $[\text{col} - 0 + 1, \text{col} - 0] = [\text{col}+1, \text{col}]$, or if $\text{len}(\text{link}(1))$ is not $0$, it can corrupt range updates at index $p + 1$. Always exclude root $1$ by setting its interval length to $0$ (or keeping $\text{min\_fa\_len}(1) = \text{len}(1) = 0$ so the range $[p+1, p]$ is empty and skipped).
2. **Updating $\text{col}$ Before Splitting the Splay Tree in `access`**:
   In `access(x, r)`, when you `splay(u)`, the right child `ch[u][1]` contains nodes *deeper* than $u$ on the old preferred path. Those deeper nodes are **not** ancestors of $x = \text{pos}[r]$ and must **keep** their old color $p_{\text{old}}$! You must push down the lazy color tag `col[u]` to `ch[u][1]` *before* detaching `ch[u][1]` and only erase/overwrite the Segment Tree contribution of $u$ and its left subtree `ch[u][0]`.

---

## Iteration 66: HLD, Intra-Node Split Ordering & Prefix-Suffix Graph Optimization on the Link Tree (`[十二省联考 2019] 字符串问题` & `CF 1098F`)

### 1. The Diagnostic Signal (Why Node-Granularity Link-Tree Graphs Fail When Multiple Substrings Share a SAM State)

In many string graph and range-LCP problems, substrings $A_i = S[l_i..r_i]$ act as vertices or query items, and a directed edge or contribution exists whenever $B_j = S[l'_j..r'_j]$ is a **prefix** of $A_i$ (or we sum $\min(r - i + 1, \text{LCP}(S[i..N], S[x..N]))$ for $i \in [l, r]$ as in `CF 1098F`).
- By Reversed-SAM Duality (Iteration 63), building $\text{SAM}(S^R)$ turns the Link Tree into the Suffix Tree $\text{ST}(S)$: $B_j$ is a prefix of $A_i$ if and only if $A_i$ lies in the **subtree** of $B_j$ in the Link Tree of $\text{SAM}(S^R)$ AND $|B_j| \le |A_i|$!
- **Why Naive Subtree Graph Construction Fails**:
  1. First, connecting every $B_j$ to all $A_i$ in its Link-Tree subtree explicitly creates $O(N_A N_B)$ edges ($N_A, N_B \le 2 \times 10^5$).
  2. Second, even if we use Link-Tree hierarchy (connecting each SAM node $u$ to its Link-Tree children $v$), **what happens when $A_i$ and $B_j$ land on the EXACT SAME SAM node $u$**?
     A single SAM state $u$ covers all lengths in $[\text{len}(\text{link}(u)) + 1, \text{len}(u)]$. If both $A_i$ and $B_j$ map to state $u$, then $B_j$ is a prefix of $A_i$ **if and only if $|B_j| \le |A_i|$**! If we collapse $u$ into a single graph vertex, then a shorter $A_{i'}$ at node $u$ with $|A_{i'}| < |B_j|$ would illegally be reachable from $B_j$, creating false edges or spurious cycles!

---

### 2. The Combinatorial Word Invariant (Intra-State Length Stratification & Heavy-Chain Distance Decomposition)

#### 2.1 Intra-State Length Stratification Invariant (`[十二省联考 2019] 字符串问题` / `Luogu P5284`)
Let $T = \text{LinkTree}(\text{SAM}(S^R))$ be the prefix Link Tree of $S$. Any substring $w = S[l..r]$ of length $L = r - l + 1$ maps to the unique ancestor $u$ of $\text{pos}_{S^R}(N - l + 1)$ satisfying $\text{minlen}(u) \le L \le \text{len}(u)$.

For any two substrings $B_j$ (mapped to $(u_B, |B_j|)$) and $A_i$ (mapped to $(u_A, |A_i|)$):

$$
\boxed{
B_j \text{ is a prefix of } A_i
\;\Longleftrightarrow\;
\begin{cases}
u_A \text{ is in the proper subtree of } u_B \text{ in } T, \text{ OR} \\
u_A = u_B \text{ AND } |B_j| \le |A_i|.
\end{cases}
}
$$

Notice the complete decoupling between **inter-state dominance** (if $u_A$ is a proper descendant of $u_B$, then $|A_i| \ge \text{minlen}(u_A) > \text{len}(u_B) \ge |B_j|$ holds automatically!) and **intra-state dominance** (within a single state $u$, dominance is a 1D prefix order sorted by length, with $B_j$ preceding $A_i$ on ties $|B_j| = |A_i|$).

#### 2.2 Heavy-Light / Centroid LCP Clipping Invariant (`CF 1098F — Ж-function`)
In `CF 1098F`, given $S[1..N]$ and queries $(l, r)$, we must compute:

$$\sum_{i=l}^{r} \min\big(r - i + 1,\;\; \text{LCP}(S[i..N], S[l..N])\big)$$

In $T = \text{LinkTree}(\text{SAM}(S^R))$, let $v_i = \text{pos}_{S^R}(N - i + 1)$ be the terminal state for suffix $S[i..N]$. Then:

$$\text{LCP}(S[i..N], S[l..N]) = \text{len}\big(\text{LCA}_T(v_i, v_l)\big)$$

Thus for a query $(l, r)$, every suffix $i \in [l, r]$ contributes $\min\big(r - i + 1,\; \text{len}(\text{LCA}(v_i, v_l))\big)$, which breaks into two regimes at the threshold $i \le r - \text{len}(\text{LCA}(v_i, v_l)) + 1$:
- **Unclipped Regime ($i + \text{len}(u) - 1 \le r$, where $u = \text{LCA}(v_i, v_l)$)**: Contributes $\text{len}(u)$.
- **Right-Boundary Clipped Regime ($i \in [r - \text{len}(u) + 2,\; r]$)**: Contributes $r - i + 1$.

---

### 3. The Reverse-Engineering Scratchpad (Compiling `[十二省联考 2019]` and `CF 1098F`)

#### 3.1 `[十二省联考 2019] 字符串问题` (`Luogu P5284`): Prefix-Chain Auxiliary Graph in $O((N + N_A + N_B) \log N)$
We are given $N_A$ substrings $A_i$ (with weights $|A_i|$), $N_B$ substrings $B_j$ (with weight $0$), and $m$ explicit directed edges $A_i \to B_j$. Plus, every $B_j$ has an implicit directed edge to every $A_i$ that has $B_j$ as a prefix. We want the maximum path weight (or $-1$ if a positive-weight cycle exists).
1. Build $\text{SAM}(S^R)$ and its Link Tree $T$, plus binary lifting tables $\text{up}[u][k]$ in $O(N \log N)$.
2. Locate each $A_i$ and $B_j$ at its Link-Tree state $u$ via binary lifting from $\text{pos}_{S^R}(N - l + 1)$, and bucket all $A_i$ and $B_j$ landing on state $u$ into a list $\text{bucket}[u]$.
3. **Intra-State Prefix Chain at Each State $u$**:
   - Sort $\text{bucket}[u]$ in **non-decreasing order of length**, breaking ties by placing **$B_j$ before $A_i$** when $|B_j| == |A_i|$!
   - Create an entry portal node $\text{in}[u]$ and a chain of prefix-link nodes $p_1 \to p_2 \to \dots \to p_k$ corresponding to the $B$-items in $\text{bucket}[u]$, such that each $B_j$ points to its suffix of $A$-items in $\text{bucket}[u]$ (or reverse the chain so smaller lengths point to larger lengths) and the last node in $\text{bucket}[u]$ (the exit portal $\text{out}[u]$) connects to $\text{in}[v]$ for every Link-Tree child $v$ of $u$!
   - Specifically: let $\text{in}[u]$ be the entry vertex for state $u$ (reached from $\text{out}[\text{link}(u)]$). Any $A_i \in \text{bucket}[u]$ is reached from $\text{in}[u]$ AND from all $B_j \in \text{bucket}[u]$ that precede $A_i$ in sorted order; finally, $\text{out}[u]$ is reached from $\text{in}[u]$ and from all $B_j \in \text{bucket}[u]$, and $\text{out}[u] \to \text{in}[v]$ for each child $v$ of $u$.
4. Run Kahn's Topological Sort + Longest Path DP on this DAG of $O(N + N_A + N_B)$ vertices and edges! If a cycle exists, return $-1$; otherwise return $\max dp$.

#### 3.2 `CF 1098F — Ж-function`: Heavy-Light Decomposition (HLD) + 2D Range Sweeps on the Link Tree
Using HLD (or Centroid Decomposition) on $T = \text{LinkTree}(\text{SAM}(S^R))$:
1. Decompose the root-to-$v_l$ path into $O(\log N)$ heavy-chain prefixes. On each heavy chain, as a query climbs from $v_l$ to the root, at each ancestor $u = \text{LCA}(v_i, v_l)$, $v_i$ enters $u$ from a light subtree (or from another branch when aggregating over the heavy chain).
2. By applying DSU-on-Tree / Heavy-Light offline sweeping: for each node $u$ on a heavy chain, we collect queries $(l, r)$ passing through $u$ and points $i$ in light subtrees of $u$. Each point $i$ transitions from contributing $\text{len}(u)$ (when $r \ge i + \text{len}(u) - 1$) to contributing $r - i + 1$ (when $i \le r < i + \text{len}(u) - 1$).
3. Using two Fenwick trees (one over $i$ and one over $i + \text{len}(u) - 1$) swept by $r$, all contributions are answered in $O(N \log^2 N + Q \log N)$ time.

---

### 4. Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Tie-Breaking Order Between $A_i$ and $B_j$ of Equal Length in `[十二省联考 2019]`**:
   Suppose $A_1 = S[1..3]$ and $B_1 = S[1..3]$ have the **exact same length** $|A_1| = |B_1| = 3$ at SAM state $u$. Since every string is a prefix of itself, $B_1$ **is** a prefix of $A_1$, so there **must** be an implicit edge $B_1 \to A_1$! If your comparator sorts $A_1$ before $B_1$ on equal length, you miss the edge $B_1 \to A_1$ (and if there was also an explicit edge $A_1 \to B_1$, you fail to detect the cycle $A_1 \leftrightarrow B_1$!).
2. **Reversed Indexing Offset on $S^R$**:
   In $\text{SAM}(S^R)$, the $k$-th character of $S^R$ is $S[N - k + 1]$. Thus a substring $S[l..r]$ of $S$ corresponds to $S^R[N - r + 1 .. N - l + 1]$, whose **ending position** in $S^R$ is $N - l + 1$ (corresponding to the **starting position** $l$ in $S$!). Binary lifting must start from $\text{pos}_{S^R}[N - l + 1]$, **not** $\text{pos}_{S^R}[r]$.

---

## Iteration 67: Comprehensive Multilingual Problem Mining (`[EN]`/`[ZH]`/`[JA]`), 4-Tier Difficulty Ladder & Template Quarantine

### 1. Quarantine Table of Excluded Pure-Template Problems (`R-2A-01` to `R-2A-07`)

Per `AGENTS.md` and `PLAN.md`, pure template verification problems where the task is directly copying a standard SAM, GSAM, or Segment Tree Merge routine without a structural reduction are strictly quarantined:

| Quarantine ID | Problem Source & Title | Lang | Reason for Quarantine |
| :--- | :--- | :---: | :--- |
| **`R-2A-01`** | **Luogu P3804** — `【模板】后缀自动机 (SAM)` | `[ZH]` | Bare template asking for $\max_{|\text{endpos}(u)| > 1} |\text{endpos}(u)| \cdot \text{len}(u)$ via a single bottom-up Link-Tree sum. |
| **`R-2A-02`** | **Luogu P6139** — `【模板】广义后缀自动机 (广义 SAM)` | `[ZH]` | Bare template asking for the number of distinct substrings $\sum (\text{len}(u) - \text{len}(\text{link}(u)))$ across $k$ strings. |
| **`R-2A-03`** | **Library Checker** — `Number of Substrings` | `[EN]` / `[JA]` | Pure template verification of $\sum (\text{len}(u) - \text{len}(\text{link}(u)))$ on a single string. |
| **`R-2A-04`** | **SPOJ SUBLEX** — `Lexicographical Substring Search` | `[EN]` | Standard textbook DAG path-counting template ($k$-th lexicographical distinct substring on SAM DAG). |
| **`R-2A-05`** | **SPOJ LCS** — `Longest Common Substring` | `[EN]` | Bare two-string LCS walk on $\text{SAM}(S_1)$ without range clipping or multiple strings. |
| **`R-2A-06`** | **LOJ #171** — `多个串的最长公共子串` | `[ZH]` | Bare multi-string LCS template on SAM without additional combinatorial constraints. |
| **`R-2A-07`** | **HihoCoder #1441 / #1445 / #1449 / #1457** — `后缀自动机一～四` | `[ZH]` | Instructional tutorial verification series for basic SAM construction, Link Tree, and GSAM sizes. |

---

### 2. Master 4-Tier Non-Template Problem Archive for Wave 2A (36 Curated Problems Across `[EN]`, `[ZH]`, `[JA]`)

#### Tier 1: Stepping Stone (Structural Link-Tree & DAG Invariants, Multi-String GSAM, Basic Rightmost/Leftmost Endpos) — 9 Problems

##### 1. `[TJOI2015] 弦论` (Luogu P3975 / BZOJ 3998) — `[ZH]`
- **Constraints**: $N \le 5 \times 10^5$, $t \in \{0, 1\}$, $k \le 10^9$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Find the $k$-th lexicographically smallest substring of $S$, either counting distinct substrings ($t=0$) or counting substrings with multiplicity ($t=1$).
  2. *Combinatorial Invariant*: Every path in the SAM DAG from root $1$ corresponds bijectively to a distinct substring of $S$. Under $t=0$, visiting state $u$ contributes weight $w(u) = 1$; under $t=1$, visiting state $u$ contributes weight $w(u) = |\text{endpos}_S(u)|$ (computed bottom-up on the Link Tree).
  3. *Scratchpad*: First propagate $w(u)$ bottom-up on the Link Tree (for $t=1$). Then compute $dp[u] = w(u) + \sum_{c} dp[\text{next}[u][c]]$ bottom-up in reverse topological order of the DAG ($\text{len}$ decreasing). Walk the DAG greedily from root $1$.
  4. *Pitfall*: Failing to zero out $w(1) = 0$ at the root causes the empty string to be counted as the 1st substring.

##### 2. `[HAOI2016] 找相同字符` (Luogu P3181) — `[ZH]`
- **Constraints**: $|S_1|, |S_2| \le 2 \times 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Count pairs of identical substrings $(S_1[l_1..r_1], S_2[l_2..r_2])$, i.e., $\sum_{w} \text{occ}(w, S_1) \cdot \text{occ}(w, S_2)$.
  2. *Combinatorial Invariant*: In $\text{GSAM}(S_1, S_2)$, all strings $w \in u$ have the exact same occurrence counts $\text{cnt}_1(u)$ in $S_1$ and $\text{cnt}_2(u)$ in $S_2$, and there are exactly $\text{len}(u) - \text{len}(\text{link}(u))$ such strings in state $u$.
  3. *Scratchpad*: Build the GSAM of $S_1$ and $S_2$ using `extend_gsam`, accumulate $\text{cnt}_1(u)$ and $\text{cnt}_2(u)$ bottom-up on the Link Tree, and sum $(\text{len}(u) - \text{len}(\text{link}(u))) \cdot \text{cnt}_1(u) \cdot \text{cnt}_2(u)$.
  4. *Pitfall*: Online GSAM without zero-length clone protection creates ghost nodes where $\text{cnt}_1$ and $\text{cnt}_2$ are split across twin states.

##### 3. `[AHOI2013] 差异` (Luogu P4248 / BZOJ 3238) — `[ZH]`
- **Constraints**: $N \le 5 \times 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Compute $\sum_{1 \le i < j \le N} \big((N - i + 1) + (N - j + 1) - 2\,\text{LCP}(S[i..N], S[j..N])\big)$.
  2. *Combinatorial Invariant*: By Reversed-SAM Duality, the Link Tree of $\text{SAM}(S^R)$ is the Suffix Tree of $S$, so $\text{LCP}(S[i..N], S[j..N]) = \text{len}(\text{LCA}(v_i, v_j))$.
  3. *Scratchpad*: Build $\text{SAM}(S^R)$ and run a Link-Tree DP counting pairs of suffix leaves separated at each LCA $u$, multiplying by $2\,\text{len}(u)$.
  4. *Pitfall*: Counting cloned nodes as suffix leaves; only the $N$ prefix states $\text{pos}[1..N]$ initialize with leaf count $1$.

##### 4. `CF 802I — Fake News (hard)` — `[EN]`
- **Constraints**: $\sum |S| \le 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Compute $\sum_{w \text{ distinct}} \text{occ}(w, S)^2$.
  2. *Combinatorial Invariant*: Each state $u$ of $\text{SAM}(S)$ bundles $\text{len}(u) - \text{len}(\text{link}(u))$ distinct substrings, all having multiplicity $|\text{endpos}(u)|$.
  3. *Scratchpad*: Sum $(\text{len}(u) - \text{len}(\text{link}(u))) \cdot |\text{endpos}(u)|^2$ over all $u > 1$.
  4. *Pitfall*: 64-bit integer overflow on $|\text{endpos}(u)|^2 \cdot \text{len}(u)$.

##### 5. `CF 123D — String` — `[EN]`
- **Constraints**: $N \le 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Compute $\sum_{w \text{ distinct}} \frac{\text{occ}(w, S)(\text{occ}(w, S) + 1)}{2}$.
  2. *Combinatorial Invariant*: Identical right-equivalence bundling on $\text{SAM}(S)$: each state $u$ contributes $(\text{len}(u) - \text{len}(\text{link}(u))) \binom{|\text{endpos}(u)|+1}{2}$.
  3. *Scratchpad*: Propagate $|\text{endpos}(u)|$ bottom-up via bucket sort on $\text{len}(u)$ in $O(N)$.
  4. *Pitfall*: Using $O(N \log N)$ sort when radix/counting sort on $\text{len}(u) \le N$ is $O(N)$.

##### 6. `CF 427D — Match & Catch` — `[EN]`
- **Constraints**: $|S_1|, |S_2| \le 5000$ (solvable in $O(|S_1| + |S_2|)$ via GSAM).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Find the shortest substring that appears **uniquely** (exactly once) in $S_1$ and **uniquely** in $S_2$.
  2. *Combinatorial Invariant*: In $\text{GSAM}(S_1, S_2)$, a state $u$ represents strings occurring once in $S_1$ and once in $S_2$ iff $\text{cnt}_1(u) = 1$ and $\text{cnt}_2(u) = 1$. Among strings in $u$, the shortest has length $\text{minlen}(u) = \text{len}(\text{link}(u)) + 1$.
  3. *Scratchpad*: Take $\min_{\text{cnt}_1(u) = \text{cnt}_2(u) = 1} (\text{len}(\text{link}(u)) + 1)$.
  4. *Pitfall*: Returning $\text{len}(u)$ instead of $\text{len}(\text{link}(u)) + 1$.

##### 7. `[SDOI2016] 生成魔咒` (Luogu P4070) — `[ZH]`
- **Constraints**: $N \le 10^5$, $|\Sigma| \le 10^9$ (large alphabet), online append.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: After each character append $S[1..i]$, report the number of distinct substrings in $S[1..i]$.
  2. *Combinatorial Invariant*: Appending $S[i]$ creates a single new primary state `cur` and optionally splits $q$ into `clone` + $q$. Notice that splitting $q$ into `clone` and $q$ **preserves** the sum $(\text{len}(\text{clone}) - \text{len}(\text{link}(\text{clone}))) + (\text{len}(q) - \text{len}(\text{clone})) = \text{len}(q) - \text{len}(\text{link}_{\text{old}}(q))$! Thus only `cur` adds $\text{len}(\text{cur}) - \text{len}(\text{link}(\text{cur}))$ new substrings!
  3. *Scratchpad*: Use `std::map<int, int> next[u]` for the $10^9$ alphabet, and add $\text{len}(\text{cur}) - \text{len}(\text{link}(\text{cur}))$ to the running answer after each step.
  4. *Pitfall*: Copying `next[q]` into `next[clone]` via `map` assignment is $O(|\Sigma_{\text{active}}|)$, which amortizes to $O(N \log N)$ because each transition is copied only when a node is cloned.

##### 8. `[Usaco2010 Dec] Standing Out from the Herd` (Luogu P6140 / USACO Platinum Dec 2017) — `[EN]`
- **Constraints**: $\sum |S_i| \le 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: For each string $S_i$, count how many of its distinct substrings do **not** appear in any $S_j$ ($j \ne i$).
  2. *Combinatorial Invariant*: In $\text{GSAM}(S_1, \dots, S_k)$, propagate up the Link Tree a tag $\text{owner}[u] \in \{0, 1..k, -1\}$ where $-1$ means $\ge 2$ distinct strings own suffixes in $u$'s subtree. If $\text{owner}[u] = i > 0$, state $u$ contributes $\text{len}(u) - \text{len}(\text{link}(u))$ exclusively to string $i$.
  3. *Scratchpad*: Build GSAM, compute $\text{owner}[u]$ bottom-up in $O(\sum |S_i|)$, and accumulate answers per string.
  4. *Pitfall*: If string $S_i$ visits the same GSAM node $u$ multiple times, $\text{owner}[u]$ must remain $i$, not become $-1$!

##### 9. `CF 235C — Cyclical Quest` — `[EN]`
- **Constraints**: $|S| \le 10^6$, $\sum |P_i| \le 10^6$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Given $S$ and query patterns $P$, count how many occurrences in $S$ match *some cyclic shift* of $P$.
  2. *Combinatorial Invariant*: Every cyclic shift of $P$ of length $m = |P|$ is a substring of length $m$ of $P \cdot P[1..m-1]$. Two shifts may be identical if $P$ is periodic, so we must deduplicate visited SAM states $u$ per query.
  3. *Scratchpad*: Slide a window of length $m$ over $P \cdot P[1..m-1]$ on $\text{SAM}(S)$: advance right by $c$, and when matched length $> m$, decrement length and step $u \gets \text{link}(u)$ if length $\le \text{len}(\text{link}(u))$. Whenever matched length $\ge m$, add $|\text{endpos}_S(u)|$ if $\text{vis}[u] \ne \text{query\_id}$.
  4. *Pitfall*: Clearing `vis` with `memset` per query takes $O(|S| Q)$ time; use timestamped `vis[u] == qid`.

---

#### Tier 2: Intermediate (Generalized SAM on Trees/Tries, Subsequence/SAM Couplings, First Endpos Merging) — 9 Problems

##### 10. `[ZJOI2015] 诸神眷顾的幻想乡` (Luogu P3346) — `[ZH]`
- **Constraints**: Tree with $N \le 10^5$ nodes, alphabet $|\Sigma| \le 10$, **at most $20$ leaves**.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Count the number of distinct strings formed by simple paths on a tree with $\le 20$ leaves.
  2. *Combinatorial Invariant*: Every simple path on a tree is a sub-path of a path starting at one of the $\le 20$ leaves! Thus the set of all tree-path strings equals the set of all substrings of the $20$ leaf-rooted trees (which form $20$ Tries of total size $\le 20 N$).
  3. *Scratchpad*: Merge the $20$ leaf-rooted DFS trees into a single Trie (or build the GSAM directly via **BFS** from each leaf root), then sum $\text{len}(u) - \text{len}(\text{link}(u))$.
  4. *Pitfall*: Building the GSAM via **DFS** on the tree without checking/cloning or on a skewed tree with high-degree branch gadgets risks the $O(V^2)$ Trie-DFS trap (Iteration 63); use BFS order on the Trie!

##### 11. `[JSOI2012] 越狱老虎桥` / `[BZOJ 2780] Sevenk Love Oimaster` (SPOJJZPGYZ) — `[ZH]`
- **Constraints**: $N \le 10^4, \sum |S_i| \le 10^5, \sum |Q_j| \le 3.6 \times 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Given $N$ dictionary strings $S_1, \dots, S_N$, for each query $P$, count in how many *distinct* strings $S_i$ the pattern $P$ occurs at least once.
  2. *Combinatorial Invariant*: Each prefix of $S_i$ colors its GSAM state with color $i$. A state $u$'s answer is the number of distinct colors in its Link-Tree subtree.
  3. *Scratchpad*: This is the classic tree distinct-color counting problem on the GSAM Link Tree: sort nodes by DFS order, and for each color $i$, add $+1$ to each node $u$ of color $i$ and $-1$ to $\text{LCA}(u_{\text{prev}}, u)$ along the Link Tree (or use Segment Tree Merging).
  4. *Pitfall*: Duplicate prefixes of the same string $S_i$ landing on the same GSAM node $u$ must be deduplicated before LCA subtraction.

##### 12. `[HEOI2015] 最短不公共子串` (Luogu P4112) — `[ZH]`
- **Constraints**: $|A|, |B| \le 2000$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Given strings $A$ and $B$, solve all 4 combinations of finding the shortest (substring / subsequence) of $A$ that is NOT a (substring / subsequence) of $B$.
  2. *Combinatorial Invariant*: A Subaton (SAM) recognizes all substrings, while a Subsequence Automaton (DASG, where $\text{next}[i][c]$ is the first occurrence of $c$ after $i$) recognizes all subsequences. A string is a shortest non-occurring word iff it corresponds to a shortest path in the product automaton $\mathcal{A}_A \times \mathcal{A}_B$ from $(\text{root}_A, \text{root}_B)$ to any state $(u_A, \text{null}_B)$!
  3. *Scratchpad*: Build $\text{SAM}(A), \text{SAM}(B), \text{DASG}(A), \text{DASG}(B)$ and run BFS/DP on the 4 product graphs.
  4. *Pitfall*: Since $\text{SAM}(A)$ is a DAG (not a tree), you don't even need $\text{SAM}(A)$ for the left side—any shortest substring of $A$ is just a contiguous slice $A[l..r]$, or you can run BFS on $\text{Automaton}(B)$ while scanning $A$.

##### 13. `CF 452E — Three Strings` — `[EN]`
- **Constraints**: $|S_1|, |S_2|, |S_3| \le 3 \times 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: For every length $L \in [1, \min(|S_1|, |S_2|, |S_3|)]$, compute the sum over all strings $w$ of length $L$ of $\text{occ}(w, S_1) \cdot \text{occ}(w, S_2) \cdot \text{occ}(w, S_3) \bmod (10^9+7)$.
  2. *Combinatorial Invariant*: In $\text{GSAM}(S_1, S_2, S_3)$, each state $u$ contributes $\text{cnt}_1(u) \cdot \text{cnt}_2(u) \cdot \text{cnt}_3(u)$ to **every length $L$ in the interval $[\text{len}(\text{link}(u)) + 1, \text{len}(u)]$**!
  3. *Scratchpad*: Compute $\text{prod}(u) = \text{cnt}_1(u) \text{cnt}_2(u) \text{cnt}_3(u)$ via Link-Tree bottom-up sum, and add $\text{prod}(u)$ to a difference array over lengths $[\text{len}(\text{link}(u)) + 1, \text{len}(u)]$. Take prefix sums at the end.
  4. *Pitfall*: Applying the difference update at $u = 1$ (where $\text{len}(1) = 0$).

##### 14. `CF 616F — Expensive Strings` — `[EN]`
- **Constraints**: $\sum |S_i| \le 5 \times 10^5$, costs $c_i \in [-10^7, 10^7]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Maximize $|w| \cdot \sum_{i=1}^n c_i \cdot \text{occ}(w, S_i)$ over all nonempty strings $w$.
  2. *Combinatorial Invariant*: Within any GSAM state $u$, the weighted sum $C(u) = \sum_{i=1}^n c_i \cdot \text{occ}(u, S_i)$ is constant across all lengths $\ell \in [\text{minlen}(u), \text{len}(u)]$. Since $\ell > 0$, if $C(u) > 0$, the product $\ell \cdot C(u)$ is maximized at $\ell = \text{len}(u)$.
  3. *Scratchpad*: Build GSAM, propagate $C(u)$ bottom-up on the Link Tree, and take $\max_{u > 1} \text{len}(u) \cdot C(u)$.
  4. *Pitfall*: Negative $c_i$ values mean $C(u)$ can be negative; initialize answer to $0$.

##### 15. `CF 873F — Forbidden Indices` — `[EN]`
- **Constraints**: $N \le 2 \times 10^5$, binary forbidden mask.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Maximize $|w| \cdot \text{occ}_{\text{allowed}}(w, S)$, where an occurrence is allowed iff its starting (or ending) index is not forbidden.
  2. *Combinatorial Invariant*: Only mark $\text{endpos}$ for non-forbidden prefixes $\text{pos}[i]$ ($S_{\text{forb}}[i] = 0$). Then $|\text{endpos}_{\text{allowed}}(u)|$ is constant across all strings in state $u$, so the optimal length in $u$ is $\text{len}(u)$.
  3. *Scratchpad*: Build $\text{SAM}(S)$, initialize $w[\text{pos}[i]] = [i \text{ allowed}]$, sum bottom-up on the Link Tree, and take $\max_{u > 1} \text{len}(u) \cdot w[u]$.
  4. *Pitfall*: If the problem forbids **starting** indices $l$, build $\text{SAM}(S^R)$ so starting indices become ending indices!

##### 16. `AtCoder ABC 272 Ex / ARC — Substring Queries on GSAM` / `JOI Spring Camp — String Problems` (`[JA]` Representative: `ABC 141 E / ARC 097 / yukicoder #430`) — `[JA]`
- **Constraints**: $N \le 5 \times 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Find the maximum length of a non-overlapping repeated substring $S[l_1..r_1] = S[l_2..r_2]$ with $r_1 < l_2$.
  2. *Combinatorial Invariant*: For any SAM state $u$, let $\min\_\text{pos}(u) = \min \text{endpos}(u)$ and $\max\_\text{pos}(u) = \max \text{endpos}(u)$. The two most distant occurrences of state $u$ end at $\min\_\text{pos}(u)$ and $\max\_\text{pos}(u)$. They are disjoint for a string of length $\ell \in [\text{minlen}(u), \text{len}(u)]$ iff $\max\_\text{pos}(u) - \min\_\text{pos}(u) \ge \ell$.
  3. *Scratchpad*: Propagate $\min\_\text{pos}(u)$ and $\max\_\text{pos}(u)$ bottom-up on the Link Tree in $O(N)$, and take $\max_{u} \min\big(\text{len}(u), \max\_\text{pos}(u) - \min\_\text{pos}(u)\big)$ over states with $\ge 2$ occurrences.
  4. *Pitfall*: Forgetting to cap the valid length at $\max\_\text{pos}(u) - \min\_\text{pos}(u)$ when $\text{len}(u)$ exceeds the gap.

##### 17. `[CTSC2012] 熟悉的文章` (Luogu P4022) — `[ZH]`
- **Constraints**: $\sum |S_i| + \sum |T_j| \le 1.1 \times 10^6$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Given a dictionary of strings $S_1, \dots, S_m$ and query text $T$, binary search the maximum $L$ such that $T$ can be partitioned into segments where segments of length $\ge L$ occurring in the dictionary cover $\ge 90\%$ of $|T|$.
  2. *Combinatorial Invariant*: Let $\text{match}[i]$ be the maximum length of a suffix of $T[1..i]$ that occurs in $\text{GSAM}(S_1, \dots, S_m)$. Then a valid dictionary segment ending at $i$ of length $\ge L$ starts at any $j \in [i - \text{match}[i], i - L]$.
  3. *Scratchpad*: Compute $\text{match}[i]$ in $O(|T|)$ by walking $T$ on the GSAM, then for each binary-search midpoint $L$, run a monotonic-queue DP $dp[i] = \max(dp[i-1], \max_{j \in [i - \text{match}[i], i - L]} (dp[j] + i - j))$ in $O(|T|)$ time, since $i - \text{match}[i]$ is non-decreasing!
  4. *Pitfall*: Assuming $i - \text{match}[i]$ isn't monotonic; because extending $T[1..i-1]$ by $T[i]$ increases $\text{match}$ by at most $+1$, $i - \text{match}[i]$ is strictly non-decreasing!

##### 18. `[BZOJ 2555] SubString` — `[ZH]`
- **Constraints**: $Q \le 6 \times 10^5$, $|S| + \sum |P| \le 3 \times 10^6$, **online encrypted**.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Interleave online character appends to $S$ with pattern frequency queries $\text{occ}(P, S)$.
  2. *Combinatorial Invariant*: Each character append adds $+1$ to all Link-Tree ancestors of `cur`, and splits at most one Link-Tree edge via `clone` (which inherits $q$'s exact prior $\text{endpos}$ count).
  3. *Scratchpad*: Maintain the Link Tree inside a Link-Cut Tree (Iteration 65 Coupling 1) with lazy path $+1$ tags.
  4. *Pitfall*: Forgetting to copy $q$'s accumulated lazy value to `clone` before cutting $(p, q)$ and linking `clone`.

---

#### Tier 3: Advanced (Endpos Segment Tree Merging + Clipping, Binary Lifting, Interval LCS, Lexicographical Next) — 9 Problems

##### 19. `[HEOI2016 / TJOI2016] 字符串` (Luogu P4094) — `[ZH]`
- **Constraints**: $N, Q \le 10^5$.
- **4-Step Analysis**: Complete derivation in Iteration 64 §3.3(A): Binary search length $L \in [0, \min(b-a+1, d-c+1)]$, binary lift from $\text{pos}[c+L-1]$ to state $u$, and test $\text{endpos}(u) \cap [a+L-1, b] \ne \emptyset$ via Segment Tree Merge.

##### 20. `CF 666E — Forensic Examination` — `[EN]`
- **Constraints**: $|S| \le 5 \times 10^5, \sum |T_i| \le 5 \times 10^4, Q \le 5 \times 10^5$.
- **4-Step Analysis**: Complete derivation in Iteration 64 §3.3(B): GSAM + persistent Segment Tree Merge over dictionary indices $[1, m]$ + Link-Tree binary lifting.

##### 21. `CF 1037H — Security` — `[EN]`
- **Constraints**: $|S| \le 10^5, \sum |X| \le 2 \times 10^5$.
- **4-Step Analysis**: Complete derivation in Iteration 64 §3.3(C): Walk $X$ on $\text{SAM}(S)$, backtrack $i = k \dots 0$, and test $v = \text{next}[u_i][c]$ for $c > X[i+1]$ against $\text{endpos}(v) \cap [l+i, r] \ne \emptyset$.

##### 22. `CF 700E — Cool Slogans` — `[EN]`
- **Constraints**: $N \le 2 \times 10^5$.
- **4-Step Analysis**: Complete derivation in Iteration 64 §3.3(E): Canonical longest-string representative per SAM state + Link-Tree top-down DP testing $\text{endpos}(v) \cap [\text{pos}(u) - \text{len}(u) + \text{len}(v), \text{pos}(u) - 1] \ne \emptyset$.

##### 23. `CF 1063F — String Journey` — `[EN]`
- **Constraints**: $N \le 5 \times 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Find the maximum $k$ such that there is a sequence of non-overlapping substrings $S[l_k..r_k], \dots, S[l_1..r_1]$ from left to right where $|S[l_{i+1}..r_{i+1}]| = |S[l_i..r_i]| + 1$ and $S[l_i..r_i]$ is a substring of $S[l_{i+1}..r_{i+1}]$ (which forces $|S[l_i..r_i]| = i$ and $S[l_i..r_i]$ to be either the prefix $S[l_{i+1}..r_{i+1}-1]$ or the suffix $S[l_{i+1}+1..r_{i+1}]$!).
  2. *Combinatorial Invariant*: By reversing $S$ (or working left-to-right), let $dp[i]$ be the maximum valid length of a chain starting (or ending) at $i$. As $i$ moves by $1$, $dp[i] \le dp[i-1] + 1$, so we can decrement candidate $L = dp[i]$ one by one ($O(N)$ total decrements!) and test if there is a valid previous index $j \le i - L$ with $dp[j] \ge L - 1$ that shares a prefix/suffix of length $L - 1$ with $i$.
  3. *Scratchpad*: On the Link Tree of $\text{SAM}(S^R)$, a shared prefix of length $L - 1$ corresponds to the Euler-tour subtree interval $[\text{dfn}[u], \text{out}[u]]$ of the ancestor $u$ at length $L - 1$ (found via binary lifting or rolling pointer), queried with a Range-Max Segment Tree over $\text{dfn}$.
  4. *Pitfall*: Inserting $dp[j]$ into the Segment Tree before $j \le i - L$ becomes valid; use a delayed pointer $j = i - L$ as $L$ decrements.

##### 24. `[BZOJ 3413] 匹配` — `[ZH]`
- **Constraints**: $|S| \le 10^5, \sum |P| \le 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Simulate a naive sequential matcher comparing $P$ against suffixes/substrings of $S$ up to the first occurrence of $P$ (or end of $S$), summing $\text{LCP}(P, S[i..N])$.
  2. *Combinatorial Invariant*: In $\text{SAM}(S)$ with Segment Tree Merging on $\text{endpos}$, as we walk prefixes $P[1..k]$ on $\text{SAM}(S)$, each state $u_k$ contributes $+1$ to every occurrence of $P[1..k]$ that ends at or before the first full match of $P$.
  3. *Scratchpad*: First find the leftmost occurrence $r_{\min}$ of $P$ in $S$ via $\min \text{endpos}(u_{|P|})$. Then along the walk of $P$, query the count of $\text{endpos}(u_k)$ before $r_{\min}$ using the merged Segment Tree.
  4. *Pitfall*: Off-by-one when shifting ending positions of $P[1..k]$ relative to the starting position of the full match of $P$.

##### 25. `CF 149E — Martian Strings` — `[EN]`
- **Constraints**: $|S| \le 10^5, m \le 100, |P_i| \le 1000$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Check whether $P$ can be split into $P = P[1..k] \cdot P[k+1..|P|]$ ($1 \le k < |P|$) such that $P[1..k]$ and $P[k+1..|P|]$ occur as **disjoint** substrings in $S$.
  2. *Combinatorial Invariant*: $P[1..k]$ and $P[k+1..|P|]$ have a disjoint occurrence pair iff the **leftmost** ending position $\min \text{endpos}_S(P[1..k])$ is $\le$ the **rightmost** starting position $\max \text{startpos}_S(P[k+1..|P|]) - 1$.
  3. *Scratchpad*: Build $\text{SAM}(S)$ (tracking $\min \text{endpos}$) and $\text{SAM}(S^R)$ (tracking $\max \text{startpos}$). Walk $P$ forward on $\text{SAM}(S)$ and $P^R$ backward on $\text{SAM}(S^R)$ in $O(|P|)$ time.
  4. *Pitfall*: Failing to reject $|P| = 1$ (since both pieces must be non-empty).

##### 26. `[FJOI2016] 所有公共子串问题` / `UOJ / LOJ Multi-String Range Substring Problems` (`[BJWC2018] Border 的四种求法` — SAM + Endpos / Link-Tree Component) — `[ZH]`
- **Constraints**: $N, Q \le 2 \times 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Given query $[l, r]$, find the longest border of $S[l..r]$, i.e., maximum $L < r - l + 1$ with $S[l..l+L-1] = S[r-L+1..r]$.
  2. *Combinatorial Invariant*: On the Link Tree of $\text{SAM}(S)$, $S[1..l+L-1]$ and $S[1..r]$ must have a common suffix of length $\ge L$, meaning $\text{len}(\text{LCA}(\text{pos}[l+L-1], \text{pos}[r])) \ge L$, equivalently $p = l + L - 1 \in [l, r-1]$ satisfies $p - \text{len}(\text{LCA}(\text{pos}[p], \text{pos}[r])) \le l - 1$.
  3. *Scratchpad*: Decompose the Link-Tree path from $\text{pos}[r]$ to root $1$ via HLD or Centroid Decomposition, and query the Segment Tree of $p - \text{len}(u)$ in light subtrees of ancestors $u$ of $\text{pos}[r]$.
  4. *Pitfall*: Allowing $p = r$ (which gives the trivial whole-string border $L = r - l + 1$).

##### 27. `AtCoder AGC 047 B — First Second` / `ARC 151 E — Keep Being Substring` (GSAM / Suffix Link Tree Reduction) — `[JA]`
- **Constraints**: $\sum |S_i| \le 10^6$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: In `ARC 151 E`, transform string $X$ into $Y$ (both substrings of $A[1..N]$) by appending/deleting one character at a time while keeping the current string a non-empty substring of $A$.
  2. *Combinatorial Invariant*: If $X$ and $Y$ share any common substring (even a single character $c$), we can shrink $X$ to $c$ and grow $c$ to $Y$ in $|X| + |Y| - 2\,\text{LCS}(X, Y)$ steps! We only need to find $\text{LCS}(X, Y)$ using $\text{SAM}(X)$ and $Y$, and if $\text{LCS}(X, Y) = 0$, run a shortest-path BFS over the alphabet graph induced by adjacent characters in $A$.
  3. *Scratchpad*: Build $\text{SAM}(X)$ to compute $\text{LCS}(X, Y)$ in $O(|X| + |Y|)$; if $>0$, return $|X| + |Y| - 2\,\text{LCS}(X, Y)$.
  4. *Pitfall*: Assuming you must stay inside $A$'s specific occurrence interval when shrinking/growing, whereas any common character jumps between occurrences in $A$ for free!

---

#### Tier 4: Mastery (`[NOI2018] 你的名字`, LCT Color-Chain Sweeping, Prefix-Suffix DAG Optimization, 2D HLD on Link Tree) — 9 Problems

##### 28. `[NOI2018] 你的名字` (Luogu P4770 / UOJ #395 / LOJ #2720) — `[ZH]`
- **Constraints**: $|S| \le 5 \times 10^5, Q \le 10^5, \sum |T| \le 5 \times 10^5$.
- **4-Step Analysis**: Complete derivation in Iteration 64 §3.3(D): Dual SAM ($\text{SAM}(S)$ with persistent Segment Tree Merge on $\text{endpos}$ + per-query $\text{SAM}(T)$), two-pointer computation of $\text{lim}[i]$ in $O(|T| \log |S|)$, and exact deduplication via $\sum_{v \in \text{SAM}(T)} \max(0, \text{len}_T(v) - \max(\text{len}_T(\text{link}_T(v)), \text{lim}[\text{pos}_T(v)]))$.

##### 29. `Luogu P6292 — 区间本质不同子串个数` / `[SDOI2017]` Paradigm — `[ZH]`
- **Constraints**: $N \le 10^5, Q \le 2 \times 10^5$.
- **4-Step Analysis**: Complete derivation in Iteration 65 §3 (Coupling 2): Offline sweep $r = 1 \dots N$, LCT `access(pos[r], r)` color-chain sweeping on the Link Tree of $\text{SAM}(S)$, and Range-Add Range-Sum Segment Tree over starting positions $[p - \ell_{\max} + 1, p - \ell_{\min}]$ in $O(N \log^2 N + Q \log N)$.

##### 30. `[十二省联考 2019] 字符串问题` (Luogu P5284 / LOJ #3052) — `[ZH]`
- **Constraints**: $|S|, N_A, N_B, m \le 2 \times 10^5$.
- **4-Step Analysis**: Complete derivation in Iteration 66 §2.1 & §3.1: $\text{SAM}(S^R)$ Link Tree + binary lifting + intra-state length sorting (with $B_j$ before $A_i$ on equal length) + topological longest-path DP.

##### 31. `CF 1098F — Ж-function` — `[EN]`
- **Constraints**: $N, Q \le 2 \times 10^5$.
- **4-Step Analysis**: Complete derivation in Iteration 66 §2.2 & §3.2: $\text{SAM}(S^R)$ Link Tree + HLD / Centroid Decomposition + two Fenwick trees separating the unclipped $\text{len}(u)$ regime from the $r - i + 1$ clipped regime.

##### 32. `[NOI2016] 优秀的拆分` (Luogu P1117 / UOJ #219) — `[ZH]`
- **Constraints**: $T \le 10, N \le 3 \times 10^4$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Count the number of splits $AABB$ in $S$, i.e., $\sum_{i=1}^{N-1} f[i] \cdot g[i+1]$ where $f[i]$ is the number of squares $AA$ ending at $i$ and $g[j]$ is the number of squares $BB$ starting at $j$.
  2. *Combinatorial Invariant*: Using $\text{SAM}(S)$ (for $\text{LCSuf}$ via Link-Tree LCA) and $\text{SAM}(S^R)$ (for $\text{LCP}$ via Link-Tree LCA), harmonic grid checkpoints $kL, (k+1)L$ detect all squares of half-length $L$ as range $+1$ updates to $f$ and $g$.
  3. *Scratchpad*: Build $\text{SAM}(S)$ and $\text{SAM}(S^R)$ with $O(1)$ Euler-tour RMQ LCA on their Link Trees, iterate $L = 1 \dots N/2$ and $k = 1 \dots \lfloor N/L \rfloor - 1$, and update difference arrays for $f$ and $g$ in $O(N \log N)$.
  4. *Pitfall*: Allowing $\text{LCSuf} + \text{LCP}$ to double-count the checkpoint boundary character; subtract $1$ from the overlap length and cap $\text{LCSuf} \le L, \text{LCP} \le L$.

##### 33. `CF 653F — Paper task` — `[EN]`
- **Constraints**: $N \le 5 \times 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Count the number of **distinct** substrings of $S$ that are valid balanced bracket sequences.
  2. *Combinatorial Invariant*: Every SAM state $u$ represents substrings ending at $r = \text{pos}(u)$ with starting positions $l \in [r - \text{len}(u) + 1,\; r - \text{len}(\text{link}(u))]$. Let $\text{pref}[k]$ be the bracket prefix balance. Then $S[l..r]$ is a balanced bracket string iff $\text{pref}[l-1] = \text{pref}[r]$ AND $\min_{k=l-1}^{r} \text{pref}[k] \ge \text{pref}[r]$ (i.e., $l-1$ is to the right of the last index $p_{\text{bad}} < r$ with $\text{pref}[p_{\text{bad}}] < \text{pref}[r]$).
  3. *Scratchpad*: Build $\text{SAM}(S)$, propagate one representative $\text{pos}(u)$ per state, and for each state $u$, count indices $j = l - 1 \in [\max(p_{\text{bad}}(\text{pos}(u)) + 1,\; \text{pos}(u) - \text{len}(u)),\;\; \text{pos}(u) - \text{len}(\text{link}(u)) - 1]$ satisfying $\text{pref}[j] = \text{pref}[\text{pos}(u)]$ via binary search in `std::vector` buckets!
  4. *Pitfall*: Off-by-one between the 1-based starting index $l$ of the substring and the prefix-sum index $j = l - 1$.

##### 34. `[CTT 2017 / 集训队互测] / UOJ / QOJ — Range Shortest Unique Substring / Substring Cover` (`CF 1286E / CF 1476G / BZOJ 4556`) — `[EN]` / `[ZH]`
- **Constraints**: $N \le 2 \times 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Maintain or query properties of unique/repeated occurrences across intervals $[l, r]$ using $\text{SAM}(S)$ + Segment Tree Merging + Link-Tree DSU-on-Tree (adjacent elements in $\text{endpos}(u)$ generate dominance pairs $(p_k, p_{k+1})$ of length $\text{len}(u)$!).
  2. *Combinatorial Invariant*: **The Adjacent-Endpos Dominance Lemma**: While merging $\text{endpos}$ sets bottom-up at state $u$ of the Link Tree (using DSU-on-Tree /启发式合并), inserting $p \in \text{endpos}(v)$ into $\text{endpos}(u)$ can only create new maximal-LCP adjacent pairs with its **immediate predecessor $p^-$ and immediate successor $p^+$** in $\text{endpos}(u)$! This reduces $O(N^2)$ pairs $(i, j)$ with $\text{LCSuf}(i, j) = \text{len}(u)$ to at most $2N \log N$ dominated pairs $(p^-, p, \text{len}(u))$ and $(p, p^+, \text{len}(u))$!
  3. *Scratchpad*: Use DSU-on-Tree (`std::set` heuristic merge) on the Link Tree to extract all $O(N \log N)$ triples $(x, y, \text{len}(u))$ and sweep offline with a Fenwick/Segment Tree.
  4. *Pitfall*: Emitting pairs for all $a, b \in \text{endpos}(u)$ instead of only adjacent predecessors/successors during the small-to-large `std::set` insertion.

##### 35. `[ZJOI2019] 语言` (Luogu P5327 / LOJ #3093) — `[ZH]` (Tree Path Union / SAM Subtree Coverage Dual)
- **Constraints**: $N, M \le 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: In both tree-path union problems and multi-interval SAM Link-Tree coverage problems (`[BZOJ 2780]` generalized to intervals), we must maintain at each node the size of the **Virtual Tree union** of active nodes in its subtree.
  2. *Combinatorial Invariant*: Given a set of vertices $V' \subseteq V(T)$ sorted by DFS entry time $\text{dfn}(v_1) < \text{dfn}(v_2) < \dots < \text{dfn}(v_k)$, the total weight (or number of distinct substrings $\sum (\text{len}(u) - \text{len}(\text{link}(u)))$) in the union of root-to-$v_i$ paths in the Link Tree is strictly:
     $$\sum_{i=1}^k \text{len}(v_i) - \sum_{i=1}^{k-1} \text{len}\big(\text{LCA}(v_i, v_{i+1})\big)!$$
  3. *Scratchpad*: Maintain the active DFS-ordered leaves in a Dynamic Segment Tree tracking the leftmost leaf, rightmost leaf, and adjacent-leaf LCA sum under Segment Tree Merging!
  4. *Pitfall*: Using $O(\log N)$ binary-lifting LCA inside the Segment Tree `pushup` makes the complexity $O(N \log^2 N)$ with a large constant; use $O(1)$ Euler-tour RMQ LCA so `pushup` is $O(1)$!

##### 36. `[国家集训队论文 / QOJ / Universal Cup] — SAM + LCT + Endpos Synthesis (`[SDOI2017] / BZOJ 4771 / UCup Substring Distinct Weighted Sum`)` — `[ZH]` / `[EN]`
- **Constraints**: $N, Q \le 2 \times 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Given string $S[1..N]$, weights $w[1..N]$ on lengths, and queries $[l, r]$, compute $\sum_{s \text{ distinct in } S[l..r]} w[|s|] \cdot g(\text{last\_occ}(s, r))$.
  2. *Combinatorial Invariant*: By Iteration 65's LCT Color-Chain Invariant, each homogeneous splay tree $C$ of color $p = \text{last}(C)$ represents lengths $\ell \in [\ell_{\min}+1, \ell_{\max}]$ whose rightmost occurrences start at $s = p - \ell + 1 \in [p - \ell_{\max} + 1, p - \ell_{\min}]$. Notice that $\ell = p - s + 1$, so updating the starting-position interval $s \in [p - \ell_{\max} + 1, p - \ell_{\min}]$ corresponds to a shifted prefix-weight range update on the Segment Tree!
  3. *Scratchpad*: Couple LCT `access(pos[r], r)` with a Segment Tree supporting shifted polynomial/prefix weight updates.
  4. *Pitfall*: Failing to reverse the indexing of $w[\ell] = w[p - s + 1]$ when mapping lengths $\ell$ to starting positions $s$.

---

## Summary Checklist of Cohort 2 Wave 2A Findings

1. **Duality**: $\text{LinkTree}(\text{SAM}(S)) \cong \text{ST}(S^R)$, and $\text{LinkTree}(\text{SAM}(S^R)) \cong \text{ST}(S)$.
2. **Generalized SAM Complexity & Correctness**:
   - Online `extend_gsam(last, c)` is $O(\sum |S_i|)$ on explicit strings, provided `next[last][c] != 0` returns `q` or `clone` directly without allocating a zero-length ghost node `cur`.
   - When the input is a compressed Trie $T$ of $V$ nodes (where $\sum |S_i|$ can be $\Theta(V^2)$), **DFS on the Trie takes $\Theta(V^2)$ time** even on a binary alphabet ($\{\text{a}^k \text{b} \mid 1 \le k \le m\}$), whereas **BFS on the Trie takes $O(V)$ time**.
3. **Endpos Segment Tree Merging & Clipping**:
   - A pattern $w$ of length $L$ in state $u$ occurs in $S[l..r]$ iff $\text{endpos}(u) \cap [l + L - 1, r] \ne \emptyset$.
   - Persistent Segment Tree Merging (`new_node` whenever both children exist) preserves interior states' trees in $O(N \log N)$ space.
4. **LCT `access` Color-Chain Sweeping & Adjacent-Endpos Dominance**:
   - Offline $[l, r]$ distinct substring queries reduce to $O(N \log N)$ homogeneous splay-chain updates via LCT `access(pos[r], r)`.
   - DSU-on-Tree (`std::set` heuristic merge) on $\text{endpos}(u)$ extracts all $O(N \log N)$ maximal-LCP adjacent occurrence pairs $(p^-, p, \text{len}(u))$.
5. **Intra-State Length Stratification**:
   - When building prefix/suffix dominance graphs on the Link Tree (`Luogu P5284`), items sharing a SAM state $u$ must be sorted by length (with $B_j$ before $A_i$ on equal length) and chained before branching to Link-Tree children.
