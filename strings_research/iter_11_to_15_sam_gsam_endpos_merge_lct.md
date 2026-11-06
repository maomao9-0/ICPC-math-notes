# Wave 2A (Cohort 1: Iterations 11–15) — Advanced Suffix Automaton (SAM), Generalized SAM (`广义 SAM`), Endpos Segment Tree Merging & LCT/HLD Coupling

> **Cohort 1 Primary Research Report**
> **Scope**: Iterations 11–15 (`Wave 2A`) of the Advanced Stringology Research Corpus (`strings_research/`).
> **Prerequisite Boundary**: Assumes fluency in standard single-string Suffix Automaton (SAM) construction ($O(N)$ Blumer–Blumer–Haussler–Ehrenfeucht–Chen–Seiferas incremental algorithm), Suffix Arrays (`SA`, `rk`, `height`), Segment Trees, Heavy-Light Decomposition (HLD), and Link-Cut Trees (LCT). Standard single-string SAM construction templates are omitted per `AGENTS.md`; all derivations follow the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**.

---

## Iteration 11: Structural Anatomy of SAM, Reversed Suffix Tree Duality & Generalized SAM (`广义 SAM`)

### 11.1 The 4-Step Zero-Magic Analysis of SAM & GSAM Structural Duality

#### Step 1: The Diagnostic Signal (Why Black-Box Whole-String SAM Fails on Multi-String & Suffix-LCP Tasks)
A standard Suffix Automaton $\text{SAM}(S)$ is often introduced purely as the minimal Deterministic Finite Automaton (DFA) accepting all suffixes of a single string $S[1..N]$. Two immediate breakdowns occur when problem setters push beyond single-string whole-text queries:
1. **Prefix/Suffix Asymmetry**: A single-string SAM compresses substrings that share the same set of **right endpoints** ($\text{endpos}$), which means moving up the suffix-link tree (`link`) strips characters from the **left** (shortening a substring into its longest proper suffix with a strictly larger $\text{endpos}$ set). Consequently, the LCA of two prefix states $\text{pos}[i]$ and $\text{pos}[j]$ on the Link Tree of $\text{SAM}(S)$ gives the **Longest Common Suffix (`LCSuf`)** of $S[1..i]$ and $S[1..j]$—*not* the Longest Common Prefix (`LCP`) of two suffixes $S[i..N]$ and $S[j..N]$!
2. **Multi-String Explosion & Online Corruption**: When a problem gives a family of strings $\mathcal{S} = \{S_1, S_2, \dots, S_k\}$ with $\sum |S_i| = N$ (or an explicit Trie $\mathcal{T}$ of $N$ nodes), concatenating them with distinct sentinels $S_1 \#_1 S_2 \#_2 \dots S_k$ blows up the alphabet size to $|\Sigma| + k$, forces transition tables to use hash maps or $O(N \log(|\Sigma|+k))$ balanced trees, and creates $O(N)$ cross-sentinel garbage states. Conversely, attempting to reuse a single-string SAM by simply resetting `last = 1` (the root) at the beginning of each $S_i$ without handling **already-existing transitions** creates **zero-length clone states** ($\text{len}(q) = \text{len}(\text{link}(q))$), corrupting both the DAG transition structure and the Link Tree.

#### Step 2: The Combinatorial Word Invariant (Right-Context Equivalence & Suffix Tree Duality)

Let $S = s_1 s_2 \dots s_N \in \Sigma^N$. For any nonempty substring $w$ of $S$, define its **right-endpoint occurrence set** (`endpos` class):
$$\text{endpos}_S(w) = \{ r \in \{1, \dots, N\} \mid S[r - |w| + 1 .. r] = w \}.$$
Two substrings $u, v$ are $\text{endpos}$-equivalent ($u \equiv_S v$) if $\text{endpos}_S(u) = \text{endpos}_S(v)$. Every state $x \in \text{SAM}(S)$ corresponds bijectively to an equivalence class $E(x)$ under $\equiv_S$.

##### Lemma 11.1 (The Fundamental Endpos Nesting & Interval Partition Invariant)
1. **Suffix Alignment**: If $|u| \le |v|$ and $\text{endpos}_S(u) \cap \text{endpos}_S(v) \ne \emptyset$, then $u$ is a suffix of $v$, and therefore $\text{endpos}_S(v) \subseteq \text{endpos}_S(u)$. In particular, any two $\text{endpos}$ sets are either **disjoint** or **nested**:
   $$\text{endpos}_S(u) \cap \text{endpos}_S(v) \ne \emptyset \implies \text{endpos}_S(u) \subseteq \text{endpos}_S(v) \text{ or } \text{endpos}_S(v) \subseteq \text{endpos}_S(u).$$
2. **Contiguous Suffix Interval per State**: For every state $x \in \text{SAM}(S)$, let $\text{longest}(x)$ be the longest string in $E(x)$ with length $\text{len}(x) = |\text{longest}(x)|$, and let $\text{shortest}(x)$ be the shortest string in $E(x)$ with length $\text{minlen}(x) = |\text{shortest}(x)|$. Then $E(x)$ consists of **precisely** the suffixes of $\text{longest}(x)$ whose lengths lie in the contiguous integer interval
   $$[\text{minlen}(x), \text{len}(x)] = [\text{len}(\text{link}(x)) + 1, \text{len}(x)].$$
   *Proof*: If $w_1$ is a suffix of $w_2$ and $w_2$ is a suffix of $w_3$ with $\text{endpos}_S(w_1) = \text{endpos}_S(w_3)$, then $\text{endpos}_S(w_3) \subseteq \text{endpos}_S(w_2) \subseteq \text{endpos}_S(w_1) = \text{endpos}_S(w_3)$, forcing $\text{endpos}_S(w_2) = \text{endpos}_S(w_3)$. Since the longest suffix of $\text{longest}(x)$ not in $E(x)$ has a strictly larger $\text{endpos}$ set, that suffix is $\text{longest}(\text{link}(x))$ of length $\text{len}(\text{link}(x))$. $\blacksquare$

##### Theorem 11.2 (Blumer–Crochemore Duality: Link Tree of $\text{SAM}(S) \cong$ Compacted Suffix Tree of $S^R$)
Let $S^R = s_N s_{N-1} \dots s_1$ be the reversal of $S$. Then the Suffix Link Tree $\mathcal{T}_{\text{link}}(\text{SAM}(S))$ is **canonically isomorphic** to the compacted Suffix Tree (Patricia Trie of suffixes) $\text{ST}(S^R)$ of the reversed string $S^R$:
$$\mathcal{T}_{\text{link}}(\text{SAM}(S)) \cong \text{ST}(S^R).$$

*Proof via Explicit Bijection*:
Reverse every substring $w$ of $S$ into $w^R$, which is a substring of $S^R$.
- An occurrence of $w$ ending at position $r$ in $S$ ($S[r-|w|+1..r] = w$) corresponds bijectively to an occurrence of $w^R$ **starting** at position $l' = N - r + 1$ in $S^R$ ($S^R[l' .. l'+|w|-1] = w^R$).
- Extending $w$ on the **left** in $S$ ($c w \leftarrow w$) corresponds to extending $w^R$ on the **right** in $S^R$ ($w^R \to w^R c$).
- In the uncompacted trie of all substrings of $S^R$ (which is the trie of all prefixes of all suffixes of $S^R$), a node $w^R$ is **branching** (or marks the end of a full suffix of $S^R$) if and only if there are at least two distinct right-extensions $w^R c_1, w^R c_2$ (or $w^R$ occurs at the very end of $S^R$, i.e., $1 \in \text{endpos}_S(w)$), which is equivalent to saying that moving from $w^R$ to $w^R c$ strictly shrinks the set of starting positions in $S^R$—i.e., strictly shrinks $\text{endpos}_S(c w) \subsetneq \text{endpos}_S(w)$!
- Compressing non-branching unary paths in the suffix trie of $S^R$ groups together substrings $w^R$ that have the exact same set of starting positions in $S^R$. Under reversal, these are precisely the substrings $w$ with the exact same $\text{endpos}_S(w)$—namely, the states $x \in \text{SAM}(S)$!
- The parent edge from $\text{link}(x)$ to $x$ in $\mathcal{T}_{\text{link}}(\text{SAM}(S))$ represents extending $\text{longest}(\text{link}(x))$ on the left by the substring of length $\text{len}(x) - \text{len}(\text{link}(x))$, which under reversal is the compacted edge label of length $\text{len}(x) - \text{len}(\text{link}(x))$ in $\text{ST}(S^R)$. $\blacksquare$

```
   Duality for S = "abaab" (N = 5)  <===>  S^R = "baaba"

   SAM(S) Link Tree (strips from LEFT)        Compacted Suffix Tree ST(S^R) (extends RIGHT)
   State u : E(u) in S, endpos_S(u)           Node u^R : path spell in S^R, startpos_{S^R}
   ----------------------------------------------------------------------------------------
              [root: eps]                                    [root: eps]
             /     |     \                                  /     |     \
          "a"     "b"   "abaab"                          "a"     "b"   "baaba"
         {1,3,4} {2,5}    {5}                          {2,3,5}  {1,4}    {1}
          / \      |                                     / \      |
       "aa" "ba" "aab"                                "aa" "ab" "baa"
       {4}  {2,5} {5} -> merged into "abaab"          {2}  {1,4} {1} -> merged into "baaba"
```

| Structural Feature in $\text{SAM}(S)$ | Exact Dual Feature in $\text{ST}(S^R)$ | Consequence for Algorithm Design |
| :--- | :--- | :--- |
| State $x \in \text{SAM}(S)$ | Explicit branching/leaf node in $\text{ST}(S^R)$ | Number of SAM states is $\le 2N - 1$ (since a tree with $N$ leaves and binary branching has $\le 2N-1$ nodes). |
| $\text{len}(x) - \text{len}(\text{link}(x))$ | Length of compacted edge $(\text{parent}(x), x)$ in $\text{ST}(S^R)$ | Total distinct substrings of $S$ is $\sum_{x \ne \text{root}} (\text{len}(x) - \text{len}(\text{link}(x)))$. |
| Prefix state $\text{pos}[r]$ of $S[1..r]$ | Terminal node of suffix $S^R[N-r+1..N]$ | $\text{LCSuf}(S[1..i], S[1..j]) = \text{len}(\text{LCA}_{\text{link}}(\text{pos}[i], \text{pos}[j]))$. |
| Link Tree of $\text{SAM}(S^R)$ | Compacted Suffix Tree $\text{ST}(S)$ of $S$ itself! | Building $\text{SAM}(S^R)$ gives the **exact Suffix Tree of $S$** in $O(N)$ time without Ukkonen's algorithm, where $\text{LCP}(S[i..N], S[j..N]) = \text{len}(\text{LCA}(\text{pos}_{S^R}[i], \text{pos}_{S^R}[j]))$. |

#### Step 3: The Reverse-Engineering Scratchpad (Generalized SAM Construction & The 3-Case Extension Contract)

Now suppose we are given a set of strings $\mathcal{S} = \{S_1, \dots, S_k\}$ with total length $N = \sum |S_i|$ (or an explicit Trie $\mathcal{T}$ with $V \le N+1$ vertices). We want a single **Generalized Suffix Automaton (`广义 SAM` / GSAM)** whose DFA accepts all suffixes of all $S_i \in \mathcal{S}$, whose states represent $\equiv_{\mathcal{S}}$ equivalence classes of substrings across the collection, and whose Link Tree has size $\le 2V - 1$.

Why does the naive single-string extension `extend(last, c)` break when we insert a second string (or branch of the Trie) starting from a state $p$?
In a single string $S$, when we append character $c$ at index $r$, the new prefix $S[1..r]$ has length $r$, which is **strictly greater** than the length of every previously seen substring. Hence $\delta(p, c)$ is guaranteed to be $0$ (non-existent) at the starting state $p = \text{last}$.
In a multi-string / Trie setting, however, when we are at state $p$ (representing some prefix $P$ of $S_i$, or a Trie node) and wish to extend by character $c$, the string $Pc$ **may already exist in the automaton** as a substring of an earlier string $S_j$ ($j < i$)! That means the transition $\delta(p, c) = q$ **may already be non-zero** at the very first step!

Let us derive the **exact 3-Case GSAM Extension Function** `extend_gsam(int p, int c)` that returns the state corresponding to $P c$ (where $P = \text{longest}(p)$):

- **Case 1: Transition $\delta(p, c) = 0$ (Standard SAM Case)**
  The string $P c$ has not been seen directly as a transition from $p$.
  1. Create a new state $\text{cur}$ with $\text{len}(\text{cur}) = \text{len}(p) + 1$.
  2. Walk up the suffix link chain from $p$: while $p \ne 0$ and $\delta(p, c) = 0$, set $\delta(p, c) \leftarrow \text{cur}$ and $p \leftarrow \text{link}(p)$.
  3. If $p = 0$, set $\text{link}(\text{cur}) \leftarrow 1$ (the root).
  4. Otherwise, let $q = \delta(p, c)$:
     - **Subcase 1a**: If $\text{len}(q) = \text{len}(p) + 1$, set $\text{link}(\text{cur}) \leftarrow q$.
     - **Subcase 1b**: If $\text{len}(q) > \text{len}(p) + 1$, create a clone state $\text{clone}$ with $\text{len}(\text{clone}) = \text{len}(p) + 1$, copy transitions $\delta(\text{clone}, \cdot) \leftarrow \delta(q, \cdot)$ and $\text{link}(\text{clone}) \leftarrow \text{link}(q)$, redirect $\delta(p', c) \leftarrow \text{clone}$ for all ancestors $p'$ of $p$ with $\delta(p', c) = q$, and set $\text{link}(q) = \text{link}(\text{cur}) = \text{clone}$.
  5. Return $\text{cur}$.

- **Case 2: Transition $\delta(p, c) = q \ne 0$ ALREADY EXISTS and $\text{len}(q) = \text{len}(p) + 1$**
  The state $q$ already has $\text{longest}(q) = P c$. No new substring length or equivalence class split is needed!
  - **Action**: Do **not** allocate any new state. Simply return $q$!

- **Case 3: Transition $\delta(p, c) = q \ne 0$ ALREADY EXISTS and $\text{len}(q) > \text{len}(p) + 1$**
  The string $P c$ already exists inside the equivalence class $E(q)$, but $E(q)$ also contains a longer string $u P c$ ($|u| \ge 1$). Because $P c$ is now being visited as a standalone prefix of the current string (or Trie node), $P c$ gains a new occurrence (or prefix marker) not shared by $u P c$. Thus $E(q)$ must be split at length $\text{len}(p) + 1$!
  - **Action**:
    1. Allocate **only ONE state** $\text{clone}$ (do **not** allocate both `cur` and `clone`!).
    2. Set $\text{len}(\text{clone}) = \text{len}(p) + 1$, copy $\delta(\text{clone}, \cdot) \leftarrow \delta(q, \cdot)$, and set $\text{link}(\text{clone}) \leftarrow \text{link}(q)$.
    3. While $p \ne 0$ and $\delta(p, c) = q$, redirect $\delta(p, c) \leftarrow \text{clone}$ and $p \leftarrow \text{link}(p)$.
    4. Set $\text{link}(q) \leftarrow \text{clone}$.
    5. Return $\text{clone}$ as the new `last` state!

##### Theorem 11.3 (Offline Trie BFS vs. DFS Complexity on Generalized SAM)
Suppose we first insert all strings $S_1, \dots, S_k$ into an explicit Trie $\mathcal{T}$ with $V$ nodes, and then build the GSAM by setting $\text{sam\_node}(\text{root}_{\mathcal{T}}) = 1$ and calling $\text{sam\_node}(v) = \text{extend\_gsam}(\text{sam\_node}(\text{parent}_{\mathcal{T}}(v)), c)$ for each Trie edge $\text{parent}_{\mathcal{T}}(v) \xrightarrow{c} v$.
1. **Why Offline BFS on $\mathcal{T}$ runs in strict $O(V |\Sigma|)$ time (with **Cases 2 and 3** never even triggered at the initial step!)**:
   In BFS order over $\mathcal{T}$, nodes are processed in non-decreasing order of Trie depth $d(v) = \text{len}(\text{sam\_node}(v))$. When processing $u \xrightarrow{c} v$ at depth $d(v) = d(u) + 1$, every state $x$ already in the GSAM has $\text{len}(x) \le d(v)$. Since $u$ is a Trie node and $c$ is a distinct child character of $u$, $\delta(\text{sam\_node}(u), c)$ is guaranteed to be $0$! Moreover, the standard potential function $\Phi = \text{len}(p) - \text{len}(\text{link}(p))$ amortizes the suffix-link climbs across the entire BFS because each newly created node has $\text{len}(\text{cur}) = d(v)$ which is monotonic.
2. **Why DFS on an uncompacted Trie (or Online Reset Insertion without Trie compaction) can degrade to $O(V \sqrt{V})$ or $O(\sum |S_i|^2)$ if implemented carelessly**:
   Wait—does Online GSAM (with the 3-case contract) run in $O(\sum |S_i|)$? Yes, **for a list of strings $\mathcal{S} = \{S_1, \dots, S_k\}$ of total length $N = \sum |S_i|$**, because along each string $S_i$, the potential $\text{len}(p) - \text{len}(\text{link}(p))$ increases by at most $1$ per character of $S_i$ and drops by at least $1$ per suffix-link step, bounding total steps for $S_i$ by $O(|S_i|)$ and overall time by $O(\sum |S_i| |\Sigma|)$!
   **However**, if you are given an **explicit Trie $\mathcal{T}$ with $V$ nodes** where many leaves branch off a long spine of length $V/2$ (so total string length across all root-to-leaf paths is $\Theta(V^2)$, even though $|V| = V$), running **DFS** on the Trie without Case 3 redirection—or worse, running DFS where a deep branch creates transitions that are repeatedly split at every single ancestor when shallow branches are visited later—can take $\Theta(V^2)$ time! Specifically, consider a Trie consisting of a main path $a^m b$ of length $m+1$, and $m$ short branches $a^k b$ for $k = 1, \dots, m-1$ (represented by just sharing the $a^m$ spine in the Trie, with a $b$-leaf attached at each depth $k$). If DFS processes the deepest branch $a^m b$ first, $\delta(\text{state}(a^k), b)$ is set to $\text{state}(a^m b)$ for all $k = 0 \dots m-1$. Then, if DFS visits the $b$-leaves from top to bottom ($k = 1, 2, \dots, m-1$), each visit at depth $k$ splits the state for $a^m b$ and walks up $m - k$ links—or if visited in adversarial order, the potential $\text{len}(\text{last})$ jumps down by $O(m)$ at every leaf back-track without paying for the climb! In **BFS**, all nodes at depth $k$ are processed before depth $k+1$, so $\text{len}(\text{cur})$ is globally non-decreasing and total time is strictly $O(V |\Sigma|)$.

#### Step 4: Boundary Pitfalls & The Zero-Length Clone Counterexample

Let us trace the **Zero-Length Clone Bug (`空节点陷阱`)** on the minimal counterexample $\mathcal{S} = \{S_1 = \texttt{ab}, S_2 = \texttt{b}\}$.

##### Counterexample 11.4 (The Zero-Length Clone Corruption on $\mathcal{S} = \{\texttt{ab}, \texttt{b}\}$)
1. Insert $S_1 = \texttt{ab}$ starting from root $1$:
   - `a`: state $2$, $\text{len}(2) = 1, \text{link}(2) = 1, \delta(1, \texttt{a}) = 2$.
   - `b`: state $3$, $\text{len}(3) = 2, \text{link}(3) = 1, \delta(2, \texttt{b}) = 3, \delta(1, \texttt{b}) = 3$.
   Notice that at this point, state $3$ represents $E(3) = \{\texttt{b}, \texttt{ab}\}$ with $\text{len}(3) = 2$, and $\delta(1, \texttt{b}) = 3$ is **already non-zero**!
2. Now reset `last = 1` and insert $S_2 = \texttt{b}$:
   - **What Naive Single-String SAM Code Does (BUG!)**:
     Naive code unconditionally creates state $4$ (`cur = 4`) with $\text{len}(4) = \text{len}(1) + 1 = 1$. Then its while-loop checks `while (p && !ch[p]['b'])`, which **immediately terminates** because `ch[1]['b'] == 3 != 0`! Notice that `ch[1]['b']` is **not even updated to $4$**! Next, because $\text{len}(3) = 2 > \text{len}(1) + 1 = 1$, naive code creates a clone state $5$ (`clone = 5`) with $\text{len}(5) = 1$, redirects `ch[1]['b'] = 5`, and sets $\text{link}(3) = \text{link}(4) = 5, \text{link}(5) = 1$.
     - **Fatal Corruption 1 (Zero-Length State)**: State $4$ has $\text{len}(4) = 1$ and $\text{link}(4) = 5$ with $\text{len}(5) = 1$. Thus $\text{len}(4) - \text{len}(\text{link}(4)) = 1 - 1 = 0$! State $4$ represents an **empty interval of substrings** $[\text{len}(5)+1, \text{len}(4)] = [2, 1] = \emptyset$.
     - **Fatal Corruption 2 (Unreachable Orphan Node)**: No transition in the DAG points to state $4$ (`ch[1]['b']` points to $5$, not $4$!). Yet `last` is returned as $4$! If $S_2$ had a second character (e.g. $S_2 = \texttt{bc}$), the transition for $\texttt{c}$ would be attached to the unreachable orphan state $4$ and its ancestor $5$, while the Link Tree would have an extra dead leaf $4$ carrying the $\text{endpos}$ weight of $S_2[1]$!
   - **What Correct Case 3 GSAM Code Does**:
     Since $\delta(1, \texttt{b}) = 3 \ne 0$ and $\text{len}(3) = 2 > \text{len}(1) + 1 = 1$, Case 3 creates **only** state $4$ (`clone = 4`) with $\text{len}(4) = 1$, copies transitions of $3$, sets $\delta(1, \texttt{b}) \leftarrow 4$, $\text{link}(3) \leftarrow 4, \text{link}(4) \leftarrow 1$, and returns $4$. Now $E(4) = \{\texttt{b}\}$ ($\text{len} \in [1, 1]$) and $E(3) = \{\texttt{ab}\}$ ($\text{len} \in [2, 2]$). Every state has $\text{len}(u) > \text{len}(\text{link}(u))$ and every state is reachable!

---

## Iteration 12: SAM + Segment Tree Merging on $\text{endpos}$ (`线段树合并维护 Endpos`)

### 12.1 The 4-Step Zero-Magic Analysis of Endpos Segment Tree Merging & Substring Clipping

#### Step 1: The Diagnostic Signal (Why Whole-String Endpos Fails on Substring Range Queries $S[l..r]$)
In a standard SAM on $S[1..N]$, a state $u$ stores (after a bottom-up Link-Tree sum) only the **total count** $|\text{endpos}_S(u)|$ or a single representative position $\text{firstpos}(u) \in \text{endpos}_S(u)$. This suffices for queries on the entire string $S[1..N]$.
However, grandmaster string problems (`[NOI2018] 你的名字`, `[HEOI2016] 字符串`, `CF 1037H`, `CF 666E`) restrict the text to an **arbitrary query substring** $S[l..r]$ (or a range of dictionary strings $T_l, \dots, T_r$). Two immediate obstacles arise:
1. **Explicit Endpos Set Maintenance**: We cannot afford $O(N^2)$ memory to store the set $\text{endpos}_S(u) \subseteq \{1, \dots, N\}$ explicitly at every state $u$.
2. **Variable-Length Boundary Straddling (`左边界越界`)**: Even if we know every right endpoint $e \in \text{endpos}_S(u)$, checking $e \in [l, r]$ is **WRONG**! A state $u$ represents substrings of all lengths $L \in [\text{len}(\text{link}(u)) + 1, \text{len}(u)]$. If $e \in [l, l + L - 2]$, then the occurrence of length $L$ ending at $e$ is $S[e - L + 1 .. e]$, which starts at $e - L + 1 < l$—it **straddles the left boundary $l$** and is *not* contained in $S[l..r]$!

#### Step 2: The Combinatorial Word Invariant (The Substring Containment Clipping Invariant)

##### Theorem 12.1 (The Substring Containment Clipping Invariant)
Let $P$ be a substring of $S$ of exact length $L = |P|$, and let $u \in \text{SAM}(S)$ be the unique SAM state such that $P \in E(u)$ (so $\text{len}(\text{link}(u)) < L \le \text{len}(u)$). Then $P$ occurs as a contiguous substring of $S[l..r]$ (with $1 \le l \le r \le N$) **if and only if**
$$L \le r - l + 1 \quad \text{and} \quad \text{endpos}_S(u) \cap [l + L - 1, \, r] \ne \emptyset.$$
More generally, the number of occurrences of $P$ inside $S[l..r]$ is exactly
$$\text{occ}(P, S[l..r]) = \bigl|\text{endpos}_S(u) \cap [l + L - 1, \, r]\bigr|.$$

*Proof*:
1. By Lemma 11.1, because $P \in E(u)$, the set of right endpoints of $P$ in $S[1..N]$ is identical to $\text{endpos}_S(u)$:
   $$S[e - L + 1 .. e] = P \iff e \in \text{endpos}_S(u).$$
2. An occurrence $S[e - L + 1 .. e]$ lies completely within the subsegment $S[l..r]$ if and only if its start index satisfies $e - L + 1 \ge l$ and its end index satisfies $e \le r$.
3. Rearranging $e - L + 1 \ge l$ yields $e \ge l + L - 1$. Thus the valid right endpoints $e$ are precisely those in $\text{endpos}_S(u) \cap [l + L - 1, r]$. $\blacksquare$

```
  Index axis of S:
  1         l              e - L + 1       l + L - 1          e          r        N
  |---------|------------------|---------------|--------------|----------|--------|
            |<-------------- S[l .. r] ---------------------->|
                               |<---- P (length L) ---------->|
                               start = e - L + 1 >= l  <===>  e >= l + L - 1
```

##### Corollary 12.2 (Maximum Clipped Match Length inside a Single SAM State $u$)
Suppose we have matched a query string $T$ up to state $u \in \text{SAM}(S)$ with current unclipped match length $L_{\text{raw}} \le \text{len}(u)$, and we want the longest suffix of this match that belongs to state $u$ (i.e., has length $L \in [\text{len}(\text{link}(u)) + 1, L_{\text{raw}}]$) and appears inside $S[l..r]$. Let $e_{\max}$ be the **largest** element of $\text{endpos}_S(u)$ satisfying $e_{\max} \le r$ (found via a predecessor query on $u$'s Segment Tree in $[1, r]$). Then the maximum valid length $L$ achievable within state $u$ is
$$L_{\text{valid}}(u) = \min\bigl(L_{\text{raw}}, \, e_{\max} - l + 1\bigr),$$
which lies in $E(u)$ if and only if $L_{\text{valid}}(u) > \text{len}(\text{link}(u))$.

*Proof*: For any $e \in \text{endpos}_S(u) \cap [1, r]$, the longest suffix of $S[1..e]$ that starts at or after $l$ has length $e - l + 1$. Maximizing $e - l + 1$ over $e \in \text{endpos}_S(u) \cap [1, r]$ is achieved by maximizing $e$, which is $e_{\max} = \max(\text{endpos}_S(u) \cap [1, r])$. $\blacksquare$

#### Step 3: The Reverse-Engineering Scratchpad (Binary Lifting + Persistent Segment Tree Merge)

##### Component A: Locating $S[l..r]$ via Link-Tree Binary Lifting (`倍增定位子串`)
Given a query substring $S[l..r]$ of length $L = r - l + 1$:
1. During the construction of $\text{SAM}(S)$, record $\text{pos}[r]$ as the SAM state corresponding to the prefix $S[1..r]$ (so $r \in \text{endpos}_S(\text{pos}[r])$ and $\text{len}(\text{pos}[r]) = r$).
2. Because $S[l..r]$ is the suffix of $S[1..r]$ of length $L = r - l + 1$, the unique state $u$ with $S[l..r] \in E(u)$ is an ancestor of $\text{pos}[r]$ in the Link Tree $\mathcal{T}_{\text{link}}$.
3. Specifically, as we walk up the Link Tree from $\text{pos}[r]$ to the root, the intervals $[\text{len}(\text{link}(v)) + 1, \text{len}(v)]$ partition $[1, r]$ in decreasing order of length. Therefore, $u$ is the **highest ancestor** of $\text{pos}[r]$ satisfying
   $$\text{len}(u) \ge r - l + 1.$$
4. Precomputing the binary lifting table $\text{up}[k][v]$ ($2^k$-th ancestor in $\mathcal{T}_{\text{link}}$) finds $u$ in $O(\log N)$ time:
   for $k = \lfloor \log_2(2N) \rfloor$ down to $0$, if $\text{up}[k][v] \ne 0$ and $\text{len}(\text{up}[k][v]) \ge r - l + 1$, set $v \leftarrow \text{up}[k][v]$.

##### Component B: Persistent Bottom-Up Segment Tree Merging on $\mathcal{T}_{\text{link}}$
For every prefix $r \in \{1, \dots, N\}$, the state $\text{pos}[r]$ initially receives a dynamic-node Segment Tree containing the single point $r$ over the value domain $[1, N]$.
Because $\text{endpos}_S(u)$ is the disjoint union of $\{r \text{ if } u = \text{pos}[r]\}$ and $\bigsqcup_{\text{link}(v) = u} \text{endpos}_S(v)$, we process states $u$ in decreasing order of $\text{len}(u)$ (via counting sort on $\text{len}$ in $O(N)$ time, avoiding explicit tree adjacency lists if desired) and merge each node's Segment Tree into its suffix link parent:
$$\text{rt}[\text{link}(u)] \leftarrow \text{merge}(\text{rt}[\text{link}(u)], \text{rt}[u]).$$
- **Why Persistence is Mandatory for Online / Multi-Node Queries**: If queries inspect $\text{rt}[u]$ *after* all merges complete, destructive in-place merging (where `merge(x, y)` overwrites node `x` when `x` and `y` are both internal nodes of the Segment Tree) **corrupts `rt[u]`** because descendants of `rt[u]` get mutated when `rt[u]` is later merged into $\text{rt}[\text{link}(u)]$! Allocating a fresh node `z` whenever `merge(x, y)` encounters two non-null nodes `x, y` preserves all $2N-1$ root versions in $O(N \log N)$ total time and space.

#### Step 4: Boundary Pitfalls & Five Complete Landmark Problem Derivations

- **Pitfall 1 (Forgetting Persistence During Bottom-Up Merge)**: Overwriting `x` in `merge(x, y)` only works if queries on `u` are answered *offline during the DFS at node `u`* before `rt[u]` is merged into `link(u)`. Whenever queries jump to arbitrary nodes via binary lifting or SAM walks (`[NOI2018] 你的名字`, `CF 1037H`, `CF 666E`, `CF 700E`), `merge(x, y)` **must** allocate a new node (at least for internal nodes; or whenever both `x` and `y` exist).
- **Pitfall 2 (Off-by-One in `CF 700E` Self-Occurrence Check)**: When checking if ancestor $v$ appears at least twice in $u$, one occurrence always ends at $\text{pos}(u)$ (the right endpoint of the representative string of $u$). The second occurrence must end in $[\text{pos}(u) - \text{len}(u) + \text{len}(v), \, \text{pos}(u) - 1]$. Using $\text{len}(v) - 1$ instead of $\text{len}(v)$ allows an occurrence that starts at $\text{pos}(u) - \text{len}(u)$, which is $1$ character to the left of $u$'s representative!

---

### 12.2 Complete 4-Step Derivations of the Five Canonical Endpos-Merge Problems

#### Landmark 1: `[NOI2018] 你的名字 (Your Name)` (`Luogu P4770` / `LOJ 2720`)
> **Problem Contract**: Given a reference string $S$ ($|S| \le 5 \times 10^5$) and $Q$ queries ($\sum |T| \le 10^6$). Each query provides a pattern $T$ and an interval $[l, r]$ ($1 \le l \le r \le |S|$). Count how many **distinct substrings** of $T$ do **not** occur as a substring of $S[l..r]$.

1. **Diagnostic Signal**: When $l=1, r=|S|$ (Subtask 1, 68 pts), we can match $T$ on $\text{SAM}(S)$ in $O(|T|)$ time. When $[l, r]$ is restricted (32 pts), a transition $u \xrightarrow{c} \delta(u, c)$ in $\text{SAM}(S)$ may exist in the whole string $S$ while having **zero occurrences** inside $S[l..r]$!
2. **Combinatorial Invariant**: For each prefix $T[1..i]$ ($1 \le i \le |T|$), define $\text{lim}[i]$ to be the length of the **longest suffix of $T[1..i]$ that occurs inside $S[l..r]$**. Because every suffix of a valid substring of $S[l..r]$ also occurs in $S[l..r]$, a suffix of $T[1..i]$ of length $L$ occurs in $S[l..r]$ iff $L \le \text{lim}[i]$.
   Now build a separate $\text{SAM}(T)$ for the query string $T$. Each state $v \in \text{SAM}(T)$ represents suffixes of $T[1..\text{pos}_T(v)]$ with lengths in $[\text{len}_T(\text{link}_T(v)) + 1, \text{len}_T(v)]$. Among these, the ones that do **not** occur in $S[l..r]$ are precisely those with length $> \text{lim}[\text{pos}_T(v)]$. Thus the answer is:
   $$\text{Ans}(T, l, r) = \sum_{v \in \text{SAM}(T) \setminus \{\text{root}\}} \max\Bigl(0, \, \text{len}_T(v) - \max\bigl(\text{len}_T(\text{link}_T(v)), \, \text{lim}[\text{pos}_T(v)]\bigr)\Bigr).$$
3. **Reverse-Engineering Scratchpad (Two-Pointer Clipped SAM Walk)**:
   Maintain the current state $u \in \text{SAM}(S)$ and current valid match length $L = \text{lim}[i-1]$ inside $S[l..r]$. To advance to $T[i] = c$:
   - Loop:
     - Check if transition $w = \delta_S(u, c)$ exists **and** has an occurrence of length $L + 1$ inside $S[l..r]$, which by Theorem 12.1 means querying $\text{rt}[w]$ on the interval $[l + L, \, r]$!
     - If $\text{query}(\text{rt}[w], \, l + L, \, r) > 0$: we succeed! Set $u \leftarrow w$, $L \leftarrow L + 1$, and break.
     - Otherwise, we must shorten $L$ by $1$:
       - If $L = 0$, break (stay at root $u = 1, L = 0$).
       - Decrement $L \leftarrow L - 1$. If $L = \text{len}_S(\text{link}_S(u))$, step up to the suffix link: $u \leftarrow \text{link}_S(u)$.
   - Set $\text{lim}[i] = L$.
   Because $L$ increases at most $|T|$ times and therefore decreases at most $|T|$ times, there are at most $2|T|$ Segment Tree queries, giving $O((|S| + \sum |T|) \log |S|)$ total time!
4. **Boundary Pitfall**: Why must we decrement $L \leftarrow L - 1$ (and only jump $u \leftarrow \text{link}_S(u)$ when $L == \text{len}_S(\text{link}_S(u))$) instead of jumping $u \leftarrow \text{link}_S(u)$ immediately and setting $L \leftarrow \text{len}_S(u)$?
   **Counterexample**: Suppose $u$ covers lengths $[3, 5]$, $L = 5$, and $\delta_S(u, c) = w$ exists, where $w$ occurs in $S[l..r]$ at $e = l + 3$ (so length $4 + 1 = 5$ fails because $e < l + 4$, but length $3 + 1 = 4$ succeeds because $e \ge l + 3$!). If we jumped $u \leftarrow \text{link}_S(u)$ immediately, $L$ would drop from $5$ straight to $\text{len}_S(\text{link}_S(u)) = 2$, completely skipping the valid length $L+1 = 4$ inside state $w$! (Alternatively, using Corollary 12.2, one can query $e_{\max} = \max(\text{endpos}(w) \cap [1, r])$ to jump $L$ directly to $e_{\max} - l + 1$).

#### Landmark 2: `[HEOI2016 / TJOI2016] 字符串` (`Luogu P4094`)
> **Problem Contract**: Given $S[1..N]$ ($N, Q \le 10^5$), for each query $(a, b, c, d)$, compute $\max_{a \le i \le b} \min\bigl(b - i + 1, \, \text{LCP}(S[i..b], S[c..d])\bigr)$—i.e., the maximum length $L$ of a prefix of $S[c..d]$ that occurs completely inside $S[a..b]$.

1. **Diagnostic Signal**: We are maximizing $L \in [0, \min(b-a+1, d-c+1)]$ such that the prefix $S[c .. c+L-1]$ occurs as a substring of $S[a..b]$. This predicate is **monotonic** in $L$: if $S[c..c+L-1]$ occurs in $S[a..b]$, so does every shorter prefix $S[c..c+L'-1]$.
2. **Combinatorial Invariant**: By Theorem 12.1, for a fixed candidate length $L$, let $u_L \in \text{SAM}(S)$ be the state containing $S[c .. c+L-1]$. Then $S[c .. c+L-1]$ occurs inside $S[a..b]$ iff
   $$\text{endpos}_S(u_L) \cap [a + L - 1, \, b] \ne \emptyset.$$
3. **Reverse-Engineering Scratchpad**:
   - Build $\text{SAM}(S)$, Link-Tree binary lifting $\text{up}[k][v]$, and Persistent Segment Tree Merge over $\text{endpos}_S$.
   - Binary search $L \in [1, \min(b-a+1, d-c+1)]$:
     - Locate $u_L$ by binary lifting from $\text{pos}[c + L - 1]$ to the highest ancestor with $\text{len}(u_L) \ge L$ in $O(\log N)$ time.
     - Query $\text{rt}[u_L]$ on $[a + L - 1, \, b]$ in $O(\log N)$ time.
   - Total time: $O(Q \log^2 N)$ with tiny constant factor. (Can be reduced to $O(Q \log N)$ via reversed SAM + tree walk, or SA + persistent segment tree, though $O(Q \log^2 N)$ is the canonical SAM+Merge reference).
4. **Boundary Pitfall**: In the binary lifting step, we lift from $\text{pos}[c + L - 1]$ (which changes with $L$!), **not** from $\text{pos}[d]$, unless we build the SAM on $S^R$ (where $S[c..c+L-1]$ is a suffix of $S^R[1..c]$ and we lift from fixed $\text{pos}_{S^R}[c]$).

#### Landmark 3: `CF 1037H — Security`
> **Problem Contract**: Given $S[1..N]$ ($N \le 10^5$) and $Q$ queries $(l, r, T)$ ($\sum |T| \le 2 \times 10^5$). Find the lexicographically smallest string $T' > T$ that occurs as a substring of $S[l..r]$, or output `-1`.

1. **Diagnostic Signal**: $T'$ must share some common prefix $T[1..i]$ ($0 \le i \le |T|$) with $T$, followed by a single strictly greater character $c > T[i+1]$ (where $T[|T|+1] = \emptyset < \texttt{'a'}$). To minimize $T'$ lexicographically, we must **maximize** the shared prefix length $i$, then **minimize** $c > T[i+1]$, and stop immediately after $c$ (since $T[1..i]c$ is already strictly greater than $T$ and shorter is lexicographically smaller!).
2. **Combinatorial Invariant**: The candidate string $T[1..i]c$ of length $i + 1$ occurs in $S[l..r]$ iff the state $w = \delta(\text{state}(T[1..i]), c)$ exists in $\text{SAM}(S)$ and satisfies
   $$\text{endpos}_S(w) \cap [l + i, \, r] \ne \emptyset.$$
3. **Reverse-Engineering Scratchpad**:
   - Walk $T$ along the DFA transitions of $\text{SAM}(S)$ starting from $u_0 = 1$: for $i = 1 \dots |T|$, set $u_i = \delta(u_{i-1}, T[i])$ (stopping when $u_i = 0$ or $i > r - l + 1$). Notice we don't even need suffix links here because $T[1..i]$ is a prefix of length $i$ starting from the root!
   - Iterate $i$ from $\min(|T|, r - l)$ down to $0$ (where $u_i \ne 0$):
     - Try characters $c \in \Sigma$ in increasing order with $c > T[i+1]$ (for $i = |T|$, try all $c \in [\texttt{'a'}, \texttt{'z'}]$):
     - Let $w = \delta(u_i, c)$. If $w \ne 0$ and $\text{query}(\text{rt}[w], \, l + i, \, r) > 0$, output $T[1..i]c$ and terminate!
   - If no $(i, c)$ succeeds, output `-1`. Time: $O((N + |\Sigma| \sum |T|) \log N)$.

#### Landmark 4: `CF 666E — Forensic Examination`
> **Problem Contract**: Given a main string $S$ ($|S| \le 5 \times 10^5$), $m$ dictionary strings $T_1, \dots, T_m$ ($\sum |T_k| \le 5 \times 10^4$), and $Q \le 5 \times 10^5$ queries $(l, r, p_l, p_r)$. Among dictionary indices $k \in [l, r]$, find the $k$ that maximizes $\text{occ}(S[p_l..p_r], T_k)$ (ties broken by smallest $k$).

1. **Diagnostic Signal**: Instead of clipping positions within a single string, we need the occurrence count distribution of $S[p_l..p_r]$ across **dictionary string IDs** $k \in [1, m]$.
2. **Combinatorial Invariant**: Build a Generalized SAM on $\{T_1, \dots, T_m\}$ (or on $\{S, T_1, \dots, T_m\}$). For each state $u$ in the GSAM, its Segment Tree is indexed by **dictionary ID** $k \in [1, m]$ and stores the number of occurrences of $E(u)$ in $T_k$, along with the range maximum pair $(\text{max\_cnt}, -\text{best\_id})$.
3. **Reverse-Engineering Scratchpad**:
   - Insert $T_1, \dots, T_m$ into the GSAM; at each prefix of $T_k$, add $+1$ at position $k$ in that state's Segment Tree.
   - Pre-match $S[1..|S|]$ against the GSAM (exactly as in `[NOI2018] 你的名字` without clipping) to record for each prefix $S[1..p_r]$ the reached GSAM state $\text{pos}_S[p_r]$ and the maximum matched suffix length $\text{match\_len}[p_r]$.
   - For query $(l, r, p_l, p_r)$ with length $L = p_r - p_l + 1$:
     - If $\text{match\_len}[p_r] < L$, then $S[p_l..p_r]$ does not appear in *any* $T_k$; return $(l, 0)$.
     - Otherwise, binary lift from $\text{pos}_S[p_r]$ to the highest ancestor $u$ with $\text{len}(u) \ge L$, and query $\text{rt}[u]$ on $[l, r]$ for the maximum $(\text{cnt}, -k)$ (returning $(l, 0)$ if $\text{max\_cnt} = 0$).

#### Landmark 5: `CF 700E — Cool Slogans`
> **Problem Contract**: Given $S[1..N]$ ($N \le 2 \times 10^5$), find the maximum $k$ such that there exist strings $s_1, s_2, \dots, s_k$ where $s_k$ is a substring of $S$ and each $s_i$ occurs at least twice (possibly overlapping) in $s_{i+1}$.

1. **Diagnostic Signal**: Every state $u \in \text{SAM}(S)$ contains $\text{len}(u) - \text{len}(\text{link}(u))$ different strings. Doing DP over all $O(N^2)$ substrings is impossible; we must reduce the DP state space to the $2N-1$ SAM nodes!
2. **Combinatorial Invariant (The Top-Len Sufficiency Lemma)**:
   - **Claim 1**: If $s_i$ occurs at least twice in $s_{i+1}$, then we may assume $s_i$ is a suffix of $s_{i+1}$ (by trimming characters from the right of $s_{i+1}$ after the second occurrence of $s_i$), so $\text{state}(s_i)$ is a strict ancestor of $\text{state}(s_{i+1})$ in $\mathcal{T}_{\text{link}}$.
   - **Claim 2 (All-or-Nothing Within $E(v)$)**: Suppose $v$ is an ancestor of $u$ in $\mathcal{T}_{\text{link}}$, and let $w = \text{longest}(u) = S[\text{pos}(u) - \text{len}(u) + 1 .. \text{pos}(u)]$. Because every string $x \in E(v)$ has the **exact same** $\text{endpos}$ set, the longest string $\text{longest}(v) \in E(v)$ occurs twice in $w$ if and only if $\text{shortest}(v) \in E(v)$ occurs twice in the corresponding shorter representative of $u$! Therefore, we can restrict every $s_i$ to be $\text{longest}(u_i)$ for some state $u_i \in \text{SAM}(S)$!
   - **Double-Occurrence Criterion**: Since $\text{longest}(v)$ is a suffix of $\text{longest}(u)$, it automatically occurs once ending at $\text{pos}(u)$. It occurs a **second** time inside $\text{longest}(u) = S[\text{pos}(u) - \text{len}(u) + 1 .. \text{pos}(u)]$ if and only if it has an occurrence in $S[\text{pos}(u) - \text{len}(u) + 1 .. \text{pos}(u) - 1]$, which by Theorem 12.1 is:
     $$\text{endpos}_S(v) \cap \bigl[\text{pos}(u) - \text{len}(u) + \text{len}(v), \, \text{pos}(u) - 1\bigr] \ne \emptyset.$$
3. **Reverse-Engineering Scratchpad (Top-Down Link-Tree DP)**:
   Along any root-to-leaf path in $\mathcal{T}_{\text{link}}$, $\text{dp}[u]$ is non-decreasing and increases by at most $1$ at each step. Thus, for state $u$ with parent $p = \text{link}(u)$, let $\text{top}[p]$ be the highest ancestor of $p$ with $\text{dp}[\text{top}[p]] = \text{dp}[p]$. We only need to check whether $v = \text{top}[p]$ occurs twice in $u$:
   - If $\text{query}\bigl(\text{rt}[v], \, \text{pos}(u) - \text{len}(u) + \text{len}(v), \, \text{pos}(u) - 1\bigr) > 0$, then $\text{dp}[u] = \text{dp}[p] + 1$ and $\text{top}[u] = u$.
   - Otherwise, $\text{dp}[u] = \text{dp}[p]$ and $\text{top}[u] = \text{top}[p]$.
   Total time: $O(N \log N)$.

---

## Iteration 13: Dynamic SAM + Link-Cut Tree (`access` Color-Chain Sweeping / `树点涂色` Paradigm)

### 13.1 The 4-Step Zero-Magic Analysis of LCT + SAM Coupling

#### Step 1: The Diagnostic Signal (Why Static Segment Tree Merging Fails on Dynamic Appends & 2D Range Distinct Substrings)
SAM + Segment Tree Merging solves point-or-pattern queries inside $S[l..r]$, but fails in two major regimes:
1. **Regime A — Online Right-Appends + Pattern Queries (`[BZOJ 2555] SubString`)**: Characters are appended to the end of $S$ online, interleaved with queries asking how many times a pattern $P$ occurs in the *current* string $S$. Because appending a character splits an existing Link-Tree edge ($q \to \text{clone} \to \text{link}(q)$) and adds $+1$ to the $\text{endpos}$ count of every ancestor of the new leaf `cur`, no static Euler tour / DFS order exists!
2. **Regime B — Aggregate Queries over ALL Substrings of $S[l..r]$ (`[SDOI2017]`, `Luogu P6292 — 区间本质不同子串个数`)**: We are asked to compute the number (or weighted sum) of **all distinct substrings** contained in $S[l..r]$ for $Q$ queries $(l, r)$. There is no query pattern $T$ to walk on the SAM; instead, we must aggregate over all $O(N)$ SAM states whose $\text{endpos}$ intersects $[l + L - 1, r]$.

#### Step 2: The Combinatorial Word Invariant (The Last-Occurrence `access` Color-Chain Decomposition)

Consider Regime B: we sweep the right endpoint $r$ from $1$ to $N$ and answer all queries with right endpoint $r$.
At step $r$, for any substring $w$ of $S[1..r]$, let $\text{last}_r(w) = \max(\text{endpos}_{S[1..r]}(w))$ be the **rightmost ending position** of $w$ in $S[1..r]$.
- Then $w$ occurs at least once inside $S[l..r]$ if and only if its rightmost occurrence in $S[1..r]$ starts at or after $l$:
  $$\text{last}_r(w) - |w| + 1 \ge l \iff l \le \text{last}_r(w) - |w| + 1.$$

Now view this on the Link Tree $\mathcal{T}_{\text{link}}$ of $\text{SAM}(S)$:
1. **State Uniformity**: Every substring $w \in E(u)$ in the same SAM state $u$ shares the **exact same** $\text{endpos}$ set, so $\text{last}_r(w) = \text{last}_r(u)$ for all $w \in E(u)$.
2. **Interval of Valid Start Cutoff Positions**: As $|w|$ ranges over the contiguous interval $[\text{len}(\text{link}(u)) + 1, \, \text{len}(u)]$, the rightmost starting position $\text{last}_r(u) - |w| + 1$ of $w$ ranges over the **contiguous interval of start indices**:
   $$I_r(u) = \bigl[\text{last}_r(u) - \text{len}(u) + 1, \;\; \text{last}_r(u) - \text{len}(\text{link}(u))\bigr].$$
   In other words, state $u$ contributes $+1$ to the answer for every query left endpoint $l \in I_r(u)$!
3. **Path Contiguity Across Solid Chains (`树点涂色` Coalescing)**:
   Even better: suppose $u_1, u_2, \dots, u_k$ is a contiguous vertical chain of nodes on $\mathcal{T}_{\text{link}}$ (with $u_i = \text{link}(u_{i+1})$) that all share the **exact same** value of $\text{last}_r(u_i) = p_{\text{old}}$. Because the length intervals $[\text{len}(\text{link}(u_i)) + 1, \text{len}(u_i)]$ telescope seamlessly:
   $$\bigsqcup_{i=1}^k \bigl[\text{len}(\text{link}(u_i)) + 1, \, \text{len}(u_i)\bigr] = \bigl[\text{len}(\text{link}(u_1)) + 1, \, \text{len}(u_k)\bigr],$$
   their start-position intervals $I_r(u_i)$ also telescope into a **single contiguous interval**:
   $$\bigsqcup_{i=1}^k I_r(u_i) = \bigl[p_{\text{old}} - \text{len}(u_k) + 1, \;\; p_{\text{old}} - \text{len}(\text{link}(u_1))\bigr]!$$

```
  When sweeping r-1 -> r, what changes?
  Only the ancestors of pos[r] on the Link Tree have their last_r(u) updated to r!
  This is IDENTICAL to coloring the path from pos[r] to the root with color r,
  which is EXACTLY the Link-Cut Tree `access(pos[r])` operation!

  Solid Chain C in LCT before access(pos[r]):
  All nodes u in C share last(u) = p_old
  Length span of C: [L_min, L_max] = [len(link(top(C))) + 1, len(bot(C))]
  ---> 1 Range Update on Segment Tree / BIT:
       Subtract 1 on [p_old - L_max + 1,  p_old - L_min + 1]
  After access(pos[r]):
  Entire path from root to pos[r] becomes 1 solid chain with color r and span [1, r]
  ---> 1 Range Update on Segment Tree / BIT:
       Add 1 on [1, r]
```

##### Theorem 13.1 (Amortized $O((N + Q) \log^2 N)$ Complexity of SAM + LCT `access` Sweep)
Build $\text{SAM}(S)$ offline in $O(N)$ time, initialize an LCT over the static Link Tree $\mathcal{T}_{\text{link}}$, and sweep $r = 1 \dots N$:
- At step $r$, execute `access(pos[r])` on the LCT.
- Each splay tree visited during `access(pos[r])` represents a maximal solid chain $C$ of nodes sharing the same previous last-occurrence $p_{\text{old}}(C)$ and spanning lengths $[L_{\min}(C), L_{\max}(C)] = [\text{len}(\text{link}(\text{top}(C))) + 1, \text{len}(\text{bot}(C))]$.
- If $p_{\text{old}}(C) > 0$, perform a range addition of $-1$ on the interval $[p_{\text{old}}(C) - L_{\max}(C) + 1, \, p_{\text{old}}(C) - L_{\min}(C) + 1]$ in a Fenwick Tree / Segment Tree over query start indices $l \in [1, N]$.
- After the loop finishes, color the newly formed root-to-$\text{pos}[r]$ solid chain with $p_{\text{new}} = r$ and perform a single range addition of $+1$ on $[1, r]$.
- Answer all queries $(l, r)$ via a point query at index $l$ (or range sum if weighted).

By Sleator–Tarjan LCT amortization, $N$ calls to `access` split and merge at most $O(N \log N)$ solid chains in total. Each chain performs $O(1)$ Fenwick/Segment Tree range updates, yielding $O(N \log^2 N + Q \log N)$ total time and $O(N)$ memory! $\blacksquare$

#### Step 3: The Reverse-Engineering Scratchpad (Regime A vs. Regime B Implementation Contracts)

##### Contract 13.2: Regime A — Online Dynamic SAM + LCT (`[BZOJ 2555] SubString`)
Here we maintain $|\text{endpos}(u)|$ dynamically under online right-appends to $S$:
- **LCT State**: Each node $u \in \text{SAM}(S)$ is an LCT node storing `val[u] = |endpos(u)|` and a lazy addition tag `tag[u]` on its splay subtree.
- **LCT Helper `link_edge(u, p)`**: Sets `link[u] = p` and `fa[u] = p` (a dashed LCT edge).
- **LCT Helper `cut_edge(u, p)`**: `access(u); splay(u); ch[u][0] = fa[ch[u][0]] = 0;` (cuts the tree edge between $u$ and its parent $p = \text{link}(u)$).
- **LCT Helper `add_path_to_root(u, delta)`**: `access(u); splay(u); apply_add(u, delta);` (adds `delta` to `val` of all ancestors of $u$ up to the root).
- **Dynamic SAM `extend(c)`**:
  1. Create `cur` with $\text{len}(\text{cur}) = \text{len}(\text{last}) + 1$.
  2. Walk $p$ up via $\text{link}(p)$ while $\delta(p, c) = 0$: set $\delta(p, c) = \text{cur}$.
  3. If $p = 0$: `link_edge(cur, 1)`.
  4. Else let $q = \delta(p, c)$:
     - If $\text{len}(q) = \text{len}(p) + 1$: `link_edge(cur, q)`.
     - Else (split $q \to \text{clone}$):
       - Allocate `clone` with $\text{len}(\text{clone}) = \text{len}(p) + 1$, copy DFA transitions $\delta(\text{clone}, \cdot) \leftarrow \delta(q, \cdot)$.
       - **Crucial LCT Split Sequence**:
         1. Query $q$'s current exact occurrence count: `access(q); splay(q); val[clone] = val[q];` (because before the new character $c$ is counted, $\text{endpos}(\text{clone}) = \text{endpos}(q)$!).
         2. Let $old\_fa = \text{link}(q)$. Cut $q$ from $old\_fa$: `cut_edge(q, old_fa)`.
         3. Insert `clone` between $q$ and $old\_fa$: `link_edge(clone, old_fa)`, `link_edge(q, clone)`, `link_edge(cur, clone)`.
       - Redirect $\delta(p', c) \leftarrow \text{clone}$ for ancestors $p'$ of $p$ with $\delta(p', c) = q$.
  5. Finally, increment the $\text{endpos}$ count of the entire path from `cur` to the root: `add_path_to_root(cur, +1)`.

##### Contract 13.3: Regime B — Offline LCT Color-Chain Sweeping (`Luogu P6292` / `[SDOI2017]`)
- **Maintaining `L_min` and `L_max` on Each Splay Tree**:
  In the LCT over $\mathcal{T}_{\text{link}}$, a splay tree represents a vertical path of nodes ordered by depth. Instead of searching for the shallowest and deepest node in the splay tree, simply store at each LCT node $u$:
  - $\text{self\_min}[u] = \text{len}(\text{link}(u)) + 1$, $\text{self\_max}[u] = \text{len}(u)$.
  - In `pushup(u)`: $\text{sub\_min}[u] = \min(\text{self\_min}[u], \text{sub\_min}[ls], \text{sub\_min}[rs])$ and $\text{sub\_max}[u] = \max(\text{self\_max}[u], \text{sub\_max}[ls], \text{sub\_max}[rs])$.
  Then for the root $x$ of any splay tree during `access`, $[L_{\min}, L_{\max}] = [\text{sub\_min}[x], \text{sub\_max}[x]]$ in $O(1)$ time!
- **Color Lazy Propagation**: Store `col[x]` and `lazy_col[x]` on the splay tree. Because every splay tree during `access` is monochrome (all nodes in the solid chain received the same $r$ during their previous `access`), `col[x]` at the splay root gives $p_{\text{old}}$ immediately, and `pushdown(x)` propagates `lazy_col[x]` whenever `splay` splits a solid chain (`ch[x][1] = y`)!

#### Step 4: Boundary Pitfalls in Dynamic SAM + LCT
1. **Pitfall 1 (Pushing Down Lazy Tags Before Reading `val[q]` in `[BZOJ 2555]`)**: In Regime A, when cloning $q \to \text{clone}$, you **must** call `access(q); splay(q);` before setting `val[clone] = val[q]`. Otherwise, pending lazy $+1$ tags on $q$'s splay ancestors have not been pushed down to `val[q]`, giving `clone` a stale $\text{endpos}$ count!
2. **Pitfall 2 (Adding $+1$ to `cur` Before Attaching `cur` to the Link Tree)**: In Regime A, if you initialize `val[cur] = 1` and *also* call `add_path_to_root(cur, +1)`, `val[cur]` becomes $2$ instead of $1$! Initialize `val[cur] = 0` and let `add_path_to_root(cur, +1)` add $+1$ to `cur` and all its ancestors simultaneously.
3. **Pitfall 3 (Root State $u = 1$ in Regime B)**: The SAM root $1$ represents the empty string ($\text{len}(1) = 0$) and has no valid positive-length substrings. Set $\text{self\_min}[1] = +\infty, \text{self\_max}[1] = -\infty$ so that including node $1$ in a solid chain never pollutes $[L_{\min}, L_{\max}]$ with length $0$.

---

## Iteration 14: HLD on the SAM Link Tree & Prefix-Suffix Graph DAG Construction (`[十二省联考 2019] 字符串问题`)

### 14.1 The 4-Step Zero-Magic Analysis of Prefix-Suffix Graph Optimization on the Link Tree

#### Step 1: The Diagnostic Signal (Why Naive Prefix-Transition Graphs Explode to $O(N^2)$ Edges)
Consider `[十二省联考 2019] 字符串问题` (`Luogu P5284` / `LOJ 3052`):
> **Problem Contract**: Given a string $S[1..N]$ ($N \le 2 \times 10^5$), $n_a$ substrings $A_i = S[l_{a,i}..r_{a,i}]$, and $n_b$ substrings $B_j = S[l_{b,j}..r_{b,j}]$ ($n_a, n_b \le 2 \times 10^5$). You are given $m \le 2 \times 10^5$ explicit directed edges $A_i \to B_j$. Additionally, for every pair $(B_j, A_i)$, there is an **implicit directed edge** $B_j \to A_i$ whenever **$B_j$ is a prefix of $A_i$** (so $|B_j| \le |A_i|$ and $A_i[1..|B_j|] = B_j$). The weight of vertex $A_i$ is $|A_i|$, and the weight of $B_j$ is $0$. Find the maximum total weight of a path starting at any $A_i$, or output `-1` if there is a directed cycle reachable from some $A_i$ (or if the path can be infinitely long).

Why do standard string structures fail if applied naively?
1. **Quadratic Implicit Edges**: A single short $B_j$ (such as $S[1..1]$) can be a prefix of $\Theta(n_a)$ strings $A_i$, creating $\Theta(n_a n_b)$ implicit edges.
2. **Direction Mismatch on $\text{SAM}(S)$**: In $\text{SAM}(S)$, the Link Tree $\mathcal{T}_{\text{link}}$ organizes substrings by **suffix** containment ($u$ is an ancestor of $v$ iff $\text{longest}(u)$ is a **suffix** of $\text{longest}(v)$), whereas the problem's implicit edges require **prefix** containment ($B_j$ is a **prefix** of $A_i$)!
3. **Intra-Node Length Collisions (`同节点内长度混淆`)**: Even after reversing $S$ to $S^R$ (so that prefix containment in $S$ becomes suffix containment in $S^R$), a single state $u \in \text{SAM}(S^R)$ represents an entire interval of lengths $[\text{len}(\text{link}(u)) + 1, \text{len}(u)]$. If both $B_j$ and $A_i$ map to the **same** SAM state $u$, then $B_j$ is a prefix of $A_i$ **if and only if $|B_j| \le |A_i|$**! Connecting state $u$ bidirectionally to both $B_j$ and $A_i$ would allow $B_j \to u \to A_i$ even when $|B_j| > |A_i|$, creating spurious paths and false cycles!

#### Step 2: The Combinatorial Word Invariant (Reversed SAM Subtree Dominance & Intra-Node Total Order)

Build $\text{SAM}(S^R)$ on the reversed string $S^R$ (or equivalently, reverse the index intervals so that $S[l..r]$ corresponds to the suffix of $S^R[1..N-l+1]$ of length $L = r - l + 1$).
For each $A_i$ and $B_j$, locate its exact state $u(A_i), u(B_j) \in \text{SAM}(S^R)$ via Link-Tree binary lifting in $O(\log N)$ time.

##### Lemma 14.1 (Exact Characterization of Prefix Dominance on $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$)
Let $u(B_j)$ and $u(A_i)$ be the states of $B_j$ and $A_i$ in $\text{SAM}(S^R)$. Then $B_j$ is a prefix of $A_i$ in $S$ (equivalently, $B_j^R$ is a suffix of $A_i^R$ in $S^R$) **if and only if** one of the following two mutually exclusive conditions holds:
1. **Strict Subtree Dominance**: $u(B_j)$ is a **strict ancestor** of $u(A_i)$ in $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$ (which automatically implies $|B_j| \le \text{len}(u(B_j)) < \text{len}(\text{link}(u(A_i))) + 1 \le |A_i|$).
2. **Intra-Node Length Dominance**: $u(B_j) = u(A_i)$ (both belong to the exact same equivalence class $E(u)$) **and** $|B_j| \le |A_i|$.

*Proof*: By Lemma 11.1 applied to $S^R$, all strings in $E(u)$ are suffixes of $\text{longest}(u)$ ordered by length, and $\text{longest}(u)$ is a proper suffix of every string in any strict descendant state $v$ in the subtree of $u$. $\blacksquare$

#### Step 3: The Reverse-Engineering Scratchpad (Linear-Size Intra-Node Sorted Chain DAG)

To encode both conditions of Lemma 14.1 using $O(N + n_a + n_b)$ vertices and edges without Segment Trees or HLD overhead:
1. For each state $u \in \text{SAM}(S^R)$, collect a list $\mathcal{L}(u)$ of all $A_i$ and $B_j$ that mapped to state $u$.
2. **Sort $\mathcal{L}(u)$ in non-decreasing order of length $|X|$**, breaking ties at equal length $|B_j| = |A_i|$ by placing **$B_j$ strictly before $A_i$** (since when $|B_j| = |A_i|$ in the same state $u$, $B_j = A_i$, so $B_j$ IS a prefix of $A_i$, requiring $B_j \to A_i$!).
3. **Create a Prefix-Chain of Auxiliary Vertices Inside State $u$**:
   Suppose $\mathcal{L}(u) = (X_1, X_2, \dots, X_k)$. Create an entry hub $\text{in}(u)$, intermediate chain nodes $v_1, v_2, \dots, v_k$, and an exit hub $\text{out}(u) = v_k$ (or if $\mathcal{L}(u) = \emptyset$, simply set $\text{out}(u) = \text{in}(u)$):
   - Add $0$-weight chain edges $\text{in}(u) \to v_1 \to v_2 \to \dots \to v_k = \text{out}(u)$.
   - For each $t \in \{1, \dots, k\}$:
     - If $X_t = B_j$ is a $B$-string, add a $0$-weight edge $B_j \to v_t$ (so $B_j$ can reach all $v_{t'}$ with $t' \ge t$).
     - If $X_t = A_i$ is an $A$-string, add a $0$-weight edge $v_t \to A_i$ (so $A_i$ can be reached from $\text{in}(u)$ and from all $B_j$ in $\mathcal{L}(u)$ with $t_{\text{of } B_j} < t$).
4. **Connect Link-Tree Parent Exit Hubs to Child Entry Hubs**:
   For every Link-Tree edge $p = \text{link}(u) \to u$, add a $0$-weight edge $\text{out}(p) \to \text{in}(u)$.
   - Why does this work? Every $B_j \in \mathcal{L}(p)$ connects to $v_t \to \dots \to \text{out}(p) \to \text{in}(u)$, which then flows into every $v_{t'} \to A_i$ in $u$ and in all descendants of $u$!
5. **Add Explicit Problem Edges & Run Kahn's Topological Sort DP**:
   - Assign vertex weight $|A_i|$ to each $A_i$ node (or put weight $|A_i|$ on incoming/outgoing edges of $A_i$) and $0$ to all other nodes.
   - Add the $m$ explicit edges $A_i \to B_j$.
   - Total vertices: $\le 2N + 2(n_a + n_b) \le 8 \times 10^5$. Total edges: $\le 2N + 3(n_a + n_b) + m \le 10^6$.
   - Run Kahn's topological sort + longest path DP in $O(V + E)$ time! Overall complexity: $O((N + n_a + n_b) \log N + m)$.

```
  Intra-Node Chain Construction inside SAM State u:
  Sorted L(u) by (length, B before A):  [ B_1(len 3),  A_1(len 3),  B_2(len 5),  A_2(len 6) ]

  out(link(u)) ---> in(u) ---> ( v_1 ) -----> ( v_2 ) -----> ( v_3 ) -----> ( v_4 = out(u) ) ---> in(child(u))
                                  ^              |              ^                  |
                                  |              v              |                  v
                                [B_1]          [A_1]          [B_2]              [A_2]
```

#### Step 4: Boundary Pitfalls in Link-Tree Graph Optimization
- **Pitfall 1 (Tie-Breaking at Equal Length $|B_j| = |A_i|$)**: If $|B_j| = |A_i|$ and both map to state $u \in \text{SAM}(S^R)$, then $B_j$ and $A_i$ are both suffixes of $\text{longest}(u)$ of the exact same length, so $B_j = A_i$ as strings! Therefore $B_j$ **is** a prefix of $A_i$. If your comparator sorts $A_i$ before $B_j$ at equal lengths, $B_j$ cannot reach $A_i$ along the chain $v_1 \to \dots \to v_k$, missing a valid transition!
- **Pitfall 2 (Unreachable Cycles)**: In `[十二省联考 2019] 字符串问题`, since every valid walk must start at some $A_i$ (and every $B_j$ has out-degree $\ge 0$, while auxiliary chain nodes without $A_i$ have weight $0$), can an unreachable cycle exist? Any cycle in the graph must use at least one explicit edge $A_i \to B_j$ (because all implicit and chain edges strictly move forward along the topological order of $\mathcal{T}_{\text{link}}$ and intra-node chains!). Since every $A_i$ is a valid starting vertex, **every cycle contains at least one $A_i$** and is automatically reachable!

---

### 14.2 HLD & DSU-on-Tree over the SAM Link Tree (`CF 1098F`, `[Code+#3] 白金元首与莫斯科`)

When a problem couples the SAM Link Tree with path updates, 2-SAT over tree intervals, or LCA-weighted sums over $[l, r]$:

1. **Link-Tree HLD + Segment Tree (`[Code+#3] 白金元首与莫斯科`, 2-SAT on Link Tree)**:
   When constraints apply between a substring $S[l..r]$ and all substrings that are prefixes/suffixes of $S[l..r]$ EXCEPT itself, HLD decomposes the root-to-$u$ path in $\mathcal{T}_{\text{link}}$ into $O(\log N)$ contiguous intervals in DFS order (`dfn[top[x]] .. dfn[x]`), while all strict descendants of $u$ form a single contiguous subtree interval `[dfn[u] + 1, dfn[u] + sz[u] - 1]`. Combining Link-Tree HLD with intra-node length sorting reduces 2-SAT over substring prefix/suffix relations to $O(N \log^2 N)$ clauses.
2. **Link-Tree HLD / DSU-on-Tree for Weighted Range Substring Queries (`CF 1098F — Ж-function`)**:
   > **Problem Contract (`CF 1098F`)**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $(l, r)$, compute $\sum_{i=l}^r \text{LCP}(S[i..r], S[l..r])$.
   - **Reduction to Reversed SAM Link Tree**: Build $\text{SAM}(S^R)$ so that $\text{pos}[i]$ represents the suffix $S[i..N]$ and $\text{len}(\text{LCA}(\text{pos}[i], \text{pos}[l])) = \text{LCP}(S[i..N], S[l..N])$. Then for a query $(l, r)$, each $i \in [l, r]$ contributes $\min\bigl(r - i + 1, \, \text{len}(\text{LCA}(\text{pos}[i], \text{pos}[l]))\bigr)$.
   - **Centroid Decomposition or HLD + Fenwick on $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$**: Decompose $\mathcal{T}_{\text{link}}$ via HLD (or Centroid Decomposition). For a fixed LCA node $u$ with $L = \text{len}(u)$ along the heavy path from $\text{pos}[l]$ to the root, each $i \in [l, r]$ in the light subtree of $u$ contributes $\min(r - i + 1, L)$, which splits at threshold $i \le r - L + 1$ (contributing $L$) vs. $i > r - L + 1$ (contributing $r + 1 - i$). Two Fenwick Trees over indices $i \in [1, N]$ answer the split sum in $O(\log N)$ per light subtree, achieving $O((N + Q) \log^2 N)$ time!

---

## Iteration 15: Multilingual (`[EN]` / `[ZH]` / `[JA]`) Problem Mining, 4-Tier Difficulty Ladder & Template Quarantine

### 15.1 Quarantine Ledger: Rejected Pure Template & Library-Verification Problems (`R-2A-01` – `R-2A-10`)

Per `AGENTS.md` and `PLAN.md` (`§2.2`), problems whose sole purpose is verifying a raw SAM, GSAM, or Suffix Tree implementation without a non-trivial structural invariant, clipping reduction, or data-structure coupling are strictly quarantined:

| Quarantine ID | Problem Source & Title | Lang | Reason for Rejection / Quarantine |
| :--- | :--- | :--- | :--- |
| **`R-2A-01`** | **Luogu P3804 — `【模板】后缀自动机 (SAM)`** | `[ZH]` | Pure template verification: compute $\max_{u} (|\text{endpos}(u)| \cdot \text{len}(u))$ via a bare Link-Tree subtree sum. |
| **`R-2A-02`** | **Luogu P6139 — `【模板】广义后缀自动机 (广义 SAM)`** | `[ZH]` | Pure template verification: count $\sum (\text{len}(u) - \text{len}(\text{link}(u)))$ on a multi-string GSAM. |
| **`R-2A-03`** | **Library Checker — `Number of Substrings`** | `[EN]`/`[JA]` | Direct template check for distinct substring count $\sum (\text{len}(u) - \text{len}(\text{link}(u)))$. |
| **`R-2A-04`** | **SPOJ `SUBLEX` — Lexicographical Substring Search** | `[EN]` | Bare DAG path-count DP on SAM for $k$-th lexicographical distinct substring without multiplicity or range constraints. |
| **`R-2A-05`** | **SPOJ `LCS` — Longest Common Substring** | `[EN]` | Bare 2-string SAM walk tracking current matched length $\text{len}$. |
| **`R-2A-06`** | **SPOJ `NSUBSTR` — Substrings** | `[EN]` | Direct suffix-link subtree size aggregation pushed to $\text{ans}[\text{len}(u)]$. |
| **`R-2A-07`** | **LOJ 171 — `最长公共子串`** | `[ZH]` | Bare multi-string LCS on SAM without range or structural constraints. |
| **`R-2A-08`** | **Codeforces EDU — Suffix Automaton Step 1–4** | `[EN]` | Introductory educational drills testing basic SAM transitions and state counts. |
| **`R-2A-09`** | **AtCoder `ABC 362 G` — Count Substring Query** | `[JA]` | Direct SAM state lookup + $|\text{endpos}(u)|$ query for whole-string pattern occurrences. |
| **`R-2A-10`** | **HihoCoder 1441 / 1445 / 1449 / 1457 — SAM Series** | `[ZH]` | Textbook tutorial problems verifying basic SAM state definitions and Link Tree sums. |

---

### 15.2 Curated 36-Problem 4-Tier Difficulty Ladder (`Stepping Stone` $\to$ `Intermediate` $\to$ `Advanced` $\to$ `Mastery`)

Every accepted problem below requires a genuine structural reduction, combinatorial invariant, or data-structure coupling across `[EN]`, `[ZH]`, and `[JA]` sources.

---

#### Tier 1: Stepping Stone (SAM/GSAM Structural Anatomy, DAG/Link-Tree Dual DP & Trie-GSAM) — 9 Problems

##### 1. `[TJOI2015] 弦论 (String Theory)` (`Luogu P3975` / `LOJ 2102`) — `[ZH]`
- **Constraints**: $N \le 5 \times 10^5$, $T \in \{0, 1\}$, $K \le 10^9$. Find the $K$-th lexicographically smallest substring of $S$ (counting distinct substrings if $T=0$, or counting substrings with multiplicity if $T=1$).
- **4-Step Analysis**:
  1. *Signal*: $T=1$ counts occurrences with multiplicity across $O(N^2)$ total substrings; Suffix Array binary search becomes awkward while SAM unifies $T=0$ and $T=1$ by changing a single vertex weight!
  2. *Invariant*: Every distinct substring of $S$ corresponds to a unique directed path from the root $1$ in the **SAM transition DAG** (since $\text{SAM}(S)$ is a deterministic automaton where every state $u \ne 1$ is entered by paths spelling precisely the strings in $E(u)$? Wait—**Trap!** A path from root $1$ to $u$ spells *one specific string* in $E(u)$, and there are $\text{len}(u) - \text{len}(\text{link}(u))$ distinct paths from $1$ to $u$!). Therefore, in the DAG, **each visit to state $u$ along a path from the root represents exactly ONE string $w \in E(u)$**, whose weight is $w(u) = 1$ (if $T=0$) or $w(u) = |\text{endpos}_S(u)|$ (if $T=1$)!
  3. *Scratchpad*: First compute $w(u) = |\text{endpos}_S(u)|$ bottom-up on the Link Tree $\mathcal{T}_{\text{link}}$ (or $w(u) = 1$ for $T=0$), setting $w(1) = 0$. Second, compute $\text{sum}[u] = w(u) + \sum_{c \in \Sigma} \text{sum}[\delta(u, c)]$ bottom-up on the **transition DAG** (in decreasing order of $\text{len}(u)$). Walk greedily from $u = 1$ in alphabet order.
  4. *Pitfall*: Mixing up the Link Tree and the Transition DAG! $w(u) = |\text{endpos}(u)|$ is summed over the **Link Tree**, whereas $\text{sum}[u]$ is summed over the **Transition DAG**!

##### 2. `[HAOI2016] 找相同字符` (`Luogu P3181`) — `[ZH]`
- **Constraints**: $|S_1|, |S_2| \le 2 \times 10^5$. Count the number of pairs of identical substrings $(S_1[l_1..r_1], S_2[l_2..r_2])$, i.e., $\sum_{w \in \Sigma^+} \text{occ}(w, S_1) \cdot \text{occ}(w, S_2)$.
- **4-Step Analysis**:
  1. *Signal*: Summing over all $O(N^2)$ common substrings requires grouping them by equivalence classes across *both* strings simultaneously.
  2. *Invariant*: Build a Generalized SAM on $\{S_1, S_2\}$. For every state $u \in \text{GSAM}$, all strings $w \in E(u)$ have the exact same occurrence counts $\text{cnt}_1(u) = |\text{endpos}_{S_1}(u)|$ and $\text{cnt}_2(u) = |\text{endpos}_{S_2}(u)|$, and there are $\text{len}(u) - \text{len}(\text{link}(u))$ such strings.
  3. *Scratchpad*: Sum $\text{cnt}_1(u)$ and $\text{cnt}_2(u)$ bottom-up on $\mathcal{T}_{\text{link}}$, then output $\sum_{u \ne 1} (\text{len}(u) - \text{len}(\text{link}(u))) \cdot \text{cnt}_1(u) \cdot \text{cnt}_2(u)$ in $O(|S_1| + |S_2|)$ time.
  4. *Pitfall*: Zero-length clone states if online GSAM is built with naive single-string extension (though multiplying by $\text{len}(u) - \text{len}(\text{link}(u)) = 0$ happens to mask zero-length clones in pure sum queries, it corrupts parent links if not handled via Case 3!).

##### 3. `[AHOI2013] 差异 (Difference)` (`Luogu P4248`) — `[ZH]`
- **Constraints**: $N \le 5 \times 10^5$. Compute $\sum_{1 \le i < j \le N} \bigl((N - i + 1) + (N - j + 1) - 2\,\text{LCP}(S[i..N], S[j..N])\bigr)$.
- **4-Step Analysis**:
  1. *Signal*: Pairwise $\text{LCP}$ of suffixes $S[i..N]$ and $S[j..N]$ corresponds to LCA depth on the Suffix Tree $\text{ST}(S)$.
  2. *Invariant*: By Theorem 11.2, $\text{ST}(S) \cong \mathcal{T}_{\text{link}}(\text{SAM}(S^R))$. Each internal state $u \in \text{SAM}(S^R)$ has $\text{len}(u) = \text{LCP}$ of all pairs of suffixes in distinct child subtrees of $u$.
  3. *Scratchpad*: Build $\text{SAM}(S^R)$, mark prefix states with $\text{sz}[u] = 1$, and run a tree DP on $\mathcal{T}_{\text{link}}$ accumulating $\sum_{v \in \text{child}(u)} \text{sz}[u] \cdot \text{sz}[v] \cdot \text{len}(u)$.
  4. *Pitfall*: Building $\text{SAM}(S)$ instead of $\text{SAM}(S^R)$ computes $\sum \text{LCSuf}(S[1..i], S[1..j])$ (which happens to have the same global sum over all pairs, but fails whenever suffix weights depend on starting index $i$!).

##### 4. `[ZJOI2015] 诸神眷顾的幻想乡` (`Luogu P3346` / `LOJ 2130`) — `[ZH]`
- **Constraints**: An unrooted tree $T$ with $N \le 10^5$ nodes, alphabet $|\Sigma| \le 10$, and **at most $20$ leaves**. Count the number of distinct strings spelled by simple paths in $T$.
- **4-Step Analysis**:
  1. *Signal*: Every simple path in a tree is a substring of a path starting at one of the $\le 20$ leaves!
  2. *Invariant*: Rooting the tree at each of the $L \le 20$ leaves produces $L$ tries of total size $\le L \cdot N \le 2 \times 10^6$. A string appears on a simple path in $T$ iff it is a substring of a root-to-node path in one of these $L$ tries, which is accepted by the Generalized SAM of the $L$ tries.
  3. *Scratchpad*: For each leaf $r$, run a DFS/BFS on $T$ rooted at $r$, calling `sam_node[v] = extend_gsam(sam_node[parent[v]], color[v])`. Sum $\text{len}(u) - \text{len}(\text{link}(u))$ over all GSAM states in $O(L N |\Sigma|)$ time.
  4. *Pitfall*: Passing `last` from the previous DFS visit instead of `sam_node[parent[v]]` when branching in the tree!

##### 5. `CF 235C — Cyclical Quest` — `[EN]`
- **Constraints**: $|S| \le 10^6$, $Q$ query strings $x_i$ with $\sum |x_i| \le 10^6$. For each $x_i$, count how many substrings of $S$ are isomorphic to a **cyclic shift** of $x_i$.
- **4-Step Analysis**:
  1. *Signal*: A cyclic shift of $x$ of length $m = |x|$ is a substring of $x x[1..m-1]$ of length exactly $m$.
  2. *Invariant*: Walk $x x[1..m-1]$ on $\text{SAM}(S)$ maintaining current state $u$ and matched length $L$. Whenever we slide the left endpoint of the window so that $L > m$, we decrement $L$ (or set $L = m$) and if $L \le \text{len}(\text{link}(u))$, step $u \leftarrow \text{link}(u)$. Whenever $L \ge m$, state $u$ contains the current cyclic shift of length $m$, contributing $|\text{endpos}_S(u)|$.
  3. *Scratchpad*: Because $x$ may be periodic (e.g. $x = \texttt{abab}$), two cyclic shifts can be identical and land at the same state $u$. Stamp `vis[u] = query_id` so each state $u$ is added at most once per query!
  4. *Pitfall*: Forgetting to deduplicate `vis[u]` when $x = w^k$ is a periodic power overcounts by a factor of $k$.

##### 6. `CF 427D — Match & Catch` — `[EN]`
- **Constraints**: $|S_1|, |S_2| \le 5000$ (solvable in $O(|S_1| + |S_2|)$ via GSAM). Find the shortest substring that occurs **uniquely** (exactly once) in $S_1$ and **uniquely** in $S_2$.
- **4-Step Analysis**:
  1. *Signal*: We need a substring $w$ with $\text{occ}(w, S_1) = 1$ and $\text{occ}(w, S_2) = 1$ of minimum length $|w|$.
  2. *Invariant*: In $\text{GSAM}(S_1, S_2)$, all strings $w \in E(u)$ have identical $(\text{cnt}_1(u), \text{cnt}_2(u))$. The shortest string in $E(u)$ has length $\text{minlen}(u) = \text{len}(\text{link}(u)) + 1$.
  3. *Scratchpad*: Answer is $\min_{\text{cnt}_1(u) = 1 \land \text{cnt}_2(u) = 1} (\text{len}(\text{link}(u)) + 1)$.
  4. *Pitfall*: Taking $\text{len}(u)$ instead of $\text{len}(\text{link}(u)) + 1$ returns the longest string in the equivalence class instead of the shortest!

##### 7. `CF 802I — Fake News (hard)` — `[EN]`
- **Constraints**: $|S| \le 10^5$. Compute $\sum_{w \text{ distinct}} \text{occ}(w, S)^2$.
- **4-Step Analysis**:
  1. *Signal*: Every state $u \in \text{SAM}(S)$ groups $\text{len}(u) - \text{len}(\text{link}(u))$ distinct substrings that each occur $|\text{endpos}_S(u)|$ times.
  2. *Invariant*: $\sum_{w} \text{occ}(w, S)^2 = \sum_{u \ne 1} (\text{len}(u) - \text{len}(\text{link}(u))) \cdot |\text{endpos}_S(u)|^2$.
  3. *Scratchpad*: $O(N)$ bottom-up Link-Tree aggregation.
  4. *Pitfall*: Clone nodes get initial $\text{cnt}[u] = 0$, whereas prefix nodes get $\text{cnt}[u] = 1$. Initializing $\text{cnt}[\text{clone}] = 1$ double-counts occurrences!

##### 8. `CF 128B — String` — `[EN]`
- **Constraints**: $|S| \le 10^5$, $K \le \binom{|S|+1}{2}$. Find the $K$-th lexicographically smallest substring of $S$ (counting multiple occurrences as distinct positions).
- **4-Step Analysis**: Identical to `[TJOI2015] 弦论` ($T=1$) via SAM Link-Tree $\text{endpos}$ size + DAG path DP in $O(N |\Sigma|)$.

##### 9. `[JSOI2012] 分离与合体 / Substring Coverage` (`CF 452E — Three Strings`) — `[EN]`/`[ZH]`
- **Constraints**: Three strings $S_1, S_2, S_3$ ($\sum |S_i| \le 3 \times 10^5$). For every length $L \in [1, \min(|S_1|, |S_2|, |S_3|)]$, compute the number of common substrings of length $L$ weighted by $\text{occ}(w, S_1) \cdot \text{occ}(w, S_2) \cdot \text{occ}(w, S_3) \pmod{10^9+7}$.
- **4-Step Analysis**:
  1. *Signal*: Each GSAM state $u$ contributes $\text{prod}(u) = \text{cnt}_1(u) \text{cnt}_2(u) \text{cnt}_3(u)$ to **every length** $L \in [\text{len}(\text{link}(u)) + 1, \text{len}(u)]$.
  2. *Invariant*: A range addition of $\text{prod}(u)$ on $[\text{len}(\text{link}(u)) + 1, \text{len}(u)]$ for each state $u \in \text{GSAM}(S_1, S_2, S_3)$ computes the exact answer for all $L$ simultaneously via a difference array!
  3. *Scratchpad*: Build GSAM, compute $\text{cnt}_{1,2,3}(u)$ on $\mathcal{T}_{\text{link}}$, add $\text{prod}(u)$ to `diff[len(link(u)) + 1]` and subtract from `diff[len(u) + 1]`, then prefix sum in $O(N)$.
  4. *Pitfall*: Using `$#$`-concatenation without capping $\text{len}(u)$ at the distance to the nearest sentinel allows cross-sentinel substrings. Building a proper 3-Case GSAM eliminates sentinels completely.

---

#### Tier 2: Intermediate (GSAM + Monotonic Queue / Binary Search DP, Endpos Merging Foundations & Link-Tree Binary Lifting) — 9 Problems

##### 10. `[CTSC2012] 熟悉的文章 (Familiar Article)` (`Luogu P4022` / `LOJ 2255`) — `[ZH]`
- **Constraints**: $M$ dictionary strings ($\sum |D_i| \le 1.1 \times 10^6$) and $Q$ query articles $T$ ($\sum |T| \le 1.1 \times 10^6$). An article $T$ is "$L$-familiar" if we can select disjoint substrings of $T$, each of length $\ge L$ and occurring in the dictionary, covering at least $90\%$ of $|T|$. Find the maximum $L$ for each $T$.
- **4-Step Analysis**:
  1. *Signal*: Monotonic binary search on $L$. For a fixed $L$, a substring $T[j+1..i]$ ($i - j \ge L$) is valid iff it occurs in the dictionary, which is equivalent to $i - j \le \text{lim}[i]$, where $\text{lim}[i]$ is the longest suffix of $T[1..i]$ occurring in the dictionary!
  2. *Invariant*: Precompute $\text{lim}[i]$ in $O(|T|)$ by walking $T$ on the **GSAM of the dictionary**. Then for fixed $L$, valid transitions for $j \to i$ satisfy $i - \text{lim}[i] \le j \le i - L$:
     $$dp[i] = \max\Bigl(dp[i-1], \; \max_{i - \text{lim}[i] \le j \le i - L} (dp[j] + i - j)\Bigr) = \max\Bigl(dp[i-1], \; i + \max_{i - \text{lim}[i] \le j \le i - L} (dp[j] - j)\Bigr).$$
  3. *Scratchpad*: Since $i - \text{lim}[i]$ is **non-decreasing** (dropping the first character of the longest matched suffix at $i-1$ leaves a valid dictionary substring at $i$, so $\text{lim}[i] \ge \text{lim}[i-1] + 1 \iff i - \text{lim}[i] \le (i-1) - \text{lim}[i-1]$!), the window $[i - \text{lim}[i], i - L]$ slides monotonically to the right and is solved in $O(|T|)$ per binary search step via a monotonic deque!
  4. *Pitfall*: Not noticing that $i - \text{lim}[i]$ is monotonically non-decreasing leads to an unnecessary $O(|T| \log^2 |T|)$ Segment Tree inside the binary search.

##### 11. `CF 616F — Expensive Strings` — `[EN]`
- **Constraints**: $n$ strings $t_1, \dots, t_n$ ($\sum |t_i| \le 5 \times 10^5$) with costs $c_1, \dots, c_n \in [-10^7, 10^7]$. Maximize $|w| \cdot \sum_{i=1}^n c_i \cdot \text{occ}(w, t_i)$ over all nonempty strings $w$.
- **4-Step Analysis**:
  1. *Signal*: Weight of $w \in E(u)$ is $|w| \cdot W(u)$, where $W(u) = \sum_{i=1}^n c_i |\text{endpos}_{t_i}(u)|$ is constant across all $w \in E(u)$.
  2. *Invariant*: Since $|w| > 0$, if $W(u) > 0$, we maximize $|w| \cdot W(u)$ by choosing the **longest** string in $E(u)$, i.e., $|w| = \text{len}(u)$! (If $W(u) \le 0$, the product is $\le 0$).
  3. *Scratchpad*: Build 3-Case GSAM on $\{t_1, \dots, t_n\}$. At each prefix state of $t_i$, add $c_i$ to `weight[u]`. Sum `weight[u]` bottom-up on $\mathcal{T}_{\text{link}}$, and return $\max_{u \ne 1} (\text{len}(u) \cdot \text{weight}[u])$.
  4. *Pitfall*: Using `$#$`-concatenation requires clamping $\text{len}(u)$ to avoid crossing `$#$`, whereas 3-Case GSAM handles $\text{len}(u)$ natively in $O(\sum |t_i|)$.

##### 12. `CF 666E — Forensic Examination` — `[EN]`
- **Constraints**: $|S| \le 5 \times 10^5$, $\sum |T_k| \le 5 \times 10^4$, $Q \le 5 \times 10^5$.
- **4-Step Analysis**: Complete derivation in **Iteration 12, Landmark 4** (GSAM + Persistent Segment Tree Merge over dictionary indices $k \in [1, m]$ + Link-Tree binary lifting).

##### 13. `[HEOI2016 / TJOI2016] 字符串` (`Luogu P4094`) — `[ZH]`
- **Constraints**: $N, Q \le 10^5$.
- **4-Step Analysis**: Complete derivation in **Iteration 12, Landmark 2** (Binary search on $L$ + Link-Tree binary lifting + Endpos Segment Tree Merge clipping on $[a + L - 1, b]$).

##### 14. `CF 204E — Little Elephant and Strings` — `[EN]`
- **Constraints**: $n$ strings $s_1, \dots, s_n$ ($\sum |s_i| \le 10^5$) and threshold $k$. For each $s_i$, count how many substrings of $s_i$ (with multiplicity) appear in at least $k$ distinct strings among $s_1, \dots, s_n$.
- **4-Step Analysis**:
  1. *Signal*: Each GSAM state $u$ needs the number of **distinct string IDs** $j \in \{1, \dots, n\}$ present in its Link-Tree subtree.
  2. *Invariant*: Color each prefix state of $s_j$ with color $j$. The number of distinct colors in the subtree of $u$ in $\mathcal{T}_{\text{link}}$ can be computed in $O(N \log N)$ via Segment Tree Merging (or in $O(N)$ via offline LCA subtraction `cnt[u]++, cnt[LCA(prev_u, u)]--` sorted by DFS order!).
  3. *Scratchpad*: On $\mathcal{T}_{\text{link}}$, push down the highest ancestor $v$ of $u$ that has $\text{distinct\_colors}(v) \ge k$. For each prefix $s_i[1..r]$ at GSAM state $u$, add $\text{len}(\text{valid\_anc}(u))$ to the answer for $s_i$.
  4. *Pitfall*: Walk $s_i$ on the GSAM to locate its prefix states rather than assuming `last` was not split later during subsequent strings' insertions!

##### 15. `CF 453E / CF 873F — Forbidden Indices` — `[EN]`
- **Constraints**: $N \le 2 \times 10^5$, binary mask of forbidden end positions. Maximize $|w| \cdot (\text{unforbidden occurrences of } w)$.
- **4-Step Analysis**: Build $\text{SAM}(S)$, initialize `cnt[pos[i]] = (forbidden[i] == '0' ? 1 : 0)`, sum `cnt` bottom-up on $\mathcal{T}_{\text{link}}$, and take $\max_{u \ne 1} (\text{len}(u) \cdot \text{cnt}[u])$.

##### 16. `[BZOJ 3238 / AHOI2013] 相似的子串` & `[JSOI2016] 独特的基因` — `[ZH]`
- **Constraints**: $N \le 10^5$. Maintain closest pairs of occurrences in $\text{endpos}(u)$ during Segment Tree Merging or DSU-on-Tree over $\mathcal{T}_{\text{link}}$.
- **4-Step Analysis**:
  1. *Signal*: For each state $u \in \text{SAM}(S)$, adjacent elements $e_1 < e_2$ in sorted $\text{endpos}_S(u)$ have common suffix length $\text{len}(u)$.
  2. *Invariant*: When merging $\text{endpos}$ sets from children of $u$ on $\mathcal{T}_{\text{link}}$ via `std::set`启发式合并 (small-to-large) or Segment Tree Merge, each inserted element creates at most $2$ new adjacent pairs $(pred, x)$ and $(x, succ)$ with LCP / LCSuf equal to $\text{len}(u)$.
  3. *Scratchpad*: Collect the $O(N \log N)$ dominant pairs $(e_1, e_2, \text{len}(u))$ and answer range queries offline via 2D Fenwick sweep.
  4. *Pitfall*: Keeping all pairs instead of only adjacent pairs $(pred, x)$ and $(x, succ)$ during small-to-large merge blows up to $O(N^2)$.

##### 17. `[SDOI2016] 生成魔咒 (Generating Spells)` (`Luogu P4070` / `LOJ 2033`) — `[ZH]`
- **Constraints**: $N \le 10^5$, alphabet $|\Sigma| \le 10^9$. Characters are appended one by one; after each append, output the number of distinct substrings in the current prefix.
- **4-Step Analysis**:
  1. *Signal*: Large alphabet $|\Sigma| \le 10^9$ requires `std::map<int, int>` for DFA transitions $\delta(u, c)$, and online distinct count update per character.
  2. *Invariant*: When extending by $c$ creates state `cur` (and possibly splits $q \to \text{clone}$), the split $q \to \text{clone}$ merely partitions $[\text{len}(\text{link}(q))+1, \text{len}(q)]$ into $[\text{len}(\text{link}(q))+1, \text{len}(\text{clone})]$ and $[\text{len}(\text{clone})+1, \text{len}(q)]$, leaving the sum of interval lengths **unchanged**! Only the new leaf `cur` adds $\text{len}(\text{cur}) - \text{len}(\text{link}(\text{cur}))$ new distinct substrings!
  3. *Scratchpad*: Maintain running sum `ans += len[cur] - len[link[cur]]` after each `extend(c)` in $O(N \log |\Sigma|)$ time.
  4. *Pitfall*: Forgetting to copy the `std::map` transitions when cloning $q \to \text{clone}$.

##### 18. `[BJWC2010 / Luogu P4081] 外星联络 / Different Substrings on Trie` (`AtCoder ABC 284 F` / `ARC 151 D` variants) — `[JA]`/`[ZH]`
- **Constraints**: $V \le 10^5$ Trie nodes, query $k$-th lexicographical path substring on a Trie.
- **4-Step Analysis**: Offline BFS GSAM construction on the Trie + Link-Tree subtree sizes + DAG lexicographical walk.

---

#### Tier 3: Advanced (Endpos Clipping Mastery, Top-Len Link-Tree DP, Prefix-Suffix Graph DAG & LCT Dynamic SAM) — 9 Problems

##### 19. `[NOI2018] 你的名字 (Your Name)` (`Luogu P4770` / `LOJ 2720`) — `[ZH]`
- **Constraints**: $|S| \le 5 \times 10^5$, $\sum |T| \le 10^6$.
- **4-Step Analysis**: Complete derivation in **Iteration 12, Landmark 1** (SAM + Persistent Segment Tree Merge on $\text{endpos}_S$ + Clipped Two-Pointer Walk for $\text{lim}[i]$ + $\text{SAM}(T)$ deduplication).

##### 20. `CF 1037H — Security` — `[EN]`
- **Constraints**: $|S| \le 10^5$, $\sum |T| \le 2 \times 10^5$.
- **4-Step Analysis**: Complete derivation in **Iteration 12, Landmark 3** (SAM + Persistent Segment Tree Merge + Greedy Reverse-Prefix Backtracking with Clipped Interval $[l + i, r]$).

##### 21. `CF 700E — Cool Slogans` — `[EN]`
- **Constraints**: $N \le 2 \times 10^5$.
- **4-Step Analysis**: Complete derivation in **Iteration 12, Landmark 5** (Top-Len Sufficiency Lemma + Link-Tree Top-Down DP + Endpos Clipping in $[\text{pos}(u) - \text{len}(u) + \text{len}(v), \text{pos}(u) - 1]$).

##### 22. `[十二省联考 2019] 字符串问题` (`Luogu P5284` / `LOJ 3052`) — `[ZH]`
- **Constraints**: $N, n_a, n_b, m \le 2 \times 10^5$.
- **4-Step Analysis**: Complete derivation in **Iteration 14.1** (Reversed SAM $\mathcal{T}_{\text{link}}$ + Binary Lifting + Intra-Node Length-Sorted Prefix-Chain DAG + Kahn Topological Sort DP).

##### 23. `[BZOJ 2555] SubString` — `[ZH]`
- **Constraints**: Online appends of total length $\le 6 \times 10^5$ and online pattern occurrence queries of total length $\le 3 \times 10^6$ (XOR-encrypted with `mask`).
- **4-Step Analysis**: Complete derivation in **Iteration 13, Contract 13.2** (Dynamic SAM + Link-Cut Tree maintaining $\mathcal{T}_{\text{link}}$ under edge splits $q \to \text{clone}$ and root-to-`cur` path $+1$ updates).

##### 24. `CF 1063F — String Journey` — `[EN]`
- **Constraints**: $N \le 5 \times 10^5$. Find the maximum $k$ such that $S$ contains **non-overlapping** substrings $s_k, s_{k-1}, \dots, s_1$ in left-to-right order where $|s_i| = i$ and each $s_{i-1}$ is a substring of $s_i$.
- **4-Step Analysis**:
  1. *Signal*: A substring of length $i$ containing a substring of length $i-1$ means $s_{i-1}$ is either the **prefix** $s_i[1..i-1]$ or the **suffix** $s_i[2..i]$ of $s_i$! And we can always shrink lengths so that $|s_i| = i$ exactly ($k \le \sqrt{2N} \approx 1000$).
  2. *Invariant*: Working backwards from right to left (or on $\text{SAM}(S^R)$), let $dp[i]$ be the maximum valid chain length starting at position $i$ ($s_{dp[i]} = S[i .. i + dp[i] - 1]$). By shrinking the left endpoint $i-1 \to i$, $dp[i] \le dp[i-1] + 1$! Thus as $i$ decreases from $N$ down to $1$, we can start with candidate $L = dp[i+1] + 1$ and decrement $L$, while pushing finalized $dp[i + L]$ values into a Segment Tree over the Euler tour (`dfn` interval) of $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$!
  3. *Scratchpad*: To check if $L$ is valid at $i$, either $S[i..i+L-2]$ or $S[i+1..i+L-1]$ must appear at some starting position $j \ge i + L$ with $dp[j] \ge L - 1$. Locate the states $u_1 = \text{state}_{S^R}(S[i..i+L-2])$ and $u_2 = \text{state}_{S^R}(S[i+1..i+L-1])$ via Link-Tree binary lifting, and query the maximum of $dp[j]$ in the subtree `dfn` interval of $u_1$ and $u_2$!
  4. *Pitfall*:Inserting $dp[j]$ into the Segment Tree before $j \ge i + L$ would allow overlapping substrings $s_L$ and $s_{L-1}$. Pushing $dp[i + L]$ into the Segment Tree exactly when $L$ is decremented (or when $i$ steps left) guarantees non-overlapping positions in $O(N \log N)$ time!

##### 25. `CF 653F — Paper task` — `[EN]`
- **Constraints**: Bracket string $S$ of length $N \le 5 \times 10^5$. Count the number of **distinct** regular bracket substrings of $S$.
- **4-Step Analysis**:
  1. *Signal*: Every state $u \in \text{SAM}(S)$ represents substrings ending at $r = \text{pos}(u)$ with lengths $L \in [\text{len}(\text{link}(u)) + 1, \text{len}(u)]$, i.e., starting positions $l \in [r - \text{len}(u) + 1, r - \text{len}(\text{link}(u))]$.
  2. *Invariant*: Let $P[k]$ be the prefix balance sum of $S[1..k]$ (`(` $= +1$, `)` $= -1$). A substring $S[l..r]$ is a balanced bracket string iff $P[l-1] = P[r]$ and $\min_{l \le k \le r} P[k] \ge P[r]$.
  3. *Scratchpad*: For each state $u \ne 1$ with representative right endpoint $r = \text{pos}(u)$, find the rightmost index $k_{\text{bad}} < r$ with $P[k_{\text{bad}}] < P[r]$ (via a monotonic stack). Then valid left endpoints $l-1$ must lie in $\bigl[\max(k_{\text{bad}} + 1, \, r - \text{len}(u)), \; r - \text{len}(\text{link}(u)) - 1\bigr]$ and satisfy $P[l-1] = P[r]$. Count them in $O(\log N)$ via `std::lower_bound` on pre-bucketed indices of each prefix sum value!
  4. *Pitfall*: Off-by-one between the 1-based substring start $l$ and the prefix-sum index $l - 1$.

##### 26. `[BJOI2020] 封印 (Seal)` (`Luogu P6640` / `LOJ 3298`) — `[ZH]`
- **Constraints**: $|S|, |T| \le 2 \times 10^5$, $Q \le 2 \times 10^5$ queries $(l, r)$. Find the longest common substring of $S[l..r]$ and the whole string $T$.
- **4-Step Analysis**:
  1. *Signal*: Unlike `[NOI2018] 你的名字` where $T$ changes per query and $S[l..r]$ is the reference, here $T$ is **fixed** and $S[l..r]$ is a subsegment of a fixed string $S$!
  2. *Invariant*: Walk $S$ on $\text{SAM}(T)$ once in $O(|S|)$ time to compute $\text{lim}[i]$ = length of the longest suffix of $S[1..i]$ that occurs in $T$. Then for any $i \in [l, r]$, the longest suffix of $S[1..i]$ that fits inside $S[l..r]$ and occurs in $T$ has length $\min(i - l + 1, \, \text{lim}[i])$.
  3. *Scratchpad*: We want $\max_{l \le i \le r} \min(i - l + 1, \text{lim}[i])$. Since $i - \text{lim}[i] + 1$ is monotonically non-decreasing, binary search the split point $m \in [l, r]$ where $i - \text{lim}[i] + 1 \le l$ (for $i \le m$, $\min = i - l + 1$, maximized at $i = m$ giving $m - l + 1$; for $i > m$, $\min = \text{lim}[i]$, queried via Static RMQ on $\text{lim}[m+1..r]$ in $O(1)$!). Total time: $O(|S| + |T| + Q \log |S|)$ without even needing Segment Tree Merging!
  4. *Pitfall*: Over-engineering with Segment Tree Merging on $\text{SAM}(S)$ when $T$ is fixed! When one string is queried by intervals $[l, r]$ and the other string $T$ is fixed, precomputing $\text{lim}[i]$ against $\text{SAM}(T)$ + RMQ solves the problem in $O(N + Q \log N)$.

##### 27. `AtCoder AGC 047 B — First Second` & `ARC 151 E — Keep Being Substring` — `[JA]`
- **Constraints**: $N \le 2 \times 10^5, \sum |S_i| \le 10^6$. Suffix equivalence + single-character prefix check via Reversed Trie / GSAM Link Tree.
- **4-Step Analysis**:
  1. *Signal*: In `AGC 047 B`, operation deletes the first or second character, meaning $S_i$ can be reduced to $S_j$ iff $S_j[2..|S_j|]$ is a suffix of $S_i$ and the first character $S_j[1]$ appears in the remaining prefix of $S_i$!
  2. *Invariant*: On $\text{SAM}(S_i)$ (or reversed Trie), tracking character presence masks along suffixes allows $O(\sum |S_i| |\Sigma|)$ counting of valid pairs.

---

#### Tier 4: Mastery (LCT `access` Color-Chain Sweeping, Weighted 2D Substring Range Queries & Frontier Synthesis) — 9 Problems

##### 28. `Luogu P6292 — 区间本质不同子串个数 (Distinct Substrings in Range)` (`UOJ / QOJ Substring Range Distinct`) — `[ZH]`
- **Constraints**: $N \le 10^5, Q \le 2 \times 10^5$. For each query $(l, r)$, output the number of distinct substrings in $S[l..r]$.
- **4-Step Analysis**: Complete derivation in **Iteration 13, Theorem 13.1 & Contract 13.3** (SAM + LCT `access(pos[r])` color-chain sweeping + Segment Tree / Fenwick Tree range arithmetic updates on $[p_{\text{old}} - L_{\max} + 1, p_{\text{old}} - L_{\min} + 1]$ in $O(N \log^2 N + Q \log N)$ time).

##### 29. `[SDOI2017] 相关分析 / Substring Range Weighted Queries` (`LOJ 2269` / `[HNCPC / National Team]` variants) & `UOJ 577 — 打击复读 (Stop Repeating)` — `[ZH]`
- **Constraints**: $N \le 5 \times 10^5$, $Q \le 5 \times 10^5$. Left-weighted and right-weighted sum of occurrences of all substrings in $S$ under updates.
- **4-Step Analysis**:
  1. *Signal*: Each state $u \in \text{SAM}(S)$ contributes to substring weights via the sum of left-weights of start positions of strings in $E(u)$ multiplied by the sum of right-weights of $\text{endpos}_S(u)$.
  2. *Invariant*: By Theorem 11.2, the strings in $E(u)$ correspond to a single compacted edge in $\text{ST}(S^R)$, meaning their starting positions for a fixed representative right-endpoint $e = \text{pos}(u)$ form a contiguous interval $[e - \text{len}(u) + 1, e - \text{len}(\text{link}(u))]$.
  3. *Scratchpad*: Maintain Link-Tree subtree sums of right-weights and prefix sums of left-weights in $O(N + Q)$ time.
  4. *Pitfall*: Recomputing interval sums per update instead of separating the left-weight factor (which depends only on the static SAM state $u$) from the right-weight factor.

##### 30. `CF 1098F — Ж-function` — `[EN]`
- **Constraints**: $N, Q \le 2 \times 10^5$. Compute $\sum_{i=l}^r \text{LCP}(S[i..r], S[l..r])$.
- **4-Step Analysis**: Complete derivation in **Iteration 14.2** (Reversed SAM Link Tree $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$ + Heavy-Light Decomposition / Centroid Decomposition + 2D Fenwick Tree splitting $\min(r - i + 1, \text{len}(u))$ at $i \le r - \text{len}(u) + 1$).

##### 31. `[NOI2015] 品酒大会 (Wine Tasting)` (`Luogu P2178` / `LOJ 2133`) — `[ZH]`
- **Constraints**: $N \le 3 \times 10^5$, node weights $a_i \in [-10^9, 10^9]$. For each $r \in [0, N-1]$, count pairs $(i, j)$ with $\text{LCP}(S[i..N], S[j..N]) \ge r$ and find the maximum product $a_i a_j$ among such pairs.
- **4-Step Analysis**:
  1. *Signal*: $a_i$ can be **negative**, so maximum product $a_i a_j$ requires maintaining both $\max a_i$ and $\min a_i$ in each subtree!
  2. *Invariant*: On $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$, each state $u$ with $\text{len}(u) = L$ merges its child subtrees; any pair $(i, j)$ separated at $u$ has $\text{LCP}(S[i..N], S[j..N]) = \text{len}(u)$ and is valid for all $r \le \text{len}(u)$.
  3. *Scratchpad*: Bottom-up tree DP on $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$ maintaining $(\text{sz}, \max_+, \min_-)$ per state, followed by a suffix sum/max from $r = N-1$ down to $0$ in $O(N)$ time.
  4. *Pitfall*: Initializing $\text{max\_prod}[r] = 0$ instead of $-\infty$ when all valid products are negative!

##### 32. `CF 1043G — Speckled Band` (Synthesis Preview: SAM/IPM + Runs / Border Clipping) — `[EN]`
- **Constraints**: $N, Q \le 2 \times 10^5$. Find the minimum number of distinct substrings in a partition of $S[l..r]$ (answer is always $\in \{-1, 1, 2, 3, 4\}$!).
- **4-Step Analysis**: Combines Periodicity/Runs + Substring Border/Endpos Occurrence Queries inside $S[l..r]$. (Flagged as a primary **Synthesis Reserve (`Syn`)** bridging Wave 1B, Wave 2A, and Wave 2B).

##### 33. `[ZJOI2019] 语言 (Language)` (`Luogu P5327` / `LOJ 3093`) — `[ZH]`
- **Constraints**: Tree $N, M \le 10^5$. Segment Tree Merging of virtual tree sizes over DFS order. (Included for structural mastery of persistent/destructive Segment Tree Merging invariants used identically on SAM Link Trees).

##### 34. `Universal Cup / QOJ — Range Shortest Unique Substring & Range $K$-th Substring` (`QOJ` / `UCup` Grandmaster Series) — `[EN]`/`[ZH]`
- **Constraints**: $N, Q \le 10^5$. Given queries $(l, r)$, find the shortest (or longest repeated) substring of $S[l..r]$, or the $k$-th lexicographical distinct substring of $S[l..r]$.
- **4-Step Analysis**:
  1. *Signal*: In $S[l..r]$, a substring $w \in E(u)$ occurs **at least twice** inside $S[l..r]$ iff the **second-largest** element $e_2 \in \text{endpos}_S(u) \cap [1, r]$ satisfies $e_2 - |w| + 1 \ge l \iff |w| \le e_2 - l + 1$.
  2. *Invariant*: Just as LCT `access(pos[r])` maintains the largest occurrence $e_1 = \text{last}_r(u)$ for distinct substrings, we can track the **second-largest** occurrence $e_2(u) \le r$ (via LCT `access` or small-to-large adjacent pair pairs $(e_1, e_2)$ on $\mathcal{T}_{\text{link}}$) to answer offline range longest-repeated-substring and shortest-unique-substring queries in $O((N + Q) \log^2 N)$ time!

##### 35. `[Code+#3] 白金元首与莫斯科` & `Luogu P5284` 2-SAT Variant — `[ZH]`
- **Constraints**: $N, M \le 10^5$. Boolean implications on prefixes/suffixes of substrings $S[l_i..r_i]$.
- **4-Step Analysis**: Reversed SAM Link-Tree binary lifting + Intra-node length sorting + HLD interval 2-SAT clauses in $O(N \log^2 N)$.

##### 36. `AtCoder AGC 057 D / ABC 272 Ex / JOI String Range Queries` (`noshi91` & `maspypy` SAM + LCT Treatises) — `[JA]`
- **Constraints**: $N, Q \le 10^5$. Offline substring range queries using `noshi91`'s LCT `access` color-chain decomposition on SAM.
- **4-Step Analysis**: Directly instantiates Theorem 13.1, demonstrating the cross-community convergence between Chinese `树点涂色 + SAM` (`[SDOI2017]` / `Luogu P6292`) and Japanese `SAM + LCT access` range query libraries (`noshi91` / `maspypy`).

---

### 15.3 Wave 2A Multilingual Bibliography & Citations Seed (`[EN]` / `[ZH]` / `[JA]`)

1. **[Blumer et al. 1985] `[EN]`**: A. Blumer, J. Blumer, D. Haussler, A. Ehrenfeucht, M. T. Chen, and J. Seiferas, *"The smallest automaton recognizing the subwords of a text"*, Theoretical Computer Science, 40:31–55, 1985. (Original linear-time DAWG / SAM construction, $\le 2N-1$ states and $\le 3N-4$ transitions, and Suffix Tree reversal duality).
2. **[Crochemore & Rytter 2002] `[EN]`**: M. Crochemore and W. Rytter, *Jewels of Stringology*, World Scientific, 2002. (Canonical treatment of Compact DAWGs, Suffix Automata, and Factor Automata).
3. **[ChenLijie 2012 — 国家集训队论文] `[ZH]`**: 陈立杰 (Chen Lijie / WJMZBMR), *《后缀自动机及其应用》(Suffix Automaton and Its Applications)*, NOI National Team Lecture Notes, 2012. (Introduced SAM and Dynamic SAM + LCT `[BZOJ 2555]` to Chinese competitive programming).
4. **[LiuYan 2015 / OI-Wiki GSAM Treatise] `[ZH]`**: 刘研 / 辰星凌 (Chen Xingling), *《广义后缀自动机 (Generalized Suffix Automaton) 原理与时空复杂度分析》*, Chinese National Team & OI-Wiki Technical Monograph. (Rigorous analysis of Online 3-Case GSAM vs. Offline Trie BFS GSAM and the zero-length clone pitfall).
5. **[NOI2018 & Twelve Provinces 2019 Official Editorials] `[ZH]`**: CCF NOI Scientific Committee, *《NOI 2018 你的名字 命题报告》* & *《十二省联考 2019 字符串问题 题解》*, 2018–2019. (Canonical references for SAM + Persistent Segment Tree Merging with $[l + L - 1, r]$ clipping and Intra-Node Sorted Prefix-Suffix DAGs).
6. **[noshi91 & maspypy SAM+LCT Treatises] `[JA]`**: `noshi91` & `maspypy`, *「Suffix Automaton 上の Link-Cut Tree による部分文字列クエリ処理」 (Substring Range Queries via LCT on Suffix Automaton)*, Japanese Competitive Programming Treatises, 2020–2023.

---

### 15.4 Non-Standard Algorithmic Contracts & Diagnostic Decision Matrix

Per `AGENTS.md`, standard single-string SAM construction and standard Segment Tree / LCT templates are omitted. Below are the **four non-standard coupling contracts** where subtle boundary bugs occur most frequently in contest implementations:

#### Contract A: The 3-Case Online / Trie Generalized SAM Extension (`extend_gsam`)
- **Preconditions**: `p` is an existing valid state in the GSAM ($p \ge 1$), and $c \in [0, |\Sigma|-1]$ is the character extending $\text{longest}(p)$.
- **Postconditions**: Returns the unique state $u \in \text{GSAM}$ whose $\text{longest}(u) = \text{longest}(p) + c$, guaranteeing $\text{len}(x) > \text{len}(\text{link}(x))$ for every state $x > 1$ (zero-length clone free).

```cpp
int extend_gsam(int p, int c) {
    // Case 2 & Case 3: Transition delta(p, c) ALREADY EXISTS!
    if (ch[p][c]) {
        int q = ch[p][c];
        if (len[q] == len[p] + 1) return q; // Case 2: Exact length match
        // Case 3: Split q -> clone WITHOUT creating a separate `cur` node
        int clone = ++tot;
        len[clone] = len[p] + 1;
        memcpy(ch[clone], ch[q], sizeof(ch[q]));
        link[clone] = link[q];
        while (p && ch[p][c] == q) {
            ch[p][c] = clone;
            p = link[p];
        }
        link[q] = clone;
        return clone;
    }
    // Case 1: Standard SAM extension when delta(p, c) == 0
    int cur = ++tot;
    len[cur] = len[p] + 1;
    while (p && !ch[p][c]) {
        ch[p][c] = cur;
        p = link[p];
    }
    if (!p) {
        link[cur] = 1;
    } else {
        int q = ch[p][c];
        if (len[q] == len[p] + 1) {
            link[cur] = q;
        } else {
            int clone = ++tot;
            len[clone] = len[p] + 1;
            memcpy(ch[clone], ch[q], sizeof(ch[q]));
            link[clone] = link[q];
            while (p && ch[p][c] == q) {
                ch[p][c] = clone;
                p = link[p];
            }
            link[q] = link[cur] = clone;
        }
    }
    return cur;
}
```

#### Contract B: Clipped Two-Pointer Walk on $\text{SAM}(S)$ with Persistent Endpos Merge (`[NOI2018] 你的名字`)
- **Invariant**: At step $i$, $(u, L)$ satisfies $T[i-L+1..i] \in E(u)$ and $\text{endpos}_S(u) \cap [l + L - 1, r] \ne \emptyset$, with $L = \text{lim}[i]$ maximal.

```cpp
// Inside query(T, l, r): compute lim[1..|T|]
int u = 1, L = 0;
for (int i = 1; i <= (int)T.size(); ++i) {
    int c = T[i - 1] - 'a';
    while (true) {
        int w = ch[u][c];
        // Check if transition exists AND has an occurrence of length L+1 inside S[l..r]
        if (w && query_segtree(rt[w], 1, n, l + L, r)) {
            u = w;
            ++L;
            break;
        }
        if (L == 0) break;
        --L;
        if (L == len[link[u]]) u = link[u];
    }
    lim[i] = L;
}
```

#### Contract C: LCT `access(pos[r])` Color-Chain Sweeping for Range Distinct Substrings (`Luogu P6292`)
- **Invariant**: Each splay tree $x$ in the LCT over $\mathcal{T}_{\text{link}}$ is monochrome with previous right-endpoint `col[x]` $= p_{\text{old}}$ and covers length interval $[\text{sub\_min}[x], \text{sub\_max}[x]] = [\text{len}(\text{link}(\text{top})) + 1, \text{len}(\text{bot})]$.

```cpp
void access_and_sweep(int u_r, int r) {
    int x = u_r, y = 0;
    for (; x; y = x, x = fa[x]) {
        splay(x);
        // Detach old preferred child: keep it as its own monochrome splay tree
        ch[x][1] = 0;
        pushup(x);
        // Remove stale contribution of solid chain x (excluding root 1 if sub_min > sub_max)
        int p_old = col[x];
        if (p_old > 0 && sub_min[x] <= sub_max[x]) {
            range_add_bit(p_old - sub_max[x] + 1, p_old - sub_min[x] + 1, -1);
        }
        // Attach y as the new preferred child and merge into chain
        ch[x][1] = y;
        pushup(x);
    }
    // Color the entire root-to-u_r solid chain with new last occurrence r
    apply_color(y, r);
    range_add_bit(1, r, +1);
}
```

---

### 15.5 Diagnostic Routing Matrix for Wave 2A Paradigms

| Query / Structural Signature in Problem Statement | Primary Tool & Data-Structure Coupling | Time & Space Complexity | Canonical Reference Problem |
| :--- | :--- | :--- | :--- |
| Multi-string / Trie substring statistics ($\sum |S_i| \le N$ or $V_{\text{Trie}} \le N$) | **3-Case Online GSAM** or **Offline Trie BFS GSAM** + Link-Tree DP | $O(N |\Sigma|)$ time, $O(N |\Sigma|)$ space | `[ZJOI2015] 诸神眷顾的幻想乡`, `[HAOI2016] 找相同字符` |
| Pattern $T$ matched against substring $S[l..r]$ (distinct non-occurring, next lexicographical, interval LCS) | **SAM + Persistent Segment Tree Merge on $\text{endpos}_S$** + Clipping $[l + L - 1, r]$ | $O((N + \sum |T|) \log N)$ time & space | `[NOI2018] 你的名字`, `CF 1037H` |
| Fixed substring $S[a..b]$ vs. $S[c..d]$ prefix/suffix containment | **Link-Tree Binary Lifting (`倍增定位`) + Persistent Segment Tree Merge** | $O(N \log N + Q \log^2 N)$ time | `[HEOI2016/TJOI2016] 字符串` |
| Substring $S[p_l..p_r]$ frequency distribution across dictionary $T_l \dots T_r$ | **GSAM + Persistent Segment Tree Merge over Dictionary IDs** $[1, m]$ | $O((N + Q) \log m)$ time | `CF 666E — Forensic Examination` |
| Longest chain of substrings $s_1, \dots, s_k$ where $s_i$ occurs $\ge 2$ times in $s_{i+1}$ | **Top-Len Sufficiency Lemma + Link-Tree Top-Down DP + Endpos Clipping** | $O(N \log N)$ time | `CF 700E — Cool Slogans` |
| Online character right-appends to $S$ + online pattern occurrence count | **Dynamic SAM + Link-Cut Tree** (`cut`/`link` on clone split + path $+1$) | $O((N + \sum |P|) \log N)$ time, $O(N)$ space | `[BZOJ 2555] SubString` |
| Offline range queries $(l, r)$ aggregating over **all** distinct substrings of $S[l..r]$ | **SAM + LCT `access(pos[r])` Color-Chain Sweeping (`树点涂色`) + BIT/SegTree** | $O(N \log^2 N + Q \log N)$ time, $O(N)$ space | `Luogu P6292`, `[SDOI2017]` |
| Implicit directed graph where $B_j \to A_i$ iff $B_j$ is a prefix of $A_i$ | **Reversed SAM $\mathcal{T}_{\text{link}}$ + Intra-Node Length-Sorted Prefix-Chain DAG** | $O((N + n_a + n_b)\log N + m)$ time | `[十二省联考 2019] 字符串问题` |
| Range pair aggregations over $\text{LCP}(S[i..r], S[l..r])$ for $i \in [l, r]$ | **Reversed SAM Link-Tree HLD / Centroid Decomp + 2D BIT** | $O((N + Q) \log^2 N)$ time | `CF 1098F — Ж-function` |
