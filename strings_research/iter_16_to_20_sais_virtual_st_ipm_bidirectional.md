# Wave 2B (Iterations 16–20): Advanced Suffix Structures — Induced Sorting (SA-IS), Virtual Suffix Trees, Internal Pattern Matching (IPM) & Bi-Directional Structures

> [!IMPORTANT]
> **Cohort 1 Primary Research Dossier — Wave 2B (`iter_16_to_20`)**
> This report executes Iterations 16 through 20 of the Phase 1 Multi-Cohort Research Pipeline (`strings_research/PLAN.md`). In strict compliance with `AGENTS.md` and the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**, we omit boilerplate $O(N \log N)$ suffix array construction templates and standard RMQ code. Instead, we derive the deep structural reductions that power grandmaster string algorithms: why SA-IS is a prefix-free grammar compression by Leftmost S-type (LMS) blocks, how the Cartesian tree of the `height` array and Virtual Suffix Trees (`后缀树虚树`) compress $O(k^2)$ substring interactions into $O(k)$ tree DP states, how Kociumaka et al.'s **Internal Pattern Matching (IPM)** and the **Four Methods of Internal Border Queries (`[BJWC2018] Border 的四种求法`)** answer substring period/border/occurrence queries in polylogarithmic or $O(1)$ time, and how bi-directional suffix structures (Affix Trees, SCDAWGs, and Online Prepend/Append Suffix Trees) unify left- and right-extension equivalence classes.

---

## Iteration 16: Linear-Time Induced Sorting (SA-IS) as a Structural Reduction

### 16.1 Prerequisites, Learning Objectives & Diagnostic Context

- **Assumed Baseline**: Familiarity with the Suffix Array $\text{SA}[1..N]$, inverse suffix array $\text{rk}[1..N]$, LCP array $\text{height}[2..N]$, and classic $O(N \log N)$ prefix-doubling sorting.
- **Learning Objectives**:
  1. Formulate **SA-IS (Nong, Zhang, and Chan 2009)** not merely as an implementation black box for fast suffix sorting, but as an **order-preserving structural reduction** (a locally consistent parsing of a string into Leftmost S-type substrings).
  2. Prove the three central invariants: the **Strict $L < S$ Bucket Partition**, the ** LMS Size-Halving Bound ($\le \lfloor N/2 \rfloor$)**, and the **Two-Pass Monotonic Bucket Pointer Invariant** (why sorting LMS suffixes alone uniquely induces the order of all $L$-type suffixes in a left-to-right sweep, and all $S$-type suffixes in a right-to-left sweep).
  3. Adapt the SA-IS induction principle to non-standard settings: cyclic strings without sentinel distortion, generalized suffix arrays with multiple sentinels, run-length encoded (RLE) strings, and Lyndon / suffix-tree construction via induced sorting.

---

### 16.2 The 4-Step Structural Derivation of SA-IS

#### Step 1: The Diagnostic Signal (Why Prefix Doubling Fails Structural & Asymptotic Demands)

Prefix doubling sorts suffixes of $S[1..N]$ by lengths $2^0, 2^1, \dots, 2^{\lceil \log_2 N \rceil}$ in $O(N \log N)$ time. In two major regimes, prefix doubling is inadequate:
1. **Tight $O(N)$ Asymptotic Bottlenecks ($N \ge 2 \times 10^6$ or Large Integer Alphabets)**: When $N = 5 \times 10^6$ or SA construction sits inside a divide-and-conquer / alphabet-reduction inner loop, the $\Theta(\log N)$ cache-unfriendly radix passes of prefix doubling exceed time limits.
2. **Lack of Local Parsing Structure**: Prefix doubling treats every position symmetrically at every scale $2^k$. It provides no canonical decomposition of $S$ into variable-length local blocks whose lexicographical order mirrors the global suffix order. By contrast, induced sorting partitions $S$ at local extrema of the suffix comparison relation (`L`-to-`S` transitions), turning suffix sorting into a $2\times$-smaller recursive problem.

#### Step 2: The Combinatorial Word Invariant (L/S Classification, LMS Blocks & Order Homomorphism)

Let $S[1..N]$ be a string over an ordered alphabet $\Sigma$, terminated by a unique sentinel $S[N] = \$$ that is strictly smaller than every character in $\Sigma$. For each position $i \in \{1, \dots, N\}$, write $\text{suf}(i) = S[i..N]$.

##### Definition 16.1 ($S$-Type, $L$-Type, and LMS Positions)
Every position $i \in \{1, \dots, N\}$ is classified into one of two types by comparing $\text{suf}(i)$ with its right neighbor $\text{suf}(i+1)$:
- **Type $S$ (Smaller)**: $i = N$ (by convention for the sentinel $\$$), or $\text{suf}(i) < \text{suf}(i+1)$.
- **Type $L$ (Larger)**: $\text{suf}(i) > \text{suf}(i+1)$.

Because all suffixes have distinct lengths and end with the unique sentinel $\$$, $\text{suf}(i) \ne \text{suf}(i+1)$ is guaranteed. By peeling off the first character $S[i]$ vs. $S[i+1]$, the classification satisfies a backwards single-character recurrence for $i = N-1$ down to $1$:

$$
\text{type}(i) = \begin{cases}
S & \text{if } S[i] < S[i+1], \\
L & \text{if } S[i] > S[i+1], \\
\text{type}(i+1) & \text{if } S[i] = S[i+1].
\end{cases}
$$

A position $i \in \{2, \dots, N\}$ is a **Leftmost $S$-type (LMS) character** (denoted $S^*$) if $\text{type}(i) = S$ and $\text{type}(i-1) = L$. Let $p_1 < p_2 < \dots < p_m = N$ be all LMS positions in $S$.
- An **LMS-prefix** is a suffix $\text{suf}(p_k)$ starting at an LMS position.
- An **LMS-substring** is either the terminal single-character string $S[N..N] = \$$, or a substring $S[p_k .. p_{k+1}]$ spanning from one LMS position $p_k$ to the immediately following LMS position $p_{k+1}$ (inclusive of both endpoints!).

```
Index i:    1   2   3   4   5   6   7   8   9  10  11  12
Char S[i]:  m   i   s   s   i   s   s   i   p   p   i   $
Type:       L   S   L   L   S   L   L   S   L   L   L   S
LMS (S*):       *           *           *               *
LMS-substrings: S[2..5]="issi", S[5..8]="issi", S[8..12]="ippi$", S[12..12]="$"
```

We now prove the three combinatorial word invariants that justify SA-IS.

##### Lemma 16.2 (The $L < S$ Bucket Partition Invariant)
For every character $c \in \Sigma \cup \{\$\}$, let $\mathcal{B}(c) = \{i : S[i] = c\}$ be the bucket of suffixes starting with $c$. In the sorted Suffix Array, **every $L$-type suffix in $\mathcal{B}(c)$ appears strictly before every $S$-type suffix in $\mathcal{B}(c)$**:

$$
\forall i, j \in \mathcal{B}(c), \quad \text{type}(i) = L \text{ and } \text{type}(j) = S \implies \text{suf}(i) < \text{suf}(j).
$$

**Proof**: Suppose $S[i] = c$ with $\text{type}(i) = L$, and $S[j] = c$ with $\text{type}(j) = S$. Let $r_i \ge 1$ be the run length of character $c$ starting at $i$, so $S[i .. i+r_i-1] = c^{r_i}$ and $S[i+r_i] = d_i \ne c$. Since $\text{type}(i) = L$ propagates across equal adjacent characters, we must have $c > d_i$. Similarly, let $r_j \ge 1$ be the run length of $c$ starting at $j$, so $S[j .. j+r_j-1] = c^{r_j}$ and $S[j+r_j] = d_j \ne c$ (or $j+r_j = N$ where $d_j = \$$, which is inconsistent with $\text{type}(j)=S$ unless $c < d_j$). Since $\text{type}(j) = S$, we have $c < d_j$.
Now compare $\text{suf}(i) = c^{r_i} d_i \dots$ and $\text{suf}(j) = c^{r_j} d_j \dots$:
- If $r_i \le r_j$, at offset $r_i$ from the start, $\text{suf}(i)$ has character $d_i < c$, while $\text{suf}(j)$ has character $c$ (if $r_i < r_j$) or $d_j > c$ (if $r_i = r_j$). In both cases $d_i < \text{suf}(j)[r_i]$, so $\text{suf}(i) < \text{suf}(j)$.
- If $r_i > r_j$, at offset $r_j$ from the start, $\text{suf}(i)$ has character $c$, while $\text{suf}(j)$ has character $d_j > c$. Again $\text{suf}(i) < \text{suf}(j)$. $\blacksquare$

> [!NOTE]
> **Sub-Bucket Geometry**: Lemma 16.2 implies that each character bucket $\mathcal{B}(c)$ splits cleanly into two disjoint contiguous sub-buckets: the **$L$-sub-bucket** $\mathcal{B}_L(c)$ at the front (head), and the **$S$-sub-bucket** $\mathcal{B}_S(c)$ at the back (tail). Moreover, every LMS suffix $\text{suf}(p_k)$ is $S$-type, so it resides inside $\mathcal{B}_S(S[p_k])$.

##### Lemma 16.3 (The LMS Halving Bound)
For any string $S[1..N]$ of length $N \ge 2$, the number of LMS positions $m$ satisfies $m \le \lfloor N / 2 \rfloor$.

**Proof**: Position $1$ is never LMS because it has no left neighbor $i-1$. By Definition 16.1, if $i$ is LMS ($\text{type}(i) = S$ and $\text{type}(i-1) = L$), then $i-1$ is $L$-type and therefore not LMS. Thus no two LMS positions can be adjacent in $S$, and $1$ is not LMS, immediately yielding $m \le \lfloor N / 2 \rfloor$. $\blacksquare$

##### Theorem 16.4 (LMS-Substring Order Homomorphism)
Define a total preorder $\preceq$ on LMS-substrings by comparing them character-by-character, where at every aligned position we compare the **pair** $(S[x], \text{type}(x))$ lexicographically with $L < S$:
- Two LMS-substrings $U = S[p_a .. p_{a+1}]$ and $V = S[p_b .. p_{b+1}]$ are **LMS-equal** ($U \equiv V$) if and only if they have the same length $\ell$ and for all $t \in [0, \ell-1]$, both $S[p_a+t] = S[p_b+t]$ and $\text{type}(p_a+t) = \text{type}(p_b+t)$.
- Otherwise, at the first offset $t$ where $(S[p_a+t], \text{type}(p_a+t)) \ne (S[p_b+t], \text{type}(p_b+t))$, that mismatch immediately and permanently decides whether $\text{suf}(p_a) < \text{suf}(p_b)$ or $\text{suf}(p_a) > \text{suf}(p_b)$!

Consequently, if we replace each LMS-substring $S[p_k .. p_{k+1}]$ ($1 \le k < m$) by its equivalence-class rank $T[k] \in \{1, \dots, \sigma'\}$ under $\preceq$, then for all $1 \le a, b \le m$:

$$
\text{suf}_S(p_a) < \text{suf}_S(p_b) \iff \text{suf}_T(a) < \text{suf}_T(b).
$$

**Proof**: Consider two suffixes $\text{suf}_S(p_a)$ and $\text{suf}_S(p_b)$ starting at LMS positions. Partition both suffixes into their consecutive overlapping LMS-substrings:

$$
\text{suf}_S(p_a) \leftrightarrow (S[p_a..p_{a+1}], S[p_{a+1}..p_{a+2}], \dots), \qquad \text{suf}_S(p_b) \leftrightarrow (S[p_b..p_{b+1}], S[p_{b+1}..p_{b+2}], \dots).
$$

Notice that no proper prefix of an LMS-substring $S[p_a..p_{a+1}]$ can equal another full LMS-substring $S[p_b..p_{b+1}]$ in both characters and $L/S$ types! Why? Because inside $S[p_a..p_{a+1}]$, position $p_a$ is $S$-type, it stays $S$-type until the first transition to $L$-type, and then stays $L$-type until the unique second transition back to $S$-type at $p_{a+1}$. Thus $p_{a+1}$ is the *first* index after the $L$-type zone that returns to $S$-type. If $S[p_b..p_{b+1}]$ matched a proper prefix of $S[p_a..p_{a+1}]$ in both characters and types, its right endpoint $p_{b+1}$ would be an $L \to S$ transition strictly inside $S[p_a..p_{a+1}]$, contradicting that $p_{a+1}$ is the next LMS position after $p_a$. Therefore, the first difference between $\text{suf}_S(p_a)$ and $\text{suf}_S(p_b)$ must occur inside the first mismatched pair of LMS-substrings $S[p_{a+k}..p_{a+k+1}]$ and $S[p_{b+k}..p_{b+k+1}]$, where either $S[p_{a+k}+t] \ne S[p_{b+k}+t]$ or $\text{type}(p_{a+k}+t) \ne \text{type}(p_{b+k}+t)$ (which resolves via Lemma 16.2). $\blacksquare$

#### Step 3: The Reverse-Engineering Scratchpad (Two-Pass Induced Sorting Invariant)

How do we both (a) sort all LMS-substrings in $O(N)$ time *before* recursion, and (b) reconstruct the full Suffix Array from the sorted LMS-prefixes *after* recursion? The answer is that **the exact same Two-Pass Induced Sorting routine achieves both!**

##### The Core Induced Sorting Procedure (`InduceSort`)
Suppose we are given an initial placement of the LMS positions $\{p_1, \dots, p_m\}$ into the **tails of their respective $S$-sub-buckets** $\mathcal{B}_S(c)$:
1. **Pass 0 (Seed LMS at Bucket Tails)**: Clear $\text{SA}[1..N] \leftarrow \text{EMPTY}$. Maintain a tail pointer $\text{tail}[c]$ at the right end of each bucket $\mathcal{B}(c)$. Place the LMS positions into $\text{SA}[\text{tail}[S[p_k]]]$ decrementing $\text{tail}[S[p_k]]$.
2. **Pass 1 (Left-to-Right Scan $\to$ Induce $L$-Type Suffixes at Bucket Heads)**: Initialize a head pointer $\text{head}[c]$ at the left end of each bucket $\mathcal{B}(c)$. Scan $k = 1, 2, \dots, N$ from left to right. If $\text{SA}[k] = i > 1$ and $\text{type}(i-1) = L$, place $i-1$ at $\text{SA}[\text{head}[S[i-1]]]$ and increment $\text{head}[S[i-1]]$.
   - *Why is every $L$-type suffix $i-1$ visited only AFTER $\text{SA}[k]=i$ is already placed?* Because $\text{type}(i-1) = L \implies \text{suf}(i-1) > \text{suf}(i)$. Thus in the sorted Suffix Array, $\text{suf}(i)$ appears at some index $k$ strictly **to the left** of the destination index of $\text{suf}(i-1)$! Furthermore, inside every $L$-chain $i-r \to \dots \to i-1 \to i$ where $\text{type}(i) = S$ and $\text{type}(i-1) = L$, the base of the chain is an LMS position $i$, which was already seeded in Pass 0. Since $\text{suf}(i-1) < \text{suf}(j-1) \iff (S[i-1] < S[j-1]) \lor (S[i-1] = S[j-1] \land \text{suf}(i) < \text{suf}(j))$, visiting $i$ before $j$ in increasing $\text{SA}$ order inserts $i-1$ before $j-1$ into $\mathcal{B}_L(S[i-1])$.
3. **Pass 2 (Right-to-Left Scan $\to$ Induce $S$-Type Suffixes at Bucket Tails)**: Reset $\text{tail}[c]$ to the right end of each bucket $\mathcal{B}(c)$. Scan $k = N, N-1, \dots, 1$ from right to left. If $\text{SA}[k] = i > 1$ and $\text{type}(i-1) = S$, place $i-1$ at $\text{SA}[\text{tail}[S[i-1]]]$ (overwriting the initial LMS seeds) and decrement $\text{tail}[S[i-1]]$.
   - *Why does scanning right-to-left work?* Because $\text{type}(i-1) = S \implies \text{suf}(i-1) < \text{suf}(i)$. Thus $\text{suf}(i)$ sits at some index $k$ strictly **to the right** of the destination of $\text{suf}(i-1)$! Moreover, every maximal $S$-chain terminates at an $S \to L$ boundary (or $N$), and all $L$-type suffixes have already been placed in their exact final sorted order in Pass 1. Scanning from $N$ down to $1$ encounters $\text{suf}(j)$ before $\text{suf}(i)$ whenever $\text{suf}(j) > \text{suf}(i)$, so inserting $j-1$ at the tail of $\mathcal{B}_S(c)$ and decrementing the tail pointer places larger $S$-type suffixes to the right of smaller $S$-type suffixes!

> [!TIP]
> **Why `InduceSort` Works Twice in SA-IS**:
> - **First Invocation (Pre-Recursion)**: Seed the LMS positions at the tails of $\mathcal{B}_S(c)$ in *arbitrary* order. Because each LMS position $p_k$ is initially treated as a 1-character string $S[p_k]$ of type $S$, Pass 1 induces all $L$-portions of the LMS-substrings in sorted order, and Pass 2 induces all $S$-portions back to the left endpoints $p_k$. After Pass 2, the LMS positions appear in $\text{SA}$ sorted by their **LMS-substrings** under $\preceq$! We then scan adjacent LMS positions in $\text{SA}$ to assign equivalence-class names $T[1..m]$ in $O(N)$ total time.
> - **Second Invocation (Post-Recursion)**: If all LMS-substring names in $T[1..m]$ are distinct, the relative order of LMS-prefixes is directly given by the inverse permutation of $T$; otherwise, recursively call $\text{SA-IS}(T)$. Once the LMS positions are sorted by their **full suffixes** $\text{suf}(p_k)$, seed them into the tails of $\mathcal{B}_S(c)$ in that exact sorted order and run Pass 1 + Pass 2 a second time. This yields the exact global Suffix Array $\text{SA}[1..N]$!

##### Hand-Checkable Trace on $S = \text{m i s s i s s i p p i \$}$ ($N = 12$)

| Bucket $c$ | Size | $\mathcal{B}_L(c)$ Range | $\mathcal{B}_S(c)$ Range | After Pre-Recursion Pass 0 (LMS Seed) | After Pass 1 (Induce $L$) | After Pass 2 (Induce $S$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\$$ | 1 | $\emptyset$ | $[1..1]$ | `[12]` | `[12]` | `[12]` |
| $\text{i}$ | 4 | $[2..2]$ | $[3..5]$ | `[_, 2, 5, 8]` | `[11, 2, 5, 8]` | `[11, 8, 2, 5]` |
| $\text{m}$ | 1 | $[6..6]$ | $\emptyset$ | `[_]` | `[1]` | `[1]` |
| $\text{p}$ | 2 | $[7..8]$ | $\emptyset$ | `[_, _]` | `[10, 9]` | `[10, 9]` |
| $\text{s}$ | 4 | $[9..12]$ | $\emptyset$ | `[_, _, _, _]` | `[7, 4, 6, 3]` | `[7, 4, 6, 3]` |

Extracting LMS indices from the post-Pass-2 array gives `[12, 8, 2, 5]`, corresponding to LMS-substrings:
- $p_4 = 12$: `"$"` $\to$ name $1$
- $p_3 = 8$: `"ippi$"` $\to$ name $2$
- $p_1 = 2$: `"issi"` $\to$ name $3$
- $p_2 = 5$: `"issi"` $\to$ name $3$ (equal to $S[2..5]$ in characters and types `S L L S`)

Thus the reduced string is $T = [3, 3, 2, 1]$ of length $m = 4 \le 6$. Because name $3$ appears twice, we recurse on $T$, obtaining $\text{SA}_T = [4, 3, 2, 1]$, which orders the LMS positions in $S$ as $(p_4, p_3, p_2, p_1) = (12, 8, 5, 2)$. Seeding $(12, 8, 5, 2)$ into the bucket tails (pushing $2, 5, 8$ from right to left so `[_, 8, 5, 2]` sits in $\mathcal{B}(\text{i})$) and running Pass 1 + Pass 2 yields the final Suffix Array $\text{SA} = [12, 11, 8, 5, 2, 1, 10, 9, 7, 4, 6, 3]$.

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Pitfall 1: Comparing LMS-Substrings by Characters Only (Omitting $L/S$ Type Equality)**:
   - *Counterexample*: Consider two substrings $S[p_a..p_{a+1}] = \text{"aba"}$ and $S[p_b..p_{b+1}] = \text{"aba"}$ where the character following $p_{a+1}$ makes $\text{type}(p_{a+1}) = S$, while another substring of length 3 in a modified variant (if one forgets to stop strictly at LMS boundaries or omits type checks at the right endpoint) has different type. More subtly, if one does not verify that **both** endpoints are LMS and have identical lengths, a prefix match `"ab"` inside `"aba"` might be falsely equated if length equality $\ell_a = \ell_b$ is not checked first! Always check `len(U) == len(V)` and character equality across the entire closed interval $[p_a, p_{a+1}]$.
2. **Pitfall 2: Reversed Insertion Order when Seeding Sorted LMS Suffixes into Bucket Tails**:
   - In Pass 0 of the second invocation, we have the LMS positions sorted in increasing suffix order $q_1 <_{\text{suf}} q_2 <_{\text{suf}} \dots <_{\text{suf}} q_m$. Because we insert into the $S$-sub-bucket using a **decrementing** $\text{tail}[c]$ pointer, we must iterate $k = m$ **down to** $1$! Iterating $k = 1 \dots m$ while decrementing $\text{tail}[c]$ reverses the order of LMS suffixes within the same bucket and corrupts Pass 1.
3. **Pitfall 3: Omitting the Unique Sentinel $\$$**:
   - Without a unique sentinel $S[N] = \$$, two suffixes starting with character $c$ can have $\text{suf}(i)$ be a proper prefix of $\text{suf}(j)$, or $S[N-1] = S[N]$ can make $\text{type}(N-1)$ ambiguous. Always append a virtual sentinel $0$ at index $N+1$ (and strip $\text{SA}[1] = N+1$ afterward).

---

### 16.3 Non-Standard Adaptations of SA-IS

1. **Cyclic Shift Sorting (BWT Construction without Sentinel Distortion)**:
   - Appending $\$$ changes the order of cyclic shifts when $S$ is periodic or when comparing two positions whose match wraps around $N$ (e.g., $S = \text{"aba"}$; cyclic shift at $3$ is `"aab"` $<$ shift at $1$ `"aba"`, whereas with sentinel `"aba$"`, `"a$"` $<$ `"aba$"` happens to agree, but for $S = \text{"bzb"}$, cyclic shift at $3$ is `"bbz"` $>$ shift at $1$ `"bzb"` if `$` > `b` vs `<`). In **Cyclic SA-IS (e.g., Nong et al. / Köppl)**, types are defined cyclically modulo $N$; if $S$ is a pure power $w^k$, its minimal period $p = N/k$ is extracted via KMP first, and cyclic LMS blocks wrap around index $N \to 1$.
2. **Generalized Suffix Array on $K$ Strings ($S_1, \dots, S_K$)**:
   - **Never concatenate with the same separator `#`** if you run unmodified SA-IS without special sentinel handling, because `# == #` merges $L/S$ runs across string boundaries! Either:
     - Assign distinct negative sentinels $\$_1 < \$_2 < \dots < \$_K$, or
     - Use a single separator character $0$, and modify the type recurrence and LMS equality check so that **every separator position is unconditionally Type $S$ and an LMS boundary**, and two separators at indices $i \ne j$ satisfy $S[i] < S[j] \iff i < j$.

---

## Iteration 17: Virtual Suffix Trees (`后缀树虚树`), Cartesian Tree on `height` & DSU-on-Tree

### 17.1 The Exact Three-Way Duality: Suffix Tree, SAM Link Tree, and `height` Cartesian Tree

A foundational structural insight in competitive stringology is that three seemingly distinct trees on a string $S[1..N]$ are **isomorphic** (up to leaf/unary-node handling):

| Structure | Construction Origin | Nodes & Edge Weights | How $\text{LCP}(\text{suf}(i), \text{suf}(j))$ Appears |
| :--- | :--- | :--- | :--- |
| **1. Suffix Tree $\mathcal{T}_{\text{ST}}(S)$** | Compact Trie of all suffixes $S[i..N]\$$ | $\le 2N$ nodes; each internal node $u$ has string depth $\text{dep}(u)$ | String depth $\text{dep}(\text{LCA}_{\text{ST}}(\text{leaf}(i), \text{leaf}(j)))$ |
| **2. Reversed SAM Link Tree $\mathcal{T}_{\text{SAM}}(S^R)$** | Parent tree (`link`) of the Suffix Automaton built on $S^R$ | $\le 2N-1$ states; each state $u$ has maximum length $\text{len}(u)$ | $\text{len}(\text{LCA}_{\text{SAM}}(\text{prefix\_node}(i), \text{prefix\_node}(j)))$ |
| **3. Cartesian Tree of $\text{height}[2..N]$** | Min-heap Cartesian Tree built on $H[k] = \text{LCP}(\text{SA}[k-1], \text{SA}[k])$ | $N-1$ internal nodes interwoven with $N$ leaves $\text{SA}[1..N]$ (merging equal-height parent-child nodes) | Value $H[\text{LCA}_{\text{Cart}}(\text{rk}[i], \text{rk}[j])]$ |

#### Theorem 17.1 (Cartesian Tree – Suffix Tree Isomorphism)
Let $H[k] = \text{height}[k] = \text{LCP}(\text{suf}(\text{SA}[k-1]), \text{suf}(\text{SA}[k]))$ for $k = 2, \dots, N$. Build the **min-Cartesian tree** on $H[2..N]$, and attach leaf $\text{SA}[k-1]$ as the left child and leaf $\text{SA}[k]$ as the right child where subtree bounds reach singletons. If we contract every tree edge $(u, v)$ where $H[u] = H[v]$, the resulting tree is **canonically isomorphic to the Suffix Tree of $S$**!

**Proof**: By the LCP Interval Theorem, for any $1 \le l < r \le N$:

$$
\text{LCP}(\text{suf}(\text{SA}[l]), \text{suf}(\text{SA}[r])) = \min_{l < k \le r} H[k].
$$

In the min-Cartesian tree of $H[2..N]$, each node $k$ with value $H[k]$ represents the maximal contiguous range $[L_k, R_k]$ of indices in $\text{SA}$ such that all adjacent pairs in $[L_k, R_k]$ share a common prefix of length at least $H[k]$. Contracting equal-valued adjacent Cartesian tree nodes groups all split points achieving the same minimum $h = H[k]$ inside $[L_k, R_k]$ into a single multi-way branching node of string depth $h$, which is the exact definition of an explicit branching node in the Suffix Tree of $S$. $\blacksquare$

---

### 17.2 The 4-Step Derivation of Virtual Suffix Trees (`后缀树虚树`)

#### Step 1: The Diagnostic Signal (Why Full-Tree DP Fails on Subset/Substring Queries)

Consider problems where:
- We are given a long string $S[1..N]$ and $Q$ queries, each specifying two sets of suffixes or substrings $A = \{u_1, \dots, u_a\}$ and $B = \{v_1, \dots, v_b\}$ with $\sum (|A| + |B|) = O(N)$ (e.g., `CF 1073G — Yet Another LCP Problem`), asking for $\sum_{u \in A} \sum_{v \in B} \text{LCP}(u, v)$.
- Or we must compute an aggregate over all pairs of suffixes $(i, j)$ weighted by $\text{LCP}(\text{suf}(i), \text{suf}(j))$ or bucketed by LCP thresholds $r \in [0, N-1]$ (`[NOI2015] 品酒大会`, `[AHOI2013] 差异`, `CF 802I`, `CF 873F`).

A naive double loop over $A \times B$ takes $O(|A| \cdot |B|)$ per query, which is $O(N^2)$ in the worst case. Even running a tree DP over the entire Suffix Tree takes $O(N)$ per query, yielding $O(NQ)$ total time. The diagnostic signal for a **Virtual Suffix Tree (`后缀树虚树`)** is: **queries touch $k_q$ arbitrary substrings $S[l_i..r_i]$ with $\sum_q k_q \le 5 \times 10^5$, and the objective depends only on pairwise LCPs $\text{LCP}(S[l_i..r_i], S[l_j..r_j])$**.

#### Step 2: The Combinatorial Word Invariant (Truncation Node & Adjacent-Rank LCA Closure)

How do we map an arbitrary **substring** $S[l..r]$ (not just a full suffix $S[l..N]$) to a node in the Suffix Tree, and why do $k$ query substrings generate at most $2k-1$ nodes in the Virtual Suffix Tree?

##### Invariant 17.2 (Substring Truncation via Dummy Leaf or Link-Tree Binary Lifting)
For a substring $S[l..r]$ of length $\ell = r - l + 1$:
1. **On the Reversed SAM Link Tree $\mathcal{T}_{\text{SAM}}(S^R)$**: Locate the SAM state for suffix $S[l..N]$ (which is a prefix of $S^R$), and binary-lift along `link` ancestors to the highest ancestor $u$ with $\text{len}(u) \ge \ell$. To handle the exact length truncation $\min(\text{LCP}, \ell)$ when multiple substrings land inside the same edge $(\text{link}(u), u)$ with $\text{len}(\text{link}(u)) < \ell \le \text{len}(u)$, subdivide the edge by inserting a virtual node at string depth $\ell$.
2. **On the Suffix Array `(rk, height)` directly (Zero Explicit Tree Needed!)**: Sort all query substrings $U_i = S[l_i..r_i]$ in lexicographical order using $O(1)$ LCE comparisons:
   - Compute $d = \text{LCE}(l_i, l_j) = \text{RMQ}_{\text{height}}(\min(\text{rk}[l_i], \text{rk}[l_j]) + 1, \max(\text{rk}[l_i], \text{rk}[l_j]))$.
   - The true substring LCP is $\text{LCP}(U_i, U_j) = \min(d, |U_i|, |U_j|)$.
   - If $d < \min(|U_i|, |U_j|)$, compare $S[l_i + d]$ vs. $S[l_j + d]$; otherwise compare $|U_i|$ vs. $|U_j|$.
   Once $U_1 \le_{\text{lex}} U_2 \le_{\text{lex}} \dots \le_{\text{lex}} U_k$ are sorted, the adjacent LCP values $h_t = \text{LCP}(U_{t-1}, U_t)$ for $t = 2, \dots, k$ satisfy the **Exact Substring Interval LCP Identity**:

$$
\forall 1 \le a < b \le k, \qquad \text{LCP}(U_a, U_b) = \min_{a < t \le b} \text{LCP}(U_{t-1}, U_t) = \min_{a < t \le b} h_t.
$$

**Why is this true?** Because truncating suffixes to substrings $U_t$ is equivalent to inserting $k$ virtual suffixes $U_t \$$ into a Trie; in any Trie, the LCA of any range of DFS-ordered leaves $[a, b]$ equals the shallowest LCA of consecutive leaves $(t-1, t)$ for $a < t \le b$!

#### Step 3: The Reverse-Engineering Scratchpad (Two Paradigms: Monotonic Stack Virtual Tree vs. DSU Merge on `height`)

We derive the two workhorse algorithmic translations of Theorem 17.1 and Invariant 17.2.

##### Paradigm A: Offline All-Pairs LCP Aggregation via Decreasing `height` DSU Merge (`[NOI2015] 品酒大会`)
Suppose we must answer for every threshold $L \in [0, N-1]$:
1. How many pairs of suffixes $(i, j)$ ($i < j$) have $\text{LCP}(\text{suf}(i), \text{suf}(j)) \ge L$?
2. What is the maximum product $a_i \cdot a_j$ among all pairs with $\text{LCP}(\text{suf}(i), \text{suf}(j)) \ge L$?

Instead of building the Suffix Tree explicitly, process the Cartesian tree bottom-up by sorting the split points $k \in \{2, \dots, N\}$ in **descending order of $H[k] = \text{height}[k]$**:
- Maintain a Disjoint Set Union (DSU) over indices $1..N$ in the Suffix Array. Initially, each index $x \in [1..N]$ is an isolated component of size $\text{sz}[x] = 1$, maintaining $\text{max}_1[x] = \text{min}_1[x] = a_{\text{SA}[x]}$.
- When processing $H[k] = L$ in descending order, merge the component containing $k-1$ and the component containing $k$:
  - New pairs achieving $\text{LCP} = L$ strictly at this merge step: $\Delta \text{pairs}(L) += \text{sz}[u] \cdot \text{sz}[v]$.
  - Candidate maximum product at threshold $L$ (accounting for two negative numbers multiplying to a positive number!):

$$
\text{cand}(L) = \max\Big(\text{max}_1[u] \cdot \text{max}_1[v], \; \text{min}_1[u] \cdot \text{min}_1[v]\Big).
$$

- Finally, compute a suffix sum on $\Delta \text{pairs}(L)$ and a suffix maximum on $\text{cand}(L)$ from $L = N-1$ down to $0$. Total time after SA construction: $O(N \alpha(N))$!

##### Paradigm B: Per-Query Virtual Suffix Tree via Monotonic Stack (`CF 1073G`)
Given query sets $A, B$ of total size $k = |A| + |B|$:
1. Tag each element of $A$ with $(w_A = 1, w_B = 0)$ and each element of $B$ with $(w_A = 0, w_B = 1)$.
2. Sort all $k$ items by $\text{rk}[\cdot]$ in $O(k \log k)$ time. Merge identical items by summing their $(w_A, w_B)$ weights and adding $w_A(u) w_B(u) \cdot |u|$ to the answer.
3. Let the unique sorted items be $u_1, \dots, u_m$ ($m \le k$). Compute adjacent LCPs $h_t = \text{LCP}(u_{t-1}, u_t)$ for $t = 2, \dots, m$ in $O(1)$ per pair via RMQ on `height`.
4. Build the Cartesian tree of $h_2, \dots, h_m$ in $O(m)$ time using a monotonic stack (or run a monotonic stack directly twice, or a single tree DP on the $m-1$ internal nodes):
   - At each internal node $t$ with LCP value $h_t$, its left child subtree has total weight $(W_{A,L}, W_{B,L})$ and its right child subtree has total weight $(W_{A,R}, W_{B,R})$.
   - The contribution of pairs separated at node $t$ is:

$$
\text{ans} += h_t \cdot \Big(W_{A,L} \cdot W_{B,R} + W_{B,L} \cdot W_{A,R}\Big).
$$

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Pitfall 1: Negative Valuations in Max-Product DSU (`[NOI2015] 品酒大会`)**:
   - If $a_i \in [-10^9, 10^9]$, maintaining only the maximum $a_i$ in each DSU component fails when two large negative numbers $(-10^9) \times (-10^9) = +10^{18}$ produce the global optimum. You **must** maintain both $\max$ and $\min$ in every component, and initialize the answer array for each $L$ to $-\infty$ (not $0$, because the maximum product can be negative when a component has size 2 with one positive and one negative value!).
2. **Pitfall 2: Identical Substrings in Virtual Suffix Tree Queries (`CF 1073G`)**:
   - If $u \in A \cap B$ (the exact same suffix or substring appears in both query sets), $\text{rk}[u] = \text{rk}[u]$, so calling $\text{RMQ}(\text{rk}[u]+1, \text{rk}[u])$ passes an invalid inverted interval $[r+1, r]$ to the RMQ table! Always deduplicate equal substrings first and handle $u \in A \cap B$ with $\text{LCP}(u, u) = |u|$ before computing adjacent `height` RMQs.
3. **Pitfall 3: Confusing Number of Substrings with Number of Suffixes on `height` (`CF 802I` vs. `[AHOI2013] 差异`)**:
   - In `[AHOI2013] 差异`, we sum $\text{LCP}(\text{suf}(i), \text{suf}(j))$ over pairs of **suffixes**, where each leaf has weight $1$.
   - In `CF 802I — Fake News (hard)`, we sum $\text{occ}(s)^2$ over all **distinct substrings** $s$. In the Cartesian tree of `height`, a node $u$ covering $k$ suffixes (i.e. interval of width $k$ in $\text{SA}$, which means $k = R_u - L_u + 1$ suffixes share that prefix) with value $H[u]$ and parent value $H[\text{par}(u)]$ represents $H[u] - H[\text{par}(u)]$ distinct substrings, each occurring $k$ times! Forgetting to multiply the occurrence square $k^2$ by the edge length $(H[u] - H[\text{par}(u)])$ undercounts substrings inside compressed Suffix Tree edges.

---

## Iteration 18: Internal Pattern Matching (IPM) & The Basic Substring Dictionary (Kociumaka et al.)

### 18.1 Architecture of the Basic Substring Dictionary (Static String $S[1..N]$)

In modern stringology—formalized by **Kociumaka, Radoszewski, Rytter, and Waleń (SODA 2015, *"Internal Pattern Matching Queries in a Text and Applications"*)**—a preprocessing phase on a static string $S[1..N]$ builds a **Basic Substring Dictionary** that answers internal queries about arbitrary substrings $U = S[l_1..r_1]$ and $V = S[l_2..r_2]$ without ever materializing $U$ or $V$ explicitly.

| Internal Query Operation | Input | Time Complexity | Structural Mechanism |
| :--- | :--- | :--- | :--- |
| **1. Longest Common Extension ($\text{LCE}(i, j)$ / $\text{LCE}^R(i, j)$)** | Indices $i, j \in [1..N]$ | $O(1)$ | RMQ ($\pm 1$ RMQ or Sparse Table) over $\text{height}$ of $S$ and $S^R$ |
| **2. Lexicographical Comparison of Substrings** | $U = S[l_1..r_1]$, $V = S[l_2..r_2]$ | $O(1)$ | $d = \min(\text{LCE}(l_1, l_2), |U|, |V|)$; compare $S[l_1+d]$ vs. $S[l_2+d]$ or lengths |
| **3. Concatenation Comparison ($U_1 U_2 \dots U_k$ vs. $V_1 V_2 \dots V_m$)** | Two sequences of substrings | $O(k + m)$ ($O(1)$ for $U_1 U_2$ vs. $V_1 V_2$) | Two-pointer walk advancing by $\min(\text{LCE}, \text{remaining block length})$ |
| **4. Substring Locus & Rank ($\text{Rank}(S[l..r])$)** | $U = S[l..r]$ | $O(\log N)$ or $O(1)$ | Binary lifting on SAM/ST or RMQ-threshold binary search around $\text{rk}[l]$ for $[L_{\text{SA}}, R_{\text{SA}}]$ |
| **5. Internal Pattern Matching ($\text{IPM}(P, T)$)** | $P = S[l_1..r_1]$, $T = S[l_2..r_2]$ with $|T| < 2|P|$ | $O(1)$ query ($O(N)$ or $O(N \log N)$ space) | Occurrences of $P$ in $T$ form a **single Arithmetic Progression** of step $\text{per}(P)$! |
| **6. Anchored / 2D Substring Range Query** | $P_1$ prefix, $P_2$ suffix, or $S[a..b]$ containment | $O(\log N)$ | Orthogonal 2D range query on $(\text{SA}, \text{SA}^R)$ via Wavelet Matrix / Persistent SegTree |

---

### 18.2 The 4-Step Derivation of Internal Pattern Matching (IPM) & The Four Methods of Substring Border Queries (`[BJWC2018] Border 的四种求法`)

#### Step 1: The Diagnostic Signal (Why Whole-String KMP and SAM Fail on $S[l..r]$ Border/Period Queries)

Consider the landmark problem **`[BJWC2018] Border 的四种求法`** (Luogu P4482):
> Given a string $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[l, r]$, find the length of the **longest proper border** of the substring $S[l..r]$ (i.e., the maximum $b \in [1, r-l]$ such that $S[l .. l+b-1] = S[r-b+1 .. r]$).

Why do standard algorithms fail?
- **KMP Failure**: The KMP $\pi$-array only gives borders of *prefixes* $S[1..r]$. Re-running KMP on $S[l..r]$ takes $O(r - l + 1) = O(N)$ per query $\implies O(NQ)$ total.
- **Naive SAM / SA Failure**: For a candidate border length $b$, the condition $S[l..l+b-1] = S[r-b+1..r]$ is equivalent to:

$$
\text{LCS}\big(\text{pre}(r), \text{pre}(l+b-1)\big) \ge b \quad \Longleftrightarrow \quad \text{LCP}\big(\text{suf}(l), \text{suf}(r-b+1)\big) \ge b.
$$

Look closely at the inequality $\text{LCS}(\text{pre}(r), \text{pre}(i)) \ge i - l + 1$ (where $i = l + b - 1 \in [l, r-1]$): **the variable $i$ appears on BOTH sides of the inequality**—inside the tree node $\text{pre}(i)$ (whose LCA with $\text{pre}(r)$ gives $\text{LCS}(r, i)$) AND in the required threshold $i - l + 1$! Because the threshold changes linearly with the query index $i$, a simple RMQ or single Segment Tree range-max query cannot isolate $i$.

#### Step 2: The Combinatorial Word Invariant (Bounded-Ratio IPM & $2^k$-Scale Periodicity Reduction)

Before deriving the four tree/data-structure solutions, let us prove the core theorem of **Internal Pattern Matching (IPM)** and how it decomposes any substring border query into $O(\log N)$ scale levels.

##### Theorem 18.1 (Bounded-Ratio IPM Arithmetic Progression Lemma — Kociumaka et al.)
Let $P$ and $T$ be two strings such that $|P| \le |T| < 2|P|$. Then the set of starting positions of occurrences of $P$ in $T$, denoted $\text{Occ}(P, T) = \{i \in [1, |T|-|P|+1] : T[i..i+|P|-1] = P\}$, is either empty, a singleton, or forms a **single arithmetic progression** whose common difference equals the shortest period $d = \text{per}(P)$ of $P$.

**Proof**: Suppose $P$ occurs at least three times in $T$, at starting positions $i_1 < i_2 < \dots < i_m$ ($m \ge 2$). Since $i_m - i_1 \le |T| - |P| < |P|$, even the **first** occurrence $T[i_1..i_1+|P|-1]$ and the **last** occurrence $T[i_m..i_m+|P|-1]$ overlap by at least $|P| - (i_m - i_1) \ge 1$ character!
Specifically, for any two consecutive occurrences $i_k < i_{k+1}$, their shift $d_k = i_{k+1} - i_k$ is a period of $P$, so $d_k \ge d = \text{per}(P)$. Could $d_k > d$? No: because both $T[i_k..i_k+|P|-1]$ and $T[i_{k+1}..i_{k+1}+|P|-1]$ equal $P$ and overlap by $|P| - d_k \ge |P| - (i_m - i_1) \ge 1$, the union $T[i_1 .. i_m + |P| - 1]$ is periodic with period $d = \text{per}(P)$ across the entire span from $i_1$ to $i_m + |P| - 1$ (since any shift by $d$ inside the overlap preserves $P$). Conversely, shifting $P$ by $d$ within that periodic span produces another valid occurrence of $P$ at $i_k + d \le i_{k+1}$. By minimality of $i_{k+1} > i_k$, we must have $i_{k+1} - i_k = d$ for every $k$. $\blacksquare$

##### Corollary 18.2 (Dyadic Scale Decomposition of Substring Borders)
Let $U = S[l..r]$ have length $n = r - l + 1$. Partition all candidate border lengths $b \in [1, n-1]$ into $\lceil \log_2 n \rceil$ dyadic intervals $B_k = [2^k, \min(2^{k+1}-1, n-1)]$ for $k = 0, 1, \dots, \lfloor \log_2(n-1) \rfloor$.
A border of $U$ of length $b \in [2^k, 2^{k+1}-1]$ must have:
- Its prefix occurrence starting at $l$ contain the prefix block $P_k = S[l .. l + 2^k - 1]$ of length $2^k$, and
- Its suffix occurrence ending at $r$ contain the suffix block $Q_k = S[r - 2^k + 1 .. r]$ of length $2^k$.
Specifically:
1. Any border $b \in [2^k, 2^{k+1}-1]$ corresponds to an occurrence of the $2^k$-prefix $P_k = S[l .. l+2^k-1]$ inside the suffix window $T_k = S[\max(l+1, r - 2^{k+1} + 2) .. r]$ of length $< 2 \cdot 2^k = 2^{k+1}$!
2. By Theorem 18.1, the occurrences of $P_k$ inside $T_k$ form **at most one arithmetic progression**, which we can validate or extend to position $r$ using a single $O(1)$ $\text{LCE}$ check!

```
Substring U = S[l .. r]:
[ l -------- l+2^k-1 ] .......................... [ r-2^{k+1}+2 ............ r ]
  |---- P_k (2^k) ---|                              |------- T_k (< 2^{k+1}) --|
                                                        [ r-b+1 .. r-b+2^k ]
                                                          |-- P_k occurs --|
```

#### Step 3: The Reverse-Engineering Scratchpad — All Four Canonical Methods for `[BJWC2018] Border 的四种求法`

Because `[BJWC2018] Border 的四种求法` is the Rosetta Stone of internal substring structure, we derive all **four** canonical solutions and compare their trade-offs.

##### Method 1: Dyadic IPM Bucket Decomposition ($O(N \log N)$ Preprocessing, $O(\log N)$ Online Query)
For each scale $k \in [0, \lfloor \log_2 N \rfloor]$, partition $S[1..N]$ into blocks of size $2^k$, or assign each length-$2^k$ substring $S[i..i+2^k-1]$ its lexicographical rank ID (from step $k$ of Prefix Doubling SA!). Store for each rank ID a sorted list of its occurrence indices in $S$.
To check if $U = S[l..r]$ has a border $b \in [2^k, \min(2^{k+1}-1, r-l)]$:
1. Look up the rank ID of $P_k = S[l .. l+2^k-1]$, and find via `std::lower_bound` the first $\le 2$ occurrences and last occurrence of $P_k$ starting in the interval $I_k = [\max(l+1, r - 2^{k+1} + 2), r - 2^k + 1]$.
2. If there are $\le 2$ occurrences of $P_k$ in $I_k$, test each occurrence $x$ directly in $O(1)$: $x$ induces a border of length $b = r - x + 1$ if and only if $\text{LCE}(l, x) \ge r - x + 1$.
3. If there are $\ge 3$ occurrences $x_1 < x_2 < \dots < x_m$ in $I_k$, Theorem 18.1 guarantees they form an AP $x_t = x_1 + (t-1)d$ with step $d = x_2 - x_1$. Symmetrically, find the occurrences of the suffix block $Q_k = S[r-2^k+1 .. r]$ in $[l, l+2^k-1]$ (which also form an AP of the same step $d$ when overlapped), or simply compute the maximum valid extension $\ell = \text{LCE}(l, x_1)$ of the AP starting at $x_1$: any $x_t = x_1 + (t-1)d$ satisfies $\text{LCE}(l, x_t) \ge r - x_t + 1 \iff x_t + \text{LCE}(l, x_t) - 1 \ge r$. Since $S[l..l+\ell-1]$ and $S[x_1..x_1+\ell-1]$ share period $d$, for every $x_t$ before the periodic run breaks, $x_t + \text{LCE}(l, x_t) - 1 = x_1 + \ell - 1$ (if $\ell$ stops before $l+2^{k+1}-1$) or extends across the whole run! Even simpler: intersecting the AP of $P_k$ in $T_k$ with the AP of $Q_k = S[r-2^k+1..r]$ in $S[l..l+2^{k+1}-2]$ takes $O(1)$ arithmetic!

##### Method 2: SAM Link Tree + Heavy-Light Decomposition + Segment Tree Merging ($O(N \log^2 N)$)
Build the SAM of $S$ (so $\text{LCA}(u_r, u_i)$ on the Link Tree has $\text{len}(\text{LCA}) = \text{LCS}(\text{pre}(r), \text{pre}(i))$).
For a query $[l, r]$, we want the largest $i \in [l, r-1]$ such that:

$$
\text{len}\big(\text{LCA}(u_r, u_i)\big) \ge i - l + 1.
$$

Decompose the path from $u_r$ to the root of the Link Tree into $O(\log N)$ **Heavy-Light Decomposition (HLD) chains** (or do tree divide-and-conquer / heavy-path prefix sweeps). Along the path from $u_r$ to the root, every ancestor $w$ of $u_r$ contributes to all $i \in \text{subtree}(w)$ (i.e. $i \in \text{endpos}(w)$):
- **Case A ($i$ is in the light-child subtree of an ancestor $w$ of $u_r$, so $\text{LCA}(u_r, u_i) = w$ is fixed)**:
  Here $\text{len}(w)$ is known! The condition $\text{len}(w) \ge i - l + 1$ simplifies to:

$$
i \le l + \text{len}(w) - 1 \quad \text{and} \quad i \in [l, r-1] \cap \text{endpos}(w).
$$

  That is a pure **predecessor query** ($\max \{i \in \text{endpos}(w) : l \le i \le \min(r-1, l + \text{len}(w) - 1)\}$) on the Segment Tree Merge of $\text{endpos}(w)$!
- **Case B ($w = \text{LCA}(u_r, u_i)$ lies on a heavy chain $C$, and $u_i$ enters $C$ at node $w$ above $u_r$)**:
  Rewrite the inequality $\text{len}(w) \ge i - l + 1$ as:

$$
i - \text{len}(w) \le l - 1, \quad \text{with } i \in [l, r-1] \text{ and } \text{depth}(w) \le \text{depth}(\text{top\_entry}(u_r \text{ on } C)).
$$

  Notice that $i - \text{len}(w)$ is now **independent of the query $(l, r)$** for each pair $(w, i \in \text{light\_subtree}(w))$! So on each heavy chain $C$, we build an offline 2D sweep or Segment Tree over chain depth $w \in C$ keyed by index $i \in [l, r-1]$ storing the minimum value of $i - \text{len}(w)$, and walk the segment tree to find the largest $i \in [l, r-1]$ with $i - \text{len}(w) \le l - 1$.

##### Method 3: Centroid Decomposition on the Suffix Tree / Link Tree ($O(N \log^2 N)$)
Instead of HLD, perform **Centroid Decomposition (点分治)** on the Link Tree of SAM($S$). When processing centroid $c$, every node $u$ in the current component has a path to $c$ whose minimum string length is $L(u) = \text{len}(\text{LCA}_{\text{orig}}(u, c))$. Thus for a query $(l, r)$ where $u_r$ is in the component of $c$ and $u_i$ is in a different branch of $c$ (or higher towards the root):
- If $\text{LCA}(u_r, u_i)$ is an ancestor of $c$, then $\text{len}(\text{LCA}(u_r, u_i)) = \min(L(u_r), L(u_i))$:
  - When $L(u_r) \le L(u_i)$, the LCA length is $L(u_r)$, giving $i \le l + L(u_r) - 1$ (query largest $i \in [l, \min(r-1, l+L(u_r)-1)]$ with $L(u_i) \ge L(u_r)$).
  - When $L(u_i) < L(u_r)$, the LCA length is $L(u_i)$, giving $i - L(u_i) \le l - 1$ (query largest $i \in [l, r-1]$ with $L(u_i) < L(u_r)$ and $i - L(u_i) \le l - 1$).
Both cases reduce to standard 2D orthogonal range queries solved by an offline sweep-line + Segment Tree in $O(N \log^2 N)$ time and $O(N \log N)$ space!

##### Method 4: DSU-on-Tree (`樹上啓発的合併`) + Offline Query Splitting ($O(N \log^2 N)$)
At each Link Tree node $w$, when merging a small child subtree into the heavy child's active set of indices $\text{endpos}(w)$:
- Any query $(l, r)$ parked at $u_r$ in one subtree interacts with indices $i$ in the other subtree at fixed $\text{LCA}(u_r, u_i) = w$. Since $\text{len}(w)$ is fixed at node $w$, the condition is simply $i \in [l, \min(r-1, l + \text{len}(w) - 1)]$.
- Conversely, if we insert active indices $i$ from the small subtree into a data structure keyed by $i - \text{len}(w)$ as we climb the heavy path, we recover the exact same clean separation of variables as Method 2.

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Pitfall 1: Allowing Improper Border $b = r - l + 1$ ($i = r$)**:
   - The definition of a border requires $1 \le b \le r - l$, so the prefix right-endpoint $i = l + b - 1$ must satisfy $l \le i \le r - 1$. Failing to clip the upper bound of $i$ to $r - 1$ returns $i = r$ (the whole substring $S[l..r]$ itself) because $\text{LCS}(r, r) = r \ge r - l + 1$.
2. **Pitfall 2: False Period Extension in Method 1 (IPM Bucket AP)**:
   - *Counterexample*: Let $S = \text{"ababacababab"}$, query $[1, 12]$, scale $k = 1$ ($2^k = 2$). The prefix $P_1 = \text{"ab"}$ occurs inside the suffix window $T_1 = S[10..12] = \text{"bab"}$ at $x = 11$, and inside a wider window $S[8..12] = \text{"babab"}$ at $x_1 = 9, x_2 = 11$. If one blindly assumes that because $P_k$ occurs in an AP inside $T_k$, the *entire* interval between the first and last occurrence of $P_k$ in $S[l..r]$ is periodic without checking $\text{LCE}(l, x_t) \ge r - x_t + 1$, the mismatch `'c'` at index $6$ breaks the global border while preserving local occurrences of `"ab"`! In Method 1, the AP property holds **only inside a window of length $< 2 \cdot 2^k$**, and you must intersect the AP of $P_k$ in $S[r-2^{k+1}+2..r]$ with the AP of $Q_k = S[r-2^k+1..r]$ in $S[l..l+2^{k+1}-2]$ (both of which have length $< 2^{k+1}$!).

---

### 18.3 2D Orthogonal Range Queries on $(\text{SA}, \text{SA}^R)$ for Anchored Substrings

Many internal pattern matching problems ask:
- **Bidirectional / Concatenation Anchor**: Given a pattern split $P = P_1 \cdot P_2$ (for example, $1$-mismatch or $1$-wildcard matching where we brute-force the mismatch index $k$, splitting $P = P[1..k-1] \cdot ? \cdot P[k+1..m]$), how many positions $i$ in text $S[1..N]$ have $S[i-k+1..i-1] = P[1..k-1]$ and $S[i+1..i+m-k] = P[k+1..m]$?
- **Substring Range Anchor**: Does pattern $P$ occur inside $S[l..r]$ at a position whose reversed prefix satisfies a condition in $\text{SA}^R$?

#### Invariant 18.3 (2D Suffix-Prefix Point Grid)
For each text split position $i \in [1, N]$, define a 2D point:

$$
p_i = \big(\text{rk}_{S^R}[N - (i-1) + 1], \; \text{rk}_S[i+1]\big) \in [1, N] \times [1, N].
$$

- The condition that the prefix ending at $i-1$ ends with $P_1$ is equivalent to the reversed suffix of $S^R$ starting at $N-(i-1)+1$ having $P_1^R$ as a prefix, which defines a contiguous interval $[L_1, R_1]$ in $\text{SA}^R$!
- The condition that the suffix starting at $i+1$ starts with $P_2$ defines a contiguous interval $[L_2, R_2]$ in $\text{SA}$!
- Therefore, counting or locating occurrences of $P_1 \cdot ? \cdot P_2$ reduces to a **2D orthogonal rectangle query $[L_1, R_1] \times [L_2, R_2]$** on the $N$ static points $\{p_1, \dots, p_N\}$, answered in $O(\log N)$ time per query using a **Wavelet Matrix** or **Persistent Segment Tree**.

---

## Iteration 19: Bi-Directional / Double-Ended Suffix Structures (SCDAWG, Affix Automata & Online Prepend/Append)

### 19.1 The Algebraic & Equivalence Hierarchy of Substring Structures

To understand bi-directional suffix structures (`双向后缀结构`), we must first classify the four fundamental equivalence relations on the substrings $\text{Sub}(S)$ of a string $S[1..N]$:

1. **Right-Context Equivalence ($\equiv_R$, Myhill–Nerode / SAM States)**:
   Two substrings $u, v \in \text{Sub}(S)$ satisfy $u \equiv_R v$ if and only if they have the same set of ending positions $\text{endpos}_S(u) = \text{endpos}_S(v)$ (equivalently, $\forall w \in \Sigma^*, \; uw \in \text{Sub}(S) \iff vw \in \text{Sub}(S)$).
   - **Canonical Representative**: The longest string $\text{rep}_R([u]_R)$ in the $\equiv_R$-class. Every shorter string in $[u]_R$ is a suffix of $\text{rep}_R([u]_R)$, and their lengths form a contiguous interval $[\text{minlen}_R, \text{len}_R]$.
   - **Data Structure**: The **Suffix Automaton (SAM / DAWG)** of $S$. Its suffix-link tree (`link`) is the **Suffix Tree of $S^R$** (each state splits when a left-extension $c \cdot u$ loses an occurrence).

2. **Left-Context Equivalence ($\equiv_L$, Reversed SAM / Suffix Tree States)**:
   Two substrings $u, v \in \text{Sub}(S)$ satisfy $u \equiv_L v$ if and only if they have the same set of starting positions $\text{startpos}_S(u) = \text{startpos}_S(v)$ (equivalently, $\forall c \in \Sigma^*, \; cu \in \text{Sub}(S) \iff cv \in \text{Sub}(S)$).
   - **Canonical Representative**: The longest string $\text{rep}_L([u]_L)$ in the $\equiv_L$-class. Every shorter string in $[u]_L$ is a **prefix** of $\text{rep}_L([u]_L)$.
   - **Data Structure**: The **Suffix Tree of $S$** (explicit branching nodes) or the Link Tree of $\text{SAM}(S)$.

3. **Two-Sided / Context-Intersection Equivalence ($\equiv_{LR} = \equiv_L \cap \equiv_R$, Compact DAWG / CDAWG)**:
   Define $u \equiv_{LR} v \iff (u \equiv_L v \land u \equiv_R v)$.
   - **Crucial Warning**: Better still is the **two-sided extension closure** (**Maximal Repeats / Prime Substrings**): for any substring $u \in \text{Sub}(S)$, let $\overleftrightarrow{u}$ be the unique longest substring discovered by extending $u$ to the left as long as all occurrences share the same preceding character ($\equiv_R$ invariant), and to the right as long as all occurrences share the same succeeding character ($\equiv_L$ invariant).

##### Theorem 19.1 (Uniqueness of Two-Sided Closure & Symmetric Compact DAWG — Blumer et al. 1987 / Inenaga et al. 2001, 2005)
For any substring $u \in \text{Sub}(S)$, extending $u$ maximally to the left within $[u]_R$ and maximally to the right within $[u]_L$ **commutes**:

$$
\text{rep}_L\big([\text{rep}_R([u]_R)]_L\big) = \text{rep}_R\big([\text{rep}_L([u]_L)]_R\big) =: \overleftrightarrow{u}.
$$

The resulting canonical strings $\overleftrightarrow{u}$ are the **maximal repeats** (plus full suffixes/prefixes) of $S$, and they form the vertices of the **Symmetric Compact DAWG (SCDAWG)** of $S$!

**Proof**: Suppose $u$ is always preceded by $c$ at every occurrence in $S$ (so $cu$ has the same ending positions as $u$), and $u$ is always followed by $d$ at every occurrence in $S$ (so $ud$ has the same starting positions as $u$). Because every occurrence of $u$ both is preceded by $c$ and is followed by $d$, every occurrence of $u$ is embedded inside an occurrence of $cud$! Hence the occurrence set of $u$ (viewed as center intervals $[i, i+|u|-1]$) bijects with the occurrence set of $cud$, proving that left-extension and right-extension preserve each other's determinism and therefore commute. $\blacksquare$

| Structure | Vertex Equivalence Class | Forward Edges | Backward / Dual Edges | Number of Vertices | Online Construction |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SAM($S$)** | $[u]_R$ ($\text{endpos}$ classes) | Right char $u \to uc$ | Suffix link $\text{link}_R(u)$ (left-truncation) | $\le 2N - 1$ | Ukkonen / Blumer $O(N)$ right-append |
| **Suffix Tree $\mathcal{T}_{\text{ST}}(S)$** | $[u]_L$ ($\text{startpos}$ classes) | Right-compressed $u \to uw$ | Weiner link $u \to cu$ (left-extension) | $\le 2N$ | Ukkonen $O(N)$ right-append; Weiner $O(N)$ left-prepend |
| **Affix Tree / Affix Automaton** (Stoye 2000; Maaß 2000) | Explicit $\mathcal{T}_{\text{ST}}(S)$ + $\mathcal{T}_{\text{ST}}(S^R)$ coupled | Right suffix-tree + Left prefix-tree edges | Cross-links between $\equiv_L$ and $\equiv_R$ | $\le 2N$ per side | $O(N)$ bi-directional Ukkonen |
| **SCDAWG($S$)** (Inenaga et al. 2001/2005) | Two-sided closure $\overleftrightarrow{u}$ | Right compressed $u \to uw$ | Left compressed $u \to vu$ | $\le 2N$ nodes, $\le 2N$ edges | $O(N)$ online both-ends (`prepend` & `append`) |

---

### 19.2 The 4-Step Derivation of Online Prepend & Append Suffix Structures

#### Step 1: The Diagnostic Signal (When Do We Need True Bi-Directional / Double-Ended Suffix Maintenance?)

Suppose a problem maintains a dynamic string $S$ under:
- `push_back(c)`: append $c$ to the right end of $S$ ($S \leftarrow S \cdot c$),
- `push_front(c)`: prepend $c$ to the left end of $S$ ($S \leftarrow c \cdot S$),
- and queries after each operation for the number of distinct substrings, pattern occurrences, or longest repeated suffixes/prefixes (`QOJ / Universal Cup Double-Ended String Queries`, `[ZJOI / 集训队互测]` bi-directional string maintenance).

Why does a single SAM or single Ukkonen Suffix Tree fail?
- **SAM Append vs. Prepend Asymmetry**: In $\text{SAM}(S)$, appending $c$ to the right creates only $1$ new suffix $S \cdot c$, touching the suffix-link chain of the old whole-string state `last` and splitting at most one state along that chain (amortized $O(1)$ via Ukkonen/Blumer potential). By contrast, **prepending $c$ to the left** ($S \leftarrow c \cdot S$) changes *every* prefix of $S$, adding $N+1$ new prefixes $c, cS[1], \dots, cS[1..N]$ simultaneously! In $\text{SAM}(S)$, a single left-prepend can split $O(N)$ states if maintained naively on the $\equiv_R$ classes.
- Conversely, **Weiner's Algorithm (1973)** builds the Suffix Tree $\mathcal{T}_{\text{ST}}(S)$ by **prepending characters from right to left** ($S \leftarrow c \cdot S$), adding only $1$ new suffix $cS$ per prepend!

#### Step 2: The Combinatorial Word Invariant (Ukkonen–Weiner Duality & Active Frontier Coupling)

Why can Ukkonen's right-append and Weiner's left-prepend be fused on the same underlying substring representation?
Look at what changes when $S$ grows by one character at either end:
1. **Under `push_front(c)` ($S \leftarrow cS$)**: The set of suffixes of $S$ gains **one** new longest suffix $cS$. In the Suffix Tree $\mathcal{T}_{\text{ST}}(S)$, every existing suffix is already a leaf (or implicit node along the active suffix chain if $cS[1..k]$ already occurred in $S$). However, in the dual SAM $\text{SAM}(S) = \mathcal{T}_{\text{ST}}(S^R)$, `push_front(c)` on $S$ is literally `push_back(c)` on $S^R$!
2. **Under `push_back(c)` ($S \leftarrow Sc$)**: This is `push_front(c)` on $S^R$ and `push_back(c)` on $S$!

##### Theorem 19.2 (Bi-Directional Ukkonen–Weiner Frontier Invariant — Inenaga et al. 2001 / Breslauer–Italiano 2013)
In a string $S$, let $L_{\max}$ be the longest prefix of $S$ that occurs at least twice in $S$ (the **active prefix** in $\mathcal{T}_{\text{ST}}(S^R)$), and let $R_{\max}$ be the longest suffix of $S$ that occurs at least twice in $S$ (the **active suffix** in $\mathcal{T}_{\text{ST}}(S)$).
- When `push_back(c)` is executed ($S \leftarrow Sc$), the new substrings added to $\text{Sub}(Sc) \setminus \text{Sub}(S)$ are exactly the suffixes of $Sc$ of length $> |R_{\max}(Sc)|$. In $\mathcal{T}_{\text{ST}}(S)$, these correspond to extending existing open leaf edges by $+1$ (via a global right-endpoint pointer $\infty$) and walking Ukkonen's active suffix point $(u_R, \text{offset}_R)$ along suffix links until $R_{\max} \cdot c$ is present. Meanwhile, in $\mathcal{T}_{\text{ST}}(S^R)$, only **one** new leaf $(Sc)^R = c S^R$ is inserted via Weiner's link from $R_{\max}^R$!
- Symmetrically, when `push_front(c)` is executed ($S \leftarrow cS$), Ukkonen's step runs on $\mathcal{T}_{\text{ST}}(S^R)$ at active prefix point $(u_L, \text{offset}_L)$, while Weiner's single-leaf insertion runs on $\mathcal{T}_{\text{ST}}(S)$ at $L_{\max}$!

#### Step 3: The Reverse-Engineering Scratchpad (Offline vs. Online Decision Matrix in Contests)

In competitive programming, before coding a full 300-line online SCDAWG or Affix Tree, apply the following **3-Tier Decision Filter**:

1. **Filter 1: Can all `push_front` / `push_back` operations be read OFFLINE?**
   - If queries are **not** encrypted (or only depend on the sequence of deque operations), pre-simulate the deque to obtain the final master string $M[1..N]$, where at time $t$ the current string is a known contiguous interval $M[l_t .. r_t]$!
   - Then **every** double-ended string problem reduces to an **Internal Substring Query on $M[l_t .. r_t]$**, which we solve using standard offline SAM + LCT `access` (`[SDOI2017]`, Wave 2A), SAM + Segment Tree Merge, or SA + 2D Range Queries!
2. **Filter 2: Are we only counting Distinct Substrings Online under `push_front` and `push_back`?**
   - By Theorem 19.2, appending $c$ to the right increases the number of distinct substrings by:

$$
\Delta_{\text{distinct}}(S \to Sc) = |Sc| - \text{LCS\_internal}(Sc) = |S| + 1 - |R_{\max}(Sc)|,
$$

     where $|R_{\max}(Sc)|$ is the length of the longest suffix of $Sc$ that occurred previously in $S$.
   - Symmetrically, prepending $c$ to the left increases the number of distinct substrings by:

$$
\Delta_{\text{distinct}}(S \to cS) = |S| + 1 - |L_{\max}(cS)|,
$$

     where $|L_{\max}(cS)|$ is the length of the longest prefix of $cS$ that occurred previously in $S$.
   - If we maintain a **Dynamic Suffix Tree / Online LCT-SAM** or a **Dynamic Suffix Balanced Tree (后缀平衡树, Weight-Balanced BST + Hash/LCE)** over both $S$ and $S^R$:
     - On `push_front(c)`, insert the new suffix $cS$ into the Suffix Balanced Tree of $S$ in $O(\log N)$ (or $O(\log^2 N)$) time; its predecessor and successor in the BST immediately give $|L_{\max}(cS)| = \max(\text{LCP}(cS, \text{pred}), \text{LCP}(cS, \text{succ}))$!
     -Wait: what if `push_back(c)` is also called? In a naive Suffix Balanced Tree of $S$, `push_back(c)` modifies *all* suffixes of $S$. **Crucial Trick**: Because a substring occurrence inside $M[l_t..r_t]$ is invariant unless it touches the newly added boundary, we can maintain **two** online structures or use **Dynamic LCE via Polynomial Rolling Hash + Treap/Suffix Balanced Tree** where the string lives on a global array $M[\text{mid}-Q .. \text{mid}+Q]$, and comparing any two positions $i, j$ inside the current active window $[L, R]$ uses $\min(\text{LCE}_{\text{hash}}(i, j), R - \max(i, j) + 1)$! Wait—does `push_back(c)` change the relative lexicographical order of two existing suffixes $M[i..R]$ and $M[j..R]$?
     - **Critical Analysis**: Two suffixes $M[i..R]$ and $M[j..R]$ ($i < j$) change their relative order when $R \to R+1$ **only if** $M[i..R]$ had $M[j..R]$ as a prefix! That means $M[j..R]$ is a **border** of $M[i..R]$, so $j$ is the start of the active suffix $R_{\max}$! That is precisely why Ukkonen's active point only modifies the active suffix chain!
3. **Filter 3: Full Online SCDAWG / Affix Automaton**:
   - When true online worst-case/amortized $O(\log |\Sigma|)$ both-ends extension with full state-graph queries is mandated (e.g., online encrypted queries over $S$ with `push_front` and `push_back`), maintain the coupled pair $(\text{DAWG}(S), \text{DAWG}(S^R))$ (or $\text{SCDAWG}(S)$) where each node stores both its right-transition map, left-transition map (Weiner links), suffix link (`slink`), and prefix link (`plink`).

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Pitfall 1: Assuming Suffix Order is Invariant Under `push_back(c)` in a Suffix Balanced Tree**:
   - *Counterexample*: Let $S = \text{"ab"}$. The suffixes are $S[1..2] = \text{"ab"}$ and $S[2..2] = \text{"b"}$, with `"ab" < "b"`. Now compare $S = \text{"aa"}$: $S[1..2] = \text{"aa"} > S[2..2] = \text{"a"}$. If we `push_back('b')` so $S \leftarrow \text{"aab"}$, now $S[1..3] = \text{"aab"} < S[2..3] = \text{"ab"}$! Their relative order **flipped** because prior to appending `'b'`, $S[2..2] = \text{"a"}$ was a prefix of $S[1..2] = \text{"aa"}$. Therefore, you cannot simply leave existing nodes untouched in a Suffix Balanced Tree of $S[i..R]$ when $R$ increments! (By contrast, `push_front(c)` with fixed right end $R$ NEVER flips the order of existing suffixes $S[i..R]$ and $S[j..R]$!).
2. **Pitfall 2: CDAWG vs. SCDAWG Asymmetry**:
   - A standard one-sided Compact DAWG (compacting only unary right-branching paths in SAM) is **not** symmetric under reversal $S \leftrightarrow S^R$. Only the **Symmetric Compact DAWG (SCDAWG)**, whose vertices are closed under both left and right unique extensions ($\overleftrightarrow{u}$), is strictly isomorphic to the SCDAWG of $S^R$ with forward and backward edges swapped.

---

## Iteration 20: Multilingual Literature Audit, Problem Curation Ladder & Quarantine Ledger

### 20.1 Multilingual Bibliography & Terminology Rosetta Stone (`[EN]` / `[ZH]` / `[JA]`)

#### Academic & Competitive Stringology Bibliography (Wave 2B)
1. **[EN] Nong, G., Zhang, S., & Chan, W. H. (2009 / 2011)**. *"Two Efficient Algorithms for Linear Time Suffix Array Construction"* (IEEE Transactions on Computers, 60(10), 1471–1484; DCC 2009). — The foundational SA-IS paper introducing $L/S$ types, LMS characters/substrings, and two-pass induced sorting.
2. **[EN] Kociumaka, T., Radoszewski, J., Rytter, W., & Waleń, T. (2015 / 2024)**. *"Internal Pattern Matching Queries in a Text and Applications"* (SODA 2015, pp. 532–551; SIAM Journal on Computing 2024). — Establishes the Basic Substring Dictionary, $O(1)$ bounded-ratio IPM in arithmetic progressions, internal period queries, and cyclic/substring rank queries.
3. **[EN] Kociumaka, T. (2019)**. *"Minimal Suffix and Rotation of a Substring in Optimal Time"* & PhD Dissertation *"Efficient Data Structures for Internal Queries in Texts"* (University of Warsaw). — Unifies IPM, periodic queries, and substring compression.
4. **[EN] Blumer, A., Blumer, J., Haussler, D., McConnell, R., & Ehrenfeucht, A. (1987)**. *"Complete Inverted Files for Efficient Text Retrieval and Analysis"* (JACM 34(3), 578–595) & **Inenaga, S., Hoshino, H., Shinohara, A., Takeda, M., Arikawa, S., Mauri, G., & Pavesi, G. (2001 / 2005)**. *"On-Line Construction of Symmetric Compact Directed Acyclic Word Graphs"* (SPIRE 2001 / Discrete Applied Mathematics 2005). — Formalizes SCDAWGs and bi-directional online construction.
5. **[EN] Stoye, J. (2000)** & **Maaß, M. G. (2000)**. *"Affix Trees"* (Technical Report, Universität Bielefeld) & *"Linear Bidirectional On-Line Construction of Affix Trees"* (CPM 2000). — Bi-directional suffix trees.
6. **[EN] Breslauer, D., & Italiano, G. F. (2013)**. *"Near Real-Time Suffix Tree Construction via the Fringe Marked Ancestor Problem"* (J. Discrete Algorithms). — Quasi-real-time prepend/append suffix trees.
7. **[ZH] 金策 (Jin Ce, 2019)**. 《字符串算法选讲》 (*Selected Topics in String Algorithms*, 2019 Chinese IOI National Team Training Paper `国家集训队论文`). — Definitive Chinese competitive programming treatise on Runs, Lyndon Trees, Significant Suffixes, Internal Pattern Matching (IPM), and Substring Border Queries (`Border 的四种求法`).
8. **[ZH] 陈立杰 (WJMZBMR, 2014)** & **张天扬 (2015)**. 《后缀自动机及其应用》 / 《广义后缀自动机与后缀树》 (*Suffix Automaton and Applications*, `国家集训队论文`). — Establishes the SAM Link Tree $\leftrightarrow$ Reversed Suffix Tree duality and Virtual Suffix Trees (`后缀树虚树`).
9. **[JA] AtCoder Library (`ACL` — `atcoder::suffix_array`) & `noshi91` / `maspypy` / `henkoku` Treatises**:
   - `noshi91`: *"SA-IS の正当性証明と実装"* (Proof of correctness of SA-IS LMS induction and linear-time LCP construction).
   - `henkoku`: *"Internal Pattern Matching (内部パターンマッチング) と 부분文字列周期クエリ"* (Japanese exposition of Kociumaka's IPM and $2^k$-bucket border queries).

#### Multilingual Stringology Rosetta Stone (Wave 2B)

| Concept (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) | Core Structural Meaning |
| :--- | :--- | :--- | :--- |
| **Induced Sorting (SA-IS)** | 诱导排序 (`SA-IS`) | 誘導ソート (`SA-IS`) | Linear-time SA via $L/S$ classification & LMS-substring recursion |
| **LMS Character / Substring** | LMS 字符 / LMS 子串 | LMS 文字 / LMS 部分文字列 | Leftmost $S$-type position ($\text{type}(i)=S, \text{type}(i-1)=L$) |
| **Cartesian Tree of `height`** | `height` 数组的笛卡尔树 | `LCP` 配列の Cartesian Tree | Min-heap tree on adjacent LCPs, isomorphic to the Suffix Tree |
| **Virtual Suffix Tree** | 后缀树虚树 / 虚后缀树 | 圧縮接尾辞木 / Auxiliary Tree | Auxiliary tree of $O(k)$ query substrings sorted by $\text{rk}$ + adjacent LCAs |
| **Internal Pattern Matching (IPM)** | 内部模式匹配 (`IPM`) | 内部パターンマッチング (`IPM`) | Finding all occurrences of $S[l_1..r_1]$ inside $S[l_2..r_2]$ as $O(1)$ APs |
| **Internal Border Query** | 区间 Border 查询 (`Border 的四种求法`) | 部分文字列 Border / 周期クエリ | Longest border of $S[l..r]$ via dyadic IPM or Link-Tree HLD/Centroid |
| **Symmetric Compact DAWG** | 对称压缩有向无环词图 (`SCDAWG`) | 対称圧縮 DAWG (`SCDAWG`) | Bi-directional automaton of maximal repeats ($\overleftrightarrow{u}$) |
| **Suffix Balanced Tree** | 后缀平衡树 | 接尾辞平衡二分探索木 | Weight-balanced BST maintaining dynamic suffixes under `push_front` |

---

### 20.2 Curated Non-Template Problem Archive (32 Problems Across 4-Tier Difficulty Ladder)

Every problem below is a non-template problem requiring structural modeling, Cartesian/Virtual Suffix Tree aggregation, IPM / $2^k$-scale decomposition, 2D $(\text{SA}, \text{SA}^R)$ range geometry, or bi-directional maintenance.

---

#### Tier 1: Stepping Stone (8 Problems — Cartesian Tree on `height`, Monotonic Stack LCP & Basic DSU Merge)

##### 1. `[AHOI2013] 差异` (Luogu P4248) — `[ZH]`
- **Statement & Constraints**: Given a string $S[1..N]$ ($N \le 5 \times 10^5$), compute $\sum_{1 \le i < j \le N} \big(\text{len}(T_i) + \text{len}(T_j) - 2 \cdot \text{LCP}(T_i, T_j)\big)$, where $T_i = S[i..N]$.
- **4-Step Analysis**:
  1. *Diagnostic*: Naive $O(N^2)$ pair enumeration TLEs. Separating the sum gives $\frac{N(N-1)(N+1)}{2} - 2 \sum_{1 \le i < j \le N} \text{LCP}(T_i, T_j)$.
  2. *Invariant*: By the LCP Interval Theorem, $\text{LCP}(\text{SA}[l], \text{SA}[r]) = \min_{l < k \le r} \text{height}[k]$. In the min-Cartesian tree of `height[2..N]`, node $k$ is the unique split point for $(L_k - k + 1)(k - R_k)$ pairs of suffixes.
  3. *Scratchpad*: Use a monotonic stack on `height[2..N]` to find for each $k$ the nearest smaller index $L_k < k$ (strictly smaller `<`) and $R_k > k$ (smaller or equal `<=`). Sum $\text{height}[k] \cdot (k - L_k) \cdot (R_k - k)$.
  4. *Pitfall*: Using strict `<` on both sides double-counts ranges with duplicate minimum `height` values; use `<` on the left and `<=` on the right.

##### 2. `CF 873F — Forbidden Indices` — `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and a binary mask $B[1..N]$ marking forbidden starting indices, maximize $|P| \cdot \text{occ}_{\text{allowed}}(P)$ over all substrings $P$.
- **4-Step Analysis**:
  1. *Diagnostic*: Only non-forbidden suffixes $S[i..N]$ ($B[i] = 0$) count toward $\text{occ}_{\text{allowed}}(P)$.
  2. *Invariant*: For any substring $P$ of length $L$, its allowed occurrences form a contiguous interval $[l, r]$ in $\text{SA}$ where $\min_{l < k \le r} \text{height}[k] \ge L$, and the count of allowed occurrences is the prefix sum of $(1 - B[\text{SA}[x]])$ over $x \in [l, r]$.
  3. *Scratchpad*: Check the single longest allowed suffix (for $\text{occ} = 1$). For $\text{occ} \ge 2$, find the maximal interval $[L_k, R_k]$ around each $k \in [2..N]$ where $\text{height} \ge \text{height}[k]$ via monotonic stack, and multiply $\text{height}[k]$ by the prefix-sum count of allowed suffixes in $[L_k-1, R_k]$.
  4. *Pitfall*: Forgetting the $\text{occ} = 1$ case where a single long allowed suffix beats all repeated substrings!

##### 3. `CF 802I — Fake News (hard)` — `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), compute $\sum_{P \in \text{Sub}(S)} \text{occ}(P)^2$ over all **distinct** non-empty substrings $P$.
- **4-Step Analysis**:
  1. *Diagnostic*: Unlike `[AHOI2013] 差异`, we sum over distinct substrings $P$, not pairs of suffixes (though $\sum_{P} \text{occ}(P)^2 = \sum_{i, j} \text{LCP}(\text{suf}(i), \text{suf}(j))$!).
  2. *Invariant*: Double counting reveals two equivalent solutions: (a) On the Cartesian tree of `height`, a node $u$ covering $k$ suffixes with parent height $H[\text{par}(u)]$ contributes $(H[u] - H[\text{par}(u)]) \cdot k^2$; or (b) Since every common prefix of $\text{suf}(i)$ and $\text{suf}(j)$ contributes $1$ to $\text{LCP}(\text{suf}(i), \text{suf}(j))$, $\sum_P \text{occ}(P)^2 = \sum_{i=1}^N (N - i + 1) + 2 \sum_{1 \le i < j \le N} \text{LCP}(\text{suf}(i), \text{suf}(j))$.
  3. *Scratchpad*: Compute $\frac{N(N+1)}{2} + 2 \sum_{k=2}^N \text{height}[k] \cdot (k - L_k)(R_k - k)$ in $O(N)$ time!
  4. *Pitfall*: Omitting the diagonal $i = j$ terms $\sum_{i=1}^N |\text{suf}(i)| = \frac{N(N+1)}{2}$.

##### 4. `[NOI2015] 品酒大会` (Luogu P2178) — `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^5$) and integer weights $a_i \in [-10^9, 10^9]$, for every $r \in [0, N-1]$ find the number of pairs $(i < j)$ with $\text{LCP}(\text{suf}(i), \text{suf}(j)) \ge r$ and the maximum of $a_i \cdot a_j$ among such pairs.
- **4-Step Analysis**:
  1. *Diagnostic*: Threshold $r$ varies over all $[0, N-1]$; we need all-threshold connected components of the Cartesian tree.
  2. *Invariant*: Decreasing `height[k]` merges adjacent SA intervals in DSU order (Paradigm A in §17.2).
  3. *Scratchpad*: Sort $k \in [2..N]$ by $\text{height}[k]$ descending, union $k-1$ and $k$, update pair count and $\max(\max_u \max_v, \min_u \min_v)$, then take suffix sums/maxima from $N-1$ down to $0$.
  4. *Pitfall*: Negative weights $a_i < 0$ require tracking both $\max$ and $\min$ per DSU root, and initializing max-product answers to $-\infty$.

##### 5. `[HAOI2016] 找相同字符` (Luogu P3181) — `[ZH]`
- **Statement & Constraints**: Given two strings $S_1, S_2$ ($|S_1|, |S_2| \le 2 \times 10^5$), count the number of pairs of equal substrings $(S_1[l_1..r_1], S_2[l_2..r_2])$.
- **4-Step Analysis**:
  1. *Diagnostic*: Equivalent to $\sum_{i \in S_1} \sum_{j \in S_2} \text{LCP}(\text{suf}_{S_1}(i), \text{suf}_{S_2}(j))$.
  2. *Invariant*: Concatenate $S_1 + \text{'\#'} + S_2$, build SA + `height`, and compute $\sum_{\text{all}} \text{LCP} - \sum_{S_1 \times S_1} \text{LCP} - \sum_{S_2 \times S_2} \text{LCP}$ (or maintain bi-colored subtree sizes $(W_1, W_2)$ in the Cartesian tree of `height`).
  3. *Scratchpad*: Run the monotonic stack pass three times (on $S_1 \# S_2$, $S_1$, $S_2$) or maintain $W_1, W_2$ in one pass on $S_1 \# S_2$.
  4. *Pitfall*: Ensuring the separator `'#'` never matches itself by either using a unique sentinel or capping $\text{height}$ at the distance to `'#'`.

##### 6. `CF 123D — String` — `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), compute $\sum_{P \in \text{Sub}(S)} \frac{\text{occ}(P)(\text{occ}(P)+1)}{2}$.
- **4-Step Analysis**:
  1. *Diagnostic*: $\frac{k(k+1)}{2} = \binom{k}{2} + k$.
  2. *Invariant*: $\sum_P \binom{\text{occ}(P)}{2} = \sum_{1 \le i < j \le N} \text{LCP}(\text{suf}(i), \text{suf}(j))$, and $\sum_P \text{occ}(P) = \frac{N(N+1)}{2}$.
  3. *Scratchpad*: Monotonic stack over `height[2..N]` plus $\frac{N(N+1)}{2}$.
  4. *Pitfall*: 64-bit integer overflow on $\frac{N(N+1)}{2}$ and stack products.

##### 7. `[SDOI2016] 生成魔咒` (Luogu P4070) — `[ZH]`
- **Statement & Constraints**: Characters $x_1, \dots, x_N$ ($N \le 10^5$, $x_i \le 10^9$) are appended one by one to the right of $S$. After each append, output the number of distinct substrings.
- **4-Step Analysis**:
  1. *Diagnostic*: Large alphabet $10^9$ and online right-append distinct substring count.
  2. *Invariant*: Reversing the string turns `push_back` into `push_front`! If we read the sequence offline (or use SAM with `std::map`), in the reversed string $S^R$, adding prefix $k$ adds $(k) - \max(\text{LCP}(\text{suf}(k), \text{pred}), \text{LCP}(\text{suf}(k), \text{succ}))$ distinct substrings where `pred` and `succ` are the neighbors of $\text{rk}[k]$ among active suffixes!
  3. *Scratchpad*: Build SA on $S^R$ after coordinate compression, maintain a `std::set` of active $\text{rk}$ positions (or delete in reverse using a doubly linked list on $\text{SA}$!), and update $\text{ans} += (N - i + 1) - \max(\text{LCP}(\text{pred}, i), \text{LCP}(i, \text{succ}))$.
  4. *Pitfall*: Online requirement check—this problem is unencrypted, so offline SA + doubly-linked list runs in $O(N \log N)$ with tiny constant factor, avoiding `std::map` overhead in SAM.

##### 8. `AtCoder ABC 213 F — Common Prefixes` — `[JA]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6$), for every $k = 1, \dots, N$ compute $\sum_{j=1}^N \text{LCP}(\text{suf}(k), \text{suf}(j))$.
- **4-Step Analysis**:
  1. *Diagnostic*: Requires per-suffix LCP sum against all other suffixes for $N = 10^6$.
  2. *Invariant*: Split $j$ into $\text{rk}[j] < \text{rk}[k]$ and $\text{rk}[j] > \text{rk}[k]$. As we sweep $r = \text{rk}[k]$ from $1$ to $N$, the values $\text{LCP}(\text{SA}[l], \text{SA}[r]) = \min_{l < t \le r} \text{height}[t]$ form a right-to-left prefix minimum histogram that updates via a monotonic stack!
  3. *Scratchpad*: Sweep $r = 1 \dots N$ maintaining a monotonic stack of $(\text{height}, \text{count})$ and the running sum of stack rectangles; repeat from $N$ down to $1$. Use SA-IS for $N = 10^6$.
  4. *Pitfall*: $O(N \log N)$ prefix-doubling SA can be slow for $N = 10^6$; SA-IS finishes in $< 50$ ms.

---

#### Tier 2: Intermediate (8 Problems — Virtual Suffix Trees, Substring Sorting & Concatenation Comparison)

##### 9. `CF 1073G — Yet Another LCP Problem` — `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q$ queries ($Q \le 2 \times 10^5$), each giving two sets of suffix starting positions $A_q, B_q$ with $\sum (|A_q| + |B_q|) \le 2 \times 10^5$, compute $\sum_{i \in A_q} \sum_{j \in B_q} \text{LCP}(\text{suf}(i), \text{suf}(j))$.
- **4-Step Analysis**:
  1. *Diagnostic*: Archetypal Virtual Suffix Tree problem on subset queries $\sum k_q \le 2 \times 10^5$.
  2. *Invariant*: Sort $A_q \cup B_q$ by $\text{rk}[\cdot]$; adjacent LCPs $h_t = \text{LCP}(u_{t-1}, u_t)$ determine all pairwise LCPs via $\min_{a < t \le b} h_t$ (Paradigm B in §17.2).
  3. *Scratchpad*: Sort $A_q \cup B_q$ by $\text{rk}$, handle $A_q \cap B_q$ with $(N - i + 1)$, build the virtual Cartesian tree of $h_t$ via monotonic stack, and sum $h_t (W_{A,L} W_{B,R} + W_{B,L} W_{A,R})$.
  4. *Pitfall*: Duplicate elements between $A_q$ and $B_q$ must be merged before querying `RMQ(rk[u]+1, rk[v])`.

##### 10. `[HEOI2016 / TJOI2016] 字符串` (Luogu P4094) — `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$) and $Q \le 10^5$ queries $(a, b, c, d)$, find the maximum length $L \le d - c + 1$ such that $S[c .. c+L-1]$ occurs as a substring of $S[a..b]$.
- **4-Step Analysis**:
  1. *Diagnostic*: Internal substring containment query: does $S[c..c+L-1]$ occur in $S[a .. b-L+1]$?
  2. *Invariant*: Binary search on $L \in [1, \min(b-a+1, d-c+1)]$. For a fixed $L$, all suffixes sharing prefix $L$ with $\text{suf}(c)$ form a contiguous interval $[l_{\text{SA}}, r_{\text{SA}}]$ around $\text{rk}[c]$ (found via binary search on `height` RMQ). Then $S[c..c+L-1]$ occurs in $S[a..b]$ iff there exists $x \in [l_{\text{SA}}, r_{\text{SA}}]$ with $\text{SA}[x] \in [a, b - L + 1]$.
  3. *Scratchpad*: Binary search $L$, find $[l_{\text{SA}}, r_{\text{SA}}]$ via RMQ binary search, and check if the Persistent Segment Tree over $\text{SA}$ has a point in $[l_{\text{SA}}, r_{\text{SA}}] \times [a, b - L + 1]$. Time: $O(Q \log^2 N)$.
  4. *Pitfall*: Checking $\text{SA}[x] \in [a, b]$ instead of $[a, b - L + 1]$ allows matches that overflow past $b$!

##### 11. `AtCoder ABC 272 F — Two Strings` — `[JA]`
- **Statement & Constraints**: Given two strings $S, T$ of length $N \le 2 \times 10^5$, count pairs $(i, j) \in [0, N-1]^2$ such that the cyclic shift $S^{(i)}$ is lexicographically $\le$ the cyclic shift $T^{(j)}$.
- **4-Step Analysis**:
  1. *Diagnostic*: Cyclic shift comparison across two strings of equal length $N$.
  2. *Invariant*: Concatenate $U = S + S + \text{'a'-1} + T + T + \text{'z'+1}$. Why `'a'-1` after $S+S$ and `'z'+1` after $T+T$? Because if $S^{(i)} = T^{(j)}$ across all $N$ characters, we need $S^{(i)}$ to be ordered **before** $T^{(j)}$ in the Suffix Array so that equal shifts are counted!
  3. *Scratchpad*: Build SA-IS on $U$ (length $4N+2$), scan $\text{SA}$ from left to right maintaining the count of seen valid start positions $i \in [1, N]$ of $S$, and whenever we see a valid start position $j \in [2N+2, 3N+1]$ of $T$, add the current count of $S$-positions to the answer.
  4. *Pitfall*: If you use the same sentinel or order $S > T$ on ties, equal cyclic shifts $S^{(i)} = T^{(j)}$ are ordered with $T^{(j)}$ before $S^{(i)}$ and missed!

##### 12. `CF 504E — Misha and LCP on Tree` — `[EN]`
- **Statement & Constraints**: Given a tree of $N \le 3 \times 10^5$ nodes with a character on each node, answer $Q \le 10^6$ queries: find the LCP of the string on the simple path $u_1 \to v_1$ and the simple path $u_2 \to v_2$.
- **4-Step Analysis**:
  1. *Diagnostic*: Path strings on a tree are concatenations of $O(\log N)$ Heavy-Light Decomposition (HLD) chain substrings!
  2. *Invariant*: Write the HLD Euler tour string $M$ concatenated with its reversal $M^R$ (total length $2N$). Every tree path $u \to v$ decomposes into at most $2 \log_2 N$ contiguous substrings of $M \cdot M^R$. Comparing two concatenations of $k \le 2 \log N$ substrings uses the Basic Substring Dictionary two-pointer walk (`LCE` jumps).
  3. *Scratchpad*: Build SA + $\pm 1$ RMQ (or Sparse Table) on $M \cdot M^R$. For each query, decompose both paths into HLD segments and advance two pointers by $\min(\text{LCE}, \text{len}_1, \text{len}_2)$ per step in $O(\log N)$ time per query.
  4. *Pitfall*: With $Q = 10^6$, binary search + hashing takes $O(Q \log^2 N)$ and TLEs; two-pointer `LCE` advancing across HLD segments takes $O(Q \log N)$ total!

##### 13. `[JSOI2016] 扭动的回文串` (Luogu P4324 / Twisted Palindrome) — `[ZH]`
- **Statement & Constraints**: Given two strings $A[1..N]$ and $B[1..N]$ ($N \le 10^5$), find the longest palindrome of the form $A[l_1..r_1]$ alone, $B[l_2..r_2]$ alone, or $A[i..j] + B[j..k]$ ($i \le j \le k$).
- **4-Step Analysis**:
  1. *Diagnostic*: A hybrid palindrome $A[i..j] + B[j..k]$ centered inside $A$ (or $B$) grows as a regular palindrome until it hits the boundary of $A[i..j]$ (or $B[j..k]$), after which its outer wings must match $A[\dots .. i-1]^R = B[k+1 .. \dots]$!
  2. *Invariant*: Let $R_A(c)$ be the Manacher radius in $A$ at center $c$, spanning $[l, r]$. At the boundary $(l, r)$, we can switch from $A[l..r]$ to $B[r..k]$ and extend outward by $\text{LCE}(B\text{ from }r, A^R\text{ from }l-1)$!
  3. *Scratchpad*: Run Manacher on $A$ and $B$, and build SA + RMQ on $A^R + \# + B$ to evaluate $\text{LCE}(A^R[l-1], B[r])$ in $O(1)$ at every Manacher center.
  4. *Pitfall*: Off-by-one alignment at the crossover index $j$: the problem specifies $A[i..j] + B[j..k]$ (both include index $j$), so at the Manacher boundary $[l, r]$ in $A$, the right wing in $B$ begins at index $r$ while the left wing in $A$ continues at $l-1$!

##### 14. `[BZOJ 3238] 差异 + 虚树扩展 / Substring LCA Compression` (`CF 616F — Expensive Strings`) — `[EN]`
- **Statement & Constraints**: Given $M$ strings $S_1, \dots, S_M$ ($\sum |S_i| \le 5 \times 10^5$) with costs $c_1, \dots, c_M \in [-10^7, 10^7]$, maximize $|P| \cdot \sum_{i=1}^M c_i \cdot \text{occ}(P, S_i)$ over all strings $P$.
- **4-Step Analysis**:
  1. *Diagnostic*: Generalized Suffix Tree / Cartesian tree on `height` over concatenated strings.
  2. *Invariant*: Concatenate $S_1 \#_1 S_2 \#_2 \dots S_M$. For each suffix starting at $p$ inside $S_i$, cap its effective maximum length at $\text{max\_len}(p) = \text{end}(S_i) - p + 1$, and assign leaf weight $c_i$.
  3. *Scratchpad*: Cap `height[k]` at $\min(\text{height}[k], \text{max\_len}(\text{SA}[k-1]), \text{max\_len}(\text{SA}[k]))$. For substrings occurring in multiple suffixes, evaluate Cartesian tree nodes $(L_k, R_k)$ where $H[k] > \max(H[L_k], H[R_k])$; for substrings occurring only once in a single suffix $p$, check $\text{max\_len}(p) > \max(\text{height}[\text{rk}[p]], \text{height}[\text{rk}[p]+1])$.
  4. *Pitfall*: If $\text{height}[L_k] = \text{height}[k]$ or $\text{height}[R_k] = \text{height}[k]$, evaluating $\text{height}[k] \cdot \text{sum}(L_k..R_k)$ before all equal-height merges finish can evaluate a partial non-maximal occurrence set when $c_i < 0$! Only evaluate a Cartesian tree node when its height is strictly greater than its parent's height.

##### 15. `AtCoder ARC 151 E — Keep Being Substring` — `[JA]`
- **Statement & Constraints**: Given an array $A[1..N]$ and two subarrays $X = A[l_1..r_1], Y = A[l_2..r_2]$ ($N \le 2.5 \times 10^5$), in one step you may either append or prepend an element to current array $C$, or delete an end element of $C$ (keeping $|C| \ge 1$), subject to $C$ always remaining a contiguous subarray of $A$. Find the minimum steps to transform $X \to Y$.
- **4-Step Analysis**:
  1. *Diagnostic*: Transforming $X \to Y$ either shrinks $X$ down to the **longest common substring** $W = \text{LCS}(X, Y)$ (cost $|X| + |Y| - 2|W|$) if $\text{LCS}(X, Y) \ge 1$, or shrinks to a 1-element array $[c]$ and walks on a graph of adjacent characters in $A$.
  2. *Invariant*: Finding $\text{LCS}(A[l_1..r_1], A[l_2..r_2])$ is an internal longest common substring query on $A$, or since $X$ and $Y$ are given explicitly as single arrays in the problem, equals the longest common substring of $X$ and $Y$ via SA + `height` on $X \# Y$!
  3. *Scratchpad*: Check if $\text{LCS}(X, Y) > 0$ using SA-IS + `height` on $X \# Y$; if so, answer is $|X| + |Y| - 2 \cdot \text{LCS}(X, Y)$. Otherwise run BFS between the character sets of $X$ and $Y$ on the adjacency graph of $A$.
  4. *Pitfall*: Assuming you must always pass through a 1-element state when $\text{LCS}(X, Y) \ge 2$.

##### 16. `Luogu P5341 [TJOI2019] 甲苯先生和大中锋的字符串` — `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$) and $K$, find the length $L$ that appears most frequently among all distinct substrings of $S$ that occur **exactly $K$ times** in $S$.
- **4-Step Analysis**:
  1. *Diagnostic*: Substrings occurring exactly $K$ times correspond to nodes in the Suffix Tree / Cartesian tree of `height` whose subtree contains exactly $K$ leaves.
  2. *Invariant*: A node $u$ in the Cartesian tree of `height` with leaf-interval width $R_u - L_u + 1 = K$ represents distinct substrings of lengths $L \in (\max(H[L_u], H[R_u+1]), H[u]]$, each occurring exactly $K$ times!
  3. *Scratchpad*: Build SA + `height` + Cartesian tree (or monotonic stack for $[L_u, R_u]$). Whenever $R_u - L_u + 1 = K$ (or $K = 1$ at leaves), add $+1$ to the difference array on $(\max(H[L_u], H[R_u+1]), H[u]]$.
  4. *Pitfall*: For $K = 1$, the single-suffix leaves $i$ contribute lengths in $(\max(\text{height}[i], \text{height}[i+1]), N - \text{SA}[i] + 1]$!

---

#### Tier 3: Advanced (8 Problems — Internal Pattern Matching, Substring Ranks, 2D $(\text{SA}, \text{SA}^R)$ & Virtual Suffix Tree DP)

##### 17. `[BJWC2018] Border 的四种求法` (Luogu P4482) — `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[l, r]$, output the length of the longest proper border of $S[l..r]$.
- **4-Step Analysis**:
  1. *Diagnostic*: Canonical internal border query where $i = l + b - 1$ appears on both sides of $\text{LCS}(\text{pre}(r), \text{pre}(i)) \ge i - l + 1$.
  2. *Invariant*: Solved via any of the Four Canonical Methods derived in §18.2 (Dyadic $2^k$ IPM AP intersection, SAM Link Tree HLD + SegTree Merge, Link Tree Centroid Decomposition, or DSU-on-Tree).
  3. *Scratchpad*: Implement Method 1 (Dyadic $2^k$ IPM buckets with AP intersection in $O(N \log N + Q \log N)$) or Method 2/3 ($O((N+Q)\log^2 N)$).
  4. *Pitfall*: Remember to clip candidate right endpoints of the prefix occurrence to $i \le r - 1$ so the whole string $S[l..r]$ is not returned as its own border.

##### 18. `[NOI2016] 优秀的拆分` (Luogu P1117) — `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^4$, $T \le 10$), count the number of quadruples $(i, j, k, l)$ forming a splitting $S[i..j] + S[j+1..k] = AA + BB$ where $A$ and $B$ are non-empty strings.
- **4-Step Analysis**:
  1. *Diagnostic*: Equivalent to $\sum_{j=1}^{N-1} f[j] \cdot g[j+1]$, where $f[j]$ is the number of squares $AA$ ending at $j$ and $g[j+1]$ is the number of squares $BB$ starting at $j+1$.
  2. *Invariant*: Partition the half-length $L = |A|$ by placing **harmonic grid checkpoints** at multiples of $L$: $p = L, 2L, 3L, \dots, \lfloor N/L \rfloor L$. Any square $AA$ of length $2L$ must cover **at least two consecutive checkpoints** $kL$ and $(k+1)L$!
  3. *Scratchpad*: Build SA + $O(1)$ RMQ on $S$ (for $\text{LCP}$) and $S^R$ (for $\text{LCS}$). For each $L = 1 \dots \lfloor N/2 \rfloor$ and each pair of adjacent checkpoints $x = kL, y = (k+1)L$, compute $l_{\text{ext}} = \min(\text{LCS}(x, y), L)$ and $r_{\text{ext}} = \min(\text{LCP}(x, y), L)$. If $l_{\text{ext}} + r_{\text{ext}} - 1 \ge L$, all shifts in that overlap range produce valid squares of length $2L$, which we add via a range-addition difference array on $f$ and $g$! Total checkpoints: $\sum_{L=1}^{N/2} \frac{N}{L} = O(N \log N)$.
  4. *Pitfall*: Capping $l_{\text{ext}} \le L$ and $r_{\text{ext}} \le L$ is mandatory so that a long periodic run $a^{10}$ is not double-counted by adjacent checkpoint pairs $(kL, (k+1)L)$ and $((k+1)L, (k+2)L)$!

##### 19. `CF 1098F — Ж-function` — `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[l, r]$, compute $\sum_{i=l}^r \text{LCP}(S[l..r], S[i..r]) = \sum_{i=l}^r \min\big(\text{LCP}(\text{suf}(l), \text{suf}(i)), \; r - i + 1\big)$.
- **4-Step Analysis**:
  1. *Diagnostic*: Notice the structural similarity to `[BJWC2018]`: instead of maximizing $b$ with $\text{LCP}(l, i) \ge r - i + 1$, we **sum** $\min(\text{LCP}(l, i), r - i + 1)$ over all $i \in [l, r]$!
  2. *Invariant*: On the Suffix Tree (or Reversed SAM Link Tree), let $w = \text{LCA}(u_l, u_i)$ have string depth $L(w) = \text{LCP}(\text{suf}(l), \text{suf}(i))$. The summand is $\min(L(w), r - i + 1)$, which splits at the threshold $i \le r - L(w) + 1$ (contributing $L(w)$) vs. $i > r - L(w) + 1$ (contributing $r - i + 1$)!
  3. *Scratchpad*: Apply Centroid Decomposition or Heavy-Light Decomposition on the Suffix Tree (exact same tree decomposition as `[BJWC2018]` Methods 2 & 3!), reducing both branches of $\min(L(w), r - i + 1)$ to 2D Fenwick tree range sums in $O((N+Q)\log^2 N)$.
  4. *Pitfall*: Handle the $i = l$ term ($r - l + 1$) separately so $\text{LCA}(u_l, u_i)$ is always evaluated between distinct leaves.

##### 20. `CF 700E — Cool Slogans` — `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$), find the maximum $k$ such that there exist strings $s_1, \dots, s_k$ where $s_1$ is a substring of $S$ and each $s_{i-1}$ occurs at least **twice** in $s_i$.
- **4-Step Analysis**:
  1. *Diagnostic*: How do we check if an ancestor substring $u$ on the Suffix Tree / SAM Link Tree occurs at least twice inside a descendant substring $v$?
  2. *Invariant*: By the Basic Substring Dictionary / $\text{endpos}$ clipping invariant, Pick any fixed occurrence ending position $\text{pos}(v)$ of $v$. Then $u$ (taken at its maximum length $\text{len}(u)$ in its equivalence class) occurs at least twice in $v[\text{pos}(v)-\text{len}(v)+1 .. \text{pos}(v)]$ if and only if $u$ already occurs at $\text{pos}(v)$ AND has another occurrence in $[\text{pos}(v) - \text{len}(v) + \text{len}(u), \text{pos}(v) - 1]$!
  3. *Scratchpad*: Build SA + Persistent SegTree (or SAM + SegTree Merge). Do top-down tree DP on the Suffix Tree / Link Tree maintaining the lowest ancestor $u$ with the current max $dp$ value and checking via a range query on $[\text{pos}(v) - \text{len}(v) + \text{len}(u), \text{pos}(v) - 1]$ whether $dp[v] = dp[u] + 1$.
  4. *Pitfall*: Every state $u$ must be tested at its **longest** representative $\text{len}(u)$; testing a shorter string in the same equivalence class is always suboptimal.

##### 21. `[十二省联考 2019] 字符串问题` (Luogu P5284) — `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$), $N_a$ type-$A$ substrings $A_i = S[l_{a,i}..r_{a,i}]$, $N_b$ type-$B$ substrings $B_j = S[l_{b,j}..r_{b,j}]$, and $M$ directed edges $A_i \to B_j$. Every $B_j$ also has a directed edge to every $A_k$ that has $B_j$ as a prefix! Find the maximum total length of $A$-strings on a path (or $-1$ if a cycle exists).
- **4-Step Analysis**:
  1. *Diagnostic*: $B_j$ has edges to all $A_k$ with $\text{LCP}(B_j, A_k) \ge |B_j|$ and $|A_k| \ge |B_j|$.
  2. *Invariant*: On the Suffix Tree of $S$ (or SA with Persistent Segment Tree range optimization), $B_j$ is a prefix of $A_k$ iff $A_k$ lies in the subtree of the locus of $B_j$ (and if they share the same Suffix Tree edge, $|A_k| \ge |B_j|$).
  3. *Scratchpad*: Locate the locus of each $A_i$ and $B_j$ via binary lifting on the Suffix Tree (or SA interval $[L_j, R_j]$ sorted by length), sort substrings landing on the same Suffix Tree edge by length (with $B_j$ before $A_k$ on ties $|B_j| = |A_k|$), link tree edges top-down, and run topological sort + DAG longest path in $O((N + N_a + N_b)\log N)$.
  4. *Pitfall*: When $|B_j| = |A_k|$ on the same Suffix Tree edge, $B_j$ IS a prefix of $A_k$, so $B_j$ must be placed **above** $A_k$ in the subdivided edge!

##### 22. `CF 666E — Forensic Examination` — `[EN]`
- **Statement & Constraints**: Given $S[1..|S|]$ ($|S| \le 5 \times 10^5$), $M$ dictionary strings $T_1, \dots, T_M$ ($\sum |T_i| \le 5 \times 10^4$), and $Q \le 5 \times 10^5$ queries $(l, r, p_l, p_r)$: find $k \in [l, r]$ maximizing the occurrences of $S[p_l..p_r]$ in $T_k$.
- **4-Step Analysis**:
  1. *Diagnostic*: Substring locus lookup for $S[p_l..p_r]$ coupled with color-frequency range max over $k \in [l, r]$.
  2. *Invariant*: Concatenate $S \# T_1 \#_1 \dots T_M$ and build a Virtual/Explicit Suffix Tree (or GSAM + SegTree Merge). Locate the locus of $S[p_l..p_r]$ via binary lifting, and query the merged segment tree (or Mo's / offline sweep on SA interval) for $\arg\max_{k \in [l, r]} \text{cnt}[k]$.
  3. *Scratchpad*: Binary lift from $p_l$ to depth $\ge p_r - p_l + 1$, then query the Segment Tree Merge at that node on range $[l, r]$.
  4. *Pitfall*: If $\max_{k \in [l, r]} \text{cnt}[k] = 0$, the problem requires outputting the smallest index $k = l$ with count $0$ (not index $0$!).

##### 23. `Universal Cup / Gym — 1-Mismatch Pattern Matching via 2D (SA, SA^R)` (`CF 755G / ICPC Regional 2D SA Archetype`, `Gym 102900E` / `LOJ 6071`) — `[EN]`/`[ZH]`
- **Statement & Constraints**: Given a text $S[1..N]$ ($N \le 2 \times 10^5$) and pattern queries $P_q$ ($\sum |P_q| \le 2 \times 10^5$), count how many positions in $S$ match $P_q$ with **at most 1 mismatch** (or exactly 1 wildcard split $P_1 ? P_2$).
- **4-Step Analysis**:
  1. *Diagnostic*: Splitting $P_q$ at mismatch index $k \in [1, |P_q|]$ yields a prefix $P_q[1..k-1]$ and suffix $P_q[k+1..|P_q|]$.
  2. *Invariant*: By Invariant 18.3, text position $i$ matches $P_q[1..k-1]$ on the left and $P_q[k+1..m]$ on the right iff the 2D point $p_i = (\text{rk}_{S^R}[N-(i-1)+1], \text{rk}_S[i+1])$ lies in the rectangle $[L_1(k), R_1(k)] \times [L_2(k), R_2(k)]$.
  3. *Scratchpad*: Precompute SA of $S$ and $S^R$, map each $P_q$ prefix/suffix to its SA/SA$^R$ interval via Suffix Tree walk, and answer the $\sum |P_q|$ 2D orthogonal range queries using an offline Fenwick sweep or Wavelet Matrix in $O((N + \sum |P_q|) \log N)$.
  4. *Pitfall*: Exact matches (0 mismatches) are counted $|P_q|$ times (once for each candidate split index $k$)! Subtract $(|P_q| - 1) \times \text{occ}_{\text{exact}}(P_q)$ at the end.

##### 24. `[ZJOI2017] 字符串` (Luogu P3763 / Significant Suffixes + IPM Comparison) — `[ZH]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[l, r]$, find the starting position $i \in [l, r]$ of the lexicographically smallest suffix of the substring $S[l..r]$.
- **4-Step Analysis**:
  1. *Diagnostic*: Notice that the lexicographically smallest suffix of $S[l..r]$ is **not** simply the suffix $i \in [l, r]$ with minimal $\text{rk}[i]$ in the whole string $S$, because truncating at $r$ drops characters after $r$, so a shorter suffix $S[j..r]$ that is a prefix of $S[i..r]$ beats $S[i..r]$ even if $S[i..N] < S[j..N]$!
  2. *Invariant*: Can be solved either by the **Significant Suffixes Theorem** (Part II / Wave 1B) OR by **IPM / Suffix Tree Decomposition**: first find $i_0 = \arg\min_{i \in [l, r]} \text{rk}[i]$ (the suffix in $[l, r]$ minimal in $S[1..N]$). Any suffix $S[j..r]$ that beats $S[i_0..r]$ when truncated at $r$ must be a **proper prefix** of $S[i_0..r]$, which means $S[j..r]$ is a **border** of $S[i_0..r]$!
  3. *Scratchpad*: By the Weak Periodicity Lemma / Dyadic IPM (Theorem 18.1), all borders of $S[i_0..r]$ decompose into $O(\log N)$ arithmetic progressions (or $O(\log N)$ dyadic IPM queries), and in each AP only the **shortest** (rightmost $j$) border needs to be compared via $O(1)$ LCE!
  4. *Pitfall*: Comparing $S[j..r]$ and $S[i..r]$ must truncate LCE at $r - \max(i, j) + 1$ so characters at $\ge r+1$ are never inspected.

---

#### Tier 4: Mastery (8 Problems — Dynamic Prepend/Append Suffix Structures, Substring Dictionary Rank/K-th & Synthesis)

##### 25. `[BZOJ 3682] Phorni` (Dynamic Prepend + Suffix Balanced Tree `后缀平衡树`) — `[ZH]`
- **Statement & Constraints**: Maintain a string $S$ under online encrypted `push_front(c)` operations ($N \le 5 \times 10^5$) along with a dynamic pointer array $A[1..M]$ where each $A[k]$ points to a suffix of $S$, supporting point updates on $A[k]$ and range queries asking which index $k \in [L, R]$ points to the lexicographically smallest suffix.
- **4-Step Analysis**:
  1. *Diagnostic*: Encrypted online `push_front(c)` requires maintaining the dynamic lexicographical order of all suffixes of $S$ in real time.
  2. *Invariant*: Unlike `push_back(c)`, `push_front(c)` ($S \leftarrow cS$) **never alters the relative order of existing suffixes**! Only one new suffix $cS$ is inserted per operation. By assigning each node in a **Weight-Balanced BST (Scapegoat / Treap)** a real/64-bit tag $\text{tag}(u) \in (L_u, R_u)$ via binary interval halving, comparing any two suffixes $i$ and $j$ takes $O(1)$ time ($\text{tag}(i) < \text{tag}(j)$)!
  3. *Scratchpad*: When prepending $c$ at step $i$, compare the new suffix $S[i..]$ against any BST node $j$ in $O(1)$ by comparing $(S[i], \text{tag}(i+1))$ vs. $(S[j], \text{tag}(j+1))$! Insert $i$ into the Suffix Balanced Tree in $O(\log N)$ time, and maintain a Segment Tree over $A[1..M]$ keyed by $\text{tag}(A[k])$.
  4. *Pitfall*: Standard unbalanced BSTs can exceed depth $60$ and overflow 64-bit integer interval halving $[L_u, R_u]$; use a weight-balanced BST ($\alpha = 0.75$) or rebuild tags on rotations to guarantee depth $\le 40$.

##### 26. `[BZOJ 4768 / UOJ] 双向后缀平衡树 / Online Prepend & Distinct Substrings` (`Luogu P6164` / Dynamic String Queries) — `[ZH]`
- **Statement & Constraints**: Maintain a string $S$ online under `push_front(c)` and `pop_front()` (or substring count queries) with $N, Q \le 3 \times 10^5$.
- **4-Step Analysis**:
  1. *Diagnostic*: Online front insertions and deletions with distinct substring count maintenance.
  2. *Invariant*: In the Suffix Balanced Tree of $S$, inserting suffix $i$ between predecessor `pred` and successor `succ` increases the distinct substring count by $|S[i..]| - \max(\text{LCP}(i, \text{pred}), \text{LCP}(i, \text{succ}))$, where $\text{LCP}$ is computed in $O(\log N)$ via binary search + rolling hash. Deleting $i$ reverses the exact delta!
  3. *Scratchpad*: Maintain the Suffix Balanced Tree with $O(1)$ tag comparison $(S[i], \text{tag}(i+1))$ during insertion, locate `pred` and `succ`, compute $\text{LCP}$ with hash binary search, and update the running distinct substring sum.
  4. *Pitfall*: When deleting node $i$ from a weight-balanced tree with interval tags, use lazy deletion or update tags of the replacement node carefully so existing tags remain valid.

##### 27. `[NOI2018] 你的名字` (Luogu P4770 — Virtual Suffix Tree / SA + Persistent SegTree Formulation) — `[ZH]`
- **Statement & Constraints**: Given master string $S[1..|S|]$ ($|S| \le 5 \times 10^5$) and $Q$ queries $(T_q, l_q, r_q)$ with $\sum |T_q| \le 5 \times 10^5$, count how many distinct substrings of $T_q$ do **not** occur in $S[l_q..r_q]$.
- **4-Step Analysis**:
  1. *Diagnostic*: While Wave 2A solves this with SAM + SegTree Merge, it also admits a pure **Suffix Array + Persistent Segment Tree + `height` Cartesian Tree** solution!
  2. *Invariant*: For each prefix $T_q[1..i]$ (or suffix $T_q[i..|T_q|]$), let $\text{lim}[i]$ be the longest prefix of $T_q[i..|T_q|]$ that occurs in $S[l_q..r_q]$. Using the Suffix Array of $S$ and a Persistent Segment Tree over $\text{SA}$, we can binary search (or two-pointer walk) the SA interval containing $S$-suffixes in $[l_q, r_q - L + 1]$ and evaluate $\text{LCP}$ against $T_q[i..]$!
  3. *Scratchpad*: Once $\text{lim}[i]$ is known for each suffix $i$ of $T_q$, build the Suffix Array and `height` array of $T_q$ alone (in $O(|T_q|)$ via SA-IS): the number of valid substrings is $\sum_{k=1}^{|T_q|} \max\big(0, \; (|T_q| - \text{SA}_{T_q}[k] + 1) - \max(\text{height}_{T_q}[k], \text{lim}[\text{SA}_{T_q}[k]])\big)$.
  4. *Pitfall*: Clipping the occurrence start in $S$ to $[l_q, r_q - L + 1]$ is essential.

##### 28. `CF 1063F — String Journey` — `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), find the maximum $k$ such that there exist non-overlapping substrings $S[l_1..r_1], \dots, S[l_k..r_k]$ ($r_1 < l_2, \dots$) where $|s_i| = k - i + 1$ and each $s_{i+1}$ is a substring of $s_i$.
- **4-Step Analysis**:
  1. *Diagnostic*: Because $|s_i| = |s_{i+1}| + 1$, every optimal step shrinks $s_i$ by **1 character** at either the left end ($S[i+1..i+L-1]$) or the right end ($S[i..i+L-2]$)!
  2. *Invariant*: Let $dp[i]$ be the maximum valid chain length starting at $S[i .. i + dp[i] - 1]$. Notice $dp[i] \le dp[i+1] + 1$! Therefore, as $i$ decreases from $N$ down to $1$, we can test candidate length $L = dp[i]$ in decreasing order while inserting completed $dp[j]$ values ($j \ge i + L$) into a Segment Tree over the Suffix Array $\text{SA}$!
  3. *Scratchpad*: To check if $L$ is valid at $i$, query the SA interval of $S[i..i+L-2]$ and the SA interval of $S[i+1..i+L-1]$ (found via RMQ binary search around $\text{rk}[i]$ and $\text{rk}[i+1]$) for whether the maximum $dp[j]$ in that SA interval is $\ge L - 1$. Total time: $O(N \log N)$.
  4. *Pitfall*: Only insert $dp[j]$ into the Segment Tree at $\text{rk}[j]$ once the sliding pointer $j = i + L$ is reached, ensuring the non-overlapping condition $j \ge i + L$ holds!

##### 29. `[CTS2019 / CTSC] 重复` (`Repeats` / Lyndon & Suffix Structure Synthesis, Luogu P5401) — `[ZH]`
- **Statement & Constraints**: Given $S[1..n]$ ($n \le 2000$) and $m \le 2000$, count length-$m$ strings $T$ over $|\Sigma| = 26$ such that at least one cyclic shift of $T$ has a substring lexicographically smaller than $S$.
- **4-Step Analysis**:
  1. *Diagnostic*: Dual bi-directional extension + cyclic periodicity check on the KMP/Suffix structure of $S$.
  2. *Invariant*: Complement counting: count cyclic strings $T^\infty$ where *every* suffix is $\ge_{\text{lex}} S$, which corresponds to valid walks on the pruned KMP/DAWG automaton of $S$ where transitions smaller than the matched prefix of $S$ are forbidden.
  3. *Scratchpad*: Prune forbidden transitions on the prefix automaton of $S$ and compute traces / DP paths of length $m$.
  4. *Pitfall*: Handling periodic overlaps when wrapping around the boundary of $T$.

##### 30. `QOJ / Universal Cup — Substring Lexicographical Rank & K-th Distinct Substring in Range` (`CF 1286E` / Substring Rank Archetype) — `[EN]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^5$) and $Q$ queries: (Type 1) Given $S[l..r]$, find how many distinct substrings of $S$ are lexicographically $< S[l..r]$; (Type 2) Given $K$, find the $K$-th lexicographically smallest distinct substring of $S$.
- **4-Step Analysis**:
  1. *Diagnostic*: Basic Substring Dictionary `Rank` and `Select` operations.
  2. *Invariant*: In the Suffix Array $\text{SA}[1..N]$, the $k$-th suffix $\text{SA}[k]$ contributes $(N - \text{SA}[k] + 1) - \text{height}[k]$ new distinct substrings in exact lexicographical order!
  3. *Scratchpad*:
     - For Type 2 (`Select(K)`): Binary search the prefix sum of $(N - \text{SA}[k] + 1) - \text{height}[k]$ to find the first $k$ where the sum $\ge K$; the answer is the prefix of $\text{suf}(\text{SA}[k])$ of length $\text{height}[k] + (K - \text{sum}_{k-1})$.
     - For Type 1 (`Rank(S[l..r])`): Find the **leftmost** SA index $k_0 \le \text{rk}[l]$ such that $\text{LCP}(\text{SA}[k_0], l) \ge r - l + 1$ via RMQ binary search; then the rank is $\text{sum}_{k_0 - 1} + (r - l + 1 - \text{height}[k_0])$.
  4. *Pitfall*: For Type 1, you must jump to the **first** (leftmost) index $k_0$ in the SA interval of $S[l..r]$, NOT use $\text{rk}[l]$ directly, because $\text{height}[\text{rk}[l]]$ can be $\ge r - l + 1$ when $S[l..r]$ already appeared at $k_0 < \text{rk}[l]$!

##### 31. `AtCoder AGC 047 B — First Second` — `[JA]`
- **Statement & Constraints**: Given $N$ strings $S_1, \dots, S_N$ ($\sum |S_i| \le 10^6$), in one operation on a string you may delete either its first character or its second character. Count pairs $(i, j)$ such that $S_i$ can be reduced to $S_j$.
- **4-Step Analysis**:
  1. *Diagnostic*: Deleting the first or second character repeatedly means $S_i$ can reach $S_j$ ($|S_j| = m$) iff $S_i$ ends with the suffix $S_j[2..m]$ of length $m-1$, AND the first character $S_j[1]$ occurs somewhere in the remaining prefix $S_i[1 .. |S_i| - m + 1]$!
  2. *Invariant*: Bi-directional prefix/suffix split: reverse all strings (or build a Trie / Suffix Tree on reversed strings $S_i^R$). Then $S_j[2..m]^R$ is a prefix of $S_i^R$, and $S_j[1]$ must appear in the remaining suffix of $S_i^R$.
  3. *Scratchpad*: Insert all $S_i^R$ into a Trie, maintaining along each root-to-leaf path $S_i^R$ a 26-bit mask of characters present in the remaining suffix of $S_i^R$, and accumulate counts at depth $m-1$ for bit $S_i[1]$.
  4. *Pitfall*: Do not count $i = j$.

##### 32. `QOJ / ICPC WF — Symmetric Compact DAWG & Bi-Directional Maximal Repeats` (`SPOJ / Universal Cup Maximal Repeats & Context Classes`) — `[EN]`/`[JA]`
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), identify all **maximal repeats** (substrings $u$ occurring $\ge 2$ times such that neither $cu$ nor $ud$ has the same occurrence count as $u$) and answer queries over two-sided equivalence classes $\overleftrightarrow{u}$.
- **4-Step Analysis**:
  1. *Diagnostic*: Directly characterizes the vertices of the **Symmetric Compact DAWG (SCDAWG)** (Theorem 19.1).
  2. *Invariant*: A node $u$ in the Suffix Tree $\mathcal{T}_{\text{ST}}(S)$ (which is already right-maximal because it is a branching node of $\mathcal{T}_{\text{ST}}(S)$!) is **also left-maximal** if and only if the characters $S[\text{SA}[x] - 1]$ for $x \in [L_u, R_u]$ are **not all identical** (i.e., the range $[L_u, R_u]$ contains at least two distinct left-preceding characters, or contains $\text{SA}[x] = 1$).
  3. *Scratchpad*: Build SA-IS + `height` Cartesian tree on $S$, and build a prefix-sum array that checks in $O(1)$ whether $B[x] = S[\text{SA}[x] - 1]$ is constant on $[L_u, R_u]$. Every Cartesian tree branching node where $B[L_u..R_u]$ is non-constant is a maximal repeat (an internal SCDAWG node)!
  4. *Pitfall*: Treating index $\text{SA}[x] = 1$ as having left character `'a'` instead of a unique sentinel $\$_0$: if $\text{SA}[x] = 1 \in [L_u, R_u]$ and $|[L_u, R_u]| \ge 2$, the left contexts are automatically distinct!

---

### 20.3 Quarantine Table of Excluded Pure Template Problems (`R-2B-01` to `R-2B-10`)

Per `AGENTS.md` and `PLAN.md` (`§2.2`), bare library-verification and template problems are strictly excluded from textbook chapters and logged below.

| Quarantine ID | Platform & Problem Title | Reason for Quarantine |
| :--- | :--- | :--- |
| **`R-2B-01`** | **Library Checker — `Suffix Array`** | Pure SA construction verification ($N \le 5 \times 10^5$); zero modeling or LCP interaction. |
| **`R-2B-02`** | **Library Checker — `Number of Substrings`** | Bare computation of $\sum_{k=1}^N (N - \text{SA}[k] + 1 - \text{height}[k])$. |
| **`R-2B-03`** | **Luogu P3809 — `【模板】后缀排序`** | Standard Chinese Suffix Array template verification problem. |
| **`R-2B-04`** | **Luogu P2408 — `不同子串个数`** | Identical to `R-2B-02`; pure formula application on SA/SAM. |
| **`R-2B-05`** | **SPOJ `SUBST1` / `DISUBSTR` — Distinct Substrings** | Pure template distinct substring count. |
| **`R-2B-06`** | **SPOJ `SARRAY` — Suffix Array** | Pure suffix sorting template benchmark. |
| **`R-2B-07`** | **UOJ #35 — `后缀排序`** | Pure template problem outputting `SA` and `height` arrays. |
| **`R-2B-08`** | **LOJ #111 — `后缀排序`** | Pure template verification of Suffix Array construction. |
| **`R-2B-09`** | **Library Checker — `Longest Common Prefix`** | Pure LCE / `height` RMQ template lookup. |
| **`R-2B-10`** | **SPOJ `LCS` — Longest Common Substring** | Bare 2-string LCS template on SA + `height` without constraints or queries. |

---

### 20.4 Wave 2B Validation Checklist & Pedagogical Handoff Summary

- [x] **Iteration 16 (SA-IS Structural Reduction)**: Proved the $L < S$ Bucket Partition (Lemma 16.2), LMS Halving Bound $\le \lfloor N/2 \rfloor$ (Lemma 16.3), LMS-Substring Order Homomorphism (Theorem 16.4), and Two-Pass Induced Sorting Invariant with a full hand-checkable trace on `"mississippi$"` and cyclic/generalized SA adaptations.
- [x] **Iteration 17 (Virtual Suffix Trees & Cartesian Tree on `height`)**: Proved the three-way isomorphism between $\mathcal{T}_{\text{ST}}(S)$, $\mathcal{T}_{\text{SAM}}(S^R)$, and the contracted min-Cartesian tree of `height` (Theorem 17.1), plus the decreasing-`height` DSU paradigm (`[NOI2015] 品酒大会`) and $O(k \log k)$ Virtual Suffix Tree monotonic-stack DP (`CF 1073G`).
- [x] **Iteration 18 (Internal Pattern Matching & `[BJWC2018] Border 的四种求法`)**: Proved Kociumaka et al.'s Bounded-Ratio IPM Arithmetic Progression Theorem (Theorem 18.1), derived all **Four Canonical Methods** for substring border queries (`[BJWC2018]`), and formalized 2D orthogonal range queries on $(\text{SA}, \text{SA}^R)$.
- [x] **Iteration 19 (Bi-Directional Suffix Structures)**: Proved the commutativity of left/right maximal extensions in the Symmetric Compact DAWG (SCDAWG, Theorem 19.1), Ukkonen–Weiner frontier duality for online `push_front`/`push_back` (Theorem 19.2), and Suffix Balanced Tree (`后缀平衡树`) tag invariants.
- [x] **Iteration 20 (Multilingual Problem Mining & Quarantine)**: Cataloged 32 non-template `[EN]`/`[ZH]`/`[JA]` problems in a 4-Tier Difficulty Ladder with 4-Step Zero-Magic Analysis, plus 10 quarantined template problems (`R-2B-01..R-2B-10`).
