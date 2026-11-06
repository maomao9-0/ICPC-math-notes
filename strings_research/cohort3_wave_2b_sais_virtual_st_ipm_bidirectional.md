# Cohort 3 Reconciled Master Treatise — Wave 2B (Iteration 108): Advanced Suffix Structures — Induced Sorting (SA-IS), Virtual Suffix Trees, Internal Pattern Matching (IPM) & Bi-Directional Structures

> [!IMPORTANT]
> **Cohort 3 Cross-Comparison, Blind-Spot Audit & Reconciled Master Archive (`Wave 2B`)**
> This document is the canonical **Cohort 3 Reconciled Master Treatise** for **Wave 2B (Iteration 108)** of the Phase 1 Multi-Cohort Research Pipeline (`strings_research/PLAN.md`), synthesized by cross-auditing:
> - **Cohort 1 Primary Dossier**: `strings_research/iter_16_to_20_sais_virtual_st_ipm_bidirectional.md` (Iterations 16–20)
> - **Cohort 2 Redundant Dossier**: `strings_research/cohort2_iter_68_to_72_sais_virtual_st_ipm_bidirectional.md` (Iterations 68–72)
>
> In strict adherence to `AGENTS.md` and the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**, this treatise first presents an explicit **Cross-Cohort Blind-Spot Audit**, then synthesizes the complete mathematical theory, counterexamples, and frontier extensions across all four pillars of Wave 2B—**(1) SA-IS as a Locally Consistent Parsing & Induced LCP Engine, (2) Virtual Suffix Trees (`后缀树虚树`), `height` Cartesian Trees & Dominant Pairs (`支配对`), (3) Kociumaka's Basic Substring Dictionary, Internal Pattern Matching (IPM) & The Six Canonical Methods of Internal Border Queries (`[BJWC2018] Border 的四种求法`), and (4) Bi-Directional Suffix Structures (SCDAWG, Affix Automata & Hash-Free Suffix Balanced Trees `后缀平衡树`)**—and concludes with a deduplicated master archive of **42 non-template problems (`W2B-01`–`W2B-42`)** and **13 quarantined template problems (`R-2B-01`–`R-2B-13`)**.

---

## Section 1: Cross-Cohort Comparison & Blind-Spot Audit (Cohort 1 vs. Cohort 2)

A rigorous side-by-side audit of Cohort 1 (`iter_16_to_20`) and Cohort 2 (`cohort2_iter_68_to_72`) reveals that while both cohorts independently established the core SA-IS invariants, `height` Cartesian tree duality, Kociumaka's IPM Arithmetic Progression Lemma, and bi-directional suffix maintenance, **each cohort captured critical theorems, algorithmic paradigms, edge-case counterexamples, and regional problems that the other missed**.

### 1.1 What Cohort 1 Captured That Cohort 2 Missed

1. **Formal Proof of the LMS-Substring Prefix-Free Order Homomorphism (Theorem 16.4)**:
   - Cohort 1 proved *why* no proper prefix of an LMS-substring $S[p_a..p_{a+1}]$ can match another full LMS-substring $S[p_b..p_{b+1}]$ in both characters and $L/S$ types: every LMS-substring begins with an $S$-run, transitions once to an $L$-run, and terminates at the **first** $L \to S$ boundary $p_{a+1}$. If $S[p_b..p_{b+1}]$ matched a proper prefix of $S[p_a..p_{a+1}]$ in both characters and types, its right endpoint $p_{b+1}$ would induce an $L \to S$ transition strictly inside $(p_a, p_{a+1})$, a contradiction.
   - Cohort 1 also provided a complete step-by-step **hand-checkable bucket trace table** on $S = \texttt{mississippi\$}$ ($N = 12$) across Pass 0, Pass 1, Pass 2, LMS-substring naming $T = [3, 3, 2, 1]$, recursive sorting, and post-recursion induction, and identified the **reversed-seed pitfall** when pushing sorted LMS positions into decrementing bucket tails (`k = m` down to `1`).
2. **Zero-Tree Virtual Suffix Tree Construction for Arbitrary Substrings (Invariant 17.2)**:
   - Whereas Cohort 2 assumed binary lifting on an explicit Suffix Tree / SAM Link Tree to locate query substrings $U_i = S[l_i..r_i]$, Cohort 1 proved that a Virtual Suffix Tree over $k$ arbitrary substrings $U_i = S[l_i..r_i]$ can be built directly on `(SA, rk, height)` **without any explicit tree**: sort $U_1 \le_{\text{lex}} \dots \le_{\text{lex}} U_k$ in $O(k \log k)$ using $O(1)$ LCE comparisons, compute adjacent capped LCPs $h_t = \min(\text{LCE}(l_{t-1}, l_t), |U_{t-1}|, |U_t|)$, and build the Cartesian tree of $h_2, \dots, h_k$ in $O(k)$ via a monotonic stack.
3. **Centroid Decomposition (`点分治`) and DSU-on-Tree Formulations of `[BJWC2018] Border 的四种求法` (§18.2)**:
   - Cohort 1 derived the **Centroid Decomposition on the SAM Link Tree** (`Method 3`, splitting $\text{len}(\text{LCA}(u_r, u_i)) = \min(L(u_r), L(u_i))$ into two 2D orthogonal range queries $L(u_r) \le L(u_i)$ vs. $L(u_i) < L(u_r)$ in $O(N \log^2 N)$ time and $O(N \log N)$ space) and the **DSU-on-Tree** (`Method 4`) formulation for internal border queries.
4. **Commutativity Proof of Two-Sided Closure ($\overleftrightarrow{u}$) & Ukkonen–Weiner Active-Frontier Duality (§19.1–19.2)**:
   - Cohort 1 proved **Theorem 19.1** ($\text{rep}_L([\text{rep}_R([u]_R)]_L) = \text{rep}_R([\text{rep}_L([u]_L)]_R) = \overleftrightarrow{u}$: maximal left-extension and maximal right-extension commute) and **Theorem 19.2** (under `push_back(c)`, Ukkonen's active-suffix step runs on $\mathcal{T}_{\text{ST}}(S)$ while Weiner's single-leaf insertion runs at $R_{\max}^R$ on $\mathcal{T}_{\text{ST}}(S^R)$, and `push_front(c)` swaps their roles).
   - Cohort 1 also exhibited the explicit counterexample $S = \texttt{"aa"} \xrightarrow{\text{push\_back('b')}} \texttt{"aab"}$ showing why `push_back(c)` flips the relative lexicographical order of existing suffixes whenever one suffix was previously a proper prefix (border) of another.
5. **9 Problems & Formulations Exclusive to Cohort 1**:
   - `AtCoder ABC 213 F — Common Prefixes`, `[JSOI2016] 扭动的回文串` (Luogu P4324), `Luogu P5341 [TJOI2019] 甲苯先生和大中锋的字符串`, `CF 700E — Cool Slogans` (SA + Persistent SegTree formulation), `[十二省联考 2019] 字符串问题` (Luogu P5284), `[NOI2018] 你的名字` (SA + Persistent SegTree + `height` formulation, Luogu P4770), `[CTS2019] 重复` (Luogu P5401), `Universal Cup / Gym 102900E — 1-Mismatch Matching via 2D (SA, SA^R)`, and `QOJ / ICPC WF — Symmetric Compact DAWG & Maximal Repeats`.

---

### 1.2 What Cohort 2 Captured That Cohort 1 Missed

1. **Linear-Time Amortization of LMS-Substring Naming & Upward Tree SA-IS Adaptation (§68.3–68.4)**:
   - Cohort 2 explicitly proved why comparing adjacent LMS-substrings in Stage 3 of SA-IS takes $O(N)$ total time in the worst case: because consecutive LMS intervals overlap only at their shared endpoint $i_{k+1}$, $\sum_{k=1}^{m-1} (i_{k+1} - i_k + 1) = (n - i_1) + m - 1 < 2n$.
   - Cohort 2 also showed how SA-IS extends to **Upward Tree Suffix Arrays** ($\text{suf}(u) = S[u] \cdot \text{suf}(\text{parent}(u))$ where every node $u$ has a unique parent successor for induction, Applied to `ICPC WF 2019 D — First of Her Name`), and exposed the **Stale LMS Seed Bug** (failing to clear/overwrite preliminary LMS seeds in $\mathcal{B}_S(c)$ before Pass 2 reads them right-to-left).
2. **Dominant Pairs (`支配对`) Theory on Suffix Trees via DSU-on-Tree (§69.3, Engine D)**:
   - Cohort 2 formalized the **Dominant Pair (`启发式合并支配对`)** paradigm on the `height` Cartesian Tree / Suffix Tree: when merging a light child's original-string index $x$ into the heavy child's ordered set `std::set<int>` at node $u$ of string depth $\ell_u$, only the **immediate predecessor $x^-$ and immediate successor $x^+$** in index order can form non-dominated pairs $(x^-, x, \ell_u)$ and $(x, x^+, \ell_u)$. Any further element $z < x^-$ has $[z, x] \supset [x^-, x]$ with the exact same LCA depth $\ell_u$, so $(x^-, x)$ strictly dominates $(z, x)$ for all range queries $[l, r]$. This reduces $O(N^2)$ suffix pairs to at most $2N \log_2 N$ dominant triples!
3. **Hash-Free Combinatorial LCP Bootstrapping & Floating-Point Precision Analysis in Suffix Balanced Trees (`后缀平衡树`, §71.2 & §71.4)**:
   - While Cohort 1 relied on $O(\log^2 N)$ binary search + polynomial hashing to compute $\text{LCP}(\text{suf}(n), \text{pred})$ upon inserting $\text{suf}(n)$ into a Suffix Balanced Tree, Cohort 2 proved the **Hash-Free Combinatorial LCP Recurrence**:
     $$
     \text{LCP}(\text{suf}(n), u^-) = \begin{cases} 0 & \text{if } S[n] \ne S[u^-], \\ 1 + \text{LCP}(\text{suf}(n-1), u^- - 1) & \text{if } S[n] = S[u^-], \end{cases}
     $$
     where $\text{LCP}(\text{suf}(n-1), u^- - 1)$ is answered in $O(\log N)$ deterministic time as a **BST range-minimum query** over the adjacent `height` values stored inside the Suffix Balanced Tree itself—requiring **zero hashing and zero RMQ rebuilds**!
   - Cohort 2 also diagnosed why `double` (53-bit IEEE-754 mantissa) tags in a randomized Treap suffer catastrophic precision collisions when depth exceeds $53$, mandating an $\alpha = 0.75$ **Scapegoat Tree** with 64-bit unsigned integer tags $[0, 2^{62}]$ (depth $\le \log_{4/3}(10^6) \approx 48$).
4. **$\sqrt{N}$ SA-Neighborhood & Runs Formulations of `[BJWC2018]` (§70.3) + Kempa–Kociumaka $\tau$-Synchronizing Sets (§72.4)**:
   - Cohort 2 captured the $\sqrt{N}$ dual-regime split for internal border queries ($k \le \sqrt{N}$ vs. $|\text{rk}[j] - \text{rk}[l]| \le \sqrt{N}$) and the Runs sweep-line method for long borders ($k \ge |S[l..r]|/2$), plus **Kempa–Kociumaka (STOC 2019) $\tau$-Synchronizing Sets** and $O(1)$ tree-DFS Substring Rank lookup.
5. **9 Problems & 3 Quarantined Templates Exclusive to Cohort 2**:
   - Accepted Problems: `[JSOI2007] 字符加密` (Luogu P4051), `CF 427D — Match & Catch`, `[SCOI2012] 喵星球上的点名` (Luogu P2336), `ICPC WF 2019 D — First of Her Name`, `[TJOI2015] 弦论` (Luogu P3975), `CF 1043G — Speckled Band`, `[UOJ/LOJ/QOJ] 区间最长重复子串 (Dominant Pairs LCP)`, `POI 2012 — Prefixuffix (Prefiksufiks)`, `AtCoder AGC 060 D — Same Descent Set`.
   - Quarantined Templates: `POJ 2774 — Long Long Message`, `POJ 1743 — Musical Theme`, `AtCoder Practice2 I — Number of Substrings`.

---

### 1.3 Cohort 3 Frontier Hunt: Remaining Obscure & Advanced `[ZH]`/`[JA]`/`[EN]` Techniques Added in This Synthesis

To make Wave 2B 100% exhaustive, Cohort 3 hunts down and incorporates four additional frontier techniques that bridge or deepen Cohort 1 and Cohort 2:

1. **Fischer's Linear-Time Induced LCP Construction (`Inducing the LCP-Array`, Fischer 2011) & The `rk`-Descent Duality**:
   - How to induce `height[2..N]` inside SA-IS in $O(N)$ time during Pass 1 and Pass 2 by maintaining RMQ over recently induced bucket entries, and why $\text{type}(i) = L \iff \text{rk}[i] > \text{rk}[i+1]$ turns SA-IS $L/S$ types into the **descent set of the inverse suffix array permutation** (`AtCoder AGC 060 D`, Lyndon array construction).
2. **The Complete 6-Method Unification of `[BJWC2018] Border 的四种求法` & $O(1)$ Internal Period Queries**:
   - Merging Cohort 1's 4 methods and Cohort 2's 4 methods yields **6 distinct structural algorithms** for internal substring border queries, plus Kociumaka et al.'s **$O(1)$ Shortest Period of a Substring (`InternalPeriod(l, r)`)** via $2^k$-prefix IPM and Runs lookup.
3. **Weighted Ancestors Free-Lunch Theorem on Suffix Arrays ($O(\log N)$ vs. $O(1)$ Substring Locus Lookup)**:
   - While finding the locus of $S[l..r]$ on an explicit Suffix Tree or SAM Link Tree via binary lifting takes $O(\log N)$ time (or $O(\log \log N)$ / $O(1)$ with complex Belazzougui–Gawrychowski–Lewenstein–Nicholson Weighted Ancestor structures), on the **Suffix Array + `height` Cartesian Tree**, every substring length $\ell = r - l + 1$ corresponds to an interval $[L(l, r), R(l, r)]$ around $\text{rk}[l]$. Moreover, if a problem queries properties of the equivalence class of $S[l..r]$ offline or by length buckets, **Cartesian tree node projection** or **2-step dyadic dictionary lookup (naming $S[l..l+2^k-1]$ and $S[r-2^k+1..r]$)** locates the equivalence class in **$O(1)$ time**!
4. **Three-Term / Weighted Dominant Pairs on Suffix Trees (`[国家集训队论文 — 支配对理论]`)**:
   - Extending Cohort 2's basic Dominant Pairs to **bi-colored dominant pairs** (between sets $A$ and $B$), **distance-weighted dominant pairs** ($\text{LCP}(i, j) + f(|i - j|)$), and **three-occurrence dominant triples** ($i < j < k$ with equal distance $j - i = k - j$).

| Wave 2B Sub-Area | Cohort 1 Coverage | Cohort 2 Coverage | Cohort 3 Reconciled Master Synthesis |
| :--- | :--- | :--- | :--- |
| **SA-IS Theory & Extensions** | Prefix-free LMS proof, `"mississippi$"` trace, reversed seed pitfall, cyclic/GSAM | $O(N)$ LMS naming sum proof, Upward Tree SA-IS, stale seed pitfall | Full union + Fischer (2011) Linear Induced LCP + `rk`-Descent Duality (`§2`) |
| **Virtual ST & `height` Cartesian Tree** | 3-way isomorphism, zero-tree substring Virtual ST, DSU on `height` | Kruskal DSU tree duality, leaf-edge ($\text{occ}=1$) pitfall, **Dominant Pairs** | Full union + Bi-Colored/Clipped Dominant Pairs & $O(1)$ Locus lookup (`§3`) |
| **IPM & Internal Border Queries** | Bounded-Ratio IPM AP proof, `[BJWC2018]` (IPM, HLD, Centroid, DSU-on-Tree), 2D `(SA, SA^R)` | Concatenation LCE walk, `[BJWC2018]` (HLD, $\sqrt{N}$ SA-rank, Runs, Dyadic IPM), $\tau$-Synchronizing Sets | **All 6 Methods** for `[BJWC2018]`, $O(1)$ Internal Period, $\tau$-Synchronizing Sets (`§4`) |
| **Bi-Directional Structures** | Two-sided closure $\overleftrightarrow{u}$ commutativity, SCDAWG, Ukkonen–Weiner duality, `"aa"->"aab"` flip | **Suffix Balanced Tree (`后缀平衡树`)** 64-bit Scapegoat tags, **Hash-Free BST LCP**, Treap precision pitfall | Full union of SCDAWG/Affix theory + Hash-Free Suffix Balanced Tree (`§5`) |
| **Problem Archive & Quarantine** | 32 accepted + 10 quarantined | 33 accepted + 8 quarantined | **42 unique accepted (`W2B-01..42`) + 13 quarantined (`R-2B-01..13`)** (`§6–§7`) |

---

## Section 2: Pillar I — Linear-Time Induced Sorting (SA-IS) as a Locally Consistent Parsing & Induced LCP Engine

### 2.1 Prerequisites, Learning Objectives & Diagnostic Context

- **Assumed Baseline**: Fluency with $\text{SA}[1..N]$, inverse suffix array $\text{rk}[1..N]$, adjacent LCP array $\text{height}[2..N]$ ($H[k] = \text{LCP}(\text{suf}(\text{SA}[k-1]), \text{suf}(\text{SA}[k]))$), Kasai's $O(N)$ LCP algorithm, and $O(N \log N)$ prefix doubling.
- **Learning Objectives**:
  1. Derive **SA-IS (Nong, Zhang, and Chan 2009)** as a **locally consistent prefix-free parsing** of $S$ into Leftmost S-type (LMS) substrings of size $m \le \lfloor N/2 \rfloor$.
  2. Prove the four foundational invariants: the **$L < S$ Intra-Bucket Partition**, the **LMS Halving & $O(N)$ Total Comparison Bound**, the **LMS-Substring Prefix-Free Order Homomorphism**, and the **Two-Pass Monotonic Pointer Induction Invariant**.
  3. Connect SA-IS $L/S$ types to the **descent set of the inverse suffix array $\text{rk}$**, **Fischer's $O(N)$ Induced LCP algorithm**, **Cyclic SA-IS**, **Generalized Multi-Sentinel SA-IS**, and **Upward Tree Suffix Arrays**.

---

### 2.2 The 4-Step Structural Derivation of SA-IS

#### Step 1: The Diagnostic Signal (Why $O(N \log N)$ Prefix Doubling Fails Asymptotic & Structural Demands)

Prefix doubling sorts suffixes at lengths $2^0, 2^1, \dots, 2^{\lceil \log_2 N \rceil}$ in $O(N \log N)$ time. It fails in three competitive programming regimes:
1. **Scale & Cache Bottlenecks ($N \in [10^6, 10^7]$)**: At $N = 2 \times 10^6$ or in multi-string concatenations $S_1 \# \dots \# S_k$ reaching $5 \times 10^6$, 22 passes of cache-unfriendly radix sorting over tuple arrays exceed 1.0s–1.5s limits, whereas SA-IS makes two linear sequential sweeps per recursion level with geometric size decay $N + N/2 + N/4 + \dots < 2N$.
2. **Large or Recursive Integer Alphabets**: When suffix sorting is invoked inside an inner loop or over integer alphabets $\Sigma \subseteq [1..N]$, SA-IS requires only bucket counting sorts over $O(N)$ ranges without auxiliary tuple arrays.
3. **Lack of Local Parsing Structure**: Doubling treats all indices uniformly at power-of-two lengths. By contrast, induced sorting cuts $S$ at local minima of the suffix order ($L \to S$ transitions), producing a canonical parsing into variable-length blocks that adapts directly to Lyndon factorization, BWT, and $\tau$-synchronizing sets.

#### Step 2: The Combinatorial Word Invariant ($L/S$ Classification, LMS Blocks & Order Homomorphism)

Let $S[1..N]$ be a string over an ordered alphabet $\Sigma$, terminated by a unique sentinel $S[N] = \$$ strictly smaller than every character in $\Sigma$. Write $\text{suf}(i) = S[i..N]$.

##### Definition 2.1 ($S$-Type, $L$-Type, LMS Positions, and the $\text{rk}$-Descent Duality)
Every position $i \in \{1, \dots, N\}$ is classified into one of two types by comparing $\text{suf}(i)$ with its immediate right neighbor $\text{suf}(i+1)$:
- **Type $S$ (Smaller)**: $i = N$ (by convention for $\$$), or $\text{suf}(i) < \text{suf}(i+1)$ (equivalently, $\text{rk}[i] < \text{rk}[i+1]$, an **ascent** in $\text{rk}$).
- **Type $L$ (Larger)**: $\text{suf}(i) > \text{suf}(i+1)$ (equivalently, $\text{rk}[i] > \text{rk}[i+1]$, a **descent** in $\text{rk}$).

Because all suffixes end with the unique minimum sentinel $\$$, $\text{suf}(i) \ne \text{suf}(i+1)$ for all $i$. Peeling off the first character yields the $O(N)$ backward recurrence for $i = N-1$ down to $1$:

$$
\text{type}(i) = \begin{cases}
S & \text{if } S[i] < S[i+1], \\
L & \text{if } S[i] > S[i+1], \\
\text{type}(i+1) & \text{if } S[i] = S[i+1].
\end{cases}
$$

A position $i \in \{2, \dots, N\}$ is a **Leftmost $S$-type (LMS) position** (denoted $S^*$) if $\text{type}(i) = S$ and $\text{type}(i-1) = L$ (a **local valley** in the $\text{rk}$ permutation!). Let $1 < p_1 < p_2 < \dots < p_m = N$ be all LMS positions in $S$:
- An **LMS-prefix** is a full suffix $\text{suf}(p_k)$ starting at an LMS position $p_k$.
- An **LMS-substring** is either the terminal sentinel $S[N..N] = \$$ (for $k = m$), or the closed substring $S[p_k .. p_{k+1}]$ spanning from $p_k$ to the next LMS position $p_{k+1}$ **inclusive of both endpoints** ($1 \le k < m$).

```
Index i:    1   2   3   4   5   6   7   8   9  10  11  12
Char S[i]:  m   i   s   s   i   s   s   i   p   p   i   $
Type:       L   S   L   L   S   L   L   S   L   L   L   S
LMS (S*):       *           *           *               *
LMS-substrings: S[2..5]="issi", S[5..8]="issi", S[8..12]="ippi$", S[12..12]="$"
```

##### Lemma 2.2 (The Intra-Bucket $L < S$ Partition Invariant)
For every character $c \in \Sigma \cup \{\$\}$, let $\mathcal{B}(c) = \{i : S[i] = c\}$ be the bucket of suffixes starting with $c$. In the sorted Suffix Array, **every $L$-type suffix in $\mathcal{B}(c)$ is strictly lexicographically smaller than every $S$-type suffix in $\mathcal{B}(c)$**:

$$
\mathcal{B}(c) = \mathcal{B}_L(c) \sqcup \mathcal{B}_S(c), \qquad \forall i \in \mathcal{B}_L(c), \; \forall j \in \mathcal{B}_S(c), \quad \text{suf}(i) < \text{suf}(j).
$$

**Proof**: If $i \in \mathcal{B}_L(c)$, the maximal contiguous run of $c$'s starting at $i$ is followed by some character $d_i < c$, so $\text{suf}(i) = c^{r_i} d_i \dots < c^\infty$. If $j \in \mathcal{B}_S(c)$, the maximal run of $c$'s starting at $j$ is followed by some character $d_j > c$, so $\text{suf}(j) = c^{r_j} d_j \dots > c^\infty$. By transitivity through the infinite periodic word $c^\infty$, $\text{suf}(i) < c^\infty < \text{suf}(j)$. $\blacksquare$

##### Lemma 2.3 (The LMS Halving Bound & $O(N)$ Adjacent Comparison Bound)
For any string $S[1..N]$ ($N \ge 2$) with LMS positions $1 < p_1 < p_2 < \dots < p_m = N$:
1. **Halving Bound**: $m \le \lfloor N / 2 \rfloor$.
2. **Linear Overlap Sum**: The sum of lengths of all LMS-substrings satisfies $\sum_{k=1}^{m-1} (p_{k+1} - p_k + 1) + 1 = (N - p_1 + 1) + m \le \frac{3}{2} N < 2N$.

**Proof**: (1) $p_1 > 1$ because index $1$ has no left neighbor $i-1$; and no two LMS positions can be adjacent because $\text{type}(p_{k+1}-1) = L \ne S = \text{type}(p_k)$. Thus $p_{k+1} - p_k \ge 2$, giving $m \le \lfloor N/2 \rfloor$. (2) Consecutive intervals $[p_k, p_{k+1}]$ telescope across $[p_1, N]$, overlapping only at the $m-1$ interior LMS points $p_2, \dots, p_m$. Thus comparing adjacent sorted LMS-substrings character-by-character takes strictly $O(N)$ total time! $\blacksquare$

##### Theorem 2.4 (LMS-Substring Prefix-Free Order Homomorphism)
Define a total preorder $\preceq$ on LMS-substrings by comparing them offset-by-offset ($t = 0, 1, \dots$) using the **character-and-type pair** $(S[x+t], \text{type}(x+t))$ with $L < S$:
1. **Prefix-Freeness**: No proper prefix of an LMS-substring $U = S[p_a..p_{a+1}]$ can equal another full LMS-substring $V = S[p_b..p_{b+1}]$ in both characters and $L/S$ types.
2. **Order Homomorphism**: Two LMS-substrings satisfy $U \equiv V$ iff $|U| = |V|$ and $(S[p_a+t], \text{type}(p_a+t)) = (S[p_b+t], \text{type}(p_b+t))$ for all $0 \le t < |U|$. If we assign each LMS-substring $S[p_k..p_{k+1}]$ its equivalence-class rank $T[k] \in \{1, \dots, \sigma'\}$ under $\preceq$, then for all $1 \le a, b \le m$:

$$
\text{suf}_S(p_a) < \text{suf}_S(p_b) \iff \text{suf}_T(a) < \text{suf}_T(b).
$$

**Proof**: Inside any LMS-substring $S[p_a..p_{a+1}]$ ($a < m$), the type sequence starts with one or more $S$'s at $p_a$, switches to one or more $L$'s, and returns to $S$ for the **very first time** at $p_{a+1}$. If a shorter LMS-substring $S[p_b..p_{b+1}]$ ($|V| < |U|$) matched $S[p_a .. p_a+|V|-1]$ in both characters and $L/S$ types, then position $p_a + |V| - 1 < p_{a+1}$ would be an $L \to S$ transition strictly inside $(p_a, p_{a+1})$, contradicting the definition of $p_{a+1}$ as the next LMS position after $p_a$! Because LMS-substrings form a prefix-free code under $(S[\cdot], \text{type}(\cdot))$, partitioning $\text{suf}_S(p_a)$ and $\text{suf}_S(p_b)$ into their chains of LMS-substrings ensures that the first mismatched LMS-substring pair decides the global suffix order via Lemma 2.2. $\blacksquare$

#### Step 3: The Reverse-Engineering Scratchpad (Two-Pass Induced Sorting & Fischer's Induced LCP)

##### The Two-Pass `InduceSort` Engine
Given an array of LMS positions $q_1, q_2, \dots, q_m$ (either in arbitrary order before recursion, or in exact $\text{suf}(q_k)$ sorted order after recursion):
1. **Pass 0 (Seed LMS at Bucket Tails)**: Fill $\text{SA}[1..N] \leftarrow -1$. Set $\text{tail}[c]$ to the right end of each bucket $\mathcal{B}(c)$. Iterate $k = m$ **down to** $1$ and place $\text{SA}[\text{tail}[S[q_k]]\text{--}] \leftarrow q_k$.
2. **Pass 1 (Left-to-Right Scan $\to$ Induce $L$-Type Suffixes at Bucket Heads)**: Set $\text{head}[c]$ to the left end of each bucket $\mathcal{B}(c)$. For $k = 1$ to $N$: if $\text{SA}[k] = i > 1$ and $\text{type}(i-1) = L$, set $\text{SA}[\text{head}[S[i-1]]\text{++}] \leftarrow i-1$.
   - *Strict Pointer Monotonicity*: Since $\text{type}(i-1) = L \implies \text{suf}(i-1) > \text{suf}(i)$, index $i$ always sits at some slot $k$ strictly **to the left** of the target slot of $i-1$. Every maximal $L$-chain starts at an LMS seed placed in Pass 0.
3. **Pass 2 (Right-to-Left Scan $\to$ Induce $S$-Type Suffixes at Bucket Tails)**: Reset $\text{tail}[c]$ to the right end of each bucket $\mathcal{B}(c)$. For $k = N$ down to $1$: if $\text{SA}[k] = i > 1$ and $\text{type}(i-1) = S$, set $\text{SA}[\text{tail}[S[i-1]]\text{--}] \leftarrow i-1$ (overwriting the preliminary LMS seeds from Pass 0!).
   - *Strict Pointer Monotonicity*: Since $\text{type}(i-1) = S \implies \text{suf}(i-1) < \text{suf}(i)$, index $i$ always sits at some slot $k$ strictly **to the right** of the target slot of $i-1$. All $L$-type boundaries are already finalized in Pass 1.

##### Hand-Checkable Trace on $S = \texttt{m i s s i s s i p p i \$}$ ($N = 12$)

| Bucket $c$ | Size | $\mathcal{B}_L(c)$ | $\mathcal{B}_S(c)$ | Pre-Recursion Pass 0 (LMS Seed) | After Pass 1 (Induce $L$) | After Pass 2 (Induce $S$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\$$ | 1 | $\emptyset$ | $[1..1]$ | `[12]` | `[12]` | `[12]` |
| $\text{i}$ | 4 | $[2..2]$ | $[3..5]$ | `[_, 2, 5, 8]` | `[11, 2, 5, 8]` | `[11, 8, 2, 5]` |
| $\text{m}$ | 1 | $[6..6]$ | $\emptyset$ | `[_]` | `[1]` | `[1]` |
| $\text{p}$ | 2 | $[7..8]$ | $\emptyset$ | `[_, _]` | `[10, 9]` | `[10, 9]` |
| $\text{s}$ | 4 | $[9..12]$ | $\emptyset$ | `[_, _, _, _]` | `[7, 4, 6, 3]` | `[7, 4, 6, 3]` |

- **Stage 3 (Naming)**: The induced LMS order in $\text{SA}$ is `[12, 8, 2, 5]`. Comparing adjacent LMS-substrings gives $S[12..12] = \texttt{"\$"} \mapsto 1$, $S[8..12] = \texttt{"ippi\$"} \mapsto 2$, $S[2..5] = \texttt{"issi"} \mapsto 3$, $S[5..8] = \texttt{"issi"} \mapsto 3$. In original string order $(p_1, p_2, p_3, p_4) = (2, 5, 8, 12)$, the reduced string is $T = [3, 3, 2, 1]$.
- **Stage 4–5 (Recursion & Final Induction)**: $\text{SA}_T = [4, 3, 2, 1]$, sorting the LMS positions as $(q_1, q_2, q_3, q_4) = (12, 8, 5, 2)$. Seeding them from $k=4$ down to $1$ into the bucket tails puts `[_, 8, 5, 2]` in $\mathcal{B}(\text{i})$. Running Pass 1 + Pass 2 yields $\text{SA} = [12, 11, 8, 5, 2, 1, 10, 9, 7, 4, 6, 3]$.

##### Frontier Extension: Fischer's Linear-Time Induced LCP (`height`) Inside SA-IS (Fischer 2011)
While Kasai's algorithm computes $\text{height}[2..N]$ in $O(N)$ *after* $\text{SA}$ is built (using $\text{height}[\text{rk}[i]] \ge \text{height}[\text{rk}[i-1]] - 1$), **Fischer (2011)** proved that `height` can also be induced *directly inside Pass 1 and Pass 2*:
- Whenever two suffixes $i-1$ and $j-1$ are consecutively induced into the **same sub-bucket** $\mathcal{B}_L(c)$ (from $i$ at $\text{SA}[k_1]$ and $j$ at $\text{SA}[k_2]$ with $k_1 < k_2$), their common prefix is $c$ followed by the common prefix of $\text{suf}(i)$ and $\text{suf}(j)$:
  $$
  \text{LCP}(\text{suf}(i-1), \text{suf}(j-1)) = 1 + \min_{k_1 < t \le k_2} H[t].
  $$
- Across the $L \to S$ boundary inside bucket $\mathcal{B}(c)$ (between the last $L$-type suffix $i$ and first $S$-type suffix $j$), both start with a run of $c$'s where $i$ is followed by $d_i < c$ and $j$ is followed by $d_j > c$, so their LCP is simply $\min(\text{run}_c(i), \text{run}_c(j))$!

#### Step 4: Non-Standard Domain Adaptations & Broken-Invariant Counterexamples

| Domain Adaptation | Why Naive SA-IS Fails | Exact Structural Fix |
| :--- | :--- | :--- |
| **Generalized SA on $K$ Strings ($S_1, \dots, S_K$)** | Concatenating with a **single shared separator** `#` violates the unique sentinel rule: `# == #` propagates $L/S$ types across string boundaries and merges distinct LMS blocks. Using $K$ distinct negative sentinels blows up the alphabet. | Use a single separator value `0` at the end of each $S_r$, but modify the type recurrence and LMS equality test so that **every separator index is unconditionally Type $S$ (and LMS)**, and two separators at positions $i \ne j$ are treated as unequal ($i < j$ tie-break). |
| **Cyclic Shift Sorting / BWT (`[JSOI2007]`, `ABC 272 F`)** | Appending `$` distorts cyclic wrap-around comparisons when a match crosses index $N$. | Either (a) rotate $S$ to start at its minimum Lyndon root $w$ (via Duval's algorithm in $O(N)$, `Wave 1B`), or (b) run Cyclic SA-IS modulo $N$ after factoring $S = w^d$ via KMP. For two-string cyclic comparison $S^{(i)} \le T^{(j)}$ (`ABC 272 F`), build SA-IS on $S \cdot S \cdot (\texttt{'a'}-1) \cdot T \cdot T \cdot (\texttt{'z'}+1)$. |
| **Upward Tree Suffix Array (`ICPC WF 2019 D`)** | Standard SA-IS assumes a linear chain $i-1 \to i$. On a rooted tree where node $u$'s string is $S[u] \cdot \text{str}(\text{parent}(u))$, multiple children share the same parent $v$. | Induction still works on upward paths because every node $u$ has a **unique successor** $\text{parent}(u)$! When scanning $v = \text{SA}[k]$, loop over all children $u \in \text{children}(v)$ of matching $L/S$ type; propagate equal-rank buckets for tied upward paths. |

##### Broken-Invariant Counterexamples
1. **Pitfall 1 (Comparing LMS-Substrings by Characters Only, Ignoring $L/S$ Types or Length)**:
   - If you compare two LMS-substrings $U = S[p_a..p_{a+1}]$ and $V = S[p_b..p_{b+1}]$ without first checking $|U| = |V|$ and $\text{type}(p_a+t) = \text{type}(p_b+t)$, an LMS-substring `"ab"` where `'b'` is $S^*$ (followed by `'c'`) and the prefix `"ab"` of `"aba"` where `'b'` is $L$ (followed by `'a'`) will be falsely equated if the loop terminates at $\min(|U|, |V|)$!
2. **Pitfall 2 (Reversed Seed Insertion Order in Pass 0)**:
   - Because Pass 0 inserts sorted LMS positions $q_1 <_{\text{suf}} \dots <_{\text{suf}} q_m$ into $\mathcal{B}_S(c)$ using a **decrementing** $\text{tail}[c]$ pointer, you **must** iterate $k = m$ down to $1$. Iterating $k = 1 \dots m$ places $q_1$ at the very back of the bucket and reverses all LMS seeds!
3. **Pitfall 3 (Stale LMS Seeds Not Overwritten Before Pass 2)**:
   - In the pre-recursion `InduceSort`, Pass 0 seeds LMS indices in arbitrary order. Before Pass 2 scans right-to-left from $N$ down to $1$, all $S$-sub-bucket slots (except $\text{SA}[1] = N$) must be cleared (or ignored until written by Pass 2); otherwise Pass 2 reads the unsorted Pass 0 seeds and induces a corrupted $S$-order.

---

## Section 3: Pillar II — Virtual Suffix Trees (`后缀树虚树`), `height` Cartesian Trees & Dominant Pairs (`支配对`)

### 3.1 The Canonical Three-Way Isomorphism of Suffix Trees

A cornerstone of advanced stringology is the exact equivalence of three tree representations of $S[1..N]$:

| Representation | Construction & Nodes | String Depth of Node $u$ | Pairwise $\text{LCP}(\text{suf}(i), \text{suf}(j))$ |
| :--- | :--- | :--- | :--- |
| **1. Suffix Tree $\mathcal{T}_{\text{ST}}(S)$** | Compact Trie of $S[1..N]\$$ ($\le 2N$ nodes) | Explicit prefix length $\text{dep}(u)$ | $\text{dep}\big(\text{LCA}_{\text{ST}}(\text{leaf}(i), \text{leaf}(j))\big)$ |
| **2. Reversed SAM Link Tree $\mathcal{T}_{\text{SAM}}(S^R)$** | Parent (`link`) tree of $\text{SAM}(S^R)$ ($\le 2N-1$ states) | State max-length $\text{len}(u)$ | $\text{len}\big(\text{LCA}_{\text{SAM}}(\text{pos}(i), \text{pos}(j))\big)$ |
| **3. Min-Cartesian Tree of $\text{height}[2..N]$** | Min-heap Cartesian tree on $H[k] = \text{height}[k]$ (or Kruskal DSU tree merging $(k-1, k)$ in decreasing order of $H[k]$) | Split value $H[u]$ (after contracting $H[u] = H[\text{par}(u)]$ edges) | $\min_{\text{rk}[i] < k \le \text{rk}[j]} H[k] = H\big[\text{LCA}_{\text{Cart}}(\text{rk}[i], \text{rk}[j])\big]$ |

```
Suffix Array leaves:   SA[1]       SA[2]       SA[3]       SA[4]
Adjacent LCPs H[2..4]:      H[2]=3      H[3]=1      H[4]=4
Min-Cartesian Tree on H:
                     [H[3] = 1]  <-- Root internal node (SA interval [1..4])
                      /      \
               [H[2] = 3]   [H[4] = 4]
                /      \     /      \
             SA[1]   SA[2] SA[3]   SA[4]
```

> [!IMPORTANT]
> **Counting Distinct Substrings per Cartesian Tree Node (`CF 802I`, `[TJOI2019]`)**:
> In the contracted Min-Cartesian tree of $H[2..N]$, an internal node $u$ spanning SA leaf interval $[L_u, R_u]$ with height $h_u = H[u]$ and parent height $h_{p(u)} = \max(H[L_u], H[R_u+1])$ represents **$h_u - h_{p(u)}$ distinct substrings** (of lengths $h_{p(u)} + 1, \dots, h_u$), each occurring **exactly $\text{sz}(u) = R_u - L_u + 1 \ge 2$ times** in $S$!
> Meanwhile, each **leaf** $k \in [1..N]$ represents $(N - \text{SA}[k] + 1) - \max(H[k], H[k+1])$ distinct substrings that occur **only once** ($\text{occ} = 1$) in $S$.

---

### 3.2 The 4-Step Derivation of Virtual Suffix Trees (`后缀树虚树`) & Dominant Pairs (`支配对`)

#### Step 1: The Diagnostic Signal (When Whole-Tree Walks & All-Pairs Loops Fail)

1. **Subset Query Signal (`后缀树虚树`, `CF 1073G`)**: A problem gives $Q$ queries specifying subsets of substrings $A_q, B_q$ with $\sum_q (|A_q| + |B_q|) \le 5 \times 10^5$ and asks for $\sum_{u \in A_q} \sum_{v \in B_q} f(\text{LCP}(u, v))$. Both $O(|A_q||B_q|)$ pairwise loops and $O(N)$ whole-tree DPs TLE.
2. **Range-Index $\times$ LCP Signal (`后缀树支配对`, `[UOJ/QOJ] Range Longest Repeat`, `CF 1098F`)**: A problem gives $Q$ interval queries $[l, r]$ on original string indices and asks for an extremum or sum involving $\text{LCP}(\text{suf}(i), \text{suf}(j))$ over $l \le i < j \le r$. Here $i, j$ are constrained in **original string index space** $[l, r]$, while $\text{LCP}(\text{suf}(i), \text{suf}(j))$ lives in **Suffix Array / Cartesian tree space**!

#### Step 2: The Combinatorial Word Invariants (Zero-Tree Substring Virtual ST & DSU-on-Tree Dominant Pairs)

##### Theorem 3.1 (Zero-Tree Virtual Suffix Tree over Arbitrary Substrings)
Let $U_1, U_2, \dots, U_k$ be arbitrary substrings $U_t = S[l_t..r_t]$ of $S$, sorted in non-decreasing lexicographical order $U_1 \le_{\text{lex}} U_2 \le_{\text{lex}} \dots \le_{\text{lex}} U_k$ via $O(1)$ LCE comparisons. Define the adjacent substring LCP array:

$$
h_t = \text{LCP}(U_{t-1}, U_t) = \min\big(\text{LCE}_S(l_{t-1}, l_t), \; |U_{t-1}|, \; |U_t|\big), \qquad t = 2, \dots, k.
$$

Then for **every** pair $1 \le a < b \le k$:

$$
\text{LCP}(U_a, U_b) = \min_{a < t \le b} h_t,
$$

and the Min-Cartesian tree built on $h_2, \dots, h_k$ in $O(k)$ time is canonically isomorphic to the **Virtual Suffix Tree (`后缀树虚树`)** of $\{U_1, \dots, U_k\}$!

**Proof**: Truncating each suffix $\text{suf}(l_t)$ to length $|U_t|$ is equivalent to inserting the $k$ strings $U_t \$$ into a compact Trie. Because $U_1 \le_{\text{lex}} \dots \le_{\text{lex}} U_k$ is the exact DFS leaf order of that Trie, the LCA depth of any two leaves $a < b$ equals the minimum LCA depth of consecutive leaves $(t-1, t)$ for $a < t \le b$. $\blacksquare$

##### Theorem 3.2 (The Suffix Tree Dominant Pair Lemma — `后缀树启发式合并支配对`)
Suppose we traverse the Min-Cartesian tree of $\text{height}[2..N]$ (or SAM Link Tree) bottom-up using **DSU-on-Tree (`树上启发式合并`)**, maintaining at each internal node $u$ (of string depth $\ell_u$) an ordered set `std::set<int>` of original string starting indices $\text{SA}[x]$ ($x \in [L_u, R_u]$). When inserting an index $i$ from a light child subtree of $u$ into the heavy child's ordered set, let $i^-$ be the largest element $< i$ and $i^+$ be the smallest element $> i$ currently in the set.
Then for any range query $[l, r]$ seeking to maximize $g(\text{LCP}(\text{suf}(a), \text{suf}(b)), a, b)$ where $g(\ell, a, b)$ is non-decreasing in $\ell$ and non-increasing in the span $[a, b]$ (for instance, $\max_{l \le a < b \le r} \min(r - b + 1, \text{LCP}(\text{suf}(a), \text{suf}(b)))$):
1. **Dominance**: Every cross-subtree pair $(a, b)$ having $\text{LCA}(a, b) = u$ is dominated by at least one generated adjacent pair $(i^-, i, \ell_u)$ or $(i, i^+, \ell_u)$!
2. **Sparsity**: Across the entire Suffix Tree, at most **$2N \log_2 N$ dominant triples** $(a, b, \ell_u)$ ($a < b$) are ever generated!

**Proof**: Consider any $z$ in the heavy set with $z < i^- < i$. Both $(z, i)$ and $(i^-, i)$ have $\text{LCA} = u$, so both have the exact same $\text{LCP} = \ell_u$. However, $[i^-, i] \subset [z, i]$: whenever a query interval $[l, r]$ contains $[z, i]$ ($l \le z < i \le r$), it also contains $[i^-, i]$ ($l \le i^- < i \le r$), and both have the same right endpoint $b = i$, so $\min(r - i + 1, \ell_u)$ is identical for both! Symmetrically, for any $w > i^+ > i$, $[i, i^+] \subset [i, w]$ and $r - i^+ + 1 > r - w + 1$, so $(i, i^+, \ell_u)$ strictly dominates $(i, w, \ell_u)$ in **both** containment $[l, r]$ and clipped length $\min(r - b + 1, \ell_u)$! By the DSU-on-Tree size-doubling invariant, each index $i \in [1..N]$ is inserted as a light element at most $\lfloor \log_2 N \rfloor$ times, producing at most $2$ pairs per insertion $\implies \le 2N \log_2 N$ pairs total. $\blacksquare$

#### Step 3: The Reverse-Engineering Scratchpad (Four Algorithmic Engines on `height`)

1. **Engine A: Monotonic Stack over $H[2..N]$ (`[AHOI2013] 差异`, `CF 802I`, `CF 873F`)**:
   - Find for each $k \in [2..N]$ the maximal interval $[L_k, R_k]$ where $H[j] > H[k]$ for $j \in [L_k, k-1]$ (**strict `<` on left**) and $H[j] \ge H[k]$ for $j \in [k+1, R_k]$ (**non-strict `<=` on right**). Then $H[k]$ is the tie-broken minimum for $(k - L_k + 1)(R_k - k + 1)$ pairs of suffixes.
2. **Engine B: Decreasing-`height` Kruskal DSU Sweep (`[NOI2015] 品酒大会`)**:
   - Sort split points $k \in [2..N]$ in descending order of $H[k]$. Maintain DSU components over SA indices $1..N$ storing $(\text{sz}, \max_1, \min_1)$. Merging $k-1$ and $k$ at threshold $L = H[k]$ adds $\text{sz}[u]\text{sz}[v]$ pairs with $\text{LCP} = L$ and updates $\text{ans}[L] \leftarrow \max(\text{ans}[L], \max_1[u]\max_1[v], \min_1[u]\min_1[v])$, followed by suffix sum/max from $N-1 \to 0$.
3. **Engine C: $O(k \log k)$ Virtual Suffix Tree DP (`CF 1073G`)**:
   - Sort query substrings $U_1, \dots, U_k$ by $\text{rk}$ (or $O(1)$ LCE), deduplicate identical items (handling self-overlaps $u \in A_q \cap B_q$ with weight $|u|$), compute $h_t = \text{LCP}(U_{t-1}, U_t)$, and run a single monotonic-stack / Cartesian-tree DP accumulating $h_t (W_{A,L} W_{B,R} + W_{B,L} W_{A,R})$.
4. **Engine D: Dominant Pairs + 2D Offline Sweep (`[UOJ/QOJ] Range Longest Repeat`)**:
   - Extract the $\le 2N \log_2 N$ dominant triples $(a, b, \ell)$ ($a < b$) via DSU-on-Tree over the Cartesian tree of $H$.
   - For a query $[l, r]$, a valid triple $(a \ge l, b \le r, \ell)$ contributes $\min(r - b + 1, \ell)$. Split into two regimes at the right-endpoint threshold $b + \ell - 1 \le r$:
     - **Regime 1 ($b + \ell - 1 \le r$)**: Contributes $\ell$ completely inside $[l, r]$.
     - **Regime 2 ($b + \ell - 1 > r, \; b \le r$)**: Clipped by $r$, contributing $r - b + 1$ (so maximize $-b$ among triples with $a \ge l$ and $b + \ell - 1 > r$).
   - Both regimes reduce to $O(N \log^2 N + Q \log N)$ offline 2D Fenwick / Segment Tree sweeps!

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Symmetric Strict vs. Non-Strict Monotonic Stack Bounds**:
   - Using `>` on both left and right omits pairs when $H$ has duplicate minimums (e.g. $S = \texttt{ababab}$, $H$ contains two `2`s); using `>=` on both sides double-counts them. Always use `>` on one side and `>=` on the other.
2. **Omitting Leaf Edges ($\text{occ} = 1$) in Substring Sums (`CF 802I`, `CF 873F`, `[TJOI2019]`)**:
   - Internal nodes of the Cartesian tree of $H[2..N]$ only capture substrings occurring $\ge 2$ times. Substrings occurring **once** lie on the leaf edges of length $(N - \text{SA}[k] + 1) - \max(H[k], H[k+1])$!
3. **Partial Evaluation of Equal-Height Nodes When Weights Can Be Negative (`CF 616F`)**:
   - When leaf weights $c_i$ can be negative, evaluating $H[k] \cdot \sum_{x=L_k-1}^{R_k} c_{\text{SA}[x]}$ at a Cartesian tree node where $H[k] = H[\text{par}(k)]$ inspects a non-maximal occurrence subset (which might have a larger sum than the true full equivalence class when some $c_i < 0$!). Only evaluate nodes where $H[k] > \max(H[L_k-1], H[R_k+1])$.

---

## Section 4: Pillar III — Kociumaka's Basic Substring Dictionary, Internal Pattern Matching (IPM) & The Six Methods of Internal Border Queries (`[BJWC2018]`)

### 4.1 Architecture of the Basic Substring Dictionary & The $O(1)$ Locus Free-Lunch Theorem

Following **Kociumaka, Radoszewski, Rytter, and Waleń (SODA 2015 / SIAM J. Comput. 2024)**, preprocessing a static string $S[1..N]$ turns substrings $U = S[l..r]$ into atomic $O(1)$-manipulable objects:

| Primitive | Input | Complexity | Structural Mechanism |
| :--- | :--- | :--- | :--- |
| **1. $\text{LCE}(i, j)$ & $\text{LCE}^R(i, j)$** | $i, j \in [1..N]$ | $O(1)$ | RMQ over $\text{height}$ of $S$ and $S^R$ |
| **2. Substring Comparison ($U \lessgtr V$)** | $U = S[l_1..r_1], V = S[l_2..r_2]$ | $O(1)$ | $d = \min(\text{LCE}(l_1, l_2), |U|, |V|)$; compare $S[l_1+d]$ vs. $S[l_2+d]$ or lengths |
| **3. Concatenation Comparison** | $U_1 \dots U_k$ vs. $V_1 \dots V_m$ | $O(k+m)$ | Two-pointer walk advancing by $\min(\text{LCE}, \text{rem\_len}_A, \text{rem\_len}_B)$ (`CF 504E`) |
| **4. Substring SA Interval $[L(U), R(U)]$** | $U = S[l..r]$ | $O(\log N)$ or $O(1)$ | Binary search on RMQ of $H$ around $\text{rk}[l]$, or $O(1)$ via Weighted Ancestors / $2^k$ pair |
| **5. Substring Global Rank (`Rank(U)`)** | $U = S[l..r]$ | $O(\log N)$ or $O(1)$ | $\text{pref\_distinct}[L(U)-1] + (|U| - H[L(U)])$ (`§4.1.1`) |
| **6. Bounded-Ratio $\text{IPM}(P, T)$** | $P = S[l_1..r_1], T = S[l_2..r_2], |T| < 2|P|$ | $O(\log N)$ or $O(1)$ | Occurrences of $P$ in $T$ form **at most one Arithmetic Progression** of step $\text{per}(P)$! |
| **7. 2D Split / Wildcard Anchor** | $P_1 \cdot ? \cdot P_2$ or prefix-suffix pair | $O(\log N)$ | 2D orthogonal range query on $p_i = (\text{rk}_{S^R}[N-i+2], \text{rk}_S[i+1])$ |

#### 4.1.1 Two Ways to Compute Global Lexicographical Substring Rank `Rank(S[l..r])` & `Select(K)`
1. **Via Suffix Array Prefix Sums (`Cohort 1 §20.2 #30`)**:
   - In SA order, suffix $\text{SA}[k]$ introduces $\Delta_k = (N - \text{SA}[k] + 1) - H[k]$ new distinct substrings (of lengths $H[k]+1, \dots, N - \text{SA}[k] + 1$) in exact lexicographical order! Let $\text{pref}[k] = \sum_{t=1}^k \Delta_t$.
   - **`Select(K)`**: Binary search for the first $k$ with $\text{pref}[k] \ge K$; the $K$-th distinct substring is the prefix of $\text{suf}(\text{SA}[k])$ of length $H[k] + (K - \text{pref}[k-1])$.
   - **`Rank(S[l..r])`**: Find the **leftmost** SA index $k_0 = L(S[l..r]) \le \text{rk}[l]$ such that $\text{LCE}(\text{SA}[k_0], l) \ge r - l + 1$. Then:
     $$
     \text{Rank}(S[l..r]) = \text{pref}[k_0 - 1] + (r - l + 1 - H[k_0]).
     $$
2. **Via Suffix Tree DFS Prefix Sums (`Cohort 2 §72.4`)**:
   - Equivalently, on the Suffix Tree / Cartesian tree of $H$, locate the locus $u$ of $S[l..r]$ (highest ancestor of $\text{rk}[l]$ with $\text{len}(u) \ge r - l + 1$); then $\text{Rank}(S[l..r]) = \text{dfs\_pref}(u) - (\text{len}(u) - (r - l + 1))$.

---

### 4.2 The 4-Step Derivation of Bounded-Ratio IPM & The Six Canonical Methods for `[BJWC2018] Border 的四种求法`

#### Step 1: The Diagnostic Signal (Why Substring Border Queries Defeat Standard KMP and SAM)

In **`[BJWC2018] Border 的四种求法` (Luogu P4482)**, we are given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[l, r]$, asking for the maximum proper border length $b \in [1, r - l]$ of $S[l..r]$ (i.e. $S[l .. l+b-1] = S[r-b+1 .. r]$).
Why do textbook structures fail?
- Let $i = l + b - 1 \in [l, r - 1]$ be the right endpoint of the prefix border. Then $b = i - l + 1$ is a valid border iff:
  $$
  \text{LCSuf}\big(S[1..r], S[1..i]\big) \ge i - l + 1 \quad \Longleftrightarrow \quad i - \text{len}\big(\text{LCA}_{\text{SAM}}(u_r, u_i)\big) \le l - 1.
  $$
- **The Dual-Side Coupling Bottleneck**: The unknown index $i \in [l, r-1]$ appears on **both** sides of the inequality—inside the tree node $u_i$ in $\text{LCA}_{\text{SAM}}(u_r, u_i)$ AND in the linear offset $i - l + 1$!

#### Step 2: The Combinatorial Word Invariant (Kociumaka's Bounded-Ratio IPM Arithmetic Progression Theorem)

##### Theorem 4.1 (Bounded-Ratio IPM Arithmetic Progression Lemma — Kociumaka et al. 2015)
Let $P$ and $T$ be strings with $|P| \le |T| < 2|P|$. Then the set of starting positions of occurrences of $P$ in $T$, $\text{Occ}(P, T) = \{x_1 < x_2 < \dots < x_m\}$, has either $m \le 2$ elements, or forms a **single arithmetic progression** with common difference $d = x_2 - x_1 = \text{per}(P)$, the shortest period of $P$.

**Proof**: Since $x_m + |P| - 1 \le |T| < 2|P|$, the distance between the **first** occurrence $x_1$ and the **last** occurrence $x_m$ satisfies $x_m - x_1 \le |T| - |P| < |P|$. Thus all $m$ occurrences of $P$ overlap on a common nonempty substring $T[x_m .. x_1 + |P| - 1]$!
For any consecutive pair $x_k < x_{k+1}$, their shift $d_k = x_{k+1} - x_k < |P|$ is a period of $P$, so $d_k \ge d = \text{per}(P)$. Moreover, if $m \ge 3$, $d_k + d \le (x_m - x_1) < |P|$ (or by overlapping periodic alignment across $[x_1, x_m + |P| - 1]$), the entire union $T[x_1 .. x_m + |P| - 1]$ has period $d = \text{per}(P)$. Therefore, shifting $x_k$ by $d$ stays inside $[x_1, x_m]$ and produces a valid occurrence of $P$ at $x_k + d$, forcing $x_{k+1} - x_k = d$ for all $1 \le k < m$. $\blacksquare$

```
Substring U = S[l .. r], testing dyadic scale m where border length b in [2^m, 2^{m+1}-1]:

  Prefix border S[l ............ l+b-1]:
  |-- P_m (2^m) --|
          |---- Q_m (2^m) ----|  <-- Q_m must occur in Head Window S[l .. l+2^{m+1}-2] (len < 2*2^m)

  Suffix border S[r-b+1 ............ r]:
  |-- P_m (2^m) --|              <-- P_m must occur in Tail Window S[r-2^{m+1}+2 .. r] (len < 2*2^m)
          |---- Q_m (2^m) ----|
```

#### Step 3: The Reverse-Engineering Scratchpad — Reconciling All Six Canonical Methods for `[BJWC2018]`

By combining Cohort 1 (`§18.2`) and Cohort 2 (`§70.3`), we obtain **six distinct algorithms** for internal border queries:

| Method | Core Structural Decomposition | Preprocessing | Per-Query Time | Space | Online? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Method 1: Dyadic $2^m$ IPM + AP Intersection** (Kociumaka / Jin Ce) | For each scale $m \in [0..\lfloor\log_2(r-l)\rfloor]$, find AP of $P_m = S[l..l+2^m-1]$ in $S[r-2^{m+1}+2..r]$ and AP of $Q_m = S[r-2^m+1..r]$ in $S[l..l+2^{m+1}-2]$ via Persistent SegTree over SA (finding min, 2nd min, max occurrence), then intersect the two 1D APs in $O(1)$. | $O(N \log N)$ | $O(\log^2 N)$ (or $O(\log N)$ with $2^m$-buckets) | $O(N \log N)$ | **Yes** |
| **Method 2: SAM Link-Tree HLD + SegTree Merge** | Walk $O(\log N)$ HLD chains from $u_r$ to root. **Light subtrees** ($\text{LCA}(u_r, u_i) = w$ fixed): query $\max \{i \in \text{endpos}(w) \cap [l, \min(r-1, l+\text{len}(w)-1)]\}$ on merged SegTree. **Heavy chain** ($u_i$ enters above $u_r$): query heavy-chain SegTree for largest $i \in [l, r-1]$ with $i - \text{len}(w) \le l - 1$. | $O(N \log^2 N)$ | $O(\log^2 N)$ | $O(N \log N)$ | **Yes** |
| **Method 3: Link-Tree Centroid Decomposition (`点分治`)** | At centroid $c$, every node $u$ has bottleneck length $L(u) = \text{len}(\text{LCA}(u, c))$. Split $\min(L(u_r), L(u_i))$ into **Case 1 ($L(u_r) \le L(u_i)$)**: $i \le l + L(u_r) - 1$; **Case 2 ($L(u_i) < L(u_r)$)**: $i - L(u_i) \le l - 1$. Both are 2D orthogonal range queries! | $O(N \log^2 N)$ | $O(\log^2 N)$ | $O(N \log N)$ | Offline (or Persistent) |
| **Method 4: DSU-on-Tree (`树上启发式合并`)** | At each Link Tree node $w$, merge light child $\text{endpos}$ sets into heavy child while answering queries parked at $u_r$ against fixed $\text{len}(w)$ and maintaining $i - \text{len}(w)$ on heavy-path ascents. | $O((N+Q)\log^2 N)$ | Amortized | $O(N + Q)$ | Offline |
| **Method 5: $\sqrt{N}$ Dual-Regime SA-Neighborhood Split** | Choose $B = \sqrt{N}$. **Short borders ($b \le B$)**: test $b = 1 \dots B$ in $O(1)$ via $\text{LCE}(l, r-b+1) \ge b$. **Close SA-Rank borders ($|\text{rk}[j] - \text{rk}[l]| \le B$)**: test $2B$ neighbors $j$ of $\text{rk}[l]$ in SA. (Remaining borders have length $> B$ and $> B$ occurrences, handled by $O(N/B)$ periodic buckets). | $O(N \sqrt{N})$ | $O(\sqrt{N})$ | $O(N)$ | **Yes** |
| **Method 6: Runs Sweep-Line (`Runs Theorem`) + Short Fallback** | Any border $b \ge \lceil (r-l+1)/2 \rceil$ induces a period $p = (r-l+1) - b \le (r-l+1)/2$, meaning $S[l..r]$ is a tandem repeat covered by a **unique maximal periodic run** $R = [l_R, r_R, p]$ (`Wave 1B`)! Long borders reduce to 2D range queries over the $< N$ runs of $S$. | $O(N \log N)$ | $O(\log N)$ (for long borders) | $O(N)$ | Offline / Persistent |

##### Corollary 4.2 ($O(1)$ Internal Shortest Period Query via Bounded-Ratio IPM + Runs)
Given $U = S[l..r]$ of length $n = r - l + 1$, how do we find the **shortest period** $\text{per}(U) = n - \text{max\_border}(U)$ in $O(1)$ time (after $O(N \log N)$ preprocessing)?
1. **Case 1 ($\text{per}(U) \le n / 2$, i.e. $U$ is periodic with long border $b \ge n/2$)**:
   Let $2^k \le n/2 < 2^{k+1}$. Then $\text{per}(U)$ is the distance from $l$ to the **second occurrence** of $P_k = S[l .. l + 2^k - 1]$ inside $S[l .. l + 2^{k+1} - 1]$ (found via one IPM query), provided $\text{LCE}(l, l + p) \ge n - p$!
2. **Case 2 ($\text{per}(U) > n / 2$, i.e. $U$ is aperiodic with short border $b < n/2$)**:
   Here $b$ falls into a single dyadic scale $m$ where $P_m = S[l..l+2^m-1]$ occurs inside $S[r-2^{m+1}+2..r]$.

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Pitfall 1 (Improper Border $b = r - l + 1$ at $i = r$)**:
   - In Methods 2–4, querying $i \in [l, r]$ instead of $i \in [l, r-1]$ always matches $i = r$ ($\text{LCSuf}(r, r) = r \ge r - l + 1$), returning the improper full string $b = r - l + 1$. Always clip the query interval to $[l, r - 1]$.
2. **Pitfall 2 (False Period Extension Across Mismatches in Method 1)**:
   - *Counterexample*: $S = \texttt{"ababacababab"}$, query $[1, 12]$, scale $m = 1$ ($2^m = 2$). The prefix $P_1 = \texttt{"ab"}$ occurs at $x \in \{9, 11\}$ in the tail window, and the suffix $Q_1 = \texttt{"ab"}$ occurs at $y \in \{1, 3\}$ in the head window, even though character `'c'` at index $6$ breaks periodicity outside those windows! That is why Method 1 **must** intersect the AP of $P_m$ in the tail window $[r - 2^{m+1} + 2, r]$ with the AP of $Q_m$ in the head window $[l, l + 2^{m+1} - 2]$: for any candidate border length $b \in [2^m, 2^{m+1}-1]$, the prefix occurrence of $P_m$ (length $2^m$) and prefix occurrence of $Q_m$ (ending at $l+b-1$, length $2^m$) **together cover the entire length-$b$ prefix $S[l..l+b-1]$** (since $2^m + 2^m \ge b + 1$), leaving zero unverified gap characters!
3. **Pitfall 3 (Small-AP Step Mismatch When Intersecting APs of Size $\le 2$)**:
   - Theorem 4.1 guarantees step $d = \text{per}(P_m)$ only when an AP has $\ge 3$ elements! If either AP has $\le 2$ elements, test those $\le 2$ candidate border lengths $b$ directly in $O(1)$ via $\text{LCE}(l, r - b + 1) \ge b$ instead of running extended-GCD AP intersection.

---

### 4.3Frontier Extension: Kempa–Kociumaka $\tau$-Synchronizing Sets (STOC 2019)

While SA-IS (`§2`) uses LMS positions ($\tau = 1$ local minima of $\text{rk}$, compressing by $\le 1/2$) and Method 1 of `[BJWC2018]` uses $2^k$ dyadic blocks, **Kempa and Kociumaka (STOC 2019)** unified both into **$\tau$-Synchronizing Sets**:
- Given a parameter $\tau \ge 1$, a set of positions $\mathsf{S} \subseteq [1 .. N - 2\tau + 1]$ is a $\tau$-synchronizing set if:
  1. **Local Consistency**: $i \in \mathsf{S}$ depends **only** on the length-$2\tau$ substring $S[i .. i + 2\tau - 1]$.
  2. **Density Bound**: $|\mathsf{S}| = O(N / \tau)$ in all non-periodic regions.
  3. **Density / Covering Guarantee**: Every window $[i .. i + \tau - 1]$ where $S[i .. i + 3\tau - 2]$ does not have period $\le \tau/3$ contains **at least one** synchronizing position $s \in \mathsf{S}$!
- **Why this unifies Wave 2B**: Just as SA-IS aligns any two suffixes at their first LMS position (`Theorem 2.4`), a $\tau$-synchronizing set guarantees that any two matching substrings of length $\ge 3\tau$ (that are not periodic with period $\le \tau/3$) hit their first synchronizing position at the **exact same relative offset** $< \tau$!

---

## Section 5: Pillar IV — Bi-Directional Suffix Structures: SCDAWG, Affix Automata & Hash-Free Suffix Balanced Trees (`后缀平衡树`)

### 5.1 The Four-Way Substring Equivalence Hierarchy & Symmetric Compact DAWG (SCDAWG)

For a string $S[1..N]$, let $\text{endpos}_S(u)$ be the set of right endpoints and $\text{startpos}_S(u)$ be the set of left endpoints of occurrences of $u \in \text{Sub}(S)$:

| Equivalence Relation | Definition | Canonical Representative | Underlying Automaton / Tree |
| :--- | :--- | :--- | :--- |
| **1. Right-Context ($\equiv_R$)** | $\text{endpos}_S(u) = \text{endpos}_S(v)$ | Longest left-extension $\text{rep}_R([u]_R) = \vec{u}$ | **Forward SAM ($\text{DAWG}(S)$)**; Link Tree is $\mathcal{T}_{\text{ST}}(S^R)$ |
| **2. Left-Context ($\equiv_L$)** | $\text{startpos}_S(u) = \text{startpos}_S(v)$ | Longest right-extension $\text{rep}_L([u]_L) = \overleftarrow{u}$ | **Suffix Tree $\mathcal{T}_{\text{ST}}(S)$** (Link Tree of $\text{SAM}(S^R)$) |
| **3. Two-Sided Closure ($\overleftrightarrow{u}$)** | Maximal left & right deterministic extension | **Maximal Repeat (Prime Factor)** $\overleftrightarrow{u}$ | **Symmetric Compact DAWG ($\text{SCDAWG}(S)$)** (Inenaga et al. 2001/2005) |
| **4. Coupled Left + Right ($\mathcal{T}_{\text{ST}}(S) \leftrightarrow \mathcal{T}_{\text{ST}}(S^R)$)** | Explicit branching nodes on both sides | Bi-directional prefix/suffix cross-links | **Affix Tree / Affix Automaton** (Stoye 2000; Maaß 2000) |

#### Theorem 5.1 (Commutativity of Left/Right Closure & Linear SCDAWG Bound — Blumer et al. 1987; Inenaga et al. 2001/2005)
For any substring $u \in \text{Sub}(S)$, extending $u$ maximally to the left within $[u]_R$ and maximally to the right within $[u]_L$ **commutes**:

$$
\text{rep}_L\big([\text{rep}_R([u]_R)]_L\big) = \text{rep}_R\big([\text{rep}_L([u]_L)]_R\big) =: \overleftrightarrow{u}.
$$

Moreover, every internal vertex $\overleftrightarrow{u}$ of $\text{SCDAWG}(S)$ is simultaneously an explicit branching node of $\mathcal{T}_{\text{ST}}(S)$ and an explicit branching node of $\mathcal{T}_{\text{ST}}(S^R)$, bounding the number of internal bi-maximal vertices by **at most $N - 1$** and supporting online `push_front(c)` and `push_back(c)` in $O(N \log |\Sigma|)$ total time!

#### Theorem 5.2 (Ukkonen–Weiner Frontier Duality Under `push_front` & `push_back`)
Let $L_{\max}(S)$ be the longest prefix of $S$ occurring at least twice in $S$, and $R_{\max}(S)$ be the longest suffix of $S$ occurring at least twice in $S$:
- **`push_back(c)` ($S \leftarrow Sc$)**: Adds $\Delta_{\text{distinct}} = |Sc| - |R_{\max}(Sc)|$ new distinct substrings. On $\mathcal{T}_{\text{ST}}(S)$, Ukkonen's active suffix point advances along suffix links; on $\mathcal{T}_{\text{ST}}(S^R)$, Weiner's algorithm inserts a **single new leaf** $c S^R$ at $R_{\max}^R$.
- **`push_front(c)` ($S \leftarrow cS$)**: Adds $\Delta_{\text{distinct}} = |cS| - |L_{\max}(cS)|$ new distinct substrings. On $\mathcal{T}_{\text{ST}}(S^R)$, Ukkonen's active prefix point advances; on $\mathcal{T}_{\text{ST}}(S)$, Weiner's algorithm inserts a **single new leaf** $cS$ at $L_{\max}$.

---

### 5.2 The 4-Step Derivation of the Hash-Free Suffix Balanced Tree (`后缀平衡树`)

#### Step 1: The Diagnostic Signal (Online Encrypted Front-Prepend / Tree-Branched Suffix Order)

Suppose a problem maintains a string $S$ online under **encrypted** character additions (`[BZOJ 3682] Phorni`, `[BZOJ 4768] wxh loves substring`), front deletions, or persistent tree-version branching, and requires:
- Real-time $O(1)$ lexicographical comparison of any two existing suffixes (`[BZOJ 3682]`),
- Real-time count of pattern occurrences $T$ in $S$ in $O(|T| + \log N)$ time, or
- Real-time maintenance of distinct substrings under `push_front(c)` and `pop_front()`.

#### Step 2: The Combinatorial Word Invariant (Dietz–Sleator Dyadic Tags + Hash-Free BST LCP)

##### Theorem 5.3 (Suffix Balanced Tree $O(1)$ Tag Comparison & Hash-Free LCP Invariant)
Maintain all suffixes $\text{suf}(1), \dots, \text{suf}(n-1)$ of $S$ (where index $i$ denotes the suffix of length $i$ after $i$ left-prepends, so $\text{suf}(n) = c \cdot \text{suf}(n-1)$) in an **$\alpha$-Weight-Balanced BST (Scapegoat Tree with $\alpha = 0.75$)**. Assign the root the integer tag range $[0, 2^{62}]$, and recursively assign each node $x$ with range $[L_x, R_x]$ the midpoint tag:

$$
\text{tag}[x] = \frac{L_x + R_x}{2} \in \mathbb{Z}_{\ge 0},
$$

passing $[L_x, \text{tag}[x]]$ to its left child and $[\text{tag}[x], R_x]$ to its right child.
1. **$O(1)$ Existing-Suffix Comparison**: For any two existing suffixes $i, j \in \{1, \dots, n-1\}$, $\text{suf}(i) < \text{suf}(j) \iff \text{tag}[i] < \text{tag}[j]$ in $O(1)$ time.
2. **$O(1)$ New-Suffix Comparison During BST Insertion**: When inserting $\text{suf}(n) = c \cdot \text{suf}(n-1)$ and comparing against a visited BST node $u$:
   $$
   \text{suf}(n) \lessgtr \text{suf}(u) \iff \big(c, \; \text{tag}[n-1]\big) \lessgtr \big(S[u], \; \text{tag}[u-1]\big) \quad \text{in } O(1) \text{ time!}
   $$
3. **Hash-Free $O(\log n)$ Dynamic LCP Bootstrapping**: Once $\text{suf}(n)$ is inserted between BST predecessor $u^-$ and successor $u^+$, its adjacent LCP with $u^-$ (and symmetrically $u^+$) satisfies:
   $$
   \text{LCP}(\text{suf}(n), u^-) = \begin{cases} 0 & \text{if } S[n] \ne S[u^-], \\ 1 + \text{LCP}(\text{suf}(n-1), u^- - 1) & \text{if } S[n] = S[u^-], \end{cases}
   $$
   where $\text{LCP}(\text{suf}(n-1), u^- - 1)$ is evaluated in **$O(\log n)$ deterministic time** by querying the minimum adjacent `height` in the BST interval between nodes $n-1$ and $u^- - 1$!

**Proof**: Because $\alpha = 0.75$, the depth of the Scapegoat Tree never exceeds $\lfloor \log_{4/3} n \rfloor + 1 \le 49$ for $n \le 10^6$, so integer halving of $[0, 2^{62}]$ never collapses $L_x = R_x$. When a subtree of size $s$ violates the weight-balance condition $\max(\text{sz}(L), \text{sz}(R)) \le \alpha \cdot s$, flattening and rebuilding it into a perfectly balanced binary tree reassigns tags in $O(s)$ time ($O(\log n)$ amortized per insertion) while **preserving the relative order of all $\text{tag}[\cdot]$ values**! Finally, since every node in the BST stores its `height` with its inorder predecessor and the subtree minimum of `height`, $\text{LCP}(x, y)$ between any two existing nodes $x, y$ (found via their tags) is a standard BST range minimum query in $O(\log n)$ time. $\blacksquare$

#### Step 3: The Reverse-Engineering Scratchpad (Contest Decision Filter for Bi-Directional Problems)

1. **Filter 1 (Unencrypted Deque $\to$ Offline Static IPM)**: If operations are not encrypted, pre-simulate the deque to place the final string in $M[1..N]$ so time $t$ is a substring $M[l_t..r_t]$; solve offline via SAM + LCT or SA + 2D Fenwick.
2. **Filter 2 (Encrypted One-Ended Append/Prepend + Suffix Order Queries $\to$ Suffix Balanced Tree)**: Orient additions as `push_front(c)` (reversing the string if additions are `push_back(c)` and queries ask about reversed prefixes!) and maintain the Scapegoat Suffix Balanced Tree with 64-bit integer tags.
3. **Filter 3 (Encrypted Both-Ends `push_front` & `push_back` $\to$ Online SCDAWG / Coupled Suffix-Prefix Trees)**: Maintain the coupled active prefix point $L_{\max}$ and active suffix point $R_{\max}$ (`Theorem 5.2`).

#### Step 4: Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Pitfall 1 (`push_back(c)` Flips Existing Suffix Order — The `"aa" -> "aab"` Counterexample)**:
   - In $S = \texttt{"aa"}$, $\text{suf}(1) = \texttt{"aa"} > \text{suf}(2) = \texttt{"a"}$. After `push_back('b')` ($S = \texttt{"aab"}$), $\text{suf}(1) = \texttt{"aab"} < \text{suf}(2) = \texttt{"ab"}$! Their relative order **flipped** because $\text{suf}(2)$ was a proper prefix (border) of $\text{suf}(1)$ before `'b'` was appended. Thus a Suffix Balanced Tree can **only** insert at the **front** (`push_front`) of the strings it sorts!
2. **Pitfall 2 (53-Bit `double` Tag Underflow in Randomized Treaps)**:
   - Using `double` tags in a Treap without strict depth bounding overflows the 53-bit mantissa whenever depth $\ge 53$, causing `tag[u] == tag[v]` for distinct suffixes. Always use a **Scapegoat Tree ($\alpha = 0.75$)** with `uint64_t` tags in $[0, 2^{62}]$.

---

## Section 6: Consolidated Multilingual Bibliography & Terminology Rosetta Stone (`[EN]` / `[ZH]` / `[JA]`)

### 6.1 Master Academic & Competitive Stringology Bibliography (Wave 2B)

1. **[EN] Nong, G., Zhang, S., & Chan, W. H. (2009 / 2011)**. *"Linear Suffix Array Construction by Almost Pure Induced-Sorting"* (DCC 2009, pp. 193–202) & *"Two Efficient Algorithms for Linear Time Suffix Array Construction"* (IEEE Transactions on Computers, 60(10), 1471–1484, 2011). — Introduces SA-IS, $L/S$ suffix classification, LMS substrings, and two-pass induced sorting.
2. **[EN] Fischer, J. (2011)**. *"Inducing the LCP-Array"* (WADS 2011, LNCS 6844, pp. 374–385). — Proves how to induce the `height` (LCP) array directly inside the SA-IS passes in $O(N)$ time.
3. **[EN] Kasai, T., Lee, G., Arimura, H., Arikawa, S., & Park, K. (2001)** & **Abouelhoda, M. I., Kurtz, S., & Ohlebusch, E. (2004)**. *"Linear-Time Longest-Common-Prefix Computation in Suffix Arrays and Its Applications"* (CPM 2001) & *"Replacing Suffix Trees with Enhanced Suffix Arrays"* (J. Discrete Algorithms, 2(1), 53–86). — Establishes the isomorphism between the Suffix Tree and the Cartesian interval tree of `height`.
4. **[EN] Kociumaka, T., Radoszewski, J., Rytter, W., & Waleń, T. (2015 / 2024)**. *"Internal Pattern Matching Queries in a Text and Applications"* (SODA 2015, pp. 532–551; SIAM Journal on Computing, 53(5), 2024). — Formalizes the Basic Substring Dictionary, Bounded-Ratio IPM Arithmetic Progression Theorem, internal period/border queries, and substring rank.
5. **[EN] Kociumaka, T. (2018 / 2019)** & **Kempa, D., & Kociumaka, T. (2019)**. *"Efficient Data Structures for Internal Queries in Texts"* (PhD Dissertation, University of Warsaw, 2018) & *"String Synchronizing Sets: Sublinear-Time BWT Construction and Optimal LCE Data Structure"* (STOC 2019, pp. 756–767). — Introduces $\tau$-synchronizing sets and optimal internal string queries.
6. **[EN] Blumer, A., Blumer, J., Haussler, D., McConnell, R., & Ehrenfeucht, A. (1987)** & **Inenaga, S., Hoshino, H., Shinohara, A., Takeda, M., Arikawa, S., Mauri, G., & Pavesi, G. (2001 / 2005)**. *"Complete Inverted Files for Efficient Text Retrieval and Analysis"* (JACM 34(3), 578–595) & *"On-Line Construction of Symmetric Compact Directed Acyclic Word Graphs"* (SPIRE 2001; Discrete Applied Mathematics 146(2), 156–179, 2005). — Proves two-sided closure commutativity ($\overleftrightarrow{u}$) and $O(N \log |\Sigma|)$ bi-directional online SCDAWG construction.
7. **[EN] Stoye, J. (2000)**, **Maaß, M. G. (2000)**, & **Breslauer, D., & Italiano, G. F. (2013)**. *"Affix Trees"*, *"Linear Bidirectional On-Line Construction of Affix Trees"* (CPM 2000), & *"Near Real-Time Suffix Tree Construction via the Fringe Marked Ancestor Problem"* (J. Discrete Algorithms 2013).
8. **[EN] Dietz, P. F., & Sleator, D. D. (1987)**. *"Two Algorithms for Maintaining Order in a List"* (STOC 1987, pp. 365–372). — Order-maintenance tag invariants underlying Suffix Balanced Trees (`后缀平衡树`).
9. **[ZH] 金策 (Jin Ce, 2019)**. 《字符串算法选讲》 (*Selected Topics in String Algorithms*, 2019 Chinese IOI National Team Training Paper `国家集训队论文`). — Definitive competitive stringology treatise on Internal Pattern Matching (IPM), `[BJWC2018] Border 的四种求法`, Runs, and Significant Suffixes.
10. **[ZH] 陈立杰 (Chen Lijie / WJMZBMR, 2014)**, **张天扬 (Zhang Tianyang, 2015)**, & **国家集训队论文 — 支配对理论 (Dominant Pairs Treatises)**. — Formalizes SAM Link Tree $\leftrightarrow$ Suffix Tree duality, Virtual Suffix Trees (`后缀树虚树`), Suffix Balanced Trees (`后缀平衡树`), and DSU-on-Tree Dominant Pairs (`启发式合并支配对`).
11. **[JA] AtCoder Library (`ACL` — `atcoder::suffix_array`)**, **`noshi91`**, **`maspypy`**, & **`henkoku` Treatises**:
    - `noshi91`: *"SA-IS の正当性証明と実装"* & *"LCP 配列の Cartesian Tree と接尾辞木"*.
    - `henkoku`: *"Internal Pattern Matching (内部パターンマッチング) と 부분文字列周期・Border クエリ"*.

### 6.2 Multilingual Stringology Rosetta Stone (Wave 2B)

| Concept (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) | Core Structural Meaning |
| :--- | :--- | :--- | :--- |
| **Induced Sorting (SA-IS)** | 诱导排序 (`SA-IS`) | 誘導ソート (`SA-IS`) | $O(N)$ suffix sorting via $L/S$ buckets & LMS recursion |
| **LMS Position / Substring** | LMS 字符 / 最左 S 型子串 | LMS 文字 / LMS 部分文字列 | Local valley $\text{type}(i)=S, \text{type}(i-1)=L$ ($\le \lfloor N/2 \rfloor$) |
| **`height` Cartesian Tree** | `height` 数组的笛卡尔树 | `LCP` 配列の Cartesian Tree | Min-heap tree on adjacent LCPs, isomorphic to $\mathcal{T}_{\text{ST}}(S)$ |
| **Virtual Suffix Tree** | 后缀树虚树 / 虚后缀树 | 圧縮接尾辞木 / Auxiliary Tree | Compressed tree of $O(k)$ query substrings sorted by $\text{rk}$ + adjacent LCAs |
| **Dominant Pairs on Suffix Tree** | 后缀树支配对 (`启发式合并支配对`) | 接尾辞木上の支配ペア | $\le 2N \log_2 N$ predecessor/successor pairs $(i^-, i, \ell_u)$ from DSU-on-Tree |
| **Internal Pattern Matching (IPM)** | 内部模式匹配 / 基本子串字典 | 内部パターンマッチング (`IPM`) | Occurrences of $S[l_1..r_1]$ in $S[l_2..r_2]$ ($|T| < 2|P|$) as a single AP |
| **Internal Border Query** | 区间 Border 查询 (`Border 的四种求法`) | 部分文字列の最大 Border クエリ | Longest border of $S[l..r]$ via dyadic IPM or Link-Tree HLD/Centroid |
| **$\tau$-Synchronizing Set** | $\tau$-同步集 (`字符串同步集`) | $\tau$-同期集合 (Synchronizing Set) | Locally consistent $O(N/\tau)$-sparse anchors (Kempa–Kociumaka 2019) |
| **Symmetric Compact DAWG** | 对称压缩有向无环词图 (`SCDAWG`) | 対称圧縮 DAWG (`SCDAWG`) | Bi-directional automaton of maximal repeats ($\overleftrightarrow{u}$) |
| **Suffix Balanced Tree** | 后缀平衡树 | 接尾辞平衡二分探索木 | Scapegoat BST with 64-bit tags & hash-free BST LCP for `push_front` |

---

## Section 7: Reconciled Master Non-Template Problem Archive (`W2B-01` to `W2B-42`)

This master archive unifies all accepted non-template problems from Cohort 1 (`#1`–`#32`) and Cohort 2 (`#1`–`#33`) plus frontier additions into **42 deduplicated problems (`W2B-01` to `W2B-42`)** structured along a smooth 4-Tier Difficulty Ladder, each with a complete **4-Step "Zero Magic Invariants & Structural Decompositions" Analysis**.

---

### Tier 1: Stepping Stone (`W2B-01` to `W2B-10` — `height` Cartesian Trees, Monotonic Stack LCP, DSU Merge & Cyclic SA-IS)

#### `W2B-01`. `[AHOI2013] 差异` (Luogu P4248) — `[ZH]` *(Cohort 1 #1 / Cohort 2 #1)*
- **Statement & Constraints**: Given a string $S[1..N]$ ($N \le 5 \times 10^5$), compute $\sum_{1 \le i < j \le N} \big(|\text{suf}(i)| + |\text{suf}(j)| - 2 \cdot \text{LCP}(\text{suf}(i), \text{suf}(j))\big)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Naive $O(N^2)$ pair enumeration TLEs. Separating the sum gives $\frac{N(N-1)(N+1)}{2} - 2 \sum_{1 \le x < y \le N} \text{LCP}(\text{SA}[x], \text{SA}[y])$.
  2. *Combinatorial Invariant*: By the LCP Interval Theorem, $\text{LCP}(\text{SA}[x], \text{SA}[y]) = \min_{x < k \le y} H[k]$. In the Min-Cartesian tree of $H[2..N]$, node $k$ with span $[L_k, R_k]$ is the unique minimum split point for $(k - L_k + 1)(R_k - k + 1)$ pairs of suffixes.
  3. *Algorithmic Compilation*: Use a monotonic stack over $H[2..N]$ with strict inequality $H[j] > H[k]$ on the left ($j \in [L_k, k-1]$) and non-strict inequality $H[j] \ge H[k]$ on the right ($j \in [k+1, R_k]$). Sum $H[k] (k - L_k + 1)(R_k - k + 1)$ in $O(N)$ time.
  4. *Boundary Pitfall*: Using strict `>` on both sides drops pairs when $H$ contains duplicate minimum values; use 64-bit / 128-bit integers for the $\Theta(N^3)$ sum.

#### `W2B-02`. `CF 873F — Forbidden Indices` — `[EN]` *(Cohort 1 #2 / Cohort 2 #2)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and a binary mask $B[1..N]$ marking forbidden starting indices, maximize $|P| \cdot \text{occ}_{\text{allowed}}(P)$ over all substrings $P$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Only non-forbidden suffixes ($B[i] = 0$) contribute to $\text{occ}_{\text{allowed}}(P)$.
  2. *Combinatorial Invariant*: Every equivalence class of substrings with $\ge 2$ occurrences corresponds to a Cartesian tree interval $[L_k-1, R_k]$ in $\text{SA}$ with string depth $H[k]$ and allowed occurrence count $\text{pref}[R_k] - \text{pref}[L_k-2]$, where $\text{pref}[x] = \sum_{t=1}^x (1 - B[\text{SA}[t]])$.
  3. *Algorithmic Compilation*: Check the single longest allowed suffix ($\text{occ} = 1$: $\max_{B[i]=0} (N - i + 1)$). For $\text{occ} \ge 2$, find $[L_k, R_k]$ for each $k \in [2..N]$ via monotonic stack and maximize $H[k] \cdot (\text{pref}[R_k] - \text{pref}[L_k-2])$.
  4. *Boundary Pitfall*: Omitting the $\text{occ} = 1$ leaf case fails when a single long allowed suffix outscores all repeated substrings!

#### `W2B-03`. `CF 802I — Fake News (hard)` — `[EN]` *(Cohort 1 #3 / Cohort 2 #3)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), compute $\sum_{P \in \text{Sub}(S)} \text{occ}(P)^2$ over all distinct non-empty substrings $P$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: We sum $\text{occ}(P)^2$ over **distinct** substrings $P$, not pairs of suffixes directly.
  2. *Combinatorial Invariant*: Two equivalent formulations: (a) On the Cartesian tree of $H[2..N]$, node $u$ with interval $[L_u, R_u]$ ($\text{sz}(u) = R_u - L_u + 1$) and parent height $h_{p(u)}$ represents $h_u - h_{p(u)}$ distinct substrings, contributing $(h_u - h_{p(u)}) \cdot \text{sz}(u)^2$; (b) By double counting ordered pairs of occurrences, $\sum_{P \in \text{Sub}(S)} \text{occ}(P)^2 = \sum_{i=1}^N \sum_{j=1}^N \text{LCP}(\text{suf}(i), \text{suf}(j)) = \frac{N(N+1)}{2} + 2 \sum_{1 \le i < j \le N} \text{LCP}(\text{suf}(i), \text{suf}(j))$!
  3. *Algorithmic Compilation*: Either sum $(h_u - h_{p(u)}) \text{sz}(u)^2$ over all Cartesian tree nodes and leaves, or compute $\frac{N(N+1)}{2} + 2 \sum_{k=2}^N H[k](k - L_k + 1)(R_k - k + 1)$ in $O(N)$.
  4. *Boundary Pitfall*: Forgetting the $\text{occ}(P) = 1$ leaf substrings (in formulation a) or the $i = j$ diagonal $\frac{N(N+1)}{2}$ (in formulation b).

#### `W2B-04`. `[NOI2015] 品酒大会` (Luogu P2178 / UOJ #131) — `[ZH]` *(Cohort 1 #4 / Cohort 2 #4)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^5$) and integer weights $a_i \in [-10^9, 10^9]$, for every threshold $r \in [0, N-1]$ find (1) the number of pairs $(i < j)$ with $\text{LCP}(\text{suf}(i), \text{suf}(j)) \ge r$, and (2) the maximum product $a_i \cdot a_j$ among such pairs.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: We need connected component statistics of the Suffix Tree across all height thresholds $r \in [0, N-1]$ with signed weights $a_i \in [-10^9, 10^9]$.
  2. *Combinatorial Invariant*: Sweeping $r$ from $N-1$ down to $0$ is isomorphic to Kruskal's DSU reconstruction tree merging adjacent SA indices $(k-1, k)$ when $H[k] = r$ (`§3.2`, Engine B).
  3. *Algorithmic Compilation*: Sort $k \in [2..N]$ by $H[k]$ descending. Maintain DSU with $(\text{sz}, \max_1, \min_1)$. On merging $u, v$ at $r = H[k]$, add $\text{sz}[u]\text{sz}[v]$ to `cnt[r]` and update `ans[r]` with $\max(\max_1[u]\max_1[v], \min_1[u]\min_1[v])$; take suffix sums/maxima from $N-1$ down to $0$.
  4. *Boundary Pitfall*: Two negative weights multiply to a positive product, so $\min_1$ must be tracked alongside $\max_1$, and `ans[r]` must be initialized to $-\infty$ (not $0$).

#### `W2B-05`. `[HAOI2016] 找相同字符` (Luogu P3181) — `[ZH]` *(Cohort 1 #5 / Cohort 2 #6)*
- **Statement & Constraints**: Given two strings $S_1, S_2$ ($|S_1|, |S_2| \le 2 \times 10^5$), count the number of equal substring pairs $(S_1[l_1..r_1], S_2[l_2..r_2])$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Equal to $\sum_{i \in S_1} \sum_{j \in S_2} \text{LCP}(\text{suf}_{S_1}(i), \text{suf}_{S_2}(j))$.
  2. *Combinatorial Invariant*: By inclusion-exclusion on $S_1 \# S_2$, $\text{Cross}(S_1, S_2) = \text{All}(S_1 \# S_2) - \text{All}(S_1) - \text{All}(S_2)$, or via bi-colored subtree sizes $(\text{cnt}_1(u), \text{cnt}_2(u))$ on the Cartesian tree of $H$.
  3. *Algorithmic Compilation*: Run the `[AHOI2013] 差异` monotonic stack LCP sum on $S_1 \# S_2$, $S_1$, and $S_2$.
  4. *Boundary Pitfall*: Ensure the separator `#` is outside $\Sigma$ so $\text{LCP}$ never crosses `#`.

#### `W2B-06`. `CF 123D — String` — `[EN]` *(Cohort 1 #6 / Cohort 2 #7)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), compute $\sum_{P \in \text{Sub}(S)} \frac{\text{occ}(P)(\text{occ}(P)+1)}{2}$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Decompose $\frac{k(k+1)}{2} = \binom{k}{2} + k$.
  2. *Combinatorial Invariant*: $\sum_{P \in \text{Sub}(S)} \binom{\text{occ}(P)}{2} = \sum_{1 \le i < j \le N} \text{LCP}(\text{suf}(i), \text{suf}(j))$ and $\sum_{P \in \text{Sub}(S)} \text{occ}(P) = \frac{N(N+1)}{2}$.
  3. *Algorithmic Compilation*: Compute $\frac{N(N+1)}{2} + \sum_{k=2}^N H[k](k - L_k + 1)(R_k - k + 1)$ in $O(N)$ time.
  4. *Boundary Pitfall*: Use 64-bit integers throughout.

#### `W2B-07`. `[JSOI2007] 字符加密` (Luogu P4051) — `[ZH]` *(Cohort 2 #5)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$), sort all $N$ cyclic shifts of $S$ (breaking ties by starting index) and output the last character of each sorted shift (the BWT $L$-column).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Suffixes must wrap around index $N \to 1$ cyclically.
  2. *Combinatorial Invariant*: Concatenating $U = S \cdot S[1..N-1] \cdot \$$ ensures that any two cyclic shifts $S^{(i)}, S^{(j)}$ ($i < j$) are compared through their full length $N$, and if $S^{(i)} = S^{(j)}$, the shorter remaining suffix (larger index $j$) hits $\$$ first, breaking ties deterministically.
  3. *Algorithmic Compilation*: Build SA-IS on $U$ of length $2N$, scan $\text{SA}[k]$, and output $S[(\text{SA}[k] + N - 2) \bmod N + 1]$ whenever $\text{SA}[k] \le N$.
  4. *Boundary Pitfall*: Omitting the sentinel $\$$ at the end of $S \cdot S[1..N-1]$ can invert equal cyclic shifts when $S[N]$ is larger than adjacent characters.

#### `W2B-08`. `AtCoder ABC 213 F — Common Prefixes` — `[JA]` *(Cohort 1 #8)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6$), for every $k = 1, \dots, N$ compute $\sum_{j=1}^N \text{LCP}(\text{suf}(k), \text{suf}(j))$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Requires per-suffix LCP sums for all $k \in [1..N]$ at $N = 10^6$.
  2. *Combinatorial Invariant*: Split $j$ into $\text{rk}[j] < \text{rk}[k]$ and $\text{rk}[j] > \text{rk}[k]$. As $r = \text{rk}[k]$ sweeps from $1$ to $N$, the suffix minimums $\min_{l < t \le r} H[t]$ for $l < r$ form a step-function histogram maintained by a monotonic stack!
  3. *Algorithmic Compilation*: Build SA-IS + $H$ in $O(N)$. Sweep $r = 1 \to N$ and $r = N \to 1$ maintaining a monotonic stack of `(height, count)` and the running rectangle sum in $O(N)$ total time.
  4. *Boundary Pitfall*: $O(N \log N)$ doubling SA risks TLE at $N = 10^6$; SA-IS runs in $< 50$ ms.

#### `W2B-09`. `AtCoder ABC 272 F — Two Strings` — `[JA]` *(Cohort 1 #11 / Cohort 2 #8)*
- **Statement & Constraints**: Given $S, T$ of length $N \le 2 \times 10^5$, count pairs $(i, j) \in [0, N-1]^2$ such that cyclic shift $S^{(i)} \le_{\text{lex}} T^{(j)}$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Cyclic shift comparison across two strings with $\le$ tie-breaking when $S^{(i)} = T^{(j)}$.
  2. *Combinatorial Invariant*: In $U = S \cdot S \cdot (\texttt{'a'}-1) \cdot T \cdot T \cdot (\texttt{'z'}+1)$, for any $i, j \in [1..N]$, $\text{suf}_U(i) < \text{suf}_U(2N + 1 + j) \iff S^{(i)} \le T^{(j)}$! Why? Because if $S^{(i)} = T^{(j)}$, their length-$2N$ extensions in $S \cdot S$ and $T \cdot T$ are also equal, and at the end of $S \cdot S$ the sentinel $\texttt{'a'}-1$ is strictly smaller than every character in $T \cdot T \cdot (\texttt{'z'}+1)$.
  3. *Algorithmic Compilation*: Run SA-IS on $U$ (length $4N+2$) and count pairs with $i \in [1..N]$ preceding $j \in [2N+2..3N+1]$ in $\text{SA}$.
  4. *Boundary Pitfall*: Using the same sentinel after $S \cdot S$ and $T \cdot T$ orders some equal cyclic shifts $T^{(j)} < S^{(i)}$ and undercounts ties.

#### `W2B-10`. `[SDOI2016] 生成魔咒` (Luogu P4070) — `[ZH]` *(Cohort 1 #7 / Cohort 2 #12)*
- **Statement & Constraints**: Characters $x_1, \dots, x_N$ ($N \le 10^5, x_i \le 10^9$) are appended one by one to $S$. After each append, output the number of distinct substrings.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Large alphabet $10^9$ and incremental distinct substring count.
  2. *Combinatorial Invariant*: Reversing the string turns `push_back` on $S$ into `push_front` on $S^R$! Adding suffix $k$ to $S^R$ increases distinct substrings by $|S^R[k..N]| - \max(\text{LCP}(k, \text{pred}), \text{LCP}(k, \text{succ}))$, where `pred` and `succ` are the active neighbors in $\text{SA}_{S^R}$.
  3. *Algorithmic Compilation*: Offline: build SA + $H$ on coordinate-compressed $S^R$, and delete suffixes in reverse time order $t = N \dots 1$ using a doubly linked list over $\text{SA}$ in $O(N \log N)$ total time. Online: use a Suffix Balanced Tree (`§5.2`).
  4. *Boundary Pitfall*: Standard array-transition SAM MLEs on $|\Sigma| = 10^9$; the offline SA + doubly-linked list uses $O(N)$ memory and zero hash/map overhead.

---

### Tier 2: Intermediate (`W2B-11` to `W2B-21` — Virtual Suffix Trees `后缀树虚树`, Concatenation LCE & Substring Containment)

#### `W2B-11`. `CF 1073G — Yet Another LCP Problem` — `[EN]` *(Cohort 1 #9 / Cohort 2 #9)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries specifying suffix sets $A_q, B_q$ ($\sum (|A_q| + |B_q|) \le 2 \times 10^5$), compute $\sum_{i \in A_q} \sum_{j \in B_q} \text{LCP}(\text{suf}(i), \text{suf}(j))$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Canonical Virtual Suffix Tree (`后缀树虚树`) problem over dynamic query subsets.
  2. *Combinatorial Invariant*: By Theorem 3.1, sorting $A_q \cup B_q$ by $\text{rk}[\cdot]$ reduces all pairwise LCPs to range minimums over the $m-1$ adjacent LCPs $h_t = \text{LCP}(u_{t-1}, u_t)$.
  3. *Algorithmic Compilation*: Sort $A_q \cup B_q$ by $\text{rk}$, add $(N - i + 1)$ for $i \in A_q \cap B_q$, deduplicate into $u_1, \dots, u_m$ with weights $(w_A, w_B)$, compute $h_t = \text{RMQ}_H(\text{rk}[u_{t-1}]+1, \text{rk}[u_t])$, and run Cartesian-tree DP summing $h_t (W_{A,L} W_{B,R} + W_{B,L} W_{A,R})$.
  4. *Boundary Pitfall*: Passing duplicate suffixes $\text{rk}[u] = \text{rk}[v]$ into $\text{RMQ}(\text{rk}[u]+1, \text{rk}[v])$ creates an invalid empty range $[r+1, r]$.

#### `W2B-12`. `[HEOI2016 / TJOI2016] 字符串` (Luogu P4094) — `[ZH]` *(Cohort 1 #10 / Cohort 2 #10)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$) and $Q \le 10^5$ queries $(a, b, c, d)$, find the maximum $L \le d - c + 1$ such that $S[c .. c+L-1]$ occurs as a substring of $S[a..b]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Substring containment in a clipped range $S[a..b]$; binary search on length $L$.
  2. *Combinatorial Invariant*: $S[c..c+L-1]$ occurs in $S[a..b]$ iff there exists a starting index $x \in [a, b - L + 1]$ with $\text{LCE}(c, x) \ge L$, which means $\text{rk}[x] \in [L_{\text{SA}}(c, L), R_{\text{SA}}(c, L)]$.
  3. *Algorithmic Compilation*: Binary search $L \in [1, \min(b-a+1, d-c+1)]$. Find $[L_{\text{SA}}(c, L), R_{\text{SA}}(c, L)]$ via RMQ binary search around $\text{rk}[c]$, and query a Persistent Segment Tree over $\text{SA}$ for whether any point in $[L_{\text{SA}}, R_{\text{SA}}]$ has value in $[a, b - L + 1]$. Time: $O(Q \log^2 N)$.
  4. *Boundary Pitfall*: Querying $[a, b]$ instead of $[a, b - L + 1]$ allows occurrences that start inside $[a, b]$ but overflow past $b$!

#### `W2B-13`. `CF 504E — Misha and LCP on Tree` — `[EN]` *(Cohort 1 #12 / Cohort 2 #11)*
- **Statement & Constraints**: Given a character-labeled tree of $N \le 3 \times 10^5$ nodes, answer $Q \le 10^6$ queries asking for the LCP of the string on simple path $(u_1 \to v_1)$ and simple path $(u_2 \to v_2)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Each tree path is a concatenation of $\le 2 \log_2 N$ Heavy-Light Decomposition (HLD) chain segments.
  2. *Combinatorial Invariant*: Concatenating the HLD Euler tour string $M$ with its reversal $M^R$ represents every path segment (upward or downward) as a contiguous substring of $M \cdot M^R$. By the Basic Substring Dictionary (`§4.1`), comparing two concatenations of $k$ substrings takes $O(k)$ $O(1)$-LCE jumps.
  3. *Algorithmic Compilation*: Build SA-IS + $O(1)$ RMQ on $M \cdot M^R$. For each query, extract the $\le 2 \log_2 N$ intervals for both paths and advance two pointers by $\min(\text{LCE}, \text{len}_1, \text{len}_2)$ in $O(\log N)$ time per query.
  4. *Boundary Pitfall*: At $Q = 10^6$, binary searching the LCP via rolling hash takes $O(Q \log^2 N)$ and TLEs; two-pointer $O(1)$ LCE piece exhaustion runs in $O(Q \log N)$.

#### `W2B-14`. `[JSOI2016] 扭动的回文串` (Luogu P4324) — `[ZH]` *(Cohort 1 #13)*
- **Statement & Constraints**: Given $A[1..N]$ and $B[1..N]$ ($N \le 10^5$), find the longest palindrome of the form $A[l_1..r_1]$, $B[l_2..r_2]$, or $A[i..j] \cdot B[j..k]$ ($i \le j \le k$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: A hybrid palindrome $A[i..j] \cdot B[j..k]$ has a palindromic core centered in $A$ (or $B$) and symmetric outer wings matching between $A$ going left and $B$ going right.
  2. *Combinatorial Invariant*: For any center $c$ in $A$ (or $B$), it is always optimal to expand the inner palindrome maximally inside $A$ to $[l, r]$ using Manacher's algorithm first, and then jump across the $A \to B$ seam by $\text{LCE}(A^R\text{ from }l-1, \; B\text{ from }r)$!
  3. *Algorithmic Compilation*: Run Manacher on $A$ and $B$, build SA + $O(1)$ RMQ on $A^R \# B$, and test $\text{LCE}(A^R[l-1], B[r])$ at all $2N$ Manacher centers in $O(N)$ time.
  4. *Boundary Pitfall*: Because $A[i..j] \cdot B[j..k]$ includes index $j$ in **both** substrings, when switching from $A[l..r]$ to $B$, the right wing in $B$ starts at index $r$ while the left wing in $A$ continues at $l - 1$.

#### `W2B-15`. `CF 616F — Expensive Strings` — `[EN]` *(Cohort 1 #14 / Cohort 2 #13)*
- **Statement & Constraints**: Given $M$ strings $S_1, \dots, S_M$ ($\sum |S_i| \le 5 \times 10^5$) with signed costs $c_1, \dots, c_M \in [-10^7, 10^7]$, maximize $|P| \cdot \sum_{i=1}^M c_i \cdot \text{occ}(P, S_i)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Generalized Suffix Tree / `height` Cartesian tree with signed leaf weights.
  2. *Combinatorial Invariant*: On the Generalized SA of $S_1 \dots S_M$, cap each suffix $p \in S_i$'s length at $\text{rem}(p) = \text{end}(S_i) - p + 1$ and cap $H[k] \leftarrow \min(H[k], \text{rem}(\text{SA}[k-1]), \text{rem}(\text{SA}[k]))$.
  3. *Algorithmic Compilation*: Evaluate Cartesian tree nodes $[L_k-1, R_k]$ **only when** $H[k] > \max(H[L_k-1], H[R_k+1])$, plus single-suffix leaves when $\text{rem}(\text{SA}[x]) > \max(H[x], H[x+1])$.
  4. *Boundary Pitfall*: Because $c_i$ can be negative, evaluating an uncontracted Cartesian node where $H[k] = H[\text{par}(k)]$ inspects a partial subset of occurrences and produces wrong answers!

#### `W2B-16`. `AtCoder ARC 151 E — Keep Being Substring` — `[JA]` *(Cohort 1 #15 / Cohort 2 #14)*
- **Statement & Constraints**: Given $A[1..N]$ and subarrays $X = A[l_1..r_1], Y = A[l_2..r_2]$ ($N \le 2.5 \times 10^5$), in one step you may append/prepend an element or delete an end element of current array $C$ ($|C| \ge 1$), keeping $C$ a contiguous subarray of $A$. Find the minimum steps from $X$ to $Y$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: If $\text{LCS}(X, Y) = L \ge 1$, we can shrink $X$ to that common substring and expand to $Y$ in $|X| + |Y| - 2L$ steps; if $L = 0$, we must transition between length-1 subarrays via adjacent elements in $A$.
  2. *Combinatorial Invariant*: Since any single transition on $A$ changes the longest common substring with $Y$ by at most $1$, the shortest path when $L \ge 1$ never needs to drop to length $1$ and switch locations.
  3. *Algorithmic Compilation*: Compute $L = \text{LCS}(X, Y)$ via SA-IS + `height` on $X \# Y$. If $L \ge 1$, return $|X| + |Y| - 2L$; otherwise run multi-source BFS from elements of $X$ to elements of $Y$ on the adjacency graph $A[k] \leftrightarrow A[k+1]$.
  4. *Boundary Pitfall*: Dropping to the empty string $C = \emptyset$ is forbidden (`|C| >= 1`).

#### `W2B-17`. `[TJOI2019] 甲苯先生和大中锋的字符串` (Luogu P5341) — `[ZH]` *(Cohort 1 #16)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$) and $K$, find the length $L$ that appears most frequently among all distinct substrings of $S$ that occur **exactly $K$ times**.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Count distinct substrings of each length $L$ whose equivalence class has size $K$.
  2. *Combinatorial Invariant*: A contracted Cartesian tree node $u$ of $H[2..N]$ with leaf count $R_u - L_u + 1 = K$ represents distinct substrings of every length $L \in (h_{p(u)}, h_u]$, each occurring $K$ times.
  3. *Algorithmic Compilation*: Build SA + $H$ + Cartesian tree. For every node (including leaves when $K = 1$) with size $K$ and $h_u > h_{p(u)}$, add $+1$ to a difference array on $(h_{p(u)}, h_u]$.
  4. *Boundary Pitfall*: When $K = 1$, remember to process the $N$ leaf edges $(\max(H[x], H[x+1]), N - \text{SA}[x] + 1]$.

#### `W2B-18`. `CF 427D — Match & Catch` — `[EN]` *(Cohort 2 #15)*
- **Statement & Constraints**: Given $S_1, S_2$ ($N \le 5 \times 10^5$), find the length of the shortest substring $t$ that occurs **uniquely** ($\text{occ}_{S_1}(t) = \text{occ}_{S_2}(t) = 1$) in both $S_1$ and $S_2$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Exact occurrence count $1$ in both strings, minimizing length.
  2. *Combinatorial Invariant*: On the Cartesian tree of $H$ for $S_1 \# S_2$, a node $u$ has $\text{cnt}_1(u) = \text{cnt}_2(u) = 1$ iff its SA interval has width $2$ (an adjacent pair $\text{SA}[k-1], \text{SA}[k]$ from opposite strings) with $H[k] > h_{p(u)} = \max(H[k-1], H[k+1])$. The **shortest** substring in this class has length $h_{p(u)} + 1$!
  3. *Algorithmic Compilation*: Scan $k = 2 \dots |S_1|+|S_2|+1$; whenever $\text{SA}[k-1]$ and $\text{SA}[k]$ belong to different strings and $H[k] > \max(H[k-1], H[k+1])$, update answer with $\max(H[k-1], H[k+1]) + 1$.
  4. *Boundary Pitfall*: Taking $H[k]$ (longest string in the node) instead of $\max(H[k-1], H[k+1]) + 1$ (shortest string in the node).

#### `W2B-19`. `[SCOI2012] 喵星球上的点名` (Luogu P2336) — `[ZH]` *(Cohort 2 #16)*
- **Statement & Constraints**: Given $N$ cats (each with a first and last name integer string) and $M$ query patterns ($\sum \text{len} \le 10^5$), find (1) for each pattern, how many distinct cats contain it, and (2) for each cat, how many patterns it matched.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Multi-pattern substring containment coupled with range distinct-color counting and dual point-in-interval counting on SA.
  2. *Combinatorial Invariant*: In the Generalized SA of all cat names and queries, each query $P_q$ spans a contiguous SA interval $[L_q, R_q]$. Sweeping right endpoint $r$ while tracking `last[c]` (the latest SA index of cat $c$) means cat $c$ is newly covered by $[L_q, R_q]$ whenever $\text{last}_{\text{old}}[c] < L_q \le \text{last}_{\text{new}}[c]$ and $R_q \ge \text{last}_{\text{new}}[c]$.
  3. *Algorithmic Compilation*: Sort query intervals $[L_q, R_q]$ by $R_q$. Maintain a Fenwick tree for distinct cat counts (Question 1) and a difference/Fenwick array over query-sorted order for each cat's interval coverage between consecutive occurrences $(\text{last}_{\text{old}}[c], i]$ (Question 2).
  4. *Boundary Pitfall*: Both the first name and last name of cat $c$ share the same color ID $c$.

#### `W2B-20`. `[TJOI2015] 弦论` (Luogu P3975) — `[ZH]` *(Cohort 2 #22)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), $t \in \{0, 1\}$, and $K \le 10^{18}$, output the $K$-th lexicographically smallest substring of $S$ (counting distinct substrings if $t = 0$, or counting with multiplicity if $t = 1$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Substring `Select(K)` in both distinct ($t=0$) and multiplicity-weighted ($t=1$) modes.
  2. *Combinatorial Invariant*: For $t = 0$, suffix $\text{SA}[i]$ contributes $(N - \text{SA}[i] + 1) - H[i]$ new distinct substrings (`§4.1.1`). For $t = 1$, on the Cartesian tree of $H$ (or SAM), each node $u$ with interval $[L_u, R_u]$ contributes $(h_u - h_{p(u)}) \cdot (R_u - L_u + 1)$ total occurrences in DFS lexicographical order!
  3. *Algorithmic Compilation*: Traverse the Cartesian tree of $H$ (or SAM DAG) accumulating subtree substring counts and jump to the $K$-th substring in $O(N)$ time.
  4. *Boundary Pitfall*: Output `-1` when $K$ exceeds the total number of substrings.

#### `W2B-21`. `QOJ / Universal Cup — Substring Lexicographical Rank & Select Dictionary` — `[EN]` *(Cohort 1 #30 / Cohort 2 §72.4)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^5$) and $Q \le 3 \times 10^5$ queries: (Type 1) Given $S[l..r]$, output its 1-based lexicographical rank among all distinct substrings of $S$; (Type 2) Given rank $K$, output the endpoints $(l, r)$ of the $K$-th distinct substring in $O(\log N)$ time.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Direct implementation of Basic Substring Dictionary `Rank(S[l..r])` and `Select(K)` (`§4.1.1`).
  2. *Combinatorial Invariant*: The first (leftmost) occurrence of $S[l..r]$ in SA order is at $k_0 = L_{\text{SA}}(S[l..r]) \le \text{rk}[l]$, where $S[l..r]$ is the $(r - l + 1 - H[k_0])$-th new distinct prefix introduced by $\text{SA}[k_0]$.
  3. *Algorithmic Compilation*: Precompute $\text{pref}[k] = \sum_{i=1}^k (N - \text{SA}[i] + 1 - H[i])$. For `Rank(S[l..r])`, binary search on RMQ of $H$ to find $k_0 \le \text{rk}[l]$ and return $\text{pref}[k_0-1] + (r - l + 1 - H[k_0])$. For `Select(K)`, binary search $\text{pref}$ for $k$.
  4. *Boundary Pitfall*: Using $\text{rk}[l]$ directly instead of the leftmost SA index $k_0 = L_{\text{SA}}(S[l..r])$ fails whenever $S[l..r]$ also occurs at another suffix $\text{SA}[k_0]$ with $k_0 < \text{rk}[l]$, where $H[\text{rk}[l]] \ge r - l + 1$!

---

### Tier 3: Advanced (`W2B-22` to `W2B-32` — Harmonic Checkpoints, 2D `(SA, SA^R)`, Suffix Tree HLD/Centroid & Upward Tree SA)

#### `W2B-22`. `[NOI2016] 优秀的拆分` (Luogu P1117 / UOJ #219) — `[ZH]` *(Cohort 1 #18 / Cohort 2 #21)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 3 \times 10^4$, multi-test), count the number of decompositions $S[i..j] \cdot S[j+1..k] = AA \cdot BB$ into two adjacent squares.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Compute $\text{pre}[j]$ (squares $AA$ ending at $j$) and $\text{suf}[j+1]$ (squares $BB$ starting at $j+1$) in $O(N \log N)$ time.
  2. *Combinatorial Invariant*: For a fixed half-length $L = |A|$, place checkpoints at multiples $L, 2L, 3L, \dots$. Every square $AA$ of length $2L$ covers **exactly two consecutive checkpoints** $x = mL$ and $y = (m+1)L$! Let $l_{\text{ext}} = \min(\text{LCSuf}(x, y), L)$ and $r_{\text{ext}} = \min(\text{LCE}(x, y), L)$. Whenever $l_{\text{ext}} + r_{\text{ext}} - 1 \ge L$, all shifts in $[x - l_{\text{ext}} + 1, x + r_{\text{ext}} - L]$ start a valid square of length $2L$.
  3. *Algorithmic Compilation*: Build SA + $O(1)$ RMQ on $S$ and $S^R$. Loop over all $\sum_{L=1}^{N/2} \lfloor N/L \rfloor = O(N \log N)$ checkpoint pairs and apply range additions to difference arrays for $\text{pre}$ and $\text{suf}$.
  4. *Boundary Pitfall*: Capping $l_{\text{ext}} \le L$ and $r_{\text{ext}} \le L$ is mandatory so periodic runs of length $\ge 3L$ are not double-counted by adjacent checkpoint pairs!

#### `W2B-23`. `CF 1098F — Ж-function` — `[EN]` *(Cohort 1 #19 / Cohort 2 #19)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[l, r]$, compute $\sum_{i=l}^r \text{LCP}(S[l..r], S[i..r]) = \sum_{i=l}^r \min\big(\text{LCE}(l, i), \; r - i + 1\big)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Sum of the internal Z-array of $S[l..r]$, coupling Suffix Tree LCA depth $\text{LCE}(l, i)$ with linear right-boundary clipping $r - i + 1$.
  2. *Combinatorial Invariant*: On the Suffix Tree (or Reversed SAM Link Tree), let $w = \text{LCA}(u_l, u_i)$ have string depth $L(w) = \text{LCE}(l, i)$. The summand $\min(L(w), r - i + 1)$ splits at $i + L(w) - 1 \le r$ (contributing $L(w)$) vs. $i + L(w) - 1 > r$ (contributing $r - i + 1$).
  3. *Algorithmic Compilation*: Apply Centroid Decomposition or Heavy-Light Decomposition on the Suffix Tree (`§4.2`, Methods 2 & 3), reducing both cases to 2D Fenwick tree range sums in $O((N+Q)\log^2 N)$ time.
  4. *Boundary Pitfall*: Separate the $i = l$ term ($r - l + 1$) first; on heavy chains, run two passes (for $u_i$ entering above $u_l$ where $L(w) = \text{len}(w_i)$, and below $u_l$ where $L(w) = \text{len}(w_l)$).

#### `W2B-24`. `CF 700E — Cool Slogans` — `[EN]` *(Cohort 1 #20)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$), find the maximum $k$ such that there exist strings $s_1, \dots, s_k$ where each $s_{i-1}$ occurs at least twice in $s_i$ and $s_k$ is a substring of $S$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Top-down DP on the Suffix Tree / SAM Link Tree checking whether ancestor $u$ occurs $\ge 2$ times inside descendant $v$.
  2. *Combinatorial Invariant*: Pick any occurrence end-position $\text{pos}(v)$ of $v$. Ancestor $u$ (at its full length $\text{len}(u)$) occurs at least twice in $S[\text{pos}(v)-\text{len}(v)+1 .. \text{pos}(v)]$ iff $u$ has another occurrence ending in $[\text{pos}(v) - \text{len}(v) + \text{len}(u), \; \text{pos}(v) - 1]$ (or starting in $[\text{pos}_{\text{start}}(v) + 1, \; \text{pos}_{\text{start}}(v) + \text{len}(v) - \text{len}(u)]$ on SA!).
  3. *Algorithmic Compilation*: On the Cartesian tree of $H$ (or SAM Link Tree), maintain the highest ancestor $u$ with the current $dp$ value and test occurrence in $v$ via a Persistent Segment Tree over $\text{SA}$ (or Segment Tree Merge) in $O(N \log N)$.
  4. *Boundary Pitfall*: Always test $u$ at its **maximum** length $\text{len}(u)$ in its equivalence class.

#### `W2B-25`. `[十二省联考 2019] 字符串问题` (Luogu P5284) — `[ZH]` *(Cohort 1 #21)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$), $N_a$ substrings $A_i$, $N_b$ substrings $B_j$, and $M$ explicit edges $A_i \to B_j$; furthermore, every $B_j$ has a directed edge to every $A_k$ that has $B_j$ as a prefix. Find the maximum total length of $A$-strings on a path (or `-1` if a cycle exists).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Implicit prefix-containment graph over substrings $B_j \to A_k$ ($\text{LCE}(l_{b,j}, l_{a,k}) \ge |B_j|$ and $|A_k| \ge |B_j|$).
  2. *Combinatorial Invariant*: On the Suffix Tree of $S$ (or SA intervals via Persistent Segment Tree optimization), $B_j$ is a prefix of $A_k$ iff $A_k$'s locus lies in the subtree of $B_j$'s locus (with $|A_k| \ge |B_j|$ if they land on the same compressed edge).
  3. *Algorithmic Compilation*: Locate the locus of every $A_i$ and $B_j$ via binary lifting on the Suffix Tree, sort substrings on the same edge by length ($B_j$ before $A_k$ on ties $|B_j| = |A_k|$), link tree edges top-down, and compute DAG longest paths via topological sort in $O((N + N_a + N_b)\log N)$.
  4. *Boundary Pitfall*: When $|B_j| = |A_k|$ on the same Suffix Tree edge, $B_j = A_k$ IS a prefix of $A_k$, so $B_j$ must be ordered **before** $A_k$!

#### `W2B-26`. `CF 666E — Forensic Examination` — `[EN]` *(Cohort 1 #22 / Cohort 2 #23)*
- **Statement & Constraints**: Given $S[1..|S|]$ ($|S| \le 5 \times 10^5$), $M$ dictionary strings $T_1, \dots, T_M$ ($\sum |T_i| \le 5 \times 10^4$), and $Q \le 5 \times 10^5$ queries $(l, r, p_l, p_r)$: find $k \in [l, r]$ maximizing the occurrences of $S[p_l..p_r]$ in $T_k$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Substring locus lookup for $S[p_l..p_r]$ coupled with range-mode query over dictionary IDs $k \in [l, r]$.
  2. *Combinatorial Invariant*: In the Generalized SA (or GSAM) of $S \# T_1 \# \dots \# T_M$, suffixes sharing prefix $S[p_l..p_r]$ form a contiguous SA interval $[L(p_l, p_r), R(p_l, p_r)]$ (a node in the Cartesian tree of $H$).
  3. *Algorithmic Compilation*: Find $[L, R]$ via RMQ binary search around $\text{rk}[p_l]$ (or binary lifting on GSAM), and query Segment Tree Merge on the Cartesian tree (or Mo's algorithm on SA) for $\arg\max_{k \in [l, r]} \text{cnt}[k]$.
  4. *Boundary Pitfall*: When the maximum occurrence count in $[l, r]$ is `0`, output $k = l$ (not `0`).

#### `W2B-27`. `Universal Cup / Gym 102900E / LOJ 6071 — 1-Mismatch & Wildcard Split Matching via 2D (SA, SA^R)` — `[EN]`/`[ZH]`/`[JA]` *(Cohort 1 #23 / Cohort 2 #24)*
- **Statement & Constraints**: Given text $S[1..N]$ ($N \le 2 \times 10^5$) and pattern queries $P_q$ ($\sum |P_q| \le 2 \times 10^5$), count occurrences of $P_q$ in $S$ with **at most 1 mismatch** (or wildcard split $P_1 \cdot ? \cdot P_2$, `JOI 2018 Spring Camp`).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Splitting at the mismatch index $k \in [1..|P_q|]$ requires simultaneous prefix match $P_q[1..k-1]$ ending at $i-1$ and suffix match $P_q[k+1..m]$ starting at $i+1$.
  2. *Combinatorial Invariant*: By the 2D Suffix-Prefix Point Grid (`§4.1`), text position $i$ matches iff $p_i = (\text{rk}_{S^R}[N-i+2], \text{rk}_S[i+1]) \in [L^R(k), R^R(k)] \times [L(k), R(k)]$.
  3. *Algorithmic Compilation*: Build SA on $S$ and $S^R$, find all prefix intervals $[L^R(k), R^R(k)]$ and suffix intervals $[L(k), R(k)]$ for $P_q$, and answer the $\sum |P_q|$ 2D rectangle queries via a Wavelet Matrix or offline Fenwick sweep in $O((N + \sum |P_q|)\log N)$.
  4. *Boundary Pitfall*: For $\le 1$ mismatch, exact matches (0 mismatches) are counted $|P_q|$ times (once per split index $k$); subtract $(|P_q| - 1) \cdot \text{occ}_{\text{exact}}(P_q)$!

#### `W2B-28`. `[ZJOI2017] 字符串` (Luogu P3763 — IPM & Prefix-Border Tie-Breaking View) — `[ZH]` *(Cohort 1 #24 / Cohort 2 #28)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[l, r]$, find the starting index $i \in [l, r]$ of the lexicographically minimal suffix of $S[l..r]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Truncating suffixes at $r$ flips the global SA order $\text{rk}[i] < \text{rk}[j]$ **if and only if** $S[j..r]$ is a proper prefix of $S[i..r]$!
  2. *Combinatorial Invariant*: Let $i_0 = \arg\min_{i \in [l, r]} \text{rk}[i]$ be the suffix in $[l, r]$ with minimal global rank in $S[1..N]$. Any suffix $S[j..r]$ ($j \in (i_0, r]$) that beats $S[i_0..r]$ when truncated at $r$ must be a **proper prefix (border)** of $S[i_0..r]$!
  3. *Algorithmic Compilation*: Find $i_0$ via a Persistent Segment Tree over SA (or RMQ on $\text{rk}[l..r]$), then inspect the $O(\log N)$ border APs of $S[i_0..r]$ via Dyadic IPM (`Theorem 4.1`) or Significant Suffixes (`Wave 1B`), testing only the shortest border in each AP.
  4. *Boundary Pitfall*: Counterexample $S = \texttt{"abad"}$, query $[1, 3] = \texttt{"aba"}$: globally $\text{suf}(1) = \texttt{"abad"} < \text{suf}(3) = \texttt{"ad"}$, yet inside $S[1..3]$, $S[3..3] = \texttt{"a"} < S[1..3] = \texttt{"aba"}$!

#### `W2B-29`. `ICPC WF 2019 D — First of Her Name` — `[EN]` *(Cohort 2 #20)*
- **Statement & Constraints**: Given a rooted tree of $N \le 10^6$ nodes where each node prepends a character to its parent's string, and $Q$ query strings ($\sum |P_q| \le 10^6$), count for each $P_q$ how many tree nodes have a string starting with $P_q$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Upward tree paths $u \to \text{root}$ have a unique successor $\text{parent}(u)$ at every step.
  2. *Combinatorial Invariant*: Sorting all $N$ upward tree paths via Upward Tree SA-IS or rank-pair doubling (`§2.2`, Step 4) maps every query prefix $P_q$ to a contiguous interval $[L_q, R_q]$ in the Tree Suffix Array.
  3. *Algorithmic Compilation*: Build the Tree Suffix Array (or backward Burrows–Wheeler / Wheeler DFA range transition $c \cdot [L, R] \to [L', R']$ in $O(1)$ per character!) to find $[L_q, R_q]$ in $O(|P_q|)$ or $O(|P_q| \log N)$ time.
  4. *Boundary Pitfall*: Multiple tree nodes can have identical upward strings to the root; assign identical ranks to ties during construction.

#### `W2B-30`. `AtCoder AGC 047 B — First Second` — `[JA]` *(Cohort 1 #31 / Cohort 2 #29)*
- **Statement & Constraints**: Given $N$ strings $S_1, \dots, S_N$ ($\sum |S_i| \le 10^6$), in one operation you may delete either the 1st or 2nd character of a string. Count pairs $(i, j)$ ($i \ne j$) such that $S_i$ can be reduced to $S_j$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Deleting the 1st or 2nd character preserves the last $|S_j|-1$ characters $S_j[2..m]$ untouched while allowing the 1st character $S_j[1]$ to be **any** character from the prefix $S_i[1 .. |S_i|-m+1]$.
  2. *Combinatorial Invariant*: $S_i \to^* S_j$ iff $S_j[2..m]^R$ is a prefix of $S_i^R$ AND character $S_j[1]$ appears in the remaining suffix of $S_i^R$.
  3. *Algorithmic Compilation*: Insert all reversed strings $S_i^R$ into a Trie / Suffix Tree, maintaining a 26-bit mask of characters present in the remaining prefix of $S_i$ as you walk down $S_i^R$, and query at the node of $S_j[2..m]^R$ for bit $S_j[1]$.
  4. *Boundary Pitfall*: Subtract $i = j$ self-pairs.

#### `W2B-31`. `POI 2012 — Prefixuffix (Prefiksufiks)` — `[EN]` *(Cohort 2 #30)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6$), find the longest **cyclic border** of $S$—a prefix $S[1..k]$ and suffix $S[N-k+1..N]$ ($k \le N/2$) that are cyclic shifts of each other ($S[1..k] = U V$ and $S[N-k+1..N] = V U$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $U$ is an exact border of $S[1..N]$, and $V$ is an exact border of the stripped interior $S[|U|+1 .. N-|U|]$!
  2. *Combinatorial Invariant*: Let $f(i)$ be the longest exact border of $S[i .. N-i+1]$ that does not overlap the center. When expanding $(i+1, N-i) \to (i, N-i+1)$ by 1 character at both ends, any valid border of $S[i..N-i+1]$ stripped of its first and last character is a valid border of $S[i+1..N-i]$, so **$f(i) \le f(i+1) + 2$**!
  3. *Algorithmic Compilation*: Sweep $i$ from $\lfloor N/2 \rfloor$ down to $1$: start at $\ell = \min(\lfloor N/2 \rfloor - i + 1, f(i+1) + 2)$ and decrement $\ell$ while $\text{LCE}(i, N - i + 2 - \ell) < \ell$. By amortization, $\ell$ decreases at most $2 \cdot (N/2) = N$ times $\implies O(N)$ total time! Then maximize $|U| + f(|U|+1)$ over all exact borders $U$ of $S$.
  4. *Boundary Pitfall*: Always cap $f(i) \le \lfloor N/2 \rfloor - i + 1$ so the prefix and suffix never overlap at the center.

#### `W2B-32`. `AtCoder AGC 060 D — Same Descent Set` (SA-IS $L/S$ Descent Permutation Bridge) — `[JA]` *(Cohort 2 #33)*
- **Statement & Constraints**: Count pairs of permutations $(P, Q)$ of $(1..N)$ ($N \le 2 \times 10^5$) sharing the same descent set $\{i : P_i > P_{i+1}\} = \{i : Q_i > Q_{i+1}\}$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Direct combinatorial manifestation of Definition 2.1: in SA-IS, position $i$ is $L$-type iff $\text{rk}[i] > \text{rk}[i+1]$ (a descent in the inverse suffix array permutation $\text{rk}$), and $S$-type iff $\text{rk}[i] < \text{rk}[i+1]$ (an ascent in $\text{rk}$), with LMS positions $S^*$ marking the valleys!
  2. *Combinatorial Invariant*: Inclusion-exclusion over forced descent runs decomposes the permutation pair into independent contiguous blocks, solvable via divide-and-conquer / FPS NTT.
  3. *Algorithmic Compilation*: Formulate the EGF of matching descent runs and invert via polynomial divide-and-conquer in $O(N \log^2 N)$.
  4. *Boundary Pitfall*: Cross-reference with Wave 5A (`String Inequalities & Descent Graphs`) for general SA restoration from $L/S$ types.

---

### Tier 4: Mastery (`W2B-33` to `W2B-42` — `[BJWC2018]`, Dominant Pairs, Suffix Balanced Trees `后缀平衡树`, SCDAWG & Grandmasters)

#### `W2B-33`. `[BJWC2018] Border 的四种求法` (Luogu P4482) — `[ZH]` *(Cohort 1 #17 / Cohort 2 #25)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[l, r]$, output the length of the longest proper border of $S[l..r]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Flagship internal substring border problem where $i = l + b - 1 \in [l, r-1]$ appears on both sides of $i - \text{len}(\text{LCA}_{\text{SAM}}(u_r, u_i)) \le l - 1$.
  2. *Combinatorial Invariant*: Solved by any of the **Six Canonical Methods** reconciled in `§4.2` (Method 1: Dyadic $2^m$ IPM AP intersection via Theorem 4.1; Method 2: SAM Link-Tree HLD + SegTree Merge; Method 3: Link-Tree Centroid Decomposition; Method 4: DSU-on-Tree; Method 5: $\sqrt{N}$ SA-rank split; Method 6: Runs + short border fallback).
  3. *Algorithmic Compilation*: Implement Method 1 ($O((N+Q)\log^2 N)$ online via Persistent Segment Tree over SA finding min, 2nd min, max occurrence of $P_m$ and $Q_m$, then $O(1)$ AP intersection) or Method 2 ($O((N+Q)\log^2 N)$ via HLD + SegTree Merge predecessor queries).
  4. *Boundary Pitfall*: Clip $i \le r - 1$ to exclude the improper border $b = r - l + 1$, and handle APs of size $\le 2$ individually before using step $d = x_2 - x_1$.

#### `W2B-34`. `[UOJ / LOJ / QOJ] 区间最长重复子串 (Dominant Pairs LCP on Suffix Tree)` — `[ZH]` *(Cohort 2 #27)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[l, r]$, compute $\max_{l \le i < j \le r} \min\big(r - j + 1, \; \text{LCP}(\text{suf}(i), \text{suf}(j))\big)$—the length of the longest substring occurring at least twice inside $S[l..r]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Range query $[l, r]$ in original string index space maximizing boundary-clipped $\text{LCP}(\text{suf}(i), \text{suf}(j))$.
  2. *Combinatorial Invariant*: By **Theorem 3.2 (The Suffix Tree Dominant Pair Lemma)**, running DSU-on-Tree over the Min-Cartesian tree of $H[2..N]$ extracts at most $2N \log_2 N$ dominant triples $(i, j, \ell_u)$ ($i < j$) that provably dominate all $\binom{N}{2}$ suffix pairs for every query $[l, r]$!
  3. *Algorithmic Compilation*: Extract the $\le 2N \log_2 N$ triples $(i, j, \ell_u)$. Split each triple's contribution $\min(r - j + 1, \ell_u)$ into Regime 1 ($j + \ell_u - 1 \le r$, value $\ell_u$) and Regime 2 ($j \le r < j + \ell_u - 1$, value $r - j + 1$), and answer all queries offline by sweeping $l$ from $N$ down to $1$ with two Segment/Fenwick Trees in $O(N \log^2 N + Q \log N)$ time.
  4. *Boundary Pitfall*: Forgetting Regime 2 (or forgetting to cap $\ell_u$ by $r - j + 1$) either misses valid repeats whose global LCP extends past $r$, or counts characters outside $[l, r]$!

#### `W2B-35`. `CF 1043G — Speckled Band` — `[EN]` *(Cohort 2 #26)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5, |\Sigma| = 26$) and $Q \le 2 \times 10^5$ queries $[l, r]$, partition $S[l..r]$ into segments and assign each distinct segment string a color such that no two adjacent segments share the same color, minimizing the total number of colors used (or `-1` if impossible).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: The answer is always in $\{-1, 1, 2, 3, 4\}$!
     - `-1`: All characters in $S[l..r]$ are distinct ($r - l + 1 \le 26$, checkable in $O(1)$ via prefix counts).
     - `1`: $S[l..r] = w^d$ ($d \ge 2$) is a pure periodic power (check prime divisors of $n = r - l + 1$ via $O(1)$ $\text{LCE}(l, l + n/p) \ge n - n/p$).
     - `2`: $S[l..r]$ has the form $A B A$ (**any non-empty border**!), $A A B$ (starts with a square), or $B A A$ (ends with a square).
     - `3`: $S[l]$ repeats in $S[l+1..r]$, $S[r]$ repeats in $S[l..r-1]$, or $S[l..r]$ contains any square $AA$ strictly inside $[l, r]$.
     - `4`: Always achievable otherwise!
  2. *Combinatorial Invariant*: Precompute the shortest square starting at each $i$ ($\text{min\_sq\_L}[i]$) and ending at each $j$ ($\text{min\_sq\_R}[j]$) in $O(N \log N)$ using the harmonic checkpoints of `W2B-22` (`[NOI2016] 优秀的拆分`), and test whether $S[l..r]$ has **any** border in $O(\sqrt{N})$ via Method 5 (`§4.2`) or $O(\log N)$ via Method 1 (Dyadic IPM)!
  3. *Algorithmic Compilation*: Precompute $\text{min\_sq\_L}, \text{min\_sq\_R}$, RMQ over $\text{min\_sq\_R}$ for internal squares, and run the 5-way cascade per query.
  4. *Boundary Pitfall*: Checking only $A B A$ (border) for answer `2` and forgetting $A A B$ ($\text{min\_sq\_L}[l] \le r$) or $B A A$ ($\text{min\_sq\_R}[r] \ge l$).

#### `W2B-36`. `[BZOJ 3682] Phorni` (Suffix Balanced Tree `后缀平衡树` + Segment Tree) — `[ZH]` *(Cohort 1 #25 / Cohort 2 #17)*
- **Statement & Constraints**: Maintain a string $S$ under online **encrypted** `push_front(c)` operations ($N \le 5 \times 10^5$) and maintain an array $P[1..M]$ of suffix indices under point updates $P[x] \leftarrow v$ and range queries asking for $x \in [L, R]$ minimizing $\text{suf}(P[x])$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Encrypted online `push_front(c)` coupled with $O(1)$ suffix comparison inside a Segment Tree over $P[1..M]$.
  2. *Combinatorial Invariant*: By **Theorem 5.3 (Suffix Balanced Tree Tag Invariant)**, maintaining all suffixes in an $\alpha = 0.75$ Scapegoat Tree with 64-bit integer midpoint tags $\text{tag}[x] \in [0, 2^{62}]$ allows comparing $\text{suf}(n) \lessgtr \text{suf}(u)$ during insertion in $O(1)$ via $(c, \text{tag}[n-1]) \lessgtr (S[u], \text{tag}[u-1])$, and comparing any two suffixes in the Segment Tree in $O(1)$ via $\text{tag}[P[x]] < \text{tag}[P[y]]$!
  3. *Algorithmic Compilation*: Insert each new suffix into the Scapegoat Suffix Balanced Tree in $O(\log N)$ amortized time; update/query the Segment Tree over $P[1..M]$ reading `tag[P[x]]` on the fly.
  4. *Boundary Pitfall*: Because Scapegoat rebuilds preserve the relative order of all existing tags, the Segment Tree over $P[1..M]$ **never** needs to be rebuilt when a Scapegoat subtree rebuilds—just look up `tag[P[x]]` dynamically during Segment Tree comparisons!

#### `W2B-37`. `[BZOJ 4768] wxh loves substring` / `Luogu P6164 【模板】后缀平衡树` — `[ZH]` *(Cohort 1 #26 / Cohort 2 #18)*
- **Statement & Constraints**: Maintain a string $S$ online under **encrypted** front-insertions `push_front(c)`, front-deletions `pop_front()`, and pattern occurrence queries asking how many times query string $T$ occurs in $S$ ($\sum |T| \le 10^6, Q \le 2 \times 10^5$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Online encrypted front-insertions and front-deletions with pattern counting.
  2. *Combinatorial Invariant*: Prepending $c$ inserts one suffix $\text{suf}(n)$ into the Suffix Balanced Tree; deleting the front character removes $\text{suf}(n)$. Pattern $T$ occurs at $\text{suf}(u)$ iff $T$ is a prefix of $\text{suf}(u)$, which corresponds to the contiguous BST range $(T^-, T \cdot \infty)$ in the Suffix Balanced Tree!
  3. *Algorithmic Compilation*: Maintain the Scapegoat Suffix Balanced Tree with lazy deletion. To count occurrences of $T$, insert a temporary virtual suffix for $T$ (or walk down the BST comparing $T$ character-by-character in $O(|T| \log N)$, or build $T$ backwards in $O(|T| + \log N)$!).
  4. *Boundary Pitfall*: Wait—how do you query $T$ in $O(|T| + \log N)$ instead of $O(|T| \log N)$? Instead of comparing $T$ from scratch at each BST node, we only care about suffixes of $S$, NOT arbitrary external strings, UNLESS we just compare $T$ at each of the $O(\log N)$ BST nodes: to avoid $O(|T| \log N)$ worst-case character comparisons when walking down the BST for external pattern $T$, track the LCP with the current BST interval bounds $(l_{\text{bst}}, r_{\text{bst}})$ or use the Suffix Balanced Tree's $O(1)$ tag if $T$ is built, or simply note $\sum |T|$ with LCP skipping takes $O(|T| + \log N)$!

#### `W2B-38`. `[THUPC 2019 / QOJ] 双向后缀平衡树 (Online Encrypted Deque Distinct Substrings)` — `[ZH]` *(Cohort 2 #31)*
- **Statement & Constraints**: Start with $S = \varepsilon$; support $Q \le 2 \times 10^5$ online **encrypted** operations: `push_front(c)` and `push_back(c)`, outputting the number of distinct substrings of $S$ after each step.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: True bi-directional online distinct substring maintenance where encryption forbids offline deque simulation (`Filter 3` in `§5.2`).
  2. *Combinatorial Invariant*: By **Theorem 5.2 (Ukkonen–Weiner Frontier Duality)** and **Theorem 5.3 (Hash-Free Suffix Balanced Tree)**, `push_front(c)` increases distinct substrings by $|S| - |L_{\max}(cS)|$, and `push_back(c)` increases distinct substrings by $|S| - |R_{\max}(Sc)|$.
  3. *Algorithmic Compilation*: Maintain the online **Symmetric Compact DAWG (SCDAWG)** (`Theorem 5.1`), or maintain coupled forward/backward Suffix Balanced Trees where the newly added boundary character updates the active frontier.
  4. *Boundary Pitfall*: Never assume a single Suffix Balanced Tree can handle `push_back(c)` without updating border suffixes (`"aa" -> "aab"` flip counterexample!).

#### `W2B-39`. `[NOI2018] 你的名字` (Luogu P4770 — SA + Persistent SegTree + `height` Formulation) — `[ZH]` *(Cohort 1 #27)*
- **Statement & Constraints**: Given $S[1..|S|]$ ($|S| \le 5 \times 10^5$) and $Q$ queries $(T_q, l_q, r_q)$ with $\sum |T_q| \le 5 \times 10^5$, count how many distinct substrings of $T_q$ do **not** occur in $S[l_q..r_q]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Dual to the Wave 2A SAM + SegTree Merge solution, this problem admits a pure Wave 2B **Suffix Array + Persistent Segment Tree** solution.
  2. *Combinatorial Invariant*: For each starting position $i \in [1..|T_q|]$ of $T_q$, let $\text{lim}[i]$ be the longest prefix of $T_q[i..|T_q|]$ occurring in $S[l_q..r_q]$. Since $\text{lim}[i] \ge \text{lim}[i-1] - 1$, we can maintain the SA interval of $T_q[i .. i+\text{lim}[i]-1]$ in $\text{SA}_S$ and test whether $\text{lim}[i]$ can increment by querying the Persistent Segment Tree over $\text{SA}_S$ on index range $[l_q, r_q - L + 1]$!
  3. *Algorithmic Compilation*: Compute $\text{lim}[1..|T_q|]$, build SA-IS + $H_{T_q}$ on $T_q$, and return $\sum_{k=1}^{|T_q|} \max\big(0, \; (|T_q| - \text{SA}_{T_q}[k] + 1) - \max(H_{T_q}[k], \text{lim}[\text{SA}_{T_q}[k]])\big)$.
  4. *Boundary Pitfall*: Clipping the valid starting index in $S$ to $[l_q, r_q - L + 1]$ is mandatory.

#### `W2B-40`. `CF 1063F — String Journey` — `[EN]` *(Cohort 1 #28 / Cohort 2 #32)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), find the maximum $k$ such that there exist disjoint substrings $t_1, t_2, \dots, t_k$ from left to right where $|t_i| = k - i + 1$ and each $t_{i+1}$ is a proper substring of $t_i$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: By greedy truncation, $|t_i| = k - i + 1$ and $t_{i+1}$ is either the prefix $t_i[1..|t_i|-1]$ or the suffix $t_i[2..|t_i|]$.
  2. *Combinatorial Invariant*: Let $dp[i]$ be the maximum chain length starting at $S[i .. i+dp[i]-1]$. Because dropping the first character of $S[i..i+dp[i]-1]$ gives a valid chain at $i+1$, **$dp[i] \le dp[i+1] + 1$**!
  3. *Algorithmic Compilation*: Sweep $i$ from $N$ down to $1$, starting candidate $L = dp[i+1] + 1$ and decrementing $L$ while invalid. As $i + L$ decreases monotonically, insert completed $dp[j]$ ($j \ge i + L$) at position $\text{rk}[j]$ in a Segment Tree over $\text{SA}$. $L$ is valid iff the SA interval of $S[i..i+L-2]$ or $S[i+1..i+L-1]$ has $\max dp[j] \ge L - 1$. Total time: $O(N \log N)$.
  4. *Boundary Pitfall*: Never insert $dp[j]$ into the Segment Tree before the pointer $i + L$ reaches $j$, or $t_i$ and $t_{i+1}$ will overlap!

#### `W2B-41`. `[CTS2019] 重复 (Repeats)` (Luogu P5401) — `[ZH]` *(Cohort 1 #29)*
- **Statement & Constraints**: Given $S[1..n]$ ($n \le 2000$) and $m \le 2000$, count length-$m$ strings $T$ over $|\Sigma| = 26$ such that at least one cyclic shift of $T$ contains a substring lexicographically smaller than $S$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Complement counting over infinite periodic extensions $T^\infty$ where every suffix is $\ge_{\text{lex}} S$.
  2. *Combinatorial Invariant*: On the KMP / DAWG prefix automaton of $S$, forbidding any transition $c < S[\text{matched}+1]$ leaves a pruned DFA where every state has at most **one** outgoing transition that falls back along the border chain and remaining transitions returning to the root!
  3. *Algorithmic Compilation*: Count closed walks of length $m$ on the pruned DFA by decomposing into root-return cycles and the unique non-root cycle in $O(nm)$ time.
  4. *Boundary Pitfall*: Accounting for walks that never visit the root when wrapping around $T^\infty$.

#### `W2B-42`. `QOJ / ICPC WF — Symmetric Compact DAWG & Bi-Directional Maximal Repeats` — `[EN]`/`[JA]` *(Cohort 1 #32)*
- **Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$), identify all **maximal repeats** (substrings $\overleftrightarrow{u}$ occurring $\ge 2$ times such that neither $c\overleftrightarrow{u}$ nor $\overleftrightarrow{u}d$ has the same occurrence count as $\overleftrightarrow{u}$) and compute statistics over the vertices of $\text{SCDAWG}(S)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Direct characterization of the bi-maximal vertices $\overleftrightarrow{u}$ of the **Symmetric Compact DAWG** (`Theorem 5.1`).
  2. *Combinatorial Invariant*: Every internal node $u$ of the contracted Min-Cartesian tree of $H[2..N]$ is already **right-maximal** (it is a branching node of $\mathcal{T}_{\text{ST}}(S)$). It is also **left-maximal** iff the preceding characters $B[x] = S[\text{SA}[x] - 1]$ across its SA interval $x \in [L_u, R_u]$ are **not all identical** (or $\text{SA}[x] = 1 \in [L_u, R_u]$)!
  3. *Algorithmic Compilation*: Build SA-IS + $H$ + Cartesian tree on $S$, and precompute a prefix-difference sum on $B[x] = S[\text{SA}[x] - 1]$ (with $B[\text{rk}[1]] = \$_0$). Check in $O(1)$ per Cartesian node whether $B[L_u..R_u]$ is non-constant; each such node is an internal vertex of $\text{SCDAWG}(S)$!
  4. *Boundary Pitfall*: Treating $\text{SA}[x] = 1$ as having left character `'a'` instead of a unique sentinel $\$_0$ misses maximal repeats that touch the start of $S$.

---

## Section 8: Reconciled Quarantine Ledger (`R-2B-01` to `R-2B-13`) — Excluded Pure Template Problems

Per `AGENTS.md` and `PLAN.md` (`§2.2`), bare template and library-verification problems are strictly quarantined from textbook chapters and logged below (representing the full union of Cohort 1 `R-2B-01..10` and Cohort 2 `R-2B-01..08`):

| Quarantine ID | Platform & Problem Title | Source Cohort | Reason for Quarantine |
| :--- | :--- | :--- | :--- |
| **`R-2B-01`** | **Library Checker — `Suffix Array`** | Cohort 1 & 2 | Pure SA construction verification ($N \le 5 \times 10^5$); zero modeling beyond SA-IS template. |
| **`R-2B-02`** | **Library Checker — `Number of Substrings`** | Cohort 1 & 2 | Bare evaluation of $\binom{N+1}{2} - \sum_{k=2}^N \text{height}[k]$. |
| **`R-2B-03`** | **Luogu P3809 — `【模板】后缀排序`** | Cohort 1 & 2 | Standard Chinese Suffix Array template benchmark ($N = 10^6$). |
| **`R-2B-04`** | **Luogu P2408 — `不同子串个数`** | Cohort 1 | Identical to `R-2B-02`; pure distinct substring formula verification. |
| **`R-2B-05`** | **SPOJ `SUBST1` / `DISUBSTR` — `Distinct Substrings`** | Cohort 1 | Bare distinct substring count template. |
| **`R-2B-06`** | **SPOJ `SARRAY` — `Suffix Array`** | Cohort 1 | Pure suffix array construction benchmark. |
| **`R-2B-07`** | **UOJ #35 — `后缀排序`** | Cohort 1 & 2 | Standard template outputting `SA` and `height` arrays. |
| **`R-2B-08`** | **LOJ #111 — `后缀排序`** | Cohort 1 & 2 | Pure Suffix Array template verification. |
| **`R-2B-09`** | **Library Checker — `Longest Common Prefix`** | Cohort 1 | Bare LCE / `height` RMQ lookup verification. |
| **`R-2B-10`** | **SPOJ `LCS` — `Longest Common Substring`** | Cohort 1 | Bare two-string LCS via $S_1 \# S_2$ SA + `height` scan. |
| **`R-2B-11`** | **POJ 2774 — `Long Long Message`** | Cohort 2 | Identical to `R-2B-10`; bare two-string LCS template. |
| **`R-2B-12`** | **POJ 1743 — `Musical Theme`** | Cohort 2 | Classic introductory binary search on answer + `height` block min/max check. |
| **`R-2B-13`** | **AtCoder Practice2 I — `Number of Substrings`** | Cohort 2 | Bare ACL `atcoder::suffix_array` + `lcp_array` template verification. |

---

## Section 9: Phase 1.5 Curriculum Integration Blueprint & Wave 2B Validation Checklist

### 9.1 Recommendations for Phase 1.5 Post-Research Curriculum Architecture (`CURRICULUM_ARCHITECTURE.md`)

Based on our reconciled discovery corpus across Cohort 1, Cohort 2, and Cohort 3's blind-spot hunt, Wave 2B feeds directly into two core regions of the post-research textbook:
1. **Part III (Advanced Suffix Structures & Suffix Tree Duality — `Ch 12` & new split if needed)**:
   - **SA-IS as Locally Consistent Parsing + Fischer's Induced LCP + Upward Tree SA** (`§2`),
   - **Three-Way Isomorphism ($\mathcal{T}_{\text{ST}}(S) \leftrightarrow \mathcal{T}_{\text{SAM}}(S^R) \leftrightarrow \text{height}$ Cartesian Tree), Virtual Suffix Trees (`后缀树虚树`), and DSU-on-Tree Dominant Pairs (`后缀树支配对`)** (`§3`),
   - **Bi-Directional Suffix Structures — SCDAWG, Ukkonen–Weiner Frontier Duality, and Hash-Free Suffix Balanced Trees (`后缀平衡树`)** (`§5`).
2. **Part IV (Internal Pattern Matching & The Basic Substring Dictionary — `Ch 13` & `Ch 14`)**:
   - **Kociumaka's Basic Substring Dictionary** ($O(1)$ LCE, Concatenation LCE Walk, Substring `Rank`/`Select`, 2D $(\text{SA}, \text{SA}^R)$ Orthogonal Range Queries, and Kempa–Kociumaka $\tau$-Synchronizing Sets) (`§4.1`, `§4.3`),
   - **Bounded-Ratio IPM Arithmetic Progression Theorem & All Six Canonical Methods for Internal Border / Period Queries (`[BJWC2018] Border 的四种求法`)** (`§4.2`).

### 9.2 Wave 2B Master Validation Checklist

- [x] **Cross-Cohort Blind-Spot Audit Completed (`§1`)**: Explicitly documented all theorems, counterexamples, complexity proofs, and problems captured by Cohort 1 vs. Cohort 2, plus 4 frontier extensions hunted in Cohort 3.
- [x] **Pillar I — SA-IS & Induced LCP Reconciled (`§2`)**: Proved Lemma 2.2 ($L < S$ bucket split), Lemma 2.3 ($\le \lfloor N/2 \rfloor$ halving & $< 2N$ linear comparison sum), Theorem 2.4 (prefix-free LMS order homomorphism), `"mississippi$"` hand-checkable trace, Fischer's $O(N)$ induced LCP, `rk`-descent duality, and cyclic/generalized/tree adaptations.
- [x] **Pillar II — Virtual Suffix Trees & Dominant Pairs Reconciled (`§3`)**: Proved the 3-way Suffix Tree isomorphism, Theorem 3.1 (zero-tree substring Virtual Suffix Tree), and Theorem 3.2 ($\le 2N \log_2 N$ DSU-on-Tree Dominant Pairs on Suffix Trees).
- [x] **Pillar III — IPM, Basic Substring Dictionary & `[BJWC2018]` Reconciled (`§4`)**: Proved Theorem 4.1 (Kociumaka's Bounded-Ratio IPM AP Lemma), synthesized all **6 Canonical Methods** for `[BJWC2018] Border 的四种求法`, derived $O(1)$ Internal Shortest Period queries, and formalized Kempa–Kociumaka $\tau$-Synchronizing Sets.
- [x] **Pillar IV — Bi-Directional Suffix Structures Reconciled (`§5`)**: Proved Theorem 5.1 (SCDAWG two-sided closure commutativity $\overleftrightarrow{u}$), Theorem 5.2 (Ukkonen–Weiner frontier duality), and Theorem 5.3 (64-bit Scapegoat Suffix Balanced Tree `后缀平衡树` with hash-free $O(\log N)$ BST LCP bootstrapping).
- [x] **Master Problem Archive & Quarantine Ledger (`§6–§8`)**: Compiled **42 unique accepted non-template problems (`W2B-01`–`W2B-42`)** with full 4-Step Zero-Magic Analysis across 4 difficulty tiers and **13 quarantined template problems (`R-2B-01`–`R-2B-13`)**.
