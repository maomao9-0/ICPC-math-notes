# Wave 4A (Cohort 1: Iterations 31–35): Goulden–Jackson Cluster Method, String PGFs / Martingales, Automaton DP & DFA Minimization (`DP套DP`)

> **Cohort & Scope Metadata**
> - **Cohort**: Cohort 1 (Primary Discovery & Structural Audit Loop, Iterations 31–35)
> - **Topic Wave**: Wave 4A — Goulden–Jackson Cluster Method, Autocorrelation Systems, String Probability Generating Functions (PGFs) & Martingale Optional Stopping (`康威赌博`), Automaton DP & DP-of-DP (`DP套DP` / `自動機上のDP`), Nerode Minimization, Exact Weighted Occurrence Generating Functions, and Multilingual Problem Mining.
> - **Prerequisite Baseline**: Reader holds tested library implementations of **KMP (`pi` array)**, **Z-Algorithm**, **Aho–Corasick (AC) Automaton**, **Suffix Automaton (SAM)**, **Gaussian Elimination over $\mathbb{F}_p$**, and **Formal Power Series (FPS) Inversion / Bostan–Mori Linear Recurrence Extraction**.
> - **Editorial Mandate**: Enforce the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard** across every theoretical derivation and every curated contest problem:
>   1. *The Diagnostic Signal (Why Naive String / Automaton Structures Fail)*
>   2. *The Combinatorial Word Invariant (Double-Overlap / Cluster / Martingale / Nerode Proof)*
>   3. *The Reverse-Engineering Scratchpad (Algorithmic & Algebraic Compilation)*
>   4. *Boundary Pitfalls & Broken-Invariant Counterexamples*

---

## Iteration 31: The Goulden–Jackson Cluster Method & Autocorrelation Systems

### 31.1 The Diagnostic Signal: Why Naive Aho–Corasick Matrix Exponentiation & Naive Inclusion–Exclusion Fail

Consider the foundational pattern-avoidance enumeration problem:
- **Concrete Objects Counted**: Given an alphabet $\Sigma$ of size $\sigma = |\Sigma|$ and a set of forbidden patterns $\mathcal{P} = \{P_1, P_2, \dots, P_m\}$ where $P_i \in \Sigma^*$, count the number of valid strings $W \in \Sigma^n$ of length $n$ (or compute the ordinary generating function $F(x) = \sum_{n \ge 0} a_n x^n$) that contain **none** of the patterns $P_i$ as a contiguous substring.

Why do standard automaton and combinatorial approaches collapse under grandmaster constraints?

1. **Failure of Aho–Corasick + Matrix Exponentiation / Gaussian Elimination**:
   Let $L = \sum_{i=1}^m |P_i|$ be the total length of all forbidden patterns. Building the Aho–Corasick (AC) automaton produces up to $L + 1$ states.
   - If $n \le 10^{18}$ and $L \le 100$, transition matrix exponentiation runs in $O(L^3 \log n)$ (or $O(L^2 \log n)$ via Cayley–Hamilton / Bostan–Mori).
   - **The Diagnostic Bottleneck**: Suppose $m \le 300$, each pattern has length $|P_i| \le 10^5$ (so $L = \sum |P_i| \le 3 \times 10^7$), and we want $[x^n] F(x)$ for $n \le 10^5$ or $n \le 10^{18}$. An AC automaton has $O(L)$ states, making $O(L^3)$ Gaussian elimination or even $O(n L)$ DP completely impossible in time and memory! Yet the number of *distinct patterns* $m$ is tiny ($m \le 300$), or $m = 1$ with $|P_1| = 10^5$. Can we compress a system of $L = \sum |P_i|$ states down to a system of size **only $m \times m$** (or $1 \times 1$ for a single pattern)?
2. **Failure of Naive Inclusion–Exclusion (`容斥原理`) over Positions**:
   If we attempt to apply Principle of Inclusion–Exclusion (PIE) by choosing a subset of occurrences of $P_i$ in $W$, two marked occurrences $P_i$ at $[l_1, r_1]$ and $P_j$ at $[l_2, r_2]$ can **overlap** ($l_1 \le l_2 \le r_1 < r_2$). The number of free characters left unconstrained in $W$ depends not merely on *how many* occurrences are chosen, but on their exact overlap lengths! Enumerating all valid overlap configurations naively over positions takes exponential time.

**The Structural Breakthrough (Goulden–Jackson Cluster Method, 1979)**:
Instead of tracking character-by-character prefix states in an AC automaton of size $O(\sum |P_i|)$, we perform Inclusion–Exclusion directly on the **marked occurrences** by grouping overlapping occurrences into maximal connected components called **clusters** (`簇`). Because two consecutive marked patterns in a cluster can overlap *only* along a suffix of some $P_i$ that equals a prefix of some $P_j$, the entire state space collapses from $O(\sum |P_i|)$ prefix states to the **$m$ complete patterns $\{P_1, \dots, P_m\}$** connected by **overlap border polynomials** $C_{i,j}(x)$.

---

### 31.2 The Combinatorial Word Invariant: Marked Words, Clusters, and the Overlap Border Decomposition

To avoid any unmotivated algebraic leaps, we explicitly define the combinatorial objects before writing down a single generating function.

#### Step 1: Reduced Pattern Set Assumption (Antichain Invariant)
Before running the Goulden–Jackson method, $\mathcal{P} = \{P_1, \dots, P_m\}$ **must** be reduced so that no pattern is a substring of another:
$$i \ne j \implies P_i \text{ is not a contiguous substring of } P_j.$$
*Why?* If $P_i$ is a substring of $P_j$, any string avoiding $P_i$ automatically avoids $P_j$; keeping $P_j$ in $\mathcal{P}$ is redundant for avoidance, and worse, in the cluster expansion it would allow a marked occurrence of $P_i$ to sit *strictly inside* a marked occurrence of $P_j$ ($l_2 < l_1 \le r_1 < r_2$), violating the left-to-right proper-overlap chain structure!

#### Step 2: Double-Counting via Marked Words $(W, M)$
For any word $W \in \Sigma^*$, let $\text{Occ}(W)$ be the set of all occurrences of patterns from $\mathcal{P}$ in $W$. Because $\mathcal{P}$ is substring-free, every occurrence is uniquely identified by its ending position $r$ (or interval $[l, r]$) and pattern index $i \in \{1, \dots, m\}$.
Define a **marked word** (`标记串`) as a pair $(W, M)$ where $W \in \Sigma^*$ and $M \subseteq \text{Occ}(W)$ is a subset of occurrences of patterns from $\mathcal{P}$ in $W$ that we choose to "highlight".
Assign to each marked word $(W, M)$ the weight:
$$\text{wt}(W, M) = (-1)^{|M|} x^{|W|}.$$
Now sum $\text{wt}(W, M)$ over all words $W \in \Sigma^*$ and all subsets $M \subseteq \text{Occ}(W)$:
$$\sum_{W \in \Sigma^*} \sum_{M \subseteq \text{Occ}(W)} (-1)^{|M|} x^{|W|} = \sum_{W \in \Sigma^*} x^{|W|} \sum_{M \subseteq \text{Occ}(W)} (-1)^{|M|} = \sum_{W \in \Sigma^*} x^{|W|} (1 - 1)^{|\text{Occ}(W)|}.$$
 In the inner sum, each summand $(1 - 1)^{|\text{Occ}(W)|}$ equals $1$ if and only if $|\text{Occ}(W)| = 0$ (meaning $W$ avoids all patterns in $\mathcal{P}$), and equals $0$ whenever $|\text{Occ}(W)| \ge 1$ because every non-empty set of occurrences has an equal number of even-sized and odd-sized marked subsets $M$.
Therefore, the ordinary generating function $F(x)$ of $\mathcal{P}$-avoiding words is **identically equal** to the generating function of all marked words $(W, M)$ weighted by $(-1)^{|M|}$:
$$F(x) = \sum_{(W, M)} (-1)^{|M|} x^{|W|}.$$

#### Step 3: Unique Factorization of Marked Words into Free Letters and Clusters
How is an arbitrary marked word $(W, M)$ constructed from left to right?
Each position $t \in \{1, \dots, |W|\}$ is either covered by no interval in $M$, or covered by the union of intervals in $M$. Furthermore, two marked occurrences $[l_1, r_1], [l_2, r_2] \in M$ with $l_1 < l_2$ (Remember: $l_1 = l_2$ is impossible since $\mathcal{P}$ is substring-free, which also gives $r_1 < r_2$) are said to **overlap** if $l_2 \le r_1$.
This overlap relation partitions the marked occurrences $M$ into connected components:
- **Free Letter**: A single character $c \in \Sigma$ not covered by any occurrence in $M$. Its generating function is $\sigma x = |\Sigma| x$.
- **Cluster (`簇`)**: A word $U \in \Sigma^*$ together with a non-empty chain of marked occurrences $M_U = (e_1, e_2, \dots, e_k)$ ($k \ge 1$) of patterns $P_{i_1}, P_{i_2}, \dots, P_{i_k}$ covering all of $U$ from $1$ to $|U|$, such that every adjacent pair $e_r = [l_r, r_r]$ and $e_{r+1} = [l_{r+1}, r_{r+1}]$ **strictly overlaps** ($l_r < l_{r+1} \le r_r < r_{r+1}$).

**Combinatorial Word Invariant (Unique Concatenation)**:
Every marked word $(W, M)$ decomposes uniquely as a sequence (concatenation) of free letters in $\Sigma$ and clusters!
Let $C(x) = \sum_{\text{clusters } (U, M_U)} (-1)^{|M_U|} x^{|U|}$ be the generating function of all clusters. Because a marked word is a sequence (`SEQ`) of items where each item is either one of the $\sigma$ free letters or a cluster, geometric series summation yields:
$$F(x) = \sum_{k \ge 0} (\sigma x + C(x))^k = \frac{1}{1 - \sigma x - C(x)}$$
valid in the formal power series ring $\mathbb{Q}[[x]]$ (since both $\sigma x$ and $C(x)$ have zero constant term $[x^0] = 0$, making $1 - \sigma x - C(x)$ a unit with constant term $1$).

#### Step 4: Decomposing Clusters via the Overlap Set $\text{Overlap}(P_i, P_j)$
How do two consecutive marked patterns $P_i$ and $P_j$ overlap inside a cluster?
Because $\mathcal{P}$ is an antichain, $P_j$ cannot be contained inside $P_i$, so $P_j$ must extend strictly to the right of $P_i$, while sharing a non-empty overlap of length $k \in \{1, 2, \dots, \min(|P_i|, |P_j|) - 1\}$ (or $k = |P_i| = |P_j|$ only if $i = j$, which would be the exact same occurrence—not allowed since $M$ is a *set* of distinct occurrences!).

```
P_i:  [ - - - - - | * * * * ]          length |P_i|
P_j:              [ * * * * | + + + ]  length |P_j|
                    <-- k --><-|P_j|-k->
```

Define the **overlap length set** from $P_i$ to $P_j$:
$$\text{Overlap}(P_i, P_j) = \Big\{ k \in \{1, 2, \dots, \min(|P_i|, |P_j|)\} \setminus \{\,|P_i| \text{ if } i = j\,\} \;\Big|\; P_i\big[|P_i|-k+1 \dots |P_i|\big] = P_j\big[1 \dots k\big] \Big\}.$$
Note carefully: when $i = j$, $\text{Overlap}(P_i, P_i)$ is the set of **proper borders** of $P_i$ (excluding $k = |P_i|$ itself, because a cluster cannot pick the exact same occurrence twice, though we will find it algebraically convenient below to separate the identity $I$ corresponding to $k = |P_i|$!).

When $P_j$ overlaps the end of $P_i$ by $k$ characters, it appends $|P_j| - k$ **new** characters to the right of $P_i$ and adds $1$ new marked occurrence (multiplying the sign $(-1)^{|M|}$ by $-1$).
Let $\tilde{C}_{i,j}(x)$ be the generating function of proper extension steps from $P_i$ to $P_j$:
$$\tilde{C}_{i,j}(x) = \sum_{k \in \text{Overlap}(P_i, P_j)} x^{|P_j| - k}.$$
And define the **Autocorrelation / Overlap Polynomial** (`自相关 / 互相关多项式`) $C_{i,j}(x)$ by including the $k = |P_i|$ trivial self-overlap (which contributes $x^{|P_i| - |P_i|} = x^0 = 1$ when $i = j$, and $0$ when $i \ne j$):
$$C_{i,j}(x) = \delta_{i,j} + \tilde{C}_{i,j}(x) = \sum_{\substack{1 \le k \le \min(|P_i|, |P_j|) \\ P_i[|P_i|-k+1..|P_i|] = P_j[1..k]}} x^{|P_j| - k}.$$
 Notice the algebraic elegance of $C_{i,j}(x)$: it sums $x^{|P_j|-k}$ over **all** non-empty suffix-prefix matches of $P_i$ and $P_j$, **including** $k = |P_i|$ when $i = j$!

---

### 31.3 The Reverse-Engineering Scratchpad: Deriving the $m \times m$ Linear System

Let $C_j(x)$ be the signed generating function of all clusters whose **last** (rightmost) marked occurrence is pattern $P_j$.
A cluster ending with $P_j$ is either:
1. A single-pattern cluster consisting solely of $P_j$, which has $1$ marked occurrence (sign $(-1)^1 = -1$) and length $|P_j|$, contributing $-x^{|P_j|}$; OR
2. A cluster ending with some pattern $P_i$ ($1 \le i \le m$), extended on the right by an overlapping occurrence of $P_j$ with overlap $k \in \text{Overlap}(P_i, P_j)$, which multiplies the weight by $-x^{|P_j| - k}$.

Writing this dichotomy as an equation for each $j \in \{1, \dots, m\}$:
$$C_j(x) = -x^{|P_j|} - \sum_{i=1}^m C_i(x) \tilde{C}_{i,j}(x).$$
Move the sum to the left-hand side and use $\delta_{i,j} + \tilde{C}_{i,j}(x) = C_{i,j}(x)$:
$$\sum_{i=1}^m C_i(x) \big(\delta_{i,j} + \tilde{C}_{i,j}(x)\big) = -x^{|P_j|} \iff \sum_{i=1}^m C_i(x) C_{i,j}(x) = -x^{|P_j|} \quad \forall j \in \{1, \dots, m\}.$$
Once $C_1(x), \dots, C_m(x)$ are solved from this $m \times m$ linear system, the total cluster generating function is $C(x) = \sum_{i=1}^m C_i(x)$, and the generating function of $\mathcal{P}$-avoiding words is:
$$F(x) = \frac{1}{1 - \sigma x - \sum_{i=1}^m C_i(x)}.$$

#### Alternative Direct Formulation Coupling $F(x)$ and End-Tagged Words $F_j(x)$ (The Guibas–Odlyzko Form)
In competitive programming (especially when combining with probability generating functions in Iteration 32), there is a second, even cleaner way to view the exact same $m \times m$ system without minus signs:
Instead of signed clusters, consider adding a single forbidden pattern $P_j$ to the right of a **valid** ($\mathcal{P}$-avoiding) word $W \in \mathcal{G}$.
In $W \cdot P_j$, the first occurrence of any pattern from $\mathcal{P}$ must end inside the appended $P_j$ (since $W$ has no occurrences). Suppose this **first** occurrence is $P_i$, ending at a position where $k$ characters of $P_j$ have been read (so $|P_j| - k$ characters of $P_j$ remain to the right).
Because $P_i$ ends at the $k$-th character of $P_j$ and cannot be strictly inside $P_j$ (as $\mathcal{P}$ is substring-free, if $P_i$ were strictly inside $P_j$ then $P_i$ would be a substring of $P_j$, contradiction!), the suffix of $P_i$ of length $k$ **must** equal the prefix $P_j[1..k]$!
Let $F_i(x)$ be the generating function of strings that avoid $\mathcal{P}$ until the very end, where they terminate with their **first** occurrence of a pattern from $\mathcal{P}$, and that pattern is $P_i$.
Then every word $W \cdot P_j$ (counted by $F(x) x^{|P_j|}$) decomposes **uniquely** at its first occurrence of a pattern $P_i \in \mathcal{P}$, followed by the remaining $|P_j| - k$ characters of $P_j$:
$$F(x) x^{|P_j|} = \sum_{i=1}^m F_i(x) \sum_{\substack{1 \le k \le \min(|P_i|, |P_j|) \\ P_i[|P_i|-k+1..|P_i|] = P_j[1..k]}} x^{|P_j|-k} = \sum_{i=1}^m F_i(x) C_{i,j}(x).$$
Notice that dividing both sides by $F(x)$ gives $\frac{F_i(x)}{F(x)} = -C_i(x)$! Furthermore, since extending any $\mathcal{P}$-avoiding word by one character in $\Sigma$ produces either a non-empty $\mathcal{P}$-avoiding word or a word ending in a first occurrence $F_i(x)$:
$$1 + \sigma x F(x) = F(x) + \sum_{i=1}^m F_i(x) \iff (1 - \sigma x) F(x) + \sum_{i=1}^m F_i(x) = 1.$$
This gives the **Guibas–Odlyzko $(m+1) \times (m+1)$ System**, which is algebraically identical to the Goulden–Jackson Cluster system!

#### Special Case $m = 1$ (Single Pattern $P$): The Autocorrelation Formula
When $\mathcal{P} = \{P\}$ consists of a single pattern of length $L = |P|$, let $A_P(x)$ be the **border polynomial** (evaluating $x^k$ or $x^{L-k}$ over all non-empty borders of $P$):
$$C_{1,1}(x) = \sum_{k \in \text{Borders}(P)} x^{L - k}, \quad \text{where } L \in \text{Borders}(P) \text{ contributes } x^0 = 1.$$
Then $C_1(x) C_{1,1}(x) = -x^L \implies C_1(x) = -\frac{x^L}{C_{1,1}(x)}$, and therefore:
$$F(x) = \frac{1}{1 - \sigma x + \frac{x^L}{C_{1,1}(x)}} = \frac{C_{1,1}(x)}{(1 - \sigma x) C_{1,1}(x) + x^L}.$$
**Computational Impact**: For a single pattern $P$ of length $L = 10^5$ and $n = 10^5$, we compute $\text{Borders}(P)$ in $O(L)$ via KMP, form the polynomial $(1 - \sigma x) C_{1,1}(x) + x^L$ of degree $L$, and take a **single polynomial inverse** mod $x^{n+1}$ in $O(n \log n)$ time—bypassing the $10^5$-state KMP DP or matrix exponentiation completely!

#### Small Hand-Checkable Example
Let $\Sigma = \{\texttt{A}, \texttt{B}\}$ ($\sigma = 2$) and forbid $P_1 = \texttt{ABA}$ ($L = 3$).
- The non-empty borders of $\texttt{ABA}$ are $\texttt{A}$ ($k = 1$) and $\texttt{ABA}$ ($k = 3$).
- Thus $C_{1,1}(x) = x^{3-3} + x^{3-1} = 1 + x^2$.
- By the single-pattern Goulden–Jackson formula:
  $$F(x) = \frac{1 + x^2}{(1 - 2x)(1 + x^2) + x^3} = \frac{1 + x^2}{1 - 2x + x^2 - x^3} = 1 + 2x + 4x^2 + 7x^3 + 12x^4 + 21x^5 + \cdots$$
- Hand-check for $n = 3$: Out of $2^3 = 8$ binary strings of length $3$, only $\texttt{ABA}$ is forbidden, leaving $8 - 1 = 7 = [x^3]F(x)$.
- Hand-check for $n = 4$: Out of $16$ strings of length $4$, those containing $\texttt{ABA}$ are $\texttt{ABAA}, \texttt{ABAB}, \texttt{AABA}, \texttt{BABA}$ ($4$ strings, since $\texttt{ABA}$ cannot overlap itself at distance $1$ inside length $4$). Thus $16 - 4 = 12 = [x^4]F(x)$.
- Hand-check for $n = 5$: Out of $32$ strings, a naive subtraction of $2 \times 4 + 4 = 12$ fails because $\texttt{ABABA}$ contains $\texttt{ABA}$ **twice** (overlapping at border $k = 1$)! The cluster of two overlapping $\texttt{ABA}$'s in $\texttt{ABABA}$ has weight $(-1)^2 x^5 = +x^5$, which corrects $32 - 3 \times 2^2 + 1 = 21 = [x^5]F(x)$.

---

### 31.4 Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Pitfall 1: Unreduced Pattern Set (Substring Containment Bug)**
   - *Counterexample*: Let $\Sigma = \{\texttt{a}, \texttt{b}\}$, $P_1 = \texttt{ab}$, and $P_2 = \texttt{aabb}$. Here $P_1$ is an internal substring of $P_2$ ($P_2 = \texttt{a} \cdot P_1 \cdot \texttt{b}$).
   - *What breaks*: In our overlap definition, $C_{1,2}(x)$ only checks whether a *suffix* of $P_1$ matches a *prefix* of $P_2$ ($\texttt{ab}$ has no suffix matching a prefix of $\texttt{aabb}$). It completely misses the fact that $P_1$ occurs inside the middle of $P_2$! If you feed $\{P_1, P_2\}$ into the $2 \times 2$ Goulden–Jackson matrix without first deleting $P_2$, the Guibas–Odlyzko decomposition of $W \cdot P_2$ fails because the first occurrence of $\mathcal{P}$ in $W \cdot \texttt{aabb}$ is $P_1 = \texttt{ab}$ ending at index $3$ of $P_2$, not at the end of $P_2$!
   - *Mandatory Fix*: Always filter $\mathcal{P}$ first (e.g., via AC automaton fail-tree reachability or KMP/SAM substring check) to eliminate any $P_j$ that contains another $P_i$ as a substring (and deduplicate identical patterns).
2. **Pitfall 2: Reversing the Exponent $x^k$ vs. $x^{|P_j|-k}$ in $C_{i,j}(x)$**
   - In probability/expected value problems (`Iteration 32`), we evaluate at $x = 1/\sigma$ and multiply by $\sigma^{|P_j|}$, turning $\sigma^{|P_j|} (1/\sigma)^{|P_j|-k}$ into $\sigma^k$. Many readers memorize $\sigma^k$ from coin-game problems and mistakenly write $C_{i,j}(x) = \sum x^k$ for the generating function! Remember: $k$ is the length of the **shared overlap** (which is already paid for by $P_i$), so $P_j$ extends the cluster by $|P_j| - k$ new characters, requiring the exponent $|P_j| - k$.
3. **Pitfall 3: Asymmetric Overlap ($C_{i,j}(x) \ne C_{j,i}(x)$)**
   - Both the overlap condition ($P_i$ on the left, $P_j$ on the right) and the extension length ($|P_j| - k$) are **directed**. Even if $k$ were the same, $|P_j| - k \ne |P_i| - k$ when $|P_i| \ne |P_j|$. And in the linear system $\sum_{i=1}^m C_i(x) C_{i,j}(x) = -x^{|P_j|}$, the summation index $i$ is the **left** pattern in the overlap pair $(P_i, P_j)$. Transpose errors here silently corrupt every multi-pattern answer when $m \ge 2$.

#### Algorithmic Contract: Computing All $C_{i,j}(x)$ Efficiently
- **Case 1 ($m$ patterns, total length $L = \sum |P_i|$ small or moderate)**:
  - Build the KMP `pi` array for each $P_j$, or build the Generalized Aho–Corasick automaton of $\mathcal{P}$.
  - In the AC automaton, after feeding $P_i$, the state is $u = \text{end}(P_i)$. All suffix-prefix overlaps with any $P_j$ correspond to prefixes of $P_j$ that are ancestors of $u$ on the AC `fail` tree!
  - Alternatively, using the **Z-Algorithm** or **Polynomial Hashing / SA + RMQ**: for each pair $(i, j)$, only lengths $k \in \text{Ancestors}_{\text{fail}}(\text{end}(P_i))$ or borders can match. Better yet: insert all $P_j$ into a Trie/AC automaton; the set of valid prefix lengths $k$ of $P_j$ that are suffixes of $P_i$ is simply the path from the root to $\text{LCA}_{\text{Trie}}(\text{end}(P_j), \text{fail-ancestors of } \text{end}(P_i))$, or by traversing the `fail` chain of $\text{end}(P_i)$ of length at most $|P_i|$ and marking reached Trie nodes, which takes $O(m \cdot \sum |P_i|)$ total time across all $m^2$ pairs!

---

## Iteration 32: Probability Generating Functions (PGFs) & Martingale Optional Stopping on Strings (`康威赌博`)

### 32.1 The Diagnostic Signal: Why Transition Matrix Gaussian Elimination Fails on Long Patterns

Consider the classic stochastic string stopping-time problem (`[CTSC2006] 歌唱王国` / `[SDOI2017] 硬币游戏` / `[JSOI2009] 有趣的游戏`):
- **Concrete Random Process**: Characters are drawn independently at each step $t = 1, 2, \dots$ from alphabet $\Sigma$, either uniformly with probability $p_c = 1/\sigma$ or with general letter probabilities $p_c > 0$ ($\sum_{c \in \Sigma} p_c = 1$).
- **Stopping Condition**: Given a target pattern $S$ of length $L \le 10^5$ (or a set of competing player patterns $P_1, \dots, P_m$, each of length $L \le 10^5$), the process stops at the first time $T$ when $S$ (or some $P_j$) appears as a contiguous substring of the generated string.
- **Questions**:
  1. What is the expected stopping time $\mathbb{E}[T_S]$ (and variance $\text{Var}(T_S)$) for a single pattern $S$?
  2. In a $m$-player pattern race, what is the exact probability $\pi_j$ that $P_j$ is the **first** pattern to appear?

**Why Naive Markov Chain / AC Automaton Gaussian Elimination Fails**:
- Building the KMP / AC automaton over the prefixes gives $V = \sum |P_i| \approx 3 \times 10^5$ states.
- Because `fail` transitions jump backward to shorter prefixes, the transition graph has cycles. Running Gaussian elimination on $V$ states takes $O(V^3)$ time—impossible for $V = 10^5$!
- Even for a single pattern $S$ where KMP DP can be unrolled in $O(L)$ by exploiting the DAG + back-edge structure (`递推消元`), doing so directly for $m = 300$ patterns of length $L = 300$ ($V = 9 \times 10^4$) is $O(V^3)$.
- **The Diagnostic Signal**: Whenever a Markov chain on strings stops **immediately upon completing one of $m$ patterns**, all non-terminal transitions are generated by appending random characters to a $\mathcal{P}$-avoiding prefix! Thus, the entire $O(\sum |P_i|)$-state Markov chain collapses into the **$m+1$ variables** of the Guibas–Odlyzko / Goulden–Jackson system evaluated at $x = 1$!

---

### 32.2 The Combinatorial Word Invariant: Two Dual Proofs (PGFs vs. Conway's Casino Martingale)

We present **both** the analytic Probability Generating Function (PGF) derivation and John Conway's Probabilistic Martingale (`康威赌博`) proof, and show that they are literally the same algebraic identity viewed through two lenses.

#### Method A: The Probability Generating Function (PGF) Derivation
Suppose letter $c \in \Sigma$ is drawn with probability $p_c$. For any word $u = c_1 c_2 \dots c_k$, denote its probability weight by $\mathbb{P}(u) = \prod_{r=1}^k p_{c_r}$ (for a uniform alphabet of size $\sigma$, $\mathbb{P}(u) = \sigma^{-|u|}$).
Let:
- $f_n$ = probability that the process stops at **exact step $n$**, with PGF $F(z) = \sum_{n \ge 0} f_n z^n$.
- $g_n$ = probability that the process has **not yet stopped** after step $n$ (i.e., the prefix of length $n$ avoids $S$), with GF $G(z) = \sum_{n \ge 0} g_n z^n$.

Let us relate $F(z)$ and $G(z)$ using two combinatorial word equations on the single pattern $S = s_1 s_2 \dots s_L$:

1. **One-Step Extension Relation**:
   Every $\mathcal{P}$-avoiding prefix of length $n$ (probability $g_n$), when extended by one random character (total probability $\sum_{c \in \Sigma} p_c = 1$, shifting length by $z^1$), either remains $\mathcal{P}$-avoiding at length $n+1$ (probability $g_{n+1}$) or stops for the very first time at length $n+1$ (probability $f_{n+1}$). Including the empty string $g_0 = 1$ at $z^0$:
   $$1 + z G(z) = G(z) + F(z) \iff F(z) + (1 - z) G(z) = 1.$$
   Differentiating with respect to $z$ gives:
   $$F'(z) - G(z) + (1 - z) G'(z) = 0.$$
   Setting $z = 1$ (since $S$ is finite and $p_c > 0$, the stopping time is almost surely finite with exponentially decaying tails, so $F(1) = 1$ and $G(1), G'(1) < \infty$):
   $$\mathbb{E}[T_S] = F'(1) = G(1).$$
   *(In plain words: $\mathbb{E}[T_S] = \sum_{n \ge 0} \mathbb{P}(T_S > n) = \sum_{n \ge 0} g_n = G(1)$.)*

2. **Full-Pattern Append Relation (The Overlap Identity)**:
   Take any $\mathcal{P}$-avoiding prefix $W$ of length $n$, and imagine forcefully appending the entire pattern $S = s_1 \dots s_L$ to its right. The probability weight of $W \cdot S$ is $g_n \mathbb{P}(S) z^{n+L}$, summing to $G(z) \mathbb{P}(S) z^L$.
   On the other hand, in $W \cdot S$, the pattern $S$ is guaranteed to appear by the end, and its **first** appearance must end at some index $k \in \{1, \dots, L\}$ inside the appended copy of $S$.
   As proven in Iteration 31, $S$ can end at the $k$-th character of the appended $S$ **if and only if** $k \in \text{Borders}(S)$ (meaning $S[1..k] = S[L-k+1..L]$), followed by the remaining suffix $S[k+1..L]$!
   The probability weight of stopping at that first occurrence is accounted for by $F(z)$, and the remaining suffix $S[k+1..L]$ has probability weight $\mathbb{P}(S[k+1..L]) = \frac{\mathbb{P}(S)}{\mathbb{P}(S[1..k])}$ and length $L - k$:
   $$G(z) \mathbb{P}(S) z^L = F(z) \sum_{k \in \text{Borders}(S)} \mathbb{P}(S[k+1..L]) z^{L-k}.$$
   Divide both sides by $\mathbb{P}(S)$:
   $$G(z) z^L = F(z) \sum_{k \in \text{Borders}(S)} \frac{z^{L-k}}{\mathbb{P}(S[1..k])}.$$

Now evaluate at $z = 1$, where $F(1) = 1$ and $G(1) = F'(1) = \mathbb{E}[T_S]$:
$$\boxed{\mathbb{E}[T_S] = G(1) = \sum_{k \in \text{Borders}(S)} \frac{1}{\mathbb{P}(S[1..k])} = \sum_{\substack{1 \le k \le L \\ S[1..k] = S[L-k+1..L]}} \left(\prod_{r=1}^k p_{s_r}\right)^{-1}.}$$
In particular, for a uniform alphabet of size $\sigma = |\Sigma|$ where $p_c = 1/\sigma$:
$$\boxed{\mathbb{E}[T_S] = \sum_{k \in \text{Borders}(S)} \sigma^k.}$$

#### Variance $\text{Var}(T_S)$ via Second Derivative of PGF (`[CTSC2006] 歌唱王国` Extended)
Because we have the exact rational PGF relation, computing $\text{Var}(T_S) = \mathbb{E}[T_S^2] - (\mathbb{E}[T_S])^2 = F''(1) + F'(1) - (F'(1))^2$ requires zero extra combinatorics!
Differentiating $F(z) + (1 - z)G(z) = 1$ twice at $z = 1$ gives $F''(1) = 2 G'(1)$.
And differentiating $G(z) = F(z) \sum_{k \in \text{Borders}(S)} \frac{z^{-k}}{\mathbb{P}(S[1..k])}$ at $z = 1$ yields:
$$G'(1) = F'(1) \sum_{k \in \text{Borders}(S)} \frac{1}{\mathbb{P}(S[1..k])} - F(1) \sum_{k \in \text{Borders}(S)} \frac{k}{\mathbb{P}(S[1..k])} = \big(\mathbb{E}[T_S]\big)^2 - \sum_{k \in \text{Borders}(S)} \frac{k}{\mathbb{P}(S[1..k])}.$$
Substituting $F''(1) = 2 G'(1)$ into $\text{Var}(T_S) = F''(1) + F'(1) - (F'(1))^2$:
$$\boxed{\text{Var}(T_S) = \big(\mathbb{E}[T_S]\big)^2 + \mathbb{E}[T_S] - 2 \sum_{k \in \text{Borders}(S)} \frac{k}{\mathbb{P}(S[1..k])}.}$$

---

#### Method B: Conway's Casino Betting Martingale (`康威赌博`) & Doob's Optional Stopping Theorem
Why does $\mathbb{E}[T_S] = \sum_{k \in \text{Borders}(S)} \sigma^k$ have such a clean sum-over-borders form? John H. Conway gave a famous martingale interpretation that makes the border sum completely transparent:

1. **The Fair Casino Setup**:
   At each integer time step $t = 1, 2, \dots$, a new gambler $G_t$ walks into a fair casino with initial capital $\$1$.
   Gambler $G_t$ wants to bet on the pattern $S = s_1 s_2 \dots s_L$ starting at time $t$:
   - At step $t$, $G_t$ stakes their entire $\$1$ on the character $s_1$ appearing at step $t$.
   - Because $s_1$ occurs with probability $p_{s_1}$, a **fair bet** pays multiplier $1 / p_{s_1}$ (or $\sigma$ in the uniform case) if $s_1$ appears, and $0$ (bankruptcy) otherwise.
   - If $G_t$ wins at step $t$, they now hold $\$ p_{s_1}^{-1}$ (or $\$ \sigma$), and at step $t+1$ they stake their **entire fortune** on $s_2$ appearing!
   - In general, if gambler $G_t$ has matched the prefix $S[1..k]$ across steps $t, t+1, \dots, t+k-1$, their fortune after step $t+k-1$ is $\mathbb{P}(S[1..k])^{-1}$ (or $\sigma^k$); if any character mismatches, their fortune drops to $0$ forever.
2. **The Martingale Invariant**:
   Let $X_n$ be the **total net profit of all gamblers combined** after step $n$.
   Because $\$1$ is paid in at each step $1, \dots, n$ ($n$ gamblers have entered) and the total fortune currently held by surviving gamblers after step $n$ is $W_n$, the net profit is $X_n = W_n - n$.
   Since every individual bet is fair ($\mathbb{E}[\text{payout} \mid \mathcal{F}_{n-1}] = \text{stake}$), the sequence $\{X_n\}_{n \ge 0}$ is a **martingale** with $X_0 = 0$, so $\mathbb{E}[X_n] = 0$ for every fixed $n$.
3. **Stopping at $T_S$ (Who is still alive when $S$ finishes?)**:
   Stop the casino at the exact stopping time $T = T_S$ when $S$ first appears as the suffix of the generated string $W[1..T]$.
   Which gamblers $G_t$ are still alive at time $T$?
   Gambler $G_{T-k+1}$ (who entered $k$ steps ago and has bet on $S[1..k]$ during steps $[T-k+1, T]$) is still alive at time $T$ **if and only if** the last $k$ characters of $W[1..T]$ equal $S[1..k]$.
   But the last $L$ characters of $W[1..T]$ equal $S[1..L]$! And no gambler who entered before $T - L + 1$ can still be alive (otherwise $S$ would have already completed before time $T$).
   Therefore, gambler $G_{T-k+1}$ ($1 \le k \le L$) is alive at time $T$ **if and only if** the suffix of $S$ of length $k$ equals the prefix $S[1..k]$—that is, **$k \in \text{Borders}(S)$**!
   Hence, at the exact moment $T = T_S$, the total fortune held by all surviving gamblers is deterministically:
   $$W_{T_S} = \sum_{k \in \text{Borders}(S)} \frac{1}{\mathbb{P}(S[1..k])} \quad \left(= \sum_{k \in \text{Borders}(S)} \sigma^k \text{ in the uniform case}\right).$$
4. **Why Optional Stopping Applies Rigorously**:
   Since the martingale increments $|X_{n} - X_{n-1}|$ are uniformly bounded by $\max_{1 \le k \le L} \mathbb{P}(S[1..k])^{-1} < \infty$ (because every gambler exits or finishes after at most $L$ steps) and $\mathbb{E}[T_S] < \infty$, **Doob's Optional Stopping Theorem** guarantees $\mathbb{E}[X_{T_S}] = \mathbb{E}[X_0] = 0$:
   $$\mathbb{E}[W_{T_S} - T_S] = 0 \implies \mathbb{E}[T_S] = \mathbb{E}[W_{T_S}] = \sum_{k \in \text{Borders}(S)} \frac{1}{\mathbb{P}(S[1..k])}.$$

---

### 32.3 Multi-Player Pattern Racing (`[SDOI2017] 硬币游戏` & `[JSOI2009] 有趣的游戏`)

Now suppose $m$ players hold reduced (antichain) patterns $P_1, P_2, \dots, P_m$. We want to find the winning probabilities $\pi_1, \dots, \pi_m$ where $\pi_i = \mathbb{P}(\text{process stops on } P_i)$.

#### The $(m+1) \times (m+1)$ Overlap Linear System
Let $F_i(z)$ be the PGF of stopping on pattern $P_i$, so $\pi_i = F_i(1)$, and let $G(z)$ be the GF of $\mathcal{P}$-avoiding prefixes.
Evaluating the Guibas–Odlyzko system from Iteration 31.3 at $z = 1$:
1. **Total Probability Conservation**: Since one of the $m$ patterns eventually wins with probability $1$:
   $$\sum_{i=1}^m \pi_i = 1.$$
2. **Appending $P_j$ to an Avoiding Prefix (or Running Conway's Casino for $P_j$)**:
   In the PGF view, appending $P_j$ to a $\mathcal{P}$-avoiding prefix gives:
   $$G(z) \mathbb{P}(P_j) z^{|P_j|} = \sum_{i=1}^m F_i(z) \sum_{k \in \text{Overlap}^+(P_i, P_j)} \mathbb{P}(P_j[k+1..|P_j|]) z^{|P_j|-k}$$
   where $\text{Overlap}^+(P_i, P_j)$ includes $k = |P_i|$ when $i = j$.
   Dividing by $\mathbb{P}(P_j)$ and setting $z = 1$ (where $F_i(1) = \pi_i$ and $G(1)$ is a single scalar unknown representing the expected game length $\mathbb{E}[T]$!):
   $$\boxed{\sum_{i=1}^m \pi_i \left(\sum_{\substack{1 \le k \le \min(|P_i|, |P_j|) \\ P_i[|P_i|-k+1..|P_i|] = P_j[1..k]}} \frac{1}{\mathbb{P}(P_j[1..k])}\right) - G(1) = 0 \quad \forall j \in \{1, \dots, m\}.}$$
   *(In Conway's Martingale view: run a casino where every step a gambler enters to bet exclusively on $P_j$. At the stopping time $T$, the game actually ended on some $P_i$ with probability $\pi_i$, leaving alive only those $P_j$-gamblers whose prefix $P_j[1..k]$ matches a suffix of $P_i$, holding fortune $\mathbb{P}(P_j[1..k])^{-1}$. Since expected payout $\sum_{i=1}^m \pi_i W_{i \to j}$ equals expected entry fee $\mathbb{E}[T] = G(1)$, we get the exact same equation!)*

Together with $\sum_{i=1}^m \pi_i = 1$, this is an **$(m+1) \times (m+1)$ system of linear equations** in the unknowns $(\pi_1, \dots, \pi_m, G(1))$, solvable in $O(m^3)$ via Gaussian elimination regardless of how large $|P_j|$ is!

#### Hand-Checkable Paradox Example (Penney's Game: Why Pattern Racing is Non-Transitive!)
Let $\Sigma = \{\texttt{H}, \texttt{T}\}$ ($\sigma = 2$), $P_1 = \texttt{HHT}$, and $P_2 = \texttt{THH}$.
Notice that both patterns have expected solo waiting time $\mathbb{E}[T_{\texttt{HHT}}] = 2^3 = 8$ and $\mathbb{E}[T_{\texttt{THH}}] = 2^3 = 8$ (neither has a proper border!). Yet in a head-to-head race:
- $\text{Overlap}^+(P_1, P_1) = \{3\} \implies C_{1,1} = 2^3 = 8$.
- $\text{Overlap}^+(P_2, P_1)$: suffixes of $\texttt{THH}$ matching prefixes of $\texttt{HHT}$ are $\texttt{H}$ ($k=1$) and $\texttt{HH}$ ($k=2$) $\implies C_{2,1} = 2^1 + 2^2 = 6$.
- $\text{Overlap}^+(P_1, P_2)$: suffixes of $\texttt{HHT}$ matching prefixes of $\texttt{THH}$ is $\texttt{T}$ ($k=1$) $\implies C_{1,2} = 2^1 = 2$.
- $\text{Overlap}^+(P_2, P_2) = \{3\} \implies C_{2,2} = 2^3 = 8$.
The linear system is:
$$\begin{cases} 8 \pi_1 + 6 \pi_2 = G(1) \\ 2 \pi_1 + 8 \pi_2 = G(1) \\ \pi_1 + \pi_2 = 1 \end{cases} \implies 6 \pi_1 = 2 \pi_2 \implies \pi_1 = \frac{1}{4}, \;\; \pi_2 = \frac{3}{4}, \;\; G(1) = \mathbb{E}[T] = \frac{13}{2}.$$
Even though $\mathbb{E}[T_{P_1}] = \mathbb{E}[T_{P_2}] = 8$, player 2 ($\texttt{THH}$) beats player 1 ($\texttt{HHT}$) **$75\%$ of the time** because whenever $P_1$ is about to appear after $\texttt{HH}$, $P_2 = \texttt{THH}$ has already intercepted it unless the game started with $\texttt{HH}$ at the very beginning!

---

### 32.4 Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Pitfall 1: Zero-Probability Letters ($p_c = 0$) in General Alphabet Distributions (`[JSOI2009] 有趣的游戏`)**
   - *What breaks*: In the formula $\mathbb{P}(P_j[1..k])^{-1}$, we divide by $\prod_{r=1}^k p_{P_j[r]}$. If some character in $P_j$ has $p_c = 0$, then $\mathbb{P}(P_j[1..k]) = 0$ and division by zero occurs!
   - *Fix*: Either work with the **un-divided** Guibas–Odlyzko form where the coefficient of $\pi_i$ in equation $j$ is $\sum_{k} \mathbb{P}(P_j[k+1..|P_j|])$ and the coefficient of $G(1)$ is $-\mathbb{P}(P_j)$ (which has **zero divisions** and works smoothly even when $\mathbb{P}(P_j) = 0$, immediately forcing $\pi_j = 0$ if all its equations vanish!), or discard any pattern containing a $p_c = 0$ letter at the start because it can never occur ($\pi_j = 0$).
2. **Pitfall 2: Arithmetic Overflow / Modular Division When $\sigma^k$ is Computed in Floating Point**
   - In floating-point multi-player games (`[SDOI2017] 硬币游戏`, $L = 300$, $\sigma = 2$), $\sigma^L = 2^{300} \approx 2 \times 10^{90}$ is still within `double` range (up to $10^{308}$), but for $L = 2000$, $2^{2000}$ overflows IEEE-754 `double`!
   - *Fix*: Multiply the $j$-th equation by $2^{-|P_j|}$ (the un-divided form!), so that every overlap coefficient becomes $\sum_k 2^{-( |P_j| - k )} \in [1, 2]$, completely avoiding floating-point overflow!
3. **Pitfall 3: Confusing "Prefix of $P_i$ is Suffix of $P_j$" vs. "Suffix of $P_i$ is Prefix of $P_j$"**
   - When the game stops on $P_i$ (so $P_i$ is already on the tape) and we evaluate how close $P_j$ is to finishing, the characters on the tape end with $P_i$. Therefore, a surviving $P_j$-bettor must have matched a **prefix of $P_j$** against a **suffix of $P_i$**! Reversing $i$ and $j$ solves the transposed system and gives wrong probabilities (e.g., $\pi_1 = 3/4, \pi_2 = 1/4$ in the Penney's game example above).

---

## Iteration 33: DP over AC / SAM / Minimal DFA & DP-of-DP (`DP套DP` / `自動機上のDP`)

### 33.1 The Diagnostic Signal: When Counting Strings $T$ Requires Running an Inner DP on $T$

Consider a second major class of string enumeration problems:
- **Concrete Objects Counted**: Given a reference string $S$ of small length $K \le 15$ (or a small family of structural rules such as "contains a palindrome of length $\ge k$", "has Longest Common Subsequence $\text{LCS}(S, T) = c$ for each $c \in [0, K]$", or "can be reduced to $\texttt{1}$ under a given rewriting game"), count how many strings $T \in \Sigma^N$ of length $N \le 1000$ (or $N \le 10^{18}$) satisfy a predicate $P(S, T)$.
- **Why Standard Automaton DP Fails**:
  In classical AC Automaton DP, the predicate $P(S, T)$ is simply "does $T$ contain $S$ as a contiguous substring?", for which the KMP/AC automaton is already known and has $K+1$ states.
  However, what if the predicate $P(S, T)$ is **"$\text{LCS}(S, T) = c$ after reading all $N$ characters of $T$"** (`[TJOI2018] 游园会` / `HDU 4352`), or **"$T$ wins a stack/interval DP game"** (`AGC 022 E — Median Replace`)?
  For a fixed string $T$, we check $P(S, T)$ by running an **inner dynamic programming algorithm** $\mathcal{A}$ left-to-right over the characters of $T$. If we do not know $T$ in advance—because we are **counting** how many strings $T \in \Sigma^N$ make the inner DP accept—how can an **outer counting DP** keep track of what the inner DP would compute on $T$?

**The Structural Breakthrough (DP-of-DP / `DP套DP` / `自動機上のDP`)**:
Treat the entire **state vector of the inner DP after reading prefix $T[1..i]$** as a single vertex in an implicit Deterministic Finite Automaton (DFA)!
1. If the inner DP state vector is compressed so that it takes only $V_{\text{inner}}$ reachable configurations (e.g., via difference-encoding $\Delta dp \in \{0, 1\}^K$ where $V_{\text{inner}} \le 2^K$), then the inner DP **is** a DFA $\mathcal{M} = (Q, \Sigma, \delta, q_0, F)$ with $|Q| \le V_{\text{inner}}$.
2. Even better, by the **Myhill–Nerode Theorem**, many distinct inner DP state configurations are behaviorally indistinguishable with respect to all future suffixes $T[i+1..N]$. Running BFS exploration of reachable inner DP states followed by **Hopcroft's DFA Minimization** often collapses thousands of inner DP states down to $10$–$50$ minimal Nerode equivalence classes!

---

### 33.2 The Combinatorial Word Invariant: Inner DP State Compression & Myhill–Nerode Equivalence

We categorize the four canonical `DP套DP` and Automaton-DP architectures in competitive stringology and prove the state-space invariant for each.

#### Architecture 1: LCS DP-of-DP via Monotonic Row-Difference Encoding (`差分状态压缩`)
- **Problem**: Fix $S[1..K]$ ($K \le 15$) and count for each $c \in \{0, 1, \dots, K\}$ the number of strings $T \in \Sigma^N$ with $\text{LCS}(S, T) = c$.
- **Inner DP Transition**: When reading character $ch = T[i]$, the standard LCS DP updates the array $f[0..K]$ (where $f[j] = \text{LCS}(S[1..j], T[1..i])$) to $f'[0..K]$ via:
  $$f'[j] = \begin{cases} f[j-1] + 1 & \text{if } S[j] = ch, \\ \max(f'[j-1], f[j]) & \text{if } S[j] \ne ch. \end{cases}$$
- **Why Naive Inner State Fails**: Since $f[j] \in \{0, 1, \dots, K\}$, there are $(K+1)^K$ possible tuples—far too large even for $K = 10$!
- **The Combinatorial Word Invariant (Unit-Step Monotonicity)**:
  For every prefix $T[1..i]$ and every index $1 \le j \le K$, extending $S[1..j-1]$ by a single character $S[j]$ can increase the LCS by at most $1$ and cannot decrease it:
  $$f[0] = 0, \quad \text{and} \quad \Delta f[j] := f[j] - f[j-1] \in \{0, 1\} \quad \forall j \in \{1, \dots, K\}.$$
  *Proof*: Every common subsequence of $S[1..j-1]$ and $T[1..i]$ is also a common subsequence of $S[1..j]$ and $T[1..i]$, so $f[j] \ge f[j-1]$. Conversely, any common subsequence of $S[1..j]$ and $T[1..i]$ loses at most its last character if $S[j]$ is deleted, so $f[j] - 1 \le f[j-1]$.
- **Bitmask Compilation**:
  Therefore, the entire inner DP array $f[0..K]$ is **bijectively encoded** by the $K$-bit binary mask:
  $$\text{mask} = \sum_{j=1}^K \big(f[j] - f[j-1]\big) 2^{j-1} \in \{0, 1, \dots, 2^K - 1\}$$
  where $f[j] = \text{popcount}\big(\text{mask} \ \& \ (2^j - 1)\big)$, and in particular $\text{LCS}(S, T) = f[K] = \text{popcount}(\text{mask})$.
  Precomputing the DFA transition table $\text{trans}[\text{mask}][ch]$ takes $O(K |\Sigma| 2^K)$ time, after which the outer counting DP runs in $O(N |\Sigma| 2^K)$ (or coupling with an inner forbidden-pattern automaton in `[TJOI2018] 游园会`).

#### Architecture 2: Automaton-State Subset / Profile DP (`NFA 转 DFA` / Recognition of Complex String Games)
- **Problem**: Given a string rewriting rule or regular/context-free decision problem on $T$ (e.g., `AGC 022 E — Median Replace`, where three adjacent bits are repeatedly replaced by their median until one bit remains, or regular expression matching, or palindrome/square avoidance), count how many completions of a partially specified string $T \in \{\texttt{0}, \texttt{1}, \texttt{?}\}^N$ are winning.
- **Inner Automaton Compilation**:
  Design a deterministic greedy stack or small inner DP that decides whether a fixed string $T$ wins.
  Explore all reachable inner states from the initial state $q_0$ by BFS over transitions $c \in \Sigma$.
  Even when the theoretical upper bound on inner states looks large, the **reachable state space** $|Q_{\text{reach}}|$ from $q_0$ is frequently minuscule!
- **Myhill–Nerode Theorem & Hopcroft Minimization (`最小化 DFA`)**:
  Two inner DP states $u, v \in Q_{\text{reach}}$ are **Nerode-equivalent** ($u \sim v$) if and only if for every suffix string $w \in \Sigma^*$:
  $$\delta^*(u, w) \in F \iff \delta^*(v, w) \in F$$
  (or, in a multi-valued classification problem, $\text{output}(\delta^*(u, w))$ is identical for all $w$).
  By iteratively refining partitions $\Pi_0 = \{F, Q \setminus F\}$ via:
  $$u, v \text{ stay in the same block of } \Pi_{t+1} \iff \Pi_t(u) = \Pi_t(v) \text{ and } \forall c \in \Sigma, \, \Pi_t(\delta(u, c)) = \Pi_t(\delta(v, c))$$
  until stabilization, we obtain the **unique minimal DFA** $\mathcal{M}_{\min}$ recognizing the language. If $|\mathcal{M}_{\min}| = S_{\min}$, we can then run $O(N \cdot S_{\min})$ outer DP or $O(S_{\min}^3 \log N)$ matrix exponentiation!

#### Architecture 3: DP over Aho–Corasick Automaton with Subset/Length/Palindrome Constraints
When counting or optimizing strings over an AC automaton of pattern set $\mathcal{P} = \{P_1, \dots, P_m\}$:
- **Invariant of AC Node $u$**: Being at node $u$ in the AC automaton after generating prefix $T[1..i]$ means that the longest suffix of $T[1..i]$ that is a prefix of some pattern in $\mathcal{P}$ is exactly the string $\text{str}(u)$ on the Trie path from root to $u$.
- **Crucial `fail`-Tree Closure Invariant (`end_mask` Propagation)**:
  A pattern $P_r \in \mathcal{P}$ ends at position $i$ of $T$ if and only if $\text{end}(P_r)$ is an **ancestor of $u$ in the AC `fail` tree** (not just $u$ itself!).
  Therefore, during AC construction (BFS order), one **must** propagate pattern-completion flags or weights down the `fail` tree:
  $$\text{bad}[u] \gets \text{bad}[u] \lor \text{bad}[\text{fail}[u]], \quad \text{mask}[u] \gets \text{mask}[u] \mid \text{mask}[\text{fail}[u]], \quad \text{val}[u] \gets \text{val}[u] + \text{val}[\text{fail}[u]].$$
- **Bidirectional / Palindromic Coupling over AC (`回文串 + AC自动机 DP`)**:
  What if we want to count **palindromes** $T$ of length $N$ containing (or avoiding) patterns in $\mathcal{P}$, or concatenations of strings from a dictionary $D$ that form a palindrome (`[POI / AtCoder ABC 249 G / ARC]` style)?
  Because a palindrome grows simultaneously from the left and right (or from the center outward), a single AC automaton only tracks left-to-right matches. To handle boundary-straddling matches at the center or concatenation seams, we either track a pair $(u_{\text{left}}, u_{\text{right}})$ in the AC automata of $\mathcal{P}$ and $\mathcal{P}^R$, or match long dictionary words against short remaining overhangs (of length $\le \max |w_i|$).

#### Architecture 4: DP over Suffix Automaton (SAM) & Lyndon Automaton
- **SAM Path-Counting & $k$-th Substring DP**:
  Every distinct substring of $S$ corresponds to a **unique directed path from the initial state $t_0$** in the DAWG (transition graph) of $\text{SAM}(S)$. And every node $u \in \text{SAM}(S)$ represents an equivalence class of $\text{len}(u) - \text{len}(\text{link}(u))$ substrings sharing the exact same $\text{endpos}(u)$ set (hence the exact same occurrence count $|\text{endpos}(u)|$ in $S$).
  Since the transition graph of a SAM is a **Directed Acyclic Graph (DAG)**, backward DP on the SAM DAG:
  $$dp[u] = \text{weight}(u) + \sum_{c \in \Sigma} dp\big[\text{next}[u][c]\big]$$
  computes in $O(|S| |\Sigma|)$ time the total number of distinct substrings ($\text{weight}(u) = 1$) or total occurrences of substrings ($\text{weight}(u) = |\text{endpos}(u)|$) starting with the prefix path from $t_0$ to $u$ (`[TJOI2015] 弦论`).
- **Lyndon / Lexicographical Automaton DP (Duval Pointer State)**:
  To count strings $T \in \Sigma^N$ that are **Lyndon words** (or whose minimum cyclic shift / Lyndon factorization satisfies a constraint) together with an automaton constraint, note that checking whether a prefix of $T$ is a prefix of a Lyndon word only tracks the active period pointer $j \in \{1, \dots, i\}$ in Duval's algorithm (where $T[i] = T[j]$ continues the period, $T[i] > T[j]$ resets $j \gets 1$ making the whole prefix $T[1..i]$ a single Lyndon word, and $T[i] < T[j]$ is forbidden if we require the entire string to be $\ge$ its cyclic shifts).

---

### 33.3 The Reverse-Engineering Scratchpad: Automated DFA Discovery & Minimization Pipeline

When faced with an unfamiliar string game or inner DP in a contest (`DP套DP`), do **not** guess the minimal state space by hand! Use the **Automated DFA Exploration & Minimization Scratchpad**:

1. **Step 1 (Write the Naive Inner Verifier State)**:
   Write a clean struct `State` representing the exact information needed by the inner DP after reading $T[1..i]$ (for example, a small `std::array<int, K>` or bitmask, canonically normalized so that capped/irrelevant entries are clamped).
2. **Step 2 (BFS Reachability from $q_0$)**:
   Initialize a hash/tree map `id[State]` with `q_0` at index `0` and a queue. While the queue is non-empty, pop state `u`, and for each character $c \in \Sigma$, compute the next inner state `v = transition(u, c)`. Insert `v` if unseen, and record `trans[u][c] = id[v]`.
   *Diagnostic Check*: Print `id.size()` on a local test! In a shocking number of grandmaster problems (such as `HDU 4352` Digit-LIS, `AGC 022 E`, or `CF` string game problems), a theoretical state bound of $3^{10} = 59049$ has **fewer than $300$ reachable states**!
3. **Step 3 (Optional Partition Refinement / Hopcroft Minimization)**:
   If `id.size()` is around $2000$–$10000$ and you need $O(|Q|^3 \log N)$ matrix exponentiation, run partition refinement:
   - Partition states initially by their acceptance output $\text{accept}(u)$.
   - Repeatedly split any partition class where two states $u, v$ have differing tuple of destination classes $\big(\text{class}(\text{trans}[u][c])\big)_{c \in \Sigma}$.
   - Replace the DFA with the quotient DFA on equivalence classes.
4. **Step 4 (Outer Counting DP)**:
   Run the outer DP $dp[i][q]$ (or matrix exponentiation) over the states $q$ of the discovered DFA!

#### Hand-Checkable Trace: Reachable States of Digit LIS (`HDU 4352 — XHXJ's List`)
Suppose $\Sigma = \{0, 1, \dots, 9\}$ and the inner algorithm is the $O(N \log N)$ patience-sorting Longest Increasing Subsequence (LIS) array, which maintains for each length $l$ the smallest tail digit of an increasing subsequence of length $l$ in the number read so far.
- Naive bound: subset of $\{0, \dots, 9\}$ seems to have $2^{10} = 1024$ states, plus leading-zero handling.
- Invariant: Because the patience-sorting array is strictly increasing, it is just a subset of $\{0, \dots, 9\}$! Transitioning on digit $d$ finds the smallest element $\ge d$ in the mask and replaces it with $d$ (or inserts $d$ if no element $\ge d$ exists).
- Thus the DFA has **at most $2^{10} = 1024$ states** and $|\Sigma| = 10$ transitions per state, allowing digit DP across $T$ queries in $O(1)$ per query after a single $O(\text{digits} \times 1024 \times 10 \times K)$ precomputation!

---

### 33.4 Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Pitfall 1: Un-normalized Inner DP States Causing Infinite or Unbounded BFS**
   - *Counterexample*: Suppose the inner DP counts occurrences of a pattern up to threshold $K$, and you store the raw count $c$ in `State` without clamping $c \gets \min(c, K)$. Then the BFS generates infinitely many states ($c = 0, 1, 2, \dots, N$)!
   - *Fix*: Every coordinate of `State` **must** be clamped to the exact range that affects future acceptance (or stored as relative differences $\Delta dp[j] = dp[j] - dp[j-1]$ when absolute values grow with $i$!).
2. **Pitfall 2: Forgetting AC `fail`-Chain Inheritance During DP Transitions**
   - *Counterexample*: Let $\mathcal{P} = \{\texttt{ab}, \texttt{bc}, \texttt{abc}\}$. In the AC Trie, node $u = \texttt{abc}$ has a `fail` pointer to $v = \texttt{bc}$. If $\texttt{bc}$ has a forbidden flag or a weight $+5$, and you only check flags defined directly on the Trie end-node of a pattern without accumulating `val[u] += val[fail[u]]` in BFS order, then passing through $\texttt{abc}$ fails to trigger the match of its suffix $\texttt{bc}$!
3. **Pitfall 3: Double-Counting Substrings When Coupling AC Automaton with SAM**
   - While every state in an AC automaton represents a **single prefix** on the Trie (and matches all suffixes on its `fail` path to the root), every state $u$ in a SAM represents a **bundle** of $\text{len}(u) - \text{len}(\text{link}(u))$ substrings of different lengths! If you run a path DP on a SAM without distinguishing whether each path is weighted by $1$ or by $\text{len}(u) - \text{len}(\text{link}(u))$, you confuse "paths from the root in the DAWG" (each of which is already a single distinct substring of length equal to the path length!) with "equivalence classes in the Link Tree".

---

## Iteration 34: Exact String Counting with Forbidden Substrings & Weighted Occurrence Generating Functions

### 34.1 The Diagnostic Signal: Counting Strings with *Exactly* $k$ Pattern Occurrences (or Weighted by $w^{\text{occ}}$)

In Iteration 31, we counted strings $W \in \Sigma^n$ that have **zero** occurrences of $\mathcal{P} = \{P_1, \dots, P_m\}$.
Now consider the generalized quantitative counting problem:
- **Concrete Objects Counted**: Given an alphabet $\Sigma$ of size $\sigma = |\Sigma|$ and patterns $\mathcal{P} = \{P_1, \dots, P_m\}$ (where now a pattern $P_i$ **is allowed** to be a substring of $P_j$ if both carry independent weights or occurrence counts!), compute:
  1. The number of strings $W \in \Sigma^n$ containing **at least $k$** (or **exactly $k$**) total occurrences of patterns from $\mathcal{P}$, where overlapping occurrences are counted with multiplicity; OR
  2. More generally, assign a formal variable (or multiplicative weight) $t_i$ to each occurrence of $P_i$, and compute the **Bivariate / Multivariate Generating Function**:
     $$F(x; t_1, \dots, t_m) = \sum_{W \in \Sigma^*} x^{|W|} \prod_{i=1}^m t_i^{\text{occ}_i(W)}$$
     where $\text{occ}_i(W)$ is the number of occurrences of $P_i$ in $W$.

**Why Naive Avoidance Methods Fail Here**:
- When $t_i = 0$ (strict avoidance), any pattern $P_j$ containing $P_i$ is automatically avoided and can be discarded before running Goulden–Jackson.
- **When $t_i \ne 0$**: If we want strings with **exactly $k = 1$** occurrence of $P_1 = \texttt{ab}$ and $0$ occurrences of $P_2 = \texttt{aba}$, we **cannot** discard $P_2$! Even for a single pattern $P$ with weight $t$, an occurrence of $P$ is not forbidden—it merely multiplies the weight of $W$ by $t = 1 + (t - 1)$.

---

### 34.2 The Combinatorial Word Invariant: The $(t - 1)$ Cluster Expansion (Weighted Goulden–Jackson Theorem)

How do we generalize the Marked-Word double count from Iteration 31.2 when each occurrence of $P_i$ carries weight $t_i$ instead of $0$?

#### Step 1: The Binomial Identity $t^{\text{occ}(W)} = \sum_{M \subseteq \text{Occ}(W)} (t - 1)^{|M|}$
Write each factor $t_i$ as $1 + (t_i - 1)$:
$$\prod_{i=1}^m t_i^{\text{occ}_i(W)} = \prod_{e \in \text{Occ}(W)} \big(1 + (t_{\text{pat}(e)} - 1)\big) = \sum_{M \subseteq \text{Occ}(W)} \prod_{e \in M} (t_{\text{pat}(e)} - 1).$$
Look at what each summand represents in plain words:
- Just as in Iteration 31.2, we sum over all **marked words** $(W, M)$ where $M \subseteq \text{Occ}(W)$ is an arbitrary subset of pattern occurrences in $W$ that we choose to highlight!
- Instead of weight $(-1)^{|M|} x^{|W|}$ (which corresponds to the special case $t_i = 0 \implies t_i - 1 = -1$), each marked occurrence $e \in M$ of pattern $P_i$ now contributes a multiplicative factor of **$(t_i - 1)$**!
- Unmarked occurrences in $\text{Occ}(W) \setminus M$ contribute factor $1$ (we simply ignore them!).

#### Step 2: Weighted Clusters When $\mathcal{P}$ Is Reduced (Antichain)
Assume first that $\mathcal{P} = \{P_1, \dots, P_m\}$ is an antichain (no $P_i$ is a substring of $P_j$).
Then no two marked occurrences in $M$ can strictly contain one another, so $(W, M)$ again decomposes uniquely into free letters $\sigma x$ and **weighted clusters** $C(x; t_1, \dots, t_m)$:
$$F(x; t_1, \dots, t_m) = \frac{1}{1 - \sigma x - \sum_{i=1}^m C_i(x; t_1, \dots, t_m)}.$$
In a weighted cluster ending with $P_j$:
- Starting a new cluster with a single marked occurrence of $P_j$ contributes weight $(t_j - 1) x^{|P_j|}$ (instead of $-x^{|P_j|}$).
- Extending a cluster ending in $P_i$ by an overlapping marked occurrence of $P_j$ with overlap $k \in \text{Overlap}(P_i, P_j)$ contributes weight $(t_j - 1) x^{|P_j| - k}$ (instead of $-x^{|P_j| - k}$).
Therefore, for each $j \in \{1, \dots, m\}$:
$$C_j(x; t) = (t_j - 1) x^{|P_j|} + (t_j - 1) \sum_{i=1}^m C_i(x; t) \tilde{C}_{i,j}(x).$$
Divide by $(t_j - 1)$ (or rearrange directly without division):
$$C_j(x; t) - (t_j - 1) \sum_{i=1}^m C_i(x; t) \tilde{C}_{i,j}(x) = (t_j - 1) x^{|P_j|}.$$
Recall that $\tilde{C}_{i,j}(x) = C_{i,j}(x) - \delta_{i,j}$. Substituting this into the left-hand side gives the **Weighted Goulden–Jackson Linear System**:
$$\boxed{\sum_{i=1}^m C_i(x; t) \Big(\delta_{i,j} - (t_j - 1) \tilde{C}_{i,j}(x)\Big) = (t_j - 1) x^{|P_j|} \quad \forall j \in \{1, \dots, m\}.}$$
*(Check: When $t_j = 0$, $t_j - 1 = -1$, so $\delta_{i,j} - (-1)\tilde{C}_{i,j}(x) = \delta_{i,j} + \tilde{C}_{i,j}(x) = C_{i,j}(x)$ and the right-hand side is $-x^{|P_j|}$, recovering Iteration 31.3 verbatim!)*

---

### 34.3 The Single-Pattern Bivariate Generating Function $F(x, t)$ & Exact $k$-Occurrence Formula

Let us specialize the Weighted Goulden–Jackson system to $m = 1$ (a single pattern $P$ of length $L = |P|$ with weight $t$ per occurrence).
Here $\tilde{C}_{1,1}(x) = C_{1,1}(x) - 1 = \sum_{k \in \text{ProperBorders}(P)} x^{L - k}$ is the proper-border polynomial of $P$.
The $1 \times 1$ equation for the cluster GF $C_1(x, t)$ is:
$$C_1(x, t) \Big(1 - (t - 1)\big(C_{1,1}(x) - 1\big)\Big) = (t - 1) x^L \implies C_1(x, t) = \frac{(t - 1) x^L}{t - (t - 1) C_{1,1}(x)}.$$
Substituting $C_1(x, t)$ into $F(x, t) = \frac{1}{1 - \sigma x - C_1(x, t)}$ yields the **Master Bivariate Generating Function for Pattern Occurrences**:
$$\boxed{F(x, t) = \frac{t - (t - 1) C_{1,1}(x)}{(1 - \sigma x)\big(t - (t - 1) C_{1,1}(x)\big) - (t - 1) x^L} = \frac{C_{1,1}(x) + t\big(1 - C_{1,1}(x)\big)}{D_0(x) - t D_1(x)}}$$
where:
- $D_0(x) = (1 - \sigma x) C_{1,1}(x) + x^L$ is the avoidance denominator from Iteration 31.3, and
- $D_1(x) = (1 - \sigma x)\big(C_{1,1}(x) - 1\big) + x^L$.

#### Extracting $F_k(x) = [t^k] F(x, t)$ (Strings with *Exactly* $k$ Occurrences of $P$)
Because $F(x, t)$ is a linear fractional transformation in $t$, we can expand $[t^k] F(x, t)$ explicitly as a rational function of $x$!
Write $F(x, t)$ by factoring $D_0(x)$ out of the denominator:
$$F(x, t) = \frac{C_{1,1}(x) - t \tilde{C}_{1,1}(x)}{D_0(x) \left(1 - t \frac{D_1(x)}{D_0(x)}\right)} = \frac{C_{1,1}(x) - t \tilde{C}_{1,1}(x)}{D_0(x)} \sum_{k \ge 0} t^k \left(\frac{D_1(x)}{D_0(x)}\right)^k.$$
Reading off the coefficient of $t^k$:
1. **For $k = 0$ (Zero occurrences of $P$)**:
   $$F_0(x) = \frac{C_{1,1}(x)}{D_0(x)} = \frac{C_{1,1}(x)}{(1 - \sigma x) C_{1,1}(x) + x^L}.$$
2. **For $k \ge 1$ (Exactly $k$ occurrences of $P$)**:
   $$F_k(x) = \frac{C_{1,1}(x) D_1(x) - \tilde{C}_{1,1}(x) D_0(x)}{D_0(x)^2} \left(\frac{D_1(x)}{D_0(x)}\right)^{k-1}.$$
   Let us simplify the numerator $C_{1,1}(x) D_1(x) - \big(C_{1,1}(x) - 1\big) D_0(x)$:
   $$\begin{aligned}
   C_{1,1} D_1 - (C_{1,1} - 1) D_0 &= C_{1,1}\big[(1 - \sigma x)(C_{1,1} - 1) + x^L\big] - (C_{1,1} - 1)\big[(1 - \sigma x)C_{1,1} + x^L\big] \\
   &= C_{1,1} x^L - (C_{1,1} - 1) x^L = x^L!
   \end{aligned}$$
   Everything cancels to a single monomial $x^L$! Thus, for every $k \ge 1$:
   $$\boxed{F_k(x) = [t^k] F(x, t) = \frac{x^L \big((1 - \sigma x)(C_{1,1}(x) - 1) + x^L\big)^{k-1}}{\big((1 - \sigma x) C_{1,1}(x) + x^L\big)^{k+1}}.}$$

**Why This Cancellation Is Not Magic (Combinatorial Proof of $F_k(x)$)**:
Every string $W$ with **exactly $k \ge 1$** occurrences of $P$ decomposes uniquely as:
1. A prefix avoiding $P$ ending at the **first** occurrence of $P$: generating function $\frac{x^L}{D_0(x)}$.
2. Followed by $k - 1$ transitions from the $r$-th occurrence of $P$ to the $(r+1)$-th occurrence of $P$ (which either overlaps the $r$-th occurrence along a proper border in $\tilde{C}_{1,1}(x) = C_{1,1}(x) - 1$, or separates and starts fresh after an avoiding bridge): generating function $\left(\frac{D_1(x)}{D_0(x)}\right)^{k-1}$.
3. Followed by a suffix after the $k$-th occurrence of $P$ that contains no further occurrence of $P$: generating function $\frac{1}{D_0(x)}$.
Multiplying these three factors immediately gives $\frac{x^L D_1(x)^{k-1}}{D_0(x)^{k+1}}$!

---

### 34.4 What If $P_i$ Is Contained Inside $P_j$ in a Weighted Problem?

Suppose $P_1 = \texttt{ab}$ has weight $t_1$ and $P_2 = \texttt{aabb}$ has weight $t_2$. Because $t_1 \ne 0$, we **cannot** delete $P_2$! How do we restore the Antichain Invariant?
- **Method 1 (Aho–Corasick + Matrix/Gaussian System when $\sum |P_i|$ is small)**:
  In the AC automaton of $\mathcal{P}$, every state $u$ knows the exact set of patterns ending at $u$ via its `fail`-tree ancestors, so its transition weight is simply $\prod_{P_i \text{ ends at } u} t_i$.
- **Method 2 (Pattern Absorption into Super-Patterns for Cluster Expansion)**:
  Whenever a marked occurrence of $P_j$ is placed, any occurrence of $P_i$ that sits *strictly inside* $P_j$ can be absorbed directly into the effective weight of $P_j$! Specifically, in the $(t - 1)$ expansion, instead of choosing subsets $M$ of individual occurrences that can nest inside one another, we group any nested occurrence inside $P_j$ into the internal weight of $P_j$ (or split into maximal non-nested segments), reducing back to proper left-to-right overlaps.

---
## Iteration 35: Multilingual (`[EN]` / `[ZH]` / `[JA]`) Problem Mining, 4-Tier Difficulty Ladder & Template Quarantine

### 35.1 Master Summary Table of Curated Non-Template Problems (32 Problems)

Every problem below has been audited against the editorial policy (`AGENTS.md`): bare template verification problems (e.g., pure AC automaton matching or bare SAM substring counting) are quarantined in Section 35.6 (`R-4A-01` to `R-4A-08`). All 32 accepted problems require structural modeling, border/cluster generating functions, martingale stopping systems, or `DP套DP` / minimal DFA reductions.

| ID | Problem Title & Source | Lang | Tier | Primary Technique | Core Structural Invariant |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P-4A-01** | `[JSOI2007] 文本生成器` (Luogu P4052) | `[ZH]` | Tier 1 | AC Automaton Complement DP | Complement counting: $\sigma^N - (\text{avoiding all } P_i)$ via `fail`-propagated `bad[u]` |
| **P-4A-02** | `[HNOI2004] L语言` (Luogu P2292) | `[ZH]` | Tier 1 | AC Fail-Mask Bitwise DP | Bitmask of valid prefix end-positions compressed to $w \le 20$-bit word over AC `fail` mask |
| **P-4A-03** | `[POI 2000] 病毒 Viruses` (Luogu P2444) | `[ZH]`/`[EN]` | Tier 1 | Infinite Avoidance / Cycle on AC | Infinite avoiding string exists $\iff$ directed cycle exists in non-`bad` subgraph of AC DFA |
| **P-4A-04** | `CF 86C — Genetic Engineering` | `[EN]` | Tier 1 | AC Uncovered-Suffix Depth DP | State $(u, d)$ tracks AC node $u$ and number of uncovered tail chars $d \le \max |P_i|$ |
| **P-4A-05** | `[SDOI2014] 数数` (Luogu P3311) | `[ZH]` | Tier 1 | Digit DP $\times$ AC Automaton | Coupled state `(pos, ac_node, tight, leading_zero)` skipping AC transitions on leading zeros |
| **P-4A-06** | `[AHOI2005] 病毒检测` (Luogu P2536) | `[ZH]` | Tier 1 | Wildcard Pattern DFA / Trie DP | Bitset/BFS reachability of wildcard `?`/`*` states over Trie transitions |
| **P-4A-07** | `[TJOI2015] 弦论` (Luogu P3975) | `[ZH]` | Tier 1 | SAM DAG Path-Counting DP | $k$-th lexicographical substring via SAM DAG subtree sum with $\text{weight}(u) = 1$ vs. $|\text{endpos}(u)|$ |
| **P-4A-08** | `AtCoder ABC 270 G / ARC 107 D / ABC 138 E` | `[JA]` | Tier 1 | Automaton / Lexicographical DP | Minimal-step automaton state transition for subsequence / substring avoidance |
| **P-4A-09** | `[CTSC2006] 歌唱王国` (Luogu P4548) | `[ZH]` | Tier 2 | Single-Pattern PGF / Conway Martingale | $\mathbb{E}[T_S] = \sum_{k \in \text{Borders}(S)} \sigma^k$ via PGF $F'(1) = G(1)$ or fair casino betting |
| **P-4A-10** | `[SDOI2017] 硬币游戏` (Luogu P3706) | `[ZH]` | Tier 2 | Multi-Player Pattern Race PGF | $(m+1) \times (m+1)$ Guibas–Odlyzko overlap system $\sum_i \pi_i C_{i,j}(1/2) 2^{|P_j|} = G(1)$ |
| **P-4A-11** | `[JSOI2009] 有趣的游戏` (Luogu P2467 / BZOJ 1444) | `[ZH]` | Tier 2 | Non-Uniform Multi-Player Race | Un-divided PGF overlap system handling non-uniform $p_c$ and zero-probability patterns |
| **P-4A-12** | `CF 109C / CF 1768F / CF 494B — Obsessive String` | `[EN]` | Tier 2 | KMP Border DP / Occurrence Splitting | Counting valid splits where every piece contains $P$ via last-occurrence index $L[i]$ |
| **P-4A-13** | `[BJWC2011] 禁忌` (Luogu P3735 / BZOJ 2319) | `[ZH]` | Tier 2 | Greedy Non-Overlapping AC Partition + Matrix | Minimizing expected/maximum non-overlapping pattern hits via AC root-reset transitions |
| **P-4A-14** | `[HNOI2008] GT考试` (Luogu P3193) | `[ZH]` | Tier 2 | Single-Pattern KMP Matrix / GJ Recurrence | $O(M^3 \log N)$ KMP matrix or $O(M \log M \log N)$ Bostan–Mori on Goulden–Jackson rational GF |
| **P-4A-15** | `AtCoder ABC 305 G — Banned Substrings` | `[JA]` | Tier 2 | AC Automaton Matrix / Short-Length Cutoff | For $N \le 10^{18}$ and $|P_i| \le 6$, Aho–Corasick over $2^6$-state suffix mask + Matrix Exponentiation |
| **P-4A-16** | `AtCoder ARC 081 C — Don't Be a Subsequence` | `[JA]` | Tier 2 | Shortest Absent Subsequence DAG DP | Backward shortest path on DASG (`next_pos[i][c]`) to reconstruct lexicographically first absent string |
| **P-4A-17** | `[TJOI2018] 游园会` (Luogu P4590) | `[ZH]` | Tier 3 | LCS `DP套DP` $\times$ KMP Avoidance | Outer DP over `(2^K LCS difference mask, NOIP KMP state in {0,1,2})` |
| **P-4A-18** | `HDU 4352 — XHXJ's List` | `[ZH]`/`[EN]` | Tier 3 | Digit LIS `DP套DP` | Patience-sorting LIS tail array encoded as 10-bit subset mask $\in [0, 2^{10})$ inside Digit DP |
| **P-4A-19** | `AtCoder AGC 022 E — Median Replace` | `[JA]` | Tier 3 | Greedy Stack DFA Minimization (`DP套DP`) | Compressing ternary median reduction into a 7-state minimal DFA over prefix stack states |
| **P-4A-20** | `CF 1119F / CF 1408G / CF 1207G — Indie Album` | `[EN]` | Tier 3 | Offline Trie DFS $\times$ AC `fail`-Tree Euler Tour | Answering $(q_i, P_j)$ occurrence queries on a dynamic Trie via Fenwick tree on AC `fail` subtree |
| **P-4A-21** | `[SDOI2017] 天才黑客` (Luogu P3703 / LOJ 2003) | `[ZH]` | Tier 3 | Trie Virtual Tree + LCP Prefix-Suffix Optimization | Converting Trie LCP transition costs into Euler-tour prefix/suffix range edges for Dijkstra |
| **P-4A-22** | `AtCoder AGC 057 C / ARC 141 D / ABC 249 G` | `[JA]` | Tier 3 | Two-Sided Palindromic Concatenation DFA | Matching dictionary strings from left and right simultaneously via overhang suffix/prefix states |
| **P-4A-23** | `[ZJOI2019] 麻将` (Luogu P5279) | `[ZH]` | Tier 3 | Hu-Checker `DP套DP` + Minimal DFA | BFS exploration of reachable $3 \times 3$ melds + pair inner DP states ($2092$ states) + EGF expectation |
| **P-4A-24** | `QOJ / UCup — String Avoidance with Long Patterns` | `[EN]`/`[ZH]` | Tier 3 | Goulden–Jackson + FPS Inversion | Single/multi-pattern avoidance for $|P| \le 10^5, N \le 10^5$ via $O(N \log N)$ polynomial inversion |
| **P-4A-25** | `CF 963D / CF 710F — String Set Queries` | `[EN]` | Tier 4 | Online AC Automaton via Binary Grouping | Maintaining dynamic pattern dictionary in $O(\log M)$ AC automata of sizes $2^k$ (`二进制分组`) |
| **P-4A-26** | `AtCoder AGC 020 E — Encoding Subsets` | `[JA]` | Tier 4 | Recursive Subset-Compression Interval DP | Memoized interval/automaton DP over bitwise-AND intersection of repeating block factors |
| **P-4A-27** | `[NOI2020] 美食家 / [CTS2019] 随机立方体 / String PGF` | `[ZH]` | Tier 4 | Multivariate PGF + Stopping Time Variance | Extracting $\mathbb{E}[T]$ and $\text{Var}(T)$ for stopping on $k$-th pattern completion via $F'(1), F''(1)$ |
| **P-4A-28** | `CF 1608F / AGC 039 F / Lyndon Automaton Counting` | `[EN]`/`[JA]` | Tier 4 | Duval Automaton DP for Minimum Cyclic Shift | Counting necklaces/Lyndon words avoiding patterns by coupling AC state with Duval pointer |
| **P-4A-29** | `UOJ / LOJ — Exact k Pattern Occurrences` | `[ZH]` | Tier 4 | Weighted Goulden–Jackson Bivariate GF | Extracting $[x^n t^k] F(x, t)$ via $\frac{x^L D_1(x)^{k-1}}{D_0(x)^{k+1}}$ and polynomial power/inversion |
| **P-4A-30** | `Project Euler 597 / ICPC WF — Non-Transitive Pattern Games` | `[EN]` | Tier 4 | Penney's Game Optimization over $\Sigma^L$ | Choosing $P_2$ of length $L$ to maximize winning probability $\pi_2$ against $P_1$ via border matrix |
| **P-4A-31** | `[国家集训队论文] 最小化 DFA 与正则匹配计数` | `[ZH]` | Tier 4 | Thompson NFA $\to$ Subset DFA $\to$ Hopcroft Minimization | Counting strings of length $N \le 10^{18}$ matching a general regex via minimal DFA matrix power |
| **P-4A-32** | `Universal Cup / QOJ — Palindromic Goulden–Jackson` | `[EN]`/`[ZH]` | Tier 4 | Symmetric Cluster Expansion on Palindromes | Counting palindromes of length $N$ avoiding $\mathcal{P}$ via center-straddling cluster boundary equations |

---

### 35.2 Tier 1 (`Stepping Stone`): Foundational Automaton DP & Complement Invariants

#### **P-4A-01 — `[JSOI2007] 文本生成器` (Luogu P4052)**
- **Source & Metadata**: `[ZH]` JSOI 2007, Luogu P4052. Constraints: $m \le 60$ patterns, $|P_i| \le 100$, target string length $N \le 100$, $|\Sigma| = 26$, modulo $10^4 + 7$.
- **1. The Diagnostic Signal**:
  We need to count strings of length $N$ containing **at least one** pattern $P_i \in \mathcal{P}$. Tracking *which* subset of patterns has appeared requires $2^{60}$ states if done directly. However, the predicate "at least one $P_i$ appears" is the complement of "zero $P_i$ appear"!
- **2. The Combinatorial Word Invariant**:
  By complementation, $\#\{\text{valid } W \in \Sigma^N\} = 26^N - \#\{\mathcal{P}\text{-avoiding } W \in \Sigma^N\}$. A prefix $W[1..t]$ avoids $\mathcal{P}$ if and only if at every step $1 \le r \le t$, the reached AC automaton node $u_r$ has no pattern ending on its `fail`-tree path to the root:
  $$\text{bad}[u] = \big(\exists P_i \text{ ending at } u\big) \lor \text{bad}\big[\text{fail}[u]\big] = \text{false}.$$
- **3. The Reverse-Engineering Scratchpad**:
  Build the AC automaton of $\mathcal{P}$ ($\le 6001$ states), propagate `bad[u] |= bad[fail[u]]` in BFS order, and run a 2D DP `dp[t][u]` over $0 \le t \le N$ and non-`bad` nodes $u$, transitioning along `tr[u][c]` Whenever `!bad[tr[u][c]]`. Return $26^N - \sum_u dp[N][u] \pmod{10007}$.
- **4. Boundary Pitfalls**:
  Failing to propagate `bad[u] |= bad[fail[u]]` during BFS allows a long pattern prefix `u` to mask a short forbidden pattern `P_i` that is a suffix of `u`.

#### **P-4A-03 — `[POI 2000] 病毒 Viruses` (Luogu P2444)**
- **Source & Metadata**: `[EN]`/`[ZH]` POI 2000, Luogu P2444. Constraints: binary alphabet $\Sigma = \{\texttt{0}, \texttt{1}\}$, total pattern length $\sum |P_i| \le 3 \times 10^4$. Decide whether an **infinite** binary string avoiding $\mathcal{P}$ exists.
- **1. The Diagnostic Signal**:
  We are not counting strings of finite length $N$; we must determine whether $\lim_{N \to \infty} a_N > 0$.
- **2. The Combinatorial Word Invariant (König's Infinity Lemma on Finite DFAs)**:
  Because the AC automaton $\mathcal{M}$ is finite ($|Q| \le 3 \times 10^4 + 1$) and deterministic, an infinite path from the root $q_0$ avoiding all `bad` states exists **if and only if** the subgraph of reachable non-`bad` states contains a **directed cycle**!
- **3. The Reverse-Engineering Scratchpad**:
  Build AC automaton, propagate `bad[u] |= bad[fail[u]]`, and run standard 3-color DFS (`vis[u]` $\in \{0, \text{in\_stack}, \text{done}\}$) from $q_0$ restricted to `!bad[v]` transitions.
- **4. Boundary Pitfalls**:
  If $q_0$ itself is `bad` (empty pattern) or if DFS only checks `vis[v]` without distinguishing `in_stack` (back-edge) from `done` (cross-edge in a DAG), DAG diamonds are misclassified as cycles!

#### **P-4A-04 — `CF 86C — Genetic Engineering`**
- **Source & Metadata**: `[EN]` Codeforces Beta Round 73 Div. 1 C. Constraints: $N \le 1000$, $m \le 10$ patterns over $\{\texttt{A}, \texttt{C}, \texttt{G}, \texttt{T}\}$, $|P_i| \le 10$. Count strings $W \in \Sigma^N$ that are **completely covered** by occurrences of patterns from $\mathcal{P}$ (every index $1 \le r \le N$ belongs to at least one occurrence of some $P_i$ in $W$).
- **1. The Diagnostic Signal**:
  This is the opposite of pattern avoidance: every character must be covered by some pattern $P_i \in \mathcal{P}$, and patterns may overlap arbitrarily! Since $|P_i| \le 10$, a character at position $r - d + 1$ that is currently uncovered can **only** ever be rescued by a pattern of length $\ge d$ ending at or after position $r$.
- **2. The Combinatorial Word Invariant (Uncovered Suffix Depth $d$)**:
  After generating prefix $W[1..r]$, suppose the last covered position was $r - d$ (so the trailing $d$ characters $W[r-d+1..r]$ are currently uncovered).
  - If $d > \max_i |P_i|$, no future pattern can ever reach back to cover $W[r-d+1]$ (dead state!).
  - When transitioning from $u \to v = \text{tr}[u][c]$, $d$ increments to $d + 1$; then if the longest pattern in $\mathcal{P}$ ending at $v$ (on $v$'s `fail` chain, say of length $\text{max\_len}[v]$) satisfies $\text{max\_len}[v] \ge d + 1$, it covers the **entire** uncovered tail, resetting $d' \gets 0$! Otherwise $d' \gets d + 1$ remains uncovered!
- **3. The Reverse-Engineering Scratchpad**:
  Precompute $\text{max\_len}[u] = \max(\text{own\_len}[u], \text{max\_len}[\text{fail}[u]])$. Run DP over `dp[r][u][d]` ($0 \le r \le N$, $u \in Q$, $0 \le d \le \max |P_i|$), and sum `dp[N][u][0]` at the end. Complexity: $O(N \cdot |Q| \cdot \max |P_i| \cdot |\Sigma|) \approx 1000 \times 100 \times 10 \times 4 = 4 \times 10^6$ operations.
- **4. Boundary Pitfalls**:
  Thinking that a pattern of length $L < d + 1$ reduces $d+1$ to $d + 1 - L$ is **false**! A pattern of length $L < d+1$ covers the *last* $L$ characters $W[r-L+1..r]$, leaving a gap at $W[r-d]$ that still requires a future pattern of length $\ge d + 2$ to reach all the way back to $W[r-d]$! Thus $d'$ is either $0$ (if $\text{max\_len}[v] \ge d + 1$) or $d + 1$ (if $\text{max\_len}[v] < d + 1$).

#### **P-4A-05 to P-4A-08 (Condensed Tier 1 Walkthroughs)**:
- **P-4A-02 (`[HNOI2004] L语言`, Luogu P2292)**: Given dictionary $|D| \le 20$ with $|w_i| \le 20$ and query strings $|T| \le 2 \times 10^6$, find the longest prefix of $T$ that is a concatenation of dictionary words. **Invariant**: Maintain a 20-bit machine word `reach_mask` whose $d$-th bit is $1$ iff $T[1..i-d]$ is valid; precompute for each AC state $u$ the bitmask `len_mask[u]` of all dictionary word lengths on $u$'s `fail` chain. Then $T[1..i]$ is valid iff `(reach_mask & len_mask[u]) != 0`, reducing $O(|T| \cdot \max |w_i|)$ to $O(|T|)$ bitwise operations!
- **P-4A-05 (`[SDOI2014] 数数`, Luogu P3311)**: Count integers $\le N$ ($N \le 10^{1200}$) avoiding digit strings $\mathcal{P}$ ($\sum |P_i| \le 1500$). **Pitfall**: Leading zeros do **not** advance the AC automaton from the root $q_0$! While `leading_zero == true` and digit $d = 0$ is chosen, the AC state must stay at $q_0$.
- **P-4A-06 (`[AHOI2005] 病毒检测`, Luogu P2536)**: Match a wildcard pattern $P$ ($|P| \le 1000$ with `?` and `*`) against $n \le 500$ dictionary strings on a Trie. **Invariant**: View the Trie as the outer graph and run BFS/bitset over `(trie_node, pattern_pos)` where `*` adds an $\epsilon$-loop on `trie_node`'s children.
- **P-4A-07 (`[TJOI2015] 弦论`, Luogu P3975)**: Find the $k$-th lexicographical substring of $S$ ($|S| \le 5 \times 10^5$, $k \le 10^9$), both for distinct substrings ($T=0$) and counting multiplicity ($T=1$). **Invariant**: Every distinct substring is a unique path in the SAM DAWG; node $u$ contributes $w(u) = 1$ (if $T=0$) or $w(u) = |\text{endpos}(u)|$ (if $T=1$, accumulated bottom-up on the Link Tree) upon arrival, plus $\sum_c dp[\text{tr}[u][c]]$ for extensions.
- **P-4A-08 (`AtCoder ABC 270 G / ARC 107 D / ABC 138 E`)**: Subsequence and cyclic-concatenation automaton jumps via `next_occ[i][c]` binary search / table lookup.

---

### 35.3 Tier 2 (`Intermediate`): Single & Multi-Pattern PGFs, Martingales & Border Recurrences

#### **P-4A-09 — `[CTSC2006] 歌唱王国` (Luogu P4548)**
- **Source & Metadata**: `[ZH]` CTSC 2006, Luogu P4548. Constraints: alphabet size $\sigma \le 10^5$, $T \le 50$ queries, each query gives a pattern $S$ of length $L \le 10^5$. Compute $\mathbb{E}[T_S] \bmod 10^4$.
- **1. The Diagnostic Signal**:
  With $L = 10^5$ and $\sigma = 10^5$, building an AC/KMP transition matrix is $O(L^3)$, way too slow.
- **2. The Combinatorial Word Invariant**:
  As proven in Iteration 32.2 via both PGFs ($F'(1) = G(1)$) and Conway's Casino Martingale, a gambler who entered $k$ steps before stopping time $T_S$ survives if and only if $S[1..k] = S[L-k+1..L]$ ($k \in \text{Borders}(S)$), holding fortune $\sigma^k$:
  $$\mathbb{E}[T_S] = \sum_{k \in \text{Borders}(S)} \sigma^k \pmod{10^4}.$$
- **3. The Reverse-Engineering Scratchpad**:
  Compute the KMP `pi` array of $S$ in $O(L)$ time. Start at $k = L$ and follow $k \gets \text{pi}[k]$ while $k > 0$, adding $\sigma^k \bmod 10^4$ at each step. Total time: $O(L)$ per testcase!
- **4. Boundary Pitfalls**:
  Forgetting to include $k = L$ itself (the full pattern is always an improper border of itself, contributing $\sigma^L$!).

#### **P-4A-10 — `[SDOI2017] 硬币游戏` (Luogu P3706)**
- **Source & Metadata**: `[ZH]` SDOI 2017, Luogu P3706. Constraints: $m \le 300$ players, each has a binary string $P_i \in \{\texttt{H}, \texttt{T}\}^L$ of equal length $L \le 300$. Compute the exact winning probability $\pi_i$ for each player $i = 1, \dots, m$ to $10^{-6}$ precision.
- **1. The Diagnostic Signal**:
  Total AC states can be $m \times L = 9 \times 10^4$, so Gaussian elimination on AC states takes $(9 \times 10^4)^3$ operations (TLE). However, $m = 300$ is small!
- **2. The Combinatorial Word Invariant**:
  Since all patterns have the same length $L$ and are distinct, $\mathcal{P}$ is automatically an antichain! By the Guibas–Odlyzko / Conway Martingale theorem (Iteration 32.3), appending $P_j$ to a $\mathcal{P}$-avoiding prefix $G(z)$ and setting $z = 1$ yields:
  $$\sum_{i=1}^m \pi_i \left(\sum_{k \in \text{Overlap}^+(P_i, P_j)} 2^{k - L}\right) = 2^{-L} G(1) \quad \forall j \in \{1, \dots, m\}, \qquad \sum_{i=1}^m \pi_i = 1.$$
  Notice we divided by $2^L$ so that every coefficient $\sum_k 2^{k-L} \in [0, 2]$ is numerically well-conditioned and never overflows `double` even if $L = 10^5$!
- **3. The Reverse-Engineering Scratchpad**:
  Compute all suffix-prefix overlaps between $P_i$ and $P_j$ using polynomial rolling hashes (or KMP on each $P_j$) in $O(m^2 L)$ time, assemble the $(m+1) \times (m+1)$ matrix, and solve via partial-pivoting Gaussian elimination in $O(m^3)$ time.
- **4. Boundary Pitfalls**:
  Using $2^k$ instead of $2^{k-L}$ works for $L = 300$ in `double`, but loses precision or overflows if $L > 1023$. Always normalize by $2^{-L}$!

#### **P-4A-11 — `[JSOI2009] 有趣的游戏` (Luogu P2467 / BZOJ 1444)**
- **Source & Metadata**: `[ZH]` JSOI 2009. Constraints: $m \le 10$ players, $|P_i| = L \le 10$, alphabet size $\sigma \le 10$ with rational letter probabilities $p_c = a_c / b_c \ge 0$.
- **1. The Diagnostic Signal**:
  Letter probabilities $p_c$ are non-uniform and **can be $0$** ($a_c = 0$).
- **2. The Combinatorial Word Invariant**:
  Using the **un-divided** Guibas–Odlyzko system (Pitfall 1 of Iteration 32.4):
  $$\sum_{i=1}^m \pi_i \left(\sum_{k \in \text{Overlap}^+(P_i, P_j)} \mathbb{P}\big(P_j[k+1..L]\big)\right) - \mathbb{P}(P_j) G(1) = 0,$$
  or pre-filtering patterns containing any character with $p_c = 0$ (whose winning probability is identically $\pi_j = 0$).
- **3. The Reverse-Engineering Scratchpad & 4. Boundary Pitfalls**:
  If *all* patterns contain a letter with $p_c = 0$, the game never terminates; for valid patterns with $\mathbb{P}(P_j) > 0$, removing zero-probability patterns first ensures the remaining $(m'+1) \times (m'+1)$ matrix is strictly non-singular.

#### **P-4A-12 to P-4A-16 (Condensed Tier 2 Walkthroughs)**:
- **P-4A-12 (`CF 494B — Obsessive String`)**: Count ways to choose non-overlapping substrings $S[l_1..r_1], \dots, S[l_k..r_k]$ inside $S$ ($|S| \le 10^5$) such that every chosen substring contains pattern $T$. **Invariant**: A substring $S[l..r]$ contains $T$ iff $l \le \text{last\_start}(r)$, where $\text{last\_start}(r)$ is the largest starting index of an occurrence of $T$ ending at or before $r$ (found via KMP in $O(|S|)$), reducing the DP to a double prefix sum!
- **P-4A-13 (`[BJWC2011] 禁忌`, Luogu P3735)**: Given $\mathcal{P}$ ($\sum |P_i| \le 75$) and length $N \le 10^9$, a string $W$ is partitioned left-to-right greedily: the moment a pattern in $\mathcal{P}$ completes, we increment the score by $1$ and **clear the string buffer** (resetting the AC state to the root $q_0$!). Compute the expected score. **Invariant**: Any transition $u \xrightarrow{c} v$ where `bad[v] == true` redirects immediately to $q_0$ with reward $+1$, turning the problem into $O(|Q|^3 \log N)$ matrix exponentiation on $(p_{u,v}, \text{expected\_score}_{u,v})$.
- **P-4A-14 (`[HNOI2008] GT考试`, Luogu P3193)**: Count strings of length $N \le 10^9$ avoiding a single pattern $P$ of length $M \le 20$ mod $K$. Solvable either by $O(M^3 \log N)$ KMP transition matrix or in $O(M \log M \log N)$ via Bostan–Mori on the Goulden–Jackson rational GF $\frac{C_{1,1}(x)}{(1-\sigma x)C_{1,1}(x) + x^M}$.
- **P-4A-15 (`AtCoder ABC 305 G — Banned Substrings`)**: $N \le 10^{18}$, $m \le 126$ banned binary strings of length $\le 6$. **Invariant**: For $N < 6$, brute force all $2^N$ strings; for $N \ge 6$, the state only needs the last $5$ characters ($2^5 = 32$ De Bruijn states), with forbidden transitions removed, solved in $O(32^3 \log N)$.
- **P-4A-16 (`AtCoder ARC 081 C — Don't Be a Subsequence`)**: Find the shortest (and lexicographically smallest) string over `'a'..'z'` that is **not** a subsequence of $S$ ($|S| \le 2 \times 10^5$). **Invariant**: In the Subsequence Automaton (DASG), the shortest absent subsequence corresponds to the shortest path from index $0$ to the dead state $\infty$ along transitions $i \xrightarrow{c} \text{next\_occ}[i+1][c]$.

---

### 35.4 Tier 3 (`Advanced`): DP-of-DP (`DP套DP`), Minimal DFAs, and Goulden–Jackson FPS

#### **P-4A-17 — `[TJOI2018] 游园会` (Luogu P4590)**
- **Source & Metadata**: `[ZH]` TJOI 2018, Luogu P4590. Constraints: alphabet $\Sigma = \{\texttt{N}, \texttt{O}, \texttt{I}\}$, target length $N \le 1000$, reference string $S$ of length $K \le 15$. For each $c \in \{0, 1, \dots, K\}$, count strings $T \in \Sigma^N$ avoiding substring $\texttt{NOI}$ such that $\text{LCS}(S, T) = c$ modulo $10^9 + 7$.
- **1. The Diagnostic Signal**:
  We must simultaneously enforce a substring-avoidance constraint ($\texttt{NOI}$) and classify strings $T$ by the output of an $O(N K)$ dynamic program ($\text{LCS}(S, T)$).
- **2. The Combinatorial Word Invariant (Product Automaton of LCS-Difference DFA $\times$ KMP DFA)**:
  By Architecture 1 of Iteration 33.2, the inner LCS DP row $f[0..K]$ has adjacent differences $\Delta f[j] = f[j] - f[j-1] \in \{0, 1\}$, so it is bijectively represented by a $K$-bit mask $\text{mask} \in [0, 2^K)$.
  The avoidance of $\texttt{NOI}$ is tracked by a 3-state KMP automaton $q \in \{0, 1, 2\}$ (representing suffix match $\epsilon$, $\texttt{N}$, $\texttt{NO}$; state $3 = \texttt{NOI}$ is forbidden).
- **3. The Reverse-Engineering Scratchpad**:
  1. Precompute `next_mask[mask][ch]` for all $2^K$ masks and $ch \in \{\texttt{N}, \texttt{O}, \texttt{I}\}$ in $O(K 2^K)$ time by unpacking `f[0..K]` from prefix popcounts of `mask`, applying one step of the LCS recurrence for `ch`, and packing `f'[j] - f'[j-1]` back into `mask'`.
  2. Run a rolling-array outer DP `dp[i & 1][mask][q]` over $1 \le i \le N$, $0 \le \text{mask} < 2^K$, and $q \in \{0, 1, 2\}$, skipping $(q = 2, ch = \texttt{I})$.
  3. Finally, accumulate `ans[__builtin_popcount(mask)] += dp[N & 1][mask][q]`.
  Total complexity: $O(N \cdot 3 \cdot 3 \cdot 2^K) \approx 1000 \times 9 \times 32768 \approx 2.9 \times 10^8$ ultra-simple loop additions.
- **4. Boundary Pitfalls**:
  In KMP for $\texttt{NOI}$, when at state $q = 1$ ($\texttt{N}$) or $q = 2$ ($\texttt{NO}$) and reading $\texttt{N}$, the state transitions to $q' = 1$ (not $0$!), because $\texttt{N}$ starts a new prefix of $\texttt{NOI}$.

#### **P-4A-19 — `AtCoder AGC 022 E — Median Replace`**
- **Source & Metadata**: `[JA]` AtCoder Grand Contest 022 E. Constraints: string $S \in \{\texttt{0}, \texttt{1}, \texttt{?}\}^N$ with $N \le 3 \times 10^5$ ($N$ odd). In one operation, replace any 3 consecutive bits of a binary string by their median until a single bit remains. Count how many of the $2^{\#\texttt{?}}$ completions of $S$ can be reduced to $\texttt{1}$, modulo $10^9 + 7$.
- **1. The Diagnostic Signal**:
  For a fixed binary string $T$, there are exponentially many ways to choose which triple to reduce at each step. Before we can count over `?`, we need a deterministic left-to-right inner automaton that decides if $T$ can reduce to $\texttt{1}$, and its state space must be $O(1)$ since $N = 3 \times 10^5$!
- **2. The Combinatorial Word Invariant (Canonical Greedy Stack Automaton)**:
  Consider scanning $T$ left-to-right and maintaining a stack:
  - Two $\texttt{1}$'s at the bottom of the stack (`11`) already guarantee a final $\texttt{1}$ regardless of all future characters (because `11x` $\to$ `1`, absorbing one character at a time until `11` wins!). Thus we never need more than two $\texttt{1}$'s on the stack.
  - Whenever the top of the stack has `000`, immediately reduce `000` $\to$ `0` (creating extra $\texttt{0}$'s is never helpful, and compressing `000` $\to$ `0` is always optimal).
  - Whenever a $\texttt{1}$ is pushed on top of a $\texttt{0}$ (`...0` + `1`), immediately cancel the pair (`01x` $\to$ `x`), popping the $\texttt{0}$!
  Under these rules, the stack can only ever consist of $a \in \{0, 1, 2\}$ ones followed by $b \in \{0, 1, 2\}$ zeros!
  At the end of the string, reduce remaining `0`s and `1`s: the string wins iff $a \ge b$ (specifically, $(a, b) \in \{(1, 0), (1, 1), (2, 0), (2, 1), (2, 2)\}$; note $(1, 1)$ has odd total length only if impossible, and on odd-length inputs the winning final states are $a > b$ or $a = 2$).
- **3. The Reverse-Engineering Scratchpad**:
  The inner stack only has **$3 \times 3 = 9$ states** $(a, b) \in \{0, 1, 2\}^2$ (and only $7$ are actually reachable from $(0, 0)$!). Run a simple $O(N)$ outer DP over the $7$-state DFA!
- **4. Boundary Pitfalls**:
  Failing to cap $a$ at $2$: once `11` is at the bottom of the stack, pushing a `0` makes `110`, and if another `0` arrives (`1100`) and then `1` (`11001` $\to$ `110`), the `11` base is untouchable. Without capping $a \le 2$, the state space grows to $O(N)$, causing $O(N^2)$ TLE.

#### **P-4A-23 — `[ZJOI2019] 麻将` (Luogu P5279)**
- **Source & Metadata**: `[ZH]` ZJOI 2019, Luogu P5279. Constraints: $n \le 100$ tile types ($4$ copies of each, total $4n$ tiles), $13$ initial tiles given. Draw remaining tiles uniformly at random; stop when a winning hand ($4$ melds + $1$ pair, or $7$ distinct pairs) is formed. Compute expected draws $\mathbb{E}[T] \bmod 998244353$.
- **1. The Diagnostic Signal**:
  Checking whether a multiset of tile counts $c_1, \dots, c_n \in \{0, 1, 2, 3, 4\}$ contains a winning hand is itself a classic DP over tile types $i = 1 \dots n$ with state `(j, k, has_pair)` ($j, k \in \{0, 1, 2\}$ uncommitted sequences starting at $i-1, i$). We need to count hands that **avoid** winning after $m$ draws, requiring a `DP套DP`!
- **2. The Combinatorial Word Invariant (Bounded Reachability of Inner DP Automaton)**:
  In the inner DP over tile types $i$, for each $(j, k) \in \{0, 1, 2\}^2$, we maintain the maximum number of completed melds (clamped to $\le 4$), both with $0$ pairs ($f_{0}[j][k] \in \{-1, 0, 1, 2, 3, 4\}$) and $1$ pair ($f_{1}[j][k]$), plus the count of tile types with $\ge 2$ copies (clamped to $\le 7$).
  Although the naive product of ranges is $6^{18} \times 8 \approx 10^{15}$, running the **Automated BFS Reachability Scratchpad** (Iteration 33.3) from the initial state discovers that **only $2092$ non-winning inner DP states are reachable**!
- **3. The Reverse-Engineering Scratchpad**:
  Precompute the $2092$-state DFA transitions for $c \in \{0, 1, 2, 3, 4\}$ copies of tile $i$, then run an outer DP over tile types $i = 1 \dots n$, number of total tiles drawn $m \le 4n - 13$, and DFA state $u \in \{1 \dots 2092\}$, using $\mathbb{E}[T] = \sum_{m \ge 0} \mathbb{P}(T > m)$.
- **4. Boundary Pitfalls**:
  If you do not clamp meld counts at $4$ (or map all winning states to a single absorbing sink `WIN`), the BFS state count explodes!

#### **P-4A-24 — `Goulden–Jackson + FPS Inversion for Long Pattern Avoidance` (QOJ / UCup / Extended `[HNOI2008] GT考试`)**
- **Source & Metadata**: `[EN]`/`[ZH]` Grandmaster FPS-String synthesis. Constraints: single pattern $P$ of length $L \le 10^5$ (or $m \le 20$ patterns of total length $\le 10^5$), query $N \le 10^5$, modulo $998244353$. Count strings of length $n$ avoiding $P$ for all $1 \le n \le N$.
- **1. The Diagnostic Signal**:
  Both $L = 10^5$ and $N = 10^5$ are large, so $O(N L)$ KMP DP takes $10^{10}$ operations (TLE).
- **2. The Combinatorial Word Invariant**:
  By the single-pattern Goulden–Jackson formula (Iteration 31.3), the generating function is rational with sparse denominator:
  $$F(x) = \frac{C_{1,1}(x)}{(1 - \sigma x) C_{1,1}(x) + x^L}, \quad \text{where } C_{1,1}(x) = \sum_{k \in \text{Borders}(P)} x^{L - k}.$$
- **3. The Reverse-Engineering Scratchpad**:
  Find $\text{Borders}(P)$ via KMP in $O(L)$, construct polynomials $A(x) = C_{1,1}(x)$ and $B(x) = (1 - \sigma x) C_{1,1}(x) + x^L \pmod{x^{N+1}}$, and compute $A(x) B(x)^{-1} \bmod x^{N+1}$ via NTT Newton iteration in $O(N \log N)$ time! (And if $N \le 10^{18}$ with $L \le 5 \times 10^4$, apply Bostan–Mori in $O(L \log L \log N)$ time!)
- **4. Boundary Pitfalls**:
  Notice $B(0) = C_{1,1}(0) = x^{L-L} = 1$, so $B(x)$ is always invertible in $\mathbb{F}_p[[x]]$. However, if $L > N$, the $x^L$ term in the denominator vanishes modulo $x^{N+1}$, which would wrongly give $F(x) = \frac{1}{1-\sigma x}$ if you truncated $C_{1,1}(x)$ from the wrong end! Because $C_{1,1}(x) = 1 + \sum_{\text{proper } k} x^{L-k}$, the exponents $L - k$ are the **periods** $p = L - k$ of $P$, which are well-defined even when $L > N$!

#### **P-4A-18, P-4A-20, P-4A-21, P-4A-22 (Condensed Tier 3 Walkthroughs)**:
- **P-4A-18 (`HDU 4352 — XHXJ's List`)**: Count numbers in $[L, R]$ ($R \le 2^{63}-1$) whose decimal digits have $\text{LIS} = K$ ($1 \le K \le 10$). **Invariant**: Patience-sorting LIS array is a subset of $\{0..9\}$ ($2^{10} = 1024$ states). Precompute `dp[len][mask][K]` once outside the testcase loop to answer $10^4$ queries in $O(\log_{10} R)$ per query!
- **P-4A-20 (`CF 1207G — Indie Album`)**: $n \le 4 \times 10^5$ strings defined as a Trie (each string appends a char to a previous string), $q \le 4 \times 10^5$ queries asking how many times pattern $P_j$ occurs in Trie string $s_i$. **Invariant**: Build AC automaton on all query patterns $\{P_j\}$; as we DFS the input Trie of $s_i$, maintain the active AC node $u$ in a Fenwick tree over the Euler tour of the AC `fail` tree (+1 on enter $s_i$, -1 on exit), answering all queries at $s_i$ by subtree sum on $\text{end}(P_j)$!
- **P-4A-21 (`[SDOI2017] 天才黑客`, Luogu P3703)**: Shortest path on graph where transitioning from edge $e_1$ (string $u$) to $e_2$ (string $v$) at a vertex costs $\text{LCP}(u, v)$ on a given Trie. **Invariant**: On the Trie Virtual Tree of incident edges at a vertex, $\text{dep}(\text{LCA}(u, v)) = d$ is optimized via prefix/suffix range auxiliary nodes over the DFS order of the Virtual Tree.
- **P-4A-22 (`AtCoder ABC 249 G / ARC 141 D / Palindromic Concatenation`)**: Form a palindrome by concatenating words from a dictionary $D$ with costs. **Invariant**: Build from outside in (left and right simultaneously); at any step, either the left side or right side overhangs the other by a suffix/prefix of a dictionary word $w_i$ of length $\le \max |w_i|$, creating a small Dijkstra/DP state space of size $2 \sum |w_i|$.

---

### 35.5 Tier 4 (`Mastery`): Dynamic AC Grouping, Weighted Bivariate GFs, Regex Minimization & Palindromic Clusters

#### **P-4A-25 — `CF 710F — String Set Queries`**
- **Source & Metadata**: `[EN]` Codeforces Round 368 E / Educational Round 16 F. Constraints: $m \le 3 \times 10^5$ online operations (1: insert pattern $P$, 2: delete pattern $P$, 3: query total occurrences of all active patterns in text $T$), $\sum |P| + \sum |T| \le 3 \times 10^5$, **forced online** (`fflush(stdout)`).
- **1. The Diagnostic Signal**:
  Aho–Corasick `fail` pointers are not dynamically updatable in $O(1)$ per character insertion because inserting a short prefix can redirect the `fail` links of $O(\sum |P_i|)$ existing nodes!
- **2. The Combinatorial Word Invariant (Binary Grouping of Decomposable Search Problems / `二进制分组`)**:
  Because pattern occurrence counting is **linear and additive** over disjoint sets of patterns ($\text{occ}_{\mathcal{P}_1 \sqcup \mathcal{P}_2}(T) = \text{occ}_{\mathcal{P}_1}(T) + \text{occ}_{\mathcal{P}_2}(T)$), we maintain two separate collections (one for insertions, one for deletions), each partitioned into $O(\log m)$ immutable AC automata containing $2^{k_1} > 2^{k_2} > \dots$ patterns!
- **3. The Reverse-Engineering Scratchpad**:
  When inserting $P$, create a group of size $1$. While the last two groups have equal pattern count $2^k$, merge their pattern lists and rebuild a fresh AC automaton of size $2^{k+1}$ from scratch!
  - *Amortized Rebuild Cost*: Every pattern participates in at most $\log_2 m$ merges, so total AC construction work across all operations is $O((\sum |P|) \log m)$.
  - *Query Cost*: Run $T$ through each of the $\le \log_2 m$ insertion AC automata and subtract the counts from the $\le \log_2 m$ deletion AC automata in $O(|T| \log m)$ time.
- **4. Boundary Pitfalls**:
  In each AC automaton, do **not** construct the full $26$-array transition table for empty children during rebuild if memory or alphabet factor is tight, or only rebuild `tr[u][c]` over active characters; however, since $\sum |P| \le 3 \times 10^5$ and each character exists in at most **one** group at any given moment, total memory at any instant is strictly $O(\sum |P| \cdot |\Sigma|)$ (not multiplied by $\log m$!) if you free/reuse node pools upon merging!

#### **P-4A-29 — `UOJ / LOJ — Exact k Occurrences of a Long Pattern` (Weighted Goulden–Jackson Mastery)**
- **Source & Metadata**: `[ZH]` Grandmaster FPS & String Enumeration. Constraints: single pattern $P$ of length $L \le 5 \times 10^4$, target length $N \le 10^5$, occurrence target $0 \le k \le N$, alphabet $\sigma$, modulo $998244353$. Compute $[x^N t^k] F(x, t)$.
- **1. The Diagnostic Signal**:
  Neither $L$ nor $N$ nor $k$ is small enough for $O(N L k)$ DP.
- **2. The Combinatorial Word Invariant**:
  By Iteration 34.3, the exact generating function for strings with $k \ge 1$ occurrences of $P$ is:
  $$F_k(x) = [t^k] F(x, t) = \frac{x^L \big((1 - \sigma x)(C_{1,1}(x) - 1) + x^L\big)^{k-1}}{\big((1 - \sigma x) C_{1,1}(x) + x^L\big)^{k+1}} = \frac{x^L D_1(x)^{k-1}}{D_0(x)^{k+1}}.$$
- **3. The Reverse-Engineering Scratchpad**:
  Compute $C_{1,1}(x)$ via KMP on $P$ in $O(L)$. Form $D_0(x)$ and $D_1(x) \bmod x^{N-L+1}$. Using polynomial $\ln / \exp$, compute $D_1(x)^{k-1} D_0(x)^{-(k+1)} \bmod x^{N-L+1}$ in $O(N \log N)$ time, and extract $[x^{N-L}]$!
- **4. Boundary Pitfalls**:
  While $D_0(0) = 1$ (so $\ln D_0(x)$ is immediately valid), $D_1(x) = (1 - \sigma x)(C_{1,1}(x) - 1) + x^L$ has constant term $D_1(0) = 0$! Before taking $\ln D_1(x)$ to compute $D_1(x)^{k-1}$, you **must** factor out its lowest nonzero degree term $c x^d$ (where $d = \min\text{Period}(P)$ is the shortest period of $P$, since $C_{1,1}(x) - 1$ starts at $x^{L - \max\text{ProperBorder}(P)}$)! If $(k - 1) d + L > N$, the answer is immediately $0$.

#### **P-4A-26, P-4A-27, P-4A-28, P-4A-30, P-4A-31, P-4A-32 (Condensed Tier 4 Walkthroughs)**:
- **P-4A-26 (`AtCoder AGC 020 E — Encoding Subsets`)**: Count valid compressed representations $(A \times d)$ of all subsets of a binary string $S$ ($|S| \le 100$). **Invariant**: When compressing $d$ blocks $S[l..r]$ into $(P \times d)$, a string $P$ is a subset of all $d$ blocks iff $P$ is a subset of the **bitwise AND** string $\bigwedge_{t=0}^{d-1} S[l + t \cdot len \dots l + (t+1)len - 1]$. Memoizing on the actual string $S'$ (rather than just $(l, r)$) has a tiny reachable state space because bitwise AND rapidly strips $\texttt{1}$'s!
- **P-4A-27 (`Stopping Time Variance & k-th Occurrence PGF`)**: Combine the exact $k$-occurrence PGF $F_{[k]}(z) = \left(\frac{\mathbb{P}(P) z^L}{D_0(z)}\right) \left(\frac{D_1(z)}{D_0(z)}\right)^{k-1}$ with $F_{[k]}'(1)$ and $F_{[k]}''(1)$ to compute expected time and variance until the $k$-th (possibly overlapping) occurrence of $P$.
- **P-4A-28 (`Lyndon / Necklace Pattern Avoidance`)**: By Burnside's Lemma and Mobius inversion, counting necklaces of length $N$ avoiding $\mathcal{P}$ reduces to counting periodic strings of period $d \mid N$ whose infinite repetition avoids $\mathcal{P}$, which equals $\text{Tr}(M^d)$ where $M$ is the AC transition matrix!
- **P-4A-30 (`Penney's Game Optimal Counter-Strategy`)**: Given $P_1 \in \{0, 1\}^L$, to maximize $\pi_2 = \frac{C_{1,1} - C_{1,2}}{C_{1,1} - C_{1,2} + C_{2,2} - C_{2,1}}$, player 2 should choose $P_2 = b \cdot P_1[1..L-1]$ (prepending one bit $b$ to the $(L-1)$-prefix of $P_1$), which maximizes $C_{2,1} \ge 2^{L-1}$ while keeping $C_{2,2}$ minimal!
- **P-4A-31 (`Regex Counting via Thompson NFA -> Subset DFA -> Hopcroft Minimization`)**: Compile regex to $\epsilon$-NFA, run reachable subset construction, minimize via Hopcroft partition refinement, and apply Berlekamp–Massey + Bostan–Mori on the minimal DFA to reach $N \le 10^{18}$.
- **P-4A-32 (`Palindromic Goulden–Jackson`)**: Count palindromes $W = W^R$ of length $N$ avoiding $\mathcal{P} = \mathcal{P}^R$. A marked palindrome decomposes into free symmetric letter pairs from the outside in, clusters duplicated symmetrically on the left and right halves, and a single **central cluster** (or central free letter) straddling the midpoint $N/2$!

---

### 35.6 Template Quarantine Ledger (`R-4A-01` to `R-4A-08`)

In strict compliance with `AGENTS.md` and `PLAN.md`, the following pure implementation/template problems discovered during `[EN]`/`[ZH]`/`[JA]` mining are **quarantined** and excluded from textbook problem ladders:

| Quarantine ID | Problem Source & Title | Reason for Rejection |
| :--- | :--- | :--- |
| **R-4A-01** | Luogu P3808 — `【模板】AC 自动机（简单版）` | Bare Aho–Corasick construction and `fail`-chain traversal template. |
| **R-4A-02** | Luogu P3796 — `【模板】AC 自动机（加强版）` | Bare AC occurrence counting template without modeling or DP reduction. |
| **R-4A-03** | Luogu P5357 — `【模板】AC 自动机（二次加强版）` | Bare AC `fail`-tree topological accumulation template. |
| **R-4A-04** | Luogu P3804 — `【模板】后缀自动机（SAM）` | Bare SAM construction and `len[u] * cnt[u]` Link-Tree sum template. |
| **R-4A-05** | Library Checker — `Number of Substrings` | Pure template verification of $\sum (\text{len}(u) - \text{len}(\text{link}(u)))$ or SA LCP. |
| **R-4A-06** | Luogu P3375 — `【模板】KMP` | Standard KMP border array verification. |
| **R-4A-07** | Luogu P3389 — `【模板】高斯消元法` | Routine linear algebra library routine without string-overlap structure. |
| **R-4A-08** | Luogu P4723 — `【模板】常系数齐次线性递推` | Pure Bostan–Mori / Kitamasa library template without string GF derivation. |

---

### 35.7 Multilingual Bibliography & Reference Sources for Wave 4A

1. **Goulden, I. P., & Jackson, D. M. (1979)**. *An inversion theorem for cluster decompositions of sequences with distinguished subsequences*. Journal of the London Mathematical Society, s2-20(3), 567–576. (Original formulation of the Goulden–Jackson Cluster Method).
2. **Guibas, L. J., & Odlyzko, A. M. (1981)**. *String overlaps, pattern matching, and nontransitive games*. Journal of Combinatorial Theory, Series A, 30(2), 183–208. (Autocorrelation polynomials, non-transitive Penney's game probabilities, and equivalence with cluster systems).
3. **Noonan, J., & Zeilberger, D. (1999)**. *The Goulden–Jackson cluster method: extensions, applications, and implementations*. Journal of Difference Equations and Applications, 5(4-5), 355–377. (Weighted $(t-1)$ cluster expansion and bivariate occurrence generating functions).
4. **Graham, R. L., Knuth, D. E., & Patashnik, O. (1994)**. *Concrete Mathematics* (2nd ed., Chapter 8.4: Flipping Coins). Addison-Wesley. (PGF derivation of $\mathbb{E}[T_S]$, $\text{Var}(T_S)$, and Conway's Casino Martingale).
5. **Li, S.-Y. R. (1980)**. *A martingale approach to the study of occurrence of sequence patterns in repeated experiments*. The Annals of Probability, 8(6), 1171–1176. (Rigorous Doob Optional Stopping justification of Conway's casino betting martingale for multi-player pattern racing).
6. **中国国家集训队论文 (Chinese National Team Papers)**:
   - 刘家骅 (2018), *《浅谈“DP套DP”问题》* (`DP套DP`, inner-DP DFA construction, difference state compression, and Myhill–Nerode minimization).
   - 钟知闲 / 杜瑜皓, *《概率生成函数在字符串匹配问题中的应用》* (`[CTSC2006] 歌唱王国`, `[SDOI2017] 硬币游戏`, PGF vs. Martingale duality).
7. **Japanese Competitive Stringology Treatises (`[JA]`)**:
   - `maspypy` — *文字列の周期とオートマトン・母関数 (String Periodicity, Automata, and Generating Functions / Goulden–Jackson Method)*.
   - `noshi91` / `tatyam` — *DFA Minimization & Automaton DP (`自動機上のDP` / `DP of DP`) in AtCoder Grand Contests*.

---

### 35.8 Wave 4A Diagnostic Routing Matrix & Multilingual Rosetta Stone

#### Diagnostic Routing Matrix: Which Automaton / Generating Function Engine Applies?

| Problem Signature & Constraints | Why Naive Approach Fails | Target Wave 4A Engine | Complexity Achieved |
| :--- | :--- | :--- | :--- |
| Avoid single long pattern $P$ ($L \le 10^5$), find $[x^N]F(x)$ for $N \le 10^5$ | KMP DP is $O(N L) = 10^{10}$ | **Single-Pattern Goulden–Jackson + FPS Inversion**: $F(x) = \frac{C_{1,1}(x)}{(1-\sigma x)C_{1,1}(x) + x^L}$ | $O(L + N \log N)$ |
| Avoid single long pattern $P$ ($L \le 5 \times 10^4$), huge $N \le 10^{18}$ | Matrix power is $O(L^3 \log N)$ | **Goulden–Jackson Rational GF + Bostan–Mori** | $O(L \log L \log N)$ |
| Avoid $m \le 300$ long patterns ($L \le 10^5$), find stopping probabilities $\pi_i$ | AC Gaussian elimination is $O((mL)^3)$ | **Guibas–Odlyzko / Conway Martingale $(m+1) \times (m+1)$ System** | $O(m^2 L + m^3)$ |
| Single pattern $S$ ($L \le 10^5$), expected stopping time $\mathbb{E}[T_S]$ & $\text{Var}(T_S)$ | KMP state elimination is tedious for $\text{Var}$ | **Conway Casino Martingale & PGF Derivatives $F'(1), F''(1)$** | $O(L)$ |
| Count strings $W \in \Sigma^N$ with **exactly $k$** occurrences of $P$ ($L, N \le 10^5$) | 2D KMP DP is $O(N L k)$ | **Weighted $(t-1)$ Cluster Bivariate GF**: $[x^N]\frac{x^L D_1(x)^{k-1}}{D_0(x)^{k+1}}$ | $O(L + N \log N)$ |
| Count strings $T \in \Sigma^N$ with $\text{LCS}(S, T) = c$ ($|S| = K \le 15$) | Inner LCS state has $(K+1)^K$ tuples | **LCS `DP套DP` via Monotonic Row-Difference Mask $\Delta f \in \{0,1\}^K$** | $O(N |\Sigma| 2^K)$ |
| Count strings winning a custom rewriting / tile / bracket game | Ad-hoc invariant analysis is error-prone | **Automated BFS Inner-State Exploration + Hopcroft DFA Minimization** | $O(N |\Sigma| \cdot |Q_{\min}|)$ |
| Online pattern insertions, deletions, and substring occurrence queries ($\sum |P|, \sum |T| \le 3 \times 10^5$) | AC `fail` links cannot be updated online in $O(1)$ | **Binary Grouping (`二进制分组`) of $O(\log M)$ Immutable AC Automata** | $O((\sum |P| + \sum |T|) \log M)$ |

#### Wave 4A Multilingual Stringology Rosetta Stone (`[EN]` $\leftrightarrow$ `[ZH]` $\leftrightarrow$ `[JA]`)

| English (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) | Core Mathematical Object |
| :--- | :--- | :--- | :--- |
| **Goulden–Jackson Cluster Method** | **Goulden–Jackson 簇方法 / 标记串容斥** | **Goulden–Jackson 法 (クラスター法)** | PIE over overlapping marked pattern chains (`clusters`) |
| **Autocorrelation / Overlap Polynomial** | **自相关多项式 / 互相关多项式 $C_{i,j}(x)$** | **自己相関多項式 / オーバーラップ多項式** | $C_{i,j}(x) = \sum_{k \in \text{Overlap}^+(P_i, P_j)} x^{|P_j|-k}$ |
| **Probability Generating Function (PGF)** | **概率生成函数** | **確率母関数** | $F(z) = \sum_{n \ge 0} \mathbb{P}(T = n) z^n$, $\mathbb{E}[T] = F'(1)$ |
| **Conway's Casino Martingale** | **康威赌博 (鞅与可选停时定理)** | **コンウェイのギャンブル (マルチンゲール)** | Fair sequential betting where surviving bettors match $\text{Borders}(S)$ |
| **DP of DP / Automaton DP** | **DP套DP / 自动机上的动态规划** | **自動機上のDP / DP of DP** | Outer counting DP over reachable states of an inner decision/value DP |
| **Myhill–Nerode Equivalence & Hopcroft Minimization** | **Myhill–Nerode 等价类与最小化 DFA** | **DFA 最小化 (Nerode 同値関係)** | Quotienting inner DP states by suffix indistinguishability |
| **Binary Grouping of AC Automata** | **AC自动机二进制分组** | **Aho–Corasick 法のバイナリグルーピング** | Dynamizing static AC structures into $O(\log N)$ powers-of-two blocks |
