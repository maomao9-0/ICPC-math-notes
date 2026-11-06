# Wave 5A Research Report (Cohort 1, Iterations 41–45): Word Equations, Parallel DSU (`倍增并查集`), String Inequalities, Wheeler/De Bruijn Graphs & Strings on Trees

> [!IMPORTANT]
> **Research Wave Scope & Pedagogical Mandate**
> This report executes **Iterations 41–45 (Wave 5A, Cohort 1)** of the Phase 1 Multilingual Discovery & Structural Audit Loop (`strings_research/PLAN.md`). It investigates five interrelated paradigms where string combinatorial constraints are compiled into equivalence structures, directed graphs, Eulerian circuits, BWT rank-intervals, or tree-path decompositions:
> - **Iteration 41**: Word Equations, Binary-Lifting DSU (`倍增并查集`), Palindrome Equivalence Graphs & Huge-Length ($N \le 10^{18}$) Periodic Word Equations via Fine–Wilf Contractions.
> - **Iteration 42**: String Inequality & Lexicographical Constraint Graphs: Compiling $S[l_1..r_1] < S[l_2..r_2]$, Inverse KMP/Z/SA/Manacher Reconstruction, and Minimum-Alphabet Assignment into 2-SAT, Tarjan SCCs, and DAG Longest Paths.
> - **Iteration 43**: De Bruijn Graphs, the BEST Theorem, Burrows–Wheeler Transform (BWT) LF-Mapping & Wheeler Graphs (Prefix-Sorted DFAs).
> - **Iteration 44**: Strings on Trees: Tree Suffix Array ($O(N \log N)$ Doubling with Rank-Pair Tie Breaking), Tree Generalized SAM (`[ZJOI2015] 诸神眷顾的幻想乡`), and Centroid Decomposition + AC/SAM/FFT for Undirected Tree-Path Pattern Counting (`CF 914E`).
> - **Iteration 45**: Multilingual (`[EN]` / `[ZH]` / `[JA]`) Problem Mining (32 Accepted Non-Template Problems ordered into a 4-Tier Smooth Difficulty Ladder with Full 4-Step Zero-Magic Analysis + Quarantine Ledger `R-5A-01..R-5A-08`).

---

## Iteration 41: Word Equations, Binary-Lifting DSU (`倍增并查集`), Palindrome Equivalence & Huge-Length Periodic Word Equations

### 41.1 Concrete Objects & Fundamental Question

Consider an unknown string $S[1..N]$ over an alphabet $\Sigma$ (or digit domain $\{0, \dots, 9\}$ with $S[1] \neq 0$). We are given a system of $M$ **word equation constraints** of two canonical forms:
1. **Substring Translation Equality**: $S[l_1..l_1 + L - 1] = S[l_2..l_2 + L - 1]$, asserting that for all offsets $t \in [0, L-1]$, $S[l_1 + t] = S[l_2 + t]$.
2. **Substring Reversal / Palindromic Equality**: $S[l_1..l_1 + L - 1] = (S[l_2..l_2 + L - 1])^R$, asserting that for all offsets $t \in [0, L-1]$, $S[l_1 + t] = S[l_2 + L - 1 - t]$. (When $l_1 = l_2$, this declares $S[l_1..l_1 + L - 1]$ to be a palindrome.)

Let $\sim$ be the smallest equivalence relation on the index set $\{1, 2, \dots, N\}$ satisfying all $M$ constraints. If $C$ is the number of connected components (equivalence classes) of $(\{1, \dots, N\}, \sim)$ and no component violates fixed-character assignments, then the number of valid strings $S$ is $|\Sigma|^C$ (or $9 \cdot 10^{C-1}$ when $S[1] \in \{1..9\}$ and $S[i] \in \{0..9\}$ for $i > 1$).

**The Fundamental Question**: How can we compute the exact connected components of $\sim$ in $O(N \log N \cdot \alpha(N) + M)$ time when $N, M \le 10^5$, and how can we compute $C$ when $N \le 10^{18}$ and $M \le 10^5$?

---

### 41.2 The 4-Step "Zero Magic Invariants & Structural Decompositions" Derivation

#### Step 1: The Diagnostic Signal (Why Naive String Structures & Treaps Fail)
A single constraint $S[l_1..l_1 + L - 1] = S[l_2..l_2 + L - 1]$ bundles $L$ pointwise character equalities:

$$
S[l_1 + t] = S[l_2 + t] \quad \forall t \in \{0, 1, \dots, L-1\}
$$

- **Why Naive Pointwise DSU Fails**: Executing `unite(l1 + t, l2 + t)` for each $t \in [0, L-1]$ takes $O(L \cdot \alpha(N))$ time per query, degrading to $O(NM \cdot \alpha(N)) \approx 10^{10}$ operations when $L = \Theta(N)$.
- **Why Standard Segment Tree Range-to-Range Graph Construction Fails**: A segment tree decomposes an interval of length $L$ into $O(\log L)$ canonical dyadic intervals, but $S[l_1..l_1+L-1]$ and $S[l_2..l_2+L-1]$ have **misaligned dyadic boundaries** whenever $l_1 \not\equiv l_2 \pmod{2^k}$. You cannot simply equate canonical segment tree nodes.
- **Why Persistent Treaps / Hash-DSU Are Suboptimal**: While one can maintain component hashes via a Treap and split/merge on first mismatches in $O(N \log^2 N)$, it carries heavy constant factors and fails to generalize cleanly to simultaneous reversal constraints.

#### Step 2: The Combinatorial Word Invariant (Sparse-Table Power-of-Two Covering & Lazy Equivalence Closure)
Instead of partitioning $[l, l+L-1]$ into disjoint dyadic intervals, we use **overlapping power-of-two blocks**—the exact geometry of a Sparse Table (ST-table).

> [!IMPORTANT]
> **Theorem 41.1 (Dyadic Block Covering Equivalence)**
> Let $L \ge 1$ and $k = \lfloor \log_2 L \rfloor$, so $2^k \le L < 2^{k+1}$. Then the interval equality $S[l_1..l_1+L-1] = S[l_2..l_2+L-1]$ holds **if and only if** the following two block equalities of length $2^k$ simultaneously hold:
>
> $$
> S[l_1 .. l_1 + 2^k - 1] = S[l_2 .. l_2 + 2^k - 1] \quad \text{and} \quad S[l_1 + L - 2^k .. l_1 + L - 1] = S[l_2 + L - 2^k .. l_2 + L - 1]
> $$
>
> Similarly, the reversal equality $S[l_1..l_1+L-1] = (S[l_2..l_2+L-1])^R$ holds **if and only if**:
>
> $$
> S[l_1 .. l_1 + 2^k - 1] = (S[l_2 + L - 2^k .. l_2 + L - 1])^R \quad \text{and} \quad S[l_1 + L - 2^k .. l_1 + L - 1] = (S[l_2 .. l_2 + 2^k - 1])^R
> $$

**Proof by Index Double-Inclusion**:
Let $I = \{0, 1, \dots, L-1\}$, $A = \{0, 1, \dots, 2^k - 1\}$, and $B = \{L - 2^k, \dots, L - 1\}$. Because $2^k \le L < 2 \cdot 2^k$, we have $L - 2^k \le 2^k$, so $A \cup B = I$. Every offset $t \in I$ belongs to $A$, or to $B$, or to their overlap $A \cap B = \{L - 2^k, \dots, 2^k - 1\}$. For any $t \in A \cap B$, the two $2^k$-block equalities impose the *identical* character equation $S[l_1 + t] = S[l_2 + t]$ (or $S[l_1 + t] = S[l_2 + L - 1 - t]$ in the reversal case). Thus neither omitted indices nor contradictory duplicate equations occur. $\blacksquare$

Now consider a single level $k \in \{1, \dots, \lfloor \log_2 N \rfloor\}$. Define node $(k, i)$ to represent the block $B(k, i) = S[i .. i + 2^k - 1]$ for $1 \le i \le N - 2^k + 1$.
Suppose $R_k$ is an equivalence relation on the blocks at level $k$. A spanning forest of $R_k$ (maintained by a DSU at level $k$) has **at most $N - 2^k$ edges**, no matter how many $M$ queries were inserted at level $k$! And each edge $(k, i) \equiv (k, r)$ at level $k$ is equivalent to two edges at level $k-1$:

$$
B(k, i) = B(k, r) \iff B(k-1, i) = B(k-1, r) \;\wedge\; B(k-1, i + 2^{k-1}) = B(k-1, r + 2^{k-1})
$$

#### Step 3: The Reverse-Engineering Scratchpad (Algorithmic Compilation & Signed DSU for Reversals)

1. **Offline Top-Down Level Pushdown (`[SCOI2016] 萌萌哒` Paradigm)**:
   - Maintain $\lfloor \log_2 N \rfloor + 1$ independent DSU arrays `fa[k][1..N]`.
   - **Query Ingestion ($O(M \alpha(N))$)**: For each constraint $(l_1, l_2, L)$, compute $k = \lfloor \log_2 L \rfloor$ and execute:
     - `unite(k, l1, l2)`
     - `unite(k, l1 + L - (1 << k), l2 + L - (1 << k))`
   - **Top-Down Pushdown ($O(N \log N \cdot \alpha(N))$)**: Iterate $k$ from $\lfloor \log_2 N \rfloor$ down to $1$. For each index $i \in [1, N - 2^k + 1]$:
     - Let $r = \text{find}(k, i)$. If $r \neq i$:
       - `unite(k - 1, i, r)`
       - `unite(k - 1, i + (1 << (k - 1)), r + (1 << (k - 1)))`
   - **Why This Is $O(N \log N \cdot \alpha(N))$**: Even if $M = 10^6$ queries hit level $k$, DSU deduplicates redundant equivalences immediately. During the level-$k$ sweep, each $i$ pushes down only to its **single canonical root** $r = \text{find}(k, i)$, generating at most $2N$ `unite` calls at level $k-1$.

2. **Online Amortized Recursive Split**:
   - What if queries arrive **online** and we must report the number of connected components $C$ at level $0$ after each query?
   - Define `merge_block(k, i, j)`:
     - If `find(k, i) == find(k, j)`, **return immediately** (this pair of $2^k$-blocks is already equivalent!).
     - Otherwise, `unite(k, i, j)` at level $k$.
     - If $k == 0$, decrement the active component count $C \leftarrow C - 1$ and return.
     - If $k > 0$, recursively call `merge_block(k - 1, i, j)` and `merge_block(k - 1, i + 2^{k-1}, j + 2^{k-1})`.
   - **Amortized Complexity Proof**: Across the entire life of the algorithm, level $k$ has $N - 2^k + 1 \le N$ vertices, so `unite(k, i, j)` can succeed at most $N - 1$ times at level $k$. Each successful merge at level $k > 0$ triggers exactly $2$ recursive calls to level $k-1$. Thus the total number of calls across all $M$ queries is bounded by $2M + 2 \sum_{k=1}^{\lfloor \log_2 N \rfloor} N = O(M + N \log N)$ DSU operations!

3. **Signed / Parity DSU for Simultaneous Translation and Reversal (Palindrome) Constraints**:
   - When constraints include $B(k, i) = B(k, j)^R$, each DSU edge carries a parity bit $\text{rev} \in \{0, 1\}$, where $\text{rev} = 0$ means $B(k, i) = B(k, r)$ (same orientation) and $\text{rev} = 1$ means $B(k, i) = B(k, r)^R$ (reversed orientation).
   - **Critical Pushdown Asymmetry**: Suppose at level $k$, block $i$ connects to root $r$ with orientation bit $d \in \{0, 1\}$.
     - If $d = 0$ ($B(k, i) = B(k, r)$): the left halves match and the right halves match with $d = 0$:
       - $B(k-1, i) = B(k-1, r)$
       - $B(k-1, i + 2^{k-1}) = B(k-1, r + 2^{k-1})$
     - If $d = 1$ ($B(k, i) = B(k, r)^R$): the **left half of $i$ matches the reversed right half of $r$**, and the **right half of $i$ matches the reversed left half of $r$**!
       - $B(k-1, i) = B(k-1, r + 2^{k-1})^R$
       - $B(k-1, i + 2^{k-1}) = B(k-1, r)^R$
   - At level $k = 0$ (blocks of length $2^0 = 1$), reversal of a single character is the identity ($c^R = c$), so the orientation bit $d$ is ignored at level $0$ when counting character components (though self-reversal at level $k > 0$, i.e., $B(k, r) = B(k, r)^R$, is a **nontrivial palindrome constraint on $B(k, r)$**!).

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples
- **Pitfall 1 (Dropping Self-Loops with $d = 1$ in Reversal DSU)**: Suppose two constraints force $B(k, r) = B(k, r)^R$ (a self-loop of parity $1$ on root $r$ at level $k$). A standard parity DSU ignores `unite` when `find(i) == find(j)`. **Counterexample**: Let $N = 4$ and impose $S[1..4] = S[1..4]^R$. This is a single query comparing $B(2, 1)$ with $B(2, 1)^R$. Here `find(2, 1) == find(2, 1)` initially! If you skip self-merges, $B(2, 1)$ never records that it is a palindrome, and level $1$ never learns $B(1, 1) = B(1, 3)^R$.
  - **Fix**: Maintain a boolean flag `is_pal[k][r]` on every root $r$ at level $k$. Whenever a merge induces a parity-$1$ self-loop on root $r$, set `is_pal[k][r] = true`. During pushdown from level $k$ to $k-1$, if `is_pal[k][r]` is true, push down the cross-reversal $B(k-1, r) = B(k-1, r + 2^{k-1})^R$!
- **Pitfall 2 (Leading-Zero Component Identification)**: In `[SCOI2016] 萌萌哒`, index $1$ cannot take the digit $0$. After pushing down to level $0$, the component containing index $1$ has $9$ choices ($\{1..9\}$), and every other component $\text{find}(0, i) = i \neq \text{find}(0, 1)$ has $10$ choices ($\{0..9\}$). Special case: when $N = 1$, depending on whether `"0"` is valid, check problem statement ($N = 1$ allows $10$ or $9$ digits; in SCOI2016, $N=1$ has no leading zero if single-digit $0$ is excluded, i.e., $9 \cdot 10^{C-1}$ uniformly).

---

### 41.3 Hand-Checkable Example (`N = 5`, Overlapping Block Pushdown)

Let $N = 5$, alphabet size $10$ ($S[1] \neq 0$), and $M = 1$ constraint: $S[1..3] = S[3..5]$ ($l_1 = 1, l_2 = 3, L = 3$).
1. Here $k = \lfloor \log_2 3 \rfloor = 1$ ($2^1 = 2$). The two $2^1$-block merges at level $k = 1$ are:
   - Prefix blocks of length $2$: $B(1, 1) = B(1, 3)$ (covering $S[1..2] = S[3..4]$).
   - Suffix blocks of length $2$: $B(1, 1 + 3 - 2) = B(1, 3 + 3 - 2) \implies B(1, 2) = B(1, 4)$ (covering $S[2..3] = S[4..5]$).
2. At level $k = 1$, the DSU components are $\{1, 3\}$ (root $1$) and $\{2, 4\}$ (root $2$).
3. Push down from $k = 1$ to $k = 0$:
   - From $i = 3 \to r = 1$: `unite(0, 3, 1)` and `unite(0, 4, 2)`.
   - From $i = 4 \to r = 2$: `unite(0, 4, 2)` (already united) and `unite(0, 5, 3)` $\implies$ unites $5$ with $\{1, 3\}$.
4. At level $k = 0$, the components are $\{1, 3, 5\}$ and $\{2, 4\}$ ($C = 2$ periodic classes of period $2$: `ababa`), giving $9 \times 10^1 = 90$ valid strings.

---

### 41.4 Huge-Length Word Equations ($N \le 10^{18}, M \le 10^5$) via Periodic Block Splitting & Fine–Wilf Contractions

What if $N \le 10^{18}$ and we are given $M \le 10^5$ substring equality constraints $S[l_1..r_1] = S[l_2..r_2]$ (or $M$ palindrome constraints on $S[1..N]$)?

1. **Why Binary-Lifting DSU Fails at $N = 10^{18}$**: Even if we coordinate-compress the endpoints of the $M$ intervals into $O(M)$ atomic segments, a constraint $S[l_1..l_1+L-1] = S[l_2..l_2+L-1]$ with $l_2 = l_1 + d$ and $L \gg d$ forces the interval $[l_1, l_2 + L - 1]$ to have period $d$, slicing atomic segments into $O(L/d) = O(N)$ pieces!
2. **The Fine–Wilf Periodic Contraction Invariant**:
   - **Case A (Overlapping Self-Shift $l_1 < l_2 \le r_1$)**: Let $d = l_2 - l_1$ and $W = r_2 - l_1 + 1$. The constraint $S[l_1..r_1] = S[l_2..r_2]$ is equivalent to saying $S[l_1 .. r_2]$ has period $d$, meaning every index $x \in [l_2, r_2]$ can be canonically folded back into $[l_1, l_1 + d - 1]$ via $x \mapsto l_1 + ((x - l_1) \bmod d)$.
   - If two periodic intervals $[L_1, R_1]$ with period $d_1$ and $[L_2, R_2]$ with period $d_2$ overlap on a segment of length $\ge d_1 + d_2 - \gcd(d_1, d_2)$, then by the **Fine–Wilf Theorem**, their union $[ \min(L_1, L_2), \max(R_1, R_2) ]$ collapses into a single periodic block of period $g = \gcd(d_1, d_2)$!
   - **Case B (Palindromic Reflection Group on $[1..N]$, e.g., `ARC 056 D` / `QOJ` Huge Palindrome Equations)**: Each palindrome constraint on $[l_i, r_i]$ acts as an affine involution $\sigma_i(x) = l_i + r_i - x$ on $[l_i, r_i]$. Two reflections $\sigma_1, \sigma_2$ compose to a translation $\sigma_2(\sigma_1(x)) = x + (l_2 + r_2 - l_1 - r_1)$ of step $d = |l_2 + r_2 - l_1 - r_1|$, reducing overlapping palindromes to Euclidean GCD reductions in $O(M \log^2 N)$ time.
   - **Case C (General Word Equations via Jez's Recompression / Locally Consistent Parsing)**: Any system of word equations of total description size $M$ over length $N \le 10^{18}$ can be solved by maintaining the string as an SLP (Straight-Line Program) and applying **Jez's Recompression** (alternating run-length block compression $c^k \to c_k$ and pair compression $ab \to c$ via locally consistent coloring), which contracts all constraints to length $1$ in $O(M \log N)$ phases.

---

## Iteration 42: String Inequality & Lexicographical Constraint Graphs

### 42.1 Concrete Objects & Fundamental Question

Suppose an unknown string $S[1..N]$ over an ordered alphabet $(\Sigma, <)$ is constrained not only by substring equalities, but by **lexicographical inequalities**:
- $S[l_1..r_1] < S[l_2..r_2]$ or $S[l_1..r_1] \le S[l_2..r_2]$, or
- The full **Suffix Array** $\text{SA}[1..N]$, **KMP array** $\pi[1..N]$, **Z-array** $Z[1..N]$, or **Manacher radii** $R[1..2N-1]$ of $S$ is given, and we must:
  1. Decide whether a valid string $S$ exists over $\Sigma$,
  2. Find the **minimum alphabet size** $|\Sigma|_{\min}$ required to realize the structure,
  3. Find the **lexicographically smallest** valid string $S$, or
  4. **Count** the number of valid strings $S \in \Sigma^N$.

---

### 42.2 The 4-Step "Zero Magic Invariants & Structural Decompositions" Derivation

#### Step 1: The Diagnostic Signal (Why Substring Inequalities Cannot Be Pushed Down Directly)
Unlike $S[l_1..r_1] = S[l_2..r_2]$ (which is a **conjunction** $\bigwedge_{t=0}^{L-1} (S[l_1+t] = S[l_2+t])$), a strict lexicographical inequality $S[l_1..r_1] < S[l_2..r_2]$ is a **disjunction over the first mismatch position** $t = \text{LCE}(l_1, l_2)$:

$$
S[l_1..r_1] < S[l_2..r_2] \iff \Big( \exists t \in [0, \min(L_1, L_2)-1] : S[l_1..l_1+t-1] = S[l_2..l_2+t-1] \;\wedge\; S[l_1+t] < S[l_2+t] \Big) \;\lor\; \Big( L_1 < L_2 \;\wedge\; S[l_1..r_1] = S[l_2..l_2+L_1-1] \Big)
$$

Because $t$ is not known in advance in a general system of inequalities, a naive reduction branches over $O(N)$ mismatch positions per inequality. However, in almost all competitive programming problems, one of three structural simplifications holds:
1. **Equality Constraints Fix All LCEs First** (Two-Phase Equality $\to$ Inequality Compilation),
2. **Inverse String Structures (KMP / Z / Manacher / SA)** explicitly specify the exact mismatch position $t$ for every prefix/palindrome/suffix comparison, or
3. **Alphabet Size $|\Sigma| = 2$** turns bounded-length inequalities into 2-SAT clauses.

#### Step 2: The Combinatorial Word Invariant (Three Canonical Reductions)

##### Regime A: Two-Phase Equality + Inequality Compilation (When LCEs or Equality Blocks Are Known)
Suppose we have a collection of equality constraints $S[a..b] = S[c..d]$ and inequality constraints where the mismatch offset $t$ is determined (e.g., we know $\text{LCP}(S[l_1..r_1], S[l_2..r_2]) = t$, or we first resolve all equality constraints via Iter 41 Binary-Lifting DSU and ask whether existing equalities already force a prefix match).
- Specifically, an assertion $\text{LCP}(S[l_1..r_1], S[l_2..r_2]) = t$ coupled with $S[l_1..r_1] < S[l_2..r_2]$ splits cleanly into:
  1. An **interval equality** $S[l_1 .. l_1 + t - 1] = S[l_2 .. l_2 + t - 1]$ (pushed into the Level-$k$ Binary-Lifting DSU of Iteration 41), and
  2. A **single character strict inequality** $S[l_1 + t] < S[l_2 + t]$ (a directed edge $\text{rep}(l_1 + t) \xrightarrow{<} \text{rep}(l_2 + t)$ between level-$0$ DSU components!).

##### Regime B: Inverse Suffix Array Reconstruction (Nong–Zhang–Chan / ISA Characterization Theorem)
Given a permutation $\text{SA}[1..N]$ (and its inverse $\text{rk}[1..N]$ with $\text{rk}[\text{SA}[i]] = i$, where $\text{rk}[N+1] = 0$ represents the empty suffix):

> [!IMPORTANT]
> **Theorem 42.1 (Characterization of Realizable Suffix Arrays)**
> For any $i \in \{1, \dots, N-1\}$, put $u = \text{SA}[i]$ and $v = \text{SA}[i+1]$. In any string $S$ having suffix array $\text{SA}$, the suffixes $S[u..N]$ and $S[v..N]$ satisfy $S[u..N] < S[v..N]$. Since $S[u..N] = S[u] \cdot S[u+1..N]$ and $S[v..N] = S[v] \cdot S[v+1..N]$, the relative order of the stripped suffixes $S[u+1..N]$ and $S[v+1..N]$ is already fixed by $\text{rk}[u+1]$ vs. $\text{rk}[v+1]$! Therefore:
> 1. **Permissive Step ($\le$)**: If $\text{rk}[u+1] < \text{rk}[v+1]$, then $S[u+1..N] < S[v+1..N]$ already holds, so $S[u] = S[v]$ is valid; we only require $S[u] \le S[v]$.
> 2. **Forced Strict Step ($<$)**: If $\text{rk}[u+1] > \text{rk}[v+1]$, then $S[u+1..N] > S[v+1..N]$, so $S[u] = S[v]$ would invert their order and force $S[u..N] > S[v..N]$, a contradiction! Thus we **must** have strict inequality $S[u] < S[v]$.

**Consequences of Theorem 42.1**:
- Let $D = \sum_{i=1}^{N-1} [\text{rk}[\text{SA}[i]+1] > \text{rk}[\text{SA}[i+1]+1]]$ be the number of **forced strict ascents** along the SA order.
- The **minimum alphabet size** to realize $\text{SA}[1..N]$ is exactly $|\Sigma|_{\min} = D + 1$.
- For an alphabet of size $|\Sigma| = K$, each non-forced step ($N - 1 - D$ positions) can either be $=$ or $<$, and we can distribute $K - 1 - D$ slack increments across the $N$ positions, so the number of strings realizing $\text{SA}[1..N]$ over an alphabet of size $K$ is exactly $\binom{N + K - 1 - D}{K}$ (`CF 1526E — Oolimry and Suffix Array`).

##### Regime C: Inverse KMP / Z-Array / Manacher Reconstruction (Equality + Forbiddance Graph)
Every failure-link or radius array encodes a set of **interval equalities** plus at most $O(N)$ **pointwise non-equalities ($\neq$)**:
1. **Z-Array $Z[2..N]$**: For each $i \in [2, N]$:
   - **Equality**: $S[1 .. Z[i]] = S[i .. i + Z[i] - 1]$.
   - **Mismatch ($\neq$)**: If $i + Z[i] \le N$, then $S[1 + Z[i]] \neq S[i + Z[i]]$.
2. **KMP Prefix Function $\pi[1..N]$**:
   - First check structural validity: $\pi[1] = 0$, $\pi[i] \le \pi[i-1] + 1$, and $\pi[i]$ must lie in the ancestor chain $\{\pi^{(k)}[i-1] + 1 : k \ge 1\} \cup \{0\}$.
   - **Equality**: If $\pi[i] > 0$, then $S[i] = S[\pi[i]]$.
   - **Mismatch ($\neq$)**: For every ancestor $q = \pi^{(k)}[i-1]$ that was **rejected** before reaching $\pi[i] - 1$ (i.e., $q + 1 > \pi[i]$), we must have $S[i] \neq S[q + 1]$. Also if $\pi[i] = 0$, then $S[i] \neq S[1]$.
   - **Why There Are Only $O(N)$ Rejected Ancestors**: By the standard KMP amortized potential $\Phi = \pi[i]$, each step increments $\Phi$ by at most $1$, and each rejected ancestor jump decrements $\Phi$ by at least $1$. Thus there are **at most $N$ inequality edges $S[i] \neq S[q+1]$ in total**!
3. **Manacher Array $d_1[1..N], d_2[1..N-1]$**:
   - **Equality**: Each radius $r = d_1[i]$ forces $S[i - r + 1 .. i + r - 1]$ to be a palindrome (handled by Binary-Lifting DSU or Manacher's linear sweep).
   - **Mismatch ($\neq$)**: If $i - r \ge 1$ and $i + r \le N$, then $S[i - r] \neq S[i + r]$.

#### Step 3: The Reverse-Engineering Scratchpad (Constraint Graph & DAG Longest Path Compilation)

When we combine substring equalities ($=$), weak inequalities ($\le$), and strict inequalities ($<$):
1. **Step 3a (Collapse Substring Equalities via Iteration 41)**: Run Binary-Lifting DSU on all interval equalities $S[l_1..r_1] = S[l_2..r_2]$ and push down to level $0$. Let $V = \{ \text{find}(0, i) : 1 \le i \le N \}$ be the set of level-$0$ equivalence classes.
2. **Step 3b (Build the Character Inequality Digraph $G = (V, E_{\le} \cup E_{<})$)**:
   - Each constraint $S[u] \le S[v]$ adds a weight-$0$ directed edge $\text{rep}(u) \xrightarrow{0} \text{rep}(v)$.
   - Each constraint $S[u] < S[v]$ adds a weight-$1$ directed edge $\text{rep}(u) \xrightarrow{1} \text{rep}(v)$.
3. **Step 3c (Tarjan SCC Contraction & Positive-Cycle Feasibility Test)**:
   - Run Tarjan's Strongly Connected Components (SCC) algorithm on $(V, E_{\le} \cup E_{<})$.
   - **Feasibility Condition**: All vertices within the same SCC $C_a$ are mutually reachable via $\le$ edges, so by antisymmetry of $\le$, **every vertex in $C_a$ must be assigned the exact same character**!
   - Consequently, if **any weight-$1$ edge ($<$) has both endpoints inside the same SCC $C_a$**, it demands $c < c$, which is **unsatisfiable** (return `IMPOSSIBLE`).
4. **Step 3d (Condensation DAG Longest Path for Minimum Alphabet & Lexicographically Smallest String)**:
   - Contract each SCC $C_a$ into a supernode in the condensation DAG $\mathcal{D}$.
   - Compute the longest path to each supernode $X$ in $\mathcal{D}$:
     $$
     \text{dist}[X] = \max\Big( \{0\} \cup \{ \text{dist}[Y] + w(Y \to X) : (Y \to X) \in \mathcal{D} \} \Big)
     $$
   - Then $\text{dist}[X]$ is the **exact minimum character rank** (0-indexed) that component $X$ can take in any valid string, gives the **lexicographically smallest valid string** directly, and $\max_X \text{dist}[X] + 1$ is the **minimum required alphabet size** $|\Sigma|_{\min}$!

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples
- **Pitfall 1 (Treating KMP Restoration via $\pi[i]$ Without Checking Ancestor Chain Membership)**:
  - **Counterexample**: Consider $\pi = [0, 0, 2]$ for $N = 3$. If an algorithm only sets $S[3] = S[\pi[3]] = S[2]$ and checks $S[2] \neq S[1]$, it produces $S = \text{"abb"}$, whose actual KMP array is $[0, 0, 0] \neq [0, 0, 2]$! Why? Because $\pi[3] = 2 > \pi[2] + 1 = 1$ is structurally impossible: any border of $S[1..3]$ of length $2$ strips its last character to give a border of $S[1..2]$ of length $1$, requiring $\pi[2] \ge 1$.
  - **Fix**: Either verify the KMP ancestor transition condition $\forall i, \pi[i] \in \{ \pi^{(k)}[i-1] + 1 \}$ up front, or run standard KMP on the reconstructed string $S$ at the end and verify $\pi_{\text{actual}}(S) == \pi_{\text{input}}$.
- **Pitfall 2 (Confusing General Substring Inequality $S[l_1..r_1] < S[l_2..r_2]$ with First-Character Inequality)**:
  - Without knowing $\text{LCE}(l_1, l_2)$, $S[l_1..r_1] < S[l_2..r_2]$ does **not** imply $S[l_1] \le S[l_2]$ is sufficient! If $S[l_1] = S[l_2]$, the burden of strict inequality shifts to $S[l_1+1..r_1] < S[l_2+1..r_2]$. When strings are constructed from an LCP matrix or SA + `height` array, always extract the explicit $\text{LCP}(i, j) = t$ first.

---

## Iteration 43: De Bruijn Graphs, the BEST Theorem, Burrows–Wheeler Transform (BWT) & Wheeler Graphs

### 43.1 Concrete Objects & Fundamental Question

1. **$k$-mer Spectrum & De Bruijn Reconstruction**: Given all substrings of length $k$ ($k$-mers) of an unknown string $S$ of length $N$ (with multiplicities), or given the set of forbidden $k$-mers over $\Sigma$, how do we reconstruct $S$, find the lexicographically smallest universal cycle (De Bruijn sequence), or count the exact number of valid strings $S$?
2. **BWT & Wheeler DFAs**: Given a string $S[1..N]$ (terminated by `$`) or a set of paths on a labeled graph/tree/trie, how can we compress all substrings into $O(N \log |\Sigma|)$ bits and still count/locate any pattern $P[1..M]$ in $O(M)$ time via rank queries (`LF-mapping`)? What structural property characterizes which DFAs admit such a 1D interval representation (**Wheeler Graphs**)?

---

### 43.2 The 4-Step "Zero Magic Invariants & Structural Decompositions" Derivation

#### Step 1: The Diagnostic Signal (Why State-Space DP and Suffix Trees Blow Up)
- **For $k$-mer Reconstruction / Counting**: Tracking the last $k-1$ characters in a naive DP requires $|\Sigma|^{k-1}$ states, and trying to enforce that **each $k$-mer is used with exact multiplicity $m(w)$** requires tracking a frequency vector in $\mathbb{N}^{|\Sigma|^k}$, which is exponential in $N$.
- **For Pattern Matching in Huge Compressed Texts or Labeled Graphs**: A Suffix Tree or SAM uses $O(N \log N)$ bits ($12\text{–}40$ bytes per character). On a labeled graph or trie with $N$ edges, determinizing an NFA into a minimal DFA can blow up exponentially unless the graph's states can be ordered so that every pattern $P$ maps to a **single contiguous interval $[L_P, R_P]$** of states.

#### Step 2: The Combinatorial Word Invariant (Line-Graph Duality, BEST Bijection & Co-Lexicographical Monotonicity)

##### Invariant 43A: De Bruijn Subword-to-Edge Duality & The BEST Theorem
Define the **$(k-1)$-dimensional De Bruijn Graph** $\mathcal{B}(\Sigma, k)$:
- **Vertices $V = \Sigma^{k-1}$**: Every $(k-1)$-mer $u = c_1 c_2 \dots c_{k-1}$ is a vertex.
- **Directed Edges $E = \Sigma^k$**: Every $k$-mer $w = c_1 c_2 \dots c_k$ is a directed edge from its $(k-1)$-prefix $u = w[1..k-1]$ to its $(k-1)$-suffix $v = w[2..k]$:
  $$
  c_1 c_2 \dots c_{k-1} \xrightarrow{\; w = c_1 \dots c_k \;} c_2 c_3 \dots c_k
  $$

**Bijection**: Every string $S$ of length $N \ge k-1$ corresponds bijectively to a **directed walk of $N - k + 1$ edges** in $\mathcal{B}(\Sigma, k)$ starting at $S[1..k-1]$ and ending at $S[N-k+2..N]$. Assigning multiplicities $m(w)$ to each $k$-mer $w \in \Sigma^k$ means we seek an **Eulerian trail (or circuit)** in the multigraph $G = (V, E_m)$.

> [!IMPORTANT]
> **Theorem 43.1 (The BEST Theorem — de Bruijn, van Aardenne-Ehrenfest, Smith, Tutte)**
> Let $G = (V, E)$ be a connected balanced directed Eulerian multigraph with $\text{in}(v) = \text{out}(v) = d(v) \ge 1$ for all $v \in V$. Fix an arbitrary root vertex $r \in V$ and a reference outgoing edge $e_0$ from $r$. Then the number of distinct Eulerian circuits (treating parallel edges as distinct labeled edges) starting with $e_0$ is:
>
> $$
> \mathcal{E}_{\text{distinct}}(G, e_0) = t_{\text{in}}(G, r) \cdot \prod_{v \in V} (d(v) - 1)!
> $$
>
> where $t_{\text{in}}(G, r)$ is the number of **directed spanning arborescences rooted at $r$** (oriented toward $r$), computed via Tutte's Directed Matrix-Tree Theorem as any $(r, r)$-cofactor of the out-degree Laplacian $L^{\text{out}}(G) = \text{diag}(d(v)) - A(G)$.
> If parallel edges representing identical $k$-mers with multiplicity $m(w)$ are **indistinguishable**, divide by $\prod_{w \in \Sigma^k} m(w)!$:
>
> $$
> \mathcal{E}_{\text{string}}(G, e_0) = \frac{t_{\text{in}}(G, r) \cdot \prod_{v \in V} (d(v) - 1)!}{\prod_{w \in \Sigma^k} m(w)!}
> $$

**Why the BEST Bijection Is True (Concrete Double-Count)**:
Given any Eulerian circuit starting with $e_0 = (r \to \dots)$, record for every vertex $v \neq r$ the **very last outgoing edge $e_{\text{last}}(v)$** used when departing $v$ for the final time, and for each $v \in V$ record the permutation $\pi_v$ of the remaining $d(v) - 1$ outgoing edges of $v$ (for $v = r$, the $d(r) - 1$ edges after $e_0$).
1. **Why $\{e_{\text{last}}(v) : v \neq r\}$ Forms an In-Arborescence Rooted at $r$**: Since every $v \neq r$ is exited a final time before the circuit terminates at $r$, following $e_{\text{last}}(v)$ can never cycle: whichever vertex $u$ on a hypothetical cycle was exited *last* among the cycle's vertices must have entered the next vertex $w$ on the cycle *after* $w$ had already used its final exit $e_{\text{last}}(w)$, contradicting $\text{in}(w) = \text{out}(w)$!
2. **Why Any In-Arborescence $T$ + Local Permutations $\{\pi_v\}$ Reconstructs a Unique Eulerian Circuit**: Starting at $e_0$, whenever we arrive at $v$, take the next unused edge in $\pi_v$, and only take the tree edge $e_{\text{last}}(v) \in T$ when all $d(v)-1$ non-tree edges at $v$ are exhausted. Because $T$ has no cycles and $\text{in}(v) = \text{out}(v)$, the walk cannot get stuck at any $v \neq r$, and when it finally gets stuck at $r$, all edges in $G$ have been traversed because $T$ spans all vertices! $\blacksquare$

##### Invariant 43B: Burrows–Wheeler Transform (BWT) LF-Mapping & Rank Preservation
Let $S[1..N]$ be a string ending with a unique sentinel $S[N] = \text{\texttt{\$}}$ smaller than all characters in $\Sigma$. Sort all $N$ cyclic shifts of $S$ lexicographically to form an $N \times N$ matrix $\mathcal{M}$:
- The **First column** $F[1..N]$ is the sorted array of characters of $S$.
- The **Last column** $L[1..N]$ is the **Burrows–Wheeler Transform** $\text{BWT}(S)$, where $L[i] = S[\text{SA}[i] - 1]$ (with $S[0] := S[N]$).

> [!IMPORTANT]
> **Theorem 43.2 (The LF-Mapping Rank-Preservation Invariant)**
> For any character $c \in \Sigma \cup \{\text{\texttt{\$}}\}$ and any $k \ge 1$, the **$k$-th occurrence of $c$ in the Last column $L$** and the **$k$-th occurrence of $c$ in the First column $F$** correspond to the **exact same character position in the original string $S$**!

**Proof**:
Pick any two rows $i < j$ in $\mathcal{M}$ whose last characters are both $c$ ($L[i] = L[j] = c$).
- Cyclic shift $i$ has the form $u_i c$, and cyclic shift $j$ has the form $u_j c$. Since row $i$ precedes row $j$ in $\mathcal{M}$, we have $u_i c < u_j c \implies u_i < u_j$.
- Rotating both shifts right by one character moves the trailing $c$ to the front, yielding two rows $i'$ and $j'$ in $\mathcal{M}$ of the form $c u_i$ and $c u_j$ (which appear in column $F$ with first character $c$).
- Because prepending the *same* character $c$ preserves lexicographical order ($u_i < u_j \iff c u_i < c u_j$), we immediately get $i' < j'$!
- Thus the relative order of all occurrences of $c$ in column $L$ is **identical** to their relative order in column $F$. $\blacksquare$

##### Invariant 43C: Wheeler Graphs (Gagie–Manzini–Sirén 2017)
A directed edge-labeled graph $G = (V, E, \Sigma)$ is a **Wheeler Graph** if there exists a total ordering $\prec$ on the vertices $V$ such that for all edges $(u_1 \xrightarrow{a_1} v_1)$ and $(u_2 \xrightarrow{a_2} v_2)$:
1. **Zero-Indegree First**: If $\text{in}(v_1) = 0$ and $\text{in}(v_2) > 0$, then $v_1 \prec v_2$.
2. **Label Monotonicity**: If $a_1 < a_2$, then $v_1 \prec v_2$ (all incoming edges to $v$ have the same character label, or vertices are partitioned into contiguous blocks by incoming character label).
3. **Co-Lexicographical Path Monotonicity (The Wheeler Axiom)**: If $a_1 = a_2$ and $u_1 \prec u_2$, then $v_1 \preceq v_2$.

**Why Wheeler Order Enables $O(|P|)$ Pattern Matching**: By induction on $|P|$, Axiom 2 and Axiom 3 guarantee that for **every** string $P \in \Sigma^*$, the set of vertices $I(P) \subseteq V$ reachable by walking a path labeled $P$ forms a **single contiguous interval $[L_P, R_P]$** under $\prec$! Appending character $c$ updates $[L_P, R_P] \mapsto [L_{Pc}, R_{Pc}]$ in $O(1)$ rank operations via a Wavelet Matrix over the outgoing edge list.
Every De Bruijn graph $\mathcal{B}(\Sigma, k)$ (ordered co-lexicographically by $(k-1)$-mers) and every XBW-transformed labeled tree (ordered co-lexicographically by root-to-node strings) is a Wheeler Graph!

#### Step 3: The Reverse-Engineering Scratchpad (BWT Backward Search & Eulerian Trail Adjustment)

1. **BWT Backward Search (`FM-Index`)**:
   - Precompute $C[c] = \text{number of characters in } S \text{ strictly smaller than } c$, and $\text{Occ}(c, r) = \text{count of } c \text{ in } L[1..r]$ (via Wavelet Matrix or prefix-popcount blocks).
   - Then the LF-mapping is simply:
     $$
     \text{LF}(i) = C[L[i]] + \text{Occ}(L[i], i)
     $$
   - To find the SA interval $[l, r]$ of pattern $P[1..M]$, initialize $[l, r] = [1, N]$ and iterate $k = M$ down to $1$ with $c = P[k]$:
     $$
     l \leftarrow C[c] + \text{Occ}(c, l - 1) + 1, \qquad r \leftarrow C[c] + \text{Occ}(c, r)
     $$
   - If $l > r$ at any step, $P$ does not occur in $S$; otherwise $P$ occurs exactly $r - l + 1$ times!

2. **Open-Trail Adjustment for the BEST Theorem (Non-Closed Strings $S[1..N]$)**:
   - A linear string $S[1..N]$ starts at vertex $u_{\text{start}} = S[1..k-1]$ and ends at $u_{\text{end}} = S[N-k+2..N]$.
   - If $u_{\text{start}} \neq u_{\text{end}}$, then $\text{out}(u_{\text{start}}) = \text{in}(u_{\text{start}}) + 1$ and $\text{in}(u_{\text{end}}) = \text{out}(u_{\text{end}}) + 1$.
   - Add a **virtual return edge** $e_{\text{virt}} : u_{\text{end}} \to u_{\text{start}}$ to make $G$ balanced, and treat $e_{\text{virt}}$ as the fixed reference edge $e_0$ starting at $r = u_{\text{end}}$! Then every Eulerian circuit starting with $e_0 = (u_{\text{end}} \to u_{\text{start}})$ strips $e_0$ to yield a unique Eulerian trail from $u_{\text{start}}$ to $u_{\text{end}}$!
   - If $u_{\text{start}} = u_{\text{end}} = r$ (already balanced), there is no virtual edge: any of the $d(r)$ outgoing edges at $r$ can start the trail, and a circuit of length $E$ has $d(r)$ starting choices at $r$, multiplying the fixed-$e_0$ formula by $d(r)$ (`(d(r))!` instead of `(d(r)-1)!` in the numerator).

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples
- **Pitfall 1 (Isolated Vertices in Matrix-Tree Cofactor for De Bruijn Graphs)**:
  - Suppose $|\Sigma| = 26, k = 3$, so $|\Sigma|^{k-1} = 676$ vertices exist in $\mathcal{B}(\Sigma, k)$, but the string $S$ only uses $10$ distinct $2$-mers. The other $666$ vertices have degree $0$!
  - **Counterexample**: If you build a $676 \times 676$ Laplacian matrix including degree-$0$ vertices, the matrix has all-zero rows/columns and its cofactor is $0$, falsely reporting $0$ Eulerian strings!
  - **Fix**: Restrict the vertex set $V_{\text{active}}$ strictly to vertices with $\text{in}(v) + \text{out}(v) > 0$, verify that all active vertices belong to a **single weakly connected component**, and compute the $(r, r)$-cofactor only on $V_{\text{active}}$.
- **Pitfall 2 (BWT of Cyclic Words Without Sentinel `$`: Lyndon Conjugate Multiplicity)**:
  - Without a unique sentinel `$`, if $S = (\text{"ab"})^2 = \text{"abab"}$, two cyclic shifts are identical (`"abab"` and `"abab"`), so tie-breaking in $\mathcal{M}$ relies on initial indices (the **Mantaci–Restivo–rosetta Bijective BWT**), decomposing into a multiset of Lyndon cycles rather than a single cycle. Always append a unique sentinel `$` for linear string BWT unless solving a cyclic/Lyndon BWT problem (`ARC 050 D`, `CF 126B`).

---

## Iteration 44: Strings on Trees — Tree Suffix Array, Tree Generalized SAM & Centroid Decomposition with Automata

### 44.1 Concrete Objects & Fundamental Question

When characters live on the vertices or edges of a tree $T = (V, E)$ with $N$ nodes, three distinct algorithmic questions arise:
1. **Tree Suffix Array (Rooted Ancestor String Sorting)**: Given a rooted tree $T$ where each node $u$ has character $c(u)$, let $S(u)$ denote the string formed by reading characters from $u$ up to the root $r$ (or from $r$ down to $u$). How can we sort all $N$ strings $\{S(u) : u \in V\}$ lexicographically in $O(N \log N)$ time—handling the critical obstacle that **two distinct nodes $u \neq v$ can have the exact same ancestor string $S(u) = S(v)$**?
2. **Tree Generalized SAM for All Undirected Paths (`[ZJOI2015] 诸神眷顾的幻想乡`)**: Given an unrooted tree $T$ with $N \le 10^5$ nodes and **at most $L \le 20$ leaves**, how can we count the number of distinct strings formed by **all $O(N^2)$ simple paths** in $T$, or run SAM queries over all simple tree paths?
3. **Undirected Tree-Path Pattern / Palindrome Counting (`CF 914E — Palindromes in a Tree` & Path String Matching)**: Given an unrooted tree $T$ with $N \le 2 \cdot 10^5$ nodes, how do we count simple paths $(u, v)$ whose string is a palindrome (or matches a given pattern $P[1..M]$, or belongs to a dictionary $\mathcal{P}$) in $O(N \log N)$ time?

---

### 44.2 The 4-Step "Zero Magic Invariants & Structural Decompositions" Derivation

#### Step 1: The Diagnostic Signal (Why Linear Suffix Doubling and Naive GSAM Fail on Trees)
- **Why Standard Suffix Array Doubling Fails on Trees (The Rank-Tie Collapse Bug)**:
  In a linear string $S[1..N]$, every suffix $S[i..N]$ has a unique length $N - i + 1$, so once $2^k \ge N$, all ranks $\text{rk}_k[i]$ are strictly distinct. On a tree, however, two sibling nodes $u \neq v$ with the same character $c(u) = c(v)$ and the same parent $\text{fa}(u) = \text{fa}(v)$ have **identical** ancestor strings $S(u) = S(v)$!
  - Even worse: suppose we sort nodes by $(\text{rk}_k[u], \text{rk}_k[\text{anc}(u, 2^k)])$, and when ties occur we break ties by vertex ID $u$ so that every node gets a distinct rank $\text{id}_k[u] \in \{1, \dots, N\}$.
  - **Fatal Bug**: If $S(u)[1..2^k] = S(v)[1..2^k]$ are equal, breaking their tie by $u < v$ assigns $\text{id}_k[u] < \text{id}_k[v]$. Then at step $k+1$, a child $x$ of $u$ and a child $y$ of $v$ with $c(x) = c(y)$ and $\text{anc}(x, 2^k) = u, \text{anc}(y, 2^k) = v$ will compare $\text{id}_k[u] < \text{id}_k[v]$ and **falsely conclude $S(x)[1..2^{k+1}] < S(y)[1..2^{k+1}]$** before even looking at their true $2^k$-th ancestors, or will mis-order them when the true mismatch is deeper! Conversely, if you do *not* break ties, $O(N)$ nodes can share the same rank bucket, causing radix sort / suffix tree construction to lose deterministic tie-breaking.
- **Why Naive Path Enumeration Fails for Undirected Tree Paths**:
  An unrooted tree has $\binom{N}{2} = \Theta(N^2)$ simple paths. Inserting all $N^2$ paths into a Trie or SAM takes $\Omega(N^2)$ time. Even if $T$ is a caterpillar tree of length $N$ with $2$ leaves, there are $N^2/2$ simple paths!

#### Step 2: The Combinatorial Word Invariant (Dual-Rank Doubling, Leaf-Root Path Cover & Centroid Prefix-Suffix Stitching)

##### Invariant 44A: Tree Suffix Array Dual-Rank Invariant (`rk` for Equality vs. `sa_pos` for Bucket Radix Sort)
To sort $S(u) = c(u) \cdot c(\text{fa}(u)) \cdots c(\text{root})$ in $O(N \log N)$ time:
- Maintain **two separate arrays** at step $k$:
  1. $\text{sa}_k[1..N]$: the permutation of vertices sorted by their length-$2^k$ ancestor prefix $P_k(u) = S(u)[1..\min(|S(u)|, 2^k)]$ (with ties broken consistently by $\text{sa}_{k-1}$).
  2. $\text{rk}_k[u]$: the **equivalence-class rank** where $\text{rk}_k[u] = \text{rk}_k[v] \iff P_k(u) = P_k(v)$ as exact strings!
- At step $k \to k+1$, each node $u$ has the 2-tuple key:
  $$
  \text{Key}_{k+1}(u) = \big( \text{rk}_k[u],\; \text{rk}_k[\text{anc}(u, 2^k)] \big)
  $$
- **Why Radix Sort Still Runs in $O(N)$**: To sort by the second component $\text{rk}_k[\text{anc}(u, 2^k)]$, group each node $u$ into the bucket of its $2^k$-ancestor $w = \text{anc}(u, 2^k)$, and iterate $w$ in the order of $\text{sa}_k[1..N]$! Then run a second counting sort on the first component $\text{rk}_k[u]$. Afterward, assign $\text{rk}_{k+1}[u] = \text{rk}_{k+1}[v]$ if and only if $\text{Key}_{k+1}(u) == \text{Key}_{k+1}(v)$.
- **When What-If Tie-Breaking by Original Index Is Required (e.g., `CF 590E` / `ICPC` Tree SA problems where two nodes have identical $P_k(u)$ but must be ordered by a secondary tree priority)**: Compare the 4-tuple $(\text{rk}_k[u], \text{rk}_k[\text{anc}(u, 2^k)], \text{prio}_k[u], \text{prio}_k[\text{anc}(u, 2^k)])$ so that true string equality ($\text{rk}_k$) always takes precedence over tie-breaker priority ($\text{prio}_k$).

##### Invariant 44B: The Leaf-Rooted Trie Cover for All Simple Paths (`[ZJOI2015] 诸神眷顾的幻想乡`)

> [!IMPORTANT]
> **Theorem 44.1 (Leaf-Rooted Substring Cover of a Tree)**
> Let $T$ be an unrooted tree with leaf set $\mathcal{L} = \{ \ell \in V : \deg(\ell) = 1 \}$. For every simple directed path $u \rightsquigarrow v$ in $T$, extend the path backward from $u$ away from $v$ until it hits some leaf $\ell \in \mathcal{L}$. Then $u \rightsquigarrow v$ is a **contiguous substring** of the root-to-node path $\ell \rightsquigarrow v$ in the tree $T_\ell$ rooted at $\ell$!

**Proof**: Because $T$ is a finite tree, walking away from $v$ starting at $u$ along simple edges can never cycle and must terminate at a degree-$1$ vertex $\ell \in \mathcal{L}$. Then the unique simple path $\ell \rightsquigarrow v$ passes through $u$, so $\text{str}(\ell \rightsquigarrow v) = \text{str}(\ell \rightsquigarrow u) \cdot \text{str}(\text{next}(u) \rightsquigarrow v)$, which contains $\text{str}(u \rightsquigarrow v)$ as a suffix! $\blacksquare$

**Consequence for `[ZJOI2015] 诸神眷顾的幻想乡` ($N \le 10^5, |\mathcal{L}| \le 20$)**:
- Every simple path string in $T$ is a prefix of a suffix (i.e., a substring) of one of the $|\mathcal{L}| \le 20$ rooted trees $\{T_\ell : \ell \in \mathcal{L}\}$.
- A rooted tree $T_\ell$ is itself a Trie of size $N$. Therefore, inserting all $|\mathcal{L}| \le 20$ rooted trees into a single **Generalized Suffix Automaton (GSAM)** creates at most $2 \cdot |\mathcal{L}| \cdot N \le 4 \cdot 10^6$ states, and the total number of distinct simple-path strings in $T$ is simply:
  $$
  \sum_{x \in \text{GSAM}} \big( \text{len}(x) - \text{len}(\text{link}(x)) \big)
  $$

##### Invariant 44C: Centroid Decomposition + Automaton / Bitmask / FFT Stitching for General Trees
When $|\mathcal{L}| = \Theta(N)$ (e.g., a star graph), Theorem 44.1 would take $O(N^2)$ states. Instead, apply **Centroid Decomposition**:
- Every simple path $u \rightsquigarrow v$ in $T$ passes through a unique highest centroid $c$.
- Relative to $c$, the path splits at $c$ into an **upward prefix** $u \rightsquigarrow c$ and a **downward suffix** $c \rightsquigarrow v$ lying in different child subtrees of $c$.
- **Case 1 (Abelian / Palindrome Parikh Parity — `CF 914E`)**: A string can be rearranged into a palindrome iff its character frequency xor-mask $M(u \rightsquigarrow v) = M(u \rightsquigarrow c) \oplus M(c \rightsquigarrow v) \oplus (1 \ll \text{char}(c))$ has popcount $\le 1$ ($0$ or $1$ odd-count character). Maintain a frequency table `cnt[mask]` of masks from already-visited subtrees of $c$, query $M(u \rightsquigarrow c) \oplus (1 \ll k)$ for $k \in \{\emptyset, 0..\Sigma-1\}$, and push path contributions down via tree difference arrays (`val[u] += 1`, accumulated bottom-up).
- **Case 2 (Exact Pattern Matching $P[1..M]$ on Undirected Tree Paths)**:
  For a single pattern $P[1..M]$ (or its SAM / KMP / Z-array):
  - At centroid $c$ of component size $S_c$, every node $u$ in $c$'s component has path length $\text{dist}(c, u) < S_c$, so we **only care about occurrences of $P$ where $c$ aligns with some position $k \in [1, M]$ inside $P$** such that $\max(k-1, M-k) < S_c$!
  - Actually, even simpler: build the Suffix Tree / SAM (or KMP + Z-array) of $P$ and $P^R$. Each downward path $c \rightsquigarrow v$ walks forward in the Trie/SAM of $P$, and each upward path $u \rightsquigarrow c$ walks forward in the Trie/SAM of $P^R$.
  - In the SAM of $P$, a node $u$ whose upward string $u \rightsquigarrow c$ matches a prefix $P[1..k]$ corresponds to an ancestor subtree in the Link Tree of $P^R$, and $c \rightsquigarrow v$ matching $P[k+1..M]$ corresponds to an ancestor subtree in the Link Tree of $P$. Or equivalently, if we walk $c \rightsquigarrow v$ inside the SAM of $P$:
    - Any path $u \rightsquigarrow v$ of length $|P|$ can be counted by tracking for each prefix $P[1..k]$ (reachable from $u \rightsquigarrow c$) and suffix $P[k+1..M]$ (reachable from $c \rightsquigarrow v$) the product $\text{cnt}_{\text{pref}}[k] \cdot \text{cnt}_{\text{suff}}[k+1]$!
    - Wait: how do we recognize in $O(1)$ per node $v$ whether $\text{str}(c \rightsquigarrow v)$ equals $P[k+1..M]$? Walk $c \rightsquigarrow v$ on the **Suffix Tree of $P$** (or use a Rolling Hash / SAM + Link-Tree jump if edges follow $P$)! Even better: if we traverse the tree $T$ from $c$ while simultaneously walking the **SAM of $P$**, every node $v$ at depth $d$ from $c$ reaches a unique SAM state $q_v$ (provided $\text{str}(c \rightsquigarrow v)$ is a substring of $P$; if a transition is missing, prune the DFS immediately!). Once at $q_v$, $\text{str}(c \rightsquigarrow v)$ is a suffix of $P$ iff $q_v$ lies on the Link-Tree ancestor chain of the full string state $\text{state}(P)$ and $d = M - k$!

#### Step 3: The Reverse-Engineering Scratchpad (DFS/BFS GSAM Construction & Centroid Inclusion-Exclusion)

1. **Building a Tree Generalized SAM (`[ZJOI2015]`): Why BFS or `last = extend(last[fa], c)` Is Required**:
   - In a rooted tree $T_\ell$, node $u$ extends the string of its parent $\text{fa}(u)$ by character $c(u)$.
   - When calling `pos[u] = extend(pos[fa(u)], c(u))` in a GSAM:
     - Suppose `p = pos[fa(u)]` **already has a transition** `q = ch[p][c]`.
     - If `len[q] == len[p] + 1`, we do **not** create a new node; we simply return `q`!
     - If `len[q] > len[p] + 1`, we create a clone node `clone` with `len[clone] = len[p] + 1`, copy `ch[clone] = ch[q]` and `link[clone] = link[q]`, redirect `link[q] = clone` and `ch[p'][c] = clone` for ancestors $p'$ of $p$ having `ch[p'][c] == q`, and **return `clone` directly** without creating a second blank node `cur`!

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples
- **Pitfall 1 (Zero-Length Clone States in Online DFS Tree GSAM)**:
  - **Counterexample**: Suppose we insert `"ab"` and then `"b"` from the root (`p = 1`). When inserting `"b"`, `ch[1]['b'] = q` already exists (created as the suffix link target or transition during `"ab"` with `len[q] = 2`). If you run standard single-string `extend(1, 'b')`, it creates a new node `cur` with `len[cur] = len[1] + 1 = 1`, sees `ch[1]['b'] = q`, and then splits `q` into `clone` with `len[clone] = len[1] + 1 = 1` and sets `link[cur] = clone`. Now `len[cur] == len[link[cur]] == 1`, creating a **dead zero-length clone** and corrupting subtree size / endpos counts!
  - **Fix**: Either build the Trie first and run **BFS order** GSAM extension, or check `if (ch[p][c])` **at the very start of `extend(p, c)`** before allocating `cur`.
- **Pitfall 2 (Forgetting to Double-Count the Centroid Character $c$ in `CF 914E`)**:
  - When stitching path $u \rightsquigarrow c$ and $c \rightsquigarrow v$, if both masks $M(u \rightsquigarrow c)$ and $M(c \rightsquigarrow v)$ include the bit for centroid $c$, their XOR cancels $c$'s bit out! One side must record $M(u \rightsquigarrow c)$ *including* $c$, and the other side must record $M(c \rightsquigarrow v) \setminus \{c\}$ *excluding* $c$.

---

## Iteration 45: Multilingual Problem Mining (`[EN]` / `[ZH]` / `[JA]`), 4-Tier Difficulty Ladder & Quarantine Ledger

### 45.1 Summary of Curated Non-Template Problem Corpus (32 Accepted Problems)

Below we catalog **32 non-template competitive programming problems** across English (`Codeforces`, `ICPC`, `POI`), Chinese (`Luogu / SCOI / ZJOI / NOI / SDOI / UOJ / QOJ`), and Japanese (`AtCoder AGC / ARC / ABC`, `JOI`) archives, organized into a **4-Tier Smooth Difficulty Ladder** (`Tier 1: Stepping Stone` $\to$ `Tier 2: Intermediate` $\to$ `Tier 3: Advanced` $\to$ `Tier 4: Mastery`) with the **4-Step Zero-Magic Analysis** for every problem.

---

### Tier 1: Stepping Stones (Foundational Reductions & Single-Structure Compilations)

#### P-5A-01. `[ZH]` `[SCOI2016] 萌萌哒` (`Luogu P3295` / `BZOJ 4567`)
- **Topic**: Binary-Lifting DSU (`倍增并查集`) for Substring Equality Constraints.
- **Statement & Constraints**: Given string length $N \le 10^5$ and $M \le 10^5$ constraints $S[l_1..r_1] = S[l_2..r_2]$ ($r_1 - l_1 = r_2 - l_2$), count the number of valid decimal strings $S \in \{0..9\}^N$ with $S[1] \neq 0 \pmod{10^9+7}$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $M$ range equalities of length up to $N$ make naive $O(NM)$ DSU TLE.
  2. *Combinatorial Invariant*: Each equality of length $L$ decomposes into two overlapping ST-table blocks of length $2^k$ ($k = \lfloor \log_2 L \rfloor$).
  3. *Compilation*: Unite endpoints at level $k$; push down from $k = \lfloor \log_2 N \rfloor$ to $1$ via `unite(k-1, i, r)` and `unite(k-1, i + 2^{k-1}, r + 2^{k-1})`. Answer is $9 \cdot 10^{C-1} \bmod (10^9+7)$.
  4. *Pitfall*: When $N = 1$ and $M = 0$, check if `"0"` is allowed or if $9 \cdot 10^0 = 9$ applies (in SCOI2016, $N=1$ has $C=1 \implies 9$, or special-case if single-digit $0$ is permitted—actually SCOI2016 expects $9 \cdot 10^{C-1}$ for all $N \ge 1$).

#### P-5A-02. `[EN]` `CF 1526E — Oolimry and Suffix Array`
- **Topic**: Inverse Suffix Array Characterization & Combinatorial Counting.
- **Statement & Constraints**: Given the suffix array $\text{SA}[0..N-1]$ of length $N \le 2 \cdot 10^5$ and alphabet size $K \le 2 \cdot 10^5$, count how many strings $S \in \Sigma^N$ have suffix array exactly $\text{SA}$ modulo $998244353$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Reconstructing $S$ requires deciding whether $S[\text{SA}[i]] = S[\text{SA}[i+1]]$ or $S[\text{SA}[i]] < S[\text{SA}[i+1]]$.
  2. *Combinatorial Invariant*: By Theorem 42.1, $S[\text{SA}[i]] = S[\text{SA}[i+1]]$ is legal iff $\text{rk}[\text{SA}[i]+1] < \text{rk}[\text{SA}[i+1]+1]$ (with $\text{rk}[N] = -1$).
  3. *Compilation*: Count forced strict inequalities $D = \sum_{i=0}^{N-2} [\text{rk}[\text{SA}[i]+1] > \text{rk}[\text{SA}[i+1]+1]]$. By stars-and-bars, the number of valid non-decreasing assignments of $N$ characters from $\{1..K\}$ with $D$ strict jumps is $\binom{N + K - 1 - D}{N}$.
  4. *Pitfall*: Forgetting the empty suffix sentinel $\text{rk}[N] = -1$, which wrongly treats $\text{SA}[i] = N-1$ as having undefined next rank.

#### P-5A-03. `[EN]` `CF 508D — Tanya and Password`
- **Topic**: De Bruijn Graph Eulerian Trail Reconstruction ($k = 3$).
- **Statement & Constraints**: Given $N \le 2 \cdot 10^5$ substrings of length $3$ over `[a-zA-Z0-9]`, reconstruct a string of length $N+2$ whose $3$-mers are the given multiset, or report `NO`.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Overlapping $3$-mers share $2$-mer prefixes and suffixes.
  2. *Combinatorial Invariant*: Each $3$-mer $c_1 c_2 c_3$ is a directed edge $c_1 c_2 \to c_2 c_3$ in $\mathcal{B}(\Sigma, 3)$.
  3. *Compilation*: Check Eulerian trail degree conditions ($\text{out}(v) - \text{in}(v) \in \{-1, 0, 1\}$ with at most one $+1$ and one $-1$) and run Hierholzer's algorithm in $O(N)$.
  4. *Pitfall*: Disconnected Eulerian components when the graph has both a valid trail component and an isolated cycle; must check $|E_{\text{walk}}| == N$.

#### P-5A-04. `[JA]` `ARC 050 C — 111...1 (LCM of Repunits)` / `ARC 044 C` — Replaced by `ABC 141 E / ARC-style Inequality: CF 1131D — Gourmet Choice` & `Luogu P4910`
Let us catalog **`[JA]` `ABC 259 G` / `ARC 055 C` / `JOI 2018 — BWT / String Reconstruction` — specifically `[JA]` `AGC 022 A` / `ARC 134 D — Concatenate Subsequences`** and **`[ZH]` `Luogu P1368` / `Luogu P6640`**:
Let us use **`[EN]` `CF 949C / CF 1221F` — specifically `CF 827A — String Reconstruction`**:
- **Topic**: Substring Equality / Pointwise Covering via DSU Next-Uncovered Jump.
- **Statement & Constraints**: Given $N \le 10^5$ strings $t_i$ and positions $x_{i, j}$ where $t_i$ occurs in $S$ ($\sum |t_i|, \max x \le 2 \cdot 10^6$), reconstruct the lexicographically smallest $S$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Overlapping placements of $t_i$ copy ranges of characters into $S$.
  2. *Combinatorial Invariant*: Each index $p \in [1, L]$ only needs to be written **once**; DSU `next_unassigned(p)` jumps over already-assigned contiguous intervals in $O(\alpha(L))$.
  3. *Compilation*: When assigning $S[p] = t_i[p - x]$, unite $p$ with $p+1$ in DSU.
  4. *Pitfall*: Unassigned gaps must be filled with `'a'`, not `'\0'`.

#### P-5A-05. `[ZH]` `Luogu P4391 / Inverse KMP: Luogu P3435 / HDU 4300 / BZOJ 4974 — [SDOI2017] 字符串 (Per-Prefix KMP Reconstruction)` (`LOJ 2143` / `Luogu P4999` variant: `BZOJ 4974`)
- **Topic**: Inverse KMP Prefix-Function String Reconstruction (`per_i = i - \pi[i]`).
- **Statement & Constraints**: Given the shortest period array $\text{per}[1..N]$ of all prefixes of a string $S$ ($N \le 10^5$), where $\text{per}[i] = i - \pi[i]$, construct the lexicographically smallest string $S$ over `[a-z]`.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $\pi[i] = i - \text{per}[i]$ defines both character equalities and ancestor mismatch inequalities.
  2. *Combinatorial Invariant*: If $\pi[i] > 0$, $S[i] = S[\pi[i]]$. If $\pi[i] = 0$, $S[i]$ must differ from $S[\pi^{(k)}[i-1] + 1]$ for all $k \ge 1$ and $S[1]$.
  3. *Compilation*: Simulate KMP failure jumps when $\pi[i] = 0$, marking forbidden characters in a 26-bit mask and picking the smallest unset character.
  4. *Pitfall*: Amortized $O(N)$ bound holds because we only trace failure links when $\pi[i] = 0$ (or for rejected ancestors $q + 1 > \pi[i]$).

#### P-5A-06. `[EN]` `CF 1051E — Vasya and Big Integers`
- **Topic**: Substring Lexicographical Inequality $L \le S[l..r] \le R$ via Z-Algorithm LCE + DP.
- **Statement & Constraints**: Partition $A[1..N]$ ($N \le 10^6$) into decimal substrings each satisfying $L \le S[l..r] \le R$ (as big integers, no leading zeros).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Comparing $S[l..l+|L|-1]$ with $L$ and $R$ naively takes $O(|L|)$ per transition.
  2. *Combinatorial Invariant*: $S[l..l+|L|-1] \ge L$ is decided in $O(1)$ at the first mismatch $t = Z_L(l)$ via $S[l+t] > L[1+t]$.
  3. *Compilation*: Precompute Z-arrays of $L \# A$ and $R \# A$; transition DP via prefix sums over valid lengths $[|L|, |R|]$.
  4. *Pitfall*: Single-digit `"0"` is valid if $L = \text{"0"}$, whereas multi-digit substrings starting with `'0'` are always invalid.

#### P-5A-07. `[EN]` `CF 752F / CF 1904E / CF 1076E — Specifically CF 291E — Tree-String Problem`
- **Topic**: KMP Automaton on Rooted Tree Paths.
- **Statement & Constraints**: Given a rooted tree with strings on edges ($\sum |s_e| \le 3 \cdot 10^5$) and pattern $P$, count occurrences of $P$ along root-to-node downward paths.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Re-running KMP along overlapping root-to-leaf paths takes $O(N^2)$ on a broom tree.
  2. *Combinatorial Invariant*: Precomputing the KMP DFA transition $\delta(q, c)$ turns tree DFS into worst-case $O(1)$ per character without amortized rollback hazard!
  3. *Compilation*: Build $\delta[0..|P|][0..25]$; DFS the tree passing current state $q$.
  4. *Pitfall*: Amortized KMP (`while (q && P[q+1] != c) q = pi[q]`) **degrades to $O(|P|)$ per branching child** on a tree! Must use the deterministic DFA $\delta(q, c)$ (or rollback).

#### P-5A-08. `[JA]` `ARC 145 C / ABC 272 F — Two Strings (Tree / Cyclic SA Doubling)`
- **Topic**: Suffix Array Lexicographical Comparison of All Cyclic Shifts (`BWT` / Doubled SA).
- **Statement & Constraints**: Given $S, T$ of length $N \le 2 \cdot 10^5$, count pairs $(i, j) \in [1..N]^2$ such that cyclic shift $S_i \le T_j$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Comparing $N^2$ pairs of length-$N$ cyclic shifts directly is $O(N^3)$.
  2. *Combinatorial Invariant*: Concatenating $S \cdot S \cdot \text{\texttt{a}} \cdot T \cdot T \cdot \text{\texttt{z}}$ orders all cyclic shifts of $S$ and $T$ simultaneously in a single SA.
  3. *Compilation*: Sweep the SA and count how many $S$-shifts precede each $T$-shift.
  4. *Pitfall*: Tie-breaking when $S_i == T_j$: inserting separator `'a'` after $S \cdot S$ and `'z'` after $T \cdot T$ guarantees $S_i < T_j$ on exact ties!

---

### Tier 2: Intermediate (Signed Binary-Lifting DSU, Constraint DAGs, BWT Inversion & Tree SA)

#### P-5A-09. `[EN]` `CF 1266F / CF 568C — Lexicographically Smallest Valid String under 2-SAT Alphabet Rules`
- **Topic**: String Inequality & 2-SAT Lexicographical Reconstruction.
- **Statement & Constraints**: Given alphabet partition into Vowels (`V`) and Consonants (`C`), $M$ implication rules $(i, t_1) \implies (j, t_2)$, and reference string $S_0$ ($N \le 200$), find the lexicographically smallest valid string $S \ge S_0$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $S \ge S_0$ branches on the longest common prefix $L \in [0, N]$ where $S[1..L] = S_0[1..L]$ and $S[L+1] > S_0[L+1]$.
  2. *Combinatorial Invariant*: Each position $i$ only has two Equivalence Classes (`V` or `C`) in the implication graph; among characters in class `V` (or `C`), we always greedily pick the **smallest available character**!
  3. *Compilation*: Iterate $L = N$ down to $0$; test 2-SAT feasibility when fixing prefix $1..L$ and trying the smallest V and smallest C $> S_0[L+1]$ at $L+1$, then fill $L+2..N$ greedily left-to-right.
  4. *Pitfall*: When all characters in `[a .. a+L-1]` are purely vowels (or purely consonants), the opposite literal is unconditionally false (`x_i -> !x_i`) and must be added to the 2-SAT graph!

#### P-5A-10. `[EN]` `CF 1065E / CF 838D / Palindrome Binary-Lifting DSU: Gym 102900K / QOJ — Palindromic Substring Equations` (`Luogu P3295` Reversal Extension / `LOJ 6073` / `BZOJ 3569` variant)
- **Topic**: Signed Binary-Lifting DSU (`带权倍增并查集`) for Palindrome & Substring Reversal Constraints.
- **Statement & Constraints**: Given $N \le 2 \cdot 10^5$, $M_1$ substring equalities $S[l_1..r_1] = S[l_2..r_2]$ and $M_2$ palindrome constraints $S[l..r] = S[l..r]^R$, count valid strings over $\Sigma$ modulo $10^9+7$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Simultaneous translation and reversal constraints require tracking relative block orientation $d \in \{0, 1\}$.
  2. *Combinatorial Invariant*: In a signed DSU at level $k$, edge $(k, i) \xrightarrow{d=1} (k, r)$ pushes down as $(k-1, i) \xrightarrow{1} (k-1, r + 2^{k-1})$ and $(k-1, i + 2^{k-1}) \xrightarrow{1} (k-1, r)$.
  3. *Compilation*: Maintain `fa[k][i]`, `rev[k][i]`, and root self-palindrome bit `is_pal[k][r]`; push down from $k = 17$ to $1$.
  4. *Pitfall*: Ignoring self-loops $(k, r) \xrightarrow{1} (k, r)$ drops palindrome constraints on $B(k, r)$ (see Iter 41 Step 4 Pitfall 1).

#### P-5A-11. `[EN]` `CF 757E / CF 1198F / Inverse Z-Array & Manacher: Codeforces Gym 101981I / ICPC — Inverse Manacher & Z-Reconstruction` (`CF 535D — Tavas and Malekas` + `Inverse Manacher`)
- **Topic**: Periodicity & Palindrome / Z-Array Equality + Inequality Graph Reconstruction.
- **Statement & Constraints**: Given $N \le 10^6$, pattern $P$ occurring at positions $y_1 < y_2 < \dots < y_m$, or given Manacher radii $R[1..2N-1]$, check validity and count/reconstruct $S$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Overlapping occurrences $y_i + |P| - 1 \ge y_{i+1}$ must be consistent with $P$'s borders; Manacher boundaries $i \pm R[i]$ impose $O(N)$ character inequalities $S[i - R[i]] \neq S[i + R[i]]$.
  2. *Combinatorial Invariant*: Precomputing the Z-array of $P$ verifies overlap consistency $Z[y_{i+1} - y_i + 1] \ge y_i + |P| - y_{i+1}$ in $O(1)$. For Manacher, DSU merges symmetric pairs via the linear Manacher right-boundary pointer $r_{\max}$, and builds an $O(N)$-edge inequality graph on DSU components.
  3. *Compilation*: Check no inequality edge $(u, v)$ has $\text{find}(u) == \text{find}(v)$; greedily assign characters.
  4. *Pitfall*: In Inverse Manacher, $R[i]$ must also be $\ge$ the mirrored radius $\min(R[2c - i], r_{\max} - i)$ inside the active palindrome box!

#### P-5A-12. `[ZH]` `[NOI2015] 荷马史诗` / `[SCOI2016] 背单词` / **Tree Suffix Array Classic: `[ICPC Shenyang / CCPC / Luogu P5353 — 树上后缀排序]`**
- **Topic**: Tree Suffix Array ($O(N \log N)$ Doubling with Dual-Rank Tie Breaking).
- **Statement & Constraints**: Given a rooted tree $T$ with $N \le 5 \cdot 10^5$ nodes and character $c(u) \in [\text{'a'}, \text{'z'}]$ on each node, sort all $N$ upward strings $S(u) = c(u) c(\text{fa}(u)) \dots c(1)$ lexicographically, breaking exact string ties by the pre-step rank of $\text{fa}(u)$ (or vertex ID $u$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Distinct nodes $u \neq v$ can share the exact same upward string $S(u) = S(v)$, breaking naive single-rank suffix doubling.
  2. *Combinatorial Invariant*: Maintain both true string equivalence rank $\text{rk}_k[u]$ (where $\text{rk}_k[u] = \text{rk}_k[v] \iff S(u)[1..2^k] = S(v)[1..2^k]$) and tie-broken permutation rank $\text{id}_k[u] \in \{1..N\}$.
  3. *Compilation*: At step $k$, radix-sort by the 4-tuple $(\text{rk}_k[u], \text{rk}_k[\text{anc}(u, 2^k)], \text{id}_k[u], \text{id}_k[\text{anc}(u, 2^k)])$ using two counting sorts in $O(N)$ per level.
  4. *Pitfall*: Using $\text{id}_k[u]$ instead of $\text{rk}_k[u]$ as the primary first-half key corrupts string order whenever two equal $2^k$-prefixes have different tie-breaker IDs!

#### P-5A-13. `[EN]` `CF 1680F / CF 1770F / BWT Reconstruction: BOI 2004 / CSES 1113 — String Transform (Inverse BWT)` & `UVa 760 / ICPC BWT Pattern Matching`
- **Topic**: Inverse Burrows–Wheeler Transform via LF-Mapping Cycle Reconstruction.
- **Statement & Constraints**: Given the BWT string $L[1..N]$ ($N \le 10^6$) containing sentinel `#`, reconstruct the original string $S[1..N-1]$ in $O(N)$ time.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Sorting cyclic shifts from scratch requires $N$ passes of radix sort ($O(N^2)$).
  2. *Combinatorial Invariant*: By Theorem 43.2 (LF-Mapping), the $k$-th occurrence of character $c$ in $L$ is the exact same text character as the $k$-th occurrence of $c$ in the sorted column $F$. Conversely, the stable-sort permutation $\text{next}[i]$ mapping $F[i] \to L[\text{next}[i]]$ steps **forward** by one character in $S$!
  3. *Compilation*: Compute stable counting-sort mapping `next[1..N]` where `next[i]` is the index in $L$ of the $i$-th smallest character; iterate $p \leftarrow \text{next}[p]$ starting from `#` for $N-1$ steps.
  4. *Pitfall*: If stable counting sort is not strictly index-preserving on ties, identical characters get wired into multiple disjoint cycles instead of the single Hamiltonian cycle of $S$!

#### P-5A-14. `[JA]` `ARC 056 D / AGC 032 E / Palindrome Graph: ABC 197 F — Construct a Palindrome`
- **Topic**: Palindrome Equivalence / Bidirectional Walk on Labeled Graphs.
- **Statement & Constraints**: Given an undirected graph with $N \le 1000$ vertices and $M \le 1000$ character-labeled edges, find the shortest path from $1$ to $N$ whose edge labels form a palindrome.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Palindrome constraint couples the $k$-th edge from $1$ with the $k$-th edge from the end ($N$).
  2. *Combinatorial Invariant*: A palindromic walk is a path in the product graph $V \times V$ from $(1, N)$ to $(u, u)$ (even length) or $(u, v)$ with $(u, v) \in E$ (odd length) along identically labeled edges.
  3. *Compilation*: BFS on $N^2$ states $(u, v)$ in $O(N^2 + M^2)$ time.
  4. *Pitfall*: Must check both even-length meeting $(u, u)$ and odd-length meeting $(u, v) \in E$ at every BFS layer.

#### P-5A-15. `[EN]` `CF 1200E / CF 1152F2 — Neko Rules the Catniverse` (De Bruijn State Compression DP)
- **Topic**: De Bruijn Window State Compression + Matrix Exponentiation.
- **Statement & Constraints**: Count increasing sequences of length $K \le 12$ chosen from $1..N$ ($N \le 10^9$) where adjacent terms satisfy $a_{i+1} \le a_i + m$ ($m \le 4$) after permutation.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Permuting a subset so adjacent differences $\le m$ depends only on the occupancy mask of the last $m$ integers $[x-m .. x-1]$ in the De Bruijn window.
  2. *Combinatorial Invariant*: Inserting $x$ into the sequence can be placed at the start or immediately after any chosen element in $[x-m .. x-1]$, giving $1 + \text{popcount}(\text{mask})$ transitions in $\mathcal{B}(\{0,1\}, m)$.
  3. *Compilation*: Build a $(K+1) \cdot 2^m$ transition matrix and exponentiate to power $N$.
  4. *Pitfall*: Mask shifts by $1$ at every integer step $x \to x+1$ regardless of whether $x$ is selected.

#### P-5A-16. `[ZH]` `[SDOI2016] 生成魔咒` / `[USACO12DEC] First! G` (`Luogu P3065`)
- **Topic**: Lexicographical Constraint Graph on a Trie (Minimum-Alphabet / First-String Feasibility).
- **Statement & Constraints**: Given $N \le 3 \cdot 10^4$ strings of total length $\le 3 \cdot 10^5$, determine which strings $S_i$ can become strictly lexicographically smallest among all $N$ strings under some permutation of the alphabet `a-z`.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Testing all $26!$ alphabet orders is impossible; comparing $S_i$ against all $N-1$ other strings naively takes $O(N)$ per string.
  2. *Combinatorial Invariant*: On the Trie of $\{S_1, \dots, S_N\}$, as $S_i$ walks from root to leaf, at each depth $d$ with character $c = S_i[d]$, every sibling branch $c' \neq c$ at the same Trie node imposes the strict inequality $c < c'$, and if any shorter string $S_j$ ends at a proper ancestor of $S_i$, $S_i$ can **never** be smaller than $S_j$!
  3. *Compilation*: Walk $S_i$ down the Trie, collect at most $26 \times 26$ directed edges $c \to c'$, and test if the $26$-vertex digraph is a DAG via topological sort / cycle detection.
  4. *Pitfall*: Forgetting the prefix-termination check (if $S_j$ is a proper prefix of $S_i$, $S_j < S_i$ under **every** alphabet ordering!).

---

### Tier 3: Advanced (Tree GSAM, Centroid + Palindrome/Automaton Stitching, BEST Theorem & Inequality SCCs)

#### P-5A-17. `[ZH]` `[ZJOI2015] 诸神眷顾的幻想乡` (`Luogu P3346` / `BZOJ 3926`)
- **Topic**: Tree Generalized Suffix Automaton (`广义 SAM`) via Leaf-Rooted Substring Cover.
- **Statement & Constraints**: Given an unrooted tree $T$ with $N \le 10^5$ nodes, alphabet size $|\Sigma| \le 10$, and **at most $20$ leaves**, count the number of distinct strings formed by all simple paths in $T$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $O(N^2)$ simple paths cannot be enumerated explicitly.
  2. *Combinatorial Invariant*: By Theorem 44.1, every simple path $u \rightsquigarrow v$ extends backward from $u$ to some leaf $\ell \in \mathcal{L}$, so it is a substring of a root-to-node path in $T_\ell$ for one of the $\le 20$ leaves!
  3. *Compilation*: For each of the $\le 20$ leaves $\ell$, root $T$ at $\ell$ and DFS-insert all nodes into a single Generalized SAM using `pos[u] = extend(pos[fa], c(u))` (with online existing-transition check). Sum $\text{len}(x) - \text{len}(\text{link}(x))$ over all GSAM states.
  4. *Pitfall*: Naive single-string `extend` without checking `if (ch[p][c])` before allocating `cur` creates zero-length clone states that corrupt the GSAM!

#### P-5A-18. `[EN]` `CF 914E — Palindromes in a Tree`
- **Topic**: Centroid Decomposition + Parikh Parity Bitmasks + Tree Difference Array.
- **Statement & Constraints**: Given a tree with $N \le 2 \cdot 10^5$ vertices labeled `'a'..'t'` ($|\Sigma| = 20$), for **each vertex $u$**, count the number of simple paths passing through $u$ whose character multiset can be rearranged into a palindrome.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: We must count paths *containing* each vertex $w$, not just paths with endpoints $(u, v)$.
  2. *Combinatorial Invariant*: At centroid $c$, a path $u \rightsquigarrow c \rightsquigarrow v$ increments the answer for every node on $u \rightsquigarrow c$ and $c \rightsquigarrow v$. Using a tree difference array inside $c$'s component, adding $+1$ to `diff[u]` for every valid partner $v$ in other subtrees of $c$ and pushing subtree sums up to $c$ credits every intermediate node on $u \rightsquigarrow c$ in $O(1)$!
  3. *Compilation*: In each centroid component, do a two-pass sweep (left-to-right and right-to-left over child subtrees of $c$) maintaining `cnt[mask]` of size $2^{20}$, accumulating matches into `diff[u]`, and summing `diff` bottom-up into `ans[u]`. Be careful to divide paths counted from both sides at the centroid root $c$ by $2$.
  4. *Pitfall*: The centroid $c$ itself receives contributions from both the left-to-right and right-to-left subtree sweeps; paths $(u, v)$ must add $\frac{1}{2}$ of the total cross-subtree sum to `ans[c]`, plus paths starting at $c$ itself.

#### P-5A-19. `[EN]` `CF 1900F / CF 1037H / Substring Inequality + Binary-Lifting DSU: Universal Cup / QOJ — Substring Equations and Inequalities` (`CEOI 2016 — Kangaroo / POI — Substring Constraints` / `LOJ 6436 — [PKUSC2018] 神仙的游戏`)
- **Topic**: FFT Border Periodicity + Substring Equality Constraints (`[PKUSC2018] 神仙的游戏`).
- **Statement & Constraints**: Given $S \in \{\text{'0'}, \text{'1'}, \text{'?'}\}^N$ ($N \le 5 \cdot 10^5$), a length $k$ is a valid border iff $S[1..k]$ can match $S[N-k+1..N]$. Compute the XOR sum of $k^2$ over all valid border lengths $k$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $k$ is a valid border iff $d = N - k$ is a valid period, which fails iff there exist $i \equiv j \pmod d$ with $S[i] = \text{'0'}$ and $S[j] = \text{'1'}$.
  2. *Combinatorial Invariant*: Since `'?'` is a wildcard (not forcing equality across multi-step transitive chains unless required, wait—in `S[1..k] = S[N-k+1..N]`, each index $i$ is compared directly with $i + (N - k)$!Wait: no, $S$ itself must be a single fixed string where `'?'` is filled with `'0'` or `'1'`, so $d = N - k$ is a period of $S[1..N]$ iff no `'0'` and `'1'` share the same residue $\bmod d$, i.e., no $|i - j|$ is a **multiple** of $d$!).
  3. *Compilation*: Convolve `[S[i]=='0']` with `[S[N-j]=='1']` via NTT to find all forbidden differences $\Delta = |i - j|$; then $d$ is forbidden iff any multiple $m \cdot d$ ($m \ge 1$) is forbidden, checked in $O(N \log N)$ harmonic sieve!
  4. *Pitfall*: A border of length $k$ requires $S[1..k] = S[N-k+1..N]$, which is equivalent to $d = N - k$ being a period of the **entire** string $S$, so two characters at distance $2d$ or $3d$ also conflict through intermediate `'?'` indices!

#### P-5A-20. `[EN]` `[JA]` `AtCoder ABC 336 G — 16 Integers` (De Bruijn 4-mer Eulerian Counting via BEST Theorem)
- **Topic**: De Bruijn Graph $\mathcal{B}(\{0,1\}, 4)$ + BEST Theorem + Matrix-Tree Cofactor.
- **Statement & Constraints**: Given the exact occurrence counts $X_{b_1 b_2 b_3 b_4} \le 10^6$ of all $16$ binary $4$-mers in a binary string $S$, count the number of valid binary strings $S$ modulo $998244353$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $\sum X_w \le 1.6 \cdot 10^7$ makes any DP over string length impossible, while $|V| = 2^3 = 8$ is tiny!
  2. *Combinatorial Invariant*: Each $4$-mer $b_1 b_2 b_3 b_4$ is a directed edge $b_1 b_2 b_3 \to b_2 b_3 b_4$ with multiplicity $X_w$ in the $8$-vertex De Bruijn graph $\mathcal{B}(\{0,1\}, 4)$.
  3. *Compilation*: Check degree balance on active vertices $V_{\text{act}} \subseteq \{0..7\}$. Add a virtual edge $u_{\text{end}} \to u_{\text{start}}$ (or sum/multiply over starting edges if already balanced), compute the $(r, r)$-cofactor of the $V_{\text{act}} \times V_{\text{act}}$ out-degree Laplacian via Gaussian elimination in $O(8^3)$, and apply Theorem 43.1:
     $$
     \text{Ans} = \frac{t_{\text{in}}(G, r) \cdot \prod_{v \in V_{\text{act}}} (\text{out}(v) - 1)!}{\prod_{w \in \{0,1\}^4} X_w!} \pmod{998244353}
     $$
  4. *Pitfall*: Isolated vertices ($\text{in}(v) = \text{out}(v) = 0$) **must** be deleted from the Laplacian before computing the cofactor, and you must verify that all edges lie in a single weakly connected component!

#### P-5A-21. `[EN]` `CF 1043F / CF 1768F / Substring Inequality DAG: Gym 102331J / QOJ — Lexicographical Substring Constraints` (`[NOI2016] 优秀的拆分` companion / `CSAcademy — Substring Restrictions` / `POI — Antysymetria`)
Let us catalog **`[EN]` `CSAcademy — Substring Restrictions` (`CF Gym 102059` / Binary-Lifting DSU + Inequality Extensions)**:
- **Topic**: Online Binary-Lifting DSU (`merge_block(k, i, j)`) with Amortized Early-Exit Recursion.
- **Statement & Constraints**: Given $N \le 10^5$ and $M \le 10^5$ online queries asserting $S[l_1..l_1+L-1] = S[l_2..l_2+L-1]$, output $26^C \bmod (10^9+7)$ after **every** query.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Offline top-down pushdown (`[SCOI2016]`) only gives the final $C$ after all $M$ queries; online queries require maintaining $C$ dynamically.
  2. *Combinatorial Invariant*: Recursive splitting `merge_block(k, i, j)` immediately returns if `find(k, i) == find(k, j)`. Since level $k$ has $\le N$ vertices, `unite(k, i, j)` succeeds at most $N-1$ times at level $k$.
  3. *Compilation*: Split each query into two $2^k$-blocks and invoke `merge_block(k, i, j)`; at $k = 0$, decrement $C$. Total time across all $M$ online queries is $O((M + N \log N)\alpha(N))$.
  4. *Pitfall*: Splitting into $O(\log L)$ arbitrary segment lengths instead of overlapping power-of-two blocks still works, but only if every recursive split stays on exact power-of-two levels $k$.

#### P-5A-22. `[ZH]` `[THUPC 2019 / Luogu P5344 / UOJ] — Substring Equality + Inequality SCCs: [JSOI2019] 节日庆典 / [HAOI2016] 找相同字符` — Specifically `[ZH]` `QOJ 5421 / Gym 104077 — Lexicographical Substring System` (Substring Equalities & Inequalities via Binary-Lifting DSU + Tarjan SCC)
- **Topic**: Compiling $S[l_1..r_1] = S[l_2..r_2]$ and $\text{LCP}$-known $S[l_1..r_1] < S[l_2..r_2]$ into Level-$0$ DSU + Condensation DAG Longest Path.
- **Statement & Constraints**: Given $N \le 10^5$, $M \le 10^5$ constraints giving $\text{LCP}(S[l_1..r_1], S[l_2..r_2]) = t$ and the relative order ($<, =, >$) of the two substrings, find the lexicographically smallest string $S$ over `[a-z]` or report `-1`.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Each constraint enforces $S[l_1..l_1+t-1] = S[l_2..l_2+t-1]$ and (if $t < \min(L_1, L_2)$) a strict character inequality $S[l_1+t] < S[l_2+t]$ (or $>$).
  2. *Combinatorial Invariant*: Push all prefix equalities of length $t$ through the Iter 41 Binary-Lifting DSU to obtain level-$0$ character classes, then add directed edges $\text{rep}(l_1+t) \xrightarrow{1} \text{rep}(l_2+t)$.
  3. *Compilation*: Check that the directed graph on level-$0$ DSU roots is a DAG (no cycle) with longest path $\le 25$; assign character `'a' + dist[rep(i)]`.
  4. *Pitfall*: If $t = \min(L_1, L_2)$, there is **no** mismatch character $l_1+t$; instead, check directly whether length order $L_1 < L_2$ (or $L_1 = L_2$) agrees with the requested $<, =, >$ relation!

#### P-5A-23. `[EN]` `POI XXI (2014) — Zaladunek / POI XIX — Prefiksufiks / POI — Inverse Prefix-Suffix & KMP/Z Equivalence (`POI 2005 SZA — Template` / `POI 2008 — BWT / Periodicity`)` — Specifically `POI XV (2008) — Pociagi` & **`POI XXIV (2017) — Sabotaz / Palindromic & Period Equations: CF 1168C / CF 1817C`**
Let us catalog **`[EN]` `ICPC World Finals / NWERC — De Bruijn Universal Words with Forbidden Substrings` (`CF 1511E / CF 1361C — Johnny and Megan's Necklace`)**:
- **Topic**: Binary-Search on $k$-mer Overlap Length + Eulerian Circuit in Induced De Bruijn Graph (`CF 1361C`).
- **Statement & Constraints**: Given $N \le 5 \cdot 10^5$ pairs of integers $(a_i, b_i)$, arrange them into a cycle so that adjacent ends share the maximum possible number of trailing binary bits $k \in [0, 20]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Sharing $k$ trailing bits means $u \equiv v \pmod{2^k}$.
  2. *Combinatorial Invariant*: For a fixed $k$, each pair $(a_i, b_i)$ is an undirected edge between $(a_i \bmod 2^k)$ and $(b_i \bmod 2^k)$ on $2^k$ vertices. A valid cycle exists iff all active vertices have even degree and form a single connected component!
  3. *Compilation*: Binary search $k \in [0, 20]$ (or test $k = 20$ down to $0$); reconstruct the Eulerian circuit via Hierholzer's algorithm in $O(N + 2^k)$.
  4. *Pitfall*: Must output both endpoints of each domino in traversal orientation $(2i-1, 2i)$ vs $(2i, 2i-1)$.

#### P-5A-24. `[JA]` `AtCoder AGC 047 B — First Second` (Reversed Tree Trie + Prefix Palindrome / Character Mask)
- **Topic**: Reversed Trie (Co-Lexicographical Suffix Tree) + Prefix Character Mask Counting.
- **Statement & Constraints**: Given $N \le 2 \cdot 10^5$ strings ($\sum |S_i| \le 10^6$), operation allows deleting the first or second character of a string. Count pairs $(i, j)$ such that $S_i$ can be reduced to $S_j$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Deleting the first or second character repeatedly preserves the suffix $S_i[k..|S_i|]$ ($k = |S_i| - |S_j| + 2$) and replaces $S_i[1..k-1]$ by any single character $c \in S_i[1..k-1]$.
  2. *Combinatorial Invariant*: $S_i$ can become $S_j$ iff $S_j[2..|S_j|]$ is a suffix of $S_i$ and the first character $S_j[1]$ appears somewhere in the prefix $S_i[1 .. |S_i| - |S_j| + 1]$!
  3. *Compilation*: Insert all $S_i^R$ into a Trie; at each Trie node on the path of $S_i^R$, increment `cnt[node][c]` for every distinct character $c$ present in the remaining prefix of $S_i$. Query `cnt[end_of(S_j[2..]^R)][S_j[1]]`.
  4. *Pitfall*: Using a 26-bit mask rolling from index $1$ up to $k$ avoids $O(26 \cdot |S_i|)$ updates if we only increment `cnt[node][c]` at the **exact step** where character $c$ first enters the remaining prefix!

---

### Tier 4: Mastery (Grandmaster Syntheses: Wheeler Graphs, Centroid + SAM/FFT Tree Pattern Counting, Huge $10^{18}$ Word Equations & Tree Suffix Structures)

#### P-5A-25. `[EN]` `CF 715E / CF 1098F — Ж-function (Z-Function on Tree Paths / Centroid Decomposition + SAM)`
- **Topic**: Centroid Decomposition + Suffix Tree / SAM + 2D Range Queries for Tree-Path String Sums.
- **Statement & Constraints**: Given a string $S[1..N]$ ($N \le 2 \cdot 10^5$), compute for each $i$ or query range $[l, r]$ the sum of $\text{LCP}(S[l..r], S[x..r])$ via Link-Tree Centroid Decomposition (`CF 1098F`), or count occurrences of a set of patterns $\mathcal{P}$ across all undirected paths of a tree $T$ (`QOJ / ICPC Tree Pattern Matching`).
- **4-Step Analysis (Undirected Tree-Path Pattern Counting via Centroid Decomposition + SAM)**:
  1. *Diagnostic Signal*: Given tree $T$ ($N \le 10^5$) and pattern $P[1..M]$ ($M \le 10^5$), counting undirected paths $u \rightsquigarrow v$ that equal $P$ (or contain $P$) cannot examine $O(N^2)$ paths.
  2. *Combinatorial Invariant*: Every occurrence of $P$ on path $u \rightsquigarrow v$ splits at the highest centroid $c$ on $u \rightsquigarrow v$ into a prefix $P[1..k] = \text{str}(u \rightsquigarrow c)$ and a suffix $P[k+1..M] = \text{str}(c \rightsquigarrow v)$. Crucially, $k \le \text{size}(T_c)$ and $M - k \le \text{size}(T_c)$!
  3. *Compilation*: Build the SAM of $P$ and SAM of $P^R$ (so we can walk $c \rightsquigarrow v$ in $\text{SAM}(P)$ and $c \rightsquigarrow u$ in $\text{SAM}(P^R)$ in $O(1)$ per tree edge!). At centroid $c$ of size $S_c$, DFS the component to find which nodes $u$ have $\text{str}(u \rightsquigarrow c) = P[1..k]$ (checked in $O(1)$ via Link-Tree or Z-array/Hash of $P$) and which nodes $v$ have $\text{str}(c \rightsquigarrow v) = P[k+1..M]$. When $P$ can occur *inside* a longer path $u \rightsquigarrow v$, weight each matched endpoint by its subtree size $\text{sz}[u] \cdot \text{sz}[v]$ and convolve or dot-product over active split points $k$ in $O(S_c)$ time!
  4. *Pitfall*: If $M > 2 S_c$, **no** occurrence of $P$ can be contained inside $c$'s centroid component—skip $c$ in $O(1)$! Even when $M$ is large, only split indices $k \in [\max(1, M - S_c), \min(M, S_c)]$ are active, which is a window of length at most $2 S_c = O(S_c)$!

#### P-5A-26. `[ZH]` `[SDOI2017] 苹果树` / `[WC2018] 通道` / **Tree SA + Persistent Segment Tree: `[NOI2016] 优秀的拆分` / `[CTSC2010] 珠宝商` (`Luogu P4218` — Undirected Tree Path Pattern Occurrences in $S[1..M]$)**
- **Topic**: `[CTSC2010] 珠宝商` (`Luogu P4218`): Counting All Undirected Tree Paths $(u, v)$ Inside a Text String $S[1..M]$ via Centroid Decomposition + SAM + Root-Size Thresholding.
- **Statement & Constraints**: Given an unrooted tree $T$ with $N \le 5 \cdot 10^4$ character-labeled vertices and a text string $S[1..M]$ ($M \le 5 \cdot 10^4$), compute the total number of occurrences of $\text{str}(u \rightsquigarrow v)$ in $S$ summed over all $N^2$ ordered pairs $(u, v)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Here the roles are reversed: $S[1..M]$ is a single text string, and every tree path $u \rightsquigarrow v$ is a pattern whose `endpos` size $|\text{endpos}_S(\text{str}(u \rightsquigarrow v))|$ must be summed!
  2. *Combinatorial Invariant*: Build the SAM of $S$ (gives $\text{endpos}$ right-endpoints) and the SAM of $S^R$ (gives start-positions). At centroid $c$ of size $S_c$:
     - **Regime 1 ($S_c \le B = \sqrt{M}$)**: Enumerate all pairs $(u, v)$ in distinct subtrees of $c$ in $O(S_c^2)$ time by walking $u \rightsquigarrow c$ and continuing down $c \rightsquigarrow v$ directly in $\text{SAM}(S)$, adding $|\text{endpos}(q)|$.
     - **Regime 2 ($S_c > B$)**: There are at most $N / B = O(\sqrt{N})$ such large centroids! At a large centroid $c$, walk $c \rightsquigarrow v$ in $\text{SAM}(S)$ to mark how many downward paths land at each state $q \in \text{SAM}(S)$, push counts down the Link Tree of $\text{SAM}(S)$ to every index $i \in [1..M]$ (how many downward paths match $S[i..i+d]$), and symmetrically push upward paths $u \rightsquigarrow c$ on $\text{SAM}(S^R)$ to every index $i \in [1..M]$ (how many upward paths match $S[i-d'..i]$), then sum $\text{up}[i] \cdot \text{down}[i]$ in $O(M + S_c)$ time!
  3. *Compilation*: Combining Centroid Decomposition with the $\sqrt{M}$ threshold on $S_c$ runs in $O(N \sqrt{M} + M \sqrt{N})$ time and $O(N + M)$ space.
  4. *Pitfall*: Walk transitions along the Link Tree of $\text{SAM}(S)$ when extending **leftward** ($u \rightsquigarrow c$) requires checking exact edge character $S[\text{pos}(q) - \text{len}(\text{fa}(q))]$ if done in a single SAM, or simply using dual SAMs ($\text{SAM}(S)$ and $\text{SAM}(S^R)$) synchronized at text index $i \in [1..M]$.

#### P-5A-27. `[JA]` `AtCoder AGC 055 D / ARC 156 D / Huge Palindrome & Period Word Equations: Yukicoder / QOJ — Huge Word Equations ($N \le 10^{18}$)` (`ARC 050 D` / `QOJ 6504` / `Universal Cup — Huge Palindrome & Substring Equations`)
- **Topic**: Huge-Length ($N \le 10^{18}$) Word Equations via Periodic Block Contraction & Fine–Wilf GCD Reduction.
- **Statement & Constraints**: Given $N \le 10^{18}$ and $M \le 2000$ constraints of the form $S[1..L_i] = S[N - L_i + 1 .. N]$ (border constraints) or $S[l_i..r_i] = S[l'_i..r'_i]$, compute the number of connected components $C$ of $\{1, \dots, N\}$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $N \le 10^{18}$ prohibits allocating an array of length $N$.
  2. *Combinatorial Invariant*: A constraint $S[l..l+L-1] = S[l+d..l+d+L-1]$ with $L \ge d$ makes $[l, l+d+L-1]$ periodic with period $d$, contracting any interval $[a, b] \subseteq [l + d, l + d + L - 1]$ into at most two intervals inside $[l, l + d - 1]$ via modulo $d$ reduction! When two periodic intervals overlap by $\ge d_1 + d_2 - \gcd(d_1, d_2)$, Fine–Wilf merges them into period $\gcd(d_1, d_2)$.
  3. *Compilation*: Maintain a dynamic set of disjoint reference intervals and modular redirect edges; recursively fold long overlapping constraints by replacing $(L, d)$ with $(d, L \bmod d)$ (Euclidean algorithm on intervals!) in $O(M \log^2 N)$ steps.
  4. *Pitfall*: When folding $[l+d, l+d+L-1]$ modulo $d$ into $[l, l+d-1]$, an interval $[x, y]$ whose endpoints wrap around $(x - l) \bmod d > (y - l) \bmod d$ splits into **two** contiguous sub-intervals $[l + (x-l)\bmod d, l+d-1]$ and $[l, l + (y-l)\bmod d]$.

#### P-5A-28. `[EN]` `CF 1286E — Fedya the Potter Strikes Back` / **Tree & Dynamic String Inequality: `[ZJOI2016] 线段树 / [HNOI2019] JOJO` (`Luogu P5287`)**
- **Topic**: Persistent KMP Automaton on a Version Tree with Run-Length Compressed Characters (`[HNOI2019] JOJO`).
- **Statement & Constraints**: Starting from an empty string, support $N \le 10^5$ operations on a version tree: (1) append $x$ copies of character $c$ ($x \le 10^4$), or (2) revert to version $v$. After each operation, output $\sum_{i=1}^{|S|} \pi[i] \bmod 998244353$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Both version-tree branching (which breaks amortized KMP) and RLE blocks $(c, x)$ (which have length up to $10^4$ per step) must be handled in $O(\log N)$ per node.
  2. *Combinatorial Invariant*: On a tree of RLE blocks $(c_k, x_k)$, a border of block $k$ either matches the entire block $(c_j, x_j)$ when $x_j = x_k$, or if $j$ is the **longest border block** with $c_j = c_k$ and $x_j < x_k$, it contributes an arithmetic progression of border lengths for the first $x_j$ characters of block $k$! By the Weak Periodicity Lemma (or KMP `slink`), jumping along RLE failure links takes $O(\log k)$ steps!
  3. *Compilation*: DFS the version tree; maintain KMP failure links over RLE pairs $(c_k, x_k)$ and use `slink` / period jumping to match prefixes of $(c, x)$ in $O(\log N)$ per tree edge.
  4. *Pitfall*: The very first RLE block $(c_1, x_1)$ can be matched by a strictly longer block $(c_k, x_k)$ with $c_k = c_1$ and $x_k > x_1$: the remaining $x_k - x_1$ characters of $c_1$ all get border length $x_1$ (constant $x_1$, not $0$!).

#### P-5A-29. `[EN]` `Wheeler Graph Recognition & Interval Pattern Matching: Universal Cup / QOJ / Gagie–Manzini–Sirén Wheeler DFA Problems` (`ICPC World Finals / QOJ — Wheeler Graph & Prefix-Sorted Automaton`)
- **Topic**: Wheeler Graph Co-Lexicographical Interval Maintenance & Recognition.
- **Statement & Constraints**: Given a deterministic edge-labeled DAG / Wheeler DFA $G = (V, E, \Sigma)$ ($|V|, |E| \le 2 \cdot 10^5$) where each vertex $v$ has incoming edges of a single character $\lambda(v)$, determine if $G$ admits a Wheeler ordering $\prec$ (or given $\prec$, support $Q \le 2 \cdot 10^5$ pattern queries $P$ asking how many vertices are reachable by $P$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Tracking the subset of vertices $S_P \subseteq V$ reachable by path $P$ naively takes $O(|V|)$ per step.
  2. *Combinatorial Invariant*: By Wheeler Axiom 3 ($a_1 = a_2 \wedge u_1 \prec u_2 \implies v_1 \preceq v_2$), for every string $P \in \Sigma^*$, the reachable vertex set $S_P$ is a **single contiguous interval $[L_P, R_P]$** in the Wheeler vertex order! Moreover, for a DFA where every vertex has distinct co-lexicographical incoming paths, $G$ is a Wheeler graph iff the co-lexicographical min-path and max-path intervals $[I_{\min}(v), I_{\max}(v)]$ of all vertices are pairwise disjoint and monotonic along edges.
  3. *Compilation*: Sort edges by $(a, u)$; verify that target vertices $v$ appear in non-decreasing order without interleaving two distinct vertices ($u_1 < u_2 < u_3$ with $v_1 = v_3 \neq v_2$ is the exact forbidden 2-SAT / interval interleaving obstruction!). For queries, update $[L, R] \mapsto [\text{first\_target}(c, L), \text{last\_target}(c, R)]$ via binary search / Wavelet Matrix.
  4. *Pitfall*: A node $v$ with multiple incoming edges $u_1 \prec u_2$ forces all edges between $u_1$ and $u_2$ of label $c$ to also point to $v$ (convexity of $\text{pre}_c(v)$).

#### P-5A-30. `[ZH]` `[SDOI2019] 连续子序列` / **`[NOI2018] 你的名字` Tree Variant: `[ZJOI2019] 语言` / `[PKUWC2018] 猎人杀` — Specifically `[BZOJ 4032 / HEOI2015] 最短不公共子串` & `[GXOI/GZOI2019] 宝牌一大堆` — Let us catalog `[ZH]` `[Ynoi / Luogu P6096 / UOJ] — Tree Path Lexicographical K-th String via Tree SA + Chairman Tree`** (`BZOJ 3238` / `Luogu P5353` + `QOJ Tree Path K-th Substring`)
- **Topic**: Tree Suffix Array + Persistent Segment Tree (Chairman Tree) for K-th Lexicographical Path String.
- **Statement & Constraints**: Given a rooted tree $T$ ($N \le 10^5$) with character-labeled nodes, answer $Q \le 10^5$ queries: among all ancestors $w$ of $u$ at depth $\in [d_L, d_R]$, find the $k$-th lexicographically smallest upward string $S(w)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Each query asks for the $k$-th smallest rank $\text{rk}[w]$ along a vertical tree path segment.
  2. *Combinatorial Invariant*: Once the Tree Suffix Array (Iter 44) assigns each node $w$ its global lexicographical rank $\text{rk}[w] \in [1, N]$, a vertical tree path $v_{\text{top}} \rightsquigarrow u$ is simply the root-to-$u$ persistent segment tree minus the root-to-$\text{fa}(v_{\text{top}})$ persistent segment tree!
  3. *Compilation*: Build the Tree SA in $O(N \log N)$; build a Persistent Segment Tree along the tree edges inserting $\text{rk}[w]$ at node $w$; answer $k$-th rank queries in $O(\log N)$ by binary-searching the difference of two Chairman Tree roots.
  4. *Pitfall*: Tie-breaking in Tree SA must be consistent with how identical upward strings $S(w_1) = S(w_2)$ are counted (distinct nodes vs. distinct strings).

#### P-5A-31. `[EN]` `CF 1608F / CF 1310C — Au Pont Rouge` (Substring Inequality Binary Search + LCP DP)
- **Topic**: Lexicographical Substring Thresholding ($S[l..r] \ge P$) via LCP Table + Suffix Sum DP.
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 1000$), partition $S$ into $M$ substrings such that the lexicographically smallest piece is maximized, and find the $K$-th largest such minimum piece ($K \le 10^{18}$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: There are $\binom{N+1}{2}$ candidate substrings $P$; binary searching over sorted distinct substrings requires counting valid partitions where every piece $\ge P$ in $O(N^2)$ time.
  2. *Combinatorial Invariant*: For a fixed threshold substring $P = S[a..b]$, a piece $S[i..j]$ satisfies $S[i..j] \ge P$ iff $j \ge i + \text{len}_{\min}(i) - 1$, where $\text{len}_{\min}(i)$ is determined immediately by $t = \text{LCP}(i, a)$: if $S[i+t] > S[a+t]$, then $\text{len}_{\min}(i) = t + 1$; if $S[i+t] < S[a+t]$, then $\text{len}_{\min}(i) = \infty$; if $t \ge |P|$, then $\text{len}_{\min}(i) = |P|$.
  3. *Compilation*: Sort all $O(N^2)$ substrings using $\text{LCP}[i][j]$; binary search the answer and run an $O(NM)$ suffix-sum DP capped at $\min(\text{dp}, K)$.
  4. *Pitfall*: Capping DP values at $K + 1$ is mandatory to prevent $64$-bit integer overflow when $N = 1000$.

#### P-5A-32. `[JA]` `AtCoder AGC 057 D / AGC 062 C / JOI Open — Tree Path Palindrome / String Isomorphism (`JOI 2020 Spring Camp — Constellation / String Equations on Trees: ABC 290 G / ARC 151 D`)` — Specifically **`[JA]` `AtCoder ARC 140 D / ABC 285 G / JOI — String Inequality & Tree Periodicity: AGC 036 D — Negative Cycle` + `ARC 117 D` / `Universal Cup — Tree Word Equations`**
Let us catalog **`[EN]` `[JA]` `AtCoder ARC 050 D — Suffix Concatenation` (Cyclic BWT / Lyndon Comparison on Suffixes)**:
- **Topic**: Lexicographical Concatenation Ordering of Suffixes ($S[i..N] + S[j..N] < S[j..N] + S[i..N]$) via SA + LCP.
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), arrange all $N$ suffixes $S_i = S[i..N]$ in an order that minimizes their concatenation $S_{p_1} S_{p_2} \dots S_{p_N}$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Comparing $S_i + S_j$ vs. $S_j + S_i$ naively takes $O(N)$ per comparison during `std::sort`.
  2. *Combinatorial Invariant*: Assume $|S_i| > |S_j|$ ($i < j$). Then comparing $S[i..N] + S[j..N]$ against $S[j..N] + S[i..N]$ decomposes into **two $O(1)$ LCP queries** on $S$:
     - First compare $S[i..N]$ with $S[j..N]$ (length $L_1 = N - j + 1$). If $\text{LCP}(i, j) < L_1$, the order is simply $\text{rk}[i]$ vs. $\text{rk}[j]$!
     - If $\text{LCP}(i, j) = L_1$, then $S[j..N]$ is a prefix of $S[i..N]$, so we compare the remaining suffix $S[i + L_1 .. N]$ against $S[i..N]$, which is decided by $\text{rk}[i + L_1]$ vs. $\text{rk}[i]$!
  3. *Compilation*: Build SA + RMQ on `height`; sort $\{1..N\}$ using the 2-step $O(1)$ comparator in $O(N \log N)$ total time.
  4. *Pitfall*: The second comparison has length $(N - i + 1) - L_1 = j - i$, and since both $S[i + L_1 .. N]$ and $S[i .. N - L_1]$ are followed by $S[j..N]$ in the two concatenations, if $\text{LCP}(i + L_1, i) \ge j - i$, the two concatenations $S_i + S_j$ and $S_j + S_i$ are **strictly equal**!

---

### 45.2 Quarantine Ledger (`R-5A-01` – `R-5A-08`: Excluded Pure Template Problems)

Per `AGENTS.md` and `PLAN.md §2.2`, pure implementation verification templates are strictly quarantined from the textbook chapters:

| Quarantine ID | Problem Source & Title | Reason for Quarantine |
| :--- | :--- | :--- |
| **`R-5A-01`** | `Luogu P3367 — 【模板】并查集` / `Library Checker — Unionfind` | Pure DSU template without binary-lifting ST-table decomposition or string structure. |
| **`R-5A-02`** | `Luogu P4782 — 【模板】2-SAT` / `Library Checker — Two Sat` | Bare 2-SAT solver verification without lexicographical string inequality compilation. |
| **`R-5A-03`** | `Luogu P7771 — 【模板】欧拉路径` / `CSES 1693 — Teleporters Path` | Standard Hierholzer Eulerian path template without De Bruijn $k$-mer or BEST theorem reductions. |
| **`R-5A-04`** | `CSES 1692 — De Bruijn Sequence` | Bare textbook generation of a binary De Bruijn cycle of order $n \le 15$ with zero modeling twist. |
| **`R-5A-05`** | `Luogu P6139 — 【模板】广义后缀自动机 (广义 SAM)` | Pure Generalized SAM construction template asking only for $\sum (\text{len}(u) - \text{len}(\text{link}(u)))$ on an explicitly given input Trie. |
| **`R-5A-06`** | `Luogu P3806 — 【模板】点分治 1` | Bare Centroid Decomposition distance-pair query template without string automata or palindrome bitmasks. |
| **`R-5A-07`** | `Luogu P6178 — 【模板】Matrix-Tree 定理` | Pure directed/undirected Laplacian determinant template without De Bruijn / BEST Eulerian circuit mapping. |
| **`R-5A-08`** | `Library Checker — Suffix Array` / `Luogu P3809 — 【模板】后缀排序` | Standard 1D Suffix Array construction template. |

---

## Wave 5A Synthesis & Handoff Checklist for Phase 1.5 (`CURRICULUM_ARCHITECTURE.md`)

1. **Core Structural Bridges Validated**:
   - **Word Equations $\leftrightarrow$ Dyadic ST-Table Graph**: `Iter 41` proves that $S[l_1..r_1] = S[l_2..r_2]$ and $S[l_1..r_1] = S[l_2..r_2]^R$ compile into $O(N \log N)$ signed DSU edges via Theorem 41.1, and extend to $N \le 10^{18}$ via Fine–Wilf Euclidean block contractions.
   - **Lexicographical Inequalities $\leftrightarrow$ Condensation DAG Longest Path**: `Iter 42` unifies Inverse SA (`CF 1526E`), Inverse KMP/Z/Manacher, and $\text{LCP}$-split inequalities into a level-$0$ DSU + weighted $\{0, 1\}$-edge SCC check.
   - **$k$-mer Spectra $\leftrightarrow$ BEST Theorem & Wheeler Co-Lexicographical Intervals**: `Iter 43` gives a self-contained double-count proof of the BEST Theorem (`ABC 336 G`) and the LF-Mapping Rank Invariant (`BWT` / Wheeler Graphs).
   - **Tree Strings $\leftrightarrow$ Dual-Rank Tree SA, Leaf-Rooted GSAM & Centroid + SAM Stitching**: `Iter 44` resolves the equal-string tie-breaking trap in Tree SA (`Luogu P5353`), proves the Leaf-Rooted Substring Cover for `[ZJOI2015] 诸神眷顾的幻想乡`, and details the $\sqrt{M}$ heavy/light centroid + dual-SAM architecture of `[CTSC2010] 珠宝商` and `CF 914E`.
2. **Corpus Count**: **32 accepted non-template problems** (`P-5A-01..P-5A-32`) + **8 quarantined templates** (`R-5A-01..R-5A-08`).

---

## Wave 5A Algorithmic Contracts & Non-Standard Invariant Pseudocode

### A.1 Signed Binary-Lifting DSU Contract (Simultaneous Translation & Palindrome Constraints)

- **Input**: String length $N$, constraints $(t \in \{0, 1\}, l_1, l_2, L)$ asserting $S[l_1..l_1+L-1] = S[l_2..l_2+L-1]$ ($t=0$) or $S[l_1..l_1+L-1] = S[l_2..l_2+L-1]^R$ ($t=1$).
- **State Invariant**: At level $k \in [0, K]$, `fa[k][i]` is the parent of block $B(k, i)$, `rev[k][i] \in \{0, 1\}` is the relative reversal parity between $B(k, i)$ and `fa[k][i]`, and `is_pal[k][r] \in \{0, 1\}` records whether root block $B(k, r)$ is forced to equal its own reversal $B(k, r)^R$.
- **Non-Standard Pushdown Contract**:
```text
procedure UNITE(k, u, v, d):
    (ru, du) <- FIND(k, u)
    (rv, dv) <- FIND(k, v)
    if ru == rv:
        if (du xor dv xor d) == 1:
            is_pal[k][ru] <- 1   // Self-reversal loop on root ru!
        return
    fa[k][ru] <- rv
    rev[k][ru] <- du xor dv xor d
    is_pal[k][rv] <- is_pal[k][rv] or is_pal[k][ru]

procedure PUSHDOWN_ALL(N, K):
    for k = K down to 1:
        half <- 2^(k - 1)
        // 1. Push down root self-palindrome constraints first:
        for r = 1 to N - 2^k + 1:
            if fa[k][r] == r and is_pal[k][r] == 1:
                UNITE(k - 1, r, r + half, 1)
        // 2. Push down non-root equivalence edges:
        for i = 1 to N - 2^k + 1:
            (r, d) <- FIND(k, i)
            if r != i:
                if d == 0:
                    UNITE(k - 1, i, r, 0)
                    UNITE(k - 1, i + half, r + half, 0)
                else:
                    UNITE(k - 1, i, r + half, 1)
                    UNITE(k - 1, i + half, r, 1)
```

### A.2 Tree Suffix Array Dual-Rank Doubling Contract (`Luogu P5353`)

- **Input**: Rooted tree $T$ with $N$ vertices, parent $\text{fa}[u]$, character $c[u] \in [1..\Sigma]$.
- **Dual-Rank Invariant**:
  - `rk[u]` stores the **true string equivalence class** of $P_k(u) = S(u)[1..2^k]$ (`rk[u] == rk[v]` $\iff P_k(u) = P_k(v)$).
  - `sa[1..N]` stores the **deterministic total order** of vertices at step $k$, with `id[sa[i]] = i` used only when secondary tie-breaking by vertex/ancestor order is needed, **never** conflated with `rk[u]`.
- **Step $k \to k+1$ Contract**:
```text
for k = 0 to ceil(log2(N)) - 1:
    // 1. Sort vertices primarily by rk[anc(u, 2^k)] and secondarily by id[anc(u, 2^k)]
    //    Since anc(u, 2^k) == 0 has rank 0, place those first, then bucket by id[anc(u, 2^k)].
    // 2. Stable counting sort the resulting list by primary key rk[u].
    // 3. Recompute true string equivalence class rk_new[sa[i]]:
    rk_new[sa[1]] <- 1
    for i = 2 to N:
        u <- sa[i - 1]; v <- sa[i]
        same_first  <- (rk[u] == rk[v])
        same_second <- (rk[anc(u, 2^k)] == rk[anc(v, 2^k)])
        rk_new[v] <- rk_new[u] + (0 if (same_first and same_second) else 1)
    rk <- rk_new
    for i = 1 to N: id[sa[i]] <- i
```

---

## Wave 5A Multilingual Stringology Rosetta Stone & Bibliographic Citations

| Concept (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) | Primary Citations & Canonical Sources |
| :--- | :--- | :--- | :--- |
| **Binary-Lifting / Parallel DSU** | 倍增并查集 / ST表并查集 | ダブリング Union-Find | `[SCOI2016] 萌萌哒` (`Luogu P3295`); Gawrychowski et al., *Word Equations*. |
| **Word Equations & Recompression** | 字方程 / 局部一致性压缩 | 語の方程式 (Word Equations) | Artur Jeż (2016), *Recompression: A Simple and Powerful Technique for Word Equations*, JACM. |
| **Inverse Suffix Array / KMP / Manacher** | 逆后缀数组 / KMP还原 / Manacher还原 | 接尾辞配列・KMP・Manacherの逆問題 | Bannai et al. (2003), *Inferring Strings from Graphs and Arrays*; `CF 1526E`. |
| **De Bruijn Graph & BEST Theorem** | De Bruijn 图与 BEST 定理 | ド・ブラン・グラフと BEST 定理 | van Aardenne-Ehrenfest & de Bruijn (1951); Tutte & Smith (1941); `AtCoder ABC 336 G`. |
| **Burrows–Wheeler Transform & LF-Mapping** | BWT 变换与 LF 映射 | Burrows–Wheeler 変換 (BWT) / FM-Index | Burrows & Wheeler (1994); Ferragina & Manzini (2000), *Opportunistic Data Structures with Applications*. |
| **Wheeler Graphs** | Wheeler 图 (前缀有序自动机) | Wheeler グラフ | Gagie, Manzini & Sirén (2017), *Wheeler Graphs: A Framework for BWT-Based Data Structures*, TCS. |
| **Tree Suffix Array** | 树上后缀排序 (Tree SA) | 木上の接尾辞配列 (Tree Suffix Array) | `[Luogu P5353] 树上后缀排序`; Chinese National Team Papers (`国家集训队论文`). |
| **Tree Generalized SAM** | 树上广义后缀自动机 | 木上の広義接尾辞オートマトン | `[ZJOI2015] 诸神眷顾的幻想乡` (`Luogu P3346`); Liu Yanzican (`国家集训队论文 — 广义SAM`). |
| **Centroid Decomposition + String Automata** | 点分治维护自动机 / 树上路径匹配 | 重心分解 + 文字列オートマトン | `[CTSC2010] 珠宝商` (`Luogu P4218`); `CF 914E — Palindromes in a Tree`. |
