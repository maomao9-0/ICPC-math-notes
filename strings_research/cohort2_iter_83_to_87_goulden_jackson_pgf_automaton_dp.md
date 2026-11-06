# Wave 4A (Cohort 2: Iterations 83–87) — Goulden–Jackson Cluster Method, String PGFs / Martingales, Automaton DP & DFA Minimization (`DP套DP`)

> [!IMPORTANT]
> **Cohort 2 Independent Redundant Discovery & Structural Derivation Pass**
> This document is the 100% independent Cohort 2 research report (`strings_research/cohort2_iter_83_to_87_goulden_jackson_pgf_automaton_dp.md`) for **Wave 4A (Iterations 83–87)**. Every theorem, overlap polynomial identity, martingale stopping argument, bivariate cluster sieve, and automaton-over-automaton construction is derived from first principles following the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**, with explicit hand-checkable examples, algebraic invertibility hypotheses, exact index boundaries, failure-mode counterexamples, and a 32-problem multilingual (`[EN]` / `[ZH]` / `[JA]`) 4-Tier Difficulty Ladder plus Quarantine Ledger.

---

## Iteration 83: The Goulden–Jackson Cluster Method & Autocorrelation Linear Systems

### 83.1 The Diagnostic Signal: Why Naive Aho–Corasick Matrix Exponentiation & Naive Inclusion–Exclusion Both Fail

Consider the foundational pattern-avoidance enumeration problem:
- **Concrete Objects Being Counted**: Given an alphabet $\Sigma$ of size $\sigma = |\Sigma|$ and a set of forbidden patterns $\mathcal{P} = \{P_1, P_2, \dots, P_m\} \subset \Sigma^+$, we want to count the number $a_n$ of strings $W \in \Sigma^n$ of length $n$ that contain **no** $P_i \in \mathcal{P}$ as a contiguous substring, or compute the ordinary generating function (OGF)
  $$A(x) = \sum_{n \ge 0} a_n x^n \in \mathbb{Q}[[x]].$$

Why do standard automaton and combinatorial approaches fail when $L = \sum_{i=1}^m |P_i|$ or $n$ is large?
1. **Failure of Direct Aho–Corasick DP / Matrix Exponentiation**:
   - Building the Aho–Corasick (AC) automaton on $\mathcal{P}$ creates $V = O(L)$ states, where $L = \sum_{i=1}^m |P_i|$.
   - If $n \le 10^{18}$ and $L \approx 2000$, matrix exponentiation over the $V \times V$ AC transition matrix costs $O(L^3 \log n)$—completely infeasible!
   - Even if $n \le 10^5$ and we only want $a_n \pmod p$, running the AC DP takes $O(n L \sigma)$ time. Yet frequently in contest problems, $m$ (the number of patterns) is very small ($m \le 15$ or $m = 1$) while individual pattern lengths $|P_i|$ are up to $10^5$, or $m \le 300$ and we want the exact rational generating function $A(x) = P(x)/Q(x)$ to run Bostan–Mori in $O(L \log L \log n)$.
2. **Failure of Naive Inclusion–Exclusion on Occurrences**:
   - Suppose a single pattern $P = \texttt{aba}$ is forbidden. A beginner might try inclusion–exclusion over positions where $P$ occurs: "subtract strings with at least one `aba`, add back strings with at least two `aba`, etc."
   - **Why it breaks**: Two occurrences of $P = \texttt{aba}$ can **overlap**! In the string $W = \texttt{ababa}$ of length $5$, $P$ occurs at `[1..3]` and `[3..5]`. Their union has length $5$, not $2 \times 3 = 6$. The number of free characters depends not just on *how many* occurrences of $P$ we force, but on *how adjacent chosen occurrences overlap*.

---

### 83.2 The Combinatorial Word Invariant: Marked Words, Clusters, and the Overlap Polynomial

To turn overlapping occurrences into an exact algebraic system without tracking character-by-character AC states, the **Goulden–Jackson Cluster Method** changes the set of objects being counted.

#### Step 1: Reduced Pattern Set (Antichain Assumption)
Before writing any equations, we enforce a structural precondition:
- **Antichain Invariant**: No pattern $P_i \in \mathcal{P}$ is a contiguous substring of another pattern $P_j \in \mathcal{P}$ ($i \ne j$).
- Why? If $P_i$ occurs inside $P_j$, any string avoiding $P_i$ automatically avoids $P_j$, so $P_j$ is redundant for avoidance ($w(P_j) = 0$). Wait: in weighted occurrence counting (Iteration 86), if $P_i$ is inside $P_j$, we cannot simply delete $P_j$, which requires a separate modification. For pure avoidance, we first run AC / KMP to remove any $P_j$ that contains some $P_i$ as a substring.

#### Step 2: Double-Counting Marked Words $(W, M)$
For any word $W = w_1 w_2 \dots w_n \in \Sigma^*$, let $\text{Occ}(W)$ be the set of all pairs $(r, i)$ such that $P_i$ occurs in $W$ ending at position $r$ (i.e., $W[r - |P_i| + 1 .. r] = P_i$).
By the Antichain Invariant, at most one pattern $P_i \in \mathcal{P}$ can end at any given index $r$.

Now define a **marked word** as a pair $(W, M)$ where $W \in \Sigma^*$ and $M \subseteq \text{Occ}(W)$ is a subset of actual occurrences of patterns from $\mathcal{P}$ in $W$ that we choose to "highlight" (mark). Assign each marked occurrence weight $-1$, so the weight of $(W, M)$ is $(-1)^{|M|} x^{|W|}$.

Summing over all words $W \in \Sigma^*$ and all subsets $M \subseteq \text{Occ}(W)$ gives our fundamental double count:
$$\sum_{W \in \Sigma^*} \sum_{M \subseteq \text{Occ}(W)} (-1)^{|M|} x^{|W|} = \sum_{W \in \Sigma^*} x^{|W|} \prod_{(r, i) \in \text{Occ}(W)} (1 - 1) = \sum_{\substack{W \in \Sigma^* \\ \text{Occ}(W) = \emptyset}} x^{|W|} = A(x).$$
In words:
- Every word $W$ that contains **zero** occurrences of $\mathcal{P}$ has $\text{Occ}(W) = \emptyset$, so its inner sum has $2^0 = 1$ term ($M = \emptyset$) with weight $+1 \cdot x^{|W|}$.
- Every word $W$ that contains $k \ge 1$ occurrences of $\mathcal{P}$ has $\sum_{M \subseteq \text{Occ}(W)} (-1)^{|M|} = (1 - 1)^k = 0$, so all its marked versions cancel out completely!

#### Step 3: Unique Factorization of Marked Words into Free Letters and Clusters
Now look at a marked word $(W, M)$ from the outside. Each marked occurrence $e = (r, i) \in M$ covers the closed integer interval of character positions $[r - |P_i| + 1, r]$.
- Two marked occurrences **overlap** if their covered character intervals intersect in at least one character position. (Crucially, if one ends at $r$ and the next starts at $r+1$, they are *adjacent/concatenated*, NOT overlapping!)
- Taking the connected components of marked occurrences in $M$ under interval intersection decomposes $(W, M)$ uniquely as a sequence of two kinds of atomic blocks:
  1. **Unmarked single letters** $c \in \Sigma$ (weight $\sigma x$ in total across the alphabet), and
  2. **Clusters** $\mathcal{C}$: maximal connected chains of overlapping marked patterns $P_{i_1}, P_{i_2}, \dots, P_{i_s}$ ($s \ge 1$) ordered by their right endpoints $r_1 < r_2 < \dots < r_s$. Because no pattern is a substring of another, strict right-endpoint order $r_1 < r_2 < \dots < r_s$ is equivalent to strict left-endpoint order $l_1 < l_2 < \dots < l_s$, and by minimality of connected components (after throwing away redundant three-way overlaps, or simply ordering all marked occurrences in the component by endpoint), each consecutive pair $(P_{i_q}, P_{i_{q+1}})$ in the chain overlaps by at least $1$ character and at most $\min(|P_{i_q}|, |P_{i_{q+1}}|) - 1$ characters!

Wait—what if $P_{i_1}$ and $P_{i_3}$ also overlap? Because $l_1 < l_2 < l_3$ and $r_1 < r_2 < r_3$, any character shared by $P_{i_1}$ and $P_{i_3}$ is automatically inside $P_{i_2}$. Thus, a sequence of marked intervals ordered by $r_1 < r_2 < \dots < r_s$ forms a single connected component if and only if **every adjacent pair** $(P_{i_q}, P_{i_{q+1}})$ overlaps in at least one position:
$$r_q \ge r_{q+1} - |P_{i_{q+1}}| + 1 \iff 1 \le |P_{i_{q+1}}| - (r_{q+1} - r_q) < \min(|P_{i_q}|, |P_{i_{q+1}}|).$$

Therefore, by the Symbolic Method (`SEQ` construction), any marked word $(W, M)$ is uniquely a sequence of single unmarked letters and clusters:
$$A(x) = \frac{1}{1 - \sigma x - \text{Clust}(x)}, \qquad \text{where } \text{Clust}(x) = \sum_{i=1}^m C_i(x),$$
and $C_i(x)$ is the generating function of all clusters whose **last** (rightmost) marked pattern is $P_i$.

---

### 83.3 The Reverse-Engineering Scratchpad: Deriving the $m \times m$ Autocorrelation System

Let us decompose a cluster ending with $P_j$ according to whether $P_j$ is the only marked pattern in the cluster, or whether it extends a smaller cluster ending with some $P_i$:
1. **Base case**: The cluster consists of the single marked pattern $P_j$ alone. Its weight is $(-1)^1 x^{|P_j|} = -x^{|P_j|}$.
2. **Inductive extension**: The cluster is formed by taking a valid cluster ending with $P_i$ and overlapping $P_j$ onto the right end of $P_i$ so that their overlap has length $k \in \{1, 2, \dots, \min(|P_i|, |P_j|) - 1\}$.
   - When can $P_j$ overlap the right end of $P_i$ by $k$ characters? Exactly when the **suffix of $P_i$ of length $k$** equals the **prefix of $P_j$ of length $k$**!
   - How many new characters does $P_j$ append to the cluster beyond the end of $P_i$? Exactly $|P_j| - k$ characters, and adding $P_j$ to the marked set $M$ multiplies the sign by $-1$.

Let us define the **Overlap Set** and **Cross-Correlation (Overlap) Polynomial**:
$$\text{Overlap}(P_i, P_j) = \bigl\{\, k \in \{1, 2, \dots, \min(|P_i|, |P_j|)\} : P_i[|P_i|-k+1 .. |P_i|] = P_j[1..k] \,\bigr\}.$$
Notice that for $i = j$, $k = |P_i|$ is the full match of $P_i$ with itself, while for $i \ne j$, the Antichain Invariant guarantees $k < \min(|P_i|, |P_j|)$.
If we define the **Cross-Correlation Polynomial** (including the $k = |P_i|$ term when $i = j$):
$$C_{i,j}(x) = \sum_{k \in \text{Overlap}(P_i, P_j)} x^{|P_j| - k},$$
then separating the $k = |P_j|$ self-overlap term ($x^0 = 1$ when $i = j$) from proper overlaps ($k < |P_j|$, denoted $\widetilde{C}_{i,j}(x)$) yields:
$$C_j(x) = -x^{|P_j|} - \sum_{i=1}^m C_i(x) \widetilde{C}_{i,j}(x) \iff C_j(x) + \sum_{i=1}^m C_i(x) \widetilde{C}_{i,j}(x) = -x^{|P_j|}.$$
Since $1 + \widetilde{C}_{j,j}(x) = C_{j,j}(x)$ and $\widetilde{C}_{i,j}(x) = C_{i,j}(x)$ for $i \ne j$, this collapses into the remarkably clean **$m \times m$ Goulden–Jackson Linear System**:
$$\sum_{i=1}^m C_i(x) C_{i,j}(x) = -x^{|P_j|} \qquad \text{for all } j = 1, \dots, m.$$

> [!IMPORTANT]
> **Local Algebraic Hypotheses & Ring Invertibility**
> - Over the formal power series ring $R[[x]]$ (where $R = \mathbb{Q}$ or $\mathbb{F}_p$), $C_{j,j}(0) = 1$ (from $k = |P_j|$) and $C_{i,j}(0) = 0$ for $i \ne j$ (since no two distinct patterns are substrings of each other, $|P_j| - k \ge 1$).
> - Therefore, at $x = 0$, the matrix $\mathbf{C}(x) = [C_{i,j}(x)]_{1 \le i,j \le m}$ satisfies $\mathbf{C}(0) = I_m$.
> - Because $\det \mathbf{C}(0) = 1$ is a unit in any commutative ring $R$, $\det \mathbf{C}(x) \in 1 + x R[x]$ is **always a unit in $R[[x]]$**, regardless of the characteristic of $R$! Similarly, $1 - \sigma x - \sum_{i=1}^m C_i(x)$ has constant term $1$, so it is always invertible in $R[[x]]$.

#### Special Case $m = 1$ (Single Pattern $P$ with Autocorrelation Polynomial $C_P(x)$)
When $\mathcal{P} = \{P\}$ has a single pattern of length $L = |P|$, the $1 \times 1$ system gives $C_1(x) C_{P,P}(x) = -x^L$, where
$$C_P(x) = C_{P,P}(x) = \sum_{k \in \text{Borders}(P)} x^{L - k} = 1 + \sum_{\substack{k \in \text{Borders}(P) \\ 1 \le k < L}} x^{L - k}$$
(using the convention that $L \in \text{Borders}(P)$ gives $x^0 = 1$). Substituting $C_1(x) = -x^L / C_P(x)$ into $A(x) = (1 - \sigma x - C_1(x))^{-1}$ yields the famous **Guibas–Odlyzko Single-Pattern Avoidance Formula**:
$$A(x) = \frac{1}{1 - \sigma x + \dfrac{x^L}{C_P(x)}} = \frac{C_P(x)}{(1 - \sigma x) C_P(x) + x^L}.$$

---

### 83.4 Small Hand-Checkable Example: $P = \texttt{aba}$ vs. $P = \texttt{aaa}$ over $\Sigma = \{\texttt{a}, \texttt{b}\}$ ($\sigma = 2$)

Let us hand-check $n = 3$ and $n = 4$ for two patterns of length $L = 3$ over a binary alphabet ($\sigma = 2$):
1. **Case 1: $P = \texttt{aba}$**.
   - Borders of $\texttt{aba}$ (including $k=3$): $k \in \{3, 1\}$ (since $\texttt{aba}[1..1] = \texttt{aba}[3..3] = \texttt{a}$, while $k=2$ has $\texttt{ab} \ne \texttt{ba}$).
   - Autocorrelation polynomial: $C_{\texttt{aba}}(x) = x^{3-3} + x^{3-1} = 1 + x^2$.
   - Generating function:
     $$A_{\texttt{aba}}(x) = \frac{1 + x^2}{(1 - 2x)(1 + x^2) + x^3} = \frac{1 + x^2}{1 - 2x + x^2 - x^3} = 1 + 2x + 4x^2 + 7x^3 + 12x^4 + 21x^5 + \cdots$$
   - Hand-check $n = 4$: Out of $2^4 = 16$ binary strings of length $4$, those containing $\texttt{aba}$ are $\texttt{abaa}, \texttt{abab}, \texttt{aaba}, \texttt{baba}$ ($4$ distinct strings, no self-overlap of length $2$ fits inside length $4$!). Thus $a_4 = 16 - 4 = 12$. Matches $[x^4] A_{\texttt{aba}}(x) = 12$!
   - Hand-check $n = 5$: Out of $32$ strings, naïve count subtracts $2 \times 4 + 4 = 12$, except $\texttt{ababa}$ contains two overlapping copies of $\texttt{aba}$ (`[1..3]` and `[3..5]`). So $11$ strings contain $\texttt{aba}$, leaving $32 - 11 = 21$. Matches $[x^5] A_{\texttt{aba}}(x) = 21$!
2. **Case 2: $P = \texttt{aaa}$**.
   - Borders of $\texttt{aaa}$: $k \in \{3, 2, 1\}$.
   - Autocorrelation polynomial: $C_{\texttt{aaa}}(x) = 1 + x + x^2$.
   - Generating function:
     $$A_{\texttt{aaa}}(x) = \frac{1 + x + x^2}{(1 - 2x)(1 + x + x^2) + x^3} = \frac{1 + x + x^2}{1 - x - x^2 - x^3} = 1 + 2x + 4x^2 + 7x^3 + 13x^4 + 24x^5 + \cdots$$
   - Hand-check $n = 4$: Strings containing $\texttt{aaa}$ are $\texttt{aaaa}, \texttt{aaab}, \texttt{baaa}$ ($3$ strings, because $\texttt{aaaa}$ has two overlapping occurrences of $\texttt{aaa}$ at `[1..3]` and `[2..4]`!). Thus $a_4 = 16 - 3 = 13 > 12$. Because $\texttt{aaa}$ has a stronger border ($k=2$, $x^1$ term in $C_P(x)$), its occurrences cluster more tightly, leaving **more** valid avoiding strings!

---

### 83.5 Algorithmic Contract & Boundary Pitfalls

- **Precondition**: Pattern set $\mathcal{P} = \{P_1, \dots, P_m\}$ reduced to an **antichain** (no $P_i$ is a substring of $P_j$ for $i \ne j$).
- **Computing $C_{i,j}(x)$**:
  - Run KMP on each $P_i$, or build the Aho–Corasick automaton on $\mathcal{P}$ in $O(\sum |P_i|)$.
  - In the AC automaton, the borders of $P_i$ that are prefixes of $P_j$ correspond precisely to the ancestors of the terminal node of $P_i$ in the AC fail tree that lie on the trie path of $P_j$!
  - Even simpler: to find $\text{Overlap}(P_i, P_j)$ for all pairs $(i, j)$ in $O(\sum |P_i| + m^2 \cdot \text{output})$, walk the trie of $\mathcal{P}$ or traverse the fail-tree ancestors of node $P_i$ and mark their depths on each pattern $P_j$.
- **Boundary Pitfalls**:
  1. **Forgetting Antichain Reduction**: If $P_1 = \texttt{ab}$ and $P_2 = \texttt{cabd}$, $P_1$ occurs strictly *inside* $P_2$, which is not a prefix-suffix overlap! Failing to delete $P_2$ before building $\mathbf{C}(x)$ breaks the interval chain ordering $l_1 < l_2 \iff r_1 < r_2$ and produces wrong polynomials.
  2. **Swap of $C_{i,j}(x)$ Exponent**: When $P_i$ is on the left and $P_j$ is on the right overlapping by $k$, the newly added suffix of $P_j$ has length $|P_j| - k$ (NOT $|P_i| - k$). However, if you instead define $D_i(x)$ as clusters *starting* with $P_i$, the exponent becomes $|P_i| - k$. Keep left-to-right orientation consistent!

---

## Iteration 84: Probability Generating Functions (PGFs), Conway's Casino Martingale (`康威赌博`) & Pattern Racing Games

### 84.1 The Diagnostic Signal: Stopping Times on Infinite Random String Streams

Suppose characters are drawn independently at each step $t = 1, 2, \dots$ from $\Sigma$, either uniformly ($\Pr[c] = 1/\sigma$) or with biased probabilities $p_c = \Pr[c] > 0$ ($\sum_{c \in \Sigma} p_c = 1$).
- **Questions Asked in Contest Problems**:
  1. *Single-Pattern Hitting Time (`[CTSC2006] 歌唱王国`)*: Let $T_S$ be the first step $t$ at which the generated string ends with pattern $S$. What are the expectation $\mathbb{E}[T_S]$ and variance $\text{Var}(T_S)$?
  2. *Multi-Player Pattern Racing (`[SDOI2017] 硬币游戏`, `[JSOI2009] 有趣的游戏`)*: Given $m$ patterns $P_1, \dots, P_m$ (none a substring of another), the game stops at the first step $T = \min_i T_{P_i}$ when *any* pattern $P_i$ appears. What is the probability $\pi_i = \Pr[T = T_{P_i}]$ that $P_i$ wins the race?

Why does naive Markov-chain Gaussian elimination over the AC automaton fail?
- If $|S| = 10^5$ (`[CTSC2006] 歌唱王国`), Gaussian elimination on $10^5$ KMP states takes $O(|S|^3)$—and even tridiagonal-like KMP elimination is messy when variance $\text{Var}(T_S)$ is requested.
- If $m = 300$ and $|P_i| = 300$ (`[SDOI2017] 硬币游戏`), total AC states can be $O(m \cdot |P_i|) = 90{,}000$. Running $90{,}000 \times 90{,}000$ Gaussian elimination is $O((m|P|)^3) \approx 7 \times 10^{14}$ operations! We MUST compress the $90{,}000$ AC states down to an $(m+1) \times (m+1)$ system of size $301 \times 301$.

---

### 84.2 First Derivation: The Probability Generating Function (PGF) Algebra (`F'(1)` & `F''(1)`)

Let us set up the exact double-generating-function system for a general pattern race among an antichain $\mathcal{P} = \{P_1, \dots, P_m\}$ under arbitrary character probabilities $p_c > 0$. For any string $u = u_1 \dots u_k$, denote its probability weight by
$$\Pr(u) = \prod_{r=1}^k p_{u_r} \qquad (\text{for uniform alphabet, } \Pr(u) = \sigma^{-|u|}).$$

#### Concrete Objects and Their PGFs
- Let $F_i(z) = \sum_{n \ge 0} f_{i,n} z^n$, where $f_{i,n}$ is the probability that the game **stops at step $n$ with pattern $P_i$ appearing for the first time**.
- Let $G(z) = \sum_{n \ge 0} g_n z^n$, where $g_n$ is the probability that the game **has NOT stopped by step $n$** (i.e., the generated string of length $n$ contains no $P_1, \dots, P_m$).

Let us derive the two fundamental identities linking $G(z)$ and $F_1(z), \dots, F_m(z)$:

1. **The Conservation-of-Probability (One-Step Extension) Equation**:
   Take any valid non-terminating string of length $n$ (counted by $g_n$) and append one random character $c \in \Sigma$ at step $n+1$. Since the total probability of all 1-step extensions is $\sum_{c \in \Sigma} p_c = 1$, every surviving string at step $n$ either remains surviving at step $n+1$ (contributing to $g_{n+1}$) or terminates for the first time at step $n+1$ with some unique pattern $P_i$ (by the Antichain Invariant, at most one $P_i$ can complete at step $n+1$).
   Multiplying by $z^{n+1}$ and summing over $n \ge 0$ (with $g_0 = 1$ and $f_{i,0} = 0$):
   $$z G(z) + 1 = G(z) + \sum_{i=1}^m F_i(z) \iff (1 - z) G(z) + \sum_{i=1}^m F_i(z) = 1. \tag{84.1}$$

2. **The Over-Shooting (Append-$P_j$) Equation**:
   Take any surviving string $W$ of length $n$ (which contains no $P_i \in \mathcal{P}$) and **forcibly append the entire pattern $P_j$** to its right end, multiplying by $\Pr(P_j) z^{|P_j|}$.
   Because $P_j$ now definitely appears at the very end (at step $n + |P_j|$), this combined string $W P_j$ **must trigger the stopping condition for the first time** at some position $n + k$ where $1 \le k \le |P_j|$!
   Suppose the first trigger occurs at step $n + k$ with pattern $P_i$. Because $W$ had no occurrences of $\mathcal{P}$, this first occurrence of $P_i$ must straddle the boundary between $W$ and $P_j$ (or equal $P_j$ at $k = |P_j|$). That means the suffix of $P_i$ of length $k$ must equal the prefix of $P_j$ of length $k$:
   $$k \in \text{Overlap}(P_i, P_j) \iff P_i[|P_i|-k+1 .. |P_i|] = P_j[1..k].$$
   Once the game stops at step $n + k$ with $P_i$, the remaining $|P_j| - k$ characters of $P_j$, namely $P_j[k+1 .. |P_j|]$, are simply the deterministic suffix required to finish writing $W P_j$!
   Therefore, every pair of (surviving string $W$, appended $P_j$) bijects uniquely with a triple of (first stopping string ending with $P_i$, overlap length $k \in \text{Overlap}(P_i, P_j)$, remaining suffix $P_j[k+1..|P_j|]$):
   $$G(z) \cdot \Pr(P_j) z^{|P_j|} = \sum_{i=1}^m F_i(z) \sum_{k \in \text{Overlap}(P_i, P_j)} \Pr(P_j[k+1..|P_j|]) z^{|P_j| - k}.$$
   Dividing both sides by $\Pr(P_j)$ (which is nonzero since $p_c > 0$) and noting that $\frac{\Pr(P_j[k+1..|P_j|])}{\Pr(P_j)} = \frac{1}{\Pr(P_j[1..k])}$, we obtain the **PGF Autocorrelation Equation**:
   $$G(z) z^{|P_j|} = \sum_{i=1}^m F_i(z) \sum_{k \in \text{Overlap}(P_i, P_j)} \frac{z^{|P_j| - k}}{\Pr(P_j[1..k])} \qquad \text{for all } j = 1, \dots, m. \tag{84.2}$$

---

### 84.3 Extracting Expectation $\mathbb{E}[T_S]$, Variance $\text{Var}(T_S)$, and Multi-Player Win Probabilities

#### 1. Single Pattern $S$ ($m = 1$)
When $\mathcal{P} = \{S\}$, write $F(z) = F_1(z)$. Since $\Sigma$ is finite and $p_c > 0$, the game stops with probability $1$ in finite expected time, so $F(1) = 1$, $G(1) = \sum_{n \ge 0} \Pr[T_S > n] = \mathbb{E}[T_S]$, and differentiating (84.1) $(1 - z)G(z) + F(z) = 1$ at $z = 1$ gives:
- At $z = 1$ in (84.2): since $F(1) = 1$ and $P_1[1..k] = S[1..k]$, we immediately obtain
  $$\mathbb{E}[T_S] = F'(1) = G(1) = \sum_{k \in \text{Borders}(S)} \frac{1}{\Pr(S[1..k])} = \sum_{k \in \text{Borders}(S)} |\Sigma|^k \quad (\text{for uniform } \Sigma). \tag{84.3}$$
  Here $\text{Borders}(S)$ includes $k = |S|$ (the whole string $S$ is a border of itself) and excludes $k = 0$.
- **Variance $\text{Var}(T_S)$**: How do we get $\text{Var}(T_S) = \mathbb{E}[T_S^2] - (\mathbb{E}[T_S])^2 = F''(1) + F'(1) - (F'(1))^2$?
  Differentiate $(1 - z)G(z) + F(z) = 1$ twice at $z = 1$:
  - First derivative: $-G(z) + (1 - z)G'(z) + F'(z) = 0 \implies F'(1) = G(1)$.
  - Second derivative: $-2G'(z) + (1 - z)G''(z) + F''(z) = 0 \implies F''(1) = 2G'(1)$.
  Now differentiate the single-pattern version of (84.2), namely $G(z) = F(z) \sum_{k \in \text{Borders}(S)} \frac{z^{-k}}{\Pr(S[1..k])}$, at $z = 1$:
  $$G'(1) = F'(1) \sum_{k \in \text{Borders}(S)} \frac{1}{\Pr(S[1..k])} - F(1) \sum_{k \in \text{Borders}(S)} \frac{k}{\Pr(S[1..k])} = (\mathbb{E}[T_S])^2 - \sum_{k \in \text{Borders}(S)} \frac{k}{\Pr(S[1..k])}.$$
  Substituting $F''(1) = 2G'(1)$ into $\text{Var}(T_S) = F''(1) + F'(1) - (F'(1))^2$ yields the closed-form **Single-Pattern Hitting Time Variance Formula**:
  $$\text{Var}(T_S) = (\mathbb{E}[T_S])^2 + \mathbb{E}[T_S] - 2 \sum_{k \in \text{Borders}(S)} \frac{k}{\Pr(S[1..k])}. \tag{84.4}$$
  For a uniform alphabet of size $\sigma = |\Sigma|$:
  $$\text{Var}(T_S) = \left(\sum_{k \in \text{Borders}(S)} \sigma^k\right)^2 + \sum_{k \in \text{Borders}(S)} (1 - 2k) \sigma^k.$$

#### 2. Multi-Player Pattern Race ($m$ Patterns $P_1, \dots, P_m$)
Evaluate (84.1) and (84.2) at $z = 1$. Since $(1 - z)G(z) \to 0$ as $z \to 1^-$ (because $g_n$ decays exponentially), setting $\pi_i = F_i(1) = \Pr[P_i \text{ wins}]$ and $E = G(1) = \mathbb{E}[T]$ gives an exact **$(m+1) \times (m+1)$ linear system**:
$$\begin{cases}
\displaystyle \sum_{i=1}^m \pi_i = 1, \\[10pt]
\displaystyle \sum_{i=1}^m \pi_i \, \Omega_{i,j} - E = 0 \quad \text{for } j = 1, \dots, m,
\end{cases}
\qquad \text{where } \Omega_{i,j} = \sum_{k \in \text{Overlap}(P_i, P_j)} \frac{1}{\Pr(P_j[1..k])}. \tag{84.5}$$
In uniform alphabet problems (`[SDOI2017] 硬币游戏`), $\Omega_{i,j} = \sum_{k \in \text{Overlap}(P_i, P_j)} \sigma^k$ is called the **Conway Betting Payoff Number** between $P_i$ and $P_j$! Solving this $(m+1) \times (m+1)$ system by Gaussian elimination takes $O(m^3)$ time instead of $O((m|P|)^3)$.

---

### 84.4 Second Derivation: Conway's Casino Martingale (`康威赌博`) & Doob's Optional Stopping Theorem

Why does $\Omega_{i,j} = \sum_{k \in \text{Overlap}(P_i, P_j)} \frac{1}{\Pr(P_j[1..k])}$ appear so naturally? John Horton Conway explained this via a **fair casino betting syndicate** (`康威赌博`):

- **The Casino Model**: Imagine that before each step $t = 1, 2, \dots$, a new gambler $G_t$ walks into the casino with $\$1$ of initial capital and wants to bet solely on pattern $P_j = c_1 c_2 \dots c_L$ appearing at positions $t, t+1, \dots, t+L-1$.
  - At step $t$, gambler $G_t$ stakes their entire $\$1$ on the event that the $t$-th character is $c_1$. Since $\Pr[c_1] = p_{c_1}$, a **fair bet** pays $\frac{1}{p_{c_1}}$ dollars if $c_1$ appears and $\$0$ otherwise.
  - If $c_1$ appears, $G_t$ now holds $\frac{1}{p_{c_1}}$ dollars and stakes the **entire amount** at step $t+1$ on $c_2$ appearing! If $c_2$ appears, $G_t$ holds $\frac{1}{p_{c_1} p_{c_2}} = \frac{1}{\Pr(P_j[1..2])}$ dollars, and so on.
  - At the first mismatch, $G_t$ loses everything ($0$ dollars) and leaves the table. If $G_t$ matches all $L$ characters of $P_j$, $G_t$ holds $\frac{1}{\Pr(P_j)}$ dollars and stops betting.
- **The Martingale Property**: Because every individual bet is fair ($\mathbb{E}[\text{wealth after step} \mid \mathcal{F}_{t-1}] = \text{wealth before step}$), and exactly $\$1$ of fresh capital is injected by the newly arriving gambler $G_t$ at each step $t \le T$, the process
  $$M_t = (\text{total wealth of all gamblers at time } t) - t$$
  is a **martingale** with $M_0 = 0$.
- **Doob's Optional Stopping Theorem**: Since the stopping time $T = \min_i T_{P_i}$ is exponentially bounded ($\mathbb{E}[T] < \infty$) and the incremental change $|M_{t} - M_{t-1}|$ is uniformly bounded by $\sum_{k=1}^{|P_j|} \frac{1}{\Pr(P_j[1..k])} < \infty$, Doob's Optional Stopping Theorem guarantees $\mathbb{E}[M_T] = M_0 = 0$, i.e.,
  $$\mathbb{E}[T] = \mathbb{E}[\text{total wealth of all gamblers targeting } P_j \text{ at stopping time } T].$$
- **What is the total wealth of $P_j$-gamblers when the game stops with $P_i$?**
  Suppose the game stops at step $T$ because $P_i$ just appeared at the end of the string. Any gambler $G_t$ targeting $P_j$ who is still alive at step $T$ must have matched some prefix $P_j[1..k]$ of $P_j$ against the last $k$ characters of the string—which are the suffix $P_i[|P_i|-k+1 .. |P_i|]$ of $P_i$!
  Thus, the alive gamblers targeting $P_j$ correspond bijectively to $k \in \text{Overlap}(P_i, P_j)$, and the gambler who matched $k$ characters holds $\frac{1}{\Pr(P_j[1..k])}$ dollars!
  Consequently, conditioned on $P_i$ winning the race, the deterministic payout to the $P_j$-syndicate at time $T$ is $\Omega_{i,j} = \sum_{k \in \text{Overlap}(P_i, P_j)} \frac{1}{\Pr(P_j[1..k])}$. Taking the expectation over which $P_i$ wins gives:
  $$\mathbb{E}[T] = \sum_{i=1}^m \pi_i \Omega_{i,j} \quad \text{for every } j = 1, \dots, m.$$
  That is Equation (84.5), proved in three lines without a single derivative!

---

### 84.5 Small Hand-Checkable Example: Penney's Game ($P_1 = \texttt{HTH}$ vs. $P_2 = \texttt{HTT}$, $\sigma = 2$)

Let $\Sigma = \{\texttt{H}, \texttt{T}\}$ with uniform coins ($p_{\texttt{H}} = p_{\texttt{T}} = 1/2$), $P_1 = \texttt{HTH}$, $P_2 = \texttt{HTT}$.
- Compute the $2 \times 2$ overlap payoff matrix $\Omega_{i,j} = \sum_{k \in \text{Overlap}(P_i, P_j)} 2^k$:
  - $\text{Overlap}(P_1, P_1) = \text{Overlap}(\texttt{HTH}, \texttt{HTH}) = \{3, 1\} \implies \Omega_{1,1} = 2^3 + 2^1 = 10$.
  - $\text{Overlap}(P_1, P_2) = \text{Overlap}(\texttt{HTH}, \texttt{HTT}) = \{1\} \implies \Omega_{1,2} = 2^1 = 2$ (suffix `H` of `HTH` matches prefix `H` of `HTT`).
  - $\text{Overlap}(P_2, P_1) = \text{Overlap}(\texttt{HTT}, \texttt{HTH}) = \emptyset \implies \Omega_{2,1} = 0$ (no suffix of `HTT` starts with `H` except `HTT` itself, which doesn't match `HTH`).
  - $\text{Overlap}(P_2, P_2) = \text{Overlap}(\texttt{HTT}, \texttt{HTT}) = \{3\} \implies \Omega_{2,2} = 2^3 = 8$.
- **Single-pattern expectations**: $\mathbb{E}[T_{\texttt{HTH}}] = \Omega_{1,1} = 10$, whereas $\mathbb{E}[T_{\texttt{HTT}}] = \Omega_{2,2} = 8$.
- **Head-to-head race ($\pi_1 + \pi_2 = 1$)**:
  $$\begin{cases}
  10 \pi_1 + 0 \pi_2 = E \\
  2 \pi_1 + 8 \pi_2 = E
  \end{cases}
  \implies 10 \pi_1 = 2 \pi_1 + 8 \pi_2 \implies 8 \pi_1 = 8 \pi_2 \implies \pi_1 = \pi_2 = \frac{1}{2}, \quad E = 5!$$
  **Counter-Intuitive Phenomenon**: Even though $\texttt{HTH}$ takes longer on average to appear alone ($\mathbb{E}[T_{\texttt{HTH}}] = 10 > 8 = \mathbb{E}[T_{\texttt{HTT}}]$), in a head-to-head race against $\texttt{HTT}$ they tie $50\%$–$50\%$ because whenever $\texttt{HTH}$ wins, it leaves a live $\$2$ bet for $\texttt{HTT}$ ($\Omega_{1,2} = 2$), whereas when $\texttt{HTT}$ wins, $\texttt{HTH}$ holds $\$0$ ($\Omega_{2,1} = 0$)!

---

## Iteration 85: Automaton DP (`自動機上のDP`), Nerode Minimization & DP-of-DP (`DP套DP`)

### 85.1 The Diagnostic Signal: Outer Counting Over Inner String Recognition

In competitive programming, an **Automaton DP** (`自動機上のDP`) counts or optimizes strings $W \in \Sigma^n$ satisfying a property $\mathcal{L}$ by running an outer DP over prefixes $W[1..i]$ whose state tracks the current node $u$ in a deterministic automaton $\mathcal{A}$ recognizing $\mathcal{L}$:
$$dp[i][u] \xrightarrow{+ c \in \Sigma} dp[i+1][\delta(u, c)].$$
This splits into two distinct tiers of difficulty:
1. **Classical Automaton DP (AC / KMP / SAM / Palindromic / Lyndon State DP)**: The property $\mathcal{L}$ is already recognized by a standard string automaton:
   - *Multi-pattern avoidance / occurrence counting*: $\mathcal{A}$ is the Aho–Corasick automaton on $\mathcal{P}$ (where `bad[u]` is propagated down the fail tree: `bad[u] |= bad[fail[u]]`).
   - *Distinct substring / lexicographical / Lyndon constraints*: $\mathcal{A}$ is a Suffix Automaton or Duval Lyndon-factorization state machine (`(i - j, k)` tracking the period and phase of the current pre-Lyndon word).
2. **DP-of-DP (`DP套DP` / Automaton Synthesis via Inner DP)**:
   - **Diagnostic Signal**: What if the condition $W \in \mathcal{L}$ is defined not by substring matching, but by the output of an **inner dynamic programming algorithm** $f(S, W)$ run on a fixed reference string $S$ (typically $|S| \le 15$ or $|S| \le 20$) and the unknown string $W$ (length $n \le 1000$ or $10^4$)?
   - *Canonical Examples*:
     - Count strings $W \in \Sigma^n$ whose **Longest Common Subsequence** $\text{LCS}(S, W)$ with a given template $S$ ($|S| = K \le 15$) equals $k$ for each $0 \le k \le K$ (`[BZOJ 3864] Hero meet devil`, `[TJOI2018] 游园会`).
     - Count strings $W$ whose Levenshtein edit distance to $S$ is $\le d$, or strings that can be partitioned into valid tiles (Mahjong hand / regular expression / palindrome partition DPs).

---

### 85.2 The Combinatorial Word Invariant: Compressing Inner DP Rows & Myhill–Nerode Minimization

Why doesn't the inner DP state space explode?
1. **Difference-Bitmask Compression for LCS DP-of-DP**:
   - In the standard LCS DP between $S[1..K]$ and $W[1..i]$, after processing prefix $W[1..i]$, the inner DP state is the row vector
     $$\mathbf{v}^{(i)} = \bigl(dp_{\text{inner}}[i][0], dp_{\text{inner}}[i][1], \dots, dp_{\text{inner}}[i][K]\bigr),$$
     where $dp_{\text{inner}}[i][j] = \text{LCS}(W[1..i], S[1..j])$.
   - Naive bound: Since $0 \le dp_{\text{inner}}[i][j] \le K$, there look to be $(K+1)^K$ possible row vectors—for $K = 15$, $16^{15} \approx 10^{18}$ states!
   - **Monotonicity Invariant**: Adding one character $S[j]$ to the prefix $S[1..j-1]$ can increase the LCS with $W[1..i]$ by **at most $1$** and at least $0$:
     $$dp_{\text{inner}}[i][0] = 0, \qquad \Delta_j = dp_{\text{inner}}[i][j] - dp_{\text{inner}}[i][j-1] \in \{0, 1\} \quad \text{for all } 1 \le j \le K.$$
   - Therefore, the entire inner DP row $\mathbf{v}^{(i)}$ is uniquely encoded by a **$K$-bit binary mask** $M \in \{0, 1\}^K$, reducing the number of reachable inner DP states from $(K+1)^K$ to at most $2^K$ ($32{,}768$ for $K = 15$)!
2. **State-Space Reachability & Myhill–Nerode / Hopcroft DFA Minimization**:
   - Even when the theoretical upper bound on inner DP tuples is large (e.g., edit distance $\le 2$, Mahjong tile meld states, or KMP-like game states), the set of **actually reachable** inner DP states starting from $\mathbf{v}^{(0)}$ via BFS over $c \in \Sigma$ is often tiny (e.g., $O(2^K)$ or a few thousand states instead of millions).
   - Furthermore, by the **Myhill–Nerode Theorem**, two inner DP states $u, v$ that cannot be distinguished by any suffix $Z \in \Sigma^*$ can be merged via **Hopcroft's $O(|\Sigma| V \log V)$ DFA Minimization** before running the outer $O(n \cdot |\Sigma| \cdot V_{\min})$ DP or matrix exponentiation!

---

### 85.3 The Reverse-Engineering Scratchpad: Precomputing the Inner Automaton $\delta(M, c)$

Let us trace how to compile the LCS inner transition $\delta(M, c)$ for a mask $M \in [0, 2^K)$ and character $c \in \Sigma$:
1. **Unpack $M$**: Reconstruct prefix sums $a[0] = 0$ and $a[j] = a[j-1] + ((M \gg (j-1)) \ \& \ 1)$ for $1 \le j \le K$.
2. **Apply the Inner DP Transition for Character $c$**:
   $$b[0] = 0, \qquad b[j] = \begin{cases} a[j-1] + 1 & \text{if } S[j] = c, \\ \max(b[j-1], a[j]) & \text{if } S[j] \ne c, \end{cases} \quad \text{for } j = 1, \dots, K.$$
3. **Repack into New Mask $M'$**:
   $$M' = \sum_{j=1}^K (b[j] - b[j-1]) \cdot 2^{j-1}.$$
   Notice we can also compute $M' = \delta(M, c)$ in $O(1)$ bitwise operations using the Allison–Dix / Myers bit-parallel LCS transition (covered in depth in Wave 4B), or simply precompute the table `trans[M][c]` in $O(K |\Sigma| 2^K)$ before the outer DP!
4. **Couple with Additional Outer Automata (`[TJOI2018] 游园会`)**:
   If the problem simultaneously forbids a pattern $P = \texttt{NOI}$ (tracked by a KMP state $q \in \{0, 1, 2\}$) AND asks for the LCS distribution with $S$ ($|S| = K \le 15$), the outer DP simply walks the **product automaton** state $(M, q) \in \{0, \dots, 2^K - 1\} \times \{0, 1, 2\}$ in $O(n \cdot |\Sigma| \cdot 3 \cdot 2^K)$ time!

---

### 85.4 Boundary Pitfalls in Automaton DP & `DP套DP`

1. **Missing Fail-Tree Or-Propagation in AC DP**:
   In Aho–Corasick avoidance DP, marking only the exact terminal nodes of $P_i \in \mathcal{P}$ as `bad[u] = true` is **fatal** when a shorter forbidden pattern $P_j$ is a suffix of a prefix of $P_i$. You MUST propagate `bad[u] |= bad[fail[u]]` in BFS order before building the transition matrix.
2. **Unminimized Inner DP Blowup**:
   When designing an inner DP for `DP套DP`, keeping raw unbounded integers (like total score or position $i$) in the inner DP state destroys finiteness! Every component of the inner DP tuple **must** be capped (e.g., $\min(\text{val}, \text{cap})$) or converted to relative offsets ($\Delta_j = dp[j] - dp[j-1]$) so that the BFS over reachable inner states terminates in a small finite DFA.

---

## Iteration 86: Exact String Counting with Forbidden Substrings & Weighted Occurrence Bivariate Generating Functions

### 86.1 The Diagnostic Signal: Counting Strings with *Exactly* $k$ Pattern Occurrences

What if, instead of pure avoidance ($k = 0$ occurrences), a problem asks for:
- The number of strings $W \in \Sigma^n$ containing **exactly $k$ occurrences** (or at most $k$ occurrences) of a single pattern $P$ or a pattern family $\mathcal{P} = \{P_1, \dots, P_m\}$?
- Or the expected $r$-th power $\mathbb{E}[\text{occ}(W)^r]$ of the number of occurrences of $\mathcal{P}$ in a random string of length $n$?
- Or each pattern $P_i \in \mathcal{P}$ carries a formal weight variable $t_i$ (meaning each occurrence of $P_i$ multiplies the string's weight by $t_i$), and we want the multivariate generating function
  $$F(x; t_1, \dots, t_m) = \sum_{W \in \Sigma^*} x^{|W|} \prod_{i=1}^m t_i^{\text{occ}_i(W)}?$$

Why does standard AC DP struggle here?
- Tracking the exact occurrence count $0 \le c \le k$ in the AC automaton multiplies the state space by $(k+1)$, costing $O(n \cdot k \cdot \sum |P_i|)$. Worse, if $n \le 10^{18}$ or $L = |P| \le 10^5$ with $k \le 500$, AC DP is too slow by orders of magnitude, whereas the **Weighted (Bivariate) Goulden–Jackson Cluster Method** yields a closed-form bivariate rational generating function $F(x, t)$ directly from the autocorrelation polynomial $C_P(x)$!

---

### 86.2 The Combinatorial Word Invariant: Bivariate $(t - 1)$ Cluster Sieve

How do we generalize the marked-word cancellation $(1 - 1)^{\text{occ}(W)} = [{\text{occ}(W) = 0}]$ from Iteration 83 so that a word $W$ with $\text{occ}(W)$ occurrences gets weight $t^{\text{occ}(W)}$ instead of $0$?

#### The Algebraic Identity: $t = 1 + (t - 1)$
Instead of giving each marked occurrence weight $-1$, assign each marked occurrence of pattern $P_i$ the formal weight
$$w_i = t_i - 1 \qquad (\text{or } w = t - 1 \text{ when all patterns share one variable } t).$$
Now sum over all words $W \in \Sigma^*$ and all subsets of marked occurrences $M \subseteq \text{Occ}(W)$:
$$\sum_{W \in \Sigma^*} x^{|W|} \sum_{M \subseteq \text{Occ}(W)} \prod_{(r, i) \in M} (t_i - 1) = \sum_{W \in \Sigma^*} x^{|W|} \prod_{(r, i) \in \text{Occ}(W)} \bigl(1 + (t_i - 1)\bigr) = \sum_{W \in \Sigma^*} x^{|W|} \prod_{i=1}^m t_i^{\text{occ}_i(W)}!$$
Look at what just happened:
- Every occurrence of $P_i$ in $W$ has two choices in the marked word $(W, M)$:
  1. Leave this occurrence **unmarked** (weight $1$), or
  2. **Mark** this occurrence (weight $t_i - 1$).
- Because the geometry of connected components of *marked* occurrences $M$ depends ONLY on the intervals in $M$ (and is completely oblivious to any unmarked occurrences of $\mathcal{P}$ that happen to appear elsewhere in $W$!), the decomposition of a marked word $(W, M)$ into free letters and connected clusters of marked occurrences is **100% identical** to Iteration 83—the only change is that every marked pattern $P_j$ contributes factor $(t_j - 1)$ instead of $-1$!

---

### 86.3 The Reverse-Engineering Scratchpad: Bivariate Cluster System & Single-Pattern Closed Form

Assume first that $\mathcal{P} = \{P_1, \dots, P_m\}$ is an **antichain** (no $P_i$ is a substring of $P_j$ for $i \ne j$).
Replacing $-1$ by $(t_j - 1)$ in the cluster extension recurrence from Section 83.3:
- A single-pattern cluster $P_j$ has weight $(t_j - 1) x^{|P_j|}$.
- Extending a cluster ending in $P_i$ by a properly overlapping $P_j$ multiplies by $(t_j - 1) \widetilde{C}_{i,j}(x)$.
Thus:
$$C_j(x, \mathbf{t}) = (t_j - 1) x^{|P_j|} + (t_j - 1) \sum_{i=1}^m C_i(x, \mathbf{t}) \widetilde{C}_{i,j}(x).$$
Dividing by $(t_j - 1)$ and using $\widetilde{C}_{j,j}(x) = C_{j,j}(x) - 1$ gives the **Weighted Goulden–Jackson Linear System**:
$$\sum_{i=1}^m C_i(x, \mathbf{t}) \left( \widetilde{C}_{i,j}(x) - \frac{\delta_{i,j}}{t_j - 1} \right) = -x^{|P_j|} \iff \sum_{i=1}^m C_i(x, \mathbf{t}) \left( C_{i,j}(x) - \frac{t_j}{t_j - 1} \delta_{i,j} \right) = -x^{|P_j|}. \tag{86.1}$$
Once $C_1(x, \mathbf{t}), \dots, C_m(x, \mathbf{t})$ are solved, the full multivariate generating function is:
$$F(x; t_1, \dots, t_m) = \frac{1}{1 - \sigma x - \sum_{i=1}^m C_i(x, \mathbf{t})}. \tag{86.2}$$

#### Single Pattern $P$ ($m = 1$): Exact Generating Function for $k$ Occurrences
For a single pattern $P$ of length $L = |P|$ with autocorrelation polynomial $C_P(x) = \sum_{r \in \text{Borders}(P)} x^{L - r} = 1 + \widetilde{C}_P(x)$ and weight variable $t$:
- Equation (86.1) becomes:
  $$C_1(x, t) \left( C_P(x) - 1 - \frac{1}{t - 1} \right) = -x^L \implies C_1(x, t) = \frac{(t - 1) x^L}{1 - (t - 1)\bigl(C_P(x) - 1\bigr)}.$$
- Substituting into $F(x, t) = \bigl(1 - \sigma x - C_1(x, t)\bigr)^{-1}$ yields the **Bivariate Guibas–Odlyzko Generating Function**:
  $$F(x, t) = \frac{1 - (t - 1)\bigl(C_P(x) - 1\bigr)}{(1 - \sigma x)\Bigl(1 - (t - 1)\bigl(C_P(x) - 1\bigr)\Bigr) - (t - 1) x^L}. \tag{86.3}$$
- **Extracting $[t^k] F(x, t)$ (Strings with Exactly $k$ Occurrences of $P$)**:
  Rewrite the numerator and denominator of (86.3) by grouping terms with and without $t$:
  Let $D_0(x) = (1 - \sigma x) C_P(x) + x^L$ (the avoidance denominator from Iteration 83!) and $D_1(x) = (1 - \sigma x)\bigl(C_P(x) - 1\bigr) + x^L$. Then:
  $$F(x, t) = \frac{C_P(x) - t \bigl(C_P(x) - 1\bigr)}{D_0(x) - t D_1(x)} = \frac{C_P(x)}{D_0(x)} + \sum_{k \ge 1} t^k \, \frac{x^L}{D_0(x)^{k+1}} D_1(x)^{k-1}! \tag{86.4}$$
  Let us verify the algebraic identity $C_P(x) D_1(x) - \bigl(C_P(x) - 1\bigr) D_0(x) = x^L$:
  $$C_P(x)\Bigl((1 - \sigma x)(C_P(x) - 1) + x^L\Bigr) - (C_P(x) - 1)\Bigl((1 - \sigma x)C_P(x) + x^L\Bigr) = x^L \bigl(C_P(x) - C_P(x) + 1\bigr) = x^L.$$
  Thus, for every $k \ge 1$, the generating function $A^{(k)}(x) = [t^k] F(x, t)$ of strings containing **exactly $k$ occurrences** of $P$ is:
  $$A^{(k)}(x) = \frac{x^L \Bigl((1 - \sigma x)\bigl(C_P(x) - 1\bigr) + x^L\Bigr)^{k-1}}{\Bigl((1 - \sigma x) C_P(x) + x^L\Bigr)^{k+1}}. \tag{86.5}$$

---

### 86.4 Small Hand-Checkable Example: Exactly $k = 1$ Occurrence of $P = \texttt{aa}$ in Binary Strings of Length $n = 3, 4$

Let $\Sigma = \{\texttt{a}, \texttt{b}\}$ ($\sigma = 2$), $P = \texttt{aa}$ ($L = 2$).
- Borders of $\texttt{aa}$: $r \in \{2, 1\} \implies C_{\texttt{aa}}(x) = 1 + x$.
- Avoidance denominator: $D_0(x) = (1 - 2x)(1 + x) + x^2 = 1 - x - x^2$ (Fibonacci!).
- Numerator factor: $D_1(x) = (1 - 2x)(x) + x^2 = x - x^2$.
- For $k = 1$ occurrence of $\texttt{aa}$, Formula (86.5) gives:
  $$A^{(1)}(x) = \frac{x^2 D_1(x)^0}{D_0(x)^2} = \frac{x^2}{(1 - x - x^2)^2} = x^2 (1 + x + 2x^2 + 3x^3 + \cdots)^2 = x^2 + 2x^3 + 5x^4 + 10x^5 + \cdots$$
- Hand-check $n = 3$: Binary strings of length $3$ with **exactly one** occurrence of $\texttt{aa}$ are $\texttt{aab}$ and $\texttt{baa}$ ($\texttt{aaa}$ has **two** occurrences of $\texttt{aa}$, at `[1..2]` and `[2..3]`!). Count $= 2 = [x^3] A^{(1)}(x)$.
- Hand-check $n = 4$: Strings of length $4$ with **exactly one** occurrence of $\texttt{aa}$ are:
  - `aaba`, `aabb` (starts with `aa`, 3rd char `b`),
  - `baab` (`aa` in middle),
  - `abaa`, `bbaa` (ends with `aa`, 2nd char `b`).
  Total $= 5$ strings (`aaaa` has 3 occurrences; `aaab` and `baaa` have 2 occurrences). Matches $[x^4] A^{(1)}(x) = 5$!

---

### 86.5 What If $\mathcal{P}$ Is NOT an Antichain? (Embedded Substring Adjustment)

In pure avoidance ($t_i = 0$), if $P_1 = \texttt{ab}$ is a substring of $P_2 = \texttt{cabd}$, any word avoiding $P_1$ also avoids $P_2$, so we simply discard $P_2$.
**Critical Failure Mode**: In weighted counting ($t_i \ne 0$, e.g., counting total occurrences of all patterns in $\mathcal{P}$), if $P_1$ is a contiguous substring of $P_2$, we **cannot** discard $P_2$!
How do we handle embedded substrings when $\mathcal{P}$ is not an antichain?
- **Method 1 (Aho–Corasick Transfer Matrix)**: When $\sum |P_i|$ is small, build the AC automaton and let `cnt[u]` be the number of patterns in $\mathcal{P}$ that are suffixes of state $u$ (accumulated down the fail tree: `cnt[u] += cnt[fail[u]]`). Then transitioning into $u$ multiplies by $t^{\text{cnt}[u]}$.
- **Method 2 (Cluster Weight Absorb / Maximal Pattern Reduction)**: If we only keep patterns that are not proper substrings of each other, or if we modify the weight of marking $P_2$ to absorb all subsets of marked occurrences of $P_1$ strictly contained inside $P_2$—specifically, if $P_2$ contains $c_{2,1}$ internal occurrences of $P_1$, summing over all ways to mark/unmark those internal occurrences multiplies the effective weight of $P_2$ by $(1 + (t_1 - 1))^{c_{2,1}} = t_1^{c_{2,1}}$—PROVIDED no third pattern straddles an internal occurrence of $P_1$ and an endpoint of $P_2$. Whenever patterns can straddle internal occurrences arbitrarily, the AC transfer matrix or the general Kupavskii–Noonan–Zeilberger inclusion–exclusion graph must be used.

---

## Iteration 87: Multilingual Problem Mining (`[EN]` / `[ZH]` / `[JA]`), 4-Tier Difficulty Ladder & Quarantine Table

### 87.1 Curated 32-Problem Non-Template Corpus Across 4 Difficulty Tiers

Every problem below has been selected for requiring genuine structural modeling—Goulden–Jackson cluster reductions, martingale / PGF stopping-time linear systems, bivariate occurrence GFs, or inner-outer `DP套DP` automaton synthesis—and includes its **4-Step Zero-Magic Analysis**.

---

### Tier 1: Stepping Stone (Foundational Automaton DP, Single-Pattern Martingales & Basic Cluster Avoidance)

#### 1. `[ZH]` `[CTSC2006] 歌唱王国` (Luogu P4548 / BZOJ 1444 — Singing Kingdom)
- **Statement & Constraints**: Given an alphabet of size $\sigma \le 10^4$ and $T \le 50$ query strings $S$ of length $L \le 10^5$, a singer generates uniform random characters in $\{1, \dots, \sigma\}$ until $S$ appears as a contiguous suffix. Output $\mathbb{E}[T_S] \bmod 10^4$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $L \le 10^5$ per testcase makes $O(L^3)$ Gaussian elimination on KMP states impossible; we need an $O(L)$ evaluation of $\mathbb{E}[T_S]$.
  2. *Combinatorial Invariant*: By Conway's martingale (or $F'(1)$ of PGF (84.3)), alive gamblers when $S$ completes correspond bijectively to borders $k \in \text{Borders}(S)$, each holding $\sigma^k$ fair payout.
  3. *Algorithmic Compilation*: Compute KMP `pi` array of $S$ in $O(L)$; iterate $k = L, \pi[L], \pi[\pi[L]], \dots > 0$ and sum $\sigma^k \bmod 10^4$.
  4. *Pitfall*: Forgetting $k = L$ itself (which is always a border of $S$) or stopping before $k = 0$.

#### 2. `[ZH]` `[JSOI2007] 文本生成器` (Luogu P4052 — Text Generator)
- **Statement & Constraints**: Given $m \le 60$ uppercase words of length $\le 100$, count how many strings of length $n \le 100$ over $\Sigma = \{\texttt{A}..\texttt{Z}\}$ contain **at least one** of the $m$ words as a substring, modulo $10^4 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: "At least one" over $m$ overlapping patterns cannot be counted by naive sum $\sum 26^{n - |P_i|}$ due to overlaps and multi-pattern containment.
  2. *Combinatorial Invariant*: Complement counting: $(\text{at least one}) = 26^n - (\text{avoiding all } P_i)$. Avoidance is recognized by the AC automaton with fail-tree `bad[u] |= bad[fail[u]]` propagation.
  3. *Algorithmic Compilation*: Build AC automaton on $\mathcal{P}$ ($V \le 6000$ states), propagate `bad[u]` in BFS order, run outer DP $dp[i][u]$ over $0 \le i \le n$ and safe states $u$, subtract $\sum_u dp[n][u]$ from $26^n$.
  4. *Pitfall*: Only marking Trie end-nodes as `bad` without propagating along `fail[u]` misses shorter patterns embedded inside longer ones.

#### 3. `[EN]` `POJ 2778 — DNA Sequence`
- **Statement & Constraints**: Given $m \le 10$ forbidden DNA patterns of length $\le 10$ over $\{\texttt{A}, \texttt{C}, \texttt{G}, \texttt{T}\}$ and length $n \le 2 \times 10^9$, count strings of length $n$ avoiding all $m$ patterns modulo $100000$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $n \le 2 \times 10^9$ rules out $O(n V)$ step-by-step DP; total AC states $V \le 101$ or pattern count $m \le 10$ permits matrix exponentiation or Goulden–Jackson rational GF.
  2. *Combinatorial Invariant*: Safe AC transitions form a directed graph whose adjacency matrix $M$ has $(M^n)_{0, u} =$ number of safe paths of length $n$ ending at state $u$.
  3. *Algorithmic Compilation*: Build AC automaton, propagate `bad[u] |= bad[fail[u]]`, construct safe $V \times V$ transition matrix $M$, compute $M^n$ in $O(V^3 \log n)$ (or use $m \times m$ Goulden–Jackson + Bostan–Mori in $O(m^3 + L \log L \log n)$).
  4. *Pitfall*: Failing to merge identical patterns or failing to delete patterns containing shorter forbidden substrings if using Goulden–Jackson.

#### 4. `[JA]` `AtCoder ABC 138 F / Educational DP Contest S & Digit-Automaton Variants / ABC 305 G — Banned Substrings`
- **Statement & Constraints** (`ABC 305 G`): Given $n \le 10^{18}$ and $m \le 126$ banned binary strings $s_i$ of length $\le 6$ over $\{\texttt{a}, \texttt{b}\}$, count binary strings of length $n$ containing no $s_i$ modulo $998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $n \le 10^{18}$ requires matrix exponentiation or polynomial recurrence; since $|s_i| \le 6$, the last $5$ characters uniquely determine whether the next character completes a banned substring of length $\le 6$.
  2. *Combinatorial Invariant*: The minimal DFA / De Bruijn state of length $5$ (for $n \ge 6$) has at most $2^5 = 32$ states (or AC automaton on $s_i$ with $\le 64$ states).
  3. *Algorithmic Compilation*: Handle $n < 6$ by direct enumeration; for $n \ge 6$, initialize vector of valid length-$5$ prefixesAvoiding $\mathcal{P}$ and multiply by the $32 \times 32$ safe transition matrix $M^{n-5}$ in $O(32^3 \log n)$.
  4. *Pitfall*: A banned string of length $\le 5$ can already occur inside the initial length-$5$ seed state if not filtered out at initialization!

#### 5. `[EN]` `CSES 1113 / 2102 / 1739 Variants — Finding Patterns & Required Substring (CSES 1112)`
- **Statement & Constraints** (`CSES 1112 — Required Substring`): Given $n \le 1000$ and a pattern $P$ of length $m \le 100$ over $\Sigma = \{\texttt{A}..\texttt{Z}\}$, count strings of length $n$ containing $P$ at least once modulo $10^9+7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Single pattern avoidance / hitting count; teaches the exact equivalence between KMP-automaton DP and the Guibas–Odlyzko autocorrelation GF $A(x) = C_P(x) / ((1 - 26x)C_P(x) + x^m)$.
  2. *Combinatorial Invariant*: Complement count $26^n - [x^n] A(x)$, where $C_P(x) = \sum_{k \in \text{Borders}(P)} x^{m-k}$.
  3. *Algorithmic Compilation*: Either run KMP automaton DP in $O(n m \sigma)$ or extract $[x^n] \frac{C_P(x)}{(1 - 26x)C_P(x) + x^m}$ in $O(n m)$ via polynomial division.
  4. *Pitfall*: In KMP DP, once state $m$ is reached, it is an **absorbing state** (`trans[m][c] = m`), NOT transitioned via `pi[m]`.

#### 6. `[ZH]` `[HNOI2004] L语言` / `[POI 2000] 病毒 Viruses (Luogu P2444)`
- **Statement & Constraints** (`Luogu P2444`): Given $m$ binary virus strings of total length $\sum |P_i| \le 3 \times 10^4$, determine whether there exists an **infinite** safe binary string avoiding all $m$ patterns.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Asking whether $a_n > 0$ for all $n \to \infty$ (i.e., whether the rational GF $A(x)$ has a positive radius of convergence or only finitely many terms).
  2. *Combinatorial Invariant*: An infinite safe string exists if and only if the safe subgraph of the AC automaton (excluding all states where `bad[u] == true`) contains a **directed cycle** reachable from the root $0$.
  3. *Algorithmic Compilation*: Build AC automaton over $\{\texttt{0}, \texttt{1}\}$, propagate `bad[u] |= bad[fail[u]]`, run 3-color DFS (`vis` / `in_stack`) from root $0$ avoiding `bad` nodes to detect any cycle in $O(\sum |P_i|)$.
  4. *Pitfall*: Forgetting to build explicit trie-graph transitions `ch[u][c] = ch[fail[u]][c]` before cycle detection misses cycles that jump via failure links!

#### 7. `[EN]` `Codeforces 494B — Obsessive String` (Stepping Stone to Cluster/Border DP)
- **Statement & Constraints**: Given string $S$ and pattern $T$ ($|S|, |T| \le 10^5$), count non-empty ways to choose disjoint substrings of $S$, each containing $T$ at least once.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Warmup connecting KMP occurrence end-positions with prefix-sum DP before moving to unknown-string cluster generation.
  2. *Combinatorial Invariant*: A substring $S[l..r]$ contains $T$ iff $l \le \text{last\_start}(r)$, where $\text{last\_start}(r)$ is the latest start index of $T$ ending at or before $r$.
  3. *Algorithmic Compilation*: KMP finds all occurrences of $T$ in $S$; maintain double prefix sums of $dp[i]$ in $O(|S|)$.
  4. *Pitfall*: Off-by-one when $T$ matches at $r$, shifting valid left endpoints to $[1, r - |T| + 1]$.

#### 8. `[JA]` `AtCoder ABC 265 G / ARC 058 E (Iroha and Haiku)`
- **Statement & Constraints** (`ARC 058 E`): Given $N \le 40$ and $X \le 5, Y \le 7, Z \le 5$, count sequences of $N$ integers in $\{1, \dots, 10\}$ that contain a contiguous subsegment whose prefix sums hit $X$, then $X+Y$, then $X+Y+Z$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Subsegment sum pattern $(X, Y, Z)$ with $X+Y+Z \le 17$ is a forbidden pattern in unary-encoded prefix sums!
  2. *Combinatorial Invariant*: Encode the recent suffix sums $\le X+Y+Z$ as a bitmask $M \in [0, 2^{X+Y+Z})$ where bit $s-1$ is $1$ iff some suffix of the current sequence has sum $s$. Appending $a \in \{1..10\}$ transitions $M \to ((M \ll a) \mid 2^{a-1}) \ \& \ ((1 \ll (X+Y+Z)) - 1)$.
  3. *Algorithmic Compilation*: The bad mask condition is having bits $Z-1$, $Y+Z-1$, and $X+Y+Z-1$ simultaneously set! Run automaton DP over $2^{17}$ states in $O(N \cdot 10 \cdot 2^{X+Y+Z})$.
  4. *Pitfall*: Treating $(X, Y, Z)$ as a single string rather than a family of compositions; the bitmask DFA automatically merges all compositions into $2^{17}$ Myhill–Nerode states!

---

### Tier 2: Intermediate (Multi-Player Pattern Races, Biased PGFs, AC + Digit/Profile DP & Basic `DP套DP`)

#### 9. `[ZH]` `[SDOI2017] 硬币游戏` (Luogu P3706 — Coin Game)
- **Statement & Constraints**: $m \le 300$ students each pick a binary string $P_i \in \{\texttt{H}, \texttt{T}\}^L$ of length $L \le 300$ (all $P_i$ distinct). A fair coin is tossed repeatedly until one student's string appears; that student wins. Find each student's winning probability $\pi_i \in \mathbb{R}$ to $10^{-6}$ precision.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: AC automaton has up to $m L = 90{,}000$ states, so naive Markov-chain Gaussian elimination $O((mL)^3)$ TLEs completely.
  2. *Combinatorial Invariant*: Since all $|P_i| = L$ and $P_i$ are distinct, $\mathcal{P}$ is automatically an antichain! By Conway's martingale / PGF system (84.5), the $90{,}000$ states collapse to the $(m+1) \times (m+1)$ linear system $\sum_{i=1}^m \pi_i \Omega_{i,j} - E = 0$ and $\sum_{i=1}^m \pi_i = 1$, where $\Omega_{i,j} = \sum_{k \in \text{Overlap}(P_i, P_j)} 2^k$.
  3. *Algorithmic Compilation*: Compute $\Omega_{i,j}$ using polynomial hashing or KMP in $O(m^2 L)$ (scaling by $2^{-L}$, so $2^{k-L}$ avoids `double` overflow for $L = 300$!), then run $(m+1) \times (m+1)$ Gaussian elimination in $O(m^3)$.
  4. *Pitfall*: $2^{300}$ overflows standard 64-bit integers and needs scaling! Divide every equation by $2^L$ so $\tilde{\Omega}_{i,j} = \sum_{k \in \text{Overlap}(P_i, P_j)} 2^{k - L} \in [0, 2]$.

#### 10. `[ZH]` `[JSOI2009] 有趣的游戏` (Luogu P3311 / BZOJ 1444 — Interesting Game)
- **Statement & Constraints**: $m \le 10$ players each have a word $P_i$ of length $L \le 10$ over an alphabet of size $\sigma \le 10$, where character $c$ is generated with given probability $p_c = a_c / b_c$. Find the winning probability of each player.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Biased character probabilities $p_c \ne 1/\sigma$; works both as an AC Markov absorption test ($V \le 100$) and as a biased-PGF verification of (84.5) where $\Omega_{i,j} = \sum_{k \in \text{Overlap}(P_i, P_j)} \frac{1}{\Pr(P_j[1..k])}$.
  2. *Combinatorial Invariant*: If any character in $P_i$ has $p_c = 0$, $P_i$ can never win ($\pi_i = 0$); for positive probabilities, biased martingale bets multiply by $1/p_c$ on each matched character.
  3. *Algorithmic Compilation*: Either solve the $(m+1) \times (m+1)$ biased PGF system (after removing unreachable zero-probability patterns) or run Gaussian elimination on the $V \le 100$ AC states.
  4. *Pitfall*: Zero-probability characters $p_c = 0$ cause division by zero in $\frac{1}{\Pr(P_j[1..k])}$ if patterns containing $c$ are not pruned first!

#### 11. `[ZH]` `[SDOI2014] 数数` (Luogu P3311 — Digit Counting with Forbidden Substrings)
- **Statement & Constraints**: Given an upper bound $N \le 10^{1200}$ (as a decimal string) and $m$ forbidden digit strings $P_i$ with $\sum |P_i| \le 1500$, count integers in $[1, N]$ whose decimal representation contains no $P_i$ modulo $10^9+7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Coupling **Digit DP** (tracking `tight` prefix bound and `leading_zero` flag) with **Aho–Corasick Automaton DP**.
  2. *Combinatorial Invariant*: Leading zeros before the first nonzero digit of $x \in [1, N]$ are **not** part of the decimal string of $x$! Thus, while `leading_zero == true` and we place digit `0`, the AC automaton must stay at root `u = 0` rather than stepping along `ch[0][0]`.
  3. *Algorithmic Compilation*: Build AC automaton on $\mathcal{P}$, propagate `bad[u] |= bad[fail[u]]`, run Digit DP with state `(pos, ac_node, tight, started)` in $O(|N| \cdot 10 \cdot \sum |P_i|)$.
  4. *Pitfall*: Advancing `ac_node` on leading zeros falsely rejects numbers when a forbidden pattern starts with `'0'`.

#### 12. `[ZH]` `[BZOJ 3864] Hero meet devil` (LCS `DP套DP` Canonical Archetype)
- **Statement & Constraints**: Given a DNA string $S \in \{\texttt{A}, \texttt{C}, \texttt{G}, \texttt{T}\}^K$ with $K = |S| \le 15$ and length $n \le 1000$, for every $0 \le k \le K$ count how many DNA strings $W$ of length $n$ satisfy $\text{LCS}(S, W) = k$ modulo $10^9+7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Counting unknown strings $W$ by the output of an inner DP $\text{LCS}(S, W)$ with $K \le 15$.
  2. *Combinatorial Invariant*: The inner DP row $dp_{\text{inner}}[i][0..K]$ has adjacent differences $\Delta_j = dp_{\text{inner}}[i][j] - dp_{\text{inner}}[i][j-1] \in \{0, 1\}$, bijecting with a $K$-bit mask $M \in [0, 2^K)$, where $\text{LCS}(S, W) = \text{popcount}(M)$.
  3. *Algorithmic Compilation*: Precompute `trans[M][c]` for all $M \in [0, 2^K)$ and $c \in \{0..3\}$ in $O(K \cdot 4 \cdot 2^K)$; run outer rolling DP $dp[i][M]$ in $O(n \cdot 4 \cdot 2^K)$ and group $dp[n][M]$ by `__builtin_popcount(M)`.
  4. *Pitfall*: Computing the inner DP transition inside the $O(n \cdot 2^K)$ loop instead of precomputing `trans[M][c]` adds an extra factor of $K = 15$ and causes TLE.

#### 13. `[ZH]` `[TJOI2018] 游园会` (Luogu P4590 — Party / Product Automaton `DP套DP`)
- **Statement & Constraints**: Same as `BZOJ 3864` ($K \le 15$, $n \le 1000$), over alphabet $\{\texttt{N}, \texttt{O}, \texttt{I}\}$, with the extra constraint that $W$ must **not** contain $\texttt{NOI}$ as a contiguous substring.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Requires simultaneous tracking of non-contiguous subsequence LCS (`DP套DP` mask $M \in [0, 2^K)$) and contiguous substring avoidance ($\texttt{NOI}$ KMP automaton $q \in \{0, 1, 2\}$).
  2. *Combinatorial Invariant*: Because deterministic automata are closed under Cartesian product, the combined state $(M, q) \in [0, 2^K) \times \{0, 1, 2\}$ is a deterministic automaton of size $3 \cdot 2^K \le 98{,}304$.
  3. *Algorithmic Compilation*: Precompute `trans_mask[M][c]` and `trans_kmp[q][c]`; run rolling outer DP $dp[i \ \& \ 1][M][q]$ discarding transitions where `trans_kmp[q][c] == 3`.
  4. *Pitfall*: Memory limit is tight ($128$ MB)—must use rolling array `dp[2][1 << K][3]` instead of `dp[n + 1][1 << K][3]`.

#### 14. `[EN]` `Codeforces 86C — Genetic Engineering` (AC Coverage Automaton DP)
- **Statement & Constraints**: Given $n \le 1000$ and $m \le 10$ DNA patterns $P_i$ of length $\le 10$, count strings $W$ of length $n$ such that **every single character** of $W$ is covered by at least one occurrence of some $P_i \in \mathcal{P}$, modulo $10^9+9$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Not avoidance, but **100% tile coverage** by overlapping patterns of length $\le L_{\max} = 10$.
  2. *Combinatorial Invariant*: At prefix $W[1..i]$, we only need to know the AC state $u$ AND the number of trailing uncovered characters $d \in [0, L_{\max})$ at the right end of $W[1..i]$. If $d$ ever exceeds $|P_{\max}|$, those uncovered characters can never be covered by any future pattern! Whenever we enter state $u$, let $\text{max\_len}[u]$ be the length of the longest pattern in $\mathcal{P}$ that is a suffix of $u$ (propagated down the fail tree via `max_len[u] = max(max_len[u], max_len[fail[u]])`). If $\text{max\_len}[u] \ge d + 1$, all $d+1$ trailing characters become covered ($d' = 0$); otherwise $d' = d + 1$.
  3. *Algorithmic Compilation*: Run DP on state `(i, u, d)` over $n \times 100 \times 10$ states; sum $dp[n][u][0]$ over all $u$.
  4. *Pitfall*: Checking `max_len[u] >= d` instead of `max_len[u] >= d + 1` (after appending the $(i+1)$-th character, there are $d+1$ uncovered characters that must be spanned by the pattern ending at $i+1$).

#### 15. `[JA]` `AtCoder ARC 081 E — Don't Be a Subsequence` / `ABC 299 G` (Subsequence / Automaton Shortest Non-Subsequence & Counting)
- **Statement & Constraints**: Given string $S$ ($|S| \le 2 \times 10^5$), find the lexicographically smallest (or count all shortest) string over `'a'..'z'` that is NOT a subsequence of $S$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Bridges substring automata (AC/SAM) and subsequence automata (DASG, detailed in Wave 4B), showing how shortest avoiding strings correspond to BFS/DAG shortest paths to the dead sink state $\perp$.
  2. *Combinatorial Invariant*: In the subsequence automaton of $S$ where $\delta(i, c)$ is the first occurrence of $c$ after index $i$, strings NOT occurring as subsequences of $S$ are precisely paths from root $0$ to the sink state $\perp = |S|+1$.
  3. *Algorithmic Compilation*: Compute $dp[i] = 1 + \min_{c} dp[\delta(i, c)]$ backward from $i = |S|$ to $0$ in $O(|S| |\Sigma|)$ and reconstruct greedily.
  4. *Pitfall*: Treating $\perp$ as unreachable rather than an explicit terminal state at distance $0$.

#### 16. `[EN]` `ICPC World Finals 2012 — Fibonacci Words` / `Codeforces 55E / String Periodicity PGFs` (or `UVa 11468 — Substring`)
- **Statement & Constraints** (`UVa 11468`): Given $m \le 20$ patterns of length $\le 20$, character probabilities $p_c$, and length $n \le 100$, find the probability that a random string of length $n$ contains none of the $m$ patterns.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Evaluates $[z^n] G(z)$ (survival probability at step $n$) on a biased alphabet.
  2. *Combinatorial Invariant*: Either run biased AC automaton DP $dp[i][u]$ where transition $(u, c)$ multiplies by $p_c$, or extract $[z^n] G(z)$ from the biased Goulden–Jackson rational function.
  3. *Algorithmic Compilation*: Build AC automaton, propagate `bad[u]`, run $O(n V \sigma)$ probability DP.
  4. *Pitfall*: Floating-point precision loss if $n$ is large and probabilities are tiny, fixed by keeping state probabilities normalized or using exact fractions when required.

---

### Tier 3: Advanced (Goulden–Jackson Cluster Systems, Bivariate $k$-Occurrence GFs, Variance PGFs & DFA-Minimized `DP套DP`)

#### 17. `[EN]` `Codeforces 1096G / 1718D / Universal Cup & Gym — Multi-Pattern Avoidance for Huge Length ($n \le 10^5, m \le 15, |P_i| \le 10^5$)` (Goulden–Jackson + Bostan–Mori Archetype, e.g., `QOJ / Gym — Forbidden Patterns with Long Strings`)
- **Statement & Constraints**: Given $m \le 15$ binary patterns $P_1, \dots, P_m$ each of length up to $L \le 5000$ (or $|P_1| \le 10^5$ for $m=1$) and $n \le 10^{18}$ (or $n \le 10^5$), compute the number of strings of length $n$ avoiding all $P_i$ modulo $998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Total AC states $\sum |P_i| \le 75{,}000$ makes $O(V^3 \log n)$ AC matrix exponentiation impossible, while $m \le 15$ is tiny!
  2. *Combinatorial Invariant*: By the Goulden–Jackson Cluster Method (Iteration 83), after reducing $\mathcal{P}$ to an antichain, the avoidance OGF is $A(x) = \bigl(1 - \sigma x - \sum_{i=1}^m C_i(x)\bigr)^{-1}$ where $\sum_{i=1}^m C_i(x) C_{i,j}(x) = -x^{|P_j|}$.
  3. *Algorithmic Compilation*:
     - Remove any $P_j$ that contains another $P_i$ via AC / KMP in $O(\sum |P_i|)$.
     - Compute all $m^2$ overlap polynomials $C_{i,j}(x)$ using KMP / Z-algorithm in $O(m^2 L)$.
     - Solve the $m \times m$ polynomial linear system (via Gaussian elimination over $\mathbb{F}_p[[x]] \bmod x^{n+1}$ using NTT polynomial inverses in $O(m^3 L \log L + n \log n)$, or compute the exact rational function $P(x)/Q(x)$ of degree $\le \sum |P_i|$ and apply Bostan–Mori in $O(D \log D \log n)$).
  4. *Pitfall*: Attempting to invert $C_{i,j}(x)$ for $i \ne j$ as pivot in Gaussian elimination over $\mathbb{F}_p[[x]]$ fails because $C_{i,j}(0) = 0$ is NOT a unit! Always pivot on the diagonal $C_{j,j}(x)$ since $C_{j,j}(0) = 1$ is guaranteed to be a unit!

#### 18. `[EN]` `Codeforces 1764G / CF 1019E / Codeforces Gym 102538 (SJTU) — Expected Hitting Time & Variance of Pattern Stopping` (`Var(T_S)` via PGF `F''(1)`)
- **Statement & Constraints**: Given a pattern $S$ of length $L \le 10^6$ over an alphabet of size $\sigma$ with biased character probabilities $p_c$, compute both the expected stopping time $\mathbb{E}[T_S]$ and the **variance** $\text{Var}(T_S) \bmod 998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Conway's simplest $\$1$-bet martingale gives $\mathbb{E}[T_S]$ directly, but how do you get $\text{Var}(T_S) = \mathbb{E}[T_S^2] - (\mathbb{E}[T_S])^2$ in $O(L)$ time?
  2. *Combinatorial Invariant*: By double differentiation of the PGF system $(1 - z)G(z) + F(z) = 1$ and $G(z) = F(z) \sum_{k \in \text{Borders}(S)} \frac{z^{-k}}{\Pr(S[1..k])}$ at $z = 1$ (Equation (84.4)),
     $$\text{Var}(T_S) = (\mathbb{E}[T_S])^2 + \mathbb{E}[T_S] - 2 \sum_{k \in \text{Borders}(S)} \frac{k}{\Pr(S[1..k])}.$$
  3. *Algorithmic Compilation*: Compute KMP `pi` array of $S$ and prefix probability products $\Pr(S[1..k])$ in $O(L)$; walk the border chain $k = L, \pi[L], \dots > 0$ accumulating both $S_0 = \sum \frac{1}{\Pr(S[1..k])}$ and $S_1 = \sum \frac{k}{\Pr(S[1..k])}$; output $(S_0^2 + S_0 - 2 S_1) \bmod 998244353$.
  4. *Pitfall*: Confusing $F''(1) = \mathbb{E}[T_S(T_S - 1)]$ with $\mathbb{E}[T_S^2]$ and dropping the $+\mathbb{E}[T_S]$ term in $\text{Var}(T_S) = F''(1) + F'(1) - (F'(1))^2$.

#### 19. `[ZH]` `[SDOI2019] 移动金币 / [ZJOI2019] 麻将` (Luogu P5279 — Mahjong, DFA-Minimized `DP套DP` Classic)
- **Statement & Constraints**: In $14$-tile Mahjong with $n \le 100$ tile types ($4$ copies each), a winning hand is either $7$ distinct pairs OR $1$ pair + $4$ melds (triplets/chow sequences). Given $13$ initial tiles, find the expected number of random draws from the remaining wall until the subset of drawn tiles contains a winning $14$-tile hand, modulo $998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: To compute expected stopping time $\mathbb{E}[T] = \sum_{k \ge 0} \Pr[T > k]$, we must count hands of size $k$ that do **not** yet contain a winning sub-hand. Checking whether a tile count array $(c_1, \dots, c_n) \in \{0..4\}^n$ contains a winning hand is itself a DP!
  2. *Combinatorial Invariant*: The inner DP scans tile types $1 \to n$, tracking a $3 \times 3$ matrix $M_{a,b}$ (maximum number of completed melds given $a \in \{0,1,2\}$ open `[i-1, i]` sequences and $b \in \{0,1,2\}$ open `[i]` sequences) for both "no pair yet" (`dp0`) and "has pair" (`dp1`), plus total distinct pair count $p \in [0, 7]$. Capping values at $\le 4$ melds and $\le 7$ pairs, BFS exploration from the initial inner state discovers only **$2092$ reachable non-winning DFA states**!
  3. *Algorithmic Compilation*: Run BFS over tile counts $c \in \{0..4\}$ to construct the $2092$-state **Mahjong Automaton**; then run the outer knapsack DP over the $n$ tile types and total drawn tiles $k \in [0, 4n-13]$ in $O(n^2 \cdot 2092)$ time.
  4. *Pitfall*: Failing to cap inner DP meld counts at $4$ (and set all winning states to a single absorbing state $\top$) explodes the BFS state count past $10^5$.

#### 20. `[EN]` `Codeforces 1119H / CF 954I / Codeforces 1392H / Exact $k$-Occurrence Pattern Counting via Bivariate Goulden–Jackson` (e.g., `TopCoder SRM — ExactSubstrings` / `QOJ — Strings with Exactly K Occurrences`)
- **Statement & Constraints**: Given a pattern $P$ of length $L \le 5000$, alphabet size $\sigma$, string length $n \le 10^5$, and $k \le n$, count strings of length $n$ containing **exactly $k$** (possibly overlapping) occurrences of $P$ modulo $998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $L \le 5000$ and $n \le 10^5$ prevents $O(n L k)$ KMP-state DP; we need the bivariate cluster GF $[x^n t^k] F(x, t)$.
  2. *Combinatorial Invariant*: By Formula (86.5), for $k \ge 1$ the exact OGF is
     $$A^{(k)}(x) = \frac{x^L \Bigl((1 - \sigma x)\bigl(C_P(x) - 1\bigr) + x^L\Bigr)^{k-1}}{\Bigl((1 - \sigma x) C_P(x) + x^L\Bigr)^{k+1}},$$
     where $C_P(x) = \sum_{r \in \text{Borders}(P)} x^{L-r}$ is computed in $O(L)$ via KMP.
  3. *Algorithmic Compilation*: Compute $C_P(x)$ from KMP `pi` array; form $D_0(x) = (1 - \sigma x)C_P(x) + x^L$ and $D_1(x) = (1 - \sigma x)(C_P(x) - 1) + x^L$ truncated $\bmod x^{n+1}$; compute $x^L D_1(x)^{k-1} D_0(x)^{-(k+1)} \bmod x^{n+1}$ using FPS `ln`/`exp` and polynomial inverse in $O(n \log n)$ regardless of $L$ and $k$!
  4. *Pitfall*: When $k = 0$, Formula (86.5) is NOT used—for $k = 0$, the answer is $[x^n] \frac{C_P(x)}{D_0(x)}$.

#### 21. `[JA]` `AtCoder AGC 022 E — Median Replace` (DFA Synthesis & Minimization for Recursive String Reduction)
- **Statement & Constraints**: Given a string $S \in \{\texttt{0}, \texttt{1}, \texttt{?}\}^{2N+1}$ ($2N+1 \le 3 \times 10^5$), a valid binary string can be reduced to `'1'` by repeatedly replacing any contiguous $3$-character substring with its median. Count ways to replace `'?'` with `'0'` or `'1'` so the string reduces to `'1'` modulo $10^9+7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A recursive $3$-to-$1$ reduction rule looks like interval DP $O(N^3)$, which fails for $N = 3 \times 10^5$; we must compile the greedy left-to-right stack reduction into a tiny minimal DFA!
  2. *Combinatorial Invariant*: Maintain a compressed stack of characters read so far:
     - Whenever `'1'` is already at the bottom of the stack with two `'1'`s (`"11"`), it is already a guaranteed win regardless of future characters!
     - Any adjacent `"01"` at the top of the stack after a `'0'` cancels (`"001" -> "0"`), and three `"000"` compress to `"0"`.
     - Thus, the reachable stack states form a **5-state minimal DFA** ($\epsilon, \texttt{0}, \texttt{00}, \texttt{1}, \texttt{10}, \texttt{100}, \texttt{11}$—only $7$ unminimized states, collapsing to $5$ Nerode equivalence classes)!
  3. *Algorithmic Compilation*: Hand-derive or BFS-minimize the $7$-state stack DFA, then run a simple $O(N)$ linear DP over $S$.
  4. *Pitfall*: Reducing `"10"` immediately without waiting for the third character—`"101"` becomes `"1"`, whereas `"100"` becomes `"0"`.

#### 22. `[JA]` `AtCoder AGC 020 E — Encoding Subsets` (Recursive Automaton / Interval Subset DP)
- **Statement & Constraints**: Given a binary string $S$ ($|S| \le 100$), count all valid run-length compressed encodings $(P \times k)$ of all strings $T \le S$ (bitwise $T_i \le S_i$) modulo $998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Repeating block $(P \times k)$ must dominate $k$ contiguous blocks of $T$, which means $P$ must be a subset of the **bitwise AND** of the $k$ slices of $S$!
  2. *Combinatorial Invariant*: The state space of all sub-strings closed under $(S[l..r])$ and bitwise AND of periodic slices shrinks rapidly by length: for length $L$, there are at most $\min(2^L, O(|S|^2/L))$ reachable strings, totaling $< 2000$ memoized states.
  3. *Algorithmic Compilation*: Memoized DP over string $U$: split $U$ into first block + rest, where first block is either a single character or $(V \times k)$ recursive call on $V = \bigwedge_{j=0}^{k-1} U[j d + 1 .. (j+1) d]$.
  4. *Pitfall*: Counting ambiguous factorizations twice if the first block is not restricted to be a single atomic unit (either 1 char or 1 parenthesized $(V \times k)$ with $k \ge 2$).

#### 23. `[ZH]` `[ZJOI2017] 字符串 / Lyndon Automaton & Lexicographical State DP` (`CF 1606F` / Duval Automaton Counting)
- **Statement & Constraints**: Count strings $W \in \{1..\sigma\}^n$ ($n \le 100$) whose Lyndon factorization $W = w_1 w_2 \dots w_k$ has exactly $k$ factors (or whose minimum cyclic shift is $W$ itself, or whose Duval algorithm makes exactly $c$ comparisons).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Duval's algorithm processes $W$ left-to-right maintaining pointers $(i, j, k)$ for the current pre-Lyndon word $W[i..k]$ of period $p = k - j$.
  2. *Combinatorial Invariant*: For counting Lyndon words or tracking the current pre-Lyndon prefix of length $L$ and period $p$, when we append character $c$:
     - If $c = W[k - p]$, the period $p$ is preserved!
     - If $c > W[k - p]$, the entire prefix of length $L+1$ becomes a **simple Lyndon word** with new period $p' = L+1$!
     - If $c < W[k - p]$, the pre-Lyndon word breaks into $\lfloor L/p \rfloor$ Lyndon factors of length $p$.
  3. *Algorithmic Compilation*: When the alphabet comparison only depends on how many choices of $c$ are $> W[k-p]$ vs. $= W[k-p]$, or by building the Duval state DP over `(len, period, min_char_info)`.
  4. *Pitfall*: Confusing a **pre-Lyndon word** (prefix of a periodic repetition of a Lyndon word, $p < L$) with a **Lyndon word** ($p = L$).

#### 24. `[EN]` `Codeforces 1349D — Slime and Biscuits` / `[CTSC2006] 歌唱王国 + Game Martingale Potential Synthesis`
- **Statement & Constraints**: Connects potential-function martingales on Markov chains with string stopping-time martingales: given a process stopping when all tokens or a target string configuration is reached, compute $\mathbb{E}[T]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Multi-target stopping time where each target $i$ can be analyzed by isolating its potential $\phi(X_t)$ so that $\phi(X_t) - t$ is a martingale until $T$.
  2. *Combinatorial Invariant*: By Optional Stopping, $\mathbb{E}[T] = \sum_{i} \pi_i \phi(\text{terminal } i) - \phi(X_0)$. In string pattern races, $\phi_j(\text{state } u) = \sum_{k \in \text{Overlap}(u, P_j)} \sigma^k$ is the exact potential function!
  3. *Algorithmic Compilation*: Construct the potential difference recurrence or overlap payoff matrix $\Omega_{i,j}$ and solve.
  4. *Pitfall*: Forgetting to subtract the initial potential $\phi(X_0)$ when the game starts from a non-empty initial prefix $S_0 \ne \epsilon$! (If the stream starts with a given seed string $S_0$, $\mathbb{E}[T]$ for target $P_j$ subtracts $\Omega_{S_0, P_j} = \sum_{k \in \text{Overlap}(S_0, P_j)} \sigma^k$, assuming $S_0$ has not already triggered a stop!)

---

### Tier 4: Mastery (Grandmaster Synthesis: Palindrome-Avoiding Automata, Non-Antichain Weighted Clusters, Minimal DFA Game Synthesis & $O(L \log L \log N)$ Cluster Bostan–Mori)

#### 25. `[JA]` `AtCoder AGC 064 C / ARC 141 D / Palindrome-Avoiding & PAM-State Automaton DP` (`CF 932G` + Automaton Avoidance Synthesis)
- **Statement & Constraints**: Count strings of length $n \le 10^{18}$ over alphabet $\sigma$ avoiding all palindromes of length $\ge K$ (where $K \le 10$), OR given a set of forbidden palindromic/general substrings, count strings avoiding both a given dictionary $\mathcal{P}$ and all even/odd palindromes of length $\ge K$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Every palindrome of length $\ge K$ contains a core palindrome of length **$K$ or $K+1$** centered at the same position!
  2. *Combinatorial Invariant*: Avoiding all palindromes of length $\ge K$ is equivalent to avoiding all palindromes of length $K$ and $K+1$. Rather than building an AC automaton on all $\sigma^{\lceil K/2 \rceil}$ palindromes, two prefixes of length $K$ are Myhill–Nerode equivalent up to alphabet permutation (Bell number $B_K$ states)!
  3. *Algorithmic Compilation*: Encode the last $K$ characters by their restricted growth string (canonical partition of $[1..K]$ by character equality, at most $B_{10} = 115{,}975$ states, or pruned to palindrome-free states $\ll 5000$), run Hopcroft DFA minimization to get $< 100$ states, and exponentiate the minimized transition matrix in $O(V_{\min}^3 \log n)$.
  4. *Pitfall*: Only forbidding palindromes of length $K$ (e.g., $K = 3$ forbids `aba`), which fails to forbid even-length palindromes of length $K+1 = 4$ (`abba` contains no length-$3$ palindrome!). You MUST forbid both $K$ and $K+1$.

#### 26. `[ZH]` `[NOI2020] 制作菜品 / [CTS2019] 随机立方体 / [WC2019] 数树` & `[国家集训队论文] Automatic DFA Construction for String Games (DP套DP + Hopcroft Minimization)` (e.g., `LOJ 3045 / UOJ — String Automaton Minimization`)
- **Statement & Constraints**: Given a string verification game (such as checking whether a string $W \in \{0, 1, 2\}^n$ can be reduced to $\epsilon$ under custom cancellation/rewriting rules, with $?'$ wildcards and $n \le 10^4$), count the number of valid completions of $W$ modulo $998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: The validity check for a fixed string $W$ is a known $O(n)$ DP, where each step maintains a subset of reachable states $S \subseteq Q_{\text{inner}}$ ($|Q_{\text{inner}}| \le 12$). Naive subset construction gives $2^{12} = 4096$ states, still somewhat slow for $n = 10^4$ with large constant, or $|Q_{\text{inner}}| = 18$ ($2^{18}$ states).
  2. *Combinatorial Invariant*: By the **Myhill–Nerode Theorem**, the minimal DFA recognizing the language has a unique canonical state space obtained by: (1) BFS subset construction from $\{q_0\}$ keeping only **reachable** subsets $S \subseteq Q_{\text{inner}}$, followed by (2) **Hopcroft's $O(|\Sigma| V \log V)$ partition refinement** starting from the two-block partition $\{F, V \setminus F\}$.
  3. *Algorithmic Compilation*: Run offline BFS + Hopcroft minimization to compress thousands of reachable inner-DP subsets into typically $V_{\min} \le 50$–$200$ states; then run the $O(n \cdot V_{\min})$ DP over the input string $W$.
  4. *Pitfall*: Skipping Hopcroft minimization when multiple distinct inner DP subsets have identical future acceptance behavior, leaving redundant isomorphic subgraphs that TLE the outer DP.

#### 27. `[EN]` `Universal Cup / QOJ — Expected Power of Pattern Occurrences $\mathbb{E}[\text{occ}(W)^K]$ in Long Strings` ($n \le 10^9, |P| \le 10^5, K \le 20$)
- **Statement & Constraints**: Given a pattern $P$ of length $L \le 10^5$, alphabet size $\sigma$, $n \le 10^9$, and $K \le 20$, compute $\sum_{W \in \Sigma^n} \text{occ}_P(W)^K \bmod 998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $|P| \le 10^5$ and $n \le 10^9$ rule out AC/KMP DP; $K \le 20$ asks for the $K$-th moment at $t = 1$ of the bivariate Goulden–Jackson generating function $F(x, t) = \sum_{W} x^{|W|} t^{\text{occ}_P(W)}$.
  2. *Combinatorial Invariant*: Substitute $t = 1 + u$ into the bivariate cluster GF (86.3)! Because $t - 1 = u$, Equation (86.3) in $u = t - 1$ is:
     $$F(x, 1 + u) = \frac{1 - u\bigl(C_P(x) - 1\bigr)}{1 - \sigma x - u \Bigl((1 - \sigma x)\bigl(C_P(x) - 1\bigr) + x^L\Bigr)} = \frac{1}{1 - \sigma x} + \sum_{j \ge 1} u^j \, \frac{x^L \Bigl((1 - \sigma x)\bigl(C_P(x) - 1\bigr) + x^L\Bigr)^{j-1}}{(1 - \sigma x)^{j+1}}!$$
     Look at $[u^j] F(x, 1+u)$: it equals $\sum_{W \in \Sigma^*} \binom{\text{occ}_P(W)}{j} x^{|W|}$, and its denominator is simply $(1 - \sigma x)^{j+1}$ (**NOT** $D_0(x)^{j+1}$)!
  3. *Algorithmic Compilation*:
     - Using Stirling numbers of the second kind, $\text{occ}^K = \sum_{j=0}^K \left\{ \begin{matrix} K \\ j \end{matrix} \right\} j! \binom{\text{occ}}{j}$.
     - Notice that $C_P(x) - 1$ has degree $< L$, so in $[u^j] F(x, 1+u)$, the numerator $x^L \bigl((1 - \sigma x)(C_P(x) - 1) + x^L\bigr)^{j-1}$ is a sparse polynomial of degree $\le j L \le 20 \times 10^5$, and dividing by $(1 - \sigma x)^{j+1}$ means $[x^n] [u^j] F(x, 1+u)$ is just a **weighted sum of binomial coefficients** $\sum_{d} c_d \binom{n - d + j}{j} \sigma^{n - d}$, computable in $O(K L \log(KL))$ via NTT!
  4. *Pitfall*: Expanding in powers of $t$ around $t = 0$ (which has complicated denominator $D_0(x)^{k+1}$ of degree $(k+1)L$ requiring Bostan–Mori) instead of expanding in $u = t - 1$ around $t = 1$ (where the denominator collapses to $(1 - \sigma x)^{j+1}$!). This $t = 1 + u$ shift is the single most powerful algebraic trick in Wave 4A!

#### 28. `[ZH]` `[THUPC / QOJ / UOJ] 多模式串出现次数乘积 / Non-Antichain Weighted Cluster System`
- **Statement & Constraints**: Given $m \le 8$ patterns $P_1, \dots, P_m$ of lengths up to $L \le 2000$ (where some $P_i$ MAY be substrings of $P_j$, or where each $P_i$ has formal variable $t_i$) and $n \le 10^5$, find the coefficient of $x^n t_1^{k_1} \dots t_m^{k_m}$ (with $\sum k_i \le 10$) or evaluate the weighted sum where each occurrence of $P_i$ multiplies weight by $w_i \in \mathbb{F}_p$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Each occurrence of $P_i$ multiplies the string's weight by a known scalar $w_i \in \mathbb{F}_p \setminus \{1\}$ (or $w_i = 1$, which can be discarded since multiplying by $1$ has no effect!). What if $P_1$ is a contiguous substring inside $P_2$?
  2. *Combinatorial Invariant*: In the marked-word expansion $\prod_{e \in \text{Occ}(W)} (1 + (w_{e} - 1))$, we do NOT need $\mathcal{P}$ to be an antichain if we allow a cluster to be a connected component of marked intervals where an interval $P_i$ strictly inside $P_j$ simply gets absorbed into $P_j$'s effective weight! Specifically, once $P_j$ is marked, any occurrence of $P_i$ that lies **completely inside** $P_j$ adds no new characters to the union of intervals, so summing over whether that internal occurrence of $P_i$ is marked ($w_i - 1$) or unmarked ($1$) simply multiplies the weight of marking $P_j$ by $(1 + (w_i - 1)) = w_i$! What if an occurrence of $P_i$ is contained inside the *overlap* of $P_a$ and $P_b$ of length $k$? Then it was counted in both $P_a$'s internal product and $P_b$'s internal product, so the overlap transition $C_{a,b}$ divides by $w_i$ for every $P_i$ completely contained inside the overlap $P_b[1..k]$!
  3. *Algorithmic Compilation*:
     - For each pattern $P_j$, replace its base weight by $\widetilde{W}_j = (w_j - 1) \prod_{P_i \subsetneq P_j} w_i^{\text{occ}(P_i, P_j)}$.
     - For each proper prefix-suffix overlap $k \in \text{Overlap}(P_a, P_b)$ ($1 \le k < \min(|P_a|, |P_b|)$) such that the union interval has length $|P_a| + |P_b| - k > \max(|P_a|, |P_b|)$, multiply $x^{|P_b| - k}$ by $\prod_{P_i \text{ straddling } k} w_i / \prod_{P_i \subseteq P_b[1..k]} w_i$ (the exact change in internal occurrences when gluing $P_a$ and $P_b$ at overlap $k$).
     - Solve the $m \times m$ polynomial linear system and extract $[x^n] F(x)$.
  4. *Pitfall*: Applying the naive antichain Goulden–Jackson system without accounting for internal occurrences of shorter patterns inside longer patterns or inside overlaps when $w_i \ne 0$.

#### 29. `[EN]` `Codeforces 1608F — MEX Counting` / `CF 1142E` / `Automaton DP with Deferred Alphabet Assignment (Open-Class DFA DP)`
- **Statement & Constraints**: Count strings/arrays of length $n \le 2000$ over an alphabet where characters are only compared by equality or MEX/canonical first-appearance order, coupled with an inner automaton transition.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: When the alphabet $\Sigma$ is large ($\sigma \le 10^9$) and the string condition only depends on **equality** between positions (such as canonical partition / palindrome / border structure), tracking actual characters is impossible.
  2. *Combinatorial Invariant*: Track the number of distinct characters seen so far (or deferred "anonymous" equivalence classes) and resolve their distinctness when the automaton closes a class.
  3. *Algorithmic Compilation*: Combine canonical restricted-growth string transitions with deferred combinatorics ($\binom{\sigma - c}{k}$).
  4. *Pitfall*: Overcounting permutations of unused alphabet symbols.

#### 30. `[ZH]` `[ZJOI2019] 开关` / `[WC2018] 州区划分` / `String PGF + Exponential Generating Function Stop-Time Synthesis` (`LOJ 3042` / Random Walk to String Target with Reset)
- **Statement & Constraints**: A string generator appends random characters, or with probability $p_0$ resets (or edits the last character), until pattern $S$ ($|S| \le 10^5$) is formed. Compute the expected time to form $S$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Non-standard step transitions (such as backspacing or resetting) break the naive $\sigma^k$ fair-bet multiplier, requiring a modified martingale bet multiplier or tridiagonal KMP elimination.
  2. *Combinatorial Invariant*: On the KMP automaton of $S$, every backward fail transition goes to $\text{anc}(u)$ while only $1$ character $S[u+1]$ advances $u \to u+1$. Thus $E[u] - E[u+1]$ can always be expressed as a linear combination of $E[\text{anc}]$ along the KMP fail tree, solvable in $O(|S|)$ time from $u = 0$ to $|S|-1$!
  3. *Algorithmic Compilation*: Maintain $dp[u] = E[u] - E[u+1]$ (the expected time to advance from KMP state $u$ to $u+1$) in $O(|S| \sigma)$ or $O(|S|)$ using the KMP transition table, then sum $\sum_{u=0}^{|S|-1} dp[u]$.
  4. *Pitfall*: Trying to apply $\sum_{k \in \text{Borders}(S)} \sigma^k$ blindly when the random process allows backspaces or state-dependent transition probabilities!

#### 31. `[JA]` `AtCoder AGC 058 D — Yet Another ABC String` (Cluster Inclusion–Exclusion on Cyclic / 3-Letter Forbidden Blocks)
- **Statement & Constraints**: Given $A, B, C \le 10^6$, count strings containing $A$ copies of `'A'`, $B$ copies of `'B'`, and $C$ copies of `'C'` that contain **none** of the three cyclic substrings `"ABC"`, `"BCA"`, `"CAB"`, modulo $998244353$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Multi-variable exact character count ($x^A y^B z^C$) with forbidden pattern set $\mathcal{P} = \{\texttt{ABC}, \texttt{BCA}, \texttt{CAB}\}$.
  2. *Combinatorial Invariant*: Apply the Goulden–Jackson cluster decomposition directly to $\mathcal{P} = \{\texttt{ABC}, \texttt{BCA}, \texttt{CAB}\}$! Notice how patterns in $\mathcal{P}$ overlap:
     - `"ABC"` overlapped with `"BCA"` gives `"ABCA"` (length 4), `"ABCAB"` (length 5), `"ABCABC"` (length 6), etc.
     - In fact, ANY valid cluster of overlapping marked patterns from $\{\texttt{ABC}, \texttt{BCA}, \texttt{CAB}\}$ is simply a contiguous cyclic run of `"ABCABC..."` of length $L \ge 3$!
     - What is the total cluster weight $w_L$ of a cyclic run of length $L$? By the single-variable cluster GF (since shifting the cyclic start by 1 is isomorphic):
       $$\sum_{L \ge 3} w_L x^L = \frac{-3 x^3}{1 + x + x^2} = -3 x^3 (1 - x + x^3 - x^4 + x^6 - x^7 + \cdots)!$$
       Look at the coefficients: a cluster of length $L = 3k$ has weight $-3 (-1)^{k-1} = 3(-1)^k$ (and uses exactly $k$ `'A'`s, $k$ `'B'`s, $k$ `'C'`s!), while a cluster of length $L = 3k + 1$ has weight $+3 (-1)^{k-1} = -3(-1)^k$ (using $k$ of each plus $1$ extra character of the starting letter, so summing over the 3 starting letters contributes $-(-1)^k (x + y + z) (xyz)^k$), and length $L = 3k + 2$ has weight **$0$**!
  3. *Algorithmic Compilation*: Every cluster of weight $\ne 0$ has length $3k$ (weight $3(-1)^k (xyz)^k$) or $3k+1$ (weight $-(-1)^k (x+y+z)(xyz)^k$). Summing over the number $m$ of clusters in the marked word reduces the entire 3-variable count to a single $O(\min(A, B, C))$ loop of multinomial coefficients!
  4. *Pitfall*: Trying to run 3D DP instead of noticing that the cluster polynomial $1 + x + x^2$ cancels all $3k+2$ clusters to zero and balances the counts of `'A'`, `'B'`, `'C'` inside every cluster of length $3k$!

#### 32. `[EN]` `ICPC World Finals 2016 — String Theory` / `QOJ — Minimal DFA of Palindromic / Border Game (`DP套DP` Mastery)`
- **Statement & Constraints**: Given a two-player game or multi-level structural decomposition on a string $W \in \Sigma^n$ with wildcard characters `'?'`, count the number of assignments to `'?'` such that the first player wins (or the string is a valid $k$-quotation / square-free / border-winning string).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Counting wildcard completions where the predicate is a game-theoretic winning condition ($\text{sg}(W) > 0$) on prefixes/substrings.
  2. *Combinatorial Invariant*: Build the inner DP that computes the Sprague–Grundy tuple for a fixed string left-to-right, cap the tuple coordinates, and run BFS + Hopcroft DFA minimization to extract the exact finite automaton of winning states.
  3. *Algorithmic Compilation*: Offline automaton discovery $\to$ transition table hardcoding or runtime BFS $\to$ $O(n \cdot V_{\min})$ outer DP.
  4. *Pitfall*: Forgetting that trailing conditions at index $n$ (such as closing open quotation levels) determine the accepting set $F \subseteq V$ of the inner DFA.

---

### 87.2 Quarantine Table (`R-4A-01` to `R-4A-08` — Excluded Pure Template Problems)

Per `AGENTS.md` and `strings_research/PLAN.md`, problems whose sole task is implementing a bare Aho–Corasick automaton, KMP matcher, or polynomial division template without a structural cluster/martingale/`DP套DP` reduction are strictly quarantined from the textbook chapters:

| Quarantine ID | Source & Problem Name | Reason for Quarantine |
| :--- | :--- | :--- |
| **`R-4A-01`** | Luogu P3808 — `【模板】AC 自动机（简单版）` | Pure Aho–Corasick construction & single-pass matching template. |
| **`R-4A-02`** | Luogu P3796 — `【模板】AC 自动机（加强版）` | Standard AC occurrence counting template without DP or GF structure. |
| **`R-4A-03`** | Luogu P5357 — `【模板】AC 自动机（二次加强版）` | Standard AC fail-tree subtree sum template; belongs in baseline library prerequisites. |
| **`R-4A-04`** | Library Checker — `KMP / Z Algorithm` | Pure border/prefix-match array verification with zero combinatorial modeling. |
| **`R-4A-05`** | Luogu P3375 — `【模板】KMP` | Baseline KMP template assumed in reader's library. |
| **`R-4A-06`** | Library Checker — `Find Linear Recurrence / Kth Term of Linearly Recurrent Sequence` | Pure Berlekamp–Massey / Bostan–Mori algebra template (covered in FPS textbook). |
| **`R-4A-07`** | HDU 2222 — `Keywords Search` | Bare Aho–Corasick textbook template problem. |
| **`R-4A-08`** | POJ 1204 — `Word Puzzles` | 2D grid Aho–Corasick search implementation exercise with no theoretical reduction. |

---

### 87.3 Wave 4A Synthesis Checklist & Cross-Cohort Handoff Notes

1. **Unification of Iterations 83, 84, and 86**:
   - Notice that the **Goulden–Jackson Overlap Matrix** $C_{i,j}(x) = \sum_{k \in \text{Overlap}(P_i, P_j)} x^{|P_j| - k}$ (at $x = \sigma^{-1}$ multiplied by $\sigma^{|P_j|}$) is **identical** up to diagonal scaling to the **Conway Martingale Payoff Matrix** $\Omega_{i,j} = \sum_{k \in \text{Overlap}(P_i, P_j)} \sigma^k = \sigma^{|P_j|} C_{i,j}(\sigma^{-1})$!
   - Why? Because the probability generating function $G(z)$ of surviving strings at step $n$ is simply the ordinary avoidance generating function $A(x)$ evaluated at $x = z / \sigma$:
     $$G(z) = A\!\left(\frac{z}{\sigma}\right)!$$
   - Presenting this exact algebraic bridge in Chapter 18 unifies combinatorial string avoidance (Goulden–Jackson), probabilistic stopping times (PGFs), and fair casino martingales (`康威赌博`) as three facets of a single overlap linear system!
2. **The $t = 1 + u$ Binomial Moment Trick (Problem 27 & `AGC 058 D`)**:
   - Expanding the bivariate Goulden–Jackson GF around $t = 1$ ($u = t - 1$) instead of $t = 0$ collapses the denominator from $((1 - \sigma x)C_P(x) + x^L)^{j+1}$ to $(1 - \sigma x)^{j+1}$, turning $K$-th moment occurrence queries on $n \le 10^{18}$ into $O(K L \log(KL))$ polynomial convolutions.
3. **Hopcroft Minimization as a First-Class Tool in `DP套DP`**:
   - Every `DP套DP` problem should be taught as a 3-stage compiler pipeline: (1) design a capped/relative-offset inner DP, (2) run BFS from the initial inner state to discover reachable states, and (3) run Hopcroft DFA minimization to quotient by Myhill–Nerode equivalence before running the outer DP or matrix exponentiation.


---

### 87.4 Algorithmic Decision Matrix: Choosing Between AC Transfer Matrix, Goulden–Jackson Cluster System, and `DP套DP`

| Problem Regime | Best Structural Tool | Time Complexity | Why Competing Approaches Fail |
| :--- | :--- | :--- | :--- |
| $\sum |P_i| \le 200$, $n \le 10^{18}$, arbitrary pattern containment | **AC Safe Transfer Matrix + Matrix Exponentiation** | $O(V^3 \log n)$ where $V \le \sum |P_i| + 1$ | Goulden–Jackson requires antichain reduction or non-antichain overlap weights; at $V \le 100$, direct AC matrix power is simpler. |
| $m \le 15$, $|P_i| \le 10^5$, $n \le 10^{18}$, pure avoidance | **Goulden–Jackson $m \times m$ System + Bostan–Mori** | $O(\sum |P_i| + m^3 L \log L + D \log D \log n)$ where $D = \sum |P_i|$ | AC automaton has $V = O(\sum |P_i|) \approx 10^6$ states; $O(V^3)$ matrix exponentiation is impossible. |
| $m = 1$, $|P| \le 10^5$, $n \le 10^5$, exact $k$ occurrences | **Bivariate Guibas–Odlyzko GF $[t^k] F(x, t)$ (Eq. 86.5)** | $O(L + n \log n)$ via FPS `ln`/`exp`/inv | Tracking $k$ occurrences on KMP takes $O(n L k)$ time. |
| $m = 1$, $|P| \le 10^5$, $n \le 10^{18}$, $\mathbb{E}[\text{occ}^K]$ for $K \le 20$ | **$t = 1 + u$ Binomial Moment Shift around $t = 1$** | $O(K L \log(KL))$ via NTT + Stirling numbers | Expanding around $t = 0$ has denominator $D_0(x)^{k+1}$ of degree $k L$; shifting $t = 1 + u$ collapses denominator to $(1 - \sigma x)^{j+1}$! |
| $m \le 300$, $|P_i| \le 300$, stopping-time pattern race | **Conway Martingale / PGF $(m+1) \times (m+1)$ System (Eq. 84.5)** | $O(m^2 L + m^3)$ | AC Markov chain has $90{,}000$ states; Gaussian elimination on AC states takes $O((mL)^3)$. |
| Unknown string $W$ of length $n \le 10^4$ constrained by inner DP $f(S, W)$ ($|S| \le 15$) | **`DP套DP` (Difference-Mask / Capped Inner State BFS + Hopcroft Minimization)** | $O(|\Sigma| V \log V + n |\Sigma| V_{\min})$ | Naive outer DP has $(K+1)^K$ states; difference encoding + Myhill–Nerode minimization shrinks $V_{\min}$ to $\le 2^K$ or a few hundred states. |

---

### 87.5 Worked Mini-Trace: Hopcroft Partition Refinement on an Inner DP Automaton

Suppose an inner verification DP for a string reduction rule produces $V = 6$ reachable subset states $\{q_0, q_1, q_2, q_3, q_4, q_5\}$ over $\Sigma = \{\texttt{0}, \texttt{1}\}$ with accepting states $F = \{q_3, q_4, q_5\}$ and transition table:

| State $u$ | $\delta(u, \texttt{0})$ | $\delta(u, \texttt{1})$ | Accepting? |
| :--- | :--- | :--- | :--- |
| $q_0$ | $q_1$ | $q_3$ | No |
| $q_1$ | $q_2$ | $q_4$ | No |
| $q_2$ | $q_2$ | $q_5$ | No |
| $q_3$ | $q_1$ | $q_3$ | **Yes** |
| $q_4$ | $q_2$ | $q_4$ | **Yes** |
| $q_5$ | $q_2$ | $q_5$ | **Yes** |

1. **Initial Partition ($\Pi_0$)**: Split into non-accepting $B_0 = \{q_0, q_1, q_2\}$ and accepting $B_1 = \{q_3, q_4, q_5\}$.
2. **First Refinement Step**:
   - Check transitions from $B_0 = \{q_0, q_1, q_2\}$:
     - On `'0'`: $\delta(q_0, \texttt{0}) = q_1 \in B_0$, $\delta(q_1, \texttt{0}) = q_2 \in B_0$, $\delta(q_2, \texttt{0}) = q_2 \in B_0$ (all stay in $B_0$).
     - On `'1'`: $\delta(q_0, \texttt{1}) = q_3 \in B_1$, $\delta(q_1, \texttt{1}) = q_4 \in B_1$, $\delta(q_2, \texttt{1}) = q_5 \in B_1$ (all go to $B_1$).
   - Check transitions from $B_1 = \{q_3, q_4, q_5\}$:
     - On `'0'`: all go to $\{q_1, q_2\} \subseteq B_0$.
     - On `'1'`: all go to $\{q_3, q_4, q_5\} \subseteq B_1$.
3. **Fixed Point Reached ($\Pi_1 = \Pi_0$)**:
   Neither $B_0$ nor $B_1$ is split by any character $c \in \{\texttt{0}, \texttt{1}\}$! Thus $q_0 \equiv q_1 \equiv q_2$ and $q_3 \equiv q_4 \equiv q_5$, collapsing the $6$-state inner DP down to a **2-state minimal DFA** ($B_0$: last character was `'0'` or start; $B_1$: last character was `'1'`)!
   In general `DP套DP` problems (`[ZJOI2019] 麻将`, `AGC 022 E`), running this exact partition refinement automatically discovers hidden invariants that would otherwise require hours of manual case analysis.
